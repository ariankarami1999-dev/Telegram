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
<p>@withyashar • 👥 466K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 02:20:54</div>
<hr>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ما
تا آخرین لحظه به مقاومت ادامه خواهیم داد
. بله، قطعاً با مشکلات اقتصادی مواجه هستیم، اما برای اینکه بتوانیم پابرجا بمانیم،
هر سختی و فشاری را تحمل خواهیم کرد و از آن عبور می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/withyashar/24095" target="_blank">📅 02:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24094">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ترامپ مدام می‌گفت «می‌خواهم برای مردم ایران هدیه بیاورم»، اما هدیه‌ای که آنها برای ما آوردند
موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی
بود. آنچه آنها واقعاً می‌خواهند انجام دهند،
ایجاد و تحریک حوادث و ناآرامی‌هایی در داخل کشور است که زمینه را برای فروپاشی نظام، جامعه و دولت فراهم کند.
@WarRoom</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/withyashar/24094" target="_blank">📅 02:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24093">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
اگر دولت کنونی آمریکا بخواهد
در چارچوب قوانین بین‌المللی
به توافق برسد، بسیار خوب. اما اگر نخواهد،
برای ما چه تفاوتی دارد که این اتفاق قبل از انتخابات آمریکا باشد یا بعد از آن؟
@WarRoom</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/withyashar/24093" target="_blank">📅 02:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
هرکس بخواهد اعتراض کند،
کاملاً حق دارد این کار را انجام دهد
. ما با بسیاری از این معترضان نشستیم و با آنها گفت‌وگو کردیم؛ اما
مسلح‌کردن اعتراضات و تبدیل آنها به ابزار درگیری، موضوع کاملاً متفاوتی است.
@WarRoom</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/withyashar/24092" target="_blank">📅 02:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
یکی از مشکلاتی که با آن مواجه هستیم این است که
پول ایران در چین مسدود شده است
. ما حتی نمی‌توانیم پول خودمان را از کشوری که در ازای آن به آن کالا صادر کرده‌ایم، خارج کنیم؛ چه رسد به اینکه بتوانیم از این منابع برای پرداخت به فرد یا طرف دیگری در نقطه‌ای دیگر از جهان استفاده کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/withyashar/24091" target="_blank">📅 02:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24090">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مسعود پزشکیان:
ما با ترامپ به توافق رسیدیم. آن توافق امضا شد و بر اساس همان توافق، ما آماده بودیم و همچنان مایل هستیم که مسیر را ادامه دهیم و چارچوب آن نیز مورد توافق قرار گرفته بود. ما تنگه هرمز را نبسته بودیم و تنگه باز بود؛ اما آنها بدون هیچ توجیه یا چارچوب قانونی به ما حمله کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/withyashar/24090" target="_blank">📅 02:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24089">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مسعود پزشکیان:
ما جنگ را انتخاب نکردیم؛ جنگ به ما تحمیل شد. ما به‌دنبال جنگ نیستیم، بلکه هر زمان به ما حمله شود، مجبوریم از خودمان دفاع کنیم. ما هرگز آغازکننده جنگ نبوده‌ایم، اما اگر آنها بخواهند به جنگ با ما ادامه دهند، با قدرت پاسخ خواهیم داد
@WarRoom</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/withyashar/24089" target="_blank">📅 02:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24088">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e58f2038.mp4?token=IDDvQRvkF2ooHd1S8XB4HRqitjAWsp1a6kWtGcVeMWjRMv7rNwejE3jnex0faPUjbolQ5G_Wf-JQZOGHPt3vb0IywLKbeioEuavC7Il8KwRqH7wx-EmFmuKGc4zUeCW0p_Oio6qC1NXQ9oqD3CV1Z2AYzxW0syAJ_BXR7iHUgan-K9xj3GXwTqb0gbAARG9-TjYUnxpwQAC51SlCc_HYKfHCZBDF3O9KbDzH7Q1XHPNOh8K44E80a4AkqTID-039n4I0864VXedN-78vzZ14AO45i5-jECKNmx10Hgnd_u4qz_jNshNFBZi6QCmZ_dIdotXTJPMh3w4kLxRa7b-8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e58f2038.mp4?token=IDDvQRvkF2ooHd1S8XB4HRqitjAWsp1a6kWtGcVeMWjRMv7rNwejE3jnex0faPUjbolQ5G_Wf-JQZOGHPt3vb0IywLKbeioEuavC7Il8KwRqH7wx-EmFmuKGc4zUeCW0p_Oio6qC1NXQ9oqD3CV1Z2AYzxW0syAJ_BXR7iHUgan-K9xj3GXwTqb0gbAARG9-TjYUnxpwQAC51SlCc_HYKfHCZBDF3O9KbDzH7Q1XHPNOh8K44E80a4AkqTID-039n4I0864VXedN-78vzZ14AO45i5-jECKNmx10Hgnd_u4qz_jNshNFBZi6QCmZ_dIdotXTJPMh3w4kLxRa7b-8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس‌نیوز: آقای رئیس‌جمهور، منظورم همان حادثه ژانویه است. شما جراح قلب هستید.
نیروهای امنیتی ایران چند ایرانی را کشتند؟
پزشکیان: ببینید چندان هم دشوار نیست. می‌توانید افرادی را به آنجا بفرستید تا حقیقت را مشخص و احراز کنند. آنچه فلان و بهمان نشریه در خارج از کشور گزارش می‌کند، با روایت دقیق و مستند از وقایع مطابقت ندارد. وقتی می‌گویند ۱۰ هزار نفر یا ۱۷ هزار نفر، چرا دست‌کم دو شماره ملی ارائه نمی‌کنند؟
@WarRoom</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/24088" target="_blank">📅 02:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24087">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/24087" target="_blank">📅 02:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24086">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c08c2421f.mp4?token=i4P10mX0evpwjP-W5EJ4QoJ66t-RTdOOs8uU-T7-hdNb7A_IQ4ugAyLsY5rQYyxdwEYjIuaekgYoQ7reUmQKFwk_MpKIQN7Y3gye7EAfrkdr9slrPKi6J1pGXX1NVVDotOkYswud44jzrBmyrQ9I9eopO0ys3WwUEXolgmJ_l8ynpEvNfOdtmkXp7SuRP8y2HppamftqJePydhE0JNizwv2_YjCZyP90JtX_y0OXFaj-ZC6wi9aw-YROV5Ze3uESz2ZXccZTdDlYAcLBfwgA3nMM6O4aB8Hrc-cSUVnCPGjHOEdBst2dm16m1uFdrRPEpM32-_fRRR78gjVvbK8f5GWpiMX4SPL0H28ExQM9_gZKb1uuTbHxCZLK0SVJ0iDaZ_FNs_bF6ncYlE6-u1oYqb2RI7fH2nQq69O9chi26LNNXwIixxWqjzZl9844QGFM1hMUiiOfo8pCrlTyhMf6jDgOIJzvavuwxAawxuBTaNwFuafmZAFuMrLE8xPmWtlwq21mX0F4fgZqJW4871qVy3ZbaqyXYeq4WJbS3zNFpbwBebMEHt1dVUObmV9W83z13DtPUn0sOhN8woLMusCvWlifwoP4qHlcCMAGU6DX9GReimgPiNggjQAUfhztuH0cSaQGQIf-4CsA-qrIqRWoVjjiaQ21xLr9zq6vfo-tQJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c08c2421f.mp4?token=i4P10mX0evpwjP-W5EJ4QoJ66t-RTdOOs8uU-T7-hdNb7A_IQ4ugAyLsY5rQYyxdwEYjIuaekgYoQ7reUmQKFwk_MpKIQN7Y3gye7EAfrkdr9slrPKi6J1pGXX1NVVDotOkYswud44jzrBmyrQ9I9eopO0ys3WwUEXolgmJ_l8ynpEvNfOdtmkXp7SuRP8y2HppamftqJePydhE0JNizwv2_YjCZyP90JtX_y0OXFaj-ZC6wi9aw-YROV5Ze3uESz2ZXccZTdDlYAcLBfwgA3nMM6O4aB8Hrc-cSUVnCPGjHOEdBst2dm16m1uFdrRPEpM32-_fRRR78gjVvbK8f5GWpiMX4SPL0H28ExQM9_gZKb1uuTbHxCZLK0SVJ0iDaZ_FNs_bF6ncYlE6-u1oYqb2RI7fH2nQq69O9chi26LNNXwIixxWqjzZl9844QGFM1hMUiiOfo8pCrlTyhMf6jDgOIJzvavuwxAawxuBTaNwFuafmZAFuMrLE8xPmWtlwq21mX0F4fgZqJW4871qVy3ZbaqyXYeq4WJbS3zNFpbwBebMEHt1dVUObmV9W83z13DtPUn0sOhN8woLMusCvWlifwoP4qHlcCMAGU6DX9GReimgPiNggjQAUfhztuH0cSaQGQIf-4CsA-qrIqRWoVjjiaQ21xLr9zq6vfo-tQJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج پیغام های  شما از گزارش عجیب ایران اینرنشنال توسط مجری افغان این شبکه مرضیه حسینی که مجاهدین خلق رو مردم ایران میدونه و پرچم جعلی اونها رو پرچم شیرو خورشید عنوان میکنه ! و پروموتشون میکنه !
@WarRoom</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/24086" target="_blank">📅 02:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24085">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کلمبیا در مجمع عمومی سازمان ملل متحد، قطع روابط دیپلماتیک با ایران را اعلام کرد.
@WarRoom
امشب الهیه صف سفید‌ بازاست فردا قیمت میره بالا
❄️
😂</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/24085" target="_blank">📅 01:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24084">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtiF6Xbxfx5YLRObKN8xD6HYVH7-Msz7bcSKzL5oQD4BeiUbc-O_t2rhrToYFNdjJ4zIqBNGPyTFZ5RiL26YcouPMofAHkierr9F0F4f9Yus7rGePo_lMKCk_LE0mW4YpuBJFUSjODdbWHeIrf8tdz36o0WJ2-VluF99KBPwwAMg5_5re8vVJGz4BfdLD7DZy5djeL_lgv2XllOhwdJZiXeVkdWK575YL4lq7QZ20IuJ8t0DyKpiaiY_cgjTntBCKakYPdUZG22JLBqp-M_pWobM2XVOjq9lk8g1ge0lETWdfc9ag5EvtFPEZPGdzmYhIzPxnz9BEdHmiydlwrYiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده اسرائیل یه استارلینک میبره برای نمایندهی ایران در صحن سازمان ملل و می‌گه اینو بگیر به کارت میاد. و می‌گه ما عاشق مردم ایران هستیم و برای تغییر رژیم دعا می‌کنیم. @WarRoom</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/withyashar/24084" target="_blank">📅 01:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24083">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137bb832f8.mp4?token=bX5_DS3swzyiIoTSpsiO_RoYX9LtWpMUoLTO1GFVMgINsJniftU9poucigXSSgZnVxwjVjvjPln1wZyNNBDC4UUXtIwECzExmI0AMQr1d1BlaOcFzWrFsyk0c-U47_PsAXa7vu-GwtJCxcWDDYHD0NYA2V49LEd9oZm5nglNP6aJL3WHj0x6LCnf6hldiOIBCE2DSf1UG-aBem8Sknl0873Atz5NbKwAP56Pa2d7N9vGwnSSgu9hugpphvwK-EadhqxaFdYzU229k2aD7z_URCJsDP3Rz02xvz1JsUuouc-wFQdXjpG3coIfS4Znl7Rb9pwfQRVQV13TBp1gujAd0zXojYsyxLFBD0OoTHVhk6LhuGZryPJMYL5wrtlBDlBXNljCZRm_IMCZtNZ7f7-SmTMsLv5LU68oaYZrDR484Kub4_5zG8OgQSkQPyO1x_rBzhJFkREMI4MS55lJdIQGXdO4z_OItsKW2oY-OkXsNA9EVUxMamErf1NF39BmrdzLAZNUWAeuMq3gSNubCbbg8cPwyLjMmcP0affFij-BKPuclhAWNmgZe3t5v61nHy2dBgZ3qpxyrzVxOqwTanHl2kP8U6DJt85e3Jm1X5NdhNO5ZqD2AdfkD4HW83A32wy_H1tPhWphp3bfpw61aggcjg1lX55pK45fO-u5SbHiLMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137bb832f8.mp4?token=bX5_DS3swzyiIoTSpsiO_RoYX9LtWpMUoLTO1GFVMgINsJniftU9poucigXSSgZnVxwjVjvjPln1wZyNNBDC4UUXtIwECzExmI0AMQr1d1BlaOcFzWrFsyk0c-U47_PsAXa7vu-GwtJCxcWDDYHD0NYA2V49LEd9oZm5nglNP6aJL3WHj0x6LCnf6hldiOIBCE2DSf1UG-aBem8Sknl0873Atz5NbKwAP56Pa2d7N9vGwnSSgu9hugpphvwK-EadhqxaFdYzU229k2aD7z_URCJsDP3Rz02xvz1JsUuouc-wFQdXjpG3coIfS4Znl7Rb9pwfQRVQV13TBp1gujAd0zXojYsyxLFBD0OoTHVhk6LhuGZryPJMYL5wrtlBDlBXNljCZRm_IMCZtNZ7f7-SmTMsLv5LU68oaYZrDR484Kub4_5zG8OgQSkQPyO1x_rBzhJFkREMI4MS55lJdIQGXdO4z_OItsKW2oY-OkXsNA9EVUxMamErf1NF39BmrdzLAZNUWAeuMq3gSNubCbbg8cPwyLjMmcP0affFij-BKPuclhAWNmgZe3t5v61nHy2dBgZ3qpxyrzVxOqwTanHl2kP8U6DJt85e3Jm1X5NdhNO5ZqD2AdfkD4HW83A32wy_H1tPhWphp3bfpw61aggcjg1lX55pK45fO-u5SbHiLMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایمان دشتی، دانشجوی دانشگاه میشیگان، در گفت‌وگو با ویل کین از فاکس‌نیوز گفت از عبدالسعید (نامزد دموکرات انتخابات فرمانداری میشیگان) پرسیده آیا بدون هیچ ابهامی با سپاه پاسداران مخالف است، اما به گفته او عبدالسعید از پاسخ مستقیم خودداری کرد. دشتی گفت فقط کافی بود او صریحاً بگوید با «بزرگ‌ترین حامی تروریسم در جهان» مخالف است و مدعی شد شاید عبدالسعید به دلیل حمایت بخشی از هوادارانش از حکومت ایران و سپاه، نمی‌خواهد آنها را از خود دور کند.
@WarRoom</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/withyashar/24083" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24082">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرگزاری NBC به نقل از مسعود پزشکیان: می‌‌خوایم قبل از شروع انتخابات میان‌دوره‌ای آمریکا توافق کنیم!
اصلا نمی‌خوایم کار به انتخابات میان‌دوره‌ای بکشه و آرزو می‌کنم آمریکایی‌ها قبل از اون به تفاهم‌نامه‌ی آتش‌بس برگردن
ایران برای بازرسی از تأسیسات هسته‌ای خودش اعلام آمادگی کرده
ما به هیچ‌وجه دنبال ترور ترامپ و یا اعضای خانواده‌اش نیستیم
@WarRoom</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/24082" target="_blank">📅 01:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400ab8f284.mp4?token=OqSBcDCmZj-9veP7_wlvBB7vvuEcONgW0hPzdPNhd7PMn1n-IAcPbWPTEErvzPD2n_Qk6SrHrhI7l55cKn6XE_wzhQAyRUFlbF40P9ArC52rdNdMZ35PFt0g0f_TgBYReO8Mi6iwxDBwJ2AwEFoEx1AR6yP561g1cQlqqTj7rZ5qc_dHcY-VPQEUvQpCXe0wW4Zd_Sp-NT_5TvH3S5MEs_oiVcrfBW2c81VUzpp16dZ9PiFClq_nscRNS_5cofDlgrtw_PNXFzty0WTPauwg7Fgbi9C-H_iMtkscVaF_CPwelY1rpTLP-YrE7MTl7464Q_mrUxz4G6Gs0GVu1YBbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400ab8f284.mp4?token=OqSBcDCmZj-9veP7_wlvBB7vvuEcONgW0hPzdPNhd7PMn1n-IAcPbWPTEErvzPD2n_Qk6SrHrhI7l55cKn6XE_wzhQAyRUFlbF40P9ArC52rdNdMZ35PFt0g0f_TgBYReO8Mi6iwxDBwJ2AwEFoEx1AR6yP561g1cQlqqTj7rZ5qc_dHcY-VPQEUvQpCXe0wW4Zd_Sp-NT_5TvH3S5MEs_oiVcrfBW2c81VUzpp16dZ9PiFClq_nscRNS_5cofDlgrtw_PNXFzty0WTPauwg7Fgbi9C-H_iMtkscVaF_CPwelY1rpTLP-YrE7MTl7464Q_mrUxz4G6Gs0GVu1YBbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده اسرائیل یه استارلینک میبره برای نمایندهی ایران در صحن سازمان ملل و می‌گه اینو بگیر به کارت میاد. و می‌گه ما عاشق مردم ایران هستیم و برای تغییر رژیم دعا می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/24081" target="_blank">📅 01:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24080">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7adc972c.mp4?token=VU3EK0vIsCI3wp3qN4AYepMdk1b6mgihLNxzuudWdQ_mpOHFIuAxe9c8aPnV37fT3oYXlguVXEGRcN4oRFZnTomzps2WUa98QLqHIzZlQvmTPXab3Ro2X2Mil42mNmgi0EZj7qEEX5EPVr6nz4azrIP_CCxJ6gqVBGAaLa6Tjd9vAo91QKciF9SULzJ5bu9Hd5qDYzF4GM8ANxAeHGCXDuuPowFuu0v2lNGAR7g3Hj8QgyIBdtigxwYUYKZNKr9VtfGVvNwCJJ7iznYaN8CDBcuG2s5uG8k4EFLKOVYfO5zpcmAUla9kDKhhmoIDvVNTLSh_uEWQPcGFOe5EKtlnuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7adc972c.mp4?token=VU3EK0vIsCI3wp3qN4AYepMdk1b6mgihLNxzuudWdQ_mpOHFIuAxe9c8aPnV37fT3oYXlguVXEGRcN4oRFZnTomzps2WUa98QLqHIzZlQvmTPXab3Ro2X2Mil42mNmgi0EZj7qEEX5EPVr6nz4azrIP_CCxJ6gqVBGAaLa6Tjd9vAo91QKciF9SULzJ5bu9Hd5qDYzF4GM8ANxAeHGCXDuuPowFuu0v2lNGAR7g3Hj8QgyIBdtigxwYUYKZNKr9VtfGVvNwCJJ7iznYaN8CDBcuG2s5uG8k4EFLKOVYfO5zpcmAUla9kDKhhmoIDvVNTLSh_uEWQPcGFOe5EKtlnuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان به فاکس‌نیوز می‌گوید مجتبی خامنه‌ای بسیار سالم است؛ «بعلهههه بسیار زیاد. کاملاً.»
@WarRoom</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/24080" target="_blank">📅 00:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24079">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مدیریت فرودگاه بین‌المللی نجف:
بر اساس دستور رسمی مراجع ذی‌صلاح، تمام پروازهای ورودی و خروجی از مبدأ یا به مقصد ایران از ساعت
۲:۰۰ بامداد جمعه ۳ مهر ۱۴۰۵
(۲۵ سپتامبر ۲۰۲۶) تا اطلاع ثانوی متوقف می‌شود. از شرکت‌های هواپیمایی و بخش‌های عملیاتی خواسته شده تا زمان اعلام رسمی، هیچ اقدام عملیاتی برای این پروازها انجام ندهند.
@WarRoom</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/24079" target="_blank">📅 00:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24078">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پرتاب دو موشک از نوع ابومهدی المندس ، از سیریک به سمت تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/24078" target="_blank">📅 00:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24077">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نیویورک‌پست:
سنای آمریکا بار دیگر طرحی برای محدود کردن اختیارات جنگی ترامپ در جنگ ایران را رد کرد؛ این رأی به معنای حفظ اختیارات فعلی رئیس‌جمهور آمریکا برای ادامه عملیات نظامی است.
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24077" target="_blank">📅 23:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24076">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش‌های تأییدنشده از شلیک دو موشک/پهپاد از ارومیه، به سمت اربیل عراق   @WarRoom</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/24076" target="_blank">📅 23:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیویورک‌پست :
ارتش آمریکا در حال استفاده از
سامانه‌های لیزری
برای مقابله با برخی پهپادها و موشک‌های کروز و همچنین اهداف زیرساختی ایران در منطقه هرمز است. طبق گزارش این رسانه، هزینه شلیک لیزر به‌مراتب کمتر از استفاده از موشک‌های رهگیر عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/24075" target="_blank">📅 23:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سازمان هواپیمایی کشوری امارات اعلام کرده پروازهای شرکت‌های هواپیمایی ایرانی
از امروز ۲۴ سپتامبر تا اطلاع ثانوی
به مقصد و از مبدأ امارات تعلیق شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/24074" target="_blank">📅 23:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رویترز ـ مذاکرات آمریکا و ایران وارد مرحله جدید شده:
منابع نزدیک به مذاکرات می‌گویند تهران و واشنگتن در نیویورک درباره یک
توافق مرحله‌ای
برای پایان جنگ مذاکره کرده‌اند؛ طرح مورد بحث شامل بازگشایی تدریجی تنگه هرمز در برابر کاهش یا پایان محاصره اقتصادی آمریکا و احتمال آزادسازی بخشی از دارایی‌های ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/24073" target="_blank">📅 23:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مسئولان جمهوری اسلامی بعد از ترک سالون، عکس قاسم کتلت را روی میزشان قرار دادند. @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24071" target="_blank">📅 22:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDxSEXfndNMZN6RXUkM5OjDR1JY8KipfCqsNNth9eFG1Ghp8ujP0AMRsAaHUO6rqdqW_acQskO-k6ODR22g_D5I3cbpYnoW5rq08rLAUHy1VDE3717SfVP4QSJBjioasHJmpF4yIncSoTrPqw0c_d0DmAK-n-Q--uFa4glLNyoVrOsGt46KamYMpYL43mfhQcjVxcnWpYMuiWFGtoPSwO9dPhXVGU1yeugBTsBStsUlR7xL2JiqFRUv7yS_SkQsFb7gXrFzSORCMMqVOLQPp9214GKV258iJT9PFZov6MFshL6FJeBMwtHfj6EMXJedSNI_bKxf31Mb2MJgC_SG6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئولان جمهوری اسلامی بعد از ترک سالون، عکس قاسم کتلت را روی میزشان قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24070" target="_blank">📅 22:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/24069" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24068">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/24068" target="_blank">📅 22:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24067">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/24067" target="_blank">📅 22:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24066">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/24066" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24065">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو:
در طول قرن‌ها، حکومت‌های مستبدی که تلاش کردند ما را نابود کنند، بارها و بارها شکست خورده‌اند و به خواست خدا، همچنان شکست خواهند خورد. اگر شجاعت خود را جمع کنیم و عزم خود را جزم کنیم، به پیروزی ادامه خواهیم داد.
همان‌طور که در کتاب مقدس آمده است: «נצח ישראל לא ישקר»؛ یعنی «جاودانگی اسرائیل هرگز لغزش نخواهد کرد.» و دلیلش ساده است:
ما انتخاب دیگری نداریم.
از همه شما متشکرم.
חג שמח לעם ישראל
؛ عید بر مردم اسرائیل مبارک. متشکرم.خداحافظ
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/24065" target="_blank">📅 22:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24064">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e66c6dc10.mp4?token=QrtvgTF0fPloNzOEidvYS3kGaoFR5A0Sp19qxdn90GIwxMiNTT9uPVSZBJtz-ACFMq6f-zTnToahA_S5t9mjrxOI0e3IDdVOju7TfsmigWyIqoiSgIzXFSmqXZd8ideqFuCTamjSNnPa6lrYLyD9IWemEZGELfz3arDsMApFp0TqLopnExw1KUPzmLIueAReOQHP3qI6lDpEgD-othUvh5RMCN7Qoxi9fJo_3CoG5r7HvM-rGmP67guldSwz5RUuSMm2od0zspxwDOQNG8_443QyYcFzYXLp8WFuXGlWbBTrzDaBGOvP-Te_6Q8FbO21XVzzMLV99TAqQPbJRFh0kL5BcwUTF8mQiwXdtsnjDwCittATSwm9QiOviDi2tY8jQYFTiiQh44x9APjLITYIZ-qfFtKrF1id1LZ_FcrEo_Gy-zfiXa-nVvXQ9SwJDU5h8gUAiZ_83B3y0-_W1bHu4T9c4XRD_r7WKS-FggrRNTcDYbsljbLb6rOneX7QJtbMlkBEj0c4NY4U_MF9Gf-RefyAz7OkeF5Y8J0UgDkDoKXCPjUprri0kwgHtWx2Md_boas_a3rgs9TxksYj_QD-DiWdrcSL-UwFjIMCYxIa7NyYgBx7BipH9iB1HzXeu-akWZz5PwyHs358znYsehaZoZnipMCaG2YxJwbxuPnNtAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e66c6dc10.mp4?token=QrtvgTF0fPloNzOEidvYS3kGaoFR5A0Sp19qxdn90GIwxMiNTT9uPVSZBJtz-ACFMq6f-zTnToahA_S5t9mjrxOI0e3IDdVOju7TfsmigWyIqoiSgIzXFSmqXZd8ideqFuCTamjSNnPa6lrYLyD9IWemEZGELfz3arDsMApFp0TqLopnExw1KUPzmLIueAReOQHP3qI6lDpEgD-othUvh5RMCN7Qoxi9fJo_3CoG5r7HvM-rGmP67guldSwz5RUuSMm2od0zspxwDOQNG8_443QyYcFzYXLp8WFuXGlWbBTrzDaBGOvP-Te_6Q8FbO21XVzzMLV99TAqQPbJRFh0kL5BcwUTF8mQiwXdtsnjDwCittATSwm9QiOviDi2tY8jQYFTiiQh44x9APjLITYIZ-qfFtKrF1id1LZ_FcrEo_Gy-zfiXa-nVvXQ9SwJDU5h8gUAiZ_83B3y0-_W1bHu4T9c4XRD_r7WKS-FggrRNTcDYbsljbLb6rOneX7QJtbMlkBEj0c4NY4U_MF9Gf-RefyAz7OkeF5Y8J0UgDkDoKXCPjUprri0kwgHtWx2Md_boas_a3rgs9TxksYj_QD-DiWdrcSL-UwFjIMCYxIa7NyYgBx7BipH9iB1HzXeu-akWZz5PwyHs358znYsehaZoZnipMCaG2YxJwbxuPnNtAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: شما درباره ایران هم سکوت کردید، اما من خبر خوبی دارم؛ با وجود این سکوت و آنچه من ریاکاری می‌دانم، روزی قدرت مردم ایران بر حاکمان آن غلبه خواهد کرد. ممکن است این روز چندان دور نباشد. مردم ایران روزی آزاد خواهند شد و رژیم حاکم، که من آن را سرکوبگر و جنایتکار می‌دانم، به‌دلیل دروغ، فساد و ظلم خود سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/24064" target="_blank">📅 22:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24063">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو: به هیئت ایرانی توصیه می‌کنم این پیام را بشنوند تا اگر روزی از کشورشان خارج شدند، بتوانند آزادانه داستان خود را در شبکه‌های اجتماعی بازگو کنند. خطاب به معترضان حقوق بشر در خارج از اینجا می‌پرسم: وقتی حکومت ایران ده‌ها هزار غیرنظامی ایرانی را شکنجه و مجروح کرد و هزاران نفر از مردم خود را کشت، کجا بودید؟ آیا تجمع گسترده، اعتصاب غذا یا اعتراضی مقابل نمایندگی ایران در سازمان ملل برگزار کردید؟ درباره مسیحیان تحت آزار در ایران و خاورمیانه چطور؟ هیچ‌کدام
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/24063" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24062">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو قول بر اندازی رژیم و جشن همگانی را داد
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/24062" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24061">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac08257aa.mp4?token=IzhOEb9dU3ttJVaSOLfXI0mK62RDz5llI8waQk1sjIrgwisD-OLVbvm8_RIlJHxnjuDR0fPKtoXN5ixyaUhXa8DGfB8Dqm8RwZcvXJGYTJ7QNpuGQdB1B78Y8OLMYEOmMu-jGtIdA696fEi2Dy8NxmyL_crgTr1kSttByUT5hAMH0wqRqpaaLtz0Yb9Mlpv8bPCf7aBBVDjnJ9DoZ8mUio_oTg9Ge6udXbcAp51-x2HXOixj9IzWJ88u4zXQS3gkyl-R0beGo6VZ2GkJ4lTxKoQQiYyTulqCjd-AUUj2U4ftmLf9YW9pbmsXT4WzrocjNJNDXQ4FUiLAJVeApuujZV22vNjLIkPJ23dlT8CSc3SIENFfw4DF7M90rhmB_i0uZn6zBarCUKBJbY8B6TgqfN2AQgwPad96m9Whr1OHcV_nwJmWInsxmo-Z9NaMDePo59TI32SFKAXJ23Fg8MnkbmVqbkBuuCpRXfpW_xtwotiCxvRDXKSLwc7ieNMLPVeXiZc6gmf8ZmcNqMsvXV81c-ZDqfWcCue3M45pSNOjQBbdigH3rgWFT0DmyQyEB51hwp8Lja--pFbNwomEagh6GiVnO5ArCNAL3xX9f_ajiz2yvcu_zZzzHJ9-WeqHfulXrix0DDMbLNjfTHornAbBRclecf-dZ303lwumuWtRvm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac08257aa.mp4?token=IzhOEb9dU3ttJVaSOLfXI0mK62RDz5llI8waQk1sjIrgwisD-OLVbvm8_RIlJHxnjuDR0fPKtoXN5ixyaUhXa8DGfB8Dqm8RwZcvXJGYTJ7QNpuGQdB1B78Y8OLMYEOmMu-jGtIdA696fEi2Dy8NxmyL_crgTr1kSttByUT5hAMH0wqRqpaaLtz0Yb9Mlpv8bPCf7aBBVDjnJ9DoZ8mUio_oTg9Ge6udXbcAp51-x2HXOixj9IzWJ88u4zXQS3gkyl-R0beGo6VZ2GkJ4lTxKoQQiYyTulqCjd-AUUj2U4ftmLf9YW9pbmsXT4WzrocjNJNDXQ4FUiLAJVeApuujZV22vNjLIkPJ23dlT8CSc3SIENFfw4DF7M90rhmB_i0uZn6zBarCUKBJbY8B6TgqfN2AQgwPad96m9Whr1OHcV_nwJmWInsxmo-Z9NaMDePo59TI32SFKAXJ23Fg8MnkbmVqbkBuuCpRXfpW_xtwotiCxvRDXKSLwc7ieNMLPVeXiZc6gmf8ZmcNqMsvXV81c-ZDqfWcCue3M45pSNOjQBbdigH3rgWFT0DmyQyEB51hwp8Lja--pFbNwomEagh6GiVnO5ArCNAL3xX9f_ajiz2yvcu_zZzzHJ9-WeqHfulXrix0DDMbLNjfTHornAbBRclecf-dZ303lwumuWtRvm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
این یک وسیله ارتباطی است؛
استارلینک
. ابزاری که به مردم اجازه می‌دهد به حقیقت دسترسی پیدا کنند، انتخاب داشته باشند و از آزادی اندیشه و آزادی بیان برخوردار شوند. به همین دلیل است که رژیم ایران از دسترسی مردمش به چنین فناوری‌هایی می‌ترسد
@WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/24061" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24060">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نتانیاهو:
می‌دانید چه کسی می‌ترسد؟
مستبدان تهران.
و بیش از همه از چه چیزی می‌ترسند؟
از مردم خودشان؛ مردم شجاع ایران که برای مدت طولانی فداکاری کرده‌اند.
رژیم ایران به‌ویژه زمانی می‌ترسد که مردم ایران به ابزارهایی برای دسترسی آزاد به اطلاعات دسترسی داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/24060" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24059">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهو:
ما در اسرائیل منتظر نمی‌مانیم تا دیگران از خواب اخلاقی خود بیدار شوند. ما به پیش می‌رویم و در حوزه‌هایی مانند پزشکی، کشاورزی و هوش مصنوعی پیشرفت می‌کنیم و این نوآوری‌ها را در اختیار بشریت قرار می‌دهیم. اسرائیل هرگز قدرتمندتر از امروز نبوده و ما نمی‌ترسیم
@WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/24059" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24058">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نتانیاهו: جهان باید بداند که حماس از غیرنظامیان فلسطینی به‌عنوان سپر انسانی استفاده می‌کند و از بیمارستان‌ها، مدارس و مساجد به‌عنوان مراکز فرماندهی بهره می‌گیرد. اسرائیل برای دور کردن غیرنظامیان از مناطق درگیری، میلیون‌ها پیام هشدار، تماس تلفنی و اعلامیه ارسال کرده است. اتهام نسل‌کشی علیه اسرائیل، به گفته من، «بزرگ‌ترین دروغ قرن» است؛ زیرا اسرائیل هم‌زمان با جنگ، یک میلیون واکسن فلج اطفال و دو میلیون تُن غذا برای مردم غزه فراهم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/24058" target="_blank">📅 22:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24057">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتانیاهو: برخی کشورها میلیاردها دلار برای انتشار آنچه ما دروغ علیه اسرائیل می‌دانیم هزینه کرده‌اند.
قطر و ترکیه
از جمله کشورهایی هستند که به انتشار این روایت‌ها متهم‌شان می‌کنم. قطر سال‌ها از دانشگاه‌ها و رسانه‌هایی مانند الجزیره حمایت مالی کرده و ترکیه نیز تحت رهبری اردوغان بارها علیه اسرائیل موضع گرفته است. اردوغان خواستار نابودی اسرائیل شده و گفته است که می‌خواهد حاکم اورشلیم شود؛ اما این کشور و این شهر، پایتخت ابدی ماست
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/24057" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24056">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو: مردم اسرائیل در برابر هزار موشک بالستیک سنگین ایران که بر سر شهرها و غیرنظامیان ما فرود آمد، ایستادگی کردند. شما در سالن مجمع عمومی سازمان ملل نشسته‌اید؛ اگر تنها یک موشک بالستیک یک‌تنی به اینجا اصابت کند، می‌تواند کل این مجموعه را ویران کند و دو موشک از این نوع می‌تواند سازمان ملل را نابود کند. حال تصور کنید هزار موشک عظیم از آسمان بر سر شهرها و خانه‌های شما فرود بیاید. من به شجاعت مردم اسرائیل و سربازانمان، از یهودی و مسیحی تا دروزی و مسلمان، ادای احترام می‌کنم
@WarRoom</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/24056" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24055">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو: چرا پیروز می‌شویم؟ یوناتان نتانیاهو پاسخ را ساده بیان کرد: «ما انتخاب دیگری نداریم.» هدف ما در تمام این جنگ ثابت بوده است؛ پیروزی با اراده‌ای تزلزل‌ناپذیر و شجاعتی بی‌وقفه. این اسرائیل است؛ یک ملت با یک آینده مشترک، از چپ و راست، جوان و پیر، مذهبی و سکولار
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/24055" target="_blank">📅 22:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24054">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نتانیاهو: در این نبرد با آنچه «بربرها» می‌نامیم، هیچ شریکی بزرگ‌تر از رئیس‌جمهور ترامپ نداشتیم. از او و رهبری جسورانه‌اش تشکر می‌کنم. او دهه‌ها پیش فهمید که اگر با رهبران افراطی ایران که شعار «مرگ بر آمریکا و مرگ بر اسرائیل» سر می‌دهند مقابله نشود، در نهایت به دنبال عملی کردن اهداف خود خواهند رفتاسرائیل و آمریکا در کنار یکدیگر برای حفاظت از خود و نجات تمدن اقدام کردند. خلبانان شجاع آمریکایی در کنار خلبانان اسرائیلی در مأموریت‌های مشترک بر فراز ایران فعالیت کردند. دو کشور همچنین برای بازگرداندن گروگان‌های باقی‌مانده همکاری کردند و همه آنها را به خانه بازگرداندیم
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/24054" target="_blank">📅 22:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24053">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتانیاهو: با وجود همه این رنج‌ها، تسلیم نمی‌شویم. «نریا» در آخرین نوشته خود پیش از حمله به او نوشته بود: «ما کشور دیگری نداریم؛ دفاع از آن یک افتخار است.» به نریا و همه قهرمانان اسرائیل قولی مقدس می‌دهم: فداکاری شما بیهوده نخواهد بود. ما به دفاع از کشورمان ادامه می‌دهیم و پیروز خواهیم شد، چون انتخاب دیگری نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/24053" target="_blank">📅 22:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24052">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسانه های عبری : نریا لیتر، پسر یحیئل لیتر، سفیر اسرائیل در آمریکا، در حمله با خودرو در ایست‌بازرسی مَکابیم در مسیر ۴۴۳ در کرانه باختری به‌شدت زخمی و به بیمارستان شعاری زِدِک در اورشلیم منتقل شد. راننده خودرو محمود محمد محمود سلیمان، ۲۹ ساله، ساکن روستای بیت‌عور…</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/24052" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24051">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نتانیاهو:
ای
امانوئل مکرون، همکارم، به این موضوع توجه کن: دو یا سه روز پیش، یک شهروند فرانسوی به نام ناتانیل شوکرون، پدر شش فرزند، هنگامی که همراه پسر ۱۶ ساله‌اش از یک چشمه بازدید می‌کرد، هدف گلوله قرار گرفت. یک تروریست حماس در یهودیه و سامریه از فاصله نزدیک به او شلیک کرد.
آخرین کلماتی که او بر زبان آورد این بود: «فرار کن، فرار کن پسرم، خودت را نجات بده.» این اتفاق سه روز پیش رخ داد
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/24051" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24050">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتانیاهو:
سران تروریست‌ها و بزرگ‌ترین عاملان کشتار جمعی در جهان، نه‌تنها اسرائیلی‌ها، بلکه آمریکایی‌ها، بریتانیایی‌ها و شهروندان ده‌ها کشور را به قتل رساندند؛ خامنه‌ای، ضیف، سنوار، هنیه، نصرالله و هزاران تروریست دیگر که در پی نابودی ما بودند، همگی از بین رفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/24050" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24049">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو:
می‌دانید چه اتفاقی برای بخش عمده زرادخانه عظیم حزب‌الله، شامل حدود ۱۵۰ هزار موشک بالستیک و راکت که همگی برای هدف قرار دادن غیرنظامیان ما آماده شده بودند، افتاد؟ همه آنها از بین رفته‌اند. رهبران حزب‌الله کشته شده‌اند و روحیه آنها درهم شکسته است
@WarRoom</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/24049" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24048">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو:
ارتش، نیروی دریایی، نیروی هوایی و تأسیسات هسته‌ای ایران را هدف قرار دادیم. اسرائیل حماس را به‌شدت درهم کوبید و ما نیز حزب‌الله را به‌شدت درهم کوبیدیم. آن ضربه را به خاطر دارید؟ می‌توانم این را به شما بگویم: حزب‌الله قطعاً آن را به خاطر دارد
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/24048" target="_blank">📅 21:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24047">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتانیاهو: دشمنان ما انتظار داشتند اسرائیل پس از ۷ اکتبر فروبپاشد، اما ما فرو نریختیم و جنگیدیم. طی سه سال گذشته، سربازان ما در یک جنگ هفت‌جبهه‌ای با حماس، حزب‌الله، حوثی‌ها، ایران، شبه‌نظامیان عراق و سوریه و گروه‌های مسلح فلسطینی در کرانه باختری جنگیده‌اند. همه آنها برای نابودی اسرائیل با یکدیگر همراه شدند، اما شکست خوردند
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/24047" target="_blank">📅 21:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24046">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو: به دنبال برادرم، یوناتان «یونی» نتانیاهو، رفتم که افسر ۲۱ ساله تیپ چتربازان بود و واحدش از قبل بسیج شده بود. وقتی او را پیدا کردم، از دیدنم شوکه شد. از او پرسیدم چه اتفاقی خواهد افتاد. مکث کرد و گفت: «ما پیروز خواهیم شد؛ انتخاب دیگری نداریم.» این…</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/24046" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24045">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو: به دنبال برادرم، یوناتان «یونی» نتانیاهو، رفتم که افسر ۲۱ ساله تیپ چتربازان بود و واحدش از قبل بسیج شده بود. وقتی او را پیدا کردم، از دیدنم شوکه شد. از او پرسیدم چه اتفاقی خواهد افتاد. مکث کرد و گفت: «ما پیروز خواهیم شد؛ انتخاب دیگری نداریم.» این جمله را هرگز فراموش نکردم
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/24045" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24044">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نتانیاهو: اسرائیل کشوری بسیار کوچک است؛ مساحت آن حتی به یک‌سوم یک درصد از کل سرزمین‌های جهان عرب نمی‌رسد. با این حال، ما را به استعمار متهم می‌کنند؛ آن هم از سوی کشورهایی مانند بریتانیا و فرانسه که خود سابقه استعمار گسترده دارند. این هم یک دروغ دیگر است
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/24044" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24043">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو: در بین کسانی که سالن را ترک کردند، کشورهای بودند که در خفا برای نابودی قدرت هسته‌ای ایران از ما تشکر کردند؛ و این نهایت تزویر و ریا است.
اگر هنوز بزدلانی هستند که اتاق را ترک نکرده‌اند، از آنها می‌خواهم همین حالا بروند.
@WarRoom</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/24043" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24042">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نتانیاهو: تخریب تاسیسات هسته‌ای ایران بسیار سخت بود، اما برای من یکی از آسان‌ترین تصمیم‌هایی بود که گرفتم
من به آقای احمد الشرع سوریه ای می‌گویم که یهودیان از زمان موسی در بلندی‌های جولان بوده‌اند و اگر جرعت داری علیه جولان اقدام کن.
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/24042" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24041">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نتانیاهو:۱۴ سال پیش گفتم مانع این میشم که جمهوری اسلامی به سلاح هسته‌ای برسه و ما دقیقا این کار رو کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24041" target="_blank">📅 21:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24040">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتانیاهو : ما باید ببریم هیچ راه دیگه ای نداریم
حاضران : تشویق
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24040" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24039">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینستاگرام بی بی رفت لایو</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/24039" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24038">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765c13dc80.mp4?token=SEovDoa_PGpJLBAjGeDuW9hNSlFLnpqlIyJ8X-ZIsGb1LfqjedUf5pxuXP0w0q5S8Ht9QjFF2G-9nO1rhIjnCZzFeROgyxaWlmHwXdakF_MEpEq_gPn1exbNZKuDR6c_bwkHMv3W_LH1I2Uj2KLdOH_KIBQkX2EiXEZjFr_yJROpdKwRZD5ZsykEnr6930lbDTeX_a_MHgRFrXjjcs_sKOIcZ6oacNXPG9ppLV8NjaPuy9z8T1c38R6vHRTI7rs7dlgxzRYpAmxIUXQLXo3nNqSUMpiqkclccO1L-zmbA5ov_F5cBVyWvbUullSpFuLPud_s_al8OF4ZHw0dYV-H3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765c13dc80.mp4?token=SEovDoa_PGpJLBAjGeDuW9hNSlFLnpqlIyJ8X-ZIsGb1LfqjedUf5pxuXP0w0q5S8Ht9QjFF2G-9nO1rhIjnCZzFeROgyxaWlmHwXdakF_MEpEq_gPn1exbNZKuDR6c_bwkHMv3W_LH1I2Uj2KLdOH_KIBQkX2EiXEZjFr_yJROpdKwRZD5ZsykEnr6930lbDTeX_a_MHgRFrXjjcs_sKOIcZ6oacNXPG9ppLV8NjaPuy9z8T1c38R6vHRTI7rs7dlgxzRYpAmxIUXQLXo3nNqSUMpiqkclccO1L-zmbA5ov_F5cBVyWvbUullSpFuLPud_s_al8OF4ZHw0dYV-H3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/24038" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24037">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شروع نکرده گفت ایران داره بمب میسازه</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/24037" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24036">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یه عده سیاه پوست و محجبه سالن رو ترک کردن
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/24036" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24035">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو اومد پشت تریبون سازمان ملل
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24035" target="_blank">📅 21:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24034">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBx8Ao2Wm4homO7Z3Nc4sh0AYwuveEEEp_If-8OaEY-aKyMaDoOld9x93qERmZMv1kiPHP3nHYMKjlVJM6xfAjR2ZfgUwwWfCBDR6kciWj01bafEvsZg7ia3yvEUANRDHPiSElAWkbfzkSIlRNXwmZLP5XYwGyDyke6RcTGYaAGxsHskWe-gxhQu3w43xbGgJ5ky3omTv5DWuhANBmxihZCURZ55m28s5ZjZlh3PeT0ms7ve8S9W1FjDxDbVaOf7M5vlA3eTgTYj3eXwOopBXSd9S9qN9KCrlU19aj-l4CVgv7GHK4vrzBmW-4_3DBME4B_7qK_0bS8MPpjaaWz-cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، قرار است امروز پنجشنبه ۲۴ سپتامبر، در گفت‌وگویی با «برت بایر»، مجری شبکه فاکس‌نیوز، حضور پیدا کند. این برنامه ساعت ۶ عصر به وقت شرق آمریکا پخش می‌شود که با توجه به اختلاف زمانی، برابر با ۱:۳۰ بامداد جمعه ۳ مهر به وقت تهران…</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/24034" target="_blank">📅 21:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24033">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بنیاد FDD: ترکیه در حال افزایش فشار بر شبکه مالی و حمل‌ونقل مرتبط با ایران است.
نهاد ناظر بانکی ترکیه مجوز فعالیت شعبه استانبول بانک ملت ایران را لغو کرده است. این اقدام پس از تحریم بانک سرمایه‌گذاری گلدن گلوبال ترکیه و دو شرکت زیرمجموعه آن از سوی آمریکا به‌دلیل ارتباط با سپاه انجام شد و ترکیه نیز وجوه این بانک را نقد و آن را تحت کنترل دولت قرار داد. ترکیش ایرلاینز، AJet و پگاسوس نیز پروازهای ترکیه و ایران را تا مارس ۲۰۲۷ متوقف کرده‌اند و آنکارا در حال محدود کردن فعالیت ماهان‌ایر به‌دلیل ارتباط ادعایی با سپاه است. بانک ملت حدود ۳۴.۸ میلیارد دلار دارایی دارد و از سال ۱۹۸۲ در تسویه تجارت ایران و ترکیه نقش داشته؛ آمریکا از سال ۲۰۰۷ آن را تحریم کرده و در سال ۲۰۱۸ تحریم‌های مرتبط با تروریسم را نیز علیه آن اعمال کرد. این گزارش همچنین به پرونده هالک‌بانک اشاره می‌کند که آمریکا آن را به انجام ۱۳ تا ۲۰ میلیارد دلار تراکنش مرتبط با ایران بین سال‌های ۲۰۱۲ تا ۲۰۱۶ متهم کرده بود. در جمع‌بندی، این اقدامات نشانه تلاش آنکارا برای حفظ روابط با تهران، همزمان با کاهش خطر تحریم‌های ثانویه آمریکا، ارزیابی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/24033" target="_blank">📅 21:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24032">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو: پیش از سخنرانی در سازمان ملل، به دیدارهای سیاسی خود ادامه می‌دهم؛ از جمله با نخست‌وزیران یونان و اسلوونی. با یونان در حال گسترش همکاری‌های انرژی و بین‌المللی، از جمله نشست سران اسرائیل، یونان و قبرس هستیم. در اسلوونی نیز با افتتاح سفارت اسرائیل در لیوبلیانا، فصل جدیدی در روابط دو کشور ایجاد کرده‌ایم که به هماهنگی نزدیک‌تر سیاسی منجر خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/24032" target="_blank">📅 21:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24031">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وحیدی : از جنگ نمیترسیم
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/24031" target="_blank">📅 20:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24029">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۴۵ دقیقه تا سخنرانی ‌و سورپرایز نتانیاهو
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/24029" target="_blank">📅 20:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24028">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم ورود ششمین زیردریایی نیروی دریایی این کشور،
INS Drakon
، به پایگاه دریایی حیفا گفت ورود این زیردریایی «پیامی مهم برای همه کسانی است که اسرائیل را تهدید می‌کنند، در رأس آنها رژیم آیت‌الله‌های تهران».
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/24028" target="_blank">📅 20:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24027">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش‌های تأییدنشده
از شلیک
دو موشک/پهپاد
از
ارومیه، به سمت اربیل
عراق
@WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/24027" target="_blank">📅 20:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24026">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3bc11b06.mp4?token=lpbwmhgXKyLmSC0yq8_LJ7QcPHkD0yrsIROj7hOebeyZ3vReUUUU17dHOWEAd9G5rtxeA9NxCd9Zbppc8O_FuzhSOJYg-fw9rZzpZqQEPYn8k5oJ9xFuGOdx6dPqEmJsz1GP_8wKH_EmL1jxQd8qHJjG9jvl0fDLlGVqrkaV6d8fBe925xMqLU4DEPhL4a_nxBTnJgP76PD1UcuLDjjons28yR3O-YFQvT8BQx2AMcfmkfQ5s18-In63IOFTU4Qqpy9XadUulH47SQWSRmTTmq1m5MQvwKS8OhU_mYAVQ4FFP9Ux9UZVTLY5o7dK-tXVSHPYlahoy3d1jLzfQ-dnCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3bc11b06.mp4?token=lpbwmhgXKyLmSC0yq8_LJ7QcPHkD0yrsIROj7hOebeyZ3vReUUUU17dHOWEAd9G5rtxeA9NxCd9Zbppc8O_FuzhSOJYg-fw9rZzpZqQEPYn8k5oJ9xFuGOdx6dPqEmJsz1GP_8wKH_EmL1jxQd8qHJjG9jvl0fDLlGVqrkaV6d8fBe925xMqLU4DEPhL4a_nxBTnJgP76PD1UcuLDjjons28yR3O-YFQvT8BQx2AMcfmkfQ5s18-In63IOFTU4Qqpy9XadUulH47SQWSRmTTmq1m5MQvwKS8OhU_mYAVQ4FFP9Ux9UZVTLY5o7dK-tXVSHPYlahoy3d1jLzfQ-dnCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون آتش سنگین و ستون دود عظیم در شهریار یوسف آباد صیرفی
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/24026" target="_blank">📅 20:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24025">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرگزاری CBS: بر اساس گزارش‌های منتشرشده، ۸۰ کشور با صدور بیانیه‌ای مشترک در سازمان ملل بر ضرورت بازگشت کامل و بدون مانع تردد دریایی در منطقه تأکید کردند. همزمان، مذاکرات غیرمستقیم مذاکره‌کنندگان آمریکایی و ایرانی در نیویورک ادامه دارد و
بازگشایی تنگه هرمز و پایان جنگ
از محورهای مهم گفت‌وگوهاست. گزارش‌های قبلی رویترز نیز نشان می‌دهد که بازگشت کشتیرانی در هرمز و رفع محدودیت‌های اقتصادی علیه ایران از موضوعات اصلی مذاکرات بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/24025" target="_blank">📅 20:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24024">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">داداش اعتصابات  من خودم مغازه دارم  و دور و بریام تا  لحظه یی که  خود مامور اداره برق نیاد داخل پاساژ بگه  فردا برقو قطع میکنیم. پرداختش نمیکنیم  ینی تقریبا هر ۵ماه یکبار پرداخت میکنیم ، اما  هم  هی فله یی میزارن روش هم اخرش وقتی مامور میاد مجبوریم پرداخت…</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/24024" target="_blank">📅 20:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24023">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMilad</strong></div>
<div class="tg-text">داداش اعتصابات
من خودم مغازه دارم
و دور و بریام تا  لحظه یی که  خود مامور اداره برق نیاد داخل پاساژ بگه  فردا برقو قطع میکنیم. پرداختش نمیکنیم
ینی تقریبا هر ۵ماه یکبار پرداخت میکنیم ،
اما  هم  هی فله یی میزارن روش هم اخرش وقتی مامور میاد مجبوریم پرداخت کنیم
چیکار کنیم</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/24023" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24022">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مسعود پزشکیان و عراقچی در حاشیه مجمع عمومی سازمان ملل با نواف سلام، نخست‌وزیر لبنان در گداخانه دیدار کردند. @WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/24022" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24021">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMDAIBbuNI_Ns7JuSYomoTzbPrVM6Nr4lryNXtWr1vThFPkxcIw8RU8YOIjMwwhbGN1bPGHwVRD93t_K8ZmkZjNaCevdLPtgAQmtDX5KS4mSSm_BHG9pEB4_SuWMyo9WTKq5KqMvWpLI2aHw1rNBcmUa9tsHP1bJXzlZnvrqFEeYqdc_fRNUfC_PMBORHpdOt32MUMWb2dDKFo7TbLkO7cx1U3MLhLnOORSLwPPW9ma0wj4XBmp20qK8LV0GI8w95-kWX88BZmr7VQWCN50d0PPZM96g_UVz9KYQTpP6vJyrnJclCrF2kltzmGwk1fFtpEZyIpsugXrgyQ99fk6ohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان و عراقچی در حاشیه مجمع عمومی سازمان ملل با نواف سلام، نخست‌وزیر لبنان در گداخانه دیدار کردند. @WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/24021" target="_blank">📅 19:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24020">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFlKeyxNixlwExvo9OCr_ca27XREDni7E1p6UPj3o_68pZOs-rmTTmHVY2wHTcyybFcSH6ETrOr1aZxuOVBgxPzTPPBwOPtpj2zlowYhQIeVuFqEGlY8K5tS_UnxABXQzgHFwlrsKZwpE6z9fmLeU04Tr7LFB26Vrxdbk4Otg7HQm5DcRLhG4tY20IoLwt6Mv_ZYXjJhcvDswssPVlp0AyI5b2kVTaIGvdXEwLw4F3w8d5n_jFsPVmYHFrTC03Tiw0faFbOhHGN1GpeMD-5I44RphqvekdV0R-wZo6cC9wIuF49gQ0GBRkDl6DXyvDX9c887rrkR4MLPX26eiL4L7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان
و عراقچی در حاشیه
مجمع عمومی سازمان ملل
با
نواف سلام، نخست‌وزیر لبنان
در گداخانه دیدار کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24020" target="_blank">📅 19:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24019">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d37142d90.mp4?token=NrYZX7xovreMBnaJ6msT1dGKChlkl3W9W3SYJXigZo3mAqiP320lpk6QjI9WVgoJbXEmFfEagR6H34PnHPTcnJxqdsxJ_yIjsQ3n4uJhm-nTwiUug11U8U2JgRM9U9Z5PDJZO1PUGtLhDtXHh8uTosvBca-eLVgJ1wgwbzIAZRpMRlstdBL4E9ezOCYdZVQWDS-m0VK6SZ-SjkwYGXZuW03NByKSDhsmDU92j3Zj2y-MT3vnchyFW1i6WPLv3OdvUAhriigwflaZVlBJMU6-a3lNtJbTlDHT_WJUTZGZOuClnAQW-W9uwYOA3uIHGTe1XT8CMbJfrHoZlfsJgMN_bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d37142d90.mp4?token=NrYZX7xovreMBnaJ6msT1dGKChlkl3W9W3SYJXigZo3mAqiP320lpk6QjI9WVgoJbXEmFfEagR6H34PnHPTcnJxqdsxJ_yIjsQ3n4uJhm-nTwiUug11U8U2JgRM9U9Z5PDJZO1PUGtLhDtXHh8uTosvBca-eLVgJ1wgwbzIAZRpMRlstdBL4E9ezOCYdZVQWDS-m0VK6SZ-SjkwYGXZuW03NByKSDhsmDU92j3Zj2y-MT3vnchyFW1i6WPLv3OdvUAhriigwflaZVlBJMU6-a3lNtJbTlDHT_WJUTZGZOuClnAQW-W9uwYOA3uIHGTe1XT8CMbJfrHoZlfsJgMN_bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو وارد سازمان ملل متحد در نیویورک شد
@WarRoom</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/24019" target="_blank">📅 19:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24018">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/24018" target="_blank">📅 19:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24017">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نفت به کانال ۱۰۲$ وارد شد @WarRoom</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/24017" target="_blank">📅 19:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24016">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2b2b37f7.mp4?token=KxltwFJHO2L1QjbKxDSBkmk0gFwgBnwIEiNopUjbRj4RxSSkFNVsodSYzJuYymSdOHAusCMgWfeOdbp8xxjSDh00JfLpULdtru1ZgNoPtczeCrbX3ZByHz8O6JQq40nGpdA9EXi9kvW0V7nFfw2Hdj25qcXpH-aRfpeeY5ARARdJMTntnno9A9X15SWK7CIxBBOyfv9tUeOIVsDZRWV6HssKvRWnTp2Z7YEYzY1RiPnb62vLGTg70i4vfMymxcyKBpti_OI9UBFJ4SOEWN-_fLKzyCH8ZWzv-UBLkk6WQdMf1FXMTqiM9GivORi3s_ACspev96Bx25iaVrkLUYzcjqmW5kICWD6QuYzeQmlehusuffSe5AfOJW74dFClKJtHBVyblbVsTsBowSFQJwMyorT2lrvEO7SbRTU4o4255tFkbSyDvNVqJ789v3BVGR8VZ5HKtQde76QLmQXSgr4qaze4F7miylMrmQTHCH8wfutzzBN7jmTTp252KVNVJUY6p4dlGkDTKsr7ej6QxmSuuoBNp8R1g4WsYfaA3ANrj6vr3T_CKBlsjCIem5qOmD6pkKdaJROWHxliWRzQydulVbPwQRr-BU33xesu3TE6bUuxCy0Cc0esHia2Z8ZpmwxSKAsV3T0aubQKTzQFZaDKABPgNc0UJQIglA10ynAO48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2b2b37f7.mp4?token=KxltwFJHO2L1QjbKxDSBkmk0gFwgBnwIEiNopUjbRj4RxSSkFNVsodSYzJuYymSdOHAusCMgWfeOdbp8xxjSDh00JfLpULdtru1ZgNoPtczeCrbX3ZByHz8O6JQq40nGpdA9EXi9kvW0V7nFfw2Hdj25qcXpH-aRfpeeY5ARARdJMTntnno9A9X15SWK7CIxBBOyfv9tUeOIVsDZRWV6HssKvRWnTp2Z7YEYzY1RiPnb62vLGTg70i4vfMymxcyKBpti_OI9UBFJ4SOEWN-_fLKzyCH8ZWzv-UBLkk6WQdMf1FXMTqiM9GivORi3s_ACspev96Bx25iaVrkLUYzcjqmW5kICWD6QuYzeQmlehusuffSe5AfOJW74dFClKJtHBVyblbVsTsBowSFQJwMyorT2lrvEO7SbRTU4o4255tFkbSyDvNVqJ789v3BVGR8VZ5HKtQde76QLmQXSgr4qaze4F7miylMrmQTHCH8wfutzzBN7jmTTp252KVNVJUY6p4dlGkDTKsr7ej6QxmSuuoBNp8R1g4WsYfaA3ANrj6vr3T_CKBlsjCIem5qOmD6pkKdaJROWHxliWRzQydulVbPwQRr-BU33xesu3TE6bUuxCy0Cc0esHia2Z8ZpmwxSKAsV3T0aubQKTzQFZaDKABPgNc0UJQIglA10ynAO48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی بی اس : در جریان مراسم استقبال رسمی از شی جین‌پینگ، رئیس‌جمهور چین، در کاخ سفید، یک فروند بمب‌افکن رادارگریز
B-2 Spirit
به همراه چهار فروند جنگنده
F-22 Raptor
بر فراز محل مراسم پرواز کردند. این پرواز بخشی از برنامه رسمی مراسم استقبال دولت آمریکا از رئیس‌جمهور چین بود
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/24016" target="_blank">📅 19:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24015">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLBbXCj06ax1woUjvm7iWYSHFeyMtmjrzKIE1IEDYo-LuMtkXyadhN3wzy2O4NcUk5yu-r0ZXiuweI8EilKfI32T5L-pwCp4HVmDqjmnbXxcshM-obOwk4FBr9FSenLF7Dnv6_edOOehO10KNWw6cxHKCoewE92__U6h2zo3WMd84Z3XkQggun7MJ_cjP_6KWDnNy9oTh8S1b3xQFT0pfY1a8r9o1VZgaQCLsFCbDD4BvrQtArTKt-QDHuQGQCvRb-F6PBTPdKWCDIdN3RjkNrt4T1IKCXvDi6rY6TSL2H5n4go8MZjHGKIvF4RSX4oN_LgDAJy1I0qK7cgY2pxuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت به کانال ۱۰۲$ وارد شد
@WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/24015" target="_blank">📅 19:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24014">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjea3-hJHyfQra6aTBdmx7341KTM-Uyhy3cXJRNe1JWpoX-jiQN4WEdV4nvpwicjybAL9b19bpcHclIJx7lK7m__ZiH6J1BSsEeadjdrxr4QbEAwYxbyIlycFxSrnaqo2n2JHeQxygZi-0wG-KhCu3pDM6aLwzdLFo7Ee4_4Bl7CI6uDkB-R3ai9ousaCyqxB4btozR06DfRD7z6zVH_YoTVqemdCv_-RgvvRB-Dywzirh-kU73JerHSWUqwgA8Idri-n6vf_nUGf4HLL8EDw4WqWqoBcJM2qipOs2Kn8o5AioLwpN4rJuMj1RHr0o3K4mwbjPsKW6GSn4yhDsPB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، قرار است امروز پنجشنبه ۲۴ سپتامبر، در گفت‌وگویی با «برت بایر»، مجری شبکه فاکس‌نیوز، حضور پیدا کند. این برنامه ساعت ۶ عصر به وقت شرق آمریکا پخش می‌شود که با توجه به اختلاف زمانی، برابر با
۱:۳۰ بامداد جمعه ۳ مهر به وقت تهران
است. فاکس‌نیوز برنامه «Special Report with Bret Baier» را در همین ساعت پخش می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/24014" target="_blank">📅 19:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24013">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وال‌استریت ژورنال: نتانیاهو در سفر کوتاه خود به نیویورک به دنبال ترتیب‌دادن دیداری با دونالد ترامپ بود، اما این دیدار محقق نشد.
همزمان، هواپیمای نخست‌وزیر اسرائیل به جای فرود در فرودگاه‌های اصلی نیویورک، در فرودگاه «استوارت» در دره هادسون و حدود ۱۰۰ کیلومتری شمال منهتن به زمین نشست؛ اقدامی که گزارش‌ها آن را در ارتباط با ملاحظات امنیتی و لجستیکی سفر نتانیاهو عنوان کرده‌اند. منابع اسرائیلی همچنین از حضور غیرمعمول نیروهای سرویس مخفی آمریکا در تمهیدات امنیتی سفر او خبر داده‌اند. نتانیاهو پس از سخنرانی در مجمع عمومی سازمان ملل قرار است نیویورک را ترک کند و در این سفر نیز دیداری با ترامپ در برنامه رسمی او قرار نگرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/24013" target="_blank">📅 18:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24012">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، و ملانیا ترامپ در کنار شی جین‌پینگ، رئیس‌جمهور چین، و همسرش پنگ لیویوان، در مراسمی ویژه به تماشای اجرای گارد افتخار نیروی دریایی ایالات متحده نشستند. این یگان ۲۴ نفره که به «گارد افتخار بدون فرمان صوتی» شهرت دارد، مجموعه‌ای از حرکات نظامی و نمایش‌های دقیق با تفنگ را به‌صورت کاملاً هماهنگ و بدون دریافت هیچ‌گونه فرمان کلامی اجرا کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/24012" target="_blank">📅 18:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24010">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شی جین‌پینگ، رئیس‌جمهور چین: بسیار خرسندم که به کشور زیبای شما، ایالات متحده آمریکا، سفر رسمی انجام می‌دهم. از شما، رئیس‌جمهور ترامپ و خانم ترامپ، بابت میزبانی گرمی که برای من و همسرم به عمل آورده‌اید، سپاسگزارم. به نمایندگی از بیش از ۱.۴ میلیارد نفر از مردم…</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/24010" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24009">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f270237e.mp4?token=gW0v5PckKO5tBTIvzGvHMS1YgjxABLC9OxS7GbDAZvZO2bOyeFcElClzG68Zzg2pVsFvqx3408ooqQ3l-i48nDAE7IqZicLPnt0ltjk8QuyK_XT5Qcmbh9TO8ixwOsz-uGp9MwtCnJkHXoP1vc6m1LnK0YN80iHcZ_F4UbKIGklj2Ivzeh8_puG9eVJ3u9QVcE3YK3gr0cMfkpForUjiW94UQ4WmwEyFZg_tuFKCA4lwMRLG6M1BT5fWYJk7Y2LhuwPxl2VfaIJKRufr582ZFHRfG8sbNFkwGB0B0Ku6QPLi-V4wHJ5q97qunCLM3h81IDV_7LdC4q-vGjmdo9ee1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f270237e.mp4?token=gW0v5PckKO5tBTIvzGvHMS1YgjxABLC9OxS7GbDAZvZO2bOyeFcElClzG68Zzg2pVsFvqx3408ooqQ3l-i48nDAE7IqZicLPnt0ltjk8QuyK_XT5Qcmbh9TO8ixwOsz-uGp9MwtCnJkHXoP1vc6m1LnK0YN80iHcZ_F4UbKIGklj2Ivzeh8_puG9eVJ3u9QVcE3YK3gr0cMfkpForUjiW94UQ4WmwEyFZg_tuFKCA4lwMRLG6M1BT5fWYJk7Y2LhuwPxl2VfaIJKRufr582ZFHRfG8sbNFkwGB0B0Ku6QPLi-V4wHJ5q97qunCLM3h81IDV_7LdC4q-vGjmdo9ee1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی جین‌پینگ، رئیس‌جمهور چین:
بسیار خرسندم که به کشور زیبای شما، ایالات متحده آمریکا، سفر رسمی انجام می‌دهم. از شما، رئیس‌جمهور ترامپ و خانم ترامپ، بابت میزبانی گرمی که برای من و همسرم به عمل آورده‌اید، سپاسگزارم. به نمایندگی از بیش از ۱.۴ میلیارد نفر از مردم چین، می‌خواهم با ابراز سلام صمیمانه به مردم آمریکا و تبریک صمیمانه به مناسبت ۲۵۰مین سالگرد استقلال ایالات متحده، آغاز کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/24009" target="_blank">📅 18:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24008">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پرزیدنت ترامپ: رئیس‌جمهور شی اولین رهبر چینی در تاریخ است که دومین سفر رسمی دولتی خود را به آمریکا انجام می‌دهد. @WarRoom</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/24008" target="_blank">📅 18:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24007">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7ca36547.mp4?token=Fxr0rElMXfPt3eHj-wweg5Q35e8VLtkgunBIphdG-xe_-C-QoTzA-YuZXJrGJyQrOxoaI08xekzBpz39Ieoj5AmiN4I05CdGhwbecJWNln8POrYkO3yXmbKHEGDgywTmR7X6n2K_Bw14RlzsPZuYYzem7bCTafXgrz7_QCOQIW4LBmyP3PkFD61gqJebj_vfWCUjIWWMSgTtTOl9VCTkydeoLYd3bR40XQgigFsKoWBLtF6burko-Rb6dtqWCWIMBZz9Y15LITXIkZY-NkApNpOfJPDpBZnQh4rEjPm3XtCpbgqHZdG0u4kILhCzcusM5uTsRCqcAkeQo4cxe5gAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7ca36547.mp4?token=Fxr0rElMXfPt3eHj-wweg5Q35e8VLtkgunBIphdG-xe_-C-QoTzA-YuZXJrGJyQrOxoaI08xekzBpz39Ieoj5AmiN4I05CdGhwbecJWNln8POrYkO3yXmbKHEGDgywTmR7X6n2K_Bw14RlzsPZuYYzem7bCTafXgrz7_QCOQIW4LBmyP3PkFD61gqJebj_vfWCUjIWWMSgTtTOl9VCTkydeoLYd3bR40XQgigFsKoWBLtF6burko-Rb6dtqWCWIMBZz9Y15LITXIkZY-NkApNpOfJPDpBZnQh4rEjPm3XtCpbgqHZdG0u4kILhCzcusM5uTsRCqcAkeQo4cxe5gAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
رئیس‌جمهور شی اولین رهبر چینی در تاریخ است که دومین سفر رسمی دولتی خود را به آمریکا انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/24007" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24006">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شاهزاده باید هرچه زودتر یه فراخوان اقتصادی بده ، حتی اگه اعتصابات هم نبود ، باید فراخوان پرداخت نکردن قبض‌ها و هرگونه تراکنش مالی با رژیم رو اعلام کنه که همه همزمان انجام بدن !!!! خانوم فلانی آقای بیساری که اینجایی برسون به ایشون !
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/24006" target="_blank">📅 18:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24005">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو برای سخنرانی امشبش در سازمان ملل وارد آمریکا شد @WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/24005" target="_blank">📅 17:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24004">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو برای سخنرانی امشبش در سازمان ملل وارد آمریکا شد
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/24004" target="_blank">📅 17:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24003">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT6U4pt6pWID52-wIGNWRqXX2tThOSnl9GaH3SNq7JM-lbHV8VXaBGCJ9v6fdLfLfkCm9cfCrGTfRIP_OI9uE6Xf-wlG4Q7CPn6B0GOQ8Bg2IoIt16F9D-p2HK5xjU9M2fLd6FBi5hm1dqaF1y5qjp-5j3MKcatBLc7Q3pN3T47oHL9Uidah6LsFX-_LTX6ctT1TfbrGVEgqRPMPMAVuuNXkn-air_hZJ6KVr_BIbXLOQcKe_81ELVqjKP5kpskxQkrreFvxExKkDQBfZtJteC5MZRyimTR4BvoP3Hoc5C3Tjlj7eRygaYSFREr5sJeBgdsWCG1sXAWQIdAucA9gRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پل سنگین ترابری نظامی آمریکا در این لحظه. همچنین چهار سوخترسان هم اکنون بر روی تنگه هرمز مشغول انجام عملیات هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/24003" target="_blank">📅 17:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24002">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تنگه صدای فرمانده پیشین هوا فضا سپاه میاد
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/24002" target="_blank">📅 17:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24001">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سی‌ان‌ان: در نشست ترامپ با سران کشورهای عربی در نیویورک، قطر و عراق با هرگونه اقدام نظامی بیشتر علیه ایران مخالفت کردند.
به گزارش CNN، رهبران کشورهای عربی و خلیج فارس تلاش کردند ترامپ را از تشدید بیشتر جنگ با ایران منصرف کنند؛ آنها نگران گسترش جنگ و کشیده‌شدن بیشتر کشورهای منطقه به درگیری هستند
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24001" target="_blank">📅 17:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24000">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری فرانسه:
یحیی رحیم‌صفوی، مشاور رهبر جمهوری اسلامی، هشدار داد اگر آمریکا حملات خود را از سر بگیرد، ایران ممکن است دامنه جنگ را از خلیج فارس و دریای سرخ به اقیانوس هند و حتی فراتر از آن گسترش دهد. این نخستین‌بار است که یک مقام ارشد ایرانی به‌طور صریح از احتمال کشیده‌شدن درگیری به اقیانوس هند سخن می‌گوید.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24000" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23999">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بلومبرگ: ترامپ و شی آتش‌بس تجاری آمریکا و چین را تا ۱۰ ژانویه ۲۰۲۷ تمدید کردند.
این توافق که قرار بود ۱۰ نوامبر منقضی شود، دو ماه دیگر ادامه خواهد داشت و از تشدید دوباره تنش‌های تجاری میان دو اقتصاد بزرگ جهان جلوگیری می‌کند؛ هرچند اختلافات بر سر عناصر کمیاب، محدودیت‌های فناوری و تایوان همچنان پابرجاست.
@WatRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23999" target="_blank">📅 14:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23998">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نیروهای دولتی یمن: سرنگون کردن یک پهپاد متعلق به حوثی‌ها در آسمان منطقه "جبل حبشی" در استان تعز.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23998" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23997">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک منبع اسرائیلی: ایران فعالیت‌های خود برای انتقال و تقویت تأسیسات هسته‌ای در منطقه کوه کلنگ، در نزدیکی نطنز، را افزایش داده است. این منبع مدعی شده در صورت عبور تهران از «خطوط قرمز» تعیین‌شده، اسرائیل بار دیگر برای حمله به تأسیسات هسته‌ای ایران اقدام خواهد…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23997" target="_blank">📅 14:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23996">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سخنگوی ائتلاف: ۶ موشک بالستیک که توسط شبه‌نظامیان حوثی تروریست شلیک شده بود، منهدم شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23996" target="_blank">📅 14:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23995">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سخنگوی دولت بریتانیا به شبکه الجزیره: ما با فرانسه و کشورهای دیگر همکاری می‌کنیم تا طرحی را برای پاکسازی مین‌ها از تنگه هرمز تدوین کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23995" target="_blank">📅 14:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23994">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_p5MGmF8zfB3Lqz65Tv5gTaKkTdHYxhTsilo3ngqPszcIMrVMpJCHpcm26DbYMbEj8na3cnM9UrHRb-X6kvKHiCknUIAax2zHZp0Mu0fNQghOtBxSzsxrLbDXR1jS45ovw8-5JmhAbe6hNSYfnAh-5yvT8pHMaCpuVT2h1qWb6OYf3l7a4QKDgABWRsLYOXyH7BFyDhoqyKVA2fqsQn90LMt78wB6NT41x0zakOcuDQYeLurqJARxcq2WAz96KHoNst0yDk0QPXlicOoxrNgPRsJczU3O8zebU-w2X6OZX-4oFsE2gknj5YdGiiMHtZr-qvawOBQTvX03IK_ImdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدان استاندارد کرج  خودرو ضد شورش زرهی تو جنگ مونده بود زیر آوار از زیر خاک کشیدن بیرون
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23994" target="_blank">📅 14:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23993">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eba653675.mp4?token=bBqUQLfPzFuABof7uXtgL9IS-x2ggDh5D5IC0IztGykN6ephe8d66rC9fEUvv9ptun-YETCwG8kXEmnv82lTEHF5ctyCpZwGZG2IY1FWTXuFZzynyIcMypE4W7HMwkcln-jDDRn91cAeg2ZvGAOClsfTGUplxgnmqbdef78MPOu_IloAiDr8mXfqx-O8682fHnS6LtOvHiLCYq0cPMUz9nSoM-obLriHOolDAvAvg7spWcwqIUfixOU8Isl2yrp5W1jI3BT39ylBMZrncfPTWk7pAsxuWd0xZuZjiWVTiQEHdTt0EMTU5PDrL6JvYRxGDSFV4iXfN6mFqVUpOTzsLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eba653675.mp4?token=bBqUQLfPzFuABof7uXtgL9IS-x2ggDh5D5IC0IztGykN6ephe8d66rC9fEUvv9ptun-YETCwG8kXEmnv82lTEHF5ctyCpZwGZG2IY1FWTXuFZzynyIcMypE4W7HMwkcln-jDDRn91cAeg2ZvGAOClsfTGUplxgnmqbdef78MPOu_IloAiDr8mXfqx-O8682fHnS6LtOvHiLCYq0cPMUz9nSoM-obLriHOolDAvAvg7spWcwqIUfixOU8Isl2yrp5W1jI3BT39ylBMZrncfPTWk7pAsxuWd0xZuZjiWVTiQEHdTt0EMTU5PDrL6JvYRxGDSFV4iXfN6mFqVUpOTzsLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتوبان نیایش ، شرق به غرب، قبل از باکری ,ساعت یازده صبح پنجشنبه @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23993" target="_blank">📅 13:57 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/t-R1rgFxngI6clhi97qQqVAv4oMqzQk82QQEvWl6UYj2-x6DNu8s26iSGo9qanbydk-gOmin22RR8CJbr4Tiyk0lYh4V_iIudttnLieynZnf3fw1gH6no7s0zDRpfzt6h8iQ-Uim_qEz-JLbbJgJO5-cEvnnzOfQBMbPmNPlzvpSu--BVtAeDEF3Ul5xfjDMm-Kzv8avdA5YvyLYP_mFmORnAEd27TSJpBgBY2XrtXThJCal-XXu1UtZmy8QiWlDYirgIfTsiY8PF4AdX6p_VsBDntyQCbcesL83AL6fNVagKlkWLXPL8O9pNsbhUrw2MRxz5vPF5cUDt-53XzuASw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 479K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرنگار تایم:
پس از حملات حوثی‌ها گزارش‌هایی منتشر شد که عربستان از اینکه آمریکا از این کشور دفاع نکرده ناراضی بوده است. رابطه شما با سعودی‌ها چگونه است؟
ترامپ:
خوب است. رابطه‌ام با آنها بسیار خوب است و رابطه خوبی با ولیعهد دارم( پاسخ نمیدهد)
@WarRoom</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/withyashar/24673" target="_blank">📅 17:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ به تایم : خیلی‌ها می‌گویند جنگ با ایران بیش از حد طولانی شده، اما ما در جنگ‌های زیادی سال‌ها جنگیده‌ایم؛ در ویتنام سال‌ها حضور داشتیم، در افغانستان سال‌ها جنگیدیم و در کره هم سال‌ها آنجا بودیم. جنگ ایران حدود شش ماه است ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/withyashar/24672" target="_blank">📅 17:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ درباره ادامه دار بود حمله به ایران به مجله تایم :
من آنها را از بین بردم و می‌توانستم همان‌جا متوقف شوم، اما تصمیم گرفتم ادامه بدهم. وقتی سایت‌های هسته‌ای آنها را با بمب‌افکن‌های B-2 زدیم، آن تأسیسات زیر هزاران تن آوار قرار گرفتند. می‌توانستم همان‌جا متوقف شوم ، اما احساس کردم این کار درست نیست، چون آنها می‌توانستند به شکل دیگری دوباره فعالیت کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/24671" target="_blank">📅 16:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خبرنگار تایم :
شما در اسرائیل بسیار محبوب هستید. آیا اگر گادی آیزنکوت رهبرحزب یاشار در انتخابات اسرائیل پیروز شود، آمریکا می‌تواند با او بهتر از نتانیاهو کار کند؟
ترامپ:
نمی‌دانم. درباره او چیز بدی نشنیده‌ام. اما نباید نتانیاهو را دست‌کم گرفت. بارها او را کنار گذاشته‌شده تصور کرده‌اند، همان‌طور که بارها من را کنار گذاشته‌شده تصور کرده‌اند. من او را دست‌کم نمی‌گیرم
@WarRoom</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/24670" target="_blank">📅 16:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ درباره اسرائیل و ایران‌به مجله تایم :
هدف اصلی من کمک به دفاع از اسرائیل است. ایران نمی‌تواند قدرت هسته‌ای داشته باشد، چون آنها دیوانه هستند و نمی‌توان اجازه داد افراد دیوانه سلاح هسته‌ای داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/24669" target="_blank">📅 16:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز:
چین صادرات سوخت به خارج از هنگ‌کنگ و ماکائو را برای ماه اکتبر متوقف کرده است؛ این تصمیم در شرایط اختلال عرضه ناشی از جنگ ایران و حملات به پالایشگاه‌های روسیه، می‌تواند فشار بیشتری بر بازار جهانی سوخت وارد کند.
@WarRoom</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/withyashar/24668" target="_blank">📅 16:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng64JLq9WIvh0WVNKSdy4xnSfqhF9-FpudpTQgDjnHSNYgILWohdYmVNqiT0rNhaDEEfROD0XhOczffuE5viOY_RqekT9lhWghteRbFL1yBHAFZggtZmZTNqRof-j4nfflDBkvz6pexHowxxlvVNbpi5fxhooiLbSYMY1-DF5OeEki4Wwq3KnHCmZ-Hk0iCqavknnGWeYV2s1P1wR8l023GCG04Wr_N3iD2VCJKKJHw9Km5as4kq5eH9vBvjNzbXiueKnq6sP3xjWzfpijnsibIvXeaDlci8a0jyCotSZRt9qctYci-vv76lKu95AsoIa2-3aMOy_xsE8asq-iASIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل: ارتش اسرائیل دو تروریست را که در حمله ۷ اکتبر به اسرائیل شرکت داشتند، از پای درآورد. یکی از آنها در حمله به کیبوتص بئری و ربودن ۶ نفر (شارون هرتسمن-آویگدوری، نوعام آویگدوری، عدی شوهم، نِوِه شوهم، یاهل شوهم و شوشان هاران) نقش داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/withyashar/24667" target="_blank">📅 16:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ در مصاحبه‌ با مجله تایم:
هزینه‌های مربوط به جنگ ایران برای ما کمتر از درآمدی است که از نفت ونزوئلا در یک ماه به دست می‌آوریم
@WarRoom</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/withyashar/24666" target="_blank">📅 16:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ به مجله تایم : ممکن است ایران نابود شود ، این یک احتمال است چون احتمالا دارد پس از انتخابات میان‌دوره‌ای، حملات به ایران را بیشتر کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/24665" target="_blank">📅 16:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24664">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو: ما همچنان در حال بررسی دلایل حادثه هواپیمای شرکت "فلای دبی" هستیم و می‌دانیم که کمک خلبان،
تحت یک فرآیند آموزش ایدئولوژیک افراطی
قرار داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/24664" target="_blank">📅 16:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ به مجله تایم: فکر نمی‌کنم ما هرگز با ایران به صلح دست پیدا کنیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/24663" target="_blank">📅 16:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24662">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو: «ظرف چند روز آینده متوجه میشم که آیا کمک‌خلبان ارتباطی با ایران داشته است یا خیر.»
@WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/24662" target="_blank">📅 15:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تتر ۲۵۸،۱۰۰
بیتکوین ۸۳،۹۹۰
نفت برنت : ۹۹،۸۰
@WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/24661" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دونالد ترامپ با روزنامه تایم: خبرنگار: آیا در نظر دارید که قبل از پایان دوره ریاست‌جمهوری خود، اعضای دولت خود را مورد عفو قرار دهید
دونالد ترامپ: بله، قطعا این کار را خواهم کرد؛ جو بایدن که به خواب علاقه زیادی دارد، برای همه عفو صادر کرد؛ من بالاترین ضریب هوشی را دارم. من بالاترین را بین همگی دارم و بسیار خوب هستم
@WarRoom</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/24660" target="_blank">📅 15:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترابری نظامی خیره‌کننده و عجیب آمریکا از ۲۴ ساعت گذشته تا همین لحظه…
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/24659" target="_blank">📅 15:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ به مجله تایم : اگر من رئیس‌جمهور نبودم، امروز عربستان و اسرائیلی وجود نداشت
@WarRoom</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/24658" target="_blank">📅 15:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db5c82ed3.mp4?token=lHcwJP4VvhNG9s1rV7O7eVrRTLe1Xhes243i5YtTRzZtzf0CDtV1GcpthVOzQxHaPKeps88zcbfdLbXZZy72tuvoYy7TE1slKwrcCcB4g_RaLDZUzDidD-aE-Z74HW0yoEiXPWZSxBa2bkxf7d_Xj5xDrtLUwH6lfhn1I-BDs9puGMqEu4C3Zp6iWGSMtZlJD-yRc8kWu4A_CGHzSUnZ0WbyEzKeNetzt1t5oJKNdLf1XFV6t6gy6HSQINjt1spoCVhnpzT8oOa1ncQKFVjpfBgoauQiygK_SPFGbgyoqYqrT12XAe13vXv-BYJv-lXUnmZlDfeB0BPD91iTUjc6_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db5c82ed3.mp4?token=lHcwJP4VvhNG9s1rV7O7eVrRTLe1Xhes243i5YtTRzZtzf0CDtV1GcpthVOzQxHaPKeps88zcbfdLbXZZy72tuvoYy7TE1slKwrcCcB4g_RaLDZUzDidD-aE-Z74HW0yoEiXPWZSxBa2bkxf7d_Xj5xDrtLUwH6lfhn1I-BDs9puGMqEu4C3Zp6iWGSMtZlJD-yRc8kWu4A_CGHzSUnZ0WbyEzKeNetzt1t5oJKNdLf1XFV6t6gy6HSQINjt1spoCVhnpzT8oOa1ncQKFVjpfBgoauQiygK_SPFGbgyoqYqrT12XAe13vXv-BYJv-lXUnmZlDfeB0BPD91iTUjc6_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو، درباره ایران: ببینید، ما فقط سر راه آنها هستیم. ما مانع آنها برای فتح سراسر خاورمیانه هستیم، اما هدف اصلی، شما، آمریکا، هستید. به همین دلیل است که آنها شعار می‌دهند آنها ما را
«شیطان کوچک»
می‌نامند و
شما را «شیطان بزرگ»
، و آنها به دنبال از بین بردن «شیطان بزرگ» هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/24657" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ درباره طولانی شدن جنگ با ایران: خودم خواستم جنگ را ادامه دهم
خبرنگار تایم از ترامپ پرسید: «ابتدا گفته بودید جنگ ایران حدود شش تا هشت هفته طول می‌کشد؛ اکنون وارد ماه هفتم شده‌ایم. چرا جنگ این‌قدر طولانی شده است؟»
ترامپ پاسخ داد: «فقط به این دلیل که می‌خواستم جلوتر بروم. آن‌ها را از میدان خارج کردم و همان زمان می‌توانستم جنگ را متوقف کنم، اما می‌خواستم ادامه دهم.»
@WarRoom</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/24656" target="_blank">📅 15:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: ما سلاح‌های زیادی داریم و وضعیت ما عالی است. در حال حاضر، حجم زیادی از سلاح‌ها را ذخیره کرده‌ایم و آن‌ها را نگه داشته‌ایم و به متحدان خود توزیع خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/24655" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس جمهور ایران: آمریکا باید از این خیال پوچ که می‌تواند ما را از طریق ترور و آدم‌کشی وادار به تسلیم کند، دست بردارد. @WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/24654" target="_blank">📅 15:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دونالد ترامپ در مصاحبه با مجله تایم: وضعیت ایران بسیار وخیم است و اقتصاد آن‌ها در حال فروپاشی است. آن‌ها می‌خواهند یک توافق انجام دهند، اما من می‌خواهم یک توافق واقعی داشته باشم.
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/24652" target="_blank">📅 15:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رئیس جمهور ایران: آمریکا باید از این خیال پوچ که می‌تواند ما را از طریق ترور و آدم‌کشی وادار به تسلیم کند، دست بردارد.
@WarRoom</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/24651" target="_blank">📅 15:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ درباره ایران : ایرانی‌ها پیشنهادی برای باز کردن تنگه هرمز ارائه کردند. من برخی از جنبه های آن را بررسی کردم، اما نه همه آن، اما به سادگی کافی نیست.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/24650" target="_blank">📅 15:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24649">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مجله تایم: ترامپ احتمال افزایش حملات هوایی به ایران پس از انتخابات میان‌دوره‌ای را مطرح کرده است @WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/24649" target="_blank">📅 15:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مجله تایم: ترامپ احتمال افزایش حملات هوایی به ایران پس از انتخابات میان‌دوره‌ای را مطرح کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/24648" target="_blank">📅 14:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">در‌ انتظار‌ تایید : در همین لحظه خواهر عباس عراقچی، پری سادت عراقچی، (لواسانی)، رئیس انجمن دیپلماتیک بانوان وزارت خارجه، ریق رحمت را سر کشید و مرد @WarRoom دیروز شایعه مردن میرحسین موسوی هم پخش شد که تکذیب شد</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/24647" target="_blank">📅 14:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزارت خارجه امارات: دادستان کل دستور تشکیل تیم ویژه‌ای از دادستانی عمومی را برای تحقیق درباره حادثه پرواز فلای دبی و نقش احتمالی ایران صادر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/24646" target="_blank">📅 13:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COABT9j8FQUSRTuGRLb4Wk4LigFWe2iWXXBI5NYMiipRwhMJuVBHDoe2VnYk92FpL5TZbGR94QfyeQxvw0ZaaOc0-wCIhzZJTssOsSyJriFisghFkY_O-uoZ0VAlNU2Lwf83pfBAVfFv8lhu9ObHUW9SXgfaMMKl5zfyjldIsugElo8GuS3VnwlrWLsEfXmWtBzdwAYHqlxfB_3O1Fad1EGUDNIXBvImbFD7Re64aiXd4yHK6GjtmxQ3PegrklNsEUXxKPBybJevyAH9xCM2rb1JlmEpmy7oBk4_2CnqgGn171y4KRl-PZ6O0yegiIb1_xBHZDvIFg5go70nu4g4Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گزارش نیویورک‌پست درباره هشدار اسکات بسنت درباره اقتصاد ایران رو بازنشر کرد.
بسنت: احتمالا ظرف دو هفته چیزی از اقتصاد ایران باقی نمی ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/24645" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ویدئوی جدید شرکت اسرائیلی XTEND؛ نمایش سناریوی عملیات نیروهای آمریکایی با پهپادهای تهاجمی در ایران:
شرکت XTEND که در سال
۲۰۱۸ در تل‌آویو
تأسیس شده و دفتر مرکزی آن اکنون در
تامپای فلوریدا
قرار دارد، ویدئویی تبلیغاتی از عملیات زمینی نیروهای آمریکایی در کویر ایران منتشر کرده است که با پهپاد شکارچی حمله ایرانی ها را دفع و با مدل انتهاری به ایرانی ها حمله و آنها را نابود میکنند. این شرکت می‌گوید سامانه‌هایش در
عملیات واقعی هم علیه ایران
استفاده شده و سابقه همکاری با وزارت دفاع و ارتش اسرائیل را دارد؛ همچنین در سال ۲۰۲۵ قراردادی برای تأمین
هزاران پهپاد FPV
برای نیروهای زمینی اسرائیل را تکمیل کرده. اهمیت این ویدئو در این است که XTEND هفته پیش اعلام کرد وارد فاز سوم برنامه پهپادهای تهاجمی
نیروهای عملیات ویژه آمریکا (USSOCOM)
شده است؛ پروژه‌ای شامل
STRIKER، Scorpio 500 و Scorpio 1000
برای شناسایی، عملیات در محیط‌های شهری و بسته که حملات دقیق با پهپادهای قابل‌بازیابی و گروه‌های پهپادی را شامل میشود
@WarRoom</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/24644" target="_blank">📅 13:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb859cb846.mp4?token=mKbWLTPHHs5VD-bq77U2l11VcgrLObsHerOepm757iGVClypmM4fbZ4pI85S00DDjrWwfopvL2hfZd67NNKVdM1wQ0UYoR9Ujp0FWtqXq8cKsyLKlQ8jfUBEXvk7FEql4X6sEthsZD-Pr46VbSxAXvKjRpIDvIf-yvcPcMCS4n7MKFG5xy_kAM9TKgMLg2VH2MhbsEHnTBBLJtfvw1HB9lYbK3lEv1O5lGml-gnZYM4-__xJUdx3KNgG1eUhEbx2OMf7a3yPVr8uPNvgsH8Q-UhmniyXXTZPVDxiJ2s5GZpK9FNowB-kbahhGul_zbWSuzs1NU2uPVXqBLrn3xIMTWbCbdUXWV79kdZwar8zOHYPqQNPXqtdWz5TlRSEXm2QUGM6cD0CK2e-kbCE5xHvPj20cUQm_xfQCym_BsBICIt-EfymiSNoIwDOSwsSviBX4E5gd4vVX7EnH7MaTEqkpR6y0waSdC-dSnXzzowhFWK20gEtdBrmzDLGOKJUWTyzhQmGXenQFCYhjioUp8Z77Gof1ClfIypETUAxN3ePzbHKTXwdFYsPs08i_9P39nH2YW0zB1O-4wN9NqqY21TjmyoY01UHba_ZF8lqzaTGTS4e4w7_i8tm-NuKV4cRnkp57MAzZmMJUoIp2jcJbDs2yLz451OmL6o3AlbOydUdO-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb859cb846.mp4?token=mKbWLTPHHs5VD-bq77U2l11VcgrLObsHerOepm757iGVClypmM4fbZ4pI85S00DDjrWwfopvL2hfZd67NNKVdM1wQ0UYoR9Ujp0FWtqXq8cKsyLKlQ8jfUBEXvk7FEql4X6sEthsZD-Pr46VbSxAXvKjRpIDvIf-yvcPcMCS4n7MKFG5xy_kAM9TKgMLg2VH2MhbsEHnTBBLJtfvw1HB9lYbK3lEv1O5lGml-gnZYM4-__xJUdx3KNgG1eUhEbx2OMf7a3yPVr8uPNvgsH8Q-UhmniyXXTZPVDxiJ2s5GZpK9FNowB-kbahhGul_zbWSuzs1NU2uPVXqBLrn3xIMTWbCbdUXWV79kdZwar8zOHYPqQNPXqtdWz5TlRSEXm2QUGM6cD0CK2e-kbCE5xHvPj20cUQm_xfQCym_BsBICIt-EfymiSNoIwDOSwsSviBX4E5gd4vVX7EnH7MaTEqkpR6y0waSdC-dSnXzzowhFWK20gEtdBrmzDLGOKJUWTyzhQmGXenQFCYhjioUp8Z77Gof1ClfIypETUAxN3ePzbHKTXwdFYsPs08i_9P39nH2YW0zB1O-4wN9NqqY21TjmyoY01UHba_ZF8lqzaTGTS4e4w7_i8tm-NuKV4cRnkp57MAzZmMJUoIp2jcJbDs2yLz451OmL6o3AlbOydUdO-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس پایانی تایتانیک…
سکانس پایانی رژیم هم یه نوازنده ویلون نداشت که اومد…
@WarRoom</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/24643" target="_blank">📅 12:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52888268eb.mp4?token=V-XewfpY6Uk3mkYq7_sB_6uDio5Vkd_pKiOWbUGg9LlARgowpB-E5DvuRoLdXC-ryVJht-YED4VKufAZ_OYrjvxIfOiumOSAr3q7yXxSb0DBJQXJlbq9ksWLgcnGalxeZm4A0YY61-gxaaRMh56SBunJHoyAwOxIfGHJoLufWALGHUlrBry1FI41AZuSE-bG5lRaLjiLG1S5Rst5vGXWPmGmNmgpskVml46geJYBLFzao_JErbYzwTX6EQN2dOQKrbKFKRlVJtw-aajQiSCjBfm-5AzvhmrUKti5G_oSMf4Qck6OOhFrDcR5Rh3reMW3AmtWPD4cv6-fxHpjtoyDkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52888268eb.mp4?token=V-XewfpY6Uk3mkYq7_sB_6uDio5Vkd_pKiOWbUGg9LlARgowpB-E5DvuRoLdXC-ryVJht-YED4VKufAZ_OYrjvxIfOiumOSAr3q7yXxSb0DBJQXJlbq9ksWLgcnGalxeZm4A0YY61-gxaaRMh56SBunJHoyAwOxIfGHJoLufWALGHUlrBry1FI41AZuSE-bG5lRaLjiLG1S5Rst5vGXWPmGmNmgpskVml46geJYBLFzao_JErbYzwTX6EQN2dOQKrbKFKRlVJtw-aajQiSCjBfm-5AzvhmrUKti5G_oSMf4Qck6OOhFrDcR5Rh3reMW3AmtWPD4cv6-fxHpjtoyDkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیلی مک‌انانی
،
فاکس نیوز:
«واقعاً چقدر ساده‌لوحانه است که فکر کنیم شعار «مرگ بر آمریکا» معنای دیگری دارد؟ سپاه پاسداران می‌گوید این شعار هیچ خصومتی با مردم آمریکا ندارد، اما هم‌زمان از آمریکایی‌ها می‌خواهد علیه دولت ترامپ موضع بگیرند. انتخابات آمریکا پیامد دارد؛
ایران این را می‌داند، کارتل‌ها می‌دانند و چین هم می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/24642" target="_blank">📅 12:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60c71917d.mp4?token=N9kU4WTOvgcwPYA3GnCFlqPdq8Srd_BM8ZDzmzRCZnmNxYfWafHlrqV47amwdOwIeWq4yNDc4FgdI3e0kmBhHEg_sehbbPuhjlHQc0gR7BnWWFs9zDDyEQmQcMe4s-WfqvJFWf8moBVwk3kUkn5iT2SkLKnnPm0E1j-Vx8R9mrrU4GmqIXAjzz8Ia3nUl3cGz3_w4IOz-gjCs_TOgt9DP8X8SqSRhd0DFwviuwDaojYLkSSEwsJ42-PdKVEi7MFy6i_dbxLsfy1wLwKLGeK-gN-5zQgSDOuj3KoGhBIJ3n9qvD9SiqUJiIK4AxmLeO8kHRxenlrRN9pqzJ7O0AA7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60c71917d.mp4?token=N9kU4WTOvgcwPYA3GnCFlqPdq8Srd_BM8ZDzmzRCZnmNxYfWafHlrqV47amwdOwIeWq4yNDc4FgdI3e0kmBhHEg_sehbbPuhjlHQc0gR7BnWWFs9zDDyEQmQcMe4s-WfqvJFWf8moBVwk3kUkn5iT2SkLKnnPm0E1j-Vx8R9mrrU4GmqIXAjzz8Ia3nUl3cGz3_w4IOz-gjCs_TOgt9DP8X8SqSRhd0DFwviuwDaojYLkSSEwsJ42-PdKVEi7MFy6i_dbxLsfy1wLwKLGeK-gN-5zQgSDOuj3KoGhBIJ3n9qvD9SiqUJiIK4AxmLeO8kHRxenlrRN9pqzJ7O0AA7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏درگیری مسلحانه شدید در زاهدان ادامه دارد ؛ صدای تیراندازی و شلیک آرپی‌جی
‏از حدود ساعت ۶ صبح درگیری مسلحانه میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح بومی در منطقه منزل‌آب زاهدان آغاز شده و همچنان ادامه دارد. صدای تیراندازی سنگین و شلیک آرپی‌جی از منطقه شنیده می‌شود و تاکنون گزارشی از شمار کشته‌ها یا مجروحان منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/24641" target="_blank">📅 11:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آسوشیتدپرس:
ایران تأیید کرد پاسخ رسمی آمریکا به پیشنهاد تهران برای پایان جنگ را دریافت کرده است؛ جزئیات پاسخ هنوز منتشر نشده و موضع ترامپ درباره این طرح همچنان منفی است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/24640" target="_blank">📅 11:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">در‌ انتظار‌ تایید : در همین لحظه خواهر عباس عراقچی، پری سادت عراقچی، (لواسانی)، رئیس انجمن دیپلماتیک بانوان وزارت خارجه، ریق رحمت را سر کشید و مرد @WarRoom دیروز شایعه مردن میرحسین موسوی هم پخش شد که تکذیب شد</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24639" target="_blank">📅 11:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">در‌ انتظار‌ تایید : در همین لحظه خواهر عباس عراقچی، پری سادت عراقچی، (لواسانی)، رئیس انجمن دیپلماتیک بانوان وزارت خارجه، ریق رحمت را سر کشید و مرد
@WarRoom
دیروز شایعه مردن میرحسین موسوی هم پخش شد که تکذیب شد</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24638" target="_blank">📅 10:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24637">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آژانس ایمنی هوانوردی اتحادیه اروپا (EASA):
توصیه‌های محدودیت پروازی بر فراز
ایران، عراق، لبنان و آب‌های سرزمینی خلیج فارس و دریای عمان در محدوده بحرین، کویت، قطر، امارات و عمان
تا
۱۶ نوامبر
تمدید شد. EASA همچنین از امروز محدودیت جداگانه‌ای برای بخش‌هایی از حریم هوایی
عربستان سعودی
صادر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24637" target="_blank">📅 10:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec6681269.mp4?token=quJuWVwh-L1xwBmL10LCILWN8mFMpAG-knZc154T6suu5ETtcCyMmYnmAqzljqW8q3TOxuvacZNWvuD_f7k6dgMNzCm9Bejsuhr1DOwb5L5HPXMlWjUwAbAqkpdsD0Jo2lrRY3rcIXC5eZyyBNQ6Fu3B23xJFEJlrVt3RwtJ3A76vSuPnKslKYKb3OvHe1YPKGX8kSws1lG6UWyBwuFGQVEl0tW5k694OJVuqFKGE4LHsgABSrGIsM9NBriiMxvG8kZLxUUf4VhwFHFeCoVTSt2M4wHCtYkDC3PWck3tWUhAHdTxow3NyUot1CWfLzThbi-_b1wHd7n7eDS9XvZTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec6681269.mp4?token=quJuWVwh-L1xwBmL10LCILWN8mFMpAG-knZc154T6suu5ETtcCyMmYnmAqzljqW8q3TOxuvacZNWvuD_f7k6dgMNzCm9Bejsuhr1DOwb5L5HPXMlWjUwAbAqkpdsD0Jo2lrRY3rcIXC5eZyyBNQ6Fu3B23xJFEJlrVt3RwtJ3A76vSuPnKslKYKb3OvHe1YPKGX8kSws1lG6UWyBwuFGQVEl0tW5k694OJVuqFKGE4LHsgABSrGIsM9NBriiMxvG8kZLxUUf4VhwFHFeCoVTSt2M4wHCtYkDC3PWck3tWUhAHdTxow3NyUot1CWfLzThbi-_b1wHd7n7eDS9XvZTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در
مورد
اسلامگرایان تندرو
:
ما در حال مبارزه با
بربرها
هستیم؛ این افراد
بربر
هستند.
(منظور او از «بربرها» افراد بی تمدن و وحشی است
)
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24636" target="_blank">📅 10:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85883a33b.mp4?token=i_zUH_pyi3q-d5YUSQhCFLMtI_KgGmt6Z_GG5cr2l7R5PWw11BolX_ZYT0O5G296wS9sqhoeh-nfOXkCkv7ArnEZPxLFzwo5llipffifToipiIwGtSehWGzr2EfEUXr5dL0lgUdYsn7SsO4f-npQhrgewin8xCD4lkjFtTcIiFAGij0SCd58FoWO1fzlnpwo_zid5nVmImFJio5T3uYPQNKmTI5R7hiFmN4E4CLHYtTIPfco0CZp_kxF6zhRB3097p85fdKnqZAM4SU72yYrX2GwxS3Nz7Kop8ZSXFhrcOFCxYhzoXtH-9nS4__KXELvoh3wHdow3ihLyAT0fSBJqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85883a33b.mp4?token=i_zUH_pyi3q-d5YUSQhCFLMtI_KgGmt6Z_GG5cr2l7R5PWw11BolX_ZYT0O5G296wS9sqhoeh-nfOXkCkv7ArnEZPxLFzwo5llipffifToipiIwGtSehWGzr2EfEUXr5dL0lgUdYsn7SsO4f-npQhrgewin8xCD4lkjFtTcIiFAGij0SCd58FoWO1fzlnpwo_zid5nVmImFJio5T3uYPQNKmTI5R7hiFmN4E4CLHYtTIPfco0CZp_kxF6zhRB3097p85fdKnqZAM4SU72yYrX2GwxS3Nz7Kop8ZSXFhrcOFCxYhzoXtH-9nS4__KXELvoh3wHdow3ihLyAT0fSBJqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران
به CNN
:
این یک
رژیم افراطی و بی‌پروا
است و نباید سلاح هسته‌ای داشته باشد؛ این موضوع کاملاً روشن است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24635" target="_blank">📅 09:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4854e3d13b.mp4?token=nsRz6sjftTLsoQTLYYVESQtXCll_6yjh2Qi6c_Bt5bYjEQSys7Sci1PH4I6jYA4O48ze8up4XnZR1-Fg3ZSLFOtRKLhf7bSDSlUGTGGUA-AD5ySoMtjG2niu9b3R7qSohnw2hM-96y8f_H2mWYxUyHuY-CL-BnGTK0DhCjj0Z9iW-0s1c0Xr1wV1Q4Wn18ksdRHlkKmVsHjjkA0sdLhKHdk9GzlwpDWyHxusSLFjsPcp3lWzi5pao7Ai77gtqi7ABw__shWQU_UBipjwAlxEEQUbY4f3MQB6mlnleJoKBfQmGwYWDHr-C_LcLb8MTD1Oqdf3OBnYydBrViWmpmeUEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4854e3d13b.mp4?token=nsRz6sjftTLsoQTLYYVESQtXCll_6yjh2Qi6c_Bt5bYjEQSys7Sci1PH4I6jYA4O48ze8up4XnZR1-Fg3ZSLFOtRKLhf7bSDSlUGTGGUA-AD5ySoMtjG2niu9b3R7qSohnw2hM-96y8f_H2mWYxUyHuY-CL-BnGTK0DhCjj0Z9iW-0s1c0Xr1wV1Q4Wn18ksdRHlkKmVsHjjkA0sdLhKHdk9GzlwpDWyHxusSLFjsPcp3lWzi5pao7Ai77gtqi7ABw__shWQU_UBipjwAlxEEQUbY4f3MQB6mlnleJoKBfQmGwYWDHr-C_LcLb8MTD1Oqdf3OBnYydBrViWmpmeUEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره بریتانیا
و
ایران:
ما اطلاعاتی در اختیار بریتانیایی‌ها قرار دادیم که نشان می‌داد قرار است یک
حمله با حمایت ایران
انجام شود، اما تقریباً روز بعد، آنها علیه ما تحریم وضع کردند. واقعاً عجیب است؛
عقب‌نشینی و فروپاشی در برابر ائتلاف اسلام‌گرایان و مارکسیست‌ها
برای آینده غرب بسیار خطرناک است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24634" target="_blank">📅 09:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e94c9fbb.mp4?token=UrNHLnJH3v5jU9wAtCT7neA3eMH07s2iyF8YtaS-n2zFZsy2cr36PujgbfXBMDoVcfBBY5jPqKF5BPtXSzLEHI2wyt3neEPTBqsqwl93PkoA6hO4GRSbbcLEWQ3ki7XzWW3YJ5t_rEvL0Ft7f1UnackGlk0zSaNEusRIFvWCfFNUNxTzfk-m1b5fpKibtBUoEQc5ME76E9o3a9dRqLyxCgVvCvd5DinIklqyq8y-kgtpGP1jG9EcAAinL-cIhfeQD6dUQ0K8Aa7Ve8CfFWPHHpbV8n9Kvs50138QM9juTV8iyZcsbmi94Neee-yB4HxpW2ty_7bqbVPJk5NsOpNtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e94c9fbb.mp4?token=UrNHLnJH3v5jU9wAtCT7neA3eMH07s2iyF8YtaS-n2zFZsy2cr36PujgbfXBMDoVcfBBY5jPqKF5BPtXSzLEHI2wyt3neEPTBqsqwl93PkoA6hO4GRSbbcLEWQ3ki7XzWW3YJ5t_rEvL0Ft7f1UnackGlk0zSaNEusRIFvWCfFNUNxTzfk-m1b5fpKibtBUoEQc5ME76E9o3a9dRqLyxCgVvCvd5DinIklqyq8y-kgtpGP1jG9EcAAinL-cIhfeQD6dUQ0K8Aa7Ve8CfFWPHHpbV8n9Kvs50138QM9juTV8iyZcsbmi94Neee-yB4HxpW2ty_7bqbVPJk5NsOpNtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران
به CBS
:
آنها در تلاش‌اند
سلاح‌های هسته‌ای و ابزارهای لازم برای رساندن آن به هر شهر آمریکا
را توسعه دهند. این کار مدتی زمان خواهد برد، اما آنها در حال کار روی آن هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/24633" target="_blank">📅 09:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/919a200a36.mp4?token=cvxwDMUB1f82O2JzmeyA4s5PR8qSrZRNinOQPHM0_YQYR4LLDCuKdSw1VcgjhXXQU70N4XHmIxD61z-EBCx2wXCFQKfryiJciToG5Sl37b24uJjHLusdHbO9hZq6VxaR7ucOH7fLZO1qD3VnSvK0vI1OqGd5yOVugTAdnSTiboypscrQp2x5S1k62Bmmy3UPmoIpPQUf834IccQdsO154OIKvsZt1hrfqMvHRw4B0DwuBLkcuBUN8RbRcbO-5quKJmbZhHvMrMRMIUGg57WYWmu63BLThXXbgXy0Cr6AvhvDIkn7kgz4H8ScDEeC-ciJ48x3MiaQZadqyydpmCFY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/919a200a36.mp4?token=cvxwDMUB1f82O2JzmeyA4s5PR8qSrZRNinOQPHM0_YQYR4LLDCuKdSw1VcgjhXXQU70N4XHmIxD61z-EBCx2wXCFQKfryiJciToG5Sl37b24uJjHLusdHbO9hZq6VxaR7ucOH7fLZO1qD3VnSvK0vI1OqGd5yOVugTAdnSTiboypscrQp2x5S1k62Bmmy3UPmoIpPQUf834IccQdsO154OIKvsZt1hrfqMvHRw4B0DwuBLkcuBUN8RbRcbO-5quKJmbZhHvMrMRMIUGg57WYWmu63BLThXXbgXy0Cr6AvhvDIkn7kgz4H8ScDEeC-ciJ48x3MiaQZadqyydpmCFY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
بر کسی پوشیده نیست که ایران می‌خواهد اسرائیلی‌ها را در خارج از کشور هدف قرار دهد و در داخل اسرائیل نیز به دنبال حمله است؛ ما این را می‌دانیم. در واقع، ما نشانه‌هایی می‌بینیم که نه‌تنها ایران، بلکه نیروهای نیابتی آن، از جمله
حماس و حزب‌الله
، به دنبال انجام حملاتی پیش از انتخابات هستند و ما شواهد روشنی در این زمینه داریم. اما اینکه
حادثه فلای‌دبی نیز بخشی از این طرح بوده یا نه، هنوز نمی‌دانیم.
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/24632" target="_blank">📅 09:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0159708785.mp4?token=raQkbQ8R7WRy9ogR0rWB94PF7XKxA6ddDuH2To7936ssadIWWfM1pHzRf2MPSIMsjuzPupWrETr6JRttWFrRid97hT5IHiiqLg9agBNorbM1rRjWN6ZaVXNomDOvOYOGvAWDW-fPnrDkOqjs7B9tXP8KE7cKPRrLPkLbO_G7EOrjb4kUaoPBG0Waz5mpQZlewJ-v2KTCnsm9moBEF4uKVlYeD8TJ9ZfrJ8ckY2sTHhWKNpp9qKxLA6gPbCK_pDpgkj20c7z51REKYZHIfmVs0EackDJB9LyFDcFka4oWOBGxm5J27FeiYgkxDJ6OYDpx7IyAGXjK30ukcNM9DyJjdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0159708785.mp4?token=raQkbQ8R7WRy9ogR0rWB94PF7XKxA6ddDuH2To7936ssadIWWfM1pHzRf2MPSIMsjuzPupWrETr6JRttWFrRid97hT5IHiiqLg9agBNorbM1rRjWN6ZaVXNomDOvOYOGvAWDW-fPnrDkOqjs7B9tXP8KE7cKPRrLPkLbO_G7EOrjb4kUaoPBG0Waz5mpQZlewJ-v2KTCnsm9moBEF4uKVlYeD8TJ9ZfrJ8ckY2sTHhWKNpp9qKxLA6gPbCK_pDpgkj20c7z51REKYZHIfmVs0EackDJB9LyFDcFka4oWOBGxm5J27FeiYgkxDJ6OYDpx7IyAGXjK30ukcNM9DyJjdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در گفت‌وگو با فاکس‌نیوز:
به ریشه این حمله‌کننده خواهیم رسید؛ اینکه آیا همدستانی داشته و آیا ایران پشت این ماجرا بوده است. فکر می‌کنم خیلی زود مشخص خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/24631" target="_blank">📅 09:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">واشنگتن‌پست:
به گفته یک مقام ارشد دفتر نخست‌وزیری عراق،
سپاه پاسداران تاکتیک خود در عراق را تغییر داده
و به‌جای گروه‌های بزرگ، از
هسته‌های کوچک‌تر
و خارج از ساختارهای اصلی شبه‌نظامیان حمایت می‌کند. همچنین
عصائب اهل‌الحق
حدود نیمی از سلاح‌های خود را به دولت عراق تحویل داده، اما اعضای جداشده با تشکیل
یک گروه جدید
، بخشی از سلاح‌های باقی‌مانده را در اختیار گرفته‌اند. به گفته این مقام، این گروه جدید با
سپاه و انصارالله یمن
همکاری دارد و در حملات به
زیرساخت‌های انرژی عربستان
نیز نقش داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/24630" target="_blank">📅 08:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رویترز: آمریکا برای شناسایی بهتر انفجارهای هسته‌ای، آزمایش انفجاری زیرزمینی انجام داد.
سازمان ملی امنیت هسته‌ای آمریکا در سایت امنیت ملی نوادا یک
انفجار شیمیایی پرقدرت، بدون استفاده از مواد هسته‌ای
انجام داد. هدف آزمایش، تقویت توانایی آمریکا برای شناسایی انفجارهای هسته‌ای کم‌توان و به‌ویژه آزمایش‌هایی با «اتصال کاهش‌یافته» به زمین بود؛ روشی که می‌تواند
آثار لرزه‌ای انفجار
را کاهش دهد. واشنگتن مدعی است چین در ژوئن ۲۰۲۰ از این روش برای کاهش قابلیت شناسایی یک آزمایش هسته‌ای در سایت لوپ‌نور‌ برای ‌مخفی کردن آزمایشات هسته‌ای استفاده کرده است؛
چین این اتهام را رد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/24629" target="_blank">📅 08:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe0100bea.mp4?token=GZjvyRrAL8OtJFSCdp1OZW3W3XJqPqoEQjMhNodBRBtz4alViYgpfjrUrgEgOEI6kMpGMX7887sM3nHgJMn1q7u9ZfuKMjOX15OYj22xcMWuFpn3Xy4iboSzl4OYv38Xmqz85sN4PHSBmwhgCN-MMcSPP--Va8tNhoT04hzgOhAqJ1KlNY6t0HoxFKwaLDhXESDGLp8QpuR0gErJPHc74Yn9d8BfXMRcKRWBqfkoUG451uZTAEi4DNYVNF1jqj62hlDo2XTBglEn3941CP_uJi2IMVMZ__-XerAK6UOPjlTKm2h0Fux9F16MbGWbybPWKIoyq8fR8NThR3CGo2h-nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe0100bea.mp4?token=GZjvyRrAL8OtJFSCdp1OZW3W3XJqPqoEQjMhNodBRBtz4alViYgpfjrUrgEgOEI6kMpGMX7887sM3nHgJMn1q7u9ZfuKMjOX15OYj22xcMWuFpn3Xy4iboSzl4OYv38Xmqz85sN4PHSBmwhgCN-MMcSPP--Va8tNhoT04hzgOhAqJ1KlNY6t0HoxFKwaLDhXESDGLp8QpuR0gErJPHc74Yn9d8BfXMRcKRWBqfkoUG451uZTAEi4DNYVNF1jqj62hlDo2XTBglEn3941CP_uJi2IMVMZ__-XerAK6UOPjlTKm2h0Fux9F16MbGWbybPWKIoyq8fR8NThR3CGo2h-nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری سی‌بی اس: چه چیزی شما را مطمئن می‌کند که حادثه فلای دوبی یک اقدام تروریستی بوده است و نه یک مشکل روانی؟
نخست‌وزیر اسرائیل، نتانیاهو: خب، ممکن است اینطور باشد. من نمی‌دانم. به زودی متوجه خواهیم شد.ما نشانه‌هایی داشتیم که ایران، و به ویژه از طریق عوامل خود، قصد داشت حملات تروریستی علیه اسرائیل و شهروندان اسرائیلی در خارج از کشور را افزایش دهد.اما فکر می‌کنم که هنوز خیلی زود است که بگوییم آیا در این ماجرا همدستی ایرانی وجود داشته است یا خیر. فکر می‌کنم به زودی متوجه خواهیم شد
@WarRoom</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/24628" target="_blank">📅 08:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24627">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae8a735a2.mp4?token=TPw9ZWfC2t2cMQmNTtt6eHuLezO4y0OKUyVXtbM6d2PdajviU499OGkE8Pm5OX_k4Dc_BDWCHpqGLNbS_dCnGjdcg9j2_uZh1BxPEWuZirc226QW-6aVOmhGoIi9SUtIU_KmSyvDCL7HvQnEQIf4-UWq2yl_MxN1ZOeiI6c8UvuMIC_xCR9NZ669wDIBL0Qu7m7ZpBjSrIcMxqUAMQJxDdrXwkNtz4lx-EADvJavSkCOtYTA1wyDaA-JsZXATzwI9KusXPpj0VIo_8PqJy0J6DsveWYgZPIrlM7HTwD6qsI6en3NIpuLx-fDTUAiXBFUFdZmNfPp5QbnRvzwPqo-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae8a735a2.mp4?token=TPw9ZWfC2t2cMQmNTtt6eHuLezO4y0OKUyVXtbM6d2PdajviU499OGkE8Pm5OX_k4Dc_BDWCHpqGLNbS_dCnGjdcg9j2_uZh1BxPEWuZirc226QW-6aVOmhGoIi9SUtIU_KmSyvDCL7HvQnEQIf4-UWq2yl_MxN1ZOeiI6c8UvuMIC_xCR9NZ669wDIBL0Qu7m7ZpBjSrIcMxqUAMQJxDdrXwkNtz4lx-EADvJavSkCOtYTA1wyDaA-JsZXATzwI9KusXPpj0VIo_8PqJy0J6DsveWYgZPIrlM7HTwD6qsI6en3NIpuLx-fDTUAiXBFUFdZmNfPp5QbnRvzwPqo-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری سی بی اس : آیا در حال حاضر نگران پروازهای دیگری هستید که مقصدشان اسرائیل است؟
نخست‌وزیر ، نتانیاهو: بله، ما نگران هستیم
من با رئیس‌جمهور امارات متحده عربی، شیخ محمد بن زاید، صحبت کردم و ما توافق کردیم که پروازهای شرکت هواپیمایی فلای دوبی را به مدت چند روز متوقف کنیم، تمام شرایط را بررسی کنیم و تعدیلات امنیتی لازم را انجام دهیم
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24627" target="_blank">📅 08:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اکسیوس به نقل از یک مقام آمریکایی:
مارکو روبیو، وزیر خارجه آمریکا، روز دوشنبه پس از به بن‌بست رسیدن مذاکرات ایران و آمریکا، از هیئت ایرانی به ریاست
عباس عراقچی
خواست
فوراً نیویورک را ترک کنند
. به گفته این مقام، مذاکرات که صبح همان روز امیدوارکننده به نظر می‌رسید، تا بعدازظهر به بن‌بست رسید. هیئت ایرانی چند ساعت بعد نیویورک را به مقصد دوحه ترک کرد. ایران می‌گوید خروج هیئت از نیویورک از قبل برنامه‌ریزی شده بود و موضوع به وزارت خارجه آمریکا نیز اطلاع داده شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24626" target="_blank">📅 08:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffd865ee13.mp4?token=VLKb0y6m9mnff3G8VfT_pOd8KYpe4ybRYZllrE03qJoYeYWjU6i10wCyWba8oV91Mg0sIL2G2tYTbcVpqEs2yeG4OwC3UrKDHMZVr6RhKK1j1Zpy5pWJ8-lgTHwn7lr3RxwEFKvQtJLydF3N3KhY5lbaTS5gxt2z2TYQSqMJIphoW5EcIVtCdU-mNd4m22dXw6JQbs9oH6rvotGqAIp_xFn9eSHgU4PIx61ssBIdpH5RzMgYOkFbC4nlBBruoTy7Inz2pvNJ_lj-ItBDyW_iNUwmRZDpKAUmyfzHmNPFgYmkKQQmh10UEcmIf0aprSeVwwbOoSzhbgqDLpZzo3MDeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffd865ee13.mp4?token=VLKb0y6m9mnff3G8VfT_pOd8KYpe4ybRYZllrE03qJoYeYWjU6i10wCyWba8oV91Mg0sIL2G2tYTbcVpqEs2yeG4OwC3UrKDHMZVr6RhKK1j1Zpy5pWJ8-lgTHwn7lr3RxwEFKvQtJLydF3N3KhY5lbaTS5gxt2z2TYQSqMJIphoW5EcIVtCdU-mNd4m22dXw6JQbs9oH6rvotGqAIp_xFn9eSHgU4PIx61ssBIdpH5RzMgYOkFbC4nlBBruoTy7Inz2pvNJ_lj-ItBDyW_iNUwmRZDpKAUmyfzHmNPFgYmkKQQmh10UEcmIf0aprSeVwwbOoSzhbgqDLpZzo3MDeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: الان تنگه هرمز تو دستمونه، عملاً اونو اداره می‌کنیم و کنترل کامل در دست ماست؛ البته می‌دانم که این وضعیت همیشه می‌تواند تغییر کند. کافی است یک مین بندازند؛بنابراین اگر واقعاً مین باشه، شرکتها حاضر نیستند کشتی‌های یک میلیارد دلاری خودشونو از تنگه هرمز عبور بدن. اما دوباره تأکید می‌کنم ، الان نفت بیشتری از تنگه در حال خروج است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24625" target="_blank">📅 01:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: من با بی‌بی نتانیاهو درباره این حادثه صحبت کردم. طبق روایتی که از او و چند نفر دیگر شنیدم، کمک‌خلبان احتمالاً تروریست یا فردی دیوانه بوده که به خلبان چاقو زده است. خلبان با وجود جراحات شدید توانست درِ کابین را باز کند و فریاد بزند. هواپیما با زاویه‌ای بسیار شدید رو به پایین می‌رفت و سکان عقب آن نیز آسیب دید. یک لوله‌کش اسرائیلی که هرگز هواپیما نرانده بود، متوجه ماجرا شد، وارد کابین شد و کمک‌خلبان را با وجود فشار جی از صندلی بیرون پرت کرد و با کمک مسافران او را مهار کرد. سپس این مرد قوی با وجود نداشتن تجربه پرواز، اهرم کنترل را بالا کشید و توانست هواپیما را پیش از سقوط دوباره متعادل کند.وقتی از او پرسیدند چطور این کار را انجام داده، گفت برنامه «سوانح هوایی» (Air Disasters) را تماشا می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24624" target="_blank">📅 01:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9ea45ed0.mp4?token=lnyvoWQ4r9mFhupQo87EGQa99LQDwfpOoKaX0RIdz2s28BPAjYfZ_33OsvN5yI0hW2DjFlIUJ05FNR4ZRGV1w16bF9gtiTxBo5M5L2xNQLc-LY0eoorfxFalzRbRjVdoQb6-K1h3PdXM9u82L2QRkysxAK09cv4Cdj7EW-zP0lt6ZcSlqNk1dFQLwKkwC8jEezT3-AUZlNFKqGybGclFPsj62RUvMXw5dOjm1eN6mg_019TkJSJLwb8U3stG2juHeGABemvq9zTM2uvVmV1VzgB3Od1QKlRgjTcC3QjyT-4aFHgas3uycAYiruUXyN9Cz8EQxyvQgtfT5BzrUaf11w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9ea45ed0.mp4?token=lnyvoWQ4r9mFhupQo87EGQa99LQDwfpOoKaX0RIdz2s28BPAjYfZ_33OsvN5yI0hW2DjFlIUJ05FNR4ZRGV1w16bF9gtiTxBo5M5L2xNQLc-LY0eoorfxFalzRbRjVdoQb6-K1h3PdXM9u82L2QRkysxAK09cv4Cdj7EW-zP0lt6ZcSlqNk1dFQLwKkwC8jEezT3-AUZlNFKqGybGclFPsj62RUvMXw5dOjm1eN6mg_019TkJSJLwb8U3stG2juHeGABemvq9zTM2uvVmV1VzgB3Od1QKlRgjTcC3QjyT-4aFHgas3uycAYiruUXyN9Cz8EQxyvQgtfT5BzrUaf11w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار
:
شما حاکمان ایران را دیوانه توصیف می‌کنید. چطور می‌توان با افراد «دیوانه» به توافق رسید؟
ترامپ:
«شاید آنها را
بمباران کنیم
. باید درباره این موضوع تصمیم بگیریم؛
یا آنها را بمباران می‌کنیم یا به توافق می‌رسیم.
زمان تصمیم‌گیری نزدیک است.
این ماجرا خیلی زود به پایان خواهد رسید.
»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24623" target="_blank">📅 00:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16a58f7f7c.mp4?token=d6xqcVNgQb0WrdHAPk-IJMpoVvwZ4rkVI5QXreZYOASLqS7ocoKTRHvLBiM6ikB5IovACfXU5tWjANGM6eV6-jbLVaUbI8RjOIFbb8QhD-tfebdmObZFSMeyPPKjmK4BOx9uZ96j3sFFdeQgLl7xw4qx8ySzOPYwcl5fq7m20xp5EErpeWWBY5u5VNH8PwbIBA_xx7ozthGQ_8_UrEwfEK2iMC7_FHNajmKmYkSvbdON9nY6x_Z8nM6UqaURto0ngeoEkC81Q0awuNlqksdkSikj-c4nAEhXjgscIhR5RiRQi-Fkz-KevateMsR5BduLeDDJWuH0XAkB0VvVMNA6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16a58f7f7c.mp4?token=d6xqcVNgQb0WrdHAPk-IJMpoVvwZ4rkVI5QXreZYOASLqS7ocoKTRHvLBiM6ikB5IovACfXU5tWjANGM6eV6-jbLVaUbI8RjOIFbb8QhD-tfebdmObZFSMeyPPKjmK4BOx9uZ96j3sFFdeQgLl7xw4qx8ySzOPYwcl5fq7m20xp5EErpeWWBY5u5VNH8PwbIBA_xx7ozthGQ_8_UrEwfEK2iMC7_FHNajmKmYkSvbdON9nY6x_Z8nM6UqaURto0ngeoEkC81Q0awuNlqksdkSikj-c4nAEhXjgscIhR5RiRQi-Fkz-KevateMsR5BduLeDDJWuH0XAkB0VvVMNA6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«
رهبران ایران به‌شدت برای حفظ کنترل در حال مبارزه هستند، اما کنترلِ چه چیزی؟
»
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24622" target="_blank">📅 00:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24621">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76e3f894e7.mp4?token=WyYq0-LyhRcugtdXymgHnQDea_mw5lDugjCfEghPNP7cParNcWK8OeQZpH1a1wkDWC_Jem4yy7OrGMbN-p32QDJXL_zaytvSyV2g21vUDUuWRyjA3sYP2o5PWlxafE2vidPfT1k713JIQs3VQEbSy5B28gBeb2nHtOHh1YpCuf0dRP9dLMsQSG6yIaz-rIAK7r1ETHxM21_NdX---OcASA50AmDCS33aSdXdwTdX49Ht27MNGC6ThH-h5rMOR1ReW-KWrjqsgIBGdWPDyKBDO9Z4qUhJh26KMp9hHZ_qbwy_1mk3eO0kHPWbSRI-EXatiQ0cHPBi2FO267QMpWSYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76e3f894e7.mp4?token=WyYq0-LyhRcugtdXymgHnQDea_mw5lDugjCfEghPNP7cParNcWK8OeQZpH1a1wkDWC_Jem4yy7OrGMbN-p32QDJXL_zaytvSyV2g21vUDUuWRyjA3sYP2o5PWlxafE2vidPfT1k713JIQs3VQEbSy5B28gBeb2nHtOHh1YpCuf0dRP9dLMsQSG6yIaz-rIAK7r1ETHxM21_NdX---OcASA50AmDCS33aSdXdwTdX49Ht27MNGC6ThH-h5rMOR1ReW-KWrjqsgIBGdWPDyKBDO9Z4qUhJh26KMp9hHZ_qbwy_1mk3eO0kHPWbSRI-EXatiQ0cHPBi2FO267QMpWSYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار
:
اندی برنهام گفته است که
ایران در حادثه پایگاه هوایی RAF فرفورد
نقش داشته است.
ترامپ:
«ما در حال حاضر در حال بررسی این موضوع هستیم.
خیلی جدی در حال بررسی آن هستیم.
ایران در حال حاضر
مشکلات زیادی دارد.
»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24621" target="_blank">📅 00:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93e19363c.mp4?token=vCV-glylA0onIc-kgWnZlYhH1pqZdA6-YBW9o1toze1ByOa6KcAdNFrtLuG49M4K8K2EOTVXWVBVjOt8of_DueIKScyupi2SmW5jXhiFuOEAJ_tRl1-NCQZ1RtDst6eXfP7bFsH8ULMwm4Txku2XyCYeqOoKkGphsgjs3QACb26wArwmciAFUou3kgro8gGYtgFoVlV-scbFr4sKfvieIIRnqCcQehf2tLPN9Hur657hq7S8XsX1LAyYjf59mjEz4gd4-oH36-in1-11EJPVgMrq3KHPQYgvZfdhg_vCtigznkmLJZhSLZIj3FfwSEbzrko_-qLvO7NibLdL6Js9tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93e19363c.mp4?token=vCV-glylA0onIc-kgWnZlYhH1pqZdA6-YBW9o1toze1ByOa6KcAdNFrtLuG49M4K8K2EOTVXWVBVjOt8of_DueIKScyupi2SmW5jXhiFuOEAJ_tRl1-NCQZ1RtDst6eXfP7bFsH8ULMwm4Txku2XyCYeqOoKkGphsgjs3QACb26wArwmciAFUou3kgro8gGYtgFoVlV-scbFr4sKfvieIIRnqCcQehf2tLPN9Hur657hq7S8XsX1LAyYjf59mjEz4gd4-oH36-in1-11EJPVgMrq3KHPQYgvZfdhg_vCtigznkmLJZhSLZIj3FfwSEbzrko_-qLvO7NibLdL6Js9tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۸ نفر از نیروهای بسیار خوبمان را در درگیری با ایران از دست دادیم؛ از دست دادن حتی یک نفر هم زیاد است. اگر به عراق نگاه کنید، ۴۵۰۰ نفر را از دست دادیم، اما نتیجه آن حتی نزدیک به چیزی نیست که اینجا به دست آورده‌ایم. ما در عراق برای نابودی داعش وارد شدیم و من در دوره اول ریاست‌جمهوری‌ام این کار را انجام دادم؛ به همین دلیل آنها باید مدت‌ها پیش از آنجا خارج می‌شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24620" target="_blank">📅 00:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c295dc969.mp4?token=L-cNnOCBdTCOSNyW4SX4rAYdzvFGIPohA9hMjb_59lYJfdhbIFl1oj8fv_2DOpxYZVnm1U2wzDQggbA52Q5lmu630LBtUN6_d_ykNnb9PnVETKLzcudtOhAZ3LVh7lbwVcpvEHKELhE3LNhIJiEHxpTwZXiS0uFwk7T6Uft4aoeN5oDhh-zWpPtndyTPmLCrPMDMkDglMw8ThlJSv1A4jlcB1e1cAzSkER3Vvwzm_01yUI8R3GeA4gxDy-lRvxgg-eGtPjCBg40WmK7hFoojMcxqP05jFIId32vnuTZo9fLg_ET4yAhK_hmQTsdI77zFChRYgIzpId3DZS9gwj4NCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c295dc969.mp4?token=L-cNnOCBdTCOSNyW4SX4rAYdzvFGIPohA9hMjb_59lYJfdhbIFl1oj8fv_2DOpxYZVnm1U2wzDQggbA52Q5lmu630LBtUN6_d_ykNnb9PnVETKLzcudtOhAZ3LVh7lbwVcpvEHKELhE3LNhIJiEHxpTwZXiS0uFwk7T6Uft4aoeN5oDhh-zWpPtndyTPmLCrPMDMkDglMw8ThlJSv1A4jlcB1e1cAzSkER3Vvwzm_01yUI8R3GeA4gxDy-lRvxgg-eGtPjCBg40WmK7hFoojMcxqP05jFIId32vnuTZo9fLg_ET4yAhK_hmQTsdI77zFChRYgIzpId3DZS9gwj4NCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست: رسانه‌های ما باعث می‌شوند رسانه دولتی ایران منطقی به نظر برسد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24619" target="_blank">📅 23:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24618">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری i24NEWS: در پی هشدارهای منتشر شده , رئیس ستاد مشترک ارتش اسرائیل ، سفر خود به ایالات متحده را لغو کرد
@WarRpom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24618" target="_blank">📅 23:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وحیدی: اشتراک چت جی‌پی‌تی مقوا رو از پلاس به پرو ارتقا دادیم ، علی ای حال فردا یک پیام خیلی مهم منتشر میکنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24617" target="_blank">📅 22:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ja-Nf9fTcfwdMZ8HmB45AjVejxeKk9pWzUeHLjGTbdV8w7ppVrHVFGXkapgC_XHI_wCTcT01bFGhwo_qIY5M8wGWqTcJY4rdwnnOiIUhOhGyi-yyJNnuVv8eaTBSeaLv9s7LlvS_T_hn2_A1uSASirV2jTbD-4ihX2z1NlkHJJfAL3qB_kzToBaDkDemynbiOO4O7FTKQFiqa1LYO8ESNOWGXWgQiIKubMx_oYkjItFclHIRnSlPB5Z1dWkjVpPczlok_wAnDIDF1RSVAqmtYbJ7cyvDwLVIsNCWiweOAVklTWdAOQjeEVbRpFZSoRsvnfCc9THVC0pwiiJUnenpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : خلبان هندی ، ناجی جان ۱۷۴ اسرائیلی مسافر در پرواز فلای دبی شد!(پیشتر به اشتباه خلبان اماراتی معرفی شده بود) @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24616" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">روایت قهرمان ماجرا به نتانیاهو از لحظه درگیری در کابین: «فشار شدید هواپیما من را به سمت پایین می‌کشید. وقتی به درِ کابین رسیدیم، یک نفر با پیراهن سفید هم آنجا بود که فکر می‌کنم یکی از خلبان‌ها بود. خلبانی که مورد حمله قرار گرفته بود، بسیار نزدیک در افتاده…</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24615" target="_blank">📅 22:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f7a659bf.mp4?token=pA8M30UY3Kr5WfwulU73BevGn1x41DPpGfmRYQ_4Y3XwZvK-NdnKgvVKEwb_wrJFbwtkOPRfEm-zojY_Jxm_bGyg3haMS2ijomrRw5mubtknmCczOslBXQCzZxATvXmA16xkQAKgmcjahE36_uo8cud6Lyc0K4pJMnUs0hAZn0xy0dIX7LyUP3kuZ1ERox4IlZU_kAzC6w_GcLb3pECrwTtWoyeXPLNMxrZ1OpLcY2qk67mbBmKj8PckhH3ahcYaHuFQgIogzCs5D99ylUZbRmfRhWaP-VO-4hMhF4b89igdwDdSluluvAKGPF1Mcq5Gz5ER4m1pNGEzbWJ_x1o-fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f7a659bf.mp4?token=pA8M30UY3Kr5WfwulU73BevGn1x41DPpGfmRYQ_4Y3XwZvK-NdnKgvVKEwb_wrJFbwtkOPRfEm-zojY_Jxm_bGyg3haMS2ijomrRw5mubtknmCczOslBXQCzZxATvXmA16xkQAKgmcjahE36_uo8cud6Lyc0K4pJMnUs0hAZn0xy0dIX7LyUP3kuZ1ERox4IlZU_kAzC6w_GcLb3pECrwTtWoyeXPLNMxrZ1OpLcY2qk67mbBmKj8PckhH3ahcYaHuFQgIogzCs5D99ylUZbRmfRhWaP-VO-4hMhF4b89igdwDdSluluvAKGPF1Mcq5Gz5ER4m1pNGEzbWJ_x1o-fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارک روته، دبیرکل ناتو: اروپا نتوانست توان هسته‌ای ایران را از بین ببرد، اما طی ۱۰ سال آینده توانایی انجام این کار را خواهد داشت و باید خودش این کار را انجام دهد. او گفت اروپا همچنین باید مسئول مقابله با حوثی‌ها در دریای سرخ باشد، نه آمریکا. روته تأکید کرد که اقدام آمریکا برای از بین بردن توان هسته‌ای ایران کاملاً ضروری بود و پیامدهایی خواهد داشت، اما این پیامدها از این واقعیت آغاز می‌شوند که اقدام آمریکا ضروری و مثبت بوده است. او همچنین گفت عجیب است که برای حفاظت از حدود ۶۰۰ میلیون نفر در اروپا در برابر ۱۴۰ میلیون روس، کشورهای اروپایی به آمریکا با ۳۴۰ میلیون نفر جمعیت و فاصله ۶ تا ۸ ساعت پرواز وابسته باشند؛ اروپا باید بتواند در آینده خودش از خود دفاع کند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24614" target="_blank">📅 22:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24613">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c1b577539.mp4?token=gywF7n2S37QQeM449w3zvmSIgOIR_xZ6I03piUeXrFM_d6AUzKuWe9ycOjeRDTM8gACivL-11u3ouCOO0wBo7zAWET_j-eXfE2t7ogczT93e_peltfqWcDUQUHZNskUIXg2uCrGSNz_hN8OOh3XNClMrTe9qvGyw_iOSwBnCrXVDVKtUi3-MIHWdaGXHfuBtZfl__kslcvmGFYmuF4sPUcbe-2I5xbiyrXO9hjzv2m356GX7sbU5YUC0PWig9tbKULimll9q-xT4RYZ4bqr7OlKOdpcZHduVn1zsZC8lsiZOOSaLBl114X9i6IBobCXFV24ZqNUUS3i6I9PPFkDbcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c1b577539.mp4?token=gywF7n2S37QQeM449w3zvmSIgOIR_xZ6I03piUeXrFM_d6AUzKuWe9ycOjeRDTM8gACivL-11u3ouCOO0wBo7zAWET_j-eXfE2t7ogczT93e_peltfqWcDUQUHZNskUIXg2uCrGSNz_hN8OOh3XNClMrTe9qvGyw_iOSwBnCrXVDVKtUi3-MIHWdaGXHfuBtZfl__kslcvmGFYmuF4sPUcbe-2I5xbiyrXO9hjzv2m356GX7sbU5YUC0PWig9tbKULimll9q-xT4RYZ4bqr7OlKOdpcZHduVn1zsZC8lsiZOOSaLBl114X9i6IBobCXFV24ZqNUUS3i6I9PPFkDbcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: من تنها رئیس‌جمهوری هستم که حقوقش را اهدا کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24613" target="_blank">📅 21:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f09c19e00.mp4?token=C0NGmnCXZYu9Z0Vp07Dom5plBVm-2AnuEi5Aq2DghVjZAh4baUnPtSKFq9ZDLCM5kCjgN-YGTvvia_xpb61u-fsfTlEbMagT8i9ZHRK29UYybOwP21ZgxrvAyYeLr6b_5Ws4sQFlQPkWk1ltpsTzUcFiFYmtHXd4gjmkiYAdCMq8iRxkJ_O6-FPgqG6I1FRn0RkZk1xBkjHHL6mLEclcC2FwMcav1A512_hrwVzDaJWTdbyZQunZEQfDGMsiruXiOv4BeeQPso75j1aLbGNbdB8q7lG801Q5YnTIir21OvrltotdtQOuYXZxo1i9B08Hj_vxk-OKjnepKhnRpUdP8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f09c19e00.mp4?token=C0NGmnCXZYu9Z0Vp07Dom5plBVm-2AnuEi5Aq2DghVjZAh4baUnPtSKFq9ZDLCM5kCjgN-YGTvvia_xpb61u-fsfTlEbMagT8i9ZHRK29UYybOwP21ZgxrvAyYeLr6b_5Ws4sQFlQPkWk1ltpsTzUcFiFYmtHXd4gjmkiYAdCMq8iRxkJ_O6-FPgqG6I1FRn0RkZk1xBkjHHL6mLEclcC2FwMcav1A512_hrwVzDaJWTdbyZQunZEQfDGMsiruXiOv4BeeQPso75j1aLbGNbdB8q7lG801Q5YnTIir21OvrltotdtQOuYXZxo1i9B08Hj_vxk-OKjnepKhnRpUdP8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما نیروی هوایی آنها را از بین بردیم ، در سه روز گذشته، حجم نفت عبوری از تنگه هرمز بیش از هر زمان دیگری در تاریخ این تنگه بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24612" target="_blank">📅 21:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa854dc852.mp4?token=MI_j_PjweuImLIcNwVubEYVty2M_VaEwScU5JsnUdp7apNJQqDZC3SNSe7wXDF95pqBmD23g3jHNujP1fhJq1hAmE6aRVBuyeTxEvcN0CG3_YdD-IM_rC5SK0py4vJKBLfVP7c21Eghby8d5UXMiqT-kgzwaVCkjulqnvSltIaxPgoGmTd-B2-t4WjjHJb0LQRH-fMGinsSqX1cZxeV6DrJNblAJLI5QgEhKLLR-IN8ijbizzKoYmh-H00TUiX_bIj7o25kvnSxRgkqVN_Jbnoye_-oPFAtyTI7lDzjLn1xYy-tAF4Tm6mgaio3wfgy32cdFVXFNxP0aNE4EwcQHVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa854dc852.mp4?token=MI_j_PjweuImLIcNwVubEYVty2M_VaEwScU5JsnUdp7apNJQqDZC3SNSe7wXDF95pqBmD23g3jHNujP1fhJq1hAmE6aRVBuyeTxEvcN0CG3_YdD-IM_rC5SK0py4vJKBLfVP7c21Eghby8d5UXMiqT-kgzwaVCkjulqnvSltIaxPgoGmTd-B2-t4WjjHJb0LQRH-fMGinsSqX1cZxeV6DrJNblAJLI5QgEhKLLR-IN8ijbizzKoYmh-H00TUiX_bIj7o25kvnSxRgkqVN_Jbnoye_-oPFAtyTI7lDzjLn1xYy-tAF4Tm6mgaio3wfgy32cdFVXFNxP0aNE4EwcQHVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران : ما کلا از نظر نظامی پیروز شدم ، در ۶ ماه ۱۸ نفر را از دست دادیم، اما آن‌ها ۴۵۰۰ نفر را از دست دادند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24611" target="_blank">📅 21:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d8d88008.mp4?token=SlMe2Qpx2vuQBTAqccfCGNElKr1yTbQTzlv-bpJ4OkykMA63CSlFDwoHMei37Hx8Wilydig2wljrqt97wD_zYrYDJjEM6O_zkQRy9xzFDHNbtVhrk1Su78O_X9YA5voBZirA5VHtjAmiB_VO8_cwIvFYXsjHs1u7DWFWEAMdd3Sx5qN6oDuepTkY-pqex1YjQ2n-S-DKU6sNEAsl10flXj0IE_4cntT9ZHs__8qHntk6P7A41fnPO-TtaFx8DYMsrHtLuKBJUmk5Cpt9uZM585-hu6eR-Lc7Mf-WD2xPvPLB1kvb7S74d3BiQvhcjm1yIAIIcCiyo_p0D_3ToHNufw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d8d88008.mp4?token=SlMe2Qpx2vuQBTAqccfCGNElKr1yTbQTzlv-bpJ4OkykMA63CSlFDwoHMei37Hx8Wilydig2wljrqt97wD_zYrYDJjEM6O_zkQRy9xzFDHNbtVhrk1Su78O_X9YA5voBZirA5VHtjAmiB_VO8_cwIvFYXsjHs1u7DWFWEAMdd3Sx5qN6oDuepTkY-pqex1YjQ2n-S-DKU6sNEAsl10flXj0IE_4cntT9ZHs__8qHntk6P7A41fnPO-TtaFx8DYMsrHtLuKBJUmk5Cpt9uZM585-hu6eR-Lc7Mf-WD2xPvPLB1kvb7S74d3BiQvhcjm1yIAIIcCiyo_p0D_3ToHNufw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما تقریباً کنترل کامل تنگه هرمز را در اختیار داریم میگم تقریبأ چون یکم مین پرت کردن.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24610" target="_blank">📅 21:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6830cdeb6.mp4?token=Zsl_ltBALF4OUH8auSGSmPo5RPcYNMQQz6Kx2E5TAJjDXe04U1yjFGmIILmgPT-z0L8yCzNuEnlvrPquQ8GTn2mpPjmWOQ-UE5b7Z-rMGqj7mfZ7ZXycUG3X-IUP4_-JlCyMKdW3y7BooLcvC3bq2dlDAsGsx9fnWkHZe3nDUv8YKWAXKkBCDLJUCfFy_NE3wcoJHg98R7kX0_H0OR4mYtHXsDYGYGmEQHxKPpnKn-V5FKCjoaw3ttCXOzZvnGnDI6uF94iRXBMfRihcNWVzIb5Tc7IR6Qm69MOGxMXKW_gJ-8-tkAibJOn2bo8xRU8sDqk5VFSk3LVK0Z6-VqfwHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6830cdeb6.mp4?token=Zsl_ltBALF4OUH8auSGSmPo5RPcYNMQQz6Kx2E5TAJjDXe04U1yjFGmIILmgPT-z0L8yCzNuEnlvrPquQ8GTn2mpPjmWOQ-UE5b7Z-rMGqj7mfZ7ZXycUG3X-IUP4_-JlCyMKdW3y7BooLcvC3bq2dlDAsGsx9fnWkHZe3nDUv8YKWAXKkBCDLJUCfFy_NE3wcoJHg98R7kX0_H0OR4mYtHXsDYGYGmEQHxKPpnKn-V5FKCjoaw3ttCXOzZvnGnDI6uF94iRXBMfRihcNWVzIb5Tc7IR6Qm69MOGxMXKW_gJ-8-tkAibJOn2bo8xRU8sDqk5VFSk3LVK0Z6-VqfwHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:خیلی زود شاهد وقوع اتفاقاتی خواهید بود.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24609" target="_blank">📅 21:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24608" target="_blank">📅 21:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24607">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de03a67f35.mp4?token=dAfV-zDkz2obiETE94hHv9qcDvi3Du4eEoQmU03HBxMzqU84VONW4DxSNXFDLAVrSETSFWHuKEp048XCf4h2D0txZjUegWT9Db_XnDq_INC2fri4QrtF2qd0BSicnPhM1NbRFarbs8UHpqPMO640NtM-BK9Ms_QG0drmicVOD1t04bPTfDIl4aCorCNlsrx596sCVi1bMU1V3Czs5UU5SG_ItWpSwny5oWRWtAv05OirnYqQM2f2-dNeK3t80izD04dMHNjb3iNDZhqzCJQcb7CRnei7bRckW885N2AGHqfujweC2wEnKWC1NqlfVIQT4wOOlTPNgZ237lUxtKM1OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de03a67f35.mp4?token=dAfV-zDkz2obiETE94hHv9qcDvi3Du4eEoQmU03HBxMzqU84VONW4DxSNXFDLAVrSETSFWHuKEp048XCf4h2D0txZjUegWT9Db_XnDq_INC2fri4QrtF2qd0BSicnPhM1NbRFarbs8UHpqPMO640NtM-BK9Ms_QG0drmicVOD1t04bPTfDIl4aCorCNlsrx596sCVi1bMU1V3Czs5UU5SG_ItWpSwny5oWRWtAv05OirnYqQM2f2-dNeK3t80izD04dMHNjb3iNDZhqzCJQcb7CRnei7bRckW885N2AGHqfujweC2wEnKWC1NqlfVIQT4wOOlTPNgZ237lUxtKM1OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره عراق: داریم با کله از اون جهنم بیرون می‌آییم.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24607" target="_blank">📅 21:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با قهرمانان اسرائیلی پرواز FZ1073 شرکت «فلای‌دبی» دیدار کرد؛ پروازی که صبح امروز توسط یکی از خلبانان تا آستانه ربوده شدن پیش رفت، اما با مداخله خدمه و مسافران اسرائیلی، از این اقدام جلوگیری شد. @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24606" target="_blank">📅 21:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6e044a2b.mp4?token=Y27ihA5tSMocfeo2Ptw0S2KWwBTL-76zj81UOSY5eZo4ck9bvnYNmHFq0VW6TUw3OndMGm06YrR1SoJIwl7Ov1ddmuthu2wmI0f3ZLoqP-uCM52GkMDOCpMPmyi0eVSSBEhJVS-Y2lI1BisF_xCmppP76FQA9On4VWWqjUevZYXUam8AbxlSlFY1fjQG8lvvyBwsX1mdL5f3shRjtKx8KANTTWH8Ed2GOG7qJSNcyicC1qD-Saf1el52Tk_7h3Snb60ZNjxpFC76DHZGExfvfqANUkE-Q5ANTxLLntq5kcN0hwOlSRHM5ecBCdU8Of1-DHTznCynO2na65pXOtBLqk_G9jqg8Y_Na9idrPbu_tCn1s-rKztps5GNpnOfwCl2S7nguqZgv5MDbp59bNoytSwcnmXtweTL1pjoPaRbxmmJKoW6lFEHIUzzK6zL12W6SPLv58lALq_ikcdTepjIOzzERVX3eli1lfYrnFggNDzwlMNanF4bQNDJBSgQEEMH3fOhREvdhaAakH9Cpp-YaaDi5vMvGnhMFKc0Lubv5y5QaVvdS0JOay7tdTJ0nvNR49cLXQHTCGoWbkNTqhIICy0Hj1HiHdgPYdDtQ_2b4DYtYJLyqOhDwSlsFvvyDd6a-gmza8qBXE6n9T9l5XVcnajIry5Phi_lfqp1CjAlDTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6e044a2b.mp4?token=Y27ihA5tSMocfeo2Ptw0S2KWwBTL-76zj81UOSY5eZo4ck9bvnYNmHFq0VW6TUw3OndMGm06YrR1SoJIwl7Ov1ddmuthu2wmI0f3ZLoqP-uCM52GkMDOCpMPmyi0eVSSBEhJVS-Y2lI1BisF_xCmppP76FQA9On4VWWqjUevZYXUam8AbxlSlFY1fjQG8lvvyBwsX1mdL5f3shRjtKx8KANTTWH8Ed2GOG7qJSNcyicC1qD-Saf1el52Tk_7h3Snb60ZNjxpFC76DHZGExfvfqANUkE-Q5ANTxLLntq5kcN0hwOlSRHM5ecBCdU8Of1-DHTznCynO2na65pXOtBLqk_G9jqg8Y_Na9idrPbu_tCn1s-rKztps5GNpnOfwCl2S7nguqZgv5MDbp59bNoytSwcnmXtweTL1pjoPaRbxmmJKoW6lFEHIUzzK6zL12W6SPLv58lALq_ikcdTepjIOzzERVX3eli1lfYrnFggNDzwlMNanF4bQNDJBSgQEEMH3fOhREvdhaAakH9Cpp-YaaDi5vMvGnhMFKc0Lubv5y5QaVvdS0JOay7tdTJ0nvNR49cLXQHTCGoWbkNTqhIICy0Hj1HiHdgPYdDtQ_2b4DYtYJLyqOhDwSlsFvvyDd6a-gmza8qBXE6n9T9l5XVcnajIry5Phi_lfqp1CjAlDTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۵ اسرائیل : فشار جدی اسرائیل بر عربستان سعودی برای تحقیق درباره فرد تروریست در حادثه پرواز فلای‌دبی؛ به گفته رسانه‌های اسرائیلی، عربستان تاکنون اجازه دسترسی اسرائیل به تحقیقات را نداده و در اسرائیل احتمال ارتباط این فرد با ایران و سازمان‌های تروریستی در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24605" target="_blank">📅 20:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ :
چرا شبکه فاکس‌نیوز همیشه چاک شومر، حکیم جفریز، جسیکا تارلوف و تمام دموکرات‌ها را روی آنتن می‌آورد تا علیه حزب جمهوری‌خواه و البته علیه من صحبت کنند؟ به نظرم حتی زمان بیشتری از جمهوری‌خواهان طرفدار ما در اختیار آنها قرار می‌گیرد. به همین دلیل است که MAGA و میهن‌پرستان واقعی هرگز فاکس را دوست نخواهند داشت! آنها دائماً یک روایت کاملاً منفی را تکرار می‌کنند و بعد در نهایت یک پاسخ کوتاه به ما می‌دهند. واقعاً شگفت‌انگیز است که من هر سه انتخابات را پیروز شدم. مخالفان بسیار قدرتمند و گسترده‌اند، اما مبارزه ادامه دارد!
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24604" target="_blank">📅 20:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با قهرمانان اسرائیلی پرواز FZ1073 شرکت «فلای‌دبی» دیدار کرد؛ پروازی که صبح امروز توسط یکی از خلبانان تا آستانه ربوده شدن پیش رفت، اما با مداخله خدمه و مسافران اسرائیلی، از این اقدام جلوگیری شد. @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24603" target="_blank">📅 20:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با قهرمانان اسرائیلی پرواز FZ1073 شرکت «فلای‌دبی» دیدار کرد؛ پروازی که صبح امروز توسط یکی از خلبانان تا آستانه ربوده شدن پیش رفت، اما با مداخله خدمه و مسافران اسرائیلی، از این اقدام جلوگیری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24602" target="_blank">📅 20:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df0e976c18.mp4?token=cMOqhQLQKA5-iA-Q-MuVly7SmxX8gbYCwKDh-SGKj8ul3AVh1f33jEdn0_efE2QdsU-wASpPNXM6f7pESCdcSUjyi2uIBLA34iMXdjMMGOafmep4WOPDf-Q6CKZwdyu6lpMi7NDC-o953gAQql6hmrAvfs24P21T7lAES77DxB2wmVoneLdfQeZ__sz6CX7sJnb_DnJugB0D67ZyoGx1mBybDqzg5T-LkS-FWZEOBjKPVmWUj8HtA9LRAbnlypLxJSp8h3ALEwOZR8WbMbltrJ9GI1Jzb1Aujfc0K8cn2V00rzTPcceHuLdVmW6WowhAa4R2hUr2w7HXmjUWgDZomRZD8sRNSpNVEAp4Yc130YcUz9Z4wFfkG8MhlaX0gouT_ZvCra0RbPRpOu6lyjY4gN6bEbY9DnIl1cl4M6HLwDo3aj4NvnnbPAXIw5ml5tXfuQCXGZRKLFo7cuUukuSQCVWcvbfbmjx4lXUAkrliICSw5ACjNDFdR5VBJu4UJhZOgWmW5FYZcUogdOnBnO-PwjTdbQ49M7DXaljZy1KdTeE0lL3bYEq63ejiJzPJJ8A-EH3Or9zYopnWRqY2Trmzs4LABhWznCUi7qmghnwOhcES1v_ZhwE8l3jMKDLduII8ubq7Y84pgr6qmUpQzxejXcDR3SXwkfHSw9X4GaR-1u4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df0e976c18.mp4?token=cMOqhQLQKA5-iA-Q-MuVly7SmxX8gbYCwKDh-SGKj8ul3AVh1f33jEdn0_efE2QdsU-wASpPNXM6f7pESCdcSUjyi2uIBLA34iMXdjMMGOafmep4WOPDf-Q6CKZwdyu6lpMi7NDC-o953gAQql6hmrAvfs24P21T7lAES77DxB2wmVoneLdfQeZ__sz6CX7sJnb_DnJugB0D67ZyoGx1mBybDqzg5T-LkS-FWZEOBjKPVmWUj8HtA9LRAbnlypLxJSp8h3ALEwOZR8WbMbltrJ9GI1Jzb1Aujfc0K8cn2V00rzTPcceHuLdVmW6WowhAa4R2hUr2w7HXmjUWgDZomRZD8sRNSpNVEAp4Yc130YcUz9Z4wFfkG8MhlaX0gouT_ZvCra0RbPRpOu6lyjY4gN6bEbY9DnIl1cl4M6HLwDo3aj4NvnnbPAXIw5ml5tXfuQCXGZRKLFo7cuUukuSQCVWcvbfbmjx4lXUAkrliICSw5ACjNDFdR5VBJu4UJhZOgWmW5FYZcUogdOnBnO-PwjTdbQ49M7DXaljZy1KdTeE0lL3bYEq63ejiJzPJJ8A-EH3Or9zYopnWRqY2Trmzs4LABhWznCUi7qmghnwOhcES1v_ZhwE8l3jMKDLduII8ubq7Y84pgr6qmUpQzxejXcDR3SXwkfHSw9X4GaR-1u4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاردین: اندی برنهام، نخست‌وزیر بریتانیا، می‌گوید «شواهد قوی» وجود دارد که نشان می‌دهد ایران در توطئه تروریستی احتمالی در نزدیکی پایگاه نیروی هوایی سلطنتی «فِیرفورد» (RAF Fairford) جایی که پنج مرد در جریان تعطیلات آخر هفته دستگیر شدند نقش داشته است. برنهام…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24601" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو طی چند ساعت آینده با ترامپ تلفنی صحبت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24600" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گاردین: اندی برنهام، نخست‌وزیر بریتانیا، می‌گوید
«شواهد قوی» وجود دارد که نشان می‌دهد ایران در توطئه تروریستی احتمالی در نزدیکی پایگاه نیروی هوایی سلطنتی «فِیرفورد» (RAF Fairford) جایی که پنج مرد در جریان تعطیلات آخر هفته دستگیر شدند نقش داشته
است.
برنهام گفت: «شواهد قوی حاکی از آن است که ایران در وقایع آخر هفته در پایگاه فِیرفورد نقش داشته است، اما البته این پرونده همچنان موضوعی در دست بررسی، پیچیده و جدی برای پلیس است.»
وی افزود که مقامات بریتانیایی همکاری نزدیکی با ایالات متحده دارند و جزئیات بیشتر در زمان مقتضی منتشر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24598" target="_blank">📅 19:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یا موسی
🙌🏾</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24597" target="_blank">📅 19:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24596">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24596" target="_blank">📅 19:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc2d60a6a.mp4?token=L52XKD_5r0VahJ_Za-9kWAw5AoR2fu80i1cZ0hYfMcxozfmKWtCiAs_6dUNpyZePuaOTELw4ZRy1JE1UgSYGmZ4ceW-ZaUzALqxzGAN75XkNoflDq8ePC5zJd9m0mKby2FFsg69XbMXfmQIp7Adi8hNbzoTSOL32Rcu175hR18p0rGh6mCPFRNTGRDT4UfM82ZWk-e8_SKqtb_80pSVoH6BGLl1Jr9VDAOolSEnBPvx_BVQg1iiJ-dc1DPP_KS-Pe0A0dzqazrjVJnQrm_uSmSdeQdvdQrlg8-Rhp8yplqH76bo-SVcnN87v5aoyp1QE4GeImZFJ9dYhMLbjPq6kEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc2d60a6a.mp4?token=L52XKD_5r0VahJ_Za-9kWAw5AoR2fu80i1cZ0hYfMcxozfmKWtCiAs_6dUNpyZePuaOTELw4ZRy1JE1UgSYGmZ4ceW-ZaUzALqxzGAN75XkNoflDq8ePC5zJd9m0mKby2FFsg69XbMXfmQIp7Adi8hNbzoTSOL32Rcu175hR18p0rGh6mCPFRNTGRDT4UfM82ZWk-e8_SKqtb_80pSVoH6BGLl1Jr9VDAOolSEnBPvx_BVQg1iiJ-dc1DPP_KS-Pe0A0dzqazrjVJnQrm_uSmSdeQdvdQrlg8-Rhp8yplqH76bo-SVcnN87v5aoyp1QE4GeImZFJ9dYhMLbjPq6kEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ششصد نیروی نظامی ایالات متحده به پیت هگست، وزیر جنگ، برای «تمرینات بدنی در پنتاگون» پیوستند؛ این برنامه پیش از سخنرانی «وضعیت نیروها» توسط او در کوانتیکو در اواخر امروز برگزار شد. انتظار می‌رود این سخنرانی شامل یک تغییر عمده در ساختار پنتاگون باشد و هگست قصد دارد ۲۰ درصد از سمت‌های اختصاص‌یافته به ژنرال‌ها و دریاسالارها را کاهش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24595" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0894765b2.mp4?token=H3M6rBuMKBu1M6zTdfgbnShcz1yw1glDVc48Y2pBaEZAfhzC72Uk4aJAA4y6MvOc3aIt_ZxK2-e1Yj5fwdk1Zj9egbOgvM_HvwUh1QDTTfpK7m8VPAu0JsQ7K8hQsAYxq68FPbZ4T4YDrFGOYmUcb5rP_whN798VJohBg-X61rmN5KBSEofErdHQaq0aUKHPYG_h_wWQUPXxrrplyracRDmCHHjh-z1hghN9enYVyYx_juCumavou_MrCh35rHWcQHtfm6O-QBHB-sq2kLZsZ_H7An7azH-WqHSSCROK3ic5c-oGq-QgdvzQBynu3MQf8kBbCHV2a9SRxAjA3ugSgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0894765b2.mp4?token=H3M6rBuMKBu1M6zTdfgbnShcz1yw1glDVc48Y2pBaEZAfhzC72Uk4aJAA4y6MvOc3aIt_ZxK2-e1Yj5fwdk1Zj9egbOgvM_HvwUh1QDTTfpK7m8VPAu0JsQ7K8hQsAYxq68FPbZ4T4YDrFGOYmUcb5rP_whN798VJohBg-X61rmN5KBSEofErdHQaq0aUKHPYG_h_wWQUPXxrrplyracRDmCHHjh-z1hghN9enYVyYx_juCumavou_MrCh35rHWcQHtfm6O-QBHB-sq2kLZsZ_H7An7azH-WqHSSCROK3ic5c-oGq-QgdvzQBynu3MQf8kBbCHV2a9SRxAjA3ugSgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اسکورت هواپیما فلای دوبی در حریم هوایی اسرائیل با دو جنگنده @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24594" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFsJ1vXvOWKv7EgiJjBbWUURUNY_kX3zmtdL1I0bNIZXu1kmLX7-8Un8LmV1EwvlyNwM1AKtQaIMT_DBJ5Rmce_HusEQuxgjHDlGGdNlHaiZW_tP5SnEc7skHe_RDOYtglbW9Ftp8ZzuklC_lJ-1ya-TVFcL0VxFs3YUNHlsSeU0nMu4mVEnooxRrMBtxZPRKzYBbaDgciFFFYOHJGqg2J_RqvM7_WWxPcf7bcAXU7LfbB2Oeo2oz2J1MAhdEC9m_KMexeuOjo2YINZsKKfQ60Rnwt9Dqo0amDHux9jgdhrY_bHCPJKp_QIAvAZRmm4lLEuO4hNHPfDPhqdMF0x2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز دوم «فلای دوبی» مسافرها رو از عربستان به اسرائیل باز گرداند @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24593" target="_blank">📅 19:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آسوشیتدپرس:
پاکستان اعلام کرده در صورت حمله حوثی‌ها به عربستان، برای دفاع از عربستان از
«هر وسیله‌ای که در اختیار دارد»
استفاده خواهد کرد. وزیر دفاع پاکستان این موضع را در چارچوب توافق دفاعی مشترک جدید میان
پاکستان، عربستان و ترکیه
اعلام کرده است. او در عین حال گفت پاکستان همچنان کانال‌های دیپلماتیک خود با ایران را حفظ می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24592" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-G3JKaFU0b_X0qfRRDJICjXdDpyFHA1fFCRH8TALO6f-eCKwqbE_nsi13-hmLdUVtPs4zv--TjD441PS3_GkGYfR3qExX5SWBBVjlB8uHVYS-KfDMuHGQ_saydL3DlqsGSxIRR4dzfop_Z-LtoW_6jIX_AqE7EhGlxvY4p2OPNiUn2DFyNDVwaJLPk4R4or7Ip7RxW1tSX-HNRNpHmLonAe40BGqMgxQMh9kxykYLs20j-uLOw-ZnCC2joKdwHJKzvJkPNk75XNhQLVTUsR_TGOjXXIZ95unawQCF1I_Xb1-lh-zfcF4XKOqQ6sYXqhaNTgvHxrck5U4aIRZGdJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOwMUyACPcsEtQJ1vguP9BwZk8lsTgCQkpnX5tVlsDRHFzM-jPFFPYZSpKtC-yfb-J8uXq_VgVkc2_ZoWYYgCW6nnyUFPLjb_Ld8-bW0WD8BplTcipHgo-lAPmX91BFpPAgubprpkV6pxmQ9gIFkCQ_AdI1meu-56lNvcGnclUVvrxCI-w-3hHnHWcmdJCbxiki3OMxFwMZC6nU5f2SCRB_gPyDpjQ49HZPgZNWcqsL9vZ8EOPF-RF9Ssx_uPbZ3Ei_7bK51A0MDhQBkH_zxPFjm8izOnFL4z_y_zYTQ9LRTNcBIKxJ490FlpXJeCvW_gp46XmIwAwvdGzChl-jKWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : با دقت بیشتر مشخصه این خط جت است
و موشک نیست
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24590" target="_blank">📅 18:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuttPxAXuH9uoRmF_YpgJ3R8ensTJLXOWXvyxTeuY5ENdbnWoiXoS5eQPHKR8bPEJtE8JPkdlUPoYaf7paK4Zm8ThQ_mpdArDnEY0s6Y8vq3T1zaeMcQdz_28vQcSbvLAaSwf6CMF0suLjFsRytZ5Npm_j8920SeIq8MK5Bucwzs6XlII4Teb7LJHf7t_-g0-eGZZr8IKGXKmVuP2qTd8zhnIuA9eQfZ4bbZpd6BBsU9aizmytV5Vzk7Ko6vqNAmgivneznPlpycGMsBycgTrqvM-V8VRbv1jI4QMHqVwGsR-AQ2bDHXbeeUoH4xFgiBridhZJ8LEySbpdlmLkhXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز دوم «فلای دوبی» مسافرها رو از عربستان به اسرائیل باز گرداند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24589" target="_blank">📅 18:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82776f51d.mp4?token=NB5lnJd8XuVukpf6tjYprehudKEwBI6HRjoUQp71oGfCziDGzqgnJ0mlfo0NIqkh28GdSP5IK2nuXgWo5ppMoIeFzTj9w7AVIC23FeNeX_iStb67Jj5ajF8iJkcySMPxKbLx28ejF14F92_6tTOLmwMTSqMWsmxLPr3NqbM4-_w8K79aQdvI4HpK0-Lf0-WImQNLysZ2ISSHuqx2_de9CQ5LEqIc6UucpWyN5vOxQpbtWsZMoZz5GlyovqmLsTdxVa4UEve49B2Dg5Ho5CLKPfk0peMQdvP6bUW4W2-qtxaveKsoAHtQAG94VYbCaFxFQU-KXewV4Y6LWAUEDK6dSTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82776f51d.mp4?token=NB5lnJd8XuVukpf6tjYprehudKEwBI6HRjoUQp71oGfCziDGzqgnJ0mlfo0NIqkh28GdSP5IK2nuXgWo5ppMoIeFzTj9w7AVIC23FeNeX_iStb67Jj5ajF8iJkcySMPxKbLx28ejF14F92_6tTOLmwMTSqMWsmxLPr3NqbM4-_w8K79aQdvI4HpK0-Lf0-WImQNLysZ2ISSHuqx2_de9CQ5LEqIc6UucpWyN5vOxQpbtWsZMoZz5GlyovqmLsTdxVa4UEve49B2Dg5Ho5CLKPfk0peMQdvP6bUW4W2-qtxaveKsoAHtQAG94VYbCaFxFQU-KXewV4Y6LWAUEDK6dSTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در تروث
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24586" target="_blank">📅 18:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتاق جنگ با یاشار : توصیف دقیق و خط به خط درگیری در‌تنگه هرمز و نحوه پایان یافتن
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24585" target="_blank">📅 18:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا تنها</strong></div>
<div class="tg-text">داداش .
جای چرت پرت های این الاغچیان
یک قسمت از تام جری بزار شاد بشیم</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24584" target="_blank">📅 18:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عراقچی: ایران در شرایط جدید، به موقعیت ممتازی دست یافته
کشورهای اروپایی، عربی و آسیایی اشتیاق شدیدی برای دیدار و ملاقات در نیویورک نشان دادند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24583" target="_blank">📅 18:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24582">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOuPCLBWZFfwsPYNyjsy8pCLnZQxbcrjf_Eh61TPjtAD-iyInLK5dwmy-wdvMOLkxEKH9l6zHg1J-6QzXY85ZiM5VgYbdrw1HSzMImFpOeXZGLaUvQn8xeP131eJwu0-Kt6eXOxjf4ufgEJ4yW7Axshr_HVDfpj0EYG7CH5vaIzLWkd5dgypWbPbDYUvV7qK5vMBnNGBuDSz1XgxI9pgTF1hZ5AKViu7vzTWGOVpTQqQRxSTWlcPyVVNYPXf-OVI6ogu0tcfS_F3JvlZ7kuyq6O4jJHCQlJs7PjooeSWJbzI4gggZnIR9qYxwDx9kCe3NObqAH4SY-yqbbQhaAbUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابک زنجانی عکسی از
«
محمود زیبایی
»
گذاشته که طی دستگیریش به عنوان کارشناس بانک مرکزی حضور داشته و ازش بازجویی میکرده، اکنون
زنجانی ادعا میکنه که این فرد عامل موساد بوده و روش‌هایی دور زدن تحریم رو یادگرفته
با خودش برده.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24582" target="_blank">📅 17:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24581">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو:
«این یک
رویداد امنیتی بسیار جدی
بود. در پرواز فلای‌دبی از دبی به تل‌آویو، یکی از خلبانان با چاقو به خلبان دیگر حمله کرد و ظاهراً تلاش کرد هواپیما را با تمام سرنشینان سرنگون کند. هواپیما وارد حالت چرخش شد و شروع به شیرجه رفتن کرد، اما یک مسافر اسرائیلی و یکی از اعضای خدمه وارد کابین خلبان شدند و مهاجم را هنگام تلاش برای دستکاری سامانه‌های هواپیما مهار کردند. اعضای دیگر خدمه نیز وارد کابین شدند و به تثبیت هواپیما کمک کردند. آنها قهرمان هستند؛ با ابتکار عمل و شجاعتی فوق‌العاده، جان بسیاری را نجات دادند و از وقوع یک فاجعه بزرگ جلوگیری کردند.»
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24581" target="_blank">📅 17:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مردی اتاق جنگ همه جا هست ! @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24580" target="_blank">📅 16:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">استاد بزرگ شطرنج ، نتانیاهو : توان هک هر تلفنی رو داریم
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24578" target="_blank">📅 16:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لغو سفر نتانیاهو و کاتس به غزه در پی فرود اضطراری پرواز «فلای‌دبی»
بنا بر گزارش‌ها، سفر برنامه‌ ریزی‌ شده نخست‌وزیر، وزیر جنگ و رئیس ستاد ارتش اسرائیل به نوار غزه، در پی فرود اضطراری هواپیمای فلای‌دبی و احتمال امنیتی بودن آن لغو شده است
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24577" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24576">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61a612b92.mp4?token=rN6j60b-ML3SJPNM8ARUugzblilFAVgFRjpHbO3lG-I0aYKHjfbhdc1xiOvkOr6juV4ulXBFuijE6RTyGV7rDxj_8dls2dHzCtg65vYXhspXyyvWfJ1dlaMZChDIP9FnoKoTWP8SaBFlGIm3FzLjc5HZSHakQGOEDm9FtOTPlhu0rx1ANDXn-3-vih9F76CtTVKDe54CoIDNhxJGhEY03qu0dWUW5aUneztgw50jAINbtq6L9RBztwkeTMxOtfdcKYOlcZmINnsFvH_zGiXIDm1L4Z6rmNlO16X-217cNO1y72QnL0GHAYV62nkYgpo6i-37bl7jIXw11EC9c6HyKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61a612b92.mp4?token=rN6j60b-ML3SJPNM8ARUugzblilFAVgFRjpHbO3lG-I0aYKHjfbhdc1xiOvkOr6juV4ulXBFuijE6RTyGV7rDxj_8dls2dHzCtg65vYXhspXyyvWfJ1dlaMZChDIP9FnoKoTWP8SaBFlGIm3FzLjc5HZSHakQGOEDm9FtOTPlhu0rx1ANDXn-3-vih9F76CtTVKDe54CoIDNhxJGhEY03qu0dWUW5aUneztgw50jAINbtq6L9RBztwkeTMxOtfdcKYOlcZmINnsFvH_zGiXIDm1L4Z6rmNlO16X-217cNO1y72QnL0GHAYV62nkYgpo6i-37bl7jIXw11EC9c6HyKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل:
جمهوری اسلامی نزدیک به
۴۷ سال و نیم
است که حرف‌هایی می‌زند که هرگز قصد عملی کردن آن‌ها را ندارد. اما تنها چیزی که واقعاً قصد انجامش را دارد،
نابودی آمریکا و به ارمغان آوردن مرگ برای آمریکایی‌هاست.
یکی از دلایلی که بسیار سپاسگزارم این است که ترامپ سرانجام شجاعت به خرج داد و گفت: «کافی است؛ آن‌ها به سلاح هسته‌ای دست پیدا نخواهند کرد.» اگر بعد از نزدیک به ۵۰ سال که به شما می‌گویند قصد کشتنتان را دارند، هنوز حرفشان را باور نکردید،
شرم بر شما باد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24576" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کودن هم بسیار هست..</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24575" target="_blank">📅 16:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH H</strong></div>
<div class="tg-text">مصاحبه زن این یارو رو دیدی که باهاش عکس گذاشتی؟</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24574" target="_blank">📅 16:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24573" target="_blank">📅 16:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24570">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mvfi9HXZiYBfGOx0VybXowoZ8my6mUdHH5Tr90Ym4FfELuX2lPBchhDThw0QWY91hvI06eRKH6h5fUbIrZHpG7OhKQyxZpeNTthob5rnQh6kAwm1gK90yV5CqsjKNqx_BF0qPlMRYdySpgKEUAgpQjM08cCr6sUc4z16w7V4oVTMkjQPupmkuDnmLWdMc15GItLwLJ5xYW_GFze64omKfURYdxCHd-oKIirZ-SnZUpMh6S-XnEapUYdOzbFkn5x7Ta31YOHgcRwwiwgK-SFiIu_i_Mh9brhuvxjWqIqvo84FICTWBfAyW0-Fw6Adkzdv85qT3kNezm1OW_ppMk6EBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af7c379d02.mp4?token=mmmke8cEbzIyG4DTUPHuzbjkAVO3LEHo05u9fC6RjOXj7DpYftkQLzzR8aDFRq0U6ecMglovjDEELb07Nks195UYwRV0Y-UrE637OK7XDatZxEHvAR3Xh4pzZWma4Xnrh8dNzpJSJn3CG_mf10pZn0NzpZVNuN58iJGWSxcbb3miPPOuo0R4o3T05iS7Sqa282YKdIINQLmvHbGHiHYBLfw8LuN-r_fI-m8sCklAst5itwouZaCutwWWphqWhOmdz7dKfagQX-Jv3tXjG15i_bo16OHEaFqUcFEeB3ufJr8kAdqLuvOKeci_F7rptPcTHUyU4pGVvDk5_QxaJhhPjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af7c379d02.mp4?token=mmmke8cEbzIyG4DTUPHuzbjkAVO3LEHo05u9fC6RjOXj7DpYftkQLzzR8aDFRq0U6ecMglovjDEELb07Nks195UYwRV0Y-UrE637OK7XDatZxEHvAR3Xh4pzZWma4Xnrh8dNzpJSJn3CG_mf10pZn0NzpZVNuN58iJGWSxcbb3miPPOuo0R4o3T05iS7Sqa282YKdIINQLmvHbGHiHYBLfw8LuN-r_fI-m8sCklAst5itwouZaCutwWWphqWhOmdz7dKfagQX-Jv3tXjG15i_bo16OHEaFqUcFEeB3ufJr8kAdqLuvOKeci_F7rptPcTHUyU4pGVvDk5_QxaJhhPjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردی اتاق جنگ همه جا هست !
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24570" target="_blank">📅 16:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واکنش نیم میلیون اتاق جنگی به هر‌ خبر بازگشت :
🥚
🥚
ما هدف داریم و فرمول دادم ، فقط بایکت کنید و اصلا انتشار ندید @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24569" target="_blank">📅 16:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">واکنش نیم میلیون اتاق جنگی به هر‌ خبر بازگشت :
🥚
🥚
ما هدف داریم و فرمول دادم ، فقط بایکت کنید و اصلا انتشار ندید
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24568" target="_blank">📅 16:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرگزاری رژیم فارس:
مدیریت بازار دلار تهران عملاً به وزیر خزانه‌داری آمریکا سپرده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24567" target="_blank">📅 16:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مرد خردمند ، مارک لوین : آیا این کار آن‌قدر تحریک‌آمیز هست که آن حرام‌زاده‌ها را نابود کنیم؟ متن تفاهم‌نامه‌ی ما باید این باشد : «ما شما را از بین خواهیم برد؛ فهمیدید؟»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24566" target="_blank">📅 15:55 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

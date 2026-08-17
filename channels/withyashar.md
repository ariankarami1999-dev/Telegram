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
<img src="https://cdn4.telesco.pe/file/OPzn1X_dSWpIGamUkrlSWs5wY3Ph6bcu1UFDL2pt7ZO0c70WCb4HqWIFlSOH7crKM9468D7RNqKWfyhCAXce0wGmolRlJcVExk8-SbZnbL-2Q79LewQmfDhno_nJuOMfXhUyr5Y2M9V3i-qkpXjhD6l8tWGbgU4oTEpuxE_9yI_THjEQuq-iDVGUPw8a1aab-5B2KtpTN0EmCv8ERIInisF3F7zvpc2Hw-pGwYDQN1UCzpxxPrbi-vhqUq8tcSbk0O2WoJggOcfBQmXQkqFEgN7A5NWWM9L9loMqUXSVjPIoFZoRpWDfIeKo9m02VXri9cc-a59RpMWmDNahmBcEgw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 08:34:47</div>
<hr>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e2168088.mp4?token=dVKOyK78sCh-RVVd-jxmtA8JZPTfjNa7QhVqwKdxrnnGGJ052hnicPt8xwS20BeaZepYcscCcFOrixxZ8DjhwBRSr_-2CCz1sRwqrp4MJubkjBphxJO9BCZjRvIlhpcAWAUkUC0YmM9AyRBhA7rviWpEAwuVKApVK3Wt_Y_MfchSyuaUAhsdTIwnOgQyCUE9ApwutTX8aDqbuVf99KDFE8QVid-4ci5PsruyOG6eHJKN8T8YKwSXvL-Yy5UEkBfHej4vJEf7XxiU--h1gJVoFwxTRwl3sWedHWQsCDt4EW6MWSG52DgGsMZ2ZfDoYHYyhb4qe0epcm_xGTNINknTVBnra1NLol3t_AzPdChGiznozNls86gpj-ixqivTZObgjX9C6Fes5bvDB06C6ZeTdrX2k7sKHoE7OLJj8qGx8Mn98c_Wn0N2qydekNIeLxZBanjgYXhZu5tumdNYIm3WRx4B1tDipvHIQCtLrwULhJDsZ9PPmvHDoPVkUTSnN_pZXUqkemawtNFrb69fVaXZAFsvJXVrbxOfzOLfQCd7L9Klyv7FEE3LEmufHwn9W_ImtFZUwyPaxiCVigTAWlydqkCQEERxiBb4hG1twUtYewBGQYItwQy3UMk5G7BtJGg91bKpUn4DoVBBeiD3Kiq8reSLAA8ZlV0bTzHQfR33iNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e2168088.mp4?token=dVKOyK78sCh-RVVd-jxmtA8JZPTfjNa7QhVqwKdxrnnGGJ052hnicPt8xwS20BeaZepYcscCcFOrixxZ8DjhwBRSr_-2CCz1sRwqrp4MJubkjBphxJO9BCZjRvIlhpcAWAUkUC0YmM9AyRBhA7rviWpEAwuVKApVK3Wt_Y_MfchSyuaUAhsdTIwnOgQyCUE9ApwutTX8aDqbuVf99KDFE8QVid-4ci5PsruyOG6eHJKN8T8YKwSXvL-Yy5UEkBfHej4vJEf7XxiU--h1gJVoFwxTRwl3sWedHWQsCDt4EW6MWSG52DgGsMZ2ZfDoYHYyhb4qe0epcm_xGTNINknTVBnra1NLol3t_AzPdChGiznozNls86gpj-ixqivTZObgjX9C6Fes5bvDB06C6ZeTdrX2k7sKHoE7OLJj8qGx8Mn98c_Wn0N2qydekNIeLxZBanjgYXhZu5tumdNYIm3WRx4B1tDipvHIQCtLrwULhJDsZ9PPmvHDoPVkUTSnN_pZXUqkemawtNFrb69fVaXZAFsvJXVrbxOfzOLfQCd7L9Klyv7FEE3LEmufHwn9W_ImtFZUwyPaxiCVigTAWlydqkCQEERxiBb4hG1twUtYewBGQYItwQy3UMk5G7BtJGg91bKpUn4DoVBBeiD3Kiq8reSLAA8ZlV0bTzHQfR33iNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران شد: اتفاقات خوبی خیلی زود رخ خواهد داد. در واقع، آنها همین حالا هم رخ داده‌اند، چون یک کاری هست که ما نمی‌توانیم اجازه دهیم انجام شود: ما نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
@WarRoom</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/21074" target="_blank">📅 02:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKzxkE94Fi0xZFcnx7ShtS7HoTcNadPLcSkf6i34KcLx-i4E1sJLiM6gYBS3_ZNyCVJb2PFo4vrA55nhoRwvJn7EbK0v2DHai3rMJ5o6DgrcE-CpPUyUPWvdn_6BsVYHTpPFW_rYJWX77SEhYzVPlptlTrp8L_AHe_13HV6qwApQCIW79jNKnXDwSRcjYNLy8NLotOMD12lnV7DZk6ishEG9sYJYZFK4DE3CDF0KKKxy4iBpu7ZZVP2KDJyUFHM3ZIwvawUrQW0retn4oavfkBDSqxyyvND_7y2JNLOhTiutytBt9n7uk8OO8OBPh5hU5RoSK0F1NX3O2CJ3xPFg1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :با توجه به رابطه بسیار خوبی که با کیم جونگ اون، رهبر کره شمالی، دارم، از اینکه ایالات متحده مدت‌ها پیش با برگزاری رزمایش‌های نظامی مشترک با کره جنوبی موافقت کرده، خوشحال نیستم. این رزمایش‌ها نه‌تنها پرهزینه هستند و بخش زیادی از هزینه‌هایشان، مثل همیشه، بر عهده آمریکا است، بلکه پیامی کاملاً نامناسب و خصمانه به کشوری ارسال می‌کنند که تا زمانی که دونالد جی. ترامپ رئیس‌جمهور بوده، رفتاری تهدیدآمیز نداشته و محترمانه رفتار کرده است. بنابراین، و با توجه به اینکه دیگر برای لغو آنها خیلی دیر شده است، به پیت هگست، وزیر جنگ، دستور داده‌ام رزمایش‌های نظامی مشترک را به میزان قابل‌توجهی کاهش دهد! البته این موضوع تا حدی بی‌ارتباط است (؟)، اما اخیراً از رئیس‌جمهور کره جنوبی پرسیدم که آیا مایل هستند به ما در خلع سلاح هسته‌ای جمهوری اسلامی ایران بپیوندند و آنها گفتند: «نه، ممنون!» از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/21073" target="_blank">📅 02:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ از نیوجرسی پرواز کرده و در راه واشنگتن است. او به طور خلاصه به خبرنگاران گفت: «آخر هفته فوق‌العاده‌ای بود. جلسات زیادی داشتیم.» وقتی خبرنگاران از او پرسیدند که آیا این جلسات درباره ایران بوده است، پاسخی نداد
@WarRoom</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/21072" target="_blank">📅 01:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ در تروث‌ :بسیار خوشحالم که عربستان سعودی، ترکیه و پاکستان سرانجام و اخیراً توافق دفاعی مشترک مکه را امضا کرده‌اند. این نشان می‌دهد که خاورمیانه در حال متحد شدن است و کشورها سرانجام خواهند توانست به شکلی مؤثرتر و معنادارتر از خود دفاع کنند.به رهبران بزرگ این سه کشور تبریک می‌گویم. این یک گام نخست بزرگ، جسورانه و مهم است , واو!
@WarRoom
واکنش بی بی : فقط کسی توضیح بده دقیقاً قرار است از چه کسی در برابر چه کسی دفاع کنند!
😂</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/21071" target="_blank">📅 00:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ در تروث به‌شدت از برنامه شنون بیم در فاکس‌نیوز انتقاد کرده و آن را هم‌سطح «بدترین بخش‌های سی‌ان‌ان» دانسته است. او می‌گوید این برنامه دائماً مهمان‌ها و نظرسنجی‌های منفی علیه دولتش انتخاب می‌کند و دستاوردهای دولتش را نادیده می‌گیرد. ترامپ همچنین از خوان ویلیامز و جسیکا تارلوف انتقاد کرده و پیش‌بینی کرده رتبه بینندگان برنامه شنون سقوط خواهد کرد. او در پایان تأکید کرده که خودش در دفتر بیضی مشغول ادامه کار برای «پیروزی‌ها و موفقیت‌های بیشتر» است
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21070" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21069" target="_blank">📅 00:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21068" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21067" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سیریک موشک بلند شد
🤠
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21066" target="_blank">📅 00:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سیریک موشک بلند شد
🤠
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21065" target="_blank">📅 23:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">داریوش اقبالی با انتشار ترانه جدیدی به نام «توهم توطئه» و کنایه به شاهزاده رضا پهلوی به کمپین آنفالو توسط مردم پیوست. در صدر این جدول نوید محمدزاده با نزدیک به یک میلیون آنفالو قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21064" target="_blank">📅 23:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز : جرد کوشنر، فرستاده ویژه ترامپ، فردا دوشنبه ۱۷ اوت با بنیامین نتانیاهو دیدار خواهد کرد. این دیدار در چارچوب تلاش واشنگتن برای پیشبرد طرح صلح غزه انجام می‌شود؛ طرحی که شامل خلع سلاح حماس، توقف عملیات نظامی و خروج تدریجی نیروهای اسرائیلی از غزه است.…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21063" target="_blank">📅 23:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال 12 اسرائیل: اعضای حزب الله و سپاه در زیر زمین در ارتفاعات علی الطاهر گیر افتاده اند و تعداد آنهابیش از ده هانفر تخمین زده می شود.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21062" target="_blank">📅 22:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام به وال استریت ژورنال: گروه ضربت ناو هواپیمابر لینکلن تیمی قوی از آمریکایی‌های با دستاوردهای بالا است که با غرور فراوان و موجه به هر آنچه که به دست آورده‌اند، ایستاده‌اند.
تاریخ این استقرار را به عنوان یکی از فشرده‌ترین و مهم‌ترین استقرارهای دوران مدرن ثبت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21061" target="_blank">📅 22:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8429c9c845.mp4?token=Zmt2YS9bosZlsrBnzpqzr27QiahruXdfGdb_DoJf6MAKE-yOiN36X-zZTH6F-AGHokJjVy0Ujh6iHyYE9GwBO_hW0TrgJzaEN2NvzHV88tKf2RITzcRrjlZoootWrt2qxzw6FWQkEHTmvZyRdhWomXdsiWmX0b5mME0y4ymhE6AxBnKpK7s9UXSjyW_FuBLWPJbC7j7Xvxt1yPX8APKumy7GvOf4Oahy2OcBhELmwpURjb993tI8SbWVWwtMWfyuoVj9_VYdqrviWsqLyiAP57eqfXCiHj6uUL2iqx_J_KunTcv7D8POYF2KhEd9KtBtVR8YIuU0_bx20cNhiLiolA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8429c9c845.mp4?token=Zmt2YS9bosZlsrBnzpqzr27QiahruXdfGdb_DoJf6MAKE-yOiN36X-zZTH6F-AGHokJjVy0Ujh6iHyYE9GwBO_hW0TrgJzaEN2NvzHV88tKf2RITzcRrjlZoootWrt2qxzw6FWQkEHTmvZyRdhWomXdsiWmX0b5mME0y4ymhE6AxBnKpK7s9UXSjyW_FuBLWPJbC7j7Xvxt1yPX8APKumy7GvOf4Oahy2OcBhELmwpURjb993tI8SbWVWwtMWfyuoVj9_VYdqrviWsqLyiAP57eqfXCiHj6uUL2iqx_J_KunTcv7D8POYF2KhEd9KtBtVR8YIuU0_bx20cNhiLiolA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ‌ درباره سخنگوی ‌کاخ سفید:
من متوجه شدم که کارولین لیویت فرزندانش را بیشتر از ترامپ دوست دارد، من از این بابت بسیار نگران هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21060" target="_blank">📅 21:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اورشلیم پست :
حماس بخش مهمی از فعالیت‌های خود را از قطر به ترکیه منتقل کرده است.
بر اساس گزارش‌های تازه، بخش عمده فعالیت‌های محرمانه حماس، از جمله واحدهای برنامه‌ریزی و سایبری، به ترکیه منتقل شده و بسیاری از رهبران این گروه نیز بیشتر در ترکیه حضور دارند. با این حال،
دفتر سیاسی و فعالیت‌های علنی حماس همچنان در قطر ادامه دارد
و هنوز انتقال کامل دفتر سیاسی به ترکیه تأیید نشده است. این جابه‌جایی در حالی انجام شده که حماس همزمان برای مذاکرات مربوط به آینده غزه، از کانال‌های قطر، ترکیه و مصر استفاده می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21058" target="_blank">📅 21:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش پرتاب موشک از قشم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21057" target="_blank">📅 20:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رویترز : جرد کوشنر، فرستاده ویژه ترامپ، فردا دوشنبه ۱۷ اوت با بنیامین نتانیاهو دیدار خواهد کرد. این دیدار در چارچوب تلاش واشنگتن برای پیشبرد طرح صلح غزه انجام می‌شود؛ طرحی که شامل
خلع سلاح حماس، توقف عملیات نظامی و خروج تدریجی نیروهای اسرائیلی از غزه
است. نتانیاهو پیش‌تر با بخش‌هایی از این طرح مخالفت کرده بود و کوشنر برای نزدیک‌کردن مواضع دو طرف به اسرائیل سفر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21056" target="_blank">📅 20:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c8cf686.mp4?token=bIgpTNhM9jb4H4aGMluhLJhARSqmzoLyNC-xoVNkJuPgHmM3LIEsD14v1PtEqgxYoxQlid6C5otfJAbMdiD3XA8Ke9rmk4BnuxjXTaD1qGlyCxwKBwJdKcv0nL3NE8EtIwg6RSavc-pETGJ17QQk-P1xzafG55mt4a7RuWuw_-kIUWkvvr-mZd8nkr0MbaqWIlM_2Ogd52gXkHMAYsbLPQkYdsAm-FQtU2VD6hrmyJ6agdLcpFpTT8zGr0F_VzM3rAiuYF5rCVKA2AoESfC8NKM6gURpD5o0n6CRb-cY8XIfN9MZhdk3g3YsipIrWX3adABgIqo0SaiUAn7nPSziMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c8cf686.mp4?token=bIgpTNhM9jb4H4aGMluhLJhARSqmzoLyNC-xoVNkJuPgHmM3LIEsD14v1PtEqgxYoxQlid6C5otfJAbMdiD3XA8Ke9rmk4BnuxjXTaD1qGlyCxwKBwJdKcv0nL3NE8EtIwg6RSavc-pETGJ17QQk-P1xzafG55mt4a7RuWuw_-kIUWkvvr-mZd8nkr0MbaqWIlM_2Ogd52gXkHMAYsbLPQkYdsAm-FQtU2VD6hrmyJ6agdLcpFpTT8zGr0F_VzM3rAiuYF5rCVKA2AoESfC8NKM6gURpD5o0n6CRb-cY8XIfN9MZhdk3g3YsipIrWX3adABgIqo0SaiUAn7nPSziMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرش دعوا شد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21055" target="_blank">📅 20:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏کارزار انتخاباتی جدید نتانیاهو؛ «آنها می‌خواهند نتانیاهو شکست بخورد، اجازه ندهید پیروز شوند» مجتبی خامنه ای، زهران ممدانی ، اردوغان ، نعیم قاسم @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21054" target="_blank">📅 19:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onKnMbFb8Dg2dYTK2y8vW4jDooYBGrXqXTwNmVhxgCSRuBJd78c2slklMTMUZ6prWQL0EFFq8Tf0WNy1gc7ChgXeF0wIUlh332thuCpkPvm8jVZ85ETKD2FihCTimPM-sl_BUfLWkGAoe7rFA_oDjBTaEEpq2LB4dSbH8f_4FvuBwpcUv7xnO-MGV7I33TmbeThqP-KBNcxSlr46Wv-moF6ih3qXcDF8s01GOAUW1vi400bHxjplFctA7DN4aQgivclpCZIwoYQRewg5tqh-HtSTDxjwe8OX9rfvoVnLNb9A7_CRscDiE-MZJXCO4jQStyfYMwFOJp6PCjwdEbTRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏کارزار انتخاباتی جدید نتانیاهو؛ «آنها می‌خواهند نتانیاهو شکست بخورد، اجازه ندهید پیروز شوند»
مجتبی خامنه ای، زهران ممدانی ، اردوغان ، نعیم قاسم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21053" target="_blank">📅 19:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فاکس‌نیوز: مهلت ۶۰ روزه تفاهم‌نامه آمریکا و ایران فردا به پایان می‌رسد.
بر اساس گزارش فاکس‌نیوز، تفاهم‌نامه ۱۷ ژوئن میان واشنگتن و تهران یک بازه ۶۰ روزه برای مذاکره درباره برنامه هسته‌ای و موشکی ایران، تحریم‌ها و آزادی کشتیرانی در تنگه هرمز تعیین کرده بود که مهلت آن
۱۷ اوت
است
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21052" target="_blank">📅 17:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">افسر قطری در گفت‌وگو با الجزیره درباره خلبانان ایرانی اظهارنظر کرده است.
در این گفت‌وگو، سرهنگ دوم
ناصر محمد الکبیسی
از وزارت دفاع قطر درباره سرنگونی دو فروند سوخو-۲۴ ایرانی گفت که هواپیماها بمب حمل می‌کردند و در توضیح منبع اطلاعات، به «تأیید خلبان» اشاره کرد؛ در حالی که قطر پیش‌تر گفته بود خلبانان به تماس‌های رادیویی پاسخ نداده‌اند. این اظهارات دوپهلو اکنون در کنار ادعای ایران درباره زنده‌بودن و اسارت سه خلبان ایرانی، مورد توجه قرار گرفته است، زیرا قطر می‌گوید هیچ خلبان ایرانی زنده‌ای را در اختیار ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21051" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آکسیوس: پیام‌ها میان تهران و واشنگتن همچنان ردوبدل می‌شود، اما مذاکرات در بن‌بست است.
آکسیوس گزارش داده آمریکا و ایران از طریق
پاکستان و قطر
همچنان پیام‌هایی را ردوبدل می‌کنند، اما تاکنون پیشرفت قابل‌توجهی حاصل نشده است. در پشت پرده نیز دولت ترامپ برای ارتباط مستقیم‌تر با
سپاه
یک کانال محرمانه از طریق
بارزانی
ایجاد کرده بود و چند پیشنهاد و پاسخ میان دو طرف ردوبدل شد؛ حتی یک تفاهم اولیه شکل گرفت، اما خیلی زود فروپاشید. اکنون میانجی‌ها همچنان فعال‌اند و بارزانی نیز اخیراً به کاخ سفید پیشنهاد داده برای ازسرگیری مذاکرات آمریکا و ایران کمک کند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21050" target="_blank">📅 17:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رویترز: ترامپ به دنبال تشدید فشار اقتصادی بر ایران است؛ محاصره زمینی هم به‌عنوان یک گزینه مطرح شده است.
رویترز گزارش داده آمریکا علاوه بر محاصره دریایی و تحریم‌های گسترده، گزینه
محاصره زمینی ایران
را نیز بررسی کرده؛ اقدامی که به همکاری عراق، ترکیه، پاکستان، افغانستان، ترکمنستان، جمهوری آذربایجان و ارمنستان نیاز دارد و به‌دلیل دشواری‌های جغرافیایی و سیاسی، اجرای آن بسیار سخت ارزیابی می‌شود. واشنگتن همچنین در حال بررسی تحریم پالایشگاه‌ها و بانک‌های چینیِ مرتبط با نفت ایران و اعمال فشار بر کشورهایی است که به تجارت یا تأمین تسلیحات ایران کمک می‌کنند. رویترز می‌گوید از آغاز دور دوم ریاست‌جمهوری ترامپ،
بیش از ۱۰۰۰ فرد، کشتی و هواپیما
تحریم شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21049" target="_blank">📅 17:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd67bb941.mp4?token=pP_8a2NJc3sBF9RUzpwk-ZIDAsg28RxsznkPrm8ULf9CVwJE-ytkrsHSeuTlR-ph37d_2h6oN7ZmVC_W074yPh1O2Z223jVfbwSxWcQ5q02jsPQofaU3yDsyQOFo_dojOt1g8MlZ7OHSK4PcWMRpKazw6Pp_3ms7__ympuBZXlkM0ajEEBo2BK3WrE8AoJBz-gj4rmEJZ9agrnbT8CEkczjMoEQNwKMfzAfDWkOYN5STn_NRwwXR7mLk1a-oxgs2DOVHYQFZcMefKA1q6gIWARLFSCYUDrYOe9h9XeFgo1fxzaAYm_WrxP0EBdVhRaeVC170jGJV7U9IYuQxHwxdBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd67bb941.mp4?token=pP_8a2NJc3sBF9RUzpwk-ZIDAsg28RxsznkPrm8ULf9CVwJE-ytkrsHSeuTlR-ph37d_2h6oN7ZmVC_W074yPh1O2Z223jVfbwSxWcQ5q02jsPQofaU3yDsyQOFo_dojOt1g8MlZ7OHSK4PcWMRpKazw6Pp_3ms7__ympuBZXlkM0ajEEBo2BK3WrE8AoJBz-gj4rmEJZ9agrnbT8CEkczjMoEQNwKMfzAfDWkOYN5STn_NRwwXR7mLk1a-oxgs2DOVHYQFZcMefKA1q6gIWARLFSCYUDrYOe9h9XeFgo1fxzaAYm_WrxP0EBdVhRaeVC170jGJV7U9IYuQxHwxdBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه اصلی ویدی منتشر شد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21048" target="_blank">📅 16:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/057d64cb85.mp4?token=hJev0xog_RsqvPBLlPiXAZIs8VfzfCAVKifwmoHW1chv0gOsjxjnaoHyfjUGUBkq4Nv4w35Qb4Rrnu-BiSXouTtrjQg9K1L8f6wce2H_-oyWgsN-wNYfwjNecZ41krGiY18MAUavHkp8K93bjmiFMjCQ-kLcRYeP3hGNB-MEOXoHsFGQTBAISgtvbrwsp0_1tf7DdwFdmSvpoHc5vhQvMchL1un9Hk3nSdTFvfMUEh9-Ud8EU_GuMscbNtEHbltDSwjuanthMQy31Og4MSnd4cY15zNxZo5Q6U1beljA6DD6TC5ogoFFnECY9Geimxcb_ESBYvkLpPBlYPlT2QauBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/057d64cb85.mp4?token=hJev0xog_RsqvPBLlPiXAZIs8VfzfCAVKifwmoHW1chv0gOsjxjnaoHyfjUGUBkq4Nv4w35Qb4Rrnu-BiSXouTtrjQg9K1L8f6wce2H_-oyWgsN-wNYfwjNecZ41krGiY18MAUavHkp8K93bjmiFMjCQ-kLcRYeP3hGNB-MEOXoHsFGQTBAISgtvbrwsp0_1tf7DdwFdmSvpoHc5vhQvMchL1un9Hk3nSdTFvfMUEh9-Ud8EU_GuMscbNtEHbltDSwjuanthMQy31Og4MSnd4cY15zNxZo5Q6U1beljA6DD6TC5ogoFFnECY9Geimxcb_ESBYvkLpPBlYPlT2QauBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان رژیم ویدئویی با عنوان «دیدار رئیس جمهور مسعود پزشکیان و مجتبی خامنه‌ای»، رهبر ایران منتشر کردند.
@WarRoom
یاشار : شک نکنید فیکه اگه اصل‌ بود فارس اینا میدادن بیرون نه اینکه یه پیج مداحی تا الان منبع اصلی باشه !</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21047" target="_blank">📅 16:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21046">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرمانده کل ارتش: تنگه مقدس هرمز یکی از لازمه‌های خاتمه جنگ است؛ با همه توان حفظش می‌کنیم
سرلشکر حاتمی:این اهرم یکی از لازمه‌های خاتمه جنگ، به نحوی است که سایه جنگ از سر ایران برداشته شود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21046" target="_blank">📅 16:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21045">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ادعای اکسیوس: ترامپ از طریق بارزانی با سپاه تماس می‌گرفت
مقامات دولت ترامپ کاری غیرمتعارف انجام دادند آنها مذاکره‌کنندگان ایران را دور زدند و مستقیماً با رهبری سپاه تماس گرفتند.
فردی که آنها برای کانال ارتباطی انتخاب کردند، نچیروان بارزانی، رئیس منطقه کردستان عراق بود که چیزی داشت که کمتر کسی دارد؛ اعتماد رهبران ایالات متحده و سپاه.
بارزانی در طول جنگ ایران و عراق در ایران زندگی می‌کرد و در دانشگاه تهران تحصیل می‌کرد.
او به زبان فارسی مسلط است و روابط شخصی با بسیاری از اعضای ارشد ایران، از جمله اعضای ارشد سپاه پاسداران دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21045" target="_blank">📅 13:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نیویورک‌تایمز: جنگ آمریکا با ایران وارد مرحله‌ای اقتصادی شده است؛ واشنگتن در کنار فشار نظامی، تلاش می‌کند با ضربه زدن به درآمدهای نفتی و منابع مالی جمهوری اسلامی، توان تهران برای ادامه جنگ و تأمین هزینه‌های آن را کاهش دهد. این رویکرد یادآور سیاست فشار اقتصادی سال‌های گذشته است که هدفش وادار کردن ایران به محدود کردن برنامه هسته‌ای و بازگشت به مذاکره بود. گزارش می‌گوید این فشار اقتصادی می‌تواند برای آمریکا یک اهرم مهم در مذاکرات آینده باشد، هرچند تجربه گذشته نشان داده که تحریم‌ها به‌تنهایی الزاماً ایران را وادار به تغییر سیاست نکرده‌اند. در نتیجه، مسئله اصلی اکنون این است که آیا فشار اقتصادی همراه با حمله نظامی می‌تواند کار آمد باشد یا نه
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21044" target="_blank">📅 13:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسکای‌نیوز در گزارشی افشا کرده بیش از ۱٬۳۰۰ کاربر استراوا (اپلیکیشن ثبت و اشتراک‌گذاری فعالیت‌های ورزشی و موقعیت مکانی) از پایگاه‌های نظامی آمریکا در خاورمیانه اطلاعات منتشر کرده‌اند؛ اطلاعاتی که مسیر رفت‌وآمد، برنامه روزانه و جابه‌جایی نیروها را آشکار می‌کرد.
کارشناسان امنیتی می‌گویند ایران می‌توانسته این داده‌ها را در کنار اطلاعات دیگر برای رصد نیروهای آمریکایی و شناسایی اهداف استفاده کند. در مواردی در
بحرین و اردن
، تغییر فعالیت‌های ثبت‌شده ظاهراً جابه‌جایی نیروها را نشان داده و مناطقی که این افراد در آن حضور داشتند، بعداً هدف حمله ایران قرار گرفته‌اند. پنتاگون از سال
۲۰۱۸
درباره خطر چنین اطلاعاتی هشدار داده بود و این مشکل همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21043" target="_blank">📅 12:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29877262ff.mp4?token=FQVkhg1C47-X8qlCNVCPVt1MVtc3af-XiYWz9i64gjPvAF5IPVybrpy0StZtxbyZtVlJp_KWCQMvniY1Ne42YCNK0bGiXpKUwE9HnW33YXr5q92RN7lNIUADKrlEEhkVxGZsLBS62vWo3Qju7pde4zQW7vScrbQ0B8ywHerjM2fSLYKI3gI_f6059oTSvp519QJ1PtiVrFZfztKD0WlIdkfEL7x-x0jfJm4NfIZMjIBeYlGYAttPlFy0Atmroi6_PQkOpmf5jtp-YvKMqZMAetQzyBSA8WcA7Av4jBDvA-XTAxzqOxB1WK8yaY6fE6QPw2tnEGLpiMJ91Fgoj1mr7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29877262ff.mp4?token=FQVkhg1C47-X8qlCNVCPVt1MVtc3af-XiYWz9i64gjPvAF5IPVybrpy0StZtxbyZtVlJp_KWCQMvniY1Ne42YCNK0bGiXpKUwE9HnW33YXr5q92RN7lNIUADKrlEEhkVxGZsLBS62vWo3Qju7pde4zQW7vScrbQ0B8ywHerjM2fSLYKI3gI_f6059oTSvp519QJ1PtiVrFZfztKD0WlIdkfEL7x-x0jfJm4NfIZMjIBeYlGYAttPlFy0Atmroi6_PQkOpmf5jtp-YvKMqZMAetQzyBSA8WcA7Av4jBDvA-XTAxzqOxB1WK8yaY6fE6QPw2tnEGLpiMJ91Fgoj1mr7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : پاملا براون گزارشگر سی‌ان‌ان، همین یک ماه پیش در ناو هواپیمابر آبراهام لینکلن حضور داشت و آنها حتی هنگام بازدید از کشتی بستنی هم خوردند و بسیار شاد بودند ! با توجه به این که پنج روز قبل از شروع جنگ ۴۰ روزه و کشته شدن علی خامنه‌ای، خبری پخش شده بود که ناو جرال فورد مشکل توالت و حمام دارد و تمام کارکنان بسیار ناراضی هستند و شرایط خیلی بدی دارند. اکنون با تکرار همان الگو، ممکن است این بار هم یک استراتژی برای حمله دوباره باشد…
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21042" target="_blank">📅 11:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کاخ سفید : موشک کافی برای ادامه جنگ با ایران داریم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21041" target="_blank">📅 11:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ستادکل نیروهای مسلح: تا شکست کامل دشمنان آمریکایی اسرائیلی در منطقه و احقاق حق ملت قهرمان ایران و تسلیم دشمن، از خواست مشروع مردم و مطالبات رهبر عزیزمان، در برابر آمریکای متجاوز کوتاه نخواهیم آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21040" target="_blank">📅 10:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">منم مشکلات زیادی دارم ولی برای شما شاد هستم
😍
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21039" target="_blank">📅 10:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز⁠ گزارش داده که حزب «یاشار!» به رهبری گادی آیزنکوت، ژنرال پیشین و رئیس سابق ستاد ارتش اسرائیل، با شعار مبارزه با فساد و تغییر مسیر سیاسی اسرائیل شکل گرفته است. نام
«یاشار» (ישר)
در عبری به معنای
«راست، مستقیم و درستکار»
است و ارتباطی با نام ترکی «Yaşar» ندارد. انتخاب این نام نیز حامل یک پیام سیاسی است: معرفی حزب به‌عنوان جریانی که می‌خواهد «مستقیم و درست» عمل کند. آیزنکوت از چهره‌های بسیار سختگیر در برابر جمهوری اسلامی و تهدیدهای امنیتی منطقه است,
یاشار در نظرسنجی‌های اخیر به لیکود نتانیاهو نزدیک شده و حتی در برخی نظرسنجی‌ها جلو افتاده است.
رویترز آیزنکوت را یکی از جدی‌ترین رقبای نتانیاهو معرفی کرده و گزارش کرده که حزب او توان بالقوه تشکیل ائتلاف گسترده‌تری نسبت به لیکود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21038" target="_blank">📅 10:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏مارک لوین به وعده خود عمل کرد و نظر سنجی‌را  انتشار داد و گفت : ‏بر اساس یک نظرسنجی اخیر (۱۰ اوت) که توسط تنها نظرسنجی‌کننده‌ای انجام شده که دو دوره انتخاباتی اخیر را درست پیش‌بینی کرده بود، حزب لیکود نتانیاهو پیش‌بینی می‌شود ۳۳ کرسی در کنست به دست آورد و…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21034" target="_blank">📅 10:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21032">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw6Tu--gqCQwkgr0Baln2JG_3TuwbjOxX66HsbWsE_a2t2IKD5j25UKWoUx64G8D2F1Op2IvJ92BsXk2ll_W9ormd_p7y7QMO3-iuMFpubGOI07Qs-BPnyKBk4bK5-HkxUxwiXBJwgobArUM9mNGWr9GMc9A8erA7Fo1wfziOwlm0UpDi-IpoV0j811sZncQ9SXWp9yMOMnOgng8OrRNwBBalAsM8kd6XCnVmpWaZfNb50VIPmg4523Bo7V7k7HOzGUaTDOXGGvxy3LAmin241beU5fAI_GRjWy6eZIvUcPz7F7FajWfmYfpI93rdDogm3NbvYmuEfsDkda6FO5QSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : من قویاً معتقدم که پرزیدنت ترامپ باید از نتانیاهو حمایت کند، چون در مقطعی برای ادامه مقابله با ایران به او نیاز خواهد داشت. به احتمال زیاد، نتانیاهو در هر صورت پیروز خواهد شد. اما بر اساس اطلاعات منابع من، در دیدار آنها هیچ توطئه یا زدوبندی در…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21032" target="_blank">📅 09:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21031">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مانوک : رژیم پاشیده
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21031" target="_blank">📅 09:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21030">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b22325bf.mp4?token=p3CGXKs__OUFRGQOsHygiPbJjD56sMxtdbp0I8Tt6-FHQBjp-Xq4cH-7fjDs5SbRa9R2RCK7Rl2ilv22nKfLGMmazQDxYrP2eHUT8HzuFvCunpxs8LDkKJjRu4CT0ED4uDkqUYxcFdD_WqCkYiYdYDnmtbjZx5yJ1dLiWlM2a_rsyFWdZjSOucb9X-7UVBSBVLjm3g0Bfr41MsZ9Zw-NpK2yGD6SPcStZ3lLEivkNcxIjCNtuS0-cKVIiMB2CWtsj4teCP3x8qJvgh_7zs6fKuGp5jJeFxED_9n11SE_KytTDNbttUjharHoWWz_pOeE72vNKPixea1LZ-Q-BorQKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b22325bf.mp4?token=p3CGXKs__OUFRGQOsHygiPbJjD56sMxtdbp0I8Tt6-FHQBjp-Xq4cH-7fjDs5SbRa9R2RCK7Rl2ilv22nKfLGMmazQDxYrP2eHUT8HzuFvCunpxs8LDkKJjRu4CT0ED4uDkqUYxcFdD_WqCkYiYdYDnmtbjZx5yJ1dLiWlM2a_rsyFWdZjSOucb9X-7UVBSBVLjm3g0Bfr41MsZ9Zw-NpK2yGD6SPcStZ3lLEivkNcxIjCNtuS0-cKVIiMB2CWtsj4teCP3x8qJvgh_7zs6fKuGp5jJeFxED_9n11SE_KytTDNbttUjharHoWWz_pOeE72vNKPixea1LZ-Q-BorQKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز با دسترسی نادر به یک پایگاه ارتش اسرائیل، مجموعه بزرگی از سلاح‌های ضبط‌شده از حماس و حزب‌الله را به نمایش گذاشته است؛ مجموعه‌ای شامل راکت، پهپاد، خمپاره، موشک ضدزره، تفنگ تک‌تیرانداز و مسلسل. به گفته اسرائیل، بخشی از این تسلیحات ساخت ایران است و سلاح‌هایی از روسیه و چین نیز در میان آنها دیده می‌شود؛ حتی یک مسلسل آلمان نازی
MG34 مربوط به جنگ جهانی دوم
نیز در این انبار وجود دارد. این مجموعه تصویری از گستردگی و تنوع تسلیحاتی را نشان می‌دهد که اسرائیل می‌گوید از گروه‌های مورد حمایت ایران از زمان ۷ اکتبر کشف و ضبط کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21030" target="_blank">📅 09:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21029">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خبرگزاری قوه قضائیه : شهرام صادقی که در ۱۸ دی ماه پس از حمله به مامورین با خودروی پراید ۷ مامور را زیر گرفت به اتهام اقدام عملیاتی به نفع اسرائیل و آمریکا، بعد از اذان صبح امروز، حکم وی اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21029" target="_blank">📅 08:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21027">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سنتکام :
فرمانده سنتکام پس از سفری ۱۰ روزه به خاورمیانه بازگشت.
دریادار
برد کوپر
در این سفر به
بحرین، عراق، اسرائیل، اردن، عربستان سعودی و امارات
رفت و با مقام‌های ارشد سیاسی و نظامی این کشورها دیدار کرد و همچنین از نیروهای آمریکایی مستقر در منطقه بازدید داشت؛ سنتکام می‌گوید بیش از
۵۰ هزار نیروی آمریکایی
در خاورمیانه مشغول مأموریت هستند. کوپر در جریان سفر خود همچنین برای دومین بار در سال جاری از ناو هواپیمابر
USS Abraham Lincoln
در دریای عرب بازدید کرد. سنتکام اعلام کرده این ناوگروه تاکنون
هزاران پرواز رزمی
در پشتیبانی از عملیات «Epic Fury»، مأموریت‌های امنیت منطقه‌ای و
محاصره دریایی آمریکا علیه ایران
انجام داده است. کوپر درباره استقرار آبراهام لینکلن گفت این مأموریت از نظر شدت و پیامدهای عملیاتی، یکی از مهم‌ترین مأموریت‌های دوران مدرن بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21027" target="_blank">📅 07:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عراقچی می‌گوید اساساً چیزی به نام
«آتش‌بس ۶۰روزه برای تمدید
بعد از نقض آن توسط آمریکا
وجود ندارد»
و تفاهم اسلام‌آباد از نگاه ایران
پایان جنگ بوده، نه آتش‌بس ۶۰روزه
. با این حال، اگر مبنا را همان دوره ۶۰روزه و پایان آن در
۱۷ اوت
بگیریم، با فرض ساعت ۰۰:۰۰ واشنگتن، موعد پایان آن در ایران
ساعت ۷:۳۰ صبح ؛ یکشنبه
(اگر مبنا آغاز روز) و
دوشنبه ۲۶ مرداد
(اگر مبنا پایان روز) باشد پایان میابد
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21026" target="_blank">📅 23:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قطر ادعای ایران دربارهٔ به اسارت گرفته شدن سه خلبان ایرانی توسط این کشور را قاطعانه تکذیب کرد
و گفت تهران تاکنون به دعوت دوحه برای اعزام هیئتی به قطر و بررسی جزئیات عملیات جست‌وجو و نجات پاسخ نداده است.
سوخو-۲۴ ایران روز ۱۱ اسفند ۱۴۰۴ برای انجام مأموریتی علیه یک پایگاه نظامی در قطر اعزام شدند و هنگام بازگشت هدف پدافند قرار گرفتند.
بر اساس روایت ایران، چهار خلبان این دو جنگنده اجکت کردند که یکی از آن‌ها، مجید کاظمی، کشته شد و سه نفر دیگر به نام‌های جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان «زنده توسط نیروهای قطری به اسارت گرفته شدند».
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/21025" target="_blank">📅 22:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21024">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دیدبان اتاق جنگ : سیریک هرشب قبل اینکه بزنن یک ساعت برق قطع میکنن بعد که وصل کردن شروع میکنن شلیک
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/21024" target="_blank">📅 22:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21023">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش صدای ۳ انفجار/شلیک در‌ سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/21023" target="_blank">📅 22:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21022">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏دونالد ترامپ در تروث‌سوشال ویدیویی را منتشر کرد که در آن بهنام طالب‌لو، مدیر ارشد برنامه ایران در بنیاد دفاع از دموکراسی‌ها، بر تاثیر محاصره دریایی آمریکا در کاهش صادرات نفت ایران تاکید کرده و می‌گوید محدود کردن حکومت ایران از نظر بودجه‌ای پس از پایان درگیری‌ها، در کنار محاصره، به آمریکا اجازه می‌دهد از دلار به‌عنوان یک سلاح استفاده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/21022" target="_blank">📅 22:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21021">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21021" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21020">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اندی بیکر، یکی از نزدیک‌ترین چهره‌های امنیتی به جی‌دی ونس، در هفته‌های آینده کاخ سفید را ترک می‌کند.
بیکر که سال‌ها مشاور امنیت ملی ونس بوده و در دولت ترامپ نیز در تصمیم‌گیری‌های مهم سیاست خارجی و امنیت ملی نقش داشته،
مستقیماً در مذاکرات آمریکا و ایران حضور داشت
و به جناح مخالف جنگ شناخته می‌شد.  خروج او در حالی رخ می‌دهد که جنگ ایران همچنان موضوعی حساس است؛ هرچند دلیل رسمی برای رفتنش، تمایل به وقت بیشتر با خانواده و سرمایه گزاری های شخصی عنوان شده ، همچنین
در مورد شایعه افشای اطلاعات محرمانه نیز اتهام مستندی علیه بیکر منتشر نشده، اما با توجه به دسترسی او به پرونده‌های حساس و نقش مستقیمش در مذاکرات، این گمانه‌زنی درباره علت واقعی خروجش مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21020" target="_blank">📅 19:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21019">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مارک لوین : من قویاً معتقدم که پرزیدنت ترامپ باید از نتانیاهو حمایت کند، چون در مقطعی برای ادامه مقابله با ایران به او نیاز خواهد داشت. به احتمال زیاد، نتانیاهو در هر صورت پیروز خواهد شد. اما بر اساس اطلاعات منابع من، در دیدار آنها هیچ توطئه یا زدوبندی در کار نبوده است. آکسیوس این گزارش‌های منفی را با هدف تأثیرگذاری بر سیاست‌گذاری و انتخابات اسرائیل، از دیدگاهی چپ‌گرایانه و افراطی، در زمان‌بندی خاصی منتشر می‌کند.
همچنین نتانیاهو بر اساس آخرین نظرسنجی‌ای که در انتخابات قبلی واقعاً نتیجه را درست پیش‌بینی کرده بود، وضعیت خوبی دارد. آن نظرسنجی را پیدا می‌کنم و جداگانه منتشر خواهم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/21019" target="_blank">📅 19:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21018">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیانیه دفتر نتانیاهو : امروز صبح، حزب‌الله توافق آتش‌بس در لبنان را نقض کرد، زمانی که به سربازان ما در منطقه امنیتی که از شهرک‌های اسرائیلی واقع در نزدیکی مرز محافظت می‌کند، حمله کرد. در این حمله، سه تن از سربازان ما به شدت مجروح شدند. ارتش اسرائیل با بمباران مقر فرماندهی حزب‌الله که دستور حمله را صادر کرده بود، پاسخ داد
…
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21018" target="_blank">📅 18:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21017">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">واشنگتن پست : هیچ توافق خوب و قابل‌قبولی با ایران نمی‌توان منعقد کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/21017" target="_blank">📅 17:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21016">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اردوغان به شبکه الجزیره: اولویت ما بازگشایی تنگه هرمز است، زیرا ادامه بسته بودن آن به نفع هیچ‌کس نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/21016" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21015">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ستاد کل نیروهای مسلح ایران اعلام کرده است سه خلبان ایرانی به نام‌های
جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان
که در جریان حملات اسفندماه جنگنده‌های سوخو-۲۴ آنها سقوط کرده، زنده مانده و حدود شش ماه است در
قطر به اسارت نیروهای قطری
درآمده‌اند. محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین، گفته این خلبانان هنگام بازگشت از یک مأموریت رزمی پس از هدف قرار گرفتن جنگنده‌ها توسط پدافند، اجکت کرده‌اند. او با استناد به کنوانسیون سوم ژنو خواستار دسترسی کمیته بین‌المللی صلیب سرخ به آنها شده و گفته قطر تاکنون اجازه تماس یا دیدار خلبانان با خانواده‌ها و مقام‌های ایرانی را نداده است.
قطر تاکنون به این ادعا واکنش رسمی نشان نداده است
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/21015" target="_blank">📅 16:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN_-gm3oBAsreDu-71T6qRDfHlePOu9LBSiHFnW1nyPrLJtONdjaruOI_f0R96WYBZ_KjEwTNFZhEnlwLtNE1EwotM3p6hg8GipHO2wxU3JiRuKHYicpH3_IU06MIdjotx19bKVpDvnzg4pvzGlKs--v6-Y_PRAz6Sb5mj1WBxO6kpwXycTOpG3St-wz2ZDD6iJppNplnqsxH_Ein98cmaF0AilY7d34e1M3WD4pW_LgPm9D4zOC4XjPKgM7ue98HeywnWb43doALlSPAtOzHdzQCW3rnW0EXnKeK7WohbJ13w-YT4OumUkwLFpIwB5CpudUeR7nIeVD_4g3gSKwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : اندازه هواپیما هایی که ما در اتاق جنگ زیاد سروکار داریم
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/21014" target="_blank">📅 15:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21013" target="_blank">📅 14:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرنگار الجزیره: ۳ حمله هوایی اسرائیل بامداد امروز، مناطق اطراف شهر النبطیه الفوقا و حومه شهر انصار در منطقه النبطیه را هدف قرار داد. @WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21012" target="_blank">📅 12:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21011">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9z0PABk-c1gU00MtGPtQRfDlcSJxiwhuip_-ldsXDuUrumqDsbonk7DFDvEAGalmyKQtkmNC4t65LaTdw9JQ3UloOfMRUyVJTJjBS5lvVoNSry3YntV5KSKsSstHX6rzeb2XceigEDqiPiGtofl6t_s8qMLynIm1pt8by6F31sN5J79S78R7vdirBIWKj1G8D3zBa_-TBSGlfJr_W_Wfqp5X4VtLVH7I3T1unFLG5bpl6ksSS0EWpMeGkYymS81m3vWWtXRWMEL3o4l0vp8ogAnLUSA9VJczHwH2ftozdXvBJDmp--Qv0N43oW5l4t4SAPITWmKyVVZf2SA1E64WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیوار فولادی، محاصره
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/21011" target="_blank">📅 11:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21010">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaaScqPw8BQZZqZIMxhKO0Mty_RpAgzNItD9ClFLbD5Zd1UfzG1U53Pap6h_ruzVbYNZ6_MdkHo1TuN1_Dk73LbkgUgtP5VP31Bw0Ceqbd7R5YKWZTAqwI69QSWsk-1upStkDcdDWBjhl9x2F7f91CH1fLo-nglema0QgcgUFhNCFKFtM6ecvNxYXxqirVlzWSvf5BguJe6Lsf-q45zbbuP2UZ82cjkxn8VvAE1-q6EbvNCr8wLCOyj2s6XCrWZZmZYWaKG1olrBZh29t_1xacxkxBr9AH_Z5fiBgoKPqgKBlba__BU4KvEL981cOrbFjiSSzH61aVjX11PSeLQ2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ : تصاویر ماهواره‌ای منتشر شده توسط رویترز: دو لکه نفتی در نزدیکی جزایر قشم و سیری ایران در خلیج فارس مشاهده شد، در حالی که حملات مکرر به کشتی‌ها در این منطقه ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21010" target="_blank">📅 11:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21009">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مستند دیدنی
«جاسوس ۲»
از کانال ۱۴ اسرائیل ، که در آن با مأموران سپاه مصاحبه میشود !
با زیرنویس فارسی
، پیش تر قسمت اول را برای شما قرار داده بودم… از دست ندید…
🌐
@WarRoom
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21009" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21008">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNBVYZihIQwn14INMnbnUWrsvjwgOirygBHQJQOOQZzL2tym1KDc9s-g4UHxximliRhrDXg7wI1jPr7KHDwezWLLJwZwqkjj4TjcRDrDXVcLhTukJBVI0EkkMQqoaFh-XsjXe6oYBKEEuskXAhtd8DXqIER_OnSHvmJq1V47vKSLyurEZ1IDBIO6dwI_RRoNcoklMI4vnlAErw8HDU8NQrdLm9RFV2E6NZLP_Dd3VZlMSH9EYZLYs7MqPUnwp_VALU12KSHn_Mjci8VYQHcw5-uZXWkaZQ7-Rl-2SWCyDwDDYNcXplIlTPq_3gm2Fp3uTmA918heT-p5sqX-AzYA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : خط جدید ترابری لاجستیکی نظامی آمریکا و کد عملیات «مووسی MOOSE» نشان میدهد در جنگ بعدی پایان دهنده کار، آمریکا بر روی پایگاه خود در قاهره حسابی ویژه ای باز کرده و مرکز پشتیبانی عملیات خواهد بود هم نزدیکی به منطقه هم فاصله دورتری نسبت به کشورهای حاشیه خلیج فارس…
سفر قاهره تازه شروع شده…
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21008" target="_blank">📅 10:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21007">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرنگار الجزیره: ۳ حمله هوایی اسرائیل بامداد امروز، مناطق اطراف شهر النبطیه الفوقا و حومه شهر انصار در منطقه النبطیه را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21007" target="_blank">📅 10:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21006">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhGXHDmYC2q2ITvd8pRiLEBBgmL0dXiIMgty6y2r5P-YXVH3_0YMCRSRgyWH6UIlD5fDm5-5goioOvXldeS0ihmISHeuEW0K3unBN6Y20Vlkmt0vkUeXps-BF77QyL6YIbqCSiuocsTkJscQRg1uEjljxgTku4dZzhtyaZX-VWTNCbiFmzU8L93u6RZQNiEoLrfS_K9peW7ddQd6Bw5f75JiVcwiLQTE9Qzum3DaO4aPSf0ohiSskbXWRzTRYsA8p_q-S4QeIrvYMFixxteu0DFgZl3FylwK7t8cbYPWeuwEEPuseNww6Zzyp2yu0rBL4IHUHC_l9FJAaIM2sp8eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏UKMTO گزارش تأیید شده‌ای مبنی بر برخورد یک پرتابه ناشناخته به بدنه یک کشتی فله‌بر دریافت کرده است. خدمه در سلامت گزارش شده‌اند، هیچ ارزیابی خسارتی گزارش نشده است و در حال حاضر تأثیر زیست‌محیطی آن مشخص نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21006" target="_blank">📅 09:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21005">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادعای نیویورک‌تایمز: مشکل تأمین و تدارکات ناو آبراهام لینکلن پس از آن آغاز شد که ایران، به پایگاه نیروی دریایی آمریکا در بحرین آسیب شدیدی وارد کرد و یک مرکز لجستیکی مهم را از کار انداخت
سپس پنتاگون مرکز تأمین و پشتیبانی منطقه‌ای خود را به دیه‌گو گارسیا منتقل کرد که ۳۵۴۰ کیلومتر از ناو‌های آمریکایی فعال در دریای عمان، فاصله دارد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21005" target="_blank">📅 09:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21004">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCay-zHAWLGw1Cd256NHcFIf2tU2yWSd5FfzVL8nCJmdcfE6dS7spjonAsFgV8sfulESRfwH04NtvY5iMJfeio3YJFXOAlC0YEvSk4xCG76zeFtzpF-5OlI9vZLdQJmdiijfyGSm7I4TPZ8rkFy3dhT7HeT71umD7CG45w4mIYGo8RL6mxqUt21l_fqLSKwTHcQ2xgJXifvGAG7wDDSxhZBhGzIgBFr5KuwXUieHfQ9h6LpmSNMi4VbclW9YttoATltmzQJ9gvL60x8zqKHEbqtOYRNOKA1aqBLNXPOv_SnAn-Njvj0powthaK22Iiqr0clTzMULau5MIWSs7JhjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز : آقای معاون رئیس‌جمهور، یک لحظه به توافق نزدیک هستیم، لحظه بعد می‌گوییم قرار است حسابی آنها را بمباران کنیم. یک لحظه تنگه هرمز باز است، لحظه بعد بسته است. مطمئنم این نگرانی و سرخوردگی داخل کاخ سفید هم وجود دارد. می‌دانم پیش‌بینی کردن دشوار است،…</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21004" target="_blank">📅 03:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21003">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ در مورد ایران: به زودی تنگه هرمز را جزو قلمرو ایالات متحده اعلام خواهم کرد.  ایران به شدت شکست خورده است. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21003" target="_blank">📅 03:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21002">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2jEk1TgFe9R_tmfITHXdpzy-tC4yNvlzUddNwf4MUCFlQzzJSLH7PcaZFTS0ny3OmFn7zhbIGpNmRQ2B-gWGA0Z7TXKPUPit3B_6XrBzIj6BuLn6wLxjvObcIU2FmxHk-_M9emMerVg8vthq8VuxC550lA7GxM0vsGRq34Y9NQzXSiJ4HEuMSZsiZWT38cKU-QBjTA40APliFnzjGebYO4upOn07J36PnkCtAktEZvoR_gk9SCnhesBGRFlFZj9l3zMJlp-oMKYKNiohpW6u8DSFgfpFisXC5jB8QNzvXJf8WygHN6Zk6qweKNyoOXtMf-gcRk-PfGDvKkxvfiWIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار هواپیمای C130 سوپر هرکولس از آمریکا به انگلستان و یک C5Mسوپر گالاکسی، یک راست از آمریکا به خاورمیانه میآیند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21002" target="_blank">📅 02:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21001">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وقوع زمین‌لرزه ۷.۴ ریشتری در اندونزی!
دو زمین‌لرزه جدید با قدرت های ۶.۱ و ۶.۶ ریشتر نیز دقایقی بعد رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21001" target="_blank">📅 02:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21000">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRoRj48XYsZkvf2Q7vnvCHxuMKMwhruYSdA3qL4Cuv_dXoDhxAiHlC5363CHaxrrtRK-aTH7TuO-Zn0CpsGpfzHJzGuasNiNOUCjtZo5AoADIBeonIhkuiUiJqlQAhwOsOJiNLZeldZ1joDGuMVm_Vgr2DsomcDYeJeJfXhj0-cNCY4_QFD50rrwTC-DqslHRQbcXvnsOq9b5SHOQ4iJurnnHqqrjZN6YaQohm-0dsfYP7lcQ_9F3Q0dIrKTiWO7S9p3LS1MxDiD0s4jTeJG3YC3rLP1fG-eBKv_ehmzSMXYd10hWXaur8lC7AQL-HKK6RXIKWIi9Dx3AnBqzVIe3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام E3B-Sentry با رادار AWACS هم راه با ۴ سوخترسان هم اکنون در منطقه خلیج فارس انجام مأموریت میکنند
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21000" target="_blank">📅 01:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20999">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">@WarRoom
مسیر من</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20999" target="_blank">📅 01:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20998">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from………..</strong></div>
<div class="tg-text">درود یاشار
شما بیشتر خرف های جاوید نام روح الله زم رو بیشتر قبول دارین یا استاد مانوک خدایخشیان؟
ممنون میشم جواب بدی</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20998" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20997">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">@WarRoom
مسیر ما</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20997" target="_blank">📅 01:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20996">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">@WarRoom
مقدمه</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20996" target="_blank">📅 00:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20995">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: تمام کشورهای منطقه در شرایطی شبیه به محاصره قرار دارند، زیرا ایران به عنوان یک کشور زورگو در خاورمیانه شناخته می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20995" target="_blank">📅 00:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20994">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=S6-tDuGFYOIB6N7aUklFRUPcIU2H8uBvbUCsjX5a4nQCWCTL32UwrRGeeLL7jOUrgvGaTrpjIvGSj9vvvAjn5O_cFk1lNzCgA4a4n84ajswnj_epXVjL_s3iroewlKLn49Ldz8-wrRqTespVHuj2JjodpvlJCLyz85eYD8nVtZw7TWQSxCOruJhuG9cHgvLqgMdhQitPEpE9F9RzsOqWmQJ0CF8INmqq_x3NETo0zlxLyj53IZD6LFpjX44JH6u7PObkt9Tw0IoK8HFAYTN8k-scZK5gG-D_8VDzvMFN2c14XVc_9vuGaIx6SzD2dNCUL4-1Pa_TQdmehstqNhKt3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=S6-tDuGFYOIB6N7aUklFRUPcIU2H8uBvbUCsjX5a4nQCWCTL32UwrRGeeLL7jOUrgvGaTrpjIvGSj9vvvAjn5O_cFk1lNzCgA4a4n84ajswnj_epXVjL_s3iroewlKLn49Ldz8-wrRqTespVHuj2JjodpvlJCLyz85eYD8nVtZw7TWQSxCOruJhuG9cHgvLqgMdhQitPEpE9F9RzsOqWmQJ0CF8INmqq_x3NETo0zlxLyj53IZD6LFpjX44JH6u7PObkt9Tw0IoK8HFAYTN8k-scZK5gG-D_8VDzvMFN2c14XVc_9vuGaIx6SzD2dNCUL4-1Pa_TQdmehstqNhKt3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20994" target="_blank">📅 00:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20993">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxC4oumXEpTs0wssOyZE4tF8KAA7fxQYKbXI0TMGxFjW63e3nqGRCIRiP2X5pxwC-rMByeyC9qZjlHq1aTVBYtKmVvZtEzVwdKQBazDNtGf4aX0JNsd4YswY7qw9rMm969ZQqJv3pQt8O7b_p1NKGTAp2QavadrIMPk3iBsA2jieat74bPULTvl_iKDx7BsFsz4O1PO8bR_Rolb6d1_Be_IdIilmvCLDG_8sHZpbnDPZ9ztvqiGNgpe2VYjx5JfxKZuTFMSUcUajI9gTndYQjyZ5uTbPbxN_3bE_6XDtJ8yntjh610ZCzJ618CQOK6sWfB4AD2A5U4odSMWwsfW6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست در اتاق جنگ  در حال شنیدن گزارش نیروهای مستقر در خط مقدم فرماندهی مرکزی آمریکا (سنتکام) در حوزه‌های هوایی، زمینی و دریایی، از جمله ناو هواپیمابر
USS Abraham Lincoln
، هستم.آمریکایی‌های شگفت‌انگیزی که در حال انجام یک مأموریت تاریخی هستند.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20993" target="_blank">📅 00:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20992">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e4825bc3.mp4?token=Xr2sI3vO2sQV_jWOm5YJSIqUi49hiMzzEAZ6EvimyyezqPuGf92Yh9QtfnCRBBli0L216cBcO_nVQJULBhv2zVs2W7Gs-eoL6ZSHWKmnlxDQxHxLupG9JrAfrK7bUwSHUzY-577lwRbPiWqpKAIghFZNlVlbW_5km3aw88dTZtv4VWRrDwfjMQYmPgpBzXmvksoQIkSSYcxznC0E2pZ--114JYT0oJQX9l4789bsbO4BPAs42YU-_bqtCW7foiJspqyr-qEODwFLarkJdofgNjfPpR0ctunvCkrHqvLiNEjEsQgRoZV1hM1xNk1UkWmKZ3mqbQ5XjGERxuxhsmh01Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e4825bc3.mp4?token=Xr2sI3vO2sQV_jWOm5YJSIqUi49hiMzzEAZ6EvimyyezqPuGf92Yh9QtfnCRBBli0L216cBcO_nVQJULBhv2zVs2W7Gs-eoL6ZSHWKmnlxDQxHxLupG9JrAfrK7bUwSHUzY-577lwRbPiWqpKAIghFZNlVlbW_5km3aw88dTZtv4VWRrDwfjMQYmPgpBzXmvksoQIkSSYcxznC0E2pZ--114JYT0oJQX9l4789bsbO4BPAs42YU-_bqtCW7foiJspqyr-qEODwFLarkJdofgNjfPpR0ctunvCkrHqvLiNEjEsQgRoZV1hM1xNk1UkWmKZ3mqbQ5XjGERxuxhsmh01Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما قادر به نابودی کل کشور هستیم. ما نمی‌خواهیم این کار را انجام دهیم.
ما تحریم‌های اقتصادی علیه آنها داریم که هیچ کس قبلاً نداشته است.
اگر آنها حمله کنند، ما ۱۰۰ برابر سخت‌تر پاسخ خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20992" target="_blank">📅 00:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20991">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: ایران همچنان موشک‌هایی دارد، اما این بخش کوچکی از موشک‌هایی است که قبلاً در اختیارش بود.
تولید موشک‌ها در ایران 82 درصد کاهش یافته و توانایی‌های تولیدی آن‌ها تا حد زیادی از بین رفته است.
نرخ تورم در ایران به 350 درصد رسیده و ارزش پول آنها هیچ است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20991" target="_blank">📅 00:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20990">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ: آن‌ها رهبری ندارند. ما رده‌های اول، دوم و سوم آن‌ها را از بین برده‌ایم. این یکی از مشکلات من است، زیرا کسی وجود ندارد که بتوان با او مذاکره کرد.
ما رادارها و تمام تجهیزات اطلاعاتی پیشرفته و مدرن ایران را نابود کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20990" target="_blank">📅 00:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها ۲۱۲ هواپیمای بسیار خوب داشتند که برخی از آنها به طرز درخشانی از طریق اوباما از ایالات متحده خریداری شده بودند.
همه هواپیماهای آنها از بین رفته‌اند.
یکی از مشکلات ایران این است که کسی برای مذاکره وجود ندارد. این یک مشکل است.
این تنها کشور در جهان است که هیچ کس نمی‌خواهد رئیس جمهور شود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20989" target="_blank">📅 23:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20988">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ: هیچ کس نمی‌داند که ما در ایران تا چه حد موفق بوده‌ایم.
می‌دانید چه کسی می‌داند که ما در ایران تا چه حد موفق بوده‌ایم؟ خود ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20988" target="_blank">📅 23:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20987">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ : به همکارانم گفتم: «ما باید سفری به خاورمیانه داشته باشیم، زیرا باید از یک فاجعه بالقوه، یک آتش بسیار بزرگ که مثل آن را قبلاً ندیده‌اید، جلوگیری کنیم.»
وقتی مجبورید برای بنزین خود کمی بیشتر هزینه کنید، من هرگز عذرخواهی نخواهم کرد. من کار درستی انجام دادم.
یک کشور بسیار بد، نباید سلاح هسته‌ای داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20987" target="_blank">📅 23:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20986">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ درباره ایران:
جنگ با ایران، خدمت بزرگی به جهان است و ما کار فوق‌العاده‌ای انجام می‌دهیم.
من هرگز عذرخواهی نخواهم کرد، من کار درستی انجام میدهم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20986" target="_blank">📅 23:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20985">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ: اگر ایران به ما حمله کند، ما با صد برابر قدرت بیشتر پاسخ خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20985" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20984">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: ما نمی‌توانیم اجازه دهیم که ایران به مسیر فعلی خود ادامه دهد. اگر ما آن‌ها را با بمب‌افکن‌های B-2 مورد حمله قرار نمی‌دادیم، آن‌ها سلاح هسته‌ای به دست می‌آوردند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20984" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20983">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ درباره ایران: من هرگز عذرخواهی نخواهم کرد، من کار درستی انجام دادم.
ایران، بدترین حامی تروریسم در جهان است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20983" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20982">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ در مورد ایران: آمریکا قرار است زین پس هزینه بسیار کمی برای بنزین بپردازد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20982" target="_blank">📅 23:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20981">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درباره ایران: محاصره اقتصادی، دیواری فولادی است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20981" target="_blank">📅 23:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20980">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb3349271.mp4?token=JHppwNzqOFLjDs9PmFqZc26eUl2oquraEIf8i0QuUn4oldaUzu6oOSk7EX-XmCn2yLYbCqxkbLG2UC63DdGqxQm4LHLD4bsfb1jDIxgSUHUIK741-3uGIGNY8enqPbx08zcZDl-KAKm42IYKOXpp9UJ6CmV-FbYvA6Z7wWHWtpe9M1k7rg0p87Pk7s78J9Hi41Vs3pmvUeTrFMJASR89XtgnL05JIwludrgzucl2GXh6H115OB668p_BgyKiBrWpJugC-3UajmPEbRbkM9Mglk2idu1N-kUvtktMZUgLdwKQnFk3uwnR6xFAJCSGbBuK5D_IgKU2SSi83h_rQ3oP-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb3349271.mp4?token=JHppwNzqOFLjDs9PmFqZc26eUl2oquraEIf8i0QuUn4oldaUzu6oOSk7EX-XmCn2yLYbCqxkbLG2UC63DdGqxQm4LHLD4bsfb1jDIxgSUHUIK741-3uGIGNY8enqPbx08zcZDl-KAKm42IYKOXpp9UJ6CmV-FbYvA6Z7wWHWtpe9M1k7rg0p87Pk7s78J9Hi41Vs3pmvUeTrFMJASR89XtgnL05JIwludrgzucl2GXh6H115OB668p_BgyKiBrWpJugC-3UajmPEbRbkM9Mglk2idu1N-kUvtktMZUgLdwKQnFk3uwnR6xFAJCSGbBuK5D_IgKU2SSi83h_rQ3oP-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: به زودی تنگه هرمز را جزو قلمرو ایالات متحده اعلام خواهم کرد.
ایران به شدت شکست خورده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20980" target="_blank">📅 23:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20979">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">لحظاتی پیش حمله هوایی اسرائیل به المنصوری در جنوب لبنان انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20979" target="_blank">📅 23:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20978">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کاخ سفید: به مجازات ایران و فلج کردن اقتصاد آن ادامه می‌دهیم. ابزارهای بیشتری برای اعمال فشار علیه ایران در اختیار داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20978" target="_blank">📅 22:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20977">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آنا کلی، معاون سخنگوی کاخ سفید، درباره ناو هواپیمابر لینکلن:
رئیس جمهور ترامپ بیش از هر کسی به سربازان اهمیت می‌دهد.
به یاد داشته باشید که جو بایدن تمرکز را از جنگجویان به سیاست‌های حمایت از نیروهای دفاعی تغییر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20977" target="_blank">📅 22:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20976">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به گزارش کانال 13 اسرائیل، اسرائیل قصد داشته به مواضع ترکیه در سوریه حمله کند، اما ترامپ مداخله کرده و مانع آن حمله شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20976" target="_blank">📅 22:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20975">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ced329bda.mp4?token=LXRr0zNHQ9TXGxajYGKRwTj1u3Bk-f7pEN4a25nflEGhdVN1soMMjJPfLO7QyXz-YPt5uve-vvOT5T-HPUCVoptyBBZkbbnd7AnyzMibEvUb0HJ-8VBtgCmtEPidkIGh83911yJ2KUtrIzRIpGbrTUQkV4Yxq2MA4S5Ne65bBBMwRjOY18glDdRrOKQ1t6sp_bzaR0iHVka4FzfkQLPfuyYJaQmm_17BwK5zKRvmeL9zt-blRrUeJeWZ0KT8ay8idmsoTGw0nfwXzae-COgFQQ6FRzchtJzyVMLmvT0duhdrM0DKZCYrMuN-7_FV7bFblib7V4F0gZL_06zmsD57mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ced329bda.mp4?token=LXRr0zNHQ9TXGxajYGKRwTj1u3Bk-f7pEN4a25nflEGhdVN1soMMjJPfLO7QyXz-YPt5uve-vvOT5T-HPUCVoptyBBZkbbnd7AnyzMibEvUb0HJ-8VBtgCmtEPidkIGh83911yJ2KUtrIzRIpGbrTUQkV4Yxq2MA4S5Ne65bBBMwRjOY18glDdRrOKQ1t6sp_bzaR0iHVka4FzfkQLPfuyYJaQmm_17BwK5zKRvmeL9zt-blRrUeJeWZ0KT8ay8idmsoTGw0nfwXzae-COgFQQ6FRzchtJzyVMLmvT0duhdrM0DKZCYrMuN-7_FV7bFblib7V4F0gZL_06zmsD57mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های اسرائیلی با انتشار این ویدیو می‌گویند برخلاف تصور رایج، بخش زیادی از پرواز جنگنده‌های اسرائیلی بر فراز ایران نه پرتنش و پیچیده، بلکه شبیه یک پرواز عادی است. به ادعای آن‌ها، اطلاعات لحظه‌ای از موقعیت سامانه‌های پدافندی در اختیار خلبانان قرار می‌گیرد؛ تا جایی که این تصاویر از آسمان تهران، بیشتر به یک پرواز معمولی شباهت دارد تا مأموریتی در دل خاک دشمن
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20975" target="_blank">📅 21:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20974">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امشب تا صبح بیدارم
🙌🏾
روال هر هفته</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20974" target="_blank">📅 21:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20973">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سیریک گزارش صدای انفجار/پرتاب موشک/پهپاد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20973" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20972">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1310e64db.mp4?token=jvgOfBA7tn-yMb2c5RpE4vTq_UsCSXO4LYeMmslALiRUIfz4Tl3iDN_fRV7eiIieMqJ5I_hztbCr0wR2eEnInf_XO_PVkdnTmwXQYIC0lEAfo51uONLduq8B0bFE_Xj3kWeI4jQKbJ3womb0RwsVvVHLAqz7W3M15okNmcEPo9j68JUsC1FpXj3Pkzukcl_S-uoc5gz9ch1lNntV2zk2j-yrIgZMMeBuPD085MQwIw6dLU8ab8hVkavozuwcrqbGZKkthWjIr5M-hmFHW3Wgh5KdkpKTaNo32o1TD6x4jPRKba7fffIaF0SKRrbqfm21OD4thSN1vjLzhEFhyGVhLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1310e64db.mp4?token=jvgOfBA7tn-yMb2c5RpE4vTq_UsCSXO4LYeMmslALiRUIfz4Tl3iDN_fRV7eiIieMqJ5I_hztbCr0wR2eEnInf_XO_PVkdnTmwXQYIC0lEAfo51uONLduq8B0bFE_Xj3kWeI4jQKbJ3womb0RwsVvVHLAqz7W3M15okNmcEPo9j68JUsC1FpXj3Pkzukcl_S-uoc5gz9ch1lNntV2zk2j-yrIgZMMeBuPD085MQwIw6dLU8ab8hVkavozuwcrqbGZKkthWjIr5M-hmFHW3Wgh5KdkpKTaNo32o1TD6x4jPRKba7fffIaF0SKRrbqfm21OD4thSN1vjLzhEFhyGVhLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : این کشتی با یک کشتی یکسان (جرج واشنگتن) جایگزین میشود
خبرنگار: خانواده‌های نظامیان نگرانند از شرایط ناو لینکلن
ترامپ : «نه، آن‌ها نگران نیستند.»
خبرنگار: آیا این استقرار نظامی بیش از حد طولانی شده است؟
ترامپ: «نه، نه، نه؛ حتی نزدیک به آن هم نیست که بگوییم بیش از حد طولانی شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20972" target="_blank">📅 21:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20971">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfefd33ebd.mp4?token=SU7EUZ3N2LRHyuMQ6hTQpyAnJ2bkNjYg21QZ1UUzZdG8lh-omY1fOaYb8C9n8GkgUfkMrxpHfyznk2hwtd66yARadWwYRjv40gGJriUbJnFCmCpFyCGL2iqdT9Stqc3v8QpHyhWj22-CKnoMc6Yn2VHqV1gh4C12idYmhIeWxlIfIN8Sp7QpcU8V7V-U72ct6HK2tHETbCHk3pnsEc2R4t_Hr994DBbaPxX6ky5tG2nHtDiq8sz8jc9eXq4o9k_BnlBg620iYaI8_oEL13siHPgVJRiT383VPbB87FgsuDAigbhnzz2Y7sp_L8vmNnCxY4lahp0RL3TkIa7x9HFlhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfefd33ebd.mp4?token=SU7EUZ3N2LRHyuMQ6hTQpyAnJ2bkNjYg21QZ1UUzZdG8lh-omY1fOaYb8C9n8GkgUfkMrxpHfyznk2hwtd66yARadWwYRjv40gGJriUbJnFCmCpFyCGL2iqdT9Stqc3v8QpHyhWj22-CKnoMc6Yn2VHqV1gh4C12idYmhIeWxlIfIN8Sp7QpcU8V7V-U72ct6HK2tHETbCHk3pnsEc2R4t_Hr994DBbaPxX6ky5tG2nHtDiq8sz8jc9eXq4o9k_BnlBg620iYaI8_oEL13siHPgVJRiT383VPbB87FgsuDAigbhnzz2Y7sp_L8vmNnCxY4lahp0RL3TkIa7x9HFlhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم : دود مشاهده شده تو جنوب تهران مربوط به آتش زدن ضایعات پلاستیکیه ( عمو پلاستیکیاهو )
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20971" target="_blank">📅 21:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">داعش شروع به تهدید علیه اسپانیا کرد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20970" target="_blank">📅 20:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dd6977b1.mp4?token=hcrVpyDNdDLMbcs8crJOXBJWeGJdGCtK_osC3x02Gs7hzWCn9NLL1KDHnmlAf29rg4sZygvzlMxRqRRRrIRcRwm5R9igVfqgXcczmA9iVJQABoBc2YteWk5Ie6QqfWbZM48WZxpWdVKNyzge_eunqlpAIkvoNoWVvDKxEvYaJAKFBqkU9I-4YPe8orfj9Nb2cXEnyX_5J72jvg96thmrR-QjjscqdoeDWG4i875XUkepFekM1uIImmd_M_ZbThSRbcobzY-DK8XnIToBk7g4VsTNjZV0tbtf6yoeX4yaHPc5mU7bhbUw2J1Q_sobSOoObOx0qQ9S2NNX8_Jes7i3pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dd6977b1.mp4?token=hcrVpyDNdDLMbcs8crJOXBJWeGJdGCtK_osC3x02Gs7hzWCn9NLL1KDHnmlAf29rg4sZygvzlMxRqRRRrIRcRwm5R9igVfqgXcczmA9iVJQABoBc2YteWk5Ie6QqfWbZM48WZxpWdVKNyzge_eunqlpAIkvoNoWVvDKxEvYaJAKFBqkU9I-4YPe8orfj9Nb2cXEnyX_5J72jvg96thmrR-QjjscqdoeDWG4i875XUkepFekM1uIImmd_M_ZbThSRbcobzY-DK8XnIToBk7g4VsTNjZV0tbtf6yoeX4yaHPc5mU7bhbUw2J1Q_sobSOoObOx0qQ9S2NNX8_Jes7i3pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزمکس: وقتی یک دموکرات می‌گوید «ایران هیچ‌وقت قوی‌تر از این نبوده»، واکنش شما چیست؟
وزیر خزانه‌داری بسنت: آنها بی‌اطلاع، دیوانه و فاقد هرگونه درک از چیزی هستند که درباره آن صحبت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20969" target="_blank">📅 17:27 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

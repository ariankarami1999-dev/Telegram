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
<img src="https://cdn4.telesco.pe/file/FY4jGW5iipWAZgJWAhlJPdRrvHjPPbvD858TKvnr9P8BFTJczgAAXu8bbZG7c7YT8pN16ChsEnWY3OpI9tqmrZv-PGBGODVaqtREc0i1aUHuqSGPXqokRpBAoxoWi0oEeq4VmK4Bez-frwRoT2FsHNURNo_oMSO5JOTBlhc-grpXHRD76joFs9TsrCmgF6Se2gl3YkQ1qTgSzGsMDNdOpIsXpRGYesCG9eglFboQnmMTcKySrDodyR0dDYh1no7tTU2x4Rv9ztg1OrwFTpvanV4vDOa2krr_O3XhArhpawvuE3P5iDRPanH1cMoNDoWKyNcaLasIHGY-nJiZZgs1yw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 489K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 22:44:37</div>
<hr>

<div class="tg-post" id="msg-25048">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULK7NGggNU9WoidK4voLR-G4Y8qomOeu79ebxxoaTHZJxcgp7ITXdBeoTGnFXapbpEih37rrwFr5tX7k_mXT1Ra8Wc5KlDk_icv5cSQYwVfA3pWNILFfN2P7xlvOhdIng2SytWiuIqSZFyURKFtcvpJELJVb2wumpl87VgqctscKyRUY4oTRqf093LGBcDvXEj4_nR9dG8Zs08sowuD_JgePeviYdl5LPEXUfDnDjSIzV9aAy1nDy2NpBqYrO066Gh4L3wryf7D9QMYakG74mn7lB0Q3k9Ma0UR0jQH9QfKeTQwrYozzVp6oNiP9a9IVE6ZzM7vqaOJ0mboUiNnqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصل خبر فاکس‌نیوز:
دو شناور مهم نظامی آمریکا، از جمله ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش، موقتاً خاورمیانه را ترک کرده‌اند و برای توقف بندری به تایلند رفته‌اند. در حال حاضر یواس‌اس جورج واشنگتن تنها ناو هواپیمابر آمریکایی در خاورمیانه است. با این حال، بوش قرار است طی چند هفته آینده دوباره به خاورمیانه بازگردد. در مجموع حدود ۱۷ شناور نظامی آمریکایی همچنان در منطقه حضور دارند و سه ناوشکن موشک‌انداز نیز در دریای سرخ مستقر هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/withyashar/25048" target="_blank">📅 22:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : ناو بوش بر میگردد
فاکس نیوز»: ناو هواپیمابر «بوش» خاورمیانه را ترک می‌کند و تنها ناو هواپیمابر «جورج واشینگتن» در منطقه خواهد ماند.
این خبر کانال های زرد فیک نیوز است
@WarRoom</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/withyashar/25047" target="_blank">📅 22:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سیریک صدای انفجاررررر
@WarRoom</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/25046" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه : جنگنده‌های آمریکایی در چند روز گذشته چندین بار تا نزدیک مرزهای ایران آمدند مانور انجام دادند و برگشتند
@WarRoom</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/withyashar/25045" target="_blank">📅 22:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چند پرتاب موشک کروز ضد کشتی از قشم به سمت تنگه انجام شده @WarRoom</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/25044" target="_blank">📅 21:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e04b0950.mp4?token=JzP-YTqxbwQKrlr2YuGWhgAOs8QzFL5H029w1kL2lhWLg1m4FjEW-FGbjKvLWw7-2hqZUU9Dh10wMcNqpcxfTBIu1GLG10i5YUz8P2aohfq3xIACs59wIbJyeE83el6dRdk7NnhZOvZ89gn0oswrTdHgbQJIt7rJpBnaNTnT8AEFdUwEY7ddvmagyGusuLwMLqwYTQ3v3rsJBsyrVjYfVqMYwjyMdmYQuKxYUorQER-PY2IiI7I9jG7oI-3a9gK24uLu-MkOeqVqa0oIcedICzmjXX9LhmSNfUFkTdgcmOx47Q6gkgBr933c7WaDHCKbXg0lnsEC2ARuxZWXSXRfxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e04b0950.mp4?token=JzP-YTqxbwQKrlr2YuGWhgAOs8QzFL5H029w1kL2lhWLg1m4FjEW-FGbjKvLWw7-2hqZUU9Dh10wMcNqpcxfTBIu1GLG10i5YUz8P2aohfq3xIACs59wIbJyeE83el6dRdk7NnhZOvZ89gn0oswrTdHgbQJIt7rJpBnaNTnT8AEFdUwEY7ddvmagyGusuLwMLqwYTQ3v3rsJBsyrVjYfVqMYwjyMdmYQuKxYUorQER-PY2IiI7I9jG7oI-3a9gK24uLu-MkOeqVqa0oIcedICzmjXX9LhmSNfUFkTdgcmOx47Q6gkgBr933c7WaDHCKbXg0lnsEC2ARuxZWXSXRfxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: «کدام قسمت استیک را بیشتر دوست دارید؟»
ترامپ: «راستش من
همه قسمت‌های استیک را دوست دارم
؛ برخلاف تالافریکو در تگزاس (جیمز تالاریکو، نامزد دموکرات مجلس سنا) که وگان است و حالا یک‌دفعه استیک می‌خورد، ولی از آن هم راضی نیست!
این آدم کاهو دوست دارد، نه استیک!
»
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/25043" target="_blank">📅 21:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU63fqfgpN7AO1Fn68sAAjy4LIL1b0Vf79fXYn_iZuk0tx4tHobhS-rTt6d4YBzSV3wixZFotzAdmDCyPnW36B2HMiJbjwBNeZG4sZMZTzdCh0PjS3hz9z6q3y0UF8RXf5tsJnGH2hWQVw68rzAnRIFnrtmD3Eeq86H5tsAT_1iygteGU9ycix2_jck874qLE46UPMAVOJD_luB7MuzK1s3N216x2zCfwyPNcvPkCm3IRvPSLp-hfqkBaavP7yi-ePZiOBEsMIw6HsKrHAKSzH7NRaASt1EegAkOQRKgJmfXBJ8hcBHdJK_FKDdBRcLcg9w7iJzEzZ8moaoudlRLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پی۸ پوسایدون و ۵ سوخترسان هم‌اکنون در حال انجام مأموریت در منطقه هستند.تمرکز اکثر آنها بر روی تنگه هرمز میباشد. همچنین ترامپ دیشب گفته بود که موشکهایی که به سمت کشتی ها می‌آید، ما «بینگ بینگ» میزنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/25042" target="_blank">📅 21:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش های بسیار از صدای انفجار در قشم @WarRoom
🚨</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/25041" target="_blank">📅 21:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دادستان‌های بریتانیا سه ایرانی را به جاسوسی برای جمهوری اسلامی متهم کردند. مصطفی سپهوند ۴۱ ساله، فرهاد جوادی‌منش ۴۶ ساله و شاپور قلعه‌علی‌خانی نوری ۵۷ ساله متهم‌اند بین اوت ۲۰۲۴ تا مارس ۲۰۲۵ فعالیت‌های روزنامه‌نگاران ایران اینترنشنال را زیر نظر گرفته و برای…</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/25040" target="_blank">📅 21:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش های بسیار از صدای انفجار در قشم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/25039" target="_blank">📅 21:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرنگار کانال ۱۲ اسرائیل: نتانیاهو در هفته‌های پایانی انتخابات، به‌جای نظرسنجی کانال ۱۲ که
۵۳ کرسی برای بلوک او و ۵۴ کرسی برای مخالفان
نشان می‌دهد، ظاهراً روی کانال ۱۴ حساب کرده که
۶۳ کرسی برای بلوک نتانیاهو و ۴۵ کرسی برای مخالفان
پیش‌بینی کرده است. او دعوت گادی آیزنکوت برای مناظره را رد کرده و هم‌زمان کارزار علیه
اوفر وینتر، نامزد مستقل راست‌گرا
را تشدید کرده تا آرای راست پراکنده نشود. این رویکرد نشان می‌دهد لیکود تصور می‌کند برای تشکیل دولت به همه کرسی‌های جناح راست نیاز ندارد.
لیکود اکنون سه هفته پایانی را با این باور آغاز کرده که می‌تواند پیروز شود و حتی به اکثریت مطلق برسد
؛ هرچند این ارزیابی با بسیاری از نظرسنجی‌ها تفاوت دارد. نتیجه انتخابات برزیل نیز این اعتماد را تقویت کرده؛ جایی که بولسونارو
۲ تا ۳ درصد بهتر از نظرسنجی‌ها
عمل کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/25038" target="_blank">📅 20:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpIVC18fNBIYN7bGFHpBtC3e3xEntfajShFEuHHDa_XHEoinIHStQhpLb0rlMTa01JO2XnKQMjdYTSS7jv1IOuMkPGrWCmJ3mlyr_cZOWnNA4oi33BjKBRl32AQ2bfT8dTZyF5C0W_ZE4M3KlO6yU6zDDYTrNN_uAgfauGhjfb6Eguq7FWVJn-sypzNAmsUf3_ayMlEVn0wDkCfK2mZnoaOrXj4OYnizqmBULY6CYOsX6NgAJBkNskpgxi1thqZM1yHfF-QlrBGWVbGK4cGGPNb6pA7aeZTqtn9be_riUS1kKh5bGYbs-XzU8Y_ByMcN62Dg4HFbc9DLabhLjiNLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: آلارم جنگی در بالاترین سطح؛ ورود ناو سوم آمریکا و «کد ۱۰۰» سپاه!
حقیقت‌یاب اتاق جنگ
:
پخش
خبر فیک و فوتوشاپ شده ، توسط کانال های زرد از قول سنتکام
@WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/25037" target="_blank">📅 20:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فاکس نیوز :
شورش‌های گسترده در پاریس
؛ پرچم‌های فلسطین در خیابان‌ها به اهتزاز درآمده و نیروهای پلیس ضدشورش برای کنترل اوضاع با مشکل مواجه‌اند. گاز اشک‌آور نیز به کار گرفته شده است.
جنبش‌های مرتبط با حماس به‌طور فعال در شورش‌ها دخالت دارند
و معترضان در نقاط مختلف تحت تعقیب پلیس هستند.
بازداشت‌ها باید گسترده‌تر
شود «فرانسه در حال سقوط است.»
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/25036" target="_blank">📅 20:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25035">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رایتل ورشکسته شد !
شستا امروز آگهی مزایده
۱۰۰ درصد سهام رایتل
را منتشر کرد؛ قیمت پایه این واگذاری
۱۳۰ هزار میلیارد تومان (۱۳۰ همت)
تعیین شده و فروش به‌صورت
نقدی و یکجا
انجام می‌شود. مزایده قرار است
۲۳ مهر
برگزار شود. رایتل پیش‌تر نیز به‌دلیل مشکلات مالی و کاهش درآمد، اعلام کرده بود که در معرض ورشکستگی قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/25035" target="_blank">📅 19:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMjIOt2fD01tCKevlyrgB5aZs89KEr6k8HwItsqM1yPtKfrVYL5b5lYB_4KQJhEfBk06MQ4w8JavaZ1koQ8qAvncM-3Zbf4e8fK1OiHhyAfwgfbDe8bg-4le4x-in0S0rGTol5P0LN3I_-ES0UOrqEG4E7ZhOsNTDmdYsqo403aKp53_IcD2wiiPmEVi8-bKrS6Xh_x3FfYAKIPqb2yxVa-UUlcq0V6g7I_B8bcDDfIPXoDbaeo-edCSyfQz7o3Rq7YZ_JW8opGGPNRyXxPCa-_wfZR2Jf-O2bXVbGByTRTgfoTyusJjEn_hGpyMtSMRuV5izOsEatsBMDU0AZUShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌ : آنچه در فرانسه در حال رخ دادن است، چیزی کمتر از
مهاجرت گسترده و خارج از کنترل
نیست. این موضوع درباره مدارس نیست؛ موضوع این است که
اسلام می‌خواهد کنترل کشوری را که زمانی بزرگ بود، در دست بگیرد!
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/25034" target="_blank">📅 19:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ادعای مرگ دوم بر اثر طاعون در روسیه
؛ رسانه‌های محلی روسیه مدعی شده‌اند فرد دومی در منطقه ایرکوتسک بر اثر ابتلا به طاعون جان باخته است؛ ادعایی که هنوز از سوی مقام‌های روسیه یا سازمان جهانی بهداشت تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/25033" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184e92d2f2.mp4?token=gB5_cZNdVtC1OZ5dqomCx6FBNxoieMKWZuFmb59jGlss3otFWciyFVn-lwaDssvSyb2VH8iDXy1YyTG5RSRtgqyZfrMq1fuT2IUOe1wAmx6YkWsBViiSjw_NYLzj6amLrnnW32VX7a0LKexXywtVSiwThnB7cvmbIJrEPmpMt8NM8oXTWwairKqZySajYMfbwmCIksuVlXILjd8dXUpuuxhs5VeRyatVAz0ClMOo1h_SubQIR_2M-vSRDH2dVnrl3Ueuh3rmwfZf5uFknW5tnFIuAWM28ZOS9qu3HG-EHfPA6vAAreJME4P393C2laXjGTHqzeGI-Y2IDvMk2NhEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184e92d2f2.mp4?token=gB5_cZNdVtC1OZ5dqomCx6FBNxoieMKWZuFmb59jGlss3otFWciyFVn-lwaDssvSyb2VH8iDXy1YyTG5RSRtgqyZfrMq1fuT2IUOe1wAmx6YkWsBViiSjw_NYLzj6amLrnnW32VX7a0LKexXywtVSiwThnB7cvmbIJrEPmpMt8NM8oXTWwairKqZySajYMfbwmCIksuVlXILjd8dXUpuuxhs5VeRyatVAz0ClMOo1h_SubQIR_2M-vSRDH2dVnrl3Ueuh3rmwfZf5uFknW5tnFIuAWM28ZOS9qu3HG-EHfPA6vAAreJME4P393C2laXjGTHqzeGI-Y2IDvMk2NhEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امان از دست جاده های باب المندب. هر دو قدم، یه دست انداز گذاشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/25032" target="_blank">📅 18:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کاتز ، وزیر دفاع اسرائیل : ۴ هزار نفر از تروریست‌های حماس که ۷ اکتبر وارد اسرائیل شدن، کشته شدن و ۲ هزار نفر دیگه باقی موندن.
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/25031" target="_blank">📅 18:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانال ۱۴ اسرائیل: نیروهای امنیتی جمهوری اسلامی طی دو هفته گذشته به دست‌کم
پنج خانواده از معترضان کشته‌شده در اعتراضات ژانویه ۲۰۲۶
یورش برده‌اند. مأموران با ورود به خانه‌ها، وسایل شخصی قربانیان از جمله لباس، دفتر خاطرات، کتاب و حتی عروسک‌های دوران کودکی را ضبط کرده‌اند. به گفته خانواده‌ها، نیروهای امنیتی همچنین آنها را تهدید کرده‌اند که در صورت انتشار عکس یا ویدئو از فرزندانشان در شبکه‌های اجتماعی، وسایل بیشتری از اتاق‌های آنها برده خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/25030" target="_blank">📅 18:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25029">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مدیرعامل آرامکو : حتی اگر بحران جنگ علیه ایران همین الان پایان یابد، امکان دارد جهان برای پر کردن دوباره ذخایر نفتی که در طول جنگ مصرف شده‌اند، تا ۲ سال به حدود ۲ میلیون بشکه نفت بیشتر در روز نیاز داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/25029" target="_blank">📅 18:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏
کشتی حامل گاز طبیعی مایع "ال مافیار" متعلق به قطر، از طریق مسیر ایران وارد تنگه هرمز شد و در راه پاکستان قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/25028" target="_blank">📅 17:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مهم‌ترین رویدادهای پیش‌روی بیت‌کوین به وقت و تاریخ ایران در‌ این ماه میلادی : ۱۵ مهر، ساعت ۲۱:۳۰ — صورت‌جلسه فدرال رزرو؛
۲۲ مهر، ساعت ۱۶:۰۰ — تورم آمریکا (CPI)
؛
۶ آبان، ساعت ۲۱:۳۰ — تصمیم نرخ بهره فدرال رزرو
؛ ۶ آبان، ساعت ۲۲:۰۰ — سخنرانی جروم پاول؛ ۸ آبان، ساعت ۱۶:۰۰ — شاخص تورمی PCE آمریکا.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/25027" target="_blank">📅 17:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کوین‌دسک: بیت‌کوین امروز چند بار به محدوده
۸۷ هزار دلار
نزدیک شد اما برای سومین بار از ۲۳ سپتامبر در عبور پایدار از این سطح ناکام ماند و دوباره تا حوالی ۸۵۶۰۰ دلار عقب نشست. اتریوم نیز حوالی ۲۷۰۰ دلار معامله می‌شود. همزمان شاخص‌های سهام آمریکا در نزدیکی رکوردهای تاریخی قرار دارند و بازار کریپتو همچنان تحت تأثیر شرایط نقدینگی و نرخ بهره قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/25026" target="_blank">📅 17:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7d0da0527.mp4?token=jpMR2e-N1gcsLa-vAhvu0LBIEP2dodKigjIf-9SK67HtzWWjtrff2hDgGpSe8LY9ZEgIO0U75_LmFiRdE595_oBnNbV6Mwd-rXK6IZ2BuA2K20a0B5-j0sLptJ6SV3lItozjv44FjFaAM4PL1jlWIQOTcW2ivxkXtRmn1XoaZBZ2LyNVU_oEF5yTk5m1w9uIFrtT3iRaMxOvR3Dyt83SykF4mFu4GTJYjd5rr_nMw4029_XRno5F4UMPK8tYM8LMr49Zd_jYLp2MkAEcNFMMP57Lg5ob22pXl62ZIjmdAliHRQAAa4-vLQTRf0mFEOoqjPgze_mn2rCCYFG9xSQs6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7d0da0527.mp4?token=jpMR2e-N1gcsLa-vAhvu0LBIEP2dodKigjIf-9SK67HtzWWjtrff2hDgGpSe8LY9ZEgIO0U75_LmFiRdE595_oBnNbV6Mwd-rXK6IZ2BuA2K20a0B5-j0sLptJ6SV3lItozjv44FjFaAM4PL1jlWIQOTcW2ivxkXtRmn1XoaZBZ2LyNVU_oEF5yTk5m1w9uIFrtT3iRaMxOvR3Dyt83SykF4mFu4GTJYjd5rr_nMw4029_XRno5F4UMPK8tYM8LMr49Zd_jYLp2MkAEcNFMMP57Lg5ob22pXl62ZIjmdAliHRQAAa4-vLQTRf0mFEOoqjPgze_mn2rCCYFG9xSQs6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو از روسیه خواست اطلاعات بیشتری درباره مرگ کارمند مؤسسه تحقیقات ضدطاعون در سیبری منتشر کند.
روبیو گفت آمریکا این موضوع را «ساعت‌به‌ساعت» زیر نظر دارد و در صورت جدی‌تر شدن وضعیت، واشنگتن اقداماتی برای کمک به روسیه در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/25025" target="_blank">📅 17:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رویترز:
دست‌کم دو فلسطینی در حملات اسرائیل به غزه کشته شدند.
به گفته مقام‌های پزشکی، یکی در نزدیکی بیمارستان شفا در شهر غزه و دیگری در حمله‌ای جداگانه در همان منطقه کشته شده است. ارتش اسرائیل گفت این دو حمله، نیروهای مسلح تروریست را هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/25023" target="_blank">📅 17:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رویترز:
صادرات نفت کشورهای خلیج فارس، بدون احتساب ایران، در سپتامبر به بیش از ۸۱ درصد سطح پیش از جنگ رسید.
صادرات نفت خام و میعانات به حدود ۹۱ درصد سطح قبل از جنگ برگشته، اما صادرات فرآورده‌هایی مانند گازوئیل و سوخت جت تنها حدود ۶۰ درصد سطح پیش از جنگ است. صادرات نفت ایران نیز به دلیل محاصره آمریکا تقریباً به صفر رسیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/25022" target="_blank">📅 17:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX-7C4-JiBT9sDYCvXyn6KsGcNdC_qgQv5-37f8FwSfFR2k5EzS3gZ053bMe-WKGDt4ykscabJmfzyiUxuEvlYEPKuLrQL4-ukKIGAWsGh1R_7F6qKazLvHZdwfCyFy5d59rhfaMbby5TrXOYJv_cx4rLbP-g4vY7rXkPf_OyXgLaug07RKx2A97OFlb0nQtsm1KKH-73yOmC9rZeswW_zDP5-ztHiwPk0XP8_9Gw99IKMWYbZxwK3L7wI_X5A7go-66TsUtP50wvH4Rc9HR6TnQET6_vA8CmX-q6RLDKApREjozgrfbhOL118YX2RjzBbamJ0ptqKV9IGpEpdo75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت ایران روز فلج مغزی رو به ترامپ تبریک گفت
@WarRoom
البته باید به موشتبی این رو تبریک میگفت</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/25021" target="_blank">📅 16:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سفارت بریتانیا در ریاض برای شهروندان خود هشدار امنیتی داد
سفارت بریتانیا در عربستان سعودی با صدور اطلاعیه‌ای از اتباع خود در این کشور خواست با توجه به شرایط فعلی، ضمن حفظ هوشیاری کامل، پروتکل‌های ایمنی را رعایت کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/25020" target="_blank">📅 16:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پلیس بریتانیا یک مظنون دیگر را در پرونده پایگاه هوایی فیرفورد بازداشت کرد.
پلیس ضدتروریسم بریتانیا اعلام کرد یک
مرد ۲۲ ساله بریتانیایی
در وست‌مینستر لندن به ظن
آماده‌سازی برای انجام اقدامات تروریستی
در ارتباط با پرونده مرتبط با پایگاه هوایی
RAF Fairford
بازداشت شده است. در جریان این عملیات، یک ملک در وست‌مینستر نیز مورد بازرسی قرار گرفت. این فرد
هفتمین بازداشت
در این پرونده محسوب می‌شود؛ تحقیقات درباره طرح احتمالی مرتبط با پایگاه فیرفورد همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/25019" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25018">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlvRDhrc1gbhKReCaQb2qVLcI6HAXV4L-fKFW3P3BoZQiJxiEnfxzcyTpTZM9kxbGgTCgHk-w9ZeuIv4nStTdwLVnElYBw6pv_TQ8kw7WlbvXhicwwooR89oqiG0nml3M6zZgoPu1LgEmXldNHFKXetFS7230C0eSvyrv-XT4gZyXB8QKK1hswLftimMXWMabE8YN0la_KJyn3Hzm3t6-G8jAumRDsR9AvaNh2s_TChWEnBrOyF-8U-MJydqeeG0oMxhc4W7UP4m2bAqKndh6xNbpInkE3QZblrkQkqyyGmaGHLdq3aO18UjPS8xFdF9U8cyXUUpmavDDLopa6cGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب
سنتکام گزارش سقوط بالگرد آمریکایی در دریای سرخ را تکذیب کرد.
فرماندهی مرکزی آمریکا اعلام کرد گزارش‌های منتشرشده در
رسانه‌های دولتی ایران
درباره سقوط یک بالگرد
MH-60R نیروی دریایی آمریکا
پس از اعلام وضعیت اضطراری، صحت ندارد و
تمام هواگردها و نیروهای نظامی آمریکا در سراسر خاورمیانه سالم و در دسترس هستند.
این تکذیب پس از آن منتشر شد که بالگردی با همین مدل، دوشنبه شب هنگام پرواز در نزدیکی
ینبع عربستان
وضعیت اضطراری اعلام کرد و سپس از سامانه‌های ردیابی عمومی ناپدید شد. دلیل وضعیت اضطراری همچنان اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25018" target="_blank">📅 16:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25017">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دادستان‌های بریتانیا سه ایرانی را به جاسوسی برای جمهوری اسلامی متهم کردند.
مصطفی سپهوند ۴۱ ساله، فرهاد جوادی‌منش ۴۶ ساله و شاپور قلعه‌علی‌خانی نوری ۵۷ ساله
متهم‌اند بین
اوت ۲۰۲۴ تا مارس ۲۰۲۵
فعالیت‌های روزنامه‌نگاران ایران اینترنشنال را زیر نظر گرفته و برای
تدارک حمله خشونت‌آمیز
علیه دست‌کم دو روزنامه‌نگار، از آنها عکس و فیلم تهیه کرده‌اند. دادستان پرونده گفت هدف،
تلافی انتقاد از جمهوری اسلامی و ایجاد ارعاب
بوده است. هر سه نفر اتهامات را رد کرده‌اند؛ سپهوند مدعی است تحت فشار و تهدید عمل کرده و دو متهم دیگر می‌گویند از ارتباط اقداماتشان با سرویس اطلاعاتی ایران بی‌خبر بوده‌اند. دادگاه در
وولویچ کراون لندن
برگزار شده و رسیدگی به پرونده حدود
شش هفته
ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25017" target="_blank">📅 16:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25016">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhCm4Jj9UOM9GFRuYDl6X4twEd2wsSJFcOFKyLbDf7vQrpqwjuxm19VWjQzverOHcfNTkYCDp378tovY5mMJtSI-kYP5cbjsZTxWE74v67RxsPnh3Yg3sHRCL9jDMp-aUknhnHPpHExEeSkUFjSXrU3hoMNSWDo5Z3-N38vT4E60IF_IS5JkIAi3U73o9JzOC-9VH1d9GSyTMgK5NhPwUxtAUlgDhbM8lwpWiBFgbxAt6A0RQe3vNs0dwv6_WKyIpVT9DFP0Z_I8N7SHoUF6yuapLCu63-Q5rOdJeeTai2bQ6ZkXlYOMdqXvjOG_vzgqlZdzqJQiZvaCuj_S611Mrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب یک دستگاه آبگرمکن گازوئیلی از بهبهان خوزستان
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25016" target="_blank">📅 15:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d6cd9fcc.mp4?token=ddOPtvGjxHwWJnRuiPbzgyvg3eTmMSlpiTq1IOrklqAEH-DBWxAwKJllApQ4FGNUvUxDSVPXO6Jmmz7OgXUERUPBi71k0crjV1axa3u-7AOxDbogkGMeSEmypip6IWpGWUrKqTKPEy1IytkZ16gycWUa1vk-YEpbtjeB_gEGvRGRavLLKGMGprjhsaoiOPk-fui46TtGZePOzgjX8Md4PRGpAZCxQv1JOYkiMuq4Lsg1hbO2lvAkeedoC3EiV2WuPq1rk1nGjAmv5X9mAYoUMiJgv5UeigILEYoepPALf9RnNyu0ZTows5RjzXuWSPr407exM5BOVHvQt0wBrupXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d6cd9fcc.mp4?token=ddOPtvGjxHwWJnRuiPbzgyvg3eTmMSlpiTq1IOrklqAEH-DBWxAwKJllApQ4FGNUvUxDSVPXO6Jmmz7OgXUERUPBi71k0crjV1axa3u-7AOxDbogkGMeSEmypip6IWpGWUrKqTKPEy1IytkZ16gycWUa1vk-YEpbtjeB_gEGvRGRavLLKGMGprjhsaoiOPk-fui46TtGZePOzgjX8Md4PRGpAZCxQv1JOYkiMuq4Lsg1hbO2lvAkeedoC3EiV2WuPq1rk1nGjAmv5X9mAYoUMiJgv5UeigILEYoepPALf9RnNyu0ZTows5RjzXuWSPr407exM5BOVHvQt0wBrupXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۱۰۰ موتورسوار که از حضور مسلملنان و صدای مسجد در منطقه کلافه شده بودند در روبروی مسجد آنها و در حال عبادتشان گرد هم آمدند تا موسیقی گروه «ای‌سی/دی‌سی» را با صدای بلند برای آن‌ها پخش کنند!
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25015" target="_blank">📅 15:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی وزارت امور خارجه قطر : تماس ها و بازدیدها در تلاش برای پیشرفت در مذاکرات بین واشنگتن و تهران ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25014" target="_blank">📅 15:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز:
پالایشگاه‌های نفت چین، حجم خرید خود از نفت خام عراق را افزایش داده‌اند تا کمبود عرضه نفت ایران از طریق تنگه هرمز را جبران کنند. بر این اساس، حداقل ۱۲ میلیون بشکه نفت خام عراق و قطر خریداری شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25013" target="_blank">📅 15:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6a1530a7.mp4?token=UnU9oMqis7CdRKEs9xi5UbdCeWZJS9A7SMidVR9jJ2-e21fgpoyE74qTkFA_b0nDFbJ_oHmMpHv_aABWvb_U8jtFZD0qx1pVQLdxoiRMB_0h4Ao7116jUX64tvrJSsyFEMz_v1racWxb07-iFQBG5gGvFXYZHTmvtiPIVNeTgkTPzeCfuGH_wDa7-U0FlZF8oqGuHG17-sH_g6G3nZcKvdk6e9CtBAXNiQdC7zsSlBNHeMg_YInZS4mWe4qe1ftT0ueqn8kV05q7_S0yUNvqiFEPZSS7Sp9ypVanWFyDqgnje-ojHIKVqnHBnbRRh8pEyjIuz7ncNi_YrlRhAKXfHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6a1530a7.mp4?token=UnU9oMqis7CdRKEs9xi5UbdCeWZJS9A7SMidVR9jJ2-e21fgpoyE74qTkFA_b0nDFbJ_oHmMpHv_aABWvb_U8jtFZD0qx1pVQLdxoiRMB_0h4Ao7116jUX64tvrJSsyFEMz_v1racWxb07-iFQBG5gGvFXYZHTmvtiPIVNeTgkTPzeCfuGH_wDa7-U0FlZF8oqGuHG17-sH_g6G3nZcKvdk6e9CtBAXNiQdC7zsSlBNHeMg_YInZS4mWe4qe1ftT0ueqn8kV05q7_S0yUNvqiFEPZSS7Sp9ypVanWFyDqgnje-ojHIKVqnHBnbRRh8pEyjIuz7ncNi_YrlRhAKXfHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای خبرنگار وال‌ استریت‌‌ ژورنال: سرویس مخفی آمریکا CIA یک لیست از ۵ الی ۱٠ نفر مسئولان ایرانی را به اسرائیل داده که این افراد را نباید ترور کرد چون قصد دارند در آینده، حکومت را به دست بگیرند تا ایران کشوری نرمال شود!!️
@WarRoom
یاشار: این ادعا فقط در همین ویدیو بیان شده و در وال استریت ژورنال یا رسانه دیگری منتشر نشده است</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25012" target="_blank">📅 14:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">منابع هندی اعلام کردند یک
کشتی تجاری با پرچم پاناما
امروز،
۶ اکتبر, ۱۴ مهر
هنگام عبور از نزدیکی تنگه هرمز و سواحل عمان هدف یک
پرتابه ناشناس
قرار گرفته و
۱۱ خدمه هندی زخمی شده‌اند
. تاکنون هویت عامل حمله به‌طور رسمی اعلام نشده ولی این حمله به سپاه نسبت داده میشود.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25011" target="_blank">📅 14:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عملیات کاگ‌ب برای ایجاد اختلاف میان شاه و آمریکا:
بر اساس اسناد
آرشیو میتروخین
و
اسناد رسمی وزارت خارجه آمریکا (FRUS)
، بخش «سرویس A» کاگ‌ب که مسئول عملیات فریب و اطلاعات نادرست بود،
نامه‌ای جعلی به نام جان فاستر دالس، وزیر خارجه آمریکا، خطاب به سفیر آمریکا در تهران جعل کرد
؛ نامه به‌گونه‌ای تنظیم شده بود که توانایی شاه را تحقیرآمیز جلوه دهد و این تصور را ایجاد کند که
آمریکا در حال بررسی کنار گذاشتن یا سرنگونی شاه است
. کاگ‌ب نامه را مستقیماً به شاه نداد؛ مأموران شوروی
نسخه‌هایی از آن را میان نمایندگان بانفوذ مجلس و سردبیران مطبوعات ایران پخش کردند
تا نامه از طریق محافل سیاسی به شاه برسد؛ طبق پرونده کاگ‌ب، این نقشه موفق شد و
شاه نامه را واقعی تصور کرد و دستور داد نسخه‌ای از آن برای سفارت آمریکا ارسال و درباره آن توضیح خواسته شود
. سفارت آمریکا اعلام کرد نامه جعلی است، اما طبق گزارش کاگ‌ب،
تکذیب آمریکا نیز در میان برخی محافل ایرانی و حتی شاه باور نشد
و محتوای تحقیرآمیز منتسب به دالس به موضوع گفت‌وگوهای پنهانی در میان نخبگان ایران تبدیل شد.
هدف اصلی عملیات، ضربه زدن به اعتماد شاه به آمریکا و تشدید شکاف میان تهران و واشنگتن بود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25010" target="_blank">📅 14:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تلاش شنیده نشده نافرجام کاگ‌ب برای ترور شاه در تهران:
بر اساس اطلاعات
آرشیو میتروخین
، یک مأمور مخفی کاگ‌ب یک
فولکس‌واگن بیتل مملو از مواد منفجره
را در مسیر حرکت محمدرضا شاه به سمت
مجلس شورای ملی
پارک کرد. طبق روایت منتشرشده، این عملیات به دستور کاگ‌ب و با تأیید
نیکیتا خروشچف
انجام شده بود. هنگامی که کاروان شاه از کنار خودرو عبور کرد، مأمور کاگ‌ب با
کنترل از راه دور
اقدام به انفجار بمب کرد، اما
چاشنی عمل نکرد و انفجار رخ نداد
؛ در نتیجه شاه از این سوءقصد جان سالم به در برد. این گزارش در کتاب
«آرشیو میتروخین ۲: کاگ‌ب و جهان»
نوشته کریستوفر اندرو و واسیلی میتروخین آمده است. آرشیو میتروخین شامل یادداشت‌ها و رونوشت‌هایی است که یک آرشیویست ارشد کاگ‌ب از پرونده‌های محرمانه این سازمان تهیه کرده بود و اکنون در
مرکز آرشیو چرچیل دانشگاه کمبریج
نگهداری می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25009" target="_blank">📅 14:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اتاق جنگ با یاشار | حقیقت‌یاب: ماجرای موسوم به «طاعون روسی» پس از مرگ یک پژوهشگر ۲۸ ساله در مؤسسه تحقیقات ضدطاعون در ایرکوتسک روسیه مطرح شد؛ اما آزمایش‌های رسمی تاکنون ابتلای او به طاعون را تأیید نکرده‌اند و علت مرگ، ذات‌الریه با منشأ نامشخص اعلام شده است.…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25008" target="_blank">📅 13:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WciHhsDC8Z3NIM-cJfaT6ptQ-vghfUDo3APkGKdw3L4dYxH5Yw-BCHcUh5e28OP6DXN--ZFf09TI1PtBhuuPv3ROtEssdvlaWpQLlAtz8ouitr0WOXX3USoiPXs5yKI3D-UN-zli39wQkNzlY7Ffnox5FmThDe7PMvPHfoIk5YZ8LTz1lDoFWM2gYJbe8QOoqJESn0yibvld9Jh1wOYJww5bm-bGoAf3JNvBMfZbWTAXhwNMKX-zqBKlWuDNCkrz_qSfiWMXcVrP82U6O5jm2DFPR74vojvqdaC8RqpZSFRot247zw6OpJON4SCpT2AKML5GmzVI4FLO3tnR5TYfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران اعلام کرد در واکنش به اقدامات آمریکا علیه نفتکش‌ها و شناورهای ایرانی، نیروی هوافضای سپاه با موشک‌های بالستیک به دو ناوشکن آمریکایی  DDG119 - USS Delbert D. Black و  DDG53 - USS John Paul Jones  حمله کرده است. سپاه مدعی شده این دو ناوشکن که به…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25007" target="_blank">📅 13:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230bdf5772.mp4?token=G6B9esnM1IVQocNDTKTyJ0DfMDD_Fot97wGZ5Cwsd-uy7dg7Jup9KDlClOxcDXUDFrspRPg6B1DsxWTCHHe4VneSRVXjV6toEpaY9qxtEqgiqS-OmS6hvCVb_NbTha4NP25p2VrfQXHpO81yjVJloj2p2DV8rFQgUnekLoA37IYj8OzfrlelfRhOlVwBHEG1nEPZqdWZFdCGC0_13qCocDYc1zAQSVfwDwAMkhV7ItC-dHU0wcwjJFm6YTPiEotXqjYMxeTB-k8S4ae9AjuNscmHiBXY0g0fXqSqcwBj4I4vhuwtNQlq01LXcHyqVEbg6LEkg0_nvVCcyb9njI3CzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230bdf5772.mp4?token=G6B9esnM1IVQocNDTKTyJ0DfMDD_Fot97wGZ5Cwsd-uy7dg7Jup9KDlClOxcDXUDFrspRPg6B1DsxWTCHHe4VneSRVXjV6toEpaY9qxtEqgiqS-OmS6hvCVb_NbTha4NP25p2VrfQXHpO81yjVJloj2p2DV8rFQgUnekLoA37IYj8OzfrlelfRhOlVwBHEG1nEPZqdWZFdCGC0_13qCocDYc1zAQSVfwDwAMkhV7ItC-dHU0wcwjJFm6YTPiEotXqjYMxeTB-k8S4ae9AjuNscmHiBXY0g0fXqSqcwBj4I4vhuwtNQlq01LXcHyqVEbg6LEkg0_nvVCcyb9njI3CzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو: «معجزه‌ای که امروز جهان شاهد آن است این است که حتی بعضی از کسانی که ما را محکوم می‌کنند، در دل خود می‌گویند: «وای، ادامه بدهید، ادامه بدهید!» چون خودشان چنین قدرتی ندارند.»
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25006" target="_blank">📅 12:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d6a47346f.mp4?token=BA7gok026wLXJTldqznB_9tQ69e_dMdMq7sb-J05VstWosYHIYf7YAKAuzBF261MHGWsVRKBb-6xcsBWQh5F0E0N23UnK0vKa96pI0kpl8JHtyOXT6-Lxwj3AdSmhfg9zn0H0iBIbbvKwy99xeF4m-lmGlNh4htz1Q0JL7VDvx-y52YgqUtEoGIYQqTNCOrmq3nns8jc_lZgZJZ47LPsaSXrIECCM-iKhiTmhHXnn7CZrlRmm2AgMfyBKjchEC8k2ykScsw8RyW4PR08n9g9A5aCjZ-DJFNjKgZno29XIwnBsmeYJ16Su288tTAaEQP2HDENS2yC9af7MZsIsBjf4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d6a47346f.mp4?token=BA7gok026wLXJTldqznB_9tQ69e_dMdMq7sb-J05VstWosYHIYf7YAKAuzBF261MHGWsVRKBb-6xcsBWQh5F0E0N23UnK0vKa96pI0kpl8JHtyOXT6-Lxwj3AdSmhfg9zn0H0iBIbbvKwy99xeF4m-lmGlNh4htz1Q0JL7VDvx-y52YgqUtEoGIYQqTNCOrmq3nns8jc_lZgZJZ47LPsaSXrIECCM-iKhiTmhHXnn7CZrlRmm2AgMfyBKjchEC8k2ykScsw8RyW4PR08n9g9A5aCjZ-DJFNjKgZno29XIwnBsmeYJ16Su288tTAaEQP2HDENS2yC9af7MZsIsBjf4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو: «در دنیای غرب امروز، در جوامع دموکراتیک، آنها هم انتخاب دیگری ندارند؛ اما نمی‌جنگند. ما هم انتخاب دیگری نداریم، اما
می‌جنگیم
.»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25005" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نتانیاهو در اکس: «ما ایران را عقب راندیم؛ مأموریت را هم به پایان خواهیم رساند.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25004" target="_blank">📅 12:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">استیضاح عراقچی در سامانه مجلس ثبت شد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25003" target="_blank">📅 12:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزیر کشور رژیم جمهوری اسلامی , اسکندر مؤمنی برای شرکت در مذاکراتی وارد دوحه قطر شد هم زمان ۶ سوخترسان و جنگنده های آمریکای با تمرکز بر تنگه هرمز در حال اسکورت کشتی ها از مسیر جنوبی تنگه هستند @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25002" target="_blank">📅 12:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شبکه ۱۲ اسرائیل : همام الهمامی، کمک‌خلبان عمانی در بازجویی جدید گفته است او قصد داشت هواپیما را طبق روال عادی برای فرود هدایت کند و در ثانیه‌های پایانی، زمانی که دیگر امکان رهگیری وجود نداشته باشد، هواپیما را به ساختمان ترمینال فرودگاه بنگوریون بکوبد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25001" target="_blank">📅 11:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8573ef2225.mp4?token=ci7pkuW1uKlMwfYE70QPlE317VpXXI_FokqmNz03lb2IkSG7SqLrhNYZGU9NyWwvBjWf28iYfIxzgsdQjSr6nCPG34nxUMqar_TUijSSJ77kSL-fB4AgFAohEpHsPFtbVFe62DcZ0u4cWPMX3xETZclkfAxwD9-1T7F6K1dIHA_NhrsEiHtTVlzex1dbokXl6RTsLmFjdoHfdJxt0JZpImqYqeLnWkVSHIw6G3YvdB9yOqoczYFGl0AcAbtD_FAqxXVLZ-1N0pBCZQJEc5NE4NDS2LIWnfeEd__ha9DNi3T6jEDAvkJni7GVpOPpLaVaL2nct7ffoflJDMA1Ut4SiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8573ef2225.mp4?token=ci7pkuW1uKlMwfYE70QPlE317VpXXI_FokqmNz03lb2IkSG7SqLrhNYZGU9NyWwvBjWf28iYfIxzgsdQjSr6nCPG34nxUMqar_TUijSSJ77kSL-fB4AgFAohEpHsPFtbVFe62DcZ0u4cWPMX3xETZclkfAxwD9-1T7F6K1dIHA_NhrsEiHtTVlzex1dbokXl6RTsLmFjdoHfdJxt0JZpImqYqeLnWkVSHIw6G3YvdB9yOqoczYFGl0AcAbtD_FAqxXVLZ-1N0pBCZQJEc5NE4NDS2LIWnfeEd__ha9DNi3T6jEDAvkJni7GVpOPpLaVaL2nct7ffoflJDMA1Ut4SiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سخنگوی ارتش اسرائیل: یک تونل به طول یک‌ونیم کیلومتر را در شمال نوار غزه منهدم کردیم. عملیات برای نابودی زیرساخت‌های زیرزمینی در این منطقه ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25000" target="_blank">📅 11:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24999">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏اداره فدرال حفاظت از قانون اساسی آلمان : تلاش جمهوری اسلامی برای دستیابی به فناوری آلمانی مورد استفاده در ساخت موشک و سامانه‌های پرتاب افزایش یافته است. حکومت ایران برای بازسازی زرادخانه و تاسیسات آسیب‌دیده خود به دنبال فناوری‌های غربی است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24999" target="_blank">📅 11:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELzRnhDUuZii83NnHNfpNfu5Ewtr_HgQnuOJCoJhqcufG6XTw46mdlsiAwKiTekDcebnCkeTPqyhyp5SdF0egfYHMldVyAyr89PH4k32KXbXAq-G_Gxsiq4R0gfKVB48q4eD2-zXIj1VOCWSf3WVxjbQd_d4UMQwH73_v59T29EKNtxHeVqTvxFp2gTx3w4uYFa8FvHo58bj-Iz1WvciAkOf4YR1wattXcXj6sDhtdSavuvwdSyJTEKphXt6_29TElUngSFmjxnI0rc_AJnSsSJBuyxlISWzxvKzr6iE-YLNcYDJ5ek_BO9A9BD_pu3u7_eesB5k7oAX6YzD7Qv4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت آموزش و پرورش ترکیه تو جلد کتاب درسی جدید خودش، تمام مناطق شمالی و شمال‌غربی ایران رو، جزو نقشه‌ی "دنیای ترک" قرار داده.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24998" target="_blank">📅 11:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بلومبرگ: دست‌کم
۵۰ نفتکش حامل نفت ایران
همچنان در نزدیکی سواحل ایران متوقف مانده‌اند و تعدادی نفتکش خالی نیز در نقاط مختلف اقیانوس هند و اطراف سریلانکا منتظر هستند و به سمت بنادر ایران حرکت نمی‌کنند. دست‌کم ۱۱ نفتکش حامل محموله در شرق جزیره خارک لنگر انداخته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24997" target="_blank">📅 11:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24996" target="_blank">📅 05:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24995" target="_blank">📅 05:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3258eb63.mp4?token=rEsQcknV2u-6UOToqNCKUWdPayi697b2zynHyjbI6Ta0blblRmguLP7RCwUSwtZuDuk0lptss3qLz_9mlE04rO6kIk6ACIjw8XdMky1Y2zk8gib-_ZQgmvhQLnZqaeRLY2eQVMDdMdKwdHYvOXeUb7r6r-XCzhkH8k2KQ2epW9prBCbklVvuzJjIYBSUqx2g69n88Sn48Hiw4ttPCmJGDMn6uwewV-MR66sLtdV04tLuR7xq5Q7NF4wAo1W7bPWylY0asj_hb-V4OycCMuNWdb7Um-DrOB45EZbTFhYHhw9JgnlY16oq_qRaOAwTUsfLUfFzMtL_5jIprpj_LXx3gK4pTa0mjz9NZ8uTC2HKk8t9OvxG-aOHgmmQAKt71TlwuHnrnvaL09aA-1PQAWUba3kppkzXA8Sm5N2HVx_WW0OhhWmjWzmpD3VHRJsOiPvQ5qDdJc7MheLDn83Ru9NDd0WM9MYR_aEa2o0wIlDDDuWoA11E37dQlW5YKCepg-Qsh6Hoe6RDTIhjOJqACIYcHAavWyD3gYJzeMW2rkifal1nffIug-cc3cFZNsi9zpPljvLEGXgHOXKyRsba_A8JXiMDBIk-mPVOnj3hTqZinKGxOaS5pzDG9IgKxjNq0KEXXrXxSqhl4xo3Js0eM2itbUltDFWFWVX_PArttluSPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3258eb63.mp4?token=rEsQcknV2u-6UOToqNCKUWdPayi697b2zynHyjbI6Ta0blblRmguLP7RCwUSwtZuDuk0lptss3qLz_9mlE04rO6kIk6ACIjw8XdMky1Y2zk8gib-_ZQgmvhQLnZqaeRLY2eQVMDdMdKwdHYvOXeUb7r6r-XCzhkH8k2KQ2epW9prBCbklVvuzJjIYBSUqx2g69n88Sn48Hiw4ttPCmJGDMn6uwewV-MR66sLtdV04tLuR7xq5Q7NF4wAo1W7bPWylY0asj_hb-V4OycCMuNWdb7Um-DrOB45EZbTFhYHhw9JgnlY16oq_qRaOAwTUsfLUfFzMtL_5jIprpj_LXx3gK4pTa0mjz9NZ8uTC2HKk8t9OvxG-aOHgmmQAKt71TlwuHnrnvaL09aA-1PQAWUba3kppkzXA8Sm5N2HVx_WW0OhhWmjWzmpD3VHRJsOiPvQ5qDdJc7MheLDn83Ru9NDd0WM9MYR_aEa2o0wIlDDDuWoA11E37dQlW5YKCepg-Qsh6Hoe6RDTIhjOJqACIYcHAavWyD3gYJzeMW2rkifal1nffIug-cc3cFZNsi9zpPljvLEGXgHOXKyRsba_A8JXiMDBIk-mPVOnj3hTqZinKGxOaS5pzDG9IgKxjNq0KEXXrXxSqhl4xo3Js0eM2itbUltDFWFWVX_PArttluSPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رقص و قر تمام کننده ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24994" target="_blank">📅 05:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ca302cfb.mp4?token=HiL3R3MwCekSOWIQjRz2jrhWUejMfGsl5Q1QAZ9bVN8BIhiupEpa3TWGNF4FGD8GVAyKMeVmUMEd1kq9PbxTuSWm16sDNV4Mo2OCot6MT4VwYR0jfM2nIEiL43odsaoV7-RgxRNYfvw_UYi_rVEhFx9FIYsHGTlFnFa3jIgtzp5c1Mv1kZY49yIeA-J_g9ZY7KkCNMkYaN_1PPBKww8xjfI2yBH3AhnNtD9qOMRQ25U1dpCIXmU3c7Sb1LNgrJHhS-5YDLQbEDoTtp2SRnhvISwzwTxLb2dalVqz8jzFN6yH9TG5pVwSOaujOZwGJXY1fdJ8PbrFSS3AUYQlG1jNFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ca302cfb.mp4?token=HiL3R3MwCekSOWIQjRz2jrhWUejMfGsl5Q1QAZ9bVN8BIhiupEpa3TWGNF4FGD8GVAyKMeVmUMEd1kq9PbxTuSWm16sDNV4Mo2OCot6MT4VwYR0jfM2nIEiL43odsaoV7-RgxRNYfvw_UYi_rVEhFx9FIYsHGTlFnFa3jIgtzp5c1Mv1kZY49yIeA-J_g9ZY7KkCNMkYaN_1PPBKww8xjfI2yBH3AhnNtD9qOMRQ25U1dpCIXmU3c7Sb1LNgrJHhS-5YDLQbEDoTtp2SRnhvISwzwTxLb2dalVqz8jzFN6yH9TG5pVwSOaujOZwGJXY1fdJ8PbrFSS3AUYQlG1jNFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: «فقط یادتان باشد، من دارم می‌دوم، باشه؟حقیقتأ به تمام معنا، واقعاً دارم می‌دوم.»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24993" target="_blank">📅 05:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24992">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571e103bc9.mp4?token=eP98RMvkox8Uv4G9UeMjJ9_Yai2jfidwQOPlTKM0pNMzl0y5___T5nPwSmGQpsjbULw_aQuwDsI7coIsUssJaCDKgvX5EmuXkhu8g727qgoNKi6JLm0xgPpWq22LXFdoWGSWPoTjp-j48jUoq3a066XDbpoQ3Hlz0rDXeIpKAMaFuNH4j6JK90b7ZqKeYUqLicFjbFVTsm9kg6abfwEGLl_nuZ5GmmwGQp6lRY6kVgSRKuRn4bVFIeST9uFN_NYfSvyfGnpZe4OMRrqrJzGtShf21n3AUDd5SMjFpd9zQUL3Ci6klB2OzjPrOEu9tOvl1TUMTTOfjUqSkWXgyogdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571e103bc9.mp4?token=eP98RMvkox8Uv4G9UeMjJ9_Yai2jfidwQOPlTKM0pNMzl0y5___T5nPwSmGQpsjbULw_aQuwDsI7coIsUssJaCDKgvX5EmuXkhu8g727qgoNKi6JLm0xgPpWq22LXFdoWGSWPoTjp-j48jUoq3a066XDbpoQ3Hlz0rDXeIpKAMaFuNH4j6JK90b7ZqKeYUqLicFjbFVTsm9kg6abfwEGLl_nuZ5GmmwGQp6lRY6kVgSRKuRn4bVFIeST9uFN_NYfSvyfGnpZe4OMRrqrJzGtShf21n3AUDd5SMjFpd9zQUL3Ci6klB2OzjPrOEu9tOvl1TUMTTOfjUqSkWXgyogdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره احتمال حمله هسته‌ای ایران به یک شهر آمریکا: «میخواهید بگذارید این کار را بکنند؛ بگذارید لس‌آنجلس را از بین ببرند، بگذارید سن‌دیگو را از بین ببرند؟؛
این
گرانی بهای بسیار کوچکی است که باید پرداخت شود.
»
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24992" target="_blank">📅 05:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش چند صدای انفجار بندر عباس ۱۰ دقیقه پیش
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24991" target="_blank">📅 05:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871cf2b90c.mp4?token=Uk0jHyayiM4Q69HkvmshgA9bPTonsF2lciugfiY4Fxquq4Ln5ntz8lOPr7j2KPsHKl_ZR35t6KPu4_GtRd5uH-quX0kO7abLNlPDw1EydunH-_HZUtB4V5bkEOZc3YZ6gGux_DV2rKY_7K-fI-9QufqdzdMCe8mcggYwJqZCm_kuYhHcU5A1dpjVPjIX1VWgG_Z8nvGJR5CdFlsg0rzCWlT2F19BolLxyWZQT0y7uIQuKi-C0i8Dsm7DKUNFZx9_4VTQzvhKnnBzRVfjR4C_M9svQgAWzVyut6MLvSq77wpXZpq9AVauJMI8S2tSifFxE7WiHhXMJXDX3heasQmnPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871cf2b90c.mp4?token=Uk0jHyayiM4Q69HkvmshgA9bPTonsF2lciugfiY4Fxquq4Ln5ntz8lOPr7j2KPsHKl_ZR35t6KPu4_GtRd5uH-quX0kO7abLNlPDw1EydunH-_HZUtB4V5bkEOZc3YZ6gGux_DV2rKY_7K-fI-9QufqdzdMCe8mcggYwJqZCm_kuYhHcU5A1dpjVPjIX1VWgG_Z8nvGJR5CdFlsg0rzCWlT2F19BolLxyWZQT0y7uIQuKi-C0i8Dsm7DKUNFZx9_4VTQzvhKnnBzRVfjR4C_M9svQgAWzVyut6MLvSq77wpXZpq9AVauJMI8S2tSifFxE7WiHhXMJXDX3heasQmnPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره عبور کشتی‌های آمریکا از تنگه هرمز: «کار نیرودریای ما حرف نداره ، نفت از قبل هم بیشتر از تنگه عبور میکنه ، هر از گاهی آنها یک موشک کوچک شلیک می‌کنند. ما هم می‌گوییم «بینگ» و موشک را می‌زنیم و نابودش می‌کنیم. به شما می‌گویم، خیلی خفن است! موشک می‌آید، موشک می‌آید، موشک دیگر نیست. تمام. و کشتی‌ها هم به حرکت خودشان ادامه می‌دهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24990" target="_blank">📅 05:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دونالد ترامپ: «آنها شیاد هستند. دروغ می‌گویند. ما کاری جز پایین آوردن قیمت‌ها انجام نداده‌ایم و وقتی جنگ با ایران تمام شود، که خیلی زود خواهد بود، قیمت نفت به‌شدت سقوط خواهد کرد.آنها نمی‌توانند سلاح هسته‌ای داشته باشند، چون دیوانه‌اند. این کاری بود که رئیس‌جمهورهای دیگر یا کشورهای دیگر باید سال‌ها پیش انجام می‌دادند. ما همیشه مجبوریم کارهای سخت و کثیف را انجام دهیم، در حالی که این کار باید سال‌ها پیش انجام می‌شد. این وضعیت ۵۱ سال ادامه داشته است؛ زورگوی خاورمیانه دیگر چیزی ندارند همه چیزشان نابود شده است و تنها چیزی که دارد ، تورم ۳۱۰ درصدی است، کار را زود تمام میکنم احتمالا بعد از انتخابات میان دوره‌ای
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24989" target="_blank">📅 04:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b95796cd.mp4?token=iZAu2PHBN0YgfOBgkgkJQ_4MRFLcTKh0U0RKz56dsw5HB9YYudscMl-ovCCgDeRDkP9-NWvume1VuGiBUZFzEJhGptuKKKRLSXRiA0ra6qnt1z8t5jiboFdTTfzUxc1wGbFNdetI1zKQN_BRcpWCM52AZO_qg3ipSRLRgZ-sFUShKSqy7BRGlcasZ6ePdQ9WitlYH6_9cgcqs59GpomG63USSQMej7-AiWZ6OyRgJV3_q7jpNTEAdTnfUAlxmzAtKEVcSAhubI5K1G6R0gQoFSUnbKjzG9yRqPkzF1X6lUKUshBXVSVWu-MFtfwc2xtmAzZGhb5qBopnfRoTGxAgO4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b95796cd.mp4?token=iZAu2PHBN0YgfOBgkgkJQ_4MRFLcTKh0U0RKz56dsw5HB9YYudscMl-ovCCgDeRDkP9-NWvume1VuGiBUZFzEJhGptuKKKRLSXRiA0ra6qnt1z8t5jiboFdTTfzUxc1wGbFNdetI1zKQN_BRcpWCM52AZO_qg3ipSRLRgZ-sFUShKSqy7BRGlcasZ6ePdQ9WitlYH6_9cgcqs59GpomG63USSQMej7-AiWZ6OyRgJV3_q7jpNTEAdTnfUAlxmzAtKEVcSAhubI5K1G6R0gQoFSUnbKjzG9yRqPkzF1X6lUKUshBXVSVWu-MFtfwc2xtmAzZGhb5qBopnfRoTGxAgO4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: راستی، ما داریم به ایران در کونی میزنیم ، اینو که می‌دونید، مگه نه؟
این ماجرا، به هر شکلی، به پایان خواهد رسید. خیلی زود تمام می‌شود و قیمت‌هایتان به‌شدت پایین خواهد آمد
ما خاورمیانه ، اسرائیل و جهان را نجات میدهیم, آنها هیچوقت سلاح هسته‌ای نخواهند داشت
@WarRoon</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24988" target="_blank">📅 04:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پزشکیان گزینه جدید وزارت دفاع را معرفی کرد.
مسعود پزشکیان،
مهرداد اخلاقی کتابچی
، از مدیران باسابقه صنایع موشکی و هوافضای وزارت دفاع را برای تصدی وزارت دفاع به مجلس معرفی کرد. او سابقه ریاست سازمان صنایع هوافضای وزارت دفاع و گروه صنعتی شهید باقری را دارد و نامش در فهرست تحریم‌های مرتبط با برنامه موشکی ایران نیز بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24987" target="_blank">📅 01:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فرمانده سنتکام، دریاسالار برد کوپر: «ارتش آمریکا همچنان با تمرکز کامل بر این مأموریت فعالیت می‌کند و علیه هر کشتی که تلاش کند محاصره را دور بزند،
سریعاً اقدام خواهد کرد.
نیروهای ما آموزش‌دیده، حرفه‌ای و مرگبار هستند.» به تمامی دریانوردان توصیه شده هنگام تردد در
دریای عمان و مسیرهای منتهی به تنگه هرمز
، اطلاعیه‌های دریایی را پیگیری کنند و در صورت نیاز از طریق کانال ۱۶ ارتباط «کشتی به کشتی» با نیروهای دریایی آمریکا تماس بگیرند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24986" target="_blank">📅 00:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ab1YilLXs7YZQL7ucz-TiimhtKGB2o3Zye64w5sUJoF1LkVgHlv3i_iB2Mc5xTsQrkoD2ZpxVfQ3sDV5pQPCLUdiIQfZ7gJKpKzKyTqk6yewT-Y5H_ky1XWQt7D-ogMwvdB6ulcxiWvCF0d0DHH7BeseqzD4RAzJuVd6VV2bF069tTugSqhhLX4cpyFZaNgM5lVmVjTSonAFY4LLuPq8Q1-j3BOecsS-lH3gj394Y_cwM_YTxMgHwybUuAXPQme7j9_3HRsNr4Qi2ruVgTlvpK7YOrgePWCLAgbuVbU_JQmke-kRkWkFNvG49QAs1KkwU8-8GP3jZowuscIiW9Q6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی روز دوشنبه
صدوسی‌امین کشتی تجاری
را که قصد ورود یا خروج از بنادر ایران داشت، در چارچوب محاصره دریایی ایران، وادار به تغییر مسیر کردند. از زمان ازسرگیری محاصره در
۲۳ تیرماه
، نیروهای آمریکایی مدعی‌اند
۱۳۰ کشتی
را تغییر مسیر داده و
۳ کشتی
را که حاضر به تبعیت نبوده‌اند، از کار انداخته‌اند. همچنین به بیش از
۷۰ کشتی بشردوستانه
اجازه عبور داده شده است. سنتکام همچنین مدعی است طی ۱۲ هفته گذشته،
۱۳ کشتی تجاری
را که متهم به نقض محاصره یا فعالیت در شبکه چند میلیارد دلاری سایه سپاه پاسداران بوده‌اند، منهدم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24985" target="_blank">📅 00:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کانال 14 اسرائیل
: لحظاتی پیش نتانیاهو با روبیو، وزیر خارجه آمریکا یک تماس تلفنی اضطراری و ویژه برقرار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24984" target="_blank">📅 00:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54e4b572e.mp4?token=doD1UYCsOY2GAq6AdDDuUc9-oWP2nGgQYZBApnnB3Rs5W3CGXW4hXBDRJH5Nd3YeFHXo19oKTAinvmq_715BkMTiLvLLiiOO7ziH2M9msQOpIK0Lx2jAs3nKx_lsFC5uLi5XOjMqxdJU4s8JG05C6TzF2REZovJVyO8-iGI7l5-_0iBIGGSr9MmCdQMtkQkl2l0a6S0eFbkTghtrVE0I1FPN8WZNuToLrQtoxq7aAtQoZ-i9ZM0jAhL2DUiuCV9yoP6P9R8fQrL2A6YFTn0q5DLd8Mi0v8vU-iBfEEokvTWlt1t7ZRaplv-4K--YfMsEKYH8rF1onHFgR00a8d8zPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54e4b572e.mp4?token=doD1UYCsOY2GAq6AdDDuUc9-oWP2nGgQYZBApnnB3Rs5W3CGXW4hXBDRJH5Nd3YeFHXo19oKTAinvmq_715BkMTiLvLLiiOO7ziH2M9msQOpIK0Lx2jAs3nKx_lsFC5uLi5XOjMqxdJU4s8JG05C6TzF2REZovJVyO8-iGI7l5-_0iBIGGSr9MmCdQMtkQkl2l0a6S0eFbkTghtrVE0I1FPN8WZNuToLrQtoxq7aAtQoZ-i9ZM0jAhL2DUiuCV9yoP6P9R8fQrL2A6YFTn0q5DLd8Mi0v8vU-iBfEEokvTWlt1t7ZRaplv-4K--YfMsEKYH8rF1onHFgR00a8d8zPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌های ترامپ: «این جمعیت از معمول بیشتره یا چی؟ دارم جذاب سکسی می‌شم؟ چه خبره اینجا؟ اینجا واقعاً آدم‌های زیادی هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24983" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd3fb47f0.mp4?token=BhIittI63SLkOryG2uC9eRZmQfYoHdf_em7tppjEZ7p4WEHK-ni_cUwSycvqPnwKKszL2ho338F5juYfrXbJwFc0tJZXiIfAa4_cc2HQfIlTbow2Dn44GVadJ24ZNAj94RBrcT8Y4JwEMS6b6Ins2uNrvkZaHKCPEWkBFr2vd_eJFP-DCciSpmdHa_LfTvqQHfrJXSDGC7HYWE0hUYecfW455ziCR9ZMBr3SwWn23OX6qqZUjXpRJAaEW62kKemL23jwQvKZQhbu7JEj-gVITOw-pCvk-5qTIvYT-oIFhkmDMeKmQdqhEp1rXArBDPoXH8lpjal-fSGjZHKJvzaeVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd3fb47f0.mp4?token=BhIittI63SLkOryG2uC9eRZmQfYoHdf_em7tppjEZ7p4WEHK-ni_cUwSycvqPnwKKszL2ho338F5juYfrXbJwFc0tJZXiIfAa4_cc2HQfIlTbow2Dn44GVadJ24ZNAj94RBrcT8Y4JwEMS6b6Ins2uNrvkZaHKCPEWkBFr2vd_eJFP-DCciSpmdHa_LfTvqQHfrJXSDGC7HYWE0hUYecfW455ziCR9ZMBr3SwWn23OX6qqZUjXpRJAaEW62kKemL23jwQvKZQhbu7JEj-gVITOw-pCvk-5qTIvYT-oIFhkmDMeKmQdqhEp1rXArBDPoXH8lpjal-fSGjZHKJvzaeVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوکاس فاکس، خبرنگار فاکس‌نیوز: «درباره فلای‌دبی، آیا فکر می‌کنید ایران مسئول این حمله تروریستی بوده است؟»
ترامپ: «بله، شخصاً همین‌طور فکر می‌کنم.»
با این حال، بازرسان هنوز در حال بررسی هستند تا مشخص شود مظنون با
ایران یا یک طرف خارجی دیگر
ارتباط داشته است یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24982" target="_blank">📅 23:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b58bc0dae.mp4?token=DXqBHvDHdVW_CBwtmvWueANg3MZ5X49ghl357jEA3YVdxslqtwzvA2o0kWu3Wwju75NI_NNyT4r6sRbwaWDHt20RjZ1U_UIiHpigRO_8enDgM54QnojIqiADXN8NrA-oHCaV9s00R3I-RLV-TvmSlZiNZZpEbYR1jy2KLrUedE6aXSVXnfzC3UmVeDXBiIy2_fdWw3H75xq3hOfFu3lN92xra7uN6eseuREOBv4vK2C1Oe85PZxGikQfbuf_-WrwvOunZObHgcOV6mabHgszflXsXudTXnj1oaESpNd0qOTimx81N8Mhxds0xf2vfSepH2heVxHZNGz7_ctk27o9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b58bc0dae.mp4?token=DXqBHvDHdVW_CBwtmvWueANg3MZ5X49ghl357jEA3YVdxslqtwzvA2o0kWu3Wwju75NI_NNyT4r6sRbwaWDHt20RjZ1U_UIiHpigRO_8enDgM54QnojIqiADXN8NrA-oHCaV9s00R3I-RLV-TvmSlZiNZZpEbYR1jy2KLrUedE6aXSVXnfzC3UmVeDXBiIy2_fdWw3H75xq3hOfFu3lN92xra7uN6eseuREOBv4vK2C1Oe85PZxGikQfbuf_-WrwvOunZObHgcOV6mabHgszflXsXudTXnj1oaESpNd0qOTimx81N8Mhxds0xf2vfSepH2heVxHZNGz7_ctk27o9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : فکر می‌کنی احتمال داره که ایران پهپادهای نظامی خودشو به بریتانیا انتقال داده باشه ؟
ترامپ: من نمیتونم راجبش به شما چیزی بگم.
اما اگه اونا اینکار رو کرده باشن، عواقب خیلی سنگینی رو متحمل میشن.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24981" target="_blank">📅 23:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرنگار فاکس نیوز: در کاخ سفید، رئیس‌جمهور ترامپ به من گفت که معتقد است ایران مسئول حمله تروریستی به هواپیمای فلای‌دبی است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24980" target="_blank">📅 23:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e53e579ac.mp4?token=ZInh4mAVkns7OJCQ_3UE1TDAQzNoYrac0IQ5Yscb97jtb0rEAMZuSCW-iKkDS6XwfAognu05yHudFeugj8GadwVl_2DpkzIS_oGYLUR_VENka00PdoXBO1oanAE2_iFpLTXmPaxbN03qCySL7bIDouP_8iGGDgLLq_x7xWMvzePeIK_WtuZ-JW3H-jM5KefProw_Kpt2V2rTgpnF3XuAHV43Dcy-cxHtlgqXmG9Vcuzik_oF3FxmGfd2exvJ9fMdqL_Jq2Tn1TFsSGCOFwIZkibsHmYC66UzL0P5TeJ-26HU9Inmr-z_ZhIZT8DlXmCzNaDNBgqwfDFfTKf7iL07tAZXbikkcuuxQ_0EtM3CGqWfrNJO4lNwVscuN_XWC7G0tmFHGh2EVGFRpstYEzGlQkCEmjSvOdqIJeqiPUCOPhEF0DtsSEdVstmcJ5Ffm_fQhxfG87qKzUN1S2H_jPVgtXNdRfAbc9F9rjpsC24A8u7MnDLRwPSnNXI8wZDXt042ZmEFzcfAQq4USTEx550THLrABe1jtzAfsapukdUdavADJNTBxqYSJ9AXviz9Dnf7y_32x4BW45Bq8yWokFF8k1qC0nvP2I9-4ZDlDBNEqDGY4DfBu3AM3w1rcIY7F_XqXa5AC1-i9JMETBgPsfyCuNAIGPjFNmwlXPHTihU1QG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e53e579ac.mp4?token=ZInh4mAVkns7OJCQ_3UE1TDAQzNoYrac0IQ5Yscb97jtb0rEAMZuSCW-iKkDS6XwfAognu05yHudFeugj8GadwVl_2DpkzIS_oGYLUR_VENka00PdoXBO1oanAE2_iFpLTXmPaxbN03qCySL7bIDouP_8iGGDgLLq_x7xWMvzePeIK_WtuZ-JW3H-jM5KefProw_Kpt2V2rTgpnF3XuAHV43Dcy-cxHtlgqXmG9Vcuzik_oF3FxmGfd2exvJ9fMdqL_Jq2Tn1TFsSGCOFwIZkibsHmYC66UzL0P5TeJ-26HU9Inmr-z_ZhIZT8DlXmCzNaDNBgqwfDFfTKf7iL07tAZXbikkcuuxQ_0EtM3CGqWfrNJO4lNwVscuN_XWC7G0tmFHGh2EVGFRpstYEzGlQkCEmjSvOdqIJeqiPUCOPhEF0DtsSEdVstmcJ5Ffm_fQhxfG87qKzUN1S2H_jPVgtXNdRfAbc9F9rjpsC24A8u7MnDLRwPSnNXI8wZDXt042ZmEFzcfAQq4USTEx550THLrABe1jtzAfsapukdUdavADJNTBxqYSJ9AXviz9Dnf7y_32x4BW45Bq8yWokFF8k1qC0nvP2I9-4ZDlDBNEqDGY4DfBu3AM3w1rcIY7F_XqXa5AC1-i9JMETBgPsfyCuNAIGPjFNmwlXPHTihU1QG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: «آیا نگران شیوع بیماری در روسیه هستید؟»
ترامپ: «بله، هستم.
شیوع ذات‌الریه، اگر بخواهید این‌طور صدایش کنید.
این بیماری چیزی بود که قبلاً می‌توانستیم آن را کنترل کنیم. اما به‌نوعی این میکروب‌ها قوی‌تر و باهوش‌تر شده‌اند. آنها مثل یک ارتش هستند. میکروب‌ها واقعاً نسبت به گذشته قوی‌تر شده‌اند و چیزهایی که قبلاً برای درمان ذات‌الریه مؤثر بودند، دیگر به همان اندازه مؤثر نیستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24979" target="_blank">📅 23:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c5518a59.mp4?token=F7czdVlMDypiwvlvq7XoY7RotzGmalnBEouQc_XqRGbK3qhMyZ3rZ7KCBJhVWsBTTI0qr4fXojgTun_lstiqSPTE7R5Kyernn3xE6UHs85xEf8y2pDx0PVG-U7sWoXH9NEIAnmymrM6Qw_HLTinJUgZEr869K9iGudnRwrd65w-H5w6VqxUj8A_6RM9etT6PX9jyRvnBYwF9mEK8BBrDQTZS-s3D3ABbZRz9mTJtg8-C40ks6HT6G7674txgaSuiKDCh0wOGc_ZiAkZCBpYsHArjM8wZKUrqvm4FDUP3RTlkFd-sDTCGXanIo2aR2iUQLW1oMdxCKgBQ6HFH278UxDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c5518a59.mp4?token=F7czdVlMDypiwvlvq7XoY7RotzGmalnBEouQc_XqRGbK3qhMyZ3rZ7KCBJhVWsBTTI0qr4fXojgTun_lstiqSPTE7R5Kyernn3xE6UHs85xEf8y2pDx0PVG-U7sWoXH9NEIAnmymrM6Qw_HLTinJUgZEr869K9iGudnRwrd65w-H5w6VqxUj8A_6RM9etT6PX9jyRvnBYwF9mEK8BBrDQTZS-s3D3ABbZRz9mTJtg8-C40ks6HT6G7674txgaSuiKDCh0wOGc_ZiAkZCBpYsHArjM8wZKUrqvm4FDUP3RTlkFd-sDTCGXanIo2aR2iUQLW1oMdxCKgBQ6HFH278UxDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : «چه تهدیدی باعث شد هواپیماهای آمریکایی را از بریتانیا خارج کنید؟»
ترامپ: «ما به این نتیجه رسیدیم که ممکن است تهدیدی وجود داشته باشد و چرا باید آنها را آنجا نگه می‌داشتم؟ انتقال آنها هزینه بسیار کمی دارد. ما افرادی را که این تهدید را مطرح کرده‌اند می‌شناسیم و آنها
با ایران مرتبط هستند
.»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24978" target="_blank">📅 23:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4307e8a523.mp4?token=tTnlOXIDmLUe0raM4J3SRPc2oox_wbwCqIwtHFKZv7uMUBXiHfIxQ84pt2LrZvdRXUOIo-ISKqL106tKfyDI_r0fW0Nah74szwJ0lmiq57Sfas29DC9tPAt7egzqDpxqa2WP_8wZ1C2HM-wAQR-G6uKZOLm5Pk9l1NMVNYRPVP8cCeNXtu3XHQl4EhehXfNlEhF6fUvO0dNcBS1zNglruq6zv1p48SfEGfbEdVIO5MT3-eOJhHjF0NAxJ0M4CsZoLrtjaDus9gpvMuqsa-THpwjaU6xOPNZQ_M50lNPSjOKkU0tLr9HvO4oRVpMUITNNXEGFaG4B2lD7alkskynugA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4307e8a523.mp4?token=tTnlOXIDmLUe0raM4J3SRPc2oox_wbwCqIwtHFKZv7uMUBXiHfIxQ84pt2LrZvdRXUOIo-ISKqL106tKfyDI_r0fW0Nah74szwJ0lmiq57Sfas29DC9tPAt7egzqDpxqa2WP_8wZ1C2HM-wAQR-G6uKZOLm5Pk9l1NMVNYRPVP8cCeNXtu3XHQl4EhehXfNlEhF6fUvO0dNcBS1zNglruq6zv1p48SfEGfbEdVIO5MT3-eOJhHjF0NAxJ0M4CsZoLrtjaDus9gpvMuqsa-THpwjaU6xOPNZQ_M50lNPSjOKkU0tLr9HvO4oRVpMUITNNXEGFaG4B2lD7alkskynugA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: «نظر شما درباره ضدحمله و عملیات تهاجمی عربستان و یمن علیه حوثی‌ها چیست؟»
ترامپ: «همه‌چیز درست خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24977" target="_blank">📅 22:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e845f43990.mp4?token=So4a1nZbRCcNH-jLAARLGIJSUhfmdUA-3IS0rlBftkmfxy08EOtUp3sgQmTm7U_GFFnnX4L_88bRVVRhy6yc4wgDISpspcict_TpG1cqbZUwsJEH-oampQ48oyTnxe-AW27SBYLBsKZYGLD03pPYXnA4akExYhPvJA2CZ2vraAhN44F-z0PvDquS8hTL8cZSrUDIvAl1R5yPEtNA8BAgkY4t5RTS0YYX2MgKVZ9uKQBT-MhT1PDFs8ms9m2s2wZUSfPG-X-10NUtEqrU7gSCeCJ47DMWQrvKIqttPDUdx---6-IBdURNjzvK_HhsOCrNR0vIc7n4SADYZu7NDfXPFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e845f43990.mp4?token=So4a1nZbRCcNH-jLAARLGIJSUhfmdUA-3IS0rlBftkmfxy08EOtUp3sgQmTm7U_GFFnnX4L_88bRVVRhy6yc4wgDISpspcict_TpG1cqbZUwsJEH-oampQ48oyTnxe-AW27SBYLBsKZYGLD03pPYXnA4akExYhPvJA2CZ2vraAhN44F-z0PvDquS8hTL8cZSrUDIvAl1R5yPEtNA8BAgkY4t5RTS0YYX2MgKVZ9uKQBT-MhT1PDFs8ms9m2s2wZUSfPG-X-10NUtEqrU7gSCeCJ47DMWQrvKIqttPDUdx---6-IBdURNjzvK_HhsOCrNR0vIc7n4SADYZu7NDfXPFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره پالایشگاه‌های نفت روسیه: «مشکل، کمبود پالایشگاه‌هاست.
حجم بسیار زیادی نفت از تنگه هرمز خارج می‌شود.
به‌دلیل جنگ، با کمبود پالایشگاه مواجه هستیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24976" target="_blank">📅 22:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24975">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آسوشیتدپرس: آمریکا در حال گسترش بررسی درباره تسلیحات فضایی است و کارشناسان هشدار داده‌اند که نبود مقررات روشن درباره سلاح‌های متعارف در فضا می‌تواند به رقابت نظامی جدید میان قدرت‌های بزرگ منجر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24975" target="_blank">📅 22:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیمان مکه فعال شد
وزارت امور خارجه پاکستان: پاکستان، پادشاهی عربستان سعودی و ترکیه توافق کردند که نیروهای نظامی و قابلیت‌های مورد توافق را فراهم کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24974" target="_blank">📅 21:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ای۲۴نیرز تصاویر جدید و جزئیات جدیدی درباره خلبان مهاجم: او چندین بار در گذشته به اسرائیل سفر کرده بود و قصد انجام این حمله را از ماه ژوئیه برنامه‌ریزی کرده بود. در امارات متحده عربی، مقامات در حال تحقیق درباره کارمندانی هستند که به این خلبان اجازه ورود به "فلای دبی" را داده‌اند. همچنین، بررسی می‌شود که آیا او یک هدف جایگزین را در صورت شکست طرح اصلی در نظر گرفته بود یا خیر، که احتمالاً یک پایگاه نظامی آمریکایی در اردن بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24973" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پزشکیان: هربار بازرسان آژانس به ایران آمده‌اند، مراکز هسته‌ای و دانشمندان ما شناسایی و پس از آن این مراکز بمباران و دانشمندان ما ترور شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24972" target="_blank">📅 20:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24971">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پزشکیان: مشکل ما با آمریکا این است که هر بار به میز مذاکره می‌آییم، بلافاصله جنگ به ما تحمیل می‌شود @WarRoom
🤣</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24971" target="_blank">📅 20:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24970">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aokH5lr02EiXrkg6Zr8TVrq61eAfkIuvdDh5noVqR216R9VW2RSrA-sQDDPQGfQK9DoXoP4zlYjKo1yaYtXLc0aC8JkOo2CS8k7gAH3_t8_8aXJNMPPLxHWj4qKsJGnqM1iHHq2rXrh4EmB_R7ifo3Pi7k0cCZNUL-rHrvEqhpBCtrLQFRfmXIbs81H4Zb8DKSjy6qw12dXvOXOyV-2qrjVdVRcwcJrIauCzAPK8b_KMrKDO2ObqcgI2oGqf37uZs9rI_PnKqiOmUTDlXojI9nDjYASDpgO-VuiF06tCXZedlzbwxXhhc1UmvbKh0FkzGMDnZEfXGvdnEpuQD0Cf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه ترکیه، حاکان فیدان، وزیر دفاع ترکیه، یاشار گولر، و رئیس ستاد مشترک نیروهای مسلح، سرلشگر سلجوق بایراکتاراوغلو، در ریاض با همتایان پاکستانی و سعودی خود دیدار کردند تا در جلسه کمیته سیاسی، دفاعی و استراتژیک شرکت کنند. این کمیته بر اساس توافق مکه برای همکاری‌های دفاعی تشکیل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24970" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پزشکیان: مشکل ما با آمریکا این است که هر بار به میز مذاکره می‌آییم، بلافاصله جنگ به ما تحمیل می‌شود
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24969" target="_blank">📅 20:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJptizBBn0_aG0lCzZszHar5KNgJSIEMiqFwvElMUsd0L3qf7afpDiTl8jXy7bCzZCu-rnVxGQfeoks45MxRN4rj4ZViFrOqApatCb7juWSTohF6Uc51xbont4x3o_8lAuglD1YnpNV6DLjSqt6_NWsICINPKYCQfIUXkLvOiLPGbTzYC9-0yLcOSsYK1eLCCJbf0vF6IC_pLeQmRiACACTs-QDNPbc1HgDrV4fOdz0HKKwbt7tEMaTz6-d8bE1E2NWEKPZOIXIkVSlF0hZKRUXTkDlAVjLYbE12SMcJnLk0s3ICD23ZMiVU_D7RXjPamb2b0ikFOUuklNjp747i2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : آنچه باعث افزایش قیمت بنزین می‌شود، دیگر تنگه هرمز نیست، چون اکنون تعداد بی‌سابقه‌ای بشکه نفت تقریباً به‌صورت روزانه از آن خارج می‌شود، بلکه این کلمه است: «پالایشگاه‌ها»؛ جایی که پالایشگاه‌های روسیه توسط اوکراین منفجر می‌شوند و پالایشگاه‌های ما در ایالت‌های آبی، مانند کالیفرنیا، توسط دموکرات‌ها تعطیل می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24968" target="_blank">📅 20:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24967">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسرائیل هیوم: آمریکا محدودیت‌های عملیاتی پیشین برای فعالیت نیروی هوایی اسرائیل در حریم هوایی عراق را لغو کرده و به اسرائیل چراغ سبز برای حمله به گروه‌های مسلح مورد حمایت ایران در عراق داده است.
این گزارش به نقل از منابع ناشناس منتشر شده و تاکنون از سوی آمریکا، اسرائیل یا عراق به‌طور رسمی تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24967" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca7496737.mp4?token=bt_UnXJRFngGa-Vo7ivwbeQCzelVLpuLd_rk5-GpUMKWsxBJBAOUE0vCyAg4MBvKseDn68CzCYLfVF7kdrrGP7c69JA6S4o46cIhdylEoWqUt0DHzzz3SCUisyBRcSQVf74McZB8yFZHana2RMReMXD2hJxmgziDzdjEq_61lEgXRS-nhWuJ2p9zpViEnJiTmqJ1WTfxTXTFaFUoYAesVYKoXsQ0-ibvKPKQGJYyf1SJfpMKJrF-rBJ4HCbuzYuO8ZIsk4PwwULkMJ3_kHQnYvkbQ1rjVdULSJbQ6rQ-MlEDKKYPcrzIzaCdohkMgwFLMwrIP0Gz-vGH1sPY7fegQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca7496737.mp4?token=bt_UnXJRFngGa-Vo7ivwbeQCzelVLpuLd_rk5-GpUMKWsxBJBAOUE0vCyAg4MBvKseDn68CzCYLfVF7kdrrGP7c69JA6S4o46cIhdylEoWqUt0DHzzz3SCUisyBRcSQVf74McZB8yFZHana2RMReMXD2hJxmgziDzdjEq_61lEgXRS-nhWuJ2p9zpViEnJiTmqJ1WTfxTXTFaFUoYAesVYKoXsQ0-ibvKPKQGJYyf1SJfpMKJrF-rBJ4HCbuzYuO8ZIsk4PwwULkMJ3_kHQnYvkbQ1rjVdULSJbQ6rQ-MlEDKKYPcrzIzaCdohkMgwFLMwrIP0Gz-vGH1sPY7fegQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور جمهوری‌خواه ریک اسکات:
من هم از قیمت‌های بالای بنزین خوشم نمی‌آید، اما نمی‌خواهم با یک سلاح هسته‌ای کشته شوم.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24966" target="_blank">📅 19:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش رویترز می‌گوید پاکستان پیش از آغاز عملیات صبح امروز،
تجهیزات نظامی، سامانه‌های پدافندی، توپخانه سبک، پهپاد و تجهیزات ضدپهپاد
به عدن فرستاده و
مشاوران نظامی پاکستانی
نیز در محل حضور دارند. اما رویترز تأکید کرده که متحدان عربستان قرار نیست مستقیماً در عملیات رزمی زمینی شرکت کنند. همچنین
پهپادهای ترکیه‌ای
که عربستان قبلاً خریداری کرده، در عملیات به کار گرفته شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24965" target="_blank">📅 19:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نتانیاهو : ما مأموریت را تکمیل خواهیم کرد. می‌خواهم بدانید‌که ما هر روز آن را تکمیل می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24964" target="_blank">📅 19:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f364dd49e8.mp4?token=dT-77CgbjDRRghpI8pzfHulOQvuls9x0GZHpLhHvvbffMGIa2OV2l9QoubOcrHs-3qLKlCbkagVk2tQfDkWxK3rrXUx-5o7FhPEnjDULXq9klbDoBYN7I312WWCclD0JcJMe8XZM-LGJbeBD6AjT4j8WBCrWvCGGHii76Gp10K9se6oq-aeSUnZCNBfkwJrTmllAcOK_bZqvM1Rrpt5ITySrB-5DEv0DciuaY9i-r6BQRgOYrW13d56BPzhUJ78G8BM6jfE3u29RSN-sZpKClGbn4sdyHIJPscWnbigcgr3giTDdPpjqpki57e0Il2r9jCdYZBiuS6-Rk8sdjSdlrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f364dd49e8.mp4?token=dT-77CgbjDRRghpI8pzfHulOQvuls9x0GZHpLhHvvbffMGIa2OV2l9QoubOcrHs-3qLKlCbkagVk2tQfDkWxK3rrXUx-5o7FhPEnjDULXq9klbDoBYN7I312WWCclD0JcJMe8XZM-LGJbeBD6AjT4j8WBCrWvCGGHii76Gp10K9se6oq-aeSUnZCNBfkwJrTmllAcOK_bZqvM1Rrpt5ITySrB-5DEv0DciuaY9i-r6BQRgOYrW13d56BPzhUJ78G8BM6jfE3u29RSN-sZpKClGbn4sdyHIJPscWnbigcgr3giTDdPpjqpki57e0Il2r9jCdYZBiuS6-Rk8sdjSdlrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسحاق هرتزوگ، رئیس‌جمهور اسرائیل: «رئیس‌جمهور ترامپ درباره تهدیدی که از سوی تهران وجود دارد،
حق دارد
. ما با یک
امپراتوری شیطانی
روبه‌رو هستیم که می‌خواهد جهان را به‌شدت افراطی کند، جهان آزاد را به تصرف خود درآورد و تا اروپا و ایالات متحده پیش برود.»این موضوع فقط نگرانی اسرائیل نیست و
تمام منطقه همین احساس را دارد
؛ چه آن را علناً بیان کنند و چه پشت درهای بسته.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24963" target="_blank">📅 18:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFbzJEThFlAgzpOrFA8ptKbbJ6a843lPTltys-8XcckEETj7bWvNGp9XItqODrJRL00CMrzfYt-1u1mBhY3st-mhOAgwre8VGbTeis4yNppC9p08feL1ykorcIg03capmqPJfZJK7pQ5dUVIpuWXCEPSt3d_kD3YqrQ_CwgJHwoQ1eLjW6xeG9bA05V0cN2oUMHBm3jnmT-PXk_ZmX2Zw1JWUOrJ6imV4EzIEXUd9wlNc5joYJ8e3307q0aaEIT4dfuOJ4utZmOJstXhx9peCP-mX3kdO-SGDNc73MHtiNEbsTSFFWzYHog11H793wtdfqSvr7hfxdmiUJOmRzeY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور رژیم جمهوری اسلامی , اسکندر مؤمنی برای شرکت در مذاکراتی وارد دوحه قطر شد هم زمان ۶ سوخترسان و جنگنده های آمریکای با تمرکز بر تنگه هرمز در حال اسکورت کشتی ها از مسیر جنوبی تنگه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24962" target="_blank">📅 18:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shG_AjxAK59QETxzwVBbzBEeA3BRtTmB3Fs59mRc2uNx43RO5nBscfvpXtujx9F19I1fJZlzOKJQCuSKinB0zMlt_9CxhwjMa9FTXIhxbN4l5ZclogHE_H0KlsleYLNK9b2DN2DCYyFJCTG-LAUrp9BylKi11YSYOS4shmyLIo6qPLFxXPaT0Tlvp6nRQGip7X9FKyQHZVc_YkmbPcLjFVaBKnIzpThskOakT2TYoFfht7nfwvrIibC2pATBAq5w5gH0bsiC86n9GB6G3QdAdyBww-bpTTSEqjMMGvG9ThtmPFehFrqxTzC1sEzUSu-Y7IpAR6q22-zRMhNToPbiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است. یک منبع موثق گزارش داده است که یک نفت‌کش حامل نفت خام، در ناحیه‌ای بالاتر از خط آب‌خور، مورد اصابت یک پرتابه ناشناس قرار گرفته است.
مقامات در حال بررسی موضوع هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24961" target="_blank">📅 18:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اتاق جنگ با یاشار | حقیقت‌یاب:
آیا آمریکا و استارلینک می‌توانند بدون همکاری حتی یک اپراتور یا نهاد ایرانی، اینترنت را مستقیم به گوشی مردم ایران برسانند؟
فناوری «Direct-to-Cell» برای همین نوع اتصال طراحی شده و گوشی معمولی می‌تواند بدون دیش و دستگاه اضافی مستقیماً با ماهواره ارتباط برقرار کند؛ ماهواره عملاً مانند
دکل موبایل در فضا
عمل می‌کند. در مدل فعلی، استارلینک عمدتاً از فرکانس و شبکه اپراتورهای شریک استفاده می‌کند، اما در سناریوی ایران می‌توان از
یک اپراتور خارجی یا معماری مستقل ماهواره‌ای
استفاده کرد؛ بنابراین همراه اول، ایرانسل و رایتل الزاماً نباید همکاری کنند. در این حالت می‌توان برای کاربران
eSIM
( آسان ولی نیازمند گوشی مدل بالا)
یا سیم‌کارت فیزیکی(
سخت در توزیع ، ولی راحت تر) صادر کرد، اما سیم‌کارت به‌تنهایی کافی نیست و باید شبکه ماهواره‌ای، احراز هویت و فرکانس موردنیاز از سمت استارلینک و اپراتور شریک خارجی فراهم شود که این هم میتوانند . از نظر گوشی، سرویس‌های ماهواره‌ای اپراتورها در برخی کشورها از
iPhone 13 به بالا
پشتیبانی می‌کنند(قابلیت‌های ماهواره‌ای اختصاصی اپل از
iPhone 14 به بعد
وجود دارد این دو سرویس با یکدیگر یکی نیستند) اما سؤال مهم‌تر این است که آیا حکومت ایران می‌تواند چنین ارتباطی را قطع کند؟
قطع دکل‌ها و شبکه اپراتورهای داخلی، ارتباط مستقیم گوشی با ماهواره را قطع نمی‌کند
؛ ولی هیچ تضمینی وجود ندارد که دولت نتواند با
پارازیت و اختلال رادیویی روی فرکانس مربوطه
یا روش‌های فنی دیگر ارتباط را مختل کند. بنابراین «کاملاً مستقل از زیرساخت ایران» از نظر فنی ممکن است، اما «غیرقابل اختلال توسط حکومت ایران» نیست.
اگر تصمیم و زیرساخت لازم آماده باشد، راه‌اندازی محدود می‌تواند در مقیاس چند هفته تا چند ماه تصورپذیر باشد، اما ایجاد اینترنت موبایلی گسترده برای میلیون‌ها نفر به زمان و ظرفیت بیشتری نیاز دارد و اگر در انتظار این سرویس هستید بهتر است گوشی با قابلیت eSIM هم آماده داشته
باشید
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24960" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اتاق جنگ با یاشار | حقیقت‌یاب: ماجرای موسوم به «طاعون روسی» پس از مرگ یک پژوهشگر ۲۸ ساله در مؤسسه تحقیقات ضدطاعون در ایرکوتسک روسیه مطرح شد؛ اما
آزمایش‌های رسمی تاکنون ابتلای او به طاعون را تأیید نکرده‌اند
و علت مرگ، ذات‌الریه با منشأ نامشخص اعلام شده است. گزارش‌هایی درباره شکستن لوله حاوی باکتری یرسینیا پستیس منتشر شد، اما مقام‌های روسیه می‌گویند
هیچ حادثه آزمایشگاهی و ارتباطی میان مرگ او و عوامل بیماری‌زای محل کارش پیدا نشده است.
حدود ۲۰۰ نفر تحت مراقبت قرار گرفتند و در میان افراد بررسی‌شده
دو مورد کووید و دو مورد راینوویروس
شناسایی شده، اما مورد جدیدی از طاعون گزارش نشده است. کشورهای همسایه از جمله قزاقستان، تاجیکستان، ازبکستان و قرقیزستان
کنترل‌های بهداشتی مرزی را افزایش داده‌اند، اما مرزها بسته نشده‌اند.
کارشناسان نیز می‌گویند فعلاً هیچ شواهدی از شیوع طاعون ریوی یا یک بیماری جدید مشابه کرونا وجود ندارد.
طاعون ریوی در صورت تأیید بیماری جدی و بدون درمان می‌تواند مرگبار باشد، اما با تشخیص سریع و آنتی‌بیوتیک قابل درمان است.
بنابراین ادعای «طاعون مهندسی‌شده روسی» یا یک همه‌گیری جدید در حال حاضر
فاقد شواهد معتبر است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24959" target="_blank">📅 17:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c88d29dc5.mp4?token=gBKxX434FS56vWwuIwpg7OnSOjUZSC74VpA2KhGGN8j3SxC1p70zgIxldQQ0jcx7rvd0-y81eGo0paRE7ykGtULIybaikYgkkzCTNaAt6-ZXmnXM8i57MOYL8aFuOHGFza0NfM4eETwxbsPh9P21TOIvHNuscgZA-fqZbHzrjG3auRlnLlc1FTPKoS_aItNq8-7UNLQMewojxryAuYG1iw6MnTkQv66Pmf1JJh61zZl8IZ_ytQI-J4S9rVyQ1D4trZMypVkYggHY6GNk5IZJFoDOMbC8qfYLsEUTBXMp-ATA2T-dudci2u1p6haCPy1tCzGB9jGSQfIi_r6nhbYlLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c88d29dc5.mp4?token=gBKxX434FS56vWwuIwpg7OnSOjUZSC74VpA2KhGGN8j3SxC1p70zgIxldQQ0jcx7rvd0-y81eGo0paRE7ykGtULIybaikYgkkzCTNaAt6-ZXmnXM8i57MOYL8aFuOHGFza0NfM4eETwxbsPh9P21TOIvHNuscgZA-fqZbHzrjG3auRlnLlc1FTPKoS_aItNq8-7UNLQMewojxryAuYG1iw6MnTkQv66Pmf1JJh61zZl8IZ_ytQI-J4S9rVyQ1D4trZMypVkYggHY6GNk5IZJFoDOMbC8qfYLsEUTBXMp-ATA2T-dudci2u1p6haCPy1tCzGB9jGSQfIi_r6nhbYlLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز:
نیروهای دولت یمن با پشتیبانی عربستان مدعی
تصرف منطقه راهبردی ذوباب و مواضع کلیدی مشرف بر تنگه باب‌المندب
شده‌اند. طبق گزارش‌ها،
فرودگاه ذوباب
نیز به کنترل این نیروها درآمده و مسیرهای تدارکاتی منتهی به باب‌المندب قطع شده است. درگیری‌ها همچنان در اطراف برخی مواضع نظامی ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24958" target="_blank">📅 17:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رویترز:
بانک HSBC میانگین قیمت طلا را برای سال‌های آینده کاهش داد؛ پیش‌بینی ۲۰۲۶ از
۴۵۶۰ به ۴۴۹۰ دلار
و پیش‌بینی ۲۰۲۷ از
۴۹۲۵ به ۴۸۲۵ دلار
در هر اونس کاهش یافته است. با این حال، HSBC همچنان چشم‌انداز بلندمدت طلا را مثبت می‌داند و معتقد است اگر قیمت به محدوده
۴۰۰۰ دلار یا پایین‌تر
برسد، احتمال افزایش خرید توسط بانک‌های مرکزی وجود دارد که می‌تواند از قیمت حمایت کند. در کوتاه‌مدت،
افزایش بازده اوراق آمریکا، دلار قوی و رشد قیمت نفت
همچنان از عوامل فشار بر طلا هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24957" target="_blank">📅 17:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/990c4f7388.mp4?token=OlXZSmg4MapMW4E_-Ft1eFsmVo0eY1KNhdnbE7qXJWkd-tnhtPxwrQ5in9gwy47DfOrB1IW9smvOGqwSwJfn5w4zc_myVNxP9xdW9DoRx3SnSAXwEt2TyG9tCSAwDVQl5PRVKROB8kZ7ZNoch_MWY9xBqV3lLxMdWdq4km-8OnplVIqu-UXIS_AdM1nRGzwOVdtTP8tB7Om6fCsrDtrcGEOWiXWYl53ssQ6LxIBhOxCeMrig8hkVWvOJg06ZwxPGY2ODzIVk97phagyxkIFvgtyes-R7uoRDrmLNC96pMBM2o39wV-I1uIODzVYvsE0HhZDanKT1M_IseDP_J_5N2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/990c4f7388.mp4?token=OlXZSmg4MapMW4E_-Ft1eFsmVo0eY1KNhdnbE7qXJWkd-tnhtPxwrQ5in9gwy47DfOrB1IW9smvOGqwSwJfn5w4zc_myVNxP9xdW9DoRx3SnSAXwEt2TyG9tCSAwDVQl5PRVKROB8kZ7ZNoch_MWY9xBqV3lLxMdWdq4km-8OnplVIqu-UXIS_AdM1nRGzwOVdtTP8tB7Om6fCsrDtrcGEOWiXWYl53ssQ6LxIBhOxCeMrig8hkVWvOJg06ZwxPGY2ODzIVk97phagyxkIFvgtyes-R7uoRDrmLNC96pMBM2o39wV-I1uIODzVYvsE0HhZDanKT1M_IseDP_J_5N2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو تأیید کرد
بمب‌افکن‌های آمریکایی بلافاصله پس از طرح تروریستی، پایگاه ویرفورد را ترک کردند، اما این جابه‌جایی را «غیرعادی» ندانست: «چرخش‌های منظمی وجود دارد… من مستقیماً این موضوع را به جابه‌جایی انجام‌شده مرتبط نمی‌کنم. دیدن چنین چرخش‌هایی غیرعادی نیست.» تمام بمب‌افکن‌های آمریکایی مستقر در این پایگاه به پایگاه‌های اصلی خود در آمریکا بازگشته‌اند. هر ۶ مظنون این پرونده نیز آزاد شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24956" target="_blank">📅 17:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32f588d98.mp4?token=Uncz7JaInOTc9P7Wf_NFqsa3S0J1bJMIb7TTE9EzVnB1KRZ6_B8hTPd8xKZqWuZI_9d1DJjk5AkWIbWTq9_74WUAELo41_wJQ6GsGhpD-m3jHYoUVS_rJA0SJtzeyImhgppCaQW0FqzCMj_z9BldRB3bIiBYtuM868ozg6Zv2smmVMZtVfAjTEifXioIQx3mnI0yVA8NAaBrOTdA19BMRJZk4dsHIEECtqOHs0tMZ8qTJC7GD7SddNeQPMvJu7_wWUYkBzDb0zNGx6aZod9rRDOxvL-NrtsP2b34-qOPpYDgNS0beyF1G1NHWNTDh0dh0uYtsSYQ9I2zR93OoYJc8EJxiFtmen3MHCDgAt8D8Yy54AaHn494goaaAOHmlthn9YZam0xJJOinJ27yHZDD8m5nC_Mkwalied9csX50jLqJyBugAr0PIFURH7MqcGepYVtXxHawdDevYIKNbLRPQoGYYCVbykc3mJgkcN_J5EvFRY-ClzC3fPjiRII42MrxYLeU6oDPzpsBqnFjcHoakQO3FB4xEQgGQ87tqcxQdS7ZxoIj5DtjS9opvrBITUK444DhH4DC01UwL5dH26Nrlk1J8IYTkVG11RmFuQDg4EMfUIDIRGq2zsqm_zx06_pfcTCSpCpxTt-gcGDP4fpqhP2i5KMr43ojrahM2pPMU4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32f588d98.mp4?token=Uncz7JaInOTc9P7Wf_NFqsa3S0J1bJMIb7TTE9EzVnB1KRZ6_B8hTPd8xKZqWuZI_9d1DJjk5AkWIbWTq9_74WUAELo41_wJQ6GsGhpD-m3jHYoUVS_rJA0SJtzeyImhgppCaQW0FqzCMj_z9BldRB3bIiBYtuM868ozg6Zv2smmVMZtVfAjTEifXioIQx3mnI0yVA8NAaBrOTdA19BMRJZk4dsHIEECtqOHs0tMZ8qTJC7GD7SddNeQPMvJu7_wWUYkBzDb0zNGx6aZod9rRDOxvL-NrtsP2b34-qOPpYDgNS0beyF1G1NHWNTDh0dh0uYtsSYQ9I2zR93OoYJc8EJxiFtmen3MHCDgAt8D8Yy54AaHn494goaaAOHmlthn9YZam0xJJOinJ27yHZDD8m5nC_Mkwalied9csX50jLqJyBugAr0PIFURH7MqcGepYVtXxHawdDevYIKNbLRPQoGYYCVbykc3mJgkcN_J5EvFRY-ClzC3fPjiRII42MrxYLeU6oDPzpsBqnFjcHoakQO3FB4xEQgGQ87tqcxQdS7ZxoIj5DtjS9opvrBITUK444DhH4DC01UwL5dH26Nrlk1J8IYTkVG11RmFuQDg4EMfUIDIRGq2zsqm_zx06_pfcTCSpCpxTt-gcGDP4fpqhP2i5KMr43ojrahM2pPMU4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل: «رهبران جهان به من می‌گویند: تو از دل جهنم ۷ اکتبر برخاستی، افراطی‌های اسلام‌گرا را شکست دادی و به بشریت امید دادی که می‌توان نیروهای تاریکی را شکست داد.
سپس بسیاری از آنها اضافه می‌کنند: ای کاش جوانانی مثل اینها در میان ما هم رشد می‌کردند.»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24955" target="_blank">📅 15:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2091a813.mp4?token=fkIPLY8IXf6kuLkGX3xmtB5_BJ_famIRgBu7gSfB4tlvIgKckF-ht_2Dy5KmKoz167Tnvsrw97-7hgjd64ANXaTG5nzcJRNasnAA1avm2h1QC9Xk_8JoyXIkD6VFaygVbra5O_TG2c9f5nF_koQ_ed4cq4wK0kcrySUAmmBkyl5GBUi-7f3Zszg6ySzBz1aZIX9qW0kcrB5UhBoluxZa5rRkPJvMI-hwj_Iq4quckv8zE1PA8RwNLLDqqTYH4Oypj7Wmp0YpYHIJlvNck6tvcDqHVTi4QBwFIVROIp8L1E_IOBXbu0kPIQUrhP-8XZJhosLzzI-8Bj9aTMPXPZcvEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2091a813.mp4?token=fkIPLY8IXf6kuLkGX3xmtB5_BJ_famIRgBu7gSfB4tlvIgKckF-ht_2Dy5KmKoz167Tnvsrw97-7hgjd64ANXaTG5nzcJRNasnAA1avm2h1QC9Xk_8JoyXIkD6VFaygVbra5O_TG2c9f5nF_koQ_ed4cq4wK0kcrySUAmmBkyl5GBUi-7f3Zszg6ySzBz1aZIX9qW0kcrB5UhBoluxZa5rRkPJvMI-hwj_Iq4quckv8zE1PA8RwNLLDqqTYH4Oypj7Wmp0YpYHIJlvNck6tvcDqHVTi4QBwFIVROIp8L1E_IOBXbu0kPIQUrhP-8XZJhosLzzI-8Bj9aTMPXPZcvEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در مراسم گرانیداشت ۷ اکتبر : اسرائیل اجازه نمیده جمهوری اسلامی موجودیت این کشور رو تهدید کنه. رژیم تهران ضعیف‌تر از هر زمان دیگه‌ای از زمان تأسیسشه، برای بقای خودش می‌جنگه و در نهایت از بین خواهد رفت. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24954" target="_blank">📅 15:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو در مراسم گرانیداشت ۷ اکتبر : اسرائیل اجازه نمیده جمهوری اسلامی موجودیت این کشور رو تهدید کنه. رژیم تهران ضعیف‌تر از هر زمان دیگه‌ای از زمان تأسیسشه، برای بقای خودش می‌جنگه و در نهایت از بین خواهد رفت.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24953" target="_blank">📅 14:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiW2f1z5H_GGS-NYiE36WJrZ-kOI3-0mocLWzyJdVkHAK0QDh11XFxuH5icoTztc6AiyYBMqBHcQaOnj3iZTFK8A3tTmpIIqAxKKCfiBEdxQujDRZBLLx2ImSXXOxwLlooToIurFX3CMsnRSVtlLAc-P8uU_IFM9db8-5xkBuRq5LtGv_qVWFU-7j3-8oPgvZ0g0NTeYD26mArpcMLtxxA5oqxU_wzNguwxTMmZyhmk_qbbvRHMaL9W2KhraeWxkvfF8wH5ZeMr1Boy4pd48gIHrRV1RMlKfrhN3FV4omO8yy7fHGR-mxtD_sc-GZ3ZGJIm4LbETBdY1GSY9VXQ3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم میهن بکش هر جوری که میتونی نا امید نشو … چیزی‌نمونده
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24952" target="_blank">📅 14:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سازمان دریایی بریتانیا :  گزارش می‌دهد که ایران یک نفتکش را که قصد داشت خلیج فارس را از طریق مسیر عمانی تنگه هرمز ترک کند، مجبور به بازگشت کرد و نفتکش از دستورالعمل‌های سپاه پیروی کرد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24951" target="_blank">📅 14:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-UKMNTP30qZvH30AiV_QKvVOrxIzlZaioZ5gzs99AlRq2saQlsH-7smdCqCwNdkL5ecjURT4GIgB1g8ClXnnLeYkssNCE7iZMYweZl07oKnGHeRqNpKnbVtCzd7WLhTL3Oh_Po8CWYIXyuXyMi9xsIrsXzcQ5wJPNN_CZ6-Xn74bLPMvZA1rXYSdKNZpXOSsnM3k7r4VBHqTsjIuBWjOoYZ_eR18a3o-K3ZxiEqnpJP7O7Nuab8G4sjsi7WCULGVGtCy6Gu-wiRFXV6bqBCPJPQj1r1Sw_5erK05HlUr2sd2kLFd6ksf4x70prZe6tg2UkXYAZPEh-2vsO8fUJYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گشت‌وگذار یک دانشجوی عراقی با خودروی آمریکایی دوج چارجر در همدان، در حالی که تصویر تروریستها؛ علی خامنه‌ای، قاسم سلیمانی و ابومهدی المهندس (جمال جعفر محمدعلی آل‌ابراهیم، معاون پیشین حشدالشعبی عراق) روی بدنه آن نقش بسته است. @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24950" target="_blank">📅 13:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دایرک جای ، کامنت جای درد و دل و جای سوالی های  بی مورد و آموزش کامپیوتر یا پشتیبانی اینترنت شما نیست ! برای آخرین بار میگم ۹ ماه شد چرا ملت نمیفهمند ؟ مسیج پشت هم ندین در هم و جا بجا میاد !  فقط در‌یک پیغام ،الان این دو نفر‌هی دارن پیغام میدن یکی قبض برق…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24949" target="_blank">📅 13:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7jRmLAFvAKLZi3a-em7g6QzJ039WDgXN5ZHw9dWHgDqE1kYNuPHPlaajfVc3VJBw7CDsu3hnkHOeYYnEj5Y3EyBwcKNNaETTuF9pA_RJ9Wuh5NMBVACxEssHQ0mKb0emSaK1bL_4eyuWwcy54WxYX-fUnAJOJgFR48_kydNrGYj-nyZ9TUPE-pPDkRqDcMVtW5xDvE9a3IB1uvEeFkSKuXbeTtwAhiZdkEZ_LuQ1q2MiYrICBVs7NMgHcUbdeE8TRLqV3WLgnJcZzGAp40Kx5_Ix6waXlQB5j3SWbAkcMqamgpvSZ-rQQql59Wpt4UARYejOt5aGYcUyzPk2sngYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرک جای ، کامنت جای درد و دل و جای سوالی های  بی مورد و آموزش کامپیوتر یا پشتیبانی اینترنت شما نیست ! برای آخرین بار میگم ۹ ماه شد چرا ملت نمیفهمند ؟ مسیج پشت هم ندین در هم و جا بجا میاد !  فقط در‌یک پیغام ،الان این دو نفر‌هی دارن پیغام میدن یکی قبض برق داده و اون هو میگه من کجام ، اخه یک بگه به تو چه ، چرا حالیشون نمیشه من نمیدونم !!!! من مشاور نیستم چیزی باشه برای همه میگم دایرکت جواب‌ نمیدم</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24948" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

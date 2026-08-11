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
<img src="https://cdn4.telesco.pe/file/DWOw1fVnu9-oT9hLaH8nzZ9yw8HjzLKd6S9ZDBVuc5cynjVP4qvMj2MRaHeEMwV811ml-4HIRDBYYKwGm8WdrgMyCisOx58zpBYIAMS-vlGiCBJU-iN1p4sERNTFHWS5wQ539VZdGeMkdQftGm8ZpLchFewXzBMxx7eI7aIo_1RUCw9jOCDxKuZkxXB0-KQOsvgi8QwKT5j1KVznupxhii0mMXoZEq9YrwPeXNOCc5X3u6OYGC5KIji2plJ6j89q0OMcgUfzwTHHLx0wg8H62oQUzh3hCLrV5BCfX98CUnXEA9Tn64kPYu53iD7UEac-0J-cgECpCi3xuTqMeOZx9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.22M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 14:41:23</div>
<hr>

<div class="tg-post" id="msg-680288">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رسانه قطری: توافق مکه بی‌معناست؛ چرا ائتلافی ضداسرائیل شکل نمی‌گیرد؟
عربی۲۱:
🔹
توافق مکه مشخص نکرده در برابر تهدیدهای منطقه‌ای، از جمله اسرائیل، چه موضعی خواهد داشت و هیچ‌یک از این ائتلاف‌ها اسرائیل را به‌عنوان دشمن معرفی نکرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/680288" target="_blank">📅 14:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680287">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
تنها جمله‌ای که پدر مینابی بعد از شهادت دخترش گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/680287" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8715daf57.mp4?token=E8Ze7hLVgKQURM20n9Qg6U7vp8hcatdi5xk7anoE3CfY9YWo7jroZB9sK7LmobzbCdbpd7dqX4KDm4dtgo8ybk-LVXkBMU3Ta0eaOIX89FQE1ssCPX7aWg0Ka01QXiik3Unn7-SaF4ocPP2K4jLsriZxsn_5OXu0Ol9bW9AfvXpzqnYxyFOeqmt6Jlzj5kSKkOr8Qb6K2ceMi-aAwyoL4OaimpMQMZ6o623jwq57sbDXF_9HQNh-sXs2JiM7lxDhCe6z6noVAFGvye-nGDK85pSD2f5yW8plVyHKUMEU1iIbLqOQmSLxj7JnDmYcQ_nKHCdDzoonuwfKrAQzUuyMRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8715daf57.mp4?token=E8Ze7hLVgKQURM20n9Qg6U7vp8hcatdi5xk7anoE3CfY9YWo7jroZB9sK7LmobzbCdbpd7dqX4KDm4dtgo8ybk-LVXkBMU3Ta0eaOIX89FQE1ssCPX7aWg0Ka01QXiik3Unn7-SaF4ocPP2K4jLsriZxsn_5OXu0Ol9bW9AfvXpzqnYxyFOeqmt6Jlzj5kSKkOr8Qb6K2ceMi-aAwyoL4OaimpMQMZ6o623jwq57sbDXF_9HQNh-sXs2JiM7lxDhCe6z6noVAFGvye-nGDK85pSD2f5yW8plVyHKUMEU1iIbLqOQmSLxj7JnDmYcQ_nKHCdDzoonuwfKrAQzUuyMRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
براساس علم عصب‌شناسی کتاب خواندن برای نوزاد، قوی‌ترین محرک رشد مغز است
🔹
در سال‌های اول، مغز کودک در هر ثانیه بیش از ۱ میلیون اتصال عصبی جدید می‌سازد!
🔹
شنیدن آهنگِ صدای والدین و دیدن تصاویر کتاب، دقیقاً همان چیزی است که این شبکه عصبی را فعال و قوی می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/680286" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680285">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
وزیر کشور پاکستان وارد تهران شد
🔹
سید محسن رضا نقوی، وزیر کشور پاکستان برای گفتگو با مقامات ایرانی وارد تهران شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/akhbarefori/680285" target="_blank">📅 14:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680284">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شهردار بوشهر برکنار شد
.
🔹
انصارالله: عربستان به دنبال وارد کردن یمن به جنگ‌های بی‌پایان است.
🔹
وزیر خارجه آلمان: ایران وارد مذاکرات با همسایگان منطقه‌ای و آمریکا شود.
🔹
براثر وقوع سیل و طوفان در فیلیپین ۱۹ نفر جان باختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/akhbarefori/680284" target="_blank">📅 14:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680283">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رئیس پلیس‌راه خراسان شمالی از اعمال محدودیت تردد انواع کامیون و تریلر در محور فاروج–جنگل گلستان و بالعکس از ۲۰ مرداد تا پایان هفته خبر داد
🔹
ممنوعیت تردد شامل انواع ناوگان باری است و وسایل نقلیه حامل مواد سوختی، مواد بهداشتی، کودهای شیمیایی و کالاهای اساسی از جمله گندم، جو، برنج، ذرت، سویا و دانه‌های روغنی از این محدودیت مستثنی هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/680283" target="_blank">📅 14:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680282">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: در زمان جنگ، جلسات را در هتل‌ها و ساختمان‌های خصوصی به طور محرمانه برگزار کردیم
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبر فوری:
🔹
انتقال بالغ بر ۴۰ درصد کالا در زمان جنگ نسبت به شرایط عادی بیشتر شد.
🔹
در زمان جنگ هفته‌ای ۴ جلسه به صورت حضوری برگزار می‌کردیم که مکان‌های آن به صورت محرمانه تغییر می‌کرد. در کشور شبهه ایجاد شده بود که نمایندگان نیستند، اما دستگاه امنیتی اجازه ندادند که مجلس به صورت رسمی کارش را ادامه بدهد.
🔹
با مجوزی که با تایید شورای نگهبان گرفتیم این موضوع به قانون تبدیل شد که مجلس در شرایط اضطرار می‌تواند جلسات خود را با فضای مجازی انجام بدهد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/680282" target="_blank">📅 14:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680281">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
الجزیره: آمریکا به‌دنبال راه خروج از جنگ با ایران؛ ترامپ از مذاکرات کنار گذاشته شده است
🔹
ونس،روبیو،رئیس سازمان سیا و دن کین برای خروج از بن‌بست جنگ با ایران، بدون حضور ترامپ، گفت‌وگوهای محرمانه‌ای داشته‌اند./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/680281" target="_blank">📅 14:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680280">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه حمایت از کودکان مبتلا به سرطان خراسان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIra1MrhPoBWi_ttyH8-wrRBCi912BHkrrfqCdVHSBwzoYz7BujloyCqZdvJGJz7EQ-UpLeBxHQxwaZ4AhkGtiH3b5IQinMmgL8T-fFchP4TthJNJilEHBornozedJYTVzNhcFuiejVTt4G_b9hriqm_rOG15rYwT2kkGmnm_wU9PwGpT8iDfCvEXXghPYD4bETCCWZIDzSi1aVwrnGdIwoyJok37ARTvMtsbQpLRt5Di3DPcK_jeFqgOkNxT9ALKqUsowcN9TWoKTkZlbAcJW7a7bwSVFS8eW1dZJIBnB0Zmfz0sqDIc8rKT9HfbtoEdb4-X6EBOVMgh8W5eIiQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«برای بچه‌ها هر روز تابستون، مهمه»
؛ حتی امروز
🎗
با هر سهم ۱۵۰ هزار تومانی، کنار کودکان مبتلا به سرطان باشیم تا با لبخند سلامت روزهاشون و بگذرونن
💛
🔗
لینک کمپین:
https://sahm.khorasan-charity.org
شماره کارت :
5047-0610-9009-3739
————————————
💛
راه‌های ارتباط با ما:
☎️
051-31504
🌐
www.khorasan-charity.org
🆔
instagram:
@khorasancharity
🆔
telegram:
@khorasan_charity</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/680280" target="_blank">📅 14:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680279">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
مقام یمنی: ما هرگز درهای گفت‌وگو و مذاکره با عربستان را نبستیم
🔹
این طرف سعودی است که مذاکره را رد می‌کند.
🔹
صنعا به مدت چهار سال به آتش‌بس و کاهش تنش پایبند بوده و هیچ‌گونه اقدام خصمانه‌ای علیه عربستان انجام نداده است.
🔹
عربستان از فرصت آتش‌بس سوءاستفاده کرد تا عمدا وضعیت را در عرصه‌های اقتصادی و معیشتی به منظور فرسوده کردن ملت ما تشدید کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/akhbarefori/680279" target="_blank">📅 14:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680276">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fICUchnAPuW8I5ygiMz0_fu0nGiGFRRwwdCSyGXUVMqVTWSTCZ8K_eOmvJauIF4Wn26MGwDTvoyUW2G4tXwIUfghtcUB-fteDc8qZQN0wcPqD1sw7Fc2_kDtklb4TWLlFXmAEzZ9_RjIT7F5b7W9yr4T80Pj5XGnt9jSPGb57hMU83pYfXlRIVA7f6CWGTgfP5XrXhQMKVs1sCnHIKMOKGuLRwbbgdL8HmPxrP-mTYCdin62ngFRFy-_a6Tq4Q2OFW7MP7njvGdcQv7OQUXsezhpz6j-4ssHrpFZUiGCnuquLBZm_JYEuN2DRXBShP3QscAmV6RW3q87_x7X_hE2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8084ed1d3c.mp4?token=LrhUgaMIIz2k3b2hdimjAmK0S9fkYZ8D3Ygbp3_GtrCF6bvLRlfcZJFJjAy03rVLJ92x1vfpaIM8dzl6DwWED29nBd3Wru-aQd1q9JhxUtFl4PXTNz2SHxdjVih2CkLHPs4Yy9IQ__U6-7tjTfVTecm_htzI8f7pafR35mhfylBt8hkVdVrFVwc2E_8TjGWGtEqk0AxU7G8jmcDzllPRZH6_WsEEUosgUfzRqFP7lqdrcovtiU3l119n5bbC5YhihCYIQrvuk-EBbufSasaBC_KoCK3MrpJLcQYUe5OS16xsX24r3ffO1xGQz--VN9EXdsKcFiMOnNxGdta3gWBYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8084ed1d3c.mp4?token=LrhUgaMIIz2k3b2hdimjAmK0S9fkYZ8D3Ygbp3_GtrCF6bvLRlfcZJFJjAy03rVLJ92x1vfpaIM8dzl6DwWED29nBd3Wru-aQd1q9JhxUtFl4PXTNz2SHxdjVih2CkLHPs4Yy9IQ__U6-7tjTfVTecm_htzI8f7pafR35mhfylBt8hkVdVrFVwc2E_8TjGWGtEqk0AxU7G8jmcDzllPRZH6_WsEEUosgUfzRqFP7lqdrcovtiU3l119n5bbC5YhihCYIQrvuk-EBbufSasaBC_KoCK3MrpJLcQYUe5OS16xsX24r3ffO1xGQz--VN9EXdsKcFiMOnNxGdta3gWBYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاسیسات آرامکو عربستان منفجر شد
🔹
وزارت انرژی عربستان حمله به تاسیسات آرامکو در منطقه جازان طی بامداد یکشنبه را تایید کرد. طبق منابع عربی چندین انفجار در این تاسیسات گزارش شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/akhbarefori/680276" target="_blank">📅 14:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680275">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهشتم از فصل پنجم
🔹
اولین قسمت از روایت تجربه‌ نزدیک به مرگ آقای سید محمد موسوی که در میان انجام امور روزمره به ناگاه روح از جسم جدا شده و از طبقه اول آسمان تا طبقه هفتم را پیموده و در هر آسمان آثار تمامی رفتارهای دنیوی از جمله آزار یا خیررسانی به والدین، خویشان و حتی حیوانات را درک کرده و هر طبقه را با لطف و نگاه اهل بیت گذرانده و اجازه ورود به طبقه دیگری را پیدا می‌کند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید امید متقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/akhbarefori/680275" target="_blank">📅 14:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680274">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه قطر: مذاکرات میان عمان و ایران اکنون در مرحله پیشرفته‌ای قرار دارد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/680274" target="_blank">📅 14:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680273">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f478208a45.mp4?token=l5I7rbdDZSb-ulV7NSnNLK8C8UEeS2_GkwIdmLNe9rPsXqK3T0qlNk5XxHq55NlF-scYBow2z4pHRAx4zdpdGndkdWATuRfOVR7uqU0VzSJvWcBQjHQE0BBWX6hxwCGJNMNXZwz1O-aAF5d4AFHmOSjXibGYjLQBEwhvX7nx0B_kvwdBK6kUBbelS8x0VT4z1R3c99KikNPG-xv_GyYlSbcReH4fCSp760aXC7IA1ijIGZVFcDHj7rXPfJRd5FR60HJR0AaJ0JS2xcQ7oz-cDpSEEB4jR5gp7IxlNKI3egY-xfe7sPWWBXPdaaBSpz7DpnYqzfLh9iBucX3go784WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f478208a45.mp4?token=l5I7rbdDZSb-ulV7NSnNLK8C8UEeS2_GkwIdmLNe9rPsXqK3T0qlNk5XxHq55NlF-scYBow2z4pHRAx4zdpdGndkdWATuRfOVR7uqU0VzSJvWcBQjHQE0BBWX6hxwCGJNMNXZwz1O-aAF5d4AFHmOSjXibGYjLQBEwhvX7nx0B_kvwdBK6kUBbelS8x0VT4z1R3c99KikNPG-xv_GyYlSbcReH4fCSp760aXC7IA1ijIGZVFcDHj7rXPfJRd5FR60HJR0AaJ0JS2xcQ7oz-cDpSEEB4jR5gp7IxlNKI3egY-xfe7sPWWBXPdaaBSpz7DpnYqzfLh9iBucX3go784WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقتصاد رانتی و نهادهای فرادولتی؛ انتقادهای یک کارشناس اقتصادی از پدیده‌هایی که به گرانی ختم می‌شوند
/ تلویزیون اینترنتی مدار
بردار را در لینک زیر تماشا کنید
👇
https://www.aparat.com/v/zkahcd7
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/680273" target="_blank">📅 13:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680272">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d533c4997.mp4?token=g7XvF5zWJMeVvmgd5M5HNOK_RorjuyxSgo0QNGXm6a14b_KtL8D-uIjMfu8P7qdS9LVhVrzqSLF2YiFh7UMYpOyicYyjBLQkngG1yiux2zZ3sVb22_Rli4EGM_g5I4s94oQ53fHbc4Uz_EKjEwN5_bOOKLsgc9C3wr4LNeQUN6w0xd-ecJ0QYq30aqNrh6THX01kS_3zlOb0b4aguvV5WkEQpuTKExFtag0qlwYH4bgEe7vxPoH24MTAvUA741ZqWTf5H_6H03sZRmfrCTOxWdaGmUqnWzHyOGnarNOSut17Me3zweDrAJAB0omVmQhZ_ciiZ7s5UFMeeNQZGge9UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d533c4997.mp4?token=g7XvF5zWJMeVvmgd5M5HNOK_RorjuyxSgo0QNGXm6a14b_KtL8D-uIjMfu8P7qdS9LVhVrzqSLF2YiFh7UMYpOyicYyjBLQkngG1yiux2zZ3sVb22_Rli4EGM_g5I4s94oQ53fHbc4Uz_EKjEwN5_bOOKLsgc9C3wr4LNeQUN6w0xd-ecJ0QYq30aqNrh6THX01kS_3zlOb0b4aguvV5WkEQpuTKExFtag0qlwYH4bgEe7vxPoH24MTAvUA741ZqWTf5H_6H03sZRmfrCTOxWdaGmUqnWzHyOGnarNOSut17Me3zweDrAJAB0omVmQhZ_ciiZ7s5UFMeeNQZGge9UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دادستان قشم فرمان مهار فوری آلودگی نفتی سواحل جزیره را صادر کرد
🔹
دادستان عمومی و انقلاب شهرستان قشم با ورود فوری به موضوع آلودگی نفتی مشاهده‌شده در بخش‌هایی از سواحل این جزیره، دستگاه‌های مسئول را مکلف کرد ضمن شناسایی منشأ آلودگی، عملیات مهار، جمع‌آوری و پاک‌سازی نوار ساحلی را بدون وقفه در دستور کار قرار دهند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/680272" target="_blank">📅 13:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680271">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f436d1830.mp4?token=VYcSjVj8bLzPW-tEGKP7wUN6OodMZzw-GCeXMM0jephg_N9RhaglkpIhhBJ-hdfBfh8zc7SEkflK6azkXKGVsMPsYZehQlTHlEd_B3yhpOzXvnKkj_kT9y7Mya-93qou6hqrOTPR_SlGr0KMEysrIwAnDYG-8za0pRTWMXCMlRS7kNLupCAELjzdwOhVXukfRA9PyjCal84rDCp-q0gOMco1qNOsMdaLO4aQ75GLkuTKLe_Vr140QMtZf0jU-FPyHqmvn6JKXOa-YZpTzgdR9VHBUZPGyU7uNuH8l8MienXXyXvukr9VV0AEApV_7itI3Khpm4SmA3Kq_iFCi8zOYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f436d1830.mp4?token=VYcSjVj8bLzPW-tEGKP7wUN6OodMZzw-GCeXMM0jephg_N9RhaglkpIhhBJ-hdfBfh8zc7SEkflK6azkXKGVsMPsYZehQlTHlEd_B3yhpOzXvnKkj_kT9y7Mya-93qou6hqrOTPR_SlGr0KMEysrIwAnDYG-8za0pRTWMXCMlRS7kNLupCAELjzdwOhVXukfRA9PyjCal84rDCp-q0gOMco1qNOsMdaLO4aQ75GLkuTKLe_Vr140QMtZf0jU-FPyHqmvn6JKXOa-YZpTzgdR9VHBUZPGyU7uNuH8l8MienXXyXvukr9VV0AEApV_7itI3Khpm4SmA3Kq_iFCi8zOYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واشنگتن پست: ترامپ در ترکیه از ترس ایران با کامیون پذیرایی جا به جا شد  واشنگتن‌پست:
🔹
دونالد ترامپ، پس از حضور در اجلاس ماه گذشته ناتو در آنکارا از ترس تهدید ایران، به صورت مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه خارج شد.
🔹
طبق گزارش واشنگتن پست، ترامپ…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/680271" target="_blank">📅 13:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680270">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb9os0w_3r-XEH6qAzG1UJRCCpCazuLf7hzR-39A8ULgVSyFFtL1Kc_dF9_HYbXp3SmZQWfIEpj4N72kLsDvKGbb8W5yhkTUyt5tCD5z8PSa1tF4QL1f_iUgjG-p3xQuzvw1LFujO0tSW8QsbZFc9NvViXSvEzVUzT4PoWqqZzHHdz0nUfHSho37E4aNg6KAf2gPz76YQDUqry2azlzAwNa62Ncfam_PGdQ3ITse1qKUueluy34kx2yDFrUWC-DSi_ZNHF-a--w00pY-gCRe2FyE2gcKDcIX9XVdsFmpSCJJO_fWHE7elGKJBwPuL1Ft5pWYFHnXMZUEwSZQVq5n0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
بر اساس این احکام، سردار سرلشکر خلبان پاسدار علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح و امیر سرتیپ کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح تعیین شدند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/680270" target="_blank">📅 13:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680268">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D79nibzanWhf66jnYZmlL29wqMS5daMlmc16LaJxmNVAzxdIv6_AZa3qXYptKgz_4fZU7zxSvlxysiN079p_tRoa-0yy0USHd1hHrNWhCOebWpv49sBnrT23LuaSNUQB6e05kO30JPulUz57RMTN8RrblWUvdhE_zHuJMnjzZIQuSp62sYGn5wLGuU_axB0iljEWXA-NTofgDW9SfD1LhD0DoGDSgQZoir8bYIEu-u1hS3zFlzRXn0AmJwH_3dzhua0FTcB-v9jAYwAkHIBakiKn5wHX-6MbGemqy8yMslyU8bAheQRxRYBaCvzKlVY401ktKFCWpqBleOcg2J1jpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0oM5WFnXXaBt0n8om3SEQLwQ14HapJ99IbdkjtwEEcj0mmhHORu0uLsStdpACJH34n8SiliTNmZkNh0N5r9ocBrHK63guFccjAUrzgtVENHPfja-bF-J_Kw6DAEB2R70qoueSDXBNdV0BC9Vnz2eWPuR8eVmgi4Bahm8tGRaIQcj6VTWv-on00AGDguzHwggHvZ97oV2es5vVqgXxtVVlvizZBkwpWsJB-UU8aU7UlIIW_VZCV2O9f-zFsuZnN5QzuvKSTkRPVMWDllbjyTMPCz7mONuC4GGF9Dy-VeJd1cJfj21K4a6JUCQs9krCqOWKoB7xvFsQaY0ahEYUhToA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اصابت موشک به کشتی سعودی در باب المندب
ادعای کانال عبری زبان کان:
🔹
موشکی که حوثی‌ها شلیک کردند، به یک کشتی تجاری سعودی در منطقه باب المندب اصابت کرد که به کشته شدن سه نفر از سرنشینان کشتی منجر شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/680268" target="_blank">📅 13:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680266">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06149768b.mp4?token=LafomNVI30DPKSYiMPLXZ2InOdlKicO9-WjSzvjqpzVyiEpasUnEFRdh4GSeJPYe09a8mPTKjuQsoIIlBsEji89-2p1_nJOhKGMUbL3p5gIhAKPslk8NqwVXWcpLDMOC8s9jvBFr2paXgr0ShOdHusHrjZnCwnwEQk59nz7i29eoB4MKABd65otubuLw51NEUDVBaciijQD-RkMEo2vMir1Q93Dera07ib6fPLzON3mL3aJBpwQW3mUUQX9YV2tvV5lf0KasVM4pQMoqCCyi3TP4NQUoeKPd878BdZyWxM-TKWiFivLq-p4j4-Zw8v5Bme2nre8b3Eg3J93dr6MDhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06149768b.mp4?token=LafomNVI30DPKSYiMPLXZ2InOdlKicO9-WjSzvjqpzVyiEpasUnEFRdh4GSeJPYe09a8mPTKjuQsoIIlBsEji89-2p1_nJOhKGMUbL3p5gIhAKPslk8NqwVXWcpLDMOC8s9jvBFr2paXgr0ShOdHusHrjZnCwnwEQk59nz7i29eoB4MKABd65otubuLw51NEUDVBaciijQD-RkMEo2vMir1Q93Dera07ib6fPLzON3mL3aJBpwQW3mUUQX9YV2tvV5lf0KasVM4pQMoqCCyi3TP4NQUoeKPd878BdZyWxM-TKWiFivLq-p4j4-Zw8v5Bme2nre8b3Eg3J93dr6MDhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضامن آهو؛ روایتی که هوش مصنوعی دوباره زنده کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/680266" target="_blank">📅 13:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680264">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmvASZvgROLuSd_PTMX-CFr_zf3duJ-7Yiim9nupFPJdAA27MoLxgtaU7gxRpfbBMPZrr_WGwSxWkeGO2NQEQg35bdcSHJU0qgIeMWA-8J3E0DFAE9N6Db9QcYyoalKt2zmk33yC43VuXrgpkqjeqK2LfL6yNbmfYnhLLyqT3cBgJ-ldhdDwhu0b0Ngfyn6BBFBwa9fo3kSjx1npDjHGcxc37Gmc95G0vArTmhhTVx8iwQoBTiq8Jj1tdHgQtA1bmqOa2N191zpNdbBxybnT7Uxer8Jycruaph9OT3oKpnoraQ--aw8DxtMlbsA9OTBXimHWkariicC5BJoUssXu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۹۰ درصدی عبور نفت از تنگه هرمز
🔹
تولیدکنندگان انرژی در خلیج فارس بیشتر از قبل انتظار دارند که کنترل ایران بر تنگه هرمز، پایدار باشد.
🔹
عبور نفت از تنگه هرمز از ۲۰ میلیون بشکه در روز پیش از جنگ به ۲.۲ میلیون بشکه در روز در هفته گذشته کاهش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/680264" target="_blank">📅 12:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680263">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9561845d9.mp4?token=KZ82a8OO1eIx5CIonYQOwz9cCvoAhDEdBaOfjQxywuWQt18KVxrtvRmsVTRav2jBdjlDqPS-EOJmET-owcH8j2A6IN3BDSigg-WPv2y3LdjCRrc0sz6i6LgPU-fIIBvEcOLtW36Z0KDHoLCrZfp8mSCDPUjY3oA3Hv3xT6O8BLSUpW_a4Ozvgp4aJVR4miQ2gXT3eF26JScX24MP9mXZGjPxroUMMpQrJWQgNJ1yEJgT60hIsJVQpubXmQNtjD4iVXhSHcMpvS2B-j9Ld_UQhvTPJOrmo86jMBgEIoQWitw1O636haCo0gFEjtRA6Lmrof0MFIm0ykx7Yaa1i2kCNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9561845d9.mp4?token=KZ82a8OO1eIx5CIonYQOwz9cCvoAhDEdBaOfjQxywuWQt18KVxrtvRmsVTRav2jBdjlDqPS-EOJmET-owcH8j2A6IN3BDSigg-WPv2y3LdjCRrc0sz6i6LgPU-fIIBvEcOLtW36Z0KDHoLCrZfp8mSCDPUjY3oA3Hv3xT6O8BLSUpW_a4Ozvgp4aJVR4miQ2gXT3eF26JScX24MP9mXZGjPxroUMMpQrJWQgNJ1yEJgT60hIsJVQpubXmQNtjD4iVXhSHcMpvS2B-j9Ld_UQhvTPJOrmo86jMBgEIoQWitw1O636haCo0gFEjtRA6Lmrof0MFIm0ykx7Yaa1i2kCNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آپشن‌های ماشین‌های چینی تمومی ندارن
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680263" target="_blank">📅 12:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680262">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDGpt238vYOlQeq1Ff1s1zPamH3pwQy3PYlftgSd6V85pS2V3cGzo7vBtkQOfl8P7zSOkOIeszBpktTqdN_8gnwE2mq4zZukOJa-uQuWfaofJwLRscNiMKPYcCwXbOKProaAy1cKXWkAC0w3CgD2_oH57KeWnOBT7EGyMF5gwWxv3UTPTkNYC76wcYfT_jUpOPzrVy9eQ9ZU-jrrpyygx1k5Xy5VdA3Appg9vxMNfGRXsExPtpf0w1-9NeVm3TUg6usCplk18DGWogEQNNtiJWHuUItCngRLO31OxXF9FdjaJTbBaVPQYd7oVL_TxcfZjp50a2tuozkgzt_f5urARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/680262" target="_blank">📅 12:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680261">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEx41BSC9998ltvsvim5XrwgxEj8kKQGPRe4M6r5VUyMy94zvvQWNuEHQFWqirmHWPVQa563vpRVJDp6GAOMIkSwl7GmCg3eAb1bDUG26EzfPAdyzerTvVvqda1JXnab7UhdyRwqf767zAdDwRKWWg4JbyzFow6UhnkjOJuP2n6yvr6j5cjqsmTlIFSaac_zXu44yWGk6f1IXMxUVA6TAY6LgbLARYkS3YnIGd3MKq9j_PEhm3278Ej121LwCJo7k3ZJWB9CsdHq0LT_n1DVFSgFqJSyj1xhl5fis7menwUYmFYSYqzGfo5aJJRgjyHd2exMyXLkAVKQWsxphI4v0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همراه اول پیشتاز توسعه زیرساخت هوش مصنوعی
🔹
پایگاه خبری رویداد ۲۴ در گزارشی با اشاره به نیازهای زیرساختی هوش مصنوعی نوشت که آینده این فناوری برخلاف تصور عموم تنها در مراکز داده یا مدل‌های پیشرفته ساخته نمی‌شود و به شبکه‌های ارتباطی قدرتمندی وابسته است که داده‌ها را میان میلیاردها دستگاه هوشمند جابه‌جا می‌کنند.
🔹
بر اساس این گزارش، بانک جهانی چارچوبی با عنوان «4Cs» را معرفی کرده که شامل چهار ستون اصلی «اتصال»، «توان پردازشی»، «زمینه» و «شایستگی» است. اهمیت بخش «اتصال» در آمار کشور ما نیز نمایان است؛ جایی که تعداد کاربران فعال 5G همراه اول به ۴.۴۴ میلیون نفر رسیده و ترافیک روزانه داده در شبکه آن از مرز ۳۸ پتابایت عبور کرده است.
🔹
این گزارش تاکید می‌کند که ضعف در شبکه‌های ارتباطی می‌تواند ظرفیت کشورها را در بهره‌گیری از هوش مصنوعی به شدت محدود کند؛ بنابراین توسعه نسل‌های جدید ارتباطی، پیش‌نیاز اصلی برای ورود موفق به عصر فناوری‌های آینده است.
لینک گزارش:
https://www.rouydad24.ir/fa/news/465938
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/680261" target="_blank">📅 12:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680260">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X75AR_ubebKQ4O0p5WTdItySsEG9sswTqWgXeW4Wbi3gnsAxGz19E8ts54VldkNbL0wLsLIfs3sXuEBjqPBJp8cE0Nt4tsI8Z5giU-qitGXe1WnQnFnoviP-zBDgE_RshY7YIZW8-8BAleSxp7jvZn_6V3tbRAZ4XF1uI-_N6CVcd_QBYhy7B8k5BKHFbG184UR3ADyYDC2vfqQDf0hy5flsjh3R54XqWBb9EcV58OZrBjnax8xhgCFo109Kzz5_v8EOrMvrkI5v6VhNsOHIQfNcgOEmfU4ejfKXj4hITmhv-OmFfTcNfqC5VxdbeOif210v3ERcmVVRmn5mTlfjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با رکورد جدید هفته را تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۲ هزار واحدی به ۵ میلیون و ۷۳۷ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/680260" target="_blank">📅 12:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680259">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر ارتباطات: با قطع اینترنت، امنیت تأمین نمی‌شود.
🔹
استانداری خراسان‌رضوی: ورود ۶ میلیون زائر به مشهد در ایام دههٔ آخر ماه صفر پیش‌بینی می‌شود.
🔹
فرمانداری سیریک: انفجار کنترل‌شدهٔ مهمات امروز در بندرکوهستک انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/680259" target="_blank">📅 12:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680257">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ac9d060fb.mp4?token=pxgz9BZOdJ6XbVY7eAsOyxLVoB4Y6R5bzw2IGeqZWkZRP5k8DCBb2zHq0-CXCsHyRFzfrBdxAfnyVIbl8UxmrXdv7BSUNYi1eocDMwviC5i8a9JodUtreazh72BvccDKkb73IXA7IfimnHPo-dKZBmduAhv1FIL9liLBeZxd8L42Leunu99XX9xreh2mkO0Xj2isbI8_Wexwm7De6xhFs_2HzTmj8s8nC4ERAVvRkMwME3DujWn6wTvD6j6JeEUre_djB2mxrsr-WlwGB8-zQLTNRSHzG-zd5wF3th9GZlR1AaV7rh1ZnR4QI3_NiwGIwiMdr65verhNZBDzWT8FAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ac9d060fb.mp4?token=pxgz9BZOdJ6XbVY7eAsOyxLVoB4Y6R5bzw2IGeqZWkZRP5k8DCBb2zHq0-CXCsHyRFzfrBdxAfnyVIbl8UxmrXdv7BSUNYi1eocDMwviC5i8a9JodUtreazh72BvccDKkb73IXA7IfimnHPo-dKZBmduAhv1FIL9liLBeZxd8L42Leunu99XX9xreh2mkO0Xj2isbI8_Wexwm7De6xhFs_2HzTmj8s8nC4ERAVvRkMwME3DujWn6wTvD6j6JeEUre_djB2mxrsr-WlwGB8-zQLTNRSHzG-zd5wF3th9GZlR1AaV7rh1ZnR4QI3_NiwGIwiMdr65verhNZBDzWT8FAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ، آخر هفته در زمین گلف خود در بدمینستر، در کنار یک سامانه پدافند هوایی کوتاه‌برد AN/TWQ-۱ اونجر (SHORAD)، گلف بازی کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/680257" target="_blank">📅 12:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680256">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2109fd84ca.mp4?token=qC6ELezqVhJPsSc6rumN8thKY5hUqiM1CDiMRW3HqVxBqD1T9YfvhrfBGAWEFXDuwJTGY6i_qKylcGXCuq1dA4ujqlVBy6pNyD4z22EPYFYofaEJp6Odwpb9Dz6PBNbbdmJ1yIA_qbtVas33gzR1GvK7s3NnpEdflbJggXTtLIzPu6eA9eGyoMZp-aSiq2ei0ISRhyGGR09DG4FIMf3QY8rUjeCcC5yzuk7a4NUTj9Y9cDvXZFwOb5OM_QR5esUKw54rgvgyCyuxevy6A6DyMo6MBFA9FhCpreY7Qet2_AlGc-EsxcQBiqfR_HMhFIEiwa2bfIE03doiK0p-TU2bfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2109fd84ca.mp4?token=qC6ELezqVhJPsSc6rumN8thKY5hUqiM1CDiMRW3HqVxBqD1T9YfvhrfBGAWEFXDuwJTGY6i_qKylcGXCuq1dA4ujqlVBy6pNyD4z22EPYFYofaEJp6Odwpb9Dz6PBNbbdmJ1yIA_qbtVas33gzR1GvK7s3NnpEdflbJggXTtLIzPu6eA9eGyoMZp-aSiq2ei0ISRhyGGR09DG4FIMf3QY8rUjeCcC5yzuk7a4NUTj9Y9cDvXZFwOb5OM_QR5esUKw54rgvgyCyuxevy6A6DyMo6MBFA9FhCpreY7Qet2_AlGc-EsxcQBiqfR_HMhFIEiwa2bfIE03doiK0p-TU2bfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استفاده از آب‌پاش علیه مهاجران در مرز لهستان
🔹
نیروهای مرزی لهستان برای دور کردن مهاجران از مرز، از خودروهای آب‌پاش استفاده کردند؛ این اقدام با واکنش‌های متفاوتی در فضای مجازی همراه شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/680256" target="_blank">📅 12:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680255">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اتومبیل کایزر دراگون؛ خودروی کمیاب ۱۹۵۳
🔹
اتومبیل کایزر دراگون (اژدها) در سال ۱۹۵۳ تولید شد و تنها ۱۲۰۰ دستگاه از آن ساخته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/680255" target="_blank">📅 12:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680254">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52844ba385.mp4?token=tOk593Bsj1rZm-kjxpiKwixwk4MJgQRPnp-COIAAITyrUH-poOOG6YQ_1np5dGVDXsbO70r-EE2vETpwJH1i1o64wKveEZ_58aOwI2ER5tTWrw3TcVNF7i8qF65269qnk-is7oEaT3ida800kNbp8VHFplDX4lyfxDAfA1XnzqV3BgwWJD4eGzkWX5Q8-a38sH83v_CNwfEO4DTNPTW9vbDUy_ibkVjDPDbrRGtYBNwutSV91PsitcWdsE5kSUPG8fWogoeCyOQsJNDTlvCoXTGXmg8M77FxBWIlRY1LJ0XBA5_3RnQuHEZaw0bGMeC0Yrkm7lzFFq9u6mfWTM10GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52844ba385.mp4?token=tOk593Bsj1rZm-kjxpiKwixwk4MJgQRPnp-COIAAITyrUH-poOOG6YQ_1np5dGVDXsbO70r-EE2vETpwJH1i1o64wKveEZ_58aOwI2ER5tTWrw3TcVNF7i8qF65269qnk-is7oEaT3ida800kNbp8VHFplDX4lyfxDAfA1XnzqV3BgwWJD4eGzkWX5Q8-a38sH83v_CNwfEO4DTNPTW9vbDUy_ibkVjDPDbrRGtYBNwutSV91PsitcWdsE5kSUPG8fWogoeCyOQsJNDTlvCoXTGXmg8M77FxBWIlRY1LJ0XBA5_3RnQuHEZaw0bGMeC0Yrkm7lzFFq9u6mfWTM10GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی پنیک‌ها خاموشن و هیچ علامتی ندارن، اما می‌تونن از درون آدم رو‌ مورد حمله قرار بدن #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/680254" target="_blank">📅 12:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680253">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQQm2pFdvoVLAdSXD83nDPbyQjdpch4T7e9STVvPn1xkur4bx5S-u5h0-0ZsfHJdUH0NMf2l5o8VJJZK2-9tjW-Z1bc17esW38eQrSONUr3ZfWcJ3cQtkJIuEuaJC3TJNjtdLV2i87cCIYp0XVp_1ZN7UvNNaUuxDQlDhkfpReUREMQFS18R9QLqCU7GWXlAoR5yqXLFMykI0-GKqK5x9kBvWeRk5YflI8M2sr9N1WewUeUdkbYqFsNZiAk8NbF89hfQiW89pzxVslbYJAMcV8P137p5r-6zhaf1YaIoVbNcXxcFujmZqq2ERisxeIXoEtslZZ1SntC0T6jU-Sps6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون قرعه کشی، 50 دلار برنده شو
🎉
۵۰ تتر سرمایه معاملاتی، برای کاربران جدید ورسلند که باهاش می‌تونی  ترید کنی و سودش رو برداشت کنی
💸
🔻
فقط کافیه ثبت نامت رو تکمیل کنی و به صورت آنی، 50 تتر رو دریافت کنی
🔸
بدون قرعه‌کشی
🔸
بدون واریز اولیه
همین الان ثبت نام کن و از 50 دلارت استفاده کن
👇
🔗
ثبت نام در 5 دقیقه
🆔
https://t.me/versland_io
🆔
https://t.me/versland_io</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/680253" target="_blank">📅 12:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680252">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k54aBWs5Gac2JL2Q4AH_5TcsOIhRG8p93fkf3gVFSaVKWiFmN95ndQbRbTDzCYWuM0KjhWWv4Vm2Dv4t3X-P7dX02oP87q4qM4DNR5FXR2SGNoUEr6KxTieNdHHgARXFxV67t0K85bOBeR8S34wuZRNNQOiwP5NfAEzTio-aXQ4MClsVunbTdNi6ILK1i7TwYfmgv3cktu2s7SfDhdLkeWVErsyxinpj6OVhQ2Eb-P1vPbvv49OdyaAJ5fOetV_A2VvpIk4jalYO9jt8-dvi85_2cTunGei0yrMBt3MxUeUwuC4ekh8Z4KxOy2fUoUnlaGqm74YCdf46K_gNbM2G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بشار اسد به اعدام محکوم شد
🔹
دادگاه جنایی دمشق بشار اسد رییس جمهوری سابق را به صورت غیابی به اعدام محکوم کرد‌.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/680252" target="_blank">📅 11:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680251">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAh_-Jztut5HXf0LBg-pS1nqWgqIyk0nb6bclEVTPzgXU9D5s8IlDy4PyygCz9dInohpQMTj-VNAc5RJSXhhNvGTuirxCKBirUamOeuoDm_A1THFEKSP8n5bXfx60nnnZIKh3ex_7botc3-3HH-Dvoo-o_lhPKBLVcKINS6tuZrzqfIf7i5o_vmpQ2DlMXe3hLcBhDSDG0mD7pv7dJxUCFnflWVDCB-n2T1AB6oVLQDhrK4-jI_Q-WEwmGqiKmGr7POKrN65LLfRyL0thnb1OCIrTtkoDx2jP1w3oCpoNiMX30cFfcQrh7o3riAnQV4LADPxkVYZ8ylAomfVg7GQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت از زیر ۸۰ دلار به حدود ۸۹ دلار بازگشت و به مرز ۹۰ دلار نزدیک شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/680251" target="_blank">📅 11:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680250">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف در نامه‌ای به پزشکیان خواستار ارائه فوری لایحه اصلاح قانون بودجه ۱۴۰۵ برای تطبیق بودجه با شرایط جنگی شد
.
🔹
استانداری آذربایجان‌غربی: حجم آب دریاچهٔ ارومیه نسبت به سال گذشته افزایش ۷ برابری داشته است.
🔹
وزیر بهداشت: شرایط موجود کشور برای حذف ارز ترجیحی دارو مناسب نیست و نیاز به بررسی‌های بیشتر دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/680250" target="_blank">📅 11:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680246">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RykvMyrkPQRpvOPqxnddRxNOQi3hsvw_l-qYHvE_6GtVaYKghW1egUw7QX-_mJ9-Qj0rdABKJwTy5cAVL_1BkHKlzWd8H3dD5YDxb_2vemQK_G-2mU90o5mXf0pJNaf418sSS_6uQZbZdGI5k--CV8gVZJ-JKfSjmcGqfXCHYbL-7WMQpRLSS6Yh-_GyYg7cYbkfr_WJaCcG611Tu-4g0HpcN9C6sH-yFyp41uPQjNOEIVu26aEaVT1nOEbixUmcTU9IqJs6H4KQkLAXX5KRO6Rew3SlfXWU0UnkDp1pk04B9G-eetfgJmfNKoWAfbKQX3LZ_Azx-rT7339_FzbriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRHs8ZMTVyzTtIMUfOIf-CD1QoX8iGrZBAk0QEZglZq09qpnJ0GG3xW-2Ez_NhKWvvCHX7tK2k-4r6yzNQmIlD-1-M2VcwEvl51s6yPmcfGet_E47HhhDaeETEMsdz6pFzzPbxXhibMaZgfsjst3uM5tl9CP0oLuFLw1r1DdEc7M4o8HXAypVmHJRxAhmJYS9l4rPLNchtiGCVIqxVCWChqhodOiSHhaUaxqgYeFl5s0EOSyAAa2ANtGAMOXQghQ3M1-u7bN9rv2TYn__fP-l1_Nsda8Dwb6gdcXCuHW3kWzqa4Q3RMSQnPQ52dzFkRIOSorDSP2szxv5cZuSGH6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVzczK5e9mjIwi20UNsKISMFA_b4lCWOj3NcAte5YgEhfxhKbp7Fdu062LYqFmjNhMHtN_GBGlMvN3pD3WSyhfZEd-kbNEvm08ogQowjpxo3OllD7QOCVtjaTcO4A9j-NCebA2mEYs2CI619r0v2J8OpTPsrl6nc65HNkI14MZ0Fen1vvi3FFAfZ7DyjPQbLiWpZcpybQGlQiUgi0FInTHrc1Le6LJdVenQHQkGr3rTSveqcoCUHVl4Wdd7eBwJJuNwYA12yyGQNzW4aDRJMG1CebUZ7IDMYhDezWaNo1Nuziuqfsq6y-BS3Wyl0lhD-ndYjZO_DLOaovmuGEaqM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDqCPpLfOXPf04QY8gVc5NUlhQlS99hQyjWWDeoHyO9RSdzJ_6us8LzRWNeU7cbKu7M-JChx6O82xVvpeS6iB6DPMBA1Nq9hByYr8yys1-6AlXqTa_YS0yILV4817YcsdFGJn6BPOJsMZQWdXLwnxM4l2fUj7CSd-XvLFP4Ez8Lu46VWSdBCp77cuTEdUxSOZf6abEKsqaV8NFqkEzoEQ00oQTmKnvpy1UfHbCnd2MMKkLEGxmqhrdgMhUL-X7jhZQ-sXd6axQmIre76hRjHWX5mhZutPTGovpT9-xNuCQrYgbLHJJp3tMUNne1CCG5MP-MYc5GzVqSxxcG619dsJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گوشی‌های جدید سامسونگ وارد ایران شدند
🔹
گلکسی زد فولد ۸ اولترا (Galaxy Z Fold 8 Ultra) با حافظه ۲۵۶ گیگابایت و رم ۱۲ گیگابایت که جزو گران‌ترین‌ها به حساب میاد، حدود ۴۳۷ میلیون تومان قیمت دارد.
🔹
ارزان‌ترین سری هم، گلکسی زد فلیپ ۸ (Galaxy Z Flip 8) با رم ۱۲ گیگابایت و حافظه ۲۵۶ گیگابایت، از حدود ۳۰۰ میلیون تومان شروع می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/680246" target="_blank">📅 11:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680244">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
کاهش تردد کشتی‌ها در تنگه هرمز
🔹
تردد کشتی‌ها در تنگه هرمز روز دوشنبه به ۶ فروند کاهش یافت؛ در حالی که میانگین ۱۰ روزه حدود ۱۱ فروند و پیش از جنگ ۱۳۰ تا ۱۴۰ فروند در روز بود.
🔹
داده‌های کپلر نشان می‌دهد سه‌شنبه ۴ کشتی وارد و ۲ کشتی، شامل یک شناور LPG و یک کشتی حامل سوخت، از تنگه خارج شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/680244" target="_blank">📅 11:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680243">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVIG8JLScQMZK1uoTQ-gV_G5VTb-rEFQw38hW8wM3ENB6SQDOKlVP1CX7icFnAFPEDnLj2lfWnPYSKW5SNKKr-W9pKklF1BKKMsUqLGHu7OMFV9_f2BLlYt5QEocIuEXBitxvvtHA7GA3-waBT8DiaUB3IE15agCKUkdEgxehiN1X9cj49o7Y0s3EAbB79d-m3AvefjNSRDrA0OsZmkxcDmE8G4Sat44cEml3lH676VDrWQj-Y9D4lkHGP_f2DTnP86HRSktO7gBxSuEFzV0kSKfERfxJc2j-rbS3H8MO75IcAsIM0wv0fVDyOodEHOOzJo5jWxpqboLTCPkEcMjfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از سقف عمارت هشت بهشت اصفهان
🔹
علی آذر
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/680243" target="_blank">📅 11:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680242">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358c82a18f.mp4?token=VVgZPkcg7w45STrPnUiTEvi_bvpLVW235AcsWfXQlAs67wZ51b8taDOKgUqkZFsC_Yy-6pfoZxQsFHqqOmRVv173Pxh6vc6JBolFbLIj_Zd9RiAo6uSwUbiKzRq-zvL7jODocE3HIjVUQwXRrgNT-L8Aa-Cpd0aMBv7gztQKsaWFiFFb1IGEeahcZbRceMpdom1uqRYmPEOZkn5r_bj-44kL_Y_pq64h0gIecyf8WYLndGHueiMg7im3Lnf2moYOWFYAYi2_n9Pq0mwQ6LclitTFvgc_omIyraLqsbx4NySshOflw8eVSu_TeoT81_L3rJrK53Gvw3b_p-uJsJUMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358c82a18f.mp4?token=VVgZPkcg7w45STrPnUiTEvi_bvpLVW235AcsWfXQlAs67wZ51b8taDOKgUqkZFsC_Yy-6pfoZxQsFHqqOmRVv173Pxh6vc6JBolFbLIj_Zd9RiAo6uSwUbiKzRq-zvL7jODocE3HIjVUQwXRrgNT-L8Aa-Cpd0aMBv7gztQKsaWFiFFb1IGEeahcZbRceMpdom1uqRYmPEOZkn5r_bj-44kL_Y_pq64h0gIecyf8WYLndGHueiMg7im3Lnf2moYOWFYAYi2_n9Pq0mwQ6LclitTFvgc_omIyraLqsbx4NySshOflw8eVSu_TeoT81_L3rJrK53Gvw3b_p-uJsJUMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلا چطور جورکش ریال شد؟
🔹
وقتی ارزش ریال پایین می‌آید، پول مردم کجا می‌رود؟
🔹
مهرک محمودی و ملینا جعفری از تحریریه ماهنامه پیوست برای آرش برهمند از عددهای بالای تسویه و برداشت در پلتفرم‌های آنلاین طلا، از جمله طلاین، می‌گویند؛ عددهایی که می‌توانند نشانه‌ای از تلاش مردم برای حفظ و مدیریت سرمایه شخصی در روزهای بی‌ثبات ریال باشند.
🔹
اما یک سؤال مهم‌تر هم هست: وقتی طلا از گاوصندوق و طلافروشی به موبایل ما آمده، آیا فقط شکل پس‌انداز عوض شده یا بخشی از کارکرد پول هم دارد به پلتفرم‌های طلا منتقل می‌شود؟
🔹
روایت «پیوست هفته» از بازاری که این روزها طلا در آن فقط یک کالای سرمایه‌ای نیست؛ گاهی باید جور ریال را هم بکشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/680242" target="_blank">📅 11:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680241">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: تورم در بسیاری از استان‌ها، ۱۰۰ درصد است/ فکر می‌کنند با اعلام آمارها، فضای روانی جامعه آشفته می‌شود
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
دستگاه اقتصادی ما نتوانسته کارش را خوب انجام بدهد. همه گرانی‌ها ناشی از جنگ نیست، خیلی از آنها ناشی از سوءمدیریت است.
🔹
رییس اتاق اصناف کشور روایت می‌کرد که همزمان که یک کالا از یک زنجیره به زنجیره دیگر انتقال داده می‌شود، یک فاکتور الکترونیک می‌دهند و یک مبلغ دیگر در کنار آن ردوبدل می‌شود؛ این بدان معنی است که رانت و فساد انجام می‌شود.
🔹
مردم از ما بیشتر می‌فهمند و می‌دانند و راهکار این نیست که پنهان کاری کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/680241" target="_blank">📅 11:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680240">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کارت کنکور سراسری سال ۱۴۰۵ یکشنبه منتشر می‌شود
.
🔹
هشدار آب منطقه‌ای تهران؛ همچنان در دوران خشکسالی هستیم.
🔹
سپاه اصفهان: احتمال صدای انفجار کنترل‌شده در صفه و بهارستان تا ساعت ۱۴.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/680240" target="_blank">📅 11:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680239">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4dd75d13.mp4?token=H1wDdeOi_WWS9hBQTNn8hUltyXx6Pece5IbwZZbgEzIbsz2PRTPxpTYgw2AOwA3Hjyt84EMGhO-5TFlwkLRGAPnW9VtNbm1pnFmA5OCSbXb_7wjrdl5iKw0Ony3q7RHgWet8bLj7InnX2UrRSSo9emVytrmpzixMYisL5qRMPpCzoWCvTWgaRbfkicgy46sPldH443fPOrovMIOeGqSXADd8mCnU1atwz1W4K5b4tf8eccugotamPsEHbCr7YjAgA9sg63qFjaRA6rp0uWOmhF3HQOVf8zxRReRVt96Ii1l1ZKwiAbjkAKh8gzbFnlPR-s2Z3O9fpwoxg_0E-bHdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4dd75d13.mp4?token=H1wDdeOi_WWS9hBQTNn8hUltyXx6Pece5IbwZZbgEzIbsz2PRTPxpTYgw2AOwA3Hjyt84EMGhO-5TFlwkLRGAPnW9VtNbm1pnFmA5OCSbXb_7wjrdl5iKw0Ony3q7RHgWet8bLj7InnX2UrRSSo9emVytrmpzixMYisL5qRMPpCzoWCvTWgaRbfkicgy46sPldH443fPOrovMIOeGqSXADd8mCnU1atwz1W4K5b4tf8eccugotamPsEHbCr7YjAgA9sg63qFjaRA6rp0uWOmhF3HQOVf8zxRReRVt96Ii1l1ZKwiAbjkAKh8gzbFnlPR-s2Z3O9fpwoxg_0E-bHdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ شیاد : اگر من نبودم، ایران به سلاح هسته‌ای رسیده بود؛ مجبور بودید آن‌ها را « قربان» خطاب کنید
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/680239" target="_blank">📅 11:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680238">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6ca5ca28.mp4?token=uut-sp0MGMxuMbkVdSBWpNa3bI4gmDR0RlZNDkqoHmsnKMzC_0FI7u6GB6beuwVr3PnYzQS3IEyT4ahdzku4XdfButQsPeyzL7a5YumMvor9xuWu_jdkD8Vcskx_R86YEtQBgL_DBzQBbBDVUvpWy48kVRsdVEh7GA4n3cLLt18S9cCfG_4iEJFSBdB-ZjB2lSN_51oTm-o9itZCQJeQF1msfyAGrdBA5THFZDX3ULIAtmcQVyKQvPuOclIPC9BPGqvJg9qhAm2MxRKxxSRl570npmSeN8bXVFj-ecemmGVTZmB0pJnN6XxOWzjryhud7wdPxU-Co1wjulKyNjEBCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6ca5ca28.mp4?token=uut-sp0MGMxuMbkVdSBWpNa3bI4gmDR0RlZNDkqoHmsnKMzC_0FI7u6GB6beuwVr3PnYzQS3IEyT4ahdzku4XdfButQsPeyzL7a5YumMvor9xuWu_jdkD8Vcskx_R86YEtQBgL_DBzQBbBDVUvpWy48kVRsdVEh7GA4n3cLLt18S9cCfG_4iEJFSBdB-ZjB2lSN_51oTm-o9itZCQJeQF1msfyAGrdBA5THFZDX3ULIAtmcQVyKQvPuOclIPC9BPGqvJg9qhAm2MxRKxxSRl570npmSeN8bXVFj-ecemmGVTZmB0pJnN6XxOWzjryhud7wdPxU-Co1wjulKyNjEBCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: در جنگ اخیر نیروهای مسلح ما جانفشانی کردند و بزرگ‌ترین ارتش ظاهری دنیا را عاجز و شکست دادند
🔹
این اصلا شعار نیست؛ یک واقعیت است که همه دنیا به آن اعتراف می‌کنند.
🔹
در جنگ اخیر، جمهوری اسلامی ایران خود را به دنیا ثابت کرد و نشان داد که یک قدرت سرسخت…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/680238" target="_blank">📅 11:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680237">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee2a327f6.mp4?token=J0xPa9oBDMXEKZJt9kLwJ8k1Hb5Rk3NXoJunguXVVDrS3Z1nMT70IWJVHgIUU1XLO0mfd06UsYlMqMiPhoOvyhGiB7WVOJSKAC72KBU4LnaTB0Z6QoTg-x2YEAOK-hRcinbOPcyPwWvta1272divphT2kquEc4slTYLFInL0ESA2nErvAyfUbRGLtTgkXs3kgeCId3_4xCS2RECHiM0sSmhrJZ1STHOy3dBJpyKyFOaa56WGnrIe2t-DeR8nuu4E9D_MtY3dsnFOdkISE3WcSr4gpkoQcGoySRooLK_EXxkvsXVMYCdI7l_wf3RxZarXs9TyRM4mayTnW_cNl9GbFA3qe_axMpabqzQxawzpOCQ1KqDJXA_ULi6AAguaE3xS5pfmGs8J8WekYeU1M9b_WEYGlrudMEzgQZy9DfeoPIYpzaCqhjrfhQXymhuhpkcfLy_vrtlkCZ11BgQr_q9HdeNTWh1oVL_BFKbB24hmNt2GRYqJNCh1IQKA_6T_DDX9c_b-5qr-PdJuf4W45BjkmAQJu1qYdp-Yt5ezi0iRYpUwOZho2oVnjP95LQdmAAulbUfiYOkET5bkVMHqCNbLZI2wuHFBlQWO60pod6SsFul9Pa-VsKw6cWM7oq2jqzeCqsjgQnR31Um4kHWkowFLZ7PbWsCinmIEwu01WgUWY0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee2a327f6.mp4?token=J0xPa9oBDMXEKZJt9kLwJ8k1Hb5Rk3NXoJunguXVVDrS3Z1nMT70IWJVHgIUU1XLO0mfd06UsYlMqMiPhoOvyhGiB7WVOJSKAC72KBU4LnaTB0Z6QoTg-x2YEAOK-hRcinbOPcyPwWvta1272divphT2kquEc4slTYLFInL0ESA2nErvAyfUbRGLtTgkXs3kgeCId3_4xCS2RECHiM0sSmhrJZ1STHOy3dBJpyKyFOaa56WGnrIe2t-DeR8nuu4E9D_MtY3dsnFOdkISE3WcSr4gpkoQcGoySRooLK_EXxkvsXVMYCdI7l_wf3RxZarXs9TyRM4mayTnW_cNl9GbFA3qe_axMpabqzQxawzpOCQ1KqDJXA_ULi6AAguaE3xS5pfmGs8J8WekYeU1M9b_WEYGlrudMEzgQZy9DfeoPIYpzaCqhjrfhQXymhuhpkcfLy_vrtlkCZ11BgQr_q9HdeNTWh1oVL_BFKbB24hmNt2GRYqJNCh1IQKA_6T_DDX9c_b-5qr-PdJuf4W45BjkmAQJu1qYdp-Yt5ezi0iRYpUwOZho2oVnjP95LQdmAAulbUfiYOkET5bkVMHqCNbLZI2wuHFBlQWO60pod6SsFul9Pa-VsKw6cWM7oq2jqzeCqsjgQnR31Um4kHWkowFLZ7PbWsCinmIEwu01WgUWY0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروگان‌گیری در پایتخت
🔹
صبح امروز در پی اعلام یک مورد گروگانگیری در خیابان ولیعصر، بالاتر از پارک ساعی، موضوع از طریق مرکز فوریت‌های پلیسی ۱۱۰ به پلیس گزارش شد.
🔹
در پی این گزارش، تیم‌های تخصصی رهایی گروگان، سرکلانتری و سایر نیروهای انتظامی در محل حاضر شدند…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/680237" target="_blank">📅 11:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680236">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4979d719f8.mp4?token=c3LtkRv3JNhuRFgtrFjtQMPQBXGIC93hJIp5r1EmfzmhBVdvINAW-RiB-T-_BJ9anSNHHfSr8c7EZrsE5EgcLjl33HLklv9C4xiCXFe4fOQWonGgcFLQQ71osKirwjrCugyEzDLYeHr5lIuqmI501CodtQi24ew-Qr3PSIPn7yFwMld87DXkqLt_kccAaZUiGNXtR_oymiXMOj9N9uHWI4XdPrWsSfs1wMa_bwO6efD-aSxSoPB-betXHGDMaIUYOCyljV_bWdHepe_X4VmXtBgCJUxqqLP45orf5EFeA1q-YYz_q9hkMf3plchHwmsRLp95zqdU8aKhBGpykSXFkUQgCdMLa7234-O_4ij1yDVKY4AbmDBvb2zle77iAeH6Hcf65JNiL34MS9hrK1Cb5zGAbKYd1ltvJIfbbNQ4h7M3iqU1Vodknq6v335XFq_zfaq7ykrMxiZ3YWltTsEr0dipuXH6xZ3V7KZNSugqMKZxn5-2wUrLTGl0Ms2JjSNtxDj1iCUWHPJtRI00Ja1lUxJUfe4_N3QBcKhPAyjrmTzsfZb-hPjdsURtTwlytrnYgoa9kh1ePH8kXACMGfRObdp83cB9d4_VRTFgHoMKkrauCfYVAsiYOrBQQvtSh7EE5Xf2D9riTh2q_RAGi3mcxGIj2N9FxlBpv6OW9QQftiM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4979d719f8.mp4?token=c3LtkRv3JNhuRFgtrFjtQMPQBXGIC93hJIp5r1EmfzmhBVdvINAW-RiB-T-_BJ9anSNHHfSr8c7EZrsE5EgcLjl33HLklv9C4xiCXFe4fOQWonGgcFLQQ71osKirwjrCugyEzDLYeHr5lIuqmI501CodtQi24ew-Qr3PSIPn7yFwMld87DXkqLt_kccAaZUiGNXtR_oymiXMOj9N9uHWI4XdPrWsSfs1wMa_bwO6efD-aSxSoPB-betXHGDMaIUYOCyljV_bWdHepe_X4VmXtBgCJUxqqLP45orf5EFeA1q-YYz_q9hkMf3plchHwmsRLp95zqdU8aKhBGpykSXFkUQgCdMLa7234-O_4ij1yDVKY4AbmDBvb2zle77iAeH6Hcf65JNiL34MS9hrK1Cb5zGAbKYd1ltvJIfbbNQ4h7M3iqU1Vodknq6v335XFq_zfaq7ykrMxiZ3YWltTsEr0dipuXH6xZ3V7KZNSugqMKZxn5-2wUrLTGl0Ms2JjSNtxDj1iCUWHPJtRI00Ja1lUxJUfe4_N3QBcKhPAyjrmTzsfZb-hPjdsURtTwlytrnYgoa9kh1ePH8kXACMGfRObdp83cB9d4_VRTFgHoMKkrauCfYVAsiYOrBQQvtSh7EE5Xf2D9riTh2q_RAGi3mcxGIj2N9FxlBpv6OW9QQftiM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ کمبود مهمات آمریکا را گردن بایدن انداخت
ترامپ شیاد: بایدن با ارسال مهمات به اوکراین، ذخایر آمریکا را کاهش داد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/680236" target="_blank">📅 11:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680235">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a073856ca.mp4?token=Ytc50QqSvvv0jEQBdskVG9Q1Um4KEBYs8gHnF4Gz3mPYciRourVPO8fv8hXHMW0Nd6bvqggJtyD6jQnXmfM7N5lgXUBMlqE53MErf5htZtnB-DQdZpEbNwJhV2ZjOcJ1ssWWjOcIKKmPbYfMD-g01X41gVAsr_txz1oUkpYwnS4aNicV40MgNKh7yC4fTLgmqKu4XsnVkbaAJLEQxlM6KRK7TnYWWLHTMWjwuS9DCDMYj0JWO_xkGAKaR_-qZyI42nlM6m-P2W6VXFd3o_tR9bpTs67zAyEKu8AGl4xaw_v0ViFxLaVTTBkPzRWE1MoqCfIhahEgT9rSovzi26FxFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a073856ca.mp4?token=Ytc50QqSvvv0jEQBdskVG9Q1Um4KEBYs8gHnF4Gz3mPYciRourVPO8fv8hXHMW0Nd6bvqggJtyD6jQnXmfM7N5lgXUBMlqE53MErf5htZtnB-DQdZpEbNwJhV2ZjOcJ1ssWWjOcIKKmPbYfMD-g01X41gVAsr_txz1oUkpYwnS4aNicV40MgNKh7yC4fTLgmqKu4XsnVkbaAJLEQxlM6KRK7TnYWWLHTMWjwuS9DCDMYj0JWO_xkGAKaR_-qZyI42nlM6m-P2W6VXFd3o_tR9bpTs67zAyEKu8AGl4xaw_v0ViFxLaVTTBkPzRWE1MoqCfIhahEgT9rSovzi26FxFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هانتر بایدن: نتانیاهو تجسم شرارت است، دیگر نمی‌دانم به مردم چه بگویم
پسر رییس جمهور سابق آمریکا:
🔹
واقعاً چشمانتان را باز کنید. برای یک دقیقه قلبتان را باز کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/680235" target="_blank">📅 11:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680234">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رسانه‌های عربی: یمن به یک کشتی عربستان حمله کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/680234" target="_blank">📅 11:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680233">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
عراقچی: هیچ‌کس فکر نمی‌کرد که ایران دشمن را مجبور کند که برای مذاکره درخواست دهد  عراقچی:
🔹
هیچ‌کس فکر نمی‌کرد که ایران بتواند این‌گونه در مقابل آمریکا، با همراهی رژیم صهیونیستی و حمایت بسیاری از کشورهای دیگر، از جمله کل کشورهای غربی و برخی کشورهای دیگر که…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/680233" target="_blank">📅 11:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680230">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEJfLubjWESKU_7yjZGkalWn0CgjjjuxIPhPWeqX9bus17IyYrD5__oGk2a9isYmHakblBvREtCCFeo7aXA1fItEv38A7IJN3B8CYi3y3ggKyAtYSVoWKe3nfo384vneBVPhQRg0k6sqo7A2AwU7addQomCucOSXA47f7b1uX1ObEPzin2k3kRQWKqgBjgVrfdx60JJ8E6NhpxH1XdYAAAvUF1avz6NVJXIxZI39ihsdX4ho8Q3YCjaiAr5Fvw54ND8s08TdIuCmTsXuktyIkOx98yYNBXGQtqpBmWiYQ_OlmPjHV1mvGXJCO4FR-EaS4c_-mGBCLzMIHq__vhtpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sskarh59K3_S3UIgxcX8qEoWmfi-eNwBsTl9j6xy-CTZfu6faA_aSH_v26_v80ZHAAVCmUB1t926f-tpgUpYDjslrZRO-I0JdzzDZAkK45LKpOSPTj6KF3G7ifOyFjvJjl9iBclwg5YJMoHUmypMKrwIkke-BxP6eXxn8q4t6Zg3-FQpvF9SSAcRRPTjpVLbAYp_Eny0Y7rrQagFeoxvAg7z6D-jaw90fIfvf3B4Wp6spt76QMtgvbe-1hsYqnVkiESBOfKpXaaiXU11DV9USaieJ8UjQfZLCidr1o5dsLfyixcVlYA88nFMZljEFdfuzL4rBKIEdYUHIN1YFsFtuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghPdmmK6_miedAEaeteaNqEN3WoTQrqZJtvy12OUYJaB4cphSiTbdjxQLmsyV4IgNlbWsRE3aWcRnjYY3gVRyMqvR3db1QFSzEXmi7WzlMCxz8tgVTMkANYYWMKOed4-xvwQmrTogKqpG7WioK6HU_SWgaSF7Ax2kMKhEL3uxPUzu0MV7XwT42EZqlL2okGhf6G7HLZWzBntnDldUOa5hsQJdZHjlUG3k-NoRsLxNbPfL65oTAW2AgdgssihJmGz6hyJ0xS3UFRBUa9sJy6GqqawlrToF0hMTcxdQmZNTmF5uam4TqDsfDo5I8G-d6MIr7Um7MV8Cv18zqYtkvRu-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از وضعیت تاسف‌بار بهداشتی در منطقه گردشگری دریاچه ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/680230" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680229">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
عراقچی: ایرانیان خارج از کشور و شیعیان جهان میلیون‌ها دلار در زمان جنگ برای بخش سلامت کمک کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/680229" target="_blank">📅 10:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680228">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی: افزایش قیمت بنزین منتفی است/ حذف کارت‌های سوخت آزاد جایگاه‌داران
سخنگوی کمیسیون انرژی مجلس:
🔹
حذف کارت‌های سوخت آزاد جایگاه‌داران به صورت پایلوت در استان کرمان آغاز خواهد شد.
🔹
براین اساس، سهمیه کارت‌های آزاد به سهمیه کارت‌های سوخت شخصی افراد منتقل می‌شود تا ضمن جلوگیری از قاچاق؛ توزیع سوخت به شکل عادلانه‌تری صورت گیرد.
🔹
برای مصرف‌کنندگانی که نیازمند سوخت بیشتری هستند نیز تمهیدات ویژه‌ای در نظر گرفته شده که به‌زودی توسط دولت اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/680228" target="_blank">📅 10:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680227">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz_8dSbcvQSHoFO6B1F1FxVd987BT2CZ-qNCkuLMb4HpLSmdiDwv3VqDMSv2r43qDGMTLP_v0k13NYdE2aZlQCRWmP3dNujenJdpFaYqD4uAVPNyR8rMrzaW9iR8CjGO44N58vS6ei3YzqCKiG-l4A5fuLEXScF11zcu_Mqp0dwN4OVT3a6snZF-0T4O2zHQXmGvIVz1vyeN0OD_eGxG-yYFyADsHsiIVXCVAqpMYSU0sdjAlZWrF5BpSdLBQkGLYaUH5hz4n_8TfsvpK23SwbpziWUAiydSxQnVmN1CCXeADFr1aOalevOZWCRQI-OEX4j7LRDY7HJdfTBx1t-8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت سالروز شهادت امام رضا (ع)؛ حاجت روا
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از حاجت شیرینی که با عنایت و لطف امام رضا (ع) برآورده شده است، برایمان بگویید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و روایتگر کرامت و نگاه ویژه ضامن آهو در زندگی‌تان باشید.
🔸
صدای شما می‌تواند امیدبخش دل‌های بی‌قراری باشد که این روزها به سوی خراسان پر کشیده‌اند
👇
#حاجت_روا
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/680227" target="_blank">📅 10:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680226">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d142c98d.mp4?token=leEU2ccJAlPbaqZJqXtMgkoBERyOPj4yWs7GPHfDLkGJRLYe3fGM5ju2WmFmWdwEnP6txqtg19l0gCUsNbHoYCutX4-xJAHHRQP8eWW3-7SEWnM3UiEZeGBrvEnGnLCVv6z_2diD4Kmzxtjv3JpW1Pj8Yyk1SLKDB4-cajgSHc02eP25REUFxi9629wDA69HF2a2Z1G3dTvSSmtRLTGCSTNzU-A8LnX8v_kFvnItspI7e85iq-hZZJrqmVKShcLBERBcEHKl8rOtxx65LdB-O_gqPSzE9jx8eQGxJznkJcXcLGM0XJUt2Ap-OSdWM9oJTNWw2mx9WJQK7aPNYhZ_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d142c98d.mp4?token=leEU2ccJAlPbaqZJqXtMgkoBERyOPj4yWs7GPHfDLkGJRLYe3fGM5ju2WmFmWdwEnP6txqtg19l0gCUsNbHoYCutX4-xJAHHRQP8eWW3-7SEWnM3UiEZeGBrvEnGnLCVv6z_2diD4Kmzxtjv3JpW1Pj8Yyk1SLKDB4-cajgSHc02eP25REUFxi9629wDA69HF2a2Z1G3dTvSSmtRLTGCSTNzU-A8LnX8v_kFvnItspI7e85iq-hZZJrqmVKShcLBERBcEHKl8rOtxx65LdB-O_gqPSzE9jx8eQGxJznkJcXcLGM0XJUt2Ap-OSdWM9oJTNWw2mx9WJQK7aPNYhZ_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ایرانیان خارج از کشور و شیعیان جهان میلیون‌ها دلار در زمان جنگ برای بخش سلامت کمک کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/680226" target="_blank">📅 10:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680225">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cea4e39ea.mp4?token=Vs1Up5uQFDNmf6PNJ54dUiZu4DHgCYhi6PeN0pO_9Az34I5ppeNNespAl60TzUdRgctvKJzIFLeTuk__CyN17cYvqpIsFktTNw9Yq6hstKS8_zUKqFIbm94q5cDcwqBI5tR3dT3tOvNMw0963SH-VbSB51UkiKxfoUTk1ji3iVi5K5hHMUhMsq00PMzg7zqkQd1CcXyktuX4LgmZNsntcus0hVzU2dn5IM1PJGP52-fvMWhRt4gu26zsw38RrtMVy6MAfxLHqO544HSqBoPib2276xh7oCNYZNgsGCSy4HGkphU9H6TcI9p3mWnPuKgcD4hRYlW6SCReR2OVQLb_ZzvEr69z-heSE1FqYHYTETG7Pe-m7J0FU4F4CNl6ZQtoEFo3jVIw3_pjWYc0WH4aqaP6Pb5z_QggKEiFPNMAVjwwPgdLO62C0OBlkAfpygat1afJGhAjhXWXP91F6TlZXjnjeQ927io8wqda82rzz8kje2CwX2T8xxam6aTmxKvRuwmzXaTPtsOplGEd51OrE5EEEZ5WRKjR0xZtPTQ_JgNsUibFJxt-Z90QHNgRbhivsACZgswRLuwH4CpKAquZNwWiXyp9n_yhD2lSj70vuuCTTwAnkRXDDWvJMKMQ4qDKYxu2ydbSYRjNJkQdY_Gj2le5Q6GUGukRtCZ3qFPERRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cea4e39ea.mp4?token=Vs1Up5uQFDNmf6PNJ54dUiZu4DHgCYhi6PeN0pO_9Az34I5ppeNNespAl60TzUdRgctvKJzIFLeTuk__CyN17cYvqpIsFktTNw9Yq6hstKS8_zUKqFIbm94q5cDcwqBI5tR3dT3tOvNMw0963SH-VbSB51UkiKxfoUTk1ji3iVi5K5hHMUhMsq00PMzg7zqkQd1CcXyktuX4LgmZNsntcus0hVzU2dn5IM1PJGP52-fvMWhRt4gu26zsw38RrtMVy6MAfxLHqO544HSqBoPib2276xh7oCNYZNgsGCSy4HGkphU9H6TcI9p3mWnPuKgcD4hRYlW6SCReR2OVQLb_ZzvEr69z-heSE1FqYHYTETG7Pe-m7J0FU4F4CNl6ZQtoEFo3jVIw3_pjWYc0WH4aqaP6Pb5z_QggKEiFPNMAVjwwPgdLO62C0OBlkAfpygat1afJGhAjhXWXP91F6TlZXjnjeQ927io8wqda82rzz8kje2CwX2T8xxam6aTmxKvRuwmzXaTPtsOplGEd51OrE5EEEZ5WRKjR0xZtPTQ_JgNsUibFJxt-Z90QHNgRbhivsACZgswRLuwH4CpKAquZNwWiXyp9n_yhD2lSj70vuuCTTwAnkRXDDWvJMKMQ4qDKYxu2ydbSYRjNJkQdY_Gj2le5Q6GUGukRtCZ3qFPERRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانی‌ها به هیچ عنوان بر سر تنگه هرمز امتیاز نخواهند داد
سردبیر وال استریت ژورنال:
🔹
گزینه نظامی در برابر ایران «غیرممکن» است. هیچ‌گونه فشار اقتصادی علیه ایران جواب نخواهد داد.
🔹
ایرانی‌ها به هیچ عنوان بر سر تنگه هرمز امتیاز نخواهند داد و آمریکا نیز تا حد زیادی موشک‌های خود را از دست داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/680225" target="_blank">📅 10:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680224">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
پیکر شهید «بهروز مصلحیان» پس از ۳۸ سال با آزمایش DNA شناسایی شد
سپاه فجر فارس:
🔹
پیکر شهید «بهروز مصلحیان» از شهدای لشکر ۱۹ فجر پس از ۳۸ سال شناسایی شد. پیکر این شهید والامقام با انجام آزمایش DNA و نمونه‌گیری از مادر و خواهران وی شناسایی و تفحص شده است.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/680224" target="_blank">📅 10:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680223">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9102b2c0e.mp4?token=uezXWYe7TUnKwt_jcdOIa-4_II4vhTgXyEGUWnylv01izmqnPGJE75tnwkIjU7sne-RHo91aZv3oRNgrmPEiCAsqHnkUQowWvQ-COHepz7GHX8A5_41ppx8W2LrKAqqnzV9-Gj0SGRZy9AzbeyEFnHlz_Sx8b_ZmI_hXDY70YkPjsQiowgv0b8rxutvuybeb_UKOluH_1Z2y4BJr_FR-04StvNZ8d6byS8rwCOjrqA2vcjpIH76FOmHFlb207nUQExOonGk7Rt5xZTGOUxUdtV7eyjevMjOkAqJNtx4_DOa1ZxXGd7yq80f_EEYe_os9wx7AUmvrSyZOidOkXFmvzFpEjrfgqjMJh2BUyl869DUktYb5BwqUGd4plSHiTvRU4vf1tXbWg4IBO0rq4LpfzBSlg4RsrbBZQ1576MiL7xNsK65d6mKvxxh3lTIyiW_NozNhonQL4mRJxm-N5P10jH2srbmnBVGKPyKekATHCjW9AckEGdhh30SR6Eb7NrAIklT8uiVsmuJIdPQubTr8Ym91uBIDTaFUI7LDwimnK4jQw2tcnvgfICSm1Ds9f3IUv8QtmoaqtF69YTcQE97fT94W42vfgAY6r4JZ_4kvbVYDmIxGAQEZsgUsra0KNB0WNi84qGcWb0dFH1h36OxHuxDtdTG-4r6GVseDlAp3s-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9102b2c0e.mp4?token=uezXWYe7TUnKwt_jcdOIa-4_II4vhTgXyEGUWnylv01izmqnPGJE75tnwkIjU7sne-RHo91aZv3oRNgrmPEiCAsqHnkUQowWvQ-COHepz7GHX8A5_41ppx8W2LrKAqqnzV9-Gj0SGRZy9AzbeyEFnHlz_Sx8b_ZmI_hXDY70YkPjsQiowgv0b8rxutvuybeb_UKOluH_1Z2y4BJr_FR-04StvNZ8d6byS8rwCOjrqA2vcjpIH76FOmHFlb207nUQExOonGk7Rt5xZTGOUxUdtV7eyjevMjOkAqJNtx4_DOa1ZxXGd7yq80f_EEYe_os9wx7AUmvrSyZOidOkXFmvzFpEjrfgqjMJh2BUyl869DUktYb5BwqUGd4plSHiTvRU4vf1tXbWg4IBO0rq4LpfzBSlg4RsrbBZQ1576MiL7xNsK65d6mKvxxh3lTIyiW_NozNhonQL4mRJxm-N5P10jH2srbmnBVGKPyKekATHCjW9AckEGdhh30SR6Eb7NrAIklT8uiVsmuJIdPQubTr8Ym91uBIDTaFUI7LDwimnK4jQw2tcnvgfICSm1Ds9f3IUv8QtmoaqtF69YTcQE97fT94W42vfgAY6r4JZ_4kvbVYDmIxGAQEZsgUsra0KNB0WNi84qGcWb0dFH1h36OxHuxDtdTG-4r6GVseDlAp3s-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک چین در هوا منفجر شد
🔹
جدیدترین موشک چین کمتر از ۹۰ ثانیه پس از پرتاب منفجر شد. آژانس فضایی چین هنوز بیانیه‌ای در مورد این حادثه منتشر نکرده است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/680223" target="_blank">📅 10:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680221">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzKk6_JSUs8A0RuKTbNzF-oZWkDApyoQPwjMXCeCBeaOn9OU8t8o0bsQFknuWTDErDJeBofU3bfpGjsUHErLaQSeFfoSRQvhqDhjqmqD1OHGk_gUvyE5lzgG8e4RKmi5ThlyFF7wM-DTdIWgER8emfNNVFiNw8E_K5ExEHsDnzl2QHpF6MahRh_Jf037-V-g0-XVN2Faeik4s0mN1guF0uA5QAb_TAfV7IIS5m5X6S35J2BeBbrnh0V_ZNRJx3po5-0ckpZGe94vwPRGeK7M8KZfjFeP9OKufGq-GTslC1B73QhC3NeKtsgh4fMWxx9GNN6WKrVUzEqzDzx9Dcav0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcIiUoiUHGYkM5Rc9Cysz-GCxNPhxPs8kemsp_fgx13HXCiTcfp1MiB3t8LbDbO-aYv1Ap-bqg_WRAYuerwytl9j6Z3XyYH8ikvydjFtKsGxnXo20A_REi-oA9IRCcTfn0vhed-XY_OGtwjC7QyadmtGTYFBve6SA8Y5WBVzOVNqAyzVeEeBCDf_J1mhpX1nq1wBVRiFuahKGcxd41hmjN2ck_CrQNGLuGlKklG1WmamtUKH4fI2FeDz7OcA6B_gzmTV3yhPtBXr555k7qfxThAViYh-DfR6R9qd3AAEqE4lYRO-U7Xw8jNfa5kMAj10_PT1JlkE8FwE0TIQAFbCKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیدا شدن پهپاد ناشناس در سواحل شمالی ترکیه
🔹
رسانه‌های ترکیه اعلام کردند که یک پهپاد ناشناس، در دریای سیاه در ساحل استان دوزجه پیدا شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/680221" target="_blank">📅 10:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680218">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681a3a0b98.mp4?token=oz03B3BUKxzGEnGIuUXVhabBudccuNC7plw-qQq08jNXOZB53d4qn1hhkoHdvx1o_NjZBJwN3YTDEHYyMvu_zlEEyXl5n4fxvh69-mJZaRHbq7frPl2JzBboBSWDc6VpI3BCpcQ_0tj2eCpBfLo32hbNkn20Nm16z32GxxNgDyzqbDF2b-hQxEaxebPNGHKjMihh3ZnuvRWYpNdC2kq_UpyyZ09Y1L4QKKiP7USVS2QBhxfnGqnMkXGaDe0wIdwSfsqyRX_aUDQaEj_1zeyyA04LGSKKnd5XI4lGHB74dTqvAcU8N2wgjIJBHZSVLckWNmkdS3fQ2WS_d-A2HK-03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681a3a0b98.mp4?token=oz03B3BUKxzGEnGIuUXVhabBudccuNC7plw-qQq08jNXOZB53d4qn1hhkoHdvx1o_NjZBJwN3YTDEHYyMvu_zlEEyXl5n4fxvh69-mJZaRHbq7frPl2JzBboBSWDc6VpI3BCpcQ_0tj2eCpBfLo32hbNkn20Nm16z32GxxNgDyzqbDF2b-hQxEaxebPNGHKjMihh3ZnuvRWYpNdC2kq_UpyyZ09Y1L4QKKiP7USVS2QBhxfnGqnMkXGaDe0wIdwSfsqyRX_aUDQaEj_1zeyyA04LGSKKnd5XI4lGHB74dTqvAcU8N2wgjIJBHZSVLckWNmkdS3fQ2WS_d-A2HK-03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عطر و طعم این ته‌چین، مزه‌‌ غذاهای خونه‌ مامان‌بزرگ‌هامون رو می‌ده
😍
مواد لازم:
🔹
یک استکان زعفران دم‌کرده
🔹
دو استکان ماست
🔹
دوقاشق چای‌خوری ادویه ته‌چین
🔹
یک استکان روغن
🔹
سه عدد زرده تخم‌مرغ
🔹
فیله مرغ آب پز
🔹
پلوی آب‌کش #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/680218" target="_blank">📅 10:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680217">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYTI5jy5MIwgpojxxgYb2PXSwJLcq4Fm8GaT9OF78nPSa1ULCb4dBwpb5zO0G5Ednydw1ndHPBNAM942aaFaGl5rpboBzf0jWh2rcvp6VY2_hdfNOc6R7r2ykVKFtJFLYQAYX5VQ45FcgMPSTVQFAlacLSVMysViIoBbWkg5Q65Uaa9092Uq4nL_dhrvhxym7hkBdAjnRphul9bPqOmy5MTfUI20C4kaEVCEFQ0PWIZecY7GnDGyTu4yIKNEhWGfVADcXQiPrmOc_hKkzzaGl4ERvOBkqwnmoEfXI6M5yL__zCInvd8Ap7zXTz0Dvrpxzhm5pG9PqD6Ks6DXEq16BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثه دریایی در باب المندب
🔹
شبکه الجمهوریه یمن و برخی منابع عربی از هدف قرار گرفتن یک کشتی عربستان سعودی در نزدیکی باب‌المندب و وارد شدن خسارت به این کشتی و تلفات به سرنشینان آن خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/680217" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680207">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmJbRLl0zz_SwMGgHacz7X0xiB7uL6mzkw3qvCFarQeQVqocc2jQmz374AV1ceNTg_FOSeA-ffAt62hsxtc48MriXJTR4qhiYP71Q_EZuZWxDqYCDxQBlXGADE_1AkOHPBBneWqO1dAMKYloqLCHokeHuDZWmzmCN8mhVaIKgAKonuRp2LzkchjMkOWEagjm_40whNVooQzt1cGchi5s59XOQVkqImat1UdS8-QZMh2gBJ7T_YW_xUsM6b8PIn4EW3CTOCGLsI1ew2a-543samHJIKbHkaF--7Jj9KVUe_whI6b1pab1WhE8toaQ7YMmufc8MBpnupqBblhLyoAtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5JNKhDMgjDWB6DBHery7HT8U6qOM0qOG-VJe1EBYN0kHxaFdD7axd9LjaoSRjqrU7rr1LcUknfgzxwnZ2OtIv02kiZGc0wrIB4ib8FuM0XgIc5WMpkbtA2a9NTNvAGShHke2Dn8MaKp6QkAK6xy5CGQTL5omjziasJsEjhG6ScBxDmtm5NBBM8H37EY4N2AULqYvKWEFA4yBQbsN2gNJ8jxJha4R184Ep2tfR6OYaQiFbwlN6MQCM9g3ZnI7fkd1jJvmCxuNqcjjr4AsEYbwJXprH5SeanJ3bGVPAGxzvTlcKQjgqlrQTXTqJXdfJrl_JxSLEL06xNH0I4piphZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rulio6HXXmDJ1TjL4Es2DtQItObAZUzTEOmJEy69_uY8wbDMPBKdjGolX7qDa5pq4WqWqatKL_y-6ahpd9wNLqwgIg5uvffsvu27N2DrxF5ja4c4hZLC6uC_0HoPV39LLfTuu890B_-7GxLDeo5waqh9iWlr1NqQuZ48ezNcEb_FaPHfLY4pYwNAppRWIfwV4DETpycXhNkLXkDrA0sUjmB-2CWwve5v6BLqPE4kRZg86VH7yypZRTe8raihkoawWR6jI6mE4rV34Hh2ngpCbzG2wzzHbFSGw20dyG6pZ562vtwTfRhHv_G_alu75Ap6OgIzEZnpi2DRgyFrZXKagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrNZWmD1UuHkwf_O0Fd3Q9B48HUakS_6X7QXZVDZSHsvIUt4aD8VJwDuQPig4wDC-KiJ2h88hAfD3EgZDbNm5eJfOsFlj_l5kabOPMlFZfEHZZxxmpDQNUWBMqhihfnvg06FxzFpMVkZPNdUOe50qHhbS9AHiTbyfc_P0r6hn1lAWxysAVc-IajXlYo8hplfGlF17kS2HFt2iA_oTk7qhPYF0xEUon7E8QWla_QJHGAQrCjOs-rPCaQiWAe-ZIBp5CF4GyCa4xlWPLOMfpV3phRTDcDgscX5XeP4cyOCeyIEPDpAK70EjvwMYF10FSjbu_e_9RAQJ3rsiml8WaF1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6PB7QvH0m5E4D0AG8WUxy2nBn1yOEMZGZWBuRkGTjUSzH3oW8ah016ixJD7jpr2sCC110gAwFDSUptfxE5MLYLNWg2MepR5c1kOOZU_OaudJFWCFjHrZ7RAV8ySd03jeU2mj8NxVND2u5gs1xFit1zxccDUgNhxE41ANhTxTudJdzGvqnTkgNhqaopfX_6XWbNlRgnIy3mPoRYL1-0cAkd3N5JDy8PZefiJCwHNKAljXCCltiMTMXXbyRbBMbfAqCDOwtxCp6dbNTLAxBrIUZjMuy_UueFCVWtxUr9-9IBmelr9PfiXyD3rNJal5OLASGG8HEn2btjRLi71Fu_xfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBr9scHCImDJwNEqV2Q6YTjAyCWauZmT_MzYpEMxnzl8mVy5NzOB0vInWS_N2TypJu8Yuk59QxHSaFfS3DngQuTi7gSD94KmOREIjoJc1vl6wNoODvnU_xu89CbiAKr9nFxVfJ4NpJLfzyBNlUHXfYB6hzJqFOK7AOT0UCf_BPWjw283lwlym3k9kdee5RdonTVvVKKbP0QKXuKCumhg4vdAawZ4ybXFWDxl_dwYPAMD7GrxcjI0oeh7eiqppmm-qf9G4UxDdSU_Ig_edaopSJGUMGJffqArTyg1yAiQF6hplakTfzaCMi0JkfOneNt4NDpHEdxmT_Q2HjwZwB3ebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJ3mCAG5BjgG8VRjDrNSqX8PmBkgp5dyQInkuHlpTTDFQ7UdUmPN-M6GMngeRaHd472--m7Kx9SZbPqNzTrmIlgInZT1bBuWELRBp1uaLPlEjCe3wvQ8lmnLjunRjWY1YN7NUYkY5avJZf-hG9btls0yQDrA1WrHyImAxtYsa11qO4AKSwfoxGLXJ-gqYMNCg5v-dQ4GgBv1q30CEHb1kL22q4-i6mN63_FrHSZ-6lCbc-nODxzAKOP9tB5Jqdvm4SZjLq6L1_Tg7LY1iAg8kPzD7g0goznPK3YYhLDvXC7nR6AHUkcYeERAuGAw6lpRfJunrXNd5LGSE4j_-Ppw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ai23omX7MCVQxs3pGmkWBG2kcfPsH1_-0TKidPeKNoXC5f6faLs_Uk5joe_7CeswdNND9va9iT-8Sz6qGj4kyzQgCuTc92tt5iSn6bdqMVajjB6B8RHc62tXAvAWMi39Od2ki2lMsqoUpCejJM8qNuo71Ttc-uqkuSRyE_hC9r1fmsELd0A_VUDBYkUtRB3IgXWAKWa2nLIU9OFS8iKcVlINKbSQkX3HI0WZcSbPGJHzjaQ7v1CGlqSEryjrJHMj0dS24h4CmFG9gWU4bb0Jstw4JkIsldM-resQnFod0YRVCuQZ8Dd3wHJCDnJqu6X3dr9gvmJEqnG_ELbEesAWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhyXxgGuqt57GJZ3VRaMZkZBSQ2aSA6f9c3ecIcEcixU1ZJL2ZKNcrHdxtdrFo22LOSFc9ic66dPfuacYZ-fCy0OsdgVqVDf1VSd66colSDjSRU4ChrFhXWB0ERH5hWeZPhSUHApiXvOKOUFdbEKbUpQWTFDEuMDg59lBarYdOpkdjZZWKJht_wHQsqSNHVk1mSTF7kCK4lk0Jwcb-8BLlboQqFYNrUJRzyxVL8vo3-RiAXC5sEv5oH0YRKgd-4hZgUfqPTqNdT6Rv9ZBvhdWr11XH1_ftuMEVtRqs3lIH3pYYsvyA18fGOjII-rFAvEGdWtIl41wuiU2ZAZKFp7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4UjMhyGCgmBtuwuPa-_S1g30Pw4oEzfgb2magxKXLTS-7CFt2BmcHgP6xW4Ke6_j-TKW2Wr2PaVxwJObrcDOrpZxCJ06FsSTNBQQkvf5InAsxtHtr4TROeEM7e92DTQUth2X6ohrHMi62JckjENHo8CfzFqOROsqcj_KAZOM7Ct4072u-oxaigJGaa3ukpRU0TQtL9GjK5IfraIQUpmHPCMmEEAPL4CByAgNCtLu0hOI8LB9DTDOtc-b0IM5pEqKyXAVpBNIAy8m9RmmQ4J9sLJdzRjmsgG7N63faSZ19PPULebBOx9lF2eMS--YICsLrCgXkpp0PGn1474vZ8qVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حال و هوای موکب هیئت قرار در مسیر پیاده‌رویی زائران امام رضا(ع) به سمت مشهد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/680207" target="_blank">📅 09:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680206">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
گروگان‌گیری در پایتخت
🔹
صبح امروز در پی اعلام یک مورد گروگانگیری در خیابان ولیعصر، بالاتر از پارک ساعی، موضوع از طریق مرکز فوریت‌های پلیسی ۱۱۰ به پلیس گزارش شد.
🔹
در پی این گزارش، تیم‌های تخصصی رهایی گروگان، سرکلانتری و سایر نیروهای انتظامی در محل حاضر شدند و همزمان عوامل آتش‌نشانی نیز در محل حضور داشتند. با حضور به‌ موقع نیروهای انتظامی، گروگان آزاد و فرد گروگانگیر مهار شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/680206" target="_blank">📅 09:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
آخرین وضعیت ترافیکی راه‌های کشور
🔹
جاده چالوس از ساعت ۹ صبح امروز، به‌دلیل ترافیک سنگین، در مسیر شمال به جنوب از مرزن‌آباد به سمت تهران و کرج مسدود و مسیر جنوب به شمال یک‌طرفه شده است.
🔹
ترافیک در محور چالوس، محدوده‌های پل زنگوله تا هریجان و هزارچم سنگین گزارش شده است.
🔹
در آزادراه تهران–شمال، محدوده سنگان، تونل‌های ۱۶ تا ۱۸ و انتهای تونل البرز ترافیک سنگین است.
🔹
آزادراه قزوین–کرج در محدوده پل فردیس تا پل کلاک و آزادراه کرج–قزوین در محدوده حصارک نیز ترافیک سنگین دارد.
🔹
در محور چالوس مه‌گرفتگی و در محور فیروزکوه بارش باران و مه‌گرفتگی گزارش شده است.
🔹
تردد در محورهای منتهی به مشهد، شامل نیشابور–مشهد، تربت‌حیدریه–مشهد و قوچان–مشهد روان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/680204" target="_blank">📅 09:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680203">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: با ایرانی‌ها در مرحله مذاکره هستم؛ آن‌ها مذاکره‌کنندگانی بسیار باهوش هستند
🔹
سه استراتژی برای برخورد با ایران داریم؛ نظارت دقیق بر وضعیت این کشور، زدن ضربه‌ بسیار شدید به آن‌ها و فشار اقتصادی
🔹
به هر حال به تهران «فشار اقتصادی» وارد می‌کنیم.
🔹
ایران نمی‌تواند سلاح هسته‌ای داشته باشد و نخواهد توانست./ انتخاب
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/680203" target="_blank">📅 09:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680202">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
انصارالله: عربستان در پی تبدیل المخا به یک مرکز نظامی بود.
🔹
شبکه ۱۲ رژیم صهیونیستی: آمریکا به روند خروج هواپیماهای سوخت‌رسان از فرودگاه بن‌گوریون ادامه می‌دهد.
🔹
آلمان خواستار مذاکرات سازنده برای پایان دادن به جنگ علیه ایران شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/680202" target="_blank">📅 09:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680201">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
۴ فوتی و ۳۰ مصدوم در پی واژگونی اتوبوس زائران مشهد در خراسان جنوبی
🔹
صبح امروز واژگونی یک دستگاه اتوبوس حامل زائران مشهد مقدس در منطقه قهستان خراسان جنوبی، چهار کشته و ۳۰ مصدوم برجا گذاشت.
🔹
امدادگران هلال‌احمر در حال امدادرسانی به حادثه‌دیدگان هستند.
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/680201" target="_blank">📅 09:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680199">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: اگر یک پل ما را زدند، باید دو پل آن‌ها را بزنیم/ ما بسیاری از زیرساخت‌های دشمن را نابود کرده‌ایم که اطلاعات آن‌ها توسط دشمن سانسور شده است
محمدرضا رضایی کوچی، عضو کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
نیروهای رزمنده ما خیلی از زیرساخت‌ها، پل‌ها و نیروگاه‌های دشمن را مورد هدف قرار دادند؛ منتهی اخبار بیرون نمی‌آید.
🔹
نزدیک به ۵۰ هواپیمای ما آسیب دید که حدود هشت مورد آن‌ها عملیاتی و فعال بودند، مابقی از رده خارج شده بودند یا در تعمیرات بودند.
🔹
در بحث خسارات جنگ آمارها متفاوت است؛ وزارت اقتصاد، وزارت راه و بانک‌ها هر کدام یک آمار می دهند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/680199" target="_blank">📅 09:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680198">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادغام ستادکل و قرارگاه خاتم؛ آغاز یک ساختار جدید نظامی در کشور
🔹
فرماندهی معظم کل قوا طی حکمی ضمن انتصاب سرلشکر پاسدار خلبان علی عبدالهی به عنوان رئیس ستادکل نیروهای مسلح، بر ضرورت تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیاء(ص) تاکید کردند؛ ادغامی که براساس تدبیر امام شهید از سال گذشته آغاز شده است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/680198" target="_blank">📅 08:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680196">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52aa08b141.mp4?token=W0nCv4Q_r0cwK4Ey_-D3zboyEscsPNzdi11vdTWFxS_cWAMurJT7bnICKxpDIyjELXBDyxU6ZEy16KVgDp9fNr6P12jeNX_z2ZVMJ9FI4sL-lUfODVVqJSs3Vu85ZWXhI2J3yJiW-ZWrKVxlehSU__PJPO93fACx3ZaAelZxFMhqRstPSCaHzEUz_-BDWvjRN8wmkWvn5icCJAGeCDgG1S2RsZeOl4Z6Am_xExtck6C9PKyh3QgHt3664J09cjtNj02R3zj_6NDUw3ZQPLegpbpywJd-3Eb-gPGjBFkxTUlV-lXi19HSgQXhS868JRMxMwoFLJk0JyQ8hjwIAem06w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52aa08b141.mp4?token=W0nCv4Q_r0cwK4Ey_-D3zboyEscsPNzdi11vdTWFxS_cWAMurJT7bnICKxpDIyjELXBDyxU6ZEy16KVgDp9fNr6P12jeNX_z2ZVMJ9FI4sL-lUfODVVqJSs3Vu85ZWXhI2J3yJiW-ZWrKVxlehSU__PJPO93fACx3ZaAelZxFMhqRstPSCaHzEUz_-BDWvjRN8wmkWvn5icCJAGeCDgG1S2RsZeOl4Z6Am_xExtck6C9PKyh3QgHt3664J09cjtNj02R3zj_6NDUw3ZQPLegpbpywJd-3Eb-gPGjBFkxTUlV-lXi19HSgQXhS868JRMxMwoFLJk0JyQ8hjwIAem06w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال و هوای موکب هیئت قرار در مسیر حرکت زائران پیاده امام رضا(ع) به سمت مشهد
🔹
موکب هیئت قرار به همت همکاران هلدینگ رسانه‌ای خبرفوری راه‌اندازی شده است
@Heyate_gharar</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/680196" target="_blank">📅 08:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680195">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
انتقام عجیب عروس از مادرشوهر: ۳۰۰ گرم طلا را با بدلی عوض کردم!
🔹
زن میانسالی از عروسش به اتهام سرقت ۳۰۰ گرم طلا شکایت کرد.
🔹
عروس اعتراف کرد با تهیه کلید یدکی گاوصندوق، از طلاها بدل مشابه می‌ساخته و آنها را با اصل جابه‌جا می‌کرده است.
🔹
او گفت به دلیل اختلاف با خانواده همسرش، طلاهای اصل را می‌فروخته تا از آنها انتقام بگیرد. تحقیقات درباره این سرقت‌های سریالی ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/680195" target="_blank">📅 08:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680194">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وال استریت ژورنال: ۴۲ هواپیمای آمریکایی در حملات ایران منهدم شدند یا آسیب دیدند.
🔹
بلومبرگ: کمبود موشک‌ فشار بر اوکراین را افزایش خواهد داد.
🔹
پلیس راه البرز: ترافیک سنگین در آزادراه تهران - شمال؛ یک طرفه شدن مسیر از ساعت ۹
🔹
فرماندار بوشهر از خنثی‌سازی مهمات عمل‌نکرده دشمن در بوشهر
خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/680194" target="_blank">📅 08:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c442ac82b.mp4?token=CbG3acC5H5Lx_g9EL0kc7gZ3yCWORpFR0tMUPciz2lMxS79gm3RNkEZ5CzI6Z0bwvzeS2MCi2N60Yqc9126VWDnq_BbWXxaLGyInbud0A7TNo2HY5vij9pguFcz63m4vRkbQq3DgBGMQV82pzlf7AgAnMsyeN9iPKhnR70oQjDcavxe9r58rvK0ztHxMViglFyNczJMmXz-Vxw_c4FqhxVeG5aA7fOC35ecPbo1dKBwOG37JCha1ezjBj8cadfJVyL1R5IxIvYpRDJIV4DLOVR6PULgeLkVVm_PuC6CDEt6UMPtu440e7hdWmNv9nQfm1rOZOrw8qA6g6bS-R_y997-ax5aFuvuJKi4AAzMEy6DpTOroszhqRZraNx277q0ZPXUgjF-b1LFppie6Z4a4vj19zHngEAqSHcCFa1GpGzTR5svmQJqlxbzkI2Mx-6C51fv1du2mBizmd2TDuEcRYKneHil31i_zPhHDSrJTWJUCgccg750CPl4y9d4KxP5-umd6t4-Yz7qUhuMDdrlRLhcthQXedet6-X4DIpzh6nkvGha2-bpS4s176UQnmSqfPsKj5fKQkPgBz-XVAEBugdP3ZJpr6LxSXPHTNln9dPdXJfgzPwiXj01x2gCeiqSC308RfF_YPYRDCvKT9iQ7mF8Vp15DQL9fiS_LZQqwiM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c442ac82b.mp4?token=CbG3acC5H5Lx_g9EL0kc7gZ3yCWORpFR0tMUPciz2lMxS79gm3RNkEZ5CzI6Z0bwvzeS2MCi2N60Yqc9126VWDnq_BbWXxaLGyInbud0A7TNo2HY5vij9pguFcz63m4vRkbQq3DgBGMQV82pzlf7AgAnMsyeN9iPKhnR70oQjDcavxe9r58rvK0ztHxMViglFyNczJMmXz-Vxw_c4FqhxVeG5aA7fOC35ecPbo1dKBwOG37JCha1ezjBj8cadfJVyL1R5IxIvYpRDJIV4DLOVR6PULgeLkVVm_PuC6CDEt6UMPtu440e7hdWmNv9nQfm1rOZOrw8qA6g6bS-R_y997-ax5aFuvuJKi4AAzMEy6DpTOroszhqRZraNx277q0ZPXUgjF-b1LFppie6Z4a4vj19zHngEAqSHcCFa1GpGzTR5svmQJqlxbzkI2Mx-6C51fv1du2mBizmd2TDuEcRYKneHil31i_zPhHDSrJTWJUCgccg750CPl4y9d4KxP5-umd6t4-Yz7qUhuMDdrlRLhcthQXedet6-X4DIpzh6nkvGha2-bpS4s176UQnmSqfPsKj5fKQkPgBz-XVAEBugdP3ZJpr6LxSXPHTNln9dPdXJfgzPwiXj01x2gCeiqSC308RfF_YPYRDCvKT9iQ7mF8Vp15DQL9fiS_LZQqwiM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیگر از فروریختن ساختمان‌ها در کلمبیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/680184" target="_blank">📅 08:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0124cfeedb.mp4?token=FzgPlLzI83-2Gbz0VBS7WNogWk1NY5g9M42_LKuCk8PCCC-A_4uHP2J8xNNtJQEGvwYMrMXA44_RNgNlT6v903BdLRXrcf_-AZXIedn1gbNySfymaDIrle4XQ9PeDO49LwUybFnGHsin92N4MN1fp2PXkduSDAs4_hpVVir-5v74J622szGUoDVGO_eE_b4L_JB9ua_PiVoD7NVNqw3zFWovAqKQz05_8d-Ro6_uPl6wGTwRB7KbCXnLmaywpUV2Q5B82L9m1HDHGebKa4YIN8P7T8sqHhhQn5jMCbNYQ2Jy7MLq5otztvHGcxZc9eYS02FdvC-0P6FJSnFbWRnp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0124cfeedb.mp4?token=FzgPlLzI83-2Gbz0VBS7WNogWk1NY5g9M42_LKuCk8PCCC-A_4uHP2J8xNNtJQEGvwYMrMXA44_RNgNlT6v903BdLRXrcf_-AZXIedn1gbNySfymaDIrle4XQ9PeDO49LwUybFnGHsin92N4MN1fp2PXkduSDAs4_hpVVir-5v74J622szGUoDVGO_eE_b4L_JB9ua_PiVoD7NVNqw3zFWovAqKQz05_8d-Ro6_uPl6wGTwRB7KbCXnLmaywpUV2Q5B82L9m1HDHGebKa4YIN8P7T8sqHhhQn5jMCbNYQ2Jy7MLq5otztvHGcxZc9eYS02FdvC-0P6FJSnFbWRnp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین‌هایی برای فرم‌دهی به پایین‌تنه و میان‌تنه
🔹
اگر به‌ دنبال تمرین‌هایی برای تقویت عضلات پا، زیربغل، کمر و شکم هستید، این حرکات را امتحان کنید. #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/680183" target="_blank">📅 08:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680180">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hL8ni_JZlQF6lFgD4S5LWJbUHxuzF5JuJ08FTVT7aCWwyY-zr4-ZZauAe0lodIzzT7pBvQTIsikqEQe6FCZywoXppWIgeaC25rHBCS-Xg7lhR7dxOzzh838Qogg_hILO5LGFkMUaDCICIACjuiWhlmlY7iOrjHEkG79hCx4ly6SFMrDx6IeY5Y-TalAjhWL1u8W2x5OlJiXGNFGjstTLT_-4hEfKQTrPgFF4ch71sChLbvDh0MKw0im4Nq8zkFJBPC0x-L7peCJmw124VDIPpGS-QZ4usxeIk6pCyyypfgaCBlk-bR_vFOGMutkTV85RMg_JDzIKopE_2LBh3D34Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن پست: ترامپ در ترکیه از ترس ایران با کامیون پذیرایی جا به جا شد
واشنگتن‌پست:
🔹
دونالد ترامپ، پس از حضور در اجلاس ماه گذشته ناتو در آنکارا از ترس تهدید ایران، به صورت مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه خارج شد.
🔹
طبق گزارش واشنگتن پست، ترامپ پس از سوار شدن به جت قدیمی ایر فورس وان، دقایقی بعد مخفیانه به یک هواپیمای کوچک‌تر C-32A نیروی هوایی منتقل شد.
🔹
او از طریق یک کامیون پذیرایی فرودگاهی که معمولاً برای بارگیری غذا و سایر تدارکات استفاده می‌شود به آن هواپیما رسید./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/680180" target="_blank">📅 07:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d7c54a64.mp4?token=D8h9EI46T89yv6KyJ4HjAJADTB5GxqmCCihQaH4N9EYqZqVbobh5ZXONx6KX3rkFquPUWQzIzyAMkeQ_-Z0GCOskoBS4Mgk-mhCy2ShycqyHcygKkow9Oeh6snE96475X17U_y44zl9uKmCumI2hCDKM9WWVsXy91zurt04-IDIC9FQsyJqykn4Caz0eHk0aR7t6xQdb6ZXhC5VB5vDkmYY1lSFZUO3PnGa9Cb5_FmilguOxkn11tgKbRyZ89Ae7EVy13HkMJYnUhkYonJmcPgYPFDiiFtayeyu6TK-UtlzAWakysf2454iAAFdAYWyWnyEcsrkECnBFGFuTayidNlqDUEYN2Ccf7D1QoDnUSRsV7o9GR5NxbYmKKk5Z7GkgxSeFaOwSE5iGV1Wbc3gUdlLC1yPBcK9-xgUPuWzl5eIcv2PnaAtPub-lSAtZoMp0gGv2AHlAf2Xv__m63_P5msGsWYQjGHwvMZPrbe7YBBqMjl9tba5SGeDfSDNWlxNLfQ8n6rmSpFENkPd1JYNh8yubAHl97qFM7op_q3IIgenomYb8OWTiGqWey65TGPTTtODAerWrA2OJM9WlZStlvlMgLRZXV0xFhE0WfIvKCnhMiC8_6_AD4EEgWQgVEeAPv-f1T4S-05IIBNdLZCi4ePrOyCfsas7e6OTl7JoLuug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d7c54a64.mp4?token=D8h9EI46T89yv6KyJ4HjAJADTB5GxqmCCihQaH4N9EYqZqVbobh5ZXONx6KX3rkFquPUWQzIzyAMkeQ_-Z0GCOskoBS4Mgk-mhCy2ShycqyHcygKkow9Oeh6snE96475X17U_y44zl9uKmCumI2hCDKM9WWVsXy91zurt04-IDIC9FQsyJqykn4Caz0eHk0aR7t6xQdb6ZXhC5VB5vDkmYY1lSFZUO3PnGa9Cb5_FmilguOxkn11tgKbRyZ89Ae7EVy13HkMJYnUhkYonJmcPgYPFDiiFtayeyu6TK-UtlzAWakysf2454iAAFdAYWyWnyEcsrkECnBFGFuTayidNlqDUEYN2Ccf7D1QoDnUSRsV7o9GR5NxbYmKKk5Z7GkgxSeFaOwSE5iGV1Wbc3gUdlLC1yPBcK9-xgUPuWzl5eIcv2PnaAtPub-lSAtZoMp0gGv2AHlAf2Xv__m63_P5msGsWYQjGHwvMZPrbe7YBBqMjl9tba5SGeDfSDNWlxNLfQ8n6rmSpFENkPd1JYNh8yubAHl97qFM7op_q3IIgenomYb8OWTiGqWey65TGPTTtODAerWrA2OJM9WlZStlvlMgLRZXV0xFhE0WfIvKCnhMiC8_6_AD4EEgWQgVEeAPv-f1T4S-05IIBNdLZCi4ePrOyCfsas7e6OTl7JoLuug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات انسان‌نما در نمایشگاه AWE ۲٠۲۶ شانگهای
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/680179" target="_blank">📅 07:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680176">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBmcSU1jo1r3Ae4OCKXJjJzij9adMrr_kUDiB_m_WmRHN2Jh1in0RMzFpmWXg40DnFc1gF8pzcBesZpTz-K34pIYWoTvMZ74_pQdt5g-TYz6xbofcmUxM3Rzf2KBy2I5SsBfTz6D7ZJ6N5sCfgeksspjeOfpHzLbzh0F_OIWij5A-uDtwv-1bK3D8sHXOoTcTcnlSaJUYlBRjall_dS6rCOvuvWYylpHWmOYz5q59qWzGlZoVfDd7Nb_PmBAgVNi4CwlbeqN8b4EfIU1IbUtbYC231K5vvBCkP1bcJuct5w8EyhfRm5FJnlwd8D2Jg7MSUM2laNuIuUOfAvvbTKDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲۰ مرداد ماه
۲۷ صفر ‌۱۴۴۸
۱۱ آگوست ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/680176" target="_blank">📅 07:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680174">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9ovyiuw6WSdVYSR4cJLhnDKdqupaSIzWceds1V629nxYDsnUfbfdKHp41EHK-QQZhuJqmnVf6v_RZlLbqhRDBz-FWRJJGaulGRbIcqsMu9BLYXJqBm5oGnD0Hb3LcZCmYssKtVUvJMpQ7ERePpS7tSIH_CHyAJePDW7IN8scbsgiPCeV8R7tn6_YKH9xT3xCnwU_jopbytYuhya-7dTLnmWbB4-lY2E_ovRuQ2vMoX4vo-Q8x8toUZa5c2AAwD9lBMOV7Xg3IG3nCthCwYIsBPgtXimlMW1KkbEMZzgxahb0ybSGGbI-UOhM_CQy04JCqz8zLzB2muL8rCm4KpzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسوایی اخلاقی رئیس فیفا فاش شد
🔹
طبق گزارش یک نشریه انگلیسی، او در دوران حضورش در یوفا به مدت ۵ سال با یک زن رابطهٔ غیراخلاقی داشته و از سمت خود سوءاستفاده کرده است.
🔹
پیشتر نیز پروندهٔ اخراج او به دلیل زدوبند با ترامپ مطرح شده بود. حالا این افشاگری در ۳…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/680174" target="_blank">📅 06:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680172">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-c-j93cFqWYo_mAqzHBNc5DVYarzh9yy1rJ2jAdFBWpaSnbbACtynJtYickGUGTh8yD1NlWELeOB7xhoxbFn1_WV_sFHna4nH-ZGKuczHgUuyRLlU3nDK3MdhkdtPuiSDomDEgx4dUlsSsZt2d5gRYTOJrt0YVkNKLkZUvSEyRazrWTN4CZrQ14rzSr0AsiY7APAPgSyCNXRaCjawTY26sgb3aoDeS9T7qyeHTuxCol4vEWgJ1F6TsAIDQQ4aIaBQHp58eMjFtEhZekmJrwHjrO5qNIPVYlv7bcWZTi7VzN1jgSHgD4dSlHv3bRkovIS1Q659e9yGMFjyssH478RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ، آخر هفته در زمین گلف خود در بدمینستر، در کنار یک سامانه پدافند هوایی کوتاه‌برد AN/TWQ-۱ اونجر (SHORAD)، گلف بازی کرد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/680172" target="_blank">📅 03:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c50bf2a37.mp4?token=hXa1CeGCBbbYlTu08gIbdPYNyCSiceDoLT8p2qvHxQEICp638vfKCmz8uxAebA0GcYEt9S26wO5sqNyp7WAf5xPu6HB2z1clYc2Bg4OuNE-2vxk6c1Y7AdRK61GDxcMBXmRsZcESnjmHLUfkuZPYdYd_WRugIFfjm3DpK8Rgwph9U0TQecNAw5OVkj62AEXZhovK64JD8FSUmFtgFLHqiJlQyA8rIr1pmX53BW-Mu0dciU3rqPsuQj4Y4TtiWqTo9hwGk6f3gCpC9kKnaQLEGuqF-ZbavEY1V4QFiiat_V4stvlGKde2w7yIAY0ylYDam7QQcRbz9k8zj-kX8EIZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c50bf2a37.mp4?token=hXa1CeGCBbbYlTu08gIbdPYNyCSiceDoLT8p2qvHxQEICp638vfKCmz8uxAebA0GcYEt9S26wO5sqNyp7WAf5xPu6HB2z1clYc2Bg4OuNE-2vxk6c1Y7AdRK61GDxcMBXmRsZcESnjmHLUfkuZPYdYd_WRugIFfjm3DpK8Rgwph9U0TQecNAw5OVkj62AEXZhovK64JD8FSUmFtgFLHqiJlQyA8rIr1pmX53BW-Mu0dciU3rqPsuQj4Y4TtiWqTo9hwGk6f3gCpC9kKnaQLEGuqF-ZbavEY1V4QFiiat_V4stvlGKde2w7yIAY0ylYDam7QQcRbz9k8zj-kX8EIZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع چندین انفجار در مناطق مختلف کی‌یف پایتخت اوکراین
🔹
منابع خبری از وقوع چندین انفجار در مناطق مختلف کی‌یف پایتخت اوکراین خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/680167" target="_blank">📅 01:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680164">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R26vwlxhNlWw1vSVsKzKl5pFSM_0RkbmXUcZdgqZAw1Wrl6DrzQORSxFOKV5jmPnHWmz-isj-q63zztNqURNm5j2VgsnyUq5m-esk92vXjaG9JUwntaVr6f1pVBIv5I4auns19vwimpxT0Tz_9CBuRZ0b4L_1BXmNo5bgW3VPq1g6qteYmkrBiJCcufmR1xs6XiXJZk4vO0cTh-1gja-OdLgqdd5wy4xzK9e9kEREeIUbfXDKMBwvuWLm12UaLWiBuvw9f8Ts2vjBlX5ceQckhs2g0nPD78NqjpjCNXd371vQfjgaBDEp1spS0GJtCOMOKARwM6XjCkj_uapC01mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لشکرکشی نفتکش‌های عربستانی به سوی تنگۀ هرمز
🔹
گروهی از نفتکش‌های مرتبط با عربستان از دریای عمان به سمت تنگۀ هرمز روانه‌ شده‌اند.
🔹
ناوگان ترانزیت نفت عربستان توان عبور از باب‌المندب را ندارند و در تنگۀ هرمز هم باید ترتیبات ایرانی را رعایت کنند‌.
🔹
تنها راه بدون نظارت ایران و محور مقاومت برای نفتکش‌های عربستانی حرکت از کانال سوئز، دورزدن آفریقا و گذر از دماغۀ امیدنیک است که طول سفر را ۲۵ روز افزایش می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/680164" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680163">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrQlz-V4HlXPEXhhGKjoR1YEE6AqOsNvJrTqrITZSy6RzbGFV3k_PtqTXoB3O4THpXm1Kd2uHRzxMngxYoLFkf-YUi_tImjBpyHCr2DG__6eeGmDHEr3OLJv6fwdeAoLveYLH6qSN76FriJSeMW8tx7YACBAp_UkDuWb1_FUF_Lh-olwxSuAgP1xDcuAVOcG0hCIONFczd3lOdfUa03Fb-9tu463PRffhZMjRCeaaFwhR94F-JpnQDgKl0akY9wXXhs1l7jQc73ndiKISKvOoVuiMoABvb6scGx-5O40BReaOFroBtWR4Ep4Sy25GKwr87FgMH54TTfXTWsXwBUD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرایش جدید فرماندهی
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های شش تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند. بر اساس این احکام، سردار سرلشکر خلبان پاسدار علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح و امیر سرتیپ کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح تعیین شدند.
همچنین سردار سرتیپ پاسدار احمد وحیدی با اعطای درجه سرلشکری عهده‌دار فرماندهی کل سپاه پاسداران انقلاب اسلامی شد و سردار سرلشکر پاسدار مصطفی ایزدی مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفت. در ادامه این احکام، مسئولیت فرماندهی نیروی دریایی سپاه به سردار دریادار پاسدار علی عظمایی و ریاست سازمان بسیج مستضعفین به حجت‌الاسلام والمسلمین حسین طائب محول شد.
🔹
هشتصدوسی‌‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/680163" target="_blank">📅 00:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680160">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9009082601.mp4?token=jTCBWjq821V79TYGGTEJO0xB4EBOswfsGgWIcK1w-81e-GlPcZaaadhf5rt37ieR2kKfRuxsj62_8GZR72eNxhIdZO3IqAogCEOXGC9sIszEugguAW17r8m5xOKKP-ZoF9aWOJWONVVQt6UzV6QqOfz_ewatJZx4oklFIUfEZUjwbPEAgqjc3k_mksLFwOP4iMXg9eCy9n53fYSvlCbcZOV3GkjujVAre533pBMZF51zyB4d4epuijux_84aTFLQcMREws-gBpufOXBEd2LITpj2AwAusV6a4n89HmU92hJCL8VQt5lo4lDm4WkqBIhMpoxxQPWkoRUlDeZuenaoHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9009082601.mp4?token=jTCBWjq821V79TYGGTEJO0xB4EBOswfsGgWIcK1w-81e-GlPcZaaadhf5rt37ieR2kKfRuxsj62_8GZR72eNxhIdZO3IqAogCEOXGC9sIszEugguAW17r8m5xOKKP-ZoF9aWOJWONVVQt6UzV6QqOfz_ewatJZx4oklFIUfEZUjwbPEAgqjc3k_mksLFwOP4iMXg9eCy9n53fYSvlCbcZOV3GkjujVAre533pBMZF51zyB4d4epuijux_84aTFLQcMREws-gBpufOXBEd2LITpj2AwAusV6a4n89HmU92hJCL8VQt5lo4lDm4WkqBIhMpoxxQPWkoRUlDeZuenaoHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان حضرت ابراهیم رو اینجوری نشنیده بودید!
برنامه متفاوت پُلاریس رو در تلویزیون اینترنتی مدار ببینید
👇
▫️
https://youtu.be/4feAD2lqlHI?si=8_SmjCmzNJ7rwuSR
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/680160" target="_blank">📅 00:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680159">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12023699aa.mp4?token=d4L2A9tL6bkRptt2xkxmTjOYYPz26bcjj4fZByAbzb_FzI7xYX2-aGWAeeJFalrXhlxz7QPD6Vo1XK9ix3ACbGHr1TticACjsSgizY8hxnUmmm6gHeMRfKNY_d53Kzw2b4OhN7vBTNNlOnMS6YHy97DU4lQF3iwXVyAiDzrZm63M3vI1QUjXWzVVRK5SusIod47T6TYlT7mvZnk0-j1YQzwKvDHmseH3kzePZdxkLv-m87cpuzbnr0WW6V_15dpa_M4_REaRPS0sdUDQXt5beYAPg6cYo0NELUYsxxWbabz9FkHNk-m01oc3PolECXHcTxj2mfxL6CSSXnRk9LY2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12023699aa.mp4?token=d4L2A9tL6bkRptt2xkxmTjOYYPz26bcjj4fZByAbzb_FzI7xYX2-aGWAeeJFalrXhlxz7QPD6Vo1XK9ix3ACbGHr1TticACjsSgizY8hxnUmmm6gHeMRfKNY_d53Kzw2b4OhN7vBTNNlOnMS6YHy97DU4lQF3iwXVyAiDzrZm63M3vI1QUjXWzVVRK5SusIod47T6TYlT7mvZnk0-j1YQzwKvDHmseH3kzePZdxkLv-m87cpuzbnr0WW6V_15dpa_M4_REaRPS0sdUDQXt5beYAPg6cYo0NELUYsxxWbabz9FkHNk-m01oc3PolECXHcTxj2mfxL6CSSXnRk9LY2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز تحقیقات از متهمان اصلی پروندهٔ حمیدرضا رجب‌زاده / در تحقیقات اولیه متهمان به قتل اعتراف کردند  فراجا:
🔹
پس‌از دستگیری متهمان اصلی پروندهٔ حمیدرضا رجب‌زاده؛ تحقیقات و پی‌جویی، توسط کارآگاهانِ پلیس آگاهی در خصوص علت و چگونگی وقوع جنایت در جریان است. همچنین…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/680159" target="_blank">📅 00:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680157">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
گزافه‌گویی‌های فرستاده آمریکا به سازمان ملل علیه ایران
مایک والتز، فرستادهٔ آمریکا به سازمان ملل، در مصاحبه‌ای با شبکهٔ فاکس نیوز:
🔹
وقتی ایران پای میز مذاکره با مذاکره‌کنندگان ما می‌آید، صحبت از پول، پول، پول است. زیرا آنها بمباران‌ها را تحمل می‌کنند.
🔹
آنها به دنبال دسترسی به پول نقد و دارایی‌هایشان هستند که ما مسدود کرده‌ایم؛ این همان نقطهٔ فشار است.
🔹
این فشار همراه با محاصره، چیزی است که در نهایت باعث می‌شود ایران عقب‌نشینی کند. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/680157" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680154">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2ba2f533.mp4?token=kZCClHO5gVEkE9Fv5_jHrpb1K-2gV_Edeo94k29onbPZUvnTCdkQ_6L8IPxKb7Iqd-1iXDqsnQSxObv2KdS6Q04FvPHkUvm8cW-ENovYzFDGm2Pg-l-xjVsOaUPZdlLPI_19H1uC3-0ymeFIL-kT-hI8fyBmK9lUsvXIFps_kW2oRBcWes38s9UmzkO-jY7AiERpe5qjmfnWpnG4N3thb3AVeQ4ngf72fQxXN9PfFqyBQ1t2U_YXCpRWFZXiX6mJv1TT_QMN6TgctpHuAl0VNQRNijxzAYxSgzgPjSBajaa8KKIoLJeDukL33jNV58Enfp6dGjeRw_ZKqQ7VUAkQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2ba2f533.mp4?token=kZCClHO5gVEkE9Fv5_jHrpb1K-2gV_Edeo94k29onbPZUvnTCdkQ_6L8IPxKb7Iqd-1iXDqsnQSxObv2KdS6Q04FvPHkUvm8cW-ENovYzFDGm2Pg-l-xjVsOaUPZdlLPI_19H1uC3-0ymeFIL-kT-hI8fyBmK9lUsvXIFps_kW2oRBcWes38s9UmzkO-jY7AiERpe5qjmfnWpnG4N3thb3AVeQ4ngf72fQxXN9PfFqyBQ1t2U_YXCpRWFZXiX6mJv1TT_QMN6TgctpHuAl0VNQRNijxzAYxSgzgPjSBajaa8KKIoLJeDukL33jNV58Enfp6dGjeRw_ZKqQ7VUAkQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بذرها روی خط؛ گامی تازه برای کاشت منظم‌تر و بهره‌ورتر
🔹
در این روش، بذرها با فاصله‌ای مشخص روی نوارهای زیست‌تجزیه‌پذیر قرار می‌گیرند و سپس نوار در خاک کاشته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/680154" target="_blank">📅 00:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680153">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONGkQRrsN4R0Lq5DyARi1-22eyFHtI762BacF7jCjeYmzILkxiFhfChWilCspQvQow3dZ3cD1a2OOcwO407yC3A09zhMORjn0Egz31vNoPlg5xc6nYyo1pTDhe_7anjAcxbzY9qq61gc_ow_-E9xddZi341eDLOtM84w6QhSvKUpFH3EqwIu5y8q4PoEdOziA07H7XpGahxYi3C3o9xx6lGfm4UNg0fUaCrUFLK4pwdcSMMay8nQdlaPwtRGAeZ0rTaC9ZJLNkefn4KlWj4CgTyw3pJ8vmYyoTT2cpD9P4SSCQRCqzlovNc-yf3fm4GnRTROaF-cthGA_B2mTqNvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/680153" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سقوط صادرات فرش ایران از ۵۰۰ میلیون دلار به ۳۵ میلیون دلار
سپهرزاد، رئیس کمیسیون فرش دستباف کشور در اتاق اصناف ایران در
#گفتگو
با خبرفوری:
🔹
طبق آمار گمرک در سال ۱۴۰۴ میزان صادرات فرش دستباف معادل ۳۵ میلیون دلار بود، در حالی که در دهه ۷۰ و ۸۰ این رقم برابر با ۵۰۰ میلیون دلار در سال بود و تنها یکی از تجار ما در سال ۳۵ میلیون دلار صادر می‌کرد.
🔹
در سال ۲۰۰۰ سهم ایران در صادرات فرش در جهان به ۳۲ درصد و سهم هند به ۱۴ درصد می‌رسید و در سال ۲۰۱۹ این آمار برای ایران به ۸.۶ درصد و سهم هند به ۳۵ درصد رسید و در سال ۲۰۲۶ اصلا در این جدول نیستیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/680150" target="_blank">📅 23:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680148">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c45736caf.mp4?token=VbonF1QueRbExBpeqzYLxYELIUos4akwPI8aYadWpf462i20nXhBiWH0AGy7UlPs9_VN79qSOrpJVvgNy4AaiSfVJR5riNPHLIUn8sTsxO8p4z5hRhH5PCVGTOgFdLn8zfgLZFrpaE3wfBNQN_vbwGXXLCAC0N5U2iDf_aJlK5LaCG1OAYMywiBKKbc9gWKSBhY_bN4_Tf0NedkEYzwNXKTkd1y7MfUkUzVmN7mfSVLX-ZOazfMZiTMBlkZy1dLJEwkyFQhGtqVsceTvcTfrHGNi6X_wmuRyVIx4Mn99KnSx_g5frstEb4Y0WTLt5u6v-1H3mp106vw6qFTFp-UeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c45736caf.mp4?token=VbonF1QueRbExBpeqzYLxYELIUos4akwPI8aYadWpf462i20nXhBiWH0AGy7UlPs9_VN79qSOrpJVvgNy4AaiSfVJR5riNPHLIUn8sTsxO8p4z5hRhH5PCVGTOgFdLn8zfgLZFrpaE3wfBNQN_vbwGXXLCAC0N5U2iDf_aJlK5LaCG1OAYMywiBKKbc9gWKSBhY_bN4_Tf0NedkEYzwNXKTkd1y7MfUkUzVmN7mfSVLX-ZOazfMZiTMBlkZy1dLJEwkyFQhGtqVsceTvcTfrHGNi6X_wmuRyVIx4Mn99KnSx_g5frstEb4Y0WTLt5u6v-1H3mp106vw6qFTFp-UeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیاست ترامپ دیوانه: هر جا خوابت آمد؛ بخواب| وقتی رئیس‌جمهور آمریکا یک چرت مبسوط می‌زند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/680148" target="_blank">📅 23:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680143">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
معاملات ۵۵ میلیارد دلاری ایرانی‌ها در پلتفرم‌های رمزارز خارجی
🔹
داده‌های سال ۱۴۰۳ نشان می‌دهد حجم معاملات کاربران ایرانی در پلتفرم‌های رمزارزی خارجی به حدود ۴۰.۵ تا ۵۵.۵ میلیارد دلار رسیده است.
🔹
به گزارش TechRasa Insight حجم معاملات در پلتفرم‌های داخلی بین ۲۷ تا ۳۷ میلیارد دلار برآورد می‌شود. دسترسی گسترده‌تر صرافی‌های خارجی به معاملات آتی، اهرم‌های معاملاتی و ابزارهای حرفه‌ای ترید از مهم‌ترین عوامل جذب معامله‌گران ایرانی به این پلتفرم‌هاست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/680143" target="_blank">📅 23:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680142">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۵۶۸ هزار نفر در صف وام ازدواج هستند
علیرضا نثاری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مبلغ مصوب تسهیلات قرض‌الحسنه ازدواج ۳۵۰ میلیون تومان با کارمزد ۴ تا ۵ درصد است و حدود ۵۶۸ هزار نفر در صف انتظار دریافت این تسهیلات هستند و تنها حدود ۱۲ درصد از تسهیلات مصوب در چهار ماه اول سال پرداخت شده است.
🔹
بانک‌ها موظفند قسمتی از منابع داخلی خود را بابت پرداخت این تسهیلات به انجام رسانند و بانک مرکزی باید سهمیه‌های بانک‌های عامل را مشخص و تا پرداخت این تسهیلات به متقاضیان نظارت لازم را داشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/680142" target="_blank">📅 23:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680141">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9c6bb8.mp4?token=TwYgVwL3wOnXV5NGIQ4qDTOWyePGcMiQ1CuA_wmDz7LRZHjcf8etsW_JXgWKOqC0oSkKsgt3x8j2ADGEUghmboVFzrW_2TbkIfz2103ZUoP53zt3-Y50_eDO0uCxLiO5f9M6BGvPce5pSTPyayAhFDA2aHOVjY1TPvnH9qPey3nOmY4QSIUe09IxrGRliVJkWagAxdyNmU_NjfSNgeHKYbBznELimXPOFVl0bG4J01T3lJ8zSVGpaywnlJ29kWoajUVW-dFFD9lHEdEXACdbCgZ9gffdGd2AacOPGCAyZZNRfekHJLlY0cj3M-zI5GaL9YoNo-RLYj5ZpxfwjJRyxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9c6bb8.mp4?token=TwYgVwL3wOnXV5NGIQ4qDTOWyePGcMiQ1CuA_wmDz7LRZHjcf8etsW_JXgWKOqC0oSkKsgt3x8j2ADGEUghmboVFzrW_2TbkIfz2103ZUoP53zt3-Y50_eDO0uCxLiO5f9M6BGvPce5pSTPyayAhFDA2aHOVjY1TPvnH9qPey3nOmY4QSIUe09IxrGRliVJkWagAxdyNmU_NjfSNgeHKYbBznELimXPOFVl0bG4J01T3lJ8zSVGpaywnlJ29kWoajUVW-dFFD9lHEdEXACdbCgZ9gffdGd2AacOPGCAyZZNRfekHJLlY0cj3M-zI5GaL9YoNo-RLYj5ZpxfwjJRyxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشگر: آیا پاسخی به نتانیاهو دارید؟
ترامپ:
🔹
من امروز در شبکه "تروث سوشال" (Truth Social) پاسخی را منتشر کردم. پاسخی خوب دارم. رابطه ما بسیار خوب است، بله
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/680141" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680140">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9343495b20.mp4?token=vdXJVVVKZAmnFP_MyEL-HuXD2XtHL2C5ptEsSi2tk3nea_iqudn-r_c1dCbua-Z4odmB_XPjjU4BKFBmLdQn6EngNOw4RMqe_zpf8FcBsUtCcGat-XOIBd4qMx7Ty73rK7rqCUMqgotFkjZH4pU8rFaJ1jx-rLeSu2z3q3CTfZH8iyiosrqZL_C9ZauFp0pSbgwazJg3jBlan7yYkV6s1-mOoJfd4lMttLzdDmJ30dWidnqVt3x1WpCKH5C5JyMOQs_3cIywCu6lIEk0L5EQkciG2Un8kX5VuahDWhwvV2qUFIP56-JcqMaBSyJft7k2XW1SAEcdXH36sdHH9TUvwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9343495b20.mp4?token=vdXJVVVKZAmnFP_MyEL-HuXD2XtHL2C5ptEsSi2tk3nea_iqudn-r_c1dCbua-Z4odmB_XPjjU4BKFBmLdQn6EngNOw4RMqe_zpf8FcBsUtCcGat-XOIBd4qMx7Ty73rK7rqCUMqgotFkjZH4pU8rFaJ1jx-rLeSu2z3q3CTfZH8iyiosrqZL_C9ZauFp0pSbgwazJg3jBlan7yYkV6s1-mOoJfd4lMttLzdDmJ30dWidnqVt3x1WpCKH5C5JyMOQs_3cIywCu6lIEk0L5EQkciG2Un8kX5VuahDWhwvV2qUFIP56-JcqMaBSyJft7k2XW1SAEcdXH36sdHH9TUvwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی اساس ترامپ دروغگو درباره ایران: آنها می‌توانند مشکلات ایجاد کنند، اما ورشکسته هستند، آنها پولی ندارند
🔹
ایران کاملاً ورشکسته است. آنها به سربازان خود حقوق نمی‌دهند.
🔹
نرخ تورم آنها ۳۰۹ درصد است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/680140" target="_blank">📅 23:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680139">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697393a302.mp4?token=L6PuCi8L3dEQpp8DvRfubP0qwMEGFVqG3qe0CxHsqCHdcd4iMon0Cg5EdXWMKwcrsuyiJtPgUP2tuFACFvc1c168Hq91SZuaVsVFPAdrRqWNH9x4SoENrN2Q3kzzcdkgGKF29r7A2hxC0NXInYw2cO2oIEXvOogb5VIgAxBt9OPMn5n-eC3Os4oe8fmDt7r-QyBmkDH64qBd1PdJ7FiNRUs6HSXxUOUtVBg9ZUCmrSADSBOZbH0LFnHafP0HqYQ4VQKI8a1leoTapyiuLO7J6Uany3sFafPRi2VhLHDacy6NvViy96DPtHH1H2dR2sXFyQaXAlbk26CtgJKa6yrecQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697393a302.mp4?token=L6PuCi8L3dEQpp8DvRfubP0qwMEGFVqG3qe0CxHsqCHdcd4iMon0Cg5EdXWMKwcrsuyiJtPgUP2tuFACFvc1c168Hq91SZuaVsVFPAdrRqWNH9x4SoENrN2Q3kzzcdkgGKF29r7A2hxC0NXInYw2cO2oIEXvOogb5VIgAxBt9OPMn5n-eC3Os4oe8fmDt7r-QyBmkDH64qBd1PdJ7FiNRUs6HSXxUOUtVBg9ZUCmrSADSBOZbH0LFnHafP0HqYQ4VQKI8a1leoTapyiuLO7J6Uany3sFafPRi2VhLHDacy6NvViy96DPtHH1H2dR2sXFyQaXAlbk26CtgJKa6yrecQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات مضحک ترامپ جنایتکار درباره ایران: ایرانی ها صدها هزار نفر را به قتل رسانده‌اند
🔹
اکنون آن‌ها در حال پرداخت بهای این اعمال خود هستند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/680139" target="_blank">📅 23:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680138">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f23aa183c1.mp4?token=i2jw1WzJHCsSy1iwqK4VnmqpCJP-3NnqHyUyCtV5ptoLCd388iaVzi4cdlxXjh1kmBsZ7sLhDKA6u3m9VnXKU7nwRg7sowI1yHAXNA8K65aFiHkGZmw025LiE5ERSlEz_hwXhV2H2_7x77J3IJwgdRObxJqnL-ZwBIqFtZrzFVYKRZ81f2hbIDw6oTjI378xzoswG6WkXI6G7tTLD-SIrGpc8wiSJGCrzYtDsO58lqUHgj8z_9LVcc6uL6pxhI26sWlucGbFo9O-8Uw9gKU49jryuBNp2zOnZQ7PDDq7waWz5DMZdu5bVsKyV3MYy_TSeYvnvGyMXU75l8DQXrtCZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f23aa183c1.mp4?token=i2jw1WzJHCsSy1iwqK4VnmqpCJP-3NnqHyUyCtV5ptoLCd388iaVzi4cdlxXjh1kmBsZ7sLhDKA6u3m9VnXKU7nwRg7sowI1yHAXNA8K65aFiHkGZmw025LiE5ERSlEz_hwXhV2H2_7x77J3IJwgdRObxJqnL-ZwBIqFtZrzFVYKRZ81f2hbIDw6oTjI378xzoswG6WkXI6G7tTLD-SIrGpc8wiSJGCrzYtDsO58lqUHgj8z_9LVcc6uL6pxhI26sWlucGbFo9O-8Uw9gKU49jryuBNp2zOnZQ7PDDq7waWz5DMZdu5bVsKyV3MYy_TSeYvnvGyMXU75l8DQXrtCZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشگر: تنگه هرمز چه زمانی باز خواهد شد؟
ترامپ دیوانه:
🔹
الان باز است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/680138" target="_blank">📅 23:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680137">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c51c663d55.mp4?token=bVUqEOZRM7EUqAAdz7oeS3fy3zEcr8ecqhSZunnjiYUL0RIG9RDh_caXWuJuFhmLkUpvdNtmDE-POz1CC-F68Rgwm2plPW5GH7VmiOHbwVxjqbCUggeYKVlXQ0HmADroE-lAYM2SEnQcRjHkBeReEIDJsPQREBVgA5pWKS7xkT8hfUsUdXDnqZRMcNw4gC_qSG-O-SAHdySl2AAAmVfj0Mu_BVzMUDIPhxu-3OUkLhSRpUZyDZTWxh8yx32kpLSMFILs2K73zvvjTtX0X-WKdOA9sQVDQNzdek6XoY42MQC1cQstcO_QwSnM3oZhE_ftr8sCn4k4NdECr1TBhmjApg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c51c663d55.mp4?token=bVUqEOZRM7EUqAAdz7oeS3fy3zEcr8ecqhSZunnjiYUL0RIG9RDh_caXWuJuFhmLkUpvdNtmDE-POz1CC-F68Rgwm2plPW5GH7VmiOHbwVxjqbCUggeYKVlXQ0HmADroE-lAYM2SEnQcRjHkBeReEIDJsPQREBVgA5pWKS7xkT8hfUsUdXDnqZRMcNw4gC_qSG-O-SAHdySl2AAAmVfj0Mu_BVzMUDIPhxu-3OUkLhSRpUZyDZTWxh8yx32kpLSMFILs2K73zvvjTtX0X-WKdOA9sQVDQNzdek6XoY42MQC1cQstcO_QwSnM3oZhE_ftr8sCn4k4NdECr1TBhmjApg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات ترامپ شیاد درباره ایران: همانطور که احتمالاً شنیده‌اید، ما تمام تنگه را پاکسازی مین کرده‌ایم، شاید شما این را نشنیده باشید
🔹
ما کنترل ۱۰۰ درصدی این تنگه را در اختیار داریم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/680137" target="_blank">📅 23:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680136">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44cff11291.mp4?token=JzIqrMz06W_dT_3yqvsSAOOGXwLlknbXB_oYmZg82CHF_e3llwW0xHglgxXw_3Q0jIXdE5CBHEMICy2gQt6MvxloN7-KKdHeYMKtJVhaBKA1GiJ5RcRIfup0eq3Y-8sM0DdKdrFUvZnTN4aiGDIL2b4qwDv9bGNU6Btq56BhrSTkLDo9Y4v0hNydvwgW2Jm90FrkkTeC1YQl_SBjfQbymRB0xfqnHaJKx4SiXHW8jbzfhEwEvO-tklRcViT3C9soUfXAvOZx53SPrbcYodEAuF6rwagfUFNPTaTZJcbLzefQZw6iesltfzH_N-y2Qsye7yurX3IQnnOLBssCRNcWog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44cff11291.mp4?token=JzIqrMz06W_dT_3yqvsSAOOGXwLlknbXB_oYmZg82CHF_e3llwW0xHglgxXw_3Q0jIXdE5CBHEMICy2gQt6MvxloN7-KKdHeYMKtJVhaBKA1GiJ5RcRIfup0eq3Y-8sM0DdKdrFUvZnTN4aiGDIL2b4qwDv9bGNU6Btq56BhrSTkLDo9Y4v0hNydvwgW2Jm90FrkkTeC1YQl_SBjfQbymRB0xfqnHaJKx4SiXHW8jbzfhEwEvO-tklRcViT3C9soUfXAvOZx53SPrbcYodEAuF6rwagfUFNPTaTZJcbLzefQZw6iesltfzH_N-y2Qsye7yurX3IQnnOLBssCRNcWog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: گاهی اوقات دوست دارم من هم سنا را از بین ببرم، اما این را نمی‌گویم، من این کار را انجام نمی‌دهم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/680136" target="_blank">📅 23:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680135">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f8a136fe.mp4?token=D7t5y_5hA1lWiqcEYLooIiSvbgJtmhMJYORcNaZdIifjWGzJZNqvpe35icKgVcidosnfnOZFJqqGY6qlaXCLa42FZbK0vN4QbAOsT69EciFm5nLOKA1g44VBQaL-bhWyyXIxgsYMdFS0Rv0s-nx-tDsi4-hgnXeZeuxu3CfYitOJ5bwCtSpQAQ2uh7_v-qELNAGbVRaG7Oed-iXDcy2NtGxLtfHhID1TQz-ZF77dRpdg5sqyHl7DPCuncvA2H9o_M1hxrdFNRny5-E9mK84ByCAjPVEw9EuS0eMLqhrSQsZjNCl805NUPFiXwxns-lvPtsWp1C2dcxXBPH3J2x686h4UnVqMxq7UKlUvh7-_dfwklXfuHBLL1weJYJ8B334BFbw0Mz6ny2Q_6eOQw1MBjvOuTR6x7HgtzSc1B3w4GY3bXF7ZuarJNx8QFADVkYiYICE4Val0NRrB556dDzSXQOlD6Z3A8Hnbb6qQUqxw1HXC0iJirOqQWSDhVxgjLfyxNnyMLbEIEg_5p7T0Q9G8yLq8H_Hc1QgHReL-fQ78mG0bFcLNIuKWQjslyOfFiKXSY-UZOZtciTZNzyiiB-H8kitxzVFpS7PIGDDX2OEeNZGdL-uBgX5Sa04zBn4ylQsM3gzGlaCZHcCTFyf-Da8O_PPp_RUHgDv2ZtIIsPG90ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f8a136fe.mp4?token=D7t5y_5hA1lWiqcEYLooIiSvbgJtmhMJYORcNaZdIifjWGzJZNqvpe35icKgVcidosnfnOZFJqqGY6qlaXCLa42FZbK0vN4QbAOsT69EciFm5nLOKA1g44VBQaL-bhWyyXIxgsYMdFS0Rv0s-nx-tDsi4-hgnXeZeuxu3CfYitOJ5bwCtSpQAQ2uh7_v-qELNAGbVRaG7Oed-iXDcy2NtGxLtfHhID1TQz-ZF77dRpdg5sqyHl7DPCuncvA2H9o_M1hxrdFNRny5-E9mK84ByCAjPVEw9EuS0eMLqhrSQsZjNCl805NUPFiXwxns-lvPtsWp1C2dcxXBPH3J2x686h4UnVqMxq7UKlUvh7-_dfwklXfuHBLL1weJYJ8B334BFbw0Mz6ny2Q_6eOQw1MBjvOuTR6x7HgtzSc1B3w4GY3bXF7ZuarJNx8QFADVkYiYICE4Val0NRrB556dDzSXQOlD6Z3A8Hnbb6qQUqxw1HXC0iJirOqQWSDhVxgjLfyxNnyMLbEIEg_5p7T0Q9G8yLq8H_Hc1QgHReL-fQ78mG0bFcLNIuKWQjslyOfFiKXSY-UZOZtciTZNzyiiB-H8kitxzVFpS7PIGDDX2OEeNZGdL-uBgX5Sa04zBn4ylQsM3gzGlaCZHcCTFyf-Da8O_PPp_RUHgDv2ZtIIsPG90ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ما شاهد انتخاب افرادی هستیم که دیدگاه‌های جهادی دارند، تقریباً در همه جا، ما با کمونیسم و جهادگرایی روبرو هستیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/680135" target="_blank">📅 23:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680134">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/856b799e72.mp4?token=sbxWZLfdMow7sOf-dL1KuDuTGzpNeB71ejKqpIauidZUVERa0eSOjAm8oOEB8VvvXjw-cEjBMKdnJLQ3Ybgz_lmE2RR_-jPfMq8dKdrKg3ZKs8QsNyzLQQgeXdXbMmnDwjHfvXnmdrb6OHN59IoGreqGrJDYBNrmGarqX8QTyJgMY40ovWDo_zFbuUS-4hG8Obt2Bq05tZ4rpox6lntyWT44eAtXRit9ITTLhLe5yYn_70ByArXTHAF1LGGtEykpuIQupAlV1BZyKP-ONAcsRpkD9VMICyebgqo03SxfgOG8M6e0CnfmkLr5PxvBPzWoybZ3AfHIvEwQgXig4tiAIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/856b799e72.mp4?token=sbxWZLfdMow7sOf-dL1KuDuTGzpNeB71ejKqpIauidZUVERa0eSOjAm8oOEB8VvvXjw-cEjBMKdnJLQ3Ybgz_lmE2RR_-jPfMq8dKdrKg3ZKs8QsNyzLQQgeXdXbMmnDwjHfvXnmdrb6OHN59IoGreqGrJDYBNrmGarqX8QTyJgMY40ovWDo_zFbuUS-4hG8Obt2Bq05tZ4rpox6lntyWT44eAtXRit9ITTLhLe5yYn_70ByArXTHAF1LGGtEykpuIQupAlV1BZyKP-ONAcsRpkD9VMICyebgqo03SxfgOG8M6e0CnfmkLr5PxvBPzWoybZ3AfHIvEwQgXig4tiAIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دروغگو: رئیس‌جمهور بعدی، اعتبار زیادی را به خاطر کارهایی که من انجام داده‌ام، کسب خواهد کرد
🔹
لطفاً به یاد داشته باشید که این کارها را من انجام داده‌ام، نه آن‌ها
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/680134" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680133">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1030697b.mp4?token=g-cd_y_fAq2h0Lq3dYkjhJ_57vap2Ih8XquZKAJ1nX9XkxMO_cWutLkaQZefY8iPB3HD59JId_veug_G6HKGdkBgdiU8_-A1UJ1PtBKNRMsqk3ekm_bDlM9RWZmkqJuSQHPQ9_Tri4-gBKCBL2NdxrxjOl9Z8V-m4L4K3qccD94Ck_EFEjxLlFrhrdvkH5F5S1oFwFZ8HtyHfMeWxgP8t9YzqDnPadpDtxj38PHfqOB-HONzQ2z7b7emQ2HjDgYeQeyyHn4JJd63Z0sD8SBnTV6QGBjOF-2-xeNH1n_1g5G9_cGusUs7x1ET3vSqnvYscPTSlIKRodBnZGL4uJCK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1030697b.mp4?token=g-cd_y_fAq2h0Lq3dYkjhJ_57vap2Ih8XquZKAJ1nX9XkxMO_cWutLkaQZefY8iPB3HD59JId_veug_G6HKGdkBgdiU8_-A1UJ1PtBKNRMsqk3ekm_bDlM9RWZmkqJuSQHPQ9_Tri4-gBKCBL2NdxrxjOl9Z8V-m4L4K3qccD94Ck_EFEjxLlFrhrdvkH5F5S1oFwFZ8HtyHfMeWxgP8t9YzqDnPadpDtxj38PHfqOB-HONzQ2z7b7emQ2HjDgYeQeyyHn4JJd63Z0sD8SBnTV6QGBjOF-2-xeNH1n_1g5G9_cGusUs7x1ET3vSqnvYscPTSlIKRodBnZGL4uJCK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ شیاد: هیچ اتفاق بدی از کارهایی که ما انجام می‌دهیم، نخواهد افتاد، هیچ اتفاق بدی رخ نخواهد داد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/680133" target="_blank">📅 23:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680132">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b9a07b7a.mp4?token=fQV_RG63GuKTMDN9MbtKHLiw0yV8euhu2jG_FxXuDNeQ6dUeStQvXLbcxxt3ormJs-laUF8sLJpjvZx3h6TBcZZmYXZxuFINWW5GzSfKua1DFdl9quZoFfuJXKS8ryesEi3QbiDKjLRb2xOJEU2AkruVY1Iiw-EYg0vLbUlu3LFKgvzKMjXS4wi-rTAljk9GqAufFO1FOYSCylGKnQIQlJ5coAwUrNsEFMQyXBPWALsH-U-5c6kruqVOhsPTBRfOx4SuqYgTUdnKJ1rtZ4GBtRaHv7SuuxLuDVDKDTQmFnmWjzPm4PnaJEcxiUjfU51EeD3eFEzDoei106FY4zTDVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b9a07b7a.mp4?token=fQV_RG63GuKTMDN9MbtKHLiw0yV8euhu2jG_FxXuDNeQ6dUeStQvXLbcxxt3ormJs-laUF8sLJpjvZx3h6TBcZZmYXZxuFINWW5GzSfKua1DFdl9quZoFfuJXKS8ryesEi3QbiDKjLRb2xOJEU2AkruVY1Iiw-EYg0vLbUlu3LFKgvzKMjXS4wi-rTAljk9GqAufFO1FOYSCylGKnQIQlJ5coAwUrNsEFMQyXBPWALsH-U-5c6kruqVOhsPTBRfOx4SuqYgTUdnKJ1rtZ4GBtRaHv7SuuxLuDVDKDTQmFnmWjzPm4PnaJEcxiUjfU51EeD3eFEzDoei106FY4zTDVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: برخی از گروه‌ها تقریباً هیچ مشکلی با اوتیسم ندارند
🔹
این گروه‌ها، افرادی هستند که به شدت به دنیای واکسن‌ها علاقه‌مندند.
🔹
هر سال، میزان ابتلا به اوتیسم افزایش می‌یابد، و این افزایش روز به روز بیشتر می‌شود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/680132" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680131">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa584be63.mp4?token=QlU5x0Y2x5m0YDoGIuQYSsTDJFPAca3DxIBphdeOCw6UfuktDc1P_S87d76wJcH1xalXMiHKr7cJQ1aFgykoiiIWB-3vhpDC2FhUBZ3hAj8jfmqbWfYLCkWd_rWwuGdm4y5PL7ASGHINrN58bhesI3VHWZnVKT1U8xMci7EG2yfANRrOlD6DNXmaFBh2Xk6JFz3NjhpSFX8MvhQBkWawgVdLOtlSEoOlttKjloGTdgpheQ4whFqW54-Ph_oIBqUiTsl5pbtg2qeyvyGQW8wMpb_K1S-xAdrudlUqCkrcDJac9AtWDps2dWXvruaAwe4NUhGubZKonrUjoyA4_m4JRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa584be63.mp4?token=QlU5x0Y2x5m0YDoGIuQYSsTDJFPAca3DxIBphdeOCw6UfuktDc1P_S87d76wJcH1xalXMiHKr7cJQ1aFgykoiiIWB-3vhpDC2FhUBZ3hAj8jfmqbWfYLCkWd_rWwuGdm4y5PL7ASGHINrN58bhesI3VHWZnVKT1U8xMci7EG2yfANRrOlD6DNXmaFBh2Xk6JFz3NjhpSFX8MvhQBkWawgVdLOtlSEoOlttKjloGTdgpheQ4whFqW54-Ph_oIBqUiTsl5pbtg2qeyvyGQW8wMpb_K1S-xAdrudlUqCkrcDJac9AtWDps2dWXvruaAwe4NUhGubZKonrUjoyA4_m4JRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ده‌ها سال پیش، کودکان تنها بخش کوچکی از واکسن‌هایی را دریافت می‌کردند که امروزه مورد نیاز است
🔹
در آن زمان‌ها، مردم بسیار سالم‌تر بودند و البته، میزان بالای اختلال اوتیسمی که امروزه مشاهده می‌شود، وجود نداشت.
🔹
دلیلی برای این میزان بالای شیوع اختلال اوتیسم وجود دارد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/680131" target="_blank">📅 23:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680130">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02f617be6.mp4?token=kDoDhzFWz_QalZGYWP2rExennIjxyi0N5DGsK8iLQpaOS2E9hUQk8bmZjJzt48IPRmyJAYKYwmqCdqnETjAfTvTzFW6qWhGH9ipHRX9L4lhcg_g5oG-9hV4Pyn9unc6HCOX5sNRXGOpNzZNmr3JxpqZnpPRPu2Tmu-smuBpLIMyiBxfFcVZnCk09cKVo88COlJN8gHuu2LX8aBH0rVVGSfRUzIBqCXIPquQk2VaXxhqiRpVFgL_guUj4_9yXg83vUOe8WYK-U502oJrkgA4tuK7Nif_7dtTaclabDzTgdG2OR7Jazh_zXMDuyFrDyalWkGkLuNwM54qB2ktvtcI2bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02f617be6.mp4?token=kDoDhzFWz_QalZGYWP2rExennIjxyi0N5DGsK8iLQpaOS2E9hUQk8bmZjJzt48IPRmyJAYKYwmqCdqnETjAfTvTzFW6qWhGH9ipHRX9L4lhcg_g5oG-9hV4Pyn9unc6HCOX5sNRXGOpNzZNmr3JxpqZnpPRPu2Tmu-smuBpLIMyiBxfFcVZnCk09cKVo88COlJN8gHuu2LX8aBH0rVVGSfRUzIBqCXIPquQk2VaXxhqiRpVFgL_guUj4_9yXg83vUOe8WYK-U502oJrkgA4tuK7Nif_7dtTaclabDzTgdG2OR7Jazh_zXMDuyFrDyalWkGkLuNwM54qB2ktvtcI2bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دیوانه: واکسیناسیون برای بیماری‌هایی مانند هپاتیت B، کووید-19 و آنفولانزا، و سایر بیماری‌ها، دیگر برای همه کودکان توصیه نمی‌شود
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/680130" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680129">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c3bdfc9.mp4?token=NPzUbCgRncQBI16gm0a8TdAgjW5tzMHiHY2imXsZ72UBlsi22zc3pYA0uXQudk2NaEm8ZFLWIcWWV0IyaGOB6Gr4J5w2SvpPbcVjue7b88XhGA7swUlsUOG4Le6WlBf-tZP61nkHo2BdhXVB7YAIf-TbsLsrfduDplgC4Z3sDWQvLfc596lw7teOCq1VJHYT-TryyyiVHxE1nnMZW454iNGS-kT03orpJ6elt8dx7PJNlD_-pdr3GfxSMpO_mKCRNrgffLU_QMmUrQH91Pz0ae1axXpeSxAx9c2o5szUbsIHgaSBP3SH_7sduoay8z9yMRDZe1SvMYUPqZoimnlbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c3bdfc9.mp4?token=NPzUbCgRncQBI16gm0a8TdAgjW5tzMHiHY2imXsZ72UBlsi22zc3pYA0uXQudk2NaEm8ZFLWIcWWV0IyaGOB6Gr4J5w2SvpPbcVjue7b88XhGA7swUlsUOG4Le6WlBf-tZP61nkHo2BdhXVB7YAIf-TbsLsrfduDplgC4Z3sDWQvLfc596lw7teOCq1VJHYT-TryyyiVHxE1nnMZW454iNGS-kT03orpJ6elt8dx7PJNlD_-pdr3GfxSMpO_mKCRNrgffLU_QMmUrQH91Pz0ae1axXpeSxAx9c2o5szUbsIHgaSBP3SH_7sduoay8z9yMRDZe1SvMYUPqZoimnlbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه اتفاقی خواهد افتاد؟
ترامپ:
🔹
شما متوجه خواهید شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/680129" target="_blank">📅 23:02 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

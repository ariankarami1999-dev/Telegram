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
<img src="https://cdn4.telesco.pe/file/rr-yTw7LaHsD1liy1FAwbi4sHkmJm1qiXVPdqIUzakMu-165OvxxRcT-apcGXa-08v3rTPeZ7cNrTg2PG1sQX_GZkqLP5mn0jsJCFjCWx_oUWeLiYU4nsiA8etf1PIiEE2uq71nDOaluRZxiZ3oKlr145nGPQmMyJXCAZ3SQbXWLmJonAGyS78JOLVtSsTHGs-QX1QzOihPe6TtYjyB8-QBcKw2XvpBTe7wmhiMBAsBHvsxcBvm9Yybkqk9x6j1DiAG08GT3m3YKCKi1l8HSLsol1fniQp7sVqILk-uS6xc7_xRNSw7DlBG6uE0t1o-AYwcypBPwrQgu1xHwhKZYgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 327K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 03:43:59</div>
<hr>

<div class="tg-post" id="msg-14690">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">محسن رضایی:
ترامپ با آزادسازی 24 میلیارد دلار از دارایی‌های بلوکه‌شدۀ ایران موافقت کرده اما با صراحت این موضوع رو اعلام نمیکنه.
@withyashar
🥴</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/withyashar/14690" target="_blank">📅 02:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14689">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeHMgVq98Xv53vjSlWjvNT4F5vgBXKiB9GcaOVTwmJhWwS_dVwja1ysfgybLyueV5DZwRw5xmXtJh4NM920Od17U1Hm2R7RcDL7e744v6Q4xdlvtvsncQj9NlyoZKgZc4StRly4gLUvbvRS7JOY58npyg3GXSFjpVsI2AVdpMmbOu4AWkreYssznE7gb3AZ9Ee49Sx3JVo2Gzssqd9mFlMgCA-__1a9fAsdpqeqRlF0Y51IsxX0jtRA74DX7gKYr8syCDt7O0m1AvVIv1vWBX34rZwMU3bWiDWhxeSy7tTEA6v4SN5ix9FxjG-75WXCSZ-k5UouJ-NVmEeYLofL74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشروی ارتش اسرائیل در جنوب لبنان؛ ۶.۷ کیلومتر تا نبطیه
ارتش اسرائیل به شهر ارنون رسیده و هم اکنون در حال حملات توپخانه ای سنگین به تپه علی الطاهر هستند.  l بالگرد های آپاچی ۶۴ اسرائیلی نیز به تپه علی الطاهر حمله کردند.  با تصرف این تپه مهم رسما تصرف شهر نبطیه برای اسرائیلی ها آسان خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/14689" target="_blank">📅 02:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14688">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">Bombardier E-11A در منطقه توضیح در ویس @withyashar</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/withyashar/14688" target="_blank">📅 01:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14686">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRmKOUgtUlJj4oAjptE9KOok3obJ1WV7Bvge_oeY2-7hhAXgELTDeLnhBm4PRvBAuiKJbI2SPXcKmnNelShfp3f1mBl71WylyVIeMoPsAjTo1NCGXMLP5PWPhsmfvhb5VBg0syl-8bsYyOYm5loIYPri-pG7judFlSr9mcAqS4mX3xYGvcdpWCGMdoWtBbBPHe9ORB7WIsxKriZ9yFLm8kGkOEU0Iz1LbpuCOagkB9_wJcZGyo0WWgLDfrbVhDJqJ98Aupil81Z7rkV5kFcA9pndNtdvluS0KgVio3OwawUSh_UsdErPTMtqPhgfr0jrFq3YlxnldBQk4U1XdctxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Bombardier E-11A در منطقه توضیح در ویس
@withyashar</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/withyashar/14686" target="_blank">📅 01:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14685">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/14685" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14684">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyX3utef_YyE3DLPyBIMMHQ6hMe8vMwfAcaf4kkX9E22KNeIujg26CoTle7PDGHOvH8TAt7VxEWb_J4q7bM6nM2tSGhZfDj0s-NlJG_q27S-VgPj6-o-D4jCpMdUi75dT9rXi4W_eS0rRRXVynDgmzmiommsKFnInTn6Jtb-zDcUqHZ4INyjJVpdsvutkxQiBWcdQqBjOLoyJeRzlYBgrHKADaI44jbplvFvq9iwrNXIMx3ip69KUrHQ3MpOgjbW5am3IoYe1x61DIkDr6mL6_BPEXtz0Qa7tu734Y8BzC69Tbn74ZtUWMjQHYnv3M_haNd582u8Zn1f3-CVSYI-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ادعای رویترز بابت آزادسازی دارایی های ایرانو تکذیب کرد
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/14684" target="_blank">📅 01:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14683">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Khabam Nemibare Live(IG @yashar)</div>
  <div class="tg-doc-extra">Amir tataloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/14683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/14683" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14682">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/14682" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14681">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/14681" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14680">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار :  باز‌ تنگه دعوا شد ، گزارش عجیب از حضور هواپیماهای جاسوسی آمریکا همه با هم. !!!⁩
https://www.instagram.com/reel/DZgA2cQxrjS/?igsh=cnM5b3ViejIxcm5t
کلیک کنید و کارهای اداری پست را انجام دهید.</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/14680" target="_blank">📅 00:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14679">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کاور  @withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/14679" target="_blank">📅 00:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14678">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۳پا : کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/14678" target="_blank">📅 00:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14677">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1ff8xU_nN4vE7VqEqWljwp2w5X1B5dWF1dnxfmwf2_zGYVkxSU40EZr3PQochLeAMrDh_ETEpISK5yzV3XnXBYQM99zECG4xP4faihidC5YMu6tSyfQ4QEbAgYHen014nHEvOQqD9GBuPA_KQqa5D2eqmhoHkd4jrDWKrJpqIL-MesHXAJpvbD98JzTos99HJmXlWgVyopDFvV72Q4xdE9kn9IYtaPrOYeh81AFdXqn1J1IEOO0U_YGdtH6V96uOMusmuRXRxxpPL-xh4d8TIH3K_kPsSSsR0TvsL05KVXlbEa33EyV6ZDDWmwzazqR15g7oTOv6eWMiDGI10MrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/14677" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14676">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تو تنگه دعوا شد
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/14676" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14675">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مهر : شنیده شدن صدای انفجار در حوالی جزیره قشم و سیریک؛ گمانه‌زنی از درگیری دریایی
بررسی‌های اولیه نشان می‌دهد، در پهنه شهرستان سیریک انفجاری رخ نداده است و احتمالا صدای شنیده شده تلاشی برای کنترل تنگه هرمز و از سوی دریا بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/14675" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14674">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/14674" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14673">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">صدای انفجار سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/14673" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14672">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عراقچی: در مذاکرات ۶۰ روزه چند حالت رخ می‌دهد
۱. تمدید مهلت مذاکرات در صورت خوب‌پیش‌رفتن مذاکرات.
۲. نرسیدن به توافق، به‌علت بی‌فایده‌بودن مذاکره‌.
بستگی به شرایط آن موقع تصمیم می‌گیریم که اگر نتیجه نگیریم چه خواهد شد.
تنها کاری که می‌توانیم برای اورانیوم غنی‌شده انجام دهیم "رقیق‌سازی در داخل" است!
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14672" target="_blank">📅 23:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14671">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عراقچی:به‌زودی ایران و عمان بیانیه مشترکی در مورد اداره تنگه هرمز منتشر خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14671" target="_blank">📅 23:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14670">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی: عوارض نخواهیم گرفت اما هزینه خدمات میگیریم
ممکن است در دوره ۶۰ روزه این مورد کمی متفاوت باشد
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14670" target="_blank">📅 23:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14669">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عراقچی:  این توافق دشمنایی داره که اسرائیل اصلی ترینشونه
امیدواریم تفاهم‌نامه امضا بشه ولی اگر نشه وارد دور بعدی مذاکرات نمیشیم
اگر قرار بود به تهدیدهای حمله به زیرساخت‌های خود تن دهیم، قبلاً این کار را انجام داده بودیم.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14669" target="_blank">📅 23:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14668">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عراقچی: به صراحت میگم که این توافق دشمنانی داره که در راس آنها اسرائیله.
سکوت کنن رسانه ها که برسیم به توافق خوب
وقتی ما به توافق میرسیم که دو طرف راضی باشن
حالا توافق 50/50 هم نیست و درصدش مهم نیست
مهم اینه که توافق کنیم
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14668" target="_blank">📅 23:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14667">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عراقچی: نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم
بهترین زمان برای پایان دادن به جنگ زمانی است که دست بالا را داریم؛ ما واقعاً در میدان نبرد پیروزیم.
ما به مدت ۴۰ روز در برابر ابرقدرت ظاهری جهان ایستادیم.
توافق و پایان جنگ، پیروزی را تثبیت خواهد کرد.
توافق نهایی هنوز حاصل نشده است؛ اگر نهایی شود، قول می‌دهم هر بند را به طور کامل توضیح دهم.
توافق شامل دو مرحله است و ما مسئله هسته‌ای را به مرحله دوم منتقل کرده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14667" target="_blank">📅 22:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14666">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15f030f45.mp4?token=IjuJVfncy7AkJInSemklO2CTRoJ5H2nMAy0IARdRjC_IgwZOUjO94FZOKnmNLKNk7OnGgNX4cwGcqqHoJQbccf4_v6zgN728nKCD0um0N1_ZMkF0CRHREFLUW3Q2EW7-Fw4TUHCJVzTEilJIft4FrVAEoD1biWRHKQf-2K1yaOOUjxMWSKn6ZGRGKeYIfADw0Hbzt6PLpPaydPjkuUWBE5yrOGaBnPd5aqg37Ufm9oH_rpsn-xdFNnEzigeYcsLlOBbDi16Zt6rxyZYJ6NpuNWM-My4wYzrS2IHzeou1l4NDDcXdfq1THZfC-WTxN6BGisNYnxJCp-jsyX6PkkOAnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15f030f45.mp4?token=IjuJVfncy7AkJInSemklO2CTRoJ5H2nMAy0IARdRjC_IgwZOUjO94FZOKnmNLKNk7OnGgNX4cwGcqqHoJQbccf4_v6zgN728nKCD0um0N1_ZMkF0CRHREFLUW3Q2EW7-Fw4TUHCJVzTEilJIft4FrVAEoD1biWRHKQf-2K1yaOOUjxMWSKn6ZGRGKeYIfADw0Hbzt6PLpPaydPjkuUWBE5yrOGaBnPd5aqg37Ufm9oH_rpsn-xdFNnEzigeYcsLlOBbDi16Zt6rxyZYJ6NpuNWM-My4wYzrS2IHzeou1l4NDDcXdfq1THZfC-WTxN6BGisNYnxJCp-jsyX6PkkOAnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند مشهد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14666" target="_blank">📅 22:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14665">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14435d52ae.mp4?token=RWIkdkm6CGUm5f_5deLtJCIj7NEEwjSmvLd7TSoGmjaf9Rc3SyZVnxZzkciZpU4CDyTVERaeHeG1GmWxEHCwK8unrjxCKWBXIaKhezd-y7sSsh1ixxvtjzFisNlyL97C776e6Zz3LE7hsJVBagSLbY1PSBUidbRT3CBFArPf4tNFMXczhM_dMjQS1maYXMOhSREDLygryKEkaePxFvgUFXg9C5sRwxg0JmLo6icGx8niyMc49m5QfK9NfI682BrbM8NLKA22kmP93qZxsmiMgzkrVvHqlf_smHMSRX0bUcBP3P92gLfNO4sI9QgpMm3EB1bebqoTGCjO8a6Hg56DEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14435d52ae.mp4?token=RWIkdkm6CGUm5f_5deLtJCIj7NEEwjSmvLd7TSoGmjaf9Rc3SyZVnxZzkciZpU4CDyTVERaeHeG1GmWxEHCwK8unrjxCKWBXIaKhezd-y7sSsh1ixxvtjzFisNlyL97C776e6Zz3LE7hsJVBagSLbY1PSBUidbRT3CBFArPf4tNFMXczhM_dMjQS1maYXMOhSREDLygryKEkaePxFvgUFXg9C5sRwxg0JmLo6icGx8niyMc49m5QfK9NfI682BrbM8NLKA22kmP93qZxsmiMgzkrVvHqlf_smHMSRX0bUcBP3P92gLfNO4sI9QgpMm3EB1bebqoTGCjO8a6Hg56DEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشهای زیاد شما از مشاهده چندین پهپاد شناسایی هم اکنون در آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/14665" target="_blank">📅 22:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14664">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea29ba51ad.mp4?token=sqNWUm8l6wpvSqe72QW7L_sB7VQC_aNFttMdCAKP-H8oX8JG9iELllI4xChV86cm-y9Xu5y1j4CUWAfvbCYv2wMbDDzwfNzLSd_NPDfMiedeTh3rtGYlszJ3EOExHJ7e9nXUIHrSF2uNemZPet6iaF-RApXltuO-vDnRo1uTGvrhUJqqdUfB2k_Ru053miVhgkRmLQoZwigQ8Vkq_mKH8cYpUgtn3jDndDci03PdnLIJPX_ijAY_9Pvu8aylxpT-qej6gVTtHJmeVNXIhUY80ju38SeN6FV6WU5p16zMERjxKMFIKx6ccXrqNwNNb5XsxVqapFS1PWFXoxqU0JfzBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea29ba51ad.mp4?token=sqNWUm8l6wpvSqe72QW7L_sB7VQC_aNFttMdCAKP-H8oX8JG9iELllI4xChV86cm-y9Xu5y1j4CUWAfvbCYv2wMbDDzwfNzLSd_NPDfMiedeTh3rtGYlszJ3EOExHJ7e9nXUIHrSF2uNemZPet6iaF-RApXltuO-vDnRo1uTGvrhUJqqdUfB2k_Ru053miVhgkRmLQoZwigQ8Vkq_mKH8cYpUgtn3jDndDci03PdnLIJPX_ijAY_9Pvu8aylxpT-qej6gVTtHJmeVNXIhUY80ju38SeN6FV6WU5p16zMERjxKMFIKx6ccXrqNwNNb5XsxVqapFS1PWFXoxqU0JfzBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهام شرکت فضایی و موشک‌سازی SpaceX که تحت مالکیت ایلان ماسک قرار دارد، امروز برای نخستین بار در بازار بورس آمریکا عرضه شد و معاملات آن با قیمت ۱۳۵ دلار به ازای هر سهم آغاز شد.
عرضه اولیه این شرکت توانست بیش‌ از ۷۵ میلیارد دلار سرمایه جدید جذب کند و ارزش کلی اسپیس‌ایکس را به حدود ۱.۷۸ تریلیون دلار برساند.
در پی این جهش تاریخی، ثروت ایلان ماسک از مرز یک تریلیون دلار عبور کرد و او رسماً عنوان نخستین تریلیونر تاریخ را به خود اختصاص داد.
در لحظه نگارش این متن هر سهم حدود ۱۷۰$ است
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14664" target="_blank">📅 22:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14663">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حزب‌الله:
بر اساس آنچه مقامات ایرانی به ما گفته‌اند، اسرائیل بر اساس این توافق از خاک لبنان عقب‌نشینی خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/14663" target="_blank">📅 22:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14662">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">طبق گزارش ها،فرمانده کل سپاه، احمد وحیدی با شرایط متن تفاهم نامه ایران و آمریکا موافق نبوده متن تفاهم نامه با همکاری عراقچی و قالیباف تنظیم شده است و پس از مخالفت فرمانده سپاه به رهبری در ایران ارسال شده،
رهبری در ایران نیز تاکنون مانند دفعات قبلی متن تفاهم نامه را تایید نکرده
@withyashar
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14662" target="_blank">📅 21:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14661">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سازمان ملل: از روند مذاکرات دلگرم شدیم!
@withyashar
😁</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14661" target="_blank">📅 21:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14660">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرنگار فاکس‌نیوز نزدیک به ترامپ از نقل یک مقام کاخ سفید درباره توافق :
۱. مواد هسته‌ای نابود و منتقل خواهند شد.
۲. برنامه هسته‌ای برچیده خواهد شد.
۳. هیچ‌یک از پول‌هایشان تا زمانی که تعهداتشان را انجام ندهند آزاد نخواهد شد.
۴. تنگه هرمز باز خواهد بود.
۵. هیچ تأمین مالی از سوی ایران برای گروه‌های تروریستی وجود نخواهد داشت.
این مقام افزود: «این همان چیزی است که آنها با آن موافقت کرده‌اند. این یک توافق مبتنی بر عملکرد است.»
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14660" target="_blank">📅 21:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14659">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الحدث: وزیر خارجه پاکستان امشب عازم ژنو می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14659" target="_blank">📅 21:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14658">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز:
توافق با ایران اهداف اصلی ایالات متحده را محقق می کند
این توافق تنگه هرمز را بازگشایی خواهد کرد، ایالات متحده مواد هسته ای غنی شده دریافت خواهد کرد.
توافق ایران همچنین شامل یک رژیم بازرسی است. اگر ایران رعایت کند، پاداش اقتصادی خواهد داشت.
منافع برای ایران تنها در صورتی حاصل می شود که آنها واقعاً به تعهدات خود عمل کنند.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14658" target="_blank">📅 21:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14657">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانال 12 اسرائیل : سرانجام توافق شد ؛ این توافق قطعیه و به نتانیاهو اعلام شد!
ترامپ از ایران خواسته به‌صورت علنی درباره توافق شفاف‌سازی کنه و هشدار داده در صورت انجام ندادن این کار، با پیامدهایی روبه‌رو خواهد شد.
ترامپ در تماس تلفنی با نتانیاهو گفته:
«این همون توافقیه که دنبالش بودیم؛ یک توافق عالیه و وقتشه این جنگ تموم بشه.»
طبق این گزارش، نتانیاهو در این گفت‌وگو زیاد حرفی نزده و ظاهراً متوجه شده که توافق در آستانه نهایی شدنه و توانایی متوقف کردنش رو نداره.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14657" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14656">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آکسیوس: ترامپ به بنیامین نتانیاهو نخست وزیر اسرائیل خبر داد زمان پایان دادن به جنگ ایران فرا رسیده
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/14656" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14655">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بقایی، سخنگوی هیأت مذاکره:
همین الان جلسهٔ نهادهای ذی‌ربط درحال برگزاری است؛ در مورد متن تفاهم ما در مراحل جمع‌بندی در داخل هستیم
اینکه گفته می‌شود ما خیلی به تفاهم نزدیک هستیم، حرف جدیدی نیست
مشکلی که ما در این مدت داشتیم اظهارات ضدونقیض طرف مقابل است.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14655" target="_blank">📅 21:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14654">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: جمهوری اسلامی به‌طور محرمانه بابت ارائه اطلاعات نادرست در مورد توافق عذرخواهی کرد.
@withyashar
😁</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/14654" target="_blank">📅 20:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ثابتی:متن توافق احتمالی از برجام هم ضعیف‌تره و نه گشایش اقتصادی ایجاد می‌کنه و نه جلوی جنگ رو می‌گیره
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14653" target="_blank">📅 20:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14652">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ : پست اخیر عباس عراقچی، وزیر خارجه ایران، درباره توافق را بسیار مثبت ارزیابی می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14652" target="_blank">📅 20:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14651">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ : هنوز هم معتقدم که توافق ممکنه تا پایان این هفته یا نهایتاً روز دوشنبه امضا بشه.
ایران به‌صورت محرمانه بابت ارائه اطلاعات نادرست درباره توافق عذرخواهی کرده
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14651" target="_blank">📅 20:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14650">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وزیر جنگ اسرائیل: رئیس‌جمهور ترامپ در حال حاضر به سمت توافقی با ایران پیش می‌رود که از دیدگاه منافع آمریکا، از جمله منافع مشترک با اسرائیل—برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای است و ما انتظار داریم او این اصل و اصول اضافی در حوزه موشک‌ها و نمایندگان نیابتی را حفظ کند.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14650" target="_blank">📅 19:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14649">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سناتور لیندسی گراهام:
بسیار خوشحالم که ترامپ گزارش رسانه‌های ایران را جعلی خواند، چرا که آن توافق افتضاح بود
آنها در ضعیف‌ترین وضعیت خود در ۴۷ سال اخیر قرار دارند.
ما نباید فراموش کنیم که نظام ایران ۴۲ هزار نفر را تنها به دلیل خواست زندگی بهتر کشت.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14649" target="_blank">📅 19:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14648">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به گفته‌ی CNBC معاملات سهام  اسپیس اکس $SPCX تا پنج دقیقه‌ی دیگر آغاز می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14648" target="_blank">📅 19:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14647">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6u-G1qs00HiyPT4Ds2K26AU3ZDbHVfRzJ8Glj-TUki7KxIZSEHf_LvSjUUWh0j-Ny9BkzErX1JMKd3lL6RjjqX9M6RlQnSBWbHq0qvQh6kwoofzHyM_L83BHrHWgVN945TN3A9UXgeXlwELJLkYVaqjBfwr8_W0i9YwFBE0VFZym-bbxvgVtFhPGXkI2_CfUf8H_ka-gxII8xdsj1f8d6hWqyHaGu13Q-6rsDbpi9cVNatqR0Iv6ZoezNEBGKPoO92DLDyrA975vNCuGvqWd2VSnD_hwjkIG3xqNOCzKVY5ghn6fAZuLwJU9-U9dawvdTnHWuAOu627frH5KjsBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چپقچی، وزیر خارجه: حفظ یادداشت تفاهم اسلام‌آباد هرگز به این اندازه نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از ورود به حدس و گمان درباره محتوای آن خودداری کنند.  در راستای رویکرد مسئولانه و شفاف ما، تمام جزئیات در زمان مناسب با عموم مردم به اشتراک…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14647" target="_blank">📅 19:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14646">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اوهو‌ووووو‌‌
🤣</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14646" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14645">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جی‌ دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود
این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد. این توافق پتانسیل بازسازی منطقه و منجر شدن به صلح پایدار را دارد.
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14645" target="_blank">📅 19:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14644">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سناتور لیندزی گراهام: ایدهٔ یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی در ایران مسئول است، به نظر بی‌توجه می‌آید.
این مانند طرح مارشال برای آلمان است در حالی که نازی‌ها هنوز در قدرت هستند.
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/14644" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14643">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بعدن میگم
🥶</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/14643" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14642">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه چیز بگم مغزتون سوت بکشه
🤯</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/14642" target="_blank">📅 18:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14641">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جی دی ونس، معاون ترامپ:
این توافق به گونه‌ای ساختاربندی شده است که نگرانی‌های آمریکا و متحدانش در اولویت قرار گیرد و اگر جمهوری اسلامی ایران به تعهدات خود عمل کند، منافع اقتصادی به آن‌ها و کل منطقه خواهد رسید. این توافق پتانسیل بازسازی منطقه و ایجاد صلح پایدار را دارد.
در گزارش‌های چند ساعت گذشته چند نکته عجیب دیده‌ام. اول، افرادی که (به درستی) یک ماه پیش گفته بودند دونالد ترامپ رئیس‌جمهور تاریخی بود، اکنون بر اساس گزارش‌های رسانه‌ای تأییدنشده از توافق انتقاد می‌کنند. دوم، افرادی که می‌گویند نمی‌توان به هیچ کلمه‌ای از سپاه پاسداران اعتماد کرد، ظاهراً به پست‌های ناشناس در شبکه‌های اجتماعی باور دارند.
رئیس‌جمهور به هر حال نتیجه خوبی برای ما به دست خواهد آورد.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14641" target="_blank">📅 18:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14640">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چپقچی، وزیر خارجه: حفظ یادداشت تفاهم اسلام‌آباد هرگز به این اندازه نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از ورود به حدس و گمان درباره محتوای آن خودداری کنند.
در راستای رویکرد مسئولانه و شفاف ما، تمام جزئیات در زمان مناسب با عموم مردم به اشتراک گذاشته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14640" target="_blank">📅 18:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14639">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14639" target="_blank">📅 18:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14638">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDqmHQKm4gCjaA1lPAWNGICkEWGgBYZBPtMicXodsudBoy8tIvR_U_fpL3-37IZzRGMaaXNP89RAfw5O0aLGJlPLLbMWzvOQ39hdGj-fHu-KqZVXToAeSBy0PAtNA4WU94CTy1dhmNYH_zO4hUbCPIhT3Fdj5SV1bZ8ruevyfAsTLkZir9VW0dLJ_hWeznD5zihg4JdU8_EHzhONqg15mRyWLIoeTRJ3mKClpXNgiobtXvstBvJU6_UTjW-qYBahweBFXzJJQkMmQwBbLKgRlaWPz1dTDZ2RZE8XVEAF5R2ujX-xOPPRNs9pvaUo8_pWQMGKz5Jurxd3EJaz96HpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : مفادی که ایران به رسانه‌های جعلی (Fake News) درز داده است، هیچ ارتباطی با مفادی که به‌صورت مکتوب بر سر آن‌ها توافق شده بود، ندارد.
آنچه آن‌ها گفته‌اند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود یک توافق، هیچ نسبتی با حقیقت ندارد.
آن‌ها افرادی بسیار بی‌شرافت برای مذاکره و معامله هستند. در مورد آن‌ها، چیزی به نام مذاکره و رفتار با حسن نیت وجود ندارد. شگفت‌انگیز است!
همچنین، حمله پهپادی کاملاً ناکام‌مانده آن‌ها دیشب علیه کشتی‌های هندی که در حال خروج از تنگه هرمز بودند، کاملاً غیرقابل قبول است.
بهتر است هرچه سریع‌تر اوضاع خود را سر و سامان دهند؛ وگرنه با عواقب آن روبه‌رو خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14638" target="_blank">📅 17:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14637">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرنگار وال‌استریت ژورنال: برای اینکه توافقی شکل بگیره، مهمتر از تایید مجتبی خامنه‌ای، تایید فرمانده‌های ارشد سپاهه.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14637" target="_blank">📅 17:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14636">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منبع ارشد در تیم مذاکره کننده ایران:
یادداشت تفاهم نامه برای ورود به مذاکرات میان ایران و آمریکا نهایی نشده است و در حال بررسی است و
هرگونه امضای یادداشت تفاهم در روز های آینده کذب است
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14636" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14635">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏شاهزاده رضا پهلوی: در ایران نوین با مافیایی شدن ورزش مقابله خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14635" target="_blank">📅 16:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14634">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رویترز: توافق توسط جی‌دی ونس و قالیباف امضا می‌شود.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14634" target="_blank">📅 16:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14633">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نبویان: ما آمریکا رو زدیم زمین، رو سینه‌اش نشستیم که کار رو تموم کنیم یهو رفتیم پای میز مذاکره، میخوایم توافقی بکنیم که اون بیاد بشینه رو سینه ما اخه.
@withyashar
😂
🍋
🍋</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14633" target="_blank">📅 15:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14632">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع اسرائیلی:
اسرائیل به آمریکا فشار میاره تا دارایی‌های مسدود شده ایران رو به عنوان بخشی از یادداشت تفاهم آزاد نکنه.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14632" target="_blank">📅 15:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14631">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1qOwEv2C_syxeLaKR5S704biiNyuDpCCQmSGnffVjtp_lCeLS3TQyGo4Gxy8LVdx2-SklhfjHk-4-18FMKm5niEZt5isOnarEka_whmMNawZDWkEHoRV0_Bd2GRRk2NRv_1SubBv9ILUkTYBInXwxdHEbG1WJfxTEWPON0zOH2yJ03qKfQIGM57UXrpLZ2VRS-Qq_5XD0z219drLqu_nUIrPef8EEWrJHEsKPKuxFgWL0Z8dxFbPUWoywYR94fU2ypg1KNSIXWIT90I21fzIcmTTLM0tCpQpOGYp_IqyeFgVwZGqa5XI4dLxQJNCLq3QAYWWdicGckC8AbKkJgLnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ناوهای جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان در آب‌های منطقه‌ای به گشت‌زنی ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند.
تا امروز، نیروهای آمریکا ۱۳۶ شناور را تغییر مسیر داده‌اند و ۹ شناور را از کار انداخته‌اند تا از رعایت این محاصره اطمینان حاصل شود.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14631" target="_blank">📅 15:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14630">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرگزاری ایرنا درباره جزئیات توافق احتمالی میان جمهوری اسلامی و آمریکا:
متن یک توافق برای پایان جنگ با دقت بسیار بالا و وسواس زیاد تدوین شده و هیچ مجالی برای تفسیر خودسرانه یا فرار از تعهدات از سمت هیچ‌یک از طرفین در این توافق وجود نداره.
در این یادداشت تفاهم هیچ توافقی درباره پرونده هسته‌ای حاصل نخواهد شد و جمهوری اسلامی هیچ تعهد جدیدی ارائه نخواهد کرد!
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14630" target="_blank">📅 15:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14629">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو:
تا وقتی من نخست‌وزیر اسرائیل باشم، ایران به سلاح هسته‌ای دست پیدا نخواهد کرد.
من و ترامپ در این موضوع کاملاً هم‌نظر هستیم.
بیش از ۳۰ ساله که در خط مقدم مقابله با برنامه هسته‌ای ایران حضور دارم.
اگر این تلاش‌ها نبود، ایران سال‌ها پیش به بمب اتمی دست پیدا کرده بود؛ بمب‌هایی که به گفته او برای نابودی اسرائیل استفاده می‌شدند.
ایران به‌دنبال نابودی اسرائیله و من زندگی‌ام رو وقف جلوگیری از این موضوع کردم. تا وقتی نخست‌وزیر اسرائیل باشم، اجازه نمی‌دم چنین اتفاقی بیفته
.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14629" target="_blank">📅 15:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14628">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فارس: هر گمانه‌زنی دربارۀ امضا در سوئیس یا دیدار حضوری، چیزی جز فهم اشتباه از پیشنهادها و آرزوهای آمریکایی نیست!
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14628" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14627">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ایرنا؛ تفاهم‌نامه پایان جنگ چه مسائل و موضوعاتی را در بر می‌گیرد؟
۱.
موضوع هسته‌ای دست‌نخورده باقی می‌ماند
هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت ۶۰ روزه پس از امضا انجام خواهد شد.
۲.
تنگه هرمز؛ نه واگذاری، نه نقش آمریکا
ایران هیچ تعهدی در مورد واگذاری مدیریت تنگه هرمز نمی‌دهد. آینده اداره تنگه در چارچوب یک امر منطقه‌ای و از طریق گفت‌وگو و تصمیم گیری مشترک تهران با عمان حل و فصل می‌شود.
۳.
پایان قاطع جنگ در تمام جبهه‌ها، از جمله لبنان
هدف اصلی تفاهم‌نامه، پایان جنگ در تمامی جبهه‌های منطقه است. آمریکا تعهد می‌دهد که اسرائیل را وادار به پایان جنگ در لبنان کند و عبارت «تمدید آتش‌بس» در متن جایی ندارد.
۴.
آزادی دارایی‌های مسدودشده با ساز و کار مشخص
بخشی از دارایی‌های مسدودشده بلافاصله پس از امضا و بقیه به تدریج در طول مذاکرات آزاد خواهند شد. تهران تضمین‌های روشنی بر اساس ساز و کارهای مورد نظر خود دریافت کرده است.
۵.
غرامت جنگ در دستور کار
خسارات وارده به ایران در تجاوز آمریکا و اسرائیل از جمله موارد مورد اشاره در تفاهم‌نامه است. ساز و کار اجرایی دریافت غرامت در مذاکرات ۶۰ روزه پس از امضا مورد توافق قرار خواهد گرفت.
۶. جزییات رفع تحریم‌های اولیه و ثانویه؛ موضوع مورد بحث در توافق نهایی
رفع تمامی تحریم‌های آمریکا و قطعنامه‌های بین‌المللی در مهلت ۶۰ روزه مذاکرات هسته‌ای بررسی می‌شود.
۷. سه موضوع و ۶۰ روز برای توافق نهایی
در مذاکرات ۶۰ روزه تنها سه موضوع بررسی می‌شود: استمرار برنامه صلح‌آمیز هسته‌ای، رفع تحریم‌های یکجانبه آمریکا، و ساز و کار جبران خسارات. هیچ موضوع دیگری در از جمله توانمندی موشکی ایران، دستور کار نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14627" target="_blank">📅 14:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14626">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سخنگوی وزارت خارجه : متن نهایی تفاهم‌نامه تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد!
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/14626" target="_blank">📅 14:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14625">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مهر : توی توافق با آمریکا، واشنگتن متعهد شده بخشی از تحریم‌ها رو برداره و نیروهاش رو هم از اطراف ایران عقب بکشه
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14625" target="_blank">📅 14:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14624">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرگزاری فارس : آمریکا ترسیده و عقب نشینی کرده ولی ما هنوز داریم پیشنهادات رو بررسی میکنیم و جواب خاصی هنوز بهشون ندادیم !
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14624" target="_blank">📅 14:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14623">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری دولت: هدف اصلی امضای تفاهم‌نامه، پایان جنگ در تمامی جبهه‌ها در منطقه است. در این تفاهم‌نامه پایان جنگ علیه ایران به اضافه تمامی جبهه‌های دیگر منطقه به در برگرفتن لبنان هم مورد اشاره قرار گرفته‌است.
عبارت تمدید آتش‌بس در متن فعلی ذکر نشده‌است و اشاره به چنین عبارتی در برخی گزارش‌های رسانه‌ای نادرست است؛ متن تفاهم‌نامه خواهان پایان قاطع جنگ در تمام جبهه‌ها می‌شود.
تهران تضمین‌های روشنی برای آزادی دارایی‌های مسدود شده بر اساس ساز و کارهای مشخص و مورد نظر تهران دریافت کرده‌ است و در صورت تصمیم تهران به امضای تفاهم‌نامه پایان جنگ، بخشی از دارایی‌های مسدود شده بلافاصله و بقیه به تدریج در طول مذاکرات، آزاد خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14623" target="_blank">📅 14:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14622">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYHfrJFQPlt7xn1Wjv-ouMpWZkR5hOazVk4HNyCgg57Vxg4f-3-9AAdFREzJx5S9CM4P_Uw3A6XddG7zc47k7AQRoYOMWrS5krdYeXmUy6j5vvm56-3gzZoSK-eaaXU0ec39Bxdp5od9ZrvsBcPMJAM30LS2I74R9kg4Ktn6YZQWRUAHBjslWBdeoMouej3JxoV-Uw1dxVdATNLtaOJ9aE0PfkXWpqS0Q93qZDdI1GzEsrHNdWeNYhIa52W39mVEF0yaCVDXgy2wRZb6QiN3O-_CsTpzDs6iR7cTNOhp3H9nJi3SFUSkuM9zi0wlHEsFbri7XNtuxwoO7O8uQ8n0ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی اعلام دونالد ترامپ مبنی بر  احتمال امضای قریب‌الوقوع توافق با ایران، قیمت جهانی نفت 5 درصد کاهش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14622" target="_blank">📅 14:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14621">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">️تسنیم مجددا این خبر رو منتشر کرد:
متن تفاهم تا این لحظه در مراجع ذی‌صلاح جمهوری اسلامی به تایید نهایی نرسیده.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14621" target="_blank">📅 13:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14620">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسرائیل هیوم: ایران موافقت کرده است اورانیوم غنی‌شده خود را تحویل دهد.
از غنی‌سازی بلندمدت صرف‌نظر کندو  آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.
ایران باید متعهد شود که به دنبال دستیابی به سلاح هسته‌ای نباشد. تنگه هرمز بدون محدودیت باز خواهد شد. هر دو طرف متعهد می‌شوند که اقدامات نظامی بیشتری علیه یکدیگر انجام ندهند.
پرونده لبنان همچنان شکافی بین آمریکا و ایران باقی مانده است. انتظار می‌رود یادداشت تفاهم روز یکشنبه در ژنو امضا شود، در حالی که ترامپ برای اجلاس جی۷ در فرانسه حضور دارد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14620" target="_blank">📅 13:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14619">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بلومبرگ به نقل از یک مقام گروه هفت: توافق بین واشنگتن و تهران به احتمال زیاد یک یادداشت تفاهم خواهد بود، نه یک توافق نهایی
!
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14619" target="_blank">📅 13:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14618">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ادعای آکسیوی : شرایط توافق بین امریکا و ایران:
1. باز شدن فوری تنگه هرمز
بدون دریافت عوارض یا محدودیت جدید.
2. برگشت ترافیک دریایی حجم حمل‌ونقل و کشتیرانی ظرف ۳۰ روز به سطح قبل از درگیری‌ها برگرده
3. لغو محاصره دریایی آمریکا
4. تمدید آتش‌بس به مدت ۶۰ روز شامل لبنان
5. ادامه مذاکرات هسته‌ای
6. توافق دوم برای پرونده هسته‌ای
7. تسهیل محدود فروش نفت برای ایران
8. کاهش تحریم‌ها به‌صورت مشروط
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14618" target="_blank">📅 12:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14617">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رسانه عبری i24: از جزئیات توافقی که تاکنون اعلام شده کاملاً مشخص است که ایران تضمین‌هایی از آمریکایی دریافت خواهد کرد مبنی بر این‌که اسرائیل تا پایان دوران ترامپ هیچ‌گونه فعالیتی در خاک ایران انجام ندهد
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14617" target="_blank">📅 12:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14616">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شبکه ۱۲ اسرائیل:
مذاکرات نهایی ایران و آمریکا بر مسائل اقتصادی و هسته‌ای متمرکز خواهد بود و شامل بحث‌هایی درباره برنامه موشک‌های بالستیک ایران نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14616" target="_blank">📅 12:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14615">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hzd-oUwBtDKyj0i7bkDUxhzqeHvelNzssPnp8ZJaGp5s9NjRM-Qv0FAk_pblO3kFqKmNu9ipMk43BphTtxGc8cqlngX7j7-Ydr6VTZ_y9qvtUb6jg_jSLK7ldJIxFU1bkPKkLvwWDs-uac6PbOg63UPvt3zffQ2IrPPGmHrU0ElntKC1wnyk3MzwSbOQ8WP-c-IsIS-kPUjKruVgaVIfkpkaqGl2IlzqjtPSelo-udpDKr1mItFPhm4nlpbRVPDVt0X5JHedqXGUEOJpxwF8zKh7QeMmn1HEEmKirCj2r3ZrU6VU-US6Zy3h97F9tPtQ29w0_lB5Du-lfeh4N8Al8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات امروز اسرائیل به جنوب لبنان شروع شد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14615" target="_blank">📅 12:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14614">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIXIQQ3-AGkt03gLvrI1CUOmuno-tzi6FOMQp7iikeZkC3KKDa-ciE5zabL1hbV_DUWt6JQwkLwylAR5E1DCGESert1I3cK3saOOQahEyVT5fQij02wlwFKIta4nwr_tis0MTfawu64tpKc_S2dUqEZ11GSWRJOaomZhYuG_iHO9MqfAMdE1QPZnLmrRYktDdip2jFY208hJwbTzJpb3CL0CkqtsOzd_nqWbTk53nL6EUYgvD_FLzXlrlxxxTEi0hZLvCjplaRwXpvamQjwPtYDm5nZfwecS70S9tZlt_mgwOLVgSrFTXujsEuiTafo6QrYeH1oroaE6WCQEw9Rk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش یکی از طرفداران تندرو تجمعات شبانه حکومتی
@withyashar
🥴</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14614" target="_blank">📅 12:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14613">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یدیعوت آحارونوت:
نتانیاهو گفت که به ترامپ اطمینان داده است که تلاش‌های او برای رسیدن به توافق با ایران را درک می‌کند، اما اسرائیل نباید قربانی چنین توافقی شود
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14613" target="_blank">📅 12:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14612">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کارشناس شبکه خبر:  با صراحت میگویم که متاسفانه بخش عمده ای از شروط ده‌گانه رهبری در توافق وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14612" target="_blank">📅 11:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14611">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffd5b99a6.mp4?token=Mr_C1rAH1uHuutirnUFdlBEusHizaRA00QxCegJliGBrO0RaOwgwnXcLGi4DbXAw1yvS4fxbxw9JaHJsyCdh5F46G4_CKhe4I_GvVlAdCmuzcGGL8TO7VbaOQvgTqs_UmXOiF1BsEXBv0g4O2RcJPdhdjLsBA8FwAYmZBpx7hLDhFwPPRDoY1MgL9-ybdeF8qz_RVCpM8qpgErVgfpAg4t7QAf9jqFKLZ29VkO-iasaWgzofJIkPBjGpUkzEOze1p9KmrM9UMsKE3aETYRbWhlc7Owh0Q89z5hOcIKqP9p1LQm-GyNanYEmaEDWe82sJDXTV5qXiRl_-oI4yvm3sZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffd5b99a6.mp4?token=Mr_C1rAH1uHuutirnUFdlBEusHizaRA00QxCegJliGBrO0RaOwgwnXcLGi4DbXAw1yvS4fxbxw9JaHJsyCdh5F46G4_CKhe4I_GvVlAdCmuzcGGL8TO7VbaOQvgTqs_UmXOiF1BsEXBv0g4O2RcJPdhdjLsBA8FwAYmZBpx7hLDhFwPPRDoY1MgL9-ybdeF8qz_RVCpM8qpgErVgfpAg4t7QAf9jqFKLZ29VkO-iasaWgzofJIkPBjGpUkzEOze1p9KmrM9UMsKE3aETYRbWhlc7Owh0Q89z5hOcIKqP9p1LQm-GyNanYEmaEDWe82sJDXTV5qXiRl_-oI4yvm3sZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکرار ۳۹ باره ادعای «نزدیکی به توافق» توسط ترامپ از زمان شروع جنگ
شبکه CNN با انتشار ویدیویی از اظهارات دونالد ترامپ، نشان داده که او از زمان آغاز جنگ با ایران، دست‌کم ۳۹ بار ادعای «نزدیک شدن به توافق» را مطرح کرده است. این در حالی است که با وجود این تکرارها، هنوز توافق نهایی امضا نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14611" target="_blank">📅 11:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14610">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اکسیوس :  توافق ایران و آمریکا در ژنو سوئیس امضا خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14610" target="_blank">📅 11:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14609">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14609" target="_blank">📅 11:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14608">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کامنتم هم زیر پست ترامپ، کارهای اداریش را انجام بدهد فقط همین رو لایک کنید  https://www.instagram.com/p/DZdJ2LZvAza/?carousel_share_child_media_id=3917330556395457754_347696668&comment_id=18055196378739071</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14608" target="_blank">📅 10:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14607">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی:   احتمال فریب از سوی ترامپ بالاست
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14607" target="_blank">📅 10:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14606">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14606" target="_blank">📅 10:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14605">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14605" target="_blank">📅 10:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14604">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14604" target="_blank">📅 10:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14603">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14603" target="_blank">📅 10:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14602">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تولد بیبه
🥴</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14602" target="_blank">📅 10:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14601">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14601" target="_blank">📅 10:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14600">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی:
واشینگتن، تهران و قطر در مورد سازوکاری بحث کردند که به تهران اجازه دهد از وجوه مسدود شده برای خرید کالاهای بشردوستانه استفاده کند.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14600" target="_blank">📅 10:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14599">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اکسیوس: چهار فروند هواپیمای ترابری C-17 نیروی هوایی آمریکا روز پنجشنبه به سمت اروپا پرواز کردند و تجهیزات لازم برای احتمال سفر جی‌دی‌ونس به مراسم امضای توافق در ژنو طی روزهای آینده را منتقل کردند
.
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/14599" target="_blank">📅 09:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14598">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ: با ایران به توافق رسیدیم، توافق خیلی خوبی بود، دیگه هیچ سلاح هسته‌ای در کار نخواهد بود. تقریباً همه‌چیز نهایی شده و ما به هر چیزی که می‌خواستیم رسیدیم. مهم‌ترین بخش ماجرا اینه که ایران هیچ سلاح هسته‌ای نه خودش می‌سازه و نه از جایی می‌خره.
ما امروز جنگ با ایران رو پایان دادیم و آنها موافقت کردن که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن اصرار داشتیم. این هدف اصلی بود. این 95 درصد از کل موضوع رو تشکیل میده، و آنها این کار رو به قوی‌ترین شکل ممکن انجام دادن.
@withyashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/14598" target="_blank">📅 06:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14597">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فارس: یه کشتی متخلف تو هرمز رو هدف قرار دادیم دلیل صدای انفجار سیریک همین بود
@withyashar</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/14597" target="_blank">📅 01:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14596">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqObpL9I4aLPiZtcfu5P1BNgyAY1QWysdeuo58aBxr_V7W1gbS5en7ZqiarWpTrPwMmuWHZMHCcva0mX6sVYHZk1WQGJ_d7xsG5a7JYjPvUwkExvZ8fBQT0AiBktJQpL4Af-yP0upYuwn8kQETrtdjyi_AQI6ibPWEUfl62OPan_IByiPOqYeq_fpOlOwXh-Ho1LQ1jJAJW6NmfzKzP9ALH1e5ZKRy8CEs0CS-hKLkaDxNwyxfG-GmHx-ugNo9mIANJPLo6r61TArGEsl_QAel8_YLTI9jYMsIazqSC-yxu61H_BLFsiAJiVj5bHW_tEKLZkzCFKx6deCHNWnRii_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت توافق به سبک خاورمیانه
@withyashar</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/14596" target="_blank">📅 01:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14595">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZN3gigb5OWM51ntADaSSqUp9jpM7Vb1XPxlaHelu8xMCjqTomA7ZzGarQUfrK1I_eNUYsBde_2fS3TU6LIV2JMnY61F9Jcq97MeCn3dvKrN3_dLk9fGXwwRODgF1w6cpaqtQTdhSwt4F4ZB9s7X_KjjR3N6b4OfEUdebx8_yZFLuVwAhTONiO9kBH8WLFNQ8teKYWc4Nvf0V2uOqt2b0T45b6wyvPg2cdhQ4oJ4MHNkfm2hgy8obtJRdVuBLh0vn9AHdTTi3FOZZNpQ6b-oyHYXlCvWRlhiKyRcewqpcwivpjoz3_kqg-QFtotCSkknMLeBmBqMYk5qROaCBSnzCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه اف۳۵  کد اضطراری 7700 داد!!
فرود اضطراری
@withyashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/14595" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14594">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صداوسیما: دو انفجار در بندرعباس شنیده شده.
@withyashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/14594" target="_blank">📅 01:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14593">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZOlXTXDE88t3sTZ5D5oEyKB4Fl7BZUw-rrmNeHx4b-642Wt21NNTgZPhsMkIu62w4qU8lkS2xvVqyAn8M8oeZwoR8dzT-Qxtm7Cy0XCL9vVonENzZnW2Jz8UoFaUREwb0NhLExOeveEli-hAugM4B8rSzWrzCRWCYfHXbmcDKn6Ef4bWNFYORFB3Kcd9Qdgxs-iw3M3Gt7-edIpbM873D8qyTosiGroJXLvBCI3vwPvqT9bCF_LB7tqH-JJzntQQ85eKObYVJ4dMoHkg3Vh4CtuV8I7_AeaEhsiao_yqS4WAGrkY7ULz2LHfRwv8hcpTreI21d1-3_YJSt7gy6pmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : هر کی میگه الان تو جنوب کشور جنگ نیست، ببرش کنار یکی بخابون زیر گوشش.
@withyashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/14593" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14592">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صدای انفجار در بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/14592" target="_blank">📅 01:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14591">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صداوسیما:
برخی منابع آگاه صدای انفجارها را مرتبط با مدیریت و بسته نگه داشتن تنگه هرمز می‌دانند
.
@withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/14591" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14590">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش صدای انفجار در گناوه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/14590" target="_blank">📅 00:52 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

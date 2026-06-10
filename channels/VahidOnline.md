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
<img src="https://cdn1.telesco.pe/file/GTh1yUrPp6k1hrNNLuGeiMc_-1Urh8T9mucjgHP-paY1SOR34x5X5IAZz5t73hL8zcCV952Hq7J--xvlmgRUq6PjqTCycI1921EoJW5KMWW1QLyvnEEBw0ObvtQ3wzMeDJ5q3Nn2Awdr7jdiF0qYB1RtwNasoLzTPrhfHmlTMm3vKX-h_-dJiJ9XJ_YbL91D7xtQfq-iTzq3udamZhlCOo-TiKX3lEHf4c4yLrVSMMMROOK3IP-FQoVPI1LigO6pgfDrGfuTR-Zp30n9JdDR0dnNKd0Sx4bYW2089XtGznDTu5NfmiPOaC_22pyhZTJ9qDfKTHj3HTTVqZXTayPnBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 03:23:56</div>
<hr>

<div class="tg-post" id="msg-76177">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bEwYiI1idwWsdoS2kOK7b0Oxakq-8uon8IDza9RBneTCCoQOnAcf1XLHOipyeI0hYbq08G8z9P8801GuwatdxQw1bCOtbYCxMZrHXih9FdV-b9I7Xmdj7Zcvxqh89R3mrlq7XaCOHpvdh-N7DaNVOJRAslgeN0SEJMf68dL08bMjowKjONb0e1yEPNnglDGvwnoiwwPagUEVMEG8x7jbyFX_4VVBnqn92qZUIqszE6wjhWyMprVH_XghpkQ13Z_ZuB5NGSckXm0MbzjJvWy4fXRIhKDUZkTJZC-30xtZFSnjZR5oCbE3n-fVT5sMP5RfhS7mF-VYvccEuDGvn0eUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌‌‌های اکانت فرماندهی مرکزی ایالات متحده، سنتکام
ترجمه ماشین:
🚫
ادعا:
سپاه پاسداران انقلاب اسلامی ایران مدعی شده است که تنگه هرمز بسته شده است.
✅
واقعیت:
کشتی‌های تجاری امشب همچنان در حال عبور و مرور به داخل و خارج از تنگه هرمز هستند.
CENTCOM
🚫
ادعا: منابع رسانه‌ای ایران مدعی‌اند که ایران به یک ناو جنگی آمریکا در تنگه هرمز حمله کرده است. نادرست است.
✅
واقعیت: هیچ ناو جنگی آمریکایی هدف قرار نگرفته است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/VahidOnline/76177" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76176">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYbH3ZdQIVouEf-N1QBNkFQC1LvzZT6mz0gT6XO6GFMqYPf2SACFguQXx31sj_pA-69gWi0bNYWrK9gkSCFV83jrDfV4O_ZxrbXGmyuSn3mMXal71VO-tmknX1z_dWbpgWJHHN_tp3aK84HkiIJvWz-Vx56VGXlZ21SRdcdV66YsT5XBbs6ddNUj8THZ5FkjgE1zou1borTWK3aZwZ-RC8P__2RNhqVNSk1SZ6M7LdxyhWONiphIZeMoZe9Xc3cQ2mwrSicigEAwa5f7b-sBjanS-9U4azmVj6I5xu8eTmkaZAfbqQ1jc6nAsKL395fI9RynY83tVZriG4Svj3AQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: مقامات ایرانی در تماس مستقیم خواستند بمباران متوقف شود
پست خبرنگار فاکس‌نیوز، ترجمه ماشین:
امشب با پرزیدنت ترامپ صحبت کردم؛ در حالی که او از اتاق وضعیت، حملات نظامی آمریکا علیه ایران را زیر نظر داشت.
رئیس‌جمهور به من گفت که امشب مستقیماً با مقام‌های ایرانی صحبت کرده است؛ مقام‌هایی که از او خواسته‌اند بمباران را متوقف کند.
در زمان گفت‌وگوی ما، ایالات متحده ۴۹ موشک تاماهاوک شلیک کرده بود و جنگنده‌ها نیز در حال بمباران بودند. نزدیک‌ترین هدف به تهران حدود ۴۰ مایل بیرون از شهر بود.
ترامپ افزود که بمباران به‌زودی متوقف خواهد شد، اما اگر آن‌ها توافق را امضا نکنند، «تا سر حد نابودی بمبارانشان می‌کنیم.»
پرزیدنت ترامپ این را «نقض‌شده‌ترین آتش‌بس در تاریخ جهان» خواند.
جی‌دی ونس، معاون رئیس‌جمهور، به من گفت که ایالات متحده در روند مذاکرات، هم با صداهای میانه‌رو و هم با صداهای تندروتر در ایران سروکار دارد.
به‌روزرسانی‌های بیشتر در فاکس‌نیوز منتشر خواهد شد.
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/VahidOnline/76176" target="_blank">📅 03:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76174">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3LJe-shX3K73wpxcIkx3J-UyUpaj7QLA0K6MMmAMNdRtGyqb5fFIaDC_NfphNUDUFGmLMIR62Wvtnz70SGQaIY_UUbctwOeVMunQCZF1ttH7j8R5gkNU6nHGrMLhb0AnoiFskWRSbHni2afdvtApwKH7BPWzD5bX9vFTMueeK5M017ZM7As9yu1ymkKVFk8i2XclrZVYZEEkeXMZsE5jdqO46u0dJzZ1gugLkV9mwgLDwpL2sWUfe28QHwyk95XcnFiIYlcdqAE5A1SQ_L1EqmPGHCoW-GjUD2NFKeuWp_G3H-_13rO5OcjZWkrNGRSqok4pMmKEzLTRAellhfuwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دقایقی پس از بیانیه قرارگاه خاتم که در آن تنگه هرمز کاملا بسته اعلام شده و هشدار داده شده بود که به هر شناوری که قصد عبور داشته باشد شلیک می‌شود، تسنیم از مورد اصابت قرار گرفتن دو کشتی در تنگه هرمز خبر داد. در گزارش این رسانه وابسته به سپاه آمده است که کشتی‌های «متخلف» قصد داشتند «به‌طور غیرقانونی» از تنگه هرمز عبور کنند. هنوز مقامات رسمی و سنتکام در این زمینه اظهارنظر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/VahidOnline/76174" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76173">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rgGbpDkrBYcoUg_OnM_Q0dUWK1LpAQpUn8caNlYHxzn8ERyDeIdTb1kuxQrE_9nyrZ1ov-3KfpxmN8AAXq-rlYpjCqTbq1qqcg6SFLrS8LkLtZd7oAIIiDtsP5gaG2mzTNxfZ9EJrMFefZSe9ksC9B-Fx9OT1eAV6xYc2jxA6uq70RDLjNGYCZ621mzD1ttUT3WaWuLBkmDCEYDHYv3KGnY0wnWzJuMD89pb1LRLUMriSrhewCetpCY31be0qLrqRmxUNJeXxlYU2bTblxBa7nCHfA5o2yumJ_NHadQuBnOv6eRK4cWs4DmYboNHGhXxY-FLBDDiPa259tiIjQsMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
روزنامه وال‌استریت ژورنال پنج‌شنبه شب به وقت واشنگتن به نقل از یک مقام ارشد آمریکایی گزارش داد که هیچ سایت زیرساختی در ایران مورد اصابت قرار نگرفته است و نیروهای نظامی ایالات متحده در حال حمله به پدافند هوایی و سایت‌های راداری در نزدیکی تنگه هرمز بودند. انفجارهایی در امتداد تنگه هرمز، از جمله بندرعباس، جزیره قشم و سیریک گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/VahidOnline/76173" target="_blank">📅 02:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76172">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پیام‌های دریافتی:
قشم ۲:۳۵ صدا و لرزشش حس شد
۲:۳۵ دقیقه بندرعباس دوباره صدای انفجار اومد
سلام  بندرعباس دوباره زدن ۲:۳۷
[احتمالا منظورشون اینه که صدا شنیدند!]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/VahidOnline/76172" target="_blank">📅 02:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76171">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VdPjsAG0dvZ21DOAop4D4f29gJZawU4QYFO1x0bdduGD36JEO3XgY4hP0T6WfebBrZgXiVcWAQqadYWQmKA8ngNpEvukbImtbhddtr0fCc_SQyQ3f47Bl1O88Y5S6OsYKaoD7hkYTUAMuL6f555WlZhzOlpKumyWi2j0b1YND4x0RPihzPL_zWwf8yG9NmgvZ61-InkCtYL9Yc361qJpBcD-ueApV-vtSdQu4_W0GN7UyawVnaddJkrJhCHdIVo1D6qhjjTiqHUOQnqVnMefJjgwAgC57x6DSaqfLZslSKWLKKw7bav7i7SenNP26vMWw4kTa2L3kpr9EN5c3kNpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: هرگونه تردد شناورها از تنگه هرمز مورد اصابت قرار خواهد گرفت
منابع حکومتی:
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت
در ادامه شرارت های آمریکای جنایتکار و با توجه به آغاز حملات ارتش متجاوز آن کشور به برخی از مناطق جنوب در استان هرمزگان، از این لحظه به دلیل ناامنی در منطقه، تنگه هرمز برای تردد هر نوع شناور اعم از نفتکش و تجاری بسته اعلام می گردد و هرگونه تردد مورد اصابت قرار خواهد گرفت.
ادعای آمریکا مبنی بر عبور کشتی از تنگه یاد شده تکذیب می شود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/VahidOnline/76171" target="_blank">📅 02:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76170">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2wNg7k5cU22Qo6U3BEqhIVbfwG8lxpKwI6UAZHdMAumf_KpOLlzqHEjL9AwU0Hq6GC_QG8Px9EuG-_7BvCADU1PTQGj6I9ZqMLuVeqeB3MfYLJrYJQ7MI8-cn9y_IbBWYX6b1W0p5zUPj-DN25kkTAbHdfut8S5rxXVaCj0poqJh4BLqvaeDzYXpMDxWswzErm0sBD01jCrct-5A9UoqShQEn5pR0Ts6IKuKGsgMZeqF0Gu4mIcedBj6bkoPuMEonB9ltX2cQ2k-xIBIoXYXuqtZ1ZJgOttMj0-J1fwsg_7cutAfl-SBCUakLVr4lL0vC1zqYCx0sIr0czIwjGQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس بامداد پنجشنبه ۲۱ خردادماه به نقل از یک مقام آمریکایی گزارش داد تمامی اهدافی که در حملات اخیر مورد هدف قرار گرفته‌اند، در جنوب ایران واقع شده‌اند.
این مقام آمریکایی گفت سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها از جمله اهداف این حملات بوده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/76170" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76169">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بعضی کانال‌های خبری به نقل از تسنیم نوشته بودند:
‌
منابع خبری از هدف قرار گرفتن یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه خبر دادند
خبرگزاری تسنیم وابسته به سپاه در پستی نوشت:
انتشار خبر جعلی در کانالهای فیک‌نیوز به نقل از تسنیم
برخی فیک‌نیوزها از دقایقی پیش به صورت هماهنگ خبری با عنوان "هم اکنون یک کارخانه پتروشیمی متعلق به مجتمع گاز پارس جنوبی در عسلویه بمباران شد" به نقل از تسنیم نقل می‌کنند.
این در حالی است که امشب چنین خبری تا این لحظه بر روی هیچکدام از خروجی‌های تسنیم قرار نگرفته است و چنین خبری تاکنون صحت ندارد.
به هرحال اون خبر رو خبرگزاری دانشجو وابسته به بسیج هم منتشر کرده و الان به نقل از اون داره پخش میشه.
🔄
آپدیت:
ایرنا، خبرگزاری رسمی دولت در جمهوری اسلامی:
فرمانداران عسلویه و کنگان که هر دو شهرستان میزبان تاسیسات پارس جنوبی هستند هرگونه حمله و انفجاری را تکذیب کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76169" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76168">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پیام‌های دریافتی:
صدای سه انفجار در بندرعباس
بندر عباس سه صدای پشت سر هم ساعت 1:20
وااااایییی تو دو ثانیه سه تا انفجار شنیدم بندرعباس خیلی نزدیک بود
بندر عباس همین الان چند تا صداااا
بندرعباس سمت زندان شهرک صدای جنگنده یا انفجار طولانی اومد
همین الان یک انفجار خیلی خیلیییی سنگین بندرعباس
دوباره انفجار بندرعباس ۱:۲۲
وحید بندرعباس الان یجوری زد شهر لرزید
وحید ساعت ۱:۲۰ بندرعباس سه تا انفجار خیلی سنگین شد
دوبارهههه صدا اومد ولی خیلی دوررر بود فکر کنم سه/چهار تا بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76168" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76167">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxdRP1XKl_6TT52SV0491mH-VATkhFalvveQGkUpV-33OSphuZLBgp4zGumUTHbVrbiQZidkxIz-TtzjoWD69JRTlSspKsW_0dRglXtvssT1QL4IbMvxB-bi8jQ6wTMwPpN-pzSfEQvKVjvbGOkjaNiPx6q7zr4eYGJA7JMkpDaAyp5lr_K0VkRFAlJw5iFTVWvoHXrDUz78EAFa8QsjxQw8vabAI4cGFSWypEJ6IHGbEoVgCcDTynk-U-_uBsrB_J_J9zdfDVg85Z0cceUxIPzVGXGUdrKWhsvQKdr9S9NIrBexzi_7M2Wk4ns0vUatpeZ1ALHUFsYBMCHrf9wD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سنتکام، ترجمه ماشین:
نیروهای فرماندهی مرکزی آمریکا امروز، به دستور فرمانده کل قوا، از ساعت ۵:۱۵ عصر به وقت شرق آمریکا، حملات دفاعیِ بیشتری را علیه چندین هدف در ایران آغاز کردند.
این حملات در پاسخ به تجاوزهای بی‌دلیل و ادامه‌دار ایران انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76167" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76166">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۱:۰۳ بندرعباس صدای انفجار شدید اومد
بندرکرگان شهرستان میناب، رو با موشک زد
همین الان
پاسگاه دریابانی رو زد
صدای دو انفجار در بندرعباس همین الان
سلام ساعت همین الان انفجار شدید در بندرعباس ساعت ۱:۴ دقیقه
وحید از ساعت ۱:۰۳ دقیقه بامداد
چهار تا انفجار بندرعباس
سلام وحید،صدای چند انفجار همین الان بندرعباس
سلام. همین الان صدای انفجار شدید، بندرعباس، ساعت یک و سه دقیقه شب
صدای انفجارهای ممتد میاد
صدای انفجار بندرعباس
بندر عباس فکر کنم سه تا انفجار با فاصله چند ثانیه
صدای انفجار بازم میاد میناب نوار ساحلی
انفجار دوباره
سلام،وحید جان بندرو زدننن من لرزیدمم
همین الان صدای انفجار بندرعباس دو الی سه تا صدا اومد
انفجارها داره زیاد و قوی‌تر میشه، بندرعباس ساعت یک و شش دقیقه شب
سلام‌وحید جان بندرعباس همین الان ۱:۰۵ دقیقه صدای انفجار اومد
سلام وحید جان
همین الان ۱:۰۶صدای انفجار داره میاد بندرعباس
پنجره خونمون لرزید
درود درگهان همی پنچره ها لرزید
سلام اقا وحید ۰۱:۰۶ دقیقه بندرعباس الان یه صدای بزرگ انفجار که مرکز شهر شنیده شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76166" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76165">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، بدون هیچ توضیح بیشتری نوشته:
شنیده شدن صدای انفجار در سیریک
🔻
خبرگزاری تسنیم، وابسته به سپاه، نوشته:
بررسی‌ها نشان می‌دهد که
تا این لحظه
اخبار مربوط به صدای انفجار در جزایر کیش و قشم صحت نداشته و صداهای شنیده شده مرتبط با درگیری در خلیج‌فارس است.
براساس گزارش منابع محلی، دقایقی پیش صدای انفجار در اطراف میناب و سیریک شنیده شد.
🔻
پیام‌هایی در ابراز تعجب از پرواز هواپیمای مسافربری در تهران دریافت کردم.
🔻
تسنیم در پست دیگری نوشت:
تاکنون صدای ۴ انفجار در سیریک شنیده شده است
🔻
عکس‌هایی از فرود  هواپیماهای مسافربری در تهران دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76165" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76164">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0af3a46aeb.mp4?token=tXA9ed-3qT_kR-TjGUKng4d5eQgRT7yNikebyGqz3nNRuTmBEc_sgm_5Na-byKwBYqI8fxdBrAUDkJiNo3PPmwllAD1rLtGmB42Cy9aBrur4JYjVLkl5ldj-LwVIbxGQGKv4b3T47QqYZYeCB4I2BV4GclXtaKrbMBNkhcuJlkIkVWYyi62XEjT90KONugfEIQUI-52MBO94DEHVhNNmYB9pM-CAzCVD8AiVj36bGQKl59UNM0_fjqutCegJNhB2HQqiX2vleULZ4tv6JQkhgf4lIYcJE-U0YFMqGT01WzgInBNN2W4EhB2uS--q7weOxQkZT74t9Ev2ZXar1tPbH4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0af3a46aeb.mp4?token=tXA9ed-3qT_kR-TjGUKng4d5eQgRT7yNikebyGqz3nNRuTmBEc_sgm_5Na-byKwBYqI8fxdBrAUDkJiNo3PPmwllAD1rLtGmB42Cy9aBrur4JYjVLkl5ldj-LwVIbxGQGKv4b3T47QqYZYeCB4I2BV4GclXtaKrbMBNkhcuJlkIkVWYyi62XEjT90KONugfEIQUI-52MBO94DEHVhNNmYB9pM-CAzCVD8AiVj36bGQKl59UNM0_fjqutCegJNhB2HQqiX2vleULZ4tv6JQkhgf4lIYcJE-U0YFMqGT01WzgInBNN2W4EhB2uS--q7weOxQkZT74t9Ev2ZXar1tPbH4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، در جمع خبرنگاران گفت حملاتی که امشب به ایران انجام خواهد شد، «قوی و روشن» خواهد بود و فرماندهی مرکزی آمریکا امشب درگیر عملیات خواهد بود.
او افزود آمریکا تاسیسات کلیدی در جمهوری اسلامی را بمباران می‌کند و امشب «ضربه سختی» وارد خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76164" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76163">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bCU0hh8b-izH0zOb9KUZvaSYDTyKsT3_U7yAPTu5THnX-HJulWE-JGhhANsgCmMhI28r95AyX5KNorGeBaRXQEhgYaLmjsFk6g87zhsDi3svpAaoDSqJfvf-K9l76Zwce0Ebr2vMVwQpt6GPbjMWMmpKlkL-Nv8KdrMAysPKaycL0AcR6tOsVKXL83Z5exFy6NhBAGjwE2zHoMngaCZvpJcNlJxZZ6qd4QcCikObAcgoOzGU5VR7MXNdYpsFQjDr-uwTweTntz13Cq886bCez7iUJi5TseIBa_lDpqsnOpuWWrVyxb6XqTe_Ccoyc-lq3CGXxEfp87ZfghkV0a3tuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: ترامپ درباره گزینه‌های حمله به ایران در اتاق وضعیت جلسه برگزار کرد
ترجمه ماشین:
پرزیدنت ترامپ بعدازظهر چهارشنبه جلسه‌ای در اتاق وضعیت کاخ سفید برگزار کرد تا درباره حملات احتمالی تازه علیه ایران گفت‌وگو کند؛ این جلسه چند ساعت پس از آن برگزار شد که او به خبرنگاران گفته بود آمریکا «امروز دوباره ضربه سختی به آن‌ها خواهد زد». این را دو منبع آمریکایی اعلام کردند.
این منابع گفتند یکی از گزینه‌هایی که ترامپ در حال بررسی آن است، انجام عملیاتی است که از نظر مقیاس بزرگ اما از نظر مدت‌زمان کوتاه باشد؛ با هدف فشار آوردن به ایران برای تغییر موضعش در مذاکرات.
این منابع جزئیات بیشتری ارائه نکردند.
پیت هگست نیز در فلوریدا خطاب به سربازان گفت: «اگر قرار نیست توافق کنند، ما ضربه سختی به آن‌ها خواهیم زد»؛ سخنی که بازتاب‌دهنده اظهاراتی بود که ترامپ پیش‌تر در روز چهارشنبه بیان کرده بود.
axios
کلی میر،‌خبرنگار نیوزنیشن گزارش داد پس از آنکه پرزیدنت ترامپ گفت ایالات متحده به حمله به جمهوری اسلامی ادامه خواهد داد، پیت هگست، وزیر جنگ آمریکا اعلام کرد سنتکام امشب مشغول خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76163" target="_blank">📅 23:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76162">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loZ_NKgccrLS1NN16JsA_jCZacffclVqVbHdbnyr_QpSTCJExfdeWlUTXXG7BeMpChw-3fmwdzo5PeGTiEUwjp-BoxsW4VKxcaodEtsyTUspumIJdGYR_bLDZpiEDJbO_pcpY2rV8TaPXR8wXbxlnrs9HpC5YuBxksJR8RSgkN-IfRBoeRyR7IpyehpyZZdpB5B-BXnTZws4G4xAkPEpbfV48R0jHc1OekHPasotAKqHhxLtHbx2lIvyZkHSUMjcTNtIctZDFKm4tqnPl0KotCO9eDjkdMJuELhunjMM50uwbIlThPs0d7qaPKlrW_jsDHHYfUy124siqSAHTrDolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز ۲۰ خرداد ۱۴۰۵، گزارش داد جمهوری اسلامی با پیشنهاد میانجی‌های قطری برای برگزاری یک نشست سه‌جانبه با حضور نمایندگان ایران، آمریکا و قطر به منظور حل اختلافات باقی‌مانده در مذاکرات موافقت نکرده است.
بر اساس این گزارش، مقام‌های ایرانی و آمریکایی طی دو روز گذشته به صورت جداگانه با میانجی‌های قطری در دوحه در تماس بوده‌اند. با این حال، تلاش قطر برای برگزاری یک نشست مستقیم میان طرف‌ها با مخالفت تهران روبه‌رو شده است.
اکسیوس به نقل از منابع آمریکایی و منطقه‌ای نوشت که همزمان با ادامه تلاش‌های دیپلماتیک، هیئت قطری روز چهارشنبه برای گفت‌وگو با عباس عراقچی و دیگر مقام‌های جمهوری اسلامی به تهران سفر کرده تا روند مذاکرات را از بن‌بست خارج کند.
این گزارش می‌افزاید که دستور دونالد ترامپ برای حمله به اهداف نظامی ایران تنها به دلیل سرنگونی یک بالگرد آمریکایی صادر نشد، بلکه نتیجه افزایش نارضایتی او از تاخیر جمهوری اسلامی در پاسخ به آخرین پیشنهاد واشنگتن بود.
به گفته یک مقام ارشد آمریکایی، هدف از حملات محدود آمریکا در شامگاه سه‌شنبه «بازگرداندن اهرم فشار» در مذاکرات بود، بدون آنکه تلفات انسانی بر جای بگذارد یا مسیر دستیابی به توافق را مسدود کند.
دو مقام ارشد کاخ سفید نیز به اکسیوس گفته‌اند که حتی اگر سرنگونی بالگرد آمریکایی عمدی نبوده، واشنگتن برای جلوگیری از تضعیف موقعیت خود در مذاکرات ناچار به واکنش بود.
به گفته این منابع، حملات آمریکا به گونه‌ای طراحی شد که تنها سامانه‌های راداری و مراکز کنترل پهپاد ایران را هدف قرار دهد.
اکسیوس همچنین گزارش داد که کاخ سفید ساعاتی پیش از آغاز حملات، بار دیگر از تهران خواسته بود پاسخ نهایی خود را درباره پیشنهاد اخیر ترامپ ارائه کند، اما مقام‌های جمهوری اسلامی اعلام کردند هنوز تصمیم نهایی اتخاذ نشده است.
بر اساس این گزارش، ترامپ پس از نشست ۸ خرداد در اتاق وضعیت کاخ سفید، دو شرط جدید را به پیش‌نویس تفاهم میان دو کشور اضافه کرده بود.
نخست اینکه ایران ظرف ۶۰ روز ذخایر اورانیوم غنی‌شده خود را رقیق‌سازی کند و دوم اینکه از دریافت هرگونه عوارض یا هزینه از کشتی‌های عبوری در تنگه هرمز خودداری کند.
در مقابل، واشینگتن آمادگی خود را برای پذیرش انجام فرآیند رقیق‌سازی در داخل ایران و تحت نظارت آژانس بین‌المللی انرژی اتمی اعلام کرده بود.
اکسیوس به نقل از منابع آگاه نوشت عباس عراقچی به میانجی‌ها گفته بود برای ارائه پاسخ تهران به چند روز زمان نیاز دارد، اما این روند به نزدیک دو هفته انتظار تبدیل شد و موجب افزایش نارضایتی ترامپ شد.
این گزارش همچنین می‌گوید پیش از تشدید درگیری‌های اخیر میان ایران و اسراییل، دو طرف به دستیابی به توافق نزدیک شده بودند، اما تحولات نظامی روزهای گذشته روند مذاکرات را پیچیده‌تر کرده است.
با وجود حملات متقابل و افزایش تنش‌ها، مقام‌های آمریکایی به اکسیوس گفته‌اند که مذاکرات همچنان متوقف نشده و واشینگتن امیدوار است فشارهای اخیر، جمهوری اسلامی را به ارائه پاسخ نهایی درباره پیشنهاد آمریکا وادار کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76162" target="_blank">📅 23:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76161">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iBShcOok_FK_AB8TPwbqN6nBi8DHAFHK1e-F5UJT6P6aO858WfW8OivKcnvAbk7ajXeX_xpWl15U60DIxPObD0aETBqg57TdZhq9ZaTbS-Ib26-VCY2weoFpOev0zH8rh_oOnMCOUJXrONrj-mQUpAcGqmYmzf_o0B6pjYBRFWT5wfagiHY6vEAeJGxOi7GiIuUg_uKNf1GdUxvIwQa9Ruv1eBQeOumhN1u5tAGFcpUtpuimEoQploBMt5wREIM-CZRawCDVSadto__TV5cxhayqkUoJuDRYvGEuRF2A8oTVIPgsTQmb1HAbJxK58tQ9MnsuBAx2vLkaCSXotGGdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی مجلس، در شبکه ایکس نوشت: «در جنگ ۴۰ روزه وسعت آب‌های سرزمینی ایران افزایش یافت، در جنگ بعدی شاید وسعت خاک ایران افزایش یابد.»
او در مطلبی دیگر تاکید کرد جمهوری اسلامی آماده‌تر از قبل است.
او همچنین در یک برنامه تلویزیونی گفت: «دست از لبنان برنمی‌داریم و دشمن یا باید به خواسته‌های ما در میز مذاکره تن بدهد یا در میدان نبرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76161" target="_blank">📅 22:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76159">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/274405ecae.mp4?token=vy8kSBdpbwxxjmmj60ojiQO6S8M8GIgGx9-QhRigQdwOPZfF8nZ623t3FifzUI5nCbUq5C6M-PalBPs50Clr_U-eSzsKoQ31hPNWeYdS1SYpkLLYuQpDxCYck356Gs-jM0ARw-I7aamafwtudI-_8uIK4mqbq6US4pAGx-r1ijMMojVLSJcRCJ4p2AK7cFAP8lRpXRB-obcHlMEAl6os1yXfKK7VA42voINBu67jYUF30ifkBTuQmfVkZSAu5GFFLEoNWj1i_KOQZQl4nUD9Mvb5Bsak3Wu5NkWL2p9Fqwzp0J2tZEaEzjjOxv0w86sA4qWKmbATHLi0h6Fp3QbAhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/274405ecae.mp4?token=vy8kSBdpbwxxjmmj60ojiQO6S8M8GIgGx9-QhRigQdwOPZfF8nZ623t3FifzUI5nCbUq5C6M-PalBPs50Clr_U-eSzsKoQ31hPNWeYdS1SYpkLLYuQpDxCYck356Gs-jM0ARw-I7aamafwtudI-_8uIK4mqbq6US4pAGx-r1ijMMojVLSJcRCJ4p2AK7cFAP8lRpXRB-obcHlMEAl6os1yXfKK7VA42voINBu67jYUF30ifkBTuQmfVkZSAu5GFFLEoNWj1i_KOQZQl4nUD9Mvb5Bsak3Wu5NkWL2p9Fqwzp0J2tZEaEzjjOxv0w86sA4qWKmbATHLi0h6Fp3QbAhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'آتش‌سوزی حوالی میدان قیام تهران'
چهارشنبه ۲۰ خرداد
Vahid
و گزارش صدا و سیما که میگه بیشتر انبار فرش هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76159" target="_blank">📅 21:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76158">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uYlEx93uo9g7lAqIABCuXaTEnLVq3opkUbFPX47RUneRL1OGaFXomGU5RLy6uM7h4HzPYfiJNxYDutcdjJx1GUfSYmtu1gKUD1P4-OiLgWrCKUG1P12cqal1iJ7rqInCuE8wbhELbQFVK6i5lMHaT1c-6GChd_ZAuBjK5dNYpCEK6YxbDQdBVkUG-73NP1Is44C76HRgToj31lgbbGfWuFrkTdzAjpXdeuXYQ3DD3w3YZQjuMhclOm6uAQAx0h8iE-Fvj1vTEJyFEHxCuC504RQQenAHb-oPNe2SLX88w6dcVXsMXZLSxlNK_rXEOtk9P2KBrN_r8JXqAuX4Vn2EJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بیش از ۱۰۰ میلیون بشکه نفت در جریان ماموریتی محرمانه از تنگه هرمز عبور کرده است
ترجمه ماشین:
ماه گذشته، من به ارتش بزرگ ایالات متحده دستور دادم مأموریتی محرمانه برای حمایت از نفتکش‌ها و دیگر کشتی‌های تجاری در عبور از تنگه هرمز اجرا کند. امروز خوشحالم اعلام کنم که این تلاش باعث شده بیش از ۱۰۰ میلیون بشکه نفت از تنگه عبور کند و وارد بازار آزاد شود. بیش از ۲۰۰ کشتی تجاری نیز با ایمنی از تنگه عبور کرده‌اند.
این تلاش به‌شدت موفقیت‌آمیز به این دلیل است که ایالات متحده آمریکا تنگه هرمز را کنترل می‌کند — نه ایران. ارتش آن‌ها شکست خورده و اقتصادشان از دست رفته است. کار ایران تمام است!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76158" target="_blank">📅 21:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76156">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OYvz63hRsMhfQyejxKm9A-vfBD8eYibERC_snObcKg_cGspdjB4MP5HZXogug-hHS0Vs1VDG1pDCLD8JzOuCOXZpjKxY4jLtQ1WCt2vDIFQU79dyzwOL1wA0804mEH9baan-PsWMJZEt5oGQ6FrTiFptCv-9ieNi82BhJtLrgtYbiGxpok71mao8NkjEJuM3DcgukvVUTYVMJWOuuP8eEnxO4PPQXDTGr45XDxiJXOnHRXjgvcG5dYj2fiV0O7Fnxf0qObd1xyXMs0QWceaSYFyCx9EFwDBbMud66VuYvi-tu8pwmtDAKIHUcT4cda-sv-ZhmHREhKU4-SJYk18a9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1379a1972.mp4?token=m6Y7N6RnfRCwoexNc9B0m_RXeUko4zw8bcDOddKnwHEbhiihdb4Y95kccrGyngrq6qMx3GGuDSV2kB7GLDYVdKPkOW_bh0JH4P_bOaySeNJUrepJnQ5iDjgF2tqSCoJoKFrtnRmJcQK56IPM7mFRqxdsZFh85QJ6vmSvpHubaQ_z_Dv_1EoDk684c3IVneFfZHQEyREwgdp0m2fU-g9-0AH3WLqITIPNo65KMPWZncIfRtgyKYh7TAWfpmkQ31MRV3Us7xG6jv_GnXP0dqpFycPIBfF-UZqAVSRjLp05L81DS7qOxGG1O29TK9kkVaHW6kBaxoluGVFh0UXRhA1XyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1379a1972.mp4?token=m6Y7N6RnfRCwoexNc9B0m_RXeUko4zw8bcDOddKnwHEbhiihdb4Y95kccrGyngrq6qMx3GGuDSV2kB7GLDYVdKPkOW_bh0JH4P_bOaySeNJUrepJnQ5iDjgF2tqSCoJoKFrtnRmJcQK56IPM7mFRqxdsZFh85QJ6vmSvpHubaQ_z_Dv_1EoDk684c3IVneFfZHQEyREwgdp0m2fU-g9-0AH3WLqITIPNo65KMPWZncIfRtgyKYh7TAWfpmkQ31MRV3Us7xG6jv_GnXP0dqpFycPIBfF-UZqAVSRjLp05L81DS7qOxGG1O29TK9kkVaHW6kBaxoluGVFh0UXRhA1XyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از نزدیک‌تر: 'آتش‌سوزی حوالی میدان قیام تهران'
چهارشنبه ۲۰ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76156" target="_blank">📅 20:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a-jFXr2u1aL7GHod3oVt7jUVnKEbe4OIswVGAdik1rVvtiCC7-Z9nxM_6YwKlXW0tOxRND1EST7WuYfJ50szrHEwdcA6INJwk-vExpPx_ywcXAVhQJ_dzxsWmZNqtAXc4ogL-raApN90vUsY2EJJsZnlt32G2PBf25YSRejqz4scKoAWMCcRt90jAVcP2ZxXXq-mOlVs-LPMiFvJNzlII9LeQHd0iaI0MNJ4neO-Ni0kidBXFvzwPnIxaRvNKkJAHvt6PB3_kdgbLZwX_SaJm5mphRJM3cSgfBCYHX3ybJQXttoc5l7tanJ2WYHKoxujHPe39GH8wSPSQHgu6V3d4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kTGJBNZiVz2LSs3Vbyl1l_D5mTD3EOlQUSunnAdOlDUt40LWXrbVfCmMMFOm8HMcgde-NcsjGD64HXjCLVhyZFyvd_YMgRvVTDePHK87mt-u2fOzW10rAwuibfRZf6u4avs1Ue-yzM1ErwWgaYJHAhcskOWU63-vjsOzVptKuBUtjzdf8aA-oi6xgeSAAFt2tgYSTPM-UPyBRszaSWQfeiQKZJjOdGLS6uVVkrbWluQb7Gpb0vw4IPOjNDXFQ0GbMYZSFbS8WaJXHPyOGItYMAQ8hZGTKT7gstRtrK7iAT9XLB7R9yCaHwrK3ETDeO1AsX09eoTGzi1tQxpikshxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ANI_4GyONcVLg5RpHdLLLMJ1n2HtqmHc5QxHBJnBeXDzXM1ec5bSei5sbUHk2CUXIxxLhvQpgJrMVCeooWpdAH4SHYJbzeH7UfJunQj-c3mF5uRAy6YyKpOROaEQ_9hUFhp7lS9ehRlyx4crwjqOSkvVnqWFfhyKCzjKdl0_VheAgvfPtvCfHzLLOBJ0SrO0Hw76QD-qNQ7pNtrMTFniaS-wP710gntGNOqQmUEkJpUxZUXnM5i8U6UfmD4s_9JhXJb23ZpHZv_F_LfgAk3UnUoc0ekLkTUfm_FmLehtEctWw0LnvJNgxvBUBk2ILr3bnEme6DjZTb9qCJ_m08TPJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pS_nKwFTnSHaatRhnqm6fWSGCPv18KMsWcGAtSWRHshdRfDwY6kwNzcev0sqgskQioG-SUboKgG_G-JTMeHYmJrZVaNqTQlwSLwEpJwZMMwXkRLzkHuyj4Q0fy3BXNGZ5uC7CgntdAV75WfIhOYWOqXoEUd-2HjsvbQz2pw_8slg6_PGCn2Fdp7Nxqtd4wFv1UOC1-aXhPN6Ltf8KB_cmjjZ_De6qo-bkvu8CNfD_7Bz8azt_bIHe2BUDbKbeCB6AQu4i_B_Ui6MIVfnP2jdBv42UcFCYikH_L-_axdA-sknXy1kxtZoI62BgogNZQvYcGPon5djJEHskb8CeJPkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PnR_stdYpuzMqbPOZwPkL9Bfo6xhqRWt9gdJQbSvgv4UX9CmuV50HMRX2UFjzo5euwrHrTSKF9M22owQg7QU3phHH-nWcukPUtNndwPu9CjWotLglj0VtiAVCDPRYygI0RbYE1C8EePvM8vllec5M0N_EHTulmHSw2CAyGSLRI05Y-xJmqAZF4fOW-MnfxDDQsQhUzJKCF_3QFfu8vC0nEYnO1rpwb_gT3mhPW5j6z5aTE6XkxRKgV4GVg1ac5XVVhA2e4YvhurvrEnhJr5icGNh9hovMuo-qTONgRtY2fAaO6SuQQsRPznijjBuRU-gy-DiqGYu9doTdNiPn_aaXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی از ستون دود سیاه و غلیظ حوالی مرکز
#تهران
منابع حکومتی نوشته‌اند: "یک انبار کالا حوالی میدان قیام در منطقه ۱۲ تهران دچار
#آتش‌سوزی
شده است."
چهارشنبه ۲۰ خرداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76151" target="_blank">📅 20:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/02bad1a497.mp4?token=NiYGQ7imOjICjDFe0b4Fh3YvShD1T9sMy--IcyqNhiM-KqphbO4GprnIVoqxT3Boenqy9AEzQJzNbd7gG0MBEwWWpuL2pVr3gRG5l-k6_U7s2VbJF0nALWy52lTtSJST4sybLSdvlhxu1K1PYe5GjyNSRcHAk3m50LwMr4C3lRTDdhTULzDbk9sQUkggK1eXXAZepcFCJ23ou-mcu-va-10CgHpFz8k3KklLSxXqkzC-Tf3NNsS6HXqaGV3zmBgESTvIwPSl5EtciKsRYaYxXyKxeiu2JOAEoKeDNmkL5PuFqliBv8S4JTZnZR_WmLr4oZ-6M0aOKixBPpwrvcK5KA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/02bad1a497.mp4?token=NiYGQ7imOjICjDFe0b4Fh3YvShD1T9sMy--IcyqNhiM-KqphbO4GprnIVoqxT3Boenqy9AEzQJzNbd7gG0MBEwWWpuL2pVr3gRG5l-k6_U7s2VbJF0nALWy52lTtSJST4sybLSdvlhxu1K1PYe5GjyNSRcHAk3m50LwMr4C3lRTDdhTULzDbk9sQUkggK1eXXAZepcFCJ23ou-mcu-va-10CgHpFz8k3KklLSxXqkzC-Tf3NNsS6HXqaGV3zmBgESTvIwPSl5EtciKsRYaYxXyKxeiu2JOAEoKeDNmkL5PuFqliBv8S4JTZnZR_WmLr4oZ-6M0aOKixBPpwrvcK5KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، طی سخنانی در کاخ سفید درباره جمهوری اسلامی، گفت: «ما آنها را بسیار سخت هدف قرار خواهیم داد. باید توافق را امضا کنند. ما توافقی می‌خواهیم که معنادار باشد و کار کند.»
او ادامه داد: «امروز دوباره ضربه محکمی به آنها خواهیم زد.»
ترامپ افزود: «نخواهم گفت آیا پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد یا نه.»
ترامپ با اشاره به هدف قرار گرفتن یک بالگرد آمریکایی گفت جمهوری اسلامی ابتدا مسئولیت این اقدام را رد کرد، اما بعدا آن را پذیرفت. او افزود بمبی که به بالگرد اصابت کرد منفجر نشد و دو خلبان آن در جریان یک عملیات نجات زنده ماندند.
ترامپ بار دیگر گفت: «دیروز ضربه سختی به آن‌ها زدیم و امروز هم دوباره ضربه سختی خواهیم زد.»
او در پاسخ به سوالی درباره احتمال هدف قرار دادن پل‌ها و نیروگاه‌ها در ایران گفت جزییات عملیات احتمالی را اعلام نخواهد کرد، اما آمریکا توان انجام چنین اقداماتی را دارد و «قوی‌ترین ارتش جهان» را در اختیار دارد.
دونالد ترامپ، رییس‌جمهوری آمریکا، در در کاخ سفید، گفت جمهوری اسلامی «به هیچ‌وجه» نباید سلاح هسته‌ای داشته باشد و نخواهد داشت و افزود مقام‌های جمهوری اسلامی نیز با این موضوع موافقت کرده‌اند. او گفت تنها کاری که جمهوری اسلامی باید انجام دهد امضای توافق است.
رییس‌جمهوری آمریکا افزود توافق «کاملا مذاکره و نهایی شده» است، اما جمهوری اسلامی همچنان در حال وقت‌کشی است.
او گفت: «چند روز دیگر هم به آن‌ها فرصت می‌دهیم، چون این یک سند مهم و معنادار است و آن‌ها می‌دانند وقتی آن را امضا کنند، تعهدی جدی ایجاد می‌شود.»
ترامپ بار دیگر برجام را هدف انتقاد قرار داد و گفت: «توافق اوباما، برجام، یکی از بدترین و احمقانه‌ترین اسنادی بود که تا به حال دیده‌ام.»
ترامپ همچنین گفت جمهوری اسلامی از برخی اقدامات اخیر آمریکا اطلاعی نداشته و افزود آمریکا چند شب پیش ۲۲ کشتی را در تاریکی و بدون چراغ جابه‌جا کرده است. او گفت جمهوری اسلامی «دیگر رادار ندارد» زیرا آمریکا سامانه‌های آن را نابود کرده است.
او در ادامه گفت زمانی که تصمیم به حمله گرفت، به اطرافیانش گفته بود اقتصاد آمریکا در بهترین وضعیت قرار دارد، بازار سهام و حساب‌های بازنشستگی به رکوردهای تاریخی رسیده‌اند، اما جمهوری اسلامی به‌زودی به سلاح هسته‌ای دست خواهد یافت و به همین دلیل باید اقدام نظامی انجام شود.
ترامپ افزود آمریکا با بمب‌افکن‌های بی-۲ به جمهوری اسلامی حمله کرده است. او این عملیات را «بسیار شجاعانه» و «کاملا موفقیت‌آمیز» توصیف کرد و گفت پس از آن «مرحله دوم» نیز باید انجام می‌شد.
رییس‌جمهوری آمریکا گفت برخی پیش‌بینی می‌کردند بازار سهام پس از این حملات تا ۲۵ درصد سقوط کند، اما جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای «ارزشش را داشت». او همچنین گفت نگران بود قیمت نفت تا ۲۵۰ دلار در هر بشکه افزایش یابد، اما اکنون حدود ۸۵ دلار است.
ترامپ در ادامه گفت نیروی دریایی جمهوری اسلامی «از بین رفته» و ۱۵۹ شناور آن در کف دریا قرار دارند. او افزود جمهوری اسلامی دیگر نیروی هوایی ندارد، هواپیماهایش نابود شده‌اند، بخش عمده پهپادها، توان تولید پهپاد و موشک‌هایش از بین رفته‌اند و رهبری جمهوری اسلامی نیز جایگزین شده است.
او در پایان گفت فکر می‌کند جمهوری اسلامی خواهان توافق خواهد بود، اما افزود:
«خواهیم دید چه اتفاقی می‌افتد.»
ترامپ همچنین گفت با پایان جنگ، تورم کاهش پیدا خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76150" target="_blank">📅 19:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qkovHG4fHLqXbPsPPMOIjdqa8AN6flXE7ccxNLb6A-yPiJLKwklVqjcleGUnFUP57XlDfOY8pnDJX7SzviixM_virJyKiewanlnEybhkMxja9dQPjoxEFtaPu4vl5OXnQJHzX8HQ6KRlXmia7gaSFC3w1toh9PG83k9mYmcvW-FquxGSoKnk8Gb_IBCPXibobezk27BEaCErrtGzZ5hTmtdNFDmCT8YndXZpxKWyXClRG9HMKw3vSEKh2qk8JQdYwV7HqdM8QUELDzwE_SBf2n80SzSzlQ1bJR6-Vy15EcqmNqJSPYUvNxL6ehVge6yuq30_3YbzZogvJnc8g490jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا روز چهارشنبه ۲۰ خرداد، در پاسخ به درخواست خبرنگاران برای شفاف‌سازی درباره اظهارات قبلی‌اش مبنی بر اینکه جمهوری اسلامی ایران باید بهای طولانی کردن روند توافق را «بپردازد»، موضع تندی اتخاذ کرد.
دونالد ترامپ در دفتر بیضی کاخ سفید به خبرنگاران گفت: «خب، ما به آن‌ها حمله خواهیم کرد، و بسیار هم سخت حمله خواهیم کرد.»
در ادامه از او سوال شد که آیا این به معنای از سرگیری کارزار بمباران [مواضع ایران] توسط ایالات متحده است؟ ترامپ پاسخ داد: «بله، خب، با توجه به موضوع بالگرد، فکر می‌کنم این حق را داریم که چنین کاری انجام دهیم.»
ترامپ ایران را متهم کرده است که یک بالگرد آپاچی ارتش آمریکا را بر فراز تنگه هرمز سرنگون کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76149" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76148">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/460f7345bd.mp4?token=Cx1xmdJjYLe_KqVzTl_OIsaduJ8qZiXhtdi-gOR4OhDDYGG31WAmF01ozi5KyUxwmEACFv7oD5kNAcCXo1x2GfPGMR0neQ0Xlz4gF8UncOM1kxXE1ECdVU3aJjNLjufJwjrHZY2DRwnKW5GsZ7WrUXy9nKrHpAxuEY1b09DwX0TlDegUXeKDjeda_FDSCWAi-VL2G-b_0CVu4obkLVhxa7ax4wvXa6P5yQj-Pv17PsyZm2KI58TBhJe6TCjN3wXXuXg5ThWtGBaYvln8oovrWQ-u0-Y3-VPgiWQb35xoVkr5yJOeDA88zc8FgIg4qYRPAKLf8L3uvllHQOTRw9jpvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/460f7345bd.mp4?token=Cx1xmdJjYLe_KqVzTl_OIsaduJ8qZiXhtdi-gOR4OhDDYGG31WAmF01ozi5KyUxwmEACFv7oD5kNAcCXo1x2GfPGMR0neQ0Xlz4gF8UncOM1kxXE1ECdVU3aJjNLjufJwjrHZY2DRwnKW5GsZ7WrUXy9nKrHpAxuEY1b09DwX0TlDegUXeKDjeda_FDSCWAi-VL2G-b_0CVu4obkLVhxa7ax4wvXa6P5yQj-Pv17PsyZm2KI58TBhJe6TCjN3wXXuXg5ThWtGBaYvln8oovrWQ-u0-Y3-VPgiWQb35xoVkr5yJOeDA88zc8FgIg4qYRPAKLf8L3uvllHQOTRw9jpvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت آب و فاضلاب استان هرمزگان گفته است در پی حملات بامداد امروز آمریکا «زیرساخت‌های حیاتی توزیع آب در شهرستان سیریک» تخریب شده است.
عبدالحمید حمزه پور گفته در این حملات «دو مخزن استراتژیک آب در بخش بمانی هدف قرار گرفته و به طور کامل تخریب شدند ... که نقش کلیدی در تأمین آب شرب بخش بمانی و شهر کوهستک ایفا می‌کردند.»
@
VahidHeadline
خبرگزاری فارس:
آبفای هرمزگان: شبکهٔ آبرسانی مناطق آسیب‌دیده در مدت کمتر از ۱۲ ساعت مجدداً وارد مدار بهره‌برداری شده و مشکل قطعی آب در شهر کوهستک و روستاهای بخش بمانی به‌طور کامل برطرف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76148" target="_blank">📅 19:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76147">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrGIoH_NE4Sw2yNIUTcP5HrZkUXrrWY9YslvLYjT3c7BIoRnjyM6rC_Fn1m7Yo_oFf5F0OmkMpV-yZG3k0bQMve40nrQGdfRAQEi31vjIh2A0CBB2HbztG8Pg4anObr-OBsRf8sIea5akK8Jodhcaye1Yn1L2rE4JUD0apTH-mUjNyFsD8Qe-jDrSUCw_jJNhxc8r6K5cw-rbSjp0stgMCNOyhFef_xDDCEC_hleikqKgpYLICQ_xjnCX-JGn5DoOJ6iFG4zzsrSM4ztAgIJyawmJ_qI-puFyu90wZHe2ApDBYbu8GnMKilDker60lXFA0Q8pQE0m3vQu6QZ9EWFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده، بریتانیا و ۲۰ کشور دیگر در بیانیه‌ای مشترک تاکید کردند که نهادهای امنیتی جمهوری اسلامی ایران باید به توطئه‌های خود برای ترور، ربودن و آزار و اذیت افراد در اروپا، آمریکای شمالی و استرالیا پایان دهند.
وزارت امور خارجه بریتانیا روز چهارشنبه ۲۰ خرداد اعلام کرد که سازمان اطلاعات سپاه پاسداران، نیروی قدس و وزارت اطلاعات ایران، مخالفان سیاسی، روزنامه‌نگاران و همچنین جوامع و منافع یهودی و اسرائیلی را هدف قرار داده‌اند. این کشورها همچنین حملات منتسب به گروهی موسوم به «حرکت اصحاب الیمین الاسلامیه» را محکوم کردند.
در این بیانیه آمده است: «ما در عزم خود برای محافظت از کشورها و شهروندانمان در برابر این تهدیدات متحد هستیم. جمهوری اسلامی ایران باید فورا این اقدامات را متوقف کند.»
این بیانیه به امضای کشورهای آلبانی، استرالیا، بلژیک، بلغارستان، کانادا، جمهوری چک، دانمارک، استونی، فرانسه، فنلاند، آلمان، ایرلند، لتونی، لیتوانی، هلند، نیوزیلند، مقدونیه شمالی، نروژ، پرتغال و سوئد رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76147" target="_blank">📅 18:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76146">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFDRVQWNxl2jdbvb_dWFX64whUG3TPKz_mMhnAEosIiJO0j_JSzdjlMuhx1mImqrVn3EdteGdUpqP7t-Cw2SGnuualBcUeNetsMxqKwScc_iilOFiRaHsGliMFaaa_M3BFUuMCtv-6YlwkCjBQ2lm3b1HffpG2L-Zx1r4LndyVyuaTEUd3wwmPwcf3AjLqZNAHXP84JbKbDDnOuDDusxOIBPvVOBbJA26Sezi5BARmkDPAK_pFlU65E4qZVo-blBlqqtEvvGLJnQfqGzCO1-BTHG5TyGUYy_SBz9x3k_ER6iIBtYVccUdtbFn9sgRpirPeNNfU22oM-VN8cZeROwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای حکام آژانس بین‌المللی انرژی اتمی روز چهارشنبه قطعنامه‌ای با حمایت آمریکا را تصویب کرد که از ایران می‌خواهد ذخایر باقی‌مانده اورانیوم غنی‌شده خود را اعلام کند و به بازرسان اجازه دهد آنها را راستی‌آزمایی کنند.
به گزارش خبرگزاری رویترز، دیپلمات‌های حاضر در نشست غیرعلنی اعلام کردند که این قطعنامه که از سوی ایالات متحده، بریتانیا، فرانسه و آلمان ارائه شده بود، با ۲۱ رأی موافق، ۳ رأی مخالف و ۱۰ رأی ممتنع به تصویب رسید.
به گفته این دیپلمات‌ها، روسیه، چین و نیجر به این قطعنامه رأی مخالف دادند. آنها همچنین افزودند که ونزوئلا اجازه شرکت در رأی‌گیری را نداشت.
هیئت نمایندگی ایران در سازمان ملل و سایر سازمان‌های بین‌المللی در وین در واکنش به تصویب این قطعنامه، آن را «سیاسی» و «عاری از حرفه‌ای‌گری مورد انتظار از یک نهاد فنی» خواند.
در بیانیه این هیئت نمایندگی آمده است که تهران «از حقوق مسلم خود، از جمله در پاسخ به این قطعنامه ناقص، کوتاهی نخواهد کرد.»
تصویب این قطعنامه می‌تواند مذاکرات جاری بین ایران و آمریکا برای رسیدن به توافق صلح را پیچیده‌تر کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76146" target="_blank">📅 18:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooBMXMmMnH5Z86N8fOAbu3KRF9jcUf2t2eZYaoZFUmwFV5BFG2BnZTPQ8BhRtggTBw21OBCT7hghFyIES3VlrNxecw3TljhaiazJcGZsDnp3ilqVUhz-urPSA-eiYX4PWfFEgtGPG7tBkdhg_wNazLseX0aGGMwtQhbniiCJXI2AYOUUme4ZhWFZNBulCMJ9p2mI32brAkAJ9ho77s24_8X0rj9xnoko2H2rfxm_H9Zb-x6MYjYF1EPfdH9krvcMy7lZ5T7ESx51eRDkjDQ8upQ7HBPXxugYTn50cF2_WtZg-sLYsCUknNFcqs3W1H2LeoZDG3hVzjEteCqjxQEqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا در گفتگو با شبکه فاکس‌نیوز اعلام کرد که دلیل سقوط روز دوشنبه بالگرد آپاچی آمریکا در نزدیکی تنگه هرمز، یک پهپاد ایرانی بوده که در بدنه این پرنده نظامی و در فضای میان دو خدمه آن گیر کرده بود.
به گزارش فاکس‌نیوز و به نقل از گفتگوی تلفنی ترامپ با تری اینگست، خبرنگار این شبکه در روز چهارشنبه، این بالگرد آپاچی در ارتفاع پایین در حال پرواز بوده که پهپاد ایرانی بدون منفجر شدن، درون این بالگرد جنگنده گیر می‌کند. بر اساس این گزارش، خلبانان پس از این اتفاق بالگرد را به همراه پهپادی که درون آن بوده، به پایین هدایت کرده و در آب افتاده‌اند.
در پی این حادثه در شامگاه دوشنبه، فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد که «حملات دفاع مشروع» را علیه اهدافی در ایران انجام داده است؛ حملاتی که در ادامه منجر به پاسخ تلافی‌جویانه ایران و هدف قرار گرفتن تأسیسات نظامی آمریکا در سراسر خلیج فارس شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76145" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76144">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OevLYHbZUDWXRf1dFXyP93-w9JoA2ojX94GEVLjcp63wSkoUM3RQpDyk0srEk7YrGOZYZmZtSdjySwVrVqQ6O1ip5xBNIdg29Xr2MaliCbfcgyQUaQSrcEYlU1rqCyGnhfAgtNiRVFCZtW00uzFlgZA4b5t8wUVW_-wLryxStCFosfG1ftXKdbj6mV2Mni2v_VaFnj4nUE9G0gVJv43In2X0CnZhZF1Ep2isHjGxaeb39M5wV3aaAdF-ZuUtxdT2Wy7K0REfICyX26JKRJwX1aNDptecWozyWBZHA8DkKOD_N07YChmS_IC1y9ZqswBV01ks8JY1lcty3jkLoF-E9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های مختلف به نقل از دیپلمات‌ها از سفر یک گروه مذاکره کننده قطری به تهران در روز چهارشنبه برای رسیدگی به اختلافات باقی‌مانده بین ایالات متحده و ایران خبر دادند.
خبرگزاری فرانسه به نقل از دیپلماتی آگاه به این سفر نوشت که این گروه مذاکره کننده قطری «پس از مشورت با ایالات متحده» به تهران سفر کرده تا در دیدار با مقام‌های ایران «شکاف‌های باقی‌مانده را پر کنند.»
از زمان آتش‌بس میان ایران و آمریکا و اسرائیل، پاکستان به عنوان میانجی اصلی مذاکرات صلح میان ایران و آمریکا را هدایت می‌کرد اما در هفته‌های اخیر قطر نیز به عنوان میانجی دیگر تلاش کرده تا امکان برقرای تفاهمی میان ایران و آمریکا را فراهم کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/76144" target="_blank">📅 18:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76143">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OqTnbWy4pmcVsdMU8ClpA2ilAh2hNQ2TT_gTiRajASZF8PLW43x6CfhWVvGYGlxs1ZOD_MCkNOOg7GzZtpBFaYrq5yasCl8omcrg7TlCDB8s5HaysP2cxhGW9aflxgvscVYmEFx05psg2EKRSFCY0IzbjwB4KSAMuXC9fF7veoiwcVhdh3v1dAycwdGe8G4q8tWM5-VlRk_-hNO8Ho7BHCu1h-UIiUZLU6bFvrOaSGX20vNw1QjFiGgJQnS1vY1VmIdXAZAj3NsRUdWiTcskRJEZp1v1EFb2udZAFBwyDAt1Snzt-hy9Sq-ou2OukRFPq4bgQuNB3DSSvhpZ4CN5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: ممکن است به‌زودی دستور حمله به نیروگاه‌ها و پل‌ها در ایران را صادر کنم
دونالد ترامپ، رییس‌جمهوری آمریکا، در مصاحبه با فاکس‌نیوز گفت ممکن است به‌زودی دستور حملات جدید به نیروگاه‌ها و پل‌ها در ایران را صادر کند.
او دلیل این موضوع را طولانی شدن روند مذاکرات از سوی جمهوری اسلامی عنوان کرد و افزود تهران دستیابی به توافق را بیش از حد به تاخیر انداخته است.
ترامپ تاکید کرد صدور دستور حملات جدید نزدیک است و گفت اگر روند مذاکرات تغییر نکند، تصمیم‌های تازه‌ای اتخاذ خواهد شد. او افزود ۵۵ درصد از سامانه‌های راداری که جمهوری اسلامی در دوران آتش‌بس بازسازی کرده بود، در حملات جدید آمریکا نابود شد.
🔻
دونالد ترامپ: محاصره دریایی جمهوری اسلامی، یک دیوار فولادی است
دونالد ترامپ با انتشار پیامی در شبکه اجتماعی تروت سوشال، محاصره دریایی بنادر جنوبی ایران را کارآمد خواند و آن را به یک «دیوار فولادی» تشبیه کرد.
در این پیام آمده است: «رسانه‌های جعلی از گزارش میزان اثربخشی محاصره دریایی آمریکا خودداری می‌کنند. این موفق‌ترین محاصره در تاریخ جنگ‌های دریایی است.»
رییس‌جمهوری آمریکا ادامه داد: «ایران هیچ داد و ستدی انجام نمی‌دهد، به نیروهای نظامی خود حقوق نمی‌دهد، بدهی‌هایش را تسویه نمی‌کند و به‌سرعت در حال تبدیل شدن به یک کشور شکست‌خورده است.»
🔻
ترامپ: حمله بامداد چهارشنبه جمهوری اسلامی به بالگرد آپاچی ناکام ماند
دونالد ترامپ، رییس‌جمهوری آمریکا، در مصاحبه با فاکس‌نیوز گفت در حمله بامداد چهارشنبه جمهوری اسلامی، یک پهپاد ایرانی به یک بالگرد آپاچی اصابت کرد اما منفجر نشد.
او افزود این پهپاد میان دو خلبان گیر کرد و با وجود برخورد، انفجاری رخ نداد.
ترامپ گفت خلبانان بالگرد را در دریا فرود آوردند و برای نخستین بار در تاریخ نظامی آمریکا، به وسیله یک شناور دریایی بدون سرنشین نجات پیدا کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76143" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76141">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZpehcRPMobECo7xeii9Ka78DG-_0vYzLXHRg8Ht2VIm2wldzo6lMiEPWEMcHGcks7j6MH_xgRVsV2wIF1GxI8r5V9Tit4PWNsmdNoQqAzcWwCCwrYgNNXeMTMx0O4RBilloYkzAR8TUnoFIy2scrseQXrWV2jPQSPB-KbomgGKRQBVGDHSzjiO6k6MZxNH2UyLSL2DhGe3_gEJuxJ3G9-VlkPNADfZ9TNkPpiKmDys62VK5DM1pc-aVTx_nei6LPizd-9dSyJop_vfTqFoC1CPIvNKAjxdBTrfBC0GufOLOMp4po_Gr5P2Dhod84jgGaKxdtYphTcSjvecU7eXgmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a780747f7a.mp4?token=ADIqLjiW8OtCnZZ1RFVF3gpGFYwO9Ls8zH6tBVpvEE5z2T95p4FIlOnhhVLgg-eZt1leHLcF1SVEFn0GGYQotPRCjgd510viioZseuyUh7qySsWUs2A6eW9BR2vnXDuxyJYh9qkpVpL5Y2_VwSVCdGbH4kARkd2_FFWqeUu6_p-ZAYQgJNWrNVo-P7jT9ORf9W1R0k0ZHWba0Iwt9ZG2_rCrhUc3_ZnOeoqVcQW5YmHY_cjJRV0O9_WBbTL4J7ZrEM9YMiOqq75UDvtVAWLdNXs2VaclUsFaOQwneatOtEjI9cW-tN-Z1-Bj9SGk72JG_aYgXErGiMJTgyJiTkBMhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a780747f7a.mp4?token=ADIqLjiW8OtCnZZ1RFVF3gpGFYwO9Ls8zH6tBVpvEE5z2T95p4FIlOnhhVLgg-eZt1leHLcF1SVEFn0GGYQotPRCjgd510viioZseuyUh7qySsWUs2A6eW9BR2vnXDuxyJYh9qkpVpL5Y2_VwSVCdGbH4kARkd2_FFWqeUu6_p-ZAYQgJNWrNVo-P7jT9ORf9W1R0k0ZHWba0Iwt9ZG2_rCrhUc3_ZnOeoqVcQW5YmHY_cjJRV0O9_WBbTL4J7ZrEM9YMiOqq75UDvtVAWLdNXs2VaclUsFaOQwneatOtEjI9cW-tN-Z1-Bj9SGk72JG_aYgXErGiMJTgyJiTkBMhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل ظهر چهارشنبه ۲۰ خردادماه، ساعاتی پس از صدور هشدار تخلیه برای ساکنان شهر صور و مناطق اطراف آن، این شهر در جنوب لبنان را بمباران کرد.
@
VahidOOnLine
بنیامین نتانیاهو در واکنش به محکومیت حملات اسرائیل در منطقه از سوی رجب طیب اردوغان در بیانیه‌ای گفت: دولت اسرائیل و ارتش اسرائیل، که اخلاقی‌ترین ارتش جهان است، به اقدام قاطع علیه ایران و نیروهای نیابتی آن که خاورمیانه و سراسر جهان را تهدید می‌کنند، ادامه خواهند داد.
نخست‌وزیر اسرائیل در این بیانیه گفت: دیکتاتور یهودستیز اردوغان که در حال نسل‌کشی علیه کردهاست، از سازمان «تروریستی» حماس حمایت می‌کند، مردم خود را سرکوب می‌کند و مخالفان سیاسی را زندانی می‌کند، آخرین کسی است که می‌تواند برای اسرائیل موعظه اخلاقی کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/76141" target="_blank">📅 17:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76139">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۲۰ خرداد گفت که ایران برای رسیدن به توافقی که می‌توانست برایش بسیار خوب باشد بیش از حد تعلل کرد و حالا باید بهای آن را بپردازد.
دونالد ترامپ در پیامی در شبکه اجتماعی خود، تروث سوشال، نوشت: «ارتش ایران کاملاً در وضعیت آشفته‌ای قرار دارد. بخش زیادی از آن، مانند نیروی دریایی و نیروی هوایی، عملاً دیگر وجود ندارد؛ آن‌ها کاملاً شکست خورده‌اند».
او افزود: «ایران فقط حرف می‌زند و عمل نمی‌کند. قلدر خاورمیانه مُرده است!!! آن‌ها برای رسیدن به توافقی که می‌توانست برایشان بسیار خوب باشد بیش از حد تعلل کردند و حالا باید بهای آن را بپردازند!!!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/76139" target="_blank">📅 17:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud0VJBpc0sUAoI_o5jMAsIa9-wB9sspzIsDAlV2zTo63DdqC_wMDn_jTH-llNTCAGhgFBlh9K6umQa5WhMatd5fBEAss0VGF0PTT2-gvZ9-uaS7Z5LqErBOYXHrBRFcv3fl4apYdBOGuQqa6UiNBkSvRKmUUI1QzEcJtDxZSCElR2zowby8IWAjgaGbIKx1M9xO5lmNF9msImBkvLdWFo9KRb1f97tynlAdEw7Gj2BdDHaWljpqvnvg0BzUOUQ3ZmJZhURgpljrHPr4EdeWvkBsduBGMr6yYNXcgVuseOrInRy9ChcH7AjHTuIyoMFcbIa2-4z-wq9yh3lD8Taa4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه ایران درباره تأثیر درگیری‌های نظامی اخیر بر مذاکرات با آمریکا گفت ««باید بررسی شود، دیپلماسی و میدان دو امر جدا از هم نبوده و در امتداد و عرض یکدیگر» هستند.
اسماعیل بقائی روز چهارشنبه ۲۰ خرداد دربارهٔ آخرین وضعیت مذاکرات هم گفت: «با توجه به تحولات دیشب باید بررسی کنیم. روند دیپلماتیک در خلأ اتفاق نمی‌افتد و برای پیشبرد هر فرایند دیپلماتیکی نیازمند فضای حداقلی هستید تا بتوان روند جاری را پیش برد.»
شب گذشته ارتش ایالات متحده، در واکنش به سرنگونی یک بالگرد آمریکایی در سواحل عمان، حملاتی را به جنوب ایران انجام داد و ایران نیز در واکنش به شلیک موشک به برخی کشورهای منطقه اقدام کرد.
دونالد ترامپ که پیشتر بارها از نزدیک بودن توافق خبر داده بود، هنگام انجام عملیات آمریکا در جنوب ایران گفت: «ما توافقی بسیار خوب داشتیم و احتمالاً همچنان خواهیم داشت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76138" target="_blank">📅 17:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY5LvC-YfsOaZJinK-BsTa0t0ffOZAaVyVPGh0McTAkygAJHdGp1PDRyNjLDEhXz_QXqPAgj5dyDcZ_zSfvgrLpvqwV09svHbaAXvDTpBYS_oeIk_lSkNEAdLj9iT3oQlEYCZjKMBvUj3QIQkVa1h0oHVQzz-n7A9J69Qo-aab3q0Lg4ChYbe__c_k0J88dtaCuczVHJHviQYMeGUtDpU1s0h8KHvRh_TNUf2I5eKZOZbV3M4sYJufY0Sp742KZo0Yc8lqMwUUv1QyznkCCNsdfkhjD5PyUb3SbvqmNuAgl9pA9VaJAg141fLo65Z2r-FNSFFKvAZPVdWtgNM0UQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه، حملات موشکی و پهپادی جمهوری اسلامی به بحرین، کویت و اردن را به‌شدت محکوم کرد.
وزارت خارجه امارات در بیانیه‌ای این حملات را «تروریستی» و «بی‌دلیل» خواند و اعلام کرد که هدف قرار دادن پادشاهی بحرین، دولت کویت و پادشاهی اردن هاشمی، نقض آشکار حاکمیت این سه کشور و تهدیدی علیه امنیت و ثبات آن‌هاست.
در این بیانیه همچنین آمده است که امارات همبستگی کامل خود را با بحرین، کویت و اردن اعلام می‌کند و از همه اقداماتی که این کشورها برای حفاظت از امنیت و ثبات خود انجام دهند، حمایت می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76137" target="_blank">📅 17:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ivZe2g0vX-gxKCkIlSH3z4cOT5K7aVmxy-f07HzoZeaFmaxY9xNMSDPs9-IIKjICf1GYr58HZbXTdD-QIHGd06SreEmiCd9jYHpy2IjhpL3wnMUVm165XALyitDsJhSi417LzJLpuUqQ9Hnffo1MBOh0-lzpjl1Mn3MgUxAeaVtCbxbaUJfci8x00B9ayp9DkkoxgT4rnJpoBxNBku5ZqKclSTMF_f-jlgoUVvGCMkPIoo-iUVNVJxZoUWAY49rdiFmGSsk3a02XcVAzkaVjBFWJwOFwRltGM5ldcIFw2Ev6C7bkMm87S3_Icut5Hy-_iEN1xvvL5gpvGBntH-mVJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NEVHvXdVGUIV-88in_t_yhibsALLsFMjHMIQzB5q1C3tcX-JuMmMxqE1-ONel7PWKmTxTODveETZNfmemBL5dr_qlX9iwrK-Mx_cRuCrdetxzMeoyY4ZQojyXuY2uZLQosJt9rwJziEah1qoWO0paEl7lz_BUBt-dNf0RHc-tc_R-5ehf7cCGJCpW5j1-1b4HPISMFuzCYdZ3PS7m3TrtUg6SLh1N54hqSbz0mscOUbSQQ73fFBVIHxlLXzVEVcULsWbXQ3umPhkmXlPg6actv-q3NcJsbrmrl6_e6h_rlFeoGVW49OA9CZlxXubVp3Gh8fK3EIfW9BQwYTfpTctiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انجمن اسلامی دانشجویان دانشگاه صنعتی شریف با صدور اطلاعیه ‌ای از اعمال نخستین حکم اخراج یک دانشجو توسط شورای انضباطی این دانشگاه خبر داد.
به این ترتیب، رضا دالمن، دانشجوی کارشناسی ارشد مهندسی کامپیوتر، به اخراج و محرومیت از تحصیل در تمام دانشگاه‌ها به مدت چهار سال محکوم شده است.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف اعلام کرد که آقای دالمن با وجود تبرئه از سوی دستگاه قضایی، از سوی شورای انضباطی دانشگاه با این حکم سنگین روبه‌رو شده است.
این انجمن یادآور شد که حکم اخراج دانشجوی فوق برای تأیید به وزارت علوم ارسال و در روزهای اخیر نیز حداقل برای یک دانشجوی دیگر نیز حکم «بدوی اخراج» صادر شده است.
رضا دالمن، در ۲۸ اسفند سال ۱۴۰۴ و در اوج جنگ ۴۰ روزه از سوی نهادهای امنیتی بازداشت و پس از یک ماه با قرار وثیقه آزاد شده بود.
@
VahidHeadline
پیش‌تر گزارش‌هایی منتشر شده بود که یکی از دلایل بازداشت او، آویختن یک عروسک موش از درختی در محوطه دانشگاه عنوان شده بود؛ اقدامی که در فضای اعتراضی آن زمان، با اشاره به لقبی که برخی معترضان برای علی خامنه‌ای به‌کار می‌بردند، انجام شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/76135" target="_blank">📅 17:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76134">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5eljf5YqZ7cJnvn6nzUC60F0zyG-yApx6h9ARCzw9FF1erSufKLfa4BZQG8JzqIwElkzZqt08jOgVZaNZKLlwgs6h24eGXD6HfKY9syRVXD-HKhObHRKdmBw0vfaHwFJI7Ui27LiH5DQt0IOgNZBUXBup1g_nfxDfj7CfPPOp05KkpFIvsAHcyt-LFwMZDnGkGKCkTy_6hU7-Ys4Ug764XIr1LMecyntiUYzYX6o2V-ywU4VOx5-6qP8F9OvB5qJ3BO6vqVRFETB9GV5LCTJYY3OBVfIn8pysG2E4eYsJV9osdaHyoRn4xxsHa0hDH_m3Ew0NthEUNHddEuhIpJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی روز چهارشنبه ۲۰ خرداد خبر داد که صادق زیباکلام، استاد سابق دانشگاه تهران و فعال سیاسی، بازداشت شده است.
خبرگزاری میزان، وابسته به دستگاه قضائی ایران، اعلام کرد که «قرار نظارت قضائی» بر آقای زیباکلام روز ۱۷ خرداد تشدید شده بود و به دلیل انجام مصاحبه‌ای جدید، علیه او اعلام جرم و سپس صبح امروز بازداشت شد.
اعلام جرم روز ۱۷ خرداد در پی انتشار مصاحبه صادق زیباکلام با شبکه بریتانیایی «کانال ۴» رخ داد.
این فعال و تحلیلگر سیاسی در این گفت‌وگو به زبان انگلیسی، علی خامنه‌ای، رهبر سابق جمهوری اسلامی، را «ستون فقرات تندروها» در ایران خواند و گفت او در طول مدت رهبری خود به مدت ۳۶ سال ایده‌هایی مانند «آمریکاستیزی، نابودی اسرائیل، حمایت از حماس و حزب‌الله» داشت.
زیباکلام درباره مجتبی خامنه‌ای، رهبر جدید، نیز گفت تردید دارد او ایده‌های پدرش را داشته باشد و همچنین اعلام کرد که او نمی‌تواند قدرت و جایگاه رهبر سابق جمهوری اسلامی را به دست بیاورد.
او در اردیبهشت ۱۴۰۳ در پی تشکیل سه پرونده قضائی بازداشت شده بود و تیر ماه همان سال به دلیل «ابتلا به بیماری سرطان» از زندان آزاد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76134" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKmDpVw894pCSBNO_uE3X57IQsTClLHyz7JC1E5JpCOPgReQgNUEUsAFd9tQev4da00vXxDjKE_UMpg8DvNfukQh0p9ZdYO2VEuA2-efbrn8Kl2oLJiYF3L44F9o2HNdnRA3iphOglV-3A4zf4jDM_qq96RoNuhRpptbHA-MmA9KGk7oBTZgbXpzU9iBallAjyTEsu5vgdwBsqONAXzKQMCJqg9RZw49CpzmlLJ8yXrv3PEfc2IpHgEij3PTquO9w15MYZ6uCCJ9vr7Z6WT9wCrSPqiqZHJ0LEliTjPVXEqEnE-QuRfGbdWRhEF17S6vxfIdWmAwLFAdlJoAQpXBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
«از آغاز سال ۲۰۲۶، بنیاد عبدالرحمن برومند دست‌کم ۷۱۱ مورد اعدام را در ایران ثبت کرده است. این آمار شامل دست‌کم ۶۶ مورد اعدام در ماه مه و ۱۸ مورد تنها در نه روز اول ماه جون است.
‏
@IranRights</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76133" target="_blank">📅 17:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2b79c4913.mp4?token=Hr-3iqeKtvXzbJF1ulUzl9BoRxdHG1C4LHU0UgoH6mHl755WRVY_yF1DvEf6IRvCQfLD5jakw3dpkpD5HmMPlq-PhCe_6EiP7EwrWIKRR07R9U0RxtnH4xL3KzhK3bt08-ZWT_yHu237YodXRtyBtKmskNfryVSC-WKsaawWNQGru_DxWwsYLi48G2eoLW7tuxzOSsFL8mup2doMuSkQOONEw8cMNb8gORFYaX4IABKLJUEj9NyVWSu-yUH38wfGtfkPV3dcB6pysuTnbmGJmQ2Z-Da6ATIsV-_lFt82VVTneJkZGNntMGLoszK6k2xIAIAAq01I85dKuZ4s3InQdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2b79c4913.mp4?token=Hr-3iqeKtvXzbJF1ulUzl9BoRxdHG1C4LHU0UgoH6mHl755WRVY_yF1DvEf6IRvCQfLD5jakw3dpkpD5HmMPlq-PhCe_6EiP7EwrWIKRR07R9U0RxtnH4xL3KzhK3bt08-ZWT_yHu237YodXRtyBtKmskNfryVSC-WKsaawWNQGru_DxWwsYLi48G2eoLW7tuxzOSsFL8mup2doMuSkQOONEw8cMNb8gORFYaX4IABKLJUEj9NyVWSu-yUH38wfGtfkPV3dcB6pysuTnbmGJmQ2Z-Da6ATIsV-_lFt82VVTneJkZGNntMGLoszK6k2xIAIAAq01I85dKuZ4s3InQdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
realDonaldTrump
چت‌جی‌پی‌تی:
ترامپ سکانسی از سریال معروف سیاسی The West Wing منتشر کرده است؛ سکانسی که برای مخاطب آمریکایی معنای کاملاً مشخصی دارد.
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
اهمیت انتخاب این سکانس در این است که ترامپ پس از حمله‌ای که رسماً «متناسب» توصیف شده، پیامی دوگانه می‌فرستد: از یک طرف می‌گوید پاسخ فعلی کنترل‌شده و محدود بوده؛ از طرف دیگر هشدار می‌دهد که محدود بودن این پاسخ نباید به‌عنوان ضعف تعبیر شود. پایان سکانس با تهدیدی روشن همراه است: اگر آمریکایی کشته شود، پاسخ بعدی می‌تواند از چارچوب «متناسب» خارج شود و به «فاجعه کامل» تبدیل شود.
با این حال یک نکته مهم در خود سریال وجود دارد: بارتلت در نهایت توسط مشاورانش از واکنش نامتناسب بازداشته می‌شود و به پاسخ محدود تن می‌دهد. بنابراین ترامپ با انتشار این بخش، بیش از آنکه کل پیام سریال را بازگو کند، بخش خشم‌آلود و بازدارنده آن را برجسته کرده است؛ پیامی برای تهران، و همزمان برای مخاطب داخلی آمریکا: «فعلاً محدود زدیم، اما گزینه بزرگ‌تر هنوز روی میز است.»
گراک:
**این سکانس از سریال تلویزیونی «The West Wing» (نام فارسی: بال غربی یا اتاق بیضی) است.**
دقیقاً فصل اول، قسمت سوم با عنوان **«A Proportional Response»** (پاسخ متناسب).
### زمینه داستان چیست؟
این صحنه ادامه مستقیم قسمت قبلی (قسمت دوم فصل اول به نام «Post Hoc, Ergo Propter Hoc») است. در قسمت قبل، یک هواپیمای آمریکایی که دوست شخصی رئیس‌جمهور **جوزایا بارتلت** (با بازی مارتین شین) داخل آن بود، توسط نیروهای سوری سرنگون می‌شود و چند آمریکایی (از جمله دوست رئیس‌جمهور) کشته می‌شوند.
رئیس‌جمهور بارتلت که معمولاً آدم آرام، باهوش و اخلاق‌گرایی است، این بار بسیار عصبانی و دنبال انتقام شخصی است. او در اتاق وضعیت کاخ سفید (Situation Room) با دریاسالار **فیتزوالاس** و مشاوران نظامی‌اش جلسه دارد.
### معنی و مفهوم مکالمه چیست؟
نظامی‌ها گزینه‌ای به نام **«پاسخ متناسب» (Proportional Response)** پیشنهاد می‌کنند. یعنی:
- سوریه (یا نیروهای مورد حمایت آن) یک هواپیما را زده → ما هم چند هدف نظامی محدود مثل انبار مهمات، پل راه‌آهن و ساختمان اطلاعاتی‌شان را بزنیم.
- این کار «عادلانه» و «متناسب» با خسارت واردشده به نظر می‌رسد و جلوی escalation (تشدید درگیری) را می‌گیرد.
**رئیس‌جمهور بارتلت** اما این منطق را قبول ندارد و با عصبانیت می‌پرسد:
> «فضیلت پاسخ متناسب چیست؟ چرا خوب است؟
> آنها یک هواپیما را زدند، ما یک فرستنده را می‌زنیم؟ این پاسخ متناسب است؟»
او استدلال می‌کند که:
- دشمن دقیقاً می‌داند ما چه کار می‌کنیم (چون همیشه همین کار را کرده‌ایم).
- بنابراین اهداف را از قبل تخلیه می‌کنند (مثل همان انبارها و پل‌هایی که سه روز است خالی هستند).
- نتیجه؟ پاسخ ما بی‌اثر می‌شود و دشمن جری‌تر می‌شود.
بارتلت می‌خواهد **«پاسخ نامتناسب» (Disproportional Response)** بدهد:
> «اگر یک آمریکایی را بکشید، هر آمریکایی، ما با پاسخ متناسب برنمی‌گردیم.
> ما با فاجعه کامل برمی‌گردیم.»
یعنی ضربه‌ای آن‌قدر سنگین و غافلگیرکننده بزنیم که دشمن برای همیشه بترسد و دیگر جرأت حمله نکند.
### در نهایت چه اتفاقی می‌افتد؟
وقتی نظامی‌ها گزینه شدیدتر را پیشنهاد می‌کنند (بمباران فرودگاه که هزاران کشته غیرنظامی دارد)، بارتلت عقب‌نشینی می‌کند و همان پاسخ متناسب اولیه را انتخاب می‌کند. این نشان‌دهندهٔ تعارض درونی اوست:
- از یک طرف خشم و احساسات شخصی (چون دوستش کشته شده).
- از طرف دیگر مسئولیت ریاست‌جمهوری و ترس از کشتن بی‌گناهان و شروع جنگ بزرگ‌تر.
### چرا این صحنه این‌قدر معروف و مهم است؟
- نوشتهٔ **آرون سورکین** (نویسندهٔ نابغهٔ سریال) است و دیالوگ‌هایش بسیار قوی و فلسفی هستند.
- نشان‌دهندهٔ یکی از تم‌های اصلی سریال است: تعارض بین **ایده‌آلیسم** و **واقع‌گرایی** در قدرت.
- مارتین شین در این صحنه بازی فوق‌العاده‌ای دارد و عصبانیت، ناامیدی و در نهایت پختگی بارتلت را به زیبایی نشان می‌دهد.
- خیلی‌ها این صحنه را نمادی از سیاست خارجی آمریکا می‌دانند: آیا همیشه باید «متناسب» پاسخ داد یا گاهی باید قاطع و بازدارنده عمل کرد؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/76132" target="_blank">📅 07:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76131">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdGP6mmtfx-60iH0S7MN-5lUjK-YDth49Qh3lyPl9-v36ObJiqL6mfyq6vPDOFxxmadvHOYUJT_LCPCNRMqoO9qE_ebqE6N5n3lGNCyyftDiHdnYzfWmaQ0ceygrgDxnbt_qdbH_mvZ3vB6EsbLJ7SVJ69jS9tdP6DoQ1Yn25uKFwcmOUnFx1S2GVnT-sSNYzdmDjRy8ed5k1e4xRzdL5tVBRpe38UQG_8t2v5ZLplxz69Zrx8jgRmwJ-SX4qNkOD2CMISPnGkS7XcF4DxTY2IH_bg4mLdUU3GhmwFLJa7PU_22cjWcNMH9ZUbo-bB8cFor6w_9F-v3t2rKI2m5asw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درحالی که سپاه پاسداران ادعا می‌کند ۲۱ پایگاه آمریکا را در منطقه هدف قرار داده است، نیویورک‌تایمز صبح چهارشنبه به نقل از یک مقام آمریکایی نوشت که برآورد‌های اولیه حاکی از آن است که تقریبا همه حمله‌های ایران رهگیری شده و هیچ گزارشی از خسارت به پایگاه‌های آمریکا یا تلفات نیروها مخابره نشده است.
یک مقام آمریکایی دیگر نیز به نیویورک‌تایمز گفته، ادعای سپاه درباره حمله به پایگاه‌های آمریکایی صحت ندارد. هنوز مقامات سنتکام به‌طور رسمی در این زمینه اظهارنظر نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76131" target="_blank">📅 07:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76130">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omgBAO31N2F9eibAz5kIlmyubz3JTc30TCiUGjBIzZcMpizfjXwRdb6KMVUpNU3Fpj5CnkfQT9NhIorlD2ecBL5KhIjMLbjMBw0mR_JaBTqF9MeoFd2T7BzMb8FgpIXWDlvQla6lsZ0krR7u2Wabwy_p8wK5WVJm83Hc0oZqnqrmee54Z2RsV5ajKZ67txVmyv_-ztMQM919ZchRhzr_YluhpREFRSBzd8LSQhwtM0EAmKYHaZkStrH9PPd5BUKqBGr50DPzKR_B4zEJ2vPANVeeeSk1e3HsOSSjQeUZ0AIYXMZY7-IdXNLMi372J0LAx58xMAUrFcJJKOdWhvdmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش ایران و سپاه پاسداران اعلام کردند که «با موجی از حملات پهپادی، پایگاه‌های آمریکایی و سامانه‌های راداری ناوگان پنجم ایالات متحده را در بحرین هدف قرار» دادند. همچنین گزارش‌هایی از حملات سپاه و ارتش به پایگاه‌های آمریکا در اردن و کویت منتشر شده است.
ارتش ایران می‌گوید این حملات را «اقدامی متقابل» در پی «مزاحمت‌های» آمریکا برای ساکنان جنوب ایران خوانده است.
خبرگزاری فارس گزارش کرده که سپاه پاسداران به پایگاه ارتش آمریکا در اردن حمله موشکی کرده است.
سپاه پاسداران گفته که با «موشک‌های سوخت جامد دور برد خود ۴ هدف مهم از جمله آشیانه‌های جنگنده‌های اف‌۳۵ در پایگاه هوایی و مرکز فرمانده کنترل ارتش» آمریکا در الازرق اردن را مورد هدف قرار داده است.»
باراک راوید، گزارشگر اکسیوس به نقل ازمقامات آمریکایی می‌گوید که دست‌کم ۴ موشک بالستیک و چندین پهپاد به سوی پایگاه‌های آمریکا در بحرین،‌ کویت و اردن شلیک شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76130" target="_blank">📅 05:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mmEIkHlkoLNrH6QWysJQ7giB0xcUYENFXv4jbor_ba4SJgYF9IDZW2lN2tKgntAT6fJv0YKpZbd28XNzn0goz4uQ2YHYzthR6H0OdxGHQjJu4vplWR3w86BX8n5nfVYASqbkK0rRcsdaWicOFWAOGLVdC6FbSH2BDaxt3n3HATuyYI5rE6bTpyvWF0VmmDOzn8d5LyvFyd964k-rOYy1pevfuMwzpz8tCWH_FTCRQspz_Enw35v43gjBX4Dgvpdih4XS6E-B66e9ib8wLgnmiQQJrfCFKCQesIrt9gn03ViOx2_txAQKsBNDsm4XI2yqb3rTc4ymGYxGu-s7CovcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه از حمله به ۲۱ هدف در پایگاه‌های آمریکا در منطقه خبر داد و گفت نیروی هوافضای سپاه با موشک‌های سوخت جامد دوربرد، چهار «هدف مهم»، از جمله آشیانه‌های جنگنده‌های اف-۳۵ در پایگاه هوایی و مرکز فرماندهی و کنترل ارتش آمریکا در الازرق اردن را هدف قرار داد و منهدم کرد.
@
VahidOOnLine
توییت اکانت وزارت کشور بحرین، ترجمه ماشین:
آژیر هشدار به صدا درآمده است. از شهروندان و افراد مقیم درخواست می‌شود آرامش خود را حفظ کنند، به نزدیک‌ترین مکان امن بروند و اخبار را از طریق کانال‌های رسمی دنبال کنند.
moi_bahrain
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76129" target="_blank">📅 05:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n3ejOe0R1FUWSV_rWT0iJjFf_hP9Y9rtEAq0AuxDeB0iGuJHMGzeHeqBmnj2M-zDSPO70StDz2o1LzmlOzevZMzMzbCL1XsUwGok86nlCO89jOdK6eGgDRIw0_czXdkPpMJzfDqZbVe1VWUM_kl7PnlYIoKIKtLvS_l8X7ERkroW0Qg0tF6UKW4blcXVczgZFyau9RLXbsP8i82lXdd3h4iSPIGY3OjZqNlpDNII7M_2Xy1bz_mE-wyAB_1yr1arz2rdb-xheXKy6CI6mKJx5tYUvyq5p0k7L2jCoWEnsjUTyN8EpPPF01n-4L9clVx3Eqiwti8jNSZXUmzTrCKVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار فاکس‌ نیوز، جنیفر گریفین می‌گوید که یک مقام ارشد آمریکایی به او گفت که سه‌شنبه شب به وقت واشنگتن ۲۰ هدف در داخل ایران هدف قرار گرفت. این مقام گفت اگرچه حملات آمریکا به گفته سنتکام پایان یافته است، ارتش آمریکا آماده است تا در صورت تصمیم جمهوری اسلامی برای تلافی، واکنش نشان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76128" target="_blank">📅 04:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkendx6_btI-p2YnlIhJVkQJmB5EoYAIHgzvD4sfSCm2Rmfam6yD_9Y2SG5KysWa46fnuCHc7Q4UyyqVDmpXrESXaoN4bcAc1deHIJhXyFaa-npv9x0RHvZ_l7fp6MOAmsRRW9dQQbXcFqcrjcwHYXr1BLT3xEL1RwjT03Cj5t-PlrZYOxezZ7HFuzVeY1NNnKWamDu_n9d01ER7IwGtjkA7ImR0kCsmwdrXDBhp8LpdqeoOQirJzjTfe7wc7quMhAUrrgYqAlYZUbdwOss0Mbbghqt7Yisc-fl8sMGmGuaibtSBcPzNXS5RiLeOD8mnN78PzKlEnQT7QeH3TNAssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم الانبیا اعلام کرد ارتش و سپاه در پاسخ به حمله‌های جدید آمریکا علیه جمهوری اسلامی، برخی از پایگاه‌های آمریکا در منطقه هدف حمله‌های قرار دادند.
این قرارگاه تاکید کرد در صورت تکرار حملات آمریکا، جمهوری اسلامی «حملات سهمگین و گسترده‌تری» علیه بانک اهداف تعیین شده در منطقه انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76127" target="_blank">📅 04:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2fc27bcc31.mp4?token=brF4lEjsSDW-cQCqZ6pgU61vhmPjIdcspRPmOABGRMyshDQsK00_12lmEEBShwbYTlo_kKz7WnS-c8UN8KJEBSO-urKzw0cbtgHx7kBvlaHcUDE59mIHaQGJwdsXJdEr91KvnIBU7Jas-BZDyDSirlWs7Xbeo0Lz4uut4BMNBQ9ccHD102nfhTf_wgSnF9P-MsJhDTd53H42DqrWhvGzsPJXAFr0OHWte9mgT65lbtX6cR_sTaCJU6JVR_3SNVapyDeoh-iIz-frQDgectHs-oUZw_d8nCrc8UH6kwcbvX7OAht_W3xhqG4vRMBhETsmH5_ae7WyeJgWvKRnZet4dg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2fc27bcc31.mp4?token=brF4lEjsSDW-cQCqZ6pgU61vhmPjIdcspRPmOABGRMyshDQsK00_12lmEEBShwbYTlo_kKz7WnS-c8UN8KJEBSO-urKzw0cbtgHx7kBvlaHcUDE59mIHaQGJwdsXJdEr91KvnIBU7Jas-BZDyDSirlWs7Xbeo0Lz4uut4BMNBQ9ccHD102nfhTf_wgSnF9P-MsJhDTd53H42DqrWhvGzsPJXAFr0OHWte9mgT65lbtX6cR_sTaCJU6JVR_3SNVapyDeoh-iIz-frQDgectHs-oUZw_d8nCrc8UH6kwcbvX7OAht_W3xhqG4vRMBhETsmH5_ae7WyeJgWvKRnZet4dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید  ساعت ۴و۳۶ دقیقه
خمین ۳ تا موشک پرتاب شد
همین الان پنج تا موشک از خمین شلیک شد ساعت ۴:۳۵
سلام وحید جان  همین الان ازنا لرستان زدن
ساعت4:37
ساعت ۴:۳۵ از خمین چهارتا موشک زدن
از خمین حدود ۴ تا موشک فرستادنننن همین الان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76126" target="_blank">📅 04:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iB2H3EtH4wMjuC-SRHszUl8Psdu7WcMzQwr2x64tw3lxGmVt7Rw9tNI_TPyhR31NWtx1BMUv3tHIc2xEV-k0AC7zPTfhf73-b5TfabAJXBXOcki5PLCPqgqrgrISi6sUz894HskqOS5zbfrprjqrpMokwK15nLogeTJJsj6fAFxgCzVRKYPfHHCfRg-SjfHqAzzjAqaa2Gjc4we92DaDojcD1YJ6Mtdx4OrvJkVgC9YbtucxGqggoFch4Wri1YAIgqm1Vr7C-1UtmbJxgGl_zFqNiPtncaqwKTwo92XvM4d0Gc29naG7PwTtgGXlYfmllJ4gBdmpzLL10LMUZdo-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
آمریکا حملات خود را در پاسخ به حمله ایران به آپاچی تکمیل کرد
"
پست سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده، سنتکام، روز ۹ ژوئن به دستور فرمانده کل قوا، حملات دفاعی خود علیه ایران را در پاسخ به سرنگونی هلیکوپتر آپاچی ارتش آمریکا در روز گذشته تکمیل کردند.
نیروهای سنتکام با استفاده از مهمات هدایت‌شونده دقیق شلیک‌شده از جنگنده‌های نیروی هوایی و نیروی دریایی آمریکا، سامانه‌های پدافند هوایی ایران، ایستگاه‌های کنترل زمینی و سایت‌های راداری نظارتی در نزدیکی تنگه هرمز را هدف قرار دادند.
این عملیات پاسخی متناسب به حملات اخیر علیه نیروهای آمریکایی و کشتی‌های تجاری بین‌المللی در حال عبور از آب‌های منطقه بود.
نیروهای آمریکایی همچنان هوشیار و در موضع آمادگی برای دفاع در برابر تجاوزات توجیه‌ناپذیر ایران باقی می‌مانند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76125" target="_blank">📅 04:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه:
"
سپاه پاسداران: یک فروند پهپاد MQ9 دشمن رهگیری و منهدم شد
در جریان درگیری‌های هوایی جاری در تنگۀ‌هرمز یک فروند پهپاد MQ9 که از آسمان شمال خلیج‌فارس قصد نزدیک شدن و مداخله در صحنۀ نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش رزمندگان قهرمان پدافند هوایی نوین سپاه قرار گرفت و منهدم شد."
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76124" target="_blank">📅 04:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d621f55f6.mp4?token=AUTC0RYXou8BURYeI_aNC-rj75W0PGM49jjoBf7RMh21ag5bz59A0-2HBSJQhnXri1zVZEc1VXAZmYR41VVBgP5J7LlbFC1KOscLdwX3sialHZ3Gqg_BMxRjlQTiYTVW6-G9OGi03ELo9WE3CvB1TYRNYhSWTHy9DWFXaJWGtn-E8T_TueCwgSYKITqLkQa05DmPTYC4_2ZIAwflakhdU_sMBfjIxtbwsuIczYjTGMZSVE66bIOfxzYlR9xXmbmjioQEAkdMxC76k9U6YWoeh9pt9HoC2VUYNhrvXIDm2JJsMn8fpd9jKYr3sTrY1-nns1hpw0baBfZ3rqFcO2NsVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d621f55f6.mp4?token=AUTC0RYXou8BURYeI_aNC-rj75W0PGM49jjoBf7RMh21ag5bz59A0-2HBSJQhnXri1zVZEc1VXAZmYR41VVBgP5J7LlbFC1KOscLdwX3sialHZ3Gqg_BMxRjlQTiYTVW6-G9OGi03ELo9WE3CvB1TYRNYhSWTHy9DWFXaJWGtn-E8T_TueCwgSYKITqLkQa05DmPTYC4_2ZIAwflakhdU_sMBfjIxtbwsuIczYjTGMZSVE66bIOfxzYlR9xXmbmjioQEAkdMxC76k9U6YWoeh9pt9HoC2VUYNhrvXIDm2JJsMn8fpd9jKYr3sTrY1-nns1hpw0baBfZ3rqFcO2NsVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:  دو انفجار در بندر عباس
هنوز درباره محل دقیق انفجارها و جزئیات اصابت‌های احتمالی، اطلاعات دقیقی در دسترس نیست.
دو‌ مخزن آب در سیریک و‌ بندر کوهستک بطور کامل تخریب شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76123" target="_blank">📅 04:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
یک صدای انفجار هم تو اهواز اومد 03:53
سلام وحید جان، اهواز ساعت 3:53 صدای بمب شنیده شد.
سلام همین الان اهواز رو زدن
همین الان اهواز صدا انفجار زدن پنجره لریزید
یه صدای شدیدی اومد که خونمون لرزید همه همسایه ها ریختن بیرون
سری قبل کولر روشن بود اصلا صدا نمیرسید این خیلی شدید بود
آپدیت:
خبرگزاری مهر: صدای انفجار در اهواز شنیده شد
منابع محلی از شنیده شدن صدائی شبیه به انفجار در اهواز خبر می‌دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76122" target="_blank">📅 03:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
از جم شلیک کردن ساعت ۳:۳۳
نصفش تو هوا منفجر شد،بقیه‌اش هم نمیدونم کجا قراره فرود بیاد.
بعد از انتشار پست: وحید جان نزدن،تو آسمون منفجر شد،صدای اون بود.
سلام وحید جان شهرستان جم رو همین الان  ۳ و نیم صبح زدن، یه صدایی اومد ولی چون پنجره‌ بسته است لرزشش خیلی بیشتر بود
ساعت ۳:۳۴  شهر جم رو زدن
اول فکردیم موشک بلند شد
ولی بعدش خورد زمین ترکید
سلام فک کنم جم رو زدن یه صدای انفجاری اومد الان 3:35
توی جم این پدافند بود فعال شد اون صدای انفجار هم پهپاد زدن باهاش
قشم: دوباره یه لرزش دیگه ۳:۳۹
احتمالا بندرعباسه ما داریم حس می‌کنیم
وحید هنوز صدای انفجار قشم داره حس میشه
همین
الان پشت سر هم
سلام وقت بخیر ۳:۳۸ بندر عباس پایگاه هوایی رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76121" target="_blank">📅 03:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbVbEhosdrN8srOR-zDJ_vvJ1_LJkzuRWjNdBnfdAgOZCaHyBSMUQP8WId3ZjzidPFriQoxtVSZ2fK1KuMnYrXkJ6zLMyzJXlS3qbEaMfGGLC63lJ4AEOlHv3ZEj6m_ujSCXSNk6Jl7Uu03f8Bn2Bph9MgZsqb4YNL45BQNBRPTikPacDrqS-WKoWCkKXBKamvuZCWD4vc4Q4ksQUOJvYYHc7OZteiEpU8bdgoPuXimprwjDVU3B3DX6EDpK8f35fVFJHAZp2clC4oC-9FWR7H0PsxUTsp2kYjeDlKaJ98m54cm70ycyAHbin9ciS6VgMRsIH0njOIRlsxQ9znQNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک جانسون، رییس مجلس نمایندگان آمریکا، گفت پیشاپیش از دور جدید حملات آمریکا به جمهوری اسلامی با خبر شده بود. او این حمله‌ها را «متناسب و محدود» توصیف کرد و گفت این عملیات سامانه‌های راداری، موشکی و مراکز فرماندهی و کنترل را هدف گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76120" target="_blank">📅 03:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیام‌‌های دریافتی تایید نشده:
سلام وحید جان، ۰۳:۱۸ و ۰۳:۱۹ دوتا صدای انفجار اومد بندرعباس
الانم دوتا وحشتناک تر
🤯
همین الان بندرعباس صدا اومد ۳:۲۱
سلام وحید همین الان دوتا انفجار شدید بندرعباس
وحید بندرعباس انفجار شدید
همين الان بندرعباس صدا اومد ٣:٢٢ دقيقه
درود بندر ۳.۲۳ انفجار پیاپی + ۳.۲۲
و مجدد ۳.۲۴ بندرعباس
دوتا صدای وحشتناک ۳:۲۳
همین الان بندرعباس
سلام وحید سیریک سمت روستایی طاهرویی صدای انفجار شدیدی اومدم فکر کنم نیرو دریایی سپاه رو زدن
سلا وحید جان، همین الان بندرعباس صدای دوتا انفجار پشت سر هم اومد، ترسناک بود
صدای انفجار بندرعباس همین الان دوبار صدا اومد
صدای نسبتا شدید و خطرناک
وحید ساعت ۳:۲۴ بندرعباس صدای دو تا انفجار
بندرعباس ۴ انفجار
قشم ساعت ۳:۲۳ بامداد ۲۰ خرداد
در محدوده طولا یه لرزش نسبتا شدید احساس شد ولی صدای انفجار خاصی نیومد، شاید زلزله شاید هم انفجارات حمله‌های اخیر بوده که لرزشش رو حس کردیم، خونه کامل لرزید
سلام وحید جان همین حالا قشم ۲ تا صدای انفجار اومد ، دومی نزدیکتر یا شدید تر بود
بندر دوتا انفجار خیلی شدید پشت سرهم اومد سمت پارک جنگلی
ساعت ۳:۲۳ بامداد بندرعباس یه چیزی منفجر شد
سلام سمت پایگاه هوایی بندرعباس رو میزنن
#قشم
، 03:23، 20 خرداد صدای بلند انفجار شنیده شد. (شاید صدای انفجار بندرعباس بوده)
سلام بندعباس صدای انفجار الان چهارشنبه ۳:۲۴
نزديك  پایگاه هوایی بندرعباس خونه ماست به فاصله پنج دقیقه چهار انفجار بزرگ صدا اومد
اقا وحید بندر خیلی صدا  انفجار میاد
سلام وحید جان بندرعباس 3:24 دوبار زدن صدای خیلی زیادی اومد همراه با لرزش
وحید جان درود
ساعت 3:24 دقیقه بامداد چهارشنبه 4 انفجار شدید سمت فرودگاه و پایگاه هوایی بندرعباس
۳:۲۳ دقیقه ۴ ۵ تا پشت هم زدن بندر رو
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76119" target="_blank">📅 03:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFe5x-EmJd2XJTFtDE7wOl9x4tGKr3Q0b9H7_HknsLUXJdy19ynl5sHez_oJq7LiGpHWWpYtOOO5sKuVBYN39YRp5rt-nsADLUnuIiHK5SA3RbR93fcZTJB7RgT9vQbVLDIepGEWsY0H23hrLwl5Q4VTO-pOuI7haP92isJDzAbIPMtaX9PNDMoK3oyRKntv3vt0zovc_bE-9cHhJ_tGZIaBMsfiY_U4wWQqkTBOGhKeruRri1NcVPBAxCIlVhUcpLP6qLf53O3wFwYPKgptAw-m9d4YtPirISkJT4PtadrZik-UFxsIDYykOTEGN-3gkO90FWGrNzEepWdxrpqKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر به نقل از منابع محلی و ساکنان روستاهای اطراف، از شنیده شدن مجدد صدای چندین انفجار در محدوده شهرستان جاسک خبر داد. پیش‌تر حملات نظامی به بندر جاسک و کوه مبارک توسط منابع آگاه تایید شده بود و این حادثه، دومین موج از صداهای انفجار در این منطقه از آغازین ساعات بامداد چهارشنبه به شمار می‌رود.
@
VahidOOnLine
من هم حدود ساعت ۲:۳۰ چند پیام از جاسک دریافت کرده بودم.
خبرنگار آکسیوس هم به نقل از مقام آمریکایی گفته یک موج حمله دیگه انجام شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76118" target="_blank">📅 03:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">موج حملات آمریکا «فروکش کرده است»
رسانه‌های ایران از «فروکش کردن» موج حملات آمریکا خبر دادند که می‌تواند نشانه‌ای از «مقطعی و محدود» بودن این حملات، تلقی شود. چنانچه سنتکام آنها را «متناسب» خوانده بود.
خبرگزاری تسنیم  همچنین تصاویری ویدیویی منتشر کرده و مدعی شده که یک پهپاد شاهد ایران در آسمان عراق مشاهده شده و آژیرهای خطر در کویت و بحرین که میزبان پایگاه‌های نظامی آمریکا هستند به صدا در آمده است
اما هنوز جزییات رسمی در این باره از سوی رسانه‌های بین‌المللی مخابره نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76117" target="_blank">📅 02:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرنگار صدا و سیما در سیریک: در پی حمله امشب آمریکا به سیریک، ۲ مخزن آب بخش بمانی مورد اصابت قرار گرفته و آب آشامیدنی این بخش قطع شده است.
"خبرگزاری صداوسیما" در خبر دیگری نوشته: هیچ بندر تجاری در جزیره قشم هدف قرار نگرفته است. در پی شنیده شدن ۶ انفجار در قشم برخی کانال های خبری از حمله به یک بندر تجاری در قشم خبر داده بودند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76116" target="_blank">📅 02:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pRWuNAVrFTT1EkX0HmFa1pe5JmJA4MIuj_mmdjCmzi5YCx2-adt6RWzICVZRE8_dhKkWrtKwyVYJTiLbiY25IOJnoC3IBJ-Q72mteM4e36KX0F2kLBxQrVsUOD_WjvzgJ0uMJt4X92xMmq0VQg2-k1owKXVAEJYC3QVdOxcPGmmKaFVvPvakoHSWeW_psWSoQKM9kNv1jVAxLSVPzzVI-i98-6wL00uXgz__7jx-zFnmP_3qhRfRWAZOS3UDle2B9weGVY8dC5AlbQ5fp8wpbUjIxtZg1dktNVgoXXJI8mQ64Y01vi4YpFsihXNwqEZr8DpmxJJkdnKefFVT17RKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت تازه عباس عراقچی، ترجمه ماشین:
با وجود شکست‌هایش در میدان نبرد، ایالات متحده تصمیم گرفت عزم ما را بیازماید.
نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نخواهند گذاشت.
اگر می‌خواهید در امان باشید، منطقه ما را ترک کنید.
تاریخ خلیج فارس فصل‌های بسیاری درباره سرنوشت‌های شومِ بیگانگانِ مداخله‌گر دارد.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76115" target="_blank">📅 02:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UPoC4v5gtsvPI8L0aAtZm_udazo9qeEiPiGq6Kz49VU7tvVqvIapGj_l_fzPQkQIok5LlqUY3kh1JmIQeOgxFCs2ABbmssceuuspKXZUyXK_E9RCc_yIS2_50e0jMRmmUpZ2LdtXVSjSrPTgd5gBSb9wy5DsLGk0zkXgWHSjmAL1oqD0ZvASHrKLwVlz0AfmEseFeJAvW7Pr0Y6Zp6ixbCJbeNjLKAkooW52Ttmc0VBomxoJ7O9yaOz_Ed2AThyQELWxewKO0-kcZEj4-NtWqm_YWIswrUQAAnfYNXGDmyM-Wpw0oVrekfs1Y5tRxtSCHJ6EQBjek_6s9-YnINZtWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان گفت که حملات جدید سنتکام با قصد هشدار دادن به جمهوری اسلامی است.
او گفت ایالات متحده معتقد است که این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76114" target="_blank">📅 01:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76113">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41278e3d2c.mp4?token=QwcGcfOxAFd6jssf6r4TCTp9p_3tCD-Rp7R81_3AfFg6JBdnTc_igcm6AE_pHzbKyJHXoFub1wUTA95NBTHH-MnCBPDfUM0JkQ5Lx1ptmZbLmqyAZhvdPVOO_GyQmdX4EO1YBIiK1WXM1DJgXyGJagoPO9iVRHbnCvVAcSaTDGBw8rsNYZoeay4dWmMfYbc0JSnz4Zh__F9OKlatJGw-yE2-o8IbnMY9xLLpcrk8fp8qdMDuxpuiyNB6BWQfLEJl59cZg7XgSBNlFOGC3fcIRkqgstZZNUaL8sXf5t9ig5KVKeWuGPnJM8VDfVtHZazDyy3KLhc6CDpumrPFKgek6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41278e3d2c.mp4?token=QwcGcfOxAFd6jssf6r4TCTp9p_3tCD-Rp7R81_3AfFg6JBdnTc_igcm6AE_pHzbKyJHXoFub1wUTA95NBTHH-MnCBPDfUM0JkQ5Lx1ptmZbLmqyAZhvdPVOO_GyQmdX4EO1YBIiK1WXM1DJgXyGJagoPO9iVRHbnCvVAcSaTDGBw8rsNYZoeay4dWmMfYbc0JSnz4Zh__F9OKlatJGw-yE2-o8IbnMY9xLLpcrk8fp8qdMDuxpuiyNB6BWQfLEJl59cZg7XgSBNlFOGC3fcIRkqgstZZNUaL8sXf5t9ig5KVKeWuGPnJM8VDfVtHZazDyy3KLhc6CDpumrPFKgek6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام آمریکایی گزارش داد که حملات آمریکا به جمهوری اسلامی ادامه دارد و اهداف شامل سامانه‌های پدافند هوایی و رادار است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76113" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76112">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rG3qgzCWFlu5QswLm53QCnVAjcMgAQRuxXKY27QdS3mgpBhuu7l40GbZPs3cs0lGtUAOHDaamkNQgtsRmTG32OxK1zvZHqMc_Vbg3mIWT-iQgmgFIaxICHYWgT9Mn8c9IaqCUM2gXMW2DPFz3e_mdclNwasSGQaeTmh8arT42b5Z8IMAoeqatbWDzHFR-chlYwBEqPJ20H9FaYPB8xwQEGyYuBG9r_drCuVJYzZCzBsAVr7H2D2lV4GpfU0RqWNat-rgu-M9DWEC5krLMKRxIX3B2QK8EssKsRJkcxiudG-nwuLY1n8flzNPn_3y2xsM3DJnsY2wAOhOaMRS8Mmy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، سه‌شنبه‌شب، در گفتگو با شبکه خبری «ای‌بی‌سی» (ABC) درباره آغاز عملیات نظامی واشنگتن علیه ایران گفت: «من فکر می‌کنم پاسخ دادن امر بسیار مهمی است. آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین حالا که صحبت می‌کنیم، در حال پاسخ دادن به آن‌ها هستیم.»
ترامپ با تاکید بر موضع قاطع خود افزود: «این اقدام پاسخی به کاری است که آن‌ها شب گذشته با هلیکوپتر ما انجام دادند و من معتقدم این واکنش باید بسیار قوی و قدرتمند باشد و حملات جاری نیز دقیقا همین‌گونه است.»
@
VahidOOnLine
"خبرگزاری صدا و سیما":
سیریک اصابت یک پرتابه تایید شده اما مکان و نحوه اصابت مشخص نشده است
برخی منابع از شنیده شدن صدای انفجار و فعالیت پدافند در بندرعباس، قشم و سیریک خبر می دهند.
"به گفته یک منبع آگاه ۶ صدای انفجار در قشم شنیده شده که بر اثر پرتابه های دشمن بوده است.
ظاهراً این پرتابه ها از جنگنده شیلک شده است."
من از جاسک هم چندین پیام داشتم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76112" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76111">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kdyUMEfOwvYGp7tk_lGicrAzElj97o1A1e3ZVRlIaV5pB5Xm2gOZrOZVQ3NXZREud5Nr7raFB8lyNK_NhxKWrQoo46qKbAB9gzwyANSE6sxF_GvhlNlWucWREm4TwkiI0y9DfqP1yeXEDvVioeAvHif8NNIqSzZI4iqal8hZuEHfM8QYY9BXh8YrslyovGhqU-1UEUC_lkOBIIxa_wXI_HCniMnq5OnZHhyShLTG7Agjb3S4gXc2W9MnpxJTjDUMpwwhaYM6RZFT1753yMuSeUazHkPeES91L8By2W_pta0OeZw8mK8en9NpX6weGOrEI6WoWKCvmU1zOvioJWTvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
سنتکام: حملات در پاسخ به سرنگونی بالگرد آغاز شد
ترجمه ماشین:
فرماندهی مرکزی ایالات متحده آمریکا، سنتکام، اعلام کرد نیروهایش امروز ساعت ۵ عصر به وقت شرق آمریکا، به دستور فرمانده کل قوا، حملات دفاع از خود علیه ایران را آغاز کردند. این اقدام در پاسخ به سرنگونی هلیکوپتر آپاچی ارتش آمریکا در روز گذشته انجام شده است. این مأموریت پاسخی متناسب به تجاوز بی‌دلیل ایران است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76111" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76110">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیام‌های دریافتی از ساعت ۰۰:۳۰
صدای چندتا انفجار بزرگ پشت سرهم شهرستان سیریک
وحید جون سیریک صدای  انفجار اومد
وحید بندرعباس صدای انفجار میاد
چهارتا انفجار سیریک هرمزگان سه تای آخری کناره های ساحل
وحید بندرعباس صدای انفجار اومد الان
صدای سه تا انفجار شدید از سیریک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76110" target="_blank">📅 00:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76109">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H-yYX__vzdydJZT5kmagT8a_UXbTN6qDKQKvY3YzDC1E6_PpuQanQ8DH2fCDBN1uv0d08d8gIHC_NtcZWgyugX6RxMw2QAOcAQElDn67xzyqdzM8iiWS5LtehugUu2zrdavJCOzWIJ8fjplvAFLf2fvEOyk2Y0aqF3ww4OELr7N_kb45BpwtnvKai52H0BbscazrpkNB-iKQ5dasgNiCzLlTTaHMdc50byWC_ztQGd3AxgJfSgihnJAHysKuYqP_otpfmwdHfCH6D98YyQZImc6C4ziQDgmUYSW7txXOYAr_jmWqydh0ltfZ2CyRE6FqLDRLEfBflr9X-yQ_T5xhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نظامی نوشت: «در ۲۴ ساعت گذشته هیچ عملیات نظامی هجومی هوایی در تنگه هرمز انجام نشده است».
@
VahidOOnLine
پیش‌تر خبری بدون ذکر نام پخش شده بود که:
معاون وزیر خارجه جمهوری اسلامی ایران، روز سه‌شنبه، ۱۹ خردادماه، در گفتگو با «الجزیره» اعلام کرد که هلیکوپتر آپاچی ارتش ایالات متحده که روز گذشته در تنگه هرمز سقوط کرد، به طور عمدی توسط ایران هدف قرار نگرفته است.
این مقام رسمی با تاکید بر اینکه ایران پشت این حمله نبوده، در عین حال هشدار داد که به دلیل شرایط به شدت ملتهب و متشنج منطقه، ممکن است بروز چنین حوادثی در این فضا «عمدی» تلقی و تعبیر شود.
همزمان، دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگوی تلفنی روز سه‌شنبه با روزنامه «وال‌استریت ژورنال» با کوچک جلوه دادن حادثه سقوط هلیکوپتر آپاچی گفت این اتفاق «مسئله چندان مهمی نبود» و تأکید کرد که «حال خلبان خوب است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76109" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CieBN6yqndkAYqzsvclJ2vdaM5qI56jZkCnbolujLLmye6JARZg1tn4OUAYLA5Hg8UdpPBr-HA2liDEtvGP6oEl_Gaz8bzdsN8R9WMfx6_Qbv5lJ4hvYF7sJg9q3_SG54khrVM5amALKd3F0hzRbqqlXBAfCmRxvqxogBgX2cebwd8hi7WbaWQTG9Tann3Gr6TeQ_4OrWe7L6kFrhkrYjVjuAyPqqtoydpF2_0xxJaEm6e8EXAEMLgzLlRmOmhJc6p_3lYj-ImtkakQ3sKVAM925L_33-nwHTEr8ijom-LbqAsnGYGf8fjJ-RX9E-890uirj-qtUfONp_s_1R6rnEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uRXLu5WlWgNbiyQzU8P6JWIhdn2ZUkVt-gOluxLkgQJclisHfGUr1RHwPWuIcRumY4G-J9Q6JJv0bIBdGFkx5s1mYjrpb4XmyGf95ftWiEKtvvta57lR9DaiIJwEtMf2DJvljj-TH55n360JfaUuyCA64dJVCwfCpCUVXK_3WlvCQt6oUr_Lk8xSydYxDicIG9ILs_FmvemmX1FM6BMYezgquS8hysw2NWLvcuYJv8LU7H6YPWt8mdCygVSszXIt9q3V-irAHioqx27he1a1_W7fJ1zbRRPthkp0UbGQ7djeBHPO_u8xoAneYzeca6BjieNS8KLdMJd4r-RVE6bbzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگوی تلفنی روز سه‌شنبه با روزنامه «وال‌استریت ژورنال» با اشاره به اثرات شدید تحریم‌ها اعلام کرد که محاصره دریایی بنادر ایران باعث شده این کشور «بسیار فقیر» شود و واشنگتن این محاصره را تا هر زمان که لازم باشد حفظ خواهد کرد.
ترامپ همچنین با کوچک جلوه دادن حادثه سقوط اخیر هلیکوپتر آپاچی آمریکا گفت این اتفاق «مسئله چندان مهمی نبود» و تأکید کرد که «حال خلبان خوب است».
بر اساس گزارش سنتکام، سرنشینان این آپاچی پیش از نجات، دو ساعت را در تاریکی شب روی آب سپری کردند و یک مقام ارشد آمریکایی فرار آن‌ها از این سانحه را معجزه‌ای همچون «دست خدا» توصیف کرده است.
@
VahidOOnLine
وال‌استریت ژورنال نوشت که حادثه سرنگونی بالگرد آپاچی در تنگه هرمز برای ترامپ «کم اهمیت» بوده است.
این در حالی است که پیش‌تر ترامپ در تروث سوشال تاکید کرد که «ایالات متحده ناگزیر باید به این حمله پاسخ دهد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76107" target="_blank">📅 00:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZSYR3JCuVz55xWAvonioOiULF25I6fEFO-ePU30TewFl-qyj6qzXhN0VC_M1WT5yye_hFrZxlsWGMJGk151prR6R6dh7A0sXQ23kkU8-rEGXMKBLFoejprOtBaZNaPz0inti9BBUz1xotpRd6M2O87xogF6pzZCsuFWI4rVrCCYdwo1jN1sXyCWk3OVp_8rLxJ6tDRXtF_NuSarPur6A1_w-u2Y46nPxMEer7uGdC2mW6e7cmNr7d2HgmBid3meWinCdQ_y8DZmq8tztvqXirV5Yv6ntg8e3tIhjdcFf13cxZD7isH5AuOk_2mFNf5BVXSuH-t1gMUCChttOQ6gEfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عراقچی، ترجمه ماشین:
نیروهای خارجی در نزدیکی قلمرو ما همواره در معرض خطرند؛ چه به‌دلیل خطاهای انسانی خودشان، چه حوادث ساده، و چه احتمال گرفتار شدن در آتش متقابل.
برای کاهش خطر، بهترین راه‌حل این است که آنجا را ترک کنند.
ما زبان دیپلماسی را ترجیح می‌دهیم، اما زبان‌های دیگری را هم بلدیم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76106" target="_blank">📅 22:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/teXq_6Y4fHAhWLRT-OmSC_LXyeuo5YJYV0B53XFVqYXosNceBDj_Jo2Ry-Gnm54As1RH_zkFb543nBK61DRBYd-xNW7nru80vgI556_hGehcy7FcpTunrwyId4N9CTKLET_9Rs7PpHf9ElCQoG5DUNRyS5G0hYX6Mql-Td32okQGTUnLeVUj-YOQo23afv61iVegtqP15PkSIyko8KKht3ZCZ1quW3Snuto1wU7kt8FgX69zqBI9jMmRBfWYGQ5_zttRdtKLQ0nGjP72DihcWwjCGzhaAr6eSw1MH2oJGiECvR-MoDQ3sh4pM6DL9XG_XKaOkrIkeVPNrW_zfQ7bYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری سی‌ان‌ان به نقل از دو مقام آمریکایی گزارش داد که هلی‌کوپتر نیروی زمینی ارتش این کشور که در سواحل عمان سقوط کرد، توسط یک پهپاد ایرانی سرنگون شده است.
یک منبع آگاه دیگر  تایید کرد که یک پهپاد از نوع «شاهد» به این هلی‌کوپتر آمریکایی برخورد کرده است.
یک مقام آمریکایی به اکسیوس گفت تحقیقات هنوز مشخص نکرده که آیا این برخورد عمدی بوده است یا نه.
😱
‍
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76105" target="_blank">📅 21:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/quILFFB54z-SO44ADm6YjYO8_hYMZD227QAZNQudWvt18A7VXZ8GJWbg5QI4kgx0bU4pFnwsG5rvZHkBsHDBMYF34TwWegxiHFn8z-yiqDorzRo9BCxmjfrEhY03jAerb3eBK1iu7gsvPp8cwDORSfwv4GcIvZaiMH7SYQ2CApY1fGmadxJcQUA9Jcp-TAA_Exk4rWTZ2lJqAzVtL1YZlmTs-op07Ntr-Juz8UOpEEJG0D8A1eFcddzDrd7lrw2VUZirBRBMUv6RxGZYUWqnf-nRCN3HJm9hFdDRhxxT7osk61uTrl8g6DbiCPofOT_nN7SsMh7bGaQ2U8V1ycIwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
ما زبان دیپلماسی را ترجیح می‌دهیم، اما به زبان‌های دیگری بسیار روان‌تر سخن می‌گوییم. تعهداتتان را زیر پا بگذارید، آن‌وقت ما به زبانی روی می‌آوریم که در آن بهترینیم.
خودتان بر اسبی سوار می‌شوید که زین کرده‌اید!
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76103" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mU3zqfmn8ubZoSmVvbcffCJZe53H457_fVlqo1tBZG3YMdDyKIxG8ViKr_alP5quI-LQqNqfaVozWNapfe9pzK2Dh0Nq8usJRBxPeNjQksd7BGtCO3b2btfG8oC8ROkuyobUj9oXww8AfjSP5hALupcb3V0yqYaPUOYK8A11KSomAVfrn60ax0fUQgN3M132vXWncuHSfK3Je7vY9VKFRW2qDCdykzoR0bMqdHIn-GJzSHHwxbSID8Z7BBa4uby72_mbZ9wbruAjiM2d1XzCvGtSbOrO6h1KdHO4b0L1Sn7HPIoYrQ9Mh6FYf-Y2jbLOC3YkDSlu9SU-BR7u2uXh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: ایرانی‌ها بالگرد پیشرفته ما را سرنگون کردند، ناچاریم پاسخ بدهیم
ترجمه ماشین:
به‌تازگی از سوی ارتش بزرگمان به من اطلاع داده شد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی بسیار پیشرفته ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کرده‌اند. دو خلبان در این حادثه حضور داشتند که هر دو سالم و بدون آسیب هستند. با این حال، ایالات متحده ناگزیر است به این حمله پاسخ دهد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76102" target="_blank">📅 20:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76100">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YTZx7rxQ9TOPwC-DBAYDw9TzDHgYndMZikZH28a11i2YDKpKFdMkyfBMWOrOMsAM4XL1MjzmaasqvKf_93QVOssvR0hkxYsOUA3SwNdpGa17_dNi642_Vg3FqI5iF9_qxgQKtBJq_MfCw852rvOEqi-ZpoRWCeoPIy1JOxGb-sKEpEnBYnyO7seIqf1a16sXehqA9PopDxAcPVHrhIvEuSRklF4sDO3O6UQGSXuyLQAkhsLTuwgt0yzTTXePpzZVn3YH5TyGwZzfCGOpQpW9PLAX4sm114uLnR6qlF8S_zJ95anl30vjnH380JitLtPfvWv3NU__2HX4kABxrzXgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f396691769.mp4?token=dbcNU7WnwgRiiLc2glrwzHbTV8Vml7pEWdbqshG0RMeVgtYTpsuoIs-LIhULOU-qvUfOo2-jo531eTsRwhowKDdram6L2F_TvH7vLUxMzZF2chrcfha4bHeAnI1h_Mt8YuCaCKFvvCMMpWp6k81uNsdtbU2_K4mEufcXh4UDydZoOh5Vb1DANwRyoxLKr6mXBB5jhDHKJQ9pEYu4As_xA9xj8CskYr6J9Vl11f2n853jmh8yxFCpyD-drL8U_CqtRnRjKU7hQq4sYGlIa3l1hfEFJMjwTagLw5VX1bulUX88ZbhL9MMri_pzbRDWKR-3nfLzNEUxpwtnaSJa7ktc6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f396691769.mp4?token=dbcNU7WnwgRiiLc2glrwzHbTV8Vml7pEWdbqshG0RMeVgtYTpsuoIs-LIhULOU-qvUfOo2-jo531eTsRwhowKDdram6L2F_TvH7vLUxMzZF2chrcfha4bHeAnI1h_Mt8YuCaCKFvvCMMpWp6k81uNsdtbU2_K4mEufcXh4UDydZoOh5Vb1DANwRyoxLKr6mXBB5jhDHKJQ9pEYu4As_xA9xj8CskYr6J9Vl11f2n853jmh8yxFCpyD-drL8U_CqtRnRjKU7hQq4sYGlIa3l1hfEFJMjwTagLw5VX1bulUX88ZbhL9MMri_pzbRDWKR-3nfLzNEUxpwtnaSJa7ktc6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طالبان به تجمع مدافعان حقوق زنان و مخالفان حجاب در غرب افغانستان حمله کرد
AngelaGhayour_
مقام‌های امنیتی افغانستان روز سه‌شنبه ۱۹ خرداد تظاهراتی که در حمایت از حقوق زنان را در ولایت غربی هرات برگزار شده را متفرق کرد.
این اعتراض پس از آن آغاز شد که پلیس امر به معروف طالبان گروهی از زنان را به اتهام نقض قوانین اجباری پوشش بازداشت کرده بود.
به گزارش خبرگزاری رویترز، شاهدان گفتند که در جریان حمله طالبان یک نفر کشته شده، چندین نفر دیگر زخمی شده‌اند و ده‌ها نفر از جمله زنان و دختران بازداشت شده‌اند.
..
به گزارش رویترز، هرات که مدت‌ها به‌عنوان یکی از پویاترین شهرهای اجتماعی و فرهنگی افغانستان شناخته می‌شد، دستخوش تغییرات قابل توجهی شده است.
...
شاهدان گفتند اعتراض‌ها زمانی آغاز شد که مأموران امر به معروف تلاش کردند زنانی را که با الزامات پوشش اجباری مخالفت می‌کردند بازداشت کنند.
برخی از ساکنان گفتند مأموران حتی زنانی را هدف قرار دادند که از پیش نیز پوشش مورد نظر، شامل پوشاندن کامل صورت و بدن، را رعایت کرده بودند.
@
VahidAfLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76100" target="_blank">📅 19:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9jPiEcf2xs8lhgqhi-esePYMa5iOG2rM5YfTk1Yv4fs_wEKnOokpia5YZUZkbaPvYz8VEWGzuMi7G4SWLcJwlHTpEuPH2cM9TpW_WRxpil11mo_elAsaK3_Q5OQfFzS-iAVWb3bG2l9wOdG7GGST4JxgcVWM5jviytWI6DDMkvCmblX561az5mNT3S2hf4d-_eJ2LZfSGwtUw4eWCDZ32pcXsnvNc8IQI_WYkPXYDWBNQ7arzWMR_tEDfhf70sdfximZTrpT5fXmsmLGzZnAVcKDC6k53ccUloaYHvVHyrEJyDvoWGasdzxFnmB7K7a96R3Ff4c2OqM70sSmrGQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا پیغمبری، جوان ۲۶ ساله و از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴، توسط دادگاه انقلاب تهران، بابت اتهام «محاربه» به اعدام محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76099" target="_blank">📅 18:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/677a13e326.mp4?token=EesMGYMTtLjY6-_jTZTNqX7kvisoAWhjScXX47N9RvqoNMMgcaX6GaPgfo42F6mjstw-E7pDuzQeCp-Sl9zs4G8FbkayQGLOwGLEVnf6JS81DyeZtBrd08RzMiRd5s1BDBKCbS7PvIOuDFUN6OaAPBN5EobOGyyEDuOWwzeS0KWeRkzVcxICHJwWKPGoljkeBH7ReprsYj3xLRU_senqTC4lmpH8KjPOlq0EF7qgWB_c-I9WfjuKPk-y8sWz3UzBzGahQtRyklofF3PrYSPPCTI_UqyRBqHoIPw_dOZPq2cJJIg_7xuNgih3kRHdLObx3vMben7pa9D5qTD3BkYTAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/677a13e326.mp4?token=EesMGYMTtLjY6-_jTZTNqX7kvisoAWhjScXX47N9RvqoNMMgcaX6GaPgfo42F6mjstw-E7pDuzQeCp-Sl9zs4G8FbkayQGLOwGLEVnf6JS81DyeZtBrd08RzMiRd5s1BDBKCbS7PvIOuDFUN6OaAPBN5EobOGyyEDuOWwzeS0KWeRkzVcxICHJwWKPGoljkeBH7ReprsYj3xLRU_senqTC4lmpH8KjPOlq0EF7qgWB_c-I9WfjuKPk-y8sWz3UzBzGahQtRyklofF3PrYSPPCTI_UqyRBqHoIPw_dOZPq2cJJIg_7xuNgih3kRHdLObx3vMben7pa9D5qTD3BkYTAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه شب هنگام بازگشت از نیویورک به واشنگتن، در گفتگو با خبرنگاران اعلام کرد که ایالات متحده به دستیابی به یک توافق بسیار خوب، محکم و قدرتمند با جمهوری اسلامی بسیار نزدیک شده است.
ترامپ با رد وجود هرگونه نقطه اختلاف بزرگ در مذاکرات، گفت: «اگر بخواهید حقیقت را بدانید، شانس خوبی داریم و باید بتوانیم ظرف یک ساعت توافق را نهایی کنیم.»
رئیس‌جمهوری آمریکا با ترجیح راهکار دیپلماتیک بر گزینه نظامی هشدار داد که بمباران ایران در مقطع کنونی، به قیمت جان انسان‌های بی‌شمار و بسته‌شدن چندماهه تنگه هرمز تمام خواهد شد و فرصت توافق را کاملا از بین می‌برد.
او با تاکید بر موفقیت راهبرد واشنگتن افزود: «سند امضاشده نهایی، کارسازتر از بمباران خواهد بود. ثابت شده که محاصره دریایی اهرم بسیار قدرتمندی است و بسیار قوی‌تر از بمباران عمل کرده است.» ترامپ در پایان اشاره کرد که ترکیب تهاجم اولیه و محاصره، ضربه سختی به اقتصاد ایران وارد کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76098" target="_blank">📅 17:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZExVfkKfXEncO3eD7YEriiftwBD8mWKJfF_w1tSavvDBU1nTe8m1b8p0iVhov9ey-wIV8OJbsPXRzZUMcOv0ou4pqZd1AXE7YIW_cWT3zPQHT11p1pstw_HEzXZirsHOoj7FSKFVU1zKnguxdUg1ujcjOS1qjxcrWxXRik_5zhdZZUfGNF6BlS5hWGtKFts2Rsa-zJdnUgqgn4sCeAj4wlZ1TZUzLx5Lu8n4ttw91NaodVv_7GyphWzfNjOfNjDUaby1pyB4ju_9yhi0XoDT1RFGsbSQ_J38Ur4ZadT3XtPLPY0f8poftBAok-8Fux2NxtXQcYhAC5Ob2hWIXwZmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو عضو نیروی پدافند هوایی ارتش ایران در حمله دیروز اسرائیل کشته شدند
تاکنون در حملات دوشنبه و سه‌شنبه اسرائیل کشته‌ای گزارش نشده بود و ۱۵ زخمی اعلام شده بود.
ارتش اسرائیل دیروز گفت حمله «همه‌جانبه‌ای» به سامانه‌های پدافندی راهبردی ایران کرده است.
بنابر بیانیه‌ ارتش اسرائیل، در جنگ ۱۲ روزه پدافند ایران ضعیف شد اما بعد «سامانه‌های پدافندی در نقاط مختلف ایران» مستقر شدند تا توانشان را بازسازی کنند که در این حملات این سامانه‌ها منهدم شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76097" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UMsgfLSJgsUVrJ1_hC78eY-FFGyZmQih7MtZ5H6MhbC7sykxy7PoZPqt2oOj-6pqJSdLSk9Q7-COy9FiWvzPqy7aCfqBE-Wb3iFBez6kJMrZB6E7zcFwKiU-6F8caPLwK3CFmshcBmMYRvaxu6UMNznYfNRACJoSeD0ZEONGevJlRfxRvBC7Zzgs_536rMzMW6b-oDprsNg9Dc4c8YLYoPX8J8wPVSttocqA7vEcILh3pTvB2k5WeTzA-8fR57DPAn8MA_KAksjc9Pxbct_pUsgZn1qo4HQyoig22OiI86TB8THgtXPBjTj-ifM1guwwZ0zDK_Nx-_cJQkB1O3Y80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، در بیانیه‌ای اعلام کرد دو خدمه یک فروند بالگرد تهاجمی «ای‌اچ-۶۴ آپاچی» ارتش آمریکا که در نزدیکی سواحل عمان دچار سانحه شده بود، توسط نیروهای آمریکایی نجات یافته‌اند.
بر اساس بیانیه سنتکام، این حادثه ساعت ۷:۳۳ عصر به وقت شرق آمریکا در روز ۱۸ خرداد ۱۴۰۵ رخ داد. این بالگرد در زمان وقوع سانحه در حال گشت‌زنی بر فراز آب‌های منطقه بود.
سنتکام اعلام کرد دو نظامی حاضر در این بالگرد ظرف حدود دو ساعت نجات یافتند و در وضعیت پایدار قرار دارند. این نهاد همچنین افزود که علت وقوع حادثه همچنان تحت بررسی است.
یک مقام آمریکایی به شبکه ای‌بی‌سی گفت دو خلبان این بالگرد پس از سقوط در آب، توسط یک شناور سطحی بدون سرنشین یا پهپاد دریایی از آب گرفته شده و به خشکی منتقل شدند.
به گفته این مقام، پهپاد دریایی مورد استفاده در این عملیات طراحی مشابه یک قایق تندرو داشته است.
@
VahidHeadline
هنوز مشخص نیست که آیا این هلیکوپتر بر اثر آتش نیروهای ایرانی سرنگون شده، دچار نقص فنی شده یا با مشکل دیگری مواجه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76096" target="_blank">📅 17:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OVT0MxqYIke9tkDqU2fU4c0O4syIwn8ikpeJOyDugB3qdKnW5TDQRikxR4zVAeZVfll7yu1M9CuI6Z0DKeAwh4u7fWlroDtoBWmGITNRAep97Ov24FGR3EGoYlJHUij3bntV1GVwF8UPU5r_KXepTSAkuFPvMQtyXC6Apy-Ds9tdyEToSLCVApV0vX4enZRRc2NbiKWA7YgdAkJlfdb_CKc_UH01_s3qQz5FFLiYB2rR9eBtYlVoUNQL5QJWKihowktUOIF8Uzsf7WvbG3I_10-8GrnxXHqOkR3d5Jf30WuKBFrgNflgZkL51pRboDp7KKY5wqZVclOPB4IJFLbX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ang6dwI50MIbjfP3mUY6NF8TZTlBsuvkvkmtfuwCJq6xm5ySgaaTOeommOdcR6r2eQUWsAVrJ-G-0PjZfoAtXyOIOzAT3haocK59kUvt7Jk6ODbxyonS_dXyjdPfqY0DZeZEmfB19_uzh4zAG3Wd3w7Lkmvf1ClwS_JfxZaxOSRHwdvosxwCKjSjP-zo7Z_pNemweuwHjcRh-JSZ9lEi85ZiSrjx775g8C2h7TCGGIL_Ee-FunvQNHXmmemkc-LiCrUnAZDY8To2bTEVqPnSlTD10d045sq1xY19yhIPgKKdROTXf_AZRlN69Zaa7_ifxblB-a586UrMC4bKX9XJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OE8grulbjVgqBf0JSMHPTwAt3YLjdqHivNyLBzehxGtFfrkoHOtvdHxueNL4kEnSKVhms9wjNIAdT40MpuMeg8E996kkC6nc7vA61JPzIN7LpanxXaQIiQpHpx9B6soC1NA9609y-wCEmwTqRH-CZy3OTxYmobRfCX14BjAq67DyrR4nwCRLapcGUikj6G1g3zzZJE9QKKPCmjo276mwJ8YO_S8Iku5qyRIEeJl_VTEvXlVc3Yg3o7NQ88YpQqQZKJwU4x3wq5iJL5h9bhnjnfDuUW0fBabpTwvQjiEY5DoTa2LudNB_M7vz0eavJ-d-mwojVjt9CpX5iWkocUnvxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8642136842.mp4?token=i7w1A2tEw-zKlaOAI44OIVWFEEzD9h8KmdDyUcWw_8BYe39i5fzcoxMbavmN8jwXTDt9bsNrnWJp23tlGU3Wv3wtZ8h8iBCNULTLphsD6TNCHuTLvd3bE44Iep436U9E5zAyjOH5X9X1No_I0IpN1Lu98bBOXs-MFuUmCvC1lGuGq4ZYEpDKH739lGvx3OvFoJjXLFi3C4W6tuGcUehLzgvPgqL-r3wJ9Ex6pkbStAp5P_Y1QhqYTiqyrBV8Cgm7fzuG_cyYMXy5LuO7AkbJA6QbRfUaysX9bDCVg90s_rQ1J-203Fl98Nr6WSRO_E1ZHrmIxlBGAY-RVVSEI3ymAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8642136842.mp4?token=i7w1A2tEw-zKlaOAI44OIVWFEEzD9h8KmdDyUcWw_8BYe39i5fzcoxMbavmN8jwXTDt9bsNrnWJp23tlGU3Wv3wtZ8h8iBCNULTLphsD6TNCHuTLvd3bE44Iep436U9E5zAyjOH5X9X1No_I0IpN1Lu98bBOXs-MFuUmCvC1lGuGq4ZYEpDKH739lGvx3OvFoJjXLFi3C4W6tuGcUehLzgvPgqL-r3wJ9Ex6pkbStAp5P_Y1QhqYTiqyrBV8Cgm7fzuG_cyYMXy5LuO7AkbJA6QbRfUaysX9bDCVg90s_rQ1J-203Fl98Nr6WSRO_E1ZHrmIxlBGAY-RVVSEI3ymAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از برقراری تدریجی دسترسی به اینترنت در ایران، ویدیویی در شبکه‌های اجتماعی منتشر شده است که فرزند جاویدنام نسترن زارع‌منش را در حالی نشان می‌دهد که پشت پیانو نشسته و هم‌زمان با نواختن ملودی، یاد مادرش را گرامی می‌دارد.
نسترن زارع‌منش، ۳۹ ساله و مادر دو فرزند ۱۰ و ۱۵ ساله، ساکن تهران بود که ۱۸ دی ۱۴۰۴ در جریان انقلاب ملی با شلیک گلوله نیروهای سرکوبگر جمهوری اسلامی به سینه و گلو جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76092" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76091">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TH7TQbunFKGv4b5VAgfcc24PbHy5mpnwoGwBbCgnLU4DJ0NjvDrRGRaD1HwjclfEwnuekksEwmJcAhO7wQHjW1fXXlbK_FGCD-fU5G3gzZmCargWioBNuzHSxcgIN0OZk_Pm2-srXIddHlYP9yNbGVCBOZhACEE9l5ikjZvvrupShnEmIVtoVMUQT2OZ74LbEd77udauM6COsUU2i9DWGLFWjaM1qAQsAios42_6yrIL3UHSej0KRhfq1WioUckYo2wEajytCRzBM8R7mRuWsU0g_XbGJ8T75y2AYs3SFi4zYc0P8OPPh0Fokyc3FC-_Vw2fn76S6Sg_mQmzOyaYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون ترامپ، در مصاحبه با فاکس‌نیوز ابراز اطمینان کرد آمریکا و جمهوری اسلامی می‌توانند درباره پرونده هسته‌ای به یک توافق بلندمدت برسند.
او گفت صرف‌نظر از اینکه اسرائیل از این موضوع خوشش بیاید یا نه، چنین توافقی به نفع آمریکا است و واشینگتن به پیگیری آن ادامه می‌دهد.
ونس با اشاره به نگرانی درباره اینکه تهران ممکن است در حال بازی دادن واشینگتن باشد، گفت: یکی از مهم‌ترین عوامل موفقیت این توافق نهایی این نیست که جمهوری اسلامی چه چیزی روی کاغذ می‌نویسد، بلکه این است که آیا واقعا به برخی از الزامات توافقی که به آن می‌رسیم پایبند می‌ماند یا نه.
او با تاکید بر اینکه آمریکا تعهد جمهوری اسلامی به چنین توافقی را در بلندمدت راستی‌آزمایی خواهد کرد، گفت
:
بیایید صادق باشیم. ایرانی‌ها نمی‌خواهند این جنگ ادامه پیدا کند. ادامه جنگ به نفع آن‌ها نیست. آن‌ها پای میز مذاکره آمده‌اند و پیشنهادهای واقعی را مطرح می‌کنند. اگر به این توافق برسیم، یک موفقیت بزرگ برای مردم آمریکا خواهد بود.
@
VahidOOnLine
جی دی ونس در گفتگو با شبکه فاکس نیوز: موضع رییس‌جمهوری کاملا روشن بوده است. اسرائیل اهداف خاص خود را دارد، اما هدف اصلی آمریکا در قبال ایران این است که اطمینان حاصل شود ایران به سلاح هسته‌ای دست پیدا نمی‌کند
جی دی ونس: در ماه‌های گذشته و در واقع طی حدود یک سال و نیم اخیر، شرایطی ایجاد شده که رییس‌جمهوری معتقد است ــ و من هم فکر می‌کنم درست می‌گوید ــ می‌توان به یک راه‌حل بلندمدت برای مسئله هسته‌ای ایران دست یافت
ونس: ممکن است اسرائیل از چنین توافقی خوشش بیاید یا خوشش نیاید، اما ما معتقدیم این مسیر به نفع ایالات متحده آمریکا است.
به همین دلیل به دنبال آن خواهیم رفت، زیرا این همان چیزی است که رییس‌جمهوری آمریکا برای انجام آن انتخاب شده و همان کاری است که برای خدمت به مردم آمریکا باید انجام دهیم
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/76091" target="_blank">📅 06:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76090">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMEj8JduCUavMypsGwZbbAEAq6zbaSojd77zkb54GIruFwmCkNP-8_uxuvNXwEASalbrVC8l-9zypSkbcFlW1WRC-RHaCb97mXyfC7HmDHNhB0jaDiv_TBLsmklTGu_CbRmQJ6aGQlBVaflX5LQv1ftRkwY71ynPc7K3dasbMJAzhBOytkdWWAm8PGdaKj1dKQAXCCzFuDeoYXjP8W69aQbGmRdgwm0Vsmx-bl3cLU95u3JUTb0DVtRnRUJTM7LFnqGLFsxpf6OaCj2V4w54CT8fgzAQd0NV7P7F06DzRfDm3O-T1H3ggHGAeaVEbHAWbPefa-U1XKAG1GTzbatw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه با تاکید بر موضع سرسختانه واشنگتن در قبال برنامه‌های هسته‌ای تهران، با تقدیر از همراهی لیندزی گراهام، سناتور برجسته آمریکایی گفت:
«لیندزی در تمام این مسیر پابه‌پای من جنگیده و ما تیم بسیار سرسختی بوده‌ایم. من فکر می‌کنم در حال پیروز شدن در این نبرد هستیم، اما طی دو هفته آینده با اعلام پیروزی کامل، برنده واقعی آن خواهیم شد. این یک پیروزی کامل خواهد بود که بسیار زود رخ خواهد داد.»
رئیس‌جمهوری آمریکا در ادامه با اشاره به نابودی گسترده زیرساخت‌های نظامی ایران، این وضعیت را مصداق تحقق «صلح از طریق اقتدار» دانست و خاطرنشان کرد:
«ما در حال حاضر مشغول مذاکره هستیم و آن‌ها به شدت می‌خواهند یک توافق بسیار خوب انجام دهند. آن‌ها اکنون حاضرند همه‌چیز را به ما واگذار کنند و توافق کنند که ایران هیچ سلاح هسته‌ای نداشته باشد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76090" target="_blank">📅 02:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPQDAg9sptuetDBei8HTPhCWq_BcqS9gDZvzpfneo1Qr8tDlhqrrYmwfeJQrqEGhc_sz6qiMF0rQ_bdwyhdH-_NhAA4tjjWLnqK9-YMHrCCO94iaZjxNUrbmsvNIf48qqEj93D3PMEPC4fHKr4MsYFIovCe70m3HCg0IlwFWFD3NL8RvvUyayBcIpd1dxew9xYr1P89cQ-FwbUF925kVGFGngOqbsF5guUzmsXkgW7fjavHgovjk2xvCVw98KreOvP_6naIY02V9L8OxWub96bDvNAw55xmMErb45-njIPzxKqxmrzgyWeeCEcTwoIWH1-pGSzJuXqwgovVxY-01fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران در اظهاراتی جدید به حمله موشکی شب گذشته از خاک یمن به سوی اسرائیل واکنش نشان داده و آن را نشانه‌ای آنچه «هوشمندی جبهه مقاومت» خوانده، دانسته است.
آقای قاآنی روز دوشنبه گفت: «اقدام به موقع و با اقتدار یمن قهرمان نشان از هوشمندی جبهه مقاومت دارد اگر لازم شد دیگران نیز می‌آیند. شرارت‌های رژیم صهیونی و آمریکا در این منطقه عکس‌العمل جبهه متحد مقاومت را در پی خواهد داشت. رزمندگان بدون مرز مشرف برگلوگاههای عبور شما هستند به تعرض ادامه دهید گلوی شما را خواهند گرفت.»
یکشنبه شب ارتش اسرائیل اعلام کرد که پرتاب یک موشک از خاک یمن به سوی اسرائیل را رصد کرده و کمی بعد از رهگیری آن خبر داد.
کمی بعد حوثی‌های یمن حمله به اسرائیل را تایید کردند و گفتند که «منطقه اشغالی یافا» را هدف قرار داده‌اند.
حوثی‌ها همچنین در بیانیه‌ای «ممنوعیت کامل و مطلق» تردد دریایی اسرائیل در دریای سرخ را اعلام کردند:
«ما در قبال محاصره ناعادلانه تحمیل‌شده بر مردم خود و مردم محور جهاد و مقاومت در فلسطین، غزه، ایران، لبنان و عراق ساکت نخواهیم نشست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76089" target="_blank">📅 02:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76088">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a40e8ba.mp4?token=VKF8p-feJeujdZNRVMMP3js-M2TyzN4MNeDIk0uACE5kqwZxiYbMB22935N5zLr-0QAnwK6E9kcEpgvdwhJnjw3ikdp7IkGgB6Tjp5NDH074FQ7nE-3A5wHHvsBCPXxa206uvOGnmHEdZ9vapYjhYf9NseIgqiH9M8iSwpQjqt4HXkrP5eg2I0rO1QmYbRfq16Rr_vRSRQJOkU504D-mHMu6-FTqRvLbZ7PeCYF3hZiLiVm2a4MuPm5azUx3cmHBhDNFNq0E9_y2mCrXn0sqB2TeDnlu8XCn5jiQAOhoi5MguKla8dDWcs0_Fbz8BLr_1jk0lJRwh3uPubhRf57Xew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a40e8ba.mp4?token=VKF8p-feJeujdZNRVMMP3js-M2TyzN4MNeDIk0uACE5kqwZxiYbMB22935N5zLr-0QAnwK6E9kcEpgvdwhJnjw3ikdp7IkGgB6Tjp5NDH074FQ7nE-3A5wHHvsBCPXxa206uvOGnmHEdZ9vapYjhYf9NseIgqiH9M8iSwpQjqt4HXkrP5eg2I0rO1QmYbRfq16Rr_vRSRQJOkU504D-mHMu6-FTqRvLbZ7PeCYF3hZiLiVm2a4MuPm5azUx3cmHBhDNFNq0E9_y2mCrXn0sqB2TeDnlu8XCn5jiQAOhoi5MguKla8dDWcs0_Fbz8BLr_1jk0lJRwh3uPubhRf57Xew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسی حکومتی در صداوسیمای جمهوری اسلامی مدعی شد آمریکا در جنگ ۴۰روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته است.
او گفت: «برای ما کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها هیچ کاری ندارد» و افزود جمهوری اسلامی به درخواست «عالمانه و عاجزانه» کشورهای منطقه خویشتن‌داری کرده است.
پیش‌تر، دونالد ترامپ، ریس‌جمهوری آمریکا، چهارم خرداد در مراسم «روز یادبود»، یاد ۱۳ نظامی آمریکایی کشته‌شده در جریان جنگ ایران را گرامی داشت و گفت آن‌ها جان خود را فدا کردند تا اطمینان حاصل شود که ایران «هرگز به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
"روایت فتح"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/76088" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76087">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زمین‌لرزه در هرمزگان
پیام‌های دریافتی:
سلام وحید جان
زلزله همین الان بندر عباس ساعت ۱۲:۴۰
آقا وحید بندرعباس همین الان زلزله اومد
قشنگ زمین لرزید
00.39 بندرعباس زلزله شد
زمین لرزه نسبتا شدید ساعت ٣٩ دقیقه بامداد بندرعباس
داداش همین الان بندرعباس زلزله‌ اومد
🔄
آپدیت:
‌
خبرگزاری فارس: زلزله‌ای به بزرگی ۵ و در عمق ۲۲ کیلومتری زمین، منطقۀ سرگزی احمدی در شمال هرمزگان را لرزاند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76087" target="_blank">📅 00:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76086">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7QAvnz1K8pqrgEVv8gtDxPjTI69OyEqN4LxATLwuQlcSBxupoisA8LRn5-v6a0LF3BNk91OlIg9Etuf1rYrcEdo1k30V8kJ9ZmjaQgcGh4nrfJQ3dWhCHOFtzJL5hPHB6eVhZT_cB_jRHFyylfVJiRY9hkqGg_jRu94ocfj3edpbhdUWiB-srrCysPtPd9PkbO8Tzt6kW570cIPhObWQ1qKTQmyQC14phcxjLwmltBx-vspGQtGTKh7YsppLGLcqXIMHMTFJW52XiJ7ZznlRKnh63318xJ-zT8Kw3XU9DlGgnZYTP-6tXmSEMhc5jyay9MXaDBJ3JLjyGULNsmkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سارا اسمیت، سردبیر بخش آمریکای شمالی بی‌بی‌سی، در یک تماس تلفنی کوتاه با دونالد ترامپ درباره گفت و گوی تلفنی روز گذشته او با بنیامین نتانیاهو، نخست وزیر اسرائیل، پرسید.
وقتی از آقای ترامپ سؤال شد که آیا نتانیاهو با حمله موشکی به ایران در روز یکشنبه از درخواست او سرپیچی کرده است، رئیس‌جمهور آمریکا این موضوع را رد کرد و گفت: «نه، نه. موشک‌ها از قبل شلیک شده بودند. آن‌ها از قبل در راه بودند.»
او سپس افزود: «اگر به او بگویم کاری انجام دهد، انجام می‌دهد.»
این تماس کمتر از یک دقیقه طول کشید.
در بخش دیگری، سارا اسمیت از آقای ترامپ پرسید که برای متوقف کردن حملات اسرائیل به ایران به نتانیاهو چه گفته است.
«تنها چیزی که گفتم این بود که باید از عقل و منطق استفاده کنیم. ما به امضای یک توافق بسیار قدرتمند و بسیار خوب نزدیک هستیم. بدون سلاح هسته‌ای، بدون هیچ چیز دیگر.»
او ادامه داد: «می‌دانید، باید از مقدار زیادی عقل سلیم استفاده کنیم. همه چیز خوب بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76086" target="_blank">📅 00:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
وحید جان گیشا یه جارو زدن یه انفجار وحشتناک بود
[از روی صدای یک انفجار چطور میشه تشخیص داد که دلیلش حمله بوده یا چی؟]
وحید جان ۱۲ و ۱ دقیقه صدای انفجار خیلی خیلیییی بزرگ
گیشا
سلام از گیشا
یه صدای خیلی بلند انفجار اومد
همین ده دقیقه پیش
همه ی همسایه ها اومدن دم پنجره
نمی‌دونم چی بود خیلی عجیب بود
همه جا لرزید
📡
@VahidOnline
۲۰ دقیقه صبر کردم ولی پیام‌های زیادی دریافت نکردم.
آپدیت:
ما وسط گیشاییم و خونه هم ساکته، کوچیکترین صدایی نیومده
وحید جان راست میگن دقیقا ۱۲ و یک دقیقه در گیشا صدای انفجار بزرگ اومد،اما فقط یکی و واقعا نمیدونم چی بود، ضمنا برخورد به زمین و یا عمیق نبود.
من گیشا زندگی میکنم ، با اینکه امروز ظهر هم گفتند یک جا یک جای گیشا را زدند متوجه نشدم
حتی الان هم که پیام گذاشتی داشتم می‌خوندم اما متوجه انفجاری نشدم
من گیشا هستم چیزی نشنیدم
آپدیت:
بعدش کلی پیام دیگر هم در تایید و تکذیب شنیده شدن صدا دریافت کردم ولی چون بعد از انتشار پست بودند نمیشه خیلی روشون حساب کرد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76085" target="_blank">📅 00:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsyO3P6o2VNozJP0xfUHFcLZfNf9wqJR8KDqyyXBG9Xzcl_cPaXx6Vk2u-eN-VYUTnai0csUq5G4S-leZV2K1Fp4VrAsCTbuppTAJiStWfYODTo2yyZ4gPw43vc2qXyUuOSH1ArJlvjQNtXIOU8WRfAwKlyAqvzrE0iZAI6p_vd9fBQlEANQW7yDLHMhEXbOIcvAUl1A1AenC3X7YnN2ANYekfQqnKSbK2Mm8DpzQdwXEjQy1V9-ltXxwTsjibdbpwyM182j2pLO7GWq7i0f2XR1bP_k7WCxRlB8IWqnz8G_6vPKNvcNqcUs8wiry0z43iTTq9AoUYn0qcCfo1CVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبری سی‌بی‌اس، روز دوشنبه ۱۸ خرداد ماه گزارش داد، دولت دونالد ترامپ قصد دارد روند لغو تابعیت ۱۷ شهروند آمریکایی را که به تقلب در پرونده‌های مهاجرتی یا برخی جرایم متهم هستند، آغاز کند.
بر اساس این گزارش، وزارت دادگستری آمریکا این افراد را به پنهان کردن اطلاعات مهم، ارائه اطلاعات نادرست در روند دریافت تابعیت یا ارتکاب جرایم مختلف متهم کرده است.
سی‌بی‌اس نوشت این اقدام بخشی از کارزار گسترده دولت ترامپ برای استفاده از سازوکار قانونی سلب تابعیت از افرادی است که به گفته مقام‌های آمریکایی، شهروندی این کشور را از طریق تقلب یا پنهان‌کاری به دست آورده‌اند.
در میان افرادی که هدف این اقدام قرار گرفته‌اند، نام چند نفر که به جرایمی از جمله سوءاستفاده جنسی از کودکان، کلاهبرداری مالی، پولشویی، تقلب مهاجرتی و استفاده از هویت‌های جعلی متهم یا محکوم شده‌اند، دیده می‌شود.
تاد بلانش، معاون دادستان کل آمریکا، گفت دولت در برابر سوءاستفاده از روند دریافت تابعیت «هیچ‌گونه مدارا» نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76084" target="_blank">📅 23:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76083">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htz2Q3Wl8pE-Wlk4-3xHsAfdTfYocawhHOe_1MOMcFtD_rTsuArba0cRQfxdLDhM3ZQh4bokb6s8vhCiz5T-i-rs9PoLxC7g0JR6O4V2UvpTY13T77qV7aumorBG29iwZpynpztw-shNVXc9fMBNcnS25WcuZDo8B_xhsMSmttVREbEEK8Jv__7WiMrMMjjMp_ku2qxCJzmHVsopUV6WTKcmQwZCtdh5wl7VbQhBSFsB7A9V9BUT2im7qUD6lDrpt65ybUVUmrOshgTXXWynkeyhZj_RdHBaEZ4GORfPn4q5waN_mQ26E9Sg1PRvlmY6QoASJofLYXTikwelW_nLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری سی‌ان‌ان، شامگاه دوشنبه ۱۸ خرداد ماه، به نقل از یک منبع اسرائیلی و یک مقام آمریکایی آگاه گزارش کرد اسرائیل در حال آماده شدن برای حمله‌ای گسترده به تهران بود، اما دونالد ترامپ، رئیس‌جمهوری آمریکا، در تماس تلفنی با بنیامین نتانیاهو از او خواست از انجام حملات تلافی‌جویانه بیشتر خودداری کند.
به گفته منبع اسرائیلی، ترامپ در این تماس از نتانیاهو خواست دامنه واکنش اسرائیل را محدود کند تا از تشدید تنش‌ها جلوگیری شود.
بر اساس این گزارش، نتانیاهو در نخستین تماس که شامگاه یکشنبه به وقت آمریکا انجام شد، در برابر درخواست ترامپ مقاومت کرد و اصرار داشت اسرائیل باید به حملات ایران پاسخ دهد.
با وجود اخطار ترامپ در گفتگوی یکشنبه شب، ارتش اسرائیل برخی اهداف را در ایران، از جمله یک مجتمع مهم پتروشیمی، هدف قرار داد.
این شبکه همچنین نوشت لحن گفتگوهای اخیر ترامپ و نتانیاهو به اندازه تماس‌های هفته گذشته تند نبوده است. به گزارش سی‌ان‌ان، در تماس‌های هفته گذشته تنش میان دو طرف به حدی رسیده بود که ترامپ با الفاظ تندی با نخست‌وزیر اسرائیل صحبت کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76083" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPM4x9wc5KPrnO7KcAB_QJb7I2HLIVaoNmatdxWa3bmRYpxhO1Oiz4qzexd5e3f72xTY7h0dwxJK6bKCuGYl9gqTBxbgwIQaLhR3D__Abtd7sMEDzuS90YmJlVN-SxAdX342v1sdfumXO_phY1cGti5OYQAuNoS8bC8izSVMKpC39Ny2rtVuWaZX3osUSWb7FaWf41JQmDF44ROKT2e7Az5dQ7Y33I9wraaDhntP3AwtfvgX_8QE-JJUixA5PllVxWiJhsAdrKMYlqchR1RG2ZH3bg653Pd2WzsL5Q0TEMUyNX4B-j4mnxXJrlWPm1Mh0yls2n5K_7dbrYJ9SVm99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان، درباره حملات موشکی اخیر جمهوری اسلامی به اسرائیل نوشت که دشمن در کوتاه‌ترین زمان ممکن ناچار به التماس مجدد برای پذیرش توقف آتش از سوی تهران شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76082" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g7mebF_YXG6zeSr8KRb5sZhHDhZT3zjCytK68a-ez9QyJfrQxVrNq4LGKYeLIx-OskgeGU6e1KDHvBxqSczaOQopGdPKJVlKFwlBDVThwQrovHuIliY0wYcJkCT4NxQV4vfnwrS3ki-fNsdVm_1UcDtwWVmOoo6JWcZCV6mGQTONkgl3Rj9r3tRUWW65V6YHqzUFsB5lNPNedbA9Hh56G-gI--UsTm4R5WWfLqWzoB0NZCVmXydRZuCj-UltdMg7x26xsS3ROKqNJGCEINf1b5yykcqGmL9ytr-BofnCXMLE_53SOHnNAxHZqlSv8F6FrZHKKYgGoqdu8TCFulHM2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DfTxjG0okQUMxsKoHb1zeGervKi2xwh_gSFQ2ZVP3oCbddCA7FLbNuB7Q06Qu3FA0cz4YMAwc0R_9ZfN1Agj2VJJ51RvXSJXzLXZ5vLMYf66c0iLtAS8dPLWZQPk-5RniwooMe8yl1Tph7fsYbn_-nvXQPhRdYVaiL-DERmHBCvMtZTe_MeGMAoXqYMz9WScga1xkXUpQJBNngto1d-081qn0d7J5bVsKc4m3_XRTwWBpCuCxmjjB0pzl5gdMleU1aVAWZ3n5_ZgAuzRb0XbfsXaX0QXYckybPnWRo4wOxo9Sri3iZeKMijwwoND9MDBMHPjFrzQukoFvpnCMJkzNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ گفت: «به بی‌بی گفتم خیلی مراقب باش چه کار می‌کنی، چون ممکن است خیلی زود در برابر ایران تنها بمانی».
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز دوشنبه در گفتگو با کانال ۱۲ تلویزیون اسرائیل اعلام کرد توانسته دامنه حمله اسرائیل به ایران را محدود کند و بنیامین نتانیاهو را برای کاهش تنش‌ها تحت فشار قرار داده است.
ترامپ گفت: «من موفق شدم شدت حمله اسرائیل به ایران را کاهش دهم.»
او همچنین افزود شماری از کشورهای منطقه از او خواسته‌اند بر نتانیاهو فشار بیاورد تا از تشدید درگیری‌ها جلوگیری شود.
رئیس‌جمهوری آمریکا در ادامه گفت در مورد حمله به ایران به نخست‌وزیر اسرائیل هشدار داده است: «به نتانیاهو گفتم خودت را در برابر ایران تنها خواهی یافت.»
ترامپ همچنین گفت نتانیاهو «با تاخیر مرا در جریان حمله به ایران قرار داد، اما من موفق شدم این حمله را کاهش دهم.»
کانال ۱۲ تلویزیون اسرائیل عصر دوشنبه ۱۸ خردادماه به نقل از یک مقام رسمی دولت نتانیاهو اعلام کرده بود اسرائیل حملات به ایران را به درخواست دونالد ترامپ متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76080" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cs5dwWtnTauDH7Z3yiZbTz-SdNilY7EjdxiZGgAcKvRh7OQqOX7c_3khNl54AHrTop8vbcIyqn_jgGWhiDFlizCAYZDJLJQ3rJaftlmdprvvpuw2Palu1clzXRT17O_VDf8pzddko_kTaI5BDdpcXVYYyjNfXDdB7LwrNI1UiAJNU4lMmQWmQUNpCe9l3ihhS8D2WCu1cxvIj8EvzkOBipyLEdi1TLNDXUsy4349E4OXTpuqp3_Kxk55KlmjCHX9_nEqXZgPcDDkhd-Gx1xlkpChXbg9KHcPhfSAaWy37PXzAWuL1eHcJU3seCxWRf2n46KTFpfTFNXq0KceeazpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: نیروهای آمریکا نفتکشِ متخلف را در خلیج عمان از حرکت بازداشتند
پست اکانت فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
تامپا، فلوریدا — نیروهای آمریکایی روز ۸ ژوئن یک نفتکشِ بدون بار را در خلیج عمان از کار انداختند؛ پس از آن‌که این کشتی با تلاش برای حرکت به‌سوی یک بندر ایرانی، محاصره جاری علیه ایران را نقض کرد.
فرماندهی مرکزی ایالات متحده، سنتکام، نفتکش
M/T Marivex
با پرچم پالائو را هنگامی که در آب‌های بین‌المللی خلیج عمان به‌سوی ایران در حرکت بود، از کار انداخت. یک جنگنده
F/A-18 سوپر هورنت
از ناو
USS Abraham Lincoln (CVN 72)
پس از آن‌که خدمه کشتی از اجرای دستورهای نیروهای آمریکایی سر باز زدند، یک مهمات دقیق‌زن را به بخش‌های مهندسی و هدایت کشتی شلیک کرد. کشتی Marivex دیگر به‌سوی ایران حرکت نمی‌کند.
از زمان آغاز محاصره در ۱۳ آوریل، نیروهای سنتکام هفت کشتیِ متخلف را از کار انداخته‌اند، ۱۳۴ کشتیِ فرمان‌بردار را به مسیر دیگری هدایت کرده‌اند و اجازه عبور به ۴۲ کشتیِ حامل کمک‌های بشردوستانه داده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76079" target="_blank">📅 20:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FvUIopfLqRUZvJ8z8hckL58sBTnorT0gdbAV2fzlyYq9bVld8IMEoHy5LoZSE0JCeeXCEH4xxd86id6t2MDDbgXYrF2W42eXHfcOjO2IElnnXQfOpr59JjQ3XNYtQ8f0rOVlz9eq0h1T_gheHJVQY8i0WSbwzASqNQcRpsHGK-qj96A0jLMnD8ykn0cv7wZ9rhGVPCjp2XeFic1CSkSEdYQQg1xLl3BYRlOZHnDPGfa1izAx2CpRU6KpRD-cLMTokryI_Gen02PxwrtP7OFp6w5VqHRtmDGTtruWjQHsKdZRecuDHhnHJd7GG99Y2Lod7NpVD7qky_LCi7XRX8VhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.  به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.   اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع…</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76078" target="_blank">📅 19:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mJ8O0i_bqgc8U6dcmZu17ZNvW1p-rue7I5M7kHBFztCw6BPHW89c6-gC07vTFcTaWo7jFsE9HCUIkOW6UIwF_pgZS18Q4er889eSUXw0EI1_e-ahvMPtnd3FrypDXS-3RDki7J8aGYs4OVFKIZUqC4lHVdJnnIuNvAIldR4hzNDjzElui5RDwS891VHtUObfVBCon7WzmYCJtp3wwXjuaQ8Y5mh_knG8uc6KUakILnGu8_mOjXwi3UznHgg-P80Ejk2zpJtRUicQFv9oecfvAaFy_xLr9AuugP_z-U1McHZDe235yQM3w0ilzMlL6MLa1HpVjHaYZsafa_-QujcKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران وضعیت پرواز‌ها به حالت عادی برگشته است
سازمان هواپیمایی کشوری ایران عصر دوشنبه اعلام کرد که فضای هوایی کشور به شرایط عادی بازگشته و عملیات هوانوردی مطابق با اطلاعیه‌های هوانوردی (نوتام)، از سر گرفته خواهد شد.
ایران ساعاتی پیشتر گفته بود که تمام پروازها از فرودگاه‌های کشور لغو شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76077" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lnakouFw-1a1MqPzP2bJ9BUJJfO5Ib4ZbBO2Zc_m-2Min0rqqyRrJrPVwrd7T4-nr56kKNXheAXl-_cdHn3_P6mqwvEf006FrzukNbSdU-zpvM0C3lXfhkTjiZnCL4_Z3fV_kxRv0udj9g0Bs43HTxskWdimxtK7a5IGZtdQKNQgSicrT6VdXPhNG4VgTQ2qQWgGK3jCkeMdFCpObXawVHEnG4wa1KWsJeikwv187pS5P5kZBr-Z0pvFh2gWH2j1ODhALfKtJ3TzIPzjZSaNU_AB6Nel1Zezsobtqc93RuagiXWxob0PzqZm8kiZEBKYllhn4iBn3Mzdbiq1iLz8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد یک موشک بالستیک که از یمن شلیک شده بود، در منطقه‌ای خالی از سکنه در نزدیکی مرزهای عربستان سعودی و یمن سقوط کرد.
به گزارش رویترز، وزارت دفاع عربستان سعودی اعلام کرد این موشک به سمت یکی از کشورهای منطقه در حرکت بود.
همزمان حوثی‌های یمن، تحت حمایت جمهوری‌ اسلامی، اعلام کردند دوشنبه یک حمله موشکی به منطقه یافا در اسرائیل انجام داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76076" target="_blank">📅 19:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU6xbiRnZQmotiyjE1yzqR49DAQeAp94_Ht7gz_JC056MpRRWCJIHy1VkfLbmCLpZqsOf5njL1OvOJA87ACmgfP9q38kx1mQLJsJzPIkCim2HcsglTakDZywhlJrEzV5aeV669UaR2tDvyjd6UzVGmlWhF2gXEJ4nsD_jAFmN1fEsfKWf_i4KwwJXqSmuTF0UtCW_tJg-Fu4iAeYDXbJRH6TsDl3iOosbA-7Nm6UCZTTPbkgcQMtbnBM9iVqJihB61F1wRYAgUsYRLm7ydGuLdTSn_MPzW1a4wEZjO1K_ec7KCnCKK0uXwMqhkmz8qkRDeuYK2lJKVq0vUOy5tUXTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اظهارات مطرح‌شده از سوی ارتش اسراییل مبنی بر مشارکت ایالات متحده در رهگیری موشک‌های بالستیک شلیک‌شده از جمهوری اسلامی به سوی اسراییل را رد کرد.
به گزارش سی‌ان‌ان، این مقام آمریکایی گفت ارتش ایالات متحده هیچ‌یک از موشک‌های ایرانی که بامداد دوشنبه به سمت اسراییل شلیک شدند را رهگیری نکرده است.
این موضع‌گیری در حالی مطرح می‌شود که در دورهای پیشین درگیری میان ایران و اسراییل، آمریکا با استفاده از سامانه‌های دفاعی خود در رهگیری برخی موشک‌های شلیک‌شده به سوی اسراییل مشارکت داشت.
@
VahidHeadline
نباید اینجوری نگاه کرد که تعداد موشک‌ها چقدر بوده و نیاز به کمک داشتند یا نه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76075" target="_blank">📅 19:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76073">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E4mENJYuyT1uJnX7ynfmErZuj3fluTZcAoF_Q1-pvNdTNvM40QwBWfusLStfMh4Uwn5qkk-l7qnUGIN0AiRzctaJwuPHlZpCPRX5P-q-kImbcV6lw5KClR3FfmJaP5sxRusZ_8eTwjIZIMaxK0fMmiwEIsl1al69_iZR7xQ_b8r8aXhl6vJUwa0uderX8xypogiRbhoFq0-2GiXDXSTLKaMfa7oB7qBu-S_HIIJ_rJjkNh2IZjeVAVHrau_B27_iEkEbCzDUa15zzfDbmNaMKPQh3HBifS7joL2JbdCNrab4U8y7UzvhTiURuzx23xlgmhj-kjyM80N71KI2E8RZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fca0bb1962.mp4?token=JuZBGHF48Nt8R_aBar1r14g0JEW2pixgI0uoHnqOcKM0RSkkT2EgmEYsxZDOdxOLU629b7iPKOcs5wzsFmpkMLfgTAKVVm76IvStZGJNX4KJ8m-WiFclTKOWSlR7qY7sDOcQdxr6XVdOUS4tMbSHAl7022852p2GxDDXVqKV9CzMpc2oApRpccHnT_ctOnpdubjfGOXEAW_SoU0QqTD1FphIAXd17YKs0h35H4WkC_Aq5kza9NqqAt_38uVCEj0BfT8DYAl_qalTXxsBsuLTZ5uEG8SJtitdew9-6DvvoaTDUfWNHbBlu--8_33BqLIYPu_bHaK30eFpSijAo-vpFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fca0bb1962.mp4?token=JuZBGHF48Nt8R_aBar1r14g0JEW2pixgI0uoHnqOcKM0RSkkT2EgmEYsxZDOdxOLU629b7iPKOcs5wzsFmpkMLfgTAKVVm76IvStZGJNX4KJ8m-WiFclTKOWSlR7qY7sDOcQdxr6XVdOUS4tMbSHAl7022852p2GxDDXVqKV9CzMpc2oApRpccHnT_ctOnpdubjfGOXEAW_SoU0QqTD1FphIAXd17YKs0h35H4WkC_Aq5kza9NqqAt_38uVCEj0BfT8DYAl_qalTXxsBsuLTZ5uEG8SJtitdew9-6DvvoaTDUfWNHbBlu--8_33BqLIYPu_bHaK30eFpSijAo-vpFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل روز دوشنبه ۱۸ خرداد با اشاره به توقف حملات متقابل اسرائیل و ایران گفت «آتشباری متوقف شده اما اگر رژیم تروریستی (ایران) اشتباه کند، ما به شدت پاسخ خواهیم داد».
بنیامین نتانیاهو در اولین پیام ویدئویی خود پس از آغاز موج تازه حملات ایران و اسرائیل، افزود: «ایران و حزب‌الله از همیشه ضعیف‌تر و ما قوی‌تر از همیشه هستیم».
به گفته او، «ایران و حزب‌الله تلاش کردند معادله جدیدی را به ما تحمیل کنند که از نظر ما غیرقابل تحمل و غیرقابل قبول است. آن‌ها فکر می‌کردند که از خاک لبنان و از ایران به اسرائیل حمله می‌کنند و ما سکوت خواهیم کرد. این اتفاق نیفتاد و نخواهد افتاد، نه در زمانی که من رهبر هستم».
نخست‌وزیر اسرائیل تصریح کرد: «ما حمله خواهیم کرد، با قدرت پاسخ خواهیم داد. به نابودی تمام زیرساخت‌های تروریستی آن‌ها در جنوب لبنان ادامه می‌دهیم، و امنیت را به شمال باز خواهیم گرداند. اگر به موقع و با قدرت اقدام نکرده بودیم، امروز این‌جا نبودیم».
نتانیاهو همچنین گفت که ایران به سلاح هسته‌ای دست نخواهد یافت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76073" target="_blank">📅 19:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BujII5PUc8KLoZsMyd5NnFbGbObeQ9e3pBITUcNuklIlrybyoTR1Sb_7-RRr9riAuPAiy9UcYYWUE80TRMqySGKJ1COJV4JcJyKg_O8WHdx0ZXVyGw7pTcVfYFFaMN6WkIiaQ-6M7ZKEsWuM0a3TX4mmRb0mxZioDsu5q3cnH8qdeyhZ0KWYN8RhjC-3gA3kny51axOSc_1pUHaPsS-_v25lT-f2QivcCGCU5iQcnxoObsTA6EOiIwEZ_80ie4unuOY0vRQWsBTyt5bTvNAf1Rjxmpdy99X5SGb2NVenbDYZoxWcU6qvVuxtNRTiHPohM8onUxC8cQlJoLDRuPmQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هشدار تخلیه فوری برای مناطقی از لبنان صادر کرده.
J74wabx
ارتش اسرائیل با صدور یک «هشدار فوری» از ساکنان جنوب لبنان، به‌ویژه در منطقه «زقوق المفدی» خواست خانه‌های خود را ترک کرده و به سمت شمال حرکت کنند.
آویخای ادرعی، سخنگوی عرب‌زبان ارتش اسرائیل، در شبکه اجتماعی ایکس نوشت: «در پی نقض توافق آتش‌بس از سوی گروه تروریستی حزب‌الله، ارتش اسرائیل ناگزیر است با قدرت اقدام کند. ارتش اسرائیل قصد آسیب رساندن به شما را ندارد.»
او همچنین هشدار داد: «هر فردی که در نزدیکی نیروهای حزب‌الله، تأسیسات آن یا تجهیزات و امکانات رزمی این گروه حضور داشته باشد، جان خود را به خطر می‌اندازد.»
این در حالیست که ایران امروز گفت عملیات جنگی علیه اسرائیل را متوقف کرده است اما هشدار داد اگر حمله به لبنان ادامه پیدا کند با شدتی بیشتر از قبل پاسخ خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76072" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EesRjRmNBRX4K4SvZYP8Khx9teDKNZyDKA1aaku5w2JtrcuYQtIwC7uuFEPlq3sHM_TMk79zjOmVNa3jOb-_Jk4iauEErEAuHEpJ4ixrgzd08YhlEI76TZ05puiwLiQDDplrGer7q052q8Reru1dWu-aN2TuPqIwVS1WrFFf3_CXjqE7Aa-x_XFuZy0o_tipkO-E6uKlkGSeZ5n7HWB4YAeFvzbYAA1i6OsdQySqPuYXoC6ArRrBy6IrdVmXrwsAFnUfzkH3cOUEr64RHeRC7LwhZr6wCiqpabjwnbNLV1WiFE75-B85tzef-g017RfZPJaxGfkE-m2iRDA7WJokOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranSaat25
(وطنه*)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76071" target="_blank">📅 18:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76070">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BhpGg7nXoI5JFFNGaXWdH5wEvIRtdxytpiqh9CS8HenBQlGL38xt8DUAizB74XlAK-SIBFz4rDII9PSbY93ZvK63u3nmPkxbOBEVIYG9cdRNsfrcJhCgSEAx_EhnHYMleRxrYfXXIREToA6i336uUokHCEAisk5cFOwhCqnmXbRaUKIJrem583lL2_WJjoLiW_SfUhUhG3q4AFGh5_sZyvQnVqPwYqAy4W0OOZ3KvLKi3TUvUgAL7JQgmHAeydVBIgfK_ljG6C2ekmHWeju9TzLHDOtNbZeVoK3CS6ts5VWxIM1Qu55jiXuZYkoIRZrtwVHmcIcp_GT_l0cGrmB_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Atlansick
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76070" target="_blank">📅 18:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76069">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p9Yc79OX10wnwLaI1QROKIhiz3qDrQM5afyW00COhI03AoR8gLhlQ81k4HV74xCVj9j6zXRpFPtmp4vPp_q4hAg-qE-SThcl09aW1J9oM2TSxtxocWgtSIZgH8UCTshqYwg1vu5Q3FKLL0ugoZc9ygaCzP_zdMjHnjEZRRGCTOvcGHb98vsKR3Zm5jiktSvic93KjJe1pOteMjr40pOIo6FDnATyYZ0BdfsKOQ1HYSVXqCx1bplZ7TqSc4jPwoZYz555XnFoWKyRd3fzwRjO-N_NwvYgOgQEgVWSGcnakb2pqmjBbeXLAwa3HsXgO-TJGwmVUU8ECZKEham88JdynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی جمهوری اسلامی ایران، در پیامی که روز دوشنبه ۱۸ خرداد منتشر شد، هشدار داد در صورت تکرار اقدامات آمریکا و اسرائیل، منطقه با پیامدهای گسترده‌ای روبه‌رو خواهد شد.
ذوالقدر در این پیام نوشت: «تهدید معتبر را از جایی غیر از واشنگتن و تل‌آویو جست‌وجو کنید.» او افزود: «اگر ائتلاف شیطانی صهیونی-آمریکایی دیگر بار دست از پا خطا کند، منطقه برایش جهنم خواهد شد.»
دبیر شورای عالی امنیت ملی در بخش دیگری از این پیام مدعی شد که جمهوری اسلامی طی «چهل و هفت سال و صد روز مقاومت»، از میدان جنگ تا عرصه سیاست و دیپلماسی، معادلات امنیتی جهان را تغییر داده است.
این پیام پس از آن منتشر شد که قرارگاه مرکزی خاتم‌الانبیا اعلام کرد عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل پایان یافته است. رسانه‌های رسمی اسرائیل نیز از توقف حملات این کشور به ایران به درخواست دونالد ترامپ خبر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76069" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76068">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul79O6SyeLn64CAhrXHG4CJDELf_4H81mTj09Worf8x_egt5Z7G0M5X4nnKzh71k8SJytopmAtar5x4hIgeTmTVjiv6pd7P_wmY7kKCk-winUYux48cZfOAF8zz018CCqwwToDcOuitgBCvI4_D7WAAyZPwraFkVB5MdAOnhTitCHDzaBxH5sVipxZepj4TfSAppBg5B35Jak1KdZAJ9PafVyRsZC-UUq5cZBDOgy3ehnXAqP60bQwo-n1KXpNSxhnXjm6lhIWqjLchYfxZ08w6HoRDygVo7wapQjeAJDM6O6QPQKF-KBVvtohO9XEbUVLzBV0EH757qosqaHf-HuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، اعلام کرد هرگونه حمله به شهرهای شمالی این کشور با حمله به ضاحیه در جنوب بیروت پاسخ داده خواهد شد و ارتش اسرائیل به عملیات خود در لبنان علیه سازمان «تروریستی» حزب‌الله ادامه خواهد داد.
او افزود: ما تهدیدات جمهوری اسلامی را کاملا رد می‌کنیم. هرگونه تلاش تهران برای پیوند دادن لبنان و ایران و حمله به اسرائیل، همان‌طور که یک‌شنبه اتفاق افتاد، با شدت زیادی پاسخ داده خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76068" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76066">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c3ab90b1c.mp4?token=pgzpWgcqwQqk9CWW-8bDbt11gYGMMUcB_hbydfV-5El4gH_F6bYG6rP2xAsMvy_pwVpV1R-ZPSsSqc7VjRIOgrF9qydsRy0m7GlmKd2x_CtJtVyBrcVzFO4nZxUN1tD-FO9_FAYnnz-QGbwC7I2mTy7ktT6NXCTzfVnK2v8unC8uqwv5n5wdXNdcZRZrIzBNYGGGQg2hfHHHq56JHAgyEF3AicRfAZ9q-iMjb0F1DjpnzWRH2c6o9Po2pi_G5mS1mLsEnN7lqlidoqCagSMVCGEPkKMCRLSExWxahdMdAqVGG6a0tVgHTfmrm0ZbIi8rdWubNblMAkDzBjXZKE0Muw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c3ab90b1c.mp4?token=pgzpWgcqwQqk9CWW-8bDbt11gYGMMUcB_hbydfV-5El4gH_F6bYG6rP2xAsMvy_pwVpV1R-ZPSsSqc7VjRIOgrF9qydsRy0m7GlmKd2x_CtJtVyBrcVzFO4nZxUN1tD-FO9_FAYnnz-QGbwC7I2mTy7ktT6NXCTzfVnK2v8unC8uqwv5n5wdXNdcZRZrIzBNYGGGQg2hfHHHq56JHAgyEF3AicRfAZ9q-iMjb0F1DjpnzWRH2c6o9Po2pi_G5mS1mLsEnN7lqlidoqCagSMVCGEPkKMCRLSExWxahdMdAqVGG6a0tVgHTfmrm0ZbIi8rdWubNblMAkDzBjXZKE0Muw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسراییل، روز دوشنبه ۱۸ خرداد، ویدیویی را از لحظه حمله به یک سامانه پدافندی جمهوری اسلامی منتشر کرد.
ارتش اسراییل گفته نابودی سامانه‌های پدافند هوایی ایران، آزادی عمل هوایی بیشتری برای عملیات‌های بعدی فراهم می‌کند و بخشی از تلاش این کشور برای مقابله با تهدیدهای جمهوری اسلامی به شمار می‌رود.
@
VahidHeadline
و در پستی دیگر ویدیوی دوم بالا رو درباره مجتمع پتروشیمی در ماهشهر منتشر کردند.
بدون هیچ شرحی درباره اقدام نظامی خودشون نسبت به اون مجتمع پتروشیمی
نه در متن پست نه در خود ویدیو
اگر قبلا تایید نکرده بودند که به اونجا حمله کردند این طور پست گذاشتن بیشتر شبیه به تهدید به نظر می‌رسید. شاید الان هم همینطور باشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76066" target="_blank">📅 18:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76065">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V9QfNjmKZ8XIAx-qNwkLmto5kWvSur5AVU__ch1TU9xT2RzUP9VeH_d0R3aX_l0Nt6trsnn38w0KCqFsnZRnebml7A_0j8DhD6ka0IUdRY9tSkcA5Zmz2JYCa2Yg3t-1qvmhfDEViG6ImQ9bLMnifLcQ03dbNIjyNsLeLHbvq9vcPGCtvZbTXi3-xXbU70xSqHg3Gck_oy0t0qkObxdGMzIusY_EJ6TgO-ytlae0iWDR_dXyHm1Q9mL2C4fYS22uEpjfcJACqbLigT4sdd1TNSMk2HXhZXLn-y7cuzYLli8Nu60RzEEN7uVDztpm7VPMHkFaoffu6y-vER6KFw3Q4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت محمدباقر قالیباف:
"معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را بر هم زدیم.
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود."
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76065" target="_blank">📅 18:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3_v5nPukwFI7x8LMKV51RmV0wn7y5Uuzd9KsqmjPmkOQOEHtqbOGKKJne6pmlMC9Tc9YK0F3VpKbtmkcg-HQ4cZV6NSbQiEul850nS1d55USzrf2zr1Sp1UTUf4qZnSmISldkkEvAv2CcxCjDRt7A6Xh6GylFLPGRBuqrXlA-MdCRHoTaeH-PV1xLDJrZ9QTW8jLXwZOUTcLdRYuUySxIs6wv86GyI-6Zi_pKS5dGXuoKdYHbTuOf_YGUeAJX3f7mHSfMSFKT68rME52cWn-_Kl4NHxwSqmfuzQqEDs2mQPDi22tIwos01DMh6XhD5lNrBhoIjBxJrzrK9jSFAJeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های دولتی لبنان گزارش دادند یک حمله هوایی اسرائیل روز دوشنبه ۱۸ خرداد یک خودرو را در شهر صور در جنوب لبنان هدف قرار داده است.
خبرگزاری ملی لبنان اعلام کرد: «یک حمله هوایی دشمن، خودرویی را با موشک در شهر صور و در نزدیکی ساختمان صلیب سرخ لبنان هدف قرار داد.» تاکنون جزئیاتی درباره تلفات احتمالی یا هویت سرنشینان این خودرو منتشر نشده است.
این حمله ساعتی پس از آن صورت گرفت که جمهوری اسلامی ایران و اسرائیل پس از ۱۶ ساعت درگیری نظامی اعلام کردند حمله به یکدیگر را متوقف می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76064" target="_blank">📅 18:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJT2f15w3-vNjyhwsMZHQPzdOO-2NCA-7hDBSi-IT2SLnbToNKEzCLQPW9uQ6kpBAB2XZt5V_-ZTfBb7ZvMPpejAV41q2XjkiKodT4sZfj1mluIp0K9hEjkG2Gr0HtI92wEWB8JqxTe39JyOf-im6v9vwKwjLbVM2MUyPLGRZWQ6tkoceW4FHvmcwyHHL70PrsfuuOWVpHBht8SagQtjD7fGdTfB3c-atJNLlNdnBrzKEd6tEGMjw-ZDw8YWOZoy1bpj-DO7b5MFBZWgl6xzImiIpKLrOqzHgomICtDo0rzfcBpclUJhLjlI_CxUlGIDucT2e4Ie0gCM96m7ez_noQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس سازمان اورژانس ایران، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اعلام کرد در جریان حملات اسراییل به ایران، ۱۵ نفر مجروح شده‌اند و تاکنون هیچ موردی از جان‌باختن شهروندان گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76063" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNZXfcx0avFgaHBVaOLqFslV3Cl7RYv12ACv87ln2c_agBLIpc_zJw75ajg9ri9E3cpyuYn7sFvBj2l3QxrNrQPubO6OypBnr-uM9zLG7PEpBjV_9-wIYuiWjOdXEYyTk5GIoVqSoqeoK4iPGTq_jAPNBx-OB4KzEYfNIUFRwS0fs72OSMZ09WikTjDv6nW3mu65MqZWpZum26Z3KII9BZt9JxoMY8_DjGhAFUFjcEKgom7SjRjr-xCf_4IGXoNxpVu5T0iX-Zbzs10Iymq7CfcceVnvYdls0mzVjsMjBSy1JFG0B8f35v4HPsM6bQl5UGGAHOzkIK8-kpVHf5XTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایسنا عصر روز دوشنبه، ۱۸ خردادماه، به نقل از شرکت فرودگاه‌ها و ناوبری هوایی ایران خبر داد که «همه پروازهای فرودگاه‌های کشور تا اطلاع ثانوی لغو شد».
این اداره همچنین از تمام مسافران خواست تا «جهت حفظ نظم و پیشگیری از هرگونه سردرگمی، تا زمان اعلام وضعیت عادی از سوی مراجع ذی‌صلاح به فرودگاه‌ها مراجعه نکنند».
این خبر ساعتی پس از آن منتشر شده که قرارگاه مرکزی خاتم‌الانبیاء سپاه در آغاز بعدازظهر روز دوشنبه با انتشار بیانیه‌ای از توقف عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل خبر داد.
همزمان رئیس سازمان حج و زیارت خبر داده است که «با توجه به شرایط پروازهای بازگشت حجاج احتمال تأخیر در برخی پروازها حتی تا ۷۲ ساعت وجود دارد».
او اضافه کرد: «برای فردا (سه‌شنبه ۱۹ خرداد) ۱۰ پرواز پیش‌بینی شده که امیدواریم بخش عمده آن‌ها انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76062" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZUv4XeATCP3ZAhdklV834qj0Kp5kI08HOe7oFJaEVUJwcdGzMfA0HPqmpUZQcFcRLOkpWEUy65jVLDaitwSf_kIsnyglZna2FDBtlCjU7z_EHfxOkVDgAjq0swACrGLj9cDxUbc9qj2P_RPpTv1FIy_Id374pRYp1nfWDUFTCPmL7mEvpil2rJMJcT-LuchKiU-5I9mqyJPpuaXQJMWSWyFHYTb4pPuXtmQdXgqIuGXTOBplL17o3h5FRALjoksUAOrgfbw-m4Jcew4u6OoqrC3yLYKulcOqH7TIiEI9dv_7wXQ5_r2Pzk6PArTqWaJB-BVwfKA3abAklxkckYWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا، روز دوشنبه ۱۸ خرداد اعلام کرد که اتحادیه اروپا به‌دلیل تهدید آزادی تردد دریایی توسط جمهوری اسلامی، تحریم‌هایی را علیه شماری از افراد و نهادهای ایرانی اعمال کرده است.
کالاس این اظهارات را در جمع خبرنگاران و در حاشیه نشست وزیران دفاع اتحادیه اروپا در قبرس مطرح کرد.
هنوز جزئیات بیشتری درباره این تحریم‌ها ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76061" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b31564948.mp4?token=MPAhZNzrvFi-ESiqYVUTZuSG5IWAJV5WrKOYmmWPP6d-svRTR5apblzjgvGw2caJAxMje-hAC9C-brEpW4jNrpOG-b8arO6FNdSnw2W3Zx7BrHOwHWcI1EputF6zbjqa9ITjvFuO9Yw3vBTuURshsz8Yai2K0eE0Lp0rNCLGMzmbmncM18aG3CMIrUGhbktvr5oiOM979f1vYkxbFLhJcBEviam7IRVxY6dRqhRxixXCMfoqzL53hdBSrW9arepQUN-UdRTp1u40sp_B_eFoTED4THSHA9Sol_QrYuWB1uDWxp7ba-8CneHxYM0MbZp1eaYUm2JjJmn_mIY1RBOWVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b31564948.mp4?token=MPAhZNzrvFi-ESiqYVUTZuSG5IWAJV5WrKOYmmWPP6d-svRTR5apblzjgvGw2caJAxMje-hAC9C-brEpW4jNrpOG-b8arO6FNdSnw2W3Zx7BrHOwHWcI1EputF6zbjqa9ITjvFuO9Yw3vBTuURshsz8Yai2K0eE0Lp0rNCLGMzmbmncM18aG3CMIrUGhbktvr5oiOM979f1vYkxbFLhJcBEviam7IRVxY6dRqhRxixXCMfoqzL53hdBSrW9arepQUN-UdRTp1u40sp_B_eFoTED4THSHA9Sol_QrYuWB1uDWxp7ba-8CneHxYM0MbZp1eaYUm2JjJmn_mIY1RBOWVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی از لحظه حمله‌ الهه و شهربانو منصوریان به اتاق ریاست فدراسیون ووشو و شکستن دوربین مداربسته منتشر شده است.
طی سال‌های اخیر
خواهران منصوریان
بارها به ساختمان فدراسیون یا کمپ تیم‌های ملی حمله کرده یا با مدیران درگیر شده‌اند، اما همواره از حمایت نهادهای حکومتی برخوردار بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76060" target="_blank">📅 15:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kF4nVG2dTchRehoE8eDSCTZuWkJ1t2dFqDUBT2U4CRGvzv3v73lXTEMWyOlwaey8rFVX-kCxgqMSwiEz_SLuKq8PKfvbU9W8QmS4woy-00G-ylTtAN4vcUhRmQC0i_hVkcYQVosGSvPWHYIj-6i9Dd5aZOOWuKwroYwwwE-ClgP_k0xXF7G0TOawZQSVbT8HrVVXfcHOvUzzY1bJm8akTrYA8GvqhUHUW31Vdb7ayJiKCg6WX-61e6cDFqlbrCgg-h24Q8b-djFXXzZTAGN5JPWozw6BQ6qwEAzHt4Xe4m5Ue3Vht43S2KpZBiiMoZOFgGunzGk88cF2bwwImbBWHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سپاه پاسداران از «توقف عملیات» علیه اسرائیل خبر داد
♦️
قرارگاه مرکزی خاتم‌الانبیا سپاه پاسداران، روز دوشنبه ۱۸ خرداد ماه با اعلام آنکه نیروهای مسلح جمهوری اسلامی ایران در واکنش به حملات اسرائیل به منطقه ضاحیه و جنوب لبنان «پاسخی دردناک» به این کشور داده‌اند، از «توقف عملیات» نظامی خبر داد.
بر اساس بیانیه قرارگاه خاتم‌الانبیا، پرتاب موشک به اسرائیل «در راستای حمایت از مردم مظلوم لبنان» توصیف شده است.
در این بیانیه آمده است که این پاسخ برای اسرائیل و حامیانش باید «درس عبرت» باشد.
قرارگاه خاتم‌الانبیا همچنین اعلام کرد «توقف عملیات نیروهای مسلح» در دستور کار قرار گرفته است.
با این حال، در این بیانیه هشدار داده شده که در صورت ادامه حملات و اقدامات اسرائیل، به‌ویژه در جنوب لبنان، جمهوری اسلامی ایران «اقدامات بسیار شدیدتر و کوبنده‌تر از قبل» انجام خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 467K · <a href="https://t.me/VahidOnline/76059" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

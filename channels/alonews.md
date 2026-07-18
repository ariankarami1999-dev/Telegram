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
<img src="https://cdn4.telesco.pe/file/OkNnPhH7KymmABjXjlJA3J4cTf_AikVTNSbnH1m4bDqm2NWJha84kZoIGCy220omjQvpXfiZyP81aMPa7vRsfjA6FFCglZgFwNTD1lEsxrrdfRZCyuPTiHl-w1JugPXxQBdJyt8O3VvwfxlTJ8-HKCcUMbDy0hbCyaKUBngeRLl-kFrq9TYzamj5_moK0N_dYiNJUTp22EzDwIzDnGIZf7YqE1_bnhlOTx7Sc2_7PCewFqGL2yFB7DQRmWj_jmERyePfxGyLKRZfWLo-rXS6wRiQmIV-r3yquTpWK9H5jgKKOhNBUHl_2oHGdCq9wVqJf05BrhR4d1eHTquHnYMBcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 15:41:26</div>
<hr>

<div class="tg-post" id="msg-135368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری / اکسیوس: ترامپ در حال بررسی یک عملیات گسترده علیه ایران است، از جمله بمباران تأسیسات زیرساختی، حملات بیشتر علیه تأسیسات هسته‌ای و بمباران سایت «کوه کلنگ»
🔴
او هنوز تصمیم نهایی خود را نگرفته
🔴
رئیس‌جمهور آمریکا ممکن است که در روز‌های آینده دستور تشدید عملیات را صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/135368" target="_blank">📅 15:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
غریب‌آبادی: تعهداتمان در تفاهمنامه اسلام‌آباد را متوقف کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/135367" target="_blank">📅 15:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135366">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
به صدا در آمدن آژیر خطر در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/alonews/135366" target="_blank">📅 15:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135365">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/alonews/135365" target="_blank">📅 15:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135364">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
انفجار در منطقه میناء کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/135364" target="_blank">📅 15:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135363">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
به صدا در آمدن آژیر خطر در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/135363" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135362">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/135362" target="_blank">📅 15:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135361">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ممدانی شهردار نیویورک: به دنبال قانونی برای بازداشت نتانیاهو هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/135361" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135360">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
مقامات آمریکایی به «الحدث» گفتند: ترامپ در حال بررسی گزینه انجام حمله‌ای گسترده به زیرساخت‌های ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135360" target="_blank">📅 15:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135359">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d3f43769.mp4?token=MS5nt1D7eUYWtbvMYeFsDgVIO3TnenRx4Q4snBNUEtVB1h0IJ7t3j8-E7YD8FrKgBDy3wcQNexMPqpkWqg39jH1LXv-J-66M_e1IwpEOvVzj81Jv894G3LAvW87simmAbDiVSHgaNLNOylB5a7SBW0Mi61_RQc2FaLUiEuKEjnoN8a5p_GWithUTjBo59fdDKmgErH481Senli2voNbkeM0biaJa-QlJsRMweB7X5Motf6Gl2VFHIJ9_wYH-QxtbWlK9IhywnyRfTvfRfHDfk_bNbhq7CDSjOJm3mQOaBQ2NQSIZzcejimSWUmiqO2iKNQc08ThUOAIrsGI6mIaIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d3f43769.mp4?token=MS5nt1D7eUYWtbvMYeFsDgVIO3TnenRx4Q4snBNUEtVB1h0IJ7t3j8-E7YD8FrKgBDy3wcQNexMPqpkWqg39jH1LXv-J-66M_e1IwpEOvVzj81Jv894G3LAvW87simmAbDiVSHgaNLNOylB5a7SBW0Mi61_RQc2FaLUiEuKEjnoN8a5p_GWithUTjBo59fdDKmgErH481Senli2voNbkeM0biaJa-QlJsRMweB7X5Motf6Gl2VFHIJ9_wYH-QxtbWlK9IhywnyRfTvfRfHDfk_bNbhq7CDSjOJm3mQOaBQ2NQSIZzcejimSWUmiqO2iKNQc08ThUOAIrsGI6mIaIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دولت سوریه اعلام کرد یک کامیون حامل میوه که به سمت مرز لبنان در حال حرکت بود را توقیف و درون آن چندین  قبضه گلوله و موشک ضد زره کورنت/هویزه کشف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/135359" target="_blank">📅 15:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135358">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfM55zotzK7-MtJFnNRNVVveFwQkoNJ4Z9EDGUsqSo-gLqBN25M8rDgu9bjXRAW9fu4YteB4xi0RmIQhhRl68uMlJ61y-zb-GbWSp7a4RpjtXirxkwnvreeUaozSFawyGeV7Lz7b9fW5IQpuz3uc_vEUrPw4_W5ILZ5bvASyuUgryFg0KnuFVq7qxxs7wYYW0Y92i0vIsHziR2k2ysQxGrMwBsL0Cs5ydRj_TXtXNbtwzAAI_bhBgPHFx67rVn4D7d77zPwOP8g8q3TlgA_VwVnWGyvL627Ecv4KgEATSsAVUUlyXyhPketPS0joZAOVqlGfEVTrvS1kFjiBRKtjwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پایگاه های نظامی در اردن هنوز بعد از گذشت چند ساعت در حال سوختن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/135358" target="_blank">📅 15:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZDnimTPedBulHFi2JG34woJVuU39d11yIQGu4J1Pi8LdAtpJ0HDyVJfx7kRaxSWWq-M0ls7V1u-lCFQePLqDT0SA7mfw0_P6S2WNhrZujfvszhV8ofVPvdOKSr18qLMNb7gru8DXvmHJ8uYWK3l5RL-U86pF60npfnfLQko0ejOWtAijupWqhlEp--pc3QaFhZIBwiFNmjEK0hJrBHN9wrnf0BSzZlzaZTK60g1i-6zyIsHWV5byDlQ_WdcmIuXUM3XGWPm44htTwkaY3W-0ccvxjSW_r0pM9ha-2plLvTba0C8rWZKUDsuhJLLASxNhHld1QNPh02sXl3kYelZ-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات پهپادی اوکراین به روسیه، هفت کشته برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/135357" target="_blank">📅 15:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135356">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رویترز : حملات پهپادی اوکراین به روسیه، هفت کشته برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/135356" target="_blank">📅 15:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135355">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
شبکه "فاکس نیوز": نیروهای ویژه ارتش آمریکا سال‌هاست که برای ورود زمینی به ایران آموزش می‌بینند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/135355" target="_blank">📅 15:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135354">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پزشکیان: من واسه وطنم هر موقع شبانه روز که جلسه بزارن شرکت میکنم و مشکلاتو حل میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/135354" target="_blank">📅 15:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135353">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ایرنا: در جریان عملیات عمرانی نزدیک بیمارستان دی در میدان ونک تهران، بر اثر ترک در انشعاب لوله ی گاز، انفجار رخ داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/135353" target="_blank">📅 14:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135352">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رویترز: کویت دیشب یکی از بدترین شب‌های خود را سپری کرد
🔴
خبرگزاری رویترز گزارش داد که کویت یکی از بدترین شب‌های خود را از زمان آغاز درگیری‌ها در خاورمیانه، در جریان حملات تلافی‌جویانه ایران سپری کرده است.
🔴
در این گزارش آمده است، در جریان این حملات، دومین نیروگاه تولید برق در کویت طی دو روز گذشته هدف قرار گرفته و حریم هوایی این کشور نیز بسته شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135352" target="_blank">📅 14:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135351">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
۱۱۶ دکل مخابراتی هرمزگان در حملات آمریکا از مدار خارج شد /تلفن ثابت، همراه و اینترنت ‌با قطعی مواجه است‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/135351" target="_blank">📅 14:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135350">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO-RSdPD4Vbd1Lib8QMxywU3FYxJMhvrt0LH0kKpFeSn-M1twgAGaK-akhomGSqAO1zX5L31v7AIJWoVUnB0kITdqmHh8uXoJZYRoKxDql3xzXr_KXRw5yH2rISwWiDiU8V6-pSbilsb7YJ70ho_C3xYzgUGVMRWLCChTe0XEYgTL5n9C8ymd2TLY58uvd3MsUZO0xhuUaeChdydMzQv8Zso6Z9WNm1qQltmvklOlsciXRG793bWZZS0C3oV4sq_F-24lDh7ZACVyJa56L7E4ltVTIH8P5wHKmykDRgKKkEulVq8qhrGqqxFgNqmPMf1t-raCq059ypWn9ZOJilhSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمیدرضا مقدم فر، مشاور فرهنگی فرمانده کل سپاه: اگر آمریکا بخواهد از طریق دریایی و اقتصادی ما را تحت فشار قرار دهد، هزینه انرژی و اقتصادی آن را اروپا پرداخت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135350" target="_blank">📅 14:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رئیس جمهور عراق حملات ایران به اربیل در کردستان عراق را به شدت محکوم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135349" target="_blank">📅 14:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-h9WaDBK_z7qOEeIYSbjgdcQgQkk55ImC1ngI29HvElksCx5_8rOLQIJIumL1zvEHcSBV9OV_O04LwUBDik2PFwNtRtfpxOyh8qTcVPXQQKLWGOR40-4iAmDGneNFbD58aNQonQCOssGt0H0AWV5lWmL8QIFO8U6npWg7Ukl2ZhUmLcEERDY17kkZzWx6W6S_ZnN70Aq8K7TUXWvXKr4kKVZlTWxZBYeyyhtvd0wif7J6DnyJtHMJpm27QxNl6DWKcG8YR_NQEn0YC8RlLmlyLaWjrCwgheqGeS569rZwugnedTXQN1Qt_frZ6X7CBJ8gFKvCy68zewuyEs5SV_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از رد موشک های ایرانی در آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135348" target="_blank">📅 14:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135347">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
جنگنده های عراقی ، حملات هوایی را علیه پایگاه‌های داعش در منطقه روا در استان الانبار انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135347" target="_blank">📅 14:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135346">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری/العربیه، یک مقام آمریکایی:
ترامپ به ایران فرصتی داد تا تصمیمات درستی بگیرد، اما آنها تصمیمات اشتباهی را انتخاب کردند و عواقب سختی به زودی خواهد آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135346" target="_blank">📅 14:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135345">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
خداوندا بزرگیت رو شکر که هرکی مرگ کسی رو خواست، سر خودش آوردی.</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135345" target="_blank">📅 14:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135344">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN7HxrjrFZmg5wtBGA_pI1gxOQTv9SiEYVd4tpGVGoJodL7Qq8aTUThn-zS5AOtuI0Iu_vJep1-thfvwdR3v4G_hx05DeXXInwfc1rPuw6HcLI3d1xqGqTBQdq45nGFpFO2h1bMsqE4xPyf8_P_Zj_UGZZxHMHGjKh__orsMOg6lI7fMijdc72E0JY7_DRLUCjaSb-jaDaSKf6_jCSkBrrUKLfQeL11vZ-2LQiEnw-jbqY1OTjmvhWsagq5hY0cOEzwsQxk5Yu1k_ipwvEzBNMj8fa607IWNBhh5iJ6jifmD8HVCITRwixmR4lL3zGwJsBn4ziYmAsxU1fcsjo0BcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: اژه‌ای و قالیباف با تمام توان برای احقاق حق ملت در کنار دولت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135344" target="_blank">📅 14:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135343">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0375faeb3d.mp4?token=SIkwlvfGhr_KaiZ8Co95A-oRczxxseTLLgMm85oc5FkxudHUA058n1VcBN2CWhNVutARodVA2H8RQU6PypZvUMupv-s0xXFwmYj84rOLKxPCzlwIxEBNePgJFAdlMVjEooYLidqVks5EL4fSFNvzKFsepawKnAhLmTgQFSOmdd02LY_pHXpL21OVZ7_kxyo8H1fT2-1nM6Nv1_3Qivjdao-u937Sw7QUnuoALpRpY3bXSZQM-FO_s6A76_zFFmpRIptsg31cPg_GUwLnprTjqCnjjiDeAr7Vs6xsRaEJoIBzBCUEtnaIO32a9SIdmLgWZi8VDzKQqsYlED4eWl47GxY9wveOc4m15i_SZoQBpmLC5AAaayXdiTjeH4llZsD88Cb2aV0zfVTLDGTwDO7DHTK50g9Slsb2kOjUMikTfe5kQVx4rSRpkXYhJFaWLvzdlTnmNd4KvHFEwUZ_YMf194kjNn42jN51L_IGxZlhU6J9EDK_J1HdfoeFXoSBJDT7esf5YkUocnNPsaFDp6cmhlQg5GcEvkJziOyoWgGeuMABJx3lktLtbtjF7lBqogRIMtOEDwtn-uXKdIa6JsIv7CAHTejUHDEdXKOqPFHEKmR9oyFTXLUMJsYpG74nEHT2F_fCkntSM-fTpv9uY0KmszJyhsyWY2nl3M4v4Y5AEWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0375faeb3d.mp4?token=SIkwlvfGhr_KaiZ8Co95A-oRczxxseTLLgMm85oc5FkxudHUA058n1VcBN2CWhNVutARodVA2H8RQU6PypZvUMupv-s0xXFwmYj84rOLKxPCzlwIxEBNePgJFAdlMVjEooYLidqVks5EL4fSFNvzKFsepawKnAhLmTgQFSOmdd02LY_pHXpL21OVZ7_kxyo8H1fT2-1nM6Nv1_3Qivjdao-u937Sw7QUnuoALpRpY3bXSZQM-FO_s6A76_zFFmpRIptsg31cPg_GUwLnprTjqCnjjiDeAr7Vs6xsRaEJoIBzBCUEtnaIO32a9SIdmLgWZi8VDzKQqsYlED4eWl47GxY9wveOc4m15i_SZoQBpmLC5AAaayXdiTjeH4llZsD88Cb2aV0zfVTLDGTwDO7DHTK50g9Slsb2kOjUMikTfe5kQVx4rSRpkXYhJFaWLvzdlTnmNd4KvHFEwUZ_YMf194kjNn42jN51L_IGxZlhU6J9EDK_J1HdfoeFXoSBJDT7esf5YkUocnNPsaFDp6cmhlQg5GcEvkJziOyoWgGeuMABJx3lktLtbtjF7lBqogRIMtOEDwtn-uXKdIa6JsIv7CAHTejUHDEdXKOqPFHEKmR9oyFTXLUMJsYpG74nEHT2F_fCkntSM-fTpv9uY0KmszJyhsyWY2nl3M4v4Y5AEWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک ایرانی در آسمان اردن
‎‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135343" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135342">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وای نت: 10 هواپیمای سوخت رسان دیگر آمریکایی تا امشب وارد اسرائیل خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135342" target="_blank">📅 14:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135341">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / معاریو:"اسرائیل" و ایالات متحده، سطح آمادگی خود را برای از سرگیری جنگ علیه ایران افزایش دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135341" target="_blank">📅 14:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135340">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قیمت دلار به ۱۹۳۰۰۰ تومن رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135340" target="_blank">📅 14:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135339">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رویترز: بر اساس گزارش‌ها، نخستین تماس بین‌المللی مجتبی خامنه‌ای، رهبر جدید ایران، ممکن است گفتگوی تلفنی یا دیدار با ولادیمیر پوتین، رئیس‌جمهور روسیه باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135339" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135338">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ثبت سفارش جدید خودروهای وارداتی متوقف شد
🔴
دبیر انجمن واردکنندگان خودرو ایران:واردات فعلی از محل مجوزهای ثبت سفارش سال گذشته انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135338" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135337">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
شرکت ملی نفت کویت اعلام کرد حملات مکرر ایران به تأسیسات حیاتی بخش نفت این کشور، موجب مجروح شدن افراد و وارد شدن خسارات مادی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135337" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ارتش اردن: چهار پهپاد که وارد حریم هوایی اردن شده بودند را رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135336" target="_blank">📅 13:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135335">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت نفت کویت:  خسارات مالی سنگین در پی حمله‌ به یک تأسیسات نفتی‌مان رخ داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135335" target="_blank">📅 13:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135334">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
پولتیکو: «آیپک» یا کمیته امور عمومی آمریکا و اسرائیل، کمک‌های مالی به بیش از ۱۲ عضو دموکرات مجلس نمایندگان را که از کاهش کمک‌ها به تل‌آویو حمایت کرده بودند، تعلیق کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/135334" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135333">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
دبیرکل سازمان ملل : نسبت به حمله به زیرساخت‌های غیرنظامی ابراز نگرانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135333" target="_blank">📅 13:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135332">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اژیر خطر در شهر الازرق اردن به صدا درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135332" target="_blank">📅 13:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135331">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97983fad64.mp4?token=deKCmM0dJFIHrL_wuzEY3Jjlso-3pMrBPNDH-DZcJvDiKbtzr-wZgYCmNvrh7VjaHTJ1pVYMlywqVt7SfXI9KJs6LtSlGm99JKl4DcYtkZ6dlFNOqpYFOSMDy4h6Qjagr-pjWTknZYV84lKHhQ6rx895Ae2ZXyoL0rSdTYPwETBKABH1ncrfYnZdyzHhHKeXCsJf2MdEe5pnpqFldNCjZFRmX6mdDOOh0VhvDiXLAvnKNkR8fq6TBEyWk0nND9B-Vm7xfjh6tPOS4B0S1LrFAiw8ucTIgWymjd-VCC4jBhPG75F-EZRA-gs5M88O52bhFDfJwwNEmg0Xf8gnQB-2xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97983fad64.mp4?token=deKCmM0dJFIHrL_wuzEY3Jjlso-3pMrBPNDH-DZcJvDiKbtzr-wZgYCmNvrh7VjaHTJ1pVYMlywqVt7SfXI9KJs6LtSlGm99JKl4DcYtkZ6dlFNOqpYFOSMDy4h6Qjagr-pjWTknZYV84lKHhQ6rx895Ae2ZXyoL0rSdTYPwETBKABH1ncrfYnZdyzHhHKeXCsJf2MdEe5pnpqFldNCjZFRmX6mdDOOh0VhvDiXLAvnKNkR8fq6TBEyWk0nND9B-Vm7xfjh6tPOS4B0S1LrFAiw8ucTIgWymjd-VCC4jBhPG75F-EZRA-gs5M88O52bhFDfJwwNEmg0Xf8gnQB-2xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز های متعدد هواپيماهاي آمریکایی در ۲۴ گذشته از اروپا به خاورمیانه
🔴
این جابجایی ها خبر از یک درگیری شدید در روزهای آینده می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/135331" target="_blank">📅 13:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135330">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
اژیر خطر در شهر الازرق اردن به صدا درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/135330" target="_blank">📅 13:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eRTmcx02jPVaeQQm9NiPyJM1RQccrRdCD_rH8FndIwq3z77uAWAxAxomMSNH3qQ90Mx-DeixsZtnhACJ90_DIzlXGaZGNCMmcuWmuVW8xqLurnd6nXpW4hm09AWia0DetI8MVHp-FTMqKzs0qLzfuRcs-Za27EM8-iI6YH6n8Asymt02zfNYteZ3f_JFfIoGVRqvQjOyzf7cENts7F59b4yFhP_k2n9r9zeK1zbwefELZJW_GYuJ9vjB52jg-9GLLqG6q8AJ1pkIZjfErZAlkJ6y025jKYS9SbguqvrqfHMKC6_YWo6rjint74JtrH-MwuQgxgzS_9J79VxZHtRa6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ER0-kyUONoq2n3hOLDbmvsBpwkdOSkhhTNYIPPuLCsypDuFBWXYL1Oqzg3uQdwemymwLu9cu6FI8WnPqrsdfQ2kgDinCF_ZP3PZRecHL67L6tGkOw5ImcPvR-e3iW5IB9z_BUsQAj9I-VflTx8h2xe2Xl4ohmFKqRPB-bI_gdmAZso_M3P7hG2VDe8DdR-uEcFP2Tfemzo7FdJV_8mfQzBqoFNUb5tYQwh8HC6SEhZb3yczA19v_UwU3FPBFsfDOj-JaVeVvMnW_b_vFefKhpvscsHS_lx9q6u_VGG-rkwQ8QUQ2cZWOndignLVII0F1Pe3YuNUh_sIIes7qkkGl0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از موج جدید حملات موشکی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135328" target="_blank">📅 13:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
عراق ۶۰ میلیارد دلار قرارداد انرژی با شرکت‌های آمریکایی امضا کرد
🔴
در نشست تجاری آمریکا-عراق، شرکت‌های انرژی غربی ده‌ها توافقنامه نفت، گاز و خطوط لوله با عراق امضا کردند. بغداد به دنبال تقویت روابط با واشنگتن و توسعه مسیرهای صادراتی جایگزین برای دور زدن تنگه هرمز است.
🔴
شورون قصد دارد در خط لوله‌ای از عراق به سواحل مدیترانه سوریه سرمایه‌گذاری کند. کونوکو فیلیپس نیز ۴۲ درصد سهام «بی‌پی انرژی کرکوک» را خریداری کرده و به بازسازی چهار میدان نفتی شمال عراق می‌پیوندد.
🔴
نخست‌وزیر عراق تأکید کرد بغداد از سیاست درهای باز برای جذب سرمایه‌گذاری استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135327" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
موج جدید حملات موشکی از ایران به مواضع آمریکا در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135326" target="_blank">📅 13:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فؤاد حسین، وزیر امور خارجه عراق، در گفت‌وگو با Rudaw English گفت که علی الزیدی، نخست‌وزیر عراق، پس از سفر به واشنگتن برای گفت‌وگو با مقام‌های ایرانی راهی تهران خواهد شد.
🔴
نخست‌وزیر عراق در مسیر بازگشت از واشنگتن، ابتدا به قطر سفر می‌کند تا در مراسم تشییع جنازه شرکت کند و سپس برای گفت‌وگو با مقام‌های ایرانی عازم تهران خواهد شد.
🔴
روداو همچنین مطلع شده است که علی الزیدی پس از سفر به ایران، در ادامه یک تور دیپلماتیک منطقه‌ای، به ترکیه نیز سفر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135325" target="_blank">📅 13:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
العربیه به نقل از یک مقام ایرانی: مجتبی خامنه‌ای تا پایان جنگ در انظار عمومی ظاهر نمیشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135324" target="_blank">📅 13:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گزارش شلیک موشک از لرستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135323" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135319">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSXNRlRaRScYwK0B-hepB6IhiCfG2kF1gJVBGQXdg1ZGyjpR_sTaQKOzMPxyAtsQmRYvvErj3jcZxgnvmbTn4dFZBUV89GJahbILnyICrkm5JZhgMe6yUsEE4z5ZdfVx-sEQxY2h7vojLd2Xvj588yArVz5NC5Fcf8XmQSnF5tqcePtPSKwlQihf8p-Bs-AWJd80iTy4JcpI9nbdhoIGUL3nk1RxYNfge3205YfXNQs3NhRtBMRRksck3xz1vcF72YejZlR5bFVbMe7lPav7YvYXqD86oWapw7fmPoszztAmMssfSaDiqe97M7Ittv4yOFzXdK5Uuh8v9L8tQO6f7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mkEnuDMqr56E5rS-Vm5WrPvRPvD56XEEE_cJYURmxbj3hi99gYI3m_HU_5_LBWPMcNtOD17f-eFmPCBwZAkhOstnAfiyC9O5Mey6-sq-8aLCROXqAQq5_GmmO_CGRahj55gYY2wS7BNxO9fh5e8ueKgtmSUJensY2PAPsV7VzjlS0Kdjc8UW3nfuI8S56YyQw3mn8KE2DgHtTScU9NTSa40hfW_BCYKA1wKPmgedWG3GH6zIvKrXbms1JX7IX1A-4qqMcoeFDoeRgTQJxz-8mkJzIvXyqB6JNmGvzVNYfQvxHqGQL8OnH7fBOF0Xf9uHbmycXwhveygOSRW4s1qpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_IOUoNjqPXdkfHlGN-bvihy45ij0qaoeUVa4rjOUNSzmRod3wgYFUesBP8zF7qkdbif_8rybif8glQVauUvlD9cFWLWSmqn3dSodGcVjMf6myORvWBdmk-BBbnFVmdAcpV1TP0zw-29x-7wnN0i2al1_auQZVObyrmgnyaR3NZs2Y3Z7dgemBb530HAel3Z4XAOikYct9UYTCGP-rWSwBXvwFAn8G-qGmts369vI44jIf5_RpIWxPLkm6BwBmHcwaZdEqCd9KeKGmN9kCvEwXwQF3kz1XM2plU67AiAJSQxzjY79aRpj-hUFgqT7PuDG2ahjWOjMRWxNncnK-z5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PEj_DLfbieQ-Kp54JvsOvIg_knolv4hcDPKehzzseA3a27RxgK3p7X2Atw_-i45t9ZKDvSXwTqDqoFbvUumh6X8ish5AsGoZH2OlX2nVj6WQa0zKi-xJ4SquxidxJf9n9s-ApPvPS25qN1rks7J59vdAyP8WdVzR1toUIyGTCs4CIVnZf3_7pSoJlAfZY-VPMi9pEdQU1NB0bv_8xketJHGgvtcecUXYJ_oxU6vXTXwl6oCPKtf7nfZ6e3oVl2IrcYAdMpcsMhmiNnsgWcK9Wpo9nQpu05WY4P_3fKO95JF7VI_MZLrO9OGWW4-1pA9Rjw8AomH7jS0HQmZkR9-iyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک آتش‌سوزی بزرگ در منطقه کروکستادلوا، در شهر درامن، واقع در جنوب نروژ، بیش از 100 خانه را تخریب کرده و باعث تخلیه بیش از 400 نفر شده است.
🔴
این آتش‌سوزی که از دیروز آغاز شده، از مناطق مسکونی به جنگل‌های اطراف گسترش یافته و همچنان مهار نشده است.
🔴
حدود 100 آتش‌نشان از ایستگاه‌های مختلف، به همراه نیروهای مسلح، سازمان دفاع مدنی و هلیکوپترها، در عملیات اطفاء حریق مشارکت دارند.
🔴
چندین نفر دچار مسمومیت ناشی از دود شده‌اند، اما هنوز هیچ مورد فوتی گزارش نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135319" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135318">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GotrTd0xHM2Xq7ZarLQaMX888POUkkbgEpNenF0hynCKX_TUAxxRfQ_2ECF2qD43SVR7rihW5kwn0QwYxt3G1RidRZtk38BuIchYVaO8LhLFHrQ91TQHHmiJY-oBI8ypnZhN8rbHVkXDjgtAtOJydYp7RPeXWIPD-4rQV7rzlVZKq48LrYGTtbsiPTPNo3SnXN6aHB8fLmj7vuLlblRlQ2cr5VSg8PT1O7n5ZNkCYzzz1NcN9jmULVn4S0EFNkqu2O7bLneLAkiwKuBIod541G9qgjeahNOePb4JvDuPoJ18bFIDrQDCud29L6IexVd71UrLnffsFxrJii8sPpLCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل: آمریکا هواپیماهای سوخت‌رسان بیشتری به این کشور اعزام می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/135318" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135317">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بلومبرگ: قیمت بنزین در ایالات متحده با تشدید رویارویی بین ایران و آمریکا، بار دیگر به نزدیکی ۴ دلار در هر گالن رسیده
🔴
قیمت‌ها تنها طی ۱۰ روز، حدود ۲۰ سنت افزایش یافته
🔴
در حالی که بخش قابل توجهی از ظرفیت تولید پالایشگاه‌های روسیه از دست رفته، پالایشگاه‌های آمریکایی بیشتر به تولید سوخت جت و گازوئیل توجه دارند تا بنزین خودرو‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135317" target="_blank">📅 12:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135316">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
دقایقی پیش؛ دو انفجار در نزدیکی فرودگاه بین‌المللی اربیل کردستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135316" target="_blank">📅 12:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135315">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اتحادیه اروپا (EASA) با تشدید دوباره تنش‌های نظامی در منطقه، هشدار امنیتی خود برای شرکت‌های هواپیمایی را به‌روزرسانی و توصیه کرده است ایرلاین‌های اروپایی تا ۲۹ ژوئیه از پرواز در حریم هوایی بحرین، کویت، قطر، امارات و فراز خلیج عمان خودداری کنند. همچنین توصیه قبلی مبنی بر عدم پرواز بر فراز ایران، عراق و لبنان نیز تا پایان ماه اوت تمدید شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135315" target="_blank">📅 12:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135314">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbTuMdYvoqA5oV6ugs00MpUaMD4vDnyji5YcDxczXnSm_6_xxIHGhibo3DlAPwHOC1sR22KnQDoBDc8iMc21L7qjml9MaLjWGA41nwbBzgZc0yt8fH06YZ845bcs_rXwWEizttqq5c3WsDBaB3lRv4Jiky4NNwDNB3_bGdn4rv8BezLPdX-bioI03YCyC9m87xWCI24tIqTg7S0HXx0S4PLigoqOLtvD5lil5IQhgTt8ja2o_mfLa5QbObrML1D6SjCbD383IvGrZB7dj0SoCC5aWUfkzEk1NiH7WNxyF0lLh5DLzuJVlks0Qk7zdQTfowd4MRIVrGvRkXDBNGNjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۲۱ هزار واحدی به ۴ میلیون و ۷۷۳ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135314" target="_blank">📅 12:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135313">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
معین الدین سعیدی، نماینده سابق چابهار:
نمایندگانی که بر جنگ تأکید دارند و شعار میدهند لطفا زودتر به جنوب بیایند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135313" target="_blank">📅 12:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135312">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqCZSJMlotHrNCk7tyJjH6o7TW-RqYdi-BP5cBd2utktXkmi3PgGNixa50tOt6hBJxAjtSH3KwSYWev8XkcFvLl2FeLoN7z8jDKmN5kDrNG4XUQ-npzEzlnfqMgqKtKrqV9gLubFzSMOzi7BT7y2gIy7ju33__Ggks_WFjNfyoo7I-gJ5V1qkudKyNOa8UH_ciOw3RUGQX4IFoQaE_fQ-U9bvLVDkGCWmzg23X93XFRzY_STSqlFFl337ir0sOd1UFlGWXLbutJ6rLULCZGSIqmEXtTG_jcy91Zt_FUIprFuEhTEoVkBytRGxUabR9HVwhPWs4vjxTazIUJH-eTffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات جدید اسرائیل به خان یونس در جنوب نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135312" target="_blank">📅 12:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135311">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس جمهوری اوکراین: تأسیسات انرژی در خاک روسیه را هدف قرار دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135311" target="_blank">📅 12:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135310">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزارت خارجه آمریکا هشدار سفر به کشورهای بحرین، لبنان، مصر، عمان، ایران، قطر، عراق، عربستان سعودی، اسرائیل، سوریه، اردن، امارات متحده عربی، کویت و یمن اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135310" target="_blank">📅 12:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135309">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d04de4038.mp4?token=sjfkxs0wHJv40wzh7cPDrjAx5iABA0lkwjvSYERNIRXt95bM9NM50TEWfYBXo3g6JfYFyj0iNk_P8FH5KcjIk6rMQdXlg6XaJTsfw3Z5LO3w6Z2dExHWko3Z0xPPK0xIsVD_4C11wEx3IUwy5QVTYyawGWecMhLQTqerA2BotVYab_RiJYYAtt4aK1DRx5YvA0tnbjhJ8QQR_EN2km3CaTeaKH7oy9EeE9c-FCAsqKvJjZMl24wadm2C5u3m7On_ePfb9Yi87ZEX6RTlJUXto3BE8EpKqeaLYuMNiseAEc-oUvT4YMixaNq6m6a1w46lv1TgRt0oMqD2kQGr9u2bRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d04de4038.mp4?token=sjfkxs0wHJv40wzh7cPDrjAx5iABA0lkwjvSYERNIRXt95bM9NM50TEWfYBXo3g6JfYFyj0iNk_P8FH5KcjIk6rMQdXlg6XaJTsfw3Z5LO3w6Z2dExHWko3Z0xPPK0xIsVD_4C11wEx3IUwy5QVTYyawGWecMhLQTqerA2BotVYab_RiJYYAtt4aK1DRx5YvA0tnbjhJ8QQR_EN2km3CaTeaKH7oy9EeE9c-FCAsqKvJjZMl24wadm2C5u3m7On_ePfb9Yi87ZEX6RTlJUXto3BE8EpKqeaLYuMNiseAEc-oUvT4YMixaNq6m6a1w46lv1TgRt0oMqD2kQGr9u2bRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تردد در جادهٔ بندرعباس به رودان نیز که بامداد امروز مورد حملهٔ آمریکا قرار گرفت، از سر گرفته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135309" target="_blank">📅 12:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135308">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ضرب الاجل فیلد مارشال محسن رضایی برای آمریکا : آمریکایی‌ها فقط 48 ساعت فرصت دارند که به دیپلماسی بازگردند بعد از این زمان، دیگر فرصت دیپلماسی به پایان رسیده و نوبت به جنگ بی‌امان خواهد رسید که تبعات ویرانگرش را نه تنها مردم منطقه، که همه کشورهای جهان خواهند دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135308" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135307">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b779c493.mp4?token=ALtOkdBFangLyqS4syCmV8rHomV6EruODPH1JZ8dDw_CPdQ6zZSk65vdInqU6Jn5B9opLLxt8tYSZxhImZaH_qTXG0wGIT075kdAuVL0Y23txo6jJz9y8JMDszC1Cy1EBwE3jHGGpb3DXdHHsEti_a_E43Tr-OK3P2Dx7EviFXrmhuI-y-OM66-bgT0BPrjzeZrWiBlzahAQv_Jo5bN4CJwnrdvu720dhyOqWIbW5Bn0aC90Ixe5CskTmPO442tTyedLx8K3x7oa1_KcfOFwwI4cfLZHK9w7x_Og8tsbC6UjKTJOA6hjV85iVngbhQ99Ifj7F843pNICoQzEQNmD-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b779c493.mp4?token=ALtOkdBFangLyqS4syCmV8rHomV6EruODPH1JZ8dDw_CPdQ6zZSk65vdInqU6Jn5B9opLLxt8tYSZxhImZaH_qTXG0wGIT075kdAuVL0Y23txo6jJz9y8JMDszC1Cy1EBwE3jHGGpb3DXdHHsEti_a_E43Tr-OK3P2Dx7EviFXrmhuI-y-OM66-bgT0BPrjzeZrWiBlzahAQv_Jo5bN4CJwnrdvu720dhyOqWIbW5Bn0aC90Ixe5CskTmPO442tTyedLx8K3x7oa1_KcfOFwwI4cfLZHK9w7x_Og8tsbC6UjKTJOA6hjV85iVngbhQ99Ifj7F843pNICoQzEQNmD-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی به بزرگ‌ترین مرکز پردازش سفارش‌ها «وایلدبریز» (Wildberries) — بزرگ‌ترین خرده‌فروش تجارت الکترونیک روسیه — در منطقه مسکو حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135307" target="_blank">📅 12:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135306">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIBMjKriJLbzKGtYl0yheDbERznCAQ07spMH9ojpoD1WtB4-49mzpcR2lATy0J_olcViuUtKRtwMCLAvxFA-CxeA0iljnRv0NOjfNpSlal-IuWSIJOCuhVD6DUTyz9FEfEopETHZ1JGpUpwbvQ_O_cMamcwU6_8x2MGU3m8OK1ereu2et4Lb9oQwNmHr5lzX-SNBCJG_gR4YTPWN66Mj5v4ke0UVHaXPDucQfLyt01m2QrvDIat2NGUIIPzC3AM-znobuF_VjpNwuKceglYK8S-l9LYQ69zYRbSNBdeq2GHKaxckBMscXnPOpcI_Xll_elZUiJGUUSZwyv8hJjFvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد قربانیان دو زلزله‌ای که ماه گذشته در ونزوئلا رخ داد، به 5069 نفر افزایش یافته است.
🔴
16740 نفر مجروح شدند، در حالی که بیش از 128000 خانواده کمک‌های لازم را دریافت کردند.
🔴
این زلزله‌ها به 856 ساختمان آسیب رساندند، که از این تعداد، 190 ساختمان کاملاً تخریب شدند و هزاران نفر بی‌خانمان شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135306" target="_blank">📅 12:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135305">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی قوه قضاییه: برای ترامپ و نتانیاهو پرونده قضایی تشکیل دادیم و کیفرخواست اونا صادر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135305" target="_blank">📅 11:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135304">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a265df119.mp4?token=mk7H4mrQiMkBIUx9zD5kXia5lyFlAf6TpPJHQp2uzhsuSUMhU49Grx3k6rUtFnBr0kxRXfJ_Kh4lh9AlTaMPeYED8tNyrhcN6v6tRFGhrXFyhyuPne-2Ws6dSJIatown-L6Xt0EcwnJjxYUXnBD_ugzKoGSObcYtJGzl_johmAAfqlQNsQIYg0riGcUMt6KzU3PQ9RIm-gVq1OrIO78uLSbcat0hZTDVDlQiS0_BprMFqD3o-DxV-UsQg0JR1ncXUlOTv1Zd2_l9eZmxk8YmleS3lfqkKtn-UYVRb4SB4hvC2eAmsQATc92nqOiAO-Z8Tda0n9Bk1-ss3ddxltLIFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a265df119.mp4?token=mk7H4mrQiMkBIUx9zD5kXia5lyFlAf6TpPJHQp2uzhsuSUMhU49Grx3k6rUtFnBr0kxRXfJ_Kh4lh9AlTaMPeYED8tNyrhcN6v6tRFGhrXFyhyuPne-2Ws6dSJIatown-L6Xt0EcwnJjxYUXnBD_ugzKoGSObcYtJGzl_johmAAfqlQNsQIYg0riGcUMt6KzU3PQ9RIm-gVq1OrIO78uLSbcat0hZTDVDlQiS0_BprMFqD3o-DxV-UsQg0JR1ncXUlOTv1Zd2_l9eZmxk8YmleS3lfqkKtn-UYVRb4SB4hvC2eAmsQATc92nqOiAO-Z8Tda0n9Bk1-ss3ddxltLIFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوووووووری/ترامپ ترور شد
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135304" target="_blank">📅 11:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135303">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
دست کم ۴ اصابت قطعی در پایگاه شیخ عیس بحرین گزارش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135303" target="_blank">📅 11:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135302">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e976fc0ba.mp4?token=ne8GUHXFTUv9QfanTrKRNmbOdVvTz1IXULpS-fXQbygmnVFIr43WQVfXNNlxXObpaoVpWkwECgT1ZkETGrRoJPEz1E19510mFbCINJrx-IR4-Sy0-Ho1OWlVjP6j8n734Y0Fvqwm6KioHar_dtuPZZhfAw5001Rb__jhEaR4XPH-WXY8mWsoCOIC4O4Sak0BrlRdVK_ddjo4n_o7oHxFm4JQ5JLR-6sCF53nqhjD5idhYgybDzDKRJ1QWP1TiRAC01Qs_tKJ2cJBS--v10Y9qtX2w1mmec5h7czHVe7roYrLrS9-ZIkZf9NSp_KMqzYl7fx1BWFgcQEuFzF7zLH88w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e976fc0ba.mp4?token=ne8GUHXFTUv9QfanTrKRNmbOdVvTz1IXULpS-fXQbygmnVFIr43WQVfXNNlxXObpaoVpWkwECgT1ZkETGrRoJPEz1E19510mFbCINJrx-IR4-Sy0-Ho1OWlVjP6j8n734Y0Fvqwm6KioHar_dtuPZZhfAw5001Rb__jhEaR4XPH-WXY8mWsoCOIC4O4Sak0BrlRdVK_ddjo4n_o7oHxFm4JQ5JLR-6sCF53nqhjD5idhYgybDzDKRJ1QWP1TiRAC01Qs_tKJ2cJBS--v10Y9qtX2w1mmec5h7czHVe7roYrLrS9-ZIkZf9NSp_KMqzYl7fx1BWFgcQEuFzF7zLH88w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاقی عجیب در مصاحبه با یک جانفدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135302" target="_blank">📅 11:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135301">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD0Dq6P-QUCMt7GPSIl74Gv5-Tw6Za551VmYm72vvMo8pkPaRP1J3Jzcv5zxfbjyYixB0w9crQF-KVyi_VPG3ixId-HztldPk9O4H9gDkhbH-XnF5uUJ76LpzT1X-ReC8C1gESRGqrjXVTDzUjpZcYdnmbgSBkp12dmTmZXiyLqvcb0jMlH1ElUROgRkQXHDtpaXF6QSaUBzDhFirpJs8FZyNiRJgbBcghWZ5vIeB_uuxO_0Mcb1HoJn4ElefCXv4Wo4O35t6SbWhxutlUBXRb_95EaUf3MXmUbilTGVUoJ0JhWs-rusqLW7W4WWLpy3jYr_k3I3k3HNnsVaNoXMDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه آتش‌سوزی ناسا (NASA firemap) آتش‌سوزی بزرگی را در پایگاه هوایی موفق السلطی در اردن نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135301" target="_blank">📅 11:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135300">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjHNRWU0X0gMuL7SHVeaRr0R6jXnuQ9lqfrBYzgFm8NmWb4NkWYihecHzxPuGzJXZXFM_Bub5ZjEdY2LUwX93uSgDWC12X6gIbctdB1NPUk5yGz5uoHl4IicnSTFM4n8hEt6RfJra1xMFXVCt3A3ZIPsGHsn_dnLyTvyjQvC_jyFfv7yjdteHFGFUAxtTjBboGkHWQCs34NqBHZPsT9qtSaUuTzdDLax6enzasGgugl6Lcs9ZBwehlBUKj_OggeG4e-AIydqOqNU1LNy0WAjzOprHIgW0y3jp8p5pHH4K4hyKq5bl7AXeqlzN8KNFbRW1Gn7U2nPYpeB5yxS71i_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاطمه مهاجرانی، سخنگوی دولت: دولت تا پای جان کنار مردم جنوبه و از صبر و ایستادگیشون تشکر میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135300" target="_blank">📅 11:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135299">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ارتش کویت :  یه نیروگاه و تأسیسات آب شیرین‌کنمون، به‌شدت آسیب دیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135299" target="_blank">📅 11:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135297">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmxyepIi6famyttEoW6tw8NNWYJ_ONzGGRUS-c6cLb_3c3z_R3Kp0gOTsM5UkBwHO1Sa_6RLcvi4kZXZPVXb1IP0gx7dgbYZo_nCWtN76zGwXxTRH3dvRicGrNGHP5XqdWPT1Ykln7etAtDt3faS9mPicCnsM1KDY2yqNmIz47klf0EbjSUY9MZYLjLx9M6QSFKIcqHU0ShBWS3xFjJuJUt6X8L51XVVAiHQ152DnIsBJmHnNpXn7Ugsp30THzk90qsQX_zqFINc8EhXRScvSeKfzhqNLcpXS5ucTBZOghRYI4x0EYmlZSgfdBGXindXWSZzDj8nSzHw_yWleviKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22fbca48f1.mp4?token=DcvqFsLwCgw0zFORfsd7sbzpPJXN-rBQQ64CEJpzI7gOZBqp5pc0JU-c8CC_VNwS7Fh8l6YbazPk0RO5Wrkm8qBgTz90LZkheNYGTZF0XvOAd8-2MQWxy4P345_Ubl3WUgXT69C1vopOI3aU3hDklgZTOY-IsOJ8to5IUDmnLcsJAZatrLZ3CjeBXQvZDHYAYsTxVYD6oCrPEDVHLXD-iOIabl5jA2AJ26mbAPyLcbZTUqiBikeFhnQg9XyjxiXY98x8klFwk057OpFxSVh5O84nadgR_6ajnT9mKmqgU-pQ4BnDQrO4T2IO2zWUusnUqsZtq0jm7YtTqv0cT2WGvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22fbca48f1.mp4?token=DcvqFsLwCgw0zFORfsd7sbzpPJXN-rBQQ64CEJpzI7gOZBqp5pc0JU-c8CC_VNwS7Fh8l6YbazPk0RO5Wrkm8qBgTz90LZkheNYGTZF0XvOAd8-2MQWxy4P345_Ubl3WUgXT69C1vopOI3aU3hDklgZTOY-IsOJ8to5IUDmnLcsJAZatrLZ3CjeBXQvZDHYAYsTxVYD6oCrPEDVHLXD-iOIabl5jA2AJ26mbAPyLcbZTUqiBikeFhnQg9XyjxiXY98x8klFwk057OpFxSVh5O84nadgR_6ajnT9mKmqgU-pQ4BnDQrO4T2IO2zWUusnUqsZtq0jm7YtTqv0cT2WGvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پس از حملات پهپادی امروز اوکراین، بخشی از شهر مسکو در روسیه زیر پوششی از ابرهای غلیظ، تیره و تقریباً بی‌حرکت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/135297" target="_blank">📅 11:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135296">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
گزارش انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135296" target="_blank">📅 11:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135295">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
از سرگیری پروازهای شیراز-دبی پس از ۵ ماه وقفه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135295" target="_blank">📅 11:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135294">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
قطع آب در بخش‌هایی از کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135294" target="_blank">📅 11:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135293">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3ab201d85.mp4?token=EHKdCPdZY2JO5BzbYmpkGFWuqdCMKdR_X3a7kxeCKl8yp92d1z2JUrh_Y3m5WePUJXVMuaBlzrrkBtsBspFMiawtss44wPOP4JmmlWS9Y_4fBM2PrKnebdTjBBFFW-wC9P0UCH7eqFa4Gk_Cm4XnPq56qf3Ti3GVt0KOliqly6uYwCwkl83KUT0ri_OBGZ5jDLI8L7amoT86YxmKsJZYQhNOD1Ns9wXWGt9Av9Q4xteQ9NNPzN2Y8CmSIMr5LFlg-ySG5yww_eaBAFsRR19Z2JTctbUqeuKpbo-JJwrVNT65empqNlGmzAtddHKgfoKNTF9-S2cMBX6a_RZI_lkcBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3ab201d85.mp4?token=EHKdCPdZY2JO5BzbYmpkGFWuqdCMKdR_X3a7kxeCKl8yp92d1z2JUrh_Y3m5WePUJXVMuaBlzrrkBtsBspFMiawtss44wPOP4JmmlWS9Y_4fBM2PrKnebdTjBBFFW-wC9P0UCH7eqFa4Gk_Cm4XnPq56qf3Ti3GVt0KOliqly6uYwCwkl83KUT0ri_OBGZ5jDLI8L7amoT86YxmKsJZYQhNOD1Ns9wXWGt9Av9Q4xteQ9NNPzN2Y8CmSIMr5LFlg-ySG5yww_eaBAFsRR19Z2JTctbUqeuKpbo-JJwrVNT65empqNlGmzAtddHKgfoKNTF9-S2cMBX6a_RZI_lkcBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون وزیر اسبق نفت: آمریکا در کویت و بحرین مزدورانی را با حقوق‌های بسیار بالا استخدام کرده که به ایران حمله زمینی کنند. البته این افراد فعلا آمادگی جنگیدن در دمای ۶۰ درجه جنوب ایران را ندارند و منتظرند تا در هوای خنک وارد خاک ایران شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135293" target="_blank">📅 11:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135292">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر خارجه عراق: عراق تحت فشار است تا وارد جنگ [در منطقه] شود
🔴
مخالف درگیری‌ها، ادامه و گسترش آن هستیم
🔴
از زمان آغاز جنگ، نفت صادر نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135292" target="_blank">📅 11:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135291">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjTLsH4NexnJetgCmz_thUd0m6Zl4vw8-hVDmw1KFgLgZRnt2Qp47PFd-tmCMXUBC53CvqvH8AeqS4154VZz5OQsZ8AvntD9o5Ix3zRkjcAz4jfRZ7fjYbXR-N6Doi1gcwFlZ46lE7XkVNzCEnQ_eVdZVvchBq3-1oMdtr6EXR3i78T2tSf8di_coNRqFGlidcAXvbsqJ98v5HTQduPFTUBtGvux4vEPkLX_fiUbMnr1tDgiFcpe5_IY8ta3nhxohY8DlHPhGtVETaaMd0KCDrnsV7whij3LT09m1DYKh119xDXgQTYoM80h79-cG1y6eN8c6qg5xwleZ4nmhi0fxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: قطر قرار بود ۶میلیارد دلاری که از کره وارد این کشور گردید را به علاوه‌ی ۶میلیارد دلارِ دیگر _جمعا ۱۲میلیارد دلار_ در گام اولِ تفاهمنامه برای ایران آزاد کند
🔴
اولی را اوفک (دفتر کنترل داراییِ خارجیِ وزارت خزانه‌داری آمریکا) مستقیما جلویش را گرفت و دومی را نیز خود قطر همراهی نکرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135291" target="_blank">📅 11:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135290">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e463366e51.mp4?token=YAs9iN5UJVL2GEbsuvb9Zh2CZpPrqcoZIiIiXfr_tW2K7jehb9TdKUvtDwSVo1aOBMPIDPmS6jB_qhgQ_cFvyCGN2a5cXWdwZE3RqZ98Ib-JtoZ1oekSlDvLnSU1z80NhoQSW1IjDkw3e3swW4jOxeFKTiD0dF8G9sbXdxj_9lhVaxgv1__dsvA4yuklF2zIfPUVzzriXJ3n8Np7f5S-52BwPnIdllILvqvEwRIBJSRp8t9UBZf5bLf2bBy9ePBzmWdKSK7_1tRU09rSDEQAM_ZWSZSo_809CUS-bPrluMrBAk2K5LYcbSuJLYxI8D2ToV7L9qpMqAvXCdw7gRqYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e463366e51.mp4?token=YAs9iN5UJVL2GEbsuvb9Zh2CZpPrqcoZIiIiXfr_tW2K7jehb9TdKUvtDwSVo1aOBMPIDPmS6jB_qhgQ_cFvyCGN2a5cXWdwZE3RqZ98Ib-JtoZ1oekSlDvLnSU1z80NhoQSW1IjDkw3e3swW4jOxeFKTiD0dF8G9sbXdxj_9lhVaxgv1__dsvA4yuklF2zIfPUVzzriXJ3n8Np7f5S-52BwPnIdllILvqvEwRIBJSRp8t9UBZf5bLf2bBy9ePBzmWdKSK7_1tRU09rSDEQAM_ZWSZSo_809CUS-bPrluMrBAk2K5LYcbSuJLYxI8D2ToV7L9qpMqAvXCdw7gRqYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اچ‌اف‌آر: تنها مسیر فعال در تنگهٔ هرمز مسیر ایران است
🔴
موسسهٔ تحلیلی در بخش نفت‌وگاز: آمریکا در صورت واگذاری تنگهٔ هرمز به ایران، این کشور را به قدرتمندترین بازیگر نفت جهان تبدیل خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135290" target="_blank">📅 11:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135289">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
منابع خبری از فعال شدن مستمر آژیرهای هشدار در بحرین خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/135289" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135287">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c7774f4f.mp4?token=QL6glVt8jQxh9BtzP7jLl_ErkKp6ZjDxJKzzVFapCRpehGGnzVvGWvwKJUUebec8oY_k7Mvp1uTSZmjsIlGbNU2gdbCVRiuQ6kqKyaBc4GymR3Qv2Sp0VOYnVJPsbyxS8kHBpV03RBaGirtw3FC2rFhnu7IpQLybKquZ86vVrebea59jecc0WQOGKY6khy1I6XXxe1RNSEmpzSYtaKFGoSIzHJOnvP_Tkzz7fYR_GOUmEafsHR5vq7FUjma2BJPgUX0N28XJKtWfRRFTjnQDOnk2Rb9VPzTLRFyCGNqZE8NvtqnJzhVis2lNP8-S9W3RNir_4yC3TTCzPMBm8tolfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c7774f4f.mp4?token=QL6glVt8jQxh9BtzP7jLl_ErkKp6ZjDxJKzzVFapCRpehGGnzVvGWvwKJUUebec8oY_k7Mvp1uTSZmjsIlGbNU2gdbCVRiuQ6kqKyaBc4GymR3Qv2Sp0VOYnVJPsbyxS8kHBpV03RBaGirtw3FC2rFhnu7IpQLybKquZ86vVrebea59jecc0WQOGKY6khy1I6XXxe1RNSEmpzSYtaKFGoSIzHJOnvP_Tkzz7fYR_GOUmEafsHR5vq7FUjma2BJPgUX0N28XJKtWfRRFTjnQDOnk2Rb9VPzTLRFyCGNqZE8NvtqnJzhVis2lNP8-S9W3RNir_4yC3TTCzPMBm8tolfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین وضعیت تونل شهید میرزایی (گلوگاه) پس از حملات ‌آمریکا
🔴
تلاش راهداران برای بازگشایی سریع مسیر
🔴
گلوگاه یا تونل شهید میرزایی دو تونل ورودی و خروجی شمالی شهر بندرعباس ‌بود که به دلیل حمله جنگنده‌های آمریکایی مسدود شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/135287" target="_blank">📅 10:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135286">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrlJvfPQeJByJz3Zm0lz_2JqcHzuLgj0US1jAJVHMcz0uZQsQhjQReuScPp_ZlSUIZxKGhzKTPBP5rTrDAPRAS6nVbaFw4hvKVxa1G0Ayw5Q3dSnUS12Toe7ZYopfzROIGQmEZdCcApDl_dLNths7yBR57rY-VXvHKbzp_0hODWQ_P6mNly3fWAwl5uOvEkoXaFUsBC84JGSeheXCLanS2BTyZg778CCIVrm4FniXkc9emtTRLZcgYz7p6D962pmGyfdQTzxTPbP1DL16QxeztErY54aOZ2rwcIpD79kp9OgiJAO1T5Jfb31LxXjwN_uFQyLPvIbM8uEEf2fvkyx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مناطقی که دیشب مورد حمله آمریکا قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135286" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135285">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9tJWoFlxeA_Ca9ykCcr5B6-P_JmrAb88gtrCj_Im84IHNDNQx00DJj5vyh9FDXa3wr1GeGIiiga_VtRyQu_PGDyKjy4l9w5LCsPN0BwELxB6d0BEORZ3I2ULOCu1cDicf3EgQ4NTujBnCrL5FL_rUxl9Zw6FsLHGsG9n2rbo1mhFXDZrYAtxy5Nup6pkBJ9aARelyFr2LUr8KlzTPpfWidcEe6IdcyUYGSmjaIlvfG8Z97aB2Rd4Dr5snC5pUGhCjeVLVfY4_AL8e53pQ2YEkRLTBqIU-QnQXFFPONvphY-7Fs9W1WTCzInq0tByYlSdm2DeyFLoNxVD3MacrWBfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر آب‌شیرین‌كن تخریب شده بونجی جاسك
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135285" target="_blank">📅 10:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135284">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1vcaFiKYkRpSwjRlugTOsQ7TIkEHN-Y4S3CTEuph6_FyML_LwjZl21K-C03snhujMpKQS7EN1jKW_iRaujpYmxaOAFjaiv5_W2fDglr5A84PpQppkFcyruVR3HQVGc6YGanVtSmn0HxgEiLDFxTYX7HtpdV9DHXIIdqf_t0w9ALPVhmqUWgdxp6hYCL5B56P4swX0EZXetiS6nqwoKTTyKSmJ1efQDzH15UFgB0FI5RXTszzjbSK7Wm-bQa0bLAHmusxGyl_eeBC46ZnkktuRMyDAmrxk3SrGZrqNBSVmj1B1lGHAo4tgEBEVOii1yYIH2g95kCEMx6jrXJ8bFgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پل‌ها و تونل‌هایی که دیشب توسط آمریکا هدف قرار گرفتن:
پل بندرعباس - رودان.
پل سه‌راه میناب - رودان.
تونل شهید میرازیی بندرعباس - حاجی‌آباد.
پل رودخانه شور بندرعباس - سیرجان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135284" target="_blank">📅 10:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135283">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b66fe6ee.mp4?token=GfY3XHxlK9wBZ1CleGFjQQQyBMCBnH9SOro0UvCP2FpQFM2ug9KWkccACeCHjrEGABxWRV4R3TmzNW5S6FQyT7FQSX_Y0fZcB42ycEp6xLzkEXRazloFe-vGd3HtiPM49wTu-m8Opa--O5rJ1fhnm3yooLeFhhTbwWZuMnYBEHK9Z9A3XYyvkLrpeZR27OvU91Adk7Rp5m0_NldWQZVoqRXxZLLUT4WyrhWRMvhliTVyMHec-k_1muvguwytTnrql-3jLFT2TVQpcvqH_2zP0o-X7sdmuG-wNQ2_tXqhsWiUHnwbBP9swUR0N7svf7iYlhv2DB4um-WOrJE96WnxBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b66fe6ee.mp4?token=GfY3XHxlK9wBZ1CleGFjQQQyBMCBnH9SOro0UvCP2FpQFM2ug9KWkccACeCHjrEGABxWRV4R3TmzNW5S6FQyT7FQSX_Y0fZcB42ycEp6xLzkEXRazloFe-vGd3HtiPM49wTu-m8Opa--O5rJ1fhnm3yooLeFhhTbwWZuMnYBEHK9Z9A3XYyvkLrpeZR27OvU91Adk7Rp5m0_NldWQZVoqRXxZLLUT4WyrhWRMvhliTVyMHec-k_1muvguwytTnrql-3jLFT2TVQpcvqH_2zP0o-X7sdmuG-wNQ2_tXqhsWiUHnwbBP9swUR0N7svf7iYlhv2DB4um-WOrJE96WnxBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدای آژیرهای هشدار در کویت همچنان به طور مداوم به گوش می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/135283" target="_blank">📅 10:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135282">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار جنگ الونیوز AloNews</strong></div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135282" target="_blank">📅 10:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135281">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xwb2Bl1MvPNja20kM02V8wvo01cniBxBFN_oSaLSmmHRoGXItc8E5qwTPTSK83ml6YTbX6LygPIQpUwRoscpTHmt-LfyFV_9D9yhaIasUo2tDDtfNO0Kn9Lmfy_ykcp0er9lNj0nGkUe1Ua2XO0Jq2a2TAbSlcgZMVqy4twyZi5Rilql5o7lrKeIafmKCEFXk8UUwkp1YJSgPwbNt3LvHNxjnvlLJb-T7yvMFyYJ_W08uWch7hKEPADZZiBrK1xvy50QzehU0BmKXfF1bDYLs-ej0ABYufG0IVMtBeuwtWDSzBpHOqrlrLgBu2s_wW_TfB8n0otNouADLC24QTSbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیرانوند: علی دایی رانتخور هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135281" target="_blank">📅 10:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135280">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کنسولگری آمریکا در شهر پیشاور پاکستان روز جمعه در بیانیه‌ای اعلام کرد که فعالیت‌های دیپلماتیک مرتبط با ایالت خیبرپختونخوا از این پس از سوی بخش خیبرپختونخوا در سفارت آمریکا در اسلام‌آباد پیگیری خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135280" target="_blank">📅 10:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135279">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1Kj0Btsy3BkSq3C7zm8qE0kYZHAMpvDo4-A3kJadzNLmIrSWAdTfBhZYJdqDwBx_e_SKYOjzXiJKbgw9njMZds_9f4jv7-WCy2mp2Fo4a1D9LRVZQ6Oq9FL0xVVVtlcgy3nigQ35jH7Daj_7O8nKAXgwDwOJyStEXcqRWUwQdcRr7NY1-xQyOAfkiRmKSYz7QweC0MZM5fkHsMSqFgVgLdmQaJX68aVChnEH9huLo2amKuk5Q020bKM--eL3N__rkvQ_mZTudK2SwOfW361TwpUtiggJF6LzYDCZiR4wPSycUOiaySqPpCPMfkGM-9sTZeKTBW-2JByWfwRASw1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دفاعی بحرین: حملات هوایی ایران را رهگیری و منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/135279" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135278">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مدیر سازمان سیا، جان راتکلیف: اگر چین از نظر فناوری بر ما برتری پیدا کند، این یک مشکل جدی است. ما نباید اجازه دهیم این اتفاق بیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135278" target="_blank">📅 10:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135277">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سی‌بی‌اس: مقامات آمریکایی اعلام کردند که ایران در این هفته دست‌کم ۲ پایگاه در اردن را هدف قرار داده و چندین نفر از نیروهای نظامی آمریکا مجروح شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135277" target="_blank">📅 10:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135276">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رسانه لبنانی الاخبار: رئیس دوره انتقالی سوریه طی روزهای گذشته پیامی از دولت عراق دریافت کرده که در آن از وی خواسته شده است از ورود به پرونده لبنان خودداری کند. دولت عراق به دمشق اطلاع داده است که اگر شیعیان لبنان یا حزب‌الله از خاک سوریه با تهدیدی مواجه شوند، گروه‌های مقاومت عراق بی‌تفاوت نخواهند ماند و هر اقدام سوریه در قبال لبنان می‌تواند با اقدامی متقابل از سوی مقاومت عراق علیه سوریه همراه شود.
🔴
احمد الشرع در گفت‌وگو با مقام‌های عراقی تأیید کرده که دولت آمریکا از او خواسته است در پرونده لبنان وارد شده و علیه حزب‌الله موضع‌گیری کند، اما او این درخواست را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/135276" target="_blank">📅 10:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135275">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
امتحانات نهایی ۴ استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، یکشنبه و دوشنبه ۲۸ و ۲۹ تیر، هم برای پایه یازدهم و هم دوازدهم، لغو و به زمان دیگری موکول شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135275" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135274">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e88f12b6e5.mp4?token=XvlofKveSzt8p-OyLNdTGHqQgJQPjCRwt9Fx0u510e1m55thi1ceAHfTJ6cdfbcnGZgLsZQwymfoH864VHisPrnwKjLEzZfBESV0NPmqBZx2RGekYjLNLUHIhydvVoZJF_UXdCwH0r4WFWIrduKlkJOS3VRzodC1C3WxJiuAclKVh_7Pv6rJ5K4oOPGakpimcxBmFRBBZ-WHcrFCuRRVyPX4GUKuViQ8-4T6pl5bLXf8qtJw9YZDXF1jEzPCZ3x1mmudrZ7kSiVOF768neO-WDH-0LuJ2VgV6R4fLwcbwkRzsBBun4heoA9T1uitva0OBmj-J-jieuuDqbhEi9sy9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e88f12b6e5.mp4?token=XvlofKveSzt8p-OyLNdTGHqQgJQPjCRwt9Fx0u510e1m55thi1ceAHfTJ6cdfbcnGZgLsZQwymfoH864VHisPrnwKjLEzZfBESV0NPmqBZx2RGekYjLNLUHIhydvVoZJF_UXdCwH0r4WFWIrduKlkJOS3VRzodC1C3WxJiuAclKVh_7Pv6rJ5K4oOPGakpimcxBmFRBBZ-WHcrFCuRRVyPX4GUKuViQ8-4T6pl5bLXf8qtJw9YZDXF1jEzPCZ3x1mmudrZ7kSiVOF768neO-WDH-0LuJ2VgV6R4fLwcbwkRzsBBun4heoA9T1uitva0OBmj-J-jieuuDqbhEi9sy9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای جدید سنتینل-۲  نشان می‌دهد که یک دیش ارتباطات ماهواره‌ای در پایگاه ناوگان پنجم نیروی دریایی ایالات متحده در بحرین، توسط پرتابه ایرانی مورد اصابت دقیق قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135274" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135273">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135273" target="_blank">📅 09:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135272">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
شرکت برق کویت: یک حمله جدید صبح امروز به یک ایستگاه برق و تاسیسات شیرین‌سازی آب انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135272" target="_blank">📅 09:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135271">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
زمین‌لرزه‌‌ای به بزرگی 5 ریشتر، جنوب‌شرق ترکیه را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135271" target="_blank">📅 09:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135270">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e21fc7be.mp4?token=FKK5XQSnUmZp8DiFLphE_LUz_U_aLB48wZxKLEHoqeH2ucKtvVE15ia62UXGSNLxMeSDaPktzbxK95RpxsQSg9BPMQKZP75Y7lG6VBIpBsIYyaYWDBR4N72_nUY1m_9QaZaDiKVOVmcS1neUEIWZgqQa74FLYswj8T7m0OHG355NNPPZHHjTq8-fOpW9NkSxuwCORE0aWACTqcsfZwliC0ABbttOeXh_qlXd6Cc9sh5RLD7qd-0DtT57XyDuhXEIlrfH0I5W_U-eqZIlb80moY52JPeR4Xh0NoQNzbw4bd56evs3Tii5YEiXJSsPJLZHjA3Z9w5Ex4wWtyNMujMfNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e21fc7be.mp4?token=FKK5XQSnUmZp8DiFLphE_LUz_U_aLB48wZxKLEHoqeH2ucKtvVE15ia62UXGSNLxMeSDaPktzbxK95RpxsQSg9BPMQKZP75Y7lG6VBIpBsIYyaYWDBR4N72_nUY1m_9QaZaDiKVOVmcS1neUEIWZgqQa74FLYswj8T7m0OHG355NNPPZHHjTq8-fOpW9NkSxuwCORE0aWACTqcsfZwliC0ABbttOeXh_qlXd6Cc9sh5RLD7qd-0DtT57XyDuhXEIlrfH0I5W_U-eqZIlb80moY52JPeR4Xh0NoQNzbw4bd56evs3Tii5YEiXJSsPJLZHjA3Z9w5Ex4wWtyNMujMfNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی به ثابتی میگی چرا جنوب نمیری؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135270" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135269">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فرمانداری دزفول: به‌دلیل انجام عملیات انهدام مهمات، احتمال شنیده‌شدن صدای انفجار از ساعت ۱۰ صبح امروز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135269" target="_blank">📅 09:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135268">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سنتکام پایان هفتمین شب حملات به ایران را اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135268" target="_blank">📅 09:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135267">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ونزوئلا اعلام کرد شمار قربانیان دو زمین‌لرزه ماه گذشته در این کشور از ۵۰۰۰ نفر فراتر رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135267" target="_blank">📅 09:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135266">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
منابع رسانه‌ای از وقوع انفجارهایی در شهر الخرج عربستان سعودی گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135266" target="_blank">📅 09:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135265">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
حمله آمریکا به آب‌شیرین‌کن بونجی جاسک /۲۰ روستای ۱۰ هزار نفری بی‌آب شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135265" target="_blank">📅 09:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135262">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f6a6ca0f6.mp4?token=rQN_AhO2Bml8w8mXVJbZZpUndaRfPv4nYAxHjlY52dB5dvSEF1mZMaegYNB30X8nDweEsp4wwHWngH42I5fKrLWNgT_olNUT3in5vRtN5PzgfEDG3kv1iNj7aoEqXIoE9T-yzshBnCcPrYgkt1xNQrBSb_aotL5irbbB65ZG_aDT50gHGTS0CsHt6zxpo3MUCA8PhJELHwcVRkycbYWIEeBtYHvQyBOJ3vIMxdTbZBet3IfAOwNo8-U2wQ6L6cdTW8QZ4DVOd1PLZZVOHT0J4fIVG4tjV7tBhzALsJrV9kEhIJBhO3-rdJUhpSq5FzeTBfoksk6uEehZxUoQ3XQ84A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f6a6ca0f6.mp4?token=rQN_AhO2Bml8w8mXVJbZZpUndaRfPv4nYAxHjlY52dB5dvSEF1mZMaegYNB30X8nDweEsp4wwHWngH42I5fKrLWNgT_olNUT3in5vRtN5PzgfEDG3kv1iNj7aoEqXIoE9T-yzshBnCcPrYgkt1xNQrBSb_aotL5irbbB65ZG_aDT50gHGTS0CsHt6zxpo3MUCA8PhJELHwcVRkycbYWIEeBtYHvQyBOJ3vIMxdTbZBet3IfAOwNo8-U2wQ6L6cdTW8QZ4DVOd1PLZZVOHT0J4fIVG4tjV7tBhzALsJrV9kEhIJBhO3-rdJUhpSq5FzeTBfoksk6uEehZxUoQ3XQ84A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادهای اوکراینی به انبارهای نفت در مسکو
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135262" target="_blank">📅 09:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135261">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlO2jOUErpyUbXvh-Pnuk0YW2Qu_FqLy23nH-VpWwA94KRm-s1_-MjLHBrDSqNU8rZGqcnZeXcpCF65jIU748CQi7Ltnpl-u_WthqQ8sMX0huSCWP6MEeFaD2O65Hv033kiI-DhA7SHVQR_dg5aniEXjQu3nAaZN2b34Pj9TECfNtNrsj3wEQxJ8EASme9N_bRGv6hl-HN0KxyRbt-a1LlMEfAiKfiIC-lizOjri9E9mWWTiN9KIlx1LCallK1fvv8ylfOVHd4vyabgRBlTDYJHXgaUI8oQB2UXaXlAQTQ_xQeTBOnLdxJ0qbfJpli5Uvgsb6zhbG-PPht7YAQVvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان بوشهر امروز صبح
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135261" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

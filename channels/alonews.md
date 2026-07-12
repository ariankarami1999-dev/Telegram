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
<img src="https://cdn4.telesco.pe/file/gXs83xBQpDXPTAqlZDYhWUt60pjHZsJ3-lP-AfDUV1sLWUUTvi5S4xI3MSzmiWmhQx-QDjROtaqChyKSYV55Q37UjIPUfneFozFeX2dYBT26v8cu03LTgnz-8GVCsOmh4x1sKrbAkaiodE9QFDiJGvYYzu8_-z-Dtsngohpf4rAWyM432soQhKaie7WoWGmHxJnJ7cM8kJV2WTyX7DcT7PsPGbZWWjPEqWacLjQwJsH9AF5A_ETaqDDKDAUFZ4eU_6rDNAVhga1E3vmRyQ3Uw2dLqBsgXAgTAdbKn8MZmqG00PuSxKozVhlZT0tlkasbU-hu2pNwimt6meE948vQ8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 919K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 20:18:59</div>
<hr>

<div class="tg-post" id="msg-133508">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوووری/ترامپ: امشب جهنم بپا خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/alonews/133508" target="_blank">📅 20:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133507">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ارتش کویت اعلام کرد سه مرکز مرزی این کشور هدف حمله قرار گرفته‌اند که در نتیجه آن خسارت‌های مادی وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/133507" target="_blank">📅 20:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133506">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فرماندار قشم : اصابت ۱۰ تا ۱۱ پرتابه (موشک) از عصر امروز یکشنبه، تو جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/133506" target="_blank">📅 20:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133505">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوووری/ فارس: برخی منابع از کشته شدن ۳ آمریکایی در حملات ایران به کویت خبر دادند
🔴
وال استریت ژورنال یک ماه پیش در خبری مدعی شد: در صورت کشته شدن سربازان آمریکایی ترامپ پایان کامل آتش‌بس با ایران را بررسی خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/133505" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133504">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی مدعی شد: ارتش آمریکا ساعتی پیش حملاتی را علیه سامانه‌های موشکی، پدافند هوایی و قایق‌های کوچک متعلق به سپاه پاسداران در دو نقطه نزدیک تنگه هرمز انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/133504" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133503">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نهاد فرودگاه‌های پاکستان از فرود اضطراری یک فروند هواپیمای امارات در این کشور خبر داد.
🔴
یک فروند هواپیمای باری بوئینگ ۷۷۷ متعلق به شرکت  «امارات اسکای‌کارگو» که از اوساکا به مقصد دبی در حال پرواز بود، امروز پس از آنکه خدمه از بروز یک مشکل فنی در حین پرواز مربوط به یکی از موتورهای هواپیما خبر دادند، مسیر خود را تغییر داد و در کراچی فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/133503" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133502">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9iPSW1jdr7SToqO1-wDD1IC1riJB6eSeCLBq3XbaQbhwIdIVKD3wc_VtvafnfIguqCSzDPqiOkuizSMvVbfsV1v9NXz7Yk-hjhgTgJfFUw6niXY68G5F0PWoju_n5enqKlph9EvtFm03nF746aXaIuHFVoJkw-9wMb6ZK55pyegXOQFrZOchRUzSttd-F1R_MDlcIiFJKPwTl-WlymmXUG7bVd-X9bNc0j3cBbsyFz3jHNnybclB5We1u7t187bz02bq4WsIUotprP3DrGPd_QlxDTRwi6UchHZvKbI6Yi6az1xyyzQmR-_2Q0K2TTEyX5HKdqxgnXHnXe7Kx9n2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر بیشتر  از جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/133502" target="_blank">📅 20:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133501">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / منابع امنیتی به نیویورک تایمز.
🔴
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/133501" target="_blank">📅 19:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133500">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKeVhMDwrCBWdLYl11afl6K0T7TFnMGX0JmcNqcw1d6Ng2-74rPt6V1iKxb4FQv1td_TTBQCtHARa4K3hu-7m3GPYExxAzCdhq5RqwBIwIvpT_WdMATKMA7wGOmLMipkzwBt0CS0PxP7PbXnnt9LVRWmlFOAmA96-JjaQJT2dumk3Z7Xd9op1JmulxHY7ND2gV2nnZTBum3-GnRKLty6z88UoKgE3d5916jI02Eu86_Ub44O7h9JAOdhbBk5VW4IvrFZO_X0_hI9EiuslPnrJ6Oh6QglpwX8BbCzGkVGrKOxJFfBD0r6M76aWfVuAQKSaziHNSciE7D5Cf1Uj90eBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از آتش سوزی در جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/133500" target="_blank">📅 19:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133499">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ایالات متحده حملات تلافی‌جویانه‌ای را در پاسخ به حملات ایران به کشتی‌ها آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/133499" target="_blank">📅 19:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133498">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / گزارش‌هایی در برخی رسانه‌های منطقه‌ای از درگیری در دریا بین نیروی دریایی ایران و کشتی‌های جنگی آمریکا منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/133498" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133497">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ca9785e0.mp4?token=lzibSJQpSBSuwdBe4nJ99J3eylPIVL3vbOpvNQW3tWVochHSoJ2CwJ0F9V6kdhtg-npugPbn1d57NMUgMASyxOtpm7ASXwwB4I_cRpq0l6VVCn9eu_xRF_Vxt9AxRyv6WVptC18GXsTJ7rGRuF5bn_Dr0vxFS6hBlo0MgktHS5txX47qtpCGRHHuahwOR2zExJs9aT6LUFXpRb9POWUZ4ex7K28QfJLmzHpFWkzwQCPQT4e6pHbuY82Y_v_wZ4f8QtdpHRlWCIF6NyFO1F43xjY8oKFDCo3kniz7uNNU1M5hJmcOtKyp2xYFz8oxMJrdQvovdc9ZZAxOHjanL5CtOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ca9785e0.mp4?token=lzibSJQpSBSuwdBe4nJ99J3eylPIVL3vbOpvNQW3tWVochHSoJ2CwJ0F9V6kdhtg-npugPbn1d57NMUgMASyxOtpm7ASXwwB4I_cRpq0l6VVCn9eu_xRF_Vxt9AxRyv6WVptC18GXsTJ7rGRuF5bn_Dr0vxFS6hBlo0MgktHS5txX47qtpCGRHHuahwOR2zExJs9aT6LUFXpRb9POWUZ4ex7K28QfJLmzHpFWkzwQCPQT4e6pHbuY82Y_v_wZ4f8QtdpHRlWCIF6NyFO1F43xjY8oKFDCo3kniz7uNNU1M5hJmcOtKyp2xYFz8oxMJrdQvovdc9ZZAxOHjanL5CtOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از مِسن استان هرمزگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/133497" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133496">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/صدای انفجارهای مهیبی از تنگه هرمز به گوش می‌رسد.
🔴
گزارشاتی از درگیری بین نیروی دریایی ایران و ناوهای جنگی آمریکایی مخابره میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/133496" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133495">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / صدای دو انفجار در جزیره قشم و بندرعباس، ، شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133495" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133494">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری / هم اکنون سفیر آمریکا در سازمان ملل: تهران به یادداشت تفاهم نامه با آمریکا پایبند نیست، همه گزینه ها اکنون روی میز قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133494" target="_blank">📅 19:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133493">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
عراقچی: ایران از تمامیت ارضی و حاکمیت ملی لبنان قاطعانه حمایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133493" target="_blank">📅 19:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133492">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری / منابع خبری از شلیک ۳ موشک بالستیک به سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/133492" target="_blank">📅 18:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133491">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6a433de38.mp4?token=UQ99txvR2IVifbcKhQOPwN3kR1REwUd7ma0-eWodaYn4uCmn9vjuWsO8uVsfxmMchh7z4TbBQddB7LPeE2YRRhe_HcqbcGrxyc80DgWje6_svYldLMPn4F1ruSXeOcMke3bCvd8zOgw5YP8tQbib_hlD35D8NxAf9vyuBbGZUn2_YYOOThfzPDsWxnfscyqcNY-4ZiTpA5GdZWeh1w1tpsvrxKwp8l2otRE7XD2w2DURHK8-FghuhHCZ9txu1kDTr75ZYDoSj26N_M69grJAWSWWBGGSxBBluswBInfNgpDGZy_DTPbMLEgN3cZWmEz4YCzJJY9EUPrNd_0Q54Kx2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6a433de38.mp4?token=UQ99txvR2IVifbcKhQOPwN3kR1REwUd7ma0-eWodaYn4uCmn9vjuWsO8uVsfxmMchh7z4TbBQddB7LPeE2YRRhe_HcqbcGrxyc80DgWje6_svYldLMPn4F1ruSXeOcMke3bCvd8zOgw5YP8tQbib_hlD35D8NxAf9vyuBbGZUn2_YYOOThfzPDsWxnfscyqcNY-4ZiTpA5GdZWeh1w1tpsvrxKwp8l2otRE7XD2w2DURHK8-FghuhHCZ9txu1kDTr75ZYDoSj26N_M69grJAWSWWBGGSxBBluswBInfNgpDGZy_DTPbMLEgN3cZWmEz4YCzJJY9EUPrNd_0Q54Kx2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انبار در مقر فرماندهی ناوگان پنجم نیروی دریایی ایالات متحده در بحرین نیز شب گذشته مستقیماً مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/133491" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133490">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری / منابع خبری از شلیک ۳ موشک بالستیک به سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/133490" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133489">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / منابع خبری از شلیک ۳ موشک بالستیک به سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/133489" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133487">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14311630a.mp4?token=eLrni_6JJOxZzf2Q9il9Kc1VAPkIWi0KA3T8OYe_M8vINU4YZ53ixA9CM_2aHg_jrH7HUy5l56LQrItD-nuP5KcaCjsEWic-l-ZOnZZ3b5n8beiHQfs1rWqNdrjdnRpxMurBt-ID2cKUhK3cpjEkAZnqtr8Gq3UUjUYVzA5VTa0QfEZ61Ia8mGlBub5lCqdgVBbaMGIyUeOeCV3gl-HAsxPbJE-swI0vxakw0tfjfzaMpA-6H9UZkakSi0OkK9W5_calfil2toz_7A3NbaAzfhuXcjU_BPTe3RlIwhjYqp3KyJUiCNfTFbIsBi8l1wg9nXEn1BGfThzPswd6iB4PzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14311630a.mp4?token=eLrni_6JJOxZzf2Q9il9Kc1VAPkIWi0KA3T8OYe_M8vINU4YZ53ixA9CM_2aHg_jrH7HUy5l56LQrItD-nuP5KcaCjsEWic-l-ZOnZZ3b5n8beiHQfs1rWqNdrjdnRpxMurBt-ID2cKUhK3cpjEkAZnqtr8Gq3UUjUYVzA5VTa0QfEZ61Ia8mGlBub5lCqdgVBbaMGIyUeOeCV3gl-HAsxPbJE-swI0vxakw0tfjfzaMpA-6H9UZkakSi0OkK9W5_calfil2toz_7A3NbaAzfhuXcjU_BPTe3RlIwhjYqp3KyJUiCNfTFbIsBi8l1wg9nXEn1BGfThzPswd6iB4PzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی گسترده در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/133487" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133486">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbpQOS0b_OI-pEa8OZuYW3xted4-WyfkgrBI8xYm0vjGckwIuZMk3ADYQsQ5qMACnEAgBOQI4cdH56XmfdMWlh4gmVDIHb6VXMIPvEmA4Che1G6eNIbWnxzyv6fSQjY2ECyofPieDmB9skWQNjTm_PFafnrD2gCkKkeJuQrkCNP9xpEnlxNndlcVvT2Szfa5Cgrc6NjJmtTaMsnUoxfPigg5CtPdTOqfWOiRtmeJAmib2mHNKh7Fyt4jmu3qSkeefDdjFHkONhV9PLfDJdz39o25Sex08l1DmRuZOm7gmn4jauoVKCBaSynFc9jftOXtbh09aQ87KgLOYRzyzm5RHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون‌های غلیظ دود در مرزهای مشترک عراق و کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/133486" target="_blank">📅 18:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133485">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
المانیتور به نقل از منابع اسرائیلی:
راهبرد محتمل اسرائیل، دور ماندن از درگیری ایران و آمریکا همزمان با فشار به واشنگتن برای تشدید تحریم‌ها و مقاومت در برابر خواسته‌های تهران
🔴
سناریوی مطلوب و کم‌ریسک تل‌آویو، بازگشت محاصره دریایی است که «بسیار بهتر از یک توافق بد با ایران یا یک جنگ کم‌شدت است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/133485" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133484">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn56oozZhKcAZz3rncm_NjlvUFDmvJ6IXLRttOOFiHFKSRzlKHnlBlluvQNd7jLkE48kt8hpnKHSt9XOn2c3Razyv3qrM6WZ_OwEHs_r8D1kw28QHEdd5_rKOZ1VvI2DhmemBR2sE5WHdFpup7rnfAcsG6NC0XHBrAkeoGK1hueCVDB2Ykd0Xo965ONc0uql1sy4e4iIaj7fDz_Kxzau107Z8rZJdgR8Z98TmqBIh5f8Z7UwjOhwDH7a9WZJ49vsqWIB5kJJWtXt8BZ2JiK7tBj3ZuwHAIAYL4z9uqsAUKg9JttAjAX6WbDDwudjwRguW1bjn_AKqW4hdy9nxLFuAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره ای از پایگاه هوایی العدید در قطر که دست کم محل اصابت یک پرتابه ایرانی در آن دیده می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133484" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133483">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رسانه i24: انتخابات اسرائیل در تاریخ ۲۷ اکتبر [ ۵ آبان ] برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133483" target="_blank">📅 18:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133482">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/365f150fdc.mp4?token=je7HCFd9OGph-7wEd9bkSy5089TWy23Opnqw5kEehu5dnewXVPozFCau8-A0JuPMihJer9Cwj9w_Pqa_9p7Nbp6i-bIH3Tsn5DuNcNa0hh7iylwiRFdNyNafiLfzCjrrDIhTCqkmssMYWnCzQAIzBzXddpbIvyQt3Vl9L-ZLzXWzeD0S1boMQc29_CSzD92HU3CwsWTXQQLK65BVESzKtwLHOj4f6WdEfnATG4KA570snUOxH3qTcbN7mM1xFaZoYyAP65bpxnbuieI2RxwEIluPCPMGiLsTs4QFXJj4dw0ZqgMRMowfQLxpxkjIi5GlL09T_z62c7Cx5sFUy-bxxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/365f150fdc.mp4?token=je7HCFd9OGph-7wEd9bkSy5089TWy23Opnqw5kEehu5dnewXVPozFCau8-A0JuPMihJer9Cwj9w_Pqa_9p7Nbp6i-bIH3Tsn5DuNcNa0hh7iylwiRFdNyNafiLfzCjrrDIhTCqkmssMYWnCzQAIzBzXddpbIvyQt3Vl9L-ZLzXWzeD0S1boMQc29_CSzD92HU3CwsWTXQQLK65BVESzKtwLHOj4f6WdEfnATG4KA570snUOxH3qTcbN7mM1xFaZoYyAP65bpxnbuieI2RxwEIluPCPMGiLsTs4QFXJj4dw0ZqgMRMowfQLxpxkjIi5GlL09T_z62c7Cx5sFUy-bxxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: فکر می‌کردم لیندزی قراره تا ابد زنده بمونه! بهش گفتم: "لیندزی، تو که جاودانه‌ای!"
🔴
و قرار بود یه پیروزی بزرگ به دست بیاره؛ همه پیش‌بینی‌ها هم نشون می‌داد با اختلاف زیادی برنده می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/133482" target="_blank">📅 18:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133481">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_coqMGP__PV_d_PnemwOjPB6KabCOQilNsFVVS-rWmseVNZz3TyM9a047BgDZftSFmeE4S5K_aMsDbvN6wltsJyJmLqW-61Lzz_d_geDdsICd98gXHauI7OqOz460AhhWkLScBtpSunbLIqaeHd54_ISfSO7VhYP8gUmDI0Gjqr1_tWF0tFgM4oDeRMOo3cx1VCJh3pjbiNDdm9lKXpgDETZp7KnUPmeEOR8ewa8g2QJ5WIMCr-gDc9kLoyB3X97K6W5EFsP9Bt_yN8jj9Ri6HGGVh-LtAxRzZzHCoJXEjZshqeQ4It75gN3smEnA_8Wxp1n7aLTN0lLH5E8movHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حمله گسترده پهپادی اوکراین به سمت روسیه.
🔴
بیشتر این حملات در حال حرکت به سمت مسکو، دریای آزوف و شبه جزیره کریمه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133481" target="_blank">📅 18:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133480">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664dc8a38e.mp4?token=hGxcpduSbdd8fpmQd1vvSa715doaXaRUgPFQWItvxeVEDulRs9s7HsYp8ET09g_v5GlA9EtZDGwi654nm6wKkBVZm9JHWDuhAcKvRNkZZ3FGHGxIfyGx1HLreDQlAmdRtEat73ROOlIo0G6xmR1ByLylePgg6fWvSOEhw-BcS-P3tiXxXJEzz8EaHltJ7xgt7WxviKG0bQo_FfNDAQuhf3F6Piv1QBq7kCgg2c_5dnb6JJJRwtkrzJB-67lQD07GkwB4_bWZBCP8tEIYnzetNpPmuIHtG7EGoor-BRlMol55G7ASzGL1oyWGqklxlKua8rTdSkF330GssNJL95c0KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664dc8a38e.mp4?token=hGxcpduSbdd8fpmQd1vvSa715doaXaRUgPFQWItvxeVEDulRs9s7HsYp8ET09g_v5GlA9EtZDGwi654nm6wKkBVZm9JHWDuhAcKvRNkZZ3FGHGxIfyGx1HLreDQlAmdRtEat73ROOlIo0G6xmR1ByLylePgg6fWvSOEhw-BcS-P3tiXxXJEzz8EaHltJ7xgt7WxviKG0bQo_FfNDAQuhf3F6Piv1QBq7kCgg2c_5dnb6JJJRwtkrzJB-67lQD07GkwB4_bWZBCP8tEIYnzetNpPmuIHtG7EGoor-BRlMol55G7ASzGL1oyWGqklxlKua8rTdSkF330GssNJL95c0KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع امشب تندروها بخاطر مرگ گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133480" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133479">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
لهستان خواستار دریافت 10 هزار زلوتی در سال از آلمان برای هر قربانی رژیم نازی است.
🔴
در نتیجه تجاوز و اشغال آلمان، حدود 6 میلیون لهستانی جان خود را از دست دادند. بنابراین، درخواست لهستان معادل 13.8 میلیارد یورو در سال است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133479" target="_blank">📅 18:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133478">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
علی خضریان، عضو کمیسیون امنیت ملی مجلس:
جمهوری اسلامی ایران چه با عمان و چه بدون عمان تنگه هرمز را مدیریت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/133478" target="_blank">📅 18:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133477">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزارت خارجه پاکستان:
پاکستان تحولات اخیر را که
تنش‌های منطقه‌ای را بیش از پیش تشدید می‌کند
، با نگرانی عمیق پیگیری می‌کند.
🔴
پاکستان مجدداً بر حمایت قوی خود از حاکمیت و تمامیت ارضی تمام کشورهای برادر در منطقه تأکید می‌کند و از همه طرف‌ها می‌خواهد که خویشتنداری پیشه کنند،
گام‌های فوری برای کاهش تنش بردارند و تعهدات خود را بر اساس تفاهم‌نامه اسلام‌آباد (mou) حفظ نمایند.
🔴
پاکستان از سوی خود متعهد می‌ماند که از طریق گفت‌وگو و دیپلماسی، همه گونه حمایت را برای دستیابی به صلح و ثبات پایدار در منطقه فراهم آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/133477" target="_blank">📅 18:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133476">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: رهبران ایران دیوانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/133476" target="_blank">📅 18:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133475">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=lhPJEHoiksnuhcOdnrVNtfjhrWWwTNYpMk1YIwSXYLx12XJDtmw5-sQdKGhpnImN4llAejTpMIM0lavG7ozPY6grqT2lgNgvIK3uFiICJtAhtE3t0C4kjvYu6T5rV1ucuQOqXT5XaY2RDOLxmXGFPymkJKh857eI6YkrX0U66iZaRwTVRA_9xbMlqisF7Pa2oeb_VVakCZJgQMUfuIV_0K9vvyGTifWz39M8UQay2M9-WoOEq04HAJeeqgEABduz3n2dITJI1jOTnIJyT6HirzSGqSnpvx8jRXfTCtrsER8249d4EyWSEfB9DzA0RgingjHyDL-Ivb3DoKI1tk-_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=lhPJEHoiksnuhcOdnrVNtfjhrWWwTNYpMk1YIwSXYLx12XJDtmw5-sQdKGhpnImN4llAejTpMIM0lavG7ozPY6grqT2lgNgvIK3uFiICJtAhtE3t0C4kjvYu6T5rV1ucuQOqXT5XaY2RDOLxmXGFPymkJKh857eI6YkrX0U66iZaRwTVRA_9xbMlqisF7Pa2oeb_VVakCZJgQMUfuIV_0K9vvyGTifWz39M8UQay2M9-WoOEq04HAJeeqgEABduz3n2dITJI1jOTnIJyT6HirzSGqSnpvx8jRXfTCtrsER8249d4EyWSEfB9DzA0RgingjHyDL-Ivb3DoKI1tk-_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
چند دقیقه قبل اینکه لیندسی گراهام فوت بشه، باهاش تلفنی حرف زدم؛ حالش خوب و فقط یه خرده احساس خستگی می‌کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/133475" target="_blank">📅 17:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133474">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ad100662.mp4?token=CP5lqFrv1E1u_mYfgHlcBIzolzOs-Y4gqHCOKOpGoOdVrKVNVUBHlqABVZylbej-6gKMGqngc_2WJVnJwuOWPUwb4U9MVPdMzp5n07xi_mKqrJvs5qDF3IG3LLmW96NJ9qW0fHbcR2v5AAypb99OQNfWZ5LaZH3zOboEC-z-y6m-YdQGEaMxEZt2ZW6eDWQuuU-3SKF3WGGw4NyLgciPJQYzrpqwf8Crdhqw5-IArmkBnWlOWW2_QWmpAFUdbn9qviJa5jgvZMWAnRHvbVjUF2vUhBw2FwLD8NCnaZ5HGgHuhCJj_hdkhRqByIx8CZOlUEAUpnavrM3nAthQhCWpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ad100662.mp4?token=CP5lqFrv1E1u_mYfgHlcBIzolzOs-Y4gqHCOKOpGoOdVrKVNVUBHlqABVZylbej-6gKMGqngc_2WJVnJwuOWPUwb4U9MVPdMzp5n07xi_mKqrJvs5qDF3IG3LLmW96NJ9qW0fHbcR2v5AAypb99OQNfWZ5LaZH3zOboEC-z-y6m-YdQGEaMxEZt2ZW6eDWQuuU-3SKF3WGGw4NyLgciPJQYzrpqwf8Crdhqw5-IArmkBnWlOWW2_QWmpAFUdbn9qviJa5jgvZMWAnRHvbVjUF2vUhBw2FwLD8NCnaZ5HGgHuhCJj_hdkhRqByIx8CZOlUEAUpnavrM3nAthQhCWpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ برای ادای احترام به لیندسی گراهام، دستور داد تا پرچم آمریکا در کاخ سفید به حالت نیمه افراشته در بیاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/133474" target="_blank">📅 17:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133473">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/321fd5e5da.mp4?token=II3evLHEz0K6yfAjeyhpIv3NR1VXBNOh4X-UONurIJENHozaYDAlwUXty_voeYXGVLNbaVvr5oA1YqkGClLdYFxZtZxlz4Vmv8p6-ubh_h6nF8ejmcANEEeCWgLXILFD0DemPqMi-mPOCvx3401rv9R8D93EG8GO6KnAnfyqyxjeSi6z-b4XNyuGX6IIUuGvbPxwjE3ogATVvOQn9zFrzmBitPf2essmWAYScET2auJBMq_-lraWBtWpym37naLbsFSM9yvJ5GG6Hxfdn4OW1jm1wXORhg9rrZcyKCsGDgm6G4jAyqIJGpNab0raqbf3xS_BEkjfh9J8Cw5P0JhrFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/321fd5e5da.mp4?token=II3evLHEz0K6yfAjeyhpIv3NR1VXBNOh4X-UONurIJENHozaYDAlwUXty_voeYXGVLNbaVvr5oA1YqkGClLdYFxZtZxlz4Vmv8p6-ubh_h6nF8ejmcANEEeCWgLXILFD0DemPqMi-mPOCvx3401rv9R8D93EG8GO6KnAnfyqyxjeSi6z-b4XNyuGX6IIUuGvbPxwjE3ogATVvOQn9zFrzmBitPf2essmWAYScET2auJBMq_-lraWBtWpym37naLbsFSM9yvJ5GG6Hxfdn4OW1jm1wXORhg9rrZcyKCsGDgm6G4jAyqIJGpNab0raqbf3xS_BEkjfh9J8Cw5P0JhrFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره
جانشینش :
- یه نفر رو تو ذهنم دارم که فکر می‌کنم گزینه خیلی خوبی باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/133473" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133472">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز باز است. ما حملات شدیدی علیه ایران انجام دادیم.
🔴
ما دیروز با ایرانی‌ها به توافق رسیده بودیم و آن‌ها از همه چیز گذشتند، اما ناگهان دو ساعت بعد، با یک پهپاد به یک کشتی حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133472" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133471">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: تنگه کاملا بازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/133471" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133470">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9TuPQN8kcQCoXG2VEV2sc5SlDGkO3O8RWqOdo4GJFeLGCBQQ8eP75PeUJdGkUEfBsBGLslqVbtvbEutvaadbTyeixZLZQWiMSx3Zm9rczgQAHBXL-_3JbduAij93dcc5ySB3xB_V353GFSt-Zq1ZRCJyIKzL6XIKQsVmsqIzrY-yUCfhpPxJf6IL1uZ5_TY9utaV2QKHBOLFr0mpI5E92kE8KxWu21Rsfuxdi1yDBK4pj5u6h2n3qGIrPNqxOQcpGsl2WOGJoAP0o6eJv3VUUAacc85MPS6MSfcLclTZ_h0gvux7r07YQanhBuS38bxrmDiDE54DaLwFSYoolaV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به هوش مصنوعی گفتم یه تصویر از تندروهای ایرانی بده که اینو داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/133470" target="_blank">📅 16:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3I6C-U5Rk9pF5g3_wLIM4MLoyQR6e9ggnVfLe0aNeHJzkFTpAnM4gAQcgl9Ll8_YgH9PfLgnlSAB65TgxmRRnuOODUT3kcUe60JQpuh4uygHeK-0Y3i4wnYUKW80dtJyS05_b0OjmwzkXcI40K5NDRi5CiAR2IOit_qI8nVC1DnujNc0jj0dnC7vz-59zgLtX4louAafjQjfvNUboorC48Trlz-58MMKV1Ca2bL0FRx5nQtm9xq15SX3d7PDPJe5Odn_-4VnN51Mwa6YpwkOXe0X8LxG2ViKFiTViGgf23lisGbs4ythpAhSPruwtqVLhGa84Nn2RC7tLoSGf1rKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhZezeN_cr0N-rHj5KLmGaqveO8EO2_yTSC5zy4ObYWesFZyxOrP0M1HiymBpK6o6F9GvQ6e_9V3sedoY0RmQXks0G5lmA5i-XrZuPOufLmlHeAcYlps8ODdyJF5DUS5_offIMxpJqhDDZ-7X-qpSIzueDcdHDwiXdLuUbzfZ0xVB__0q2dQr5CliNBW2Qia2uYzdwIS97tL2wkgmIWz0O98wz-VCaaJ6hZ4Z0ULcQXWQu1Pfknb-jreqjcd3BhLrgJAHh44kxTPm76xMeGpMSTC-ZY2af7jk6_LCaTVj-Wgj34fuCszAyY1W08p7vS1COG0EBNxBAHMez_YKchh_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فراخوان و لشگرکشی پایداری‌ها(ملت معکوس) برای محاکمه قالیباف و پزشکیان و اعضای شعام
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/133468" target="_blank">📅 16:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va1QDzOSwhV009nZNRExbwu4LOicVYj52my8jo2Crvv7OU5H8tqy_Cns0GxoVZ-J6i2LVyl0ERu5lvMpE0qMVaRDt6Y1o318taaq5PyDR_BfpGyLgVV4tTzrkuGzw_DXziAa1k93bRlc5ueBn3cEcBMLgncHbOCoCrh8YRygqXgPFiRxeJmpZnBI7TrltU-54zPExTmkVlrR3nbAG9rpj99ENnhF_Fgick79vM1XFeZxMw_02NrFQX4Aufq6Wgt0ptrfYOUtSBeJ1S9hor5tStfz422c8GQXvUYP_1sDEwbBII7tK4N4ZAU-1cgQPfpUgM8ovBkLfM59zHesNpaFhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان مدیریت مسیر آبی خلیج فارس:
به دلیل تحرکات غیرقانونی اخیر نیروهای نظامی آمریکایی در منطقه، عبور از تنگه هرمز در حال حاضر امکان‌پذیر نیست.
🔴
به محض بازگشت ثبات و آرامش، تمامی درخواست‌ها مطابق با برنامه زمانی بررسی خواهند شد و مجوزهای لازم صادر خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/133467" target="_blank">📅 16:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133466">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=rYKQiYCY7ZDr7-QJvODwsq0-ZHVmMSdHtR3Ww7OtuF2FH2F9VA4U66TuYPtHJDTpqKt-ByKdwaJvBVjaiBZzpqyyxAAomaPpN-IN-CmdYEr6yhMFDxUM5RV1tquVEvuADf33y2u9FP5lcG7zM13cHoM9iJAlnB3iuskr_bF_FUlyjYL4EQftdKA-FSgPF5rgTDEp4YZV4lTLbjCvHqngZE_mI72RDqo9aVGuMLBtXkwZVA_WWJu-cKEY6AjqiM2pvkabxYR3sDaLrLOCbe6NDM6j_wn-n_E0ox943Eoc2y4-JGX21UsQETszd5htYfUUpjsh8wNjmhqrSTsexdwuwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=rYKQiYCY7ZDr7-QJvODwsq0-ZHVmMSdHtR3Ww7OtuF2FH2F9VA4U66TuYPtHJDTpqKt-ByKdwaJvBVjaiBZzpqyyxAAomaPpN-IN-CmdYEr6yhMFDxUM5RV1tquVEvuADf33y2u9FP5lcG7zM13cHoM9iJAlnB3iuskr_bF_FUlyjYL4EQftdKA-FSgPF5rgTDEp4YZV4lTLbjCvHqngZE_mI72RDqo9aVGuMLBtXkwZVA_WWJu-cKEY6AjqiM2pvkabxYR3sDaLrLOCbe6NDM6j_wn-n_E0ox943Eoc2y4-JGX21UsQETszd5htYfUUpjsh8wNjmhqrSTsexdwuwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عادل فردوسی پور: آقای اژدهایی، خبرنگار صداوسیما وقتی صدتا موشک خوردیم و صدنفر آدم کشته شده می گوید همه چیز عادی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/133466" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133465">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سنتکام: تنگه هرمز برای همه کشتی‌هایی که مایل به عبور قانونی از این آبراه بین‌المللی هستند، باز است/ نیروهای ما در موقعیت مناسب قرار دارند و آماده‌اند تا علیرغم حملات بی‌دلیل ایران، آزادی مداوم دریانوردی را تضمین کنند
🔴
ایران تنگه هرمز را کنترل نمی‌کند و ترافیک دریایی ادامه دارد.
🔴
بیش از ۱۴۰ کشتی در هفت روز گذشته از تنگه هرمز عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133465" target="_blank">📅 16:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133464">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=XT6pL9-FEYTIu91IuN-vfB5JZx_bGVDZW-MP_JMiuzArFCjWJD2FLwPASx-qPc_xqPLXQYWJQDV9YgituZsbYzhLSTDtb6W2mA9qxRJcwDD3Tz8ygmxFVJ6TKtmetIokJBDACGrwbpmslQFWYEBNJkpm6kp9NStpgBGFqFTdit_vBP6ik5noaoDPsPCWyRUrBre7EGv980zyWkT-ElAy9Qo7qrQmb7r1BLCzcNJZCrl4UlCYAPoW1A4w2PsJq2w6SRWKLY2FpD3-u8yXnzFejWcdKiA1gFtlTMn1Sn7G-B1hspwv-kwzExavA3yRXAUXrMHqjsiLK20TfJKrI0tv1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=XT6pL9-FEYTIu91IuN-vfB5JZx_bGVDZW-MP_JMiuzArFCjWJD2FLwPASx-qPc_xqPLXQYWJQDV9YgituZsbYzhLSTDtb6W2mA9qxRJcwDD3Tz8ygmxFVJ6TKtmetIokJBDACGrwbpmslQFWYEBNJkpm6kp9NStpgBGFqFTdit_vBP6ik5noaoDPsPCWyRUrBre7EGv980zyWkT-ElAy9Qo7qrQmb7r1BLCzcNJZCrl4UlCYAPoW1A4w2PsJq2w6SRWKLY2FpD3-u8yXnzFejWcdKiA1gFtlTMn1Sn7G-B1hspwv-kwzExavA3yRXAUXrMHqjsiLK20TfJKrI0tv1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار اشتباهی در تمرین پدافند هوایی روسیه/ پرتاب شدن سرباز
🔴
فیلم منتشرشده نشان می‌دهد که نقص فنی در جریان یک تمرین پدافند هوایی، منجر به انفجار زودهنگام شده و سرباز مسلح به سلاح را به هوا پرتاب کرده است. این حادثه تقریباً به کشته شدن همرزم وی منجر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/133464" target="_blank">📅 15:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133463">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEz3YNjx7rnhrLx0mpnzsuVSmxP0JEe2PQO413MpOz6LHYeKQCKzXeJyMSvDDal9Zfgy5G5kcHfRGPuqImFYyO-yUlHmxCkT2sVPOTDB6c_VmQS4-4udpqqzPueDi7xW2wh4eN8dF9M5pcUMOrN9yXZRGAQVT_2bHdh1Y185au047CSHDLnYgr8It0YAHWph3mEBbgAx98JDLqmt-zklPPOabQS80YgkRX2t5kPQgLdIu6CImSqlupW7Ue0CH7L8dyXTXxpHV_C1b02oL-3w3eD5S7kfa3Uy7mc61eEylFYqcfTeZJirdabPGhKkYLwPk1N5TqKZSOgspkEXixT8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمام کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است.
🔴
نیروهای ایالات متحده در موقعیت‌هایی مستقر هستند و آماده‌اند تا اطمینان حاصل کنند که آزادی تردد دریایی همچنان حفظ می‌شود، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران.
🔴
ایران کنترل این تنگه را در اختیار ندارد. ترددها به روال خود ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/133463" target="_blank">📅 15:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133462">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، کاتز : الان وسط غزه هستیم
🔴
نه‌تنها از غزه خارج نشدیم، بلکه حضورمون هر روز بیشتر هم می‌شه؛ الان بیش از ۶۰ درصد غزه رو در اختیار داریم
🔴
همون‌جا هم می‌مونیم و عقب‌نشینی نمی‌کنیم
🔴
این مناطق امنیتی از این به بعد بخشی از سیاست امنیت ملی اسرائیله
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133462" target="_blank">📅 15:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133461">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از داده‌های ردیابی: تردد دریایی از طریق تنگه هرمز پس از اعلام بسته شدن این تنگه از سوی ایران، به طور محسوسی کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133461" target="_blank">📅 15:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133460">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKDp4TkGogP2f3fhDjrCox2i9jUwAiBgNxEweWqNvq30-LJgopfSLLkF_KsTZqnDluVzy8Tt0kDcKnp4rncR3G5f5IsOOb0zaLVXPjdgL24xxBEprwwzLp_Kcw7T9sf862KrEC1-yi_Nkv9TrGvd3YG_T9d1qOe1k5n09RMwG37L1SepQPEsX5eFLVm-fAx_IGNDDGzvXfFkMSWI5SXcqkNzC1bvhjRz4iCTmslm6GUVgu-8x73ekSYc4jwDwSPOtBLqYwjME5ElAM2Lb8xfz_h9R3xxr1D3dXBQ6-LZaEKWhnmBK0l-OFIxcxLDqdiYUl2BQHnmqmcsmDnb6y6WDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاتس وزیر جنگ اسرائیل درباره لیندسی گراهام: او دوستی واقعی برای دولت اسرائیل و یکی از سرسخت‌ترین و استوارترین حامیان ما بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133460" target="_blank">📅 15:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133459">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
عمان، سفیر ایران رو احضار کرد و حمله‌ها به کشورش رو محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/133459" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133458">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / وقوع حادثه دریایی در سواحل عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133458" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133457">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نواف سلام، نخست‌وزیر لبنان، ضمن اعلام همبستگی با کشورهایی که هدف حملات ایران قرار گرفته‌اند، این حملات به اردن، بحرین، کویت، عمان و قطر را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/133457" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133456">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
صداوسیما: از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات در استان هرمزگان شنیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/133456" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133455">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1747c4666.mp4?token=YMnawhHzNtPBOXn5PZn1_B1M96Z0OFlWxTf7gcs8BhWPoTueCo2vBKyHyHmJqgLzn60XLIvEQUzShTsbmNiFQRDsv8zlxdbwtbfaWMNc7pKm1NINRyAFwryZL6O6dy2-yGHXqwiB5cTlWRIsxnYk8BX16-zuEm6snYQE1jCqmxtikWRX5BSkv170lnUDYHnHwpSaD9SwCftdMat-o1ycBzFJz5GfGWlZ-9LkN0SzA1ZoysLLiZ0EGVIwHGBrbrShqVcVORidwjk_bbHy2IDcROCccs7GbyWxxXNEZtY9qyEZPqbGwaAjdXFtQXiclGW7m6-uG4rv7S7y0SWf_cLbtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1747c4666.mp4?token=YMnawhHzNtPBOXn5PZn1_B1M96Z0OFlWxTf7gcs8BhWPoTueCo2vBKyHyHmJqgLzn60XLIvEQUzShTsbmNiFQRDsv8zlxdbwtbfaWMNc7pKm1NINRyAFwryZL6O6dy2-yGHXqwiB5cTlWRIsxnYk8BX16-zuEm6snYQE1jCqmxtikWRX5BSkv170lnUDYHnHwpSaD9SwCftdMat-o1ycBzFJz5GfGWlZ-9LkN0SzA1ZoysLLiZ0EGVIwHGBrbrShqVcVORidwjk_bbHy2IDcROCccs7GbyWxxXNEZtY9qyEZPqbGwaAjdXFtQXiclGW7m6-uG4rv7S7y0SWf_cLbtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: به ارتش دستور آماده‌سازی برای عملیات مستقل علیه ایران داده شد
🔴
یسرائیل کاتز اعلام کرد نخست‌وزیر و او به ارتش اسرائیل دستور داده‌اند برای یک عملیات نظامی مستقل علیه ایران آماده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/133455" target="_blank">📅 15:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133454">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKo9YwoMn3hJghW8iR9eESxhHOvbIkuWeFkPEe0kSpAcTV6UQ2Nhm_Ygim0ZwThCUzRp5dSvuLcH8fREJM5vjBmgu8G6uYqdfFD8Lk0GFIgP4nFyfj3JNeySZ3xyATlcz1eWlcdo51a0oWDdE1nVsGBlOrf5D7Vc9DhZZ5NkMABaSqNnS9-oXoANTdrhcYr4H8bbmg1GSwL4VTJv0EZaUaYi4_BrhuF6W2DUUpd4s1sQtsW6QYm1w6gGDHMvdYGQQp_zdiwD7WdduzhWZ_TLjXHwN9sxB5er8VZluqQZI3EXUIv1hYatRjR8t37I8KScIzhs-Jr2mDpTpVrL9xHeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تبلیغات موساد در vpnها
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/133454" target="_blank">📅 15:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133453">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhloYaGqktCVaFJPg3FtNOVb00e24njyPCE0Mp5KmFfgLXpI1bxRTaO4LR5LfhtTikZS35N4UT9nZKd3guH40iYb0A8MPti5Qfp8HjrAcUZWjp2m5beKmWtvGU0q4VYbx8S1whD-zQtAYwpBMIgsfxYf99x82L8qLdN0h_VGYaYDbzoN1dJ4ltIot8dfLhSUNNuOa5t382Psl4u4-2SkcNwG9MqyqnzpSbk8kq2MkMmgCZ9ALc6OS1IZyZpz4dBEFufXSA0JG8r_N9klEjKs8VfVxeKUSmvtiNoFqizKa8WrDqPTadsZr_vviC9a4g7JOlsRfeWtOBzx2bt0wypayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کل دنیا دارن مرگ لیدنسی گراهام را گردن ایران میندازن
🔴
جوگیری و گنده گوزی و حماقت تندروها ایران را نابود خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/133453" target="_blank">📅 14:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133452">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1926fd3153.mp4?token=ZtpQFxp8r8HpBJcezCNAIsvufRI8Nu9BiSmBSaHVwHjM2WhjdhuLflKdkwXT3cYas0a4EHWg1HztoCo_shLLZ-MS89Bq_jntfvuV0n9ohVI-9ytQh7OtFjASRaC4wVJzugW17q8LBGbuFmA8foBA3QEVDptpB7DwbhZC8ZRftTPVTco3SMZzf_Zlx5bgQA4bBC5MdMA_ucbvnopYDnlQ9ZCONhFLca_c35IPbqt0hUlNFULaOValTRU6WKdcOtRnbe4zFV5X5Ue4u4R9cNeXRg3MlrmgdRYHuOa79HFYwFSx_6bAKXi5WTrTNmOiggqKUOKsJgq2kntcEKsGTKGPTj-28Oi35_nPkBFVRubGAj8BWZXF6Q0pAkM7aFD4idTzBC3NiMlxkJNbWQsSt5B_NnBg9JnQ0gpFhsmPFliCTpGvkyYh8Y4B5z4RacvuDRpMGBwI6HSb9_JwsIGddrxDZutOffA7s6OePN_3naN5cfN0exSWQCr5uMBdG7sbItX7mubH9K5PBP5pNrBOKca03aYWksktADHlipRFbqkRtBlVwtjE7ztqldFwTdAEjm5k2lTEoKXYrp7yhqRT8Vj98I6K6knI-QPtoLmvOFTjVbmlnutJUpDVPBPD5CmPb48WTaRPGKnocum2qbIpYN9ips1d8MuQR6wXxVBBSI_n1p0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1926fd3153.mp4?token=ZtpQFxp8r8HpBJcezCNAIsvufRI8Nu9BiSmBSaHVwHjM2WhjdhuLflKdkwXT3cYas0a4EHWg1HztoCo_shLLZ-MS89Bq_jntfvuV0n9ohVI-9ytQh7OtFjASRaC4wVJzugW17q8LBGbuFmA8foBA3QEVDptpB7DwbhZC8ZRftTPVTco3SMZzf_Zlx5bgQA4bBC5MdMA_ucbvnopYDnlQ9ZCONhFLca_c35IPbqt0hUlNFULaOValTRU6WKdcOtRnbe4zFV5X5Ue4u4R9cNeXRg3MlrmgdRYHuOa79HFYwFSx_6bAKXi5WTrTNmOiggqKUOKsJgq2kntcEKsGTKGPTj-28Oi35_nPkBFVRubGAj8BWZXF6Q0pAkM7aFD4idTzBC3NiMlxkJNbWQsSt5B_NnBg9JnQ0gpFhsmPFliCTpGvkyYh8Y4B5z4RacvuDRpMGBwI6HSb9_JwsIGddrxDZutOffA7s6OePN_3naN5cfN0exSWQCr5uMBdG7sbItX7mubH9K5PBP5pNrBOKca03aYWksktADHlipRFbqkRtBlVwtjE7ztqldFwTdAEjm5k2lTEoKXYrp7yhqRT8Vj98I6K6knI-QPtoLmvOFTjVbmlnutJUpDVPBPD5CmPb48WTaRPGKnocum2qbIpYN9ips1d8MuQR6wXxVBBSI_n1p0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ترورهای هدفمند، ایرانی‌ها را دیوانه کرده است
🔴
یسرائیل کاتز درباره ایران گفت: یکی از اولین شروطی که آن‌ها هرگاه مذاکرات آغاز می‌شود مطرح می‌کنند، این است که ترورهای هدفمند باید متوقف شود. این روش اسرائیلی آن‌ها را دیوانه کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133452" target="_blank">📅 14:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133451">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwV1Ut1rYid6SrcpsZOPqX6_8MfZAlPJOh3SUvL55VafmqbBZKuGenqZ6V24_Guh00BKKHv2JV7oB8z6p5bQL5wFf2_Otzdny_I1yWgBysQBnooEnBxTn_4NMPFjumH7jDrrJr2SitAvbo5IlvSdCDeM_cpX_5Y_xTCSzsMvNHpp1Ei0Ar5OfOmRDVk_WEK8l8ka0DtGiQMwJLDDTyNbBhmBJifeIwQHSnSj-OO-nGL24-9YJKtDZOCD9RM-7BsuKy3EEkxZNNN4wiqtsBz3-7-qaeLxhd_yeErnBCG8iDDGv0dXeepTrP2yu6_wDQ7hTt0PEJUFWOIz8CZwL1KBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی: علت مرگ لیندسی گراهام دیدن تصاویر میلیونی مردم ایران‌ و عراق در ادای احترام به ‎رهبر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/133451" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133450">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بلومبرگ به نقل از مرکز اطلاعات دریایی مشترک گزارش داد: مسیر جنوبی تنگه هرمز در امتداد ساحل عمان همچنان باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133450" target="_blank">📅 14:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133449">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgg0LYss1YR6ije4apdoGwniGyo2YzrOLnm481YWL-_pz_AgB19hgonGCihKtY5QF0ab_xFhWuAivNKkOltJtVGIVf34wcvbmYsaxoym_tbmR22UL35UG70dXORozpJmq44dTVf8jZSkQ9V8JW06fTQZKtF8e1osKdkllZbNKmfTF0yEKytpyn1ew9Fn-OLUU5JGS-ckkVpKfCYV9nmgGyDgvJ5a1b8rHQfffSp2hol9DDOT74ZwaCG7uJ_wdzKKWvM0Hl5W2FdAQMewX7fLlyxmGCRs6kNiecF80utp11pjkPp_-o4C0Vpa0m-O4HwK97ajClZADLv_3G9rwFkG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تسنیم: دیروز یدونه موشک آمریکایی تو خرم آباد رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133449" target="_blank">📅 14:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133448">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoXg_hqq2xLjp-KNfkQv_fWyTU9mC3RV54dNru4tdLNWOg1rJQeGcAh42YmSjeqT1z-2knTupLUeF23e-5Uj-kTgNIIrzWSm6xU3jvGZUYae1hoU8DVZPDAPWpoA99opnZbtvygZln0SjCgAc-EmZszco78yVZQTTcoUA0z4R2qEnhQdY2oXD5XrfdcPPRNcf2pap4bpojZPqOOcbUSKQxOHI6sW21gM-Vp4cY4zVmFwg_Mjwvnh1iT0514sRwVPhDS4ckm1dDV1dmTU2KeARbw1mv8ewGGBw_BbFe4wLT5rUTETbkFhn5F3b0ovSR2Ue5nGJKTHDXo5cVe7w_qtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فردریک مرتس، صدراعظم آلمان:
سناتور ایالات متحده، لیندسی گراهام، یک دوست واقعی و شریک آلمان در پیمان فراتلاتی اقیانوسی بود. بیش از چهار دهه است که در کنار یکدیگر ایستاده‌ایم.
🔴
من فقدان او را احساس خواهم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133448" target="_blank">📅 14:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133447">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی :‌  تنگه از ده‌ها بمب هسته‌ای مهم‌تره و ایران از اون محافظت میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/133447" target="_blank">📅 14:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133446">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / وقوع حادثه دریایی در سواحل عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133446" target="_blank">📅 14:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119b6d9912.mp4?token=ZcZVeJY7CqxakXEey5wxv_o2q9FOKeKNdmmDQjZF6AnLZPk2o1uY26Wt6grTjFnIBoZOTVwQrC3Ck3Sefy2msxygCRvI0p1bz0Z113u_oUT7FODLMZjk4oaZuJYBIfK5SnIMNWzl_sXGbTs-iOxOx-t20Hxie0SyjWFerWi8STxm7VFq6XQSRnVzPb0JCd3AQSeKjeI1F8WImCah_0IKZoRAaLRpquDjj5uAD5h_M6qC4F-qHuLEx0P0Wb5O9hIVpQMtvJY7K4c9ELNh8htAc7ZAJjcA-F_8THW7ZJ8JiYP_wei3ck7uoEps9w2TC-cHmHPhPAG--c9mhnJSnliNQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119b6d9912.mp4?token=ZcZVeJY7CqxakXEey5wxv_o2q9FOKeKNdmmDQjZF6AnLZPk2o1uY26Wt6grTjFnIBoZOTVwQrC3Ck3Sefy2msxygCRvI0p1bz0Z113u_oUT7FODLMZjk4oaZuJYBIfK5SnIMNWzl_sXGbTs-iOxOx-t20Hxie0SyjWFerWi8STxm7VFq6XQSRnVzPb0JCd3AQSeKjeI1F8WImCah_0IKZoRAaLRpquDjj5uAD5h_M6qC4F-qHuLEx0P0Wb5O9hIVpQMtvJY7K4c9ELNh8htAc7ZAJjcA-F_8THW7ZJ8JiYP_wei3ck7uoEps9w2TC-cHmHPhPAG--c9mhnJSnliNQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای بدون سرنشین «گران-4» که تحت کنترل نیروهای روسی قرار دارند، به یک کشتی گشت دریایی نیروی دریایی اوکراین، یک کشتی باری و یک کشتی صیادی اوکراینی در بندر چورنومورسک، واقع در منطقه اودسا، حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133444" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133443">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: اگر ترور رهبران به رفتاری عادی تبدیل شود، هیچ کشوری امنیت نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/133443" target="_blank">📅 14:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133442">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euUg7EJH63yNP-k3EIP8hcVHJlHLk9SfLrdgigcwzCa2lv2U1K2OpzboNlbOx71YxWnrRg9nLMbq2jyfOo-NNhbtVcd2MTxOKRJa9ZAcoGWYlXfvegyuTSXpxirb4IJi6rvYSvjIO2K5trw_n5oqJ21iTlzThunexj8vRE5Gucp4VDcJnwV63Bi-B7TuOk0xOciB0YDqgTTdUKGWpklPCRFFd3q5YAsentH8AiDYN7TSrXpFC07tvcyjFL0MptsfnbW8ycCCcmTizAMz7ShpIbPEQFsY7JvLTVcteJxyyCKTe-ZfP7PQCfDX0YCAPqMnXS3AmElOvVoveOhhaqecNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روسیه کامیون‌های نظامی خود را با نوارهای درشت سیاه‌وسفید رنگ‌آمیزی می‌کند تا سیستم‌های دید مبتنی بر هوش مصنوعی را در پهپادهای اوکراینی گیج کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133442" target="_blank">📅 14:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133441">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEwoP_z4idZGNvy40RSFHO9WmQTASxSr_U4wxmB50zM9NsFXjvicQh_QlKanxFi-vPbAxwVeRLxc3nTuVgYpxzVE-hlvKUiDFXiJAmEMEDSBdMLJGdQHWz_T1awqrEffEZXY0Sb4SWG2Ej1ab-F75L5JNpFugNCLIz8Z4zqFqOnkdZkKnq4xFQp4ime8zn0fXJDUoTBftXLPy0W41ZQZmHWKZtOHI6XC6-qbXyYfbV5pWUJb6VsVsqr1wqm1tF1-P2XVlacqdKPs98dpL75MMkJe-MxNdfy_bPoobiedaQA3muh50fLOBrBoWr3plyHC6u34r-7gNVJmMhI0dVkuSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز مشترک اطلاعات دریایی (JMIC) اعلام کرد: با وجود ادعای ایران درباره بسته شدن تنگه هرمز، کریدور ترانزیتی جنوبی در آب‌های عمان همچنان باز است و تمامی کشتی‌های تجاری می‌توانند از این مسیر عبور کنند. این مرکز تأکید کرد که مسیر جنوبی با وجود ادامه تنش‌های منطقه‌ای، همچنان عملیاتی و در دسترس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133441" target="_blank">📅 14:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133440">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خبرگزاری «مهر» از کشته‌شدن حمیدرضا دهقانی، ناوبان سوم تفنگدار نیروی دریایی ارتش ایران در حمله شب گذشته آمریکا به بندر جاسک در استان هرمزگان خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/133440" target="_blank">📅 13:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133439">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
روزنامه ایندیا تودی: وزارت امور خارجه هند طی بیانیه ای خواستار کاهش فوری تنش‌ها در تنگه هرمز و یافتن راه‌حلی دیپلماتیک به منظور بازگشت صلح و ثبات به منطقه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133439" target="_blank">📅 13:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133438">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2dade27f.mp4?token=VntahllHTHo8TQlDJUDEnbJLgKJ8t5N5tgr-fgU3OqnX_d1_ac1iDaRsWBF3OSTFK6fM18R92R_nP8KWFD5FidBfRNOxnqlH091xLpMbjmOn4mNEL9_RbFEDVQrez5O38LpTfxF0JrE0Rvo6bbmtHyyNM_b6XGL4po9HLy90HDfqCurEq4qJPoKJP06Y4noJGmT8kUCeEyoEnCzNsx3rkz16GhziC9hmNF0iqwDV0KtIUB8ZDEvYAmTFqb8WNfikxDSTfv5Syos9PsAbUSuYCm0NnLwaJujMM40lPQ_rHvIsv2Il2vsil5H_7Y1ZbI_qAuOsFA6mu9LIrzNca_1FEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2dade27f.mp4?token=VntahllHTHo8TQlDJUDEnbJLgKJ8t5N5tgr-fgU3OqnX_d1_ac1iDaRsWBF3OSTFK6fM18R92R_nP8KWFD5FidBfRNOxnqlH091xLpMbjmOn4mNEL9_RbFEDVQrez5O38LpTfxF0JrE0Rvo6bbmtHyyNM_b6XGL4po9HLy90HDfqCurEq4qJPoKJP06Y4noJGmT8kUCeEyoEnCzNsx3rkz16GhziC9hmNF0iqwDV0KtIUB8ZDEvYAmTFqb8WNfikxDSTfv5Syos9PsAbUSuYCm0NnLwaJujMM40lPQ_rHvIsv2Il2vsil5H_7Y1ZbI_qAuOsFA6mu9LIrzNca_1FEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنی که صبح به صبح و شب به شب کمر مردش رو خالی میکرد: دلتنگ رهبرم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133438" target="_blank">📅 13:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133437">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نخست وزیر عراق فردا به واشنگتن سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133437" target="_blank">📅 13:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133436">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
امارات: تهدیدهای موشکی که صبح امروز شناسایی شدند، خارج از مرزهای
کشور ما بوده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133436" target="_blank">📅 13:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133435">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بحرین، قطر و اردن : حملات ایران رو محکوم میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133435" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133434">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: اگر ترور رهبران به رفتاری عادی تبدیل شود، هیچ کشوری امنیت نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/133434" target="_blank">📅 13:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gX9pyoDXcRAWg0bGJJu8bYtG1bV-eYP4_s4qkH71ROEcZ9GsS1Jtq_KRLv9ZRJrr1FldTvV7HrkssXDBp3Cq5_BwkOtX5HaG3OrBGeXflVxOpbBf5_ZafY2UzlkuEyqWYZIPUkMTGKsGBfF9GoadD8HvECRk2cbTEmtt9eaQQ8hIOj2t1i5wQFX5pzRQoExDJ1rhwmKgy8GE8Hkhd08AAfrwypJcGmBzpofBcp_s-6kjq-yWJEwEtbFDKTGut4oeA8ei3BW5tmbfKGxEseozmmRsF0TyajXZxd8fXQJYrDViGraaR4WqDoSWUCEgKK3BAUDIzXVapUanx3feT7KVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsyYrXQ5hQ7k6Nulgkh77iK_hsu5CEVYHew-8LZnBfJSxNcOqvwIfwhy470wjeYOYs7meoo0G3pcXNAC7-lc4IIvZqfRt04RGIupm54zNT_Se0fqNWVcUBuvd8FHeP6Ufb4liWT7viEQzfm2NnWDGLxSjCStjBP3gMuasjoyA1lG5osJYAagTIBSneMKDHNap8az4WbJrMOoBA1eHW9DW7atyEvKliWlJ2_48AN_MntVq8jEh8zKqYmqQzwZcx_kSC-Zpv37M3msUkOpZAKBWwEHCCQDbMRZADiHhgxu4npz2h5-0cXKdXk-LZVklwG-AKH9wa8DQ4S0uf_B0XVP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_GZHwcSQqoRdqmgub3XmilFM8AxrYTgTu0iUUocI6cHbZmYOGH0K9lzZl3ViLP1hWB_NuaFHBFX6rOGwV6VmTqOX9ngDCQ2e-Jq88dfs3cWOuf4jZRBQCSv7Wa9BUgIbU6XwuIdP5gmJf3IFzhu7ISmjnRQke8yr-iuoQRSfeBhcMhYooqTAWZprDA7Co_zkxb8Ntpn6-ADUFnAmkKn_dKPi-EL9NDadKD0p-d6fob3ekyejJgnaI2zLq3seDcGPYJBQx0vwC2XnELOTJFx7oKnOks4K82c9qfzE6Xly4VPaimSg297bY7_ijDZRCsySFVmsnFqRNfBuESElRgqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCKFmwcKVxQYQLvQrS02xdSLCno6Fh36_mmlYh0KZN2uhsFXpnY04x_P-kILbgmrt5BzsWWG8nrC5Bg8Qz365AoqrF6McURpsiLpKoMbyjslCMe9RV9meVAky8ZJvU2u5vNIIxXLu31QY4ETSLJLULn44ZrcrJcZUEHgSU3AoJOOzygKzyT97nDYS15NKhu93OJH-Yv8cWkZja2asMHpqyZJJIQT8uSuJKU-o81pAVdNdLosUuzmmMpuI_6UcfNeJCvgoCC9OFLL7F0JFTBW3Ir7JirjR8Jg4w8XpzoNVhOFgSHZyLwVtJ_Oovi2YcH0q_bUbd2BA1E9UOaa-tpbbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیشب یه موشک بالستیک سپاه تو [لرستان] سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/133430" target="_blank">📅 13:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWW3seiOJ7Toq92Yq1ShUCxJA1XoweBrk3ObEOyWR3PDndwGY8K44GczJthvDzd06h4KdJ3Fa984y0ylQShzUkAVg9cuur1oQZ-VxXhPP4Ch9Y6hSS9IGE-rbrOg4HArrQLvXY8MwIR798DqgWyhAn4N1w6TS41d6of5vRvoOVMhTL_dpIg03MLSFoH666D2ZLzMFJ7vL6xyoRn3vAfUy4jpjpKVKOaiI23UQVymOAwd1Ed23NFtnwid_JmFIfOZOVtQrTMg1Gmcdls4WPcuYRUwZ8iZYsD-mlhlMPrGc6yoDKu5t6v-rrsG08T1t4TP7VGuM1fpKdL_br5U78Q0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس با ریزش ۱۲۶ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۰۵۵ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133429" target="_blank">📅 13:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133428">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رسانه‌های اوکراینی خبر دادند که یک پالایشگاه بزرگ نفت روسیه در شهر سیزران هدف حمله پهپادی شبانه قرار گرفت.
🔴
به روایت «کی‌یف ایندیپندنت»، این پالایشگاه روسیه در ۸۰۰ کیلومتری مرز اوکراین واقع شده و در نتیجه حمله، آتش‌ گرفت.
🔴
به ادعای رسانه‌های اوکراینی، این پالایشگاه ظرفیت فرآوری حدود ۹ میلیون تن نفت خام در سال را دارد و سوخت ارتش روسیه را تأمین می‌کند و فرآورده‌های نفتی را از طریق رودخانه ولگا و دریای خزر نیز صادر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133428" target="_blank">📅 13:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سپاه پاسداران: ما در عملیات امروز از موشک‌های بالستیک مدل قدر، عماد، خیبرشکن، فاتح ۱۱۰ و ذوالفقار استفاده کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133427" target="_blank">📅 13:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133426">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
سطح تهدید دریایی در تنگه هرمز همچنان در بالاترین درجه خطر، یعنی «شدید»، طبقه‌بندی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/133426" target="_blank">📅 12:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت حمل و نقل قطر از مالکان و کاربران کشتی‌های دریایی خواست تا اطلاع ثانوی، موقتاً دریانوردی و فعالیت‌های دریایی خود را متوقف کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133425" target="_blank">📅 12:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: نتانیاهو در حال بررسی امکان سفر به مراسم تشییع جنازه لیندسی گراهام است.
🔴
در صورتی که این سفر انجام شود، به احتمال زیاد با ترامپ نیز دیدار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/133424" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
احتمال تحویل ۶ فروند اف-۳۵ ترکیه تا پایان ۲۰۲۶
🔴
آمریکا ۶ فروند F-35A را که پیش از تعلیق مشارکت ترکیه برای این کشور ساخته شده بود، همچنان در انبار نگهداری می‌کند. با پیشرفت مذاکرات واشنگتن-آنکارا برای بازگشت ترکیه به این برنامه، احتمال تحویل این جنگنده‌ها تا پیش از پایان سال ۲۰۲۶ افزایش یافته است.
🔴
ترکیه در سال ۲۰۰۲ با سرمایه‌گذاری ۱.۴ میلیارد دلاری به برنامه F-35 پیوست و قصد خرید ۱۳۰ فروند داشت، اما پس از خرید اس-۴۰۰ از روسیه در سال ۲۰۱۹، مشارکتش در این برنامه به حالت تعلیق درآمد. هیچ مقام رسمی هنوز زمان‌بندی دقیق تحویل را تأیید نکرده است.
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/133422" target="_blank">📅 12:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133421">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی دولت عراق: هیچ پایگاه خارجی در عراق وجود ندارد، بلکه مشاوران بین‌المللی در خاک ما حضور دارند که به درخواست دولت است
🔴
خروج آن‌ها هم شامل تحویل پایگاه‌های متعلق به هیچ طرف بین‌المللی‌ای نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133421" target="_blank">📅 12:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133420">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
امارات: «تهدیدهای موشکی که صبح امروز شناسایی شدند، خارج از مرزهای امارات متحده عربی بوده‌اند.»
🔴
در این بیانیه آمده است: «اوضاع همچنان باثبات است و سامانه‌های ملی در بالاترین سطح آمادگی قرار دارند.»
🔴
پیش‌تر در روز یکشنبه، سازمان ملی مدیریت بحران، حوادث و بلایای امارات (NCEMA) اعلام کرده بود: «سامانه‌های پدافند هوایی هم‌اکنون در حال مقابله با یک تهدید موشکی هستند. لطفاً در محل امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده در وب‌سایت‌های رسمی را دنبال کنید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133420" target="_blank">📅 12:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133419">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
خبرگزاری مهر :  شبکه ارتباطی تو کرمان بر اثر حمله آمریکا دچار اختلال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/133419" target="_blank">📅 12:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
دیوان امیر قطر: پیکر حمد بن خلیفه آل ثانی پس از اقامه نماز در گورستان لوسیل به خاک سپرده می‌شود.
🔴
از امروز چهار روز عزای عمومی در سراسر قطر اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/133418" target="_blank">📅 12:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133417">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت بازرگانی آمریکا با ارتقای جایگاه امارات، محدودیت‌های صادرات تجهیزات نظامی، فناوری‌های پیشرفته و صنایع فضایی به این کشور را کاهش داد.
🔴
واشنگتن این تصمیم را قدردانی از همکاری‌های ابوظبی، از جمله در جنگ علیه ایران، عنوان کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/133417" target="_blank">📅 12:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133416">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
فرودگاه سیرجان بعد از چهار ماه تعطیلی دوباره باز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/133416" target="_blank">📅 12:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133415">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کانالای ایتا: گراهام رو ترور بیولوژیکی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133415" target="_blank">📅 12:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133414">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجارهای کنترل‌شده در تبریز به‌دلیل پاکسازی منطقه از مواد منفجره
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/133414" target="_blank">📅 12:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133413">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبرگزاری رسمی عمان به نقل از یک منبع امنیتی اعلام کرد: چندین نقطه در استان مسندم هدف حملات پهپادی قرار گرفته است.
🔴
استان مسندم، یک منطقه کوهستانی عمان است که بر تنگه هرمز اشراف دارد و با امارات هم‌مرز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/133413" target="_blank">📅 12:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133412">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد سامانه‌های پدافند هوایی این کشور طی شب گذشته ۳۴۹ پهپاد اوکراینی را بر فراز مناطق مختلف روسیه رهگیری و منهدم کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133412" target="_blank">📅 11:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133411">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
تصاویر حملات موشکی هوافضای سپاه به پایگاه‌های آمریکا در منطقه منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133411" target="_blank">📅 11:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133410">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت خارجه هند: در حمله به کشتی کانتینری «جیافاس گلکسی» (GFS Galaxy)  ۱۰ نفر از ۱۱ تبعه هندی حاضر در این کشتی نجات یافته‌اند، اما یک نفر همچنان مفقود است
🔴
سفارت ما در عمان اوضاع را از نزدیک زیر نظر دارد و در عملیات جستوجو و نجات در حال انجام، با مقامات عمانی هماهنگی فعالانه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/133410" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133409">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNpwQtUKds2YFwA6hrltzoTpAkJ5PbHNQgcRVBDa50_UIQb3zsfrnbcSbaK5a9bbe7rczKMrLsnzdyLBnfS4Mbp7o9u-IJWnyM_y_mNkT5KXwvOmOB-SRtViGEaQ15R8wNFc7yBY1unJFQgr06ptAvrjakr2-deGzY888NHLAMnAM4N7PBfqy-69g3i0IU1THUGiBTn3sARBOZVXz2sE0-57F91zT9E6CDxkpP6UK9l07hVw5LWtSqwYzJBLxek83rmf_E9sg2n__pw1ua18i8i81tdzmn8RAOYCK0SqhYDIS3m0pTgYk2Sq8WrbuJFoU4SNpBawOQ5GwRdVjeLmSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: گراهام اولیش بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133409" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133408">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شریعتمداری: اکنون باید به زیرساخت های اسرائیل حمله کنیم
🔴
باید علاوه بر بحرین و کویت به امارات نیز یورش ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133408" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133407">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuTdIxWHHCXLHiGQ3_zXhficzgcqUmjLpNgnj7h1gyFyp-0tDmXFtz6EDzm_U0CDYLKFIopgM-8ivC8J8WMleyw20dhRv-1wAL_kD1e2Zan3Pic46OCLUz9GKiwhvx7MLJsAUASogvZNbYXA3W2cqw7aXqbGpgAV-dZATlQZPAV88QIePUBmQSVyCFtPuW0PlnNm5mu4bOB_OrvuQTbcuO0bzWLTDRGUjD_Lqd3jDJBlBymQMufpHAatrDzmOoTSszzGrGQA29zXTOZAnp8SqSgWC9nDcPI1RzUN82l5zdT_VAk6tpmE-P6Hje9RAhOLjANS2K0LhM0CzVCbZ5FfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش کنایه‌آمیز مرندی به مرگ گراهام: حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/133407" target="_blank">📅 11:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133406">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkgRqvKWqV25XKgam1IGgPuXm8qrecJ6LMQjJvKm1gO2OXNXPKMUn3hZdtY9hgyE9j5l7OCRWObvvqySg4tsZr1zt0xSrq9Tt0fLPDbCh-FF4mr7Pabh0Eb4j-4p1pvAoDz7JiZ13MFD5oFbXfZy8kcKchlf6I1Mv9Me46A0iu03ZLpiH3Ti5qgvCiv2WDWazvM0FnLnFAkWsxGFP_PqDmtAM3JnxdcegGB5WXeYP_Rb1-l9Va1rYYYmEmTCRhdzz5JeqpYryyTgOT66-h83iP3z8mxfqDkKIeuncRzyPDnP1gDKWuqpN_uD3GER-fCIjqHAv2SEK9pjIYQT7dT5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی با محکومیت شدید حملات ایران به کویت، بحرین، قطر، امارات، عمان و اردن، تهران را به نقض قوانین بین‌المللی، تضعیف امنیت منطقه و تهدید آزادی کشتیرانی متهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133406" target="_blank">📅 11:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133405">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
مقاومت عراق: سلاح ما قابل معامله نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133405" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133404">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd35346900.mp4?token=nTjLizKcEyzl8RLOl2ZQMWUx4tFX58EWWtTJ7-3Gcu56xsvNQcDohFt2HvWVSOI31PJx0_GLXBRMkT-ybErPjViTCeij9I99o3_NuyMfn2UkLTOIui3LXiSZ_Yqmv-EKAIbK0z8InVVsGXTL-FfNpBLMDLF8_ElI8nLU067J9ci3Y-t_nJk83zM779Axvie-Zq4lQD4fOun43f4BBgB8rFCEJC67f6HD8fs93sbt2Y1gn4_2DVLLmTRdT9peyl4PL2DyPaOjYZ-jauPmbdb0vAAFTA_yIH8MWKvqJhGBCGWWPQhaaMnpP0MoEppqlClIREr5-VWC5RZE6yTqz5pWwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd35346900.mp4?token=nTjLizKcEyzl8RLOl2ZQMWUx4tFX58EWWtTJ7-3Gcu56xsvNQcDohFt2HvWVSOI31PJx0_GLXBRMkT-ybErPjViTCeij9I99o3_NuyMfn2UkLTOIui3LXiSZ_Yqmv-EKAIbK0z8InVVsGXTL-FfNpBLMDLF8_ElI8nLU067J9ci3Y-t_nJk83zM779Axvie-Zq4lQD4fOun43f4BBgB8rFCEJC67f6HD8fs93sbt2Y1gn4_2DVLLmTRdT9peyl4PL2DyPaOjYZ-jauPmbdb0vAAFTA_yIH8MWKvqJhGBCGWWPQhaaMnpP0MoEppqlClIREr5-VWC5RZE6yTqz5pWwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اعلام مرگ لیندسی گراهام در شبکه CNN: "خبری به سی‌ان‌ان رسیده است، خبری که هیچ‌کس انتظار شنیدن آن را نداشت… لیندسی گراهام درگذشته است."
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/133404" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133403">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5IlQGijw3sHDO0G-3cW6E6V8Mt8xUYxsGtSlY4G2OJ4Vm2OaxYN7cNWr4YayjOV5HWRXeN97ogAR4e-AZsuU90BgOlhoRsepwI9qu3HDdmI2NDP19WI6WOENUyMHEHCwZq6lZlCrOYYO7Uv3aqwhuLB5SbndOkohmqAvWIqqf8YbNRfFVWuIreCjS5SGdHpmB5tPUYB2aEarjApDmNUD2g6b2-yvbIFkBR-rdQbXXe3xZcYDsLJn63JH6hpEyRrt1ltSUG4oHhu8wabg-k4VxKJHFVSkop_qqsU4AupWmLlQ5ETR7J7v7vvwRyf7WsFRiDmAw0CjxAj36NtkJ_ZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: اسرائیل و آمریکا دوستی بزرگتر از گراهام نداشتند
🔴
نتانیاهو با ابراز اندوه عمیق، سناتور لیندزی گراهام را دوستی عزیز برای خود و اسرائیل خواند و گفت در آخرین دیدارشان به او گفته است: «ما دوستی بهتر از لیندزی نداریم.» او گراهام را کسی دانست که امنیت اسرائیل و آمریکا را جدایی‌ناپذیر می‌دانست و تأکید کرد اسرائیل یکی از بزرگترین دوستانش، آمریکا یک میهن‌پرست بزرگ، و خودش یک دوست عزیز را از دست داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/133403" target="_blank">📅 11:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133402">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
یک منبع امنیتی اعلام کرد «چندین نقطه در استان مسندم عمان هدف حملات پهپادی قرار گرفته است.»
🔴
استان مسندم، یک منطقه کوهستانی عمان است که بر تنگه هرمز اشراف دارد و با امارات متحده عربی هم‌مرز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/133402" target="_blank">📅 11:05 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

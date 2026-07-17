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
<img src="https://cdn4.telesco.pe/file/TsHtSeINuSNnBx8tegBWfWK5_PwlLgkeap7aLRPX0k8-f8LTVDZuiCFHffd_kK2reAGRcsRHyU-FxJ9hFyBltcin3p6gwmU3BiKRXtZ8mPFjvslGkk6T8xmDU-grweQNlHc1bJBimdntzBzMkoARG0qOCe6coBuktnPGhEQ0eyV7bR0_nAsaYlecMOCvf0tqJ0m17h4kQ31aj8vn_Zp_LJiQfxxXOWiRTmhcwhE2yIHgRpzYX9_peQ6lvJzUPz8JHY_3f06D73_OS-S3fUVdJVA_okdz6xebKEugyi-AXbl-T4c-Jv8bbdRFktpuNzPTzwodfGE6KqE3XcY1zQ2sww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 14:08:44</div>
<hr>

<div class="tg-post" id="msg-135026">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHYREC3ytBPPtBFyrLaeipdy_LGutk-5N12asJOJe0Ms6nbuHiJdiiiBjONaFer8rezvUEMvwd7EzaIGC3Ugpc2juQMU4-6YjC0Y_cLWaRLgTM6kAk4-SLqpJN_ziBj6TuqDdj2rJi3JCHNWReaMuj1tl-ucDxpQfCrQ1GHKkobDATFyKnZkvvgKFC1Ia7H5VOvmc1GmqIECjE5A8V-ALMMh5IXaEzzHX6G-XoBcYdt3xBl-0oWSI8Y3TGoxvzsyiau4TZ6YTDLYCCKjWUFCfZwXe3mwBNKqoolY5ycQe-6ktlTd1ASQku8bOQ-FQuWjjpiqLhObtYsTK_a1RuC50w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی:
گرونیا بخاطر جنگه دیگه! طبیعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/135026" target="_blank">📅 14:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135025">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce491105e.mp4?token=O2rTjnUtwqCajwfa28OrKfBMZTEwvlADKe0yysypV9Crh1JGM8xvid47yhi_aKTQ2XLz7rWRgEy0Ph9AwmC75vkmbDovwQC65ZZLYbmKZ1YmrIZa7kkq0Fj5XG-XNcTCTYiy_AiAVwCayVLpCEbeP6Lo3KhBYMdz5ut8ut36YIQG9kZFUcDBHHAc1jS3tuwErgvbkRfUxF81X9wonybbPCq3jXJGAs9OUANG4GZcDYpD5pjaKmbTfIyxT2h9WNeMUTT1emAEKRMebsSHQlBMed7Oba4ZfR8Sw6Yyc1Swrr0TMLAuyj622wzgTwv-0V3YcBjLDrfWXKdtknGq4y9OMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce491105e.mp4?token=O2rTjnUtwqCajwfa28OrKfBMZTEwvlADKe0yysypV9Crh1JGM8xvid47yhi_aKTQ2XLz7rWRgEy0Ph9AwmC75vkmbDovwQC65ZZLYbmKZ1YmrIZa7kkq0Fj5XG-XNcTCTYiy_AiAVwCayVLpCEbeP6Lo3KhBYMdz5ut8ut36YIQG9kZFUcDBHHAc1jS3tuwErgvbkRfUxF81X9wonybbPCq3jXJGAs9OUANG4GZcDYpD5pjaKmbTfIyxT2h9WNeMUTT1emAEKRMebsSHQlBMed7Oba4ZfR8Sw6Yyc1Swrr0TMLAuyj622wzgTwv-0V3YcBjLDrfWXKdtknGq4y9OMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدخشان از دست طالبان لغزید
🔴
گروه تازه‌ تاسیس مخالف طالبان موسوم به سپاهیان میهن صبح امروز موفق شد برای مدت کوتاهی کنترل شهرستان یفتل در استان بدخشان افغانستان را از دست طالبان خارج کند
🔴
این گروه همچنین مدعی شده پیش از آغاز ضدحمله طالبان، بخشی از تجهیزات نظامی مستقر در منطقه را به غنیمت گرفته است
🔴
اگرچه طالبان در ادامه با اجرای عملیات متقابل، کنترل منطقه را دوباره به دست آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/135025" target="_blank">📅 14:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135023">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9pBK0O-nr2F8dwqlVl78DEdf9QStVD_I_rjf5mX3wn9NgWU9QjoeMdI1HC3FgJv2Kg8O1ZZ1SJFq5biV6MHbRbLH1C9MZ6jtGMUIal6rdpDZB0ET-rR2jWSYyY4q3sODLKhnUJYeEPEDWpKmSIVFqZMZJQvNlh4687UKCNXLryn2_W_H8tGMHHj8WiulP-r6bVRwnpTv-mzneujqW6LP3fYZwsCE4_7FavjzkAjSS_DoFvmcH2WPK5NzcmWeq3kvqhH7CS3Ti8gWX3fcyFIH1an4PS5wT90QcsHStl5ZVbZ1eYydKTzq4WI7l_LuMetfjNCr3Xo221JOmJbjSqkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر دوباره همه را غافلگیر کرد؛ بازار در تب‌وتاب افزایش قیمت
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/135023" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135022">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRsrTGfQVNTLhI4zCrv8QkaN6PqcN8oa-1G_dJ0bTKRXKnIfsd1fzlyJVk64BEHJJwq2V2llLqbxnsBZBG-AVh10K-3qlYvAreHuQrxBRzlavqBKwUgz2BIA8uhh-PqNtttGlLWHxjRrwnpHXvyViKLaidtBFfTrREPsDkjaS1ewpM5PwmkLsdhOSS54J5nj2E8Zu_kPbEp704LFCBRlqGU4IeD7otmN3tJVx7aHymALAQIQm2El3aHd_dFYEpbll_mzeOceie04beWrwDK-ok4JkWtlAe6F-BJiQP0jjg6VHQmsJKcab84FPGSsDB_pnk_beUgY42-rqHWmajG7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱۰ فروند ترابری نظامی C-17A به خاورمیانه اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/135022" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135021">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
توانیر: همه روزی ۱ ساعت کولرو خاموش کنن تا به جنوب کمک بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/135021" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135020">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در حال دریافت گزینه‌هایی برای گسترش عملیات نظامی آمریکا علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/135020" target="_blank">📅 13:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135019">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سفارت آمریکا در عراق سطح هشدار سفر به این کشور را به بالاترین درجه افزایش داد و از شهروندان آمریکایی خواست به عراق سفر نکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/135019" target="_blank">📅 13:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135018">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در سخنرانی دیشب خود که در ساعات پربیننده انجام شد، به‌ندرت به درگیری با ایران اشاره کرد
🔴
رئیس‌جمهور دونالد ترامپ در شرایط جنگی به دنبال یک سخنرانی نادر در ساعات پربیننده بود تا مستقیماً با مردم آمریکا سخن بگوید، اما او از این فرصت استفاده نکرد تا به‌وضوح چشم‌انداز خود را برای مسیر پیش‌روی درگیری با ایران - که در روزهای اخیر تشدید شده - ترسیم کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/135018" target="_blank">📅 13:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135017">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
دلار هم اکنون 188,250
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135017" target="_blank">📅 13:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135016">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFfjEPBx4jbrTSnn6ES6ptA7D_qfM_sgzh2Uvlx2VvTy_tQJqiPcFzqqJ44yUmy10nDiBZrBw-Td4LOoNI1SfNGYyTTiqlJcLRj-_lyWAosDW_eBgpkFKyrTIf_09wYH6sgZOhiMy01Z_ylIwf_IDUu6I90XJoyyzB3C_NaSQft680s_ojsPVH9pJSbfSvf1MVt4LXPv-yoYAdlkyEFjo6TCx09rcyKNFcepGhAPkEe-AKgqCCzSoGu3KXXYvH92tcXWC2kXsnaWVnusf5jfU9q1iIBvesjORtafxbUAP9rPDgWYN2abIFCFmt0Pjm2fArqip5jxBmQ5EAwk3uQLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در همین حال، ارتش اسرائیل به تضعیف زیرساخت‌های حزب‌الله ادامه می‌دهد و گزارش‌ها حاکی از تخریب گسترده در شهر زوطر الشرقیه در جنوب لبنان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135016" target="_blank">📅 13:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135015">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد.
🔴
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135015" target="_blank">📅 13:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135014">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از منابع امنیتی دریایی گزارش داد: افراد مسلح به نفتکش حامل محصولات شیمیایی «آسانا» در خلیج عدن در سواحل یمن حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135014" target="_blank">📅 13:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135013">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل : موج بعدی حملات آمریکا قراره خیلی شدیدتر باشه و‌ احتمالا تهران و بقیه شهر هارو هم بزنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135013" target="_blank">📅 12:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135012">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد.
🔴
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135012" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135011">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
آمریکا: حملات ایران به کشورهای حوزه خلیج فارس هیچ تاثیر عملیاتی بر نیروهای آمریکایی نداشته است
🔴
سخنگوی سرفرماندهی مرکزی ایالات متحده، سنتکام، به شبکه تلویزیونی الجزیره گفته است که حملات ایران به کشورهای حوزه خلیج فارس «هیچ تأثیر عملیاتی بر نیروهای ما نداشته است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/135011" target="_blank">📅 12:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135010">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b9f44987.mp4?token=PHxaWnj5EgXQPArpuxVh4xIFWz3oRu_sAnfT40Q1Pc2sdzAKOUwDZdew1iUym-mOHkdGyc2yT9kX0JI71ySWPZobAt3_E7eRn4UzBWiK922C6I0JJwXkTvnRkNXub2He-odbe40-tAWWRTjIr_-6eqEEHuMQBFr0BM7oHB6enL-vF0NCODUCcJiKVGIBqfXOAorZTliPFJTtyRON_ePDexwGf-X5sHR7OQ9GTchU1o9MtGFNIbwGk773_AXHMYkUvVQvHgjg768BJr4vW8ecUiN_gV80VgZW8wVKR1Zm86T2purSbfBndvYWnrsaU4Xc0t9kSTMB1H_GrwtNI1EErR5_5M_kpf47en-IpHs4OhEvqyr9kWQKnQWrVkwx9_Vrsqna9pHlEpxP9sBljaOtc1gs_SYjedXNDG_tkFfoViFeemwtMZYAaFfGnPAJ22o7oa_fY1IkRdbNOdfOR3VEvcSf5EG9eTz6mOpZK_S-l0g-OS80dxepBVQuX-ygjYxpvmFjbYUBBgfWvMiUEUWXOJ1AnQXgmsOUeKD7fdySL86oO2TAwWmSqScUvyQtyIWvvsbXiNapNEcdJx2UXLADQOJuAdpyzDGSPeUkgL2pVlJHKK3T0SRvQnVFOgI3pi64lfs_qHEl6pxVA4Gl4Geh7agXgThtiDuecIDET9JFVxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b9f44987.mp4?token=PHxaWnj5EgXQPArpuxVh4xIFWz3oRu_sAnfT40Q1Pc2sdzAKOUwDZdew1iUym-mOHkdGyc2yT9kX0JI71ySWPZobAt3_E7eRn4UzBWiK922C6I0JJwXkTvnRkNXub2He-odbe40-tAWWRTjIr_-6eqEEHuMQBFr0BM7oHB6enL-vF0NCODUCcJiKVGIBqfXOAorZTliPFJTtyRON_ePDexwGf-X5sHR7OQ9GTchU1o9MtGFNIbwGk773_AXHMYkUvVQvHgjg768BJr4vW8ecUiN_gV80VgZW8wVKR1Zm86T2purSbfBndvYWnrsaU4Xc0t9kSTMB1H_GrwtNI1EErR5_5M_kpf47en-IpHs4OhEvqyr9kWQKnQWrVkwx9_Vrsqna9pHlEpxP9sBljaOtc1gs_SYjedXNDG_tkFfoViFeemwtMZYAaFfGnPAJ22o7oa_fY1IkRdbNOdfOR3VEvcSf5EG9eTz6mOpZK_S-l0g-OS80dxepBVQuX-ygjYxpvmFjbYUBBgfWvMiUEUWXOJ1AnQXgmsOUeKD7fdySL86oO2TAwWmSqScUvyQtyIWvvsbXiNapNEcdJx2UXLADQOJuAdpyzDGSPeUkgL2pVlJHKK3T0SRvQnVFOgI3pi64lfs_qHEl6pxVA4Gl4Geh7agXgThtiDuecIDET9JFVxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لغو پرتاب استارشیپ؛ نقص فنی موتورها پرتاب اسپیس ایکس را متوقف کرد
🔴
شرکت اسپیس ایکس دومین پرتاب آزمایشی راکت ارتقایافته استارشیپ V3 را به دلیل روشن‌نشدن چهار موتور رپتور در فرایند احتراق به‌طور ناگهانی متوقف کرد. ایلان ماسک اعلام کرده است که سیستم خودکار لغو پرتاب به‌موقع عمل کرده و تیم فنی باید دو موتور را تعویض کند. پرتاب بعدی این موشک غول‌پیکر زودتر از هفته آینده انجام نخواهد شد.
🔴
این حادثه درست در زمانی رخ داد که اسپیس ایکس پس از بزرگ‌ترین عرضه اولیه تاریخ، فشار زیادی را در بازار بورس تحمل می‌کند. به دنبال این لغو پرتاب، ارزش سهام شرکت بیش از ۴ درصد افت کرد و به زیر قیمت عرضه اولیه (۱۳۵ دلار) رسید. این مأموریت قرار بود ماهواره‌های نسل جدید استارلینک را برای راه‌اندازی پروژه دیتاسنترهای مداری به فضا ببرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/135010" target="_blank">📅 12:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135009">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otUNFHIq-Czsj7HRzFllij3-Uuwq_A5Uh-BUKu_hBT6JbH-OwEJZ1yPikFnI4inuE_LXUZ-n7rTf8dzAAO2EMPwjH_y8Dt5UjHZ3JOS36eWjHeyKusjf5glV_jZ-5jPqJbhuPon43DHE2UnJ2iiAQj2uS5lRr_txQ8umi-rO4yaaOYA8GQ_sbEoHs5owi7b7ff5f21G2WhSCluKVs8wtBspJmrz0OXXujPv1ihLTB67iZW7y68D4hgjWoEKW4OulaUNzx0YHegJWRRpoVrhambaS-Gy4Jw4IXDSr_B8KUrg1Zn3KlOBPTdRUwvnMzAgXKuEQZvA5vAhP-OI7oxMA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا اعلام کرد برای اولین بار در جام جهانی، علاوه بر جام؛ انگشتر قهرمانی هم به تیم قهرمان
تعلق میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/135009" target="_blank">📅 12:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135008">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / ترامپ: هفته آینده خاورمیانه تغییر خواهد کرد و همه باید برای آن آماده باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/135008" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135005">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N11mXOvQQGXXOgvoqqmybRqUKOr6G1_0aeCgPM7Bxwdw7ufgOicUkYOiz24gQaVZjCHYlod7WtUBF1Pq0rlfS7S-9kXRND57eFIWRvNNen8boZFrQgsfQXRa5Q0Q9OQB4tTeh7io-Jr88nH5fzGqtXK8ueyPFreSjAyLZ0twQXumoLB9WFSJdJqOOUSWGnDkmy4ASSzRQrWaE_Lt4B414lD7ub1aNk1Jh-OvaFPQ5oMoKbZspFokECBC1EXEXi1-tdsyR49MAyFbdlQa2BklMhQtYp8oQGJCBWoO9z4zM7_n3oKEvjj2NafLpu0Yu6ZfDTE4wstNx737QhW5rtm02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دست کم ده ترابری از پایگاه‌های آمریکا در آلمان، یک پرواز اطلاعاتی از خاک ایتالیا و یک سوخت‌رسان و یک ترابری از آمریکا به سمت خاورمیانه در حال حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135005" target="_blank">📅 11:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135004">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/135004" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135001">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۲ درصد کاهش، به ۳۹۸۸ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/135001" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135000">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFTsyCF-4RjihZFp5G5ox4iJvq6lCZpGjtclfuEdHP2SjFZ1012QsofxjxRjEMajeBehXTGFygnOc8mnUGdUsWIcQogWdUSg_U03mbDIVeKB0fKlykQphWyf4U1ax6GsGf_QQCjaBQDu9F6KYr5_8o7KxBixIawvBIdmAyj0iucauFSuDimgnCB089BGoOVdqpf0vinYMbQdbOlfe9zSTH8OTmHIDJG5jCk0pgZVsUDXO6blaNEghnivf6KPS9AZI12xWwUsTSxtDn83Ub9I0iM1A5DVZwDqWEmKecQ6WKdVI3fQgwd2wKu1-wNCcCebrXZO-3s29pLEne5zLAlLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا صدور گواهی امنیتی SSL را برای خبرگزاری فارس مسدود کرد که این موضوع باعث میشه اخبار این خبرگزاری به مرور از گوگل پاک شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/135000" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134999">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سپاه: چندین جنگنده و سوخت‌رسان آمریکا را با حملات خود منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134999" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134997">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ec9980c.mp4?token=CgCbj37yBSYhsgzGvatqWGRU9UDXNDC6GUHgqCGTNan61PGp9Bn40m1F0NcTHPRBuqVPNuXVj9MUNOph-9r8MNimECQ-271zWh0UKtSmRyFVovLo41HJULzt1R-HRyDdDiMw3WimZtXLhROyXJaK_slP8WO93LZMFcG7838fG1A3r1uuyU-YqLKGDe1jV3Y7ccH9tdC0T0utJrSjNsuDvrmKNBpiBS4BCbkNepdFSipe6RLshflkhOBq2m4aZQ1oXrdku6UMhCvVUxrnPkw0fOrXS9YETv8TCntcgjDjmz9G7zTnwk_IrhUFlnGYDTjpfBSLUxJv1QSSjZ5q4TtR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ec9980c.mp4?token=CgCbj37yBSYhsgzGvatqWGRU9UDXNDC6GUHgqCGTNan61PGp9Bn40m1F0NcTHPRBuqVPNuXVj9MUNOph-9r8MNimECQ-271zWh0UKtSmRyFVovLo41HJULzt1R-HRyDdDiMw3WimZtXLhROyXJaK_slP8WO93LZMFcG7838fG1A3r1uuyU-YqLKGDe1jV3Y7ccH9tdC0T0utJrSjNsuDvrmKNBpiBS4BCbkNepdFSipe6RLshflkhOBq2m4aZQ1oXrdku6UMhCvVUxrnPkw0fOrXS9YETv8TCntcgjDjmz9G7zTnwk_IrhUFlnGYDTjpfBSLUxJv1QSSjZ5q4TtR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : شبکه‌های تلویزیونی که این سخنرانی من را پخش نمی‌کنند، باید مجوزهایشان باطل شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134997" target="_blank">📅 11:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134996">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رئیس پلیس راه مازندران: جاده هراز به صورت موقت برای اجرای چند عملیات عمرانی ‌۲۹ و ۳۰ تیرماه جاری مسدود می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134996" target="_blank">📅 11:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134995">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وال استریت ژورنال: اختلاف میان محافل تصمیم‌گیرنده در ایران گسترش یافت
🔴
‏ گروهی به دنبال تشدید تقابل با آمریکا و کنترل تنگه هرمز هستند و گروهی با در نظر گرفتن محاصره دریایی و تشدید جنگ نگران وخامت اقتصادی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/134995" target="_blank">📅 11:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134994">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
اسرائیل در مورد نقشه ترور به ترامپ چه گفته بود؟
🔴
اکسیوس نوشت: در جریان سفر ترامپ به آنکارا، تل‌آویو به واشنگتن هشدار داد که یک مقام ایرانی درباره تلاش برای ترور رئیس‌جمهور آمریکا در زمانی که او در ترکیه حضور داشت، صحبت کرده است.
🔴
این اطلاعات باعث افزایش تدابیر امنیتی شد. از جمله این اقدامات، جابه‌جایی ترامپ را یک هواپیمای قدیمی‌تر «ایرفورس وان» (هواپیمای ریاست‌جمهوری آمریکا) بود.
🔴
با این حال، مقام‌های آمریکایی گفتند این اطلاعات بر اساس یک منبع واحد و تاییدنشده بوده و جنبه برنامه عملیاتی واقعی نداشته است.
🔴
بر اساس اطلاعات اسرائیل یک مقام ایرانی در گفت‌وگو با همکارانش گفته‌بود که ایران باید تلاش کند رئیس‌جمهور آمریکا را زمانی که در آنکارا حضور دارد، ترور کند.
🔴
نیروهای امنیتی ترکیه نیز این ادعا را بررسی و اعلام کردند هیچ طرح مشخصی برای ترور ترامپ در آنکارا پیدا نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/134994" target="_blank">📅 11:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134993">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نظامیان اسرائیلی با ورود به روستاهای «معریه» و «عابدین» در درعا، مسیرهای مسدود را بازگشایی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/134993" target="_blank">📅 10:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134992">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: چین به اطلاعات ۲۲۰ میلیون پرونده رأی‌دهندگان آمریکایی دست پیدا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134992" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134991">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن جانشان را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134991" target="_blank">📅 10:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134990">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
جنگنده‌های آمریکایی صبح امروز، برای سومین بار برج مراقبت دریایی چابهار را با سه موشک هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134990" target="_blank">📅 10:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134989">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134989" target="_blank">📅 10:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134988">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
آکسیوس: مقامات کاخ سفید از گزارش‌های اسرائیل مبنی بر اینکه ترامپ قرار است روز دوشنبه با نتانیاهو دیدار کند، متعجب شدند، زیرا در واقع هیچ جلسه‌ای برنامه‌ریزی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134988" target="_blank">📅 10:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134987">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75dbcaec2b.mp4?token=Przbx_mG6VkZlWvEzCp9XCgMXme7XzWFYwaTjhcWwHkevJycxwLlXG3iP2kLR_tsWwD8_10LJkroa-r1Z-MzMN-iq0FsWFnL7Z_34m_FGQs5-XyS9xa4vnE10q_PpCLZlsaD5Ap56oKzJ6Xl1rbAKbZfUcXCL8aj9z9T6ORC5dkyH_AK5XMn0xMxyoNGrnKsdetOd5eLJY2FE-R14UpQzrZ9eb9aPwN1E0fcrziNiPY1rADEE-KOHA8yUkwdnIEcTT_JblC0kRWE7k3XIhzaSIH-3j_X5Gaf4EyLMRzZzDCwvV4Ui1QPgFqjxN6R9u7_uhIVrGv_ja4-jPzZ_eQdCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75dbcaec2b.mp4?token=Przbx_mG6VkZlWvEzCp9XCgMXme7XzWFYwaTjhcWwHkevJycxwLlXG3iP2kLR_tsWwD8_10LJkroa-r1Z-MzMN-iq0FsWFnL7Z_34m_FGQs5-XyS9xa4vnE10q_PpCLZlsaD5Ap56oKzJ6Xl1rbAKbZfUcXCL8aj9z9T6ORC5dkyH_AK5XMn0xMxyoNGrnKsdetOd5eLJY2FE-R14UpQzrZ9eb9aPwN1E0fcrziNiPY1rADEE-KOHA8yUkwdnIEcTT_JblC0kRWE7k3XIhzaSIH-3j_X5Gaf4EyLMRzZzDCwvV4Ui1QPgFqjxN6R9u7_uhIVrGv_ja4-jPzZ_eQdCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهگیری یک موشک بالستیک توسط پدافند قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134987" target="_blank">📅 10:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134986">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAMpExEY4Kg7hG3PMwOI1LXOC4aXuo7D3DcpsqhAxkh419O1vDujqUDtt-DShIcM91DPw_w3WJAbMbGCzf9PFJT9nra6g2zACohj93gdlfXsmorTG3u2P9nu-AsSK6sGxI1Y8uukEFwWhZ7UZnriKqB2SNFkkSIY8LGV7_zUfavIVoMY12Qx79oAQVHHgLYglieGrQ4sJu4S4DZ_f8J8ghKewkb6_SmWuiN-y75DjuD48chtrlLmmmS2-JzvkS2LoXHx-qc1uS2VFblsZxgeyatKKxQF61d3HtuKn9g5g1EqxHTrLA68OpmXJWxmPJtCNwimxRgFKcNE_a0BkFnDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش رئیس کمیسیون امنیت ملی مجلس به حملات به جنوب کشور:روزگارتان را سیاه می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134986" target="_blank">📅 10:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134985">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY12AjdKxrqXbpWM-qKC_tJooi0Glepan7Gje6JvDk5bL6PC5SuVxdPo65Oe2Z59Jfxqg0_RO-anq-4UH9aRbLwSVgJq2GWQmmwmzfB6w0J_nOzAfsoiN2BwusVJ3xtXzGJKS8e8NoF34jeRTIcV4dHqH9MNTFGxbLlispZKEKlFPNu3KJen6ni4RtHIEqmMIR1sgcy-1-o-XhGr2znO4CoJnpL9oaMFQx_q1pHdeg_TvREOeUHq_eR0J7yYsvteUEkPY189v-Ch4o6GlprnMsH0P9631c3H0-GRF6RpWHVS6ret55KIOchlaRe1tdnadCM1X2T6B7nrPg78SiBSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134985" target="_blank">📅 10:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134984">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری / برخی منابع عربی: پالایشگاه‌های نفت در بحرین مورد حملۀ پهپادی قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134984" target="_blank">📅 10:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134980">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSiO6Tmwb4BIbmcTdMwsBhNflnK9dZiFSz1_8mOUWy6pvRUFm2fQQlJ-3h3NZnINNTqav5e_TT7WfOCfP5__qzQHax9ntJAhb4OSe8nUb8f52K4il0JqBll182ef7xTzQaZX6sQLPKk5d_Hd69TQKTfn6uy1UhK8GFEB8SMF8UX7Y9GIfFpwdl4TbBgHX1BxtjlTqM8t65lfITyjOa32-c6ts2uPCiCeX0ECXsAgwhUKzDjNnGjX30zfvcZJ-SxTf6DSMK8QXb82Xa1-jdTqnsYBwmVJL8Md6k2xwDgwgG0DU--VvrBDEVKXL63tThFkKj-SIulqgXS2yrOnrozNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a4635a48.mp4?token=oO8-fDu5_d8v-3l53QOeI0ozm4_AGHak-UllQiVNCoN_rxLR0-M0y0dGQKPNoov3qhHD1kFphAK2ZFYOLAzEcbGFVJdrRZY5_TTiAtefxUKEzwVKitLE7MVDmeGIM-uBfpI4Yv3vdXS_Rlmb-N53RpNxqGUQ8uuvsXBQm86ytWaLQYmJGmV509aPulG0kD6faEAEehaemZS8PQ7f_qFOlCcrQffui-gIbhYQdYm1zdKk8LNhwtJtvNDCTIrDTdFS3eHxYLyih1YD7S-XZSNU6-jw6vn_FFlqPijcrZDsA-i0mrSZI_snG2-pTUnLt57ngBDOA_eS49qWocgRj4RzIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a4635a48.mp4?token=oO8-fDu5_d8v-3l53QOeI0ozm4_AGHak-UllQiVNCoN_rxLR0-M0y0dGQKPNoov3qhHD1kFphAK2ZFYOLAzEcbGFVJdrRZY5_TTiAtefxUKEzwVKitLE7MVDmeGIM-uBfpI4Yv3vdXS_Rlmb-N53RpNxqGUQ8uuvsXBQm86ytWaLQYmJGmV509aPulG0kD6faEAEehaemZS8PQ7f_qFOlCcrQffui-gIbhYQdYm1zdKk8LNhwtJtvNDCTIrDTdFS3eHxYLyih1YD7S-XZSNU6-jw6vn_FFlqPijcrZDsA-i0mrSZI_snG2-pTUnLt57ngBDOA_eS49qWocgRj4RzIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام: «تفنگداران دریایی ایالات متحده از واحد یازدهم اعزامی دریایی، در ۱۶ ژوئیه، در خلیج عمان، عملیات بازرسی و تأیید ورود به کشتی M/T Wen Yao را انجام می‌دهند.
🔴
تا به امروز، نیروهای آمریکایی ۳ کشتی تجاری را که سعی در عبور از محاصره داشتند، تغییر مسیر داده‌اند، ۱ کشتی را که رعایت نکرده بود، غیرفعال کرده‌اند و ۱ کشتی را نیز برای اطمینان از رعایت کامل محاصره دریایی مداوم ایالات متحده علیه ایران، سوار کشتی کرده‌اند.
🔴
تنگه هرمز و آب‌های اطراف آن، به جز کشتی‌هایی که سعی در نقض محاصره دیوار فولادی آمریکا دارند، همچنان آزاد و باز هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134980" target="_blank">📅 10:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134979">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کنست رأی به انحلال خود داد؛ اسرائیل به سمت انتخابات زودهنگام می‌رود
🔴
پارلمان اسرائیل با تصویب نهایی طرح انحلال خود، به فعالیت دوره کنونی پایان داد و مسیر برگزاری انتخابات زودهنگام را هموار کرد. انتظار می‌رود زمان انتخابات جدید در روزهای آینده مشخص شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134979" target="_blank">📅 09:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134978">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سنتکام: مسیر سه کشتی تجاری را که قصد حرکت به سوی ایران را داشتند، تغییر دادیم. یکی از کشتی‌ها که از دستورات نیروهای آمریکایی تبعیت نکرد از کار انداخته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134978" target="_blank">📅 09:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134977">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XFD5yRMkvkAUcUaP9irlE8RcN6YwLv7cpfk9fgeyiGry0UiEttwig-OMBdbxiC_8mczLxeLlX8_ghUY1a4oXcU_9zavmRQ5RX6yT8yg7yEA-f1E02PKYJUGoQopywkhzV57UHLBlSUN-hKUiO4BtgFvsxHU-8MXtdFCsNXeclU6UPhT1ZLO-1-F_HjBK1d2_FFufof0DeTdBBFScfV_UaxYEIVS9OvBDlwlY70JXM1pxZk3WB5yVlSxrBt1Q7NzE6_HRmQspjdxPXI23vfW9UaB28zPOh7TA30z2LHeQbpZa9wN9ikR4Q78aB3frLzUePoGI9jT6Z9U3IRUwL9U5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که سه انبار در منطقه نظامی زاید در نزدیک ابوظبی امارات، در نتیجه حملات موشکی-پهپادی سپاه پاسداران در تاریخ 13 جولای (22 تیرماه)، نابود شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134977" target="_blank">📅 09:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134976">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ1KQv98nzB2WwxRwFP67tDiYVmLfqOcJK18XJG1qdEqTw29DIdC86bUBaJYmhC8EHor5_SzPAGplJlRrSO7Q8eluZnRUnf63BJyT36AoPy6-I0htBb3k46dkWtHz-1Xi10AN4EWlY3gd9hW6ZRV1ojiNH4BzOnZgfYAxPrttBNeJXgLbi_ZR434SeJ2JEdzXwPz3dwJtyMcuetfFEOayIFwCBjw3E-pxa2p5rD8qZLFBI2N4QaLe442s2f5ts9hQx4mHtQgau4-1KoEZAtpnFUIBA0szLpoDKmfEboMpXxxejrSvc8xa8J2JJFPkuKlUmS--ffsyeulWwI9Bg3W4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردن اعلام کرد سه موشک ایرانی شلیک‌شده به سوی این کشور را رهگیری و سرنگون کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134976" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134975">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
الجزیره: قیمت نفت با تشدید حملات آمریکا و ایران افزایش یافت
🔴
قیمت معاملات آتی نفت برنت به میزان ۱٫۰۵ دلار یا حدود ۱٫۲۵ درصد افزایش یافت و به ۸۵٫۲۸ دلار در هر بشکه رسید و قیمت معاملات آتی نفت خام وست تگزاس اینترمیدیت (WTI) آمریکا نیز ۱٫۰۳ دلار یا ۱٫۳ درصد افزایش یافت و به ۷۹٫۹۸ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134975" target="_blank">📅 09:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134974">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551b40e9d2.mp4?token=i7aYBHjh6GzmIxfyhfK0Dj9qQ_2mgzQIClW378xvpritgYLLVXwW_XdzRoQAWkbtAfsgYbr24gz103IItw0VJMndzJjb92S2g3XJbn3KLRpMJYbUf-kcANGDgoUHGjgjOUqva6Aw1dN-0hPKifEL5les1uA9FDjU-iOnAbeb_QDVHlX8ePOr2JY5gKdPUv_HhjmwOX8aEcy4bJgPpqlzSRC4XhyIp5nsjNySUjnM4nl13oAjcxSWJSB6ljrUtZnosEkBU-3o-XsbxF7_HGPbXRMX8J_9lECYU0SPY6W7yj636u5_MIbLnRdeG9vBxSHhGsWZSvN-GDBSxm_Ltg9kmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551b40e9d2.mp4?token=i7aYBHjh6GzmIxfyhfK0Dj9qQ_2mgzQIClW378xvpritgYLLVXwW_XdzRoQAWkbtAfsgYbr24gz103IItw0VJMndzJjb92S2g3XJbn3KLRpMJYbUf-kcANGDgoUHGjgjOUqva6Aw1dN-0hPKifEL5les1uA9FDjU-iOnAbeb_QDVHlX8ePOr2JY5gKdPUv_HhjmwOX8aEcy4bJgPpqlzSRC4XhyIp5nsjNySUjnM4nl13oAjcxSWJSB6ljrUtZnosEkBU-3o-XsbxF7_HGPbXRMX8J_9lECYU0SPY6W7yj636u5_MIbLnRdeG9vBxSHhGsWZSvN-GDBSxm_Ltg9kmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات موشکی ایران به پایگاه‌های آمریکایی در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134974" target="_blank">📅 09:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134973">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPsRbdD5toprI5GrBP3uXL7ak4BAJkv3ZhyaGUMMo_Yd7ZXPCatvdC2f6dlrQRpW5tbLvNJHeBDbjPUg77w7WTAsfFPaJkf9GYw5a3NSyAglPMXDcJBBBCWGf513W5PqtisvFb9Y08Xmv1bpPAwuPidzzuOHd2mqBh_ePVoU5-OtHBGQU9X4NQNSVnA3vCiBDembTYQrOBJmfPN33u5_CVpfoqaZ38bIn4fF4PRLN3xmh1W21XIkw99gkVZvafQpUYvEGVHAs0ZBLNIAjNdXnSaJJlaSURa6_E--ogV7XoIMcDQ7J1NOB2od241mA95DMrkh0i1lsbJGYEdZgBbRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134973" target="_blank">📅 09:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134972">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سپاه: رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134972" target="_blank">📅 09:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134971">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام بار دیگر افزایش یافت و قیمت نفت خام برنت به ۸۵ دلار به ازای هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134971" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134970">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پکن: چین و پاکستان خواستار آتش‌بس و از سرگیری مذاکرات بین آمریکا و ایران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134970" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134969">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مقام آمریکایی به وال استریت ژورنال:
حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134969" target="_blank">📅 09:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134968">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=YXmtg1oAVQj4uLJeeoAgP8CJqfdDEJU6q04zUYsHGYQ0DXy9T-FhfC5ZuMWITW1wgZtfFM6UDcF30vmA-ce-JbCuFZpWb3isP_onmtxW1Mv5Qw4mMCZwXWqzvthWqpqTcYI-ClRRBCXS-3HbZ-Hl3Hx-i-vSXWBKgBRrQcbn5wRlRMmVMYdC3xyReTzU-FRYovRj15cjyKLgq3P1jBwbmiFx7wjmh9SNRYPwYTsdDBL6lRlKBkNCpYrRcodLz2AdaisQXF28D7_F3vG1hZySmfJtxTwsp2EwTgWsSD0w_4M2daTqLR4fQxsB-Txgk9T7OHbqLxrxJ2mxnIhcGAU4lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=YXmtg1oAVQj4uLJeeoAgP8CJqfdDEJU6q04zUYsHGYQ0DXy9T-FhfC5ZuMWITW1wgZtfFM6UDcF30vmA-ce-JbCuFZpWb3isP_onmtxW1Mv5Qw4mMCZwXWqzvthWqpqTcYI-ClRRBCXS-3HbZ-Hl3Hx-i-vSXWBKgBRrQcbn5wRlRMmVMYdC3xyReTzU-FRYovRj15cjyKLgq3P1jBwbmiFx7wjmh9SNRYPwYTsdDBL6lRlKBkNCpYrRcodLz2AdaisQXF28D7_F3vG1hZySmfJtxTwsp2EwTgWsSD0w_4M2daTqLR4fQxsB-Txgk9T7OHbqLxrxJ2mxnIhcGAU4lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت پل کهورستان در محور بندرعباس شیراز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/134968" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134967">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSE3YJIv-JRJq7nmv0WaF6R4mSlXUH0wVKaJe-DlCmGCSUpX-u_tPvpKvYa0lgB1tsxy6zXScyjlds4i7J_8zRDxDKvlRQtgbik2M0w6dXZlE7ybeR6aYrxaFrR2g0JIx7QFFfTnBqQbhar6SfR9SCtx8sqC1Z8UBA-WVzLYJ-518tWrcj7XhkUb9Po2H1iRTYP1CwfnB-cdleatyh1s0f_2uEd5xH4IDtuFgcilUa-SCVKteGDJu5bp84EMDMAH7-ONLjZx0Mirfm2ZAkkyEYwqDck5YWfjA3RFo7CzCELdTS1tiG6hWdEPakzYZXFUPE1Yn8_ZaUBWhokssiPcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون دود در
نزدیکی فرودگاه اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134967" target="_blank">📅 09:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134966">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913d736794.mp4?token=AUvDdYaOk1Ca2e9OrosCVVmmcOtQDlHkosleb8brwrmpuSvOoQC1wKSVS9NCu9SljGdtnZmFlI1ppVOH_U43RiW6BuGWqdp7pYDkRaewNR5AJi-h_GDdf4E2c0GJ-z-KmI60vLr4pFQmH9_JxqKa7POQXo1PPnN-2eIYtLjuVqLasAlvomQLoeCQpTprxCfIw1v_xz2BMN_TkQkwOsdtUIMZpehPfBINy696_5v2GUxkU4DGhMASo_1RQTyno8fOVoZQyAE-lrwj2BhT-oWXZtIw9rntRvyJsfLUJTjumZnIix3jV3VL7UdrYQq1XnbOFTphQZG3OxCMMIDLtfJVbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913d736794.mp4?token=AUvDdYaOk1Ca2e9OrosCVVmmcOtQDlHkosleb8brwrmpuSvOoQC1wKSVS9NCu9SljGdtnZmFlI1ppVOH_U43RiW6BuGWqdp7pYDkRaewNR5AJi-h_GDdf4E2c0GJ-z-KmI60vLr4pFQmH9_JxqKa7POQXo1PPnN-2eIYtLjuVqLasAlvomQLoeCQpTprxCfIw1v_xz2BMN_TkQkwOsdtUIMZpehPfBINy696_5v2GUxkU4DGhMASo_1RQTyno8fOVoZQyAE-lrwj2BhT-oWXZtIw9rntRvyJsfLUJTjumZnIix3jV3VL7UdrYQq1XnbOFTphQZG3OxCMMIDLtfJVbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ستون دود برخاسته از مقر گروه‌های تجزیه‌طلب در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134966" target="_blank">📅 09:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134965">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فارس: آمریکا دیشب ۵ پل را هدف قرار داد!
🔴
پلگریوه؛  مسیر بندرعباس، خمیر، لار
🔴
پل بعد از روستای لاتیدان (کلمتلی)؛  مسیر برگشت بندرعباس، خمیر، لار
🔴
دو پل مسیر کهورستان، لار
🔴
پل نیمه‌کاره؛  مرکز بندر خمیر، کشار، بندرعباس
🔴
پل روستای مارو شهرستان خمیر
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134965" target="_blank">📅 09:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134964">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVMpGnvJwxiTbecz2_jEFBsgzR3V6W9Q2q-d8SEwUEb6kCc5C9f44p6e8Iej4aE_VPDwQXSJq8Txq_jYc5IO8aySyvms7wbG3Wt_PqZqyqjYmbvteoFUl0BCC0m77mjbOXIDUVx4Xk4n486syWFI6jUsYckMLryQ6XIo4LkeMLD4XE4X6jR1r1PSTG1hv3FxvMFv9uHjQMBjJ2s0H0p69VIgaNM5_Ji2A1dRkAb5kvpakckZwwnUXAgbCyDl453-uDNPEe0ALfmP3o_UvWPwKPTvjcQCuGFdcrLrKlpAnrqpwJ2cRp0H2Bdyiww65clCQ09Iek35-1RSKZ5qh-XgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهباد آمریکایی روی آسمان چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/134964" target="_blank">📅 05:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134963">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ در پایان سخنرانیش: ما قویترین ارتش جهان رو داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/134963" target="_blank">📅 04:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134962">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/alonews/134962" target="_blank">📅 04:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134961">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c26581b61.mp4?token=FFuOKrhPhRvuBOHRurjPegCoeNAdo1TOISyiD5nbu_TTdcu9LFnbow91HU_H-3_JYC6aN8tDZMgohXKvnF7o2eT-Fw2LP8EASPWpHyZGr3jUUoTEoy3fBb7_JaX3p8NPuoR-pLTFaNDRmse7R_n0RL0XvF_joG-pZwf1zTelTzUYKgW7M-6Mda7k2NftECRlNkp9MhnsL6ihcBb3Nlogi8bqXIMBQLczjogGSZjtbsxA2do0bX9Nd6_y_444ibD13vnTnSbHatedmhx3X4qniDYLO1RdXHA3w4lgFh7NGUDoPUpdOzAnhLBaWAzSOzT37igMpVbT3fX-3TQ1mx4OeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c26581b61.mp4?token=FFuOKrhPhRvuBOHRurjPegCoeNAdo1TOISyiD5nbu_TTdcu9LFnbow91HU_H-3_JYC6aN8tDZMgohXKvnF7o2eT-Fw2LP8EASPWpHyZGr3jUUoTEoy3fBb7_JaX3p8NPuoR-pLTFaNDRmse7R_n0RL0XvF_joG-pZwf1zTelTzUYKgW7M-6Mda7k2NftECRlNkp9MhnsL6ihcBb3Nlogi8bqXIMBQLczjogGSZjtbsxA2do0bX9Nd6_y_444ibD13vnTnSbHatedmhx3X4qniDYLO1RdXHA3w4lgFh7NGUDoPUpdOzAnhLBaWAzSOzT37igMpVbT3fX-3TQ1mx4OeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور آمریکا، دونالد ترامپ
: ما در ونزوئلا پیروز شدیم، کشوری که اکنون با ما همکاری می‌کند تا میلیون‌ها بشکه نفت تولید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/134961" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134960">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4ce05c84.mp4?token=lyc9L5YSwIrVdHyCvE-b5Win-xjdZEMgSwHGrlI4fQzOz8Sb_wGTYImDHkD31SsfB9LNmE3x8dwCUHHTWobtKTQ0-INM6BlTQsmWWIQ2XH_TG9CzXL4igSNIqV35CLISYBGa_J38H-q4bSrx7twWtOq3W6NNFy1pKVYwqHypCG5okWmOzz2w9teQ_tyjW7guYCSos6yzaEbspXloF36v0nkaGbOpMa4hEJmfcy3ho7JTp_uz9N6wIzv4MzE9lmnXdWJx8lPE2NIaU9TJaL8jCw9jbhsFUQvTbZsMsEqXzQhiw2y6RER6VWvrt-3hUNWXz2xus0eR5gKQIOpl4dZeIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4ce05c84.mp4?token=lyc9L5YSwIrVdHyCvE-b5Win-xjdZEMgSwHGrlI4fQzOz8Sb_wGTYImDHkD31SsfB9LNmE3x8dwCUHHTWobtKTQ0-INM6BlTQsmWWIQ2XH_TG9CzXL4igSNIqV35CLISYBGa_J38H-q4bSrx7twWtOq3W6NNFy1pKVYwqHypCG5okWmOzz2w9teQ_tyjW7guYCSos6yzaEbspXloF36v0nkaGbOpMa4hEJmfcy3ho7JTp_uz9N6wIzv4MzE9lmnXdWJx8lPE2NIaU9TJaL8jCw9jbhsFUQvTbZsMsEqXzQhiw2y6RER6VWvrt-3hUNWXz2xus0eR5gKQIOpl4dZeIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: چین به اطلاعات ۲۲۰ میلیون پرونده رأی‌دهندگان آمریکایی دست پیدا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/134960" target="_blank">📅 04:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ:
اگه من تو انتخابات رای نیارم یعنی تقلبی در سیستم شکل گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/134959" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134958">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37596bf02.mp4?token=NX1H1lP3phMxIbJP6TolqILOSiTLqZBUEEtzna9v7RX3Hjf9EkuU9ksr6zpY9P9D4tAAzKklZ-JbOTd20n0vjrp8nbEl6kUSqUO2sp6T11fia7IjoePwJY_aQJEtPyE03euDcovqut7SyILcAv5lB5Xa3kj78N9EYSfmyTYKoe1589brqk9K79ELHVBIl4rVkh7mzbrvocH3YB-GjYzZd3gveNGyxwFNDJEFxgWxn5LGDCd1lzlvM0zqo81DCXIaCWJKeX0c1Hmlb4T2La4zliHGdK20x0XXy4WPs9zzbVgWK4CFc7JLh7aJ139ZBYVk-hAjA5po1C29iLJA_9XOxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37596bf02.mp4?token=NX1H1lP3phMxIbJP6TolqILOSiTLqZBUEEtzna9v7RX3Hjf9EkuU9ksr6zpY9P9D4tAAzKklZ-JbOTd20n0vjrp8nbEl6kUSqUO2sp6T11fia7IjoePwJY_aQJEtPyE03euDcovqut7SyILcAv5lB5Xa3kj78N9EYSfmyTYKoe1589brqk9K79ELHVBIl4rVkh7mzbrvocH3YB-GjYzZd3gveNGyxwFNDJEFxgWxn5LGDCd1lzlvM0zqo81DCXIaCWJKeX0c1Hmlb4T2La4zliHGdK20x0XXy4WPs9zzbVgWK4CFc7JLh7aJ139ZBYVk-hAjA5po1C29iLJA_9XOxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ
: اعلام می‌کنم که از همین لحظه، اسناد اطلاعاتی مهمی که آسیب‌پذیری‌های تکان‌دهنده‌ای در زیرساخت‌های انتخاباتی آمریکا را نشان می‌دهند، از حالت محرمانه خارج شده و منتشر خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/134958" target="_blank">📅 04:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134957">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38775e5358.mp4?token=X0cdoucBzsYLKSrlKRrXjvfb9Kbvb7ue_etI1GioTTQLLAUvbgmL7wV5La7LK59CGTsLPnqYrY3IiRlsBi85-1xIykOwedXM64TRlUN-zbhetLTGvjHau9O9QpNt-W_73qq64Md6ilZu_Nw-j73zrMmeZtxmpLiNf5XWzYHbo3HZhUr6Lzt7kr4SiLMO_KVOIuk60T8Ztz5HVLGfmF0GtlXTubIAjzL8Mv_ZlmHmXwaNNZGqEi_8uPv5XAUrBpTVCKLgCN732PJwgNkIZp2ECu-UiqfxNEfJ8FAmSyNZS8-wmPKC07Ldn3bGuGMFvsQmcf9qwHN-6TDHIJdNuHZgAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38775e5358.mp4?token=X0cdoucBzsYLKSrlKRrXjvfb9Kbvb7ue_etI1GioTTQLLAUvbgmL7wV5La7LK59CGTsLPnqYrY3IiRlsBi85-1xIykOwedXM64TRlUN-zbhetLTGvjHau9O9QpNt-W_73qq64Md6ilZu_Nw-j73zrMmeZtxmpLiNf5XWzYHbo3HZhUr6Lzt7kr4SiLMO_KVOIuk60T8Ztz5HVLGfmF0GtlXTubIAjzL8Mv_ZlmHmXwaNNZGqEi_8uPv5XAUrBpTVCKLgCN732PJwgNkIZp2ECu-UiqfxNEfJ8FAmSyNZS8-wmPKC07Ldn3bGuGMFvsQmcf9qwHN-6TDHIJdNuHZgAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/134957" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134956">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857d55ae03.mp4?token=SEo3o0gyZxVTd9OFB3FBMIa4aUpUKc9g8dcUqWNPMJzbdb5oo4UGPsLParjG2hBwIwcKvS16dGy3_AbqzzUjN9KzRa2SYjVuwaiYMKkyJewiwdsuk9lgMzHkvx62cLZjZnsxygd456A1OF0sL0-OLTSCLfc8cImAp5OiFzXpdaok1HdIV8LV37pcYY8jTNcV8QjlpUW8ArslKwsKu1v2abkcujy6CHohVmTe7mDC52w-E2iAR7wfUPRdX_CZuwh7F8Q1o282tqzpXVPgSqitqTNHCsLpjKeu_nf1xHyRWwzMNWxhcVlBrTcuEv7f5FRbkDijQJJ-rPd8eipS51CU3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857d55ae03.mp4?token=SEo3o0gyZxVTd9OFB3FBMIa4aUpUKc9g8dcUqWNPMJzbdb5oo4UGPsLParjG2hBwIwcKvS16dGy3_AbqzzUjN9KzRa2SYjVuwaiYMKkyJewiwdsuk9lgMzHkvx62cLZjZnsxygd456A1OF0sL0-OLTSCLfc8cImAp5OiFzXpdaok1HdIV8LV37pcYY8jTNcV8QjlpUW8ArslKwsKu1v2abkcujy6CHohVmTe7mDC52w-E2iAR7wfUPRdX_CZuwh7F8Q1o282tqzpXVPgSqitqTNHCsLpjKeu_nf1xHyRWwzMNWxhcVlBrTcuEv7f5FRbkDijQJJ-rPd8eipS51CU3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: قیمت داروها بین 70 تا 80 تا 90 درصد کاهش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/134956" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134955">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ :قبلاً همه دنیا به آمریکا می‌خندیدن، اما دیگه اون دوران تموم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/134955" target="_blank">📅 04:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134954">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
گویا دالامان که نزدیک آنتالیا هست پرواز معراج داره، این پرواز رو یه آژانس هواپیمایی ایرانی چارتر می کنه هر هفته که مسافرش رو از آنتالیا برگردونه ربطی به مذاکره و ... نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134954" target="_blank">📅 04:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134953">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
برگردید عراقچی نیست توش</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134953" target="_blank">📅 04:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134952">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
هواپیمای عراقچی رو آسمون ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/134952" target="_blank">📅 04:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134951">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
انفجار ها در پایگاه آمریکایی العدیده قطر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134951" target="_blank">📅 04:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134950">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCaxd8_6wPqDzPLg2QSU2kaSnpoUMsEV61FEQIBvLhrY1HkX03wwJYwzRiCXR4JhVSdzNCiOTBfmk7Z991dzemi6ulnUdIVYWcIcQOei5uIRH9q25a-ZM4lss7ObXFOMAHhSfA_SbGDfuPOBq9BK8rSookRFHmVamb6_26DCutS30mo8WBzvdAlAS7bHgQj1eVq8S2yM7D1_auWzo4phitseSMF0DmOfwsCzsBMD_z4bfAiCio4Sv6JOQFdGQeRzzOo6TEf0ftXWsH4UTSZ8nAl0duB5TsGbX7oTErZlKCKujQIeRrJKfZe3YMF0Mqb2I_UHkHYO7EaH0zGiN21rZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت شدید پدافند در بحرین هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134950" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134949">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9NM8hd9cbL-dFjZNO3p2Kpg5TB9Bx9OdvMwUyikaStTlpfG4Wr9I--mwsvx_lb94vmNUUNM8-h-e7XZFpQTW4ZRqKHv-8RDedrGD--Edryk-p4fSFWUnCai0pjmhmOcmmrt1QeL-T4wug74lOvJXjU4t5xdSQcIvMz4oDxsNRG0ec0TQmHzS0liHpHdhlD4qtQTRh1pgl2fT8zV6MdQiDsSZwx02l6eyiPaOd-xkuB4fWhPqhke2frBPbFgUVdCW8WVof2TlnpZgsOTUmfmy6lZpaQZm5Ru4wu8ihUZ2SWnYitKRmXYNW4kppjbNODr_2mZqmnmLZT-xBZC4qVwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان قطر بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/134949" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134948">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
حمله موشکی به العدید قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/134948" target="_blank">📅 04:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134947">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ویدیو تخریب پل ملک فهد که درحال پخشه متعلق به یک پل در روسیه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/134947" target="_blank">📅 04:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134945">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99c3c0b64.mp4?token=cuqzTYMdRb8cZ8YFM9Cfn_xS3xyNENRJrhTvEzrlm3UHdog3XuH9voWE2EoEPmYHuUMPGaMf97Exg--NzyEi_9jIA-9nxYdH5f2TJjEzQaj-qYK4DmfJJ1iZFfhNYO1S_0HnM7c9neiUi5RYygFIn850cgBX4DnAp0YPLwc1iQ2WvQU3L004JCtL6q2f6zLtlRc3mtROPNLzfJ-apea407HVm4PUa_Z-5FP-quF4ExVo3FQXpyZQW41g6ngGb2CrWiJEY6AGddRU_gH9Wp6ynobWvXcfL0EjUQVZZ__hzkGTdXE5dysdHgEiXiCQIcAt1QikvKPoZ52JgDVsEy6Y9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99c3c0b64.mp4?token=cuqzTYMdRb8cZ8YFM9Cfn_xS3xyNENRJrhTvEzrlm3UHdog3XuH9voWE2EoEPmYHuUMPGaMf97Exg--NzyEi_9jIA-9nxYdH5f2TJjEzQaj-qYK4DmfJJ1iZFfhNYO1S_0HnM7c9neiUi5RYygFIn850cgBX4DnAp0YPLwc1iQ2WvQU3L004JCtL6q2f6zLtlRc3mtROPNLzfJ-apea407HVm4PUa_Z-5FP-quF4ExVo3FQXpyZQW41g6ngGb2CrWiJEY6AGddRU_gH9Wp6ynobWvXcfL0EjUQVZZ__hzkGTdXE5dysdHgEiXiCQIcAt1QikvKPoZ52JgDVsEy6Y9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک های ایرانی در آسمان قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134945" target="_blank">📅 04:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134944">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت کشور قطر:
سطح تهدیدات امنیتی بالاست و از همه شهروندان تقاضا می‌شود که در خانه‌ها و مکان‌های امن بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/134944" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134943">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
انفجار در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/134943" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134942">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
برخی منابع: اعزام گسترده نیروهای امنیتی عربستان به مسیر پل ارتباطی عربستان و بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/134942" target="_blank">📅 03:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134940">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
چندین انفجار جدید در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/134940" target="_blank">📅 03:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134939">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18319f2842.mp4?token=bzG-uffCLl-KeCLy1MkFdQIDuhS4b_ss3boHesPNS7D68PcACjpfQu0VABuvGg7LrcxAjo9qMzRBmfL9P2BZ2O5_tPzb9n0LKOAd7d_RE4EuYx7KBrT92ClhoGF6kQ2-eSBb1rWksF-1X54LlsKBvo4W8UYDqxI2kr3sentbKDuoxbr8f0udqVZ9ZzeOQG39xaKw8nnX-JBnjRaNrdSCYWex1IxAhz6IxFFTE8ppApYuJDxNS1mYge10tjO4vcvVi22FUVC8H60ZZgckwTUc6-XtC-0W9vqz6DXZxdCxUqzREgOe-QwBO0GhfTZWSzKGE2yyx-WRu1hkQByQysRv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18319f2842.mp4?token=bzG-uffCLl-KeCLy1MkFdQIDuhS4b_ss3boHesPNS7D68PcACjpfQu0VABuvGg7LrcxAjo9qMzRBmfL9P2BZ2O5_tPzb9n0LKOAd7d_RE4EuYx7KBrT92ClhoGF6kQ2-eSBb1rWksF-1X54LlsKBvo4W8UYDqxI2kr3sentbKDuoxbr8f0udqVZ9ZzeOQG39xaKw8nnX-JBnjRaNrdSCYWex1IxAhz6IxFFTE8ppApYuJDxNS1mYge10tjO4vcvVi22FUVC8H60ZZgckwTUc6-XtC-0W9vqz6DXZxdCxUqzREgOe-QwBO0GhfTZWSzKGE2yyx-WRu1hkQByQysRv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش خبرنگار تسنیم از پل بندرعباس به لار
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/134939" target="_blank">📅 03:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134938">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbAdJ8tKVmNkWJ5u292coNcu_4hdAonCvvp7dgo53BU_WrgKFPCPS6BaC9mvKRyFccfqBMqQnRdLhK0EkJl6TZ9YCrYhj3hG1vS0q1pnrZK8Jw0ZopA_krlNShDS4qz5b0CsRRxhA_QVRIsZp7Cm47NN287gdw483BxWJhecaawlzNOlDi8ijgtaLxb1dSFL1gDrF3CRW_gVdHqaHpG0gcS3Ea5JrGRdc3L2EhmaqTXlbiqoV6cHSbDc9tsKi3k77Q4gjQWmmOwCsdFHHneb73sCDVeuTgGQxLBg6kzrvdL87MU8-As3UGBeIdr0H-HxBSts3aYFT0EvsT-3jx1TEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
شاید به تهران حمله اتمی بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/134938" target="_blank">📅 03:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134937">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
مقام آمریکایی به وال استریت ژورنال:
حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/134937" target="_blank">📅 03:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134936">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwXQ0rDyiCL4eJj4RkKWr2vaUTIa38AIAoyBalQhxI7091PKVzLmU2YnYIpGrNLtj5x0f7YKcCqgk3WQW9FTXoA5mvq8DoPql-lmr-uKZnEPT8_Ef4zc6LbGDSKZj5CBq_nda8wpsXgLI-paysjbkFl0i-n4PY7Oj63JQ4keK4gVxhk5M7d_0KFGIhVcea8SRwfEPqtkp_SFQejzJ5GD5Jper8F0Ebjg0S2-uUkPAuta58PILaTdb30DugHONMjdfCvwZ-7LmKzuIdGIvqU9idBYyONfiYSd842A9Z1nV_YbS2N6K6mfGtjA14mVrKcrjJzKVoprfQ1MXasnn0LSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: فیفا اعلام کرد که سلاوکو وینچیچ داورِ اسلوونیایی، برای داوری فینال جام جهانی 2026 بین آرژانتین و اسپانیا انتخاب شده، داورِ بازی انگلیس و فرانسه هم یه مشت ونزوئلایی انتخاب شدن و خبری از علیرضا فغانی نبود
@AloSport</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/134936" target="_blank">📅 03:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134935">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
دقایقی پیش اسامی داوران فینال و رده بندی از سوی فیفا اعلام شد
🔴
علیرضا فغانی داور هیچکدوم از بازی ها نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/134935" target="_blank">📅 03:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134934">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی:
در صورت تداوم اختلال در عبور نفت و گاز از تنگه هرمز طی هفته‌های آینده، نگرانی‌ها درباره امنیت عرضه جهانی انرژی به‌طور جدی افزایش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/134934" target="_blank">📅 03:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134933">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
برخی منابع از وقوع انفجار در پایگاه‌های آمریکایی اردن خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/134933" target="_blank">📅 03:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134932">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزارت دفاع کویت اعلام کرد تمامی حملات ایرانو رهگیری کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/134932" target="_blank">📅 03:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134931">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7QowPgQ_JcazxH9-aWY_CzP53KGQtaR3QYbf529Sds4j0_h7eSufznrmmPamdTe3KZ7mo-AKkAIS1sbIoLHP0alCX_Bz8hyKPAeRsB8azUXXqxJ46p90ZLNdOA1_tqhRYW4Wz9JjKhMIoZmGM8yYp2MyybP5WJb2Tl8QVS5AOTCmHT0cqusYYO-s0QKeZUNOlqa7OFuBesEW4WsBGADJHmK2n4bOo9AoogeMwuBaRgMvL4mR1cYdlGdFHA7H_oWrCzEfPVgwgYxZ0L3GVwysnLM58mMHITE9UsqoGLBruWwaHkQnDzbgKPq9c3V668-CgbP4nqs1vswr4s5uMGOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای عراقچی رو آسمون ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134931" target="_blank">📅 03:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134930">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
به ما میگین وطن فروش جنگ طلب چون نهایتا ۶ ماهه داریم میگیم ترامپ بزنشون!
🔴
شما که ۴۷ ساله هر جمعه دارین شعار مرگ میدین بهشون میشین وطن پرست جنگ نَطلب؟
🤔
این است شعور و منطق عرزشی‌ها!</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134930" target="_blank">📅 03:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134929">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز:
اگر جمهوری اسلامی نتونه پاسخ قاطع به پل‌های تخریب شده بده٫ حملات بعدی امریکا به زیرساخت حیاتی‌تر ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134929" target="_blank">📅 03:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134928">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHc2koCzt86m38HGcaz-xfxtTHahj5aFr4OcM1am66mmUhRa3yZpc3AIo1Vfp4o_rUKsJwcnpc6sF_G8cgjUUwz7nnFVUEWkGA1XUssD-xY3CnwtjeEo0xi7INvEiy0JNZUbAIoZ32j9F4-e0WH4fagoxufrVvlv4y82CgzjQ-WH832Ylwfc482MYOFmtlyzyGaPl3DLUXJjMsytjTjqs4niI0fo3cznlcRXyAkUFLiH-KJIBA-3_c440C2ufhO7G-btrrXVYAhfPhWtRjyg8nZb5ybjbTgZe9olSBIUGlKp5QCOXJsW12_Iqo7aDxnjLC5kLdTFCa8afszGkjmy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آسمان بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134928" target="_blank">📅 03:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134927">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiZrt_HxxhmaQPzBCBEQ8mjxhxnV_5ZDB7IClypvg4ruzNQa2HnhQfCq4QLChpgxKXDYHM8-9KgQWz9K7pEKMdZizHfsIclhAj6ftrsBPDQ8Tt_STxyOne3bQllRmmQZErYbQ0SxTrVe2sg-5Ti63PszDPQCD4yJJRIYOW7KlITlWFYFsPAapuxUaigTVEP8YyS6LqBwEEj3ksymw10Lex6E5wzIrm_vyA0RzezXkM1LBEew5pnJ7kwKFPGYMeUSiB0kbBfv0KkAHwNJrbE2Q7hcihsS9826ywyzkV4hjVbMV-fTWhJqVK_0Uriym4VIup0k8Tl_tbCeXP9KYf9hZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق آمار گوگل  تو همین چند ساعت، سرچ کردن جمله[لغو عضویت  جانفدا‌] افزایش چشمگیری یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/134927" target="_blank">📅 03:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134926">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
انفجارهای مهیب در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134926" target="_blank">📅 03:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134925">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c312ce96.mp4?token=FX1kvZn1aDk_I1d-nXshsbPg_eceNG2bLClDbxGNJ747UjDDA2p8TEAg4e4QwjRKJuop25liGNv85SikrdbYY_KevdhHo12W5Eu0t4v9ajOi0YXJFYi6sK-UmT_gJ9Fi9KdLYew1kG8BISGrLp-WZqyrJ70rWqBX1z0GDDTCoXamdPwkd8kCuoxQlY57BzhmwWyXjSk4Ajcp121xB38tGqOUgm6LAKX1e7HDP2M8ZOrXDOYqqjlIdtTqnFojMHsVYGUq9GeS7ovDiQWx4_XC3rd2V2qhaTFs1Vg8nwqaeWj89SOC9B_nVDd_n49BGeDhXLq7UTzoICmX1mJoBazziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c312ce96.mp4?token=FX1kvZn1aDk_I1d-nXshsbPg_eceNG2bLClDbxGNJ747UjDDA2p8TEAg4e4QwjRKJuop25liGNv85SikrdbYY_KevdhHo12W5Eu0t4v9ajOi0YXJFYi6sK-UmT_gJ9Fi9KdLYew1kG8BISGrLp-WZqyrJ70rWqBX1z0GDDTCoXamdPwkd8kCuoxQlY57BzhmwWyXjSk4Ajcp121xB38tGqOUgm6LAKX1e7HDP2M8ZOrXDOYqqjlIdtTqnFojMHsVYGUq9GeS7ovDiQWx4_XC3rd2V2qhaTFs1Vg8nwqaeWj89SOC9B_nVDd_n49BGeDhXLq7UTzoICmX1mJoBazziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی میبینم اونی که به ترامپ میگفت عمو الان داره واسه جنوب استوری میزاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/134925" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134924">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08de537c4.mp4?token=S4cvFXngE9jKmMky6TIjNDKhBWMsMVQVLqlCkPxCkDEPzq71u0xUBON_pGS3sxcyUlgXZNfDLP9NhSPAjkc7QNAq9KNL6nbFYareEbFoFVMgL-Gy6qNhUTdraZIU7ndqnJWeNgp1VLZRoj8i5_BDR27SXNU009TtH5xfaUQAM9MnBq0JcAOKSzV5s9UYH9Fx-N9Cms2fsDuh8642y8zOhY4952RhsS465GVnQs8v695jGeTBKn2PMRb0t9rMQb2JjX6fHytt07CSGUR7tSCBiXbgOhot4m0n2k5wJT-rueQWbk-tFToogv--BTqAkoNdH3rgKYXsO01i2aR_ehOq5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08de537c4.mp4?token=S4cvFXngE9jKmMky6TIjNDKhBWMsMVQVLqlCkPxCkDEPzq71u0xUBON_pGS3sxcyUlgXZNfDLP9NhSPAjkc7QNAq9KNL6nbFYareEbFoFVMgL-Gy6qNhUTdraZIU7ndqnJWeNgp1VLZRoj8i5_BDR27SXNU009TtH5xfaUQAM9MnBq0JcAOKSzV5s9UYH9Fx-N9Cms2fsDuh8642y8zOhY4952RhsS465GVnQs8v695jGeTBKn2PMRb0t9rMQb2JjX6fHytt07CSGUR7tSCBiXbgOhot4m0n2k5wJT-rueQWbk-tFToogv--BTqAkoNdH3rgKYXsO01i2aR_ehOq5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله به توپ ضد هوایی سپاه در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134924" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134923">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRCpyG-rqa3bwaUJyTKv96xy-02AcAOYUf7bsg4HvI_jMqPt_uRKun3uAOA4hsO6rkx_MGgHI0epz9lAlRCg2z6JlZFF4LGrFY49HC8f0Kg1zSsQZvGp60DwImWpOToswN_WMfmNrkNmc6B05942N-u61hSvqCh2L3bMKEHzeBdTFAhxD2LK8adoBNtC9OEeUegcGX7Xhk5qbsMwX4LHOj_ozFwq2JfqsVaelQxTD7ewsigtkdsSdCvbzgoL960LM1zinftQGu312icWTHXFD6eWvBtOaTDs-SZ2exEYmGMml1qmZzo_yIp0RF-FBlMk4RCzeJOYAIWO8HnYLt0Vbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش
کویت :
در حال رهگیری حملات موشکی و پهپادی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134923" target="_blank">📅 03:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134922">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
آژیر حمله موشکی در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134922" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134921">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-2jPQegujpSZYTkOqucBJhOGPWqa5hvFg-iDARr9qZq8j09aGUFbWIHreH7Th8nZzNMC6tjn_QoDcBZ47PQ1IWX2g_91LEZNQyF9pFvaaheSp7k4I6v1DyR-Dw2SdBcVWVvXsRCQUeAgdZryXpJ64LBpKhk36ugWzDODyt2Afi_d-8vKE9QmOd8QGS2x2UI5LNe79ywm581UHqbLMS1A7le6ybwo9Ul_zwh7uKqlHtolgiBEEFxohLkWfy2Qj-vjEsDaHghOksdLWoGYmBOZM14Fo8-YTBnN_HeiopDt44uz076W4Q6su183_TYtLdyI-7mr4o3C3sqEGvegkMHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه خبر نام دور جدید درگیری ها و جنگ رو "نبرد هرمز" اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134921" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134920">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBep2Jy62aEFD2mxVQYALDmfQ3KR_0U_p1mtm95_3F1-bJ-9CxbTSkEGup2CNYXvrEZCFFcj93RMVvthqW11GGUGGXbjqUN5pwZY_xF4aYksk67WvmeGxfG-qsdx1CkbuPJUjW7bLKHIYUbXqUB5OLCqMwk_MxJbU_VVdp25V06VrhF_q-v2XhC94QcAf3ZzEHtqIrnuPUdyX26qJTbc94tdBicstS-mtAONbV_mGYxmmngwKugiwzVfs3U8tT70AiJwIjkkS-_TZEjH2E6-Kv_nxVSgs0uL8Hwy5yAa7K5SEKqNqzE6lK9FxjkVxx1ZBqei5pfhdpB5tYrfv_dPXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حمله موشکی سپاه به بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/134920" target="_blank">📅 02:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134919">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONuD3WSz8L5eSUCWmZEZ3X-0A--ffYdTtkpOL-gF1xz1wYr2aBlvV-VkDjX6RqfuuwJxwohcedoYwF4zfh3x09zTQ453kzCIDJlwe2kSiGzIBzkibgSybB3RvRPF5L2Ese5OkuoUzyj5FHLtaenD2tQRTWBSl4nY6eU1HsClkZiteRHocvGJh__irFJnkmW-bl4uwik-dS1xWKk4vEz9T37ET7PSNEXUM_Hyb4LP1ijF0kLXXGdT4uHe2mZ0nShEbCzv2fnHZdCwVMgFIMeeNhW1ZLl5oH3tkKUnZ2Y3YcVd0mpy86-7pb4Jmmkh64f2TSDKEwhjJLIjZvmVBmfy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای عراقچی در حال خروج از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134919" target="_blank">📅 02:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134918">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVAPTPyA--12njCmaunJJmRSAhLD2_of5TJebAXyF9bDFb6nn7KXOS0slVpbLJEe_Zq-IaIR6dCotCMevD6MEuciIeyUNZK3-V31onFPda2CcNqquheEdBF-vOFrk5vhO9LlGKlAV0hgG9-sNPxjBZpAwkxiSQqqgTNzowz79iwaH0RtAKDUU9ywVvERf9imz_emz-GUoazmJ27gyK7l5FEBs7MNIhr56whOnBnMTXrY3dkCpApmpK-SBdWVqlBhoZXc85LndLIgEqZCSEqm8-r43nqZt57tYEbh0q3tUbJr9T5bxRrE-MTM8CaCpF3FKAgyJp9WS8bcof3ecC0Q3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون دود در پایگاه دریایی بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134918" target="_blank">📅 02:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134917">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=ZrFvAZ1m4lcVVbcnKRuwxcY_-b0I3LA9yOsv-VH5QeLxlKeFd2n3tyqSmi6dFkghBQnLyHy1i_2HSaB0XTjzbGd1Or9eflPSGHycaAjXsxOjWq2-GeiWRllJC5DG8iXzNn593Dfe1ftF1mxL0QTL4C_fsYI1-qodmrYmYqu76MVZduXQAxDS8TXLzvO888VE11sxTRvUqp7nJnHwlq8Ly8OXjREsa7AU22-3o1zk4AQFA1maFglTYE8KQhg8Yw7aGFNkJ_Pnsbhx3QFBLGPZET8rXIU4fR5W9MmrhQ0oWcttjS47hQAY6KRsYWL2JGDauNGtC9Z3yRp02uc6A7CxUKXTd00B7voVs7LejNdbBT27Fo-sc98eeO2AXiifPuihbWL65nDhOeSWVFLrtIqwRw6y0nh3Tg_4MM9CiaIklUn_-1HGRud26LoeEdfkYdF7BUQ-QpnmfzeB1A7lPMr4aOx4IPF-CNN4J5-K71W5i22ppu7A35C76neooukqWWeyXMgNGBdroOd0miOAwXDBOU6Da6PQNXGPZl96becAmRrWdIIFcJJ0JQtw3Fs-QJYXeO_XfRv7olaBuaFzQzbfOo_ibuq6msccqs1PqRZW-Yc98hkvtPxSsCN5WTKwZ4aIHKWU1QGxSeQJTt76JQgckn9oLFVM3lg6BWjhuEhuT9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=ZrFvAZ1m4lcVVbcnKRuwxcY_-b0I3LA9yOsv-VH5QeLxlKeFd2n3tyqSmi6dFkghBQnLyHy1i_2HSaB0XTjzbGd1Or9eflPSGHycaAjXsxOjWq2-GeiWRllJC5DG8iXzNn593Dfe1ftF1mxL0QTL4C_fsYI1-qodmrYmYqu76MVZduXQAxDS8TXLzvO888VE11sxTRvUqp7nJnHwlq8Ly8OXjREsa7AU22-3o1zk4AQFA1maFglTYE8KQhg8Yw7aGFNkJ_Pnsbhx3QFBLGPZET8rXIU4fR5W9MmrhQ0oWcttjS47hQAY6KRsYWL2JGDauNGtC9Z3yRp02uc6A7CxUKXTd00B7voVs7LejNdbBT27Fo-sc98eeO2AXiifPuihbWL65nDhOeSWVFLrtIqwRw6y0nh3Tg_4MM9CiaIklUn_-1HGRud26LoeEdfkYdF7BUQ-QpnmfzeB1A7lPMr4aOx4IPF-CNN4J5-K71W5i22ppu7A35C76neooukqWWeyXMgNGBdroOd0miOAwXDBOU6Da6PQNXGPZl96becAmRrWdIIFcJJ0JQtw3Fs-QJYXeO_XfRv7olaBuaFzQzbfOo_ibuq6msccqs1PqRZW-Yc98hkvtPxSsCN5WTKwZ4aIHKWU1QGxSeQJTt76JQgckn9oLFVM3lg6BWjhuEhuT9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین وضعیت شبکۀ برق شهرهای مورد حمله، از زبان روابط‌عمومی وزارت نیرو
🔴
مردم با مدیریت مصرف برق، به برق‌رسانی پایدار به جنوب کشور کمک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134917" target="_blank">📅 02:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134916">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82adfa6fe.mp4?token=Ft39T36H4yqH4gmWVyDe4vi2jwV2sD8Bs-og9_WIZNjyVCKKJGQ61UtOxqJPZPnEt9y5YMPgD6Fd8fTjU2rdCzHmdeMpVGGXfyeuMF6FowQpH3guwoM9fg8ULKTcfLtLBErnv0lQ806liT3GPH-_StPxsp1TRjfiFxxnKkEA2EZxW52h8DwUOR6pFCJQnhg-fI6D1VJ6OND7OgMhZGhVh9yYlR38we3vhUhJpe2xG6TloDO11jNq8UjPbFdNjy-A9PI_PT7wfOnDFp_6SZrnBaemE8zr5X1hh0ktZlClDtnOatMpWxX0zBg2lEZL6GXb2PWBGHvyHocC2rSOj7PBjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82adfa6fe.mp4?token=Ft39T36H4yqH4gmWVyDe4vi2jwV2sD8Bs-og9_WIZNjyVCKKJGQ61UtOxqJPZPnEt9y5YMPgD6Fd8fTjU2rdCzHmdeMpVGGXfyeuMF6FowQpH3guwoM9fg8ULKTcfLtLBErnv0lQ806liT3GPH-_StPxsp1TRjfiFxxnKkEA2EZxW52h8DwUOR6pFCJQnhg-fI6D1VJ6OND7OgMhZGhVh9yYlR38we3vhUhJpe2xG6TloDO11jNq8UjPbFdNjy-A9PI_PT7wfOnDFp_6SZrnBaemE8zr5X1hh0ktZlClDtnOatMpWxX0zBg2lEZL6GXb2PWBGHvyHocC2rSOj7PBjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی وحشتناک از حمله به اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/134916" target="_blank">📅 02:28 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

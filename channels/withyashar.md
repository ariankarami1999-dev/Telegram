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
<img src="https://cdn4.telesco.pe/file/FM_GxKHcHxLBB4pUvkoAXVrNvCSCgPp6UJToGDEojdtO2rEtF56h3oUS4y87XfF4-is8SlW3FpVYxawf_2gzMDTACNx-i5C_4N52KjGm8Y_y7xzHQ2tIa_8oT3fLiPT_M0Z-q9xSfNGLOdzHRbtKi2V-UKp3rZu-i1YNUOvHlq6yNkDxf7eU8WWFI1I2GjQAtTMBW1JSFGABKNLLhDo14gwQ1CtKyygdDkZuU7-Y-6mvjnf0dexWOSVy_5Q7EdvF-il26wGjsssgNd_-sbTymq1itAQUDLC3-2ajNedO9OscZ8Z9ZYCEVG1bJKKecVqyGRLjByayOyyAl1i1MKVezQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 272K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 13:46:11</div>
<hr>

<div class="tg-post" id="msg-12314">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Pishro (instagram.com/yashar) – Sonnat Shekan (t.me/withyashar)</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/withyashar/12314" target="_blank">📅 13:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12313">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نتانیاهو:
خوشحالم که رئیس‌جمهور دونالد ترامپ، بهترین دوستی که اسرائیل تا حالا در کاخ سفید داشته، در امانه و مهاجم قبل از اینکه بتونه آسیب بیشتری بزنه خنثی شده.
خشونت سیاسی، از جمله تلاش‌های مکرر برای ترور ترامپ، باید بدون هیچ ابهامی و با قاطعیت کامل از طرف همه محکوم بشه
@withyashar</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/withyashar/12313" target="_blank">📅 13:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/withyashar/12312" target="_blank">📅 13:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12311">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عجب سکوتی …</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/withyashar/12311" target="_blank">📅 13:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12310">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29d543059.mp4?token=G_A0Xb4QrHHQ7TslLVmWP2IIZcCzQT1I9-M3obrS-pKxqbSwFajRlmkg1QGCWxILhhPfyQmAVt5Ivql4iKW1kQXPgNVTU6RvPlmBQZJ7mmt94d3ixAbzgFPd0aUD0PyBf6THCFj4JlZcWLMT7OPiSyoyu9hAoIwU-xvmCP8WYK3g8BqGA9HWQdNX65Z4o9QGW7-q6oTe7ktr4W50h2EkM6Jszk6Qf0zKAMI5vkQxb5mA4nk5AWx48bhy_dJX6bA0bkfVz5TXX5xESwsUwDDtu7LdiBOLWO58ocNZHAG8HdikTcVLyEFLh1Xhm96uZyPomE6K2ro803ZlmJuWD6AG8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29d543059.mp4?token=G_A0Xb4QrHHQ7TslLVmWP2IIZcCzQT1I9-M3obrS-pKxqbSwFajRlmkg1QGCWxILhhPfyQmAVt5Ivql4iKW1kQXPgNVTU6RvPlmBQZJ7mmt94d3ixAbzgFPd0aUD0PyBf6THCFj4JlZcWLMT7OPiSyoyu9hAoIwU-xvmCP8WYK3g8BqGA9HWQdNX65Z4o9QGW7-q6oTe7ktr4W50h2EkM6Jszk6Qf0zKAMI5vkQxb5mA4nk5AWx48bhy_dJX6bA0bkfVz5TXX5xESwsUwDDtu7LdiBOLWO58ocNZHAG8HdikTcVLyEFLh1Xhm96uZyPomE6K2ro803ZlmJuWD6AG8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
🤣
بی بی عشقه</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/12310" target="_blank">📅 12:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12309">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال ۱۴ اسرائیل: نتانیاهو به وزرا دستور داده است از بحث در مورد توافق قریب الوقوع بین تهران و واشنگتن خودداری کنند
@withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/12309" target="_blank">📅 12:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12308">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/withyashar/12308" target="_blank">📅 12:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تسنیم: اختلاف بر سر یک یا دو بند در یادداشت تفاهم ادامه دارد. اگر آمریکا به ایجاد موانع ادامه دهد، امکان رسیدن به تفاهم وجود نخواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/withyashar/12307" target="_blank">📅 12:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12306">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رویترز به‌نقل از یک منبع ارشد ایرانی: ایران تحویل ذخایر اورانیوم خود را نپذیرفته و موضوع هسته‌ای بخشی از توافق اولیه نیست
@withyashar</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/withyashar/12306" target="_blank">📅 12:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12305">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فارس : ‌
احتمال دبۀ آمریکا در یکی از بندهای توافق اولیه؛ ایران بر مواضع خود ایستاده است
درحالی که مذاکرات به‌سمت توافق اولیه پیش می‌رود، منابع آگاه از احتمال بازگشت آمریکا به رویۀ قبلی و تخطی از یکی از بندهای مورد توافق اولیه خبر می‌دهند. این چندمین‌بار است که واشنگتن برخلاف توافق اولیه عمل می‌کند.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/withyashar/12305" target="_blank">📅 12:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12304">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ادعای العربیه: دور بعدی مذاکرات بین آمریکا و ایران ممکن است در ۵ ژوئن برگزار شود.
واشنگتن و تهران هنگام آغاز مذاکره برای توافق نهایی، روسای هیئت‌های خود را اعزام خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/withyashar/12304" target="_blank">📅 12:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الحدث به نقل از منابع: توافق اولیه احتمالی بین ایران و ایالات متحده «اعلامیه اسلام‌آباد» نام خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/withyashar/12303" target="_blank">📅 12:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بازنشری دوباره از صحبت های بسیار مهم از صحبت های مانوک درباره مذاکره و آینده ایران
مجری  :  آیا به توافقی میرسند؟
آیا مذاکره می‌کنند؟ یا ایران رد خواهد کرد؟
مانوک خدابخشیان : ایران رد نخواهد کرد، اگر بپذیرند خلع سلاح کامل می‌شوند، و مجبور به پذیرش بقیه شرط ها حقوق بشر دیگر برگ کوبنده ای نیست زیرا صدها برگ دیگر وجود دارد
مجری: ترامپ میگه پیشرفت زیادی در ارتباط با ایران به دست آمده! از این پیشرفت منظورش چیه؟
مانوک خدابخشیان : دونالد زبل بزرگترین خواسته اش اینه با یکی از این ها سلفی بگیره! ایمان داشته باشید«اینها با یک جماعتی در تهران ساخت و پاخت کردن!»نه این که رژیم بمونه!
یادتون نره!
همه ترسشون اینه امروز آمدن مذاکره کردن کار تموم شد ، استمرار پیدا کرد این رژیم ،نه اینچنین نیست.
«این تحلیل های آبکی رو بعد بذارید و بعد بگید »
آمریکا جایی که رفت مذاکره کنه مذاکره نمیکنه ، باز تکرار میکنم « حکم میکنه »
ببینید آیا رژیم جمهوری اسلامی حاضره مثل صدام حسین تحقیر بشه ؟ اینا به نوکر صدام گفتن برید بهش بگید تمام سلاح های اتمی و شیمیایش بده به ما و بعدش میشینیم مذاکره میکنیم و دیدید صدام حسین تو سری رو خورد چرا ؟ چون «بازی تموم شده رژیم کارش تمومه »
اگر یک آلترناتیو الان بود و اطمینان خاطر داشتن اینها در ایران بحران به وجود نمیاد قطعا عمل میکردن و الانم قول هایی گرفتن!
دلیل خوشحالی ترامپ هم همینه
@withyashar</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/withyashar/12302" target="_blank">📅 12:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/withyashar/12301" target="_blank">📅 11:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کیر استارمر، نخست وزیر بریتانیا:
پیشرفت به سمت توافق بین ایران و آمریکا رو تبریک میگیم. باید به توافقی برسیم که منجر به پایان درگیری بشه. حیاتیه که ایران هرگز نتونه سلاح هسته‌ای داشته باشه. با شرکای خود در جهان پیش میریم تا از این فرصت استفاده کنیم و به یک توافق سیاسی بلندمدت دست پیدا کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/12300" target="_blank">📅 11:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/12299" target="_blank">📅 11:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBFah_zdhDXNMY2SP1bvkxIzXyz0bi58rTHY8xY2qYLRVmIMbHWTmcSWc4E2zkYqjjGqVECweeUjOXy5T7rAYSjVLPwl02BHkAEQ0rke8hd8RRjii0uR-pqqWoIJSjRVBP9Rd56MSomhoBw3hhVBsLSna_rqiXC0cI5mpAUs06dkSsnVQXQKOd6ZChr5BE0imMoroGN94seqr1uVIn957OqUt1tPhLmd2AEWdRMFAKKkcoGkXaSwUxWkRwbHe9itueYMYFewrMKSkmCIVIaDgaJE2oPwFXwYV1uNxiNMCI3WPGbMuL5FaElHDvQLudJQ06PdEUOGGNOkiaNfa2HbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">B2 رسید
@withyashar</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/12298" target="_blank">📅 11:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/withyashar/12297" target="_blank">📅 11:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12296">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/withyashar/12296" target="_blank">📅 11:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انتقاد تند تد کروز، سناتور مطرح جمهوری‌خواه از اخبار توافق آمریکا و ایران :
به‌شدت نگران چیزهایی هستم که درباره توافق احتمالی با ایران می‌شنویم؛ توافقی که بعضی صداها داخل دولت آمریکا دارن برایش فشار میارن.
تصمیم ترامپ برای حمله به ایران، مهم‌ترین تصمیم دوره دوم ریاست‌جمهوریش بود. او کار درستی انجام داد و ما به نتایج نظامی فوق‌العاده‌ای رسیدیم؛ از جمله نابودی تمام موشک‌ها و پهپادهای ایران و غرق کردن کل نیروی دریایی‌شان.
اگر نتیجه همه این‌ها این باشد که حکومت ایران — که هنوز توسط اسلام‌گراهایی اداره می‌شود که شعار «مرگ بر آمریکا» می‌دهند — حالا میلیاردها دلار دریافت کند، بتواند اورانیوم غنی‌سازی کند و سلاح هسته‌ای توسعه دهد و کنترل مؤثری روی تنگه هرمز داشته باشد، آن وقت این یک اشتباه فاجعه‌بار خواهد بود.
جزئیات هنوز کامل منتشر نشده و امیدوارم گزارش‌های اولیه اشتباه باشند؛ اما اینکه راب مالیِ دولت بایدن از این توافق تعریف کرده، اصلاً امیدوارکننده نیست.
ترامپ به «صلح از طریق قدرت» اعتقاد دارد و رهبری قدرتمند او همین حالا آمریکا را امن‌تر کرده. او باید همچنان محکم بایستد، از آمریکا دفاع کند و خطوط قرمزی را که بارها اعلام کرده، اجرا کند.
@withyashar</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/12295" target="_blank">📅 11:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دلم میخواد یه ویس بی‌پروا بدم ولی افسوس ….</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/12294" target="_blank">📅 11:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12293">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خامنه ای کپک زد
ترامپ به ما کلک زد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/12293" target="_blank">📅 11:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12292">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانال 12 اسرائیل به نقل از یک مقام ارشد اسرائیلی:
توافق احتمالی اصلاً خوب نیست؛ چون به ایرانی‌ها این پیام رو میده که سلاحشون به اندازه بمب هسته‌ای خطرناکه و اونم تنگه هرمزه؛ ترامپ هم فکر میکنه این توافق فقط اقتصادی هست و شامل باز شدن متقابل تنگه هرمز میشه، ولی هر قدمی برای حل مسئله هسته‌ای وابسته به خروج اورانیوم ها هست. و اصلا معلوم نیست بعد از مرحله اول اصلاً چی پیش میاد.
@withyashar</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/12292" target="_blank">📅 11:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزیر امور خارجه آمریکا :
«ترامپ اجازه نمیده ایران به سلاح هسته ای دسترسی پیدا کنه احتمالاً جهان در ساعات آینده، به ویژه در مورد تنگه هرمز، اخبار خوبی خواهد شنید
»
@withyashar</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/12291" target="_blank">📅 11:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12290">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تسنیم : پیش‌نویس توافق با واشنگتن تصریح می‌کند که وضعیت حاکمیتی تنگه هرمز به شرایط قبل از جنگ برنمی‌گردد و تنها تعداد کشتی‌های عبوری ظرف ۳۰ روز، همزمان با لغو کامل محاصره دریایی و اجرای تعهدات ایالات متحده، به حالت عادی باز می‌گردند. تهران بر حفظ حق حاکمیتی خود بر این تنگه اصرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/12290" target="_blank">📅 11:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12289">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزیر امور خارجه آمریکا :
«هیچ کشوری نباید از گذرگاه‌های دریایی یا حریم هوایی سوءاستفاده کند و آزادی کشتیرانی باید تضمین شود
»
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/12289" target="_blank">📅 10:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال 14 اسرائیل : ایران تنگه رو بدون هیچ عوارضی باز می‌کنه و آمریکا هم هیچ پولی نمی‌ده و تحریمی رو برنمیداره فقط اجازه میده به ایران بتونه یکم نفت بفروشه ، احتمالأ اسرائیل هم حملاتش به لبنان رو قطع میکنه ، خلاصه اگه پذیرفته بشه یه آتش بس 30 الی 60 روزس که برای مذاکره داده شده بدون هیچ امتیازی اجازه نفس کشیدن میده به جهان
@withyashar</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/12288" target="_blank">📅 10:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اکسیوس؛شرایط پیشنهادی تفاهم‌نامه آمریکا و ایران:
🚨
🚨
🚨
🚨
🚨
🚨
🚨
آتش‌بس ۶۰ روزه بین دو طرف.
بازگشایی تنگه هرمز بدون عوارض.
پاکسازی مین‌های دریایی در تنگه توسط ایران.
رفع محاصره بنادر ایران توسط آمریکا.
معافیت‌های تحریمی که به ایران اجازه صادرات نفت رو میده.
تعهد ایران به مذاکرات درباره تعلیق غنی‌سازی اورانیوم.
مذاکره ایران درباره حذف ذخایر اورانیوم بسیار غنی‌شده.
مذاکره آمریکا درباره رفع تحریم‌ها و آزادسازی دارایی‌های ایران در دوره ۶۰ روزه.
باقی‌موندن نیروهای آمریکایی در منطقه طول مذاکرات.
پایان گزارش‌شده جنگ اسرائیل و حزب‌الله در چارچوب این توافق.
@withyashar</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/12287" target="_blank">📅 10:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کابینه جنگ اسرائیل امشب تشکیل خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/12286" target="_blank">📅 10:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g79lygJiftk7ManljYiTavbvkc6D6H_YVakJh0TAnUz1vhmpWChVJc2PblBhMa4sFH_w1eLKlbCtPTBaZ_L7gqD_Drn-hHJyTY-SU1FKdBiOROCM8jlP0a3zVWvXoDtBGwIrGxDTWxOz96-5RojDxJuP9-XJcY78Vh5waCaaWpkhEev6dxUG8f3WSRuxIPBoDpYbbgQithO59oHZgJfn23y75gyHR54vkH-PIYrYIrq7cMkx-NSawOXyXBljCK0B3cheomO0IkoRQrGtd2I7yl_6JRyNm9dfnujc84EufhM3qeDbvQXYoubBWUReyyxDWmQoRvOoX0A715PS2CUy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس فرد مهاجم ۲۱ ساله در نزدیکی کاخ‌سفید
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/12285" target="_blank">📅 10:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">احتمال از سرگیری روابط دیپلماتیک ایران و آمریکا
آکسیوس به نقل از مشاوران ترامپ:
رئیس جمهور آماده است در صورت برآورده شدن خواسته‌هایش در مورد برنامه هسته‌ای، روابط با ایران را از سر بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/12284" target="_blank">📅 10:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12283">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIFSE3tYhwD6G3v2ZPF_NoZfm3Q2L_XZ4Ywfg86umPR2j9R6z6Vd-LkjBkbtvhnGoVIMawPAAagfJgGseWsxPAY1ZiWHcfhNwsIgMIzfDJi1t0kDt78s5nO7e72FNZEoOUk0rcahwdWYU-KE7fVVRuJCVvKnZpSCCq9NZfNbRa0kZ_3tAd60oG3tpqFzqShLzw19vUv2VXc2rMzaaWGBgO4DtsMigvVOEOpbhl1sSScZdlHLXy6Djm3HpTA_xwmKGGGRmp6hj7ICtUbLc5lcRm6dIBQYcgflFEByoY82e5jVdHyHok3kQSQkpAMo7s86Z5qStfEm21nW1QQOp0m_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از سرویس مخفی و نیروی انتظامی عالی‌مون به خاطر اقدام سریع و حرفه‌ای که امشب علیه یک فرد مسلح در نزدیکی کاخ سفید، که سابقه خشونت‌آمیز و احتمالاً وسواس فکری نسبت به گرامی‌ترین بنای کشورمون داشت، انجام شد، سپاسگزاریم.
فرد مسلح بعد از درگیری با مأموران سرویس مخفی در نزدیکی دروازه‌های کاخ سفید کشته شد.
این اتفاق یک ماه بعد از تیراندازی در ضیافت شام خبرنگاران کاخ سفید رخ داد
برای همه روسای جمهور آینده مهمه که امن‌ترین و مطمئن‌ترین فضایی رو که تاالان در واشنگتن دی سی ساخته شده، داشته باشن.
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/12283" target="_blank">📅 10:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12282">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007a727a10.webm?token=Lpu8dAiadDHyDuYmzw6B6ubk110Sr8LjcMuBZfKDcmJpGkYpnMqWQYhiQ79oK3nYvycB6uGnCOG3o5hhcU79qIUOYSpOUlOCb5uldqQiuxs7FqD2bsZz1eIZin9pyvuVkLVoX60RdzBVtf7ob7mn0_O45HnhO2nZi1imTuxQFLQM3EeA9GZ342Y8jOz0dASJYn1p3tgCLQjzM29pjioorywVm9xWoICW0NGEVuID0xBPIa5DFqgPECPQYRJIfoHJTeGkCKky75bMz5ipU3rwUQ2X-cSgMtBj8odtKdtLK_KBMLkn1G8AV2EeGFR_X84Kaha3ZbMauEdghIkMCkOzAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007a727a10.webm?token=Lpu8dAiadDHyDuYmzw6B6ubk110Sr8LjcMuBZfKDcmJpGkYpnMqWQYhiQ79oK3nYvycB6uGnCOG3o5hhcU79qIUOYSpOUlOCb5uldqQiuxs7FqD2bsZz1eIZin9pyvuVkLVoX60RdzBVtf7ob7mn0_O45HnhO2nZi1imTuxQFLQM3EeA9GZ342Y8jOz0dASJYn1p3tgCLQjzM29pjioorywVm9xWoICW0NGEVuID0xBPIa5DFqgPECPQYRJIfoHJTeGkCKky75bMz5ipU3rwUQ2X-cSgMtBj8odtKdtLK_KBMLkn1G8AV2EeGFR_X84Kaha3ZbMauEdghIkMCkOzAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/12282" target="_blank">📅 08:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12281">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تیرانداز به هلاکت رسید و فرد حاضر زنده و هوشیار است. هر دو به بیمارستان منتقل شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/12281" target="_blank">📅 02:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds9BVYoM4G5DddDo9EqTDrqtMKGdrUShDtv2KLKfGccDcmIWoLzwAhTUIUBuQvE9hQI0Es_oVPlHI36XIFs_e6gDvS_iq-E7LIxfSfSyHsAWYUCiaz9u5cfw3zl37HvHMHUDlOVh1KTrwaC_s53ClqoT98E8hIjFwvsDelwQNZpmvPISXOATwjhuq8_-KYubNxBNCiJYIp2mhKhpbQVg48HYNSSWfJX5wlxYthmGa5isEq3as9IqjJpS71QrVc3aGs9Bz8QFBdDIX4doMNYOWYKvJ5WBoTIIiUSnlR9lqtlxOgdlVxvtzUM6vEoEA8HI0KsFllTZSC3tbDgC4Rvjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس مخفی پس از شروع تیراندازی در سمت غرب کاخ سفید به یک مظنون مسلح شلیک کرد، به گزارش فاکس نیوز.
یک عابر پیاده در این حادثه زخمی شد و تأیید شده است که رئیس‌جمهور ترامپ در امنیت است.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/12280" target="_blank">📅 02:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12279">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بی‌بی‌اس نیوز گزارش داد: در تیراندازی نزدیک کاخ سفید دو نفر زخمی شدند که یکی از آن‌ها مظنون است.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/12279" target="_blank">📅 02:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12278">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22e5d7ca97.mp4?token=bHu1BD75yBDj7yKQt9prbAZkTxM1HY4ykTDmNY5pkm9nGPJcMXPfqyadtYkPBPIlPXXbn9cgEs4l8rC8Ka6eO35nijHS-hHtXvR9qhq7pNF-B6ViKbNFqqeOKJlFxM-0iY0Nc9H4qBYShSb6DZUCDo0QOk71WXTGOa-DvUIoUoFLT7AayOY1-wf4j0bQ5QNZ7PFI8OpbGEud2TiqDdqtB_7_92GaBretq9URRx2VwTzIGJa80afojmVEWx71ImJtyCJHVeBeyY5ygkwxEzjGlhNTyZm3vrA-8YXk4WqJsTUpMoxiwV5R5WUFubUHfiNMsDHtNvpZFH_WKRQWbDcb7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22e5d7ca97.mp4?token=bHu1BD75yBDj7yKQt9prbAZkTxM1HY4ykTDmNY5pkm9nGPJcMXPfqyadtYkPBPIlPXXbn9cgEs4l8rC8Ka6eO35nijHS-hHtXvR9qhq7pNF-B6ViKbNFqqeOKJlFxM-0iY0Nc9H4qBYShSb6DZUCDo0QOk71WXTGOa-DvUIoUoFLT7AayOY1-wf4j0bQ5QNZ7PFI8OpbGEud2TiqDdqtB_7_92GaBretq9URRx2VwTzIGJa80afojmVEWx71ImJtyCJHVeBeyY5ygkwxEzjGlhNTyZm3vrA-8YXk4WqJsTUpMoxiwV5R5WUFubUHfiNMsDHtNvpZFH_WKRQWbDcb7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
تیرندازی از دیدی دیگر</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/12278" target="_blank">📅 02:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12277">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egwzg8gTuNYZRuG5GU9vnmttflidrmqCj1N4sOZAxNOBYor0dV5VlI0TCe_ZH_BQ0t5p_a451DG5-xoFhcglvm7EVzoZCzWNePdNEZDDMma0zmey6eh_Xmbq5TGkm3N91E4zx7BhzGGJVpr-bAXIyDUVqdi_IXUcyC2OYjaEUytcbsfxPXBJQY77TottU1eWxpSxZDJHWAREfnGG8RE9qUO-uNztDR-kIr2fp4y79opKUTtZzwh89ku2ALLNdSCP0NlLF3-HCn9jrnn_CfDe7EzVDzuYaIT16FWXkAaUWUcHUUA9Hz20SS-gVxH3Pps5sDCpegLpmT24y_AzYR-gjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه هایی از خارج از کاخ سفید.
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/12277" target="_blank">📅 02:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12276">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مدیر اف‌بی‌آی کاش پاتل:
اف‌بی‌آی در محل حاضر است و از سرویس مخفی که به شلیک‌های نزدیک محوطه کاخ سفید پاسخ می‌دهد، حمایت می‌کند, ما به محض امکان، به‌روزرسانی‌های لازم را به عموم ارائه خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/12276" target="_blank">📅 02:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12275">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978b6cb95d.mp4?token=Z6Z8lL-ICvRXP8PHBfb_zdP8shs_5XJQpdvsCADxbS8PHMOUjky2OzgKS940l7TWJn7SyeJL4vDf-bCesGdiUlUgqigHPbfNnp8g50JQv4IQ4kAUt2_cw7tT-Tgp9pHBg-ZC7JgjfK0kslBLZ8NIzpt6bf3N5PNwqKviyNiYEP7UCcePgaM8gwYlX9NCwb4JdGpHZVLzGuCQO3n7Tm9bdkvIDeaWLyADEd35RZA7_BgXHCxqNzfs8mekxIz62AJuPoZdNEn8bd-0YdxtSjLvXaS0eC3e0G-F6alN3u349uXnqaYbGuS9sKSwRfLU0HhI3Hjpu24WKj9rGuWkCbl7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978b6cb95d.mp4?token=Z6Z8lL-ICvRXP8PHBfb_zdP8shs_5XJQpdvsCADxbS8PHMOUjky2OzgKS940l7TWJn7SyeJL4vDf-bCesGdiUlUgqigHPbfNnp8g50JQv4IQ4kAUt2_cw7tT-Tgp9pHBg-ZC7JgjfK0kslBLZ8NIzpt6bf3N5PNwqKviyNiYEP7UCcePgaM8gwYlX9NCwb4JdGpHZVLzGuCQO3n7Tm9bdkvIDeaWLyADEd35RZA7_BgXHCxqNzfs8mekxIz62AJuPoZdNEn8bd-0YdxtSjLvXaS0eC3e0G-F6alN3u349uXnqaYbGuS9sKSwRfLU0HhI3Hjpu24WKj9rGuWkCbl7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/12275" target="_blank">📅 02:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12274">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d610a95e.mp4?token=F7aQmyCLpewNHO1PrZxZdpZraW7wRmDRMKZJYEu5s9Z8VpW3RbsptHiVxGh0jV4RLE4N7s3_IsCP6th5vt5DR5hIjucHjGXY3MDVSobziCrKsEmpWOHFiKOHi2gEF0LwuKO8wkL0YwEE4HPUT7lUQkLlro2ulSFvfT5UbPFGdKgINA0NXBPhnMyP4pmItLVV-XHMWsO-rTf5JjIcSYl5X9wQzyICRT8ElzJdt15-OvPJtnL2pcf7SQwjX67zJDGQoBi6i1vGIIgSSCfpbq44ES_0d_1fReANeWO6EdUSWJvRjgZocgZzYFuHlEFDH5jdnAOoCw8-Xjq2kpD-TfgpDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d610a95e.mp4?token=F7aQmyCLpewNHO1PrZxZdpZraW7wRmDRMKZJYEu5s9Z8VpW3RbsptHiVxGh0jV4RLE4N7s3_IsCP6th5vt5DR5hIjucHjGXY3MDVSobziCrKsEmpWOHFiKOHi2gEF0LwuKO8wkL0YwEE4HPUT7lUQkLlro2ulSFvfT5UbPFGdKgINA0NXBPhnMyP4pmItLVV-XHMWsO-rTf5JjIcSYl5X9wQzyICRT8ElzJdt15-OvPJtnL2pcf7SQwjX67zJDGQoBi6i1vGIIgSSCfpbq44ES_0d_1fReANeWO6EdUSWJvRjgZocgZzYFuHlEFDH5jdnAOoCw8-Xjq2kpD-TfgpDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارش‌ها، تیم‌های تک‌تیرانداز سرویس مخفی اکنون بر روی پشت‌بام کاخ سفید قابل مشاهده هستند.
این یک واکنش حفاظتی استاندارد پس از یک حادثه امنیتی است که در آن تیم‌ها برای ایمن‌سازی محوطه به موقعیت‌های مرتفع اعزام می‌شوند.
این با وضعیت فعال پس از گزارش‌های قبلی تیراندازی و انتقال خبرنگاران به داخل کاخ مطابقت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/12274" target="_blank">📅 02:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12273">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4f39d6.mp4?token=NJYaskUo2b2JxBYJjk_nkfE8H9v_mjYwJVKjWLHESuo66lMnrj5dRM44iy464LfzoxubZlAh0HH3SO5pwFIUZ98qOi5xTxdLhb30jS53FKIfOGSCL3nxpign4_y_074Q-LvXJlBg8PoKDfQZdYCVQS86ZiVwsbq0CPR-nzkOMysJ5Lepri6Tj0L4QJc43Ebx1n7xoKGk7_5XCyrsZNCRIgirv9qQgL9vyuGT674kqh0WSLS6dVfJ9jZ7XdlrU-FUfzHhclIm3RKZZVi952azp6cvqETJW-8p1CrB8cSdvvmIMRHgIMAnjbPdL1QO2orHimV8bz1iIRBICx3KIcT03w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4f39d6.mp4?token=NJYaskUo2b2JxBYJjk_nkfE8H9v_mjYwJVKjWLHESuo66lMnrj5dRM44iy464LfzoxubZlAh0HH3SO5pwFIUZ98qOi5xTxdLhb30jS53FKIfOGSCL3nxpign4_y_074Q-LvXJlBg8PoKDfQZdYCVQS86ZiVwsbq0CPR-nzkOMysJ5Lepri6Tj0L4QJc43Ebx1n7xoKGk7_5XCyrsZNCRIgirv9qQgL9vyuGT674kqh0WSLS6dVfJ9jZ7XdlrU-FUfzHhclIm3RKZZVi952azp6cvqETJW-8p1CrB8cSdvvmIMRHgIMAnjbPdL1QO2orHimV8bz1iIRBICx3KIcT03w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از اخبار ABC لحظه‌ای را ثبت می‌کند که تیراندازی در خارج از کاخ سفید رخ داد.
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/12273" target="_blank">📅 01:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12272">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طبق گزارش NBC News، صدای تیراندازی در خارج از کاخ سفید شنیده شد، با حدود ۲۰ تا ۳۰ گلوله شلیک شده. سرویس مخفی به اعضای مطبوعات که در چمن شمالی جمع شده‌اند دستور داده است که به داخل اتاق جلسه بروند.
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/12272" target="_blank">📅 01:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12271">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87c6f32ee8.mp4?token=GuYYmYjEfnX-c48gCU-NFXvjSeDSxJ3LaSnEuhgtrJamihPPi1h3Ip6Uehf9UJnDEml5ukZswqQiCdmsMGHAn8-LI1aFAzeMCm_c_aVj0AiRqt8uw1CORGWcPex1GPXZ9nj53DzN1uvCfT6p1kS_ShK4w1_i-uEqAo-sa5pXB4u7U1ZZR5y4iZQ5dXMrXy-9VZ0kWhJzQ7DSYmxIGkZ0AcXuExJ8TW5evwwIxERvBh4CJzpZRtUBADEKIDC2zvoHZIidI7AoB3gMdWhun2l_bto9B5Zgjxh5cIMYiRu4qIkAxpl6eTGvXko86qmUwDaGmu9XUQM0jYr_61CzcJzTyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87c6f32ee8.mp4?token=GuYYmYjEfnX-c48gCU-NFXvjSeDSxJ3LaSnEuhgtrJamihPPi1h3Ip6Uehf9UJnDEml5ukZswqQiCdmsMGHAn8-LI1aFAzeMCm_c_aVj0AiRqt8uw1CORGWcPex1GPXZ9nj53DzN1uvCfT6p1kS_ShK4w1_i-uEqAo-sa5pXB4u7U1ZZR5y4iZQ5dXMrXy-9VZ0kWhJzQ7DSYmxIGkZ0AcXuExJ8TW5evwwIxERvBh4CJzpZRtUBADEKIDC2zvoHZIidI7AoB3gMdWhun2l_bto9B5Zgjxh5cIMYiRu4qIkAxpl6eTGvXko86qmUwDaGmu9XUQM0jYr_61CzcJzTyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت اعصاب و روان من الان
👺
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/12271" target="_blank">📅 01:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12270">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الحدث: ایران و آمریکا به دشمنی طولانی مدتشون پایان دادن!
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/12270" target="_blank">📅 01:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12269">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/12269" target="_blank">📅 01:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12268">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">«نیویورک تایمز به نقل از سه مقام ایرانی: در این توافق موضوع هسته‌ای را به مرحله‌ای بعدی موکول می‌کند.
ولی این توافق به آزادسازی ۲۵ میلیارد دلار از دارایی‌های مسدودشده در خارج از کشور منجر خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/12268" target="_blank">📅 01:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12267">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">المیادین:
آنچه پیشنهاد می شود یک توافق نهایی نیست، بلکه یک یادداشت تفاهم است.
این یادداشت تفاهم شامل هیچ بند مرتبط با پرونده هسته ای ایران نمی شود.
این یادداشت بر پایان جنگ و ترتیبات آتش بس متمرکز است. این تفاهم نامه شامل تسهیل دریانوردی در تنگه هرمز است.
این تفاهم نامه شامل خروج ناوگان آمریکایی از مجاورت ایران است.
این تفاهم نامه شامل آزادسازی نیمی از وجوه مسدود شده ایران است که بالغ بر 12 میلیارد دلار است.
این یادداشت شامل پایان محاصره نظامی دریایی ایالات متحده است. مهلت 30 روزه برای دستیابی به توافق هسته ای پس از امضای چارچوب توافق داده شد.
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/12267" target="_blank">📅 01:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12266">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فارس : ایران هیچ توافق هسته ای هم با امریکا نداشته
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/12266" target="_blank">📅 01:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12265">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دقایقی پیش صداسیما گفت ادعای ترامپ در خصوص بازگشایی تنگه هرمز دروغ است و تنگه دست ایران خواهد ماند
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/12265" target="_blank">📅 00:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12264">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScfjMM9ruvVmulGwgg7vRHMHOtNdJdUPB68RFPln6TyalxaQvIzlebDvSbwxxz9qKynKg0_ZyY2DTicjRDrXOSb_SvQsCfP3j90VbXz6LkoPCxLhkOSiR2ZAAoajJWO2N-tkK70XFQnjc8cuotuTQUAidXKgFQJHcVNrvlhM1GN25yrEVdciNSm78xfAJq1hvQnNZN2G8R61PgSJhyL6U4CfeRrL8QHbSkH9zgy7akV9PF865KemLuW_OO4yM6_b_oCn5GdchNv36zxrzONPkrrmfOp_1te1BDTP40Pl4SF07Kv9Yh46_IUYS2Md_6nyGU8q6Bqu4sqAOZCIHEDM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ کمی پیش در حال تماس با سران کشورها
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/12264" target="_blank">📅 00:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12263">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرنگار کانال 12 اسرائیل:
ترامپ تسلیم خواسته های ایران شد
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/12263" target="_blank">📅 00:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer"><a href="https://t.me/withyashar/12262" target="_blank">📅 00:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12261">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/12261" target="_blank">📅 00:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA M</strong></div>
<div class="tg-text">یاشار فکر میکنم خیلیا که پنیک میکنن تازه به جمعمون اضافه شدن
اونای که قدیمین فقط میشینن به این اتفاقات میخندن چون از چیزای با خبرن و شناخت دارن که بقیه نمیفهمن
البته این اتفاق زمانی میفته که نقشه راهو نداشته باشی
ولی ما که میدونیم چه خبره
😉</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/12260" target="_blank">📅 00:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/12259" target="_blank">📅 00:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12258">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/12258" target="_blank">📅 00:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12257">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/12257" target="_blank">📅 00:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12256">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChhT0jrhuBy3hc6C8PI_JIDM4OQREeX96am0qwmfPMvuqCGEaeVTpCX94PVQp4zPqUA8Vkj4aM93njJJ8V5r77k6St_I5oToxtIkthqqegh27F9atK32z6_hxetVNrCusi3CkCA_eRIOfvX4MyYiXiqDgJQ3FjwLHrAAMvBE4XO4pKLzG4fldWvL1T2DCsvLccHJoC-rDz9NQ0EEQdzCv6kvoqszxSVsDbBiUX1e669SmqBGucYGaUph8tYzGM-V9kpUgvNVVLCgmJx4IiptBuCbagRb-Ak3QFsPXhOwgvJxdo80XBS3RraDJxjxuG2m7lX064YRVRgZEmRuBKDxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸ سوخت رسان از اسرائیل بلند شدن شاید بیشترم بشن هنوز چند تا رو باندن دارن پا میشن !!!!!
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/12256" target="_blank">📅 00:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12255">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فقط کی حالتو خوب‌ میکنه ؟ عمو یاشار حالا اگه این پست رو ریکشن آتیش فقط بزنی میگم</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/12255" target="_blank">📅 00:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anvZM_3HMyeD_J6MZSB6lJpJDYZfKRZ6oV7_sai4enh47cPJsQzoHl3aN538ccZykOgkiKeaT51vdjySkazZiXjd0aBxy47cv_P5ru2rhas6GyUUf9SbR9XV1X1nQqwwCQ2MCse77vb3gFmLKrhuMLvjJNKCPN9i492s9C7a2mnPUOVGy9uYyPyU32ztP6It_9ZOn82t98uHvtex441l7kUUjWE2Ed_m5mNJuKdVk4sN2jsGN8TenrZNSY5kIcOqFtaltoew-SgpZQkzkiGj01SXTqJ7WdWhgrep1bk_ldJkw5JWqMEND6EJmVDSmglw-ozp3xGygC_jEG4LvQd5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «من اکنون در دفتر بیضی کاخ سفید هستم؛ جایی که همین حالا گفت‌وگوی بسیار خوبی با محمد بن سلمان آل سعود، عربستان سعودی؛ محمد بن زاید آل نهیان، امارات متحده عربی؛ امیر تمیم بن حمد آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم آل ثانی و وزیر علی الثوادی از قطر؛ فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛ رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛ و حمد بن عیسی آل خلیفه، پادشاه بحرین، دربارهٔ جمهوری اسلامی ایران و همهٔ مسائل مرتبط با یک یادداشت تفاهم مربوط به صلح داشتیم.
@withyashar
یک توافق تا حد زیادی مذاکره و تنظیم شده است، اما نهایی شدن آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد، همچنان منوط به تکمیل جزئیات است.
@withyashar
به‌طور جداگانه، با نخست‌وزیر اسرائیل، بیبی نتانیاهو، نیز گفت‌وگو کردم که آن هم بسیار خوب پیش رفت.
جنبه‌ها و جزئیات نهایی توافق در حال حاضر در دست بررسی است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بخش‌های دیگر این توافق، تنگهٔ هرمز نیز بازگشایی خواهد شد.
از توجه شما به این موضوع سپاسگزارم
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/12254" target="_blank">📅 00:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12253">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12253" target="_blank">📅 23:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ در تروث:  ممنونم رئیس‌جمهور اردوغان!  ترامپ همون رهبریه که دنیا قرن‌ها منتظرش بود فقط از قدرت حرف نمی‌زنه، خودش نماد قدرته. @withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/12252" target="_blank">📅 23:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/12251" target="_blank">📅 23:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/12250" target="_blank">📅 23:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرنگار العربیه: مقر گروه‌های مخالف نظام ایران در «وادی آلانه» در اربیل با 4 پهپاد هدف حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/12249" target="_blank">📅 23:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/12248" target="_blank">📅 23:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b7da70d7.mp4?token=i7l0JyjQ2DxbdwD3xC3Oq0XRuaKC9X9837DyOkt1B8yA-KQUKy4IdKo-Vam_NnG3QSQmJMJZDdnb03Uh8_-QY93zJ7bf_oMDxpsVG9sJYUD5_I0NS8zmRKr3u9srlDB3khSMYxxp7ieptzw_c8rCVROnRMgNO7iFS89MD_R3dhdOpYq8HuMjcjtjibsY3re0Y1Itek1IY8CLT1bCa6ONoGLBNr-MPULkMzKHrZvwkxw2HB1rq5AqR07qXJiVrXUdlsTVn3tYodebkMLCSRoKDLfOZ7ZVCIAVuHxSicbB52nf1aPXSnA3fQgnnKGltF8H5X47zz0yxIniJ72w8YyiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b7da70d7.mp4?token=i7l0JyjQ2DxbdwD3xC3Oq0XRuaKC9X9837DyOkt1B8yA-KQUKy4IdKo-Vam_NnG3QSQmJMJZDdnb03Uh8_-QY93zJ7bf_oMDxpsVG9sJYUD5_I0NS8zmRKr3u9srlDB3khSMYxxp7ieptzw_c8rCVROnRMgNO7iFS89MD_R3dhdOpYq8HuMjcjtjibsY3re0Y1Itek1IY8CLT1bCa6ONoGLBNr-MPULkMzKHrZvwkxw2HB1rq5AqR07qXJiVrXUdlsTVn3tYodebkMLCSRoKDLfOZ7ZVCIAVuHxSicbB52nf1aPXSnA3fQgnnKGltF8H5X47zz0yxIniJ72w8YyiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیت رهبری رو جوری زدن که شده بیابان
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/12247" target="_blank">📅 23:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رویترز:
یک چارچوب سه مرحله‌ای برای مذاکرات آمریکا و ایران پیشنهاد شده:
پایان رسمی جنگ.
حل و فصل بن‌بست تنگه هرمز .
باز کردن پنجره مذاکره ۳۰ روزه برای توافقی گسترده‌تر.
امکان تمدید آتش بس نیز وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/12246" target="_blank">📅 23:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کنسول جمهوری آذربایجان در تبریز بر اثر تصادف در اتوبان جلفا-تبریز جان باخت.
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/12245" target="_blank">📅 23:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سناتور لیندسی گراهام:
اگه با ایران توافق کنیم فقط بخاطر اینه که چون فهمیدیم نمی‌تونیم تنگه هرمز رو از دست ایران حفظ کنیم و ایران هنوز هم میتونه زیرساخت‌های نفتی خلیج فارس رو نابود کنه؛ یعنی اون‌وقت ایران به‌عنوان قدرت غالب منطقه شناخته میشه و همه مجبور میشن باهاش دیپلماتیک کنار بیان.
اینکه ایران بتونه همیشه تنگه هرمز رو به‌هم بریزه و همزمان توان ضربه سنگین به نفت خلیج فارس رو داشته باشه، موازنه قدرت منطقه رو کامل عوض میکنه و در آینده واسه اسرائیل تبدیل به کابوس میشه.
من شخصاً قبول ندارم که نشه جلوی توان ایران رو گرفت یا منطقه نتونه از خودش در برابر قدرت نظامی ایران دفاع کنه. باید خیلی حواسمون باشه که این قضیه رو خراب نکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/12244" target="_blank">📅 23:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرنگار لبنانی در شبکه سه: حزب‌الله بر روی نابودکردن گنبد آهنین اسرائیل تمرکز کرده است!
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/12243" target="_blank">📅 23:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">توییت مارک لوین:
شما متحدی را که در یک عملیات نظامی بزرگ در کنار شما جنگیده است، کنار نمی‌گذارید. یا این فقط یکی دیگر از فهرست طولانی تهمت‌ها علیه نتانیاهو است که نیویورک تایمز و جروزالم پست بدنام از او متنفرند، یا یک اشتباه استراتژیک بسیار بزرگ است.
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/12242" target="_blank">📅 23:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/12241" target="_blank">📅 23:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/12240" target="_blank">📅 23:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پرواز گسترده جنگنده های آمریکایی در نزدیکی مرز ایران
@withyashar</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/12239" target="_blank">📅 23:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">علی خضریان، عضو کمیسیون امنیت ملی مجلس :
در هر توافقی ایران حتما باید غرامت جنگ را دریافت کند.
شرایط تنگه هرمز به قبل از جنگ برنخواهد گشت این دستاورد و  مطالبه رهبری است .
مطالبه ملت ایران است که از مدیریت تنگه هرمز عقب‌نشینی نشود
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/12238" target="_blank">📅 22:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گروه کرد ایرانی کومله می‌گوید پهپادها کمی پیش پایگاه‌های آن را در استان اربیل، کردستان عراق، مورد حمله قرار دادند، در حالی که پهپادهایی توسط «هواپیماهای ائتلاف» سرنگون شدند.
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12237" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">همین الان دارن میجنگن فقط تو عراق
😂</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/12236" target="_blank">📅 22:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جنگنده‌های نیروی هوایی ایالات متحده در حال حاضر بر فراز منطقه خلیفان در استان اربیل در شمال عراق پرواز می‌کنند تا پهپادهای ایرانی را که گروه‌های مخالف کرد-ایرانی در منطقه را هدف قرار داده‌اند، رهگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/12235" target="_blank">📅 22:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فاکس نیوز:هنوز هیچ توافقی بین رژیم جمهوری اسلامی و آمریکا صورت نگرفته
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/12234" target="_blank">📅 22:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یاشار جان این ترامپ اشتباهی بجای اینکه مارو ببره قاهره داره میبره بورکینافاسو
😂
😂
😂</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/12233" target="_blank">📅 22:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi</strong></div>
<div class="tg-text">یاشار جان این ترامپ اشتباهی بجای اینکه مارو ببره قاهره داره میبره بورکینافاسو
😂
😂
😂</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/12232" target="_blank">📅 22:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانال 14 اسرائیل: چند منبع معتبر تأیید می‌کنند که ایران با برخی از درخواست‌های کلیدی ایالات متحده موافقت کرده است و کمتر از 24 ساعت دیگر اعلام توافق انجام خواهد شد که به تهران چند ماه فرصت می‌دهد تا کاملاً تسلیم شود
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/12231" target="_blank">📅 22:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به منظور بررسی آخرین تحولات مذاکرات با ایران، جلسه امنیتی محدودی برگزار خواهد کرد. یک منبع اسرائیلی در گفت‌وگو با سی‌ان‌ان این خبر را اعلام کرد.
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/12230" target="_blank">📅 22:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
چند منبع معتبر تأیید می‌کنند که ایران با برخی از درخواست‌های کلیدی ایالات متحده موافقت کرده است و کمتر از ۲۴ ساعت دیگر اعلام توافق انجام خواهد شد که به تهران چند ماه فرصت می‌دهد تا کاملاً تسلیم شود.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/12229" target="_blank">📅 22:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هم اکنون تماس تلفنی نتانیاهو و ترامپ! @withyashar</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/12228" target="_blank">📅 22:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ با سران منطقه گفتگو کرد
آکسیوس:
ترامپ روز شنبه با رهبران عربستان سعودی، امارات متحده عربی، قطر، مصر، ترکیه و پاکستان تماس تلفنی داشت.
به گفته منبعی که از جزئیات این تماس مطلع شده، چند تن از این رهبران عرب از ترامپ خواستند که توافق را بپذیرد.
@withyashar</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/12227" target="_blank">📅 22:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هم اکنون تماس تلفنی نتانیاهو و ترامپ!
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/12226" target="_blank">📅 22:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/12225" target="_blank">📅 21:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هم اکنون جلسه اضطراری امنیت ملی دولت ترامپ در اتاق جنگ کاخ سفید در حال برگزاری است.
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/12224" target="_blank">📅 21:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/12223" target="_blank">📅 21:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به گفته یک مقام آمریکایی که توسط اکسیوس نقل شده است، دونالد ترامپ هنوز تصمیم نهایی خود را در مورد این توافق نگرفته است
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/12222" target="_blank">📅 21:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">من که میدونیم ترامپ کار رو در میاره ولی این رسمش‌ نبود که این کارا رو با ما بکنه
😂
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/12221" target="_blank">📅 21:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الحدث به نقل از یک منبع عالی‌رتبه: تنها ساعات کمی تا اعلام توافق بین آمریکا و ایران فاصله است
@withyashar</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/12220" target="_blank">📅 21:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">معاون رئیس‌جمهور ونس به کاخ سفید رسید
۱ دقیقه تا تماس تصویری ترامپ با شیوخ کشور های خلیج فارس
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/12219" target="_blank">📅 21:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/12218" target="_blank">📅 21:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParisa</strong></div>
<div class="tg-text">یاشار جان خسته نباشی
تو ویس های آخرت احساس ناامیدی کردم والا تو ماشین نشستم گریه میکنم
ما به امید شما امیدواریم
من پدرام مادرم بالای ۸۰ دارن و مریضن و من دیگه نمیتونم برم ایران ببینمشون
به امید ویس  و تحلیل های شما تا حالا گذروندم
✌🏼
💔</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/12217" target="_blank">📅 21:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3610291d.mp4?token=pfmiCDRl_z5UBBV7h8RdfW5I-IwdpflbFXOvc7m02i_6pCTjKNWr3pmaklECl8_83xuUjHu-DQxG8VCA5nTgbA5No4OZYQyy0kmdzHqbIPQg91VzDd3b2E4RbNWeWlM2i2HUB-jXgVD44FRmrKrZHVYRpDbySm_oSbnONPywee4cyOQRmLqIqYk-OEe2RfoqS59fcdzJZUgubQ8hGQ82NS2ZYGq4j52BIRw6tHSltzIWWv29rVwllvP2tiH9MLkzQzQuMKyNtBuzuKvrBP9BXduPp9loTUQZfuSvtlA5mD0cKUhz6DpVQCBETqrSqMYjNISEQwlqC4vLrNM0n0ie_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3610291d.mp4?token=pfmiCDRl_z5UBBV7h8RdfW5I-IwdpflbFXOvc7m02i_6pCTjKNWr3pmaklECl8_83xuUjHu-DQxG8VCA5nTgbA5No4OZYQyy0kmdzHqbIPQg91VzDd3b2E4RbNWeWlM2i2HUB-jXgVD44FRmrKrZHVYRpDbySm_oSbnONPywee4cyOQRmLqIqYk-OEe2RfoqS59fcdzJZUgubQ8hGQ82NS2ZYGq4j52BIRw6tHSltzIWWv29rVwllvP2tiH9MLkzQzQuMKyNtBuzuKvrBP9BXduPp9loTUQZfuSvtlA5mD0cKUhz6DpVQCBETqrSqMYjNISEQwlqC4vLrNM0n0ie_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر جنگ پیتر هگستث
:
اولین حمله هوایی که هرگز انجام دادم و یک دسته را در وسط شب در بغداد رهبری کردم. ما ۳۶ ساعت برای آماده‌سازی داشتیم و من هر دقیقه از آن ۳۶ ساعت را صرف آماده‌سازی کردم.
وقتی خلبان‌ها ما را چند صد متر در نقطه اشتباهی در وسط یک زمین گل‌آلود فرود آوردند و GPS کار نمی‌کرد.
یک مرد بود که آن دسته به او نگاه می‌کردند و آن مرد من بودم.
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/12216" target="_blank">📅 21:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/12215" target="_blank">📅 21:19 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/YN5dSGrgn0AFOgOhTqYhjotqu1Shrj9vDoyrF1FbTrIcMiygQk4FA9R-Gz5_oxmnXD_QJjvuKK9q3NjqcLTKw836_PETiz7awpsvsYv2jRjPBezkZFiuKcKcvycZzJt43y2wvwKSdm4V8tV84-PUpuu5FS9RwtNAMVYAppBd6Nsb6mUWXtXMT2c6ihzS4AAOlOYkB1pWW94gYOFhjz1y4yqpHsX7e6QNdEr6lmRfWkd8vZFZzq297_lxVkkwsy5rVpyarQ7gTTXHATa2KJ-7qebidp5hpYBLYfK6SdR7TlsEkJH9OwFlIDOieE1oLQdOffQ-qrH8a1mI5OlhhEYs3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 01:18:55</div>
<hr>

<div class="tg-post" id="msg-671198">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در پهنه دریایی شرق هرمزگان و سیریک
🔹
بامداد چهارشنبه صدای چندین انفجار از مسافتی دور دست در شهرستان سیریک شنیده شده است.
🔹
به نظر می‌رسد صدای انفجارها مربوط به تبادل آتش و وقوع درگیری‌هایی در پهنه آبی خلیج فارس و دریای عمان و همچنین تنگه هرمز است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/671198" target="_blank">📅 01:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671197">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
معاون استانداری کهگیلویه و بویراحمد: هیچ‌گونه صدای انفجار یا فعالیت پدافندی در شهر یاسوج رخ نداده است
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/akhbarefori/671197" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671196">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b85d1a2c.mp4?token=jvLQedzk8IYRy5wyJLSgjs7k_hmFH6IVbFV7MBa9bXFtODIpHYDL1P-QknszPex5EGEs7gjIKzb0TTrxGXAq215B3aEOjo43USLdP4XZNdtFoQnSeohhEyWM0rOuJHESvY9Vzyc_V3q7uApLiUUx50wbhawe25P6jgcQ55RaPq_eTXBCVa_nEPxM19_-JMpP4qCpLp47KvGIQGOjtPzR-ya-MpMALqIM40P13_g34w7LPNCPNaFZKQaChdUE7AfaBy3As22_BPJVcnxk4Yol9cCNP73UPMo4EVLipmehjKtyoF3BuiKyXc3Pg8dQils8ppjJ_ItkHZAAI6Gw-j32UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b85d1a2c.mp4?token=jvLQedzk8IYRy5wyJLSgjs7k_hmFH6IVbFV7MBa9bXFtODIpHYDL1P-QknszPex5EGEs7gjIKzb0TTrxGXAq215B3aEOjo43USLdP4XZNdtFoQnSeohhEyWM0rOuJHESvY9Vzyc_V3q7uApLiUUx50wbhawe25P6jgcQ55RaPq_eTXBCVa_nEPxM19_-JMpP4qCpLp47KvGIQGOjtPzR-ya-MpMALqIM40P13_g34w7LPNCPNaFZKQaChdUE7AfaBy3As22_BPJVcnxk4Yol9cCNP73UPMo4EVLipmehjKtyoF3BuiKyXc3Pg8dQils8ppjJ_ItkHZAAI6Gw-j32UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه‌های آمریکا در منطقه آماج هدف حملات پهپادی ارتش
روابط عمومی ارتش:
🔹
در مرحله هفتم عملیات صاعقه و در ادامه حملات کوبنده پهپادی ارتش جمهوری اسلامی ایران علیه پایگاه‌های آمریکا در منطقه، ساعتی قبل، محل استقرار جنگنده های اف ۱۸، ساختمان اسکان و سوله بزرگ تجهیزات ارتش تروریستی آمریکا در پایگاه الازرق اردن، هدف حملات پهپادهای انهدامی قرار گرفت.
🔹
ارتش جمهوری اسلامی ایران، تاکنون ۶ مرحله عملیات پهپادی علیه پایگاه‌ها و مراکز ارتش تروریستی آمریکا در منطقه انجام داده و این عملیات تا رسیدن به پیروزی نهایی استمرار خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/671196" target="_blank">📅 01:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dko_dgPE0uOaa_0OCNUSzNCRpoN_v5_RJj52KMMfc0qa6LmRCKriU82HoFEUZesGnEOlSY9lEJ35p28ywVK8gayMqTFMXZI6vFdIGsltR-1lrlS1DH7jsN3EqDYQZp4-lwsTwVbjfFFbfkuuLv5szagdFWEajU1DEKQsYnMlbuKuqyWLwZgNIk2gSlq0JzOy1qdPxRBXinwTohvPLO5tCzv1FpF-tE4JZ1SCkPXY-v7J1n6LOz9ggzXvq8oJ-6bGVXfl4vypd5vkIIgwwElzkXV49Bc1Vq2LM2wxf3UDAg7eKJdwcpIeVBG8dCmJEclioEj-PWPHZbRKN940PY58Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا به بهانه صعود اسپانیا به فینال جام جهانی ٢٠٢۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/671195" target="_blank">📅 00:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671194">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
صدای انفجار در بمپور و چابهار
🔹
دقایقی پیش مردم در بمپور و چابهار صدای چند انفجار شنیدند. هنوز محل دقیق این انفجارها مشخص نیست و مسئولان استان در این خصوص اظهارنظر نکرده‌اند. اخبار تکمیلی متعاقبا اعلام می‌شود.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/671194" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
صدای یک انفجار دیگر در بندرعباس شنیده شد
🔹
چند دقیقه قبل نقطه‌ای دیگر در بندرعباس مورد اصابت قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/671193" target="_blank">📅 00:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671192">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a8203838b.mp4?token=nYlS7y2O1M8dZ1qFFrJrDah5l_lHZHmMrlseBmcbzCMhglEQ_lIFZ23IAzgqoWVOo5m5rcrtjQ4HblWJSdXE_f8jDPv21WL7DfGkvE2oALjRe9NRopbxIUD8pRJTzqp6CGLEQ0x5hEe1ORejzo_HOzRrHdqp-nTktvIIYneWPk_KKsrhXwuUgiflK1-xGqN9ceEhm72O62X60CrD0jvfAForxI-Gd70wAp239IKI0eiXiXjrejvTwJlZjlPPBEiixLSwE5wFJXlYUf_immOhmJ8QpLyWYgbK5RygCgZ1XwSESH-SCz-JEHpCq5iwaQKpYMtsSfmLcsFtFVH6RrV67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a8203838b.mp4?token=nYlS7y2O1M8dZ1qFFrJrDah5l_lHZHmMrlseBmcbzCMhglEQ_lIFZ23IAzgqoWVOo5m5rcrtjQ4HblWJSdXE_f8jDPv21WL7DfGkvE2oALjRe9NRopbxIUD8pRJTzqp6CGLEQ0x5hEe1ORejzo_HOzRrHdqp-nTktvIIYneWPk_KKsrhXwuUgiflK1-xGqN9ceEhm72O62X60CrD0jvfAForxI-Gd70wAp239IKI0eiXiXjrejvTwJlZjlPPBEiixLSwE5wFJXlYUf_immOhmJ8QpLyWYgbK5RygCgZ1XwSESH-SCz-JEHpCq5iwaQKpYMtsSfmLcsFtFVH6RrV67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار طلایی‌نیک: خون‌خواهی رهبر شهید به فراموشی سپرده نخواهد شد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/671192" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ایرنا: شنیده شدن صدای انفجار در جزیره هنگام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/671191" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شد
🔹
بررسی‌های میدانی نشان می‌دهد که لحظاتی پیش پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شده است. تاکنون اظهار نظر رسمی در این زمینه صورت نگرفته است./ مهر
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/671190" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
اصابت پرتابه‌های دشمن آمریکایی به نقاطی در استان هزمرگان
🔹
اصابت پرتابه دشمن آمریکایی در قشم: در ساعت ۱۲:۱۰ نقطه ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
اصابت پرتابه دشمن آمریکایی در بندرعباس: در ساعت ۱۲:۰۵ نقطه‌ای در بندرعباس مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
اصابت پرتابه دشمن آمریکایی در هنگام: در ساعت ۲۴ درست در نیمه‌شب، نقطه‌ای در جزیره هنگام مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
بنا بر اعلام استانداری هرمزگان، در حملات جدید آمریکا به برخی نقاط استان هرمزگان هیچ مصدوم غیر‌نظامی یا خسارت به زیر‌ساخت‌های مسکونی و تجاری گزارش نشده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/671189" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
خروج نظامیان آمریکایی از عراق تا پایان ماه سپتامبر
🔹
«پیت هگزث» وزیر جنگ آمریکا شامگاه سه‌شنبه در دیدار با «علی الزیدی» نخست‌وزیر عراق گفت که تا تاریخ ۳۰ سپتامبر ۲۰۲۶، تمام نظامیان آمریکایی از عراق خارج خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/671188" target="_blank">📅 00:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
صدای انفجار در بمپور و چابهار
🔹
دقایقی پیش مردم در بمپور و چابهار صدای چند انفجار شنیدند. هنوز محل دقیق این انفجارها مشخص نیست و مسئولان استان در این خصوص اظهارنظر نکرده‌اند. اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/671187" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671186">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شبکه کان: نتانیاهو، قصد دارد در روزهای آینده به ایالات متحده سفر کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/671186" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671185">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz-pxZ8-hlstEExd-szart5slYTHHzKPoUaXthJts8NermZwYiyrpXA_4c7-yjy2WGWxTORkxowJ5UoUEpBBBsZrGOfABFAXR2iq_lRg5IHke9zZFzfqlE3SEphbxvcj2Ds-9mNugg_MwG5RLz6zELVryk0mP5BEOthSnYlKMy399CgmEo4RV6F5N3zx7HHDKE-LmTRGQBvw8FsHhJ947cc_DN-JjehvJ2ow84U_U8jPeqARlJPbQR5LySLKHsEgouWFMfEwu4m4hbAfKKKQyAGBc46TVIe0VuRXMDmbpj-B5ObtFzowiziT4y7XyLHQm0JysvLKoN9UIhnVgLZBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل دوم اسپانیا به فرانسه توسط پدرو پورو
🇪🇸
2️⃣
🏆
0️⃣
🇫🇷
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/671185" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671184">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmVkNU-l47LjmLejp5kJQTSC4KuvX5icGs_VDIAfp6AgwqUVeHwuPeX_wyqA6X7_H7pk5FswFnjMwyb-dMp0leDb_pd5lEuBKBVyvcuNP5c2gHJG2xhpMve6yWI_yekSRZIKzXuTOwwhDsdEnau3juHfuzDfD_JXRYe97QlpsfPTTe8gPWH1QGZhhttU_yhXq1lNIzcKSbiN6SHGLagXXij8s-3DxH03pMHjFXsfk_3t0UFeWgG4ADxwoNKXZvtUBZmMoNhY_AEgxV7rdVvZIXG_Dx7wFEStIDpgiAep6TIw9fI_7vKAG0OLukPKmXcZi17PxV6ZnoC4pP5FrDOQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: حمله به پست سرمحیط‌بانی در استان هرمزگان، جدیدترین نمونه از جنایت جنگی آمريکا علیه کیان ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/671184" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671183">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ee44b24a.mp4?token=EM-T94YlzqA7ylzY8Lcw1-3K_R-itu9uY0KKafRxJgecWadskj3Oc8p0sp8xdUuh8g4FOLV79d29VGO_239_tAeUl29LRb7xBZ3WC291PW2R1j12fDfLhzeGDT19ED6y_YSdspNRK2J45W6RVXmcJKZu7k4ndE0K_W7fRWBnGm0u-nezazhoVNg06A5YE5UY4LyhVAhzDXOYpf0UeoCsDLbrrkneRfUDIv2r4HCV6lvHKV7vZvGcuTaOOt7gtgEw4RqXhVsNASqX_9nbuhPY4EdoAmoG-pkFyrtWVCAsd6p9LsGL9QizGJoOtWtmIz0b6bw0k-CJ4uei_UlgeMuGQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ee44b24a.mp4?token=EM-T94YlzqA7ylzY8Lcw1-3K_R-itu9uY0KKafRxJgecWadskj3Oc8p0sp8xdUuh8g4FOLV79d29VGO_239_tAeUl29LRb7xBZ3WC291PW2R1j12fDfLhzeGDT19ED6y_YSdspNRK2J45W6RVXmcJKZu7k4ndE0K_W7fRWBnGm0u-nezazhoVNg06A5YE5UY4LyhVAhzDXOYpf0UeoCsDLbrrkneRfUDIv2r4HCV6lvHKV7vZvGcuTaOOt7gtgEw4RqXhVsNASqX_9nbuhPY4EdoAmoG-pkFyrtWVCAsd6p9LsGL9QizGJoOtWtmIz0b6bw0k-CJ4uei_UlgeMuGQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عمو پورنگ وقتی اینارو گفت نمی‌دونست مادرش این برنامه رو هیچوقت نمیبینه...
❤️‍🩹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/671183" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671182">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تکذیب شایعات درباره وقوع انفجار در شهرهای استان خوزستان
🔹
در پی انتشار برخی اخبار و شایعات در فضای مجازی، اعلام می‌شود به‌جز چند انفجار در اهواز که پیش‌تر گزارش آن منتشر شده است، تاکنون هیچ گزارش رسمی مبنی بر وقوع انفجار در سایر شهرهای استان خوزستان وجود ندارد و این ادعاها تکذیب می‌شود./ ایرنا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/671182" target="_blank">📅 00:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671181">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ستاد استهلال دفتر مقام معظم رهبری: چهارشنبه آخرین روز محرم الاحرام و پنجشنبه ۲۵ تیرماه  آغاز ماه صفر ۱۴۴۸ ﻫ‌.ق خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/671181" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671180">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
اصابت پرتابه دشمن آمریکایی در قشم
🔹
دقیقه ۱۰ بامداد چهارشنبه نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/671180" target="_blank">📅 00:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671179">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0099aa6ab7.mp4?token=r2roTCG1Mt-J6-YZ0agZgr_O4lxWHwc-sPX_7COW8wzfAnvBgs99qCMi1PcI6A0p5stUobGE0nKM_IeJSKulMumY0eqrn1eTlv7VCbh7i5cR62F_EvSm6XW_ssGMox6i5R97lAkaDBqRnu_XXQHCuwwEuiOIqLmWZL3LBMIEsI6UVjNpbHUQ_a4hM0pBA_8YmxQM8ifB1IYaGaALQ-GjCKJzFtHJmr-X1VphKFeFwhZMAPNFtBL3HiccH592A1XfOhd_bENlgy-7FXxRS2mhsPlMcIWcOvnib2ltp94aH9Dv8od07fRjySFTGXhLwb3gB9ZNq8WDw2ZJjWFRKmh08b1FxYfoHUOcA3zJYwuxLRB7W2OoBOkOpkNFNMUDd7HKvb3bHRv9zW1aXPdwvkxxqPSrqspWLmjOtVTuz0nalAIOV4Dw43QctTLi-tETXdUS_ejbswr1YtXolbZWZh6lKlNAtJ5XOl57hMNcGTjzqT_hhFsPtQI0PLiN3fgmIT5ri_cs0ctWVI88p-eLLSn6LfFYsDQiq57-ODznjxvGBzTHkXteMHhxXm04_fACiswHvbldsuC55VUobWoKDIHAE2dr2-gDKO9MwhGQMPOvAYC3aKNCt5u6W3NiBSkdzEW3vLcWL0fz24G4HwSXYDKMrGWch42BmiQivPAGxOX8EeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0099aa6ab7.mp4?token=r2roTCG1Mt-J6-YZ0agZgr_O4lxWHwc-sPX_7COW8wzfAnvBgs99qCMi1PcI6A0p5stUobGE0nKM_IeJSKulMumY0eqrn1eTlv7VCbh7i5cR62F_EvSm6XW_ssGMox6i5R97lAkaDBqRnu_XXQHCuwwEuiOIqLmWZL3LBMIEsI6UVjNpbHUQ_a4hM0pBA_8YmxQM8ifB1IYaGaALQ-GjCKJzFtHJmr-X1VphKFeFwhZMAPNFtBL3HiccH592A1XfOhd_bENlgy-7FXxRS2mhsPlMcIWcOvnib2ltp94aH9Dv8od07fRjySFTGXhLwb3gB9ZNq8WDw2ZJjWFRKmh08b1FxYfoHUOcA3zJYwuxLRB7W2OoBOkOpkNFNMUDd7HKvb3bHRv9zW1aXPdwvkxxqPSrqspWLmjOtVTuz0nalAIOV4Dw43QctTLi-tETXdUS_ejbswr1YtXolbZWZh6lKlNAtJ5XOl57hMNcGTjzqT_hhFsPtQI0PLiN3fgmIT5ri_cs0ctWVI88p-eLLSn6LfFYsDQiq57-ODznjxvGBzTHkXteMHhxXm04_fACiswHvbldsuC55VUobWoKDIHAE2dr2-gDKO9MwhGQMPOvAYC3aKNCt5u6W3NiBSkdzEW3vLcWL0fz24G4HwSXYDKMrGWch42BmiQivPAGxOX8EeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راننده‌ای که کامیونش را وقف برپایی موکب رهبر شهید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671179" target="_blank">📅 00:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671178">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزارت خارجه: دیگر چیزی تحت عنوان تفاهم‌نامه اسلام‌آباد وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/671178" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671177">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک برای خرید سمعک جوان معلول
🔸
بیمار نیازمند حمایت جوانی ۲۰ساله است کم شنوا از خانواده نیازمند واهل یک روستای محروم منتظر مهربانی شما عزیزان می باشد
🔸
هزینه خرید سمعک ۱۰۰ میلیون  میباشد امیدوارم با کمک شما عزیزان شنوایی وصدای زندگی به این جوان هدیه دهیم‌.
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید.
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در تنها در کانال تلگرام خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/671177" target="_blank">📅 00:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671176">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMZ59aXoY8gVJeDou6pJUvqIwr0WEq62r5hGQWgG1nTXTvmhVetsjlWv8nq-NOZR873JZkfRbmlkE10v4zndPLtIWd3_7xhggmGBg4_ahhlQB61VQwccttB82R3EusuRAQIlEE1K6jCvaigZpl148Hi-yeR7F3QoqXdWh-Q3cNdXiioIYPBOfqaMtTUcC8JvVr30HejJjztzE7iTNdCqdSPP4wmsvOq9FtLXU-_WkZae4fwgTYddVhAfztnKAxNIq7BxJagcWxyim70Vb-2LcNgs3on2Sw0t7ao9QXvo1o77Yfzqml-mZuqQW2Jxbc-TFMErHZOUCRAffmniB5OcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/671176" target="_blank">📅 00:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671175">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e812ee880.mp4?token=Ffc9lkwBuVuJLaRwe-2xGXzxwk_wln_w_WOhcDDKFOCN9UMA6QmN9tNYD1zo4mfGTXQl-Mu8Jg9QVHJA_6N6gIBkRfvaTtdsVvjaRyVopyPZ18ALDfMUZkb9OyzQpm85yGaOSR3o6vw5RkjGg913MMmUokFfCJVpArwaXkwDdCBm18HLCRrRTC8u3TY27mhuEUXcRA9ZE3nWmhp6W8RBm9MhRXJy01E3sQlgJ8nQkJ4kfxqryHpZsjBvNp4R1M7RSBtRvMbFfoalQm5iuYtXeB3Zo4MH8tchO5OZdh5ps5qLisOpto24S8-qWBmZK8C1331nFyu32ygZcIXAtl-BbRiSFVKru3O2AoNXvCenxzjiNVS47ZOHbo3Jam6COHEqa-eH4kBWLzPm5cVHftbpPnd6NiGyTT5sFxML-NUzZDbpQifx5igvkOPXe6H6km_9CidZUw1mBFEhWZeEQjXa2c7QdWWnWallAgAs0xPlX9AfAr4TnWbQqb60qQdVs7OiT1Jm25m9zVX7XhP3UPv1TyK-HmmoVYsmx0JtKxWJC_TxsjYVfrGjX287sThR3TywU8WXZQBZP3KQe8zFZphAra93PvEjti1x8Rrr62Jo17s4-hn1_Xnir1AMqhbPhQmZIsNYTQlGn1DhUKoBFCuF0Vy2qj8yq57y7YRp6YJ5zG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e812ee880.mp4?token=Ffc9lkwBuVuJLaRwe-2xGXzxwk_wln_w_WOhcDDKFOCN9UMA6QmN9tNYD1zo4mfGTXQl-Mu8Jg9QVHJA_6N6gIBkRfvaTtdsVvjaRyVopyPZ18ALDfMUZkb9OyzQpm85yGaOSR3o6vw5RkjGg913MMmUokFfCJVpArwaXkwDdCBm18HLCRrRTC8u3TY27mhuEUXcRA9ZE3nWmhp6W8RBm9MhRXJy01E3sQlgJ8nQkJ4kfxqryHpZsjBvNp4R1M7RSBtRvMbFfoalQm5iuYtXeB3Zo4MH8tchO5OZdh5ps5qLisOpto24S8-qWBmZK8C1331nFyu32ygZcIXAtl-BbRiSFVKru3O2AoNXvCenxzjiNVS47ZOHbo3Jam6COHEqa-eH4kBWLzPm5cVHftbpPnd6NiGyTT5sFxML-NUzZDbpQifx5igvkOPXe6H6km_9CidZUw1mBFEhWZeEQjXa2c7QdWWnWallAgAs0xPlX9AfAr4TnWbQqb60qQdVs7OiT1Jm25m9zVX7XhP3UPv1TyK-HmmoVYsmx0JtKxWJC_TxsjYVfrGjX287sThR3TywU8WXZQBZP3KQe8zFZphAra93PvEjti1x8Rrr62Jo17s4-hn1_Xnir1AMqhbPhQmZIsNYTQlGn1DhUKoBFCuF0Vy2qj8yq57y7YRp6YJ5zG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، تحلیلگر حوزهٔ مقاومت: نباید بگذاریم بمباران هیچ نقطه‌ای از ایران برای دشمن عادی شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/671175" target="_blank">📅 23:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671174">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
شبکه کان: نتانیاهو، قصد دارد در روزهای آینده به ایالات متحده سفر کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/671174" target="_blank">📅 23:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671173">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزارت خارجه: دیگر چیزی تحت عنوان تفاهم‌نامه اسلام‌آباد وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/671173" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671172">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54e28773c.mp4?token=EKS5V4QpFqBZMJpprEvRZXCh4y6irn4aDHwdHKYN5QxAzdhBr5MCoFlNmln4xE_nNUxJXVUSUmJThTVimismxjbFKGpPU03NymQQj1T7HjYmFvuzN-4gKc0KELOarzluSHcnQs_r9rNHFJscvDRKdORnyJzs1z6IAdKNR74xcre2FhXDDnBMAuTrAZZh-Ppp8re9hvAjqKlgLIp2i9Xg68z8ymvBsDb_icyu8NIcMadqyPB8m4jklGk0Sltf81nG0k7V15RAH0cVzp3rAWvwCItYRdyx_Z8Uh-zcyB2XBzNYgNVkcTqpCf1y3klOhpplBTxxni9FQsDOnGhsXXiJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54e28773c.mp4?token=EKS5V4QpFqBZMJpprEvRZXCh4y6irn4aDHwdHKYN5QxAzdhBr5MCoFlNmln4xE_nNUxJXVUSUmJThTVimismxjbFKGpPU03NymQQj1T7HjYmFvuzN-4gKc0KELOarzluSHcnQs_r9rNHFJscvDRKdORnyJzs1z6IAdKNR74xcre2FhXDDnBMAuTrAZZh-Ppp8re9hvAjqKlgLIp2i9Xg68z8ymvBsDb_icyu8NIcMadqyPB8m4jklGk0Sltf81nG0k7V15RAH0cVzp3rAWvwCItYRdyx_Z8Uh-zcyB2XBzNYgNVkcTqpCf1y3klOhpplBTxxni9FQsDOnGhsXXiJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم اسپانیا به فرانسه توسط پدرو پورو
🇪🇸
2️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/671172" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671171">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBhoHUHZjj7g8LEIgd0kFyjRBxfkNnTB8AICaopLFmJ5YEjBLh6yzTFl3tNhP30YFIwPq9yzWM3E_VzMdFdVJaBMrCJSV4EoCmE3IlGgiuom9K3g94iJrB1w5Pjljjj6m8BmAEAZKcblHs_RFnlvxK-mOJnxaJc1SjOZlz7ipWUt8CZOkD9RzBVPmFMdzhAkdCeOKX_tpkAWeOE9m0vbgJHAF6tfcE57aje3iK6yRiqgHhJAbVHGLKLnxalEu8s3nOw2H7qUDVT-_XedbVVJzLpXMgrcDEPgC_Uz-PDeCzbQICAM6CquIkozZJr5arCHK3S5sJZ8x7RpPYYPq50tRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انسان خود رأی، هلاک می‌شود
🔹
امام علی (ع) استبداد به رأی را عامل هلاکت و مشورت را راه بهره‌مندی از خرد دیگران می‌دانند. مشورت، که مورد تأکید قرآن و عقل است، با تجمیع اندیشه‌ها خطا را به حداقل رسانده و نقاط تاریک تصمیمات را روشن می‌کند. خردمند کسی است که…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/671171" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671170">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای سنتکام: محاصره دریایی آمریکا علیه ایران وارد مرحله اجرا شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/671170" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671169">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
شنیده شدن ۶ انفجار در قشم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/671169" target="_blank">📅 23:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671168">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تصاویر شلیک پهپادها و موشک‌های خیبرشکن و ذوالفقار در موج سوم عملیات نصر۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/671168" target="_blank">📅 23:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671167">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای سنتکام: محاصره دریایی آمریکا علیه ایران وارد مرحله اجرا شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/671167" target="_blank">📅 23:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671166">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f525d7e01.mp4?token=Ztwnibb2l2gFHJiE1gwHFNtYJMaTyQ6y-oWCkkj--7rhG0kqS3tBg30r8DC7JCIquWFRzwGrFhwaRQ-RoWuTDmke57JB9_cjVxq1zboiK_iL8qJ7qcgxtgyDs7FtCfh30OQtHqlICN5XXP8HbKo_3GvNwKbxxBR0bDBR05CqlkKPtHBluXD-SlL6vtCZF04PdLr2w10JSLHeU6GFn59CpfjLIoH-KDXoZugW771848euKKMHyvGU1JkCZOy5cPnP2vDNHaQLtr7Hh6y4uH-6Rkug-ETwNYB_jAxTR2uafpCb7-jRjaW36tZg5SC3duqUVzNNE9bLe9RaKM3yrBTOMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f525d7e01.mp4?token=Ztwnibb2l2gFHJiE1gwHFNtYJMaTyQ6y-oWCkkj--7rhG0kqS3tBg30r8DC7JCIquWFRzwGrFhwaRQ-RoWuTDmke57JB9_cjVxq1zboiK_iL8qJ7qcgxtgyDs7FtCfh30OQtHqlICN5XXP8HbKo_3GvNwKbxxBR0bDBR05CqlkKPtHBluXD-SlL6vtCZF04PdLr2w10JSLHeU6GFn59CpfjLIoH-KDXoZugW771848euKKMHyvGU1JkCZOy5cPnP2vDNHaQLtr7Hh6y4uH-6Rkug-ETwNYB_jAxTR2uafpCb7-jRjaW36tZg5SC3duqUVzNNE9bLe9RaKM3yrBTOMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، تحلیلگر حوزهٔ مقاومت: راه درست شکستن محاصره، حمله به خطوط انتقال نفت به دریای سرخ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/671166" target="_blank">📅 23:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671156">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALEy2COp7euMnLbM8YYEHSLg4Ry9jXQGd7vIdu0C0S4lDWBgtu-SyERsHjAC3u-JioFNmWXgrwzC1l5QHEDGItt9-ehSp8Arh3TgavO5jADPTAOsDgnhjDwKlHNonHEYaZ6EyAIh08yu3kQ7ZrwE3UwbaTOSm0raalzOn2OznLTnGvFLwaBoqr4g9mEWmAY4I3kb5vkuEEnVaI2qoPeO0W0l43T_SAfZu1rvwgkFpzErfpZGb6aZdZKaikrJbiLy1_l4sMTs4mF-GrxeF5vDGkpm5gLB6tqSI_LYObWz_57QQ4YgnXB1onXqKeCV7MjXYO7y88As77TQ09Tepx7N7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSyFRv9lU7BXSSC0tWoLhEQzycA4v9uU2tMBPTI1Txudw7XdTEZE__mV3MVkWvTA_0V5Iu0DRPgB7oXIKchk6vVnFpv65QjL6aKQ12nXbR2LHpGpAAukzY8npYf9VI2myeNa9A6_5xFWcaroaxX0KiSdwfU4VD7r6ENgHXXXDgOCRAMQmEimBR6xRdenAFilk_psvjUcfBcLRsd8CMUi2hPpmEHxwnjDF3Z0HVyqVGqYevSOFu1rr1q8iVD6p_yobz6kryYW5pc0H86FACg8wRB0GE0KCn0kqr8A3vMtZWljcUO8P22yRUt8GS8cTiP_i5z54jLHkiFx1p5xJg7HZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFBTApKc9KnhVgVIxh011b5fjGbt42YC1-Zl_eCfJEmU06qa_-Qk7Y21uVnomg_MR6tStCX_5FBwojIQ6SFfBsaBeP6oiRLOSzMhyqqBa3YRCbs7P4Rmozed5m5MDHAb1YDR0cZYbORwf-q2VxbZ3FbfUQPvH7TJ9pe_ht3R4THsf2iNsXpru-IvQWTp-MJ5QYgkyjizahaFY8s8KJxMcij85c3_bMlfMUWLnOdxb0pVG4UZWOg8LqJdfNSL4O5UrU9KWuzF8mA-TYdKzeGUpIrCVdwOgvJ6PWw24RSTKfMjFiF6Ed6Kc-z2b9lESVar2WGEM4lTikTxqurB9R2Pmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VYJvcP_2Kf7OyPqcPqq4pbkQaWDflzTNQfvl2y-JDGrrzM56Iaz0JLk78q34NEwbHeeG11YRlDXxZOwwbcUA8g9Hrz3nMy-wIznBs98n3xdpyQ7BUHZ97oXZpTkM7K7RzmI47RGILDxvitoVxZ4KU0Q1fzqGcudp5mYPux-eijlFyPfiGrfkXchCBfLlJxVQwQC1AtwheyIymLifDHUXt_HRr9PweGry_V5XpCg7ac93w_z4E2IVVEixePJhvknyHNnx7-txkUalZWcA4Jc0D4ClL594mo_VVOsct_0yl3bw9UXQImDyJ9DV-nzOXEjVWVnm8Y-C6SJfxg3RKgnorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qV20LODvYRxr-Uf3PgeXKf9i4sTQEWiqAUR3MIDExwOgWu6kFj74hdYB_ls2LjThoGkYB1iABPjH_cw17eogz1ZQDpoHDgAOj2dr5RmxxXKGh9DzWosv6662NKTpRV9Pt7Z1MIXFVZ_3rziLVK5bodpJOneXi-QuVzRWA7WGZ_AHdIXw9g6hT97UIdfk4zGnD1nDG5XVaeDhhXrkvlgwgqCJkjbB_zMmqiLNpNUmxBVhw0QoRDfCF0zB3vRnlva2Kn7rDJji5L9kYKQ73NdYUFVsizRiUvoQs6fUVy4xh81S1quOxiGlUEULqmHV94g2M4bxueUTCzbJCjT58RfZ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frVY-vdTyAYKI-FQpPAPxrQJ3YBwp0bhQLLJaBDvv-rztAi1NQWEA52Ld2nOzzXTGYQ-iBF9hIff7fAF2VDPWCIJbHdLWJJ1jERTtwIUebQ5pFxSh5Cgf9gCx39dN9NNwmAF4dcbarUURzPsgjKREb1GPq-UQU8two48xiNQb_89NtAbpQ2m54e3Elf09W0nDgq0K9tkHpBWSGKl7p_mHS9LU4Yz-4qzx8n9An8mC-FVWjBTM8L18Dj6fajcY9xOi3hVYxWTQojW5akiDPupZ4D1NhXDgYmvyj0WJ69dWw8qm5fH_1CQm0rEJ9tpUc9Cfgd6fSXnqKgN_KOdE0YCfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBLWuXSatzMuMdjWtZoVx5Tvv9KLFOBzxuM9MsW3vECxJ5bjN2duRuSz-28JMng4z7rIu-jGm56_zj5_YcUYHpVDuqwa8JEmCmPfxI_Lfa9Zlt4fWLwVAQ5_XUs0oOlduehiPmCI-LoQLmaA75zJcJvyXOzLdOGWUTiDZLj7jHrTdoDQQ5WHuUS7WvCNpBCUT0O0FqLWSeMG6BFea5hG6eikgdsZ7NNGVWrSVnuvgSFvu-apy-6fajIWYWE7jmLEIzuk4zi6bs_hhhoWXiid5-od2sGvPXt-46eTw0TYln5XuSNjA6TRePo5umQay3H1t5N8IJjFnf6EegtsEQZFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqsB2DtvaraWIrzFYEoRkCBQEIuBFAGGbJObBigsdJNV59bgWv9LonqDi5uazfMGR9Kd78GlL64YNvE_XhbWBpp4XmjUwuxvQAMo_aYOn62zG19vXtr2H9Mvw6wzobuCUsvvHSVoljIVz05HuwOSv4_5BdrnC7q8FZJPEE6bb3yD8icboXnuidCg7i1cDXOrnn74TNiyjXUJ7eXuaiDvcrJ_fV7YcaEuf_4iCD7X_MyJyVdCVa8wN_ImJJ-41FEPJ6q7nZUPA-T7NdPjNcH51LvI-vkTrJVJjiLlH6DYd2DqOA-eHMwsr4hk0coD2zFv2OSRBdzUww0XUVdj1HippQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llVdkKnPb333vC8x7SP3SYNG3px3mgwT9b25QzpBk8UiZLPv6UaT9D1-Zvvi_nbtox5fCaRQW9ArLeEP3h6v9beZ6sw8NfL67eYuqajB680h2SwcT-6NvEFZ702Hh9Z-qpEf17x6IWG9HbRMsLr7yZTtD3LXgdb1IGguGSxS9CWmehGPIjJ95vRzkoJLWG1TgfmwlH-i9-hK0exhEGvQBJ00D5z89jtujSa88rdSS6fkTPfxyiMLsidwHfWDn3GwT6f5yUJcwk9HAHsBVi3heFhP0T62f2wDLbxt97FOojZQ2In5duwDMUlvzjftdjw3INzMJIC18BlNTaY4ZmN3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YH6wXOrLSldcieKFU1bBLSXxo7-2bUsjuUBRDE1_TbYLTjCHybE4YxuqWhqUCbqJbP99oNLOfyjpoahBJT2EKuXfeCZSg9ZZfL46y52Wn8TPc1HKkCAJMfQWMRj0ijmZltzh20QBwpAg1mJJHxJLIcbiubDbF--ls1S2jqYQC71O-0tqrZFsvEdCk4W_Y5S4dV2kMTljZsaCBybjkFowM-F1ZUxb-Ife8jIYW_SmB3E046fk3fVMJWxTzLZj4HrTsDmmwzNcVL2l-QE8jjL9FGxC5FY5H2rRbMoP99K8Xp2sHVQeYyLHwZJLIXkZEdFazS71LSBH0tkvhrdDZ-aCHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منتخبی از پیام‌های ارسالی مخاطبان خبرفوری درباره قطعی برق خارج از جدول زمان‌بندی
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/671156" target="_blank">📅 23:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671155">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار مجدد در اهواز شنیده شد
🔹
در قشم هم صدای چند انفجار شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/671155" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671154">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h50hGrKU7esqDEMtSKtnoXHm7aKpmQ000lNjbAVTCK8t5pXIDW5MRoyh7bv0SIeTEOSrE6jUwnaFkAgsw9_X1C4qQ7oIaeSD2C5iopzD4RxVcbY0aerPBaKz_fZPUX21kfp_QIYLW_aHGcHfaS6gp-r3QxUl0n0hcyc9KScu95yY5V7nzFklVskQbiIvddEyWDvFe5dbiNIa0qeCz5jM-4q3ctuGkYBLpmZBT9Y9TaFDAIVUlI6mgTfp5uql4LohtG-LvMmv1xXOXah7bAjYA3hoFmFM3jG0Wb6RJ-JqUu2TtgAZaf1aY-KolxkqEnoNhJVSvMwX6Ygw5kqnbpEp8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا آمریکا می تواند خارک را تصرف کند؟
🔹
حمله به خارک نه از منظر دیپلماسی می تواند مثمر ثمر باشد و نه از منظر میدانی می تواند عملیات پیروزمندانه ای برای آمریکا به حساب بیاید و احتمالا با شکست یانکی ها به پایان برسد.
نظر شما چیست؟ گزارش خبرفوری را بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230409</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/671154" target="_blank">📅 23:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671153">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
اعمال تحریم‌های جدید علیه ایران
🔹
وزارت خزانه‌داری آمریکا همزمان با آغاز دوباره محاصره دریایی ایران، تحریم‌های تازه‌ای را علیه بیش از ۵۰ فرد، نهاد و کشتی به بهانه ارتباط با تهران اعمال کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/671153" target="_blank">📅 23:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671152">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
کوه کلنگ که ترامپ تهدید به حمله به آن کرد، کجاست؟ / تاسیسات مرموز ایران در قلب زاگرس
👇
khabarfoori.com/fa/tiny/news-3230219
🔹
ادعای جنجالی یک رسانه اسرائیلی: عربستان به پیمان ابراهیم پیوست
👇
khabarfoori.com/fa/tiny/news-3230163
🔹
آیا آمریکا می تواند خارک را تصرف کند؟
👇
khabarfoori.com/fa/tiny/news-3230409
🔹
احمدی نژاد علنی شد تا نشان دهد در حصر خانگی نیست
👇
khabarfoori.com/fa/tiny/news-3230311
🔹
سید محمد خاتمی: طرفداران جنگ همان راهی را می‌روند که اسرائیل می‌رود
👇
khabarfoori.com/fa/tiny/news-3230351
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/671152" target="_blank">📅 23:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اصابت پرتابه دشمن آمریکایی در سیریک
استانداری هرمزگان:
🔹
در ساعت ۲۳ نقطه‌ای در حوالی سیریک مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
در حملات جدید آمریکا به حوالی بندرعباس و سیریک هیچ مصدوم  یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/671150" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
تکذیب آسیب به مولدهای برق کیش
مدیرعامل شرکت آب و برق کیش:
🔹
مطالب منتشرشده درباره احتمال آسیب‌دیدگی مولدهای برق ناشی از سوءبرداشت از مباحث یک نشست فنی و داخلی بوده است.
🔹
هم‌اکنون خدمات‌رسانی در حوزه آب و انرژی در جزیره کیش بدون هیچ‌گونه اختلالی و به صورت پایدار در جریان است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671149" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671148">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNJ2yjuqtxD8o3onRv65DulX2hoTJ-WE1fx5NV6U0oGJIb5Cr-TWikZNckU63Q9MiWq0AOMhew90g36aYWKBc6BYjy9QX0eBj1N7-epve9nAaXzDNGZ37MJaeN9RYd-ibjh2FQksVlNIWsXulCZWHI_0GHKEP8gKGcj3WjIKEQtwmqlaO3dKesM2GoDYpRxJkXLDo93KpYT3hltNalWOHmjBs2gNP4d-F103Y8jOyxLv9rcvQVNR67HDA3NVtniLZKeOmPMho0mjkb7O6iY3YC_JlwbecTRcArQH3xxgyg431ntGBb6pPoYTnHlYtcPSXfWzJZy2OA1nlZvIco8NDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛞
وقت تعویض لاستیکت نرسیده؟ یا فقط داری ریسک می‌کنی؟
شاید فکر کنی هنوز لاستیکت چند ماه دیگه هم کار می‌کنه...
💡
⚠️
یک ترمز ناگهانی، یک جاده خیس یا یک پیچ ساده، می‌تونه تفاوت بین یک توقف ایمن و یک حادثه رو مشخص کنه.
⚠️
❓
چرا وقتی می‌تونی با هزینه‌ای منطقی، امنیت خودت و خانوادت رو تضمین کنی، ریسک کنی؟
🔴
لاستیک‌های اصل کویر تایر
🔴
سایزهای ۱۶ تا ۱۸
🔴
۵ سال گارانتی
🔴
قیمت رقابتی و مناسب
🔴
خرید حضوری یا ارسال سریع با پیک
📍
تهران، بازار سرچشمه، پاساژ رنگ
📞
فروش: توکلی
09122386439
📱
اینستاگرام:
https://www.instagram.com/youtabnatanz?igsh=b2YwN2E1Z3FicmQ1
📱
کانال تلگرام:
@youtabtire
امروز لاستیکت رو عوض کن؛ چون امنیت، چیزی نیست که بشه به فردا موکولش کرد
.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/671148" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671147">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
آمریکا دور دیگری از حملات به ایران را اعلام کرد
🔹
فرماندهی مرکزی نیروهای آمریکایی موسوم به سنتکام اعلام کرد که ارتش این کشور دور دیگر از تجاوز و حملات به خاک ایران را آغاز کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/671147" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671146">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
دقایقی پیش؛ شنیده شدن صدای ۶ انفجار در غرب بندرعباس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/671146" target="_blank">📅 23:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbioUxmp5tyse7N9-2RP3YqkFErIMwX2hxcG94BvKIwGVQa2lHD513HxDMzga7HjRXbpvJ7p25bcLnE3Kv52m-fCOOJioiwCOUtN5qqBuP5k2tko5tZvtaZqN801kT5CJtGzckYTPK_2Eysyp8QYoRMLDSjvhWTCAnTASo4_tkoX2m1JI_Iu11vDNiSxEMgX_X2MCG6MATfiO4zk3azvTFz6NZP8a_y0kcy3dA_dg3TY5ZfCfYy5lyRW6MdwLq-J7MXzNSiXMrHf49bUJqqxmVUOjkZsRvXTUZrGnetAuXV-P9_Annn8VK8XAEWNQmk3lo-z-9WJQ9xOgcP10lzZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران بزرگ‌ترین حمله به بحرین در طول جنگ را با بیش از ۳۰ موشک علیه دارایی‌های ایالات متحده آغاز کرده است، از جمله موشک خرمشهر حامل کلاهک تسلیحات خوشه‌ای
🔹
انفجارهای مداوم و سنگین دقایقی پیش در سراسر بحرین گزارش شده است، با ساکنان که از لرزش شیشه‌ها خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/671145" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب.pdf</div>
  <div class="tg-doc-extra">10.4 MB</div>
</div>
<a href="https://t.me/akhbarefori/671144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تاریخ مستطاب آمریکا؛ روایتی متفاوت به زبان طنز از تاریخ یک ابرقدرت
🔹
تاریخ مستطاب آمریکا نوشته دکتر محمدصادق کوشکی، با زبانی طنزآمیز و نگاهی انتقادی، روایت رسمی تاریخ آمریکا را به چالش می‌کشد. این اثر، همراه با کاریکاتورهای مازیار بیژنی و بهره‌گیری از نظر…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/671144" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671142">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-X9jPTBRu5AkSIwubytgzyt3YEbrTIK3Lh4E8dRgpEQNb_Jt2PHMOLKBG-SkziLrHiUu0OR46woWNQZBRapnbCH6PDoi9xqMf04wpLw9Nf5tta9UuFAd7Q2FSd5HknhRsvCrdijU23FJCLi5laaD6RQ87-bWo9rBJWL89LQmD7HGq-UKmawno3C5CfZUy5XgKmzQdWZ2yosJhpL5F64V2H2MVdGQgyQkc8dQBJ84qNqt6vNpHM-_s3JmxGVeETfCV46FCZR4Vo8NybMjs2rid99MHT_BLN5276DkSOUyBrbye5KbJV_rBXBDxqoyr2UQ2rK93y4VmLJeEp55Q0naQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tynl5DyIIcfawj3TQHNR-BfjdsDMXr42s1qW8ixkb8rhDFb_5iUUSz0WXtalrDIOnk2vb65NKjWcYcXQ_eFdJf-CF0vqPZYCDmezSh9ovawFQ3IXeokhv_YKAQ5LrAqW_KX-9KjuvNJoIuEMVBa4k1I6_aI2KJslQFq5m3d466j5NI90DDvKjYh8Iwxx-NjWyzBV7JdrevicTzEdzESjZP5MQWU01aOmXbgl_aEA4AiH45Ni58fm4yHuwv0wlVHfXnk9VWbd9Huc-JQfV5hSbuyz6EZMA-5tEiHyS97oCwMZ74vXKN-1Mhn17zaxKhEYrqO-G0DMdKvIZJplVEsGbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کتابی که نگاه بسیاری را در جهان درباره زندگی برای همیشه عوض کرد
🔹
«شازده کوچولو» فقط یک داستان کودکانه نیست؛ سفری شاعرانه به دنیای عشق، دوستی، تنهایی و معنای واقعی زندگی است. آنتوان دوسنت‌اگزوپری با زبانی ساده؛ اما عمیق، یادمان می‌آورد که آدم‌بزرگ‌ها چگونه…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/671142" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac602c29f.mp4?token=VAJo3LTCzIEIFfu5F_fO5cPSYgz6pY7H-_Et6y8tzzwkdF3kBa5VF77EWWLF3csX6XmxE2ONfnAc6lUTfqpMcmahdHGAKfWCY_V_8TKWMWOhNPkwdAI4RaNyL0IhkFGShiMkWEIzEZNDulScHHUhdUHbt4Mz1Vqf1y0f02RWlwH_UAtUuWfCCYrCRjpOFOPVAIYqOyDiztWCxxVg-W6jCCzI2vBnqsVlH31FDezpoxsvaO-aCTVxes7pLjxKvRNw7OeNDAIFkPUQHNcYjnXI47DP6yb6Ym2O13zT8-O_FwCdDw5eZnzFVDj2qOcmNlGhujEZKzeF6DHRjHYJrhyZwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac602c29f.mp4?token=VAJo3LTCzIEIFfu5F_fO5cPSYgz6pY7H-_Et6y8tzzwkdF3kBa5VF77EWWLF3csX6XmxE2ONfnAc6lUTfqpMcmahdHGAKfWCY_V_8TKWMWOhNPkwdAI4RaNyL0IhkFGShiMkWEIzEZNDulScHHUhdUHbt4Mz1Vqf1y0f02RWlwH_UAtUuWfCCYrCRjpOFOPVAIYqOyDiztWCxxVg-W6jCCzI2vBnqsVlH31FDezpoxsvaO-aCTVxes7pLjxKvRNw7OeNDAIFkPUQHNcYjnXI47DP6yb6Ym2O13zT8-O_FwCdDw5eZnzFVDj2qOcmNlGhujEZKzeF6DHRjHYJrhyZwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اسپانیا به فرانسه توسط اویارزابال
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/671141" target="_blank">📅 22:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2HAMQKjNvJ066XnKY1wQygvgmmAK6SpcCgQV_ZR3WgXZykJC1JAxnRy6qK2os7bMn8wIpuUC9ftGz2loZCvcXhc5n3JPQUQrrekYHkYg8eSuw9Ovya_Wh0UKBWdCNiQtPJR60fjB5o4Z7ZonJsGUYO4_h-tIbwMcgs7dIQleKVTldqqFTNHMH_XgNqCHnaKfiLt3qnPgh5iIwQ6EhFs8UJs9xWFqM0d3yfXVKLeupRIoBbZAR8bQ-7gm95VT52nbuG07Sv6iNkwAR30yVYpy1t_Gt_8rqxHbuZuXhTKH9Zql9MBoKwrlMH-sMjcXHZeGv8klbdl4DJ0X1pnAMQXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا «آنگ سان سوچی» مُرده است؟ | چهار سال است کسی او را ندیده |‌ راز ناپدید شدن رهبر سابق میانمار
🔹
بیش از سه سال است که آنگ سان سوچی، رهبر سابق میانمار و برنده جایزه صلح نوبل، در انظار عمومی دیده نشده است؛ موضوعی که اکنون به گمانه‌زنی‌های جدی درباره وضعیت سلامتی، محل نگهداری و حتی زنده بودن او دامن زده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230365</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/671140" target="_blank">📅 22:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d35debec.mp4?token=RxCpVLWCcrfFynGLtyoHLGSVUVsq_u8bnRpkyrjIztO6MFuxuUfJtR47mHfHaVaVdSd_yx9ok2r4thZW0Hv069Kce_OTangVYJ-Utf8eW1vs5BAdA6NLMFqPhy7Ft1Jk4oM_rp98V2Fev3XqkGX16sKomM3OJcPEtLrd6mLUyp7ff1C9jwNYWS8H6jrVHoOasOxDlxkOCXMS2XfyN3R6Owg5yyT093HtbbN4q7FsbTTDyKDmBXdb7_Pajk7l4cTrofeXYgxRMbvwXq5XLJ-1QTzx42RI5J2WzWysYUnzzvo5PEE2NSXuzXGYIoLV3Q4ah3df663mZtMAX99_4Uit0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d35debec.mp4?token=RxCpVLWCcrfFynGLtyoHLGSVUVsq_u8bnRpkyrjIztO6MFuxuUfJtR47mHfHaVaVdSd_yx9ok2r4thZW0Hv069Kce_OTangVYJ-Utf8eW1vs5BAdA6NLMFqPhy7Ft1Jk4oM_rp98V2Fev3XqkGX16sKomM3OJcPEtLrd6mLUyp7ff1C9jwNYWS8H6jrVHoOasOxDlxkOCXMS2XfyN3R6Owg5yyT093HtbbN4q7FsbTTDyKDmBXdb7_Pajk7l4cTrofeXYgxRMbvwXq5XLJ-1QTzx42RI5J2WzWysYUnzzvo5PEE2NSXuzXGYIoLV3Q4ah3df663mZtMAX99_4Uit0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت پهپاد آرش ارتش به صنایع معامیر قطب آلومینیوم بحرین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/671139" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcrZT3Ws-KOqDgVUH4h1jEDeAhZeN2N4Lx58xOGa_pvwOflW3b64o98RFlV35lNzaHiHrF4kEyUFz9yus7RNmyQjg9I2iZs5BdIGVPNIfsxowvNS4e2CN7aQ_jaKwUYPD_ahoPAXtR3pp9F5YChqeM3Z5c4HCFh-dW8F0Itag0fCGNsKINhqxnvrSfO-VZpiuL2SdCTWEYv0fl7-a9TPyjCwhjJ0otkptgx8DMlr8KV7rx-xrwDXSmk35kpUzD08oyD8mN-iXeaUAuqPJmcilF-qMy4DKWaDQVjXLw13MuIE_dR7VS6-cZ6e1qOxvLvu28X7hoPY4T7Eds-UBAVn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقاومت عراق: اگر جنگی علیه ایران آغاز شود، مشارکت نیروهای مقاومت فوری و قاطع خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/671138" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671137">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
منابع غربی: تاکنون به طور تخمینی صدای ۳٠ تا ۶٠ انفجار در بحرین شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/671137" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671136">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1Qhy1rDLN416rfOBPbOmhwBq8SEmfLQK38smMPmVIeJ1H9_AYj2A0Td0h0D1ZPSQyfX-j8MuOuWiUWR145pzxGHYqe9i8yEiOiaedVUYxipFtYrr5fiiGT1DlORFzn8t6uLIGm1JTOPX1BAwa5KnhGmzWBFV33an3Ng5mpTKltpPbTAcQab8Gx2ybX1OM9g4gQM2rAHk75kDYiVYoqLRocdDHBfSFIJ536CbhaCX5ItdpmxSIg4G_WESNSNNxqAoe_iFoE-vdguHK_Efh6jdT8A6ynlx3o0Aa8AKhVIBsuJ6wx_Q2Eszpvr-7Je4LrX1l8aImN8Zgsx6CL02FjQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: آمریکا در حال تدارک حمله زمینی بوسیله یک رژیم عربی است، ایران به ارامی برای جنگ بزرگ تدارک دیده است، حمله انجام شود این کشور عربی به پایان میرسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/671136" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5lHZ90LLGEzJx2sHj1dFqahoOG6szaNfUkR__k1OO-4gLjjM0bT0l4KeuH4YpxPx_WoDjcKG-3Oswa7PMwidVbHiG_HksJMjSxy88vf8EQtaEU7CK3OPljaiRM_0vPhpKq6cLjRl4TBPC51MXH4FcU--6NL6E4ZPHN9CnhZbttyZg05WMOtmc_JJByCAnDM6kYuK3zhfXOjHoHdwZVfAg2MyPZSf12ozRGDgXUGv1EfgOJOYci3-BhMcAxhou1P0V4_bxpMNawsPIwxSetzl6jnvXbJspBdh8pl2wlwEdWRlxIxA-nY5bGSn-OkeUfc0z-2oKD-GgBteswSvxue4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نیرو فردا به وزارت صمت می‌رود
🔹
عباس علی‌آبادی، وزیر نیرو، فردا در نشستی مشترک با وزیر صنعت، معدن و تجارت، آخرین وضعیت تأمین برق صنایع و راهکارهای عبور از ناترازی انرژی در بخش تولید را بررسی خواهد کرد.
🔹
علی‌آبادی که پیش‌تر وزیر صنعت، معدن و تجارت بوده و سال‌ها مدیریت یکی از بزرگ‌ترین مجموعه‌های صنعتی کشور را بر عهده داشته است، از ابتدای حضور در وزارت نیرو، تأمین برق پایدار صنایع را در اولویت قرار داده و با وجود محدودیت‌های شبکه، برای افزایش سهم برق بخش تولید تلاش کرده است.
🔹
این رویکرد به گواه گزارش مرکز پژوهش‌های مجلس نیز در عملکرد دولت پزشکیان قابل مشاهده است؛ به‌گونه‌ای که روند تأمین برق صنایع، به‌ویژه در دوره‌های اوج مصرف، نسبت به گذشته بهبود یافته است.
🔹
حضور فردای وزیر نیرو در وزارت صمت نیز در ادامه همین رویکرد ارزیابی می‌شود؛ اقدامی که نشان‌دهنده عزم وزارت نیرو برای تعامل نزدیک‌تر با بخش تولید و یافتن راهکارهای عملی به‌منظور تأمین هرچه پایدارتر برق مورد نیاز صنایع و همچنین سایر بخش‌های مصرف‌کننده از جمله کشاورزی، تجاری و خانگی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/671135" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671134">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">روزهایی که از تاریخ گذشت و ما میان این لحظه های دردناک بوده ایم ..</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/671134" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671133">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3acd02fbe.mp4?token=LTFj4Pm5SyP-Pi--tsl28J7ciBlufJZ2RmTUT9BfNe082QPStYTArHqCIwgCbU4rXnJz6CDhgFp8_bzRTJc9E6Gq8Xp5vxBWYb4c2-SuMWHXcmZcpuwlDr-rgVaX22xZO1KWvtAbkBXENHQ7zL_iyEzzGRAQRwDO2P65jEKXQHKIgKkiEQMuxyxDBSCe124WVIseR--xzHfQOTKJJ5bUgyIqdKgreHUWNFyewuYvZKvsp4nEFtjrvv-rX_cXr7nXQUXfDde1SYUAP3WAaSk002vs6A1DKrYqrF8KEorQiZUXSF-L-PMC39cULPcTmu-E3ivZiFMOCneSP_DNzZCuBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3acd02fbe.mp4?token=LTFj4Pm5SyP-Pi--tsl28J7ciBlufJZ2RmTUT9BfNe082QPStYTArHqCIwgCbU4rXnJz6CDhgFp8_bzRTJc9E6Gq8Xp5vxBWYb4c2-SuMWHXcmZcpuwlDr-rgVaX22xZO1KWvtAbkBXENHQ7zL_iyEzzGRAQRwDO2P65jEKXQHKIgKkiEQMuxyxDBSCe124WVIseR--xzHfQOTKJJ5bUgyIqdKgreHUWNFyewuYvZKvsp4nEFtjrvv-rX_cXr7nXQUXfDde1SYUAP3WAaSk002vs6A1DKrYqrF8KEorQiZUXSF-L-PMC39cULPcTmu-E3ivZiFMOCneSP_DNzZCuBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر قرار بود شخصیت‌های کارتونی زمان ما هم پیر بشن
😢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/671133" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671132">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ارتش کویت: یکی از شناورهای نیروی دریایی کویت هدف قرار گرفت که در پی آن، ۴ نفر از نیروهای مسلح کویت مجروح شدند./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/671132" target="_blank">📅 22:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671131">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6f8ce096.mp4?token=lqkdk1XqvGoYJMqrOg9dPTtyAIeyWdTC4GS60lY7Gp0LMwqJjXtFlWvBITHmxi2zGs4hjxERqky56846SzJ5lmEn5BmHx0pYvKLcFP-OhTeTIZOnUSesa7lN3cV8aMz6oHzWTtx-Z6SORwoyqNfTUmvbbS5RoLdMb64JkMm5BbkX7IPwhb0kBD0dhhMQHKsF4H_LuZjz5iNfiq0GAa5vuF4liWvEF6CANrysslZED7Z1bSqA8a68A9MuoFKqRIfGrpqj8q6E-Skh8UjMmTsi3wnT-FTkdk8B9FGC12b1ZNP80cAEzfvgNHzmwr2qtfAZIaiCiY1IzbHPwoe0RxbkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6f8ce096.mp4?token=lqkdk1XqvGoYJMqrOg9dPTtyAIeyWdTC4GS60lY7Gp0LMwqJjXtFlWvBITHmxi2zGs4hjxERqky56846SzJ5lmEn5BmHx0pYvKLcFP-OhTeTIZOnUSesa7lN3cV8aMz6oHzWTtx-Z6SORwoyqNfTUmvbbS5RoLdMb64JkMm5BbkX7IPwhb0kBD0dhhMQHKsF4H_LuZjz5iNfiq0GAa5vuF4liWvEF6CANrysslZED7Z1bSqA8a68A9MuoFKqRIfGrpqj8q6E-Skh8UjMmTsi3wnT-FTkdk8B9FGC12b1ZNP80cAEzfvgNHzmwr2qtfAZIaiCiY1IzbHPwoe0RxbkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار موشک پاتریوت آمریکا به دلیل نقص فنی در آسمان بحرین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/671131" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671130">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در اهواز
🔹
دقایقی پیش مردم اهواز صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/671130" target="_blank">📅 22:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671129">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
وقوع چند انفجار مهیب در ریف دمشق
🔹
منابع سوری گزارش دادند این انفجارها در شهر «صحنایا» رخ داده و هنوز علت انفجارها مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/671129" target="_blank">📅 22:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671125">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CE53vqD120IH3ddzYitQnebNK3Rh0yFbi6iwSuhWjX5B4w7DNVB1XhcuYoPF0iMb2V47MsoC-tbKBNWEFNVsACYNr1_O3suOcwUfbfIqhy5jXfd88LrPKqNlbMlxz9xdylYuLZHMdbBIdEPDzGHDI2jUQhfnCJmQlQktXbgJtEB_HM2iBCD5w0FO6FBoiU_c3_VVFuUWcT4Q634HhB9WKy8-PWlIKdGFKFt9muoN29F5yVd6kiuZrZ0lRudb__9Ni-IFVZTpVopCkR2SUTxQYOnnQB9RBgM9t38wzqGToc1SuXaRPwAOZyC2BLmYj0QzVrYqxsNQLakTeBWETYfAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AU6g29IFqToaEAv2AOWdC48H40G0FIe4VZBwypt-0behS-ZSFD4mgIBJUHH2UkyqgotV5G0hp9oa3XVGTUpVSZ_5SfBmwVivWKMUF8JGkbgr_9lyGxJC0HOvgZd7kb6EqsbWFpi8B3-k4L77968zBsWMVnq0OFTnz3DtR83beTd0d_fSqmYd23u-4gm5HrwyPwWESZvUDWmh-zDKaIEHq2x1peabRAVmyhh_20TCA3MpADNw6AsUZCrbu-I4gvwAtaXD-0czF5DU_3rJNSJXO2cn_zmF7QuFtE6Nfq1CEJwZWxsFWeXIas7r_hUbMM8rWDN3N9iIwwhAOkOHbHlyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYUUgu_gc7f2V_987QNTABuXWx2FQrQuZRl7nXQKbkoGr05yMXIHIyaZF4ryNf3R77JqNiwX7ydKIuDNO62GV_TQ-DqnwYs__ADwSZfb7mw0fUgEdgTO9u48h-VDIlZV-QEJgbM-Bv_isz0AWpDuBaazM4LQut0QQ1t6dQdQAyjIcpUyPdyhhwOvJ2Mo8JxtgW58KAkrfhLrQBKeHVM8F3zwm_q2AijRr_G1g7VwC0_71PNeyyHs7FT8DfrfCDkE3VQDYOLqDO-igMYkdjPNh4G1dfboSu06DnqpdyPyzVzL55mph4OxY8B_B3C84IECVAvHsnbmNLgIW43YQ_ZrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gK2NQH3oueU0NTf0P3H3W4psYLdYCMol8sdvuzBe7VIEEYrPW0cM8avBrDpna6ePmsEC1CW0E_h2gQjckraykCZxsDE0flf6yDtJc6vfCN40blL-J9LObp1RJl_fX9jvzgScyWGXKdub7yewL8JQYiDzcumInyZfXzIpOqHuHvo1yUOcnDq6YivqeTGBginCfkTG5jZVdDnm4Qz06Al62bE6UyzRergfEL2FOkRX4rQIQjYH57isMtO60OpOSOlmy5tZvlXgk1p6ItMVpqGyWiKxZElSggcgIt8OKsb_KIZObnveyzJT7_eIJ0j2SuMyrPGbtk3OEVwG0Gwi40O0Zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع پروتئینی هم متنوع هستند با بهره‌گیری از تمام آنها میتوان از سایر مزایا نیز بهره‌مند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/671125" target="_blank">📅 22:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671124">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbaf1ccbd8.mp4?token=KhefnX--Kf81fmjXBJuorTMh49xgKIGO8bzxjNZzR8fQ5ERKoecKY96qzYkV-6qZGSBlva8Hcmzjch8uB9sCpfcdluRKM02fIptSm6U7xmF8m3ZYobJAtJKtRRRtuGdBLmgxRbNgKQZjgUypnOXkWCnYq-2gQk_boh8S5IImXeTIz1yewjwnl6v7pYrz57fovTEBj9phLsGkxh6HFlvRk3IERdL6x38Vkz_CMVLO2yod96nh1OR_usivloZCxLOOXYMfA4J5eSZXvcbCidYdWoVgbyNEx6u6l4YdUSPtC1CzjjAmhH7LmK0WFyjLYWyxzkQOi67Vg7h_I4K4p9DTV3LU1N34J9xFXO_c27BQ0vAdCRH01DAFgV04ouBFToETaUZeffvCXC7YHx8m0tjX7NCM_f864o1_tVv7qdsyzthmnupmnAXbJ2eZZuJB2VRYRsdfLmB70pNQQEDgrGKOEHYbf_U3oQ0643B2ZeEaoqtmQCwv38ZundwExu2YVYW2zlhGlk7D8UHQdDWmFjt6iMoJ_ZwQsmOQIDxg9UigSIrh4TPOylw077yb_1juBsRJRyRFfDW6lw8vNEoFcNRyo2etf4s5jZHpHfAqhHSNCxWZblufHbR_GPFMiuDHWS7KvnDsxC2NjL0c--EFk_vi-FJ7igkC_n9cabAztokIwAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbaf1ccbd8.mp4?token=KhefnX--Kf81fmjXBJuorTMh49xgKIGO8bzxjNZzR8fQ5ERKoecKY96qzYkV-6qZGSBlva8Hcmzjch8uB9sCpfcdluRKM02fIptSm6U7xmF8m3ZYobJAtJKtRRRtuGdBLmgxRbNgKQZjgUypnOXkWCnYq-2gQk_boh8S5IImXeTIz1yewjwnl6v7pYrz57fovTEBj9phLsGkxh6HFlvRk3IERdL6x38Vkz_CMVLO2yod96nh1OR_usivloZCxLOOXYMfA4J5eSZXvcbCidYdWoVgbyNEx6u6l4YdUSPtC1CzjjAmhH7LmK0WFyjLYWyxzkQOi67Vg7h_I4K4p9DTV3LU1N34J9xFXO_c27BQ0vAdCRH01DAFgV04ouBFToETaUZeffvCXC7YHx8m0tjX7NCM_f864o1_tVv7qdsyzthmnupmnAXbJ2eZZuJB2VRYRsdfLmB70pNQQEDgrGKOEHYbf_U3oQ0643B2ZeEaoqtmQCwv38ZundwExu2YVYW2zlhGlk7D8UHQdDWmFjt6iMoJ_ZwQsmOQIDxg9UigSIrh4TPOylw077yb_1juBsRJRyRFfDW6lw8vNEoFcNRyo2etf4s5jZHpHfAqhHSNCxWZblufHbR_GPFMiuDHWS7KvnDsxC2NjL0c--EFk_vi-FJ7igkC_n9cabAztokIwAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با فرزندم که به وطن عِرق ندارد مواجه شوم؟
!
پاسخ مشاور را ببینید
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/671124" target="_blank">📅 22:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671123">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر کل سندیکای صنعت برق: خاموشی‌ها فقط به تابستان ختم نمی‌شود و احتمالا به زمستان هم کشیده می‌شود
مهدی مسائلی، دبیر کل سندیکای صنعت برق در
#گفتگو
با خبرفوری:
🔹
با وجود ورود نیروگاه‌های خورشیدی و سیکل ترکیبی، کشور همچنان با دست‌کم ۱۰ هزار مگاوات کسری برق مواجه است.
🔹
دولت برای مدیریت ناترازی برق دو گزینه دارد: محدودیت برق صنایع مانند سال گذشته برای کاهش خاموشی خانگی، یا افزایش خاموشی بخش خانگی با هدف حفظ تولید و فعالیت کارخانه‌ها.
🔹
از ۱۰۰ هزار مگاوات ظرفیت نصب‌شده نیروگاهی، در بهترین شرایط تنها ۷۰ هزار مگاوات قابل تولید است؛ روز گذشته نیز با پیک مصرف ۷۱ هزار مگاواتی، فقط ۶۳ هزار مگاوات برق تأمین شد. به دلیل کمبود سوخت نیروگاه‌ها، احتمال تداوم خاموشی‌ها در زمستان نیز وجود دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/671123" target="_blank">📅 22:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671121">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
معرفی انیمیشن: بچه زرنگ (۱۴۰۱)
🔹
ژانر: انیمیشن، ماجراجویی، خانوادگی
🔹
امتیاز: ۴.۱
🔹
خلاصه: محسن، پسربچه‌ای عاشق ابرقهرمان‌ها، پس از آشنایی با آخرین ببر ایرانی وارد ماجراجویی پرهیجانی می‌شود تا او را از دست شکارچیان نجات دهد. «بچه زرنگ» با ترکیب طنز، هیجان…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671121" target="_blank">📅 22:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671120">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc203453c9.mp4?token=kPSqzfOOFOpWH-106DdSdRXYH5WbWrhQ0AMGdOT_COKUATGEWic_ncDypvirbigLu2GZ_vd6b-gNyQTaswlM2VRheEulRP2ti9FMcJoC4zG8FAbmfxpUT62SYDhFOi8Q85b0CyblACFaRqcGuhSFe0Biok5vLTR_M4pzQ0Bl0PNYCgcj56nTqC5nInkWA7msuJdgv2DBcBHOHIp72F_62xUzuqDHZXsT_PpU4fF2SA64c517ea1yMZdOpFMnSsbs6Z8h_hl_BN2zdbHBfynO4P0y8rS7Q6XifvbxO-_Qqv3XFfCPoYXfil4Uo-hRnlFDEKCUVIiYa4LNvrALWGtn7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc203453c9.mp4?token=kPSqzfOOFOpWH-106DdSdRXYH5WbWrhQ0AMGdOT_COKUATGEWic_ncDypvirbigLu2GZ_vd6b-gNyQTaswlM2VRheEulRP2ti9FMcJoC4zG8FAbmfxpUT62SYDhFOi8Q85b0CyblACFaRqcGuhSFe0Biok5vLTR_M4pzQ0Bl0PNYCgcj56nTqC5nInkWA7msuJdgv2DBcBHOHIp72F_62xUzuqDHZXsT_PpU4fF2SA64c517ea1yMZdOpFMnSsbs6Z8h_hl_BN2zdbHBfynO4P0y8rS7Q6XifvbxO-_Qqv3XFfCPoYXfil4Uo-hRnlFDEKCUVIiYa4LNvrALWGtn7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون حقوقی وزارت خارجه: آمریکا با بازگرداندن محاصره کاملا تفاهم‌نامه را متلاشی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/671120" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671119">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سپاه: چندین سوله نگهداری تسلیحات، قطعات شناورها و هواگردهای دشمن و رمپ استقرار پهپادهای MQ9  در بحرین هدف موج سوم قرار گرفتند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
الَّذِينَ آمَنُوا يُقَاتِلُونَ فِي سَبِيلِ اللَّهِ ۖ وَالَّذِينَ كَفَرُوا يُقَاتِلُونَ فِي سَبِيلِ الطَّاغُوتِ فَقَاتِلُوا أَوْلِيَاءَ الشَّيْطَانِ ۖ إِنَّ كَيْدَ الشَّيْطَانِ كَانَ ضَعِيفًا
🔹
ملت شجاع و بصیر ایران اسلامی؛
رزمندگان غیور نیروی دریایی و هوافضای سپاه در موج سوم عملیات نصر ۲ با رمز مبارک یا زین العابدین علیه السلام و تقدیم به ملت مبعوث شده، طی یک عملیات همزمان موشکی و پهبادی در ساعاتی قبل چندین سوله نگهداری تسلیحات و قطعات شناورها و هواگردهای دشمن در پایگاه شیخ عیسی بحرین را منهدم کردند و همچنین با حمله به رمپ استقرار پهپادهای MQ9 دشمن در پایگاه علی السالم کویت تعدادی پهپاد را منهدم و یا به آنها خسارت وارد کردند.
🔹
این حملات در پاسخ تجاوزات بعد از ظهر امروز ارتش کودک‌کش آمریکا در حمله به تعدادی از ایستگاه‌های ساحلی نیروهای مسلح ما بود.
🔹
مقابله به مثل و تنبیه متجاوز تا وقتی جنایت آمریکا ادامه دارد استمرار خواهد یافت و در صورت تکرار این تعرضات با پاسخ‌های غافلگیر کننده مواجه خواهند شد.
🔹
تا زمانی که شرارت های آمریکا در منطقه وجود دارد یک قطره نفت و گاز از منطقه صادر نخواهد شد و این تجاوزها جز تأخیر در بازگشایی تنگه هرمز نتیجه‌ای نخواهد داشت.
و ماالنصر الا من عندالله العزیز الحکیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/671119" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671118">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سلطه شهرهای خوزستان بر لیست گرم‌ترین‌های جهان؛ ۶ شهر استان در میان ۱۰ نقطه داغ کره زمین
🔹
بستان: با ثبت دمای ۵۱.۶ درجه سانتی‌گراد (رتبه دوم جهان و گرم‌ترین شهر خوزستان)
🔹
اهواز: با ثبت دمای ۵۰.۸ درجه سانتی‌گراد (رتبه سوم جهان)
🔹
امیدیه: با ثبت دمای ۵۰.۵ درجه سانتی‌گراد (رتبه پنجم جهان)
🔹
صفی‌آباد دزفول: با ثبت دمای ۵۰.۵ درجه سانتی‌گراد (رتبه ششم جهان)
🔹
آبادان: با ثبت دمای ۵۰.۲ درجه سانتی‌گراد (رتبه هفتم جهان)
🔹
بندر ماهشهر: با ثبت دمای ۴۹.۴ درجه سانتی‌گراد (رتبه نهم جهان)
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/671118" target="_blank">📅 22:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671117">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvHsrckHWV4d3w3-aFfzcoEKYYPqDE9y2nhHdT0omkcj26yCPgocwoNoZcWcU8VTOw_qtpE-wic8eduXcou38K5udAIZ3gPI2RWpur3wLDJZQTVPF9gGbOAZzwOPzZycRVa5VptGhrHaPZ0HdU9DfnkD0Z569j05wMAQYGf9YdpLvFqnBs_AvhIogPwJ4wqjIbSdU3f8lXHcBx5PP_89lZWx6ABaLB_-67Gi5-5YheHqv3mfUYl3n65ZEoXUFlWkdQnrC9LrU4moaBm7MbCsfBSvS7LBD09tt0UIXQww5zgTtX20Ts3Ou8bsrDh-ev8mDHAnXQNE-gaaD-l1UDGtrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارش کارت بانکی با طرح ماه تولد از طریق اپلیلکیشن دیما/ ۳۰ طرح جدید کارت برای مشتریان بانک ملت
‌‌
🔷
بانک ملت امکان انتخاب و سفارش کارت‌های ویژه ماه تولد را را از طریق اپلیکیشن «دیما» فراهم کرده است و مشتریان می‌توانند از بین ۳۰ طرح جدید، کارت ماه تولد خود را انتخاب و درخواست صدور آن را ثبت کنند.
‌
🔷
این مجموعه کارت‌ها شامل ۱۶ طرح عمومی، ۱۲ طرح مرتبط با ماه تولد و ۲ طرح ویژه مشتریان مهان است و بدون نیاز به مراجعه حضوری از طریق شعبه دیجیتال بانک ملت قابل سفارش خواهد بود.
‌
🔷
در بازه برگزاری جشنواره کارت‌های جدید بانک ملت تا پایان شهریورماه، صدور و ارسال کارت برای مشتریان رایگان است، به این صورت که مبلغ کارمزد کسر شده پس از ثبت درخواست، ظرف ۲۴ ساعت به حساب مشتری بازگردانده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/671117" target="_blank">📅 22:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671116">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTBpnEonF_1VZbIJv48IFX2JTKNeVTe_SI6TW3ozrHNfI6ej_wvDCUhg7HKLIxr8gXbtERIvSk90j28nOISiL8ApGAz3M4nr6w9bHthYAz7vsTfTJR_PmiYsYg3PQn92Ho1nN_0V3XbqoppNTzJDFzMl54TVd3YBPegxvNhRCWgzJfORJguLo32NQjSz1_4rZHEwXYbVnuTj1YnkdsFzGvIK64oC10UbPnc5BrfdTNjAX34MvKzNYnQjoYzqM-FI9OwYAQE8LUoPAYrBOUWJcuOCLd66YmxG5megoUj0Rg7CyhPxUVNwWGioUNrMXhIzdqSzLsObQAYod6OAPRWD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
خون در برابر خون؛ جدیدترین دیوارنگاره میدان فلسطین اکران شد
🔻
دیوارنگاره جدید میدان فلسطین تهران با تصویری از ترامپ، نتانیاهو و خانواده‌هایشان رونمایی شد. این اثر با تأکید بر خون‌خواهی امام شهید و شهدای مظلوم جنگ اخیر، پیامی صریح درباره پاسخ به آمران و عاملان این جنایت‌ها ارائه می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/671116" target="_blank">📅 22:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671115">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وقوع انفجار مهیب در حومه دمشق
🔹
گزارش‌های اولیه از شنیده شدن صدای یک انفجار بسیار بزرگ در شهر «صدنایا» در حومه دمشق حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/671115" target="_blank">📅 22:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671114">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de3410e77.mp4?token=cBRym-LMt2JTeHKK6wisaEmhjx9ZaRVJ6oxiHGfUgX1hcZRkhSX5eE3DvXjOs1VYGOi6mwNsPM-bdovWqyjj3u3uZrR7PsrMiLIOLBpGHIQB_SRhN_J-uOOKcvPFqJoZQnjlDyJouJYMbYKf46DKG_AFj8ROIxmhntFnMoK0wTqddaMORSiQQxXBL-LSCPM2aP5pJWw_oijtHG2sQKxuH0I2jIW0VOdUotseGoJVo0XR4np0gT8JywXA3Gl6S7N6pdPa-7HVC_V9S2cSHiiuH2Q8FIRjnJO87GSZq5cgo_J5bWvibLQrD2fS7c4eUk1u8VPINHAFhqbcXU52O4vZ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de3410e77.mp4?token=cBRym-LMt2JTeHKK6wisaEmhjx9ZaRVJ6oxiHGfUgX1hcZRkhSX5eE3DvXjOs1VYGOi6mwNsPM-bdovWqyjj3u3uZrR7PsrMiLIOLBpGHIQB_SRhN_J-uOOKcvPFqJoZQnjlDyJouJYMbYKf46DKG_AFj8ROIxmhntFnMoK0wTqddaMORSiQQxXBL-LSCPM2aP5pJWw_oijtHG2sQKxuH0I2jIW0VOdUotseGoJVo0XR4np0gT8JywXA3Gl6S7N6pdPa-7HVC_V9S2cSHiiuH2Q8FIRjnJO87GSZq5cgo_J5bWvibLQrD2fS7c4eUk1u8VPINHAFhqbcXU52O4vZ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون حقوقی وزارت خارجه: آمریکا با بازگرداندن محاصره کاملا تفاهم‌نامه را متلاشی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/671114" target="_blank">📅 22:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671113">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c15bb8d4.mp4?token=r1CTEt3en7X1yeEaFMfMH5kAvphgHSKx_99uCLCJgsxP99rCp-geOYK1wVO-8zeUSl033DkXLpv5MwnMzpXkcQsmkNv8xZFqa6fFKpR0EBx764tJ61j0WB_cWrjvcXJSmPmN6-j_vMIgh-k395QNp4EDobolPWXPmXRTeCs-gEpyXC5g7uFa9ZuVkTYK355QPPJtKnxZf03dbj6eUqfiQxWkrj3d45ERYDD1zQRve7FRdM3nE4xulnsewoOqOBxKv62EtqDhB5P95HQh6Tpho72st1aah_Ezu6ZUqNVRjrIpoONldg4P4dRipKk_KXodsZQuKPee-eqHzvsJ43md4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c15bb8d4.mp4?token=r1CTEt3en7X1yeEaFMfMH5kAvphgHSKx_99uCLCJgsxP99rCp-geOYK1wVO-8zeUSl033DkXLpv5MwnMzpXkcQsmkNv8xZFqa6fFKpR0EBx764tJ61j0WB_cWrjvcXJSmPmN6-j_vMIgh-k395QNp4EDobolPWXPmXRTeCs-gEpyXC5g7uFa9ZuVkTYK355QPPJtKnxZf03dbj6eUqfiQxWkrj3d45ERYDD1zQRve7FRdM3nE4xulnsewoOqOBxKv62EtqDhB5P95HQh6Tpho72st1aah_Ezu6ZUqNVRjrIpoONldg4P4dRipKk_KXodsZQuKPee-eqHzvsJ43md4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلیلی: انتقام باید به‌شکلی باشد که مردم از آن راضی باشند
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/671113" target="_blank">📅 22:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671112">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb1475316.mp4?token=CWq7MBxvvX9wVSG_n3kwsuNhwsAuTbBdFiS7i3QU3qmrPIWFFruhpwB1Qj2W61AFMjvWWO0h40C00sN8NmS5G68irwgKJmSABUhngB-7EDe4DyFWpDoYz8xeWr8VZkTAfEvKgmWFbMj4FHrdAj0XT1jnfw4HMX5FxXWJGWDZgt3lw3oGCqi5XX_V1bGowA1fuX8DourOnZp8zu4qkQkHcF7odvNxd65BNEHN-t0OodCGsW_IGcwAMB7yAmaKawVGoRVPfaj-dlk7waSFfkNxYvcrMo3hSWqhRrd3ODJpYrgCCi7Jw0z2P74nVv-tbxtOoA-0v2It_yI34Yh7SxYtfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb1475316.mp4?token=CWq7MBxvvX9wVSG_n3kwsuNhwsAuTbBdFiS7i3QU3qmrPIWFFruhpwB1Qj2W61AFMjvWWO0h40C00sN8NmS5G68irwgKJmSABUhngB-7EDe4DyFWpDoYz8xeWr8VZkTAfEvKgmWFbMj4FHrdAj0XT1jnfw4HMX5FxXWJGWDZgt3lw3oGCqi5XX_V1bGowA1fuX8DourOnZp8zu4qkQkHcF7odvNxd65BNEHN-t0OodCGsW_IGcwAMB7yAmaKawVGoRVPfaj-dlk7waSFfkNxYvcrMo3hSWqhRrd3ODJpYrgCCi7Jw0z2P74nVv-tbxtOoA-0v2It_yI34Yh7SxYtfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جام جهانی ۲۰۰۶؛ عصر اسطوره‌های تکرارنشدنی
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/671112" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671111">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ایرنا: شلیک پرتابه دشمن آمریکایی به قشم
🔹
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/671111" target="_blank">📅 22:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671110">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287e492c12.mp4?token=rqseluHrN5yBMw5ylBaBUnjCupp84fM6ntqdL-Bg-SJfYjExh0Utm_xX6euvWpIHFzYWVEN7N9X7UGWqdQkPly0Jjn6DhQWVgswh5ln9Tq4ADRwRgTE_UPCFOliT4Z6tGpk5cQU6JmNO3tWq60H__wsN7S81vtHyijSom9pR3T9i-R52aXX3woNAqH0lT13HSLDw5TeUu9jaPYj-5HBiequJs2Fh-eH8s2jy9foM-lssvtokGanAy2wDro5LTgyfQ5OwgUWt5E7DrQYfKytpIEUnrVeS5Ni0FzZBgppHekWU_93-LiLjoVV2rRUOJ0A3HA88OXEpEH0mZAvILUG4egd4JoIqfmGY06NaEslFRI6ggPf29Z_p5YcNnOjk4y4xxUtsuxlJpeRg2BY-narfvm44-Dn7AaptXCA-Kn7SZ0O9TyaZy7-rwfHjxHsR-scBJzG2FlT4g6bBEawbqYzo60AAcixmdcC-t1Ue4703bokFGRR1sI1w3UhIosaM7XrzzLfTuaGHcjB5iJ3i2xSz_OqUjMNLr0kMMR96ltd9rAnz2vyYDrwHE1evhJALufo0JM-OuEgLZVFWTtAQ5XFxxttxX-2x6pZapnM0OXPolWoaZCxhuBPYkzQEgMjekOqxa5Fbz-QsBHanbIu4kANOarWeEtO52Vxbg54u7lm6Dhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287e492c12.mp4?token=rqseluHrN5yBMw5ylBaBUnjCupp84fM6ntqdL-Bg-SJfYjExh0Utm_xX6euvWpIHFzYWVEN7N9X7UGWqdQkPly0Jjn6DhQWVgswh5ln9Tq4ADRwRgTE_UPCFOliT4Z6tGpk5cQU6JmNO3tWq60H__wsN7S81vtHyijSom9pR3T9i-R52aXX3woNAqH0lT13HSLDw5TeUu9jaPYj-5HBiequJs2Fh-eH8s2jy9foM-lssvtokGanAy2wDro5LTgyfQ5OwgUWt5E7DrQYfKytpIEUnrVeS5Ni0FzZBgppHekWU_93-LiLjoVV2rRUOJ0A3HA88OXEpEH0mZAvILUG4egd4JoIqfmGY06NaEslFRI6ggPf29Z_p5YcNnOjk4y4xxUtsuxlJpeRg2BY-narfvm44-Dn7AaptXCA-Kn7SZ0O9TyaZy7-rwfHjxHsR-scBJzG2FlT4g6bBEawbqYzo60AAcixmdcC-t1Ue4703bokFGRR1sI1w3UhIosaM7XrzzLfTuaGHcjB5iJ3i2xSz_OqUjMNLr0kMMR96ltd9rAnz2vyYDrwHE1evhJALufo0JM-OuEgLZVFWTtAQ5XFxxttxX-2x6pZapnM0OXPolWoaZCxhuBPYkzQEgMjekOqxa5Fbz-QsBHanbIu4kANOarWeEtO52Vxbg54u7lm6Dhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار آمریکایی: از منظر عینی، هیچ تردیدی وجود ندارد که این آمریکا بوده که  توافق‌نامه تنگۀ هرمز را نقض کرده‌است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/671110" target="_blank">📅 21:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671109">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ایرنا: شلیک پرتابه دشمن آمریکایی به قشم
🔹
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671109" target="_blank">📅 21:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671108">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ba926c24.mp4?token=tInRXF0me2wEhB_zVw7j0Vm1fLRyt1tfOnQcBPPOuexPveDfAMt0gLvH2KKW67tgQ8FMwwBqubwWxLj8pazn2k4Z6Ezh87Gr9AVgtRZ2QK4edD4udkS0GEmtfSqSL4QwfkOM7JneWo8UFZj-XpPvnv20ZimDF08ZFHxZd6CctrNY-x9sT59t24plwUGTOMVfeAeAueiYc3nU3KqlxJFZU55TEY4b4QqyxfTIYJ2RMi0B22tVjxgeorkTdzNOlnK_benvgsyqCYY_R9dYl1gBcJhGC16IO2gOQf34uzHArzHdSLYwhqfa3PhrRK7bYC-wOLjxhBJW2Zhh6h2COXs4VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ba926c24.mp4?token=tInRXF0me2wEhB_zVw7j0Vm1fLRyt1tfOnQcBPPOuexPveDfAMt0gLvH2KKW67tgQ8FMwwBqubwWxLj8pazn2k4Z6Ezh87Gr9AVgtRZ2QK4edD4udkS0GEmtfSqSL4QwfkOM7JneWo8UFZj-XpPvnv20ZimDF08ZFHxZd6CctrNY-x9sT59t24plwUGTOMVfeAeAueiYc3nU3KqlxJFZU55TEY4b4QqyxfTIYJ2RMi0B22tVjxgeorkTdzNOlnK_benvgsyqCYY_R9dYl1gBcJhGC16IO2gOQf34uzHArzHdSLYwhqfa3PhrRK7bYC-wOLjxhBJW2Zhh6h2COXs4VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت دهم مستند احیاء و حقیقت | یادمان می ماند
🔹
تقدیم به آنان که در میانه آتش ایستادند!
🔹
آن‌ها می‌دانستند کار در یک کارخانه فولادسازی، هنگام وقوع حمله، تنها به معناین شنیدن صدای انفجار نیست...
🔹
انفجارهای زنجیره‌ای، نشت گازهای خطرناک، ریزش سازه‌های عظیم…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/671108" target="_blank">📅 21:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671107">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d052002c2.mp4?token=P_QqDbksXnlG3tk7Gl_j4g4sKmhm_PNpU5hhRhp84hsqtKg9pDv9eJyfEVugdq49uRbxglX249x-70WRr2MI8GnAzutm21Isg1uAuVhsxBt0PZNEAgoaXtrsMb_tXowMnjx0TZp5qvemo5CZpUu29dvOnTM6R6tBl9x5pZ3cgGbyAgfXBBDqLegdEU84-dZ4G4ev-yBvuIrxrCd-t0loHAQzmrwI6B8ne_rIqhRYiVObd_sC3mhFtmm4Hkwlkm806F_XNl-8SGlJ1NesjnV_s9CESafetmFew6eu5WIuyG2bQEeuRnXLq51V1vJ5bf9VwyY1UzImfkmQhBVf6Ak4Si5NXl4p5Bg85sZyEcKNq-oQ5MQsBrh-ojGWpqTCE9JvZ2v4wcvPiXuMOQAFTNmfkzCc_Var7ZA2cHf1MVHWmBOCZGkh39x1RP9MYXRj9qYNYEywWGQ8sPo-IpIBWJQ6S0rSOTsPCTdKSuPk8Mi0iyH5PSIbW3j_jU4jlzszYnAAHLDNAwsePKqwflpgC250gZ2dNkGwWOFqoy96xyFI40FGXL4PcvG5dCmZUGLO_Qw1DSCQlmzPeeG-oW4sGkSnI5avj6ptxpVgXYk1hvSi6A6EDXFNIW8ZJ6DGO49OeT34uiYnGzbeQ6zHXmPhfdfDoCJlAvUqq3t9GkjTd8xEmJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d052002c2.mp4?token=P_QqDbksXnlG3tk7Gl_j4g4sKmhm_PNpU5hhRhp84hsqtKg9pDv9eJyfEVugdq49uRbxglX249x-70WRr2MI8GnAzutm21Isg1uAuVhsxBt0PZNEAgoaXtrsMb_tXowMnjx0TZp5qvemo5CZpUu29dvOnTM6R6tBl9x5pZ3cgGbyAgfXBBDqLegdEU84-dZ4G4ev-yBvuIrxrCd-t0loHAQzmrwI6B8ne_rIqhRYiVObd_sC3mhFtmm4Hkwlkm806F_XNl-8SGlJ1NesjnV_s9CESafetmFew6eu5WIuyG2bQEeuRnXLq51V1vJ5bf9VwyY1UzImfkmQhBVf6Ak4Si5NXl4p5Bg85sZyEcKNq-oQ5MQsBrh-ojGWpqTCE9JvZ2v4wcvPiXuMOQAFTNmfkzCc_Var7ZA2cHf1MVHWmBOCZGkh39x1RP9MYXRj9qYNYEywWGQ8sPo-IpIBWJQ6S0rSOTsPCTdKSuPk8Mi0iyH5PSIbW3j_jU4jlzszYnAAHLDNAwsePKqwflpgC250gZ2dNkGwWOFqoy96xyFI40FGXL4PcvG5dCmZUGLO_Qw1DSCQlmzPeeG-oW4sGkSnI5avj6ptxpVgXYk1hvSi6A6EDXFNIW8ZJ6DGO49OeT34uiYnGzbeQ6zHXmPhfdfDoCJlAvUqq3t9GkjTd8xEmJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بریم در خیابان‌های قشنگ ایتالیا یه دور بزنیم
🇮🇹
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671107" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671106">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edxbb62I_0AbrTLw_ScGHsOfp6dEcaoNz27HN8tOauBtAguD7xx9JF_5jAzOlPOalINaee7GgiChl0fJcqXdcvi3zT2NTLWKWKpQvyK7MSiU2PlupPeTSOxpLDi99PDJrZFMoNjhrk5bWZom-MqpkdpGyKzqsrNCst5Y04svTJVlUcP25pEPhClyWQoEJNl850XYtsly0trXegwn2nqppv4RU9wEScrNfyckmfS_07BITqXxLaMqOoLy9habRZvF64IChG_TEnFV_VIw3Npb15h_1DclsjbmvdAVVc2NWMaotf_RubP8qRTTsnfG0R7YVuexXVqXPf9iAmXLdtai7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا لیندسی گراهام با سم روسیه کشته شد؟/ سوالی که ترامپ مطرح کرد!
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا، پس از مرگ لیندسی گراهام، سناتور جمهوری‌خواه، پرسش‌هایی درباره احتمال دخالت روسیه در مرگ او مطرح کرده است؛ موضوعی که بار دیگر گمانه‌زنی‌ها درباره روابط پرتنش واشنگتن و مسکو را افزایش داده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230368</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/671106" target="_blank">📅 21:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671105">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49773d4f2.mp4?token=vdEDS85Zfh9AQlFDxHvQmczJzzImddRXvErVBvLMTjEreUSoyzCYOGalKP9ryvmpDGPic5c1OwjlGQYnwG8OEjHPEG5l1Rfmcl1-yAGBMbA7RklPwMN_aHWJ7jd7fzYp86256nuSFjXBj2tC728xa7BHyHsSQR89i4AdCBBg8IE1Y3r8KkmqwlxhLO1tPFz2m06dqSaRBlf09toRvrgF8E2ogS-vJOKhc7PtbvJ8ZXnATHHoIAH5plckZPMSP5TEDEXJ-ABPcrRmMbS8VplGIBaD96OW_aMUUu157VD0cny-wASpE1IPKOLzQv3cvFVhihVssbgC3Z65McUGbAahCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49773d4f2.mp4?token=vdEDS85Zfh9AQlFDxHvQmczJzzImddRXvErVBvLMTjEreUSoyzCYOGalKP9ryvmpDGPic5c1OwjlGQYnwG8OEjHPEG5l1Rfmcl1-yAGBMbA7RklPwMN_aHWJ7jd7fzYp86256nuSFjXBj2tC728xa7BHyHsSQR89i4AdCBBg8IE1Y3r8KkmqwlxhLO1tPFz2m06dqSaRBlf09toRvrgF8E2ogS-vJOKhc7PtbvJ8ZXnATHHoIAH5plckZPMSP5TEDEXJ-ABPcrRmMbS8VplGIBaD96OW_aMUUu157VD0cny-wASpE1IPKOLzQv3cvFVhihVssbgC3Z65McUGbAahCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منابع اعلام کردند در حمله به مواضع نظامیان آمریکایی در بحرین از موشک‌های بارشی استفاده شده است/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/671105" target="_blank">📅 21:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671104">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
این منابع تأکید کردند پایگاه «شیخ عیسی» و ناوگان پنجم آمریکا، هدف شدیدترین حملات موشکی قرار گرفته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/671104" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671103">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/671103" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671102">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ادعای ‌سی‌‌ان‌ان به نقل از داده‌های ناوبری: ۲۲ کشتی تجاری از تنگه هرمز در شبانه‌روز گذشته عبور کرده‌اند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/671102" target="_blank">📅 21:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671101">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPtbpsvwsS8Tkp3yORDRcrdXBh4ftjDJelsk0hlvSv2HIxtEd66tNW53jumLysE1qhEVsJcOQIoBqCB9-AM6zKYAZOxEZ64t42qvktbX7IJ9MD4_RGsOzqoubfdd5hCY_UMts4Oj3srrcUgtmjiVZq1V0KPNudn7_O4pcRw7odKiO-Gj45wsnIXI-w6MQM0Nho3MrtIVp_RF-lfp2Vr9uwzVQLU6Dk4szIMaAjOtB9q9N8tXttVGj7rSTxgXS5wcCBTxEFkIzhIcnDP3GKvuTEg0pWeTOuQVwpeFeOseAHAG_dBHNGLxGPKWTByC0OPMj8eAfLhKYJyX5eXODRKHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملّی‌گلد در سال گذشته ۲۰۱۴۵ تحویل موفق فیزیکی در سراسر کشور ثبت کرد
پلتفرم خریدوفروش طلای آبشده آنلاین «ملّی‌گلد» گزارش سال ۱۴۰۴ خود را منتشر کرد؛ در سال گذشته تعداد کاربران این پلتفرم با ۲۹۸۷درصد رشد به بیش از ۱۷.۵ میلیون کاربر رسید.
ملّی‌گلد در این سال ۲۰۱۴۵ تحویل فیزیکی در سراسر ایران انجام داده و با ۲۳ شعبه در ۱۷ شهر امکان تحویل حضوری را برای کاربران خود فراهم کرده است.
همچنین در دل جنگ ۴۰ روزه نیز، سرویس تحویل درب منزل با پوشش ۳۰۰ نقطه در ایران را ارائه کرد.
رکورد سنگین‌ترین تحویل فیزیکی متعلق به کاربری است که در یک سفارش ۶۷۸ گرم طلا تحویل گرفته است.
دریافت گزارش سال ملّی‌گلد</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/671101" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671100">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش نماینده مجلس به توهمات ترامپ: امنیت تنگه هرمز یا با ایران است و یا برای همیشه ناامن می‌ماند!
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
از یک تفکر شیطانی (ترامپ) غیر از حرف‌های بی‌اساس چیزی در نمی‌آید. خب مردک تو از ۱۵ هزار کیلومتر آن طرف‌تر آمدی اینجا و می‌خواهی عوارض بگیری؟ چنین چیزی محال است و شدنی نیست.
🔹
امنیت اینجا (تنگه هرمز) یا با ایران است و یا همیشه ناامن می‌ماند. اگر لازم باشد یمنی‌ها حتما تنگه باب‌المندب را خواهند بست و باتوجه به اینکه عربستان با یمن نقض آتش‌بس کرده، باعث شد که اعلام شود جنگ شروع خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/671100" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671099">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4KIAWF5oG9e0-2LEx4VJEv1bDQxHyGOc-McxyeJ4V0BjfvMVET5RUEMAeKX8uqueXzunk0cuUOK6CCJ-wW7goIbNx1n3Vbscqa_TPbwxTF6rtm7MZu3rmPol-ne9Lfo3Zz9R-9-EYhDrL9Q0ATLIQ5IuOWijax2BNytPFIXVCh0sT8ChGBm2Fd91AG2IeJar3F_E5gii-nf7wphvK4zX_NYul0usIEWzXW_DEi7zlcIzxjL8fEvoPqbjP2kZiN3Oky_Z54Ux-pWZE_YI6PdUSqdX1RxpPjuEpoTvpbRI44FNo6dNF7eQSX-E0dfq_yOwDH4Q1V1dWIF9U-fJLqKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاکارد جالب زائران صربستانی در حرم رضوی: رهبر شهیدم، چون آهنربایی دل‌های همه را جذب می کنی طوری که از سه هزار کیلومتر دورتر به مراسم وداعتان کشانده شدیم و این دعوت را مشتاقانه لبیک گفتیم؛ سپاسگزار این روزی ویژه هستیم. عاشقانت از صربستان
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/671099" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671098">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
برخی منابع خبری گزارش دادند یک پایگاه آمریکا در بحرین، هدف اصابت موشک‌ها قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/671098" target="_blank">📅 21:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671097">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe7e9cf4f.mp4?token=HnQGLKfZapXSySS7_bDJR13BdR0hZTVApmFIuIGPkNvdNQ8gzCBZh8WS_-_ojZWGMXSuzeWLosJ-yN_i7j_vJHBU8DSpS_TcNwVtg11vRSP97F9TZC42c44o_n9cq1YfH8-nkOJAXOaDNzptYrwAHOlsYvotr8K5qrK7-29GCjlYmSC1Dd-GkBMYsnL5YLPNPPyHs5cIUxYDMMp6Tp9LFTFanKWBANGtIMCj4blVxhETyo0k1L0qI-QJ3XrxntuVp1viBrkd0gWuxYTjTmMEZR64rtL8oM05e9KsOCJ7ioSbMRoO_olHjXbp87451t5Fue-xr5zaKI17ZzMj7K4Fmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe7e9cf4f.mp4?token=HnQGLKfZapXSySS7_bDJR13BdR0hZTVApmFIuIGPkNvdNQ8gzCBZh8WS_-_ojZWGMXSuzeWLosJ-yN_i7j_vJHBU8DSpS_TcNwVtg11vRSP97F9TZC42c44o_n9cq1YfH8-nkOJAXOaDNzptYrwAHOlsYvotr8K5qrK7-29GCjlYmSC1Dd-GkBMYsnL5YLPNPPyHs5cIUxYDMMp6Tp9LFTFanKWBANGtIMCj4blVxhETyo0k1L0qI-QJ3XrxntuVp1viBrkd0gWuxYTjTmMEZR64rtL8oM05e9KsOCJ7ioSbMRoO_olHjXbp87451t5Fue-xr5zaKI17ZzMj7K4Fmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باقری‌کنی ،معاون دبیر شورای عالی امنیت ملی: برابر دشمن هیچ‌گونه انعطاف و نرمشی نه در کلام و نه در عمل نباید نشان دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/671097" target="_blank">📅 21:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671096">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH2PN11wwUb14WGl73m6tF1dJbTt9nd_5I0hmqQRjKX3qsD3tJ4842DlCDBmDqVqUj13ZjA5G_c2MJgJzLnV-U6dCeX7jHwdUxy2CxaLhZ4dLyhrpH-PYB9SkyQ8xkZUUF7SGdFEGYuHjpDlcyJ-hatjovviasSioCj3vMntTuJ5n8DgNO7JPghN8wLnzyNyxIwO_5wSSofkMy0XjpB0LG0NFOTzF0flDZy75Ex2yLLdV79AUDs6lFyeraYu26pzp_IvFudnJCMdnqvIvp2Y6xxSpTWdgO_mu9D1UD49PAIQIyx1_LxkM1IeF-i9cafX57SCFNndlua7N67IFV0xzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رییس سازمان عقیدتی سیاسی فراجا: رهبر شهید انقلاب فرموده بودند رژیم صهیونی ۲۵ سال آینده را نخواهد دید؛ اکنون اگر دشمنان برای تحقق این سرنوشت عجله دارند، ما نیز آماده‌ایم و برای نابودی کفر جهانی آمادگی کامل داریم.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/671096" target="_blank">📅 21:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671095">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
برخی منابع اعلام کردند در حمله به مواضع نظامیان آمریکایی در بحرین از موشک‌های بارشی استفاده شده است/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/671095" target="_blank">📅 21:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671088">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRHqc657Zeh8kcFX9V5UIXG3eR4IvxXyHC__0bc10NINriTgOWwPvESIIbIAQlzsNtcsqtYXC1o_ZT3fW897a2JWG1oQysX08tug4yAoqC7kmlLS1euJa-d7Z6Z6iUSCo20MRXSp-_BRjg2HpzJ75nWhL5_GjwQBJl-2l9maWM63LWoE8FTrQltSd4YYetEhPvnmdu6OG5PbrOnMOolvI8DCL4h6L2MLMd-tgSCKYLoUQw_TBWxvzX1Ykb64RZys5cY34sz498pfwlJNK6ORsg04a-S6hSS5J1nZO1-cy9f0gh_hJ1OEVwsBWc0Aox0430GfiXbbIb1hXuwe3bJJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQw0qCjGkkUsT0G1OWxccwMsCpsGG6BvTqc4VR1cWGNCWnez1qtkhpOXJ9BUxXLfyps8bbJQWkKFcA8nJgfo9_aBm-CFLdt8kVM6gUvuY_cdW93qnvp0yev3lxaaG16TRsFNQZFAloTEx5Myy4ggecdb3scwz1rloCMiioW0YBLZ38UeIdHmxqoJmw91AvQIveaRSuCoe01rM9dGo77mcvvAGhWCzVomkSlcr9NV3XT7DIDLScpsT4EbjzV7zywsslhpOyEn1q6SsHcDLDWds_k1ECxBqFZNKLaUR96twLVq_gcVkh8GxgPnG_XMVIU56gnZwDA19whF24x1enuAsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEmPLg-ikf4Z7NwunNFvYN08Pn-z6_TJVRLLfM475W3pLx4gq-93kpiDXGtNm2zelM2GlvgkUhrxuKDxEUiSphq2qWvmKQeBMjgGPJ4D6HkIGL_LcM1g5xa-xGrua-i_tpE1dWT7r1ZCykNI8_5gMucO5cNBAhvB5NP7-Fdq7b0a-VuZjUWP9ZQ_p4fFkNwEbHSt8bAM9xk_-JUMyIttt6HtyDdxNyptdqMXu922kLrfU-4y3jhUKVFd7kC7VakoSYqr6sNurDhrJ6_CZvQ5N6egNioahwOzAoBUpDM1Lpc_N9QTlea3TqdFmOkfDrtc6mWMl_JTBlnJ133Y-qwOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iV7I0i3R_vYzlbwCxKBQhH4gK2uGtJIQhaEc2zIF-EHpQ3lXUvv3nBbwcNDeHCiYC-G_-tUxYdaCi-5jjC2DaH6_GPa8Qt6z5aqDs2y-8Mxc3QNIS7qHCawsI2nvEy87SoagG8V0Iobpf-0wu5Goj6x7uI9lgNM0XOFlQr8JGSTc9jqp7KVDqHS2wBstmmDS2L--mAiJ5dAnw8ZrwrDdVw2qcf3vdjNEIiauC4y3tMI9BKhOWf4-164zXpnpVAfu2StH8dqvAZkrNm9E57IZ1W0kLW_cO2jgqKCHq1cyexDtb1svweDkI2ytc7AwmK4UxooyVWsQVnaleyzcCPpkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QoAGhaszA_H5C-cHNmrEubuKph9ZBq8j2dI_8Dpi0AzS_OHN82CbsErBTROiM4q69Hgwq5G4ytFI1iPEfLlFspAgONR71aN1jQB6bH6KMIfDKcH6dGZmRsXZknZWD-NozJJbDORMSiBy0fyBsAl4nE1nx0Wx0CJP1BBee1QYXOMqTOdkJar4_V3xtFQPzxeEAs6jL7kkGAjJUndoLAS9g08wVPtJRWJu4RDuvUCyFDVIV0xpA4cPIScg30OvZDwmHSIS8otIU3I3Px5GXYkCzc5S2OceeI9CcDHHxMBQilGMMd0kpAdwbzmgyHl-O2ZvE9YZDvC0RmSXs_Q16-H1Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SY3bwNW786Y0Pghf1pzKDBHE-d8FWOjcn-NvNNvLPZXnPeWa4tevVHj-rrrbPFIZZZSuLxqsT_D18GhHEuz2rlT9EgN4O2ogVh1c9bve8lB2w_SHTK76O5vNUFYvQuVA7Hu_wimKq658ExGqLXUCcci3RR9pWMyTmPWEnksz1WZCzEw-NsbX7uSvFp9NhWb90TOJmdsa2gygR1xYEinuEDnuoEx1YOb6tq7Itv3-IEUmXsucDflv9k_r4k8MZsrQ3bUBIVp2qCpuWSY9zgyjn8HRQoR7QePfMlFpsVySsiDfWTItYqEQg-8JiNRO0uK4CcgD19Fjo_yxdco2XA5aCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAMdIJs-oBqnGG9rJmnLxEdMSe8uXDjcQ0vCNUdTQGxqxWXc92VBWCYwPqwbB-r4dFyFYOgKlXFY-soe7PHalQM5TuGoCsVGxMQqO9jYXr2mryf1S46xWWSDuIi_-Sc4QgnXdJzHKqfkwvTrVYLMhmOI-0dKCrCF7WPDNfKsQBorvzoX0sfEqr2WiQpycXDKiW7T9kjp-el_xDCfY9D_5ujBDyNvSQKxPc3W48P7gEIVpk2A0y_SB7guxmM0jZIwt4YEJ72gdXGKfUIDuYHfjQ-3Wdu8kWew9wzsMPZkuoP13EUmcsJ-OhRS4da-3xHbtgVvZhn9LKCkrvsaSJS8yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم بزرگداشت رهبر شهید انقلاب در مصلای امام خمینی(ره)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/671088" target="_blank">📅 21:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671085">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
توانیر: از فردا قطعی برق برنامه‌ریزی شده در شهر تهران آغاز خواهد شد
🔹
با توجه به افزایش شدید دمای هوا و رشد قابل‌توجه بار مصرفی در پایتخت، محدودیت‌های برقی و خاموشی‌های پراکنده در تهران از تاریخ ۲۴ تیرماه ۱۴۰۵ آغاز می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/671085" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671084">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmF_5C8TQs5M5fS3FFa8gyEfCTYmZhKwjK3YcxeVXgY1nhW-AwFTfwU0IQr6YxL-1Axyx1ICXDaFPZL-DJ86FavB8C9_DIV8I5kdmZgFGZph4WqJS5MOiegW7lmAJI3rasuTdYrWTyWgi9ayNpEjYIUf8c7g_K2_7jSVILOmfWeWRoYhoF-wXLMYKqhbIiNI6gbdBFZi8GIxB7bLLCrJaEFwSX8N_DnUZqcg7s4EiIkwN_ZDVHpJRp2v_WxLt-3s43nHccDHCeJfStiPlfYToa-IDfwG0HA-Wrz1gCLIP9atXkaflsYNw5h36kNRXl_3YaLT69zNZgG2YO6LjdZTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیت‌ دِلُم خینه
🔹
چند روزی است که جنوب ایران آماج حملات نظامی آمریکا قرار گرفته و مردم غیور این دیار با صلابت و استواری در برابر این تجاوز ایستاده اند. آنان با وجود همه سختی ها از سرزمین هویت و عزت خود دفاع کرده و بار دیگر نشان داده اند که روح مقاومت در این خاک ریشه ای عمیق دارد. مردم نجیب جنوب با شجاعت و همبستگی مثال زدنی، صفحه ای ماندگار از ایثار و استقامت را رقم زده اند. ملت ایران نیز قدردان این پایداری و فداکاری است و باور دارد که نام و ایستادگی مردم جنوب همواره در حافظه تاریخی این سرزمین باعزت افتخار و سربلندی جاودانه خواهد ماند
🔹
هشتصدونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/671084" target="_blank">📅 21:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671083">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adcbdf98be.mp4?token=pGN2sqhwgb25vOvtMektGa1XkyU3YKjxBJ2kY_c61PRcFRO_bxoWB96yHecXYN-9ypwr2EHwpntrJb2a5D2C9_73kASrDXTDrXWxguVMyr7oGK0OyvdtPfC6gcCj1Wyml8b5G16jfeYENRnG8_36SnTggunlp7WLKfXVrLpWRaswFtA78phCECUuYcIC0Yx9cIjg3oelBXV4JOh-NEtlcGP454TeQhaL6AhO1g3a3OKLGkMV7a0aIufiFcTml9VhuMIi_C0eJ0rHP_tJMaPRZGFAKYnE421JhIZ66XjmYAfaPz4EeCRSM_racWH6Dxj9AHoSjJrhfUOdyiBzUwtw1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adcbdf98be.mp4?token=pGN2sqhwgb25vOvtMektGa1XkyU3YKjxBJ2kY_c61PRcFRO_bxoWB96yHecXYN-9ypwr2EHwpntrJb2a5D2C9_73kASrDXTDrXWxguVMyr7oGK0OyvdtPfC6gcCj1Wyml8b5G16jfeYENRnG8_36SnTggunlp7WLKfXVrLpWRaswFtA78phCECUuYcIC0Yx9cIjg3oelBXV4JOh-NEtlcGP454TeQhaL6AhO1g3a3OKLGkMV7a0aIufiFcTml9VhuMIi_C0eJ0rHP_tJMaPRZGFAKYnE421JhIZ66XjmYAfaPz4EeCRSM_racWH6Dxj9AHoSjJrhfUOdyiBzUwtw1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منابع اعلام کردند در حمله به مواضع نظامیان آمریکایی در بحرین از موشک‌های بارشی استفاده شده است/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/671083" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671079">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGmNsy33cyJx7NbTxmhjYaeCyoeSg9vx35Fk2mMuGYDtYaskhKjwmUd8MP_Lz61F2IIeSvmYFRr-oo04giYVoz_qwWMGM5MrxQbOv8ZY-gBcBznG1OiIFcEbGLO7Dc70NvaztIDbm7OG0wKEFY_Kmd5ZotJ7LZULmqr9dva9lO2o-wtPlEOOddghCLLcYpMLhD7nmyUKNzJzINMitBektwDlY5Jug-WcwSm_H8h-TrsirXqS7lh1OL00cy4c3uX8LaeI3iroqIaFzloRnkmvwIBj-xr9DpUSUv9bHOq8gYAU9xKgIRKKjwCVF2rYI9RcIMYozpER_LQXplw-ajUDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsK5InA-WnrqjODbqJz_6ZKwYyJsdMt0TXHVd-8mqA2NRaMDVWC1UXKBB7MTeAg3KQFxpb2xGIgLHSqKjUQPp2703A7tKEWBFKpxlaX4puUKjU32YYyoXcNkvIBajfasKLuEse9-VApOHp3hcsDrbXqdDYrLxBl_YbTpZr_raDyeNoGKScUsKIY581z3JLbwRegRJoG04LlsAqU3s_vgXOwRTwbhrIDZPEFpl6Gk9cm2eSJNh7IcbLvOnK1yGTZ6eaDGVv2fE3-MpyKTeE0A0R84ertIK-lFAu3_ygqCbb-mCy5NxVCegleObo9naMqhzBPlbJz2C8owfJ3XJ9aavg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در سایه جنگ
🔹
گشت و گذار مردم در سواحل سورو واقع در غرب بندرعباس.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/671079" target="_blank">📅 20:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671078">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رئیس‌جمهور جنگ‌طلب آمریکا خطاب به نخست‌وزیر عراق: ما [سردار] سلیمانی و یک فرد بد از عراق (ابومهدی مهندس) را کشتیم؛ نمی‌دونم بهتون لطف کردم یا نه؟
🔹
نخست‌وزیر عراق: در آن زمان در سیاست نبودم …. ترجیح می‌دهم دربارهٔ آینده صحبت کنم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/671078" target="_blank">📅 20:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671077">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4lbNo1clkbBxhtdBlxsky9CcbwJzYAuIhmEVK4P28NB0rJX-l_oi91RbAld56x_z4-ktnXoJgjV9aHp_9B_IsLMg0yN1lQKkeOXj5iV_hUAI-eCRs-q4fDFUJcRpNXjsH3J2XJWBCSAI53LFCvh5SukoQ48IT4K14HpYS7PYfsNNnZQI007wsgYzPWVDKfnwIffhP1rOuCJpNNfX7cxkTiNtW7QYhPV1pBQ8i1D85NRwcUpZcZl7y8EwYGmpaCxgH34Rd6_B22RZ8rpZd6bUVyfRHG_U_mZtSeLoSdcZAhMTXyTUFTRFyvMSu_KuBpvwIjhe1erK3YAYztc-CCB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اخطار مالیاتی به بانک‌های مالک مسکن؛ ۵ بانک ۵۰۳۵ واحد را در اختیار دارند
🔹
بانک‌ها در مجموع بیش از ۶۷۰۰ ملک مسکونی مازاد دارند که ۵ بانک سپه، تجارت، رفاه، ملی و اقتصادنوین بیشترین سهم (۵۰۳۵ واحد) را به خود اختصاص داده‌اند؛ سازمان امور مالیاتی این املاک را مشمول مالیات دانسته و برای واگذاری آن‌ها تا پایان سال ۱۴۰۵ مهلت تعیین کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/671077" target="_blank">📅 20:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671076">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=PTjEQmRQOmOc0Yrzgj-B_z9lre7jEqon9f0_5Q5s0WmFTJ9xmlwIXfl6TqJn1FCBGL3sXoxIhiTtAlj7dsK7Sdhjy9R40fRIi0yDaJ0s8LSryKmYWdEXMVkvbKxn5FE1uK9ybZ0fS6UI-gvm8kaQzQ3k0IjEYsgYhheUvWzgBuGCGaqy5VwpxYUMPIA4lkt-_D_GeytTi_roaajd23o083GiiPuCO_0EMRD6vJouIbKJQZGZbJv3dKtSM7FD0S8fcs5uX0cEJe02_zONr6VdtPl0ZjGG_17Yk3uCit6JdgIDMA6UGQyS0grglylfM-Q-nlvosonhTpsLbSvTpOvhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=PTjEQmRQOmOc0Yrzgj-B_z9lre7jEqon9f0_5Q5s0WmFTJ9xmlwIXfl6TqJn1FCBGL3sXoxIhiTtAlj7dsK7Sdhjy9R40fRIi0yDaJ0s8LSryKmYWdEXMVkvbKxn5FE1uK9ybZ0fS6UI-gvm8kaQzQ3k0IjEYsgYhheUvWzgBuGCGaqy5VwpxYUMPIA4lkt-_D_GeytTi_roaajd23o083GiiPuCO_0EMRD6vJouIbKJQZGZbJv3dKtSM7FD0S8fcs5uX0cEJe02_zONr6VdtPl0ZjGG_17Yk3uCit6JdgIDMA6UGQyS0grglylfM-Q-nlvosonhTpsLbSvTpOvhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: لفاظی‌های ترامپ را در عمل جواب می‌دهیم و از وجب‌به‌وجب خاکمان دفاع خواهیم کرد
🔹
بی‌ادبی‌های ترامپ شایستۀ خود آمریکایی‌هاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/671076" target="_blank">📅 20:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671072">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b95fb9dbc.mp4?token=GvrXfl7facNc2Pj0CMleLZVRCzvw7dgRhHPMKSUejLAU9JDiRs06n7VL6N7MO6d_3E6Pcc4lZIUAXlQrXAtnU2rFRReLrztQja-W0FdEblpnAaT9yk411J2TkVPBtOIofZtMG0rMn4dSqMHQJ0n2VHyBBVtv-C31WVWqwYnV46QuJocMx-2o_h1LlgFpcQiI3ZGlQze8mlEwU-dYJSuP7Fi6uMzTntDurn4a3S3FBiaNpRMhj0m-EunhXxaW7ZgllhlxILc9WWHomHsTIwutB_unU3hFjC5Qmv0x0wy63YF1NPuogNitcEgTSLF71sNtwU5XbNkgAH_Y4KuDlJ296Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b95fb9dbc.mp4?token=GvrXfl7facNc2Pj0CMleLZVRCzvw7dgRhHPMKSUejLAU9JDiRs06n7VL6N7MO6d_3E6Pcc4lZIUAXlQrXAtnU2rFRReLrztQja-W0FdEblpnAaT9yk411J2TkVPBtOIofZtMG0rMn4dSqMHQJ0n2VHyBBVtv-C31WVWqwYnV46QuJocMx-2o_h1LlgFpcQiI3ZGlQze8mlEwU-dYJSuP7Fi6uMzTntDurn4a3S3FBiaNpRMhj0m-EunhXxaW7ZgllhlxILc9WWHomHsTIwutB_unU3hFjC5Qmv0x0wy63YF1NPuogNitcEgTSLF71sNtwU5XbNkgAH_Y4KuDlJ296Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام مهم سپاه به مردم اردن/ تاسیسات مهم و محل استقرار دشمن آمریکایی در یک پایگاه هوایی در اردن هدف موشک های بالستیک قرار گرفت  روابط عمومی سپاه:
🔹
ملت شریف و مسلمان اردن؛  سحرگاه امروز رزمندگان اسلام در مرحله سوم موج دوم عملیات نصر۲ بارمز یالثارات الحسین…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/671072" target="_blank">📅 20:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671071">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
از آزار یک پیرمرد در کودکی تا نجات یک جوان؛ روایت عجیب از عالم برزخ
🔹
00:06:00 تغییرِ ناگهانیِ بوی خوش به تعفن، با شنیدن وحشتناک‌ترین جیغ
🔹
00:12:00  آزار و عذاب توسط موجودات انسان‌نما در تاریکی مطلق
🔹
00:17:00 حضور منجی و دور شدن موجودات عذاب‌دهنده با صلوات
🔹
00:37:30  هیچ آتشی، مثل شرم از خطا، جان را نمی‌سوزاند
🔹
00:42:20 ماجرای شنیدنی از جوانمردی دکتر شیخ مشهد
🔹
00:55:30 کمکی که مسیر زندگی جوان را کاملاً تغییر داد
🔹
01:10:45 بازگشت به دنیا با خوردن یک دانه انگور
🔹
قسمت اول (رنج و گنج)، فصل پنجم
🔹
#تجربه‌گر
: سعید اعمی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/671071" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671070">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
صدای انفجار در اندیمشک شنیده شد/ صداوسیما   #اخبار_خوزستان در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/671070" target="_blank">📅 20:30 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

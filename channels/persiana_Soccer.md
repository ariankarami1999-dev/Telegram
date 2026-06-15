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
<img src="https://cdn4.telesco.pe/file/hpFo2wrsVScXtoLNBn4KgqatEA8M7NqeZ3xD9aaDmuo5kRVjzTjZ3u2Bg0i1aN9pxpQFX0w_3cLK_Fz2mO8xB4kncKvmG_JajoJ4ZRzVLoFbdr_KTR5dLLgu7kB_wpCdBKwgdtB342-rqcijAR_0NFfPB7Zi_cxfTYB2BnQkpk3-Knnn0Z6mmbcUN73u-Mi35dJaLbzpmy3HZtMsRreqwPQwHTaJGiBIL9MYVpm8qs2EP18mAQTPd4nbS0sO3W8h-14PberAHR3Ja3rj7zVTel388fxbDpficzBVu7JwYCH108nYLAB6MHThSCNpCHR59FvHy6orjsgpqFB_JWXCjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 257K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-23495">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2c7e5ef1.mp4?token=D3GJhC3ao-i9lTH_bUvjpulWEeOqlkT-kb0DSVMt9PwpYyzpu5qasVspgGUqvjFtaXMRXiEKIXWpP2sIf6x6KHytzkHd2RGZ8ZceDkDCb5KOH0BdmGJOXnchvhUwZ33hSZhuYYmy5Xf0RLKPwqKXWy-7joF57lyNp5_yOtScXLdFNFz9hvlNEBMzIRK2wjdsadD_8H-GYBJEJ5C0LZ6URTcungXOW9nj173-ZgaPl66yNFd8BopjuaJjqg12gs5xPk0jLh-KlRdMBv9o1FaA91KPTDosBj8VjIk7cT5LI8qN30SKMn5wLAg2f9k0NW9wCSe3pcqns-6SmxHGZ1Povw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2c7e5ef1.mp4?token=D3GJhC3ao-i9lTH_bUvjpulWEeOqlkT-kb0DSVMt9PwpYyzpu5qasVspgGUqvjFtaXMRXiEKIXWpP2sIf6x6KHytzkHd2RGZ8ZceDkDCb5KOH0BdmGJOXnchvhUwZ33hSZhuYYmy5Xf0RLKPwqKXWy-7joF57lyNp5_yOtScXLdFNFz9hvlNEBMzIRK2wjdsadD_8H-GYBJEJ5C0LZ6URTcungXOW9nj173-ZgaPl66yNFd8BopjuaJjqg12gs5xPk0jLh-KlRdMBv9o1FaA91KPTDosBj8VjIk7cT5LI8qN30SKMn5wLAg2f9k0NW9wCSe3pcqns-6SmxHGZ1Povw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/23495" target="_blank">📅 12:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23494">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz9YOzI1FO3pyJX6vcrRqS7vF01vSGi8QI_5rrUGxpQwED856odc4qAi3Nhx9fVcb2A6h7IFLFv8wcDDYKaJ0Fxr6YnDpPPmQYz0wvuCAP-Y810bxV35SDTup1EVRcBYOhXiMBQ4pZCU6xvHtmXMOOYcw2DIL00624M-ZWq5OCFRM08-j20JVQ8dCDvZPCccPwY3mdZFIVpQmzPQxqvueJ7KRlZgY8DC8mKMlt-jN7TlCuqwAkqCpL2vQSpUS7SRFeuXZwo5WoOBTHKP9e7u1CS7o__plxo2EJOOZH3tCo4FgSf5YD26ntOamc_HkRHRVQjE92plgKfk4dLPSHaBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اروپا هنوز راه شکست دادن ژاپن را پیدا نکرده! سامورایی‌های آبی ازسال ۲۰۱۹ تاکنون مقابل تیم‌های اروپایی شکست‌نخورده‌اند؛ از آلمان و اسپانیا گرفته تاانگلیس و هلند. بزودی تماس سرمربیان بزرگ تیم‌ های اروپایی با ژنرال برای آموزش راه شکست ژاپن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/persiana_Soccer/23494" target="_blank">📅 11:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23493">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyOoiDlI5zsRIaGxYOnzs9DUuOORogIqGiqUoskg0DaEq1j8FzPlU3nYUIkPvEvBTfcieapR6ldqchuEyYbLqntuG6E48KsRIpiI4ncQvfD3ouV0opJW2eDzG6gxEu1Im5G3LKlURPrKzn7nijEphaVktr1BN42tXIcqjgIOT2Pkg5pNY2V-aPsXI0rBwTPD9vfO4XZWJ6TRtN1MwPKKlmgOysN6SjyDYLG9MumkAi1on_ROSOYZ6HjqLQ_xceyAKQzkfzCrsdO_YM2Yl-MIWT_KVsJsmKtYcHFBkiAGxRNvMoTwEXeCdfymUIacnjdr8K91HIeDjQ_YC4wKMP-5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/23493" target="_blank">📅 11:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23492">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST0zYbmkJVI89XAT75bB6KLBZVnpkdgUeke2lqz2GSunH0DZXHU_kdKwhdO6eBPtJt-lt7ymub5girHliEMFrdzLpzoQdvUPwgN4Rkokbv5XgEXb8tPh28R1pHAuBdAAKIAyYpG5xHyx2KS3oiK7kT-2FOScKvCkao6K8CqXC9MQyaS0nY-Nssud8rN02H3Duob9GAguz9eKZ7JU15TceGNcnPun201V3-vthq5yO-qT5JVuWu3KaCLqyalzqmOJVpCoRprXxR54f_Nf3PpsLdps0DGPHGmLtWgQCZ0Ix9Xx72InR35jeMSSpDtLP7yeFW_XTHaSmOHe0RFFgoHKhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ نماینده کسری طاهری تا ساعتی دیگر بامدیریت باشگاه پرسپولیس در محلی خارج از ساختمان باشگاه‌جلسه‌ای برگزار خواهد کرد تا تکلیف نهایی این‌مهاجم‌با سرخپوشان‌پایتخت مشخص شود.
‼️
آخرشب نتیجه نهایی جلسه رو خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/23492" target="_blank">📅 10:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23491">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiR9_vqY5NzajxdzV-eQ6ra77kSY2nTcsvW2-ThOFaJ3ZBfd1GfIa7lob0IQpJiQN1CvMMXuAp_U6LOZWtQWbbiBAjjUgJ1oPivtLQzUk1ngeOwff6-rxi_OffTFEERxIDGyMAzN87bszYHRDx-jxnuIHULoa7uatAKWAUmDiz22obQZp-2ZsXRIP_RPwWl67GuysoR4lTT0uHiZ6i9qdT8NEmrO-MLY4W-Rpmodp4ezAQ_tWQowSEf025cMELU2J9EFKOr1r49AZGdShZj_Va5OasfoXW9ildm39OyYM1af7mVjJPT7BUZ_xXu7ljlYCaZprioM8Xv-NTGik2kDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/23491" target="_blank">📅 09:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23490">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkdmaGsa0wfjm411uWiVzRS2my_kSGpYdHOr0Z5_nQ1D_vIDhwPrikWXTBTxDFr8vGYidEC6IFJlQXIHX3oGqb2WfsPqE3KldDchp-9Oar01dphCfIkE7SSUbSnpQ46shX8sKNL0r4tz55C6Qll55gZPt7L6BwdJmfa3x-uQdvxycQTvk0PU6T3BSPGDGDoapbTiJqadz_9cn_lVJ46S0Ag4LrLuKwDBZ7I5BDOa7F6bEupP6sYQmQrkTLwBX_foQfRbgli8_jh1ZOr1qik2WH3zaSq04rOotTacxlrqvY8O61go8Bn7mMAi2Ezt6bDLoFgiN0r3nZOveby9nUQqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق شنیده‌های پرشیانا؛ مدیر برنامه کسری طاهری فرداصبح‌و‌عصر بامدیریت دو تیم استقلال و پرسپولیس جلسه‌ای مهم برگزار خواهد کرد تا مقصد نهایی کسریِ 19 ساله برای فصل بعد مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/23490" target="_blank">📅 09:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23489">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c70aec3.mp4?token=cF_YHfamA9EOLFMiufYZYhQZudo4wrYOhopf-7hskmziIqH8-FjdMxy20OqPh6Ok48lMsGMQ3rI56QAaFMWWKZAbj4jIIyeNuSpA_9BZNUAgDTDffuYF8O1bKGSLwSK5F_jkFKmYD0uNOeFZHewTMuUEGuXTXaVin3Rjfzg_sW-1Qsz6l-UtqWYmI7T70iWLefKROoXJKILeqp0E8UKzi-VNSBDpb-QK7V3h04uWHL5o18GVGkS_bWQdq53VkquE9vnxNBWEegOV9C3_l3nVXPszpNL3IIGFPkhpbxqZKvyKcYQFnpM0-zmGI3vxORLBa2WOWdVDbJ6HM1qHZ3hEPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c70aec3.mp4?token=cF_YHfamA9EOLFMiufYZYhQZudo4wrYOhopf-7hskmziIqH8-FjdMxy20OqPh6Ok48lMsGMQ3rI56QAaFMWWKZAbj4jIIyeNuSpA_9BZNUAgDTDffuYF8O1bKGSLwSK5F_jkFKmYD0uNOeFZHewTMuUEGuXTXaVin3Rjfzg_sW-1Qsz6l-UtqWYmI7T70iWLefKROoXJKILeqp0E8UKzi-VNSBDpb-QK7V3h04uWHL5o18GVGkS_bWQdq53VkquE9vnxNBWEegOV9C3_l3nVXPszpNL3IIGFPkhpbxqZKvyKcYQFnpM0-zmGI3vxORLBa2WOWdVDbJ6HM1qHZ3hEPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مهمون‌های ویژه بازی هفته نخست آمریکا مقابل پاراگوئه در رقابت‌های جام جهانی 2026 رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/23489" target="_blank">📅 09:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23488">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f0fa31c5.mp4?token=h3LViyB-vfN-COmeIiWNz0i98n7pLW9rKQnRe9GRdb61xyGJxzUr90y9V4lHNkwAS0rQyWueKX_8ky7IdDkKPRqWE8ZYqI3rvXq51Ts1vYd2BGjfE6r5HEJbAl3HLYyu0W3NO64ct6o4ul9BgaJ-7uSJxCEq7vCKrUyp19kq1n4TrJaAyhMy5TbNE8YZtR_V0L49oU_knbHx6hO_hlNyPpykyJiiegULfe7tsioTyubC_6b4dbDCYV9y4Ejjf_S34009GjYJejXLuyaaR1pV7OqBmPWBy7c3Vt1BoKOrvUOB3XkYE0Z5SBZ6nBIs2Wr8yzHlduH69upyHrbenugcbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f0fa31c5.mp4?token=h3LViyB-vfN-COmeIiWNz0i98n7pLW9rKQnRe9GRdb61xyGJxzUr90y9V4lHNkwAS0rQyWueKX_8ky7IdDkKPRqWE8ZYqI3rvXq51Ts1vYd2BGjfE6r5HEJbAl3HLYyu0W3NO64ct6o4ul9BgaJ-7uSJxCEq7vCKrUyp19kq1n4TrJaAyhMy5TbNE8YZtR_V0L49oU_knbHx6hO_hlNyPpykyJiiegULfe7tsioTyubC_6b4dbDCYV9y4Ejjf_S34009GjYJejXLuyaaR1pV7OqBmPWBy7c3Vt1BoKOrvUOB3XkYE0Z5SBZ6nBIs2Wr8yzHlduH69upyHrbenugcbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌محمدسیانکی‌درباره‌درآمد گزارشگری؛ سیانکی: هر ۶ ماه یک‌بار ۴ میلیون‌برام واریز میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/23488" target="_blank">📅 09:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23486">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ydrz4rb1UpIH_R22HomIkR5Q8A4cZiaXyJPldOn5XXDVyOYCR_dGzbZjK_Th6NXKedch06bOBzFMGUT9OvONpv-Hnnqav47A_Xl64QcNegdG79Esku1orNDG4VyFo0ki4_P7vnLzvn-q6I2zv7DyoOs04ut9h2mfkjW4WhHRw2W2kNcSW3-yEk7UDoT9uJtxbtmf6x7qy7rdIR99YyzNBEgTRMh3k5bK2irf50drCAAc8Nx5PnIqGglKMXfBzNFRQxQ4L7b_9Mubjv_4iGaYeCyPPHEZ33sM9O8anUwikZN-DpzCWWHMinuTpiOREp_sf4q7jk8s_fUiA33b_ev78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EMyhHVSsuZArxjZKZDoRsuRdOqHw2trZZ-FhfMXoSlFrExhtqU2cL3JOqF23DI-jPJdC4JmdA-QWh6qlPf_Aye0h5krS70MmfaGrQVxPN3Oyi8GVCgzFF6mCApVdAB_NAEi_8wfuPwLGw4hcHIePt6PQ0AukkBs_hciJ8_jJMZ1NGwOE7jNvxJFKPLUmp3hpm5MNprNa8M9Lo20qUHAwm0QJF-2caeM9i6GQEatRZflDiGN_INdtx0oEad2hmqFvmuFEpZn8jC-hJDcTirazhGJmxfluW_9n3IAMZtvTaTVs6HHxrDqO1HOumak3CjPil5jMro56tGIMlehT0JyixQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/23486" target="_blank">📅 09:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X57w7ZqpmfSsBr9l6tpNBdBQym80fZHdumgVIwImhFRbzUDvYUjYVPqnYEaL1ZXsLUEEUig5eVOK77CKyGjVkt-ExxAHcM7XsYwEZMB9XF1blBD3bWA8wvOR3bMRcW88KqhxmxR_1iu_McuYoUEyvFnhbR3qCeuJ9peIsUdGIXaF4uXl68W83T5xNo7S3gZ42kl-TQCZ-YMAkzvIZTVEAXehhQO_2qQbS1SquAl0itZhuUE962Fv4EVTQgqWTP9oCgMGLwDr3NS-lc5bymgkGnZARTMhg_JuNgE3Az83YAO8cnLx2tQsOl_48xXdfrtXssvx7TYhUMSytbR0VGK5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌چهارم‌لیگ‌ملت‌های‌والیبال؛ کامل شاگردان روبرتو پیاتزا کامل نشد؛ سومین شکست ایرانی‌ها در لیگ ملت‌های والیبال در چهارمین بازی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23484" target="_blank">📅 03:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh5_y7ZWQc5HdcOnaf44h9M-EtM0vaYixgfWhhwDptUZ6XAFMr2qStCaCWKEaK3q7ibH1vYbEUXrkDHBhtosR6c4jUgKqAcrsvaRTeoyeiNO6Q5Hhsx4TrnTJ5HqT4vpW57TqhAivyetEUm1CPsQZfjUMUkv8LNxAs7nZZ3PrUr54PgEeJPvAWjE1lQr2RjlO6TCBZThz_UMRvvyi2daCze7egMBGKSiCwpEyP7q12xrDCkfB173wMAHVN-GVMKaqLPKKUxSHyt6qOh9lEZbN6QZPebF_LUTDuLuuEk3mYBsUuPVQKR4p-MKih3ynJzkG0a0qj4Id5S_ExJjzhDzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نماینده انزو فرناندز به سران رئال اعلام کرده که این ستاره آرژانتینی بسیار علاقمند به پیوستن به‌این‌تیمه و حتی‌حاضره دستمزدش کاهش دهد تا بعد جام جهانی شاگرد مورینیو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23483" target="_blank">📅 02:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxfN5_n2gEJD_CA7qnqQ7qYlSTCkWnQRVumviGxiI_bQ-kTKDDYtmz46ZCDLgB_3wjc77SMiPLCvq3DLet11ZP2l3nc3ysVwxVnvfSz4P_RUIjlt6z3kd53Uq2FKLMAGIHDJu3EtPP2DYzgW49WqpQM1ftUeSGza2TaSDVOkZD_v5a3aYJwBWFQ7W4ogk4fCfmrcEmbeysPCLcHNAVtpPFI2f9g5uqYGl4I5P9Z5512Heo7tPkL5jS3ds_wufH6Jqd25EYnIgX6Kb6R69vgAUg9oxyqx_Eh72GDXHkGxbPGadpJ0iiak2ll6crv8cIiobd2n3uPQKlCOb8FQqMzwLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23482" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/renpx7ADW9ZQCdeMHsJmC8Qu7aAgibktLoPmNgaY_is3ba5lvjnjPmfkrEzeE0iKiY2Pg_Oa4WYl0h9OrEzGOHnhWT5--SBTCfroDL1MKHx0Jx_Nk9bBjfMfPKpeRH2C7uexo5W19LT_eMym4DNp3RQZqBY5oNyBdPrv6rSdj50MnafPRnJW_5-0bGAXyJPgAj0NZBCbqFNLI-1R5JgKhYT-OYaSQJR8ix7T5HUiPz5dJQkNUZ4vOhqRdZMfFCYXLuGFQyfToHPYDpwnC0O9u5jLhKVB59qBCsjTGXAlcDoJwdmI1v0Nm2Xy5iEUyFdsaxbNN0Abc4Whuy0XO4WkJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23481" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD8tsEVO860FnwsocAEkiIFcBOFuZVuBuY65yhXLkZc0-XJyGBIBVGXb0i1NcDhwfL-5YAdNQa2F4IvQVlRBthOAEKus7Fw0W4YgHoyg4Okpua-8_Zt6ZyucmxqnRcanD2DghO04XoIFEjBvVy0tzIL0G3tabr_HY59Mjkvin-vLi6uo0tKZaUjC9bxFmHmXp2ghpirT4_VpKHDdgG6aZhzE6O3kW7E9iIc8g11h-pyRFF6GveBzCuFfz263WyMdFs7NlgygGeKycjI35Z0FUyofs2-7a9OuwK6i6vf-NaRoyGCPvfk0sbvXK_Wte2WxophfYaT8zlovx5LCzX3eOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
‌جشنواره‌گل‌ژرمن‌ها درشب دبل هاورتز و تقسیم‌امتیازات درجدال هلند
🆚
ژاپن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23480" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23479">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9b859a0a.mp4?token=C1vAL4xESfGs8klJIS7cSzANfqnRu3pqni_FI7T97gQKcI0lNBpWAP6eYhf1_JENyEcb-1V6P4PNToFh5BDofJtPkUHjC-5TLWx_kXmQ2oFuahMdeHG_Xaz5Zrx0EHD_dZZa0VF8Tn21YiU20nYy10n3SvUByFXReT72ZuURs-0Xa9LB9l5XCCaMKK85xvZpIWGve6WHAWkQASNM7Rba7uw3W4M-0Js0sdDEVgfdEePkKL0b3spCze-UfiHf774l62WA-AWdpjaTidQfeJ4w8HPTASMF3xPw3MT8ldmcKFRI5rHF4DRuJaDt7gmSNzSm2ndRfbX-LLkZtc22KAi4IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9b859a0a.mp4?token=C1vAL4xESfGs8klJIS7cSzANfqnRu3pqni_FI7T97gQKcI0lNBpWAP6eYhf1_JENyEcb-1V6P4PNToFh5BDofJtPkUHjC-5TLWx_kXmQ2oFuahMdeHG_Xaz5Zrx0EHD_dZZa0VF8Tn21YiU20nYy10n3SvUByFXReT72ZuURs-0Xa9LB9l5XCCaMKK85xvZpIWGve6WHAWkQASNM7Rba7uw3W4M-0Js0sdDEVgfdEePkKL0b3spCze-UfiHf774l62WA-AWdpjaTidQfeJ4w8HPTASMF3xPw3MT8ldmcKFRI5rHF4DRuJaDt7gmSNzSm2ndRfbX-LLkZtc22KAi4IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌محمدسیانکی‌درباره‌درآمد گزارشگری؛
سیانکی: هر ۶ ماه یک‌بار ۴ میلیون‌برام واریز میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23479" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23478">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23478" target="_blank">📅 01:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-opPYMbvEDcylL2qmIyi3nUqCkOEx32OnIR40Ix5LBtLJrBxS7XV77H6FAnqVvcSvirVY8hswaB6b6kNP1O2canzg23MvjHnRh5bnsjIgu7svnVuLorZEMLyUwI_5LrDb-5W8jjT7uXCPxsIHef12p_eLhJGeKMh52Zi0hxHNQu4XFX7CwBft0lndnBLUOpsaq2l5hdnYvZDfiepr-_wKUDG1Hm2_1Dc4ncQEpYly9lzEEfgToc3Z3l7TNdvkB47cT6Gg2vGtMen3QEsUQqPOc5b-Gs-PtwG6UvfYAiXn3tf3EUfiRyUnCqCQzKA--ZToQi6P2HWhSGHrZjdTuzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23477" target="_blank">📅 01:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78498ffe8b.mp4?token=laQc5Yh9obgBrym833Ha8Ic88LARdUqxPo6QYAP_8wxoD7aHNG_Wk5QtmLV6WXD7BAhQVbY-vpH2xlwHkHCThLn1i5OqXRsohBg4a1nW3gW6PtO5llPCmSdORuk-OMgjxAVTdVF3zw9g4vP1N-Qsocc-7ge0kDHSKDfP6L58ZLLKeDPWYFVu__7IOjrIxSMIDB_NtD_kEJ2sX7AF0Rs-edB-mChux7fv_dgEtNxd81zYTHXxKsp_WS3x-mVhjzPqrO1qTqqUoSj8NcnvkdUmPziFx0vvYFvGv3yLZrB1OVjZo5hIgarMdpefm2GH4b5mJnZSw7VDOSKxOfly0J7a7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78498ffe8b.mp4?token=laQc5Yh9obgBrym833Ha8Ic88LARdUqxPo6QYAP_8wxoD7aHNG_Wk5QtmLV6WXD7BAhQVbY-vpH2xlwHkHCThLn1i5OqXRsohBg4a1nW3gW6PtO5llPCmSdORuk-OMgjxAVTdVF3zw9g4vP1N-Qsocc-7ge0kDHSKDfP6L58ZLLKeDPWYFVu__7IOjrIxSMIDB_NtD_kEJ2sX7AF0Rs-edB-mChux7fv_dgEtNxd81zYTHXxKsp_WS3x-mVhjzPqrO1qTqqUoSj8NcnvkdUmPziFx0vvYFvGv3yLZrB1OVjZo5hIgarMdpefm2GH4b5mJnZSw7VDOSKxOfly0J7a7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
عادل‌فردوسی‌پور در ویژه‌برنامه امشب جام جهانی به این‌شکل‌جواب صحبت‌های میثاقی رو داد: اصلا حرفات ذره‌ای برای هیچ کسی اهمیت نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23476" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23475">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fa8e48e0d.mp4?token=UTBrYjEQsruN2B9TGV6FsxHS7O1JDtWD76bdTuNgqnlS-O_1LGYVbOLN7qcirq85w7CP0Y_7yALV4AsJQulJ-IrJs07-_gUgR3PNod29YKOYFMNpHHehP3IXRNs7ERsTVa81FX8x4qk4w9zdzk-_hfRhWEeIDyDaL-iHymu58_9HWBHD63UtmAdmeSF6sqV5Dx_Btb5BQSC6y27QAk0giJH7OmgmSCIUYxIU1TebxhvSK41vsFN8ZNEaTlcZ5gB6CxkDNzPes_XJf22aI-GEkaIW45dJew947x8oi-a0krMNLDrIA0xsA4pOy6mVH6DKy_rYXfUjm2N-ztjog5Q4BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fa8e48e0d.mp4?token=UTBrYjEQsruN2B9TGV6FsxHS7O1JDtWD76bdTuNgqnlS-O_1LGYVbOLN7qcirq85w7CP0Y_7yALV4AsJQulJ-IrJs07-_gUgR3PNod29YKOYFMNpHHehP3IXRNs7ERsTVa81FX8x4qk4w9zdzk-_hfRhWEeIDyDaL-iHymu58_9HWBHD63UtmAdmeSF6sqV5Dx_Btb5BQSC6y27QAk0giJH7OmgmSCIUYxIU1TebxhvSK41vsFN8ZNEaTlcZ5gB6CxkDNzPes_XJf22aI-GEkaIW45dJew947x8oi-a0krMNLDrIA0xsA4pOy6mVH6DKy_rYXfUjm2N-ztjog5Q4BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسپویل‌ازصحبت‌های‌امیرقلعه‌نویی سرمربی تیم ایران بعداز دیدارفردامقابل نیوزیلند در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23475" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdZOfutJj1LAyX-6LdYcRN419jrvWIOKoB1WfxXIVU0WTiJSzfBt4QmeKf67A9JTjhYt0sauj7rEu_ydDM236ZwxT8syMw_wNIOuI7hwNo_7tAHru1c2k6sJSaxEMyvBD55XS7146nU-2t8EJs-ZMsthHdiMSCha6SzhAuvmNTYAFKnN_X8h10okCh43a_OUbFvcIsHADqpD9l9FVGFobAC_lkFkaUgLmX47cA4Go_UaBl-nAJFZnIKgSFCr8thY7oY3n3BWIZ2KcfH1QFJEICuOwy9fgx6VQaTzW9t62XVLtPZ3j1z0zaE_c42_Ue_tPVwKRBw2G3KCrLSQGL29hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
میخوای‌ازبازیای‌جام‌جهانی‌فوتبال‌پول دربیاری
؟
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش‌بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون e24:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23474" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23473">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaP-LfvB5s4AfAlnNSNQ0azsuk6JeQFM3Us4j_wjpjyJeH8HV-V32bUwOQ074JVP8WAInX7VfAnRcwaIYzqt7GtJ2QBtw6zCEi62fAB0VkEpVQbgQ1Glm30jRAxwPrcPgMemZUVbsicwzd98jsLTs-2NfheqcKHAygqqwWBQfQXyltdU8JXI7cRQumYNkUX3kBysfxzGb_Hr2y8ttiGR0K05DLzfeiPNqPW1JbzQWbSB3y0FdAPPI3J6W_CMIIIfdLubeWW2tOGZkvuEPNOcikGVwiANr_HS33oj594yDOVgRSRySMGUAong0SrfV8xp4BFPff29H38v8LW-LW_dTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ نخست‌وزیر پاکستان رسما اعلام کرد:
🔴
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد؛ جنگ در تمام جبه‌ها پایان یافت، مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23473" target="_blank">📅 00:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23472">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX5KysDQXtzoEB0gfaaDvLAziLbAYApI7cpapFOmtRIaZp11_WA7CDZfVgqwVMx_u-X3bu4ZzQdg_Hkf4wxva8V0yax9MMwJwUKQ3GkCSPQorfVBppVlmSwSoA3KqofU5dm9syNhUGNIWh-2jl1HO5CmxPtdmol9zCgM9PFlaW3NCljkEZXlevXKLFhMfPd1XzwAtpeQXHtbw90YoBbQphTyYM9Gn1aDB3AKSByMbZQoWfkviflLWYmgD849bFtZlRYgiQ90YZ0PuG9k2Pd6DTDSMmvQR6PJQHz6IWxXJGRotrNybKXmgqrLFl1huH-Wp8Y3najhFHyhe6YmJ4toww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
#فوری؛ گویا دقایقی‌قبل توافق میان ایران و آمریکا رسما امضا شد. ترامپ درگفتگو با وال‌استریت ژورنال: بزودی بیانیه‌ای صادر خواهم کرد تا موافقت ایالات متحده با توافق با کشور ایران را تأیید کنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23472" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfDDjXaCObsHk5n4PFssXkv5LbCbm7HX_9Zh10uITlKSMvQYSj_yYe2Jw2zZ40FOF7kw8HPRStU0pBfbbfUzy4v_9CHMSPoCFpTogOCK9FfX-EtFp7n-BnZnBsW8WRfa4MzMGBrJiem8CMxkOUqTvPpMCBpkwfqjLwWMHi3OpbOTB67YfbNrT64DihjGZSWgmRo3ATcQsDLKhkPlLNTMmOdTyiazwBJn8_hrwjW1MlXYnOKu4ZngaTqQfrEHuvPhpGu9tJqBHIgdyEihWjBQ9hKbvz1KkcRZ6arEpxrPhSvf-dYVD0Y8GdJrOKn10P1R3iIqopdfv7iByc1BUh56iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
انزو فرناندز در گفتگو با ESP: به سران چلسی اعلام کرده‌ام که برنامه‌ای برای موندن در این باشگاه ندارم و قصد دارم راهی باشگاه رئال مادرید شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23471" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJH9x5GgOp_BSwaaTFkKwz6C_9k2LefSQikoQsXtJyKiFS1lqCqXH-lBTfbBVDpxnUogSsfKeOUG414I3smO29UDd81qKp_JyohtabXqrByCnw1CU1oFElmzlfqypLvKypP9t61qierDYjSqlo518Fx7kW8dS5Zc9k4NITYCNKAZoitU8IFibz8EbkLmFpu0ZK-aZ-mfa3Q3Wy3UIKieLEX97lTBY9V3QX1wNkoPMXjPfhoLRcn5H3Ywy6UqP1tyvjjG3xOYViZ2ws8HFNKyggL4avnI6g61nW8I4OrHFiQfdRAmAmRerWdRqvseVew5Y3vR91YyfwqrLi9UU1mh8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#تکمیلی؛ رومانو: روبن آموریم تموم شروط باشگاه میلان رو برای سرمربیگری پذیرفته و گفته با هر شرایطی حاضره به این تیم بیاد. سران میلان هم گفته خب باشه بزار حالا ما بریم دورامون رو بزنیم اگه گزینه بهتری پیدا نشد با تو قرارداد میبیندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23470" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDn5avfzB5kdz36xohNC6dkU352tRybQCxVxsSCFFxN3VWUz-tYQJtiMQOu3t4fXxtMpDpcn-IW2S9UFeLUn6QYgnN74-KrXSLplCzoq4MV0kDudqvc5XzS55TOmqfW3xp0e2C8ApZ1I9j3y8ryE8uMWLZ9f-K1xpyaLW9x8sUpvnrwpGpz-rwItHFLgeckgwcnxJvcktjDo9TCxEwG1KU06OnwEAW1-tc1fVxHMRGycQkSDVFRvleg9JMWkhR_i-YSy9UEgpUkKbJNxPNwOPc2u0ABdBHIpRbkqXt2chip43J9ylUlkbs4ulsGP6-ZEOO-Wfa9Dci63-eGCQY7OBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23469" target="_blank">📅 23:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8H_gPz-66xG75eo3HHD6nnx6goSs8tIRDmT1HMjxM--06BTEx3Fu0rWYfi_LoZ4kzOJw3wWSHAdP_ZFMubq0i6__jLSUbcyhVRnnEbrAjb9f_r6itAFNqfmp0_dnEveeBKnwttgxoETCC6LrtYCEwOP0xswLm9k4gTHuc-N0jH-0lizHpWiYPW8l16UfCFv7bajxEBlxy9G1hxHxQQroGTA5ruFdgDCVdyHDd7l-RG70GFlWVYiOVac8KMPe0DI6ELzm-Hc2oAlK3igTinG1TBUSupaM121NhQr-lbAnQ2YGfdhQBQ4gSEUVAybU-IKTISBscJeodlc00-E9Sd8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاریخ‌فراموش‌نمیکنه بچه جون؛ یه زمانی برای یه صندلی اینجوری داشتی خواهش و التماس میکردی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23468" target="_blank">📅 23:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23467">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmNLS0NQ7OP495AZdi-DFq5nTswnzJ4PJAGOPTUWtz02VBcAB5cTe1N5qegENye8vKTRg3VNUwi8jpifIuGq8JS-BzBmxkvAsgM2haZca9iV_JULP4BtczVuL6Q7E8Z8Ww7PbYPbOtoB8kMwIWRu4rm3c5eP6E0GYlAU8M4xB0f8-rFl3d2Yf-MHGuOP4mC30WZCyWOciisG9kRKUQ-rY3z8OGeCy_Lj4XkFa4llwyNCaBcGzgYeHMWMzt9Z-AmCfyYLT4g8C5eKtHG_QOo-isfHkL1RzBeB3vIwJroP4DlX9QBQ4xEUzjAzWJj4UidkRqKh_CWRPngKOK4refvkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23467" target="_blank">📅 23:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23466">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=jGBqK1Fvvq3cAkXD7OPWm6o4y7JzaOGCP26fABGwsr9PXi3ZX6VFkDS4Cwp4Z60PI4KS6_uPTVmHDDLqLeBR1Kp4WawMHEh9fvJmjL2fVqGHBC6vCcL93H6y0ATDLVOTWqzXwwG50zJl1O0zpPQL4SHwC9y9NkC_NV9ZkYOALYxNz0mczmnSdUQLwqTus7WLEkVKxZBXV87w7g27sh_plY5xAkY1efzxJKKFmZEWZ_VEHshQyTVawp04uEFVpn87UOGLuAaury04hqGHjPZaNZ_aKHQ39U28TTNHJVA00OYSda5sCfApp4Uh1xokO9A0SeUrlqJdMZWPhE4RdmmryTOtptd74jmnRdIq1ljZagwtcUJDTczFpSv7EIrwLV5npW1iKGQ-WUzKPKlPI6BCwzeQ1r9v-7dZt3Bj_UHL2rlmgQlDhjw6JRlnCp0rtPl_aVw0KmWtgwtKdFEsJ5DzL7Pa9s2ja1ijtoBvXuCgSZAjvaXfU-PkfMOW_WRfQ0ux0DWdA88JuRA--9Yk8I8Ebd_-3H7MZB9EkBTtxYPQ_UIWjwJq9Ws9Agcdm9zT_Mt2Pzm6FM7vf24b3K8Lfb_0_Q6f_zr-xc73K5sTKWLRiPqbBPHfdDKYoA0VfMHYDeWTAjDwIrnYwiFBORcizE17EU0vf4-gl90Yj4u7gY65y_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=jGBqK1Fvvq3cAkXD7OPWm6o4y7JzaOGCP26fABGwsr9PXi3ZX6VFkDS4Cwp4Z60PI4KS6_uPTVmHDDLqLeBR1Kp4WawMHEh9fvJmjL2fVqGHBC6vCcL93H6y0ATDLVOTWqzXwwG50zJl1O0zpPQL4SHwC9y9NkC_NV9ZkYOALYxNz0mczmnSdUQLwqTus7WLEkVKxZBXV87w7g27sh_plY5xAkY1efzxJKKFmZEWZ_VEHshQyTVawp04uEFVpn87UOGLuAaury04hqGHjPZaNZ_aKHQ39U28TTNHJVA00OYSda5sCfApp4Uh1xokO9A0SeUrlqJdMZWPhE4RdmmryTOtptd74jmnRdIq1ljZagwtcUJDTczFpSv7EIrwLV5npW1iKGQ-WUzKPKlPI6BCwzeQ1r9v-7dZt3Bj_UHL2rlmgQlDhjw6JRlnCp0rtPl_aVw0KmWtgwtKdFEsJ5DzL7Pa9s2ja1ijtoBvXuCgSZAjvaXfU-PkfMOW_WRfQ0ux0DWdA88JuRA--9Yk8I8Ebd_-3H7MZB9EkBTtxYPQ_UIWjwJq9Ws9Agcdm9zT_Mt2Pzm6FM7vf24b3K8Lfb_0_Q6f_zr-xc73K5sTKWLRiPqbBPHfdDKYoA0VfMHYDeWTAjDwIrnYwiFBORcizE17EU0vf4-gl90Yj4u7gY65y_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی وسط‌پخش‌زنده سرودملی آلمان رو خوند خداداد از خنده کم مونده که پخش رو زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23466" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23465">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی2026|جشنواره‌گل ژرمن‌ ها مقابل تیم کم نام و نشان کوراسائو؛ شاگردان ناگلزمن در ایستگاه نخست رقابتا حریفش رو هفتایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23465" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq63ocoVrFdITWE9wkSmjPBIuCMwTZU2K17cHWOxvqB2UBY2TQqKCE_5rFsIIB7Ae_zowOasOOLtYUSWHCzZxJrFWa1qGDM8qGeGfRw-UsFNIXyIb-hjynOu0DzeqN1qyIYUn_zKCVDGWyl82XjvTX9XBdD9gCTI12xa7ZZpZpezRf-UAIvywdcRO4ZQQ9QOL-6M2UaIlVGQtia-GGKcJn_ZAqzVgNvuKExsmsArnGqOmAXswZ5Pn_BrgThACUx9fn_h_aeBA3R1g3DHdlA0h7_zcaIlOQeAue5KkwNvYRX3yOeOBECV_Ewb5RRXq8iec1JW7xLybO9mFRWg1KUCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23464" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyqJ6C3-rk5khcCykJboNXqjd8hMd2WlsekF-xuXUcW9_2YbglSGcM9xe3TypbFJ8kt0KlBl_JCbSgv5EbwEaiO7b87urM_x5fBbKEjNgV-R715l53sIuZUcuiFZOlL9KG80xMI43OKpGIC5agtwsJTy0WgMdRdM1VjDwDJQCRk1fs4UBmmV1tbXuSD6bOk9MnpdOk67BIfAl8ij3CKOyr13wXby9xRkKrTgMx2gUl9dt-Perlo3IubjGonkEdAEe_RWcmwYzVl_4J_ZrMB-kSK_NYO2YKAlGQ509fGvrLTVPwuf0n6nywCHd_LSEPpmMoWg9Y4R4aaofYF9IDsL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLEvb-WU1fqLy3XJErsJnn1OzXCzZq6gV4Ttf3iMgIvqGFwnsoLRT8L_N2qDCqIIS10-FcVx0xYapxd3LzbvYBVdyLA4y0bhU5QCmY6BwD0BvYDHByv8z8XFgRgBwzPRjKUn9b9mYgokIJat1VKBkSBPz3pgc-lSFzZpgGw-4hfQzng1pssj6r6gUEzqrUxum395tHiDGraI3ieIXFxk767yG_wyImv_nvEu_hTJLOZs_e3bD5FaihUmU0cZVUyIFO3fI3x9nZGjuJADyn2SwzgIh_Nn9puUz5-5L2OI95kOizP_B1nfIeY87lYLrzHe1DjU_v_Y-ZewdgEPhCqk-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی
؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23462" target="_blank">📅 22:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp01EtSsEflBw-HyHdmHSL0wANpapDDwW9Gys3aAVaBnA85kBKpIq3tVh92sRNDpUuQJe7ixrrw4EJTpvXMsfJgpzn5yhzoCsVhIClqDPT_yUamA8hGaCqh0h0hb4_Jx2Df-Y-vJ3HNnjCJJUmIu0LuSag1Wpglz85Rgefa1G8n6678pa_2EFnvqTuyJGuEVZzgIOapVgj9CV6hxqyfhESyE0ctJzwbxStGCxALgUbjmP1fuwbq8yU_QQLwF0fE1uAK-4lJRIFbhZkTPbC5KsTJH1HxZnRe9EIWBsWB5_-1BXpfmAccBbym9rgUjytrWfqd1nm2UZOnMaoc4O9gR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23461" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=H32pV1WiEvARfj5w5RLH29zBAd31XroLy2_uBtlHGKw_CNlO23kUNT_-spD__6gw2JK6oUA6DpCfSZJ_kZ2-D8QlJc-4jCBcBHwTM2dT89EOd_hbPbH2woKyiyzhQsrRothL0IePLhW4mfzJ85Gx1J7SOJLqR2MN-PBhQ5xc6AjhfV0NoKe_aKcbVxefA_Ia9lL7JxZVaLUvzBBPDwzM3pVQeXLFeAG1oVdD6uC2EWs7ncUqXEGV0TmA2R-QYRrpUQfHtVP2xBpUt0_QDwQHvTsVmGOjkfLAr-ch0oj-zgf5vdydknfQChM6eX9x3prJVHXcukGmsPW_e4PtXa0BEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=H32pV1WiEvARfj5w5RLH29zBAd31XroLy2_uBtlHGKw_CNlO23kUNT_-spD__6gw2JK6oUA6DpCfSZJ_kZ2-D8QlJc-4jCBcBHwTM2dT89EOd_hbPbH2woKyiyzhQsrRothL0IePLhW4mfzJ85Gx1J7SOJLqR2MN-PBhQ5xc6AjhfV0NoKe_aKcbVxefA_Ia9lL7JxZVaLUvzBBPDwzM3pVQeXLFeAG1oVdD6uC2EWs7ncUqXEGV0TmA2R-QYRrpUQfHtVP2xBpUt0_QDwQHvTsVmGOjkfLAr-ch0oj-zgf5vdydknfQChM6eX9x3prJVHXcukGmsPW_e4PtXa0BEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های ابوطالب‌حسینی به بعضی از مجری‌های بیهوده،دلقک و بی‌خاصیت صداوسیما فعلی مملکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23460" target="_blank">📅 21:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lONOUfto7B9AMGJW2KvZM6q9yUlUN9ZxiyCUpAV3xzEdYHHYMUp7QCuK8NdD_pQdJQaGQZK3s1d_kUh5P14i3-TLW53Os9j0cSJEpbklQsRev7LNya7i_N0LPzniBQrwP3dWeXl23_3UkLiK7ksaCPYN2TjPxTFMID1Kty0Pto5qy8VTJuYU6TM0T8nEs15Upa88eL1DvYVHArTw_JQnBvrWmnjKimXJs4xbH5wyXLoU4Ci4WM7hg2VHOKCaMsioToZvrWd7vMI13h9P1THp8Hqh9jVwi96jdcncAK6eP0rq0E_RvBx9iH6Ju4cgByObEvcFJkFandwIUrZASEi5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اصلی‌ اینکه اکثر بازیکنان ایرانی خارج از کشور علاقه دارند به لیگ برتر برگردن اینه که چون شرایط کشور خاصه و ممکنه در هر مقطع از فصل جنگ بشه و بازیکنان‌ خارجی تیم‌هاشون‌رو ولکنن برند لژیونرها قصد دارند با رقمی بسیار نجومی تر از دستمزد فعلیشون در باشگاه‌هاشون…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23459" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDVs5H43veGJjDMy5mqA20tJ73Rd9rd3NaOsOc5TshIKhtmZD0AlPZZ1hU0sfcVn2_okH5hc7Wgr5ybwNnh8vfjcT5MVWUWBWsFq8keu4EqWX3-koB6qdgIAaZHLZpZWcTqiMN3I60bHr-jczczccWnAdHiBjM4kOkafZUIJjDmfZUdgoa6bvojBm3PGEZJXmW5TzHzrQyYMQGKi4tTf2RolochBojpFoDcuhNnjBUP9Pe9UXPmqfdid90GGtL_CvH_mxqQio9xzq_4NtGxlHW9TuzQg9RYWmk62UkTq0BvIq1xE7diRfzQmMsgVjG1L2xkeFFNL-0PkbSPD4fRKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ اولویت اول رضا غندی پور مهاجم 19 ساله الوحده امارات دراین‌تابستان پیوستن به باشگاه پرسپولیس است و درصورتیکه کادر فنی سرخپوشان روی این بازیکن نظر مثبت داشته باشد جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23458" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egwhMK4Ep_kY0PlimegGy-SzCpskvjsZwlLOVYtXZKJaJzDsR1D1RoFbyerfEZy_Lx8aWzhzZ_wRSWLAq9zKCk6VaWD6c-nfQXs7Wwxx2rZCd62zZd_1JUWCU2hqCvnb3icy0KaMZ3L44xPOuxShtlMpUyk9dR3hQZMUKUUlTddpObYarmMZcv-0lOY_eXQvXh14sOjlCDV_OgkfQBQXmu1ORUBEEvdJdUdaw-BCI8PxNCTq7i5rLMHRpV09h_kxXgAvcgYdQd_Po3OBezxL-P3xKpaOHRxVfiE8eGf21KTbnO904M4Q32tyhWZONyP1Doj6hL-vueaWg5q5J1Izog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23457" target="_blank">📅 20:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvX9BJ7OjLLASqYWuqI4uYPEDyf5qHOM7IscyyL6QzqElCEzBAt-TRSxA0mNYR-QwhVVw2ZRhYyOTKIU3cHckrZYQ_R1cnbLGjJ-GNWwoX8RsFCn9LGKpI1Wobuk2Q2lscuc9V2Cv1a_E2WILnkKOmwkaN2uAgMhMGibIN_V9YNs_BMyr1bVQaxoTO_8nucZ2DST0yENj6rQPKPkBqOeVEtelI6TNymlntjwI-Kug5DkMpQKcI_MC9EvqdyA6IZwQt7xsUFjP3K0PovEF8cG9TbAee-_IhSSwxJzB52OCs5MkjLwQwjn93hb2d4mnUvHRZQT5Wxzy5dhbtAGeB5VOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چهار خرید باشگاه رئال مادرید در این پنجره تا اینجای کار؛پرزبرای جذب‌کوکوریا 50 میلیون یورو به تیم چلسی‌پرداخت‌کرد.درحالی کوکوریا جذب شد که اکثر رسانه ها خبر از اومدن کالافیوری میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23456" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=cuRtPtcQ9AN1ixI86hdbJ6MLJk95yRW6a-Q-lSL6F1l467kEjNaj7SxM8ObkrJBxlZNYskiCxZqa68YkObyeJ1TiHkf8-k1nDJ6JpetgdysB86rtzlg0dMNeaDDep8mVp6Pknuu6u7obUQ38K1AEbcL8D0DOB1r25K8Alw7LzwZvS4luV2JjmoJZDDkTKhBnl5lPVgXEnKBoxa0wiJLS-k06TcGLveBY9OVL9lj72SLOm5D_mTwGdUrY7IvjvWNTAL92ignbb0rGhb9n-1R26Yx50zLgUeSG7kSJheuUOnuNCSBf1WZ-b_pdEEkxlb9HdN6r7KSFEvxkvrLpqI-AZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=cuRtPtcQ9AN1ixI86hdbJ6MLJk95yRW6a-Q-lSL6F1l467kEjNaj7SxM8ObkrJBxlZNYskiCxZqa68YkObyeJ1TiHkf8-k1nDJ6JpetgdysB86rtzlg0dMNeaDDep8mVp6Pknuu6u7obUQ38K1AEbcL8D0DOB1r25K8Alw7LzwZvS4luV2JjmoJZDDkTKhBnl5lPVgXEnKBoxa0wiJLS-k06TcGLveBY9OVL9lj72SLOm5D_mTwGdUrY7IvjvWNTAL92ignbb0rGhb9n-1R26Yx50zLgUeSG7kSJheuUOnuNCSBf1WZ-b_pdEEkxlb9HdN6r7KSFEvxkvrLpqI-AZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شهاب زاهدی درباره عینک خاص‌ش در برنامه عادل و عزیزم گفتن‌های عادل به شهاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23455" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAHPagziok7Suqdaa7pd1WtgMM5i-Mn7f0iDwDxDi65f3toFy8YEsxWSjcz97j5n946aGAAf0ZzEyrsOYZK0Vh9RXdeAFR5LVGT4fr6WhoMrw9W-Pf8CLq7L9U7vXmc3ex6mPtoniz-xAvyhG21hjJ2KbQ4Iu6SHhRPG9vohiuEsXBkz5ulmFnXpiYNTgbOKwRAYMR5QMKBrUXTvCLQyFL6nyqlvYOMUC489azFHJntNx8Wzk7uCqCLqUioL1QYV9nGtYQNvmDEwgxC7zN-ZZ5tR1s6EW6zq2Mh0GyDtG2VCm_GzMw7CNLIGoeMDEPXL-6-nX-Bn8Z9WlVqqfpoD_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
میانگین سنی تیم‌های حاضر درلیگ ملت‌های والیبال؛ ایرانِ مدل پیاتزا دومین تیم جوان این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23453" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23452">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aem5zcWMyuRCgCUfnhMwOrtYpbjO4EIffAe-bDBwBQbKM-J3mJEWgUC6qMNAXArrDbPqk-911-jCF78yiaBlzWViBSZntymBZaMVdlboOxFGwHKrHzt20VtZixV_BKRmCZbgzQoUbNFkcIEonJW8UW2POJNdUVQY3_XmGQ17gkycYaW_31KrR120TQnIV6nhFiXBioOe8o4J2koYjo1PlJ_2L1ubHDViknlDRFaMPCOaka-uYqsfJFIFw8WGvtjSaFSWw_NoBcx8d1NMK7SAzoknhGvvQMGgyJ8bfVeFr0rKgqxA3ODA9IqQyNi1aIZhp_u-HoUGAsamUlrz7dGleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23452" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u77ejBKK-aFHkMc4a2NzaUyJZzfyypEbmLt5AbdlcXUR3emeICktC50KZiepqkukf2A8k9EoRxNGpgigZOMG3C2fgQgymSizCgGrzH8rc3bPRNJeFv_aQivQPONoCThfsfy_9oT5TAPwwnH7Q60oF2N31SgaZRXnHsaH4_OqOYQrC-3YAxESNOO1eJIQ9mqx01d2zrmO-QWiMMPsXQFWZ7ddt4zoMXmS80RKfYqthDOV0KcGkjU-x17V6WzYaa9qge6895k4whRi3zCDNADdW8MsfMxGrpWEv1Hz2G-oLNlHW21vhirijuF-aWOlSQSVkpay4Ol-Hnhmlb-kvFSrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23451" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiW8TjpSokLV1iEso8QK224lc7xxdx6NFuPvP3-0jlsITEZjRHznLvG0P0omEL9t-qtqwjoIXb5rlS2OSVqRFfVE1ALJUcISA1lPrPVW1xdpexX-N8rTxX5WexE8aYTOmDOuahgefB7lx2HSaTVGeYr2o1K0aq0xM7cJQ_U-JtcwalmHG7x5qJcPYr4V1_mJvN8GbydMQXQQ4E8XkXKXaNhITRKwaZ-R1vKZDlsCCpiX9UOqRUcjb7lJIyXxgxeFAtECQ3Nh_BcNY41jGp--qEJibnAHd6FYwvxISet6N7hTbjarxid7IAQGZUCjO1mNFzR8yfdNFuOj7CwJbh69mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23450" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=VoUPaY090GSvtI7hUhm5gpNBulNRlnHHbLaY8h7hAT3jAXkMsrELV8D-ZIXwFEh-M17xxBYEgUyCA1brcCzBA7FXoehftpN6qGzdWv5meDLxVg_ud4G4KdAvUgu_84jZkBVXEIeyMhWyYnorc2TcIBKthTi9zA5fv-CrxFcHa18NjSocMpaIbEqJFqHfrlDkonqZEIbJHA0cFLZLAlgtV_A7uQFtwtNeN--pLiKx85rHvTQN_a83vsbUVc8yZ5adzJdcFBcNgH7fORnNwUtxfPnUuUPjiFQjXloFejTmuPVg1QXjOZUlIP4iNbQIL-w5GgGG3bP2qB_VUzAcdYBUKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=VoUPaY090GSvtI7hUhm5gpNBulNRlnHHbLaY8h7hAT3jAXkMsrELV8D-ZIXwFEh-M17xxBYEgUyCA1brcCzBA7FXoehftpN6qGzdWv5meDLxVg_ud4G4KdAvUgu_84jZkBVXEIeyMhWyYnorc2TcIBKthTi9zA5fv-CrxFcHa18NjSocMpaIbEqJFqHfrlDkonqZEIbJHA0cFLZLAlgtV_A7uQFtwtNeN--pLiKx85rHvTQN_a83vsbUVc8yZ5adzJdcFBcNgH7fORnNwUtxfPnUuUPjiFQjXloFejTmuPVg1QXjOZUlIP4iNbQIL-w5GgGG3bP2qB_VUzAcdYBUKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23448" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23447">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw_KgSnFgOmXFkIX5eUFUzp7fnvMVDKECqN7UXahtAXACY5kLNzBm0zb2DyFWjWYaOIb39MF4cxA1c5RGFLkmnmcdo99mMJ0Yd4h5GbdMHTlPMdnUU1FNuTYzxt2NKgkeovNNWd0r47Ifwjg-Xb3GCCvxgX9PVyWCZroozNzWJRIMRnWfWXxEYDTzcKF__ZokoJrucmsP-kGMeJWUUUhRMr6IUog2ZHm0hzRmkb3SqDbkDG9R9Um2mt7WK7F_sgsVooX9Xt3UdChcShIfI4CE-SSqDNkd9ofVuKzB42myDOidbBA4tHIO9kXqXOV9Ud2FCUajTeiTZQ03yqmZv0H7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23447" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23446">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔵
👤
هایلایتی‌کامل‌از عملکرد درخشان محمد جواد حسین نژاد درفصل‌گذشته‌رقابت‌های‌لیگ برتر روسیه؛ قطعا‌بازگشت محمدجواد حسین نژاد به لیگ‌برتر یکی از بزرگ‌‌ترین بمب‌های تاریخ فوتبال ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23446" target="_blank">📅 18:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23445">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpRDLlZy5xY4AWAqofCLFkxo_cnEmC6Vf2Ldb2TqKPVj3NlrOXwEDlijsWxbNelbLslz87aZGDrUiR0I_BNdxKigRZ6czxUkt2qINelPM9O1t2R2EEbPhVj2KKHgIGoeLvjqztPZ_on6VT9hpfhgiWkPBJnPPCkYEvyABoz2j2SN6B3V0Y-ELnMwhVsrIpGOqUgu-uCF-OVUc_243fYRpv7mummYtVUg__RKoyHk86uYv_qB6KJ5GWoxa0WsoQSv-h7XPYCGK9gMA7chn56sjfIzk1Hf0s0L9W6siVodre5eFrnAXfFHGQzUQv_E_KweNKQWwSw9HVgFkM5Tn-rc8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ ایران میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23445" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOn35IXV61U7EBtrVzzzYoIjS369wx6cvDu_Ddgjplag9HsPErO3Cy1gfPCfpdmQVRtNZOVhkvAe8CnobaRTEpv4nU85KYPffsrktDt6UuUXC1t5z3xcrg15rI-8ABbEuCnr4a-MCL-7cS-qo8UbHHo5GuwAGW-O3EnwgBwDnIIHNAH9Vdhrdrq74tujY_kMriMLwyzFPREMq1GJko-vjLCm3i_FkHe95eS0i7cVMTRHQEHRvKh6Kp38IOjVyuLcSqA1iMg5Y0rG0OhDVqDWPIn5u7ZGcB7acT5gvfowMSnFy8bDg0J3-5NGjAbzZzoHBULfH3z_hzukh1U5PJD5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت اوپتا پیش‌از دیدار ایران و نیوزیلند، شانس پیروزی‌شاگردان‌قلعه‌نویی را ۵۳.۸ درصد اعلام‌کرد. در این آنالیز احتمال برد نیوزیلند ۲۰.۴ درصد اعلام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23444" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=dMK0JbG6mLG_AHqrbNGJkSGq8oYaT8_7i9pbeHlul0koQOaKqoMmiu79X6lt2hLIyDVhTUxrjFtmkMu1RySGzgLeOmjDi5NXRSvbCE2OPZrHqSTi1oSDBpng6i3sQwj4600a3zbVfZyU6zc_GpuB-kAncQ1Cjcqt4sNlD7ikvHN3561caukZIamF0hiG8pqj_jy0W0nN9wMzXyTy-363-uG2XKaqxKZOa7ziL5gx0iwwTusUT4GrXVA2q5hx2AU3kBLq8wnw4PNkrnYupWuAskteFzVRtUNxmuegdhn6qqh4FXC89N8uEdg7SFPgDJZf5sFhV1dAKX2PjyerGwQhxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=dMK0JbG6mLG_AHqrbNGJkSGq8oYaT8_7i9pbeHlul0koQOaKqoMmiu79X6lt2hLIyDVhTUxrjFtmkMu1RySGzgLeOmjDi5NXRSvbCE2OPZrHqSTi1oSDBpng6i3sQwj4600a3zbVfZyU6zc_GpuB-kAncQ1Cjcqt4sNlD7ikvHN3561caukZIamF0hiG8pqj_jy0W0nN9wMzXyTy-363-uG2XKaqxKZOa7ziL5gx0iwwTusUT4GrXVA2q5hx2AU3kBLq8wnw4PNkrnYupWuAskteFzVRtUNxmuegdhn6qqh4FXC89N8uEdg7SFPgDJZf5sFhV1dAKX2PjyerGwQhxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برخی از حواشی مثبت هیجده و جنجالی رقابت های جام جهانی 2026 آمریکا از زبان ابوطالب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23443" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OadQibaAHfMX_EoIGkVhqm77y7j4xaTYBkCPVAjrVcfHbvrULPcz9d-UDMvqQ6LMilkn2JrlVmHsYsCE4Hpq97ncxl59HFA1KxK2ePpTnpKIdSXbWquGiJDpb8flJNhk4PgiyHGuB906xHYPNQ61Z_t8rLSXNA3igpprWYof7Gp9_1s-SEdHMy9xxZn_KbkFjx8KbVTWwkiTIjYeat17SWJT7E6DRABUQQihSajKV0bsxGSVHJYpCvNSsfGv1Yjktw-rzEhXr67VRcPXx5Bq-CrtdQlwKGFuDsksC6rzAEeD4QxqlnLMnHx2MC7Tz0o2yS7drVXcNSOUPeYHGAVYeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
صندوق‌سرمایه‌گذاری قطر اعلام‌کرده که بوعلام خوخی پس‌از گلزنی‌مقابل سوئیس در جام جهانی 3 میلیون‌دلار و جدیدترین‌رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23442" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SduDmkcg0ETonGIE3gJ6n_r3v7rVizqekA2eksh_FpZI2VHO7pT5tkfN_OVx_uJuAFV4XAuHgPQ58JNiv5eaounzAh79D-o7Q16NCWI2DyWoIjTkJEvhy9x7yeGAQyjniWJFsvPBxAb3UYfXkpwoT18FyzMDDxe6Q2Xmg0PCeQwnO50CLcmnx6Yo17SfKQiyShioiIRDwqcncsrsbMpthjoi-jMLqyA-nkUuneDL06tDeeK4JD8H1o_kRsulL8uDYysPT-vUsxKxp-b4lgnML8TH06XGf62cBvPuzFIgwOdFrYe856PZ35FK27wuh3HOJ1jfAZzU8xlMtC0gYQyqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی قطر
🆚
سوئیس در هفته نخست رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23441" target="_blank">📅 16:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDWEcYtUf0PXgGxMHMFFToVVl23zqo_yT4QxFbx1gsF4v4jnFxakSGDtwgl7tNF_x_uqZWQwVS6ThZ4IMVVSFqvA1TGMsKJoRnhIJC_ByFtW5iU7TQCaBF_AHiqMmtCxrwsPfPmJEwHvamyN-LXs9fvWyGCS-xRZHe__Rd1OP-c34ZpifMyJxEiFAIGBNmjKiscBQzN8cu_bsu0Jt2Q3OO9G7rSuX1mSbMwrv6IJvgO8PR_vqapb3zMwWTnLPG8m4Va9c79SLE7zqYekrGef1L3oodE0bFCU3xEJIBB8f_DYd2NHw-ncBDKzC4ulvs40PJEE7VxhgrHN7hzWWPN39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شبکه‌های‌رایگان‌که‌مسابقات لیگ ملت‌های والیبال رو باکیفیت‌بسیار بالا پخش میکنند. امروز حدود یک ساعت دیگ تیم ایران مقابل بلژیک بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23440" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7jbQC3gr5qMIpjrLigEcgj2wI7XWNMKVDV3oOeS5Kx071aNaobWBIBUc4_9tUrOk3FSwkA6S-G4j2BM07teUIrFQEtYh2acgnYiTO5G9OLOfBtiLF1Do5icFII0kqGK2OdOKo3yawyNLrtqH6PE5PYTEb7PkcIx-hIayYRafVS1S85gLG3SSqKSn44a_Vvl36lQpNj9DjGmcDpCymQZdE2ggxa1jyoVSiH3dQHNVrwhkzuBJwL-fVQQYD_FUxVloLCAitRkevfZV24VAPaAKgyIF3q0qFjMcmHsDEWCpSEQRRdGvR4g4BOo0aKHDLK9h_I0trY-M7KRVBT3kW9ukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23439" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU3op-Ip6ADZI3bnZMv_OorOpjNZKM9qSM8PQXVTS-rLS_pq14WNyvI2iZWLlWdOqJ-R5aoiNciRDTES1c3WYrNrmdQmmSUweNxi8_YMiy1g7qir6Jo-2m2Rs87-1Pqv_SenX1rtzvhuwMr-AGCBedR-Tq-6E_5BCWHkKYG714jj8890cwiyR-J2909v4WOB0H2U879Jp8rD9ftQpJxmm3_tYS8C8gAcYSYNRu4mElQstZ4bKOSES2Qiqn2kHJ1wS2J1EeLZc7Lu4zpTWIk8nMz05WdmvmezhJop6GHrzj7UpB95ZWjlfuSw81HIX3Wz0FyrSS8IkuXgfdYKGgybtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23438" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">▶️
قسمت‌‌‌سوم‌ویژه‌برنامه‌‌فان‌ جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید. شیت و محمد نصرتی مهمونای این قسمت بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23437" target="_blank">📅 14:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=Rc0nnvTo9dtgqzsbzbm50FwsAuoLnvv7XpV7Fkvya4MUYUtU4PXWR8fGu20JKefM65ayR9pWyxUYjaW1_DJTC2TiLNXPu08_mz1g-6uQ3GOX0A3BpjA_MeLPkaBaaCH57CzNMp229bvWbgvxIk-9TlcPsdbY0YNCU6TNc_rgdBJK9DdgimFNr6_5E88aQFuOk_VSgFhkstKUoP4JFxdM-Ho4x5uZ-Mkn1fc0AkUJ5w2_SMLloan_KVe5-fWck9Gy9qhQ9yjSGZ3MYfGTeE8AxyfhE-Z98dPzZNIgFldZYVCUOp3xVfFztwKN8SZKcXWBaiucCi7BMta8VjThcDOQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=Rc0nnvTo9dtgqzsbzbm50FwsAuoLnvv7XpV7Fkvya4MUYUtU4PXWR8fGu20JKefM65ayR9pWyxUYjaW1_DJTC2TiLNXPu08_mz1g-6uQ3GOX0A3BpjA_MeLPkaBaaCH57CzNMp229bvWbgvxIk-9TlcPsdbY0YNCU6TNc_rgdBJK9DdgimFNr6_5E88aQFuOk_VSgFhkstKUoP4JFxdM-Ho4x5uZ-Mkn1fc0AkUJ5w2_SMLloan_KVe5-fWck9Gy9qhQ9yjSGZ3MYfGTeE8AxyfhE-Z98dPzZNIgFldZYVCUOp3xVfFztwKN8SZKcXWBaiucCi7BMta8VjThcDOQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وکیل تتلو گفته‌تتلو واسه‌ماه‌محرم درخواست مرخصی کرده که بیاد داخل هیئت‌ها نوحه بخونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23436" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=pVjcj6mHUXHI1DbND7u3UgYlmHGMtoIuBgvVKOmaCgHrSxFQd2DMyu__dTiqZDT6Xjcp5z3hBQhZEDoZ0yIoVcr07KO8JP-OdHc2qNirkZ7Kst8hZO7VBlq-5oQjHk9Vc0PD5N_hau9QIxdP5jlYjduOBG1jUYFqrWAxFqHPLe3tvGmyebZfee02Z511UZSmy-1FNPbXK61FuFachH_sEn0hIW_xBwSlWcEfCSRxpQ8fB7a9p5ach_DqxJK72O_jnGd-u94cCqz8kQeaiHUSSHiwSyGAho0ABG7AxoSows1hKLR5_JeqwxbkYmagM_4yIo-XfZ7t4tbvvRedPUnC6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=pVjcj6mHUXHI1DbND7u3UgYlmHGMtoIuBgvVKOmaCgHrSxFQd2DMyu__dTiqZDT6Xjcp5z3hBQhZEDoZ0yIoVcr07KO8JP-OdHc2qNirkZ7Kst8hZO7VBlq-5oQjHk9Vc0PD5N_hau9QIxdP5jlYjduOBG1jUYFqrWAxFqHPLe3tvGmyebZfee02Z511UZSmy-1FNPbXK61FuFachH_sEn0hIW_xBwSlWcEfCSRxpQ8fB7a9p5ach_DqxJK72O_jnGd-u94cCqz8kQeaiHUSSHiwSyGAho0ABG7AxoSows1hKLR5_JeqwxbkYmagM_4yIo-XfZ7t4tbvvRedPUnC6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23435" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s50BuxGp4rfeC3Fn8LDPMguN2ORdM0jnFWXxmbDhHuOIOMq86_Oek7Xlbr_zv5QBOseiW8DxNj24Onn9Q6o3qfHA7RbM7bXoXTWg-fMAw7DV-wAKzPSZHac3EcgQXaqoG-oF9u6QLL-CStKsiwFDSvh8KMMKZw6qscFhuMbDCt0EzsEPquISBMQof2nB0HlXInjkvl7GElJ4hmqLRMGNz-JGD3ZKwl6p6nX0XdSRgSm_HOWUjpgYRXcEmS2UpkRjL8UIiAusHh6RRltggndBU2KxvsAIOdJO8yGfMwIl_rxalYJ3JpBXmreJ9YCL7CHkBxI-BpYUGK8ZH9NlZaMElg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
با اعلام فابریزیو رومانو؛ سران باشگاه آث میلان مذاکرات‌رسمی‌خود را با روبن‌آموریم سرمربی پرتغالی سابق منچستریونایتد آغاز کرده تا درصورت توافق نهایی بااین‌سرمربی جوان قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23434" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=V5jrBShSYe0JNJLAxmx4P9sn_GV2J-FrHwaqbBKQayi6t9OfP61m5lnuEfFXnik0xIHRMttV0DfYOuf-jqPkI6Jfhd5e3xShwXJCteeT940Dhm8EOw6hnRpOxuOfriiaRzFaQtlGSc49wD_x2UnGSL8SZr9MMxEgbGYWGAAkP8erzxRVPm5nPJrW3yF_HwDr9ByIuga7Sles1i5bPuqey1FFL1Mx1TXVWZoxgxgJl6ghEpRvpbpZE3AQTbfA-72aQwEetf-01AOXeta-Wsn0nnC3vgpFdz7p_KLIdalE2XtQ2shAqYq5WfxlEhPRMTWXcEU-ZxLr72Z_wzCv7nEF0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=V5jrBShSYe0JNJLAxmx4P9sn_GV2J-FrHwaqbBKQayi6t9OfP61m5lnuEfFXnik0xIHRMttV0DfYOuf-jqPkI6Jfhd5e3xShwXJCteeT940Dhm8EOw6hnRpOxuOfriiaRzFaQtlGSc49wD_x2UnGSL8SZr9MMxEgbGYWGAAkP8erzxRVPm5nPJrW3yF_HwDr9ByIuga7Sles1i5bPuqey1FFL1Mx1TXVWZoxgxgJl6ghEpRvpbpZE3AQTbfA-72aQwEetf-01AOXeta-Wsn0nnC3vgpFdz7p_KLIdalE2XtQ2shAqYq5WfxlEhPRMTWXcEU-ZxLr72Z_wzCv7nEF0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=uT5O-975BTC_yEi6vkEozPo5aGJHTBdQuWwSFPEUlNTgVg8AKiqOB543UKpoFx2MEnI9E5MEYCuD5P4gxigZ9YDyH_DCVl40Z-T8FRBlzyvejlpGqnjZmSpR1tkIc67Z_w_rrmbSMuQTIYjK3a0rISo9f1zHMsDIyTbZ3Cx-BFE3n7xTcCwDsN9nUS7h7HjDM6ourJzMORGZuy3foJ3iHpado_CFG-NU4eVqL8FpWa-PSm7084XuL_vWtvAsFhHZRj0odbCrDTlLeBhgYAtEWymhwH65G9cc_YnOa12NoQlD4vT7n2y7WaXfbAcfwyrTrAFS4kar6E5ajwVgWpswtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=uT5O-975BTC_yEi6vkEozPo5aGJHTBdQuWwSFPEUlNTgVg8AKiqOB543UKpoFx2MEnI9E5MEYCuD5P4gxigZ9YDyH_DCVl40Z-T8FRBlzyvejlpGqnjZmSpR1tkIc67Z_w_rrmbSMuQTIYjK3a0rISo9f1zHMsDIyTbZ3Cx-BFE3n7xTcCwDsN9nUS7h7HjDM6ourJzMORGZuy3foJ3iHpado_CFG-NU4eVqL8FpWa-PSm7084XuL_vWtvAsFhHZRj0odbCrDTlLeBhgYAtEWymhwH65G9cc_YnOa12NoQlD4vT7n2y7WaXfbAcfwyrTrAFS4kar6E5ajwVgWpswtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شهردار شهر سیاتل اعلام کرد که ورود پرچم‌های شیر و خورشید ایران برای بازی تیم ملی برابر مصر مجاز است و از ممنوعیت‌فیفا پیروی نخواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQj346k8mVniqfS6rx_5Au64zg6vpzSfHru_HBZ04S8OnUN8FlQ7DkU8ko6RgXLjWxPvP5BSNhuZivGZ7bcE_2luo6A0psOvwBqhY_3w1pqU2rrNoEG5BXLcJUpfxz7Qr-pa5K2M63m2wrfXVdIFfL0dnzakN2_hgh9-ytaSxDjXLX6RQX_Gb-kIaS1IaJfFIuK36gv3GE9uzesnNDCOjt_WTPSM0-xgxO5F0LuWqojeQ7tPGMUaOfxWJC9PM7Z6ugFNM71AqDB9tZmaDjhN9D8lz5B3sYFGWeTwiGCFZCit3Z532k0Fa488UgK3KsY-0kRLk2CkvA7_UOHLBRR8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6RwbHU1KDvIUjShdJTmEstb1xt418AbD9VIqNCc6t3sliIj_8rZoJhoXZEl4M22MmyphlQyUIwzZEz1ObAY-y07MhxXyolDUAWjGgtwTrvnWx056YQMdOu4xxEq2CbijTqQa4hrHan5GXjuHGJa59ltQb35Adq3IPRrNVgMwz9kszsfUWCPPUinKPUDWQNgwWx_VIeNbFFQ0JQ9qZ1ljozsJsBJTGoW5Yv2eXS20PTAVGcmoc5tXCJDwBPf5jctWxNCWMTB_DCkXxEfNRRFusguFG_KLiqIgLl9hEHlgcBAjRkOJaksdU_OCIxwqzeG0rZV-u1fH4550_CIM83LLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=VeHdP081_YwgmeBVLrtF_I5Opwkf_cBKFr92x-wzI5mDy7NEjqP7bLjwYGS48UQcmwUU8rvKPfC9htzVLe4u93axngFUJY67PrVgf_PiZ58oJfQF31weXf0ADVV8srW1HiWVdHxFW1yErkjGLk-GkbugHkhIARzOk1IQ2izyaDBzhUeIPaZOds4ZMRQJhvXKbRVKZ6WsewORKk9x5PW4pjtZeYNxHyv6H6sZqLvQf_EU2cT6nGrImxipQ_L_drwR2-oSRPqIWv8CKn5ia5NXoOqwxf8PolFFoxJohvAHVmzBtLlVaAbpddMaIeL9Qu_dUJhIJl1RBL-A9PLKxrV6fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=VeHdP081_YwgmeBVLrtF_I5Opwkf_cBKFr92x-wzI5mDy7NEjqP7bLjwYGS48UQcmwUU8rvKPfC9htzVLe4u93axngFUJY67PrVgf_PiZ58oJfQF31weXf0ADVV8srW1HiWVdHxFW1yErkjGLk-GkbugHkhIARzOk1IQ2izyaDBzhUeIPaZOds4ZMRQJhvXKbRVKZ6WsewORKk9x5PW4pjtZeYNxHyv6H6sZqLvQf_EU2cT6nGrImxipQ_L_drwR2-oSRPqIWv8CKn5ia5NXoOqwxf8PolFFoxJohvAHVmzBtLlVaAbpddMaIeL9Qu_dUJhIJl1RBL-A9PLKxrV6fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNXLz-ZA2Zg0097D6FRo0cBTgn22ljGjt-a7l2BLdtj0FEHIYuown4GtxUaK6HT-diWmu7-z_BhiCYr2Zx0r8A_BYMgXWkmk4_kDa-DupsF6uT5Knjw3f75vb_mH_t_OWfCGCjxWr3poaRzSrkFr0f6ZItTvubrl-cjQsHwLg-NptAiz3eyq5Zdh5MGIo8BkyC8bgNmfu4Pa8f306wXLKDXtw9nMazGDcQwQoMAmh3Xx-ebrH9qk9fLgFo91cVX29uUJy-k3ZucpxStRh49eSSavbAO56XoR6FB0vd3BVftF66u5yda4tKD56qVTA1qrDU6FqFDZhWBo3NPiR-adVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRp-imXv8NIZPV5_s0uGku0MtV85jubV1Pc72MCgFpDsl7ILq3Z6d9rgdMp1bmxxFQHdHbw10uYxbgYruRi6m0zqC1CvC0rnPrwPUZcNIVIu3-Lg6vO6xWbfGzC7AzFu2r0QXQlGl_7ItR9ypLr5jTV51vRXQm7LZjBlUaAYx2ZB3MX7Ri5OqQGTS_K5I4JfiTM1Pw-VDa8wbFf_4BVoF_1qMIL1x-w4t0rYKVDx2HjcGsm33-T_uUV1kDh0sOmjdfaFJk9J3Pu07XCdS1joyghaLDe0FT-ttFNsR0eflRWydnXMQDRQI56Loqe-BEbBrYbHuNrc8GkNA9m8bjsIzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGSnf5aB0eisU7jwyqCoa2mnL5ROPpg6tnkWGbbX4btxw84AjMpn9XddnsC0FiNXJV2MyCG8lazx06z8_hfvyEpTo_DZLeYj-n-2x6OFTidNp5-n0gls-lIZt9BseFrSfFxHwk6xVCQyLLZOb4ZHs6td-bQI5Q9zw1bBvRoSRSGsJ4DTckHqifD_JDRau_sHttfSFRKymD-DyCWy1vwK9NMqUvVuGKGw1LNtkD0E1XJu4aMkZw6KWZ-T7K_knaHViFWRgwqbeag7BmpATJdOQUwFAKSAlEHiBqGifyTQwbkWgxr0TchccBblF7yY44vTuNLzlAYu5xOmXIZv8-Eqpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItGEh2B1gaxOjQwqozZX5P-kwyGXRo6xAWYggVU67Wn2B8yOIq22nowSJLJBKkHpuGB8JQCSeaTANNZCK4SzduNL1ykbYOE82YKLvBS6mSTiGFK3-nEip-2hXeg22lkMR6-OEKvB337jdRY2EExXjAX-WHxewou27vxLb4D-nXBUDvVj6gCHG0cmE5PlVKPTTnglhqrGosCWtdfndnycPI8FyjYkCEG1ICkgVqB-WYQoeZhw6vNNFGjfOxPH1ZYAM_nDzX4OXtqGYKoUd-BSvqWHIFFl4KNRiChnOGOOtLfHPQ5qDRWfbBRRY_EwDq5fvejtQVqjXHkXZTU-bO57hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZzhKyWpc4Sz_zvsCm-u2zTSQipzTcOGIfyoxC0v8mwzY3L9KsJWYb08djzaqaASykwgojupI8RWCiQ7KHj1chJNE-L7FhTab_C7WO-4fBprvJ50ud6vuaAiiaeTLax7c6aDlYagSJG5RNT3Ibe3bb6hOZ_th8ZV70Bth2XWYbjDgZ3nB_fiIEXm0X6eAVhiJk5OpOSNHaKEkHgcSDguzf2BdcTEqOF4uirosaXx-gig7w3Zh6BdCxVyRLqO-u0ENHsW7_TXykoCfLlV-pUPfc-4v1r2-p7Kyxh4AVWCrp0rkW_fPMVtR5oE4qOCO5Qc1RaBcfC3uQmXO3CO3wFfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpDx2D0evrwIxJDDqheHYivu-GA9aAVChfkKyM4Hin7airCpF7Zm9srF91H6DROxWWo5hwJKnRondzJW5yKDYzATDQ2Vb2PHP8-vjgvCXCRxC3-LuO3dMVbJKRvCf9O952NMho_sSFRCQSWld_BY6eir6GCwMVbz6ZNP12-J_y4OAEnpDOeZBXkYudNxwyzRUl2h2xmkUplBLsd1CTjU8aOnShPUmWhWGnKxRDsDxOlyM6Z0BOJzR0tDPGud70brk8ff0kFkjUxSPzUDLaaIdr2012OOXpx_NDFoPjaGAra6nrvTUpNJqhCyI3X85f1XhdfZBLDNp1LpM6utAVOTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swi8RcPkHYgRvDOIejd5slJpotiEj2p2ZywNEXyRjzvmuR89qj9n--xmFKRp-2E7-JoKG-lzEWNvVP4presdur5pnu9-QsXkRzEBDSxtkP_kxmkPb-13zKl6S0VnE84VGI6pSrEyIN1kdQPr5emoVX007UcpESX4IXNPoV-XhYijajsrZSBTcUA14YzJoIPgrk9IabejlSBm-Y0Eod5wAV7ax8oKsP6GTuXCAb6UITkrEDbZM1yFZ3R42YInZmDYOAPMQuU7W9uRadA2EKSmtq1Wfhg2yRn5sxLcyA9Q1VIfPzs4nEMtV5UfhY0RjlbALHcpIegO438h1sTBTEK1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hP-S9cDBbimtrEIO3UianrUEzArLpiOBqDjbMKsM_4nClWjzjwj56VgOE84uIdZBX_DsrE4SRUbm5vrsqsBE2RsI5DeXwJcq1e7QS_RFpCWDg7UuU9k_GEYrdRjsYcO2Ofu5zyT_LKuw5f938RXbjazyPlddawjIlLC2NiNzLbi-g6vgjt9im-SidNopRhE9lDCWJGx9bA4LOWD6XuGw_Snr9qW4b0yRlyIa3MYXXUcAsz28YsjkKoO8lmaGuUo72Ev2Vsy0CCXxxonRiGL90coy1LQlk7BgtDAtp5xY1tlBZIE4d0JeA14Of7wH8g_DIcOKfmP5AeiQ3KQs-HbONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nz5TulJUD7dn_9S2p50INKBjEjhn3q0AtCmhPD6p4eAfhG8Sb212-aroKJHIx8fFffJClLblf-XW-xBE5MxMeofUGQJSRvOHN9cG5cyDh1e-D-MeZRvefavkWq9nSyT9qsq1A8ipH7xdHsvb9mfnsRwil5yOsGc9p7nm4B-QKFMPIT41ob4qFcLzVHGXfhqRyuRJ7ktptZYnLL8o-sPKzxXtPBvHC3_ai5nNdZ5iaSn3vJldWF2fIl3IhbNMuC0CoL28IufLw9gPis3j4fYQVWY24ICbCuDh5tOsN--u-R75JJaPQ4d20yeLnvU7sj3Oq16BTetSr7BLcHrJIlZ5_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCKi9tZ7e3GVD0V6lYrO9WWQa8kust-uZBhyLkgWFI49HHZBpNsT6zN0G-UmNJ6yahiFWOacdP7tPIj1YuV7I22p14pa6cehnvly-PX4La_2yMloKyHYkwOLhNawYZoFhRhpCbuMKkqkY46ORp2Nly2vgbkcsS7EWTGyWMzVSo2o_eeYTqURUJxA1TBMyLRR-nleMtEUwYWVAWvpO5YxMq8XHPmLk6dObcqZxFNZfiHLpYX2BWqMRUgyQNT1_XO28LUZ5NRnQBfwdoVwdKuA_rRb-po43EgqCYW7DStsrKTRjQSyeniDdN4RJSiRmue3Y2NVoZuTKvhFtFJpZH3dEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=ZAePhZ2cVsLSmDbSI65wDQsO30_-Wus09a1oi727-uZGHd61WARdJ2x6l7rdwxIi855q5ylGh5zi6BDHeqDaa_fKXjJd74Epfqw5moXDXWNOV23cABW89kfEeKuxTYF9um9LttE0tHR9QeXWJ40-wmbnIWUTaRfqqTb1_CKuQz6uxwiPsOOd_TPIaFOQOir9qH4ecfm1xm6mQ0ggvUTJnB18QqoSoXMDzJiFEcm67BwjW5iSJt1mMKsv6JFoZlcJnS5fvZWVqcfvYScy_JCgMsaBle3VLShZoz5cqyyhG9PYnQWqLZGBbqJGCpMdn22nPtNDMtWCQmhprwhX-nClcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=ZAePhZ2cVsLSmDbSI65wDQsO30_-Wus09a1oi727-uZGHd61WARdJ2x6l7rdwxIi855q5ylGh5zi6BDHeqDaa_fKXjJd74Epfqw5moXDXWNOV23cABW89kfEeKuxTYF9um9LttE0tHR9QeXWJ40-wmbnIWUTaRfqqTb1_CKuQz6uxwiPsOOd_TPIaFOQOir9qH4ecfm1xm6mQ0ggvUTJnB18QqoSoXMDzJiFEcm67BwjW5iSJt1mMKsv6JFoZlcJnS5fvZWVqcfvYScy_JCgMsaBle3VLShZoz5cqyyhG9PYnQWqLZGBbqJGCpMdn22nPtNDMtWCQmhprwhX-nClcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برونا بیانکاردی پارتنر فعلی نیمار جونیور و کارولین لیما اکس میلیتائو در ورزشگاه بازی دیشب برزیل
🆚
مراکش درهفته‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RatcbpzQujycRU-xFLS_sp7FlNvb43wmQxdnSC7QSOFIXBaaSSrbAG7uRqQBV_Tsa_HfTD-xEZy8b7hCBpWToUatvBWm4aZn_s0D_HyqVzzBVTwblEGcHjq8EyVk2Ec3nuF9Cvg6gxCq9jKvgNZ1ydu-IZg6CWA-xM79g6NOdOq_ndwuHbk9HS3WMzKTYJehlYskEhD9eqt1JRXERXJetsUECb9eVkpKleR6e4eNyTUtsttZ3ef7KtvKZ8b9IqSHki7JvuDm1rpV305HvcNWbiZItRFXulBJnvOx54RkS-FRZUseP_wtfGUz8qoRscROfU-hbpcpfYOEBlXj8ISiMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=LJ2958kH2xwr9KVNxIE24k0dKSkG2GmvRu1LR1mpoOr0TgfiwSQ939w-28MYiae9hfuuxI2XY5LVDy_cTIHizSqqSHezSSPfLX1_zbRwOxOQPD2R0tdTxfeoDZdPtWXfW3r78hMU7WV7zqCAvnAsaziNiNKTU3yU63jcZ0GJIwcPYnyXNGZSBaxBjzZy6G05Vdnf80hWNYj123j0atLxuLnUO9Abo4y6Zv3t8a8e9uLpwkjEKAQNWukrjQ3CdAahZpu2nf_wI0F0XwZjgDuJKzwod-8ShRbM-_9-kz5u4YIkG7_n5ZamiCr17QogYPPdmgTs65LfhkplwvdxjQ78GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=LJ2958kH2xwr9KVNxIE24k0dKSkG2GmvRu1LR1mpoOr0TgfiwSQ939w-28MYiae9hfuuxI2XY5LVDy_cTIHizSqqSHezSSPfLX1_zbRwOxOQPD2R0tdTxfeoDZdPtWXfW3r78hMU7WV7zqCAvnAsaziNiNKTU3yU63jcZ0GJIwcPYnyXNGZSBaxBjzZy6G05Vdnf80hWNYj123j0atLxuLnUO9Abo4y6Zv3t8a8e9uLpwkjEKAQNWukrjQ3CdAahZpu2nf_wI0F0XwZjgDuJKzwod-8ShRbM-_9-kz5u4YIkG7_n5ZamiCr17QogYPPdmgTs65LfhkplwvdxjQ78GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgCJfKy_oHgnOgevA9TKhi4sEX8CxioeUkEfYxBn0VLqwOd2yoTWwsgicx6G8CmzAZsYeco6kKSJf-2142OqkXPeI42ZbGIQxrEqGwlGR4vKK951X_U-fx5xCyqtP1N4BRO783ZP-BXEIH2H3C11PCzkos2kZgZcmq8VLdS3uPkfq9IDEUShVJ8EuNIlWT9PDfi4S0t95tGek8cBeJKb6F0XSvhISsLWqOHtv78j7fQFqEMcW6W64K7CUH3rYKb4LizCvM8P2XooZQPFCpAXas0s1aZpHIPzZgfPWuMrNA6XZvf9nfEMxsqhvJr5rGl8Hq2yrMqGigCcJG-wOl_nWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=O7PYS_v6k7OLy9iNnvWP2h-xxQLhlLi-C2vyY67Yuu4iQINrgTQ4UXRKBDhv204ME2ayg9LDG7Ye507p9jQ6W-LoLnC9rRM9cnuqIndykrI4cWE1Xyg507_KBpA4dAk8fOd9UKHnr7xTvRYqzBKecNnzhSHsGjkiyaR4XNGhbfe09FietHx_k6y0BrHymm2sKI6ose81LbW5m6fActvbxJyXCa5RTsyx_pwd8aDZUnSBCb0l9SEBgEX7_9E4MUp2X_It-L9ThCTcHC0_pPmJGjp-DinQWnDhfzAw_IJXF5AMOTQI7TULvfDfXrCOuEDBcSnkCbYgCGy0_ihWH_nRsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=O7PYS_v6k7OLy9iNnvWP2h-xxQLhlLi-C2vyY67Yuu4iQINrgTQ4UXRKBDhv204ME2ayg9LDG7Ye507p9jQ6W-LoLnC9rRM9cnuqIndykrI4cWE1Xyg507_KBpA4dAk8fOd9UKHnr7xTvRYqzBKecNnzhSHsGjkiyaR4XNGhbfe09FietHx_k6y0BrHymm2sKI6ose81LbW5m6fActvbxJyXCa5RTsyx_pwd8aDZUnSBCb0l9SEBgEX7_9E4MUp2X_It-L9ThCTcHC0_pPmJGjp-DinQWnDhfzAw_IJXF5AMOTQI7TULvfDfXrCOuEDBcSnkCbYgCGy0_ihWH_nRsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3SzicpqtuJSov22TXqmkGIoN8pRpmMPMQIFpJNGIRQ-H-NZDaA9gvrzGCaFwTBjhOk_wQsEYtzJYdyOXzM0SHq-m0YyQ78TSbIKEP0xXOpmH1RSHLTpkXbuEuMkr6IlzkayM8HL8w8Ko0v09GO8O94mmonlQZsDaKSNZ7e3E4xnaZYCrXc24NqFoZ4FzqdoEoqEjCIPOcJphisV-Oviya6O4qkxDepFZz6ABnE97f3TcIWfhSIs28QS5MX4wOwT2pYqlopD1mnx71dEc2jq5Oeb_-1d8R93eclNQzS6v7yZeWrDvf03dxnIU0maAudbLq6BDf2lc7ae5B6vsIR-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jzi0maD1E2NyJk6GSL7Jhu_6Qg3EydVdfG_zMpu3LNMvrpNMHRz2nVAWFvcbEYxWrd4ARaolPsqk2rL7oRLdQSPn4CJI6wq-KtIgcs6c9HKcHY-AvLsN4mCxZkxg1j86iAvvaHZEZF5AZ_cT0QeRam5QbRRs3uS6k5qYmZ6__eZWxPH6EQ95_L04IknGB-EPknKaZ8WMNtwiJXxQcwC8PUJUHdFFxh1l9NsMolvu-MufiC-42eQ5L1cWvhJI9d2zYdE2ZZ-swJEPmd3KynPgvMqiGnHIAQGAhvVzucJNRpzWUIXB6VZdqjgbA32--VdAYgHB_qTSMmyUwPx-nTYnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=aFQbeQnnq7lxYAfF67jVsAvluF2KbNn9O3LmvQJxZ1Qut_e4smokwPvRQvY3ZO6MYkgWxdtoaFOflSU51HdVdSbAOOmBmv4FCitBPupbgvJie_Mjl048twE9FGYEsZ_niBTQTcJPoCyC8h18OxrztlakWQsWa0E9Bu8duBN-tnDQSWEah64qQp_dB_WP0eAKthkwctkecmJ_7L0l3p2BSNas3WxwobtZOZvBYU9uT0v4cyuQ7BbG2XWX9QLfu_3BxdnTMjdNQBgkN5Rg3BlRqLaBapcSvidwUrAUg-vd23sheOIlfYf_nDkKlIgxV0OyVYEIXr6ZHUN_W4DditX_tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=aFQbeQnnq7lxYAfF67jVsAvluF2KbNn9O3LmvQJxZ1Qut_e4smokwPvRQvY3ZO6MYkgWxdtoaFOflSU51HdVdSbAOOmBmv4FCitBPupbgvJie_Mjl048twE9FGYEsZ_niBTQTcJPoCyC8h18OxrztlakWQsWa0E9Bu8duBN-tnDQSWEah64qQp_dB_WP0eAKthkwctkecmJ_7L0l3p2BSNas3WxwobtZOZvBYU9uT0v4cyuQ7BbG2XWX9QLfu_3BxdnTMjdNQBgkN5Rg3BlRqLaBapcSvidwUrAUg-vd23sheOIlfYf_nDkKlIgxV0OyVYEIXr6ZHUN_W4DditX_tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spNklkXQctR_s6KPiZLkeilSxBSyW1Oajwj834qBcqFXJwqL2LW9yD0hW5o20ru5R7kOnSKcHcPwQdKKRiV56hRfhVIkSXeHSrK0r_pcgsDaxqxTky9l9npVeWefhCkICVvEvWkjUlYOMZ7VoqV66TeSIC6KB-NfC-V7AW3joMEgxBKwDry4FxH_WW2SWWXSLkE_7mI5EiQ6Xy-Vd1CxTXASRnmOTkXEyUKP7kwZEOFaMapRf8kdiJOJSOJm7KkhM1NuLnqZfdc4YwIjw48St1oKyw31XxlY1NGu8UxhPef402AYH7P9bHUwFOo60unn637ilgurtnT7K62D2TjBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUiJznm_xJ60RwSYLItAvEr9KHdicsBXQYoUN5ja_nvUM1oZgo8lD545Jvzz5wCHu5DRmFOn-hvSTqiqqQ0tRfhm-FVUVNSFTXn6n9HzfW9X35ii7xAm3LU9uHyZELRbDKCUh6wbzqVo4pr5rMs-WubEKX2uo3tAYUtujp9w72c4nQz6dP5MgLqROzkwTzRN3oEewe_X_P80WmQ0eb15KZEt8FYho7aMyHLFVSdJ3Vqx2BEWwDXEuPDMVjA3vJp7E2z7KYZBSq4REXvOyJbmI68FO0Vhy3CsBXgtC4mjJTFJ6PsCaSKI7KlURYhYp1Isit2LLs82CRKJoRBfgLMFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwP-9kLC23WAjA6ZjPERhu2_iQFf-yAqXIkQkdGXjVSigHGHx74qHAkL9cQbr-avw1ZRM13hkuYfDoJaY-MZb3oX6tx2aSJOGm_c5zFfYvwYkpJetTDu4-WdZkWdc9gOTookMPjDlty9ow43dfkDslMC0hqNtHvYniQ16mFCQkJZX6YTPNvbca6wM48i-1UB6CdcOrXRSPKyroZB65p0Ci5ByeS89HaKpXQWjs7O7OhoLcUZfrjhKZWrTCHBWBbPEMUVQ7o081O4ai3QZznpQV5DzqxBmN9QRf1bcNmI9ZpiCHa47Qebp3SO-rM2iwiu-2UFAWYMx1zqwjNJDxhAzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=QxsHAukSczCUQ-TRt6bFYvlYuLCmHXO_h1CqO91XXbtcisBd2HW_1y_O5p5_BhoUwmvhcXHySqA2-rKl2A_oa16NOZlVLNIab5uYJSM9U5jLR8VYHCqQWjMQ7LSm5t14-dlTEmFppT8oDaGqHkE8-hG4gkUWHa4-0NUbOyhTpOE8cYqxlfCB8Px6ZILCDCF0YK9oNCMUL2_kYt7gWwWZ7sJYR5PZj_VA5IGjFg-jOTBqV3g5DsTQYc6-2mJ90eVh7i9xPGovuuYYl6uf-7r8xoirmMtnGarMWh2WzPrKLO_MjSEkEInwQP1V5PDvoL9BJtzooZbcVqRPo_qV3NUAdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=QxsHAukSczCUQ-TRt6bFYvlYuLCmHXO_h1CqO91XXbtcisBd2HW_1y_O5p5_BhoUwmvhcXHySqA2-rKl2A_oa16NOZlVLNIab5uYJSM9U5jLR8VYHCqQWjMQ7LSm5t14-dlTEmFppT8oDaGqHkE8-hG4gkUWHa4-0NUbOyhTpOE8cYqxlfCB8Px6ZILCDCF0YK9oNCMUL2_kYt7gWwWZ7sJYR5PZj_VA5IGjFg-jOTBqV3g5DsTQYc6-2mJ90eVh7i9xPGovuuYYl6uf-7r8xoirmMtnGarMWh2WzPrKLO_MjSEkEInwQP1V5PDvoL9BJtzooZbcVqRPo_qV3NUAdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptlRj3RFzgN_RIrZ2OIvV3Fe8t6pv0m4N6GdSC-AIN_ctgOjtDlgn5CfwMuykFIansmq0rIcR-OKc_rAalum1VLeXG3yPEaLf2C-3b6sIUYF6z4TyLcEPO68GpYtHckGykMjC8idsy4do0a5s6dVt7111PSiVeAj6YnXt7DM435bTL5kIAFQcjw4KFdbux8pKcqq8N_N6u01c1NBEthp_X7vYIl0FTaRiQrHaSmIeAUuBFDoTfLYhhD441IMaDeoYXG5T9X1UCJW7DESfsoIU1BbPiA0DRGuYNcF1qSZ6SUKAmT5LS5pk6MBL4oFWg9Vxx61cNlMQ2SELdmfYOIwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=eVjnIAM__KYyUoocYaVwuQM1fuVAViR67kXpXoWwSOndriiGeRnkwLHqTt8TrQoYwX3HLhscBrVNKKIspyOip48Q6vzJPZ0nVga_f2XqRN07AS--4kWbu0fHQmkYm8HPBc5h_kr5RSBAN96A1bcB6hh8x6XwGlBGbpbkIxozEOb9U5hJBYiQ1R8LdpxP0LlA6wDygn8bbZEhjdZhrzVJlbfDMWioD6PRwFNPNg1zDEZm4E0NpTo5Il_7R7anaIlW0SqnALc0zVW8V40Bu0RuiKseHQmpNVA8_mS-PzWPHDCce456c75PKWEt9nunYCVZJqUMK__ay1GeIThqls8G4hCWnKJRLspEKu5vFTUxzf8EH_4h_fa_OVpqjmGdYUx935VZLSMTTvxfvvbylXSQzOf-pLuJBCIqwttsWbSJbM2c-NwuKoLnTRxxcy0k8NAOjAf6cIVvmJeHkEZ4bZMbGa1UTewLXT1okYZyg8qFde7OqLJrCNrKq5d5mmA5D_Cg5tdF6BZFeIBl65P0LS2exuNzMk3YXQoIRviyFWcOQSrVY-isd3QphqR22XwBx4nb6d45lq9cJ2DrE16w0dvJjwAK8UmF0DuWY1enEufx_wy2A-qMzMlRqjaprRFWqD4NG4FY7M1eNgzzxEqQtwJXnS1dsoXUuYYu9vq6FVs8RTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=eVjnIAM__KYyUoocYaVwuQM1fuVAViR67kXpXoWwSOndriiGeRnkwLHqTt8TrQoYwX3HLhscBrVNKKIspyOip48Q6vzJPZ0nVga_f2XqRN07AS--4kWbu0fHQmkYm8HPBc5h_kr5RSBAN96A1bcB6hh8x6XwGlBGbpbkIxozEOb9U5hJBYiQ1R8LdpxP0LlA6wDygn8bbZEhjdZhrzVJlbfDMWioD6PRwFNPNg1zDEZm4E0NpTo5Il_7R7anaIlW0SqnALc0zVW8V40Bu0RuiKseHQmpNVA8_mS-PzWPHDCce456c75PKWEt9nunYCVZJqUMK__ay1GeIThqls8G4hCWnKJRLspEKu5vFTUxzf8EH_4h_fa_OVpqjmGdYUx935VZLSMTTvxfvvbylXSQzOf-pLuJBCIqwttsWbSJbM2c-NwuKoLnTRxxcy0k8NAOjAf6cIVvmJeHkEZ4bZMbGa1UTewLXT1okYZyg8qFde7OqLJrCNrKq5d5mmA5D_Cg5tdF6BZFeIBl65P0LS2exuNzMk3YXQoIRviyFWcOQSrVY-isd3QphqR22XwBx4nb6d45lq9cJ2DrE16w0dvJjwAK8UmF0DuWY1enEufx_wy2A-qMzMlRqjaprRFWqD4NG4FY7M1eNgzzxEqQtwJXnS1dsoXUuYYu9vq6FVs8RTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=tMWuVhrhbLPd_H1hVhkYsZ8nWkHbJOlM2taLS_LCfsEAzeJx2Y7t7vHjlXD4Exr0Df_-9YvFNJLF08KmDOgMUU7x-b6rMJUzN96zzRbiwDiKdIQ-uiObSaLmg_WCfdOjlgIHu5m7flLF0VohZ-eqj9xBfv9yYTcefg4orYfOCvtDJQDA5E_ASIVGH7n4ZxNFQBlSKvOcOtIl9hlK66cgwMP5MIcYgJW-8Be-P2ItHnlm2sLAfmOwUzFunHIvc2wuqWBPbiQB0zXnWF9nz-Lr1Rn--5Y8W4P6AnUI-PbkJFBGNdNxIdz0JJVw4_JvewmiPwicSoCvXvgsSPkKEgsx1UZpeN0SAGgB-Z6KulRGRNnTBCFe_bDhMS-JJ_6Oeb0Fs5LX1hZxRgfXxieiYXl4LYN34t7RKdWaIQDnBZILeXueuH_2zb_LyQQdD1I_OR9VF0ksDCvDjXHkS7Uvh8UFwLxiVfO9aoNgL7obAMNDBodAgbisoiIXns7OC1HTrwYDvpX5sKb-aAJ6CG0_mRYgvWyYMBgPPqmkMHi7HgFsUGFi1gZBcz_vJByzDjktsFhnRty2a9J4IftwxDmhyaD1dslQiwwMLIq-6b9xQOmVh-b-tk-orcYGcPK_UjYONm-4xc7DWikTrWr79nJDtDIQLwIrx5-sJCz2e5lcFMDr6g0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=tMWuVhrhbLPd_H1hVhkYsZ8nWkHbJOlM2taLS_LCfsEAzeJx2Y7t7vHjlXD4Exr0Df_-9YvFNJLF08KmDOgMUU7x-b6rMJUzN96zzRbiwDiKdIQ-uiObSaLmg_WCfdOjlgIHu5m7flLF0VohZ-eqj9xBfv9yYTcefg4orYfOCvtDJQDA5E_ASIVGH7n4ZxNFQBlSKvOcOtIl9hlK66cgwMP5MIcYgJW-8Be-P2ItHnlm2sLAfmOwUzFunHIvc2wuqWBPbiQB0zXnWF9nz-Lr1Rn--5Y8W4P6AnUI-PbkJFBGNdNxIdz0JJVw4_JvewmiPwicSoCvXvgsSPkKEgsx1UZpeN0SAGgB-Z6KulRGRNnTBCFe_bDhMS-JJ_6Oeb0Fs5LX1hZxRgfXxieiYXl4LYN34t7RKdWaIQDnBZILeXueuH_2zb_LyQQdD1I_OR9VF0ksDCvDjXHkS7Uvh8UFwLxiVfO9aoNgL7obAMNDBodAgbisoiIXns7OC1HTrwYDvpX5sKb-aAJ6CG0_mRYgvWyYMBgPPqmkMHi7HgFsUGFi1gZBcz_vJByzDjktsFhnRty2a9J4IftwxDmhyaD1dslQiwwMLIq-6b9xQOmVh-b-tk-orcYGcPK_UjYONm-4xc7DWikTrWr79nJDtDIQLwIrx5-sJCz2e5lcFMDr6g0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmbe4hSz2LUXFbRf2-PkU9-6FkCfBYWxbicwPHVvSTONOwmdflrBPUb3Tt7h-7tw_PeCM8tijayAKkS200gAdaYO-PaduiSSBJQQ9oxywrIbzYHzzAObhU207DG9NRDawt8rTnJj9pn7Ol2wXNbWy7k69SKoS0xa_KEL9MFweXj3Q-N3U4NbIY-el2mToVUGEKb2WjFxBIFUMIGHi56TRRzCvyJWMBWIqJ_21vIyUEsIGPAkz5z1cpEezyczOSdQQuGSvao396tE8V4aTT4iHwJH9n49wFE_XKujFJcfRkNBABBGXC2cYUZOI9uaC9cM7EkY_om-7YRvIHCfBESfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbkQ3DV7qcHUToa8xRVR1giXgwQFnAVYCZg6LaU2sV7Djsd1e4Qg3FBMxhMqQEBoqnk76ZbfpJv65F1SU4HT7cCFJl2QEzgLIOJI2cbCkdf0yW9lzTqBc357LXkDmh9tRVrmM1_BCTW_3q-woPgbSrPhU3rYte-zbibrarkcPLvCWMTaon_MjF6c64sTZPnBpzmws2gvchqsCgqukncz8b5uwlhT6tmxZWdNeABx3zC6jVD-2k1pmZ4R_ATXXYXbSs8zy0Dp6fijmIGfo6Uw98x6vwibAgfg_n7DirHN6OCFFbuDDal-0ONRpIW616BNLyVRNkoGraObtPID3nN6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gv9kRH5JHCg_EN7tMq4n8jTkrzCImhq-Ha-6Pb5nMnEWkPh2crqSWhUdFw-HraHZprjusdUm2kamz7DNlQsxptdDgjaue7c6WGc1SaWbGD-0YmIA9M7vJQBkefE3PcrPnL-x9bJ0ICgZvLiINbyQI-yBmlNtt1Eg0ntO8BXEhTDTKbkNbfAHfYzsV6YTQ6rGbddcNNgomD9jscBbNhLrMgjZNDMQmgPndlJPFtWc6zcHS1HEG3kSbOW9ssuT9q-854MWxYP8fZx65hYDvXZW2Jsn5XEeNv7cx--DxP4rv6XYKhCDyDFr6FYf69dh3inwLwRkIg6om8c0ZYSGk8K1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-QM4nJLHdXDTMwdfEAedSp8fhJ8lw60h2w0y71acDPZdtZx2VD5Ntd10Er_v3QIyWnVYbfKYg8P6QTrDGRCyVE_GydlyIrHHletsi70jH8YBKn9E8Y7S_u8ykYQXQieeBUVHvA2rSkjZEzEUNBw52WfO6HKrjOaqG93Xjqbhe3dkGv_K_oua28kQNoZBy8LUxc-H8gu6pMq0CNXIuV9Ih1c6-UXYIAYxDUO8vs_4yIbHEJiXs943PIOXEoVvQBJk1eKRr3b5S8N9eMReiAKYvlUDLUEutLlWn8HnMx3kb9AMyuFvEUTaUhfm418yR6a4RxHIRMFvqor_EMqBKmcoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=G1pwRErVDh1nGq_Z0KIrFKtbHEtwsd9xN7gOIxJTtojPljMP6exl-UG1dHIz_YP-Wa2ruXAR6fDmewEy-8Ol-_Pl3XikFFk6bYSoAhEBEy07r3djsQgBfIYIr0NulPDNuhPyZyRm50Su1wGRsWk-dctjnGTKNJU7tDEV_MTxygt7iGThgPsAG_tqMtlZSEx9i3Lp0pVt8Q64T63AArT8Of2Uyh3j7aAE9KdcrI_HtY94MazFqiIoCtu1Z-W_qDM-BrF9-dbBHdKWFDegnL5vuO_HzPsZ2Zsazv2j-IihuSk0GFuQwA4AKUj5nb3SicAH1ly41NyVKQ0zOXTROEWFrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=G1pwRErVDh1nGq_Z0KIrFKtbHEtwsd9xN7gOIxJTtojPljMP6exl-UG1dHIz_YP-Wa2ruXAR6fDmewEy-8Ol-_Pl3XikFFk6bYSoAhEBEy07r3djsQgBfIYIr0NulPDNuhPyZyRm50Su1wGRsWk-dctjnGTKNJU7tDEV_MTxygt7iGThgPsAG_tqMtlZSEx9i3Lp0pVt8Q64T63AArT8Of2Uyh3j7aAE9KdcrI_HtY94MazFqiIoCtu1Z-W_qDM-BrF9-dbBHdKWFDegnL5vuO_HzPsZ2Zsazv2j-IihuSk0GFuQwA4AKUj5nb3SicAH1ly41NyVKQ0zOXTROEWFrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWotoHFRfkfI0aRaI4uRRzx0v5BmWsquamSnKmIGWbYmrAWWdsSyV5bbn19hf2cR7EZNBPOVI-I6bZchSoJMy6G1J5-zVvu5zBFekMPqZADKlU4A56UI7f-4gmBCnOO4nmYMJ4RVakHeo0UjcKLA1HBCl7F-GQfBP7SwDrTibo-1K3MJ3xxtiqc8F66UhkwV9cFFacfYHcCI9_4VkRH2S7jfFw87uiRGaEYcS2qbbuTuD5cZs_M2MKQUQ3JJ1kZ0zy5DxKDmbxJVXUtH7FVLbrDjtjtr5qys8SPGSp1mjKadM-t3SzI3wVgiJGdYmky12wKEDOf3bIwb1Bfyx2NdTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXC9Mgjv-SFCOKOEVR3HxhG2cbe56G4xT37NpgWTOKm1yc-8BROONE7J4zW9fpqpfMuTZm3f2j-21Zqb4Xd-3sXmBzU7XzXzD33mBvMnaHB_wHbWFfAq6Ww_LV-E4b1Nn4-uzMqkNI2HLb1ylVs5RpDzD1S1J5SsY_BZf4v_4y77oXV72CVUVDuo4MqxpR-v6Yg0s4gWus4LtW0JgoJyGPLz-VQUY6kR1PjbryyAO7rMFbh0rvsYph-bYHdHYgSRehOwx_gq7cAW1WnutEt66mB7cfVJ-vy1NGJLRIhB3kiCKUh8vAH4sqyX74ms-P2iCXSbwg9cvNRGIviWm2RQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2TlXWSy-efKIkmuNotsyLt6o-emKFC3l4uvkMfad64hl11ojH7ikOWYEbKJZR-71T3Np1b4QUirqF6B0MydJ64du71fJa1ODrOtAKfG-X2xP1vKfFC6AqIFiR6uT-4LrmS6W3laebjDbV49CHV9tXcv5yswwNTZ5dZZ-Aijc_6WMxXC5a4ZYK1N0rnUdgm8b-JjQ7ag5_NRFyIJ8Qw2YIvvBwKXW7Bc0uff66dVY4lmQ8GHP2qI5V1-mKJrJurR5NgJPNMQBHi3amol8g8orGaRSavfvco8toZYzAMdKM3lYjRTHyYvUm9AzxA10eNWgZQnvlsw1Edy-R71gjqivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=tZtJmMxRrOz6_g3332EpaWTpN0gIRjULUz_iSX51AofFxpNgIWOKIh49tt4nTE9rWV7cWnfE8U5S2V5Ob28NzVp3XpAelQuDQh3ROaGCFkUoBguYpMsI399cbj7BIxEC135MM75VySd-3Tq9Hse3SymOkwRjuRsdij2-FRnyL-2FCuPAvjfU7LIcwOT9ZFvbuIqg0ji8I6egsPk52uXBacoMmFkYoyXfgW5ejon1O4GZpL5M4MdH2uJ-jgTcqzBxZFrUJA_g3ZP10yEEPqKvQK3idrM3VRuRrP3SlzjC3zv0D34nl_qS_URzNI41ondnU_hlJtv8pjLKb-z2iakTpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=tZtJmMxRrOz6_g3332EpaWTpN0gIRjULUz_iSX51AofFxpNgIWOKIh49tt4nTE9rWV7cWnfE8U5S2V5Ob28NzVp3XpAelQuDQh3ROaGCFkUoBguYpMsI399cbj7BIxEC135MM75VySd-3Tq9Hse3SymOkwRjuRsdij2-FRnyL-2FCuPAvjfU7LIcwOT9ZFvbuIqg0ji8I6egsPk52uXBacoMmFkYoyXfgW5ejon1O4GZpL5M4MdH2uJ-jgTcqzBxZFrUJA_g3ZP10yEEPqKvQK3idrM3VRuRrP3SlzjC3zv0D34nl_qS_URzNI41ondnU_hlJtv8pjLKb-z2iakTpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcLgWWvp1KEXjntJaRKg40X0mrXefb7wzJZK9tM0aRYNt4i2CZg8wUx-SX9jfbIBXWiWRyzhEMByU1B5BP8tfoAeIuDXv0Npy73cEKMpsXoZp1xUnHPUDSkWCF3Q6GGYn8VQlDMlOmFjjnR4gdNXTHtNBfHCeTA5jDTJCD7Kof3_SzSkKYBLfP3SzUXZl_iJB6Go9TvpEXYnFcpEG6ambTSpgR1U91PASxEsdvSbWXoYr2-AXvBwvzTInxa9e5ZDr0np32GQg7vVZGk-3gNDgvdrpqk4pHyheo5IqDyQldnBpCNWWYGc3pPS-X5y9kS8U5EBnpguo631ZDcQxsSrhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=NARqP7YPcyQNqGBpeyGKScx7Q9znGFWKzGzAK7aEsbwfQRuAceE6HZd4jflzAFA-76b8Kwf80wvoIRZ6Va9R04hSv0kebsXJtlpgcioOYHCQUUeYx0Dl25XCTMVhZMthSWMgIE2OBfclAdY-knZ8Q_d7kgO_U3pSw_FGzDKag8-zMz8K3u3rrEfbR8kQbgNP2XcFuVEqE3uy55uHFnTpqYyihZ0g82GK5a7mwFbCtS4W0IYbIgvQcx7SpCoHQkQRBf8NMDrd_LhVSLDt1ALM001fxKqkqY-JZqr_XD92EwMUnkXLv-mmmvo6HWv1a2pG1AXuQmiDFEoPaLBGg4uCTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=NARqP7YPcyQNqGBpeyGKScx7Q9znGFWKzGzAK7aEsbwfQRuAceE6HZd4jflzAFA-76b8Kwf80wvoIRZ6Va9R04hSv0kebsXJtlpgcioOYHCQUUeYx0Dl25XCTMVhZMthSWMgIE2OBfclAdY-knZ8Q_d7kgO_U3pSw_FGzDKag8-zMz8K3u3rrEfbR8kQbgNP2XcFuVEqE3uy55uHFnTpqYyihZ0g82GK5a7mwFbCtS4W0IYbIgvQcx7SpCoHQkQRBf8NMDrd_LhVSLDt1ALM001fxKqkqY-JZqr_XD92EwMUnkXLv-mmmvo6HWv1a2pG1AXuQmiDFEoPaLBGg4uCTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCZFXvdv5AwNB-axSKEvcgnvdn5L3sJECnjdoHa0d1a46S5XZZNTx3D7AaJMcgPONkAaR3jBHTa8MBG-zsJJnubFnp0B0BEJosFisr2cC8acASxAmj9s8I8ebLtX1bmEtZyGOWgCBw4pdAZf3anoA5xiuC72c_Zngn9V_qbQO_Nv61-Iedz4IQSgkNG65Xt_61r2B-sBxYjddlXYUjEGxeieFszPLhbhGVYJFf6QSKfbKe1UbuH8wfEzybOX0mxoT88IFRfWxRGhm43XAcqJT-p2pYHtqL9PwEtOPyc4Wej0ejhoI5-hylMmPtelaiDaeJy-jhTEkW0MC8ua5IoAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om-jLs5HTptBfQPp3F96JnSXljIiCHkdbN5IbZk4NdBbvlIu7S0rQFSNG2TYRekvl7dCYK-eFVoobx9fhrlncYPgEEztmTx3AYo7x-kqLAbhpx0hMCYjkTbjEJ1hf_F828ezuUCO5hJQfqUPb_j1SOXSLwwLipPtsxtjD1WWGOIIb95ZScRzFNzY7Pw1gea_VOXxI7_K7xUa6fVBrWLAXxoVtz-SmmckneDtz6It_tBe00Kn00bat8CoKQteHPDRvYwjC9-kg8Jzk_doEnoYwkRMu_19t11T_Jobbqz0AGdTTUob6dN2iJXi1ALl3UVpHxmey9YwPGFPOhUYUtspig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

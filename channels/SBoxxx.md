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
<img src="https://cdn4.telesco.pe/file/nIjooApiN0dhkeKt2ZLOMK2DA57hfTlhr5EKK7K1oOpQFN-YpqeGk7RxONc5IGEQK3kFoTfLgWLyVqnjchiruJssDOO_3mE6WEG2y3a43oQnMK8ipjM6k0UFsVQOrexeLllFETfyGJMis_SvYjNvIIF5lyEAq-A1BQ0xEL4FnSQxi0beoJCryqeUsKUaiJre6qQLxy9qgLNEh5ni1wdXN-A0SDxLYxGKO9t5xrzbV25cuzmvt9-DgebZFEMhvaEzy7lK9CZ9Ml_6y9sDdjmF_XXeYo9wXzo_FBxCY2eoJWbnExkpwQJhguwifuJc9hSCNOQlgaw-GpZh6y5Invubug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.85K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 22:22:22</div>
<hr>

<div class="tg-post" id="msg-16369">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHd0t0qKTCbdF0A7PVq0T6tlDzkVGw_LfyQaHMY6qALJGhBcikDs_9hsJzySr7vPl1xaw2LqUZzqWFGXsemQHvnPa3o6G1BQKMlykX3ururgnQtxS6l22_pub386TeJbzIeP9a2pz4EFq49PcoFwx-0z686OiXMLFFkJs1i_J9-4q95fjVa1gPVShjH_XlupyO1qA2_BtOFwiaIqZRtYvu9Vk5Frsi9YmtZd7haBl2ieQOGYp2JaafLbqIYW5soXJ7dcrSzOUm2xl34V0nSOJGURZ_92O2t0_lMC-kvdlNrXUPdNk5D0tE2vD-fr6GceUXDBRnlUM6hvz_mNR5En4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر داگلاس مک گرگور از میلیتاری نویس های برجسته X دال بر نزدیک بودن دور بعدی جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SBoxxx/16369" target="_blank">📅 22:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16368">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بازگشایی بازار سهام از روز سه‌شنبه
‌
معاون نظارت بر بورس‌ها و ناشران سازمان بورس و اوراق بهادار:
برنامه‌ریزی لازم برای آغاز معاملات سهام و ابزارهای مربوط به آن از روز سه‌شنبه ۲۹ اردیبهشت ۱۴۰۵ انجام شده است.
‌
بر اساس هماهنگی‌های صورت‌گرفته و پس از اخذ مجوزهای لازم، مقرر شد بازگشایی بازار سهام، انواع صندوق‌های سرمایه‌گذاری در سهام و مشتقات آن‌ها از روز سه‌شنبه هفته جاری صورت پذیرد.</div>
<div class="tg-footer">👁️ 458 · <a href="https://t.me/SBoxxx/16368" target="_blank">📅 22:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16367">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عارف، معاون اول رئیس‌جمهور:
دیگر اجازهٔ عبور تجهیزات نظامی دشمن از تنگهٔ هرمز را نخواهیم داد.</div>
<div class="tg-footer">👁️ 709 · <a href="https://t.me/SBoxxx/16367" target="_blank">📅 21:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16366">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✈️
پاول دوروف ، مالک تلگرام
:
دبی دوباره شلوغ و پر از ترافیک شده است. از همین حالا دلم برای آتش‌بازی‌های ایران تنگ شده؛ آن‌ها کمک کردند تا شهر از افراد زودباور (وحشت‌زده) خالی شود .
پدافند هوایی امارات زیر آتش (حملات) عالی عمل کرد. ما با پرداخت ۰٪ مالیات، حفاظت بهتری نسبت به اروپایی‌هایی دریافت می‌کنیم که ۵۰٪ مالیات می‌دهند.</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SBoxxx/16366" target="_blank">📅 21:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16365">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حالا امارات را مسخره کنید اما اساسا یکی از مشوق های اسراییل برای پیوستن کشورها به یک پیمان راهبردی با تل آویو «تصرف خاک» است.  نمونه اش پیمان با باکو که منجر به تصرف قراباغ شد و از دید اماراتی ها، وضعیت جزایر سه گانه برای آنها معادل وضعیت قراباغ برای باکویی…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SBoxxx/16365" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16364">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/16364" target="_blank">📅 19:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16363">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEYbxtX-mHoLeLkP_XSFpl9ydiH7_WJgow0PhzBtiyIRLmP_yOIRuf7XrWQTQZy3OmbrCQC8I2bIwxvdsOr_V629hVlnhcieO3-jPSYBbDSsO2xWNvmZVT3RDWsoicAZDmUPqTlEEYCtk_T45LQwlLQo5-JOZ6Jyr8bAg0-tnuGNw6_uNoADd6TS71e23TV34GPt2ond6x46YcuD9D4XY8a9mgt-vr2bEIwCqaiFM-uOGU7M1PHgP-G7EI-ODNKScxFLx6spJoNfVWKxkmgCLeAlbon9jhqlwB75-dNq4Qp2wSRi0c6KiLnUzNNlwOrir3qE-f_xfXKjbDRfD3MZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد از تعمیر سوپراپلیکیشن "بله" ، سوپراپلیکیشن "شاد" دچار اختلال شدید شده است</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SBoxxx/16363" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16362">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♥️
سوپر اپلیکیشن "بله" دقایقی قبل از دسترس خارج شد</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/16362" target="_blank">📅 17:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16361">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♥️
سوپر اپلیکیشن "بله" دقایقی قبل از دسترس خارج شد</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16361" target="_blank">📅 15:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16360">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKrdu8lzIPQJ1hu9mBNLWvu-AifFcMeGHLGEbbI0SAj_EySCXqyRVHQ8-pq7XHbRnulQUD1nuDoVokNBDGha40RqdB5gdmCI-MUuTI18ZfFYCI09lSyisLFC8V7n2H8l5jf7LgcRhDmJIs80IvwTCAExYIdQC-voDhtEIZHctAtDG_6e9q_zTiw5GdAlnYLtEhdMKj6C_pE8qSIwKbDpTvkvJm0ipsDd93u6jcTshIU23zza6MGd-_jGFS2HjnPlWtjbMzbCYL6Rrw7ecBQOlWUuS3MVq622AeUDB1vSvgQ9X_NY9vPve7IZC0FLcMFjT_HWyA4Tff29NrZjm6sqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تحولات رفتار بانک‌های مرکزی درباره طلا
بانک‌های مرکزی در سال ۲۰۲۶ رویکردهای متفاوتی نسبت به طلا اتخاذ کرده‌اند؛ برخی مانند ترکیه فروش را افزایش داده و برخی دیگر همچنان خریدار هستند.
ادامه خرید طلا توسط کشورهایی مانند چین و لهستان نشان می‌دهد طلا همچنان جایگاه مهمی در تنوع‌بخشی ذخایر و مدیریت ریسک بانک‌های مرکزی دارد.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/16360" target="_blank">📅 15:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16359">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">◆ در صبحگاه دهم اسفندماه، چهار فروند جنگنده فانتوم نیروی هوایی ایران مأموریتی علیه مواضع کردهای مسلحی که قصد نفوذ به خاک ایران را داشتند، و همچنین علیه نیروهای آمریکایی مستقر در فرودگاه اربیل، انجام دادند. در این عملیات، دو فروند فانتوم وظیفه اسکورت به عنوان…</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16359" target="_blank">📅 13:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16358">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParvaz dar oj</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYw0ldb8-6EsB0fwlzcO5s2NnGw_18UQdWURIN6m0GdTnfCwPAGmqRpP0Pr7QcLADhTiRz1s3PJVWIstSeHc5ZqnGrgWFU_5BS-f_HFWcZPSUhlwRGxpNygcGOZKg2pbDfZEojtzcxpqhVJTi42E1imnv8v0tRt0nu4ByZUfpIZP-8vuF1vUKIE-6unFzdSRBKW7zah0B99K7BD26t97U4IiyFYRHZxxmU_prAPer8_PVU4Dii_VTlrEpsTFkgQ-dBkaJ_q-y4keGJSQX7_QcKSchBfRw7hLqy1ph32B9itXAzzzEpPTI76U5Eg026Oyl5oDCOyz9rGfE-c5hCal5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◆ در صبحگاه دهم اسفندماه، چهار فروند جنگنده فانتوم نیروی هوایی ایران مأموریتی علیه مواضع کردهای مسلحی که قصد نفوذ به خاک ایران را داشتند، و همچنین علیه نیروهای آمریکایی مستقر در فرودگاه اربیل، انجام دادند. در این عملیات، دو فروند فانتوم وظیفه اسکورت به عنوان تاپ کاور  یا تأمین امنیت هوایی را بر عهده داشتند و دو فروند دیگر مأمور اجرای عملیات بمباران بودند. جنگنده‌های بمب‌افکن موفق شدند مأموریت خود را به‌طور کامل انجام داده و اهداف تعیین‌شده را مورد اصابت قرار دهند.
◆ در جریان بازگشت، در منطقه مرزی ایران و عراق، جنگنده‌های اف 16 و سوپر هورنت  با هواپیماهای ایرانی درگیر شدند. هویت دقیق جنگنده‌های فالکون مشخص نشد و احتمال تعلق آن‌ها به نیروهای آمریکایی یا اسرائیلی مطرح بود. در این درگیری، دو فروند از جنگنده‌های ایرانی مورد اصابت قرار گرفتند، اما هیچ‌یک سرنگون نشدند و هر چهار فروند موفق شدند به پایگاه خود بازگردند.
◆ همزمان،تامکت های نیروی هوایی ایران نیز به حالت اسکرامبل درآمدند و برای پشتیبانی و مقابله احتمالی به پرواز درآمدند، اما در ادامه درگیری هوایی مستقیمی رخ نداد. با این حال، پایگاه مادر این عملیات بعداً هدف حمله قرار گرفت و از آن زمان تاکنون از وضعیت عملیاتی خارج شده است.
◆ با وجود خسارات واردشده، این عملیات از نظر نظامی و تحقق اهداف تعیین‌شده، عملیاتی موفق ارزیابی شد . خلبانان اعزامی با توجه به گشت دائمی هواپیما های آواکس و جنگنده ها بر فراز آسمان عراق،کار بسیار بزرگی انجام دادند .
به خلبانان اطلاع داده شده بود که به احتمال 70 درصد ،هواپیمای انها مورد اصابت قرار خواهد گرفت،اما همگی با شجاعت مثال زدنی راهی آسمان اربیل شدند .
@PARVAZDAROJ
| 𝐀.𝐑.𝐀</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/16358" target="_blank">📅 13:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16357">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6d3c48e2.mp4?token=J-236nA7NXSy3LfK90CuESY8KkHvBCm0kU_1iZoWRLLDncsoOn_EPfTSJcbqaAsMZucxDhdyA3pPVmFKp5B9GOb1CYMDYd2rMJD-_27_sbnc6hXxV6FX4xyMAqPm135YKfuNOWOUC8W6hqDdEyELJihoQ8YgH40tGCrVFwp5_1EKzQprZ7Tdaf5RNxhtjNhyHB8beF-tBSaBEx2JX22FWXOTYUz19n1Sa5q8Eh88DhS8LEt00s2hYEwx9o9yF8i2rnhLOKXDohWDw_69WqwfjurrBWzFrMwueY03dCB3znA6xt16pBOkHbFS0qfmbRVL97TvwF3O2b8G11w_3r0KxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6d3c48e2.mp4?token=J-236nA7NXSy3LfK90CuESY8KkHvBCm0kU_1iZoWRLLDncsoOn_EPfTSJcbqaAsMZucxDhdyA3pPVmFKp5B9GOb1CYMDYd2rMJD-_27_sbnc6hXxV6FX4xyMAqPm135YKfuNOWOUC8W6hqDdEyELJihoQ8YgH40tGCrVFwp5_1EKzQprZ7Tdaf5RNxhtjNhyHB8beF-tBSaBEx2JX22FWXOTYUz19n1Sa5q8Eh88DhS8LEt00s2hYEwx9o9yF8i2rnhLOKXDohWDw_69WqwfjurrBWzFrMwueY03dCB3znA6xt16pBOkHbFS0qfmbRVL97TvwF3O2b8G11w_3r0KxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#اعلام_وضعیت
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SBoxxx/16357" target="_blank">📅 12:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16356">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLFSJWNZEBsGHILU35R_C-mAPOF5sp73DjmrmxRGZKarQA85dtjwOqH5FS8IfiAWBAYDcCSWi7TCyHirwKSyO0dtY6CqqXRIelDLrFAa_vNfiGpdVi1xmvyBPfOJsJUNrQisGBrXZQxB2bB7J7tWO7DdmoWVovzvGspxGe_IBYt0Jo3CxCr_NwjXql4karJ_AzLzCONf6bWYzUMlfB62kcokyOErE4xOVxwdpG1Cwr_UHaRFj9ce-WU0pwYquUTvhagYwUMB8CsRM1ST26CJr8KmPQ5kUPavysm1aQhPbm3qSMgQGDAJrYjQRxLg7YDVktFce62qe3unLztNsbl7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب گویا شماری از مجریان صداوسیما فاز امام جمعه بودن برداشته و با سلاح در برنامه شان حاضر شدند!
سبحان الله !</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/16356" target="_blank">📅 12:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16355">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو.pdf</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/16355" target="_blank">📅 12:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16354">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به نظر می‌رسد ایشان از خوانندگان Secret Box باشند.</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16354" target="_blank">📅 12:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4117d0b4d4.mp4?token=GT1V_hkJo8094tp8gs3NQIYaG0lqQ0vwIU1cumlX3PCrNfWRBRX3E_OVfXFOmbNR_aGgG25fZ8niYnrmilWsUem0i86VRk1MigFwXlbPdkuxOdY5lpecd27HmG8kStMa5Z04fzPr8mRIQvUr1zOWlL3O3R91qN8sJXG1ppSZndzRLQar6SGa9xzeAo3qVzbedoaG0bsxkvbxQ2j6gwEjqsJ7C6vcN4bH1Ls8U-ip3Z5jhX6IJqci0eL9xWOcQsv3_0gS9_D8Vy5xleaj-Qncfmni3iQG6lemqGiM_eLhdQEJso1UgPz2D-gfWJLJhbXGzFSjVqLyZAltjXPvROz70raucAE2FMo5UbxVTgQluRVnUaEIHxeNWcQ3XS-WGjx3kjeu8OQ033HieJwyqYE4UKLMb6uxxXJxhSqu5hwEDkj9hkctwHLuaiWYtRZcrumqpeztpiOY-u1CqnqKegY-OOB8qg3rsB8aTAO3U1Yq4MzYSA7YnoPlHZQkLSVXr4ckoc8Kz0-sC1OzI1tNQC6B9siDm17EC-Z_szTCqlvq3jjp7tJuZvkYP0e43nh5gOidKmoKwVw42pRkkSwRA5x9oGmYBPXE2RtzBE-G7RkReZPGAGTKPBgvE14nTewyUgWWTePPQ_CJDt-QTCpgtrq6mPwFoS-7fL13wK0rSf-NAFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4117d0b4d4.mp4?token=GT1V_hkJo8094tp8gs3NQIYaG0lqQ0vwIU1cumlX3PCrNfWRBRX3E_OVfXFOmbNR_aGgG25fZ8niYnrmilWsUem0i86VRk1MigFwXlbPdkuxOdY5lpecd27HmG8kStMa5Z04fzPr8mRIQvUr1zOWlL3O3R91qN8sJXG1ppSZndzRLQar6SGa9xzeAo3qVzbedoaG0bsxkvbxQ2j6gwEjqsJ7C6vcN4bH1Ls8U-ip3Z5jhX6IJqci0eL9xWOcQsv3_0gS9_D8Vy5xleaj-Qncfmni3iQG6lemqGiM_eLhdQEJso1UgPz2D-gfWJLJhbXGzFSjVqLyZAltjXPvROz70raucAE2FMo5UbxVTgQluRVnUaEIHxeNWcQ3XS-WGjx3kjeu8OQ033HieJwyqYE4UKLMb6uxxXJxhSqu5hwEDkj9hkctwHLuaiWYtRZcrumqpeztpiOY-u1CqnqKegY-OOB8qg3rsB8aTAO3U1Yq4MzYSA7YnoPlHZQkLSVXr4ckoc8Kz0-sC1OzI1tNQC6B9siDm17EC-Z_szTCqlvq3jjp7tJuZvkYP0e43nh5gOidKmoKwVw42pRkkSwRA5x9oGmYBPXE2RtzBE-G7RkReZPGAGTKPBgvE14nTewyUgWWTePPQ_CJDt-QTCpgtrq6mPwFoS-7fL13wK0rSf-NAFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها مواردی است که اسراییل را به سمت یک راهکار نهایی پایدار منطقه ای بوم پایه  — بجای آویزان شدن از غرب (و خصوصا آمریکا) — می برد و کریدور داوود و پیمان موسوم به کوروش و … در چنین بستری معنا می یابد.</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16353" target="_blank">📅 12:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16352">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">۸ سال پیش …</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16352" target="_blank">📅 10:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16351">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">استوری مشاور محمدباقر قالیباف</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16351" target="_blank">📅 10:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16350">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQDpF78J4-DyflQwugxbXV2LscxqJxmfJmIH0VU_EXmTPiTLUN0_kxJ2g4zP16rkpVf7GvEw2RXkUaViKuOO6rO7Iu8V9dka66Arog-482YxlgdI2_eXm226zKdX5Aw38ZoOs3AnrZuNACCHlvWUxl6ghZyq5ydllbNfbX0_9irpRUMRg75bEeLyhBLKsqk3cj1_TVjP7_pxfWWRmJh0hGU-BrIEAcspurZ35fdpAnapgGJ0U0msZDSy8oxfPOTNO50rU77v30gLvtkb0qTYyzr1We9eSIUKNeUzOHYBdEm142C-eh5chPo3Hzf_4gdPt0_b6fX2Vwtz3dNqoa6V_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16350" target="_blank">📅 10:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16349">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDwYNp_Qt04HeCZO6Ks8oFZGTRHz17h1C97teUYcOhv8gpqQzgUT3wkGpr2QX1Ixcjem0fvBbWEsDHsEJT-pCCzcF6pI2zq9LMsJyGBrABDiErMThOhOdLH2D8bL5qVvZwlrBwf6d0Yp3ckpJ8-e2DHJ3l83aQ4fVQy7lKwtmTnkSopk7wBJCzRGyWAIDx43G4EV1-toTQd2_FOx9ozE_bCd9ac3uHR_QxdYdlQOY2vQ7YB6drcOuNCB2G8DFsG8ooorY7MTAXpehf9FXX8WqkgLoTrk2P6zmqlM2-nf-kg0UJj5JLaFPdlrYI_rDeVpWMwpteSUAAzwDLKiXJCd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/16349" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16348">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16348" target="_blank">📅 08:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16347">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f23855f2.mp4?token=iM1KVc1b97O9QiUxq9e1J31vszkhjX_eO8Oupb3xUmN2rvU_8PWa5iISUOco4xNdi4xNO1b5TBAHzqiH7l-zYT-4eZH47sNsz2yd4eN__2KTiSXKJgygZtn7GkxcOoewDxI4Gk9P60kYA6522MD1UXBETOi9_U1XPbqbaRAoPw1GPassTTzsBfFX9RF5se49iwnB_ZMgr-GTT4XMG5tQ2934iYJhxkcuCfxzdwPuExFhtSGFWSj70BVOwsInKkpVRRTWAI9dkFj2CLGlsdZcUwtLK0k5IYH4IEr_1gBuBslFNINSfomP5cRtf9WGlNyKQtHIb1OYKPRCtimt65wO0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f23855f2.mp4?token=iM1KVc1b97O9QiUxq9e1J31vszkhjX_eO8Oupb3xUmN2rvU_8PWa5iISUOco4xNdi4xNO1b5TBAHzqiH7l-zYT-4eZH47sNsz2yd4eN__2KTiSXKJgygZtn7GkxcOoewDxI4Gk9P60kYA6522MD1UXBETOi9_U1XPbqbaRAoPw1GPassTTzsBfFX9RF5se49iwnB_ZMgr-GTT4XMG5tQ2934iYJhxkcuCfxzdwPuExFhtSGFWSj70BVOwsInKkpVRRTWAI9dkFj2CLGlsdZcUwtLK0k5IYH4IEr_1gBuBslFNINSfomP5cRtf9WGlNyKQtHIb1OYKPRCtimt65wO0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره سازی اورانیوم غنی سازی شده بشوند، شدیداً به آنها ضربه خواهیم زد.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16347" target="_blank">📅 08:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16346">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ: ما به پیروزی کامل نظامی بر ایران دست یافته‌ایم</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16346" target="_blank">📅 07:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16345">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRJ43zVnNLU2W8BhPn2QQ3bKYjwB0xecWFLHXY5wuEHwFdhHodXDS6mZbHj9Sf8ve5AwMes9puM_EIsYngsuZecfaU1-Db0d1RdO5YKD4M3PGZkPhTUsb_G6VsOEPkDLcLFBnkDq57bQWueeoHNRgeh9_H8lRAc6UtJwKYR_lwoXNvxFC2QPhZ3KqCx5rv3713KDmGVoTDAVcTYOhl1riLSceQLyTBcaZ6s_BdwKld0Q6B6RnXhcAjD-dwOxsWlaxCvcX9g0MKsJHXIJL2u2puDehcA1aDcckS4GgAVda7MatZVeFw5U2YnAhkmdwnS5ICj60LYFISXz7bhxPkcaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستوفر نولان این خانم را برای نقش «هلن» در فیلمش درباره افسانه اودیسه برگزیده و ایلان ماسک هم با گفتن اینکه «نولان با این فیلمش دارد به قبر هومر می شاشد» از خجالت او درآمده است!</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/16345" target="_blank">📅 02:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16344">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به نظر معامله بزرگی در راه است.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16344" target="_blank">📅 02:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16343">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePhKAG3KD9sXW8IRIvVNOJfKWm6FfqwCW80W89dKm7M13idJkNUkEXZX7Jv-inrhuWaHikkmznb58HyOZUBHdqcCd7rqyjMf_i_hTtaqTZ4jslFoTTMrFFFw0I-O5w2GNDCNtlLktQzfDnCuHvd5CMT_7cI6buAqAtA5kSMAd5GNc_4vrm0FA6nJoZqGOFLvM8TxmcctcDicDmUEAcRG879FtbR7jcpkLkJIydZbFcwSPLUowD3EbwOKxjin7_VX45J947fbfJH_3pRBchg7RYxsbk-Wtt3t_3eFs1BgL_AgCp9E-gB9ZCXV3BCoFu5D9WzRl7ON6yB_wI3EHi1DoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران   بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.  افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16343" target="_blank">📅 00:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16342">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حس میکنم دوباره سوی شیر گرسنه دارد گاو می آید که ولی خب.</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16342" target="_blank">📅 23:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16341">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرانسه حضور ناو هواپیمابر شارل دوگل در تنگه هرمز را تکذیب کرد</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16341" target="_blank">📅 22:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16340">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فرانسه حضور ناو هواپیمابر شارل دوگل در تنگه هرمز را تکذیب کرد</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16340" target="_blank">📅 22:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16339">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ مخالفت خود را با اعلام رسمی استقلال تایوان ابراز کرد
من دنبال این نیستم که کسی مستقل شود می‌خواهم آنها آرام شوند. می‌خواهم چین آرام شود.</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16339" target="_blank">📅 22:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCaK9_GxFYUTJUqh5jEh81E5s8MWJ7CDg2ZeCAcDEjR8W4JoIlfDqDmLaMUnOQnRFVs85j4nvVZs7wlA31mFiFkO5Qp8nAMjvUzsMNJnvOtaxAcDCYrVDcEWIQ9pd3KI6HtuU5Kj6x7lwgbONTHSdWP9I0c1h0D4_s5_uOD3e40-yhj0G0HOVqqdI-KFK5dIXqC3Zz2aE-XAelaWkYIyJgN7RvqkYXmbwcxPKizOrySf6__XbzT_JkHq7vmcUwtPFIP_YG4Ebze4r03JxfD0kWW_qXIvTn0AbROGKofu5fBpk2l7i90NFQ-G2t2T8LkmtvAPxI-tKJtfLYI5IFdegw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:  عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16336" target="_blank">📅 21:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16335">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو:
عزالدین الحدّاد، رهبر حماس در غزه را ترور کردیم.</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16335" target="_blank">📅 20:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ولی خداوکیلی راست می‌گوید ، هر چه آدم توخالی بیسواد عقده ای که با قر و فر جلوی دوربین توانسته نقابی فریبنده برای خودش بسازد، در اینستا لانه کرده.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16334" target="_blank">📅 20:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16333">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">میرزا ایلان ماسک السلطنه:  اینستاگرام برای دخترهاست!</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16333" target="_blank">📅 20:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16332">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ای ایلان، ای مرد پرگهر !
ای ایکس ت سرچشمه هنر!</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16332" target="_blank">📅 20:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16331">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">میرزا ایلان ماسک السلطنه:
اینستاگرام برای دخترهاست!</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16331" target="_blank">📅 20:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16330">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شاید ما برخی کشتی ها را با پهپاد زده باشیم، برخی ها را با موشک بالستیک، برخی ها را هم با موشک کروز.  خب اینها می‌شود تفاوت‌های حملات ما.  اما یک شباهت بزرگ هم میان همه حملات ما وجود دارد و آن اینکه کشتی مورد تهاجم مال هر کشوری که باشد، دستکم ۲ ملوان هندی در…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16330" target="_blank">📅 19:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16329">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16329" target="_blank">📅 19:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0nn_uD6GxG-4aYDoz6zqo6NkBtU0M1-PfDRLmnorOtNqFq36wXIJXxjvw-UaYduKmo2EAQ7MI0FftjV-AzIQD0nmDOpZJ0T4CsQo3CfcXzJYfJTAVJV_RUy1ikVCISe_FNJi751ney7nAb5trax_EiompYh_itcTc5QjfL6BVXAHxds5cHgnNbBgDc00EsxoISJ2W6-Zn6Ovqr25ogkDyMUl1CHOIBNwYiKdXGpln3Cb1J0N-Aeo6z01czSa-eirZKv-H1jhrAapteJXNngrv73znJMQj-IOkmi1YBrijxITf4mwH_gEvgcM59Qxeq5aPG_O0LiRJaHLeSF1dH5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران
بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.
افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن است به اهرم سیاسی مهمی برای ایران در مذاکرات و معادلات ژئوپلیتیکی تبدیل شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16328" target="_blank">📅 18:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze24OKMWNZECfthL6mDHnfYCC4Lwc81MzBTOsreSIoWhQ21cfwhbwIsVxwQ3hQmTnRQgUU_4ubKzfdJF8zqCsMi2PFNzZiHAdm71JDcxlt9U2GotoNAYuJxLkTAXEWPwuAMCcad21fDt03mCdqwxVH2tbp6oc7ruRIo12kML2EG-Re5J0JfdrWpH6gWLTBRCDlpYuWrvEwlVNHlOjs0bTCxe2uLQNLHIuX4FEyBxSeBs1Sg2CDiExmF6RD8NjcV3Ll-OJdPMVQ4qXIXEQDEJV__zkghl9IQsqqYdFfXQ7o-sfw0y-5-sAciO2MWezvRhGGrV-IrxVuwQFJwS7hu1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی ؛ وزیر امور خارجه دولت :  پس از تجاوز آمریکا به ایران ، کشورهای بریکس به چشم دیگری به ما می نگرند</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16327" target="_blank">📅 15:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg1qlLNpKrmWYwc5OzIpYdrTO2KJ3Sob8vjwlhFPjilUbemJZJ-NQwrmNr7ScG5tU5T0TcFRvyyrv6UYgmGtQSExJ2penvN3wMJgeuEqQ2V42fCQqyXau-Tcsb33JRxIK4zx6d1_mswLFJpirgoicw5xuy80WHE6tJLLmRAAwhBwOcmIBd1hMJsRdHbpvdIjp8W5tgnHhpO1rTvNo2s18u9e-PrScD6yAu5okDPbNlEnwZSqllHox5aGRzgY-ThziVvfNpav9XXU2ZKF_tV-_RvdVVLuzoJhbvfTtTg6mtS4mexOawfg9boGIUIUwdv_vUzTeq04p5V_oWrV_0KjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحران نیرو در اسرائیل عمیق‌تر می‌شود: ارتش اسرائیل به هزاران سرباز جدید نیاز دارد
۱۵ مه ۲۰۲۶ | پیترو باتاچی
در سخنرانی خود در برابر کنست در ۱۰ مه، رئیس ستاد کل ارتش اسرائیل، ایال زامیر، بار دیگر بر لزوم جذب سربازان جدید تأکید کرد.
وضعیت ارتش اسرائیل:
ارتش اسرائیل طی سه سال گذشته در سه جبهه درگیر بوده و اکنون نشانه‌های خستگی را نشان می‌دهد: نیروی فعال عالی آن فرسوده شده، در حالی که عملکرد نیروی ذخیره در سطحی نیست که انتظار می‌رود. به‌ویژه، بسیج مداوم نیروهای ذخیره، منابع انسانی را از اقتصادی پیچیده و کوچک اسرائیل — که فاقد عمق استراتژیک است و در چرخه‌های جنگ طولانی مدت آسیب‌پذیر است — تخلیه می‌کند. بر اساس اعلام ارتش اسرائیل، ۱۲٬۰۰۰ سرباز جدید به‌صورت فوری مورد نیاز هستند، به‌ویژه برای نقش‌های رزمی عملیاتی.
یکی از راه‌حل‌های پیش‌رو:
اجباری کردن خدمت سربازی برای یهودیان فوق‌ارتدکس (حریدی‌ها) است که همواره از خدمت نظامی معاف بوده‌اند و در حال حاضر حدود ۱۴ درصد از جمعیت اسرائیل را تشکیل می‌دهند — سهمی که با نرخ زاد و ولد بالاتر از سایر جمعیت یهودی، در حال افزایش است. در ژوئن ۲۰۲۴، دیوان عالی اسرائیل حکم به لغو معافیت آن‌ها داد، اما از آن زمان، حریدی ها به‌صورت سیستماتیک به خیابان‌ها آمده‌اند و عملیاتی شدن این تصمیم را به تعویق انداخته‌اند. برآوردهای اسرائیل نشان می‌دهد که حداقل ۸۰٬۰۰۰ مرد فوق‌ارتدکس بین ۱۸ تا ۲۴ سال سن دارند که واجد شرایط خدمت سربازی هستند.
کمبود نیرو برای ارتش اسرائیل:
واضح است که ارتش اسرائیل با کمبود نیرو مواجه است و تحولات اخیر در جبهه لبنان نیز اوضاع را بدتر می‌کند. حزب‌الله، علی‌رغم ضربات سنگینی که متحمل شده، مقاومت شگفت‌انگیزی از خود نشان داده و اکنون با موفقیت از تاکتیک پهپادهای FPV استفاده می‌کند — توانایی‌ای که در مدت کوتاهی (با کمک چه کسی؟ وفاداران سابق اسد؟ روسی‌ها؟) به دست آورده و برای ارتش اسرائیل مشکل‌ساز شده است.</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16326" target="_blank">📅 15:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ: ما به پیروزی کامل نظامی بر
ایران
دست یافته‌ایم</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16325" target="_blank">📅 15:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزیر امور خارجه ایران: همه کشتی‌ها می‌توانند از تنگه هرمز عبور کنند به جز آن‌هایی که با ما در جنگ هستند.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16324" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزیر امور خارجه ایران: همه کشتی‌ها می‌توانند از تنگه هرمز عبور کنند به جز آن‌هایی که با ما در جنگ هستند.</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/16323" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ: آخرین چیزی که الان نیاز داریم جنگ است.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16322" target="_blank">📅 14:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16320">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">از دیروز که رفته چین 2 عقب نشینی داشته ترامپ:  — اینکه به قول خودش گردوغبار هسته ای لازم نیست حتماً خارج بشود و همین که ایران دنبال کرم ریختن اطراف محل دفن آن نباشد کافی است.  — اینکه اصل غنی سازی در خاک ایران از دید او مشکلی ندارد.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16320" target="_blank">📅 14:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نرخ بازدهی و نفت به جاهایی رسیده بودند که فشار می آورد و شاخص های سهام هم نزولی شده بودند. از این رو لازم بود که کله زرد یک آرامش مصنوعی تزریق کند</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/16319" target="_blank">📅 14:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فوری | ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم، به شرطی که این یک تعهد واقعی باشد.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16318" target="_blank">📅 14:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فوری | ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم، به شرطی که این یک تعهد واقعی باشد.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16317" target="_blank">📅 14:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16315">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ژاپن معاملات تسلیحات مرگبار را در جنوب شرق آسیا پیش می‌برد  وزیر دفاع ژاپن، شینجیرو کویزومی، روز دوشنبه در جاکارتا با همتای اندونزیایی خود، شمس الدین، یک پیمان همکاری دفاعی امضا کرد، و پس از به مانیل خواهدرفت؛ جایی که نیروهای ژاپنی در کنار نیروهای آمریکایی…</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16315" target="_blank">📅 13:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16314">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGd1UhQO96zf5poR5_okIyroZXS_Mo8tzWNtChq7v054NZu9vchDdesghPWUvKyjE6tEF9vUGVd45Ur7TGfkjdyaqNqoZrDmDSDUrObkG-sdc14yhJ7FlCQH05X2jYHP6OZltR8KdxWa419M6Tmun6FWR2-H8YYYzt0quypu_XdxJCAyopfVvDHkpyM6LWTYM7-ueKp8od7OQQ763xSBG68YRVWCpcdrkwsuEaKF_FmhX917FbQNQB-S9TXsZbprjJwMXf0FFoWGc7CtG1n2NhrhX7SSrY8J7XM5ZRFMEBIdkSQ9m5aFLNJS3xUd9kZCHNnqtpSXgQm6WSdfqNPwXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی ؛ وزیر امور خارجه دولت
:
پس از تجاوز آمریکا به ایران ، کشورهای بریکس به چشم دیگری به ما می نگرند</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16314" target="_blank">📅 12:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/16313" target="_blank">📅 10:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRcIc659hGtIosaheix73AV65QYlSwZCAr0AJLZTjTyhExWrjGpa-7AmB_9ef6Gv-_gS4ebCEP9NULA1VmanD3eygkpNoMWcy25dbRI0UWOfMeegPJf0Ll3qd_Jis17s4pcKpc-qYr1tqZB5OGxZ0Tgmomw5wCBoOINyZVOWY0a810ZRgyvuRAJA3aZcTxO2Fbj_gtf-KJcVGZW5MjXQSGJVNIswvHMz0rxAIp33K2W83b6gf3HuiCxuFUJqEVuQROHViEUZ96Ey1s9WKPoSvhn46g1NgR9t7-5FVKYEyCSRnfFrT7plnw0KQaGnUnq92Ang24ZpH_T4EJdBLKsY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستوفر نولان این خانم را برای نقش «هلن» در فیلمش درباره افسانه اودیسه برگزیده و ایلان ماسک هم با گفتن اینکه «نولان با این فیلمش دارد به قبر هومر می شاشد» از خجالت او درآمده است!</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16312" target="_blank">📅 10:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
🇻🇪
وزارت امور خارجه ایالات متحده اعلام کرد که «اورانیوم بسیار غنی‌شده» با موفقیت از تنها «راکتور هسته‌ای» ونزوئلا خارج شده است.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16311" target="_blank">📅 10:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zaraban</div>
  <div class="tg-doc-extra">Shahab Tiam</div>
</div>
<a href="https://t.me/SBoxxx/16310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16310" target="_blank">📅 10:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اینطور که پیش می‌رود، فقط نمادهای استقلال و پرسپولیس در بورص باقی خواهندماند.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16309" target="_blank">📅 10:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تهران تایمز:
آمریکا پیشنهاد ۱۴ ماده‌ای ایران را رد کرد
طبق اطلاعات رسیده به تهران تایمز، دولت آمریکا پاسخ پیشنهاد مکتوب ایران درباره پایان جنگ را داده است.
آمریکا با رد پیشنهادات تهران، بار دیگر مواضع خود بخصوص در بحث هسته‌ای را تکرار کرده است. / مهر</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16308" target="_blank">📅 10:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کریستوفر نولان این خانم را برای نقش «هلن» در فیلمش درباره افسانه اودیسه برگزیده و ایلان ماسک هم با گفتن اینکه «نولان با این فیلمش دارد به قبر هومر می شاشد» از خجالت او درآمده است!</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16307" target="_blank">📅 09:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16306">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXnNaxgAz5Lf2AfoQEkmoTrJEEnotOXOZz_3qZ-4Gk7j7MQnzYt4KE7KvFSKR6vE7JWa1lm06j-pQ613k8a4v_eSLjzZw52wS4TPCfuWpbVLET-0bGl64YxCIAJdrX_AtPLyyBq-ziwGUV2GvIVVeQ6-k2tOlmHS8SmDrMSi0UK7-tqaQggwhP9bKHofj02Ip_jU6hQTNST0st31w1c-isivCTSRlSYTpNAZQY6LwXrcLE8a4vW8MaPE6hufcLCbPSA4Oi3uD_DA9ki6iTx3Q70HZsi9zwzyER7CpnXRzH6ct4s4mVysADt910VzAtoRyvSTGicpKD5q6ncBwkJrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD -- H4  مسیر بعدی مدنظر پس از رسیدن به سقف کانال.  تحلیل تایم پایین تر در یادداشت بعدی...
💬
ارتباط با پشتیبانی : @cyclicalwavessupport
📌
کانال ما : @cyclicalwaves</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16306" target="_blank">📅 09:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16305">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNOiC1s8j-3oFUOxhP0AviR1GoetbAaPItMWpuDvojsias0R5qZVhTvlj_7sOcfn4CRu2Shz2IgVR1XVlOshjt4Co-6PdwRp6OMLder_FAVENWTJwBwU5tzF15NhN-FkAFKwx8kPxNXNGj70oorG0wa8t2W8xVOA3LBbdwt4EPAlbe1RAtMtCVG9_IT_nXahHUtTIdJNnKfz4JIWIdejCqWcxORCx-zLADajhlRZlEJ6CvpZYHJ9vzgVtvWMFr-semWv3x5e5cC9cOR6Gi0zO71AjgM0sOyu_fzf5ZiHROpu9_NhZgPurnkZyoLUwVcQ8kNekw_Ld4YWrkPGc-fdrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستوفر نولان این خانم را برای نقش «هلن» در فیلمش درباره افسانه اودیسه برگزیده و ایلان ماسک هم با گفتن اینکه «نولان با این فیلمش دارد به قبر هومر می شاشد» از خجالت او درآمده است!</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16305" target="_blank">📅 09:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16304">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ در نشست خبری مشترک با شی :
ما در مورد ایران بسیار مشابه احساس می‌کنیم... می‌خواهیم که این پایان یابد
ما نمی‌خواهیم آن‌ها سلاح هسته‌ای داشته باشند
ما می‌خواهیم تنگه باز بماند</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16304" target="_blank">📅 07:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16303">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وزارت دادگستری آمریکا در حال بررسی رسیدگی به یک دعوی ۱۰ میلیارد دلاری است که ترامپ علیه اداره مالیات (IRS) مطرح کرده است که ممکن است منجر به پرداخت ۱۰ میلیارد دلار  به ترامپ شود
در حالی که رئیس‌جمهور بر وزارت دادگستری کنترل دارد ،  وزارت دادگستری در حال رسیدگی به پرونده‌ای با خودِ رئیس‌جمهور است و این تسویه‌حساب از جیب مالیات‌دهندگان پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16303" target="_blank">📅 07:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16302">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-5W5oFumssn-j1AnTOeaSjP0MFHOGcMPAX1_9BP0IH0FJ1n6JEEwVJhjTsqDe_nMjF1Wu_K0oF4TUix4KfjDyl2ELDSItBHkov7aK1iDKigKW2XLBwC2sw5OEerex1UZvVS2xtz3riE-JKo41xAG4e5RGFIoiaucFp9OwaZzhEdOfhzpSUZ-pRRvWsxvR1wcSueEU_uqIXN-JnWu6DsfEQw2gQrpm5FrbYuL8daCDVy2Wl6mjUgSR0fKdhj5NlpYId9AieEnQ3XLFMbH_ZfPCSfx9Rsj3UDVodKGk5CLSaGcBY4sVHnSfgoBBgL8kOgg_FaWAl1yBT5v_8LoBy1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر سعودی ها یا می خواهند وسط بازی کنند یا حتی به محور اخوانی گرایش یافته اند:
🚨
ناتو اسلامی در حال شکل‌گیری؟
👉
وزیر دفاع پاکستان، خواجه محمد آصف، اخیراً پیشنهاد داد که قطر و ترکیه می‌توانند به پیمان دفاعی موجود بین پاکستان و عربستان سعودی بپیوندند،…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16302" target="_blank">📅 03:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16301">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ:  وقتی رئیس‌جمهور شی به‌طور بسیار مؤدبانه به ایالات متحده به‌عنوان کشوری که شاید در حال افول است اشاره کرد، منظورش آسیب‌های عظیمی بود که ما در طول چهار سال ریاست‌جمهوری جو بایدن خواب‌آلود و دولت بایدن (منظورش محتملاً حسین اوباما بوده) متحمل شدیم، و در…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16301" target="_blank">📅 01:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16300">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7rE4qWyeeuMQ6V8T6Z-KY11o2EQJnAbheSBhjoV6MlhHv0joECFFYH5OqjKze_4albWeLQ-pyFA6A78EoDoltcpi1z7Q4FrjYtJ1e73z-VJfIQcEPaaaSSxSMDWb_10iFdbzO_0vc1yA_5ZacKlXp5gAHnOSEtW2mQn69GxBfUvl9eU18HlAeIXryGlj7oFYY-8IE_XUwYS7OQuBwJx26lg4kJfQYvTq_4uI5cfmXdWgMVio6twPfnzBCtSQybD_SpTDGpNZt07HMblTuX8Mpz77WL3SH7-AMpEPD1VP7atSrlH1coh5uZOX-vTF0pwVGvbFpesiD6EtGtU_EB0Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می رسد کوبا هم بزودی به وضعیت شب بخیر عزیزم رسیده و از شر رجس و نجاست کمونیسم رها خواهدشد.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16300" target="_blank">📅 01:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16299">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ:
وقتی رئیس‌جمهور شی به‌طور بسیار مؤدبانه به ایالات متحده به‌عنوان کشوری که شاید در حال افول است اشاره کرد، منظورش آسیب‌های عظیمی بود که ما در طول چهار سال ریاست‌جمهوری جو بایدن خواب‌آلود و دولت بایدن (منظورش محتملاً حسین اوباما بوده) متحمل شدیم، و در این مورد، او صد در صد درست می‌گفت. کشور ما به‌طور غیرقابل اندازه‌گیری با مرزهای باز، مالیات‌های بالا، تراجنسی برای همه، مردان در ورزش‌های زنان، DEI، قراردادهای تجاری وحشتناک، جرم و جنایت گسترده و خیلی چیزهای دیگر آسیب دید!
رئیس‌جمهور شی به صعود شگفت‌انگیزی که ایالات متحده در طول ۱۶ ماه فوق‌العاده دولت ترامپ به جهان نشان داد اشاره نکرد، که شامل بازارهای سهام در بالاترین سطح تاریخ و 401K‌ها، پیروزی نظامی و رابطه شکوفا در ونزوئلا، نابودی نظامی ایران (
که ادامه خواهدیافت!)
— قوی‌ترین نیروی نظامی روی زمین به‌طور قابل توجه، قدرت اقتصادی دوباره، با رکورد سرمایه‌گذاری ۱۸ تریلیون دلاری دیگران در ایالات متحده، بهترین بازار کار تاریخ آمریکا، با تعداد بیشتری از مردم که اکنون در ایالات متحده مشغول به کار هستند نسبت به همیشه، پایان دادن به DEI که کشور را نابود می‌کرد، و خیلی چیزهای دیگر که فهرست کردن آن‌ها به‌راحتی ممکن نیست. در واقع، رئیس‌جمهور شی به من بابت این همه موفقیت بزرگ در مدت زمان کوتاه تبریک گفت.
دو سال پیش، ما واقعاً کشوری در حال افول بودیم. در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده داغ‌ترین کشور در هر نقطه از جهان است و امیدوارم رابطه ما با چین قوی‌تر و بهتر از همیشه باشد!</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16299" target="_blank">📅 01:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16298">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iez0u_j2WBk0PrsBlyT0CccucUj0VvBAi6AGzsFToWoyt_jkTDI1qXsY3XvHAf37nNrdH7vjNvv_3Yg5dAgwUODDE5-w3m6qVYg6b1DBZwudHp0BIZCCxzWuIbKpSz_7S14tDimL9Lcsawb_1sVWdUKVWm1PFoO30e5BCXLUTUKYjMriYAJh1Nl21ML6-YhVSK_NpH6DEpdKZVoK86UOXRhOVxPteR5H8Nsn5NiFrMN5YHholLfekSSH5t972ulYqAk4djvY3nGpLJ91dLEar_Sp73dnQwbIBx6ux8hXfMuBslGfefi3c94wE9BQKTxLaa0HHTT7QmPpeLKH8gjA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روش وحشتناک شکتجه وجود دارد به اسم شکنجه قطره آب یا «شکنجه چینی» !  این شکنجه روشی برای تخریب روان طرف است که در آن قطره‌های آب به‌طور منظم روی پیشانی فرد می‌چکد. تکرار یکنواخت و انتظار برای قطره بعدی موجب اضطراب شدید، بی‌خوابی و آشفتگی ذهنی می‌شود.  در…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16298" target="_blank">📅 01:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به مجالس قانونگذاری آمریکا برای جلوگیری از آغاز دوباره جنگ امید نبندید!
پس از شکست دوباره طرح محدودسازی اختیارات جنگی دونالد ترامپ در قبال ایران، بار دیگر این پرسش مطرح شده که آیا اساساً کنگره و سنا توان متوقف کردن یک رئیس‌جمهور آمریکا در مسیر جنگ را دارند یا نه. از نظر حقوقی پاسخ تا حدی مثبت است، زیرا طبق قانون اساسی آمریکا اختیار رسمی اعلان جنگ در اختیار کنگره قرار دارد و رئیس‌جمهور صرفاً فرمانده کل نیروهای مسلح محسوب می‌شود. به همین دلیل پس از جنگ ویتنام، قانون «War Powers Resolution» در سال ۱۹۷۳ تصویب شد تا رؤسای جمهور نتوانند بدون مجوز کنگره وارد جنگ‌های طولانی شوند. این قانون رئیس‌جمهور را موظف می‌کند ظرف ۴۸ ساعت کنگره را از هرگونه اقدام نظامی مطلع کند و در صورت عدم دریافت مجوز، عملیات باید پس از حدود ۶۰ روز متوقف شود.
اما واقعیت سیاسی و عملی آمریکا با متن قانون تفاوت زیادی دارد. طی دهه‌های گذشته تقریباً همه رؤسای جمهور آمریکا راه‌هایی برای دور زدن این محدودیت‌ها پیدا کرده‌اند. آنها معمولاً عملیات نظامی را «اقدام محدود»، «دفاع پیش‌دستانه» یا «عملیات ضدتروریستی» می‌نامند تا از نظر حقوقی مشمول تعریف رسمی جنگ نشود. علاوه بر این، حتی اگر مجلس نمایندگان و سنا قانونی برای محدودکردن رئیس‌جمهور تصویب کنند، رئیس‌جمهور می‌تواند آن را وتو کند و شکستن وتو نیازمند رأی دو سوم هر دو مجلس است؛ امری که در فضای سیاسی شدیداً دوقطبی آمریکا بسیار دشوار است.
به همین دلیل بسیاری از ناظران معتقدند امید بستن به رأی کنگره یا سنا برای پایان دادن به تنش یا جنگ احتمالی با ایران، تا حد زیادی واهی و غیرواقع‌بینانه است. در عمل، تنها زمانی که اجماع سیاسی بسیار گسترده‌ای علیه جنگ شکل بگیرد یا هزینه‌های نظامی و اقتصادی به‌شدت افزایش یابد، امکان مهار واقعی اختیارات جنگی رئیس‌جمهور به وجود می‌آید. در غیر این صورت، این نوع رأی‌گیری‌ها بیشتر جنبه نمادین و تبلیغاتی دارند تا اینکه بتوانند عملاً مسیر یک درگیری نظامی را متوقف کنند.</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16297" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16296">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4TZ7X8-po-q384bsEXtiqkA5w3Q4UXOpjXc5HGsJWrN31IQk4hiqi8Nncje8MuWUs1_xzelxEkUIp3JCfrJ_TgRd5LeMcX0v-tyUjcrUGlndIv1_jrZGvyDZRv5F9QxzJIM3DVWdSKiK3wQUD1ZX3uQs9B6tCB5Rcvp5nw89XRPbkfo8J23LvlRIkHI6rbxmMh30g6yhJsZb6-roP9ZzsgKiNMPBnaE5m6S2ZTQKTkPdlqWxAxasXKp9t7Xjj9emymykAGtPshvEQthfbC7vDXXWefktRwzGSeke1sHSvQxHKmD6aYT_GeF0JXq_Uiguo3CM5UtVJ9qPdPFwogdEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار فرج از نیمه خرداد کشم …</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16296" target="_blank">📅 23:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16295">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جایزه رئیس کمیسیون امنیت ملی مجلس برای کشتن ترامپ
عزیزی، رئیس کمیسیون امنیت ملی مجلس: پیش بینی کرده‌ایم دولت به هر کسی که این رسالت دینی (کشتن ترامپ) را انجام دهد، به عنوان پاداش ۵۰ میلیون یورو بپردازد</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16295" target="_blank">📅 23:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16294">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس:   ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقبه سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16294" target="_blank">📅 22:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16293">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس:
ترامپ در جنگ گیر کرده است و با بلوف زدن به دنبال این است که عقبه سیاسی را در ایران فعال کند تا مردم را به سوی تسلیم سوق دهند</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16293" target="_blank">📅 22:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16292">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK3yHS8OQn7JsuqjIOaCKl43dAhqpXvglV3iTWH2kEan1J7HODI08ZdRS0QzdkHpClqmRIDQR_4VJ3cmsr8YlvUuzItlFzUyJxUOdoyPU-JitNDgsI5WYJJxV7XcKQMvdMmmFII9EZZUoEFEYlGopoNebi7ztTr6FDGPEn709NrgGgj3H5F_HWS8j2P55M4qVLBCy8i-EnA31kIofe0nistDBeO3a9AbUdaXx_WPTVfFHEOKz8KZvQbBxnzZXaj2dP23obmHDK2mWG5jQeoGnkj39jafGCDW4ROxdtN0v1FgMsovcXeLqaDIGiah8SMcSZgg2QcDIy89_3s6pdZfpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16292" target="_blank">📅 22:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16291">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزیر انرژی آمریکا:
ایران به طور ترسناکی به ساخت سلاح‌های هسته‌ای نزدیک است و تنها چند هفته با آن فاصله دارد</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16291" target="_blank">📅 22:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16290">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اسرائیل سطح هشدار خود را به بالاترین حد ممکن افزایش داده تا برای احتمال جنگی تازه با ایران پس از بازگشت  ترامپ از چین آماده شود.</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16290" target="_blank">📅 20:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16289">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسرائیلی ها به این نتیجه رسیده اند که هر مدل ابتکارات نظامی که ضد حزب الله به کار برده و می برند تا زمانی که حمایت فنی و مالی ایران ادامه دارد در نهایت بی فایده خواهدبود.  از این رو بسیاری از آنها الان بر این باورند که تنها راه شکست قطعی حزب الله، تغییر حاکمیت…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16289" target="_blank">📅 20:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16287">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رئیس‌جمهور ترامپ می‌گوید چین توافق کرده ۲۰۰ هواپیمای بوئینگ بخرد.</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16287" target="_blank">📅 19:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16286">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارت امور خارجه هند اعلام کرد که دیروز کشتی‌ای که پرچم هند را برافراشته بود در سواحل عمان مورد حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/16286" target="_blank">📅 18:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16285">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شاید ما برخی کشتی ها را با پهپاد زده باشیم، برخی ها را با موشک بالستیک، برخی ها را هم با موشک کروز.
خب اینها می‌شود تفاوت‌های حملات ما.
اما یک شباهت بزرگ هم میان همه حملات ما وجود دارد و آن اینکه کشتی مورد تهاجم مال هر کشوری که باشد، دستکم ۲ ملوان هندی در جریان حمله ما کشته یا زخمی می شود.
سبحان الله !</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16285" target="_blank">📅 18:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16284">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭕️
قیمت‌ «سیمکارت سفید» و «اینترنت پرو» در بازار سیاه چقدر است؟
🔹
اینترنت پرو و دسترسی بدون فیلتر از طریق کانال‌های غیررسمی و بازار سیاه فروخته می‌شود.
🔹
قیمت ۵۰ گیگ اینترنت پرو در بازار سیاه تا حدود ۱۲ میلیون تومان اعلام شده است.
🔹
سیمکارت‌های سفید با وعده اینترنت بدون فیلتر با قیمت‌هایی بین ۴۴ تا ۱۲۰ میلیون تومان فروخته می‌شوند.
🟢
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16284" target="_blank">📅 17:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16283">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔹
🔹
نشست مشترک رئیس جمهور چین و دونالد ترامپ برگزار شد
🔹
شی جین پینگ، رئیس جمهور چین، در نشستی در پکن به دونالد ترامپ، رئیس جمهور آمریکا، گفت: «ما باید شریک باشیم، نه رقیب»
🔹
ترامپ در سخنانش، از «رابطه فوق‌العاده» خود با شی تمجید کرد و گفت رهبران تجاری ایالات متحده برای «ادای احترام» به شی و چین در این شهر هستند
🔘
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16283" target="_blank">📅 14:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16282">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۶ ماه پیش …
امروز مس دوباره ATH زد!</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16282" target="_blank">📅 14:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16281">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔹
چین با تغییر نام روبیو اجازه ورود او به پکن را داد
مارکو روبیو، وزیر امور خارجه آمریکا، که تحت تحریم‌های چین قرار دارد، با تغییر ترجمه نامش به «مارکو لو» توانست همراه رئیس‌جمهور ترامپ در نشست با شی جین‌پینگ در پکن شرکت کند. چین با این روش دیپلماتیک تحریم‌ها را لغو نکرده اما ورود او را ممکن ساخت.
روبیو به دلیل انتقاد از سرکوب‌های چین در هنگ کنگ و وضعیت اقلیت اویغور در سین‌کیانگ در دوران سناتوری‌اش تحریم شده بود. او همچنین از تصویب قانون پیشگیری از کار اجباری اویغور حمایت کرده بود
🟢
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16281" target="_blank">📅 13:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16280">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تنش‌های میان ترکیه با یونان دارد دوباره داغ می شود….</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16280" target="_blank">📅 13:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16279">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مقامات اسرائیلی به آکسیوس گفتند: «ما در انتظار تصمیم ترامپ برای از سرگیری جنگ، وضعیت حداکثری هشدار را در طول آخر هفته افزایش خواهیم داد».</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16279" target="_blank">📅 13:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16278">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزارت امور خارجه هند اعلام کرد که دیروز کشتی‌ای که پرچم هند را برافراشته بود در سواحل عمان مورد حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16278" target="_blank">📅 13:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16277">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">من 7.5 سال پیش گفته بودم که از اهداف اصلی ترامپ در تشدید تنش با ایران، دزدیدن مشتری های نفتی ما است که اینک دیگر به صورت کامل در حال تحقق است.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16277" target="_blank">📅 12:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16276">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حسین شریعتمداری: بحرین خاک ماست و باید به ایران بازگردانده شود
شریعتمداری در روزنامه کیهان نوشت:
این جزیره ایرانی در تابستان سال ۱۳۵۰ و در جریان یک زد و بند خیانت‌آمیز میان شاه معدوم و دولت‌های انگلیس و آمریکا از ایران جدا شده است و از آن هنگام تاکنون یکی از اصلی‌ترین خواسته‌های مردم بحرین، بازگشت این استان جدا شده از ایران به سرزمین اصلی و مادری خود، یعنی ایران اسلامی است.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16276" target="_blank">📅 12:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16275">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
علی کیایی فر؛
کارشناس امنیت اطلاعات:
بانکها در جنگ ۱۲ روزه ، ازسرور یک مدرسه علمیه خواهران در قم هک شدند</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16275" target="_blank">📅 12:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16274">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در طرح جدید سپاه، کل منطقه بین این 2 خط تیره حوزه دریایی تحت کنترل ایران تعریف شده که ملاحظه می کنید بندر کلیدی فجیره نیز درون این حریم قرار گرفته است.  در واقع آمده اند تا خود فجیره این حریم را تعریف کرده اند تا امارات نتواند از این بندر صادرات جایگزین انجام…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16274" target="_blank">📅 11:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16273">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPz5YAghrmHHGDC-m9ck344cr9OZtYlkHkpx-uqhHJ4C1-OOiZMA68mhnhdJh12ATtQjrX_yVOG1Gc163iOnGcyIUfMDxp7G3Wu185lCA6sVvuk1--R2JnTSt5SGmnBRloM01Vm2WpeTEwdBu1304wQDn2gsnB_3m2VGLREWR3FjpG4X3uLQryJGo-4Iedn-m6woWG4GKf6MUVQkw-RHgEI9DfBX0Ny_NiQzBNgX_k0axKF2tw1CqTHZ3NfpQWfSQ9dyV0jLkuRQg50agjaSk-VdGaw8RpQDHtd6OJ3FA9mMyqcUdNRuh4KSeJW8gMRhtZHc-ADJj-CgYgKMUhaaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بحران سیاسی بریتانیا و تأثیر آن بر پوند و دارایی‌های انگلیسی
بحران سیاسی بریتانیا و افزایش احتمال استعفای کییر استارمر باعث فشار بر پوند و افت بازارهای سهام انگلیس شده است.
سرمایه‌گذاران نگران‌اند که ادامه بی‌ثباتی سیاسی، هزینه‌های استقراض را افزایش داده و نوسانات بیشتری در دارایی‌های انگلیسی ایجاد کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16273" target="_blank">📅 11:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16272">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بحران برق در کوبا  کوبا در حال حاضر با یکی از شدیدترین بحران‌های انرژی در تاریخ معاصر خود روبه‌رو است. آنچه در ابتدا به‌صورت کمبودهای دوره‌ای برق آغاز شد، اکنون به یک وضعیت اضطراری سراسری تبدیل شده که با خاموشی‌های طولانی، کمبود سوخت و پیامدهای جدی اقتصادی…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16272" target="_blank">📅 10:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16271">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بحران برق در کوبا
کوبا در حال حاضر با یکی از شدیدترین بحران‌های انرژی در تاریخ معاصر خود روبه‌رو است. آنچه در ابتدا به‌صورت کمبودهای دوره‌ای برق آغاز شد، اکنون به یک وضعیت اضطراری سراسری تبدیل شده که با خاموشی‌های طولانی، کمبود سوخت و پیامدهای جدی اقتصادی و انسانی همراه است.
در بسیاری از مناطق کشور، مردم روزانه تا ۲۰ ساعت قطع برق را تجربه می‌کنند؛ مسئله‌ای که تقریباً تمام جنبه‌های زندگی روزمره را مختل کرده است.
ریشه‌های این بحران در فرسودگی زیرساخت‌های برق کوبا و وابستگی شدید این کشور به سوخت وارداتی قرار دارد. بخش بزرگی از شبکه برق کوبا همچنان متکی به نیروگاه‌های حرارتی دوران شوروی است که چندین دهه عمر دارند و به‌شدت فرسوده و غیرقابل‌اعتماد شده‌اند. سال‌ها کمبود سرمایه‌گذاری، مشکلات نگهداری و کمبود قطعات یدکی، این سیستم را تا حدی تضعیف کرده که خرابی تنها یک نیروگاه بزرگ می‌تواند خاموشی‌های زنجیره‌ای گسترده‌ای در سراسر جزیره ایجاد کند.
این وضعیت در سال ۲۰۲۶ شدیدتر شد؛ زمانی که واردات سوخت کوبا به‌شدت کاهش یافت. ونزوئلا که به صورت تاریخی مهم‌ترین تأمین‌کننده نفت کوبا بود، به‌دلیل مشکلات اقتصادی داخلی صادرات خود را کاهش داد. هم‌زمان، ایالات متحده فشار بر کشورها و شرکت‌های صادرکننده سوخت به کوبا را از طریق تحریم‌ها و محدودیت‌های مالی افزایش داد. مقام‌های کوبایی اعلام کردند که ذخایر دیزل و نفت کوره کشور تقریباً به پایان رسیده و این مسئله توانایی اداره نیروگاه‌ها، سیستم حمل‌ونقل و ژنراتورهای اضطراری را مختل کرده است.
پیامدهای خاموشی‌ها بسیار فراتر از مسئله برق است. سیستم‌های توزیع آب به‌دلیل ناتوانی پمپ‌های برقی در عملکرد مداوم، مرتباً دچار اختلال می‌شوند. بیمارستان‌ها برای حفظ خدمات درمانی در طول خاموشی‌های طولانی با مشکلات جدی مواجه‌اند و کمبود امکانات سرمایشی، نگهداری مواد غذایی و داروها را تهدید می‌کند. حمل‌ونقل عمومی به‌دلیل کمبود سوخت بی‌ثبات شده و خدمات جمع‌آوری زباله در برخی شهرها تقریباً فروپاشیده است؛ مسئله‌ای که نگرانی‌های بهداشتی ایجاد کرده است.
بحران انرژی همچنین مشکلات اقتصادی گسترده‌تر کوبا را تشدید کرده است. صنعت گردشگری، که یکی از منابع اصلی ارز خارجی کشور محسوب می‌شود، به‌دلیل اختلال در فعالیت هتل‌ها و فرودگاه‌ها آسیب دیده است. تولید صنعتی نیز به‌شدت کاهش یافته و بسیاری از کسب‌وکارها بدون برق پایدار قادر به فعالیت عادی نیستند.
مسئولیت این بحران همچنان موضوعی سیاسی و بحث‌برانگیز است. دولت کوبا تحریم‌ها و محدودیت‌های سوختی آمریکا را عامل اصلی فروپاشی می‌داند. منتقدان اما دهه‌ها سوءمدیریت اقتصادی، نوسازی ناکافی زیرساخت‌ها و وابستگی بیش‌ازحد به تأمین‌کنندگان خارجی انرژی را از عوامل اصلی بحران معرفی می‌کنند.</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16271" target="_blank">📅 10:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16270">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ریزپهپادهای حزب‌الله   فیلم‌هایی از جنوب لبنان تایید کرده‌اند که حزب‌الله بارها اهداف ارتش اسرائیل، به ویژه تانک‌ها را هدف قرار داده است، در حالی که اسرائیل به عمق بیشتری در سرزمین‌های جنوب رود لیتانی فشار می‌آورد   گزارش‌ها تایید می‌کنند که یک حمله پهپادی…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16270" target="_blank">📅 09:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16269">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJttfvmUBgzbzEgX4mpd1V69yoaWgSoi7RRS0-jWrOIIFD2fulMm9o1eG_OI04yzrlCjz_1xUfM4K8oTVIYdMzyAiLZ8mSfRM0e7BPSBClqqdDaNeu5mfRkYTyGCWaEfuZeWPenbimuCyr70dwn2hCFiR9yZdVk3h4_xsNh68JzsOBC-0HI9TX-ukDSH-VNTwjdoEK2LNI5vXDXJiorI9GT2DayakTkgw41hO7KDZsRiCw2m8sOipKk4WnacAgRzMBsemB9oIVbYjHwEroyecpcnihALDEk8XyRQT8bi8MmcTP7gLA5qu3P1CY4bVrl4SkhNHHEFk_DyV2NYYJ3uYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2 سال پیش آگاه است که بستن تنگه هرمز بیش از همه به سود روسها بوده و هست و چینی ها ابداً از ادامه مسدود بودن این تنگه سود نمی برند و لذا فشارشان بر جمهوری اسلامی برای پذیرش توافق کاملاً قابل توجیه است.  بد نیست بدانید اکنون بیش از 90%…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SBoxxx/16269" target="_blank">📅 09:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16267">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUqXzGeuWAKlAM6mJelZyb6Uq4vmsYUh8seUGJWxh-NVp_Zc337RmHLjRufekCOLoeYLvA49dT-C2jezAu03VieyKWwskJGAB7118rd__KLn2WfVQRVDqicHtVsNyyqj2mOgS6F0Mrf4BUChAF_bw988Ryg7ZtzMcAGfVKrpWhDb0LaZBD3wknWp8PL9ysH_yVta3-F212bsgXcoKqGDMI3IQX5otKFG_bBFyz-oLck1fDjFsk364z1tqraEIOvYbXEyf4QNgjsD8zXFyeS7jL-UEJNpGsCOHQsQa2Fug2KlWdhEvNmEsZTWQ21cOFORNrHDxOmr-Yu8fAur9GQLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خط لوله حبشان به فجیره بود که اماراتی ها می خواستند از آن استفاده کنند تا به تنگه هرمز بی نیاز بشوند که ولی خب.</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/16267" target="_blank">📅 09:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16266">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایلان ماسک می‌گوید مشکل سوسیالیسم این است که «بعد از اینکه آن‌ها «ثروتمندان را خوردند»، گرسنه خواهند ماند.»</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/16266" target="_blank">📅 09:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16265">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چرا مخالفت ونس نمیتواند منجر به اخراج او از سوی ترامپ بشود؟!
در ساختار سیاسی ایالات متحده، رئیس‌جمهور نمی‌تواند معاون رئیس‌جمهور خود را برکنار کند، زیرا معاون رئیس‌جمهور صرفاً یک مقام اجرایی منصوب‌شده نیست، بلکه مقامی مستقل و منتخب در چارچوب قانون اساسی آمریکا محسوب می‌شود.
رئیس‌جمهور و معاون او به‌صورت مشترک در انتخابات سراسری و از طریق سیستم کالج الکترال انتخاب می‌شوند و به همین دلیل رابطه میان آن‌ها شبیه رابطه رئیس با یک کارمند کابینه نیست. وزرا و مقامات اجرایی توسط رئیس‌جمهور منصوب می‌شوند و او می‌تواند آن‌ها را عزل کند، اما معاون رئیس‌جمهور دارای مشروعیت انتخاباتی مستقل است و رئیس‌جمهور اختیار قانونی برای اخراج او ندارد.
معاون رئیس‌جمهور تنها در چند حالت می‌تواند از مقام خود کنار برود: استعفا، فوت، برکناری از طریق فرآیند استیضاح و محکومیت در کنگره، یا تبدیل شدن به رئیس‌جمهور در صورت ناتوانی یا مرگ رئیس‌جمهور.
البته رئیس‌جمهور می‌تواند از نظر سیاسی معاون خود را به حاشیه براند؛ برای مثال او را از جلسات مهم کنار بگذارد، اختیارات غیررسمی‌اش را کاهش دهد یا در انتخابات بعدی فرد دیگری را به‌عنوان معاون انتخاب کند، اما از نظر حقوقی امکان اخراج مستقیم معاون رئیس‌جمهور وجود ندارد.
این استقلال همچنین به متمم بیست‌وپنجم قانون اساسی مرتبط است که در موضوع ناتوانی رئیس‌جمهور، نقش مهمی برای معاون رئیس‌جمهور در نظر گرفته است.</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16265" target="_blank">📅 09:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16264">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کره جنوبی:  «ما به شدت حمله به یک کشتی باری کره‌ای را محکوم می‌کنیم و قصد داریم پس از شناسایی مهاجم، به او پاسخ دهیم».</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16264" target="_blank">📅 08:21 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/XsC6sW3Ug4EOkokJQpk_lMnxVg9_YQ0I4pzD-VZsv1pRr7dvE1TahgD4Brr_EZbxf47ZbsGbKd6K3AgHnImN6wUt4VZ8nGqlOmHEzKTUptt3oEB0AKU-HeL5Y3YLeB2LZFRCGsSul7ZKgIuELS1FMsDvFADoh8vOcBlxewx5omDIpF3zoCBX5L24X2lIlHRzrauF6-Oy_y-TaId4HRaV0aZ_BhaWIQFaZfbWE-ppm8oatz-G-iUXwNWAN2EOByoXic-e4iwxL3e4J-yaM24SeLM9YrsMiMBJ1oDPCdQG5FNx56XGii6V83gZKJ4CIEfKrnDOWIzqkTakku2YyHnuVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 11:07:53</div>
<hr>

<div class="tg-post" id="msg-672874">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
انهدام یک پهپاد MQ9 در اهواز
🔹
دقایقی قبل، یک پهپاد MQ9 با آتش سامانهٔ نوین پدافند پیشرفتهٔ نیروی هوافضای سپاه و تحت کنترل شبکهٔ یکپارچهٔ پدافند هوایی کشور، در آسمان اهواز ساقط شد.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/akhbarefori/672874" target="_blank">📅 11:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672873">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKE941khMiPYbMzBf2N2KMKdluFE6FQS4MNIFPVcvxB1QLygKHdsBKjP2KKZzdWhKmyStrQhLBjZUfXyqwR3Py1eBxkAOiFgu6dMVoFhYPG3Ej9yD-ZL4fL_wkIPjfd4aCnNXwxljnmGjWEjyMihorXhoMMEmg6IxfOKAYf4DmnQCGPtg2AFSzezbJwTs9Wkakz8jOPKm_S1FGFglStpD44PSi5gdPjSlTtC536CynS5s43kgfh6AjQPk9a9G39F1iklsp_LaF-6LcpxrBsT_QTmndnGjRP5uSLEOrkV3XrDHo_7WjaKe-EODLufekE0aB4xGSAcTF7yKr2410f8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر نفت آمریکا به کمترین سطح در بیش از ۴۰ سال اخیر رسید
آژانس بین‌المللی انرژی (IEA):
🔹
ذخایر نفت خام آمریکا با کاهش به ۷۲۶ میلیون بشکه، به پایین‌ترین سطح در بیش از چهار دهه گذشته رسیده است.
🔹
برداشت گسترده از ذخایر راهبردی در جریان جنگ با ایران و کاهش ذخایر تجاری، نگرانی‌ها درباره امنیت انرژی آمریکا را افزایش داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/akhbarefori/672873" target="_blank">📅 11:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672872">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی شورای‌ نگهبان:‌ مجلس از هفته آینده به کار خود ادامه خواهد داد.
🔹
مهاجرانی: دولت بازسازی مناطق آسیب‌دیده را در دستور کار قرار داده است.
🔹
کارت ورود به جلسه آزمون دستیاری بر روی سایت سنجش آموزش پزشکی منتشر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/akhbarefori/672872" target="_blank">📅 10:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672871">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pblsvR8OtxrW-88kDFWpMKVUkr8wjDt_9qjWC6NHYfL4J1NJZQ_w0WXTT0kBu-ds1LfYCkC9qnXRmVJOT8WyAdpfVOA9FNtjj7aq9rVGvbaG6QJj2pehzzDAHiubUmRvSTyDvZkl6ZWEl7XRwEMo4u-GkX58-yIPv2AxIYhOtDOL78syFatHkj17aImS7qadZBHKl0jTFZx-MB-gEkTKJ9xs8ddtg8XmEavdtOTjnRUPW1g6CTjbCcn0iNO9I1rBm6GCR_cpKg_3Mjs2fTwnX4WULESvR7FJFCKdZ0nO7TGDk4cKZgzpe_V1KCXNILNcc2svhCmXkT1cE0eQAD-uYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید گاز ایران؛ ۲ برابر سریع‌تر از جهان
🔸
ایران در سال ۲۰۲۵ با تولید ۲۶۴.۸ میلیارد مترمکعب گاز و سهم ۶.۳ درصدی از تولید جهان، سومین تولیدکننده بزرگ گاز طبیعی جهان شد.
🔸
میانگین رشد سالانه تولید گاز ایران در بازه ۲۰۱۵ تا ۲۰۲۵، با نرخ ۳.۷ درصد،
بیش از دو برابر میانگین جهانی
(۱.۸ درصد) بوده است.
@amarfact</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/672871" target="_blank">📅 10:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672870">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7297470d33.mp4?token=qW1kMzkdebXZIHdSrhp4HFsNdZJx3-CrF5FUtXACVHDZhOdEBDOdHmAyCT5CXgUzyxvPG76Zk3md51dZ9zzKT7tQDvJAznX3ZeYQhkUl_Vue_OVAiQExkPHfr6_pRe5eIOszXS7QC5koB-p4UZMM5iIw6LuFpepRkhxhfqCW0Z_EjZhz1HVJb9Qc88rnypW83FmX2WjRpsQ0DpGo1osWGZ-S37Y-ciTb0nxVGcdw3qouZlzesYC0DUfvCBMfic_1N-LVJZKkg73Yg-OxdUMlwSI4uHrJI7xhAnXnfAesUJCnXYA48cqFJ5w63QohsAsoEx2a5gI7wOBGerdLC9TFIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7297470d33.mp4?token=qW1kMzkdebXZIHdSrhp4HFsNdZJx3-CrF5FUtXACVHDZhOdEBDOdHmAyCT5CXgUzyxvPG76Zk3md51dZ9zzKT7tQDvJAznX3ZeYQhkUl_Vue_OVAiQExkPHfr6_pRe5eIOszXS7QC5koB-p4UZMM5iIw6LuFpepRkhxhfqCW0Z_EjZhz1HVJb9Qc88rnypW83FmX2WjRpsQ0DpGo1osWGZ-S37Y-ciTb0nxVGcdw3qouZlzesYC0DUfvCBMfic_1N-LVJZKkg73Yg-OxdUMlwSI4uHrJI7xhAnXnfAesUJCnXYA48cqFJ5w63QohsAsoEx2a5gI7wOBGerdLC9TFIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشر شده توسط خبرگزاری  «اسپوتنیک» از حملات موشکی روسیه به کی‌یف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/672870" target="_blank">📅 10:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672869">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5597b0e4e.mp4?token=DHzXb3k28kpMFHtzVwpE4VGyEBJwIdr7G1QA7F9OKnpj3Oa43BCsFsv1aRhPmusqQZpvXHCNzzEaIcGaxQeLiDni6_tGnaNaE0SGoV4aZAhkopvuTmuaAMkSfgWuuwze0EKAj99V-vUAWMMKXhk2Nzj79Lm0i2a-k4W8kRuovnJGnt0nB2GCalN1RnUgl0QMD5UlYMYv2fIz7ysTUxT-yv-f3fTGHYLUSqsrlRXZYT2NIInCa0XuGtYLFMTod7G60yMAvM39CpgaeBqIm-tWlohKLbZTfdFareu08wXwTMVMlPWWFaXtG0zBLOZsJGX-NLtN5pheAy6c94H5pZfevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5597b0e4e.mp4?token=DHzXb3k28kpMFHtzVwpE4VGyEBJwIdr7G1QA7F9OKnpj3Oa43BCsFsv1aRhPmusqQZpvXHCNzzEaIcGaxQeLiDni6_tGnaNaE0SGoV4aZAhkopvuTmuaAMkSfgWuuwze0EKAj99V-vUAWMMKXhk2Nzj79Lm0i2a-k4W8kRuovnJGnt0nB2GCalN1RnUgl0QMD5UlYMYv2fIz7ysTUxT-yv-f3fTGHYLUSqsrlRXZYT2NIInCa0XuGtYLFMTod7G60yMAvM39CpgaeBqIm-tWlohKLbZTfdFareu08wXwTMVMlPWWFaXtG0zBLOZsJGX-NLtN5pheAy6c94H5pZfevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ ایده جذاب؛ برای داشتن آشپزخانه‌ای بی
‌
نقص
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/672869" target="_blank">📅 10:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672868">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
فرمانداری شهرستان چابهار: صدای انفجار شنیده‌ شده در روز جاری (۲۸ تیر) در حوالی شهر چابهار، ناشی از عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده است
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/672868" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672867">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e43d0a32.mp4?token=DNlzfdjGJf4C-0EM5xYDNdOJlis7KZWWadBebveK2z4aHb7J936HzTrMFGXl1QjNYnKTDDiURpB_o0O_bjopIm0aiXOjAHaMfiS9eC30rC3CLzPq8Y1cMQ-xadHyTFYaBeo2U5PNYWrx2Q9M5QEsz5QzTqmqFOpJqUghNKgWIuwRCi7JOECHkSjFhPo24-WKUegU7iGp17z5AWuHlQmMXjwjq16auSn1ZgFaGf0Z1JGsTf34csmqsqJdeEaDqsGFbI_OH5jjwsII88qRhhvvSi1MitI4w8gBZtCQ5oIIRDvN_ruigk3jWLbBMA9GpeDefCmXeVeN2lZ6CQ9uDqS2wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e43d0a32.mp4?token=DNlzfdjGJf4C-0EM5xYDNdOJlis7KZWWadBebveK2z4aHb7J936HzTrMFGXl1QjNYnKTDDiURpB_o0O_bjopIm0aiXOjAHaMfiS9eC30rC3CLzPq8Y1cMQ-xadHyTFYaBeo2U5PNYWrx2Q9M5QEsz5QzTqmqFOpJqUghNKgWIuwRCi7JOECHkSjFhPo24-WKUegU7iGp17z5AWuHlQmMXjwjq16auSn1ZgFaGf0Z1JGsTf34csmqsqJdeEaDqsGFbI_OH5jjwsII88qRhhvvSi1MitI4w8gBZtCQ5oIIRDvN_ruigk3jWLbBMA9GpeDefCmXeVeN2lZ6CQ9uDqS2wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری گزارش کردند که هشدارهای حملهٔ هوایی در کویت فعال شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/672867" target="_blank">📅 10:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672866">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
انهدام یک پهپاد MQ9 در اهواز
🔹
دقایقی قبل، یک پهپاد MQ9 با آتش سامانهٔ نوین پدافند پیشرفتهٔ نیروی هوافضای سپاه و تحت کنترل شبکهٔ یکپارچهٔ پدافند هوایی کشور، در آسمان اهواز ساقط شد.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/672866" target="_blank">📅 10:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672865">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8401e7c6a4.mp4?token=cvtRz6_1LJowkjm2ggO494YdU3yfgMWKm07IwWzoqFTQGHgIBJ5zGjoiWhKOMCCn3XKcp_m7cPdsff1ifXECngGvKuSCBaPMgZuQwiU19mt5t49Hv0gC7dVRpf64mVNUg39icfw--ezDmdFe-ZvG1V8-YUwVHCRDDw_GSNv4mF-yQwZUXt5PZz-CbAGXxssQdytgRjfIBLWFDCFl--8F8Vsc0OAflq5-1010Brk4QOzSq5o7eWlNUNEBUk3gp3IKS3S9eUEKnU3EPVZtBxhvQe1tTWvpM4zsh45Ta2EJVZGaCGEvdvX0TiFuGTo5fGMoZe5--JYzPvUXyNsPvq5pNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8401e7c6a4.mp4?token=cvtRz6_1LJowkjm2ggO494YdU3yfgMWKm07IwWzoqFTQGHgIBJ5zGjoiWhKOMCCn3XKcp_m7cPdsff1ifXECngGvKuSCBaPMgZuQwiU19mt5t49Hv0gC7dVRpf64mVNUg39icfw--ezDmdFe-ZvG1V8-YUwVHCRDDw_GSNv4mF-yQwZUXt5PZz-CbAGXxssQdytgRjfIBLWFDCFl--8F8Vsc0OAflq5-1010Brk4QOzSq5o7eWlNUNEBUk3gp3IKS3S9eUEKnU3EPVZtBxhvQe1tTWvpM4zsh45Ta2EJVZGaCGEvdvX0TiFuGTo5fGMoZe5--JYzPvUXyNsPvq5pNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی ۲۰۲۶
🔹
برنامه بازی‌ روز آخر مرحله حذفی #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/672865" target="_blank">📅 10:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672864">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
این‌بار پاستا رو به سبک انیمیشن باد برمی‌خیزد درست کن
🍝
مواد لازم:
🔹
اسپاگتی ۲۰۰گرم
🔹
گوجه‌فرنگی ۴عدد
🔹
سیر ۲حبه
🔹
روغن زیتون ۲قاشق غذاخوری
🔹
ریحان تازه
🔹
نمک و فلفل به مقدار لازم
🔹
پنیر پارمزان اختیاری #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/672864" target="_blank">📅 10:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672863">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
منابع خبری گزارش کردند که هشدارهای حملهٔ هوایی در کویت فعال شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/672863" target="_blank">📅 10:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672862">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
منابع خبری گزارش کردند که هشدارهای حملهٔ هوایی در کویت فعال شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/672862" target="_blank">📅 10:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672861">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdd44b039.mp4?token=CLAxzj_OBOqlbKwXjCJZMQDYdCMJS_iQ778WY63Pt1yjS0Yevl5PHcGz2hc1DCkAhBKuWGRrOaPq-7mwsCIeHxClNnJHVDKwfuXxR4a4cDaHWpf1qCdMOufgCo45dIH8fcEudKR2iy3Bamngu63bFvC6XgePQ-_FXSBh8PyKRAKuj6ie0rDFQes2BXc1uhca9Kicvw69Fxn-dHHWhXO__s0uRvF9C9P5lpH2_neVuv2R_cUONFhxxav-G4xWsqrZ0eH5xQJ81pxfyxtQgm6CZNK2EnAfbT7RsWn1QLAa6tMGrraOEShWsadsbUDUoLmGdtjgkKNTINSz7uHakBanSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdd44b039.mp4?token=CLAxzj_OBOqlbKwXjCJZMQDYdCMJS_iQ778WY63Pt1yjS0Yevl5PHcGz2hc1DCkAhBKuWGRrOaPq-7mwsCIeHxClNnJHVDKwfuXxR4a4cDaHWpf1qCdMOufgCo45dIH8fcEudKR2iy3Bamngu63bFvC6XgePQ-_FXSBh8PyKRAKuj6ie0rDFQes2BXc1uhca9Kicvw69Fxn-dHHWhXO__s0uRvF9C9P5lpH2_neVuv2R_cUONFhxxav-G4xWsqrZ0eH5xQJ81pxfyxtQgm6CZNK2EnAfbT7RsWn1QLAa6tMGrraOEShWsadsbUDUoLmGdtjgkKNTINSz7uHakBanSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ضبط‌شده توسط یک سرباز آمریکایی در پایگاه هوایی موفق السلطی در اردن
🔹
حداقل دو سرباز در این حمله‌ی ایران کشته شده‌اند، بسیاری زخمی شده‌اند که حال تعدادی از آنها وخیم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/672861" target="_blank">📅 10:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672860">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGs4s_lsWidc4D8MXKGL3BIJfTgvTxhp_VN8r9bE6gDqSuWKj9KbplMWcqaFhNZFCHouB8zbASDoR1LjyF5SVTSlMAggJENpPciVB7FXN3rsj_d_yDSE3f_290QuOh3JAA-xxhr0ihW690dh1oFOLVPD9FOkzmZjU09N5BiE9KP6L7a_G1ud1GtZpEWBzpKiEPAiR_MPj2_UNXkIB6clHcg42zLrqeINnEvTx7zhxdRT0G3JzDbtvaqbvC_QlrLOUKtejrg5vRDrqXHu1Ab-iJXkf8ytsNxz5cFLiatQi83EsuuWB7PjLNbC6jYl-dkOFwL4YeceC4bnbrkgp3s9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی خطاب به سربازان آمریکایی: فرار کنید؛ حتی یک ثانیه را هم از دست ندهید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/672860" target="_blank">📅 10:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672858">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
آژیرهای هشدار در کویت به صدا درآمدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/672858" target="_blank">📅 09:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672857">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsmYlMllRudnX9KXTaP1JCHRh2jyUUyvbf2lbehMz3A5Fy0qXhHaxv3wUEp1-PmjvD_E3BlmCvi_GN85RYxrdqB7_HJJJTSdLcQLIBjlRdnk-hjFGbLBlxjgo-GwxghQVMfXiFrl34tPer27x_NufoThhP0K1unBFRJ5qt5MjlfuDEkeNZl_zyXK78qHNCGDaWz00BsT4SBnHLII1kI19rAk8yolovx7TG_GtHQeujn1LMbVkU2d_GapNrvBVNowjvlu7QZWgxKtNGlvahbwYrk16ZLbdivEVp6Pa_wKQ_aRhu38DkSX3uOcbWLK9E_fEjMtYRqGIVASgOpB9xdpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران تشنه همدلی ماست
🔹
بیایید با چند تغییر ساده در سبک زندگی، از ارزشمندترین سرمایه کشور محافظت کنیم.
🔹
هر قطره، امید فرداست. #همه_باهم_برای_ایران #صرفه_جویی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/672857" target="_blank">📅 09:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672855">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس پلیس راه مازندران: تردد در محور هراز فردا و پس‌فردا ممنوع است
🔹
پیش فروش بلیت‌ قطارهای مسافری برای مرداد از فردا آغاز می‌شود
🔹
سازمان سنجش: نتایج نهایی آزمون دکتری سال ۱۴۰۵ در دهه اول مرداد اعلام ‌می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/672855" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672854">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سپاه اصفهان: تا ساعت ۱۳ امروز احتمال شنیدن صدای انفجارهای کنترل‌شده در جنوب کاشان وجود دارد
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/672854" target="_blank">📅 09:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672853">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ایران به عربستان سعودی و عمان گفته که قصد دارد «به شدت» امارات متحده عربی را هدف قرار دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/672853" target="_blank">📅 09:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672852">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
هراس از عملیات ترور؛ اسرائیل استفاده از پهپادهای شخصی را ممنوع کرد
🔹
کابینه امنیتی رژیم صهیونیستی به دلیل نگرانی از استفاده ایران از پهپادهای شخصی برای ترور مقامات، از جمله نتانیاهو، استفاده از این پهپادها را به مدت ۶ ماه ممنوع اعلام کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/672852" target="_blank">📅 09:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672851">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLI_e8vuaYNGtOe6Gp040aehLqi9JyGdCcSMVwDdHcj1rEEqLm34iTu9_2LST4nmTRytNXwpQVs4QjtCUndchWEjxEeAYkYBi_uNN15dQb_2Mj_jzHpiBbmZNs0z8S9IUi5_AGjLp89VMk3jhvsRRqrWzfYu-KFr4odpg6dRCFG8liv3BJrTNIjj0LQN5A7jqBoqViOCP_aF45ZHhcqW_2r-L6nQGNL1tfsd2K_y1p9K51NBk8iiWUbEUIDTA09ZhzpBJVuETpbuUsfY922YKZchNAkdDCNCqfjr-fmkeQC1YLo7JncTIsYDQDcEw0XJopggwnTrtpuIpxHb8hM3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سدهای مهم کشور چقدر آب دارند؟
شرکت مدیریت منابع آب ایران:
🔹
تا ۲۴ تیرماه، ۶۲ درصد از ظرفیت سدهای مهم کشور پر شده است؛ بر اساس این گزارش، حجم آب موجود در مخازن ۳۸ درصد و میزان ورودی آب از ابتدای سال آبی تاکنون ۷۶ درصد نسبت به مدت مشابه سال گذشته افزایش یافته است.
🔹
همچنین در حالی که سدهای «نهند»، «آزادی» و «ایلام» کاملاً پر هستند، ۶ سد شامل «لار»، «دوستی»، «طرق»، «پانزده خرداد»، «بارزو» و «ساوه» با کمتر از ۱۰ درصد ظرفیت، وضعیت نگران‌کننده‌ای دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/672851" target="_blank">📅 09:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672850">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_iL7TLPuEjcL5wOsOxZ8Vd5QqzhAiLVRmirtpKXybmdthYnA-HPgVL6zhsv04hPJ0Fl2v4xpG4haiKtZz8eZWueh4H9QZHhcHPfhEB3BoesWn26CKGDS-5fGY7binHCB3eL2yWn6Kl2jea8FDVzKnVyJPPVmvQ4HMwz9xy1ZioQwk3swI69izVpJHpAHq_bD5SCYQ5FXS8hj919s6-EiGCBGCTTbq3u29KLRWRZYiR4WrBfYRfxnxD0rOVce_ArbJAnah8LNcWswnDR7TQVryRkx2pKQExkPApW2xfqSq_KkJjzm9w_MdTj4qSmk997qgYFSyinzurLDhZv-3UFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هفتمین روز کاری متوالی ریزش شاخص بورس
🔹
شاخص کل بورس تهران در دقایق ابتدایی با افت ۴۱ هزار واحدی روبرو شد و به تراز ۴ میلیون و ۷۳۶ هزار واحد کاهش یافت .
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/672850" target="_blank">📅 09:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672849">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
شکست پدافندهای آمریکایی در رهگیری حملات به اربیل
یک منبع امنیتی در استان اربیل:
🔹
سامانه‌های دفاعی آمریکا در اربیل در رهگیری حملات موشکی و پهپادی شکست خورده‌اند.
🔹
این حملات منجر به تلفات و خسارت‌های مادی شد.
🔹
تلفاتی در میان نیروهای آمریکایی وجود دارد./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/672849" target="_blank">📅 09:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672848">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سامسونگ: هاله قرمز نمایشگر گلکسی S26 اولترا نرم‌افزاری است
🔹
سامسونگ با انتشار بیانیه‌ای رسمی، شایعات پیرامون نقص سخت‌افزاری نمایشگر گلکسی S26 اولترا را تکذیب کرد.
🔹
طبق اعلام این شرکت، متمایل شدن رنگ صفحه‌نمایش به قرمز، ناشی از اختلال در سیستم هوشمند تعادل رنگ‌ها هنگام قرارگیری در معرض نور شدید است و این مشکل با یک به‌روزرسانی نرم‌افزاری برطرف خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/672848" target="_blank">📅 09:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672847">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f2c9672b.mp4?token=OoTGSeD0cuAU_BETFbOBZosWwYBYxk-Vt70EK7GvwmHhq800skCzSJVjilbQZnUr0xCSe8ueUJMrZweiQcKwE6jfHSIECuDeyvOkVjfMCHzsXquLOjX7xCEpJxc-I81rUTkNzL9oYxh6uQwHAfkrn_2Bf2R5lBYKIw6xj3C5fmfORhCe9aqQqkglxHoUtsN5zPnBcaWAxI47MOqwmwYEOUUQjQusZgSIErSHf5ODtSftIfPYBBJhE-OJ7_feTfO9_UYmxyXkGBIOo6TCKeDGZJ1lCdFZNzhQORMr1rLuGryzAUc48JNjTTNg1ZqrPUVtZ0o1S2maf_eaFl9PyU596g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f2c9672b.mp4?token=OoTGSeD0cuAU_BETFbOBZosWwYBYxk-Vt70EK7GvwmHhq800skCzSJVjilbQZnUr0xCSe8ueUJMrZweiQcKwE6jfHSIECuDeyvOkVjfMCHzsXquLOjX7xCEpJxc-I81rUTkNzL9oYxh6uQwHAfkrn_2Bf2R5lBYKIw6xj3C5fmfORhCe9aqQqkglxHoUtsN5zPnBcaWAxI47MOqwmwYEOUUQjQusZgSIErSHf5ODtSftIfPYBBJhE-OJ7_feTfO9_UYmxyXkGBIOo6TCKeDGZJ1lCdFZNzhQORMr1rLuGryzAUc48JNjTTNg1ZqrPUVtZ0o1S2maf_eaFl9PyU596g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله هفدهم عملیات صاعقه ارتش؛ ادامه حملات پهپادهای ارتش به پایگاه های آمریکا در کویت
روابط عمومی ارتش:
🔹
در پی نقض معاهدات بین‌المللی و  جنایت‌های دشمن مستکبر در مناطق غیرنظامی، ارتش جمهوری اسلامی ایران در دور جدید حملات پهپادی و مرحله هفدهم عملیات صاعقه، از بامداد امروز، انبار مهمات ارتش تروریستی آمریکا در اردوگاه العدیری و سوله‌های تجهیزات و نفرات این ارتش کودک‌کش در پایگاه ‌علی‌السالم کویت را مجددا هدف حملات پهپادی قرار داد.
🔹
ارتش جمهوری اسلامی ایران تاکید کرد؛ جنگ ما دفاع  ازهویت اصیل و  تاریخ چند هزارساله ایران و مردمانی است که در پرتو تعالیم اسلامی نه ظلم می‌کنند و نه ظلم می‌پذیرند، براین اساس، رزمندگان ارتش، با اعتقاد عمیق به این آموزه الهی برای دفاع از مردم شریف در مصاف با دشمنان ایران و بشریت محکم و استوار ایستاده اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/672847" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672846">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07364b31d.mp4?token=GaFZZoGGWNI2ulq1PCvJkjW82gAeD8nevpXsE-Rbyt34cxewsQBouX51dSWbyQnQJbuO2piqOSexqilYG5s8LsvMeCMZOPUDgDq08ZMJWiXbIq095oiv1vnQJM7O8zaBDxHgUrSjmzu3luwP-L5oRGq_g5R1rD9BxHYDJCCD8yudbrDuuEEJHj5KyRaStigof1f8tiVPypoNecoEZARLE4clw3DAZv-MTDM4DqJScXpilCiicPb7JlySOGGEl8x81Iq4Or11EcOlRoiIcChru5_6KMfjKHGdVBACcps7T1J77HeNOjkKcQEysh5OXxvKHc-K7Y_XcihrluWaSNfM1RXTbSLcvQuUNX5ZiyWnv_pzqi57oYH_TER_1iRfRK6qUK43yD_P0IdIVdJlxDwEapFiOE1uHeDep4oPcSudmj5M0aY-7ALiSLN9vItSF0BWZiX_VkP3IShc5Hb2FXbSi4CgWblv5IUJ5Do_SfOpNWr8lauPvhBipghlMZaEH3DGYNXEoTuMzP7T-L8FSlki3DxtGkSFOsy3VgDENOsBUIh4iUenE-oDCrkro5MG4Rv6-k8jMRU51s_lEfSjedLC3D3ProYxQA_tpiGq6jcXviOhrCGeAJAMLyQNPsf1uIyUNhUyRuZGwEyHcAWowC0Pfa1aw0DqwyYWgxiyqWA-gEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07364b31d.mp4?token=GaFZZoGGWNI2ulq1PCvJkjW82gAeD8nevpXsE-Rbyt34cxewsQBouX51dSWbyQnQJbuO2piqOSexqilYG5s8LsvMeCMZOPUDgDq08ZMJWiXbIq095oiv1vnQJM7O8zaBDxHgUrSjmzu3luwP-L5oRGq_g5R1rD9BxHYDJCCD8yudbrDuuEEJHj5KyRaStigof1f8tiVPypoNecoEZARLE4clw3DAZv-MTDM4DqJScXpilCiicPb7JlySOGGEl8x81Iq4Or11EcOlRoiIcChru5_6KMfjKHGdVBACcps7T1J77HeNOjkKcQEysh5OXxvKHc-K7Y_XcihrluWaSNfM1RXTbSLcvQuUNX5ZiyWnv_pzqi57oYH_TER_1iRfRK6qUK43yD_P0IdIVdJlxDwEapFiOE1uHeDep4oPcSudmj5M0aY-7ALiSLN9vItSF0BWZiX_VkP3IShc5Hb2FXbSi4CgWblv5IUJ5Do_SfOpNWr8lauPvhBipghlMZaEH3DGYNXEoTuMzP7T-L8FSlki3DxtGkSFOsy3VgDENOsBUIh4iUenE-oDCrkro5MG4Rv6-k8jMRU51s_lEfSjedLC3D3ProYxQA_tpiGq6jcXviOhrCGeAJAMLyQNPsf1uIyUNhUyRuZGwEyHcAWowC0Pfa1aw0DqwyYWgxiyqWA-gEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف فرمانده ارشد پیشین نیروی دریایی آمریکا به اهداف احمقانه ترامپ برای حمله زمینی به ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/672846" target="_blank">📅 08:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672845">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haNGBLBhPPIpQEoxsW6ndeXwcEtJQEiWsJ8ASsiw5kvvHcwMLunpD3eTA0o2hxP4YW9fwO-_U4EtoyVX1Y101ouYtOklGikc2ea506hqONP1Jpc5Oed6Xal-r8k4jVUG1Di-XdXh0CQ5c84K_ePbgWlLtXlH5DMhogebMUMLeazePguOd0hrsSMt5kopAzk-uPy4egVxHvz9PohaobLn4lJ4AVNMvaioBEcS9Lnkkps1a6x8UxVq2KAc_IkQPYQPIlr7LXB_cVmsncowXxgGV-2xV_xhlubakMMX862t35bvThJh9esfF4XUFbVA2LkDzjt8Dgu2gLNAJcttc5uJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایج تقابل‌های اسپانیا و آرژانتین در طول تاریخ
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/672845" target="_blank">📅 08:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672844">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
معاون وزیرخارجه: مسیر جدیدی برای ورود و خروج شناورها به عمان پیشنهاد شد
غریب‌آبادی با رد هرگونه مسیر جنوبی و مذاکره با آمریکا:
🔹
ایران مسئولیت مین‌زداییِ کل تنگه هرمز را بر عهده دارد و ضمن احترام به حاکمیت عمان، با هر هزینه‌ای از حاکمیت خود بر این آبراه دفاع خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/672844" target="_blank">📅 08:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672843">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
زمین لرزه ۵ ریشتری سالند خوزستان را لرزاند  مدیرعامل هلال‌احمر خوزستان:
🔹
ساعت ۰۵:۵۵ امروز یکشنبه ٢۸تیرماه، زلزله‌ای به بزرگی ۵ ریشتر در عمق ۱۲ کیلومتری، سالند از خوزستان را لرزاند.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/672843" target="_blank">📅 08:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672841">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402fe3c51b.mp4?token=CkIoNMqr4ZrKd3oMduX71LZeEOr_0z7pUwvpFO1HufRb6SVOrrl_XdYAcD3dD9dOqQ8d9uax3elvOVx0kLZqprpNd8I2pYMhZxTucwExpkJ5r74-EQFmfckPM30vzQICSHZ7gzauzqMOucR_jnX3D5VGks1MWAZVJvrVZxn411PyDZfUD0cFSVHe649EPMsupyEOFptIn_G3WnWPwCa1UwhtUhh8kCXNtqj8a8HHiGpCV3jJ91nr2ec1aDNvMCSu1AoyHtPpHJ3V3DT0Rhqj-YWvw56n8rdl-gaa9KkOuOB4UwENMXzqFH7A4g4gT62LiaCSJpma5TO9xAZXoKG34g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402fe3c51b.mp4?token=CkIoNMqr4ZrKd3oMduX71LZeEOr_0z7pUwvpFO1HufRb6SVOrrl_XdYAcD3dD9dOqQ8d9uax3elvOVx0kLZqprpNd8I2pYMhZxTucwExpkJ5r74-EQFmfckPM30vzQICSHZ7gzauzqMOucR_jnX3D5VGks1MWAZVJvrVZxn411PyDZfUD0cFSVHe649EPMsupyEOFptIn_G3WnWPwCa1UwhtUhh8kCXNtqj8a8HHiGpCV3jJ91nr2ec1aDNvMCSu1AoyHtPpHJ3V3DT0Rhqj-YWvw56n8rdl-gaa9KkOuOB4UwENMXzqFH7A4g4gT62LiaCSJpma5TO9xAZXoKG34g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هند نخستین موشک مداری خصوصی خود را با موفقیت پرتاب کرد
🔹
هند با پرتاب موفق موشک «ویکرام-۱» و قرارگیری آن در مدار ۴۵۰ کیلومتری، به‌عنوان سومین کشور جهان، قدرت عملیاتی بخش خصوصی خود را در صنعت پرتاب‌های فضایی به اثبات رساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/672841" target="_blank">📅 08:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672840">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnGMjMmCo_b1hFK9nNPmuftI0YBIWQuDKBTY4zkbnafFuHwwv3Tqah5bnUbQk87UW9TjMexJTFBF8PtR4vPKYSGa0O4l0GjjeyQ4P0vDahiKiOQNmA58DezixOIG6J7B7VgYR1xjy_QqEDbFvRSBBrMbRkv9yAgKhxvgZr5UJqLJ8Dc_8gA0ShQDIzpgWenj4IeV3GQOOd4YZ1gwzfXce1eKBhT62gDORX60VE_QYQnWYBKJXN0-WqzMum-zopuEOGCypBkdfIyxL_tzKa-_Hfwo91j8hieRuNHWNXCRxRIb49bv629hqDkOsXU5ebBTsa_XYAh8gBfw5YUBdy8zsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام جهانی ۲۰۲۶
🔹
برنامه بازی‌ روز آخر مرحله حذفی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/672840" target="_blank">📅 08:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672839">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f06efb4c.mp4?token=W3IsnfGxPbjk9Q8atuHUTLAUINakvSVZcXQtWqCw5sf-WD9sUeYjjFV6WZJZbCPN4At5XA6MrsIncDJCh_FiyCZpNjR9EFRopL8iqMFsY8u7JTtFORmy2Y7H3Wwr2DG1wYThJnFL8gnKt2RPluZcW6MWlaP4tPQ7vLvQqzMiJ_pRcJuWHRH-sqUR7MBviaCmdxpGOkZ0_8NNgwjxWDzWxWjZC_p-jVWmnBzpCUaBvOFhXAYiAVgAT16yUyhy6rIVrGjEIhTglvXPdiS40mI1ONJI6upWuzOwPch-8NElwZ0HybinepSQHNb_nj4IrIIzHq0ibYy1YbPuMKreL7QDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f06efb4c.mp4?token=W3IsnfGxPbjk9Q8atuHUTLAUINakvSVZcXQtWqCw5sf-WD9sUeYjjFV6WZJZbCPN4At5XA6MrsIncDJCh_FiyCZpNjR9EFRopL8iqMFsY8u7JTtFORmy2Y7H3Wwr2DG1wYThJnFL8gnKt2RPluZcW6MWlaP4tPQ7vLvQqzMiJ_pRcJuWHRH-sqUR7MBviaCmdxpGOkZ0_8NNgwjxWDzWxWjZC_p-jVWmnBzpCUaBvOFhXAYiAVgAT16yUyhy6rIVrGjEIhTglvXPdiS40mI1ONJI6upWuzOwPch-8NElwZ0HybinepSQHNb_nj4IrIIzHq0ibYy1YbPuMKreL7QDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با انجام این حرکات هم عضلات پات قوی میشه و هم درد زانوت کم میشه! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/672839" target="_blank">📅 08:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672838">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a02a765c10.mp4?token=RF2ItSkxrv5FrJNFaTjlm57jPi2g3yBGmhMiaY7VJqkj1CplAPyAEYcoRKQjLh1CK-j-xrxEWzMWJSGZoteWyUQOhh2baUbAJ_xnJYK4M0x4nT4qYhvg9R-RI-ooogS6o3uCFbrXNmdnPDXrBzQsOm0rM3sX0MUqiwgIkfIJtgkt_e3wuNtLjq5i1nlpZ6peR5RykjD9eiUQ-A8N3ApvGS74x1dz5AaCjJI-TSVs51-e1GfGZt3OanfmlXaRUIB8YQp5lmqjAy0i_FXr1-R7tij1u9lZ6OG8DwckeCa5Mj1zHif4yZ6v9B5rkMZ4lmgauEYL6rSShxizleVT6k1aoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a02a765c10.mp4?token=RF2ItSkxrv5FrJNFaTjlm57jPi2g3yBGmhMiaY7VJqkj1CplAPyAEYcoRKQjLh1CK-j-xrxEWzMWJSGZoteWyUQOhh2baUbAJ_xnJYK4M0x4nT4qYhvg9R-RI-ooogS6o3uCFbrXNmdnPDXrBzQsOm0rM3sX0MUqiwgIkfIJtgkt_e3wuNtLjq5i1nlpZ6peR5RykjD9eiUQ-A8N3ApvGS74x1dz5AaCjJI-TSVs51-e1GfGZt3OanfmlXaRUIB8YQp5lmqjAy0i_FXr1-R7tij1u9lZ6OG8DwckeCa5Mj1zHif4yZ6v9B5rkMZ4lmgauEYL6rSShxizleVT6k1aoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضاحیه‌ی داغدار
🔹
ساختمانِ زخم‌خورده در گذشته از تجاوزات رژیم صهیونسیتی در «بئرالعبد» تاب نیاورد و فرو ریخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/672838" target="_blank">📅 07:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672837">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
زمین لرزه ۵ ریشتری سالند خوزستان را لرزاند  مدیرعامل هلال‌احمر خوزستان:
🔹
ساعت ۰۵:۵۵ امروز یکشنبه ٢۸تیرماه، زلزله‌ای به بزرگی ۵ ریشتر در عمق ۱۲ کیلومتری، سالند از خوزستان را لرزاند.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/672837" target="_blank">📅 07:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7N989uJ7kUiP0SIgd-sDNviAsuxJj9RSAI_8ksUF7fiWgqQjATU5Tw6BeUQpVDltOit7u-dxcEqOoutxr4G4lvO5BEEl9FI16ppgFq8WJpVOBQqseAlPB7m7uLJ2wlHitSEWrHPbfQBX9P0HiqlZrOj3MCSTQSJUSyckhaii51CqDoy8Bbvu3y-WyCT2svJ5pEI51mGQ3nXVVPWTI9YetpMos40YIWIie3cvJAmr7UraSGXHbrG5YV-Cdwf7mbRP-PUVcD7CA3ai0ZoqtAoJ890ptvj_wwCWBecVm_QvXAdeFb5EXLej7XNSEEJl5fcGDr3hUFQihlgCHnEScaB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwlRuabs8EUpnPHZ5JGP6n-BU3YLV5NpCkB06E-Wge7-3ar9rpuYHV5-beCW7NWPVAg3dFm51QmwQgs631svLN7pob5YzYUKdQdqwoYiFB9de3ECBLkjRl_OAFYwz9gd3QyjKYSSP3Dh2VphqFtnHDBYyIZPo57nQv8Gx0Q9A7ql4LybT5Q0m2aDH3mi6ALecJyFa9lOh_auEk0IXmE4GfXp-WL1k_dncDddKcm4LWaF8KZDez1OOnf2_m4TOPLKDSW1nqP1osciBDMYCIO6HoPjw4jFicL4H-TJIamtAiZ0KjphHupyZ9yDeAxQ-ZxEwC_OacCnyKer8UcDi9UyRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1694542022.mp4?token=jtJLQ4VM8igAxyFryKYlL52UlLqhS2fcdrP03CbrJOCzEo7J1-1HjsW2jwd3INJu-YaaGdJ1fz1xnmnMnRZZHnfHDRxLcRfQfDCnIF9kdxkDSrES1A1JXruE62XV0XtKXM7lEb-E5V-SzEy4liuGG9hUMmEktd7fIB2xhdYsRk4Hqk34TnJ8AA962KR8xifY-rAezy-rCKiXImwcqbmEcWKo0Z3X8me0L3WMsGljBh07ZAIzrV-ZNdhH-oYcnlGK6bV9ODRAlV5oA8HC6jPKGBDEIn_6EnLPdsHabhQDeALJUuVHlmKzmGq6H9dnSEUgtZPRJht1JzzYHZwYc5C1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1694542022.mp4?token=jtJLQ4VM8igAxyFryKYlL52UlLqhS2fcdrP03CbrJOCzEo7J1-1HjsW2jwd3INJu-YaaGdJ1fz1xnmnMnRZZHnfHDRxLcRfQfDCnIF9kdxkDSrES1A1JXruE62XV0XtKXM7lEb-E5V-SzEy4liuGG9hUMmEktd7fIB2xhdYsRk4Hqk34TnJ8AA962KR8xifY-rAezy-rCKiXImwcqbmEcWKo0Z3X8me0L3WMsGljBh07ZAIzrV-ZNdhH-oYcnlGK6bV9ODRAlV5oA8HC6jPKGBDEIn_6EnLPdsHabhQDeALJUuVHlmKzmGq6H9dnSEUgtZPRJht1JzzYHZwYc5C1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیویورک دوباره تبدیل به ونیز شد
🔹
وضعیت نیویورک پس‌از بارش‌های سنگین در روزهای گذشته مورد توجه کاربران فضای مجازی قرار گرفته‌است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/672834" target="_blank">📅 07:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T24w71XDKlFPfrfCtUGbSVDLLaz6ocqwW3Ki_0oz0eQj-J8XnONvvk9sjMabfqzGuZ4mcbtXoyUgslTDfBrj6tUM5gUlb-6aG2UkVDsSLyk7Spr8BFRyLx_GC54M2g0xfubcIhBDSsKe3qfzPur045Me-TH-nTduHBN9VUbt0FxC8H1GP_ZH5oZrYg58Pe7FdLja8ehmlb2yrgx634Fo2lL-69AIJTVIq0_x3navflJIAUbjciULrH1RiMdK5iSZIgwOZSBi9WTgc8OqjazSu8W4-IQNaga_U-Dt7QZveTddeW9tldiUobLKqCGv6SHhx8MMQnGWAnj_BkVc87zamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۸ تیر ماه
۴ صفر ۱۴۴۸
۱۹ جولای ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672833" target="_blank">📅 07:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672832">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
زمین لرزه ۵ ریشتری سالند خوزستان را لرزاند
مدیرعامل هلال‌احمر خوزستان:
🔹
ساعت ۰۵:۵۵ امروز یکشنبه ٢۸تیرماه، زلزله‌ای به بزرگی ۵ ریشتر در عمق ۱۲ کیلومتری، سالند از خوزستان را لرزاند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/672832" target="_blank">📅 07:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672831">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ستاد فرماندهی مرکزی ایالات متحده:
ما هشتمین شب متوالی حملات علیه ایران را تکمیل کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/672831" target="_blank">📅 07:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672830">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
حمله موشکی آمریکا به اطراف شادگان
استانداری خوزستان:
🔹
در پی تهاجم موشکی آمریکا به خاک جمهوری اسلامی ایران، یک نقطه در اطراف شهر شادگان مورد اصابت موشک قرار گرفت. این حادثه هیچ‌گونه تلفات جانی در پی نداشته است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/672830" target="_blank">📅 07:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672829">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
هشدار قرارگاه خاتم‌الانبیا به دشمن: نیروهای مسلح به هرگونه وحشی‌گری پاسخی ویرانگر می‌دهند
سرلشکر عبداللهی:
🔹
با تبعیت از فرامین و تدابیر رهبر معظم انقلاب، به شیطان بزرگ و دشمن جنایتکار، عهدشکن و حیله‌گر آمریکایی یادآور می‌شویم هرگونه طمع‌ورزی، زورگویی، تمامیت‌خواهی و وحشی‌گری با پاسخ قاطع و ویرانگر رزمندگان مومن، شجاع و مقتدر در نیروهای مسلح مواجه می‌گردد و هزینه‌هایی سنگین‌تر از جنگ تحمیلی دوم و سوم بر آنان تحمیل می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/672829" target="_blank">📅 07:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672828">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db885829ed.mp4?token=lF_VJbH_TfiQZNQgKMYjTPnaFhgCW3yfg6CzP4XvOy9dsyi7gh43DUO3FxzsyBTSSz6IdY_5J2xwZD8QWrV7LmmLA5Pm5ONLh6R4M4pOXXZftesLl6bmzAvaKAUtznxS07X7x5Qp2TjxgTjkWxV8iMxBJh4JY30JX4BQwCgqRHqKraoOtkOcIeNoX8-tsk2chMx2BgecDAAAJbUJMTctxpzQPGNhC1nmfErDHH7vF3__8XTU-LjgMiLC7Scrqez0CRBBeVhsbAfT3gU0tu_vOwHif4YFHHOeZMgTGCWV4ENOX5FxQyj_97IJVlo9L_ubD328r_Op7hrdSLVjMs537g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db885829ed.mp4?token=lF_VJbH_TfiQZNQgKMYjTPnaFhgCW3yfg6CzP4XvOy9dsyi7gh43DUO3FxzsyBTSSz6IdY_5J2xwZD8QWrV7LmmLA5Pm5ONLh6R4M4pOXXZftesLl6bmzAvaKAUtznxS07X7x5Qp2TjxgTjkWxV8iMxBJh4JY30JX4BQwCgqRHqKraoOtkOcIeNoX8-tsk2chMx2BgecDAAAJbUJMTctxpzQPGNhC1nmfErDHH7vF3__8XTU-LjgMiLC7Scrqez0CRBBeVhsbAfT3gU0tu_vOwHif4YFHHOeZMgTGCWV4ENOX5FxQyj_97IJVlo9L_ubD328r_Op7hrdSLVjMs537g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش: دو پایگاه مهم آمریکا در کویت، آماج حملات پهپاد‌های انهدامی قرار گرفت
🔹
در پاسخ به تجاوزات مکرر دشمن، شهادت هم‌وطنان عزیز و حمله به پل‌ها، زیرساخت‌ها و مناطق غیر نظامی، ساعاتی قبل و در مرحلۀ شانزدهم عملیات صاعقه، ارتش جمهوری اسلامی ایران، انبار مهمات ارتش تروریستی آمریکا در اردوگاه العدیری و رادار پاتریوت و رادار هوایی این ارتش متجاوز در پایگاه علی‌السالم کویت را، آماج حملات پرحجم پهپاد‌های انهدامی خود قرار داد.
🔹
اردوگاه العدیری یکی از پایگاه‌های مهم ارتش تروریستی آمریکا در منطقه و در فاصلۀ ۱۰۴ کیلومتری مرز‌های جمهوری اسلامی ایران و ازمراکز مهم پشتیبانی و تجدید سازمان نیرو‌های آمریکایی است که اخلال در عملکرد این پایگاه تاثیر قابل توجهی بر عملیات‌های پشتیبانی ارتش در منطقه می‌گذارد.
🔹
پایگاه هوایی علی‌السالم نیز از پایگاه‌های مهم، مرکز اصلی ترابری هوایی و دروازۀ ورود نیرو‌های نظامی به منطقه غرب آسیاست که نقش محوری در راهبرد نظامی و لجستیکی ارتش متجاوز آمریکا در منطقه ایفا می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/672828" target="_blank">📅 07:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672827">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
حمله مجدد جنگنده‌های آمریکایی به مناطقی در قشم /  ۲ صدای انفجار شنیده شد
🔹
ساعت ۶:۱۰ صبح امروز جنگنده‌های آمریکایی بار دیگر مناطقی در جزیره قشم را هدف حمله قرار دادند.  بر‌اساس گزارش‌های اولیه، در پی این حمله دست‌کم دو صدای انفجار در نقاطی از جزیره شنیده شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/672827" target="_blank">📅 07:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672826">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
انهدام چندین هواپیمای نظامی آمریکایی در حملات ایران به اردن
🔹
روزنامۀ وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد که در حملات موشکی و پهپادی ایران در روزهای گذشته به پایگاه موفق السلطی اردن که با تلفات گستردۀ نظامیان آمریکایی همراه بود، چندین هواپیمای بدون‌سرنشین و سرنشین‌دار نیز مورد اصابت قرار گرفته و نابود شده‌اند.
🔹
کانال «نایا» نیز به نقل از منابع خود نوشته که یک فروند جنگندۀ اف-۱۵ در این پایگاه در حملات ایران منهدم شده است.
🔹
ساعاتی پیش نیز روزنامۀ نیویورک تایمز در گزارش خود نوشت که در حملات موشکی ایران چند بالگرد نظامی مورد هدف قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/672826" target="_blank">📅 05:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672825">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
درگیری‌های شدید بین افراد مسلح و نیروهای امنیتی دولت موقت سوریه
🔹
یک رسانه عربی از وقوع درگیری‌های شدید بین نیروهای امنیتی حکومت موقت سوریه و افراد مسلح در استان حلب در شمال این کشور طی شنبه‌شب خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/akhbarefori/672825" target="_blank">📅 04:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672824">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
استانداری هرمزگان: تا این لحظه اصابت موشک در بندرعباس نداشته‌ایم
🔹
در حال حاضر آرامش در منطقه برقرار بوده ‌و با وجود شنیده شدن برخی صداهای نامشخص، طبق آخرین گزارش‌ها تاکنون هیچ موردی از اصابت موشک در بندرعباس تأیید نشده است./ تسنیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/672824" target="_blank">📅 04:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672823">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در نزدیکی مرز کویت و عراق
🔹
شبکه الغد عراق از شنیده شدن صدای چند انفجار در نزدیکی مرز کویت و عراق خبر داد و نوشت: گزارش‌هایی از پرتاب موشک به سمت خاک جمهوری اسلامی ایران وجود دارد. تاکنون جزئیات بیشتری در این باره منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/672823" target="_blank">📅 04:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672822">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
حملات نظامی دشمن آمریکایی به حوالی قشم  استانداری هرمزگان:
🔹
در ساعت ۳:۴۰ نقطه‌ای در حوالی قشم هدف حمله نظامی دشمن آمریکایی قرار گرفت. در این حملات جدید آمریکا به قشم هیچ مصدوم غیر نظامی یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/672822" target="_blank">📅 04:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672821">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: هواپیماهای آمریکا در اردن هدف قرار گرفتند
🔹
روزنامه وال‌استریت ژورنال آمریکا گزارش داد که در حمله موشکی ایران به پایگاه موفق السلطی اردن متعلق به ارتش تروریستی آمریکا هواپیماهای با سرنشین و بدون سرنشین هدف قرار گرفتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/672821" target="_blank">📅 04:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672819">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
حملات نظامی دشمن آمریکایی به حوالی قشم
استانداری هرمزگان:
🔹
در ساعت ۳:۴۰ نقطه‌ای در حوالی قشم هدف حمله نظامی دشمن آمریکایی قرار گرفت. در این حملات جدید آمریکا به قشم هیچ مصدوم غیر نظامی یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/672819" target="_blank">📅 03:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672818">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای مردم قشم از اصابت‌ ۳ تا ۵ موشک در مناطق مختلف جزیره
🔹
حوالی ساعت ۳:۳۸ بامداد صدای چند انفجار در مناطق مختلف جزیره قشم شنیده شد. براساس مشاهدات میدانی ‌و اظهارات شماری از ساکنان محلی، چند نقطه در جزیره هدف اصابت قرار گرفته است.
🔹
برخی از ساکنان تعداد اصابت‌ها را بین ۳ تا ۵ مورد عنوان می‌کنند. تاکنون هیچ مقام رسمی درباره محل دقیق اصابت‌ها، علت انفجارها، میزان خسارات احتمالی یا تلفات این حمله اظهار نظر ‌نکرده است./ تسنیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/672818" target="_blank">📅 03:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672817">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
گزارش‌های تایید‌نشده از صدای انفجار در بندرعباس
🔹
از دقایقی پیش اخباری مبنی بر صدای انفجار در بندرعباس منتشر شد، اما ‌‌هنوز گزارشی از اصابت موشک یا حمله جنگنده‌های آمریکایی نداشته‌ایم.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/672817" target="_blank">📅 03:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672816">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
گزارش‌های تایید‌نشده از صدای انفجار در بندرعباس
🔹
از دقایقی پیش اخباری مبنی بر صدای انفجار در بندرعباس منتشر شد، اما ‌‌هنوز گزارشی از اصابت موشک یا حمله جنگنده‌های آمریکایی نداشته‌ایم.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/672816" target="_blank">📅 03:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672815">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
صدای انفجار در اهواز تکذیب شد
🔹
دقایقی پیش خبری مبنی بر حمله جنگنده‌های آمریکایی به مناطقی در اهواز منتشر شد که این خبر صحت ندارد و تا این لحظه هیچ گونه انفجار و حمله جنگنده های آمریکایی گزارش نشده است.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/672815" target="_blank">📅 03:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672814">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccZ68D75Nf4pyHx_opDxK4_Ojcc8T4gbsHdnzLV3R6uOs_EBNuikFHT8R5TZmsb9YaXf_lHUvCgTmYpMQ2oYlLKx_tVnnX_V8QHQaecV-AkqwNRsHJIMv-2LDsq4FmpdX0rlU4IVFATv_i9f2M76ni6QdOo_4ZP-OboqfVYAr2PrL876vsf4evC491I-bIALGSVLng2Jj-P0aXHxBDcljNKQ_eMP9pjx9D5T7in2FFt9bQXHZdp7GZlsidp5_8JmxjAtTtSn8rsmdkHSm5JfR50JmXM1cmISt-RD9jM1zKbzwzwDKdLzLXrzQ19K225RwERmnlSoCBvDNJY_oad-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مدال برنز بر گردن انگلیسی‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/672814" target="_blank">📅 03:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672812">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efef3f4c7.mp4?token=j7BKXw-NJ0gc7F1Vj_V7vZ9R_aFkAe1jJNCR5fURm1Wx1Nk0IdNon_NdYY18nV1OMWrmuDEcHPnd7ROUC40MM8-Z5PMl1g8Fieb0-AB8rfalVzMma9GA9xWkCr8XDkv1M8Dvi2DgpIsOqioZEkzoHjv5tSBjWzz87_8YsTIcM7RG0Bc-V2xTn2xmvz4hGI1XkEzQu2hGynKJsAPAftNmolSA4TIZmJBeZ4MTOB33PwLjXsEhQ-ZPk-jimyaS6R7qNLY9cdXInGM_y1j6WTEd-nHh4vJtVkeV8_otSSj0k9l9_xKAfzsMU6m5ojLmnzTllzA1xTh6WKTPyyGt-6VM2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efef3f4c7.mp4?token=j7BKXw-NJ0gc7F1Vj_V7vZ9R_aFkAe1jJNCR5fURm1Wx1Nk0IdNon_NdYY18nV1OMWrmuDEcHPnd7ROUC40MM8-Z5PMl1g8Fieb0-AB8rfalVzMma9GA9xWkCr8XDkv1M8Dvi2DgpIsOqioZEkzoHjv5tSBjWzz87_8YsTIcM7RG0Bc-V2xTn2xmvz4hGI1XkEzQu2hGynKJsAPAftNmolSA4TIZmJBeZ4MTOB33PwLjXsEhQ-ZPk-jimyaS6R7qNLY9cdXInGM_y1j6WTEd-nHh4vJtVkeV8_otSSj0k9l9_xKAfzsMU6m5ojLmnzTllzA1xTh6WKTPyyGt-6VM2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ اصابت پهپاد انتحاری به مقر گروهک‌های تجزیه‌طلب در اربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/672812" target="_blank">📅 02:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672811">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
فرماندار اراک هرگونه حادثه یا انفجار در این شهرستان را رد کرد
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/672811" target="_blank">📅 02:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672810">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
انفجار و حمله جنگنده‌های آمریکایی به قم تکذیب شد
🔹
در پی انتشار اخبار مبنی بر انفجار و حمله جنگنده‌های آمریکایی به مناطقی در قم، مسئولان امنیتی ضمن تکذیب این خبر اعلام کردند تا این لحظه گزارشی از انفجار نداشته‌ایم.
🔹
در حال حاضر امنیت در استان قم برقرار بوده و تاکنون هیچ انفجاری در هیچ نقطه‌ای در استان گزارش نشده است.‌
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/672810" target="_blank">📅 02:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
مقر گروهک «حزب آزادی کردستان» هدف حملات شدید قرار گرفت
🔹
گروهک «ارتش ملی کردستان» شاخه نظامی «حزب آزادی کردستان» اعلام کرد که مقرهای این گروهک تجزیه‌طلب در ابیل و سلیمانیه هدف حملات شدید از سمت ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/672809" target="_blank">📅 02:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672808">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
حملات نظامی دشمن آمریکایی به حوالی حاجی‌آباد
🔹
در ساعت ۲:۱۰ نقطه‌ای در حوالی حاجی‌آباد هدف حمله نظامی دشمن آمریکایی قرار گرفت. در حملات جدید آمریکا به حوالی حاجی آباد هیچ مصدوم یا خسارت به زیر ساخت های مسکونی و تجاری  گزارش نشده است./مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/672808" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672807">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90746d4c73.mp4?token=bDk7T2q_G80w9TGdk96ZxAQH1xY7WGVbx0ko89rigI0v-MJaj4hzi0FPM0V-MvVHe8xQuo5L6tuo75-EQuiZb_s-AA9qk6tmekg619I_2wOSCKd1XCDxOhQo4HJjcuUiGiXPay9VlK9L2kpnP8x33mLfBjtmgwN1cnQXiUhf4g13J1ogtP1d1Vyji0qr93lyRI0SzhcghDWAeR2esQiIZsY5AVC7MhVYgbdQVmcLlRYGGStn473m7NrKY9b9poA7qiTQj3WMemnxIH0bM6t_LjFEwCAXD1oj5jaH0mGKtU8FDHUwWAK7ptUh_niedJJFABBbDeHv22rH2UWZxZ1l0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90746d4c73.mp4?token=bDk7T2q_G80w9TGdk96ZxAQH1xY7WGVbx0ko89rigI0v-MJaj4hzi0FPM0V-MvVHe8xQuo5L6tuo75-EQuiZb_s-AA9qk6tmekg619I_2wOSCKd1XCDxOhQo4HJjcuUiGiXPay9VlK9L2kpnP8x33mLfBjtmgwN1cnQXiUhf4g13J1ogtP1d1Vyji0qr93lyRI0SzhcghDWAeR2esQiIZsY5AVC7MhVYgbdQVmcLlRYGGStn473m7NrKY9b9poA7qiTQj3WMemnxIH0bM6t_LjFEwCAXD1oj5jaH0mGKtU8FDHUwWAK7ptUh_niedJJFABBbDeHv22rH2UWZxZ1l0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک رده‌بندی در حد فینال با ۱۰ گل، گل ششم انگلیس به فرانسه توسط بلینگام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
6️⃣
🏆
4️⃣
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
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/672807" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672805">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXOwigpkfi4CwhLyRFU0X3fT3B9JZKq5Jre498z56Wd4EwFYx_yg3EXAeHy1lsjS2asyY9Z0KL4d-3XmyIVLFUiK5fEkZ0DUvxK0UGjdRi-dvhnI_i0aAyid79XEmvpZTfGt_kqYP1ZG6pUqI-ZgYT_i4b6p6c5iTY0PEoBcvN2Samr9Vq5aTsfB0GbUxy3dryLrR5HoL4T4xXI3vq_Sp6-AfdD9qjVvhInHVtoFSzNs0_UkUrCuwaJ2filTA5ATGwFZv_Q1zUxNlbLHqhfpUoWC6cK09s3MRuEVAk5CcuXb0T-6gzbueOT5SI-PSc5NZw81T1X9CqWjceWbbEEnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
انگلیس روی سکوی سوم جام جهانی ۲۰۲۶
🔹
تیم فوتبال انگلیس با پیروزی پرگل ۶ بر ۴ مقابل فرانسه، روی سکوی سوم جام جهانی ۲۰۲۶ ایستاد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/672805" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672804">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a14d10202.mp4?token=pBZfSy4UO_yA2IXivzZ0oGmk4ggRpNcP9-C5f0-S_fvz4VNrEUDOuSY4iXJGS2SXzTm7sRIrz1PkcMGCcl3ByEZF5zIt68YrbRQ4d1CjFscXrbOjuOtPK8oxbayXMOCPOZe7Zn30tk3SK2m1cPZiErMwWnQXVuInG55Je4vxeZ9VMOwbL3QVkzriWR-8KgMw2yrefFyxKAl33afE7Ow3IuaqSNjsAI3OGatdQjsOC2KZc4HTPsKh-lUmZnpoIfBD4ZXH87scOp-gevvmlwjvnS1ubgX3YyQDoXLJ3D5pk06pYKJ9tZe61BtBbFXXm0jX8WI-aHgYyV7mPXSL7CKWFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a14d10202.mp4?token=pBZfSy4UO_yA2IXivzZ0oGmk4ggRpNcP9-C5f0-S_fvz4VNrEUDOuSY4iXJGS2SXzTm7sRIrz1PkcMGCcl3ByEZF5zIt68YrbRQ4d1CjFscXrbOjuOtPK8oxbayXMOCPOZe7Zn30tk3SK2m1cPZiErMwWnQXVuInG55Je4vxeZ9VMOwbL3QVkzriWR-8KgMw2yrefFyxKAl33afE7Ow3IuaqSNjsAI3OGatdQjsOC2KZc4HTPsKh-lUmZnpoIfBD4ZXH87scOp-gevvmlwjvnS1ubgX3YyQDoXLJ3D5pk06pYKJ9tZe61BtBbFXXm0jX8WI-aHgYyV7mPXSL7CKWFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم فرانسه به انگلیس توسط دمبله
🏴󠁧󠁢󠁥󠁮󠁧󠁿
5️⃣
🏆
4️⃣
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
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/672804" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672803">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
صدای انفجار در اهواز تکذیب شد
🔹
دقایقی پیش خبری مبنی بر حمله جنگنده‌های آمریکایی به مناطقی در اهواز منتشر شد که این خبر صحت ندارد و تا این لحظه هیچ گونه انفجار و حمله جنگنده های آمریکایی گزارش نشده است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/672803" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672802">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
منابع بحرینی از پرواز پر حجم جنگنده‌های آمریکایی از خاک این کشور برای انجام حملات در ایران خبر می‌دهند/
فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/672802" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672801">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2785127527.mp4?token=ECksUq7SEBXAqcrRvvQznPxR_ZIo6aq8w23_fK0iCJreYZaRLkKtbyyk8DDdodEyEbBPXEJRW5S-swy8UrV3nCcPsbeIHke-OrgHvS3VD9ZbaPflEsCynMeK3JtdsHHYR9vDdgT5a5Ug1mqMSPP9gWrm-Te9yureVmG_sPNs1hRxN-Owopl8Ssb-1qxHIPqS3wcmfJrSrXIRXIhYyhWZ4d5hqPscK-rMPu-qJBWMX4S85_wIeZ2lu6vJhoHvlEhkcvq58HWkHVrcCCkb3ZK535cskK-oBxchFLyxJ-POqKImaIO1bqTMtIw9P6M5JKNnA9ngS7FJPyJpDHqtUXBMmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2785127527.mp4?token=ECksUq7SEBXAqcrRvvQznPxR_ZIo6aq8w23_fK0iCJreYZaRLkKtbyyk8DDdodEyEbBPXEJRW5S-swy8UrV3nCcPsbeIHke-OrgHvS3VD9ZbaPflEsCynMeK3JtdsHHYR9vDdgT5a5Ug1mqMSPP9gWrm-Te9yureVmG_sPNs1hRxN-Owopl8Ssb-1qxHIPqS3wcmfJrSrXIRXIhYyhWZ4d5hqPscK-rMPu-qJBWMX4S85_wIeZ2lu6vJhoHvlEhkcvq58HWkHVrcCCkb3ZK535cskK-oBxchFLyxJ-POqKImaIO1bqTMtIw9P6M5JKNnA9ngS7FJPyJpDHqtUXBMmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل پنجم برای انگلیس از روی نقطه پنالتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
5️⃣
🏆
3️⃣
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
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/672801" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672800">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
استانداری هرمزگان: علیرغم برخی خبرها در فضای مجازی، برخوردی در بند لنگه گزارش نشده است
/ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/672800" target="_blank">📅 02:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672799">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b93e8cca8.mp4?token=J6Z-Y2IM5lFkTMCbh4zvmX_-qUPxL6a6zpNDeBVq4-JhbeIOm1qTJbHreVE4j1eWVsoQWoGstmZ-dRJ5XeOm5N0YHGh75nTf_Uqu_yzDu6i6Y9bDAr36oz-gTsSSFUHVljDLAWAErtUvYi7NGztA24pncwUqX_A81rWurfeA1p6PQb6HwmZwrz3pSwWtv5zSsu0gQYfYbEJs3epCH3MxRC8WiZu_58rzb0Qmu-Z2Q1vuEwYd78IqlzsjM1Mi4CyCh_Nxcy7wpcf0ZIk4WwAtRt5hSiLNWpnUmYmQ85TEkNjg65scP7Kyk_us7zC1kxi-DDNJPlY6zw3Ip4__dOsVIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b93e8cca8.mp4?token=J6Z-Y2IM5lFkTMCbh4zvmX_-qUPxL6a6zpNDeBVq4-JhbeIOm1qTJbHreVE4j1eWVsoQWoGstmZ-dRJ5XeOm5N0YHGh75nTf_Uqu_yzDu6i6Y9bDAr36oz-gTsSSFUHVljDLAWAErtUvYi7NGztA24pncwUqX_A81rWurfeA1p6PQb6HwmZwrz3pSwWtv5zSsu0gQYfYbEJs3epCH3MxRC8WiZu_58rzb0Qmu-Z2Q1vuEwYd78IqlzsjM1Mi4CyCh_Nxcy7wpcf0ZIk4WwAtRt5hSiLNWpnUmYmQ85TEkNjg65scP7Kyk_us7zC1kxi-DDNJPlY6zw3Ip4__dOsVIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در مقر گروهک‌های تجزیه‌طلب اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/672799" target="_blank">📅 02:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672798">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
گزارش‌های تایید‌ نشده از صدای انفجار در بندرعباس و بندرلنگه
🔹
از دقایقی پیش اخباری مبنی بر صدای انفجار در بندرعباس و بندرلنگه منتشر شد که مسئولان استانداری هرمزگان ضمن تایید این صداها می‌گویند هنوز گزارشی از اصابت موشک یا حمله جنگنده‌های آمریکایی نداشته‌ایم.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/672798" target="_blank">📅 02:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672797">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zof9YiBwxSoRclEv-7eX1O2SQUGFOGTBRizXTjbaau4fuomBnxvUWfIro0FXTy2a46aJlzOkrRv11y4ghqyGkgea5DYn5ILJyH2DHhlKQkTPcRaGXRP2G26c5j8ZWJ1CE8zCUcyoclsshz2Y3rudS--bvWOZ3eYYc9eiHrbg3M5J8w6xrDb4fIUeTJsoxMGYMnPv8Rj0AoKb2BUpffBHrg-Mu8pDkN7bYfaRYVODWs7Y5S5nEf93lEZOLDYih6lxGASGVaeDiUHxkI06fXkO_vSHPb5R6nFix8VlfkUPbuYUhg8ccoOze9Xe3y4ZMVK-8FWzfReCyzM2pq63uvI1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امباپه با ۲۲ گل بهترین گلزن تاریخ جام‌جهانی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/672797" target="_blank">📅 02:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672796">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
شنیده شدن صدای پرواز جنگنده در کیش
🔹
در جزیره کیش دقایقی پیش صدای پرواز یک یا چند فروند جنگنده را در آسمان این جزیره شنیده‌ شد. گفته می‌شود با وجود شنیده شدن این صدا، تا این لحظه هیچ‌گونه صدای انفجار یا حادثه امنیتی در سطح جزیره گزارش نشده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/672796" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672795">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا مدعی انتقام از ایران به خاطر سربازانش در اردن شد
🔹
ارتش تروریستی آمریکا در پیامی که دقایقی قبل منتشر شد، ادعا کرد: «حملات جدید به ایران با هدف مجازات فوری سپاه پاسداران به خاطر حملاتش علیه نیروهای نظامی ایالات متحده در اردن انجام می‌شود.»/ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/672795" target="_blank">📅 02:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672794">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0813f70fda.mp4?token=WmjN64--QkJ9vwdaRMcIeWRdHMvG3yBOkdo3o16qShTV9L6t9UR071gRgqcHtk0dTmZqlSkstifAWsb6jLkzviRnJePlRnW80Dn2MS1-o2ejMHJZtxUIV4VUSIHlHRZInFQJdFttx2G1k8nZt0qMYg5Veq4HtcEw2uMyBmBEKK3FkxgaQR7RzOGBhEUeG5qWtNfUCZevfaSdIE-m8PmT2oPPQwpjmJG6h3CZqZkD8SH3iWXMo9b8_NrT65U5oUnoTe1LS-7b7FwtCh41pFYDcMD0GJJs-TWWXX5ruVO78t3ib6mYrNj47R4cIuqvtUWz_rjNz_Xe12LR0xy0LAiVeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0813f70fda.mp4?token=WmjN64--QkJ9vwdaRMcIeWRdHMvG3yBOkdo3o16qShTV9L6t9UR071gRgqcHtk0dTmZqlSkstifAWsb6jLkzviRnJePlRnW80Dn2MS1-o2ejMHJZtxUIV4VUSIHlHRZInFQJdFttx2G1k8nZt0qMYg5Veq4HtcEw2uMyBmBEKK3FkxgaQR7RzOGBhEUeG5qWtNfUCZevfaSdIE-m8PmT2oPPQwpjmJG6h3CZqZkD8SH3iWXMo9b8_NrT65U5oUnoTe1LS-7b7FwtCh41pFYDcMD0GJJs-TWWXX5ruVO78t3ib6mYrNj47R4cIuqvtUWz_rjNz_Xe12LR0xy0LAiVeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرانسه در آستانه کامبک زدن، گل سوم فرانسه به انگلیس توسط امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
3️⃣
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
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/672794" target="_blank">📅 02:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672793">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
منابع عراقی از حملات سایبری علیه شرکت‌های گازی اماراتی و آمریکایی در اربیل خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/672793" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672792">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
حملات نظامی دشمن آمریکایی به حوالی سیریک
🔹
در ساعت ۱:۳۰ نقطه ای در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت.
🔹
در حملات جدید آمریکا به سیریک هیچ مصدوم یا خسارت به زیر ساخت های مسکونی و تجاری  گزارش نشده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/672792" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672791">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سنتکام: به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه اهدافی در ایران آغاز کردیم
🔹
امروز ساعت ۶ عصر به وقت شرقی آمریکا، نیروهای آمریکایی به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/672791" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672790">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
منابع عراقی: حملۀ پهپادی به کنسولگری آمریکا در اربیل ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/672790" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672789">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
سنتکام: به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه اهدافی در ایران آغاز کردیم
🔹
امروز ساعت ۶ عصر به وقت شرقی آمریکا، نیروهای آمریکایی به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/672789" target="_blank">📅 01:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672788">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
منابع عراقی: حملۀ پهپادی به کنسولگری آمریکا در اربیل ادامه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/672788" target="_blank">📅 01:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672786">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=tfzwm9Fxa01blINuPwP8JmcciD-oe0v7M2lK9yvdtB_BFQTnI7UfBgVC_3wWW1rW5G9_YBLsvO2v9H51kkX7OF09Bu0JQkuTzytnZ0UrXWbn7RvGrXYZr6eOdRhcQrm0dl6yt0jJe5tIfB2ua2BONrMgrRgNJDzSzATyNALxb1TCu-4XRKvz6JqSr3g_hYwBzNb_vuFNfVeMp_KPc_7CA__vROWXVO6ZWTAraGct7IKywAy33qxAtvQuoNaSeUy4A9goOnJnWAkm2LEC-9_JtoevkKTFJJvyWoigmczOtTGvKkTaH3cCMb-YAQhSDAkn7-IOHDPGEzkLYW-YBAINXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=tfzwm9Fxa01blINuPwP8JmcciD-oe0v7M2lK9yvdtB_BFQTnI7UfBgVC_3wWW1rW5G9_YBLsvO2v9H51kkX7OF09Bu0JQkuTzytnZ0UrXWbn7RvGrXYZr6eOdRhcQrm0dl6yt0jJe5tIfB2ua2BONrMgrRgNJDzSzATyNALxb1TCu-4XRKvz6JqSr3g_hYwBzNb_vuFNfVeMp_KPc_7CA__vROWXVO6ZWTAraGct7IKywAy33qxAtvQuoNaSeUy4A9goOnJnWAkm2LEC-9_JtoevkKTFJJvyWoigmczOtTGvKkTaH3cCMb-YAQhSDAkn7-IOHDPGEzkLYW-YBAINXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع ۵ انفجار در اربیل؛ سامانه پدافند هوایی کنسولگری آمریکا فعال شد
🔹
بر اساس این گزارش، هم‌زمان با وقوع این انفجارها، پهپادهایی نیز بر فراز آسمان اربیل در حال پرواز مشاهده شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/672786" target="_blank">📅 01:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672785">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d35cb592f.mp4?token=LgqikZTzA_L_AKQSNAw7j6zilX4SGosAvHMhhduOm6eqKz_sdNJuMB8Oh3jmUmNQShhalPzzI5uT6qsCxe_GAKR8ou9uK6jKSDLczSZ4PUpcp_qqcl5-vZJL4bhJFPVH2QLBCWL_EAimouMNvMMKFE_eJ8QEjjmNIErgT08PFr5x28Z6X9V3aF24CA70FyXn-rdbyHC4uhfASXWKsflXrCMsscb-1X_GpeyIP6pKeOigLnh4JvLOIYCu3_x9TwsncfqNhcYdYg_SfazUV-q5s7PYKM02uoHxIfMW4nKbhI2ZZmHbbcuZxeQcz1wlwKfeSapWS2Gn-TMtetMYtG6FJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d35cb592f.mp4?token=LgqikZTzA_L_AKQSNAw7j6zilX4SGosAvHMhhduOm6eqKz_sdNJuMB8Oh3jmUmNQShhalPzzI5uT6qsCxe_GAKR8ou9uK6jKSDLczSZ4PUpcp_qqcl5-vZJL4bhJFPVH2QLBCWL_EAimouMNvMMKFE_eJ8QEjjmNIErgT08PFr5x28Z6X9V3aF24CA70FyXn-rdbyHC4uhfASXWKsflXrCMsscb-1X_GpeyIP6pKeOigLnh4JvLOIYCu3_x9TwsncfqNhcYdYg_SfazUV-q5s7PYKM02uoHxIfMW4nKbhI2ZZmHbbcuZxeQcz1wlwKfeSapWS2Gn-TMtetMYtG6FJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرانسه به خودش آمد، گل دوم فرانسه به انگلیس توسط بارکولا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
2️⃣
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
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/672785" target="_blank">📅 01:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672784">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27409c54f4.mp4?token=NJMLnE0deph-dCcBqD8qBhNliBTR9GwZcBzRlOdObshLFJJG2aAYsa_Om0A_6sX50K2hYcf8SWRCfgjVIyEVg_Z0lfG-wMbUqwb4Plrs3WFde8z41RsBYdrUshznlulI7piO7qJ6Tm9YuG-u1bZeGeAZIMlk5CKgdF8LGdH-0GN1Q7Dg0p1ZNFgyY7kpl3UNL0owsNPGcp4yIKPPT6ebrf8LO3ux1kmppHioSFCuP-IpOy_78PCzSLsH7HsrXVl16ZskZbX_11_7lfzHu8REEmxHrVyeL9H5tBGXgxcxrLDMmzaBMPoH8adet43MFnnW5rRgnBFeuDJccsztvNCfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27409c54f4.mp4?token=NJMLnE0deph-dCcBqD8qBhNliBTR9GwZcBzRlOdObshLFJJG2aAYsa_Om0A_6sX50K2hYcf8SWRCfgjVIyEVg_Z0lfG-wMbUqwb4Plrs3WFde8z41RsBYdrUshznlulI7piO7qJ6Tm9YuG-u1bZeGeAZIMlk5CKgdF8LGdH-0GN1Q7Dg0p1ZNFgyY7kpl3UNL0owsNPGcp4yIKPPT6ebrf8LO3ux1kmppHioSFCuP-IpOy_78PCzSLsH7HsrXVl16ZskZbX_11_7lfzHu8REEmxHrVyeL9H5tBGXgxcxrLDMmzaBMPoH8adet43MFnnW5rRgnBFeuDJccsztvNCfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به انگلیس توسط امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
1️⃣
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
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/672784" target="_blank">📅 01:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672783">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
رسانه‌های عراقی از وقوع چندین انفجار در کنسولگری آمریکا در اربیل خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/672783" target="_blank">📅 01:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672782">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b1c746642.mp4?token=SdqhU1sUVo0Cl9rDf80-F770vi3-8WFDWgqFqsReTtriDEwX3om6gga3x5KxaVidgXtOzSNnG68Ggk2XsDP060iK78CRX1Ep8gWjphZFHdVVTpmlaqrbZASoOXmrMC-dbAdrMr8PNUvvISVqTjr59P-bTmldMM8mM8q_P-dLZ1mbHnaKFvnchxurqJCXXiNzUG9IVBDnMGa-_A0DWhuPBBNmAzc_e4nDfxAcC4Fxta5EUs2oxh0zzxNO13jD6zV4nBjgxva9r0PPSBZwlshi4_o2xnFzZaj1taq9dWdNtjImyiKxBO43z_cU28ozgJXboYFEiqyjMv1DbmmurWgeRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b1c746642.mp4?token=SdqhU1sUVo0Cl9rDf80-F770vi3-8WFDWgqFqsReTtriDEwX3om6gga3x5KxaVidgXtOzSNnG68Ggk2XsDP060iK78CRX1Ep8gWjphZFHdVVTpmlaqrbZASoOXmrMC-dbAdrMr8PNUvvISVqTjr59P-bTmldMM8mM8q_P-dLZ1mbHnaKFvnchxurqJCXXiNzUG9IVBDnMGa-_A0DWhuPBBNmAzc_e4nDfxAcC4Fxta5EUs2oxh0zzxNO13jD6zV4nBjgxva9r0PPSBZwlshi4_o2xnFzZaj1taq9dWdNtjImyiKxBO43z_cU28ozgJXboYFEiqyjMv1DbmmurWgeRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نیروهای اشغالگر صهیونی  به محله الرامیس، در شمال قدس اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/672782" target="_blank">📅 01:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672781">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
انفجار در اربیل
🔹
منابع عراقی از شنیده شدن صدای انفجار در اربیل و فعال شدن سامانه‌های پاتریوت مستقر در پایگاه آمریکایی حریر خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/672781" target="_blank">📅 01:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672780">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
فعال سازی پدافند هوایی در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/672780" target="_blank">📅 01:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672779">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b100100dad.mp4?token=msFrQfjwVfMAcsUMi8FFRrjMCHfUMHxLZgTid0-i5u7nRJjGnY8mEbNLdp2KO0qU0QnR-S7ZrsfzTTyA670UFWS7bHzDfuUbXZJl92aCJxhK19Ck8SuoJ16eOU_Nw_N0VLnnOXn24rYqeeoss202RleLt8kARrVtWInWlgqnGGWr44knipY8Pdfgh0u0GW8ojED-cPmLHZh8o-ZfvW8-S3_frzNxaZW7p6xC0UIzhQUU4rOtMq4tsxDO5kZOJM2eiFjTgx_P1PlxEfiQxDCe_NlFtIVgsMlYTbj90Ne_rPczCnnPIZfH20bqE9tdJk1zp5Q-Qnb0L7KHlYhDEdTpww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b100100dad.mp4?token=msFrQfjwVfMAcsUMi8FFRrjMCHfUMHxLZgTid0-i5u7nRJjGnY8mEbNLdp2KO0qU0QnR-S7ZrsfzTTyA670UFWS7bHzDfuUbXZJl92aCJxhK19Ck8SuoJ16eOU_Nw_N0VLnnOXn24rYqeeoss202RleLt8kARrVtWInWlgqnGGWr44knipY8Pdfgh0u0GW8ojED-cPmLHZh8o-ZfvW8-S3_frzNxaZW7p6xC0UIzhQUU4rOtMq4tsxDO5kZOJM2eiFjTgx_P1PlxEfiQxDCe_NlFtIVgsMlYTbj90Ne_rPczCnnPIZfH20bqE9tdJk1zp5Q-Qnb0L7KHlYhDEdTpww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعال سازی پدافند هوایی در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/672779" target="_blank">📅 01:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672778">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2530637954.mp4?token=DLjqnGk3ZVHgdXjDmRWyBdmaYVMpv5Mp7Y_bQbpneQGAOkHs08Y5Qa8MArlaUyuEgxLyJcU84a3xBwXdQKlu-YGxsTYbPHKS4n9JX-3826pFGKSQRknTRGcIZLmOolBhErDtOa0cMJKii4HWrDlA6tKaZZglY9ZcyhVXFR03ATFQm6fileChcZqftnv0RYuPmGfuz-hGsa-L0QnIyYN_2uhWHEx9oW1rZ3jLPA8GfwTwreRB-A8gfhRhk5STYRP4SgQPU2WtLDHIHZFAjHwM8HyQIcRVg4f8WwmRTUmd8zEUkvM0QDIFIeFJ7VLS1ZbFW5G2sZjyRPA4M-_BTU1U9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2530637954.mp4?token=DLjqnGk3ZVHgdXjDmRWyBdmaYVMpv5Mp7Y_bQbpneQGAOkHs08Y5Qa8MArlaUyuEgxLyJcU84a3xBwXdQKlu-YGxsTYbPHKS4n9JX-3826pFGKSQRknTRGcIZLmOolBhErDtOa0cMJKii4HWrDlA6tKaZZglY9ZcyhVXFR03ATFQm6fileChcZqftnv0RYuPmGfuz-hGsa-L0QnIyYN_2uhWHEx9oW1rZ3jLPA8GfwTwreRB-A8gfhRhk5STYRP4SgQPU2WtLDHIHZFAjHwM8HyQIcRVg4f8WwmRTUmd8zEUkvM0QDIFIeFJ7VLS1ZbFW5G2sZjyRPA4M-_BTU1U9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تازه از لحظه شلیک موشک از کویت به سمت ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/672778" target="_blank">📅 01:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672777">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc83a1fc86.mp4?token=M7Eu83G7nSstAcsdeqRh41kzFE0OVxKbmqDDDTihetk2j_S84jegYd4JecjnhyyneuWFThjaU9vLRjdsHMxCJdtPJ1AZ8l6IBEv8-oPCTvnMZt8qwn4s4PPQGeEhQPC0pDSyeYJ4yfiotAAzg5_BWqX9iX-XFWJ85VhXNsElHUb4NeY982tbeOKuet5HCT1rcg4VcmmW2k13NUeGviANX8IkxAlecqYZu3oidmWoDUDf__O21GMeUHnIVOmXrvt7KVcv7S_LUxA_Ck7Ox2sD-cRne_r4ZQvQSyWFa_VpXygRR17azYIdggsduVzcXXu2Ax4oTbdBQ8sP6Jxc7JTOfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc83a1fc86.mp4?token=M7Eu83G7nSstAcsdeqRh41kzFE0OVxKbmqDDDTihetk2j_S84jegYd4JecjnhyyneuWFThjaU9vLRjdsHMxCJdtPJ1AZ8l6IBEv8-oPCTvnMZt8qwn4s4PPQGeEhQPC0pDSyeYJ4yfiotAAzg5_BWqX9iX-XFWJ85VhXNsElHUb4NeY982tbeOKuet5HCT1rcg4VcmmW2k13NUeGviANX8IkxAlecqYZu3oidmWoDUDf__O21GMeUHnIVOmXrvt7KVcv7S_LUxA_Ck7Ox2sD-cRne_r4ZQvQSyWFa_VpXygRR17azYIdggsduVzcXXu2Ax4oTbdBQ8sP6Jxc7JTOfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم انگلیس به فرانسه توسط ساکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
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
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/672777" target="_blank">📅 01:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672776">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5f17f766.mp4?token=BxhWVSMndOGVCQgGiHTvlF5B0PWa_Q8AKlFTkXts7iEmoUgYXuH4S95MjpStN31igvF3iQfFGoOR1HnHAnxbPEcbw9-7Sd3jKO5DImBfuCNCuH7IE3QEAVEzqGlxDdZFy6rQtX_8qqD4V7ipmqI0OXir3r2N6TdGgEjiLOvNC6q5zqgBOF7-VrElZX-oPxl3549QiIAL_wV0HTkB7BUWQjhuKH2Ge7ExDhYnCdPinJ4wxJNTX2duR_wFZyyg2xBk8n8w8Efb2hjwh11nKeUjavUwYnOYhWUbnwp_vIkOEzTASx1UZVU7iJng0LEg-6dYt4xllA4NkW3B61QXRI2-tpixxjLZCDvVGZmgyIYoutSdvvUN0qKpOYzy-fPR96NBucgWht7_6Ba27Yo8IOawHff5HNXb-UnaHs0lOBZCh_TCARpnnDEUl3Ohl_8oKyyYantevisCJpya_KgDk1I1DY29cDALR1eOpcAoTNP7bl-I7m3fyu20E2eT9A4wWXIOIYhbgb3aht_cbwXcpDqwQxG6XVNYeSxrW65ShkSHeAh7emcVMpDkWGq_k9iiIAqfuYNEXWBYlxMhysZ_oOUwZgr0p5TNqye9r1A7_cqiLtXe1qfts_uYm1lTYF-0qr3-96Dki-0rOdMEF7-ubawwuIcHDEFQNfn3afi-XmTJHyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5f17f766.mp4?token=BxhWVSMndOGVCQgGiHTvlF5B0PWa_Q8AKlFTkXts7iEmoUgYXuH4S95MjpStN31igvF3iQfFGoOR1HnHAnxbPEcbw9-7Sd3jKO5DImBfuCNCuH7IE3QEAVEzqGlxDdZFy6rQtX_8qqD4V7ipmqI0OXir3r2N6TdGgEjiLOvNC6q5zqgBOF7-VrElZX-oPxl3549QiIAL_wV0HTkB7BUWQjhuKH2Ge7ExDhYnCdPinJ4wxJNTX2duR_wFZyyg2xBk8n8w8Efb2hjwh11nKeUjavUwYnOYhWUbnwp_vIkOEzTASx1UZVU7iJng0LEg-6dYt4xllA4NkW3B61QXRI2-tpixxjLZCDvVGZmgyIYoutSdvvUN0qKpOYzy-fPR96NBucgWht7_6Ba27Yo8IOawHff5HNXb-UnaHs0lOBZCh_TCARpnnDEUl3Ohl_8oKyyYantevisCJpya_KgDk1I1DY29cDALR1eOpcAoTNP7bl-I7m3fyu20E2eT9A4wWXIOIYhbgb3aht_cbwXcpDqwQxG6XVNYeSxrW65ShkSHeAh7emcVMpDkWGq_k9iiIAqfuYNEXWBYlxMhysZ_oOUwZgr0p5TNqye9r1A7_cqiLtXe1qfts_uYm1lTYF-0qr3-96Dki-0rOdMEF7-ubawwuIcHDEFQNfn3afi-XmTJHyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم انگلیس به فرانسه توسط ساکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
3️⃣
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
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/672776" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672775">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
مدیرعامل شرکت آب و فاضلاب هرمزگان: تاسیسات آب‌شیرین‌کن بونجی در غرب شهرستان جاسک که در پی حمله بامداد شنبه ( ۲۷ تیر ) ارتش تروریستی آمریکا دچار آسیب شده بود، مرحله نخست بازسازی آن با موفقیت به پایان رسیده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/672775" target="_blank">📅 01:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672772">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpq0LEsDKJilUPMd3UlSZPHvLpdr8WmNByL8VROZiTX-LBFKi1q2m6-6k0cXXPHcQs5n14Q6Vojc1-zsYZQQIvDtQEikJPvgGKsdDKpRZ7mXBZjDV6A_Nm94oIlQJJ0XghNkPFlgIdj-aO09GGGgPgqUMZc57tVk6N3gMuOAMrY4lIqF52Y8Ti9PpEfkjr6nyzLLyODIfszt7vN1Xt9UnNVP5h7IkQMVtCVPLqp2POHzkqVwKqArkNqmXtWfOBoJbt87HlMhq6zDPzzSUA0WSlg8XWFAiYxlloDFtqkUmJvY366MDvF46nvl6vyaGUwc88LpMjTbDpEQycc8spTf1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LGg4TKcoQS8wKG_dKv-W-n7-hAHZ2pW_ieEsCCvgmED5bdldv8lwoKWmu99VC5bQfogin0Rk9wwl2Hl2053y0S5V5Gd5hLETBCfiCpKHUzS3YtIEO3W9JVHSQQQGvYyHCiXp9OCZweq5wRh2VkrQ-83LvOrdAhQL03io_kWzu_naDmlw8I5mCPkXEvKTZYPvkSGpda_cWk8oHUbZ0tBRKocIWNNNsybUjAoAhzVgz42biWSNd_JQBdvZmbhybTEG7lcQHpOQniE21tNB6EmEJ2Zje3conNNRbtxAzmJ0GipzwaNSEPhioS-fyDK9grq3k53WLA6RiJih9FzTlD5a3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4894ed02a.mp4?token=YgtyDC53-89DTF4-_XreBbhZ1cNuOqIw9uGIt_-pL01McNCFBAJtX7Z06-4TRnrpxwcD3lJnBRhKL8v1RDVFWH3HaiMQueQj_vCoNEaIrCQvxeZKla0FUaX6-Q_eO1IyLcutFK74oH3yD0ydhg6rCayxQVR_tc582ERP0OgRcDTIMimC7B4gFT0ME_wnwYbswSVFSDEOEK7ZvJ8voWXlVKBpqdy_o6PeCDjt9GLF05vaOJxSftH2n84oevAV-e7vsDhmSzQ0kHuj0KOAEmv3Gms-KCKu-42iqf8iIP7v8ypciwJSAN8FEL8ard6AdlyA4-M2FZ8JUzgZvQvVgujjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4894ed02a.mp4?token=YgtyDC53-89DTF4-_XreBbhZ1cNuOqIw9uGIt_-pL01McNCFBAJtX7Z06-4TRnrpxwcD3lJnBRhKL8v1RDVFWH3HaiMQueQj_vCoNEaIrCQvxeZKla0FUaX6-Q_eO1IyLcutFK74oH3yD0ydhg6rCayxQVR_tc582ERP0OgRcDTIMimC7B4gFT0ME_wnwYbswSVFSDEOEK7ZvJ8voWXlVKBpqdy_o6PeCDjt9GLF05vaOJxSftH2n84oevAV-e7vsDhmSzQ0kHuj0KOAEmv3Gms-KCKu-42iqf8iIP7v8ypciwJSAN8FEL8ard6AdlyA4-M2FZ8JUzgZvQvVgujjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوکراین به مرکز لجستیکی ویلبریز روسیه در شهر الکتروستا حمله کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/672772" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672771">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرفوری
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/672771" target="_blank">📅 01:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672770">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
خوک زرد در گفت‌وگو با NewsNation درباره پایان یافتن یادداشت تفاهم با ایران ادعا کرد: اصلاً برایم مهم نیست #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/672770" target="_blank">📅 00:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672769">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
خوک زرد در گفت‌وگو با NewsNation درباره پایان یافتن یادداشت تفاهم با ایران ادعا کرد: اصلاً برایم مهم نیست
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/672769" target="_blank">📅 00:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672768">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11dfde57a3.mp4?token=hdYbQGURWIye7NrIJGOoKv9L2qJqG6mEqzvosqMOj3eoSKBANZ8m-XDrGO5y-SoJ5mzbXr1ZLj1nIqSeZHEDJoY1tp5FXoG9Jelx-0-Bol8R9z18PdJlErL60pzCUAtHSe0_xdUy-ncc7Fd2zf0n-JFPwQ-yUpxUFWC7pRraY9_IOVhJK2sSlJPXT0SZFszbHr487-ZAxl8Zx1Mu-5te4Gf4lYBJFbK_7jl8O04WKTJLM2wChF3SitghnQVDMA1rQmT7gk7J5beAPQmj_Bw3OHQOF_jauWAVyj8bQXk492p6SAmixQGm-vVH6Zt7wZNknX8jbaeNbmG44EBkgcPqwF4b7LqbBKV3s8War_2trS96SSyPGCCemL0It8GdGkvar9TJEQ5oENpnu-sW4IUIKMiCuuInNY6zCQz1eD3aAshp2pHCDBw0VL6JPSil8SreQ3MnrPSJZjrW1mqFASHBAoPQ0Ohu4arPTZO3JVU4EkiPy-PXEeB-y59iajt50VscmD-bGoWo76JyDFvpjOEveQXIg8rjl8jAiLDNKSFXz5q8pugNSQxLiM_N16asJ_SYXyTbD8_8GqocT2drhhBu3dXjwsaeCkVqa3JqPf4XZz8mlicQf5xiAeX3XVYf4XxQNOh-lz5UUWuQOF_IhDWLythazbjVt-sZvbUcO9RY3P4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11dfde57a3.mp4?token=hdYbQGURWIye7NrIJGOoKv9L2qJqG6mEqzvosqMOj3eoSKBANZ8m-XDrGO5y-SoJ5mzbXr1ZLj1nIqSeZHEDJoY1tp5FXoG9Jelx-0-Bol8R9z18PdJlErL60pzCUAtHSe0_xdUy-ncc7Fd2zf0n-JFPwQ-yUpxUFWC7pRraY9_IOVhJK2sSlJPXT0SZFszbHr487-ZAxl8Zx1Mu-5te4Gf4lYBJFbK_7jl8O04WKTJLM2wChF3SitghnQVDMA1rQmT7gk7J5beAPQmj_Bw3OHQOF_jauWAVyj8bQXk492p6SAmixQGm-vVH6Zt7wZNknX8jbaeNbmG44EBkgcPqwF4b7LqbBKV3s8War_2trS96SSyPGCCemL0It8GdGkvar9TJEQ5oENpnu-sW4IUIKMiCuuInNY6zCQz1eD3aAshp2pHCDBw0VL6JPSil8SreQ3MnrPSJZjrW1mqFASHBAoPQ0Ohu4arPTZO3JVU4EkiPy-PXEeB-y59iajt50VscmD-bGoWo76JyDFvpjOEveQXIg8rjl8jAiLDNKSFXz5q8pugNSQxLiM_N16asJ_SYXyTbD8_8GqocT2drhhBu3dXjwsaeCkVqa3JqPf4XZz8mlicQf5xiAeX3XVYf4XxQNOh-lz5UUWuQOF_IhDWLythazbjVt-sZvbUcO9RY3P4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیارت
از نزدیک‌ترین فاصله
🔹
فیلم یکی از زائران سیدالشهداء از لحظات با شکوه تشییع و ورود پیکر رهبر شهید انقلاب اسلامی از بین‌الحرمین به حرم حضرت عباس علیه‌السلام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/672768" target="_blank">📅 00:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۳.۷ ریشتر بندرعباس را لرزاند
🔹
بامداد یکشنبه، زمین‌لرزه‌ای به بزرگی ۳.۷ ریشتر حوالی سرگز در استان هرمزگان را لرزاند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/672767" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672766">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9defb1eb81.mp4?token=hmJUW9ZDIMfkGXfEL5kWD6m7JByrBnBBI7AE0gWUqa07cKnK-bqba6fgRDAZQPifUijL5DTN_RcJjWWn7TBjUODNB9M_CGBPZPATmnyqbeEN4fNdx-SKVbBhEykYgLOngNFh0Oae3GoWK-tcxq5tDMlRBzzs-BfJtsvIzieAhGRau4wbwOUNQTdwXUOM2ys58dpAzMx6SmlatmG1ZQmyANMGNPW3CzRU4l0d75QLqOEX7eZ7OYpsmGpruQyh_TpZnJFcO6lt32z50z6MA4mj3Ljr3lQUeVXySmmoG9YEGDNYrosTPUi5LUc-gDNYRuUdeFz6wCSoPKM7eLDlUbe9bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9defb1eb81.mp4?token=hmJUW9ZDIMfkGXfEL5kWD6m7JByrBnBBI7AE0gWUqa07cKnK-bqba6fgRDAZQPifUijL5DTN_RcJjWWn7TBjUODNB9M_CGBPZPATmnyqbeEN4fNdx-SKVbBhEykYgLOngNFh0Oae3GoWK-tcxq5tDMlRBzzs-BfJtsvIzieAhGRau4wbwOUNQTdwXUOM2ys58dpAzMx6SmlatmG1ZQmyANMGNPW3CzRU4l0d75QLqOEX7eZ7OYpsmGpruQyh_TpZnJFcO6lt32z50z6MA4mj3Ljr3lQUeVXySmmoG9YEGDNYrosTPUi5LUc-gDNYRuUdeFz6wCSoPKM7eLDlUbe9bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم انگلیس به فرانسه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
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
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/672766" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672765">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
کانال ۱۲ عبری: اسرائیل در حال بررسی امکان اعمال ممنوعیت کامل پرواز پهپادها در آسمان در پی نگرانی‌ها از تغییر روش‌های عملیاتی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/672765" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672764">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
یک منبع دیپلماتیک به اسکای‌نیوز عربی ادعا کرد: ایتالیا پیشنهاد داده است در کنار آمریکا در سازوکار بازرسی از مناطق مورد توافق در جنوب لبنان مشارکت کند تا اطمینان حاصل شود که این مناطق عاری از سلاح‌های حزب‌الله هستند
🔹
این منبع افزود لبنان با مشارکت هر کشور اروپایی در این سازوکار موافق است و اشاره کرد که ارتش لبنان ابتدا در شهر فرون و سپس در مناطق زوطر غربی، الغندوریه، قلاویه، برج قلاویه و صریفا مستقر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/672764" target="_blank">📅 00:41 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

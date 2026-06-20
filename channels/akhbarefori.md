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
<img src="https://cdn4.telesco.pe/file/TsJG-tXh4zslwA5kyaFRz6zZUfRB7uw_QZrhmkocBYuy7lty-Whvl21f3Wm5nTKdK3B03bMoT-aQU5C2zZrDl0OLvOCze6zp9xWXZ2-yTyoZZPAqB8oxa5keTSnxp-cPkKdICVK4t3FDstZzRgY4v-nxLv05N5fGyjx8yjbHM2ltJenkxVQDtsjYRm86INPNv8FUDgccCJmj-UxAjifGQtYxx4s9bKQB3K6zj3empbw2KpXTyaJqfK55rcXmXaflWHMO9DIcE_1-xmjeUc8cxvbR5JonH8r7vLV2XaOgmrYLeymiN9i-niPFcu5ioDIP0Mu7hJVLm9yIBaAZgSeYzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 03:31:43</div>
<hr>

<div class="tg-post" id="msg-661256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0PG8XzDLAIhZRGT4PumjYBWlaZQjKWuJwVijaoDj2h2DEdLL_nkAmYNihX_8veQ5un_p4--7oAqWPJ6JVR97UszL2FGde7mhc4BqrnTconVyMqid1ddbcrwHF70UC-vkr61m0otc6Hsv4YT9ZLJVnvPNttl7R_RerP_0sjxp-T05bTr3qCIX1KHr-BPAxXHz6CA0ZucUYYp7u8q7VVFix4tFkpFrG1auKmTVZzK22bQF5n7fusTiBpx5feMnSkC2iTkpnyWEcK66jph1ZaXeKiOI3zf-wzB_I-9wqYwulGwvyeyOTU5UyRCsahkYDh2etLqd9x3Hu3dERmbztbk8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بسیاری از کسب‌وکارها تصور می‌کنند مشکل از تبلیغات است.
🙂
✔️
برای همین مدام پلتفرم عوض می‌کنند،
✔️
بودجه را افزایش می‌دهند،
✔️
کمپین‌های جدید راه می‌اندازند.
❓
❓
اما سؤال اصلی اینجاست:
اگر تبلیغ شما به آدم اشتباه نمایش داده شود،
📌
بهترین تبلیغ دنیا چه ارزشی دارد؟
🗓
موفقیت تبلیغات از طراحی بنر شروع نمی‌شود.
🌐
از شناخت مخاطب شروع می‌شود.
📊
سن، نیاز، دغدغه، رفتار خرید و مسیر تصمیم‌گیری مشتری...
همه چیز از اینجا آغاز می‌شود.
🔽
🔼
شما برای کسب‌وکار خود پرسونای مشتری تعریف کرده‌اید؟
⬇️
⬇️
⬇️
مشاوره تخصصی تبلیغاتی</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/661256" target="_blank">📅 01:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661255">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxELqmh5B9WjtsgXZHjshyr3VjG5ltyquiFgYlbffeJ2w0MqVma96s6nLc3hdm5l_-kKuQ2r1JGwErqZ9vDom8gvk0EnMd8ZjR_pK59EPZYbJ8OHCjXI3xiTUho6zBSQbV4HLspYXxDUrRVrBtOdBRZDBUsqg32OMxlDA2LoAkp5k3EocyuuxuiHRsTvAYLsctqdtSunR79QnDWknA-Kn_ZxI3EHzuVT3Vn9siQlPtD1C1jm08dmM-dfycqh3kXTbBPnArw5u6coZyxlOZ6b7K7iome2LIevSD-XaGKLpeonnZpUDkwTYk8hcxee7_iQBGoeLy2HVJ3DOi-7UnXq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌️
❌️
خبر مهم
❌️
❌️
🔰
دلیل اصلی مشکلات آقایون رو میشناسید؟
👇
1⃣
برطرف کردن اختلالات و مسائل بهداشتی آقایان
2⃣
بی میلی/عفونت مجاری ادراری
3⃣
پروستات/کبد چرب/دیابت/سینوزیت/اعتیاد
🖲
دریافت فرم الکترونیکی مشاوره رایگان
👇
https://app.epoll.ir/71553050?Referral=telegram
شماره تماس مستقیم 09211960273
یا عدد 5 به شماره زیر ارسال کنید
👇
👇
09211960273</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/661255" target="_blank">📅 01:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661254">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw1PoDxmZLTryreqBtHVF51z83khVbWBIBj-ThsWhQ_l3paCg9IIIRPDaqLKAHL8MKIX0fa3SpRNWl7fOeL6tfjtLcfOboLM87T_8xWNzw98-4z9W8flEjaIpDzQWjyedg7mSinqT5pRNVjSQ8GJaLB5kahBJ0EdBgwl2sCkbFEbiSSJ8rlDCKJOjY9lxkHDqkCl_OFktTf9jBWNTh2e13QCzL3kEWK4nPlhDRHZurOEHg7VSQm8XdTevWAKgbj5EBx8IwbqQE9_SYQaGMYXks3rCqQmzBT_Dm0_TM_j4xJrP3ivrFEnMB6e5rLWSDxGWm3KM_549febN1GoWG_hxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌️
رژیم نگیرید ...
❌️
اگه چاق هستید و بیشتر اضافه وزنتون در ناحیه شکم و پهلو هستش، رژیم گرفتن گزینه مناسبی نیست، رژیم سوخت و ساز بدنتون رو پایین میاره و وزنتون دوباره برمیگرده
⚠️
✅
اما نگران نباشید، برای لاغری شکم و پهلو فرم زیر رو پر کنید و مشاوره رایگان بگیرید
👇
👇
https://formafzar.com/form/bgx0m
https://formafzar.com/form/bgx0m</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/661254" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661253">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
اکسیوس: روبیو برنامه‌ریزی کرده است که هفتهٔ آینده سفری به خاورمیانه داشته باشد، که در حال حاضر شامل کویت، امارات متحدهٔ عربی و بحرین می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/661253" target="_blank">📅 00:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661252">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbodW62EJUcOFeYd9J2IcrHr89e2ktU2tYRAR8N8E2xp6iEo8m1Kr4aorkgT7JA5LCnKpBbqzen9au1W5qGPjfnYnkMJts0VxgGk0aWJRHa_ea7mLw3-VN9Tv4LEeynOV6fDxi4SXNTazMTUWgsRxRl6eQFkmiB3yQnRQ8eDG6qK6aX0kFTL7gMAluAIYaJ_EJPKr2VRKJ_mumINfESmSBrko8NQZ5PjMuN4uOFSSc6s7myrcEbV-K4EZBAJlTLBRpLtbq47ceSbP7Vi8-_S7r__CA2nql_A2GuYIcT65ZKzuujpO7T4tB4HHZVN4LgouCmYbgFo9-OlcRDP6pRokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صعود دومین میزبان هم قطعی شد/ یانکی‌ها با شکست کانگوروها راهی دور حذفی شدند
🤩
🤩
🤩
🤩
🤩
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/661252" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661251">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c909e237b.mp4?token=bBr_azpi1TMCcT2AX5oBaf-JGhsAfjJtXz0T4yUlGujX5BWcYKsbl7liSquYw3GuVhXwUvA8IXonZ8v0gp0TUokMMPMZcrCUX9W4OgGyVXKYIo9GcKpYRC1Rl0UQJsSleEkmHxTaYXSR6fYCNACRLDBpp2E28lInjED-sGxgC_SyKs-UaP0HELoRxaSgxggqVZSiiJp5wLEIriUTJ4_HnPsOVxJGQpd0cu3Gv8zzpdWheqp9gLmLJ2LZw6l09ua3XzpJ3qvosqu1U8iSqJtWcj7K-hBdKLMRQJ8X_1B-B-zUMHpWWJdSZbomgwGmfVkLFgEekiHGhU_P_tIsKthAqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c909e237b.mp4?token=bBr_azpi1TMCcT2AX5oBaf-JGhsAfjJtXz0T4yUlGujX5BWcYKsbl7liSquYw3GuVhXwUvA8IXonZ8v0gp0TUokMMPMZcrCUX9W4OgGyVXKYIo9GcKpYRC1Rl0UQJsSleEkmHxTaYXSR6fYCNACRLDBpp2E28lInjED-sGxgC_SyKs-UaP0HELoRxaSgxggqVZSiiJp5wLEIriUTJ4_HnPsOVxJGQpd0cu3Gv8zzpdWheqp9gLmLJ2LZw6l09ua3XzpJ3qvosqu1U8iSqJtWcj7K-hBdKLMRQJ8X_1B-B-zUMHpWWJdSZbomgwGmfVkLFgEekiHGhU_P_tIsKthAqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنی مورنو، سناتور آمریکایی: لغو تحریم نفت ایران به نفع آمریکاست چون چین پول بیشتری می‌پردازد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/661251" target="_blank">📅 00:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661250">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFplJvmuXm1SyonTDFw6Ge6DOBljvqZ7oC6LkLvP8yxyDAB9ScsYTa9fM7AlOeX-egSFGqtBsMjpz2snK03fpOYEWCZrjStU7e4u44CMqJct7LaoS2zdT6OY0mom8BKIPPN0OZt3_JuzArXDeFtBa2DQTmyBkXEZybQWB6WupYac980Ud6x9Gjr0Cxq24iKLgofxZVf_uiW5NIHaAVRPWTVVaVR-DQGayFjgeB8RCJYToqe7cdhgOy0Qlh3O9IjWza8TciZXLD047iied3L4Uj3ltiv7nBP7LzHECRZb6oKFqZ5alLLspUpZEgfEaKwJzS0WVT02kAATsCU-ar6MgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعلاً گل‌به‌خودی آقای گل است!
جدول گلزنان جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661250" target="_blank">📅 00:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661249">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
حمله رژیم صهیونی به جنوب لبنان با بمب‌های فسفری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/661249" target="_blank">📅 00:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661248">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2674fd9d79.mp4?token=p95JhKAueFBnCwYQHCFY2hsz7NUZTIpVt9Bz4KAOYsAuo-I1G0rK8HmleCQoXvKRjXdjfQe0tto6Jk453IISIs-XvJSJ_FPICb3CUd0_37zeZo_deOGG569lu6rmtOnbn-NuoFDpNuW1v-AojolnVi7M5jXWyBBjcKg2s0qp19EbffHfthubv8ymGvVIhghC5n3pR7RCG7IOvtrl_vN58YgmXjlEoWN1dbIbfSlmpC_0ANQLHcJv8dn2DZrd0qqxXbHrLLQlrSI7cI8aGPd0ov7NSdH-KwuV-hGeGmQe1S3_4aWTzbAS1tCEp9KwToECORx45JxykcRe26VVf5Ix5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2674fd9d79.mp4?token=p95JhKAueFBnCwYQHCFY2hsz7NUZTIpVt9Bz4KAOYsAuo-I1G0rK8HmleCQoXvKRjXdjfQe0tto6Jk453IISIs-XvJSJ_FPICb3CUd0_37zeZo_deOGG569lu6rmtOnbn-NuoFDpNuW1v-AojolnVi7M5jXWyBBjcKg2s0qp19EbffHfthubv8ymGvVIhghC5n3pR7RCG7IOvtrl_vN58YgmXjlEoWN1dbIbfSlmpC_0ANQLHcJv8dn2DZrd0qqxXbHrLLQlrSI7cI8aGPd0ov7NSdH-KwuV-hGeGmQe1S3_4aWTzbAS1tCEp9KwToECORx45JxykcRe26VVf5Ix5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: بایدن چیزهای زیادی به اوکراین داد و اروپایی‌ها باید هزینه‌اش را بدهند
🔹
من آخر هفته با رهبران اروپایی بودم و به آن‌ها گفتم: «می‌دانید، ما به ارزش ۳۵۰ میلیارد دلار هواپیما و انواع تسلیحات و چیزهای دیگر به شما دادیم.»
🔹
گفتم: «چرا شما پولش پرداخت نکردید؟» و آن‌ها گفتند: «خب، هیچ‌کس تا به حال از ما نخواسته بود.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/661248" target="_blank">📅 00:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661247">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caTF4KQIKFyqesCkuU_9xL_QPSG9rWHfxS5iTwAcVZInog1l_tFZQ76XBLVGjM6hS7C-WJ-5TgV-xZJXJdvHNTzpN3IbnKgwsOQgbg0Gw0GkMlzmtpjKNo6jyjHoMANK1eDKK6EVj-P_HFohGhnYC6TLOkAXf7-mHp5oop7VqGxIwo_Fgk8CPEVsLUL8hreEPpJywL2Lw0czAnMoWyDbrgpmhXUW92PODqpp5Jrq--wgk6BJZYHB6p56KSxeJaY-8z23npiZpHCESDTGLumxHXhuBPXJu2CihEb8QITtA20dTZLEn8IC7DOFP3sZF-ZikCPA0vYb9yWv8xZg3psMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس‌جمهور: خاک بر دهانش باد کسی که در ظاهر مقدس کاری می‌کند که پسند دشمن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/661247" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661246">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awMQ7019S7yB-Po9STD1XZqlehYSV8jFgNYQ3eAxeAqm0L8k3Vw4aWwuZ9i7C1DVcTw7skOACaufqUQwcqrWfdGCRCAWq7zOerlr-wjiDUqN8h7vOlGCVFlO0XwfCCEq3nFJ0FtYffSMUMMIZUl9Zu8LHOWmWW_NVSy7Ej1wVelKq_Vx87RMU3b_Yrm7vdqbXmgWsCw5ztSgBryhQEa4-n7Ip7WQF2D_OnkoiNCb-u7UzThHBBZB5iB1cT9CZDjIWwAfI9DCkz1IUKzkR5rYOkP-0HEOsvheghRR8Wv80GETvzbEQ72JGz8jD4lhLOsFkkxHZ9XhVkt5VxuRCWo8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی‌الاصولِ جمهوری اسلامی
🔹
«علی‌الاصول نظر دیگری داشتم» جمله‌ای که شاید بیش از هر بخش دیگری از پیام رهبر انقلاب درباره تفاهم‌نامه ایران و آمریکا مورد توجه قرار گرفت، پیامی که از یک سو از تردید نسبت به مسیر طی‌شده حکایت دارد و از سوی دیگر با تکیه بر تعهد مسئولان به صیانت از حقوق ملت و مقاومت، راه را برای آزمودن توافقی گشوده است که سرنوشت آن به رفتار طرف آمریکایی گره خورده است.
🔹
هفتصدوهفتادونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/661246" target="_blank">📅 00:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661245">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5ruUU2bu4Ccr9KUyK9FLPkn8VYB3KzCX693jfULYNWfp3Uu-JuCR_1TABeFlQP9B4Tj0HVG1zVeKHP1ZUz2YracKxrJnWAE85OtjYazjO0A2TAAL3cLAQaTZU79H8tRsvVsSvAiOtF2fnmOqKFqVHBoFyhqLrWF33ueS67I-HwbQfSVN7rYngFYhMUirX-bpiG7imahO0g-SGUCvlsicZGkuffTDBbQwsCvTkJnOBXGuH959sJKGZsB7LBDLUgsubDKNk73yOjZ9foVTI1ASDrNC654sjeqe9FzVGxFsZt2h7mJvblnqGHaD_XSI5zFCMf81H8O_x4-mIQfusFqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/661245" target="_blank">📅 00:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661244">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fe79MGuqY8UgB3y1XmsAcX6X4FefTRaAMkrTXk3-XplAjk8dDRB4TYPy6KYEDFrS-HYGoP3g7W8eH9bRlOzKS4l_A81r4-bCrEfrGMyyAXzhtBWBVPUQfOEoaaU3435DeZ_PMJl3NWEya4Lcql6YWiSGu4l-VG-mfzM54dPfTKr0uK1gS3cWtbuLp691Do4Sq9TCoMSP7LtP3lMhgmJD-ZeZfZcIZjSZWZ5ZxRU615Vxp9l6KG4QA2-HB_W57tYVSuucY8V1_zZqvTIHhE_Wj48CZNrmXY39RPOS1bhBGUJiIkwB7Yw_GlpStuuzHzGD9zWFElTgcEBnBNMWusH9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت خارجه به ادعای دلسوزی وزیر خارجه فرانسه برای مردم ایران
بقائی:
🔹
جناب وزیر، ریاکاری همچنان یکی از ویژگی‌های بارز فرهنگ سیاسی فرانسه است،  فرانسه در برابر بمباران و کشته شدن شهروندان ایرانی سکوت کرد و اکنون با «وجدانی گزینشی» مدعی دفاع از حقوق بشر شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661244" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661243">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6e2275b7.mp4?token=QgGY4j9pRMQx8Nrh58BWyQPn7NHGKPVHdXPy65gZq1QsnTsT6mnhHE1AgKGjM9Z7zVZxouJgHXDUEZCe15D_YP3_iVvKIIEpbxYRd9Rja-z5Uqj5aNQ67jA2T7u4ckn8iTiiBx_KfdUH9aZpbaMU2vN_wxNVWNUM6tiCUugoJStrbx6vTGWX1rb6S8Vgq0XECqHLCcGztVTw-WSeMrYPS095TgZ2ZooSOowodUP2tcV7YQYh3OBDi_OdK9JCwycZbD0qGzU_h6g7EUukc7uuXnCJRTs2K9h955EkV5TZVEwhuWlFK7TcFv33mtlKl6K-FPhQ0Iz72fULESb2iWofpLaprX-Hw-g_sWx68_beGbDghqOcceQCaVFElCMaf4U7VHVDHFBNuiMq8UOxYGvl2xiPKdjH7YCpkb6LILhlbRrEnaHi1nhkGXuARZ7GuVLpCKNiUKh1Av9Tu6E7IOxQHjE1-q--E1q0W031pBtpZe9LQeeAMChhSJ8Ik2iHee43Y24xitMcgKivjMhPCjOO2R5IugRWkkFQ0TdKo6UiUVx5HD01faJWQ9gGW8qyq51sFXbEKqDt2etORWr-jls047P_aWBm0IRXk3b06RwVyy5jj08BeTX0Jy9fjN-16w7ZacmDwdHRpwyJ9hAmz9Kvmj_chYHfy9DKeuU4-qMEJ1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6e2275b7.mp4?token=QgGY4j9pRMQx8Nrh58BWyQPn7NHGKPVHdXPy65gZq1QsnTsT6mnhHE1AgKGjM9Z7zVZxouJgHXDUEZCe15D_YP3_iVvKIIEpbxYRd9Rja-z5Uqj5aNQ67jA2T7u4ckn8iTiiBx_KfdUH9aZpbaMU2vN_wxNVWNUM6tiCUugoJStrbx6vTGWX1rb6S8Vgq0XECqHLCcGztVTw-WSeMrYPS095TgZ2ZooSOowodUP2tcV7YQYh3OBDi_OdK9JCwycZbD0qGzU_h6g7EUukc7uuXnCJRTs2K9h955EkV5TZVEwhuWlFK7TcFv33mtlKl6K-FPhQ0Iz72fULESb2iWofpLaprX-Hw-g_sWx68_beGbDghqOcceQCaVFElCMaf4U7VHVDHFBNuiMq8UOxYGvl2xiPKdjH7YCpkb6LILhlbRrEnaHi1nhkGXuARZ7GuVLpCKNiUKh1Av9Tu6E7IOxQHjE1-q--E1q0W031pBtpZe9LQeeAMChhSJ8Ik2iHee43Y24xitMcgKivjMhPCjOO2R5IugRWkkFQ0TdKo6UiUVx5HD01faJWQ9gGW8qyq51sFXbEKqDt2etORWr-jls047P_aWBm0IRXk3b06RwVyy5jj08BeTX0Jy9fjN-16w7ZacmDwdHRpwyJ9hAmz9Kvmj_chYHfy9DKeuU4-qMEJ1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری خطاب به ترامپ: شما دنبال تسلیم بی‌قیدوشرط ایران بودید، تفاهم‌نامه که شبیه تسلیم ایران نیست
🔹
ترامپ:
در واقع، احتمالاً تسلیم بی‌قیدوشرط هست.
🔹
مجری
:
واقعاً؟
🔹
ترامپ:
فکر می‌کنم همین‌طور باشد. ببینید، آن‌ها دیگر نیروی نظامی ندارند. شناورهایشان به قعر دریا رفته‌اند. من نیروی هوایی آن‌ها را نابود کردم، تسلیحات ضدهوایی‌شان را از بین بردم
🔹
مجری:
درست، اما هنوز هم می‌توانستند تهدیدآفرین باشند. آن‌ها عمدتاً قایق‌های کوچک تندرو یا شناورهای گارد ساحلی داشتند.
🔹
ترامپ:
خب، هرطور می‌خواهید اسمش را بگذارید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/661243" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661242">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575cea691b.mp4?token=r65jyywGhcv0WN67KzSiW1D_ZzThi5fkrkQ3fSn8EfWyjhWxvzc7JF70mNO0io-m1vO653dYLx2ocxr9XOAw36oQnqhoT4pbp-2g1vkO6kBlJQs6mssnYfQgksDmjIUynmeVUfBOPB7YDhriP2WFQ5_b4HT0JHJPUkmGQPi8XW0IHJfI859RjtntRP04FmmEhgQJ8_EiPuipkn1tc9fBrUgViS6rDyTCFiArSudp74zBmUunwN7ouH6E5bEsTPnnc_RYZXwjWPrizufO4YEokEd2ls1zAhl2v5bmpbe0_mRzEgoZygjzVY0SQ2LW97y4LnA4QE6X8eK_b0bJrtGtr36MIRV2Zf2A1GoMzgbqYqq6ubHv4C7WlTwztncHk6vE3zWjZLdq2psPZdPlpYLrOGKYdWMr4NrVom0JsK4_kjx8ME5_8GE7gHWePwE6rEhm1h-lKMOjApb8FNf4rxl6wJxsk8w5t_bXJfWaH5vWxojgUfxWH_IXJQYqtn0wBNNFYp80qX_i5fzkTffqkMpLpMFpwQNGDdAhuwNvmp0bOERnWqifSs3CRN5wu8YhNnfUwkNJSEPu1fQ6ryiYpZ6e6b0VNziC0GUsIh1dxI9F2rSWUrX6YGYB9mcgRlkp7Jgq-Et-uY8OqgjEO-GpBJoY65YL_h-CbyIvaGzzCIcWpRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575cea691b.mp4?token=r65jyywGhcv0WN67KzSiW1D_ZzThi5fkrkQ3fSn8EfWyjhWxvzc7JF70mNO0io-m1vO653dYLx2ocxr9XOAw36oQnqhoT4pbp-2g1vkO6kBlJQs6mssnYfQgksDmjIUynmeVUfBOPB7YDhriP2WFQ5_b4HT0JHJPUkmGQPi8XW0IHJfI859RjtntRP04FmmEhgQJ8_EiPuipkn1tc9fBrUgViS6rDyTCFiArSudp74zBmUunwN7ouH6E5bEsTPnnc_RYZXwjWPrizufO4YEokEd2ls1zAhl2v5bmpbe0_mRzEgoZygjzVY0SQ2LW97y4LnA4QE6X8eK_b0bJrtGtr36MIRV2Zf2A1GoMzgbqYqq6ubHv4C7WlTwztncHk6vE3zWjZLdq2psPZdPlpYLrOGKYdWMr4NrVom0JsK4_kjx8ME5_8GE7gHWePwE6rEhm1h-lKMOjApb8FNf4rxl6wJxsk8w5t_bXJfWaH5vWxojgUfxWH_IXJQYqtn0wBNNFYp80qX_i5fzkTffqkMpLpMFpwQNGDdAhuwNvmp0bOERnWqifSs3CRN5wu8YhNnfUwkNJSEPu1fQ6ryiYpZ6e6b0VNziC0GUsIh1dxI9F2rSWUrX6YGYB9mcgRlkp7Jgq-Et-uY8OqgjEO-GpBJoY65YL_h-CbyIvaGzzCIcWpRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت طرفدار آمریکایی از تیم ایران / راه برای گفتگو و تجارت با ایران باید باز شود
🔹
هوادار آمریکایی تیم ملی فوتبال ایران می‌گوید: از تیم فوتبال ایران حمایت می‌کنم. با وجود همه حاشیه‌ها و رفتارهای ناعادلانه، این تیم شایسته احترام و تشویق است. باید به‌جای تنش، راهِ گفت‌وگو، تجارت و ارتباط باز رو انتخاب کنیم.
خبرهای جام‌جهانی را اینجا هر لحظه دنبال کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661242" target="_blank">📅 23:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661241">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTOKd1yyZ22zlloKDRbs56iot40VwnMsnjEK3EM_VaY1CEddS-NF0lc3gWtR7s4eAWEFvjiTQ-E7zitmeydL4Yfihvohb0Coqn5C2UWl3SNx-C7BbAgpVU4vpKk74g2m_wWALoPWXNKbd5a31xONT3_CDPybFOs8Bt_S31eXy2O4OmL9u-XvwANIO-b9hHNUvCgFQOj9ZKZj0or-ySzzU4L9zQWrZfi0Z8c_j5Sr7ys-BGPQamSHGUe_nUwur3WKn1sWQMYKvm-ESzbhx52rkjFgSjhdF9vz6vTDBH0HTOqM_nwQNOuvF4X6tL7iYcf7lgXjRbzfP9oQknQdlF7M-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس جمهور آمریکا با ارایه تصویر یک نظرسنجی : توافق با ایران بسیار محبوب است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/661241" target="_blank">📅 23:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661240">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66787826ad.mp4?token=QV9gywvjr0geNNYs_G7m2iNnyqvoz3NZrojTRw8k5PGWT0uObsc8z2TomhpV-yu7Ij5MwHi0aUg3ss09lfiCqKQ4nqrbjGqgcWGpeGYw1ePOt10PfSxYN0fFxvssVig_8WSGPx8_GXlZCtDmlCCYhgvY7TUS-LyRT4M18Udsk4fJdEohjpMgaClWhDPgQlghGPCfQTFuMXF2H4jo9MikmBf1bjSCJAZGipgx2QQdL1JhAqv6RpRlzU5TTD8vnCMnYbFI0vP1okEHH5ulDVKkQ9m0lD6RFQ78SOmr1haFrETdfUi84YULFFsv90zw3s_u4NQqvNGcO7sG200EkoQf6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66787826ad.mp4?token=QV9gywvjr0geNNYs_G7m2iNnyqvoz3NZrojTRw8k5PGWT0uObsc8z2TomhpV-yu7Ij5MwHi0aUg3ss09lfiCqKQ4nqrbjGqgcWGpeGYw1ePOt10PfSxYN0fFxvssVig_8WSGPx8_GXlZCtDmlCCYhgvY7TUS-LyRT4M18Udsk4fJdEohjpMgaClWhDPgQlghGPCfQTFuMXF2H4jo9MikmBf1bjSCJAZGipgx2QQdL1JhAqv6RpRlzU5TTD8vnCMnYbFI0vP1okEHH5ulDVKkQ9m0lD6RFQ78SOmr1haFrETdfUi84YULFFsv90zw3s_u4NQqvNGcO7sG200EkoQf6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: اکنون ما توافق‌نامه‌ای داریم که دیشب امضا شد و ۶۰ روزه است
دونالد ترامپ، رئیس جمهور آمریکا:
🔹
آنها باید معامله کنند؛ در غیر این صورت، کارهایی خواهیم کرد که آنها را خوشحال نخواهد کرد، اما فکر نمی‌کنم  کار به آنجا برسد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/661240" target="_blank">📅 23:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661239">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fu_C69kficEnJ1AsRZMPxZtrfpNTG39Vi8k7wZ9XpVRpRkpob8Q6KwML-XPXN7UoXyXSv2WGVp4M5hqB5oyMGNIpYFB29BCk4PjlnXt_PRnHCOo_Q5Z6M0xph7gI8M9i3Wxz4t5abLcuIUuhBzp96OZuv_OWSP_fYV2hcLk8mNk1Z49coDzy-qriJAXOWklkaEY7g3zVxsO0LWTbtxMFOAlAWIZ_1J9jSFlbBQuCsgFlRlbFsmPeEaunMaX59qps95Y5hVewMFmosGcHAwZKYAJl-bNpFt9KTHxm04Dk1PMd3AATJHoly9-fAqM4SzBFze2fxOR9mwV_sgUOLd-YLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدای چندین انفجار در استان ادلب سوریه شنیده شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/661239" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661238">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پل امید بر رود تردید
🔹
تفاهم با طرف‌هایی که سابقه طولانی بدعهدی و نقض تعهدات خود را دارند، نه موضوعی برای خوش‌بینی افراطی است و نه دلیلی برای ناامیدی مطلق.
🔹
تجربه‌های گذشته نشان می‌دهد که در چنین شرایطی، مهم‌ترین اصل، حرکت بر مدار واقع‌بینی، دقت و سنجش همه احتمالات پیش رو است.
🔹
در این چارچوب، منتقدان و نیروهای انقلابی که نسبت به نتایج احتمالی تفاهم تردید دارند، بهتر است از قضاوت‌های شتاب‌زده و تقابل زودهنگام با روند موجود خودداری کنند و ارزیابی نهایی را به نتایج عملی آن بسپارند.
🔹
در مقابل، دولت و تیم مذاکره‌کننده نیز باید از ایجاد انتظارات غیرواقعی در جامعه پرهیز کنند.
🔹
معرفی تفاهم به عنوان راه‌حل قطعی مشکلات یا یک پیروزی کامل، می‌تواند در صورت بروز بدعهدی یا تأخیر از سوی طرف مقابل، به سرخوردگی افکار عمومی منجر شود.
🔹
همزمان ضروری است مواضع مسئولان به گونه‌ای بیان شود که این پیام را به طرف خارجی منتقل کند که پذیرش تفاهم به معنای تغییر اصول و مواضع راهبردی جمهوری اسلامی نیست.
🔹
طرف مقابل نباید این روند را نشانه عقب‌نشینی یا ضعف تلقی کند، بلکه باید بداند تداوم و موفقیت هر تفاهمی در گرو پایبندی متقابل به تعهدات و تأمین منافع ملی است.
🔹
در نهایت، این روند فرصتی برای آزمون عملی دیدگاه حامیان مذاکره و تفاهم نیز به شمار می‌رود.
🔹
آنچه امروز اهمیت دارد، حفظ تعادل میان امید و احتیاط است؛ نه باید همه مشکلات را حل‌شده دانست و نه از امکان موفقیت یک مذاکره دقیق، هوشمندانه و مبتنی بر تیزبینی دیپلماتیک ناامید بود/خبرفوری
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/661238" target="_blank">📅 23:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661237">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxXalBBiqs1XMBSVhjHxsFMRqhz-TyrAf_ZTPRqlrg4VYMpF5TzzyceVsSI7YgJsvFgHctYm_ASdkDBc15NluOzhmFNKaisC6372FrNA5QB8j13OdokbZmC2ujrO2iTNvjr8HxZmfHWBZxWFXWoSDf8t93iKntFFUz1NbSuXWaEqr2qZYvmK7c-UC8H43v2fhylnGy0JSQACMgFcs8vA-JOIEA3cMw0y6zyBGRV-7Ye9W2T2UpyyZs8HgZGuWPkldrTERPIkmXzSgkr045DQ_tIGLLTw1NCAM3NPlQOiO5h924hfZjb-uSaFURN7IdIe0LA68ziuZ-1R2zc_JLowXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: ایران به نقض تفاهمنامه پاسخی بازدارنده خواهد داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/661237" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661236">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
گفتگو با یک آمریکایی هوادار تیم ملی / حمایت از ایران با صدای بلند
🔹
هوادار آمریکایی تیم ملی می‌گوید، این حمایت فقط از یک تیم نیست؛ از مردم، تاریخ و کرامت یک کشور است. از مردم فوق‌العاده ایران، میراث غنی آنها و مخالفت‌شان با جنگ و خشونت. فوتبال اینجا فقط یک بازی نیست، یک نماد از همدلی و ایستادگی است.
خبرهای جام‌جهانی را اینجا هر لحظه دنبال کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/661236" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661235">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGDReVf14JAKoalIkzv1hM3v0RauqRqwcZ6NnKlxxqhBxhdJeggFE7X9GoFBxXInPcqmy0pes-r9DN6BeG65IrxQPp5c3L0pGDosbMQPmnXnALBpfb4GQ7BJ8dmCzxydmk4AQmdilwiixDT-LXmUUU_PURZcolNjb4az0itbcY_hMCNTBlcAXZ9A8UxJesZLpvURxf8WtMw_yvPLiuw8uS2PTFWPowAJkvBQQ74uCtv0rNp-OAlmZqNGTTfxyfDbs3JaowhUINQnFb0sZbyAe8yP2w0dBMiqZ_oLc4z5PlgaZKZcV3_MhryfT_0abJcedDz1ZTEsBVnpeqBjpNOhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ از هدیه قطر رونمایی کرد!
🔹
ترامپ در پایگاه نیروی هوایی اندروز از یک هواپیمای موقت جدید ریاست‌جمهوری رونمایی کرد؛ یک جت لوکس که توسط قطر اهدا و عبارت «ایالات متحده آمریکا» بر روی آن درج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/661235" target="_blank">📅 23:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661231">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BR3UyDM_v1j28LLBhnxxiBguZ-BNs4QHAO5Z6vhXgWtDXs6x3D-vttd-vyP0V66YyaZ8DtpeN8FHcLwKIRvNH-Yt-Ao-6DvYx_1umHYeF7VuS-YuSrn_53cOZyYvj8tkmYjeimYRBQZsgR8YQCFrfbPArGcQ_JuK7beqVRWW-si_ssbQa4p1Tz0K6pl5ZGF4RPRpDMNZWW9DQlA6qh6cm84pSNUvg2zMI1p1zOSWXjs7GZPAIFKtq0f1W5qyiQeSkX5cJPCk7hYc56XFYqdbzKJeOgW9MfLhx55Nx-Uho_Nb3o8CKzqwgQ0VfOo9GAEV53njwQGMeQAOOLVLYnkrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HW1n4jZDynakJtXVcN0JQpivmB9FJg031hEt-fdxRCOlqSwjeLYJZ17eM7flfQtF4VtblMsRSF2bs7573e8F32XqJUSwJ20_pnQU8MrUh7BdfIZdo_XweWo2-Ey-GJs9-hR8-QnW8Atj-kBYuEnLo1_zW8dnfkzMvw_zH62sqlSNx48hlvw0a5ePjCQCIO8-VTKcmYl7NcoY1oe1yumdYESBJjZNX65rWaJmSwY1B-Bsabvfjnc2yDeydtzFigIbU6_vuT-tGKTJNdJ_PYZ_Io2YL5iuBqNilPPimjGvBSa7zX9GuaBZvD-plgp2fKfuCLgw6SwHMlo59ZrMcDqF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boItkump432m96N-Mt9dod3EvV7jw7SWZkoHBCN_mO6OMh6fE0o0HwGnXDnqsSnexZwdZZ9Ov2rnR5slrtmX16vA96SstKR_qXTKUJfbAoZ4wMAVMZ9XKvh3YvkcqdDWXLaCDK_oeLDzxVtgE3BhHWJq30NGBKqJuludW75iOe4E9Tfn11msBVPjfI63aqDgs0g1XpMJ6Whc2O_evOwLFukjJMnXUPFTKzEuCvrbOSqA9l2UwDnrYvjl4rp9tvCV5HAQuobwiwMIxb39rIOk9sQsxxnvQpg6Mv_jB1KdAcmkEtS29hsTFrNtGOPH6pgwO7XNyIp4IRUgOFcqq5e4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYnrL1_ZSZTMaSL_TIAK5SmI4W0Q4ssy56IWSWXgpb5DIclQt5AMZM65vck5AYlrTVfC7S5zIyV4nyQ-mKX8Q5zzClYSozXDRIsYAtAXeQjhb-mJPCsbDbrJ9X1o44_WDuEY-KbO0Q572UmmwLHZXsN8SOUPW4hGOxamrCVljDf1qwY0TVgIGrflLM8OOnp9fx12Zw6mypErce051jLim1v8NSDetOiZSSSS09IfaA0lwq9v4X8PSiV-SsvMW4FdZI3HMYNBtjk6MFIFWtgMXsG-yiHXvUvAyRlnGYa4jZxYaDMH-rGTV5DdiJm4WZ44zAe2lIRdTH_GsCmrBEzdvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمله دانگرید چیست؟ وقتی دستگاه شما فریب خورده و هویتتان لو می‌رود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661231" target="_blank">📅 23:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661230">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a2c758de.mp4?token=DPo5hhr_WHcSd4_7W_8CFUrdY_sav97-uP0Yb79SHUhXBeSDqaxRiD4v9McN-Iap_z7aPjMVLy4RPMxAUB_j83bnX6mI4o9KXTlf47-GdpsclBJwI-oI28OpEMw6-RgQNRj_kSEcAZT9IBm8zmef6lmGtz4_DPCa32qZYVMLJ6jPc551znTbLsv5cPOinQn7HR4SYUth9S737CSZxnfpTntrLA4hiZ0-ID2jL-vvMWT5XF9RR073DObrzNFq0hgAeLyPJbQ_2zqicVSYYSSmTOtW73llzHbkXohHRU2FBKHzfaLY5nuC0PvkL3EfOdQvjHx4eCEiKPkLXCRyxYCAqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a2c758de.mp4?token=DPo5hhr_WHcSd4_7W_8CFUrdY_sav97-uP0Yb79SHUhXBeSDqaxRiD4v9McN-Iap_z7aPjMVLy4RPMxAUB_j83bnX6mI4o9KXTlf47-GdpsclBJwI-oI28OpEMw6-RgQNRj_kSEcAZT9IBm8zmef6lmGtz4_DPCa32qZYVMLJ6jPc551znTbLsv5cPOinQn7HR4SYUth9S737CSZxnfpTntrLA4hiZ0-ID2jL-vvMWT5XF9RR073DObrzNFq0hgAeLyPJbQ_2zqicVSYYSSmTOtW73llzHbkXohHRU2FBKHzfaLY5nuC0PvkL3EfOdQvjHx4eCEiKPkLXCRyxYCAqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات جان کبوتر از تگرگ شدید مشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/661230" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661229">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای سفیر رژیم صهیونیستی در آمریکا: عملیات تهاجمی خود را در لبنان متوقف کردیم
🔹
سفیر رژیم صهیونیستی در آمریکا مدعی شد که این رژیم، عملیات تهاجمی خود را در لبنان از ساعت ۱۱:۳۰ به وقت واشنگتن متوقف کرده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/661229" target="_blank">📅 23:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661228">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: متنی که برای توافق تهیه می‌شود باید از نظر فنی و حقوقی کاملاً دقیق و متناسب با خواسته‌های ما باشد
🔹
در مورد رفع تحریم‌ها، باید کلمات به دقت تنظیم شوند. همچنین، در مورد رفع محاصره نیز باید به طور مشخص بیان شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/661228" target="_blank">📅 23:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661227">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKn6ZA5evV3Gvfyb1HX4-a1lRiYuNcLRGNTB_9o6XYoEE2Rx_J_RArvhUn_Tz3kciQRpmzjljF-aI-Hv6zp2an5ZQYiJrKcXvBOBumeJOUDbt9Jssb8fimwUm_nwwZQSSpz1FYMJoZDAfmri64kVxJKIcStXTYlyJXGM2D1wtAksLXir-HmaePQ1etSrJYj20ya9a4IRcdpQdWDi07BuRzRyD59IPi9NecSP-W5MTFUEwTeLydeJm4ruv3i18nsEhF_dV_kVJwGBayeJ4AhmXfeeDMDYuGM2Sbsz979JkELBBj1nbJjTDK_GFOlIpWaz5oi1FfLSXrcwBdljyDIPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله رژیم صهیونی به جنوب لبنان با بمب‌های فسفری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/661227" target="_blank">📅 23:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661226">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyfPZPZnPPZMMs8a-5PkrRYUzEq5ST4uJBvhrOsZ_l1STINx9yjHTJ-Nzh4quIUhBg9uHwer4jA11VsLVSjua3V3j5KRZgYrfPcE8AKDz52pRIGHbrXgqvIKZ9HLnjfFE-CasRpaMLspBWFvMEpXId1CT9ssVlzPIaYCWh12ruJBp6cV4w61mfTEzgAKvYqWvah3LG6Eg6AwAXvVooIR9WIsK48b3JSi2r1iv9S34kLV4ZhW9EWuLYU0O2un9Z6XaCPl821eJLmPMmbRDlRVZIP932mcCV9SI8k0b8fLtGa4v4af1A9JVguvWRBbPDdxOQaYlZ4IUVyWDFwOxpt22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: اگر به بمباران ایران ادامه می دادیم، کشتی‌ها دیگر نمی‌توانستند تردد کنند
🔹
ذخایر نفت ما هم حدود ۴ هفته دیگر تمام می‌شد. ذخایر جهان واقعاً تمام می‌شد.
🔹
اگر با ایران توافق نمی‌کردیم روزی ۷۰۰ میلیون دلار ضرر می‌کردیم  #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/661226" target="_blank">📅 23:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661224">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310840d86d.mp4?token=UuKnOYiSAgDkGqKaa4mUwE-igCnu1LVca8tWkJWSzOklCJwBU5OIssEaSixgxJG_m-vDto6TSQv0m8exNkkwKBrpfYGRwGDZvbFKIHd1O1uVS0wBF38Hhz0BHdSpb3KRNIUabKRM8zPXvGjeOCkoTIjVS6RGbxmQiIHMjPnxs2YgdAFbaozZqsHzukbyfc5QX7xXT6NyfGm4sDci-vhMA5T8ZKUpN0GGFAV9FolZDxGFugxQX6M2rrYsIgfGiSXQVYYEIdF9NLaPb1O_RrHNolcET1vfHMCkmXj-pS6hr-JaXiPWFVx4KkIX5EizMnA8V_Js13EI6fpBK1zg80EARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310840d86d.mp4?token=UuKnOYiSAgDkGqKaa4mUwE-igCnu1LVca8tWkJWSzOklCJwBU5OIssEaSixgxJG_m-vDto6TSQv0m8exNkkwKBrpfYGRwGDZvbFKIHd1O1uVS0wBF38Hhz0BHdSpb3KRNIUabKRM8zPXvGjeOCkoTIjVS6RGbxmQiIHMjPnxs2YgdAFbaozZqsHzukbyfc5QX7xXT6NyfGm4sDci-vhMA5T8ZKUpN0GGFAV9FolZDxGFugxQX6M2rrYsIgfGiSXQVYYEIdF9NLaPb1O_RrHNolcET1vfHMCkmXj-pS6hr-JaXiPWFVx4KkIX5EizMnA8V_Js13EI6fpBK1zg80EARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: متنی که برای توافق تهیه می‌شود باید از نظر فنی و حقوقی کاملاً دقیق و متناسب با خواسته‌های ما باشد
🔹
در مورد رفع تحریم‌ها، باید کلمات به دقت تنظیم شوند. همچنین، در مورد رفع محاصره نیز باید به طور مشخص بیان شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/661224" target="_blank">📅 22:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661223">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQpP8f7IOpn6PRN4FSjlkWiz9YAT-jvgPrr1s6duy6PT6zGgJlIueXuEWDXK4mUDQzGYxwAIOPnePU6JXNsHTrFKuCH0e4scEFDTCGKM9dc1ATYQpo_alun3NX4u3SC-uODNDUvD6GoMK8nFzPBtliOXfcnhdCF7EPbFrB9NW229Ge-JzhzXeQr5dP4iptWQEy9u7HJSAml1EavbMdw2LWxdTXJ_Q-Cg1hWTQsSONFWriMiZ5roP1ZN7sRdWIlC9bZiePvgjFqT98vP2ataZV-YgfbWiquzaEr8h0Czv9HzF3ahb4TyRYR5Z5GlV0jkatcLGd2RtLqMo7kLGNBmvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۳۰۰ دلاری؛
آیفون ۱۸ پرو احتمالاً با قیمت پایه ۱۴۰۰ دلار عرضه می‌شود
🔹
پس از اعلام افزایش قیمت محصولات توسط مدیرعامل اپل، حالا تخمین زده می‌شود که آیفون ۱۸ پرو با افزایشی چشمگیر به بازار بیاید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/661223" target="_blank">📅 22:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661222">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
محسن رضایی: دشمن آمریکایی-صهیونی در جنگ تحمیلی سوم به بن‌بست رسید
🔹
سرلشکر محسن رضایی با اشاره به عوامل داخلی و بین‌المللی، از جمله ناتوانی در تنگه هرمز و عدم همراهی متحدان آمریکا، گفت دشمن آمریکایی-صهیونی از روز پانزدهم جنگ دریافت که کنترل اوضاع را از…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/661222" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661221">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8ef44e0f4.mp4?token=Shl_rIVg9cVsQGBQw5sPP0LrGpa7ChAUDoa2tZ3U0ZRD1ObBHznru0b32unin_jVLYlzn9fr80lAyNRWvkmEugR8Brl1M6RnRtrcMbgo-4NPWsirTHMquchJhgVd6vcHQQ6wsR-CdLOrBH2xn6FhNc6V7lt7-2foJnA2LGmILt1ExGjPskE40kxBIn9qs4SpX0gDwm4urX6dyQiABsuKf0B3JHOkNVYMDE4KzjV3DY-8Ns79W6COrHi65OOdYhs0tgr2n_8RdFXL9v8E1XxBtiRaaZy3QQlJFoblvIvSl80Qb53tOL5gsPBsFB8wevsWFgGs4sbyJiHpKNhkwDTVqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8ef44e0f4.mp4?token=Shl_rIVg9cVsQGBQw5sPP0LrGpa7ChAUDoa2tZ3U0ZRD1ObBHznru0b32unin_jVLYlzn9fr80lAyNRWvkmEugR8Brl1M6RnRtrcMbgo-4NPWsirTHMquchJhgVd6vcHQQ6wsR-CdLOrBH2xn6FhNc6V7lt7-2foJnA2LGmILt1ExGjPskE40kxBIn9qs4SpX0gDwm4urX6dyQiABsuKf0B3JHOkNVYMDE4KzjV3DY-8Ns79W6COrHi65OOdYhs0tgr2n_8RdFXL9v8E1XxBtiRaaZy3QQlJFoblvIvSl80Qb53tOL5gsPBsFB8wevsWFgGs4sbyJiHpKNhkwDTVqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ به‌دنبال املاک کوبا؛ ونزوئلا نفت دارد کوبا ندارد. کوبا املاک خوب و خط ساحلی زیبایی دارد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/661221" target="_blank">📅 22:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661220">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
ژنو خالی از مذاکره‌کنندگان؛ جدیدترین اخبار گفتگوهای ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3224125
🔹
ترامپ: ما از روی استیصال به دنبال دیدار نبودیم؛ این ایران بود که چنین درخواستی داشت
👇
khabarfoori.com/fa/tiny/news-3224231
🔹
عکس‌های فروغ فرخزاد که تازه منتشر شده | مدلینگ فروغ روی پشت‌بام خانه دروس
👇
khabarfoori.com/fa/tiny/news-3224081
🔹
بازداشت مردی که کودک سه ساله‌ای را به قفس کروکودیل‌ها انداخت
👇
khabarfoori.com/fa/tiny/news-3224216
🔹
پاکستانی‌ها به سرعت در حال خرید ارز ایران هستند
👇
khabarfoori.com/fa/tiny/news-3224219
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/661220" target="_blank">📅 22:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661219">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
خبرنگار آکسیوس: یک چیز که ایران به وضوح در جنگ/مذاکرات به دست آورد: سپردن بار مهار فعالیت نظامی منطقه‌ای اسرائیل به دوش ترامپ، که نتایج مخربی برای روابط ایالات متحده و اسرائیل داشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/661219" target="_blank">📅 22:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661214">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcbca911a.mp4?token=Qcu1dipQ30AlWyIkWkY54e1G6AKuZjpj5CfleUtqCGxyBttcnUdwYy8HehJiic6XfmcBj3scsLPHVsMjuX0GWwlSCh4CdrHXGVwFH9-ABu7g-_nYIxYLfoL_RCr1kZOV8chnVIVtE8Q5r1TKSjEaVd645pO17hxdEh1pN2WtQ2S4jSJ1y0PYbWiVkv0UNsiPwRFGXMZd_VlePfcfbdQlCnBAlrV9aiXO4Y0sW4Nlf6mGNK-inJ6eHEksz0vVKp4rd5eQJkkwXWAJ8KGRYfYxUTAIxn5lhVHSSCWppb0_POGXu-JkXLOjpvtDzgT2adQyQSblpW639stj2VIFeMUQRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcbca911a.mp4?token=Qcu1dipQ30AlWyIkWkY54e1G6AKuZjpj5CfleUtqCGxyBttcnUdwYy8HehJiic6XfmcBj3scsLPHVsMjuX0GWwlSCh4CdrHXGVwFH9-ABu7g-_nYIxYLfoL_RCr1kZOV8chnVIVtE8Q5r1TKSjEaVd645pO17hxdEh1pN2WtQ2S4jSJ1y0PYbWiVkv0UNsiPwRFGXMZd_VlePfcfbdQlCnBAlrV9aiXO4Y0sW4Nlf6mGNK-inJ6eHEksz0vVKp4rd5eQJkkwXWAJ8KGRYfYxUTAIxn5lhVHSSCWppb0_POGXu-JkXLOjpvtDzgT2adQyQSblpW639stj2VIFeMUQRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شب پنجم محرم حضرت عبدالله بن الحسن (ع)
🥀
عبداللهم عبداللهم
من عاشق ثاراللهم
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/661214" target="_blank">📅 22:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661213">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2962f32c99.mp4?token=uJdBQonoOqY1k-uEltaOR2rzREC231MN0tkZYdeC_2cT-IeWR-KYIduU0kmtVDVxjkqr0HnXmEj8tLSNfQgKTSb2fQMqD0PGWZ4briTpHzOFJ-_P2ZivekBfXulFWRCexnd2IZv1XDL5kazxDugPMnJWN6JsYgkPmpZphqAFnInKGF6ZIkgyF8sFbYIM4nN6xTsW3SeAcA683P4u-gkr9p-Gdb0BLCWEu8gs5sq5SP1gqWb9TEk3Y6o6dRqBBfbLPsdtu_9uzL4cN7HXqxQuAt_mpYZGHnoHmY8C8txV5PSEj57XFicGk1OD4jy1NTTNU4vJhJUCGO6eWoaCPAHrFiKUyiXL4vfbm2tlduP9VVYzHPhwecDFiC3He6eSxsx5UHIef1F0d3tiAFMwPcaIR36vCpCXy9ZPvfnAPGAwuRfcCAiTLvFvk6Yh-1jBRz3O7D94dgbjKi76OSvKOlFjo99Py88qARHgwSucK0tObtv_HTculkXndbH5FarsbJ9t-gGau_IrjYUqp8hJketu2yrdBF1pq3TYpASMHzGgUXkAtHb8WO_owc3nnh5EZ3_Y2Mlo8My_cLMtst8qEXC5kN3PwygKgpT8DZM8laBbRlKNwitsmocLpIklT1Kw20JrabnsjqFWD_ELkv8FtcMloIeoFU0kvb04y8HIkca26J8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2962f32c99.mp4?token=uJdBQonoOqY1k-uEltaOR2rzREC231MN0tkZYdeC_2cT-IeWR-KYIduU0kmtVDVxjkqr0HnXmEj8tLSNfQgKTSb2fQMqD0PGWZ4briTpHzOFJ-_P2ZivekBfXulFWRCexnd2IZv1XDL5kazxDugPMnJWN6JsYgkPmpZphqAFnInKGF6ZIkgyF8sFbYIM4nN6xTsW3SeAcA683P4u-gkr9p-Gdb0BLCWEu8gs5sq5SP1gqWb9TEk3Y6o6dRqBBfbLPsdtu_9uzL4cN7HXqxQuAt_mpYZGHnoHmY8C8txV5PSEj57XFicGk1OD4jy1NTTNU4vJhJUCGO6eWoaCPAHrFiKUyiXL4vfbm2tlduP9VVYzHPhwecDFiC3He6eSxsx5UHIef1F0d3tiAFMwPcaIR36vCpCXy9ZPvfnAPGAwuRfcCAiTLvFvk6Yh-1jBRz3O7D94dgbjKi76OSvKOlFjo99Py88qARHgwSucK0tObtv_HTculkXndbH5FarsbJ9t-gGau_IrjYUqp8hJketu2yrdBF1pq3TYpASMHzGgUXkAtHb8WO_owc3nnh5EZ3_Y2Mlo8My_cLMtst8qEXC5kN3PwygKgpT8DZM8laBbRlKNwitsmocLpIklT1Kw20JrabnsjqFWD_ELkv8FtcMloIeoFU0kvb04y8HIkca26J8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنرنمایی‌های زلاتان و تیری آنری در استودیو فاکس اسپورت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/661213" target="_blank">📅 22:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661212">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
محسن رضایی: دشمن آمریکایی-صهیونی در جنگ تحمیلی سوم به بن‌بست رسید
🔹
سرلشکر محسن رضایی با اشاره به عوامل داخلی و بین‌المللی، از جمله ناتوانی در تنگه هرمز و عدم همراهی متحدان آمریکا، گفت دشمن آمریکایی-صهیونی از روز پانزدهم جنگ دریافت که کنترل اوضاع را از دست داده است.
🔹
جنگ و دفاع هنوز تمام نشده و مردم باید در صحنه بمانند.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/661212" target="_blank">📅 22:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661211">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ترامپ قمارباز: من بزرگترین پل آنها را نابود کردم چون در یک جلسه دیر حاضر شدند. آنها گفتند که این کار خیلی خوشایند نبود
🔹
آن پل، همانند پل جرج واشنگتنِ ما است. من آن را در سه دقیقه از بین بردم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/661211" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661210">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c41e3b9a.mp4?token=OIqTZsgr2jSc_C2JY6yXd3mBMOcciM1PKiyh-5rVvQFMsjxR-gIOmbTKIvCoFJT7rUN1TfxHBsIIsD89DBBncDWHthQwM0UfuZR6VJU9PcM-aaBJAu-haO74wWaHCibtP6hsJck6z8Om5a-e4RNPi_RtBHkV3VonlqsZS0pwNx4Z3Pc2Frdzf9Az1thxi4q6VYc5O7tRyeV2E8OQTG1Fezx9AoiyqTYkc2Y5Nl7RuoCufNyO2aKdlUdUE_gmnHs1jXr166Bkp6Wxhx5pltBD3lILgL9B7_T64y9VweWiKMTN6tQCRFvdp-a-cogOdbR-qn3LzPZatKucpdYL_5XyNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c41e3b9a.mp4?token=OIqTZsgr2jSc_C2JY6yXd3mBMOcciM1PKiyh-5rVvQFMsjxR-gIOmbTKIvCoFJT7rUN1TfxHBsIIsD89DBBncDWHthQwM0UfuZR6VJU9PcM-aaBJAu-haO74wWaHCibtP6hsJck6z8Om5a-e4RNPi_RtBHkV3VonlqsZS0pwNx4Z3Pc2Frdzf9Az1thxi4q6VYc5O7tRyeV2E8OQTG1Fezx9AoiyqTYkc2Y5Nl7RuoCufNyO2aKdlUdUE_gmnHs1jXr166Bkp6Wxhx5pltBD3lILgL9B7_T64y9VweWiKMTN6tQCRFvdp-a-cogOdbR-qn3LzPZatKucpdYL_5XyNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میثاقی: باتوجه به اخبار به‌نظر می‌رسد ۵ تیر برای سهمیه آسیایی یک بازی بین پرسپولیس با چادرملو برگزار شود و برنده باید با گل‌گهر بازی کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/661210" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661209">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ترامپ: من از رئیس‌جمهور چین خواهش کردم و گفتم واقعاً ممنون می‌شوم خودتان را درگیر ماجرای ایران نکنید
🔹
او می‌توانست وارد این موضوع شود. او می‌توانست یک نفت‌کش بزرگ را به همراه دوازده ناوشکن به منطقه بفرستد تا ببیند آیا می‌تواند با درگیری، راه خود را از میان…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/661209" target="_blank">📅 22:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661208">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d53ccdde.mp4?token=HkEC6HfhKXdgyqj5OwuSly5SP4Yt4Y6LzkgiEKtORIAmgEFMn1aXvZd4QoEXstEQmbqJGGSrhMuSqAN5DvuAfKo3ecQSYeDz5kCexD4y5LgXPjUhCoOHl4W1FBJ7zw3SsK-hsPD2gJMcGY4RHoVowqOwNxkdQ9QBae_dSRqd2rpJtRsQ3TeglDoF0rMOaDjQYl8nyBOqShHqC_gevwtAstq30dpV37ce4YWqYP0mbhHPAmmjOQAdMXwFH2U-FLo3YDGDDBeO_5Br352evCGCzED1yl2mzB8aZFJp_s9vPIuqn-Z42tPf6WRMKtyQX9OnISR4cCCMMYqwGI6_-wP9mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d53ccdde.mp4?token=HkEC6HfhKXdgyqj5OwuSly5SP4Yt4Y6LzkgiEKtORIAmgEFMn1aXvZd4QoEXstEQmbqJGGSrhMuSqAN5DvuAfKo3ecQSYeDz5kCexD4y5LgXPjUhCoOHl4W1FBJ7zw3SsK-hsPD2gJMcGY4RHoVowqOwNxkdQ9QBae_dSRqd2rpJtRsQ3TeglDoF0rMOaDjQYl8nyBOqShHqC_gevwtAstq30dpV37ce4YWqYP0mbhHPAmmjOQAdMXwFH2U-FLo3YDGDDBeO_5Br352evCGCzED1yl2mzB8aZFJp_s9vPIuqn-Z42tPf6WRMKtyQX9OnISR4cCCMMYqwGI6_-wP9mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: من از رئیس‌جمهور چین خواهش کردم و گفتم واقعاً ممنون می‌شوم خودتان را درگیر ماجرای ایران نکنید
🔹
او می‌توانست وارد این موضوع شود. او می‌توانست یک نفت‌کش بزرگ را به همراه دوازده ناوشکن به منطقه بفرستد تا ببیند آیا می‌تواند با درگیری، راه خود را از میان محاصره باز کند یا نه.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/661208" target="_blank">📅 22:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661204">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">روضه</div>
  <div class="tg-doc-extra">سعید خرازی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/661204" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک هیئت قرار  ویژه شب پنجم محرم
🖤
#محرم
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/661204" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661203">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
احتمال شنیده‌شدن صدای انفجار و تیراندازی در شهر مهران
فرمانداری مهران:
🔹
به دلیل تمرینات رزمی یکی از یگان‌های نظامی در حاشیه شهر، فردا از ساعت ۶ صبح تا پیش از ظهر احتمال شنیده‌شدن صدای انفجار و یا تیراندازی وجود دارد.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/661203" target="_blank">📅 22:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661202">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmj_DkYwJYt2coBR4T_S8YhJyk5_8yUhtqno6a0BtJPbIOUnKkXgaKXQbZS6dKKpFBJNHQ7PXaZP1R-nBQAZ3AT6asClbIm0OJzOaLLRlIUryUVERPAUR76DtHihiLb1vo1rd0tlX__Um_70AqySYLLij0ATFQnQLfT9Wjl7wnjJJUI8Jfbxi2KBG8JWw2CxpClqlUECEB4xDFCfaXZ6Cy9RA5GjJngYD0ExXGxY2IPJ2Ju597w9CJ4ONxc-5RuzFHhcR3alMdG23rR-Y62qmHeVcaj_raztaR0NRnqWatHDREZrjam8BiA68AyWwoDbCsUQITa0NuCFl6TNnqY07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
یک قرار کوچک، برای رسیدن به کربلا...
پک «اشک تربت بافت» همراهی جمع‌وجور برای لحظه‌های زیارت و دلدادگی
🌿
📦
شامل:
کیف چرمی | دستمال اشک بافت | مهر تربت | کتابچه زیارت عاشورا
💸
قیمت اصلی: ۲۲۵,۰۰۰ تومان
✨
قیمت ویژه: ۱۷۹,۰۰۰ تومان
🎟
سه کمک‌هزینه سفر کربلا در انتظار شماست؛ با هر ۳ میلیون تومان خرید از قرار، یک شانس دریافت می‌کنید.
خرید از «قرار»، سهمی در مسیر خیر
و شاید یک قدم نزدیک‌تر به کربلا باشد...
📩
سفارش:
@gharar_order
🛍
مشاهده محصولات:
@ghararshop</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/661202" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661201">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_NnMfWYnmKsoaHabupxPGSKXKJ0eRdDEzmW3K1p3xH-ExjdHrVA3o8AmvTO977mlfC0cvX_Cf7U_7P0HkYzyguxxgPOsn330kMMmzLsoDlAx_oje--__du64EqvWqHdQBCgbGu8Jgig-sqKENabjgcKhKnki9njD2RPm_WXU67oCWfkN_MF0ZFd-Gm0GQP4z5nB9DPH47VGNka7qFEvYQhUfOsNTjtHa0zIRudIkZb_QnOCbXAo1NUPmaKZzqCsINOu0vjj1gIYPK4iWKsg5f0MNjB_k740aYhfyewikOD9zDmE0WlaSJJVJ7-QS3vCVQmFCsksBRa0UL9j2e4kdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دما در ایران همچنان روند افزایشی دارد و در غرب کشور و حتی تهران با افزایش دمای ۱۲ درجه نسبت به بلندمدت مواجه شده
🔹
پیش‌بینی شده که دمای هوا در ایران به ۵۲ درجه سانتیگراد هم برسد و گرم‌ترین روزهای سال ۲۰۲۶ در راه است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/661201" target="_blank">📅 22:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661200">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835c2e4505.mp4?token=Qh696WDRCf-wohtnnfOOUaIpuEBU3ruWBDGIdxMr2TUf8IbPqhfb4gID9DSwH4Kg3t90npmhN177pyb5lMdl9vhkcg3ftWlty2THZB7lK4AzNEnotS8_vC_FSWl8SEwn4zSDJsexGAW5cU90b75x4LeieuUvZTcCRGeljPSX5nkaMAqAf8qY11kKTdxJJCEX-x66ZWL38SVhG4Hw9dwhYBYWEYeLReyVdwIEyoXLi6vpcF0lvkTo45ItitbqbHQTBMFgn5Zdse4Yq5bOuHv_Wiq_bNRgwg8G8NttkTIBKjM8FnOmCSyJCpPY1L0DbWRHzyjg72PXM83Jw0PUR3nITg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835c2e4505.mp4?token=Qh696WDRCf-wohtnnfOOUaIpuEBU3ruWBDGIdxMr2TUf8IbPqhfb4gID9DSwH4Kg3t90npmhN177pyb5lMdl9vhkcg3ftWlty2THZB7lK4AzNEnotS8_vC_FSWl8SEwn4zSDJsexGAW5cU90b75x4LeieuUvZTcCRGeljPSX5nkaMAqAf8qY11kKTdxJJCEX-x66ZWL38SVhG4Hw9dwhYBYWEYeLReyVdwIEyoXLi6vpcF0lvkTo45ItitbqbHQTBMFgn5Zdse4Yq5bOuHv_Wiq_bNRgwg8G8NttkTIBKjM8FnOmCSyJCpPY1L0DbWRHzyjg72PXM83Jw0PUR3nITg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش سوزی گسترده در یک کلیسا در بروکلین در آمریکا
🔹
آتش‌سوزی گسترده کلیسای ۱۷۴ ساله ساوث بوشویک را در بروکلین،در نیویورک در بر گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/661200" target="_blank">📅 22:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661199">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccdd7de42.mp4?token=VqN94p8e3hND18pSy2740dPtY_30cQgpUREV51CNLCfSfUKMQzYoj_tP0NhqL1CptwAjILYLddACXGPqmffboZ1Cdjgw55dNx82p0HV5yhZ3uB0ADGgR6uZ1GRyqJK1b9SPMmQ3DKYMsjxuK2b03IHTmBoMzx_Td_uQNZMqcXmZtOcKIkG83_HkmFxhR8uLUf9AhKCtpB1dhgC07BKEi6MMVourzRhw4kk-Q0scL6SwTIHRnWqYaitUKxxZBbYRNX8ZC486MSoKuFS64f9OubjbzZKTCwVF7G1ZaoM8P35kCAuEoo19PYXPF69B1JacdUgrYOK10IkxH7zbTT9HQlCaY_tzZU-pk0CX6O4tUrwEgN6aB5WfSJDBRCrU4M9UYXxYdThasP4DnJVFlkLyHfURAzPRLsmevzY6eZHbPA4oaTI-TpDbpqKsXLeVF3tPLkIz8lSJxjrAyiWtSCKDQu3A3Aaz7j28FDuXVWVvXBfQTFnZCfSj47XlMK_R2nmGtYiN3_fT5yl1grqAgta64vml1fjCWbEEjaG3YLz5fk8btMy72vPoS9X_JjHr3CqB-Hcrfn1kyeZVCaE1ATJKdIHsOAnZNNix3Rg5QW_zw4y5SR4edQ8LAIRvMZdTK2hmUb3Mt3ZxoBmzkWayD71ymJ4py-cYvHdWzGHRa1eCyTjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccdd7de42.mp4?token=VqN94p8e3hND18pSy2740dPtY_30cQgpUREV51CNLCfSfUKMQzYoj_tP0NhqL1CptwAjILYLddACXGPqmffboZ1Cdjgw55dNx82p0HV5yhZ3uB0ADGgR6uZ1GRyqJK1b9SPMmQ3DKYMsjxuK2b03IHTmBoMzx_Td_uQNZMqcXmZtOcKIkG83_HkmFxhR8uLUf9AhKCtpB1dhgC07BKEi6MMVourzRhw4kk-Q0scL6SwTIHRnWqYaitUKxxZBbYRNX8ZC486MSoKuFS64f9OubjbzZKTCwVF7G1ZaoM8P35kCAuEoo19PYXPF69B1JacdUgrYOK10IkxH7zbTT9HQlCaY_tzZU-pk0CX6O4tUrwEgN6aB5WfSJDBRCrU4M9UYXxYdThasP4DnJVFlkLyHfURAzPRLsmevzY6eZHbPA4oaTI-TpDbpqKsXLeVF3tPLkIz8lSJxjrAyiWtSCKDQu3A3Aaz7j28FDuXVWVvXBfQTFnZCfSj47XlMK_R2nmGtYiN3_fT5yl1grqAgta64vml1fjCWbEEjaG3YLz5fk8btMy72vPoS9X_JjHr3CqB-Hcrfn1kyeZVCaE1ATJKdIHsOAnZNNix3Rg5QW_zw4y5SR4edQ8LAIRvMZdTK2hmUb3Mt3ZxoBmzkWayD71ymJ4py-cYvHdWzGHRa1eCyTjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت پنجم مستند احیا و حقیقت | آب حیات
🔹
صدای انفجارها خاموش شده بود... اما اثر آن هنوز ادامه داشت.
🔹
اندکی آن‌طرف‌تر، مردم با صحنه‌ای غیرمنتظره روبه‌رو شدند! شیر آب باز می‌شد، اما آبی جاری نبود...
🔹
آسیب به تأسیسات فولاد خوزستان، باعث قطع آب منطقه مسکونی…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/661199" target="_blank">📅 22:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661198">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امیرحسین حدادی، مدیرعامل یارا وندینگ، با اشاره به نقش وندینگ در توسعه کسب‌وکارهای نوین گفت:
«هدف ما فقط فروش دستگاه نیست؛ یارا وندینگ کمک می‌کند افراد با سرمایه‌گذاری هدفمند، یک کسب‌وکار مستقل راه‌اندازی کنند، درآمد پایدار بسازند و به مرور با افزایش تعداد دستگاه‌ها مسیر رشد خود را توسعه دهند.»
وی افزود: «هر دستگاه وندینگ می‌تواند نقطه شروع یک فعالیت اقتصادی مولد باشد و ما تلاش می‌کنیم با پشتیبانی، آموزش و خدمات واقعی، این مسیر را ساده‌تر و مطمئن‌تر کنیم.»
یارا وندینگ | فروش هوشمند، بدون نگرانی
https://t.me/yaravendingmachine
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/661198" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661197">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQJRWyNTUqtoa2ROF1DRy5JHQK5bbJaSG6zQwlZtVPPR0cdLC6uxzBpXtI1LYp-QJh_DzhCPM_4RiWhRzBmXYiwXpUjlG_kWW17RHC282Gpv9Ce8h1vGLJ_w3jR8L10lqw6tQMB2Z2A3WP_lhGulmzHizxucogVzw5NGlRxX2hBn4eVzomubDrQCBFt3xnT9pZOG6o1HDZWxzCwagm1QFwnKNhQH7umDJzJE6Ap2Qzp0V80-2EvmB4fnA1jpEycJzq3HXbqroqapTp1eqKGEFGWD4jiOBR4xBk27y1R23-ZP_NLkDbyNMUjCCkTiHkj0zjFsYjjyQe-VyUKcZ1WCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/661197" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661196">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9d7605d0.mp4?token=M3-HLrPqXGq1O_53DS3H2nyYN3AK8QjVjFP4lSXrxQTrFxdlmHHkdyq0H-oFgFIkN105xL_mFsO-cq4WLKJpPKpk8UWwfAkGAj6xt8fczVIzlkoKAe6cyqcO6F_PBErILLDuK30fWvXgHbEujmFMwSbzminyWJajuVHLUdf4eCCccJpLENlKPcow0R8q90pAQtrGe-ogoq9NKsFajMdTLvXyWDMnJ8pwAW68-RXaMMQS7YckynKOkpwA0_NciRHbK5ffbTmugyapVV_oMAbr2X1i82CXirQAmPtSrqFY1w5Wnxuq8aXpgeGRJu1yS4fgYmUPDy0woffEwgxX6j8A4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9d7605d0.mp4?token=M3-HLrPqXGq1O_53DS3H2nyYN3AK8QjVjFP4lSXrxQTrFxdlmHHkdyq0H-oFgFIkN105xL_mFsO-cq4WLKJpPKpk8UWwfAkGAj6xt8fczVIzlkoKAe6cyqcO6F_PBErILLDuK30fWvXgHbEujmFMwSbzminyWJajuVHLUdf4eCCccJpLENlKPcow0R8q90pAQtrGe-ogoq9NKsFajMdTLvXyWDMnJ8pwAW68-RXaMMQS7YckynKOkpwA0_NciRHbK5ffbTmugyapVV_oMAbr2X1i82CXirQAmPtSrqFY1w5Wnxuq8aXpgeGRJu1yS4fgYmUPDy0woffEwgxX6j8A4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناریوی خیالی ترامپ درباره ایران؛ حمله دوباره به رسانه‌ها
🔹
دونالد ترامپ در اظهاراتی مدعی شد که حتی اگر ایران با «پرچم سفید» تسلیم شود، برخی رسانه‌های آمریکایی آن را پیروزی تهران توصیف خواهند کرد. او با طرح این سناریوی فرضی، بار دیگر رسانه‌های جریان اصلی آمریکا، به‌ویژه نیویورک‌تایمز، را هدف انتقاد قرار داد
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/661196" target="_blank">📅 22:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661195">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
یمن: مقاومت در برابر تجاوزات اسرائیل دست بسته نخواهد ماند
🔹
رژیم اسرائیل از طریق تشدید تنش‌ها می‌کوشد تلاش‌های صورت‌گرفته برای پایان دادن به تجاوز علیه کشورهای منطقه را تضعیف کرده و هرگونه اقدام برای تحقق امنیت و ثبات را ناکام بگذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/661195" target="_blank">📅 21:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661194">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8082710da.mp4?token=JzxDvM1ml1vPzp_5JNxsfLnthV364GyPCwuq_jMfOmzv97EjcxkmkxwLxLX_q9GpfjP_v36MhJpMvnLIFys1K2oqdT2Msr8-D5I7wNzxE5Er0cz1XYG0VyLA3Si2Ub7ApmXEed-X5tq1bFvTuCpZOeFWdymZFJE3Pz7WD4FWzViOLHmC_8uz-kedRSJZWNmVLUEp-3q-PpH8bEP3-jyDJ9XAV3OTV_O1Yx2Nye5oX5lUhtSz7mTPlJ5PKvRqBuJemXNqyF6UEONWvN0cm1orM4S7eaY_BMWSjSDBy-Di4g7GVs23vRrr4jI07npBrRm6BvUDi9az4jK_XjYDpX5vCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8082710da.mp4?token=JzxDvM1ml1vPzp_5JNxsfLnthV364GyPCwuq_jMfOmzv97EjcxkmkxwLxLX_q9GpfjP_v36MhJpMvnLIFys1K2oqdT2Msr8-D5I7wNzxE5Er0cz1XYG0VyLA3Si2Ub7ApmXEed-X5tq1bFvTuCpZOeFWdymZFJE3Pz7WD4FWzViOLHmC_8uz-kedRSJZWNmVLUEp-3q-PpH8bEP3-jyDJ9XAV3OTV_O1Yx2Nye5oX5lUhtSz7mTPlJ5PKvRqBuJemXNqyF6UEONWvN0cm1orM4S7eaY_BMWSjSDBy-Di4g7GVs23vRrr4jI07npBrRm6BvUDi9az4jK_XjYDpX5vCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ایران ۵ کشور عربی را به آغوش من سوق داد
🔹
اگر ما به ایران حمله نمیکردیم، آنها یک سلاح هسته‌ای داشتند.
🔹
از آن علیه اسرائیل استفاده می‌کردند، همچنین از آن در عربستان سعودی استفاده می‌کردند.
🔹
تقریباً بلافاصله موشک‌ها به سمت این پنج کشور دیگر [قطر، امارات…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/661194" target="_blank">📅 21:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661193">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99a54fb01d.mp4?token=ea4H9QKjCPjkrEH636bjrIyvJc4aWY8w4CCdcTuTrQwMrpXg4W7_kvFbVaQ3EKVEvRwOc1KJwYIyZJLZW57I4S1ZSxw8Z-7TVb9EHos8KcHOat6IAfHpnoaE3kItbQb9lGOlZ4mF_rtY1IFJb_0TCQXXzjxU79aXJvWQ4z5KB-cWf6oMT-i6RWOFs-y1VVe1WuGHJYfZB-QyweWR1frl0nvw-OSgxPTi3M3ecSjWJOvbhOqElNP2Z14EYcaL2F4lgFhu46p_OUlX4Q0xeJ_GXjxDbeqNFE0ih-gT1KYbydVW2J4N7OtrgsHiUVuRUiq1C8DiAPYqn1aRPEcmPy_vhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99a54fb01d.mp4?token=ea4H9QKjCPjkrEH636bjrIyvJc4aWY8w4CCdcTuTrQwMrpXg4W7_kvFbVaQ3EKVEvRwOc1KJwYIyZJLZW57I4S1ZSxw8Z-7TVb9EHos8KcHOat6IAfHpnoaE3kItbQb9lGOlZ4mF_rtY1IFJb_0TCQXXzjxU79aXJvWQ4z5KB-cWf6oMT-i6RWOFs-y1VVe1WuGHJYfZB-QyweWR1frl0nvw-OSgxPTi3M3ecSjWJOvbhOqElNP2Z14EYcaL2F4lgFhu46p_OUlX4Q0xeJ_GXjxDbeqNFE0ih-gT1KYbydVW2J4N7OtrgsHiUVuRUiq1C8DiAPYqn1aRPEcmPy_vhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ایران ۵ کشور عربی را به آغوش من سوق داد
🔹
اگر ما به ایران حمله نمیکردیم، آنها یک سلاح هسته‌ای داشتند.
🔹
از آن علیه اسرائیل استفاده می‌کردند، همچنین از آن در عربستان سعودی استفاده می‌کردند.
🔹
تقریباً بلافاصله موشک‌ها به سمت این پنج کشور دیگر [قطر، امارات متحدهٔ عربی، کویت، بحرین] پرتاب شدند.
🔹
گفتم، چرا ایران این کار را می‌کند؟ و می‌دانید آن کار چه کرد؟ آن پنج کشور را دقیقاً در دامان من نشاند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/661193" target="_blank">📅 21:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661192">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7980096d80.mp4?token=GrKwVT_ZxSQkt_Y447jtOochv6WEcAb-NMEbEYp5g7uIy_aRPlylA8eyQ08wYDx2vICkCjximX03MaQjEthNVIDGhXTXr9s0tqwGwWE0oLsBPfaQfJjVNQ2JRL5JnUwsdvslnGcyYKf__E3eBTjglh5PPZzR6Xus9ohFGnOdSZyMhsq-XFqgY3iSPYv8uD55hBIkWq7ggDrRlZ6pOrrC7rE4w44NkYVsyTzMcq5OIWEPdG-tTYpxuuJOUzJB4R_tCM3rOFs2TDAz63H1Lg3KZGQGvUt8AObAYUGsLLXdKus3mE_y7daP0yF3mTwMfQoN_n8IiEBvGRLOXLvUilMMGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7980096d80.mp4?token=GrKwVT_ZxSQkt_Y447jtOochv6WEcAb-NMEbEYp5g7uIy_aRPlylA8eyQ08wYDx2vICkCjximX03MaQjEthNVIDGhXTXr9s0tqwGwWE0oLsBPfaQfJjVNQ2JRL5JnUwsdvslnGcyYKf__E3eBTjglh5PPZzR6Xus9ohFGnOdSZyMhsq-XFqgY3iSPYv8uD55hBIkWq7ggDrRlZ6pOrrC7rE4w44NkYVsyTzMcq5OIWEPdG-tTYpxuuJOUzJB4R_tCM3rOFs2TDAz63H1Lg3KZGQGvUt8AObAYUGsLLXdKus3mE_y7daP0yF3mTwMfQoN_n8IiEBvGRLOXLvUilMMGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نانسی پلوسی درباره ترامپ و ایران: ما یک توافق خوب را پاره کردیم. به جنگ رفتیم. متأسفانه جان آمریکایی‌هایی را از دست دادیم
🔹
ترامپ فقط نمی‌تواند با این واقعیت روبرو شود که اوباما در تمام این زمینه‌ها موفقیتی بسیار برتر داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/661192" target="_blank">📅 21:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661182">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHB0y0Va1Ls7gPgYM1Bfrmses8cY3Oywz-4lR5FNhOPF17qUE0KUgg4QsS4VAtfRNudBIEq-_gR3B62jjiKeIIrMSA1HKoa5m_nq_ZNMeDP0XW5uLg-vgUeC26SMMghr7GNPoysBY3KBcnkF6hxSX6wm-Bn5Di8U37ziaYZMDagn0_QXeYob_NV23b3C9KbewX1kppaFeVXwrpJm6slhLGCAxl-y4ncRPDjZ8N-V27aFeyVAtVz5S1vt_eHqYCkfClpIZk2oRISxLJdkq93-W-P9zcG4xt85uDUn4uRFGzbL8HsYZuOvY90GYSDihUbFK206kVQGvkKC7lU3SWAmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILPL_7is-gDDHe7I9xScXAtF9aLkQMZYOvF4w99vkfYOZzY_7bj3ic62SUEocz6X54rrYLrOFN4DGUNrOQSP-5tgaTvvBrBnwQRsK-Nqdavqk4uOgl4c4wCCbcLOLTgKgXJacOtF8mKbDlXB3On-Q8kK8VUzB65_qjntVXXqaIvE0yPAJ_yjhb9-1za6_2aEqkAxlu9E6ztn3wZGo4feCCDmF1l4lZDeMe5sxGXNvr9Ls32V9f0PZj45QRg18bTXqk89WkVj9d9GHvfRvTPYG7V2z1-JrmW7eIYnOhdGK_m88H7RJwwD6w0eDJwqVUNaDERyvL33xMGq87ydygJ5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXjaDW4nzsaUt9gmXQBDhrDSHH6bSnK7w5FIadk27JY19_tm-oqrk9oD5xSB2w1ipnVKIGtlhoD51h9LrUBHvvBD-MDpQPuNx5Mp3nOxTU_cAEvtlHr6KvFqDJv_4ekW34xIGMduo5Y6nAmQu6I7uD0PfKPr_QyXVZehYPdZ4He4-gqch-XTrdlT3FmSNmL-ds7vE17RaVHiAbTsgmaY54LBVLd1m1LvQnohrxflIeVX1pHIRnkAwLsRQpoYwDDJmbGVHBnBIqAUyvRrrNvp28ID4bDLGZv90Jp_Wq0iyPu2ivasaeKdfVs8yM0xH30pEsH3FncJFVUrhZdBV243wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5h4oowO7u7b4NTM3vgH5hIPqKoGmL1kZ4xdF-KPudfu_5RdqZqngD0SWOWH-TMk6o_L9XFes1UmoZb1cY0AscMz4Zhmf5sNNfRWiCqg6aJXghGMpTEVziV1_W0LHhA8huYwpErRfwsEzFaeVuuqJU_VJ6XMnV9YDhCKIxof_PIad4_Y8lG9LUW5fkM6SvpGXLiJeYa-1lG2DMRSAjeiTG92S1rxGSElNH571eps2jsjt2k38RnLNcq942fSQJ1VpCYDACUO5K0FaNZD9T-l7qUCc-9fooynLHuzw44SYdvUGqdXTlbS00vkDpgAqGYZXRrY55_0XBC3DC8DStn-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sE5isTyMUVApgfwtVDKvqF1YcepIEoEF4IHoXeTAhekId61x0dINFbAZOqvz4CtcDYFlpMhaFfjegGRUFXbg0ZB4KYtBKCePnWmCVoWzvOB1R3xaMGws0CuwIUNGQEyMCPddNolv3VSREVHA15Urk8fvhiZt_ngILscUY2ENGp0vniUPsjYGAukZMYPoi5Z-KFWk-o7EZ7jWkOpnS7BnCjcHw-uAYDP2i20PRqmRuWWUuUECAOrVUKjoQnBBe01UniamndQBmXNBg7XkMJFVJ1UsTCWjMl8L-mohhujpezVoAhOrGXwRsWsm-1BJ6dzsObnhMW82HaRgKlkzxMhySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LkfLTNGzgng23En8AAh4Jk2iNYDJcA-3qcvM3zyMvVdngEqUvHRgnzW9I5gr-43GwDcTwz5M_Zxoxjp_5X-kN3HwRdfQWYiw9WBqUK-gJsMw8108I5fm9omuNsy5yvc_YIC11Bc8qRK4pG2ibzjK4eEyy_pQ6dzvFDmxyShawp1qFm7tcmgKF1x8_ALHIwxcXpwq3QD_p6REq6-l8ZK0F398AlEpJFpGI5cWBCQISBVHcyODf8WnXVSRzbHewdETtcbHuL4RF5Hl-Gchmjpf-IKzfOCZwBA4KaJDdZ38Zq5nHNYHH7Ij_nfYX_3yZHstdYKnIo_PfHd1xyPcPtqrFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfjAmVtFfJ8BWbdhD53eFen3ihbhYnDW_m5LmeDDqhOwL7uASuHy9ZetLkPOlF5xnuYbf5tWeFE-7L0uPU3GQqSwTy7KeyPFbPTkvLKvb0hIl2Ku-ftdAQc-9dDnj34C9LM7cftqku0hR_oBnNIOKZntDTfZ_Lml3alI7312GT-C9SxJK8ojpby_SZFc1TnxBiWiHW0CPsJwTBZwcOCYjZpzRrQ3AONLLO5dHKGV8KdYsQ8ufj3TvhJZLTacO4N7CrurAaosCvXvdlDX1no8eAwViUFqSUzhQb6eq2GBjkROzy9u8ziSJaB2Ic11fRIW2dq0Ss-hHjgq59pT7Kqo6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TENVQT761ieyPhiSrkPMzXJhYJRE-99U1q79BoHDrGRa5zih_oEFHFu_qjbn85nZMyCwZMecYxLdZuIEaKgPllX_syiMSx5rTTNIQdCNxWLjEKu9xapmzbBjjqKhURUi9rRkEwsvx5eVDWsjvQWcI4aE7pVFkesC_i_55_10NuZA4mOACBLgUMtcseq8NBSLmZJqrz_aNt4IFESxRmI7BOF4urdi_FIJycEphM8PbwrfjdpFALYSYCeMwbzALhOAXCwjGPTMeIcZe1eygVZ4znSls47ii6GmRlQgOs_tYFhz98HUJvUoJsRckLT-Ff-760ahoCvBX3zjgMIqAO_3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulDuXrxb4eLwDQYpJJjHi02c0i0b57bXTZoylJprXfeVzpzV4R9NPOBew05ZvgdSQfdkabRlGgW5y7Rk9TJ5zT5eDLN1ej6QCDtHIEycTvEGbF6zx_Q5Mu5MlMAUXs1zGTSWcbPAkvTP-TV2EFbn6tIfsC0DfTbZJFR3S1rL8OeDVw92IkfDz6WoDhxQrADzPmG2aW0GotSbBILKNJzR_ANzzPX1y42An37woq4qT7ldlwK0ncrQEnQ1d04t850AmHTtNhVbMAwa32zPCFK2Wa5LPzSwd_30N-30xXsxG5TH30YXG0n2Xf7WqwjiYHCaj1v25nyB_JKfa9XIp5mjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1FYgSNCnAOjB_T7O3jQGn3-c1Rl-v-j0KoU37c9P7wXbwKMwBjf1TGeUG9npfcJ52HJjjGop8V7_g869kS2motZxNh3ng4txcMuoPc9MTM2DNMkc-XfxJINFLjEd8jPJ125y57ZcPQBizjYy6_yNtDt3UfBpGVmvORRrXO1QcapaeOJDdy9cnGTWlZ161YJQxViWUoxqGAJ8w1hM_MKXkx7gy1yVwXVg51Q8HDiaURHztFJRlRTt6J6M1mG9h8GAJs6AZZB_LFfsf7wBmhGsfZwcakeR1FFTyPEieO4h_VmlmMBHz1RIGEIq8_5jTysK-H-Yq5jr_QLZWpCIzGyNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیرخوارگان حسینی
🔹
گوشه‌ای از تصاویر ارسالی مخاطبان عزیز خبرفوری در پویش بزرگ شیرخوارگان حسینی.
🔸
شماهم میتوانید با ارسال عکس فرزندان دلبند خود به این پویش بپیوندید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/661182" target="_blank">📅 21:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661181">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ادعای سفیر رژیم صهیونیستی در آمریکا: عملیات تهاجمی خود را در لبنان متوقف کردیم
🔹
سفیر رژیم صهیونیستی در آمریکا مدعی شد که این رژیم، عملیات تهاجمی خود را در لبنان از ساعت ۱۱:۳۰ به وقت واشنگتن متوقف کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/661181" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661180">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwuPCZK8nL77ExwZb4T7z9nBDqWfjmHxuC37DGRDCnouIfoBGRJX8z02BSP-uSq97D9u1ESqA0pwiRUqIbQJS0mCU8cZtqTzl6n-JS1mcvlpoaKLrnAYprgvM3vWSfxIHHeIfIgRSW9jVmBr4GJYwwPGdHkkWgMUeZyvKyzqNRSEMkw3_jM7AmLDBMQxPbivFtY5HoAjJZQfbygEy1COEq_kqJKQXcB5DSVaULBRM3s0EUK8lCubrSlgSauw7Zx4jl6dGGdCLutAjBr0aRSAfBNYMebMdxcIIrnMRygPHUUqWoxGcmQFiQdFAGq-0jvKnMpL7wM9ldz3NgbK4FTu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: غزه هم طوفان دارد، مراقب باشید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/661180" target="_blank">📅 21:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661179">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8f63c4d0.mp4?token=o6BxCegIV6vXCHJwdbawHSwLklTa6eh7p9QUy-Tdk8FcPMs4F_bIGhl1Z1tdrPBvR6nYdr-cFQcOSyNa1lPeLW1zwqSHH31fOLH7aN5MRulc3RhC0muDQYrfxUOQ7dvLy-o9jtQngCdvRMxliWbPOvWde8WSjp_Vve53cWk5gk3sgK38LBVClCscvKIantQ1MznmaPhihxV1WlsJ58h0m78xAFhlbQxYPOPvlGhcZv8ByI25sIMfx8GaMWgaXrcS7RCnPxSFxgYI3DBMy3x7ACbxsC4jeHa82eTwmxcjS0snLGf-gJ3T6IfZTI1SRGXAGNcBFgjTVC2yfUrqGqprYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8f63c4d0.mp4?token=o6BxCegIV6vXCHJwdbawHSwLklTa6eh7p9QUy-Tdk8FcPMs4F_bIGhl1Z1tdrPBvR6nYdr-cFQcOSyNa1lPeLW1zwqSHH31fOLH7aN5MRulc3RhC0muDQYrfxUOQ7dvLy-o9jtQngCdvRMxliWbPOvWde8WSjp_Vve53cWk5gk3sgK38LBVClCscvKIantQ1MznmaPhihxV1WlsJ58h0m78xAFhlbQxYPOPvlGhcZv8ByI25sIMfx8GaMWgaXrcS7RCnPxSFxgYI3DBMy3x7ACbxsC4jeHa82eTwmxcjS0snLGf-gJ3T6IfZTI1SRGXAGNcBFgjTVC2yfUrqGqprYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوباما: از آتش‌بس با ایران خوشحالم/ وضعیت آمریکا بدتر از قبل جنگ است
باراک اوباما:
🔹
خروج دولت دونالد ترامپ از توافق هسته‌ای، ظرفیت هسته‌ای ایران را افزایش داد و با وجود هزینه‌های سنگین جنگ، نتیجه نهایی تفاوتی با گذشته نداشته و حتی ممکن است اوضاع بدتر شده باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/661179" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661177">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bfbc62e7e.mp4?token=vYd7gAZNdR6n-2iC4RwdevX8zWg9DqeKxttlsZ18UJ4gFc30czeIx4WA1sZuM7g4F5EGD-QOV3wWuykfVEu5AmWTgI5P0CJo5hhXKGKiMYNBI9p8avQHvXp4m32Tvsgs-btqJQeAdAey_uXJHeSbth5RNCotiNENOxjNMGRdUEYckMzUIIrLkxkfXKPKBwa0KWqTOsmMLH35YAfDg7DAgMWB8MOBo9gZmkF46MpxTNR8sOY0SGdVdnts53InD41jSCzTQf00I7N4Hj68kIw2-484s6mtPKf3Pn-4OtRH9SZ1hBAJl2tIjBz70RLrzSHbjeGiYwJr-KeY_Y4rv1f6zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bfbc62e7e.mp4?token=vYd7gAZNdR6n-2iC4RwdevX8zWg9DqeKxttlsZ18UJ4gFc30czeIx4WA1sZuM7g4F5EGD-QOV3wWuykfVEu5AmWTgI5P0CJo5hhXKGKiMYNBI9p8avQHvXp4m32Tvsgs-btqJQeAdAey_uXJHeSbth5RNCotiNENOxjNMGRdUEYckMzUIIrLkxkfXKPKBwa0KWqTOsmMLH35YAfDg7DAgMWB8MOBo9gZmkF46MpxTNR8sOY0SGdVdnts53InD41jSCzTQf00I7N4Hj68kIw2-484s6mtPKf3Pn-4OtRH9SZ1hBAJl2tIjBz70RLrzSHbjeGiYwJr-KeY_Y4rv1f6zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: در درون رژیم ایران هنوز عناصر تروریستی وجود دارند، اما در عین حال عناصر عمل‌گرایی هم در آن هستند که واقعاً به دنبال برقراری رابطه بهتر با ایالات متحده هستند
🔹
این ایده که اماراتی‌ها یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، در حالی که ایرانی‌ها رفتارشان را تغییر نداده‌اند؛ به‌کلی پوچ و بی‌معناست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/661177" target="_blank">📅 21:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661176">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
صدراعظم آلمان: آتش‌بس مورد مذاکره ایران و آمریکا باید در جنوب لبنان برقرار شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/661176" target="_blank">📅 21:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661175">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69065e0edc.mp4?token=FwA8OBdAvOfJQRmRTfW5cEwm-3pZAFpiGJgUaXupQL5pLB_EL0PKIY7e0NmQwk_itccatqqzVsoyQbI8kJVZ3VoAa0x-_ckE5MX4I-bJTOEwRIlSxLCxFMbli4pbLcrxYwXQMUKnW4mU6zBaFGehc1AQveLwHSj_QAgU7-NCMp0SiAdKm3hM42bQGTLisNVDsPm9opFeYU8kDWeMVF5xK0C6-c9KCPoiZ5oIgwdCTO9hcdm_wWLaQpIrHjNlgmCr1vePipT_A3qh_Em9joK9ovvTZ0xSBhbEH_wcHu9KRyfJ9V0d1FrhFtOuKMHJHX8C1JvoYKoEOLS6hHhT140D6ScygCJAKh4voQYMIu1FI60bbzZlvd8Xo_67KhksGyfGJTA31EAV87jv5rSyTh-whXFnQKhbrlp9NlbCu02-M20uvW_9ixf0pypobQ0dP3jOA_ffifkINmkF_pPpEIVti2p-YugGcC1faRPEdAuqIji_H9CfsaYyuz9Cy-OmciSOGhtv1mH7TzjGj_WYyLy1juQkCmvWvnyOHZUTXOXRRNh338ZDy34pt80zjwZGMrotAjqBcN4MqTPy90V3591AMlBDactpL4YsQ9hHun9ZsZ5T0utFTuKP2otRkIEv4KYw_TwYEeaeRnEbgLuKBKhztv17vhh36_iUeG62enIw1dY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69065e0edc.mp4?token=FwA8OBdAvOfJQRmRTfW5cEwm-3pZAFpiGJgUaXupQL5pLB_EL0PKIY7e0NmQwk_itccatqqzVsoyQbI8kJVZ3VoAa0x-_ckE5MX4I-bJTOEwRIlSxLCxFMbli4pbLcrxYwXQMUKnW4mU6zBaFGehc1AQveLwHSj_QAgU7-NCMp0SiAdKm3hM42bQGTLisNVDsPm9opFeYU8kDWeMVF5xK0C6-c9KCPoiZ5oIgwdCTO9hcdm_wWLaQpIrHjNlgmCr1vePipT_A3qh_Em9joK9ovvTZ0xSBhbEH_wcHu9KRyfJ9V0d1FrhFtOuKMHJHX8C1JvoYKoEOLS6hHhT140D6ScygCJAKh4voQYMIu1FI60bbzZlvd8Xo_67KhksGyfGJTA31EAV87jv5rSyTh-whXFnQKhbrlp9NlbCu02-M20uvW_9ixf0pypobQ0dP3jOA_ffifkINmkF_pPpEIVti2p-YugGcC1faRPEdAuqIji_H9CfsaYyuz9Cy-OmciSOGhtv1mH7TzjGj_WYyLy1juQkCmvWvnyOHZUTXOXRRNh338ZDy34pt80zjwZGMrotAjqBcN4MqTPy90V3591AMlBDactpL4YsQ9hHun9ZsZ5T0utFTuKP2otRkIEv4KYw_TwYEeaeRnEbgLuKBKhztv17vhh36_iUeG62enIw1dY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اخبار کشتی را از دور پیگیری می‌کنم اما بخواهم درباره‌اش حرف بزنم به پراکنده‌گویی می‌رسد | اول و آخر ورزش ایران کشتی است
مشروح گفتگوی خبرفوری با عباس جدیدی را اینجا بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3223561</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/661175" target="_blank">📅 21:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661174">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نظم عجیب و شورانگیز عزاداری یزدی‌ها در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/661174" target="_blank">📅 21:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661173">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ان‌بی‌سی: ترامپ خواستار موافقت اسرائیل با آتش بس با حزب الله شد
🔹
ترامپ امروز با طرف اسرائیلی صحبت کرد و خواستار موافقت آن با آتش بس با حزب الله شد.
🔹
ترامپ در گفت‌وگو با ان‌بی‌سی: من همواره رفتار خوبی با نتانیاهو داشته ام، او گاهی باید آرامش خود را حفظ کند و از عقل بهره بگیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/661173" target="_blank">📅 20:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661172">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geDjnP454EF9-8PEeUVy5mHz_9zmTRvzCs941CMni6NmRQ7LBKCy-ZcwEg8YA4ne25zP-o-5-v1_b8v54mWXrSJihAmeEkaYPGxC_VumJcfCMqGGfbOxF57Ti_aJMA0v94AGoEmE8NICT0o2ejADSWUEVxswplI1tvoizBk58J96O-b5hRypGpyn-Fjx-gOuUDFBCwqyC8LY52pK7eP7iiYjPbL1JO88L134hdhaxVV0Vhea-5wiLFxpMDvkNT-WfMGbhLGwuKq2_-jQbpqPUtZlT4sm1dUCCn_ky4wb9qWUjUxr5MjQS4tKdIjDPXkX3apgDot308n4OFpsQPs8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس‌جمهور: آمریکا باید بسیار مراقبت کند تا صلح قربانی شرارت ذاتی طرف سوم نشود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/661172" target="_blank">📅 20:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661169">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a70075c1.mp4?token=oBDy7nU_r89zHIGGkQ-bmMFGqfzL5SKh7_9oNipWoz4gZQLfPzVwBIgfvqd8C6PbiniAoemwucjY1V5KeVxtH-fscxqHx0-S7-xwivi7hIYPcLrbJq88xcc46D-NVNJb9Bqx2OCyPonOE7P7oKYXZEWQcPZ2eqF1VfSM-hr5IX1zG6F_HdudtquaqQkSO2rkWYNOnzFefOa0s54bTbpfiVf6Ewh8CKL6LbtghfpO5rH4ZQ_TWCuSH158mDTXOZp0Tmsj1tlRUbqpFpNjkNlCAKOIMi-EwpqpKkj-ucJSLXZoSHZkN1Qc7H9qfOon8qzpW9X_xnInFMjbwhELQw4IDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a70075c1.mp4?token=oBDy7nU_r89zHIGGkQ-bmMFGqfzL5SKh7_9oNipWoz4gZQLfPzVwBIgfvqd8C6PbiniAoemwucjY1V5KeVxtH-fscxqHx0-S7-xwivi7hIYPcLrbJq88xcc46D-NVNJb9Bqx2OCyPonOE7P7oKYXZEWQcPZ2eqF1VfSM-hr5IX1zG6F_HdudtquaqQkSO2rkWYNOnzFefOa0s54bTbpfiVf6Ewh8CKL6LbtghfpO5rH4ZQ_TWCuSH158mDTXOZp0Tmsj1tlRUbqpFpNjkNlCAKOIMi-EwpqpKkj-ucJSLXZoSHZkN1Qc7H9qfOon8qzpW9X_xnInFMjbwhELQw4IDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل ایالت می‌سی‌سی‌پی امریکا‌ را درنوردید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/661169" target="_blank">📅 20:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661168">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: تماس بین نتانیاهو و روبیو، وزیر خارجه، به زودی، درباره لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/661168" target="_blank">📅 20:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661167">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
نروژ استفاده از کالاهای تولید شهرک‌های صهیونی را ممنوع می‌کند
وزیر خارجه نروژ:
🔹
شهروندان و شرکت‌های نروژی نباید از فعالیت‌هایی که به ادامه فعالیت شهرک‌‌سازی غیرقانونی اسرائیل در فلسطین کمک می‌کند یا از آن حمایت می‌کند، استفاده کنند.
🔹
ما ممنوعیت داد و ستد کالاهایی را که در داخل شهرک‌های اشغالی در سرزمین‌های اشغالی فلسطین تولید می‌شوند، برای شهروندان و شرکت‌ها اعمال خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/661167" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661166">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای نواف سلام، نخست وزیر لبنان: هرگز بر سر حتی یک وجب از خاک لبنان سازش نخواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/661166" target="_blank">📅 20:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661165">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
آیت الله علم الهدی: نقد و بحث کردن هیچ ایرادی ندارد؛ اما ما حق رویارویی با دولت و وزرای دولت را نداریم چراکه مثلاً با وزیر خارجه نظام جمهوری اسلامی ایران برخورد کردن، به مثابه برخورد با خود نظام است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/661165" target="_blank">📅 20:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661164">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای مشاور نتانیاهو: اسرائیل تا زمانی که لازم باشد نیروهایش را در لبنان نگه می‌دارد
ادعای مشاور دفتر نخست‌وزیر اسرائیل:
🔹
نیروهای اسرائیلی تا زمانی که منافع اسرائیل ایجاب کند، در جنوب لبنان باقی خواهند ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/661164" target="_blank">📅 20:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661163">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Br6O8VpSsHyNv9PKE0mwVwoOe9PMF-dKXfh2TjS70bYNVtlDfdEpaAvtRYEm8pyfWu6rRny0G_pQv8LAU_AGBeW8_jEGJSlgzzQ8_1aKqDDjltDS1HDTGozhhCPKIHLfnW9ZaXIIgo6lLAykgeg3EW1OKjY7H1psHM9hypfzXhlXLIUUHCTsYiCm9TeaTotQB04gAMLCZp90_SxMhbZCMpzRuCsfmcxlx_e_CvXY81Viqw6RUs6MqqNQaCdjfzAOmmBaVnuvhMABPyJp_k0uJd-KG_HMS1v2b4Nvc6oKGJ1bIsM1O0D0bEmSSqOvNllIR52OoVz63z_2L_xZHKfAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باراک راوید: حضور هیات قطری در سوییس؛ بدون حضور ایران و آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/661163" target="_blank">📅 20:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661160">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXUjjceHr3E0h_IBZDrqxgG8ibuErOSNbfLOUDy4mbxh__f5PRXHKV6nR4APCchNEDqR_LZ7Kx5FY27akei4NoyJHWwLWDxrxiSJ7SILuR2-6GJgs6irlp5LT89y1e9kjSO4pODvD3wAz6GRY0LffEuxxHKGo94JQ4Nx-9SCnMFJ80HbOQKmgugzOEJCN-cpBzCPg65t4WEEx0v2DGJtB9SxKCUxY-g9dmLIjBdW0aU-azEM7DZHV6TB7fhcoFVqUU3OMqKtp6ck5jNi26oGDV9yAvbusNwxqH-tHWW_iKmsMBg93CLKKDilBnHYKHebhIiQKl-LCdcaINtWgEnAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVP1DjfPCl6ucMIcQQbnmGSGxNggRFoWKYOIzBnbr3bxVyHDQgh04C_o4ma9VPQ0BPYEgkKaK6Z-G516_XSa7yJY0oXlmzIFqGIVPjkOHuOX735oJSN5mMEx93U2hd0CWdVf5TQcWdiIxp_tXLgFhleZOtMTNUBt5xKNH9356cKxELY10zVrUNaLlUbRp_2N1zqwVLhkxo7eTkZdPOMHJGtWbZdSGRAD3y5rWUsBZMACcvr_OXx0w55_fNXiOsCl9wG9KHw3uHQEBqVGqVB0qXnjazb1HQYqqOd-mVH_OlKkbLXXA1Lo8YU5bt7VGHWA8LDCNAk_e-nPXSgfOrE7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSKfskEiczIE0h9KfHiIfYVeXQ75iiVzLTkjXU-Z2Mru-cUlK80v7RT545MsEJlAHHFdXEUEmKKQfiW2ujqMQDhP6o2g9W_B5O1vynKqW-P372_CoEigng-WxxZUySjvIpq-8qwtGCTMPWZqTivQ0ZAEvJp0QW0ZneZ69n_QcvqxF4_eEBA42hjdvQXqYIkuRGIcbSp6BhXBFnuMyIU_t_pqTio9--QV_i14CDUzSi9keFPo3cnQk7rrlz3Vez20fbVZZi6BwCXPor1GjcIY1IJ8tesq6WydnNxQd3yQKJaB_OEUkEdeRotqXObPcTw8b8jY06gGXPgqihqSH0OdIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۶ اسموتی خوشمزه رژیمی
🧋
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/661160" target="_blank">📅 20:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661158">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMo_0yErWUO3ne59hX2zIFO_zFWtpTJsNgJajLJ5jRxB6qKBCc4LSb8BnQji42L6RUni9PPOS7U7AVru52ZlyJIIKGaN4vOSms-msjtmpUT6TVhO_bmduTnSAeVOX65bbVDqBg2Okpb09F8eygM8FQHdLEPzCvlIbyyTKJ3dnPkVKnCVynhCSd4BJ2Dl8SY6M1wSsaTWkvu01v_Omr57CDnzCPqrYHFM-vzkM7J5ysroe_HQT2wAsPRbcqPOxzRiHMS_PYbJDGev-lIJ03l6h-iNXhqhbE16rgW-io5Aft-X-dqHbgGKXQxK2ESzyhgBkcXREpZMRSFAb4M_uGy6SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت الله علم الهدی: نقد و بحث کردن هیچ ایرادی ندارد؛ اما ما حق رویارویی با دولت و وزرای دولت را نداریم چراکه مثلاً با وزیر خارجه نظام جمهوری اسلامی ایران برخورد کردن، به مثابه برخورد با خود نظام است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/661158" target="_blank">📅 20:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661157">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
حضور ۱۰۰ درصدی کارکنان ادارات هرمزگان از فردا
استانداری هرمزگان:
🔹
از فردا شنبه ۳۰ خرداد ماه ۱۴۰۵، ضمن تداوم فعالیت ادارات در ساعات ۷:۰۰ تا ۱۳:۰۰، تمامی کارکنان ملزم به حضور ۱۰۰ درصدی در محل کار خود هستند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/661157" target="_blank">📅 20:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661154">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ماجرای شهادت حضرت عبدالله بن حسن به روایت رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/661154" target="_blank">📅 19:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661153">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
واشنگتن پست: نتانیاهو در پی تضعیف تفاهم ایران و آمریکاست
🔹
مقامات اطلاعاتی آمریکا هشدار داده‌اند که (رژیم) اسرائیل احتمالاً در پی تضعیف تفاهم صلح ایران و آمریکاست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/661153" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661152">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMKj8R3RoikmnjBWplLIYZoa0m-v6kzuZY4A2HMKmRdbpP1964Ta6JQ5BGjXeGTGX0xb-nmf0N6UO88OakRK1uRwNTIt7NzhwMH0AYBS_jpUydj0RNHA1yoTdWxp1gO7Ofmrksxne9XJItxMEX4r4F5He0rmQjPOqVRc6R2I-PBnOoLENcriXZUQdcQNpfRM6l3sY_gqtFNB6Ya-XoWbrP7qWMl5IMUoHK-0Gg_nMcYnujORAJRtSPUXnA94VNutiDhestR8aKX9xi3mP2vFbcbpowwBDFRbnjm4DY38c3TPsBjChg3rtB-DRY6qsn5QnVdUtxwnP9VmLkLKeuJLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس نظرسنجی مؤسسه کانتار (Kantar)، میزان محبوبیت ترامپ در اسرائیل طی سه هفته گذشته با یک چرخش دراماتیک همراه بوده و از ۲۳+ به ۲۳- رسیده است.
@amarfact</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/661152" target="_blank">📅 19:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661151">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کمیسیون امنیت ملی: تحقق کامل شروط رهبری در تفاهم را تا انتها پیگیری می‌کنیم
بیانیه کمیسیون امنیت ملی مجلس:
🔹
ضمن بی‌اعتمادی مطلق به دشمنان، «یادداشت تفاهم اسلام‌آباد» را ترسیم نقشه جدید امنیت منطقه‌ای و بین‌المللی دانسته و از حیث وظیفه نظارتی مجلس با دقت تحقق کامل شروط رهبری معظم را تا انتها پیگیری و مطالبه خواهیم کرد.
🔹
ما معتقدیم استمرار این پیروزی‌ها، تنها در سایه وحدت و انسجام ملی محقق خواهد شد.
🔹
این کمیسیون در بررسی تفاهم‌نامه اخیر، رهنمودهای مقام معظم رهبری را فصل‌الخطاب و نصب‌العین خود قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/661151" target="_blank">📅 19:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661150">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f12180799.mp4?token=vPvw2pijMV7fkYhOgI-HY9TVq97xeh1bTG7k9hArvKymVaR9MwuUMotaux2rO8f4hIGmrWDonXPqYvYYN3ISd3KY23p-8B4zs0BtMk-L0qqzKE0HYyj1h3POoNv6XfgoMj4EmJsBXipykSoymRU-PAlSKVHwXeMIAuu3EHlBj-vztG59p2z8MtWoFxl6qEKrf_KZqdgZBWlYBk2Xf2_GAcxcmPFaYof5dIYLOBtYMDW2Z_DVNZ-jRVyTug7VZQH-oYfMqx8SmhOC9CGKEmuKpB68FBjeCuBiVJs8GEe_wnyiVLUGkZo2EibQXBsQzAM9AI0dLK6YTpaaW4RXoZVmRE8FOkVIz365jGWxDcJuME9gilmN2eB_P2qpjRq__BsRKBzVa1HXjsIvOUfRiCU9q65YlhHZuu6drAkeC8tN2iETECKKvz9wAdf45iO1dFlyeydLEJZOeOhBKcuyDj-SsGyCq7TY2W8_Lgl3ZaIEQYGYLGCisHEWdSDvj_yjNIP4dzZsi1TnltdL7iDZ6wcld6qaF52xEPQnKoAO86evAXC0-mDidzs-Tcjx3f6n6oTPSnI-IVE24zw0DWQDHGwsWWUCSCt3AwEDFBu_3mmEttxidX27Iysu21cSgK_ezzBIg4v5CVR0BSK9A9mNb42Ubv85nhBbuJ7k1I7ZWryRM9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f12180799.mp4?token=vPvw2pijMV7fkYhOgI-HY9TVq97xeh1bTG7k9hArvKymVaR9MwuUMotaux2rO8f4hIGmrWDonXPqYvYYN3ISd3KY23p-8B4zs0BtMk-L0qqzKE0HYyj1h3POoNv6XfgoMj4EmJsBXipykSoymRU-PAlSKVHwXeMIAuu3EHlBj-vztG59p2z8MtWoFxl6qEKrf_KZqdgZBWlYBk2Xf2_GAcxcmPFaYof5dIYLOBtYMDW2Z_DVNZ-jRVyTug7VZQH-oYfMqx8SmhOC9CGKEmuKpB68FBjeCuBiVJs8GEe_wnyiVLUGkZo2EibQXBsQzAM9AI0dLK6YTpaaW4RXoZVmRE8FOkVIz365jGWxDcJuME9gilmN2eB_P2qpjRq__BsRKBzVa1HXjsIvOUfRiCU9q65YlhHZuu6drAkeC8tN2iETECKKvz9wAdf45iO1dFlyeydLEJZOeOhBKcuyDj-SsGyCq7TY2W8_Lgl3ZaIEQYGYLGCisHEWdSDvj_yjNIP4dzZsi1TnltdL7iDZ6wcld6qaF52xEPQnKoAO86evAXC0-mDidzs-Tcjx3f6n6oTPSnI-IVE24zw0DWQDHGwsWWUCSCt3AwEDFBu_3mmEttxidX27Iysu21cSgK_ezzBIg4v5CVR0BSK9A9mNb42Ubv85nhBbuJ7k1I7ZWryRM9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش سوزی جنگلی در شهر اسپوکن در واشنگتن
🔹
آتش‌سوزی جنگلی در شهر اسپوکن در واشنگتن، دست‌کم ۱۲ خانه را تخریب کرده است.
🔹
مقامات آمریکایی اعلام کردند که بقایای احتمالی انسانی در یک اقامتگاه سوخته را کشف کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/661150" target="_blank">📅 19:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661149">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbf1zsHUoqDKoHjka71849RITc-PAgzz8sK4E26mlOOrhKCWhglB8LC3B0BQLPLZ-R4Rt5MRJFW_3xPoKQrR7H9l5kYHZeUOE2yzbGQi8zVAfsWbMYoNi20nVXgd0KJPB2ZyL-jEBD9WVL0C4UtlpgEXyWl449cuwklSZdojo9yLVnHhbqra7wac43qqi4yvT9uHvDFYmsFW-X4jh9e0L5PKkEEoHlG_2a7LzzYLvQcrO0KG1Wing2F08yLOLknDgVPwEJUl-gnKIXG5FQZTojPIU50V7fNgoe7XFGq2NIE-5xKe4MXt35FpTc6O92fZ7yK0uZbJsoDZ2zyRJbdWZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک صنعت و معدن در روزهای جنگ رمضان در کنار تولید ایستاد
اعطای تسهیلات برای حفظ تولید، اشتغال و تأمین نیازهای ضروری کشور
:
🔹
۲۰ همت تسهیلات پرداختی به واحدهای تولیدی و صنعتی کشور
🔹
۴همت تأمین مالی تولیدکنندگان کالاهای اساسی و صنایع دارویی
🔹
۱.۴همت تسهیلات پرداختی در دوران جنگ ۱۲ روزه
🔹
۴۰روز تداوم تأمین مالی تولید در دوران بحران
دستاوردهای اصلی:
🔹
حفظ پایداری تولید و اشتغال کشور
تأمین دارو و کالاهای اساسی بازار
حمایت از صنایع راهبردی و زنجیره تأمین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/661149" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661148">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa784dbea.mp4?token=fi9S0sJqYHPX76Hrr3nND89eT3MfuujCAwTxraTIC7UTGsha_9aZghsC5BPIpfy9MyN3A0vBTyZy8Solq9fgzRmdYoLBIVEO7WqFK1O5RYP9qf5oVbzSMuTtSKYbPg9LqdWmnZ2iNPdDQfbEmbolmh8WSLvS7LiNut3QYspyK7KZWz-4SbWb-4T16n81y_w8TtvYC8Tx9Ge3ndPuJAH1ZCSfAHwjljSpryqpi2tKw-4Ycbts3LB3OaukWAC1x6_XzeVAbYG8HSaqF7GDsvlKe4XWG1-cbwlMXxbP7lkfThtbuBqe5C4DvnUiTBSSJXcR3M5gpyaaRE6DSHVnSouWFY77ZuLTwbWWpsU7q-KlEZHIGIjeQGlbGBYMRowQg5S3Ud2EmHeobO3s1mJM6vOHF4I2b2IRUwCQMiZunK4FqYYFUdodI2tcW0hhDdg2JN0iQC6r-9hyWS9Vny_dltQjpOfnuEvl9b9OGwArzfVsUoT5icdTblz0dCQet0cUXJJ8eb6e31LlrUvm7iLbLuzKFmu0jC8TQmruTc2bEQ5TnxrSMWdvEA4PTjoRTNdCbIgTBq8yd8fhsmlfVIaDJTmlroeNSRrHQWZX6If0triT-ezymQfXFM4MaCgLoXS6l_nxkfYKpZn6_AtXq6heK4Cg688hbG2JoVyUIZYl_MDhKF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa784dbea.mp4?token=fi9S0sJqYHPX76Hrr3nND89eT3MfuujCAwTxraTIC7UTGsha_9aZghsC5BPIpfy9MyN3A0vBTyZy8Solq9fgzRmdYoLBIVEO7WqFK1O5RYP9qf5oVbzSMuTtSKYbPg9LqdWmnZ2iNPdDQfbEmbolmh8WSLvS7LiNut3QYspyK7KZWz-4SbWb-4T16n81y_w8TtvYC8Tx9Ge3ndPuJAH1ZCSfAHwjljSpryqpi2tKw-4Ycbts3LB3OaukWAC1x6_XzeVAbYG8HSaqF7GDsvlKe4XWG1-cbwlMXxbP7lkfThtbuBqe5C4DvnUiTBSSJXcR3M5gpyaaRE6DSHVnSouWFY77ZuLTwbWWpsU7q-KlEZHIGIjeQGlbGBYMRowQg5S3Ud2EmHeobO3s1mJM6vOHF4I2b2IRUwCQMiZunK4FqYYFUdodI2tcW0hhDdg2JN0iQC6r-9hyWS9Vny_dltQjpOfnuEvl9b9OGwArzfVsUoT5icdTblz0dCQet0cUXJJ8eb6e31LlrUvm7iLbLuzKFmu0jC8TQmruTc2bEQ5TnxrSMWdvEA4PTjoRTNdCbIgTBq8yd8fhsmlfVIaDJTmlroeNSRrHQWZX6If0triT-ezymQfXFM4MaCgLoXS6l_nxkfYKpZn6_AtXq6heK4Cg688hbG2JoVyUIZYl_MDhKF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: هرگاه دشمن با سلاح با ما روبرو شود، ما نیز با سلاح با او مقابله می‌کنیم
🔹
ما از مرگ نمی‌هراسیم و این، بخشی جدایی‌ناپذیر از پیروزی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/661148" target="_blank">📅 19:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661147">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: هرگاه دشمن با سلاح با ما روبرو شود، ما نیز با سلاح با او مقابله می‌کنیم
🔹
ما از مرگ نمی‌هراسیم و این، بخشی جدایی‌ناپذیر از پیروزی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/661147" target="_blank">📅 19:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661146">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
♦️
عراقچی در گفت‌وگو با وزیرخارجهٔ پاکستان: هرگونه نقض تعهدات مندرج در تفاهم متوجه آمریکا خواهد بود
🔹
آمریکا برای پایان‌دادن به جنگ در تمامی جبهه‌ها، از جمله لبنان تعهد داده و در قبال آن مسئولیت دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/661146" target="_blank">📅 19:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661145">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8cd3c6352.mp4?token=M3IRqnhYZFfBtHv-tB-R7EM68SdLhtuteQ8goZDf8xdG5xreXgMHSgFVPrfeiScvN8MOilMBZLi-hHBp3NAoZjYnwogyZRlKhmBY8NWDEHz4VnTXENCf_0WgxboRHdzQwU3i-lIzbpvD6VRq5ZD54GLD_NYYXAXBbQl1sKRtrzdBohEynsLJLkL5ZY5HDlIhZkifUFtNvvi4sEpbauEtC3e39NSY67S2jyqiex-LtjeH7lPH3w8TJilFx5e92FypOTN7hJKQP64crCZ-yWsfjATYdPPZy9cfrpeDzJRgX4y2DUHLVg0mXMqVkR3RJtkCC6REbYKfRUC4SXV1lBp8dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8cd3c6352.mp4?token=M3IRqnhYZFfBtHv-tB-R7EM68SdLhtuteQ8goZDf8xdG5xreXgMHSgFVPrfeiScvN8MOilMBZLi-hHBp3NAoZjYnwogyZRlKhmBY8NWDEHz4VnTXENCf_0WgxboRHdzQwU3i-lIzbpvD6VRq5ZD54GLD_NYYXAXBbQl1sKRtrzdBohEynsLJLkL5ZY5HDlIhZkifUFtNvvi4sEpbauEtC3e39NSY67S2jyqiex-LtjeH7lPH3w8TJilFx5e92FypOTN7hJKQP64crCZ-yWsfjATYdPPZy9cfrpeDzJRgX4y2DUHLVg0mXMqVkR3RJtkCC6REbYKfRUC4SXV1lBp8dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
رفاقت دیرینه عباس جدیدی با منصور پورحیدری و ماجرای آن عکس جنجالی!
مشروح گفتگوی خبرفوری با عباس جدیدی را اینجا بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3223561</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/661145" target="_blank">📅 19:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661144">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای
سنتکام: بیش از ۲۰ کشتی روز گذشته با امنیت از مسیر تعیین‌شده در تنگه هرمز عبور کردند
🔹
از کشتی‌ها می‌خواهیم دستورالعمل‌های مرکز اطلاعات دریایی مشترک را رعایت کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/661144" target="_blank">📅 18:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661143">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjI-eFKPURQ0jBGCm0unuQ-6HxXryX3I9cIDQGeE2D-6XKhzoyf8-GtnV8XKGKPIpF6ZkvMYXWA8QVtYfh-oiLlMDnCqYpjROSt4kbkYDYWMwbGUnARTG1UpZP2n524mqZqVORC6TX7xqJQLLuIDmfUj0HZ_c94VXh_YaE950RkFCkCoZpk0iTmtrsneeHQzo0q6ChXSYA8_fSDAxIKdOyXtc4eop8j1cGshexvNEmS42MtM7HO4yiAMtA-mAWcfHcsZdqSZEVwwP9kXwDunhJXdgREWXv0TSR3wMcHLhGsd8TP1JP0x1ZBBltLYybnc0wpccA42o6JHeag05zxPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/661143" target="_blank">📅 18:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661142">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
شکایت ایران به فیفا از محدودیت‌های سفر در جام جهانی
فدراسیون فوتبال ایران:
🔹
درخواست ورود تیم ملی به آمریکا دو روز قبل از بازی با بلژیک از سوی میزبان پذیرفته نشده و این موضوع روند آماده‌سازی تیم را مختل کرده است؛ به همین دلیل ایران به فیفا شکایت کرده است.
🔹
رسانه‌هایی مانند فرانس۲۴، بی‌بی‌سی و گاردین نیز گزارش دادند ایران به‌دلیل محدودیت‌های سفر اعمال‌شده از سوی آمریکا، میزبانی جام جهانی را به چالش کشیده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/661142" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661141">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
پنتاگون درخواست بودجه از کنگره کرد
🔹
پنتاگون رسماً به کنگره اطلاع داد که برای پوشش هزینه‌های مرتبط با جنگ علیه ایران و غیره باید ۸۰ میلیارد دلار اختصاص دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/661141" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661140">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
نشست چهار کشور میانجی تفاهم ایران و آمریکا در مصر
سی‌بی‌اس:
🔹
چهار کشور میانجی تفاهم ایران و آمریکا یکشنبه آینده در مصر دیدار می‌کنند.
🔹
وزارت خارجه پاکستان اعلام کرد وزرای خارجه پاکستان، عربستان، ترکیه و مصر در این نشست درباره تحولات منطقه و مسائل مرتبط با صلح، امنیت و ثبات گفت‌وگو خواهند کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/661140" target="_blank">📅 18:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661139">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTy1XCru0l-0mRhoMQfdfbpE-fY7Oabuhm-fdgcpMQBG6UGaTyIt72PDTpqz4QGJwiWyTAkzvVMEmJ1bBnAZuWKh2cIKMd_Wh4NWqLKJAJrVkti-dBxAEdxsbZUahKbySqJ4Ki6cDOh9qMYSFFOPJ4lWblnKdZZwaOT65yds0Cb8NKSRqRv9b5v3LprJaKcayu3Ehy9gPoVK57fNvhM8MGYlZ963EfK94UIy35ijlJmvqLC7lJQiA1OQ_GkJuHWz8Ej1UZO6jzO0rNqqPh1IxXeXAZFW2yLoVV7K71eoijk3MgNkhUWczkyhq5H8yrnGBBG7NR9lJkIgNjyyz90vfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام فیفا؛ مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی شناخته شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/661139" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661138">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d0224262.mp4?token=gZ9-EX7XeRLAxrfPdEloSGD_GF62kCclTqUrb3CruUUoxnj5XafiqkYZpgL03uIsqqdLlgR628v_n24zfmMeJtSb1pgPO0XzaUaq-9zPjybAWe38abInVSBGMz2EDRxPG-sB2R7R1Bl9F-yU4SkeybvECSxM7EdVZ2URn9PkTSDELq-1iPdkVkstjlntV5f1c_0GriXd81O0itc-frcjGm9n0B_IttMqcicwWvZ_hTNWvGoxvW81kyipAHChh-F2L7Y_lHtshCHlasKMa8JQKkeVO3vzaPTzPOETloQ4RwWx7GzoHTerg4TOnPUIZXAow69R0jmUGE3dAlKm4MpkTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d0224262.mp4?token=gZ9-EX7XeRLAxrfPdEloSGD_GF62kCclTqUrb3CruUUoxnj5XafiqkYZpgL03uIsqqdLlgR628v_n24zfmMeJtSb1pgPO0XzaUaq-9zPjybAWe38abInVSBGMz2EDRxPG-sB2R7R1Bl9F-yU4SkeybvECSxM7EdVZ2URn9PkTSDELq-1iPdkVkstjlntV5f1c_0GriXd81O0itc-frcjGm9n0B_IttMqcicwWvZ_hTNWvGoxvW81kyipAHChh-F2L7Y_lHtshCHlasKMa8JQKkeVO3vzaPTzPOETloQ4RwWx7GzoHTerg4TOnPUIZXAow69R0jmUGE3dAlKm4MpkTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت خوب سد کرج ۲۸ خرداد ۱۴۰۵
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/661138" target="_blank">📅 18:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661137">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GytfPG_QwnzbwrLWf3Fnik-V5__aBJCcjVUpKWigrIgFo-jFaJP7j5eQjGK8iuabp4J3fef2k-Q240eNg1dt9UR1urnfIzuSHlioSlK2mI6Y5WwpcsUSNM85eJ3N3cCyNgBql_1dZzZlLKoTYKIjjHKo00oKz2IH06rGpAMfPjpyMPWw26GqN9fPb8M4cLiZqna-mh_tGTmPt-i-jXFzyT3vguI2UOJQkOCyHbzVRYQMGYLr5pUFu7VMUSHldlH4VbbACt9ZQfFl0RZnRdvpnf0hN4xR97rEk9weuy3kPAICSJ8fbXfnX4qgz8mqx8EIHAl2vyI1BpSi-eV_4MA2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
رویترز: ایران سلول‌های مخفی جدیدی در عراق برای حملات منطقه‌ای ایجاد کرد
رویترز به نقل از ۸ منبع عراقی:
🔹
سپاه پاسداران چند سلول مخفی کوچک در عراق تشکیل داده که مستقیماً زیر نظر آن فعالیت می‌کنند.
🔹
این واحدها انجام به چند حمله پهپادی علیه اهدافی در کویت، عربستان و امارات هستند. هدف این اقدام حفظ نفوذ منطقه‌ای ایران و کاهش ریسک برای گروه‌های نیابتی شناخته‌شده عنوان شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/661137" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661136">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlBxt5MyyjNYehCPP7JumJUO9BIao94TYtBEZYK3UdjrQAWlR9zKNITkj5e9nipvs5-ujraeIkTIuZCHSKp3-PrvuO4uhTQsoT7Hi55eq3yYAutbIL8OR2cRQOU66TSnBl30g81SGe-6EsiLBvSuZgxebgjkLwdY5hmpU_tyaoinDFnF7Ewt3fT8loRCyjdh9anDgLl4fG-9Tw1NG3XmaIuIWzTRMBk1iQbiqthFUP414TMKpImlF5M2ZAcIg9CxKn8yZ7P0UQ2eHDfgLq4Lxz-1GmyYrotFtloclM26jI5-gRzMJ_OodE5hBzJNdeNsabs8x3ko6qMEXzGvuD9znA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکستن طلسم ۳۰ ساله بوکس ایران در جام جهانی
🔹
مهدی حبیبی‌نژاد با شکست نماینده انگلیس مدال برنز خود را قطعی کرد و طلسم ۳۰ ساله بوکس ایران در این مسابقات را شکست.
🔹
او فردا در مرحله نیمه‌ نهایی به مصاف نماینده آمریکا می‌رود.
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/661136" target="_blank">📅 18:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661135">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wra60tGQ5eS8Ym-zPUSCfrPplYwBpkTWrDAVLpXjALwsd7k_3x5Ic8kv3X_1A2LFMni-kpHFx7lv_mGtt07l2CuoV4LLqOzO6NJ6E80iuSExRxWZ57NH0MXD_e2uTd_0n6HHLPZCZjS29X-zFMXl6rC5hwCBJsk83mLrQMUlrjA2aK4CkgkI-jhVquYWDyT7bDV1A9F25WRMRWlGMSq6qrq4JsYD9g7jRAWGRPqRnk-xrS5lF5Rde49AYPYqLtvvjbPOxWNgqY8wUZuKKNGrtCtpK1Dz92qiUCTLZAdaENKs0lcPWKR0hgf4Kft86Cslv91jVf_ugxs7qKRpESMIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«۶۰ روز سخت» پیش روی ایران و آمریکا/ این ۴ مساله توافق را به جنگ تبدیل می کند
🔹
رفت و آمد کشتی ها در تنگه هرمز، نزدیک بودن ناوهای آمریکایی به تنگه هرمز، رفت و آمد قایق های تندرو سپاه، رفت و آمد پهپادهای ایران و بالگردهای آمریکایی در نزدیکی آب های کشور و ... همه و همه می توانند احتمال درگیری تهران و واشنگتن در جنوب را بالا ببرند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3223563</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/661135" target="_blank">📅 18:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661134">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grikuFh94_zL2kp7qbaeMnBqRk3CMsHT5h3OhTC27ixdVNEx3u8oorHlQerYOoUaKv7UCBdFYYCo6XCaxlYxylSspVg8VvwCya30NXkAyc676SWh_o_HbeDXfLSmrGoUq6uB0j0Y3o_R0IbPhhJYwycMVKvAlt7nha90uwrjUk56fZbkqUDowSUDL_UsW7rQjyIE7q_MFOMPE-D_Ge_wbhEt4-2osL8hSYclzd2OfBSpi930u2lf5eJBzmsrjFxEM2zDvePv5FIN9dTqkWH1VCLu2m3dKyPyj-TxtZB1L6Ce419QMna_Ly0Wl9D9Wl1ZGpKKI2XgXuM3rD4rAp31_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/661134" target="_blank">📅 18:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
پشت پرده حضور تیم ملی در تیخوانا از زبان سفیر ایران در مکزیک
🔹
ابوالفضل پسندیده سفیر ایران در مکزیک در گفتگو با خبرفوری به جزئیات وضعیت کمپ تیم ملی پرداخت.
خبرهای جام‌جهانی را اینجا هر لحظه دنبال کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/661130" target="_blank">📅 17:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تکذیب ادعای بسته‌شدن تنگه هرمز
🔹
سخنگوی وزارت امور خارجه ادعای برخی رسانه‌ها درباره بسته‌شدن تنگه هرمز را بی‌اساس خواند.
🔹
بقائی تأکید کرد نیروهای مسلح ایران طبق یادداشت تفاهم ۲۸ خرداد ۱۴۰۵ تدابیر لازم برای تردد ایمن کشتی‌های تجاری را اتخاذ کرده‌اند و کشتیرانی…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/661129" target="_blank">📅 17:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661127">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
نورالدین الدغیر خبرنگار الجزیره در تهران: آغاز استفاده ایران از منابع مالی مسدود شده
🔹
با شروع اجرای یادداشت تفاهم ایران و امریکا، منابع می‌گویند که ایران تقریباً شروع به استفاده از دارایی‌های مسدودشدهٔ خود کرده است که بر اساس سازوکاری است که میانجی‌گران ارائه داده‌اند.
🔹
روش استفاده و انتقال وجوه در قالب یک خط اعتباری باز تعیین شده است که به ایران اختیار تصرف در آن را می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/661127" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661126">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: نشست امروز جمعه در سوئیس، به روز دیگری موکول شد‌  سخنگوی وزارت امور خارجه:
🔹
رایزنی‌ها از طریق میانجی‌ها برای آغاز مذاکرات تدوین توافق نهایی در حال انجام است و در صورت فراهم شدن شرایط، اطلاع‌رسانی خواهد شد.
🔹
وی تأکید کرد طبق یادداشت تفاهم،…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/661126" target="_blank">📅 17:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: نشست امروز جمعه در سوئیس، به روز دیگری موکول شد‌
سخنگوی وزارت امور خارجه:
🔹
رایزنی‌ها از طریق میانجی‌ها برای آغاز مذاکرات تدوین توافق نهایی در حال انجام است و در صورت فراهم شدن شرایط، اطلاع‌رسانی خواهد شد.
🔹
وی تأکید کرد طبق یادداشت تفاهم، شروع مذاکرات منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است و با توجه به امضای دیجیتالی تفاهم‌نامه در بامداد ۲۸ خرداد، نشست سوئیس فوریت ندارد اما برای برگزاری آن در روزهای آینده برنامه‌ریزی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/661125" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

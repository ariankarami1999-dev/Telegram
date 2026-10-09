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
<img src="https://cdn4.telesco.pe/file/OLMWOmT61ifEBAgg6XRovOS1ior4sJhXzS7JPOyS5lOuUEthIkorQRlnIXcLF3cQMyPc_HOqi3HsFqQjvtIO8d1uxmPnTuXRwRFFXZ0W2zIKAHammhNoiljNpa1FC2cjqnEuNAwZ5I9xPHOoIAzOtHE0pkEA1qrGes5xRzEDIRnksrRBwLSLqBb3hK01I6Xgqocr-QBFaflIqSu8GFk5LpwN5Jr_mxQOw76enTEN-2noy8L92MtLBIP9diigMBdjifliKWRaqobunCikON0MMuiTKK1har911EvBNeqdVclWd7NjA_qQWr3cNzuO6X3-k7HLcMOIaF4EBp_ms9tzpA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 491K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
<hr>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">علیرضا بیرانوند پس از اتفاقات روز گذشته و درگیری لفظی با مدیران باشگاه تراکتور، امروز در اردوی این تیم پیش از اعزام به عمان در هتل حاضر شد اما در اقدامی جالب مدیران باشگاه تراکتور او را از اردوی تراکتور
اخراج کردند.
@WarRoom
👃</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/withyashar/25304" target="_blank">📅 23:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیویورک‌تایمز گزارش داد کاخ سفید سمت سخنگویی را به کیتی زکریا، مفسر محافظه‌کار و مشاور ارتباطات نزدیک به دونالد ترامپ، پیشنهاد کرده است. او پیش‌تر نیز برای مدتی سخنگوی وزارت امنیت داخلی آمریکا بود. در صورت نهایی‌شدن این انتصاب، زکریا جایگزین کارولین لیویت…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/withyashar/25303" target="_blank">📅 23:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: به‌تازگی گفت‌وگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که در جریان آن توافق شد روسیه فوراً بیش از ۳۰۰ هزار تن سوخت دیزل به بازار آمریکا و بازار جهانی عرضه کند. همچنین، ۵۰۰ هزار تن دیگر در طول ماه نوامبر و یک میلیون تن دیگر بلافاصله…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/25302" target="_blank">📅 23:15 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شرق هم چنان گزارش سر و صدا میاد واسم
@WarRoom</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/25301" target="_blank">📅 23:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سلامتی همگی</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/25300" target="_blank">📅 22:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhcsMHD5mgj-pzJFeeXr4Ih4JIo4OE3aknNgxbsJ40Gk_3JPcand3NXRL-r7TMxSpxDvoXGjim8rzfxg9xzxVJ5e4c_1DqMf0c90xRmfCRk7LRuFe5lRgSW9fiv4Jxsap4TSeWLJgMogDEoAvBlQbaHnrrUJQBv_J2s85ksnPYJaWzGqTmx0HoXdKeK4CU1fH1Nx7LTtPvYwRrqmFTUpp9Y4SS5nkuMPMmZUVLsFizuZbUJCzsOsQgRHqlQKZ1bZg4LBBD9TKh4h7EFcHFYoKyvFzLzE51vIQyxafpu9tOVniHmxccvhfvoii9eg1_EK0M4NNMxvNEERjQ6gjKUXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به‌تازگی گفت‌وگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که در جریان آن توافق شد روسیه فوراً بیش از ۳۰۰ هزار تن سوخت دیزل به بازار آمریکا و بازار جهانی عرضه کند. همچنین، ۵۰۰ هزار تن دیگر در طول ماه نوامبر و یک میلیون تن دیگر بلافاصله پس از آن تحویل داده خواهد شد. علاوه بر این، با توجه به وضعیت پالایشگاه‌های دیزل روسیه، این کشور در مدت کوتاهی پس از آن، ۳ میلیون تن سوخت دیزل دیگر نیز عرضه خواهد کرد. با توجه به کنترل کامل ما بر تنگه هرمز و این خبر بزرگ درباره تأمین انرژی از روسیه، قیمت گازوئیل برای آمریکایی‌ها و در واقع برای سراسر جهان، به‌سرعت و با کاهشی بی‌سابقه پایین خواهد آمد! پایین آوردن قیمت‌ها برای مردم آمریکا، به‌ویژه کشاورزان، دامداران و رانندگان کامیون، بزرگ‌ترین اولویت من است. این خبر بسیار مهم و بزرگی است. همچنین باید روشن باشد که ایران به سلاح هسته‌ای دست پیدا نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/25299" target="_blank">📅 22:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امشب مثل اینکه من باید جنگ راه بندازم</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/25298" target="_blank">📅 22:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اتاق جنگ با یاشار : ترابری ۲۴ ساعت پیش تا همین الانه الان ! دارن پرررر میان (عرزشی هستی نبین سکته میکنی) فقط آخرش که مال همین چند ساعته یکی از‌ زیبا ترین پل های هوایی شکل میگیره @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/25297" target="_blank">📅 22:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfsvHWhH6HTrrXa1az9ToeoDnXoTOjzLpjjaJd1rBxdObBuZo-IOcby7BDVnDposkT3wi2ctnA_J9kK0YoUojfWQzIQY1zmcPpJzYcN2eGyGV12VJ67JYuuepTgTTgI8lsjtFPn2F-ncK03vuTYOd9aQu1PmN045_VflzEHzd9eSlpOXrq1SoueUes7PVvThkP4i0IK6jiT5sj2wGyBTqMK6Y91r3ldwwPdnxzNmB8-WNBryA1pRpT7IT3BwD3pl5I6GpbNuXfD2i4RItgfxCUsYoHIwtqd8CSu0AkM1zdaP-vPbbXBTnAvXxYnTwulz-RsyQqqY1t-tAN5NZph40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز گزارش داد کاخ سفید سمت سخنگویی را به
کیتی زکریا
، مفسر محافظه‌کار و مشاور ارتباطات نزدیک به دونالد ترامپ، پیشنهاد کرده است. او پیش‌تر نیز برای مدتی سخنگوی وزارت امنیت داخلی آمریکا بود. در صورت نهایی‌شدن این انتصاب، زکریا جایگزین کارولین لیویت خواهد شد که در ماه اوت از سمت خود کناره‌گیری کرد. پذیرش نهایی پیشنهاد هنوز تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/25296" target="_blank">📅 22:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خلاصه پیغام های زیاد : تهرانپارس بین فلکه دوم و سوم انفجار شدید اومد آسمون رو دود گرفته و بعد صدای تیر اندازی شنیده شد! علت نامشخص ولی حمله هوایی نیست @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25295" target="_blank">📅 21:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">معاون وزیر خزانه‌داری آمریکا: بیش از ۱۵۰۰ فرد و نهاد مرتبط با ایران را تحریم کرده‌ایم
وزارت خزانه‌داری آمریکا دیروز هم ، تحریم‌های تازه‌ای علیه
۱۷ کشتی مرتبط با ناوگان پنهان نفتی ایران
اعلام کرد. هم‌زمان، وزارت خارجه آمریکا نیز ۱۰ نهاد، ۶ فرد و ۵ کشتی را هدف تحریم قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/25294" target="_blank">📅 21:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGia56Mryujy1Nvyz5nSSDhbcOIxZOhgUB5spM7r-QY8o8aI-90Mr8YRqXTmgaA3SaENlK7BrfK93DSBoijP-8HU-inhRYU_Ty3jwyskP-fjzAkruz4kb4jW4upkrlzwiRXerTXZ1jEPKFhHCejJYXIaffV7BEoHMVFarZ2FDQLuUkjomQnmBr86qkKsFNIVWQWdbYXVdYGO1Cda5CHpAyWrB7oQ9Sj6TqBLXlDdLtKPdo_69icgLwIssTwjbgQ31dK6Rdn_RAR6ABfRIuofb3jyrdj2sRO1Hjr7mSwM_wjGMqs-c01rIxyccD_Kq8XKLLLqbt-Ec8AxRt8gxvV4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تا ۹ اکتبر، نیروهای آمریکایی ۱۳۳ کشتی تجاری را برای رعایت محاصره تغییر مسیر داده‌اند.
یک بالگرد نیروی دریایی آمریکا از ناوشکن موشک‌انداز «یواس‌اس جان پل جونز» برخاست؛ ناوشکنی که در پشتیبانی از محاصره دریایی آمریکا علیه ایران فعالیت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/25293" target="_blank">📅 21:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bedb14bbb5.mp4?token=aTxrfLaHQZKwcdVyRVYR92tw3N0ajW6FeVgAG4ZF68fcEk1GoZ3bFjAwNLNNGC7u9zneKSicQDt3WBaSK0DnbCatJ21Ii-6oZtTGu1qom51n2nXeATQ5KCUDGta6oGi2UtpFbwIBJivXHmjFQU5DIzbXr6QjdUwPc1hBXwggGMvPBaNl9FZie0IdOdqBQoR1nqm7EYF1Zb19eF5XlyixAKzD68hqKa6Ua8cgpjIkKUi7WhlmqCgl1hpfxtL3BogafGFDhj4a54Ji-TjFvae03zFHdLjwsT6U8RqKCRzgMtVStJv5vH3btPUi4FY1MvR8COgoGuENLBvR6rcv-Bn1Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bedb14bbb5.mp4?token=aTxrfLaHQZKwcdVyRVYR92tw3N0ajW6FeVgAG4ZF68fcEk1GoZ3bFjAwNLNNGC7u9zneKSicQDt3WBaSK0DnbCatJ21Ii-6oZtTGu1qom51n2nXeATQ5KCUDGta6oGi2UtpFbwIBJivXHmjFQU5DIzbXr6QjdUwPc1hBXwggGMvPBaNl9FZie0IdOdqBQoR1nqm7EYF1Zb19eF5XlyixAKzD68hqKa6Ua8cgpjIkKUi7WhlmqCgl1hpfxtL3BogafGFDhj4a54Ji-TjFvae03zFHdLjwsT6U8RqKCRzgMtVStJv5vH3btPUi4FY1MvR8COgoGuENLBvR6rcv-Bn1Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سنتکام : به لطف نیروهای ما  که با موفقیت مین‌های دریایی را از مسیرهای اصلی تردد پاکسازی کرده‌اند، مسیرهای عبور آزاد از تنگه هرمز برای تمامی شناورهایی که تحریم‌های دریایی آمریکا علیه ایران را نقض نمی‌کنند، باز است؛ در نتیجه، هزاران شناور تجاری با ایمنی کامل از این تنگه عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/25292" target="_blank">📅 21:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنگوی ارتش اسرائیل: امروز جمعه، در حمله‌ای هوایی در منطقه مرزی سوریه و لبنان، یوسف علی الحسن کشته شد. به گفته ارتش اسرائیل، او با هدایت جمهوری اسلامی در حال برنامه‌ریزی حملات علیه نیروهای اسرائیلی در جنوب سوریه، از جمله با پهپادهای انفجاری و راکت، بوده است. ارتش اسرائیل مدعی شد این طرح‌ها خنثی شده‌اند و اعلام کرد به اقدام برای رفع تهدیدها ادامه می‌دهد و به توافق با لبنان پایبند است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/25291" target="_blank">📅 21:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انتقاد و تکذیب روایت تاریخی مارکو روبیو درباره جنگ‌های ایران و یونان باستان
مارکو روبیو، وزیر خارجه آمریکا، در سخنرانی خود در آتن، با اشاره به حمله خشایارشا به آتن در سال ۴۸۰ پیش از میلاد، تلاش کرد میان تاریخ یونان باستان و سیاست امروز آمریکا ارتباط برقرار کند.(تورج دریایی: ایران‌شناس برجسته و استاد تاریخ ایران باستان.)
می‌گوید این روایت بخشی از زمینه تاریخی جنگ‌های ایران و یونان را نادیده می‌گیرد؛ از جمله شورش ایونی‌ها و حمله یونانیان به سارد، مرکز مهم هخامنشیان، در سال ۴۹۸ پیش از میلاد. همچنین فتوحات اسکندر مقدونی و سقوط امپراتوری هخامنشی نشان می‌دهد که تاریخ این دو تمدن، برخلاف روایت یک‌طرفه از حمله ایران به یونان، مجموعه‌ای پیچیده از جنگ‌ها، لشکرکشی‌ها و رقابت‌های سیاسی بوده است.
آتش‌گرفتن آتن واقعیتی تاریخی است، اما استفاده از آن برای ترسیم تقابل تمدنی میان ایران و غرب امروز، نیازمند در نظر گرفتن تمام زمینه تاریخی است.
@WarRoom</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/25290" target="_blank">📅 21:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فرمانداری چابهار خبر واگذاری ۱۱۰ هکتار از اراضی این منطقه به افغانستان را تکذیب کرد. این شایعه پس از انتشار گزارش‌هایی درباره اختصاص زمین در بندر چابهار و منطقه آزاد برای سرمایه‌گذاری افغانستان مطرح شد. با این حال، تکذیب واگذاری زمین به معنای رد کامل موضوع اختصاص اراضی برای سرمایه‌گذاری نیست؛ چراکه اختصاص زمین برای اجرای پروژه‌های اقتصادی با واگذاری مالکیت یا انتقال اراضی به یک کشور دیگر تفاوت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/25289" target="_blank">📅 21:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سپاه تصاویری را منتشر کرد که نشان می‌دهد پهپادهای شاهد در جریان جنگ، به سمت کشتی ها پرتاب می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/25288" target="_blank">📅 21:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ایلان ماسک به اپراتورهای موبایل اعلان جنگ کرد!
اسپیس‌ایکس با توافقی ۸ میلیارد دلاری برای خرید فرکانس‌های رادیویی باند ۸۰۰ مگاهرتز، گام بزرگی برای رقابت با اپراتورهای موبایل برداشت. این شرکت همچنین مجوز استقرار ۱۵ هزار ماهواره نسل جدید برای ارائه اینترنت مستقیم به گوشی‌های معمولی را دریافت کرده است؛ طرحی که می‌تواند وابستگی کاربران به دکل‌های مخابراتی زمینی را کاهش دهد. البته انتقال کامل شبکه موبایل به فضا هنوز واقعیت ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/25287" target="_blank">📅 21:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a757bdbbc.mp4?token=ViEI_L6oj9VaALC34PsbxTx1584cXnLH_cjVj4dyp_Tewxcq-bg9aGDa97A4aR-dqPwrqZ0nWwx3ty80QjrYXs31Qymj_XQLtmRnuN-GDS-ua6-gjUrZOA3HmHCWh-Ix7reHQxqbqT4sT9aa6YNPv-Ir5RI1UasWqshiFOhKewrVIZ1w31jDRblyQyiPYzn6BXNyPQ8b_Xasp0SGdke4Du-I_qqT3-J7mIA44cjdeXGHDxmtHjXNK8y-bWJjb14U5YHaFLkRjjRPEZ5prgVPQA_d8cmeIDpgwsnbOfdsJikPejMVU3KLTjOvgAAxybHbaV0-AJV7tzeX_njCqLFJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a757bdbbc.mp4?token=ViEI_L6oj9VaALC34PsbxTx1584cXnLH_cjVj4dyp_Tewxcq-bg9aGDa97A4aR-dqPwrqZ0nWwx3ty80QjrYXs31Qymj_XQLtmRnuN-GDS-ua6-gjUrZOA3HmHCWh-Ix7reHQxqbqT4sT9aa6YNPv-Ir5RI1UasWqshiFOhKewrVIZ1w31jDRblyQyiPYzn6BXNyPQ8b_Xasp0SGdke4Du-I_qqT3-J7mIA44cjdeXGHDxmtHjXNK8y-bWJjb14U5YHaFLkRjjRPEZ5prgVPQA_d8cmeIDpgwsnbOfdsJikPejMVU3KLTjOvgAAxybHbaV0-AJV7tzeX_njCqLFJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس ، معاون ترامپ : می‌دانیم که مردم نگران هزینه‌های معیشت هستند و این موضوعی است که هر روز با تمرکز کامل بر حل آن متمرکز هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/25286" target="_blank">📅 21:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">واشنگتن‌پست: یک مقام ارشد دولت ترامپ اعلام کرد هرچه متحدان آمریکا سریع‌تر مسیرهای حیاتی ارتباط اقتصادی ایران با جهان را محدود کنند و منابع مالی و منافع جمهوری اسلامی را تحت فشار قرار دهند، واشنگتن زودتر به هدف خود خواهد رسید. دولت ترامپ با تشدید فشارهای اقتصادی، محدود کردن صادرات نفت و مسدود کردن مسیرهای مالی، در تلاش است ایران را به پذیرش خواسته‌های آمریکا وادار کند. با این حال، هنوز مشخص نیست این کارزار فشار چه زمانی به نتیجه خواهد رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/25285" target="_blank">📅 21:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25284" target="_blank">📅 20:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خلاصه پیغام های زیاد : تهرانپارس بین فلکه دوم و سوم انفجار شدید اومد آسمون رو دود گرفته و بعد صدای تیر اندازی شنیده شد! علت نامشخص ولی حمله هوایی نیست @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25283" target="_blank">📅 20:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqY7K2ye3nNv2R9boBD7J3_3h2p_qORfKi4Mu5fPhmdp8ZI7S_FdcSVF_BCEc-ETH-I3bX8MCJRTB_H23KsNEqlhjAUYKGEcVuNwKBB57s0Yeh4sYPlZpj88ZF3ksu9p76GIjVvrIYzBNnwgHoFTRCSiFZToHbTTwM8xsApZTPa28b-PR3O69fuTZRLHMnU3OFdCVSMqaNTy6sc_SN-pGa_wYpPcWustQKO_mkdX_c2Y1Stiv9gu-y3ILAqjR27ZThG48C_FnaZ4z9SeGxzhWMIvA-p8e5TtXDUPqbm6DPnhkh2gWM8tfJcpPUUelqMblf7MXO6RuMo6f4C_purd7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFFcNMdPgr0fOxloUo8AT6UIjuZDhE8WvBMBF8BMvmLO3Y0sE95TtPOBYI65_aePvPDowJ6Sjf86XLStlcd0ZHQLkx8VRTnYSvkZSfAf_-yJUFXjGQb4lkIzd-sHRc-oky5TPiDFuoy91-9uRLQEnL4XlQA0dRHGrx_auO4WEYcOWZHO1E-GIoOF81AMpIVBOwv_TGJqB_XKLOKC9wAGaw4_bRHgB4FdtUfiLiKwSsPy0LZX4FQHVdEvTf2c5SEtbbQlO7HCyS-zrfXsnSLTtMVgFVGkGXruYWsE4d_5imqFisfsZBOfeS5Gkir2dXeBNNkYSMU2bm1QvjSVfR2wEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خلاصه پیغام های زیاد : تهرانپارس بین فلکه دوم و سوم انفجار شدید اومد آسمون رو دود گرفته و بعد صدای تیر اندازی شنیده شد!
علت نامشخص ولی حمله هوایی نیست
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25281" target="_blank">📅 20:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هم اکنون صدای انفجار مهیب از محدوده فلکه سوم تهران پارس ، شرق تهران ، دود مشاهده میشود
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25280" target="_blank">📅 20:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a4aeebe5.mp4?token=FuwvQw9bkEKrv0FOGN5NbpoAtwE3mS7-RPL3jbTgn-ueHBf5CF7ONRF3MeBf30nCqrCD4gLJvrGCqf_xH3WGMAGzlfkgOcYrKrFy1zqPhXwX1nLHgveIFmQomueIz3WhTTgmpvI2-Ap_TjKzrtE_5ccBz9g23Jr_81mKQRgWcpQM28zSppQQHGdLkXPKquAaUsrLAitEyDVcY-b6Rkb3tNILiqcJ5KWbPqzrtYdw9klANhWL6Btn7E7AVkZZdHc8GReNhJxlG4CUcMLbhnhbTLZDRRTzbarhhs19_ZYoJogODWALC4WSqHJ17H_U_1E8pBWspZGNxwyg6Y_Gok5XCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a4aeebe5.mp4?token=FuwvQw9bkEKrv0FOGN5NbpoAtwE3mS7-RPL3jbTgn-ueHBf5CF7ONRF3MeBf30nCqrCD4gLJvrGCqf_xH3WGMAGzlfkgOcYrKrFy1zqPhXwX1nLHgveIFmQomueIz3WhTTgmpvI2-Ap_TjKzrtE_5ccBz9g23Jr_81mKQRgWcpQM28zSppQQHGdLkXPKquAaUsrLAitEyDVcY-b6Rkb3tNILiqcJ5KWbPqzrtYdw9klANhWL6Btn7E7AVkZZdHc8GReNhJxlG4CUcMLbhnhbTLZDRRTzbarhhs19_ZYoJogODWALC4WSqHJ17H_U_1E8pBWspZGNxwyg6Y_Gok5XCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: بعد از آن، موشک‌هایشان به سمت کشور ما حرکت می‌کردند. آن‌ها در تلویزیون با این موضوع شوخی می‌کنند و می‌گویند: «تو گفته بودی قرار است لس‌آنجلس را هدف قرار دهند!» اما واقعیت این است که مسیر پرتاب موشک به سمت شهرهایی مثل سن‌دیگو و لس‌آنجلس برای آن‌ها مناسب‌تر بود. البته احتمالاً پیش از آمریکا، اروپا را هدف قرار می‌دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25279" target="_blank">📅 20:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بن‌گویر وزیر امنیت اسرائیل : زنده باد جنگ.
@WarRoom
😂
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25278" target="_blank">📅 19:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b2196422.mp4?token=X_EjDSwoy-758RQQ5gy6vq5cLdfgnsBNH30AdoYMyBFIeH1GS4zcWXF9ZVla0rr-OqyLpIi0WC3AXxu3siexp-ZKUnG2GTC_UXD83yLtm7t3LOgl2zJa1nG75KdfyTy1uqOdcS52xN5nDBqUeaOZ_CBNqbl4Cv9IlvsObRjmbP0awPwEurwa5gyzXjZNUwEvuMAT98BbZ0rycy55CPiwCHaNcziyfLKBb9ZK5tuqHdtX6Zx-6qGO47NkW01l8lGjNRHZno52Koux4kwR81yb_cNUkMhBFHU0mmoLtZmFAg_oFNzF9EwzH4TdeTuVUTO28znXWEsWp-MvfX8WhQPRlHtTXgQrpetCRmhtj3GloOCMGRBZwXkKGPQ8YYc2rN6kMMisN04UT0mOP26tPAazjnWedDG8BBE7hAmjslCJq45i3m-mL_6PeDMoPBlVwYho9aQ3sjmPgrBkqN211_9AXQTvzgx9E6gr-Qbn5Izhz3LJfmQOfJ8m42djJipbC_zOIxV8kzFDY3JvH0mP_XR-LFSCcTd3OXUExqDdLIyfj-06D_XgVfFX0j2Pwda3cPPMggG6-bkb5dcNFvdBsDRlmfIG_i5HXUtZOQ-6tCHax9SDNhb7LU7GGgPQweVYoEPJKpFiCxhrdTk5G-9HIe4THtkUqYvFpP5H9UCfoFEhU44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b2196422.mp4?token=X_EjDSwoy-758RQQ5gy6vq5cLdfgnsBNH30AdoYMyBFIeH1GS4zcWXF9ZVla0rr-OqyLpIi0WC3AXxu3siexp-ZKUnG2GTC_UXD83yLtm7t3LOgl2zJa1nG75KdfyTy1uqOdcS52xN5nDBqUeaOZ_CBNqbl4Cv9IlvsObRjmbP0awPwEurwa5gyzXjZNUwEvuMAT98BbZ0rycy55CPiwCHaNcziyfLKBb9ZK5tuqHdtX6Zx-6qGO47NkW01l8lGjNRHZno52Koux4kwR81yb_cNUkMhBFHU0mmoLtZmFAg_oFNzF9EwzH4TdeTuVUTO28znXWEsWp-MvfX8WhQPRlHtTXgQrpetCRmhtj3GloOCMGRBZwXkKGPQ8YYc2rN6kMMisN04UT0mOP26tPAazjnWedDG8BBE7hAmjslCJq45i3m-mL_6PeDMoPBlVwYho9aQ3sjmPgrBkqN211_9AXQTvzgx9E6gr-Qbn5Izhz3LJfmQOfJ8m42djJipbC_zOIxV8kzFDY3JvH0mP_XR-LFSCcTd3OXUExqDdLIyfj-06D_XgVfFX0j2Pwda3cPPMggG6-bkb5dcNFvdBsDRlmfIG_i5HXUtZOQ-6tCHax9SDNhb7LU7GGgPQweVYoEPJKpFiCxhrdTk5G-9HIe4THtkUqYvFpP5H9UCfoFEhU44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما مانع دستیابی جمهوری اسلامی به سلاح هسته‌ای شدیم و این موضوع به‌زودی، به یک شکل یا شکل دیگر، حل‌وفصل خواهد شد.
ترامپ: ایران دیگر ارتش، نیروی دریایی، نیروی هوایی یا سامانه‌های پدافند هوایی ندارد.
ترامپ: دیروز بیشترین حجم نفت از زمان آغاز جنگ از تنگه هرمز عبور کرد.
ترامپ: دیروز ۲۸ میلیون بشکه نفت از تنگه هرمز عبور دادیم؛ رقمی که از زمان آغاز جنگ بی‌سابقه بوده است.
ترامپ: خبرهای مهمی درباره بحران گازوئیل داریم و برای حل این ران با قدرت اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25277" target="_blank">📅 19:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00c1954a3.mp4?token=JdRwLlYmQy-dG5_3-GyN8WiRVWQK7wwR28kbXlE5yzsQrdXG6lMvYxwb2-QRpnYYHJikBcJ8r8m1v7iJ0bds90dyT-ytgosKy1B9a58RXVZSoHZQaVuyfw-z9DQan2lS_NU3Ids2WjTwUhP5u3QyWLsNV2BNalL6zFOEEIYnAKfi09CFz1hOve1HG94xlFz-cn-WfSB0uFFw7WxTtv-FKwtnymb5RmOUL-eD_3u5jn_laMUYHEy_PIv300uoJYRhbrRwIYYRBk44RH_dWJwHpqFMWWpnZtIlstSva9nE-I1XckJeCs5q26AnE2Xhkr32REaogrKJDLNAFi0Kv1763w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00c1954a3.mp4?token=JdRwLlYmQy-dG5_3-GyN8WiRVWQK7wwR28kbXlE5yzsQrdXG6lMvYxwb2-QRpnYYHJikBcJ8r8m1v7iJ0bds90dyT-ytgosKy1B9a58RXVZSoHZQaVuyfw-z9DQan2lS_NU3Ids2WjTwUhP5u3QyWLsNV2BNalL6zFOEEIYnAKfi09CFz1hOve1HG94xlFz-cn-WfSB0uFFw7WxTtv-FKwtnymb5RmOUL-eD_3u5jn_laMUYHEy_PIv300uoJYRhbrRwIYYRBk44RH_dWJwHpqFMWWpnZtIlstSva9nE-I1XckJeCs5q26AnE2Xhkr32REaogrKJDLNAFi0Kv1763w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: دیروز ۲۸ میلیون بشکه نفت از منطقه تنگه هرمز خارج کردیم؛ فکر می‌کنم این رقم از هر زمان دیگری، حتی قبل از جنگ، بیشتر است.
ترامپ درباره محاصره دریایی: ما محاصره برقرار کردیم و هیچ‌کس از آن عبور نمی‌کند. انگار اگر محاصره را به ایتالیایی‌ها می‌سپردم؛ شاید آن‌ها حتی بهتر هم عمل می‌کردند، اما شما این کار را خیلی خشن و با شدت انجام می‌دهید.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25276" target="_blank">📅 19:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edb5373c67.mp4?token=S9UxPndMvv_rX-yn19WIrkFdTs2i31c_gvDkwUu94MTLd0JhiwlVE87rLBuDh9-hzQDRIfB4bOq8h01RtD9LXRw1ssWZ9SK-nLWDKQqxL0KnAAbaL-ff8KFcQ_6pgmGD3IaoVLy7uskHBGow6fL1fj03n8VUpQcVPwt0ISV57CzCTBzTpZKJrm389hc9X1JStDgGyKiJTFH7Ye60Fuv-fOOFjE093oHHw2NvpkFRiGUGJY1cQm2HzKIRMCXSXhM2RUP9M4xc7S_7PfFEaeWOjmsFLNtE2BOJwGOfD8fuNYKQhEPM4GwqwpSe_T_Bh0nAydUMGvwL9RinG_xRMuua9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edb5373c67.mp4?token=S9UxPndMvv_rX-yn19WIrkFdTs2i31c_gvDkwUu94MTLd0JhiwlVE87rLBuDh9-hzQDRIfB4bOq8h01RtD9LXRw1ssWZ9SK-nLWDKQqxL0KnAAbaL-ff8KFcQ_6pgmGD3IaoVLy7uskHBGow6fL1fj03n8VUpQcVPwt0ISV57CzCTBzTpZKJrm389hc9X1JStDgGyKiJTFH7Ye60Fuv-fOOFjE093oHHw2NvpkFRiGUGJY1cQm2HzKIRMCXSXhM2RUP9M4xc7S_7PfFEaeWOjmsFLNtE2BOJwGOfD8fuNYKQhEPM4GwqwpSe_T_Bh0nAydUMGvwL9RinG_xRMuua9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران و محاصره دریایی: ایتالیایی‌ها شاید حتی بهتر از شما هم این کار را انجام بدهند، اما شما این کار را خیلی خشن و با شدت زیادی انجام می‌دهید.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25275" target="_blank">📅 19:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2623ad9e11.mp4?token=McWKoPAxeBzIG7wEIO8hIJjgeGGaMhHrK9NIEtg8hPq5NAHGSdB4IJ7M1kzyAv-4x1EkePtdG2s4pcq54gOG-MfJG6LMd4Ai2bN501PRn39JEDU0mKxfaTkadbBbwRZyks5y-QVKEd_O_6EHNSro1WLfWxkS6dTO-1G3QtC4Z0nb7UsrMgyP7jhRLlCCazQ1eTi1TaGfGNKOB8gS2Un_TE_zJpMZYbtUPMo8tuJqbbmC5EwDn05i7i_HCzXf5i2SqoXCIN6xua3Sr75VdNAvjh-zlMQvg82zYwNe4seA420JpwvYuJmsyWevzDv_wbmeceBZ3zo44xzfhQc9jdDUYqFsmdnQhHfQWtU5ePYTuNdV7WfTWqzOYXufz8YpoP_6uNyuXoQsWoVASrLYno2QrsIi419Ya6O6HjpajiVAsfVjnDcx_afMWLrnXl9rv7-QWcpRESX24Pa-TMEIHg7jJYV-asngrP8x36sIYT8pURcJjoWibbbPavbunUNekL7OZ-RWfH45xi25WrfNmas3FrSkxNCpMpyl7OMADnodpZ-A1sDjdbQKe-thSLTBFsYgDyHCNrD9U96vbVRvX4dAthdtJRRdBQRAduoL201tt67lmiaPWOPtSf66s8WLoo0BMZQnKnV3R6ZVbeDErg4UpEcGpZPL4bNQYuJVZlXRQ28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2623ad9e11.mp4?token=McWKoPAxeBzIG7wEIO8hIJjgeGGaMhHrK9NIEtg8hPq5NAHGSdB4IJ7M1kzyAv-4x1EkePtdG2s4pcq54gOG-MfJG6LMd4Ai2bN501PRn39JEDU0mKxfaTkadbBbwRZyks5y-QVKEd_O_6EHNSro1WLfWxkS6dTO-1G3QtC4Z0nb7UsrMgyP7jhRLlCCazQ1eTi1TaGfGNKOB8gS2Un_TE_zJpMZYbtUPMo8tuJqbbmC5EwDn05i7i_HCzXf5i2SqoXCIN6xua3Sr75VdNAvjh-zlMQvg82zYwNe4seA420JpwvYuJmsyWevzDv_wbmeceBZ3zo44xzfhQc9jdDUYqFsmdnQhHfQWtU5ePYTuNdV7WfTWqzOYXufz8YpoP_6uNyuXoQsWoVASrLYno2QrsIi419Ya6O6HjpajiVAsfVjnDcx_afMWLrnXl9rv7-QWcpRESX24Pa-TMEIHg7jJYV-asngrP8x36sIYT8pURcJjoWibbbPavbunUNekL7OZ-RWfH45xi25WrfNmas3FrSkxNCpMpyl7OMADnodpZ-A1sDjdbQKe-thSLTBFsYgDyHCNrD9U96vbVRvX4dAthdtJRRdBQRAduoL201tt67lmiaPWOPtSf66s8WLoo0BMZQnKnV3R6ZVbeDErg4UpEcGpZPL4bNQYuJVZlXRQ28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ترابری ۲۴ ساعت پیش تا همین الانه الان ! دارن پرررر میان (عرزشی هستی نبین سکته میکنی) فقط آخرش که مال همین چند ساعته یکی از‌ زیبا ترین پل های هوایی شکل میگیره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25274" target="_blank">📅 19:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">😾</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25272" target="_blank">📅 18:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رویترز: دولت ترامپ تحریم‌های گسترده‌ای علیه دیوان کیفری بین‌المللی اعمال کرد که ممکن است دسترسی این نهاد به خدمات بانکی، بیمه و نرم‌افزار را مختل کند. این اقدام در واکنش به صدور حکم بازداشت برای بنیامین نتانیاهو و دیگر مقام‌های اسرائیلی و تحقیقات قبلی درباره…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25271" target="_blank">📅 18:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یسرائیل کاتس، وزیر دفاع اسرائیل: یائیر گولان اکنون با حذف خامنه‌ای و عملیات «غرش شیر» مخالف است؛ نفتالی بنت با عملیات «ملت شیر» مخالفت کرد؛ یائیر لاپید بخشی از قلمرو حاکمیتی اسرائیل را به حزب‌الله واگذار کرد؛ آویگدور لیبرمن می‌خواهد بزرگراه ۶ را به کنترل یک ارتش عربی بسپارد؛ گادی آیزنکوت می‌خواهد از لبنان فرار کند و منصور عباس پشت پرده پنهان شده است. اگر این‌ها گزینه جایگزین باشند، چه جای تعجب دارد که همه دشمنان ما برای سرنگونی نتانیاهو و دولت راست‌گرای او تلاش می‌کنند؟
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25270" target="_blank">📅 18:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIz0gbdjJHT_4pNq_ufPIsvsl1P_Qk9lr9XlwyqY2YyoOJ0gh51DmhouzfTBAC1qp1kgpkUJi5hamQXl1LF1B4ZXeeSjOBziUrpxsvnnCJCngNaZo4TchB79ZPlUHR8aaRGv7jPp7XQWvZNC_VUSIvxr3V531c0Jj_JfFKRfN00Kcd2d_2M1YFDKmOGoin9C8axACZUWL-U2_0VB3eU3Xx3GxOBjhIwrUAJcep5cMX1uSKw9fxgQ4MWBsz3po-Y3LhuF07gGcGSVrqUmBKtmEaKjpo5bYAJIXk6pfkXUeSCIY32bcKP3_v_TcbKm5v5xpQ5Xo4LRxZX6YNYmaCNw_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/683fae1eda.mp4?token=qNu-y8hHMmVWdNLlOvCN62tYFngehhFExBkNNTltIVafy-J0QPZPa2JKHa53XX2LIxJZa6xpPVP02YSwRvRGrcwGvELzv5onVWveWx2sykS6Ye-8Uijj4zmp91gvcuBireOTtSEvrMa72WyFhRiJ2lFcc06dMvEgZyqSSHDhStqP5OFvM8p6BW4FePte__oWshgUDfnKXy8LX_CrJj5sgfsDCp_r_kpy1PoyjkbfUW-tDnr9DgeSjknjLOCXIAvi0GNI0Za8axXjgpYVkvz0TxRwJqp4QpZOWWjpZ3_pr6wNlK3bcKmYjWYz_6QdWcQoNDQWUVIiehhrkM1pFJ_otQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/683fae1eda.mp4?token=qNu-y8hHMmVWdNLlOvCN62tYFngehhFExBkNNTltIVafy-J0QPZPa2JKHa53XX2LIxJZa6xpPVP02YSwRvRGrcwGvELzv5onVWveWx2sykS6Ye-8Uijj4zmp91gvcuBireOTtSEvrMa72WyFhRiJ2lFcc06dMvEgZyqSSHDhStqP5OFvM8p6BW4FePte__oWshgUDfnKXy8LX_CrJj5sgfsDCp_r_kpy1PoyjkbfUW-tDnr9DgeSjknjLOCXIAvi0GNI0Za8axXjgpYVkvz0TxRwJqp4QpZOWWjpZ3_pr6wNlK3bcKmYjWYz_6QdWcQoNDQWUVIiehhrkM1pFJ_otQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع محلی از کشته شدن معاونت اجتماعی انتظامی استان سیستان و بلوچستان در منطقه چشمه زیارت زاهدان بر اثر یک بمب کنار جاده‌ای خبر می‌دهند. @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25267" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز: دولت ترامپ تحریم‌های گسترده‌ای علیه دیوان کیفری بین‌المللی اعمال کرد که ممکن است دسترسی این نهاد به خدمات بانکی، بیمه و نرم‌افزار را مختل کند. این اقدام در واکنش به صدور حکم بازداشت برای بنیامین نتانیاهو و دیگر مقام‌های اسرائیلی و تحقیقات قبلی درباره…</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25266" target="_blank">📅 18:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز: دونالد ترامپ که بارها گفته بود شایسته دریافت این جایزه است، امسال نیز برنده آن نشد. جایزه صلح نوبل ۲۰۲۶ به ناوانتم «ناوی» پیلای، حقوقدان اهل آفریقای جنوبی و کمیسر عالی پیشین حقوق بشر سازمان ملل، رسید. کمیته نوبل از تلاش‌های او برای تقویت حقوق بین‌الملل…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25265" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نیوزمکس : وزیر خزانه‌داری آمریکا گفته  است دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25264" target="_blank">📅 17:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">منابع محلی از کشته شدن معاونت اجتماعی انتظامی استان سیستان و بلوچستان در منطقه چشمه زیارت زاهدان بر اثر یک بمب کنار جاده‌ای خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25263" target="_blank">📅 17:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/von-RjIKdxxAX5t3NbjcwS-m-z5NKkHW5HDFqrSV1Uys3yHdZkSRaukP9rrzWbEcZPYqEda_dL22aHK44l1CplHMjPNDmiu4IXSSxMDwggA7UhQGdbo6Ri9tYPEWOhFtZlzFarxdmJBfMgbW3Z41UwQ-09aUiC2pkhQB5Rv5NiON8OCbq1fhLpX0JPCV5QOpP1tlqIjawo1-k67rs3r4tuupw-6FvTp7YQpJusqflzzAA26hTpNJI3ZqGLIH_tBOpVW3IKXfBxZv9fvNzeQJFEpjbEQ2J_DDdUtu4_D3soW2FV8QE2Ktg8qsJsUdnh_8Q9Z4UoSBGwK2yG7qP0pC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:مربی تناسب اندام ناو هواپیمابر یو اس اس جورج واشنگتن (CVN 73) که در کشتی با نام «رئیسِ خوش‌‌اندام» شناخته می‌شود، اعضای خدمه را در طول تمرین در آشیانه هدایت می‌کند. این ناو هواپیمابر به عنوان یک شهر شناور، دارای امکانات تناسب اندام متعددی است که به صورت شبانه‌روزی در دسترس هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25262" target="_blank">📅 16:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بسنت: سپاهی‌ها دیگر نمی‌توانند برای دیدن جراح پلاستیک‌ و دوست‌دخترشان به خارج بروند
اسکات بسنت، وزیر خزانه‌داری آمریکا، از اجرای کارزار «انزوای مطلق» علیه جمهوری اسلامی خبر داد و اعلام کرد دولت پرزیدنت ترامپ با استفاده از محاصره دریایی، محدودیت پروازهای بین‌المللی، مسدود کردن مسیرهای زمینی، و توقیف دارایی‌های دیجیتال، در تلاش است ارتباط اقتصادی و مالی حکومت ایران با جهان خارج را قطع کند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25261" target="_blank">📅 16:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سپاه پاسداران اعلام کرد کشتی غول‌پیکر حامل گاز مایع (LPG) با نام اِن‌وی سان‌شاین (NV Sunshine) متعلق به شرکت نات‌ویت، هنگام عبور از مسیر غیرمجاز در جنوب تنگه هرمز هدف قرار گرفته و در بخش موتورخانه و سامانه رانش دچار آتش‌سوزی شده است و هشدار داد اقدامات علیه کشتی‌هایی که از مسیرهای غیرمجاز عبور کنند، به تنگه هرمز محدود نخواهد ماند و این شناورها در سراسر منطقه تحت تعقیب قرار خواهند گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25260" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">در سرقتی بزرگ از کارخانه شراب‌سازی
مارکزی آنتینوری (Marchesi Antinori)
در منطقه توسکانی ایتالیا، حدود
۳۰ هزار بطری شراب به ارزش ۵ میلیون یورو
به سرقت رفت.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25259" target="_blank">📅 15:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25257" target="_blank">📅 15:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آکسیوس: احتمال ازسرگیری جنگ با ایران طی ۳ هفته آینده
به گفته باراک راوید، مقام‌های آمریکایی به رئیس ارتش اسرائیل از آمادگی برای احتمال آغاز مجدد عملیات گسترده علیه ایران خبر داده‌اند. زامیر هشدار داده این اقدام ممکن است به تعویق انتخابات اسرائیل منجر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25256" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سفارت مجازی آمریکا در تهران
از شهروندان آمریکایی حاضر در خاورمیانه خواست به‌دلیل شرایط پیچیده امنیتی،
حداکثر احتیاط را رعایت کنند
.
این نهاد هشدار داد که احتمال
لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرها
وجود دارد.
همچنین با صدور
هشدار سطح ۴ (بالاترین سطح هشدار)
، تأکید کرد: «به هیچ دلیلی به ایران سفر نکنید» و از شهروندان آمریکایی حاضر در ایران خواست
فوراً این کشور را ترک کنند
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25255" target="_blank">📅 15:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25254">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اخرین ویدیو ترامپ شب حمله</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25254" target="_blank">📅 15:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اورشلیم پست : منابع اسرائیلی دستوراتی دریافت کرده اند مبنی بر اینکه ، اسرائیل در صورت شناسایی آمادگی ایران برای شلیک موشک به آنها ، حمله پیشگیرانه را انجام دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25253" target="_blank">📅 15:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">العربیه به نقل از یک مقام آمریکایی: حمله گسترده به ایران در آخرین لحظه به تعویق افتاد
یک مقام نظامی آمریکایی به العربیه گفت ارتش آمریکا روز یکشنبه ۴ اکتبر، در آستانه اجرای حمله‌ای گسترده و مشترک با اسرائیل علیه ایران قرار داشت و نیروهای آمریکایی تا نیمه‌شب به وقت آمریکا در حالت آماده‌باش باقی ماندند و انتظار برای دریافت دستور نهایی حمله تا ساعات اولیه دوشنبه ادامه یافت؛ اما در نهایت دونالد ترامپ دستور حمله را به تعویق انداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25252" target="_blank">📅 15:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الجزیره : حسین موسویان، دیپلمات پیشین ایران، و آلن ایر، دیپلمات پیشین آمریکا، ارزیابی کردند که درگیری در هفته‌های آینده احتمالاً
وخیم‌تر
خواهد شد و توافق صلح نزدیک نیست ، آکسیوس هم در گزارشی گفت
اختلاف اصلی پا برجا است
و نشانه‌ای از کاهش اختلافات از دو طرف دیده نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25251" target="_blank">📅 14:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شاهزاده رضا پهلوی در شبکه ایکس: «
تا وقتی این ساختار سر کار است، اصلاح ممکن نیست و سقوط ادامه دارد.
سقوط شتابان ریال، نابودی دستمزدها و پس‌انداز مردم و گران‌ترشدن زندگی روزمره، نتیجه مستقیم بی‌ثباتی، فساد، چاپ پول و سیاست‌های نابخردانه جمهوری اسلامی است.
تورم نزدیک به ۹۰ درصد، مالیات پنهانی است که حکومت از مردم می‌گیرد
و به جیب کسانی می‌ریزد که پول چاپ می‌کنند و زودتر خرج می‌کنند. تورم مهار نمی‌شود، اما سیاست‌های شکست‌خورده‌ای مانند دلارپاشی ادامه دارد؛
سیاست‌هایی که فقط ثروت خودی‌ها را افزایش می‌دهند.
»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25250" target="_blank">📅 14:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کان‌ نیوز عبری :
ایلان شاگيف، یک مقام سابق ارشد شاباک، ادعا می‌کند که نخست‌وزیر بنیامین نتانیاهو بارها از پیشنهادات سازمان شاباک برای ترور مسئولان ارشد حماس خودداری کرده است.
او گفت: «هر بار که ما آماده بودیم، ایشان پاسخ می‌دادند: آمادگی خود را حفظ کنید.»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25249" target="_blank">📅 14:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دو شهروند ایرانی در بریتانیا به دادگاه احضار شدند , آن‌ها یک بررسی اولیه و مشاهداتی را در مورد سفارت اسرائیل در لندن، یک کنیسه قدیمی در بریتانیا و سایر اهداف اسرائیلی و یهودی انجام داده بودند.
در کیفرخواست ادعا شده است که این دو نفر از این مکان‌ها عکس و فیلم گرفته و راه‌های دسترسی به آن‌ها را بررسی کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25248" target="_blank">📅 14:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئیس‌جمهور ، زرشکیان : ما همواره بر اهمیت گفتگو تاکید کرده‌ایم، اما گفتگو زمانی ثمربخش است که با استفاده از زور و اجبار نباشد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25247" target="_blank">📅 13:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GidlNwqxW27xOD8KyazSgMo3zpsMyPzwpEumZOhivwyDkrQEg5_SjLxOrrr15uDiAZ4esXNZHfUQAQj4v0nUNwh9eUYLI3_1vXnn5DOKx1JMbWBzM6cnMl7_Qd_MbzYpJYiX29TNJWi8rQWHN_p9e45vPqQpbJET2VU_tgUcz-i9R7jsi5qsT-znFjHJ2cKbAv03aTf5PjUMDn7GRqVmjdmwfvxG98XA3IL9U8f1MjUh3cmcoVvoCQHKRz6qvMoeN_kRE3Ot_WkP8zeFAV-mF0bCoKPjEMks1W95B9OaQuq8jrDRmG5xPJXVDxOD39tRvmGXKZm5NHQZ2HGRHBMYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا این بار برای کل خاورمیانه هشدار امنیتی صادر کرد !!!!!
وزارت خارجه آمریکا: شهروندان آمریکایی که در حال حاضر در خاورمیانه حضور دارند، به دلیل شرایط پیچیده امنیتی باید
هوشیاری بیشتری داشته باشند.
احتمال لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرها وجود دارد.
ایران و گروه‌های حامی آن ممکن است منافع دیگر آمریکا در خارج از کشور یا مکان‌های مرتبط با ایالات متحده و شهروندان آمریکایی در سراسر جهان، از جمله شرکت‌ها و سایر مؤسسات آمریکایی، را نیز هدف قرار دهند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25246" target="_blank">📅 13:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رویترز: دونالد ترامپ که بارها گفته بود شایسته دریافت این جایزه است، امسال نیز برنده آن نشد. جایزه صلح نوبل ۲۰۲۶ به ناوانتم «ناوی» پیلای، حقوقدان اهل آفریقای جنوبی و کمیسر عالی پیشین حقوق بشر سازمان ملل، رسید. کمیته نوبل از تلاش‌های او برای تقویت حقوق بین‌الملل و پیگیری قضایی جنایات جنگی و نقض حقوق بشر تقدیر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25245" target="_blank">📅 13:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اکسیوس از قول سنتکام: ما دستور حمله به ایران را دریافت کرده ایم و در حال آماده سازی طرح هایی برای حملات احتمالی هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25244" target="_blank">📅 13:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال ۱۲ اسرائیل گزارش داد که ایال زمیر، رئیس ستاد ارتش اسرائیل، دو روز پیش از مقام‌های آمریکایی مطلع شده است که کاخ سفید و پنتاگون در حال صدور دستورالعمل‌های لازم برای آماده‌سازی یک حمله احتمالی گسترده آمریکا به ایران طی هفته‌های آینده هستند. این گزارش از…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25243" target="_blank">📅 12:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25242">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الحدث به نقل از یک منبع نظامی آمریکایی گزارش داد که پیشنهادهایی به دونالد ترامپ ارائه شده تا توانمندی‌های نظامی ایران در نوار ساحلی و تا عمق ۵۰ تا ۸۰ کیلومتری هدف حمله قرار گیرند. به گفته این منبع، چنین حملاتی می‌تواند توان ایران برای
تولید انبوه و شلیک موشک‌ها و پهپادها
را به‌شدت تضعیف کند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25242" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ri0bcXaqvQLssiq6_ZBl9fRnOkKzYrTtJCKpMhRFpnrrSUkxREJl3Jhs7df2Ldf5RxQWvabIlmOv5duiLot3ZMS3UaVvpPUHQixBbaFL-Hcf8aaFVOfwh-rT8GOcKurykWvfaBPET_UPIyOvXQW-vliDsn8TjEiYr7zaQCMkuZnsbQkOjCiAUENO9I2PWeapXrDDa2Fr_91tNANzuLhvUYZEsP_N5fvVdFpGKXYpTh2Td3jJc6ZyMuWKKWmzPUjUgUWsgFmy_JbEig__a9ZttKqpQzDfoBV6SW_ITJ_NYtzcOKch_wOLdt_UKqAKlsuadJYRscRrIE8Fio7wh1RkoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkwBDSJXgZmZfysEBM2brFlX2rnizhKtlgKErkNfBMe0T_X9pWxKXHC_SRfpwWYtNR-bcaXnHgxkrnsbh-Jk0x_CC8iuoAwlm1hJSrgym4i2F0YnHVN5a8C3CEyhULpeKrRXNpGZ5JjxCVpoW6OTplCGV4nivHjROF4_hBMlwDO2Px3YBhiJ7sSVi2_0GbQa26opGQ50XMntkQrp1jK7KwhTKIU91PB4gZbdHHTX1z-h6mxyc6BywUsShOjk972GJvNkvohxMYokOe2eseTSZhkuosDABbtF6yzZJ30APorU3LhD5zAIiomiUfAv2GhUMUJVnH3WSLCQpaD-b4UBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJrO6Z1N-OfU0hvDB5b7sTmE1OQTDHU72B9nMT_kkQsH_FOi2wOsIu997MAV43aPZGulEEpMW3U8OvmmBjY8lMyk2yGRkNT68vw-JBmagZrhXLAEIT0K8oyBJDUMS8E44FDlNaHmEt72Rsun3VcgJaBgjDymUzuqncweSbbYv_85vxNe9H25R_dHHTeC7F-tUnGwUXaJJR9DnjM3SNTG2TrYjmHv0G8IFE7wH2HqibVdrR2auNyTJWTjIzfTvPKi6pe6KQVaBaHgC8QDDY_ihKfH10ChGg_ollp08LrCNpyWOPqFcYaBX7PDM9_bMPCOcsupyMvixy3Jc7aXIvw5GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یو‌اس‌اس مکین آیلند (LHD-8): ناو آبی‌خاکی تهاجمی کلاس واسپ نیروی دریایی آمریکا با حدود ۲۵۳ متر طول و ظرفیت حمل حدود ۲۰۰۰ تفنگدار دریایی است. این ناو به سامانه پیشرانش هیبریدی شامل توربین‌های گازی و موتورهای الکتریکی مجهز است، همچنین ۱۰ فروند جنگنده اف-۳۵بی…</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25239" target="_blank">📅 11:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25238">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال ۱۲ اسرائیل گزارش داد که ایال زمیر، رئیس ستاد ارتش اسرائیل، دو روز پیش از مقام‌های آمریکایی مطلع شده است که کاخ سفید و پنتاگون در حال صدور دستورالعمل‌های لازم برای آماده‌سازی یک حمله احتمالی گسترده آمریکا به ایران طی هفته‌های آینده هستند. این گزارش از افزایش آمادگی نظامی آمریکا برای احتمال ازسرگیری حملات حکایت دارد، اما به‌معنای اتخاذ تصمیم قطعی برای آغاز حمله نیست.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25238" target="_blank">📅 11:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انیمیشن جدید حکومت از حامله کردن زیردریایی آمریکایی و دادن دستورات جدید با سی دی. وقتی ذهنت فقیره، همچین چیزی میدی بیرون
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25237" target="_blank">📅 10:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تایمز اسرائیل: ایال زمیر، رئیس ستاد ارتش اسرائیل، از یک افسر زن یگان ۸۲۰۰ با نام مستعار «و» تقدیر کرد که پیش از حمله ۷ اکتبر ۲۰۲۳ درباره آمادگی حماس برای حمله گسترده هشدار داده بود، اما هشدارهایش جدی گرفته نشد. @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25236" target="_blank">📅 10:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25235" target="_blank">📅 10:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تایمز اسرائیل: ایال زمیر، رئیس ستاد ارتش اسرائیل، از یک افسر زن یگان ۸۲۰۰ با نام مستعار «و» تقدیر کرد که پیش از حمله ۷ اکتبر ۲۰۲۳ درباره آمادگی حماس برای حمله گسترده هشدار داده بود، اما هشدارهایش جدی گرفته نشد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25234" target="_blank">📅 10:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سلام یاشار خوبی خسته نباشی دم شما گرم بابت همیشه امروز جمعه ۱۷ مهر اومدم بیرون می‌بینم که خیابونا و کوچه‌ها و اینا پر بسیجی پر سپاهی نیروی انتظامی پلیس یگان ضربت کوفت زهرمار پر ارزشیه نمی‌دونم چه خبره
@WarRoom
سلام خسته نباشی یاشار جان
نمیدونم مهمه یا نه ولی بعد مدتها بسیجیا و سپاهیا امروز تو خیابونن خیلی زیاد  , من عبدل آباد میومدم خیابان فرشته پر بود , جاهای دیگه هم همینطور</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25233" target="_blank">📅 10:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی: ارتش آمریکا در حال بررسی گزینه‌هایی برای
حمله مجدد به ایران و اجرای عملیات‌های نظامی دیگر پیش از انتخابات میان‌دوره‌ای ۳ نوامبر
است. پنتاگون پیش‌تر از فرماندهی مرکزی آمریکا خواسته بود آمادگی‌های لازم برای ازسرگیری عملیات گسترده علیه ایران را تکمیل کند؛ گزینه‌های احتمالی شامل حمله به تأسیسات انرژی، زیرساخت‌ها و اهداف هسته‌ای ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25232" target="_blank">📅 10:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکنید. این پست رو‌ ذخیره کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25231" target="_blank">📅 09:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیویورک‌تایمز: برخی شرکت‌های کشتیرانی برای عبور کشتی‌های خود از تنگه هرمز به ایران پول پرداخت می‌کنند. طبق گزارش لویدز لیست، کشتی کانتینری «نیوویجر» با مالکیت شرکت چینی بنگبو شنگدا ترنسپورتیشن و مدیریت شرکت یونایتد پایونیر شیپینگ در شانگهای، از طریق یک واسطه چینی برای عبور از مسیر نزدیک جزیره لارک به ایران پول پرداخت کرده است. بخش عمده بیش از ۲۰ کشتی ردیابی‌شده در این مسیر، تحت مالکیت شرکت‌های یونانی بوده‌اند. گزارش‌های جداگانه از پرداخت مبالغی تا
۲ میلیون دلار برای عبور هر کشتی
حکایت دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25230" target="_blank">📅 09:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بابک زنجانی: تا وقتی نفت بالای ۱۰۵ دلار باشه آمریکا ۱ موشکم نمیتونه بزنه
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25229" target="_blank">📅 08:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جروزالم پست به نقل از گزارش نیویورک‌تایمز نوشت سه ناو هواپیمابر آمریکا به‌زودی در خاورمیانه حضور خواهند داشت و پنتاگون طرحی برای یک کارزار علیه ایران تهیه کرده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25228" target="_blank">📅 08:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رهبر‌حذب «یاشار»گادی آیزنکوت، رقیب اصلی نتانیاهو، میگه نگرانه که نتانیاهو برای به تعویق انداختن انتخابات، ظرف دو هفته آینده یه حمله گسترده به ایران انجام بده.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25227" target="_blank">📅 08:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پرتاب موشک از بندر لنگه
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25225" target="_blank">📅 01:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3JVYPTUSN_H_Bh9n23VlYkp5jsqhawBno4J-aV_xx1dRSaxOQRXojg8o4iSmzRhWoBICWktyJwZuBRkDd-DsdqSLchOHv1O9lEDHB7DcLi3AxR-Y0JPbP0aEnWDasW-igRU75Iqdj11MTa7eTxy-fIhl76Oll3zwXNZvsydy0xfZiMk2qSHnkBF7Q0eHkcqhM523fI9WrIyK1KRyPb2HVUEpHZPcTPX0S5gm3-ENNQaNcvydKZiBbauu5_D4fHzPJ9KZyV6Jclp05AAfUCUL8OlHTgZ-15sUga7X4tcCp1Tepx5l3wybc3t8AKe_hMUC_Xyx-9C3pNOzXkZxjN-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2a3b0dbfd.mp4?token=bnIboZLKyeOiYKzywskIqLrIvSxpAMkgwuizGP46AuZfkMUOdi81EawZ4K5Acor-jzyNMO9ym0hbCCOCJ1YCNOIUYWeGUpwop5BiYLBFIKjoHF5dU-Q3f7XEYeRQ9O7IQjZgN2nrFE1wBXsJF5VyqN25F9TAPK2s440YFDZiv0Oy7mJOO0RWc0ut9Y1Xm7s4LbCha6rgHIYgjtMWYH5o85yAoU97z-Zj-wOwqN_0s4ewNuUu3ESRvMuvKvge5HupB6bhamB06F_BCACBl9w8_opAq9SAtb0NMiDVxHFWPVwRg5amdp2xzam-qGXDlgNt-myDnwAF1B1PKdF9gIx5Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2a3b0dbfd.mp4?token=bnIboZLKyeOiYKzywskIqLrIvSxpAMkgwuizGP46AuZfkMUOdi81EawZ4K5Acor-jzyNMO9ym0hbCCOCJ1YCNOIUYWeGUpwop5BiYLBFIKjoHF5dU-Q3f7XEYeRQ9O7IQjZgN2nrFE1wBXsJF5VyqN25F9TAPK2s440YFDZiv0Oy7mJOO0RWc0ut9Y1Xm7s4LbCha6rgHIYgjtMWYH5o85yAoU97z-Zj-wOwqN_0s4ewNuUu3ESRvMuvKvge5HupB6bhamB06F_BCACBl9w8_opAq9SAtb0NMiDVxHFWPVwRg5amdp2xzam-qGXDlgNt-myDnwAF1B1PKdF9gIx5Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید از نوع استتار تکاوران نیروی زمینی من را یاد شخصیت «گریفین» در فیلم شاهکار «مرد نامرئی ۱۹۳۳» انداخت. البته برای دوستان جدید شخصیت گریفین به صورت فقط یک «عینک» در انیمیشن «هتل ترانسیلوانیا» نیز حضور دارد.
😂
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/25223" target="_blank">📅 01:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نیویورک‌تایمز گزارش داد پنتاگون پس از نشست محرمانه دونالد ترامپ و تیم امنیت ملی آمریکا در کمپ دیوید، گزینه‌های تازه‌ای برای ازسرگیری حملات گسترده به ایران تدوین می‌کند. یکی از سناریوهای مطرح‌شده،
انجام حملات طی یک دوره سه‌روزه
از حملات شدید علیه ایران است که موشک‌ها، پهپادها، زیرساخت‌های انرژی، مراکز فرماندهی سپاه پاسداران و تاسیسات نظامی را هدف قرار می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25222" target="_blank">📅 00:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">روزنامه جروزالم پست گزارش داد که هدف از ترور
علیرضا تنگسیری، فرمانده نیروی دریایی سپاه، جلوگیری از رسیدن او به فرماندهی کل سپاه پاسداران
بود. به نوشته این روزنامه، مقام‌های اسرائیلی او را فرمانده‌ای توانمند و خلاق می‌دانستند که در صورت رسیدن به رأس سپاه، می‌توانست تهدیدی جدی‌تر از احمد وحیدی باشد. این گزارش همچنین مدعی شد برد کوپر، فرمانده سنتکام، حدود ۱۹ مارس در تماسی محرمانه از رئیس ستاد ارتش اسرائیل خواسته بود تنگسیری را هدف قرار دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25221" target="_blank">📅 00:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای فارس
: نفتکش‌های متخلف روی مین‌های تنگۀ هرمز منفجر شدند
دقایقی پیش چند انفجار سنگین در معبر جنوبی تنگه هرمز رخ داد که ناشی از اصابت نفتکش‌های متخلف با مین‌های منتشره در منطقه از دریا می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25220" target="_blank">📅 23:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فارس: سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش درپی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب استان کرمان ،کشته شد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25219" target="_blank">📅 23:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرنگار المانیتور , جرد سزوبا: سناتور کریس مورفی، پس از دیدار جداگانه با
شیخ تمیم بن حمد آل‌ثانی، امیر قطر
و علی الثوادی، دیپلمات قطری و یکی از چهره‌های اصلی هماهنگ‌کننده میانجی‌گری میان آمریکا و ایران، گفت توافقی برای پایان دادن به جنگ با ایران
در آینده نزدیک بعید به نظر می‌رسد.
مورفی در سفر خود به قطر درباره تلاش‌های دیپلماتیک برای پایان جنگ با مقام‌های قطری گفت‌وگو کرد و تأکید کرد قطر همچنان نقش مهمی در میانجی‌گری میان واشنگتن و تهران دارد. این دیدارها در حالی انجام شد که مذاکرات آمریکا و ایران از طریق قطر بار دیگر با بن‌بست مواجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25218" target="_blank">📅 23:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرنگار اکسیوس: فلش‌بک: در ژوئن ۲۰۲۵، پیش از عملیات «چکش نیمه‌شب»، کاخ سفید اعلام کرد ترامپ «ظرف دو هفته» تصمیم خواهد گرفت که آیا آمریکا وارد جنگ اسرائیل علیه ایران شود یا نه.اما زمانی که این اظهارات را مطرح می‌کرد، در واقع از قبل تصمیمش برای حمله به تأسیسات هسته‌ای ایران را گرفته بود.
در ۲۷ فوریه، کمتر از ۲۴ ساعت پیش از آغاز جنگ اسرائیل و آمریکا علیه ایران، ترامپ مدعی شد که هنوز درباره ورود به جنگ تصمیمی نگرفته است.
اما در واقع، ترامپ از قبل مجوز انجام حملات را صادر کرده بود
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25217" target="_blank">📅 23:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30b8f646ae.mp4?token=ptgIZbGKj4TE2dq1pTJOwyYxnG5bWFc3Pgwy0hWg1EX7utEuY4d97cjTLs7-XsquKoK_w7kfPggexuHOdcRPiWpFotPf1RfT9jmbvWlVhODbcH5fxmnlVRNpwetzRv7NRXI0SA1Rl3mBrfjKEiBs6DCULzg2ilCTFIYdR_uLSE8ez3FAvYqiHVoN-tLNBWRFUrp-pxZfqtRtd6B0WltXjIFbqTcLuvfNOkyFC8p_F4agu87IE0qgrLd28MjlZwc8ogHeH3-KPDVxedoW8uALLj5Gh6sH2vYpCzOtPE5vDatEax-JAaXtKuW81W_-60BfY369MrzF7cCP2SyGlCqJFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30b8f646ae.mp4?token=ptgIZbGKj4TE2dq1pTJOwyYxnG5bWFc3Pgwy0hWg1EX7utEuY4d97cjTLs7-XsquKoK_w7kfPggexuHOdcRPiWpFotPf1RfT9jmbvWlVhODbcH5fxmnlVRNpwetzRv7NRXI0SA1Rl3mBrfjKEiBs6DCULzg2ilCTFIYdR_uLSE8ez3FAvYqiHVoN-tLNBWRFUrp-pxZfqtRtd6B0WltXjIFbqTcLuvfNOkyFC8p_F4agu87IE0qgrLd28MjlZwc8ogHeH3-KPDVxedoW8uALLj5Gh6sH2vYpCzOtPE5vDatEax-JAaXtKuW81W_-60BfY369MrzF7cCP2SyGlCqJFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه با پهپاد‌های موتور گازی‌ آبیش به منطقه ریزگری اربیل، کردستان عراق حمله کرد
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25214" target="_blank">📅 23:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پارلمان اروپا امروز، ۸ اکتبر، قطعنامه جدیدی درباره وضعیت حقوق بشر در ایران تصویب کرد. این قطعنامه با
۵۴۱ رأی موافق، ۱۱ رأی مخالف و ۲۵ رأی ممتنع
به تصویب رسید و در آن
خشونت علیه غیرنظامیان، افزایش اعدام‌ها، سرکوب معترضان، فعالان حقوق بشر و روزنامه‌نگاران و استفاده از اعترافات تحت شکنجه
محکوم شده است. پارلمان اروپا همچنین خواستار لغو احکام اعدام ترانه رحیمی و لیلا ابوالحسنی و لغو مجازات اعدام در ایران شد و سرکوب اقلیت‌های قومی و مذهبی و سرکوب فرامرزی جمهوری اسلامی را محکوم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25213" target="_blank">📅 23:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thYIbNw90XGDXfGTYcXD2-e5YOhbCcrca8rfrQPp52Qb9wcYY6f2wwr1sbXYZuya7mb62xRGxrkGpuSIUMhaR6vCJ84TAdz1ajMEgRMD6Xd6OsNkot15PlcMVjIPHaz2252DNBYErYC1Bj_-m3ODx-qCaWUJVEqicLcWUtntpooFN_LMY2Tgiltpo8htiic7vInSCcBtxzN43yaeP-rL6DhkfsYSIpZIzjAdiILaN7kF7poR0vVnwFeML6JBRXm5YO_xGW43ZR-14DdNGrBS0vPuP_ZVcVbc5yWHz6zd2JGC9pUxc5mdTUGVaA6QNSpk0LNCDtSXU551yualFff9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث : رسانه‌های جعلی تلاش می‌کنند این‌طور القا کنند که من از دشمن خواسته‌ام سن‌دیگو و لس‌آنجلس را بمباران کند، در حالی که منظورم این بود که
افزایش موقت قیمت بنزین، بهای کوچکی برای اطمینان از این است که ایران سلاح هسته‌ای نخواهد داشت.
تصور کنید اگر سن‌دیگو یا لس‌آنجلس بمباران شوند، چه بهای سنگینی باید پرداخت شود. من فقط مقایسه‌ای میان پرداخت مبلغی بیشتر برای مدت کوتاه بابت بنزین و
خطر بمباران شهرهای بزرگ آمریکا
انجام دادم. همه این را فهمیدند، حتی رسانه‌های جعلی، اما همچنان می‌گویند من خواسته‌ام دو شهری را که دوست دارم بمباران کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25212" target="_blank">📅 22:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ff0b265b.mp4?token=NXl9Wt6Np55B0sWWD1QnYY_jHLXz58zZEcE8AswIYusozuuKPIa-qI3Aj5agCznXbltremtV3pyI7npGlCWWomhffA11my15IgtFuivyhQgEaIUtVbrxMs653of-jYIlxTTCc4M-O0pI6jD8eQjnIcTclhTSPh2oqI222dgJK16WltNa4ExNcaQ8gYSpyBDTdkGulPG6PciiW0AuOC59Z_D3lR5689c1lz7r-jqASsbGBI-zWO6mFPuaHEsM_NeLBv9Bwi4DhJ67jm5yGIhbEO_8KtigHRgrjJ-jPzS0UQ-uCzCiHJ5LZikwbSpCUyp7iQCuffGrH9dIcEE8uuKwHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ff0b265b.mp4?token=NXl9Wt6Np55B0sWWD1QnYY_jHLXz58zZEcE8AswIYusozuuKPIa-qI3Aj5agCznXbltremtV3pyI7npGlCWWomhffA11my15IgtFuivyhQgEaIUtVbrxMs653of-jYIlxTTCc4M-O0pI6jD8eQjnIcTclhTSPh2oqI222dgJK16WltNa4ExNcaQ8gYSpyBDTdkGulPG6PciiW0AuOC59Z_D3lR5689c1lz7r-jqASsbGBI-zWO6mFPuaHEsM_NeLBv9Bwi4DhJ67jm5yGIhbEO_8KtigHRgrjJ-jPzS0UQ-uCzCiHJ5LZikwbSpCUyp7iQCuffGrH9dIcEE8uuKwHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست، وزیر جنگ آمریکا: ما به‌دنبال
اداره و بازسازی ایران از طریق حضور نظامی
نیستیم و نمی‌خواهیم تعداد زیادی نیروی نظامی را در ایران مستقر کنیم یا کنترل مناطق این کشور را در دست بگیریم. هدف ما صرفاً این است که به آن رژیم اسلام‌گرای افراطی بگوییم: شما هرگز سلاح هسته‌ای نخواهید داشت. اینکه این مسئله به روش آسان حل شود یا به روش سخت، انتخاب با ایران است؛ اما در نهایت این رئیس‌جمهور است که تصمیم خواهد گرفت. و می‌توانم تضمین کنم اگر آن لحظه فرا برسد، اقدام ما سریع و قاطع خواهد بود. این رئیس‌جمهور اهل بازی کردن نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25211" target="_blank">📅 22:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f244d9f33.mp4?token=cDK248dE1e3M_DxKuVxkENBAc8kFhOsRT_lpMWCXeOZ_efcdv9cn5VBt425DS84ua4R5vzjpPWdjYMLZ9mWbUx15JbSafjh3QUpSg8UufX-oo-FDiO9P5af_riiZo2P_TSxujFgF_Jmjqlt3mjS7UNqbrAAYz3WgE4cn0MaS1LzuzKJvE98tQzJznpWmq-UNl4LHbjeEqFXJX-g4FxewveLDH0V49ROYaG6kBVnTlXx0SRuDP_nWEQOlsKpMXnZa9MccOjDileesvxC3tCIcXjCvrSVO4u5qTTdlwQrLeeYA7NRqAfdymBoVusan0VXfc_fpDQCPVSBFwQbVFKL3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f244d9f33.mp4?token=cDK248dE1e3M_DxKuVxkENBAc8kFhOsRT_lpMWCXeOZ_efcdv9cn5VBt425DS84ua4R5vzjpPWdjYMLZ9mWbUx15JbSafjh3QUpSg8UufX-oo-FDiO9P5af_riiZo2P_TSxujFgF_Jmjqlt3mjS7UNqbrAAYz3WgE4cn0MaS1LzuzKJvE98tQzJznpWmq-UNl4LHbjeEqFXJX-g4FxewveLDH0V49ROYaG6kBVnTlXx0SRuDP_nWEQOlsKpMXnZa9MccOjDileesvxC3tCIcXjCvrSVO4u5qTTdlwQrLeeYA7NRqAfdymBoVusan0VXfc_fpDQCPVSBFwQbVFKL3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، درباره ایران:
ترامپ رئیس‌جمهوری نیست که بازی دربیاورد. او رئیس‌جمهوری نیست که
اتلاف وقت بیش از حد را تحمل کند.
ترامپ صلح می‌خواهد، اما حاضر است برای رسیدن واقعی و تاریخی به صلح،
هر کاری که لازم باشد انجام دهد.
ایرانِ دارای بمب هسته‌ای، اتفاق بدی است؛ نه فقط برای ما، بلکه
برای تمام جهان.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25210" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25209">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ایلان ماسک نشان ملی علوم را دریافت کرد. @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25209" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05da9e1cfb.mp4?token=lyeoGZ_NmUS7Wav3oO1-tK6AlBnVZNSTWLdIVTWXax4HQiRg3FIZSGoQWDYY9_Au9p_Xrmgx6hTu3toNCCJOk7oU6kEJtrDCh10tfnr_fK8Hk7mQZWOBsAsXo0TQ21tLCoTG5-MjFrGNwvN1u2FsQB_J_pEuQGU1JIZ9bhMX3jqUb9q3c1fTiMQ5knR6nncqyuepSAUpq08JYJ7f5GsJq-ajQbyGpFkbEaqD358xeIRLPDJbDrE8BYT4UcRvvH7G3KToJd1Vd2A9xHPMGTKCaoQiRRpLNlUU3-S4U-LIfJv9ymea0BF6cpi6-4ElKDC2kZrgoaa9KOpc47cKSvO6eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05da9e1cfb.mp4?token=lyeoGZ_NmUS7Wav3oO1-tK6AlBnVZNSTWLdIVTWXax4HQiRg3FIZSGoQWDYY9_Au9p_Xrmgx6hTu3toNCCJOk7oU6kEJtrDCh10tfnr_fK8Hk7mQZWOBsAsXo0TQ21tLCoTG5-MjFrGNwvN1u2FsQB_J_pEuQGU1JIZ9bhMX3jqUb9q3c1fTiMQ5knR6nncqyuepSAUpq08JYJ7f5GsJq-ajQbyGpFkbEaqD358xeIRLPDJbDrE8BYT4UcRvvH7G3KToJd1Vd2A9xHPMGTKCaoQiRRpLNlUU3-S4U-LIfJv9ymea0BF6cpi6-4ElKDC2kZrgoaa9KOpc47cKSvO6eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک نشان ملی علوم را دریافت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25208" target="_blank">📅 22:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25207">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d48Y3wtqYp3OoTiSlS0TYxauWqCJVk7sdzlgb0yQGQ9Uw-sYtluhjzF_s7QxV5bv2mZI6W8RwlR5bDgbAEMm6PU8yZOpCH6-bNKjGoz7BFS-KGgXeYREdQ2c92U9J1lW8jooqThImm3eEpFzcCfcRqye4L3oQcxJaDyjVoF74gSbNlfiDG4uqy1-YBHie_t2UEt_r_MfSAM_Hdmj3_lmwphKafyYlkEmlaxj-cCyyF0hjgw2I2ZzA14bBMtG4M6oeDtDD0BlMCWjjZRq-TZtRDDOBbf7khtdJJRjBqfhxBEMxBzOtSr4nnQMqocmne_qwQHCobRD0XE19y811Hn0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان و پوتین در حاشیه اجلاس سران کشورهای مستقل مشترک‌المنافع و اجلاس محیط‌زیستی دریای کاسپین در ترکمنستان دیدار و درباره
تقویت همکاری‌های اقتصادی و راهبردی در حوزه‌های انرژی، کشاورزی، حمل‌ونقل و تجارت
گفت‌وگو کردند. دو طرف بر تسریع اجرای پروژه‌های مشترک و گسترش همکاری‌های دوجانبه تأکید کردند.
خبرگزاری تاس: پوتین در این دیدار وضعیت خاورمیانه را
بحرانی و حاد
توصیف کرد و گفت روسیه آماده است برای مدیریت بحران و بازگشت ثبات به منطقه، در کنار ایران باشد و از تلاش‌های تهران برای پایان دادن به درگیری‌ها حمایت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25207" target="_blank">📅 21:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانال ۱۴: مقام‌های سیاسی و امنیتی اسرائیل نشانه‌هایی جدی از احتمال ازسرگیری درگیری با ایران مشاهده کرده‌اند و به همین دلیل ارتش خود را برای شرایطی آماده می‌کند که ممکن است به سرعت به یک درگیری گسترده تبدیل شود
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25206" target="_blank">📅 21:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایلان ماسک
:
ایلان توماس ادیسونِ دوران معاصر ماست.
@WarRoom
یاشار : الان خرابش کرد یا تعریف کرد؟!</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25205" target="_blank">📅 21:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25204" target="_blank">📅 21:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fceaa00395.mp4?token=QbSG7gk3zhCXcUjmTxroLos-U8Dk19nTIQdXIjF_jWPxh9a1zH3H3SZ6JhEEyEry18oHcTHh099alADgzOa9I2F0SoUamRPto_pn-ojeOjOjX-3UC2FtOarWeVsDTraC3tD-vvZQQQfPK9owpgHT7tajw2bltRF8GzMOEtsq71qN-CCt6XyvXxs5W0eisWwdZ9QstVDpcT83aimXSBRfA4bEV8YGPwGrvheQ1xaeVzl5Cq-UamwEivie_JM9YqE1hqZHtWZuQAAg61Ncv4jucutdP6RVGqOaPzSPwCzmmobOLODxX2VLjbBiLwlvsiI-1PaViIrBl2UBBm3nI63fsF9HeOagJc1fZ4D8tSkkWJlUf65kVsxRcg7uJqBwOXKGC1b3NoCd9iHemq3X7E5RUnSTsusYrZwLFueba_YhvJlllSg_69pJ0XfneG_QQEBXpGePqiYjRFMFsxyVNTv0sUoXqTbEQ4F0qBUT0h0R0QRWYZCYpzFPwPPsAV353H0yhNlVQP8eHqMoIOyZBmpe7AWlAP8-GAI6V7Y_uyqGNViW3Ja3Y2wnZ3LKLvy1THIS4D2eCUJHgLcnIHRFyDNKaM-Tch8zCCr83jxEnkJ8bHwcXRANC_szhxfWlaVpke392emohRYESZL5mvn2NP-9KwVZLuxSB0ZdloLhHM3cujI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fceaa00395.mp4?token=QbSG7gk3zhCXcUjmTxroLos-U8Dk19nTIQdXIjF_jWPxh9a1zH3H3SZ6JhEEyEry18oHcTHh099alADgzOa9I2F0SoUamRPto_pn-ojeOjOjX-3UC2FtOarWeVsDTraC3tD-vvZQQQfPK9owpgHT7tajw2bltRF8GzMOEtsq71qN-CCt6XyvXxs5W0eisWwdZ9QstVDpcT83aimXSBRfA4bEV8YGPwGrvheQ1xaeVzl5Cq-UamwEivie_JM9YqE1hqZHtWZuQAAg61Ncv4jucutdP6RVGqOaPzSPwCzmmobOLODxX2VLjbBiLwlvsiI-1PaViIrBl2UBBm3nI63fsF9HeOagJc1fZ4D8tSkkWJlUf65kVsxRcg7uJqBwOXKGC1b3NoCd9iHemq3X7E5RUnSTsusYrZwLFueba_YhvJlllSg_69pJ0XfneG_QQEBXpGePqiYjRFMFsxyVNTv0sUoXqTbEQ4F0qBUT0h0R0QRWYZCYpzFPwPPsAV353H0yhNlVQP8eHqMoIOyZBmpe7AWlAP8-GAI6V7Y_uyqGNViW3Ja3Y2wnZ3LKLvy1THIS4D2eCUJHgLcnIHRFyDNKaM-Tch8zCCr83jxEnkJ8bHwcXRANC_szhxfWlaVpke392emohRYESZL5mvn2NP-9KwVZLuxSB0ZdloLhHM3cujI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : عموی من، دکتر جان ترامپ، از سوی دولت آمریکا مأمور شده بود گزارشی درباره نیکولا تسلا تهیه کند.
آنها می‌خواستند بدانند: آیا او واقعاً وجود داشته یا نه؟ آیا واقعاً یک نابغه بوده یا نه؟
عموی من، پس از مدت نسبتاً کوتاهی، به این نتیجه رسید که
تسلا واقعاً یک نابغه بزرگ بوده و از هر نظر کاملاً واقعی بوده است.
وگرنه مجبور بودید اسم شرکت خودروسازی را تغییر بدهید.
حالا اگر من آن گزارش را تهیه می‌کردم، ایلان، شاید می‌گفتم: «آن‌قدرها هم خوب نبود.»اما عموی من آدم متفاوتی نسبت به من است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25203" target="_blank">📅 21:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ece6af3331.mp4?token=bMSLixKnPOIkBCj0z4f75tyv6CiLP-2t9lN-NcAAyGQv2VleaAYEOeOcfwktOQ1YLxmzWK9p1KyW8L0Azh0IzhLTI2UlhqYEP82VXL4hBN-sLDsdsFJ7KPQsaDCXd3o4oGdzdD8i1oQkw21ae6_bG50EeI9JHJoENRpuRXzcOT4U3BbOVzJV0ssyi4epcBHXPDFbRx6oaPIvPQgrGIemPNh-izOJzgUqf6rM8IfEI0MCmn_eLnrE6T9iADOidlQONO3RSV94tdK89Lzp6utQhHsYLGDtdKXtGSSOzXHjsGMYQBw0Md1VIoCmMd49FdlPoYioluNW9NH1dFdrzy932A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ece6af3331.mp4?token=bMSLixKnPOIkBCj0z4f75tyv6CiLP-2t9lN-NcAAyGQv2VleaAYEOeOcfwktOQ1YLxmzWK9p1KyW8L0Azh0IzhLTI2UlhqYEP82VXL4hBN-sLDsdsFJ7KPQsaDCXd3o4oGdzdD8i1oQkw21ae6_bG50EeI9JHJoENRpuRXzcOT4U3BbOVzJV0ssyi4epcBHXPDFbRx6oaPIvPQgrGIemPNh-izOJzgUqf6rM8IfEI0MCmn_eLnrE6T9iADOidlQONO3RSV94tdK89Lzp6utQhHsYLGDtdKXtGSSOzXHjsGMYQBw0Md1VIoCmMd49FdlPoYioluNW9NH1dFdrzy932A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : می‌خواهم به شرکت اسپیس‌ایکس بابت بازگشت ایمن فضانوردان مأموریت شماره ۱۲ از ایستگاه فضایی بین‌المللی، که چند ساعت پیش اتفاق افتاد، تبریک بگویم.
تصور کنید اگر همه چیز به این خوبی پیش نمی‌رفت؟ آن لحظه خیلی خوشایند نخواهد بود. فکر می‌کنم شاید ایشان اینجا نبودند.شاید شما هم اینجا نبودید. اما همیشه برای ایلان ماسک همه چیز به خوبی پیش می‌رود، نه؟ ما به شما افتخار می‌کنیم، به شما خیلی افتخار می‌کنیم، شما یک گنجینه ملی هستید
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25202" target="_blank">📅 21:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اکسیوس: سرلشکر ایال زامیر، رئیس ستاد کل ارتش اسرائیل، روز سه‌شنبه به مقام‌های ارشد آمریکایی هشدار داد که
اگر جنگ با ایران طی سه هفته آینده از سر گرفته شود، اسرائیل ممکن است مجبور شود انتخابات ۲۷ اکتبر را به تعویق بیندازد.
زامیر همچنین هشدار داد که ایران ممکن است در پاسخ به حملات، اسرائیل را با موشک هدف قرار دهد. این هشدار پس از آن مطرح شد که مقام‌های آمریکایی او را در جریان آمادگی‌های نظامی برای ازسرگیری عملیات علیه ایران قرار دادند.
ترامپ پس از آن اعلام کرد که
آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/25201" target="_blank">📅 21:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk7ScYfYb7owGFhPXxCA8WLhyjpXVpNkytf4akE96BV3hatWTrDuthgawlWc3DOywTKmFYtyzO1H45mfK-qN3zYUPwhRghHcIT0uVfPO_a7CsmKlIIzLxmWVKT8GDa2wjdQZhsJw_zrIOgg7Zge75JjNerir8eOq80BdMwyR9swWteUJj2yJ-iwhwVB9TNGJP83rzorZ0P6hm9fBv0cS2W_fgI4chBpmlwjSvRYa4dMebKayLk6iBYuE7s00FK8enKzDu-2PjFfnaMLs29MMor3mafR8bEUwlj271qKb9ZDSq7_wv-bfv_W4AETVvZWY6JO8VQM6gMVqgQYHGUYlog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ما در حال انجام گفت‌وگوهای سازنده‌ای با جمهوری اسلامی ایران هستیم. می‌خواهم برای همه روشن کنم که، با وجود اینکه ایران هم از نظر اقتصادی و هم از نظر نظامی در وضعیت بسیار بدی قرار دارد، و با وجود اینکه محاصره همچنان با تمام قدرت و به‌طور کامل ادامه خواهد داشت، در حالی که نفت با رکوردی از تعداد بشکه‌ها از تنگه هرمز عبور می‌کند؛
تنها دیشب ۲۲ میلیون بشکه نفت عبور کرده است، بدون اینکه حتی یک بشکه از ایران آمده باشد یا به ایران رفته باشد!
ما پیش از انتخابات میان‌دوره‌ای آمریکا که در ۳ نوامبر برگزار خواهد شد، به هیچ‌وجه به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25200" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا: دفتر کنترل دارایی‌های خارجی آمریکا، ۱۲ کشتی و شرکت‌های مالک و اپراتور آنها را به‌دلیل انتقال نفت و محصولات پتروشیمی ایران تحریم کرد. به گفته خزانه‌داری، این کشتی‌ها
صدها میلیون دلار نفت و فرآورده‌های نفتی ایران را به بازارهای خارجی منتقل کرده‌اند
و درآمد حاصل از این صادرات به تأمین مالی برنامه‌های تسلیحاتی، نیروهای نیابتی و نهادهای امنیتی جمهوری اسلامی کمک می‌کند. کشتی‌های تحریم‌شده شامل هوت، اوشن کوی، نورث استار، فلیسیتا، آتیلا ۱، آتیلا ۲، نیبا، لوما، رمیز، دانو‌تا ۱، علا و گس فیت هستند. شرکت‌های هدف نیز شامل پوروس مریتایم ونچرز، اوشن کادوس شیپینگ، میسترال فلیت، وست مِرین، بهنگام تدبیر قشم، پاروس مریتایم، وانسا گس شیپینگ، گلدویو مریتایم سرویسز و ایتاکی مریتایم اند تریدینگ هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25199" target="_blank">📅 20:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25198">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش ویژه فاکس‌نیوز : گزارش‌ها حاکی از آن است که پنتاگون به «فرماندهی مرکزی ایالات متحده» (سنتکام) دستور تایید داده تا تدارکات لازم برای عملیات‌های رزمی گسترده و حملات علیه ایران را نهایی کند؛ گفته می‌شود که این برنامه‌ریزی‌ها پیش از انتخابات میان‌دوره‌ای…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25198" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش ویژه فاکس‌نیوز : گزارش‌ها حاکی از آن است که پنتاگون به «فرماندهی مرکزی ایالات متحده» (سنتکام) دستور تایید داده تا تدارکات لازم برای عملیات‌های رزمی گسترده و حملات علیه ایران را نهایی کند؛ گفته می‌شود که این برنامه‌ریزی‌ها پیش از انتخابات میان‌دوره‌ای در جریان است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25197" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا : دو مرد لتونیایی است که در نزدیکی پایگاه هوایی سلطنتی مولزورث بازداشت شده‌اند. پلیس متروپولیتن ابتدا آنها را به ظن ورود غیرقانونی به یک مکان ممنوعه بازداشت کرد، سپس هر دو را طبق قانون امنیت ملی به دلیل ورود به یک مکان ممنوعه با هدفی مغایر با منافع بریتانیا دوباره دستگیر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25196" target="_blank">📅 19:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25195" target="_blank">📅 19:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سنتکام: فرماندهی مرکزی آمریکا امروز در یک نشست مجازی با شرکای بین‌المللی حمل‌ونقل دریایی درباره وضعیت تنگه هرمز گفت
افزایش تلاش‌ها برای تضمین آزادی کشتیرانی و تردد امن کشتی‌های تجاری ضروری است.
دریادار برد کوپر، فرمانده سنتکام، از حمایت مستمر صنعت کشتیرانی و نهادهای دولتی آمریکا تشکر کرد و به خسارت‌ها و فداکاری‌های خدمه غیرنظامی در پی حملات ایران اشاره کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25194" target="_blank">📅 18:53 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

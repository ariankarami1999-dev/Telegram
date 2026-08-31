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
<img src="https://cdn4.telesco.pe/file/cJO19A6IzfvX049P0y6pA63IOKu9793AjR1A1wLefh7s01YQkw6j5rcv1EFTAy7Q-Ppv0qhAz_ci_GnlyOI1o9Wp91r51lZd-QNv-UmsBKA76G1LHFDgeQyB4Dx8GoWMc1YIySieXeaU05C_hGyuX7_t7uHpTZSMQRdqpXXWMdUY0QLnp9OksttlEs9p7IxZly50fGZISqYGsx2ECL6-xZI1TS7Qk1j7-iUtfGl2EKokNmnUgAMtVirfplNozz38XA-MiiQH0yVCrOhprQjCOezwyTHnJsv_TVROgrHF5uglQzm31nVvs3fdAVb1NpBx3EH741TE5FbhX4b25iLpnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-20376">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKbPJbTQbqzL5cSstZkr56Px5qKX1JsfFSBl5skxwf2H7UkiwVbT7kf6vo9cxZmRJ3GGMY-46D4ffRneAI9JqY1Wx8f-C-U4L35foxvz_KhphH9Scfk0XBKJgaXDxJFUpFHuYpTcXAgcPvBa1TBX_xem7COfidFCOlYK15M3GwR6uee06x7JsWejtEYIIjxKQK-wm_yrthfcSZANZmZUurkXVCjCGBBvjm4cVtuiHipnrUuNQvFCgkgagQhxgSc5j8BBVVkfRbgAXLeaJ24a3_qRwPUnK6O7C8GWUNfIGpQ8FSNxA_vRbYVRRUZbuzbXQuNYvSmeC5kY0zWyYdkviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SBoxxx/20376" target="_blank">📅 19:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20375">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دادگاه مرکزی کیفری عراق، امیر رحیم جبار لازم، عضو کتیبه‌های حزب‌الله وابسته به ایران، را به دلیل گروگان‌گیری روزنامه‌نگار آمریکایی شلی کیتلسون، بر اساس قانون ضدتروریسم به ۱۵ سال حبس محکوم کرد.
کیتلسون در ۳۱ مارس در بغداد ربوده شد و پس از حدود یک هفته، در ۷ آوریل آزاد شد.</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SBoxxx/20375" target="_blank">📅 19:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20374">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسکات بنت:
به دلیل محاصره، تنها 30 میلیون بشکه نفت ایران روی آب باقی مانده است - بنابراین حتی اگر آنها بتوانند از چین پول دریافت کنند، این مقدار تمام خواهد شد.</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/20374" target="_blank">📅 19:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20373">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شمار کشته های حمله شب گذشته آمریکا در لارک به ۳ نفر رسید
خبرگزاری تسنیم:
در پی حمله شب گذشته آمریکا به نقطه‌ای در جزیره لارک، ۲ نفر به شهادت رسیدند و چند نفر نیز مجروح شدند. مجروحان این حمله برای مداوا به بیمارستان منتقل شدند که ساعاتی بعد، یکی از آنان نیز بر اثر شدت جراحات به شهادت رسید.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/20373" target="_blank">📅 18:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20372">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«ایران تحریم‌ها را بسیار جدی گرفته است. رهبران ایران از وضعیت اقتصادی کشورشان شوک‌زده شده‌اند.
ما شاهد صف‌های ۳ تا ۴ ساعته در جایگاه‌های سوخت ایران هستیم.
ایران به دلیل از دست دادن توان اقتصادی خود، به اقدامات نظامی روی آورده است.
می‌خواهم از اتحادیه اروپا بابت حمایت آن از عملیات موسوم به «Economic Outcast» تشکر کنم.
خبرنگار: آیا بازه زمانی مشخصی برای فروپاشی اقتصاد ایران وجود دارد؟
بسنت: لازم نیست اقتصاد ایران فروبپاشد؛ فقط کافی است حکومت ایران به خود بیاید.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/20372" target="_blank">📅 16:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20371">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سرتیپ ابوالفضل شکارچی، سخنگوی ارشد نیروهای مسلح ایران: صدها نیروی آمریکایی در طول جنگ کشته و هزاران نفر زخمی شدند
➡️
در این جنگ نابرابر، نیروهای مسلح ایران با استفاده از تاکتیک‌های جدید و نامتقارن در مقابل توانایی‌های فوق مدرن آمریکایی و صهیونیستی صف‌آرایی کردند و ضربات سنگینی به دشمن آمریکایی-صهیونیستی وارد کردند.
➡️
به عنوان مثال، هر زمان که یک پهپاد ۴۰ هزار دلاری ایرانی به سمت اهداف آمریکایی یا صهیونیستی پرتاب می‌شد، ارتش آمریکایی-صهیونیستی از چهار موشک به ارزش هر کدام ۴۰ میلیون دلار فقط برای رهگیری آن استفاده می‌کرد که نشان دهنده میزان خسارت مالی وارد شده به دشمنان آمریکایی-صهیونیستی توسط ایران است.
➡️
با وجود این هزینه‌ها برای آنها، پهپادها و موشک‌های بالستیک ایرانی همچنان از لایه‌های دفاعی آمریکایی و صهیونیستی عبور کرده و به اهداف مورد نظر خود در پایگاه‌های آمریکایی و سرزمین‌های اشغالی اصابت می‌کردند.</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/20371" target="_blank">📅 16:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20370">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ به فاکس‌نیوز:
ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد!
ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/20370" target="_blank">📅 16:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20369">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">میگویم اینکه خارج نرفتیم به این می ارزید که موقع برگشتن زیر تیغ «حافظه تاریخی» نرویم!
سبحان الله !</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20369" target="_blank">📅 11:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20368">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD7K9TuFqPPd63buoFVhGAZfXFQoVvVDGRvD5qzHe3wtJOsjp3n5fw8yWXGaZZeXczMfVOg4-IES-6jxr-hol_vl9HoCsbVN4_5q1zWmnvCWEE0xl0I6wITfdQVtY4CNMM0t6YsguiVQ4cQU3XivE8zemCFItpy30xu-7ZnFsIy7Nm2kJUYPV1bBPQ-NYg9POyM0PnPtkykmpJs3LuSQ3divnqx_0sBAaRC61TUdQR4n87eO9-lbK0Ql1fRcRQyfOXWdVwqX16MV_fDyITuO9XqRfLCVTZM7MFwp92J-FrV7VJIGIoesnbyLhjqIH07LMyQjSGc-upQAp5V1Zb6xJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20368" target="_blank">📅 10:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20367">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امارات متحده عربی اعلام کرد که با یک پهپاد که از ایران به سمت آب‌های این کشور پرواز می‌کرد، مقابله کرده است.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20367" target="_blank">📅 10:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20366">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9mdvIx88l6v3fa7jQuDBP_Vaeq6Xqg0t6paYjYyu-QixPRJLBuPaMv_4dZXSlcAIGd9qYWfYSpUCpXn22EeZOB_UJ2thal9dznfKXypasg3IKwDGD_B5y_NRp91nfV31I7ygAPz1AXquypv5S9mx4x_AjAD2Y5bRmOoPLVcEsNCDzmq0g73iDCoRXbvF9ZITtU80NIgHwVciDSBJ5v-mC5v1n97q8FDUC3IdEj15WXRJpCJQgpfy9j2lJoGhtvohdNSqigJeAnQEyrVw4ymjlU-81vFS1Wd6GxS9CAilgJjcIXr0JdluOFZZl3yDxFHqopW75LPQ8XXrhPuK5yKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20366" target="_blank">📅 09:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20365">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔺
پایگاه آمریکایی «المنهاد» در امارات هدف پهپادهای ارتش
🔹
ارتش جمهوری اسلامی ایران، محل استقرار بالگردها و نیروهای آمریکایی در پایگاه «المنهاد» امارات را مورد هجوم پهپادهای انهدامی قرار داد.
👤
روابط عمومی ارتش:
🔸
از بامداد امروز در پاسخ به تجاوزات اخیر دشمن متجاوز و در انتقام شهدای دلیر سپاه پاسداران انقلاب اسلامی و مردم بی گناه ایران اسلامی در جزیره لارک، ارتش جمهوری اسلامی ایران، محل های استقرار بالگردها و نیروهای ارتش کودک کش آمریکا در پایگاه «المنهاد»  امارات را با شلیک دهها پهپاد انهدامی، هدف قرار دادند.
🔸
پایگاه المنهاد، یکی  از مراکز مهم پشتیبانی و جابه جایی هوایی نیروهای خارجی است.  روابط عمومی ارتش، با اشاره به تجاوز اخیر دشمن به جزیره لارک، اعلام کرد، رزمندگان ارتش جمهوری اسلامی برای تامین امنیت پایدار و حراست از سرزمین ایران اسلامی تا رفع تهدید دشمن از متطقه، ایستاده اند و انتقام خون همه شهدای جنگ تحمیلی را از نیروهای ترویست آمریکایی خواهند گرفت.
☑️</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20365" target="_blank">📅 08:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20364">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT01cubN4hDkulswatyBeoLNSWNJoRfslygyNZoP8ij4p3rJpVROjEOOapDWAm-ayUfdD4BXYADBotzh3OWpjZ9qrxqNgOqSDZQF63h89VPQhUMuBQs2Ef2-fzZGLPQvb7bg--Cx4AHvZtHuI0-hj58ZHbepqpaCeDOd3lU1YamdJv7ZM5vocs6IezR8UV6u-e61NBleT037QjEiAOrhS7V8Yquv5CZn67QW4bUnym1JKHH2FkwJvGvqZsZpIWRJAsrYlAujwfpKnZgNN4jCVQxhZ1bxzwKsfV2FI1Dzgx7WxwCcqKrnH_sROZ9DG5NPAhG3aEP10ZgVAOEnUG3dIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20364" target="_blank">📅 07:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20363">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:
دور جدید عملیات نظامی ما در ایران تازه آغاز شده است</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20363" target="_blank">📅 02:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20362">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش هایی از حمله ایران به قطر</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20362" target="_blank">📅 01:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20361">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مدیر Secret Box بر این باور است که این تنش‌ها هنوز به جنگ نهایی موج ۵ ختم نمی‌شود و چند هفته ای دیگر زمان داریم.
لذا اگر تن ندارید لااقل آماده باشید.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20361" target="_blank">📅 01:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20360">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ادامه پرتاب موشک ها از ایران</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20360" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20359">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20359" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20358">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دلار ۲۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20358" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20357">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار در جزیره ایرانی سیریک</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20357" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20356">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارهای پی در پی در اردن</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20356" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20355">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20355" target="_blank">📅 01:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20354">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoDDrS8_d_pr47CwLhdHwA9532QeZ73gLAOW4k64nJWsb03VplPQd2Ec_rFM5m31ovexct6NiLExiAN89iDGvHMkpy5WUHVJ_t1Aw4ZFc-32pXkbVz28j4FZF6u5qhYhuTQTjqt13ZEs-gEc-JNZliagJoYMmJGEMkmHiioADABPHT5mF3wmGdPNCPlUkQREB3RbJgYgIHLllhzrcT_HWxC1qXlby-CdZGKFXOzhNfoxxwYvaRey5Wzt5dxmAaguAFJhP3rmHb-cPH9j4d6rwSvlX-QGLDCm8LHwcp0J4tD_IHkCMMdLyMoHhjEX4yxpCzNlYKBXCtqvx-mS6xHPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین کشورهای هر قاره جهان
بر حسب مایل مربع</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20354" target="_blank">📅 00:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20353">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBs6tW2uFJRftrsG8gfOewIx5lavmS6ON76_meHFyc1kthQ7qAdLkOLkpboxqNMEKO91OqBK42aajxzffwOgIKpBU1CLdu_W3dYCfY_xr2WAV_ctNm0XxK1yVX98Z6RurEYngomBMWdLoaIUanCvL5ddRsOVhIz07XN0rOACtb81dHQFZEYRHvuo1rZLqqsowGAOl6zU5iG6MlnXe71xzzTmlZeW7ZuySx2u_XlP9m1kJhB5rF6CwgPIBUXbdLwD6zbHmNlCmMHUAeDxFuNbQKDCKgZiJtPmOxNZunEVXKawPxSeH35TdqtgmD-n8-CtSIJySRUadtDLhVI9KXp92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20353" target="_blank">📅 00:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20352">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20352" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20351">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbejuLsmUUuppNE91VWc9I9lPm4Hosjt-wDLDTFSakJsu7f3YkJADt8GMFq_9htaJKShiVr2Q-8h0tdQ29tApkqDhInSq1RhAhHH1bLbUKryO7EReF1HeNWVyvRlX_4KaOfdoMJlopGd7mvLNRv_xfTPAnM_V3tc8JESiZXSWjuR8WwxFygGRhK95tw1v4HEU9JhL7gTsV6wE3D8Vx6MV5dZZDgfO82nPzDWKFSSIq84scXH5LO6RK8XVWSl2KlfDk4uVWVcDXkSIJlwp2T5By8hI9H8QZHAGCyZID3KARk0-5BF-lh8QIGXcOUt5ZHzCD9FXl8Da9QORBrDix_p4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20351" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20350">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20350" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20349">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اخباری دال بر شلیک موشک از مناطق مرکزی ایران!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20349" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20348">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اخباری دال بر شلیک موشک از مناطق مرکزی ایران!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20348" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20347">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">برخی منابع خبر از کشته شدن 70 نفر در حمله آمریکا می دهند که به نظرم اغراق آمیز است.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20347" target="_blank">📅 23:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20346">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجار دوباره در جنوب کشور!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20346" target="_blank">📅 23:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20345">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20345" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20344">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وضعیت خریداران نفت در شرایط کنونی</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20344" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20343">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13228b50c6.mp4?token=BAjGjmpaF7CxsjrcvoKp1YPiAei8zyCUmt4u1g0REyjo-5Rg9vZ86zcEvUUnmMSf_RmK_wlvRa2VMAzc7mj0SUjlH9t-pl3tdUYyWQgdZ9SVVG7djmCvLVuCJVmeHkIPlvGhd7Mr64dXxGU8PR3snYFvpZGqxAFjNMXyrUrMsztTtwHgs7l1muJGosxDv6DcuKpHh9-bRX12U5wlkAqa9WUIZjjxk-rejOk9JdZqXEkHDl1ivF3nHNm7urDQlFLEIdjwq2Tb6NLbd2fQS-YOabeAM086DWixv1m8m_wVDeFmav7Ld4s30qrYRABH8RvLH31tetMYhnQ0LLVxEgnmbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13228b50c6.mp4?token=BAjGjmpaF7CxsjrcvoKp1YPiAei8zyCUmt4u1g0REyjo-5Rg9vZ86zcEvUUnmMSf_RmK_wlvRa2VMAzc7mj0SUjlH9t-pl3tdUYyWQgdZ9SVVG7djmCvLVuCJVmeHkIPlvGhd7Mr64dXxGU8PR3snYFvpZGqxAFjNMXyrUrMsztTtwHgs7l1muJGosxDv6DcuKpHh9-bRX12U5wlkAqa9WUIZjjxk-rejOk9JdZqXEkHDl1ivF3nHNm7urDQlFLEIdjwq2Tb6NLbd2fQS-YOabeAM086DWixv1m8m_wVDeFmav7Ld4s30qrYRABH8RvLH31tetMYhnQ0LLVxEgnmbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کانال نزدیک به جریان تندرو:  بر اساس آخرین اطلاعات دریافتی، نیروی دریایی سپاه و ارتش در کنار هوافضای سپاه پاسداران امریه‌ای بسیار مهم دریافت کرده‌اند.   این امریه که از دفتر فرماندهی معظم کل قوا صادر شده به یگان‌های رزمی در تنگه هرمز دستور داده است که حتی…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20343" target="_blank">📅 23:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20342">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک کانال نزدیک به جریان تندرو:
بر اساس آخرین اطلاعات دریافتی، نیروی دریایی سپاه و ارتش در کنار هوافضای سپاه پاسداران امریه‌ای بسیار مهم دریافت کرده‌اند.
این امریه که از دفتر فرماندهی معظم کل قوا صادر شده به یگان‌های رزمی در تنگه هرمز دستور داده است که حتی اجازه عبور یک قایق ماهی‌گیری را هم از تنگه هرمز ندهند، هیچ مجوزی به هیچ طرفی داده نشود و هر طرفی که از دستورات صادره تخطی کرد، هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20342" target="_blank">📅 23:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20341">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چرا می خند؟!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20341" target="_blank">📅 23:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20340">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اسمان ایران و منطقه  @Piknikanalyst</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20340" target="_blank">📅 23:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20339">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e_Ao82sr4KsKmuCuxXzB3eHiUXJBM3u19uAhVYOc8RzyrqMV8mHYHZYsRGe64GkR_BYFAM0eH4_ACc_U7UVPyZYvF-B8DNa8m_KGAdAmom8Z42dUIF4Fv0YW6yINfd0wlyTBdBFdNmGojP78u6rmuXzePRPGw-p8sp_pwINL2f2ZwAFMvWoXM5905Vqt8_LVDadpgDh9pCc1QIMrEBG8_cNoNQmVb5vmw3HLfRcuQARe3ZWzEYPyOZ3akO2UcfenyOESV-ePc35GxMuLTTKOB1o3K8LBoEUqK28wrpuzQpqpTqybPN09pL19ZFmX2misSeyQyA2tM8hsNxve3bPOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمان ایران و منطقه
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20339" target="_blank">📅 23:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20338">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه: تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
روابط عمومی سپاه پاسداران انقلاب اسلامی:
دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی، در اقدامی تجاوزکارانه، با حمله به جزیره لارک منجر به شهادت و مجروحیت تنی چند از رزمندگان و هموطنانمان شد.
این اقدام توسط فرزندان ایران اسلامی پاسخ داده خواهد شد و تنبیه متجاوز را به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20338" target="_blank">📅 23:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20337">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnsdMZGt290spz_kckv_bF2_tFxo6_9JLBCEAJNOyEViBBk7dObk6rDIMrtJVYtlihaGiVhsrEhYKNn3atUmv0k1au7y3Co7H_2GkFpyjuo61DuItoburvtneekvbXHj-KbVq49tHSu9_swlW2acV4czgrlwCZWoHHdpNOsieBMYHe6r3c0pm9N1w0WNtuyF_o3CtN8VOuVwl3UdQWDGkwefqgOlZNxNVgp4W51SNDFB4U7_KKxNkzdOVVPiuw9ugK23VcdNibGPxIEmkZYpH1qZUD03r0Gh9KF9rXjz3QcXLZE17_rTcBK5akUrW9Gb8eg27w4lcvoOK9Wl-oETww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدافزارهای داخلی از آنچه می پندارید به شما نزدیک ترند....</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20337" target="_blank">📅 23:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20336">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مرندی :  رژیم ترامپ مرتکب اشتباه بزرگی شد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20336" target="_blank">📅 23:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20335">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این صوتی را عصر ضبط کرده بودم و اتفاقاً محور آن همین وضعیت سیال و پرنوسان خبری — خصوصاً برای یک ایرانی — است و جالب تر اینکه از مرندی (خریدار سنگین نفت و خالی کننده شبه جزیره عربستان) هم یاد کرده بودم...
برای هشتگ گذاشتن تاخیری حاصل شد و در همین فاصله دوباره جنگ شد و مرندی و ....
سبحان الله!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20335" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20334">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGkqHaARdpZvxMQjInPlTLLYdee0xecbDohXfTrcbKtArInR-QpbBZ6VSPtlnLmJcpT9WTauu63-ThWFXfrnbI1v10gfnRmvxCaCaldrl2Z5-XlhByBKVprMCsT3gXBAjjT_HwqfTmk7EA4-K0OOeMpTSnb0PcE3-p3P_cmqJeGFFP60KYQuA-l3F4uw_Scy4WvEL7C8UO8BGlesnnWeNqhdE0Vm3_AfnyIJNge-D9hFo8LlqTd3vb1izMFkWu1PVeZjG179OMBteh86HnhxHTqaVrE-UWFiql8DcRo_C5zmr43X1CvIULLhz_zGDLg5YVMykwnlOgVrorHdvI2ZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرندی :
رژیم ترامپ مرتکب اشتباه بزرگی شد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20334" target="_blank">📅 23:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20333">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رسانه عراقی به نقل از یک منبع ایرانی:   شهادت شماری در پی حمله آمریکا به جزیره لارک در جنوب کشور</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20333" target="_blank">📅 23:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20332">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کانال Secret Box بی تردید ناهمگن ترین کانال سیاسی فضای فارسی زبان تلگرام است!
از بسیجی مبعوث شده کف میدان تا شاه اللهی مخلص اسرائیل اینجا هستند!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20332" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20331">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب گویا لارک بوده نه خارک!  مقام آمریکایی به شبکه الجزیره اعلام کرد:    نیروهای این کشور امروز به یک پرتاب گر موشک در جزیره لارک حمله و آن را نابود کردند. مقامات آمریکایی اعلام کردند این سامانه آماده شلیک موشک به طرف تنگه هرمز بوده است.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20331" target="_blank">📅 23:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20330">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2967016a4b.mp4?token=NeJLBmpW4AUC_jhR9JOtmmrfL0crU8fpy5CojDC1J5Ww0od89Qk3on08wDVTqk3gryVrj3iDr7sZLOrtumMqREon-5xoFoTUMZr7KMe93lsCMdr8BnffeKDeC0SX4eBVTRkOekvDFEG3JV12TN_peAqa3sG-Yz6dJhCqwdHXeuVeu3cetc9cNeIGxvQN-Zz86JI5G4ys1mvSc7cdRR5kzGWA1J1gCfcEDL6DOpyK--px-W84Ep-LWwR5r7I-DnkZzrxAFYhz58muBhLL9FU2L4JER-RslF3YuKK_YhmJ2PUoHQMMflkNt9-hKjfFTvWZxTb2ztZBVlV-65ODmb7XHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2967016a4b.mp4?token=NeJLBmpW4AUC_jhR9JOtmmrfL0crU8fpy5CojDC1J5Ww0od89Qk3on08wDVTqk3gryVrj3iDr7sZLOrtumMqREon-5xoFoTUMZr7KMe93lsCMdr8BnffeKDeC0SX4eBVTRkOekvDFEG3JV12TN_peAqa3sG-Yz6dJhCqwdHXeuVeu3cetc9cNeIGxvQN-Zz86JI5G4ys1mvSc7cdRR5kzGWA1J1gCfcEDL6DOpyK--px-W84Ep-LWwR5r7I-DnkZzrxAFYhz58muBhLL9FU2L4JER-RslF3YuKK_YhmJ2PUoHQMMflkNt9-hKjfFTvWZxTb2ztZBVlV-65ODmb7XHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20330" target="_blank">📅 22:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20328">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتانیاهو :
طبق اسنادی که به دست آورده‌ایم ایران بار دیگر می‌خواهد برنامه هسته‌ای خود را از سر بگیرد و بمب اتم تولید کند و ما قبلا هشدار داده بودیم که اگر ایران برنامه هسته‌ای یا موشکی خود را دوباره شروع کند ما به آن حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20328" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20327">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اخبار تایید نشده از حمله هوایی آمریکا به جزیره خارک!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20327" target="_blank">📅 22:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20326">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حمله ایران به یک کشتی بحرینی در خلیح فارس</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20326" target="_blank">📅 22:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20325">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اخبار تایید نشده از حمله هوایی آمریکا به جزیره خارک!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20325" target="_blank">📅 22:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20324">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سناتور تد کروز:
چیزی که من خواستار آن هستم این است که رئیس جمهور ترامپ و دولت او معترضان را مسلح کنند تا مردم ایران بتوانند این کار را انجام دهند، کردها را مسلح کنند و به معترضان اجازه دهند این حکومت را از قدرت سرنگون کنند، نه با نیروهای آمریکایی در میدان، بلکه با مردم ایران.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20324" target="_blank">📅 21:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20323">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل طرحی را برای سرنگونی نظام ایران تدارک دیده است. در راستای این آمادگی‌ها، هزاران نیروی کرد به اسرائیل منتقل شده و سناریوهای عملیاتی مختلف را تمرین کرده‌اند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20323" target="_blank">📅 21:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20322">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سازمان رادیو و تلویزیون اسرائیل:
شناورهای جنگی ترکیه به کشتی‌های نیروی دریایی اسرائیل نزدیک شده و برای آن‌ها مسیرهای دریایی مشخص کردند.
نیروی دریایی اسرائیل سطح آمادگی خود را به منظور مقابله با هرگونه تحولی در دریای مدیترانه افزایش داده است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20322" target="_blank">📅 21:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20321">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20321" target="_blank">📅 17:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20320">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20320" target="_blank">📅 15:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20319">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315342d71a.mp4?token=Oj49VR4BjdXiJyuyGxlQJ2hGgiTDJwFtrMKbmjzwJsH8iXQp1l0CBYpbSRnePXVd9XMGar0gWDvs5jEazQfax7IOzlkmlJPUbigaf8x3_xY-xXxcj2I83YFsJb7rsCZqABzrcDTfcDalNym6xieFKUEUbEe8oNBuGMvxvwplI45XWTm-KAYwpI1C_HwxaxXw1l9G1wKF1obl4htvxlOFDmEjog1CE-UD9w19q0KT1JutO_nhSsgW6XmqZyR3urATQXpVwGGrphtfwmXKkp90m0CRzuvUYdi3wWHMxieef2GRniOo8gDXtA7_WtHIld9FI43CQGa7NtYr2edXD0UImg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315342d71a.mp4?token=Oj49VR4BjdXiJyuyGxlQJ2hGgiTDJwFtrMKbmjzwJsH8iXQp1l0CBYpbSRnePXVd9XMGar0gWDvs5jEazQfax7IOzlkmlJPUbigaf8x3_xY-xXxcj2I83YFsJb7rsCZqABzrcDTfcDalNym6xieFKUEUbEe8oNBuGMvxvwplI45XWTm-KAYwpI1C_HwxaxXw1l9G1wKF1obl4htvxlOFDmEjog1CE-UD9w19q0KT1JutO_nhSsgW6XmqZyR3urATQXpVwGGrphtfwmXKkp90m0CRzuvUYdi3wWHMxieef2GRniOo8gDXtA7_WtHIld9FI43CQGa7NtYr2edXD0UImg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتتاح یه خط فاضلاب
به مناسبت هفته دولت
اوج خلاقیت
فقط اون روبان قرمز روی شیر تانکر
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20319" target="_blank">📅 15:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20318">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVyti9NlwXoPQX-4ErZhbWx_Ye2dJ27PGwo6Pu5PlDtVM5ygh6Iz5ErHRFxAJVSu0o61A7sXfF8108crxojg0OmwsaVfq8ZC221u9wbjq82fou27XX3YvTtAggAR_ZGSFNTyC5p2KdUcyivKIyF_3pHVupe8bXm1-dvPAjgWt4_xHFFobjBdF8kjDYhfYukUc4UZN5xqxMSrzSsXhBRjR9vxG-spDt-iIJJ9PUYOWye4-0nQJWJ24Qxt5D3G_rDBbBLtHSpuPAw1e5a_Ai8UcfyuFA1xdRZ2M8_db3PhcIw6dwdTOfZ_sQmqDJK4g5Y0S6rksRgbVZqw_CGUq0qgaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور سرباز وظیفه در درگیری مرزی در پاوه
مهرداد طاهری آرپناهی، سرباز وظیفه اهل شهرستان کوهرنگ چهارمحال‌وبختیاری، در جریان درگیری با اشرار در منطقه مرزی پاوه ترور شد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20318" target="_blank">📅 15:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20317">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عراقچی:   ژاپنی‌ها آمریکا را بابت جنایاتش پاسخگو کنند</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20317" target="_blank">📅 12:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20316">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بیکاری هم بد دردی است.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20316" target="_blank">📅 12:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فوت ناگهانی، هنگام سخنرانی شبانه!
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد حین سخنرانی شبانه فوت کرد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20315" target="_blank">📅 12:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20314" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20313" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=DghCGsbkvS00nuH484Mg9pASttmTnWlWsjb2vRyZyqZBWHnuMZAtBO_yq5KBJ0QjOgxWfuU7v5AMMyT9j4tbEZvXLzpp095hpY5ej0UmX9MRP03q-FiMr1KXtOP5r9acajdxGz62Q3WUHh860MiSMOKJs5zjpdlwWV6GKOParMOoNsISIM77YjldaUlwiyKhbrr-1S9ViMY5OH9dVAEKx6tbfyDqvVspc8WiQvpCiU4enBpQvZCUmdTlFJCRQ5-UOAt8yW2KBPbv4kTCYvIX9X0MdbTF48_0zJIdnVc-xOOSD4eI3XIvZrjBN4qdyugmROHJ-yjvL1Cr5sik9OprJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345f73cdb5.mp4?token=DghCGsbkvS00nuH484Mg9pASttmTnWlWsjb2vRyZyqZBWHnuMZAtBO_yq5KBJ0QjOgxWfuU7v5AMMyT9j4tbEZvXLzpp095hpY5ej0UmX9MRP03q-FiMr1KXtOP5r9acajdxGz62Q3WUHh860MiSMOKJs5zjpdlwWV6GKOParMOoNsISIM77YjldaUlwiyKhbrr-1S9ViMY5OH9dVAEKx6tbfyDqvVspc8WiQvpCiU4enBpQvZCUmdTlFJCRQ5-UOAt8yW2KBPbv4kTCYvIX9X0MdbTF48_0zJIdnVc-xOOSD4eI3XIvZrjBN4qdyugmROHJ-yjvL1Cr5sik9OprJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/20312" target="_blank">📅 01:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=Vg1X8oI31fzbCuAI_lKUDxXqnyv9tmvAM7SE68ldiRt9da_kL2miGFol3PAom8s0Jgycd8FrUW6fEmAdBVMZ4eR7Oqb_VPP2xluRi83lFdRFuGmN_0J2PGJ6sx2ZpKRwgKTUl1VKHqdXVN62OXeuuQ1r_wfTZtylYh3FQI674UM8mn23rLKTtDL1Hi8Qz3yVmEs9DMQsKPZeQEc-0Qs7SO1oPby0uS_Pxeubd66CRFNbQRQxj3bbJ4D-3TDoh_43ymYckL8quCbSCxjf2DzXMyom80nQgTjjHTn7-crJu27NzjiPdEgeijwBluu89yrDEXlssnIZPb490-IkzC6NZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93dde0064e.mp4?token=Vg1X8oI31fzbCuAI_lKUDxXqnyv9tmvAM7SE68ldiRt9da_kL2miGFol3PAom8s0Jgycd8FrUW6fEmAdBVMZ4eR7Oqb_VPP2xluRi83lFdRFuGmN_0J2PGJ6sx2ZpKRwgKTUl1VKHqdXVN62OXeuuQ1r_wfTZtylYh3FQI674UM8mn23rLKTtDL1Hi8Qz3yVmEs9DMQsKPZeQEc-0Qs7SO1oPby0uS_Pxeubd66CRFNbQRQxj3bbJ4D-3TDoh_43ymYckL8quCbSCxjf2DzXMyom80nQgTjjHTn7-crJu27NzjiPdEgeijwBluu89yrDEXlssnIZPb490-IkzC6NZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما:
به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20311" target="_blank">📅 01:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKLy_O5-WPDj4U48Ss4h-pSQvqllMNZQ_7fxdylq7VaCg8M4AwiGgKeMHDVbwzs6IJ3KFfAh8WB_2fo6ZFZpnOWM21ngpXSdoKz6uXPnjJHJQVlDj5z2v-pfC6Akjkckbxl91Jpzhvg49O0tjpAlwrrim8ijJORHO1dvfFire2UV78Ri1-ndRcjdaKBv0Sesxr1gxSebj3rdslm512K1oqw-b7MMpA96s915_PcSktIA_AqgVX15BpMACC_uLSnYucLFS3D6Xiwxrc7i64sL68uKza6c25LPy-WeCTapexQOGuuRuGeWmTKGNt893EbchDtSeRqV9i5WdwIlYU64WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20310" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20309">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند  وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.  و آن درس چه بود ؟  ترس ها برای ایستادن در…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20309" target="_blank">📅 23:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20308">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند
وزیر امور خارجه امروز گفت: مردم ایران در جنگ ۴۰ روزه، درس بزرگی به جهان اسلام دادند که اگر با هم باشیم، می‌توانیم در برابر همه ظلم‌ها ایستادگی کنیم.
و آن درس چه بود ؟
ترس ها برای ایستادن در برابر شیطان بزرگ ریخته شد .</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20308" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20307">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">غریب‌آبادی:   هیچ کشتی‌ای بدون هماهنگی با ایران نمی‌تواند از تنگهٔ هرمز عبور کند   تنگهٔ هرمز کاملا بسته است و اگر کشتی‌ای از تنگه عبور کند قطعا با هماهنگی و مجوز ایران است.  نیروهای مسلح ایران کاملا بر هرگونه تحرک در تنگهٔ هرمز اشراف دارند و به‌هیچ‌وجه ادعاهای…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20307" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20306">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20306" target="_blank">📅 22:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20305">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌سرلشکر رضایی:  ضاحیه و بیروت خط قرمز ماست و هیچ‌کس حق ندارد به‌سمت بیروت و ضاحیه حرکت کند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20305" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa4pOm33ujjNoVcDmwEK6XQJAClti8JgLcWr0SuEALNSL3DaCSBL60uzp_RquVbc-ukeEZyzBh8TgeKQkJZwuOxeHNfeXvIT9s9Sl3vUpwxaCE-b2iJxgVZue8LQRRj_u-3YrBTSLidqQrEWBubsfSFC_a1DH6NRcFbfV3amc-OQQFYyw7Ius3TLjt-T95095dDGS-01dEffq_hfH-DJ505bzdZvGopw2ByIYh__l8WgMzad8EDjSX5IlqB7H98UAdT5DiBpUhJd5uWrXMAsGCocABXPdRZK1lcm3umHTD79FvV5X3HO4pLPCYboi1IRo7lRwYVy3U5Q1h7lH8ngHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه هشدار داده است که در پاسخ به حملات اوکراین به اهداف داخل روسیه با استفاده از موشک‌های کروز بریتانیایی، ممکن است به اهداف نظامی بریتانیا داخل و خارج از اوکراین حمله کند.  این هشدار، قوی‌ترین هشدار از این نوع تاکنون از سوی روسیه بود که توسط ماریا زاخاروا،…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20304" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!  علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20303" target="_blank">📅 18:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un19AVgl5Ap6ukce0l7knmJHLB-QLmMzHGuxKhQ2-X6fW7TdNMKXL_GOrkgSG3kTumiXWqID_Ge-LR4Ws3V24yUI_KnQhhAcoBvpA05pUOuKFA3GxXLnrEg4ARi7LhWO1J0pwutaRm9l6DuCpiEIBwwckUAP7c20Ra4Q1Vnx6a62A1tKS4dB-cHKRfTwzecwPs2QefFdIW9lM05v0OpkecSZWG3CPyO9bqpAKljLZ8ewSQwptz0_0J-sJ6Sk4qzRmD0kvyjRBui7La7sSTJyI4OgU3GAncI83yZGw2-h8QUGKiMccjykPouyBKdesIEwfEbInbsJlq01H9aad7Lveg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود آمریکایی ها یک مسیر جدید در میان جزایر عمانی باز کرده اند که میلیون ها بشکه نفت از آن عبور می‌کند!
علت سرکوب جهش نفت هم همین بوده است.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20302" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20301">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تحلیل اسرائیلی: اتحاد اسرائیل و یونان  بازدید رئیس ستاد مشترک نیروهای مسلح یونان از اسرائیل، اهمیت راهبردی روابط نظامی بین این دو کشور را برجسته می‌کند. با توجه به افزایش تنش‌ها بین اسرائیل و ترکیه، این همکاری اهمیت بیشتری پیدا می‌کند.  احتمال صادرات تانک‌های…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20301" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20300">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏پزشکیان:   اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.  با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/20300" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20299">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏پزشکیان:
اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند.
با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20299" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20298">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20298" target="_blank">📅 15:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20297">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6xQo37nNS0JB9y2m3LTvo4_yfZM2XH9xxqyepGV8D4EbGkjWdX0jGaunFMGGYVYEBi7rFY8Njdfzw5yIs-_1-1_Cq5oKkWwpwMcl5Qe5DLqgQYAGyUeHVKsu261qMBE9IaC0PnnISaxI85RHlA42nTXSWn7IBMBkw_ZIuCD4C491C_9LzQvqStITq0WzrG4mONjbgq8QHTMA_rSoLoKulg12Z0Ez9dMsLPTkj21CC90tIKfV3PRd2PROAxMBjyegtREjoywjtTZl_yWTkawc0JS4xFZ1DOY-9017Pa22ixoxuzjlXm4bwaEjVOu0uMkarTGTG2qeWXuI1D8kvFLJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی گفته عوامل دولت آمریکا دارند قیمت انرژی را دستکاری می‌کنند تا منافع شخصی بدست آورده و ترامپ را در قدرت نگاه دارند!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20297" target="_blank">📅 15:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20296">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20296" target="_blank">📅 14:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20295">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شورای شهر پایتخت کانادا در حال بررسی تغییر نام خیابان دونالد ترامپ، رئیس جمهور آمریکا است و در میان گزینه های جایگزینی «خیابان اوباما» و «خیابان تاکو» قرار دارند.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20295" target="_blank">📅 14:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKBitUt3U2V089cZbeppZaq_rDG-v2rgQCv6z1WsRe3DBnsFzkxZ46U9fOWPsZEod-PGdMYks1meTqneRT0qDjoVNkS0bcT6iD7cPMur2il3FsMstHg3O3cA97N1uDmsRgXi3MtoeO2TXqFTy9DwqtWoDMQ3JqTiRlxp1QgUk6WJPzdpBOHg8MEP9iuFIOQpcau2P7u5R1tK4QNY2iZ1DvwTb9lxA3PhTU98edDBLUcUIwgTmsKaKD0mbLAHoWibGIT7kOEErEOgB5D2JegwVD5xKcLl8p4xC62UBvNWuwsgKfgt2LYfRduAUo4pmRDi_FGJMB-vM799cCrLFeTjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/20294" target="_blank">📅 13:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20293">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=MLwLSiBsIsuRqG-Iy0OmWbaYAXS-sDbZsVHdxJb52l_fF4fTXYsEJXOvR7NqZJmrMvegD5dZhJI6Ir8I5Bn0Q_ZKsOWu3vZJ0hikDcvNo9YUHfWBJJrVAyVPgtUrnA0XF8s5yxo0mUsQd5IfawyMzN5E57ZhkRED9U4x5R-XhK0z8nzWybqmPuWD0plcR8Y6bH-iw09lbu_XfXcEuq8Pgak0BeoTBkWVxWGOIB7Qa5ytPfUGlsluZD5nyIAmldWT9Qs2Idi2k_Do_Fe-tw4zyDn_XcQETqZSnggHW79EsgrKPwyzfmZLIaBO3K3f8gnWHt_gQV_y4fYNomG_jvhnHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/421b4eca46.mp4?token=MLwLSiBsIsuRqG-Iy0OmWbaYAXS-sDbZsVHdxJb52l_fF4fTXYsEJXOvR7NqZJmrMvegD5dZhJI6Ir8I5Bn0Q_ZKsOWu3vZJ0hikDcvNo9YUHfWBJJrVAyVPgtUrnA0XF8s5yxo0mUsQd5IfawyMzN5E57ZhkRED9U4x5R-XhK0z8nzWybqmPuWD0plcR8Y6bH-iw09lbu_XfXcEuq8Pgak0BeoTBkWVxWGOIB7Qa5ytPfUGlsluZD5nyIAmldWT9Qs2Idi2k_Do_Fe-tw4zyDn_XcQETqZSnggHW79EsgrKPwyzfmZLIaBO3K3f8gnWHt_gQV_y4fYNomG_jvhnHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20293" target="_blank">📅 11:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20292">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb-u5W3W5Vv7uN3jNmAG_NXOCIoe0-rYtvW9CICUjmt8_kl1Ph7qbtKbr-3Sy9tYlM5jfP4FWsW7XL22t1c-5sxofNqH6UCew9QGAONoJMA9h_qEcEaWTdU221walADpiLMr_MU7Gh8fzfJG17Zrz6V_jbfoRgDkdNEoUPGCI3xqNG8AXqmvB2YDnIbsaj_Det2T_KW1qqMYrAv2ecVirDRVTBrk6WSMHpF2OnnZecxupEUS3b8_2Iz_68VvbImLix7B2pXm9hQmfe_in1IqWzM9TvcVFYYAz_1ZWaMqZnADJjlG5kihPoWRC-Z8kHUQYNPPi4TgLVRlszVNwFUnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
مواضع هاوکیش کوین وارش در نشست جکسون هول
مواضع هاوکیش کوین وارش در جکسون هول نشان داد اگر تورم با سرعت کافی به هدف ۲٪ نرسد، افزایش نرخ بهره همچنان روی میز است و فدرال رزرو لزوماً مسیر کاهش نرخ را ادامه نمی‌دهد.
بازار نیز این پیام را جدی گرفت؛ احتمال افزایش نرخ در سپتامبر از ۳۵٪ به ۵۶٪ رسید که می‌تواند به رشد بازده اوراق و دلار و افزایش فشار بر طلا و دارایی‌های پرریسک منجر شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20292" target="_blank">📅 10:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20291">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ:
ایالات متحده قراردادی با ونزوئلا امضا کرده است که به این کشور کنترل بخش عمده‌ای از ذخایر نفتی تایید شده، که بیش از 65 میلیارد بشکه است، را می‌دهد، و این کار بدون هیچ هزینه‌ای برای مالیات‌دهندگان آمریکایی انجام می‌شود.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20291" target="_blank">📅 10:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شلیک های متعدد در تنگه هرمز!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20290" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtjFXemrUMmW3qMRhSMl0KAfYVRymv6ySBrLYjGllfL6g1hsPp8vTObycn0U-cpB2FU3ZDiENE1mr6ePgDtSD9MwvRx60e1_lkqZorKhmqVIrwHxe2oHhjC8A6WC935cbg8cG47sGosQ4G7OF1ZgKNsFaBBToEcgd2bboYFvFEUsncpGSBelzD-kYcLXjs5o7Q6bwXlpJaGe70yXQRhe16H1OZ2KoL7byA-CNfutvgJYTv49G83Y9ZtnpY9GtKJjmEpecbFfwf-bNOjqbG9mZfwDjxOVhBlk2xCWi6F9oqD5GUrK-Gl1B0umu7Mq6qCwjkR5WGv0Lg9GDhZsme6FjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحول در پدافند لیزری اسرائیل  و تغییر احتمالی معادله بازدارندگی ایران
گزارش اخیر درباره پیشرفت‌های شرکت البیت اسرائیل در توسعه سامانه‌های لیزری، صرفاً یک خبر فناورانه نیست؛ بلکه می‌تواند نشانه‌ای از آغاز یک تحول راهبردی در موازنه نظامی خاورمیانه باشد. سامانه پدافندی پرتو آهنین  Iron Beam تاکنون توانایی خود را در مقابله با پهپادها و برخی تهدیدات هوایی به نمایش گذاشته و اکنون مهندسان اسرائیلی آشکارا از چشم‌انداز گسترش این فناوری به حوزه رهگیری موشک‌های بالستیک سخن می‌گویند. اگر این هدف محقق شود، ایران با یکی از جدی‌ترین چالش‌های راهبردی تاریخ معاصر خود روبه‌رو خواهد شد.
اساس قدرت بازدارندگی متعارف ایران در دهه‌های اخیر بر زرادخانه گسترده موشک‌های بالستیک و کروز بنا شده است. تهران به دلیل محدودیت‌های ناشی از تحریم‌ها و برتری هوایی رقبای منطقه‌ای، سرمایه‌گذاری عظیمی روی توسعه موشک‌های دوربرد انجام داده است. این موشک‌ها نه‌تنها ابزار حمله، بلکه ستون اصلی بازدارندگی ایران محسوب می‌شوند. در واقع بخش مهمی از محاسبات امنیتی ایران بر این فرض استوار است که در صورت وقوع جنگ، حجم بالای شلیک موشک‌ها می‌تواند سامانه‌های دفاعی دشمن را اشباع کند.
اما فناوری لیزری دقیقاً همین منطق را هدف قرار می‌دهد. تفاوت اساسی میان رهگیرهای موشکی متعارف و لیزر در هزینه و ظرفیت درگیری است. هر موشک رهگیر سامانه‌هایی مانند پیکان Arrow یا فلاخن داوود David's Sling ده‌ها هزار تا چند میلیون دلار هزینه دارد، در حالی که هزینه هر شلیک لیزری در مقایسه بسیار ناچیز است. به همین دلیل، اگر اسرائیل بتواند لیزرهای پرقدرت را برای مقابله با موشک‌های بالستیک عملیاتی کند، دیگر مجبور نخواهد بود برای هر تهدید از یک رهگیر گران‌قیمت استفاده کند.
اهمیت بیشتر این تحول در پروژه لیزرهای هوابرد نهفته است. برخلاف سامانه‌های زمینی که با محدودیت افق راداری و شرایط جوی مواجه‌اند، لیزرهای نصب‌شده روی جنگنده‌ها یا هواپیماهای ویژه می‌توانند در ارتفاع بالا به موشک‌های مهاجم نزدیک شوند و آنها را در مراحل اولیه پرواز هدف قرار دهند. چنین قابلیتی زمان واکنش را افزایش داده و احتمال موفقیت دفاع را بالا می‌برد.
البته هنوز موانع فنی مهمی وجود دارد و هیچ تضمینی نیست که رهگیری موشک‌های بالستیک با لیزر در آینده نزدیک به واقعیت تبدیل شود. اما اگر اسرائیل از مرحله مقابله با پهپادها و موشک‌های کروز عبور کرده و به رهگیری مؤثر موشک‌های بالستیک برسد، بخش بزرگی از مزیت راهبردی ایران زیر سؤال خواهد رفت. در آن سناریو، تهران ناچار خواهد شد برای حفظ بازدارندگی خود به دنبال راهکارهای جدیدی باشد، زیرا ستون اصلی قدرت متعارفش دیگر همان کارایی گذشته را نخواهد داشت. به همین دلیل، موفقیت احتمالی دفاع لیزری علیه موشک‌های بالستیک را می‌توان یکی از معدود تحولاتی دانست که قادر است معادله بازدارندگی میان ایران و اسرائیل را به‌طور بنیادین تغییر دهد.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20289" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">منابع اطلاعاتی سعودی اعلام کردند تا ساعات آینده، گروه های مقاومت عراقی به عربستان حمله می‌کنند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20288" target="_blank">📅 02:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خلاصه
یادداشت الجزیره | تحریم‌های جدید آمریکا؛ تلاش برای خفه‌کردن شبکه اقتصادی ایران، بدون ورود به جنگ مالی با چین
موج جدید تحریم‌های دولت ترامپ علیه ایران را باید فراتر از یک بسته تحریمی معمولی دید. وزارت خزانه‌داری آمریکا نزدیک به ۶۰ فرد و نهاد در ایران و چندین کشور دیگر را هدف قرار داده و تلاش کرده است شبکه‌ای را که به تهران امکان
فروش نفت، انتقال پول، خرید فناوری و تجهیزات، حمل‌ونقل و دور زدن تحریم‌ها
را می‌دهد، همزمان تحت فشار قرار دهد. اسکات بسنت، وزیر خزانه‌داری آمریکا، این عملیات را بخشی از راهبرد «خفه‌سازی اقتصادی» ایران توصیف کرده است.
نکته مهم این تحریم‌ها،
ماهیت شبکه‌ای آنها
است. آمریکا به جای تمرکز صرف بر شرکت‌های ایرانی، واسطه‌های خرید در چین و هنگ‌کنگ، شرکت‌های لجستیکی، کشتیرانی، شبکه‌های موسوم به «بانکداری سایه»، شرکت‌های مرتبط با تجارت نفت و حتی برخی فعالان ناوگان سایه ایران را هدف قرار داده است. این شبکه اکنون از ایران تا چین، هنگ‌کنگ، سنگاپور، امارات، سوئیس، مالزی، بریتانیا، فرانسه، یونان و چند کشور دیگر امتداد دارد.
هدف اصلی واشنگتن، افزایش هزینه هر مرحله از تجارت خارجی ایران است؛ به‌گونه‌ای که فروش نفت، انتقال درآمد، خرید تجهیزات و جابه‌جایی کالا برای تهران دشوارتر و پرهزینه‌تر شود. به‌خصوص شبکه‌های خرید فناوری دوکاربردی مورد توجه قرار گرفته‌اند؛ شبکه‌هایی که به ادعای آمریکا از شرکت‌های پوششی و واسطه‌های شرق آسیا برای پنهان کردن مصرف‌کننده نهایی تجهیزات استفاده می‌کنند.
اما
بزرگ‌ترین نقطه ضعف این استراتژی چین است.
آمریکا چند شرکت چینی و هنگ‌کنگی را تحریم کرده، اما از هدف قرار دادن بانک‌های بزرگ چینی که در تجارت نفت ایران نقش دارند، خودداری کرده است. این تصمیم اتفاقی نیست. چین بزرگ‌ترین خریدار نفت ایران است و اعمال تحریم‌های ثانویه علیه بانک‌های بزرگ این کشور می‌تواند پرونده ایران را به یک بحران مستقیم مالی میان واشنگتن و پکن تبدیل کند. بسنت نیز صراحتاً گفته است که نمی‌خواهد با این اقدامات «سیستم مالی جهانی را منفجر کند»
بنابراین،
مرحله بعدی تحریم‌ها تعیین‌کننده خواهد بود
: اگر آمریکا به سراغ بانک‌ها، پالایشگاه‌ها و خریداران بزرگ چینی برود، فشار بر ایران می‌تواند جهشی شود؛ اما همزمان خطر تقابل اقتصادی با چین نیز افزایش می‌یابد. اگر واشنگتن از این مرحله عقب‌نشینی کند، ایران همچنان می‌تواند بخش مهمی از نفت خود را از طریق شبکه‌های واسطه‌ای به چین بفروشد؛ البته با تخفیف بیشتر، هزینه انتقال بالاتر و درآمد ارزی کمتر.
در واقع، این بسته تحریمی نشان می‌دهد آمریکا تلاش دارد
تمام شریان‌های اقتصادی ایران را باریک کند، اما هنوز از قطع مهم‌ترین شریان ــ چین ــ پرهیز دارد.
همین مسئله احتمالاً سقف واقعی کارزار فشار اقتصادی جدید علیه تهران را تعیین خواهد کرد.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20287" target="_blank">📅 01:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">البزشکیان:
من میخواستم مردم بیان تو صحنه
و اصلا ریاست جمهوری تخمم نبود.
ولی حالا خودم اومدم تو صحنه
و مردم به تخمشون نیست.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20286" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پزشکیان:
اگر تحریم ادامه پیدا کند، گرانی افزایش می‌یابد</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20285" target="_blank">📅 23:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا دقایقی پیش از اعمال تحریم‌های جدید علیه ایران خبر داد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20284" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20283">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFXAV_RTIl24S8sHzucgeMI-7UKU42Tcof52DPPc5lF_wk0dCIYhA0aLGuqwMjKGs6tMygUDfn_qvNMPTRCfEYQilEQMZ6Lwtf0pGBeytt_2k1POa_p9nFdv9xo7-G5M2_o9eIYyPRMkHJn7EbR4HtIR92CgSox2iwk33Gtb8JRU0_V3JaHjca2lQrF9rNYTO0ixWFh2MJ_V--w2iSKZvGy2nhyOr5KaP8nUH67TrXgIbjIriMM5HWKvv4veRv8D8Lx5nq3l7K_AOzKxSk2G6yLmg2xaFXuNRohN6TkHlvLNZgz9CSBYZVSDlysqKMz-6rEQjKbPDoDcIiENn4q1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20283" target="_blank">📅 17:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20282">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20282" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20281">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ:  دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20281" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20279">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2hlLoNwVJXMn8G0wu0nmadtkF3Eb2MF_O2tryKD0nfP8YYaHQmE6kLn1R5dwYFQkVsktRdEEuv9PXb4yLkmBntUYMmcj7PVPkM69iILeOq3UfGeB9fRsMO2cs_qjqIqMfotuDeUSrNGQ2bN1Kqu3qz49P8hq3mB9h1SyRFx25f-FxA2eleDdnmjnndvM27Nah-W2Fnl2HjRuYiSlN74ZczME0qz0I0t4qhsg0kVRMsapKUFSvkyOPW0L5ORBtuKQT8Fk10P6V5lpFGJOZYDgH_EunbuoGXyDjlez8fPo4Igjwr0pQjhgv3pstdbMeiaR9pV87SHRaR8Oij0mySlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20279" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20278">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlFJLm-AVdtvxRpz_s7VgxZ8ZWf7xp8JMPm86yXNoDWq8TVFI8j7wiILyiwbeFT4y1hQXozzaveQsN6ED13TKThEgNn-zVH2kVDDCNL65OApxx7QF4TqbJYjF59D5Wy_7GfRxbIdfBQqsWlj0L2QqdBEUhSXetakTap69QjEH4e_h11G0BcmBgtCeeFHyYlVBin9lWhoLdLUK3s2LOUJy1lcYjt0rLt5G_nL7vESgVawEOy0kRch-LxANOuRDwv6gsAYDZMJWgAkVXVNbQLJQW2cuVb7i49yPTxeIM8cBkm_y1wxb_IywAnCo43mkKB97DPdudLAcqsBzYBpueR2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس
:
آمریکا در نبرد تنگه هرمز، دست بالاتر را دارد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20278" target="_blank">📅 14:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20277">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZpPncN2V6B7vrrgniCwn6HAGKYdfyYjaXau-yccAtBObFTyVBT9OyBPGZ3bTSpz1xMOOJ8APktaD0r0_jOU9O0Odd1vYRrpqdomLsPG_dmPX_hTpyTY_ohY9_RBEC9Lylty6kt7e_pCnbDxdo8xzsq7ufMnWhnlx0kP90Wuoad5hCmiGi4GIqfzTsoT8Mt6UAf2tDywbAOLsgNG2dWT2IyNUzT8UFjV1xh4rccfFnNv4fE6TdSE0aIM1Hf8ppc27R-onKlL5HdZuwUs15eNUplaEZ3QkSfn7QtLM6yI-HMENLfklcudkpvqIn0p15JjygKcCqWc3Zr8sMlSUZIUgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20277" target="_blank">📅 12:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20276">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoXWf2dlXPRHiIjZ9F3sd-HO60lhgwhu7rFJYTZl3IIYworeLBaem25pBdbYrBWaOh9V1ZqLjvlL3Bir63X-R9Xxag8f2lfCADo82xlteU1qQTuk_AT1Zo2Wbq68znnzlSjNeF3k6RhmoCa6RN8Xos93gYEmCMfekcinoqf3k7p2yqbUvTljijmNaS50CX6TOKUmo6I_NrmW3pp0mVVg0-Lmh2U7JnxCDi7Bdde24XKe3PHkEsr9dWB2b5vCvbWkZOd9ytQVKQgu4vAWm8dWuHZNFXeCWgY-scZh1t-BqgzKdiFTAcCLx78qqxopZVx95ezY0Nl1EulvCz0aAolwFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.
به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20276" target="_blank">📅 12:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20275">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این بار هم ۳۰۰ پیپ دیگر</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20275" target="_blank">📅 10:28 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

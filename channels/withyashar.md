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
<img src="https://cdn4.telesco.pe/file/qegKs_oH9UrZBAiWNu7PKcQtxTfNNHILGM3gdaCLan3ZppQO-vG4P2GLsejpQPZUaJcF4kkq7WTfZq5xTEARqmqpkq-5tU0KJ3waPitG75qyz4gzipOxlzWgGXK7pmXaMGW_HVzPOWIxLxW2-GJEtiFLnuerOiqC_13OcVnZhY6u5YGybXQlPLGpBSLFqa7NF8GrOGx1tPvCB2LiTtd4TjUzqMOeLxL9oBAUs0o15p3pby2thxDoz3ykATkrNBi1YiTdcr8cYtwOQswxIyzGtzQJbn3Ppa3ErV6o9k6cwzuZ926j6szXsuWudU2Smnfsq6dz3Om0IcCP68Kh7TUbJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 288K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 09:59:18</div>
<hr>

<div class="tg-post" id="msg-13464">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مقام اسرائیلی: ایران تصمیم گرفته در صورت آزادسازی اموال بلوکه‌شده‌‌اش، بخشی از آن را به حزب‌الله اختصاص دهد.
@withyashar</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/withyashar/13464" target="_blank">📅 09:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13463">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جنگ ترامپ با ایران و اختلال در حمل و نقل نفت از طریق تنگه هرمز، ذخایر نفتی آمریکا را به پایین‌ترین سطح خود از سال ۲۰۰۴ رسانده است.
برای کمک به مهار افزایش قیمت سوخت، آمریکا میلیون‌ها بشکه از ذخیره استراتژیک خود را آزاد کرده و همچنین صادرات به اروپا و آسیا را افزایش داده است تا جایگزین عرضه از دست رفته خاورمیانه شود.
@withyashar</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/withyashar/13463" target="_blank">📅 09:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13462">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=ehEQhBdS60-b5rL0MoLo889NYf6SKbmgKPzSxlzMVn6VhpdWoiEBIw43fBp5HecLCobMoGeewuXEFx_QesUbbj-YvySSeGpqC4mxnH0tVQBBPSg7A0y2kCU6FwJp3eL9tn6ZQ_SB8EbmXDXdvCjynNd7Sr7jHq4gp00lxZJYin8hkkxrkLS0RbxMECEQrXnERHP4c0CYAxk3SYUBuhbXO6KjvdfRxfLTaFpFqaHKV0ze9HTxbYEu_WwgocimS13ASyZFvE_arKs_tctD1q_4XL4moMVH6lHwB2eespxAUZpRMpH19FPePWh57dIQRw79Xb3V1G6D_r_fjit_QfzuVTo7LMkt-XQuDdU4xGFy3jfME_LjT01oa1bqGL5zDR0U7YKkobTL2LGSFI_NTj8m4UrzkC1_cxEgv5YRs05xQ8mvkg2kzVmvLj1micUpF2Rg3vlh9IidEjin4jWFx0xxy7JY1Ml1_vrWWUSMGVngikqoOa9mBZ7gekQhFaU74UEJkES2FFnwY7qmQrhXyObblGXTlnQpvnjnYmcGvhuRN5_Sk3VGjTOswS-FmXkL45GYfvbfORZt1DSiupohmTFU-N3IdFbnZyixlUw6xORBIelmbycQxfIQ9cXmVj-UjIX4tz3nkkQCBjGti0yezTCNYXr26Fsqg5O-JgtqZ6uw-E8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=ehEQhBdS60-b5rL0MoLo889NYf6SKbmgKPzSxlzMVn6VhpdWoiEBIw43fBp5HecLCobMoGeewuXEFx_QesUbbj-YvySSeGpqC4mxnH0tVQBBPSg7A0y2kCU6FwJp3eL9tn6ZQ_SB8EbmXDXdvCjynNd7Sr7jHq4gp00lxZJYin8hkkxrkLS0RbxMECEQrXnERHP4c0CYAxk3SYUBuhbXO6KjvdfRxfLTaFpFqaHKV0ze9HTxbYEu_WwgocimS13ASyZFvE_arKs_tctD1q_4XL4moMVH6lHwB2eespxAUZpRMpH19FPePWh57dIQRw79Xb3V1G6D_r_fjit_QfzuVTo7LMkt-XQuDdU4xGFy3jfME_LjT01oa1bqGL5zDR0U7YKkobTL2LGSFI_NTj8m4UrzkC1_cxEgv5YRs05xQ8mvkg2kzVmvLj1micUpF2Rg3vlh9IidEjin4jWFx0xxy7JY1Ml1_vrWWUSMGVngikqoOa9mBZ7gekQhFaU74UEJkES2FFnwY7qmQrhXyObblGXTlnQpvnjnYmcGvhuRN5_Sk3VGjTOswS-FmXkL45GYfvbfORZt1DSiupohmTFU-N3IdFbnZyixlUw6xORBIelmbycQxfIQ9cXmVj-UjIX4tz3nkkQCBjGti0yezTCNYXr26Fsqg5O-JgtqZ6uw-E8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد.
@withyashar
😟</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/13462" target="_blank">📅 01:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13461">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=ERroE_uyBC8EKHmgrTUmigJGtxhGg4F5TbX-UHjimZ3EyWsPCVKpRqkuOr4HYHhsoRtvAMww_dnuArUP73Ux5iwBNh1i2QHqFyjf6M31k0-zd_yh8odiDU4gS7FLFLICAH8qu9px9ZyC1vWFbGQVJBRzNzPcBzUMJYIYIF1SDQ3CO1K1Fxt_k9bKKTK5CAPQRq23mKY38JVQk8ftmZCxQTlWA1FMUX5afuQjsxpEYL5oIOEAwRqgSlHYkZhdg0QTljbTRaobRp177rQpOFdDRp0tLrRmJx7hP3a7dEtgoWK5coFX-Hyd_novUhlOabe4xoUwa_CWqiiE6pNMLCzNPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=ERroE_uyBC8EKHmgrTUmigJGtxhGg4F5TbX-UHjimZ3EyWsPCVKpRqkuOr4HYHhsoRtvAMww_dnuArUP73Ux5iwBNh1i2QHqFyjf6M31k0-zd_yh8odiDU4gS7FLFLICAH8qu9px9ZyC1vWFbGQVJBRzNzPcBzUMJYIYIF1SDQ3CO1K1Fxt_k9bKKTK5CAPQRq23mKY38JVQk8ftmZCxQTlWA1FMUX5afuQjsxpEYL5oIOEAwRqgSlHYkZhdg0QTljbTRaobRp177rQpOFdDRp0tLrRmJx7hP3a7dEtgoWK5coFX-Hyd_novUhlOabe4xoUwa_CWqiiE6pNMLCzNPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
با این حال، این اولین رای موفق مجلس نمایندگان است که قدرت‌های جنگی کنگره را در مورد جنگ ایران تأیید می‌کند و اقدام نظامی آینده بدون تأیید کنگره را محدود می‌سازد.
چهار جمهوری‌خواه به نفع آن رای دادند.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/13461" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13460">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">داداش اون بحث خیلی طولانیه اون میشه زمان ریست فکتوری طوفان بزرگ ( که با داستان خیالی نوح میشناسید ) تا اینجا بدون که قبلش تمدنهای بسیار پیشرفته بود روی زمین ، باشه برای بعد از آزادی
😂</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/13460" target="_blank">📅 01:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13459">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from00:30</strong></div>
<div class="tg-text">درود ولی من‌میرملاس لرستان رفتم اونجا دیوار نوشته هست‌مربوط به 12000 سال پیش</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/13459" target="_blank">📅 01:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13458">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یاشار : دمت  آقا دایی ، مردی ، خواستم تکمیل کنم که عدد
۲۵۰۰ سال
به طور مشخص به
سابقه پادشاهی شاهنشاهی ایران
اشاره دارد، نه به کل تمدن ایران ،
تمدن در فلات ایران ۵۰۰۰ الی ۷۰۰۰ سال حتی بیشتر سابقه دارد
@withyashar
😁
🙌🏾</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/13458" target="_blank">📅 01:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13457">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
‏ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/13457" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13456">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دو منبع مطلع در مذاکرات به i24NEWS عبری:
مذاکرات بین آمریکا و ایران به دلیل اصرار ایرانی‌ها بر آزادسازی پول‌ها، «پول نقد»، از میلیاردهایی که مسدود شده‌اند، حتی در مرحله اول، متوقف شده است .
در روزهای اخیر، میانجی‌ها تلاش کرده‌اند در این موضوع مصالحه کنند اما ایرانی‌ها بر دریافت پول در همان مرحله اول، در چارچوب توافق کلی، قبل از انجام هر اقدام واقعی در میدان، اصرار دارند.
مقامات ارشد آمریکایی تأکید می‌کنند: در ابتدا پولی آزاد نخواهیم کرد مگر اینکه ایران گام مهمی در مسئله هسته‌ای و هرمز بردارد و همچنین توافق کلی بسیار معنادارتر باشد.
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/13456" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13455">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvpiD6NhnH-7mmLY2V9a6KWzJVrjl2tIebkimHhxa7RE-HvtHUjrLL1qmTXgseJJ4inMu122-GIS69mZsbQSy63srSlp2STXpbNpwHFxUpogu1xOYToGlPGTSuf8sNSueOflK-oMgkH6Ndg3e1X8nbZZSAL9fcipOPQB9OAVlvUmngBflS-EHF3nfSvMUWlOy4obXuVpd-NKzHS-6hj8FJcF3czy9jRw4-5Zpsfu05R82XN4vrGhb2OL2QE6170SXagGo8VFCHeiBFb66cGW6mmm3RSYViHvzO_KdjEFMc78OxahLEUNcVPzbeREeDepuv8hjDuNbBC5I_WHyZYRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات آمریکا
جمشید قومی
، شهروند دوتابعیتی ایران و آمریکا و مدیرعامل شرکت «فرار پرداز رایانه» در تهران را به نقض تحریم‌ها متهم کرده‌اند. طبق ادعای دادستانی، او طی بیش از یک دهه تجهیزات شبکه، امنیتی و رمزنگاری ساخت آمریکا را از طریق واسطه‌هایی در دبی به ایران، از جمله سازمان انرژی اتمی و وزارت دفاع، منتقل کرده است. همچنین متهم است حدود ۱۵ میلیون دلار درآمد حاصل از این فعالیت‌ها را به آمریکا منتقل کرده و با آن یک عمارت ۳۵ میلیون دلاری در کالیفرنیا ساخته است. در صورت محکومیت، با حداکثر ۲۰ سال زندان فدرال روبه‌رو خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/13455" target="_blank">📅 00:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13454">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منابع العربیه: پیشرفت‌هایی در مذاکرات لبنان و اسرائیل حاصل شده است، اما هنوز توافق دائمی به دست نیامده است
اختلاف بر سر سلاح‌های حزب‌الله همچنان مانع اصلی هرگونه توافق بلندمدت است
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/13454" target="_blank">📅 00:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13453">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:
ما در واقع برای اولین بار با حزب‌الله صحبت کردیم. نمی‌دانستیم آن‌ها صحبت می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/13453" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13452">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ : تنگه هرمز فوراً باز می‌شه وقتی من یادداشت تفاهم رو با ایران امضا کنم
تنگه هرمز باز خواهد شد، مین‌روب‌هامون اونجاست
زیر آب هستن، خیلی خوبن، تکنولوژی‌شون فوق‌العاده‌ست
ما مین‌ها رو جمع کردیم، بیشترش رو پاکسازی کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/13452" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13451">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان خواهش میکنم دایرکت جای کامنت دادن به مطالب نیست
😟
خدایا به چه زبونی بگم ؟ بفرستید برای دوستون و باهاش‌چت کنید ، به بچه آدمیزاد چند بار میگن</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/13451" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13450">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرنگار
: شما هفته قبل گفتید آمریکا می‌ره داخل و مواد هسته‌ای دفن‌شده رو در هماهنگی با ایران بیرون می‌کشه. آیا ایران واقعاً با این موافقت کرده؟
ترامپ
: خب، بستگی داره داری درباره کدوم روز حرف می‌زنی. این چیزها خیلی هم بزرگ‌نمایی شده. من خودم هم اون رو یه‌جورایی بزرگ‌تر از واقعیت نشون دادم.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/13450" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13449">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a531a29092.mp4?token=G-0LBpEib7Ul2FDagvzCOttCsX_l3hmLbj832sl3GqGfW8gNQbD4uHlMpiKRVaZudOQ_WFn1-I4xtj57WtXrDgtNz4OQseDNRAdqoFINnuw7ISBIsqDZ782-frnV4Uq2m1np8csdBvfCKZa4J251_J0vu7Blk7i7S4lUBTyrojOC3fWTfXow0e-bQ9o1rz9b1OqCPQxnu4hx3WIDKPW_dBBQbI_DEcuJ7Dr2ai-eP8p_x__1ma556G5XEqcLE-Z6Y_x7GHKv6u5pqip1NBaW7_QgenxaNGFetDm7frT-71UzrZkSQ-PuevrSRi8KYgPFFDE-i6kXGqbCbNLx4_sT8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a531a29092.mp4?token=G-0LBpEib7Ul2FDagvzCOttCsX_l3hmLbj832sl3GqGfW8gNQbD4uHlMpiKRVaZudOQ_WFn1-I4xtj57WtXrDgtNz4OQseDNRAdqoFINnuw7ISBIsqDZ782-frnV4Uq2m1np8csdBvfCKZa4J251_J0vu7Blk7i7S4lUBTyrojOC3fWTfXow0e-bQ9o1rz9b1OqCPQxnu4hx3WIDKPW_dBBQbI_DEcuJ7Dr2ai-eP8p_x__1ma556G5XEqcLE-Z6Y_x7GHKv6u5pqip1NBaW7_QgenxaNGFetDm7frT-71UzrZkSQ-PuevrSRi8KYgPFFDE-i6kXGqbCbNLx4_sT8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما می‌توانیم دو یا سه هفته دیگر ادامه بدهیم و همه را از بین ببریم. انجام این کار خیلی آسان است.
اما اگر بتوانیم چیزی را روی کاغذ بیاوریم و مکتوب کنیم که بدون کشتن همه، همان نتیجه را به دست بدهد، ترجیح می‌دهم آن راه را انتخاب کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/13449" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13448">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=G4NyzB478YdIJX7BynEGNbDmWtI9Qy9mRjXz1bWE1dYgpLIW3NzYf2t1v98ZamC3pgkKGY1HRapwfIq7hK5Au4EP6Pt9CWW5yzkq8MSI2yfB6u9mSk1vteE3aIMkyQj673VchVY45QUzPxq_U2OIebk-4UMm6sMPddrvRyxZxvreEr-IBBSM3xi6Xg_wEGNgMSLHA-M5BLCflt61saLN61zIuufLGbJYyf9NsjWD5rIL7K7ERDLax7Rxvsj97SYmUDBRNyf0ZEV2lzyqN4xN1yg-_cdfrgn9tJAKbJEK-w3FEjBRXyEtF7FWnnFPc7Niwuv3hcrmYc5yMvlvIUlh6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=G4NyzB478YdIJX7BynEGNbDmWtI9Qy9mRjXz1bWE1dYgpLIW3NzYf2t1v98ZamC3pgkKGY1HRapwfIq7hK5Au4EP6Pt9CWW5yzkq8MSI2yfB6u9mSk1vteE3aIMkyQj673VchVY45QUzPxq_U2OIebk-4UMm6sMPddrvRyxZxvreEr-IBBSM3xi6Xg_wEGNgMSLHA-M5BLCflt61saLN61zIuufLGbJYyf9NsjWD5rIL7K7ERDLax7Rxvsj97SYmUDBRNyf0ZEV2lzyqN4xN1yg-_cdfrgn9tJAKbJEK-w3FEjBRXyEtF7FWnnFPc7Niwuv3hcrmYc5yMvlvIUlh6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در آن بخش از جهان«خاورمیانه»، آتش‌بس زمانی است که شما به شیوه‌ای معتدل‌تر تیراندازی می‌کنید.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/13448" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13447">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ درباره حمله ایران به کویت:
برای هر چیزی دلیلی وجود دارد، و ما به آنها ضربه‌ای سخت زدیم... آنها کمی تحریک شده بودند؛ آنها در حال پاسخ دادن بودند.
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/13447" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13446">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ : مذاکرات عالی پیش میره
می‌توانیم جنگ را دو یا سه هفته دیگر ادامه دهیم و همه را نابود کنیم اما ترجیح می‌دهم این کار را نکنم
هر اتفاقی ممکن است برای ایران بیفتد، و رهبری ایران سه بار تغییر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/13446" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13445">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش انفجار‌ قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/13445" target="_blank">📅 23:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13444">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ:دیشب و پریشب به ایران حمله کردیم و ضربه سختی به آنها زدیم
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/13444" target="_blank">📅 23:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13443">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G25B1ggMkFyCqIKDtIefiWwyaar1kyIqWjoZU4rl9wXpZHlenpd03rvALIKB5BKJMq-dPafJsU8Q1mYdoWYnwtwaKBZW6h_wBfKX_5o5MO3LxOHwQKU_OExJTez1kvCYXQGzLNeq10PsQaixMwSyum4cU4gWcbeAZ8cDtrLKBMvFns9n00f6OuX5q-Hb44Ug2R7UCVv6Yg1xUf9OTLMsG2kMc0N709ATHidQcGUJDQyeuVJe4-kKtGBc2WtojioKnigv9HHIeyHB-RMV9KuQlRhHgSmL2ZNWtUKpxHRoqkjqjbrv3VwljS9oihaMYIUqWZ6KBEJOL_nCXnEOlFNFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات بین اسرائیل و لبنان به زودی به پایان خواهد رسید. به زودی اعلامیه‌ای از سوی ایالات متحده منتشر میشه.
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/13443" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13442">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دفتر بازرس کل وزارت دفاع آمریکا در حال آغاز یک بررسی (بازبینی و تحقیق رسمی) درباره «عملیات خشم حماسی» (Operation Epic Fury) است؛ کارزار نظامی آمریکا علیه ایران که با هدف برچیدن تهدید هسته‌ای تهران انجام شد.
@withyashar
این آغاز یک بررسی یا بازرسی رسمی است، نه لزوماً افشای تخلف یا شکست.
Office of Inspector General (OIG)
نهاد بازرسی داخلی وزارت دفاع آمریکاست و معمولاً پس از عملیات‌های بزرگ نظامی، نحوه برنامه‌ریزی، اجرای عملیات، هزینه‌ها، تلفات، رعایت قوانین و عملکرد فرماندهان را بررسی می‌کند</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/13442" target="_blank">📅 23:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13441">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پدافند شهریار فعال شد
🚨
@withyashar
اینو دیگه دوستم اونجاست و وارده</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/13441" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13440">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTVjecQ3oAK4JE8WvSMV-6L3kSgtOesCh0F5Ltxe0ejI5g1Qce-MmtKVKSUfKbgWpJZ00DdJo_bBg8SJNS679KmTF4Xdq3mZNeqxYLiCEjRSeQjVp7iBe8jbquD_E40jp5V4b1WAeAFJL0vuGMP-q0sowSbXaWVm72_PVBmVSohtuLANEc4qoah96bYJhJpzvZCrf-ODOQ3UO2O8NLruzo4utSNVfJyzzLIVFIwYZepSkZ1JWcay5zCZcQ7lhzmgCTKW39_AW7lUsQF3t2A1b9_hbnGFy3A8aB5g7K87bhiyLYpMebNEGrQx32fAKHCS7nsRWsr_XxuYQqoZuvCGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بلافاصله پس از یکی از سرگرم‌کننده‌ترین شب‌های تاریخ آمریکا، یعنی مسابقات قهرمانی جهان UFC در چمن جنوبی کاخ سفید، به اجلاس گروه ۷ در فرانسه خواهم رفت. سوابق نشان می‌دهد که اگرچه در طول تاریخ طولانی و پرماجرای کاخ سفید، مبارزاتی در سطح بسیار پایین‌تر در این کاخ برگزار شده است، اما هیچ رویدادی حتی نزدیک به این، یعنی بزرگترین مبارزان جهان، قهرمانان جهان، برای مجلس عوام در نظر گرفته نشده است! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/13440" target="_blank">📅 23:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13439">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزارت کشور بحرین به دلیل خطر احتمالی آژیر خطر را فعال کرد و از شهروندان خواست به نزدیک‌ترین مکان امن بروند.
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/13439" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13438">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیروی دریایی جمهوری اسلامی ساعتی پیش یک ناو جنگی آمریکا را در دریای عمان هدف قرار دادیم @withyashar
🚨</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/13438" target="_blank">📅 23:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13436">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رویترز: رسانه‌های ایران گزارش دادند که تهران به یک کشتی نظامی آمریکایی که ادعا می‌شود حامل «مرکز فرماندهی و کنترل» بوده، هنگام نزدیک شدن به آب‌های سرزمینی ایران در خلیج عمان حمله کرده است
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/13436" target="_blank">📅 22:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13435">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c287d7f770.mp4?token=teCDv7PhckqGEFHypB38QeNQMAoW1dVfdnQjDMxHPpEaCZQ9N5Q0OGpP0ymZUKLvPzAQemALVuthkh_mCa7gCMUWdeLnhch9OAWsvEEVHji9UPSPpRk_euN1KwX3xLpwdLyQszd-ADA2boxPFnc4Sn1FOjEGvcCW0TsEx8pEl88O9GI6hS1xosGWN_p0fUkzuv2AassDJLaw5dATdMoWpeF_8dOhLQWczSZ-HFv365e23SUVKbojUhJOM1iFbPThBDsKh1Y70soAl8sIPYoAs3W_LLQAopbs8mCEZrpvxqZRgJOKctvb0priT5dD2NnjYY5yRZ7U0Zm-qNSXKsLfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c287d7f770.mp4?token=teCDv7PhckqGEFHypB38QeNQMAoW1dVfdnQjDMxHPpEaCZQ9N5Q0OGpP0ymZUKLvPzAQemALVuthkh_mCa7gCMUWdeLnhch9OAWsvEEVHji9UPSPpRk_euN1KwX3xLpwdLyQszd-ADA2boxPFnc4Sn1FOjEGvcCW0TsEx8pEl88O9GI6hS1xosGWN_p0fUkzuv2AassDJLaw5dATdMoWpeF_8dOhLQWczSZ-HFv365e23SUVKbojUhJOM1iFbPThBDsKh1Y70soAl8sIPYoAs3W_LLQAopbs8mCEZrpvxqZRgJOKctvb0priT5dD2NnjYY5yRZ7U0Zm-qNSXKsLfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی جمهوری اسلامی امروز ویدیویی منتشر کرد که نشان می‌دهد ساعاتی پیش موشک‌های ضد کشتی از کنار ساحل به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک کرده اند
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/13435" target="_blank">📅 22:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13434">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الجزیره: ستاد فرماندهی مرکزی ایالات متحده ادعاهای ایران مبنی بر اینکه خسارت به ترمینال مسافربری فرودگاه کویت ناشی از موشک رهگیر آمریکایی بوده، را تکذیب کرد
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/13434" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13433">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohamad▪️</strong></div>
<div class="tg-text">سمت منیریه پدافند که داره میزنه
یه صدا انفجار ام اومد ۵دقیقه پیش</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13433" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13432">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پدافند تهران فرودگاه مهرآباد فعال شد
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/13432" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13431">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🤬</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13431" target="_blank">📅 22:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13430">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فارس: نیروی دریایی ارتش یک ناوشکن آمریکایی که قصد شرارت رو داشت رو با موشک هدف قرار دادند  @withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/13430" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13429">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پدافند پرند فعال شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/13429" target="_blank">📅 22:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13428">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش هایی از پدافند غرب تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/13428" target="_blank">📅 22:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13427">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فارس: نیروی دریایی ارتش یک ناوشکن آمریکایی که قصد شرارت رو داشت رو با موشک هدف قرار دادند
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/13427" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13426">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
بچه جنگ شروع شد
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/13426" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13425">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElkBYcFyy8dhoX_gMv7Es7ZjL7n4yUObkBnaygR088FSEJ5Xqbde8Pu9kPTo1ymLURP0rZUD4QDTqzmvw4J0oWZNVklKo_xgFo14xxY1a71nZ3ntEpJNXQWkk4bpEDd69nVj-_Fbvx6l19bAmJ7oAa1OUaZYQSHux0xLMPjGIwQW0DowiVsHHZpIvFZFQR2AsapuyNcdJp7EMb8EPg9EBO-0TDooXoxueHACFK2Wh8jFTOWc8hrnH5t6HSFrKm5jJArgZWYWdwnjed72eKC_b6pRPGyiBTQJukCwZQ2sMVtUB-QHFWfK_yc4IjKfXp0TXlHnCs5o8zvdCx-p2gtMqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های داخلی آخرین عکسی که از حاکمان سلسله مموشیان در ایران کنار هم بودند را منتشر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/13425" target="_blank">📅 22:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13424">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اتاق جنگ با شما : پدافند شیراز ساعت ۲۲:۲۷ دقیقه فعال شد!
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/13424" target="_blank">📅 22:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13423">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تسنیم به نقل از عراقی: ایران آمادگی کامل برای ادامه جنگ برای مدت بسیار طولانی را دارد و ما از توانایی‌های نظامی لازم برخورداریم.
@withyashar</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/13423" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13422">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عراقچی: در حال حاضر هیچ روشی در مذاکره وجود ندارد، اما پیام هایی با آمریکایی ها رد و بدل می شود
دو روز پیش پیامی به آمریکایی ها مبنی بر لزوم توقف تجاوزات اسرائیل به بیروت فرستادیم
تماس ما با آمریکایی ها قطع نشد اما پیشرفتی در مذاکرات حاصل نشد.
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13422" target="_blank">📅 22:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13421">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAS6j_yUcUF2odcP2pbIn6-9rmaPpobYWcTRgD1uooIElUqN2UYBgTBoXs8TVvAyQKeg6HNnbU9aDUtmmedrqwu5bvQzw6NRnOxsRBsKiy7Dg1drVoTKjBiApBbj48ZTP9ypqhia-kxZVnqHWGz-04v__1CycS_IsVFtVQ3vgVlcHYKkGnyHBYIpVp5fqNmAtHzHZ6oZNe6TVR6szkI8hRam8wpNV-jTZjYb0bVlwzH6ZCkIpnpr79UYLK_cyjFOi2Jt5VXGI_H-j7Uie860Yzc-Qa2xGUKkm0oKiSXOj_m9dNUSewakU_zzowwR3k97j4WTiE0U8-kZD17v1bH3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع خلیل زاده با ارزش نزدیک به ۱۰۰ هزار یورو؛ کم ارزش ترین بازیکن تیم ملی فوتبال ایران و یکی از کم ارزش ترین بازیکنان کل رقابت های جام جهانی فوتبال ۲۰۲۶ خواهد بود.
خلیل زاده همچنین با ۳۷ سال سن پیرترین بازیکن ایران و جز ۱۵ بازیکن پیر کل رقابت های جام جهانی خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/13421" target="_blank">📅 21:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13420">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یکی از اعضای تیم مذاکره‌کننده ایران به خبرگزاری فارس: ما هنوز پاسخ خود به پیش‌نویس تفاهم‌نامه را به ایالات متحده ارسال نکرده‌ایم. ما وارد هیچ توافقی که لبنان را نادیده بگیرد، نخواهیم شد.
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/13420" target="_blank">📅 21:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13419">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کانال 12 اسرائیل :ایران پیامی به آمریکا فرستاد که هر حمله‌ای به بیروت منجر به شلیک ده‌ها موشک به اسرائیل خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/13419" target="_blank">📅 21:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13418">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سخنگوی ۳پا : تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است
بررسی و تحقیقات ما در مورد اصابت ترمینال مسافربری کویت نشان می‌دهد، نیروی هوافضای سپاه هیچ شلیکی به سوی این هدف نداشته است و تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده، که پس از شکست در رهگیری موشک‌های ایرانی بر این ترمینال فرود آمده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/13418" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13417">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt1XIW9l0-w8sqOSK9Dtsanmw46I5t1VcKL0xJfYrExeFOSxXrNbcLBTxuNpJgkfcoKy3s4QWaePU64V_jXOgH9ZS3Yd5q5dCIWHC3shHZ5X6UAodXcSydteRo5dmJ775Ga9_NSJO7MIi_TA4D1C0q9lhrpGGGEaXQKlVK-W23U-hd2UYCpbkGkZGSTjEkQjQqiJSZlGjhM6RKqWUsION1ZMdLejpt2D1o60YICrWN_P6aQ7v_EdB2_gkaprSpase64MLLGoodj_1mZx-6bfIW8BZthKqXQt66NRJigrefGCURg_hrpZpt8rIdNpsKRv_9JfVFB_gQuy0jFNVSLlhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد امین میمندیان، نویسنده پاورقی :
شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.
برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/13417" target="_blank">📅 21:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عضو تیم رسانه‌ای در تیم مذاکره‌کننده ایران: دلیل عدم موفقیت مرحله اول مذاکرات اسلام‌آباد، امتناع ایران از ورود به مذاکرات هسته‌ای بود
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/13416" target="_blank">📅 21:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو:
اسرائیل آماده است. نیروهای آمریکا آماده‌اند.
ایران با آتش بازی می‌کند.
@withyashar
شمام آماده اید ؟
😁</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/13415" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/13414" target="_blank">📅 20:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یعنی چی ؟  منظورش اینه جنگ تموم شد ؟</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/13413" target="_blank">📅 20:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromR</strong></div>
<div class="tg-text">یعنی چی ؟
منظورش اینه جنگ تموم شد ؟</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/13412" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13411">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مقامات اسرائیلی: تخمین زده می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/13411" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ادعای روبیو، وزیر خارجه آمریکا:
ما دیگر حملات مداومی در داخل ایران برای تضعیف ارتش آنها انجام نمی‌دهیم، زیرا جنگ «خشم حماسی» تمام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/13410" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تکذیب شد
😃
🤣
خاک دوباره پس زد</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/13409" target="_blank">📅 20:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13408">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">غرب‌ دوباره صدا اومد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/13408" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13407">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">غرب‌ دوباره صدا اومد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/13407" target="_blank">📅 20:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13406">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">sample : yourname.warroom</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/13406" target="_blank">📅 20:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13405">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یه ایده جالب دارم ویس میدم …</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/13405" target="_blank">📅 20:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13404">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">https://www.instagram.com/reel/DZIVRzvuaUf/?comment_id=17892109731481781
به درخواست شما متن برای بانو نور هم کامنت شد</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/13404" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13403">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">صدای مشکوک به انفجار از غرب‌ تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/13403" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13402">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اتاق جنگ با یاشار : ما الان با دو بخار مواجه هستیم، بخار هسته ای و بخار خامنه ای
@withyashar
پایان چالش رو اعلام میکنم
🙌🏾
🤣</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/13402" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13401">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی در گفت‌وگو با شبکه اسکای‌نیوز با بیان اینکه از موقعیت مکانی ذخایر اورانیوم غنی‌شده ایران که در جنگ  سال گذشته هدف حمله قرار گرفت، مطلع است.
او ادعا کرد که این مواد همچنان در همان محل پیشین قرار دارد اما دسترسی به آن به‌دلیل خسارت‌های فیزیکی دشوار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/13401" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13400">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">💩
تاریخ برگزاری آئین وداع، تشییع و خاکسپاری علی خامنه‌ای اعلام شد   ۲۰، ۲۱، ۲۲ خرداد؛ وداع در حرم امام‌ خمینی  ۲۳ خرداد؛ تشییع در تهران  ۲۴ خرداد؛ تشییع در قم  ۲۵ خرداد؛ تشییع در عراق  ۲۶ خرداد؛ تشییع و خاکسپاری در مشهد @withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/13400" target="_blank">📅 19:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13399">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">💩
تاریخ برگزاری آئین وداع، تشییع و خاکسپاری علی خامنه‌ای اعلام شد
۲۰، ۲۱، ۲۲ خرداد؛ وداع در حرم امام‌ خمینی
۲۳ خرداد؛ تشییع در تهران
۲۴ خرداد؛ تشییع در قم
۲۵ خرداد؛ تشییع در عراق
۲۶ خرداد؛ تشییع و خاکسپاری در مشهد
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/13399" target="_blank">📅 19:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13398">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e72ba1695.mp4?token=GP9YOAma2HSBFw5jGAfdE3Krp7DlQ7lBRKY8NIwHlEyPtO0zwaEKAuK6sy_0DDwEK1nx40OdP-D2cHSiQlm4wAsCer0zO5pzRYWjTv4Jm76I-4oRxHVEkBEN-78sVIuLe0_Jp-tuSw_1sIaT2cUs1FVXAUF_lQ5mSYrCfBnYIWw8TblqUDNGxg6CVU87e3Pu6houvM9yf5JZZiOnT1Vos9x10tL9FCobi2GiYef1r1baPHDE6scTBIij_UmVtZIKlZL2c-nw70ZHw-XyqE570tgVJNeXigTDbrDkBlALpFNXIUIHiEdDxYURRQd0nER164gTS19VuT3hPh3VV1AR1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e72ba1695.mp4?token=GP9YOAma2HSBFw5jGAfdE3Krp7DlQ7lBRKY8NIwHlEyPtO0zwaEKAuK6sy_0DDwEK1nx40OdP-D2cHSiQlm4wAsCer0zO5pzRYWjTv4Jm76I-4oRxHVEkBEN-78sVIuLe0_Jp-tuSw_1sIaT2cUs1FVXAUF_lQ5mSYrCfBnYIWw8TblqUDNGxg6CVU87e3Pu6houvM9yf5JZZiOnT1Vos9x10tL9FCobi2GiYef1r1baPHDE6scTBIij_UmVtZIKlZL2c-nw70ZHw-XyqE570tgVJNeXigTDbrDkBlALpFNXIUIHiEdDxYURRQd0nER164gTS19VuT3hPh3VV1AR1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه عباس چپقچی:
نیروهای مسلح ما در حال انجام حملات دفاعی به سایت‌هایی هستند که آمریکا اجازه استفاده از آن‌ها را برای حمله به کشتی‌رانی غیرنظامی و نقض آتش‌بس دارد.
هر عمل خصمانه‌ای با پاسخی فوری و قاطع مواجه خواهد شد. تحریم‌ها و جنگی که نتوانستند به هدف برسند، با جنگ بیشتر به دست نخواهند آمد.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/13398" target="_blank">📅 19:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13397">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پست جدید پیج دوم شاهزاده کامنت رو گزاشتم
🙌🏾
ادامه میدیم تا جوابی بگیریم
https://www.instagram.com/p/DZILMCsFoyR/?img_index=1&igsh=ZmZzNTQ2NHMwN2x2
و این پست
https://www.instagram.com/reel/DZIOnXHRKuy/?igsh=MWkzYmpzN2pjMmgyYQ==</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/13397" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13395">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/13395" target="_blank">📅 18:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13394">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مجری: چرا نمی‌تواند آمریکا فقط تنگه هرمز را باز کند؟
نتانیاهو: خب، می‌توانید، اما به مالکان کشتی‌هایی نیاز دارید که ریسک مالی برخورد را بپذیرند. از نظر نظامی ممکن است، اما ساده نیست
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/13394" target="_blank">📅 18:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13393">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d25386882.mp4?token=VyLjAN0zFGYXw7pl8Xv7rXFmemFchjQ8lAaT-6nrw9TvR5Rs9TiS_M9ITD955hKTg_fBWEEq-7vnrcmaElTNC9GdFBQGV-3S2gzjXokCEmZQ5zu1WgfcKWlfVt7apzwZRm9n94geTfYkik_1_WJTihVOtog-RbQKm2WkILGeFPyljvp6ShQObFA7aeDUypeVBvOxCJUuz35CHukBdkCX5yhvH9FSLRn2IGtW_8qzzuJhqzN8zp-RrxIxxjAFEMOVKpg9Fr8bbAABlnAXuP1FMJoYgn7Fw_Gi4wNV6iTc-HPfTMLKg5mDLhDEVuOAKRsjfIEtVbPyAGPcai7ePs95cESGN385ps8m4sNkQQ-0R-QQh-zbGcwb522FdgzUhyYW3bqxDFSvAWbCZEL1eeKy4a2e05Iu-w4MZ8kZpFwyL82uBXMstpw1YunNrTMRvrqNbssL0hDa8DGEpL9lpId9oSKc9RBKOJXLm-V7J_DX2MMPtFFYoY2Cmi0hyGnfMfHzzFmh2UkehF7OO2rhW1WqUVP3DS3kh_YEF_0M4pok-HMmHAhAvPFjFprTYyWm8s9Tey0DKcib0UdI0TCwFSnepgSHr1giM0vB8Dt89YpGSyVB7wphPkANUAPjeecaSjPmtSpO0GbTN42musiujApEnsRyHu1nM9dY6eBC3h8MwKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d25386882.mp4?token=VyLjAN0zFGYXw7pl8Xv7rXFmemFchjQ8lAaT-6nrw9TvR5Rs9TiS_M9ITD955hKTg_fBWEEq-7vnrcmaElTNC9GdFBQGV-3S2gzjXokCEmZQ5zu1WgfcKWlfVt7apzwZRm9n94geTfYkik_1_WJTihVOtog-RbQKm2WkILGeFPyljvp6ShQObFA7aeDUypeVBvOxCJUuz35CHukBdkCX5yhvH9FSLRn2IGtW_8qzzuJhqzN8zp-RrxIxxjAFEMOVKpg9Fr8bbAABlnAXuP1FMJoYgn7Fw_Gi4wNV6iTc-HPfTMLKg5mDLhDEVuOAKRsjfIEtVbPyAGPcai7ePs95cESGN385ps8m4sNkQQ-0R-QQh-zbGcwb522FdgzUhyYW3bqxDFSvAWbCZEL1eeKy4a2e05Iu-w4MZ8kZpFwyL82uBXMstpw1YunNrTMRvrqNbssL0hDa8DGEpL9lpId9oSKc9RBKOJXLm-V7J_DX2MMPtFFYoY2Cmi0hyGnfMfHzzFmh2UkehF7OO2rhW1WqUVP3DS3kh_YEF_0M4pok-HMmHAhAvPFjFprTYyWm8s9Tey0DKcib0UdI0TCwFSnepgSHr1giM0vB8Dt89YpGSyVB7wphPkANUAPjeecaSjPmtSpO0GbTN42musiujApEnsRyHu1nM9dY6eBC3h8MwKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
: ترامپ شما را «دیوانه لعنتی» خطاب کرد.
نتانیاهو: گاهی اوقات، مانند بهترین خانواده‌ها، ما این اختلافات تاکتیکی را داریم. همیشه راهی برای حل آن‌ها پیدا می‌کنیم.
می‌توانیم صبح با هم اختلاف نظر داشته باشیم و تا بعدازظهر اقدام مشترکی انجام دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/13393" target="_blank">📅 18:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13392">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d950e42b.mp4?token=TMHlF4dRBEiDF3_wqKLn5nL4tvWJ0chC08Ol4lF-7HFOrdNNdmOpDbJYjtiutOAC_Zy_ZH0SECpbnR5nNnoeDh2HRYk7gWoX6T22LM4KqDhZe8Vi5FGreU5kWJRofyIPlmx7Bnq1qeGYNua-Fz2f2lLcQ5NcKZjuIXHGjVbcIGZ-evTMRvl4WHaUUsB_kjp95OjVexfxxcXOJZhghTpFc20ON8M9ceE2J7Gpyp_vlbVNHHT9qZkBfioK2-Os742Il4aBMb6lwqxq9oEdlwaTKh9byoPs4QVVwuSC0uJlOsgvZjRqRu2tukb6MrK-boRpnlIevkd0fvLKuAJn3vwGOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d950e42b.mp4?token=TMHlF4dRBEiDF3_wqKLn5nL4tvWJ0chC08Ol4lF-7HFOrdNNdmOpDbJYjtiutOAC_Zy_ZH0SECpbnR5nNnoeDh2HRYk7gWoX6T22LM4KqDhZe8Vi5FGreU5kWJRofyIPlmx7Bnq1qeGYNua-Fz2f2lLcQ5NcKZjuIXHGjVbcIGZ-evTMRvl4WHaUUsB_kjp95OjVexfxxcXOJZhghTpFc20ON8M9ceE2J7Gpyp_vlbVNHHT9qZkBfioK2-Os742Il4aBMb6lwqxq9oEdlwaTKh9byoPs4QVVwuSC0uJlOsgvZjRqRu2tukb6MrK-boRpnlIevkd0fvLKuAJn3vwGOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: مردم ایران خواهان روابط خوب با آمریکا هستند و خواهان روابط خوب با اسرائیل. این می‌تواند اتفاق بیفتد.
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/13392" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13391">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مجری : شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
بی بی : چرا این را می‌گویید؟
مجری: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
بی بی : این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند.
ما باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند و این تغییر نکرده است.
اما این اتفاق دقیقاً در لحظه‌ای که ما بخواهیم رخ نخواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/13391" target="_blank">📅 18:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13390">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو به ان‌بی‌سی: وضعیت در ایران تمام نشده، اما ضعیف شده است. ما و آمریکایی‌ها آماده‌ایم در صورت لزوم اقدام کنیم.
اگر تشدید تنش لازم باشد، آن را به ترامپ واگذار می‌کنیم و باز کردن تنگه هرمز از طریق نظامی امکان‌پذیر است.
ترامپ در حال بررسی چندین گزینه است و ما هر دو روز یکبار با هم صحبت می‌کنیم.
ایران هنوز با حذف مواد هسته‌ای موافقت نکرده است، اما فشار فزاینده‌ای وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/13390" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13389">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">روبیو: سکوهای پرتاب موشک ایران آسیب شدیدی دیده‌اند که منجر به زوال قابل توجه قابلیت‌های آنها شده است.
ما می‌خواهیم شاهد تغییر در ایران و حکومت مردم بر آن باشیم و دیگر تهدیدی برای منطقه نباشد.
امیدواریم که ایران جاه‌طلبی‌های هسته‌ای خود را کنار بگذارد و حمایت از تروریسم در سراسر جهان را متوقف کند.
«عملیات خشم حماسی» به هدف خود یعنی شکستن سپر سنتی ایران و کشاندن آن به پای میز مذاکره دست یافته است.
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/13389" target="_blank">📅 18:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13388">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">روبیو: امیدواریم امروز بین اسرائیل و لبنان توافق صورت گیرد
وزیر امور خارجه ایالات متحده:
رهبران دولت‌های لبنان و اسرائیل در حال حاضر در مقر وزارتخانه ما برای مذاکره دیدار می‌کنند.
ما امیدواریم که جلسه امروز بین لبنان و اسرائیل به بیانیه و برنامه عملی برای مسیر امنیتی لبنان مستقل از حزب‌الله منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/13388" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13387">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEq5dIuzdIwTvxeUSkUBtP8HXGjHWRlmDtkd4FYu8_g4Um3YzZSQZrRtu068tzaXeLv-DaolHBBgAj47C5aQEkS-pF8qz5K5aw5t38-tBjfIsys0oXKDlZMthSSOpnzGJih7sRNenReCytQt5XE3eo0XLkqXxONu6SwyL_msrBer8TP6dGeKsf_rWSfC9jeaW-Xs0xqDuoyd4qc6m3_ngOjDRDmHzr21YFE5UTy8r_PUJGHhiqFDpUauka86qUx6Ho5PLZegUC_CZFYcdXEmx0bi-xvzM9gNX-se5JKNCr7Uwa2DhTEIf-s4SFR8O6ksZQpYAlbXxWfRJ5dpPqsHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر ترکرز: یک ابرتانکر VLCC برای اولین بار در چهار هفته اخیر، نفت خام را در جزیره خارک ایران بارگیری می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/13387" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13386">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وکیل شخصی نتانیاهو، مایکل رابلو، به عنوان بازرس کل دولت اسرائیل انتخاب شد.
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/13386" target="_blank">📅 17:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13385">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کویت در پاسخ حمله جمهوری اسلامی ، دو دیپلمات را عنصر نامطلوب اعلام و اخراج کرد.
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/13385" target="_blank">📅 17:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ارتش کویت: ما 13 موشک بالستیک و 17 پهپاد رو شناسایی کردیم.
یک فرد هندی جان باخت و شماری از افراد زخمی شدن، همچنین خسارات مادی سنگینی وارد شده.
به دلیل حملات، امروز 5 بار آژیرهای خطر به صدا در اومدن.
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/13384" target="_blank">📅 16:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13383">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">️بیانیه نیروی دریایی ایران:
فقط مسیر تعیین‌شده ایران برای تردد امن در خلیج فارس است / شناورهای متخلف هدف قرار می‌گیرند
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/13383" target="_blank">📅 15:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13382">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ : ما خیلی خوب با هم کار کردیم. من «بی‌بی» رو خیلی دوست دارم و همکاری خیلی خوبی باهاش داشتم
می‌دونی، ما تو شرایطی بودیم که اون نخست‌وزیر زمان جنگه و من هم رئیس‌جمهور زمان جنگ هستم
ولی در کل رابطه خیلی خوبی دارم. با هم خوب کار کردیم، نتیجه هم گرفته شده
همیشه هم همین‌طوره. بدون آمریکا اصلاً نمی‌شد انجامش داد، همه اینو می‌دونن. ولی ما تونستیم
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/13382" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13381">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIxPxAWORdq6TEOJOx3-KSTvegqGUT-onzXaY7Srw51Se_pp2uIcrBy3OgDmXqPRbkT1dsz5q5uphFwQnTdR3Cu-_iiKLt1qDbZH891k0BhYHMaNRSdp9Ixj5BiAoTuQv68pEt5rck2lrnF4u6z9Ngrql2uQYCXJma_gqVKZQoENyoFl9P2ofvzfszQq72s9sq1ubHgQDhuF7mY0phgFYO6zNYDezvTGvgnTSgVlegMeDc0K4BBDhSi6es-zcSXnmgtpcaW7bTWmk5agOoD4cWnUxt4TvP5wSM5lH2SvyExgTCaFfTZARwcF3o-XnN3sORQ2Miu9KzVqVOw4kRTA3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در پست جدیدی در تروث با تلقین حس مخفی‌کاری و چند چهره بودن در قالب جیمز باند مأمور مخفی شکست ناپزیر ظاهر شده
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/13381" target="_blank">📅 14:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13380">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfniKJZASHQHitJOBJjUisT1EgsN9Zf76yqqLi3ywBzgKc0wTLYgsSsNyYUJMak8fkr5LQ2sFUxwLJWnKMFfXLxt5DFFmBxrVHSmUfcoeDJsy57vn70tyVVK56nSEYL7nzpJfkGOA6iBGdYC8E59uUhJMosvWWvqyDrfsCv9uq-ndVLAZbNW9LR1gEd5cv6DQ6vyYpRlOv55JyBweHtj60xMhG5sZwHwMZWS8wDX3pBaRxdUqfUnA2eElBbYG7cZQZHTFBlVcLJvSRfyapJQhj-12JCyDeD88zdO_JCfuSnVoKbOsnFk46RmDoVsIPp8nEwCzRt8UyPWin03ScFM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان تحرکات سنگین دارن
جهیزیه را میارن
🎉
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/13380" target="_blank">📅 14:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13379">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ دربارهٔ سال ۲۰۲۸:  من هر دو نفر، جی‌دی ونس و مارکو روبیو را دوست دارم. دوست دارم که با هم باشند. جی‌دی و مارکو تیم فوق‌العاده‌ای خواهند بود. هر دو بسیار با استعداد هستند. @withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/13379" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13378">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ دربارهٔ سال ۲۰۲۸:
من هر دو نفر، جی‌دی ونس و مارکو روبیو را دوست دارم.
دوست دارم که با هم باشند. جی‌دی و مارکو تیم فوق‌العاده‌ای خواهند بود.
هر دو بسیار با استعداد هستند.
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/13378" target="_blank">📅 14:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13377">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ درباره ایران:
ما نیازی به حضور نیروهای زمینی نداریم. با بمباران، بخش زیادی از نیروی نظامی آن‌ها را نابود کردیم.
آنها نه نیرو دریایی دارند و نه نیروی هوایی همچنین سرباز‌ زیادی هم ندارند
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/13377" target="_blank">📅 14:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13376">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ایالات متحده به تازگی یک جزیره کلیدی ایران را بمباران کرد.
این یک تشدید تنش بزرگ است.
کینگ ترامپ با ملاها بازی نمی‌کند و آنها دارند متوجه می‌شوند.
اوضاع به سرعت در حال وخیم شدن است.
@withyashar</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/withyashar/13376" target="_blank">📅 14:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13375">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ : گروه‌های مختلفی از آدم‌ها هستن؛ گروه اول دیگه نیست، گروه دوم هم نیست، بخشی از گروه سوم هم حذف شده
و اون آدم‌هایی که الان باهاشون طرف هستیم، همونایی هستن که الان کشور رو هدایت می‌کنن
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/13375" target="_blank">📅 14:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13374">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ: اگر من نبودم، الان اسرائیلی هم وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/13374" target="_blank">📅 14:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13373">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ:
هر کسی که من حمایت می‌کنم برنده می‌شود. منظورم این است، همه. هفته گذشته دیدی، درست است؟
هر فردی که من حمایت می‌کنم برنده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/13373" target="_blank">📅 14:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13372">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:
می‌توانم پاسخی بدهم و سپس، ۲۰ دقیقه بعد، وارد دفتر بیضی‌شکل شوم و متوجه شوم پاسخم اکنون نادرست است.
می‌دانی، تغییر می‌کند. حقایق تغییر می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/13372" target="_blank">📅 14:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13371">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
یعنی من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من شروع‌کننده بودم چون نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.
اگر من نبودم، اسرائیل هم وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/13371" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13370">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: به نتانیاهو گفتم او کاملاً دیوانه است، چون از درگیری او با لبنان نگران بودم.
من رابطه خوبی با نتانیاهو دارم
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/13370" target="_blank">📅 13:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13369">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزارت امور خارجه کویت : حمله ایران به فرودگاه کویت یک کشته و چند زخمی در بر داشته !
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/13369" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13368">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صدای انفجار در‌ قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13368" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13367">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ تعریف میکنه نشونه زدنه
😁
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/13367" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13366">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ در پادکست :
: احتمالاً تا روز کارگر (Labor Day) بتونیم محاصره ایران رو برداریم
هیچ‌وقت به دیدار با هیچ‌یک از مقام‌های ایرانی فکر نکرده‌ام
آیت‌الله ایران تو مذاکرات با آمریکا نقش داره و تو جریان گفت‌وگوهاست.
احتمالاً یه زمانی با آیت‌الله ایران دیدار خواهم کرد
قیمت بنزین به زودی کاهش می‌یابد
وضعیت ایران خیلی سریع داره تغییر می‌کنه، و در نهایت اوضاع خیلی خوب پیش می‌ره
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/13366" target="_blank">📅 13:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13365">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/13365" target="_blank">📅 13:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13364">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صدای انفجار بندر عباس (گفته بودن ۳ روز مهمات عمل نکرده است که دیروز روز سوم بود )
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/13364" target="_blank">📅 13:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13363">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfRzrW6e2MNe0GygbjiAkeFuwuxImMlQL8WcUCOc9h9f4-NXN24H7Iwn14TjsnSI0NcTWLOUecIufVAi8TLa8jIsPPwcyjuCTFhMj_F2dIH63444bO0x0aRnhrc1BipIKMn6JQJavW4m-MT6S2P35zSh8sGURVLs8S_uaDYDi2Y_Uqgqt3Y93wSvO0bBYHwqs5alsrrZCaecexhCzDEfcLpGqjoDxC9u6Xpn2paFuZiyUpTxuPuwhCV0xkPEtBLeUJbrd9H6G4G9yPc5SopCXFZ4jyIi8jSeCHWjqpRi-MbSK-AH1sy-AcQUdYz0LqzpWIXuT5nXgAcDJca-2x4jMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای مربوط به دیروز ، آخرین موقعیت ناو هواپیمابر آبی خاکی یو‌اس‌اس تریپولی (LHA 7) را نشان می‌دهد که بسیار جلو و در نزدیکی رأس الحد عمان آمده!!!
🚨
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/13363" target="_blank">📅 13:37 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/l0oCevYuAzu8-6evub6TXK_nCnwt-wU05fsP3PBBF6K5Qx4mntzGR6pQlHpTd-Ghb6AixaLqtLNchxwmp0NFA8y3wt7j_1p4sFU6CNbZhs6TKo7G0JHYzV4-rQe5--X2S-tsu8_ISxZwGG6pL-ts6HfnNZCxHMS2iqkz5ZdZUuHnrb96YX4mdj4BEJZGMlOvzQ75uVF17s6QIqIL4HSmXLt4esf14-j1ZlKjoYyRQRmnF41KOjiqnHjlNYRwfvTDXzpTI1pZRp7IhToU9CvLXTKGrvegZkEPJIFxnZW_IWGDSY1UXlpsJwbDUJ6QykCez0604nZy3Fx6_9-hI12Jzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 504K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-29870">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/29870" target="_blank">📅 13:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29869">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoXLaFD3jGyLd5m1D0WJe988ZQ3-XzpSzuGZfwJBh3rNbiOHY_rRaxycl-Q9gMjXOUR37HY0u2MOQcWhTUr6E7mScuIE1JG-nbF_s7K-kgD5jzcFhXe_wIumjYwV5SrbJxOM_2YSX_5eG-HfIEsByKLYw7SVP3VZSEzhTfOFFLzVNf_Poa6ZqaDWfEx1aBzAxg8yAeiNphksQh3xWwYUudB_fAxTir-y8UVsBs5ILGYIfYuWLQZo9ziUcIB5Gkc0rJk1FJUCZJcP2Czm9wNkw7PGH8JmgoVvY7mUi51p2F5JNgjtw3feafCIMzprrY1I104uJGuBRjahd5Ewcx_sIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
سهراب بختیاری زاده نام دو مربی جدید ایتالیایی و پرتغالی رو به مدیریت تیم استقلال داده تا با یکی از این دو گزینه برای دستیاری او در استقلال به توافق برسند. بختیاری زاده اصرار ویژه‌ای برای جذب دستیار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/persiana_Soccer/29869" target="_blank">📅 13:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29868">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRm8Dl42dBusc6xs7yVj8SkK21Gv_QhBRjBVUt6XyZUTqOmmq-yKkrzs_cbQDUglENNkn8n-ME0qkSQGlTFmEN7eHN37rpPtQzF5hGfdtBlv3yyeZRfo9VjCNyhmhJ1N8XwwoWLbAI_cq-oLA9b654QWEgge0E6i1_Kx9HpPuASq9_INV22uDG8th6fg3XtPEgwO_MaFzPapFwuf7Dma8mhJN-O4kP4atfthRtRrO6HNlttJCSl3LSI6nYh6RkkDkSXEzmr0L6SgvO2O6ufP103pw88eyXSzjLglIhmHyg9YWGQLbLQvdgZK44x5pR_VYD9T6a_dPTdzRnXQ95QBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد حبیب فرعباسی دروازه‌بان استقلال درفصل جدید در تمام مسابقات: 8 مسابقه، 7 کلین شیت، 19 سیو، میانگین نمره 7.9 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/29868" target="_blank">📅 13:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29867">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX8mfiNUjrBY46_ln8ITK3l5y4CiR6V1vYsOhLFt8F8_BQIzzenIH5-8XHXQ8iPaDm3dtFKT5lclAwv7tbtvc3OIITLdv2ACMHQ8RWButLmAoWqhcWJE27-MTe2sAU_hCyRdUNY9Q6UhujHE2dWK0GKUqJeqW-WjbvciOGHYjXQTJRezCZ7iHoshh9JZSWkJezXIcHGEkkHGQpS3GjFZWx4cCxqJQ7_BXCVEwfkkxUgZ0lVQsvtpgvdAzEGG2m1pn14rmFTXShteBbnoGalZ6Z4F3-i53D-0TO5nOhKo7pE-Ft2Z4AkXui4C7cjTruPOEBYDu_wqeAGNbPuFXGrSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/29867" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29866">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=GBhk86pUR-Dd8PERdQwxju_eMxiEWaWeTPWcAoE80HvlSWgWk5nkB4mJ7o_OwMcMn2wUP8qJVhXnfAzBrSSA2vlZ8wZTmbTmokIucUWkYP_gOJaQdNfvOIn9plkyqmTcnb6XWpLPknNhY0GPwhi4a162C7tyTqPDviFbyVMNcA-B7ySKtHxfB8VvXMJOChR4Nk-aaZULJ-F02o99DnW9YzJ_3Yx2aWOAwEgl7NFXGesys1ZYox2sEciHV7KnpJu4PtO-16md3wRnXMUCNCir9Xa7BThVmxZV0YIzWk6vDXQOLWO_1JdYkmEU4Hi5fJZ2ryhc3AvIRgx8ZmvaPJQqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=GBhk86pUR-Dd8PERdQwxju_eMxiEWaWeTPWcAoE80HvlSWgWk5nkB4mJ7o_OwMcMn2wUP8qJVhXnfAzBrSSA2vlZ8wZTmbTmokIucUWkYP_gOJaQdNfvOIn9plkyqmTcnb6XWpLPknNhY0GPwhi4a162C7tyTqPDviFbyVMNcA-B7ySKtHxfB8VvXMJOChR4Nk-aaZULJ-F02o99DnW9YzJ_3Yx2aWOAwEgl7NFXGesys1ZYox2sEciHV7KnpJu4PtO-16md3wRnXMUCNCir9Xa7BThVmxZV0YIzWk6vDXQOLWO_1JdYkmEU4Hi5fJZ2ryhc3AvIRgx8ZmvaPJQqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/29866" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29865">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxMt0BVO8Y2CDkOZ0dKJu3wey6ETgSS2ddAMCYVlSpJC4179XMZQARiTaDXIbOH7XA4pChx5uRAO1diM-_VOh4nDvP1lXJvKMbLQ63WUJaHGWik8Afn0qc_NNDQy3q3N1PKy9X9KtzQjiUFuN2VEIC_bHjkh7TcE-Clr8YnGdAOOEShviiVvgXa0X_hoW5D7e0_v8tvNLM-w7vANwaus28b7TJROYHLLeRc1JeX44Nd-d0VAUkJ77zL_Y7_q30hakTLwYcGQ9KpvaT14tQmXLVGjcfj1lOFnhGl1ceVAqsU4Ec4aX50hJ-w-5qfuvUwJKvin3f1WjCjne26m5o3NWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤬
گردونه شانس پین فلک
👑
هم برنده باش هم لذت گردونه رو تجربه کن
🤩
واریز کن
🤩
ازپشتیبانی کد رو بگیر
🤩
گردونه رو بچرخون
🤩
بدون پوچ همیشه برنده باش
🌟
جوایز بی نظیر سایت بزرگ پین باهیس
👇
⭐️
آیفون 17
⭐️
ایرپاد پرو
⭐️
پلی استیشن 5
⭐️
300
💵
جایزه نقدی
⭐️
و هزاران جوایز ارزنده
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r25
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/29865" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29863">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THiQ7essGBwDRbFHjTFrXBRQ6WyM4EyMX62c4IyihdANdWiLrV2Cd0hWlSARsivE3quT1909SpmPKppTYs1cevr2mWDi2BDCB-dljEn-yyo022ujXymdt6FA0EqSvagjKxeOnXS-ypyYHbWHTKeglldnftLHCZ32RpWPH5avd1UpxVj_UpcB5vV44-Z8iRQ9XcY49ywEVzNgltOPZiUTHP27fAZHe2jrD2-I_86Qp6qI2EbIThiXIfuPDiUei5THkut0MazvpL5pTPdy_B1_Lip6MGUxKKgwNWpwhdoZPCZVwTUqAm_kJ-mykx5KWvuEhTLLyaBdjqKmB-OlWaNYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تراکتوری‌هایی که در پایان فصل قرار دادشون به پایان میرسه:
علیرضا بیرانوند، شجاع خلیل زاده، محمد نادری، کریم آذر، دانیال اسماعیلی فر، صادق محرمی، مهدی شیری، اودیل خامربکوف، تیبور هالیلویچ، مهدی حسینی، مهدی ترابی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/29863" target="_blank">📅 12:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29861">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5t6oAzywEFCDsE5-OBMu7CtJ7VXyS-FRjxFPe1Ic3FcmRZidnotItHGfBiMCsZis-r2trLlr0OLrwQipoobFRYG3vpfN3Js8FAYVswzYyuqsHZfmajKnEnx8Hky4G-SKMLitIj_LSq8DuIKp3tybxGEi5Qwhxp_4hTKDCr4y5izu_-C_mq2CbUFu2xiSb4RdwACkWAUziISP5awluDvSkYfikV6CpoFlkw9Gx3vxRXkWlKjFU5CLPwhUJaJak1PpCg-YdBWt0Ye1Kwu39H-e8s8hxNWfIjyrJw6F4INrMsqi4P1rWBVKZiV6f95_oRer_M0_jufJwFoeAHVY4Yk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه:
محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/29861" target="_blank">📅 12:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29860">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJPjGIjKOAxmiC9WlLWXtJEKOpjzsb1u2rG-ZSAiJCogwagtPvCnMubSHYwMMC9iQiLjphJtNrs8JmdnwJ_0MGIyd7pkbLDXpDF6PEqKxwlB3vdUf9o1p4_aSd5yaxz1gVNxzRZokZWhaRuiyHaKIeJEqqCnjXS6n5VgLNGxCNuq7gk1qM-JsL5MnFLVgHwXlAVtRlzQmrCsXld-KxzZ_NQkd7yDMHFTiAhQ-0SY6ImpWOLaOSs2zuoJJ9injZDxvJxFDc6DPbxvlwsTNA44nr7xKANbwrVKg5R1fImG9s7ieHVq_xf2pM8iUtBbfABZLUFWyWuW42ixMJq4GiSC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/29860" target="_blank">📅 12:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29858">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxWldIdBKC-c4_cbgqqIVnBkZFVh8gPViMZL7jbxDZhtK1mySdo8tj_97lapDnWzMLG7KCuJjOE4bxVTLEjKAkydcbaTFpZUKUwRto24pAyklWdd8-4er7MblxOF2o0WS_ogapRgaugDjCmpP-9df-qdQLTOxVl3WbPv6AfWJnGDyA7tUlp1F6Q9CU9C4SBmXoReZrt7Ny-VeXtTstT1pHYpY9xUeqMaZTA-oMbCYd4wanUE-QqPL1D9nbiEDhNAd29SQtxlLP15sxlR7sjiSZ76bJij2A2cCsB0F2Z49joCR0tPRciTzyIocjKs-SHl5cL0Xb2qw9SOtcckzv2QzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه:
پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه. بقیه‌فعلاحرفی نزدن باهاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/29858" target="_blank">📅 12:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29857">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ula_GVsUMOda3StiP63AJS4rLLPjz-SvkHem9F9mckdgQWhW8JnMnQKuyo61vHUkBPlac-HedmzpUcxmq84BhZMUghXEO9Uf2qPH43rWzh-HqOHjZGhWIitdZxQ2JVP0putgit8FWCX3XzLq2MSjHbm_AlU3Feiyh0LpEAsAHXR1dRWCdpkGAwbWTrN8WCsLPJJ4-eZB8MA4yhYbtjKEJbnvimkJUs_U2hjvQFpchEOLVIZbtQQASf4rObTBRKKjioft-9FoI8b-8f8PL53P4xJUdeniCR_apgYmGiZElQReFXYv3Osh7dOixhDpNQ-MGQBlp3IxwjkTmQQpK5lLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
فابیان روییز ستاره PSG
: اگه توپ طلا رو براساس‌تعدادجام‌درسال و بازی جوانمردانه میدهند خب‌قطعاهیشکی شایسته‌تر از من پیدا نمیشه. تموم جام‌های‌سال2026 روبردم. تو زمین‌هم‌همیشه سعی کردم آدم‌آرومی‌باشم و بابازیکنان‌حریف درگیر نشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/29857" target="_blank">📅 11:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29856">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7JsFR1g3pXWmpfZv4vkZfZqjeJYIG87HvdRQ0ec-AI6JKB0BqCBmDl6UYuDpf5Eyru4EuLBJB9MJ_fJi0pb12e_o3Fygo-dBHAjcFDRvkoCdQOk4qru62P9Nv9f2Wvl0pg-wVq2rDB7heolvlQQv1zXDtN9I7ynJt8BxyCZO3YLa0mMIUrjUI0aULZhZvOlGijkWXPNOewxVM3NcXjHtvnAGORVcRLbI7HyZFTLNfOy300dX9tJPtzEdB0XSYjJcArtuswaxrbvyaGQJNuKtudfBsuBzZZSDcQwK-7p7TGjpo2UVagaTUz0GmUYk6xiSNr_3AdVjLbscTOZSLrJG1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7JsFR1g3pXWmpfZv4vkZfZqjeJYIG87HvdRQ0ec-AI6JKB0BqCBmDl6UYuDpf5Eyru4EuLBJB9MJ_fJi0pb12e_o3Fygo-dBHAjcFDRvkoCdQOk4qru62P9Nv9f2Wvl0pg-wVq2rDB7heolvlQQv1zXDtN9I7ynJt8BxyCZO3YLa0mMIUrjUI0aULZhZvOlGijkWXPNOewxVM3NcXjHtvnAGORVcRLbI7HyZFTLNfOy300dX9tJPtzEdB0XSYjJcArtuswaxrbvyaGQJNuKtudfBsuBzZZSDcQwK-7p7TGjpo2UVagaTUz0GmUYk6xiSNr_3AdVjLbscTOZSLrJG1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
⚫️
آنالیزدقیق‌بازی‌استقلالِ‌سهراب بختیاری زاده مقابل تیم السد قطر در هفته اول لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/29856" target="_blank">📅 11:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29855">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDP5-7CCPW07vFXZJ_tET7IuOPVGmTW65LrZUJ0A5vd3XWsxAXlcpJHPZ4HGaXXLfzcq2DB1EaQlsKukYhMnuYdO8rfPs2ea_Fil4wGP5NIDRd3b6njUjua1B7cyI78X0Y_Wpd3jAFi1PKWAwxPoxqtLfms4zQkgpGE2vwtVoDkKXiU8dOrA9BxOzU9WCn_WDkinltZNJYrWvM03iqKsBExeF_gIV6NX9ls9S7hMEGsohOpr0R4hD-Njq93OP1HKspyW-7MDZhQe3jwEap0pu9DRf1p_kuqNLZ_wPgjZtwcKs5yUOyEwM9gm1DFwZdMtUHI9oqmkGurr6vOkugPByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه اتلتیک: به احتمال زیاد جیجی گابریل ستاره 15 ساله منچستریونایتد طی روزهای آینده با عقدقراردادی10ساله به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29855" target="_blank">📅 11:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29854">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU4KmUHs5y7fkMz53oiCRHISQyWbhi4jAJTTG2N_oblwqCrGLuQ6pxnfvbrqXvEQ1QqfZVCpneH5-3PaeF1kZATXFVZcgSfgMAbToRDlfW4hxFrBREf2o80-AyBq6iTEsW0XSUEhWTtPtEbvIuVuSNsI3eVw6wdXda1iJTwEj6yK4Q6tjDCgVOzec0IX8g9O91GdMut_P2Z6V1kT8iv8yf85jlLbasGz2GRhrR03EkBzBvn8_Vr1FyGQbYui_ca6tMCF-NPpepDdk9rqHrh9bslfrkCZjyMPS3gy56mhX9bqdjEYWMhGMNNbjdYK20HrbFrS5m2Yv31F-2ZpqxnMdqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU4KmUHs5y7fkMz53oiCRHISQyWbhi4jAJTTG2N_oblwqCrGLuQ6pxnfvbrqXvEQ1QqfZVCpneH5-3PaeF1kZATXFVZcgSfgMAbToRDlfW4hxFrBREf2o80-AyBq6iTEsW0XSUEhWTtPtEbvIuVuSNsI3eVw6wdXda1iJTwEj6yK4Q6tjDCgVOzec0IX8g9O91GdMut_P2Z6V1kT8iv8yf85jlLbasGz2GRhrR03EkBzBvn8_Vr1FyGQbYui_ca6tMCF-NPpepDdk9rqHrh9bslfrkCZjyMPS3gy56mhX9bqdjEYWMhGMNNbjdYK20HrbFrS5m2Yv31F-2ZpqxnMdqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌دیدارجذاب امروز صبح دو تیم امید ایران و امید امارات در مسابقات آسیا که با برتری سه بر یک ملی پوشان ایرانی به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/29854" target="_blank">📅 11:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29853">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29853" target="_blank">📅 02:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=kiX87__m3doVE42jSGJi0WI9VAUuErxZxNfp8dETTy32ZouY3vuNRRx9HtDZzJLSVJpHfb0K9Ttbtfycw96iNlYnYOnQ5QRBRlMXJy3HTJS9Sj3ocAd_UPaQR979YqH7679IpjAvNOQUjb3HR9VP21B_xjnkemRCwoxAm5si2SmG0jYMN-7XUulAdLAsIE-3iEXkwGzhPcMZOQCwUyvDTtMbgJbhuHYn5Tp2SiPFsBmtSxe3bKODoP6NUZF3PDXFgfFfT2xaoietlYE4dVJBVGgKiBRJgqcVYyeYetZRXmGbiaj0OBS1gAVLPX72QOWn95LcZwzgTAUk9b0jjwQCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=kiX87__m3doVE42jSGJi0WI9VAUuErxZxNfp8dETTy32ZouY3vuNRRx9HtDZzJLSVJpHfb0K9Ttbtfycw96iNlYnYOnQ5QRBRlMXJy3HTJS9Sj3ocAd_UPaQR979YqH7679IpjAvNOQUjb3HR9VP21B_xjnkemRCwoxAm5si2SmG0jYMN-7XUulAdLAsIE-3iEXkwGzhPcMZOQCwUyvDTtMbgJbhuHYn5Tp2SiPFsBmtSxe3bKODoP6NUZF3PDXFgfFfT2xaoietlYE4dVJBVGgKiBRJgqcVYyeYetZRXmGbiaj0OBS1gAVLPX72QOWn95LcZwzgTAUk9b0jjwQCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛ صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29852" target="_blank">📅 01:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29850">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBdJGP1Wfq1vmsMHEZIYOaDeJmZD2sLOsgUXKLbGGMHEw0RGHG4BWtf3AVDw3K4tTBJQZE4FRx46DWFsdRAsYfdj1AIE6SgawgbMxsdYpytO_lw4LnMgDdQ4oOmZz-W5zg0M4POHp3-VUkH9N8d3wxMHfwWQ9POvWPohWMnSUEFDVmQ8N-yRImIHM4oAUAK8iCTkNy-8i9cAABFnYoV6iifagN7z1GO7yQ9HCv5z1-T0wazRPinUJLMkoWAgFoEsU73ZT3wcLVzAaOkUha7d5Wx-RdbG3e8Fo8QldTaGWCLav1sHWXkaohfeD-JzzOf26zpOcDysJZE3-fbO-pQ1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ از دوئل یونایتدی‌ها با تیم آماده برایتون تا جدال بارساییا با تیم تازه وارد لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29850" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29849">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeoIi57ehT8BpiOSLCOXU3wGISM52GrXYlyCbzFax3WzZ3nEs1lglW6fEm1HA0wJzFNpPIo5oXUt7EyzZqSIcm-qLAXvCeCrru4bzaauxec8Lpq9mKdlw0zDLB6tYkD1zKV3-GOPggmG8lwVibvQ3oEn07VVVKmq1I8UXutyEyx81ryfvqi_J3iRAq3-QM9dvG_c49lq7GPfEEcx72hl3afMJsEJta5kSO1FezQt2sqzeIj-oZY4RyA8twPFkSPtMnqfSn2RSHMnqCjx7KkLm4sUpa_cZP57v7HfTipXp51MIeHPsFpeGXMz_KTbThFZ5x441RWrnJeLl9B57rb3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
رستگاری‌رئالی‌هاباگل اسپی و پیروزی غیرمنتظره العین در جدال با یاران رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29849" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29846">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCimgnv-UdOjxeBCN1JCFGQPM7mcMtng3yzhwqGaeTg8RbbrnOqyq4WG1dZPuvtmoVUu1mbF0NovfOETSA5apfLXgbDEnG_BfwB52MK60B91Dql36ebKPcl8PI2RZs7eCK9nuA76rSkWdWYMGEvg9k2XJrFMZ3Eyn7tNIV6kwWbKEfiYdk-WHTmsrNhdJ6CV4uXqc06ZEXctvCUA9HwhGa8R9EK_0SdY7s_bflgKli_Nmz_5Z01RBHM9Rx2QETwnqw5o3qqt-g-12HfFNaes278P2RsJHycIU65gngai9DHhc4OEjTuWjyHJSbhmCQIACd5ZDLLr2aM9vgIkvnVXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ مهدی تارتار سرمربی پرسپولیس امشب موافقت خود را باجذب بشار رسن هافبک عراقی 29 ساله پاختاکور ازبکستان به‌مدیرعامل‌سرخ‌ها اعلام‌کرده. بدین ترتیب پیمان حدادی بزودی مذاکرات رسمی خود را با ستاره سابق پرسپولیس برای بازگشت…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29846" target="_blank">📅 01:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29845">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw57bTXuAjElbw1gDPF-xO8GSiS_2_jZ2qgGon4aiRO87oDahMxVp8iOh6UXxxrEsPYlM-tJKAuTajpPPA34B9inkjG-4PK8rRUREMWwzlO2Z1C76F-mGYG-U_uzrz9N9R69A9qqXa3N5_TXwOzJo53ahBFtDQGyPLyiqSVPdTUw0BzgMBLqWBm9PDyMWfOrlmVbivIws-RTGbM-8M9nK28xEjq73EzHjL0aFrBws-P8MnMnkmfZO0F0pSeo6eZ563IhuTlWYW9Da07QI3csCwc88lEYY5IiIIN0wcbwyqmoc241LE6naoNXLFqTyOHmMwpsjz8QDZECjoAQkBhu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس تا اواسط هفته‌آینده پاسخ نهایی خود درخصوص جذب احتمالی بشار رسن هافبک‌ عراقی در نیم‌فصل خواهد داد. پاسخ تارتار مثبت باشد بشار رسن به پرسپولیس بازخواهدگشت و مارکوباکیچ و دنیل‌گرا جدامیشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/29845" target="_blank">📅 01:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29844">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_02RzcWOdTTAeDb1Cx_t-DaeLb1GiuUcP72CyfiyH1a6yPbjK_d3lQW5wY4-LGQyPXe4hS0psZJbNH_16EdcJw9H8CNtnM-TlOOpzdsL4F0ZMQ3SJ0eNUgb8V2CHLolKiGfhsWEtMPrszLZNSP6kgvOJagpUlBCmROMmBttB5mY6HV_sUtYlIAbn_wklHLVbx733VbbZnG2mtQzBfPOVjGQXAilOqPcn0aRyA1z_TcQy8YlkBJoegd54dvfRQjHIUtlQvaBL_iPAbheGEgX0ILmeT5wKMzFclYDG1ffbf8PWA1JCngdOHWS-cVl6G1jtwRy6932MAaf8rc5-wWpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/29844" target="_blank">📅 00:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29842">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L68F1F5JF6moj64ueQiw7_99oqa6BJ3LqL5mWTnghco3sfjk-v9XtkcsIJ91Jf4sEZSIPJnVjy7kw7GGNch6a9yIlSE1FCClJtUycpkFobarmAdbRhmF_1Vao3MYfNFQ0KtGsuLURfy7wjI5-X7rltNg7h_TcGDENTGfxL45CZpTgA-2p80jrX2SvmAZNEmF6SuoUDoDXph_KpNgFPG2Pxfk6T_lwV45k7sJ0prIeUOTKU1d3UwbyxYf_fWM4_opwnWR3O0OWBoLPWlDCUYkuC2Q8EVDlVptxA1pgmqOsstQ5w8nyIF1RjX-gCZvGU0jZSCCP7c2NHpS7dZIWzx2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29842" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29840">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHVRRl-wM629S_BG_8PynuMAox2cbPgHVfaGg1NR8UA0hhZdDfyyBN2YPQSh5PyCEDZtHUpjHeD_k5cunnYyD6o-lFdEPcFO82M0GoJwZMT-2SbmYE0kWGyHVFM3euHE1LEjqfGcddTv9Jxugoty9VRupjFzq97mUqP40a9U7-fI3GLTzbrkZDNx2InTVFGph6OrdAdc0SoBcUPrPOEFY1L5vI7o4V3nqIK8NpFeMySu83pCw_xj5e-lt0PQvXM_AXdedia3HjhyWbMocHbx-_Gn4U-xa8jaw4gHZcgQAg32fccxY7wwPlLlwbXDdVcUIXFhL6roshMuLhwv44NwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auEbOyAwVUake6hHYQg4XStpQWvIYCGhVGPTov0LSnjaX-gVh0kA4wfNfZgT5b_R9KNQ4ZRIKmcfn4hHqNzQ0bh8yTsBx96hdc6qR8hZdsA3Pn5g-psSPK1NWVefMJ5FLzWUmnHS6v5pjU4ab3qpUsnZDkJyGkyLktTQObOTm5CZbWlX-zEounTO5-OpXNKbuPdJHBGOjVJgLzz6xXwqGl6p5aqfehv7sTHiP4jG3BSw_3mx-ejTqGJOqknvOGoxm90ipPibGNTWEfijC2hyvVmA9HcW5SPa-s5jIALleH3i_Yx8UmFeiZ-C1ud6E1UlSmJIuH8DaPhVxWeXkn2lkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛
صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29840" target="_blank">📅 00:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29839">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqvu3uKK6JT4TvlJISi-XktZeXtzB8SznIqBgCrGXZmPk6AmwRY-4gefUx1wKq_HzYgOo1SRLH_Upw40gGp-1h9ESnAzp06jq5zH0reAxfejbrlOjnSdPKOCI2_0CxjTGIQjibto-KqxenqHDq_ZuYmQEMeTgEJ2Tp8VGoK3OaPVleXuZSLwqULOKW17C1lb_bCepBbP0wM95ubddapkGM9ypy0jOcBGMUlzUJA4F16SFCwFZb9p5kCp6KQjm1vvSzI45QTQu4rEnda34EeciMyNRvWva01UCWSc47spMrb12whQIGUam11vZOcKHMni3uoL-mvCLA3OPt96ibKtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29839" target="_blank">📅 00:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29838">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=nEshzW8nCHauffLtHciL3ISpSIDUN0lm80KeSR1AkNHEueBtaCBVFFr4ZXzlVyVBebOjv0hNq5tHDRj-IIpER8SVqxBnEr3jXCr-dN21_GqlYi2tOf41QiHoTRJP7UeQd48qJX3H2TVJ38IqrLV6OI3h4SjEzgTgOlJL4fDX9y-nfttm6ls1ZOKwd4OYN_VEcSiUL7R8BmkWMCs6Ifkh5_sfonNAf46CO9mdI7xsrrZUX3dvtSI88MrI6JQ5W0uCD368MSxM1FLpBHM8Yop5cDppFamFNvmcp1Crib5fO_toV7obOF2I0CEEMiIPT98O_KKdehW9ZRWthwz7fZl0T5Wr8zXnIFsI_aUQghsyOcTOICHgqn_YyaqqtFkk8JWiRvaDalEvxKubIa_BDamdGImsLh3GJkq5J897npVRcot93tPTe8OFL4SkdJTDdvh6w7_MfEtcAzpwIG1mTXSgzt2affXOV4BrqxAmxMYHQH7A88mO5PkiLBttribBPmRJJ11tNyhWcOpIl5j2xyx7KbGy2pmhCitZLRIK3knx2Uoy--P7pOzpndfgTcssShpTnZ2IF9xdB5ozlIuHhS9ndzfJPnvdlA64VrNLD_0Yw_ewDzIlFIR0GmsYw4UOu9_nenHZs6rAKdsuj8ssgfoPXnF_GTYPAuwKyST5GqU1xJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=nEshzW8nCHauffLtHciL3ISpSIDUN0lm80KeSR1AkNHEueBtaCBVFFr4ZXzlVyVBebOjv0hNq5tHDRj-IIpER8SVqxBnEr3jXCr-dN21_GqlYi2tOf41QiHoTRJP7UeQd48qJX3H2TVJ38IqrLV6OI3h4SjEzgTgOlJL4fDX9y-nfttm6ls1ZOKwd4OYN_VEcSiUL7R8BmkWMCs6Ifkh5_sfonNAf46CO9mdI7xsrrZUX3dvtSI88MrI6JQ5W0uCD368MSxM1FLpBHM8Yop5cDppFamFNvmcp1Crib5fO_toV7obOF2I0CEEMiIPT98O_KKdehW9ZRWthwz7fZl0T5Wr8zXnIFsI_aUQghsyOcTOICHgqn_YyaqqtFkk8JWiRvaDalEvxKubIa_BDamdGImsLh3GJkq5J897npVRcot93tPTe8OFL4SkdJTDdvh6w7_MfEtcAzpwIG1mTXSgzt2affXOV4BrqxAmxMYHQH7A88mO5PkiLBttribBPmRJJ11tNyhWcOpIl5j2xyx7KbGy2pmhCitZLRIK3knx2Uoy--P7pOzpndfgTcssShpTnZ2IF9xdB5ozlIuHhS9ndzfJPnvdlA64VrNLD_0Yw_ewDzIlFIR0GmsYw4UOu9_nenHZs6rAKdsuj8ssgfoPXnF_GTYPAuwKyST5GqU1xJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه‌برنامه‌اینترنتی شب گذشته لیگ نخبگان؛
محمود فکری کارشناس‌بازی بود. مجریان برنامه 500 بار "حاج محمود" او رو صدا زدند اونم کیف میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29838" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29837">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5vk123rSQBrqWjpFt5cjs21JVG8E77z6oTY7-9QBETAcQehfS8MBtHOsnXfQ-2KUduvlAN2B-um4uXFuU-cu4NOY08-5qH7CMrDd2iyB764f4mDVw5Sx_VdLSqC7B62Q7Q81IQjyN8sRH_fqwxMphAb8Atk1-Cbo7mrvZKmqs_qLj-qkxPTrxtmfQyV6IfjQwwgg4fY58-iw0K5mfjUfTa5Hhsa35C1oD3XMx2nUULCdE0UBo5wdoKIFrO1aNrl_QE9JE2YG4YPpyyKW8UH_QUTcuh92Ik1KANYqpzkqCrfqa9wvBcrw8SIVrOAjF-CRhh5s6k3grPqU_4Rfn_AFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رونالدو امشب‌توبازی با‌العین اعصاب نداشت، مدافع العین هم خودش رو چسپوند بهش اونم این حرکت رو روش پیاده کرد. 4 تا زدین ولکن دیگه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29837" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29836">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d67274da.mp4?token=h-JMvii-CtokTdQntHbB5nien3fvoWukgp8aoXsaxBRW-wbBn3HSlCsO7T_XzjkE-tl0Y6Le2uSRlaDaRrsjslBZL4zYPbsM6evgEfj7sUzEQqbiJiY7U0vj6BCdckFZN2Si1i1G4e6zu0wubg0bfmNsuGwP0Gwd9gIcTWCpSDC65BSyp7YBKlXgdoPsTKLbmVfRNVpNqMsANGVgrp18APU1yX93JGvqvlsXT3mDCFRGoLUhbwNU0cHTkDpsCY_mpUGf-sAdjgDE8EqzzyAatfQlOYIMUAX1E-8bHO4kNyIjeq7e9WO_Uc8yNcA6ka0fWDujBq7zcbxypOUhIcce8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d67274da.mp4?token=h-JMvii-CtokTdQntHbB5nien3fvoWukgp8aoXsaxBRW-wbBn3HSlCsO7T_XzjkE-tl0Y6Le2uSRlaDaRrsjslBZL4zYPbsM6evgEfj7sUzEQqbiJiY7U0vj6BCdckFZN2Si1i1G4e6zu0wubg0bfmNsuGwP0Gwd9gIcTWCpSDC65BSyp7YBKlXgdoPsTKLbmVfRNVpNqMsANGVgrp18APU1yX93JGvqvlsXT3mDCFRGoLUhbwNU0cHTkDpsCY_mpUGf-sAdjgDE8EqzzyAatfQlOYIMUAX1E-8bHO4kNyIjeq7e9WO_Uc8yNcA6ka0fWDujBq7zcbxypOUhIcce8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29836" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29835">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=GEYd0SI8k6nUlVwbAExMV5taZN8TLnmbuuqkp3B5KbmQsmcYVMqwXnRs_9OvriciEYGY-hMn_XE1ZLVdm86Yp1sECRswYLxO7s0fCeMeDodM0CgC0zEYwlN8aS00dLmEoaHqR7R3nAFC-3tdQxYS2SKCWb_AGYlRqK868qoGtiAx7BFY4w4A6q49EktWStfGjPPR2PUusQcYGmp3Flxm-e5muhfgkOj-tBbnJw_J_99xBYJhzsfw55n75C06cXsHIxql1Aj7GkMBkhe3El9Uz_Cqqwjr_c1EyCEwAqfSnq0fzRgdgHbWiZNWvbiB4_rfrsv9OZB1WFT45zhfWLOo56j6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=GEYd0SI8k6nUlVwbAExMV5taZN8TLnmbuuqkp3B5KbmQsmcYVMqwXnRs_9OvriciEYGY-hMn_XE1ZLVdm86Yp1sECRswYLxO7s0fCeMeDodM0CgC0zEYwlN8aS00dLmEoaHqR7R3nAFC-3tdQxYS2SKCWb_AGYlRqK868qoGtiAx7BFY4w4A6q49EktWStfGjPPR2PUusQcYGmp3Flxm-e5muhfgkOj-tBbnJw_J_99xBYJhzsfw55n75C06cXsHIxql1Aj7GkMBkhe3El9Uz_Cqqwjr_c1EyCEwAqfSnq0fzRgdgHbWiZNWvbiB4_rfrsv9OZB1WFT45zhfWLOo56j6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
توضیحات‌مهدی‌زارع ستاره‌جوان پرسپولیس درباره مصدومیت‌عجیبش؛ دیروز  پزشک پرسپولیس خبر داد پای مهدی زارع در تمرین ریکاوری امروز طی برخورد با یک جسم تیز پاره شد که بخیه زدیم. زارع امروز خودش در استروی نوشته پای چپش به شیار تخلیه آب گیر کرده و اصلا هم جدی نیست.…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29835" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29834">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=VGZooCC4DyoOHstc-kG5QWDZGLTEOJFgZ_xUXjodeTA_NSasdhzGu8d9CBHSxyldWHCTeAoWuV6qI1-iyPXb8sSK3BPL9mvvoYPFYyKFpyC5sz5DovUjORtcG8BP1VQTJuyagfy3gwbEniqWc_5RrUdz-hrf9T4hpp1fNm2i_S5lWMkimCr0xwbX7HqBMTykv2kZtxGJSA_Av2qVyMsJ66fVEWn65KliRjNZLjErLv___hehLwHBL0PRXNALS35ZKoYDlbPRhmB74JytVC9aaM51coAx_to_GqSlkVyHtyl-_35HMux5RUMry-A18eivfO04p6LsbF-AKUx5Q0fUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=VGZooCC4DyoOHstc-kG5QWDZGLTEOJFgZ_xUXjodeTA_NSasdhzGu8d9CBHSxyldWHCTeAoWuV6qI1-iyPXb8sSK3BPL9mvvoYPFYyKFpyC5sz5DovUjORtcG8BP1VQTJuyagfy3gwbEniqWc_5RrUdz-hrf9T4hpp1fNm2i_S5lWMkimCr0xwbX7HqBMTykv2kZtxGJSA_Av2qVyMsJ66fVEWn65KliRjNZLjErLv___hehLwHBL0PRXNALS35ZKoYDlbPRhmB74JytVC9aaM51coAx_to_GqSlkVyHtyl-_35HMux5RUMry-A18eivfO04p6LsbF-AKUx5Q0fUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29834" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29833">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=PGCTHdkU6apsmgyX18_5WTqOBUpDBa4hos5w-8bho6XF1DyOGvHHxQj0XsPdfpVq0zQ7wiOcxqEJX1P7A0XnI3G0_74XsbRER9DPq6OXce6wZBxokZKt41BRDiUTNGWbLTqW_RUOToWfWPd80XTm_6y6RyVD4y-V6FpHl7Pb6X4lAW3wV3cSlZh0foT6tOivn6udrqp8kyjnZVLhK00yeNnpOn1AbiKsyp_5q3iaybtDUMEAdBV-cwNz7mgYuwmA7s7b2KXjJ7H3K9iXNDduFxssk9x1o7D4H0BwfuZhtcLO-8RiaUju8qZ5X3Ch7zPC1JwxqToPU5-Kgx_PlLqVuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=PGCTHdkU6apsmgyX18_5WTqOBUpDBa4hos5w-8bho6XF1DyOGvHHxQj0XsPdfpVq0zQ7wiOcxqEJX1P7A0XnI3G0_74XsbRER9DPq6OXce6wZBxokZKt41BRDiUTNGWbLTqW_RUOToWfWPd80XTm_6y6RyVD4y-V6FpHl7Pb6X4lAW3wV3cSlZh0foT6tOivn6udrqp8kyjnZVLhK00yeNnpOn1AbiKsyp_5q3iaybtDUMEAdBV-cwNz7mgYuwmA7s7b2KXjJ7H3K9iXNDduFxssk9x1o7D4H0BwfuZhtcLO-8RiaUju8qZ5X3Ch7zPC1JwxqToPU5-Kgx_PlLqVuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
درهفته‌اول‌لیگ‌نخبگان‌آسیا؛ العینی‌ها بادرخشش خیره کننده برادران رحیمی توانستند با نتیجه پر گل چهار برصفر یاران کریس رونالدو رو شکست بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29833" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29832">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRbDTt8IuJ_so9vT1xj1_uSTsxyoE6JNX0CU0EffJvhacqnddblClaiUW2z71tJGPoHZZjgH4zczCWCdvXszVul6QfNtXUesz5woESnOaZHN7zs10PfCOj6C_7nHML_RyEqtK9buvGkaxQg0jPCMWUluYnD_ul00S3euZ-sEgxz4ss6j47xHwcQ8h7wmAOxNCLNVT8chb3HX4YP9SX68A5JQqZImEt5e5eJBLHWc8egkfnh7DbVLUqTKj3YXuzWvbON1unMQrigZT71kB1i7BFZNgsPxhR-R53Ilydxh6CRPpWV62LGSUlWCSwEFIVAP3IQQ7aRQinpCgS0894djOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29832" target="_blank">📅 22:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29831">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3q3t5gFp1i0N_TONPZ19BQh3NRPrQfeV_SRCnzFzzOjxOvlhRswHApMbNWW3UzkeDmQ-8Tg354aBOOZ-Mja3PFO-NT0aBb21FExO36ZQ6AI5CzlI9J6n5t5wvSv6LzqLGR_Eawht_zyC6YD3DuZerbM-ga_e5vxyNvi-WhEIM93WFg_UdcrnkRyKidNtE53y9VZt1AgaKal44g09RV_UZe4nMMo5NhEOdFFkDnDnjKq3j3uqdDLkZY0W4RAAvJAroyXp0HtaGA4w6_F87NnUyEdK9o2mQ-5O7fBkfD1XDId691psEWgNthHAvZAde7DMNKkEHZzERoWm56NkSOljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29831" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29830">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-ZvH2PgOfeJnYJiQZUmYgHhxkwQFpQhQiruTRpd62xs8ZYPVUavdlz0CuDwd-InyetJiKwG1WWwXLYlr5qIbDJb5uTPMEIwnIijUY_LwLK-8D_X4P9gNQ6iV0iCy2w5XwMspYwAkBGpGgkMHWkbStCW30dbwe86_KK6Bb89wTiEjGEa_PUdPjq64r51JA8W_RDM8VcoCYm-cQcJ_XZ-fa9FLwxsHv8xWLyoPlArmsV2IOAR0CZtT35H3W0oTdX2mxiY40q3QGgZqq2CRF-7vGIxdzXpYFVXV1Ed3Bb2Ih7ZCb2rVJUL8yQ2RSArj41Rb8p11HqGS2GcHyZyJ2RTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛
شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام
در سایت میتونید مسابقه بازی
رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29830" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29829">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvroLRreFCTf6QJvevhvMU8jOr1gwBddhpi-ZsDL3Wee_dR4Ri2QtpFXFf8U-aBMyFjddk0ItDDl6aa9tUvZkGEI_k5FZ8krs2lvFEa8JMxkj6xFxf6m3TY-horxc5OGOS-3zq42IItMMGq0KR2CL9A1U2AhZTMlUOIIhp96--1brp9RSRBR_HhIdFy8oUuIEsU_2Vo8Qyvyqi9eHy2VVRaru5dml9SuL59MyJpBwg86qtD75tB2OFTNJpXARcDiYygtHD_3ly1FUKbn5zzrdp32kH1tWuj3LaILiU3QQC1bHMFAGqFxgFPGCMVLh380bcIuhCAkxypim0EXB8yk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇨🇴
#تقویم؛دقیقا 11 سال‌پیش درچنین روزی؛ خامس رودریگز فوق‌ستاره‌کلمبیا این گل فوق العاده تماشایی رو در جام جهانی 2014 به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29829" target="_blank">📅 21:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29828">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29828" target="_blank">📅 21:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29827">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=ImuTia9bklseH29ptesWo2QeJpfQU9lLMTB8ITAYuK8rTcEuhmMdTDQd4-z2UEwp4-T-RjlYWdOcx8c0I_vjeiWT03EJUlLg2z5vqObWLNSXDpOhfWDnBrVD5Saqn8-uSNiFuBQhx3gNMmg4umRwOBYWg9wOPUd9OeGQqjGjm245b_1e3cKV4P1bmbGtU6UOEN11J6u4GQRlTrsVTeTxqrTVuua-mS7EjgqJrmfU8xLbN2OxVHT5liuEKX0dGGcIxVeeyRV2iyyBwa7_1-PTOyvlI1c7pgl6PQ5S4XWYL3WSoLJ5nFukiC--geppjf9UFOc9bpnpEL1WJ_PmjUCiXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=ImuTia9bklseH29ptesWo2QeJpfQU9lLMTB8ITAYuK8rTcEuhmMdTDQd4-z2UEwp4-T-RjlYWdOcx8c0I_vjeiWT03EJUlLg2z5vqObWLNSXDpOhfWDnBrVD5Saqn8-uSNiFuBQhx3gNMmg4umRwOBYWg9wOPUd9OeGQqjGjm245b_1e3cKV4P1bmbGtU6UOEN11J6u4GQRlTrsVTeTxqrTVuua-mS7EjgqJrmfU8xLbN2OxVHT5liuEKX0dGGcIxVeeyRV2iyyBwa7_1-PTOyvlI1c7pgl6PQ5S4XWYL3WSoLJ5nFukiC--geppjf9UFOc9bpnpEL1WJ_PmjUCiXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای‌ایلان‌ماسک:
گوشی‌های هوشمند امروزی تا پنج الی شش سال دیگر کانل ناپدید میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29827" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29826">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_jViPPuef1s9R7j2Ez4xKpgU76kJxhMgflfqDI_sYdjNJXe-99XQxyOmdZH1Tw_Mh8C2pfnad0LMN8xhb_s6GUZ25RnwnwxuUUiFCroMb3ByXO0kCyLgcgLAgP7YLhSFiHFUYSh6q1jEkGt3Rss93gYn_DDZ2F2JEu7ywFaH3KlYx37arBebAvko4FiddtK41Ri8YbHyMRB-YITpQFKOy7gnFIHPN3Auccrim6SFmKSywO72MUXYitwfp6XfyxMh2VU65cqenMAjYh4235LEx6mNR5O1xz3knxRO6u7dWP9EiBfeuu9wO_lpEo13wjlEEQvp37jkq1Ts9BsYe333w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29826" target="_blank">📅 20:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29825">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXbX8auptH-YVzH_hlZzAFQqRDxoQmqTQpjMpOYKpJaw-goU7cW5Oz0tyHh9P5UNGKfKc1Rq_PGTLHxv_lhkVlWr5OZIqdX_sIe7-XWStjHbVTkYh7FmDtk7rjRYdyPvpIOjmJoq_3Bq9HSQDFaGwVyUwF7kfbYTWkVJppJ03wKrWAqfJKuE2RWnmwyEbABQymo6y8f-VL9f0BidN3xVRKVU6U6uohTfX4MCCJCB8UYnaLYVllaGEEseVnPgT8OwAOEI73yt9tECBoXkR0IIm_LqHH1Tlogdtp4_Iee9mRvgy7khHur1etEvx7_SoVrbCCNEb380SGh4FtpGyXZ2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
رودری ستاره30ساله‌جدید بارسلونا:
رد کردن پیشنهادباشگاه‌رئال‌مادرید اصلا برام آسان نبود. بله‌ابتدا درآستانه‌پیوستن به رئال مادرید قرار داشتم اما بعدِصحبت‌هایی‌که با دکو و هانسی فلیک داشتم تصمیم گرفتم به پیشنهاد رئال مادرید پاسخ منفی بدهد و با باشگاه بارسلونا قرارداد امضا کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29825" target="_blank">📅 20:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29824">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de2283857.mp4?token=L8tU3y7aq9enCunRpJWj24Bgk5n7Kx88xSILYhYlDk1ox2JEwuH0Ry7OGJBXU4CAdSxG4iN5nk6OqpowR69mGKWvfOTPT-AvHQah_myXKsVHnryfXRoijeS3WQshx1qKcjDPSMwDpMq8c6ipkimBNtmncm5CGKnbo49VRLACZ62bavc0GLH6OF9SQXiLFJ2NlS_kCSpz7VAVnoFkRhAIhs5tvErEqPBTopLwHAlYBcu4tCJYBahAprBTMZIA0ON-gi7XuXfgh7_9aKbEUQ2cYbA6LV_lFRZqMJ4nhbMqo3as6nkjvboA8Y4gmYi8JXZ65rxNFi5xWfRUPV1CdkimbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de2283857.mp4?token=L8tU3y7aq9enCunRpJWj24Bgk5n7Kx88xSILYhYlDk1ox2JEwuH0Ry7OGJBXU4CAdSxG4iN5nk6OqpowR69mGKWvfOTPT-AvHQah_myXKsVHnryfXRoijeS3WQshx1qKcjDPSMwDpMq8c6ipkimBNtmncm5CGKnbo49VRLACZ62bavc0GLH6OF9SQXiLFJ2NlS_kCSpz7VAVnoFkRhAIhs5tvErEqPBTopLwHAlYBcu4tCJYBahAprBTMZIA0ON-gi7XuXfgh7_9aKbEUQ2cYbA6LV_lFRZqMJ4nhbMqo3as6nkjvboA8Y4gmYi8JXZ65rxNFi5xWfRUPV1CdkimbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایتی‌از عملکرد خیره کننده جیجی گابریل ستاره 15 ساله تیم منچستریونایتد در فصل گذشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29824" target="_blank">📅 20:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29823">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLg4Sx2WuGVPDL4ZhAACjCcs985un_6A0NkjfLpOtH5GmyTJJBU8bqI3dSpr0-1z3iC5i4tgSWWhg9JdpEr2M7hhxH9ZYPl__BAaiwp11R_oHf04inX1EEWv5XWPo7ZafH2Fpc2CfX9dlNaYw62idkKSM-sgFP5Byupruh5p5KajegVSbDorKg8PX7-BGwbQBXeMl-gSY8qpa3iHR9m5J_77-b3PH_TPiNj_0EZZFQCrxxBRLU16kP7vN3txrvO14fcG-Dgwv58t3wpp0f02wC2aze8KluMQi8Xl2ihmyg584vmNKot5XRMjYGwoWPRSKWwSjTEHJdJ4_MH1oamcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق به ثبت 27 گل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29823" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29822">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGs9GBOy-UFEPuScC5Ks8KpGAL2yBay44i4zTj-JFrBhI9OnusGVBpK2mRURuZU6TuRec-255X607tYKVAOVEklqHO707fHbpfUT01NYaKJ-iVBp7wfVFwbCG82BoqvqghDIs_jXoQPEs-mLexIwd-EEmUpYZxTCMy5238qvHB7jJ8jAuNr4dJXGEpQU_K4-nKAReVileHw-IIErHl2YffVp3wAb6_GXe93Wij-nRsj5_Pe8FCNRQT-6SX_-FGbDBBWdRCtL4iUEsDYZ6S-tr6nYfXLGynjEzeuOfZ3AOiFUY10DGZ6hT3A6K0aBimie0fsaSCi0bEJfmJha9U41Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29822" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29821">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8dtSNYSh4IsRQdhLQ111RnFYyg9GhaZYvNo3AVgKmWiE5tQfLnepltQ0IwiTJqs5Ku9VWBh_uEEWtBCay4f5xeScPyTD5CYJM4UOEtLcFKZQeIzp0tMT30qbS9HUnIPgvuEaB7WjlBJuvMBiB4fxOvF8dcIl9C_AlB-zB8c3nBUMMHfvCQRF4GIrPbSwzWxwPd7G4vkKj3NKUm7xdBRzNTvU0RqHwbKKJEqptq8y0txPIWmXd9hJO8WQS4PQqnDJCV9q8t_GByEUiM27MaoHy5QtyiIzdIcnf2r2kOPKBh2qMXUJClg25ImYS62ykVYHRPvYQ1B9nPG0gLj_m7UKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29821" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29820">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29820" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29819">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_YagaCaOk3TeDMQHCNLxw7eTQyZJboSICWZ-eOTmxhvZ-LkedkmuWposG3BXqpjovC4XJlARqc148pGk6bdSdHD12e-3i9vQ0uwNPOzj4uwftdJ7SeyklEQ1J9qbyL2qgc8biUg-bgksQ3HJCI0gKlWO3ivKMox4r4Qe3gqRhP5OY2tO42gh3sHRCiVm6TtrhqB8JmbnbF2nm13qsGWLFIwolJs7emN8UN-F48txzpE-YA4wkjFPdzOM7BnK7HmyEUvqRtYkvd3GnCEIb93PiqVoWYoiHJi9NLYOHx4850qYRq49Mg05UPGEk0tlEuJOfVn9H3YrOgMFfBsECyXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⚽️
رئال مادرید
🆚
الچه
⚽️
💥
باپین باهیس؛ برای تو، پیروزی یک سرنوشته
🌐
سایت پین باهیس بابیش از400اپشن برای پیش بینی
🛍
پیش بینی باضرایب بالا
💎
🤩
🤩
🤩
🤩
بونوس خوشامدگویی
💎
🤩
🤩
🤩
فریبت ارزی ودلاری
💎
🤩
🤩
🤩
کش بک روزانه
💎
🤩
🤩
🤩
فریبت درگاه های ریالی
🤖
دانلود اپلکیشن حرفه ای
💵
درپین باهیس دلار با آربیتاژ 30 هزارتومن بیشتر ازقیمت بازارمحاسبه میشود
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g24
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29819" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29818">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3gZbnWyDOvmF2hW86_9cw3Zbs4ztmafpYnQwPUfKSauOWk50Q6_yh_rjPAfqGeSaJq3cGpjvOjp0UAMGBiVjx1X53fbskpNdpXtbTorTD3pwd7jP0s7-9grvMiimQGlwHdl2U21JAWWjm1SPLUDBT-5_G-4fIRF-OQKdB83f-b0wq3166POdlp3nCZNJju8CEpr6AlnxPVb4haqSa8fvpHrp0jQlhVcJOLF6FhaqT1HnnRlkLWbBoJj0rD5AtUTVsOzl2s7rjrUImLLaaai31uUuKnkrkoPUMopVy7qiZDPcvTiSpY8BFG3_xwsjYE0wFRRRiSfLHx5AnM2JFAb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29818" target="_blank">📅 19:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29817">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmFIWl8Q27AlHsjJmSPy2KSN-R-4CpFA8sM5PtZD6gGd1xRUN_t98LIS_wctd67mw96VCHEYS9_nDKCttsSSeZgmt2-sTpXxEgky3avE-RhHbAcw5WpgZAQ47-6fMxzh8H4e8ETX9173QQXE59RQ7blaETqwX_VX8qu1D0MvKk10eVA-1mb5C6AzwywOJYyQ_km6_P_xlP9SdBhue2aArgXWV38610T9I8giW8JCT0jJ2iErJ0ctYvIaClmUbKHfIyrS0v_onPgR0b6-0fH_5OPM4blGm3IlLwmYGVodFEodGOXPBxK44TPBOWnmjPmihjvb1MSCphS5qoqIx2AE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29817" target="_blank">📅 19:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29816">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf-egeZeABpSkupE6yRcV0ZiIwJZEssD4ovQxPEW1_0Oj0J2TNUHw_vHhHcbHPkBbG-DlUs85SpwZ2zpr4QtlugDRd7Cg8_vJqO5FeY8D4HyhTCXjCK-7rjSgnict9jInVC9Bw7modJyvCMx5svlMXtRYlQrsUmIvEoCjIGOScciUYmrUEC7sZF0iX2ab3sXfZ1CQQhjRvpwYI1UPlUhC_oS8_zyIWByWvJ9UqS72xFnKHZha6kNA88N-47OXYc_n7GZ0PAcv8_Awzfn9Q9AgG17KquUa6qZdDJYiZ_3FE0xSlKni_e3US3RkezdFWvKmQq8avtefnF5Nf8_b8s6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29816" target="_blank">📅 18:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29815">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Nn8IB3Uj1FoghQFPJlLhNiqaBoAuWjKKBL4k_EcheMywyAGMRH6GuBLxfoAX9776-MaZyY8nlT8ZN2MdSLv0m6JE0FRN0onUC2R5UCQ6amYbigxuuiYfbaeQ3pqOZwitf25n629Oth8K5S-WLkyXOxHr7MFfI2HsofZWJ_rv7dcYdCFxnaZxSKdAAB8yZj2kcMhJwqciOb1PymlKcWOXsxcBAZXjuVmgmXbIHlcQqxr0XBy7O0L4zOm9_A2h0arCxEKBKLWA1kn9UQanyAkehYV0mXOsBFrP1TKxm7QLSKQId054P8yC5754zyf1k29rAxx0IOOieUlAihwGo5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29815" target="_blank">📅 17:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29814">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlMzHRvFCmKN-HaQcw52B5JXFUBheHk77rhCYxnoDJusxp3HU7ol-q67CiHkI36CBgc7FZMdcXLt-mXX1JCojy6mw9FcieicBXSHsedMwpepGutYQK--tns3FbpUl6x3yRsdChCUBV0UxNfEfcnKfdP4QS7EoHoMe6EhUnnDa6DOcjnY_obkatvEKZ8FIe2RSeCN7wVfrKBWg2F4kbc4wyQWYjKoIHP9s8S73yCEyYYtncQZNzj8fcss_0OgW-A-0WnFAWFyqd80CYAaLT_4EUBZeSfqW4IijuXjTO6ZJe0eNOXkUipcTs6H1lT36yfWIdxaSBVt75MA25EsEwt4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29814" target="_blank">📅 17:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29813">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okyr2B6VBTDObiVBxbI9sbf57YVWJJGeYTCj1KqcYXTnJc0Vay9vZPggXVxv8EVLqZJ5gh6x4Aj7dKVsnm3xdRp7sjPjMzoSmNwSe-EF17fQUjDZ_Xfx_L92v7vNXUtTCSTRD46pX6vOuhx0JbMAV27RV8zX3kidpUzdJP4HlXPrLk1Zxdi4bxKDVMaGWOI7ByYAVj7pXhkre2ifWneY9FD2CyZLRzwAD6SLA4FZh1ZTXNtDcUxceygUgOWjl39lme88xh9GLKs4CpyNh8lF5RYyOxfmZFjChPeMKVkLdY5HOwKL2fVcU6EINrlt5d4Mrptm_sUhvHt5zAQiBQh5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمپین تبلیغاتی جدید سیدنی سوئینی برای پلتفرم Novig هیت زیادی ازسمت ورزشکارهای زن گرفته اونا میگن این کارهای بانو ورزش زنان رو جنسیتی میکنه و اینجور به نظر میاد که تنها استفاده زنا از ورزش این حرکتای سکسیه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29813" target="_blank">📅 17:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29812">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djYmHS87O8eQmpyt4Bnb38aVDeicOVcX53hgaOWY7n7QcBCi1-s_xTElybShbVNkxMI75fTX0oPBbZ2cx4yQd_9jo7cDUTAS004mOxvIFyAcIOJVX3NZVxDe6BmRwRQjU6Mttl_9kraz8AHf33QZogpki4h5YZbGk-HdbSV-IplzJJR_QhrW-yH8qdChHPuvHw3-ublqHfYxUiOi89WRcu5nTJLVNB7JE0UFDs9c_rN0fILHnfqG_WvQCUAEPg5Hic3eCqsb60gGf7KfxML8jCPNVah8W2pZ9K2H7zONjb-7e7Oa57PWs7CMsja5sdU38Z0j2wI6zUEFJS5asTusvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای تیم امید ایران در مرحله گروهی بازی‌های آسیایی ناگویا 2026؛ فردا اولین بازیمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29812" target="_blank">📅 17:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29811">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsTvD1_JavbiI3vMnnSO3VK1l2Ib9fbJk40AinlmC23jIeJC7pXhKPE1vxDwYRR-Dl-oWCwik1xGlGeuijDcoCe-JBtpxdMk9EcYwn_EiDskAnYkD_K76AF5D7CtZBpOSiOq0xnuHwN9sftG8aHCNdMGzNu82QEfZgOj_i--zwP5KgIspYQXhDnLDgLU1nSvPFiaXMRzgVTbzoMksjLB-Oky4-UOsJP4SbysbBdbsEzU5Na9Ap9wM6O20c69ptFJqLkB2Zn3EI-WzAgU3rT_RIWPRQdZriYPAUWdZVSLroEONk73ao2ZYOhgqjmB25MqZ92YLiezd-sZBmByWlCNGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ویدیویی‌زیبابه‌بهانه خداحافظی مانوئل نویر 40 ساله از بازی‌های ملی. نویر گفته دو سال دیگه کلا از دنیای مستطیل سبز برای همیشه خداحافظی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29811" target="_blank">📅 17:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29810">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQFxB-RwN4sqe7BRpyYp_QXsk4M-uCwbWmQO8nhD0FDvBPsXX53E5Sju2k5FCxQiZtwSOUWOj-3gEynnCGBwNldjQ4RDiMsoyIUHnG0iiz5qINYHcuq1u0SySv_nblbqY2_rHm0XA-NZb-phog9X3pbUTebeXDvD4WRpT6ZYmmzVVRUj1DMaFKJ3zS8eX66Mj5DGxe7moZDoJyIQG_zTcs6CDFt4dHgUKGaAUXI1fD42i0VZJaEkIpVbPJojxrLTc1MLaWTv-wP_51xJ6UmttOauv1KDBfAqpzJrzG5fOq6onoNojG3w568ojvvTOY633UBzV2lBVJ39rv98RKHqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29810" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29809">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJJfE-C0qsRKaH9CpqyiSJ2eykZRV76-rfL4Qc028DgUdNfGVhHMrzg_cxDOJyhmiRjo4zKqBpivnWP6CgI9gfklpsemusFnIHRzOHc6tUoSMhQv--Q0UdCUOfPG9S5EYykdWVO0FylGQASEAZs2Yk2GcTSZXUBzOPSd-j_idUmJduXpyoo2TjvAmTwVWBlOqSJC96Cr2fqpYRAf3Q8y9jzH-92MRc_4JBJ1MRVaThVqAXYSIUSVU1drDH7ZtY3ZINN8bNVMVVBeEsh6BSvamHjYZQxgh2RhdPHNgrtDpE7s0yg1jTL5Vuu2AVC3Fs9I0_KsiK2VOZnJgjEWg4HfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29809" target="_blank">📅 16:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29808">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFVZMwwhcf_5Nb7nGpqAWvllbKgtYk1E7VDW7vXqF6G8jD5tOagU2sjKoEKeBe-p0na43zONwdbfjcUnZGcm8r5ZHHCrlyOc-TGW1pwFTqrA8JTJjVFHr_kGrqI7g6PUTOKpw5x4G388ZdG17Oz3KG38xZ9IvRsemJF9qEhp5fh636X6X4tZ0lBkRrZrpBJoYqpT66E0uZjNEe4_vdXw3QH15oeXom1gzwhGMd5r2V06Vcm1f_ffdLb4T7IUCMtauM7NaR9ACdS0EHlt3TVUVn9fVi0WrxPEcCcCzJZbT3SaYoR7QxkdoqlVGGoB24C_oihjlq-EKecCcfQ0BvwbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ در قرارداد شهاب زاهدی با باشگاه جوهور دارالتعظیم بند فسخ 150 هزار دلاری گنجانده شده است. هر باشگاه لیگ برتری که شهاب زاهدی رو برای نیم فصل بخواهند باید 150 هزار به باشگاه مالزیایی پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29808" target="_blank">📅 15:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29807">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrUDIQUyXDRK3yVLrW73iIp0zjA_BAWQ1BFeCkRft2_viZHhf7Y4h1wm2YyMvWyM-GuUsRCMujZgbBaZZihTVDFi8OBI4ugGTHDc9kI7eHqDZR9AkjuGO7V_ogSngPP_RJMjAFnKI0pic6gCLa3qv4jA1gJiyl3s9tLL8ADKLA4Zl29Yl4BDMvzpkgTPCRai_wudYg9tdc-Ny0liylt9By5jTQTjH__JF0KhyuB6dwOXqhO97QX8hcJ_pwQ-FVJKwerskNREqm1TX9-R3QoZ1-cEPgvxbtcsXgUqyNFY2-u9xsCbdlQRm_TXWQ9Z5hlfPspyNMhvC6-gRAzvNzPM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابل‌توجه‌مفت خورایی که با گذشت حدود چهار سال هنوز نتونستن‌آزادی روبازسازی‌کنند؛ ورزشگاهی که دیشب‌استقلال دربصره‌عراق از السد میزبانی کرد ۶۵ هزارگنجایش‌داشت و ساخته‌شرکت‌های آمریکایی بین‌سال‌های۲۰۰۹ تا ۲۰۱۳ بوده. هزینه‌ساخت مجموعه به همراه استادیوم ۵۵۰ میلیون دلار گزارش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29807" target="_blank">📅 15:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29806">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAZUuudk51XK-HZlQRPedNCk6zRDZItPQlAHrvIj02C9uv_eGG9lwb8ide3o1hijov556zIYQ4wIrnFw77M6BldG48tBBklEMRru1LDBAeVa2psFGQPehmY9IxGMzqT-68v7w0EFmx-utn6rEH9yh0PuRQhi4fkvF3LYtEGrjwvuwJDy9LhpvZ4lgFbQPJfiq0K87aby09eiIVpCi7jwePO7j-9hq0_Rr4qhFlKMPrW40VXmC3S4fOWN7kOREXDOXAiBGJu8Njclk-cAcaZv6pQ9OywklAvYMgIUaCqXwQbL1icT6YQPlEiUQalli-QqFpAjHQG9f6yrCxfJwZ2Aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29806" target="_blank">📅 14:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29805">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdv7NG0fsc_QnztDr4SZkqPO9vW7cjBdFDYdN5T5-z5U_4C5oYQDAcwkJ8qbtyXto4EfVaqdKyqCj3beLB-WartrHygEryO2f8Yo-m7F8qcrnYCg7U4MiKAiNNhqfH2WKlNVHOlBprb4PhoHc2-F9JRwodtbJocqCYVx3HY_ciPj9bJ20U2w0loif32h7REl3eOGBt5a6pWrHdfwIbN6w2ux7iY4Xi9o4wLlykWazE9P8ZuKX7lMMZHeHK6q64WYha0xFiQL7VWu5XZt_tOy2fo2OBqt9g7DKn-GtuebQ63AfJQKpNFMQKDwR7tlkPPt8hcos6h553nqvUT-cB1MYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امیرنوری‌بازیگرسینماچندروزپیش در مصاحبه‌‌ای گفته بود که خیلی پولدارم از هفت سالگی فیلم بازی کردم و اولین خونه ام رو تو پانزده سالگی خریدم.
‼️
خلاصه‌کلی از اتفاقات مثبت زندگیش گفت. بنده خدا فکر کنم چشم‌ خورد دیشب‌ تصادف شدید کرده الان بستریه. زندگی‌خودتون رو رسانه ای نکنید لطفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29805" target="_blank">📅 14:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29804">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edMw7BRef3y-vmjjBHzMQGNsmYPOBO5QpUXp30FIGgaKRfYP9i--O6C5tmXFRiqDT5cdTZGXEVvglq0AQ0vOYjEpB8h_5qPeiUv0Cdef0V_J3R7POBL0qw2vH10i-0KXfKrsk9HYnOAQzq7qKgSV1Px9ENN9FWu5q9qTsya11L3fa_xAQfeavU56HVlscOzSrDDwbz0PR88lF668l82DkQHM1ybwLy4Ziv3rLU0Te1627-iJtUw5X0V_qCZMNjYSJAIC3ay5OP_P_0mxIhN_VCoOpZ6JmEL7eAJIDQ6yitl3UkCRt5N0qILHpkBCzCQkGU_f_PGevl7ZGDS1K9q3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سسک‌فابرگاس سرمربی‌جوان‌وموفق کومو در گفتگو با گاتزتا گفته در وهله اول اولویت فابرگاس موفقیت کومو دراین‌ فصله اما اگه درپایان فصل رئال مادرید به او پیشنهاد بدهد باعث افتخار ماست که با باشگاه رئال مادرید کار کنیم و سسک به اونجا برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29804" target="_blank">📅 13:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29803">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQDOBIvCQ1nrTeESfvDBhPTjin3Gm8v-AMQRXnfjC7udUuTkzBNAFq3LGg9XRL9YWhHpvGfwJV_BLzWXMPSA7bCuyQo7GUQ-upKvIaGTapgyQfkvHjnzmxChzQA9TZWMXI5u0Ax9V44bYb6Qa_69tOEi25rmA1KFgKZRCE_HaMPBFJseGScJBzKvBm5mRO6fIIZXzqIkCZ9zohsou0Nn0Wec6rjit7Pm7aOzlIX3yq1IIVK6Pui14gkd3su5QmQG4dHCAGkay2XVjRzt6qdSJOOv64jFP_dXjbg4Zz4jNyJIp9aGXpbLNjHo47pr9kmzjuG7wDM3VrlfYeFWFJ2S9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29803" target="_blank">📅 13:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29802">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzUe_SaQdWSH2cWrW9HvWl62BnyF3Y07NpQNSaY4dg63Nfg1VU_m4NFqTRVqyFvjcEP-PipZmX6ErAc7Myo8bANBJY8fMUTwglZZ8bQMHfxxoJkgmczkmdKIVHOr911BYYLuz5WRRnrKUCto2s9rWRQtQEIUFZjrSOej7rRugY-of4G3iDXDtfqCAgLKVu92EroIKsPx6k6PmZGPmF2K1QzGrv8ruvThy5QxEAt1N1dqlq3jtMwOr29tUOUZPHevBjPZLeqjTh6naFiSX0pr5OzmgFCLsKIi__74Th4MV_TxFUKI9qzrtql0PFicYZLMcsKuUxUevTTVC8aL83Igow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دراتفاقی‌جالب‌وبی‌نظیر؛
در هفته چهارم رقابت های لیگ جزیره؛ لیدز یونایتد تنها تیم میزبان بود که موفق به کسب سه امتیاز شیرین مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29802" target="_blank">📅 13:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29801">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecWs-CQvvDIdBwU47UpCBXi8VGy3u-0Z3RWJk2c0lFGw3_zWllQ9NNdm_UozBgvcsli47McUZOc7dMfnm_iA-uC22CvZxMTjKuSfiUN-ZKw3WVuY-NFmN8Pd89s2UIcNS-6kBsg_OWu5ZQ7lXDGS6lqMTvl8q6yrfS89WlCcSTzCdEzwqXV2Ga8d0bSBOoOOC13W6-KTElKu_yAfzebV9Wb8wMczcpZGM2Hi2wJwLfoRVb7ygAf6AS8ANvURCrfhBARkoeOgRN1IrVYBSEKOrvLoAmAxFVIH5K-7AEKgwyG-zs5vIXv9ePEMvyNABfCAy2rRUbpuTbLf2cIlcABAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29801" target="_blank">📅 13:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29800">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdYXPqOTu6AtI30H3ADGFmaK_qU5mdSka2txBGlMJYcVAbmztaRfH9DkmQI9Kl3GNRnATMGmbL4Z3Q92MPXzDMtRrbOnwF3Gp9eETkDx158zGK2B5hFG15PAE-laRvAaRcvs-cxQaSBr-8XBMSz02v0uzLHnIOhEKdbkQty6_KkSsvbkZz7W_PvPzzBfV02Q1oP-lHDVrPdLfg06VTPGB0M-beeZeAT7g1tEQuRuS1LjwM1meAQR13IUz-jg5IOJwNpwMW0VnIixrOju--Jq1ARbdL8enFqsibjVWcz7fnHfO4MNvaVPPtT6DNmNEngI37MexaHTSAxxExINB2U70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های علی قلی‌زاده امشب به محسن خلیلی گفته درنیم فصل با پرداخت 700 هزار دلار به لخ‌پوزنان میتونه موافقت مدیریت این باشگاه رو برای صادر کردن رضایت‌نامه علی قلی زاده بگیرد. خلیلی قراره با حدادی و بانک شهر در میان بگذارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29800" target="_blank">📅 12:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29799">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYCCaViVBIKPEPOW2W9GrCsB5aSwy2QQigpdsvKeca5g95JVnQEuyteuOv7lTkKdPk2psAxNSG8H_E2uqOhpM7b3nCZ-ATrJPKhjMfSmMhAPPOD1WOh_S-2wbqdAYiex0qiaDtixdL-44iYWgMq-1YTn1UYQf7vzc5cRtvmoFWyYNi6hMF5sORs9TwReZj4UU-LlH0uRapCQKzJcgNKiLSLcVNfLnJ5a7GOqjRPZj6D75y8j_pgMS9CohHcNEQfeDJDJd3754xrNwPpr382kQ6CBsGxxJwutokqG5b1MeOoeOWr_IhULStgNoqHchx1h3Thc3NQgasjE1FvFtHYZRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درخواست‌عجیب‌وغریب علیرضا بیرانوند از سازمان نظام‌وظیفه: مریض هستم یه ماه سربازی ام رو بندازین عقب که بتونم برای تراکتور بازی کنم!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29799" target="_blank">📅 12:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29798">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZRQUi-htMzmbghZt5lViinWnq2nunpJUEFQZJbMEXnNfjkF9-Au_YoqnANq6Xywm_XdbND4qhb3NOZmMfYO9NHgEyF9VGGjI1tdlFkm8397G_IKCqwaD0LkmlL7ySO1zJKubaY5ObE5x10TKLSvk1I99GsRBqewqDH-7nbBhJ09GjY68rmZRt1dPfK-nZxE6D7tA9WgYjD-VDcKtYONWmvmTpq2BhJpb5aQqNbPBNUWYP2RaD7Gr8R90gTD0IWZcqE50riEneWW0cJv7CLmJTuW6UNWRRpNlAu2IMO6fggT4EqYAn8ZQsZfM9Op6HvDvmMEWDjHvH_ZsF2iLNrO7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/29798" target="_blank">📅 12:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29796">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVLkyDwQvjfKKuE4sUvBWQR6BaXuRyU7uAMkHtYtndsEg2DL1LgaHZ7-o-wNXk8mgjGrLpnjsJ7a99LhmfJOx1fR910VsahW59dGYnnKG8jjWgX1cpPP94pHppn5WjfgxDdj2e5wRZpHy-7E8ofbVsr39_vDkTK1qHZVzCis77B6C5fVmjW8zbNTZ4Fa5OdFfaUzwrKBf3108JBl3isvBPAgFBnlmul_mxFjblr6eq4X93-thy_1wnIoBvLTHrzuWytNR1HZtAj3D-F6eFDZ4o4o8bRW23fzhjuSNh0hKKU09nI0xcxHgSRTYiHh2MdseSAVbAHZ16zNRU4Esx4r2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUkWGOiXUFngUM86e6UwrGs57o2fqhDS19HThJ2MSwqJZtACHkl5minezyOVnO8VTO33uxpipq_VS8qHP2lTeV2afTaziwJvkXhTcGr8wpbVpwcyKFmcqoUQoZ5xJUPrVN6ekA-y2zxwPpgz_g9BnBec5VAMvu3D8UOR2C4mxzYzNejgNrO19M8RYyxRybxcKYyU0euawc3n5lkfAM4-uJkJlgMgI6Nyul3jiEFq_GVFrcBbz4i4jzlbncY8T5itYNXHJvFqL3d0ecmBrDSWLf6qjiniD2OMdNSms2Xa8AvRaGRZJqmKkIJZfBLMhX1-t1mAS1LvOhQxIaicoDO80A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
تمام قهرمانان رقابت‌ های لیگ قهرمانان آسیا از ابتدا تاکنون؛ الهلال‌پرافتخارترین تیم قاره کهن. نکته جالب این که تیم الاهلی تا همین دو سال پیش هیچ افتخاری نداشت اما درست هزینه کرد و عین باقلوا دوتا قهرمانی شیرین در این مسابقات بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29796" target="_blank">📅 11:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29795">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUdlz5aXJxtpqCqT_kQuFlqyXHXfL-q8MJU8Ap4Z_WeUFgg-6k2cRjBYbNj8dS3By0cEeEW6U2c1E-zbMAmPwvlHIWgEghLCaCJOpYDSQ0e1UaMBLoL5gSdmsbY5Iezzf91mrBQvhaewykGToHUgNtid___p64mtafxMituEanrXcyyaQHb9oRFAJoXjjvnMv8IDb4WWKZYrQId2Sg_CDUxzpv2okMXOyK3AmFC0U9tNJxOrrFMC4XyyT_coouAXj1mFZZ8UVVUC8WwUkLTzYTYDyMyrlAgmhk3jUSN-vyOjr4KKMWIoq5O2AINgDs6wQyVONokOaE0aOrKckor0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابیو آبرئو تا پایان نیمه اول بازی امروز بیجینگ گوان درسوپرلیگ‌چین؛ موفق به به ثبت سه گل شده که‌یکی‌ش داور بازی مردود اعلام کرد. نمره آبرئو در این بازی تا پایان نیمه اول 9.1 ثبت شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29795" target="_blank">📅 11:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29794">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7ppbslrO456jGlxn6X6lb0mdydt3M4zEMvj5JmYytC0UrQXtOUD-W8nQyFtpdXIaK4vDPdiEFBQWveTx2Ulf_bl4TlmIzLCqzE3T_vnD-qhRFU_lUn4Nut5tY7TkBkjO6XiTgPOQNJwuBXh2W5L5At6F1RxNoPE8dwbVWfUVK-2MdtSNSW3YapHZjesmzRGYhpLPfkVrqo6zkswxoKaKBZXMhjmOXvslOE-vj-N004P1-VUhmPHfVgobQzrGOaujy5UH4mZ9-4E4ursnv46YZhoxd9J5ShXmPYWf7z-Ywr1uZ2z21kY3-38yDL5eydNqKa_rGR_KjTX2JA_0fmE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ایجنت‌ایرانی‌نزدیک‌به مدیریت تیم استقلال به فابیو آبرئو اعلام‌کرده درصورتیکه باشگاه چینی بیجینگ گوان به او پیشنهاد تمدید قرارداد داد این پیشنهاد رو رد کنه. مشاور نقل‌وانتقالاتی تاجرنیا به‌آبرئو اعلام کرده که هیچ مشکلی در ایران برای او رخ‌نخواهد داد…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/29794" target="_blank">📅 11:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4d0eG0FZwKft8zs9HQ48G8M-on59s90vmZtxYQmgg3lClLbvAzqXoCT5YQquXTpW7qUuL5T0RvZRRpY9zA8nW5VB9dnxWwl8Wzoe8ibnK7NIKmIM4AhEL4u8E0Rw-LqSc7XN6mgje5ApzXyjtPGUhvPt1JR77OA1JAa5gVcdI5M95Q3sIy6eH2rApn4gedAJI_sVQdhfaaLD7VMEgDSvjFapKVhN1K91D347FkGBBwqXex1dufokY6MPCKTwoRtM6SHigzNBi4wqrVIOolLorHZ3Ijz4l4nw0sRdzhrtLAa_LkSPUC6yrHpnGFKWw27htpNc72p5hMljAvgE-QMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29793" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29792">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29792" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29790">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvvcSgsOHNRumsNM0Coj3SOjBfj4MVUh2c6USWHX9PcyriFl6TcX6621M8E9O_KDDW1iBWQ-xViFIjca5E1clx8nSus6awswdg1Nef-i_QIoHT2eNcbx3_D7pwsEYfyHAfaGgeis0cDUcrfG-HukXwem3XiysvfCCRwFYUCchkXOHUEeKuqpuFiH0xfacbO6tGvmqYH_WDrPPM7iMjrwtsneA-Xjr7YKqpejmyHBbxx2ARgxNjW5rrioIbSAdwHKGl9UraaGY1ZAOE-fV9s9R_l5_SG-tc9p_vg4GwItKwacx45D5lgvAl2M64ThSqJ8fMgo7ncWKNo3yNoZqD0qNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29790" target="_blank">📅 10:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29789">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrmwT2QR-Z1ZyorB20q_dTxy45ARYt5zOXkeQGk2OxJsQmuOkWcEXxOAl4jlm4Vrw7WHsw8B-Z2h_TJAPghAKPVl36tYclv5St4wtxgx2kNughNhQlET9uzaAJJ5FiEUR6SuUUsAh0S22SxSXMlTs5LWR9ZyX2pE6tzmyQzxeXuQEJiBHjv11qIBuP2sCrGDK4GFEECRN0r6AYagqWTEa_ygO5eOB3kdDhp_WSjugSPvz0ozOeC7FkBdzCnlUS9Y1_jfkdG1C3TzipFwrMcMRNRYMqRK010zfE3d7BHNEQv0Iqa2xFE3vCS_fap4QxzdliAPjv9x3J4OMF9JPoqQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌کادرپزشکی‌تیم استقلال؛ مصدومیت یاسر آسانی جزئی بوده و او مشکلی‌برای همراهی‌آبی‌ها در بازی روز دوشنبه مقابل السد قطر نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29789" target="_blank">📅 10:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29788">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8D_bWlFZVEO6bdArZ0Y6HhEQmwr6Tfxaa3LJP_8O5fFDGuqVE9d0quUsNBQB16odUBGP0Prh5oUhtuM5AWjUdM830JM9dUWfw92axVHE2YPBmXucSW4SBNEdvUkabZzVlw-8cup5QHCU_WWWvlv2nzIlkRUy4ic20V0N4WTvX2OET2yWWdSy7p4vNIzQ7wjYwbGSv1wc5UqpcpTOGD1NYx1KkhP59ONQM3yfoWREShqI0n3PoeBXPEk4P_9g8HaJWgwaw6gMkhrNsJMXXAp3qatLE-cyHdMHxiTaR17Rzjz7wL6bTpSG2uXuipcfohrSa7PCtnzl01Vrht-Db9jOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودیگو گومز ستاره پرتغالی ولورهمپتون در کنار دوس‌دخترش؛ پارتنرش‌به‌حدی گومز رو دوست داره که تموم بازی‌ها برای حمایت از استادیوم میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/29788" target="_blank">📅 10:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29787">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=KmCZLPWqRSSVxMFiy_7-CdwL9AK7eAa9ZLkbY4Vofb6Ie7NJmuG4A4wYqHasDhwz-24Ya5ZJ42WmH2frSdAgEpnQMo_bTDoM7Pc0H2WYvE1IO5K8Nv7DEnzd8EKlvXXlGRiZYAiQbvNotduMmp5D3ujN6thcZzyr0kOvJKstRz57-6z0nRS-d4FBiW-YEusKVmUKH18Q555KJXFpGV78fzRxZtZnX13MyALHq6n3N_VNNJxNhqp8SzbOPfny37SUO1y1QJQzTOu1l2Gq4cClMlg2naTMaNT_eGf6O4Rzk62_K71vduEZ83JGRH0sUB7EenXcrvFOdpZV4hTP_NZY4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=KmCZLPWqRSSVxMFiy_7-CdwL9AK7eAa9ZLkbY4Vofb6Ie7NJmuG4A4wYqHasDhwz-24Ya5ZJ42WmH2frSdAgEpnQMo_bTDoM7Pc0H2WYvE1IO5K8Nv7DEnzd8EKlvXXlGRiZYAiQbvNotduMmp5D3ujN6thcZzyr0kOvJKstRz57-6z0nRS-d4FBiW-YEusKVmUKH18Q555KJXFpGV78fzRxZtZnX13MyALHq6n3N_VNNJxNhqp8SzbOPfny37SUO1y1QJQzTOu1l2Gq4cClMlg2naTMaNT_eGf6O4Rzk62_K71vduEZ83JGRH0sUB7EenXcrvFOdpZV4hTP_NZY4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/29787" target="_blank">📅 10:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29786">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5bokmgI__iqMBKYdBlm3y1AkqW4mxoIRZaSdfYkOLWTZ35E7u6m886Dt8acP2djH_vtx2ay0vHuifBWUvelYnDI4f7rBj1728POjHVwEgOAyG2B-efMHPVbRI0gBPNLRsiSxYIuzaqgn6vA_e1oybX-WzCs28FiPldplwnRv5zjefYqxzhSTApISkos5etk-_Ve4_aTPGytToS2byAV7495k0WAnK5LSBYCq5eOw9YxLMIxPCNhjD1-yH27duXZ0G0Ie7aMCgDTpHh71opFN4dF6tAIPhbjgzeFhrQE9KL8dj6IUT8X8WutnAUL1MQRIbC9Cx0yBCQOCKt_042HPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/persiana_Soccer/29786" target="_blank">📅 02:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29784">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm_kEH02Gt4y3jiLDZOrxmm5JgckPm1ICu6q6sgtJtjRFXPg3O1owInW5dC_d32_ib4BBDsH47iU90OdYwG_70IDo5FvsuHGr264KhnepkRDT6qw99o7nXKY93n2h5es9dhUyIEsIEhpF-YTYrxPxt5gf6arK61BfzN-HSvdeXrxjOWXi9NWMk6QnHMerESsN9gTovoOryl-Cdcq4ea6vY5WcZCN6koxxxN0eTQbCGLRdh35Td4hca58FGdI3lzFA2cRCC_19TLaICzr50s9ly6PdnXcNwkCGuoRazEhigyCbl_hTWnOwcJQQ7s5YFN-Ll2Kumb_xtNQxioCdBtosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/persiana_Soccer/29784" target="_blank">📅 01:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29783">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUUEhhtd9qIkFHMZwanUHr-b2yEJt5ZLu0807pp3gklzeB12yqDDbYf6VhhBeoS6b_JWl9yJJH0djEdpCHR4fKEke5O4CjranIS-_pVtgsxuJHpu5u_qEYnG4AQ6rHcw1y-V4uqIe_Yr2lcKOxK3oBaaouV_x3RduDqG2mDV2BKhWLRXBjPNAaOHyohnq49qhufEP3gFU7y7mfRwh2KscgrgETumPMZjtF1qRpvx9cCnSYCk4R6iW8BpN0rcJ0O2zfMgKE-VV3WIq06gE5a2eGdirvGOXp_-Clh-R8XvoLPNBAFg_zNamuyqSKKuC7ujDBj084B72rb2C_NCTZT84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/persiana_Soccer/29783" target="_blank">📅 01:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29782">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWyzWAngF4E3VRAPqk1PmkDL_7Zcs5ve8b48G7XgBejcL2UzTMqmH6SGEiWIZmemn2vU8NUPpCMGBKh8jEBshp-uqnTB3hJCZhCXvFfHMbO-kWrPqRwYMMGcM4SAqt9Rd8rhuxgh5ad8VfbMry1j2Pp7ffQCVIA9maXRmpeC4HIVXQvdC28eEdVzZHKd79p5KDKUNkseoxZDXXI6glWGuJ_ZIKcUs59zZGbTzgfohLuGPJ_59O4rPF9jgBGlY4-kfITWyEGiwahch1dKNj46RMGS3Ufv1CoL1yzac_gB_Ir2Qykv16HBxmMCjQU3tFK4Xr3Y5uFc4uCUXb9kJEz7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ تقابل‌لیورپولیها با شاگردان دی‌زربی در کارابائوکاپ و مصاف رئال مادرید با الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/29782" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29781">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLHv6kLmLR37JsT8heNy1FvQmfOFDlpqn2srkFXUMX7fCVB2M2d8CAGyBplgqTX7Kd0okyhPlVMRIz7KRptuhu7UBFwzbnVuHOt_KYv9HgNRf3lWjB-F_Fs7mp5mV08IKHW5fr-iF6G4kjlOPPiI4T4T56Qms7MmRwuYEnFjJbGHzz1vhJW7EyPHgBxWPQp1lkNkp8_MwEvZIo6PYY2cvW3gjY-KhPK00E5NdRLj_fKEI0V0s4i_P_Kx7AUwzLGkvaAkpa5Oe0gcnlWw7grvrQTytMYkfhhB0Ct0_E22sRpTb0lq6YKmC2WihzAgoeoOC6PcICc8eJ9G080JkmM7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرد شاهکار استقلال برابر قهرمان قطر تاصدرنشینی‌یاران دیبالا در سری‌آ ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/29781" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29779">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBCoAbTkafqbwY2pfPDtWhftair_jC3kxeVfUca0MOwARXepq3_L4Uv6ptFDbQAbbHZUq8_0k37anEXDFQafiyeGphk_39PRsUDIQoP72AFnrmsCVD-tAdwE4tkSSOfG6kKG7M-kKsd4Xgv8rT-Y9GBGvJ4HOOvpK02ChmrA5l3jnrMpu4dNk_1Do1RBQvvsyhaHPdhADzZLifnNLNXaSy6B40KUeHHshHy-_Hv5sye9Kvnwe8UJQ7HKQtT2FxWtNR41Px_N3dBZWN8-McXVaFeZIcmA-o0qz0jxlPByj4JI7c-AaABFHwgIPw1yid7btSaKAnt0GAyBSL3ZnR-jBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیربرنامه‌های علی قلی زاده که رفاقت نزدیکی که با محسن خلیلی داره با توجه به چراغ سبز علی قلی زاده به پیوستن به پرسپولیس قصد داره این بازیکن رو در نیم فصل به پرسپولیس بیاره و صحبت‌های اولیه شروع شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/persiana_Soccer/29779" target="_blank">📅 01:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29778">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl0JE32LuIySwxmrCeELUfup1yz_v_gj0eNPifACCHNqqDk0u2EAjmfOGPU4ItHv7FA8qjVEofoGsv0XJVfwA2pzh4kHyyB3jbH5xJIq1bZlZeKZbP_9nUxOdisUQ51UMfqt5QI6dk90oBOpb3J8p14LP1jRx4elcttiCgjMZhtSKZH2WdCft1aqsApCjmPgpiiGYrOdTn6ghHbBCKaqVZ4eiMN5yz3p_LGnfNY3_TQ3JO5NLwo7COLhy4hrg6K8-ExsXRik03aXJS8lb30uKAkmyLZzGhbX2N0p_AaP3RrgHYOpkrc_6EeENnuEK5E0fR__GkD8Onovby5XlFZLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/persiana_Soccer/29778" target="_blank">📅 01:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29777">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRDUnUT8t6pG0YZcjfHkg-jGXWNVwnH9_Wrx5vnJ03fsmtyifcaIxO25X5Qxrjq_XoT-feL7yym2t7M9AqF3mbsjjCTJUnRbLwKiaErs7r_DlMkJczT5flEFqj5hM4xJhvdv-tbWJvWVxIGqDBKTqn5mFSQS2Q6ak35NycMHmbTkwyrbfiKw000HNkNPm4NP9Zm2mWBCJWnKNcsAkn5lOU_xgqoQizXU5nR0_wo8mHbwBhrz2aRKo75-slsl9tN0_Td0xqJtmtqdFR_85msQxbA2sBZjybOKVHEV3Yj96vOdfmsS2pMmWqDetvfBsCh6l-JiFjePW9VSZ8uBIVfnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/persiana_Soccer/29777" target="_blank">📅 00:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29776">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFS8MBlZ7Bsdi15752VgYBZKBgk5L2krF-iHXEUhzxjcTnYj0Vq-O5WcNgIN7KC75viz4NYuY9sYlbitRIeQ2V_oWZ61QcZoZQwR2POHOZEw5wW6RcuTLj8TfgXvVYgEI9C0BAsmaZveh8VIwThScQ1CtAr29c2FSpEUh2E00CXjS6VxMHFGUs0jHfpt8uWCT5fr7m3Ts8t_KftR08WC4zQzmb33xW77Qi2qscIGySG6N298gKQeG3fR98ygvTE8wtvsoej3E63ZZytqOQouk_5j9sfzXQME6DIMmD5QZ5LjzI9zET5wB7-e5n7KvfZvqbOE66KXT_jagdFT9GVAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال‌ میخواد درروزهای آتی با پرداخت 800هزاردلار به‌فابیو کاریله پرونده او ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/persiana_Soccer/29776" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29775">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p52Hqdep3JRQZ97I36K2V5NNQUn22aR0dcXE_3cELsjaAHIfQ_UbkSPlFVIKy8Zq_XWf7rHeouTkDzZeQ6vDXj_NhtomCeHDnfZl5qSk5mnjfA6fzyBNN-0FZ6YdIk_SRIcyA5imcDqJDCr4FuNx7aJG0OTDbOUpd0sDvZNaZLZk4sP9pX1ibHHB2htwokH0sA-LrK5gSb7PV3RCmxe5yJPShYeB67KLZXitQHJpqKjs91qSmvWAFGJQQMXQbecKvXpDUPvsH2Xjw2VSpHvKx3t3TcWoWgJDKuvuN9sssyojRQ_L0hTGN3TKNwxTzvJ8mkxNos7P7pWfFJRDW9RhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم سری‌آ؛ آاس رم گاسپرینی با دو گل سه‌امتیازارزشمند رو از تورینوگرفت‌و با چهار پیروزی پیاپی درصدرجدول ایستاد. شاگردان سسک فابرگاس هم دو بر یک ازسد پارماگذشت و با10 امتیاز در رتبه دوم جدول رده بندی سری‌آ ایتالیا قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/29775" target="_blank">📅 00:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29774">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_-nQZpQry9a1wm2823HNj07_yJFv-n25e6MySxxAFeK1yzZoWoKhx5VxNMgeLL-mwRomeOyllSH4SWSWmfP2sXjAVrn-pzuc8Dl2hRMhunRheSz-RQCMyQhUVKykhJ7EsyCoEMJFxrjGFReUUUAOqmwjPaA3VVJgsVv9-2pnAJeI_6XgCw3EV8rvPPSPZOhFBqNhVZVe5GA-LyqyzDaBlj3E5rO-aJMG_aEPQyaexOpFokYXUD8lHqdejzCNiM1_lMjis1NXxjGx1v84-mC8jd5ZYxx9vuyLFXfG_YuUiaR8G9kLBOTgVapwsBapQitgN7I1yacrHHhLt9TBNyxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/29774" target="_blank">📅 00:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29773">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBzPoBd2i_wEOKFb2glJdBSZ-8tBBhJUenzQLY55sYCp0OYns4Cia8ZW3ymjevxSswexHTR8WqNrObJceEXM98rkZEprXUt7_DNd8Zh0slcoiY1AFTnP9QxoucVRUpagxpV9Z8ezDBtvqRvZiQYm8kCsiK-4ne1SxEZOi54k8CEirXqJBxDcyEGAOeyPnhSo1Fbxjt2XQr_qxd-Hm_k7MtZ84ZTAr8H1pBfL9cp8XKtb3eKCz15RzaoPyYPIQfNGb9E_fUwbeIvd85UKkUdqk-KrrLkjPpDRmvI0ik5_RJtkURBYItBHCPwghdyQpiRhpynZDjKiIjaRNZTozSZhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/29773" target="_blank">📅 23:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29772">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olqW3SEb5L70OFoSlZB2ddJ3-eaInCFOt9rjuqawpXcdzZeivY8bg7ciCJU0KEzeGgJcvmHYBl29R8uGzz_7K0SPqK_V4e5yuxYKPva41KEpHh_EGVR03HQttWPybfSDrgPYMCiB3_R_zeJYhO5YsBtr1ns1_2BP3lJRMk0913oWjvI5c5j-VDoppZd6_r2JFGaICq7iZnlrkXKeuCVGGZcJxBuMbrEfyifoyiMLX2XKnqTQyErHjZCLQ4h1RWQvTBJiXyoxAqoTpA0v7Nqdc3eWY51EiYqc8AW-ek13PZjODiyIemwZO1QgjKx_xuHoxgNvHnUWzkQfYDrwbKy3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/29772" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29771">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDR18qb6TkIoFyG-XHH1iA4B-vIzR7kuQC-jPS701VfUrew5serpfDLx89P0yR_LJE_TrH9qQ2WfRldofed8_7X7EQp0SOZmYqetRpjsvrTp4X2KcrLnZinhT2BPD38A83OQIi0b3xI0wqUwTMWLW5fKMchbJa8FBGnh4fRasm-jTIlC3Hkxhh0qIPTiMm_xrcxbOWpEe3sAKtLcIIOXo5fgE7A9Q26TUeXDKuMiZv0YjAQM-Z5YQpCsq9i-HdookyyDVvaZdNcyon1G5JjKug8X9I2oGTScXe0AjDASq3ucA0u6D-kpMVZOIvUbK_-_mlddsuDaLGxLD_AtMAfwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/29771" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29770">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=DkAz7Evt9_aZFAFrV7jYLaWFmdGb86DqqdOrwwjeiUfW6mThvb3PMqfifpM7lJYtbsL66KGpKS-taV8ekWGoIdCzszkFXr2ugigfJ40OXJf1OdtiyCLPYm2qg77SMWfMsMCFGS1KSvmYo9zAFf3rVWKW7NpFed5-79SdLlYEf-ISrJEVHcmNCP0vzLM0yRRQpy8MYpXmNVf03bJBzWLXDuAjY6W_pyeS36PWK99geQs-7jm5kW-GHZgNuTuQxk2mVIW6etha4A-7r2dBqZ8Fw8H09L4WGYworC42CNIVqblDFuzGpOSgLpsjdEnXB-3KnUG-Ot0YLbLiaPqOklzu4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=DkAz7Evt9_aZFAFrV7jYLaWFmdGb86DqqdOrwwjeiUfW6mThvb3PMqfifpM7lJYtbsL66KGpKS-taV8ekWGoIdCzszkFXr2ugigfJ40OXJf1OdtiyCLPYm2qg77SMWfMsMCFGS1KSvmYo9zAFf3rVWKW7NpFed5-79SdLlYEf-ISrJEVHcmNCP0vzLM0yRRQpy8MYpXmNVf03bJBzWLXDuAjY6W_pyeS36PWK99geQs-7jm5kW-GHZgNuTuQxk2mVIW6etha4A-7r2dBqZ8Fw8H09L4WGYworC42CNIVqblDFuzGpOSgLpsjdEnXB-3KnUG-Ot0YLbLiaPqOklzu4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/29770" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29769">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eng12uDeNrex7i5sL4ntjp99BpeVefFzz1XV0-4n-_Dbgy1ZU4U-uGJurixNMNwFDfVL7o8515g5-E7IBqzlE0iLyrfLaodq4eXGOOZ_brMzN8VsSZa3zuwZOqaQIvzzREX0lEAiZ1_k9qHQt5claT-pvQynkV19-EJOgb-FVK_7ge31_gr0fPe61kL42m4qmCBtsHDPYJluXmX8aQGyu6tKLLY_w-_3Orjjt2zF3jiaqyL8jptKIFTz9yfFz3SUWY0hk3s1uXGOUEfe-uTisrXc39kX4Z9lIzNEiA47WeOXf5MiohE1pLM2GF4ifWVcnFSQitfX42W_sWz38pyWdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
اظهارات‌ جالب لامین یامال ستاره بارسلونا درباره توپ طلا: "فکر می‌کنم امسال من لیاقتش رو داشته باشم، بخاطر چیزهایی که بردم. چون از نظر من، من و امباپه دو تا از بهترین‌های دنیا هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/29769" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29768">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=XSUl0ys5EwmAWp2eDcdbBidVgieRxyrDDH5DRowA5ag9LpeXImMEjA4ueC9d_ABrIcpZp5wqgJLQx3fedsHaXoY-37SLNukmPzdMYJIUZXEAI2X0y8GgqZsvRhOEL6DJlPCz3Ei261jtTcUPX1pcYHJNl3mZJWCgGtPAhuXB4tLQRGYMgOU55uc_yGxiIKOxzeUVNEsjU0qYvSKHrb6foAX4Df7RNUaXzI8I_T2OOAkbWXAtAfxyybSHh-ECiqtO2rUelVpx4mg7l9fkj392m9g1AOWusWKfkYRaJ_TWkBrVmrawQG1A3J3i6A7uozt_SeHs8wByiCuLC76dXgpMhoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=XSUl0ys5EwmAWp2eDcdbBidVgieRxyrDDH5DRowA5ag9LpeXImMEjA4ueC9d_ABrIcpZp5wqgJLQx3fedsHaXoY-37SLNukmPzdMYJIUZXEAI2X0y8GgqZsvRhOEL6DJlPCz3Ei261jtTcUPX1pcYHJNl3mZJWCgGtPAhuXB4tLQRGYMgOU55uc_yGxiIKOxzeUVNEsjU0qYvSKHrb6foAX4Df7RNUaXzI8I_T2OOAkbWXAtAfxyybSHh-ECiqtO2rUelVpx4mg7l9fkj392m9g1AOWusWKfkYRaJ_TWkBrVmrawQG1A3J3i6A7uozt_SeHs8wByiCuLC76dXgpMhoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
روی‌سماجت‌کاپیتان‌‌آبی‌ها؛گل‌دوم استقلال به السد توسط سحر خیزان روی پاس آسانی دقیقه 47
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/29768" target="_blank">📅 23:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=ptvXNjhN6rt4ZhvUDlqAG3hA82bAyypsTy9Dmh60_N3EmFAqGOGuK50TGOerUaZ0uxbO7nQ7dwPw8pJprQRwDMJ2tRXgPVEnw645RgJWM_UmD96NJq0c0SKDHViKtYsEHd8sfa4Jo-ufXPW6iuOAAGYf0t35MHmFAC35__WOYMij2GT5gcgnhFHTWOTgkrH7JbS1t1YTt-sCA7CWLxWyhvQyZnoBAXWgXUqDQHToERC7lYmti4wL4T5oeJx_lxz5QUklwn8LL3X2o8weIMnxWA14fDEEdLh4kf7S40OTDDUGwBxmogzKQKP73p6my8kIjWM3FrKvWx1062xv7iSUPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=ptvXNjhN6rt4ZhvUDlqAG3hA82bAyypsTy9Dmh60_N3EmFAqGOGuK50TGOerUaZ0uxbO7nQ7dwPw8pJprQRwDMJ2tRXgPVEnw645RgJWM_UmD96NJq0c0SKDHViKtYsEHd8sfa4Jo-ufXPW6iuOAAGYf0t35MHmFAC35__WOYMij2GT5gcgnhFHTWOTgkrH7JbS1t1YTt-sCA7CWLxWyhvQyZnoBAXWgXUqDQHToERC7lYmti4wL4T5oeJx_lxz5QUklwn8LL3X2o8weIMnxWA14fDEEdLh4kf7S40OTDDUGwBxmogzKQKP73p6my8kIjWM3FrKvWx1062xv7iSUPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/29767" target="_blank">📅 22:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29766">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzeE6ds9p4BEzRwZ3ENW304Hl0KPcyqbN6rOXABiUyi-vm0pfsqzxO7LmzzIYnV8bNP0XkK5_twRyIz8-Y2VNdGnXWUGNpmdworeNJa1XW9eHAMmmNVytGR7SHObI5o58j218nwOtK3AJmtY5NqoWEq0D2-OQTQsLDyox2b2cUYN8LUUhouhddAsnfT0GTo2tkaL7ezFo8zlfZUVQJ0PxS6BnaXjvYtTJvPaahXFmuyTNQJN_-ssA3umVmiIy7nGwjcIqbxC32pASztK1g5gVthziF08jph1Uwnhx5gDy2r-yPYx2JSjc9JTFJVxNnxVgCHxFNKBNtHY9RMeRdfAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/29766" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29765">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InDBoLPm2WI9VX4cKIF6ixk2HLGtdLH2PpN5B8SeXa6y0O-F3eEIIElqGNm03A2wJRuCUtD7szFsasOMotmLUzhZqEqDweiA8iHTRG9RMGnoePKyreY9pP1gcTsq9IZqRPw3r_JtmSnPIMG6-dp9s1maZ0CJOeA4iljZ4OD7a_Nt1VCNdD3dczrVNeU3w4ONZTQ0NhwQGCCB7NQdcyHKGCUfj0Of9vHStiXIGkVbI9IXgU-JdOUg3Io5zAol1dV6TZqDmei8ZXp5qe2XFVsbdxs-98hxWMC7Y0Sc_uWNVj7UQt7LV0bsS3-NcyTwWzhpOss7K9yqfCCKRjhI2F9GsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/29765" target="_blank">📅 22:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29764">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=i4WlVbLNf8SJoBp8Wjvlk9EVpP8q8aFG0QI9eWf3z4b-v4V2Ckgzdb_5GvZCulDLIWEY8pi2S-n4IIUryNpYdsLQqn63VJIlnPNsQRZb-KUfcuLyhA42IfVjNV8XRWdrUbYELpCDt5mvpfY2ddz6FqH6IEgXBEblQatGcDI4KRTEnq9y6Ztg4_y6aoU9NcVCeQK6Euhn3ldq6-OPAsjWhwP27SdAgyVR1V8wGWKNf3VuLFlkjdGdLLbKjf91QhTV-4x5uIo9Rnw83cCmKxYv-uOF9Nyp83ohJgdCU0eOnBufWbMJ6rAReNQXvHUWRxMS_XpbWmlOUrpP2y98RtvRPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=i4WlVbLNf8SJoBp8Wjvlk9EVpP8q8aFG0QI9eWf3z4b-v4V2Ckgzdb_5GvZCulDLIWEY8pi2S-n4IIUryNpYdsLQqn63VJIlnPNsQRZb-KUfcuLyhA42IfVjNV8XRWdrUbYELpCDt5mvpfY2ddz6FqH6IEgXBEblQatGcDI4KRTEnq9y6Ztg4_y6aoU9NcVCeQK6Euhn3ldq6-OPAsjWhwP27SdAgyVR1V8wGWKNf3VuLFlkjdGdLLbKjf91QhTV-4x5uIo9Rnw83cCmKxYv-uOF9Nyp83ohJgdCU0eOnBufWbMJ6rAReNQXvHUWRxMS_XpbWmlOUrpP2y98RtvRPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امشب مقابل تیم السد قطر در هفته اول لیگ نخبگان اسیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29764" target="_blank">📅 21:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29763">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga5tcPsELw5IuNL_HgKOzJuLObXhLfyQXJd6KNWsOWBg18glPJCxFFwHH_Wc7_6Ayh2SCRdXhPWZ0-LJkj3WNJSV8rXIKV5MHrZfIGsVF1hTVMDxa-xotL4p5JSDv6k43wX7cC1EUQWSoDLBuBKwv235rEJABxnwWPBvy8E9efxKKiwhjEhW8WA3okFRc9Z2h4eZlw7T1QglJJFFRSiBgVvwRVw9AQ-tEmduosE2yuK8e9B1ENpc8EZ9N-PSrmAkGozMOMRxHL2PjLhPqJZV7V79s26109-40Aa0aLKhds85vJKXIcNfvI2_Lm893CI00CAcSvls4jsXhpDUikofcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل اول شباب الاهلی به تراکتور توسط یوری سزار در دقیقه 22 روی پاس زیرکانه سردار آزمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29763" target="_blank">📅 21:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29762">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=Gj3Xk0So4Ka-pnoxP0HplR0a265GUAafkNgD7Io6vDriXfSzx0o6DWViPPsTvYXDvZSk1UE5jAtVeebiN4TlHdAVb1BnDixkIYPilNhuwa-J-proYRY6zvJ29hrhXppMK9wfbGfrA9uVg85INbNvk1lhC7aGEtzANNqWvA2hYiKWLZPpfVpaQl5AvmHYWXnEWrjY7ZgYkgY0W4fzD1vmQiT0aBXfdI4e4b1FEOuUp6EnCDC1TTp1TmyWIoLw6aTd0E6OF2pCl6ZoBRjSP4H84jFei2OiVue390f9GXnW8Um4ZBMqBG0ihg7ULCRgFnRAdKq872HQyF9pXb6E7RW4j7buWa_qXRxN4h3vSNkS8ydUZ5-56jFQRJkAtVm1fi7htIvA2os8Zi7NWhKGJCCEFEXwvKJTDkh8W5xFtDk7AUNd_SnR1Pev2vGRDDBWLtnrkNZqe_ha2Iz4DVgecXALpI-S4jwAHadBNYHvQCu_fZVNx6dvaTiIieMsPKMbh8zY8GVVA5eCzJYiSFS6o4Vrz0bjxI_6sBUy6U9xl_FqqeaXsZHDsEX5rjAatzPeNNXOuSoFGyvygZvWZhm2jdDNKA-Z-U4HXUV_mo80oeHqgSqMoTg1ZMoE3lmQl4OUY7KdCXZjr_690thZi3VAkAY5ZPVrvT65O4CGb-ltuq1CQUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=Gj3Xk0So4Ka-pnoxP0HplR0a265GUAafkNgD7Io6vDriXfSzx0o6DWViPPsTvYXDvZSk1UE5jAtVeebiN4TlHdAVb1BnDixkIYPilNhuwa-J-proYRY6zvJ29hrhXppMK9wfbGfrA9uVg85INbNvk1lhC7aGEtzANNqWvA2hYiKWLZPpfVpaQl5AvmHYWXnEWrjY7ZgYkgY0W4fzD1vmQiT0aBXfdI4e4b1FEOuUp6EnCDC1TTp1TmyWIoLw6aTd0E6OF2pCl6ZoBRjSP4H84jFei2OiVue390f9GXnW8Um4ZBMqBG0ihg7ULCRgFnRAdKq872HQyF9pXb6E7RW4j7buWa_qXRxN4h3vSNkS8ydUZ5-56jFQRJkAtVm1fi7htIvA2os8Zi7NWhKGJCCEFEXwvKJTDkh8W5xFtDk7AUNd_SnR1Pev2vGRDDBWLtnrkNZqe_ha2Iz4DVgecXALpI-S4jwAHadBNYHvQCu_fZVNx6dvaTiIieMsPKMbh8zY8GVVA5eCzJYiSFS6o4Vrz0bjxI_6sBUy6U9xl_FqqeaXsZHDsEX5rjAatzPeNNXOuSoFGyvygZvWZhm2jdDNKA-Z-U4HXUV_mo80oeHqgSqMoTg1ZMoE3lmQl4OUY7KdCXZjr_690thZi3VAkAY5ZPVrvT65O4CGb-ltuq1CQUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه دورتموند با انتشار سوپرگل دیدنی و فوق العاده فیلکس کلو اِنمکا در بازی این هفته با پادربورن مدعی شده باید جایزه پوشکاش 2026 به او برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29762" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29761">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCwp-FSdOkEgYNA13iJzm7574D1xOvY0DLdmI8vn1r_NN3eAb2ElCTmG8dn_dID5Sypd-Lk0g30ZAC897fyxkKaCSGXBdpX7ZZ-jEIdnOJaBwbtxwj7pEE7GKtMWH7ji-FcZV-BQzhB0zkZlOfugineBTBq_Mv1Rr86wRrwzs4KdnyKBh7dprbw_DcYnXTbrc8qR-ZtlHsAaqdIBOLQWZZw4t-f7cDjL1jYMhdT-1NM8XxidI-ZFNZ4VhFGuJwS78e2I0vNHiSnTcvVVEZ5NCGFDJEkzfjZqL5rzI1XZzxKCOXB9NHQZyNM-GnOXI6RRv8a3yh7izQgvdTgc362OMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29761" target="_blank">📅 20:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29760">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL56y3ORHxWvQhGHb-bBpWS-TVsPM6c0nJHv-u0A9OOP7va8lFRnM_ImRedaBLlvMfVCcf2ffclld4M03HPeI_uqBnxKL-R-QrKSPx8TdWSOfNyEqrL5rQnAMnmBZYIu90_-bR85izJRiIwFKc0JdyqzBpXtWDJqaWJnaABlSxgE9e4Sxa7HXz3tT9l4rPvWjZ2plQ1Oorf6Ji3dtWN1t1bAYCJCrRftSA358sRllr5KSZV_j7AJsSHdawbvIkwdr4eCC8GTnFNGwxSMvV8YZp7c9DRa7a96TkSVhkJMImkpHmYUvRsT5AH8bcbdvATPZv36ygyFCRTKWUF6maTiSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29760" target="_blank">📅 20:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29759">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V88xiWTsA-nRLzXLEWUyRM5kCkPYQ0wJfkA2XD8oJwzKOEOtB9BS4o1K3nW4ZZDDcHR5U8v2c3G-AEQL5CyantAuzh6PjX7CtOdjHSQMua3b1uCJ3m0ihZZJD3EvBTeI3pqShRNUELCKhUq2QwgMPCqeCs9XtbKtPassRLptbG5z7lLmfAmkJSUpSTHeHeTmz1m8S8-eTwG5JbQImlOsCt9GVF3QAD03aKmUMN7wETO3y7MC923B9oUY7-YDSDmZxA7ixEIFfs7DzdAUPnxkg82WITld5JsTnxHln3f-mKjMKHOtwsZUQPS8keXWAP8HSTX24nD-9QXU0hOsa0EYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل السد قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29759" target="_blank">📅 20:32 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

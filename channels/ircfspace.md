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
<img src="https://cdn1.telesco.pe/file/v-rhdA6Js8BqZVitaAWjg5JFUrdhr7tQD64i4vL_fQybz5VWAJwfnYVGyS-rRetwZhfRwE1lexNtc6pOREfKrL0pNBTgYbUNaT-aVrXekJiBsY5_Kb_vTJrNnVax4mK1Gs2l2iK5RIkUbFrTTBhRpdbu0HRPmuhkszMtwtmrUCZk-C4Cl_Uv1uH6YVJ6JmK65i5ZpMo47oDgg4Vv5LJAYoyOu3Ijm67D-s_FyZST0L8thLsu0VX5Sx5MmPiVce-BYkQu-AoM1ZVll-HXceeVqhx3U39Q0wrbwIXiy34bp9hciW16V_ZRISyK6LE0vBQodL8Xm7lCsIzQY6FUMK4pzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 21:15:36</div>
<hr>

<div class="tg-post" id="msg-2372">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جمعی از سازمان‌های مردم‌نهاد و فعالان حوزه حقوق کودک، با انتشار بیانیه‌ای نسبت به تداوم محدودسازی و طبقاتی‌سازی اینترنت در ایران هشدار دادند و آن را عاملی در تشدید نابرابری آموزشی و اجتماعی، به‌ویژه برای کودکان و نوجوانان دانستند.
در این بیانیه که به امضای ۱۹ نهاد رسیده، تاکید شده دسترسی آزاد و برابر به اینترنت، بخشی از حقوق بنیادین شهروندان، به‌ویژه در حوزه آموزش، دسترسی به اطلاعات و رشد فردی است. این بیانیه، با اشاره به تعهدات بین‌المللی ایران از جمله پیمان‌نامه حقوق کودک، محدودسازی اینترنت را در تضاد با این تعهدات دانسته و همچنین با اشاره به نقش اینترنت در آموزش و معیشت خانوارها، تاکید می‌کند که اختلال در دسترسی بر شرایط اقتصادی و امنیت روانی خانواده‌ها نیز اثرگذار است.
©
hra_news
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/ircfspace/2372" target="_blank">📅 19:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2371">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ttGbZy5iNGyvjkARuwnfDn5QG5I9XsR4NZMwFkDHLxD0hCqwgHxSCij1pN6WAg_7SrcoPZHAoqkpywkylE7VFfOaXDy4JS6uZn4HFI19_2gXt3wH9cvmI0-O1U7BfB3TV4VAM1U8ED8lVzn8Y_wCCO1h7tjroLVTQbP96L1QFthQ5xuxDL9yFK25QXWnRqUwkyrOT6CXpWHpeC1Sqn28DFa9r0xHb9-Nxag2Z_k0SLlyuigrVDnBQMrzltdazmApoXOhMotX0hlwVB42Jp04Jefb9XprK0aiz29LA1vCQQPTze7zYbg_wRLorlpxBfGYKwNiOlNQKCAuIrjGUyobcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران با ورود به روز هشتاد و چهارم، از ۲ هزار ساعت عبور کرد. هر ساعتی که می‌گذرد، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شوند؛ به‌طوری‌که هرگونه ارتباط با دنیای خارج به جایگاه، تبعیت و امتیاز وابسته شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/ircfspace/2371" target="_blank">📅 19:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2370">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خیلی راحت آمارسازی میکنن و میگن ۹۰ درصد مردم با قطع اینترنت مشکلی ندارن؛ به همون راحتی که احتمالا قراره تعداد ثبت‌نامی‌های سامانه
#جانفدا
از کل جمعیت ایران بیشتر بشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2370" target="_blank">📅 20:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2369">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کسانی که قبلاً کانفیگ می‌خریدن، الان ترجیح میدن دیگه نخرن، دلیلش هم تکراری شدن خبرهاست. دنبال کردن مجازی دیگه اون‌قدر براشون ارزش نداره که بخوان بابت هر گیگش خدا تومن پول بدن.
از اون طرف، کسایی هم که سیم‌کارت پرو گرفتن، خیلی‌هاشون توی کسب‌وکار خودشون موندن. چون درسته اونها اینترنت دارن، ولی دیگه کسی نیست که بخواد تبلیغشون رو بخونه. تقریبا اون چرخه‌ای که باید بین محتوا، دیده شدن و فروش می‌چرخید، به بن بست خورده و کل سیستم رو از کار انداخته.
©
NR2OH
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2369" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2368">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rpu2Gj1p8sXDAZBM6xvFIq88JwFU5SHSxy0PaYIAN7TIApxRtNsgWkmpDcZhYPt7C_6iN1WZJbzRPsfL5wNs6y7MK-xemm_J63cq8gCRb08vx-u67qQIrYnhFQrBY0Efie_BATPDH_vLQPZOPEfumxXwToVZIIbTFKMBYqA8Yu7LJg5MAwCcg4vFalv5RVpfvV_mtR6TIlXolWj3J3s4pqchz0NK3VoH2o7e34oYFQKHPMFIZRBqB5kC1bZENTjT1dar-ZIwtn0XWJuXV6p7981gyTTth0IvEZY6TLHw8MHJ4XO37k0-3ux3DBuWh0vmUzGxc9r3ZhBjK0R-XDeJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا فرزانگان، اقتصاددان حوزه خاورمیانه در دانشگاه فیلیپس ماربورگ آلمان، گفته است حدود ۱۰ میلیون شغل در ایران به‌طور مستقیم یا غیرمستقیم به اقتصاد دیجیتال وابسته هستند.
او به وال‌استریت ژورنال گفته محدودیت گسترده اینترنت باعث کاهش بهره‌وری، تضعیف اعتماد کسب‌وکارها و افزایش نابرابری می‌شود؛ زیرا در چنین شرایطی تنها کاربران ثروتمندتر یا افرادی که به ارتباطات بهتر دسترسی دارند، می‌توانند اتصال پایدار و قابل اتکا داشته باشند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2368" target="_blank">📅 20:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2367">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvTyGpqeUAt4cXu2be-UQ-j3HEtibxXiEAjzJ3_HtlqR8DtQl2GriCveVMS7ewT7UqCTVB5WcRqN9Nv8ooyDhCE5vtm9CWLmZzDDKoF2gUrIXUelgLopppldMz4mJwSROSiqmPa-TcHEWJTWpmB1TxfNnxVonvP7uBy4fzDzDSUW4N6gZ3jIbLOHN-YiRiVsBDC1JF9vavkcDpl6j7sdVJEvoT7ihM8i9Dzu8_SiUWrQ9VWE6NBcd1Rqgj7IadDOzDgTNcsY6pYHk7RH5jq1tXAJvKzmxWZy7h-4_0hIBZhs1J-nCyu3cS-D9-RfrELJAiIkn3pKYYLKSM3Lj4Zcuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارع‌پور، وزیر قطع‌ارتباطات دولت قبل گفته "جمع‌بندی رئیسی این بود که اینترنت به خاطر هیچ‌چیز نباید قطع بشه"، ولی یادش رفته که رئیسی با ۶ کلاس سواد حتی جمع و تفریقشم افتضاح بود.
جهت یادآوری واسه
#قوه_عاقله
، اینستاگرام و واتس‌اپ توی دولت سیزدهم فیلتر شدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/ircfspace/2367" target="_blank">📅 20:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2366">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یزدی‌خواه، نماینده طویله مجلس گفته "در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد" و "با قطع اینترنت، کسب‌وکارهای مردم از جهت ارتباطات بانکی، خرید و فروش و بسیاری از سایت‌ها همچنان در حال خدمت‌رسانی هستند و مردم مشکل عمده‌ای ندارند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2366" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2365">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VdY0FziH-2gQXM7ks5GVTjudm8hq-Ah4wYooXGVHZa6BaqpRPRCfgZceedl8iF7Mg1Rte_Xnz-Cxk9R2jaXpbt-M7DUvMsPnqk4JfM6WtmAY87hg1u-hF8ZfVhEFcyCmuZ7pl5EHbpKr_xRRfYliKu0TjpU47zOb9L8aAyqT9rO1w2nJ2VoMOepyRhMVCRr4eEoEQWRozQEioym6OIkulBiJldp4ZUo-bn6ErJuIaGo4Jv-_XTAFDnsjKRdiP4r3qUBy00qmDLX0LK5iawlZssz-pbUfcifzoFk5wFlBjo34pQ5ztrokY24vXIVaC6agWTTdcblXu4z7quw-d6RagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه عاقله در همراهی با سایر قوا، قطع سراسری اینترنت در ایران رو به روز هشتاد و سوم کشوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2365" target="_blank">📅 08:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2364">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گیت‌هاب گفته دستگاه یکی از کارمنداش از طریق یک افزونه آلوده VS Code هک شده و مهاجم تونسته به تعدادی از ریپازیتوری‌های داخلی خود GitHub دسترسی پیدا کنه و اطلاعاتشون رو خارج کنه.
فعلاً میگن شواهدی از دسترسی به ریپوهای کاربران یا داده‌های مشتری‌ها پیدا نکردن و موضوع فقط مربوط به ریپوهای داخلی خود گیت‌هابه. البته دارن لاگ‌ها و میزان دسترسی مهاجم رو بررسی می‌کنن و گفتن بعد از کامل شدن تحقیقات، گزارش کامل منتشر میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2364" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2363">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عضو هیأت رئیسه مجلس: تصمیمات مربوط به اتصال اینترنت فقط با امضای رئیس‌جمهور انجام می‌شود؛ تشکیل ستادها نمایشی است.
این هم خبری دیگر درباره اینکه مسعود پزشکیان نه‌تنها مخالف قطع اینترنت نیست، بلکه در ساختار سرکوب و محدودسازی اینترنت کاملاً همراه و همسو با حاکمیت عمل می‌کند؛ تمام نمایش‌های رسانه‌ای درباره «بی‌اختیاری دولت» فقط برای فریب افکار عمومی بود.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2363" target="_blank">📅 08:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2362">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t9auH9gJghiJZ7FBjMm3o6IsKYk13M2NwDnuKolYvkzEqv8w9uz6hM3U82ico5uenAdZm6yWCEJgbTWGypPZ2bv6pO8I9K7erwWykOqKya9oCRUJ3KPkmzt1ynxrUzTFGipoNDHQjrs2vnk0Q9UGdlemaqFSWWFAe2eL7LR_k04yv7Ww0Nhnx677ipOjpMcDYcElheu0NNdjVAPWDXU7sYhJksibHCG17rH_yW5_cjzldW0HkqhjHLVo4WM_9_tZRPD04M_9X8AJ9sU2xIutXPKX5aHDSYat77oLxahneUv_4lhhkvu4x5lFMzVH2BHEObBoaa37r5NnfD_QVMA9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نشون میده در ۳ ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره (احتمالا) از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2362" target="_blank">📅 08:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2361">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nvKlmp4X6ROzP1DuIKpHI-ePVrwZnOEaQbqIYgQ9qCI2rf9WOUPh_nSFvccwvuDRb5P_STTNWWjn3jY3VB3kkHWKD5ffKxmegYuZ0swLFbLH4h55T5MnjzihE17gWJ21Pdf4tzZJnimz1pr0x7e0uTExKE4vTzTjOpKcVQBvYQFqP_rLzNfpTkPXVAtZmU1F9a07Cn87gP1YIPomNBV421w9jiLbZ_py8nM-1ir1oO_SjaN6U3VGJ8pOlfcT21LwE1CTXK8L0f_yQhrOCO9wKnJWGarRxSeF-4344DzFofdRBT4wPKmJEoH18TDmE0Ht-cgCfSWkdwvyN0F5pXXgXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتاد و دومین روز از قطع سراسری اینترنت!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2361" target="_blank">📅 09:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2360">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قطع اینترنت به خاطر تأمین امنیت، یک دروغ بزرگ است
گفته شده قطع اینترنت به خاطر تأمین امنیت زیرساختی، نرم‌افزاری و سخت‌افزاری است تا کمتر مورد حمله‌های سایبری قرار بگیریم، در حالی که این یک دروغ بزرگ است. حمله‌های سایبری و ناامنی زیرساخت هیچ ارتباطی به قطع اینترنت ندارد. متخصصان به این‌گونه دلیل‌تراشی‌ها پوزخند می‌زنند. البته نه به این معنا که زیرساخت مخابراتی ما یا زیرساخت شبکه ملی اطلاعات ما در حال حاضر امن است؛ نه، ناامنی وجود دارد، اما قطع اینترنت کمکی به تأمین امنیت زیرساخت نمی‌کند، بلکه لطمه بسیار جدی‌تری هم به امنیت زیرساخت می‌زند.
در همین مدت دو ماه و نیم گذشته ده‌ها آپدیت امنیتی برای باگ‌های «زیرو دی» یا اصطلاحاً باگ‌های روز صفر داده شده است. این‌ها باگ‌هایی هستند که می‌توانند دسترسی بسیار بالایی برای هکرها ایجاد کنند؛ روی گوشی‌های مردم، روی مودم‌ها، روی شبکه‌های صنعتی داخلی. این‌ها هیچ‌کدام آپدیت‌ها را نگرفته‌اند. آپدیت‌های ضروری‌ای که حتی یک روز به تعویق انداختنشان گاهی باعث ایجاد ناامنی می‌شود، الان بیشتر از دو ماه و نیم است که دریافت نشده‌اند و ما با یک بمب ساعتی در ناامنی زیرساخت شبکه کشور مواجهیم.
من فکر می‌کنم وقتی بحث امنیت مطرح می‌شود، بیشتر از اینکه منظور امنیت شبکه و زیرساخت باشد، منظورشان کنترل افکار عمومی و جریان آزاد اطلاعات است. اگر با این چارچوب امنیت را فهم کنیم، بنظر می‌رسد حق با این آقایان است؛ قطع اینترنت قطعاً باعث جلوگیری از جریان آزاد اطلاعات می‌شود. دلیل اینترنت پرو هم اتفاقاً همین است. اینترنت پرو نهایتاً شاید به یک یا دو میلیون نفر ارائه شود. یک یا دو میلیون نفر با ۵۰ یا ۶۰ میلیون کاربر فعال ایرانی خیلی متفاوت است و باعث می‌شود جلوی جریان آزاد اطلاعات گرفته شود و در واقع کنترل افکار عمومی و کنترل جامعه راحت‌تر شود.
چطور اینستاگرام یک پلتفرم آمریکایی است و ممکن است لوکیشن و اطلاعات مردم را در اختیار مثلاً نهادهای امنیتی آمریکا بگذارد، اما سیستم‌عامل اندروید که متعلق به گوگل است، نمی‌تواند چنین کاری کند؟ اساساً منطقی که مطرح شده، پر از اشکال است. وقتی شما اینترنت را قطع می‌کنید، عملاً یعنی تمام زیرساخت‌های رشد و توسعه یک جامعه را متوقف می‌کنید. به یک معنا، ما با این مسیر داریم گام‌به‌گام به عصر حجری نزدیک می‌شویم که در آن از فناوری اثری نبوده.
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2360" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2359">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امروز هشتاد و یکمین روزیه که اینترنت ایران بصورت سراسری قطع شده، ولی پروپاگاندای حکومت بدون لگ داره کار می‌کنه.
امروز هشتاد و یکمین روزیه که جمهوری اسلامی داره
#روز_ارتباطات
رو با قطع اینترنت جشن می‌گیره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2359" target="_blank">📅 08:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2358">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N53GGO9taiNTWQ_8QCsGJ9lQG2NIrX6Hd6ZAucI2zgvvco1q5PTLRaJSggqu8I6GkUpaIixSpQQ4b3i27_mGT2kLyqTT3p-tyPhcGuC-yemb8pvIMTU-hH-FzhK4hqZjm3caitRILUma4utx_RJkmAgmlW53xNKAEKC7C_V4TtDtK-1sXcNpDPsP-nPlMjQIRLqM6Knu92irkA-RYOWlloLwyadwXifuhqb2DOJRBbxc5iYgp1-mfAyLs2BXLAzdY9psOLyGzumsb3pqywQ8jH6GmknZgbjfnH3O10Fp6W9w-uLNtTKCW3aZ0DbjgjBolJ9EILOVemYvKttAu5B-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از اپ Network Checker برای اندروید، ویندوز و لینوکس، قابلیت اسکنر آیپی Akamai (جهت استفاده در اپ
#شیروخورشید
) اضافه شده.
👉
github.com/mirarr-app/network-checker/releases/latest
💡
t.me/PersianGithubMirror/5227
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2358" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2357">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B8NJqIChWwvMT7Qd76_37z6iN_zMgK5dkF_ySZA29MwK6fsz_I3Uwj10XYHV_JmUa9i2xVff6GraCWDI25uYICKMhNDccNhbKqUk5fO9yYI5xcbQqnsrGKV-n0HwYtvUIVWrjwRgS0A1fAbkYg9EE3bEzLLwz0JCxlafpaTl2Ki5fwJn0wgXlgl-MpQRK3TIL_rfe6MbSoP9GMDE_6N-MRumMocG2J7RfMJlwugGmU9cCnW8yRWy60OToIHw-B_MFXm8KS-aFTVRWC7VraLEUY58A05OWvaqM2G9D7uqMf-u9bpBPrNlZ8n3JC6PeomwkbmKv89VEiBZwgXJWXg3Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ NexaTunnel یک کلاینت رایگان برای مدیریت تانل‌های StormDNS در iOS هست، که به شما اجازه میده کانفیگ‌های مختلف رو وارد و مدیریت کنین، وضعیت اتصال و ترافیک رو بصورت زنده ببینین، DNS Resolverها رو تست کنین و خیلی راحت بین پروفایل‌های مختلف سوییچ کنین.
این برنامه با رابط کاربری ساده طراحی شده تا بتونین وضعیت تانل، سرعت دانلود و آپلود، پینگ، IP عمومی و سلامت اتصال رو بطور لحظه‌ای بررسی کنین و مدیریت بهتری روی اتصال‌هاتون داشته باشین.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2357" target="_blank">📅 08:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2355">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">توصیه اکید من اینه که برای وصل شدن به اینترنت سعی نکنید از سرویسهای ایرانی (خصوصا سرویسهای متصل به نهادهای امنیتی) که شمارو قبلا احراز هویت هم کردن، سو استفاده کنید.
به هیچ وجه حتی برای امتحان کردن هم ارزش ریسک کردن نداره. و به هیچ وجه هم روشهای مربوطه رو معرفی یا پروموت نکنید! اگر کردید بهتره همین الان پاکش کنید. از سر دلسوزی میگم، بچه‌هایی که از چندسال پیش در ایکس فعال بودن میدونن دارم در مورد چی حرف میزنم.
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2355" target="_blank">📅 20:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2354">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uTJFGtP7o7hgDLWcBtURcCAnq1TNIOVH6-yu-5fQMpvQ_MpGIjXuub9xb_OTXiT1l-h9lz7R1rDZwstgO4VwdJqPZRaSkdCPqP1zrMfIwDrHSMfOUMXbY_Es-MXQ9R_eYh8QCK0xHU6bsOSoLHy-nlOPV7A3OgMeSqZLVowURQDYXFnfXeOGBwjuOCs7S_Qeu1tqEv2jzxrG6eRSe46ENxjSV1titEV8Uh4iCOxmUx_pQu7N16Am4S2D3ejzERmlN5dYVy-FuXeAPPCFtp-V9Z3Lz1y7TbHFeJjJ3zOEOxYWVCWVZVfGEaUJabL8Ab-0OLmGF8T5fF1JRsyEk5CoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما در انجمن تجارت الکترونیک تهران تجربه واقعی کسب‌وکارها در زمان اختلالات ارتباطی را مستند کردیم. از میان ۹۴۴ کسب‌وکاری که به نظرسنجی پاسخ دادند، بیش از ۸۰٪ اعلام کردند در زمان قطعی اینترنت، فروششان بیش از ۵۰٪ افت کرده است.
اما یک نکته مهم‌تر در داده‌ها وجود دارد: حدود ۳۳٪ کسب‌وکارها گفته‌اند در زمان بحران، «پیامک» مهم‌ترین ابزار ارتباط با مشتری برای ادامه فعالیت آنهاست. پیامک در زمان اختلال اینترنت، یکی از آخرین مسیرهای باقیمانده برای حفظ ارتباط، اطلاع‌رسانی، پشتیبانی و فروش است.
حالا تصور کنید پیامک هم قطع شود. بیش از نیمی از کسب‌وکارها گفته‌اند با قطعی پیامک، افت فروش جدی (بیش از ۳۰ درصد) خواهند داشت. پیامک بخشی از زیرساخت تداوم اقتصاد دیجیتال است؛ نه یک سرویس فرعی.
©
NimaQazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2354" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2353">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BTSf5zORTkGZSOCKuDsQwrfoH3auoTFS5aWNPARyWCFQGSXaFhs1xSafHwit2Bzi2WRZv99FTGBbAvuKi08MCYGOguiDk6CNDq8KY3uGq5iqv1MMzKFIZ1EXUoIikYI3bOM8hB7I6pD8coMGp8NPFA7wUoGZuEGLkg66LOKMRRNAsAwyLSs2LW5YpH2bQWi6IFuyUR0s6hVmh6WXPgT8eTx_Iz5NPD7Zj9y6Zr_A-1Bn8W3DP-FKUpexF1_EOqokENjhrrV9kaRGxAKyoCpInef6Am8dSkQUnQvELLVdg5dxspndEq8P7uIoU7dCb8SRrrhplLNbO1RP65XPp6D0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید به افتخار وزارت قطع‌ارتباطات ایستاده
شاشید
!
آیندگان در کتب درسی از تمامی دست‌اندرکاران فیلترینگ و وزارتخونه‌ای که اسمش ارتباطات بود اما ۸۰ روز متولی قطع‌ارتباطات شدن، بعنوان
#قصاب_اینترنت
یاد خواهند کرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2353" target="_blank">📅 16:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2352">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pfotU-BOBrKnww1ojc9JXUOaBVJKEvHSaWxVCsR7XPvibny3NFcSBAMQkuQ7TWWI2ApdGsbuy-q0zKlT2T6-b-BgagPtqhpcw3IA1MkSsS7ZUbiJ2WO2wJ_42TzmrEs1ZnvaUGLLHg8QSFf-8w_tvckOWtD4qNrmaGZwHWv8TQNR1CUmgzyMNKi8nUmpVeW7mtfpH_JHbH-HT8OYLOMTrcrSeRAAuD_SdCVqTOmfG5U0wCg0uaweYa0f4iPG4_Vakz_zYIA9Bt6FlCfNd0gsiVtOhW6oqmEQiUBnR9SpgJwkJPXatg5-53FmqNGdGxe3cWYCqfH_cf-HlegvxQ93LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی از پایداری شبکه ملی اطلاعات در دوران جنگ تمجید کرد و گفت: شبکه ملی اطلاعات کارکردهای متفاوتی دارد. در شرایط جنگ شاهد پایداری شبکه داخلی کشور بودیم تا ارتباط بین مردم قطع نشود و خدمات مورد نیاز مردم ارائه شود.
وزیر ارتباطات افزود: در دولت چهاردهم نشان دادیم شبکه ملی اطلاعات ورای یک شعار در میدان عمل کار می‌کند. این اتفاق بی‌نظیر و شاید در دنیا کم‌نظیر است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2352" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2351">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RY9cOj8vFGdtuy_CMnKtikMilBxzxsI0eFpqPKqPvItyRB9Zf_pSA7ZeLDbkrVA8MlpsLSr7REnn2AB1OUdiscsW1YhSSRuZ-2gUFAJx9BrhQpj3QE8-AeUxgCLGPVo9wZXlQ0CjBJw6c4X0pPzV0KJzE5XR6SQ_cvO0MWZ7AVkF86EAeAU1ZPV2Kt8nX3--EvXYydmiYM2irnHn_9UZc3LZBXvLscHK6-jsyRfewB4koFFt4JQbBGWFM14iMA4aPMjYHBVg7zyRn8sTQlBUdn55dswEDcdF12mFkqINVgmH6iemyC6_bu5hegOqjENrWODMgwn2_krLvDI7Q0LN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/ircfspace/2351" target="_blank">📅 10:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2350">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">باورم نمیشه قطع اینترنت به ۸۰ روز رسیده!
وقتی حکومتی برای حفظ خودش حاضر میشه یک کشور رو وارد خاموشی دیجیتال کنه، یعنی مردم هیچ اولویتی براش ندارن؛ وگرنه امروز وضعیت اینترنت، اقتصاد، مهاجرت، ناامیدی و زندگی روزمره‌ی مردم این نبود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2350" target="_blank">📅 09:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2349">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwOVOgchT8t_9e2RlCzf6cZXGXQ5Uy9wFBJ3fS0b_q7n4NaevMY2bssDsnjXeGTn3A662LcAQZy94i-EJexj2biXbWucTXGpG42CM8FvuJ0eVJsNcLuT3_iG3y4BrrNW0Gdwg8oMg2eBkgRQl2r-BdUylFy-yVzVMqPQiGdNKxLrVO5DUMaqb1kAO-m6neVxpDN0iTPWEwaiiMSWjE-omMqzPIIrSnvQfDZlpXq9phkdPX-wEkb0dtxc3T0ot1DsDCN_0-VlFZtSAG0AssiRBpgw0Yt8X1_qfUK4F96By5D0iffa2kNmoposeu7aLp1bsBObwZsQBXwWRLdTuOj5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان بعد از ۷۹ روز قطع سراسری اینترنت در ایران، روز جهانی ارتباطات رو تبریک گفت!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2349" target="_blank">📅 21:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2348">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hf3rLpE_NBtIgy6JvKt-rbGXFaDWzIS51BTwmtY3reU4zebu1Gn7NCf5sKIvUU9dly2Cbgibrv9aPZG-XmQPbCVFI0YzhJ0qF9YwAlR39eQobJ67t73fpHBbcVygFxFRNSMpefPAGOZjIBsPP_CAmhcb1BO-LnzFatYx1cXM1midsff7dCNQpwGg37nwVP7evSJuoKBhfecvDIf8Y6I4axLPpIf2-c3SoSI-XYaBEweqUJn9LTGmK7y5b8YvUUUb6aqTyCrYjtsaho2AsWbNkoH9H06MaXt0vT2994MPjjMu75u_azZ3MzJyLS3nEpZopT-t3RX_koGSHchogttztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیمکارت‌های بدون فیلتر، حفره‌ی جاسوسی برای مسئولان!
در رابطه با قطع سراسری اینترنت به بهانه امنیت و اعطای
#سیمکارت_سفید
، سیتنا در مطلبی نوشته: طبق منطق فنی، وقتی با سیمکارت سفید و بدون فیلترشکن به اینستاگرام، واتس‌اپ یا سایر پلتفرم‌های خارجی وصل می‌شوید، هیچ لایه واسطه‌ای برای مخفی‌سازی وجود ندارد. یعنی دقیقاً در همان لحظه‌ای که یک مقام مسئول درحال چک کردن دایرکت‌های خود است، اپلیکیشن‌ها لوکیشن دقیق او را با کمترین خطا رصد می‌کنند. اگر نفوذ و ردیابی، خط قرمز امنیت ملی است، پس چطور با دسترسی‌های ویژه، عملاً موقعیت مکانی لحظه‌به‌لحظه خود را تقدیم سرورهای خارجی می‌کنند؟
تناقض وقتی اوج می‌گیرد که می‌بینیم مردم عادی برای اتصال به همان شبکه‌ها، مجبورند از کانفیگ و پروکسی استفاده کنند. این ابزارها با وجود تمام دردسرهایشان، حداقل یک لایه پوششی ایجاد می‌کنند که لوکیشن واقعی کاربر را تغییر می‌دهد. اینجاست که بوی یک تجارت کثیف بلند می‌شود!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2348" target="_blank">📅 08:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2347">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اینترنت برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم
امروز هفتاد و نهمین روزیه که جمهوری اسلامی اینترنت رو به روی مردم خودش بسته، تا زیر سایه‌ی خاموشی دیجیتال، سرکوب، اعدام و پروپاگاندای خودش رو پیش ببره.
چندماه هست که هزاران کسب‌وکار اینترنتی لطمه دیدن یا نابود شدن، اقتصاد ضربه‌ی سنگینی خورده، تعدیل نیرو و تعطیلی‌ها بیشتر شده و مردم حتی برای ساده‌ترین ارتباطات روزمره هم با مشکل مواجهن. با اینحال هنوز هم بهانه‌ی امنیت رو تکرار می‌کنن!
این قطعی تکان‌دهنده معلوم نیست قراره چندروز یا چندماه دیگه ادامه پیدا کنه؛ اما همزمان جمهوری اسلامی با پروژه‌ی اینترنت‌پرو هم جیب خودش رو پر می‌کنه و هم به رفتارهای متناقضش ادامه میده؛ یعنی اینترنت آزاد برای عده‌ای خاص، محدودیت و خفقان برای بقیه مردم.
در این بین، عده‌ای در شبکه‌های اجتماعی تلاش می‌کنن با فضاسازی‌های ساختگی یا حتی ری‌اکشن‌های فیک، تصویری غیرواقعی و عادی از وضعیت کشور به دنیا نشون بدن؛ رفتاری که علاوه بر نبود بلوغ فکری و ناتوانی در درک عمق بحران و رنج واقعی مردم، برای خیلی‌ها نشانه‌ی هم‌پیالگی با ساختار سرکوب یا فعالیت‌های سازمان‌یافته‌ی سایبریه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2347" target="_blank">📅 08:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2346">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hx1Lz-p0BjTGCTtF-a3MaseQdINhNUeYRKaQOYHRBJyUTpj3Lk8KtMlRSE6mFA7XS6sns9WgJKgY2L5sTjtHnoRg7adCYIQBQ4VNC6nQVIz8voQn3JQmAbL89L3b39R19mHFpjBiFtxmHTOh4WzwHWnmuPQ9xNbMvIxDCjxVaWX88aATtuXI8PG1OuNIjPNSrQ4lrx2Y370tIFPIGFJifZkV_flyJmv8LrRN1wuQyBkFggakuzn7r1SKrexerDTRjOHGDVyGRH55fPsHlUO2t17cB66-GcovyQDwQRoyGTUy2ZLgmYYb3ILYrHxKUMW5BJ0GubLwJbFP45YNOtrU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۶ از فیلترشکن
#MahsaNG
برای گوشی‌های اندروید در دسترس قرار گرفت.
در این آپدیت هسته‌های MasterDNS، GooseRelay و FlowDriver اضافه شدن، قابلیت CDN-Fronting سایفون تعبیه شده که میتونه شانس اتصال رو در برخی محدودیت‌های شدید شبکه افزایش بده، امکان وارد کردن دستی HTTP Type لحاظ شده، یه سری از مشکلات رفع شدن و اسکنر DNS حالا IPهارو بصورت تصادفی بررسی می‌کنه تا نتایج بهتری ارائه بده.
👉
github.com/GFW-knocker/MahsaNG/releases/latest
💡
t.me/PersianGithubMirror/5051
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2346" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2345">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اپ
#شیروخورشید
بعنوان یک فورک از اپ رسمی سایفون بصورت متن‌باز ارائه شده و توسط گیت‌هاب اکشنز بیلد میشه.
آپدیت جدید این برنامه تونسته دسترسی هزاران نفر به اینترنت رو در محدودیت‌های شدید فعلی فراهم کنه و همونطور که انتظار می‌رفت، افرادی سعی کردن برنامه رو به حاشیه ببرن و برای کاربران نگرانی ایجاد کنن.
علاوه بر متن‌باز بودن پروژه و امکان بررسی کامل سورس و روند بیلد، متخصصین حوزه امنیت و افراد فنی آشنا با ساختار این نوع ابزارها امکان تحلیل دقیق رفتار، ترافیک و عملکرد برنامه رو دارن؛ نه اینکه صرفاً بر اساس برداشت‌های سطحی، حدس و گمان یا خروجی‌های بدون اعتبار AI، درباره چنین پروژه‌هایی قضاوت بشه.
در رابطه با تفاوت این روش با MITM هم توضیحاتی از طرف توسعه‌دهنده برنامه منتشر شده که پیشنهاد میشه مطالعه کنین.
روش کار کلاینت شیر و خورشید کلا متفاوت هست و اصلا MitM انجام نمیده، که نیازی به سرتیفیکیت داشته باشه! دلیل اون روش این بوده که بیرون هسته سایفون میخواستن ترافیک رو در v2ray تغییر بدن، پس باید از سرتیفیکیت خودشون استفاده میکردن (که در صورت بی احتیاطی نا امن هم میتونست باشه). در شیر و خورشید تغییر تنظیمات SNI و ... که روی ترافیک ایجاد میشه در خود هسته سایفون اضافه شده. در واقع اگه کد رو بررسی کنین میبینید این قابلیت Domain Fronting چیزی هست که خود سایفون در نظر گرفته بود، ولی تنظیمات و قابلیت تغییر درستی رو برای فیلترنت امروز ایران در نظر نگرفته بودن، که الان در شیروخورشید اضافه شده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2345" target="_blank">📅 23:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2344">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fnlb2XLIixOJG_35WYctmXn-9xb_6Rsiw-vh49JK6Lw8rltfkwxRjCVQS7RSNkz00ZvNw_ot8lmvwDGbpB4axD5KSmPIkvcFwoRdMe_QgsO-OJqZ9uJMcYkwCMM43LqGdJpNTSiyFuKZn-Q7mMcOHBD2YBy2K_gHI3w_i5Qa-4OI7dpGUZlONPHtcy78BKfuTbgw1t0rSNnit7njz5owDtU_Qhj65ABQyHwicwt1kR6VwkEdhcZ1WqFjvl7tJ4p8TbfR--mh_CQFDX7PR4AMaLNDEHnj-MY7hnAIkYKpqEqxfbClEEYK_A8q1ZBYf7B9AhCF9fklJjlYukAk0F7ZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتن هرچی که تهش Hub داشته فیلتر کردن؛ حتی گیت‌هاب.
قوه عاقله‌س دیگه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2344" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uorqCsf8Uh74cmWXp_END9RNpNwqdVNb05rLgQwWnzxW2mHXmUXprw7V7appDXS-GuNXw1Bxgb7MsPQITvhx7YC5ucZAhuxn_nzNAXYAbG-12x2SAVaL2dwF7b0Q17UVPb2oEWinMHFDzguBt_iRQjt8p5it8_2BpRSnF9xaDJQqGrVunBDQMgKWXzsozk48qD3_VFEgwaCB9944gjdiVpDBoEOMwec1hBbYE66evZkJGNSTBktw4VQYjwpJMlwhY9sXjUugoPvYHHqb-sSUrVmjpKF7e2WJd998obnAW4TkXqrm9FjAchy2fR2eoxvnibq4iZCoXK-_08uc7CzZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelForge یک کلاینت L2TP برای اندروید هست، که از امکاناتی مثل حالت VPN برای کل دستگاه، حالت پروکسی با پشتیبانی از پروتکل‌های HTTP و SOCKS5، مسیریابی، پشتیبانی از چندین پروفایل همراه با ذخیره‌سازی اطلاعات لاگین، بررسی وضعیت اتصال، امکان استفاده از DNS سفارشی و تنظیم مقدار MTU برخورداره.
👉
github.com/evokelektrique/tunnel-forge/releases/latest
💡
t.me/PersianGithubMirror/5008
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2343" target="_blank">📅 09:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YknqsbIZSs2K40tP8AJu3NmmD4k0VNryg-zrQNYVXt2Okult6Te3UqTUV8ZzHIuIF5G9LR5qzYnc6FbWejkh8xg69SThKV-lGKkShMbEs9thoeLQwLyYKesnFExKYq4KEpSP47mh-X_ilM8TKqNMlDxFsMpKfBKJuorqVXYkELxDJNy-0JLmncM1zwB4Hlo7cpnc5Uy1D7hfHwrLKn_02b4ojcxlYAlnd0Y_rKqpTNYd2ocVnqJHbTMc22jSatF-BAzxVpncGGLakWcD2mFNyY05q2TLHIGcLKTe_fK19KJ0Po4jdC3hUbWyZRZYYxeaE8vFPEqayN2X8KeEPN7hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آسیب‌پذیری جدید به اسم YellowKey در سیستم‌عامل ویندوز پیدا شده که توی بعضی شرایط میشه BitLocker ویندوز ۱۱ رو با یه فلش USB دور زد؛ البته فقط وقتی مهاجم به خود دستگاه دسترسی فیزیکی داشته باشه. برای کمتر شدن ریسک بهتره ویندوز و BIOS آپدیت باشن، سیستم کامل Shutdown بشه نه Sleep، و برای BitLocker رمز یا PIN قبل از بوت فعال بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2342" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2341">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iga8qaeUHFHS1SVF-xmTTMQO7AJwqJ-l7lMPQego6jaVAnvG0osao03DrTScaGKO7JW_5Naw0uKnj5IW_HIkVKnwh-xlusFGBKrRMe4jFKWw3ulDtHKUZR3425uOLMZnrqrZbsmALN1IG5mxpvdqVYTWTrlOKirq6LX4HTp82umO9TUypegcFBV8GK62SSsznrMlukdGVIgXmDNKSjrLAx7Wvg4HUGpVesoNzqccQhqnjTDKHAfT-h55XDhYUwNc7H_ZlnfwkR-MoUI0FQS32kSEc1f7S0x81EjnYKOWSEfQ2TBtA8yhPU6UhsPj4MdRxj3zBx3_ucqr8WxXA1z5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استارلینک مینی به ۲۰۰ دلار رسیده که فعلا اشتراکش هم رایگانه. کنترل اینترنت با اینترنت پرو و قیمت‌های کذایی یه توهم زودگذر هست!
©
imanraisii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2341" target="_blank">📅 08:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2340">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jCb7vx9Hnb7jt2e3svOUYhAqCqxyPR3cGcvADqDNifX3Uu1J0Dhgu19xdX2J3JkgMWIfDvDCBbmr89NpUc6y7tAjZOGbJp82nobupyDxEb8BSmdcyIA65yFYNLQ3GN8EBTGg8lraGPLtOnQCD_LDh-wqYqDLzqS8uUiSGIx7u7KWUHXpMirpTpQ83CmShYkp6lo-lUjh2fkcviVlzN1UFQItrr49kg8loP7fT5A7ZrMMA7Wg0Lu6c8vvwitkPPFlaQR6oNbN1n2FhP7BFhzjMOm7BcLd25_qP9JaaBqrlBvsBNmOmELVg4ncn-bdTvRNbwWzfXB4rkLmaZuSQuvLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هفتاد و هشتمین روز از قطع سراسری اینترنت، از جدیدترین روش ترکیبی عبور از فیلترینگ با ذکر "لعنت بر جمهوری اسلامی" رونمایی شد.
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2340" target="_blank">📅 08:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2339">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L21jJf8aac25qDjO8H0y0k_E2gZ_a1X2hmm4j1XKlap67xPIEo4_i7dXPEBkoUoTIP6N8so61ZRoS7sv1k8OiDp3rB-eftklisE1slZr8Ralo9yd2ICE2QSMHgYCjvvf0M2Lq6_4apYcpu8Aqefg42uKv_qIsNv4T0NVH9m6Bal2eWLTR2_cMK3QVNFuitW12rOyLCzYtd0z_T_ruMO9n7dqcbpQ-q8N1WKgrQ9etTevjHR_gEG6rO-5fh-AUscCTv5-Y9fguvxTUT4K-tWrBKAR5wCtQ5a8spsb7EyqsPe6iKswuU8OWcDnt0gvn1Dtk8fjNk2qWFYZ1GPWMaSaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتگ از تبعیض بگو!
اینترنت غزه که قطع میشه، اتحادیه بین‌المللی مخابرات میاد محکومش می‌کنه، ولی وقتی که اینترنت ایران برای نزدیک ۳ ماه قطع میشه، سکوت مطلق! ۱۰ ساله در مورد ایران توییت نزده!
©
markpash
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2339" target="_blank">📅 08:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2338">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iHQmM0494qX2AmIAFTrkZ1qBxYr1e9-cXuKGqs_46iV8h1ueR_5PrKdDrb9DLSWVuzrZP7wYHIqx0QhcZuNtfoDSrthPNbg3s_SnRAb-jZMaTopaXcq_ykUzf8aYdrUt25zHqHWUodaQ1FzBoeFwap5lY0p0jv5zxj8iN9pEX6p1Ns4yilpzkkyZ9FFP0Tk3ak7qz-fd3ore0fsqcfOHRzi2zbmj3uNnLL723yozl_42cRA8sJ23St6OiP2j2f8Q2pJ4oIxuFw8vlQrSubvlVNUjRVuDFMfZLWQrPSNThBGw3effsK1mFyrS2VfLX21U0aO0kVHVzsyA8M5PK9_rOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد حساب این الاغ [توی ایکس] بسته میشه، داد میزنه که آزادی بیان نیست...
©
AminSabeti
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2338" target="_blank">📅 08:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2337">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تقابل اینترنت و امنیت یه دروغ بزرگه. مردم نه‌تنها  دسترسی به اینترنت رو به امنیت کذایی شما ترجیح میدن، بلکه هر چیز دیگری که خلاف ترجیحات شما باشه رو هم به انتخاب و تصمیم شما ترجیح میدن. شما هیچوقت جسارت برگزاری همه‌پرسی در هیچ موضوعی رو ندارید.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2337" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2336">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ستاد فضای مجازی با مدیریت دکتر عارف در اولین روز کاری برای افزایش رفاه مردم و تحقق وعده‌های دولت وفاق ملی، گیت‌هابو فیلتر کرد.
©
pey_74
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2336" target="_blank">📅 08:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RXMi_STggP-dj_W3wiD-b4tR0WaVyrd5IwTCLmzpXQmd5oDadQLsLHgLBavPIhhikRvagk3qrceHuWyjko6-r74fQ4gnjFpgCjxt2mhYJYQHffaH3tAVbswdEPJj2thy6b5Noanrm2VZI3g-saWaSg0ItCObqq8OiQTiQ3dpkhPGCutwtTcg9A9O349QyVPGNt7v2e7esV6sGMGL1rbAAuwpbsssZJq8ZeqFnEWLGyzf63DCd3dfXSNHSuBFTBpmNBPM3osmG6FMpeYa13TBbs_60jZL1REFC_PpXaE3TNnNwnP6YKhJ3diFOM1Mwf2h8rZWQLHCjnkCZpiuHN50DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lb3XCjfHQWG0nh_DgBr8HNS3YGZe5cTudQ_tLDOFt_G-JY66jUer9Zi7Jqkb0e5FaTHqmiMn8eO4K1XfFQaJ3r7bdfgUKXe4unkZFaTOhg89PleNo_aZT4enGhnP9DV13SC5ETKELm0CIC6Rov4QpvZ7yJ8uQX21iOt-NFCk9Hq8cuJOo9s3EYOTzorJKj8KV274CnE4oWNJdomAx9-vD8G_ociF477Rc9cN0Ha7GYg0H-qU525D2Ki9jSyDermCvl3OBb1TLRSjUlHVrZ52WAVOMoc8qdg_aaYQerCl_1PEvq-1lCMM-QvfwHjA3oRvZq0WNUpu_hFjfeG5x5q4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNvchtkJW7URGEWtclTBMESbBb4FFg3ieJj5U_f2FRQweHceSVS5d7BB5a9wfnfMv-qe1jd_AaA2lax8ud5YY_y-nXX1Xoplf5c6EAX7D6gVmhDWOL6dBF-asg99UZP-O3VdxeocsDr6D9cdy0lSQESXMrqRRejDHEABQziR6WPbtTlVj_v5zGCdD8TnMgS0A8fyKNLlTiESnXIpMJQE5FBSHakP4LI9Gdd-qLwL2W2fnRe1mN3q85RKdNGNuR9Z8xMtIQY3EENm5femMNZ7eQXpQyQ3nku68vq6Uo5A4HhUncWVlpp9D4ZJwPOk1CriIKYmLUFAX6fDUtdMXPokDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZSxNqCe0jzWAOa7xtb0HWeibYKirCICbr-rGsquzR8BLEpWMkXc5k3x-IOqwVnesamGYJdBH_TOLMNWEOzFjAXFg8lNQ52gCM0f7tWVp6YOpcEq0-CXDQkMBHNWUOyIFtwZn_VlEYPCKL0a_8at3yWhHNQnbq6fQRLUuo9355KKXaRnk4-40cd9-dYzAK3__NinOfcufNIL1B_RqDfC6a9Z1n6nv2HyNZv0NILQOHyHhEHQMAuIOHTlMFmv6ohCDtDBgATtiiIuUFciUQgZYK0gg3flv2rifQhFWOKvVRYdVfTOlrREeZYQ3zgZdEOw7SwIa_LI6kCRU_RDi7_QVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قوه قضائیه در یک کشور مردم سالار آنجایی که حقوق مردم با تصمیمات دولت یا نهادهای امنیتی نقض می‌شود واکنش نشان میدهد. در ایران رئیس این قوه نه تنها حق مردم در دسترسی به اینترنت و کسب و کار مردم برایش مهم نبوده، بلکه چندبار شاکی شده چرا اینترنت پرو را سختگیرانه نداده‌اید!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=Dtbvj60d0zzvGWLvGSceRQF-TU8ne5K4MwnBr_1wvf0H5z3UBY8zfmY-gR7a4_G59t6m5YJUeO4RDpHeOEvWb9iLkYE8jy4BlJQwvZIgtKzkH6OQxAsbL66rgTtbk04_nuWBGCXLtd8c7olOFA9kCpdadSfrz5_J-S15e0w-qr1Uh2vyUZCHyc6yWNjxswR9M4zSRy-qexOE04AzTnBA4gKbKfAPKbPElV-mgRdasXiF4o89s6egTfbp6pNzq-fFemx3NL26rnA6M0DjjyKt6wd_gzDsZRZI3L2AGp9AKPaHOT41Fj7rlpjYb5-kBFEgKJubJW9iXSZiGxKrnsQ8Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=Dtbvj60d0zzvGWLvGSceRQF-TU8ne5K4MwnBr_1wvf0H5z3UBY8zfmY-gR7a4_G59t6m5YJUeO4RDpHeOEvWb9iLkYE8jy4BlJQwvZIgtKzkH6OQxAsbL66rgTtbk04_nuWBGCXLtd8c7olOFA9kCpdadSfrz5_J-S15e0w-qr1Uh2vyUZCHyc6yWNjxswR9M4zSRy-qexOE04AzTnBA4gKbKfAPKbPElV-mgRdasXiF4o89s6egTfbp6pNzq-fFemx3NL26rnA6M0DjjyKt6wd_gzDsZRZI3L2AGp9AKPaHOT41Fj7rlpjYb5-kBFEgKJubJW9iXSZiGxKrnsQ8Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هکر بودین و میخواستین بانکهای جمهوری اسلامی رو هک کنین، سرورتون رو کجا میذاشتین؟
علی کیافی‌فر، متخصص امنیت اطلاعات: در جنگ دوازده‌روزه، نوبیتکس، بانک پاسارگاد، بانک سپه و بانک مرکزی از داخل خود ایران هک شدند. مثلاً نوبیتکس توسط یک سرور زامبی واقع در یک مدرسه‌ی علمیه خواهران قم هک شد.
قطع اینترنت امنیت رو کمتر میکنه و نه بیشتر. سیستم‌ها نمی‌تونن آپدیت امنیتی بگیرن، سرتیفیکیت‌ها expire میشن، ابزارهای دفاعی (فایروال، آنتی‌ویروس) از کار می‌افتن و هکرها (داخلی یا خارجی) راحت‌تر کار می‌کنن، چون نظارت و لاگ‌گیری مختل میشه.
©
farhad_mottaghi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GXXO5-1-p2H8SF0qRfOVSWgrWvqHRWjAa2x3ZuOQ2ejbd7VuuqAXbh1Os423uEV703bUwHIpT-5Gw_HxJNnTEZTX-3J9KXPxNNXZRQuUQB-CK9SJZTi4YsrN7pNjr4HREmDDNBMmDGdpiowNvwMhvPwQS9OCU3f___Jid03UiWGjOH3hJjtkUbTfN8y47-fa7mUumjBweO2M51XbgwsPmldexSI2nM0SYmRylacj4fS8gbr5Wz7za86fytd6qxf-wRnev2KluZLGAdG0cbfvGv0Rt8nOTP16YwCNPubka2nxD_VaZcniIRAABA-uu3asnQmWIKMH8GXt5GVI_WF5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگهی یک دفتر پیشخوان دولت برای فروش
#اینترنت_پرو
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X0CUZyNsh8nr4J3bRjsjakW2JotSIqN8PeAuwY3F6YmN_bw4krSbUhb6NCYQVPZZcNiW4WkaaTF1tgJifR2QGpzoPpbV_W719cpGleCtrkGsneWJIzWrKms-M-sVoiNIeHRwGjssbAJoNWKSCm7SLXhZNvXK8LNDZ0tGxnBUtahVhB5hIStIZDQW6NJcN_F5dAZrgehoPOzSxu_Q-Qkf3P2X5j53cKvA7o81GjZ-yEuKezRPtiJEapy_bGXC5PSoAxtpGhJcMi9TuvCZk5z8RndL6vgCfUUmCYctNtnP7sowd-hkDrAOd8Ha8Y2XqS6n2B1vF5jTBPDFmGuM9npefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تعداد کاربران اینترنت پرو کمتر از نیم‌میلیون نفر است!
تا امروز یک اپراتور با ارسال بیش از ۴ میلیون پیامک، برای بیش از ۴۵۰ هزار سیمکارت،
#اینترنت_پرو
فعال کرده و اپراتور دیگر با ارسال بیش از ۵۰۰ هزار پیامک، حدود ۴۰ هزار کاربر پرو فعال دارد.
©
aghplt
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dLY-gI3oUJtL7r0-qj0-DWZ9s9J6ogU9nIdE7Gw-oImEKEyl63yMAkXInGdFcsp1sdzUUa9ahstv5usBhXjxXfz_0Ua3hQRGdv0b1T9fkwiy-EBW4SIsogD7F1XB7FCCM10FOtvBno8VFo7JDwrEznSg_EQLRi3QwezhSnoR_u8Rl3N2pntZ4aUhp9NqlDAmipJDMmqMQ8S0ObPWb6r1g5ghx4ISLjKjaY982iLBZ2CCoWIge8AIyqp44SmrzRyo68cyfdMUaH-xNWiO0MYEIr0ov58TayFq0IdtawzuO0iuXYpCXg1cIoA6BRGrxGhyZ6mVj4hNhZstsM77UI5-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن مهندسان نفت برای دریافت
#اینترنت_پرو
واجد شرایط شد.
۷۵ روزه اینترنت رو به بهانه امنیت به روی میلیون‌ها ایرانی بستن و هرکی که کار و زندگیش به اینترنت وابسته بود به خاک سیاه نشوندن، تا
#اینترنت_طبقاتی
رو اجرا کنن. مدیونین اگر فکر کنین کیسه دوختن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بدتر از قطعی اینترنت فکر اینه که سالها درس خوندی، دکتر و مهندس و محقق و پژوهشگر شدی، بعد واسه کار علمی دسترسی به اینترنت بین‌الملل نداری؛ اونوقت حمید رسایی با حول و حوش دو کلاس سواد برات تصمیم میگیره تو اینترنت نداشته باشی، تازه خودشم تو ایکس وله!!!
©
NiHa_Mehr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8hkyK1rfuyHuI9i9KedKO_dlseupw8AHRYtmfk81l2pBDF76zZj4HxGpzVjP8b4m5Z4gIweAXnOmH0Xvf4tmIJLztLhNrgM-O1PzLdOfQDp91TO3Ry_97uMDDvkxPKl6pfV0xiRzBj1PMoIuZRCc9Jt7QvQZGD2yrqHBGhYvIoGLbp2SVR6Td54520gu9A2Z1ZlZhrwAqQUeHKOvyAMJOiRh3GIpUpVvCw7M4q1A9Ti5gzT2fDdKkQ6jr214SEJ7CIkNwF9dpbNcrn8xvC9zBTL1OOjIDlsBWnxPYVzDvcJ6BDgrJY9SvvOLUcY4DyBTa9_kdVqLem7nUNvGqiLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس قوای سه‌گانه کشور در واقع ۴تان، که یکیشون به نام
#قوه_عاقله
نه توان قانون‌گذاری داره، نه زور اجرای قوانین رو، و نه در جایگاه قضاوته. مهم اینه که قوه عاقله قصه ما با
#اینترنت_طبقاتی
مخالفه و قراره نقش اپوزیسیون داخلی رو در این مضحکه بازی کنه!
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y-ZNxqxPPBqw-8T96YeeyxVi7aWOURIOQuv8nCkgmDRB0LPd6T0bqCvRPdioZa1wPYFQdZ0fiU4JAuM0IQ2dV5XeL1yX2W0yHhLeNEg8YmzTO2qr-QuyIjT7mDne44BkhHEjZZ1QvSnBttIh_naU_mhQ5bSdTYYSV-czw3iAPFItJix8Id6g97b2JSEALB6WCJKzFz0EabERj9SG7zEKZlNt9jN_0Yp17ZuLtSp9fH13ZuhVUUSo_zA1dMpp5iHV41BinrfeiIripRfsLwzQFuVJDI8TL4CzohCrmk4L-IwE682ErdeXxse2ef4H8RH961-ru-ahEtN_B_i2nyILCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای
#اینترنت_پرو
به اتحادیه صنف اغذیه‌فروشان و مواد غذایی باز شد و حالا با ارائه پروانه کسب و کارت ملی میتونن از
#اینترنت_طبقاتی
استفاده کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKA7xosuTWBJy1OEuotyG8QfAui7PNAPIOO5OBJsw_5dVcPjFiT_EgF1EuHUDsKpVVy1hXpV3UxveLb7CjeaKa0RbKn7Xj_OivFS1MnnNMN2LYGlv-avDJVQyW1nqcg8cHb3ArZm3BIFVE_McKDpABQdvJR8369RNlJQkHVNOIl4wF2h_vuD0gcLDRFjo-27GWC8KI9a91KU7rhThSAzMLkpWKajKnv8FhFG1RUj4Xs3f-MCafeQagScwbzfvBCf8OIpDtk25C6Gjg5_KVQY1m1fdrl5HRvWS93Mry-UtCbHIayVfKctQKDei5DPkpKpZdyxMzzBolHZrYz7EpSWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BpnTyNpxNcwUfHIUVLx-_x4lYQFf7BpMV7tOjMtTtVPLxd5DpWIBGEmH9vNoq1XaNvaPlOFOH9Zi3whiskKChf2GMw1nc2UMetx-JZVqipkxy8pznOuH9isemNgSuw815PAHyor2u94lfQFR8lI00SDkWPb5lDMI_1g-zymGQ7u057PoLDEyht0VIeQCU_Gn0WPX6N-9sWAuhGVhASIG9GGUUdGpI7on-EwGQHkDH_IW7murBAzIeMD-NA1kg6yHRF_uiDX5oCkzv0PHjUM6DqvXtlRS8diLh67JsqctseW2Zp3iWujZQJqRwJPLH4lx2_DVwMThiY5I8jMtf4DSJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PAPc3tCsfiF1mCgAnknMrn2HfOlv-ARMwrTNL18DRFVYf-yEySEBACWgUDsOBr_qfb1so_oevfocCm05E8EnFt3W0bebKBL10TJpKhkDYyCtzWV-_pLKYcbB1WxZQZu7hFQo29dtWjjwXnXYbv7pplnfL_X8f3p-sa-MdlHBjfoZ3Z-PTs40gi1ppVAKoQiL4DQT4m6_K3zxBPaGvBQXvEOEgaoXSnUGtz7TGLIzdxrCzRkRFW0naab54EYr5-urKtY3Uu8eNYqRddVVWflUCqqus8PVFR6tyJU7GexGuhx5lsM5UtjZ47m1O-luTDQ2YTggfmrziH6RoxF1U2fdDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PFw6aVRAujkd2ApY5jgaNsemuQuPuyvH6WorzjBGWUhAYTMwB_goM9Ee4POyTiftCKPx1WVLpvcV7Mwt_dyk-u1MGf6pJQF0gmo3-bvxG_B0bLATfx19YMLjfrAbWFw_jptRjB2tAL2WixlNbxUe31zj_-zx2dryze-BCD9NEtOltoZFGT8Himk9A1X5rrGuTP6nSsNoGs4MyPZNm_j1fme7I8urN7ror_2gajd0RWuWDjBym3TWNmvEg8-PQNOG6eABc2fzAhT68aQ_lelW9ig6EK1bTXSVKStJk-0iH-UkRq50Pmn9LTMGSWaudpA_mlTg_nAeg8R3hBCpTwAWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQTY2C1MuINr741g8YFdw_oj4I9iXljvz1OapJBm3Dkad-_GHQ5bni23PubXF6bz1M9rty6B_xtC0BaIqnU9R3Sn2rSVYZDPKSM2hPw5ATWGfCrP9Ls9Re5p5Z80HzO2s8y-DKRhQ2QE3I74VZf5rGgniaKQBQ0kNoPVo-eoBDb8k1yBq6V3LvwSnNBj50HR48yVUXSHrtyNN7nTVD3gWWRNc3LEQfZLU3rmOsJBD6wFBMqcABISaZ4BuhrL_cdnQXzp4StUPTRiiJnwqkZhgHXuhNVqFJUpA5z1afn8HxyOZZ4Wh-tWCHhDI4FdT_MXU4dhkaIJyNmoE3uS4ILVBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BgM30t58V22L-pd-999-aZ9wX2sMov6sadS7R_JCQ56UPJ3yup3mYmLzjfukDGouxahSQ4NK6mt5g7s8S1RRiJz7GIRVI31BeVwEK0rIHgK7lqt5yGdtpSw3CxdI7cLiW_ieM7hJ8R4usNflJPBlCNDyFistEh2MxiEWyWfBi_JANUH2CfGU2lU9Qq-Azlqf51z8XW3hJFR_gGs1v5ZNhQWlv3vyWPKhlbf4qXiZAEbn-O2HTd6F5K-lzzHjcLKQdDGr0e4MmqY1iwnzOkM94oZauAnLKl9CczG9gS1pIsxLBkMFC-TsF-ngsH5F19skrbdWvOA8JUlHd5cP8LiE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GFI3hYIjPaddqxFQZcKvaXzpbQlODtUhdz_GSDzrAu7IhHwSpW3tRXazi4houEtFVX1mdTawK5cz8YIX80owOxMQrhO9oue8l-WpUSgA3I36CFdJ9jlp7Hbv0NZ6bfdPte60tpjI3ZVUM3_odVVFgkNmUynWdLxOM66BcO1c97qpf9-EOXwSkyHROJo7sU1rwTm6qg9pDffD6aSXqvSNJuANod_PKESdka9y7vsFBag4v95148dGcbaoR6TdcBnkozW3cB44Cijlp1eP8Tki3Du1y56HLsx8vytthx6BV_XGntlU8XpQXesMLuZD_HhxiSzPc2K7lgbccPgGXur8ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X7OaXLGv3Z2_qxuHppFLpxfjCMdlSUTtvdRrpPpmRm1bxbpMgPaPcfrTpcbwWVhf-OkUbhv5rrL15SdTN-KqGreK1FLYS5qratxEzKFcKZAzjq28hKIUAL8k92uvvPNBF3_9FBOoFxvTW5TAjp11fuFnox5gsS_w4STl0_55su4dBqyBK3iucnRRQ_gSYoHeS_TtXUTUbOgrsv1eMfuAYfVCOD0LeCHWi4550vj4g6KI2HHI-Zdo0nyxVaYBZ5laiVVuV29Ji330cmEKtO4MsQ0IKaZFmHBFtHXk-zpA9kIOZef91ewbIWpKLrDgjp_jsSfjxXTDDsIUUBLQBVed9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tej1X6Sw2uVSGW-IoRub88BqYU4vPX9zT_9Pan4409auy3qCe60UjmNAITFhIfS_f5oT7kVW4f7l8-ZbaZRJLGFyV7n3lkiGega7u9-A2tFCBnh7Yx0dU2jbdREm833Jq0yh2GntoznrIVVYZ882ij_0B_YkwlEeXbN1YFPU1-J9iQPH2xD_odht3HtzXNPn3P3xFOjZEyq769oj1VplE2RTNuHfkwQroYGC5VlUWCqfxDFjosbJHhowAhcLB72d3y9p23ati3iD3YQr3Pza6TeN67v7Hf1jBJ0vhWNWe7q4I6Ugh7TyHxw1MMeA_WLBfbpusKYuW7KSDV1feV7QcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vidIqR7vZ_ho8l-c99tpakCtMWhwhpnYXHW6zJZhdl9v4e0B49CHc1itkTWqcGBxRjFJcos-lYmhk9BviS3mGhhKPd0aJVfbV1VtxSRGnELiQmlFyYW7LFZ053pEnEpMdolwC-iMEAyQmOnwFBVg1huPfkqlS6px3eZvrkwkZPFicnIuiUolaXqiKSR5cJGywSMLW7I4dHKH2yfws_A7eoiXHYlsdws-WeiUxL2z5EzvxWBWqmY4kNrmSG_NwNYgiBmWVb9jVaf4VGeZES2dA7leaRRdnVtPCvMA9sr4u8YNzU76RIqVJ92baqDxvJcWsRiw8zEJuUDG6aw1CoW6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f7ouRX7GVpLyPxKBAyE0zJ_FiQWcbPnxY9Dfp9-fG5vBnqbBaJWyEOkDWyaKvbZ128OauI2Pw7VpfMa_SQjwaiKqkPrt8jHFtlN4h5eGcK59SdrYsPZHAsqy0iOVCvF2tIPZmSjiNSGLzeBOakkH_h-PZxhLDw-ItMj4Acz8sX6byl8-YWE9A69g0tBJUr3rhTal94hTqrZBYH4eFy8m35StmxRCSdIVYW0DRxF3oWHi-d6IB-Bx1j3_ZXj6NFAZBK4eOb6e9C1LZ08vRM5KE6JxDDbS-zIC7O3u9k9zgubfZtzzQlOObl9t5_9zbRGNdTvWGONedNbx-uQ7nc09jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u81epWyOyxRXa0GAsyywTqu709X4SwhvVNa7UysKp5tRFM92VLfMx1XO7LxepqzLx6t9dh4DtK8sBRGIP53Q66Yx-zsqwIXJzU4-AtRxq83Ycrl8c6HTJ7Vt6BSSQ_5_xWemymI7F5QBoKSJJfzzN9mD8r8iO_0uvEivlJElxnGZropJZIhR4znPBRQc1mnUV29jCFdCUcgWQ1loEr1uI7mAMzaVYzCRsyKjknaM7fnbXe0RmRc69w9LK8Z0NcO1QcS2N-BgmF-c6jJiDn5JvSb8BtYrEPRhnUvlaVQ04uGlIrtK81jg7OnsVPK1yFJTpewrE6t-umtcNUSgEw549Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jI7Gm_ZmiV8TH2v-Fk3wwUCE5LGbnullgrAdXRxV3xEf-dnIOhg7KBFmQoZToPMxmDUdx5j_foBEyGMHiw29aza2x6wJBCoQ6tC143Jpd7Zi6uS63HEhlLYCCznSP1y0mbZv06ADLj3xuKo8AnBpPwyPOSycQuuxiMvNIPIcK-Huplo2Tg4hT01I-qpe_hQ492-cOnGfPH95XIbp1vg99hj5FC1HdM8MTSAmJqs20WrS2G3SPWMx6Tz6ZZ7GgL8wgnPo4A3HfrlKu2lFwZky6TPZHNW3hykkvZaiTXWgrI_MYLwO3J871XiOmd-yEhgUNVBnFbtry3728BbkD4V0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QP0knvd0D3R6lM4X0R_uFggKQgpM5cocujXMFON6vXp2QYJNavx6B0LI10vWLkKseajWJb7z1qFk1dPNYkxhUbfybAqt1aoZfxh8Vq3fJe6RJNwMdp2lBSP3POnUrYh7JOyF6JKvu7FZgDknVW7K0K-nVyNCuxF6J3eqFTEdFXQrD5UQOZuWH7x2AzBHo-hqCd8O33SxlvwQzspbVNskdLmdvHjzPXKPGlgsmM6__FJwccoaOTd9KjB6YXiASI_9QEyPSAHFdKXJx5RRVSPmSPN5aK69Y6nP8rG3qOD34hCJ6MMAvTWxXzURy9d0qz0ur8Io1LXBoAzJk-F5A45jCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/blUVRaKzuGf3r1EdJVgTS-3P9lu7PSWPqZnpH_sSHGWagZDqGNyvBsn3KjWEvECpEPGVs7kkmhZ9QY3rd7mNUJ_0nWEda-fPik1K5IfQkSf7X7zQ6xwYg7--6A07lGE9tADAV9kkdeW-aqBWX1Jf16zSLJVf8fVZepNJDpS12CxpdYLFtVSR4CZqkGwWcjDbsOM-ZQxv8P-7gOLYuqp9-eTuP2PkPpkJZmzKlK2219LEAyXncoMlKBNWBnCJJHGoVYQuP2QPFClAZzr-YB-rT2oobQkMMzURNVvQSNoVUQvXPgB5cMAX3QbbHD4nBKyGnLRRat6x1fmzMwRUgQY8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JLvs9VN2WuCNZren10dKJklRlJBPTMWwGgLNVazA1-RO2y7lUkRLguPl_gaFRhcVGzhtkKfSQL27lGxb9zkIH7ad4Ii5eK3AOkgXACjXjHRYXve32_ZKt_536oT7ahXWcVUPxdJh2FryOPZXMfjqOrm69GHO-n-rtF3gACo1S9pQ-vDJjniYHzXEY0ofowV22w8khGSnn3C11822NreEblYMBHEruYrge65qkbZG3CRnsJhBbx3KhGv5BvrJliiADALBvET3OpJuP7eG-xIdS22gBLo3-Ur3pNW7W-UG4jLdiKqGM3tRt50-yYMDUItFJZbWqFuo2GXrjUO0_qMOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T2yZyv6VMK16K_EIxUt9zCHdsmx88pDgZAdwE1pxrbr-kvog1FejF_wAiZaJrrX7B-chSVQTiZ8MIyThoFqRCmiSbcjd6jHSDuCJXqj2zEUKNrMmSbECNiAebWbIugKvZMaU9GSMjCwnIfJZ16fAX46E5bAikeToKxQlPBsoAqsS-F39H2CgpzOyoFhV7xhMyUx78G3HnJI9nClRpzkV41GXCbFZdiEY6TPLVd-hqb-cAbOMeAQLHrb0KseszghbjBm96yjXG1mZmBsIWLyTJPPQULll8zx7LP5w4gceR4Ls1KK47ZvVKeRhAW5YML2uuknSfixApdOsjCYa8KKyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qHeTFCVftpUuRDywWl3DkJmw-40bjeeYAzZwrD252I87itnnVM5oGqi-0llFGPSRStwHFXWzGWMXH8R6QFqZOyVxok5lcrddjaayRWPYkFQ4S2k59ESiTKG73--w1q2Ymr8tc4qyaXLTXnL2NPZfCIdSpssq182IJJv6jJf0y4L_n-cqupIKQ0cK2vTcb9mzE_URg_OfCUkFcrelYoewB9fYCNG9v2yP89HNHNY_ONirFO9J8DK2KNGVP0fC1eL_FIvs9MhNro8IKCxe3AP_o4UwvyA-D2Uhe7R6LR0WcGHcm3JxKQROY4vYNJUpEEmjKw7LhtdHZbuvpK6XTVnEZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">۷۰ روز است که جمهوری اسلامی با قطع سراسری اینترنت، میلیون‌ها انسان را عملاً گروگان گرفته است.
این یک اختلال اینترنتی نیست؛ حمله‌ای مستقیم به زندگی مردم است. کسب‌وکارها نابود شده‌اند، معیشت خانواده‌ها آسیب دیده و ارتباط مردم با جهان قطع شده است.
در سایه همین خاموشی، بازداشت، سرکوب و اعدام ادامه دارد؛ بی‌آنکه صدای قربانیان شنیده شود.
اما بخش بزرگی از جامعه جهانی همچنان ترجیح می‌دهد چشمش را بر این فجایع ببندد؛ چون واکنش نشان دادن هزینه دارد و سکوت، ساده‌تر است.
For 70 days, the Islamic Republic has effectively held millions of people hostage through a nationwide internet shutdown.
This is not an internet disruption; it is a direct attack on people’s lives. Businesses have been destroyed, families’ livelihoods have been harmed, and people’s connection to the world has been cut off.
Under the cover of this blackout, arrests, repression, and executions continue while the voices of the victims go unheard.
Yet a large part of the international community still chooses to turn a blind eye to these atrocities, because taking a stand comes with a cost — and silence is easier.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قطع طولانی اینترنت تحقیر اکثریت بزرگی از افراد کشور، یک‌جا و باهم است. اما این بین، گروهی که شغلشان به‌هرشکل به اینترنت وابسته است، تحقیری عمیقتر و نفس‌گیرتر را تجربه می‌کنند. با آن‌ها طوری رفتار شده که گویا شغلشان "مهم" نيست. حرمت ندارند و می‌شود با زندگی‌، زحمات، اهداف، آینده و برنامه‌هایشان بازی کرد.
©
DevYara
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vE8_8PxXAWuKgfGBavz3mlujrhfHkYDtu9_INp5RDVr2wTuDnQILRBT2ASzmsqe_0N9N5PH46nsgJ5PTfyQn_dmLsRBA0JpEAbxVNL4yC7B6eSoroL1pUnf0lkRuj7C-BQCDSrZVG8DgzP41-FGA9ldgOh9VquxdvNqx1hEndV5RHmDEzW9Ap26mGAOdbgFHurGnho1DYZiUt7fy6TPlSSSNzakClRgzCUxWQVbOMK1o969pmMm_BtLCji0w3qo-ly8K3zc-dll1xvwEcciK1xbMk5H2mQBGshRAg2c1hhuQnr1J6rPjcQtluOHZxrJhGV7Tp_ZfQHPz-n-VmOAiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی شاکی است که چرا با وجود اینکه که پول داده، تیک آبی اکانتش حذف شده و ...
در همین حال میلیون‌ها ایرانی پول اینترنت دادند، اما بیش از دو ماه است که یک شبکه داخلی که فاصله زیادی با مفهوم اینترنت دارد بهشون تحویل داده میشه و از دسترسی به هزاران سایت و سرویس محروم شدند. سانسور اینه!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سمیه توحیدلو، عضو انجمن جامعه‌شناسی ایران، قطع اینترنت را از منظر اجتماعی خطرناک توصیف کرد و گفت: در زمینه قطع اینترنت حاکمیت هزینه-فایده انجام نداده و متوجه نیست چه میزان خشم تولید می‌کند. آنچه در این وضعیت تشدید می‌شود، شکاف دیجیتال و محرومیت نسبی و شکاف حاکمیت-ملت است. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2286" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2285">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TFX_iDVv6YWRHdt3_QGkHOYVE3SGBvZTAGdGAhSvrIQXL3ltwD114jpLt3XXEeJe2JKq4qvtI8--JuACFTMLkbVn3GCeUdSfROHz-vSgRhMfmaOlv3T7t5eQb-hSHcSNFNlV6_qmfrrFm37TBcHaRee-LcJo3SvyzpJPDY5d6utLC1ibYNhsg6s3L28hiyznuYBaMnHHS1ok1pkJskPmu17g7bxwIcFC-btyvS9me_t2e2ofYnWLg5TinIgQrY8aXYqmiPH-2_IGWtbxp8aG3xua_dcFMRxBci_6lPWoYRfn1JXoz32fnJt5LsNOgX7F6QX1EieE2nVNq9fwusk0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شرایط فعلی اینترنت ایران که روش‌های عمومی دورزدن فیلترینگ عملاً کارایی ندارن و اسکمرها و کلاهبردارها زیاد شدن، مدتیه یه مارکت‌پلیس برای خرید و فروش کانفیگ راه‌اندازی شده تا خریدارها و فروشنده‌ها در یک بستر متمرکز و نسبتا شفاف با هم ارتباط بگیرن.
طبق توضیح تیم دیفیکس، خودشون فروشنده نیستن و تمرکزشون همچنان روی ارائه و توسعه سرویس رایگانه. این بخش صرفاً برای وصل کردن فروشنده‌ها و خریدارها از طریق این فیلترشکن و حذف واسطه‌ها ایجاد شده و فعلاً هم برای تراکنش‌های رمزارزی مرتبط با ایران کارمزدی دریافت نمیشه.
در این سیستم، مبلغ پرداختی نگه داشته میشه و برای مدتی بعد از تحویل آزاد میشه، کاربران میتونن به فروشنده‌ها امتیاز بدن و تجربشون رو ثبت کنن و کانفیگ‌ها هم بصورت رمزنگاری‌شده تحویل داده میشن. البته محدودیت‌ها خرید بصورت رمزارز رو دشوار کرده، اما افراد خارج از کشور میتونن برای خانواده یا آشنایانشون داخل ایران خرید انجام بدن و فایل کانفیگ رو براشون بفرستن.
👉
market.defyxvpn.com
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=sgAuu7voM9w7oIol5LVwT8e4Jm_Vscdmqjw3eixa7TerGhUSkZE7hKDQ0tv0bRuLMftRrJKZPN7_MhDJwrID6kqyrjwDuXx3OBpyHFqN7VLZF4eNKpiNsQnacrCcWfSETtpYcH13LZFxkVoLQOE5TnXzk-YQsIWeEW6-UnEJBiXR7cKpsTAf6EcIWOeBmwpUlTT6j2I2Nn6PckcXayIH73w8yMjdwcR5D2vpfqAYx9bqD2cDT7NJzrZ7mtUqDVzZ5XV93SmXw1jhL8ZU_pDqvctBQIv0FhXAknjhYMOsH3FkFtOUKeL22VX9KxudoVQmK500GpCObYhcD4WHgkROKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=sgAuu7voM9w7oIol5LVwT8e4Jm_Vscdmqjw3eixa7TerGhUSkZE7hKDQ0tv0bRuLMftRrJKZPN7_MhDJwrID6kqyrjwDuXx3OBpyHFqN7VLZF4eNKpiNsQnacrCcWfSETtpYcH13LZFxkVoLQOE5TnXzk-YQsIWeEW6-UnEJBiXR7cKpsTAf6EcIWOeBmwpUlTT6j2I2Nn6PckcXayIH73w8yMjdwcR5D2vpfqAYx9bqD2cDT7NJzrZ7mtUqDVzZ5XV93SmXw1jhL8ZU_pDqvctBQIv0FhXAknjhYMOsH3FkFtOUKeL22VX9KxudoVQmK500GpCObYhcD4WHgkROKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2283">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وارد روز شصت‌ونهم شدیم. میلیون‌ها نفر رو با قطع سراسری اینترنت گروگان گرفتن و بازداشت‌ها و اعدام‌ها در سایه خاموشی دیجیتال ادامه داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2283" target="_blank">📅 08:16 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2282">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EGU31uUdXVuUSXIZV4YkdIxerXI5-v6LfgP7an9Q0o8HyyTO1UC6y151Uidao6Tt-0e03JdU5pZDFjTJUoP1HBU-RMXSa1L7eM_MNwpbwJ7hzGZ3MPEkQwtUi4qXjy3ETuEHl90-cdIurSCvslwwmC7OCaleElsGG7PnlwW8Chcj2zum5UuT9VYveMiignSem-mu86i_WYf54i6fVG9uJoC9I_BDvvmDyFhkbI7WXvUO8GuhTBtGwHfA7IpqEJGhWr2q6nE4jJK6t4mEqtj-KqcJfEhTre8FKjpzxY9Pb67Or6GacuDaTZ5mh9tlY2CLy4GZ-JitZ8eO_MlH8vMiqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از اپ theFeed امکان فراخوانی محتوای کانال‌های عمومی دلخواه فراهم شده و پشتیبانی از اندرویدهای قدیمی‌تر، حل مشکل رندر نکردن نظرسنجی‌ها و ...، بخشی از تغییرات جدید هستن.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/4273
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2282" target="_blank">📅 18:20 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2281">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uClLc0D0R_7D2ZxLDkpOjiBiMvltA3QF1JFuKm2b7uVRulj8TaIVPMd0vWJ_II1LJS05EfS57BnxDTSuVG2v_wyj26RiSeMdSLrWkIvuU835IhiEYa4HaHGQL9sgkAxfa054oICi8hvFozd41l3eBo8aEAojXS1hy5UA3X6HDQRJqeUC_d6YphSGXgjutO1sJZyDxVPKMzQNQ-oB2Izeh-SI-QKXFZCBvuPKdNYJ8-ji_Fyy4CZn5UQfb8MRZRlMhmlGP_L5KgrFPdu9z4cdICCFf9NL272IotmOPyBZxpd-ZIJuutmfLtkNLMsyhnUcvxDJYfegBFOWcW9BqrWeiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای آسیب پذیری اخیر کرنل (
Copy Fail
) فارغ از اینکه آسیب پذیر هستید یا نه، آپدیت کردید یا نه و کدوم لینوکس و چه ورژنی هستید، همین دوتا دستور رو واسه محکم کاری بزنید و تمام:
echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif.conf
rmmod algif_aead 2>/dev/null
ریبوت لازم نداره، ضرری هم نداره؛ چون به صورت معمول شما به این ماژول کرنل نیازی ندارید.
©
tiosus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2281" target="_blank">📅 18:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2280">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قطع اینترنت به بهانه امنیت ادعای مزخرفی است.
پشت پرده اینترنت پرو و سود حاصل از این رانت در جیب “ستاداجرایی فرمان امام” و “بنیاد تعاون سپاه” می‌رود.
حدود ۹۰٪ سهام همراه اول در اختیار شرکت مخابرات ایران است و مهم‌ترین سهام‌دار مخابرات هم “کنسرسیوم اعتماد مبین” است. این کنسرسیوم متشکل از “گروه توسعه اقتصادی تدبیر” وابسته به ستاد اجرایی فرمان امام و “شرکت سرمایه‌گذاری مهر اقتصاد ایرانیان” وابسته بنیاد تعاون سپاه است.
در واقع گردانندگان اصلی این مجموعه و به نوعی مخابرات و همراه اول دو نهاد ستاد اجرایی فرمان امام و بنیاد تعاون سپاه هستند.
©
yasharsoltani
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2280" target="_blank">📅 09:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2279">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۶۸ روزه اینترنت بصورت سراسری قطع شده و در همین تاریکی دیجیتال، بازداشت‌ها و اعدام‌ها ادامه دارن.
قطع اینترنت فقط خاموش کردن ارتباط نیست؛ پنهان کردن حقیقته، اما خون با هیچی پاک نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2279" target="_blank">📅 08:21 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2278">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/muNnrreRX82hc677LmgrCP-WjYdTrm3kDLXImuv819IDXzEeHQXE5RMn90QAKz73pdZ_Lp7W0G2R8Eb_6C_w5fXIF0t1ObfleutBti_tB732zxNcsVmMfTkotFNVYGbXmCacjw_NYTslEAz5hPNXqrMSA0Dzb-plB0zB4n8lxHc9hkRmlt87U9YP3b-oEIcXeRGpWo27jhYmUIALlq2yUKm--a2T9OBJcmPLjGx1OxLSx-IWsnT4EcknA4eVFuRcuwovJEcTF4ioPdWulFoEQ5r03IJxHN6YYKZmHAyhEWx0_5ktqp_IM6kQqTGkf8dszp_G7ClsM84qQnmHQUXNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۲ از اپ متن‌باز و رایگان TeleMirror برای دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت منتشر شد.
در این‌نسخه بیلد لینوکس و مک هم در کنار ویندوز اضافه شده، برنامه چندزبانه شده و یه سری از مشکلات برطرف شدن.
این برنامه فیلترشکن نیست و به وایت‌لیست فعلی اینترنت متکیه، بنابراین ممکنه روی یکسری از اینترنت‌ها کار نکنه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4295
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2278" target="_blank">📅 20:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2277">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MI2W9_cxS1CNRvJE_LCeIXdX5CMhQVICt276n87nnypyKkHOhuVJkJA9M-E3CS942D_XcZDEA5bdD5TUMdC3PFyOreWf8L2eGjiBeyBY2cCCmPP3FFjqluDzMVMJgAOqZmtNoZB_8L9vLnoOI3g26r6Qdgh1rkTwYJFhk2aw1FqRpA7-jN8usfPVjmfxjJMHBbApguWXrqKws8IvkeNN3Dc8dUNul49o8wpWW6HSalqJiwCACV7Rz_biHM5e8Y6sXUE0g4Q87xVR2LiBcaFdIoo13QSgBNKgvZi4OKlL5KqEjX-ZsmC814mowr_Io7AjR_kRNRaLeWBa7aa5ve48FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک آسیب‌پذیری بسیار خطرناک در هسته لینوکس با نام Copy Fail (CVE-2026-31431) شناسایی شده، که به کاربر عادی (حتی بدون دسترسی sudo) اجازه میده تا کد مخرب رو مستقیماً در حافظه (RAM) فایل‌های سیستمی تزریق کنه، بدون اینکه تغییری روی دیسک ثبت بشه؛ به همین دلیل بسیاری از ابزارهای امنیتی قادر به شناسایی اون نیستن.
این حمله به سادگی و با پایداری بالا اجرا میشه، میتونه برای فرار از کانتینرها (Docker / Kubernetes) استفاده بشه و تقریباً تمام نسخه‌های لینوکس از سال ۲۰۱۷ به بعد (Kernel 4.14+) رو تحت تأثیر قرار میده.
اگرچه با توجه به وضعیت فعلی اینترنت در ایران بروزرسانی کار دشواری هست، اما توصیه میشه در سریعترین زمان ممکن سیستم خودتون بروزرسانی کرده و وصله‌های امنیتی هسته رو نصب کنین.
©
Bamdad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2277" target="_blank">📅 17:02 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2276">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DaTQ4yoxl3cfEr-Opk3J33WPjV5Zj2Kuyq8s0Ooo2M8mJOFxXYgMv-Np2-G_u7HsnvG1gD4E_KUMZQBYGl5y0dTT8ULdSiYVKXnL6p33SYSedYuOCeZaVOpuAMnBl2wwfTlR6UOf-fwLXInEEGc9HZUK__w6B3E5rpdf9fyGneGKk7kM3tj9uM9Q1SAZ72Dya39y1jMfEvYwOVTSkRsJ-52wsQCSHrgjL9vL-UAaGyPM5cUgIa_GGIAUilE9ezA92fNjdKTdJD_47qvhwHCD0yDn-DIb2L7M6OSz5vX5WKJ6mRLSyPXoHgkzwOOY9RzuXr6mIcIB3hFmeTqthN9ehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل آموزش ساخت فیلترشکن شخصی به کمک گوگل و کلودفلر از طریق متد MHR-CFW منتشر شد. اخیرا یک کاربر فورک جدیدی از این پروژه رو به زبان GO بازنویسی کرده که مشکل سرعت پایین، لود نشدن برخی از ویدئوهای یوتیوب و همینطور یکسری از خطاهارو برطرف کرده.
👉
github.com/ThisIsDara/mhr-cfw-go
💡
t.me/ircfspace/2259
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2276" target="_blank">📅 16:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2275">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">توی خبرها دیدم که دستیار ویژه وزیر کشور گفته "محدودیت‌های اینترنت احتمالا تا ۴۵ روز دیگه رفع میشن"؛ بنابراین بنظر میرسه باید خودمون رو برای کابوس ۱۱۰ روز قطع اینترنت آماده کنیم!
😐
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2275" target="_blank">📅 16:42 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2274">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8ox8D15vIrJhEqMo4Y3TyCiK3aBxCzKn6tC6lzf_oqGKjtK8_jzFAFLkV6pkraD1VBPPL3V-bE_mrsSG63nswQXChPTBjhHxuEYswKoyKkYvWDiqehSIomgmwyH9hKMbqWu2ylubv_94QEBX0-aARATRZaCM9wbHausRbYad71C7sz1YHjvcHwvjw3ULIMqipGj2mbA8zLZBU6xQBVO9sgc2oHpgdIjbplsBXc-AKhWrdLy5hASUCj-PApueM6aq9OVmgmB5t6Ni0aYH1am9koo874l5VPqsrNlWmIRgacp8LKZ30pxU8x4SANTaQMs9sI6J2M-3jwiD_U3NJH39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز خبری در رابطه با قطع اینترنت سفید خبرنگاران توسط ایرانسل منتشر شد، که روابط عمومی این اپراتور گفته نقشی در این ماجرا نداشته و "هرگونه قطع احتمالی دسترسی متفاوت برخی کاربران به اینترنت، لازم است از نهادهای تصمیم‌گیر پیگیری شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2274" target="_blank">📅 16:38 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2273">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/juEKtk1ntugqDxwJbTpv_XILZ0joXu528g9OfRWiLg9jDDXE9qjhZIEOBscAZI5XoU7V-FPo1jTPs65fwgOhoLBgqC0pmoD5vP2nhsYHfAOBMcVI-93XuMGmMv-ZTrf9pEVBUCs3J6VuvOTr1hVPzNRvLXdtvDxRjweCvXMNt_JkteNa7BOsLx_1LAz2iyoQ62sC0UiQimpcty5hApHWN7p8Ktcppj3ngb0GWTTZcOzlaATtRBRGqDU16z7A6q3RFdyWSpZ8Q-ua8FhJpgI6Gii3GbfPGqi2eUWdvsVGy_kKF6DjAp5bhr9wRAwukLW_3dQeTUxckljDK0EIxj3GrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع اینترنت در ایران اکنون وارد روز ۶۷م شده است. اقدام به سانسور دیجیتال، پرده‌ای از سکوت بر افزایش گزارش‌ها از اعدام‌ها می‌افکند و قربانیان را از دیده‌شدن، پاسخ‌گویی و حق ابتدایی شنیده‌شدن محروم می‌کند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2273" target="_blank">📅 12:26 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2272">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">توسعه‌دهنده اپ SlipNet متاسفانه از توقف توسعه این اپ کاربردی خبر داده و در بخشی از توضیحاتش در مورد علت این تصمیم، نوشته که "توسعه ابزار آزاد، رایگان است اما بی‌هزینه نیست. متأسفانه در جامعه نرم‌افزاری ما، فرهنگ Donation هنوز جایگاه خود را پیدا نکرده است. از سوی دیگر، جنگیدن همزمان در دو جبهه (فیلترینگ از یک سو و خشم و کامنت‌های تند برخی کاربران در روزهای اختلال شبکه از سوی دیگر) توان ادامه مسیر را از من سلب کرد".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2272" target="_blank">📅 12:22 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2271">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کاربران میگن ابلاغیه‌های مشابهی رو از قوه قضائیه با موضوع "پرداخت وجه و تسویه اقساط"
دریافت کردن
، که توسط "نوآوران پرداخت مجازی ایرانیان"، یعنی نام تجاری دیجی‌پی (زیرمجموعه دیجی‌کالا) ارسال شده.
با توجه به اینکه ثبت اظهارنامه آنلاین از طریق سامانه عدل‌ایران امکان پذیره، احتمالا تعداد نفراتی که پیام‌های مشابهی گرفتن اندک نباشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2271" target="_blank">📅 22:24 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2269">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vZIE0ASNLBAeNI6eAGsjj0H_4UOe2uYigN6H7uSH0YQK7oQYQW4bCpUZuW2n03ZaTmHwURDGdus_lcRxTdksHDrk-CVjaFxeRfU6Mp3hQg3UnHDDuPJ3mHiOa1_N0EoKh2AKpt4J--FnEuz1IQpMc1yiy6jLlhux9X3_cLg_TWN6LgT_YvjRgzGs210xPDtO7kpCzaS8PyPJUIXbJgrHzQt965S-UA-BLQvCupNXHB2LjRr_om6iaWG6hcgUrZZHJiQxJ87kIT5RpUyP5kQ_dCXkpYJW5OM_gDY9p_jLPbxIStCvW-zaO7WLtxjNMM3SPXNjHahUfIoj2S-ycSlL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که امروز در مورد "ثبت رکورد ژاپن در رابطه با سرعت اینترنت" در صفحات مختلف منتشر شده، مربوط به حدود ۹ ماه قبل هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2269" target="_blank">📅 22:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2268">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E0GVEHrfglW_SYH767Zh5MkUex6A6dDP4co1BuprZwGDrdntUDqqMH3Wv83UyMpI9bzhG2JQgm0SEwVzGxVTPpvkBCLyqX8fl4QuZqCzuX49khnt5Wxo3GlHbdLOymYI60U6SiuEyTbOOw75y-GjLPmlLTLf5QdT-x_BmIZ4WEyndlQbJ6Gk4JQZq2NSreKOl0SIdSeNygKqR_gbL_6lGu3jVK-fuCZZnudtF-0UzVJgMbuqz2tX0TTWWd0GEV3eBy4dPn-EdkOHVgAHytcNRS9nHb0y0M7TLi-cjowS4lvapBrweImZpOWcNza6rHP0sBc0OmleQ-kkgSt5-K29IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیجی‌کالا خیلی اوقات در رابطه با خسارت‌هایی که بصورت مستقیم و غیرمستقیم به مشتریان و تامین‌کنندگان وارد میکنه پاسخگو نیست، اما در شرایط جنگی از طرف سرویس دیجی‌پی بخاطر ۲۰ روز تاخیر در پرداخت قسط اظهارنامه قضائی میفرسته؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2268" target="_blank">📅 21:57 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2267">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p7zwHzpEI84A9Nuw75Q5PT3yZq3GLlZEpC42Wc6zZ3sHlKqSisgY9aKQ1_oTNCglbbrpR3EkbpRkVLdmDQmWwmODSV_qQnSL8IH7JPYHQJ8crBuscleon_ETpySpQKdobn4lrLYLZ3qrcQo_HIo_vKPS1aMSRAEts9NohkMxybNRtubOAlO-Y1O9BMjBEwZNG9Aj63Q5UvdPz-YFFZHQeMPIvWnf27h3ISgruCALaQo4TqI7YLVdgZOui9Fbgbz6e-KtfK1SkZ7BgRhzcaDad6plUwWlzP7BAxCegrMmtmBkH4K7T6IPGQcCqUOv6QSvqTa6WC_PNBAP-g08_RVnCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ TeleMirror یه تلاش آزمایشی برای دریافت آخرین مطالب کانال تلگرام خودم و سایر کانال‌های موردنظر در شرایط محدودیت شدید اینترنته، که سعی می‌کنه با چند روش مختلف پست‌ها رو بگیره و نمایش بده.
این برنامه رایگان و متن‌بازه و فعلا می‌تونه برای دنبال کردن اخبار تلگرامی بدون نیاز به فیلترشکن، یه گزینه موقت و کاربردی واسه دسکتاپ باشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4128
۱. این برنامه رو برای کانال خودم نوشتم که در لیست بصورت دیفالت وجود داره، ولی هرکی میتونه سایر کانال‌های موردنظرش رو وارد کنه
۲. برای اینکه ریت‌لیمیت نخورین پست‌هارو برای مدت کوتاهی کش میکنه، که با هربار مراجعه یک درخواست به سمت تلگرام ارسال نشه
۳. به وایت‌لیست فعلی اینترنت متکی هست و فیلترشکن نیست. ممکنه روی بعضی از اپراتورها جواب نده، یا خیلی زود از کار بندازنش
۴. برنامه دیتارو از کانال‌های پابلیک میگیره و به هیچ اطلاعات شخصی‌ای واسه تلگرام نیاز نداره
۵. در حال حاضر نسخه ویندوزش رو منتشر کردم، اما اگر بازخوردها مثبت باشه برای مک و لینوکس هم ارائه میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2267" target="_blank">📅 19:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2266">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">در شصت و ششمین روز از قطع سراسری اینترنت هستیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2266" target="_blank">📅 08:59 · 14 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

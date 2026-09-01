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
<img src="https://cdn4.telesco.pe/file/j_MuSm4VCHnWYJY9oh6ywNqTDEVTm1ZuWZRuM19vddntOUWwPSv48URmqGAMyA7xCzrHIdaIPx_WtKqLxKn8kHnZWg1mthim-TxL-Ipwn4zBjTzsDFp1ZI3OLyW9b8rtuIdJGQHBQMqFQRehbOs9amQu1slc6rWZyUyIwJEzYbRCHPHZsknk_hcSIXlBNqnDV_XD0KlhTWhsGs6adA6V7GuPVfTkZvGDs8xQwNeLG29jJHVxxD5ZHtTByHGvNkn85dmVKcW5UXv3NfiOJe1IwCzVrPhRCbWqZPi7hhY-lPki1fHzn5V-xcy6N-YEmDYaU3Z0kU3IKTz1LXCMG2OSjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 01:22:27</div>
<hr>

<div class="tg-post" id="msg-686404">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73625973f.mp4?token=KH5mqnvR_v0hbKdqZTntYa6lw50qx7rYZTgMMA54940E-DvCT3AWVL43sCdmCoJipM1ERd3a8BZC5gdWij0jykIFNZIjKoCcjXooyAH-s7ju39HivJ3KHqvx99ABIAsxymnwYhdYp5GUj1cm1clZo7qz1W881cD3UYhGh_IiKPshtD6NK41j8yhL-Fh6WcT5Qu6ZNVH91VRpWBxuRSRE0yRm30oq0GPy20HUVjE2kn6DqhRvJpHR6l3s7SHaoyfjh_GVwb1wBITB6hZ8lDlIf2_MXygNl9Gg2z2vIJFpKalY-MpZF7V3125Lg22APfbL_gsJ6LNED7J0GHK5DE9W9xoQzmh9xfIq7TTS790GR2Ix0czZBWBReW0IpU5us4NEbum3MReIgJtNfreex9MHfuswaDyrLb3j05VQGvWnyyvlq2P4ZSauFjBTFaJEzdy6rRHrzjc1bAUZH3gntXOgqNkZMciGVWmchXUKSsG_ywzx1g4nBuRjEWfUpNwOqtIa6btlGIVm32MSJab2iQJ79TvevZKmPXePsWqYy0wNVWoS4DsF80Fn4nXAsDhNLyTUcnS1xjX6D1JKXbD6YXGF3LiF_wVF1XnudmfO6f8aW7cYji6YlOzQF434Z6M3-feIT09z0kf9r2xVkrxtal327GOdvOE_wYRwRZ9CCLvw8kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73625973f.mp4?token=KH5mqnvR_v0hbKdqZTntYa6lw50qx7rYZTgMMA54940E-DvCT3AWVL43sCdmCoJipM1ERd3a8BZC5gdWij0jykIFNZIjKoCcjXooyAH-s7ju39HivJ3KHqvx99ABIAsxymnwYhdYp5GUj1cm1clZo7qz1W881cD3UYhGh_IiKPshtD6NK41j8yhL-Fh6WcT5Qu6ZNVH91VRpWBxuRSRE0yRm30oq0GPy20HUVjE2kn6DqhRvJpHR6l3s7SHaoyfjh_GVwb1wBITB6hZ8lDlIf2_MXygNl9Gg2z2vIJFpKalY-MpZF7V3125Lg22APfbL_gsJ6LNED7J0GHK5DE9W9xoQzmh9xfIq7TTS790GR2Ix0czZBWBReW0IpU5us4NEbum3MReIgJtNfreex9MHfuswaDyrLb3j05VQGvWnyyvlq2P4ZSauFjBTFaJEzdy6rRHrzjc1bAUZH3gntXOgqNkZMciGVWmchXUKSsG_ywzx1g4nBuRjEWfUpNwOqtIa6btlGIVm32MSJab2iQJ79TvevZKmPXePsWqYy0wNVWoS4DsF80Fn4nXAsDhNLyTUcnS1xjX6D1JKXbD6YXGF3LiF_wVF1XnudmfO6f8aW7cYji6YlOzQF434Z6M3-feIT09z0kf9r2xVkrxtal327GOdvOE_wYRwRZ9CCLvw8kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادثه مشهد صرفا ترافیکی بوده است
روایت «سرهنگ موسی آبادی» رئیس پلیس راهور خراسان رضوی از حادثه امشب
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/686404" target="_blank">📅 01:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
وزارت خارجه یمن: حملات ایران، مشروع است، کشورهایی که پایگاه‌‌های آمریکا را میزبانی می‌کنند باید بهای آن را بپردازند
🔹
وزارت امور خارجه یمن اعلام کرد که تداوم تجاوز آمریکا علیه جمهوری اسلامی ایران، اراده و ایستادگی این کشور را تضعیف نخواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/akhbarefori/686403" target="_blank">📅 01:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
استاندار خراسان رضوی دستور پیگیری به حادثه بلوار وکیل‌آباد را صادر کرد
🔹
بنابر اعلام پلیس راهنمایی رانندگی مشهد، ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و افزون…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/686402" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9f02e16a.mp4?token=s9CJvsslTKdksADsONhsQGzh_7Lx80VWKueKc19kVIvmPoUviABtYR4S940M-c8FPJ-4wGFwPrFgv0k9axSC77AkQ-P38kd9j2HBb02U46s9Bv82vXy91Zn21TblvzEeRMMSn-0d05IslDazFMzdmhEBQadJWEetBzIwgw1SC9Kv-GiyfiuVOTWwxHdI2aVu_PWNwUOGVGILBs_n3yY4lGW-tDjBbdqTYmBLAXTTmbojTsSYUfbO43E_FJ7UmeLQYuBoURZgN2RwXKK66-0w0jXrnNDLnvTBGts2wRMMpA-xGaiF18o_7WBj0JgmWuULEJY7IpQQDtkz7Hv5jpX0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9f02e16a.mp4?token=s9CJvsslTKdksADsONhsQGzh_7Lx80VWKueKc19kVIvmPoUviABtYR4S940M-c8FPJ-4wGFwPrFgv0k9axSC77AkQ-P38kd9j2HBb02U46s9Bv82vXy91Zn21TblvzEeRMMSn-0d05IslDazFMzdmhEBQadJWEetBzIwgw1SC9Kv-GiyfiuVOTWwxHdI2aVu_PWNwUOGVGILBs_n3yY4lGW-tDjBbdqTYmBLAXTTmbojTsSYUfbO43E_FJ7UmeLQYuBoURZgN2RwXKK66-0w0jXrnNDLnvTBGts2wRMMpA-xGaiF18o_7WBj0JgmWuULEJY7IpQQDtkz7Hv5jpX0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برق مناطق آسیب‌دیده قشم پس از حملات دشمن متجاوز آمریکایی در شامگاه سه‌شنبه پایدار شد
🔹
فرماندار شهرستان قشم از رفع قطعی برق در مناطقی از این شهرستان که در پی حملات شامگاه سه‌شنبه آمریکا دچار خاموشی شده بود: جریان برق اکنون در تمامی نقاط قشم برقرار و پایدار…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/686401" target="_blank">📅 01:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نیروهای مسلح اردن: شلیک ۱۳ موشک بالستیک به سمت اردن/انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/686400" target="_blank">📅 00:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
حمله دشمن به برخی زیرساخت‌های تلفن و اینترنت در بخش‌هایی از هرمزگان
اداره‌کل مخابرات استان هرمزگان:
🔹
در جریان حملات آمریکا به مناطق غیرنظامی و زیرساخت‌های خدماتی در بخش‌هایی از مناطق جنوبی کشور از جمله کوهستک در سیریک، به تعدادی از دکل‌ها و سایت‌های مخابراتی و اینترنتی هم خسارات جدی وارد شد. حملاتی که موجب قطع شبکه ارتباطی تلفن ثابت و همراه و همچنین اینترنت در بخش‌هایی از این محدوده شده است.
🔹
در همین راستا و علیرغم تداوم حملات دشمن، عملیات تیم‌های اضطراری برای رفع مشکلات پیش آمده و وصل مجدد شبکه مخابرات و اینترنت درحال انجام است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/686399" target="_blank">📅 00:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شایعۀ حمله به کرمانشاه تکذیب شد
🔹
معاون استانداری کرمانشاه با رد شایعات مطرح‌شده؛ هیچ نقطه‌ای از استان کرمانشاه مورد اصابت دشمن قرار نگرفته و وضعیت در استان کاملاً عادی و تحت کنترل است.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/686398" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سپاه امشب کدام پایگاه آمریکا را هدف قرار داد؟
🔹
سپاه در موج دوم عملیات «یا رسول‌الله(ص)» کمپ تیتین آمریکا در اردن را با موشک‌های بالستیک هدف قرار داد؛ مقری راهبردی در نزدیکی عقبه که محل استقرار و اعزام سریع تفنگداران دریایی آمریکاست.
🔹
اهمیت حمله در این است که آمریکا پس از اختلال مسیر هرمز بخشی از نیروهایش را به این نقطه منتقل کرده بود؛ حمله سپاه، نمایش اشراف اطلاعاتی و توان هدف‌گیری این جابه‌جایی بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/686397" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686396">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMSs3L92GFfOAreGgUqnwvRMEh3jyXY5l3SXKWOzBxcnxWEW1Z_HcMr7gO5C_HIeZ1uv-DKAC-RIyKqJ-Jq20XdoDUC19DnO5l3iiXc-kxTFOd0gQ27EbkvsPC2rDLJU6gkJvbWU5sOd4QWV-P_fvtnemc8FxaEEwxDoAcnvK6-Iabq-6nYQNRO2RksTs9hFtHkQk-jEXCXFCURj6C2VXhwsY0uCqpvwfCY0t2JnKqPtAy1wbwQd_VQId5Y6KNH8zQzQQjt71DEi8QXGdsgQuTnLJE1X8USP_iaC37GZEnOPkYTvZraVzGVvXLrnNoicU9M96Plxxbm017UIldRqFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدئویی از مصدومان حمله ساعتی قبل آمریکا به یک مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/686396" target="_blank">📅 00:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
چند نقطه از شبکه برق هرمزگان هدف حملات دشمن قرار گرفت؛ خاموشی تا کم‌تر از یک ساعت رفع می‌شود  مدیرعامل شرکت توانیر:
🔹
در ساعات گذشته، چند نقطه از شبکه برق در مناطقی از استان هرمزگان مورد اصابت دشمن قرار گرفته است.
🔹
در جزیره قشم و سیریک به علت اصابت و تخریب،…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/686395" target="_blank">📅 00:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
استاندار خراسان رضوی دستور پیگیری به حادثه بلوار وکیل‌آباد را صادر کرد
🔹
بنابر اعلام پلیس راهنمایی رانندگی مشهد، ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و افزون بر ۱۰ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/686394" target="_blank">📅 00:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686391">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/face74d2d6.mp4?token=aRRpaqqtJ6WS_B6nuDWuE69XX0fHiOUZ-83Bhssntw6IZHA_woZM-7BWyJShYjLXklnzUCGR71G0TljV5HPPsnGo7sy9ziyDcVWSxZtzQFl5OIi0Rrek1OXL-KcKbKEpSdneEH7yenr3UJvB6p3yE_e4qOm2Hhfpm37L25zmfQgTrApmLBhv9IBMMH91oOOnrE_eWT_fvUZul_PhrIi9nI9-v6klKelmFUgR_e6WW8r5VuLQ0Xd6xI4wK74btJP0ItMd8_qHnni3a06C9ChSdLgWCh7d5ow1o2fi_Paj4Ofaxb0ee6R4pHDPZi8_L6YtEPA6AfqojFPSxQcwXpILYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/face74d2d6.mp4?token=aRRpaqqtJ6WS_B6nuDWuE69XX0fHiOUZ-83Bhssntw6IZHA_woZM-7BWyJShYjLXklnzUCGR71G0TljV5HPPsnGo7sy9ziyDcVWSxZtzQFl5OIi0Rrek1OXL-KcKbKEpSdneEH7yenr3UJvB6p3yE_e4qOm2Hhfpm37L25zmfQgTrApmLBhv9IBMMH91oOOnrE_eWT_fvUZul_PhrIi9nI9-v6klKelmFUgR_e6WW8r5VuLQ0Xd6xI4wK74btJP0ItMd8_qHnni3a06C9ChSdLgWCh7d5ow1o2fi_Paj4Ofaxb0ee6R4pHDPZi8_L6YtEPA6AfqojFPSxQcwXpILYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی پیش یک خودرو به تجمعات مردمی در اقبال لاهوری مشهد برخورد کرد و تعداد زیادی از مردم را زیر گرفت
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3242100</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686391" target="_blank">📅 00:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686390">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17d416a8f.mov?token=dATTF6_pd0eEqDIEhK-QmdJUtylKWhBibxziTOjEHClZHAVdLNDgzNNmPYjp2UU_iSrNyw0rdA6GhdKcWCOkmyfBn2vJfzdlkG6IlHG8Go_bwwkYGIg-7fhQq4YD8fWNbW164p3qtKmItgi2seM4fimlQxFojWgxWV198eRwZlgp1vatYCo5y4UnNIK9pJddZwJQvWyi5egxdy1myJ2GeMI8nCbOVf3A2GyjxfAtyBwgpljWmSOMX6IUwjIPeDdefJWLzgxO-P3plKaXLS-xqWAGt4uhHqZP5vTBCpQjBwe9xMISFJbC3NKPjMzMXJK16p9fv92RsPrL0r15AVlpMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17d416a8f.mov?token=dATTF6_pd0eEqDIEhK-QmdJUtylKWhBibxziTOjEHClZHAVdLNDgzNNmPYjp2UU_iSrNyw0rdA6GhdKcWCOkmyfBn2vJfzdlkG6IlHG8Go_bwwkYGIg-7fhQq4YD8fWNbW164p3qtKmItgi2seM4fimlQxFojWgxWV198eRwZlgp1vatYCo5y4UnNIK9pJddZwJQvWyi5egxdy1myJ2GeMI8nCbOVf3A2GyjxfAtyBwgpljWmSOMX6IUwjIPeDdefJWLzgxO-P3plKaXLS-xqWAGt4uhHqZP5vTBCpQjBwe9xMISFJbC3NKPjMzMXJK16p9fv92RsPrL0r15AVlpMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از مصدومان حمله ساعتی قبل آمریکا به یک مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/686390" target="_blank">📅 00:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686388">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNAjOfHsQC7HHjdLxEuFmFyl5vQpp6H2Vmxt86EREdp65oEsybhEpCCAvzWONgPzVts7Fp4O-1wNKsn2dzgpzqhEmJu2PxGjvt9SyLZRCpU91w_11M7aWmd5-oduEz04hX7kfVHsi93UlxNJ2OXbEwBkBTn74XRZL0qdcFhtkuSJTt_TAzGaStHsHaYhN34_-zcuzk3S0pFJVURyE8s7Nq3kVy6CpAcNomqRzJDShQKPjAh0CULPjvUBf1pYcaVBEC15iKCV6uZn9NcULgD-vpYEwCFAMrvnYFFSQm4UlFotiMWacQSyit-cpo1Swhp_UwYkIn7OUqMUytR7Wscb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف پروازها از فرودگاه نجف به ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/686388" target="_blank">📅 00:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686387">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e95424e8.mp4?token=vSfaKWvyBK0P-DkvlAqLzJ377qIX4AYU826Leif5xoAn_5J-yNAEREV1dXRyQvfAb_HZvkjpcVHWoxNqiDcDwjXqd-89AecXczdJ6zAHSTYcSR-2B3Va7ugTjIqUCyfFo8rNVemZZnw80Djz6A8P58QOXVvNcxGBpQ9hmy0O4r_A6P96SCDjMRZAAywKv-KhQAybSRiymVKFkZrRek-jvKd1_8bQHJtyIBENgQGX2zlYR_FZM3JsVW-QOa0gNUIG-WghCjKoq9QNcgYIa6b4IrxWYosNTkIoXUyPDi7Q96kE2lgrTOpatHcf0G3TxD3g3Y7_-rQqmewyF-HoPNtJRSGLIpj_fmYfaNA-USljHwWzhXpjhvFz4xCkA-2pLrI0f49SQkyyceaQmoPZJo2-23AuERTyFhIlEWSwHnzh9PwCOD47qvpIvLfgaWcuEQ1dT0A62Oyx9q-kNM-f0NAyb2KJDkP11OhiBjZ1pAsyWaOni6_IYJUcOt5zwAZtNcPIGeFSjZh9qXdgbmPC6q8LPwKm3sI9Bh2fmGgRgp1h-YPRBGcsUSupQWN-L0c66JOK2ITucDJdHMo1RcGPWSTuHy2I5BeHk-WQXtGmCgMl-D33qH6MIVYJAdQ63-gs8CUz4-zxkfXb5kjUuUDLD17JTfv7j0eB0ZIm1U7xg4p2sOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e95424e8.mp4?token=vSfaKWvyBK0P-DkvlAqLzJ377qIX4AYU826Leif5xoAn_5J-yNAEREV1dXRyQvfAb_HZvkjpcVHWoxNqiDcDwjXqd-89AecXczdJ6zAHSTYcSR-2B3Va7ugTjIqUCyfFo8rNVemZZnw80Djz6A8P58QOXVvNcxGBpQ9hmy0O4r_A6P96SCDjMRZAAywKv-KhQAybSRiymVKFkZrRek-jvKd1_8bQHJtyIBENgQGX2zlYR_FZM3JsVW-QOa0gNUIG-WghCjKoq9QNcgYIa6b4IrxWYosNTkIoXUyPDi7Q96kE2lgrTOpatHcf0G3TxD3g3Y7_-rQqmewyF-HoPNtJRSGLIpj_fmYfaNA-USljHwWzhXpjhvFz4xCkA-2pLrI0f49SQkyyceaQmoPZJo2-23AuERTyFhIlEWSwHnzh9PwCOD47qvpIvLfgaWcuEQ1dT0A62Oyx9q-kNM-f0NAyb2KJDkP11OhiBjZ1pAsyWaOni6_IYJUcOt5zwAZtNcPIGeFSjZh9qXdgbmPC6q8LPwKm3sI9Bh2fmGgRgp1h-YPRBGcsUSupQWN-L0c66JOK2ITucDJdHMo1RcGPWSTuHy2I5BeHk-WQXtGmCgMl-D33qH6MIVYJAdQ63-gs8CUz4-zxkfXb5kjUuUDLD17JTfv7j0eB0ZIm1U7xg4p2sOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستور پوتین برای حمله به تأسیسات انرژی اوکراین
🔹
رئیس‌جمهور روسیه گفت که دستور حملات گسترده به زیرساخت‌های انرژی اوکراین، در واکنش به حملات این کشور را صادر کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/686387" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686386">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b044a65a7a.mp4?token=WXE5USiv1J8CRg89982rhXE8y1hOCks9S0F_f033Imsy9fYDuk6DVSdK405wpTkrX8LqfRQb3SZfEn28JXfeAscWWRLyfjZqmnHL48fNrdHOElGMat-LME0CovGrOhlJRGfDvhYQcrVTWtxFxHkSkv4Vn7TAAs_j8U-bgwo70n84_ebGdZq_lULD7YQXdLqK2tqx2IotTq_P-XSxCnfm9FswMq_EtATXPJs0fQGNnJ9aRKegeCBYwotLhwFru8w1z_KFeaN5u_2oOqqEKVYIVkDNN5usUmTcPfcOIJXCinHemVXiTYagI92YVw97otzfy6fWTXJ6g5nT2xVPJnyPcg1l9Kx_LhVuSGJME88jG9QK1C6Uyy-qsmfUdrqnZ1wORRCsdx1zmEpeM3GivB3T1613viPA7KpoZzUN-_VAJIBZgjCM-bUo2VF6jo6xMluksJCNR70zalq21lhy6VQfVOGdKbCjoBq-MAyPkNSrFZaDuQ3eCT-J0ldnEfFvWT8FHfx2hfz_LdOW1_u017RtMRGqbZxQ6AUwHaDp2P3YBMnbL0lgVKWgTJ4P7-JaLbtp6wY5nsQXG2_z9yCp0kUp1r_m4knwc3e1QmHJjZ1OrvblFpSUVqJ35YgFFBbleZ51wiNCrvwMSwWHFF3tGKoCnCHmQCctcBcnxSwQ0R9PwkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b044a65a7a.mp4?token=WXE5USiv1J8CRg89982rhXE8y1hOCks9S0F_f033Imsy9fYDuk6DVSdK405wpTkrX8LqfRQb3SZfEn28JXfeAscWWRLyfjZqmnHL48fNrdHOElGMat-LME0CovGrOhlJRGfDvhYQcrVTWtxFxHkSkv4Vn7TAAs_j8U-bgwo70n84_ebGdZq_lULD7YQXdLqK2tqx2IotTq_P-XSxCnfm9FswMq_EtATXPJs0fQGNnJ9aRKegeCBYwotLhwFru8w1z_KFeaN5u_2oOqqEKVYIVkDNN5usUmTcPfcOIJXCinHemVXiTYagI92YVw97otzfy6fWTXJ6g5nT2xVPJnyPcg1l9Kx_LhVuSGJME88jG9QK1C6Uyy-qsmfUdrqnZ1wORRCsdx1zmEpeM3GivB3T1613viPA7KpoZzUN-_VAJIBZgjCM-bUo2VF6jo6xMluksJCNR70zalq21lhy6VQfVOGdKbCjoBq-MAyPkNSrFZaDuQ3eCT-J0ldnEfFvWT8FHfx2hfz_LdOW1_u017RtMRGqbZxQ6AUwHaDp2P3YBMnbL0lgVKWgTJ4P7-JaLbtp6wY5nsQXG2_z9yCp0kUp1r_m4knwc3e1QmHJjZ1OrvblFpSUVqJ35YgFFBbleZ51wiNCrvwMSwWHFF3tGKoCnCHmQCctcBcnxSwQ0R9PwkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حملات گسترده موشکی به اهداف آمریکایی در اردن در موج دوم عملیات تنبیه متجاوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686386" target="_blank">📅 00:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686385">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c02b3ddf9.mp4?token=Y_LwUqIwMw-M9fmPdHaQxRdwS0EbNtCUA9hXkhXId9RKFvU5szkxWo2toFbI4ElwYLcQwa2epNDe_3MU02-mj-x6g9pFY-FqRykz0XlF8T3jn630MO-VpRwK4OoGeeRpMrHjFi2F_S4MAXK849ObIfPwSBdcn3mRuWQRCRri4atYGUtNXCXVGCJ2pqbIMwlh_PYr9XA8F29y_-m8p-rE_CfgX7vAZbjv3nq_eyyXTn93zN0BXyY6hLJdVXOi2IrI8OZOrru5Cf-bDxBmj5CNCPtmfw342T0sTUmXQp-7tJ5ZsSezLYVODE88PEFIT0eZXpVEQS8SPtZ-rceCXjmfbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c02b3ddf9.mp4?token=Y_LwUqIwMw-M9fmPdHaQxRdwS0EbNtCUA9hXkhXId9RKFvU5szkxWo2toFbI4ElwYLcQwa2epNDe_3MU02-mj-x6g9pFY-FqRykz0XlF8T3jn630MO-VpRwK4OoGeeRpMrHjFi2F_S4MAXK849ObIfPwSBdcn3mRuWQRCRri4atYGUtNXCXVGCJ2pqbIMwlh_PYr9XA8F29y_-m8p-rE_CfgX7vAZbjv3nq_eyyXTn93zN0BXyY6hLJdVXOi2IrI8OZOrru5Cf-bDxBmj5CNCPtmfw342T0sTUmXQp-7tJ5ZsSezLYVODE88PEFIT0eZXpVEQS8SPtZ-rceCXjmfbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دردناک از کودکان مجروح حمله موشکی امریکا به سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686385" target="_blank">📅 00:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686384">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تکذیب صدور نوتام برای بسته شدن فضای کشور
سخنگوی سازمان هواپیمایی کشوری:
🔹
نوتامی برای بسته شدن فضای کشور صادر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/686384" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686383">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت
؛
تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست خورده آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام با حمله وحشیانه به یک منزل مسکونی در سیریک، محل مجلس عقد دو جوان پاک را به خاک و خون کشیده و با به شهادت رساندن و مجروح کردن نزدیک به پنجاه نفر از مردم عزیزمان خاطره وحشیگری مدرسه میناب و ورزشگاه لامرد را زنده کرد.
🔹
رژیم کودک‌کش آمریکا در این حمله جنایتکارانه یک بار دیگر با به شهادت رساندن چندین نفر از جمله یک کودک، عمق کینه‌توزی و دشمنی خود با مردم ایران را آشکار کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/686383" target="_blank">📅 00:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686382">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4cb478ba.mp4?token=OXfRYmIvmaLu8fLRp2uuK0PXVV6Z_KGAv43Bka_ellDPXU8s_8r4TjH9mWrtMztIToQ55aOt7BQBnCM-6_eYZra7Wo_C0zlQZ8BpnMGo6-zod_PfeGN9Z39yURx67l8Rk7o_FBPDXOlLhapxAra8OpnxaDpPPO1VZeJ9kSpBvZ9WuGZeBIP2Qem9mHaQxLx01KgrUOGazXQCni1olsUfdSk47JkiSyb3KSjGGGbj_KzXnmvcG7_Dnz290KRUa2VVemlx5xIMiT2uesP-ZNNbXhRB46TJqYBHxXQl6IkoWUvxo5uxgIMkJLOf6-CCTuwXCpg_4_SFMFqBmwDSNf-uPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4cb478ba.mp4?token=OXfRYmIvmaLu8fLRp2uuK0PXVV6Z_KGAv43Bka_ellDPXU8s_8r4TjH9mWrtMztIToQ55aOt7BQBnCM-6_eYZra7Wo_C0zlQZ8BpnMGo6-zod_PfeGN9Z39yURx67l8Rk7o_FBPDXOlLhapxAra8OpnxaDpPPO1VZeJ9kSpBvZ9WuGZeBIP2Qem9mHaQxLx01KgrUOGazXQCni1olsUfdSk47JkiSyb3KSjGGGbj_KzXnmvcG7_Dnz290KRUa2VVemlx5xIMiT2uesP-ZNNbXhRB46TJqYBHxXQl6IkoWUvxo5uxgIMkJLOf6-CCTuwXCpg_4_SFMFqBmwDSNf-uPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت مستقیم موشک‌های ایرانی به اهداف خود در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/686382" target="_blank">📅 00:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686381">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
چند نقطه از شبکه برق هرمزگان هدف حملات دشمن قرار گرفت؛ خاموشی تا کم‌تر از یک ساعت رفع می‌شود
مدیرعامل شرکت توانیر:
🔹
در ساعات گذشته، چند نقطه از شبکه برق در مناطقی از استان هرمزگان مورد اصابت دشمن قرار گرفته است.
🔹
در جزیره قشم و سیریک به علت اصابت و تخریب، چند نقطه دچار قطعی برق شده‌اند و همکاران با تمام توان برای رفع خاموشی در حال کار هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/686381" target="_blank">📅 00:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686380">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
جلسه توجیهی فرمانده سنتکام برای اعضای کنگره درباره جنگ علیه ایران
🔹
وال‌استریت ژورنال خبر داد که فرمانده سنتکام برد کوپر صبح روز سه‌شنبه برخی از اعضای کمیته نیروهای مسلح مجلس نمایندگان را در جریان جزئیات مربوط به جنگ علیه ایران قرار داد.
🔹
نماینده ایالت آلاباما و رئیس کمیته نیروهای مسلح مایک راجرز با اشاره به محتوای این جلسه گفت که ارتش آمریکا «برنامه‌ای» دارد و او پیش‌بینی می‌کند که درگیری‌ها تشدید شود.
🔹
این جلسه توجیهی صبح روز سه‌شنبه به وقت آمریکا برگزار شده و تجاوزات علیه ایران در ظهر سه‌شنبه به وقت آمریکا آغاز شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/686380" target="_blank">📅 00:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686379">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
صدای شنیده‌شده در برخی مناطق ایلام مربوط به جدا شدن بوسترهای موشک‌های خودی است/مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/686379" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686377">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VlQPbHSoDqbO0Cu1hYMOfnYT3NXA1kU9irxbVulilNgCrGZJI8RtO6Fl2HFdSFi6386-jUTOqlbjNo_abSZONCqIvKL5fr88An-GiQr14WgLPgHkVjJ0TN5ErQ4BqdU7ooIbXgCbZgb7pkWKN3q8hzadlHrVWRARFcKFlMZg01g7x_frIUAcbWYjJ68ZugZ02ZqXVlvqxdFlJVmfV6wRjfzpq4jgrlXYVomMtOLarpfofiedATxGPWmm6AvwxierY444RlIjs14rrrfXWF5c4aI4aIqq24WNopRmRxw-ABr77Y-jJgUI0lnu09lo2Ya1GDLQUA8gWeEBlUjM7RsqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l72kKmi-1Uw8hDMks8VV3AUztVIMSvQghi23RT6LfjUROwO3Kn5VfZor8GQwXRgEM_BNf1WEjAFPmOnjzfyhLqp3N_Ol2wsStzq2OKWK48h7htNMt_V3Nzp0_9uhj7RjKUV2IMQl-n_X0WBI6bAWnEHWYtA4CPx15rFWl73NaFCMhktYd-YBBe8uK0BXAWleC69Ztczo6Hep3LC7PDQxBqxXh1FhTsqUoWzpEMisnZhnxAgBTm3yOSlDbIFsaNBv4nfaBcDZ0ZEvlpBkl8BkaqpOhP3B92WCdSCEPBk09nhYGdwI3YXIdd8N-aznUPp5RNU0SMJtADO2p5clPlH0fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرماندار عسلویه: اصابت به یک مقر نظامی در اطراف عسلویه خسارتی نداشت  فرماندار عسلویه:
🔹
اصابت در اطراف عسلویه به یک مقر نظامی بوده است و خوشبختانه این حادثه خسارتی در پی نداشته و گزارشی از خسارت دریافت نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/686377" target="_blank">📅 00:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686376">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSTW_7JHVVr-O1jtjHKuJUG9D7RQFxuCGWE6-PnWkUP99fQZ8nI8JmE9uphWerKSLjj40P4boBS6ptUq325NeZfpzNddS3PSn5WYIabr2TZQKzGbDwM_ibLXwfKqKh4AptPY8csbCRkFp9KS1lMjc-9aWGsJONVh20Ri-YNch4jQYe4UAbFo03jcKl13HEmo52UlN-koFs55G48KiOlZNLMLVVDMFNvtMg1Q6dMWJG5lNKUseypbBLEfMcrsD-MDazrB98qX5nHrvM2_C5R9UsRf-YzIRn7rqGUUO5tIJmIb9AIf0kxYoYg8HJyXoBNm_n9STHgZirff6Ehukbe6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/686376" target="_blank">📅 00:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686375">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در عسلویه
🔹
فرماندار عسلویه از شنیده‌شدن صدای انفجار در این شهرستان خبر داد.  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686375" target="_blank">📅 23:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686374">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMxmAJG12D0FJIXNvIga8WGSB62lgLts2TgFIWbykdjILjHGQ9NJAoUuFDfE2xDuu2GC7kw4KawlxKh_5YkS9bA9vNj93TDjz1iIWzNhFyWKWTr1VQyFpLzHTiUUprs8m3zslxbCtfYfQ1wnq47eFZX6lsUlpdYxuVjL015yEsLD9LBCQ5rfE4Y1ZsjBRoQnW0i2_wZBjMYGG4CUsw5u0i1nm0v8_J3vN32I7OhebxpLriWD_otZU_DJOTerJlTgJP5oylD8SbVQK2f1mDL56BJd7FGSQa5CffYj1IhkoYvkxHzwqxB9dwd4IOi6F7dNlBDeb5UD_2YX_b3AmPA4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ارتش: بی تردید به زودی انتقام شرارت و تجاوز، از دشمن گرفته خواهد شد. سریع، کوبنده و گسترده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686374" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686373">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfgaiTgQ5-rmMIDhnHra2jEBZpHMoI0SWQxItmTRX0ROaKp1ZpO95bhThaXoKxy1-9fNczFa9R5G8mRFTn9fE095jwkulsbggvdiaC3qNi9MAFRKkcHdEJD8m3Inj7EvXQBL2DQH_LMe9DlAGQQU1-TWiOzg1aUPfveX2zv-JdeQj6QmAlSgpEni5vd1aGUp32BfSA94EIm57qGO_5WfB13wgN6l-qMw-JvCFaXvQeXI4Lc1j7-eztsqpe2cADCTOWr3_Au_wv7uiNwtjcltUKGHfRosFcTimmdo3VaDX3LRoz1voOA2e6Abh-uivo9ZWFThD7c8tBbvrWw1dFL8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری منتسب به اصابت موشک های ایرانی به پایگاه های آمریکایی در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/686373" target="_blank">📅 23:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686371">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ByyvdwuFY4AdzdVEYhc8IYGbiU04hKX5s726I3VnyiwjdJ9xvT1c-4yN_S-ZJz4aMA1NCl-7dq6D5ASm5evA_aRPahYK_8hgUiDbkHoxeq-kFcO3IqlXaR-Jf2MQ1UX_5mOJX9ziRtGXEM7aGuAAbED-LuHeM5So6y4jCd-cQFlR33KgwSf8Zg0RokK4OstukJ-rfS1X3kpwMq8ejklZVhqlQ9A24T_Digp4V8kzMTsslRZlmDFvs2uYgn7DUHsvwwUIyazcGPtlO0CJvfyxpwb20RgB3m5ny0CwJSYVthFWHmUj-DfoGLHjgQ0ChatC7PHomd1ZdICpTf7y-Rzqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqAVz0S7VigdNnHOcLZ2DRGHNRrd3KXilDiF355LOKS8I70h6m1UUzMots3EBHHFTULy0CZWQxLlakwIyPhDXDfLyPsuHYkH0ziHQJWTiftf8WJa-i6fvknbt2ohGghPSq_a5JJNEr_r0ZO38fNclW3ODcfRecZ_DTtTsuvhmt4prAjwxbM5FhVx8oFu8kyny2rzVrtdawYHOarHQhmrZO9jSarzzXX2-0zZsHPopvvYp9Yufh6dddvL7fo7wDMIlaQalqM7HSEQqieByv76kAfz-tWtaYwNAY_OLG-DHolzRdQNEykeMTMK3tKfW0M2jy6xXQ6-9whpt6yNINrT5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر تائید نشده از اصابت مستقیم موشک به هدف خود در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686371" target="_blank">📅 23:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686370">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
امشب یکی از گسترده‌ترین شلیک‌های موشکی ایران (به نسبت درگیری‌های اخیر) به سمت پایگاه‌ها و مناطق آمریکایی انجام شده است
🔹
ایران هشدار داده بود که حمله دشمن آمریکایی با پاسخ چند برابری مواجه می‌شود.
🔹
اهداف مهمی که امشب هدف قرار گرفتند متعاقباً به صورت رسمی اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686370" target="_blank">📅 23:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686368">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ed2d5287.mp4?token=BhoqH6m0eBgBy2ghIF7DsOUHo0zXI2EVqZ2RQtXoKpbPFfa3jId9dbicpygmfsWw52VfX_bhWORzcY8083qCUHRU85TMmVNlQzgUoaltDzl40_yoY1W4Pe7HteJtYagQvJEejepVo14G-HeLai1h62pWVNfpntUaMiJOv8tmpXr8OTP7tx9fC9jniEe5-G-XGvpmXfAL6QiiZSpbNUCdR-B-dWCwbeIYVREU9p3_Dwid1vt_P9Nb7e0xQ73VGhCmuxiCJnYkQI-kpvqmf3EIV5N2oTi24SmhKyA3r9XRaZ5wMLQ-nLfgecM5-8O-Wam7nX3y2q_0A4GC8ia-c_nw3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ed2d5287.mp4?token=BhoqH6m0eBgBy2ghIF7DsOUHo0zXI2EVqZ2RQtXoKpbPFfa3jId9dbicpygmfsWw52VfX_bhWORzcY8083qCUHRU85TMmVNlQzgUoaltDzl40_yoY1W4Pe7HteJtYagQvJEejepVo14G-HeLai1h62pWVNfpntUaMiJOv8tmpXr8OTP7tx9fC9jniEe5-G-XGvpmXfAL6QiiZSpbNUCdR-B-dWCwbeIYVREU9p3_Dwid1vt_P9Nb7e0xQ73VGhCmuxiCJnYkQI-kpvqmf3EIV5N2oTi24SmhKyA3r9XRaZ5wMLQ-nLfgecM5-8O-Wam7nX3y2q_0A4GC8ia-c_nw3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تائید نشده از اصابت مستقیم موشک به هدف خود در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686368" target="_blank">📅 23:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686367">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در ایلات
🔹
شبکه ۱۲ تلویزیون رژیم صهیونیستی گزارش داد که شهرک نشینان «ایلات» اشغالی صدای انفجارهای مهیبی را شنیده‌اند که به دنبال شلیک موشک از ایران به سمت اردن رخ داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686367" target="_blank">📅 23:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686366">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
تصاویری از محل عروسی در بندر کوهستک شهرستان سیریک که هدف حمله آمریکا قرار گرفت  صداوسیما:
🔹
در حمله ارتش آمریکا به مراسم عروسی در سیریک، ۲۸ نفر مجروح شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/686366" target="_blank">📅 23:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686365">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
فعالیت  پدافند در شرق تهران ـ دقایقی قبل
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3242065</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686365" target="_blank">📅 23:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686364">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
حمله آمریکا به شهرهای مختلف ایران
👇
khabarfoori.com/fa/tiny/news-3242065
🔹
شلیک موشک های ایرانی به سمت مواضع دشمن
👇
khabarfoori.com/fa/tiny/news-3242084
🔹
فرود هواپیمای غول پیکر روسی در بوشهر
👇
khabarfoori.com/fa/tiny/news-3241987
🔹
حجاب فرماندار نیویورک جنجالی شد | چرا او روسری به سر کرد؟ | عکس
👇
khabarfoori.com/fa/tiny/news-3241953
🔹
پیدا شدن جسد رزیدنت بیمارستان بهارلو دو روز بعد از فوت
👇
khabarfoori.com/fa/tiny/news-3241853
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/686364" target="_blank">📅 23:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686363">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
این منابع همچنین خبر دادند در حملات نیروهای مسلح کشورمان، پایگاه هوایی شاهزاده حسن اردن هم هدف قرار گرفته است
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3242084</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686363" target="_blank">📅 23:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686362">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7iTHZfFfCljwxQ-kausdRbHxdiWmgUOy0lAyosk3sIxOsyrRioO00gYKugGQLwxxAKxqjjHjGP1s53QRhCsC8iLCRTtkjVdFUlEMaxpUBJLoNDza0BD7Pe_Z1OzSjjJUDRs_1cW24WKpBBRu-7iwjjbnkSQGF05KHNbeSOtCvLXtBrOmx6wGv0tCZInH7MxE85O0PI-3shLc_3gWPPGnJDmH_cdW-R1VMIsx9XwniAiaWKvTj4eKHxvnrvkLX42poU8bPLf_3deFoj5zblaNcWEXE8UgR2wqAYIacMdMYitSrgEq4rcwMLiqrA16NpH3pX9czg3fFahMeB1LBKIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر معظم انقلاب: ملّت عزیز ایران و جبهه‌ی مقاومت، درسهای فراموش‌نشدنی برای دشمن امریکایی دارد ۲۶/تیر/۱۴۰۵
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/686362" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686361">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
پایگاه هوایی «موفق‌السلطی» در اردن هدف حمله موشکی قرار گرفت
🔹
گزارش‌های میدانی از وقوع حمله سنگین و اصابت موشک‌های بالستیک به پایگاه هوایی «موفق‌السلطی» در اردن حکایت دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686361" target="_blank">📅 23:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686358">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYBaTod2tcgyPx0UkZdlRumn2AMfQZe4MNad_Tsf24_cLasx6QTs2nQHM9_4Zto5d5B_Gbx267RtexhU192FRuZ7eWONuJDbwOORZREzVW7ctxDFXhwbSOZr5bda1EAcqmYjSM0wioRfi1Pvl3hxxyu5NCOCepGVWkp3tgTX-1yw0VYEYhvUuYuXFMgHf7QIybiWDX--SrX74GPKYagkS5Z-SNoQ0D148CKZmqe51Wzmh83Z9cUfN03lEwnOCBCHsV0uDFgb80mWm9Zz5jZSPQjvDwwQ2iWpRzkQ6Y__SbUZ0K8mSeXsh1gRKPPF8RlnIGpRraQjrIW_lsM4ovLmEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1Kw8haPLsfleqIuDTF6X5mdCgXvqp7gZF1AoGtrHcCNOBz83JOQEmxWJQftcZmcVgKPrxXMSCYN9x0GH-ks65hsmKeHV77hh0mCJR9v4WS6I9OxpkjaX8Vl2QM7GA2P46iWyssUL6Y8Mz_l3QShAz21lXKrikEE6CaRoX7AQMC0_gkNNTTwhJkgfFXpAIDJZH3fgSyp8DCVU3jLY3oIvUAw28uO39VJCDn0NqKK7FgtLSIiXgNW43mKl4TzOkm3DVeBD-BGcWUsAYbZWDJKkBEie6Tnfb9g-8rERPtdevK269JiMOxnYaVzLhhZ-BuYXGdavYgs4efRo-eNJY_Ntw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c089fa9b89.mp4?token=WP5kKPnDnlGujX3g2vNgvVjTsQGY0yHDP3Yb2zsXt6VURTOPPrT8kkovwokDowmI7JllvzFBTaSydQYRER_QTj6417z1frVFGB7xdjzc4fVA_CO1dMogqoU12ZpJ9GZxLWWgxn37sCgXOSbN_W9EcbNJutCBEFDHEd1LsiVgGRbj_LNgrdXJE_iQGatXu3kW71AQb5d1lXXjoHfunpg96_tdMId3SucDCG8-PnbFNTaAkmPtuVHbJGZVn8BAj1WUMZHV1fD2kYjjs-uBbVBQ8aW9SCN0qAPqkm0WXUP8JUIaeV846SwUPqk5NMMVjb00mPaC61sYhtD8SsSAMmOwJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c089fa9b89.mp4?token=WP5kKPnDnlGujX3g2vNgvVjTsQGY0yHDP3Yb2zsXt6VURTOPPrT8kkovwokDowmI7JllvzFBTaSydQYRER_QTj6417z1frVFGB7xdjzc4fVA_CO1dMogqoU12ZpJ9GZxLWWgxn37sCgXOSbN_W9EcbNJutCBEFDHEd1LsiVgGRbj_LNgrdXJE_iQGatXu3kW71AQb5d1lXXjoHfunpg96_tdMId3SucDCG8-PnbFNTaAkmPtuVHbJGZVn8BAj1WUMZHV1fD2kYjjs-uBbVBQ8aW9SCN0qAPqkm0WXUP8JUIaeV846SwUPqk5NMMVjb00mPaC61sYhtD8SsSAMmOwJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفیسی، معاون سیاسی و امنیتی استان هرمزگان: در حمله به یک مراسم عروسی در سیریک دو نفر شهید و تعدادی از افراد نیز مجروح شدند  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686358" target="_blank">📅 23:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686357">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
آمریکا مدعی توقیف بیش از ۵۶۰ هزار دلار کمک رمزارزی به حماس شد
دفتر امور عمومی وزارت دادگستری آمریکا:
🔹
در چارچوب تلاش‌های این وزارتخانه، بیش از ۵۶۰ هزار دلار کمک رمزارزی که مقصد آن حماس بود توقیف شد و پلتفرم‌ها و وب‌سایت‌های ارتباطی مورد استفاده برای جمع‌آوری کمک مالی و جذب نیرو مختل شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686357" target="_blank">📅 23:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686356">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-text">🔹️
می‌گویند دلار ۲۱۴ هزار تومان و نفت برنت ۹۵ دلار را رد کرد.
آمریکا به خستگی ما امید بسته چون برای خروج از جنگ نه طرحی در عرصه دیپلماسی دارد و نه نظامی، اما به تکرار ۱۸و۱۹دی و فروپاشی داخلی امیدوار است.
ترامپ جنگی فرسایشی را دنبال میکند که دلار را بالا بکشد و فشار معیشتی جای پرچم‌های خونخواهی و مقاومت ملّی را با پرچم‌های اعتراض و جنگ داخلی عوض کند. پاسخهای وسیع و شدید ایران هم معنای واضحی دارد؛ تنگه باز نمی‌شود و نفت و انرژی و اقتصاد جهانی روی خوش نخواهد دید.
ما زودتر خسته می‌شویم یا ذخائر نفت و گازوئیل آمریکا زودتر ته می‌کشد و اقتصاد رو به فروپاشی جهان آمریکا را زمین‌گیر می‌کند؟
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/686356" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686353">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s90mWyqdH2omJ5g1GIHImtpNb8YdZe-Vhe9aVnineIxO-vjTbZ4iCnbZV_CYlzNwjJt3vYQBU0h4FdeymY-2NWCZdjasZ01qCtWIFX4t7jblqo19O0W7Iq_S-7DPebYRO4AawXxxEt950_7pF2JtwSvNLehig_vGucJ_X2C8V_q98EyXdBIelPDFNTKqT3bx2a22h2Ua9hkQgFHTL8SvK2oGIMDhqUvBFlpVtL7TK8cSIKw0bZwUe-0DGh1Cs6k3rZ4MzyRScXX89b9QIjrQxfNd0-WYlzCwqJ-yYqk3-t_Xsgc-ND9l_pCfOnELsAb8jg-vCM9pdKvfVHC4xPFIjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUyeDs1yXKO0ht3yKAp0eo0ROe7J2MV-zyDrU_qIlvew1iE9kLh8swxNkbPXEU4xgpFmeAjA-KBVcq2fHuplA3CVefGLi5BnB6hWaVHh64wnfspe4aD24TjxCUk9QPVR-eUc8EulrAsbuHn_qfXxbjVS6Jg4HtB9Zf2kfn55S_bKOZ8KH8Y_Vic0KlhMqSEmPxsAoW59PNAZFxMH4WQv_TBEEaNSTeg-yQTz2ALADS_wHMbpm-2_zhxR53gGS6yj7e71JiYu2FU8fzI9XJByEXrZd2e4N04mfV9LCrUGl18vCSEcrgM7y3yoJ01KDVAv1PftkMnkOdP-lGS8z4pbSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2b06490f.mp4?token=IqergZcW9fggxh9om3_6TRF1DuAr1AYmrBc-1B-iFV3gcTk83vpW-CCM_A6jmNHiu0dDNC7hGxnVMBGhzjWCgiVpTZgZ3hp4AXUWJoV5ZT1W23jpaH-Zjp-mvDIPIW6wiYp8kGErqgi0VDC5gnaMMI-aAoQ5guo5WoDcc8FxGVHogNc8f_R8VtCc31Gqxo98ZezKyPFdnMDzm44cdkzX9RxLDVZ0D0XVXbqXwO5-hOV_JbMs2ANzW2GzVDeSorPzqxHaNQwvjeg7vG43E630U2xEHdZiIzO9Y0wsSbsoSmewlFfkwva3bsEczex3L_5v75jWBlinxr1NIW0-jkxzwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2b06490f.mp4?token=IqergZcW9fggxh9om3_6TRF1DuAr1AYmrBc-1B-iFV3gcTk83vpW-CCM_A6jmNHiu0dDNC7hGxnVMBGhzjWCgiVpTZgZ3hp4AXUWJoV5ZT1W23jpaH-Zjp-mvDIPIW6wiYp8kGErqgi0VDC5gnaMMI-aAoQ5guo5WoDcc8FxGVHogNc8f_R8VtCc31Gqxo98ZezKyPFdnMDzm44cdkzX9RxLDVZ0D0XVXbqXwO5-hOV_JbMs2ANzW2GzVDeSorPzqxHaNQwvjeg7vG43E630U2xEHdZiIzO9Y0wsSbsoSmewlFfkwva3bsEczex3L_5v75jWBlinxr1NIW0-jkxzwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک دسته های موشک از ایران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/686353" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686352">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پایگاه هوایی «موفق‌السلطی» در اردن هدف حمله موشکی قرار گرفت
🔹
گزارش‌های میدانی از وقوع حمله سنگین و اصابت موشک‌های بالستیک به پایگاه هوایی «موفق‌السلطی» در اردن حکایت دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/686352" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686351">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570698fa51.mp4?token=IpgU893m_BC0KfW6z322U0Ftwc-1qy7JYaeDl8PqakwNcDjr_stznnk80xyzlCOsNh2cni9hZSzLpXyP4Qfv8kRrE__tZT8PlewYYEiqNh0Zv7al73kS0QISJY_uub7HqKz3WOMBWh_qAQ0l0WA9c-R_bGS0U1Gbh-r3ddh8vYTwamUxH5MNvhCoHDodvVckgcsvsVY8OX87iGtSZXH95XLPhaHhzjcxFfnLnJ-whDAKmaFzI0o7aiLJUU0H_I8NhowgQwo7LLRaKC1QNn9Hj8gJyoe0bsEz9zRKxxLCKf5uW1JKjhHocuWV5vo_csEYYl1Hek3ac4nIhztjldM1Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570698fa51.mp4?token=IpgU893m_BC0KfW6z322U0Ftwc-1qy7JYaeDl8PqakwNcDjr_stznnk80xyzlCOsNh2cni9hZSzLpXyP4Qfv8kRrE__tZT8PlewYYEiqNh0Zv7al73kS0QISJY_uub7HqKz3WOMBWh_qAQ0l0WA9c-R_bGS0U1Gbh-r3ddh8vYTwamUxH5MNvhCoHDodvVckgcsvsVY8OX87iGtSZXH95XLPhaHhzjcxFfnLnJ-whDAKmaFzI0o7aiLJUU0H_I8NhowgQwo7LLRaKC1QNn9Hj8gJyoe0bsEz9zRKxxLCKf5uW1JKjhHocuWV5vo_csEYYl1Hek3ac4nIhztjldM1Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حرکت بدون مزاحمت ۲ موشک‌ ایرانی در آسمان اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/686351" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686350">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=a2PXNQi9mqCHOXhSqv2Ndm4Gb_Ski45V4lCAaFAElZtpaU2Rh_Nqyu9plz06kvTxNA8ZC28W15DqHqVy1bclmueyAsdqxCJGa1F9PUh5eIDokNrAxxOB5s_cND2Nit1rPtfB2LIPXw8YSH7A8hZuCC9584m1IHqtURuSpn78zGk3P6GO4p7I5W4yxqdWmkOsXtKMoDawKe6rOEcGZcJlGjIvpZvp_p6d9-vw4uXQ_yF3u5jTcTlHty5ZdGzBR2Mmi0DBTVAXjAVzPiS-gFXFKf2bHSkZWc-WWBhdKihnilXPoGwRb7lLKP2Tq0yeUh3shdOjIh_obnNEwRLt4ZLPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=a2PXNQi9mqCHOXhSqv2Ndm4Gb_Ski45V4lCAaFAElZtpaU2Rh_Nqyu9plz06kvTxNA8ZC28W15DqHqVy1bclmueyAsdqxCJGa1F9PUh5eIDokNrAxxOB5s_cND2Nit1rPtfB2LIPXw8YSH7A8hZuCC9584m1IHqtURuSpn78zGk3P6GO4p7I5W4yxqdWmkOsXtKMoDawKe6rOEcGZcJlGjIvpZvp_p6d9-vw4uXQ_yF3u5jTcTlHty5ZdGzBR2Mmi0DBTVAXjAVzPiS-gFXFKf2bHSkZWc-WWBhdKihnilXPoGwRb7lLKP2Tq0yeUh3shdOjIh_obnNEwRLt4ZLPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌هایی که از ایران به سمت پایگاه‌های آمریکایی شلیک می‌شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/686350" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
برخی منابع عربی از شنیده‌شدن صدای انفجار در اردن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/686349" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686348">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حملهٔ موشکی آمریکا به اطراف شهر اهواز
معاون امنیتی استانداری خوزستان:
🔹
نقطه‌ای در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/686348" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686347">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
برخی منابع عربی از شنیده‌شدن صدای انفجار در اردن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/686347" target="_blank">📅 23:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686346">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
برخی منابع عربی از شنیده‌شدن صدای انفجار در اردن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/686346" target="_blank">📅 23:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686345">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55155e2342.mp4?token=u4wDBl8EzFSGkY9Aa8h_gEispgj-oPpOE-sA6Dd0VOfdvqZZUbCTx0FJNk3_Q-ECOluJN_debDQF8yYaHdLiD8YJja7p4XDoRTTEinN17HelnHVk7K2Xcp8rlEwD-oiHkIQRWhqO03gliAdrvcofIXhqho_zZgDPlNCb56nEsRtAK6EZ7tIhxbP5qe6ZFKbhjiYImazSsPqtqnassOgAVJzyF7t4X6jKAXDlr8KH64hyfMl9dpawjifMi3vOOL4pvIBQleselpnYp-HhnBgXQetZY72dBwO5_YQ0EP1kTDRcQEcDPi80hAt-xEsvQygqkz1YKXhYk_tnLuWzGOTSdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55155e2342.mp4?token=u4wDBl8EzFSGkY9Aa8h_gEispgj-oPpOE-sA6Dd0VOfdvqZZUbCTx0FJNk3_Q-ECOluJN_debDQF8yYaHdLiD8YJja7p4XDoRTTEinN17HelnHVk7K2Xcp8rlEwD-oiHkIQRWhqO03gliAdrvcofIXhqho_zZgDPlNCb56nEsRtAK6EZ7tIhxbP5qe6ZFKbhjiYImazSsPqtqnassOgAVJzyF7t4X6jKAXDlr8KH64hyfMl9dpawjifMi3vOOL4pvIBQleselpnYp-HhnBgXQetZY72dBwO5_YQ0EP1kTDRcQEcDPi80hAt-xEsvQygqkz1YKXhYk_tnLuWzGOTSdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک پهپاد آمریکایی در آسمان‌ خمین سرنگون شد
🔹
یک پهپاد MQ9 آمریکایی با سامانه جدید پدافند کشور سرنگون شده است.   #اخبار_مرکزی در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686345" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686344">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
آمریکا پیش از انجام عملیات جدید، کشورهای حاشیه خلیج فارس را در جریان قرار داد
🔹
رئیس‌جمهور جنایتکار آمریکا در مصاحبه با فاکس‌نیوز گفت که متحدان آمریکا در خلیج‌فارس پیش از انجام عملیات جدید، از برگزاری عملیات جدید علیه ایران مطلع شده بودند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686344" target="_blank">📅 22:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686343">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
بانک مرکزی آمادگی عرضه تا ۲ میلیارد دلار در بازار را دارد
🔹
بانک مرکزی با استفاده از ذخایری که در پی تغییر سیاست ارزی در دی ماه سال گذشته در اختیار دارد شروع به عرضه گسترده ارز در بازار کرده است.
🔹
به گفته مسئولان این بانک، میزان ذخایر از این محل بالغ بر چند میلیارد دلار است و رئیس کل بانک مرکزی امروز از آمادگی این بانک برای عرضه تا ۲ میلیارد دلار به صورت اسکناس در بازار ارز خبر داده است.
🔹
این اقدام بانک مرکزی برای جلوگیری از اقدامات سوداگرانه کانال‌های تلگرامی و اعلام نرخ‌های غیرواقعی برای دلار صورت می‌گیرد؛ نرخ‌هایی متفاوت که هر کانال تلگرامی برای خود اعلام می‌کند و اختلاف قیمت اعلامی هر کانال با دیگری به بیش از چند هزار تومان می‌رسد.
🔹
پیشتر و در مرحله اول، بانک مرکزی با عرضه ۵۰۰ میلیون دلار برای تامین نیازهای ضروری اقدام کرد که از این میزان صرفاً ۲۰ میلیون دلار آن فروش رفت.
🔹
در این خصوص، بانک مرکزی اعلام کرده هر شخص حقیقی می‌تواند تا سقف معادل ۱۰۰۰ یورو برای تامین نیازهای ضروری خود از بانک‌ها و صرافی‌ها اسکناس ارز خرید کند همچنین اشخاص حقوقی نیز می‌توانند تا سقف ۵۰۰۰ یورو اقدام به خرید کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/686343" target="_blank">📅 22:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686342">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
خبرهایی درباره شنیده شدن صدای انفجار در اربیل
🔹
پس از اینکه برخی منابع از حملات موشکی جمهوری اسلامی ایران به مواضع آمریکا خبر دادند، منابع عراقی از شنیده شدن صدای چند انفجار در شمال این کشور خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/686342" target="_blank">📅 22:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686341">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
وضعیت استان هرمزگان کاملاً پایدار است
معاون امنیتی استانداری هرمزگان:
🔹
در ساعات ابتدایی کانون عمده صداها ناشی از تنش‌ها و درگیری‌های رخ‌داده در پهنه آبی خلیج‌فارس و محدوده تنگه هرمز بود.
🔹
با تشدید درگیری‌ها طی ساعات اخیر، مناطقی از نوار ساحلی استان هرمزگان هدف تحرکات و حملات دشمن قرار گرفت
🔹
جزئیات دقیق آن از سوی مراجع ذی‌صلاح در حال بررسی و پایش تکمیلی است.
🔹
در حال حاضر شرایط در تمامی شهرستان‌ها و مناطق مختلف استان هرمزگان کاملاً پایدار، آرام و تحت رصد است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686341" target="_blank">📅 22:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686340">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
یک مراسم عروسی در سیریک هدف ترکش های حمله وحشیانه دشمن آمریکایی قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686340" target="_blank">📅 22:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686339">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezpZFiZLo2t3ZiXUsrGHiE2XPgXRW5VuNliC0DJ5O-Xmx2WrdpSlNx_3VwWq31nSXVnxrMYc3ZQzCasENwOa8ZhJFm7laYuX0YmqQ78T6UkfAil6YphswB_2ojMzk_Yu1E7ZKRi0Aj61zsR-GLg8lxCklOklsz_W6UrNUbjAGZVa1NTz7s9_POgK8KhvNmqx50bDWMtUjAYxnQZgEIcJMPzLUAl3SgBirzWWaAu8Rd9ngR2VBj_ELlOlH02SmAIX6G01UqEzayQ_YDaJiUcHayHsGRekpSkvAPcXCluvwLuliCID977uSpeYOYREEJ215TL2x05tayk__Fpp_2VELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه پاسداران انقلاب اسلامی: تنبیه سختی در انتظار متجاوزان است، آمریکا از حملات جدید خود پشیمان خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686339" target="_blank">📅 22:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686337">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgBEA2mV9uLfDZ4_ASe4iRugcEW9jiyFyY7by8CsMekYWzSVe3w6vzM8_QK_qSWd3be7gcUYwVsFQrFnpUKmUAaNxEdns94Gqe8qtGsGEkoFcNo6BYGnRuMjhzAuzW8XORR9nC_oa0KLCB_ObCncegH_TFGvus30wklwK3he2ZzvRsD5E1BjkQFuHE33oiypU59TTWvI_nez3VCanbqXKxQTZclVO3ZtM7dXWJBJX7gJ56jErCotxTSDRwGkflI3_zN7c_QivEdzjlYDgmKo3bSS9WfDmuG_XZtPbqCq3JUum1YwiLlyFewDHAdiSbL8vASN8yH_UTBtmFVxSDXgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در بغداد: هرگونه حمله با سرنوشت «اصحاب فیل» پاسخ داده می‌شود
سفارت جمهوری اسلامی ایران در عراق با انتشار پیامی در شبکه اجتماعی ایکس:
🔹
ایران هرگز مرعوب تهدیدات و لفاظی‌های دشمنان نخواهد شد.
🔹
هرگونه تعرض به خاک و امنیت جمهوری اسلامی، با پاسخی عبرت‌آموز و سخت همچون سرنوشت «اصحاب فیل»  روبرو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/686337" target="_blank">📅 22:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686336">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
یک پهپاد آمریکایی در آسمان‌ خمین سرنگون شد
🔹
یک پهپاد MQ9 آمریکایی با سامانه جدید پدافند کشور سرنگون شده است.   #اخبار_مرکزی در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/686336" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686335">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
هم اکنون؛ شنیده شدن دوباره صدای انفجار در چابهار/ صداوسیما
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686335" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686334">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
تکذیب حملات دشمن به «جم»، «کنگان» و «لنگرود»
🔹
شبکه‌های اجتماعی از وقوع انفجار در ۳ شهرستان «جم»، «کنگان» و «لنگرود» خبر دادند که مقام‌های استانی اصابت هرگونه پرتابه و حمله دشمن آمریکایی را به این نقاط تکذیب کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686334" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686333">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
بلومبرگ: ترامپ عملاً با بی‌اعتنایی جهان روبه‌رو شده است، چین عقب ننشسته، برخی ارتباطات بانکی ایران در امارات ادامه دارد و پروازها و تجارت با چند کشور برقرار مانده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686333" target="_blank">📅 22:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686332">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
یک پهپاد آمریکایی در آسمان‌ خمین سرنگون شد
🔹
یک پهپاد MQ9 آمریکایی با سامانه جدید پدافند کشور سرنگون شده است.
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/686332" target="_blank">📅 22:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686331">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/686331" target="_blank">📅 22:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686330">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
یک مراسم عروسی در سیریک هدف ترکش های حمله وحشیانه دشمن آمریکایی قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/686330" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686329">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
دقایقی پیش حمله دشمن آمریکایی به فرودگاه جیرفت
🔹
اطلاعات تکمیلی منتشر می‌شود  #اخبار_کرمان در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/686329" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686328">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
حملهٔ دشمن آمریکایی به منطقه‌ای غیرنظامی در کوهستک
استانداری هرمزگان:
🔹
دشمن آمریکایی در حملهٔ وحشیانه به خاک کشورمان منطقهٔ مسکونی کوهستک را مورد حمله قرار داد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/686328" target="_blank">📅 22:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686327">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/686327" target="_blank">📅 22:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686326">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHY4Pk6oe2XIIxK47omY9ER21yqLVeKx9dgYbkzbZRFVAGCszk8hrrIEOyxwUzjfG65MkzJBXJWS46rWgX0MTlveJyo4zqI_Okc4qUaU2mAAdIjyjT7n7QWw_YJPwIl-muCRe-aSaD_6_Yva6Zy2c-toE1c3XQeuRvDwsyDBUEHHFCEbp-K_2nL9_MPrb7XvO7QgPRVv4h7VU2Ja6LMvObUYeoZoSJIIeFQLl5Gq0tNb8GDOafOFJx_9d3fRY0gfIfyl7PjRKsXbM-OPk-oPGfLEWRvd-xHSg56h7KFls4Z3nTqV5_uPxoSJgOfuJEmf2N_JXsDEOeOnna4Bpnho7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در غنا در واکنش به حملات مجدد امشب آمریکا: یک ساعت پیش، اشتراک دوباره تمدید شد
🔹
آمریکا همچنان وفادارترین مشتری ما برای چشیدن طعم «تحقیر ساخت ایران» است، البته مشتریان وفادار، پاداش این وفاداری را به صورت ویرانه‌ها تحویل می‌گیرند.
🔹
سفارش به‌صورت هوایی ارسال خواهد شد. انگار بعضی مشتری‌ها فقط ساخته شده‌اند که بها بپردازند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/686326" target="_blank">📅 22:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686325">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07956f8e14.mp4?token=IxdTiELVcG1E9TRzkqCns_mFwPhl3rauhT3EGLxz7MaQkQ0Jsr5n0IjaPLf0WNJMAYHCDFcUezbo65l6Xp2VD8c7NGaNQnAPybAAZzLpH5ldia3N-_r0V97mspKaqypEhXcSr15xoZAwd__-I3jjGOZ-l_eAv64NVyIG-NU-5Rtj_xVLi98EAtHKl-Icy4lceHDZTssYIUE6ZUOo73_yeuiSXvVvAUyVoZWwEnt7TdNYHE0h-MkXntMtKUFLFIttVJM4c_nwWgrftkX4GYvhxB9dm8g5PgNNqfN4Fej5jD5lblZveLpuijEsIVrvuhGsiuKCcAo9Pk_AUeAbTzBN2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07956f8e14.mp4?token=IxdTiELVcG1E9TRzkqCns_mFwPhl3rauhT3EGLxz7MaQkQ0Jsr5n0IjaPLf0WNJMAYHCDFcUezbo65l6Xp2VD8c7NGaNQnAPybAAZzLpH5ldia3N-_r0V97mspKaqypEhXcSr15xoZAwd__-I3jjGOZ-l_eAv64NVyIG-NU-5Rtj_xVLi98EAtHKl-Icy4lceHDZTssYIUE6ZUOo73_yeuiSXvVvAUyVoZWwEnt7TdNYHE0h-MkXntMtKUFLFIttVJM4c_nwWgrftkX4GYvhxB9dm8g5PgNNqfN4Fej5jD5lblZveLpuijEsIVrvuhGsiuKCcAo9Pk_AUeAbTzBN2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری که گفته می‌شود مربوط به پرتاب یک موشک بالستیک از تبریز به سمت پایگاه‌های آمریکایی در پاسخ به تجاوز امشب این رژیم است
./ فرهیختگان
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/686325" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686324">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
علی بازگشا، سخنگوی پرسپولیس در گفتگو با خبرفوری:  بازی خوبی قبل از دربی داشتیم و از نظر روحی و جسمی آماده‌ایم
🔹
خوشحالیم استقلال هم با شرایط خوب به دربی رسیده و امیدوارم شاهد بازی خوبی در اصفهان باشیم.
🔹
درباره داوری صحبت نمی‌کنم، اما نکاتی را به داور منتقل کرده‌ایم و نگرانی‌هایی در فضای هواداری وجود دارد.
🔹
تارتار تیم را هجومی بسته؛ بازیکنان دوندگی بیشتری دارند و تیم از بالای زمین پرس می‌کند.
🔹
نقل‌وانتقالات زیر نظر تارتار بوده و بیفوما با حضور او تبدیل به بازیکن متفاوتی شده است.
🔹
تارتار تحت تأثیر جو فضای مجازی قرار نمی‌گیرد و هر بازیکنی را که بتواند به تیم کمک کند، به ترکیب اضافه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/686324" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686323">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
بقائی سخنگوی وزارت امور خارجه: هشتاد و هفتمین سالگرد آغاز جنگ جهانی دوم، فرصت عبرت‌انگیز از درس‌های تاریخ است؛ عادی‌سازی قانون‌شکنی بزرگترین تهدید برای صلح و امنیت بین‌المللی است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/686323" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686322">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6jCYmYqZZUMo24TaJ7LWMKP2mzlYOGWO-A8NiIgyv35oRe9lseMb8vZt10ZoJO8NEuJY6soR7wFWOFwmrmomp6Ff-bc4N-0ev8-5oX0MfqTNHNOIDtTehtsPja3NrZaFKsR3dJQekN7HuVLtNg54B9g5HXeJxx6swX1i6ttH_EQHMAd5Ab8HnrQIz0QoM1vF5Q7n6W0YvsV5jNS4UfumPE94y755GSO7FBSYYzQB59lZMYgX4NMrapJ8vwtOfMNPLmZHGpjRj9VZOISdf_qNQrdFpRnkFf5ObgB1pqpRaJSdSyqLReFQKLWjHzYNquU2bcmAcVAAVR22q1euZ-5Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایالات متحده هشدار امنیتی برای شهرهای ابوظبی و دبی صادر کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/686322" target="_blank">📅 22:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686320">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3bee3a53.mp4?token=tsVlP7Fr7vu9Vv0HKg7vt5Iwjak57JauawiMZyIwdeU3UsHjTNPAkqHyh-jO50zuidyG2verR664HDPPdtl5WG8mP_vlxA_CYhHrrxGETnl_-ikW8YKvBucB6dGvU5xx2qdnQyIjlFaAiJ_x8Pdbvb5YUnt2GzPpUWe3BMtNfsLvD12Awb0feLscFc4jYOe0aE-Offp_Nx6xi0js5cDXnL8IqD0kX-DG-lpytaoZOO9By-xqH-zNwOGJ4CZMRP0HS3xVTqdPabcQVZANQNgMVZwbjp5y16acsCgPciy7UpcCy6MU9CN2Szw76e49WkIS0cCq7AX6vLb-Tr2bbnR5Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3bee3a53.mp4?token=tsVlP7Fr7vu9Vv0HKg7vt5Iwjak57JauawiMZyIwdeU3UsHjTNPAkqHyh-jO50zuidyG2verR664HDPPdtl5WG8mP_vlxA_CYhHrrxGETnl_-ikW8YKvBucB6dGvU5xx2qdnQyIjlFaAiJ_x8Pdbvb5YUnt2GzPpUWe3BMtNfsLvD12Awb0feLscFc4jYOe0aE-Offp_Nx6xi0js5cDXnL8IqD0kX-DG-lpytaoZOO9By-xqH-zNwOGJ4CZMRP0HS3xVTqdPabcQVZANQNgMVZwbjp5y16acsCgPciy7UpcCy6MU9CN2Szw76e49WkIS0cCq7AX6vLb-Tr2bbnR5Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ هدف قرار دادن و سرنگون کردن یک هدف متخاصم در آسمان ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/686320" target="_blank">📅 22:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686319">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سخنگوی دولت : نمایشگاه
#الکامپ
بی نظیر است. مهاجرانی: جوانان ایرانی همه محدودیت ها را دور می زنند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/686319" target="_blank">📅 22:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686318">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در عسلویه
🔹
فرماندار عسلویه از شنیده‌شدن صدای انفجار در این شهرستان خبر داد.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/686318" target="_blank">📅 22:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686317">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
عملیات قاطع نیروهای مسلح ایران در پاسخ به دشمن تروریست آمریکایی آغاز شد
🔹
پایگاه‌ها و منافع آمریکا در منطقه زیر ضرب موشکها و پهپادهای ایران قرار می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/686317" target="_blank">📅 21:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686316">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
شلیک موشک‌های ایرانی به‌سمت مواضع دشمن
🔹
مشاهدات میدانی برخی خبرنگاران از شلیک موشک‌ و پهپادهای ایرانی به‌سمت مواضع دشمن حکایت دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/686316" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686315">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ در مصاحبه با فاکس‌نیوز: اگر ایران حملات اخیر آمریکا را تلافی کند،‌ دوام نخواهد آورد
🔹
توافق با ایرانی‌ها حتی ارزش کاغذی که روی آن نوشته شده را هم ندارد و ما به آنها فرصت‌های زیادی دادیم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/686315" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686314">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هر جسارتی تاوانی دارد ...
🔹
آمریکا دوباره با سکان‌دار نابخردش، طمع حمله به ایران کرده، سکوت در برابر زیاده‌خواهی ترامپ نه‌تنها زخم گستاخی او را ترمیم نمی‌کند، بلکه جسارت دشمن را دوچندان می‌کند.
🔹
تجربهٔ تاریخی گواه است که عقب‌نشینی تنها بر طمع متجاوز می‌افزاید. آنکه مرزهای عزتِ ملتی را نادیده گیرد، باید بداند که گریز از تاوانِ اقدام خویش، محال است.
🔹
هجوم به ایران، عبور از خط قرمزی است که بازگشت از آن، به‌سادگی خیال خام متجاوز نیست.
🔹
هر گونه تعرض به حریم این سرزمین، هزینه‌هایی سنگین و جبران‌ناپذیر در پی دارد. هزینه‌هایی که نه‌تنها دامن عاملان، که تمامیتِ نظم منطقه‌ای را درگیر خواهد کرد.
اما پاسخ ایران، هرگز شتاب‌زده و هیجانی نخواهد بود، بلکه با ترازوی عقل و در چارچوب مصالح ملی سنجیده می‌شود.
🔹
جمهوری اسلامی ایران، با درک کامل از نقاط آسیب‌پذیر دشمن، قدرت محاسبه و واکنش متناسب را داراست.
این نه تهدید، که اعلام ظرفیت هوشمندانه‌ای است برای حفظ بازدارندگی. رویکرد ایران، مبتنی بر سنجش دقیق هزینه‌فایده است. تا هر گونه اشتباهِ محاسباتی طرف مقابل، پاسخی متقارن و کوبنده، اما حساب‌شده بیابد.
🔹
عزت ایران، در هیبت واکنشِ به‌هنگام و تدبیرآمیز اوست؛ واکنشی که فارغ از غرورِ کاذب و خشم زودگذر، با ثباتِ راهبردی، پایه‌های هر گونه زیاده‌خواهی را فرو می‌ریزد و به متجاوز می‌آموزد که تعرض به این سرزمین، نه صرفاً یک اشتباه، که فاجعه‌ای بی‌بازگشت است.
تاریخ، شاهد صبر راهبردی ملتی بوده که هرگز بهای عزت خود را نادیده نگرفته است.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/686314" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686313">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
دقایقی پیش حمله دشمن آمریکایی به فرودگاه جیرفت
🔹
اطلاعات تکمیلی منتشر می‌شود
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/686313" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686312">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ در مصاحبه با فاکس‌نیوز: اگر ایران حملات اخیر آمریکا را تلافی کند،‌ دوام نخواهد آورد
🔹
توافق با ایرانی‌ها حتی ارزش کاغذی که روی آن نوشته شده را هم ندارد و ما به آنها فرصت‌های زیادی دادیم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/686312" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686311">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
حمایت مالی پارک فاوا از شرکت‌های فناور؛ از لیزینگ تا خرید دین
🔹
دکتر مافی، رئیس پارک فاوا، از برنامه این مجموعه برای بازارسازی و توسعه بازار شرکت‌های فناور و دانش‌بنیان حوزه فاوا خبر داد.
🔹
به گفته مافی، با همکاری صندوق‌های پژوهش و فناوری عامل پارک، قراردادها و تفاهم‌نامه‌های منعقدشده در نمایشگاه‌ها از طریق ابزارهایی مانند تسهیلات لیزینگ و خرید دین مورد حمایت مالی قرار می‌گیرند.
🔹
او همچنین اعلام کرد تاکنون به ۱۵۰ واحد فناور خارج از پارک و ۸۰ واحد مستقر در پارک تسهیلات پرداخت شده و برای حمایت از شرکت‌های آسیب‌دیده از شرایط بحرانی نیز تسهیلات سرمایه در گردش ویژه جنگ و بحران اختصاص یافته است.
🔹
مافی ابراز امیدواری کرد با توسعه شبکه‌سازی و بازارسازی، شرکت‌های فاوا از شرایط بحرانی عبور کرده و نقش مؤثرتری در تأمین نیازهای فناورانه کشور ایفا کنند.
▫️
کانال تلگرام فاوا
https://t.me/ICTPark_Newsline
▫️
مشروح خبر
khabarfoori.com/fa/tiny/news-3242044
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/686311" target="_blank">📅 21:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686309">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
در حملات امشب تاکنون کسی آسیب ندیده و زیرساخت‌ها نیز سالم هستند/صداوسیما
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/686309" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686308">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: عبور از تنگه هرمز، منوط به پرداخت غرامت جنگی شد
🔹
مطابق ماده هفت طرح مدیریت هوشمند تنگه هرمز  تمامی کشورها، سازمان‌ها و اشخاص حقیقی و حقوقی که در دوران جنگ خساراتی به جمهوری اسلامی ایران۷ وارد کرده‌اند، ملزم هستند تا با دولت جمهوری اسلامی ایران بر سر نحوه پرداخت غرامت به توافق برسند.
🔹
بر اساس این مصوبه، در صورتی که این کشورها یا شرکت‌ها نسبت به پرداخت غرامت اقدام نکرده و یا در این زمینه با جمهوری اسلامی ایران به توافق نرسند، مجوز عبور آن‌ها از تنگه هرمز صادر نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686308" target="_blank">📅 21:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686307">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شنیده شدن دوباره صدای انفجار در بندرعباس و قشم
🔹
در جزیره لاوان هم صدای انفجار شنیده شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686307" target="_blank">📅 21:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686305">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L23GAfJp6zsL-dVPq24THIIbSsdQ3zjksEqmVQcifJ4ALgXy01HWm7hyrAVYGEW_UX_VNZhUQWMboFN844y0KB2IIpt01Ep1AgoVE5nFVJfr6iGeF1sbSSJiwHXyAWALTurqcikjRS25d4WeZLgfYDHRB2n5nWGVjZK6XS2M1z1lK9Zz0brEG4P45U4T1P40JRrjshaIEfiWOXd0RRS_8kzq8NtOj-AIST7EwGDHchqrudZCvqVRIJR8cJ4nCtu8WBvjM1_zK-cEzmJ-j9ZUW5jLoJJaA8uNPUbWnlHqdFmfYI6eYG-FR_0Ueq7oyr3Rgqu-OHkJFp7fEGlZvhG5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-WjJugHLXCQoUYQZeVCXHVc7B5VCJ4xikL3orCi1HPsRNCwmw7ZdibeU8btI0STnChCfRNu4z_5QM4ZFeIKQIPh0HpB5a7X9wKBCFfxx3n7Rqx6p3KixcdQzZ6_3PQxpjQHKoocR0617FZn7vD9e9eOSl_G2vnngqaKMWaCBnNHOVBfUAgSCbhtkYo-11PImXI8Py2J6hsNlCaTFjR666V6W2RyPmo88c4__U5rn7wu3ILlzDEEzYgvY5P6XE-gLF8BqcZnIpKluM2PevKRYnH--RtvWGrgOptodDV1hXWn0Gn3o9zTnlMjW8-Nr8-yT0tZHpLY9hGXX6edPwC1wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میزان و کیفیت خواب مناسب در رده‌های سنی مختلف
🔹
بررسی آمارهای سلامت خواب نشان می‌دهد نیاز به خواب با افزایش سن کاهش می‌یابد؛ به طوری که نوزادان به ۱۷ ساعت و سالمندان به ۷ ساعت خواب روزانه نیاز دارند.
🔹
در بخش کیفیت خواب نیز، زنان ۴۰ درصد بیشتر از مردان به بی‌خوابی مزمن مبتلا می‌شوند، در حالی که مردان ۲ برابر بیشتر از زنان دچار آپنه یا وقفه تنفسی در خواب می‌شوند.
🔹
همچنین با گذشت زمان، میزان خواب عمیق در هر دهه حدود ۲ درصد کاهش یافته و در افراد بالای ۶۵ سال، بیداری‌های ناگهانی در طول شب به اوج می‌رسد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/686305" target="_blank">📅 21:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686304">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
مرشایمر: ادعای کنترل آمریکا بر تنگه هرمز مضحک است
استاد علوم سیاسی دانشگاه شیکاگو:
🔹
کاملاً روشن است که ایرانی‌ها تا حد زیادی کنترل تنگه هرمز را در اختیار دارند.
🔹
پیش از آغاز جنگ، روزانه حدود ۱۳۰ کشتی از تنگه عبور می‌کردند، اما این رقم اکنون به حدود ۸ تا ۱۱ کشتی در روز کاهش یافته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/686304" target="_blank">📅 21:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686303">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01137ebf30.mp4?token=Re_bUBlgkMcks3uj-wdk00zm_XMydXsBcbWo26O-2G02r7vpSXT7qNi2XBIG-aNE16vLoHpN1DR4dsPQVNN7ERtde3NLDgWRw2GasWlNtH42B5H6M6tzgluZX1Kmk2CVfRJux1M8v2ZRXzAn-w6fU-bQKyExYXgsCngC2KRclRKTLMfcXHQPKG5XFA8rUBrRXs5DQf0IB1EYRwTwMX2Ow-ZowLGxwgS8wpd1wiqXfghsXf4fbgfvbCYDWzP0igmcR2hlg0S7a2Q63OoqYGlRqak6MgCqZFkaytdQspYNlHySYkMkFMRkdZaDoFOof_xUIcs81RAfQ7baPlLQuN8WOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01137ebf30.mp4?token=Re_bUBlgkMcks3uj-wdk00zm_XMydXsBcbWo26O-2G02r7vpSXT7qNi2XBIG-aNE16vLoHpN1DR4dsPQVNN7ERtde3NLDgWRw2GasWlNtH42B5H6M6tzgluZX1Kmk2CVfRJux1M8v2ZRXzAn-w6fU-bQKyExYXgsCngC2KRclRKTLMfcXHQPKG5XFA8rUBrRXs5DQf0IB1EYRwTwMX2Ow-ZowLGxwgS8wpd1wiqXfghsXf4fbgfvbCYDWzP0igmcR2hlg0S7a2Q63OoqYGlRqak6MgCqZFkaytdQspYNlHySYkMkFMRkdZaDoFOof_xUIcs81RAfQ7baPlLQuN8WOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمامی حملات امشب آمریکا به جنوب کشور به مناطقی بود که قبلا به آن حمله کرده بود
🔹
در این حملات آسیبی به افراد و زیرساخت‌ها وارد نشده است./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686303" target="_blank">📅 21:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686302">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آژانس اتمی بار دیگر مدعی «عدم پیشرفت» در برنامه هسته‌ای ایران شد
🔹
در گزارش فصلی جدید آژانس بین‌المللی انرژی اتمی درباره ایران که برای کشورهای عضو ارسال شده و رویترز نیز به آن دست یافته است ادعا شده که هیچ پیشرفتی در پرونده ایران حاصل نشده است.
🔹
در این گزارش ادعا شده که آژانس از زمان حملات آمریکا و اسرائیل در ژوئن ۲۰۲۵ به ذخایر اورانیوم ایران دسترسی لازم برای راستی‌آزمایی نداشت است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686302" target="_blank">📅 21:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686301">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
فرماندار لنگرود و مدیرکل مدیریت بحران استانداری گیلان وقوع هرگونه انفجار یا اصابت در شهرستان لنگرود را تکذیب کردند
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686301" target="_blank">📅 21:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686300">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a2512ead.mp4?token=F89d0lfrTubeItF9hHMIDmbIVB04RDKBSD3JXgFRk2HSPI1CXjKr6kBTGlEZ24bGzmcmcJtU6hXirudtJWwwq--rX2bdAi8jdSiqPbtNTnYCge82Cttv3_u_IkLVcaONaLYk4FhoUertqhRVrrTHZxXLJovSzUHCKxGwuyaAtfUCT4zC4jyVDVBBsXKRYgSi2fzqN3anOcff0CcBxZF7r8LvndNwsHcCt-lC_3_LJoabaFe7q5-CsN4PUA5VT6WQLeVORgbMy8AittNLgjiDNCBoST3r4iRfIO-5TlTNoCbTR7rEQ8a7ZMCh7UaeM3GkwmFw4w27YxpLW2rXn5IaC2tGHtCOkTsfk5kibdwnDwm_hZnwOh3IQ0vcHGolLhcGDL7RX2cXn8ljmusyt4D3ddmvXFV55A6Yn5qhWanpkm0pDqY7QaLQD1aKUfuZ5hy8ap-ldzsa-yIR-PA2A5-v1xh42Ad1QwzWesXpaDQVURj3RpT3HCu8HSAumtEPYk_MEysJ63hy00AVYvt5HFEdkT4zJ4xuQ1w068q14VL3gnu29W8C9pnV1tZkPkZQMlqBoePgz5C50WcelWVzrADUyl_85g5S8zUAdOdr3QooTY6IuzYdMQbwfyzg-1aR-Iw28_TFsHpBSioai7ZswhZtyM-VzX09w4p3leavlv-ilgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a2512ead.mp4?token=F89d0lfrTubeItF9hHMIDmbIVB04RDKBSD3JXgFRk2HSPI1CXjKr6kBTGlEZ24bGzmcmcJtU6hXirudtJWwwq--rX2bdAi8jdSiqPbtNTnYCge82Cttv3_u_IkLVcaONaLYk4FhoUertqhRVrrTHZxXLJovSzUHCKxGwuyaAtfUCT4zC4jyVDVBBsXKRYgSi2fzqN3anOcff0CcBxZF7r8LvndNwsHcCt-lC_3_LJoabaFe7q5-CsN4PUA5VT6WQLeVORgbMy8AittNLgjiDNCBoST3r4iRfIO-5TlTNoCbTR7rEQ8a7ZMCh7UaeM3GkwmFw4w27YxpLW2rXn5IaC2tGHtCOkTsfk5kibdwnDwm_hZnwOh3IQ0vcHGolLhcGDL7RX2cXn8ljmusyt4D3ddmvXFV55A6Yn5qhWanpkm0pDqY7QaLQD1aKUfuZ5hy8ap-ldzsa-yIR-PA2A5-v1xh42Ad1QwzWesXpaDQVURj3RpT3HCu8HSAumtEPYk_MEysJ63hy00AVYvt5HFEdkT4zJ4xuQ1w068q14VL3gnu29W8C9pnV1tZkPkZQMlqBoePgz5C50WcelWVzrADUyl_85g5S8zUAdOdr3QooTY6IuzYdMQbwfyzg-1aR-Iw28_TFsHpBSioai7ZswhZtyM-VzX09w4p3leavlv-ilgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک مداح از حضور رهبر انقلاب در مراسم رهبر شهید ایران در حرم رضوی
حاج عباس حیدرزاده:
🔹
آقای مروی فرمودند حضرت آقا در شب دفن رهبر شهید از ساعت ۱۲ شب تا هفت صبح، در حرم بودند و حتی مسئولان حاضر، پشت سر ایشان نماز خواندند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/686300" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686299">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سخنگوی سپاه پاسداران انقلاب اسلامی: تنبیه سختی در انتظار متجاوزان است، آمریکا از حملات جدید خود پشیمان خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/686299" target="_blank">📅 21:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686297">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
حمله آمریکا به یک کارخانه پودر ماهی در قشم
🔹
در حملات ساعتی پیش ارتش متجاوز آمریکا به سواحل جنوبی ایران یک کارخانه پودر ماهی در قشم، یک اسکله صیادی و دکل اداره‌ی بنادر در سیریک مورد حمله قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/686297" target="_blank">📅 21:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای ترامپ: این حملات گسترده و قدرتمند هستند و در واکنش به تلاش نافرجام ایرانی‌ها برای کار گذاشتن مین‌های دریایی در تنگه هرمز انجام می‌شوند
🔹
تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (مین‌ها به‌طور کامل منهدم یا منفجر شده‌اند!).
🔹
همچنین این حملات…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686296" target="_blank">📅 21:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686295">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
واشنگتن از پاسخ تند و قدرتمند ایران به تجاوزات خود بیمناک است
🔹
شبکه فاکس‌نیوز در گزارشی اعلام کرد  مقامات آمریکایی به دلیل اقدامات تهاجمی اخیر، از واکنش شدید و انتقام‌جویانه ایران در منطقه واهمه دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686295" target="_blank">📅 21:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686294">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAASfjfmrLzBlv1ouaKupK6S7wbtwzXKTvZVzsR-Iq_knANx8EI95FoRVQXaqKyACKt88-Dp3Vo7mO-i24PWdOERJD7GCiYyJoT07TwQrBhSPwcbIVcvWshIagmb6TdsaWPZu68_oSUDH8IA3Ze-EYVZRRNFCEzImsUaxghLgW5m9kSl9UBvu_LbjPFdsThZAdYpruOrtDxTM6inJt1CsLPXEAZclY7xxAJYKiUEGiP2JSKdQbEV8wrSkp7z11DZ-c7mQJVXC36nAR6oEFq76PIBevULwj7isSHv5Sd7uQfQTb9_swrQPEf1H4-zjnsSIyMtxjGEZ53QrP1Upg82kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه پاسداران انقلاب اسلامی: تنبیه سختی در انتظار متجاوزان است، آمریکا از حملات جدید خود پشیمان خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/686294" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686293">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
به گفته منابع محلی، دقایقی قبل صدای ۶ انفجار در بندر چابهار و کنارک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/686293" target="_blank">📅 21:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686292">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUDn06-D3AQicOSK84JgLPcg6MXHK8lSAQCbQZ0q4Fq4kyrux5rmRBWQP_hoTWou_pHvF2dXXI5lFM2ACULR72w2kq02vFCX0070r-L1r-kKzRfAWRkuyuOOJEs8URHUQheBxZ2OlEHPstDKe2MrS5VKTwz4L87jNPsbpizCjnYatif5BOnrT6b5QqVk-xW9n_ZTP7XcYrH5g8FyPH6hhxwsXruMGmxs3eRJHpszuQ5yVTsI9pT0lw-eGA1GNiRKtsgLTCNV7QWnVEnffOq7YxTe7HgMzNjsr5YEGaJ1Z3VoFOwYRQBAQP2rMjMO6s60RjJQy5Y-YWky4o53J5anpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: آمریکا در حال انجام حملاتی علیه اهدافی ایرانی در نزدیکی تنگه هرمز است #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/686292" target="_blank">📅 21:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686291">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
یک منبع نظامی: ایران به حملات آمریکا پاسخ چند برابری می‌دهد
🔹
یک منبع ارشد نظامی به تسنیم گفت که نیروهای مسلح ایران به جنایت امشب آمریکایی‌ها در حمله به نقاطی از کشورمان قطعاً پاسخ می‌دهند و این پاسخ چند برابر حملات آنها خواهد بود.
🔹
همچنان که پیشتر نیز هشدار…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/686291" target="_blank">📅 21:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686290">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5136a28d0a.mp4?token=s6cC7inrtlarxRTC-JzuwRdTFzpXBv2ksY0BreTIlzSS_kNj_v00w9GiwOoFgTOcVNXjUuQhfa5Y_whDCNFjjCDc1T8lvUcrRNBtiW9HP5__WgOg8-cv2JO0CW7Ue4xD-aUczrwam1-o9OFkJHvL1fPpImSURLFGs5LOIkpOUqOiV0VJNxPMAoKgCE8BSgoYRztTuKjSR6ctmw_xgN-pQNNoNa8iCXkJAXxOBnEdUgxs0OdzWL1oNLt85hxvPJzQddBZL8SBK_6rNwNXSZYyEYttgRxdtag3LLvrVPAX0zcQZ7vuHm5EvOGP_mwptey0PQ88PjvVz8EHXfC2SPdW8CQpkmrOvbN6Ly8S_Bhe7Kf5Oob6fcyDtJty5lvXRlm--x-dPj8iuu2qfCCbLJAvEn6HqpPepiWmZPU7c5nPwQLXeHIvxo6xGj2JhvpwR2OozLcPCB88x0q4pNavF3uJZ6uvvlo2zdhIs4O0zMYmgZhnFFMhaMpx0K-fXAWYuUKmVzVBnvLkd93LpCOBvprn3-CAWyGbB8fhbBPrboX-HgE-3yfz0RuMqs-b-09F60qdbLRfCjUxLMWHFd3ifq7dHqeex1vW9UIxVTOWdw-VGbWAgNjN0T3DevNCmITB7datrcRBrZV_pBcprYFo26fO16WYPUhZbloNxDdVItc2iuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5136a28d0a.mp4?token=s6cC7inrtlarxRTC-JzuwRdTFzpXBv2ksY0BreTIlzSS_kNj_v00w9GiwOoFgTOcVNXjUuQhfa5Y_whDCNFjjCDc1T8lvUcrRNBtiW9HP5__WgOg8-cv2JO0CW7Ue4xD-aUczrwam1-o9OFkJHvL1fPpImSURLFGs5LOIkpOUqOiV0VJNxPMAoKgCE8BSgoYRztTuKjSR6ctmw_xgN-pQNNoNa8iCXkJAXxOBnEdUgxs0OdzWL1oNLt85hxvPJzQddBZL8SBK_6rNwNXSZYyEYttgRxdtag3LLvrVPAX0zcQZ7vuHm5EvOGP_mwptey0PQ88PjvVz8EHXfC2SPdW8CQpkmrOvbN6Ly8S_Bhe7Kf5Oob6fcyDtJty5lvXRlm--x-dPj8iuu2qfCCbLJAvEn6HqpPepiWmZPU7c5nPwQLXeHIvxo6xGj2JhvpwR2OozLcPCB88x0q4pNavF3uJZ6uvvlo2zdhIs4O0zMYmgZhnFFMhaMpx0K-fXAWYuUKmVzVBnvLkd93LpCOBvprn3-CAWyGbB8fhbBPrboX-HgE-3yfz0RuMqs-b-09F60qdbLRfCjUxLMWHFd3ifq7dHqeex1vW9UIxVTOWdw-VGbWAgNjN0T3DevNCmITB7datrcRBrZV_pBcprYFo26fO16WYPUhZbloNxDdVItc2iuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دات‌وان ونچر؛ بازوی سرمایه‌گذاری در حوزه نوآوری و خلاقیت
🔹
در جریان برگزاری نمایشگاه الکامپ، دات‌وان ونچرز به عنوان بازوی سرمایه‌گذاری هلدینگ دات‌وان، برنامه‌های خود را برای حمایت از زیست‌بوم استارتاپی کشور تشریح کرد.
🔹
علیرضا حاج سعید، مدیرعامل دات‌وان ونچرز:
🔹
با توجه به نیازمندی‌هایی که شرکت‌های هلدینگ دات‌وان دارند، در ونچر استودیو توانستیم ۱۱ هسته فناور داشته باشیم. روی ۱۶ تیم سرمایه‌گذاری کنیم که ۶ تا از سرمایه‌گذاری‌ها به بلوغ رسیده و الان واگذار شده به هلدینگ. بقیه هم در پروسه انجام است.
🔹
فردای کشور را فقط ایده نمی‌سازد، حل مسئله می‌سازد. از خودتان سوال کنید که چه مشکلی را حل می‌کنید؟ آن‌وقت ما به عنوان دات‌وان ونچر در کنار شماییم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/686290" target="_blank">📅 21:00 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

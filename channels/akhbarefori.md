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
<img src="https://cdn4.telesco.pe/file/Fv4DFSyCIVvujP-oiP82KWpiD-TnvMTQg_sCXaK1hwbRgoLS0l-xgyvBCJtUP1g7Ur5yq_k6KnXdkrjLgAsPMSJWevtP_69m1mb58_zMCRwpx-_-iL5ERwyQf_x2XnYofltQHTcHkimHDgmG9kFGpi2d7o29cBr7ODKYw9qmW6Zdbx3YTDubo6OriJW6tA6-QzUat4URLlEtcWtVLl3lKAV_AcIzpj6J3n2PoNP1MieArFJS5gVVRjCpiAv2Swg1P3ZmYknPj5xbesmzpSWI8sLy_a8yqRYnQvfa1B-OAwlt293mTDeiVJcc74nMRHaPKKm9CYw1JpYbLQgRUXrN_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.93M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 12:53:21</div>
<hr>

<div class="tg-post" id="msg-652094">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8E0XguDzTHq8-5lQSpiIJ_dcLu0BgkkgHebWlF2I9CHJk0CegD5Q98X28w1Cz2cUJySk_XbmuN4-xdr2b5WsekP6fAFnoBcfUxa91b_309gRsNKPEEgEAcAppl6IuLTDEfDy0E6q8pY9c7hNfLHKo704aV9MVEsY1mgi7GbsEErtHN-PjuL8DWT4TUtkyJkaWEDYTf0YhxfImVtoKFCr1wgYgp0GnR-cyp80Je_GQTV7p9ax3y_MoLWXfv_Bd3fsKPwpBgVjf6DdGS_n_NppaY5ldOxlSZ0UpFH0WLnxZhWATs83JzQvNtLlhcpb13996Otm5Y4HmerIjs82BczqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کاربر فضای مجازی: بعد از اینمه فشارها آیا برای بعد از قطعی اینترنت پرو، راهکاری هم برای کسب و کارها دارید؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 551 · <a href="https://t.me/akhbarefori/652094" target="_blank">📅 12:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652093">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
۲۸ نقطه شمال تهران مورد اصابت موشکی قرار گرفت/ ۴۵۷واحد مسکونی آسیب دید
🔹
شهردار منطقه یک تهران: در این منطقه ۲۸ نقطه اصابت موشک ثبت شده که در نتیجه آن، ۴۵۷ واحد مسکونی با آسیب‌های جزئی تا تخریب کامل مواجه شده‌اند.
🔹
۱۱۵۳ دستگاه خودرو و ۸۷ دستگاه موتورسیکلت مردم عادی آسیب دیده‌اند.
🔹
در یکی از نقاط اصابت هشت بار انفجار رخ داده و همچنین انبار نفت نیز هدف قرار گرفته است.
🔹
در اصابت محله زعفرانیه ۲۸۳ واحد مسکونی پیرامونی نیز آسیب دیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/akhbarefori/652093" target="_blank">📅 12:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652092">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
همه بانک‌ها مجاز به خرید و فروش ارز تا سقف ۱۰۰۰ یورو شدند
🔹
براساس دستورالعمل بانک مرکزی، هر فردی می‌تواند تا سقف ۱۰۰۰ یورو (یا معادل آن به دلار) در سال، ارز اسکناس برای نیازهای ضروری خرد از شعب بانکی خریداری کند.
🔹
منبع این اسکناس‌ها، خرید از صادرکنندگان است و کاملاً از منابع ارزی حواله‌ای که برای واردات کالاهای اساسی و مواد اولیه استفاده می‌شود؛ جداست.
🔹
بانکها موظفند ضمن الزام به رعایت سایر ضوابط و مقررات ارزی در اجرای این بخشنامه، مراتب را به تمامی شعب و واحدهاي ارزي ذي‌ربط ابلاغ و بر حسن اجراي آن نيز نظارت کنند.‌‌‌‌‌‌‌‌‌‏
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/akhbarefori/652092" target="_blank">📅 12:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652091">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
۴ شهید در حمله هوایی رژیم صهیونیستی به لبنان
🔹
منابع محلی خبر دادند که در پی حمله هوایی رژیم صهیونیستی به دو خودرو در جاده منطقه «الجیه» در شهر الشوف واقع در جنوب لبنان، ۴ نفر به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/akhbarefori/652091" target="_blank">📅 12:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652090">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8176e013.mp4?token=Jg09XGaIg8IotFvjftMi7mWwML_XeGjzaRwf83fkJT8jhWrKRVdgyKfmEYrQdwK1MSTY8bb7qa6mYHSI95uvdbkTiBADVo8sTN1s9LCF9ofuwoO6JZdmESHfxJ__oWnE8zpYO_MOnfCwJcO_8yPXDURC8GepXiROMUUicfQNQGLsVFQCiuuQEAvad9Iiu9CAsTXjzQhzuU3AL9vJGcPueXGG3EjuxCw7wYv2avUZ2Q8ly3hZkakhBqV2_8cIkWAshjVDMRB9cZimcMz7zfcEn4pJmkBejMn4S5Vp0cT4EnLza_eaODPcwfssYYneEZheOmjwhJOpwItQuH8HDf17iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8176e013.mp4?token=Jg09XGaIg8IotFvjftMi7mWwML_XeGjzaRwf83fkJT8jhWrKRVdgyKfmEYrQdwK1MSTY8bb7qa6mYHSI95uvdbkTiBADVo8sTN1s9LCF9ofuwoO6JZdmESHfxJ__oWnE8zpYO_MOnfCwJcO_8yPXDURC8GepXiROMUUicfQNQGLsVFQCiuuQEAvad9Iiu9CAsTXjzQhzuU3AL9vJGcPueXGG3EjuxCw7wYv2avUZ2Q8ly3hZkakhBqV2_8cIkWAshjVDMRB9cZimcMz7zfcEn4pJmkBejMn4S5Vp0cT4EnLza_eaODPcwfssYYneEZheOmjwhJOpwItQuH8HDf17iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابعاد گسترده ویرانی‌ها در پی حملات سنگین اسرائیل به «برج شمالی» لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/akhbarefori/652090" target="_blank">📅 12:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652089">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxSGvZX8EX3CMLLY99EhkbAVRrtlaSuoTzRGmp2fiK54zQCKQqZuvIFmX3rgxWsQeyRDmDHDSQQn6joOu7fLjNPf9-r6l1Qckc1_KXj1VHDg3m99y5CpzdGX1xPqVZanomqtUkkLa8f83dwo7FR87Ko0z2FWe-rx3BTNzobJUF5YEKluUb92CTTXcwQp7PZqEV5sxXokrC_abZcCI_eZ9PZRlaqas6ww1bwoFrqhMvYOUgocRXykA2NURM1LjkLgoh0qzJrTWIuZFKCjFAuUYZ8XG59TV-PC2Lux7WvKgqePnA4XBFOINMrMP0TnbTyV3u2vlV60XPEAo9hpisSy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاستیک کمتر، خرید بهتر
🔹
با انتخاب‌های ساده مثل کیسه‌ پارچه‌ای، ظرف چندبارمصرف و بطری شیشه‌ای می‌تونیم مصرف پلاستیک رو کم کنیم و به یک زمین پاک‌تر نزدیک‌تر بشیم.
🌱
شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
…</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/akhbarefori/652089" target="_blank">📅 12:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652088">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIcRJLZyeBmHm5DLY4HCeCxPo5pP-ANBxqSbTh-GUu9ygzYgQ68XIYCxK_0ZDbNBrW4DvThtaZ4smcMAFOZdERuwz2kLtsEkQ7BaHmoZEFltbOtir-c9bQhXniSvl5dcngJykC2V0-e3FLgftVszmLulQZVVeiONaZcD2Td-cWNgPJ4awsg201ZUx1mfs_EqizrGy1lTL-we9kTHKU6euCCNsVJpN20ziyLVQYX2ZArf27wxm1GhB7pbcQuzmM12pQLX_5BYiD6Wwlq7Z43EhAGA3RJCM1ImiV8L87wxJLrZmSGC7YceHug9KZkPjm-hgPUE29dyZlTnN7ORomjF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دعوای مجلس و مرغداران بر سر مقصر گرانی
🔹
نایب رئیس کمیسیون اصل ۹۰ مجلس، وزارت جهاد کشاورزی را دربارهٔ گرانی مرغ مقصر دانست که با وجود نهادهٔ کافی، جوجه‌ریزی کمتری در فروردین انجام شد و تولید را کم کرد و قیمت‌ها تا ۳۹۰ هزار تومان در هر کیلو بالا رفت.
🔹
این درحالی‌ست که اتحادیهٔ مرغداران، کمبود و گرانی ۵ برابری نهاده‌ها، خوراک،‌ واکسن و دارو را مانع جوجه‌ریزی اعلام کرده که تولید با هزینهٔ گران برای آنها صرفی نداشت.
🔹
بر اساس آمار اتحادیهٔ مرغداران، جوجه‌ریزی مرغداری‌های کشور در فروردین ۱۰۶ و در اردیبهشت ۱۲۶ میلیون قطعه است که این میزان افزایش جوجه‌ریزی ۴۲ هزار تن تولید مرغ را بیشتر می‌کند و نیاز ۱۷ میلیون نفر را در ماه بیشتر از ماه قبل تامین خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/akhbarefori/652088" target="_blank">📅 12:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652087">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
هشدار چین به آمریکا در مورد فروش تسلیحات به تایوان
🔹
چین امروز و پیش از دیدار ترامپ و «شی جین پینگ»، بار دیگر مخالفت شدید خود را با فروش تسلیحات آمریکا به تایوان اعلام کرد و از واشنگتن خواست به تعهدات خود در این زمینه عمل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/akhbarefori/652087" target="_blank">📅 12:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652085">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBfOCtZDrtZfWZ0TYmgR4vzenQc4DtV2gVpJ4kEchdxRZ1-3Z-pRd--m_MmQgf5PKSPx9tEIP2Qro_WJW5J9RCpm0ee6gBqoETZIS8RAIDgxtXdYVTA6-0kyllJjxl0Jkudu6upU09_uXDi6QOl99KOMtC2zbBesyWXrpWHciUNIDafG08pZ-a2yoe5oE1ykRHrMAVvAyTASKi9HsnAw978f5lUG3W1sYUsbuQ81KrtZMrk8Q4vBhQIbz_dDUBEodde7vfmClTirIIRO8_QcTpBxb0DGr-B49anmjeUnCKv8FkfSrGNNCIiA9yqszPq-tFaa3kgy7VUwO3x2bdlkRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uya0lzq4lzvgXyEERnK7EPfbCoOUFB3Kg5QSCLViNu7k0tfnVOAFPHAppGnSZ_fkUsYaj44sGPsG4ETKq15UR0dJxWlNvn5fDMmVRK3euHVNeyeq1cpq3PKg1F4bH_QqhY1aH_tYQKUFAaAjQ1alChWSbtd6Hvvulep2cpbVKcW0ALMW4mbENrBTRNWgF4BoGiXXWLPPz3fhxzh82Rpy0EAm5Vfsf3kTH6zRI0j8Tfr9-hFpRt4Hk0-Ojzr6Hijazsl8m7ma2KPgwfakj882kQz3APaswYZlCD7HODpcG843BfKoRqYj9wlPrZu94oev7T8i29WIhoOW578M1Fuosg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تداوم نقض آتش بس؛ حمله جنگنده‌های صهیونیستی به دو منطقه در جنوب لبنان
🔹
جنگنده‌های صهیونیستی لحظاتی پیش دو شهرک یاحون و برج الشمالی را در جنوب لبنان بمباران کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/akhbarefori/652085" target="_blank">📅 12:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652084">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36bd0aa3fe.mp4?token=NyZ1Sqyb9qp6v8j9B0tuB-d7l2m6CMGIUqhyl6pCRFoAMgfg3qJ5dBQt9ndu-pXvJ0xY_8rM4dY61UVCQwGSyD17UfJVh-MI3tY_QgI_fT_edJKRommDZEIYzQ_KnhYsR5DU8OLfTUPA2G4qDW4qlf9FrWdi3cjRJDSKBrb0ISiAuto5H0Isj0u2GatoJjJqJ_7DmfPxdlaaaaYXGkzNiMVlmw6npIF3OdZassf_0knL133jch6PWyCaHXZuJt1a1lSqAyf3B7eEzr2BgHEPHfV0tC48z85UcW-TBaoNNUZPxx5nyPdOHFF2Bx4yQmc8E3Af7yo8zFmrijoEsrYXQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36bd0aa3fe.mp4?token=NyZ1Sqyb9qp6v8j9B0tuB-d7l2m6CMGIUqhyl6pCRFoAMgfg3qJ5dBQt9ndu-pXvJ0xY_8rM4dY61UVCQwGSyD17UfJVh-MI3tY_QgI_fT_edJKRommDZEIYzQ_KnhYsR5DU8OLfTUPA2G4qDW4qlf9FrWdi3cjRJDSKBrb0ISiAuto5H0Isj0u2GatoJjJqJ_7DmfPxdlaaaaYXGkzNiMVlmw6npIF3OdZassf_0knL133jch6PWyCaHXZuJt1a1lSqAyf3B7eEzr2BgHEPHfV0tC48z85UcW-TBaoNNUZPxx5nyPdOHFF2Bx4yQmc8E3Af7yo8zFmrijoEsrYXQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی معاون وزیر بهداشت با هانتاویروس و تنگه هرمز
🔹
رئیسی: کشتی کروز که هیچی یک کشتی بادی هم نمی‌تواند از تنگه هرمز رد بشه نیروهای ما سریع می‌زننش و هانتاویروس هوا میشه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/akhbarefori/652084" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652083">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
رئیس روابط عمومی وزارت بهداشت: ۴۰ هزار نفر در جنگ رمضان مجروح شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/akhbarefori/652083" target="_blank">📅 11:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652082">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
مدیرعامل یک مؤسسهٔ‌ مالی با ۱۳ هزار شاکی دستگیر شد
🔹
دادستان مرکز استان کهگیلویه‌وبویراحمد از بازداشت مدیرعامل یک مؤسسهٔ مالی به‌اتهام کلاهبرداری و فعالیت غیرمجاز خبر داد و گفت: در این پرونده بیش از ۱۳ هزار نفر مال‌باخته شناسایی شده است.
🔹
این مؤسسه در ابتدا مجوز بانک مرکزی را داشته اما از سال ۱۴۰۲ بدون تمدید یا دریافت مجوز به فعالیت خود ادامه داده و این تخلف با گزارش پرداخت‌های گزینشی احراز شده است.
🔹
براساس نظریهٔ اولیهٔ کارشناس رسمی، ماندهٔ اصل سپرده‌ها حدود ۱۶۵ میلیارد تومان و مانده تسهیلات پرداختی در اختیار اشخاص حدود ۸۵ میلیارد تومان براورد شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/akhbarefori/652082" target="_blank">📅 11:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652081">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDqd-vl4mIr-oIhgWNhRfdAFRY2Gsdzj8lsxma_WkScknrJ02FwXqkGk1SjEw6X6an7747ZNo19zLODWKpXD3qH7UzWPdBtRCoqgyqcD86FH6xLd4CsqvNGoM-SwwFoyMshBNJO-uebTk9rGmsAJecF2-dHtldqxAWUZl-Q1MPch4hd0lPpxq0hbcQW6mAEp1t--ssMgbJbx95PX8E0_2lGGRLb1Ldi_OISA_Gdb2t6BJnoq-k1J2IL7XM4RFo7cVCwvCv6iB6sg-12sY0_Lqrkr3Z0x5WwmIy7YVsLHmR6ViSxcTB827ynIAtwknC5lwL9k49V9J0r5C6cgDA7ClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: ایران به ۳۰ سایت از ۳۳ سایت موشکی خود در تنگه هرمز دسترسی دارد
نیویورک‌تایمز نوشت:
🔹
اطلاعات آمریکا نشان می‌دهد که ایران قابلیت‌های موشکی قابل توجهی را حفظ کرده است.
🔹
ارزیابی‌های جدید و محرمانه می‌گویند که ایران به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز دسترسی عملیاتی دارد.
🔹
طبق ارزیابی‌ها، ایران هنوز حدود ۷۰ درصد از پرتابگرهای متحرک خود را در سراسر کشور مستقر کرده و تقریباً ۷۰ درصد از ذخایر موشکی پیش از جنگ خود را حفظ کرده است.
🔹
گزارش داده‌اند که ایران تقریباً به ۹۰ درصد از تأسیسات ذخیره‌سازی و پرتاب موشک زیرزمینی خود در سراسر کشور دسترسی پیدا کرده است. /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/akhbarefori/652081" target="_blank">📅 11:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652076">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flroLY5Lf0HxGsQj9R1zAFL6bv3chLgD9fk-HHw2rETXHqT4s_7IBfdsXSsAPQ2b8Ab9ppgHo8VveNfun6ttjcSjFBHV_CNgwpfIKwdU0mPXkIRTZhCWZv1nbAKMTBKaQ9rIXwe4jLVfFeEYU9ct-9066ZapXwRq2NXB3JEEwPQ68Ijp0_f1e8hzWC1fyCsVLRTGCtWMQ-3Zz-vl6D4Pbcd1AD-lMIc-GUIRg1dmwicWa7MB7mK1UN_ecdqNGzgbIkpVUSKozUCebyfbx_ekgp6H8PYPlCkVZ5oI_FKB7N4VcMzfzvfJBcrgoZvu7KhKnV1U77nSc2aXLZLYop73gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_fl7CnVC8rfLyOZLhOyeAlFmMKnxzYzYQmUX10kIaZ78gMMALvpIkjuyKIWuaZsZIutIHf47eKYzISMUSjbAcV-c1NGxhoC9IXF66QYrCu6bn4QHObIf78YMSn4XX0fact4Tu7tUJ7zdl0CKorLEenEXV8QKF2pDG0PXJbH8SzPd6HSzebgoiOrDWNgf-liv7tsDyOuN34iS8QuNENSKt5uZsvoVSBU-ltkfRdnIPcC54ftDVBTuIJiOD82XGbXImMaMaKWBFjO0H6JSmliA8yF2R93YrYrkSqbmCbRR4rofR6YLLKj6zsB-IjJ54wUG2C5kyXKnihNEsuewKGJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIRThvVD-Piy6pU0COZhqGYhrXoeKdU4VGKOheGDECGxe3-VX7RUWyU2XHzAB84BodYQOb4kSG8VUHwFa4TBwIpUCiU8_VPEw7YSSg1wxXtzoU0dHL64_aPuDwWK1Ze7CGRNyA-9i3p_YWSh67XhG-QOdldc8KJaBKAs2Popaxr_V7c8adAXOTAkaHz_Qhn6Ow5JscLJyFYiYo3rjLe6YRUk4ZSvtNb6YgyNRM9229limRt7J8DNf4JIXZ-o6B3ih8YM9a4OHqZuvjZc_qPSuUqzka-H35N7ZCQwimkzRCKhRNMha0kR7kK8aC50DUiqTKDgfg05GhHehMQsauII-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3q-VwZq6m760TCVtv9Ixk6QjFhXywkTy3QLNdyuBuU6gFvbeDVuaeD_4FneIV_2X8AvyZA20hrpPODVWDENLmliYDDViojC4BUGwBIxg9gxpwuxsHr6nFqcBy69EigYHN6DxqG03uygBOdGJ_xh53wgPVrTt_cXFoxa7Ukjp1qTAbrL-y1SzI8Gm_CBWCyY6anPKM1s3oNlney3P-YcbBgGmkWripM3UYGSIJVpV9z6OUett1jPoszusValc6mib9bRhvQJC7aaXtl1tU2hRVpQWUNN373rnU7KMaPm3XRwa7VGKU-6y_Lybcb5678iJBGDAiQzFVlqj_zFx_jjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dd26kMrG_JeCmuMuZZuiz1w7U8oirKf_1X1QpTP_AKbVNBU5o6SW96s9hbbiS3fOHpQUJcixukP3gwEm7NQ6rlby3fIESCQWM0Se9jJnYvevo9CAWBAtH8W34ZsxGwRtmoFlWH3y01nxHHNLJDuniFuoQyWfCC-aBMinbI7BZ9fmeG6R11ln_5utVcAnjtqLGSmmwH4BpdWATCT-oD8HqtJP_N8VwXiqSp5uKMDM-CgtArppTTs_gwMZF1EiSvlTdku0iMs_5UzUs4g27HnR7-GUoK47j4c2rH-auW83_YbINWXKaC30T_Vor95cT_sGNHc-F5f1HVm6fzIAjiomvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انتشار فهرستی از وطن‌فروشان خارج‌نشین توسط گروه علاج
🔹
براساس اعلام گروه علاج این افراد از حملات رئیس‌جمهور آمریکا به ایران تشکر کرده و نسبت به جان باختن برخی هموطنان ابراز شادمانی کرده‌اند.
🔹
علاج خواستار اقداماتی از جمله توقیف اموال، تعلیق خدمات کنسولی و سلب تابعیت این افراد شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/akhbarefori/652076" target="_blank">📅 11:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652075">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv6H4DyadBBBSWIKxV-sf8nbndsB56hwIdjzpydf-6V3Bh6_jKnldUbUMlyZ5-qd9ZKfr9QrmdSd_mku-D1_MziwsflMI8k9FD4aAPNu-tDTOidmaqtfSV3obrVX6__toL9VGjMrJyAnWe60f-ZbAP23LeUcsSwELTSgICAKlg3YS2Bav0ApIRZ7sOSJLezRE1kkDdM6oy1s-ODEeJz27S604InyJO4G5ugbF5P83JNIcv9hyHJxGXVqhGF0MpKCLYZyyYh0eXiooQ0VkokyjlhC_j8Xzp6uBrjqUJ-mE2K2Z2RSevPsQSztg4pFn8MyPWvTccU_jZxYEHENNUaEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار ۴۰ روز جنایات آمریکا و اسرائیل در ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/akhbarefori/652075" target="_blank">📅 11:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652074">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207f1553c1.mp4?token=ajeQ4bvgBx1LtSy2bSAxmy4aBjIStloGoBUTdQcOg4ebnmW_HGPXz-UFqXwAmRGtbEwyDgh_mut58mWPmQhdZkGZ8prCuDtyr3WIaB-0z093XBkPDXZoEocifQhokGgyKMRqjlXKad3Dp9ZU7lBQNJKJD55kZ6Pb8B5iAQm778YcUCtZOpYOJ3JsZIfaoVsFumJjsa4TXS3CTU7f6sIAv2ffENrsQXXWHMmCtuRtuhZd-iRwyN4WbgoLOVbqthJ_V96ReUU5LTuKCRdDuWCRfzAHPsfXBbwCxP8li4pahInpBXlOxC33S8pOR5omp1BpUCQZjew9bAExIDWNglt6UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207f1553c1.mp4?token=ajeQ4bvgBx1LtSy2bSAxmy4aBjIStloGoBUTdQcOg4ebnmW_HGPXz-UFqXwAmRGtbEwyDgh_mut58mWPmQhdZkGZ8prCuDtyr3WIaB-0z093XBkPDXZoEocifQhokGgyKMRqjlXKad3Dp9ZU7lBQNJKJD55kZ6Pb8B5iAQm778YcUCtZOpYOJ3JsZIfaoVsFumJjsa4TXS3CTU7f6sIAv2ffENrsQXXWHMmCtuRtuhZd-iRwyN4WbgoLOVbqthJ_V96ReUU5LTuKCRdDuWCRfzAHPsfXBbwCxP8li4pahInpBXlOxC33S8pOR5omp1BpUCQZjew9bAExIDWNglt6UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر بهداشت: سیر نزولی جمعیت‌ها ادامه دارد /  ۸۹۲ هزار در سال ۱۴۰۴ تعداد متولدین ما بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/akhbarefori/652074" target="_blank">📅 11:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652073">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OarH9fEf2KT9c3AEB6jqmcegpHhcW4LZD5kCR85rs7LcmLyQIl88-PL5FUzg_VS0477AHgXNyIr95fsUairOqJYu4PWGuqNE0babToIYL9QKnBYwe1CB7H-NsUgzIOKPQco5nKVTvlCCb-edmw-ARwxoFcmNTzwseXGoIBFz7QU8mmdmBZgY_ItstMZwVo67FzAgkWj9WPfgnK-cbaA3co4k38xr_1xiiYDh2QTyKGFboMFZUFmbGZY5LtNBn4fwauAvt3bYsn6NuqiXgYb5Kooa5LuDwpjtqYLJy8zSXUrjoFyeos5KrnOy9oh5njodyJNkheYLTZw_PHHxHIF_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاوروف: تهاجم علیه ایران با هدف جلوگیری از عادی‌سازی روابط با منطقه بود
🔹
وزیر خارجه روسیه: شکی ندارم وقتی این برنامه‌ها برای حمله به ایران از سوی اسرائیل و آمریکا انجام شد، یکی از اهدافش جلوگیری از عادی‌سازی روابط بین ایران و کشورهای عربی بود.
🔹
در دوران دونالد ترامپ، مقامات آمریکایی حرف‌های درستی در مورد همکاری با روسیه می‌زنند، اما در واقع، واشنگتن همچنان سیاست جو بایدن را دنبال می‌کند.
🔹
ایالات متحده خواستار باز شدن تنگه هرمز است، تنگه‌ای که قبل از دخالت واشنگتن، در واقع به روی کشتی‌ها باز بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/akhbarefori/652073" target="_blank">📅 11:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652072">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5575ee58cf.mp4?token=RdkB6xBlwA2aX24c6r6iIMHshhmyw-Ln11l2TfKFGwSZkjVpH8ziLTc99_jVlBRbl25QN2jHd-VyOz3X9bE2d83AT-kr7fP56xHpL_Szjy1NAf0QUq8PRQtlWFHqNNYY73eBpUXLbH7dC7qRZ03KCA33elG441L5HifQbe9GizyjBawZbpjzxPOAl1C6cMSY9Esw_s5fPKazhE341L1WiFQ0CZiaGKnAsln2LvzIaHqfjsUtHTWzuCPvuqKrOqLl9m9r_DYV-Uax8XKp46stNr3jedShYW2NzCHFksxGaPjj3d5e5JFdpWedxpMMqgjmQfzlieEXRy2xYcQbyhcsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5575ee58cf.mp4?token=RdkB6xBlwA2aX24c6r6iIMHshhmyw-Ln11l2TfKFGwSZkjVpH8ziLTc99_jVlBRbl25QN2jHd-VyOz3X9bE2d83AT-kr7fP56xHpL_Szjy1NAf0QUq8PRQtlWFHqNNYY73eBpUXLbH7dC7qRZ03KCA33elG441L5HifQbe9GizyjBawZbpjzxPOAl1C6cMSY9Esw_s5fPKazhE341L1WiFQ0CZiaGKnAsln2LvzIaHqfjsUtHTWzuCPvuqKrOqLl9m9r_DYV-Uax8XKp46stNr3jedShYW2NzCHFksxGaPjj3d5e5JFdpWedxpMMqgjmQfzlieEXRy2xYcQbyhcsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر بهداشت: مسئله جمعیت از جنگ مهم‌تر است
🔹
رئیسی: اقتدار ملت است که روی آن تکیه می‌کنیم؛ شهدای جوانی که پشت پدافند می‌نشینند با اینکه می‌دانند شهید می‌شوند باز حضور دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/652072" target="_blank">📅 11:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652071">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0797785fb.mp4?token=WGwKCaq9EWkMTsHrkXXf6bnW1O8M4qhXn-gCsqkKXj70hATxT_kxUeewgQHglp5ynuqEjH3EbumbDNl257GtMwLNIspigf-d8ldWWjyhMq-CdyQ9IaxqBVljrJ0JIWblCHA4qtpRRQczA_kc9lo8lEqfEzN32KKizFhHIaTiQ2vu84RB2RiTw8rApCT8-VKxZKQES2Nzo4CDFQm81StYYjFyhJFE-G-qNC6DzL2YAKKqspz0vLHylQbkjbe_xxjOJ9tzDXercBNNSZiI1GGHyfz8vcRaHVqJsjqX5Zwl-Zj6eGwnZ5UOw6MKsoWKopQ2sPxEUuFiyDXzGS72Zpoz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0797785fb.mp4?token=WGwKCaq9EWkMTsHrkXXf6bnW1O8M4qhXn-gCsqkKXj70hATxT_kxUeewgQHglp5ynuqEjH3EbumbDNl257GtMwLNIspigf-d8ldWWjyhMq-CdyQ9IaxqBVljrJ0JIWblCHA4qtpRRQczA_kc9lo8lEqfEzN32KKizFhHIaTiQ2vu84RB2RiTw8rApCT8-VKxZKQES2Nzo4CDFQm81StYYjFyhJFE-G-qNC6DzL2YAKKqspz0vLHylQbkjbe_xxjOJ9tzDXercBNNSZiI1GGHyfz8vcRaHVqJsjqX5Zwl-Zj6eGwnZ5UOw6MKsoWKopQ2sPxEUuFiyDXzGS72Zpoz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم نقض آتش بس/ دومین حمله پهپادی اسرائیل به جنوب بیروت در کمتر از یک ساعت
🔹
منابع خبری از وقوع دومین حمله پهپادی رژیم اسرائیل به یک خودرو در بزرگراه ساحلی «الجیه» خبر دادند.
🔹
این دومین بار طی ساعات اخیر است که پهپادهای اسرائیلی خودروهای عبوری در این محور مواصلاتی استراتژیک در جنوب پایتخت را هدف قرار می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/akhbarefori/652071" target="_blank">📅 11:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652070">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0412efd61.mp4?token=qMq5JxwYF9B3Md-XGM42KjiyCSE_HR1nxOAh2EXv45yqG9yJNu5jbgp0IE9oVGv5zw9JPPyUeR7njSYOHiue-GPIsClGyvf3SqLmelAGJ0u57CNhlRbNGJnjsxgMdiO8rbwNTqTONv6mokRAFsLfsLLRCkvV8pjaOuiW9Ngphg4NIquTr9ViwxjHSKkQPFIZ1zNRSq0H2KdIFbwJU7Px6-F4jnMaGP0qF_hbr-WXEOnye9XODRHdOv6fRpjU2uLWeI1pDFyfc1hyBJAzB0UAZ2yyyfn5vBtUeSbr9PWtQspjTNC0Ffdbe-kCiB1xj1znC5XTKATj8qb6PU7fl2t1cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0412efd61.mp4?token=qMq5JxwYF9B3Md-XGM42KjiyCSE_HR1nxOAh2EXv45yqG9yJNu5jbgp0IE9oVGv5zw9JPPyUeR7njSYOHiue-GPIsClGyvf3SqLmelAGJ0u57CNhlRbNGJnjsxgMdiO8rbwNTqTONv6mokRAFsLfsLLRCkvV8pjaOuiW9Ngphg4NIquTr9ViwxjHSKkQPFIZ1zNRSq0H2KdIFbwJU7Px6-F4jnMaGP0qF_hbr-WXEOnye9XODRHdOv6fRpjU2uLWeI1pDFyfc1hyBJAzB0UAZ2yyyfn5vBtUeSbr9PWtQspjTNC0Ffdbe-kCiB1xj1znC5XTKATj8qb6PU7fl2t1cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر بهداشت: ۲۴۵ مرکز ما در جنگ آسیب دیده است
🔹
رئیسی: بیشترین سهم مراکز آسیب دیده وزارت بهداشت را کرمانشاه با ۴۸ مرکز داشت.
🔹
۵ نفر از همکاران ما در جنگ شهید شدند که یکی از آنها مادر باردار بود.
🔹
کمتر از ۴۸ ساعت در تمامی استانها همه مراکز آسیب دیده جایگزین شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/akhbarefori/652070" target="_blank">📅 10:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652069">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
اژه‌ای: هدف اصلی دشمن؛ ایجاد تفرقه و ناامیدی است
🔹
رئیس قوه قضاییه: انسجام ملی؛ اصلی‌ترین سرمایه در جنگ ترکیبی است؛ هدف اصلی دشمن؛ ایجاد تفرقه، ناامیدی و فرسایش سرمایه اجتماعی ملت ایران است.
🔹
امروز بیش از پیش ضرورت عبور از رقابت‌های سیاسی و اولویت بخشی به همکاری و مسئولیت‌پذیری ملی اهمیت دارد.
🔹
امروز؛ نقش مردم در تبدیل تهدیدها به فرصت‌های پیشرفت و اقتدار ملی بی‌بدیل است، ظرفیت‌های گسترده دینی، انسانی، طبیعی و اقتصادی ایران برای عبور از شرایط ایجاد شده از سوی دشمن کم نظیر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/akhbarefori/652069" target="_blank">📅 10:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652068">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMpBQVAoLJgLXsZJyCzPsMaCbp5xZtdTN5pYKEBhlew9XWay6YRaRuCVvE8JAjo-c8Z3Cq7_7079gOU1lTSKN1TWJWMZgnpdZtBNR5Y_ngddsYrg3lDcuSTKnnp_U4Hyh5hWdy1ovQhH0frOWJRkf4xtDm88EGK-_OszpuArhGKBX6xGWKS7yLLJdO0VRdNvKPoplQz-IiiHTUdFHVSA_7LqVyc-6FO_N5zFG9WkLlXu4cosFsiT6hiYkGbPJd3mHCdpl2aGfnxpd3ZVUFjnCoJNG8nGX1n2IJ0tMNDLV3LYvHaaJpaZOWS4wKt6s8UMtPd_1Uv_nRXHVgoiBJmzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تدارک صهیونیست‌ها برای برگزاری راهپیمایی تحریک‌آمیز پرچم
🔹
رژیم اشغالگر صهیونیستی در تدارک برگزاری اقدام تحریک‌آمیز «راهپیمایی پرچم» با حضور حدود ۵۰ هزار شهرک‌نشین در قدس اشغالی است.
🔹
این راهپیمایی از بخش غربی قدس اشغالی آغاز می‌شود و با عبور از باب‌العامود ادامه خواهد یافت و این راهپیمایی معمولاً با سر دادن شعارهای نژادپرستانه همراه است.
🔹
اشغالگران همچنین خود را برای یورش‌های گسترده به مسجدالاقصی آماده می‌کنند. پیش‌بینی می‌شود تعداد یورش‌گران از رقم سال گذشته که ۲۱۰۰ شهرک‌نشین بود فراتر برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/akhbarefori/652068" target="_blank">📅 10:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652067">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf1f551d1.mp4?token=cfKiAgOl1-H5Sduf2_LCuzrjKNZciOEzHwH4SHw8VHKWgTXV2JafZpILj8slZJz0gP81PHzUK6gRqL7HxaSJgINk9XbjdW7C-e09LZh4nQ1WHjqrzfGfedsAzt99BQeSVBL8vz1s4MZ5hLt1yZo7IJHsv9vYNTPECUgyhYGrsj_aUywvMhYjSL99W8nR9dwDsS_058nZH31Oyh8d6Dd6GhZELQWJgApX26CUYITedKgkJqS3Q3DMcWCvxVJXPnTXxV0mTMC8OWd5iwmn1t70O_SGQ9b2ATJaNiFthKQGfxfSq8_MT6UuDqJFZQSeUWhyMTVtlI6fUYT1lLeFCNk7mKk0LQpMgeASIg1_k7Mav3e6Wyz2sidWa2mARy_qQNRTMtz-3UP-CjvNMCgJlI-ktidZZLjymiCaVkdF6dzUzInUNmzHPTVfYPI14Jzpkn7ZRXkZGpFgNiL8soHMaN7BS2mbcMEnHg4jgWuOByQATWfInXlAztYNbqUnvOSEkdEQEhpenFwt5hw2q61WZfGQJA9mmAQgvhrH5AH_ACZBv08uOaxSmd7uCCkpGaVyq_bZbJ4FAbIKca6ILPlAapdKYEHhGhxmO6ouh8nvM6QdevcZc_iWip-v4Dknr5xUTTlJB2auIIOFMuGGW7qsnmwqMJl3QkYERhTZjy_rXb2EY2s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf1f551d1.mp4?token=cfKiAgOl1-H5Sduf2_LCuzrjKNZciOEzHwH4SHw8VHKWgTXV2JafZpILj8slZJz0gP81PHzUK6gRqL7HxaSJgINk9XbjdW7C-e09LZh4nQ1WHjqrzfGfedsAzt99BQeSVBL8vz1s4MZ5hLt1yZo7IJHsv9vYNTPECUgyhYGrsj_aUywvMhYjSL99W8nR9dwDsS_058nZH31Oyh8d6Dd6GhZELQWJgApX26CUYITedKgkJqS3Q3DMcWCvxVJXPnTXxV0mTMC8OWd5iwmn1t70O_SGQ9b2ATJaNiFthKQGfxfSq8_MT6UuDqJFZQSeUWhyMTVtlI6fUYT1lLeFCNk7mKk0LQpMgeASIg1_k7Mav3e6Wyz2sidWa2mARy_qQNRTMtz-3UP-CjvNMCgJlI-ktidZZLjymiCaVkdF6dzUzInUNmzHPTVfYPI14Jzpkn7ZRXkZGpFgNiL8soHMaN7BS2mbcMEnHg4jgWuOByQATWfInXlAztYNbqUnvOSEkdEQEhpenFwt5hw2q61WZfGQJA9mmAQgvhrH5AH_ACZBv08uOaxSmd7uCCkpGaVyq_bZbJ4FAbIKca6ILPlAapdKYEHhGhxmO6ouh8nvM6QdevcZc_iWip-v4Dknr5xUTTlJB2auIIOFMuGGW7qsnmwqMJl3QkYERhTZjy_rXb2EY2s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به سالن خاطره‌انگیر ۱۲ هزار نفری آزادی؛ مصداق جنایت جنگی/ میزان برآورد خسارت بر اساس قیمت دلار و طلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/akhbarefori/652067" target="_blank">📅 10:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652066">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b3806e94.mp4?token=EpxGHF7w4hbnMht8MfT2wqKaP0I4RJv4ev_JUQvYSjqqfFT_z2Rbd0WllNIOSLVHcQzV5K3gllZrdQjec--Kymct17n9Gzg8UsEDNwD6JRfhMRq8L2wMhtUQqbJn3HWP9Euuqp9Sl0lbhNekfKrF3vorv4V9HOZ_Iqp-sb8FEwiLchnSxcT5n-AUJXhChCYziyK7gfLvwBrvc9S0YDjf-PDRsDusuF8-anySFO-3_DEPhpHUAJZXxY4v83Z4EZ-6PnckUflLTCqc7ZJ2AbCevotOWN7G4qVGl5BdAoYeNaar3fgpaXAm-GioUnX67ZYPhuRzvH-lWuBxWfE6v3YxRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b3806e94.mp4?token=EpxGHF7w4hbnMht8MfT2wqKaP0I4RJv4ev_JUQvYSjqqfFT_z2Rbd0WllNIOSLVHcQzV5K3gllZrdQjec--Kymct17n9Gzg8UsEDNwD6JRfhMRq8L2wMhtUQqbJn3HWP9Euuqp9Sl0lbhNekfKrF3vorv4V9HOZ_Iqp-sb8FEwiLchnSxcT5n-AUJXhChCYziyK7gfLvwBrvc9S0YDjf-PDRsDusuF8-anySFO-3_DEPhpHUAJZXxY4v83Z4EZ-6PnckUflLTCqc7ZJ2AbCevotOWN7G4qVGl5BdAoYeNaar3fgpaXAm-GioUnX67ZYPhuRzvH-lWuBxWfE6v3YxRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یکی از پرستارهای بیمارستان میناب که دو فرزندش دانش‌آموز مدرسه شجره طیبه بودند
🔹
کرمانپور، رئیس روابط عمومی وزارت بهداشت: هشت نفر از کادر بهداشت و درمان در حادثه میناب فرزندانشان را دست دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/akhbarefori/652066" target="_blank">📅 10:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652065">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رهایی ۳ گروگان و دستگیری گروگانگیران در خاش
🔹
فرمانده انتظامی خاش: در پی گروگانگیری به قصد اخاذی، پیگیری موضوع به صورت ویژه در دستور کار پلیس قرار گرفت.
🔹
کارآگاهان پلیس شهرستان خاش موفق شدند با انجام اقدامات تخصصی و شگردهای پلیسی محل نگهداری گروگان ها را شناسایی و در عملیاتی منسجم و غافلگیرانه ۱نفر از گروگانگیران را دستگیر، ۳نفر از افراد گرو رفته را آزاد نمایند.
🔹
افراد گروگان گرفته شده از شهرستان های مشهد، ایرانشهر و خاش بودند.
🔹
یک قبضه اسلحه کلاشینکف به همراه ۳ تیغه خشاب حاوی مهمات مربوطه، یک جفت پلاک خودروی سرقتی از متهمان کشف و دستگیری سایر گروگانگیران نیز در دستور کار می باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/akhbarefori/652065" target="_blank">📅 10:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64f1c12a4.mp4?token=EKJGiP4BDwM93XbzBGsfL-CtYvIQTUz7YCxdotIiP-21rcpkTPyDsujC0YoknknmZQF22ioHhElVDn8FvYWVuHZ452jcAFolqZu0P7sP7qoRvgGvhyTxgpCZri01loAt0kPHLpbC5gT8yOflpaGLj7G8oBdggikk9JU8LURSb-lDjncVkJwyJ8j0tzCtH_V0nG9YwsG7PMhdFxjtMQwS669W44TZTchKjI8J6U5NMEoXcIpm-pXV9Eo5mtgD5FmQUTuNYgRyHSbseJMGER70RykrYTfznRvo_WzeM4ZxSDIfzIbRweRXGkELcL3l1im5N5_ZiyXKbvhIcvXdxip84g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64f1c12a4.mp4?token=EKJGiP4BDwM93XbzBGsfL-CtYvIQTUz7YCxdotIiP-21rcpkTPyDsujC0YoknknmZQF22ioHhElVDn8FvYWVuHZ452jcAFolqZu0P7sP7qoRvgGvhyTxgpCZri01loAt0kPHLpbC5gT8yOflpaGLj7G8oBdggikk9JU8LURSb-lDjncVkJwyJ8j0tzCtH_V0nG9YwsG7PMhdFxjtMQwS669W44TZTchKjI8J6U5NMEoXcIpm-pXV9Eo5mtgD5FmQUTuNYgRyHSbseJMGER70RykrYTfznRvo_WzeM4ZxSDIfzIbRweRXGkELcL3l1im5N5_ZiyXKbvhIcvXdxip84g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا کالاهای اساسی گران می‌شوند؟/ تشکیل کارگروه ویژه برای بررسی قیمت‌های کالاهای اساسی
🔹
نادری عضو هیئت‌رئیسه مجلس: ما به طور مداوم پیگیر افزایش قیمت‌های کالاهای اساسی هستیم و قرار است یک کارگروه مشترک برای بررسی افزایش قیمت‌ها تشکیل شود.
🔹
در جلسه با وزیر جهاد کشاورزی این موضوع بحث شد که چرا بعضی از اقلامی که با معیشت و سفره مردم سروکار دارند، باید گران شوند؟ در حالی که بیشتر مواد اولیه کالای مایحتاج مردم در داخل کشور موجود است. هرچند ادعای وزیر جهاد کشاورزی وقوع جنگ بود، اما برای ما قابل قبول نیست. بنابراین، ما به طور مداوم پیگیر افزایش قیمت‌های کالاهای اساسی مردم هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/akhbarefori/652064" target="_blank">📅 10:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652063">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3580e63b79.mp4?token=jqnfd7kIy3mYwzTaA3508ONStlpD7OMnz3hHAuHxx4huLmA3r9IZrsS4Icocr3wEGE88Z1zuN9ZduE8JxMRD8AjHfINm-iTNePPp5v4YFrkhaEZENYBTxtlDbl6CHvvIxmp5xRLNgsdIWDUq6Uedqb0sYiP1rS-9S8JIOXjwME08FLSvZllHLL3FU3B1bIoLo588nlCUfWT1JjsuiOhc17wUsEE6CaQyg9f9d4vq_qKsRdy84CMbP6wGx4mrv5SzGzJ5IfSyZ-LO5-fMR8D69dm-FaXbz_SxKFJ7z8sWAEiN8q-MtEohLh8tQhX3cpAuMnKkmm2c7kpm_Wxdfc3v-qxrDvxlUtfbJrYxHofE_16t6MUXmADw5fShj9MFTyIXtq6ew4wiJJNdA-1zc5QPBc7nFmDs0eOyHQi_oahXEaVDrRX0N940afVXD5ekNCqrLtw4OT96zc9XeLDD4VI1u4Rzuy9-a9jfzqq9AZCvUdEWq12hBalU3XAJzGEoPm6iLfSwNWp5SC3fXTnjIsS8CFLwFB542MoHlGrvcOfFLh3b4v8kJ6XWQOCijDdNNrOP_A2mmOUa6nfJH4vUGdDRXJKR1Qz9Y4PWH1v0udaU_At1gYC2MpZ0AkcoufqjsmHoLDg6cSilGJ5puHnYNJBWPx7xJEcgESaqFl4oHoOatJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3580e63b79.mp4?token=jqnfd7kIy3mYwzTaA3508ONStlpD7OMnz3hHAuHxx4huLmA3r9IZrsS4Icocr3wEGE88Z1zuN9ZduE8JxMRD8AjHfINm-iTNePPp5v4YFrkhaEZENYBTxtlDbl6CHvvIxmp5xRLNgsdIWDUq6Uedqb0sYiP1rS-9S8JIOXjwME08FLSvZllHLL3FU3B1bIoLo588nlCUfWT1JjsuiOhc17wUsEE6CaQyg9f9d4vq_qKsRdy84CMbP6wGx4mrv5SzGzJ5IfSyZ-LO5-fMR8D69dm-FaXbz_SxKFJ7z8sWAEiN8q-MtEohLh8tQhX3cpAuMnKkmm2c7kpm_Wxdfc3v-qxrDvxlUtfbJrYxHofE_16t6MUXmADw5fShj9MFTyIXtq6ew4wiJJNdA-1zc5QPBc7nFmDs0eOyHQi_oahXEaVDrRX0N940afVXD5ekNCqrLtw4OT96zc9XeLDD4VI1u4Rzuy9-a9jfzqq9AZCvUdEWq12hBalU3XAJzGEoPm6iLfSwNWp5SC3fXTnjIsS8CFLwFB542MoHlGrvcOfFLh3b4v8kJ6XWQOCijDdNNrOP_A2mmOUa6nfJH4vUGdDRXJKR1Qz9Y4PWH1v0udaU_At1gYC2MpZ0AkcoufqjsmHoLDg6cSilGJ5puHnYNJBWPx7xJEcgESaqFl4oHoOatJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خشم سناتور آمریکایی از میانجیگری پاکستان در مذاکرات ایران
🔹
سناتور لیندسی گراهام در جلسه استماع کنگره آمریکا با لحنی تند و بی‌سابقه، پاکستان را به نقض بی‌طرفی در مذاکرات صلح متهم کرد و ادعاها درباره هواپیماهای ایرانی در پاکستان را تکرار کرد و گفت اگر گزارش‌ها درباره پارک هواپیماهای ایرانی در پایگاه‌های پاکستانی درست باشد، واشنگتن باید دنبال میانجی دیگری بگردد.
🔹
وی در جلسه استماع کمیته نیروهای مسلح سنا با حضور دن کین فرمانده ارشد نظامی و کاتلین هیکس معاون سابق وزارت دفاع برگزار شد، از کاتلین هیکس پرسید: «اگر میانجی اجازه بدهد هواپیماهای شناسایی ایران در پایگاه‌هایش پارک شود، این با منصف بودن یک میانجی همخوانی دارد؟»
🔹
هیکس گفت نمی‌خواهد خود را «وسط این مذاکرات بیندازد»، اما گراهام با صراحتی کم‌نظیر پاسخ داد: «خب، من می‌خواهم خودم را وسط این مذاکرات بیندازم. من به پاکستان اصلاً ذره‌ای اعتماد ندارم.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/652063" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652062">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0mTT_5oYzkMNaRLgzflhwQtyEOQtJT03ZUHZXFD_R14Q0dFkQibqUxoSB7F0HIx-OErOj2qkwNmv5sPXCXf2mV4PTCuAe3TSSdRE3wuA_U8Db_B4-En10PTUbgybHsYriQc-ATBCC-hVW7tWBJ3EvIQN0tldj4JIPsrb-IvOa-KiZIWoJ8BWQ0FkmiowRnLIB8m5fdTGk4XAPBb2NMU4h2fXSJ75A-FmRFROP2Uxwg5OWQAUtu-x_wrJnFYJNsknzJZOuY_nqBR6A1cn7hE-aI_z2T21bweZP1VEXTuX9yYh-XxGApcM8gETVzbha6_GIqFYYQjOHTSYeTqhoxeGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلزله‌های بزرگ استان تهران
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/akhbarefori/652062" target="_blank">📅 10:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652061">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
متهم در یکی از واحدهای مسکونی محدوده چیتگر تهران مستقر بود و اطلاعات مربوط به محل‌های اصابت در جنگ رمضان را به شبکه‌های ضدانقلاب منتقل می‌کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/akhbarefori/652061" target="_blank">📅 10:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652059">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1pvFnpr9PkGm0_MWdI0fbO2ThX8SykJEexQeFTgJK3dsG1oN34-Mj8TobUVK2WvItJ4ZMI8_eldFtaoByLF-kAmY0L6_TFV-Ky0dJQfb3QdMChmy1WWYgC99-P6xnUT3n6Wyuo6-H63KInDztdxU1bx-ec57Kacuh_Lb_1tWX_7vlp9XfMMaQGmVlN8fMW5s-_aw0Byl7Hp9OTJi_WPXJDG8a3sFRS2DYEMtlgC8xRmMvbuzHEt6PpjWIaROdhrXCmqlafoBskhpauEcgBcIuXKddTZPCxDS2L5Xkbd4IT8pG26uP4B-7SD1_TZXTlJeN1897mPl3YYhwV7Nc3pUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفتالی بنت: کابینه نتانیاهو ارتش اسرائیل را تضعیف کرد
🔹
نخست‌وزیر پیشین رژیم اسرائیل، گفت کابینه فعلی، ارتش اسرائیل را تضعیف کرده است و ادامه جنگ، کمبود در شمار نیروها و فرسایش میدانی فزاینده را آشکار کرده است.
🔹
نفتالی بنت که «شکست ۲۰۲۳» در عملیات «طوفان الأقصى»، به تغییری سیاسی بزرگ منجر خواهد شد؛ تغییری مشابه تحولی که اسرائیل پس از جنگ اکتبر ۱۹۷۳ شاهد آن بود.
🔹
نفتالی بنت، کابینه بنیامین نتانیاهو را مسئول شکست امنیتی آن روز دانست و گفت کابینه کنونی از این حمله درس نگرفته و همچنان اسرائیل را بر اساس «همان رویکرد» اداره می‌کند؛ رویکردی که به فروپاشی نظامی انجامید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/652059" target="_blank">📅 09:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652058">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr-V6yU3RYE2JK_psLpriDvISxLYQShPLmxuUZ0n7c-9r5R36ms5WvtOb4SVy1LUewS4ijHSFrT9toz2IjJh4nJ6KlGIIlZwVu7ksRo93tKCxdPupJxA5-YTG3KG5zM0n4PPIf4ZK7HP6H67g0mBhYEZr7Y6oOIMUjMtkMKcVrCP9vfB1QsIIY_eLITq54oGCMA-b-dJIpJonMEAtg0hmY_8oL0EcRvIdx28J_c7FZeBJXlUL2EWa924Xtj5vUmfkr-FmFk1-rEsvND60mfmeEaYDfr9MeFYuNSbm4LfkUBgTYb57DWM31Wu74W6jARZBL3kl64fA7msUTPgQY6ALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر پلاستیک در کیف‌ مدرسه‌ دانش‌آموزان
🔹
پلاستیک‌های کوچکِ مدرسه، زباله‌های ماندگارِ طبیعت؛ تغییر از کیف دانش‌آموزان شروع می‌شود  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/akhbarefori/652058" target="_blank">📅 09:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652057">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnU_BZmtyVi4_bNfTPmp51JL0Z4nv4cAFAjEauA-a2FLwAW5BRJfMIIbfrw1f-QzbWDryZeTGzLH3Wurny-3rR_9PUGS2IlTeXaLB3ZYjU4cHY-alX4CXMD-ciFdfES8iTon_KnxZJ0mAEoTpSoiMLGKDgaio29PjkACvs2KH_pWRj2dSQ5rkvLjyWsTwzbRThbXBC3HdUEgDSqyUJzhqq8htKsObE1bDFOm3Tw2ej6b3oBwN9DB5pHzTq_3qrsAKy8Loadoo8SOY-vJpw0G_PfEN5sRKaD4ch-dUBHshCfu4gOsFHr0ozEDS0yPRZwFwyVuA9MtBtMZDef2iZHDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلیه خریداران ورق گرم فولادی مکلف به عرضه محصولات خود در بورس کالا خواهند شد
🔹
بنا بر شنیده ها از ماه آینده کلیه واحدهای خریدار ورق گرم فولادی، مکلف خواهند بود محصولات خود را در بورس کالا عرضه نمایند. این تصمیم مراحل پایانی مصوبات قانونی خود را میگذراند و در روزهای آینده ابلاغ خواهند شد.
🔹
به نظر می‌رسد پس از بالا گرفتن قیمت ورق و کشفیات جدید ورق‌ها به صورت انبوه در انبارهای غیررسمی توسط نهادهای نظارتی، این تصمیم با فوریت ویژه اتخاذ شده و اجرایی می‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/652057" target="_blank">📅 08:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652056">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
احسان افرشته، جاسوسی که در نپال توسط موساد آموزش دیده بود و اطلاعات حساس کشور را به اسرائیل می‌فروخت اعدام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/akhbarefori/652056" target="_blank">📅 08:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652055">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
آیت الله عاملی، عضو مجلس خبرگان رهبری: اغتشاشات و کودتای دی‌ماه، آغازگر جنگ رمضان توسط دشمن آمریکایی- صهیونیستی بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/652055" target="_blank">📅 08:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652054">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTAXRtRo3AFPkGHdP6X5ZjpmnsCQcdtdnXkIBinPE6QzmQorAKj_5n65_xu9pAzDTQObW4yU017CmtNLYndXMTb13nw2kHElphLESDI5Q01VENGxICdoWk3PD55FqZTUr1KD4Bwx-FnNKEQaObx6Z-4JOFOzPTRYnsreI6v3ngECjqjGrArOU83IZeqLO1Zlytfi8TDRsps6HErgjysH5_j0dBsyZLAJVON4QIQvOyhd-NcNNpHlx3e4GYs_Ml8WxlH4xR7bwYhG5Kcr2a69O-zz6HTtN7DF0Me53OWMAhMbiDfwBsWfBfBfHo-vVDqteCFxnGLnlncV08vaMVouuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازداشت معاون دبیرکل سازمان ملل در فرودگاه اسرائیل جنجال دیپلماتیک به ‌پا کرد
🔹
روزنامه صهیونیستی یدیعوت آحارانوت گزارش داد که سازمان امنیت داخلی رژیم صهیونیستی (شاباک) صبح امروز (چهارشنبه) ژیل میشو معاون دبیرکل سازمان ملل متحد در امور ایمنی و امنیت را هنگام ورود به سرزمین‌های اشغالی بازداشت کرده است؛ اقدامی که به گفته این رسانه صهیونیستی موجب ایجاد بحران دیپلماتیک برای رژیم اسرائیل شده و این رژیم را در وضعیتی دشوار قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/akhbarefori/652054" target="_blank">📅 08:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652053">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سی‌ان‌ان: اسرائیل نگران توافق آمریکا با ایران است
🔹
شبکه خبری سی‌ان‌ان در گزارشی نوشت که تل‌آویو نگران است آمریکا بدون رسیدگی به مسائل مد نظر این رژیم، به توافقی با ایران تن دهد.
🔹
یکی از این مقام‌های رژیم صهیونیستی گفت: یک هراس واقعی وجود دارد که ترامپ به یک توافق بد با ایران دست یابد. (رژیم) اسرائیل با تمام توان خود سعی دارد بر این امر تأثیر بگذارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/akhbarefori/652053" target="_blank">📅 07:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652052">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcRIgcTIFhsT-iYbsTRqH3KvZgLLCOJvnUVBd0G_cXKMa7mMx46LIKcj0UdaSDYZKW2gxuqQ_dHsBgqu5pzPgSLilYBIR02ZRs6ISU11mOrVa5jek76653l0wsmjyiqc9QAiMshdBKYQGHk29kbWhAh8roaToQWvVnREpg3kEVYOyqoJ4a0AEvte6LAq_ToFS5iKirR3jvUAYdbtaGp2WShd2ZhSQIGo2xAmAmMs4C1QUSudtli6L8CU0-iwCHWkL0ccul7yXXdHHSZ4jK1LSaw5tiTJGBnicc1ocCrYYhAvTJl3LVH55EQuJE2YBH5nXZBnpf_-YyLMnpR0py6fFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ظرفیت ۳۰ میلیون تنی که محاصره را دور می‌زند
🔹
در حالی که تنگۀ هرمز به گلوگاه تحریم‌های آمریکایی تبدیل شده، دریای خزر به خط مقدم تاب‌آوری اقتصادی ایران بدل شده است.
🔹
استاندار گیلان می‌گوید که بنادر شمالی ظرفیت واردات ۳۰ میلیون تن کالای اساسی را دارند؛ رقمی که معادل کل نیاز وارداتی کشور در سال گذشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/akhbarefori/652052" target="_blank">📅 07:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652051">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین- داریوش بزرگ -قسمت هجدهم</div>
  <div class="tg-doc-extra">داریوش بزرگ</div>
</div>
<a href="https://t.me/akhbarefori/652051" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
▶️
«داریوش بزرگ؛ معمار امپراتوری ایران»
🗓
این قسمت روایتی‌ست از پادشاهی که پس از طوفان شورش‌ها، ایران را یکپارچه کرد؛ از مردی که با نظم اداری، قانون‌گذاری و ساخت پارسه (تخت جمشید)، پایه‌های یکی از بزرگ‌ترین امپراتوری‌های جهان را استوار ساخت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/652051" target="_blank">📅 07:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652050">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac1de98ac.mp4?token=VQUPOphMkckf8pI_5PRoGgaKJl64yjOa-V9wEihbwDRTrnqtr0VYvv2UzhG0Tgjk5dOe8-yKDRLepqwfd88jX6Tr6w2t68i6A3n70iZaiCKueEByRIt4baLV6emj9hfyOIgbg9wkXRPw0BplaHWRPc00CAeZYiPCnAiottv4YmGtoTng7PEjXZD7r8oYoNe3bC089wdJED0TwN4EtXh_3s8vUQXZF8swlAIdpvM_EO421_Q_4kW4d95omXX61_pypMzgpCRWcQM49g-OeL8dDHCq6iRS6tZH9db-Os9sAAQ0h12RzpH4JSjRpWuIqg2QNxHrBa5c2t-lEHjg4tyjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac1de98ac.mp4?token=VQUPOphMkckf8pI_5PRoGgaKJl64yjOa-V9wEihbwDRTrnqtr0VYvv2UzhG0Tgjk5dOe8-yKDRLepqwfd88jX6Tr6w2t68i6A3n70iZaiCKueEByRIt4baLV6emj9hfyOIgbg9wkXRPw0BplaHWRPc00CAeZYiPCnAiottv4YmGtoTng7PEjXZD7r8oYoNe3bC089wdJED0TwN4EtXh_3s8vUQXZF8swlAIdpvM_EO421_Q_4kW4d95omXX61_pypMzgpCRWcQM49g-OeL8dDHCq6iRS6tZH9db-Os9sAAQ0h12RzpH4JSjRpWuIqg2QNxHrBa5c2t-lEHjg4tyjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ، پادشاهی که امپراتوری را از نو ساخت…
​قسمت هجدهم پادکست کافئین منتشر شد
☕️
⚪️
با قانون، جاده شاهی و نظمی کم‌سابقه، ایران به قدرت اول جهان باستان بدل شد…
​
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتون باشید!
​از اینجا ببینید و بشنوید
👇
https://youtu.be/Qfgg8RqcuBg?si=5uXMp7EKJBtDtAjp
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/akhbarefori/652050" target="_blank">📅 07:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652048">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJSSj3TvpP5XH3olRBd1NPaZbiPo33Ph-W1u8vZFKRBsHM55VMHfunfeLptevrhMEqyUqOF7uL0qMqq6OLj4Gx7STkeAg2kHLQ5g4GPbONQOhJv1oChxApzBf-Vn-2XG2uol2o7wwuf6eo_GxwwCZWThgFWOgB-vNvvT4r10EBDzW9NgeKJiMluGq9LvbTDY-ptIxBSi5ja5a6iCTpOyrO_UnPpm7Mm0mMO2bHHMVayJHzMLbSacwgD-JTWYTWYOS7YzxC_0bBbXyqSH9cekVpg69J1WomOl3aMIiHUhDaLNka1q_uXffPddYiwuzN2PXgmgEHBlpHjIVXo5Rh3i2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۳ اردیبهشت ماه
۲۵ ذی‌القعدة ۱۴۴۷
۱۳ می ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/akhbarefori/652048" target="_blank">📅 07:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652047">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfVpml5PzLXNQnFF18dvpodzcF1Vdi9Wh7ZzJyuKty80ju1agf56BAuh--q2KDarcANzqheSN-XIiDVEc3gIs8yrumTqqW0BWS8whhaSOfbKoGeEcVEql09yPQq0cfh7PCIBm3oofQ0MglBZRYCur_-Sl4GxpXcuuNlOS6LyUTgl3LufM46tPePe3v-bSj1PSlku04d4afsaouU-JQ1NJg8gxXL1T97oc7qEqNKYRfyzYVMQqyul3CrDE6Ja0il0ISJ_eOWVQ5_6FEMPD91mexTwB4UNLSkfVYSFOX13VNe7xe3QV6r8JL65jEHiULt8t61FTgixozNQ4uLlu6KSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسوشیتدپرس: پرسش های سخت کنگره به ویژه واکنش های منفی جمهوری خواهان به وزیر جنگ آمریکا
🔹
هگزت، وزیر جنگ روز سه‌شنبه با پرسش‌های سخت قانون‌گذاران جمهوری‌خواه و دموکرات در مورد پایان بازی دولت ترامپ برای جنگ ایران، از جمله افزایش هزینه ۲۹ میلیارد دلاری این درگیری و تأثیر آن بر کاهش ذخایر تسلیحاتی ایالات متحده روبرو شد.
🔹
اگرچه رئیس پنتاگون لحن خود را در جلسات استماع کنگره تقریباً نسبت به دو هفته پیش ملایم‌تر کرد و به ویژه از همان انتقادهای تند قانونگذاران اجتناب کرد، اما از سوی اعضای حزب جمهوری‌خواه خود در مورد میزان مهمات مورد استفاده آمریکا در جنگ ایران و انتقاد شدید دونالد ترامپ، رئیس‌جمهور آمریکا از متحدان سنتی به دلیل عدم شرکت در این درگیری، با واکنش بسیار منفی‌تری روبرو شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/akhbarefori/652047" target="_blank">📅 06:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652046">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7R5ur12qQmSDSjfSb26obkOMJ9AmL6Z3aTsjQfM0aZ-k5Y5VRP8_-bu5flVpNewCR4SONMCIzCJqpVMth2vOgpws5XHqvCw13k0Rn30BIRJdZxQld3IEWnRnDUd3kFdQ1iZWoZ4P6BQmL_UDTa5f9kS253jenDfRQ2_yDdOhysGr7gPNLJn24WhSkLJZqrrLVH55TIjQPl4xiF_mB7VM9FmX63J3XhcBqyyJvVtjhE8KT2zK_KAwfcZx4jhFzeF1ZMaewTPSVnoUgLM5kO2WlUHew5lFniK5VI_wxkN94Epw5vlcdVIfmKdZiNTeHi2NyhQNIgrL83H7lzY8aUWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دموکرات‌های آمریکا: جنگ ترامپ با ایران غیرقانونی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/652046" target="_blank">📅 05:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
چین از پاکستان خواست تلاش‌های خود برای توفق ایران و آمریکا را تشدید کند
🔹
وانگ یی، وزیر امور خارجه چین، در تماس تلفنی با محمد اسحاق دار، معاون نخست‌وزیر و وزیر خارجه پاکستان، از اسلام‌آباد خواست تلاش‌های میانجی‌گری خود بین ایران و ایالات متحده را تشدید کند و برای حل مسائل مربوط به بازگشایی تنگه هرمز نیز نقش فعال‌تری ایفا نماید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/652045" target="_blank">📅 04:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
انگلیس نیروی نظامی به تنگه هرمز اعزام می‌کند
🔹
وزارت دفاع انگلیس شامگاه سه‌شنبه از آمادگی ارتش این کشور برای اعزام یک فروند کشتی جنگی، چندین جنگنده و مین‌روب‌های بدون سرنشین به تنگه هرمز خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/akhbarefori/652044" target="_blank">📅 04:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmPkZOVYXtsRyROM66OJiWeyvgbfD8UsCkpRDBYrB1KC6Rwl5USKbyGi15LzZK2GZgerZCM6JIFjL3shXalNNO9tgLYRHtm5UhjH0WZ4yUXuCNZaxE7ObxlBqV69rHhztqddrUKCDllPzWpctWcikYgkF4ARZnmVQ2gb7njlh207AtIRrJw12SEzyGTIUOfQmsr-vVQePj2ICyNOf-1bK-auGefUJIO0uqYRYtft2p6QcRqlbXGSR-Cu5lhG_Wobvq6J8b3Q4hjnvUx9HyhkjxU0KQM586wXQnC1G8tWwg6Zx30hX4NYI5asuANmF06FTSzIK9MbfYuP-Bmcke61wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: اسرائیل نگران توافق بد آمریکا با ایران است
🔹
مقام‌های صهیونیست به شبکه «سی‌ان‌ان» گفتند که تل‌آویو نگران است آمریکا بدون رسیدگی به مسائل مد نظر این رژیم، به توافقی با ایران تن دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/akhbarefori/652043" target="_blank">📅 03:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
تصویب قانون اعدام اسرای فلسطینی در سایه سکوت جهانی
🔹
«ریاض الاشقر»، مدیر مرکز مطالعات اسرای فلسطینی: سکوت جامعه جهانی در قبال قانون اعدام اسرای فلسطینی، رژیم صهیونیستی را به تصویب قوانین جدید برای اعدام صدها اسیر اهل غزه و جلوگیری از آزادی آنان در هرگونه توافق تبادل اسرا تشویق کرده است.
🔹
این قانون، یک جنایت جنگی و نوعی مشروعیت‌بخشی رسمی به قتل اسرا از سوی کابینه افراطی رژیم صهیونیستی به شمار می‌رود و هدف آن، انتقام‌گیری و بستن راه هرگونه توافق تبادل اسرا در آینده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/akhbarefori/652042" target="_blank">📅 03:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnzY6y3B_FwNJxAO7RnQ3R9PebRXZ4p17yJWFoOwGrMqTDuZe_A-d5OEIMRIyuGGl4MLomEssT-14fTe7kHC0fcQ7rBwMKy_2H0Y_O-UcRoQ3ksLi8W9KqJnU7Xy5geQCCdPifdes1wxWm1x_3iEsE-NNcZ2KvFRnwS09oUi1LqhSbga7oGDlFSp2HpzPl5g5zs7nfJoI1vPV-2L1IHrT9I5A2zBf3fvXvWjERFNcXux0U-txj69eBgs225XQZ7r4p7FfGuvMrUzIHl6EqP_LA8L-kiWajPrHdT1TdxrQQdfTsb2h8x7esBG_NftMioWNCnvisalp0dwpgvP5vyfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ۱۱۲ کشور به قطعنامه آمریکا درباره تنگه هرمز پیوستند
🔹
منابع دیپلماتیک می‌گویند که ۱۱۲ کشور هم‌اکنون از پیش‌نویس قطعنامه پیشنهادی آمریکا به شورای امنیت سازمان ملل درباره تنگه هرمز حمایت می‌کنند.
تحلیلی دراین‌باره را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214584</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/akhbarefori/652041" target="_blank">📅 02:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
اقامۀ نماز آیات برای تهرانی‌ها درپی وقوع زلزله واجب است
🔹
به دنبال وقوع زمین‌لرزه در مرز استان‌های تهران و مازندران بر اساس موازین فقهی، با وقوع زلزله، اقامۀ نماز آیات بر افرادی که در محدودۀ لرزش حضور داشته‌اند، واجب فوری است.
🔹
طبق رسالۀ عملیه و فتوای مراجع عظام تقلید، رعایت نکات زیر حائز اهمیت است:
🔹
محدودۀ جغرافیایی وجوب: اقامۀ این نماز تنها بر کسانی واجب است که در شهر یا منطقه‌ای حضور دارند که زلزله در آن رخ داده و یا لرزش آن را احساس کرده‌اند.
🔹
زمان اقامه: نماز آیاتِ زلزله باید در اولین فرصت ممکن و بدون تاخیر (پس از رفع دلهرۀ اولیه و پیدا کردن شرایط ایمن) خوانده شود.
🔹
اطلاع دیرهنگام: اگر فردی در زمان وقوع زلزله خواب باشد یا به هر دلیلی متوجه آن نشود و بعداً از طریق اخبار یا اطرافیان مطلع شود، همچنان خواندن نماز آیات بر او واجب است.
🔹
تعدد زلزله‌ها (پس‌لرزه‌ها): با توجه به وقوع پس‌لرزه در ساعات گذشته، اگر فردی هر زمین‌لرزه را به صورت مجزا احساس کرده باشد، برای هر کدام یک نماز آیات جداگانه بر او واجب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/akhbarefori/652040" target="_blank">📅 01:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652039">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ایران به اکثر تأسیسات موشکی‌اش دسترسی دارد
🔹
روزنامه «نیویورک تایمز» بامداد چهارشنبه نوشت که بر خلاف ادعاهای ترامپ، ایران به اکثر سایت‌های موشکی خود دسترسی دارد و ۹۰ درصد آنها عملیاتی هستند.
🔹
در این گزارش آمده است: «ایران دسترسی عملیاتی به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده است، که می‌تواند کشتی‌های جنگی و نفتکش‌های آمریکایی را که از این آبراه باریک عبور می‌کنند، تهدید کند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/652039" target="_blank">📅 01:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652038">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSS7el8gs70WFvERz1o0U1s5YKl2Cys3PPA9XrjvpTMDaICYS-kiCYzCWoj6B05VWoiHrUfpi6BlrKvUKj4BB03-jppLTJveLl5zD_QrgIk8DF6Q4gOr2gUWKRwZBNjOBbjqB60hVon2Y9Q2l1vynxuEq0O2w6orQDQcDfiMJHYZWC_-zDG0916KrWNswS_rPNVH_Pg1xhbEFIO2Bw-LQO_Td89l7g-ZUL0efiBWyYrLPuUBNeST0xkUFerKD5rasij63dGRBnUEAPoa9DDrck4q0oMBA-diIfn8LomPrVOkQ3UTOwYipsCj2xkWyqhs4Tkq_PtZ3Ge2yte8FXa4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف صریح مقام صهیونیستی: خوشحال می‌شویم اگر توافقی میان ایران و آمریکا در کار نباشد!
🔹
منابع اسرائیلی گفتند توافقی که برنامه هسته‌ای ایران را تا حدی دست‌نخورده باقی بگذارد و همزمان از موضوعاتی مانند موشک‌های بالستیک و حمایت از گروه‌های نیابتی منطقه عبور کند، باعث می‌شود اسرائیل جنگ را ناتمام تلقی کند.
🔹
یک مقام ارشد نظامی اسرائیل نیز ماه گذشته به خبرنگاران گفت که اگر جنگ بدون خارج شدن اورانیوم غنی‌شده ایران از این کشور پایان یابد، آن را یک شکست تلقی خواهد کرد.
🔹
این منبع ادامه داد ما خوشحال می‌شویم اگر توافقی در کار نباشد، خوشحال می‌شویم اگر محاصره هرمز ادامه یابد، و خوشحال می‌شویم اگر ایران چند حمله دیگر نیز دریافت کند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/652038" target="_blank">📅 01:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652037">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
مصرف ۱۳۰۰ فروند موشک پاتریوت از سوی آمریکا در جنگ ۴۰ روزه با ایران
🔹
رسانه‌های عبری اعلام کردند که آمریکا در جریان جنگ ۴۰ روزه با ایران، ۱۳۰۰ فروند موشک پاتریوت مصرف کرده است. هر موشک پاتریوت بین ۴ تا ۴.۵ میلیون دلار هزینه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/652037" target="_blank">📅 01:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652036">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
فعالیت‌های ماگمایی قله دماوند با ایجاد تغییر در فشارهای منفذی، باعث تحریک گسل‌های اطراف می شود
🔹
اینکه باید منتظر زلزله بزرگی در شرق تهران باشیم از منظر علم میان‌مدت و بلندمدت زمین‌شناسی دارای دو جنبه است، از نظر پتانسیل لرزه‌زایی که از نظر علمی، گسل مشا توانایی تولید زلزله‌ای با بزرگای بیش از ۷ را دارد.
🔹
با توجه به اینکه از آخرین زلزله بزرگ این گسل (۱۸۳۰ میلادی) حدود ۱۹۶ سال می‌گذرد، این گسل در مرحله تنش بحرانی قرار دارد ولی هنوز در حال حاضر هیچ ابزاری برای تعیین زمان دقیق وقوع زلزله (ساعت، روز یا ماه) وجود ندارد.
🔹
وقوع زلزله‌های ۴ ریشتری اخیر در ۲۸ فروردین و ۲۲ اردیبهشت در پردیس نشان از تخلیه انرژی: وقوع زمین‌لرزه‌های کوچک به صورت مستمر، بخشی از انرژی گسل دارد، ولی این لرزه‌ها نشانه‌ای از ناپایداری در پهنه‌ای وسیع‌تر نیز می تواند، باشد که مقدمه رویداد بزرگتری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/akhbarefori/652036" target="_blank">📅 01:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652035">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5b045bd6.mp4?token=s9FgAojaJCBaqE2sKvWgNhRBuR5nuR9wAnp4jQt9eUbeFmArF0637GI6wiysi0-jP1Im5xGADa6TlJ8PJSwhKETFofXJeojgMzrUM_j5mjRYHDw6zXm5gxh_u4pVFfYwRuRWIXLuI8UeGd4Gi5GfhhgNAfaoD8Rzbxr4JOgEyUZGDinhPg6XKrKbu0ZEaPSNLP-doqrOc-s3DsepF9WbxgIMGDZjpJ7jJCZPXXH-Cq2kZXjJBaF3LvoKun7ZQsAkehI2URieb_Rn68d5io8EmjFSGi4qrbBLe_IhygHq7Pd07yix_OvKSWFA7N02gY1QpkpWMuXEkYI9ByC8ljAbZYOoynerdLJb07uZJC6YR1STcIeHXN4xCnC1enYIaRbeIUu7eDJ7ZojCMpu5HhCg4g616SkMih35dx8pgPwZyvCMDtb0Avao0NS0q_7CbMrsIdSZO9YRFSluymVeC3yiaD1HbYJlTf26YGgTtXlZMY4Rq_7HtI2sC53_awC6-_R7t80UhW6S8RYoCVfb1YxICvOvR2VwWjstRmFwdcswm6UB8OUhfWL_xW_vvZLfEL4eumG2y_ObCsc_UQWVN4z_zdQ_zGz4uLxG0tl45y9ZJ4h7Z4bxjlaDmcovWuxSbT837Vpey5tDh3BAM-VVfn1uvWQXoJIOS7waPFOofa95_iM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5b045bd6.mp4?token=s9FgAojaJCBaqE2sKvWgNhRBuR5nuR9wAnp4jQt9eUbeFmArF0637GI6wiysi0-jP1Im5xGADa6TlJ8PJSwhKETFofXJeojgMzrUM_j5mjRYHDw6zXm5gxh_u4pVFfYwRuRWIXLuI8UeGd4Gi5GfhhgNAfaoD8Rzbxr4JOgEyUZGDinhPg6XKrKbu0ZEaPSNLP-doqrOc-s3DsepF9WbxgIMGDZjpJ7jJCZPXXH-Cq2kZXjJBaF3LvoKun7ZQsAkehI2URieb_Rn68d5io8EmjFSGi4qrbBLe_IhygHq7Pd07yix_OvKSWFA7N02gY1QpkpWMuXEkYI9ByC8ljAbZYOoynerdLJb07uZJC6YR1STcIeHXN4xCnC1enYIaRbeIUu7eDJ7ZojCMpu5HhCg4g616SkMih35dx8pgPwZyvCMDtb0Avao0NS0q_7CbMrsIdSZO9YRFSluymVeC3yiaD1HbYJlTf26YGgTtXlZMY4Rq_7HtI2sC53_awC6-_R7t80UhW6S8RYoCVfb1YxICvOvR2VwWjstRmFwdcswm6UB8OUhfWL_xW_vvZLfEL4eumG2y_ObCsc_UQWVN4z_zdQ_zGz4uLxG0tl45y9ZJ4h7Z4bxjlaDmcovWuxSbT837Vpey5tDh3BAM-VVfn1uvWQXoJIOS7waPFOofa95_iM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: مبادی سفارش‌ها تغییر کرده تا بتوانیم کالاها را از مرزهای زمینی و بنادر شمالی وارد کنیم
🔹
گفت‌وگوهای جدی نیز با کشورهای همسایه و کشورهایی که با آن‌ها در تعامل هستیم، اتفاق افتاده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/652035" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApqBSqaXtxuyp7H_Q1BwVsTFanlSQ7N9P3kdEU3bQ8i0lG8R_e6WOXntoIqJzcDpK-Ub1Blsh0_RUy2QMKnMvrtax9AOl8SaMrTkmuqUWi9PvADrWiAHbr6z_JoxY_7AI84Ncqbvw1hbf9srNpfulovACZ4P_S7TzuBKpl-FrMoF4MiVCWmxRakuHE8kYbIktukFUxcOQ1zqfm_cqD85WfMB1udEj0ojiLOH8c2g_p2n03XOkHR4LDfWivVeVb5Ya1GhY-qxSacYdRIm9rLmLhyOeCedad_PwMNrZd8uZUHFXkiKw_r8PzpgLrIVGIAjUPtnftdT7lajWaeX-NRgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: آنچه بر ملت صلح‌دوست ایران تحمیل شده جنگ متعارف نیست
🔹
سخنگوی وزارت امور خارجه در پیامی با بیان اینکه آنچه بر ملت صلح‌دوست ایران تحمیل شده، یک جنگ متعارف نیست، نوشت: این جنگ میان دروغگویان حرفه‌ای است که برای خشونت‌شان توجیه جعل می‌کنند، و مردمی شریف که فقط با تکیه بر توان و اراده خود، از وطن و کرامت انسانی‌شان دفاع می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/akhbarefori/652034" target="_blank">📅 01:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652033">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔹
از داغ‌ترین خبرهای امروز و امشب، جانمانید
🔹
🔹
زلزله‌های پی‌درپی در تهران
👇
khabarfoori.com/fa/tiny/news-3214578
🔹
دیدار مهمی که سرنوشت جنگ به آن وابسته است
👇
khabarfoori.com/fa/tiny/news-3214551
🔹
ترامپ به جنگ ایران بازمی‌گردد؟
👇
khabarfoori.com/fa/tiny/news-3214321
🔹
چین بین تهران و واشنگتن میانجی‌گری می‌کند؟
👇
khabarfoori.com/fa/tiny/news-3214364
🔹
سیدنی سوئینی به سوی آثار مستهجن می‌رود | ماگا علیه عزیزِ ترامپ!
👇
khabarfoori.com/fa/tiny/news-3214209
🔹
تصاویر و ویدئوی املاک توقیف‌شده خبرنگار ایران اینترنشنال
👇
khabarfoori.com/fa/tiny/news-3214399
🔹
ویدئوهای جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/652033" target="_blank">📅 00:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652032">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
زلزله دوباره در تهران
اخبار لحظه به لحظه
👇
khabarfoori.com/fa/tiny/news-3214578</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/652032" target="_blank">📅 00:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652030">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qc1sxyukmacHGjhSydTofEaGT2to7fBOA7BSxv03M1jW9tBGfQt1sJWYSYMA8WXIDs_qo8eIxX4On_yc8tM4JuAvvZ0cdc-zqOO8BXyizE3ip-fDy3fsm45iB1SFATbBcvG3Kn2O02TmJ-szZLwX37asA99_U7uYZOSdIIVvkLKt8wLjYzL2NVEsdZ_1wusXa3wJ1URr3th-uuqKt_Hovl0XXqOAKin9C0KtfqS-as83OeRWUaRjC-4mRJ4mc2B3FE9geK33ccAhkkYRVoHMBl7Icl_J_MYBQln85ZPUXfiE_-qmXbbJd8JsYbhuTI2ERoDk_awv5nv_zm9KKCGGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekfJrgtXFL3YA8ONEIaGCVXvUkcFqoJvRRIJM3XrKzQw4wPeI3tdQHCJhajVRg3todHbL2WNOWXSgkLnC-AQTxM27xn81LSWS1cnDXpBAURm73wB2X3RS9TSsrIgx5b4QQolRZdTOWnOVpsfZIFRjQ2dZwjcQyws8-ytNGz3Gfea_rN5GJ6TQ9PXFvaho2mcXt4wCPkfhm1Z5_ftpDgPSYMeLnOtcdovr6UX66oEYuKKe091lxgamD04Opk9zhi8e9wMBmm16oLZTz6vlJkHEwUx9D5VqWvb4_qnjUTjmqYVMDwZ9k2LA94vJDbjfC28HnBtOwppc4bmV3smNXL5zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هم اکنون؛
🔹
پایش لحظه‌ای وضعیت تهران پس از زمین‌لرزه در مرکز عملیات اضطراری سازمان امداد و نجات
🔹
در پی وقوع زمین‌لرزه در تهران، نشست پایش و رصد وضعیت با حضور مسئولان و نمایندگان استان‌های معین، هم‌اکنون در مرکز عملیات اضطراری (EOC) سازمان امداد و نجات جمعیت هلال‌احمر در حال برگزاری است.
🔹
در این نشست، آخرین وضعیت مناطق تحت تأثیر، آمادگی و همچنین هماهنگی‌های لازم برای تسریع در روند امدادرسانی و پاسخ به حوادث احتمالی انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/652030" target="_blank">📅 00:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652029">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdQRDG5Y2r7ujlFXZnddogDPZ8iKjlRnMSGAipcNMgQtxTs-eVLXv8id45qUVyHyX_qN2yUVQVzIWfliPueZi_Y9A0ryDfa-cYwBxUvvEK-CNd63nLiwKQZ8GeOcMhjVs8FVR2-DHQ2ks9fUkdiIKuuWbfRfc6v1hJn6hIZ2ZwjWPDJtVUDZ8n-T3pgxS6oggWFHyUZ8yQCNnsPPIfe30JeqdHywE_e7V4zb5L2ObTv9zn2hOHr_2FojeWFiL9lBKgWO0Krf6MOl2H6lUxZH6yBTtCtPizpRHWB7JS_lkP7AEwLZXaVlDgAss_duzojHsIlGLVQXu-DDqU1NncqlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ:
🔹
وقتی اخبار جعلی می‌گویند که دشمن ایرانی از نظر نظامی علیه ما خوب عمل می‌کند، این عملاً خیانت است، چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آنها در حال کمک و دلگرمی دادن به دشمن هستند! تمام کاری که می‌کند این است که به ایران امیدواریِ دروغین می‌دهد در حالی که نباید هیچ امیدی وجود داشته باشد.
🔹
این افراد، ترسوهای آمریکایی‌ای هستند که علیه کشور خود ریشه می‌زنند. ایران ۱۵۹ فروند کشتی در نیروی دریایی خود داشت — اکنون هر یک از آن کشتی‌ها در کف دریا آرام گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/652029" target="_blank">📅 00:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652028">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
جزئیات کامل زلزله شدید دقایقی پیش در تهران
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3214578</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/652028" target="_blank">📅 00:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652027">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
پس از زلزله اخیر در تهران، پایگاه‌ها و امدادگران هلال احمر در حالت آماده‌باش کامل قرار گرفتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/652027" target="_blank">📅 23:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652026">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
دنی، سیترینوویچ، رئیس پیشین میز ایران در اطلاعات نظامی اسرائیل: هر توافقی تنها بر دو موضوع اصلی تمرکز خواهد داشت؛ کنترل تنگه هرمز و حق غنی‌سازی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/652026" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652025">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX1cVCHwlDFy2f8WkSQNAeHcNdir4ePgrLW0eKIkVxew1sqfFM2DawloK4DEaziL2tqir-4hdCw_z2vw95ie9IdX8eqS6IAEPTFMbc3sUEnz-JlPiHG7qmVfUpTuhyxRNLgLRszJ91vDYuTV6-ZB_Sj7kT6G9Zs5_eRBvKiCKkw4I390FceNnxCYeYwDBIVhZODSMdChAyr4xJg8TNiB4IXO-XOKXIpQ-0fYuN3cybH6UbfSk9_lDKvSEMLe1yHq9UnIg-iygNc6Ri2WUGm0Zg3eU6ZO1dlOilOkQGw-CQmoIxFKj_NyfEIYKC_fkJT6s4Y0-RTARTQ_HFXTlWbhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: زیاده‌خواهی و عدم صداقت آمریکا مانع حصول توافق است
🔹
وزیر امور خارجه امروز در دیدار معاون وزیر خارجه نروژ رویکرد زیاده‌خواهانه و لفاظی‌های تهدید و تحریک‌آمیز طرف آمریکایی و فقدان حسن‌نیت و عدم صداقت آمریکا را مهمترین مانع برای پایان قطعی جنگ و دستیابی به توافق احتمالی خواند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/652025" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652024">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
زلزله شدید در تهران
khabarfoori.com/fa/tiny/news-3214578</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/652024" target="_blank">📅 23:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652023">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تنگه هرمز معادلات جهان را برهم زد؛ همراهی با آمریکا دیگر صرف نمی‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/652023" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652022">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_Lg2qy5a9q6QH0p22CmLgzC90nkJwcehlq7QEQKKHFUY-2HFM2rVDKQJ54OvleTNzJx5DQI5Ip-TvNY2evyDM_U_SW7134GPoTCg-8mnFGv-kdpc5LDD6GJkJYnPxPoggVaq-t7EOH9rZ5H0tOCLP9EeYT9Frt8gvveVdE_jzUNK3VSk5ELSV2HxiIKA5t41EIkYDOC4RCVVf98dhgH6fZaX8QghctkwrFuJuAHrVKcmVOgxg3js0CmtNf_EqifOYdoGqQpxdIMRaFbytOFnP2Al7HNDuOsid1ce_tYj2T0nRS2QPljtIV8DStP8K_sbCJdq3aMzE2mOfgtQpIllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار مهمی که سرنوشت جنگ به آن وابسته است/ نقشه ترامپ برای ایران چیست؟/ چین صلح می آورد یا به زودی جنگ «تنگه هرمز» آغاز می شود؟
🔹
واشنگتن تلاش خواهد کرد تا از طریق چین، تهران را مجبور به لغو محاصره و باز کردن تنگه هرمز کند و امنیت انرژی را به یک برگ برنده مهم در مذاکرات با پکن تبدیل کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214551</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/652022" target="_blank">📅 23:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652021">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2170f2149.mp4?token=smvnaNoYCKiifnF6EkKLIU1f0ZN5n8VajYba5tpXtSCf-M-oUWD3fsKHD17K3eXbx7gwfwR7k5wYHf3I4ZhAXo6ScF3Bh5YRlG7jYQkxh6gFxAfzTiqwsULkvlIqN6SNjQpouL5Uoi81lq8aE6IoDFH825IvUDELXj8dT_iUIfmzwrsvnmhR-7CfOmNR3ATw7Vgev1kPg5_MTvWGywEFF0KHUX61lq3-EMyvTL0-alpMLzApk-4SH24wgZubQ4XW3AqoF33xUzCKZ-KaQE3Dow6ol5kYF56yWHzSiW4w84EDBXzag9r0CjxsySEEgRddcDnXldCc86mcJoeP4nyslA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2170f2149.mp4?token=smvnaNoYCKiifnF6EkKLIU1f0ZN5n8VajYba5tpXtSCf-M-oUWD3fsKHD17K3eXbx7gwfwR7k5wYHf3I4ZhAXo6ScF3Bh5YRlG7jYQkxh6gFxAfzTiqwsULkvlIqN6SNjQpouL5Uoi81lq8aE6IoDFH825IvUDELXj8dT_iUIfmzwrsvnmhR-7CfOmNR3ATw7Vgev1kPg5_MTvWGywEFF0KHUX61lq3-EMyvTL0-alpMLzApk-4SH24wgZubQ4XW3AqoF33xUzCKZ-KaQE3Dow6ol5kYF56yWHzSiW4w84EDBXzag9r0CjxsySEEgRddcDnXldCc86mcJoeP4nyslA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: برای واردات دارو و تجهیزات پزشکی، کارگروه ویژه‌ای در دولت تشکیل شده است
🔹
مسائل و موانع مربوط به واردات، از جمله موضوع ارز، با همکاری بانک مرکزی پیگیری می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/652021" target="_blank">📅 23:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CViyES94f3p9VO27kxL_00bSs_wCvkAqt_ZD3GssNxB_Y5v1KwSIyS9u3uQp94V4JXeXFB2JyLyMXaVKW6wAMuYzQzDH_5whsUrdjQU2GA0h7j0ewqyihlCpLdPJyKyUtvY9LXnHii6Zo7oHvzQOyx5cJttFjF8YzaIY59H9jO_Ia_zaxPJ28GRAS0RMlbSyhr7ihXq05jXGdlbu-AXsxqp_Pb7KDmiuYlgDYVSxTYbS2xHHcxXns4_I29xDrHMHh6uefJEWO8mcJMijlLa73gRcc-Oay0NC090iApFoY9dVtLPJig17dnCJH5cNlavqdjMac_yThHmzOj3W5FMgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزار‌ش‌ها درباره حمله عربستان به ایران در طول جنگ
🔹
خبرگزاری رویترز روز سه‌شنبه گزارش داد که عربستان سعودی همزمان با تجاوز نظامی آمریکا و رژیم صهیونیستی، حملاتی را علیه ایران انجام داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/652020" target="_blank">📅 23:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652019">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
پنتاگون در حال بررسی تغییر نام جنگ علیه ایران است
🔹
شبکه ان‌بی‌سی مدعی شده پنتاگون قصد دارد در صورت شکست آتش‌بس و از سرگیری عملیات جنگی‌ نام جنگ علیه ایران را به «عملیات پتک» تغییر دهد.
🔹
دونالد ترامپ نام عملیاتی که در اسفندماه علیه ایران آغاز کرده بود را «خشم حماسی» گذاشته بود اما بسیاری از منتقدان به این عملیات لقب «خشم اپستین» دادند.
🔹
این منتقدان معتقدند یکی از انگیزه‌های ترامپ برای آغاز این جنگ منحرف کردن اذهان عموم از فساد ترامپ در پرونده مجرم بدنام جنسی، جفری اپستین بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/652019" target="_blank">📅 23:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652018">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbQcwxk3qGrxa6FUDGYjZP2eIqpxgb_EyJ4RBpQkGwSk-nj_iLI2SkxMMHau6rEhAWRUsDhoZyX-gUE9AkEf5jTOAArLR1WH3nZGv1Rp79p1h6WOE2Dqjz0Va6KzG3a4zhQFwuUd-j2ODT3fN4aFIdz-6KSrkMprXUBaQdI5gNcKbi4UphwI3hqTMoiJ7bEYmFrvbsvHXhQK-yjNncVro3bZuPioxxzdheGqdBENAFcb7Zpxug7KLI3n3PA_P015Y9hf9XJQmJ1AFM1di8TEl_HSuqPcVdimBVLM7PxX-K-MUEgayguTUyR6tWQfe_ncmKAv812s7R22xj2z8kjUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌خون
🔹
مردم نجیب ایران، حتی در روزهای سخت جنگ، رسم همدلی را پاس داشتند. در جریان جنگ اخیر، بیش از ۴۰۰۰ کودک از مراکز شبانه‌روزی بهزیستی به خانواده‌ها پیوستند و ۱۲ شیرخوارگاه به‌کلی خالی شد. در هفتهٔ اول جنگ رمضان، شمار مراجعه‌کنندگان برای اهدای خون ۴۹ درصد و خود اهدای خون ۴۰ درصد افزایش یافت. در مجموع روزهای جنگ نیز آمار اهدای خون ۱۲ درصد رشد داشت. این آمارها، تصویری از همبستگی عمیق و بی‌ادعای ایرانیان است.
🔹
هفتصدوچهل‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/akhbarefori/652018" target="_blank">📅 22:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652017">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb2d80e06.mp4?token=CFv7S2J63J2gOtA5-Ln30X6SjRFVtH_8uB7qmwkDpnbhKH7C3wQ_wQV34m7ZpJN_F75HjKXAtBuztIOiEPvR0l72QsAhlevteqcNbpjmUtU6sPlNjMVLIXidDxUn47u7OMddABELVVNZTb6YfsysSkJazyhu2Vvodp16maSDs8iUOLGxuP1okD3TDFG5BuVTZXC_Ozio1UOlJha_pUTTDJWmk1H0O0ikl4Pxgu1R3nIjQTgTMK39wHXHwsLYIU_FiqgPSuouMTcUFkej5nsw2uuOyn1cs92LTsL3izNaAve9PWKnntXAo-X5LW4lGuW2aZ9sXEPfZIgNgmGagtlRQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb2d80e06.mp4?token=CFv7S2J63J2gOtA5-Ln30X6SjRFVtH_8uB7qmwkDpnbhKH7C3wQ_wQV34m7ZpJN_F75HjKXAtBuztIOiEPvR0l72QsAhlevteqcNbpjmUtU6sPlNjMVLIXidDxUn47u7OMddABELVVNZTb6YfsysSkJazyhu2Vvodp16maSDs8iUOLGxuP1okD3TDFG5BuVTZXC_Ozio1UOlJha_pUTTDJWmk1H0O0ikl4Pxgu1R3nIjQTgTMK39wHXHwsLYIU_FiqgPSuouMTcUFkej5nsw2uuOyn1cs92LTsL3izNaAve9PWKnntXAo-X5LW4lGuW2aZ9sXEPfZIgNgmGagtlRQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون اصل نود مجلس: وزارت تعاون و دولت به سرعت مبلغ مابه‌التفاوت کالابرگ و قیمت اصلی کالاها را به روز کنند تا مردم بتوانند با آن مبلغی که دریافت می‌کنند براساس قیمت مصوب کالای خود را خریداری کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/652017" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652016">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
جزئیات جدید از پایگاه مخفی اسرائیل در صحرای عراق
🔹
روزنامه عبری‌زبان «معاریو»: این پایگاه علاوه بر آنکه شامل یگان‌های کماندویی برای انجام عملیات ضد ایران بود با تجهیزات پزشکی و گروه های پزشکی نیز تجهیز شده بود تا چنانچه به خلبان‌هایی که در حملات هوایی ایران آسیب می‌بینند خدمات فوری ارائه دهد.
🔹
چند روز پیش روزنامه وال‌استریت ژورنال در گزارشی از تاسیس یک پایگاه مخفی با همکاری نیروهای آمریکایی در عمق خاک عراق در صحرای نجف خبر داد.
🔹
این خبر با موجی از واکنش‌ها به ویژه در عراق مواجه شده و دو تن از وزرا و فرماندهان ارشد عراقی برای ارائه توضیح به مجلس فراخوانده شدند.
🔹
یک مقام امنیتی عراق هم اعلام کرد: نیروهای "صهیونیستی ـ آمریکایی" برای مخفی نگه داشتن موقعیت این پایگاه سامانه موقعیت یاب (GPS) را در مناطق صحرایی غرب عراق مختل و تجهیزات پارازیت‌انداز در آنجا مستقر کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/akhbarefori/652016" target="_blank">📅 22:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652015">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0a60e4070.mp4?token=hAmyCf_g7QKVboJnjtdHLobBBGl1LsTxeZGUvPRoHen7QDl1Dbws5JmQ0yQmr_MOy-q79eIB4fbNSzrL0XuXVxKGZno613bZJVEuL97o37Y1GTc3HaXU3aTo6y4kyLT4X8V_njmTklynV4XmXvzERunDCozUYetlqPI7bkm1vIoFMdAmOPZMVgtZLJpwgWCFHIaWkBMAZ5kBegKAfzouXjOzbluCpuuO-qa7DvyaD_E5XkbsiuGXLB2cSw09JcB5Ygz2rPwkN_8CDV4up1n6_rUzmU57msIcfOYFmn_rbF6nP3qJHpfYjF_K5bJKIv6ueFp59eRmv9I2q2sua1f4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0a60e4070.mp4?token=hAmyCf_g7QKVboJnjtdHLobBBGl1LsTxeZGUvPRoHen7QDl1Dbws5JmQ0yQmr_MOy-q79eIB4fbNSzrL0XuXVxKGZno613bZJVEuL97o37Y1GTc3HaXU3aTo6y4kyLT4X8V_njmTklynV4XmXvzERunDCozUYetlqPI7bkm1vIoFMdAmOPZMVgtZLJpwgWCFHIaWkBMAZ5kBegKAfzouXjOzbluCpuuO-qa7DvyaD_E5XkbsiuGXLB2cSw09JcB5Ygz2rPwkN_8CDV4up1n6_rUzmU57msIcfOYFmn_rbF6nP3qJHpfYjF_K5bJKIv6ueFp59eRmv9I2q2sua1f4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستاورد ترامپ از جنگ با ایران: تقریبا هیچ!
🔹
سناتور آمریکایی: هیچ‌یک از اهداف جنگی ترامپ علیه ایران محقق نشده است
🔹
سناتور دموکرات آمریکا اعلام کرد اهداف اعلام‌شده دونالد ترامپ در جنگ با ایران محقق نشده و این جنگ نتیجه‌ای معکوس داشته است.
🔹
کریس مورفی، سناتور دموکرات، گفت: هیچ‌یک از اهداف جنگی ترامپ علیه ایران محقق نشده است.
🔹
او افزود ایران همچنان بخش عمده‌ای از موشک‌ها و پهپادهای خود را در اختیار دارد.
🔹
مورفی تأکید کرد برنامه هسته‌ای ایران همچنان پابرجاست.
🔹
این سناتور آمریکایی گفت ایران پس از جنگ از نظر نفوذ جهانی حتی قدرتمندتر از قبل شده است.
🔹
او در پایان این وضعیت را «یک فاجعه کامل» توصیف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/akhbarefori/652015" target="_blank">📅 22:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652014">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0348a6d7.mp4?token=XJcD4_2v8LwTCmuqATUwbAj1i1M8xDBef1BOPG102PyhBJQF9LXYdx-9Oh6un6r7jpEy1uV08kiUBSAYhsvuHdzO3G-lNkXL9NB8twUC53Mn2PNBPXlFDSM609bGZe5rxYqyGBeCRpLAZsTs0o0jN-fLJV77n8nE4PZLamwJGvT1h9CjpZwp1BJDClMsn2f5NRVv0ZUcj5s4PU3W3DX7AtO4hcIGad9uNdlOrzkrLXGjcXdtRtO-fhcrA8AdSrqnVGq8Y9EM0U9bq2-6BgIh-Apz64zesnZLYT4XiSyAE1BLiCOHP7oOdE12Ojm_SUKPaWaLEQMTz5nxPZjEC1KhqKhKKPVvApsN3AiVubBrG4wVNaAo1rjZxHs6I7Cxv0ZfykKQr1EvbrOI6ogBNYhzueQUWWa5lFEUiECWi_T1oQhFrl8oRjFCydpMV9PKELMr8wpNFVko-tJfgPXSbHj1g1BJeBNCuI3zFsbARwLBCa0YxBmf270XtnE1KwPzmG5NTxsoy_rpkxIu3I6S_kbRO6UDp0QRMrMIDvBJvy_0eONKD8MfgVt-YQuvYAGRdZwxoFUNOa8zjBmSCoD_q5XSJpDwBFZ7FU_KyZZJyBy1zeSK8XiCjcrko7uHQs6jT4NNQcVWyQmJS4LqW_eGG1vw6wGlglU_HJ_597UKQWZz-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0348a6d7.mp4?token=XJcD4_2v8LwTCmuqATUwbAj1i1M8xDBef1BOPG102PyhBJQF9LXYdx-9Oh6un6r7jpEy1uV08kiUBSAYhsvuHdzO3G-lNkXL9NB8twUC53Mn2PNBPXlFDSM609bGZe5rxYqyGBeCRpLAZsTs0o0jN-fLJV77n8nE4PZLamwJGvT1h9CjpZwp1BJDClMsn2f5NRVv0ZUcj5s4PU3W3DX7AtO4hcIGad9uNdlOrzkrLXGjcXdtRtO-fhcrA8AdSrqnVGq8Y9EM0U9bq2-6BgIh-Apz64zesnZLYT4XiSyAE1BLiCOHP7oOdE12Ojm_SUKPaWaLEQMTz5nxPZjEC1KhqKhKKPVvApsN3AiVubBrG4wVNaAo1rjZxHs6I7Cxv0ZfykKQr1EvbrOI6ogBNYhzueQUWWa5lFEUiECWi_T1oQhFrl8oRjFCydpMV9PKELMr8wpNFVko-tJfgPXSbHj1g1BJeBNCuI3zFsbARwLBCa0YxBmf270XtnE1KwPzmG5NTxsoy_rpkxIu3I6S_kbRO6UDp0QRMrMIDvBJvy_0eONKD8MfgVt-YQuvYAGRdZwxoFUNOa8zjBmSCoD_q5XSJpDwBFZ7FU_KyZZJyBy1zeSK8XiCjcrko7uHQs6jT4NNQcVWyQmJS4LqW_eGG1vw6wGlglU_HJ_597UKQWZz-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ بسته حمایتی برای صنایع و کسب‌وکارهای آسیب‌دیده
🔹
وزیر اقتصاد: ۶ بسته حمایتی برای صنایع بزرگ صنایع کوچک و واحدهای تولیدی کوچک و متوسط و کسب و کارهایی که به صورت غیر مستقیم آسیب دیدند در نظر گرفته شده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/akhbarefori/652014" target="_blank">📅 22:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652013">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
یک منبع آگاه
🔹
یک منبع آگاه تأکید کرد که پیش‌شرط‌های اعلامی ایران، تضامین حداقلی اعتمادساز برای آغاز هرگونه مذاکره با آمریکا است.
🔹
پنج پیش‌شرط ایران برای طرف آمریکایی شامل «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز» می باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/akhbarefori/652013" target="_blank">📅 22:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652012">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
حامیان ایران در برلین: کودکان چه می‌فهمند از جنگ و موشک؟
حامیان ایران در برلین:
🔹
کمترین کاری بود که می‌تونستیم انجام بدیم...
وقتی مدرسه‌ها هدف قرار می‌گیرن و بچه‌ها کشته میشن، دیگه نمی‌شه سکوت کرد. این بچه کوچیک چه فهمی از جنگ و بمب داره؟
🔹
گفت‌وگو اختصاصی خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/akhbarefori/652012" target="_blank">📅 22:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652011">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02512faff.mp4?token=bO2Q43iswqxLqmzE2eLnnCFFGa4dEcUpiIf5LjwrjOzrhG-H0oaWzIul3NZr-QScu7b39J-90_Dtylg9Ds6OLX9am7DJ81fMPCSsKLarcUhhJ6sGuM83strh3Ce1dMvwnZ8N6GQza_zEjYeHF2GDp5rejoRlUzLtdYRCsU4wrVgHsGBaLbqbfRs4hCz4Gy3ohabNZVwAR-_gFDo_nW-Fk-sMy2FyFz6fWPvdI83q1Zm2kZbW6SBonYKGsSseQtx0w51RBseHzQ8zdkwg-cRwqcuy5p753PJ4pA05qslyw6A1rf1zTVO-c7V6SIVJIIzCxZ_LKIMMwqdGTs1dCh_OLhE5XZK3YZ4v61m91AW_1Hal1SSOHsNEcuX7zkov1M3RJ3h1rJnGa-s1sDNblKpbOj0F06_E0WjL2M_-uWrPOa-lCZ0sUHbJb9Waia2APObu7EATzwK9XP7zYK0B8bI9zlihMKJzRLKJupkyimGv2FFJpYFfYDG1pMhoXCeGksKZnXoWwNc0_hLdKyjXvoAVwbSKv_NQBieYt6jdyAnFlauokPu0LITqMU7QL02JBzGA67Bhyvgx64nxnhW1XbJdu1Z1XYRD_7zKiY_S10K1DX37hIV23Khili8s_5WfnbMGHYSNgb_RPrA_9ksoc-ds5mwEtF-37E9v1b9lvzq3aKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02512faff.mp4?token=bO2Q43iswqxLqmzE2eLnnCFFGa4dEcUpiIf5LjwrjOzrhG-H0oaWzIul3NZr-QScu7b39J-90_Dtylg9Ds6OLX9am7DJ81fMPCSsKLarcUhhJ6sGuM83strh3Ce1dMvwnZ8N6GQza_zEjYeHF2GDp5rejoRlUzLtdYRCsU4wrVgHsGBaLbqbfRs4hCz4Gy3ohabNZVwAR-_gFDo_nW-Fk-sMy2FyFz6fWPvdI83q1Zm2kZbW6SBonYKGsSseQtx0w51RBseHzQ8zdkwg-cRwqcuy5p753PJ4pA05qslyw6A1rf1zTVO-c7V6SIVJIIzCxZ_LKIMMwqdGTs1dCh_OLhE5XZK3YZ4v61m91AW_1Hal1SSOHsNEcuX7zkov1M3RJ3h1rJnGa-s1sDNblKpbOj0F06_E0WjL2M_-uWrPOa-lCZ0sUHbJb9Waia2APObu7EATzwK9XP7zYK0B8bI9zlihMKJzRLKJupkyimGv2FFJpYFfYDG1pMhoXCeGksKZnXoWwNc0_hLdKyjXvoAVwbSKv_NQBieYt6jdyAnFlauokPu0LITqMU7QL02JBzGA67Bhyvgx64nxnhW1XbJdu1Z1XYRD_7zKiY_S10K1DX37hIV23Khili8s_5WfnbMGHYSNgb_RPrA_9ksoc-ds5mwEtF-37E9v1b9lvzq3aKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: کسب‌وکارهایی که تعدیل نیرو نداشته باشند، از دولت تسهیلات می‌گیرند
🔹
دولت از این واحدهای تولیدی حمایت ۱۰۰ درصدی خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/akhbarefori/652011" target="_blank">📅 22:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652010">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZkGFP-jeW-s5O0Ll1K9SMCLhrGFSJlrgYO4z-P-LspSdz7lh7OXUzCEEDEMvXPRnElHwqlMnkQCWixoPo-8jeumVNIXNCXYB3rHP8Le8hsElzeQlBITL6fX4GpT77hSXHcaBuR4sSO2YdiVSbSRDrVmS_dgry1r-uBUzaoz57ihEY-tWWgdUMTrdMt3jhBoosRCPfZ1APIOz1XAq5HmrZdwSUa8wWik8zKLZHyyyAbiQO34iLY8cUb4Idkfu6jcmmSJFntyKh5D3JzFIDxuo2lzQXB7ojsL9BAz7VU1u1cjD84mYkiKyqN4VgRHfXbIwkmYvZyaiGFyh0opUEvwJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چین خطاب به پاکستان: به میانجی‌گری ادامه بده!
🔹
وانگ یی، وزیر امور خارجه چین، روز سه‌شنبه از پاکستان خواست تا تلاش‌های میانجیگری را افزایش دهد و در حل صحیح مسائل مربوط به بازگشایی تنگه هرمز مشارکت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/652010" target="_blank">📅 22:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652009">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiGeh2bVp99pTEKrNDFTE7Mt0OECulME-kXnk6tT0YhYpRMy8svaecjdah1zb2AT1YJ1N2Arut1O6ymN93Sx_QFIu-wdEobkOKNxkERMc8dk7pDrpK4aRTIwY3kdFiBadf6e0MTzV8NijbOZ0OdZYxCjfqVbiVqJNkewLSJPGJ3BidS35a6HLmib_LC7ds67Hy2SHMb2pTDMSYn4NTiUmh0vWbbvF3YfHroN_0T47sSBETKyefhSF4YAd87SZUN8F3HtfuKpdu3n4Y9xTJcbTQKGp8MiGg-cwqTogaDuIcgKppXjF-BK-A5CuqGCAT0f8yEeXKoKdKDYXr2zl7ttyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بی‌بی‌سی: جنگ ایران، قیمت زعفران را در لندن دوبرابر کرد!
🔹
جنگ در ایران و بسته بودن تنگه هرمز باعث افزایش شدید قیمت جهانی زعفران، یکی از گران‌ترین ادویه‌های جهان، شده است. حدود ۹۰ درصد زعفران جهان در ایران تولید می‌شود؛ به همین دلیل، اختلال در صادرات زعفران، بازارهای بین‌المللی را به‌سرعت تحت تأثیر قرار داده است.
🔹
مغازه‌داران در لندن می‌گویند عرضه زعفران در حال کاهش است و قیمت‌ها به‌شدت افزایش پیدا کرده است. صاحب یک رستوران ایرانی گفت زعفرانی که قبلاً حدود ۱,۲۰۰ پوند برای یک کیلوگرم قیمت داشت، اکنون حدود ۲,۰۰۰ تا ۲,۱۰۰ پوند برای هر کیلوگرم است و تقریباً از زمان آغاز جنگ ایران در اواخر فوریه دو برابر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/652009" target="_blank">📅 22:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652008">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa26b96f7d.mp4?token=U45ZNCM6_AEJvAGU8dE_ROh5wbfoKDrOjRju3PuCLbGo7_R2ka1JM4QT5ENDatvH2NrbBdFwQGWnfpu3L5bFApwKMdfvH1LX-Ez30xOYCAnhrbhfDYZexh2VsyOc-bmM0oKuBQKGiI9LIEv05KzZOfJW3VqeO6L-wPoYiDyLnGScHCbJcDOARXNUUqKEBfEhVE9jpAOovTQ8YisMKzysuJNIieTEh1D7xbg7maC6qatUCfaNfkVLWYdGLTjGCHEoMIeMqyEzI4NBPTmqYVNs-408CUoDZwqX4Hj4vZrwfSfwM1nYTeeTFEVqkYN_zFxLEGnhVrJYUS0Zo7jb0C_YoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa26b96f7d.mp4?token=U45ZNCM6_AEJvAGU8dE_ROh5wbfoKDrOjRju3PuCLbGo7_R2ka1JM4QT5ENDatvH2NrbBdFwQGWnfpu3L5bFApwKMdfvH1LX-Ez30xOYCAnhrbhfDYZexh2VsyOc-bmM0oKuBQKGiI9LIEv05KzZOfJW3VqeO6L-wPoYiDyLnGScHCbJcDOARXNUUqKEBfEhVE9jpAOovTQ8YisMKzysuJNIieTEh1D7xbg7maC6qatUCfaNfkVLWYdGLTjGCHEoMIeMqyEzI4NBPTmqYVNs-408CUoDZwqX4Hj4vZrwfSfwM1nYTeeTFEVqkYN_zFxLEGnhVrJYUS0Zo7jb0C_YoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کار: امیدواریم هرچه زودتر مبلغ کالابرگ افزایش یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/akhbarefori/652008" target="_blank">📅 22:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652007">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
اکسیوس: حقوق کارگران آمریکایی به خاطر جنگ ایران از تورم عقب ماند
اکسیوس:
🔹
برای اولین بار در سه سال گذشته، حقوق کارگران آمریکایی از تورم عقب مانده است، که یکی از تلفات شوک انرژی جنگ ایران است.
🔹
جنگ به از بین رفتن پشتوانه مالی که مصرف‌کنندگان را در برابر آن محافظت می‌کرد، کمک کرده است.
🔹
کارگران اکنون درآمد واقعی کمتری دارند، تهدیدی برای هزینه‌هایی که اقتصاد را فعال نگه داشته است/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/akhbarefori/652007" target="_blank">📅 22:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
حملات ترامپ به ناتو بعد از عدم مشارکت در جنگ علیه ایران ادامه دارد: ناتو من را ناامید کرده است و ما به کمک آن‌ها نیازی نداریم!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/akhbarefori/652006" target="_blank">📅 22:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc-aHD0lmRYx1Pu6tga3_YSbQHyMhgxltftkPWh_Xn4Sj2hdTkMPgtV08taCE18R7_tZZrmnC9_cxTGOMLnzx7cWq0jeGeZ0qcKLxa2WVnaR42hWqAbKditLckrmqT9eor75QdG314IeTY5F1BSGLL-dYiIljkctoAvKYy40L-hqnZOsdc6MYF5ug-wrf3QaP9tENeCKRh7Hl7CbeCKRe2faAjKlFOimUZqOxWeWW7e9N0VCpYJz6ZfWPyA0P8IK9ukmavMIB1IqDFI_ZSahkIHBJMXwW5VrSRf0W6o72s4SIYjuOB0Ea5KoX0aNVOhX3z3xPj61KKj6n_xBzW1E4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فولاد مبارکه مامور واردات ورق فولادی شد
🔹
وزارت صمت اختیار واردات ورق مورد نیاز بازار داخل به فولاد مبارکه سپرد.
🔹
براساس اطلاع، ارز مورد نیاز برای واردات ورق نیز تامین شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/akhbarefori/652005" target="_blank">📅 22:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b2315c5d.mp4?token=Nes9S5SUJr-JQyONrLDxU6J35eRX1SCh6DjEefQEJdAsFvZYhIvQaXfJhDpp-b5-nDyuYUV-vghsd8yCv5_K7lSF6syUq91pzU_T0U0WXTHWsBEGd-HQXrpf5lje0Fs3_Loqe6cVkcJ35pDDnrXgXnMdRCAZxN4E7T9qEalZU81Uwose_N2qR0hbY0rnQ63TJJAlpcrPArmA0hxDXK8L74cCLLE_EJSxHXZ7V6ytC3IKT7jG7DjDEgn-roPEY9pnKpXZGRYwNNzUPaTYCUHzdKapEWyjmDuVQiFunmbbHhuIsdbJZFyx-Qd_U1qyh16pu25FMVSNdiA_3ZmUYHwZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b2315c5d.mp4?token=Nes9S5SUJr-JQyONrLDxU6J35eRX1SCh6DjEefQEJdAsFvZYhIvQaXfJhDpp-b5-nDyuYUV-vghsd8yCv5_K7lSF6syUq91pzU_T0U0WXTHWsBEGd-HQXrpf5lje0Fs3_Loqe6cVkcJ35pDDnrXgXnMdRCAZxN4E7T9qEalZU81Uwose_N2qR0hbY0rnQ63TJJAlpcrPArmA0hxDXK8L74cCLLE_EJSxHXZ7V6ytC3IKT7jG7DjDEgn-roPEY9pnKpXZGRYwNNzUPaTYCUHzdKapEWyjmDuVQiFunmbbHhuIsdbJZFyx-Qd_U1qyh16pu25FMVSNdiA_3ZmUYHwZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صبر زینبی در خانواده قرآنی با ۷ شهید
🔹
جمعی از قاریان و فعالان قرآنی کشور میهمان بازمانده خانواده شهیدان مقیمی و ساداتی شدند که در حملات ددمنشانه رژیم صهیونیستی هفت شهید را یکجا تقدیم ایران کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/akhbarefori/652004" target="_blank">📅 22:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جلسه 47_مراسم دعای ندبه_سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">@masaf</div>
</div>
<a href="https://t.me/akhbarefori/652003" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه چهل‌وهفتم
رائفی‌پور:
🔹
0:10:00 چگونگی مؤمن واقعی در قبال ائمه (ع)
🔹
0:26:15 فرمایش پیامبر در رابطه با تربیت فرزندان با ۳ خصلت اصلی
🔹
0:36:30 ملعون بودن فردی که موارد شرعی را برمبنای شهوت انجام می دهد
🔹
0:38:00 روزه هوش و حافظه را تقویت می کند
🔹
0:44:45 علت اصلی منع از غیبت، نابود شدن مغز است
🔹
0:48:00 حسرت در قیامت برای همه انسان ها
🔹
0:59:00 ضریب گرفتن اعمال در محاسبات قیامت
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/akhbarefori/652003" target="_blank">📅 22:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652002">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شهروند آلمانی: آلمان را وارد جنگ نکنید
یک شهروند آلمانی در مصاحبه‌ای با انتقاد از سیاست‌های برلین گفت:
🔹
ما خودمان مشکل داریم؛ دولت باید اول به فکر مردم آلمان باشد، نه دخالت در جنگ‌های دیگر
🔹
گفت‌وگو اختصاصی خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/akhbarefori/652002" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhLKACz6_nBddFJ42RMGUjIYv53ZxHv54PaDx4WaJC_p4-ue1TpmGL3yRXLdkgoDHdILEhEcxHis_3gNA8FekamxUY8QTlIjZWMo4PP0gThEJ46GHq9RmtOO5M-nCx-TLPoWf1GJKDxMkyaDJ0SOtLHhdAz4tOEbMOP-fpybksAHVc075L29cygutV5BwLXlaX682LF5_ZyBfPUaFs4UIvOAVIfTn0tg6ws-_xgfY2uSCWqlJJw9kFHxhxWLrCvB2ZMt4lLSdAaGdZTTda_Oj6sWODv03MBWZVRan9fb_k2Y5qn5dNhKI5kMQfrGwEdnaqoAHVCA0dwMtilns5Je4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: بسته بودن تنگه هرمز میلیون‌ها دلار هزینه روی دست آمریکا گذاشته است
بلومبرگ:
🔹
نیروی دریایی آمریکا با افزایش هزینه‌های بسته شدن تنگه هرمز مواجه است.
🔹
تا زمانی که تنگه هرمز همچنان ناآرام باشد، نیروی دریایی ایالات متحده هر بار که ناوشکنی را از طریق این آبراه اعزام می‌کند، با میلیون‌ها دلار هزینه اضافی مواجه می‌شود.
🔹
بعید است که چنین گذرگاه‌هایی به خودی خود آن را بازگشایی کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/652001" target="_blank">📅 21:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652000">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12960aa4f3.mp4?token=gJOgEGadYwa1p1B29lR4zpiqa11eBvnPkhgSVZjQDkyosapzpONPUrd95i-7vDkgEd5VELt45_En057VQyDP50RyF5GGwcutVs9fgTwiDHYulTLtYgWJeCWTLAIcZlpRxB0YfAgFG6o6_j2T4k28heU7p5U2_u_L2_9eIibb1pgHZc3bfKUdSfodltaolpmL8PJhFb4W9w_1ep8hXK7I_7QprIHYTNLp-mFFNjEfXzbjRDDVOXPCEoQiAlDNukowa3Ovz3i65A4pSuWDk1n8C_n3ZI3BXnBcnsHgJJ78p2foZtVt_iSSzysgr_BpGAbZY8USHo6Qdo96dpJnwU1ob7c76oO51LjjLBmj0bTJR6QK7AP-7hSS3_L_LwApyqPMUwPeQOgG705d1b0Nr0se0tUTFJz006ncDm418ThdJLeeZYG8VPGDCdo9JFgDOcXr0xczW2KMY1qNqB4P9xmjNnUtk0oTr5K1AEKk74HrOJIRLkdtDixlp1hPKGLmR0lI7vIgi6HanSifnAmTqDRSy8NInHNW7n_kkNcir8KoBMydhvdmri4x9GPuSXTNvpS199ojnSLxBehst1808LC7VIzb7KBfa1nZUB9U1rFB053JrI6UwTz6pelX4UdjQuchEQgHaz8sL1H4MS2w0-ZURH3vGNzG6Gv8QZBHOZQV4eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12960aa4f3.mp4?token=gJOgEGadYwa1p1B29lR4zpiqa11eBvnPkhgSVZjQDkyosapzpONPUrd95i-7vDkgEd5VELt45_En057VQyDP50RyF5GGwcutVs9fgTwiDHYulTLtYgWJeCWTLAIcZlpRxB0YfAgFG6o6_j2T4k28heU7p5U2_u_L2_9eIibb1pgHZc3bfKUdSfodltaolpmL8PJhFb4W9w_1ep8hXK7I_7QprIHYTNLp-mFFNjEfXzbjRDDVOXPCEoQiAlDNukowa3Ovz3i65A4pSuWDk1n8C_n3ZI3BXnBcnsHgJJ78p2foZtVt_iSSzysgr_BpGAbZY8USHo6Qdo96dpJnwU1ob7c76oO51LjjLBmj0bTJR6QK7AP-7hSS3_L_LwApyqPMUwPeQOgG705d1b0Nr0se0tUTFJz006ncDm418ThdJLeeZYG8VPGDCdo9JFgDOcXr0xczW2KMY1qNqB4P9xmjNnUtk0oTr5K1AEKk74HrOJIRLkdtDixlp1hPKGLmR0lI7vIgi6HanSifnAmTqDRSy8NInHNW7n_kkNcir8KoBMydhvdmri4x9GPuSXTNvpS199ojnSLxBehst1808LC7VIzb7KBfa1nZUB9U1rFB053JrI6UwTz6pelX4UdjQuchEQgHaz8sL1H4MS2w0-ZURH3vGNzG6Gv8QZBHOZQV4eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزادی بیان به سبک پلیس آلمان
دستگیری فقط به علت پوشیدن تی شرت فلسطین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/akhbarefori/652000" target="_blank">📅 21:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651999">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf4175079.mp4?token=vytzHakEgF5VppyLPqCeAZBBgeHQwA5UGHUo2G7R9xhezKHUXrUQ5Uh_ycW3BJzw7mgXKOhDabwwSt4XdfNv30Rtk2Bb_ZHbRJ7WJ81T0saK3txmpA2-xUAz479uegEdHjhMrfD538iPF4EknOJXtPWZvv4zseqoum40kReDTasVYSC9kJA9ycHNuFQ0-iV-tfqTycuPyhTN_id1ff8YM7w0SH3h_pADOBzXaNWTw5N6K6H9IT41_r9QBOCvp-2hAmMRNht38alTNPSX6QR_sYlDoFU5JgJYaQN6tFzOpiLAqGzYhO4kzK6nUMgsTqlJN_6Dbofp9LCrKK37H-G5QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf4175079.mp4?token=vytzHakEgF5VppyLPqCeAZBBgeHQwA5UGHUo2G7R9xhezKHUXrUQ5Uh_ycW3BJzw7mgXKOhDabwwSt4XdfNv30Rtk2Bb_ZHbRJ7WJ81T0saK3txmpA2-xUAz479uegEdHjhMrfD538iPF4EknOJXtPWZvv4zseqoum40kReDTasVYSC9kJA9ycHNuFQ0-iV-tfqTycuPyhTN_id1ff8YM7w0SH3h_pADOBzXaNWTw5N6K6H9IT41_r9QBOCvp-2hAmMRNht38alTNPSX6QR_sYlDoFU5JgJYaQN6tFzOpiLAqGzYhO4kzK6nUMgsTqlJN_6Dbofp9LCrKK37H-G5QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: من نه به وضعیت مالی آمریکایی‌ها فکر می‌کنم و‌ نه هیچ‌کس دیگر. من فقط به یک چیز فکر می‌کنم؛ نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/akhbarefori/651999" target="_blank">📅 21:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
طغیانی، نایب‌رئیس کمیسیون اقتصادی: در حال حاضر حدود ۱۸ درصد از خریدهای خوراکی از طریق کالابرگ انجام می‌شود
🔹
نزدیک به ۲۷۰ همت از طریق خریدها در مسیر کالابرگ جبران شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/akhbarefori/651998" target="_blank">📅 21:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ایران یا کار درست را انجام می‌دهد یا ماموریت را به پایان می‌رسانیم و ما کنترل کامل بر اوضاع در ایران داریم
🔹
اگر ایران به سلاح هسته‌ای دست یابد تمام جهان در خطر خواهد بود.
🔹
همین الان می‌توانم (از جنگ با ایران) عقب‌نشینی کنم اما این را نمی‌خواهم و خواستار آن هستم که کار را تمام کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/akhbarefori/651997" target="_blank">📅 21:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz9ARr7axu6cETVBX9qKWUmkiA8gdWG2c3Me0ngHhrFtLeUpRaJdQYLoaxnFTPUyORhTkRNr1AaI6O-TOwZXhDB-qGFuoVbNAoN2AUMCHPflh70hxcsJh-XIGrl84RhAMb9JoSqr67rigCSPLmSNnw1DCOFsfEVCyxYvpxD_N1lGr3NROW8zhOWC_pgSQHvky-piuPwhzM4zNCI0y7Fi91L2QBE5BEBC5YHgp9tot0mp6lXdcbCp1XmsW6F58MVrLtfpS6aCmTbStuX00M6ylU9nfxygGUV2w8B_tNhDszRoz6EutDlKLNV6qF6GptTZ1Fa3Qo5CB3xyAAR5FVxT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت واشینگتن پست از فراگیر شدن حمایت از ترور ترامپ بین آمریکایی‌ها: «یک نفر باید این کار را انجام دهد»
🔹
افراد مستقیماً نمی‌گویند ترامپ باید کشته شود، اما برای آن یک عبارت غیرمستقیم ساخته‌اند. عبارت «یک نفر باید این کار را انجام دهد» و مشتقات آن، به میم‌های اینترنتی به‌شدت محبوبی تبدیل شده‌اند.
🔹
طبق داده‌های مؤسسات پایش شبکه‌های اجتماعی، استفاده از عبارات کنایه‌آمیز مرتبط با «حذف فیزیکی» ترامپ در سکوهایی مثل ایکس و تیک‌تاک نسبت به سه ماهه اول سال جاری، ۳۰۰ درصد رشد داشته است.
🔹
عبارت «یک نفر باید این کار را انجام دهد» به یک ترجیع‌بند در زیر پست‌های خبری مربوط به بحران ایران، قیمت بنزین و تنش‌های خاورمیانه تبدیل شده است. کاربران بدون نام بردن مستقیم از ترور، از این عبارت برای القای ضرورت حذف ترامپ استفاده می‌کنند.
🔹
بسیاری از کاربران، این شوخی‌ها را با استناد به بحران‌های جهانی مانند خطر جنگ هسته‌ای با ایران یا فروپاشی اقتصادی توجیه می‌کنند و آن را یک «آرزوی نجات‌بخش» جلوه می‌دهند.
🔹
این نوع میم‌‌ها، فضا را برای افرادی که ممکن است شوخی را جدی بگیرند، آماده می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/651996" target="_blank">📅 21:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnW9-wZwkCv6moZq_EXNHaaWf6S5q_CXiSbzyx2Xa0xrAEplkHki_zEjiThaibcXMz86sWqe10AE7MNJiaQi-U6BUoKnwqbpY7b-Jf9h0RBESAWvi5ci2NlTvfaerq1v17wr13vTJpeVL3pKsGPc-bNU_XUazAdzQ6mIKOcW4O2COWNcWmLJUzkS3Pc3fdWDl_wp__Jh6NHEsKlmB6rvnGeu13kqjxaKhsWFWp0qRzA7rTJmbp6fFi1IycGcusKTbV7wcpaPMdxbVC4YBibZEMPTCqZ-GnMYmvd6ZNNaJaY0Fluzg30HFNLRiBb4Ab4AwYkQhnxVEucKk6gdDkTO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید علی موسوی فعال رسانه:آقای وزیر بالاخره شما مقصرید یا اپراتورها؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/651995" target="_blank">📅 21:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
هرکسی که می‌خواهد به دیوانه‌ها در ایران اجازه دهد تا به سلاح هسته‌ای دست یابند احمق است
🔹
پیام من ساده بوده و این است که ایران نمی‌تواند به سلاح هسته‌ای دست یابد و هرگز به آن دست پیدا نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/akhbarefori/651994" target="_blank">📅 21:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ترامپ: از کسی در جنگ با ایران کمک نمی‌خواهم
🔹
هرگز توافقی را با ایران نخواهیم داشت مگر آنکه توافق خوبی باشد.
🔹
مذاکره طولانی با رئیس‌جمهور چین درباره جنگ علیه ایران خواهم داشت.
🔹
هیچ کمکی از کسی درباره ایران نمی‌خواهم و ما پیروز می‌شویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/akhbarefori/651993" target="_blank">📅 21:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تفویض اختیار به استانداران استان‌های مرزی جهت واردات اقلام اساسی
هادی تیزهوش تابان، رییس اتاق بازرگانی مشترک ایران و روسیه در
#گفتگو
با خبرفوری:
🔹
با توجه به تحولات اخیر، تغییر رویکرد از بنادر جنوبی به سمت بنادر شمالی و دیگر مناطق مرزی اجتناب‌ناپذیر شده است. به همین منظور اختیار واردات برخی اقلام اساسی به استانداران استان‌های مرزی واگذار شده است.
🔹
پیش‌بینی می‌شود واردات کالاهایی مانند غلات، روغن، حبوبات، دام زنده، کود، نهاده‌های تولید در حوزه فولاد و پتروشیمی و حتی دارو از مسیر کریدورهای تجاری شمال کشور، به‌ویژه کریدور شمال–جنوب، افزایش یابد. همچنین با توجه به ظرفیت کشورهای چین و روسیه، امکان تأمین این اقلام از طریق بنادر شمالی فراهم است.
@TV_Fori</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/akhbarefori/651992" target="_blank">📅 21:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cROZm5KGidT0UjitskaOvOC-Ue_AHqdFLQrj-eMO2-jPFVqMHeaYpKpDXp8kiLgEPFFj3uejOYdU4VxgHpiYdVeGZcmggeIqOXBOD_fv3NkT9qX4Y9eqNCUyxtZe5Na-HyctQjHNp9H5wSgGl-aBOGYRKkuLy3wsmEs7UUxNT3dIXjr2vCjLGqkodCnqbt2zOm4w5vNQOFsavZl1jEsVS83o5zrzodzNBZLWiYoTW68B0rma85Ph8fiBNuN-5NwEoSCZHlIf20PidKcPKlVQAjyHIZqX6MyHbpn6pBzOkISVs0TiGSf1tehU0SgiozdQJ3XOHznXr_8kWOioiZmrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای بلومبرگ: امارات با هماهنگی اسرائیل دوبار به ایران حمله کرده است
🔹
بلومبرگ شامگاه سه‌شنبه گزارش داد که امارات دوبار با هماهنگی رژیم اسرائیل به ایران حمله کرده که یکی از این حملات پیش از آتش‌بس و دیگری پس از آتش‌بس روی داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/akhbarefori/651991" target="_blank">📅 21:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651990">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا و پیت هگست، وزیر دفاع آمریکا، هر دو از اظهارنظر درباره گزارش‌هایی که ادعا می‌کنند تنها ۳۰ درصد از توان موشکی ایران نابود شده است، خودداری کردند
🔹
هگست گفت: من اطلاعات درز یافته‌ای را که ممکن است درست یا نادرست باشد، تایید نمی‌کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/akhbarefori/651990" target="_blank">📅 21:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651989">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQlH-5E3JPw7feUvVzOvFfeDJSPIlULiHSXl6AB43C0VSm7tVyeNfzwcwZw0WdgWgPXNbBjh72XtuNZpG_najdy3-plFiq3yRI2HRRiSfMbcz35deNXpkOAUXA2CrnlYzL3ofoV4_uIj6P-IkItq6ljNg23u6v4kpBXOUb6TlQst0OsmL_DmniUcvBBtghd1jOXpzwaiJIB6wV90jO3eSsvWb5J28D8Jp6088HpiyVhPT9uax2qZUX42kCGknTfQFC7PB_4pmDlNwPhkwHywdVRHj3stF3pxt6Ujjdfkv505nlE7NAEsqDE2BUvyK2-ZEklv59_KxXpgsMHv9DD7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح جدید مجلس: میانگین پرداختی کل دوره شغلی مبنای حقوق بازنشستگی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/651989" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651988">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
لارنس ویگر سون، افسر بازنشسته ارتش آمریکا: در حال ورود به مرحله‌ای از این درگیری هستیم که دیگر راهی برای خروج‌از آن بدون تحمل تلفات انبوه وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/651988" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651987">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O64A1YNkAIT2spwUHIUgyvQl4_S9vnzcxP4u7dapl4qiO7cIbWlH4vp8ZplMUInF_6rGi44MPejhTYh17IrJ4GB2a_RPgaCDydOaVQoTGXyu1emmxcAnqIGuuUH-nFFeezzEs-tI2gbQAZEXzUaD6dx1fDOU6ar8kqpotCJ4y3KFOYOSPfzv2QZ13SK846iyS1P50EyCwxUHojJZ4f5RgNoA2FqSb4lekyyVSB9at9vBbwzoPnGm4487N37GGi5zHnxkk66yzXtta6AttV0HYo7T0JPLf2pS9z7dalN-FhCHQ5CbM5dPm3fj7tOwHyc3xZd6KdSV1UtkATOZwwSJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: تاکید ایران بر اصولی روشن است: «توقف دائمی جنگ و عدم تکرار آن»، «جبران خسارات»، «رفع محاصره»، «رفع تحریم‌های غیرقانونی» و «احترام به حقوق ایران»
🔹
معاون وزیر امور خارجه: نمی‌توان هم‌زمان از آتش‌بس سخن گفت و محاصره را ادامه داد؛ از دیپلماسی گفت و تحریم را تشدید کرد؛ از ثبات منطقه‌ای حرف زد و به رژیمی که منشأ تجاوز و بی‌ثباتی است، پشتیبانی سیاسی و نظامی ارائه کرد. چنین رویکردی، مذاکره نیست؛ ادامه سیاست اجبار با واژگان دیپلماتیک است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/651987" target="_blank">📅 21:02 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

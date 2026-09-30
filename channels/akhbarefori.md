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
<img src="https://cdn4.telesco.pe/file/rRy6W8AufzNDyFrtxpqDP6zFzqvpCBS-O9HoYtZBgn6QEBoXSEwfqn9x4vVifIL_XE1JFYNXSXyfPOiaMqmlrXrjFq2B3UIlL7HYKnywPp4rHXXW4D_sA52x626WjCh8hMlKHbYg15Ay8W-xHnAh5FAtv2z1B8Kuwk11j0L8pAxKjPcv4waqGQAWOc7f9byRIGbBfpb_gH21hN12oHtgiY-JAyJfD0XzauWYpo9anXwXtknPqGRRCKxx3Xcs0NDgdPXsARtcoZDxbioDeKOk2v1KFu_lzgGWPBgo-r3wIzL1igCcAQ-pe-mr-30_QjMsKnhJETWxuGEW3BqdR40REw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
<hr>

<div class="tg-post" id="msg-694194">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
افشای سناریوی جدید موساد برای فضاسازی علیه ایران
🔹
بر اساس ادعای منابع امنیتی ایران، اسرائیل قصد دارد با اجرای یک عملیات تروریستی و نسبت‌دادن آن به ایران، زمینه‌ساز موج جدیدی از فشار و اجماع بین‌المللی علیه تهران شود.
🔹
این ادعاها در حالی مطرح می‌شود که طی روزهای اخیر نیز گزارش‌هایی درباره نسبت‌دادن برخی حوادث به ایران منتشر شده است./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/694194" target="_blank">📅 13:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694193">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY4TALK0Bv_0Lm-uyhlJVp2YpbTeKZIf2Gjf4Y8b29aPuIVCWHLr_N2Q2-YY06E4vsm7ynGv4MrhidQkLVJKstj8nB0ouHxYmNpWLWxmbi7cuxbmOt37-Arj0Ut1uIGTwvBDk49dpuO7hVa2SKdOpQdf3I56XaasdSps7cgjdZY4cpZa5OaVX8elPFFrRB4t4S7wAhDPxRSLHYchsRBLEO2ptvxoJsXa9nGmpQ_MkELNq5un43hO70K2ZagYEfhDJGlkKkzyPWbaYa90_AwWcgP7Hc1dnAFnWR8uC8xuYwVxbZW0wPWefbxx-bFL_qDTqFi4qaChzRb4pvdda62NuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشتری مداری در گیلان ۱۰/۱۰
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/694193" target="_blank">📅 13:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694192">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
شوک بازار موبایل؛ قیمت نصف گوشی‌ها بالای ۷۵ میلیون تومان است
🔹
بررسی ۱۲۰ مدل گوشی در فروشگاه‌های آنلاین نشان می‌دهد ۷۰ درصد گوشی‌های بازار بالای ۵۰ میلیون تومان قیمت دارند و کمتر از ۷ درصد مدل‌ها زیر ۳۰ میلیون تومان پیدا می‌شوند.
🔹
همچنین نزدیک به نیمی از گوشی‌ها بالای ۷۵ میلیون تومان قیمت‌گذاری شده‌اند. میانگین قیمت گوشی‌ها در یک سال گذشته ۱۳۵ درصد رشد کرده است.
🔹
در میان مدل‌های پرفروش هم گلکسی A17، A07، A16 و A56 سامسونگ بیشترین تقاضا را به خود اختصاص داده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/694192" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694191">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
سخنگوی سپاه: در هر ۲۴ ساعت در تنگه هرمز درگیری نظامی وجود دارد اما مدتی است که آمریکا پاسخ نمی‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/694191" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694190">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu39uCC6QtkII10zeRMskuOf9tek0Hf0ofhvXgqLYz5KOgVgJw-oEnDBE1bMXrMlIkpYjlkmA9kZOZcR6YuCYHb0qXTsxMklvIg_CTI5mzldIDLXM8nXHykdo0NlDuNSCoGmew9JA9sIVXd82YBwzEwGFXX9CiY757tB_Ub-8JtwB8NF7MSWfYG5tNxETNxnQVRZcU4LaHoIpsEWixoeaUadU0mEt4EgIZcPmGG3-1qvU7F_WC3AIpP1oAs89v-1YlCD0u_ljYn_v-l1WkJeUvUedleipgIJSzWLyKPVal6-ayTQoA26yHNjx5vNgtMuy61SPzjvGaRAN0MfDbzlLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی انگلیس: یک منبع موثق گزارش کرد که یک نفتکش در تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناخته قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/694190" target="_blank">📅 13:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694189">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
«جادوگر فوتبال» به پنج سال حبس محکوم شد/ تشریح جزئیات فعالیت محکوم از فدراسیون تا وزنه برداری
🔹
رئیس کل دادگستری استان البرز از صدور و اجرای حکم قطعی «جادوگر فوتبال» خبر داد و گفت که وی به پنج سال حبس محکوم شده است.
🔹
حسین فاضلی هریکندی در گفت و گویی با اعلام…</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/694189" target="_blank">📅 13:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694188">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
اعلام انحلال یک گروه وابسته به جریان صدر
مقتدی صدر:
🔹
با عقب نشینی ائتلاف (آمریکایی) از عراق، انحلال تیپ «الیوم الموعود» و تبدیل جیش الامام المهدی(عج) را به موسسه انصارالمهدی اعلام می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/694188" target="_blank">📅 13:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694187">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a69b7cd1.mp4?token=JokIzI6N1eDSUXgvUIXEDa-SoPKObbMxav3r7BRnlhQZJ7bpKV4XpF9x-r2IaDUPbCsoKvVeOefo-H1yT_k3vW7leCHyEPM6DgIxe1Dp8qV8OndFw0dwLzi6eLkOzFXQjRHX6lpr5wHwd3tx9wF3UHjJ9Ziozh41T3zMxl3EZf0mnhUw3a6NCOLLdkznoXAHuNv5Yg2R6oJdxjuXwiT1XZdQUNoZAiuICDYfhDshK05CGLvBHUZWhdvs55sNz5KQobdhzU9YJabfhyYxOXuNZeVgah_cndUvWC_Hz800iWHZSDG7YwMfLoaBOcWSdcJom36_9wr1GykVa5OygAhWlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a69b7cd1.mp4?token=JokIzI6N1eDSUXgvUIXEDa-SoPKObbMxav3r7BRnlhQZJ7bpKV4XpF9x-r2IaDUPbCsoKvVeOefo-H1yT_k3vW7leCHyEPM6DgIxe1Dp8qV8OndFw0dwLzi6eLkOzFXQjRHX6lpr5wHwd3tx9wF3UHjJ9Ziozh41T3zMxl3EZf0mnhUw3a6NCOLLdkznoXAHuNv5Yg2R6oJdxjuXwiT1XZdQUNoZAiuICDYfhDshK05CGLvBHUZWhdvs55sNz5KQobdhzU9YJabfhyYxOXuNZeVgah_cndUvWC_Hz800iWHZSDG7YwMfLoaBOcWSdcJom36_9wr1GykVa5OygAhWlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از مراجعین کلینیک کاشت مو در بندرعباس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/694187" target="_blank">📅 12:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694186">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
محسن برهانی به جرم افترا محکوم شد
🔹
برهانی پیش‌تر درباره نحوه ورود بهادری جهرمی و برادرش به دوره دکتری و عضویت هیئت علمی، ادعاهایی مطرح کرده بود.
🔹
پس از شکایت بهادری جهرمی، دادگاه پس از بررسی و استعلام از مراجع ذی‌صلاح، اظهارات شاکی را تأیید و برهانی را به اتهام افترا محکوم کرد.
🔹
این حکم در مرحله تجدیدنظر نیز تأیید و نهایی شد و با توجه به پذیرش اشتباه از سوی برهانی، مجازات حبس به جزای مالی تبدیل و اجرا شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/694186" target="_blank">📅 12:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694185">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سردار جلالی: زیرساخت‌های امن موشکی، حملات دشمن را خنثی کردند
رئیس سازمان پدافند غیرعامل کشور:
🔹
با اقداماتی که از قبل در حوزه پدافند غیرعامل پیش‌بینی شده بود، از جمله ساخت شهرک‌های موشکی و استقرار زیرساخت‌های موشکی در قالب زیرساخت‌های امن زیرزمینی، حملات دشمن بی اثر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/694185" target="_blank">📅 12:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694184">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b160b90c8f.mp4?token=WV4cAp23jFapdf_ioFoRijRjK2DOlZ_iUA7ZXKJ5upY0L9oklj9vVOd3OvUv9yeBclnju5tY5qwdoJ5RyITIsK5J1GXko0hGOkYcRgkvuel3GEM6m0mIXg68nyN7zkBUAegtpux3PgEwqATWM2xN-g7SSTyHHRaKXt-2hF4d0g1X6a8NiFxIPxIbJmxMoaBwGrFpexdz2hYACEQk0AqL4LpMFjuD6DExKu312nGFNJhQO-cpcMQO8qz5F5qShmj660uYnJabcD9ZZnmij0IXbhOSMoZoJrqfu2aAjP8GCbP787xZKQf3rd3EQYCp_l_l0uoiw6lkP-ODvH2mqjnO9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b160b90c8f.mp4?token=WV4cAp23jFapdf_ioFoRijRjK2DOlZ_iUA7ZXKJ5upY0L9oklj9vVOd3OvUv9yeBclnju5tY5qwdoJ5RyITIsK5J1GXko0hGOkYcRgkvuel3GEM6m0mIXg68nyN7zkBUAegtpux3PgEwqATWM2xN-g7SSTyHHRaKXt-2hF4d0g1X6a8NiFxIPxIbJmxMoaBwGrFpexdz2hYACEQk0AqL4LpMFjuD6DExKu312nGFNJhQO-cpcMQO8qz5F5qShmj660uYnJabcD9ZZnmij0IXbhOSMoZoJrqfu2aAjP8GCbP787xZKQf3rd3EQYCp_l_l0uoiw6lkP-ODvH2mqjnO9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین باران پاییزی، مهمان بهشهر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/694184" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694183">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ویدئویی از لحظه فرود اضطراری هواپیمای فلای دبی پس از درگیری در کابین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/694183" target="_blank">📅 12:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694182">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سخنگوی سپاه: در هر ۲۴ ساعت در تنگه هرمز درگیری نظامی وجود دارد اما مدتی است که آمریکا پاسخ نمی‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/694182" target="_blank">📅 12:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694181">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2982e2925a.mp4?token=Y_h2CI9lDfqBH5RXvejAcdjU3QiC6mbbHUTtTPwL-Ctl-e80fcZeRGIt9z3AM8-wqrBFcdlTpBEYUn-tmAJOJgpy8j8mm28jWB7HQkWuuJR8jNmBHunBeyGC1G_dhv65pd1T5Av52EXtOH4AjATOSyXKfgVJtAx_ZGC1-tNd1elzQ939WLForUGuCMNpaV3pkuLlA8t6a9wjDDvn_HZzeH0xjyRABdnlTDlsrsRUV5a8rH5wYN7w8ZAbP2HCLyzi0-yhIU0cJ0W7TJyjql62r-ym0BfSoGYfltPO7KL1ZvwWV9UvirKzEEDzzvMd6iBQtUW5hujgaVWAZSK3q6mQzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2982e2925a.mp4?token=Y_h2CI9lDfqBH5RXvejAcdjU3QiC6mbbHUTtTPwL-Ctl-e80fcZeRGIt9z3AM8-wqrBFcdlTpBEYUn-tmAJOJgpy8j8mm28jWB7HQkWuuJR8jNmBHunBeyGC1G_dhv65pd1T5Av52EXtOH4AjATOSyXKfgVJtAx_ZGC1-tNd1elzQ939WLForUGuCMNpaV3pkuLlA8t6a9wjDDvn_HZzeH0xjyRABdnlTDlsrsRUV5a8rH5wYN7w8ZAbP2HCLyzi0-yhIU0cJ0W7TJyjql62r-ym0BfSoGYfltPO7KL1ZvwWV9UvirKzEEDzzvMd6iBQtUW5hujgaVWAZSK3q6mQzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حناچی: رایگان کردن مترو تهران کار درستی نیست!/قیمت واقعی بلیت مترو ۱۲۰ هزار تومان است
🔹
پیروز حناچی شهردار سابق تهران، در گفتگویی مدعی شده که بلیط مترو در حال حاضر  ۱۲۰ هزارتومن است و از طرح فعلی شهرداری تهران مبنی بر رایگان بودن حمل و نقل عمومی انتقاد کرده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/694181" target="_blank">📅 12:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694178">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baaa134ef2.mp4?token=iqp-djGw2dUg51fV3AFLDDzh1R-uYFGPEFTrg8iiweunbV_eSafs6VnsbLg0kH4ZZjH0YvMUDfq91Jg8-m3zM_XcQ7rRdO8GhOEXMV40pRgbpXn4_JRT-Td6c_vzZAXPiKx7NnspC9m-4NAkkBfzlaSiZWmJ_h5qpBG5g2nNGlPTJ1YXKXpsGpcdDwXu2HYRosUdWvWNl7ewpqokMiM7JCViFIUqk-DjK4RMBRPbFLtCpuH2DuYn4OGZO932i93wkLxLjt-tXwenZEiJDYq6yWlDD-yk6vc0Lg1ZF2OS0-VCdrSAYghmBpraRefHmUelEUN9x56NZIEHk9yoyPoqlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baaa134ef2.mp4?token=iqp-djGw2dUg51fV3AFLDDzh1R-uYFGPEFTrg8iiweunbV_eSafs6VnsbLg0kH4ZZjH0YvMUDfq91Jg8-m3zM_XcQ7rRdO8GhOEXMV40pRgbpXn4_JRT-Td6c_vzZAXPiKx7NnspC9m-4NAkkBfzlaSiZWmJ_h5qpBG5g2nNGlPTJ1YXKXpsGpcdDwXu2HYRosUdWvWNl7ewpqokMiM7JCViFIUqk-DjK4RMBRPbFLtCpuH2DuYn4OGZO932i93wkLxLjt-tXwenZEiJDYq6yWlDD-yk6vc0Lg1ZF2OS0-VCdrSAYghmBpraRefHmUelEUN9x56NZIEHk9yoyPoqlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌پرده ادعای نایاب شدن دارو؛ موج‌سواری رسانه‌ای روی استرس مردم!
فرامرز اختراعی؛ رئیس هیئت مدیره سندیکای تولیدکنندگان مواد دارویی:
🔹
کمبود فعلی دارو از شرایط عادی گذشته هم کمتر است، اما ادعای کمبود، بهترین فرصت برای اخذ رانت ارزی و بودجه توسط مجموعه‌های مختلف است.
🔹
بدون نگاه علمی به اولویت‌بندی داروها، تمام ۳,۸۰۰ قلم دارو در حال تأمین است؛ رویکردی که نشان می‌دهد بحران واقعی نه در رفِ داروخانه‌ها، بلکه در فضای رسانه‌ای است! / تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/694178" target="_blank">📅 12:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694177">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBblHo10w-HnMlxqobSQygsf8JxXJe7wWPaDreMxLNZpLA_4KxMTcxpZ6A6buFFbEU0OgHuIhfoA62Tgk4-G4KIDAXzBJuavpM5EVroSFhm7AJujIbUs8p1Wi00s7EgybnZqoKS3tqY2C-Nxqms_mwvrOQxnRwR2CsCRg1MLVauOuvpGL6SMPurvhsTRfNesbv5ALLMzCxhS26-UpZyNdFiwg5S4dkW0EGWm-EoKkT6XvbXfuCFdIPw3o_MXBV0dTGCBa51YzpuwaxwvjvPRW4pCaxHnINQt2p83RmooGetHZdjvYEOxipJe4alsFxOV6HmgPZV5GRdZ4ftkFfHTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۸ مهرماه | ساعت ۱۲:۰۰
🔹
اصلاح ۵ هزار تومانی قیمت تتر، اولین واکنش بازار به برنامه بانک مرکزی برای عرضه اسکناس ارز بود.
🔹
هدف‌گذاری برای عرضه ۲ میلیارد دلار، فعلاً سدی در برابر رشد قیمت‌ها شده؛ اما پایداری این آرامش مستقیماً به توان مدیریتِ سمت تقاضا بستگی دارد./تیتر تجارت
@titretejarat</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/694177" target="_blank">📅 12:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694176">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سخنگوی سپاه: در هر ۲۴ ساعت در تنگه هرمز درگیری نظامی وجود دارد اما مدتی است که آمریکا پاسخ نمی‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/694176" target="_blank">📅 12:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694167">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aT3roVPDBA4A-y-NTY3RCJdmgeUyMAsF48QwGGoo4Ku7H-yH3DmmCnSqshyBRQTkaI1G_4H0KqSwXgMD6joOqNoZ3BeLqWO9BbFs14qRqNL_x94_JItWjfhN9ior-ng2s3-mriKqu-si0RYACe4qu0kRDM0n4JV9-nUrMn_Pwg4J0jNSjGxaOA2F6UtBzIwoI22Ms37U73DCkXL9Vt8MokfbBHWU1KgOn9_OUVSuv7pwu9bKB0sYpZcnSw28tPnmypabHF4LT-Eil-UiEcpIOQF5bf7DQ72EMYVsjraiuXQ7xpuNqA4uYFD4T9Bvrhxrgv6hPeJ3xvAXQRYDftqFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_vb3Ov7onQk1hxFyFNJ0tBH7dbxRjQGjcJTI1YgFD7Fum-XRntHAsbw0nFKP04YT7gMWE1ZvbJiA4jLN2yv61pMwKirCZMIuGGqMA0_WEsoQmNnkR5K1vSmZCfVcHjFwpqb7_UOABmEZrmQRyJwFDqlJoT1dNLcvpLoWzh4oVB4tXzaxwBft3HkhVmVnyKb1UKUC6J2eLLwDzagPW-FFRopW_yC1M4as24ZpjokGYnOLdGP3kqLM7iKz8_Piy80B6yD4sXdaKU0xt2pTdpv7An2J1yzpMxsOwpy-2DOjorGakz6gvcZTcBjazqJE0CbdzOtxcHVS_2aOSZwxtxc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnxZJvMXuUbCdgwqhKCrcitrIytuIW-dvVhWUvxOLJ-1CpMuSuJ8gF_2ziexgj6YGGKAOpRsrxJJ2fUHla5KrATnNka7wnFdo8Btdf3_GE3gvcHeSon9fab76cE7yY3oxgTwONNScFN30EqibpNxpYHXU4B9M1TofRsDHlUgHi5XfKPFgL-NbtuYYUM5sIGYvg5IcV-4kLUVMWrEg7ND_2QcNqmt0Pj7pPzlfy-SFNt8k5b0P8mJ3a6foxnHbPCpYWKvXwIcBx9iFBXQyTGw06kKhz3i1ZHsRqC0uUThY_6UGIfJZX5Pue0dFf3NugC0rLOmLpSX-4tEBdlP7kQbgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HafMtYsapBb98StNzuQ79Uw49TmtAhes3Ndhy14R3K2n9Edf4Rx11LPkvi67WGIJC30Wfk2NTH4r1ZBvAkfI-BWz_2nOPnuO5fbGGqoLKpHiT6wocFVE2ECqKh-RpW9A81eLHuVRWc6Q2IpkvDQi3jvHcnbnp_PtVcPHTdFcX00B0F5nOsTx1yFiA1AyQQMPQIlGRNjOHcrlqiXuCoiGxzSNx_2pJsVJ7zar_khpCTO-JCSlLsXRIMkPh8WFckTXk0eiJP2oisIyPu60g4PWT4f6BQAhR9IT2o_yBMTdo8f806FKPeGkS9h97JsgQw5BOa-oFyAKjKh2ABFzkuRwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpJw-ABVWM5EoRBSBlfQLhncmhM87g7J5PPzBJplHbWVDnzTKke9doCGZT7BihDdn0odSrW-SIYFda60cLJJas7LlEXKPmiYPKUd4LlOQWLV60515D4IupBTweucg4Ad_J8EcPegfQcLyo17EL7uk4-ZIJC7cXtR5pJO5pvHKdKl_pJIokvGU_16byL8U5Ktr4MZeHlBrqPmrmA34BnvqQv5eSGdX9u9Q7YtW3DHu4O8yuEwjscOV091mNSkzxTJTg7VdVEk4eI5_RqhqpIGj8oQlAl7ryeVXIAcV2d44mX1yYo59OHWpVBli0Cw0wYctscev3ddTqgd3b-pVvi-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NT3s8lw6702P71c1PbVyquZpSTpR4eVzsxfRpcZo716-4cKdCZRT2rYdadW6x06gtJxyPN9o5AfiAooFlKPy-9XfQ6ItNOpYIHHA1-DKbHYj9uolAbW6kHOc2rCOLmuq94b06en2WN6yOJaRwCx6LjN_WN07DbxQNT5Ija2ZUcY0RBJ_ej2GLOA4oxsfR-neW3EUToJFUSyJpG1_5VJlYw8zOYSSXsPpgTLbLnedVeJIE8kZnFMaeSOUJJrH2_8Cy4zrsaO9TrJ7ZI5ygf174eAKVqI_L2w1daXY0J24MjRjYuHkr4gVVZgSWx25PqYIB7kXgbN5oHl0l2ZVwoFEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmoV82V9c04SlsvQXw3-Syqa0nDh0KEC-0Mdm4TkwUd1Yr78b5_zyUoYCT0ty7qZetmqedEQxuVk1O3tSTAgYsmSlLOUPsq_kZYLYy2YUhZjTziZyi9ayjPK2r_2D-kqNqIGjUQcniMouSKgN3XrAJ6yEVKcVgFqFYCfHtPY197X1preDdvYM1bOxctFABfrQBcGlINNKjJE958vcX9EEsV_LavpdsTqOPwGMAQBR65DpbXsdUfBctID7BFgjwcxvhTzsKluknRvxCpIOaU35TTzarnyfuzQd0gOFiEWN5zM9GSvkdQBKANCElsdAA3aZo4DDvz-sChHNtxOsxD-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtU_FjtNjJn2D6R1Ao_LHsZYJRnvZFUGv5LEIwRfaC5JU0vxMedPP_jiwDbHW_cecht6KzxHyMjES8MXhP6_I1gRXcL-Ck4ADgi8BQlbXi0EjMHQvlEpIaMdDRIsXsRE_B89EE1a8AR90A9y-yhzMAk6fxK8xDLn7TlCG0BDiz5fFg6jm8IT_abZyJ-nZmImJCATLk2mJhIk6zbEkBSADZ81e7sr8I6YM-fWjEPYDyEru-EEIr43w2D2tAe3FcKeORay-0lSVUwoUbgBrmgV222XKJl8c1Qi8e0FBEO54PM2Qfq2qWgS4yfzr32iywp4GXiTo0B0I4T-GpL_k1yb4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-kLLDpTL4H7J1Kf5r6AcTB-JdBCMc_baZCGiFL5WRxCYKy4yDjLI64Yu3nJnrYKvmQ4NMWYvOW7qZEnz_wFUtQLHp3Rp6H3bYYd8WrOCELcBQW1lg7s4SFxkPCD3LGWTJkwwLvx0KIPQBpjNs2lCUoJ1VxfPxttw-hbip9ylrHmTWrcpmIUT253lDlCtAcrHHn1zkQ44thnwLHJWS3W66cPYsqo-F0z0N8HGVlsy-TUAE8MsIWq4qFTEQUaosSG0MC4xt95EPhNaGTqQWbQ82Zpy_aK7QWOVYR3Co6PCIl9CKB4HgFFpPz11exGeSk2uYy-RPRclKUJvcJ6usrnzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۶ عادتی که تو رو مقابل دیگران بی‌ارزش نشون می‌ده! #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/694167" target="_blank">📅 12:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694165">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0GcEqRDw1ytWj1ObeBuc6vuHm6ik4jCam5jNULBdqzkIxkQGnNhRkZBDscGSvz_XsJ8VF3oIiHERMXlbwjOCLXJ8YgN8ZQNYBfxBkHeXdZzWCV5n0uklxRmqLVnyjPlQdNi15UBSw7iQGBxNPwQIaqUASnc3zGC14YhstQv7SAajSGfALMvcI5U2Xv8Wkyp50cznU06K5rhggXrYe3cKubiHIY1vFFRtoswfUexI78J-4XGoHT9W8944oEt0lmsuWkUN_IBEu-qpuduw5bS_X9QzY-l2zTjRoevBKSXpnBi0DiX3tuV4u7wzepavrG8WR3zAmuTTdV5XgZFACVJww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع بسته های حمایتی لوازم مصرفی خودرو در سامانه جامع
شروع طرح از ساعت ۱۰ صبح روز چهارشنبه ۸ مهر ماه تا اتمام موجودی
هموطنان گرامی می‌توانند با مراجعه به سامانه رسمی ایرانکو اقلام مصرفی حمایتی خود را به نرخ مصوب با محدودیت کد‌ملی دریافت نمایند.
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/694165" target="_blank">📅 12:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694164">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b002cdb603.mp4?token=rvTEiL9tGzob-BOA7t3BwcwWyOLA4zdFhkrLcnkr3BPzTT0-QVcMkPNg1hh4yczClNp2YXsRJ1W6Qll3ZkPagRHnMIg1U_ygF664FG2tRooq4qbkoWuJNTSb1ceRzSIrty0QBmYmj1LuS_m9LYT-9Al6l1tW8y7oGfpsFrTfqMWYVx8IVNKNlQ6PRn0qZNgqPGFSfwQnVdnIis7sZHr7qsTHT45Opj1puSwP7nlEVyd4lc2hdwj_8aFXorWPSU8_v7P84jRbZlWaQHSjGQ5-zCEEL9c5JwuuCPQpMugs27M1qI2R5iHn3QR3A-KFkuDts-o4xchewWHJ-A22jefg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b002cdb603.mp4?token=rvTEiL9tGzob-BOA7t3BwcwWyOLA4zdFhkrLcnkr3BPzTT0-QVcMkPNg1hh4yczClNp2YXsRJ1W6Qll3ZkPagRHnMIg1U_ygF664FG2tRooq4qbkoWuJNTSb1ceRzSIrty0QBmYmj1LuS_m9LYT-9Al6l1tW8y7oGfpsFrTfqMWYVx8IVNKNlQ6PRn0qZNgqPGFSfwQnVdnIis7sZHr7qsTHT45Opj1puSwP7nlEVyd4lc2hdwj_8aFXorWPSU8_v7P84jRbZlWaQHSjGQ5-zCEEL9c5JwuuCPQpMugs27M1qI2R5iHn3QR3A-KFkuDts-o4xchewWHJ-A22jefg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از لحظه فرود اضطراری هواپیمای فلای دبی پس از درگیری در کابین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/694164" target="_blank">📅 12:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694162">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پزشکیان: تمام تلاشمان را برای به سرانجام رساندن تفاهم‌نامه اسلام‌آباد به کار می‌بریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/694162" target="_blank">📅 11:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694161">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69be3d1748.mp4?token=KjI4KmXBpOmTTp04NVJTJ8qqZPuZvBfBHcVeV1WwpqoGPMrcl-YEd0GIG5dDLiAAsqkGQhBwlkO1PsZ531Bs9ro2NxLFvsNB1NKNEz9CHdnVq9T5kG2atvCPnua5szZq9HWlTgG2WRNVW6mq0n3nX0AysOQrG3X1lgyubOTOAc-OziKdoakDagiKM0y2_wLqlVn0lHCIDX3VpcXGsN2pv3ZUxy5PSib90ynH6BasEQMLxoc31hmM5AaI-IPt4AOtmwLBQkYf2uabJVeCyaLMDkaD_wFwgI7eaHfhmnOjaUbxYleDubVMkM321HGZUmU530KvC6gd17Uz66ozsmTKVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69be3d1748.mp4?token=KjI4KmXBpOmTTp04NVJTJ8qqZPuZvBfBHcVeV1WwpqoGPMrcl-YEd0GIG5dDLiAAsqkGQhBwlkO1PsZ531Bs9ro2NxLFvsNB1NKNEz9CHdnVq9T5kG2atvCPnua5szZq9HWlTgG2WRNVW6mq0n3nX0AysOQrG3X1lgyubOTOAc-OziKdoakDagiKM0y2_wLqlVn0lHCIDX3VpcXGsN2pv3ZUxy5PSib90ynH6BasEQMLxoc31hmM5AaI-IPt4AOtmwLBQkYf2uabJVeCyaLMDkaD_wFwgI7eaHfhmnOjaUbxYleDubVMkM321HGZUmU530KvC6gd17Uz66ozsmTKVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راننده اشتباهی گاز داد و وارد کافه شد
🔹
در استانبول، راننده یک خودرو به‌ جای فشردن پدال ترمز، پدال گاز را فشار داد و وارد کافه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/694161" target="_blank">📅 11:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694160">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-ckeW_uDKZyELNu7_34YGca6GkNEojV7dVBXOFTuEK6v7xKMQ7APLBoEVcmG4Nm1xHLPTpcym7g9ZpzNNMlHTHmVgJcDNvIaWe84ej19AMc4LiTirWJQVfi4xx-Os4K2nrk0GK4R-HbUiuQBneuN17HEYrfgrzJpGIpnzm3TM8m_fBtMisUqwr724QtLDbZ3HSHhG-Q7pURIQcLvAPlbpv5rTMLY9FGqaZZV4axjWdFbVVpUfbM_5PMmhAJP2VAKzu2PsOtz9s58hgP0_0kWv4D5goEehMAuujGBFUD9GqmJCVJy6geYv3sDzH6iOwygb6V5tnCo6XJPJmQ_z3YdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
قاب آینه و فرش متبرک؛ تکه‌ای از آرامشِ حرم رضوی
این قاب، تنها یک اثر تزئینی نیست؛ قطعه‌ای از حریمِ امنِ امام رئوف است که به خانه‌ی شما آمده است. استفاده از چوبِ مرغوبِ جنگلی (همان جنسی که در مصنوعات چوبی حرم مطهر استفاده می‌شود) در کنار فرش متبرک رضوی، این اثر را به یادگاری بی‌نظیر و معنوی تبدیل کرده است.
مشخصات محصول:
🔸
نوع فرش:
فرش ماشینی متبرک حرم امام رضا (ع)
🔸
جنس قاب:
چوب جنگلی (از جنسِ به‌کاررفته در مصنوعاتِ حرم مطهر)
🔸
ابعاد:
۱۵ × ۱۵ سانتی‌متر
💰
قیمت اصلی:
۹۹۸,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه:
۸۲۰,۰۰۰ تومان
📩
جهت ثبت سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/694160" target="_blank">📅 11:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694158">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qF0EytRxaPujrFY0j42g-uQUJGBXPqxEs5gh0nMEboLPhiMAuIg8e1_d0EreGzZYkqFRhpSnvr3a93DFRxvBramMOwsL16u68yG3iArXq7WfNReLhTl451A_tFF3-k3R3hQ517qseawJqwPdZ5hhPCYsY6-LlAQL17wPf9YVL-L8uh0AWIvglst7JBB0P5ag9Vzh_3fsCVX9uaYx-03hcOBjqZHS9nCJcT-r7hbDrMwAUWtCx_n7UN522R93L7t_36ymY0SHkTA8ErHuDoqQlYb6MEitqCLN7WADf8hnaLCnnKwY2ctR414i37kDYjnsh8pTi2kAq1VCDfL-XtM3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1yueCwGL-rD_YMQDD3l0AobNHLaV_1-mUrDD33gsQLXJ_DVTyvpqvQLm_Jh3flSOQRPEvvEhSem_C9p5MfWmQRoCZxRztUt1eXalxM2kVQLgflw2oOqjgvR9TwMjUE8LiEgaxTpZdj-mP2FuP5Ild8PBwyZnUxlopBKyvQyW81SMbvyQjrIlbjmN4KMYfy1VF2XK5iOcUj0mZe69sL52dwKUOKvZDrEHsof8LmMRKc6LOp_IgaNCaQc4SbI2HPWKERh2ALqFXA32QUZSta2KYUHIer2OAd6_aPUqA2j4QMUN9HXSw94_-xTfX2K7id15cDULVM474isdPmAkUq1EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خبرنگار کانال ۱۲ رژیم صهیونیستی: مقام‌های مسئول در حال بررسی این موضوع هستند که آیا یکی از خلبانان، خلبان دیگر را با چاقو زده است یا خیر
🔹
قرار است یک هواپیمای دیگر از دبی به عربستان سعودی اعزام شود تا مسافران را سوار کرده و سپس پرواز خود را به مقصد اسرائیل…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/694158" target="_blank">📅 11:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694157">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
دارایی صندوق‌های سرمایه‌گذاری دو برابر شد؛ ۴۱۳۲ همت زیر دست چند بازیگر!
🔹
بازار صندوق‌های سرمایه‌گذاری در یک سال با یک جهش بزرگ روبه‌رو شده است.
🔹
دارایی تحت مدیریت این صندوق‌ها از ۱۹۸۶ همت در سال گذشته به ۴۱۳۲ همت رسیده، یعنی بیش از ۱۰۷ درصد رشد در یک سال رشد کرده است.
🔹
در بین این صندوق‌ها، سبدگردان‌ها بیش از نیمی از کل دارایی صندوق‌ها، معادل ۵۰.۱ درصد را مدیریت می‌کنند و ۶۴.۷ درصد تعداد صندوق‌ها هم در اختیار آنهاست./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/694157" target="_blank">📅 11:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694155">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
خبرنگار کانال ۱۲ رژیم صهیونیستی: مقام‌های مسئول در حال بررسی این موضوع هستند که آیا یکی از خلبانان، خلبان دیگر را با چاقو زده است یا خیر
🔹
قرار است یک هواپیمای دیگر از دبی به عربستان سعودی اعزام شود تا مسافران را سوار کرده و سپس پرواز خود را به مقصد اسرائیل…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/694155" target="_blank">📅 11:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694154">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f9e0bbeb.mp4?token=dvXMKKeLIwzgy0L589pNFY7f32xCgyj70WRpNozsXQEbgLaNjTSgIxXEFo38QezbdV-XYGX1dsgN1aDbsVrrxBxkypdrXBqZDPyU8afovsLJ_W2Ticktei5d7z2IZcAX4160KmqktcsGnioEbOHH3YtWavvzyGTQcphxvbfK78RPy-QAMQB6VXnUL_lzbE_xYIKa6YD3zMalmnWQdjwsA9BmtGzpcwGTcpRZ7S9eo_c5bBfhmKZj-rLT24cJ_WWFQ31NlL0kTqprP9wmkCMafpqAfHPwhLCZrsA8oTiJnJTlHqcSgRb_wqouMHG0olYSeF6iBjU8_YytFx8l2zla7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f9e0bbeb.mp4?token=dvXMKKeLIwzgy0L589pNFY7f32xCgyj70WRpNozsXQEbgLaNjTSgIxXEFo38QezbdV-XYGX1dsgN1aDbsVrrxBxkypdrXBqZDPyU8afovsLJ_W2Ticktei5d7z2IZcAX4160KmqktcsGnioEbOHH3YtWavvzyGTQcphxvbfK78RPy-QAMQB6VXnUL_lzbE_xYIKa6YD3zMalmnWQdjwsA9BmtGzpcwGTcpRZ7S9eo_c5bBfhmKZj-rLT24cJ_WWFQ31NlL0kTqprP9wmkCMafpqAfHPwhLCZrsA8oTiJnJTlHqcSgRb_wqouMHG0olYSeF6iBjU8_YytFx8l2zla7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استیضاح میدری، وزیر کار تصویب شد
🔹
در پی یک جلسه پرتنش چهار ساعته، نمایندگان استیضاح‌کننده احمد میدری، وزیر تعاون، کار و رفاه اجتماعی، از توضیحات وزیر قانع نشدند؛ به این ترتیب، طرح استیضاح میدری تصویب شد و برای بررسی در صحن علنی مجلس ارجاع خواهد شد.
🇮🇷
…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/694154" target="_blank">📅 11:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694153">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSlm5RdBFWvYrctG0H4ElM6-Ub6zfsdmCNhM5V-H2yVWSzgq-OUmThK3fIYkReJshvLU-ZdpGpTkgmZg_AwdRS_cMsSJMnPNn2bVxNF0fIQydjndcqdT09QLWoSnY4JKA0X1Bz_KXgBixzeGxKnTtblMJOi1PIFZnQ7QHcr3KeSFPDfYHoP6mV9_Ee7tjUXgSAbjxawbUTq1grPDS7mP30oJVqYwqUJ-_oD4SeOUUmw9kLuQSCnaiSw-JLrT_ymYKc6DlCIFA7chGR6KW6Io2zWJM3Olat_ba5lHzaBrKnSXHIl96GjpS9LRB3bY9-pKFmgES4gFpL_DDwmRMohOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروهای آمریکا در حال ترک عراق هستند
🔹
انتظار می‌رود خروج این نیروها تا فردا تکمیل شود و ۲۳ سال تجاوز و اشغالگری به پایان برسد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/694153" target="_blank">📅 11:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694152">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
بر اساس اظهارات مدیرعامل اتحادیه مرغداران گوشتی قیمت مرغ بین ۲۴۵ هزار تومان تا ۲۵۰ هزارتومان رسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/694152" target="_blank">📅 11:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694150">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سخنگوی نخست‌وزیر اسرائیل: حادثه‌ای که برای هواپیمای فلای‌دبی رخ داد، اقدام به هواپیماربایی نبوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/694150" target="_blank">📅 11:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694149">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
مقام ارشد عربستان گزارش‌ها درباره برگزاری دیدار میان مسئولان سعودی و اسرائیلی در جریان سفر نتانیاهو به امارات را تکذیب کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/694149" target="_blank">📅 11:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694148">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تهدید بن‌گویر به سوزاندن پیکر شهید سنوار و دیگر عاملان حمله ۷ اکتبر
وزیر امنیت داخلی رژیم صهیونیستی:
🔹
پس از تصدی وزارت جنگ، اطمینان حاصل خواهم کرد که «اجساد یحیی سنوار و عاملان حملات ۷ اکتبر سوزانده شوند.»
🔹
من به عنوان وزیر جنگ تغییری اساسی در مفاهیم رایج ایجاد خواهم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/694148" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694147">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=rpEjyvt1DYGyDOWic3PZ_PVGJGXf6mFG0WbGXqYmncfYwzIENlnE7oaogTZ35HbP6qh_H0Cum-3zY-YxY8IZQBaIFBpZAR0nZTakd2qKru2OSSUiLE3a7bzUbkiv2BdeZUoIdpE1tXwaKTYjrmTML8g2dguN_-Km299SRQJTaLG_IXSBEk2rxiqMyLrhUCDi2256BAUjzihI_A388Xnoo-sEpI6Y_WHoulm24T4qeMp1rX1OgPGZbSSdwMKujJsgtISSj_1rTBPe4DmIoUSTCE2zzI565hauw1n2Zs8Hnd0Z8tUf4tO-hq_Ihw_RK9cFKlohxrVy6HFy5A4G01ebWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=rpEjyvt1DYGyDOWic3PZ_PVGJGXf6mFG0WbGXqYmncfYwzIENlnE7oaogTZ35HbP6qh_H0Cum-3zY-YxY8IZQBaIFBpZAR0nZTakd2qKru2OSSUiLE3a7bzUbkiv2BdeZUoIdpE1tXwaKTYjrmTML8g2dguN_-Km299SRQJTaLG_IXSBEk2rxiqMyLrhUCDi2256BAUjzihI_A388Xnoo-sEpI6Y_WHoulm24T4qeMp1rX1OgPGZbSSdwMKujJsgtISSj_1rTBPe4DmIoUSTCE2zzI565hauw1n2Zs8Hnd0Z8tUf4tO-hq_Ihw_RK9cFKlohxrVy6HFy5A4G01ebWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درمان ریزش مو در کوتاهترین زمان
کشف شرکت دانش بنیان ایرانی در آنتن زنده شبکه ســـه ســیــمــا!!
😳
😳
ویدیو داخل لینک را حتما مشاهده کنید تا با تاثیرات عجیب این روش درمانی آشنا شوید
👨‍⚕
👨🏻
✨
🩺
بـیـش از ۳۰هـــزار خـانم و آقـا از این روش معجزه‌_آسا نتیجـه گرفتن
😍
روی لینک زیر کلیک کنید
😃
👇
https://www.20landing.com/214/2604
https://www.20landing.com/214/2604</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/694147" target="_blank">📅 11:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8i7KzPZonSJfGxFtY40OoE_Bs0bJi2gjbax8xNXdtp-TCPMA3fyp3t58bZtaLBCrNA4Ksq2BliVINYrXXl5F_BLsgab2VvWdxD-VulbeWmsreViutng2epLeDEJMxjiuaJtH45tLsS9okYhtFpVX4zghPRWCcGgEsrX0p00FK6fihotBHxk6RPDbOyG9OeVMFIbge6UmXBjW0a6vqZ1bxx5RFLLWlsbeKuaX0TT4EAyc2gpTlEhzWJIT5lkzwWJ3UWGiRFpLrHrEr25TQAdmgEB573aL_fPXZiF1R52TZFDKMCIN6ceXV-TW8ZUvx-OALG1jLvXKl-eFCwaggbrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
منابع سازمان کجا هدر می‌روند؟
💡
کدام فرایندها نیاز به اصلاح دارند؟
در این دوره با روش‌های ارزیابی
کارایی، اثربخشی و مصرف منابع
آشنا شوید
👤
با تدریس
دکتر نظام‌الدین رحیمیان
🎯
ویژه مدیران و حسابرسان
🎁
ثبت‌نام رایگان
👇
🔗
https://b2n.ir/afder
#مدیریت
#حسابرسی
#کارایی
#اثربخشی</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/694146" target="_blank">📅 11:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694145">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDIOlxnTlJUhc8FKkmHscoj01a-R4ZbVvmQF6dzcVlAUN6AX32-lipvaVh3CTZVomOD19MpkgKwzbPPbC3fpiG9PgXA1adx7a4BAz4VmFbRbFA9ExlT3O0PU5bEg9QG2DMv9vX93gSmzTD5SY45CA99HCh4hwluTKVr-QbUBAC8GO9IPUoOfWSoWJCYPbJ2DeNzxwsRpKe9pIXdcyH2n8qJSGHyvc9b6FdRtN90CXg8aqh2PnVvfgONUXc6gFN_p042iXh4XDS2kCYCnwyLcTeQPtfGqMXfVm0ZQbW_OHCt7GYneC4k1WH-S0PNKLbjFPmA7EsDLj7OvfDJTkmjhOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کتاب‌های کمک درسی ۷۰۰ درصد گران شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/694145" target="_blank">📅 10:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694144">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKwVXOWPBsHolBvNHoDkNxXNPpLcjSzAtamDyD6vHi-Bci_5vVRcjEUm1M1gs7MQ5UuqeW1NmAJFGfebyJMErp0dnUYqlZvrGsX9gUs6b9f0zcCqemhUWqaC2BGVeulPKnxJ_uIgdwsHRNqeG0aUqjEYTqRhIUk3JLX7G74f87tSYqCgvahF4y5RMUNZgZIUDlzRNTmIs9SMUhR7PmdPFwsezFfNIYWyCITpCrqphGkndo7R8y7n2q7dKkqNsktAfY7ExP0UQiJbjV9HA-Lbcdun7OA_KUbU92dL7KnatjKzHf-nIFj2m4zbX81I5xXPPbyyMKN3HBQf8fIo2inrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرم صورتت رو بشناس و با انتخاب درست عینک، تناسب چهره و استایلت رو چند برابر کن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/694144" target="_blank">📅 10:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694143">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
رسانه‌های اسرائیل ادعا می‌کنند که دلیل درخواست کمک از سوی هواپیما، وقوع درگیری و نزاع میان مسافران در داخل آن بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/694143" target="_blank">📅 10:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694142">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
رسانه‌های اسرائیل ادعا می‌کنند که دلیل درخواست کمک از سوی هواپیما، وقوع درگیری و نزاع میان مسافران در داخل آن بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/694142" target="_blank">📅 10:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694140">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRHuuLdk0NE9HF7AjYHEp3tG8Wmb5ekzGVvT18EW3zXKRYrlW4gXkZD3MjVcBqvMACbbiZ1IA0mWGzPS1ltfwVxxlZpFJeIODiYAy-aoGsetAiHUToIg0ByrDC7ZW-hanswBgjnwnY0gzqGA67C-JCZGiy_EgZXIewCSa-UABJpb55HBNuU2OGOJOtEIxsifrUJcarul1_5BZZqAsRvu3nWYVGbmO3uJS5VGoM1p_momono-uX21bAOTKUO1LypNODASjeR63qVZ8CX6iLqwhKbE4XCo3to3bWebCFRJOm7QV8ZCocnqdNx1XB1eSPv4ywam0J1nylrprM_XUh3FmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فریبرز عرب‌نیا به ایران برمی‌گردد؛ گلشیفته هم شاید بیاید/ این دو بازیگر علیه حمله به ایران موضع‌گیری کردند
🔹
برخی منابع از جدی شدن بحث بازگشت فریبرز عرب‌نیا به ایران خبر داده‌اند. همچنین درباره گلشیفته فراهانی نیز احتمال سفر به ایران، نه اقامت، مطرح شده است.
🔹
این گزارش‌ها می‌گویند مواضع این دو چهره درباره جنگ و مخالفت با حمله به ایران، از عوامل مطرح‌ شده در این گمانه‌زنی‌هاست./ تابناک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/694140" target="_blank">📅 10:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694139">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: به نظر می‌رسد این حادثه مربوط به هواپیماربایی نیست
🔹
هواپیما با مقام‌های سعودی تماس برقرار کرده و در عربستان فرود آمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/694139" target="_blank">📅 10:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694138">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال ۱۲ اسرائیل: برآوردهای نهادهای امنیتی اسرائیل حاکی از آن است که هواپیمای «فلای‌دبی» در عربستان سعودی فرود خواهد آمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/694138" target="_blank">📅 10:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694137">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل در مورد هواپیمای بوئینگ ۷۳۷ فلای دبی: خلبان کد مربوط به ربوده شدن هواپیما را ارسال کرده است؛ حدود ۱۵۰ اسرائیلی‌ در این پرواز حضور دارند
🔹
این هواپیما دیگر در اپلیکیشن رهگیری پرواز Flightradar نیز نمایش داده نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/694137" target="_blank">📅 10:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694136">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
گروگانگیری ساختگی زن ۲۵ ساله برای گرفتن ۷۲ هزار یورو از همسرش
🔹
همسر این زن ۲۵ ساله پس از ناپدید شدن او، پیام‌هایی مبنی بر گروگان‌گیری و درخواست ۷۲ هزار یورو دریافت کرد. بعدتر نیز به او اعلام شد که همسرش به قتل رسیده است.
🔹
اما حدود یک ماه بعد، روشن شدن تلفن همراه زن در یک شهر مرزی، پلیس را به محل اختفای او رساند. مارال در خانه‌ای در حالی پیدا شد که زنده و سالم بود.
🔹
او اعتراف کرد برای تأمین هزینه مهاجرت به لندن و با مخالفت همسرش، این سناریو را طراحی کرده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/694136" target="_blank">📅 10:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694135">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c0cdd75e.mp4?token=gVG7fNs-FNO3c4iB7dEE8Ih2kZUDkLUca0_uimO3mnYbHnT8X7CFLpQ2GfgunNVtXtY381PtgAzIWHVZ4c-Z5TKdS6SphrLb4DTK_8LUfVgS7ahrt0FGGc2Y1iOjWJUHpvoe79chCmKttmrr7KiaJKJMpH9soYztdI2lCCeMFDtMcFYOX49w1p9bbShpG98F-sOuaXr5N9NvNvs5zEaL6MrkW8i8hrO_OPoxZBuJ4Glu3qUAdkvRItJ_li2hkVmBOGVfPUnwDChFXDZmvNho5Fs2EaXD2dUuwlhl9AUIwaSUF9LwpyJ2WONRWrVjlhBEFd3-4DfwxPnfMuDkB-E0ya8UpEVbUdPwtExx17NqK35hKh_2WJLLaWLJw7oOucbjfDgViBK0DlMWXs9kReu2t2SkuWgviPsTcQEOKuzsr9_naRUlUd_ec0DFWeFTauO6skESSb0iOU_K65F6AWWf0WNNnck3dPKPZ7UoYEMPPwWo9XS6MH9hVdnMr9NUygvpVdekHwvQWwVUaER8kDpszknzKzYEjXUvmVqnGP9ISP3ipuvk3LUN5BKeGiKQ-ktPzf9ID_IChtoE0Xf0UWG0HyIomzbnAQrLgIRB4DBcda4er3O-JV_BAOUT1WYYvfKsl_1jNm2OEGJL8ID7Xw1fMUa6icVxG3S3mbsypUO8oW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c0cdd75e.mp4?token=gVG7fNs-FNO3c4iB7dEE8Ih2kZUDkLUca0_uimO3mnYbHnT8X7CFLpQ2GfgunNVtXtY381PtgAzIWHVZ4c-Z5TKdS6SphrLb4DTK_8LUfVgS7ahrt0FGGc2Y1iOjWJUHpvoe79chCmKttmrr7KiaJKJMpH9soYztdI2lCCeMFDtMcFYOX49w1p9bbShpG98F-sOuaXr5N9NvNvs5zEaL6MrkW8i8hrO_OPoxZBuJ4Glu3qUAdkvRItJ_li2hkVmBOGVfPUnwDChFXDZmvNho5Fs2EaXD2dUuwlhl9AUIwaSUF9LwpyJ2WONRWrVjlhBEFd3-4DfwxPnfMuDkB-E0ya8UpEVbUdPwtExx17NqK35hKh_2WJLLaWLJw7oOucbjfDgViBK0DlMWXs9kReu2t2SkuWgviPsTcQEOKuzsr9_naRUlUd_ec0DFWeFTauO6skESSb0iOU_K65F6AWWf0WNNnck3dPKPZ7UoYEMPPwWo9XS6MH9hVdnMr9NUygvpVdekHwvQWwVUaER8kDpszknzKzYEjXUvmVqnGP9ISP3ipuvk3LUN5BKeGiKQ-ktPzf9ID_IChtoE0Xf0UWG0HyIomzbnAQrLgIRB4DBcda4er3O-JV_BAOUT1WYYvfKsl_1jNm2OEGJL8ID7Xw1fMUa6icVxG3S3mbsypUO8oW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسون‌ترین دستور مرغ مشهدی؛ یک بار درست کنی، جایگزین همه مدل‌های مرغ میشه
😋
مواد لازم:
🔹
ران مرغ به دلخواه بی‌پوست یا با پوست (مرغ‌ها ۳ ساعت داخل اب و نمک و یک قاشق سرکه بمونه)
🔹
پیاز
🔹
زعفران
🔹
سیر ترشی
🔹
کره
🔹
نصف لیوان آب جوش
🔹
یک لیوان روغن
🔹
ادویه نمک وفلفل…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/694135" target="_blank">📅 10:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694134">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است.
🔹
مقام‌های…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/694134" target="_blank">📅 10:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694133">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ofu5PDAko7o54lL6baNH81Vo-NcQraJwo24_1PVFx1J18MrlGTZOsCmc8DHk6Ou7JuB7oMRM5kgXUMWPANjfoujusHBC1mNAnVRSfkPnDbFICigO_t3SdyiS85Bk3ERNeU_sZWKRS8BDcE6MuSlOKoCDJ3KmH6kM0U2d1tzmPXY2yAVjG7pSb4KYbzDJvz8j2auC1vWPiiDMMrZsayrf4YOVgfydL-DxyInQTfTclO8HLcOpxx12_b8axI9t0qfQnZL7V1qMvFzvFxr-pv7OHvUecLdRP4HoPSr9FahAChRldwUvhtn46alm6qX12F1NGYFYiieIll4vtPTLz7FotA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است.
🔹
مقام‌های اسرائیلی ارتباط خود را با یک فروند بوئینگ ۷۳۷ فلای‌دبی از دست داده‌اند و اسرائیل در حال بررسی احتمال هواپیماربایی این هواپیماست.
🔹
جنگنده‌های نیروی هوایی اسرائیل برای رهگیری این هواپیما به پرواز درآمده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/694133" target="_blank">📅 10:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694132">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2Th23FWXhiD4yCkJjhxzZntk2ZUnYZub5fPvru_cpthxdOd-GyXRorb_sMrud9X6qVpiDjhQNyJQZ66uih1dnrCbLzRfFO3J-nqzqLBWKa1U8yUsMN9c-S4aDpXXZR0b_HdZjVR-sNhxl4YCOI3I5erCbRZkWrK3_UmpBIp8h8p9oSYIlfjvr3Ybw0MAxxakivsZbahixb5J4rfQApXkRE8dOT3BnRKyexUHyMGwIEvz98yFNKwkMvkJerV5qQAkW395YE-2GJ0XcOK-6nbTWNsT3hJ1hm3bGaSWPvKxqTbJB7TAYxjY6Z8LEJ4JlGIXNNaPBNRSHHCai8E7UpYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
اگر بازار خودرو برات مهمه، یک قدم جلوتر باش!
هر روز
مهم‌ترین اخبار خودرو، قیمت‌های بازار، تغییرات قیمت کارخانه، شرایط فروش و ثبت‌نام‌ها
را سریع و دقیق دنبال کن.
📊
تحلیل بازار | قیمت خودرو | اخبار فوری | مقایسه خودروها
🔎
قبل از خرید یا فروش خودرو، اطلاعاتت را به‌روز کن.
🔥
CarPress؛ رسانه خودرویی ایران
همیشه یک قدم جلوتر…
👇
همین حالا به کانال ما بپیوند:
T.me/carpresss</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/694132" target="_blank">📅 10:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694131">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رأی قطعی دادگاه تجدید نظر دیوان عدالت اداری؛ نبراس برگزارکننده هشتمین نمایشگاه توانمندی‌های صادراتی ایران شد
با رأی قطعی دیوان عدالت اداری، برگزاری هشتمین نمایشگاه توانمندی‌های صادراتی جمهوری اسلامی ایران توسط شرکت نبراس قطعی شد.
با صدور رأی قطعی دیوان عدالت اداری در پرونده مربوط به برگزاری هشتمین نمایشگاه توانمندی‌های صادراتی جمهوری اسلامی ایران، اختلاف ایجادشده بر سر برگزارکننده این رویداد تعیین تکلیف شد. در پی شکایت شرکت «نمایشگاهی رویداد» از سازمان توسعه تجارت ایران درباره نحوه تعیین برگزارکننده هشتمین نمایشگاه توانمندی‌های صادراتی جمهوری اسلامی ایران، موضوع در مراجع قضایی مورد رسیدگی قرار گرفت و در نهایت، در مرحله تجدیدنظر دیوان عدالت اداری، رأی قطعی به نفع سازمان توسعه تجارت ایران صادر شد. بر اساس رأی قطعی صادرشده، شرکت مدیریت نمایشگاه‌های بین المللی نبراس به عنوان برگزارکننده هشتمین نمایشگاه توانمندی‌های صادراتی جمهوری اسلامی ایران تعیین شده و این رویداد مطابق برنامه‌ریزی انجام‌شده برگزار خواهد شد.
هشتمین نمایشگاه توانمندی‌های صادراتی جمهوری اسلامی ایران قرار است از ۶ تا ۱۰ آذرماه ۱۴۰۵ در محل دائمی نمایشگاه‌های بین‌المللی تهران برگزار شود.
https://www.khabarfoori.com/fa/tiny/news-3248888
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/694131" target="_blank">📅 10:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694129">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
واردات خودروهای لوکس با دستور رئیس‌جمهور متوقف شد
🔹
وزیر صمت، اعلام کرده است که بر اساس دستور رئیس‌جمهور، واردات خودروهای لوکس حتی برای ایرانیان مقیم خارج از کشور نیز منتفی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/694129" target="_blank">📅 09:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694128">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
مشاور فرمانده نیروی هوافضای سپاه: هر چقدر لازم باشد موشک می‌زنیم تا دشمن ادب شود؛ نرخ شلیک موشک‌های ایران به‌گونه‌ای است که حتی در صورت تداوم رویارویی برای چندین سال، امکان ادامۀ عملیات با همین نرخ وجود دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/694128" target="_blank">📅 09:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694127">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/694127" target="_blank">📅 09:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694126">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253eb5d79e.mp4?token=QGt3MY8gbKuRTnslhx7oFrmQyebS3NKnKhzWrRz67PqynQzGZfXbP_nG1a6diGfAEAqe1Mgxbwcyb0i35rLVwuR_xH6_-qYgfIDkR3MnXbbqcZb1zTMDCoVZaycAX0wtR9XBJIlV1DGlLPlAdQaLJqtNvqCK8Y_6zM0xUi9FQT7eR76V7i-yWITE6H2QJMiAde7w3ISNCH1eK2WXPMMSQbFW0MZTI9oDiZa990sVm1ysD_g71PWZZWfMnW-_u7VUSKP70pHIVF9brqk_6fye8H_wt-Zsq9I8DpoOpd0MAw1dXtU8k99SJ7IHYm7L_tEzx-ByM0hVUx4e07vC23ImVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253eb5d79e.mp4?token=QGt3MY8gbKuRTnslhx7oFrmQyebS3NKnKhzWrRz67PqynQzGZfXbP_nG1a6diGfAEAqe1Mgxbwcyb0i35rLVwuR_xH6_-qYgfIDkR3MnXbbqcZb1zTMDCoVZaycAX0wtR9XBJIlV1DGlLPlAdQaLJqtNvqCK8Y_6zM0xUi9FQT7eR76V7i-yWITE6H2QJMiAde7w3ISNCH1eK2WXPMMSQbFW0MZTI9oDiZa990sVm1ysD_g71PWZZWfMnW-_u7VUSKP70pHIVF9brqk_6fye8H_wt-Zsq9I8DpoOpd0MAw1dXtU8k99SJ7IHYm7L_tEzx-ByM0hVUx4e07vC23ImVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی آقامحمدی؛ عضو مجمع تشخیص مصلحت نظام:‌ گروه‌های مسلح آموزش‌ دیده در امارات و اسرائیل وارد کشور شده‌اند، مردم در محلات مراقب باشند و گزارش دهند
🔹
جریاناتی در محلات استقرار پیدا کرده‌اند تا عملیات‌های ترور انجام دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/694126" target="_blank">📅 09:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694125">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای رویترز: عباس عراقچی پاسخ آمریکا به پیشنهاد «طرح هفت‌ روزه» را دریافت کرده است
🔹
عراقچی امروز در تهران درباره پاسخ آمریکا به این پیشنهاد گفتگو خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/694125" target="_blank">📅 09:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694124">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای رویترز: عباس عراقچی پاسخ آمریکا به پیشنهاد «طرح هفت‌ روزه» را دریافت کرده است
🔹
عراقچی امروز در تهران درباره پاسخ آمریکا به این پیشنهاد گفتگو خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/694124" target="_blank">📅 09:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سخنگوی سازمان ثبت اسناد و املاک کشور: مشاوران املاک برای تنظیم قولنامه عادی سند سبز، جریمه و تعلیق پروانه کسب می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/694122" target="_blank">📅 09:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0bf99c1d3.mp4?token=tzvMYWTjZqM16-Dld1qaq7toXGTviwvfDJqhEhajBKfoZKlCdYMn8CT2mn3qR1MwRsf-vAbv8RFYtiQsFUSdDcOpfl7TSCCEBd0F1UQk4hgLjQLX5NFC3DFXP6HzhD8D5qbLkeMNt5EjXZWpyocs66ZYdPSdlOAiWoKkKIRiH27EET_Or58nu_s-zLOdD8Nm4f5Lo0anVo8jPz3wt_kIhVRoRDfVLpxz0--ci9DyxOIo69qRfBnmsDZSN-7lz4TeypmhXUaoIeRrYNlYB6eG5McLPCqRNVSYbbycW-nqtu8HwqTB8BG5eIqVgogHQulGJ-FsbYIK8ZVolnzhzgQB4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0bf99c1d3.mp4?token=tzvMYWTjZqM16-Dld1qaq7toXGTviwvfDJqhEhajBKfoZKlCdYMn8CT2mn3qR1MwRsf-vAbv8RFYtiQsFUSdDcOpfl7TSCCEBd0F1UQk4hgLjQLX5NFC3DFXP6HzhD8D5qbLkeMNt5EjXZWpyocs66ZYdPSdlOAiWoKkKIRiH27EET_Or58nu_s-zLOdD8Nm4f5Lo0anVo8jPz3wt_kIhVRoRDfVLpxz0--ci9DyxOIo69qRfBnmsDZSN-7lz4TeypmhXUaoIeRrYNlYB6eG5McLPCqRNVSYbbycW-nqtu8HwqTB8BG5eIqVgogHQulGJ-FsbYIK8ZVolnzhzgQB4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی همتی و مجید نیک‌اندیش، از عوامل حوادث دی‌ماه ۱۴۰۴ در طبرسی مشهد که به شهادت ۴ نیروی حافظ امنیت منجر شد، پس از طی روال قانونی بامداد امروز اعدام شدند  #اخبار_مشهد در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/694121" target="_blank">📅 09:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694118">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه دهم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/694118" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه دهم؛ موج هستی
🔹
نظام هستی نتیجه یک تپش مدام و حرکت موجی است که از سوی خداوند در نام مبارک
«الْمُبْدِئ»
آغاز می‌شود و دوباره در نام مبارک
«الْمُعِيد
» به سوی او بازمی‌گردد.
🔹
برای قرار گرفتن در «موج خیر الهی»، انسان باید از محاسبات عددی و عقل جزئی فاصله بگیرد و به مقام «نادانستگی» و «توکل» برسد.
🔹
نام «الْمُعِيد» می‌تواند نقاط طلایی و فرصت‌های از دست رفته را دوباره برای انسان خلق کرده و به او بازگرداند.
🔹
«رحمت خاصه‌» خداوند در زمان‌ها و مکان‌های ویژه‌ای پنهان است که می‌تواند مسیر زندگی انسان را دگرگون کند.
🔹
هم‌سو شدن با تپش هستی و انجام کارهای نیک به‌صورت صادقانه و بی‌ریا، راه ورود به رحمت خاصه‌ی پروردگار را هموار می‌کند.
🔹
نورِ «الْمُبْدِئ» و «الْمُعِيد»، فرصتی دوباره به انسان‌ها و سرزمین‌ها می‌بخشد و  تپشی از خلقت و نیکویی را به سوی آن‌ها می‌فرستد.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/694118" target="_blank">📅 09:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694117">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/093c29c3c9.mp4?token=T8hExJWJGLWRH5HwRv1gTOsZUPGw3Q6hRlAY-r2g3fsY_Qzbc2h469yVzAMpTsGgwX1zKnqLIBN4vPC0PUux0oe30CArtGJq-GEqwungJRENKhta1iZlz6avjMGvj71J8n2goGpX7IGOh0ZdSIIwj_Fp2aqBZr3YCo2tgL1Qp4aiPz9nHh-5UoknaQm5ygVz1yc8wv41G5iL9WV2zh0NTo_Y_5Pc8sryF0RVtLn2HtKJAl7Jev6i6FAeUqomRrbbzFkB3JGelvKrGq044W-c1uI7eNgQL3nD5pfanRLXBz0mdv0PwqOiSo59w6erTjL2AaKMUXgRU3dzkRxLD6YTOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/093c29c3c9.mp4?token=T8hExJWJGLWRH5HwRv1gTOsZUPGw3Q6hRlAY-r2g3fsY_Qzbc2h469yVzAMpTsGgwX1zKnqLIBN4vPC0PUux0oe30CArtGJq-GEqwungJRENKhta1iZlz6avjMGvj71J8n2goGpX7IGOh0ZdSIIwj_Fp2aqBZr3YCo2tgL1Qp4aiPz9nHh-5UoknaQm5ygVz1yc8wv41G5iL9WV2zh0NTo_Y_5Pc8sryF0RVtLn2HtKJAl7Jev6i6FAeUqomRrbbzFkB3JGelvKrGq044W-c1uI7eNgQL3nD5pfanRLXBz0mdv0PwqOiSo59w6erTjL2AaKMUXgRU3dzkRxLD6YTOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار بیل گیتس درباره کشتار جمعی توسط هوش مصنوعی!!
🔹
هوش مصنوعی از آستانه‌ای عبور کرده که توانایی آن برای توانمندسازی یک بیوتروریست به منظور کشتن صدها میلیون نفر، امروز وجود دارد.
🔹
توانایی انجام یک حمله سایبری که تمام حساب‌های بانکی را به هم بریزد و شبکه برق را از کار بیندازد؛  این خطر امروز وجود دارد. و ما می‌دانیم که اینطور است.
🔹
دلیل وجود این وضعیت آن است که فردی با نیت بد می‌تواند هوش مصنوعی را بگیرد و باعث شود آن کارها را انجام دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/694117" target="_blank">📅 09:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
با اعلام سخنگوی قوه قضاییه، سرمداران رژیم آمریکا، در پرونده ترور شهید سلیمانی، به ۴۸ میلیارد دلار جزای نقدی محکوم شدند. همچنین ۷۲ فرد مرتبط با ترور شهید سلیمانی تحت تعقیب کیفری این قوه قرار دارند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/694116" target="_blank">📅 08:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694115">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIb_yrDInkeCeclIiC0qJ3thFR7W7HyZVi2lthTvckJvYP_8NNYhkIYu08fKS-975F5d1VPbeJ9BK2_1DLO_y2rRdS7yTAN1XCL0IpzOkYwqgLtObXPb447ahNvxNJBDje1EN4Yf1y1_6YYrojsipk4QPA3k9FI7ir7K7-fOiGD6Ucj5-OzGd7bC67x0yZ6n7dHcNeHXAl6W0DhGzQQW8X6-7l_y-BHU5Y2TwIrLuhcDyGguAXsDEwxq4ZpIbLebaE8TuzGo3eanWBJiOFhHqFM14pARLeOWROjn7bDZXUVKAOWKFZx_EkUB5XrbVElTYmHCDX1e90tEGU5ROb7aAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت تتر به ۲۵۸ هزار تومان
رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/694115" target="_blank">📅 08:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694113">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq7B7yh7T0xPAsYf9d9TuWaMkAUPfXKChLkK7WlUk5c1WprDPtDMAtG52PDWPf0g9PG3sN5JHHk4X7IFGK-ochFGNSiZHvcygtMOPoEEnZ9Qq0HwFx4CRW4fK9F8X7asW_cjxMAoRm9M0QvlArg_Alc_g1QcKJ_0GWH11GboeSajFMsQJ2PkHiaplj_rspjR8o95axqhUZX3P05pPr9ousl0DID_cydg2kwyLUePT17HbFp-Npj5xtXmMMD80LLvm54p2aaiBfZCNfympwCM1zldxxAKrJ_L6A_ofZar-YCh9YYrIknIZRio1lDCjhOA_V85Qt1q9nyiCKVApqJdBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۶ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/694113" target="_blank">📅 08:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694112">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: هر توانمندی نظامی که در اختیار پاکستان باشد، بر اساس پیمان دفاع مشترک جدید، در اختیار عربستان نیز قرار خواهد گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/694112" target="_blank">📅 08:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694111">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c541752184.mp4?token=NM9Y4vozp8Uta4VyQkHymci_RKsxKUNyZpXUXKVEIBUMfRKUfXvMg45fmnNU43NazQ7lM_riw0rpRdqP_PLEVHzd5pqm8-flhpAyOyo_PHMyH50weRkrgcUhgCNx78pqayi2dDrvSPxj-6t4g0raoL9WxPO_arcDQCbrSF-VmXXBzXQ8tvj6zO1LZn4-BKORfiPoydBH-Gn4XyHRAD6WKS9PFBnOVIYI4ESGStOqmUD_f6HI0jZauCBk4GekAT3jIBteOL0upq5XajfNc9bkJ10qWSZ4CqAGtF71qOCZjKuaIbNkUHCf4hWvmonpuiYRQN1sg3lbNFgcV9D8E9Wdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c541752184.mp4?token=NM9Y4vozp8Uta4VyQkHymci_RKsxKUNyZpXUXKVEIBUMfRKUfXvMg45fmnNU43NazQ7lM_riw0rpRdqP_PLEVHzd5pqm8-flhpAyOyo_PHMyH50weRkrgcUhgCNx78pqayi2dDrvSPxj-6t4g0raoL9WxPO_arcDQCbrSF-VmXXBzXQ8tvj6zO1LZn4-BKORfiPoydBH-Gn4XyHRAD6WKS9PFBnOVIYI4ESGStOqmUD_f6HI0jZauCBk4GekAT3jIBteOL0upq5XajfNc9bkJ10qWSZ4CqAGtF71qOCZjKuaIbNkUHCf4hWvmonpuiYRQN1sg3lbNFgcV9D8E9Wdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزانه با انجام دادن این تکنیک حافظه‌ات رو تقویت کن
🧠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/694111" target="_blank">📅 08:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694110">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
فرماندار ایالت کالیفرنیا با امضای قانونی، اعیاد فطر و قربان را به تقویم رسمی کالیفرنیا اضافه کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/694110" target="_blank">📅 08:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694109">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
شبکه ۱۴ صهیونیستی: نمایندگان عربستان سعودی و سایر کشورهای عربی در سفر نتانیاهو به امارات حضور داشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/694109" target="_blank">📅 08:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694108">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
هواشناسی: هشدار نارنجی شدت فعالیت سامانه بارشی امروز برای اردبیل، گیلان، مازندران و گلستان صادر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/694108" target="_blank">📅 08:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694106">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
علی همتی و مجید نیک‌اندیش، از عوامل حوادث دی‌ماه ۱۴۰۴ در طبرسی مشهد که به شهادت ۴ نیروی حافظ امنیت منجر شد، پس از طی روال قانونی بامداد امروز اعدام شدند
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/694106" target="_blank">📅 08:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694105">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
نیروهای آمریکا در حال ترک عراق هستند
🔹
انتظار می‌رود خروج این نیروها تا فردا تکمیل شود و ۲۳ سال تجاوز و اشغالگری به پایان برسد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/694105" target="_blank">📅 08:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694104">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای آکسیوس: میانجی‌گری قطر بین آمریکا و ایران بی‌حاصل بود
🔹
مقام‌های آمریکایی می‌گویند که با وجود میانجی‌گری‌های دوحه بین واشنگتن و تهران، مذاکرات به دلیل کوتاه نیامدن دو طرف از مواضع خود، به بن‌بست رسیده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/694104" target="_blank">📅 08:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694103">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThIlhXO3oapr_sDmtrPu5Wk1Uqggo0llwp_kRRB2ShdrIrXaG9HsRKuN2PW-ocYT3HlbKmv1hMUvrPK-PQcv2pJogLKdif2NAvPjbsqICFQk97uZ1fq4aTz0D4GIbGQO-0Zyb7ecT_9JygxhR3Je8NatjUA7N5XxfSO63ppaBeQck87l113v9Gm6VuTUWnZYxA3e0pUMcX4RRJdiNG8OrnsQKWBpaFH6CAlsgggq-rZIjnyVmq7QoBGSKHm-qvVbpURQVloTDC0FR23IgKnczs2DoaymtgwCDNVXQfhO-3xC41RdrQakLoNrUMbiFQElZXqkmAyVWIUU3oQKkBClmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۸ مهر ماه
۱۸ ربیع‌الثانی ۱۴۴۸
۳۰ سپتامبر ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/694103" target="_blank">📅 08:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694102">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKFyKo8SHnxyqIEkNY5YOUcDT3Ovh_ix4xEh8Ghzf00d1HEdMa4XYkMZriR6THZRf5DvieXNoKS1k7_9stqze7vL0s8WRWBk3nUUkCaImiwS8blFHK3FTgOpMvpuZqUSy24qX9XyK2sAlzCisZn_dfy0tKOrNOiyB7rcWr-4xudQMFHAJ7I44WsPgiahP7M6R_HvuafdfQWHOMtLoe0yFVGXhXFe3hyT7jTtNRDaEPu8EYPr9EcADUBIhLKSqbNSt-GRpROZi2rWT7EZc3R4IhBHJmHb4SAudTRl_EcwULjSt1UyHuYXnYN_8o_-W62FqH7UsOiYZ1V4sUWMlVTTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
فشارسنج دیجیتالی خانگی + هدیه ماساژور پروانه‌ای
با فشارسنج دیجیتالی، فشار خونت رو به‌راحتی در منزل اندازه بگیر و برای مراقبت از خودت و عزیزانت خیالت راحت‌تر باشه.
🎁
هدیه ویژه: ماساژور پروانه‌ای
💰
قیمت نقدی:
۱,۵۹۸,۰۰۰ تومان
🚚
یا
پرداخت کامل درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
خرید
👇
https://memarket24.ir/product/fast/64800/180124/</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/694102" target="_blank">📅 00:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694101">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
نتانیاهو و لاپید امشب دیدار امنیتی خواهند داشت
🔹
کانال ۱۲ اسرائیل گزارش داد بنیامین نتانیاهو امشب با یائیر لاپید، رهبر مخالفان، دیدار امنیتی خواهد داشت.
🔹
لاپید پس از اظهارات اخیر نتانیاهو درباره احتمال وقوع یک حمله پیش از انتخابات اسرائیل، خواستار دریافت این گزارش امنیتی شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/694101" target="_blank">📅 00:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694100">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAHIJIvtpwsiNUB1gc5oYfpdeYAl7sL17KgXvshDNiP1hbSq8v9GINC5KsgyzLB_1ZF-cDEEcN-NBMKIbv3eNpvKUyO3QP6AZwGZPRCNbNrjoYbdNhse6sgg4kfw2WSs_OfzUY6rIcm6U3daA9QE9YnXn5vDNDq8r4ZL4sPEnk4lt_WT9aAS-x-jVKWiLc91qD4b6fvPAj8DHoHF6rTU7oLzu9zQiOBi2DvIRllkMHFcRCgsRB4J7OBXZj32ZoSEaB3SvAHCS4T1evDQJk4RVSgjF2nUJD-quKQwfi6t9x1hUOPPHxYVb89iwNXDz9_kpMxmEmTHSvL7xMJEMsFNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهروند آمریکایی: من از قیمت بنزین و مواد غذایی عصبانی‌ام
🔹
خبرنگار:«از اینکه به ترامپ رأی دادی پشیمانی؟»
🔹
شهروند آمریکایی :«آره. خیلی‌ها پشیمان‌اند.»
🔹
خبرنگار:«پس آمریکا دوباره بزرگ نشده؟»
🔹
شهروند آمریکایی :«نه. کشور را به خاک سیاه نشانده‌اند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/694100" target="_blank">📅 00:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694099">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0XlQh3rny0V7QEZUozf9B4nrl5CINs-MecSiJ409DxaZ-Np3AniF5ws0pJsB5IMaTYm55QtJd9TrIkFi63pA3NZlTp0gGrPGvUuS7ChSgDZa6W8g9zlWuKjAWpqB1ujN8e9D-NDT_xMwsqqkhKpsjyVAWX18HqM5hJR6dSR7VTgVhEpLMWt_3uk2sFWQxyplAM4ETwO3wRi_a-MBfYC70Lj8E0d-QHqEgWuX8PeqLong3aGz6IjMRGyGlIoCiNN8uoD4MyOcN7SAfJ-ynSHuXQrWwqIY5ae7kujrpMsxinI_KbYHynvYlXFREPJnUx2xekRMkrz3mjox5YgJptCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افتخار نتانیاهو جنایتکار به جاسوسی با موبایل  ‌
🔹
‏نتانیاهو با افتخار می‌گوید که رژیم صهیونیستی چگونه می‌تواند هر کسی را با هک کردن تلفن‌های همراهشان، به عنوان دشمن جلوه دهد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/694099" target="_blank">📅 00:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694098">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJF03HNTCGfgVqbhvhWOlzrNV2GqVrbqlLND2HDX-JCVtiUnCjyjLM0-QJEeb3jCM-RVBQ3mXqjtfdvdTsWLqgDEI8jji_QJ7bHodYlbutTKdR5OQzq6pQR6KOi1AEfCpAawNWaFGXK4VYYQf4AZa1x7SU_8nGIq1Nex2Vo988URlZbtv0Ri2hfkh_JhC6XaPUYEsCUlvCzf4yrd1apAR3822pZum_bO5DIdFTpWKxDB1G6VS-gy6DxcIpbOPmfLY4xzkmqynStEF-NidYRMOv0yZJNlLOK8SJ8oOTOvB-2rEcEB2-vKWq1oyz2casgQ2j2dMdoBc-LLxcEg2gxWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/694098" target="_blank">📅 00:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694097">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
نیروهای آمریکا در حال ترک عراق هستند
🔹
انتظار می‌رود خروج این نیروها تا فردا تکمیل شود و ۲۳ سال تجاوز و اشغالگری به پایان برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/694097" target="_blank">📅 23:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694096">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">Live stream finished (12 hours)</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/694096" target="_blank">📅 23:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694095">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1a648eba.mp4?token=AFKlzmJiZiXinXETddCIgX5VWAnXBS2JmZzdLpc_jLG0X3gABkU4t7RKGMUFl_enmfDhkIifWPoccR3_gG9xQgr1dA73t7gyUIqvDCFLEAI4oItyEygno--INkMDGMUjDFLNMB3KoTBHAI4AKqko16Mcbunaqj4CwMnfUzsw1-mfXm3uoRVMdz_QwoMsnBPvLC-NnesNzTGORWOOWDrpiKMl3p6Sqv5ehoN2btOXwW-Z4YZzKoLzfe8FcbfFA0T44-XWMWDrUJhlMgjSEiJHPlQGs16HgtN9EeBVAdkGvkwVx_fAuJikWGIvSa6Qq5ALvbNy9J4MEZE8L0N0LvJqOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1a648eba.mp4?token=AFKlzmJiZiXinXETddCIgX5VWAnXBS2JmZzdLpc_jLG0X3gABkU4t7RKGMUFl_enmfDhkIifWPoccR3_gG9xQgr1dA73t7gyUIqvDCFLEAI4oItyEygno--INkMDGMUjDFLNMB3KoTBHAI4AKqko16Mcbunaqj4CwMnfUzsw1-mfXm3uoRVMdz_QwoMsnBPvLC-NnesNzTGORWOOWDrpiKMl3p6Sqv5ehoN2btOXwW-Z4YZzKoLzfe8FcbfFA0T44-XWMWDrUJhlMgjSEiJHPlQGs16HgtN9EeBVAdkGvkwVx_fAuJikWGIvSa6Qq5ALvbNy9J4MEZE8L0N0LvJqOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از خطرناک‌ترین ماهی‌هایی که هرگز نباید باهاش درگیر بشید
🐟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/694095" target="_blank">📅 23:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694094">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای ترامپ: ایرانی ها خیلی فقیر شده اند؛ ما ایران را از داشتن سلاح هسته‌ای منع کردیم؛ تنگه هرمز کاملا باز است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/694094" target="_blank">📅 23:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694093">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
واقعا طلای میلی کجاست؟
اسناد منتشرشده از وجود صدها کیلو طلا در بانک کارگشایی و بانک صادرات حکایت دارد؛ اما سؤال اصلی همچنان بی‌پاسخ است:
🔹
اگر طلای کاربران وجود دارد، چرا تحویل داده نمی‌شود؟
🔹
حالا نوبت نهادهای ناظر است که با سند بگویند این ادعاها درست است یا نه و تکلیف طلای مردم چیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/694093" target="_blank">📅 23:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694092">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: ایران در وضعیت بسیار بدی قرار دارد و نمی‌دانم که آیا تسلیم خواهند شد یا خیر
🔹
در چند روز گذشته بیش از هر زمان دیگری در تاریخ، نفت از تنگه هرمز خارج کردیم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/694092" target="_blank">📅 23:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694091">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392a2b6a83.mp4?token=oFagFpgb5s5A18rIFkQcHxYG0QA8lGrhiXQlY8j_DMcIfu86bvuHxTNB7EUvA_iCbNO231xNoRHW3ErBKLIvNRe9kVEgwIeEN0rRHKCixgEMTs8jS7gnE9k_eTdEkukcqP7Gnfn7c73_a49sfpMAksz5OLjZCz_VfgZilf1XTMEEINUGTLJa3u2Egmkt6P1FQ5SL-zUpzuLDw2PMpv1qWwXbTqKLEHhuADsPI4OZHu7W5WBEQZv7cr3D87KZQljOfTKkShf1EEtRhgoWVTuWcVMbU-VTloNzDWbdJ8IqMx0mis5VX6BVfRcw-j6qEUszjfGn69Co2PHr_wCjixKn6we9fDhMCDagVZMcfryECA-py84jfmKcADqR2KcCbd4IgOuAvxFqHkLIo8GSTaATYjm1WInTw0iUE8mE2fj31aE6N6g-WtV11GmNr4V34OXYh8Vpgyza0lx4EgUYdoKymCd5c9E5YjaaUc1sScqwWLgfe9aRTkYY0LGZ_xM75WL6Yd608fhx5k452NSl0PG71BBGXlSHo_BOFq1RwZhBO_YWW6a5Yfql2RJOgMDNvjpeWkIRWKbze8L7w1YPLr6xc5wlRk7BCxqyb_qKzBOJURuj9d7uquqAmtlLeTm-hktcle2n9NR6M2IPTRT7yXffCPYSiKJ2r7ZxrnNFe5HAxiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392a2b6a83.mp4?token=oFagFpgb5s5A18rIFkQcHxYG0QA8lGrhiXQlY8j_DMcIfu86bvuHxTNB7EUvA_iCbNO231xNoRHW3ErBKLIvNRe9kVEgwIeEN0rRHKCixgEMTs8jS7gnE9k_eTdEkukcqP7Gnfn7c73_a49sfpMAksz5OLjZCz_VfgZilf1XTMEEINUGTLJa3u2Egmkt6P1FQ5SL-zUpzuLDw2PMpv1qWwXbTqKLEHhuADsPI4OZHu7W5WBEQZv7cr3D87KZQljOfTKkShf1EEtRhgoWVTuWcVMbU-VTloNzDWbdJ8IqMx0mis5VX6BVfRcw-j6qEUszjfGn69Co2PHr_wCjixKn6we9fDhMCDagVZMcfryECA-py84jfmKcADqR2KcCbd4IgOuAvxFqHkLIo8GSTaATYjm1WInTw0iUE8mE2fj31aE6N6g-WtV11GmNr4V34OXYh8Vpgyza0lx4EgUYdoKymCd5c9E5YjaaUc1sScqwWLgfe9aRTkYY0LGZ_xM75WL6Yd608fhx5k452NSl0PG71BBGXlSHo_BOFq1RwZhBO_YWW6a5Yfql2RJOgMDNvjpeWkIRWKbze8L7w1YPLr6xc5wlRk7BCxqyb_qKzBOJURuj9d7uquqAmtlLeTm-hktcle2n9NR6M2IPTRT7yXffCPYSiKJ2r7ZxrnNFe5HAxiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: ایران در وضعیت بسیار بدی قرار دارد و نمی‌دانم که آیا تسلیم خواهند شد یا خیر
🔹
در چند روز گذشته بیش از هر زمان دیگری در تاریخ، نفت از تنگه هرمز خارج کردیم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/694091" target="_blank">📅 23:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694090">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9d3b7a17.mp4?token=uv_ZElEpJY6vS845tKeN6CetCBMNxNW_EOAkLFTUWWsK1XMCun9wjO8mzd7YGKvq3AlBG_pIzdX4r3bRip0xPLGDy5uhOe2F1oXN3ZX_-21nmossa4Av02Eou14qX7rEG6DPaYvmI6hYvPaD4kp5BMjje7lyg7kxSD0LUUiYD-txNBhWcX_ov0BeK6qw_wZIZLvuFBXgoPKu1tqfoMWpxWSiB1InabiXXLZVDUHaUIMRB0--yTVdhs1L3zYNae6BvUrZ7TwYkqhKShJxHyLbuSz8r_AbpCZIH8jEKeDIYMW0R3OZMXWkwTnTxi7RECPZpzdCnS7i5UPx9KOr60fVZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9d3b7a17.mp4?token=uv_ZElEpJY6vS845tKeN6CetCBMNxNW_EOAkLFTUWWsK1XMCun9wjO8mzd7YGKvq3AlBG_pIzdX4r3bRip0xPLGDy5uhOe2F1oXN3ZX_-21nmossa4Av02Eou14qX7rEG6DPaYvmI6hYvPaD4kp5BMjje7lyg7kxSD0LUUiYD-txNBhWcX_ov0BeK6qw_wZIZLvuFBXgoPKu1tqfoMWpxWSiB1InabiXXLZVDUHaUIMRB0--yTVdhs1L3zYNae6BvUrZ7TwYkqhKShJxHyLbuSz8r_AbpCZIH8jEKeDIYMW0R3OZMXWkwTnTxi7RECPZpzdCnS7i5UPx9KOr60fVZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحقیرهای مکرر اروپا توسط ترامپ: اروپا هیچ جایگاهی در صنعت هوش مصنوعی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/694090" target="_blank">📅 23:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694089">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618ee8acb7.mp4?token=YpX-bEOc3BSr6NFHkT-OPW-RsoEt9ZHrioyRhuN1wjR23i9gUOn02xkZxga8NBMVP4RO6PJTc3lZNFdHl2zFGpY-pDf0JtNilIE1XESE2fka5iLAdLFdyJcBhMhdiyTqnycpu9BCbIZ2CjKdkCFJ0s7pUoz97dAgaXviPVsB9LRr8rt2x8UyJ4MXos8VamMsUP5UBo7XVflEJAdZ0IsRKlMAbSa_7P4eeFRta_2UtZNw0CBJk7f_eVEMmi25Jms3uBcdwP5-KgNCIC98rsqFGG1Gtvu9gkA69SIiXS539rAi9BgVcJW40kW7h5VGIW3JEq3OS2c-d7SVuhBptBav7l6G1BFup6WC8sa80hPOsRmW9eI8_0_jBQRMewW6AboYhgkDLjkrnU1fspdtOy6eWRVN_WyBrVJ0Z9WUEOSR87yLJzjKQxQ1Rc4omaxqTAXI7ufbyewsNEwf7N6pgqrctmAkPzg5AnO_4bco55WQgYCC4c8wlvfdWU-wmdUf7CZEUtWzxS7Hd0Gx1xoO8LmCuBkHTcryLGY22eVTKKzyhh4rXZ06NHODjtUr8WZpS1XJIH2CO8ELw7IT6ER9OuDSOzmEh2Z971hDnxxxQ0qCsdZgj90U2fk7KFg5KmFLhG3XauEPDDFYwBNI52lUWfBD5LJbor-UAWElZFeCa_B1C24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618ee8acb7.mp4?token=YpX-bEOc3BSr6NFHkT-OPW-RsoEt9ZHrioyRhuN1wjR23i9gUOn02xkZxga8NBMVP4RO6PJTc3lZNFdHl2zFGpY-pDf0JtNilIE1XESE2fka5iLAdLFdyJcBhMhdiyTqnycpu9BCbIZ2CjKdkCFJ0s7pUoz97dAgaXviPVsB9LRr8rt2x8UyJ4MXos8VamMsUP5UBo7XVflEJAdZ0IsRKlMAbSa_7P4eeFRta_2UtZNw0CBJk7f_eVEMmi25Jms3uBcdwP5-KgNCIC98rsqFGG1Gtvu9gkA69SIiXS539rAi9BgVcJW40kW7h5VGIW3JEq3OS2c-d7SVuhBptBav7l6G1BFup6WC8sa80hPOsRmW9eI8_0_jBQRMewW6AboYhgkDLjkrnU1fspdtOy6eWRVN_WyBrVJ0Z9WUEOSR87yLJzjKQxQ1Rc4omaxqTAXI7ufbyewsNEwf7N6pgqrctmAkPzg5AnO_4bco55WQgYCC4c8wlvfdWU-wmdUf7CZEUtWzxS7Hd0Gx1xoO8LmCuBkHTcryLGY22eVTKKzyhh4rXZ06NHODjtUr8WZpS1XJIH2CO8ELw7IT6ER9OuDSOzmEh2Z971hDnxxxQ0qCsdZgj90U2fk7KFg5KmFLhG3XauEPDDFYwBNI52lUWfBD5LJbor-UAWElZFeCa_B1C24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: پزشکیان گفت می‌خواهم بخشی سخنرانی سازمان ملل را بدون متن و از ذهن خودم بیان کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/694089" target="_blank">📅 23:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌ شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/694088" target="_blank">📅 23:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694087">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c102c082.mp4?token=fVORTM8qfjPQo1G5Fnuv7-xWTTpALEq0UnhgM6smCIP8REE5KKGzsDS1A3reQl3a6PPsjzOFdmcaC7xW95h-SZk7F6k2OI37q8CgYftDjTYvSv22XUxyQCr5iOvGhgU4Jvl1spNtAcfpjJuK9GyWjliOpMG3MtZj1fq1hIAu3Xdqn-RoFFbgodjc76X40dK06PT3PQ2UdJysDa-dA8BOuRg2eYp46MUQKrfiJr1kRSt6G43MPx-bBc1tX026Z4H8Mx67UNP6IjNfLWFujLHMMgOTtKvqEN_MGyJkNBplI7R0ispdU7Mj5BYzwsVqe-SV-X4MqvFbLZIb5xlaSvYxhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c102c082.mp4?token=fVORTM8qfjPQo1G5Fnuv7-xWTTpALEq0UnhgM6smCIP8REE5KKGzsDS1A3reQl3a6PPsjzOFdmcaC7xW95h-SZk7F6k2OI37q8CgYftDjTYvSv22XUxyQCr5iOvGhgU4Jvl1spNtAcfpjJuK9GyWjliOpMG3MtZj1fq1hIAu3Xdqn-RoFFbgodjc76X40dK06PT3PQ2UdJysDa-dA8BOuRg2eYp46MUQKrfiJr1kRSt6G43MPx-bBc1tX026Z4H8Mx67UNP6IjNfLWFujLHMMgOTtKvqEN_MGyJkNBplI7R0ispdU7Mj5BYzwsVqe-SV-X4MqvFbLZIb5xlaSvYxhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوشابه فقط یه نوشیدنی ساده نیست! هر قوطی می‌تواند حدود ۹ قاشق چای‌خوری شکر وارد بدنتان کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/694087" target="_blank">📅 23:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694086">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 1- میدان اول، توبه</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/694086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان اول، توبه
🔹
در لغت توبه (بازگشت) معنی می‌شود؛ یعنی انسان در مسیر سلوک می‌بایست هر لحظه از زندگی دنیوی و زیستن در نفس خارج شود و به زیستن با روح‌ الهی و درک جان بپردازد
🔹
توبه علمی برای زندگی بهتر، حکمت آئینه، خرسندی حصار، امید شفیع، تریاقی بسیار شفادهنده، سالار بار و کلید گنج و شفیع وصال، میانجی و شرط قبول، و سرّ همه شادی می‌باشد
🔹
هرگز دچار نفس و نفسانیات نگردید و هرچه هست را فضلی الهی که نسیب حالتان گشته است در نظر گیرید
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/694086" target="_blank">📅 23:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694084">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: فاکس‌نیوز را به‌ دلیل این انتخاب کردیم که نزدیک‌ترین رسانه به ترامپ است
🔹
بیش از ۱۰ رسانه بین‌المللی درخواست مصاحبه با رئیس‌جمهور ایران را داشتند و ما ۳ تا را انتخاب کردیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/694084" target="_blank">📅 22:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694083">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
هشدار جدید کشورهای اروپایی برای خروج شهروندانشان از ایران صحت ندارد؛ سفارتخانه‌ها پیام جدیدی صادر نکرده‌اند
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/akhbarefori/694083" target="_blank">📅 22:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694082">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f3f4ad98.mp4?token=RYymt2jyTrrEG3iWUkWH_WnDM5yLzdY7rUUPPfPNK8wnoLl_52iK9WyqIM4bUZ1yKIMYUdoyRU7DpP0Gxyn2RfB9QsSdInby_9yL9byHLNCnczcmbguXAdLcmz1bddt7GdGyzpmYHkz0mSF8hLcVDbGe-RZN6FSFYGQhcAReiJVu49Mfbuw7RLYXNrWogQTmS5zT1bjTfh7IdD_FSXNfviDr3svkV5ROH6-6PNrfQUz5mEBFyLnIXG9BLjfho4BBE6iYhi5aB2UA9ZHZk9Z7gFrzXkalm_qMO0Bjpv3ROJ_hSLhJcABtWS96Mfveibfbq9XLw7hwGEKV3oJUaWkKbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f3f4ad98.mp4?token=RYymt2jyTrrEG3iWUkWH_WnDM5yLzdY7rUUPPfPNK8wnoLl_52iK9WyqIM4bUZ1yKIMYUdoyRU7DpP0Gxyn2RfB9QsSdInby_9yL9byHLNCnczcmbguXAdLcmz1bddt7GdGyzpmYHkz0mSF8hLcVDbGe-RZN6FSFYGQhcAReiJVu49Mfbuw7RLYXNrWogQTmS5zT1bjTfh7IdD_FSXNfviDr3svkV5ROH6-6PNrfQUz5mEBFyLnIXG9BLjfho4BBE6iYhi5aB2UA9ZHZk9Z7gFrzXkalm_qMO0Bjpv3ROJ_hSLhJcABtWS96Mfveibfbq9XLw7hwGEKV3oJUaWkKbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگاهی که به انتخاب مکان مناسب برای ساخت ساختمان‌ها در چین کمک می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/694082" target="_blank">📅 22:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694081">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05abcb121.mp4?token=cJ9IaxRrP6eJcy2tlI4ePdnxpApY7BWmu4DMeheo4h28hZwkZLhyebTjbppgK9ztjkEXqHPWQlmchbH_EaIW5LqoyXimVKuzZpOyu7Nfp_y1GeA2SbqDMQ-Hm21B4x7HdVHmK5QVIJLpbIIsMmN4QUtOYysHtyhvvdKJ5bHYDxNuGylMcpRNfip4Y0mLDuRYE6eNQf0z6dLsZpjh4JPCoJdO1QIn34ZYFucuTCXlFK6-z7wCjoTx1lOoZOqrfZSDxaSa3Umgv39pQdefYKqn0iCAr4H5_M5uULg5jfadBFBwUjJvRWvNkCLtNYyobf69QmmCo7Yd1Jpb8eGx2uaspQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05abcb121.mp4?token=cJ9IaxRrP6eJcy2tlI4ePdnxpApY7BWmu4DMeheo4h28hZwkZLhyebTjbppgK9ztjkEXqHPWQlmchbH_EaIW5LqoyXimVKuzZpOyu7Nfp_y1GeA2SbqDMQ-Hm21B4x7HdVHmK5QVIJLpbIIsMmN4QUtOYysHtyhvvdKJ5bHYDxNuGylMcpRNfip4Y0mLDuRYE6eNQf0z6dLsZpjh4JPCoJdO1QIn34ZYFucuTCXlFK6-z7wCjoTx1lOoZOqrfZSDxaSa3Umgv39pQdefYKqn0iCAr4H5_M5uULg5jfadBFBwUjJvRWvNkCLtNYyobf69QmmCo7Yd1Jpb8eGx2uaspQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: فاکس‌نیوز را به‌ دلیل این انتخاب کردیم که نزدیک‌ترین رسانه به ترامپ است
🔹
بیش از ۱۰ رسانه بین‌المللی درخواست مصاحبه با رئیس‌جمهور ایران را داشتند و ما ۳ تا را انتخاب کردیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/694081" target="_blank">📅 22:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694080">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf8Jxo5EkhnGTF388oL3c32-Ji29fN1-jg34xXB49tn05L_uSUT2I2UL1ZRo1YZEuUXfh-o5W5UpcwJ_Dz8C2Xl7JfSGYEbjLaODZfMVU6tBNSQQSBbkSxiN6J8OTNS7RTUfQ-Rhevi_LGqb8tQUkaE3N5fe9vjY2SKxG9qrtns4bZMpVupIQFrz2pjVx0GHdoEYSO7teYhJx8J-dPBNHcxWevF1EquCwxAh362h6c9i4q6V-h50RTgVSXw0zWiOmeP6U20W37E-Yv8JnbWbg6saIql9wuZmoH0hZrOLQLuzVNgDqs1FgchXliKfXrpYbXQcS5nCHu-8pU5yxEPKpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره محکومیت حضور فتنه‌انگیز نخست‌وزیر کودک‌کش رژیم صهیونیستی در منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/694080" target="_blank">📅 22:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694079">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1670e8c287.mp4?token=T3MxlLnHe_Ha_4la07PlCkEXjNQUDBuRV6JvHoEopuSCs1p-LfOeWFKe0qdrz0Jq_wu8VDpf86wNrA0MIUeE9lB9WQChjW2RZLLczqrkP32szxZFkJGhehbHKAOE_ucEgVjfFS3QI6yKfoDbQ4cCrr9oh4iLfL4JNSfdXTf917F46Ed2ZfqAI0b9Yn_P-mcYv2MzN2NvfgIsSDP2NrNDTMVkfFURzHSr9ncKJDZFaToXqWXuY7SD8-1shqlvN1vxFIFzeplqJ1wGqQ6lVf0u7IVpi54JRcYHjmbVEZZNE2ZbTT1uxlzHcksXB4RfMGLfUGI2byOqZYVUO-JGdTgWdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1670e8c287.mp4?token=T3MxlLnHe_Ha_4la07PlCkEXjNQUDBuRV6JvHoEopuSCs1p-LfOeWFKe0qdrz0Jq_wu8VDpf86wNrA0MIUeE9lB9WQChjW2RZLLczqrkP32szxZFkJGhehbHKAOE_ucEgVjfFS3QI6yKfoDbQ4cCrr9oh4iLfL4JNSfdXTf917F46Ed2ZfqAI0b9Yn_P-mcYv2MzN2NvfgIsSDP2NrNDTMVkfFURzHSr9ncKJDZFaToXqWXuY7SD8-1shqlvN1vxFIFzeplqJ1wGqQ6lVf0u7IVpi54JRcYHjmbVEZZNE2ZbTT1uxlzHcksXB4RfMGLfUGI2byOqZYVUO-JGdTgWdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصیحت طلایی درباره ازدواج؛ فقط یک مجرد شاد می‌تونه یک ازدواج شاد داشته باشه و یک متاهل شاد باشه...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/694079" target="_blank">📅 22:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694078">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f8f25764e.mp4?token=m3zN7h-kCy9uihesVao2gxB0Z8uSe67LkGrjE0cwnmfzDuffDEMIwDjDWkPD1eggto4FkANT6--Fwh2ILI5Xr9AqxoNAsDFv_Trlcd_VyYvbANG848QtCQfumJxK-BktC1cPvzUS1JG5HrPYRyQSax1P_o0WVJhZ_c1xaA2dCnHCY7fagkK3ADUAC4uay604ZIb9z4e6bKk9P0UwsnMKqLujvOhx8Dp3rnTVHDZatjCgtc0G1Yppdh4xwN9yQvbZujpfCW0I7uwPZbzn7MWMpETezAYOmzDLhbW5GKXjZWo2wdo-o293Z62_JeEAN0hUx_NyYoejRIScRy5q9gw26g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f8f25764e.mp4?token=m3zN7h-kCy9uihesVao2gxB0Z8uSe67LkGrjE0cwnmfzDuffDEMIwDjDWkPD1eggto4FkANT6--Fwh2ILI5Xr9AqxoNAsDFv_Trlcd_VyYvbANG848QtCQfumJxK-BktC1cPvzUS1JG5HrPYRyQSax1P_o0WVJhZ_c1xaA2dCnHCY7fagkK3ADUAC4uay604ZIb9z4e6bKk9P0UwsnMKqLujvOhx8Dp3rnTVHDZatjCgtc0G1Yppdh4xwN9yQvbZujpfCW0I7uwPZbzn7MWMpETezAYOmzDLhbW5GKXjZWo2wdo-o293Z62_JeEAN0hUx_NyYoejRIScRy5q9gw26g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: آمریکا روادید سفر به نیویورک را تا دو شب قبل از سفر صادر نکرد و ما مطمئن نبودیم که ویزاها خواهد آمد یا خیر
🔹
بصورت آگاهانه تمام تیم رسانه‌ای و ارتباطی حذف شده بود و به هیچکدام ویزا نداده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/694078" target="_blank">📅 22:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694077">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
فایننشال تایمز: میانجی‌ها در حال پیشبرد یک توافق موقت میان ایران و آمریکا هستند که هدف آن بازگشایی تنگه هرمز و از سرگیری مذاکرات برای پایان دادن به جنگ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/694077" target="_blank">📅 22:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694076">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4017be95.mp4?token=mDzdNL6IPEg5dTy67GhfirbCViX06IwCeITFVCE7rUVuih00fqZKQwtjSDxSehZfQf7iFTy_wWMCtpbxyiPJIe5pU-Aw0BsYnDXcDs2XuiGYXlaodgIERJPCaG1aSF8cRtiVv1wB-gkr7CmT9oDE0GeFvhpyPH2-zYjDIznGLLuyMHNLD2pPYNpTVBRKjdOvuY1-o4wOlgonUCge9CwGVYljEx4XUCWykJhCueJbZi9eoOeDyvJ9TuNA785NUkE91YXD_O9IpsVyij--mXugA1-0tJ_hIppPVTVlIdD5CHgjRvewS8egpaGi28KbsRIA48ipuiT990A7SDzJRgtBNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4017be95.mp4?token=mDzdNL6IPEg5dTy67GhfirbCViX06IwCeITFVCE7rUVuih00fqZKQwtjSDxSehZfQf7iFTy_wWMCtpbxyiPJIe5pU-Aw0BsYnDXcDs2XuiGYXlaodgIERJPCaG1aSF8cRtiVv1wB-gkr7CmT9oDE0GeFvhpyPH2-zYjDIznGLLuyMHNLD2pPYNpTVBRKjdOvuY1-o4wOlgonUCge9CwGVYljEx4XUCWykJhCueJbZi9eoOeDyvJ9TuNA785NUkE91YXD_O9IpsVyij--mXugA1-0tJ_hIppPVTVlIdD5CHgjRvewS8egpaGi28KbsRIA48ipuiT990A7SDzJRgtBNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب و شگفت‌انگیز مثل لوت
🏜
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/694076" target="_blank">📅 22:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694075">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD4PfGQ_Eqe5kLyUWk6emQag75VN517alhypzc-uwN8O6toQWaD7c7JQxiW_MiRInL1kcAgR2YOju1Ql9uhHXR2qpXifdaxZukvvBJFoIBaJb1XXCwkl1aDJ1TXcuM5rnkriN-bAGH0RssYekqLkWk5j5uxEA6w-WCSBzx0sPJE5GHgSjHoiB7bE3mV6Ra_KfUG7NLYESGcvT8mT9M3yEH7pjGVNG6Pm7RYjhQatkMUhca9NsWpiXt8Owprt2OM_srqjSB8kyB5GeUnQS1FdXve2S6fYg5ffmgORoYTWkPJ-8nPCZxkxKfZ4nyQD2QM3XL8nEZcq0tSy2aazxt3ZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای خرید بیمه شخص ثالث، بیمه بازار داره!
همیشه تمدید
بیمه ثالث
برام یه دغدغه بود، اما این بار تصمیم گرفتم برم
بازارش
چون :
✅
می‌خواستم همه‌ شرکت‌ها رو با هم
مقایسه
کنم و مناسب ترین انتخاب رو داشته باشم.
✅
همه چیز خیلی سریع پیش رفت؛
هم بیمه‌م
فوری صادر
شد
✅
و هم چون امکان
پرداخت ۱۱ قسطی
داشت، خیالم از بابت پرداخت هزینه‌ش هم راحت شد.
👈
تمدید بیمه ثالث از بیمه بازار
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/694075" target="_blank">📅 22:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694074">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/694074" target="_blank">📅 21:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694073">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6f8cbbdd.mp4?token=OcdDuR_5aG5131lMOiyBxShY5jInMIBl2ato3Dcm4CIcqu4okZq6Eyzf04Hq5UtpL9hbdWNRpHCltjrzdgw5Cng4SYj1bjJs7Vj-XwbKLDgjMkkpzHVKWb7DCpcu6ClNMsx0CHZjlPBfnT2fDtPDb8rXlINi1LGISQ-VRnIaCI4xPLn0ncyjN7knzK4R_LfezpoUNvepNaHgnOqImKOe5nhLnUa9Hx3ouWW9KOaUXlBKqODngRpLR0IKEVD44Ah2RFRh5g-HyJJZ4V8WA-nUzgSoscLxa7Vb7xwRzeMHuVXjpbAmpAkzlfZ8gVN6NfbTtW-0FNUktSuShtlRu74YG2UMi_9kakzlLrDoORmEbai-avTIiiXGx7jmL8mHIm2SOBqaxnDPNu8WxdFhlLDF8c8el3qqZZFqLi2CzKGDq_To0r6cEGTN04WwLAon9iNVBGlOGldTAxUtdygVyZ4XuyCzxoZw1w_9r6I0XNpSr-R5_7rJOBiYMMviYT9mgKJSs9JmZelQiVV59Zl1V2c-oprAm3DOVH7vGggGUGe5KZcftdAX6itIDH3asp8y61m2-7TMDDDHtZ1KlAcRCwvf9DdQI2pr06g1jec9AeOUc_IKmI9XsRM_AaFdCBHY5ELfgR6JX8yDD5hmukh4GAm4ax8x1sOtXzkNSFASo-DbRJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6f8cbbdd.mp4?token=OcdDuR_5aG5131lMOiyBxShY5jInMIBl2ato3Dcm4CIcqu4okZq6Eyzf04Hq5UtpL9hbdWNRpHCltjrzdgw5Cng4SYj1bjJs7Vj-XwbKLDgjMkkpzHVKWb7DCpcu6ClNMsx0CHZjlPBfnT2fDtPDb8rXlINi1LGISQ-VRnIaCI4xPLn0ncyjN7knzK4R_LfezpoUNvepNaHgnOqImKOe5nhLnUa9Hx3ouWW9KOaUXlBKqODngRpLR0IKEVD44Ah2RFRh5g-HyJJZ4V8WA-nUzgSoscLxa7Vb7xwRzeMHuVXjpbAmpAkzlfZ8gVN6NfbTtW-0FNUktSuShtlRu74YG2UMi_9kakzlLrDoORmEbai-avTIiiXGx7jmL8mHIm2SOBqaxnDPNu8WxdFhlLDF8c8el3qqZZFqLi2CzKGDq_To0r6cEGTN04WwLAon9iNVBGlOGldTAxUtdygVyZ4XuyCzxoZw1w_9r6I0XNpSr-R5_7rJOBiYMMviYT9mgKJSs9JmZelQiVV59Zl1V2c-oprAm3DOVH7vGggGUGe5KZcftdAX6itIDH3asp8y61m2-7TMDDDHtZ1KlAcRCwvf9DdQI2pr06g1jec9AeOUc_IKmI9XsRM_AaFdCBHY5ELfgR6JX8yDD5hmukh4GAm4ax8x1sOtXzkNSFASo-DbRJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا ساخت بمب اتم جلوی جنگ را می‌گیرد؟/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/694073" target="_blank">📅 21:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694072">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
انفجار غیرعادی در ملارد رخ نداده است؛ مهمات عمل نکرده دشمن در حال خنثی سازی است
🔹
صدای انفجارهایی که امشب در برخی از نقاط شهرستان ملارد شنیده شد و ادامه هم دارد مربوط به عملیات فنی انهدام مهمات عمل‌نکرده است و هیچ‌گونه حادثه یا وضعیت غیرعادی در منطقه رخ نداده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/694072" target="_blank">📅 21:42 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/ODSb7qYGPBSP8CPij_bTJauttfoMmkYDajAkfCyexnIg6cXBE-3-SKgtMVwmtq6QYOj8DuOGWRyPrHREQQwXk5d8zT0StXV2y2NLf6nXKmHVZ8JIq7_KIS2U5AalaerSoht-r9jL8SuhGdP6Kp_FMDZKzpebEHWE3bs5TWLd-WY_pH4suARqj3cfLuWjzTTcc0HV3OR_TkqZ_KnC88byIsmhxUUKqYtoZYLj7rYlaCE_AFqPqmclqj0_srzQCK0lg8_jkLgq_eWl_e3waIbz_4kW9wg4oMz0lWSnbZb-e7KblN82BmO5oOVF0YlIbI2dormFLM52d3U70TsjZfq5Lw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 20:43:08</div>
<hr>

<div class="tg-post" id="msg-655086">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
یک منبع آگاه در دولت: اینترنشنال، کارخانه تولید اکاذیب درباره پزشکیان و دیگران است
🔹
با توجه به شایعه‌سازی «اینترنشنال»، رسانه وابسته به موساد، درباره استعفای آقای پزشکیان، این رسانه ضدایرانی کارخانه تولید اکاذیب درباره ایران است دیگر بر کسی پوشیده نیست، لذا طبیعی است که کسی شایعات او را هم باور نکند.
🔹
آقای رئیس‌جمهور استعفایی نداده، امروز مشغول کار بوده و برنامه‌های آتی او نیز طبق روال برگزار خواهد شد.
🔹
این قبیل شایعه‌سازی‌ها با دو هدف عمده صورت می‌گیرد؛ نخست: خبرسازی برای کسب اطلاعات امنیتی به نفع موساد و سیا و دوّم: اختلاف‌افکنی و شکستن انسجام مقدس اجتماعی در ایران.
🔹
منابع آگاه اینترنشنال، معمولاً محصول تخیلات و فانتزی‌های گردانندگان این شبکه هستند و وجود خارجی ندارند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/655086" target="_blank">📅 20:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655085">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مبینا نعمت‌زاده به دلیل پارگی رباط صلیبی بازی‌های آسیایی را از دست داد
🔹
معاون نیروی دریایی سپاه: در برابر زیاده‌‌خواهی‌های دشمن خواهیم جنگید
🔹
رئیس جمهور فرانسه: ایران و آمریکا باید فورا به توافق برسند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/akhbarefori/655085" target="_blank">📅 20:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655084">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
آن‌طرف فقط یک نفر بود: پدر
🔹
00:08:40 رؤیت ۳ آسمان و عبور از آنها
🔹
00:16:45 خیره بودن تعداد بی‌کرانی از انسان‌ها به آسمان
🔹
00:29:00 مشاهده نتیجه کمک به دیگران در کودکی
🔹
00:52:00 امکان چندتایی شدن و حضور در مکان‌های مختلف در یک زمان
🔹
00:58:40 درک چهره واقعی انسان‌ها پشت نقاب ظاهر
🔹
01:00:45 فقط به خاطر پدرم راضی به بازگشت شدم
🔹
01:06:00 تغییرات رفتاری تجربه‌گر بعد از تجربه
🔹
قسمت سوم، (فقط پدر)، فصل چهارم
🔹
#تجربه‌گر
: میثم نثاری
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/655084" target="_blank">📅 20:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655083">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79d39b094.mp4?token=TPbSxz0cluI1KQugS8507l1ahOMCiXhuc_UZidsYpLRa8GfUSKlNwphkcs-TMg2RPr5gUSQEWhSDygFylf9L2IaI9GeUuR6vPazmD0PT9A2DuMivonl2uzzmNY2eT3CLBPDYg2XQCjE_4qeQ5ruczJPgRZ038TON5yTL09A-XTpDEzALz1L3TjJtsvUpOaj2O1h-9jiQvWFmkv8ns4-hJSJVBkp27raemAva_yEK4qfm5_TC0BGrK1pHHiPc1z2ZGrhnrOczCU1OOy2sbQlKOjRdStWwCWIbIoXISr6ul7WEkjyjjGGwTgV1y5ZTmVNMhA1vg6V9gGkF3ce05g-kpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79d39b094.mp4?token=TPbSxz0cluI1KQugS8507l1ahOMCiXhuc_UZidsYpLRa8GfUSKlNwphkcs-TMg2RPr5gUSQEWhSDygFylf9L2IaI9GeUuR6vPazmD0PT9A2DuMivonl2uzzmNY2eT3CLBPDYg2XQCjE_4qeQ5ruczJPgRZ038TON5yTL09A-XTpDEzALz1L3TjJtsvUpOaj2O1h-9jiQvWFmkv8ns4-hJSJVBkp27raemAva_yEK4qfm5_TC0BGrK1pHHiPc1z2ZGrhnrOczCU1OOy2sbQlKOjRdStWwCWIbIoXISr6ul7WEkjyjjGGwTgV1y5ZTmVNMhA1vg6V9gGkF3ce05g-kpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آوردن پرچم روسیه به ورزشگاه برای فینال لیگ قهرمانان اروپا مجاز نبود، برای همین همسر سافونوف، دروازه‌بان روسی پاری سن ژرمن، از کیسه‌های پلاستیکی پرچم درست کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/655083" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655082">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
انجمن داروسازان ایران: «کمبود کدئین» ناشی از محدودیت در تامین خشخاش است نه تحریم
عضو هیات مدیره انجمن داروسازان ایران:
🔹
علت کمبود برخی داروها مانند کدئین لزوماً به تحریم‌ها مرتبط نیست، بلکه به چالش در تأمین ماده اولیه آن بازمی‌گردد.
🔹
سیاست‌های ممنوعیت کشت خشخاش در افغانستان و محدودیت‌های مرتبط با مواد مخدر، باعث کاهش تولید ماده اولیه کدئین در آن کشور شده و این موضوع به طور مستقیم بر زنجیره تأمین این دارو در ایران تأثیر گذاشته است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/akhbarefori/655082" target="_blank">📅 20:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655081">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_7Czlte7gd4P-5M8anSaDSjapum9zgZIlhDiw4zDUY3jqiySxxpNqLR2fPJqDu8jZpALBzMNVZJPF02ARrNahREDZTwz8A5SgcbP-NC3THkni0ehxWIBaTKuoCHtH6863NCXuglQUwRvt-IxDXOPiR9gL8LIJ_sXoQMuew8UzU8BEPEKGZ78HgAEbpsKQK3VxhdFeALQuxXizAnEkFD2Wsb4Bmqmdxw8Y9LFUOpw_wlbPBfd6Djinv2SE5mKd_WA-gXmDMfexydg9IYmVSM5nZVyyTQS429THV3zPJ_6ZLQY-Dc0q6gCEZF7HO_bogDyBYTC6YjS3IQErZvJ4-T_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: رویارویی با چالش‌های بزرگ بدون تحمل سختی‌ها شدنی نیست
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/akhbarefori/655081" target="_blank">📅 20:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655080">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d509bd7f2.mov?token=oNzV4lCCUJKUoPphgRaJiDcmmQtN7PaJ2NXCSng8L4AoY1DoxgLLkQBDM5BZdcTAcHqmRg2c5yWVKB_GQI5HuwvAheB7taFN3cLiGxAxW9eQHUl8nicsLW7u81ZX9PsrDCLgFoPxUUyp0MBJD5tT8QHuXPvDh31EyIriC6Nt5zUEx3NROxYWxv8SZzkPC0TQ2M-zhjRiUAHprMVmmrrYsK7qrNCi4Zx03AcCUn3Oo3a8RBa-kzJY6kP5roreHfknsltLj099DfTyRea0wgd2V9kqtflp540Kvm_3cOZxv32IZKhFb0hJdXKPu37gklGm2INhusjt1mjq7wnqx3SFMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d509bd7f2.mov?token=oNzV4lCCUJKUoPphgRaJiDcmmQtN7PaJ2NXCSng8L4AoY1DoxgLLkQBDM5BZdcTAcHqmRg2c5yWVKB_GQI5HuwvAheB7taFN3cLiGxAxW9eQHUl8nicsLW7u81ZX9PsrDCLgFoPxUUyp0MBJD5tT8QHuXPvDh31EyIriC6Nt5zUEx3NROxYWxv8SZzkPC0TQ2M-zhjRiUAHprMVmmrrYsK7qrNCi4Zx03AcCUn3Oo3a8RBa-kzJY6kP5roreHfknsltLj099DfTyRea0wgd2V9kqtflp540Kvm_3cOZxv32IZKhFb0hJdXKPu37gklGm2INhusjt1mjq7wnqx3SFMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب در میانمار، دستکم ۵۵ کشته
برجای گذاشت
🔹
در انفجار مهیب در انبار مواد منفجره در نامکام در میانمار، دستکم ۵۵ نفر کشته و بیش از ۶۰ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/655080" target="_blank">📅 20:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655078">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7TbWwwEhl6VHsTg6ytKwnUN79rdSr99rY0QRV-Am7kHu9r1MEKiQRSWc69Zp8tpikwoBJxFGZnANkdPeKLmTXMb55DMaOSJvQC-pwkTiN7_vOZT9JaRVKKQ0mDNGJpNT98sgNd3u08U3Jp_UlIz1yHVIrJlXIjDD_ZrTuZfIyn8yU8TdypTI83vbD2-LxkfjDAtSncZeUmoVpNXbQrkyVxjBVr_FEqvGsa2snljtr3n3UuntYalOtkOHWlilSIQgMhlXJpiGdKsT5VcyOnNOi3EoXv5t9VIJQEbUi1xceABL3QY-d_8jU7_mdw7c1KqZcX-BDxruJuneZjQXWo3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmB3NOxQMrYq9GgfVpcAnzThFivnX2a4aP7EY7Y1uFRxpCX79nRWlxBhrr58mmCMtpa24eH2MYAUu9CiJvHpLCw502hB8pAsGUC6As2IgwTG699kLz3fkzixkZKQTa2j7ulRkGEh3iHU5qnjeezGmsm97BLYEEO0oXe_2cLm5mZIBwPLIHIqe_ewVvy1tkk7760wnMdGtFnOXKbBb2D2do-j8R4SJAtWqANAocrsSizvm7H9ej1SMBw9OWg9aVRDKFNxlUFPRV92x7R8uRMWX5FXiknbPW-o8gkT-4zxgyXD83RPMEeNRqu2lj3-HlyGDvyfTXMqPi_hebhA0AlKHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: الغارات
🖋
نویسنده: ابن هلال ثقفی کوفی
🔹
«الغارات» کتابی بسیار مهم با ترجمه‌ای روان و دوست‌داشتنی، روایتی زنده و پرحادثه از دوران حکومت امام علی(ع) است؛ کتابی که یورش‌ها، ناامنی‌ها، سستی یاران و مظلومیت عدالت را ملموس نشان می‌دهد و فهم نهج‌البلاغه را عمیق‌تر می‌کند.
🔹
مطالعه این کتاب مناسب تمام کسانی است که می‌خواهند دوران حکومت امام علی (ع) را بیشتر بشناسند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/655078" target="_blank">📅 20:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655077">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
نیویورک تایمز: ترامپ شروط سخت‌‌تری را برای چارچوب صلح به ایران ارسال کرده است
🔹
به گفته سه مقام مسئول، ترامپ شروط چارچوب احتمالی توافق برای پایان جنگ ایران را سخت‌تر کرده و این تغییرات پیشنهادی را برای بررسی به ایران فرستاده است.
🔹
هنوز مشخص نیست که چه تغییراتی در متن این توافقنامه ایجاد شده است. اما دو مقام مسئول گفته‌اند که ترامپ نگران بخش‌هایی از توافق احتمالی است که شامل آزادسازی دارایی‌های مسدودشده ایرانیان می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/655077" target="_blank">📅 20:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655076">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d6f98f82.mp4?token=BPI5fi1ccjX-9a1HO_lBrvIYE0yNOZwsVSeQIguYdHioRYbzYU7HZ1VdvcLv2eET1CVhfhthKvXpQDT0OQBHzXeB_YY-UO0etqmhVyRIqISKCs5ahwUlIP_XdecwkMBNCCU0FviSTqoUOA7tYkVTXjlE_ViLcvqanDQ8cl8sEcykDjLfi9GokzrISKBnWrVY3uDjqlLvxFln3ziGYgwmqSwBwKG9E9XJg_OmHMuhI8amFX92wW-meMUvaPVM6zUtn5vj20eCAMuK0QdEvBfhdEtT1BqUra5Wdi9_aBxtYBBViX8W0qGs9uLmsOglh7Wfz7gB4BWYeIrv0K6vbfrA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d6f98f82.mp4?token=BPI5fi1ccjX-9a1HO_lBrvIYE0yNOZwsVSeQIguYdHioRYbzYU7HZ1VdvcLv2eET1CVhfhthKvXpQDT0OQBHzXeB_YY-UO0etqmhVyRIqISKCs5ahwUlIP_XdecwkMBNCCU0FviSTqoUOA7tYkVTXjlE_ViLcvqanDQ8cl8sEcykDjLfi9GokzrISKBnWrVY3uDjqlLvxFln3ziGYgwmqSwBwKG9E9XJg_OmHMuhI8amFX92wW-meMUvaPVM6zUtn5vj20eCAMuK0QdEvBfhdEtT1BqUra5Wdi9_aBxtYBBViX8W0qGs9uLmsOglh7Wfz7gB4BWYeIrv0K6vbfrA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
با این ترکیب جادویی کیلو کیلو وزن کم کن
😳
😍
👆🏻
این پودر جلبک جوری لاغرت میکنه که انگار اصلا چاق نبودی
👌🏻
کلیپ رو کامل ببین و از همین امروز لاغر شو و تغییر کن
☎️
لینک سایت اصلی برای دریافت اطلاعات بیشتر و سفارش با تخفیف ویژه
👇🏻
❤️
از امروز تا پایان شب می‌توانید محصولات منتخب را با تخفیف ویژه تهیه کنید.
🔥
https://landing.creditsw.ir/UEXKr
https://landing.creditsw.ir/UEXKr</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/655076" target="_blank">📅 20:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655075">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c72db1b5e.mp4?token=Mcbemubhn-4UAeDFDXCfVLYrQNgJ8Q9T5AsBhxaB0beHP4U3dFGTzt4RCW31zNO_uPDP_B9my8lEzkS_Rf2J1lSWhAqFqEUxNGVvOleUZXIAAVfDS4Qnv_Xb82E4sWy-QDZFnG66xyk1qQ11t4m8HzAkbxcmS-QquCT0ig3BMJkiuBioQpOWl0-_IIDTzVqrVtTmMO0I8IkYTh8yLNbQL9UF_QZ1AessEWffQHP5dqyBfOrjb83r3WAkXCPrNsKjNN-7tqTMe3HNow7rU8NSoIbCvVaS_XFSgxRXq_fT-qEi6VTmVLVNInJTRtdEOo7f8aUOrhYF5P5_1ffwqEXS6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c72db1b5e.mp4?token=Mcbemubhn-4UAeDFDXCfVLYrQNgJ8Q9T5AsBhxaB0beHP4U3dFGTzt4RCW31zNO_uPDP_B9my8lEzkS_Rf2J1lSWhAqFqEUxNGVvOleUZXIAAVfDS4Qnv_Xb82E4sWy-QDZFnG66xyk1qQ11t4m8HzAkbxcmS-QquCT0ig3BMJkiuBioQpOWl0-_IIDTzVqrVtTmMO0I8IkYTh8yLNbQL9UF_QZ1AessEWffQHP5dqyBfOrjb83r3WAkXCPrNsKjNN-7tqTMe3HNow7rU8NSoIbCvVaS_XFSgxRXq_fT-qEi6VTmVLVNInJTRtdEOo7f8aUOrhYF5P5_1ffwqEXS6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش گرفتن کارخانه هیوندای موبیس در هند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/akhbarefori/655075" target="_blank">📅 20:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655074">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
نبیه بری، رئیس پارلمان لبنان به شبکه «ان‌بی‌ان»: من تعهد کامل و فوری به آتش‌بس از سوی مقاومت را تضمین می‌کنم، اما چه کسی اسرائیل را ملزم به توقف تجاوزش می‌کند؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/akhbarefori/655074" target="_blank">📅 19:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655073">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4253207142.mp4?token=mzO5BCyymMHCZ7hlledYLGPPxvfj-PoEXkbDmQjQ3rDovjtCWaSqpepWQuZfQ8qyGasg7-GWRvUwpQJWSwxYbbmYNSbyDq0dQSMoDlbnkJ1gU-xMLev6hvbyWinz8KZnyFmWIYkBTuDQS0I1rrmU3BGfjm8as8VV0DRpuh-nPU-UgbL0q0Oou9lsnpFK6Sd_hUc7iGXy94BCEoWodxWlYW38Hat7GOL3oo0sIoWw3RD60mgx1-UZfn1twreQqNql_CuTaX1CBG_k0ifV-KBm6va4qBEsY2DuJPK475UL7NElEfgyTOmtF307Md9M56aZoASIj4nHbj39mZvTtjxnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4253207142.mp4?token=mzO5BCyymMHCZ7hlledYLGPPxvfj-PoEXkbDmQjQ3rDovjtCWaSqpepWQuZfQ8qyGasg7-GWRvUwpQJWSwxYbbmYNSbyDq0dQSMoDlbnkJ1gU-xMLev6hvbyWinz8KZnyFmWIYkBTuDQS0I1rrmU3BGfjm8as8VV0DRpuh-nPU-UgbL0q0Oou9lsnpFK6Sd_hUc7iGXy94BCEoWodxWlYW38Hat7GOL3oo0sIoWw3RD60mgx1-UZfn1twreQqNql_CuTaX1CBG_k0ifV-KBm6va4qBEsY2DuJPK475UL7NElEfgyTOmtF307Md9M56aZoASIj4nHbj39mZvTtjxnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا در گفتگو با فاکس‌نیوز: اطمینان از اینکه تنگه هرمز باز است، ما اورانیوم غنی شده با خلوص بالا را دریافت می‌کنیم و ایران سلاح هسته‌ای ندارد؛ موضوع ایران را تمام می کند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/akhbarefori/655073" target="_blank">📅 19:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655070">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9be5d7fff8.mp4?token=g8dZGMOOrS-13bHOm8T-whp1Ansi_rwMUE91CYqzPdIpVGBOa8uNJXfurWkDYXT1Tsyg5Co_7K45Cgq6ORc0TEF2MYOOtnLlM6egB2yxhEcc9FC-qox1spsbcFXeRs53uE91hnT4yVmBiOohNabvaiWpJYKvC6MjRO_jNtWne5hiX9NWQpmlgU1aEgOxsRQVkdrx82rBinxKPUUVZchW2XB2AgFcPZruERSdwMTaZmhlqz8X6mleDlRaMwgmLpzLWScn4BdPFAbmQpfyhab_iwYIKpIb6xmwiGPvIcm67n0ouReCNfX7By_UH2lcyx0klpo8r5wDCYAsokiGTbMCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9be5d7fff8.mp4?token=g8dZGMOOrS-13bHOm8T-whp1Ansi_rwMUE91CYqzPdIpVGBOa8uNJXfurWkDYXT1Tsyg5Co_7K45Cgq6ORc0TEF2MYOOtnLlM6egB2yxhEcc9FC-qox1spsbcFXeRs53uE91hnT4yVmBiOohNabvaiWpJYKvC6MjRO_jNtWne5hiX9NWQpmlgU1aEgOxsRQVkdrx82rBinxKPUUVZchW2XB2AgFcPZruERSdwMTaZmhlqz8X6mleDlRaMwgmLpzLWScn4BdPFAbmQpfyhab_iwYIKpIb6xmwiGPvIcm67n0ouReCNfX7By_UH2lcyx0klpo8r5wDCYAsokiGTbMCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات سنگین هوایی رژیم صهیونیستی به شهر صور
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/655070" target="_blank">📅 19:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655069">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213580575c.mp4?token=tbU4xoszAX8aqrzLET4q4pVx9TwYdJ_FK-aKRZQ5MTyUKEL2oThjejnNt3BLDQPM6LYXVOuCJZW4nlXNm0jfLnp2ylDjuBD2IO58sK2BLYSCEKS9Jtp3guniWEIPplfGyMhmfnSCzRcFnz1jaQsnCbkJIanmReOmqe47LZjVVV3Vrny98ZaeFVibSch4eh_gmq4PvK4G9vsz8ckIKDwx2uRWqLICdkS0xPawfPQndjX6F-U2NmGgFK_Afk8LFRHJlNKXNR5p3lxSKQOtmKY0opLiq_tpEMTCA_-OnXaa4dQNgIelu8EOi6WQ75S42kkp9aWhmAxzEYcUckXpnqE9qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213580575c.mp4?token=tbU4xoszAX8aqrzLET4q4pVx9TwYdJ_FK-aKRZQ5MTyUKEL2oThjejnNt3BLDQPM6LYXVOuCJZW4nlXNm0jfLnp2ylDjuBD2IO58sK2BLYSCEKS9Jtp3guniWEIPplfGyMhmfnSCzRcFnz1jaQsnCbkJIanmReOmqe47LZjVVV3Vrny98ZaeFVibSch4eh_gmq4PvK4G9vsz8ckIKDwx2uRWqLICdkS0xPawfPQndjX6F-U2NmGgFK_Afk8LFRHJlNKXNR5p3lxSKQOtmKY0opLiq_tpEMTCA_-OnXaa4dQNgIelu8EOi6WQ75S42kkp9aWhmAxzEYcUckXpnqE9qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی حضور ربات در نماز عید قربان در دبی واکنش برانگیز شد
🔹
یک ربات انسان‌نما با لباس سنتی اماراتی در نماز عید یکی از مساجد دبی حاضر شد و ویدئوی آن به‌سرعت در شبکه‌های اجتماعی وایرال شد.
🔹
این ربات که «بوسنیده» نام دارد، با پوشش کَندوره و شماغ در کنار نمازگزاران دیده شد و حرکات نماز را انجام داد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/655069" target="_blank">📅 19:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655068">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تردد سراسری خودروهای پلاک مناطق آزاد چابهار در سراسر کشور تکذیب شد
🔹
چین به خاطر مصاحبه با رییس جمهور تایوان خبرنگار نیویورک تایمز را اخراج کرد
🔹
سخنگوی آتش‌نشانی: دود مشاهده شده در اتوبان ستاری تهران مربوط به حریق در انبار کالا بود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/655068" target="_blank">📅 19:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655067">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c342424265.mp4?token=IxTwOryVdURcV9dbShBUJX82Uwn3rVs5zJLBtjrpZaDioWsQK5gu_gMT6ioJKMQJ6mX3Yh6fJNC-I_uo9KGXLmik086Xlzsdq951bzG1R1tE7CVLn9WRIn9g_UJlT10Ur7RvHgKJTfMclNROFCHHvHMYdbg8RD-M4uIfUuVLwhrno4G5JZsiDDcnPhJHHe7RRLy8nD4iOcsFYsCiqjB6Bpe_jQj7abppNYrnHo6pDb1kFiaYZc2WfH1r0wuZzQgJHTIJwHceBfgbZBWAa2SoXOYabXq2ltWntuHU_yCL6uvlEdIdqR1vANXSjJpzy8BInXMVajyXvVS9Epz9rRAukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c342424265.mp4?token=IxTwOryVdURcV9dbShBUJX82Uwn3rVs5zJLBtjrpZaDioWsQK5gu_gMT6ioJKMQJ6mX3Yh6fJNC-I_uo9KGXLmik086Xlzsdq951bzG1R1tE7CVLn9WRIn9g_UJlT10Ur7RvHgKJTfMclNROFCHHvHMYdbg8RD-M4uIfUuVLwhrno4G5JZsiDDcnPhJHHe7RRLy8nD4iOcsFYsCiqjB6Bpe_jQj7abppNYrnHo6pDb1kFiaYZc2WfH1r0wuZzQgJHTIJwHceBfgbZBWAa2SoXOYabXq2ltWntuHU_yCL6uvlEdIdqR1vANXSjJpzy8BInXMVajyXvVS9Epz9rRAukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حداد عادل از ساده زیستی رهبر آسمانی انقلاب؛ پذیرایی رهبری از میهمان با نان و پنیر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/655067" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655066">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtzCX996BLxT4baGrjKfppvVWIVv9nE1GJmCnUKNCp47HWFsyUy5x6vBpJ2PNkcx6g3GT49jwmn-CYgdFl_NHZzqPqJhCplMhAFae8Q5ZbfWZljh90ld7PV-wHa1djOvomjZ1ezqGaancf8lc03a2YYZ3qyDUSq5doWe4puTaQCMw7I20U8JbXq5pyaLGdDhnUA-ftsU8Yn59KG1GzieV0A-gZfBVfNndhZRSoD3S5PIKXdPms4kr535QEPVzhZ2FV9OnUOYROfPmUC1Pfgp_iV_kIleYRfCYpJjX6UsDxw9pkqAi_cucYLf4UtNNAhdn-5JMyA2G3q9A2oWPgHIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در شرایط «نه توافق، نه عدم توافق»، اگر پیوست رسانه‌ای مذاکرات درست عمل نکند؛ اعتماد عمومی قربانی خواهد شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/655066" target="_blank">📅 19:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سکوت سپاهان در قبال حذف از آسیا
🔹
مدیران باشگاه سپاهان در مورد انتشار خبری غیر رسمی مبنی بر حذف این تیم در آسیا فقط سکوت کرده‌اند.
🔹
این باشگاه به‌ دلیل نقص مدرک از کمیتهٔ بدوی مجوز حرفه‌ای را نگرفته بود.
🔹
با حذف سپاهان، گل‌گهر، چادرملو و پرسپولیس در صف آسیایی‌شدن خواهند بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/655065" target="_blank">📅 19:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655064">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سپاهان مجوز حرفه‌ای نگرفت و سهمیه آسیا را از دست داد
🔹
باشگاه سپاهان بعد از عدم صورت مجوز حرفه‌ای به کمیته استیناف اعتراض کرد. این کمیته اما همانند کمیته صدور مجوز حرفه‌ای رای به  عدم صدور مجوز داد. AFC با درخواست سپاهان برای باز شدن سایت جهت بارگذاری مدارک مخالفت کرد. بدین ترتیب سپاهان از کسب مجوز حرفه‌ای بازماند و نمی‌تواند در رقابت‌های لیگ قهرمانان آسیا ٢ شرکت کند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/655064" target="_blank">📅 19:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655063">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac492f7a9.mp4?token=W4Jr9wJev7ePDSAJUUXrssrL01WRXarUrxPpgclrPU2n0SsOwAUeZnWJq6Fyrkx8sftxADMV0RvYy15MVRkGZQM1_U3sjIW7s74ljzckTnYcwaiFTjUY2dESsj0E53Y1IE9ktPihKaAjQVA8LAmKKgLEY_-JKhg48UGE0JFbmDQ7krTpB93ZFzSI1IV3VVbGDSIV6j4bCGiXIPH5M8h5GGBmsHtw-Q520ABjdhMi3vj3IYhJ9-gHkFGoadF0y5LNu_LKJHSsvJSAsJ7qT12HQyW-G1Ghkcpev-uG1pxjHHDtL3qe7izTEKXmk52NrlYsVYtYSQCoG4ooVR-S_FgJTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac492f7a9.mp4?token=W4Jr9wJev7ePDSAJUUXrssrL01WRXarUrxPpgclrPU2n0SsOwAUeZnWJq6Fyrkx8sftxADMV0RvYy15MVRkGZQM1_U3sjIW7s74ljzckTnYcwaiFTjUY2dESsj0E53Y1IE9ktPihKaAjQVA8LAmKKgLEY_-JKhg48UGE0JFbmDQ7krTpB93ZFzSI1IV3VVbGDSIV6j4bCGiXIPH5M8h5GGBmsHtw-Q520ABjdhMi3vj3IYhJ9-gHkFGoadF0y5LNu_LKJHSsvJSAsJ7qT12HQyW-G1Ghkcpev-uG1pxjHHDtL3qe7izTEKXmk52NrlYsVYtYSQCoG4ooVR-S_FgJTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کار دست مردمه؟!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/655063" target="_blank">📅 19:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655062">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوهشت - دیده‌بان رشد اقتصادی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjA36z_Qqqqec57adJkbPkc5_birS4RDTPLLjMC39qWc-9JE8HRRXPTgtpmnSx7zqaXj-FFLz8-R7k07KroRuzZ37Fq6dQgq0cD33vJpirIYAeTnXlpuxTe4e6uHxDNVzMIXAIJVoBRaEoPnt0V-dlIw6YYolqpGPx-srLENB8ZxBrIvWB2TpQ0enJAwFrK9AK7hGcUK1VWK6R-_RHEFhjcSoLdxjofeBY61AuOdpN01TbJyuvZDt8bQ6nH6beWBhYr4vthRq2QX3c1rjNMhRc2QBzXZMGdFSYAT2yzmYR-bfK6VB8WlSJxHa6IvuwH32ArC-4nKWG1tXmvYmABK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔦
قیمت مرغ یک پا دارد!
تثبیت ارز رسمی نتوانست قیمت‌ها را برای مردم مهار کند.
🍗
از فروردین ۹۸ تا بهمن ۱۴۰۴، میانگین قیمت یک کیلو مرغ با دلار آزاد معادل ۱.۲ دلار بوده است.
در بازه‌های کوتاه چندماهه، قیمت گاهی بیشتر یا کمتر از این عدد شده، اما خیلی زود دوباره به همان ۱.۲ دلار بازگشته است.
🏢
این مقطع، بازه تثبیت‌های طولانی‌مدت نرخ‌های ارز رسمی (ارز تجاری و ترجیحی) است؛ دوره‌ای که در آن، این نرخ‌ها تنها در چند مقطع کوتاه توسط سیاست‌گذار تعدیل شده‌اند.
⛔
اگر سیاست تثبیت ارز موثر بود، باید قیمت مرغ به دلار آزاد برای مردم
کاهش می‌یافت؛
اما داده‌ها نشان می‌دهند که این قیمت در فروردین ۹۸ معادل ۱.۱ دلار بوده و در بهمن ۱۴۰۴ در
همین حدود قیمت
یعنی ۱.۳ دلار قرار داشته است.
اکوهشت
- دیده‌بان رشد اقتصادی ایران
@ecohasht</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/655062" target="_blank">📅 18:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ترامپ نگران شرط آزادسازی اموال بلوکه شده ایران است   سی‌ان‌ان به نقل از مقامات آمریکایی:
🔹
ترامپ بر عبارت‌های سختگیرانه‌تری در مورد تعهدات هسته‌ای ایران و وعده‌هایش برای بازگشایی تنگه هرمز اصرار دارد.
🔹
ترامپ نگرانی خود را درباره میزان پولی که ایران ممکن…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/655061" target="_blank">📅 18:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655060">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16459d2426.mp4?token=gSg8HirMflj4GN0hHdBmY_fRaZYCli7LwivRt36TrUSPN0BlKccV99YRiRDV9CCeGbEfEyX68XU9ZE4ZhHUVGoqFOlGzA6aa7UnoDWJdHq9uM0x4mITEOf7mKhKJBZOchLpfy_YkO0SbDlKRc9r_Qho6X18hjROGyllpz7sEr0IcZOR9l8NBzrES4oceqaaVjXqHml7TQzVuols3w3mtu1f13YvFLz4yeT_eaBS1yhMoKf1csLxVQmUg9dXCDCwIQp_VXj2nI2hjmtjFmOyc9i8bqYqW7Nd8IBXpa0Ezx17wN_yo42yf9ZMScbHgYHDv_LYP0lXMq8bldEOWlFB_MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16459d2426.mp4?token=gSg8HirMflj4GN0hHdBmY_fRaZYCli7LwivRt36TrUSPN0BlKccV99YRiRDV9CCeGbEfEyX68XU9ZE4ZhHUVGoqFOlGzA6aa7UnoDWJdHq9uM0x4mITEOf7mKhKJBZOchLpfy_YkO0SbDlKRc9r_Qho6X18hjROGyllpz7sEr0IcZOR9l8NBzrES4oceqaaVjXqHml7TQzVuols3w3mtu1f13YvFLz4yeT_eaBS1yhMoKf1csLxVQmUg9dXCDCwIQp_VXj2nI2hjmtjFmOyc9i8bqYqW7Nd8IBXpa0Ezx17wN_yo42yf9ZMScbHgYHDv_LYP0lXMq8bldEOWlFB_MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین ویدیو از خلبانِ شهیدِ جنگ رمضان قبل از شروع ماموریت
🔹
شهید جابر طاهریان از شهدای جنگ تحمیلی سوم است؛ که در ۷ فروردین به شهادت رسید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/655060" target="_blank">📅 18:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655059">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سی‌بی‌اس:‌ آمریکا متن اصلاح‌شده تفاهم‌نامه را به ایران فرستاده است  سی‌بی‌اس به نقل از منابع آگاه مدعی شد:
🔹
رئیس‌جمهور آمریکا روز جمعه متن اصلاح‌شده‌ای را به ایران ارسال کرده است و این سومین بازبینی متن تفاهم‌نامه از سوی واشنگتن محسوب می‌شود.
🔹
تغییرات آمریکا…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/655059" target="_blank">📅 18:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655056">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvRZ5gd7kGn2CMkrdrqBnzzMMncymX_KCkK7PcIUMBsnjKBIB3AmoGJ4DGiku1HRfcWBCA6E0rDO_iaNAVaRMrWqmMZYdIKAIwRkTfd5UjQBm92cd4FlXIxMRvzaIkxADBCch26kCLZyJNgGqkPqketFmZ-7Z5E50P6xDNNWtCegXqnH6w7ZsW_g5mYkooIPUBDqJFKTFie28raRi5nYtvpNiCMDqUTbMxTINpw9AQ_18N-Hg_nRIICFtdsNPKEBxrKi6sqmCVugGdK-G7eOYRou6lrobjh88-uFTIDzYUhYWHraS3VNiwbQEHbOhkh-QoUIJIu0A5WLBxThY9oP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulgCGJX4jqsYHg_2xV_NLAa9j6ocFMDF4CpuSEhdmSSC-gBWs4knq5wGfJ-0MvRuyYoqfRWdbISO__ZCsgNpIBCCfIVXGPbBqb3YNorl4YEmeKz5nJkDcrxihi3nsO86gAXSZZzHBHzq8c21BuZllvykuOkd4WUUuKz9yZ0mwiexGEKmPwtK2IOJEBkfm_lfKBn74TH0pQ3-ABf-398yET7WeuNcj2cuftb1fgbHxwRUoKk3l5_zD8iBsThQdkPc4U6dMwGrCMjkewbM_gmkCtvN0RAAKi3MBnrW8niva6ciq8d5Ws0_J1mxVccuO3Qq3O3qWoH-ByK9jBaD6ntWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFxkC_w4Lc7GmCiVsVuxN-Lm9Jo5FzNQOUKVgUWbsO6vle2baofRJdW3cM6r3xS1a2ZE8siVU27kqXAADkr18F41vyud-NllwTPtXC8-LjJuNV_7FF3V_9_oYz2Kf-pcyov8XS_NQA_xucoJXRwwD4xdeOUhajafXu0-jpHXBG5P1qa7QHBlAHmz4ypjJVPSwCAdiYxkowES2D2ufaRB20VydnzMRyRpUyOgZ6Unitdl45KyQunSOxNWxUwbmpbigWT6j-IPOAn4R_pfaqwavKYP6Y4zRcHHhfY2iMhiTHKNXn8qhzOXvlnIm2K2aeeRx27MFAwUo928fgHo9dSpug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری از ابرهای متفاوت لنزوار یا لنتیکولار در بلغارستان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/655056" target="_blank">📅 18:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سی‌بی‌اس: میانجیگران در حال مذاکره با ایران و آمریکا هستند  سی‌بی‌اس مدعی شد:
🔹
میانجیگران از صبح روز یکشنبه همچنان در حال مذاکره درباره یادداشت تفاهم بین ایران و آمریکا هستند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/655055" target="_blank">📅 18:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655051">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JavDtrLFWo7C_2e0uPU0Py0TJ8Aj_2IQvDCrb91niCapx-ataI5lzScM8cugkafZk90vKkQnvG0Cs-U9L56rlJjlhjlswN1xkrAlt4xKCpdnI5aIMB6CLOPCWAL0O8ymTol-aubKIK5uHaWQ_AWFXJMve2sjDzOeJ_tGQMLWqlbrJMGWufF8QGKEerdP5MkkgP-7IfRnlXqgC92YUnoHxMtpPMr-g6YFs5ZqEOCq1FS18ArjfxH9wYu5ngY-iHLLNHa2DIosgL5qn8WFaDV_JbfvrHTnuXojexL1OsW39_G_tRcGMWc1ZUwHFA9NRA_7iSQ2Ejf2DAPh9I_hgw6uYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PciPcW0RUMkpPtufCLLX-66Y_bwgvA2a-FrFwzeG18ypT-6_GomG2FLRvzjsdPSFfqTI_a0tA5sc0ydsCxD_Zapojye-gP6TtVFN_NgiVsc1OPwiBVAQnwGQcWx-7D4gbup9cVb01aS2uRQqQfU1I5jy0Ai7dPbITlTj-jFDdYme_cgR0zmgM98MWyVx_RIhzcajQmS8_f_CEeOsVo-QFhlsoWz0ImC3DoW31fXeuYgmgGwxwyvHk-I3sTB1SnjiHeIyjTq7n1Laq-1ow8HFeWh-2tjnIzB_rjVs2v8P4upItX7C9xxrZ_mBxD3vBCt91mLvf9AGVR8oCKjuXFmn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fa_0xVD58-yyCwtyQZQKM93NC_WXfqHz1PFosOUZg_Ns8rMix8YmkrVrlf5YUBjjpPqdf8ZAllowkaph9oJ15ls5MsZdTjBSHplFT91XB0-ALj22xakGgdUkqworbIfDAFb98VqrpTMTkt_oews-RFv0n6JP-75WMUfDV4_bsVVXmYepmXpzngvhThwO5iUNCIZ8iaTwOhmhl2JzBbG2Pes2rjZ_mTLWQvNbdvPFV10uwdXZ_0fACL1HYWV8nPuQHvrhCERHXEdcRUt7jbyOPaRUCGV6k_JoyBqxqdfnjZCz0mNwMnm1M_T2NGX_ZZXXKgCNjjDSDfP9nrYo77db8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADf-LP7aXfxnG6sj6m-3GSyEqM55k--55kt_z0lkVvHziIJGM7gpdyJwYTKAUQxyyQkPd4XNZD635CuEWfNHShkuPtNLCwAraTD4-WbQz7_CAxwA0HFA3XAgRgm3pGadSptwHbNo9tUqURXp1rYGmrlCAmOWoxgzFENH7X9Me8aIKkoQRUlmPSfbOKscFfXkh_uJEvxrQ8Du67_jPzgLFwSUiuFG-J4lPwnyYWRGKYbF3VFtTBi8F4rm72Kn8KxBn4YKAnXsHbwcFaE45kTbfmpp3XDC4tbGuxXTc9Qakj2UTpX-bcRllUNfa4zu5x6r-60pNWrYFqe7qCo9O6MVeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از خوش و بش پزشکیان با وزرای دولت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655051" target="_blank">📅 18:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655050">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi9dnV564DhgINYV4OPkI-gtUGQsRMjS91y6SKazL2Icu0GudeMcDOZdMTCS2Hm3DpMw0YwYKfjE5yjLihCqKxkYK8hDVi4N7BAs-QGun4WwtbTwNtg_D7Sold_0jYCK06-SptmTuRABjmoXXfMjXbB7IzQYlrOAByRS6NT3yx3dYjHpKe5cVF-mZbRsnJh7gVYSWX7sh_fPLa1nGvlcYOZgDMCkPJPsQUpQ1cxBF_zbC4BlrrXCsKhwl7uYaPS1IGJBT8u9TCqmRNKUTT3XfzadM2FR19gSIgAo7zVIGi0bmQQZhoSacwblPYV0w4reKTRUW2F4J4AXA24BNYVfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاندان بختیشوع؛ بنیان‌گذارهای پزشکی علمی در جهان اسلام
🔹
خاندان بختیشوع یکی از مشهورترین خانواده‌های پزشک در تاریخ ایران و جهان اسلام بود. ریشه‌های این خاندان به سنت پزشکی جندی‌شاپور در دوره ساسانی و پیش از اسلام می‌رسید؛ جایی که دانش ایرانی، یونانی و هندی…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/655050" target="_blank">📅 18:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655048">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
♦️
پزشکیان: جامعه باید نسبت به الزامات و هزینه‌های مقاومت آگاه باشد
🔹
اگر قرار است کشور با اقتدار مسیر خود را ادامه دهد، باید واقعیت‌های موجود برای مردم تبیین شود و همه بخش‌های جامعه در این مسیر مشارکت داشته باشند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/655048" target="_blank">📅 17:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655047">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
♦️
پزشکیان: هیچ جامعه‌ای نمی‌تواند در شرایط رویارویی با چالش‌های بزرگ، انتظار داشته باشد که بدون تحمل سختی‌ها مسیر خود را ادامه دهد
🔹
مهم آن است که این مسیر با آگاهی، همبستگی و مشارکت عمومی طی شود.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/655047" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655046">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پزشکیان: شرایطی که کشور امروز با آن مواجه است، عادی و ساده نیست
🔹
مدیریت این شرایط نیازمند هماهنگی، همدلی، گفت‌وگو و تصمیم‌گیری‌های دقیق و مسئولانه است.
🔹
تداوم برخی محدودیت‌ها و فشارهای خارجی، به‌ویژه در حوزۀ دسترسی به منابع و ظرفیت‌های اقتصادی، پیچیدگی‌های…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/655046" target="_blank">📅 17:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655045">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
پزشکیان: شرایطی که کشور امروز با آن مواجه است، عادی و ساده نیست
🔹
مدیریت این شرایط نیازمند هماهنگی، همدلی، گفت‌وگو و تصمیم‌گیری‌های دقیق و مسئولانه است.
🔹
تداوم برخی محدودیت‌ها و فشارهای خارجی، به‌ویژه در حوزۀ دسترسی به منابع و ظرفیت‌های اقتصادی، پیچیدگی‌های خاصی را برای ادارۀ کشور ایجاد کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/655045" target="_blank">📅 17:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655044">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سی‌بی‌اس: میانجیگران در حال مذاکره با ایران و آمریکا هستند
سی‌بی‌اس مدعی شد:
🔹
میانجیگران از صبح روز یکشنبه همچنان در حال مذاکره درباره یادداشت تفاهم بین ایران و آمریکا هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/655044" target="_blank">📅 17:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655043">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
حمله موشکی به حزب ضد ایرانی «پاک» در کردستان عراق
یک مقام حزب به اصطلاح آزادی کردستان به روداو:
🔹
روز یکشنبه  پایگاه مهم وابسته به این گروه مخالف ایران نزدیک اربیل هدف حمله موشکی قرار گرفت. این مقام، این حمله موشکی را به ایران نسبت داده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/655043" target="_blank">📅 17:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655042">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae626b6d9b.mp4?token=N_o_4Si-lteEcVYFnf6VN660KRTbTH0vyZeK3ioXo9wzj8WjJjyVz55ChJaDdpHI1gvP7Pqy07ZRxjdxz5wRe_-8o2G1k0EDH5PHmExTT0Fo-IZR2dD0u_VBTTxCo8p8oLYFIwJVroHmcHMm0krtcXhmKtFwGlpY6HxuslDoBWkDGRIs41BeRR_wlYkLrRQWGsFTLNtLCXHy-rzAa4Ocj29ThuU-X5FGNrcJU8OjLs8mazReYK2xOiJaJwjZPEIXoHJCbK5mOA8tteDfPpzrowARmJrhEg8mFK_A0cMJB_k5aXnQM5UccLtCzfturalnJkzVrG6vBSaKiAtGTD6Gnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae626b6d9b.mp4?token=N_o_4Si-lteEcVYFnf6VN660KRTbTH0vyZeK3ioXo9wzj8WjJjyVz55ChJaDdpHI1gvP7Pqy07ZRxjdxz5wRe_-8o2G1k0EDH5PHmExTT0Fo-IZR2dD0u_VBTTxCo8p8oLYFIwJVroHmcHMm0krtcXhmKtFwGlpY6HxuslDoBWkDGRIs41BeRR_wlYkLrRQWGsFTLNtLCXHy-rzAa4Ocj29ThuU-X5FGNrcJU8OjLs8mazReYK2xOiJaJwjZPEIXoHJCbK5mOA8tteDfPpzrowARmJrhEg8mFK_A0cMJB_k5aXnQM5UccLtCzfturalnJkzVrG6vBSaKiAtGTD6Gnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ سخنگوی دولت به سوالی در مورد غیرقانونی‌بودن تشکیل ستاد راهبری فضای مجازی: این ستاد همان شورای‌عالی فضای مجازی است!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655042" target="_blank">📅 17:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655041">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpdwyhHpEQV8W2dxl1r6VYZkBPQl8GLXzKJsuRXy7HvGcyq_WJPDv8diKbKMb76UktHuHMWPhTEvnIE5rDo98NUl5vSXhhDCIoH6zl4PKencdYnqdOLX64tZagq7fAvmZ_m8XCGAsa8WMFnXzymu_VCk3Jcg0YFOYzgN8-rgElKaYtj6jCt0dlFmhQCNBf9lMwgLYIKxXy_QtrWHiryKADJ3HZvs8GRN5K4NbUbSFVPO5H5B6aT3O4ZNtPueJN_QhfEltse4WfmlNntDlHfPWLldgKgX6pY-UUddlOTdN5BcsmGWezCgSJX8byBQgc99XFuvYo9s3YWdYRKxCQ14GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلاش ۲۶ میلیارد دلاری پوتین برای افزایش طول عمر | علاقه به جاودانی جدی شد
🔹
گزارش تازه وال‌استریت ژورنال توضیح می‌دهد که علاقه دیرینه ولادیمیر پوتین به موضوع طول عمر و مقابله با پیری، اکنون از یک کنجکاوی شخصی فراتر رفته و به بخشی از اولویت‌های راهبردی دولت روسیه تبدیل شده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219241</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/655041" target="_blank">📅 17:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655039">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rHxv2dJBVxnZ329IZGKMcibbRm3tKOzQd4nFs7LVBw9AM9a1pztvsTSV-u4kqavdlMB8NqYs61SEGzIQTb2OWTBBfT2WWS_XwqhPP1ri0FkL8niEoY2CjEzNJNgkDmDKdRjTxoE0OVGWisrqXn5_ELd7UBYwAobG3ib3dLtXYdatcp_cJN4clbuMQVcWI8kQSHgElFaRLJRINgv1tIMRqw-3mckNNZFwSqSdzIEkyfyoa7Kl14vdzLNjYHnzy3d_6AANACTc7U_CwZDp8rHNOY_F-EFCKDVvxOQ_EhMIO6VxRaX6EYy0zIgm0tlnIsaC2VSomH4jCljYxzPYfHYbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqWFB4zDNSpe1iSCcuXIxz3FqxhkpjtC61b_n7xH1Z-LB1SaYEz5_-BYq3Add749G7DQDtmFVXKqBCj-gBlohFHlr38UnYgwqcI-ECGQV_-FGJkgqvi1JfOY9WLm7PeOCrHnx7i53PP59_HKe1SuJeLsS0rjkBY_GSTxjyjvfvrxh6b09WKXMiVQfvX1p5NKbAu3-wr8zXanpHJRT92NVwYxYTO7xxxMjfkayfM3-_W4Ki-BTT57DDFrq7Rlb0lH8miexbLwIxIWwuSb945izcfHUA3ZXUxvGiKRqvpSs9DJzQ9ImzW7rxbkI_OSbWaXPV-VPwWfjiUzYKYMXKuu6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از یک سوخت‌رسان آسیب‌دیده آمریکا در اثر حملات ایران
🔹
اویشنیست تصاویری از سوخترسان KC-135 نیروی هوایی آمریکا را که در پی پاسخ دفاعی ایران به پایگاه‌های آمریکا در عربستان سعودی با ترکش‌های انفجار مواجه شد، منتشر کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/655039" target="_blank">📅 17:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655038">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544378e4c3.mp4?token=cifHzpnbFFM2d4B5Yv7eu_N3c2AsviQVN7cp8XtgnTKAhBbcB76vFTgxg7q7-2n0AF4SjxeNhcnHi5Qtv7uO5GfCSEX9uLaTBFzfUFVlYoHK1tysH_2SLoZTt6AOwn1kr1Tx9nkIWqx7OqsGyCFcG4pTaekPEx1KGOqrISuOvMoCP6_nsaIFgqbW1PuEYRMiJfnI6NqccuToH7ZMvxJvMT4qPYlz1LiHntZ0qMn3UvDzu9iTy4Eh-e5Sg2q4564XFsVhZW1zuQ7wR-RWLA9lbNLqMPv73t_pJa_GNrcKWXkLEh86v3b0yd2yRk3LMpETB7pNhh1_PprsgQYbW6eaHHogU4NCusbOOxERn_sZatGU0wvafRz1EktUvGR728hjS7geCG_5bsga70Bl14MIiPkSKJYUT2KSKqQ8lIPhTjuLb4VoLlC2dwv3O7aNiNLNopAO_kDJRPEBgf322HZpu-a2gsVZYR9UaxAM_zRucdy8J8J89kzUe5uJbn4dZA9dzKgKBuBXZ9rqclK5m_R4ryv38bUTnCg9P9a4jhjhnYMeYy-C3lVBxo4xyQbFnmEzYqTmi-cvo-SY8vAyush-VS_RqWzU8Nqp30T7WsdQgugGxE5teaUH1r0Js3Jm4EmCcdzhx5ovVTjSTOGtv4tlR7eWCOmjltpx8s9rtif_G1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544378e4c3.mp4?token=cifHzpnbFFM2d4B5Yv7eu_N3c2AsviQVN7cp8XtgnTKAhBbcB76vFTgxg7q7-2n0AF4SjxeNhcnHi5Qtv7uO5GfCSEX9uLaTBFzfUFVlYoHK1tysH_2SLoZTt6AOwn1kr1Tx9nkIWqx7OqsGyCFcG4pTaekPEx1KGOqrISuOvMoCP6_nsaIFgqbW1PuEYRMiJfnI6NqccuToH7ZMvxJvMT4qPYlz1LiHntZ0qMn3UvDzu9iTy4Eh-e5Sg2q4564XFsVhZW1zuQ7wR-RWLA9lbNLqMPv73t_pJa_GNrcKWXkLEh86v3b0yd2yRk3LMpETB7pNhh1_PprsgQYbW6eaHHogU4NCusbOOxERn_sZatGU0wvafRz1EktUvGR728hjS7geCG_5bsga70Bl14MIiPkSKJYUT2KSKqQ8lIPhTjuLb4VoLlC2dwv3O7aNiNLNopAO_kDJRPEBgf322HZpu-a2gsVZYR9UaxAM_zRucdy8J8J89kzUe5uJbn4dZA9dzKgKBuBXZ9rqclK5m_R4ryv38bUTnCg9P9a4jhjhnYMeYy-C3lVBxo4xyQbFnmEzYqTmi-cvo-SY8vAyush-VS_RqWzU8Nqp30T7WsdQgugGxE5teaUH1r0Js3Jm4EmCcdzhx5ovVTjSTOGtv4tlR7eWCOmjltpx8s9rtif_G1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرآیند بازسازی بوگاتی ۱۹۳۲ که به آهن پاره تبدیل شده با هوش مصنوعی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/655038" target="_blank">📅 17:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655037">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4c5c5bc2.mp4?token=Exz4J4Mb6Cf1biKFVwthVaWWsz89hW3teXlm0p8FMBCb0hGgfePQlsaXruRqphQTYSEUIcNVmpMEMSE0ouAWDLereInoyj3shT3J9Kt7eQjbAsJKM7bo58RNc6MPAvwzkXgw_tLlfqCgTMMzpxiHOEyIEWfcPdXAjdPkGUTGKN91FEckzglnlx7PKuS4SVqqUl3gu4Xa07RkpTAbtHiVunUkIe0ckIfWyN6U6YHA5IOenGTsEkk5qkThHX2pEFJorq9_FPeVAo_ELb3C_IEAf2xg2lmMV0W9RtE_1AYrxXO9EK_wYJVe0FStuHc5Uf-Kg4FwQjdqiaegyBCDqoOPcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4c5c5bc2.mp4?token=Exz4J4Mb6Cf1biKFVwthVaWWsz89hW3teXlm0p8FMBCb0hGgfePQlsaXruRqphQTYSEUIcNVmpMEMSE0ouAWDLereInoyj3shT3J9Kt7eQjbAsJKM7bo58RNc6MPAvwzkXgw_tLlfqCgTMMzpxiHOEyIEWfcPdXAjdPkGUTGKN91FEckzglnlx7PKuS4SVqqUl3gu4Xa07RkpTAbtHiVunUkIe0ckIfWyN6U6YHA5IOenGTsEkk5qkThHX2pEFJorq9_FPeVAo_ELb3C_IEAf2xg2lmMV0W9RtE_1AYrxXO9EK_wYJVe0FStuHc5Uf-Kg4FwQjdqiaegyBCDqoOPcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکید رییس سازمان بازرسی کل کشور بر لزوم تامین قطعات مورد نیاز سایپا/ قطعه سازان بدون گروکشی قطعات خودروهای ناقص را تامین کنند
رئیس سازمان بازرسی کل کشور در بازدید از شرکت سایپا:
🔹
عدم تحویل قطعات از سوی یک شرکت خاص به سایپا موجب تولید ناقص ۵۲ هزار دستگاه خودرو شده که این به دلیل انحصار در تامین برخی قطعات است. وی افزود: در شرایط فعلی، هیچ‌گونه کم کاری و عدم همراهی از سوی قطعه‌سازان به بهانه وصول مطالبات مالی پذیرفته نیست و تأمین قطعات باید بدون وقفه به سایپا ادامه پیدا کند تا مطالبات آنها نیز از محل فروش خودروهای ناقص تامین و پرداخت شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655037" target="_blank">📅 17:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655035">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDcBCLgvFzwR1EogDYCgjA4u0XDyRVWhwU599ywrtAl-mMP1-fLN05itGWv4RZypaswqy1eN3zJD-2Pstpn2EmP65jdIqOeVwj2ruMoxhVeB_Ll5j2SM6_ui2HWfGKiFq-kaH9REHUzEqstxD1WQhLp1ctftFsLvSj50n-6lWh92-7s6BdIwmF95Y7J6iZ7pSgYL8giE3uMmutOfnRNoXtR2oHhfyeFwjCzqKdkCj4lBcOn6FrZTqOxKfkjlap_9zztpJhprTNYwF2078KqbeCYKckLoEF-_rvYSXNJZIL3XE6EgVdLOfMyLQj7VYuj7gh2dEZfCwFKWQGYZIoTPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817b2c792b.mp4?token=DcZyov1JMAPFlTs1_cOpeuD6XvVz8-mH9jmo_Z1PukvzpXc_CYTH768LweU5PcZYPFtoLid0c2sQmTmEYbDURpdg03PKeSa4g_x3Me3-kBmuSJ1XtIzf2TY2xTT3CgHpuwy1BOQTZGjCY6DV56McayCgr14PlbmAFcb05iu7cdgtGVpE39Ep6HiuBABCveWPN73nudY09UsxTW1YzrgPcHoxT9_fl1iLifK09THewCEwsPog8lXoVZRa2mjZQrJJOlQ8hVNAV1iVUhQx5tgUJzYoPIUszK80laKsbqpPXvxHI4heMjidbG_WsH3XyI1SUj3C0Nifl52gpZD5LpEwyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817b2c792b.mp4?token=DcZyov1JMAPFlTs1_cOpeuD6XvVz8-mH9jmo_Z1PukvzpXc_CYTH768LweU5PcZYPFtoLid0c2sQmTmEYbDURpdg03PKeSa4g_x3Me3-kBmuSJ1XtIzf2TY2xTT3CgHpuwy1BOQTZGjCY6DV56McayCgr14PlbmAFcb05iu7cdgtGVpE39Ep6HiuBABCveWPN73nudY09UsxTW1YzrgPcHoxT9_fl1iLifK09THewCEwsPog8lXoVZRa2mjZQrJJOlQ8hVNAV1iVUhQx5tgUJzYoPIUszK80laKsbqpPXvxHI4heMjidbG_WsH3XyI1SUj3C0Nifl52gpZD5LpEwyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده یک مین دریایی بزرگ در تنگه هرمز نزدیک عمان
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/655035" target="_blank">📅 17:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655034">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
کشتی آزاد نوجوانان ایران قهرمان آسیا شد
🔹
تیم ملی کشتی آزاد نوجوانان ایران در پایان رقابت‌های کشتی آزاد نوجوانان قهرمانی آسیا در ویتنام، با کسب ۴ مدال طلا، ۲ مدال نقره و ۲ مدال برنز و مجموع ۱۷۸ امتیاز به عنوان قهرمانی دست یافت.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/655034" target="_blank">📅 17:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655033">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1acebe8b5.mp4?token=Pvdgwe7dLLnFwaB_tBZuDPDX3CEUnLYV5U_dM9yRqdwyA5C5p0TsOc-aGlGCmvntcD723y65ujcYdf6U-mH2NZx8gxbGO4l424y7jPHJZ25JJrKQOqXlbFjRMFokvW3bnS8bkfGotRiKpQKhXhG8IcorJ7Ly5XqB4-7KzW0cuOVhIIO9d-oE4QjIhdAuwjZxvaiLVIDoeoQlvbu2Aa1cSjn4HPPPD3HLiX1Dc-Fq3csU2rcSEA2tmvHGLgDVK6Bf1ye16EKRte31uJ-nojV45jMCaqugumrwa8Z-mRd9jVQSqg2mXgZaUTSjF0KoDksOl0nI1u_qQc8OpUgu6W5oZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1acebe8b5.mp4?token=Pvdgwe7dLLnFwaB_tBZuDPDX3CEUnLYV5U_dM9yRqdwyA5C5p0TsOc-aGlGCmvntcD723y65ujcYdf6U-mH2NZx8gxbGO4l424y7jPHJZ25JJrKQOqXlbFjRMFokvW3bnS8bkfGotRiKpQKhXhG8IcorJ7Ly5XqB4-7KzW0cuOVhIIO9d-oE4QjIhdAuwjZxvaiLVIDoeoQlvbu2Aa1cSjn4HPPPD3HLiX1Dc-Fq3csU2rcSEA2tmvHGLgDVK6Bf1ye16EKRte31uJ-nojV45jMCaqugumrwa8Z-mRd9jVQSqg2mXgZaUTSjF0KoDksOl0nI1u_qQc8OpUgu6W5oZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور سرمایه‌گذاری حرفه‌ای انجام بدیم؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/655033" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655031">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
کشف محمولۀ تجهیزات ضدامنیتی اپتیکی در منطقۀ مرزی ارومیه
قرارگاه حمزه سیدالشهدا نیروی زمینی سپاه:
🔹
محمولۀ تجهیزات اپتیکی شامل مقادیر قابل توجهی انواع دوربین‌های پیشرفته و تجهیزات شناسایی با کاربردهای نظامی از گروهک‌های تجزیه‌طلب در روستاهای مرزی ارومیه کشف شد.
#اخبار_اذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/655031" target="_blank">📅 16:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655027">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPrG765-H7lHJW8A9udRmB1441AeysEGIyyc0gysyAd9LMDHLqAT6SN05go9ESXD-mxdg-NVl4n3cZwrB7oCiMjPxDeQJjTW95tYHmN57BV_S1t0XoS0gtj9QGERuFBN_ASP80V_K6eTx1jWfw9MbgR_OY2W9YRVVMg7MeoEWJAyKfr7mzYEiWBdvPhfGV-DKh94N7KCfql-yJAL9Kgj202nWNVYqgNvK3qEtqVZWJ0iP1GZA9zeWMSb5TeOXytSgBdz0mfdXyCDB0u8OOqCCAlMYicMy0qbufVxZKXyUS5lW46XcdibOKBiB5-_BiWX7P-5_P2xiUH5xi3mC89UtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cK4XIIJBvSyQiQ_wyav95Eri104dPZy4R1neOMRBW-pR--vG9lfOSGyrSePg6DZc__cJCsHQRDK9xAslO_QO1aGiwGv_iJ6-EX6M1E6f6yl3Mu7HziH5Q4aOGntavuSFslol8Hfs1dWDDMO5K8ZNwF9is4U3vstn9RODGk0gIEqk-cIrNm7G7Q4jU52nXkIVZ97H0tzhxdcOQn6-QyPEnDr5nzJAPKHfA1gTycCFXI4cV761WM-Q0NTwf_rqkZVhsR_M3Cir4fuWTToGvrbdJsQ-ITgaGGK9Kk18caUTaAW8YfG0KmrfvPoBbFd3ryP6iVWoQ2AjCEg_NHlPQ7UIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PigiLJS3tceOAE3DoXacwga04OITeKwKV-SsjgdH5syKtI6kRs9VaxU2z2A6hUq2nMei9We1_Qs9Ovd3_PQa9Ak7yjLJeeaaQFXeuelRUcLdyFgdeBNuPgBiYkizlAan4a_Oa2OGawf5F8ulmvgcN92gy7c2hakxB7iR4ob_7suDKLIbv5QCFxfO1oCGxPQkT5G56RAclBYzZjg237UdIwm_4OG4h0R2H_zqviK2ehl-ZqfAu1dOo1X_OCl7ZTk0X18zYB4yTxGRcL7hNRovWtSbd7GR8Vt1PcqR5Lc7X7D0qENF906qPclTaYjICdiAZApEFluzInfCqWPHCLlgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sz0yzLKedBdAFKYekcW6oJtF3Elx0R2nCnyE5Y096tjYZBmvi79FW1i2McXEUYlebVOyBOOeUS-Bw2zJR6z-wUOVKn7_5_0YmvvqI9y1ZSt3byHTW0xr55nHGiuIU2lfnz2c0lZ7ePMplZrD_Uw1pDhqW8p9NP61KhCw3j2EzF99ythuKRQFd46XYJFuPFOFutd55yO96qhxbGcKlucFB-CB89txQWRl38A1rvN9ncXUj_AKW3qkf_RMxyQrJK2MsXx6QoiNTYQ--KEZRsExnlBUrSkAtWbJGMAzB-MHRsajcapmVYBbxj0lC-3wnXboDlWdVcvbjzQupMu1jisCBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طعنه گروه «حنظله» به رئیس اف‌بی‌آی درباره جایزه ۱۰ میلیون دلاری
🔹
گروه هکری «حنظله» با انتشار تصاویر هک‌شده از «کاش پاتل»، رئیس اف‌بی‌آی، ضمن به سخره گرفتن او، با لحنی کنایه‌آمیز خواستار پرداخت جایزه ۱۰ میلیون دلاری تعیین‌شده برای دستگیری اعضای این گروه شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/655027" target="_blank">📅 16:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655026">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY70U4RQtfTqSGaoeH3--bEUWgYdycXqKyKvNbVXq2aFCELJxIQ2QT3rZZyBQnorAvNmgjJfYrSHP4Kcs_rRlQ8s2cUxBMROIUVSxs4ijzsEBXnbToHBRhJAlbQ71gaFk4PAj0jxbWNOePnD7fJNj-wyZUY0DDKDZwrmrSjRYzOuYQJcyoyeITvwVteAEX2rBJQ86_YT0ND9D_tR-yfkNFuHHMdv5Tz5OTkepaGvABaeSjuenfmfPHH1GlCClU1g9Q0jMb6UbbWG3GPmzY1z9IaOr1PTdSDVG_PimV85rTHacboiTAMwTT4JGcNOgPCM-SkyTC04CzPfnjP_WQKHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با این پرامپت گزارش ارزیابی زیبایی‌شناسی چهره‌ات را دریافت کن
Create a clean, minimal, high-end facial aesthetic report based on the uploaded photo, using a black-on-white editorial design with thin linework, rounded cards, generous spacing, modern typography, and a refined luxury feel. Include an isolated front-facing image of the face, presented as an analytical attractiveness-assessment diagram. Provide an honest, objective evaluation of facial attractiveness potential, avoiding excessive flattery and focusing on symmetry, facial thirds, overall proportions, eye spacing and shape, nose harmony, lip proportions, jawline, chin, cheekbone structure, skin texture and tone, hairline, hairstyle, grooming, overall facial harmony, and photogenic potential. Assign clear, realistic scores to each major category, along with one overall attractiveness-potential score, keeping the ratings grounded, useful, and not artificially inflated. Include practical, achievable recommendations to improve attractiveness-potential, covering grooming, haircut, facial hair, skincare, eyebrow shaping, posture, weight loss, minor aesthetic procedures, styling, and photo presentation. Maintain a refined, direct, constructive tone that feels elegant, credible, and easy to understand, with an emphasis on actionable improvement that build on the subject's existing strengths.
All visible text in the final report must be written in fluent Persian, with correct right-to-left layout, accurate Persian typography, clean spacing, and no English text anywhere.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/655026" target="_blank">📅 16:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655025">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcee3d1a93.mp4?token=F8u5Q9hTGAVc1EZ7-r5DVk8mUVgohJgqsqVnATKpdTv25hncAhX2oCyBpNxmQaYxICVyDjiTGWtJ2bvOoZai5MIeb7eBnMXtFp9v_viUtAw3GxVZwXgfmo4CPqUbkT3zb_Kp4SXOxSWB4ECb_YZxgHM3eIW1qVrYHgN55FFHCffCn4Bv39gxdzzXVwq4x7jLuaYOvFgdTk--lTnEah-v7P8p87ivL2gUjYe2ooI0BS2RgCd8Rm388f5aORlcEyCdeO-WBc53BEz2eeP9g4XVsAAESdGsXtDUKotJvQPj8w8ANg3r_X__zBw5Z4W5VEDWkCyARw_Poa9mMJ_91Ed-6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcee3d1a93.mp4?token=F8u5Q9hTGAVc1EZ7-r5DVk8mUVgohJgqsqVnATKpdTv25hncAhX2oCyBpNxmQaYxICVyDjiTGWtJ2bvOoZai5MIeb7eBnMXtFp9v_viUtAw3GxVZwXgfmo4CPqUbkT3zb_Kp4SXOxSWB4ECb_YZxgHM3eIW1qVrYHgN55FFHCffCn4Bv39gxdzzXVwq4x7jLuaYOvFgdTk--lTnEah-v7P8p87ivL2gUjYe2ooI0BS2RgCd8Rm388f5aORlcEyCdeO-WBc53BEz2eeP9g4XVsAAESdGsXtDUKotJvQPj8w8ANg3r_X__zBw5Z4W5VEDWkCyARw_Poa9mMJ_91Ed-6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق یک پسر بچه بعد از وصل شدن اینترنت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/655025" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
نیویورک‌تایمز: ترامپ شرایط سخت‌تری را برای چارچوب صلح به ایران ارسال کرده است
نیویورک‌تایمز مدعی شد:
🔹
ترامپ عناصری از پیش‌نویس توافق را اصلاح کرده و آن را برای بررسی به تهران بازگردانده است.
🔹
او نگران بخش‌هایی از توافق احتمالی است که شامل آزادسازی دارایی‌های مسدود شده برای ایرانیان می‌شود.
🔹
ترامپ از مدت زمانی که طول کشیده تا ایران به پیشنهادات واشنگتن پاسخ دهد، ناامید شده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/655024" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاونت راهبردی رئیس جمهور: ۷۰٪ شرکت‌کنندگان در تجمعات شبانه زنان هستند
🔹
سی‌ان‌ان: ایران ۵۰ ورودی از ۶۹ ورودی تونل‌های تاسیسات هدف قرارگرفته موشکی را باز کرده است
🔹
ادعای نتانیاهو: من به ارتش اسرائیل دستور دادم تا دامنه عملیات در لبنان را گسترش دهد
🔹
وزیر‌خارجه فرانسه: بازگشایی تنگه هرمز اولویت است تا بیش از این هزینه جنگی غیرمرتبط را نپردازیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655023" target="_blank">📅 15:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ناتو: ممکن است در موضوع بازگشایی تنگه هرمز مداخله کنیم
رئیس کمیته نظامی ناتو:
🔹
کشورهای عضو ناتو در حال نزدیک کردن نیروهای خود در خلیج فارس هستند و در صورت فراهم شدن شرایط در مساله تنگه هرمز مداخله خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/655022" target="_blank">📅 15:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHggPFi59qF-Fa4lAAqzdUzGeMJ3EZ7_ZsCyD6ShPZmmrDW6d5Jf1EyCruINh4ftNOp6Rqj9mljVpqHTEsJqyNgbfbJc4vEQBmCmhudChCs2qoJNgwjiUj7X0U9Yyk4nVihZexrnvkoA4K-tNJdjFW3zZliJV70ii_tSo9MOoUbWqFuHzOn4WIfXlvZLN5Gy2hZAkdHj0L0VQKe0y6CGR2O6logVG3fRQFb7lV5M4Nu6cM4Whaq_4nnqFLzMkaym6o3THmGFLiOkAOkpmiSP7c2OkzEyYUKBUYXCkULDrkYVm6OBN7wfoLgVbUgKCfdSBhhbXQ4yML6R_FB-RxSatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس وایرال شده از استایل جدید صابر ابر در یک نمایشگاه هنری سوژه رسانه‌ها شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/655021" target="_blank">📅 15:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655020">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
گردش مالی نیم میلیارد دلاری کنسرت کانیه وست در استانبول
🔹
کنسرت کانیه وست در استانبول با حضور ۱۱۸ هزار نفر رکوردشکنی کرد. در صورت فرض حضور ۱۰۰ هزار گردشگر خارجی در این مراسم و میانگین هزینه ۵ هزار دلار برای هر نفر، این کنسرت می‌تواند حدود نیم میلیارد دلار گردش مالی ایجاد کرده باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655020" target="_blank">📅 15:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655019">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
قتل پدر توسط پسر نوجوان به خاطر بیکاری
🔹
مشاجره یک خانواده ارمنی در محله مجیدیه تهران به جنایت انجامید. پسر نوجوان پس از درگیری لفظی بر سر بیکاری و عدم توانایی در پیدا کردن شغل، با چند ضربه چاقو پدر سالخورده خود را به قتل رساند. متهم دستگیر شده و به جرم خود اعتراف کرده است. پرونده برای بررسی جزئیات بیشتر در دست تحقیق است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/655019" target="_blank">📅 15:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655018">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای فاکس‌نیوز درباره آخرین وضعیت مذاکرات ایران و آمریکا
فاکس‌نیوز مدعی شد:
🔹
بنابر گزارشات جدید، ترامپ شرایط توافق با ایران را سخت‌تر کرده و شروط جدیدی در موضوعات هسته‌ای و تنگه هرمز اضافه کرده است.
🔹
پاسخ تهران ممکن است چند روز طول بکشد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/655018" target="_blank">📅 15:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655017">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7106a3dc12.mp4?token=AZqffglLuC4q1EpLsUBcpXhuKA54C4wQZ7sMWuVl5PUqHTqqmGLFsLFJ6N9m52GAXKboBkozW5vzURF81IdtncfToY_3zHdm7AL_xjSbyAKPrgqs_mP_lCJQVpkl8K2Aneu3QpUGUdC9kgg1vjQymgU0L-ABUj0EoCU8mTQeDfUOITlTkcH6Tql37u7IDo32fKdyNT_7ObsW1ScaVqa_V6_wE9ujWLOfbQt8oIkzsvY89oudWO-H0VR3WtbXszpRUr-fPEIx344UxvgEihTT3eR_KwULJ6CEWs8R2PZQ6jbPzVsxv1WqdZi88VRbIw-78hk6A7fCQmpk20OWhDKLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7106a3dc12.mp4?token=AZqffglLuC4q1EpLsUBcpXhuKA54C4wQZ7sMWuVl5PUqHTqqmGLFsLFJ6N9m52GAXKboBkozW5vzURF81IdtncfToY_3zHdm7AL_xjSbyAKPrgqs_mP_lCJQVpkl8K2Aneu3QpUGUdC9kgg1vjQymgU0L-ABUj0EoCU8mTQeDfUOITlTkcH6Tql37u7IDo32fKdyNT_7ObsW1ScaVqa_V6_wE9ujWLOfbQt8oIkzsvY89oudWO-H0VR3WtbXszpRUr-fPEIx344UxvgEihTT3eR_KwULJ6CEWs8R2PZQ6jbPzVsxv1WqdZi88VRbIw-78hk6A7fCQmpk20OWhDKLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم امیرالمومنین(ع) مهیای عید غدیر می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/655017" target="_blank">📅 15:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655015">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 آیا شما از دخانیات (سیگار، قلیان، ویپ و...) استفاده می‌کنید؛ چگونه و به چه مقدار؟</h4>
<ul>
<li>✓ بله، به صورت مستمر و روزانه</li>
<li>✓ بله، به صورت تفننی و صرفاً در شرایط یا جمع‌های خاص</li>
<li>✓ در گذشته بله، اما در حال حاضر استفاده نمی‌کنم</li>
<li>✓ خیر؛ تا بحال هیچگونه مصرف دخانیات نداشته‌ام</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/655015" target="_blank">📅 14:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655014">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
توافق نهایی هنوز حاصل نشده و امکان منتفی شدن آن همچنان وجود دارد
تسنیم:
🔹
تبادل پیام‌ها میان ایران و آمریکا درباره متن تفاهم‌نامه احتمالی همچنان ادامه دارد و دو طرف به صورت متناوب اصلاحیه‌هایی را مطرح می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/655014" target="_blank">📅 14:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655012">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNGg8obo3mWw3sM-wJuJoWLbdMncSFvjhiCQVklhBmsQ8meC1WHOKE9kSg7BFONbzw3uv0AIhTcWuvVgkE2q0QYvOXbQkP7UxN8E3LXtGqfLY5HEE1Ob0thVxTvNyzg2pDY8aw-1GhFRVpWJ6N3uJubo4coHv3B0PnbTHbK0BY1mz04YKLR1dkBG8FZL2XwyCx64DBz5TDsbnet4lVlkJK-K2gBlsYVsNA_CLqthIR8TrumMoqWJYnfZrcsLhS7t5WZOLP-SqE3xFb3GKInwyooYZrXX8FjcKzLlm1O2aDZ2mHnGiIh5fMRGCL2SSkA6BymSC-5IZhp88CL5ykEFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6YJQNLvqoesdyccqqXUq2CddbVKQPj6eI2yKe--RHa07X2lOprt8JPx-dZ9cjcdEXVajVo7VcNvW97HfV7BN5QGKnqtD708cuJ3HOCqnwy8gdq2Z1GgB1rQLN-JkRS0zsUe6XA2_ha3GF8l7199mXo2-be5UcDHew-MPcAGaSmlSlAytKU_7uiNw5AYfV3Mz5i8o_rEw7lYvzXpImHXH1S2XC5uuoYfLfx9dzqyJrmSWNbgoxAefXnJoFkLEGG4BE0szqI9t-N4NkFi-fFObt4PCjoaO0DwCSwJ_qVE3zE0S8TCn2SA4wa0qCUDalj_VjPb8rXaB4_4wZ5VkRrNRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالیکوه، الیگودرز زیبا
🇮🇷
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655012" target="_blank">📅 14:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655011">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsdwggwXwfKVS4_K4okOPGZSIEnZueZP4VSdll8OKruupv602Ass9Al7GBVs_eO-NfPDOGqXwaJrYEENndEcXqyQ9Vsyt1l3EnWp6UMpJe0yh3uUTY_pwQ8lbYKQy4DQ6Ffd3UDjbOtAJm48tZQUdxY7Yf28QHf5rNXKVnoHKSnbOruGlTrXMKY9CAkfs-AMcdWyJluv3pDUpUXnD-xALI4cHnCt4Q8ajtpJn_W40Mx6lsnPrqJEs1Kov09_-puyQbMqfA5K_h3ai3TLev1Er2-fKCWXsA9Q3exo14mM67IjiCaPpCtnrEZrfrBIdW1ITqiPejQFB9gjYezRBOD2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیما، پیشران بانكداری دیجیتال/ بیش از یك میلیون فقره تسهیلات از طریق سكوی دیجیتال بانك ملت پرداخت شد
🔹
در کمتر از ۸ ماه پس از آغاز به کار دیما به عنوان سکوی بانکداری دیجیتال بانک ملت، تعداد تسهیلات خرد اعطایی از طریق این سکو به صورت کاملا غیرحضوری، با ثبت یک رکورد جدید از مرز یک میلیون فقره عبور کرد.
🔹
دیما که از مهرماه سال گذشته در دسترس مشتریان بانک ملت قرار گرفته است، امروز با بیش از دو میلیون و ۵۰۰ هزار کاربر، به یکی از موفق‌ترین نمونه‌های تحول دیجیتال در نظام بانکی کشور تبدیل شده و نقش مهمی در توسعه خدمات غیرحضوری بانک ملت ایفا می‌کند.
🔹
بر اساس آمارهای ثبت‌شده تاکنون، تعداد تسهیلات اعطایی از طریق دیما به بیش از یک میلیون فقره رسیده که این تسهیلات شامل طیف متنوعی از محصولات اعتباری و تأمین مالی خرد از جمله تسهیلات پلکانی (میکرولون)، تسهیلات مبتنی بر سپرده‌گذاری (نیک‌وام)، تسهیلات سازمانی(فرهنگ وام)، تسهیلات ویژه کادر درمان، تسهیلات حمایتی حفظ اشتغال بنگاه‌های تک‌نفره و اعتبار خرید «دیماپی» است که تمامی مراحل به‌صورت کاملاً غیرحضوری انجام می‌شود.
لینک عضویت در دیما</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/655011" target="_blank">📅 14:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32db4f3eed.mp4?token=vnSdepNxX707PdZnzJ17LkZbSVffg2GkWt3IWT250Ry6LaF1P6l9FKhqczbFWNHiHczMy3wj7IQYT0obkW38sbFkcCNV9vM0OtmgzNzpkEaisSk0Uz41A15f0VNsgKlliQMBzo1JXu6fE4oOJlInkxyo4oObdwpMlzfDDdKk97etTlSW3xLoree2R-m5_f_ROWqdVXSES-79qujpRxmyYyLV69W7jdWsP00cbRIvo7WbQz3NPrtOBQs_b_anjDik0V6BUyoqKiZwgamRCtsabh9gw3_bj-ftQ2mEbkfj24k6zZVudn_2WciNtgThb_psZTVUZ0Ifl9lc3DtsZ2hWNZV5CFDr_eW0kcvsdY7QGFiQ85-qYcb5O_hutldxritwsdPKGM24MWMiydWmWRQGmdmzB7M9Cvn8sWt1g0HkjQ1CXUEnQXooMSVJzD7GnDc93lVkf5HG8yOgiD_NyGtQxZEW5bj66HIItp0fxOgK2KtTie9tPGxSDO4LOQk3tZ2o-vxhz_Sj_pSoIu3OYWhOZIOQLeWWYsNaiS3BrnkQP5OVzfFK39xHPIqd8dv0PzhIqSuO1SY2i3_9L8IcQJyE3zCC2CzoDwexGVkEgAWrx-olBZUanfifp2tyzmvmQBJoje5S9fJ0nd5oxUrorCix7snrzxWPtYotM3rAi1OF4ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32db4f3eed.mp4?token=vnSdepNxX707PdZnzJ17LkZbSVffg2GkWt3IWT250Ry6LaF1P6l9FKhqczbFWNHiHczMy3wj7IQYT0obkW38sbFkcCNV9vM0OtmgzNzpkEaisSk0Uz41A15f0VNsgKlliQMBzo1JXu6fE4oOJlInkxyo4oObdwpMlzfDDdKk97etTlSW3xLoree2R-m5_f_ROWqdVXSES-79qujpRxmyYyLV69W7jdWsP00cbRIvo7WbQz3NPrtOBQs_b_anjDik0V6BUyoqKiZwgamRCtsabh9gw3_bj-ftQ2mEbkfj24k6zZVudn_2WciNtgThb_psZTVUZ0Ifl9lc3DtsZ2hWNZV5CFDr_eW0kcvsdY7QGFiQ85-qYcb5O_hutldxritwsdPKGM24MWMiydWmWRQGmdmzB7M9Cvn8sWt1g0HkjQ1CXUEnQXooMSVJzD7GnDc93lVkf5HG8yOgiD_NyGtQxZEW5bj66HIItp0fxOgK2KtTie9tPGxSDO4LOQk3tZ2o-vxhz_Sj_pSoIu3OYWhOZIOQLeWWYsNaiS3BrnkQP5OVzfFK39xHPIqd8dv0PzhIqSuO1SY2i3_9L8IcQJyE3zCC2CzoDwexGVkEgAWrx-olBZUanfifp2tyzmvmQBJoje5S9fJ0nd5oxUrorCix7snrzxWPtYotM3rAi1OF4ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو ناوگان صمود: در زمان بازداشت مورد تجاوز جنسی قرار گرفتم
جولیت لامونت، مستندساز استرالیایی و عضو ناوگان صمود:
🔹
در جریان توقیف و بازداشت توسط ارتش اسرائیل در ماه مه، وقتی دستبند و پابند داشته، داخل یک کانتینر تاریک توسط یک سرباز اسرائیلی مورد تجاوز جنسی قرار گرفته‌ام.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/655010" target="_blank">📅 14:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای آکسیوس: احتمال روشن شدن سرنوشت توافق ایران و آمریکا تا پایان هفته آینده
🔹
طبق گزارش آکسیوس، یک مقام ارشد در دولت دونالد ترامپ اعلام کرد که احتمال دارد تا پایان هفته آینده وضعیت توافق احتمالی میان آمریکا و ایران روشن شود و واشنگتن برای دریافت پاسخ تهران آماده صبر کردن است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655009" target="_blank">📅 14:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655008">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده جزیره قشم
🔹
صدای یک انفجار در محدوده شهرستان قشم از سوی چندین منبع محلی گزارش شده است.
🔹
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/655008" target="_blank">📅 14:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655007">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اسرائیل هیوم: آمریکا در حال بررسی سفر ترامپ به اسرائیل در ماه سپتامبر است
🔹
مقامات آگاه می‌گویند تا زمانی که جنگ با ایران ادامه دارد، این سفر مطرح نیست. مگر اینکه توافقی حاصل شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/655007" target="_blank">📅 14:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده جزیره قشم
🔹
صدای یک انفجار در محدوده شهرستان قشم از سوی چندین منبع محلی گزارش شده است.
🔹
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست./مهر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/655006" target="_blank">📅 14:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655005">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
وضعیت پاریس پس از جشن‌های قهرمانی PSG در لیگ قهرمانان اروپا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/655005" target="_blank">📅 14:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655004">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea2beb520.mp4?token=uXkyo4j0h5Df0CGwwAmpTcOli0KJaivjOR9OZHWLN2BaYEUmMp6tb8jIrjrcntlrNfiT3EWy80_oTtUjZ9YeH2ura44Fzhdb8eTKAOwcRHsLeWIZmfRhqVb_fME-bX3gSqvTD5AKGtgt6GaX4CEXWf3LpNNyt9PHvmmOGFtWS-5PycjuCtX-l0M8WLo_2Vo98jEcQ9BrUzfHibyuSQ8agUXBMijgq3IGA5N1VtP0BqPzmWphdg0VlM2S1ZSe-k_PlX2y0FCjYIjjr_tngoxIrHhGRUuuWJUfpDjj2Bjr4m78wfcMoMEjpT8au24niuGmyUGDHZL1I5Cn1-4ZFWT19ziZs52L5L0D5rbGsjXp-j5bKb_UzUAsc-YxVUj2wgpqIub2-80yNeAv6twR_0Q1Zt2un4ToFEg9H3zOTYG2iuRcnnB2kZu1oEqsZVGMnn7zL62uouOKegv-ZUqCqa70fc64MiCpBZ6yqG-n7h6K1Mtu-hj-27aQ-7PBU_cHXTjaPGVNK8rtB6P_zOd6xT5pSmeT3bGL1rmaFyDF1tVv2uHtKqhtq0yQx7aUsJKyNJQ77G3sqC1pbLbNxN65kwTS07jtnMiu6lanOeVtH1iDGaV8giLHjfVqvBIOyOyBVf5FkfPPZI7Imzm2EUg3-f0bmGvhZpfDevjIwlYXt7nuW4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea2beb520.mp4?token=uXkyo4j0h5Df0CGwwAmpTcOli0KJaivjOR9OZHWLN2BaYEUmMp6tb8jIrjrcntlrNfiT3EWy80_oTtUjZ9YeH2ura44Fzhdb8eTKAOwcRHsLeWIZmfRhqVb_fME-bX3gSqvTD5AKGtgt6GaX4CEXWf3LpNNyt9PHvmmOGFtWS-5PycjuCtX-l0M8WLo_2Vo98jEcQ9BrUzfHibyuSQ8agUXBMijgq3IGA5N1VtP0BqPzmWphdg0VlM2S1ZSe-k_PlX2y0FCjYIjjr_tngoxIrHhGRUuuWJUfpDjj2Bjr4m78wfcMoMEjpT8au24niuGmyUGDHZL1I5Cn1-4ZFWT19ziZs52L5L0D5rbGsjXp-j5bKb_UzUAsc-YxVUj2wgpqIub2-80yNeAv6twR_0Q1Zt2un4ToFEg9H3zOTYG2iuRcnnB2kZu1oEqsZVGMnn7zL62uouOKegv-ZUqCqa70fc64MiCpBZ6yqG-n7h6K1Mtu-hj-27aQ-7PBU_cHXTjaPGVNK8rtB6P_zOd6xT5pSmeT3bGL1rmaFyDF1tVv2uHtKqhtq0yQx7aUsJKyNJQ77G3sqC1pbLbNxN65kwTS07jtnMiu6lanOeVtH1iDGaV8giLHjfVqvBIOyOyBVf5FkfPPZI7Imzm2EUg3-f0bmGvhZpfDevjIwlYXt7nuW4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت سوم، فصل چهارم
🔹
میثم نثاری تجربه‌ای نزدیک به مرگ را روایت می‌کند که در آن با حال‌وهوایی معنوی و عاطفی روبه‌رو می‌شود. محور اصلی این تجربه، توجه ویژه به مفهوم پدر و جایگاه پررنگ او در لحظات بحرانی و معنوی زندگی است.
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: میثم نثاری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/655004" target="_blank">📅 14:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655003">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3974d5e6b9.mp4?token=FvZR5hwZA_fEP9Ouni3h9WrMGScbWApEGpOolhRr9QNP5hm2u2nS0lrSWLYPupcR0zE4rjVPTWZhFoG_F4r3SNZtL4u2yceOoVsahYYoDwGxEOrtbvGkc772uoclXQD4Ndb4mxe0lHjh4DxocoCK-a7VnjFZap5nFse0NFlTcGxHBt7RU4tDE5E1q8dAEli-PUlbdCQm1cu0FLVVCX4z8ldsE6zackJDCd_2UmVmgEsbYq8K3KqQZZJYCs6EP2BCiFBA5HCzh1-TnWaVOoSNsrNQoDbwtpNqAfAijbLN14kzr-TdOKblQhhbZNxdxJ7ZmAEpPQ7aB97DZu7QSr8MiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3974d5e6b9.mp4?token=FvZR5hwZA_fEP9Ouni3h9WrMGScbWApEGpOolhRr9QNP5hm2u2nS0lrSWLYPupcR0zE4rjVPTWZhFoG_F4r3SNZtL4u2yceOoVsahYYoDwGxEOrtbvGkc772uoclXQD4Ndb4mxe0lHjh4DxocoCK-a7VnjFZap5nFse0NFlTcGxHBt7RU4tDE5E1q8dAEli-PUlbdCQm1cu0FLVVCX4z8ldsE6zackJDCd_2UmVmgEsbYq8K3KqQZZJYCs6EP2BCiFBA5HCzh1-TnWaVOoSNsrNQoDbwtpNqAfAijbLN14kzr-TdOKblQhhbZNxdxJ7ZmAEpPQ7aB97DZu7QSr8MiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ما ارتش ایران رو تقریباً دست‌نخورده گذاشتیم؛ خیلی‌ها از شنیدن این موضوع تعجب می‌کنن!
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/655003" target="_blank">📅 14:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655002">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58003f3547.mp4?token=E4TEzg7ky5HBYZ-LcAcGhAIYak-u8hH4yqCJWJBEok6-niZlNNXpqAXRuLHQhM-WzSse8tEg-r64CvTf2XB0hlW1ps36_qGDURgY7eto06KSVAXX_GL42Y49u2PS4TO_wXQg8rTHsyID2xVdwl_wEzfDhejKSGXoPe7e1RHyjmz6e-2TRZKKgZnnfVyT8H1HPlvd5LsMA2ikoDKqSa_EI662T0Jsh4W2Sl52uFKN9NsW8oLi0IzEQb0uR6ghH70BzcRvoh6UEtdq59_zQJns8ii7KgM3VHEPTwI6MYjG9D78CQD5zEuMO5kSDtD-88lxv700_vYMQyIrVbtCCxAaOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58003f3547.mp4?token=E4TEzg7ky5HBYZ-LcAcGhAIYak-u8hH4yqCJWJBEok6-niZlNNXpqAXRuLHQhM-WzSse8tEg-r64CvTf2XB0hlW1ps36_qGDURgY7eto06KSVAXX_GL42Y49u2PS4TO_wXQg8rTHsyID2xVdwl_wEzfDhejKSGXoPe7e1RHyjmz6e-2TRZKKgZnnfVyT8H1HPlvd5LsMA2ikoDKqSa_EI662T0Jsh4W2Sl52uFKN9NsW8oLi0IzEQb0uR6ghH70BzcRvoh6UEtdq59_zQJns8ii7KgM3VHEPTwI6MYjG9D78CQD5zEuMO5kSDtD-88lxv700_vYMQyIrVbtCCxAaOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه‌ میلفورد ساوْند نیوزیلند در یک روز بارونی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/655002" target="_blank">📅 13:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vf1sVnkJ3XHUQB2wp6owt5EyRvJo7mCl41H6rm7yhs-wRjzlBzTDSG2LivfGa0oO8lDuCXCyV5CSrP8diQ0kN8enVd5556zZoK7fw3VSZffnkcigXC3gXHQ5hOmXhHuDtlsxT36if36Ms42cj9vfgBj8_sUkmPd5rN18OTi_i66Qwp6-Cvz7TujorWWGP7JzpBbM0rZNw7fckxLiH8Vx6f9EhpQvBiljqtZrF3PTj__whgF_93T2irArTp3V9Xcex5ReTNxBIhLTKW5fyegn2nj0d8D83_tPOxKg8YeNnViM3rrvDc44q2Mu3LDyzTPvrus5EY-L-V0VJDod9tR0pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۰ خرداد ۱۴۰۵؛ ساعت ۱۲:۳۰
🔹
دلار تحت‌تأثیر پالس‌های مذاکراتی در مدار نزولی قرار گرفته، اما بازار همچنان برای تعیین «کف قیمتی» دچار تردید است و معامله‌گران در موضع انتظارند.
🔹
در بازار طلا نیز هر گرم طلای ۱۸ عیار با قیمت ۱۷ میلیون و ۹۶۰ هزار تومان، در آستانه ورود به کانال ۱۸ میلیونی است؛ امروز سکه بهار آزادی با نرخ ۱۷۶ میلیون تومان معامله شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/655001" target="_blank">📅 13:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fdb5ba3d.mp4?token=BYBv3-MYJ5vllwwOPGUi1vhLwiua4etJQeL8SPYe8eX7IhNKQbMZ0tSlCGiebbdZq46MWDweaj2YaqLZhYE5PbYl17eg7MgPFPf6zIBfdMkPQ8sd66vfuRRofH0e_wehrnRsXP0A_deUgJj6adobLsdWtlFde6LLE3SYcJeourYJ8oqxU7TEr7U_ItDea-q85Hfa_eaorwg1rFz3vvlmVnOc-j8rL9EB9ESmi6Tccyl23JeRr3gaipvstldoPU-GQzCS3vZwhB117GxQZ5gJ6lQ5Lwl2OhC4-xCBVA3WsDuDXfRcWPTHKxmHGbiYM5fzXmNIsxYpbqztqeB4EPEsLkSK_6E2qGXwAb-UpFQs7Ttn1hHtmwP2f3DL7XhXURnQgwWknNG-PXJpA5WHrnV_1SV5npm4y3M2bEGmkHaNV7m23eKmZ0wLpeZTrZSaQfMkc7Os2Hu36Rd3A62jDFsPDADsqF0_XRe1bR8T8I1S7g7CUkNmP2Sd2uFifhO2iC-OB53xdkpWX6KVhYnnmr4R5POjaZ-BY-3Y1KWlPSikUnV5EX3h-7SsYhBMPFmtEHZgy2O2_xMGpvh0BfNCLRn0aOUbrBky_dN2vsUpYTgSSd41JRZQZqf8hIA1CK0pLear4qO07IL2RpzJRpfgUcT1PcNqXHqytHIl9-BeCTVfMx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fdb5ba3d.mp4?token=BYBv3-MYJ5vllwwOPGUi1vhLwiua4etJQeL8SPYe8eX7IhNKQbMZ0tSlCGiebbdZq46MWDweaj2YaqLZhYE5PbYl17eg7MgPFPf6zIBfdMkPQ8sd66vfuRRofH0e_wehrnRsXP0A_deUgJj6adobLsdWtlFde6LLE3SYcJeourYJ8oqxU7TEr7U_ItDea-q85Hfa_eaorwg1rFz3vvlmVnOc-j8rL9EB9ESmi6Tccyl23JeRr3gaipvstldoPU-GQzCS3vZwhB117GxQZ5gJ6lQ5Lwl2OhC4-xCBVA3WsDuDXfRcWPTHKxmHGbiYM5fzXmNIsxYpbqztqeB4EPEsLkSK_6E2qGXwAb-UpFQs7Ttn1hHtmwP2f3DL7XhXURnQgwWknNG-PXJpA5WHrnV_1SV5npm4y3M2bEGmkHaNV7m23eKmZ0wLpeZTrZSaQfMkc7Os2Hu36Rd3A62jDFsPDADsqF0_XRe1bR8T8I1S7g7CUkNmP2Sd2uFifhO2iC-OB53xdkpWX6KVhYnnmr4R5POjaZ-BY-3Y1KWlPSikUnV5EX3h-7SsYhBMPFmtEHZgy2O2_xMGpvh0BfNCLRn0aOUbrBky_dN2vsUpYTgSSd41JRZQZqf8hIA1CK0pLear4qO07IL2RpzJRpfgUcT1PcNqXHqytHIl9-BeCTVfMx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: اطمینان دارم که از این جنگ بزرگ با پیروزی خارج خواهیم شد
🔹
تا اطمینان پیدا نکنیم که حقوق ملت ایران را گرفته ایم، هیچ توافقی را تأیید نخواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/655000" target="_blank">📅 13:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWEHDTtcL7jCvQpccCH1M3Um1djkdCkfGFH6kQFXHdAlJuqSlGaAyXCEf-W1y-f0ZfMdaNVuQiq-diUxgk7TkNS0jKK2Wt5VdFS80oSL5liSQrqcd0b3unnZ9jYKAowbmHxHfJZr4bQf66ZzdZaSWGWVi9v4pf0LcvoTMg1vVFxUcVBefYcIzWZE7OXqtilNEDbekSi02i337IAoHh7YwPvNWb3sPnJ9QUlOn0UmtrJFkjReKLDMAAzKS-HuXouzi2aWJ5lOoxpCb_WlgSZmYQ45b9_NIebO8erHu-UaJW9EJ5FUEhCRWaVMtsPgYwjR4-Tc3TKCJ3Iv-eLrT7wGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی دولت: فعلا خبری از افزایش مبلغ کالابرگ نیست
مهاجرانی:
🔹
افزایش مبلغ کالابرگ از مطلوبات دولت است اما باید مطلوبات را با مقدورات هماهنگ کرد.
🔹
وقتی جریان عرضه و تقاضا دچار مشکل میشود بازار واکنش نشان میدهد.
🔹
نمیگوییم ورود محدود میشود اما دزدی دریایی آمریکا تاثیر میگذارد که ورود کمتر شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/654999" target="_blank">📅 13:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b0209531.mp4?token=XuuyUoRw3BXwm84yvJqvLN006WHMExy0F5JcaSMPZf6rvmItRohyTonCxvSBzAf45oDImcvd2QbjFWhlyuteV1g-Joh-U3zJrqfCHO2cvW2MSa6z4Jdd8btCLeeafSRMqU5yUOplGzR6cr-WQ2e1wneuVgT8UTiShA5-fH25I5-G88Ly9ZkToYtHhphGIBkqt3pxUwIVdV6Q0kjH2XrbaL_kin1UVZfubhS0uBs-4KFHwTWycDq0g1aCy4Qu1HaA4b6CctNKSKZGvSq8P1hMRjINrYM3_4cLc73WyiA_x2_pggIUd0lqND9zRVfQFaa55tVeCXfQvSftcKd0GaBlIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b0209531.mp4?token=XuuyUoRw3BXwm84yvJqvLN006WHMExy0F5JcaSMPZf6rvmItRohyTonCxvSBzAf45oDImcvd2QbjFWhlyuteV1g-Joh-U3zJrqfCHO2cvW2MSa6z4Jdd8btCLeeafSRMqU5yUOplGzR6cr-WQ2e1wneuVgT8UTiShA5-fH25I5-G88Ly9ZkToYtHhphGIBkqt3pxUwIVdV6Q0kjH2XrbaL_kin1UVZfubhS0uBs-4KFHwTWycDq0g1aCy4Qu1HaA4b6CctNKSKZGvSq8P1hMRjINrYM3_4cLc73WyiA_x2_pggIUd0lqND9zRVfQFaa55tVeCXfQvSftcKd0GaBlIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک بار اینطوری درستش کنید عاشق مزه‌اش میشین #آشپزی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/654998" target="_blank">📅 13:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5BadmHZnVt2CejXFasYym_CRO1B351Rt1r_UdLmSef4ll0Q8KObttSrLJaPzdzyf3qhkJ351xt-IHYCV8xQ3aTPitafQ9UsglZaUKcJHR88A2nVY_ZngutiF2ehW_bs7osXhlS8PNn8vwcLjUQXByg5RaHVYO2CO8A0iXIiFYNKK0maosk2tV91J5AWVRXiPMQnDnYVUc-27q9JxsHjlJtgJz72-d1V_pQ-Zymw1UWQP_p98mkcTaoFCJeCwlZEE-dFPdl1X5yx0lg15j-tQDV5jBMUjscIcyIf4KpZh0yHJh0A6f2tku6nwyJnNfW0Z-dJv_vaXJ_5zru_wA24og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۸۳ هزار واحدی شاخص بورس
🔹
شاخص کل بورس با رشد ۸۳ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۲۳۶ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/654997" target="_blank">📅 13:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
قالیباف: در حال عقب نشاندن دشمن در یک جنگ بزرگ و تاریخ‌ساز هستیم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/654996" target="_blank">📅 13:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654995">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899a9d430b.mp4?token=LU0ul4w3vBF0HK28gkPS_ze1uehvl36-Qzo4YoAomY1HShKmNOyAH__-fyrQ0OyC-zPQG1MmXQ1KrpSgZ_sh5sYcegxs-TotbaXokiniisnOgGeDTsop7-EXxJUE4qt-I96QWF0sTjVZHLm7gWrX2Wz-q-0gltqRRPB6umnDfRUk1iHkgNYSzdAQWHxYwEpr6jGFkA9nDu4NTZZeGG5ALnPKaUj21x7dfwzf87Dbajk1luH1vrgwxLoMJqcs_rfoCkhGKPA2dAc9mPUBAM8K4i420e_-N99qKMBgMMDJrGRnZwn3Sr657zAxzCz8rwHRe9rSvxi2iSNxcoIPsDmDcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899a9d430b.mp4?token=LU0ul4w3vBF0HK28gkPS_ze1uehvl36-Qzo4YoAomY1HShKmNOyAH__-fyrQ0OyC-zPQG1MmXQ1KrpSgZ_sh5sYcegxs-TotbaXokiniisnOgGeDTsop7-EXxJUE4qt-I96QWF0sTjVZHLm7gWrX2Wz-q-0gltqRRPB6umnDfRUk1iHkgNYSzdAQWHxYwEpr6jGFkA9nDu4NTZZeGG5ALnPKaUj21x7dfwzf87Dbajk1luH1vrgwxLoMJqcs_rfoCkhGKPA2dAc9mPUBAM8K4i420e_-N99qKMBgMMDJrGRnZwn3Sr657zAxzCz8rwHRe9rSvxi2iSNxcoIPsDmDcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: رهبر شهید جانفدای ایران شد
🔹
رهبر شهید، پایه‌گذار ایران قوی و مستقل شد. رهبر شهید به ما آموخت مقابل زورگویی با مشت‌های گره کرده تا آخرین قطرۀ‌ خون مبارزه کنیم.
🔹
رهبری که ما خود را جان‌فدایش می‌دانستیم، جانفدای ایران شد.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/654995" target="_blank">📅 13:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654994">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJc7EHgE4Q9PP15EC1Bf3PBlrzT3eBOwvs1cre-vnKF9qvXzutP55f1TyW5IEbOEB1zLvYw6qTe7zxIvR1Y7b1oyLHGHOIlP3ZkKaS1C_Nhq1F1Dno8XJtdn2uX2aEI2xs1yvFv0TgXZs0LcqSYpvMWYzDGBC20MD2hXY4P4oYXUnWOGo3_0dYfLiiZGSUWoQ7WELUOWjILt6smxR-m8Dz656lddlIashkzw4hZIiNfdT6CFlre4pnFokpWUsdrRK05z1zJkfmySloL-hHj7JRvpSEtmZueELz1fLuPjaA985Emrw5MJgKVrSl2w-eKYVvgCHTHmRau_VC3g0vWQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شوخی کاربران فضای مجازی با قهرمانی پیاپی پاری‌سن‌ژرمن و ناکامی امباپه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/654994" target="_blank">📅 13:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654993">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f30bf6366.mp4?token=YO0Wa2wxVpnuUzN2hyMfFaaptTQ9h2eAjpYjoyF_JIAy4cAZhndNNEDLnrBGDpGY0dK5_KfWYqlJ0dTnOna2ueg3Gp2LyO3sDTTo1avRKBQWBFu536G5CCp8pdciYQy1oZ9SMhHRlD3xsd4QxZChI0OFOujTU7niXyvwsqf6-CqhslFdFEgqvYxSpAuHGJzrowrWLZb9e2AligQ2mmlSugug8VZ4ycYpM0hIgQ74Fdi-CS5XH5Sd4KQrhDMZlVETt-CA00wSzHvQ7-mVxS5GACf7-ZOMMsRujEldl_uC-AyOJVmyQCjZ4dUzeMtyGfsfjdvf4DP0aZ-_zORkzdQVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f30bf6366.mp4?token=YO0Wa2wxVpnuUzN2hyMfFaaptTQ9h2eAjpYjoyF_JIAy4cAZhndNNEDLnrBGDpGY0dK5_KfWYqlJ0dTnOna2ueg3Gp2LyO3sDTTo1avRKBQWBFu536G5CCp8pdciYQy1oZ9SMhHRlD3xsd4QxZChI0OFOujTU7niXyvwsqf6-CqhslFdFEgqvYxSpAuHGJzrowrWLZb9e2AligQ2mmlSugug8VZ4ycYpM0hIgQ74Fdi-CS5XH5Sd4KQrhDMZlVETt-CA00wSzHvQ7-mVxS5GACf7-ZOMMsRujEldl_uC-AyOJVmyQCjZ4dUzeMtyGfsfjdvf4DP0aZ-_zORkzdQVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ما ارتش ایران رو تقریباً دست‌نخورده گذاشتیم؛ خیلی‌ها از شنیدن این موضوع تعجب می‌کنن!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/654993" target="_blank">📅 12:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654992">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32975f3b2.mp4?token=JqU5OlSzBdxQhsOru6ump3VjiGbto6sKccvl_IWAZZTUwpqr72pc9JNcWMNCgG1CloDe9CVNtc-aZBJbTr0kNkiC0DcPvb4aSpqO8Ioe76AgOZFybWe6xFuwVMuYe0AwP4MVoIZNcbq2XRXFqDdJZBQlTlKJBeqUwCdE2bptn2PI8hDDtHhDa4MBvXEUoDpeMwh6xSTX5yqroLylKlmGMnb7Q6RmqLwx7tTFLkivl9CcKh3L7_dC50kzVIPjQmome63one59Dk-VjGneS_koQGFEGQtJ93urB7itI8QWbbP5toGxebXz_vbLG1RuKMotMKTAb1T8dc7lp2NHCsv2RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32975f3b2.mp4?token=JqU5OlSzBdxQhsOru6ump3VjiGbto6sKccvl_IWAZZTUwpqr72pc9JNcWMNCgG1CloDe9CVNtc-aZBJbTr0kNkiC0DcPvb4aSpqO8Ioe76AgOZFybWe6xFuwVMuYe0AwP4MVoIZNcbq2XRXFqDdJZBQlTlKJBeqUwCdE2bptn2PI8hDDtHhDa4MBvXEUoDpeMwh6xSTX5yqroLylKlmGMnb7Q6RmqLwx7tTFLkivl9CcKh3L7_dC50kzVIPjQmome63one59Dk-VjGneS_koQGFEGQtJ93urB7itI8QWbbP5toGxebXz_vbLG1RuKMotMKTAb1T8dc7lp2NHCsv2RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: رهبر شهید جانفدای ایران شد
🔹
رهبر شهید، پایه‌گذار ایران قوی و مستقل شد. رهبر شهید به ما آموخت مقابل زورگویی با مشت‌های گره کرده تا آخرین قطرۀ‌ خون مبارزه کنیم.
🔹
رهبری که ما خود را جان‌فدایش می‌دانستیم، جانفدای ایران شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/654992" target="_blank">📅 12:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654991">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
قالیباف: پیام رهبر انقلاب را نقشۀ راه مجلس دوازدهم می‌دانیم
رئیس مجلس:
🔹
تلاش می‌کنیم اقدامات مجلس بر امیدآفرینی و آینده‌سازی از طریق ترسیم مسیر باثبات در اقتصاد و معیشت مردم تمرکز داشته باشد
🔹
ما به ایشان و مردم عزیز اعلام میکنیم که تلاش خواهیم ‌کرد اقدامات مجلس «نسبت مستقیم و مشهود» با مسائل اصلی کشور و نیازهای مردم داشته و بر «امیدآفرینی و آینده‌سازی» از طریق ترسیم مسیر باثبات برای اقتصاد و معیشت تمرکز داشته باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/654991" target="_blank">📅 12:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654990">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
هاآرتص: غنی‌سازی ایران دیگر موضوع اصلی طرح‌های توافق نیست
🔹
یک رسانه اسراییلی نوشت غنی سازی ایران دیگر موضوع اصلی طرح‌های توافق نیست و بازگشایی تنگه هرمز و ارائه غرامت به تهران موضوع اصلی آنها هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/654990" target="_blank">📅 12:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654989">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU8YUd9iu2smgpHJ_nqmetc3IJvwW3m2Aks1olDeD0kKNGnGKf-zJ3QYLV2fpvIKaubqWEhKMqD-J512gvotdPVlwvV4D6Beiw0UV_B6uzubtMGisWBCqgYKs63blP8pq6TXxN8WDvRx5GHTKZz_xz_cWecboLQCVu3sGjiljRpy8Y46M6W1Y9StCy7_Ws3zd1wORgyTgubwzf2VbSLUngZi9uGJTQvJ-n4r2D9GfgxBhHSbtCGx4oBlcBJ_ogUPXqv7vzfLhfQH-cL3BuGPcugn_Bv0wCVDMejd9LYstVlpTLNagcii-emZpz0brQ_U1Scn2H57vM0U0Frm4nayhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گران‌ترین سرمربی جام جهانی ۲۰۲۶ کیست؟
🔹
کارلو آنچلوتی با اختلاف، در صدر فهرست گران‌ترین سرمربیان حاضر در جام جهانی قرار گرفته است.
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/654989" target="_blank">📅 12:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654988">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn0k_JrsxeNjxWTbRG1tKDWNOzeNHR190YDLOs7skqx3q-7aGq2gtvJZCO2A0MJ2TQvQXUR0u_jEI6dH5SUECZmuwXltrXGY3RfsNa5pLHhpvKjHb5VlVzFvhX0mopZCON6aXS8Z2uWJaY7f4k3R3RyhE2Ko3ZscMOZCvKXPJTuRsDmOJlFIaWVpBvR5iT-S39MJ0Vdl41vCr31O6fdhjGKhudrK-YVlft4OCU4eidVjXRl-fBk-k93jkgpoLMAc0u04Zzjn5Me-Lh8swn-5x7jzuK96jGdM9BuHdBBQZ3No7Wfqa18PaoLHfWqTroo42ZobLqKoYXz8-Nj1pWZcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«ماه آبی» امشب به آسمان می‌آید
وبگاه سی‌اِن‌اِن:
🔹
هر دو تا سه سال یک‌بار، دومین ماه کامل در یک ماه طلوع می‌کند؛ این پدیده نادر که «ماه آبی» نامیده می‌شود، امشب، ۱۰ خرداد، به آسمان می‌آید.
🔹
چرخه ماه شامل هشت مرحله است و ۲۹ روز و نیم طول می‌کشد یعنی کمی کوتاه‌تر از طول یک ماه معمولی. به دلیل همین اختلاف، گاهی در طی یک ماه، ماه کامل دوبار دیده می‌شود. به دومین ماه کامل در یک ماه، ماه آبی می‌گویند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/654988" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654987">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
خبرهای داغ امروز و دیشب را از دست ندهید
🔹
انتشار جزئیات غیررسمی از یادداشت تفاهم ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3219059
🔹
تاریخ برگزاری کنکور سراسری و ارشد مشخص شد/ سهم سوابق تحصیلی و سهمیه جنگ زدگان
👇
khabarfoori.com/fa/tiny/news-3218868
🔹
ماجرای حضور رئیس‌جمهور با تی‌شرت آستین کوتاه در یک جلسه رسمی چیست؟
👇
khabarfoori.com/fa/tiny/news-3219063
🔹
عکس عجیب نابغه ایرانی که نفر اول جهان را شکست داد
👇
khabarfoori.com/fa/tiny/news-3218974
🔹
گنج پنهان در کشوی خانه‌ها؛ موبایل‌های قدیمی از معدن طلا ارزشمندترند | یک موبایل چقدر طلا دارد؟
👇
khabarfoori.com/fa/tiny/news-3218959
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/654987" target="_blank">📅 12:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654986">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXs8jGezckfij_Vw7Zt4jIyVcoegm77yhuhKuwnHQ_Jvmdid6wSwN96jSOWrBi1m4FOfJfXAN72OrtaCpR7SSzUebCPXDracu7bzdCAduhWryWnp5RyWHc9wR-wdZw4P3YoP5ZLDB20LqBryD3B6Qv6YxgyaZq-ZPuFpMqGKytSY1RhmVud9leqFGJpRXahdNsIQCUoH8ZTqVRl1t3UZT8O9ev-NBRc23Y3y5jdiqSLImpsXIdd9BbG7mCCrAkCgOdznjgvKax24G-siHg6gOOLdhGCwP96fIyPQa5KIgBt3FkzV1MQj1vBP8Oq48NkR7O-bMfztGTlEwClSWl0EyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پسر ترامپ به جنگ با ایران فرستاده می‌شود؟
🔹
برخی از کاربران با انتشار تصاویری از بارون ترامپ،‌ پسر کوچک ترامپ یک سوال مهم مطرح کردند و آن این که ترامپ و اعضای کابینه‌اش که مدام بر طبل جنگ می‌کوبند چرا فرزندان خود را به صحنه‌های جنگی اعزام نمی‌کنند؟
گزارشی درباره جنجال رسانه‌ای در آمریکا و مساله استخدام سرباز را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219028</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/654986" target="_blank">📅 12:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654985">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwK8RVtZKpjPSnMqNn3S4qx6Ir9Qlj4b-DWdISl2tcfwsW4qaxkAVQAdOHU8WLoCCLsygkUHKXILbwxWaOmPjVvjFMAdU4eCOAfIvQrTHlQlpZrn51y1LA0w2afbsMCPgzPOZPNlfXF9byMQ8B3kuUIBUjnKdaZViWS-YYXlPgsE-ULBbflp0VZCrNU1RDlsy9PtmSEtApMdqQbiRG4Jm5nhGpB7rgcKBfo9gf934NhxzX5ASOBm6TVXPBjCHbdIQU5zmbZi5_obQU-dqVV7ide2JoHrKZrvCRbvgC7O0-R51-y12Fcpuwj05HlgGvnxoI1pzy2iBS9hYTCz1qwnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دخانیات؛ تهدیدی برای سلامت فردا
🔹
۳۱ می، روز جهانی بدون دخانیات، یادآور این حقیقت است که بسیاری از بیماری‌ها و مرگ‌های زودرس با یک انتخاب قابل پیشگیری هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/654985" target="_blank">📅 12:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654984">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e9502b75.mp4?token=j8qShYYGwpstYPRCMc9QjEayZn2GVxTXvwejsFeCmLRNz1IVGABp0sQnvw6I0K1viJZ1rl1fdzBbU-ag-7qaBW1w0DwAgLWdPjh6grJ51cuQnWkcYeY-zC7oawrkkSMzRcP4eTynJWhbZtydwEth_MFoPemSIlOo8r1z0VWKe-f3zazNcSiNtrT3KN4XzL7f6MnN9rPVRH2VFHxqBR-3wPimooQiVwjKElITX21wxTJvw74dqkHgmHJzsz8DUzabK6jdVpQ8Wm8uhCkH_aQOm0PAFe7xWS1G5yEWUHMDaD5BD4Dzy0ryOPDPzq468-L8EL6EOZTKD6gheCpl5As0TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e9502b75.mp4?token=j8qShYYGwpstYPRCMc9QjEayZn2GVxTXvwejsFeCmLRNz1IVGABp0sQnvw6I0K1viJZ1rl1fdzBbU-ag-7qaBW1w0DwAgLWdPjh6grJ51cuQnWkcYeY-zC7oawrkkSMzRcP4eTynJWhbZtydwEth_MFoPemSIlOo8r1z0VWKe-f3zazNcSiNtrT3KN4XzL7f6MnN9rPVRH2VFHxqBR-3wPimooQiVwjKElITX21wxTJvw74dqkHgmHJzsz8DUzabK6jdVpQ8Wm8uhCkH_aQOm0PAFe7xWS1G5yEWUHMDaD5BD4Dzy0ryOPDPzq468-L8EL6EOZTKD6gheCpl5As0TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش صهیونیست‌ها به مسجدالاقصی
🔹
شهرک‌نشینان صهیونیست با حمایت پلیس اشغالگر صبح امروز به مسجد الاقصی یورش برده و اقدام به خواندن سرودهای یهودی، اجرای مراسم تلمودی و هتک حرمت به این مکان مقدس کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/654984" target="_blank">📅 12:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654983">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سخنگوی صنعت آب: اگر شهروندان ۱۰ تا ۱۵ درصد دیگر از مصرف خود بکاهند، امکان «عبور از فصل گرم سال بدون بروز مشکلات جدی در تامین آب» فراهم می‌شود
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/654983" target="_blank">📅 12:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654982">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBLV8KZUfaIwvl9StPj-_FNHyW-1iVaaUdCFMzEqWXVQ7SJRGDD-FoWhfKkJwjj1uLANeY66t-2g5qJYO3pRLQjy-r9rmsKDDhL8NOjiw7aexCpRuU84rO8tlYZABro3Fwis9dEIvE8dRyC1qvHywMZE_DbGU8xZjPAY13uiLHPUTstRA1DUx8fYiQihT1JLEF29LiGh5KEizNuJys6rpwWSe4YqBMXbt0OBzaVYWfBKYQSlC_HhEnjHxuKm8mxLZ2iIQ0zZmTIUacPeAsWkMstpCbV_q5aLgLszTtgiSTE7Mtl2XJBz1TjbNkPrmiUqp74HSqUpYLY0VNxj_KW69Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سواد رسانه‌ای؛ مهارتی که جلوی فریب، شایعه و اخبار جعلی را می‌گیرد
🔹
قبل از انتشار: مکث کن، منبع را چک کن، بعد تصمیم بگیر. #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/654982" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654981">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
عبور ۲۸ کشتی از تنگه هرمز با هماهنگی سپاه طی شبانه روز
گذشته
نیروی دریایی سپاه:
🔹
طی شبانه روز گذشته ۲۸ فروند کشتی اعم از نفتکش، کانتینر بر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/654981" target="_blank">📅 11:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654980">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWJTrbhRALljhgh8Ns4A5RHZXwVhD-YXSz5A7wIHfGIa5gpwSLyWRxjcyMpaLug6fM5utTuiedNseHUgIiaIGzsNhRdy31H1c3uVBzLwPGGUfejidEKp1BK88KGUerc_k3x1nK4oEiinxpH1YV7YViXfy1ptmrZb2wxsSvYQSTX5BYD8btHSNqWGy8Ef88FE322RlDK4MqIJcdVaeL4GgoS13tC8x5-zpKVDi-2Dd4b7TE1lTZZqDMXEnpJYU_QN3WTnz8rvVkref-_6l-1ndj-yOdsogtDXHKRnDq9eJa6p-t_22fKtyM7-Qh3c2XMuj9HhnHMcQPtrC39_X76MHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تولد نوزاد دو سر در بغداد؛ پزشکان از «مورد نادر» خبر دادند
🔹
یک نوزاد با دو سر در بیمارستان «الیرموک» بغداد متولد شد. این نوع تولد که در پزشکی معمولاً در دسته «دوقلوهای به‌هم‌چسبیده» (Conjoined twins) قرار می‌گیرد، از رخدادهای بسیار نادر به شمار می‌آید و برخی برآوردها احتمال آن را حدود یک مورد در هر ۱۰۰ هزار بارداری عنوان می‌کنند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/654980" target="_blank">📅 11:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654979">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73fbb9da9.mp4?token=ELxLlpVWlNaPhohpLnR4uoc8ihqzRT1EFYUiW2FpdI6NEd_dRV1DrFCKawaCCnCQkVTgKRibCU4zPDW_Mz61oQxxbJe3qzout7-YIJL37qzDL4lUhYs2rGS26zuSfBjUN3-eLBYS8V-kM46QYruy8QiwVonWkUq3zji3UId6luPd9WPFyVwwuRyNzt4aFjlF4lmu5jNjVgJv1Q889SzQveCfEOecF2z0V-73MX9jEbnJehKS8KqKvvDO1HncunxYrU6KmOza9VdgYBN_h59MxL3w3Abr5Yzu_MO0Q6zY_bHRW_Cn2V2hsJRlcI1Yz9xh6uDWHEPByoDteMwXYH1Xxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73fbb9da9.mp4?token=ELxLlpVWlNaPhohpLnR4uoc8ihqzRT1EFYUiW2FpdI6NEd_dRV1DrFCKawaCCnCQkVTgKRibCU4zPDW_Mz61oQxxbJe3qzout7-YIJL37qzDL4lUhYs2rGS26zuSfBjUN3-eLBYS8V-kM46QYruy8QiwVonWkUq3zji3UId6luPd9WPFyVwwuRyNzt4aFjlF4lmu5jNjVgJv1Q889SzQveCfEOecF2z0V-73MX9jEbnJehKS8KqKvvDO1HncunxYrU6KmOza9VdgYBN_h59MxL3w3Abr5Yzu_MO0Q6zY_bHRW_Cn2V2hsJRlcI1Yz9xh6uDWHEPByoDteMwXYH1Xxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مری ترامپ: دموکرات‌ها باید ترامپ و نزدیکانش را پاسخگو کنند
برادرزاده ترامپ:
🔹
دونالد ترامپ و نزدیکانش سال‌ها از پاسخگویی درباره تخلفات احتمالی مالی مصون مانده‌اند و این روند باید پایان یابد. در صورت تسلط دموکرات‌ها بر کنگره، باید زمینه رسیدگی قانونی و پاسخگویی ترامپ و اطرافیانش فراهم شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/654979" target="_blank">📅 11:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654978">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFkfLZhQsZwKOdDtFT0Kgmfbs0leemDlaNWkBkzzmKltwzwU2yGSNBfECyiCKEUK7pCF_fjhBetbV_H2JsFYN9vwLNuQM7tF8vccKSb1WYrw9k_micV9k7kFfe12SFW7-ibIlgXZ04qJPHsVEeWFNvOuY_tnIJKwaYhLuraBKNinuyWZ-2FaxcAOTJTgNfmyOJSR7U60pkholTHuvoJGtSpVvKUsErM20BgDyA6u0nx-bxFodIvEfYTCsGmoTvjM0yH4IHd2ImGFQgmiqmvRwOpQZ3tkmRTQh312Xfi8_eKGMyH-rAPk2OgkY1Nbtc34sNCaRam1xXxxM-UyoqSuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممنوعیت استفاده از شبکه‌های اجتماعی توسط کدام کشورها اجرایی می‌شود؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/654978" target="_blank">📅 11:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654977">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sixbrMny4kr7Vr6uj6IhtW2fiiJkpxMgUCShV_Zusoh3aMeWD4ywj7iAPCaTNT6q9Sic6DOxFSb-RE6IDgODZRHdhZSujChKxrFa9lUX-ZrE3rSGW7h4k4GWOjdDCyxT_-DVFuralUXm8zntdn-CX9aJFz0j5q5RdvfCii2q3ig6JWVz8vDm-o64xmMm5UwmnH5cYGxSpyttymv75jK0t7H3muvJ-R4gjtszcBRaBpPRFI3TVmS_uzu-SaEtvwgLzEHtVCXUMwV8Mz3lGMqKEWumeM1oNDPEU-EB71Qq2Hm7p5OExJBnbEA1IiFVSS_G7OHWFqkJ0CT15cJldvbCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد سناتور وارن برای پیروزی انتخاباتی دموکرات‌ها: به جنگ ایران پایان دهید
الیزابت وارن، سناتور دموکرات با اشاره به انتخابات میان دوره ای ۲۰۲۶ کنگره و ۲۰۲۸ ریاست جمهوری:
🔹
اگر می‌خواهیم در سال‌های ۲۰۲۶ و ۲۰۲۸ پیروز شویم، دموکرات‌ها باید تلاش های بزرگی کنند.
🔹
هزینه‌ها را کاهش دهید.
🔹
به فساد پایان دهید.
🔹
به جنگ در ایران پایان دهید.
🔹
زندگی را برای آمریکایی‌های کارگر آسان‌تر کنید.
🔹
دیگر دست دست کردن بس است.
🔹
وقت آن است که جدی باشیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/654977" target="_blank">📅 11:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654976">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
یسرائیل هیوم:
ده‌ها کشتی حامل نفت و گاز با مجوز ایران از تنگه هرمز عبور کردند
🔹
منابع دیپلماتیک و اطلاعاتی به وبسایت اسرائیلی «یسرائیل هیوم» اعلام کردند ده‌ها نفتکش و کشتی ویژه حمل گاز مایع، طی هفته گذشته با دریافت مجوز از سپاه ایران از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/654976" target="_blank">📅 11:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlvGo7h7WgOumx2GF543KCmTBMXmkMWYiqxWg5DWHcDx5erRK6SrGHBVxLJv7ydrD9dtE3ip77dIDyJdpuUtWUeNtdvrcaU5DtK9OZ0dbTHZ5q_KZ2a1OXzmN2eBqjFto9ozCZaRx4VOFKtu2fcICA55RzWYPqpNbYLG_Qh-yS872u8Fsb_4eo4gM46HzNVd8RNJmo-LAumC3Nao3vIC_-W6u4_2tQxe1avhmRLf1N88NcXcaSbrYiP4TssrK7GO3wkwboSEaedzyQn6uZKPZ-8YQ3LJ8O4HTVCh9z4d8ThMca1hIEBxVqqE1m1uU4Zj7K4Mq1A8mWiGm6TaAbPnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sM_t3FxNwdBPbqtvW9fJaQJ0xZ0LHJ_3I6pKglV8f9Za7nqIJtYflX4N6y32ks2Rdol9m4mTeEf8wRkMjWhhnx8Ar0itpZVeIsNQu_jICI1vDAnUKj6MABhmcyzwIYQB57n-lqz4RmqwgoGi1Gkr4v9qGd6CnuAn0rKYgWTXluaiwdJLBuVLwDBro4LcyBY7okptzVYtmL8Idnqx12Ai063roEnwGck5lCcBT2ISu84qrpZWgLFM03NEyxFlf0rnBPcNFLOEPwnMGiyY62YldvXtYhxT5As0C53YgJya5NnjOc17w6ks0Mde-p9deUkJI3k2KJHApXXb2r7LqXgJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xbv3gAY5Ay1OB-5EUwUnWMpBN1I47H6a1e6Ds1J3M0FScNYi2ULWvGV_yBgqeAfWaXbl4FY9rSw9qiNS17yC7ojar7NPJzvJgz44Ze2hGfUxVwheVxnVudiIN3NCWZ9gty6bzX3Hu_C7s0bRBYqTbEQlMP-zSLaoBZ9TfcqyJu5N70OEhoy61hjzmdXjTz35K7Cg7nWP9ZuDI6jErlC2eQi2nirmJ1OlmXxMrzN9yEaVzUCnyX96jUtdeV0zWWqbXEFfbwy5LnzJSRF24EV3rFxZ0_je5iXvDJq1JrOn_PXUbzeNLdZZ5heZJ3fjN66RirP8fm6yg3-Qk6B_pJnbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRCBrhT_9t3xHqW7wipT2S95wJf8mT7mgK6OOPmKVUL_dSFMDqXLPh_bffk7gjGlCro6l-n_pnFftgQxS6yFtYqFshjESmMqzVvL6m5y6h5gQeua-EYsslTboNfZuOkBYePvxrABrniG5O0M2aofMHOyZSfzbDCCWWOeRszGZ4LjYMV32Mu1Qa9vlznCwFf_ZO30P5CONJ7vj_WwbRZWL8ABTkZkpW8QMgW0S08Zq0s0pZedy4KYzy6CEK9blmC5u-Y0uY_zOjvVh9ocTqFE6fX4-6dCXMFlA920PEUBF2K2E4FXYzoKDlyg3fQU3b0GAifkGUDUiiiFC69r2Kkslw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بابونه‌های فندقلو، اردبیل
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/654968" target="_blank">📅 11:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
سخنگوی وزارت آموزش‌وپرورش: شیر مدرسه  به شرط حضوری بودن مدارس در سال تحصیلی ۱۴۰۶ـ۱۴۰۵ توزیع می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/654967" target="_blank">📅 11:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromصبانت | Sabanet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2te1pgIFWG0dfBTCu9o98u_MVCzHieuXhCXdSFSn_yJplhqTR9zMROeVx-WS6KUMifC2VRIaBm7422w1fFcNUpCqmrhyRBumyHk1xo0gnrpdwnCY3nHxP_AG9lGjN6D_9nL9YtcNVQ0TNtAVWzuiH-xtk85qC8G2lE1eKMwk-1TS39QqpVwW4HXgvgzHz83nvQW1MGcupU3_uUmvi_uQ0uBt34bABrbRpVDNGVJtfeLFJFj2sU0ZFGhbHZB2JYey0vDzErKMhnbRhnwK_fakz3bRx8FCsKEhVpIGRlGP3Elm9vwikTOC7gCH4kKrBLFdVNwfbCjnGZfZ1s2SOzRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اتصال به اینترنت بین‌الملل فعال شد
💥
با
اینترنت پرسرعت صبانت
، دوباره به سرویس‌ها و سایت‌های بین‌المللی دسترسی داشته باش؛
از دورکاری و جلسات آنلاین تا وب‌گردی، آموزش و سرگرمی
⚡
✅
فعال‌سازی و خرید کاملاً آنلاین
✅
نصب و راه اندازی تخصصی
✅
شروع سرویس در کمترین زمان
✅
پوشش گسترده
✅
پشتیبانی ۲۴ ساعته
خرید و فعالسازی:
👇
☎️
۱۵۲۴ داخلی ۱
🌐
وب‌سایت:
sabanet.ir
📲
اپلیکیشن:
sabanet.ir/app
💻
پنل کاربری:
ecare.sabanet.ir
لینک بله:
https://zaya.io/Sabanet_ble</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/654966" target="_blank">📅 11:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654964">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiWy6RNlcjcbqMmwXbC1mSzp8goEuxtTV1B5190geBQU1Rp5Rcj6LGklEgWPD674Ym6haRwHYBV_MVMgmYk7axCYGE3CILZTL2PhxMYJLmiCizPk6AQh08U89hvPGb_HcygMUKpM5kKm8kY4Mj1kToraEk7fbEF4MnlGKvRJ-oSgNg48NPDkZpuM2ob9BdfUBi0GAg6ozfDHKrUhp5JJRFIXOlMSM2Tz7AOC7SMKXWuyj5l8-4xV_U0hSeoHd-renPUJ1CpInqh6RfOFQRkUeYq_rKviD04ySB1yXDYOvqLZOuLujYN5V1lN4ULfTjnsniKUNftb5olmWaEKxFNa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شناسایی دو ماده مخدر جدید؛ غبار میمون و کروکودیل
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/654964" target="_blank">📅 11:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654963">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
شرایط دریافت کمک‌هزینه بارداری و مرخصی زایمان اعلام شد
🔹
بیمه‌شدگان زن در صورت ارائه مدارک لازم و عدم اشتغال در دوران مرخصی، می‌توانند از غرامت دستمزد ایام بارداری و زایمان بهره‌مند شوند.
🔹
پرداخت این کمک‌هزینه منوط به داشتن حداقل ۶۰ روز سابقه پرداخت حق‌بیمه در یک سال منتهی به زایمان است.
🔹
مبلغ کمک‌هزینه معادل دو سوم آخرین حقوق بیمه‌شده بوده و بر اساس میانگین دستمزد ۹۰ روز پایانی پیش از شروع مرخصی محاسبه می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/654963" target="_blank">📅 11:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654962">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
وداع میلیونی با مردگان/ قیمت خاکسپاری در تهران ۴۰ تا ۵۰ درصدی افزایش یافت/ مرده‌ها هم از گرانی و تورم در امان نماندند
🔹
طبق مصوبه جدید نرخ بهای خدمات در بهشت‌زهرا هزینه انتقال هر متوفی از سطح شهر تهران تا شعاع ۱۰ کیلومتری به ۹ میلیون و ۷۵۰ هزار ریال رسیده و افزایشی ۵۰ درصدی داشته است. نرخ حمل به پزشکی قانونی کهریزک هم از قاعده افزایش مستثنی نشده و به ازای هر کیلومتر اضافه افزایش یافته و خدمات آمبولانس خصوصی بیشترین رشد تعرفه را تجربه کرده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/654962" target="_blank">📅 11:00 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

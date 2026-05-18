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
<img src="https://cdn4.telesco.pe/file/BH5E-dUd-WW-7ytskn_GF3xtuhInPFbmfSyRK71mnm8TjkcVVxTYhhtxF4aNjGRAqbhaRdOZPmbO6enerQDrqgdWmBePPvQY3HZhgdDBUX8jtwXu3BhVbCXlQf34zQsHnF4haykmaNrPDaW8hST-1lx1SRt1IGEfQHMbEQwXxzDkiA8MkAbRUKLNxdxXuTo8erI5VbsMqWIRz1dIsR62Ny0Ud3HOwpfL30aqA-bfjbABa9xR-_EzzZRWL80ovIU4_vPl033mpG3VLfcgwxjNEDBcIcbTDBRHxexhzVwi2oPSR9aasAuXGUtUNNanS7r_gVATz8tOOZaL58CdwMaYXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.02M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 21:57:14</div>
<hr>

<div class="tg-post" id="msg-652905">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل: اسرائیل پیام‌هایی از آمریکا دریافت کرده است که حاکی از آن است که ده‌ها هواپیمای سوخت‌رسان آمریکایی که در حال حاضر در فرودگاه بن‌گوریون مستقر هستند، انتظار می‌رود حداقل تا پایان سال در آنجا باقی بمانند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/652905" target="_blank">📅 21:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652904">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391adcbf76.mp4?token=rbbiNbhHoIYv-YTs-DcrNg2m0TnZju-vfsS-wQXMHkbFYuDUK0_rnjtYixMuF2_9daEFrr-MlhW3MtMVyl5HXD9HvcPkQBtgnbnEUckzo__rLOneQG8sVRJ2paJdI6Jo319Lasq9Y9VZhufv99QoRRbLsPCLhviKYDBrwlktQva8TPvJSNsjFcObzw_qlF9qgocSmGysny9s-ExZUijyKjhB_6lFmu8ia4HujMOTXWReZ4ps9Sa7scbM3RHsj19Ps4UTueKuzuSp8lfYVdwj2_Ey5NvIwu8TwzLGB2Qjb6Oe-igloMyQNeRVrdI99joanBKFjB9RuNFLPck2Ob_pMhOT_OrC7qG_Lwfl2h6ccrJbCYvdVWh71mF6-pJdVjWbmXlPNTdEuvko_HBjDxP_nKOvnXYLnIy_2OWHLat03ayO6L4O5uhaDtdZCv4WPUAqCMkjfVoSVJHqOKbwlGz7pqzg1JUysnDcq1ivdXGqVg9PEYdnYj4BD0G1xd75Oa1dOvfug45jebS2DqOdfXMXTRKKmITuY3H0QlylVUoYlM-j1XDWJIQwpDh3be1jT0L-KAsUODonF1VqRNT4iEyMzPiyPCZIsJ8LY6-uTEvgOJX6bqqJIVgyRt0We7oYMfP2vj-801T00Nx-bgKJ3rVrM1ri_M1p9Kceds7VsQTZqe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391adcbf76.mp4?token=rbbiNbhHoIYv-YTs-DcrNg2m0TnZju-vfsS-wQXMHkbFYuDUK0_rnjtYixMuF2_9daEFrr-MlhW3MtMVyl5HXD9HvcPkQBtgnbnEUckzo__rLOneQG8sVRJ2paJdI6Jo319Lasq9Y9VZhufv99QoRRbLsPCLhviKYDBrwlktQva8TPvJSNsjFcObzw_qlF9qgocSmGysny9s-ExZUijyKjhB_6lFmu8ia4HujMOTXWReZ4ps9Sa7scbM3RHsj19Ps4UTueKuzuSp8lfYVdwj2_Ey5NvIwu8TwzLGB2Qjb6Oe-igloMyQNeRVrdI99joanBKFjB9RuNFLPck2Ob_pMhOT_OrC7qG_Lwfl2h6ccrJbCYvdVWh71mF6-pJdVjWbmXlPNTdEuvko_HBjDxP_nKOvnXYLnIy_2OWHLat03ayO6L4O5uhaDtdZCv4WPUAqCMkjfVoSVJHqOKbwlGz7pqzg1JUysnDcq1ivdXGqVg9PEYdnYj4BD0G1xd75Oa1dOvfug45jebS2DqOdfXMXTRKKmITuY3H0QlylVUoYlM-j1XDWJIQwpDh3be1jT0L-KAsUODonF1VqRNT4iEyMzPiyPCZIsJ8LY6-uTEvgOJX6bqqJIVgyRt0We7oYMfP2vj-801T00Nx-bgKJ3rVrM1ri_M1p9Kceds7VsQTZqe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ، ترور، تحریم، محاصره، آیا گزینه دیگری هم روی میز آمریکایی‌ها باقی مانده است؟
🔹
وقتی آمریکا با کارت‌های سوخته‌اش بازی می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/akhbarefori/652904" target="_blank">📅 21:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652903">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkK9ousmcllm39yrGCcxka3WSOqZYaoEc-HjS8L02xpJSQXip5uriPwNFJRNZtXIfJwhbVmc3gVChX0glQVFK2ecy5lMNZB1Rdyzz6WFWTwp6LLKL2KEYlB_akVc2izbphU8Oewg0nNhgaH5LDu6BpKPMRB1bk33ByKNNy7Tl5u2igKP-ph_IlAVe9RwedqmKLW1TbSDzOPBW-gvAxHiiedS9ZfMY6t9ypFvCLvsdtuwK2mLIBusmOs7C_96ONTxmkjelAd5KjE7075svqg9LnMJdTh5ArO1eOjw5rizmauiC0cjd5SQtFq7iAoC8mFJ93CaxtWh391TNPXO0KkV-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از روز رئیس‌جمهور شدن ترامپ کدام بازارها سود‌ده‌تر شدند؟
🔹
از زمان تحلیف ترامپ در ژانویه ۲۰۲۴، نقره با رشد ۱۵۰٪ پربازده‌ترین دارایی بوده و طلا با ۶۸٪ در رتبه دوم قرار دارد.
🔹
شاخص‌های سهام آمریکا (نزدک، S&P ۵۰۰ و راسل ۲۰۰۰) نیز رشد مثبت اما تک‌ رقمی تا ۳۳ درصدی ثبت کرده‌اند. در مقابل، بیت‌ کوین با افت ۲۴٪ تنها بازار زیان‌ده این دوره بوده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/akhbarefori/652903" target="_blank">📅 21:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652902">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
رئیس‌جمهور ترکیه، حمله رژیم صهیونیستی به ناوگان صمود را محکوم کرد
🔹
اردوغان: امروز بار دیگر شاهد بودیم که چگونه اسرائیل با ذهنیتی فاشیستی اداره می‌شود. نیروهای اسرائیلی به ناوگان جهانی صمود که حامل کمک‌های بشردوستانه به غزه بود، در آب‌های بین‌المللی حمله کردند. من این عمل دزدی دریایی و راهزنی علیه مسافران ناوگان که از شهروندان چهل کشور مختلف تشکیل شده‌اند را قویاً محکوم می‌کنم. امروز بار دیگر تأکید می‌کنم که ترکیه در کنار مردم غزه و کسانی است که دست یاری به سوی غزه دراز کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/akhbarefori/652902" target="_blank">📅 21:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652901">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuuhQH-t1U4rIjWQXqY3IZQRW-3OWlYsjDuRKIjJsimCIp0ZMwGTrPpU4ZZISSZNPqsxgKva7559_x9XhFUJw5GJsIP8BmKc-m0RbHAoZbJK90W7_jM9clRgFemt8qPw5fqVKLKS47kdT7_uq-6cXnSQpsUzRt_8n8j0BVoTW7k2NBiMqurgy7x1X0GwrNJvU6kUXHXVHgoX-jfLapQuF3QI706mJMbN9TH6Q54DvAHdyyklv_pMQGbFM3ZGYggKbSDWuooH-04aB77nzp3UNjXLJ_y_oUvxF_oY6cYHO2v41rK73poSP0lm1WdQ_ybsCw_93O1nFjjJrkX4iAZykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت نیویورک تایمز از «دو پایگاه مخفی اسرائیل که ماه‌ها در صحرای عراق پنهان مانده بود»
🔹
اسرائیل بیش از یک سال را صرف آماده‌سازی دو سایت مخفی در عراق برای عملیات خود علیه ایران کرد.
🔹
وجود این پایگاه‌ها سؤالات سختی را برای عراق ایجاد کرده است؛ و نشان می‌دهد عراق که در کشمکش بین آمریکا و تهران گرفتار شده، همچنان قادر به اعمال کنترل کامل بر قلمرو خود نیست.
🔹
افشای این پایگاه‌ها می‌تواند تلاش‌های آمریکا برای مهار نفوذ ایران در عراق را تهدید کند. همچنین این اطلاعات نشان می‌دهد که حداقل یکی از این پایگاه‌ها از ژوئن ۲۰۲۵ یا زودتر برای واشینگتن شناخته شده بود، که به این معنی است آمریکا حقیقت حضور نیروهای دشمن را از عراق پنهان کرده است.
🔹
این پایگاه‌ها برای کوتاه‌تر کردن مسافت پرواز هواپیماهای اسرائیلی به سمت ایران ایجاد شده بودند و کاربرد موقتی داشتند. اکنون پایگاه النخیب دیگر فعال نیست، اما وضعیت پایگاه دوم مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/akhbarefori/652901" target="_blank">📅 21:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652900">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دولت ۷۵ همت گندم خرید
مجید آنجفی، معاون امور زراعت وزارت جهاد کشاورزی در
#گفتگو
با خبرفوری:
🔹
برداشت گندم در ۱۰ استان آغاز شده و تاکنون حدود ۱.۵۵ میلیون تن گندم به مراکز خرید تحویل داده شده است. با توجه به تامین مناسب نهاده‌ها و بارندگی‌های مطلوب، تولید گندم امسال به ۱۳.۵ تا ۱۴ میلیون تن برسد و حدود ۱۰ میلیون تن آن توسط دولت خریداری شود.
🔹
ارزش گندم تحویلی تاکنون حدود ۷۵ همت برآورد شده و قیمت خرید هر کیلو گندم بسته به کیفیت تا ۴۹۵۰۰ هزار تومان تعیین شده است. دولت در حال آماده‌سازی برای آغاز پرداخت مطالبات کشاورزان است
@Tv_Fori</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/akhbarefori/652900" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652899">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak8lSbgKFLWg6Ck09fM2x6BMhZh9Qq7sAzV5MW9vuNxpFvUtLD2p5-4sQbhI8iwlW3QnnpLJz_1B9US9vPRMfo3J5tzthjyzVHXiQpfN-iIh9N57XK2rlUkPjVB5FxMz-ymBEEbtIh7A_rlegFIY6nV5L3sD-6CXSpR7ket5esFR6nLwCJKar-BOJQziWAU61OmkaGQkqNiPmACazAJJdKF9odPUumwTaL8vi1yVk6lQfTYgIPmZbzpoQVbKALKnf42XasMx3Sdc7MOEdimzHPGVQYMpMTMBP_t_YfAUzfIjV24Q4s4uJwuRymWva6WmVM5AS6BityzyM5VcuHVLOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه کار در ایران را تمام کنیم؟! | حمله به زیر ساخت، تصرف جزایر، تداوم محاصره، حملات شدید به شهرها، ورود زمینی به ایران: توهمات آمریکایی‌ها ادامه دارد
🔹
ست کراپسی رئیس اندیشکده «یورک‌تاون اینستیتو» و از چهره‌های امنیتی نزدیک به جریان نومحافظه‌کار آمریکاست که سابقه فعالیت در نیروی دریایی و وزارت نیروی دریایی آمریکا را دارد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3216031</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/akhbarefori/652899" target="_blank">📅 21:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652898">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d40c662626.mp4?token=M5i0U3EtRzl0C_42qqR4QEHQhc5A-q7vdUnAI8JBESw3KQ-zC-UKO_pdZlIL9afK7sh7sK0kG88XYxdOncekq7t39Tf-aeOATzFry_Ij8UFq5Tt-4Lzg2gg1418Kuyh3oYgPeG-944LTsHA6BnT0Gm1EQSqmo7km6O59EA0o0eVLWKFLd2Nhggj00E8M10HV-qChkuO1bI4dAZwqr4qICzpmVZTIQZNcDJxPjPZTBhzYsBh7Ot7MEG2q2Ju-HlfSIDKMgCMCGqsCqa_i_CwUjYV_wZk13RVuQjIyrZ2g_l9lOOxkl3wW63MUj6bONwQB3jLBgqH1uuzkjHEcbTUBpl6ua5bbpQh1e9x5Ob7LBs-PcFaEBSVnvLAq96QX8IOjFUAKRfXbRLazz1Xg0RnCoaIjv4trLasJkgGIDkjfQ4dwiQLPvRr0JLFX-cHwaZzRcPtG4rP2RgQj1K6zxmPCWBOwzlF-iIwQMmezyF6w2ehn9-Rj9pSSdFGYgWjdZptmgjZ_oI_IUidp5bDyUHfDr5I9HXSVwTr6lKjjjPN766C-OiBOYQdr-wUZhMQv_e4cwtPtUcUyz80L8ChQqFRl4Doil5FW_l6vwnCglcofF4R9rGeA9tGD_QlN95QR7M7nlxjGodM3NVEvtTr4FzfnPPgDC8en-zB9dBlToY7B1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d40c662626.mp4?token=M5i0U3EtRzl0C_42qqR4QEHQhc5A-q7vdUnAI8JBESw3KQ-zC-UKO_pdZlIL9afK7sh7sK0kG88XYxdOncekq7t39Tf-aeOATzFry_Ij8UFq5Tt-4Lzg2gg1418Kuyh3oYgPeG-944LTsHA6BnT0Gm1EQSqmo7km6O59EA0o0eVLWKFLd2Nhggj00E8M10HV-qChkuO1bI4dAZwqr4qICzpmVZTIQZNcDJxPjPZTBhzYsBh7Ot7MEG2q2Ju-HlfSIDKMgCMCGqsCqa_i_CwUjYV_wZk13RVuQjIyrZ2g_l9lOOxkl3wW63MUj6bONwQB3jLBgqH1uuzkjHEcbTUBpl6ua5bbpQh1e9x5Ob7LBs-PcFaEBSVnvLAq96QX8IOjFUAKRfXbRLazz1Xg0RnCoaIjv4trLasJkgGIDkjfQ4dwiQLPvRr0JLFX-cHwaZzRcPtG4rP2RgQj1K6zxmPCWBOwzlF-iIwQMmezyF6w2ehn9-Rj9pSSdFGYgWjdZptmgjZ_oI_IUidp5bDyUHfDr5I9HXSVwTr6lKjjjPN766C-OiBOYQdr-wUZhMQv_e4cwtPtUcUyz80L8ChQqFRl4Doil5FW_l6vwnCglcofF4R9rGeA9tGD_QlN95QR7M7nlxjGodM3NVEvtTr4FzfnPPgDC8en-zB9dBlToY7B1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مادر یکی از دانش‌آموزان شهید مینابی: دخترم روزه‌اولی بود و با زبان روزه شهید شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/akhbarefori/652898" target="_blank">📅 21:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652897">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9688024d35.mp4?token=LBRjE5C7Xnc-Xp_3QtESTaYhdUGgId22TP7uOktWSAaA8C4lotYdPXVMDQmK-yPmkxnIBWfYBgh-S-T8JZknFSaIPpnqCVo9vhM8D1WNfXf_48qJ0HiXMBebbidlseywZsoqLK6WhtuZ-UlPXfMvZk5ZaFd4qIuZqenkt3xZItQ_kqL1zcw8IRW0Mugx46gxlGgiC-LCzPru2pjdnKoq4Tc6CuRp-iW5oxp34uyqjBFpiE9jjcPZnzWXMLNYd592JfhEab0lHSgjQ1FFYUsXTks_uUK6m8zfpaTob1w_3u8Ked3EiPOM_6IMLwDzCs8-UT52V7bUz4tEb2gyQi18bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9688024d35.mp4?token=LBRjE5C7Xnc-Xp_3QtESTaYhdUGgId22TP7uOktWSAaA8C4lotYdPXVMDQmK-yPmkxnIBWfYBgh-S-T8JZknFSaIPpnqCVo9vhM8D1WNfXf_48qJ0HiXMBebbidlseywZsoqLK6WhtuZ-UlPXfMvZk5ZaFd4qIuZqenkt3xZItQ_kqL1zcw8IRW0Mugx46gxlGgiC-LCzPru2pjdnKoq4Tc6CuRp-iW5oxp34uyqjBFpiE9jjcPZnzWXMLNYd592JfhEab0lHSgjQ1FFYUsXTks_uUK6m8zfpaTob1w_3u8Ked3EiPOM_6IMLwDzCs8-UT52V7bUz4tEb2gyQi18bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از سردار شهید محمدصالح اسدی، معاون اطلاعات ستاد کل نیروهای مسلح
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/akhbarefori/652897" target="_blank">📅 21:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652896">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
کمبود مهمات راهبردی آمریکا پس از درگیری با ایران
مرکز مطالعات استراتژیک و بین‌المللی آمریکا:
🔹
به گزارش منابع نظامی، نیروهای آمریکایی در ۳۹ روز عملیات هوایی و موشکی به ایران، مصرف بی‌سابقه‌ای از مهمات داشته‌اند. برای چهار نوع مهمات کلیدی، آمریکا بیش از نیمی از ذخایر قبل از جنگ مصرف شده است.
🔹
بازسازی این مهمات به سطح پیشین، بین یک تا چهار سال زمان نیاز دارد؛ چراکه تحویل محموله‌های جدید زمان‌بر است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/akhbarefori/652896" target="_blank">📅 21:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652895">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec7a93b6b.mp4?token=UUZgw_BefFgMP1Mh5GpiQSAFA9b_mTVDVY_Q_4rZ0g50H1Nipoh4b68iuZ4vZBrIt1eXljGFxawFnglCt8TvcWvwAAUkqm1V7l484C__U9T7iJpqJNxJeeqxK5CYn2wb5fLqlzNLD5A-LPvdkdHa1VylqiNYb8vrM5blgeGaf4S7oScodiV3BOmJXmjGjjUPjnq3GV43HXbjfvHYO_QdoWHdUP2oCzWU626xAHd-Hi2UQnrM2EhnMcZYzVMRY4c5WFOYzXd3GACqFPJfPOtZRw38_OcCTQJxJPsD8pCs1LB9upUsdZx9v7CfbLlbs0_oeHBcG8hleTmPCnr6X3OjW67hYntOc4kQHyo9sRXpPyMiXY2026pr1Ax3LaMXZvj02LQq_OnQhF0MvqRdoRWPCH6r09b32I0CoUGIc2jvMlqIyjBcFIHzhdLtVZcTGPVXqrMl1O3Oa6sfv6iqN8bANE6VNFY4vTvifCRNwkuZeojJkaMTbUVgqAUfv6nejMsmBDDCiipDe2Q1DP7gdTRekgj1ZCtFoxw31aBsm-rW3TI_YEEb2EapLZJ7pAmDOKuCKlBlnvSXzvwpH9DDh88FtALGn-Z2B1e1j5iCb-H1OSqE-F-aSsyG1BS8ADTOniQvNglxv_1w1TqUsNCe_cCa9tw-6IHBPO-GYJEEIDZJn1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec7a93b6b.mp4?token=UUZgw_BefFgMP1Mh5GpiQSAFA9b_mTVDVY_Q_4rZ0g50H1Nipoh4b68iuZ4vZBrIt1eXljGFxawFnglCt8TvcWvwAAUkqm1V7l484C__U9T7iJpqJNxJeeqxK5CYn2wb5fLqlzNLD5A-LPvdkdHa1VylqiNYb8vrM5blgeGaf4S7oScodiV3BOmJXmjGjjUPjnq3GV43HXbjfvHYO_QdoWHdUP2oCzWU626xAHd-Hi2UQnrM2EhnMcZYzVMRY4c5WFOYzXd3GACqFPJfPOtZRw38_OcCTQJxJPsD8pCs1LB9upUsdZx9v7CfbLlbs0_oeHBcG8hleTmPCnr6X3OjW67hYntOc4kQHyo9sRXpPyMiXY2026pr1Ax3LaMXZvj02LQq_OnQhF0MvqRdoRWPCH6r09b32I0CoUGIc2jvMlqIyjBcFIHzhdLtVZcTGPVXqrMl1O3Oa6sfv6iqN8bANE6VNFY4vTvifCRNwkuZeojJkaMTbUVgqAUfv6nejMsmBDDCiipDe2Q1DP7gdTRekgj1ZCtFoxw31aBsm-rW3TI_YEEb2EapLZJ7pAmDOKuCKlBlnvSXzvwpH9DDh88FtALGn-Z2B1e1j5iCb-H1OSqE-F-aSsyG1BS8ADTOniQvNglxv_1w1TqUsNCe_cCa9tw-6IHBPO-GYJEEIDZJn1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوک عجیب به بازار موبایل
🔹
گرانی موبایل این‌ روزها را که کنار بگذاریم، یک اتفاق عجیب دیگر بازار موبایل را تحت‌الشعاع قرار داده است.
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/652895" target="_blank">📅 20:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652894">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
آغاز پرداخت مستمری اردیبهشت بازنشستگان تامین اجتماعی از فردا
🔹
سازمان تامین اجتماعی: واریزی اردیبهشت به صورت علی‌الحساب و بر اساس آخرین حکم سال گذشته بازنشستگان پرداخت می‌شود.
🔹
احکام جدید با احتساب افزایش سالانه و متناسب‌سازی تا پانزدهم خرداد انجام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/akhbarefori/652894" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652893">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
چهار دسته اصلی نمادهای بورس که تعلیق می‌شوند
🔹
آسیب‌دیده مستقیم از دشمن: شرکت‌هایی که بر اثر حملات، دچار اختلال جدی در تولید یا فعالیت کلیدی شده‌اند.
🔹
آسیب‌دیده زنجیره‌ای: شرکت‌هایی که توقف تولید یا خدمات آن‌ها، ناشی از اختلال در شرکت‌های دسته اول است.
🔹
هلدینگ‌های وابسته: شرکت‌هایی که بخش مهمی از سودآوری آن‌ها (بر اساس آخرین صورت‌های مالی حسابرسی‌شده) به شرکت‌های دسته اول و دوم گره خورده است.
🔹
شرکت‌های سرمایه‌گذاری: شرکت‌هایی که بخش قابل‌توجهی از پرتفوی آن‌ها در سهام شرکت‌های تعلیق‌ شده سرمایه‌گذاری شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/akhbarefori/652893" target="_blank">📅 20:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652883">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqzOH60RzpV8xwP1JpBYHYI4OzFtJ0qmZrEkOWl9EQih9th8vR73-Eq680mwBRfDRbLxJsqMC_tfYOzxepDrwYaYA2lqP6JpYhb8fOiC9VODxvpTcNRqJGq1F0FADTVkkUfhhetEsVCqBLxDG7VTKwtAbyJfGpbVv6QDetHkacWYGl4RE6MIEpvhNr-_o5hZ3uF-5PefQdyYm8P1i7GE_5MO3mymgCzIO1oL6t-I2nXTpPA0vHFP672sBAZ4mJfYSONLDHCOqoIIZZSrCdTbJzsRwukSuZJ6N-n1EEnq-3c28-3u-LtbeVj2pGDo4B-gBCilWQlW4kU5dJSEbzWVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMsbEwPiBtwdUh_LHFbq8gvfRoA5_o26oVXzMNR3cYtYpy-LZO4Ksu5WN2myhZw4I0gl9iWnQCgvuxPFTC2fhiKZ8MMffgmgJajpC0MmpiPLKfjk5Lsm6XtDh5HTuqrZ1BiSFq3PqTjUOyXvzXDg9Dyt7lhlqjbVWlJ2mQwa_R4CzpX2SYwRDmYMJxUK5EjkGcaq8mxSM0KFyZAmItiqZZR2KAivDX_bvNONl3RV0j8_4VyQCegDes2K-w2yi0Gn4uwHkntok17GYoQo4nk_Vx-pcVSNJswnmLzPzhIKJdX0M4HyNLvGNslreQ68NmR0PvOoOepm3etq37OjGrHiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe9elpj7s-CvCyqdsoFsy2HPpnJd9QsUWKqnaFZBJsHsK23AkPCDoxkMxYhCKdCMp6_zg7fWU0mS-ckFxeZjdiU5jXzafo2yRXMki7lixrc1LWhy33MHQ3uUbdWHI8vJL66D70iI9vRl_h-bzHMWQHu90AN1Bvujud_T9oxYrkme7lTfE8mVVYAODY3LItxf46Env-2vLlnPvma3vnYd8Vkue9Odf8pRPHyRuPIjMylZa1jc-UTmNMiTYsgnHrF0NO6chu8vt_rduegS33zp06w_6RZ7aCoKwdzAofoQvifyz_SVg95JJSyQgmHUFhdJyCD7a1yD0bE_b2oUSjcYVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iahqXZq2fiUCZO2dz4bg1G-wkbXFjBGsKWRAOubLncye7oGwtgAXZK3m-N038ckdy-vPv6e9ZbxIt1P7T9QtWlr6o0XVdwVEdevkKrdZbX211DqpsYXJgggCsMm6P4SIuKODMizaAyQQ61dwioVGIXBvccx7R_67_agccdiMhobpFZfumxTA92waXbK5ba_i6Q0AIsyizjPNrPC5C-38MoAHtvc_Rp_gKOQLnIy5fROTTwlsN46_i9tv8QfUR3QT0eaEcxEYjuezLKvjARXTo0oUjv6VKBkYeAWe3oVGM9V-41wHJ7v8rtCGKyrcNvJiaeYpl3aNlfW6VJBAqyPdDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwkDPLlaHc1oz5YymmmKK_uanFW18HM6Dg5yNCTfBCcQfCQ7oThODRmS1msKV-UBUsDN2JMKBXd-jwRJOI7O5ZF5i6086OFCla68T6SWhO2267DDz_MhQGkOgwd7WyhP8RuHSnxIXW7Rhd2S7REsn0uGG_608vPPHPxxzNs1PUu5LMX3Dv-7S6arbezdZEHNUh3J8pcRrlAdSaoiI08zuAOJPsupVWiT9PGu-TVPrXAlvr_vHL4u7PrLqvCFZY_6QWc9fZs7flNg6zSdm6is59NMvGHiYoNrf-yyhyfzcP8OUg-WiXgIL01cGXK-MAUZIbEWXyU_-7qE_SCr6wOxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvkH4hutIWScLpuT50O8pNqFN54xB9iUPkzCTHBR6UYEqwwSdMDrEIAKQ-0JqfAQpwKPWIWwpgrO2L7495F-TyrHKh8x9DR3iE0iCdVGOoLutiFFzOXY8BTRyvNdUT_qVAxObEwS4GzRZN8V2i7c1sbRpDBdN8YvZR0jxihH62eQhnHpVQ0-Elg6jgfmO2QY8BF34C2KqFVrYNgLkinuBOJayug4ooUNdhltD29sCuh0D_FBZf-uaUjNCXpda3XEbDYZlsw4eNXlpArkJMSjt3bi_G3ZGFCZbhWwORO9hY6VqRt9DmmQ9X6CGZW9h0BYOJRFCv5BXIsTQKHbWQXh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yo_BWof7mTmUra3LgouEpOGt8FaSTfCIeBOiJvVVd8MPEhmQfaWdfuEZjR9QoAqdn4ytVP8zzxJt0RvHKEnECyjIdBCIICEjluIypCXHCMRfyIUOEVhhpJ3arHMlp8aXtSzNaEmFtnjkZMleVrXVTKQVo7hh_lVFcjjPeH8ark85ALiA1EMLnquq0iYAKhw41I4W9eyo_mvd6y6aCPvDUgd8HU_fscdp84JoleWQyRP-h8WbZpoA6PW3iZEi5jEEBIygWd7rHmBZxwMsdz_Xdtx6e6VjjDRW38YfM9dC1eEimPfo-d7M2ZIf2FSvkP3nNjcZmfTi9uUUALyIdZyTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndb0SlkxL1qt2R7YMxjiBCxPyQ7bCS8mYM5hZzRvp0CVhO75mtvRF7GomKTR1HrB6k_AMiMNmpQvaecQ59kga5ZWH2I_Q_G_GVHtOZeTZmwLtdVbIYq6ITRK8Kwxsk-i1ytn55nAZwo-9urNDtOsi0UaYoVtoX0W_cKUkMWVPxH5UtZrJxevv9DQTBziietwkNkUuSXN3iuuI7xmoRmrvHaBOzB9A8jMQDJrsmuBFNVd9vXNpLlop0EugdclsruqdOohzr_BbVvW-sTuRZCjutcXyVaPuOGSZ4SnGYHHE1SX4Na5i6pteH55TUAWIxsBGiJn55ONMwE0WGOt_HmQSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYTgCsoWY0n92LhlPhONAJGU5odCzwYlE66HxnZ097KjGjXeqYwN-3wBWAC4Fkh2jodcr9zdRwWxwJyBm9fCDLhq5QnMVUNbOaR-JcpNDSio08BJYeCreVC60NJAhAVfV63ei_Vk6Cr7dw7_dRKHUrX10FS_v9hm2N-vt4IVFT8WhxTELEE8OOKgUxgyWb1-pMGs-nyxBlfh0_McwhlrwGr1l6FknVl415hKMHiposN4-hOgLENgeTvFl64CumN6T6gzZk6uaeZzAfJ1FviT_lsIPMFo0_AxsDbujDKjPKF7pI5Z9EdIyaCMhvtPxy358iiLeJR59fnjzmnH6SELMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLzpzFz2-pUj5gMjHTDQhVs0uQj6BPIOecGpGdIwRv8XTaZVskItzscRzuXlyjkdt3WesMBPUUg8RQJKPyjbdjmonok3P489MI5MYEp_iBocBnyyzFuyMMNVBqWLeg05gqd_I3O2z4zmb7k2U_9DVk0dSYc-LuT_-Lz8NC0vMUMtcxZX4uzl1GE7pwEh4w8k5eUi3bf82Mf7QFwkp7pUgzEuK03nupB9BIDccW7_ZwR1Nl62yukoqeB0xV9uvlMg33my62ihZNpTnhPeuGFZ0puxXuOzBSBMNXgBw22Bdjxgb2ZdpHQJN1JKqg0brucNJvGsLIV4ekevrr1ZKwDZrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
لبخندِ کرامت در روستاهای مرزی زابل
🔸
#گزارش‌تصویری
از توزیع بسته‌های حمایتی در روستاهای کم‌برخوردار و مرزی شهرستان زابل، به همت
#هیأت‌قرار
و دستان مهربان خیرین عزیز در دهه کرامت
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/652883" target="_blank">📅 20:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652882">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
گرچه متن‌های ارسالی بین ایران و آمریکا از برخی اختلاف‌ها کاسته‌شده اما هنوز شکاف‌های جدی وجود دارد. / این شکاف‌ها شامل مواد، غنی‌سازی، پول‌های بلوکه‌شده است. / در عین حال در برخی موارد مانند اسقاطی‌های نفتی یا پایان جنگ پیشرفت حاصل شده است./ در متن ارسالی آمریکا به ایران که مربوط به هفته گذشته است، طرف آمریکایی شروط ایران از جمله پایان جنگ در همه جبهه‌ها، ایجاد صندوق بازسازی و‌ توسعه و پایان محاصره را پذیرفته است./ در متن آمریکا پذیرفته‌شده که جنگ در همه جبهه‌ها از جمله لبنان پایان یابد/ همچنین صندوق بازسازی و توسعه که مربوط به غرامت‌ها است ایجاد شود/ درباره عدد این صندوق گفتگو همچنان ادامه دارد/ همچنین در متن آمریکایی، پایان محاصره پذیرفته شده است./صبح
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/652882" target="_blank">📅 20:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652881">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
شمار شهدای حملات رژیم صهیونیستی به لبنان به بیش از ۳ هزار نفر رسید
🔹
وزارت بهداشت لبنان روز دوشنبه اعلام کرد که شمار شهدای این کشور در پی حملات رژیم صهیونیستی از ۲ مارس ۲۰۲۶ به ۳۰۲۰ نفر افزایش یافت.
🔹
همچنین به دنبال حملات این رژیم به لبنان، ۹۲۷۳ نفر نیز مجروح شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/akhbarefori/652881" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652880">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-3cEpcAU3gmQYDQ_dsDepK4yeL3uLVv36kBT2AotKb2j3eWAmD7wcDPztSeTnubqwBmcupOh082q0-EzLbXpzMxfWLZXxNzFrrFv7S9kIA__py32ye_WvqZs_WGejbwadWSFYh28SAMgABS8Ot8s3Q-SDz0VNt7bJxF008j9BhlF4LCrwyeE-20CBowJM9u4PIIm3SjJuQDLIfTf08F1KMBGY4e-hMUAsVQkgyDg7jh1OFHiH013kMGi1_OBfLtuiulpCkITHFcAKvaB646WkAySv1_BvDk9-Je9lpEOVQ_8pYPLZ32P26wfCHwNIEvyOT5atGP2TtYiRKPMUTQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: حاضر به دادن هیچ امتیازی به ایران نیستم!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/akhbarefori/652880" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652879">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سردار طلایی‌نیک: بخش قابل توجهی از توانایی‌های ما هنوز مورد استفاده قرار نگرفته است
🔹
سخنگوی وزارت دفاع: اعتبار آمریکا به دست نیروهای ما از بین رفته است.
🔹
به هرگونه تجاوزی علیه کشورمان با شدت بیشتری پاسخ خواهیم داد و برای همه سناریوها آماده هستیم.
🔹
آمریکایی ها یا باید تسلیم دیپلماسی و شرایط ما شوند یا تسلیم قدرت موشکی ما.
🔹
در حال اجرای یک نظام حقوقی جدید و تصویب آن در مجلس شورا برای مدیریت تنگه هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/akhbarefori/652879" target="_blank">📅 20:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652878">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
شبکه CNBC به نقل از یک مقام آمریکایی: گزارش‌ها درباره موافقت واشینگتن با لغو تحریم‌های نفتی ایران دروغ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/akhbarefori/652878" target="_blank">📅 20:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652877">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ترامپ: ایران می‌داند که به زودی چه اتفاقی خواهد افتاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/akhbarefori/652877" target="_blank">📅 20:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652876">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: شکست آمریکا در حمله به ایران بازارهای نفت را تحت تأثیر قرار داد
🔹
امت اسلامی، چه دولت‌ها و چه ملت‌ها، می‌توانند اقداماتی مانند تحریم اقتصادی و سیاسی را در پیش بگیرند.
🔹
تحریم اقتصادی و سیاسی ابزار مؤثر و فشار قابل توجهی بر دشمنان وارد می‌کند.
🔹
جهان از پیامدهای شکست آمریکا در حمله به جمهوری اسلامی ایران در بازارهای نفت تأثیر پذیرفته است.
🔹
نبود اراده در میان بسیاری از کشورهای اسلامی برای اتخاذ موضع، وضعیت خطرناکی ایجاد می‌کند و دشمنان را جسورتر می‌سازد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/akhbarefori/652876" target="_blank">📅 20:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652875">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRNiUWmQklPMWwwDWgmMPcEhbLfPUAt7Ys6O6QgVJsj-YmTsXU3lsayWhKLM9xSz8GaOxJR7iUg8_6OijKy_co1EFwyPym0FWBTV71YsHgUBUCWxkU9HzK3Xd74s9RN97xDnUosKlQvRnw-7uZ6a07T7v0oplP7dJcDXxBH4f1Jgh5ZxWXLrF8dvCbVU8FSyVlAi9FiPs3GPpowU4pM7LSw4NU-3ekrKQHuz-7tS6ecQBegrOJhx2tf8FUTNnaAjBaJAHU14avhZVFpb-H9MimUDuD-SXJBWbwrse2ljqccq8WvYFntegijamrGYQ30IMxFnRx4Zw4Zkyu_nOFFX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار حزب‌الله عراق به دولت اردن
🔹
حزب‌الله عراق: بخش اعظم عملیات شناسایی آمریکا و رژیم صهیونیستی از مبدا اردن انجام می‌شود و این مقدمه‌ای برای انجام اقدامات خصمانه در داخل عراق است لذا دولت امّان باید از اتفاقات جنگ اخیر درس بگیرد چرا که کاسه صبر درحال لبریز شدن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/akhbarefori/652875" target="_blank">📅 20:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652874">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_1NkmcZ2_aIwnLB8In_4eAZ4MeBx6O2x83ypEF1Qf4dgHRAK43gTPSyPi47mAtjxOjQszQKLl35wsoWxD6Dh5FOR67DrDy0R4BBE8IKqLRpoC-9WaiAQf_CH5x4Q2jWkEoiC-91n1kqFhqRSOaBo7VYYJcnlTaSo6iV-Htxs9fi7kpFeloeLHjiVRvBftA53kJXTLd7W7AqSYd1oaugqcimWpg2QN1wy1JPT-D1hJK7vUmiZT3grBUQn0yVgAz-RJeNdybOlG2i13SafoVPLAH2GpUR4Cea2SyVTLovAjsubimhNLBKaMcNppg2BIqCp_3_m9h3ByGhduidtndDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت پراید در هر سال معادل چند دلار است؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/akhbarefori/652874" target="_blank">📅 20:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652873">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG_JqzdtXDFXo7GRUPX4g4gvYjCkaDd8YSHefUNt65VUX6aKBR3iUCyfb6k-f9vAedbW1q6OuzJ-DzaeWWGZhonDqzcpPjopKebWYauCRD2llFHHKoAvgcR1eB9URos7z2At86uOfCGwlNyxKNiCgF5E2K18bHmaNMsNaSp672naPN_uZchA5P1Ql33BwUgpKYUulGC8xHvkCmIZWnR6ydtWnIA4FjX6JNHtgXaOUBa_kribRErXnpkk0aHGtzrpNMXuMzUgTnTQr526R-46lpmfw_hkaQFshGXqHbDwM_jB6Pt7_mQiJZkK-_6T8mSVb9AAx1ZWrfA8SWOTiOytzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای جلسه محرمانه ترامپ درباره جنگ با ایران/ مقاله جنجالی وال استریت ژورنال: ۷ پلن واشنگتن برای جنگ جدید/ نگرانی شدید ترامپ درباره آینده
🔹
اطرافیان ترامپ نیز در مورد ایده از سرگیری جنگ با ایران چند دسته هستند: الف. طرفداران جنگ بزرگ با ایران ب. طرفداران ترک سریع مخاصمه با ایران ج. طرفداران توافق سریع با ایران.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3216025</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/akhbarefori/652873" target="_blank">📅 20:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652872">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/652872" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652871">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myKxCIPNkHDXlVcs_FpOyphe34HrKH152kSrnUC9jR7qXVR-P-dn-JfNaEM_IS8tIOFCrzNfNg0aTlV3pw5DDdJE1XOBmXmdD8RwnIu94ajodTP-9GHCmIb768oqm1KOkiMKMEzzKvTU_kM6CJi_1QhWkfRiNVovgi6ox_NCgzyrJ4-TFo81NjJUOEak79wpphc4UeoB92a9TU-Cr9fLJAifNOr0LyYRucrDePTqUKDoStmoGBLXnCM3lJRa0dcniSSV-oQk-Md1ggBNtqxHRhAmRuVtbg_SSGtE9EEW9YlX35sm5vyWrfkafFxX88j-8pvgtRDnyXXFAIRXq07_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌ استریت ژورنال: حملات مخفیانه امارات و عربستان به ایران، همزیستی شکننده و پرتنش در منطقه را فروپاشاند
🔹
دوره تنش‌زدایی محتاطانه میان ایران و کشورهای عرب خلیج فارس عملاً پایان یافته است. آشتی‌های دیپلماتیک سال‌های اخیر، هرگز به معنای رفع واقعی رقابت امنیتی نبود و تنها نوعی همزیستی شکننده را ایجاد کرده بود؛ وضعیتی که با جنگ اخیر و حملات متقابل از هم پاشید.
🔹
ایران اکنون نسبت به گذشته اهرم‌های فشار بیشتری در اختیار دارد؛ از توان موشکی و پهپادی گرفته تا شبکه نیروهای نیابتی و موقعیت ژئوپلیتیکی در خلیج فارس و تنگه هرمز.
🔹
حتی اگر کشورهای عرب یا آمریکا بتوانند به زیرساخت‌های ایران ضربه بزنند، تهران نیز قادر است با اقدام متقابل هزینه اقتصادی و امنیتی سنگینی بر منطقه تحمیل کند.
🔹
عربستان همچنان نسبت به ورود به یک جنگ فرسایشی محتاط است، زیرا نگران آسیب دیدن پروژه‌های اقتصادی بلندپروازانه‌اش است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/akhbarefori/652871" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652870">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ddb09517.mp4?token=BhSAeeBSlODFQct2kha7ijzMuP-fKNttdqOHJ4paA_rrGUlpES4bc3ulA09q_pahMbRArkUdKdCE164AyE5Kxo4tF7VjJwItdkcHDFDYjSWFRIredlZoCsQrO51mx7Cr8X8TLlmuh_Qw-idUjQiXs1iPscE1iLh5548xT6sY4PG5NExHWTSECITJe7EB1iilAg31opLZ8awqdJUGg-QX5z4gdPvKGurU5nzbLFY0xnMeFfxJrKJgwVz1edNPHJgu1LUe1NC3sA5EGDvXpYvKHQfTM54EuSmv3mBP8irfETflpC8NhzSqusbB3KcCluJzeLWpRICPvo5320i-NOYC5w0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ddb09517.mp4?token=BhSAeeBSlODFQct2kha7ijzMuP-fKNttdqOHJ4paA_rrGUlpES4bc3ulA09q_pahMbRArkUdKdCE164AyE5Kxo4tF7VjJwItdkcHDFDYjSWFRIredlZoCsQrO51mx7Cr8X8TLlmuh_Qw-idUjQiXs1iPscE1iLh5548xT6sY4PG5NExHWTSECITJe7EB1iilAg31opLZ8awqdJUGg-QX5z4gdPvKGurU5nzbLFY0xnMeFfxJrKJgwVz1edNPHJgu1LUe1NC3sA5EGDvXpYvKHQfTM54EuSmv3mBP8irfETflpC8NhzSqusbB3KcCluJzeLWpRICPvo5320i-NOYC5w0uFQS3YFJdqzRfyUqe6uvjb7aUR1jlBQ4LiEL7AINAzvQ_NwGGqfP8O3iPRSX_MJ_EPJkl-N1XXpgkZV-bFcP9S_W-yX-OMMpJWHoe7M58amjihDl89b-fYY5rXSkHr83SgzxYRebhmaATmJR_-9v3LBmlvtDkMRgC_b1qHTFfoUmLmm3UFKEUS7EqEzKkDQPSiSodonjIr-ZV2BDOSxwWoJs0YFPu65iZ3s7quMJNNQuJ21VZGfFOgW4YSlYDRldMIdWZo0N7L8Y_-SqG0roDUDq9d9DPRl9lOEdHWrQ4XxdC_ByNz-jVTF7xyJjoMhYCL8O6zneiVrSEk0wFcug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز اگر کسانی بخواهند از منافع ملی صرف نظر کنند برای خاطر رضایت آمریکا، ملت گریبان این‌ها را خواهد گرفت
🔹
به وقت شهید ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/akhbarefori/652870" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652869">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwElvKA9np7LcqYAH8rZqDlugG_nQjSBRWsTXz6mcyFXOcgTe1b9wQrWS6qQQhxWYuh4VGDWoC1GJupRQNkgcI4zNVuvuxKGbfz6SCrQ8d-kG2Al6g6L5G93KoIl_-7T_YGFg-HvCwqYEis7uF9xK1mpHVsLlmJIY0C1UphZjji3m0blW_T4sZEruUF6uct58fTb_O4Zp7igM5Z1rATpQGgWgO3XSBRQ5YVcw55MmfBPia8J8JVosgxp5x5KVfxe3AKDlkCknmfXF_Fd2_xRUcyEGijhroSV5_cyBP8HacqfjV-aCX1-kSQbXJKdVK3QAFO1dHiMQc0Rtsbqr2MRIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف غرب به توان مدیریت محاصرهٔ ایران
🔹
شرکت رهیابی محموله‌های دریایی، تنکرترکرز می‌گوید: وضعیت ذخیره‌سازی نفت ایران بحرانی به نظر نمی‌رسد.
🔹
شبکهٔ خبری بلومبرگ ساعاتی پیش با استناد به تصاویر ماهواره‌ای نوشت که نفتکش‌هایی که در جزیرهٔ خارگ پهلو گرفته‌اند به بالاترین تعداد از زمان محاصرهٔ آمریکا علیه بنادر ایران رسیده است.
🔹
این شرکت کمک‌کننده به آمریکا برای رهیابی محموله‌های نفتی ایران می‌گوید: این نادرست است، تعداد زیادی نفتکش در محدودهٔ محاصره وجود دارد اما تولید نفت خود را مدیریت کرده و ذخیره‌سازی‌هایی هم در خشکی انجام داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/akhbarefori/652869" target="_blank">📅 19:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652868">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd98eeb7bf.mp4?token=kp5MfFnsO97sjFKdJbEr3kZtt_QDIWfv675g5jm-VFZC_JfyWVsEIVi2t5za4pDzmOBjmTdD3hR9PORDMMHumjD4vi7GHWZ4hSZiXHaJ6xjtYxMRqVX53x-7WwHYBbowJblITBn276ArqbHhc9e8iqv_v5I6bEk9UfXgbeZZDJPTUCTajmzLBrFB8FYtTHDoY7WexLKnkpW2uFMTDO39PshB8thtOIx4hYeOtFJM_-0bRICJeQwtiQorWO7bLB4-R0YFzelEjrZnMcosiT8A-DIwnklvTWxX8beQLSV-44R-HEIq2ZOyHMgqcOY3Ok3u3mx2ck44W7yTdWsXqkCSLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd98eeb7bf.mp4?token=kp5MfFnsO97sjFKdJbEr3kZtt_QDIWfv675g5jm-VFZC_JfyWVsEIVi2t5za4pDzmOBjmTdD3hR9PORDMMHumjD4vi7GHWZ4hSZiXHaJ6xjtYxMRqVX53x-7WwHYBbowJblITBn276ArqbHhc9e8iqv_v5I6bEk9UfXgbeZZDJPTUCTajmzLBrFB8FYtTHDoY7WexLKnkpW2uFMTDO39PshB8thtOIx4hYeOtFJM_-0bRICJeQwtiQorWO7bLB4-R0YFzelEjrZnMcosiT8A-DIwnklvTWxX8beQLSV-44R-HEIq2ZOyHMgqcOY3Ok3u3mx2ck44W7yTdWsXqkCSLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چالش‌های آموزش مجازی از نگاه شما؛ مشکلات نرم‌افزاری، سخت‌افزاری و اینترنتی
🔹
«تجربه شما از چالش‌های آموزش غیرحضوری چیست؟»
مخاطبان خبرفوری در پاسخ به این پرسش، از مشکلات نرم‌افزاری، سخت‌افزاری و اختلالات اینترنتی در دوران آموزش مجازی گفتند.
🔹
در ادامه، بخشی از این روایت‌ها را بازنشر می‌کنیم.
الوفوری را دنبال کنید
👇
@Alo_Fori</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/652868" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652867">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUyBF9krdZbi72vN25ewxTlgi2_CIQw1PYyZez9qL5Cb_6ZOVc7bOdmg8onOkrBOfCA55uhwhQrY--emEauelYml-sqcN3L8c09kYwMLJtWztDQ-yiOXlkHYAvOwQhn18H5_uT-djxFTAectkaQ7F2Dmf37s5XfX4HTFA6Brgvs_HXmv3VjNKVwE0Lu4WO4NmWBREis54ecNgx9cSZGguxOAML5OrGT8kevEpPQzz90RH07osEBI7k8CV22sCLdu8RsmbGx16xSD-RwliQz996wfe5LvbXvrvBlIOyCf0LyQYq0ZAxsNeQ8YB6wyQuIXvhVm2Ymal_nEWgw9JVBX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«یک انتخاب، دو سرنوشت»
🔹
سمت چپ، غذایی که با احترام به زمین سرو می‌شود
🔹
سمت راست، زباله‌ای که آینده را می‌بلعد.   هر بسته‌بندی، یک تصمیم است، تصمیمی که طعم فردا را می‌سازد.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/652867" target="_blank">📅 17:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652866">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6e8d401a.mp4?token=Lz758UhTu0Rw_Fze6KJMdBFnea43_UjwU1fxe2fB7xCjFKVG3H53yy1wcSmauQwgTx5ck8jKLQp0_vSVPnztZT57bclgjPU94s0LbYoENloGSNipj6LUYzl8KAimCmE5hwVnT0L0UqyAjp8b4_sKdoOcelERq69vmQXQdvIs18U49gbXlDFzcbb2gVh05gShMuiEAkMmzVYUw_ESKGytxD--Kg-LplQlSRiOFQeHpuvQe5UuwKPuxjydtUwnWxTG3me-VPOlA5tgfq46bctk3udSew5Oj_C_FljFjsZluXfXic4h1Kf_XT-_RMIPZMNHXjahbMjRatzGmheDheSh26bryqDCFeZyDgrqiqz0ey4o8-gD4svGWhlI8gYhxcgk0uTx7Zo_b-ZHVBs74W50PPX1hu4oX7WnVCjK-yUxltiVZ34rP4gzMmXWIB2LbGQQ41azrbeyod3lsw5G23JF2yv8SzzMOu1wAusomKX_3xuceulkmkpa8YlPUJ_A3MlBoZnCmiUPZ51NLM4IKfETrbtvOWrm3aj-UkJ21jT9hPtT1wUw9T4GsefqtIo3TojU5T2f3tiKHuTuDgiK9u7DZpFUWzOpw3nVCJfnCO3gq1WnPGGwi8XrT2CKFjO_3fkRkt9kbNB_Hv9Z5Tax0bxAgCSJR6sBtqPQVJpImVYmpKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6e8d401a.mp4?token=Lz758UhTu0Rw_Fze6KJMdBFnea43_UjwU1fxe2fB7xCjFKVG3H53yy1wcSmauQwgTx5ck8jKLQp0_vSVPnztZT57bclgjPU94s0LbYoENloGSNipj6LUYzl8KAimCmE5hwVnT0L0UqyAjp8b4_sKdoOcelERq69vmQXQdvIs18U49gbXlDFzcbb2gVh05gShMuiEAkMmzVYUw_ESKGytxD--Kg-LplQlSRiOFQeHpuvQe5UuwKPuxjydtUwnWxTG3me-VPOlA5tgfq46bctk3udSew5Oj_C_FljFjsZluXfXic4h1Kf_XT-_RMIPZMNHXjahbMjRatzGmheDheSh26bryqDCFeZyDgrqiqz0ey4o8-gD4svGWhlI8gYhxcgk0uTx7Zo_b-ZHVBs74W50PPX1hu4oX7WnVCjK-yUxltiVZ34rP4gzMmXWIB2LbGQQ41azrbeyod3lsw5G23JF2yv8SzzMOu1wAusomKX_3xuceulkmkpa8YlPUJ_A3MlBoZnCmiUPZ51NLM4IKfETrbtvOWrm3aj-UkJ21jT9hPtT1wUw9T4GsefqtIo3TojU5T2f3tiKHuTuDgiK9u7DZpFUWzOpw3nVCJfnCO3gq1WnPGGwi8XrT2CKFjO_3fkRkt9kbNB_Hv9Z5Tax0bxAgCSJR6sBtqPQVJpImVYmpKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی منتشر شده از لحظه ربودن یک قایق ناوگان الصمود توسط نظامیان صهیونیست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/akhbarefori/652866" target="_blank">📅 17:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652865">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d0577e1.mp4?token=SlC-YxV5TwGQkmUb-vW4SwIt_S8b50NYPvhgvZw_zYceEK1NvxGjbks4ACuitr6ftdArK8Ah8SC-aDRTwGxOOTWBlpCftuNgq_GZOss3iXnoyx_9LbwMv-4Geo8-ijmQaZR7wwje-5k3i_YTefmuzQg6mqqxgYTcpLQY7hMoVT9GCHC79HPkm9pcsP-VfHo8NhQEC3eHFX-n9KL8KawqMiOR8RYmYxJul1jeRDyiZE10A0FtTMXCsnY4CjlVjc7slvPqF2BRZD63TPg5K6m0WDDDD3JS-OxcPpanPesVvvKZOKb-OuPLKB9HY9vhdlTFsproNhOTSDDuBIoQsdToeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d0577e1.mp4?token=SlC-YxV5TwGQkmUb-vW4SwIt_S8b50NYPvhgvZw_zYceEK1NvxGjbks4ACuitr6ftdArK8Ah8SC-aDRTwGxOOTWBlpCftuNgq_GZOss3iXnoyx_9LbwMv-4Geo8-ijmQaZR7wwje-5k3i_YTefmuzQg6mqqxgYTcpLQY7hMoVT9GCHC79HPkm9pcsP-VfHo8NhQEC3eHFX-n9KL8KawqMiOR8RYmYxJul1jeRDyiZE10A0FtTMXCsnY4CjlVjc7slvPqF2BRZD63TPg5K6m0WDDDD3JS-OxcPpanPesVvvKZOKb-OuPLKB9HY9vhdlTFsproNhOTSDDuBIoQsdToeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Stop scrolling. Start exploring.
Dive into the best Telegram channels—curated, categorized, and just one click away.
🗂
Add the entire catalog</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/652865" target="_blank">📅 17:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652863">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
لحظه هدف قرار گرفتن خودروی مهندسی ارتش صهیونیستی در دیر سریان واقع در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/akhbarefori/652863" target="_blank">📅 17:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652862">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec851f999.mp4?token=teA6MKQ6aOvA2-ZnKfLiMRakhTqi-YE7Lat-uh8MUAgGDiGR6_2GlHubtmmfhRJOuGLiyJvmIBap7SOLa3tkWgGGE6oD7CSKTzvqGaKNFyq1HY7owfS0cgZKDj7zL1NymN4u-RWfpRLiFK8LLusZ4Dd3s2DnYHMXUQCiI4XDqoHKQDvXokiJYOA57juFL9pQf55FPspJHBRcuX_TBf3xqHOvhakcc31RZkoOC9aYOVjY7D3h8shyYr8uetiO3w6f5ege4QKP-9PyqmYpd4hUUISNhOQgIlJCLJVdwqVOdrBgBUpEKBgMEISaHcgML4Wreq5bEX2MhPG3UXwYmgmmdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec851f999.mp4?token=teA6MKQ6aOvA2-ZnKfLiMRakhTqi-YE7Lat-uh8MUAgGDiGR6_2GlHubtmmfhRJOuGLiyJvmIBap7SOLa3tkWgGGE6oD7CSKTzvqGaKNFyq1HY7owfS0cgZKDj7zL1NymN4u-RWfpRLiFK8LLusZ4Dd3s2DnYHMXUQCiI4XDqoHKQDvXokiJYOA57juFL9pQf55FPspJHBRcuX_TBf3xqHOvhakcc31RZkoOC9aYOVjY7D3h8shyYr8uetiO3w6f5ege4QKP-9PyqmYpd4hUUISNhOQgIlJCLJVdwqVOdrBgBUpEKBgMEISaHcgML4Wreq5bEX2MhPG3UXwYmgmmdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری شبکه فرانسوی از پشت پرده انفجار مهیب و مشکوک بیت‌شمش در اسرائیل؛ مردم اسرائیل روایت ساختگی دولت را قبول ندارند!
🔹
خبرنگار شبکه فرانسوی BFMTV مستقر در سرزمین‌های اشغالی: انفجار در پایگاه ارتش و نیروی هوایی اسرائیل رخ داد؛ تردیدهای جدی‌ درباره روایت رسمی اسرائیل مطرح شده است و ساکنان اینجا سؤال‌ها و نگرانی‌های زیادی دارند!
🔹
چون این منطقه، مسکونی است همیشه قبل از هرگونه آزمایشی مردم را مطلع می‌کردند اما این‌بار هیچ‌یک از ساکنین در جریان قرار داده نشدند و همین مسأله نگرانی‌های بسیاری را به وجود آورده است.
🔹
در جایی که این انفجار مهیب رخ داد، تجهیزات حساس و نظامی نگهداری می‌شود از جمله کلاهک‌های هسته‌ای که در آنجا ذخیره شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/akhbarefori/652862" target="_blank">📅 17:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652861">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0569b312a4.mp4?token=ptzzvNDes8HPOpFZiJ7IUtMu6xMO_kAoe4XzrY0-ynqTzxMM6y0wcVhTVUIP0IRYvRJSs48ruPhiUseujDKhjIeUs3dhUbya9DUj7LjIA9V1zRrxTg0HKlZP_z1VO3kunXd6NUqk-qL9cazyzUtEEAi2aamJt6s15HVC9KSL8b7iosZDTsEFiTMkxsCiRUJM-G0jV8D0AiDFdO2jsWgwJdWasLK9KeF7qYM3B-j8qO4nRIr07-ZwXkJoUyMK-2wTk__gG1yDJjAYH5DoB2nuN6AGzx0Q6g9if7plgvIwCcNMUayhjQtsLwjJzXY_9o9eiMSMFvTl7TYcnuWRQrzR2wSeo2L_W_p0a0dpVsnhSsMgyuhn7DWJS33regPjNeqSKpjggA7GcL3DlMPWarFatOwBdYSnsJJxY_CujIYR7KzBWxk_Prwr57KeNT4N0MZqCWiKitFLL_KlD_ErCga2VpU6Dbxs0CZcGtxSHVtPyHYjeFTIvAladkWZRp18x50cuV2su9CHmVFLU9f6xrYSpuXbCegaWg9uCAUXFiMvUvHyWNwSwINtw-yT9ypq9kEbWkjciGubn_iRdfHkRqOI4M7Atu23aNXKN4YLkeKDeaI9nx7SiepoFVQ9QQ-orH0ncndoHfOO8JvKrT3vILK8OHyWQurkWp8h8SGDlXRP1Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0569b312a4.mp4?token=ptzzvNDes8HPOpFZiJ7IUtMu6xMO_kAoe4XzrY0-ynqTzxMM6y0wcVhTVUIP0IRYvRJSs48ruPhiUseujDKhjIeUs3dhUbya9DUj7LjIA9V1zRrxTg0HKlZP_z1VO3kunXd6NUqk-qL9cazyzUtEEAi2aamJt6s15HVC9KSL8b7iosZDTsEFiTMkxsCiRUJM-G0jV8D0AiDFdO2jsWgwJdWasLK9KeF7qYM3B-j8qO4nRIr07-ZwXkJoUyMK-2wTk__gG1yDJjAYH5DoB2nuN6AGzx0Q6g9if7plgvIwCcNMUayhjQtsLwjJzXY_9o9eiMSMFvTl7TYcnuWRQrzR2wSeo2L_W_p0a0dpVsnhSsMgyuhn7DWJS33regPjNeqSKpjggA7GcL3DlMPWarFatOwBdYSnsJJxY_CujIYR7KzBWxk_Prwr57KeNT4N0MZqCWiKitFLL_KlD_ErCga2VpU6Dbxs0CZcGtxSHVtPyHYjeFTIvAladkWZRp18x50cuV2su9CHmVFLU9f6xrYSpuXbCegaWg9uCAUXFiMvUvHyWNwSwINtw-yT9ypq9kEbWkjciGubn_iRdfHkRqOI4M7Atu23aNXKN4YLkeKDeaI9nx7SiepoFVQ9QQ-orH0ncndoHfOO8JvKrT3vILK8OHyWQurkWp8h8SGDlXRP1Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ بیهودۀ ترامپ با ایران به روایت رئیس سابق سیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/akhbarefori/652861" target="_blank">📅 17:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652860">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2WBNQcGGfRzprW8uygR-dCMAHpEO_ugC5T0uzJ63vbAYHhOr6dovwMzjF6N0dv5WYWPSRqOhjp76-z7VW-YE1Fza-R901HCILFhp3yixGqQ6VW4ZtHPR7-FsPBTFBROglV65LXSjIfrVb1v8PNvRZzlpmKlFoRsUXlx_VwggHprrmPwLl_iWbUIRzh2anNUle8e2puz-wZjl-LKoyC3lZ_r0di0Jfv3Bb8D6XBbvPOae4ztYHcsX5clLCsX8GhLzuC-pm2H5l19blWYht8HGh1KnnoumV9N-Qi_puPT-JgjMZPIqBgXk7thPFzanyohqBDAWWxqVHWsfyrJq1ChFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: آمریکا و اسرائیل در حال آماده‌سازی نظامی هستند
🔹
به گفته دو مقام در غرب آسیا، آمریکا و اسرائیل بزرگترین فرآیند آماده‌سازی نظامی خود از زمان برقراری آتش‌بس را آغاز کرده‌اند.
🔹
روز گذشته، رئیس‌جمهور آمریکا بار دیگر به زبان تهدید روی آورد و ایران را به حمله نظامی تهدید کرد. ترامپ تصریح کرد که ایران زمان زیادی ندارد و اگر فرصت را از دست بدهد، «چیزی از آن باقی نمی‌ماند.»
🔹
این تهدیدات، بار دیگر تنش‌ها بین تهران و واشنگتن را افزایش داد. مسئولان ایرانی بارها بر آمادگی کامل خود برای مقابله با حملات احتمالی آمریکا و اسرائیل تأکید کرده‌اند. با این حال، همچنان مسیر دیپلماسی نیز در جریان است و شب گذشته آخرین پیشنهاد ایران به آمریکا ارسال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/652860" target="_blank">📅 17:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652859">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
یک کشتی ایرانی دیگر خط محاصرهٔ آمریکا را شکست
🔹
یک نفتکش ایرانی تحت تحریم‌های آمریکا که ۲ هفتهٔ پیش در سواحل هند بود حالا در جزیرهٔ خارگ پهلو گرفته است.
🔹
این نفتکش حامل ال‌پی‌جی بدون اینکه شناسایی شود از خط محاصرهٔ آمریکا گذشته و وارد آب‌های ایران شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/652859" target="_blank">📅 17:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652858">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_7i6nmYVkBJMoRtKmqIDwKDOgi1lnjipw__-2G0Dxx2RqeCLXCX-QCPkESxla9BgyxCSAR1Zj4vIIc5fI-oW9pyEpNKYNspXpMAZ4LzSE5xTEfOZHooaInpse8tlT7J2STCheZwnY1gjg5PKY7fVAmxE75mrcSGeWZhrc4u7tSPGKW_gdXKE9z76bWXzAmulqKL42vfz5UUCUgOkCZ6kXBphERwLQPPON_adM1zNGtY_m2aTCevHQJ-tdRvZaQ99jMxRDqRJcYnhHLwZwaCnGoZCktr_INUb8FXf5nelcqkXzZKkAw8tDYIN42DOPlALNrALzkBR2m4w2I_yfhn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: وزارت جنگ آمریکا به صورت مخفیانه برنامه قانونی پیشگیری از کشته‌شدن غیرنظامیان توسط ارتش را تعطیل کرده است
🔹
دولت ترامپ در بحبوحه حمله آمریکا به یک مدرسه دخترانه در ایران، به قطع برنامه کاهش آسیب‌های غیرنظامی متهم شده است.
🔹
بر اساس گزارش بازرس کل پنتاگون، ارتش آمریکا مخفیانه برنامه‌ای را که به موجب قانون موظف به اجرای آن برای پیشگیری و پاسخ به مرگ غیرنظامیان در عملیات‌های نظامی بود، برچیده است.
🔹
دولت ترامپ متهم است که بودجه مربوط به مدیریت داده‌های این برنامه را قطع، جلسات کمیته هدایت آن را متوقف و بسیاری از پرسنل متخصص آن را اخراج یا منتقل کرده است؛ امری که به گفته بازرس کل، وزارت جنگ را در خطر نقض صریح قوانین فدرال قرار می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/akhbarefori/652858" target="_blank">📅 17:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652857">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رئیس کمیسیون اقتصادی دبیرخانه مجمع تشخیص مصلحت نظام: گزارش کمیسیون اقتصادی مجمع تشخیص با سناریو‌های مختلف جنگ نظامی و اقتصادی در حال تدوین است
🔹
پورابراهیمی: به زودی گزارش کمیسیون اقتصادی در مورد تحلیل وضعیت موجود اقتصاد ایران و راهکار‌های اجرایی متناسب با شرایط فعلی کشور خدمت ریاست مجمع تشخیص و مقام معظم رهبری ارسال خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/652857" target="_blank">📅 16:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652856">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO63KSQfTz5MieLWPO516hYLvKKaxriJDAGTiQtyT8D6_clPh8zmMNT7xJh6Jy8a3lRI1PIr6Xskx-TGL9OcL2F9_PpL29JmAAeK5XI6gxxsEMZpWz0ue8DTVxjrIxU3icIMH1t2QITuNXxZpaxd4KlTxUFwnU1LmtLlcxUOUYMwVc-3Uft5e-z4X3hv751I1upfjtlx0yNTxnY_pft7t9stMmOrtqqSgnKd8MfSFZ3fh_4EtD3rCoJyTKID_W27GJ6Fh4aVsPKQekM_Qw--ljbS_X_1htmIOa3kp2St13md-4Eldb1RxURzRlpC21sk0GGAmbfQEjIhrQnO1s-CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش کرملین به سخنان زلنسکی درباره حمله از خاک بلاروس/ برنامه سفر پوتین به چین
🔹
پسکوف، سخنگوی کرملین: ادعای ولادیمیر زلنسکی، رئیس‌جمهور اوکراین مبنی بر اینکه روسیه می‌تواند از خاک بلاروس به اوکراین یا یک کشور ناتو حمله کند، چیزی بیش از تلاشی برای دامن زدن به جنگ بیشتر نیست.
🔹
پوتین در حال آماده شدن برای سفر فردا (سه‌شنبه) خود به چین است و روسیه انتظارات بسیار بالایی از نتایج سفر آتی او به چین دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/akhbarefori/652856" target="_blank">📅 16:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652855">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
اعتراض ۵ میلیون بازنشسته تأمین اجتماعی به تأخیر در افزایش حقوق
🔹
با گذشت تقریباً ۳ ماه از آغاز سال، هنوز افزایش حقوق بازنشستگان تأمین اجتماعی به شکل مورد انتظار جامعهٔ مستمری‌بگیران اعمال نشده است.
🔹
بیش از ۵ میلیون نفر از این قشر زحمتکش جامعه، بر این باور بودند که طبق مواد ۹۶ و ۱۱۱ قانون تأمین اجتماعی، حقوق آنان باید بر اساس حداقل دستمزد مصوب شورای عالی کار (که پیش از آغاز سال تعیین شده بود) از ابتدای فروردین‌ماه اصلاح و پرداخت شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/652855" target="_blank">📅 16:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652854">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqEArXr4uh0-Yq5c8ZzLRDLPPZuNrg0hYggkDFSD0-SeVyNhX9nmQ4PXLq4E9-C9lz6PaVUpkFT3dxGmdoy3FJBJWvH1MjWTnVlT7CsOlNtGp68pJGbYeqhh9G4KVkv9anxSmiSSH7R-fdZewK8xEr7f11n1pLdY8uj4lsq90oq1IX0Ecgd47TkYrUfvvQ_-JIUrtPzm-Pw2G-jNzBrNTHV7_9V0cRdw2iHkTXWr8DchvOE8Qvj6LWZ5lzIDX46wO6CB4DR7Ny94VEqVSPrKCTqW2QnBPcgUKpf3DKdr7AAfg_-lQ1NueAozcbaXoTLU6xJg2m7KuKnYLyIeq7ldrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنها چند هفته تا پایان ذخایر نفت تجاری باقی است
🔹
فاتح بیرول، رئیس آژانس بین‌المللی انرژی (IEA): به دلیل جنگ تحمیلی علیه ایران و بسته شدن تنگه هرمز به روی کشتی‌ها، ذخایر نفت تجاری به سرعت در حال کاهش بوده و تنها به اندازه مصرف چند هفته باقی مانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/akhbarefori/652854" target="_blank">📅 16:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652853">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
براساس کسب اطلاع فرهیختگان ایران یک پیشنهاد ۱۴ بندی جدید برای پیشبرد مذاکرات از طریق میانجی پاکستانی به آمریکا ارائه کرده است ارائه داده است
🔹
تهران بدون عدول از خطوط قرمز خود ابتکارهای تازه‌ای را مطرح کرده است
🔹
بر اساس اطلاعات دریافتی، اکنون توپ در زمین آمریکا قرار دارد و تصمیم‌گیری بعدی به طرف آمریکایی وابسته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/akhbarefori/652853" target="_blank">📅 16:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652852">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/784a660e16.mp4?token=BPeSDnSGU6H8LVMWAhoZlhQzagzB6iehDl20iP9v0CaJxzSST0nykuEurpfi5a1YOT0vBastst5LBoD7-XaAK8TA4N6OBZUH1HYrsK0UoeWOtWb1N8N1RVuKvn-N1NcAlSGQr5_tuEiyD5fPkiYhqzAic5NcfaLq4NYHP_rDHc2MlsNQHZptF74BmNFUKapYGNzg8euynTSuD89K4q0AbeQhdmatu1EYtoW8Xi98k_nfRkNtjgPiuw2J3PkWUQ9sqqt2XpjrqOBUKQRBtnsnmp7Q0Ajcuf_SUA8p0wQfnyReo4S2YGVRkSFY8SL5wsmgQTyotVTJDmPJRMNqGFcxglXoxxrO5n3SXrTcyR8u-igSIapPX-xfG5fq1aK4dUijhqJvjsDGR2KPLpy6EvpFwjJx7t01o2Ja7e3Nrg1_b6Q9HIapAL3dm7OjvBROvtysaTC9_EFZ_u-DRFGknkZKxLBB4AJR_gU8alERd8iDz8cAaZEBBE6c3tm3XgRiquPnSKmHFWLIRCaT29FC700MS2MzW_iOWDOXW8r6elAG0VEPnrFrFdB1cRfH4N_fb4hrHYcAREwLW6uwUyf0Q2fDwO5FR4-v6huA1InXUY64RLDYOS-VrmtRwtqYujleSYgJER9jRGJp6uBtiHE5Wl4tte9Ln7F5N6po1ZUu_tHp6RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/784a660e16.mp4?token=BPeSDnSGU6H8LVMWAhoZlhQzagzB6iehDl20iP9v0CaJxzSST0nykuEurpfi5a1YOT0vBastst5LBoD7-XaAK8TA4N6OBZUH1HYrsK0UoeWOtWb1N8N1RVuKvn-N1NcAlSGQr5_tuEiyD5fPkiYhqzAic5NcfaLq4NYHP_rDHc2MlsNQHZptF74BmNFUKapYGNzg8euynTSuD89K4q0AbeQhdmatu1EYtoW8Xi98k_nfRkNtjgPiuw2J3PkWUQ9sqqt2XpjrqOBUKQRBtnsnmp7Q0Ajcuf_SUA8p0wQfnyReo4S2YGVRkSFY8SL5wsmgQTyotVTJDmPJRMNqGFcxglXoxxrO5n3SXrTcyR8u-igSIapPX-xfG5fq1aK4dUijhqJvjsDGR2KPLpy6EvpFwjJx7t01o2Ja7e3Nrg1_b6Q9HIapAL3dm7OjvBROvtysaTC9_EFZ_u-DRFGknkZKxLBB4AJR_gU8alERd8iDz8cAaZEBBE6c3tm3XgRiquPnSKmHFWLIRCaT29FC700MS2MzW_iOWDOXW8r6elAG0VEPnrFrFdB1cRfH4N_fb4hrHYcAREwLW6uwUyf0Q2fDwO5FR4-v6huA1InXUY64RLDYOS-VrmtRwtqYujleSYgJER9jRGJp6uBtiHE5Wl4tte9Ln7F5N6po1ZUu_tHp6RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقامیری، دانشمند هسته‌ای: روز اول جنگ گفتم کار تمام شد و عمود خیمه ی ما را زده‌اند ولی ساختار حکمرانی نظام چنان دقیق چیده شده که بعد از ۷۰ روز استوار ایستاده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/akhbarefori/652852" target="_blank">📅 16:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652851">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_E-Cuoa-B5JcdsLQNxzpXGAKI1KwK461bJxXxcJzHdWiuNI4fV74sR9EdWZF0uXU1RgVdT3qxccv0T_lL5XN5Qidr-dr1u-ytJMF3AhOHXIsEW-9PZBR2E2Ilkn8rdBwZV0DZNmaS43LKtU9Z4pHGAdM-PsrYadyuIcpAMqITiZSCH9qV61W0j93ayTIc7jrQJkHITlJ9pwP17Ul5fZTsZ7ATfHon3ULwSLN2OZzR8AkP9EWrVFKFBEZiaVCE0thwVHFS5pIkWYx_GMXZIJgdQGNiF61dBRR50NjMxEXAm8hcmk-BfUyOYyqP1J_xkSjYs7P1qYkXyoyviXcyQsTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشدید حضور نظامی پاکستان در عربستان در بحبوحه جنگ ایران
🔹
اسلام‌آباد در راستای توافقنامه امنیتی خود با ریاض، یک اسکادران جنگنده، حدود ۸ هزار سرباز و سامانه‌های پدافند هوایی را به عربستان اعزام کرد.
🔹
این مقامات امنیتی تأکید کرده‌اند که این تجهیزات «آماده رزم»، می‌توانند از عربستان در مقابل حملات احتمالی پشتیبانی کنند.
🔹
اسلام‌آباد در حالی حضور نظامی خود را در عربستان گسترش داده است که تنش‌ها بین ایران و آمریکا و احتمال از سرگیری درگیری‌های نظامی در روزهای اخیر افزایش یافته است. پاکستان همچنین نقش میانجی در مذاکرات تهران-واشنگتن را برعهده دارد.
🔹
شرایط کامل توافق دفاعی بین پاکستان و عربستان محرمانه است، اما دو طرف گفته‌اند که این توافق ایجاب می‌کند پاکستان و عربستان در صورت وقوع حمله، از یکدیگر دفاع کنند. خواجه آصف، وزیر دفاع پاکستان، پیشتر تلویحاً گفته بود که این توافق، عربستان را زیر چتر هسته‌ای پاکستان قرار می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/akhbarefori/652851" target="_blank">📅 16:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652850">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48ea2e889.mp4?token=N9-Qq8ERwRQ6QFntD2FUjpo0y7ydAEC45HagdWA_uE_5TeVDIVb9p06MD8fSzUgEfhsuqBkazJc5RDEpV0oydjmYuqG8wFCCieu0Tgv-KaxH_0h0ntXXfxMCNJcJlvF-M8NUKoVJZ55S-Y1bAu5aRDz6mzzjwmYFmtlzQU3arYSSmNnlFU5dnBAsYAKy4F0dObzLO9TQQeX-KYjStYGa4w0_lVK9Vm7WBUhGEkn2D6woFaKb-6bBVo-KDE9pCC0lEJNiowupRJToXWOEJ2BMkQ31n1SMewCTh6rHddDWl_9ovchAu7rDSv2CPDZcY90OEnEAdKsRteb3joHNIJsFgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48ea2e889.mp4?token=N9-Qq8ERwRQ6QFntD2FUjpo0y7ydAEC45HagdWA_uE_5TeVDIVb9p06MD8fSzUgEfhsuqBkazJc5RDEpV0oydjmYuqG8wFCCieu0Tgv-KaxH_0h0ntXXfxMCNJcJlvF-M8NUKoVJZ55S-Y1bAu5aRDz6mzzjwmYFmtlzQU3arYSSmNnlFU5dnBAsYAKy4F0dObzLO9TQQeX-KYjStYGa4w0_lVK9Vm7WBUhGEkn2D6woFaKb-6bBVo-KDE9pCC0lEJNiowupRJToXWOEJ2BMkQ31n1SMewCTh6rHddDWl_9ovchAu7rDSv2CPDZcY90OEnEAdKsRteb3joHNIJsFgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">*۲۸ اردیبهشت*
سال روز تاسیس شرکت *بیمه پارسیان *
گرامی باد
۲۳ سال آرامش ، اميد و اطمينان
همچنان در کنار شما هستیم
#بیمه_پارسیان</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/akhbarefori/652850" target="_blank">📅 16:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAfAUrqeld6EU6UJPTz8EkFlQd0dnrFXgceHlUEGk2h6bk8wLFxNs0W4jigJ66cuSdGlnsJMH3rDgm1kKnOr5S9i5qvVdGulnV67WbMFh2YW95LlclclL0tgNejfEcchyQx_yBI-lbD_0ViareqkB4KLVT2bQ3rcvfxbstog7aqgwPN2nXBnpb9XZ-MvM1PN75FTHxmKBOV5q0_rcaHdfiPM03rgzIKXdD8hEeXFbOHr5k4Sr1HOzi0Ffda7gZdj-dNQ0Z8wnTSxq7zMyFdDRHg3vWRX8adHJwv3qj-KcOwn2ihnMPTRcb2FDL8A6mjZWKdGC_ME97P7y557n5Ta0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت وضعیت «سلامتی رهبر انقلاب» در روز اول جنگ
🔹
مدیر مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت: وقتی که ایشان به بیمارستان رسیدند، متوجه شدیم که رهبری یعنی آقا مجتبی را به بیمارستان آوردند.
🔹
همان موقع که خبر به ما رسید به این فکر افتادیم که چگونه باید روایت‌سازی کنیم. همه جای دنیا در حال ساختن روایت بودند. برای ما کار خیلی سختی بود.
🔹
اتاق عمل آماده شد؛ دوستان شنیده‌اند و بارها نیز گفته‌ایم. اقدامات لازم انجام شد. خوشبختانه اتفاق خاصی برای رهبر انقلاب نیفتاده بود. فردی که در محل چنین حادثه‌ای باشد، طبیعتا چندین زخم بر روی بدن خود خواهد داشت.
🔹
این زخم‌ها نیز زخم‌هایی نبود که بخواهد چهره رهبر انقلاب را مخدوش کند یا اینکه همانند امام شهید ما جانبازی بگیرند یا قطع عضو داشته باشند.
🔹
چند تا بخیه در محل جراحات زده شد. بخشی که همانجا تصمیم گرفته شد که بخیه زده شود روی پای ایشان بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/652849" target="_blank">📅 15:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
مبلغ کالابرگ به دو میلیون تومان افزایش می‌یابد؟
🔹
فلسفی، نماینده تهران: مبلغ کالابرگ برای برخی دهک‌ها حتی تا ۱۰۰ درصد هم قابل‌ افزایش است حتی اگر لازم باشد قانون بودجه ۱۴۰۵ اصلاح شود، این کار باید انجام شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/akhbarefori/652848" target="_blank">📅 15:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
محدودیت واردات کاندوم به کشور/ فعلا کمبود کاندوم نداریم
محمد هاشمی، سخنگوی سازمان غذا و دارو در
#گفتگو
با خبرفوری:
🔹
ارز کاندوم غیر ترجیحی بوده و مشمول قیمت گذاری دولتی نمی باشد و براساس ضوابط سازمان حمایت و هزینه های تولید قیمت گذاری می شود.
🔹
به دلیل تولید بالا در کشور، برای این کالا محدودیت واردات اعمال شده است.
🔹
میزان شناسه گذاری تولید در سالهای گذشته ۲۵ میلیون بوده و در سال ۱۴۰۴ بالغ بر ۲۹ میلیون عدد تولید شناسه گذاری شده است.
🔹
هیچ گونه کمبودی در این خصوص اعلام نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/652847" target="_blank">📅 15:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652841">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBaVtF_FRcqsDePj73TxaMJ0H9hrfaaSa_oPt8jiFxZ_z6EFp_JPKlj1EL7r-A6cF2CLazVlnguzudDCnRv6QWZ2jgUkkgm98LoEACsq1R9WKQdSHwk4PwZ1LpHL8dVLStrJSen32v8fLzCNY5No5N-yP2dbxMsGq4rsewFtbfm0EU4kIl11_czwIMIGDOeiNgFcNcJM-dLe73EK3ptZaIirBr_aH9-fzIEe5RUFMlc1-gTT5yxY761KriV9XwXdhfKSLfDfbhy3cQkyJ4bZxmflusuLi6xabbdfw3f2VPxh0hvh7IJYpUBOkeHo1jooUVeIsAL2mD4LQv8r7u1dIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zwdb5ZnPE_OBhifPhAYDMc2gvzYWjceu-OGt4OBZrZi3xBMXWKUpCZyzchxQcvtK9_MV7ZRm6gToJLHzU_HA4XyuEW23EPnQu_tLVFHJY6GfeYVYrl7WtoezbQ76cPGWtW6uxSNuUT0oXykJgrYuXQowSmxpVVUW7wij1hRPiMli2w3rX9XdTUHCpm0CE0GzScJLfkSkASbBj4B4JkpIF8sZUWzK1VtcjN_sddxUtzMfhA53Zl8jYNsEnb81rFfvUUIYDY1c7UvlbQga8LESiPxth5D99SNea61vPJdkO1h0TmqeAEbZRXIip4wDyTPXBF4RdI-ZTLq0pMLYRFUydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjlNgNOnCwnUC4WTMY30mbEJZxgmdXOe1AE679mXW-caao4ZaZ7ZjEudJbhikkm64MpfmRiUcft0yNOSmjeTPgEAkYYTsOi2HcP8L08_sqDwmDK88ABmQh4k-LD6Jn9RLbtfjP7OPN3qT2FuxPAFvrp_KzcAm22yXh6u6QakrdTOGF655BjJtcISemGngyNdPhM2YIqQc21zh_f644KdGDzuwmX-SkZbDTfBZneW6CWLqcHqxLszSbRRT8m405YDJJ5PT4nIOyTzbyXWDsAl3Kyb7xdmtPE1PoJLtbxZmVQtZLRq98yTPgK9QRDrJY2_FUB_MuAOz0ZQjRtZGAmk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHcvvfmmWUqH4vye-TGLhkZBohhTT_9qjRojJFmZnd-6EQiKhsdYGYCL-JVFBgSvdLXqdevaKcNkK4J16PTHkKziE5RIcaF2139m_MyLI3TVEtp-JSz0mmd1Z16BXAw54OpkTVuJaBtt9HSlDlaIIx9wYjznrqac6KzTi3Na-F0getTGqnTnKBu7rmf0FlJXCoPI-0XInrMHemguVuygTunR_B_zqqkc2txIaLPfJhbwn5Uvq49nFD2NRlHtse7zb44gXliQjzBaSdFAMVFgvp4a7m0CPvKmeHP-Prsu1ogvRrq5NSOD2HqqDsz3adO4U1zt62wwQgeufFBy6JZPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4S8zqn6VJ3H-KT1qwihw9L-N1Z8BIIVRXVPmFPrFiKkaPBHCz0QJL39LXEE_Ayrrcb4MXGuV79OrLPeweq391SbQAuTEktTxDcS4BTDPkqvmDZiwaRhA054ibVSQ7EkCPSAGktGitNQaimMKwv-wSv1MaAkxcqGBv3kZXvT98tueUXfWWFuThq_HsXrq4KF0zUOslezJnhQ3NWwMT5R-tIQExY4MDynefOm-oDWh0QkqJDradp-TS1x7nDaS8JuXVqHJui2MBnIvZDVY7M_m_gwK6IbhBSFXxAGCEDurOjfAgGmjGXnHdKl3uecTWVDsPbRbmLwdPy9ahfwVP97Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaA9519Dr4Jj8x8JR0pcbJr4WNBcKiGn9wZpDLjDD8HhivGzFsD_4iahCQ2ZX-5Q3DtVoRYQUAygrKkuM7lJkyEDdeosc57TWxu7cpo8814Mn9P-kJjMUWNyrmSQiyRqJG5jZ-YTcsEuDAkVTfMcUMbUE244iI5vFKsMEGxR6JwXTc1byFqq2B4XCIHxDsCiQJVEnZlzH2ThyLHyoVsUdqw5D4m133btOK8dEY-Vp3g7AmMAwQBVRL7jj1SVZj-UaFwUMB7Zkpq9Wq0Cree_Y44HD0nP9i-2Zc2LYsDyJtDNM8EXcEnDwZG4767n7i2HiBCXfkDF6wClbOWij0jNAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم یادبود شهید دکتر علی لاریجانی در مسجد بلال رسانه ملی
🔹
مراسم یادبود شهید دکتر علی لاریجانی با عنوان «صمیمی با انقلاب»، ظهر امروز دوشنبه در مسجد بلال صداوسیما با حضور رییس رسانه ملی دکتر جبلی و مقامات لشکری و کشوری برگزار شد.
🔹
شهید علی لاریجانی دبیر شورای عالی امنیت ملی و رئیس اسبق سازمان صدا و سیما در ۲۶ اسفند ۱۴۰۴ درپی حمله دشمن آمریکایی صهیونی به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/akhbarefori/652841" target="_blank">📅 15:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652840">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
حملۀ تروریستی گروهک پژاک به یک معدن در سقز
🔹
حوالی ساعت یک بامداد امروز گروهک تروریستی پژاک با سه دستگاه خودرو به معدن میرگه نقشینه در سقز حمله کرد.
🔹
در این عملیات تروریستی ابتدا دست و پای هر دو نگهبان معدن را بسته و تلفن همراه آن‌ها را خاموش کردند، سپس اقدام به آتش زدن تجهیزات معدن کردند. مهاجمان پس از حدود ۳۰ دقیقه محل را ترک نمودند.
🔹
براساس گزارش اولیه، یک دستگاه لودر، یک دستگاه بلدوزر و ۴ دستگاه کانکس شامل امکانات کامل رفاهی، ابزارآلات، وسایل تعمیرات، قطعات یدکی ماشین‌آلات و موتور برق دچار خسارت شدند.
🔹
چند بیل میکانیکی و خودرو سنگین نیز مورد هجوم این گروهک تروریستی قرار گرفتند. هدف تروریست‌ها باج‌گیری به وسیله گرونگان‌گیری نگهبانان بوده است.
🔹
گروهک‌های تروریستی و ضدانقلاب با هدف جلوگیری از توسعه اقتصادی و اشتغال‌زایی در مناطق مرزی، زیرساخت‌های حیاتی را هدف قرار می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/652840" target="_blank">📅 15:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652839">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk4k71EV_j58GeJNjE2Dd_SOteZD9ZIENZWX4UMTcLWbZO2f4q7D63vczPxi7PVr6OEyKL6pB93Em_a0soWnoM_XEUxnR6QPRB34KnxAEJl50fvgz1qfq51Tj1JouL54omJiZk9obHu7Y0YXOEmMbZuzpmEYGHHN7s4zTWEAhdfC4LuSAsDOoRLkH9Gq6H3D8XhcLpVstS_k5uvfAy5JzC8MkfAaO-bWUlYQEbbOi44PhWP7-y53E-I7RT6fVVmLLCscKCLzPn9_j_96E6hWrra7TDxnc-2wxnx-hlWGZWgTJqyaZN-K5oMzFs8zJD63NrlvHq9JG5xBmc8Crjc2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدارهای حملهٔ هوایی بر اثر حملهٔ موشکی حزب‌الله در شمال فلسطین اشغالی فعال شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/akhbarefori/652839" target="_blank">📅 15:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652838">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سرنگونی پهپاد آمریکایی MQ-۹ در استان مأرب یمن
🔹
رسانه‌های محلی یمن از سرنگونی یک پهپاد پیشرفته آمریکایی در شرق این کشور خبر داده‌اند.
🔹
پهپاد MQ-۹ Reaper از پیشرفته‌ترین پهپادهای شناسایی و تهاجمی ارتش آمریکا به شمار می‌رود که برای مأموریت‌های نظارتی، جمع‌آوری اطلاعات و حملات دقیق به کار گرفته می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/akhbarefori/652838" target="_blank">📅 15:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652837">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-SxJvgHkEbAfQTlmOcQV2IipwhRRVr7W7Fs0zRkREBdCpri2zUc7wHOn3Wk-Eci4Tow4EXyQLNT-_yrb5NaJdbZqtJMrKRAm7amnq2Wk2pZ227ot0mGs8hkThIN-PwpH-vn6hA83JvufFuXCvANbjdu7ipe3scCtoh7p2q5wcZhPGXSgJTPje9tdgrlTXu73c2oXxSnCnpBJr5gR03NO0S2hpoVR8zeLoH3pBfBcZHtudzubuOhhDk5Wb3_8Jnp5Kr84zhMEymgfN_c_BeqPGBT3EqZ2RjbPt4ScE_MY8BKJygwINVxPAPV6ye45fudbscl4FFdw__j__fiYX4aDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات پیشنهاد جدید ایران به آمریکا به روایت منابع غربی
🔹
خبرنگار کانال ۱۲ اسرائیل در توییتی مدعی شده است که در آخرین پیشنهاد ایران به آمریکا هیچ اشاره‌ای به مسئله تنگه هرمز نشده است.
🔹
آمیت سگال، از خبرنگاران کانال ۱۲ اسرائیل ادعا کرده که پیشنهاد جدید ایران شامل تعهدی — با ارزش نامشخص — برای عدم تولید سلاح هسته‌ای است. این خبرنگار همچنین تأکید کرده که در این پیشنهاد، هیچ اشاره‌ای به مسئله غنی‌سازی اورانیوم نشده است.
🔹
جنیفر گریفین، خبرنگار فاکس نیوز هم این توئیت سگال را بازنشر کرده و بر وجود این موارد در پیشنهاد ایران تاکید کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/652837" target="_blank">📅 15:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652836">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
آمریکا در متن جدید خود اسقاط تحریم‌های نفتی ایران را پذیرفته است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده در متن جدید پذیرفته‌اند که در طول دوره مذاکره، تحریم‌های نفتی ایران را Waive کنند.
🔹
ویو کردن تحریم‌ها به معنای معافیت یا اسقاط موقت تحریم‌هاست.
🔹
ایران تاکید دارد که لغو همه‌ی تحریم‌های ایران باید جزو تعهدات آمریکا باشد. آمریکا اما اسقاطی اوفک را تا زمان تفاهم نهایی مطرح کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/652836" target="_blank">📅 15:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652835">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وزارت اقتصاد: مهلت ثبت‌نام در طرح اعطای تسهیلات حمایتی به بنگاه‌های آسیب‌دیده در جنگ به منظور حفظ اشتغال تا پایان اردیبهشت‌ماه تمدید شد
🔹
تاکنون بیش از ۵۱ هزار متقاضی در این طرح ثبت‌نام کرده‌اند که حدود ۴۰ درصد از آنها مشمول دریافت تسهیلات شناخته شده‌اند.
🔹
افراد می توانند با مراجعه با سامانه «کات» به نشانی
kat.mefa.ir
برای دریافت این تسهیلات نام نویسی کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/652835" target="_blank">📅 15:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652834">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
رئیس‌جمهور در نشست تخصصی با مدیران وزارت راه: پایداری تجارت و تاب‌آوری لجستیکی، خط قرمز دولت است
🔹
پزشکیان استفاده از ظرفیت کشورهای همسایه در توسعه زیرساخت‌های حمل‌ونقل، ترانزیت و سرمایه‌گذاری مشترک را از محورهای مهم سیاست اقتصادی دولت عنوان کرد.
🔹
در این نشست، بر شفافیت در توزیع بار، افزایش هماهنگی دستگاه‌ها و تقویت زیرساخت‌های لجستیکی در شرایط جنگ اقتصادی و تحولات منطقه‌ای تأکید شد.
🔹
رئیس‌جمهور رکوردشکنی در جابه‌جایی کالاهای اساسی، بهبود تخلیه و بارگیری بنادر و تسهیل عبور کالا از مرزها را نشانه ظرفیت بالای مدیریتی کشور دانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/akhbarefori/652834" target="_blank">📅 15:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652833">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
دامداران در انتظار افزایش قیمت شیر خام هستند
🔹
نایب رئیس کمیسیون کشاورزی اتاق تعاون: متوسط قیمت خرید هرکیلوگرم شیرخام از دامدار  ۵۰ هزارتومان است در حالی که حداقل قیمت تمام شده هرکیلوگرم شیرخام برای دامداران ۶۴ هزار تومان است.
🔹
با استمرار بلاتکلیفی اصلاح قیمت شیرخام و زیان دامدار، تولید شیرخام کاهش می‌یابد و دام‌های مولد روانه کشتارگاه می‌شوند.
🔹
با اصلاح قیمت شیرخام و حمایت از دامدار، تولید شیرخام به بالای ۱۳ میلیون تن می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/akhbarefori/652833" target="_blank">📅 15:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652832">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a808ae49.mp4?token=O4_XEYXyzMFdHa5SMnAr0uXsJouOrXchqIJJIyEzWtdfjwHksv-taCI8e_lZ07n9sxx3enxNjY0v3Q71m8fro-x3vYCbeqAQy92wXer6KXvTXzKlrb1VGkYQqWrxPi8KpFfZ99oxaGO80XjiACIbYcGvrFiEuT_0_4DYxxIxGp5VkRl12HR3-tHTi2wDdSeOfGSaW3UU9pP_VDZNPDZX6SpgZkL8qCNZEs_d48Ns9jZ6rp5GRSBEVQsUSFpq73-El1LRqFvUqMCqXTtDipo3ez0jckJ7OGlzq5_2pjYQ98O-QHnMyOicvNJhAXTy_2lkTWmVQYJU_L_dJzrZSL0WDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a808ae49.mp4?token=O4_XEYXyzMFdHa5SMnAr0uXsJouOrXchqIJJIyEzWtdfjwHksv-taCI8e_lZ07n9sxx3enxNjY0v3Q71m8fro-x3vYCbeqAQy92wXer6KXvTXzKlrb1VGkYQqWrxPi8KpFfZ99oxaGO80XjiACIbYcGvrFiEuT_0_4DYxxIxGp5VkRl12HR3-tHTi2wDdSeOfGSaW3UU9pP_VDZNPDZX6SpgZkL8qCNZEs_d48Ns9jZ6rp5GRSBEVQsUSFpq73-El1LRqFvUqMCqXTtDipo3ez0jckJ7OGlzq5_2pjYQ98O-QHnMyOicvNJhAXTy_2lkTWmVQYJU_L_dJzrZSL0WDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشنگیِ ریشه‌هامون به اینه که تو اوج سختی، آشتی و همدلی رو یادمون نمیره؛ برد واقعی یعنی همین اتحاد بی‌قید و شرطمون
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/652832" target="_blank">📅 15:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652831">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwTtUffmtSgARsvdLS7irLzajnGpUjqOlLp9HXHySLg1ZgYg-QGdN3O8pGSoxdkfqtsUSI49P1pDDUsYVXddcTR6olzliB3F5tOCxrKEAf-EoTPgGR3sl0Yw3TyFn6TJrpzIZjCx5dlteIZfimfjZ7p_sIUcfyIv78v5JVmxisNXmPNFGe1Unuia3-0Yb97c28lH2KBmSqKS6uAaQgyfmJ_8tu6O1-BH-Vc1xwu_if9mDmXatUL_1NZgFM_OFeT-u0mX0n2epGqAvDZ_rJBuJ1gU8YlwbS0RPCiJWJpZet_BBB31zkAzcXi0wUOcNTbyEHGlcOakZehEZl9tOzOeaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر بطری و هر نی پلاستیکی، ردی طولانی در طبیعت باقی می‌گذارد
🔹
بیایید مسئولانه‌تر انتخاب کنیم، تا فردا زمین قابل‌زندگی‌تری داشته باشیم.   شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/akhbarefori/652831" target="_blank">📅 15:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652830">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jluthzxAiO7t4yrpFoQvz40lBkC7nXky_9pDixN2zDOekhOk6OB8vzZnOITNp_-ZLcPlAAoxfD3oL3M1VUExt00aIfcyuLUeDDcIVagUjo5RZilplGbZ6ypi79CwT6LaAciWhymXhwa4HugpCEu3KgqAaeK0JAogherypH_4i8z_XDiquOArhCxTtdd5VAKSYtYY0IUEuaAp7TxqrxKCkJd33lqVaWa6OoBOu3bxZaPwWp__rMcN3ZL7YR5y8iesT2KzV9NshuSIrCL8yHajuAAwA1rS_SfIXMn7Ch99I1Hkoriic78TpqFYXKZ3Bvh-y0onRb1UBxGfBC2A6bVrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای سبز ایران قفل اروپا را شکست
🔹
اتحادیهٔ اروپا پس از ماه‌ها مذاکرهٔ فنی و سیاسی، محدودیت‌های وارداتی پستهٔ ایران را لغو کرد.
🔹
این محدودیت‌ها از سال ۲۰۱۹ به‌دلیل ادعای وجود باقی‌ماندهٔ سموم و آفلاتوکسین اعمال شده بود و باعث افزایش هزینه‌های صادرات و کاهش قابل‌توجه فروش پستهٔ ایران به بازار اروپا شد.
🔹
به‌گفتهٔ معاون امور باغبانی وزارت جهاد کشاورزی، این تصمیم می‌تواند زمینهٔ بازگشت گستردهٔ پستهٔ ایران به بازار اروپا را فراهم کند.
🔹
برآوردها نشان می‌دهد صادرات پستهٔ ایران در سال جاری به ۲۵۰ هزار تن برسد و ارزآوری آن از ۱.۸ میلیارد دلار فراتر رود.
🔹
همچنین بازار چندصد میلیون یورویی پستهٔ اروپا دوباره در اختیار تولیدکنندگان ایرانی، به‌ویژه باغداران کرمان و رفسنجان، قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/akhbarefori/652830" target="_blank">📅 15:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652829">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlutIe2LDLQitxrphUp2_Q220OTNxgOEg9_lu_UcjMJFnK7sM-oSKS8YR8GQUyfIYUBxeyFwHxgcIw_YLPHrWV0srhBujo-zHf0fhM40aOu_rYBt7v23ndWe750Sy5qNlRG45YnM0SIWs0cASCKy6SIqMSp_Ca35YgksYyylDfTzYD9SwjDSUVkyxq2gQ_yIKYPYaH8uKhTZwCm0zskPAGvv7yvWxbIfIZbr-rb8nZgjz4meO7fALntIMtwQhuuwZq81NQ42cR0XEZy8xJ-E5S6iyRRO-hMFzCusEJOXSsAo3_2HrLXANplPLtwtg-o3c4fbAE_wzT5DDTYkAhACzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور گسترده نمایندگان در جلسه مجازی مجلس؛ خانه ملت بر مدار نظارت
🔹
برگزاری دومین نشست مجازی مجلس با حضور ۲۲۶ نماینده، بار دیگر نشان داد فعالیت پارلمان در روزهای جنگی متوقف نشده است.
🔹
در این جلسه که با حضور وزیر تعاون، کار و رفاه اجتماعی برگزار شد، نمایندگان مسائل معیشتی مردم، اجرای کالابرگ الکترونیک و حمایت از تولید را بررسی کردند.
🔹
همچنین از آغاز جنگ تحمیلی سوم تاکنون، بیش از ۱۰۰ جلسه کمیسیون ‌های تخصصی مجلس برگزار شده و جلسات نظارتی و بازدیدهای میدانی نمایندگان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/652829" target="_blank">📅 14:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652828">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
محدودیت برق برای صنایع تابستان امسال اعمال خواهد شد؟
🔹
عباس علی‌آبادی وزیر نیرو در پاسخ به سوال: صنایع کم مصرف و ضروری که منافع زیادی برای کشور ایجاد می‌کنند در اولویت هستند، کسری در صنایعی که برق را با راندمان پایین‌تری استفاده می‌کنند، اعمال می‌شود.
🔹
اگر صنایع اصلاحات لازم را در مصرف به عمل آورند تلاش می‌کنیم نیازمندی آنها را در اولویت تأمین کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/akhbarefori/652828" target="_blank">📅 14:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652827">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
طرف آمریکایی اعلام پایان فوری جنگ در همه جبهه ها را پذیرفت
🔹
پیشرفت قابل توجه در مذاکرات پایان جنگ رخ داده است
🔹
یک منبع آگاه نزدیک به تیم مذاکره کننده پایان جنگ گفت پس از چند دور تبادل متن بین ایران و آمریکا، متن‌های دو طرف درباره پایان جنگ به یکدیگر نزدیک شده است.
🔹
بر این اساس، طرف آمریکایی اعلام پایان فوری جنگ در همه جبهه ها را پس از امضای یادداشت تفاهم پذیرفته است.
🔹
ایران پیشتر تاکید کرده بود جنگ باید در همه جبهه ها از جمله لبنان پایان پذیرد و متن جدید ایران هم بر همین موضوع استوار است.
🔹
پیشرفت مذاکرات در حالی رخ داد که آمریکا با این ماده موافق است و اعلام کرده پایان این جنگ پس از امضای یادداشت تفاهم اعلام می‌شود و در طول ۳۰ روز درباره ترتیبات آن و شروع نشدن مجدد جنگ گفت و گو خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/akhbarefori/652827" target="_blank">📅 14:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652826">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwfGL5Syx2ghKhyvaAb_YYb6mcb3bCtmLq_xqB2AmA2rMYQfmBzNmrCUU67tSE_GKM8rcNpuClGGpJNsGK5kxX4-nnfoxKHIVwftoUeV8PfkAVM2D1120Rtrf3ja7F8BWKowjCR4_6zn55JrA0AXSAnd80q9BRlpQdEVE_pL7Fq8wHeGkgNMEdcAI6wfbS1oEWAH1dW-5nL9Mfl22fuvO5DOZgkTk53JZR8EmmSSZXRJZYH79DQoGvOuCzQtFtKM1TaMCdDvfXZAwUL6X-qbFgZ8tq2_7pbKT5AC_gKEAK6Ua0mErfQgJqdFXszPvVgTkPgWiNchsho11lCb6ZXldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه و بلاروس رزمایش هسته‌ای برگزار کردند
🔹
در شرایطی که تنش‌ها بین مسکو و بروکسل رو به افزایش است روسیه و بلاروس رزمایش هسته ای برگزار کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/akhbarefori/652826" target="_blank">📅 14:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652825">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3615db4f22.mp4?token=P4IvlTG2917nI0YuQPydT_9C_Nk8LsPMi8tpDANksgD_ghOPVT4rIsbcxMIkAfdr1jeBFzK5r_9lr_izZWzO46xsNzJMngdJUJuo_EkfDKrloWMlDKoEizl69jSb3f9_y01N_fJjI5du3ncMx_PNat1qVQCTVHW0GYcSUD2ZilYyAepmfxKhGdJ8SmMmxa7V0CVaStejxzSFkcnmv3oxqHtvdep1gsopVD4e84QJXki5tUIogfCnfeYxrtXc7-XsPM02O36Lumo3U_X_RrJ_5e6JTO_Rf9AcDyE7HCM-szvyOnehbuf4AMPsIayuhRJFjadr-Qk7RymjtGq7BB5xHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3615db4f22.mp4?token=P4IvlTG2917nI0YuQPydT_9C_Nk8LsPMi8tpDANksgD_ghOPVT4rIsbcxMIkAfdr1jeBFzK5r_9lr_izZWzO46xsNzJMngdJUJuo_EkfDKrloWMlDKoEizl69jSb3f9_y01N_fJjI5du3ncMx_PNat1qVQCTVHW0GYcSUD2ZilYyAepmfxKhGdJ8SmMmxa7V0CVaStejxzSFkcnmv3oxqHtvdep1gsopVD4e84QJXki5tUIogfCnfeYxrtXc7-XsPM02O36Lumo3U_X_RrJ_5e6JTO_Rf9AcDyE7HCM-szvyOnehbuf4AMPsIayuhRJFjadr-Qk7RymjtGq7BB5xHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما بلدیم تنها بمونیم... ولی تنها نمی‌بازیم
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/akhbarefori/652825" target="_blank">📅 14:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652824">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
منابع موثق خبری از وقوع یک انفجار مهیب در ورودی تنگه باب المندب به دریای سرخ در شب گذشته خبر می‌دهند
🔹
سکوت موسسات خبررسان دریایی و شبکه‌های خبری غرب در مورد این انفجار بزرگ در این آبراه استراتژیک جهانی محل تحمل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/akhbarefori/652824" target="_blank">📅 14:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652823">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFMl5Wu_eDqaRivwW9VkVsWt6JqF6zpYRtkckT5I93E6PgWu6dyDQGc7phdyhSfUEyrK0N6pUXvY-ah2STNaV2PPlGdkS6MvWUSI-Up5SJCZF9TXbczYT0WHl4YxX9Rf9oejBSt4vsThEcy4xubM-wVZeNTk-6QzFtvnjIIFQyPVDb_w49iv1jlazoHL4U8KVv_XY-rSuw9n64fVhfkce9vrKjhA_eyrJ7Sqw6m-s05eY7J0Ppd2GfsXXZe7b9xX0cC9ZoDXpdku9o6sbl2TB2PefEmL0kpy0w6tJ6AFfq86oHvcaqRW2lw8R9ljlhEIgQonNbaQPi05m8biT9sRjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده فعالیت برند پرحاشیه؛ از کارآفرینی تا اقدام علیه امنیت ملی
🔹
پرونده صادق ساعدی‌نیا، مدیر یکی از برندهای شناخته‌شده صنایع غذایی، در دادگاه انقلاب قم بررسی شد. او متهم است که در اغتشاشات ۱۴۰۴ با فعالیت‌های تبلیغی به تحریک ناآرامی‌ها کمک کرده است.
🔹
صادق ساعدی‌نیا، وارث یک امپراتوری غذایی است که پدرش محمدعلی ساعدی‌نیا از صفر آغاز کرد. اما این میراث نه سرمایه‌ای برای خدمت، بلکه اهرمی برای ضربه به امنیت کشور شد.
🔹
او در جریان ناآرامی‌های دی ۱۴۰۴، به جای حفظ آرامش و حمایت از تولید و اشتغال، با تعطیل کردن کافه‌های زنجیره‌ای خود در سطح کشور و انتشار گسترده استوری‌های تحریک‌آمیز در فضای مجازی، مستقیماً مردم را به اغتشاش و مقابله با نظم عمومی فراخواند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/akhbarefori/652823" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652822">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3311ac51c2.mov?token=obSIdbPa4-N7ApRDLB6lyZ0ZvfaqDWPMGqVbWXOhjzBIgWJE5ycE9Czwv9QLQGkxEDF5xweYzW6xlugKWwxEZxhosmv4DR1AS-pstVsKjvXBsTLpgubJB3zI8FyB3oTZQnQS4hdmiNjgaRfNDihK2CgZc5EF3qdf2oqlzH4EgHFvsMW00XSnL6reuqzdwJ0-onorXrNtkKHsEJ91Q3uy4T5bBNcfrvhwV8JHCA_EkjWZHtuCZGzVbveyKWkYdLY96-R_8n5w8hXmhRTN4LWSrTx7l2P1wOA8by50UgsmnqS19NPSeff6NJYEWTRFgPTdIVA-uh9w5nTuAsepyPVpDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3311ac51c2.mov?token=obSIdbPa4-N7ApRDLB6lyZ0ZvfaqDWPMGqVbWXOhjzBIgWJE5ycE9Czwv9QLQGkxEDF5xweYzW6xlugKWwxEZxhosmv4DR1AS-pstVsKjvXBsTLpgubJB3zI8FyB3oTZQnQS4hdmiNjgaRfNDihK2CgZc5EF3qdf2oqlzH4EgHFvsMW00XSnL6reuqzdwJ0-onorXrNtkKHsEJ91Q3uy4T5bBNcfrvhwV8JHCA_EkjWZHtuCZGzVbveyKWkYdLY96-R_8n5w8hXmhRTN4LWSrTx7l2P1wOA8by50UgsmnqS19NPSeff6NJYEWTRFgPTdIVA-uh9w5nTuAsepyPVpDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در صورت کوچک‌ترین خطایی از طرف‌های مقابل، ما به خوبی می‌دانیم که چگونه پاسخ دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/652822" target="_blank">📅 14:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/828df3711c.mp4?token=CkADPyNXzc4s8sQdFfLCw9bLT5YnkoMGqz0fPsxPU2hkZ2GS--pLXHFxlJQxQodDiViB2Ronm5cqQ4AGvqvPzo9hKUxL8LKC2uNDQ0waPGhUAXYKh8Tja9cPMgcS6WG-948QuCd25QL_tm-rAHAN4EEG_MH1HtEmz3DnU7trWrPky6MAYZb4xfTI_Csph_m6CeVJrL5gUOaUdyOgcLhZ0Pk4mARNij4gM80v1we9eJp7AwibP-_FYZz_aA5I_He1qO_g1G-BIjfBAuRp2XiLXLWbpSLCCoG17DVsMTwQ28-lX5xYT2SfRyrmwMsWeS7N4dZxXkk-h_86N9-0D8TVE4RGRmoiyVbeLnvrgS1OkshV8PgbHoQlfNiMEe9_rxRudImG4Lm42-LoxLYmTA2tw6XBe6xP9u3El6iWdKM2HH8BoYGZneHzHRGleru3Mf1jROcPugFZGev6E13zH-joBBs34CYb2r4SaPsBG7u-KBGs0Zf_Caj-VCMWH3wQrCxLuKPesXzzNmbNvdPC3aE-jXZM3kYMofmJ_MeEj3HdIdyOuP3ABd5YfXFNjO-MeVVoItztoVvcstVccjjWhGBckXLREhev_rzBKQkygyx0n2RsxbwpIr-Lfh-9HoOFxncBkiL-dxcJJuF_02sPP2X-gDWdOVVSQQMExFZj9cRwO6E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/828df3711c.mp4?token=CkADPyNXzc4s8sQdFfLCw9bLT5YnkoMGqz0fPsxPU2hkZ2GS--pLXHFxlJQxQodDiViB2Ronm5cqQ4AGvqvPzo9hKUxL8LKC2uNDQ0waPGhUAXYKh8Tja9cPMgcS6WG-948QuCd25QL_tm-rAHAN4EEG_MH1HtEmz3DnU7trWrPky6MAYZb4xfTI_Csph_m6CeVJrL5gUOaUdyOgcLhZ0Pk4mARNij4gM80v1we9eJp7AwibP-_FYZz_aA5I_He1qO_g1G-BIjfBAuRp2XiLXLWbpSLCCoG17DVsMTwQ28-lX5xYT2SfRyrmwMsWeS7N4dZxXkk-h_86N9-0D8TVE4RGRmoiyVbeLnvrgS1OkshV8PgbHoQlfNiMEe9_rxRudImG4Lm42-LoxLYmTA2tw6XBe6xP9u3El6iWdKM2HH8BoYGZneHzHRGleru3Mf1jROcPugFZGev6E13zH-joBBs34CYb2r4SaPsBG7u-KBGs0Zf_Caj-VCMWH3wQrCxLuKPesXzzNmbNvdPC3aE-jXZM3kYMofmJ_MeEj3HdIdyOuP3ABd5YfXFNjO-MeVVoItztoVvcstVccjjWhGBckXLREhev_rzBKQkygyx0n2RsxbwpIr-Lfh-9HoOFxncBkiL-dxcJJuF_02sPP2X-gDWdOVVSQQMExFZj9cRwO6E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون | چیرگی نظم ایرانی در تنگه هرمز
🔹
۱۵۰۰ شناور در تنگه هرمز منتظر اجازه نیروی دریا سپاه هستند، روی فرکانس ۱۶ همه شناورها این صدا را می‌شنوند اینجا خلیج فارس است مسیر اقتدار برای عبور از تنگه هرمز اجازه بگیرید....
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/akhbarefori/652821" target="_blank">📅 14:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652820">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxJ-SddBEpTL8D9y9Ay3iEYe9NCjXsU3NSFeIJAoo79Ake__EPQOi_-Nb_7GQPUEwmdLFNyoJ-R72XNvcrTjQwZUppnfyIX7vhls8kSebnvSF88XYb7QkkNoqHwPE_oeMVjpjy0DZzouZXQelTk69nABsHacT3AhZZ9O-aTcvuuAI2mlWcP6A7ehJPgvltDanTuAH2SUnjijjVb_4S-mvs2Z6AnMeilZJaLk_MHTze9qc9xxMADLQ_ymLO9wK98ulGNlJeLU1hc0-1TOaJDWnq9FJ1GWoDfMkeR0DAC5iiMzn6wJ6wFRnrep8SCXQpJyYgW6mUUCGyxWupZpW-a8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گنج ۱۰ تریلیون دلاری در کف تنگه هرمز
🔹
پس از اعمال مدیریت روی تنگه هرمز، ایران با استناد به حاکمیت مطلق بر بستر و زیربستر دریای سرزمینی خود (مطابق کنوانسیون ۱۹۸۲ حقوق دریاها)، می‌تواند تمامی کابل‌های فیبرنوری عبوری از این آبراه را مشمول مجوز، نظارت و عوارض حاکمیتی اعلام کند.
🔹
براساس گزارش Policy Exchange، این کابل‌ها روزانه بیش از ۱۰ تریلیون دلار تراکنش مالی را جابه‌جا می‌کنند.
🔹
هرگونه اختلال در این گلوگاه، به دلیل عبور کابل‌های محافظت شده دارای فناوری DWDM، می‌تواند روزانه ده‌ها تا صدها میلیون دلار خسارت مستقیم و غیرمستقیم به اقتصاد منطقه و جهان تحمیل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/652820" target="_blank">📅 14:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652819">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQNU34utQOhOA2_nI_MeiRP83DsPJsA0RS27HLHCUT-hIMo12fWkx9-huf_PwSykKmVK2J07DMsU3xjvOgAKfhBrMY81rxwkhUw7Sp08UmepoK-_w_YQV-6C4WuJqe-TdyGtyGo13bUmeVNeKl6BQVEY9viqDcFZym9H0ABoOD6oev49jTwGm5pYhJfUAj67FkloseAOMrzSAe1mNMxkiKbAZ-FqjBz2yDpJi4FgUDlmuAqQvnQuxHX4x2LKfpyb35lRfcMSlTiU1QIIrB__JMIO5Cp86Gm60P14AEeMge04KHvj4UB-VKtcbBp5xCLG8gxgd2SJOAV_LQYmlZudTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برلین: جنگ با ایران باید برای همیشه متوقف شود
🔹
لارس کلینگ‌بایل، معاون صدراعظم و وزیر دارایی آلمان، امروز دوشنبه پیش از عزیمت به نشست گروه هفت گفت که جنگ با ایران نه تنها یک تهدید جدی برای اقتصاد جهانی است، بلکه «خسارات عظیمی به توسعه اقتصادی وارد می‌کند.»
🔹
کلینگ‌بایل سپس تأکید کرد که باید تمام تلاش خود را برای «پایان دائمی» جنگ، برقراری ثبات در منطقه و تضمین آزادی خطوط کشتیرانی به کار گرفت.
🔹
در نشست وزرای دارایی گروه هفت که از روز دوشنبه آغاز می‌شود، شرکت‌کنندگان بر تأثیرات اقتصادی جنگ در منطقه غرب آسیا و پیامدهای احتمالی آن بر تجارت جهانی متمرکز شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/akhbarefori/652819" target="_blank">📅 14:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652818">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae6d4bd95.mp4?token=RVuKpUPoJChzwAwX285Qhd7cWzGIf2z2W3d2rbsAENmUMG1Rx57XXwZvIk5W6KOJp9N2keCNxMy02ocMJKck3pWZOmD02xVfEeD_a9You4QpJpuNjc126VKFd4roq1T8Q7rDcOqT8WqxWHEXj6YY09H6O1ZpOiFdE_Er-70kDu5JyD3Ti-GrlZrxseQlku2DVZrYKp1kzD0VdJmLcMZxD8A4-nWJIopnaQdMjHg87KVtPMPtECjYzhf-PkwNzcFgFliVz5AvagiHby6XICjUgRCXSqKxtoKtLdJISTgA2YSw7OKDNejtfqludiaiPH0MAgLpK7NHV2kGK8OysOETww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae6d4bd95.mp4?token=RVuKpUPoJChzwAwX285Qhd7cWzGIf2z2W3d2rbsAENmUMG1Rx57XXwZvIk5W6KOJp9N2keCNxMy02ocMJKck3pWZOmD02xVfEeD_a9You4QpJpuNjc126VKFd4roq1T8Q7rDcOqT8WqxWHEXj6YY09H6O1ZpOiFdE_Er-70kDu5JyD3Ti-GrlZrxseQlku2DVZrYKp1kzD0VdJmLcMZxD8A4-nWJIopnaQdMjHg87KVtPMPtECjYzhf-PkwNzcFgFliVz5AvagiHby6XICjUgRCXSqKxtoKtLdJISTgA2YSw7OKDNejtfqludiaiPH0MAgLpK7NHV2kGK8OysOETww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظارت مجلس بر بازار مسکن به عنوان یکی از اصلی‌ترین دغدغه‌های مردم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/akhbarefori/652818" target="_blank">📅 14:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652817">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
دستگیری عوامل وابسته به محور آمریکایی-صهیونی در ۳ استان
🔹
طی اقدامات سازمان اطلاعات سپاه در استان‌های قزوین، کرمان و چهارمحال‌و‌بختیاری تعدادی از عناصر وابسته به محور آمریکایی-صهیونی که قصد تولید ناامنی یا اخلال در نظام اقتصادی کشور را داشتند، دستگیر شدند.
🔹
قزوین:
🔹
دستگیری ۲ جاسوس وابسته به رژیم صهیونیستی
🔹
انهدام یک شبکهٔ توزیع سلاح‌‌های جنگی و کشف مقادیری سلاح و مهمات
🔹
کشف ۱۴۰۰ تن مواد اولیهٔ پتروشیمی احتکاری در یکی از واحدهای صنعتی
🔹
کرمان:
🔹
دستگیری ۸ تن از عوامل اصلی اقدامات تروریستی در سطح استان
🔹
چهارمحال‌وبختیاری:
🔹
دستگیری ۲۲ عنصر در قالب چند شبکهٔ وابسته به گروهک‌های ضدانقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/akhbarefori/652817" target="_blank">📅 14:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652816">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d03fe4881d.mp4?token=iDUglCQf8IgDlxOvkbXUolJcdZVOGWQENgbNlfFsl-jFjJzLjocjXFgFOCX8ZFOWJ3j325tBmciJX6ZgW6Z6Gw0AjsjYQW__dfmgXTIQrTk9rKB-U7EY-HJr5DxWPc3xL75UjscL9raF-U3EWeFWGIgR9rfoUezaPa3Ysl7Q7eb-4MLeA-kBOf76s9Hdh2i70VYNr1hPBMF3nH_stVqWKbF_pZ66sHo5SzBizTmnp1PhmyxhS9jSbenlplFYXT_dJ8zIvxCqRtu9ZALfwY3w4gy2cwmzBXKslZStjgtBIUAcpuWLIfvgW87IOtht0HZr6dzctRyyfYN5pQJLJuSLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d03fe4881d.mp4?token=iDUglCQf8IgDlxOvkbXUolJcdZVOGWQENgbNlfFsl-jFjJzLjocjXFgFOCX8ZFOWJ3j325tBmciJX6ZgW6Z6Gw0AjsjYQW__dfmgXTIQrTk9rKB-U7EY-HJr5DxWPc3xL75UjscL9raF-U3EWeFWGIgR9rfoUezaPa3Ysl7Q7eb-4MLeA-kBOf76s9Hdh2i70VYNr1hPBMF3nH_stVqWKbF_pZ66sHo5SzBizTmnp1PhmyxhS9jSbenlplFYXT_dJ8zIvxCqRtu9ZALfwY3w4gy2cwmzBXKslZStjgtBIUAcpuWLIfvgW87IOtht0HZr6dzctRyyfYN5pQJLJuSLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تانک‌های ارتش صهیونی با مخفی‌شدن هم از حملات حزب‌الله در امان نیستند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/akhbarefori/652816" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652815">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
آلیس روفو وزیر مشاور نیروهای مسلح فرانسه با اشاره به تهدیدها و لفاظی‌های تازه دونالد ترامپ رئیس‌جمهور آمریکا علیه ایران، توقف «تنش لفظی» و «تنش نظامی» را خواستار شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/akhbarefori/652815" target="_blank">📅 14:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652814">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ترکیه حمله اسرائیل به ناوگان کمک‌رسانی صمود را «دزدی دریایی جدید» خواند و خواستار آزادی فوری فعالان بازداشت‌شده و موضع قاطع جامعه جهانی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/akhbarefori/652814" target="_blank">📅 14:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652804">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNudT73SQdB2G_TcrZplD9fxPiYIeHw4789n_wfbsWmEJ0tFKs7QzQDvcHHcXR_ctmP-9Ronfb98KKHwR9p925NnEwkVsA20TgqymTjmZHJqNKrzkBIClVW2qNZZtsqu_st22tYJXatwkQuLSyRgI28jk1qPbL4MDKMtutZ3Emide6qMsyOXHBMSwmjLpmRgNNMBlyGrhERZxiwHJwbGUgd4wjt1oNLEnuE631e0zfdCv_Hp7q9RIMgnLSucnfKqX13QLpDMpC__w_EB_HFCqmS5VB7vXnZEsHh4U8i7GgU0Ldb-RE8V0oRrscucluPRimpx2yP6isTannZNhK3GcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEz8dEjupj9duSkIZ4VW-1UtPqdO040oN3MiCwmuOtq4NywWVvzGJhPqQhOt5d9DEH7fXiha_5FKIrc7nVHkx4pAu1pUP_xRVzanrpa10YDwffAb4bM_t9D-tak2sAmYq1yeUIUDqvQYbw-LZgYNYeC2gkR0GHt4j9Pn9k1pjlmDq7PA27GNcZt6eNugANMpj6LE6E0sHEnRq73sk8Ttg0UfuQ8E_Njzx-a576SnlrK1j9KEBbzcRiGWb0ztvDu3TW5YFGpeGWWVtc008ofsHVcIc04l-1XA_jbwvJ83aSfUCt0ke5h7KPa831kIP8RF430NUAMxNZp7A4Pveztotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kejs9-fYHDBqN6FnW4vxMqDcaxHM2I9QVye94MNjiZBlijcneKZ5p67hAKSfLQ88SsRMzjbE9REYMEtX1tYsELsRvTjhhaLtVKNjaWd-_57VI05mc_LSuq2IXqu-lGZKro0_KqIyQN3xhOdn_6U6-HJuarUYh8cceN-aKYuCZvY53K9mUn2gMEM5lA_sOTkW9P-UkKCiQScIYrOdXlyodKcTTDPD9webl26cWmqZ7pQl5L-ix164rjDhr293INLpVqZ0FC04KYYi6SLLpJAZSmfmJyL4N_20oTrIma5caS2A46O22DBBvJ0tU_zwik5kVP7bbVRepHILY6AJNzdSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOSMbMg8bAfGzb58rJ3szsl6oBEMLtVmQKGi9j3j4T1ejJBQ3S33sR2GccDCWaSm0jIUINuBrke4ZorZxMURX68w13bOtW-ctPA60DDI5C4pAhrWpJPYWDVEjWiJKSQWJ6zUwu9KDA_Jea1QOUffysjz0XE9Ct5MJIt_XDOxyaILZcWdyIJ4vrCrIbRdGsXAFgcBs6rKqVJldTqJgRB1581GzHEEkxUqiNtX4VxvGyi9B2r3_8HU8C1kfiGoaz4Lus-1yzUo8y44tSVdkaT877LZ0nkUeW2O7o78X82OVzaCQpqntmywR9jEVr3rEc1J7_QdBsDJlbFzAUWHkAmPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iy-mIrNVB8yjaDYVcxoE4Bv8iR8NhMfvBXgjxiCHXfkqGrv0rDc3FsDqyCZx2ZxT9OmLsGA8G4-7ohfaDrLCvjVmSyL_RdEFBUChjIPeG6E8VbvkUH6Zh6c1PO8TXKD53958zBQDGyyInefv7SFRqQgRtsRlSelF_mWs2_T8AB-RI4QLWMhETVdrgrH9rIfmBqYR_LJdRJIjlOM2wniMFHEROex3z7oG-vpd4gkkeMv_pRiPdQQq1QU-g78zfXjjJQKGHhV96Z_0-tl7k955yc8noEG6WrulE6ifay3aJkbH1KNQ0EPjkNDD12mUPdJ1lJRF3YK4x7ACk5-xmTKQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVNGtVG5wc_NRHikw2vfWQFRUJXLM1N-HIx2O_S3YmibpMe6N1iOTg4YGlRQgJapXMi6AXdNOiwXJ1UeCt8pq54y_8T73kSYZ7nXyM45-ANaN4Iq5yyN0EHlqjF3Dp75rjcuZxJ7Nu7vEg7ZiVe6-FAqHRUUxXDztff0nsNDa7wto4OwEq2fhq1yIvx_QZEVgODt9P64iZYfWHXENylvqD3xW7XBfLsrLEUvbXvPd8e5aAVm35riFJnnmVIUGtdpS9MoMA33FiWxeyWreA-zXsHvjuzB2m6ubmPyuTQ5LLOUUU3yqggcBgI0tyPECyB57HuvKPfhNhhmSJCpf9pU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QB4hkKBR7VVHfRzuFnKzZXU1wA0eQGlABvCDpUdIJo926ULFDlR92__zslxClAst4GmFDC0oyZPEYN6EKGPnv2Yo5xbPReQxtVwRWztpUcv3Oigj6XnQvbZS3U7u6qDjvsic1Pv4rBWZJyxjqm9TRHPqaypPoM_dlCIV6dAVpshZRBRuBn0aAYykQGqN0mXMg8ZZvBt3wKEjWfR-IiLpt0wi2Bynf7OXl9U1yVXQrHogfbDD7DWhJxwce-3aW972ydY575cuOuWB8PfM5YqXwEBS20KHFLdew62nxYnx3KyhjKEJRp64EHOTZNCwWtu2Ggum0y0CqUtR3aw4tb5dwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZtXngFY88pQZAiO-tY4DQDpaovNfw6A6Xn_XUpX_CGOONGVCdKf2wCT2jGGe3hNcu_RQ23dt9-GSn8w9HGHX3kELvmWSY5NOnIUljuUm0Nf6vxrYjjkofRTEL3wrGO_c-ROkVYBGzEp_ZFe-OELB9jZ38Gb-DuED6je5m0nwNBcGvjRUt2ciGMQR3Ghdizfa43j0-fbBsB-y2NlVPGZ0Uc2WZiS8yNugD8TLVKAol1homg3BtMogYpWRHM-RF6BiA8pi9b2lLf5-Wii5drhP_gyQ-lMKFRN7h6j-1vzQ0AxAywCk9N84pG6bsiKQ8lsLvui-T7qs2DGHsft3sPsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBZzQGtYzPY7WMZQm7tFIo5wFg_Pgd2dGmRv-TU31FNjYL0MQQ7Bii8MX10eiMLTFeFZoIhak8zXDIxCkcrZmamtNX757QWxS9swO-_CxoculoO3aKUHUTZOZKNfBEMKSWD21Hbu1oSsCDBaPJl3ZaSQply6QCTj9R2PZRpVmzyzzbRk7QUGZIQsZ2GXCdVLMugs8-4qWAOD5jdE3mSc3bs9RcNXkJN2Au8mC2CnLKLustlJHnQ9DNkm4vkr4LOg-kAh8fLSROTO6mlGMRt1727MKu4EyhEMKNH2gAiaZ6vcB1tKrqLLrjUE2M6hD5BLj75GdoVaZUn3UO-9RHQLww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QCDsLuSSoPiGcV4h6N_Hte6eSML4UlVm5jEq6NSk1TH1D3CikvLQ9fyeQSYu3RX8y6Q2nHCBJyh8b_W-S741S2ohE1CEfxiBI1kwJgHd8nVZL3vcHJPCB79nWefbMOW_jkoVAxw0N81Y1sVsXUUPENK0peAa3q9E9cnMnlQ8UvB7OGqQqbor6rBUrOHK63GjMdPk2OfExXVRxR7j0fBUt7w8zFn9t-uJpmjfQiL3iWlv2YQmd2TsbGtj1SfBNiqP9Zr78LEhXA8DjHaiV4eS88-DzI4_PP_a7Phh8yyiNqQAQy0dJFGfTSaPTbY2YoDi4S6_QYz6_MbcWwodcdFoNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
از دل مردم، برای مردم
🔸
#گزارش‌تصویری
از توزیع بسته‌های حمایتی در روستاهای کم‌برخوردار و مرزی شهرستان زابل، به همت
#هیأت‌قرار
و دستان مهربان خیرین عزیز در دهه کرامت
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/akhbarefori/652804" target="_blank">📅 14:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652803">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
تأیید شهادت یکی از رهبران جنبش جهاد اسلامی فلسطین
🔹
«سرایا القدس» -شاخه نظامی جنبش جهاد اسلامی- امروز دوشنبه خبر داد که «وائل محمود عبد الحلیم» در جریان حمله اسرائیل به شهرک بعلبک لبنان، به شهادت رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/652803" target="_blank">📅 14:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652802">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تابستان امسال قطعی و جیره بندی آب نخواهیم داشت
عیسی بزرگ زاده، سخنگوی صنعت آب در
#گفتگو
با خبرفوری:
🔹
شاخص متوسط کشوری بارش ۲۲۷ میلیمتر تا ۲۵ اردیبهشت بوده است و این عدد برای بلند مدت باید ۲۲۶ میلیمتر می بود؛ معنی آن این است که در شرایط نرمال بارش قرار داریم و مطلقا در شرایط ترسالی قرار نداریم.
🔹
پربارشی مناطق غرب و جنوب کشور به چه کار تامین آب تهران، مشهد و کرج می آید؟ بنابراین در تفسیر شرایط اقلیمی نباید دچار اشتباه شویم.
🔹
در تابستان به طرف قطعی آب و جیره بندی آب نخواهیم رفت، اما به طرف مدیریت مصرف خواهیم رفت.
🔹
تهران و قم با ۳۲ درصد کمبود بارش در صدر قرار دارند. استان های مرکزی، یزد، قزوین، اصفهان، سمنان، البرز، گیلان، مازندران، سیستان و بلوچستان، چهارمحال و بختیاری و اردبیل با ۱۰ تا ۲۲ درصد کاهش پایین تر از میزان نرمال خود بارش دریافت کرده اند.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/akhbarefori/652802" target="_blank">📅 13:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652801">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07130147ee.mp4?token=T-hXb2Wtk-cEPOVLJWtew-OpD-vKCkEzu89f8cy7dg4LjwAKhoLc9C8Z5Ac0BdVxGnIGxZB1Bzky9JrevgW3jK6x8q7Jfd6wZgs3BdYeo5t4JlVBiFUiOomhbwZPcBn-9odbbBnvwK6C5aCAJRBA15SfFZj-x_8cJQrA3CWNow3iP0pDqPWOLcL1S0u2EMEihSHQcxthk1tgivfoZedGwSbGq_ZH0KyimX12Ptv4Oejn1J0P1wBoZJV2-rk3bPu16Pa1AJpYLtFC8hOscGtuHt_UCe99f9RY4NNyjgOvlEOLIFEjXW4F_HQEowtuZ2Ba7FMWLTieWszR7ZEQSDt4Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07130147ee.mp4?token=T-hXb2Wtk-cEPOVLJWtew-OpD-vKCkEzu89f8cy7dg4LjwAKhoLc9C8Z5Ac0BdVxGnIGxZB1Bzky9JrevgW3jK6x8q7Jfd6wZgs3BdYeo5t4JlVBiFUiOomhbwZPcBn-9odbbBnvwK6C5aCAJRBA15SfFZj-x_8cJQrA3CWNow3iP0pDqPWOLcL1S0u2EMEihSHQcxthk1tgivfoZedGwSbGq_ZH0KyimX12Ptv4Oejn1J0P1wBoZJV2-rk3bPu16Pa1AJpYLtFC8hOscGtuHt_UCe99f9RY4NNyjgOvlEOLIFEjXW4F_HQEowtuZ2Ba7FMWLTieWszR7ZEQSDt4Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحید اشتری: هفته اول جنگ آمریکا به پدافند زندان تهران بزرگ حمله کرد؛
🔹
برخی زندانی‌ها از سلول خود فرار کردند؛ بهداری را آتش زدند؛
🔹
تا صبح در محوطه زندان صدای تیراندازی و رگبار می‌آمد؛
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/akhbarefori/652801" target="_blank">📅 13:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652800">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJq1W4H90StEaTtBuQ7PacVzAOaLZu6d81GSBFUyLYEycm1S8zZ3yacDQeIplrjkY2FArDCNqxbwmP-zlkA2CAnWmjstR8fw2dYjCLgU6DEdwb05qDmXQ_8KSxW-kksHo96qyZ9cIjNSaGhbhQO49dy-66Gg5cb4Ulrz2BmZ5HZ4SJSUv9gczaTut_Qz4jOofBTDHrmRquo0XkyaHhYDsgYSoskccJKMHkq36Qqik8COhC3M5G2AnQj9hXw1dbzh7yqhEfv3pyw2iF4ZzpzigAml6pkTFvLWCV9m3MG_lzhCfNiiaP4Afxk9fjDAxJYiH1e1ejZqEEbNXCT5lNIQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک محموله سنگین اقلام ضد امنیتی متعلق به گروهکهای ضد انقلاب، حین انتقال به داخل کشور در منطقه مرزی  شهرستان ارومیه کشف و ضبط گردید
🔹
بنا به گزارش روابط عمومی قرارگاه حمزه سیدالشهدا علیه‌السلام نیروی زمینی سپاه با اشراف اطلاعاتی و اقدامات پیچیده و فنی سربازان گمنام امام زمان (عجل الله) قرارگاه حمزه سید الشهدا علیه السلام در سازمان اطلاعات سپاه استان آذربایجان غربی ،یک محموله سنگین اقلام ضد امنیتی متعلق به گروهکهای ضد انقلاب ،حین انتقال به داخل کشور در منطقه مرزی  شهرستان ارومیه کشف و ضبط گردید.
🔹
این محموله شامل مقادیر قابل توجهی مواد منفجره و مهمات جنگی بالاخص ۱۹۸ بمب انفجاری بوده است که اشرار و عوامل تروریستی قصد داشتند با انتقال به مناطق عمقی کشور، از آن در راستای ایجاد نا امنی استفاده کنند که با هوشیاری و اقدام به موقع سربازان گمنام امام زمان (عجل الله) در سازمان اطلاعات در سپاه در نیل به اهداف شوم خود باز ماندند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/akhbarefori/652800" target="_blank">📅 13:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652799">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ایران متن جدیدی را در ۱۴ بند به واسطه پاکستانی تحویل داد
🔹
یک منبع نزدیک به تیم مذاکره کننده
🔹
وی خاطرنشان کرد: آمریکایی‌ها اخیراْ در پاسخ به متن پیشین ایران که آن هم در ۱۴ بند ارائه شده بود، متنی ارسال کرده بودند. ایران نیز مجددا بر اساس روال چند وقت اخیر در تبادل پیام، متن خود را پس از انجام اصلاحاتی مجددا در ۱۴ بند به واسطه پاکستانی ارائه کرد.
🔹
به گفته این منبع مطلع، متن جدید ایران بر موضوع مذاکرات پایان جنگ و اقدامات اعتمادساز طرف آمریکایی متمرکز است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/akhbarefori/652799" target="_blank">📅 13:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652798">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCeru-qkeeNfqelB-ddAkG57qAGZvidgeHlBMHEo0APcNO-TmS6D8yf5TwWER8C1oUWyA6jWM_sM5hvAMZo9GtveHuFkx5j4qRvdEjBojezkOaEz8H4n-OQ1D9DGp23J3lSA9Qlm7gxEOHnZbqreFiA0HPBNFES22UmV7UUgVQpUNGYJ8_b7ykqXKvamzvf0idCWwr9zl8qWs013HGm3BvPpa9izkI_iNen-MNfU5aeczR9HKWAJKUS-tUjikaeUiTdP2h_0TGGYfaXAChtG8VAhxvIBaHOmOaMQR6ZoPjSmrIqqD7lrbVaMZMYTyQcaF-ifs1N03LtolsoEuqAvgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معمای جنگ؛ تنگنایی که پیش روی ترامپ است
🔹
هیچ‌کس نمی‌داند رئیس‌جمهور آمریکا در ساعات و روزهای پیش‌رو چه تصمیمی برای رویکرد این کشور در ادامه جنگ با ایران خواهد گرفت؛ اما سوال این است که آیا خود او می‌داند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/akhbarefori/652798" target="_blank">📅 13:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652797">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tjn8UZmb8X212kau8sThK9rELW_29iqs8kAwiUGHYTHVv8q0fA6v4m579kssu3o4Ta_207qXAQSxa8Bj3cinSRDC1poALQXe_FZjp6C-T1QvfvkTohxwIJkAb46UcRr2z8rGjAbPGafWyiWWcTZClBG0gfb9K75sd0VNjEOdyFHKn4x38clHGdAGCGPiVlO7xlcd1FgX_pRZESK-a7EdltpSh-XWg7kdNt3ICf-HrIZs4J6Uyz31svqtVOyIoPRaPW1Y6t7aW7urdTktysSRpuXbDopxtQMRLjY3rJgQDpimbKFdRvwlI5hZvifoFAXaPNtkWP1OUWQ6oxARfzLy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار مسکن ایران بدون مدیریت مؤثر؟
🔹
خاوه‌ای، رئیس کارگروه مسکن دبیرخانه مجمع تشخیص مصلحت نظام، در یادداشتی اختصاصی برای گروه مسکن و شهرسازی، با انتقاد از وضعیت حکمرانی در بخش مسکن تأکید کرد: بازار مسکن ایران در سال‌های اخیر از مدیریت یکپارچه و مؤثر فاصله گرفته و همین موضوع به تشدید بحران در این بخش منجر شده است.
🔹
مسکن به‌عنوان یک نیاز پایه‌ای، در اغلب کشورها تحت مدیریت فعال دولت‌ها قرار دارد، اما در ایران این بازار عملاً دچار «بی‌متولی بودن در اقتصاد ملی» شده است.
🔹
خاوه‌ای با اشاره به سهم بالای مسکن در هزینه خانوار (تا حدود ۴۰ درصد و در تهران تا ۶۰ درصد)، این وضعیت را نشانه‌ای از بحران ساختاری در بازار مسکن دانست.
🔹
نبود استراتژی جامع، ضعف در تنظیم‌گری، کاهش سهم مسکن در بودجه عمرانی و تکیه صرف بر طرح‌های مقطعی، باعث شده فشار بر خانوارها افزایش یابد و توان خانه‌دار شدن به شدت کاهش پیدا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/akhbarefori/652797" target="_blank">📅 13:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652796">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDr9wmCFHo17c9_WMWs9ejtTA4P4u7Nnm6tjmBFNw_D49KXF28oFcw0jbDm6Y6BPjgr4pwG-6WP86iQdVwg-eiI_EgXnqCirAE0NFuAh3b_AZRb4rlGYV_GPPi2crcloIt0QbGzDRfGltBOznUirWHAOKA14Ub-zdDYt87f8cIb3YPKyq7viibNSZ-GcFqcCgH3fQl8EqV5D8FdzNmEL4HPzxyACgZe9lUNSdCqXMxV7Tzqcr9xLIOiVs_InO3LgzIiTfYm6TwRrR64sXrl4Oiw_bavW2GfIFkjHmMw9DE5TQNdRPbqFi9n40NfBziP8yvfDZjzUHisnIgt3veEO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ و تکرار حرف‌های همیشگی: ایران خواهان توافق است
🔹
ترامپ در گفت‌وگویی با نشریه فورچون که پیش از سفر او به چین انجام شده اما امروز دوشنبه منتشر شده است، ادعا کرده که مقامات ایرانی با او بر سر بعضی مسائل توافق می‌کنند اما «بعد یک کاغذ برایت می‌فرستند که هیچ ربطی به توافقی که کرده بودی، ندارد.»
🔹
وی در جدیدترین اظهارات خود در شب گذشته هم باز ایران را به حمله نظامی تهدید کرده و گفته بود که ایران زمان کمی در اختیار دارد و اگر «سریع حرکت نکند، چیزی از آن باقی نمی‌ماند.»
🔹
ترامپ پیشتر هم ادعاهای مشابهی را در مورد هدف قرار دادن زیرساخت‌های انرژی ایران با تعیین ضرب‌الاجل مطرح کرده بود، اما در نهایت از این موضع خود عقب‌نشینی کرده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/akhbarefori/652796" target="_blank">📅 13:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652795">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU1RvybSthqIi-WJckjYifNcWc32oBL__u5NoN8xH9qBKM9nxPLyPn30MQb53TxM0dWZnO1Zm3U6Ex9FFtixSJmlGmlcKmldSp2-W2x_QYFBqXtRwlK8MGRrQmSJI0GgeB2u9e0a3hDyna2sCf9HHaccNI__GrYBQ4JBjveRmcmOgGaCq5g8io4Bd5QCteWeQI0a7mljOi2C_fHzHHQs-T8wyJZRic-XkbAV513W_W8wOFkzh4Yt2hiKhQ4TifvpSjOBp8X9X5GnO5i69YLAecgnp6iwR2uKsIAMTbGiHU9Kl-OBMqUcFSy7ILtsuf29-6jgcNxWqRKthQBObx_fvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گروهک های تروریستی نیابتی آمریکایی - صهیونیستی در شهرستان بانه استان کردستان مورد ضربه قرار گرفتند
🔹
بنابه اعلام روابط عمومی قرارگاه حمزه سیدالشهدا علیه السلام نیروی زمینی سپاه، طی اقدامات اطلاعاتی پاسداران گمنام قرارگاه حمزه سید الشهدا علیه السلام گروهک های تروریستی ضد انقلاب مستقر در شمال عراق به نیابت از آمریکا و رژیم صهیونی که قصد انتقال محموله بزرگ از سلاح و مهمات آکبند آمریکایی به داخل کشور را داشتند در شهرستان بانه استان کردستان مورد ضربه قرار گرفته و مقادیر زیادی سلاح و مهمات کشف و ضبط گردید پیگیری های اطلاعاتی برای شناسایی و دستگیری تمامی عناصر داخلی خود فروخته گروهک های تروریستی در دستور کار قرار دارد.
🔹
قرارگاه حمزه سیدالشهدا علیه السلام به همه عناصر و عوامل خود فروخته و سردمداران آنها هشدار می دهد که با هر اقدام امنیتی بشدت برخورد و آماده پاسخ پشیمان کننده می باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/652795" target="_blank">📅 13:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652794">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEBs2c6X-Y_M4HVwR2lEkRK0x_OeR-O9hRA_ysf8i9efYnTZs6KjsDaB2Ux0MqN1n-iQXvxw7PS8VOPtF1C3r9bI5djIycU1HyzG_3KPi6pVWj5LIjHjhOOk6seQqLsqcn1i8XKga4RiaWAq1wz0Nu8rAuvx2Bbg8t8nNhJRoing6_3jRI3LFoLCbwso6q7lw46Ee3s1PBdHddFi8h728Drzz9iZvLFORXWX8VKPz53Xeac8pq03-IfEyDjUszORjTNDFsDmXFSGn6MKotpf50-DSlMw-pfwhOs6UxLM2CyYqW7SK1UZyppQd3JmMvQXc-NXTtqSdtyllY84aTwB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شمار شهدای غزه به چند نفر رسید؟
🔹
وزارت بهداشت غزه امروز دوشنبه آخرین آمار از شهدا و مجروحان حملات رژیم صهیونیستی را منتشر کرد که طی ۲۴ ساعت گذشته شش نفر شهید و ۴۰ نفر هم زخمی شدند.
🔹
در بیانیه این وزارتخانه آمده است: تعدادی از قربانیان همچنان زیر آواره هستند و نیروهای امدادی و دفاع مدنی تا این لحظه قادر به دسترسی به آنها نیستند.
🔹
از زمان آتش‌بس در ۱۱ اکتبر تا به امروز در مجموع ۸۸۷ نفر شهید و دو هزار و ۶۰۲ نفر هم زخمی شدند. در این مدت، پیکر ۷۷۶ شهید از زیر آوارها بیرون کشیده شده است.
🔹
از زمان آغاز تجاوزات رژیم صهیونیستی در ۷ اکتبر ۲۰۲۳، تا کنون، ۷۲ هزار و ۷۶۹نفر شهید و ۱۷۲ هزار و ,۷۰۴ هم زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/akhbarefori/652794" target="_blank">📅 13:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652793">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c126e340ef.mp4?token=UT2lwhdAKumb0JKf5csP6ZtnJ3xs5nptWr0fcNxZVzUTX5lcSY4elsBFo7B0pzpOWkI2mPN9DWKem-5Ep1QiE_k7NCha2NZNGetvaafNrk0c7kAGf0nb68JyIqxDrYbUtq-XnwMAZI8hUHCTCBFanqslyu04VKgq8C4GuRGCRkXdbroklKwZ8hy89zx37ZCC5i7H7IJkt8XuS2eB0wOHiPOnaaUrl26VlQh9u0T5lMym-WlmL-Q2bKGTXwNbXC8EmG0y7cfDRB_wVg5nDu7E75LxGguF1vRf38IA4afiKcrfvgQGLA-U3FUyNSDRkSZ3RYeQEuuEtna4JBx7yHG40g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c126e340ef.mp4?token=UT2lwhdAKumb0JKf5csP6ZtnJ3xs5nptWr0fcNxZVzUTX5lcSY4elsBFo7B0pzpOWkI2mPN9DWKem-5Ep1QiE_k7NCha2NZNGetvaafNrk0c7kAGf0nb68JyIqxDrYbUtq-XnwMAZI8hUHCTCBFanqslyu04VKgq8C4GuRGCRkXdbroklKwZ8hy89zx37ZCC5i7H7IJkt8XuS2eB0wOHiPOnaaUrl26VlQh9u0T5lMym-WlmL-Q2bKGTXwNbXC8EmG0y7cfDRB_wVg5nDu7E75LxGguF1vRf38IA4afiKcrfvgQGLA-U3FUyNSDRkSZ3RYeQEuuEtna4JBx7yHG40g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش اسرائیل برای سه شهرک در جنوب لبنان، هشدار تخلیه صادر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/652793" target="_blank">📅 13:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652792">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اجاره‌ها در دوره تمدید اضطراری ۲۵ درصد قابل افزایش است
🔹
مدیرکل دفتر اقتصاد مسکن وزارت راه وشهرسازی: طبق مصوبه شورای عالی امنیت ملی در اواخر اسفندماه ۱۴۰۴، در دوره اضطرار، قرارداد‌ها به‌مدت دو ماه به صورت خودکار تمدید می‌شد و سقف پیشنهادی وزارت راه و شهرسازی برای افزایش اجاره در آن دوره ۲۵ درصد بود.
🔹
اعضای شورای مسکن استان تهران تاکید کردند که ظرف مدت یک هفته، نرخ جدید اجاره‌بها برای شفافیت بازار رهن و اجاره تعیین شود. بر همین اساس، کمیته‌ای متشکل از دستگاه‌های مربوطه حداکثر ظرف دو هفته این موضوع را با بررسی تمام جوانب، هم برای استان تهران و هم برای سایر شهرستان‌ها مشخص خواهند کرد تا مورد قبول و عمل موجران و مستأجران باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/akhbarefori/652792" target="_blank">📅 13:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652791">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a894fb101.mp4?token=KdtEIBtwZLNe077y8BCOsDbNKu7qRrF7ZNpwfr6iN_gubJdjwW2WZ9pSFNnt3sg63iRR4PvvxKiVIMU1ozRQJOqU92pVfATu6_pppvMjB2sr6wkePqRXXJxLdaEiEmwASYdKtGsU78JxXurYSvuEBs1n54zm-lUTTqnJXFl8h_NG46pAtyN7PaHCO9bXxQipRBykD-Wdm2F748G_yZTUZpT-vrScTlaB43zAMuQ4eCcV31r3x7zFm_D4I-i5mirC49YytF4gRlYXcxAgXLoOlbMvZrtetx_majbpd9aTcb7kLAZCp3KzOnBzqbpXpIoD95ZNRztn3Z1Xtvy8yemxpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a894fb101.mp4?token=KdtEIBtwZLNe077y8BCOsDbNKu7qRrF7ZNpwfr6iN_gubJdjwW2WZ9pSFNnt3sg63iRR4PvvxKiVIMU1ozRQJOqU92pVfATu6_pppvMjB2sr6wkePqRXXJxLdaEiEmwASYdKtGsU78JxXurYSvuEBs1n54zm-lUTTqnJXFl8h_NG46pAtyN7PaHCO9bXxQipRBykD-Wdm2F748G_yZTUZpT-vrScTlaB43zAMuQ4eCcV31r3x7zFm_D4I-i5mirC49YytF4gRlYXcxAgXLoOlbMvZrtetx_majbpd9aTcb7kLAZCp3KzOnBzqbpXpIoD95ZNRztn3Z1Xtvy8yemxpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک شهروند کلمبیایی از ایران و فلسطین: ما به آن ملت بزرگ، به آن تمدن پارسی، به آن مردم بزرگ و به آن فرهنگ عظیم ایرانی که امروز به جهان درس می‌دهد افتخار میکنیم
🔹
گفت‌وگو اختصاصی خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/652791" target="_blank">📅 12:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652790">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
کشف مقادیر زیادی سلاح و مهمات‌ از گروهک‌های تروریستی ضد‌انقلاب
🔹
گروهک‌های تروریستی ضد‌انقلاب مستقر در شمال عراق به نیابت از آمریکا و رژیم صهیونی که قصد انتقال محموله بزرگ از سلاح و مهمات آکبند آمریکایی به داخل کشور را داشتند در بانه استان کردستان مورد ضربه قرار گرفته و مقادیر زیادی سلاح و مهمات کشف و ضبط گردید.
🔹
پیگیری‌های اطلاعاتی برای شناسایی و دستگیری تمامی عناصر داخلی خود فروخته گروهک‌های تروریستی در دستور کار قرار دارد.
🔹
قرار حمزه سیدالشهدا علیه‌السلام به همه عناصر و عوامل خود فروخته و سردمداران آنها هشدار می‌دهد که با هر اقدام امنیتی بشدت برخورد و آماده پاسخ پشیمان کننده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/652790" target="_blank">📅 12:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652789">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-5PvryRBypXN69cF3LFfKCW2bVZNiRI2JlUYrlJfagQLq83IENsyGh-A9RXdm-GbAGVxr8PJ0Sz22MJlBLdRvKErI5DclOiKkQ1FpAG40TB7aS1swXJR2oUPLuu8EO3_OEv3P_BsfC3pipARUH0mH67bQ9nQBS_DXjDKb_YlyT3V7_J_hI0-vTEpAk4rBFFiA-TSMJv2SKiv4Ny42Q2JzStH-s9TFYCWyWbpQDKjTQb8Kmm4cfTGLHBNTPCw84P_GadJxE9dB_r6qdzm6z83hBjKKD3tLkroa2aLMv12gJUfNcBjLfoPs8h-DLG4ALB6XAI-Z7IbPvHm0uLD0Te1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بار سنگین تنگه هرمز روی دوش اروپا؛ کالاس: لطفاً توافق کنید
🔹
با ادامه بسته ماندن تنگه هرمز و تشدید فشار بر اقتصاد جهانی، اتحادیه اروپا از ایران و آمریکا خواسته است تا در مرحله اول بر سر بازگشایی تنگه هرمز با یکدیگر به توافق برسند.
🔹
مسئول سیاست خارجی اتحادیه اروپا کایا کالاس در مصاحبه روز دوشنبه خود با خبرنگاران، هراسان از ادامه بسته ماندن تنگه هرمز، افزوده که: «ما واقعاً تلاش می‌کنیم تا همه بازیگران را قانع کنیم که آزادی دریانوردی باید رعایت شود، زیرا تنگه‌های دیگری در جهان می‌بینیم که ممکن است به روشی مشابه ابزاری شوند و این به نفع هیچ‌کس در جهان نیست.»
🔹
کالاس همچنین در بخش دیگری از سخنان خود، «بن‌بست» در مذاکرات بین تهران و واشنگتن را مشکلی بین این دو طرف دانسته و مدعی شده که اتحادیه اروپا «اهرم فشار چندانی» روی هیچ یک از طرفین مذاکره ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/akhbarefori/652789" target="_blank">📅 12:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652788">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fhu0BE60zLWg7Ty7D3Y2ZQ-8ijPpGHL5Fuqw0kZJfouaZdzE196pppLvpB9nEVPMZCOIUz_awY09ddn-nJOjLrmbIFV9ffzEXXhGMuKq33nq2QZBCU6ZIFxKUDMLTY39ST8akNKLNDC5ycMIpCDFkwTTenfGgEba59uUi-uU-5EX8ayguzhZ42rTOvB_HxFpLy9BMVodQMX7IkeJlKVVWmxCD9FZuWHDm8pKmxMzBSP6SM7ooOOTydBmz3AkUjO-T03K0j0Hrid5oHv28QMC8FZrSn21mLktsjhyI8Zoa-xv7WdpPLRbHvobKneAb9Nsou5TIrzdcP9Ago8ATVL7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چالش ۷ روز بدون پلاستیک
🔹
یک هفته برای تغییر، یک قدم برای زمین   شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/akhbarefori/652788" target="_blank">📅 12:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652787">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
العربیه: ده‌ها اسرائیلی تندرو وارد خاک سوریه شدند
🔹
شبکه خبری العربیه از ورود غیرقانونی ده‌ها صهیونیست تندرو به خاک سوریه خبر داد.
🔹
ارتش رژیم اسرائیل گفته است که این اقدام، نظامیان و غیرنظامیان را در معرض خطر قرار می دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/akhbarefori/652787" target="_blank">📅 12:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652786">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4279769e28.mp4?token=TM04tUWVbz7AkmEAKXQ_1pPDRFbwDsC5b6ao6SP4MmhEHullPoho3xUTWts0QGurVdyOskm20hJQ2Ehl7quGXKuD2ndlmRmMhIGZJBWPXXiYkgVDOPKbcQJIsgNkJhU701UodAo5PJ2yPvTMhfZWLT7ndDKxCpCthY6qhl0VcYIsWAgqRxhqqKQYX4xu-rDUFN-gaere6niPuCAQInIJu8AITa_XK0nvt5z_Lhccpmf52glCtLnutsnKSduFpjnZgN6w_GnafQXAAnrG9tho-2GGSvd91pjA3QQWUQI4AP42dl0G3SNTnsPKnqCbZDn4XHDU-YoJVytfHV-kCadL3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4279769e28.mp4?token=TM04tUWVbz7AkmEAKXQ_1pPDRFbwDsC5b6ao6SP4MmhEHullPoho3xUTWts0QGurVdyOskm20hJQ2Ehl7quGXKuD2ndlmRmMhIGZJBWPXXiYkgVDOPKbcQJIsgNkJhU701UodAo5PJ2yPvTMhfZWLT7ndDKxCpCthY6qhl0VcYIsWAgqRxhqqKQYX4xu-rDUFN-gaere6niPuCAQInIJu8AITa_XK0nvt5z_Lhccpmf52glCtLnutsnKSduFpjnZgN6w_GnafQXAAnrG9tho-2GGSvd91pjA3QQWUQI4AP42dl0G3SNTnsPKnqCbZDn4XHDU-YoJVytfHV-kCadL3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باید دشمن را عقب بزنیم؛ بازخوانی بیانات رهبر شهید انقلاب دربارهٔ جنگ اقتصادی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/akhbarefori/652786" target="_blank">📅 12:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652785">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انتخابات هیات رییسه مجلس سه شنبه آینده برگزار می شود
علیرضا سلیمی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
انتخابات هیات رییسه مجلس  به موقع روز سه شنبه هفته آینده برگزار می شود و جزییات برگزاری آن اعلام می شود.
به هیچ وجهی این انتخابات تعویق نخواهدیافت.
@TV_Fori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/652785" target="_blank">📅 12:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652784">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ju3hxiqn475RcHHPCYL1LyEyAdcHGXoY-AghPJNhuqxw-gnn-0GXew2wRYJY8MqYq3WUSRXG66VXnJblynVW4CqsZUdNyxEHgTGeyRfjFTijOhmY8Nn0kar1ZgFUzGWm7VCFPf4LS0qNiOUMDItzUJqGtiUwZiezW6SgIL3k3JfmY6d1N4iYTpGtkkTNNXAcips5DY0jcyvMLXkTFndVPTzXSAhDj_HhSagKjBOeuu89naAQEbr4ftzbTB-1NA-vHpTWBBStwfA9uY5VhTcqbPth6iIeGYoX6riMlLyJcvi_2YRJ7jp6UDj64mb5YvCrSfbIF99_Ix_VWy9Z87XWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
*جهش بی‌سابقه نسبت کفایت سرمایه بانک اقتصادنوین*
🔹
نسبت کفایت سرمایه بانک اقتصادنوین دو رقمی شد و به 10.55 رسید.
▫️
به گزارش روابط عمومی بانک اقتصادنوین، این بانک پیش از این موفق شد با ثبت افزایش سرمایه 135درصدی از محل مازاد تجدید ارزیابی دارایی‌ها، سرمایه خود را از مبلغ 103.254 میلیارد ریال به مبلغ 243.145 میلیارد ریال افزایش دهد.
🔹
برای کسب اطلاعات بیشتر روی لینک زیر کلیک کنید:
🔗
https://www.enbank.ir/s/mfa2Zu
‏
🔗
www.enbank.ir
▫️
02162740</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/akhbarefori/652784" target="_blank">📅 12:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652783">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/214629aa2f.mp4?token=lB7rTucr_MCjSUBDarsJ_GK_94ms18r5Uer5KyfOn8v0JqsZjoBLRa6NtLRkDtjbUNdBcVXtiW1_TqCk6-taPVi7_clJQyUI77lLkn-07imj797vbZQ8mVsVQHjFgy9SdLHdh4Tsq-uSp9V15cVCwcHw1I7UF3ILQ-XjUggJGCEhTh_HDed8ozdXg_-EaOtzMny6KXrqNrpiKuaaiEKmqdjViQu-9xMrQJBkIv-3Hv89xhJACBXrvzfZJVKyVjesfTROzAd_3_-71MiKGFM2ELeIPqy9hQj1EL9XstC0OL5oG7ttzMlWjdswzlsdktC-gdQHD7w91sCqUh-gM54WCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/214629aa2f.mp4?token=lB7rTucr_MCjSUBDarsJ_GK_94ms18r5Uer5KyfOn8v0JqsZjoBLRa6NtLRkDtjbUNdBcVXtiW1_TqCk6-taPVi7_clJQyUI77lLkn-07imj797vbZQ8mVsVQHjFgy9SdLHdh4Tsq-uSp9V15cVCwcHw1I7UF3ILQ-XjUggJGCEhTh_HDed8ozdXg_-EaOtzMny6KXrqNrpiKuaaiEKmqdjViQu-9xMrQJBkIv-3Hv89xhJACBXrvzfZJVKyVjesfTROzAd_3_-71MiKGFM2ELeIPqy9hQj1EL9XstC0OL5oG7ttzMlWjdswzlsdktC-gdQHD7w91sCqUh-gM54WCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رابرت گیتس: نتانیاهو سال‌هاست آمریکا را به حمله به ایران وسوسه می‌کند
🔹
وزیر دفاع سابق آمریکا می‌گوید که نخست‌وزیر رژیم صهیونیستی از سال‌ها پیش ادعای ضعیف‌شدن ایران را زیر گوش واشنگتن می‌خواند تا آن را ترغیب به اقدام نظامی کند.
🔹
گیتس در مصاحبه با برنامه «فِیس دِ نِیشن» در شبکه «سی‌بی‌اس» گفت: «او (نتانیاهو) در ماه جولای سال ۲۰۰۹ به من گفت که رژیم ایران شکننده است و با اولین حمله فرو خواهد پاشید».
🔹
وی در این‌باره توضیح داد: «من به او گفتم که کاملاً اشتباه می‌کند - اینکه او مقاومت ایرانی‌ها را دست کم می‌گیرد. این همان چیزی است که او سال‌هاست سعی در قبولاندن آن دارد».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/652783" target="_blank">📅 12:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652782">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn50XohMjBPecUJe-HRqicUWu2oucC92a6h28Dk1b0ygzaeaVOecX3AV2oHfk_PkSfHyZ2ZkBvjj1CmZFBxjdsWzp9H-n-k4n8gq24q3P8EXPMNqD6asT3BqYksGiTCe5S8UOXrLK6Z-7TIBzzVbdzFkCshNc7jlGmVHIz6pSh0UArkXr34-I1sMtpRzSdGXXeV3Z01qENKPfVpZJdklTS1boTqBa6n6Xfecicq4nijfCkjkCx9PgOd1lwmc2y4Qm3ZWPMlxDeaCCYt9hXyzyRlsgE_ZT-DOAS2KiqqIy_cKyuuuqIB-D79Ftw7PGDG4ISDs7TlzxLypxKiWM_6Ktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه صهیونیستی: آمریکا موافق حملات اسرائیل در لبنان است
🔹
آمریکا اخیرا توافق آتش‌بس را در لبنان تمدید کرد؛ اقدامی که به گفته کارشناسان صرفا مجوزی از سوی واشنگتن برای کشتار هر چه بیشتر مردم لبنان است.
🔹
روزنامه «اسرائیل هیوم» امروز فاش کرد که تمدید ۴۵ روزه آتش‌بس در لبنان توسط آمریکا، به منزله موافقت رسمی و خاموش با عملیاتهای اسرائیل است.
🔹
این روزنامه با اشاره به اینکه آمریکا با این اقدام، به اسرائیل آزادی عمل می‌دهد تا دست به عملیاتهای بیشتری در لبنان بزند، نوشت،
🔹
واشنگتن و تل‌آویو به صورت پنهانی موافقت کرده‌اند که عملیاتهای نظامی رژیم در لبنان، تحت پوشش «آتش‌بس فعال» ادامه پیدا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/akhbarefori/652782" target="_blank">📅 12:17 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

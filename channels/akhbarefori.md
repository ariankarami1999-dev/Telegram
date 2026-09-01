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
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 19:17:59</div>
<hr>

<div class="tg-post" id="msg-686236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-KOONiYI-wZqJNY4AnvvqNDH19woCNahcxh9XH7btVgWHqdF2cwDVrACkwSrllPSZ-Sgiy6djnVf5JlnQceYnGDxau7ClHX4jeU61hUiBr58n93RCFnAVINC7kJ8JkCKAKxq4_tHtF8jA8BAvmAOmqiNbUDrnUg2BRREKH2j3vYN7yZ6-Hsd6ohcHsWse-jgXG9mer8gfSr6SMNRQG68_GQWKNKkxrGg-hW8YmJNBdeKIKJhHY3kTPY9weZKxC21mDzE_Wm9u_AaTchmMa7vJ4yZbraSSK1UQubD684BSk9QDtcktBCXQt5AObv6TF5M8XYtM-0vrTxNcmS5Nxjug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمترین قیمت تتر/دلار در صرافی ایرانی ۲۱۱ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/686236" target="_blank">📅 19:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if2HAbE9vpPKsSqzY7VRN5DyrtEFjFiJZam9xRJTD2yFxDPxt4MVcZ6VS07HFv75JiNwSCSHrT_u3nL97joeRTM_jKEooJz23nBs1X8OHmD7PL-JaaQey2Q6JqMY5MbZk92SEdLxxb9x3U3KMhooozBHuKrNHnGu4Q40ln1cI_c5i4Ok35t4GT6G8v1gEcb-PHOklrzUIkxCwcghdm2LsQMxrD7JteQGRQWFtL1v67OBBULse4-FnmkCnIYT-a1_kKmeKwVQn5e4OC945WlDT2BzEx1Gbg11a53IcJMfA9Jyje-qZro_rROuwEAqTjsCJszp6nL_VUOaRWXPVlKXyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: آینده چندقطبی و چندجانبه‌گرایانه است
وزیر امور خارجه:
🔹
در دیدار و گفت‌گوها با مقامات ارشد اوراسیایی، چینی و جنوب آسیایی در اجلاس شانگهای بر دفاع اصولی ایران از حاکمیت و تمامیت ارضی خود و بر ضرورت اتحاد برای مدیریت روند افول یک امپراتوری بیمار تأکید کردم.
🔹
بیش از هر زمان دیگری، آینده چندقطبی و چندجانبه‌گرایانه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/686235" target="_blank">📅 19:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر خارجه سوریه: اسرائیل به دنبال تثبیت اشغالگری در سوریه است.
🔹
اسکای نیوز: تلفات سیلاب هیمالیا در مرز نپال و چین به ۱۰۶۶ کشته و ۴۴۶۲ مفقود افزایش یافت.
🔹
اتحادیه اروپا: دیپلماسی در تنگه هرمز تاکنون نتیجه‌‌ای نداشته است.
🔹
درگیری ارتش پاکستان با تجزیه طلبان در ایالت بلوچستان/۲۱ مهاجم و ۶ نیروی امنیتی کشته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/686234" target="_blank">📅 19:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCNfdREPHgvqHN_q-5iC22I20iwrKw6OiMbNg4OMJVU5wgC186xJoE6ytI4SR9zwOL5TyMrOgZAGx0_1AFRGXVZoa-ndgkRH94bTaiN-SfsUL4jeH2g9d8nI_LiuBWkBT_YQ94Ttbu4bBISRbl9ZzDCX_3-YmY3jKWwmVanb7bIpv6-h8ZpSHTXTjGK8GeVAwPwCxGduwOwKcZpu3wWcArGH9X1AOWVApOLDBqPFEAPZk84PgEhM5rRicum6KjP2Cl_ORBJMQrx3k16p0zWX4GlUthWOQO3uPHWn0va8S1-cSP4qeFKYg7oKL3u4xCXvf7RZmqAh0MagaXSZ8mjeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تورم و ننه‌جون
🔹
دست غریبه‌ای در یک جیب، شاهدی در جیب دیگر
🔹
امیر نیک‌رویان روزنامه نگار در یادداشتی برای روزنامه شرق نوشت: تقویم سیاست‌گذاری در این جغرافیا، گویی بر مدار استثنا کوک شده است. «مقطع حساس کنونی» دیگر یک برهه گذرا نیست، بلکه به یکی از طولانی‌ترین و تکراری‌ترین فصول تاریخ معاصر ما بدل شده است. روزی تنش‌های منطقه‌ای است، روز دیگر تحریم و بن‌بست‌های دیپلماتیک. بی‌شک هر یک از این تکانه‌ها وزنه‌ای سنگین بر دوش اقتصادند، اما مسئله از جایی آغاز می‌شود که این شرایط استثنائی در پی تکرار مدام، به وضعیت عادی و توجیهی همیشگی برای ناکارآمدی تبدیل می‌شود. اساسا ساختار دولت برای اداره کشور در دل همین واقعیت‌های سخت شکل می‌گیرد، نه برای مدیریت یک ایران فرضی که در آن خبری از تحریم نیست و بازار ارز چشم‌انتظار اخبار سیاسی نمی‌ماند.
ادامه
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/686233" target="_blank">📅 19:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا نسبت به «تشدید تنش‌ها» و لغو پروازها در فلسطین اشغالی
🔹
رسانه‌های اسرائیلی از ارسال پیام هشدارآمیز سفارت آمریکا در قدس اشغالی به تمامی شهروندان آمریکایی حاضر در منطقه خبر دادند.
🔹
این سفارتخانه در ایمیلی رسمی، نسبت به احتمال «تشدید غیرمنتظره تنش‌ها» به اتباع خود هشدار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/686232" target="_blank">📅 18:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686231">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc022fce85.mp4?token=psV4uQpt2-5bM57sZNCyLuWe0QO7BeDLR3S2L0tr6O3PEaF3qRUI8gZfUimTE7XMD6m06RDmBIf7j-octfw1jxJ3mbQjipL5B-KJR8NsVY1XPCgFICXhKKPTyjQHFq_nnryfe62J5A_4xE-2CUnPrYoCAMfTOydRw5hHbJtkHX6YhaIjATRYxcPLN8a7zupHVeA0EfAY-DSG5Ja80YSxP_dXV-X3FLuJD9dllaDj6WXWqJeYFW1kT6uFQ9-mjWEHQv3iLPJPGrWcQScq7oa1cIhYOmQjSOsQ0Fq8B0836FPwzTi9A4BOxTChd5c8-tBWzhIrtPOyielQFHk40Fa7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc022fce85.mp4?token=psV4uQpt2-5bM57sZNCyLuWe0QO7BeDLR3S2L0tr6O3PEaF3qRUI8gZfUimTE7XMD6m06RDmBIf7j-octfw1jxJ3mbQjipL5B-KJR8NsVY1XPCgFICXhKKPTyjQHFq_nnryfe62J5A_4xE-2CUnPrYoCAMfTOydRw5hHbJtkHX6YhaIjATRYxcPLN8a7zupHVeA0EfAY-DSG5Ja80YSxP_dXV-X3FLuJD9dllaDj6WXWqJeYFW1kT6uFQ9-mjWEHQv3iLPJPGrWcQScq7oa1cIhYOmQjSOsQ0Fq8B0836FPwzTi9A4BOxTChd5c8-tBWzhIrtPOyielQFHk40Fa7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشته شدن مقام ارشد بانکی آمریکا در چاقو کشی در نیویورک
🔹
یکی از معاونان بزرگترین بانک آمریکا در حادثه چاقوکشی در میدان تایمز در نیویورک به قتل رسید.
🔹
بانک او آمریکا شرکت خدمات مالی و بانکداری چندملیتی آمریکایی است، که اکنون به‌عنوان بزرگترین بانک  این کشور شناخته می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/686231" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پیشنهاد جدید برای وام ازدواج؛ ۷۰ درصد کالا و ۳۰ درصدنقد
سید نجیب حسینی، عضو کمیسیون بودجه در
#گفتگو
با خبرفوری:
🔹
حدود ۶۰۰ تا ۷۰۰ هزار نفر در صف دریافت وام ازدواج هستند.
🔹
پیشنهاد جدید این است که به‌جای پرداخت کامل پول نقد، با فروشگاه‌ها قرارداد منعقد شود و بخشی از تسهیلات به‌صورت کالا، در جهت حمایت از تولید ملی و هدفمند شدن مصرف وام، در اختیار زوجین قرار بگیرد.
🔹
این طرح می‌تواند به مدیریت نقدینگی در جامعه و کنترل تورم کمک کند و احتمالا به‌صورت ۷۰ درصد کالا و ۳۰ درصد وجه نقد اجرا شود.
🔹
بسیاری از مردم توانایی تامین ضامن را ندارند و حتی برخی افراد برای ضمانت، مبالغی دریافت می‌کنند.
🔹
با توجه به محدودیت منابع در شرایط جنگی، فعلا امکان افزایش مبلغ وام ازدواج وجود ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/686230" target="_blank">📅 18:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734d98cea5.mp4?token=j_OAF0nt9E1Wj7vUxDu3Yl7W1Z1007LNSZNnsRJw3O3XooNEfTIIykLF0X2NgF3TQNrR688fopOMqQmPK2YHUWHPXqOJ_hDou5pWuCZbS5YypERzYgrGAJdParRhFyb3puDkxyxOsbGA7GWekbQFNW1XOf8byt8wQfY3NXhoHI7HVhcKWtmFUiZgbY1_rlzwncFZ78Q38edxO2RX04TIlUp14bOWa1czGvdbZVx8k1GDuMfuUzTsHxY-7GmkTN2Go9YyB1SSfyWofmMLgm_blTACwo0DqAc27IvEgNJ3Q0GDLnAvYviRK1_GOcdbOgrKtj9NMbaZInfCory_JM4L4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734d98cea5.mp4?token=j_OAF0nt9E1Wj7vUxDu3Yl7W1Z1007LNSZNnsRJw3O3XooNEfTIIykLF0X2NgF3TQNrR688fopOMqQmPK2YHUWHPXqOJ_hDou5pWuCZbS5YypERzYgrGAJdParRhFyb3puDkxyxOsbGA7GWekbQFNW1XOf8byt8wQfY3NXhoHI7HVhcKWtmFUiZgbY1_rlzwncFZ78Q38edxO2RX04TIlUp14bOWa1czGvdbZVx8k1GDuMfuUzTsHxY-7GmkTN2Go9YyB1SSfyWofmMLgm_blTACwo0DqAc27IvEgNJ3Q0GDLnAvYviRK1_GOcdbOgrKtj9NMbaZInfCory_JM4L4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: به دشمن هرگز اجازه نخواهیم داد پا روی شرافت و عزت ما بگذارد؛ نقاط ضعف را باید در اندرون خود حل کنیم. با قوی بودن است که دشمن را وادار به عقب‌نشینی می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/686229" target="_blank">📅 18:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
هند از چابهار دست نمی‌کشد
فایننشنال اکسپرس:
🔹
هند به تلاش‌های خود برای حفظ پروژه بندر چابهار در بحبوحه جنگ جاری آمریکا و ایران، انقضای معافیت‌های تحریمی و افزایش تنش‌های تجاری با واشنگتن ادامه می‌دهد.
🔹
با توجه به اینکه جنگ آمریکا و ایران ماه‌هاست ادامه دارد، دیگر معافیت تحریم‌های آمریکا وجود ندارد و تنش‌های تجاری با واشنگتن همچنان بر این رابطه سایه افکنده است.
🔹
دهلی نو برای ایجاد تعادل بین منافع خود در غرب آسیا اکنون با مشکل مواجه شده اما همچنان خواهان استفاده از ظرفیت‌های بندر چابهار است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/686228" target="_blank">📅 18:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d97c42fe.mp4?token=jd8J3IkFVw1nCOKb8afFjO1cIrYvVxKo2TkXobTkbgGvmGo_oCMeS4nxSfzN5CfXfFii4ZnaCQm8NTdcU-bpMVKyj_WaN99rsMECn-rBq3v5rrty08IcvGS6LXM7aWFrXe4w-XqzY2U7J10ycTJBCd_lhF36CY1hwjwAz3zWF-mG5BSRCEj5OoxwuN9NnI7AOdcPbCL0wzSq4oNekeGTdEYbAwalM5xjHAk8PV7FJ4YYsLWXOQf3yJ2nY7lAl-aNPenQdY71MJaW7cM2VuoUj1BJKtYLarkkLZwvIk45Bk5hVDI97eYnTzmjBNvR5GQCVLA-kMx636EWmTYaqjcM74WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d97c42fe.mp4?token=jd8J3IkFVw1nCOKb8afFjO1cIrYvVxKo2TkXobTkbgGvmGo_oCMeS4nxSfzN5CfXfFii4ZnaCQm8NTdcU-bpMVKyj_WaN99rsMECn-rBq3v5rrty08IcvGS6LXM7aWFrXe4w-XqzY2U7J10ycTJBCd_lhF36CY1hwjwAz3zWF-mG5BSRCEj5OoxwuN9NnI7AOdcPbCL0wzSq4oNekeGTdEYbAwalM5xjHAk8PV7FJ4YYsLWXOQf3yJ2nY7lAl-aNPenQdY71MJaW7cM2VuoUj1BJKtYLarkkLZwvIk45Bk5hVDI97eYnTzmjBNvR5GQCVLA-kMx636EWmTYaqjcM74WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: انسجام اجتماعی، مهم‌ترین معروف اجتماعی است که باید یکدیگر را به آن توصیه کنیم
🔹
هر اقدامی که اصل انسجام را خدشه‌دار کند، بزرگ‌ترین منکر است.
🔹
انسجام ملی، عامل ارتقای روحیه نیروهای مسلح و شکست دشمن بود.
🔹
بعد از لطف خدا، همت و انسجام مردم پیروزی…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/686227" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686226">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09df224f40.mp4?token=vu5wGxj2PtJBpSzQwDSkPuNbRhb35frGxKhfqmdadE0HXoM1DNmeFoGT1KZK6yJf6uehANH8I7bb8tpvrZJiE0KhUUOtyhr8PbLIpHuyTJUZ1xuNP_-7XEWzuWK4ztklh9_BafABJGkM4hl2gpyO72WbVE0-3PepGpc4oquBmkZSIuOIlc3k9qcd7CpkfIRQL-qbXXyPZIOPCVZi_OkaZgC6IijXQM4dVdkeURIyRRbqh_cLwU37XtnNi5B_27587HJ5SEnx6cVe6jEILtvVtHWAu3qBbzaQ_OxyvQ7XEgT5syumMPmkAw9aOcKPVkZmMqxElmmkiWOjlAxMJXoq5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09df224f40.mp4?token=vu5wGxj2PtJBpSzQwDSkPuNbRhb35frGxKhfqmdadE0HXoM1DNmeFoGT1KZK6yJf6uehANH8I7bb8tpvrZJiE0KhUUOtyhr8PbLIpHuyTJUZ1xuNP_-7XEWzuWK4ztklh9_BafABJGkM4hl2gpyO72WbVE0-3PepGpc4oquBmkZSIuOIlc3k9qcd7CpkfIRQL-qbXXyPZIOPCVZi_OkaZgC6IijXQM4dVdkeURIyRRbqh_cLwU37XtnNi5B_27587HJ5SEnx6cVe6jEILtvVtHWAu3qBbzaQ_OxyvQ7XEgT5syumMPmkAw9aOcKPVkZmMqxElmmkiWOjlAxMJXoq5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: نباید فراموش کرد که همین الان نیز در جنگ هستیم
🔹
پیام رهبر انقلاب، با ذکر جزئیات دقیق، تکلیف همه ما را روشن کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/686226" target="_blank">📅 18:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686225">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXyJbmxGfYmNGU3xYN9OapHfISbxKZi4N5BMssVwTnf2qUQWRkpVGXgF5Pq7ZSUOv0NJdVoq53HSMfIhHacaMbR7dCPxPez80YBbOuQ2X8hRi1caCglX70mJ15Bhzn7XXwhhjOtxr8rVwxV-V8Uus5si1MRcBp9d2RRXCdj6ArnOW8CFsKzupxP5OxiJl15sCcII2fvqHqYtX1Boq4-wf7k4igxhIb-yAKFMh2TVvrRk1HuDHpgmAAgLdXwwpzHQGfnbsVEOtKqeqmFwqVAKGRktQPZxb3vKuTNzcptesrAWv66xOeRRfwpHDncO06kDjtqgtp7uobU6glPLJvmQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایزی‌لایف حامی صعود به قله دماوند
🔹
ایزی‌لایف در ادامه رویکرد مسئولیت اجتماعی خود برای تغییر نگاه به بی‌اختیاری ادرار، از صعود مهرداد شهلایی و تیم کوهنوردی انجمن ام اس به قله دماوند حمایت کرد.
🔹
این صعود در ۳ شهریور انجام شد تا بار دیگر بر یک پیام مهم تأکید شود: بی‌اختیاری ادرار نباید محدودیتی برای یک زندگی فعال باشد.
🔹
ورزش، طبیعت‌گردی، سفر و دنبال کردن تجربه‌های تازه، همچنان می‌تواند بخشی از زندگی افراد باشد؛ حتی زمانی که با بی‌اختیاری ادرار زندگی می‌کنند.
🔹
ایزی‌لایف در کنار تولید محصولات مدیریت بی‌اختیاری ادرار، تلاش می‌کند با فعالیت‌های مسئولیت اجتماعی و افزایش آگاهی، به شکستن تابوی صحبت درباره بی‌اختیاری ادرار و تغییر نگاه جامعه نسبت به این موضوع کمک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/686225" target="_blank">📅 18:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686224">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dffdbc0af.mp4?token=C2TV9ZO20vWXjfrev2KwUURTGiHbX_az1hzg_qsPRu9yTku7ytwRg34DuXiXNTc3inhTXf1RpTle-GkNnsXQDNNL7bNAOT1A0QkHuuqP-x_S5r0aYcU5ktdx-EVYkAJnBHUDmtnGf1C1CfbrNnBDQM3IoJ38pcmXD8Zyv-KcnrKfevtD0Ai75u3W_K-9idMPYqYbVUOObUndvu2Hv1ozzJtXOgNRFkjDNugW0XQN_zJf22Ic6fxrlFU8Qlzwa6XWWv4LVDLJtuEacKFzmrYvs80lh6Imh_B_8SULXoFBpdGG-4C8z9anz5GLFITBmhRiRmwHIct9wANGH1jl9zwBtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dffdbc0af.mp4?token=C2TV9ZO20vWXjfrev2KwUURTGiHbX_az1hzg_qsPRu9yTku7ytwRg34DuXiXNTc3inhTXf1RpTle-GkNnsXQDNNL7bNAOT1A0QkHuuqP-x_S5r0aYcU5ktdx-EVYkAJnBHUDmtnGf1C1CfbrNnBDQM3IoJ38pcmXD8Zyv-KcnrKfevtD0Ai75u3W_K-9idMPYqYbVUOObUndvu2Hv1ozzJtXOgNRFkjDNugW0XQN_zJf22Ic6fxrlFU8Qlzwa6XWWv4LVDLJtuEacKFzmrYvs80lh6Imh_B_8SULXoFBpdGG-4C8z9anz5GLFITBmhRiRmwHIct9wANGH1jl9zwBtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه: انسداد تنگه هرمز برنامه‌ریزی شهید پاکپور بود
🔹
شهید پاکپور پیش‌بینی کرده بود که جنگ با ترور او شروع می‌شود؛ شهید پاکپور برنامه‌ریزی کرده بود که اگر جنگ آغاز شد و او دستوری صادر نکرد، فرماندهان ۲۰ دقیقه بعد شلیک کنند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/686224" target="_blank">📅 18:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686223">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b450dc735.mp4?token=UhnfXsePf7afhEkJgTb2lzmLEUxnLRvvDwZGkyu8JYNQWwly6ZMJ52cdINp2QE6LkSjrLHWeQ-wWuQLGRefwSO4_8FedwPQR2pvcaT7pD084kKdoicjqUyZlZwrZd2TZJaiCB8WgJGb_06YZoLizkBBni7SWdxH9O2sW7fH727WALYBsBd794qMuWUUPcZHlPSnY7BM1RcALCdBcGm4kKv5DFTLuOq2zHFPjt6OdJJO8R_0GMNzifVbDgdkFTo_Qn23Y0rjsKxScZJJFa2jAPLxErS5uZUq6J0KGjrHjR1xVMMrnNreQCSCkuGUIwX-hWQLn_yMs00WU_bOQpuMZ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b450dc735.mp4?token=UhnfXsePf7afhEkJgTb2lzmLEUxnLRvvDwZGkyu8JYNQWwly6ZMJ52cdINp2QE6LkSjrLHWeQ-wWuQLGRefwSO4_8FedwPQR2pvcaT7pD084kKdoicjqUyZlZwrZd2TZJaiCB8WgJGb_06YZoLizkBBni7SWdxH9O2sW7fH727WALYBsBd794qMuWUUPcZHlPSnY7BM1RcALCdBcGm4kKv5DFTLuOq2zHFPjt6OdJJO8R_0GMNzifVbDgdkFTo_Qn23Y0rjsKxScZJJFa2jAPLxErS5uZUq6J0KGjrHjR1xVMMrnNreQCSCkuGUIwX-hWQLn_yMs00WU_bOQpuMZ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: تا زمانی که تعهدات آمریکا در تفاهم‌نامه اجرایی نشود تنگه باز نخواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/686223" target="_blank">📅 18:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686222">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff0f494e4.mp4?token=pvZ_dElzh0CAVMjW2uCCyYAIXLKoGtZcAF9L79YiiWPslnIkwLbn7ng0iPS_Ma5j07pafnA5Xkgi0G0GICUFK60ezzw-AS5tvSAumTDkTI8YOXaZRa28JxCA7ygZyajqFiwWn2lvF4X5NQDeOiB6qVw959-agJPrgfTuWkoehRGY5NPmxG2FPCdANFsNH3AnYjPHO3YB-TVXb3DP6WdJFJ8R_seZyQOLeHhNAIMGsa1j5ZkIVAIQinfkW4p9bYyFuwDebnZI8d0F66g-Y05kTF5kGjgOsOPTo_Bmxfx6VP_ogYkNJ2ZL9DKq-OoJ_loR6j9JNukTVtVtDkZnkiwzqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff0f494e4.mp4?token=pvZ_dElzh0CAVMjW2uCCyYAIXLKoGtZcAF9L79YiiWPslnIkwLbn7ng0iPS_Ma5j07pafnA5Xkgi0G0GICUFK60ezzw-AS5tvSAumTDkTI8YOXaZRa28JxCA7ygZyajqFiwWn2lvF4X5NQDeOiB6qVw959-agJPrgfTuWkoehRGY5NPmxG2FPCdANFsNH3AnYjPHO3YB-TVXb3DP6WdJFJ8R_seZyQOLeHhNAIMGsa1j5ZkIVAIQinfkW4p9bYyFuwDebnZI8d0F66g-Y05kTF5kGjgOsOPTo_Bmxfx6VP_ogYkNJ2ZL9DKq-OoJ_loR6j9JNukTVtVtDkZnkiwzqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: در آغاز گفت‌وگوها، آمریکا یک متن ۱۵ ماده‌ای در خصوص هسته‌ای، موشکی و محور مقاومت ارسال کرد؛ اما امروز وقتی متن ۱۴ ماده‌ای نهایی را نگاه می‌کنید، می‌بینید دشمن از همه آن‌ها عقب‌نشینی و رئیس‌جمهور آمریکا پای این سند را امضا کرد
🔹
چارچوب مذاکراتی…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/686222" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686221">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
قالیباف: در برق مشکل جدی داشتیم که با همراهی مردم حل شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/686221" target="_blank">📅 18:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686220">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65bc99871.mp4?token=MIDKUu6A2AIwoFxX1TT4MdExjXAN6UDcgtSsHtnmcSlbtcml8jIc2DeJsjYFpY9uaba00HBNnNKkrNuMoA9gMEJbmWTG9lelH2MF8vTmjsclRjraRruI2lg0GtY-ZKnpwRY1iFKUIPWsuIn1CObxgCtOW3fJoiAenRsNSFc-ZtJ2yVkihl4i-8ugNvBWdLQBK8h534JAAvdIVSHaZEXOJG3FmJOeAf-uQSatjlTT3DF7VLFBRAAil8QHH_WwaTrAMAHN_JNmX0CqWyPJyyiiffkBVtfu_PQxkQDO6VNKys8J4iwFI6RXmCNlL6QgSuKHt2TJJ9Pqiss9RTxv5bHpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65bc99871.mp4?token=MIDKUu6A2AIwoFxX1TT4MdExjXAN6UDcgtSsHtnmcSlbtcml8jIc2DeJsjYFpY9uaba00HBNnNKkrNuMoA9gMEJbmWTG9lelH2MF8vTmjsclRjraRruI2lg0GtY-ZKnpwRY1iFKUIPWsuIn1CObxgCtOW3fJoiAenRsNSFc-ZtJ2yVkihl4i-8ugNvBWdLQBK8h534JAAvdIVSHaZEXOJG3FmJOeAf-uQSatjlTT3DF7VLFBRAAil8QHH_WwaTrAMAHN_JNmX0CqWyPJyyiiffkBVtfu_PQxkQDO6VNKys8J4iwFI6RXmCNlL6QgSuKHt2TJJ9Pqiss9RTxv5bHpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ۱۵ الگو را یاد بگیر؛ گرامر انگلیسی را فتح کن #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/686220" target="_blank">📅 18:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686219">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c97aefd083.mp4?token=AdEU6utku4ocFTiuNXQVNM1ERBRVRTY4OdC_ou1goEjS_0PFhkrQHUyWZ4Qb-hmnicwbn1d2NJLgplWTyBCZT3GIK6gM_QG5MGqnOTmPjpBYc8_lhAsQ-V4Dwjh5yLJBnAMXcS3gc6oy7bgbhN76Tgp79dDyhSC-hZJIPfhDmhYNUjavat9VMDi_vEVU356JKoT_fMs34G6Gdi_KJhGDeX9-HaxXGiwbX_99fvMIxlkk1NVOo8jTQrczMklFAIw2xB1dXcwIJId_ahuwfYOMRabIC5WXv2gug-P2uo0TgkzN12tW34cI8w3kLjl9mVSMRWbe3SrV5j2LVDelcl7i5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c97aefd083.mp4?token=AdEU6utku4ocFTiuNXQVNM1ERBRVRTY4OdC_ou1goEjS_0PFhkrQHUyWZ4Qb-hmnicwbn1d2NJLgplWTyBCZT3GIK6gM_QG5MGqnOTmPjpBYc8_lhAsQ-V4Dwjh5yLJBnAMXcS3gc6oy7bgbhN76Tgp79dDyhSC-hZJIPfhDmhYNUjavat9VMDi_vEVU356JKoT_fMs34G6Gdi_KJhGDeX9-HaxXGiwbX_99fvMIxlkk1NVOo8jTQrczMklFAIw2xB1dXcwIJId_ahuwfYOMRabIC5WXv2gug-P2uo0TgkzN12tW34cI8w3kLjl9mVSMRWbe3SrV5j2LVDelcl7i5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: مقصر بخشی از مصرف زیاد بنزین مردم نیستند بلکه مقصر صنعت است
🔹
مسئله بنزین را می‌شود با صرفه‌جویی حل کرد. اصلاحات ضروری باید حتماً با خرد جمعی و همراهی مردم، به‌گونه‌ای باشد که فشار بر روی مردم کمتر شود.
🔹
رضایت مردم اصل اول ماست. هرجا درباره مسائل…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/686219" target="_blank">📅 18:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686218">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e47ef015.mp4?token=PKmb5pN_AmFOxzerZCpuivglYnkLndIFhfDC8CeiqdMMZDdH8UmVollwYpeq8O-NYJ5XwZoky7QY6_MrE6or1SnMaJW_x5AMcKg6FORVxnowYby4IDbAywhD8saKI4O6fejPffBbPvL_a5t6y15cpSvrDivovx5PMhuyr8l9ySHJupLuS8u-87y4vZU4VbEtamGYBORo47mFTIdD2--F5GxPAzRfFfutEcRTszO4nqXkHMsUgm6k4caxULIglzlanpnSTeJEYFaQ8KYY3DuFCTXlA3AcxHI6ETn-gr5skoWjM_C72ED26lE1Ot0ZOEyfK7kOTpxyAsTDL-lVBvhfgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e47ef015.mp4?token=PKmb5pN_AmFOxzerZCpuivglYnkLndIFhfDC8CeiqdMMZDdH8UmVollwYpeq8O-NYJ5XwZoky7QY6_MrE6or1SnMaJW_x5AMcKg6FORVxnowYby4IDbAywhD8saKI4O6fejPffBbPvL_a5t6y15cpSvrDivovx5PMhuyr8l9ySHJupLuS8u-87y4vZU4VbEtamGYBORo47mFTIdD2--F5GxPAzRfFfutEcRTszO4nqXkHMsUgm6k4caxULIglzlanpnSTeJEYFaQ8KYY3DuFCTXlA3AcxHI6ETn-gr5skoWjM_C72ED26lE1Ot0ZOEyfK7kOTpxyAsTDL-lVBvhfgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: دولت و مجلس مصمم به افزایش کالابرگ، مخصوصاً برای دهک‌های ضعیف جامعه هستیم و در اولین فرصت اجرایی می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/686218" target="_blank">📅 18:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686217">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxAFMKlefvzSpf7PUgY4CXVSsY6d7tdBSUjXprJbMxb3RnbgKaGCqfwWaiuf3_YV1uHdAr38SWaclZjnW-cK2hxzeDPZSmKel5VMuMH3adTVQ-pk8RWxvAlnnhDN-I7PIY1HscMCsQK9McxqzZernEVbl8klgoyVdkzyb7Z89qOqkpsEPibaSYMQx75lcCbTvm_EM1SwYIs8vAMwkX78cOI87HWGSXu5QhFOXdmh3M_UHe7mp_u9_qaS_GUYsFaukPnY4uBYA29zLcjGFxHVvcOkh9mCZceE-PcxhbPcS27ziX7TcFkZ3G5by81lwHzjQzBjvH4fzGUhxz-I5UbREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار سیاه بلیت دربی داغ شد؛ تا ۷ میلیون تومان!
🔹
با وجود فروش رسمی بلیت دربی استقلال و پرسپولیس، قیمت‌ها در بازار سیاه به ۲ تا ۷ میلیون تومان رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/686217" target="_blank">📅 17:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686216">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ec52fc94.mp4?token=MtAlNpi5iRdML5IfQRTTtRO2MZOqGd5wDLr14dF5-r8kUGtBVdN9HB4DHnfHNJQ-hQjHD83BKRtfuG7LWQek5S-mGVfV4es3P_8wmrxlyVRFRa31vFzy-4TCFhyEK78Twm54QbmafG2w3kkjEDYyP7kLWIT2qvwXCSQkcmBDfvaNupuqhbpugEG47Ip3XOgCvzaajSXBxDdRcCYl9uCAImWc_vYWkYbfdxS9Xw7UJRjjYuv19kVg8sDBaVUF0ZhfiyxmJja33ufbWTygAyWCG_Qgs7IUVkn6KnDcxHCJYi9mwtVO73sgOw6NZwGP8OOoA7qhmiE6xcdK8Wp2O1QEJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ec52fc94.mp4?token=MtAlNpi5iRdML5IfQRTTtRO2MZOqGd5wDLr14dF5-r8kUGtBVdN9HB4DHnfHNJQ-hQjHD83BKRtfuG7LWQek5S-mGVfV4es3P_8wmrxlyVRFRa31vFzy-4TCFhyEK78Twm54QbmafG2w3kkjEDYyP7kLWIT2qvwXCSQkcmBDfvaNupuqhbpugEG47Ip3XOgCvzaajSXBxDdRcCYl9uCAImWc_vYWkYbfdxS9Xw7UJRjjYuv19kVg8sDBaVUF0ZhfiyxmJja33ufbWTygAyWCG_Qgs7IUVkn6KnDcxHCJYi9mwtVO73sgOw6NZwGP8OOoA7qhmiE6xcdK8Wp2O1QEJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: اگر محاصره را تشدید کنند، حتماً پاسخ نظامی می‌دهیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/686216" target="_blank">📅 17:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686215">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: ناتو اسلامی را باید ایجاد کنیم
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
اشتراکات فرهنگی، دینی، اعتقادی و تاریخی کشورهای اسلامی به اندازه‌ای گسترده است که می‌توان با کنار گذاشتن اختلافات، به یک وحدت و همگرایی منطقه‌ای قوی رسید و زمینه تشکیل یک ناتو اسلامی را برای مقابله با زیاده‌خواهی صهیونیست‌ها و استکبار جهانی فراهم کرد.
🔹
تحقق این وحدت نیازمند آن است که کشورهای اسلامی با تکیه بر منافع مشترک و واقعیات میدانی، از وابستگی به قدرت‌های خارج از منطقه فاصله بگیرند و با تصمیم‌گیری مستقل، مسیر همگرایی و همکاری منطقه‌ای را دنبال کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/686215" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686214">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6410ffa96.mp4?token=h1h4FJnMEdWIGZr4I2x_KF9vnsV0SCVvy3m9Ojzgsf8yuhhMXMJNEnuFaITDAXbnmLZmFeHH7Erh0-kXW1v7wJMdDRDsE4Q9dVt4YnLshNoSRLoxvIOsI3NcCFuyfyUIUy5BUwyIinVLzWxwHZ6abcbSNrzjsR3KO09kLRrO3NKN-_YXrOMLkBG2liSeiyjZ20Sjh42RJbX4uOpR10A-pNGmK5bNgyhGk8IIkW0TpGIztR_3v-PgxnXK1bsOCjN4I8ClyZnVorXhZ5EmuM5tNQKcTLTGr5epYH-GyQFF-4jEZFLRPpBDQoFZuKNrZ-1mUUEoy9n4cU8IIW5faTgFFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6410ffa96.mp4?token=h1h4FJnMEdWIGZr4I2x_KF9vnsV0SCVvy3m9Ojzgsf8yuhhMXMJNEnuFaITDAXbnmLZmFeHH7Erh0-kXW1v7wJMdDRDsE4Q9dVt4YnLshNoSRLoxvIOsI3NcCFuyfyUIUy5BUwyIinVLzWxwHZ6abcbSNrzjsR3KO09kLRrO3NKN-_YXrOMLkBG2liSeiyjZ20Sjh42RJbX4uOpR10A-pNGmK5bNgyhGk8IIkW0TpGIztR_3v-PgxnXK1bsOCjN4I8ClyZnVorXhZ5EmuM5tNQKcTLTGr5epYH-GyQFF-4jEZFLRPpBDQoFZuKNrZ-1mUUEoy9n4cU8IIW5faTgFFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: با همراهی مردم از این جنگ عبور می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/686214" target="_blank">📅 17:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686213">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین دلیل رواج پیدا کردن خریدهای اینترنتی چیست؟</h4>
<ul>
<li>✓ امکان خرید اقساطی</li>
<li>✓ مقایسه آسان‌تر قیمت‌ها و کالاها</li>
<li>✓ تنوع بیشتر محصولات</li>
<li>✓ تخفیف‌های دوره‌ای</li>
<li>✓ صرفه‌جویی در زمان</li>
<li>✓ تحویل آسان درب منزل</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/686213" target="_blank">📅 17:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686212">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
بازار دارو در ایران ۴۰۰ همتی شد
🔹
بازار تأمین دارو در ایران در سال ۱۴۰۴ به حدود ۴۰۰ هزار میلیارد تومان رسید؛ بازاری که همزمان با رشد تولید داخلی، از مرز ۵ میلیارد دلار عبور کرد.
🔹
تولید داخلی دارو از ۵۱.۴ میلیارد عدد در سال ۱۴۰۳ به ۵۷.۴ میلیارد عدد در سال ۱۴۰۴ رسید.
🔹
رشدی ۱۱.۶ درصدی که نشان‌دهنده افزایش قابل‌توجه حجم تولید در صنعت داروسازی کشور است؛ ارزش دلاری بازار نیز از ۴.۵ میلیارد دلار به حدود ۵ میلیارد دلار افزایش یافت.
🔹
رقمی که از این میان حدود ۸۵۰ میلیون دلار سهم واردات و ۴.۱۵ میلیارد دلار سهم تولید داخل بوده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/686212" target="_blank">📅 17:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686211">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc31ca13a.mp4?token=OvLg_N0TbKcOvhHRglNY5Fsz9t_raXFB-2wfwQoUz-3VtSGmzKshAfuAgMzt-mcsHbs8-B2U1dVf2xpV2WEwpnARuVsg0IS1Fw-XAP1XLpyezJe2oz94rXLwB-PoNZN1S71l20LbXP7JiVJLYX-JtHxNHYqMaWYBHB3oFOxwh5xvmZNQuIjMx9Ge8cUspto_ch7e4St07vNb41f-wFdywjVZbYHKnY5OquOG3652HngdY2Q5tMzmo43IVNc__7OAfHEG5UJocsSjgg54LorkXBIX0hsVFk2SbA-HZnofpwZVFvJ0en1KnaJ1lfDdfhn1Tfgqi1rSD0IBoBrJdlNvpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc31ca13a.mp4?token=OvLg_N0TbKcOvhHRglNY5Fsz9t_raXFB-2wfwQoUz-3VtSGmzKshAfuAgMzt-mcsHbs8-B2U1dVf2xpV2WEwpnARuVsg0IS1Fw-XAP1XLpyezJe2oz94rXLwB-PoNZN1S71l20LbXP7JiVJLYX-JtHxNHYqMaWYBHB3oFOxwh5xvmZNQuIjMx9Ge8cUspto_ch7e4St07vNb41f-wFdywjVZbYHKnY5OquOG3652HngdY2Q5tMzmo43IVNc__7OAfHEG5UJocsSjgg54LorkXBIX0hsVFk2SbA-HZnofpwZVFvJ0en1KnaJ1lfDdfhn1Tfgqi1rSD0IBoBrJdlNvpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: هدف دشمن از جنگ ترکیبی این است که در داخل کشور، اغتشاش را به همراه ترور و حملات نظامی کوتاه آغاز کند
🔹
نقشه دشمن برای همه مسئولان ما روشن است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/686211" target="_blank">📅 17:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686210">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a80eb3ed.mp4?token=Avbfr1Nl0PT77X6djT5a5_9eTdBKIFf1GzaXkusxACeqFQiGUuwTcWQOcRgQyy55i_jMt4fI1A1QPLeDgl9oOqz_7_feRgSvrATW-IXLxfy-Nw9nnKD4FvrjulcFNM6nSEJ-7EUvlzWc3ZN9Mz41rXpSDc7889IMdC6g7w64vl0VcIHN4q1iGvD5LBmQ2VbIA2-gH9P5ZKluyYJU7ZwE77F_H7EjAKFwsA3_sjqyZzCNslxbeB8VGKKF7k3o3zOtagBQE7O7t1XKtLDyl-UOSbcTySlLdsMtdRZkrTd-VbkCsYQlSRCj5oBA7cCxG3kIJuaMhvEXUPrsYyJOXR0OFXdhLoGpWMiaPlyYIk26qO5BFnHAGgYzIBjFElhiub0tLwmzqLPjlahZb4O0bcXf9iggsOD-0cWRzZCe8uqXlTJOxJnJL1omv8MrEQFIDFAMN5V25rpCttcasr-cJHvAl4sn_1JW-kNQ0R2AJY0X7ilClUiF3yA8Dn6X-G8ji25-4GIqxe1hTkFqhNqBqm8iuvz25fJroq7A4TPZV0nQ9xgX2ORUR65kwSR7KFcooQRDsEfMezUIl4-bpBULc73ueAWJwTev8sBgnMTsa60xAXpa38kKz4C9JWY-PvIlmvWvtAXvG-jBm9pXpTTNQpv2B34n0QiKiXCHOtv6cykC4Wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a80eb3ed.mp4?token=Avbfr1Nl0PT77X6djT5a5_9eTdBKIFf1GzaXkusxACeqFQiGUuwTcWQOcRgQyy55i_jMt4fI1A1QPLeDgl9oOqz_7_feRgSvrATW-IXLxfy-Nw9nnKD4FvrjulcFNM6nSEJ-7EUvlzWc3ZN9Mz41rXpSDc7889IMdC6g7w64vl0VcIHN4q1iGvD5LBmQ2VbIA2-gH9P5ZKluyYJU7ZwE77F_H7EjAKFwsA3_sjqyZzCNslxbeB8VGKKF7k3o3zOtagBQE7O7t1XKtLDyl-UOSbcTySlLdsMtdRZkrTd-VbkCsYQlSRCj5oBA7cCxG3kIJuaMhvEXUPrsYyJOXR0OFXdhLoGpWMiaPlyYIk26qO5BFnHAGgYzIBjFElhiub0tLwmzqLPjlahZb4O0bcXf9iggsOD-0cWRzZCe8uqXlTJOxJnJL1omv8MrEQFIDFAMN5V25rpCttcasr-cJHvAl4sn_1JW-kNQ0R2AJY0X7ilClUiF3yA8Dn6X-G8ji25-4GIqxe1hTkFqhNqBqm8iuvz25fJroq7A4TPZV0nQ9xgX2ORUR65kwSR7KFcooQRDsEfMezUIl4-bpBULc73ueAWJwTev8sBgnMTsa60xAXpa38kKz4C9JWY-PvIlmvWvtAXvG-jBm9pXpTTNQpv2B34n0QiKiXCHOtv6cykC4Wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی پربازدید در فضای مجازی از مراسم افتتاحیه جام‌جهانی بازی‌های محلی در قرقیزستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/686210" target="_blank">📅 17:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686209">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادامه توهمات وزیر خزانه داری دولت تروریستی آمریکا
🔹
اسکات بسنت، وزیر خزانه‌داری دولت تروریستی آمریکا مدعی شد که با ایران هیچ مماشاتی نخواهد شد .
🔹
او مدعی فشار اقتصای بسیار سنگین بر ایران شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/686209" target="_blank">📅 17:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686208">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bf6ee6b0.mp4?token=TdK2-CR3EZZgbi4LcdedEYNutvZddzsOKmwYKX6FkrsJmrc34YX0saCv4L6U0L__kDYaWctbV3WOJ0R2v1CWr6qpM4b3sUxVbM-jopdL2ngrGzd4E8iHfDx9MqrWfzzf-mbUaoAVieDQjWgtZ8BDaEcSpMYfSa7MqSe3uUxLzj-rCXJoFx2aoeLeoxZ1OsMcjcl8Om66tukn5SwypWK3PDN54B6R00NkakC1HN9Thi16k6Y2riqMaBxYoB9EnhQeKMvegKiCp7F6o2h1KMZ1p-lTmwnvnQGkprEPZGWY-6JRky2AydIvShKgrmi_BYDRYWXzXy0dFthm_RgKkGe7qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bf6ee6b0.mp4?token=TdK2-CR3EZZgbi4LcdedEYNutvZddzsOKmwYKX6FkrsJmrc34YX0saCv4L6U0L__kDYaWctbV3WOJ0R2v1CWr6qpM4b3sUxVbM-jopdL2ngrGzd4E8iHfDx9MqrWfzzf-mbUaoAVieDQjWgtZ8BDaEcSpMYfSa7MqSe3uUxLzj-rCXJoFx2aoeLeoxZ1OsMcjcl8Om66tukn5SwypWK3PDN54B6R00NkakC1HN9Thi16k6Y2riqMaBxYoB9EnhQeKMvegKiCp7F6o2h1KMZ1p-lTmwnvnQGkprEPZGWY-6JRky2AydIvShKgrmi_BYDRYWXzXy0dFthm_RgKkGe7qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: قدرت نظامی ایران در تنگهٔ هرمز حفظ و ارتقا پیدا کرده است
🔹
اعمال مدیریت ایرانی بر تنگه، هیچ منافاتی با قوانین بین‌المللی ندارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/686208" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686207">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIrb6SRpczoZlH235mLsfusOg3ajFwkCB5oBzn75a2VlRYDdTJp_TWcqABdl_ovVNERBp6iTWYZVtZF2WHd4WnBb-X3anOJgztjHO4GDAjauupZUBt3t3byAU6oFeiRn-Si7PIxb5P8vjchxZrxVhEzT7W4t62GA4E3OHIYjPeUO30qhlM8VoLNnfoxkkoVS-_vE9DvezhkgjrLF9pp37buzd_DwnbFF_z4ahM06mGZmS0Lvm9mwFkx8zLFO5HWIsMI-ccjJPK9jd6F1feuK5e3fd2xNkON7AekKe5LHlgxmyWIOu_gs2fXTzHfxdQoFiKfesx33lp-i5b1cDPZ-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی کریمی پس از دعوا با هواداران رضا پهلوی، گوشه‌نشین شد
🔹
او پیش از این نسبت به فحاشی سلطنت‌طلبان گلایه کرده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/686207" target="_blank">📅 17:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686206">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3345c0aee0.mp4?token=nTXHDw2b87FuB0kcw3mIL72DI1ms-DEW-Ry-FXYM4EfwMEOo2ZJOnc_ENS6VRjWfXFm7h7mPHY1sJTGhH9zFHyN_VLvWP1bQTbsYuNsFXuOkNzRR-VuopwQpKWaAZxKA2KuUdoQ0o0sxA-MhWx_xoH4G39pJgcOdxkYexMrOl0ufGMPj4ZFUZ0g_i5DQEyKsl92JSG_xqi75FFzYevSjmPZ9T3VfoN_-YM6SnQrcG4Zio9ABAbkA5RmDlEAQoHXiQxM8Bon4xVC3by811HHbSIsm-OUlhXOeSvcw6uJBugfc1LcNkiE9-1iTfV2N9e1l9enc8J_JerNP_-2A9lUZnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3345c0aee0.mp4?token=nTXHDw2b87FuB0kcw3mIL72DI1ms-DEW-Ry-FXYM4EfwMEOo2ZJOnc_ENS6VRjWfXFm7h7mPHY1sJTGhH9zFHyN_VLvWP1bQTbsYuNsFXuOkNzRR-VuopwQpKWaAZxKA2KuUdoQ0o0sxA-MhWx_xoH4G39pJgcOdxkYexMrOl0ufGMPj4ZFUZ0g_i5DQEyKsl92JSG_xqi75FFzYevSjmPZ9T3VfoN_-YM6SnQrcG4Zio9ABAbkA5RmDlEAQoHXiQxM8Bon4xVC3by811HHbSIsm-OUlhXOeSvcw6uJBugfc1LcNkiE9-1iTfV2N9e1l9enc8J_JerNP_-2A9lUZnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: دشمن بداند در دوره‌های بعدی جنگ، هم در بُعد کیفی و هم کمی، مسلط‌تر خواهیم بود
🔹
نیروهای مسلح از هر فرصتی که به آن‌ها بدهیم برای بازسازی توان خود استفاده می‌کنند و حتی ساعت و لحظه‌ها را هم از دست نمی‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/686206" target="_blank">📅 17:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686205">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
توانیر: خاموشی‌ها به تدریج تا اواسط شهریور پایان خواهد یافت.
🔹
پزشکیان در حاشیه اجلاس سران شانگهای با دبیرکل سازمان ملل دیدار و گفت‌وگو کرد.
🔹
سخنگوی داعش در یمن کشته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/686205" target="_blank">📅 17:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686203">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9mrvPqpY95fHf-J-uhtKml6bsc105UjmaYFSpbGh6G_KxeIwZ33BvHcM5wfyHcs_F82cABBiswqDxOd5lYpQHI3cAxJSH67usZurCiAZUQCDgni-DdUZdWuIgYaybfhs4lLv8r6u_V3Fyy_beIhSlb_kLWfcd13xQE6vjbXHISnqihq-nPiDXR_IJUMdBE2LHczWMcPVrXuSmT5TPK0S6QKpet66jhmVcFGqwkpOCSAS078uYcuTvj_OoQfnkpVJSLZAwDfBfJFBthVf5YSH97ZaEQlzkKzNxfRIH5jvvL5XHqihdx0Il6Ip5C5UE92zmhX7bRz6NJLoDqgpiCF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
رونمایی از کارت اعتباری گردشگری ریالی و ارزی بانک رفاه کارگران با حضور وزرای رفاه و‌ میراث فرهنگی
🔹
در راستای رونق صنعت گردشگری و با هدف فراهم‌ کردن امکان دریافت و استفاده سریع از کارت‌های اعتباری گردشگری ریالی و ارزی، بدون نیاز به مراجعه حضوری، سامانه صدور آنی این کارت‌ها، توسط بانک رفاه کارگران رونمایی شد.
🔹
مراسم رونمایی از این سامانه به عنوان نخستین سامانه رسمی صدور کارت‌های مذکور در کشور، با حضور دکتر میدری وزیر تعاون، کار و رفاه اجتماعی، دکتر صالحی ‌امیری وزیر میراث فرهنگی، گردشگری و صنایع دستی، دکتر للـه‌گانی مدیرعامل بانک رفاه در محل این بانک برگزار شد.
🔹
این سامانه در راستای تسهیل پرداخت‌های بین‌المللی و پاسخ به نیاز کاربران برای خریدهای اینترنتی ارزی و ریالی، پرداخت هزینه سرویس‌های آنلاین و استفاده از خدمات جهانی، توسط شرکت دانش رفاه پردیس از شرکت‌های زیرمجموعه این بانک در بستر پلتفرم Payval راه‌اندازی شده است.
🔗
متن کامل خبر
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/686203" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686202">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243c55f1cd.mp4?token=frKKy6Jr0nDbcZ0VRsGmegM0XhsuvExiBkuz02A26H4pSqSqPfxO9uGoW31FFvnDo06H9aK1tKj9gFlLNI-NOLnyg49OdzSI54ma4B5PPz-Tm-7m0TQbXzx7qWoOYYwI5AwkDKrLyUpD7Pp_3xHaB-1GYp0lmr8nEOg8L0QYAsPA7oaF0WOIEjT7eOdWPQI89c51xhjgDfn85fbzY8Ap2HL9lAZ0Lr9_cduiJ1nyWGqKEsv8V18_vreA6j9RtoktDn_OxeYQGJO2OTW-tBbbh0J8eOmLNi2LM6r0NHq5V34vDFxZ5rfC7SGRo_IVOXvw2U8S2yqxobkIzieW1oQT6oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243c55f1cd.mp4?token=frKKy6Jr0nDbcZ0VRsGmegM0XhsuvExiBkuz02A26H4pSqSqPfxO9uGoW31FFvnDo06H9aK1tKj9gFlLNI-NOLnyg49OdzSI54ma4B5PPz-Tm-7m0TQbXzx7qWoOYYwI5AwkDKrLyUpD7Pp_3xHaB-1GYp0lmr8nEOg8L0QYAsPA7oaF0WOIEjT7eOdWPQI89c51xhjgDfn85fbzY8Ap2HL9lAZ0Lr9_cduiJ1nyWGqKEsv8V18_vreA6j9RtoktDn_OxeYQGJO2OTW-tBbbh0J8eOmLNi2LM6r0NHq5V34vDFxZ5rfC7SGRo_IVOXvw2U8S2yqxobkIzieW1oQT6oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: آمریکا می‌خواهد برخلاف تفاهم‌نامه از مسیر جنوبی تنگه هرمز عبور کند که این اجازه را نخواهیم داد
🔹
قبل از جنگ، روزانه حداقل ۱۲۰ کشتی از تنگه هرمز تردد می‌کرد و حتی اگر یک یا دو کشتی هم از تنگه عبور کند، به هیچ عنوان قابل مقایسه با قبل از جنگ نیست.…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/686202" target="_blank">📅 17:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686201">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50979ed6b9.mp4?token=LCnWsRjA5AaLZQb9yCFZThLQ4hCyFbOqelfvbqRcMTOTpcEP0anD5lQFQvtLpKBM7j2hLbQMNL1kNV6XIsKKu4n_gzgXyjd42acuqaS3qAtzVUdrbwY_WQ6IMlZoDxTst7dqLLwQZqDg1oEJcMg9aUJsCRI5Ad4KfNKk0_FFPqusbRD6QdEfZuUmkpV_QwKP512YwWG6zO2wlMoQ_9uafeSUIsPBz4Uv7T2kq0m4N0rPJ3EhdsSjOJhumxt7nJLbcQI2pLXugXMbGC_YK-kWZck70y9TgTSWX5LXXGcE8vMWSHiDYR-sQN4oI5YgHbpFMdsYVRnuc5AZFYXxqTb05w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50979ed6b9.mp4?token=LCnWsRjA5AaLZQb9yCFZThLQ4hCyFbOqelfvbqRcMTOTpcEP0anD5lQFQvtLpKBM7j2hLbQMNL1kNV6XIsKKu4n_gzgXyjd42acuqaS3qAtzVUdrbwY_WQ6IMlZoDxTst7dqLLwQZqDg1oEJcMg9aUJsCRI5Ad4KfNKk0_FFPqusbRD6QdEfZuUmkpV_QwKP512YwWG6zO2wlMoQ_9uafeSUIsPBz4Uv7T2kq0m4N0rPJ3EhdsSjOJhumxt7nJLbcQI2pLXugXMbGC_YK-kWZck70y9TgTSWX5LXXGcE8vMWSHiDYR-sQN4oI5YgHbpFMdsYVRnuc5AZFYXxqTb05w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: آمریکا در تنگهٔ هرمز تلاش می‌کند مثل دزدان و قاچاقچیان چند کشتی را عبور دهد اما با مقابله نیروهای مسلح ایران مواجه می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/686201" target="_blank">📅 17:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae9c37b57.mp4?token=qZ__swqbXEDqHSTXfoJC2vgBOMAvO9mcRkwJ0Y5hXxKN6tlTCfIEV3G3NW1uALtvgH2rUieeKHMhnuJXABnwyRnpMm9ozNoz1s6PywmHmS2ISDOh2f4WVWW2mRyVl514P2BNFAm5AK3a5S7FDr5Pp5xpYxm8_pH10Czjnk_nhex3Ct-eWEdntK-IoH-ve1ui2cdDQE22jjRB8ealq3iiUG0dWqhBV0APgWlMAvmud88rfwMNubvxb9DvpYLA6F37aYtcoP9iW_rDp1a57FSVPE_umjbLzgk7LF2XpMqlkj9kDQMQJaE23mTcMuifnViOm65Z6b2ABrRg36pG7lfw0Uf-9WX3dMiwwvtrRwZGvLb1Y8YxWBZfOow0VT6cnkXxkv8LG1CBP6uo4zMCWOxNaaCCDSQD36iadI603GIceE0edHMp1wQGFnvz-APDSs7O78Re1C6lhLbMWD1MP2OIfvSdO_tViJ2CJgzW_NS_ztG9pmNkqQJMWp3xrh4aCCqMeqbrbElBRYemFKqWdzfwFNiW0pvDe5Onp4KYcQ6k3qYnEFnkPnea31i2kYeLsFitE5jzK40NAStF-PnmOz3ukhEYvd5zvj8BsIqhB1jyVGkL03XDC1EZr7UXERHjW7fdZuDw-sBXHdwis98yPRsm_6-ne40uoqvXXyYlNU9wGMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae9c37b57.mp4?token=qZ__swqbXEDqHSTXfoJC2vgBOMAvO9mcRkwJ0Y5hXxKN6tlTCfIEV3G3NW1uALtvgH2rUieeKHMhnuJXABnwyRnpMm9ozNoz1s6PywmHmS2ISDOh2f4WVWW2mRyVl514P2BNFAm5AK3a5S7FDr5Pp5xpYxm8_pH10Czjnk_nhex3Ct-eWEdntK-IoH-ve1ui2cdDQE22jjRB8ealq3iiUG0dWqhBV0APgWlMAvmud88rfwMNubvxb9DvpYLA6F37aYtcoP9iW_rDp1a57FSVPE_umjbLzgk7LF2XpMqlkj9kDQMQJaE23mTcMuifnViOm65Z6b2ABrRg36pG7lfw0Uf-9WX3dMiwwvtrRwZGvLb1Y8YxWBZfOow0VT6cnkXxkv8LG1CBP6uo4zMCWOxNaaCCDSQD36iadI603GIceE0edHMp1wQGFnvz-APDSs7O78Re1C6lhLbMWD1MP2OIfvSdO_tViJ2CJgzW_NS_ztG9pmNkqQJMWp3xrh4aCCqMeqbrbElBRYemFKqWdzfwFNiW0pvDe5Onp4KYcQ6k3qYnEFnkPnea31i2kYeLsFitE5jzK40NAStF-PnmOz3ukhEYvd5zvj8BsIqhB1jyVGkL03XDC1EZr7UXERHjW7fdZuDw-sBXHdwis98yPRsm_6-ne40uoqvXXyYlNU9wGMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس مجلس:  گاهی انتقاد برخی فعالان رسانه‌‌ای در مورد فرماندهان نظامی را می‌شنوم و برای مظلومیت آن‌ها افسوس می‌خورم  قالیباف:
🔹
در زمان سکوت میدان، کارخانه‌ها، نیروها و بخش‌های مختلف نظامی در حال استراحت نیستند و همه خود را آماده می‌کنند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/686200" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc58e88f3.mp4?token=k6nKYRKPw23TQ1CMhlP0heFyAaf1RBpzKYj21ZsKMCIXNVbXQqEEQaZJu8HWkaCiFwwS5u_xPegIoHInljP-mjY8c473h6NVEyk524F2CaBkxecLqB_u_wOGNRan5rCHvoeOzmwyvhwOm7wm4Idn6BZJYw4sQtNYLf3cpMDY6hPZaxpxgLQ-cdMnxaQbQ7V6MJy4_sSZmbRXhrYM_JMBdk2NwzphmAKOm-Og1W9c7aR214u2G_wFl0LftE3KM2QZC2rjZmHs7T-6LvLmluFn1zr9bfgHK0iDDL4-XN1fU4UFv4m1fOuKdP-gWakXRRtPI1Axnk_5XSQHuaZ2eiJH-V1ua9tEUc5Q3u0ditPgCLBvJE1TLCHz9ncz0qrGOLpjCUeyPMNyWP8AxyIPEPmukYAja0rd2z7NqRcTKxQvmkvm5MWTz46yj8N8vXh_Hi39B85xKCidfLanMffr3JKgGmS2k14JDB2VO9JH4D5gWpHxze3rNlgvk8o4aG6GMJ5YPZ9vzaMLOcig1or1_G3CUFecQb3KzqyZXaDiRqdfTzh-NkGYH-AaIczN7iuT_0438t0k66m8H15q7tFQSLe-dHhE4Dy0Lq6sBfxe9KcvFztJnCTfqS9uHqksldDc3pD85CP7whoXK6JEl-gspl3jyxdV0JaFbL0mubZK0B0PDco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc58e88f3.mp4?token=k6nKYRKPw23TQ1CMhlP0heFyAaf1RBpzKYj21ZsKMCIXNVbXQqEEQaZJu8HWkaCiFwwS5u_xPegIoHInljP-mjY8c473h6NVEyk524F2CaBkxecLqB_u_wOGNRan5rCHvoeOzmwyvhwOm7wm4Idn6BZJYw4sQtNYLf3cpMDY6hPZaxpxgLQ-cdMnxaQbQ7V6MJy4_sSZmbRXhrYM_JMBdk2NwzphmAKOm-Og1W9c7aR214u2G_wFl0LftE3KM2QZC2rjZmHs7T-6LvLmluFn1zr9bfgHK0iDDL4-XN1fU4UFv4m1fOuKdP-gWakXRRtPI1Axnk_5XSQHuaZ2eiJH-V1ua9tEUc5Q3u0ditPgCLBvJE1TLCHz9ncz0qrGOLpjCUeyPMNyWP8AxyIPEPmukYAja0rd2z7NqRcTKxQvmkvm5MWTz46yj8N8vXh_Hi39B85xKCidfLanMffr3JKgGmS2k14JDB2VO9JH4D5gWpHxze3rNlgvk8o4aG6GMJ5YPZ9vzaMLOcig1or1_G3CUFecQb3KzqyZXaDiRqdfTzh-NkGYH-AaIczN7iuT_0438t0k66m8H15q7tFQSLe-dHhE4Dy0Lq6sBfxe9KcvFztJnCTfqS9uHqksldDc3pD85CP7whoXK6JEl-gspl3jyxdV0JaFbL0mubZK0B0PDco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای خبرفوری را از اینجا می‌شنوید...!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/686199" target="_blank">📅 17:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686197">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoYIuM5iWrUUSKuoj4qUjzU1cFMTLsv42G_ZesJu49nDNRD6QDl_gGElZHUl10LQ-xjIykjrBO3rm-ge53QhLoxp0-jY_hKfcs64rbFPCqvZBP9ybB4ZYXzoNkQqU2tmibFdU4Ou61nMgJU4KyFzTzThQkxEtfy177e08USer8hNVV_1W3LHiHK2trXqAOoZBAzCbsh4S6oqWaaxmCLCaMu1cNY9p9wfeaU1Ifg-DPGZjVRFCEgGgVXECCesgOCWfrIs4G8s9aiVHdjo981QxT67QMMZZPxSppDwv9yFlNs1gzRV-UXK2R0nHNMV6cAAlYaVOfA6R89kqT3q4yS7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی و اقتصاد دانش بنیان رئیس جمهور : «مدرسه نسل چهارم» در راه است
دکتر حسین افشین، با اشاره به تغییر شایستگی‌های موردنیاز در عصر فناوری و هوش مصنوعی، تأکید کرد که مدرسه دیگر نمی‌تواند با الگوی سنتی «انتقال پاسخ‌های آماده» ادامه دهد.
🔸
در مدرسه نسل چهارم، دانش‌آموز قرار نیست فقط شنونده باشد؛ باید
بپرسد، انتخاب کند، بسازد، آزمایش کند و از خطا و شکست برای اصلاح ایده خود استفاده کند.
🔹
افشین با تأکید بر نقش تعیین‌کننده معلمان در تحول آموزش گفت، فناوری آموزشی زمانی ارزشمند است که کیفیت تجربه یادگیری را افزایش دهد، نه اینکه صرفاً تعداد ابزارهای موجود در کلاس را بیشتر کند و در عصر هوش مصنوعی دیگر سؤال اصلی این نیست که دانش‌آموز «چقدر می‌داند»؛ بلکه این است که
با آنچه می‌داند، چه چیزی می‌تواند خلق کند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/686197" target="_blank">📅 17:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686195">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bf1b4e02.mp4?token=Tcwuij6UpUAIXfKSvM332qKBbdOaHES5eOvuiwONBhI5F0XTTCMaRn1ke9RUaSawETzCuIeb2_SIOfcrJxZICBGD_fnQnAxxNQeZvSBQy--DJ2dEEKifP-OAfbh2W-RqDbaXITf1oYpHdinZj15BwylEZ6OZzRf6DkS4ZCzMHJdj4JDhhizLpPKd9qphkwabEdB78VavudR6tjD5DdvHdqg864qJ5a2aZBbq6dDyLGmVyUxwgCqflE79I4hJvp3JrRnJTtb1T7JGoklXN8BUGUgwmjPkIAVrzkRYGfZjYduq-t0gW_nxq_OzPtfRn6RULk4bk9daAlNxuzQ7t6BR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bf1b4e02.mp4?token=Tcwuij6UpUAIXfKSvM332qKBbdOaHES5eOvuiwONBhI5F0XTTCMaRn1ke9RUaSawETzCuIeb2_SIOfcrJxZICBGD_fnQnAxxNQeZvSBQy--DJ2dEEKifP-OAfbh2W-RqDbaXITf1oYpHdinZj15BwylEZ6OZzRf6DkS4ZCzMHJdj4JDhhizLpPKd9qphkwabEdB78VavudR6tjD5DdvHdqg864qJ5a2aZBbq6dDyLGmVyUxwgCqflE79I4hJvp3JrRnJTtb1T7JGoklXN8BUGUgwmjPkIAVrzkRYGfZjYduq-t0gW_nxq_OzPtfRn6RULk4bk9daAlNxuzQ7t6BR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس مجلس:  گاهی انتقاد برخی فعالان رسانه‌‌ای در مورد فرماندهان نظامی را می‌شنوم و برای مظلومیت آن‌ها افسوس می‌خورم
قالیباف:
🔹
در زمان سکوت میدان، کارخانه‌ها، نیروها و بخش‌های مختلف نظامی در حال استراحت نیستند و همه خود را آماده می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/686195" target="_blank">📅 16:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686193">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdf4196086.mp4?token=YOgbChLRWLAHTy9o7QVBpXwXjy7Ko0gxZSJ1gN7htFTcIAyndLUjvgeDuBlYbVkrHFmHn38BV-Z5lE6Jtyj9IuNxFyubx2iyVWm5lfOqspJnGZOO1pW3QrcJC-FOToktTFnMGrEecvkcsVhhV9b5WOYqrzS1mXrDqM_AbJIL3QI5XYceGJ1A3KiJb2lCmjwuGsXZBtSTX6532kcD-Q19-RtTfI6mpabTafCEGS2khiySz-Z_4gC3tNlHdD6gPI4ubqqolI9Mrg-VcLqMfeZhKkHtTXVSLDvTNcSvkCAMuRgMdj33dVT5cHkm21sMx9_6ceyUal7kvdlVoWoZOls7uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdf4196086.mp4?token=YOgbChLRWLAHTy9o7QVBpXwXjy7Ko0gxZSJ1gN7htFTcIAyndLUjvgeDuBlYbVkrHFmHn38BV-Z5lE6Jtyj9IuNxFyubx2iyVWm5lfOqspJnGZOO1pW3QrcJC-FOToktTFnMGrEecvkcsVhhV9b5WOYqrzS1mXrDqM_AbJIL3QI5XYceGJ1A3KiJb2lCmjwuGsXZBtSTX6532kcD-Q19-RtTfI6mpabTafCEGS2khiySz-Z_4gC3tNlHdD6gPI4ubqqolI9Mrg-VcLqMfeZhKkHtTXVSLDvTNcSvkCAMuRgMdj33dVT5cHkm21sMx9_6ceyUal7kvdlVoWoZOls7uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: در ۱۵ ماه گذشته، به اندازۀ یک دهه پیشرفت در حوزۀ نظامی داشتیم
🔹
در هر دورۀ جنگ، بهتر از دوره‌های قبل عمل کردیم و جنگیدیم. فرآیندهای بازسازی و تقویت توان نیروهای مسلح در بخش‌های آفندی و پدافندی، به بهترین درحال انجام است‌؛ این اقدامات به دلیل بومی بودن فناوری ماست و جوانان ما این کار را انجام می‌دهند و دست نیازی به سمت دشمن نداریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/686193" target="_blank">📅 16:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686186">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6bFvP-XscM6B534J2-8SLIfGIvcAtltjSILVwsie68ACwbPK28Z8KzIoEVuLU-kQyu5e1qcUYKiKfQ8ZrmXu4Ew74KXkej1EBwqZ_Cmy4x75ZWDqUZxV9k72qokwvWXTRbN2-SzCmjig_qamdgbVFRVFZWoInSSQJpz_1MVoeTmf14wie90X4v1h8PinVUqyoQ84tZAhi7cKIj7DGKkvhibFU9hlG9idTB9yejb4cn-mH2WoeAm7IBCHjG4RaQl-iVzlLkv8iBo6RGcJZX6PgUeQialkj504Bnx3DfLREsFzqSMw_j4HjRLOh3xmbaVwVCmi2CZONIAlB7JLI4g1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7BXLFVr5i6_Drt9WQ0YTbgVykwdVW5QszXOT1W2HbJJNcd1PAE8zFfeLTPCJUUcObPZ51thA6cRw_hKp57_-4Oa-P9Q3xhJs9pwVVcRAnmUyqe79fhhV_6yFVkjMqPI53oWkWxVjuf0rLMeLYAdhc1t_RGqQMFdpVucuGH2WeOpRUuAWe0A3i-9-Auesr2T1C_cezSI0Ch2UUlhzj4rkXG6x1djaPK5M5-TscUhMTV0UzIYirOaz2Y96JM1sbD5qdhVMqRkVHdtlEwEcMIO3bSYoS-StuSeDZRbl0X00bX-jsNij6fLRrsgFx35HNizSknlxq16CZ7J9mplUFvlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGJO-B-HYHIck98YAzzQO-xFHjUzke4k5RFhK_UT7aLPHkcM_zHwBuV0uZ_K3Wiy_r1kU_rarxUX5V9H8KAM9oL8M47eqsyLkDob3g4yjzyFGWqcc950sUfnOdwzmVUjHUhgQYljuS8hbYQczEA_UhAZI3WqKz0QOSpuWTIAD2wR03pF7PuFdb2VCRli7TZ8SXaJAZhmsyfuRgqkDuMAE6haXeja47k-Xg1nOQdUn-qteJkoAhoDX4f0zKLCef5_1MZuzNgrfzTS0UQekA3ZEQMPcKrExqO_H0tT4wythyFtp5Ujf2LDjbHMDFYJB5jPhl5vwToejdHs9R6aHjnfVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fboJhr1C2oWjzuUoEU2Ye3YgAOn5cg5WBG7xyJXpjghR6rExfvo0JKjjI89eRnkXP0Cw-uH_gN6oQl896zqVxODBbQXzx-jG1T5pJEpM_6-q7FRIU2MXoDc2xMydGyI_ARaSRaDN9i9JG-go-OuRwvPht-3uSmyfAZ57e8yCA2l_8lo7PWE_310k0PI7CyuLy_RP93HByNYVDDE7EzOjaIU3COtMFZn_XslwyW3xsWu8Tmh3d9NI1ob_7QCqgj_viOiwt5MDRT8AoG_spoIeHN9LU4-feWIVlFa3TK0Jbhh2ASVQpji0JsX5iZ_8aozzfuw0lhOB6I6zknkF6od--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHgjMtW3hWC8Y4ee9nsThZTZhLHWXzot8ncdNvkNIN81jlPnoAnCNLPf3-cZkcKKC9zTCN0DNJeDFHRx0tG-scBGOoP6WGDC_wekeesJqY0o_aqqSpJgJXi7W9e9Icz_G6OGF2B69Is26oMBvBOLMF2WQAm5oVoJGfe7zxjK3RMTlYyYri-l9CYMJGbKmxpmFzUeMoTek6VkrTPBtw3T3WGnwoXkiiAnPuLAoCsBO3HIj90BZZeFGQmtHwh8qZjkgKI0yvjQ5gxBXzx99heUc4WspS9oztD8TCkYML2mcUMpVVPxROz8c6V-WD8z4VLX9fRVTgo0A2S5lsyuHY9vCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcHKxo8S6eSvAjj0pk_HuX_XaUSmW53i3qaafYMxyE-_G21pUezVTsGYMAH5b_g5zqX5UNxa7b2W_qZ1qslpiwxNw9taAUC3edtS8BKpJg28RaqVol-j5D8PnNJFFV_2La0mqbm3Q93UfWW0foxUqREmiqfNYK0jQreILllQxxv6y0KGnrU2Oz7D_Dm0qoSYg15uGabTnptSdqNqUeS8N1TPeXqdCmRiDA8gorZBmI02n0ik0FT6dmma_-OT_YicMASISEWcfw9FMrRyqR6IaKzUUlvYyNFbwkcHeQhSLYooLw5J7Iirkbz5jO8fZyyF0p3lQh_u6aMyh8n79pt2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7nxE-zEY-erbTai9CI_yjEj_GotG-PQ4rYOs-rXq2xOzO8KqBSUlAXkD8jKpGQqTNExfKltLfUBonZqyOjlOMA3JQ9HqnYu7FS2T-2KF4BJWneTwQoCffvXfuqNUxrsO5clyO4BSMxQHdW_psxt62qxeOGmpzge4maIf2qfIBMc2LRzJzxppa_cKsdomJabaSndtHhM7wu8hg3uvvGpK3b3q0ncEQDi6kxEvGhVz9K1tPsk79rpK9JjuLfouPdd9gREZYa5hGahlpWYf57qiBPZsA-pQVD0kMaE7Z83TIOlHkZWmWzSka1gX86M8sYHI3mpmWa1qaLi8RJCCjOYkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۶ ویژگی منحصربه‌فرد ایران که دنیا را انگشت به دهان کرده است!
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/686186" target="_blank">📅 16:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686185">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGPaHw5TMbESK1B4mi9CCGtEXIsNP_TDdDfRaXNsiyP1boYs4oJx0wsrRQ4PgPqT8bP1AQQe0n4Zwr2hdUqiyKp7lE0I5AlIdxMPHPc425M51xQ4phcREl7o0Rukk-cET9HFN_W1p3Ed9i6qiN62BELGI35wCfM4Lp6wYqQhd7B2i2aoqFox6Xt3IwDtDH2AhvYfTjV9cMhZkAYWAkwVXGVN8B1M4cNqLaAi1S73iv-G_QFMIj1UAsv4iKYsqS6dKsv7X-2O3atJ2467COYHa59lLJk70yJqGH-4HsW5N_XXt8kRtic2BntsZsbNKw-EgLLnq0l0Jm0cS-JSOiMWoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۹۵ تا ۵۰۰ میلیونی قیمت‌ خودرو طی دو هفته
🔹
بررسی قیمت خودروهای داخلی در بازار طی دو هفته اخیر نشان می‌دهد تمامی خودروهای مورد بررسی با افزایش قیمت قابل توجهی مواجه شده‌اند؛ به‌طوری که میزان این افزایش از ۹۵ تا ۵۱۵ میلیون تومان متغیر بوده و رشد قیمت برخی خودروها در این مدت به حدود ۲۰ درصد رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/686185" target="_blank">📅 16:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686184">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5973e52fa.mp4?token=C591SFaKsGnj39nF3ZLvRuc6qGwlVLF8mnuSYVUOCzDaze0RmXG9WaCUZ5osWmQ829pFHUSAjqaS_E4anaTaZdtuVemNQOG5SRRd-7FugHJ0HNE6sMSQEHpPStpEm24BQZ6pCSpJUBBkFmLR6OqMdNgvwl68pxgiXeD-TJvc7VXpGR3HRIDg5ns4JAY3UTg-79Rfn05F78DzrZgcYVNBKbcEukFTIwTFKpua35Ynd4kH1jbVD_ncbUGikCfGGK8GaDeHieJd-YvtFzMKREt2XXnyIL1EqQKVpTjcGleFWOphkmqPkbkKhJh_ea6wRg9o1y3X2xCFPWGw-HIU3UbA6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5973e52fa.mp4?token=C591SFaKsGnj39nF3ZLvRuc6qGwlVLF8mnuSYVUOCzDaze0RmXG9WaCUZ5osWmQ829pFHUSAjqaS_E4anaTaZdtuVemNQOG5SRRd-7FugHJ0HNE6sMSQEHpPStpEm24BQZ6pCSpJUBBkFmLR6OqMdNgvwl68pxgiXeD-TJvc7VXpGR3HRIDg5ns4JAY3UTg-79Rfn05F78DzrZgcYVNBKbcEukFTIwTFKpua35Ynd4kH1jbVD_ncbUGikCfGGK8GaDeHieJd-YvtFzMKREt2XXnyIL1EqQKVpTjcGleFWOphkmqPkbkKhJh_ea6wRg9o1y3X2xCFPWGw-HIU3UbA6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: آنچه من امضاء کردم یک تکه کاغذ بود و من نیازی به آن تکه کاغذ ندارم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/686184" target="_blank">📅 16:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686183">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
قبض یک میلیاردی گاز برای برخی از تهرانی‌ها
مدیرعامل شرکت ملی گاز ایران:
🔹
در برخی نقاط تهران قبض یک میلیارد تومانی صادر شده است.
🔹
زراعتکار، معاون وزیر نفت، پیشتر اعلام کرده بود که از این پس یارانهٔ پنهان مربوط به استخرهای آب گرم ویلاها در زمستان پرداخت نخواهد شد و این مشترکان مشمول اصلاح تعرفه‌های گاز خواهند شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/686183" target="_blank">📅 16:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686182">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30ffe30ff.mp4?token=PKTJeOsfwL-LyI0J3J2acDM3hjRyHe6KM99ysBtGwT8ixF2ZodjQ4ZGoPmKdi4IZaPdrYpIx3IAijLsUMHf8FYOZ7SfYU9h2f7jZsmDs3lcbO6BdRwthXvOntK7rcyswImuGNIwAECqPMxaGiak7Xf4ILrbCH8JLhDxURwT8DI9PG0QFlHv4WK1YF45OAcmycknIaHMXOTvacoQW_3KjZqVW2QzWPP-CUxeCOS6A44p9Fc8C2EK5W8UAmvrrAwjXAqC1ZRP0hCifcA2LkS0BH8dTpIo7UGZA6jFguGxvG29RY_Uh1OjLkJgT_byjPJKW73_WTqpMR7DdRVNPaiyYGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30ffe30ff.mp4?token=PKTJeOsfwL-LyI0J3J2acDM3hjRyHe6KM99ysBtGwT8ixF2ZodjQ4ZGoPmKdi4IZaPdrYpIx3IAijLsUMHf8FYOZ7SfYU9h2f7jZsmDs3lcbO6BdRwthXvOntK7rcyswImuGNIwAECqPMxaGiak7Xf4ILrbCH8JLhDxURwT8DI9PG0QFlHv4WK1YF45OAcmycknIaHMXOTvacoQW_3KjZqVW2QzWPP-CUxeCOS6A44p9Fc8C2EK5W8UAmvrrAwjXAqC1ZRP0hCifcA2LkS0BH8dTpIo7UGZA6jFguGxvG29RY_Uh1OjLkJgT_byjPJKW73_WTqpMR7DdRVNPaiyYGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار پژمان جمشیدی با خواهرش در فرودگاه کانادا
🔹
ویدیویی از دیدار پژمان جمشیدی با خواهرش، مامک، در فرودگاه کانادا منتشر شده است. مامک جمشیدی پیش‌تر گفته بود برادرش برای دیدار با خانواده به کانادا سفر کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/686182" target="_blank">📅 16:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686181">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33b37d4d9.mp4?token=VRav-wxwHdm7BZh_pm3VMhzsDF5c-uArQeKtLv3PirSNH9JOUaR_-XZGGww50yhrkEspBkaj7pzjeC4B9NBPIqSBtBB8t3iAsHuBtiH3PFnEFL9acXMBEgJ9yNkfgFs7XiDjITXeH2Xz9Mt37AWAO4diTVu3YTLMfSkqkrJ8J1dSVsB-Jj1khDqN4kkNmg8NeAC_YFgQ7IenKu66dsUAxNigFyFutrXGeA1_eeRMwVV58-bIaYtRtHz9oGMfraapfPFAK1epYJYUqbVdvO44M2OrdWLWrFt6xoKvMPJt7ChA8C7CEkKOmwc7fa84zKskWDJx6rOXHvuwINhAqYEfYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33b37d4d9.mp4?token=VRav-wxwHdm7BZh_pm3VMhzsDF5c-uArQeKtLv3PirSNH9JOUaR_-XZGGww50yhrkEspBkaj7pzjeC4B9NBPIqSBtBB8t3iAsHuBtiH3PFnEFL9acXMBEgJ9yNkfgFs7XiDjITXeH2Xz9Mt37AWAO4diTVu3YTLMfSkqkrJ8J1dSVsB-Jj1khDqN4kkNmg8NeAC_YFgQ7IenKu66dsUAxNigFyFutrXGeA1_eeRMwVV58-bIaYtRtHz9oGMfraapfPFAK1epYJYUqbVdvO44M2OrdWLWrFt6xoKvMPJt7ChA8C7CEkKOmwc7fa84zKskWDJx6rOXHvuwINhAqYEfYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مبدا حملات علیه لارک، یکی از کشورهای منطقه بود  بقائی با بیان اینکه مبدا حملات علیه لارک، یکی از کشورهای منطقه بود:
🔹
و همان طور که در اخبار آمده، ما مبدا این حملات را مورد هدف قرار دادیم./ جماران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/686181" target="_blank">📅 16:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686180">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxxZNmhLRNKtH5YiA56JygWoSIx8zIx0L81X7glm0Rmxss0EIth10LKpmLf_3CwELCdjHW6sWl_-0oAvOJLPg52FbFoBIdrgi0ERMvbzzTcGGuIRA-vCFIuMkLq-Tba_pBf9bSyiwsAwApxcShslv1Ba62dOZeJfZhAbL1BSvU7W1Fcqhya28g1xqvUB6rENfz7H1EW-gJRl28UifmIY7lSkkT7CiOAjMOhJgq8yyNbibpHIfBofOO_GJFqJWbe-GzuZOR3PhYohtDOdqeGwkHd0yJ_LqiOwT80pf-3VlWtYUSvMSIZP3bBEbIQK7Fx55LI0HRauobbf2joz6iDQZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای کامل روش‌های انتقال وجه در بانک‌ها رو از اینجا ببینید
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/686180" target="_blank">📅 16:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686179">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebdaf6725c.mp4?token=iOSmfbNZmYWJQpUAlbfbFt_pkwHh7HO4-SNVwlB5vje_ZbURK-OvBceIW1KiH-rs76t-J_QwE40SAmbTtWIk5Ch_vUUPhdm8SoRtgnZEjKtHm902gi5Dj3cKDiVduJ09hdhWHbwXIFcfU1GJRJH8hXsi5spOA5Z6k3POSymNriHIB1cVlBZJnGFdcXbZcO4yqLdroiv3Ztypj6OPPRJi1uoQurNOLXKlbpsOtZNkuQUHJEH8f-nr4Cbh6HcQz22QdOZL9qVM0E9qj59aRKnBpMFIbWmZ2UqYT-DqQD7vC-115KZBk0Z7YOGf6J8qDZZi1tweOwwovju2ysGUlAXKOYLqTO3lA8RQDuyxH0R8W9ecxOSZx-iJKuJloBa9jSJStY1bNffkF_-0kKF-s4PL_L0CbLfJYmzyEUfb8jOdmuZel0-0j2XnZXgKvrMqVmX6V7xwjIFfBKIg6WJl78cJakafNDZqfNeiCrZjrcWfcxgURhDptdmGfBj_d6o8Xq4EEt9meSKvviyYX6bbGLuz3OrY4nehwGm2TYQIFwtJ6WK89wxP1pBrGmkE4KW6aiwy2ClP49jIeiQDX7K0yblJ-Kaw12SFDjYcknWEGifH-gxGDZSgFV55iXoBUxUIj_Ov8swGK9mfuhQm20oNKBjBBtbU1JfR9ONBzP9JrcM3-f4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebdaf6725c.mp4?token=iOSmfbNZmYWJQpUAlbfbFt_pkwHh7HO4-SNVwlB5vje_ZbURK-OvBceIW1KiH-rs76t-J_QwE40SAmbTtWIk5Ch_vUUPhdm8SoRtgnZEjKtHm902gi5Dj3cKDiVduJ09hdhWHbwXIFcfU1GJRJH8hXsi5spOA5Z6k3POSymNriHIB1cVlBZJnGFdcXbZcO4yqLdroiv3Ztypj6OPPRJi1uoQurNOLXKlbpsOtZNkuQUHJEH8f-nr4Cbh6HcQz22QdOZL9qVM0E9qj59aRKnBpMFIbWmZ2UqYT-DqQD7vC-115KZBk0Z7YOGf6J8qDZZi1tweOwwovju2ysGUlAXKOYLqTO3lA8RQDuyxH0R8W9ecxOSZx-iJKuJloBa9jSJStY1bNffkF_-0kKF-s4PL_L0CbLfJYmzyEUfb8jOdmuZel0-0j2XnZXgKvrMqVmX6V7xwjIFfBKIg6WJl78cJakafNDZqfNeiCrZjrcWfcxgURhDptdmGfBj_d6o8Xq4EEt9meSKvviyYX6bbGLuz3OrY4nehwGm2TYQIFwtJ6WK89wxP1pBrGmkE4KW6aiwy2ClP49jIeiQDX7K0yblJ-Kaw12SFDjYcknWEGifH-gxGDZSgFV55iXoBUxUIj_Ov8swGK9mfuhQm20oNKBjBBtbU1JfR9ONBzP9JrcM3-f4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه: انسداد تنگه هرمز برنامه‌ریزی شهید پاکپور بود
🔹
شهید پاکپور پیش‌بینی کرده بود که جنگ با ترور او شروع می‌شود؛ شهید پاکپور برنامه‌ریزی کرده بود که اگر جنگ آغاز شد و او دستوری صادر نکرد، فرماندهان ۲۰ دقیقه بعد شلیک کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/686179" target="_blank">📅 16:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686178">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e949697f83.mp4?token=GmgN4oYz2mUueQdSH2sLmmyXvWd1pD9fzb8qZ4jfTfIpAEFek8zWN3uatWFTkQt_OAUj8AU9gzCxqwNuATg_tZtxmCi84bBNaWwA3Df9LURLfJayaCYx2j_IZfSHOdh-fXRzFi73KYtHmJl9CeqJ2LgLAyIh7wKq08JkgY2ZBANt0zvEct_VOp_G4B082-FCKC9CCTp34C9jiC7dWk32JQt-SFJuRmJum-bHqRw9htx3FQ20wAMtxarlQX-wYHPP0h0q8P3DwN-kWeQ75ule6Y9vVerNUx04DQa0qHtBJpqYWgk2sVrhMU-c8YKGRKkvNJxQZM0jrrbsP0VRjCYHGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e949697f83.mp4?token=GmgN4oYz2mUueQdSH2sLmmyXvWd1pD9fzb8qZ4jfTfIpAEFek8zWN3uatWFTkQt_OAUj8AU9gzCxqwNuATg_tZtxmCi84bBNaWwA3Df9LURLfJayaCYx2j_IZfSHOdh-fXRzFi73KYtHmJl9CeqJ2LgLAyIh7wKq08JkgY2ZBANt0zvEct_VOp_G4B082-FCKC9CCTp34C9jiC7dWk32JQt-SFJuRmJum-bHqRw9htx3FQ20wAMtxarlQX-wYHPP0h0q8P3DwN-kWeQ75ule6Y9vVerNUx04DQa0qHtBJpqYWgk2sVrhMU-c8YKGRKkvNJxQZM0jrrbsP0VRjCYHGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان صورتی‌رنگ چین پیش از طوفان!
🔹
آسمان چانگژو در استان جیانگسو، دقایقی پیش از وقوع طوفان و بارش شدید، به رنگ صورتی-قرمز درآمد و توجه مردم را جلب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/686178" target="_blank">📅 16:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686177">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/957d1e1e83.mp4?token=TDGnfX6jNXzjRekF6aHzL0wN-pR1k2Unuza1DgRN9LYnSgwp5T9MqBbysVKkx7Xz6A4dCUcFkVAKT2XWDYPo2-Joevj_MVoDeOPs-r7HJYnK38WJlU1RMbJpvAwph5bH1uNc4-aCGApTZ7pAtsrNouNQFrnYfsQZtnx5ULoWYfEcAcFn7XpaEbDuk3GJW9kF5NZ0Jrwq29kFEYhQyQinXcvIMKpVbtbMa-WLbjKXGG058G3kfBjaNOkuKjeRXaRcR9VvfU1Zb51XUtue0BpcGZZnvXDVquPpEnC4soHOvzBuhB_x_0f0l2FzE_EDcbGKeq_k1LT2O9i41kJCO_xktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/957d1e1e83.mp4?token=TDGnfX6jNXzjRekF6aHzL0wN-pR1k2Unuza1DgRN9LYnSgwp5T9MqBbysVKkx7Xz6A4dCUcFkVAKT2XWDYPo2-Joevj_MVoDeOPs-r7HJYnK38WJlU1RMbJpvAwph5bH1uNc4-aCGApTZ7pAtsrNouNQFrnYfsQZtnx5ULoWYfEcAcFn7XpaEbDuk3GJW9kF5NZ0Jrwq29kFEYhQyQinXcvIMKpVbtbMa-WLbjKXGG058G3kfBjaNOkuKjeRXaRcR9VvfU1Zb51XUtue0BpcGZZnvXDVquPpEnC4soHOvzBuhB_x_0f0l2FzE_EDcbGKeq_k1LT2O9i41kJCO_xktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین در دیدار با پزشکیان: سلام من را به آیت الله سید مجتبی خامنه ای رهبر معظم انقلاب برسانید  رئیس‌جمهور روسیه:
🔹
روابط روسیه و ایران در همه زمینه‌ها به طور پیوسته در حال توسعه است.
🔹
روسیه از امضای تفاهم‌نامه میان ایران و آمریکا استقبال کرد، اما متأسفانه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/686177" target="_blank">📅 16:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686176">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مبدا حملات علیه لارک، یکی از کشورهای منطقه بود
بقائی با بیان اینکه مبدا حملات علیه لارک، یکی از کشورهای منطقه بود:
🔹
و همان طور که در اخبار آمده، ما مبدا این حملات را مورد هدف قرار دادیم./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/686176" target="_blank">📅 15:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686175">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
پوتین در دیدار با پزشکیان: سلام من را به آیت الله سید مجتبی خامنه ای رهبر معظم انقلاب برسانید
رئیس‌جمهور روسیه:
🔹
روابط روسیه و ایران در همه زمینه‌ها به طور پیوسته در حال توسعه است.
🔹
روسیه از امضای تفاهم‌نامه میان ایران و آمریکا استقبال کرد، اما متأسفانه آتش‌بس شکننده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/686175" target="_blank">📅 15:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686171">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رویترز به نقل از پوتین در گفت‌وگو با پزشکیان: مردم روسیه در مبارزه مردم ایران برای دفاع از منافع خود، با آنان همبستگی دارند
🔹
روسیه و ایران با وجود شرایط نظامی و سیاسی کنونی، روابط اقتصادی و تجاری خود را حفظ کرده‌اند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/686171" target="_blank">📅 15:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686167">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تصاویری از دیدار و مذاکرات دوجانبه پزشکیان و پوتین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/686167" target="_blank">📅 15:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686166">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579eeda711.mp4?token=UQi6m5J4bmnWpyeq_Ug-seQ67oWSnJtoV_xzKn3EcUdED1uG_i6K49NLLPObBOyvd9Er-MA6GjaJqrK0_9TqmnnKOTnX02rRFppJ1u6WD7l97x2jYuqZ-6hAGEP7yn387Cprg6YQrlX1AVCrU-mVAXTL7xxdtjaoKHLdeolvpAzGEDHY1Hd676Xu7tsnmE7imqgK-rtePdeuKkc7hfbjseNrF1L6ldlBbmoCHSi18HEtQ-puRHNqvaX5ekIHf5XuSVgCIzIILqoD12EfNE_a-Nedi3UwD6dDHPfCqkvvww5aMkZTPXpZqd94UIkqHPlkGWm-etNf6y0lZ2FuuvlDmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579eeda711.mp4?token=UQi6m5J4bmnWpyeq_Ug-seQ67oWSnJtoV_xzKn3EcUdED1uG_i6K49NLLPObBOyvd9Er-MA6GjaJqrK0_9TqmnnKOTnX02rRFppJ1u6WD7l97x2jYuqZ-6hAGEP7yn387Cprg6YQrlX1AVCrU-mVAXTL7xxdtjaoKHLdeolvpAzGEDHY1Hd676Xu7tsnmE7imqgK-rtePdeuKkc7hfbjseNrF1L6ldlBbmoCHSi18HEtQ-puRHNqvaX5ekIHf5XuSVgCIzIILqoD12EfNE_a-Nedi3UwD6dDHPfCqkvvww5aMkZTPXpZqd94UIkqHPlkGWm-etNf6y0lZ2FuuvlDmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاید فکر کنی فقط جمجمه از مغزت محافظت می‌کنه، اما قبل از اینکه به خود مغز برسیم، ۱۳ لایه بین مغز و دنیای بیرون قرار گرفته #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/686166" target="_blank">📅 15:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686165">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ایران نوین؛ نخستین آژانس AI-Native در صنعت تبلیغات ایران
🔹
کانون ایران نوین در نمایشگاه الکامپ از رویکرد جدید خود در استفاده از هوش مصنوعی رونمایی کرد و خود را به‌عنوان نخستین آژانس AI-Native در صنعت تبلیغات ایران معرفی کرد.
🔹
این کانون با عبور از مدل سنتی کمپین‌های ۳۶۰ درجه، به سمت توسعه کمپین‌های مبتنی بر AI و پلتفرم‌های اختصاصی حرکت کرده است.
🔹
به گفته مدیران ایران نوین، استفاده از هوش مصنوعی باعث افزایش سرعت، کیفیت، تنوع و خلاقیت در اجرای پروژه‌ها و رضایت بیشتر مشتریان شده است.
🔹
ایران نوین همچنین با ایجاد «مغز برند» و استفاده از AI Agent ها، به دنبال شخصی‌سازی ارتباطات و خودکارسازی فرآیندهای تبلیغاتی و بازاریابی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/686165" target="_blank">📅 15:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686164">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b191e931cd.mp4?token=Y3UCEZz78PWTc9O7AO1KaI3419UkG72sa8v-voK9100ntMTc004SeEOD_VkaYl2xWkqGzSFp16tgy_BOuv9EjF5c73B21skhY3y3T0bUwuVoKFzLYgdjMT_tHPHt3xmcyBPnHN-YFPozA_gpoEFHANsuiIYVS_auaXLGvnPi-gHlclA4uhQWGBP2MFQ2mgSzOhdV1RoK7HFmywXHp4ewrcfYtIgU0EnE7heoJaOPA4nAlnl5r3qSgUubVZjp-UW9YUp36oa8Bc65LBP9Hk51wtih4Tv_ptLU0AIYZ6lBOJgBXOHbnGBg0th3bu1Eu4BJR_1wuCBqyV5k3ti1hMjGMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b191e931cd.mp4?token=Y3UCEZz78PWTc9O7AO1KaI3419UkG72sa8v-voK9100ntMTc004SeEOD_VkaYl2xWkqGzSFp16tgy_BOuv9EjF5c73B21skhY3y3T0bUwuVoKFzLYgdjMT_tHPHt3xmcyBPnHN-YFPozA_gpoEFHANsuiIYVS_auaXLGvnPi-gHlclA4uhQWGBP2MFQ2mgSzOhdV1RoK7HFmywXHp4ewrcfYtIgU0EnE7heoJaOPA4nAlnl5r3qSgUubVZjp-UW9YUp36oa8Bc65LBP9Hk51wtih4Tv_ptLU0AIYZ6lBOJgBXOHbnGBg0th3bu1Eu4BJR_1wuCBqyV5k3ti1hMjGMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی:فعالیت هسته‌ای در کوه کلنگ نداریم  سخنگوی وزارت امور خارجه:
🔹
ما در چارچوب متعارف با آژانس در تماس هستیم و نمایندگی ما در آژانس در وین لازم باشد با طرف‌های ذی‌ربط در آژانس گفتگو می‌کند. اینکه بگوییم مذاکره داریم، خیر نداریم.
🔹
صحبت‌ها درباره فعالیت…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/686164" target="_blank">📅 15:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686163">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085d382a76.mp4?token=IPrLDco29BTGXnBsPHoasgfO5PkMhK5HAFPKJqHzLYnDzT7WadbzuAEy9K_YUq6UZxiJn1PO_Vm7SRuctjBsAtrzN6DEHiTYni32qZlvP_EncTUUAp8gU9SoV5WUavNzXGyxzDckv_AdLIt4z7QECi6bEemK4LlkzAAtSqEy0fYBT5QBOJZIMOrMram6WuhwCku4ho3CWGJLGWz6KZiz5BVZEcIm7WeHEsgM99b-D38H7ECzEjUXr0FqIAgyNN4vLBcH4ki1Wd-_IaF6j1lDliUCCujFj_gA-HurvRqHhCd9qvW2QYJ2qDuQX0Y15TnIpkw84gqTH5ZYNG6v2xfZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085d382a76.mp4?token=IPrLDco29BTGXnBsPHoasgfO5PkMhK5HAFPKJqHzLYnDzT7WadbzuAEy9K_YUq6UZxiJn1PO_Vm7SRuctjBsAtrzN6DEHiTYni32qZlvP_EncTUUAp8gU9SoV5WUavNzXGyxzDckv_AdLIt4z7QECi6bEemK4LlkzAAtSqEy0fYBT5QBOJZIMOrMram6WuhwCku4ho3CWGJLGWz6KZiz5BVZEcIm7WeHEsgM99b-D38H7ECzEjUXr0FqIAgyNN4vLBcH4ki1Wd-_IaF6j1lDliUCCujFj_gA-HurvRqHhCd9qvW2QYJ2qDuQX0Y15TnIpkw84gqTH5ZYNG6v2xfZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از دیدار و مذاکرات دوجانبه پزشکیان و پوتین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/686163" target="_blank">📅 15:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686161">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c8bb4dd8.mp4?token=GE5k7rkwhr1LH2hjg7yNgM9M0ePVhcTaWcX0YRwTVhqePghJqaO58RI93EP2_IidjZqER5PJK9M_ErF5niI4b6Utk8eKDzDCAcG3LSObI8w2Q8pD4kTHSjrD2IjgecCXhPT_6A02WagOoEdDo-7oiaW5GXnFIYoTPUFFkef74wBYKIzsVPc_kRjFuE7Dcn1NHsDeUlhQAj5d-e1-SmVa3E2IAjsCH2QgBYzwT6sDvNvQp8UQP8czk6h9t8I2Rwhk_aLHDlq13cUPNBzpgMulf3MQlcHJizUpjmZgyQbiWqcq4FGAvZz9NQrOutJPHTCiDMBLaxKwnd41pymqsBWpUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c8bb4dd8.mp4?token=GE5k7rkwhr1LH2hjg7yNgM9M0ePVhcTaWcX0YRwTVhqePghJqaO58RI93EP2_IidjZqER5PJK9M_ErF5niI4b6Utk8eKDzDCAcG3LSObI8w2Q8pD4kTHSjrD2IjgecCXhPT_6A02WagOoEdDo-7oiaW5GXnFIYoTPUFFkef74wBYKIzsVPc_kRjFuE7Dcn1NHsDeUlhQAj5d-e1-SmVa3E2IAjsCH2QgBYzwT6sDvNvQp8UQP8czk6h9t8I2Rwhk_aLHDlq13cUPNBzpgMulf3MQlcHJizUpjmZgyQbiWqcq4FGAvZz9NQrOutJPHTCiDMBLaxKwnd41pymqsBWpUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: عاصم منیر نه پیام مثبتی داشت و نه منفی؛ بلکه برای کمک به کاهش تنش به ایران سفر کرد
🔹
آمریکا مفهوم مذاکرات را با دیکته‌کردن اشتباه گرفته. نیروهای مسلح ما هیچ تعرضی را بی‌پاسخ نخواهند گذاشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/686161" target="_blank">📅 15:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686160">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721065d0e9.mp4?token=oMAvuDgdX69EIriMipwVNGAgQm-U2isf8iyP1lLJnAN2xWni9fQRb3rTIJADLAfwl99PD3w8paBz0MdI0Lr9amUmc2mGJJRRdb_nyqKSkpvdf_HO_0_5ySi3Is7zqzRH9-3sLgxu8Zpoc4gT6Wy2r7OWo3apoc4TsDYd7k5h0O597fBdOJHOaBTFZYoH4Vsf1OuaqxVW8-oQie3oWJjjKX3jTVv99oABuJGKIAU9SzMcySukjCV2tOpmEtcWX3DUCDX1Jz3kXhpE8p92dFy8EROZlPYXIF3VyNDO8_TpFuR77flTpbDpFnZakcS_ctuBVU4o9m95efxzmTC2PYu7yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721065d0e9.mp4?token=oMAvuDgdX69EIriMipwVNGAgQm-U2isf8iyP1lLJnAN2xWni9fQRb3rTIJADLAfwl99PD3w8paBz0MdI0Lr9amUmc2mGJJRRdb_nyqKSkpvdf_HO_0_5ySi3Is7zqzRH9-3sLgxu8Zpoc4gT6Wy2r7OWo3apoc4TsDYd7k5h0O597fBdOJHOaBTFZYoH4Vsf1OuaqxVW8-oQie3oWJjjKX3jTVv99oABuJGKIAU9SzMcySukjCV2tOpmEtcWX3DUCDX1Jz3kXhpE8p92dFy8EROZlPYXIF3VyNDO8_TpFuR77flTpbDpFnZakcS_ctuBVU4o9m95efxzmTC2PYu7yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: عاصم منیر نه پیام مثبتی داشت و نه منفی؛ بلکه برای کمک به کاهش تنش به ایران سفر کرد
🔹
آمریکا مفهوم مذاکرات را با دیکته‌کردن اشتباه گرفته. نیروهای مسلح ما هیچ تعرضی را بی‌پاسخ نخواهند گذاشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/686160" target="_blank">📅 15:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686158">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: تک تک همه اقداماتی که آمریکا در جریان تجاوز نظامی علیه ایران مرتکب شد، مصداق جنایت جنگی است/ آنها می‌خواهند یکی‌دو مورد را برجسته کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/686158" target="_blank">📅 15:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686157">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8567e76bb2.mp4?token=vzvkmWkQAcNvYM1r3hDUeCtirH7L34dke38HHnOnjXPRhvGCM5M9R71G2xTIznQq1TF-SLpj5rD0JtQHARVKc4C8RzCHan0vsPsDATAF2donAe9Rvp3eOqj1ehrA1CKCypiYgJq6cXUhsEBJWS1Nmb-7Lb_KhmyklHZV6FTJtsolt2SDp5YgfCD245-yT0PGQXixmlTbTMSS0ySMiT1xk29PQMMJiXYwnP4BorNXxtEFhJO9xM8rcuccKMoMBxuwLMc6_LblaKNZb9ehX_bysAYd7BOsr3sfYMHq_Zy6Dh1EQzsCrzpbEfNB7vuGTeWOQDxiKFtsv14ALZgp0rjanA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8567e76bb2.mp4?token=vzvkmWkQAcNvYM1r3hDUeCtirH7L34dke38HHnOnjXPRhvGCM5M9R71G2xTIznQq1TF-SLpj5rD0JtQHARVKc4C8RzCHan0vsPsDATAF2donAe9Rvp3eOqj1ehrA1CKCypiYgJq6cXUhsEBJWS1Nmb-7Lb_KhmyklHZV6FTJtsolt2SDp5YgfCD245-yT0PGQXixmlTbTMSS0ySMiT1xk29PQMMJiXYwnP4BorNXxtEFhJO9xM8rcuccKMoMBxuwLMc6_LblaKNZb9ehX_bysAYd7BOsr3sfYMHq_Zy6Dh1EQzsCrzpbEfNB7vuGTeWOQDxiKFtsv14ALZgp0rjanA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: تک تک همه اقداماتی که آمریکا در جریان تجاوز نظامی علیه ایران مرتکب شد، مصداق جنایت جنگی است/ آنها می‌خواهند یکی‌دو مورد را برجسته کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/686157" target="_blank">📅 15:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686156">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbFfKLJ8PfawXf3fgTI5Qc1cp5d25xn-0r9CeSQCglHanNV31VQJNXtVS5dACLaezOMQ2d4V2Y-QuHy6PXRu0d5jmuDJsVSkBmngfAIVX0ZXIqlZDt_cnTH3vyVGgF0HEC_S9LfU7Nx65mBgyjlse7NgKEeFWK81LWq-CzDhwqHk5F4YIOKC9cdR3pGHAlrMXL-96YpVHtFh8h7tfFnoJTVFsn_uUztzIi4khTrnMXTVH8BHmZd-h3Te8T2Uw7ZlHFdevKYmy48n5HDZ4iBnyJ5-YHD5Rf6rrbn5Xbii1bgZvJ_NX-fZ1b4S2kN3p-PEb0nHRpnw9ahwXBlem4Xu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۳ درصد آمریکایی‌ها می‌گویند واشنگتن باید نفت ایران را تصاحب کند!
🔹
نظرسنجی yougov نشان می‌دهد که تنها حدود یک‌چهارم آمریکایی‌ها (۲۳ درصد) معتقدند اگر آمریکا ایران را شکست دهد، باید نفت ایران را تصاحب کند.
🔹
در مقابل، ۵۳ درصد می‌گویند آمریکا نباید چنین کاری انجام دهد.
🔹
در میان دموکرات‌ها تنها ۹ درصد، در میان مستقل‌ها ۱۹ درصد و در میان جمهوری‌خواهان ۴۲ درصد خواهان تصاحب نفت ایران در صورت پیروزی آمریکا در جنگ هستند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/686156" target="_blank">📅 15:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686155">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8482f20060.mp4?token=RYlJYb-ArZxzurBl8GjK1iDJ7MqeDJflI2PupBbrEAEIbz2CFGr3rFGi6StQx6aBvIiddD16CV7cPa_yNDkl7_P7z8zcxbMZN7u9J2cs1mCw6AARHuWzndpXm01BUnAr9-H21sIrku7w7O1DBdZWmFyqHVJ0iy41CiWmota8v3_p9p3ePMzfwHtZlDG826tVx_ovbKV8T8EUxCkPqkPsXn-uu_y2xCRDd_etlp5hmDpmhrM7jyUyB5-06FseOSfVlaHdu4yb9AsNhk1n5YBIyvRUjZkkr6m6FU7I31LNs6l0u986UkEstQISda6uwU9Y2nmj1GmRr9w9UUBgvmlQNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8482f20060.mp4?token=RYlJYb-ArZxzurBl8GjK1iDJ7MqeDJflI2PupBbrEAEIbz2CFGr3rFGi6StQx6aBvIiddD16CV7cPa_yNDkl7_P7z8zcxbMZN7u9J2cs1mCw6AARHuWzndpXm01BUnAr9-H21sIrku7w7O1DBdZWmFyqHVJ0iy41CiWmota8v3_p9p3ePMzfwHtZlDG826tVx_ovbKV8T8EUxCkPqkPsXn-uu_y2xCRDd_etlp5hmDpmhrM7jyUyB5-06FseOSfVlaHdu4yb9AsNhk1n5YBIyvRUjZkkr6m6FU7I31LNs6l0u986UkEstQISda6uwU9Y2nmj1GmRr9w9UUBgvmlQNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمول متفاوت «مای‌دات» برای شبکه‌های اجتماعی: پاداش به آشتی، نه جنجال!
🔹
پویان رازانی، مدیرعامل دات‌وان سیستم در حاشیه نمایشگاه الکامپ:
نقطه اشتراک مای‌دات با بقیه اپلیکیشن‌ها، دور هم جمع کردن مردم است؛ اما مزیت ما این است که به
تعامل و آشتی دادن
جایزه می‌دهیم، نه به دیده‌شدن به هر قیمتی!
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/686155" target="_blank">📅 15:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686152">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
آپارتمان‌های لوکس پایتخت متری چند؟
🔹
در شمال تهران، قیمت خانه از مرزهای تصور عبور کرده است. هر متر آپارتمان در گران‌ترین معاملات منطقه یک تا ۱.۵ میلیارد تومان قیمت خورده که معادل حدود ۷۵۰۰ دلار است.
🔹
در صاحبقرانیه، متوسط قیمت آپارتمان‌های نوساز در مردادماه حدود متری ۸۰۰ میلیون تومان بوده است. این قیمت‌ها مربوط به بخش بسیار کوچکی از بازار است؛ تنها حدود ۱ تا ۵ صدم درصد از کل معاملات در چنین سطوحی انجام می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/686152" target="_blank">📅 14:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686151">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c2539c0d4.mp4?token=M3bk1_bsIw5lmwA4SYEjg0A7JleGzbHVGxnSKfZe8s_DnVcWZqLFrH8iecscnul6bsQnPTF4CcH4bRIzPCxWM4ibw2QtwKY-6w0EUJBy1TCdOuq9T7cO-D03_fGdcLUWUBBA4M9cgIV0b_378ZQczeG8fXfbbMfe6iyv1zjiJJAkxUep82SI7X4qWRC591AcASo6Zmh8XC33YTSHAFk7Lw1JI8MDkLrYWn2HxWQRQGICer2ps3_f-LG8Nr-2twTXwYoDOfJ8Gc7HOUCrP-J9Jbok9PTP2ZOrlYavhgxvoB4-y6ekO39v6gnW-hsU88Uph1F_0rG-6PDXix_vZsNFVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c2539c0d4.mp4?token=M3bk1_bsIw5lmwA4SYEjg0A7JleGzbHVGxnSKfZe8s_DnVcWZqLFrH8iecscnul6bsQnPTF4CcH4bRIzPCxWM4ibw2QtwKY-6w0EUJBy1TCdOuq9T7cO-D03_fGdcLUWUBBA4M9cgIV0b_378ZQczeG8fXfbbMfe6iyv1zjiJJAkxUep82SI7X4qWRC591AcASo6Zmh8XC33YTSHAFk7Lw1JI8MDkLrYWn2HxWQRQGICer2ps3_f-LG8Nr-2twTXwYoDOfJ8Gc7HOUCrP-J9Jbok9PTP2ZOrlYavhgxvoB4-y6ekO39v6gnW-hsU88Uph1F_0rG-6PDXix_vZsNFVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود یک فروند بوئینگ ۷۳۷ به ناوگان لاد ایر
🔹
یک فروند هواپیمای بوئینگ ۷۳۷ با اتمام مراحل چک سنگین C، به ناوگان شرکت هواپیمایی لاد ایر اضافه خواهد شد. این هواپیما چند ماه پیش به کشور وارد شده بود.
🔹
به گزارش کن‌نیوز، ورود این هواپیما گامی دیگر در مسیر توسعه ناوگان لاد ایر و افزایش ظرفیت عملیاتی این شرکت به شمار می‌رود. لاد ایر که فعالیت خود را با محوریت فرودگاه لارستان توسعه داده است، در ماه‌های اخیر در مسیرهای داخلی از جمله مشهد، شیراز، ایلام، اصفهان، آبادان، اهواز و... در حال خدمت رسانی به مردم می باشد.
🔹
با اضافه‌شدن بوئینگ ۷۳۷، ظرفیت ناوگان لاد ایر برای توسعه پروازها و افزایش مقاصد پروازی داخلی و پروازهای بین المللی تقویت خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/686151" target="_blank">📅 14:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686150">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588e633c3e.mp4?token=ePTlgbNVgVDueM1WGn163geoIB7wCUvVTtU2O6p-u1vsJZJ4d2g0EGHbKMkr31NePolhe1SjXhA5OLjnr4PD1np-yDrviGJ2t4C7t9nCo_xKqcEbRhfRKhex0KNCLygEeQOEitLxDck6LJUEsIUE1yqji5LIvtrCE0DbgQ6RVsqrdISB96NPVpGjlJ4xqhw5zVUiBPRrAh0oa3aAW4KiusTTfdEE2kwHfiNqTfEx6E4l6PpiFOgrpGTgagmZxsikV40fpQHgJYm22Cxza5Ov63L7OiLnCF8QA-2wb3JdIHytbmcCmRJrtsleDCx5vmuz6GvHU8xnydGqCkc3-iqzLDeps8aiKSd-0iT6LUAGJKZMkWcUCoyJghTVAZxdNPt1n1gpmi1Yx8v1TRx_uXjMMLQ6_KUN5AquJF30tHjO94ovd1ALvOVKYkq5uCx1sRXA6iyYFFePtb9lXJQtMNZ-J47Y2XaxtmboZJ_1olWktpRCjgKUGP0QfM9YveF6bz39Ugpvvgehm0LZT0N1yO31FAexWn66Xm9S2CRFj0MTpmWerKNBQUOny0dyXkFGJhpW9VHSTqQIhgPRO_IxMlYbEgtcBGkLLmX_v33b6lLsLHHOUzpt6xQ-XhGw3OywU-A7qMfS2B2AhLV42iPZuaO2N89vFpbpQ5uNVDzRlWm64cU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588e633c3e.mp4?token=ePTlgbNVgVDueM1WGn163geoIB7wCUvVTtU2O6p-u1vsJZJ4d2g0EGHbKMkr31NePolhe1SjXhA5OLjnr4PD1np-yDrviGJ2t4C7t9nCo_xKqcEbRhfRKhex0KNCLygEeQOEitLxDck6LJUEsIUE1yqji5LIvtrCE0DbgQ6RVsqrdISB96NPVpGjlJ4xqhw5zVUiBPRrAh0oa3aAW4KiusTTfdEE2kwHfiNqTfEx6E4l6PpiFOgrpGTgagmZxsikV40fpQHgJYm22Cxza5Ov63L7OiLnCF8QA-2wb3JdIHytbmcCmRJrtsleDCx5vmuz6GvHU8xnydGqCkc3-iqzLDeps8aiKSd-0iT6LUAGJKZMkWcUCoyJghTVAZxdNPt1n1gpmi1Yx8v1TRx_uXjMMLQ6_KUN5AquJF30tHjO94ovd1ALvOVKYkq5uCx1sRXA6iyYFFePtb9lXJQtMNZ-J47Y2XaxtmboZJ_1olWktpRCjgKUGP0QfM9YveF6bz39Ugpvvgehm0LZT0N1yO31FAexWn66Xm9S2CRFj0MTpmWerKNBQUOny0dyXkFGJhpW9VHSTqQIhgPRO_IxMlYbEgtcBGkLLmX_v33b6lLsLHHOUzpt6xQ-XhGw3OywU-A7qMfS2B2AhLV42iPZuaO2N89vFpbpQ5uNVDzRlWm64cU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روز شلوغ غرفه خبرفوری در الکامپ ۲۰۲۶
🔹
از اولین ساعت‌های شروع نمایشگاه تا میانه روز، غرفه خبرفوری شاهد رفت‌وآمد و حضور پررنگ بازدیدکنندگان بود؛ از دیدارهای تازه و گفت‌وگوهای جذاب تا ثبت لحظه‌هایی که حال‌وهوای الکامپ را متفاوت‌تر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/686150" target="_blank">📅 14:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686149">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcB2GVHl2b9fiE77Hvvl9HofcTRgRznXpYMr0a_7mPo1Nrx4PuRXc2EWIO1OwSMTqct_UMgWzgVDU3hA4Vv1vwpa1B46hvDzpLKA6U5HjV_-Kq9WtXmvTu3A0oHbQpytaMlK6aSVfSJMSi98sE0_LzR7GkSAiBYmOi5JiqVOtXRtgbL8be7L-7KU7vLhutAonofBpZAzp10yeGVq1qVShLr43wiS3qIr8Krqlin2tC8nwWfVbjC3xVtY9UmatkIwoJRXVkcG9m9tY5WGWmDgJXoy2gH4A2_FcygYxN-V95MIMaCDPnMUp6t2sA3oeROTbILUERHXGAmeT0eexmJ6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دهم شهریور روز پدافند هوایی ارتش، بر تمامی کارکنان این نیرو که در خط مقدم جنگ با دشمن آمریکایی اسرائیلی بودند مبارک باد
🔹
آمار زیر تنها مربوط به عملکرد پدافند هوایی ارتش در جنگ رمضان می باشد:
۱۷ پهپاد MQ-9
۲۴ پهپاد هرمس
۱۸ پهپاد اوربیتر
۲۷ پهپاد لوکاس
۲۱ موشک تاماهاک
۱۳ موشک JASSM
۱ جنگنده A-۱٠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/686149" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686148">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H33eV8QqhOSiH_hLjAWaO-lC1gKmCfhAsKiIfLR1ePl2qodIAsgFgsOl56da8zBFBYO9E2Pf5aryEhPCvmP7wEkvZG_dDqdH-e8fKuNsy5wUZQXUTIG-jh-tO8hkYIX5vwFAIyEnEBQuMba1JX0nfI-84ZFsYF5n8l5V0cw4y77GkZ3gJRNRXbnjKiw7HQsQvtPYt1Py0IykZyHDjOP73xfRY-9CBogFiZxatrX6NVMlj64OwJlOKW-DSaQ7sCsAVhCixFffp3tDLhH1OxbyRX6-lj2tpYSCYh9ihQDJH9u7lKcVAyv2nR4rnW0iOZf0wE6QbT9X1GDID9PYFUFcxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نبویان: اکنون بهترین زمان برای حمله پیش‌دستانه به منافع آمریکا است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/686148" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686147">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8874808e.mp4?token=niYZhycWQ0VLdBbX_ayKsOuxhs1-UBL8kTyZvG2lpbIOMU8JWpnUkLS3f6Nz9RFJUYLaEPbEDeVmIut1oCiEn5UkWQZT11SV0Csgyjo1gDno0Kh7vlP89-THtchLzFaxRDOAb_cLaMdtvCE4_Uy2p2kJufXI1bc16vng6gUjgJ0RPzKab6jbPOcpoQ-432iv0g3kqFhhfm0jma05QqJBYmBYkxrpucei_x-ZpjmBqbQauC39ZqiM6I2dlqRNipJPn9P1lm0kHY_bADWktu4vsSZTdHIlwK7R5g3Nt0GIkuU9USFIRK6ZcIztYhKPDvDuK970d9o9mfWAVp0ZE-5Etg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8874808e.mp4?token=niYZhycWQ0VLdBbX_ayKsOuxhs1-UBL8kTyZvG2lpbIOMU8JWpnUkLS3f6Nz9RFJUYLaEPbEDeVmIut1oCiEn5UkWQZT11SV0Csgyjo1gDno0Kh7vlP89-THtchLzFaxRDOAb_cLaMdtvCE4_Uy2p2kJufXI1bc16vng6gUjgJ0RPzKab6jbPOcpoQ-432iv0g3kqFhhfm0jma05QqJBYmBYkxrpucei_x-ZpjmBqbQauC39ZqiM6I2dlqRNipJPn9P1lm0kHY_bADWktu4vsSZTdHIlwK7R5g3Nt0GIkuU9USFIRK6ZcIztYhKPDvDuK970d9o9mfWAVp0ZE-5Etg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این اشتباه ذهنی می‌تواند شما را فقیر‌تر کند!
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/686147" target="_blank">📅 14:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e871d307.mp4?token=h2gW6i5ZbIKTdHjWe6qsDNrzci8K8QLPwXUXAJaSgTZaSxfKN8QXlWHE_sfEY2Wj_UOvM30qYP9tT4NyAGnyQa86aMKHpVIgK0Zw7aHly088hRjkwyRVh32Q93MlzPctoXhBMKN2xxlKn2GDVDTNrSTyAfORmcwDZb6ubF0jpSPorDDjzwk-22XfpVw6ERggXzKIT8YADLUOMLUTRwBp7txevedKjw5eOhHwjxsuJIkb_B0NcoUD__npoVdVCLN3AnerogXZxc2mJUNUieV-QTZeMW8dAiIB6BdfQgJ2MsxHAiMbtxtoCoy1U5vZ5kcPtbv4eTBBCRLFOonZHJxGuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e871d307.mp4?token=h2gW6i5ZbIKTdHjWe6qsDNrzci8K8QLPwXUXAJaSgTZaSxfKN8QXlWHE_sfEY2Wj_UOvM30qYP9tT4NyAGnyQa86aMKHpVIgK0Zw7aHly088hRjkwyRVh32Q93MlzPctoXhBMKN2xxlKn2GDVDTNrSTyAfORmcwDZb6ubF0jpSPorDDjzwk-22XfpVw6ERggXzKIT8YADLUOMLUTRwBp7txevedKjw5eOhHwjxsuJIkb_B0NcoUD__npoVdVCLN3AnerogXZxc2mJUNUieV-QTZeMW8dAiIB6BdfQgJ2MsxHAiMbtxtoCoy1U5vZ5kcPtbv4eTBBCRLFOonZHJxGuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با هر رنگ شلوار، چه شومیزی بپوشیم تا استایل شیک و رسمی داشته باشیم؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/686142" target="_blank">📅 14:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686141">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
خبرفوری در الکامپ اخبار لحظه به لحظه رویداد بزرگ فناوری و اقتصاد دیجیتال را به اطلاع شما خواهد رساند
🔹
ما در نمایشگاه الکامپ در سالن ۶ غرفه ۳۲ میزبان حضور پرافتخار شما عزیزان هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/686141" target="_blank">📅 13:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686138">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRm10D9sOiMdgAZeR86KSYBckSng3fD1kR49JH6x00fMWiwF56obQ7xx4PXjsWTtmcTKxoHtZfm-DEd3jO2r4FHlagXEEtHPvA7AbrIvkkzsHbjIc776t6LGbzq0-gItqNuqqrY8nCognXrcUr_Uh8FnSYPPFySpNprrryfVMF4Jmjstnu1JMugEOe85RDhS9TivwUn1UPy0eSwZIWBIZGi2geN-8yeBN-IODVrGH6WBrbNzltTW8tycYY9dA3j83yECIhOAEXP4VaxcqtNnxIl02LC-nsvScEcsTT96yajXj_u2FXTXKhHrWPPVs2du14Zn7c6mohZ2TYl7-up0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjsCTnAXHlFR7E6kurmyeYvc_p0D6cJj3iPdW4UAKxfy7ZXZ3gNF_z2dF7prMsNTzDz3TNjVue9dVn56wLMGhSrApsp9oyR88-QatIGiW_XrE4DphRj0OgH2QOs8KKGl7DWSJX0Pm7eTPeajhaGnX-FZrxuBWNzUVUTMCs2w2F3q_iimGi0HqnujP2NJ3tzsoTJIKNgrJoY08vULlGOrQoakI8XQg6LRhqhzf1bgC6vN0mRctJh4jjRLZaVJ5qmnoWXYq52VT4Rq0G6XYlxSx8kYkfV18TBTfF8zLYh_LvvlhexXwlIoVGLogAIdT-o4mA0hrVdXPBLQqgYRPByINg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرعت عمل در بازسازی پل‌های بمباران شده در جنگ
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/686138" target="_blank">📅 13:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686135">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEB3DcETJfUBp5pioux4Q_swgV6LsBJ7tPoTYBDABH1ivDa07eanZVl9HaOj0hIfSO_mIQ8LxT-XEvzPLQyQt4XMNqrLr4-lRT6Xco1V63u-LuOqC80X54vYFaZfARHJZbpGs9_NVDSi2Ioo9c1xtGT6kWpnPOBFtnCGOnhgr3WczWlrFgbepYaHc1WtyOwzwMX5mQtvar0N1zL1vCls6Z8AjShKKzsFpZP8QxZlMrBds8Q6yENAYbd-ufVghAIec1FoQxc_wKccT-OD_r4sBwecX_uOOgfJE4-W2fe9M_dO8HjCX9PyR5TKRSUUAD3TQe70QSvYAErfCStWjPKaPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۰ شهریور ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
امروز دلار از مرز ۲۱۲ هزار تومان گذشت، و هر گرم طلای ۱۸ عیار ۲۲ میلیون و ۲۵۴ هزار تومان معامله شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/686135" target="_blank">📅 13:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686134">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPEJf5yLcyNl9OfDCcGPOUfEbou0Bpixf9edPFKumU8OcoV_dgEVf74Azm_B60Bwcdub7zDF3sip9effMbgzIoMwcoDscLBW1uKhG4AYRx9mvkNQw7D5iwuqq2e9TVyjAL0GpNqYiCsAcCvdujG2O4wAN0y-lv21IMvg3LUuo-K0P7S3xupzgufgmMNyzWgJdTxf7lxCWB2T2LmOltCmr19eruN-OQgkRywr8loR4PH7mF-MUxOjYqrXclEai-D0kHwiPvxOK4NB0H6gzPba4a2wdjTF7bmwwbfbICrxMiX12UNVzIeLwtvkDJ3N9es1WfZ0n4mbjR673S9pBtV2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جا دستمالی دست‌ساز؛ با یک ایده ساده خلاقیتت رو به درآمد تبدیل کن
🔹
این بار در #چرخ_زندگی سراغ ساخت جا دستمالی‌های دست‌ساز رفتیم؛ محصولی کاربردی و دکوراتیو که می‌تواند با طرح‌ها و رنگ‌های متنوع تولید شود.
🔹
با مواد اولیه و ابزارهای ساده می‌توان این محصولات…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/686134" target="_blank">📅 13:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686132">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بازنشستگان ۸۲ هزار میلیارد تومان طلبکارند!
علی دهقان‌کیا، رئیس کانون بازنشستگان تأمین اجتماعی تهران در
#گفتگو
با خبرفوری:
🔹
در حوزه افزایش حقوق و متناسب‌سازی، دو ماه عقب‌افتادگی داریم که مجموع آن حدود ۸۲ هزار میلیارد تومان است، یعنی در هر یک از ماه‌های فروردین و اردیبهشت حدود ۴۱ هزار میلیارد تومان افزایش حقوق برای بازنشستگان پرداخت نشده است.
🔹
هر بار وعده‌ای برای پرداخت این مطالبات داده شده اما هنوز به‌طور کامل پرداخت نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/686132" target="_blank">📅 13:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686131">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام انبوه سازمانی سروش‌پلاس
سروش‌پلاس سرویس «پیام انبوه سازمانی» را برای ارسال پیام‌های خدماتی، اطلاع‌رسانی و تبلیغاتی ارائه کرده است؛ با امکان ارسال متن، لینک، فایل و دکمه‌های تعاملی و اتصال از طریق API.
تیک آبی نیز برای افزایش اعتماد کاربران و کاهش جعل هویت در نظر گرفته شده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/686131" target="_blank">📅 13:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686128">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kibP5ZM3q6cJAErPtEK3ovu44JpTzB4_0RoLXJFcoNdxNOoLryLQGwdrfHS5Rl0zIq7owWS3M3SR_weFM2FFzxEFpnb-FpUS_6GugWQ1fsC6VtLYHub4ROJz0NE5KO2ctNQpwZOnWu3MKtaWFSqPYfqkyK9WvUW6ug1CGkoHrs3yl1-xXNYWzvszUVxKBX7Sb7qJDc3tVWJ3NEnHn4WG37N9KYqCBYuLu0Lb5dstWBFb0NU_8Q2BSlpbXy1BmZT73R_4KnFLQgUGBAbC9R1pw47QmaugCvKhGDOpa4RHaw12GqR7vq3Nieo2ZyRoOk-J2RsMa4PI_QYEXWSMTps0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع خستگی و علائمشون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/686128" target="_blank">📅 13:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686126">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF-DCw3_pBB2ANR9nTq6xql-kuvHRDscuVipbp5IvJnXUzCDIPyUYITHZJsAmb5bMu4z9V3145LwmIBi56V60h3RcQ_gNBiaPSfxtOercPOpTZeDD5xESEzDdJ3cQz7bnb38Qn8I4MmGjOiVuZFSWiebS5ol-EMqR7oNJu5TdPgx9_5B3D9JMwfNan8TxdNIsNiL_LW4xIHBelWFwQczH4tEEFp8-fcV1UFvSr9DVaZLCyuu974usyfXbqGeya4t9NFzMNF4R2v2CtortybGx-6rhQPlexeT8hGL83KnsWznrxH3BPKaQ2Ra_QY5X6ZP4j1fWuq05lnIeZ7QiW51qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤝
🙏
گام بلند بانک تجارت در حمایت از کار و تولید با مشارکت در طرح ملی همگام و معرفی محصول ستام تامین
🔵
این طرح ملی که در قالب تفاهم‌نامه همکاری مشترک میان بانک تجارت و سازمان تأمین اجتماعی و با حضور وزیر تعاون، کار و رفاه اجتماعی به امضا رسید، به‌دنبال مدیریت هوشمند تعهدات مالی کارفرمایان و رونق‌بخشی به صنایع است.
🌐
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/686126" target="_blank">📅 13:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پیش‌بینی‌های تولید گندم محقق نشد / دولت باید ۴ میلیون تن گندم وارد کند
ناصر مرادی، عضو کمیسیون کشاورزی اتاق ایران در
#گفتگو
با خبرفوری:
🔹
امسال پیش‌بینی می‌شد تولید گندم کشور به حدود ۱۲ میلیون تن برسد اما تاکنون فقط حدود ۸.۳ میلیون تن گندم تحویل سیلوها شده است.
🔹
با این میزان تولید کشور برای تأمین نیاز آرد، نان و مصارف صنعتی به حدود ۴ تا ۵ میلیون تن واردات گندم نیاز خواهد داشت.
🔹
قیمت خرید تضمینی گندم امسال ۴۹ هزار و ۵۰۰ تومان تعیین شد در حالی که کشاورزان معتقد بودند قیمت منصفانه حدود ۶۰ هزار تومان است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/686124" target="_blank">📅 12:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686122">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تکلیف سوابق تحصیلی کنکور ۱۴۰۵ مشخص شد
🔹
پایه یازدهم: تأثیر مثبت
🔹
پایه دوازدهم: تأثیر قطعی
🔹
سهم سوابق تحصیلی: ۶۰ درصد در رشته‌های پرمتقاضی
‌
🔹
این مصوبه از سوی رئیس‌جمهور برای اجرا ابلاغ شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/686122" target="_blank">📅 12:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686121">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVslmvc2WhfZYhdYTIhFB1FfyFREW6lnQIglo84xk4SwwDSi_jzBJG0IH1uebBIXzSJfumpNd1OuLTSDwTM3NPnp15DMB2ftYOn3z0emkwLr1M8qIaw8-mS3d7JrBL068QaXKh_UaM9WLU6Y5TYzmRkTVLaa-MXjpWl12Byzp6w5NgDvUD-K3o_l6rymuXoouL9p8htafaGrf22GNufYbefFoGTXe6xByE9gr_9pVqHTVazJ5ntaviW7sqEP-k9ZtZ2XxYIbwjdU-GRakZvQi4MNKDitMfUBo4XgIcGHGHACdoiECMgl62rweb6m8mss2vLifmvY5iBuR-e6Zo4vKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلگرام سرور را حذف کرد/ اجرای رایگان بات‌ها بدون خرید VPS!
🔹
تلگرام از قابلیت جدید Serverless رونمایی کرد. قابلیتی که می‌تواند دردسر خرید، مدیریت و نگهداری سرور برای توسعه‌دهندگان بات‌ها را به پایان برساند.
🔹
در این مدل، تلگرام اجرای کد بات را در محیطی ایزوله برعهده می‌گیرد و منابع را متناسب با میزان ترافیک به‌صورت خودکار مدیریت می‌کند.
🔹
بات‌ها همچنان می‌توانند از قابلیت‌های مختلف تلگرام استفاده کنند، به SQLite متصل شوند و درخواست‌های HTTP ارسال کنند؛ با این تفاوت که دیگر خبری از مدیریت سرور نیست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/686121" target="_blank">📅 12:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686120">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c879625ad8.mp4?token=sODoFgCjf1AH8_D4AiCMYknYo-q_tK0CM1tLZaj6dYXixj7-A_o6WHZ0GRc4S7O032LUN9wtKaF0pTmwyDChu9viI5mVu8j8hoR8GVyCT88-u3QWFt-YXulGyHPSAVs13XCzsVFrFPJ4fiL-P3lGzO6NmteiOv-wFZD60zXvNl1Xun9Ye64Cx8VQzhINSNnadYFMALEFrV4CKu7WulvooemXMwtPQxFi1GgfGUXK2H8ajaZMwTwo_ra8qQejeKNUisuuDD0z2z_CG-ntpHd709MByQWpS0al_rBt4pXhs-LmKJDNBSnF3xi7EbgW7m3KxzOHyrKQ3b15mRolFy2pFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c879625ad8.mp4?token=sODoFgCjf1AH8_D4AiCMYknYo-q_tK0CM1tLZaj6dYXixj7-A_o6WHZ0GRc4S7O032LUN9wtKaF0pTmwyDChu9viI5mVu8j8hoR8GVyCT88-u3QWFt-YXulGyHPSAVs13XCzsVFrFPJ4fiL-P3lGzO6NmteiOv-wFZD60zXvNl1Xun9Ye64Cx8VQzhINSNnadYFMALEFrV4CKu7WulvooemXMwtPQxFi1GgfGUXK2H8ajaZMwTwo_ra8qQejeKNUisuuDD0z2z_CG-ntpHd709MByQWpS0al_rBt4pXhs-LmKJDNBSnF3xi7EbgW7m3KxzOHyrKQ3b15mRolFy2pFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از نظر علمی چرا نباید خانم‌ها استرس مالی رو‌ به دوش بکشن؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/686120" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686118">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
کرونا دوباره فعال شد؟ وزارت بهداشت پاسخ داد
وزارت بهداشت:
🔹
افزایش فعالیت برخی ویروس‌های تنفسی ازجمله کووید۱۹ در کشور مشاهده شده، اما نشانه‌ای از وضعیت بحرانی یا ویروس جدید وجود ندارد.
🔹
مردم تهویه فضاهای بسته، شست‌وشوی دست‌ها و رعایت احتیاط هنگام علائم تنفسی را جدی بگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/686118" target="_blank">📅 12:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686117">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c029cf629.mp4?token=oQ3MjvhvniGWQXTUvnKDRESYwhlstKuEGeNbD7BBLUjKEPU9QqV4yV4IMb1nGm3uBmf5eczhD9b5vJhYKZ31DXiOQtlgsA4pvM1rKMt-Tfbaf5PLQKI_JZCYymP-EEIqubfl9esixeAuN_CqFidq5cvszHlt2lfUK-R6HIWVFnO3sX0EWZVVEVjrXgaHKMK4RmIVid0cPXAuzV1wstodVNq7cOs8cBlT1xy2UmZ_EW-tkr_e_zBerSM4P14OaN6tsk43METMyPpfaZYBeSt9Y8DH8m9-YaZUUjcdNLa7IkBjItfxEaETs49iahJopIlj7yVSPMg7ipE59huWD5iPkrtRMRtq_tguJO160iteUkvo2AY1-H7Ooq3JdwPhCiaTLiT7jRu-9ncEvX0KyH0y9d6xghvLIlMArENWdgaLhebStE08pP6pSSNxZu55Rl_PcM72XdbrjzDiBsRZ7EN5ZHwKtcZAz1S3e6NmsguKohNpYOJV4QI6J8uk1m6RYvel2mTdt2VdbOPu8MEiRMhsi0b2O9LynKAQ0wiY5qhG9OAumo9vPWFpXIb2Drh0yN8VkmUgIRvNrP5BTX4m5mJW_xChy3kmQkkdSAKq9cb6PIR7jOq-FycBJe3joxG3QRpJgcp1yHFBGHvHT06flsMsNVSZ7Ho5PIR-zX158DPvPuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c029cf629.mp4?token=oQ3MjvhvniGWQXTUvnKDRESYwhlstKuEGeNbD7BBLUjKEPU9QqV4yV4IMb1nGm3uBmf5eczhD9b5vJhYKZ31DXiOQtlgsA4pvM1rKMt-Tfbaf5PLQKI_JZCYymP-EEIqubfl9esixeAuN_CqFidq5cvszHlt2lfUK-R6HIWVFnO3sX0EWZVVEVjrXgaHKMK4RmIVid0cPXAuzV1wstodVNq7cOs8cBlT1xy2UmZ_EW-tkr_e_zBerSM4P14OaN6tsk43METMyPpfaZYBeSt9Y8DH8m9-YaZUUjcdNLa7IkBjItfxEaETs49iahJopIlj7yVSPMg7ipE59huWD5iPkrtRMRtq_tguJO160iteUkvo2AY1-H7Ooq3JdwPhCiaTLiT7jRu-9ncEvX0KyH0y9d6xghvLIlMArENWdgaLhebStE08pP6pSSNxZu55Rl_PcM72XdbrjzDiBsRZ7EN5ZHwKtcZAz1S3e6NmsguKohNpYOJV4QI6J8uk1m6RYvel2mTdt2VdbOPu8MEiRMhsi0b2O9LynKAQ0wiY5qhG9OAumo9vPWFpXIb2Drh0yN8VkmUgIRvNrP5BTX4m5mJW_xChy3kmQkkdSAKq9cb6PIR7jOq-FycBJe3joxG3QRpJgcp1yHFBGHvHT06flsMsNVSZ7Ho5PIR-zX158DPvPuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قمار دریایی آمریکا برای نفتکش‌های ایران
🔹
زمزمه‌هایی در آمریکا به راه افتاده که آنها برای نفتکش‌های ایرانی نقشه کشیده‌اند!
🔹
اما این نقشه آنها تا چه حد عملیاتی‌ست و چه عواقبی برای آنان خواهد داشت؟
🔹
ماجرا را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/686117" target="_blank">📅 12:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686116">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f2bedb73.mp4?token=RnmdFaknqRjVFhYO89Lbhzpa6VOO4LQTNRIT9zTYuIvzv_VfuDFQaNkNo0xBlbrPbTC9QouLoevyh3hS-wPKiHtYLlPhUFlsxa1KplsXwBzbjkvP_chqY-dWrhQVvOhqhp1g5agmvZ5IRQh5ODtW-5oOkGLLtaSTqGD7O2TlJmdTrZjGUoccpQSxtW4BgErb2y0uDTwYFGLK4rWK30WcUTqBrRQQyuwKnk69ZmCS2PQlRWFotoNwE1X7p_5NL6fbKDuDTZDtiwDgLfusXMUR43nUhd6XURn9PPyc0n5RBJYS8O6lfd0876zhAHrcVRNCxK89JGEr48sdKpVbOPGj1E3GYkjh3G3DADHtceWwb2XAhpfuABxKIPru-ZhBjohQ_G6FJj4iv31hlnc24Lub4kzQkSaUmLrRYG_YsfUySych2l095zeP6fnaM4ylmxdMMerImVrxQfEfMIWavzzpVBk14px8hDRfC-m1FWI8ARVcCIvuaSYL_cqsk2Vdq60unX633lAYTduPU9b29_yYemURjammVbVcx4c--vm5nqAgfZVq2yyjwx4YNOONCoBV9Dzt3FnOrO1rfgE8N89m6kT55v7h05Df9bVvdO9qAa4mh_CsR6eND6N9Dpdx0Gb2RuuekKwE_C3KaENxDbO9bNdcL42E2pKuPrBn4ObOViA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f2bedb73.mp4?token=RnmdFaknqRjVFhYO89Lbhzpa6VOO4LQTNRIT9zTYuIvzv_VfuDFQaNkNo0xBlbrPbTC9QouLoevyh3hS-wPKiHtYLlPhUFlsxa1KplsXwBzbjkvP_chqY-dWrhQVvOhqhp1g5agmvZ5IRQh5ODtW-5oOkGLLtaSTqGD7O2TlJmdTrZjGUoccpQSxtW4BgErb2y0uDTwYFGLK4rWK30WcUTqBrRQQyuwKnk69ZmCS2PQlRWFotoNwE1X7p_5NL6fbKDuDTZDtiwDgLfusXMUR43nUhd6XURn9PPyc0n5RBJYS8O6lfd0876zhAHrcVRNCxK89JGEr48sdKpVbOPGj1E3GYkjh3G3DADHtceWwb2XAhpfuABxKIPru-ZhBjohQ_G6FJj4iv31hlnc24Lub4kzQkSaUmLrRYG_YsfUySych2l095zeP6fnaM4ylmxdMMerImVrxQfEfMIWavzzpVBk14px8hDRfC-m1FWI8ARVcCIvuaSYL_cqsk2Vdq60unX633lAYTduPU9b29_yYemURjammVbVcx4c--vm5nqAgfZVq2yyjwx4YNOONCoBV9Dzt3FnOrO1rfgE8N89m6kT55v7h05Df9bVvdO9qAa4mh_CsR6eND6N9Dpdx0Gb2RuuekKwE_C3KaENxDbO9bNdcL42E2pKuPrBn4ObOViA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بات از تو، ۲۰ میلیون کاربر از سروش‌پلاس
سرویس توسعه بات سروش‌پلاس راه‌اندازی شد؛ فرصتی برای ساخت بات‌های کاربردی در حوزه‌های مختلف از خدمات و پشتیبانی تا اطلاع‌رسانی و سرگرمی.
با ابزارهای توسعه بات سروش‌پلاس، بات خودت را بساز و به بازار ۲۰ میلیونی کاربران فعال سروش‌پلاس دسترسی پیدا کن.
🔗
مشاهده مستندات و شروع توسعه:
https://soroushplus.com/p/documents</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/686116" target="_blank">📅 12:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686115">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBank Pasargad</strong></div>
<div class="tg-text">☀️
جشنواره حساب‌های قرض‌الحسنه پس‌انداز بانک پاسارگاد
🎁
جوایز جشنواره:
۲۰۰ جایزه ۲،۵۰۰،۰۰۰،۰۰۰ ریالی
و میلیاردها ریال جوایز نقدی دیگر
⏳
مهلت شرکت در جشنواره:
پایان شهریورماه ۱۴۰۵
📅
زمان قرعه‌کشی:
مهرماه ۱۴۰۵
📌
صفحهٔ ویژهٔ جشنواره:
bpi.ir/qh1405
🌻
سهمی ماندگار برای مهربانی
🟨
کانال رسمی بانک پاسارگاد:
@Bankpasargadtelegram</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/686115" target="_blank">📅 12:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686107">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFaDnRfVnmObt6UJrnc8cMmQ7XZl2wroPuDDf8O5j-lTcpFVpEfMcXBklFCXUK8wVK0pS4E5mksLr-pMBMa71S-9DO248GVQnde8Fc0bgRH8AoaAtSaRiQRBQHXKjtFLDgg5mTMDNh3A0lTfJoPyszX8vS4bx7WLd7hwCVh7XVkTVZzlmRtsOdcA4Ag0VOCoIun9_CWps84KLkW5PI5n7fuo7rJ0BQxLEQAv1YGl-ob5V8xJ5G_KpQDgVkDwSKs5aRoqwxdFTA7VNpBsZ_YTbu7Qpx8Eu0SeTEQ7Ca0vNfDYbkID8BrqCOIozg1L3DIVTDTPVmzilnj098Y3caX46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzxPzq-fRtx1j9Xo2-9Lw7zKbUY8SMfGsxq-iUb8h63JrBArD59x1kqK9Ocfukqt-blRaFNTFFuUjDh3Z8ixEPI31yDDuDFHrexLEeefoC1ILFCGzPl5mbR5ISXohD8JVc_bN4QBxiIdV1DPXS7Xh-CR6lITAOTIYJld3sOa6aCsQpcHB3MgtoisU-x_pZttANfJF7ZS88dI7TMAgEh45bztX6gOEisRGhQI6nRuzTrV79juFejZzxV1RwBkQ4qTSfqdyYMdqMRJjl8_0IhZxlWjsDgULIgqUk2Z2fC2QSjle2DmdoL8mD98YbN7J9hw5eOO7TaEz6bwDY4e6YmzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rwvnv0ACucOMMk4710zqPSOr233SDg7omu5TgarRKRJ--Pes1yPA2DUadWEtED16rzxsDNxtK5NrGI98zmoaCPqckhG1_SxeGr-WhfIj7Pd8SPp76FvaP7scifCIllHockR_AqR4CUl8PXieHnFcEdtla3KRt7rwT4jQrF32Is8RRxJm3Pqp5NDaQ52PRUx2KuLFSRznPxoQhrG-2l1L2NcwiQ46usnIQT0RKIDFyKdMbT748bFGv-ypRKA4_tB-HcmySWH1RGhgiNdpcgShP55ybzREMpr9ZECpa1dH5_-159ZCvnMoa24kctggFXZEYvg6MvKWeFMjOff812I76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwZoMHW0sZqTrHT7lWVTcZ7wxojitIwcLbZU9xmsXICoE0vbJ6VOeFQWcNZ6VI6htb9IM54LET2qJjRDDJOkxnhprhyDk8WJzbOwkp-PZIpKmXH6vudVhtKlbWYuuFxwRI0gmQpwzRbvTQsVjvSSevr15eL5DpJ-jdSoJ2fGBSTuSmgSQfw7vs0MHQJd91WgNQHPFSkXNQ4vntCBrc20QtevDmhUNFKbVzzF8Uxx8AISpm3AMoJDDNXuCsUf--rTL7QyM11XF6C8e4gh2qH-NFWsVwktZkPiq3RiOUGHhYMjsvfGD5postqQtMV6wcwZ_QDkJ10nXzyrOzuu2YPRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLSvxnULJY3ODRwY1dOVpqUBN4txkghTH4ODzEx2Rx3yXgzGH5F9BUeA9wuE9g-wp15ok-z2n04eOlILuhhxfMo49i5nyiZrHdYVUpsxwcoDnHoqZS6Li-TLEma5SDGxnhkZ6id7RVJxTKG12wevpyPbGX3y1ax_WX99YwD7R0-bDgUYCQqcDkLSffoLVib_fVNapz9zB0_16G9kzjFjhIvQoEHve_VycAqhtrbCFiHumnorKhnL1SOWRDhvowQqbD3mRGACG_HB1AyWzMXeyIyhsYhgff59eHo-RycIsuEBk93xm6zQZHA4HdGmbpiAV5ecKjOj7LeDnli4yiRi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGFgdrOxHQOSvD3T6fKzMnx2ADrO7qzeNLhV3O3ZmZOLEmsfGK6elNK_o9xF-FgfYYEtEPyXC_cCquAlwDWRl9fOTIES9ZUmOp_gt6bKv_5ofSpEuOeMZ-u7t4SHs823J57duuxYLodZ3iA8R9j-HOMOB4-y10T5sfePjsmjZuuY_zmzfw_rQ5qh-zAljzAUcj3UDpuFCfOLLSbauJqMmIQo6Rg4PmTZzIMNvRLXy4dzpqGpYFOy_foG776Cn2Jo53YhPZ8ZkYKiluam_0RmB-ZrPuBro70e19Fq0_9bNXs1Dqa7HJ0lXSKMa-zle4z5f7VM-Tf7FcjI9cdAiv9uRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdFRipguV-ng0_w8cDH5Vj_I8exB3twiIRaf-u7IfRM_swER8hxLV2v3KL92dfRrSiYF0LtsOweN0iDr6MtBa6FJ63YO3xIrwXb7J0DWUbmTrJFmkYktLbn2LPwMoMZNNP9JvHaR7wnFzGzW5WV6HxhXVJt61o5niPKiPSrdlPxIqTMENgatS8qALOUrhMf5nESPSOIN4_BIpKwi5QKwBzyr81XDP5li_GWiAvBQ_mHKGj7m1Joz_cmjRMNY93PC7vsTRiMIhmUR9ZOx8-mED1_a6WtxiZ7G5Od_Iamj-hiVLa73bdAzj_U8bISHIPDriwkWEME2Ar8E6_iqyMyoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_rLlTl-Y0vWQJxMZ9j3TkOBOTWG8JsM-El5PIZQ4ggHWIZJn2fo14tCIbNSAx_n3Hvw9TQCfqF0AxLCX3E5Al4RLpwvcL_FglvfKS_njH61v4ze60kaOLkl2j_CjXzfx-IJPiaE7YxUK3LKCAnTz_2pK6mYF58e48BKsRb3sqNLYi_76ieiS5rvI2hDudAMH1g-To4tIhc4fYcZwoiO5A2yuYxLZv2frsBrrrqGdXq5hnRWnmCRHYPccDee6EPBibpnnUETrIwOCXxOc3tdXY0VHvrLEyBa5eYgANnlN6y2I5nwEMwtSUF8YwwpM0f_ahxZn1hIpPjp0U8oL-lJkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دومین روز الکامپ ۲۹ از قاب خبرفوری
🔹
روز دوم نمایشگاه الکامپ آغاز شد و خبرفوری در سالن ۶، غرفه ۳۲، همچنان میزبان شما عزیزان است.
🔹
تصاویری از حال‌وهوای روز دوم الکامپ و حضور بازدیدکنندگان در غرفه خبرفوری؛ منتظر دیدار شما هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/686107" target="_blank">📅 11:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isPSVDMnF938w7E2vCj8OB1hQAFnm0luQVSizW6UAOt7xkm4WfeP21i218WGfgxkYas1VGKQq4KgKSlgEf-tXryX_xuuFi983G0NEgnbjik1EGsbM-WY9eWq6leBTn56y1TGlAhXFEeUe7HxzWg43dmMzrM1a69g7J3k842xg6uO2wyDjAhe6lxNaFw1RWZ8P83_QQd9HGSFuCBCG4skUiN8JkLM-1O0nnX0kTYKvXt0YHbpb8TQqt3WquWNOVvm_rX-ZdGqFe-oE5zbgw_vH5wunz6_x5NFlwBYgIKuauycXEABJXpgolJpoWKDLc80iv9FIHkTPDop9VVCW0cdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایتی از قتل هانا راکان دختر ۱۶ ساله کرمانشاهی که قربانی خشم پدر شد
🔹
هانا راکان، دختر ۱۶ ساله‌ کرمانشاهی در مسکن مهر دولت آباد کرمانشاه بر اثر اصابت گلوله به سر جان باخت.
🔹
مادر هانا مدعی شده است که همسرش را در حالی مشاهده کرده که به صورت سراسیمه از پله‌ها به سمت طبقه دوم ساختمان می‌رفته و یک قبضه سلاح کمری با رنگ مشکی در دست داشته است.
🔹
فرد مورد ظن در این پرونده تاکنون دستگیر نشده و متواری است./رکنا
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/686104" target="_blank">📅 11:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686103">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1thNXNNTo1HWUWbR0_0m3iYqcjC-DgHs9BJcdQp5ErUUgEw-3iNRs2zJnWCzQdC1-ym-vfseiizSOVo-8yzPzBUCCy8NPjX_SIkyRZvrBdzVHvZi3rZgMHFg_51UhYEDO-wGBcAo4YCn-9fw9v2sGVggUk7CxWQgK0e6Mkip1WllB1KqyMdkvvqj2HSUeCqYHiwT4nu1hvBfz0rmXi8rYb7OAhNDcFtKvdlDfGzVJit9bdK5CVRdUDxpjJ8_ayh7-BRbTdkb3E5M756Gb4ycUj4TCtrfwg4ecgwCZXxlAIEvGaiaBqrV7UINt_22M14RegOL38XzFbUddM32Px00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری در آستانه بازی استقلال و پرسپولیس
🔹
همراهان گرامی خبرفوری؛ برای حضور در این پویش کافی‌ست یک پیام صوتی ۱۵ ثانیه‌ای ارسال کرده و پیش‌بینی خود را درباره دیدار حساس پرسپولیس و استقلال با ما به اشتراک بگذارید.
🔸
برنده مسابقه کدام تیم خواهد بود؟ پرسپولیس، استقلال یا تساوی؟
🔸
نتیجه دقیق بازی چند چند می‌شود؟
🔸
گلزنان احتمالی این دیدار را حدس بزنید.
🔸
لطفاً در ابتدای پیام صوتی، نام و شهر خود را اعلام کنید.
🔸
پیام صوتی خود را به آیدی زیر ارسال کنید
👇
#دربی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/686103" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686100">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر کمیسیون آموزش:مدارس مجازی شود، هفته آخر شهریور اعلام می‌کنیم
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
در حال حاضر از سراسر کشور دانش‌آموزان درخواست مثبت شدن تاثیر معدل پایه یازدهم را دارند، به‌علت اینکه این دانش آموزان تحصیل خود را در ایام جنگ سپری کردند احتمال مثبت شدن تاثیر معدل یازدهم برای سال جدید وجود دارد.
🔹
مجازی یا حضوری برگزار شدن کلاس‌ها به دامنه و میزان جنگ بستگی دارد، اگر بنا باشد کلاس‌ها به‌صورت غیرحضوری و مجازی برگزار شود هفته آخر شهریور اعلام می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/686100" target="_blank">📅 11:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686099">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpDjwRsMILEF4x7cui-ZQy2cjkJSseGZiv2fLIK9YGrxTJcwROJlpKbBfItYZ5DNaDmykMOAk6h6L1vAX97ngVL0K6kEgBibUiW-KJPZMjUYZNVh6t7o_0r-mIPeV9dCU35vuxO9wo41u2oApBB3cHCLKDv8hKyof74_deQIGg7QeaMb5Etu6K24Qeu9rokh7POl-JfJ3DGNhyb0eEIEYT9Vnw0SdGhWQbADpMOL_PtyKYY9o_9zVmRhvSEhyQ8IDH5GLqdaYipTQwTiQaRvTPXO9yrNee8DZcqIC5L-yzP4110ggdYb5RSEnA2MI4TrMDI3i79JCIk9Ma8rRCLUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسوشیتدپرس از حمله آمریکا به لامرد پرده برداشت؛ ۲۱ غیرنظامی از جمله ۷ کودک کشته شدند
آسوشیتدپرس⁠:
🔹
بررسی «ایروارز» نشان می‌دهد سه موشک PrSM در حمله به لامرد، با پراکنده‌کردن ده‌ها هزار گلوله فلزی تنگستن در شعاع وسیع، غیرنظامیان را تا شعاع ۵۰ متری محل انفجار کشتند؛ دست‌کم ۲۱ غیرنظامی، از جمله ۷ کودک، جان باختند؛ ارتش آمریکا استفاده از این موشک‌ها در ایران را تأیید کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/686099" target="_blank">📅 11:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686098">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سخنگوی دولت: هیئت دولت طرح دورکاری برخی ادارات در فصل زمستان را بررسی می‌کند
🔹
سازمان اداری و استخدامی موظف شده برنامه این طرح را آماده کند تا پس از تصویب در دولت، جزئیات آن به‌طور کامل اطلاع‌رسانی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/686098" target="_blank">📅 11:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80a57d36c.mp4?token=u0Q80TCPGTRZc-GpXR51CbYIXF_RKv_KOz3KVq0hvWsfSpTC0qtb0bfkcE78jYx5WeH_u0v_8nd7p-4MfiBFxw657pUVDla-L4nQ5dVIQuHOmIvPLPUUykdZNX8lNnP9YFsqASi76WuWaiLfhNAeKm6LC0wml-dY55jchr9tD1U6xfdv3X0l0K3EpCpo2M8E0USY7AG1BzDbsiTjqmLI2gMdqZ1xKcrjszzrtUkFGmNP83mWq3b7GyGDziokvLrpnW0eM4QgTAhy1_dS9NoHvwFpfFv2ws6MKunr9QgvFxY9xyEVa8zVijcOG86WCe3eXK53-DOIEG7xIFYrWUF83U2FFmdS4QHNx-4dp8YOrLf_bQcJk6i6z6DVhFZLn1PUZfhepw7KIzpCJpbBY6fpncWgMrLGEETHIMpwvs5NlpPnhjHUw5ooITPGfOHmwmaCK10WwMwFr-28h7Ojx2uTizJPNUslNF2TTJPRhyMjszhsMhkiK40p3BMvsXyFccjMKb5TszNuHv4rMF4YjvIW1E57fkgQxcdf3wi3iiEeZ3-Yp8_jMaxsgvYg-BiK2Dy8kHGKY4YGt1c5KGRPcvqQ9zzVo4JZSbJFQS7sCjhHSRUoO4Yma-Zvoj04xmLVrk7jdhitiblcqb78LWIPITiKz6pRAFp13K5L0vqy42T2NDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80a57d36c.mp4?token=u0Q80TCPGTRZc-GpXR51CbYIXF_RKv_KOz3KVq0hvWsfSpTC0qtb0bfkcE78jYx5WeH_u0v_8nd7p-4MfiBFxw657pUVDla-L4nQ5dVIQuHOmIvPLPUUykdZNX8lNnP9YFsqASi76WuWaiLfhNAeKm6LC0wml-dY55jchr9tD1U6xfdv3X0l0K3EpCpo2M8E0USY7AG1BzDbsiTjqmLI2gMdqZ1xKcrjszzrtUkFGmNP83mWq3b7GyGDziokvLrpnW0eM4QgTAhy1_dS9NoHvwFpfFv2ws6MKunr9QgvFxY9xyEVa8zVijcOG86WCe3eXK53-DOIEG7xIFYrWUF83U2FFmdS4QHNx-4dp8YOrLf_bQcJk6i6z6DVhFZLn1PUZfhepw7KIzpCJpbBY6fpncWgMrLGEETHIMpwvs5NlpPnhjHUw5ooITPGfOHmwmaCK10WwMwFr-28h7Ojx2uTizJPNUslNF2TTJPRhyMjszhsMhkiK40p3BMvsXyFccjMKb5TszNuHv4rMF4YjvIW1E57fkgQxcdf3wi3iiEeZ3-Yp8_jMaxsgvYg-BiK2Dy8kHGKY4YGt1c5KGRPcvqQ9zzVo4JZSbJFQS7sCjhHSRUoO4Yma-Zvoj04xmLVrk7jdhitiblcqb78LWIPITiKz6pRAFp13K5L0vqy42T2NDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«ایران‌بوم» در الکامپ ۲۹ رونمایی شد؛ دولت پلتفرمی در مسیر تحول دیجیتال
پاویون دولت هوشمند با حضور وزرای ارتباطات ایران و عراق افتتاح شد؛ جایی که «ایران‌بوم»، برنامه ملی زیست‌بوم‌های دیجیتال دولت به همت سازمان فناوری اطلاعات ایران، برای نخستین‌بار با هدف معرفی تصویری و تعاملی خدمات این حوزه در الکامپ ۲۹ به نمایش درآمد
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/686096" target="_blank">📅 11:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARSOsnl2zlNbIOZplG-wbdomILSlNeEnv9xkKYzw4UhAzXb3E63wmCUfjIEuouhoxxQjqhWolhbprBTZ1AVpzGlcVmGxzeFzo95zo07Il5IqcUR-ChlR7tl_v0Q1Ulpi4P2u3_YT5uwu3OR4t5kHO6S8cxaQ3Z83z7_rnDtp8eSSlckbOrwGo6m31YLd8cAWVZkTGY9b0WdDilJakWxk1iNL7ViuXnpAhm7nIj6c-nZGK02ZYCleUN7fAzOiP2oWTFdemiy1L1SIjT9KMykRtwW-Vj5_RJxvx-Cq4_UIEnRtcNjJ4pVmzGPvy_mvmbQQmY35HmkWl-tz6ddDdVUGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یو‌اس‌ای تودی: ایران با موشک جدیدش به آمریکا شوک وارد کرد
یو‌اس‌ای تودی:
🔹
ایران نسل جدیدی از موشک‌های بالستیک را به کار گرفته که می‌توانند از پدافند هوایی آمریکا عبور کنند و با دقت بسیار بیشتری حمله کنند.
🔹
جهشی تکنولوژیکی که به گفته کارشناسان نظامی، حلقه پایگاه‌های ایالات متحده در سراسر خلیج فارس را آسیب‌پذیرتر از دهه‌های گذشته کرده است.
🔹
محور این تغییر، یک موشک بالستیک با قابلیت جابجایی بالا است که ایران آن را خیبرشکن یا «قلعه‌شکن» می‌نامد و بردی معادل ۹۰۰ مایل و کلاهکی با قابلیت هدایت ماهواره‌ای و مانور دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/686093" target="_blank">📅 11:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnjaRKAJ_0LHVQxnURRPY8K2gigLVKavbN_2ppBMMBCLY7tfBW0Wc_e2Wmu6KD7xeL-Iam4-E8of1QwgQE3i3FgdAEQTj0PTH6hiL3Uy9yflnJr9C3TnwLLwkagxKEwrTlNTciVWR9k-NSRexp_Xf2BEvqx427MdmrTt2IozcaLB71Rq2oiNphBO3ZQwVTaaV1j3YuGMKvuf_T4Fk_HLsB0nDpPru6ceN0bndEMmnWPWTlD8IxA5fCwRrduwU4aGHODPBR38wtKkAIorhkbu2t1MBl7wznwV4YwvPaatagDyipxfZRso74kkFa74BoBU8l5AnZpYbALptkDClX9YaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/686092" target="_blank">📅 10:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686090">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fef35b95.mp4?token=YAjC1WRcuBO2WRwZ_CrPY7WcHyejo91mn2zT5CjVHs-FkDU5x66_OVLt6oQ4O3zmyfvIk1lCYQi56WS8K_ls4D_cmHbdBMGyeUhr9hziBQupQ06yUY33dl6u6Ig7m85o3EOWbSoM7fEiRNY9wY_ovaQEZ9Hj175QZhcA0thDQSl4GOBU7iA6M6IIN_O9H6TBC_YQexB2qBQoz0fQQg3SsC48jE7ISOdIYuZu395IQ1xLHAp9qpbVt_AkKN07tWCLcapuXsEZUct_63f1oLeCOug24Xd5xH2EFk_JJaU_x-PbLlK86B5srrm8MnWdeY9e3RlMrUqzZTDoPVlnfnVbDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fef35b95.mp4?token=YAjC1WRcuBO2WRwZ_CrPY7WcHyejo91mn2zT5CjVHs-FkDU5x66_OVLt6oQ4O3zmyfvIk1lCYQi56WS8K_ls4D_cmHbdBMGyeUhr9hziBQupQ06yUY33dl6u6Ig7m85o3EOWbSoM7fEiRNY9wY_ovaQEZ9Hj175QZhcA0thDQSl4GOBU7iA6M6IIN_O9H6TBC_YQexB2qBQoz0fQQg3SsC48jE7ISOdIYuZu395IQ1xLHAp9qpbVt_AkKN07tWCLcapuXsEZUct_63f1oLeCOug24Xd5xH2EFk_JJaU_x-PbLlK86B5srrm8MnWdeY9e3RlMrUqzZTDoPVlnfnVbDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت:‌ کسانی که تا سوم شهریورماه مراجعه کردند و محل زندگی خودشان را اعلام کردند، کالابرگ مردادماه به آنها تعلق گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/686090" target="_blank">📅 10:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686089">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae60853db3.mp4?token=mmrdcnTqZpds4mjy0i31q7EsQJ8-dhXIc78XEboslys6J0LWJDicZla87E6uGeNBb1VcddWbvgsnR66I-PsmekAcThijdqHIrMa703LvfHFnvL7iUOkTZBZ448ClBjU8Cswg4XOTornSYdJjNd3xL__9ScCEEpcfFuL9QTX_KusIeSqesGOCvc5y1Rs93eu2_IHEXwYEd9QUhTFL5uQkpHqBa8gSJVkG7hQFXnLhvIKljPrxuuzSnyWZL5AVJ315shLaR-1Bcatdd6Gy2MSzJnrfoFyygLXtEyCoyRgXbXO6NCEvMdQ85s8TzqfksvK5B9mMY7VYYECpcylo9vcsdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae60853db3.mp4?token=mmrdcnTqZpds4mjy0i31q7EsQJ8-dhXIc78XEboslys6J0LWJDicZla87E6uGeNBb1VcddWbvgsnR66I-PsmekAcThijdqHIrMa703LvfHFnvL7iUOkTZBZ448ClBjU8Cswg4XOTornSYdJjNd3xL__9ScCEEpcfFuL9QTX_KusIeSqesGOCvc5y1Rs93eu2_IHEXwYEd9QUhTFL5uQkpHqBa8gSJVkG7hQFXnLhvIKljPrxuuzSnyWZL5AVJ315shLaR-1Bcatdd6Gy2MSzJnrfoFyygLXtEyCoyRgXbXO6NCEvMdQ85s8TzqfksvK5B9mMY7VYYECpcylo9vcsdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جا دستمالی دست‌ساز؛ با یک ایده ساده خلاقیتت رو به درآمد تبدیل کن
🔹
این بار در
#چرخ_زندگی
سراغ ساخت جا دستمالی‌های دست‌ساز رفتیم؛ محصولی کاربردی و دکوراتیو که می‌تواند با طرح‌ها و رنگ‌های متنوع تولید شود.
🔹
با مواد اولیه و ابزارهای ساده می‌توان این محصولات را در مدل‌های مختلف ساخت و برای فروش در شبکه‌های اجتماعی، فروشگاه‌های دکوراسیون و بازارهای آنلاین عرضه کرد.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/686089" target="_blank">📅 10:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686086">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ابداع عجیب علیرضا منصوریان از زبانی نوین!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/686086" target="_blank">📅 10:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686085">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhrRjMCC7OuTW5z5zirKkFgDraaDGhN_7dLTRJyolKGzQ9k7U-lJfb0f_CoV8e63EUR1LxEaSAdzd-bK-EiUHwfGfrnLNIDcYeXYUAxLLjo2UMEhaz9thsqOizmwwu7b8wwAJ3iTyawAe1rNYEBzWRu9FZJ3fpViFp5-T8wGW1XhM13DTPuegHrJ6Od6CvK1WkVd8sWtKPa9-FPkSKJ7F7FVyeH3btEFk_U-SBl31AOm4IXJTu5wrpkn_ViKe5IbuTpkR8ciRjuwffF1z9BW9qrnWT5vHxsRXDpb4KnPkG5rmeFLdAy5TUBu9UJ6MLgj7fMKjdK3klOTfdBCgWu8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازسازی زیرساخت‌های آسیب‌دیده از جنگ در هرمزگان؛ پل گریوه(گچین) بندرعباس تا پایان هفته زیر بار ترافیک می‌رود
🔹
مدیرکل راهداری و حمل‌ونقل جاده‌ای هرمزگان از اتمام روند بازسازی پل گریوه در غرب بندرعباس که بر اثر حملات دشمن جنایتکار آسیب دیده بود، خبر داد و گفت: با اتمام عملیات بازسازی، این پل تا پایان هفته جاری زیر بار ترافیک می‌رود.
🔹
عباس شرفی با اشاره به آغاز عملیات بازسازی دهانه پنجم این پل هشت دهانه از پنجم مردادماه امسال، افزود: با انجام عملیات آسفالت‌ریزی و نصب نرده‌های فلزی، این پل آماده بهره‌برداری است.
‌
🔗
لینک خبر:
https://rmto.ir/s/mfaonFY
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/686085" target="_blank">📅 10:25 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

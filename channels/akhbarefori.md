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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 09:31:03</div>
<hr>

<div class="tg-post" id="msg-686077">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت ورزش و جوانان: سقف زمانی پرداخت وام ازدواج در سال ۱۴۰۶ سه ماه خواهد بود.
🔹
معاون هماهنگ کننده نیروی پدافند هوایی ارتش: ۲۴ ساعته حتی فراتر از آسمان ایران را رصد می‌کنیم.
🔹
قایق‌های جنگی رژیم صهیونیستی با ادامه نقض آتش‌بس سواحل غزه را گلوله باران کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 324 · <a href="https://t.me/akhbarefori/686077" target="_blank">📅 09:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686076">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
همتی خطاب به ترامپ: ارز داریم به قدر کافی هم داریم  رئیس کل بانک مرکزی:
🔹
به‌طور قاطع می‌گویم این ادعا که ایران وارد فروپاشی اقتصادی شده، درست نیست.
🔹
روند وصول مطالبات و منابع ارزی ایران همچنان ادامه دارد و علاوه بر آن، از ذخایر داخلی نیز برخورداریم.
🔹
همچنین…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/686076" target="_blank">📅 09:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686075">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
همتی خطاب به ترامپ: ارز داریم به قدر کافی هم داریم
رئیس کل بانک مرکزی:
🔹
به‌طور قاطع می‌گویم این ادعا که ایران وارد فروپاشی اقتصادی شده، درست نیست.
🔹
روند وصول مطالبات و منابع ارزی ایران همچنان ادامه دارد و علاوه بر آن، از ذخایر داخلی نیز برخورداریم.
🔹
همچنین منابعی در اختیار داریم که به دلایل مختلف امکان اعلام جزئیات آن‌ها وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/686075" target="_blank">📅 09:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686074">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
توجهی به قواعد حقوق بین‌الملل امنیت و  ثبات کل منطقه و جهان را تهدید می‌کند  رئیس‌جمهور در اجلاس سران سازمان همکاری‌ شانگهای:
🔹
امروز منطقه ما با مجموعه‌ای از تهدیدات پیچیده و درهم‌تنیده مواجه است. تروریسم، افراط‌گرایی خشونت‌آمیز، قاچاق مواد مخدر، جرائم سازمان‌یافته…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/686074" target="_blank">📅 08:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686073">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پزشکیان: امنیت منطقه در گرو مقابله با رویکردهای مبتنی بر زور است  رئیس‌جمهور در اجلاس سران سازمان همکاری‌ شانگهای:
🔹
امنیت پایدار نه از طریق تقابل، بلکه از مسیر اعتماد متقابل، احترام به حاکمیت کشورها، عدم مداخله در امور داخلی و همکاری میان دولت‌ها حاصل می‌شود.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/686073" target="_blank">📅 08:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686072">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
محققان: برای کنترل فشار خون خود، بدون عذاب وجدان آخر هفته‌ها بیشتر بخوابید
🔹
پژوهشی جدید نشان می‌دهد افرادی که در روزهای تعطیل حدود یک تا دو ساعت بیشتر از روزهای کاری می‌خوابند، کمتر با فشار خون بالا مواجه می‌شوند و یک ساعت و ۲۷ دقیقه خواب اضافه با بیشترین میزان کاهش احتمال فشار خون بالا همراه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/686072" target="_blank">📅 08:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686071">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📷
عکس یادگاری سران کشورهای عضو سازمان همکاری شانگهای
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/686071" target="_blank">📅 08:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686070">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdsRSZp6SNPMlBTtVt9uz9dQAH7pyphYIeLICB3C00BRAg0wYYaitZ3l6g4nP5qZvUhzy0urA0_nY6z7YO9hk3_B0CXQaq63YPjbger0LTjQDDxBwxS9oraOa2I5MCB3XSRhAQk5c910KKaoCEi4HQ8wH4eTxTsxDhLHMNLHMYAPLk_uMSsMhv-pvIa3voEPcDesFCtrtI4TnfTBn_ABc13flPafD6-KyQibuL1YVboCEmmMAbeA_FOjgBTgDv854BWPEooKqElI25BVHzLQSg5f7X4e0Uo4tIEYZ7waLr-4RM_j4k7-3ndvPGeoOSB6DEXNcjCWxRuLKC1FMS6uOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس یادگاری سران کشورهای عضو سازمان همکاری شانگهای
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/686070" target="_blank">📅 08:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686069">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607c16eea6.mp4?token=VHMn8xrNwktkFd6ZwxjR0_Vpshc9aSp8DCBrdLySp89L8kM7eWgY2mO3ugIQyCQDk1wgp8IPQoRdG1w--QR-doryh6nQ4XRNbbZaRF6-CBmsRsIMdl4gvco1ax_YSsvUOgViYh7hKlkwAHdkoqjS7LN7JEbKqR9_Q56aL-LAv5FsXmsFvRUbyyekvC4pru7013QZDqPtmjGd31a04SOUlfJG6tJpaNN-jV2qOF1_0pnSMh0-4K0fCBI4FMQBkZG2LDNT_ZQQzRn9rCrPWoqe58KFpOjFo5HSazJ2NMh866t4rsHxRMltvlw7eW6mt-SRilkG2TveSvZfhAEH54jQfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607c16eea6.mp4?token=VHMn8xrNwktkFd6ZwxjR0_Vpshc9aSp8DCBrdLySp89L8kM7eWgY2mO3ugIQyCQDk1wgp8IPQoRdG1w--QR-doryh6nQ4XRNbbZaRF6-CBmsRsIMdl4gvco1ax_YSsvUOgViYh7hKlkwAHdkoqjS7LN7JEbKqR9_Q56aL-LAv5FsXmsFvRUbyyekvC4pru7013QZDqPtmjGd31a04SOUlfJG6tJpaNN-jV2qOF1_0pnSMh0-4K0fCBI4FMQBkZG2LDNT_ZQQzRn9rCrPWoqe58KFpOjFo5HSazJ2NMh866t4rsHxRMltvlw7eW6mt-SRilkG2TveSvZfhAEH54jQfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواشناسی: بارش‌ها در شمال کشور تا پایان هفته ادامه دارد
🔹
از روز جمعه مجددا دما در شمال کشور افزایش می‌یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/686069" target="_blank">📅 08:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686068">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فردا؛ آخرین مهلت انتخاب رشته کارشناسی ارشد ۱۴۰۵
🔹
فرانس۲۴: جنگ ایران تاکنون حدود ۱۱۰۰ دلار برای هر مالیات‌دهنده آمریکایی هزینه داشته است.
🔹
تلگراف: اوکراین آمار تلفات رسمی ارتش خود را کمتر از واقعیت اعلام می‌کند.
🔹
آمریکا: توافق با روسیه تا حل بحران اوکراین ممکن نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/686068" target="_blank">📅 08:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686067">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
آموزش‌وپرورش: امکان ترمیم نمرهٔ امتحان نهایی در شهریور وجود ندارد
🔹
با وجود درخواست برخی از داوطلبان کنکور برای برگزاری امتحانات نهایی شهریور ۱۴۰۵ با هدف ترمیم نمره و ایجاد سابقهٔ تحصیلی، سخنگوی آموزش‌وپرورش می‌گوید: ترمیم نمره «خرداد به خرداد» انجام می‌شود و ایجاد فرصت مجدد خارج از زمان مقرر، نیازمند تصمیم و تغییر در ضوابط مربوط است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/686067" target="_blank">📅 08:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686065">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a46c4d05a.mp4?token=uy0_aQyFTRWT112J8DMvfDtpUI2VTes2-vcheggNNol95oWCLw1tu1wI90AEQO28n9QmVJ2cFCnL11utf4w_N1NuwTbo_RghwKmUrIFooQNwiSHPrthzup4Yi4UWYC4Cw_EEnWc22W7-YRaBBofIYWcwqhJVEEuodwonyKGujtv3b6WFLF2NySoULt9dwlGrk_oPwt1S1hH9d9YPspx1GsPkb8P3RfyBd7Nq8Dddp4wR3NNx7IJQAYSiArN61gNNkA8cr2EhMiidCVX3iV_IoDxAWiwFGOq3d5lY42DfkVokSs0Sr7_nSnghsL1mkM95ZmEJbF6ZgEcJrunufjAC9aBz0cgTSaOOFEvu8XingpHV0q3ouK-eb0Z8Qddj2StBod8tBEquzVkNGOStYnZ9iWVm0-S2wuMQ-oTDKSFJ_G02pF5erSrGJuz2-vMByt0W9-FwFTihL4MPLNQ4W4b3qH-xnjL6Te1dwwy4EQI6fMSIYwe2P7ynDM6ZjKN5dUU1Qp2jHHfIx23SaZDHEV-pU_DvgqBMKMihE4QuWBQktaQ0AnSos_12ds85qjmG0tBDK2DbJwuRSmH--gcJZJAdvru68eNGmi0UYTQjx9yPMElIWvcnQvPAOrDCbgRAik6aOdnGi8fzZvRj-rQw40dBdvhg07SjI8Kg7VUrGnuwFUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a46c4d05a.mp4?token=uy0_aQyFTRWT112J8DMvfDtpUI2VTes2-vcheggNNol95oWCLw1tu1wI90AEQO28n9QmVJ2cFCnL11utf4w_N1NuwTbo_RghwKmUrIFooQNwiSHPrthzup4Yi4UWYC4Cw_EEnWc22W7-YRaBBofIYWcwqhJVEEuodwonyKGujtv3b6WFLF2NySoULt9dwlGrk_oPwt1S1hH9d9YPspx1GsPkb8P3RfyBd7Nq8Dddp4wR3NNx7IJQAYSiArN61gNNkA8cr2EhMiidCVX3iV_IoDxAWiwFGOq3d5lY42DfkVokSs0Sr7_nSnghsL1mkM95ZmEJbF6ZgEcJrunufjAC9aBz0cgTSaOOFEvu8XingpHV0q3ouK-eb0Z8Qddj2StBod8tBEquzVkNGOStYnZ9iWVm0-S2wuMQ-oTDKSFJ_G02pF5erSrGJuz2-vMByt0W9-FwFTihL4MPLNQ4W4b3qH-xnjL6Te1dwwy4EQI6fMSIYwe2P7ynDM6ZjKN5dUU1Qp2jHHfIx23SaZDHEV-pU_DvgqBMKMihE4QuWBQktaQ0AnSos_12ds85qjmG0tBDK2DbJwuRSmH--gcJZJAdvru68eNGmi0UYTQjx9yPMElIWvcnQvPAOrDCbgRAik6aOdnGi8fzZvRj-rQw40dBdvhg07SjI8Kg7VUrGnuwFUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ تلاش می‌کند تبعات جنگ برای آمریکا را کم‌اهمیت جلوه دهد
🔹
نیک ماترن، عضو پیشین نیروی دریایی آمریکا در گفت‌وگو با پرس‌تی‌وی، جنگ آمریکا و رژیم صهیونیستی علیه ایران را غیرقانونی می‌داند و معتقد است این درگیری‌، پیامدهای اقتصادی سنگینی برای جهان به دنبال خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/686065" target="_blank">📅 08:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686064">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34133a21b6.mp4?token=ex0d4FIl9r3uAEtK7ZmXeSd-KzFcAf3nVnYDjwicuC_TiHnMDDrzjazU76tAmNytAtUW5ZFD3wqYnxw5rEY0tSNBv8DVwv3VcyQh7gxH_ofOTNsorxnZCsl7EksgGxbbztD3CD7FTsDZU6qnE3hgcU3lJLlivhFSXjFmlQJFK16FKIW3omR34Y5TT5hmC8ENwzNcgc9hGGSMaaSnpcP80d9q9hZFXMDBtPZU-uKlJWwYbgk_T9Wk5JQFM8qkgRtN7KFfUW1Ce8_uhXE95MYwAxfAc5fk0zjtIty88tG2iPNe92ri-qGx8hN7bsfnfRmthNySZD5PG9ou9bM9EbhRsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34133a21b6.mp4?token=ex0d4FIl9r3uAEtK7ZmXeSd-KzFcAf3nVnYDjwicuC_TiHnMDDrzjazU76tAmNytAtUW5ZFD3wqYnxw5rEY0tSNBv8DVwv3VcyQh7gxH_ofOTNsorxnZCsl7EksgGxbbztD3CD7FTsDZU6qnE3hgcU3lJLlivhFSXjFmlQJFK16FKIW3omR34Y5TT5hmC8ENwzNcgc9hGGSMaaSnpcP80d9q9hZFXMDBtPZU-uKlJWwYbgk_T9Wk5JQFM8qkgRtN7KFfUW1Ce8_uhXE95MYwAxfAc5fk0zjtIty88tG2iPNe92ri-qGx8hN7bsfnfRmthNySZD5PG9ou9bM9EbhRsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاری شدن سیلاب در ایالت یوتا آمریکا
🔹
بارش شدید و کوتاه‌مدت باران در پارک ملی زایون در ایالت یوتا باعث جاری شدن حجم زیادی از آب و گل از دامنه‌های سنگی به سمت جاده اصلی شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/686064" target="_blank">📅 08:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686063">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52eec2cc0c.mp4?token=FvXGcqcZCIsBYm6YSQGM4B82CXSvAoHXaxXgcEQTbln7JbCrmBYB7EfSzhwqUSX6uhQ18HwsEXqaNF9XCJnt0el7X8GNeRccOxZJD9zWBMZhSdtqZd9ofK4TGg45ANyYrTpUoagPJy4f9LFF1X-ZC5zL9WBTUaXq7OccCT-xEbH-8B4G2pQelnJkKBrQalyosAOhzl5gaFXuzyOjMpr6NmIpbV7o5PLbMeYtQ8z23cUsO1Hgt3XASXAkOs6_Wb4l7Y5DugX_vo6FncWt-CenZjx9ihDN4tVuAwzFd3nGnFzmNcd1xfU06V9BTiywDdsnK8HDArv9nvkjzzjj8lysuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52eec2cc0c.mp4?token=FvXGcqcZCIsBYm6YSQGM4B82CXSvAoHXaxXgcEQTbln7JbCrmBYB7EfSzhwqUSX6uhQ18HwsEXqaNF9XCJnt0el7X8GNeRccOxZJD9zWBMZhSdtqZd9ofK4TGg45ANyYrTpUoagPJy4f9LFF1X-ZC5zL9WBTUaXq7OccCT-xEbH-8B4G2pQelnJkKBrQalyosAOhzl5gaFXuzyOjMpr6NmIpbV7o5PLbMeYtQ8z23cUsO1Hgt3XASXAkOs6_Wb4l7Y5DugX_vo6FncWt-CenZjx9ihDN4tVuAwzFd3nGnFzmNcd1xfU06V9BTiywDdsnK8HDArv9nvkjzzjj8lysuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش چند حرکت کششی کاربردی که می‌تونه در برنامه تمرینی روزانه قرار بگیره #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/686063" target="_blank">📅 08:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686062">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmiQLjwKmztcR6hNHrEvAwlraIk8iO4pbNIuBhmsJi1OaybpEP8g8d18C85Un5b1t_oAGX9E7ISN0tTHQ50SD0K69CIrzheDNlZ2tlggygCrhvt5V_aqhObpUspfld6AvCjzPdPZTTBLh0cYzK5ocHpPvkpCdBQsZY1KjVmnKzBxJqDzPhOsVIsYnZ8o6v1FAeC3mzcyU5pClWWA_RUC7wdmC9wk4pbAk2glLre6L8WmoTi36WeK-cSq-In4kuK8BSvh7iwhmAwTK2jwLcAUgewC_gBYL8SExNQ_I9xLwcSdFj9Ef8_X8lJp2UFn6O8-FdcO09Za0c9IjrYSjD8QIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار وزرای امور خارجۀ ایران با وزرای چین و پاکستان در بیشکک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/686062" target="_blank">📅 07:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686061">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
بیشترین قاچاق سوخت در ۶ استان کشور
رئیس پلیس امنیت اقتصادی فراجا
:
🔹
بیشترین موارد قاچاق سوخت در استان‌های سیستان‌وبلوچستان، هرمزگان، بوشهر و خوزستان و به طور کلی در مناطق شرق، جنوب شرق و استان‌های مرزی مشاهده می‌شود.
🔹
پس از این مناطق، در برخی استان‌های غربی از جمله کردستان و کرمانشاه نیز با موارد قاچاق سوخت مواجه هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/686061" target="_blank">📅 07:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686060">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
قصد فرار ترامپ جنایتکار به پنج طبقه زیر زمین به بهانه ساخت سالن رقص   ترامپ:
🔹
در این سالن رقص تا حد زیادی یک بخش نظامی هم محسوب می‌شود؛ با پهپادها، پناهگاه‌های بمب و همه چیز دیگری که در آنجا داریم.
🔹
این سازه تا پنج طبقه زیر زمین امتداد دارد. می‌دانید، تقریباً…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/686060" target="_blank">📅 07:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686059">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرانسه رئیس دوره‌ای شورای امنیت سازمان ملل شد.
🔹
واتسون کولمن، نماینده دموکرات: مردم آمریکا خواستار پایان جنگ علیه ایران هستند.
🔹
آمریکا از موافقت با فروش بالگردهای نظامی به عراق به ارزش ۸۰۰ میلیون دلار خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/686059" target="_blank">📅 07:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686058">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVuK1Vxxo_JBQC1aLLC1yXckDTomaPHaBrkFm8sWjDTlB5YmvrpkS3DrmDvhdDWHEjbn_L_yA1IXlpWUvXWkQudJPA5E_65w_cdoIx6F_6A6RoFzXB7ETOfrMewtXxVYGWUii1pgj8AjyyMHSeS4LuQ_h6xNqBtyd33xRL5OlBxAvWs75v9gXngzHln0S3TaV_Svtbpt2J7Mrsq2AVjzx6bcDl_EDq0YY8p6AX25yFe9yWjBHNiHFBal5fn3OKGnkNWbIIatLGpLoZ3T4XQ6MHkBpFNq2CxJeXLi3jMoW-iG10iA_-MBqg52UnpaoVI3tnkz6J0OWpkYHzQou82VfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محبوبیت ترامپ در آمریکا همچنان در سراشیبی سقوط
🔹
نظرسنجی جدید مشترک خبرگزاری «رویترز» و مؤسسه «ایپسوس» نشان می‌دهد که فقط ۳۳ درصد از آمریکایی‌ها عملکرد ترامپ را تایید می‌کنند ولی اکثر مردم از جنگ ایران و هزینه‌های زندگی مستأصل و ناراضی هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/686058" target="_blank">📅 07:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686057">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
روسیه: پوتین ۱۰ شهریور با پزشکیان دیدار می‌کند
🔹
دستیار رئیس‌جمهور روسیه روز جمعه اعلام کرد که «ولادیمیر پوتین» رئیس‌جمهور روسیه قرار است در تاریخ ۱ سپتامبر (۱۰ شهریورماه) با «مسعود پزشکیان» رئیس‌جمهور ایران دیدار داشته باشد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/686057" target="_blank">📅 07:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686056">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qekj5zJ2WqxAHp5_Wxu6ZZn9NXyqnt84tsj0iH3YQ31SBJ0axjMrrfilGTXqxd9VDBtA9beqHHPRA4V8V0TsQ27ZP0gP4D8y0PGrMwoGVAno7Qr8v852urZ0xf1x_Ijf-cUFibQDNp7sbARbeYu1Buut1AUwMtqtmDCH4GF3ZA52850yCKmEduJnS5wsA7x9vV-qdEVv__IzeYoKeCLGvQohqkhIElORCq-ND4lrz-RyGO_TOdkowXVF6yfUMkpN3QVfWWwQlRPNDPkUfSRmK1SI0yIicOYyB4qlSiF_x6wYlIDugEZe9PdSX20z3bF84BqsMl2lzsbEN6mGPIWXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۰ شهریور ماه
۱۹ ربیع‌الأول ‌۱۴۴۸
۱ سپتامبر۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/686056" target="_blank">📅 07:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686055">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعاهای ونس درباره توجیه تجاوز آمریکا به جزیره لارک
جی دی ونس معاون رئیس جمهوری آمریکا با تکرار ادعاهای واشنگتن درباره تنگه هرمز و در توجیه تجاوز شب گذشته به جزیره لارک ایران، مدعی شد:
🔹
هدف ما تضمین جریان آزاد تجارت در تنگه هرمز است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/686055" target="_blank">📅 04:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686054">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ارتش و نیروهای مسلح یمن بامداد سه‌شنبه پایگاه‌های مزدوران سعودی و اماراتی در جنوب غربی این کشور را هدف قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/686054" target="_blank">📅 03:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686053">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حمله موشکی روسیه به کی‌یف پایتخت اوکراین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/686053" target="_blank">📅 03:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686052">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نامه ایران به شورای امنیت در پی تجاوز جدید آمریکا به جزیره لارک
سفیر و کاردار نمایندگی جمهوری اسلامی ایران نزد سازمان ملل:
🔹
این اقدام تجاوزکارانه، نقض آشکار حاکمیت و تمامیت ارضی و نقض آشکار بند ۴ ماده ۲ منشور سازمان ملل متحد است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/686052" target="_blank">📅 02:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686051">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayoXbfAb35_oscPGwMOPsE_OwMc8POHwezEVphX3CI87R5WXxYN2cmj7uebMyiBIYaKhGNWrOmrvAxPI43o8Erejp2NK4M4h1Y1_ZPYPyEMoQn1TtRImPWZGlDKV1DHBUQG-dHaRVPVAETivS5jfjSq1sk7DGgCo9o9cODXGZxdWX7pdhEqYsEvGLtYT8KHdq0tkPDDUs_7KaYy3Ar-m--63CDz94H1SFz3nIn03UyCWUHZq6o3zN1LXhS1MG1W672UWQndaAPGIif05rLguAPBYrzHKHtAR3pPtf2dvfqDBT-INhNs4SD3dyr9Ghv_kyoJkkOXhgDCmlwTbhfAwZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک نفتکش عربستانی در کریدور جنوبی تنکۀ هرمز متوقف شد
🔹
نفتکش عربستانی غول‌پیکر با نام سیدر، در حین گذر از کریدور جنوبی تنگۀ هرمز متوقف شد.
🔹
ساعتی قبل UKMTO از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش خبر داد.
🔹
نفتکش سیدر قابلیت حمل ۲ میلیون بشکه…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/686051" target="_blank">📅 02:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686050">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
فاکس نیوز: درباره جنگ با ایران چه چیزی یاد گرفته‌اید؟
ادعای جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
♦️
«آنها حاضرند برای رسیدن به هدفشان دست به هر کاری بزنند و فکر نمی‌کنم پشت این اقدامات، حکمت و دوراندیشی راهبردی چندانی وجود داشته باشد؛ هدفشان این است که جریان نفت و گاز را تا حد ممکن کاهش دهند.»/انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/686050" target="_blank">📅 02:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686049">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره ایران: «دیشب حملاتی انجام شد. ما در پاسخ به ایرانی‌ها اقدام کردیم؛ آنها در آستانه مین‌گذاری بودند
🔹
ما اکنون در مرحله‌ای هستیم که بخش قابل‌توجهی از اقدامات ما در واقع با هدف تضمین جریان آزاد تجارت در تنگه هرمز انجام می‌شود.»/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/686049" target="_blank">📅 02:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686048">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP1a5X6MPq7izmDGqWHotr4lrsQ68LE19RxNxT5wsOwHTx96gHe-XbBp9fLT9i3Sf3LppGGwNbg_AZ9K5mx6VlzLhH0s3-0Pb1_NkYCgvQyREM79locgnPEw4-IfAOosZxj6niBTz7Zas3nj4cY_OfbpY6qkSLyBiRzLolSHgjB7xRqSxcBF4KgHdnVpsO-A2osdHjbIJ8YDVzvKusPjIiwUIugBxAbone8WOAOKLjQ7tojTVm3PP0UcfY_fuOQLC0cIrJ8W2521mieK2zWzximLjPVM5U1p1hveEn2cRAibaXZ1EWg5UE4nmWvNDvrApCYtGhXigUw9iH_m5KFFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر جنگ آمریکا استعفا داد
🔹
سی‌ان‌ان استعفای «دنیل دریسکول» معاون وزیر جنگ آمریکا در امور ارتش، بعد از ماه‌ها اختلاف با رئیس پنتاگون خبر داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/686048" target="_blank">📅 01:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686047">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
انفجار مین حین عملیات اطفای آتش در منطقۀ حفاظت‌شدۀ بوزین و مرخیل
فرماندار پاوه:
🔹
در جریان عملیات اطفای آتش در منطقۀ حفاظت‌شدۀ بوزین و مرخیل، یک مین در محدودۀ مرزی منطقه منفجر شد که بر اثر آن یکی از فعالان محیط‌زیست حاضر در عملیات مصدوم شد.
🔹
آتش‌سوزی در این منطقۀ حفاظت‌شده ظهر ۸ شهریورماه آغاز شد و عملیات اطفای آتش همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/686047" target="_blank">📅 01:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686046">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b7ac2b46.mp4?token=ttHccm9LKLqaIwespLJoBEauIASRmxL-D3k9ZXMabDypszMRG0O94KE73_wnYXdALRQdAD2acAceLoDf8tjueeQbbcHwOa0joTUbttMMdBbIhrQK65bfP5J_e8vn6lq5VmL0aAWb7nrs1HGHLynaBLDZTCAP45G89vcsH0YzyvOnkAAmldBkbUTwUUEBrJux8u1COLcLfkglorvq6ToJd_un2BvGP3cY-4dm7N1N8T-0foLvLohWLSTUvj7rcFntlipl4nSotw0ydo50jvCFcbut1NtufeO3Kw8g0dRirwFEuWZtzQ988cOwNKYN_XJu7n7Dy2zlqlinu5nQMJwj0L20QkaeKUvT5oRBnVyfwBYUbfBdmRvzFxCCc3IP-0BGQXZLbT_QecKq5RGtK7M0IcaKlIZIdcMsCwS1dsIHDkpGtmehygCvkRC_VzFcivsn2QVU7-7ODJvGOvzQCk2-fGyxNUPj9KIm6WyWIM8uo48itV-DkC9guEhBWuKd-IQ5qcppcChWadAdZUHYQDd1RB4KwsO8j2kuTbofwQEsb4Zcoiy2TpZJoK-9yv787z0dxTDrDKi1MFafdzDGGP62mri9MpAX8A2ExhllpqlyrEhv2qHbmgQQadRrXeBQLFcbJ5jbxRzFkS1qUeKEry6FryBaFcmyYBWNSLFzrl-UouA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b7ac2b46.mp4?token=ttHccm9LKLqaIwespLJoBEauIASRmxL-D3k9ZXMabDypszMRG0O94KE73_wnYXdALRQdAD2acAceLoDf8tjueeQbbcHwOa0joTUbttMMdBbIhrQK65bfP5J_e8vn6lq5VmL0aAWb7nrs1HGHLynaBLDZTCAP45G89vcsH0YzyvOnkAAmldBkbUTwUUEBrJux8u1COLcLfkglorvq6ToJd_un2BvGP3cY-4dm7N1N8T-0foLvLohWLSTUvj7rcFntlipl4nSotw0ydo50jvCFcbut1NtufeO3Kw8g0dRirwFEuWZtzQ988cOwNKYN_XJu7n7Dy2zlqlinu5nQMJwj0L20QkaeKUvT5oRBnVyfwBYUbfBdmRvzFxCCc3IP-0BGQXZLbT_QecKq5RGtK7M0IcaKlIZIdcMsCwS1dsIHDkpGtmehygCvkRC_VzFcivsn2QVU7-7ODJvGOvzQCk2-fGyxNUPj9KIm6WyWIM8uo48itV-DkC9guEhBWuKd-IQ5qcppcChWadAdZUHYQDd1RB4KwsO8j2kuTbofwQEsb4Zcoiy2TpZJoK-9yv787z0dxTDrDKi1MFafdzDGGP62mri9MpAX8A2ExhllpqlyrEhv2qHbmgQQadRrXeBQLFcbJ5jbxRzFkS1qUeKEry6FryBaFcmyYBWNSLFzrl-UouA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از اوضاع دردناک کودکان نوار غزه در سایه ادامه محاصره ظالمانه این منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/686046" target="_blank">📅 00:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686045">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ترامپ در اظهاراتی متوهمانه: ایران قلدرخاورمیانه بود؛ من بدنبال پر کردن ذخایر استراتژیک هستم
🔹
ما مجبور بودیم وارد ایران بشویم و مطمئن شویم سلاح هسته ای ندارند.
🔹
جنگ با ایران سخت نیست و بدنبال جبران ذخایر هستم. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/686045" target="_blank">📅 00:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686044">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
هدف قرار گرفتن یک فروند کشتی در نزدیکی سواحل عمان
🔹
یک کشتی در آب‌های ساحلی عمان، در تنگه هرمز، در حین تلاش برای عبور از این تنگه، دچار حادثه دریایی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/686044" target="_blank">📅 00:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686042">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cede7dbb3e.mp4?token=mj47TwRt3BSM50xojbjGS5tQHTCuaeNyxdekbSkM-FFMtZl9_bGnL9dcqieE9r0ZgM8_SP9vDWBcjQjmXHTi6ZH9UhfDnLETJd5dcv8DyvxNSwA7j-1jNedV3HjKZyaV3ZDTwIDmanR4O1i2XTtyFiyFsQsDTMcPFk5tHtuvnNCYZ42u8FK8_08DqRvOrMqQB3LIaHXyVYkQcmEfrstFPJ6TZZB2_ihEBQFLKP2X15k_15H2VQmNOUH7lAlDN4yVtFVs6f_AH_sDjSZYUhKbECGSAKaA8GlZOerKX6wzC7Kn2_UEZulo1-Wckm3CCu1zR23RGbd0pLIgK3cngRTQEDLIBMZNnJuW428G7hMvofKwyvq2x0MqD-U32AQs6tXHsqurkY5-UnbqsFrWk8We-5oIqKTYRl_olDYACYQlE3trKPN01OqbVX7LemKpLn-6XzNaKvK1Pk1lBQ7fQCdiQrHSo1P-9_DIXEsS47kSKA8YrATmWL7CiGaCKDW6ov1Eba-VEa3BqSFJvm-y7NzNNDyaXECVTSqHmE1t4BvLQY05C57yY1s45tzRijKNSgNGYOmOqnuuS6qoF6sZJBtwHw1PLLELXwED0YsLhK1jqcAfEGc_LDD2J0k-Q9vXkYpJpcmIpao4If2e2N2QB9DspKRHogvl5NHwdA_-YAUqKuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cede7dbb3e.mp4?token=mj47TwRt3BSM50xojbjGS5tQHTCuaeNyxdekbSkM-FFMtZl9_bGnL9dcqieE9r0ZgM8_SP9vDWBcjQjmXHTi6ZH9UhfDnLETJd5dcv8DyvxNSwA7j-1jNedV3HjKZyaV3ZDTwIDmanR4O1i2XTtyFiyFsQsDTMcPFk5tHtuvnNCYZ42u8FK8_08DqRvOrMqQB3LIaHXyVYkQcmEfrstFPJ6TZZB2_ihEBQFLKP2X15k_15H2VQmNOUH7lAlDN4yVtFVs6f_AH_sDjSZYUhKbECGSAKaA8GlZOerKX6wzC7Kn2_UEZulo1-Wckm3CCu1zR23RGbd0pLIgK3cngRTQEDLIBMZNnJuW428G7hMvofKwyvq2x0MqD-U32AQs6tXHsqurkY5-UnbqsFrWk8We-5oIqKTYRl_olDYACYQlE3trKPN01OqbVX7LemKpLn-6XzNaKvK1Pk1lBQ7fQCdiQrHSo1P-9_DIXEsS47kSKA8YrATmWL7CiGaCKDW6ov1Eba-VEa3BqSFJvm-y7NzNNDyaXECVTSqHmE1t4BvLQY05C57yY1s45tzRijKNSgNGYOmOqnuuS6qoF6sZJBtwHw1PLLELXwED0YsLhK1jqcAfEGc_LDD2J0k-Q9vXkYpJpcmIpao4If2e2N2QB9DspKRHogvl5NHwdA_-YAUqKuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✂️
ماشین اصلاح GYT-999
✅
صفرزن و خط‌زن | تیغه استیل
🔋
شارژ Type-C |  تا ۴ ساعت استفاده
📊
نمایشگر شارژ + ۴ شانه اصلاح
🔥
فقط ۱,۳۹۸,۰۰۰ تومان
💰
قیمت قبلی:
۱,۶۹۸,۰۰۰
✅
پرداخت درب منزل | ضمانت تعویض ۳ روزه
خرید از سایت
👇
https://memarket24.ir/product/brief/47608/180124/
✨
تخفیف آخر ماه؛ فرصت آخر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/686042" target="_blank">📅 00:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686041">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
عملیات نیروهای مسلح یمن علیه مزدوران عربستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/686041" target="_blank">📅 00:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686040">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac8097603.mp4?token=KFsZVbEAsUQr5Sx46Fkec2kl_27NFs5laZ4QHy0rCxCZekiGAaWyoEWMGuRUJCJ_j-h4MKXTlAI1X1S71Yyq4REHoFfeYTvgvI8rOe3AB_twdl6NvLLnQS7a120D6uNMJrEPawNZZpfCK0aWid2bS9FQWYhtVzZhQeItPlCPZ-m_GEoZec7CAZC3Q044oPyc7IdUvrArdKQ9rEzbs2bwU3ZlWWGfj_s1QHRm1ASyr4gpt-Rozl9vtdPdygx1974bofSbDh1dt5G1qJhnrl0YYrFjy4RN7tKivOAMRu2thPzRahisXizVFUrd5OdMUuFrVIgU2KkcW1OghuwZRE1J3CLHoZP5LlISaRkSuM1z-83BNs05AwTrzqXlF1LfHB1EheH6r7HmZctDVBhrBlbd3gDW_ykY0v0q7lU_0a3vqmCjMtmQ7MpZFBG2t-laNhOnFqkFG_chBX6pi85aKWhB6v-eYUW7FT43yap-dZZh4ihvXpUCq4WsTy_RKTAhdKqyyTLathkWkU7dfGCsmJ8Qkwb4qMorcBtZ0imudYnXzn-qDk2fCMomnW2DwmQtCgFoRpouDnbBDlnMixJDrnbUw5iP6S2Pwp8ik1ds48sebWHz-dBNyJcVIu6_gZt0PxYjRzYT5Hk0WoXSfvx7zt2qUtw-qxHl2-4VEr2L9b3jstk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac8097603.mp4?token=KFsZVbEAsUQr5Sx46Fkec2kl_27NFs5laZ4QHy0rCxCZekiGAaWyoEWMGuRUJCJ_j-h4MKXTlAI1X1S71Yyq4REHoFfeYTvgvI8rOe3AB_twdl6NvLLnQS7a120D6uNMJrEPawNZZpfCK0aWid2bS9FQWYhtVzZhQeItPlCPZ-m_GEoZec7CAZC3Q044oPyc7IdUvrArdKQ9rEzbs2bwU3ZlWWGfj_s1QHRm1ASyr4gpt-Rozl9vtdPdygx1974bofSbDh1dt5G1qJhnrl0YYrFjy4RN7tKivOAMRu2thPzRahisXizVFUrd5OdMUuFrVIgU2KkcW1OghuwZRE1J3CLHoZP5LlISaRkSuM1z-83BNs05AwTrzqXlF1LfHB1EheH6r7HmZctDVBhrBlbd3gDW_ykY0v0q7lU_0a3vqmCjMtmQ7MpZFBG2t-laNhOnFqkFG_chBX6pi85aKWhB6v-eYUW7FT43yap-dZZh4ihvXpUCq4WsTy_RKTAhdKqyyTLathkWkU7dfGCsmJ8Qkwb4qMorcBtZ0imudYnXzn-qDk2fCMomnW2DwmQtCgFoRpouDnbBDlnMixJDrnbUw5iP6S2Pwp8ik1ds48sebWHz-dBNyJcVIu6_gZt0PxYjRzYT5Hk0WoXSfvx7zt2qUtw-qxHl2-4VEr2L9b3jstk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به راستی شهید قاسم سلیمانی کیست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/686040" target="_blank">📅 00:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686039">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">افتتاح نمایشگاه
#الکامپ
، رییس سازمان نظام صنفی رایانه ای: امید آفرینی یکی از اهداف این نمایشگاه است. از استقبال روز اول راضی هستیم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/686039" target="_blank">📅 00:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7UTdbjjtzdEfe7GWbjrvLpX5VM_HXI4Q_-fR4CSt0LkQy5CoQMAH7NEhc7GUxL4-IxwZrj2edWyQjLUL1NnGSbBfU2L8olRb8nrhu0j0a7HLQSyZB2WENUzzQusNNLKGL9Wy1B9LpSrBH9g11p-uKN4uPMjiJSI4vc1TfkCnxEc3NESI6VPBSYwh3vuAsatdri9ircYRSTLTXe-b36VSh5Yyj56EA-ek_Cbd6J78W0V1NlTdL6owCd10NDfI_CYbqGfIv-h-QEIGZfGRP-JYu5AvU1Hcw3D8ZeZvCeOjsq8pTLs50N0tITOF7lem-u2a9MmkzAVhN5i822r9cXGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/686038" target="_blank">📅 00:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686037">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUiyL7Rz1IYuFJqpWFEcfH62y5vsWu98A-ngal3utIrzCpgjfaf5X8Xur6Eu_Qf6N5mfCCBFZTBKfhMGkgiQWAfH-ujs6Rd-QJU7npTe-8-yj2kdQD9rTfW59CZwH7mnXugj9ougkRTRfpYUibkZDZ1zPrzEpaVNTWvPGfaPbCp9LPJwXZDvAO8rTYM4FFxxiYz3dxk1Xn2OJPAXUlToGH6Z2ffp8aaaaHaS0VOlKh5b7LTTo-UkRrnwj_lD9do4TRR4bH2-MzZA78usOlFPLubs0-FH213ZfNCM0syRiKIlWXxZ2x0KMOxoftFrROV8Ta4omQhB5Rb5K7FL_dXkLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمایی سریع برای اتو کردن پارچه های مختلف
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/686037" target="_blank">📅 00:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686036">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
رایتل در مسیر اپراتور صنعت و دولت هوشمند
🔹
دکتر مهدی فقیهی، مدیرعامل رایتل، در حاشیه الکامپ از حرکت این اپراتور به سمت خدمات تخصصی صنعت و دولت هوشمند خبر داد.
🔹
رونمایی از eSIM عمومی و صنعتی
🔹
همکاری با فولاد مبارکه در حوزه 5G خصوصی
🔹
رونمایی از دوقلوی دیجیتال و سیم‌کارت گیم
🔹
توسعه خدمات سلامت الکترونیک
🔹
فقیهی همچنین گفت: قیمت اینترنت در ایران بسیار پایین‌تر از قیمت‌های منطقه‌ای است و اپراتورها با وجود افزایش هزینه تجهیزات، امکان افزایش متناسب قیمت‌ها را ندارند.
▫️
مشروح خبر
khabarfoori.com/fa/tiny/news-3241824</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/686036" target="_blank">📅 23:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686035">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R36jWpvd1z9PrcCWwRxt0sR6GwPizhqntAm_w6xzjkQ_f50xrV4rGgOJcFpbqrh7E4h3vep6Wf3SvuWkTtq9Cl3zzKIBSaAL5EYxa4lHQ_r1WiuIs9X0eJ4P9hiM-TLF7GvFDNMDNrU0yg-l7Z04JmInnRIn5Z-p17F8P8hiz5V0pajzp9h0R89ptUiNWdvDFWxRhmB7A4cHxX8n3YL2cJrjzyMDEEDIrkLTZpNd4As7gQPZ2tikN-nuUeh3pol6gt7g_J1X6TUblZOuBQR_HYysMRNb6f1lJGhJxOO0Yb8tlVTXAyS1yQhpxdEYoVIV_iwFe9UinoL6YiokKLx8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت به عصر «تاناکورا» | رونق بازار خرید و فروش کالاهای دست دوم در ایران | بازارهای پُر و جیب‌های خالی!
🔹
این روزها ترافیک سنگین پلتفرم‌های واسطه‌گری و شلوغی راسته‌های کهنه‌فروشی، نمایشی فریبنده از یک «رونق دروغین» به راه انداخته است؛ رونقی که پشت ویترین پرزرق‌وبرق اصطلاحات شیک مانند «اقتصاد چرخشی» و «فرهنگ بازیافت»، حقیقتی تلخ و گزنده را پنهان می‌کند: سقوط آزاد قدرت خرید و عقب‌نشینی ناگزیر خانواده‌ها به سنگر کالاهای مستعمل.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3241757</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/686035" target="_blank">📅 23:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686034">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ستاد عملیات دریایی بریتانیا: گزارشی درباره حادثه‌ای شامل یک نفتکش و نیروهای نظامی در اقیانوس هند دریافت کردیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/686034" target="_blank">📅 23:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686033">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
دیدار وزرای دارایی آمریکا و روسیه برای پایان جنگ اوکراین
🔹
رسانه‌های آمریکایی اعلام کردند که «اسکات بسنت» وزیر خزانه‌داری ایالات متحده امروز با «آنتون سیلوانوف» وزیر دارایی روسیه دیدار کرد تا درباره توافق احتمالی برای پایان جنگ در اوکراین گفت‌وگو کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/686033" target="_blank">📅 23:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686032">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChtNNWRXEFKyvlF8_mW4HKXOcWdsMbY1e6zHp0BjHys-lSVYxq01S6yQb5tSSItYuT2SQRFwTuvssUJ4_-EjI4i7asnjvYsr1Gc1OY7vZLtHjM1L9ijyanSSH7xZIBRcp2Un7q47r1oyQ-oKv6_CkfuMZFixwR8vh0wCa5xrQe77Vv-SwVJ8rGOelrFNdBekyh6wEhvtSCFWR9Hdm4Jzxm2tWCd-0P-X2leVYFTBi4xE4YFDdLBWnuBwc-mtWLTrSPFbxzi-XmSVsLx3H6d68Sredua7hYx9fwnIhKFObDKpOu3ZF6Ah7xCRwvFDfot_N0sWJlAaD-Eh8tHzn17Plw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: اروپا دیگر نمی‌تواند از «خودمختاری راهبردی» دم بزند، در حالی که عملاً خود را به مجری اوامر واشنگتن تقلیل داده است
سخنگوی وزارت امور خارجه در واکنش به بیانیه اتحادیه اروپایی در حمایت از جنگ اقتصادی آمریکا علیه ایران نوشت:
🔹
نویسنده فرانسوی، دو لا بوئسی، در رساله‌ای با عنوان «گفتار در باب بندگی اختیاری»، حقیقتی بنیادین درباره زمینه‌سازان استبداد و سلطه بازنمایی می‌کند: سلطه فقط محصول زور نیست بلکه اغلب با تمکین کسانی که توانایی کنش مستقل دارند شکل می‌گیرد.
🔹
اروپا دیگر نمی‌تواند از «خودمختاری راهبردی» دم بزند، در حالی که عملاً خود را به مجری اوامر واشنگتن تقلیل داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/686032" target="_blank">📅 23:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686031">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUnAKKK3BdBq4WJPuOBcjCVq5dqP_pLG4CAUlwBiLs-TW5NHgNvJRoZQ97qrSv1QVaKRz0-F_gjsrn6QkMmMkLBYH7tRiO-mEYDb8RqZrlxTknkmq_IB0Pu5qJlnFGDbPGwwPLv58yT42PbdKyWmupR_ee9kto9M7KWYxoy6GxCpDm4me-90hoVU3sCg9HtEPp2iQLm5RrxElnd3-N0XLEzBvbgef2rL1puuI97jnEvrgEyjEVSjnZ8WDNVtZ8W5I3STqaIwireEZLKcodyHPZ53BwD53FJ7i4qnFdYEEc6nb21sEKlCoiFkc4VPecvkEM9lNAyTwI2wsue5DlY8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف قرار گرفتن یک فروند کشتی در نزدیکی سواحل عمان
🔹
یک کشتی در آب‌های ساحلی عمان، در تنگه هرمز، در حین تلاش برای عبور از این تنگه، دچار حادثه دریایی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/686031" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686030">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
خبرنگار: آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی کرده‌اید؟  ادعای ترامپ متوهم:
🔹
من هرگز چنین چیزی را نمی‌گویم، اما پاسخ بله است.
🔹
هیچ دلیلی برای استفاده از آن وجود ندارد. چه سؤال احمقانه‌ای! آنها کاملاً شکست خورده‌اند.
🔹
من آنها را شکست دادم؛ آن‌وقت…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/686030" target="_blank">📅 23:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686029">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ترامپ درباره احتمال نامزدی هگست در  ۲۰۲۸: صحبت درباره این موضع خیلی زود است   #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/686029" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686028">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d36d4d7fcc.mp4?token=q8nI_OMz470pzEnl-yVjI5htmJa1N1yqiqrpdo4mGO2NTbHpXMJOLt_Sy4cSqCA1RtTPLhV28XGl4SH9P72vEZqcMjGLdP_tMRnB5vLyErDVbGEyUStlCVhwJgpJb2T6-pydV3OVPYnVxJZPNk9lCyTcYrZb6R7aoNCtDtEAuac6Q1ovnkqLtp6cNtRUsE7oDOPNPnXV-gGIXoxfFyIe4Gnf0BAMqEROCI6rpkv3gRK_v8-zLzs16YCcYAKbQkRW1HIvQbffYSuOVd6MIB9DOJVdutaf0BxDrKlB3YYuXU4dqvcqlXnlDr7WfKGTlGruBn5KtkeE4bBVu1DbgoxZqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d36d4d7fcc.mp4?token=q8nI_OMz470pzEnl-yVjI5htmJa1N1yqiqrpdo4mGO2NTbHpXMJOLt_Sy4cSqCA1RtTPLhV28XGl4SH9P72vEZqcMjGLdP_tMRnB5vLyErDVbGEyUStlCVhwJgpJb2T6-pydV3OVPYnVxJZPNk9lCyTcYrZb6R7aoNCtDtEAuac6Q1ovnkqLtp6cNtRUsE7oDOPNPnXV-gGIXoxfFyIe4Gnf0BAMqEROCI6rpkv3gRK_v8-zLzs16YCcYAKbQkRW1HIvQbffYSuOVd6MIB9DOJVdutaf0BxDrKlB3YYuXU4dqvcqlXnlDr7WfKGTlGruBn5KtkeE4bBVu1DbgoxZqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکرار آرزوهای دست‌نیافتنی توسط ترامپ شکست خورده: ما درهای جهنم را به روی ایرانی‌ها باز کردیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/686028" target="_blank">📅 23:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686027">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdWVRs43c8sMPKldYaprs0-y0YDBeyFypGaokK8_5HoZTj-yVeYR7VZPOsw2aycQAojx904yg__aDwXxjqoru549W9ZbHvVITKqw6_coHfngjfnviPzfHVU59CQehDGTCqQtEKBq0l8q6dVam8Is-Jj-k-KPMqbNqorxnF1EZPohmlTtfjE3i9EJ0DCNDvzAFfRkFrqMFNnmPEh4rvnIyOcc4p77P7NQ8HvseTeuSH9ljhvrq0yNcuujlbZpd0bHnRebJQicEUhHS50vG2vS95ZheS1KDAwmKOuhg18QDUCQcZxS67vXg6I57QVuzVRItQrbNmQPbS7HKMSQd6WWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رابرت پیپ، استاد علوم سیاسی دانشگاه شیکاگو: ترامپ اعلام کرده که آمریکا کنترل کامل نفت ونزوئلا را در دست گرفته و این نفت قرار است ذخایر رو به کاهش آمریکا را دوباره پر کند
فقط دو مشکل وجود دارد:
🔹
اول، در بهترین حالت، سال‌ها طول می‌کشد تا این نفت به دست آمریکا برسد.
🔹
دوم، نیروهای آمریکایی باید از پیمانکاران غیرنظامی محافظت کنند؛ وگرنه آنها حاضر نخواهند شد به آنجا بروند.
🔹
پس فعلا روی کاهش قیمت بنزین حساب نکنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/686027" target="_blank">📅 23:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686026">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
اظهارات متوهمانه ترامپ: ما با ایران مذاکرات خوبی داشتم اما آنها رهبر مشخصی ندارند
🔹
چین در رابطه با تنگه هرمز بی‌طرف بوده است. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/686026" target="_blank">📅 23:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686024">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a431a120.mp4?token=i_8daOLM7-_6cmT17ZSHx6pv7-UyVdKSjPqci9c1zd6Nz5mPD0QiJVNQmfN8DoZ4_oLqQPVQrq1MdYmRoyY4CKCGJX2NZ0F6wNqXSDGKrZvMuVS5R0XH_fCc77lKiHcVMQ2h4epflqlClz92gvtY3jJqPXj3iS0W24_ZrpJ5Yq6gLVMxDNTcmGE3JWHRemNl2ABD7iW5NxdfPVc9IbGT39wwi6vtv9FWqiP18l_m5xJExpbHvNMWkMsCeKsTlAn0b26BlIyfIB5y-urIyp9YLYURMRNYRW7fOZ_CW-hMDYGHYDuaOi1hQTzTntHHGAx3cYxsrCPjOos8_mB_DkhskZrsSE4OZjttSAprsFWEB7rCsNjmuI6hJaIBX7qN6SR-iCDIxVuvZtVBGLOETMOPNkyRO_WmoGUG5bHkAAhz0uiu6XJ4xwIJQKt_KGABMNYLPBNoomZVUumE9tFO8e9jihGznV2CHMK7NdWh_ZNtsUVe--EHXVWkt4oe7Mh_Eyc1fKubFOLX-E3WKx67hOf9tiwDNoTscYDmon_SmeJqlRsOsxHIOHLiUQJdxrqgTbh3HoryNxsXJLMb2F8ruloAbgmtna7VZP6h0rl0k7X9X-RSRlOkC57vDMYAULQmn1jq_JRJ6fEsSCDlPBNvA971lt5HMLSvdAsGJOVOBTrxsio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a431a120.mp4?token=i_8daOLM7-_6cmT17ZSHx6pv7-UyVdKSjPqci9c1zd6Nz5mPD0QiJVNQmfN8DoZ4_oLqQPVQrq1MdYmRoyY4CKCGJX2NZ0F6wNqXSDGKrZvMuVS5R0XH_fCc77lKiHcVMQ2h4epflqlClz92gvtY3jJqPXj3iS0W24_ZrpJ5Yq6gLVMxDNTcmGE3JWHRemNl2ABD7iW5NxdfPVc9IbGT39wwi6vtv9FWqiP18l_m5xJExpbHvNMWkMsCeKsTlAn0b26BlIyfIB5y-urIyp9YLYURMRNYRW7fOZ_CW-hMDYGHYDuaOi1hQTzTntHHGAx3cYxsrCPjOos8_mB_DkhskZrsSE4OZjttSAprsFWEB7rCsNjmuI6hJaIBX7qN6SR-iCDIxVuvZtVBGLOETMOPNkyRO_WmoGUG5bHkAAhz0uiu6XJ4xwIJQKt_KGABMNYLPBNoomZVUumE9tFO8e9jihGznV2CHMK7NdWh_ZNtsUVe--EHXVWkt4oe7Mh_Eyc1fKubFOLX-E3WKx67hOf9tiwDNoTscYDmon_SmeJqlRsOsxHIOHLiUQJdxrqgTbh3HoryNxsXJLMb2F8ruloAbgmtna7VZP6h0rl0k7X9X-RSRlOkC57vDMYAULQmn1jq_JRJ6fEsSCDlPBNvA971lt5HMLSvdAsGJOVOBTrxsio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات حریدی‌های مخالف خدمت در ارتش اسرائیل
🔹
حریدی‌های مخالف خدمت در ارتش صهیونیستی عصر امروز در وزودی شهر قدس اشغالی دست به تجمع اعتراضی زدند.
🔹
آن‌ها با اقدامات خود و آشوب، مانع از تردد خودروها شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/686024" target="_blank">📅 23:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686023">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ترامپ متوهم: تنگه هرمز در وضعیت بسیار خوبی قرار دارد
🔹
رئیس‌جمهور آمریکا مدعی شد که تنگه هرمز «در وضعیت بسیار خوبی» قرار دارد و نفت زیادی از آن خارج می‌شود. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/686023" target="_blank">📅 23:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686022">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da02bc0ad8.mp4?token=r4CbFRpOl9G8AoccaSkpvlpDFaaG2VIeRp24t3GDmT6BsY9fq_Vg5gaHtDAmbraTf92etmOMFntRWXaVfcBPG94KjxMfzPgM7YjEq9dOJMloVnuzpLxKmggxl7zgBPxWBiKlnaTTds4SwMsVCItXJsQqUADdjCEXQ0sYeDOintcWUboJMZkb4lwYYWEEY__3ek7-l97vk5LB61wLYSe4rZ0xUF0PlINUf5FtywucMUpiF7afhnCstR5I6TAJEbHSwRDWovRr7YT8u5Q9RDydNlrMqn7vdxMu0jmIvzYViZCedJmJEymtWc3PeJLtGbnuntWE6nOjs5vJ_uOvMWK1Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da02bc0ad8.mp4?token=r4CbFRpOl9G8AoccaSkpvlpDFaaG2VIeRp24t3GDmT6BsY9fq_Vg5gaHtDAmbraTf92etmOMFntRWXaVfcBPG94KjxMfzPgM7YjEq9dOJMloVnuzpLxKmggxl7zgBPxWBiKlnaTTds4SwMsVCItXJsQqUADdjCEXQ0sYeDOintcWUboJMZkb4lwYYWEEY__3ek7-l97vk5LB61wLYSe4rZ0xUF0PlINUf5FtywucMUpiF7afhnCstR5I6TAJEbHSwRDWovRr7YT8u5Q9RDydNlrMqn7vdxMu0jmIvzYViZCedJmJEymtWc3PeJLtGbnuntWE6nOjs5vJ_uOvMWK1Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز بازهم دعای دروغین خود را تکرار کرد: تنگه هرمز در کنترل داریم! / هرشب ۳۰ کشتی از تنگه هرمز عبور خواهد کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/686022" target="_blank">📅 23:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686021">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
اظهارات تکراری ترامپ تروریست: ایران یک کشور شکست خورده است   رئیس جمهور جنایتکار آمریکا:
🔹
نیروهای دریایی و تجهیزات آنها از بین رفته است. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/686021" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686020">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf83a88f5.mp4?token=pQ_7Y0Pncp1W5PdmMSaR9zH1b0gUWgsTrGQwfmj8DepyQNcyRtHL4A3M3u15RcbxwUDByfrf7xnFvKmE_6vIy2KH1JVEtMjqsxh34-VhhnGQ88OpIOh-kwL1PZSx_dTvyGPQ2HD3zvQKUEAF-4rQ9LaxQsN6HqCmC8JofkLcAxGFb0qQT6YHpd3MpsKUpa5d-wEzcgvVMkMrHOQwEsY6IdRA1sastlc_Xa5e86oL6vc-FKMpDbYHrp0ko9U0R0bTur2TLaG8JkBDkg1eCSiUTgzveDrkO9yC6sK8_eBq6g3xzChVObth_qs_zOU2KOztLXL-TCx9v6nnEQdmscPqpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf83a88f5.mp4?token=pQ_7Y0Pncp1W5PdmMSaR9zH1b0gUWgsTrGQwfmj8DepyQNcyRtHL4A3M3u15RcbxwUDByfrf7xnFvKmE_6vIy2KH1JVEtMjqsxh34-VhhnGQ88OpIOh-kwL1PZSx_dTvyGPQ2HD3zvQKUEAF-4rQ9LaxQsN6HqCmC8JofkLcAxGFb0qQT6YHpd3MpsKUpa5d-wEzcgvVMkMrHOQwEsY6IdRA1sastlc_Xa5e86oL6vc-FKMpDbYHrp0ko9U0R0bTur2TLaG8JkBDkg1eCSiUTgzveDrkO9yC6sK8_eBq6g3xzChVObth_qs_zOU2KOztLXL-TCx9v6nnEQdmscPqpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات تکراری ترامپ تروریست: ایران یک کشور شکست خورده است
رئیس جمهور جنایتکار آمریکا:
🔹
نیروهای دریایی و تجهیزات آنها از بین رفته است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/686020" target="_blank">📅 23:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686010">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUzi2n0Pxe8ZialLgQhw6y4ZIv4UO1lRIBOGyEeeeymis3jQxmeBfwvINfntqwuNWQeIvQhz4mNNcXnQotFzaQAYDD3tny36ZQGQCl9y1-ao4GCEOs3C8m3FZqP4cYaPgWTIXNyUhKRSlkRlwIc89E7o86KYpYlmjQIR_gtny-QQFcnjCGDIjrKDnDGRuOuk085pjTcLo_HrpucbKMSdsuUO-_4XGbiriN9o9WOqYMSs7p7mn1EZGyt35Ev82Pr6NdZsDj4JcaDt7vf-H1zSagvZ-hhQdLUvlttvmGlm3QXxaaxa28NKCiP6Zl35kuR9vh4oKDNEUb7Tw8AHfHA9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oDq5w7lIWMUSBEKgZo4j09pUuh85moLUgcxTMdnCmnLbHacQEe6UU196gZBSrG9xFgeKmd6M8gcDYEcpPFULwt9pbUFMNyIN1e8rPlYuqhTQx3VJ8GjqCxbhTnkcIp_bIJfTLZ2Pjk0omEE99gsJDthwBe28tdVVWmizDuuIcg1VKbMmCbmwE3UXjt0T3LBJLlFeQQWBCxw0E8MSc7T2cHVqWs-DmUirmI_7sosAbAMmX6hzVvx4tiV3d5iKSbeNZN0j5OXiC9lZdkaF5X9oZz2hM8FkgclZLjKqlmk-LmrEYg78uxpbZWhNSNZ8m-jJoNk_jibNBjDEG2IqKRCMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhpAqielwMhBkNwFCz7Q1HIYj2NgAmgfHceC0ciRh3giFvTgh4mgsGvVq_wuds-dd5M6rL2EfMglRONd5L7gHJX7cUalQ0PTfH08cthj8E3XH5iq1Yty7waYJHS_2d06jQWfu2gA-ASdi2XYpKFBiCHcBEHUXV8mPlw7uZebjJX6jYRTpXPTytB4xXSA-WYOH3XpqYGIks5uJd6CgNHwVWtoeJEZ61ffHYZ3Ke4_vLeOb0Wl6VILDVGid7GbmKrihgpqKgvzoec6DAzHb4RLIl-nnoHuOe3scIAlr7kEtVI4Wcdj8mPOtLP6AAWDhhbMpeNIRY20HEqEkwBWZjorMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJS5rmGiKD-lRsfkL8DcoxatAIUzPHcx1ZF2pRvGwLXLRYehAvt2vogvDzGrVHWG9K4o86k5WvdrS33iEIklxj5aZI9dYLS24pADZ71Qy5kxrdxsRlvDRLkDiyagGTb92hoNNe97brXabi6KUrqjKncDZSq4x3oEOrC0FabZqqCxPX3tcGSxVQXbss6qCdtvwrT8pYYO5Wyyo0T0Eo6xDGMRKk52Yvx6bp2rcUeVOCiVv-4Hi1FQI8ohPwLohDWJeu3OXNAwTof4DohKxKcsgvJh9KQcWBMIxokNtdDjghzznEGVdyrAdoLahRkpqrpmhP9AjFh9T847I596W2F9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8f7mrXeWo-jZn2fRU3Telv0FV8XoUP9JmRn8fDyo7rjngK2Y4QR_9l_JWQIdagD5lXF16z3_10-p5ZQjZjmZMG_Jrum7Yw9Fznz5XbQ8AgAIOkRuVfSivhGHDCMruAhLtikAp9-3mepmc4prh0p_uuj0Ja9bjvYtK8-tnhv7kpOHfBUW2zZyzZokZ-seDzmtS765Qcd619xYrZMlLt7TqiTkQxmcpoBT_qO9_Vcb3ZDBCu7hXm9UuabKQnsszMYbc1qWU1jR4bzKfSGRXovqyNDN1lpJSjZpzVzFUk6aLuFK4TZk2Dep7vGNG9zWJEtzQQ7YuISrrLPu6Y01Nj9GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCUDR_WL8WywaIDMQMSwuZDfniZCPGCouFcj3PRGGYlgq8zAxmXYRi9cNpINwOwyA4ihDsJ1OC_vnXPEKKUtknVAPz2J7RwwTo5_lI1FVrYZhnPj0DQSkM8NRZs_RuZkRNDlXhBsGeQDZhJ2i2vpdnN5qK9KrujimAsYI8yMUAHV1fghMn51OeA-1S_iYH_OsO5kIRKEMk0ZpQehi0DkGWhq8OQgqZErhKCz90e1EwPqFD9x9MwFktALW-lnBbE_c6MAY6D0dkn5TaXo_1D1fWBI5PIB06nnbzjfQdRHALD73lCu11xRcT_Et77vO_eFE_2bktuJYkhMtEPxufDg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hr-hu039QkBROWsEx45Y4Iyk5RP7UQIaCvXKBv88kcLJrPqPGxNmDg4zhYUBwCsuDGI8iGSTh9PhXkVE7piqz7bYteGNPHG7pKY88-h6JNiFh8UlHbhr4UVbM14lzGBtl-4JavmHLVlRIZcJXtg53kmWNuFHaQayNtxkna0cju9h3ocNCog3QyaJCIMvm7Be0KC4LDf_ChnMRVN_S8rLRHAoEO35Ysk0DqeAJAvojdyLjk08BM1p266RrmT3QdWbqLFMxn3ihpzmKLg6u0zbo3rHuHi0qisVCrrPTUdGcmm10rgqr_E4O6hO8eAQe2g94tRrfqUzVXGw2WjHwiGGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gd7F9Ud0M1iLcQJ1lOp-FTLKPrsw-xj_RqeKcFJZHM3rDNCddKqKZHcEbU1X9wwXkfSvEwHf8cmJ0_3800_73tZtsCKt2N0zL0aaIALhMkhI4h1txA4M3rAaWaoqHVk9LNxdTpJ6jQKcRz0nvXAoZSVT5Z2m01iVTepwF0s1aOB5WEnc6s7rIewJmJCg3YQ1aTxUnkOMdlXH28_c0SU6UTYWTiT-qGGZSdjDe7VfRfLADf3HhR9btJRGUmBuiqxuJ8LGgMGEZMVHX0pQMRTd9VE76tTY_s1NTxQT2oO3G7BcDKa_jhM0ClLSL7jmRUgYdD-UrFUlfKlhpRTzNpinLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfR8DYecewzhYTSFXKogQ7co8HZHWkLMNzWE63nJk1VY3T0RiSIo1vxjVuR38neZMbGueMIBRUcLtgtsE1bX3WnjzOXsgrYp8TYzEIeMRyAgWNcv8sDlhWzWuxLkqY8jy_CwJfpCQ9poWbZOzrso9-RmUov0TFcEIykqWEJysFd4k4io4Rspn5h-4kTdB3kxequlOEfp_hdzPcaZ6dxKgaPH1EmbqN5rUJWwTngfYizbOSd7bDFJ3VEwF_JROrQRkZslL1ZhEOC341fHroqrLFVSV0jxdHrZZZnu5zIDDhHkd49Iwmm7juPoE9Vp3QN0RwCtWmo4GnyNLXLmSHRykA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPVgGWlFZ5d9SsjJlGGwOKOx0e1S1o-Z7OItKiQORF5kcTgez0JW_Fq6Dl16dHdEj3i0C2hDErL6rL2YGyhSPGV8KnalumXntBcoPh0VJ6fSf4PGJcRg04_aWlvfR6uEbFXbl3h7IqhlZ88UGqsvScdtutMOyLR9jEiV-KEnBRVXwojm44eEMsqIpPza7c31mKEbeRzdfrklJpIfnn8gILt44TnPHmaWRQqsMQ2fL5UAC-gQFQDqwUtS4nR0AeWrbyelg6aWWGbvZNgiyXOAvJrR_sjEXHryJ_VCteIA41eg32N6Or2nVE_4v-dLfXpxn457gKi1aH30YOVfMu80Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایتی از موانع پیش‌رو برای دسترسی آسان به اقلام دارویی ضروری.
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/686010" target="_blank">📅 23:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686009">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef54732e3a.mp4?token=PWJcgua0Grs_Pgw1HohivlmZ8007hLHcGZK0wtfkICr_Oujr1MpMT7707jDl9cDacO9ZpzrsoKFxDM_8Z1ZxJJTeJNo5DQD2EjxZNhH_su3nYvNPr4VSgrAAnqfHw6uJEx94qBQT4rMMiqyQBAOWN4NNZ4UKiyhUI4OJlQ5bs2Kgm4iwy54ThnRr9QME7pkG6I3SALvq2XqmiMMwkR1vX0wYd2-x3bYWWZgZ5LVjeBNptnSQFAOVpEWBchMLbxvB0iAGcchcYdqYN3h1XnvC040xipARYnHoRSrElFO1_LkVwb6COk3C_e9QvpebLlzWEkUEtshTTdbSmNVhO7w0QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef54732e3a.mp4?token=PWJcgua0Grs_Pgw1HohivlmZ8007hLHcGZK0wtfkICr_Oujr1MpMT7707jDl9cDacO9ZpzrsoKFxDM_8Z1ZxJJTeJNo5DQD2EjxZNhH_su3nYvNPr4VSgrAAnqfHw6uJEx94qBQT4rMMiqyQBAOWN4NNZ4UKiyhUI4OJlQ5bs2Kgm4iwy54ThnRr9QME7pkG6I3SALvq2XqmiMMwkR1vX0wYd2-x3bYWWZgZ5LVjeBNptnSQFAOVpEWBchMLbxvB0iAGcchcYdqYN3h1XnvC040xipARYnHoRSrElFO1_LkVwb6COk3C_e9QvpebLlzWEkUEtshTTdbSmNVhO7w0QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش اختصاصی شبکهٔ سه از جزیرهٔ لارک/ تنگهٔ هرمز همچنان بسته است؛ هر روز کشتی‌های مختلف هدف قرار می‌گیرند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/686009" target="_blank">📅 23:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686008">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFC-BidOX7HT_ViNPaku9kHj6wj6yf98ePNDe0_HIMpzIY18T6INmrKlQD3jDcLPdWz3Uzv7tZ8A7Y2nZMKlZ87YAUO_kmSWLuxvYtKQbnqxFy46c0I1PuywQA7uRGTaglzZ4xFkVsQaAEgt88Dw7HFs9qs1o293AclSuHOdA3lf4xfAAoQuygPdn1h8OCODojkY6276ct9q-1L8ZV0iTOpLIZoFi2wqV6IijcJUyr2mk37VfGKDFz-JYeJIMGP3XpT2sTPETYIqlzeTllDUVsL0ikNpfEN275dLI1JeMq-Nu2CZmi9o3RT07W24Hd57um1amHk9o1jFby2gl41DSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوید محمدزاده به‌خاطر موضع‌گیری علیه اسرائیل از تئاتر «آرش» کنار گذاشته شد؟
🔹
صبانیوز نوشت: نوید محمدزاده که پیش از این به عنوان یکی از بازیگران تئاتر ارکسترال «آرش» معرفی شده بود، از این اثر کنار گذاشته شد.
🔹
این بازیگر حدود دو هفته پیش، در حمایت از فلسطین پستی در صفحه مجازی‎اش منتشر کرد که حمله لشکر سایبری را در پی داشت و تیم سازنده این نمایش، یکی از دلایل کنار گذاشتن او را عدم رغبت تماشاگران عنوان کردند! این درحالی است که بعد از باز شدن سامانه فروش بلیت این تئاتر، با وجود هزینه چند میلیونی برای هر بلیت، مخاطبان آن را خریداری کرده بودند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/686008" target="_blank">📅 23:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686007">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b600ec4856.mp4?token=COfoJ6sW3cmWgoG3eTtjga51gLghZ5BzCrrIJCIPLZKycp49NRZODJ-QodEZn0GS88xSJ8JfKYV2R_huvVwEN7IXPtks8dKEgLEbXSmmYPmZdBFSuQoSjFWitmaCeX_jbd-eD1lb8B3Im654SL5zlvNoZqKRJB8yKbLwTR1-nDpy9TNjxDNMQV-UH4hOSHn5Rpuzg2E2bgX3wyqTZ6HRKN1CNrDTWndomWI67RjM8KS1jpz3UYbGunxYpipIPQ5bjNUAmIVA8kL9EPwvPEhP0U_oo-OHQk66ZhZH8UGxk53fvdWDMIzHLWCcBb-s0tih7qSE19yopQME3Kf3fnjPsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b600ec4856.mp4?token=COfoJ6sW3cmWgoG3eTtjga51gLghZ5BzCrrIJCIPLZKycp49NRZODJ-QodEZn0GS88xSJ8JfKYV2R_huvVwEN7IXPtks8dKEgLEbXSmmYPmZdBFSuQoSjFWitmaCeX_jbd-eD1lb8B3Im654SL5zlvNoZqKRJB8yKbLwTR1-nDpy9TNjxDNMQV-UH4hOSHn5Rpuzg2E2bgX3wyqTZ6HRKN1CNrDTWndomWI67RjM8KS1jpz3UYbGunxYpipIPQ5bjNUAmIVA8kL9EPwvPEhP0U_oo-OHQk66ZhZH8UGxk53fvdWDMIzHLWCcBb-s0tih7qSE19yopQME3Kf3fnjPsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار پزشکیان با نخست‌وزیر هند
🔹
در این دیدار، طرفین ضمن بررسی آخرین وضعیت روابط دوجانبه، بر ضرورت تقویت و گسترش همکاری‌های مشترک میان ایران و هند در حوزه‌های مورد علاقه دو کشور تأکید کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/686007" target="_blank">📅 23:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686006">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afd627f0b.mp4?token=j3cMei89zFYVGDHLDuiRCixSGufbOuYXJsvQVu41Bgf1RZ1YY7AgPLKMi3RnyKdlQBLudvf_sr2zdV3P0RKGTBh8aNvLZ3P0GiTycJSCN5EU7RChEj7Lcg8Ytnh2dWcZxExjUBsOP539TmDsJKzxvDDjIViPf-Ppv6nCKL68m-I19a1WTRdPTrvQ2Avs7HNRle5wj65sBXJ4mWb9Yht4vS6D_hiHvoIIEFO3QhVeXXqhWmr4ZP3nhCLrn1YvuCM2x1oquA2ZAyoP66ND8uyPiPqvP7PszMAx-iz8eljwQi-5l139ykk0o02ruB5cgGhSNd0LJ71w0478EoPX9Iigsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afd627f0b.mp4?token=j3cMei89zFYVGDHLDuiRCixSGufbOuYXJsvQVu41Bgf1RZ1YY7AgPLKMi3RnyKdlQBLudvf_sr2zdV3P0RKGTBh8aNvLZ3P0GiTycJSCN5EU7RChEj7Lcg8Ytnh2dWcZxExjUBsOP539TmDsJKzxvDDjIViPf-Ppv6nCKL68m-I19a1WTRdPTrvQ2Avs7HNRle5wj65sBXJ4mWb9Yht4vS6D_hiHvoIIEFO3QhVeXXqhWmr4ZP3nhCLrn1YvuCM2x1oquA2ZAyoP66ND8uyPiPqvP7PszMAx-iz8eljwQi-5l139ykk0o02ruB5cgGhSNd0LJ71w0478EoPX9Iigsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: در صورت وقوع یک وضعیت اضطراری یا جنگ، ما کاملا مجهز و آماده هستیم
🔹
هیچ‌کس قرار نیست به ما حمله کند، می‌دانید چرا؟ چون آنها عاقل هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/686006" target="_blank">📅 23:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686005">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f8f10249.mp4?token=Ew0EopGUw33hna7y215Xnu9JWUoE4FhD9z0SErWHstXs9uKzpDWRBuVOJocPK-0_RAfpvATELkvKaeef_1SpDziqVMeUV0cc5XegHs4PxuYLIpNHSf9d5unLcSpHSP4lYFmVxqw3JycT2iO4IMwZ1FxhZETBvgMAwX6DSgUpAbp46Dse7GqdHlC-jDdqISmT_FlIc-egfaQjTYHLScESJCe1d0p2MCGoqfHZuQafvrELy8X0f6UvQ3fIVhl_KsOLbfJDbw-b9oXeOSpjLVVZP1aSJID0gOtUlzs8ceakhrh2wk88K2ZfialwAv8707cwJJV-zqr514KabcMJavkQ-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f8f10249.mp4?token=Ew0EopGUw33hna7y215Xnu9JWUoE4FhD9z0SErWHstXs9uKzpDWRBuVOJocPK-0_RAfpvATELkvKaeef_1SpDziqVMeUV0cc5XegHs4PxuYLIpNHSf9d5unLcSpHSP4lYFmVxqw3JycT2iO4IMwZ1FxhZETBvgMAwX6DSgUpAbp46Dse7GqdHlC-jDdqISmT_FlIc-egfaQjTYHLScESJCe1d0p2MCGoqfHZuQafvrELy8X0f6UvQ3fIVhl_KsOLbfJDbw-b9oXeOSpjLVVZP1aSJID0gOtUlzs8ceakhrh2wk88K2ZfialwAv8707cwJJV-zqr514KabcMJavkQ-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
جایزه‌های طلایی مای‌دات !
یک عکس و چند فرصت برای برنده شدن
گروه ارزش‌آفرینی دات‌وان با حضور گسترده درنمایشگاه الکامپ، مجموعه‌ای از کسب‌وکارها و راهکارهای خود را معرفی کرده است؛ ازدات‌وان گلد و شبکه اجتماعی مای‌دات گرفته تا دات‌وان سل، دات‌وان ونچرز، دات‌وانپی و دیگر کسب‌وکارهای این گروه. اما حضور دات‌وان در الکامپ فقط به معرفی محصولات و خدمات محدود نمی‌شود؛ این بار، شما هم می‌توانید بخشی از روایت دات‌وان در نمایشگاه باشید.
📸
از نمایشگاه الکامپ و غرفه دات‌وان عکس بگیرید، آن را در مای‌دات با هشتگ
#با_مای_دات
منتشر کنید و برای دریافت شمش طلای ۲.۵ گرمی دات‌وان گلد رقابت کنید.
🎁
بااسکن  QRهای مای‌دات در نقاط مشخص‌شده نمایشگاه و ثبت‌نام در اپلیکیشن، شانس دریافت روزانه ۱۰ کارت هدیه طلا و در پایان نمایشگاه یک شمش نقره یک‌اُنسی را هم خواهیدداشت. این با
ر، الکامپ را شما روایت کنید.
🔗
https://zaya.io/mydotelecomp
#با_مای_دات
#مای_دات
#دات_وان
#الکامپ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/686005" target="_blank">📅 23:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686003">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZg3dr1G1RXYLptpqEA-z7WQ-VL7PC0_Cd_UoXWgHlt9nw3cnRUxcLIHj2PQ8SWrwKja73V1L8UANr_Dx8E72cvJW1idK-Mmh4ifUUnnznOsBZoYi7CQ_xSE4cFvJ8NR5P4oXTd2Z8N5aoPp0NrnY0NRteOS6w6qHTI3p0Mmmj_Tu1IFebRWalbaN6x2Q12xTyokyWBsClRqfxbJ_3Cm95dQTHN0fqR3ugqd2a_w-RibDw7zjnFcXadbVZ3vhPvJ-S9g8wd9eiWCTwVgtIfQ8Ly1mOb867rCUYSul_HBP3XpAtF45-d1JFUJO43MucxPE1DZXb71Z9t1dFEQYRze8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKSvp9QtZ653bLOdq40gzK6Ocz5WU39mmw3WlefZcF1FvDd9eJ_f0SknAe6pBh0028dVt9YM2r7jTZlEgYyKPYB6x_t3Swl3bOLhn_5bh3YHEOEIsgHYUr7rf5n3HrFMj0v56wA6bb5VDddJWatvzc4eoiAxXi0TEoogiqf5LzFl3aEGLO42dqYSUMKzpd0gipo5hIrqm515IBKv6043OCQQRl1sl59eCUxroHSkk7JJVmmWyntiLSIykmmVfeiWakqMSXkAK3buhPjk6H5T-yMZG3PtXxNu5JrzLnjXcbRgkBb4Te4VuxEhiVjL-nNRP7TgnmYj84fGysojLJyIQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سفر خصوصی آصف علی زرداری به اتریش؛ شایعه ازدواج پسرش با نواده خاندان سلطنتی اتریش داغ شد
🔹
آصف علی زرداری، رئیس‌جمهور پاکستان و همسر فقید بی‌نظیر بوتو، برای سفری خصوصی و ۷ روزه وارد اتریش شده.
🔹
گزارش‌ها مدعی‌اند «بختو زرداری»، پسر آصف علی زرداری و بی‌نظیر بوتو، قرار است با «گلوریا فون هابسبورگ»، از نوادگان امپراتور فقید اتریش، شارل اول، ازدواج کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/686003" target="_blank">📅 22:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686002">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد MQ۹ در شرق تنگه هرمز
🔹
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/686002" target="_blank">📅 22:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686001">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
بازگشت به شبهای پرالتهاب/ حمله امشب آمریکا به ایران چگونه خواهد بود؟
👇
khabarfoori.com/fa/tiny/news-3241804
🔹
اختصاص ۵۰ لیتر سهمیه بنزین ۵ هزار تومانی برای ۲ استان
👇
khabarfoori.com/fa/tiny/news-3241796
🔹
سخنرانی یک زن غیرمحجبه در تجمعات شبانه علیه مذاکره/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3241813
🔹
واکنش شیک شمال تهران به ساعات ملتهب اخیر
👇
khabarfoori.com/fa/tiny/news-3241609
🔹
یاسمین پهلوی پیشنهاد بمباران اتمی ایران را داده است؟/ عکس
👇
khabarfoori.com/fa/tiny/news-3241752
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/686001" target="_blank">📅 22:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686000">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
المیادین: ضربات به پایگاه‌های آمریکایی در اردن سخت و دردناک بود
🔹
شبکه المیادین به نقل از منبع امنیتی و سیاسی بلندپایه ایرانی گزارش داد که تهران شب گذشته با قدرت به حملات تجاوزکارانه آمریکا پاسخ داد.
🔹
این منبع ایرانی تصریح کرد که تهران ضربات سخت و دردناکی به پایگاه نظامیان تروریست آمریکا در اردن وارد ساخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/686000" target="_blank">📅 22:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685999">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
هشدار مقامات سازمان ملل درباره از سرگیری آزمایش‌های هسته‌ای و خطر مسابقه تسلیحاتی جدید
🔹
مقامات سازمان ملل متحد همزمان با روز بین‌المللی مبارزه با آزمایش‌های هسته‌ای درباره از سرگیری این آزمایش‌ها و شکل گیری خطر مسابقه تسلیحاتی جدید هشدار دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/685999" target="_blank">📅 22:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685998">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235f699f46.mp4?token=r4ia8VQfS_cidhN6gLkO614XGUr27a1X9RJIjf2v0pr8wQ6j8cpQam2HRELN9_ojfNZxq367DlYwJMKvilJhitbyuiRa9JqzN28tiDI3tx-SK0SocIuFFkZWom3ZPkhkHl_h6_CRuPQBv1nUXatVn33pQKl5OVDFBIfDwi_vFQW8QKczh20Mfg9KhdoeigeNlM_XgXGK0jZjC-WFRltEiKMDtpAePXvxK6rJbjwCDVKeKU2bdAPAVWR4iUcHTJj2UplVx2B92mObUH-SxqjJ-SqGCG_0WNMVBwGdX9lANldTsoLjgZ3mqKv1gQmOEIx9YBNT1LOm9-bszVvgDbpQyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235f699f46.mp4?token=r4ia8VQfS_cidhN6gLkO614XGUr27a1X9RJIjf2v0pr8wQ6j8cpQam2HRELN9_ojfNZxq367DlYwJMKvilJhitbyuiRa9JqzN28tiDI3tx-SK0SocIuFFkZWom3ZPkhkHl_h6_CRuPQBv1nUXatVn33pQKl5OVDFBIfDwi_vFQW8QKczh20Mfg9KhdoeigeNlM_XgXGK0jZjC-WFRltEiKMDtpAePXvxK6rJbjwCDVKeKU2bdAPAVWR4iUcHTJj2UplVx2B92mObUH-SxqjJ-SqGCG_0WNMVBwGdX9lANldTsoLjgZ3mqKv1gQmOEIx9YBNT1LOm9-bszVvgDbpQyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: هلیکوپترهای آمریکایی از پایگاه موفق السلتی به مکان دیگری در حال جابجایی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/685998" target="_blank">📅 22:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685997">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFUAVqLPqJCHLOt3zTF_3kcIYeTcHC2UkYQOPbV5psekSbnp1f87nYOT4fT03hbebCPr-63WzRdBwqgH1Wwr_kAwNy6rwU06dxclSeq8g0jBqX8hHrBuZl5CkevxIAGHtnUc9jziOmLL_iQN9yl2URdwi2DlvgWPA4IcZmewOJSsSRA_6CFMY5X4T2whLI-VvbD9WBi7BoX5OucH4lVx6OnM-am34ZQugIFpXg_G0Fxmc7g1f_yBEM-3Jc9Ezwjxv_HX92TjQiMONtYbukAdNwz9aFB02ikju6eVxLrdzmF45A18CMIXnCWxfnyEzaYleNBnnwgldO2IpUqUe8WhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش تلویحی رئیس شورای عالی استان‌ها برای تمدید دوره ششم شورای شهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/685997" target="_blank">📅 22:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685996">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STy2IOwJk7fzSSGuMvgF8FNHUrdZgdBZqKw-fzOpPZUlXFFXE9_F1JZCdHC7JyQ1Ft9MsGz0jKs80lExPLJe_ae9fPS-fV53d15h96sc-Ql4sJS4i-PXRLIdwLyiE22PRpU8GTDZbywPtRW4YutbgXL_zgCwLHqUu6Gbc4YzXjJnFTv6MIJdAsR3LZCmEnG_uWzo1MVJjRAXNcHScnj4tFSzDRpmZ8PG1HZtzLbDfKbq8MLOPtHWmS5vCRbI3xsjmoSRvmfPVwID_KR1Ro8AYiVrFTRTFD4HJc-xKCw_5ePrkw34XEezNGfKL3pbNBkvy_sKz8Hz3mnn6dl_mjUhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکسیوس به نقل از سه مقام آمریکایی: ترامپ در حال بررسی حملات محدود علیه ایران برای مهار حملات به تردد کشتی‌ها در تنگه هرمز است
🔹
یکی از حوادثی که طی روز‌های اخیر نگرانی آمریکا را افزایش داد، شلیک به سمت یک فروند جنگنده F-۳۵ آمریکایی بود که در حال تأمین پوشش هوایی برای کشتی‌ها در تنگه هرمز بود / انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/685996" target="_blank">📅 22:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685995">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b368417012.mp4?token=Xc2T1PYlbQorGgIeJBVfPFTC5KEhl7BuTOLyZ0qX4aTI9LXg0WETimVKisR9QjjJlJ9N98jgKQUzEM4NP6NzoTAEsJuQxVRxzRX9EigxO7GMiCEBhTt5CrhPG-4CaAuDunskZmZ3fqBZktwckRSz9cgccbAmMEK8dQwoAEOY68WQxPvXKJ7rVhOXQ1jBY7bSxU65yDxK3_9upmuY25b9sYqCQhVfzFkMr8bvXyG_c_b_h2pYOPp3jt3Xh7hOcMMFbIO06UTd6c-hJu1NGd9K-nMjT5lK0uY7LvVw2gyXSb3gcubv0ykGRqUJiqLeLzF6838Gfk9UEdJ8N_OwSTHGWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b368417012.mp4?token=Xc2T1PYlbQorGgIeJBVfPFTC5KEhl7BuTOLyZ0qX4aTI9LXg0WETimVKisR9QjjJlJ9N98jgKQUzEM4NP6NzoTAEsJuQxVRxzRX9EigxO7GMiCEBhTt5CrhPG-4CaAuDunskZmZ3fqBZktwckRSz9cgccbAmMEK8dQwoAEOY68WQxPvXKJ7rVhOXQ1jBY7bSxU65yDxK3_9upmuY25b9sYqCQhVfzFkMr8bvXyG_c_b_h2pYOPp3jt3Xh7hOcMMFbIO06UTd6c-hJu1NGd9K-nMjT5lK0uY7LvVw2gyXSb3gcubv0ykGRqUJiqLeLzF6838Gfk9UEdJ8N_OwSTHGWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از لحظه شلیک موشک‌های ضد کشتی به سمت اهدافی در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/685995" target="_blank">📅 22:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685993">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf_8MZZ3iJ-0h6Jv90zLEnkLAtH-sXsYidIFyEOX1c7OZy36NrQMs4HmnfnhtH5-DuVfQTeBrJ-nCGVga-2VMJrCtOJuOc3QnMWmP_RR7UrimU_opi3zaZ80V0ysLN2U7OpMNUwj-BP8CrcD_PBGi0f79lPYF8ihKTcFTh5_7z1gCL_p9-iS9J8kofSOJ5arPnHtRMy0fFfzRKagzx0s_A6ZV25hSgSVM0eudi1-TG8sJG6zniAGJXYDLt_BNgJFGsc8hJ0hWf080J8KNN_LW-TgLBp4WXLnU8acsMvvHoxY50ZW3ppx2eHbOlFHoQkOOU1glLft6iPt8VWwzOtzrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمپین جدید سلطنت‌طلبان: علی کریمی را آنفالو کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/685993" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685992">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4b97da8c.mp4?token=s24lluNhJ7xGPcB72qfqxKO2TCp7FaM6lznVyaPSV7PtauwmO6qAKYURrb_BqaBBbK3zHWua0isgx0HU5rsALYe9aIT8mppfyX-GbXI9OKjK0tfQoOCg4pwg9cdCQeKeRDUTfAzEymt3Y13PslWavAY2mYBpKk0MFaykG4EwhWhxz9PYK-TR0HYMetGzZZGzIEyPoqssuvTxjXV0glkB0bLkZ2Bft1gUQSr3OtyURrMZawpQ6gwAuPBUBPGfs6VL2h5X59lsTxUi6Owt-t60-XHFngHGN3DD0qhjdufHxZrGCP8YBHNjNJ7pMmm-1tFupBKoBLFUmRYpZndy0Gc62IsLvgK0SZMRU0zZU-h0sKt91NiG2jxA8ZCjtg_4KSxKs573wZUdir_dbb1wfwllI-D1gg5ASPDU87dKX89ZR1ExGGo1EHu0-fRJ8TfsWFAPXjR-2Xoeoa7PhXM9XpKUjr0eFXC5_Hw5ZYa5MsQH7BQXbUzb5rhH-s49n0Iyd9zKk4qdG25DtBPudj1KfcDmaajlJwgU7QAACOk5g9pTAsnvDF6IuLB3xmeFMum8fh458Z0emUp2Z8VXw2R1R_8kKI38wgU6sqjmaneStdWGYdfy0asBECflBDFqQMeDvmWK5hl_0384MO_VQixHhqTuXHicGR2orLGn58m7IYHrtco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4b97da8c.mp4?token=s24lluNhJ7xGPcB72qfqxKO2TCp7FaM6lznVyaPSV7PtauwmO6qAKYURrb_BqaBBbK3zHWua0isgx0HU5rsALYe9aIT8mppfyX-GbXI9OKjK0tfQoOCg4pwg9cdCQeKeRDUTfAzEymt3Y13PslWavAY2mYBpKk0MFaykG4EwhWhxz9PYK-TR0HYMetGzZZGzIEyPoqssuvTxjXV0glkB0bLkZ2Bft1gUQSr3OtyURrMZawpQ6gwAuPBUBPGfs6VL2h5X59lsTxUi6Owt-t60-XHFngHGN3DD0qhjdufHxZrGCP8YBHNjNJ7pMmm-1tFupBKoBLFUmRYpZndy0Gc62IsLvgK0SZMRU0zZU-h0sKt91NiG2jxA8ZCjtg_4KSxKs573wZUdir_dbb1wfwllI-D1gg5ASPDU87dKX89ZR1ExGGo1EHu0-fRJ8TfsWFAPXjR-2Xoeoa7PhXM9XpKUjr0eFXC5_Hw5ZYa5MsQH7BQXbUzb5rhH-s49n0Iyd9zKk4qdG25DtBPudj1KfcDmaajlJwgU7QAACOk5g9pTAsnvDF6IuLB3xmeFMum8fh458Z0emUp2Z8VXw2R1R_8kKI38wgU6sqjmaneStdWGYdfy0asBECflBDFqQMeDvmWK5hl_0384MO_VQixHhqTuXHicGR2orLGn58m7IYHrtco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار ارشد بی‌بی‌سی: پس از حملات ایران در اردن و امارات سانسور شدیدی در این دو کشور حاکم شده و کسی حق فیلمبرداری ندارد
نفیسه کوهنورد:
🔹
پس از حملات ایران، سانسور شدیدی در این دو کشور حاکم شده و کسی حق فیلمبرداری ندارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/685992" target="_blank">📅 22:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685991">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1CQzJEdRPWTFqw2vCAD4CEN0daauQlKGz-CvHe3EWRlwSPRbnKJuO1_xdP5U9Bt8Cs5-MCHnhCRk4suc200V5rf39sBRZqiHlTTJIDp9Uzj-9qRbpHlGQ4vMlSBcW4bgVciwnVMB9JSCjq_IMdGeXeWqF2RFb5n_UXn9Bq2rJIOayCGs6WIy6OGzAd3XLo_JbuVmzTOrI8LWk77WSoby9GalDYV5hRwWbBfhXBqu0MiI0zP_X4CbUcCf2uhzjk60lDrhoM93-P6SdLea8xOA6JxnGxfV-VLhwdcJ3C-f15xVsvmCIsQ5y5DiO3k_Bx_h-ugYMpe2y6nz9tzH71BlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود پوتین و مودی با یک ماشین برای مراسم افتتاحیه بازی‌های جهانی عشایر در بیشکک
🔹
نخست وزیر هند عکسی از داخل ماشین رئیس جمهور روسیه منتشر کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/685991" target="_blank">📅 22:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685990">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JobZHSj0yKJKmGyw5EOtdCBI8wZTy4tA9xCyWnIXFpPKU4gRJtoQK2qMiaUuxI-ohNp7FswuEm7ZIAW3Z4i0pxItTo2JS_LoDZ4PRITFm9z4f1XlascmDlT_iEFRfRzvdJD5CtP_gZrLetlqZzK2AqGJR5dDeGUWf--SisXonBjD_iNuCmNe6C2rphqPkTOu5lV1TspY-6IuWxbJzVMKVWAAd-zl0jHiFEoYrm5KZ5C5gbKFryXDBlD9j85KfEhVYzkQYBTbfaJaNwOtK990376VhLMYY6m_-bvlQqwmKUeb22eMcrCb6HOqx8BrtdZ98lZEf06cZb60QgE0OeY8hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاهی رها کردن، شکست نیست؛ انتخابی‌ست برای آرامش و آزادی بیشتر
🔹
امام علی(ع) در نهج‌البلاغه می‌فرماید: «بهترین بی‌نیازی، ترک آرزوهاست.» وقتی انسان از خواسته‌های دست‌نیافتنی دل می‌کند، خود را از وابستگی و رنج رها کرده و به آرامش واقعی نزدیک‌تر می‌شود. #نه…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/685990" target="_blank">📅 22:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685989">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
توهمات سخنگوی کاخ سفید: همه گزینه‌ها در خصوص ایران را در اختیار داریم
شبکه الجزیره:
🔹
سخنگوی کاخ سفید در ادعایی دروغین  مدعی شد که دولت تروریستی آمریکا  همه گزینه‌ها را در مورد ایران در اختیار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/685989" target="_blank">📅 21:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
استفاده آمریکا از موشک «پریسم» در جنایت لامرد
🔹
خبرگزاری آسوشیتدپرس در یک گزارش تحقیقی امروز دوشنبه تأیید کرده که حمله روز ۹ اسفند به سالن ورزشی شهر لامرد در استان فارس توسط ایالات متحده و با موشک پریسم انجام شده است.
🔹
آسوشیتدپرس پریسم را «سلاحی مرگبار» توصیف کرده که ارتش ایالات متحده در نخستین روز جنگ علیه ایران برای اولین بار از آن استفاده کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/685988" target="_blank">📅 21:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانداری شهرستان کبودرآهنگ: انفجار کنترل‌شده مهمات باقی‌مانده از جنگ رمضان فردا صورت می‌گیرد
🔹
موعود بنیادی‌فر، به صورت رسمی به عنوان داور دیدار استقلال و پرسپولیس انتخاب شد
🔹
نخست‌وزیر پاکستان: ایران و پاکستان دو کشور برادر و همسایه‌اند؛ برای صلح و کاهش تنش‌ها همکاری می‌کنیم
🔹
کالاس: توقیف نفتکش های مرتبط با روسیه ادامه می یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/685987" target="_blank">📅 21:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08fe759132.mp4?token=ltMql_9Gpvv1EL33ebpsOlIeV_tjGN1LvviLMdAZBkuPDHkt9G5saeTkYUZd8FrwKYaoNYvLaEMpxaT86wzmkr0yic-IxXrRF4c9cNI3iYkO06umyvLF3SIWLW2777UMdLg4SVhLwSH2HP6kCzYkcmg6BaKagpcrT6Xbi3wdQ7TMeZ6QabGERIdkGbf5B4xXA9sRYPV-wc2IuuJzgQteIhPRa9H_B19BF3dyEYDbedXZbCcC83XRddzCIlEXhhpQnfa1f21RJgCfpLJiLySJYFwl2cFqMhnvRz1naJkxREvOuNaHSbKJV_oBA7SEths1gBSuqdhSgG4Xl0aX-u9FKg5ucP4fgpkoBPqQPipEHKsjjCxpObuzMA7qAvCFPMjY56z72lDh6xw-BOM9pIbEJurijIqRO1n6ATUt89DoNtNaKMZmHd6kkfTQEPdy8iK2PDHiKjdq1dvyH3sFRtPle36BNoFFydR7TpB-Bnv6GcUaWrWGEHh_MMWdXccpWVi2Evhjo45nZe3sBpEb9EPmSbFanHZxAf8LjPPvgnQONO5lkV39AbhePOLEQxUsyxI1OApICdg2zWj1AOroTjN8atc9krl_9o1izbI-WL9f3yQjv-1F6wM3mRIWG2QTtieLtC9eHq6OqKOO96-Vl86N7bsubPAOKHOcTl-vp0WDgxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08fe759132.mp4?token=ltMql_9Gpvv1EL33ebpsOlIeV_tjGN1LvviLMdAZBkuPDHkt9G5saeTkYUZd8FrwKYaoNYvLaEMpxaT86wzmkr0yic-IxXrRF4c9cNI3iYkO06umyvLF3SIWLW2777UMdLg4SVhLwSH2HP6kCzYkcmg6BaKagpcrT6Xbi3wdQ7TMeZ6QabGERIdkGbf5B4xXA9sRYPV-wc2IuuJzgQteIhPRa9H_B19BF3dyEYDbedXZbCcC83XRddzCIlEXhhpQnfa1f21RJgCfpLJiLySJYFwl2cFqMhnvRz1naJkxREvOuNaHSbKJV_oBA7SEths1gBSuqdhSgG4Xl0aX-u9FKg5ucP4fgpkoBPqQPipEHKsjjCxpObuzMA7qAvCFPMjY56z72lDh6xw-BOM9pIbEJurijIqRO1n6ATUt89DoNtNaKMZmHd6kkfTQEPdy8iK2PDHiKjdq1dvyH3sFRtPle36BNoFFydR7TpB-Bnv6GcUaWrWGEHh_MMWdXccpWVi2Evhjo45nZe3sBpEb9EPmSbFanHZxAf8LjPPvgnQONO5lkV39AbhePOLEQxUsyxI1OApICdg2zWj1AOroTjN8atc9krl_9o1izbI-WL9f3yQjv-1F6wM3mRIWG2QTtieLtC9eHq6OqKOO96-Vl86N7bsubPAOKHOcTl-vp0WDgxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل ناگهانی و شدید در گرند کنین در آمریکا
🔹
سیل ناگهانی و شدید در گرند کنین  در آمریکا دست‌کم یک نفر را کشته، بیش از ده نفر را مفقود کرده است؛ این منطقه  در ایالت آریزونا در آمریکا قرار دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/685986" target="_blank">📅 21:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سردار شکارچی: برخی نظامیان آمریکایی‌ در ناو آبراهام لینکلن دست به خودکشی زده‌اند
🔹
ناو آمریکایی جرأت پهلوگیری در کشور‌های منطقه را ندارد، کارکنانشان با افسردگی و استرس و مشکلات روحی و روانی مواجه هستند
🔹
با مشکل پشتیبانی رو‌به‌رو هستند تغذیه مناسب و بهداشت ندارند و در شرایط بسیار سختی در داخل ناو زندگی می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/685985" target="_blank">📅 21:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">09 Ane Manaee (1403-09-14) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/685984" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه نهم
حجت‌الاسلام امینی‌خواه:
🔹
عمل در آیینه هستی؛ تأملی بر جایگاه و معنای آن
🔹
سهل و دشوار؛ تقابل عادت و خلاف عادت در میدان عمل [6:20]
🔹
از تمرین تا تمرکز؛ عبور از سطح به عمق معارف دینی [16:19]
🔹
عمل قلبی؛ سخت‌ترین میدان خودسازی [19:15]
🔹
وقتی خدا با ما سخن می‌گوید؛ زمزمه‌های حمد و سوره [26:16]
🔹
حضور قلب از نگاه آیت‌الله بهجت؛ گرمای دل در زمزمه با خدا [28:48]
🔹
عمل و محبت؛ هرچه خالص‌تر، اثر عمیق‌تر [32:28]
🔹
عبادت بنی‌اسرائیلی؛ پوسته‌ای زیبا، اما بی‌عمق معرفت [39:00]
🔹
خواب با یقین؛ بالاتر از بیداری جاهلانه در عبادت [45:29]
🔹
معرفت، کلید اثر؛ چرا شناخت، عمل را متحول می‌کند؟ [47:45]
🔹
اشک‌هایی که هرگز خشک نشد... [51:48]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/685984" target="_blank">📅 21:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUELxovXzI3RFnpK0yVlRIzpfA0MwKqd9jxsavkzYxPGfNkznefV_vaTsdoWG0EmoOc-uOKQN8VsjUKRNOOkedf8RM_P08L6Epr82HVtNi6wNhL77Ip3R7SwE4snQQxp65iugNOHQ1YpSlrbZvjdAEjpbI4yTs72uZFNwgp1OtV3IruNRGeKm82KSWsvLhSBmv04EkfZXIYRBeMfD0GlUdywazyNBdz7AKu4CwokfOwqOLF42PjDP-Fb6IrIVf6WlEbWt0VIMeG4pcX5ZS1ER0DmAGTCqu_-5kbhkW0YwMoFiPwnkT9f3qvw2znb3tRgH9FyZ5z1CgO0kLcSlZEprg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پر پروتئین‌ترین غذاهای جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/685983" target="_blank">📅 21:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df8311ae6.mp4?token=XUKWfVuZ0lDsa1FdJfhaT0-8WzTnxvASM3tcAUgTAUtgM2WIv76ByiYwaJ2FzBrJTUCg2y-JsixkGgRxse3v_k_yMmQTYMczWYz2XFztF0SWCHwN7GfWUOEtT6XBWjG-n4oWlZghB2zclONk3kQ9KQHlW7sSczcCzMai1lE6_lOHKEjK13Y8OL6uRTVmFW0UdEnGjomhnakF-es3_2fMjcWld9hYPbOUCB5pr-e0d8A37ZOhlsUVLX0twvH536_q-j93GszpCQ7v6EctgZgtgt3M-3Ydpjyc0vxfLj8GqvLSqGcMGn9VnGGbyvbxzfIlQ6Vx_mn4-uzd3_g0KZ9t-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df8311ae6.mp4?token=XUKWfVuZ0lDsa1FdJfhaT0-8WzTnxvASM3tcAUgTAUtgM2WIv76ByiYwaJ2FzBrJTUCg2y-JsixkGgRxse3v_k_yMmQTYMczWYz2XFztF0SWCHwN7GfWUOEtT6XBWjG-n4oWlZghB2zclONk3kQ9KQHlW7sSczcCzMai1lE6_lOHKEjK13Y8OL6uRTVmFW0UdEnGjomhnakF-es3_2fMjcWld9hYPbOUCB5pr-e0d8A37ZOhlsUVLX0twvH536_q-j93GszpCQ7v6EctgZgtgt3M-3Ydpjyc0vxfLj8GqvLSqGcMGn9VnGGbyvbxzfIlQ6Vx_mn4-uzd3_g0KZ9t-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی پر بازدید از تمسخر ترامپ و نتانیاهو در شبکه‌های خارجی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/685982" target="_blank">📅 21:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685975">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5ftF_9KJK0SMPHiD6u2ts0jiDl-Gswg8NaEiupq6QVq-BpUQq1gVMrmeWTMeSIXbCMRSfSII_Fgde1pYRfV2bqfAJ3_jzk2e3o_t6jVJ8ZH4VSeorz4-rF9qRXj_--JNUZhKMAcBACnYKsPpO5tHLB0pjwHIlNB_wxMAOH8-9JoPSleO5wDhyKge8XWut8SfTEHP_JoU8Am3EHavPg1nkeGzTBQUchS54vv9J8uTB0DYV8WAvAmErJVB4dh9U-ThC4ostPYTmTTsu5RdzwtTe_MaJONeUk96-qTRJpgMi276PIsc53czDaM2a6G60JB1Me2k5s4H-OMkjW0hnddrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgiCrq5p9OtVkL_AjZGDAVY6w3INt1ygurQTuzeDUpOREsvnUu6MG2vsOqDKR-AEn25vEPAilMWdH2qc3wMMu58rMsSfBKeAeovXYbo_PPkjzm0xL86-pf7KVdjKFbxsCNGhrgfAUhKvA8yiHnDWZF6zfin1wUnLfFICEKWJ26gIC3JhO77akzmsSm0XR_hPMNcWMaGWM5NG-BmzUwvVeXksOtTdQOHOOTYUwT_yX9ISvet844Y4E0VAxu28ZxN_bS1RmLufsWSw5KKJxaPY04S7Wa5zS-sbMBNHtozZSjGxOu52vXRN0n0tbqdzzDmj-gWEJdDhogNeQWLaPMrskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Me0FFghfwNPQDrlF1DABDtQhx3UfHjUuzMHXnZumfyNKcmg86KzTuWU6nepDqN-XkxJx6qWlsIP76uuWIDnVLfhDWhDTJl40jftOUKoDXwnlkNZyQ7G52dFIRicQryuPc8eUMnQq-AhYTOJmGmthCjxWTrPmmYYjCxTBp3GfpM22dQz73Kgk68S8FBoLQJ_4kIcMmKMsY8QxHZQC_yQwU_0LhQ8Kpmch91IrBdZZGbTFTBdwXRmSz1immiQZqylAW3wOVLOLJrHXSThX5gcVkOpORVUWuDzCKn-Mu2XAwMoohJX5kr8QvD1EkuOGEcUIgW9vetPzUqfw7g6QtLjiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GL8vqLSQCKEbhib1UIOf3GKoggUFKfAj0rWxs__p0mNSVR_4Wug1aiq1IReAhL7xQ-Wt74EdRj1X-m2hAbP-SGPQfNleIyYcANQr2YGfyNVHHXks4AqdTQqG_QNWulSfAoXPb9xzVjiJnF8AdpFBLXV4T4CXQ8Bro8Jhq-5NFLeKTMwfXWj2MENz558n755s_Xxf18URLeE9jMlr_PxgHzl7y2fvRTK2hKjOcu0RIll_dnEAd2e5AeKsnQdLG7mkKJH9jFYsHXCeJfu2w6oiIef-Xu7_humWkKll2gXUu2cktqx-mmoO_yzNsqu5JxB2HM7sA2BHkFP9qlqREX8hPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در دنیای هوش‌مصنوعی GEO چه کاربردی داره؟
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/685975" target="_blank">📅 21:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685973">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIKReBOYyl1Fcy5KV6xRigIy0OGW7Tu37j3Il6A1nXpLLHM3M2Ej7xVI3GM568D9xHnADuLrsBb4DfLfGRqOkMTPv8mYgYQkej4rGPJNMhU4lbMRdghs5A2QPV-ifps54_mGUA8MD_hFDE37nUE6vi8ni0aZQuRhfMl0tcyK2wJI9UzdaLdYh8CZDApeGVAAF0ZGekt758J3g8Fyz_yj_9eDb24ugfN1Vt34OyoBz24kKN7zPlkFolgCOwKbKVNWcYOb8Y1fyBiby7zReHtY4ljly95Q5bUuXrsS3Z1QMouty5u-Hs0m2vJhbAwSMw4XYsephSQwTeLiT6pRCy5TuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عفو و تخفیف مجازات بیش از ۲۵۰۰ محکوم به مناسبت میلاد پیامبر(ص)
🔹
همزمان با ایام میلاد باسعادت حضرت ختمی‌مرتبت محمد مصطفی(ص) و امام جعفر صادق(ع)، رئیس قوه قضاییه در نامه‌ای به رهبر انقلاب اسلامی خواستار عفو، تخفیف و تبدیل مجازات ۲۵۷۷ نفر از محکومان دادگاه‌های عمومی و انقلاب، سازمان قضایی نیروهای مسلح و سازمان تعزیرات حکومتی شده بود که حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای تصمیم‌گیری در این خصوص را بر عهده رئیس قوه قضاییه گذاشتند.
🔹
حجت‌الاسلام‌والمسلمین اژه‌ای نیز پس از بررسی‌های لازم، دستور اجرای عفو، تخفیف و تبدیل مجازات این محکومان را صادر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/685973" target="_blank">📅 21:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685972">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkPgzoLPn4iZ4FiyEo4IULwL87CwYj-AwRvHq7l9IC4nfF5L2nGrE1lA-uvQZXqo1dSpEwoKtThow6p2a-YxpLcbdS1JflR22W1Hwq2W_cMy3v_nGGDCYXEcHWYQag9m1kXanqm7Feyf2W_hT9nGPhG7U3ywXgJ3pShlTM4n2meBP2xQi74ww2GsBd4bNl7ILVd4VcbjvAjW6Jit613ysG0UqErJfOY48xtsq99vsI8HAUTlOE3SiNeVJYJwdCwHE5yVBhIm6bggU5ANAknXTpH1JlXLmGZgU9qK30r0Z0ISMv8BgSZuuuSs-SzZGzI32CCeYiCjoinL8VGRfdsDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
🔻
مشاوره رایگان پزشکی برای متقاضیان کاهش وزن با آمپول‌های لاغری
🔹
با توجه به سیر صعودی مصرف خودسرانه آمپول های لاغری و با همکاری شرکت های دانش بنیان دوراپزشکی ، این امکان فراهم شده تا افرادی که قصد استفاده از آمپول های لاغری را دارند به صورت کاملا رایگان و آنلاین توسط پزشک ویزیت شوند.
🔸
کاربران در این سامانه با تکمیل فرم کوتاه ارزیابی، شرایط خود را از نظر BMI، سوابق بیماری و داروهای مصرفی بررسی کرده و سپس با مشاوره رایگان توسط پزشک از شرایط مصرف آمپول های لاغری با خبر می شوند.
👈
شروع ارزیابی
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/685972" target="_blank">📅 21:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685969">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufbNIHBNWej7X9f8m0wxz_k0De27dRhiP1-pRYimA_VTICFBjWigRHnMUQmh8fZHiHpY4IxKBD7lFkOdc9M0XPcUhftot7XNu133QfTKjmXxRKAvle4XdrHufXgLZ6-jc0mVb-XUh8WiOerOao8e-9Yuy1UEaN7LEJH3rkIovlqZVJ0RX_9wjgAVRnP_IJ-C-qhTgy0epuCJ9xFBqW4vBfDEO-Fv8Vx_grlSHsz_ERxOFitzVK1SktxQpAJmNKtj3jiUTnuJW2XF4xMmiN-D5FtQ6hAh6Byk6jcJphjXS6Png1BUZmkDWtDYETG42JF2dNPkSSRiobbApH8Mt0PigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0debb661.mp4?token=YFawJVH3rjgc48R2ogk2NBwTLw4KKkpmzxxOP5HCcOFTCU7ESi6pdb5xerRzy_dY1A7xFbTVtwvjD4_lEjZZXDvTOiz-Ens1PrNjxfebFPbu05hE0oKR3N3w10tcCrlndWazfXjCr980aM9zfvsCkCaMHZKqUaHxS-Ofl8pYDTWvyuCwexyCfrQXTVrWuNbMnCsgF6oaHsbi6dLLoLBLSyqJjSVQo0cRO4zQubNOSXRT7G0kF7g0EUjVIsAEVZIJ6dfSS_gV7AxD5HDFQ2kdZYRIMb1ag6k4QzRkgbLrVlnJp6oeYmhZmz52GhmqZpZerCp0hUOXE2w-NqmTRpKidg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0debb661.mp4?token=YFawJVH3rjgc48R2ogk2NBwTLw4KKkpmzxxOP5HCcOFTCU7ESi6pdb5xerRzy_dY1A7xFbTVtwvjD4_lEjZZXDvTOiz-Ens1PrNjxfebFPbu05hE0oKR3N3w10tcCrlndWazfXjCr980aM9zfvsCkCaMHZKqUaHxS-Ofl8pYDTWvyuCwexyCfrQXTVrWuNbMnCsgF6oaHsbi6dLLoLBLSyqJjSVQo0cRO4zQubNOSXRT7G0kF7g0EUjVIsAEVZIJ6dfSS_gV7AxD5HDFQ2kdZYRIMb1ag6k4QzRkgbLrVlnJp6oeYmhZmz52GhmqZpZerCp0hUOXE2w-NqmTRpKidg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تایید اصابت موشک ایرانی به پایگاه موفق سلطی
🔹
تصاویر ماهواره‌ای تایید می‌کند که موشک ایرانی مستقیماً به آشیانه هواپیما در پایگاه موفق سلطی اصابت کرده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/685969" target="_blank">📅 20:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685959">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyMXljCl0ZrSJsfuCaYXnsT1eb7VIfODC5XN77hqPqBJ2Lbe__ye77PIVDwMuSIvxk_7dxp2O44YsC6Ci1tHyTFesvY7COLQqg60Qe1NfPEgOVDkSWKjzaq0aPnJrXBMBD6XNc6vpB3EI7mRLqqoc0grp7GHmavMPrYmWrYZo5smOV4DuxFZ8-SuDtfXsOLd2aRFHxNgnbC7nZg_4FNC95YQ2AFrx8ahCCToGwOdmB7dJI7B80sPrYgd5c72wxeRsxaolxuCf7U0RN_xIyvJjs8RHdiymAc4ZbYsV0lA_cwBR2rkutyUdpVWS0iRCWcsPZYnciqerT_W3UFi0VDXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2DQ7yto-XnJtVgQ29szjfCEEsjQC-olu-IxM-_7lYFSqXvo-ld-V5__gbDzL3X8rbDvzChxheKMqjcxl4zBkWcd0oQlCnPbQg08sFM23bJG3gAGz8rNyp83ajnzVEdmIJ8FWT4cKws0SNumfaQlL0vd3opWpVNwiQO9FbDcNSWRZY18E2sgEsz2K1HGmbAy0ltnKa9skWVUntFplDeVczoY0RQ7QqB0oiiy4Gn03LLYh-uHI4d5mr2HtqBAMD1Rh641wVPoe_khOcipxZ-p6bl4TewRXwxJjN-hvjDFQZYyOGOCMNXBfTRibB3sM2VGgSdZykKqNb_7tIU70BdhYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBIVvRQrHbIL0i1Rhh5pW52n6CjuvuKAfM6IcLX-wmrulSHt7-jtqcEMmtffLXSU8cPbS_tApC4vtO2gIxG39CX9ysWHFDeco0DBk_j9QQ_UezWhGcxUvUyPdQKOtOXh_IZc_3PDAji1d0lkpkl1a782NzrtKdhhy8DMghN5mnVgVtoYvT0R26ZC4BZYBHo-mMWYo3SaCyDALimEm3SLx0kCNBKWU4FmM4VJXBEwRJi7YjsFKx8cUjqt75-NPOJxlcvfZloV8z01JGpcEzgBLQH6ybvEDTIQtLffJN_RVQnErwpA1hvNJ5kvszlk5AhFD4vBr3IIrou_DjAJm6FfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsVb_hWJsI-K4QUQ3FVRX5jlabUakq0f7-3ZdLz4HNrHwPIfuxB4Y7865n3qcpQkr07BdH3nqYZdqwW4ekZ-KhoXd5S0G2v0MAPIkbUp3HSUbQKt5iRm1yrYrOPhGd71eKxdyR8c-U3s_BYOmAsT6TBx2pTEJf5IjRLLT5rj6346F1rBhwroJRpjhrEzHmI-OsB1eo1Tf7DpD2W5h8SZIzkhykr_WRgAecikskOvHnl0v03f50uSUQ7cBX21gBkl2369c955vQVfGWnWnWea45wKplgtjccYdxHP4FWmWACs2hXCx9tGz1iw_p8KND-PyIoXklbOj-VVkIied76JtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQ4wC3dr_v0E-rC3cJj9qJ_cDd5U26cr-R1nhwRoQfLiUDZpKF0TknmelK1QjLBer4QOGIuCMLVDt4l4YGop8QaOmdGBTzQFbEfCcRbLtMBnB2eb09tcIi4BqcyWG4qROjnhx0S3eYG_vOkreI_cedlAXmBqH5ZrF8WItN-SLgSVC1eVeyUE9gXX81NbW5GUuedUvUSjFGOD7fHt-FGQgRJzjSESWhpRjzjqr0g2jaFS1qPZu6ERKqz8E2oCoZjrKf4q07shAA_Pz2iEc-n4QEnZBWu_Z2mkGx8Kfw9AaHe299KVX-AsrJI7euJJERdOzokrNnnuHeHniPNXtsNiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzwJeyXTWRi9J4F-Gn2y-2JakRTZ6g5UMlvVvoLuoSeQJ2UHyekkMYHkegOvVhiLcZtBoF3NV16rczJwhilGFy8YvOg9Fs1-RT41i41P34iCyCbC3HuT4a_U06GZa0_63IVEIlkMvD5HWO4O5AbFpK_CSxkHSzN8rRG8QEasMlwGtTWuYoIh3B9CN8ZLcDQbkItOINV2D6x84NGM91l5S8nb4EMci3swi1fzqaRmZtlTQxePC_tb_wkLvB9b8D-pwqt1AlS94Kf_QI7eMmVs8Mo2AvuW2psfWZ6kNvaC2mO7ukHcjKpOJU0AM0YTVPm5bM_Un-6KxybLR6VMFdDtIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vt7fhKF2G6U34NZjt2iDYknFTd35FgHbzhp3ceqBUVT0OGuOozwqToRdovjYr1mg5n0M-yuQ-XHfVanfdbCof79JSXTYjfrSwF4eelJvP0AeI3EefUelmNS_D45Pe-sae6SxcAQ8UiQhU6cNKy-vDfrTRU1xkdAZcuChXEboZ4gfv367Q5robvOTE5K2CteX0LlJhIno4uNQ_ybZhB0J5STfKZK5iAGimz-3Th8KeqHibIEcYRGREbUHPDHOYUUJxZecUYy_rKc9E8cbJsj9oYrww_mCL_pZI-XiMC0Rxchh8mh0Wsg-xolU0VtBah2xg6DHE6-sfxoHZePN1taSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXx3kaltZnsT1C-pCkosZH-vlxx3L0v5pIp2YDvXrAYEerikmco_Z6zGDvO5V-yfdysAdsGVxAmGXCvles-PPQN6L6p4y2MgYzZ_WvelUNMv_sx-ELY1AqYWRHk5vNmDHqoiGTJA3BTa8Eo7iPnEmbd1b3uS_wBiiYKl6ohk3KRs1DIpxPDeRuWilOQhZHSicssKFW6VJrBO1pt_AZerJxhj_IKtERRp1MIebYQ3SgpZ74YWevKh4mbM2hnJwlJayzKcCXljijCoKr5CYp9w_0j5YycoEtVc5B4JUaUzpMSCgR3j5mGIbDB-62UkX2XfPMMzWiNfZqgA-QFbnezo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOfCZqEa13wRNEUdJZ6z0WO4UXo8zYpiOd55zRXt9J4M3dIlGsKFi4lZda5wWukUtd3zaVKSTgE2L411r_H2hc_PPAqtwrBaHjMd_WeI4yQIIvZROkKCpU1XWxoGLWoWGmt1mUJsU883Ss-YCplY5vQr2NcqfFtZ7HnMHFBtTC52jL4L2TaakuP0rFVyvmkySrs9LfqOet7giy8X_K7kSsDVSKBP_5RhVLoFB1EktvpzLyu1IwOX9FftVaVQU9koQ6LpvqY7nTW2qJ1BEouTTVjadOUs09RRU3zDk6vdUxMS77mJOOXfKUJzp_NdkC2V05whVn71MTM9AgOurFFKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjDQje4P9A13kclH3VUqrn0fQMYw8cMgGDMlnGoDW50QoV4zMd4o4aL-8Euh--Q8wx2q7UgNpQ5RvSD4af1oUW07FkjyCFJCtmlforKVJCELc94SJARxkOOIU9dSZR9UO_Trqkzj4i4kHcgQuf1U6Q_ITZJtyYZmsWCxzKDaEIc9hj8SHXUgc6mmzPRXAwU4O0SoO6wKTh2JR-LJ5kmce-DLM5HnPq1v6L9R2vZzmvpZGdF5p8PY1pN5JDLwaYozXcrJFuLVdCq3D8zGFmhyjwo7MudaK318FJGUouBpMa7RaMUaGgkhbjq3qqpgLgL2O1IAEnrnLRg33Z-KCpvCDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خبرفوری در الکامپ ۲۹؛ جایی برای دیدن آینده از نزدیک
🔹
خبرفوری در بیست‌ونهمین نمایشگاه الکامپ حضور دارد تا در کنار فعالان و علاقه‌مندان فناوری، تازه‌ترین تجربه‌ها، ایده‌ها و مسیرهای نوآوری را به اشتراک بگذارد.
🔹
الکامپ ۲۹؛ منتظر دیدار شما در غرفه خبرفوری…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/685959" target="_blank">📅 20:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685958">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBh5jm-brI7JLV5OMrdanQQcOM3VAXRsft47JZEbcdy7yvLp24Eefwx9xcKLDZ3reOAif0-X7LStcz8ZrPbDFkQcpDvyMD67dSSd0-T9nh49NfciIIqoveelGy1CnS87cPM73Od99HBNEcmz28Rvl7vAXqWiGsHc7UGD348FCFtsAxe6bCxCPO36T8e5XezMjfa4BGpbzT7LHPm2vtzFbpP6PZy1pOTf-9xPFiBKQn438dYUV5Jo1BatWhUy8-oV1GyFMiwttQvJmOOxALiWTFPy-QxpBTrOPnqLcmjsMgrd8gTTeQYgTnw99OpOFe6vRkTEkuAzbhRdQ6l-SSOFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت به شبهای پرالتهاب/ حمله امشب آمریکا به ایران چگونه خواهد بود؟
🔹
شاید مدل درگیری های جنگ هرمز تکرار شود؛ این بدین معنی است که آتش محدود میان ایران و آمریکا مبادله شود؛ آتشی کنترل شده که نه افزایش می یابد و نه کاهش اما به هر روی، به نوعی میان دو طرف جنگ ایجاد می کند. این درگیری ها مانند جنگ هرمز می توانند محدود باشند و در طول یک هفته تا یک ماه به پایان برسد.
ادعای ترامپ درباره حمله به ایران بلوف است یا واقعیت؟ پاسخ به این سوال را در گزارش خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3241804</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/685958" target="_blank">📅 20:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685956">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPGH2tFxX7DajkBtB075Ue5QYMG3ILKnI5zGGrHWaEayij5EZ8QFIm4LjpyaVGxdGJ0OD0KCCwTdz316HkWRwFzsRAECfaTGunpe3-WqGvSd-8ETkXAk0-D8HJmvxsGJrh62BOOglAXaf1GlJ2WDdOb6RlaxoA3mVmTmLCojrA05XL5gU1fnZoBQ0jWxoYHPQxabXfhHs60GnKcC1Fbx0nOnWhuHusa_XgOOXLRHPERTVHT0Pq66brU-gOoXT-06IupOceL2d0YgQAuNk3mjIeqWie7P1ZQI98ei4-EzES5lSL7o6n_WONiouoVTsnLWOQ4gkSyoA6SkyhEIsdXTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCxSID470QiwIdUwkyxw6ePW0x3LaQfHlQtidKvFZ0hXtBayVWbPibnooI7Nul1soI23b-IJxsggWVm2SgieosYPQbpsudeKjMgohV9mZIwdvqt-96KusojrdVf4VwWcxvEf2nA7gwFLZGXcpjXNYSSCzPLC0L4ZAAjPiWEG4qRwmLUJAAgHns7ofSj0qgCos1Bn4vghcDkjrxjwx0qskGnnxiBkWkKBFL1_Ta0mPKNcHExmU71RC4r_INp12ZsgJ50XYo51r2VrWvhLwKhoAiWtAeoR367gHMRpzHFZBUtmDDSKU5nWOFwYHPuomrpwRrL5_oRdZjej22Zm-9jLwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور رئیس‌جمهور به‌همراه دخترش در افتتاحیۀ مسابقات عشایری قزاقستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/685956" target="_blank">📅 20:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685955">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4f69ced.mp4?token=SdPBBERC5_jsRy6d4dGSmxA9YTGE9IwqGJqn-ZpJBt3ApawHq6XfpiXIeb_-EByI9zVv7NpSZOQx-n__ETqgHkTHCRz4ki5mUOhC1rs-aGKpl5K3oMClbj_fJnZA_9RMoNRDYJFiBlqUpmFZRg4mj-MYgQhKROYN-nAEnPOu_l7mzTmzLv5lRzsnjQexU-mcTxAAmazdtKjEclb9KOX8CUlO24bgNwI99JnuCxFxk4auVANGHsMBgihwFcXguKVHAcLzdNoRravW1DuD9Xy5wiXY0WEtUAUfGB7a_FSZK8qrbDO4T_xDyIzeCQbTifz38S1t5mqwQwGji0YQA_jywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4f69ced.mp4?token=SdPBBERC5_jsRy6d4dGSmxA9YTGE9IwqGJqn-ZpJBt3ApawHq6XfpiXIeb_-EByI9zVv7NpSZOQx-n__ETqgHkTHCRz4ki5mUOhC1rs-aGKpl5K3oMClbj_fJnZA_9RMoNRDYJFiBlqUpmFZRg4mj-MYgQhKROYN-nAEnPOu_l7mzTmzLv5lRzsnjQexU-mcTxAAmazdtKjEclb9KOX8CUlO24bgNwI99JnuCxFxk4auVANGHsMBgihwFcXguKVHAcLzdNoRravW1DuD9Xy5wiXY0WEtUAUfGB7a_FSZK8qrbDO4T_xDyIzeCQbTifz38S1t5mqwQwGji0YQA_jywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
جی‌دی‌ ونس معاون ترامپ: به خاطر بایدن الان کمبود مهمات داریم نه جنگ با ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/685955" target="_blank">📅 20:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685954">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZGR7easugQNFLzrAa5wR90YbRG-rRE8jZd3wUIi2I8FruoXXLzjVlwb1m80HLK8fjtHTmZvaC5eohCvDLhpnWxpIQvfum-EZdMqqioFKyz4B0dSlHQ-Ov1kjmGNOcaLt8Qb5JBMWRhFXLnP-0159EP9Rz6LlXKb_7I52V1g7ne30lSipbRAOPWEpSqoV5TBGMcH5iiU7KLec0cngBYf5d36gBBOQ3QrSlIWIoZZGeBbZZS8CMhDXQWNGEjvgtArPofhFdjby4GEGT_HIRJdXsRDuBQ976ijnh4PucSUXNkWnLZ5XMDVMUKpMVlMv7jEafHljYN6g517B0TRQbaggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترمز هرمز
🔹
آتش‌افروزی شب‌گذشته آمریکا در حمله به لارک با واکنش قاطع ایران وارد مرحله جدیدی شد. ترامپ امروز هم با تهدید مجدد، بر سیاست جنگ‌افروزانه‌اش اصرار دارد. این رویکرد، ضرورت استفاده راهبردی از ظرفیت تنگه هرمز را بیش ازپیش نمایان می‌کند. ایران می‌تواند با مدیریت هوشمندانه این آبراه حیاتی، هزینه‌های نظامی و اقتصادی را برای آمریکا به حداکثر برساند و زمینه‌ساز عقب‌نشینی آن شود. تشدید فشار در این نقطه کلیدی، پیام روشنی ارسال خواهد کرد که هرگونه ماجراجویی، پاسخی سخت‌تر و پیچیده‌تر از گذشته به همراه دارد و معادلات واشنگتن را دستخوش تغییر می‌سازد.
🔹
هشتصدوچهل‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/685954" target="_blank">📅 20:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685953">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIy1bLcX3iTHnvkXXqNo8m-mUwMiN3tcXCZDUjnfVg2C7Z39PaM46dhoTyzey0FuDsjokg3IiutcQUPRxOmJqXYttmxIu_sq6XFNchg6jVpZn41nRxhBv_6VySGQXQE6ErKNP3D-UJKKM-0WnYteT2Chd1okfk3DStIg94pAaOD4SI111egjndy17faBQ6Ovv1CzAb5yPuTWbEi_-1Efv5t1yC9517p5lqwtc21Y20vt9txQEJyPT1j-ij8lnJ10XbMek9eNlaXNwsVn8GJjzHNUFhhF1POpmjzi88-jxxBqXos4Vz-dmTvJEaI6uO5t2ddOQ9fn3Lq3ljHIAAiQow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین انیمیشن جهان، جام سفالی در ایران متعلق به ۵۰۰۰ سال پیش
🔹
ظرفی که با چرخاندن، قوچی را در حال پرش و خوردن برگ متحرک نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/685953" target="_blank">📅 20:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685952">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ناو آبراهام لینکلن در پاتایا پهلو می‌گیرد
🔹
ناو هواپیمابر یواس‌اس آبراهام لینکلن با ۵ هزار ملوان و تفنگدار دریایی که بیش از ۲۰۰ روز را در دریا سپری کرده‌اند، روز چهارشنبه در پاتایای تایلند پهلو می‌گیرد. مقامات محلی ضمن تشدید برخورد با روسپی‌گری، برای جلوگیری از آسیب‌های اجتماعی ناشی از ورود انبوه نظامیان، گشت‌های پلیس را افزایش داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/685952" target="_blank">📅 20:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685950">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c31c441fa.mp4?token=lTrDH8ir9GdO66X1Ld54KdVQOjnPaoPdmksDoXl6aKPIFO2eWu4g3avY7S1z3SaZkC0vSGnksdDQAeoy6PVflEFr3Xet8qklsr6FxvrMYtqtvl3DYOu5Kns8M8KttgRqwPFBA1fbpBIwIZhfBhN5Kolp7EN00ZOvKYqDBUl2DfDmaSSzPsLOCVZsECKKeWNf44nx6qto2OBZ0wu2Okg-_aayCbyTpB6XTnnPDXBEBGJvelmK46QwONcJkdOOqgEY6sMHg0FhPmmGGUk-quF8tI-xxrR79VdRVnBMtA3Ot72Iq5yo_Tp3KF2btVRordlw5iecEFRERbOt0A7zy4k3jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c31c441fa.mp4?token=lTrDH8ir9GdO66X1Ld54KdVQOjnPaoPdmksDoXl6aKPIFO2eWu4g3avY7S1z3SaZkC0vSGnksdDQAeoy6PVflEFr3Xet8qklsr6FxvrMYtqtvl3DYOu5Kns8M8KttgRqwPFBA1fbpBIwIZhfBhN5Kolp7EN00ZOvKYqDBUl2DfDmaSSzPsLOCVZsECKKeWNf44nx6qto2OBZ0wu2Okg-_aayCbyTpB6XTnnPDXBEBGJvelmK46QwONcJkdOOqgEY6sMHg0FhPmmGGUk-quF8tI-xxrR79VdRVnBMtA3Ot72Iq5yo_Tp3KF2btVRordlw5iecEFRERbOt0A7zy4k3jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تایید اصابت موشک ایرانی به پایگاه موفق سلطی
🔹
تصاویر ماهواره‌ای تایید می‌کند که موشک ایرانی مستقیماً به آشیانه هواپیما در پایگاه موفق سلطی اصابت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/685950" target="_blank">📅 20:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685949">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmLydeQnLmAJLDkwRfQ9NpJ31pKwrPBwfaRPnblRaxqVPkDNYtoh-JY779Ge65kFkweVEiCZv_RrxIy8kis6UaErNfEh5rxkujafiWtUb__bscfO8Q7lVP4o0px6evZlrcl5UqaWUTtDioxx2QRbkwDiPeAWyj4GG95gIeRsKZ39WCVA7DRdx0CO9kqvM_P1zd8fFeBg9ViiA-JQe4WQwbwVnI5TsGCCYSagJUIbnRySXB03cWLvU8uY8Eiyr7tqcBp_UHAz1vutMQ4JRJiwH6A23vDDdnaHHZuzuSTP-DQ1JpY40Tz1nymrTb90WJzznoE5JHdpmwdPVv2RB_B6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلیط و هتل رو از جایی بگیر که بقیه می‌گیرن...
🥇
علی‌بابا، رتبه یک همسفری
✈️
بلیط پروازهای داخلی و خارجی
🏨
هتل‌های سراسر ایران و جهان
🚆
بلیط انواع قطار و اتوبوس
📍
رزرو اقامتگاه‌های سراسر ایران
جستجو و رزرو در علی‌بابا
👇
https://albb.ir/idsDnZ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/685949" target="_blank">📅 20:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685948">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riK3MPTWOwzuIWd9WMTP_cexCN7H67VXL8u7p3eRUfok8SPBZZR_b1nOW_maAYmWfU7P397j1hzKjeTjm57RZlBASgdEDK0XzOGvncyvc0FJdxovqsP-uK-BU-_kMj96_L0CY69OTTXYW-Xi5HusfsXLeVnKWq1pm9MJ-cTs_Tu4Dfdy1FSu0PLU8DcdLbscay7EC5X_zF4Sl6Hp1lYFcQGnOaxPnib9G4jx3KrMnwxPdlXqnsKuqsxG-IuR9_pOdGt4WGbY3TYOEXRKDkOjXQ0b5GiHegv1pr0z1E5z-HPMN4w9uu8MnQrTTeM4E2574K_lCWqyqtXsOWC2yNYlmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
✨
قرعه‌کشی بزرگ ارکیده شاپ در شهریور ماه!
✨
🎁
با خرید از ارکیده شاپ فقط محصولات باکیفیت و اصل برای خونه و مراقبت شخصی‌تون تهیه نمی‌کنید؛ بلکه شانس برنده شدن  ۶ جایزه نفیس و کاربردی رو هم دارید!
😍
🎉
💚
کیفیت بالا | قیمت مناسب | ضمانت اصالت محصول
🎁
۶ جایزه ویژه برای ۶ برنده خوش‌شانس
📲
برای دیدن محصولات و دریافت شانس قرعه کشی  به ارکیده شاپ سر بزنید
😍
https://t.me/Orkide2025
https://t.me/Orkide2025</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/685948" target="_blank">📅 20:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685947">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccf957497.mp4?token=Gxa8K_QLasPfmySVqQMfYaVk3VlK1MiGs7FuVh1i1D27ssqv5R4eo4f-L7opI1Zq78dQtbJ78PZJtpP4N6_wuSH9T8p-RDI-al3AiqZPrD7Sy_QKKu53yXFMcm5gV7Lu_bhlhuRAAN6_d4HdLL3ipwLohR-t1DLD94ESnlXxg_bkMR0w7Zg9oGNxyYyQQuVvCFRlFixtZXexNKH9JDxCfuaIU2ZKaGfmOtk2u0zl2SVkoPt5lGtzVe77yXSSdPs2tBG5L2TpUL2sbzTiZdAUk31zQ4vYsrlHD6R9sssfxnKpxa1eiIxnEspjxkCUZRfEBN5jGY1pWoGhf0M5LLyfRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccf957497.mp4?token=Gxa8K_QLasPfmySVqQMfYaVk3VlK1MiGs7FuVh1i1D27ssqv5R4eo4f-L7opI1Zq78dQtbJ78PZJtpP4N6_wuSH9T8p-RDI-al3AiqZPrD7Sy_QKKu53yXFMcm5gV7Lu_bhlhuRAAN6_d4HdLL3ipwLohR-t1DLD94ESnlXxg_bkMR0w7Zg9oGNxyYyQQuVvCFRlFixtZXexNKH9JDxCfuaIU2ZKaGfmOtk2u0zl2SVkoPt5lGtzVe77yXSSdPs2tBG5L2TpUL2sbzTiZdAUk31zQ4vYsrlHD6R9sssfxnKpxa1eiIxnEspjxkCUZRfEBN5jGY1pWoGhf0M5LLyfRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رازِ پلوی مجلسی دمکرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/685947" target="_blank">📅 20:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685946">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTVyYF7ptexpagItclnEmQDUENFRxI_vMfemozR0hz1L-dx8nOk2aUc_s3-zxOIYgJVQ6-bYw4XrxWjt3ff6B70JQuGXr65EipLHBEF4e3HfExNL3N_W8WJGV7dN-dTtWRu6tET6-GVllmnuJHniGkpwTYWsyll03hD6ljYB9qC1Bo3ya6Mxe5LF80kwn9aAeXZomu-lms4xXKDpx72Bf5Mq76w1V5vKrn8LGR9T1U_sohOTWknw8UczY4sHdLF9Yh-GTPyWsDh9vqtah0LJsfXJ53S9KLAFFnsHiPmj1Fot1V8EkA43loRY8WZ4D8CdWV5D_xzxkdfBsWs2ai9HtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناکارآمدی بیمه؛ مهم‌ترین دلیل کاهش بیمه‌شدگان از دید افکار عمومی
🔸
در این نظرسنجی بیش از ۱۸ هزار نفر شرکت کردند که سهم روبیکا ۵۶، بله ۲۶ و تلگرام ۱۷ درصد بوده است.
🔸
حدود ۵۲ درصد شرکت‌کنندگان ناکارآمد بودن بیمه و ۱۱ درصد عدم تمایل نسل جدید به بیمه را از مهم‌ترین عوامل کاهش تعداد افراد بیمه‌شده می‌دانند.
🔸
کاهش پوشش بیمه‌ای را نمی‌توان صرفاً به بی‌میلی افراد نسبت داد؛ هزینه بیمه، دشواری دسترسی و کارآمدی خدمات در کنار تغییر نگرش نسل جدید، به چالش‌های مهم نظام بیمه تبدیل شده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/685946" target="_blank">📅 20:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685945">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
زلزله‌ای به قدرت حدود ۵ ریشتر هم‌اکنون یاسوج را لرزاند
#اخبارفوری_کهگیلویه‌وبویراحمد
در فضای مجازی
@akhbar_Kohgiluyevaboyerahmad</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/685945" target="_blank">📅 20:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685942">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50af0cd4c.mp4?token=hFwnhNxLoQS8qG_Mw_52dcBBzn-ThmAcRGjo5dzm1OxsEQjh01mMWqEk4NrfYXPL8fbnVisSj14IzDF35LHDj-75bXLna71UP1-HPIKskgWwx_Y1X6HzqAtojBZIqGgkCvRhKDZfdKxTOhyzXx3vGf7y8_uDNOAhxHVZW_i-0N8Y8dBu88i7_ZpFp6HoNuc87nPNazkaqj6cfoMCgMaP4xX8e9w6dDkwEmD8mW6dEgN6tJpkf77uB8kthHlIhYbafLTvVgtPGgJtOUtwrkkjrnUnQd0L4YiDXkdJNHm56yR9IzcaPi0sVaAo2oB4pWRFLShu8t_nDUX2mjVGJvtwdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50af0cd4c.mp4?token=hFwnhNxLoQS8qG_Mw_52dcBBzn-ThmAcRGjo5dzm1OxsEQjh01mMWqEk4NrfYXPL8fbnVisSj14IzDF35LHDj-75bXLna71UP1-HPIKskgWwx_Y1X6HzqAtojBZIqGgkCvRhKDZfdKxTOhyzXx3vGf7y8_uDNOAhxHVZW_i-0N8Y8dBu88i7_ZpFp6HoNuc87nPNazkaqj6cfoMCgMaP4xX8e9w6dDkwEmD8mW6dEgN6tJpkf77uB8kthHlIhYbafLTvVgtPGgJtOUtwrkkjrnUnQd0L4YiDXkdJNHm56yR9IzcaPi0sVaAo2oB4pWRFLShu8t_nDUX2mjVGJvtwdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیونل مسی از بازی‌های ملی خداحافظی کرد
🔹
لیونل مسی با انتشار پستی از فوتبال ملی از تیم ملی آرژانتین خداحافظی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/685942" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

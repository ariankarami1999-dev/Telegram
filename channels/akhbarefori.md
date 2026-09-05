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
<img src="https://cdn4.telesco.pe/file/MwFTyyjH0Nl7IleWE3JkE1Nw6GCSCwsrt3WLeGIpKV4MtrxrxRhrMU-xrnNI2L-DzgUOvfJgoh1FXJVncpIU4FTqBXhZN-OAJs2tczfMEKnx9Y_zGhxfvSzkR3Zwf5v7fliZ1_fUHvhgiZCitYWfLL8FmDcJ7kwmkgGw7Ey22XdbAXHtYBlo1YrpuPvnFEH2ppOH57s38TuM0ZbUmApfhzuGHhCLXiy_B7qPNE9wqzB7jcHuoYg8vNtQyMhcztB8UPbDq08VgkWb68X5sE82Pe3iewz4mL57DH8bBVE7cDDKqgyN_oodlVpp9JSsZBoXZsH_io1I0gBmNYsKxSyyvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.42M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 17:26:02</div>
<hr>

<div class="tg-post" id="msg-687421">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-dlffEPNSxuMfw6gbNjx25jnS6it0Rj-y5XMUwwI-Yd1c86LJNkfA_C6aCkeTLp89Tei6pGTgKLF5DWZ3F-3Pk9zqltxq-F-pMy_GF3bCPtZhhVyA4dW5ACtG64rMWQu8I7u14SxUi-pYt0dY7Q2CN8d_1sFCTi73GORvl7SIJ6Dg2CqGr6l-R2b7sHOi-AEYUxsmFRkV4SsucNAoNgR9O8y5iIGAWlN8TwxGRC6_czMxJUwlmO0fPDiAc49ZIQP1tvfOvxBTpAgnmhZ21hmJ9MLU12P_wfzm-zlVDjn4s5nO433HZgiy8djXoVf2KL5RXFmZMx97yjbhaYl-aV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
سنتکام: نیروهای آمریکایی سه نفتکش نفت خام ایران را هدف قرار دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/687421" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687420">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
راه‌آهن: خبر توقف انتقال ریلی کالا از چین و روسیه به ایران کذب است
راه‌آهن جمهوری اسلامی ایران:
🔹
ادعای ممانعت ترکمنستان و قزاقستان از انتقال ریلی کالا به ایران به‌دلیل تبعیت از تحریم‌های جدید آمریکا، صحت ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/687420" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687419">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای نتانیاهو: سؤال اصلی انتخابات این است که چه کسی رژیم ایران، حزب‌الله و حماس را نابود می‌کند؛ ما این کار را انجام می‌دهیم #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/687419" target="_blank">📅 17:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687417">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTWMTOY2QjVwMEDk60UOkQxZTo7MRgIe44RLtnl1sAxvr6ipzCoYzC7vfd3x7k3t-oe0LUL2pY4mZkAbE_oKp7txsysm1RPPtW5cuzp6o83w-l3hf3gZZfIAdAuEB8Q10g0mqH9_UKFqsL0iSK_luwT_39bTW6XKE0xSlTi-tdlFyHrKuz4tYn_6q3ukIsb65Z5bTWbAquMG92zj4YOfkVGPUWhB3wKNyJlqE7z2AWBXbbVD3Fcg5NUieAvM3ejVIXVIvl8SiZx7F-T9Rx6-zS9a2YHA14iwjbEYmMKiFYfl7A6xHDsjArwva3nAELk55Pp_2W7DAA4XnA6t3rNq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8vEXQS3G7pTLUMM5HLwF2bQDZiPkc5GrBQJIJo1KumIRNHV4xEqWjB1oAv7tbvjV1_LERaT9pl-P7sb2kimdvbEHSM9vNIBcH0oxeuFtGIQrxOfDMJI7dYAZG7aOQpgcRog-XsrSwhB1q2f6xzYn1k_HgyN7Fk8yFWtXs_PYlh8ubYwEvmGUZg55-gG9XH2rtJkYk6skBX7lKKZFW7gMg3DghFzds5vdh6uvMACKPpecZw3BxU8KlZpDHIRCXGbJpB_mXimUFrFMOgtdr1AYS0saNc7u4NJl_-lectZC9co-msbiJM3U_2yg9oVP0hahQrONEJv9dAQHwSFTmF-FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نظرسنجی نویگیتور: جنگ ایران مهم‌ترین عامل پشیمانی رأی‌دهندگان ترامپ
🔹
طبق این نظرسنجی، ۴۵٪ از رأی‌دهندگان پشیمان ترامپ جنگ با ایران و سیاست خارجی او را دلیل اصلی پشیمانی خود عنوان کرده‌اند؛ پس از آن، گرانی و هزینه‌های زندگی با ۴۳٪ قرار دارد.
🔹
همچنین نارضایتی این گروه از عملکرد ترامپ در زمینه قیمت بنزین و مواد غذایی به ۸۳٪ رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/687417" target="_blank">📅 17:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687416">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa895fc11.mp4?token=KNnZFG4SSJaNHEg4J2JdzdzUly9mqHLTq9_C5byqUTsOk7PABZcnnzaVhadLYyNcdeYeYV5kFm5Ndo5XMDb9Jdo-i9B5hLODUG0tOTSfIj1QqB_Aq6Q9VYFStPET0F0K0pul1o7uVnohXQRfz4eE2T9i476KV6pZxkdWusE2WIXmpOGMQhnOeKOTAjdqCsvbdyWWlD13Wge0xiU_EgwzrTfGytv_ozpyMeek46unJbwyARq9tnXH8Fnh5BBiJG8zl9sxdZXFIVVtHDyVWrOaKmNcZHPNnOgJuAA06uC5SvN7NR7QWEDvqoxdODDvt3V-HcbB5aFOa25SlSZBcQ4LnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa895fc11.mp4?token=KNnZFG4SSJaNHEg4J2JdzdzUly9mqHLTq9_C5byqUTsOk7PABZcnnzaVhadLYyNcdeYeYV5kFm5Ndo5XMDb9Jdo-i9B5hLODUG0tOTSfIj1QqB_Aq6Q9VYFStPET0F0K0pul1o7uVnohXQRfz4eE2T9i476KV6pZxkdWusE2WIXmpOGMQhnOeKOTAjdqCsvbdyWWlD13Wge0xiU_EgwzrTfGytv_ozpyMeek46unJbwyARq9tnXH8Fnh5BBiJG8zl9sxdZXFIVVtHDyVWrOaKmNcZHPNnOgJuAA06uC5SvN7NR7QWEDvqoxdODDvt3V-HcbB5aFOa25SlSZBcQ4LnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
سامانه پیامکی گزارش ماینر و برق غیرمجاز:
30005121  _ 30006121
📌
استخراج غیرمجاز رمزارز، یعنی مصرف برق یارانه‌ای برای سود شخصی و تحمیل هزینه به شبکه و مردم
#قاچاق_برق
|
#برق_پایدار
روابط عمومی شرکت توزیع نیروی برق استان تهران
🆔️
http://ble.ir/bargheiran</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/687416" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687415">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB90gjInEhEZfu_BhTOvDVtBSbM3FMmqbSyjcfnaJ0Bl0aZLrxCsNv2YvtL7NpF7JoNTY55q3UbqNmb321LqhRFoEhA7ocjqYax5WlmguwjwnMw00OWTriGyowqjLu4NP5qago2abJ4okqh8sVpJUIcifHVdRWuFxtv_xgquovd-gOt6dJji8mvIUYCvgYgX2qqQfuDEv2T2aJbWkSdQxyLxRTlmoz0SM6au_5eSFK0WcWYiILD3pj9URyFxLmOrhmEvCcF884Kp2NLSFHhZ36xeH7VeIAvkfiUrKSwWVJCyjJpunPL28yhG90mQuU8R_saqzU4VhVnS_uwOP_el2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبینار رایگان «پشت پرده سکوت مشتری»
مشتری جواب نمی‌دهد؟ شاید هنوز فروش از دست نرفته باشد!
🔴
خیلی از فروش‌ها درست جایی از بین می‌روند که مشتری سکوت می‌کند. این همان پشت صحنه‌ای است که که باید ازش خبر داشته باشید.
در وبینار پشت پرده سکوت یاد می‌گیرید:
🔹
چرا مشتری‌ها پاسخ نمی‌دهند؟
🔹
چطور بفهمیم مشتری مردد است یا علاقه‌ای ندارد؟
🔹
چرا پیام‌های پیگیری معمولی نتیجه نمی‌دهند؟
🔹
چگونه دوباره گفتگو با مشتری را شروع کنیم؟
🔹
چطور مشتریان خاموش را به مسیر خرید برگردانیم؟
این وبینار با تمرکز بر تکنیک‌های عملی فروش و بررسی موقعیت‌های واقعی برگزار می‌شود.
📌
ثبت‌نام رایگان
👇
https://survey.porsline.ir/s/HnTcBfTL</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/akhbarefori/687415" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687414">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
جزئیات اجرای حکم قصاص خواننده مازندرانی
رئیس کل دادگستری مازندران:
🔹
حکم قصاص نفس متهم ۳۰ ساله پرونده قتل یک جوان در کافه‌ای در بابلسر، پس از تأیید دیوان عالی کشور، هفته گذشته ساعت ۴:۳۰ بامداد در زندان اجرا شد.
🔹
درگیری لحظه‌ای و بدون خصومت قبلی بوده و پرونده با استناد به فیلم دوربین‌های مداربسته، نظریه پزشکی قانونی و اقرار متهم رسیدگی شده است.
🔹
اجرای حکم که ابتدا برای ۱۸ خرداد تعیین شده بود، به‌دلیل ایام محرم و صفر و با هدف جلب رضایت اولیای دم به تعویق افتاده بود.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/687414" target="_blank">📅 16:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687413">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
جزئیات نسخه تازه مصوبه مجلس
🔹
بر اساس ماده‌ی ۱۵، همه‌ی اشخاص حقیقی و حقوقی ۳ ماه فرصت دارند تا فعالیت‌ها، قراردادها و ارتباطات جاری خود با کشورهای خارجی را با سازوکار جدید تطبیق داده و در سامانه شفاف کنند.
🔹
تولید اثر هنری بدون مجوز از نهادهای قانونی کشور،…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/687413" target="_blank">📅 16:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687412">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJMXf-EwZFiPkZZFjd7oyF25wwhXp-ElNWKw6Ps4YsM4RjG2TjTvpYHBdtQFjxpbsuCB50mJ7B2r9opuWeaamLAqJw6HMczq409XvygL0NrUKcKsdWmO7qCY5n3RcuZWI-kZgzExVRDRMBDKuU5DfjD-ILxq8MlXV_8HYWVkCnhppMKyV32WJWH3vZ97GT2gc46rb9kxhkukyFg0MT8MlKNfxmJZM2DweCfU45yuKZ5IEUIjQPYehFoCRKXY0gZWN_QOYWYjoK5HnUZgsrT30qx2QUIDKUUiFfTWmrbBzgs7vixKzXXM46PevvfWYvVgtt6E50OlBor8QDFZWkB4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلی بر حال و آیندهٔ صنعت فولاد در جهان، خاورمیانه و ایران
🔹
به قلم امین ابراهیمی
🔹
مدیرعامل شرکت فولاد خوزستان
🔹
نایب‌رئیس انجمن تولیدکنندگان فولاد ایران
🔹
جایگاه واقعی فولاد ایران در معادلات جهانی، بسیار فراتر از تصویری است که حتی بسیاری از فعالان داخلی از آن دارند. آمار رسمی انجمن جهانی فولاد برای سال ۲۰۲۵ گویای این واقعیت است: ایران با تولید ۳۲ میلیون تن، دهمین فولادساز بزرگ جهان است و علی‌رغم تمام محدودیت‌های انرژی و فشار تحریم، تولید خود را نسبت به سال قبل افزایش داده است....
ادامه گزارش
👇
akharinkhabar.ir/local/10995391/
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/687412" target="_blank">📅 16:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687411">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgzSeezY1rxFlfDCValOSKFh2OA6dZ150VMBuI-tjNGP6kwGUF93yd4liNTw5MCtFWMIRwTx2Gkn3jZXBoEeGyJKvBLMwPvFZgt8mn1CEQOPt2dlVWLyEC6O1RTpSwcttKFJgtcWhodFt8gs4uqCqbwOvnH85PjuNEwFFEI6cggZLs32ebePaMx7lKVRdZ1HIs7PjahssPuy-h3GkG7xlXuLgbEmhbMqLjGJQt6sJDwD3ezW2Y86aiD-IjPWI2tASBDF2ORVGkQ5wLvWRYfYEsQFjP9Kmtpu_eahEMFkBRFjGQHnIBpeQQjcdqnNygLeCuPsdRzjRhDdQWeJ6N_2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصطفی طغانی قهرمان کشتی پهلوانی شد
⁣
🔹
نماینده ایران در وزن مثبت ۱۰۰ کیلوگرم کشتی پهلوانی با پیروزی مقتدرانه برابر حریف قرقیزستانی قهرمان بازی‌های جهانی عشایر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/687411" target="_blank">📅 16:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687410">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXvXvvKU4g9Z51lI-ks7ntzev8f0PLeOV7-78GvKIh2r3DQH52LTzh5VJLptfMr8XELh0EExiUr5jpA3cfAWtd9dkZgaSQdi_ILmAVPwppsSsKU8uJVXqdMAVhR6HuldZeWfG36cmZFIckFpARDCs7f1eDMJv1glfWSKTRyObcz-Fw4JM5_ahKiXJoogcwe4V5VYKonK3c-8Be2Xs81-mlViSjS6iYuMbB1nDnl_B0sXQLzcE7AnqWps2ZcGOdY3IK9OvTjI8MIzEvB3KkGPkI8FTrObj-Ftnr72mbaLfMY-JyomJJmxPEZK6RsjAR4f28MFVEMqMpltQTYLALJllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پراکندگی جمعیت مسیحیان در منطقه غرب آسیا
🔸
بررسی داده‌های مرکز تحقیقاتی پیو (Pew Research Center) نشان می‌دهد کشور قبرس با ۷۸ درصد و لبنان با ۳۱ درصد، بیشترین سهم جمعیت مسیحی را در منطقه غرب آسیا به خود اختصاص داده‌اند.
🔸
حضور درصدی قابل‌توجه از مسیحیان در کشورهای حوزه خلیج فارس، عمدتاً حاصل مهاجرت نیروی کار بین‌المللی به این کشورهاست.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/687410" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687404">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6MS8Vr8B773unUKoj0k5FSOradpn0UXuPF_gIY8zCzR5hdc7c6IM1LX1Y6GILkGaQ-sdFW6FG4F235Z42UQuN4-n3dW6inSLBj-EJjQFf-CFph2k1JGjgb7fy_jWLWjt6GtFgHV4Z0AsuTyGJXfhPO6CI5oZ3ugKfzd9bwdBzB9xHz1GxQ8t7JujrgYYYaSi1Ef0gYPQPgYNTO89FilZP9Y3eZUGJdhMf2w04LbHXe9_jlPIsBEe6RbUFKeIg36MrUeeVfmq1_MVlsIDuCscIbWgCz4-TlBah-TfIb4lWJTDhacxplOFXFxFEyNwHJEai01YjLtxajqD1gCOf9rIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFvRns4gZuONqGswCZPty6SzmOwlCyk-X_qmEZg_P6KaOetI7qS1XC6LckYRe4TKNIwb5_ZHM0GOforcNHbBmjT0i9_p548Oc0ShsUZAgM5tCpHS9eNxf0rlAf1llk9hPDvbAwxObrWRnNH0dXqhjyOS5v5HwjjIRq896A3EbqCox8KYCGLBMh9gsXPLa34M9ofTUyYLDB6K9mV9uhbt9o-ZC6fZKJ8YmsHvzp7L2B-arZj4bTJYESBvP6Rqaew1t-epw2VpTyip9r2eNC0_62zfZhNtGgrbYRGp_8LOr8gBZkB45jaTtDNwv5eHxs_wSyMJCEG2iHkcYxG7Jke0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOJ3yPxKBQbGlY1Nr1RFrunzxkfJNmPGf4-Oz4tUujwFd5_YOw7e4OkCzgBQaVjw4pw7cGtDqo_8svWreXok93OsoakfZCAPcRJWLv5ARlyaNKajs035n3BsH0xpRX0QKPhTTCUxbaBxBjvUV9VKu9CtyNv_BkZV2Z4Ui3OxpXoMFUErmgFKT2vtZPUOcOPYJg1867efB725A1eZIwKzcSOABQMG9iCrOUd1xREFo5zcVdmV-COYdpGs2oljsisksuzOCLzfl-UyQif5Q2myhGVqJq9LIDkRZEM4d3tsR_uHLYixbE4r-Vkdps7ozlFKGyjE6lQmSwH6yBxglDRRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC_f5EcCjHvO0U8Kbq6DzSb3yiEJ2ZDZC6lryUUGMhnRa0C6n2ZZ_CW-m6AyTdzCpDqCR5-xUIV3RLrfVBDMhhkqwRV23bB-i_7ap9UFb3d7f9eMUUQKssatStzYBU3hTvb_jW9DB5mzfGeuoI-GWe0-n1y4TLHRLkS3b-9D1cOdP_HHdJ88VmASoZ4g_zWj4SaVepVJ-Coi6Xwe7gWmoHO4MbzpA4HLfzm3zmP9-YqsL4uSN7yH2aNkJ2bStPadcmmwNpeOdp_BkgemWZDcISh82ViPG7awhIpMTOShDsfURB5vFNdp-Eb3GChmQwSaYIVZl7M2VMexTUov0Je6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFtEzsGUWi7L-YVYqLm1OuvbCX0TRPB4xgfLAF8uGDyOxfHmrVnUvutLSs_FtGMNWvwFysz1zCoLDIlMgKVKZ0tuQGbkPN71y8YkBM-_Is67p1vNArHm0uuE6OHIBgJeC2D4tOc5i1QJ0ZRsffLHiAwSEY8Ibkwdri6IyU47rvDkPsPEG8jOLk6zHAcQVCB766HhoZeLd-vJ9fk_2hv2mFN5H7vHjjql1dEN_eAA9WTNZkaP-xronbk3as3Wn4zOhQ8UPsXA0cD-NQ2oxRMFZdjmPt-s-qdaaskd-KU8CX6VDdAMxnht2ntbZ67cJgo3fyp28RU-9DCy819voP1W-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4GTLUN2tor76GwPb5_W3a-u3W5ktTNua_86fw9ny521bBlCxCz8-oqDgyoGGjrFwm8KrQfZ14ZGzGmG69au8mANN47x7T6XlmRd2VAAc-I7AUF2saxTb2ZqMsUb6ADBEdB7oXqDNl3sPZ07Nrzph_T50mXmfBOH0fpG4S_cDlSNLpkDbTcKA71oc639uaj9-xfceBOIHL_LgSC3q-7c9PF2v-xT13xw5OPTerYW0IxWxOGzpPIrYSfQOS5H9WOf3OHLMUDs2WBk7a-DY60e8tDt2b_gR9GrszAn6uFKpBhs80L1ChN7PbbFe_vPX_9dE6YsVzgAKsU-20wqVagWmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چطور با ریسک کم‌تر از بانک دو برابر سود بگیریم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/687404" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687403">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دستیار رئیس کل بانک مرکزی: با وجود محدودیت‌های امسال، وصول ارزهای نفتی ۵۰ درصد بیشتر از سال ۹۸ و ۹۹ بوده است.
🔹
سخنگوی آموزش‌وپرورش: از اول مهر حق‌التدریس معلمان شاغل و بازنشسته ۲ برابر می‌شود.
🔹
تجاوز جدید صهیونیست‌ها به منطقه وادی الرقاد در حومه غربی درعا در جنوب سوریه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/687403" target="_blank">📅 16:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687402">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eb32a6f8.mp4?token=XXV9u75OYqh0VWt2I9X5LcCclbVfQE4ZNQibICF4I75PIzRM5u1FXLA4NwZkghWd4PX21mU4DAjlN8MawNhZ973tBtrJdqyIz-PgUvRAIsTe8IZSrjdi6jzzCdTSlaEfrjbjwjtn2wg0c_1VcYN1-kXV1xIifIhYiBnI_3Y4-duegFyr1K4yqFk_6Pw7wR0Kj3pjYL-dlVgssV8qmbXhK34ZoO-zJ-qYB-UOuoOTPq0nV4GU-CBQ-lv_44xjqtCR19EuP7kK3A9xxwwsq1-V_nJ-62GpoNv07j8TN2Aqnq3SSU641qq8rQ9dmodPI-zD9Uq5rZov1nXxFDsQworHxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eb32a6f8.mp4?token=XXV9u75OYqh0VWt2I9X5LcCclbVfQE4ZNQibICF4I75PIzRM5u1FXLA4NwZkghWd4PX21mU4DAjlN8MawNhZ973tBtrJdqyIz-PgUvRAIsTe8IZSrjdi6jzzCdTSlaEfrjbjwjtn2wg0c_1VcYN1-kXV1xIifIhYiBnI_3Y4-duegFyr1K4yqFk_6Pw7wR0Kj3pjYL-dlVgssV8qmbXhK34ZoO-zJ-qYB-UOuoOTPq0nV4GU-CBQ-lv_44xjqtCR19EuP7kK3A9xxwwsq1-V_nJ-62GpoNv07j8TN2Aqnq3SSU641qq8rQ9dmodPI-zD9Uq5rZov1nXxFDsQworHxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط جنگنده ساخت آمریکایی در یونان
🔹
یک فروند فانتوم اف-۴ نیروی هوایی یونان در جریان نمایش هوایی در شهر «تاناگرا» این کشور دچار سانحه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/687402" target="_blank">📅 16:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687401">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8srnJoZ5uMLLPjvsvOUiep7pDzAfvHh1uJZBG0SPDhaxXqgqSqcFSl9hCKq4m0oFr6SG4l9zTt3ejPQZVRArfkRMfkwaq0hBffzNtTpVbBYXsJTbzIVDXzaJpq4sBrKsWY8nInlRLZFN86RW-mOLInU5MNS1_Dq5QGFhDAsQE4Jw17VEuN_b6LIS8XycitMjejsvYxjXcfFzg2G6V2OEY2251fj2uNYebLoJjIbu2PjNjNSM7oq7W2B21SHrJ93jMQMs2gAwR_iefd84lFSMxLpTsTaHUIvLLe8suWfdXFowT8pxEde7uFwE5U2lE2pZOz6CXex2LUcfpB4GsPXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسخه تجزیه ایران روی میز کنگره آمریکا!
🔹
روزنامه صهیونیستی جروزالم پست در مقاله‌ای پیشنهاد کرده است که کنگره آمریکا با تصویب قطعنامه‌ای، استقلال اقلیت‌های قومی ایرانی مانند کردها و عرب‌ها را به رسمیت بشناسد و راه را برای تجزیه ایران باز کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/687401" target="_blank">📅 16:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687400">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8aedc93b.mp4?token=TnaHhul7pPs5B-cG0rShDtBvRawBCToNT0uHo_73P6xa4Qp31A-LCLHcqu_cGWjk75JLuTPHXLGMPEiLWUUkTXUqf3UhDcedwJz_eCIeVZLNZD1qtZMDL3Cco7m9jUNLE0-vNvEt5Uju19pR3xAFsiYVUodFUrZ0MuVlQihDQFQD4e-ScTpWZFpykHVFBcMQT78bOB1RnW2SYSu0-ypycoJVfehFFShfglRpie3HcfGtn_0nCRlLi0hIyc-7PhR01s1I1bMSQHuUURMByRYI1wyYEEjEzgQWugWP4pN9LCll-3IYPVXg-A5hXvgemmAcvn_F4VEwRj5oaIAauq3l0RGnZ7MMTcS40Bt26y-ZbRb_zcl8YOmmiM6v-3igSXEED2YZ5EhiOqdE7kTDXISUMJuME2Fu1d9dCzOeiMaRJ-NvDuSS1irRJfrK6ZfYXNpcQ-46kbN2OEG__8BiQVPIr4Coaa94pGOjw8kvfXePO4pqMcbUeeeYmE5kv1HusZrFtMOmi8aKG3GQIHNkofxbOnT0fl74_hgC9JoKPkzH_jLti4VFT_QY71ilcY5fWz-QPmf0L5B_ZFJIj8cI0iVIGO5bp8fnu2j_u-H3VQvFzqbxM45jox58j1_6s02_zaWUiamFuwnsPoEKqEciOqakUz-WPnMkRJC-Q-wr1ZyKj1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8aedc93b.mp4?token=TnaHhul7pPs5B-cG0rShDtBvRawBCToNT0uHo_73P6xa4Qp31A-LCLHcqu_cGWjk75JLuTPHXLGMPEiLWUUkTXUqf3UhDcedwJz_eCIeVZLNZD1qtZMDL3Cco7m9jUNLE0-vNvEt5Uju19pR3xAFsiYVUodFUrZ0MuVlQihDQFQD4e-ScTpWZFpykHVFBcMQT78bOB1RnW2SYSu0-ypycoJVfehFFShfglRpie3HcfGtn_0nCRlLi0hIyc-7PhR01s1I1bMSQHuUURMByRYI1wyYEEjEzgQWugWP4pN9LCll-3IYPVXg-A5hXvgemmAcvn_F4VEwRj5oaIAauq3l0RGnZ7MMTcS40Bt26y-ZbRb_zcl8YOmmiM6v-3igSXEED2YZ5EhiOqdE7kTDXISUMJuME2Fu1d9dCzOeiMaRJ-NvDuSS1irRJfrK6ZfYXNpcQ-46kbN2OEG__8BiQVPIr4Coaa94pGOjw8kvfXePO4pqMcbUeeeYmE5kv1HusZrFtMOmi8aKG3GQIHNkofxbOnT0fl74_hgC9JoKPkzH_jLti4VFT_QY71ilcY5fWz-QPmf0L5B_ZFJIj8cI0iVIGO5bp8fnu2j_u-H3VQvFzqbxM45jox58j1_6s02_zaWUiamFuwnsPoEKqEciOqakUz-WPnMkRJC-Q-wr1ZyKj1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس الجزیره: چرا رواست که به ایرانی‌ها گفته شود «علیه حکومت خود قیام کنید»، اما غربی‌ها نباید از دولت‌های خود انتقاد کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/687400" target="_blank">📅 16:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
نتانیاهو: خبرنگاران محل اقامت پسرش در آمریکا را لو دادند!
🔹
بنیامین نتانیاهو نخست وزیر رژیم صهیونیستی درباره ادعای ترور یائیر نتانیاهو، پسرش در آمریکا، آن را اقدامی واقعی و جدی قلمداد کرد که به زعم وی به دخالت نیروهای امنیتی و نیروهای کمکی انجامید تا او را به‌سرعت از آمریکا خارج کنند.
🔹
او در عین حال افشای محل اقامت پسرش در آمریکا را به گردن خبرنگاران انداخت و مدعی شد: این اتفاق در پی اقدامات غیرمسئولانه تعدادی از خبرنگاران و افراد دیگری رخ داد که مکان یائیر را لحظه به لحظه فاش کردند: آدرس دقیق محل اقامت او، تصویر آپارتمان، شماره طبقه و شماره واحد.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/687399" target="_blank">📅 16:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687398">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
قیمت مرغ کاهش یافت
🔹
براساس گزارش میدانی، هر کیلو مرغ به ۲۷۰ هزار تومان و ران مرغ به ۲۰۰ هزار تومان کاهش یافته است.
🔹
وزارت کشاورزی اعلام کرده نهاده به حد کافی وارد شده و بخشی از آن توزیع شده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/687398" target="_blank">📅 15:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687397">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ترامپ متوهم: ویتکاف و کوشنر در حال بردن پیشنهادی به مسکو برای پایان دادن به جنگ هستند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/687397" target="_blank">📅 15:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687396">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
حزب‌الله: تجاوزات صهیونیست‌ها با سکوت بین‌المللی و انفعال دولت لبنان ادامه دارد
حزب‌الله لبنان:
🔹
دشمن اسرائیلی همچنان به تشدید تجاوزات و جنایات خود علیه لبنان ادامه می‌دهد؛ کشتار، بمباران، تخریب و انفجار سیستماتیک منازل و روستاها، پاک کردن آثار آن‌ها و نابودی تمام مؤلفه‌های زندگی در این مناطق، بدون هیچ بازدارنده‌ای و با بهانه‌های واهی.
🔹
تجاوز تروریستی این رژیم در روز گذشته، در سایه سکوت مطلق بین‌المللی، همدستی آشکار آمریکا، غیبت کامل دولت لبنان در قبال پذیرش مسئولیت‌هایش و اصرار شرم‌آور آن بر استمرار گزینه‌های اشتباه، به شهادت چهار تن و زخمی شدن ده‌ها نفر انجامید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/687396" target="_blank">📅 15:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687395">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSalGS4XbwxVd3phHBEEPKTCn6h50jENLFHTzQQL4azJ9ZK0gon8N690IIPyeJVmRuohv93IRzTysX1SnydBV2C44RbDhoIS_mtN0GEefTrPs_OeSSdQArdwjT21Jq2ydYpHoG2urJyp07ZY9L4tg9gpZdvPWZyrZP2RgqZKl3-8YZhGXm-9OcA-9V2obZX-JjdGlb8NTqcVkpToTEk9-ezgmdyh8x3vFf3Ytb3KXu6x7PpEYsnn87HdMk2qan23bPpe58xTGTSPsJNpMgdWa0IED3IHvVuhhflYFEga0tW9jCBcO0_8T2HPg9CAcf-z9JNLgo3FxcgtoXVvgfifQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام اپراتور کمترین قطعی تماس را دارد؟
🔹
تازه‌ترین آمار سازمان تنظیم مقررات در بهار ۱۴۰۵ نشان می‌دهد همراه اول در چند شاخص مهم کیفیت شبکه، عملکرد بهتری نسبت به رقبا داشته است.
🔹
در بخش اینترنت سیار، نرخ موفقیت برقراری سرویس داده همراه اول در شبکه 4G به ۹۹.۶۵ درصد رسیده و در 3G نیز ۹۹.۴۲ درصد ثبت شده است. در تماس صوتی نیز همراه اول بالاترین نرخ موفقیت را داشته؛ به‌طوری‌که موفقیت برقراری تماس در شبکه 3G این اپراتور ۹۹.۹۶ درصد اعلام شده است.
🔹
این آمار نشان می‌دهد کیفیت شبکه فقط به پوشش محدود نیست و پایداری تماس و اتصال هم نقش مهمی در تجربه کاربران دارد./ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/687395" target="_blank">📅 15:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687394">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
اذعان نظامیان آمریکایی به دستور پنتاگون برای بمباران زیرساخت‌های غیرنظامی ایران
شبکه MS NOW:
🔹
نظامیان آمریکایی اعتراف کرده‌اند از وزارت جنگ دستور بمباران زیرساخت‌های غیرنظامی ایران را دریافت کرده‌اند.
🔹
ارتش آمریکا زیرساخت‌های غیرنظامی و چندین پل ایران که اهداف نظامی نبودند، هدف قرار داد و این نقض قوانین بین‌المللی است.
🔹
فرماندهان پنتاگون به اندازه کافی برای جلوگیری از تلفات غیرنظامیان در جریان حملات هوایی در داخل ایران تلاش نمی‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/687394" target="_blank">📅 15:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687393">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7051ae1e2a.mp4?token=fL3PKniqeye49kg4RXLA2vGP3IjcFnw4-AXgAjfXdsqYzP9l89qJY81itx_HF1s7Dh0c3fYLJuKXOVEn1FmfoH5aklnYONtihwVtahkf9mWwSU-G5uY120yzU6PZ1Z0cDt0OSGgClozzOfi7qwOYInNno8uO3h1LOxOaT_5IOMc5Ikp_v0iUgv7j3U7hQiMlmZ1Vh9nHm0E82sE7E-RyOCF2KosnR9iaqTFTuSMKRonnljL0QUFUe09-bRCReFaJ8zBOwAX1J_1-ZBOgstOlW_WT1tTOE9W6FXCFKt-pjXO-fsNeUjqZsRIernUftqh5oI3hXtCJDP_EJZznovbXiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7051ae1e2a.mp4?token=fL3PKniqeye49kg4RXLA2vGP3IjcFnw4-AXgAjfXdsqYzP9l89qJY81itx_HF1s7Dh0c3fYLJuKXOVEn1FmfoH5aklnYONtihwVtahkf9mWwSU-G5uY120yzU6PZ1Z0cDt0OSGgClozzOfi7qwOYInNno8uO3h1LOxOaT_5IOMc5Ikp_v0iUgv7j3U7hQiMlmZ1Vh9nHm0E82sE7E-RyOCF2KosnR9iaqTFTuSMKRonnljL0QUFUe09-bRCReFaJ8zBOwAX1J_1-ZBOgstOlW_WT1tTOE9W6FXCFKt-pjXO-fsNeUjqZsRIernUftqh5oI3hXtCJDP_EJZznovbXiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاری که نخ‌دندون با دندون‌هامون می‌کنه فراتر از چیزیه که تصور می‌کنید #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/687393" target="_blank">📅 15:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687392">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1410094cdb.mp4?token=WU5WYs1eM50jHZmEzRxkE5PgWh-DhZ-Et65iy6j1s1iZLb6wnJHlEdzrMxp6wjifmdc8CJzgsWSXy0BZFig6jJxuQQw52-cxCAlE8y200Y8rZvcMhGbgBqJtnWmhZg5xXNNa4vCM-dnPNb5IwOWZunBKqYhaQVXT_fxtkhmEJ2DMofdqrJ-amQ7fGZfy8w-8EyjaaiZ9tlJaA6WISkg6_HcQf9swhnQRTHLsR0B3MWvHprQJ8rwbwX3kkrgIYcCHPpxPcTT1WVXiCDSKrxzEa6u-u41Xf98gUzDAOV_OTXgMmG0-iuBxqw7hIYnY3ulOCBKCNnr45hgINNVu5t7tYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1410094cdb.mp4?token=WU5WYs1eM50jHZmEzRxkE5PgWh-DhZ-Et65iy6j1s1iZLb6wnJHlEdzrMxp6wjifmdc8CJzgsWSXy0BZFig6jJxuQQw52-cxCAlE8y200Y8rZvcMhGbgBqJtnWmhZg5xXNNa4vCM-dnPNb5IwOWZunBKqYhaQVXT_fxtkhmEJ2DMofdqrJ-amQ7fGZfy8w-8EyjaaiZ9tlJaA6WISkg6_HcQf9swhnQRTHLsR0B3MWvHprQJ8rwbwX3kkrgIYcCHPpxPcTT1WVXiCDSKrxzEa6u-u41Xf98gUzDAOV_OTXgMmG0-iuBxqw7hIYnY3ulOCBKCNnr45hgINNVu5t7tYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو: من به توانایی خود برای سرنگونی نظام ایران، یک بار برای همیشه، اطمینان دارم #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/687392" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687391">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZeIulm6UqaD3vZJTv-g2M-9mf7JaBABaWtDHu5pLQJ74Fjjpgz_LtP0InlzDrSxdAZzCizAiVTBu4bGr35mrm2pr-XNVNuF4fs0KCCCjt-X8eqrPsvoPXPp9MbaMzmCsJPSqDKidvFBkueIPqkmsQjd3Bg-R-oPkYjWP-PHVlf_ihMUz62yZddrsvBBe3Hb1iQbeevp5h99f5Ghd_1vFgmrZEZhq5KP5fAewKX9J2ZyX4_Z-7Yaqp0_3LXkLLLnwcYvPgKKenu-GTPalGpOiLAoPiCEvrDQFljw0Qv8beZmD257PpkFDGuSFOiJXJ74X49yX1qg4I2yNrMExktdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور: دوران تولید و مصرف فناوری در ایران تمام شده؛ به‌دنبال مرجعیت فناوری هستیم
حسین افشین، معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، در جمع نخبگان استان آذربایجان غربی گفت آنچه از یک دوره مسئولیت باقی می‌ماند، نباید به چند ساختمان و تجهیزات محدود شود؛
مهم‌تر از آن، ساختن توانایی‌هایی است که کشور را برای نسل‌های بعدی فناوری آماده کند.
او
هوش مصنوعی، فناوری کوانتومی، زیست‌فناوری، نیمه‌رساناها، رباتیک و فناوری‌های فضایی
را از حوزه‌های اثرگذار بر آینده کشور دانست و تأکید کرد که ایجاد ظرفیت به‌تنهایی کافی نیست؛ این ظرفیت‌ها باید به
کاربرد، حل مسئله و خلق ارزش
برسند.  افشین همچنین تأکید کرد که هدف ایران نباید فقط
استقلال فناورانه
باشد؛ در حوزه‌های منتخب باید به سمت
مرجعیت فناوری
حرکت کرد؛ یعنی ایران نه‌تنها فناوری را مصرف یا تولید کند، بلکه در تعیین مسیر آینده آن نیز نقش داشته باشد
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/687391" target="_blank">📅 15:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687390">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
عارف
:
افزایش عدد کالابرگ‌ها را فراموش نکرده‌ایم و تا هفته‌های آینده آن را حل می‌کنیم./صداوسیما
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/687390" target="_blank">📅 14:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687389">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a32b841d6.mp4?token=lchty0zvQDfUOUbORq9nZzg6z16KXNyhkbZrrh6OqyDMdgMgu6i8UmaYuPoUDx6QDxPbGPu8XFxgldN0iNBaljFVyEdifGN0cG-atz51bhQRqnv3TConITRW_Km3xAnu9ip-QuYY0eVypP5S0Pe0PxJqzxJeBCWJ3PNDsUouj5xfsvN6Ausz0cHrQzhqXyww27VHpzJ0rG3mWBCGqxdjMJlI4t-Z8yq-vLMOG3vQZxLeY-m1ZWrID2of-FXxUyD0WLCl6q-4Y0y76iag8xOI8HBuIXYRoNE5xa1SrSUZ5nTLDDYnuea2FPnDCIUnlQZqOINk0dhbAVthuA4PJf5iEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a32b841d6.mp4?token=lchty0zvQDfUOUbORq9nZzg6z16KXNyhkbZrrh6OqyDMdgMgu6i8UmaYuPoUDx6QDxPbGPu8XFxgldN0iNBaljFVyEdifGN0cG-atz51bhQRqnv3TConITRW_Km3xAnu9ip-QuYY0eVypP5S0Pe0PxJqzxJeBCWJ3PNDsUouj5xfsvN6Ausz0cHrQzhqXyww27VHpzJ0rG3mWBCGqxdjMJlI4t-Z8yq-vLMOG3vQZxLeY-m1ZWrID2of-FXxUyD0WLCl6q-4Y0y76iag8xOI8HBuIXYRoNE5xa1SrSUZ5nTLDDYnuea2FPnDCIUnlQZqOINk0dhbAVthuA4PJf5iEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاتز وزیر جنگ اسرائیل: منتظریم ایران به تصرف تل علی الطاهر واکنش نشون بده تا از غل و زنجیر و محدودیت‌های ایجاد شده توسط ترامپ آزاد بشیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/687389" target="_blank">📅 14:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687388">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5ck1NrfBMrbMsYbsNJwVGAMYbNMDjYRih1C8jf7517n2KiA7y7NzlhxurxxRUJuZGCGqcdIZzQh8zBX5C9ETlyD8kT3HK_yzuX7Ug5weh5_MXtWtBORgzfs_jZUcbaSk4UWCTUx26gtHEppFKc0QGXD-KSQAQRGBH5twBmlO6wZ1Z1U5qPNBnZ6WfMWgRksOMi5uF80VwuJSFcYkVpyqa_frmNSuviNmeWVstlh2QRrUKVbFgXQgx2AAciUwxKLEV__xj2LtVGDhvlb47LsQIpY8mKXPdHs14bkgJk6OAbzpct_mUUUGbCdKbNl4Xmqn7MXxMP1ua6QivaT50Bhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پارلمان پاکستان برای اولین بار در تاریخ این کشور، فرماندهی قانونی هر سه نیروی مسلح (ارتش، نیروی دریایی و نیروی هوایی) را به عاصم منیر، فرمانده ارتش، واگذار کرد
🔹
او می‌تواند بدون تأیید کابینه، پرسنل را در تمام خدمات بازنشسته، مرخص یا حفظ کند. دوره پنج ساله او حداقل تا سال ۲۰۳۰ ادامه دارد.
🔹
او به عنوان فیلد مارشال، رتبه و مصونیت قانونی را برای تمام عمر حفظ می‌کند و برکناری او نیاز به رأی دو سوم پارلمان دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/687388" target="_blank">📅 14:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687387">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a94bd3e2e.mp4?token=VGn3IDT-pt82sdt3V5zNlVh2564p2BGW_6aj2wWtE4ODvu86t9CPeTUM9s6VI50TXi4KfyeH-Su0cGoE7hY3i5pacQJkQyg7n2LYi8QgFqcGQmtx3KGh0MskMD9bG_uZJPjsiXMP95P7iCXlUqFujiO3A5adcNJETD5Om9iTow9M7Eum5ul4u7YMtHEZ2RdNmKWpl9GowRICX8W1aSsMwgkGKT3uF4L2eYJ45Ph4YunAp4etYtlkW3QzLK8eU0IZg8uQSJ7cIDJmOCSHj6EzAtpa35f5-07eBqxCXkCZV2WDg9BUlekoPksZKWF00fJ17qbj9yshp744EIAg_NavFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a94bd3e2e.mp4?token=VGn3IDT-pt82sdt3V5zNlVh2564p2BGW_6aj2wWtE4ODvu86t9CPeTUM9s6VI50TXi4KfyeH-Su0cGoE7hY3i5pacQJkQyg7n2LYi8QgFqcGQmtx3KGh0MskMD9bG_uZJPjsiXMP95P7iCXlUqFujiO3A5adcNJETD5Om9iTow9M7Eum5ul4u7YMtHEZ2RdNmKWpl9GowRICX8W1aSsMwgkGKT3uF4L2eYJ45Ph4YunAp4etYtlkW3QzLK8eU0IZg8uQSJ7cIDJmOCSHj6EzAtpa35f5-07eBqxCXkCZV2WDg9BUlekoPksZKWF00fJ17qbj9yshp744EIAg_NavFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریادار سیاری: ملت ایران به خود ببالد که مقابل دشمن مسلح به همه فناوری‌ها؛ ایستاد
🔹
رئیس ستاد و معاون هماهنگ کننده ارتش:وقتی در جنگ دشمن به اهداف از پیش تعیین شده نرسد یعنی شکست خورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/687387" target="_blank">📅 14:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687386">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ناو زنگ زده آبراهام لینکلن، نماد فرسودگی هژمونی آمریکا
🔹
ناو هواپیمابر «آبراهام لینکلن» متعلق به نیروی دریایی آمریکا که زمانی نماد قدرت و سیطره این کشور بود، این روزها پس از ۲۸۶ روز حضور در دریا، به دلیل فرسودگی و مشکلات فنی فراوان، سرانجام روز دوم سپتامبر…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/687386" target="_blank">📅 14:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687385">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMx7kyyrOHnQ4LTQHm3J3WlRq2bbHbc8GQalfCS3-MjWZZob2NnC9Z1uP1FKs_2_msctXWeTMxiKQus7MD7-GEYQDs_6KO3izz6j_gy8p7mCeXD2MFdqA-h1epsXX7VTiraIDnZt1LXuY0VM_siOooX1nWUtIUCGKXSys8Kr4EKb8Y_-FMlfj5qPACioi04j3c-IOysuvfspz_xEHfdh7JzF2ctRkmoO5wnPeyUPkB5ulSpQaVUZqcIuIIA-seyUkfxNkkTS8iTLCFDD4HCh5192nT1MgWFKaxJ5kq_ZmwHxt6pMGDu0uxDtyk8sk17Vdxjm73nPBTlNxmcGjAnX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۰ درصد نوشت‌افزارهای کشور تولید داخل است!
🔹
۸۰٪ نوشت‌افزارهای کشور تولید داخل است و بخش عمده مواد اولیه نیز از داخل تأمین می‌شود.
🔹
صنعت نوشت‌افزار ۱۲۰ تا ۱۳۰ هزار شغل ایجاد کرده و ۱۹ هزار صنف و ۳۰ هزار تولیدکننده مستقیم دارد.
@amarfact</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/687385" target="_blank">📅 14:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687384">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cce2cc97.mp4?token=KnK1ZhMar8evR7we5IN5CRIlLj0nLUWX02gw0THYS5rBtjHw2QwqOSROdVkzkYstiKrTxDacti74xhsLC7Bq89fxj34CntVwuBMc3T688-A4-f1htezSJ0LB08kK-GnKvMkdjO2gmcWEa8sEZTV2G81uQkeDOEFP-XjLOV8qRgKjEhYXGWt3qNOpgZIpFguIOpl4wSFNYGcT3dJBbdD2zHF-7gLQvEiVAg8piDmGdi_ZUAz6rOH8TIozwWg-6zZh1haZiNsSq_5fKPiAw4EN5Cgl6iRnf6UpQfZSfTb7Op1_WR1RcITSN-lT5-W3NsSaNn27snYsupxzMHa7KO-R5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cce2cc97.mp4?token=KnK1ZhMar8evR7we5IN5CRIlLj0nLUWX02gw0THYS5rBtjHw2QwqOSROdVkzkYstiKrTxDacti74xhsLC7Bq89fxj34CntVwuBMc3T688-A4-f1htezSJ0LB08kK-GnKvMkdjO2gmcWEa8sEZTV2G81uQkeDOEFP-XjLOV8qRgKjEhYXGWt3qNOpgZIpFguIOpl4wSFNYGcT3dJBbdD2zHF-7gLQvEiVAg8piDmGdi_ZUAz6rOH8TIozwWg-6zZh1haZiNsSq_5fKPiAw4EN5Cgl6iRnf6UpQfZSfTb7Op1_WR1RcITSN-lT5-W3NsSaNn27snYsupxzMHa7KO-R5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لباس ساده‌ات فقط یک کم گل‌دوزی کم داره تا خوشحال بشه
🌺
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/687384" target="_blank">📅 14:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687383">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up89yzxMapoHqZ7Gh2uUH3SuiR6BR7f0leOZAHvyIIx7hbRObCh4cKonTx_4e6NzkymAJdCla-D6W9XzYSa1O2El1JuK_K29NSZmmDZ24ul7iHOmvavd4zgRatcVGzgVUMW_16nnyBUky585QwohZJxc-Hlmy-KKx98Ona5ItAa3XWh9Eg_IZardCcyDlfbJl4PeTIFQsvQRIe3KevXLtzLXjVvGFFlUy6leX0RImNV_DVtPuTDX9P4Lf4wXMmsJxIPIKyhQOyerB5oaL_2-KoFhaS7YJchDUDXGQiZBCXeMKx_dPWlYfah084KWynpTvsFPYFkbqyvQ20nTtjpOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محکومیت ۱۸۰ هزار دلاری مهدی قایدی
🔹
با رأی کمیته وضعیت فدراسیون فوتبال با توجه به شکایت علیرضا نیکومنش از مهدی قایدی، این بازیکن به پرداخت مبلغ ۱۸۰ هزار دلار بابت اصل خواسته و مبلغ ۵ میلیارد و ۴۸۹ میلیون و ۵۷۰ هزار ریال بابت هزینه دادرسی در حق خواهان محکوم شد./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/687383" target="_blank">📅 14:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687382">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
توجیه فرانسه برای حملات آمریکا علیه ایران: توافق منقضی شده است!
🔹
مدیرعامل فرودگاه امام(ره): پرواز مستقیم ایران - تونس مجددا برقرار شد.
🔹
رسانه‌های لبنانی از پرواز پهپادهای شناسایی رژیم صهیونیستی بر فراز بیروت و حومه آن خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/687382" target="_blank">📅 13:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687378">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار قم(Admin)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R00M35YigQmd-OXjR-ZA3PWj6wLSDDH4CKH-fziKAaePwNy8bqNFW2sD1Py4fYMCU8mE0Q9tL9gkbxvJt7VyLoRzIB3US-mCuSFeWjCHtr-Y-32XkzGJcuEhjeKM8YjbNYUcIWJCUNR83mobQ_CGSWrEFTdYgg65-p4RxgqBxFd3OpRSWeACi-SPaK3fQCTj5m7p4EizxZR4_eIMngaWedURn7M0OBkbkwKJVSkEBwRHFp-t2tcEbnSNZ2k8i84WWwXVb1PedF-ra9oGluXZxGwfmq-f_lJG5KoIzOEXyNA1-Fxob4vzsVEoWcNhsbW3uEg5WPZIQ5DGNg55jha8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBYVb8ipzeKg7gfn-wbrEFED_sMgX2hNmPdMw3-XWJHvQKS82H4l52NX1Fj67-VwK8SHTs8Ke0XqVBf6jYqVYDk1cXH5BmjjKO8cxniX-cnmr0oVQGifU2PA_pmSKZeVyYZBVeI7AOwyMpc3bmHGLfFoHjRAu2pHiNL-Mh9pT1X2-uYO_AHGWu2BaKJopZhuVtVBOL-fBwNfehEzu1V_aVBHCpGDtIiSIPkrAGS9x3ld35t5myABX9w3xC5CwbUkbbRDvt4JIcxF2p6nZ8MkJgcDdsxAM7N4boagbOAubI8iot-3h_9O5ptjSpBrWB99b6Nhdqr9_yATC3tWbIixSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4Z7un5ECQ912de6V_MaB-zItg-StOcw1nynrypSRgXqAvGNelCwQyBV9iA77UWcQGW4f4yYHCGKUv5EdR19RVGL2QNcjT02oy79agbpcv9AZmjzBU0eruxOChpjL-Bq74s32n_6rSzoA3KN0GqRj5ucpuYPHU1AZ6wy0Y_dGd5jn952cnmsHcv7d29H3nG20cPWdDsfGo1zcjU4GEeBmd3wHG6twgMC7D4pmE94p3iqfhOxYD_mlRn1-LnmF3EabdlVF1iq7U2niWZB_GQrk6wE16jdouJl_DkFA1ap5WxsWKVc4kaOOzYzzzbk2ldbYYX8nNOcnPOz5cOOINM0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGzLFghAV0XXf6_xYGu9WgFvmr6h3khwS8lm21qYYx7Kfvzd6a2CzFu5zEzALKKY1VzyLGHj5OmSlY5rrp6C_G_EwvrE4M0NcShZKDNRC9mPB8KYBsjFlFPyDlTORc1FEpdKTjl396sBpBZy5MC22KRr66fqYYFBs7oPAV50NLvLDfg1JSEsVHtHav5Gvw_NMaFBb1zSFa7xE6jXYMBswy2jSkvnRQbyxXy0wH_jAd5y8XlL-u5eoU1-bhPCuqc6BoSqeFf4X0hSRKlBKhrNagvkkSI8YNHoNxz-tENodktkIiM-1VqEFrPGkqZgVFx0Yj9POii4b0pWxqfXJXUwPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
امروز شنبه ۱۴ شهریور ۱۴۰۵ روز قم است
🔹
قُم تلفظی از نام کُم است که اعراب آن را به صورت امروزی درآوردند.
🔹
برخی پژوهشگران، واژه کُم در نام باستانی کمیدان (کمیران) را در معنای "شهر" دانسته و بین واژه‌های "کمیران"، "شمیران"،"تهران"، "چمران (در نواحی ساوه)" و "ایران" ارتباطات واژه ساختی قائل شده و نام قدیم قم را "کمیران" (در معنای "ایرانشهر") دانسته‌اند.
#روز_قم_مبارک
@akhbareghom</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/687378" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687377">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
هلاکت ۲ تروریست در سیستان‌وبلوچستان
نیروی زمینی سپاه:
🔹
یک تیم تروریستی وابسته به آمریکا و رژیم صهیونی که قصد انجام اقداماتی بر روی اهداف از پیش تعیین‌شده در سیستان‌وبلوچستان داشتند، مورد ضربهٔ قاطع قرار گرفتند که منجربه هلاکت ۲ نفر از آنها شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/687377" target="_blank">📅 13:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687376">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a344525474.mp4?token=KRv9HbuT6VivSfb2p8d5xFtSw2-RvFu-mquqcyATP9um8EeQghAwMbmX4wWF_cVJa5Stl3nft2F-vrxH_d3i-sW0Z7F-uL8xlCLgqnuIKGpTzKOM7xtZYhQXhYah0TRFlEdkPhzXKPDvPn8vHMejNWTZxhIHw9I6Cmw9jSkTsvPlAaOMaA2nW4RQjQ1iP9bc7sM6Mx2VdbKqHzK2IjjESTQqGmgeEFBZp3FD7BDc_brQ-UbHjKeQOB32dd3PnSkKKxrTLHfm41TPh1lNGPthlW8E66AhXASDm6KoTNUCQvKCTrrlmX8TmjhrLGZ6wvuZ0tzZ8UEaAzZ1eO5iLxhnnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a344525474.mp4?token=KRv9HbuT6VivSfb2p8d5xFtSw2-RvFu-mquqcyATP9um8EeQghAwMbmX4wWF_cVJa5Stl3nft2F-vrxH_d3i-sW0Z7F-uL8xlCLgqnuIKGpTzKOM7xtZYhQXhYah0TRFlEdkPhzXKPDvPn8vHMejNWTZxhIHw9I6Cmw9jSkTsvPlAaOMaA2nW4RQjQ1iP9bc7sM6Mx2VdbKqHzK2IjjESTQqGmgeEFBZp3FD7BDc_brQ-UbHjKeQOB32dd3PnSkKKxrTLHfm41TPh1lNGPthlW8E66AhXASDm6KoTNUCQvKCTrrlmX8TmjhrLGZ6wvuZ0tzZ8UEaAzZ1eO5iLxhnnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت خارش محل گزش پشه
🔹
علت اصلی خارش شدید ناشی از نیش پشه، واکنش سیستم ایمنی بدن به بزاق این حشره است. هنگام ورود بزاق پشه به زیر پوست، بدن آن را به عنوان یک عامل بیگانه شناسایی کرده و منجر به ترشح هیستامین می‌شود. این فرآیند باعث گشاد شدن رگ‌های خونی، تورم و قرمزی موضع شده که در نهایت احساس خارش شدید را ایجاد می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/687376" target="_blank">📅 13:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687375">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7U-GsMKe7mycHg-7CMOo927mySkpmeObXFo3s-CuHSftc8homIwioz35HBI1k2azh7rC252D6hKyiT5QcLmWkSmiMzNZSJKkKFInjddoXDQDg8pU85H8EfX4rmx3_dyEp0DLS2uOEfP96by4RM-tf_tJgX-a52oBfrvsFottkd5QPAMuj6oxYr4-H1wZqbmi2p8SEG90MGj-MxoEBMee6RlKxmlmrbKJRHN-uKRHIGlOzHwGY__wd9C9UBf7PyUHeFaTpw5l6zjhu-PcgKfDKT1mCZejTnwMNobG3iNHjhDn3fMhdVOxKMwahA-d2ArJaO6Y5YR8m3Af8DfJacXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
🔰
آدرس جدید دسترسی به سایت و پیشخوان مجازی بانک مهر ایران
🔹
آدرس‌های جدید سامانه‌های بانک قرض‌الحسنه مهر ایران به شرح زیر اعلام می‌شود:
🌐
سایت بانک مهر ایران
qmb724.ir
🌐
پیشخوان مجازی (مهر من)
my.qmb724.ir
🌐
چت بات
qbot.qmb724.ir
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/687375" target="_blank">📅 13:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687374">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان: آموزش و پرورش مهم‌ترین چیزی است که می‌تواند کشور را نجات دهد.
🔹
دادستان تهران دستور تعیین تکلیف سریع محکومان مالی، به‌ویژه کسانی با بیش از ۱۰ سال حبس را صادر کرد.
🔹
توانیر: برق ۱۶ واحد صنعتی دارای ماینرهای غیرمجاز در یزد قطع شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/687374" target="_blank">📅 13:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687373">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f02229aa4.mp4?token=giDPqvFgGTqXINgzhqhTJG0xKB4idExJqXnJiFCxYTFW5C7ukXjGzRA9BQOD33Gcz_rnKj4Lwfm7DdPyFJCMMnGJD6vM3b7Z5rTvz1z6XhIUnVg4la6wucusxIYIkTwW9WYBLrATh2aShwTezI73oKXvtqsBaPh722uW3DJ06dKM1FjT3-B4R99NZZ1Y9ttTD9cv9cjVqGHBh8BybOKnCiKvTVz8lyXu4pmImwUxH2osRsN53bmSN1oFewzycsxmkLvjhHFz1yccwZSjc3renNZGBQQezQ7yz713XxUHNBs41yKiKW3UVBinR2-azvx8gi84H6CHIBx6cWduE5UEEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f02229aa4.mp4?token=giDPqvFgGTqXINgzhqhTJG0xKB4idExJqXnJiFCxYTFW5C7ukXjGzRA9BQOD33Gcz_rnKj4Lwfm7DdPyFJCMMnGJD6vM3b7Z5rTvz1z6XhIUnVg4la6wucusxIYIkTwW9WYBLrATh2aShwTezI73oKXvtqsBaPh722uW3DJ06dKM1FjT3-B4R99NZZ1Y9ttTD9cv9cjVqGHBh8BybOKnCiKvTVz8lyXu4pmImwUxH2osRsN53bmSN1oFewzycsxmkLvjhHFz1yccwZSjc3renNZGBQQezQ7yz713XxUHNBs41yKiKW3UVBinR2-azvx8gi84H6CHIBx6cWduE5UEEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: وقتی جوان ما در خیابان مشکل دارد مقصر ما هستیم/ ما نتوانستیم آنها را درست آموزش بدهیم
🔹
ان‌شاءالله خدا کمک کند تا راه حضرت ابراهیم را برویم و بت‌شکن باشیم
🔹
یاد نگرفتیم با همفکری به یکدیگر کمک کنیم، یاد گرفتیم دستور بدهیم و دیگران اطاعت کنند؛ اینجاست که کار خراب می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/687373" target="_blank">📅 13:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687372">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0c879d93.mp4?token=d0ituHn2GZqLpEZCcm1jE_qMrCCwbTwkWlEjFKg-INmxLxm56-ogZTZELDTPtGZrqzp5s6zuC5cD60aZqvQt8tK2SeyyU0kJKH9j0H89F6qJ2a7W8heC3oAOCusYyrzVZR8mYivlSn0CEVHZSOd8Oafa1GZXGSOXUg8m7QTnCdQAynkCQd7oNG1mSXJf-mmpQikkKt-OL6lE3Gcl51gWCMaoCqO9T7ZFDGJVvj63GsxjEObvi10ZfPwT36u6hlGEN9lrPcR9E9tQ0_P2pi7E2-XD0h3iJpvx4A61EJxBKsLY70bm286I5t2qI-GFAfFbnXOjLNB-fTws9ZWLJA2bBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0c879d93.mp4?token=d0ituHn2GZqLpEZCcm1jE_qMrCCwbTwkWlEjFKg-INmxLxm56-ogZTZELDTPtGZrqzp5s6zuC5cD60aZqvQt8tK2SeyyU0kJKH9j0H89F6qJ2a7W8heC3oAOCusYyrzVZR8mYivlSn0CEVHZSOd8Oafa1GZXGSOXUg8m7QTnCdQAynkCQd7oNG1mSXJf-mmpQikkKt-OL6lE3Gcl51gWCMaoCqO9T7ZFDGJVvj63GsxjEObvi10ZfPwT36u6hlGEN9lrPcR9E9tQ0_P2pi7E2-XD0h3iJpvx4A61EJxBKsLY70bm286I5t2qI-GFAfFbnXOjLNB-fTws9ZWLJA2bBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کی این گوشی‌های قدیمی و خاطره‌انگیز رو یادشه؟
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/687372" target="_blank">📅 13:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687371">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25fc13676f.mp4?token=JnYh2FlkjOoCR6kLxIavQYhrXkBWQSGlCThvb43eMNp9eGVbvblEFOGrWqq1b9dHiRh80mmrVCtX1kultPPhwBjpd5VgTGfi6F34mMUrjoEFoAW8P2lwuc10500CvPw9qlap_kxTMWppZYHpRXpGxm1rHa5fC3cM4jC3GrEaZyhZNHs3R7enUFIwSEiR-thOwzlyc3FhjWdXawr4VBITJaV053fuxHKnpdFQmrSmnw8C_P6vBC7mNrM2B7mBVYP0QQyVQ8DH6C_pEon-pOmwMCZuX_a_JFEuscLnHX0smfKnsZsjpZiffSyCmkRyH3E95r-DtokH8jEF7UnHXxkJVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25fc13676f.mp4?token=JnYh2FlkjOoCR6kLxIavQYhrXkBWQSGlCThvb43eMNp9eGVbvblEFOGrWqq1b9dHiRh80mmrVCtX1kultPPhwBjpd5VgTGfi6F34mMUrjoEFoAW8P2lwuc10500CvPw9qlap_kxTMWppZYHpRXpGxm1rHa5fC3cM4jC3GrEaZyhZNHs3R7enUFIwSEiR-thOwzlyc3FhjWdXawr4VBITJaV053fuxHKnpdFQmrSmnw8C_P6vBC7mNrM2B7mBVYP0QQyVQ8DH6C_pEon-pOmwMCZuX_a_JFEuscLnHX0smfKnsZsjpZiffSyCmkRyH3E95r-DtokH8jEF7UnHXxkJVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خارگ؛ نگین زیبای خلیج فارس
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/687371" target="_blank">📅 12:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687370">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3381f657.mp4?token=KIgvSsr4D-E2NMoYHooJOtOxS339-M-ThHGqMdOkrdQgFc9x8jmlBi2mkMdk1tNcHr_Ke-RF35g0q2Mfi2oaDWuKTlTv3hf6P_yMFC3ZEAAY5n2eqWdEU0wV_bWc45V0ylAB0S35Or_YKwOT4Tg9wcdJbN2ONqYl1N8VH1s8LKyMYooDeqPakh3nuvAewo-lzQbLMdwenNyRyjV1Y7lR_T9ECNX4LrhgcqSlLqRuzAk_7jWpdV81tOOJ7Mhj0PmXBfFggcqzc2In4i5fVOy5cuuIMskTwUxsOq2QwyXsPMzb72mJx0F9B1_AxwqLNHxynaOkgvbpY0lE56qZyTL_lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3381f657.mp4?token=KIgvSsr4D-E2NMoYHooJOtOxS339-M-ThHGqMdOkrdQgFc9x8jmlBi2mkMdk1tNcHr_Ke-RF35g0q2Mfi2oaDWuKTlTv3hf6P_yMFC3ZEAAY5n2eqWdEU0wV_bWc45V0ylAB0S35Or_YKwOT4Tg9wcdJbN2ONqYl1N8VH1s8LKyMYooDeqPakh3nuvAewo-lzQbLMdwenNyRyjV1Y7lR_T9ECNX4LrhgcqSlLqRuzAk_7jWpdV81tOOJ7Mhj0PmXBfFggcqzc2In4i5fVOy5cuuIMskTwUxsOq2QwyXsPMzb72mJx0F9B1_AxwqLNHxynaOkgvbpY0lE56qZyTL_lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: اقدام آمریکا و رژیم اشغالگر قدس علیه ایران مصداق بارز جنایات جنگی است؛ اما متأسفانه شاهد بی‌اعتنایی سازمان‌های بین‌المللی به این جنایات هستیم.
🔹
تجاوز به تمامیت ارضی ایران را محکوم کنید/ مرتکبان جنابات جنگی علیه جمهوری اسلامی ایران را تحت تعقیب قرار دهید
🔹
خواهان نظمی هستیم که هیچ قدرتی خود را فراتر از قانون نداند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/687370" target="_blank">📅 12:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687369">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67637513d.mp4?token=CwgOE9Mu1jsXXCofV1oM0MdDEoGJrj1QJamrz0TJik-4UPQ6lz_Ke_kmvD-vgeFxEmeGsMx3nEhv3SMI4gUgu4imVobYYeBSxxKuKKKjEN7aa1KnNoEx9t_vkpu7re8iVGI9pvWfFPOu7RUc5SoGNT4eoSjtuVVW5Q9cKqaFw3qAWSJlNLff1RN4FtzKMPatfpYvGXUp9DG9WH2f4lYkvFNQyLTnet6u9BvApitoxiuzpVhUlOwB6rrDiD9NdSfJdwkpH-eS90ex4BpXwNJYbWAwSk0_dcYdgpUV3LHVRPnv_K6Rd1sFUl-YmyIxB8wzLCWuE0Qdrrecj58tUl5vfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67637513d.mp4?token=CwgOE9Mu1jsXXCofV1oM0MdDEoGJrj1QJamrz0TJik-4UPQ6lz_Ke_kmvD-vgeFxEmeGsMx3nEhv3SMI4gUgu4imVobYYeBSxxKuKKKjEN7aa1KnNoEx9t_vkpu7re8iVGI9pvWfFPOu7RUc5SoGNT4eoSjtuVVW5Q9cKqaFw3qAWSJlNLff1RN4FtzKMPatfpYvGXUp9DG9WH2f4lYkvFNQyLTnet6u9BvApitoxiuzpVhUlOwB6rrDiD9NdSfJdwkpH-eS90ex4BpXwNJYbWAwSk0_dcYdgpUV3LHVRPnv_K6Rd1sFUl-YmyIxB8wzLCWuE0Qdrrecj58tUl5vfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت جزیره خارگ پس از هدف قرارگرفتن نفتکش ایرانی  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/687369" target="_blank">📅 12:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687368">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsBgm6Ym6fB4vrMjKF39AOiQBXByyiaNX-WPTFpHOdU3ResyybF5G0vZexpBTc3nytFzl5mZPjFPXEdBfmK2_m9w0ZSw0WMYY9DvhdqOI260pYTYpgF8Ozut2DSRgkbqRVvx88DD3BBuXjFxzxVYmr5_L1orRyC-B9uHrs18cnyhAk6WQn04Hzs7Ejz4LlSTmZeusRqTbpuLPgzGRcenBjqhXubfULdjJAN9EJ-b_mafF8FtLcwLMwDIhjrXsyrgbpR9wIUgMOGqAy7SZ7fJDNj4I0tA1NFDbVLsS-fJP7ThQXs6nCgkS6MKGYGs6y7bAqxJnDk5gj478JWVWntc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد بیش از ۹۷ هزار واحدی شاخص کل بورس
🔹
در جریان معاملات امروز ۱۴ شهریور شاخص کل بورس با رشد ۹۷ هزار و ۲۷۶ واحد در سطح ۶ میلیون و ۶۰۱ هزار واحدی ایستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/687368" target="_blank">📅 12:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687367">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekGiY_oiOzfnCwM4spZCYmL8A2VQxTf6I1TVKCB89Eaq4xCOzK1OIkDJ1ly05qfA5UZdXdOJFv9yNwo2Kch8VVT94L6CnlAgn2ZMhCz01Hq4DeRj6UVrM_0DgREFL_HNHuEchmMVYYxvXo4IDtRmWgFUtVTECHqfuiukBIqeTeZnVQnM57vd3e7-f_PCZQlNjWU8TFCm26SDg-60WjQpsNfnsedVzzix1d1-vOydmBku76qadL3IcGo54Grtgh-Lu0_UD37eaKHSs1Qu0A0DkFI7OxeLWOz5wAhzuc2ZbO16xdhRl-w5fyy9CYVpbm-NtP62nNmeJAUMA4TFmjpfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۴ شهریور ۱۴۰۵؛ ساعت ۱۲:۲۰
🔹
دلار آزاد با جهش امروز به ۲۲۴ هزار تومان رسید؛ رقمی که نشان می‌دهد نرخ ارز نسبت به یک ماه قبل حدود ۱۷ درصد و در مقایسه با سال گذشته نزدیک به ۱۱۷ درصد افزایش داشته است.
🔹
هم‌زمان، هر گرم طلای ۱۸ عیار به ۲۳ میلیون و ۶۶۳ هزار تومان رسید و یورو نیز در محدوده ۲۶۰ هزار تومان معامله شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/687367" target="_blank">📅 12:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687366">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57a89e8e7.mp4?token=Cs1y8Jcz8_mk2wSV8KYJUS3MQORPricxOiaZ8OQXbt-KWC4PjAWtummTZz5l1e6_VsKU7GjQQwqCok_lbPe2o0kWUI3Bti58-MEOOhLCyxg4Qv1vwC5AYYT31zqEQOK3tbI1SSKmp1kZOYuVidQXgWpNF4G-k8PNbTkNkqBC05qXp8CKtN9eiXLDoIyIrP40wfVRNZKhBLlv8CbK8YQssKEMCev98-yZ3sXEQJyen5QxolzRJkNFaon5LeewOyvNActqY205u66IY1nGvB2CuhsvtyPH3LiCbFb2Ig_wJda60RijWXH2fQjPFyCm347XkOqsniIaSCzy20_QDBNLOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57a89e8e7.mp4?token=Cs1y8Jcz8_mk2wSV8KYJUS3MQORPricxOiaZ8OQXbt-KWC4PjAWtummTZz5l1e6_VsKU7GjQQwqCok_lbPe2o0kWUI3Bti58-MEOOhLCyxg4Qv1vwC5AYYT31zqEQOK3tbI1SSKmp1kZOYuVidQXgWpNF4G-k8PNbTkNkqBC05qXp8CKtN9eiXLDoIyIrP40wfVRNZKhBLlv8CbK8YQssKEMCev98-yZ3sXEQJyen5QxolzRJkNFaon5LeewOyvNActqY205u66IY1nGvB2CuhsvtyPH3LiCbFb2Ig_wJda60RijWXH2fQjPFyCm347XkOqsniIaSCzy20_QDBNLOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرسدس میباخ GLS600 V8
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/687366" target="_blank">📅 12:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687365">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fceaa1ca.mp4?token=H9Obgz9z0ElsXeYUhP6vxLELsmT_1S4-zi8TATW6x_aehsR08sp-DNjPNDtLOGslCGTqF4ufmimtm7f4EFaVXw6N0vrCyKOx1B1dwnAZk358mYJbCOMVGCdPzYAKzWFkGHaoSIAF6ueX5Sq2kQ9N6KSrkGuqcu0u7ECoB-dTfP61dp7n5QiY0M6DNLyVPbXhUbqGnFx1HjC6kUbXs1Fh9It9CNCRXbgwc4wR-N2oBhv1vG1P1X6OKkCme7vSVY9-5gME3z1xH4ESawWVANCFwObyrQkZwdyQSEHdsgXP3ArQiMPor2aPN4DnouSF4TYC9_EMfDpY4HhuHy_GnBgKP0lYb-mitJMzYF-K6jxBnYbuPdXTDpiGEdAZMlk1HvtJmMWrMP2vq3TH0fZknt3bch2lQLWdFzOF3zYW3E5He_7UEmdt55z32bAz0ePEUZA1Fs-JgoO0CtMAgjg1skCvu8gq55VS23PxT08wVkC-SrtQWhdN3Tb-6cKWyTJO9-u3vgaYvN0MW7VbgYOalZHk5BCEBxLgCY4w0NTVKmR0_KEpvVzGQwqSPlo8OriPP4hzNCOoUynft8mFAJAfZ28XQ_fmZAIu5ZRR99iLX9PW68D9XBDvBCuYv5-VhK596mBwTWYxJqVuaaj4f2Va8vhUJ0ra88tk6hNRhMZYo4I1-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fceaa1ca.mp4?token=H9Obgz9z0ElsXeYUhP6vxLELsmT_1S4-zi8TATW6x_aehsR08sp-DNjPNDtLOGslCGTqF4ufmimtm7f4EFaVXw6N0vrCyKOx1B1dwnAZk358mYJbCOMVGCdPzYAKzWFkGHaoSIAF6ueX5Sq2kQ9N6KSrkGuqcu0u7ECoB-dTfP61dp7n5QiY0M6DNLyVPbXhUbqGnFx1HjC6kUbXs1Fh9It9CNCRXbgwc4wR-N2oBhv1vG1P1X6OKkCme7vSVY9-5gME3z1xH4ESawWVANCFwObyrQkZwdyQSEHdsgXP3ArQiMPor2aPN4DnouSF4TYC9_EMfDpY4HhuHy_GnBgKP0lYb-mitJMzYF-K6jxBnYbuPdXTDpiGEdAZMlk1HvtJmMWrMP2vq3TH0fZknt3bch2lQLWdFzOF3zYW3E5He_7UEmdt55z32bAz0ePEUZA1Fs-JgoO0CtMAgjg1skCvu8gq55VS23PxT08wVkC-SrtQWhdN3Tb-6cKWyTJO9-u3vgaYvN0MW7VbgYOalZHk5BCEBxLgCY4w0NTVKmR0_KEpvVzGQwqSPlo8OriPP4hzNCOoUynft8mFAJAfZ28XQ_fmZAIu5ZRR99iLX9PW68D9XBDvBCuYv5-VhK596mBwTWYxJqVuaaj4f2Va8vhUJ0ra88tk6hNRhMZYo4I1-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاکانی: کلاهبردارها کلاهی سرمان گذاشته‌اند که تا کمرمان امده است، خودروها را ۳۴۷ هزار یورو قیمت دادند، در صورتی که ۲۲۰ هزار یورو قیمتش بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/687365" target="_blank">📅 12:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687364">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfc331382.mp4?token=tbR7PzABwHvJHJUptRvu4Ujj2Hpd3nQ9G76A6xMtXomr-UwzQ9h2E1VVpHmuD9F2JDEugCGz0D9s2M965M3IJPEEHYjZGoRqcyysLvnv5bJiwUZCZhDSp8q7Pyko6F31yFfL9nb606XC83S1JykRnplsnU_0lbaR90ZZlc5qugFasT0ymmeLzqy29QYo0tAtwEStK5Uak6i_1l_AqaE-7mttefWSUShOzVJxzs61GhN9s-g-8M_l5V4XlDXQbioVLAka1lg0_oPerl84aaNaTkA1-rBdYyNIfFYk5H3vi56r5LPZivwA6Xel_EpP_lopV3mLCeuTllD0napDwVoqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfc331382.mp4?token=tbR7PzABwHvJHJUptRvu4Ujj2Hpd3nQ9G76A6xMtXomr-UwzQ9h2E1VVpHmuD9F2JDEugCGz0D9s2M965M3IJPEEHYjZGoRqcyysLvnv5bJiwUZCZhDSp8q7Pyko6F31yFfL9nb606XC83S1JykRnplsnU_0lbaR90ZZlc5qugFasT0ymmeLzqy29QYo0tAtwEStK5Uak6i_1l_AqaE-7mttefWSUShOzVJxzs61GhN9s-g-8M_l5V4XlDXQbioVLAka1lg0_oPerl84aaNaTkA1-rBdYyNIfFYk5H3vi56r5LPZivwA6Xel_EpP_lopV3mLCeuTllD0napDwVoqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این تکنیک ژاپنی برای جنگ با تنبلی آماده شو #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/687364" target="_blank">📅 12:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687363">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ad4677ad.mp4?token=DVLWEW-U7d_xvoRRlp_WV6WzZ4BLPHayfP-Pz55lb6aWLt_Z_kbEyaEyCzCUuK_ykoMrpee4Yrzi_nLI4PpcmC3X1MOdTquZQulHnq46IxQcYmespwty9mAlXh2KxddG8lFPHRmcgEvHMgJlgO6dgT9JKCfFEZSCxXJ1w5nc63HlzWCGfVu46tQ08_RJ3ESNCvh0Cjyvz1tm2bBPQRb4WGGAl6XO-gCNRY1TN3rv6W2zhR94gbWDw8E_y-oW2WK1ryMCG1zwYCpOoEWK_BEmMKj9BR0pQR8UX2LR0hP3YUsO3zaIrkhPejjEDlh6GjkysJDVrVWGW15g78r-16LZ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ad4677ad.mp4?token=DVLWEW-U7d_xvoRRlp_WV6WzZ4BLPHayfP-Pz55lb6aWLt_Z_kbEyaEyCzCUuK_ykoMrpee4Yrzi_nLI4PpcmC3X1MOdTquZQulHnq46IxQcYmespwty9mAlXh2KxddG8lFPHRmcgEvHMgJlgO6dgT9JKCfFEZSCxXJ1w5nc63HlzWCGfVu46tQ08_RJ3ESNCvh0Cjyvz1tm2bBPQRb4WGGAl6XO-gCNRY1TN3rv6W2zhR94gbWDw8E_y-oW2WK1ryMCG1zwYCpOoEWK_BEmMKj9BR0pQR8UX2LR0hP3YUsO3zaIrkhPejjEDlh6GjkysJDVrVWGW15g78r-16LZ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر صدای غیر طبیعی مربوط به خرابی کدوم قسمت ماشینه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/687363" target="_blank">📅 12:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687362">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تکذیب حمله به تاسیسات هسته‌ای اصفهان
سپاه اصفهان:
🔹
اخبار منتشرشده در فضای مجازی دربارهٔ حملهٔ آمریکا و رژیم صهیونیستی به مراکز و تأسیسات هسته‌ای اصفهان از اساس کذب است و چنین حمله‌ای صورت نگرفته است.
🔹
انتشار چنین مطالبی در شرایط حساس کنونی، نمونه‌ای از تلاش جریان‌های معاند برای ایجاد التهاب، تشویش افکار عمومی و برهم‌زدن آرامش روانی مردم است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/687362" target="_blank">📅 12:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687361">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
جریمه‌های سنگین در انتظار محتکران کالا در بندر خشک آپرین
دادستان تهران:
🔹
کالا‌هایی که در این بندر بدون مجوز تعیین تکلیف و ترخیص نشده‌اند، احتکار محسوب می‌شوند و جریمه‌های سنگین به آنها تعلق می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/687361" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687360">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSCPNL5HM6qlo1bYLVbxdWZRQq0kHJxoLGS4vQPs8CV8q2m8TE-W1wyYjcPAf60TRgFndHnTZtQ_-8bU9NaWmImRt_FmbGPMTjyee9Q2NxWmwxXR2q936satibSVP0Ujlp_tJTQszrxxpU_-OBdC0Rq7lSp7AUmjmI533Q4fq5qM5wFhBBgc1PIPn1MJy0SKi9fxdGFwpgmzpJ04Owqw0rqTWJKBPaFYqpUAaSe2hVF7yqfvy6AozmhJ1QhK6JAcyC1-Me-5Hmo0Tr1XF7FJ6XIlDkcRM61AHXqv4vKnI6M-nmDAj6pwgT5rWj6AQ0dMhfyH30hJdiJRqph9Jba9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: موشک آمریکایی عروسی ایرانی را به خاک و خون کشید
🔹
روزنامه نیویورک تایمز در گزارش تحقیقاتی خود با بررسی ویدئوها و مصاحبه با افراد محلی، نوشت که آمریکا در حمله به جشن عروسی کوهستک از موشک‌های JSOW استفاده کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/687360" target="_blank">📅 11:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687359">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سپاه: صدای انفجار در دماوند ناشی از برگزاری دوره نظامی حیدر کرار بود.
🔹
پلیس راهور از ترافیک سنگین در جاده چالوس و آزادراه تهران ـ شمال خبر داد.
🔹
اردوغان: حملات علیه کشورهای برادر در منطقه را به هیچ وجه تأیید نمی‌کنیم.
🔹
روسیه: ناتو از آنکارا در مقابل تل‌آویو حمایت نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/687359" target="_blank">📅 11:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687358">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76579f347.mp4?token=SQINEAqk8-j6oV_uN6ZQFwqP-i-cHUznqDv7PlSoF4-bal6Rj_F6yog2CwZh_h4deaXm-uKwikgBFPKzsrBPPwpZKWGG6CMTfD2eHthG2E7rruMWmX6ytSpvp1rsYDCzwxFVe5EmL7isk3kFH5URMCbEfn0jnGuRdrv07aC-7GBhKmG64Hr0sUi0EnCzgNcOlEBUjtNy2scow4kuuSCEGuKnxV0lJyoOsARuP50vkUdYSf_QlvHI2wrAZUy-WmxX9p_n6yhCfePvP0ZSC6hWVQVmAMAphNHo5guFqyjswS1c5PWgxdmejpDOOWSANS-0iq6qPDJvG9uRtrtyCqWoAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76579f347.mp4?token=SQINEAqk8-j6oV_uN6ZQFwqP-i-cHUznqDv7PlSoF4-bal6Rj_F6yog2CwZh_h4deaXm-uKwikgBFPKzsrBPPwpZKWGG6CMTfD2eHthG2E7rruMWmX6ytSpvp1rsYDCzwxFVe5EmL7isk3kFH5URMCbEfn0jnGuRdrv07aC-7GBhKmG64Hr0sUi0EnCzgNcOlEBUjtNy2scow4kuuSCEGuKnxV0lJyoOsARuP50vkUdYSf_QlvHI2wrAZUy-WmxX9p_n6yhCfePvP0ZSC6hWVQVmAMAphNHo5guFqyjswS1c5PWgxdmejpDOOWSANS-0iq6qPDJvG9uRtrtyCqWoAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان عصر «خالی‌فروشی» در بازار طلا؛ بانک مرکزی وارد می‌شود
رضا الفت نسب ، رییس اتحادیه کشوری کسب و کاری مجازی:
🔹
بر اساس مصوبه رسمی هیئت وزیران در آبان‌ماه ۱۴۰۴، قرار است با ورود مستقیم نهاد ناظر ضابطه‌مند شود.
🔹
طبق این مصوبه، تمامی کسب‌وکارهای فعال در حوزه طلا و جواهر مکلف هستند به سامانه جدیدی که توسط بانک مرکزی راه‌اندازی می‌شود، متصل شوند. هدف از این اقدام، ایجاد بستری امن، شفاف و قابل پیگیری برای معاملات است تا دیگر هیچ واحد صنفی یا تجاری نتواند خارج از چارچوب‌های قانونی و بدون پشتوانه واقعی، اقدام به فروش طلا به مشتریان کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/687358" target="_blank">📅 11:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687357">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
سیگار و اضافه وزن از علل بروز سرطان‌ در ایران
وزارت بهداشت:
🔹
در مردان ایرانی، عواملی مانند مصرف سیگار، تریاک، اضافه‌وزن، رژیم غذایی نامناسب و قلیان از عوامل بروز سرطان است.
🔹
در زنان نیز، اضافه‌وزن، عوامل عفونی، مصرف سیگار و قلیان و مواجهه با دود دست‌دوم از جمله عوامل خطر قابل توجه هستند.
🔹
در حال حاضر سرطان پستان، سرطان دهانه رحم در زنان و سرطان روده بزرگ، هدف غربالگری شبکه بهداشت کشور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/687357" target="_blank">📅 11:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687355">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKAWRzYyIra6P69zMtPi_xIIqXkiI_XkJcS4A6ldLZIklkzUE3bPbpFG63s79XFYJMiMGw_Hvc_2SrOgJ0LtFWzUhA5CVN-y2ArEZWm2IS3fUyC9GklhCDIPLLUjWC7xVVRpBYrHQTc2FcEHYo3auVbmhGw0yDMpKE7VI8uZYyMhWuMdarUGaPcK57bnUnXV-LzhH-PZN7oV77o2swCxl0XLCKN_6-8EJdMHIf6G5qm1001k1zSIDrN5PrHJz68B4ZeBWvkO20KCLJvY_G_HlQ4rT2grmiMcJrvg92md0aLF6fWhN47jadcbAxtxadz-ByEKMHbYV9ujw_BcQplhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پک ویژه «علوی»؛ سه تکه از بهشت، همراه شما
نجف، نه فقط یک نقطه روی زمین، که نقطه‌ی آغازِ دلدادگی است…
برای آن‌هایی که دلشان در ایوانِ طلا جا مانده، یک مجموعه اختصاصی از عطر، نور و غیرت حیدری آماده کرده‌ایم. مجموعه‌ای که با عشق در کنار هم چیده شده‌اند تا عطر و نام مولا، پیوسته همراه روزها و خلوت‌هایتان باشد.
✨
محتویات پک اختصاصی علوی:
▫️
مهر تربت بوتراب: خاکی متبرک برای زلال‌ترین سجده‌ها
▫️
عطر حرم امیرالمؤمنین (۲۰ میل): یادآور نسیم سحرگاهی ایوان نجف
▫️
گردنبند ذوالفقار: نشانه‌ای از اقتدار، اصالت و پیوند با نام علی (ع)
💰
جمع کل در خرید تکی: ۱,۳۲۴,۰۰۰ تومان
🔥
قیمت ویژه کل پک: ۱,۱۱۰,۰۰۰ تومان
⏳
موجودی این پک کاملاً محدود است.
📩
ثبت سفارش و مشاوره:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
.com</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/687355" target="_blank">📅 11:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687354">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202db681fc.mp4?token=JXUAM9BudK9CdFqa_rCCRDIgx73Lxxa-p5u_jtcg7UrdftNGwjkx6rNc4t7d7zK4RLUT7KfjSkJxRghrHMx1BRl3gjMH6GvhRcQNBh44sMaVxN9ry2R2tCj-_GZzvqbLEFOuIiEdxeGV8DD5VaqpnweVLwucj4zGhEMMBjytM1yxF_KmX9so3PbrcywkhITPV3a_n9phxM7h11tBRbhc2kgS2YoTXC0XlEssTzX9i-pVrScXwhjuaIS3bPRYPauJYbU0wqr7rFMSuiuTo1wowCYxCPArFvWMfrnmG1fVf8UX2ThfwlSz4OzpUXVRdk7kM8_ZlK_-ishJXHBD97mtyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202db681fc.mp4?token=JXUAM9BudK9CdFqa_rCCRDIgx73Lxxa-p5u_jtcg7UrdftNGwjkx6rNc4t7d7zK4RLUT7KfjSkJxRghrHMx1BRl3gjMH6GvhRcQNBh44sMaVxN9ry2R2tCj-_GZzvqbLEFOuIiEdxeGV8DD5VaqpnweVLwucj4zGhEMMBjytM1yxF_KmX9so3PbrcywkhITPV3a_n9phxM7h11tBRbhc2kgS2YoTXC0XlEssTzX9i-pVrScXwhjuaIS3bPRYPauJYbU0wqr7rFMSuiuTo1wowCYxCPArFvWMfrnmG1fVf8UX2ThfwlSz4OzpUXVRdk7kM8_ZlK_-ishJXHBD97mtyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبتی زیبا از جغد گوش دراز (شاخدار)
🔹
حامد شریفی، شهریور ۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/687354" target="_blank">📅 11:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687353">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65615080a7.mp4?token=cBBCl1demibeRJ6blEGxGy07UPHmABwQUwjiF8YCyosrxd9YAWrKSEpS3RbYqrYAgLFt2Jf677ocmE2yO6RteXf5l4DeF3fjxE6R7b82g2nYtrPqok-3iEgNmieNCiiVzVsHLhip0o8lUJ9HBsYwsG4jDIyGp0La8sJwGU41D855_S8pAvFUXR6ucBvth-qjxZpLGSKUTqObR6W7YhBuhwwza-WIfwanoL4zYzqnVQeNhhRk5H5laIststaLqM3PCMXFIKkiqNfuEXZo-JdNNB66H46bdXz9y1lezM7g7Tf6eq0H7JnBIZzJDz8Z9APL2ySRaR4qikQxi3M04mZWEpGRQGjZaYIZK0vHM26Bq5XLBPP1qO8Cextc6iGyp-YIq8EWa4CaJB1MACT0zqQFQLYJuZw1TDxwrjMYW4kbAvC2ONOCrFPuyfSh-LxUxyV8PxbXfRd-OhZ6IQWr5hf1Q5ZY0_p2lmcAsT4BUFjfl1AA4pAmTMyTod0zkTB9aPG9X8yH3U4HYJCQnu8eKctpczTkT8T098b_HwsTCXFi3rkoz9LmSHH7o6LKCUpISr3ApTiolAZCdDEynkgUEZwHRW5Enf9GudAMhm4m67dc5vsKXb8cloXr0a1GMorTCHg4S06ichehYIh5-WQb-h2Do9KUrFUgm0WKpizwllJxKcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65615080a7.mp4?token=cBBCl1demibeRJ6blEGxGy07UPHmABwQUwjiF8YCyosrxd9YAWrKSEpS3RbYqrYAgLFt2Jf677ocmE2yO6RteXf5l4DeF3fjxE6R7b82g2nYtrPqok-3iEgNmieNCiiVzVsHLhip0o8lUJ9HBsYwsG4jDIyGp0La8sJwGU41D855_S8pAvFUXR6ucBvth-qjxZpLGSKUTqObR6W7YhBuhwwza-WIfwanoL4zYzqnVQeNhhRk5H5laIststaLqM3PCMXFIKkiqNfuEXZo-JdNNB66H46bdXz9y1lezM7g7Tf6eq0H7JnBIZzJDz8Z9APL2ySRaR4qikQxi3M04mZWEpGRQGjZaYIZK0vHM26Bq5XLBPP1qO8Cextc6iGyp-YIq8EWa4CaJB1MACT0zqQFQLYJuZw1TDxwrjMYW4kbAvC2ONOCrFPuyfSh-LxUxyV8PxbXfRd-OhZ6IQWr5hf1Q5ZY0_p2lmcAsT4BUFjfl1AA4pAmTMyTod0zkTB9aPG9X8yH3U4HYJCQnu8eKctpczTkT8T098b_HwsTCXFi3rkoz9LmSHH7o6LKCUpISr3ApTiolAZCdDEynkgUEZwHRW5Enf9GudAMhm4m67dc5vsKXb8cloXr0a1GMorTCHg4S06ichehYIh5-WQb-h2Do9KUrFUgm0WKpizwllJxKcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار دوباره شاگرد و استاد بعد از ۳۰ سال
🔹
سید ستار هاشمی، وزیر ارتباطات، بعد از ۳۰ سال به دیدن مصطفی کرمانی، از پیشگامان آموزش کامپیوتر در دانشگاه اصفهان رفته است. استادی که روزی در کلاس‌های «اسمبل» و سیستم‌عامل پای درسش می‌نشست.
🔹
اگرچه استاد کرمانی در بستر بیماری است، اما به شاگرد قدیمی‌اش می‌گوید: «تاثیری که در حال حاضر شما می‌گذارید به مراتب بیشتر از شرایط عادی است. قدر زمان خودتان را بدانید و ناامید نشوید.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/687353" target="_blank">📅 11:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687352">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی شورای نگهبان: زمان برگزاری انتخابات شوراها در اختیار شورای عالی امنیت ملی است و به صورت الکترونیک خواهد بود.
🔹
عارف: اعلام لیست کشته‌شدگان حوادث دی‌ماه تدبیر رهبر شهید بود.
🔹
شبکه ۱۲ رژیم صهیونیست: ۸۳ درصد از اسرائیلی‌ها نتانیاهو را مسئول شکست ۷ اکتبر می‌دانند.
🔹
سپاه اصفهان از احتمال شنیدن صدای انفجار در جنوب اصفهان خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/687352" target="_blank">📅 11:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687351">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
طحان‌نظیف: طرح جدید مهریه در نوبت بررسی شورای نگهبان قرار گرفت  سخنگوی شورای نگهبان:
🔹
طرح جدید مرتبط با موضوع مهریه و احکام پیرامونی آن به شورای نگهبان واصل شده و در نوبت رسیدگی قرار گرفته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/687351" target="_blank">📅 11:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687350">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc6c9235.mp4?token=ov2bKo8LsBoYJj5hK1-rhwBJzP3FZmMikBfNmfGWa0CYTXYCjGmSkn2srYnglK1RXN4DCjM4hKuNEl9ZPc1umx8EaKh3LX6SIqF0utcsBIZNhU_51jYiQRosjFcvM_v_V-MqDF0ewQORvIFGM1s8u1t6CRdKG3sy5t8b8zCqDOEcr2rfz28dN1Rgka7JrxUvGwH2VUihOoWiPHNaQqNgeHxwKiU-wzuIATibg5TW5jxyK_iQb8r4rwA7Wj9m6vodgrVxr4EIIUpWVvZvI1a4G1YMR1QoSdAcgyjSngSTcKFMaztwQs1AhMQoKR5dpSOtG7gWIOjqeQYHvp5LYg-o4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc6c9235.mp4?token=ov2bKo8LsBoYJj5hK1-rhwBJzP3FZmMikBfNmfGWa0CYTXYCjGmSkn2srYnglK1RXN4DCjM4hKuNEl9ZPc1umx8EaKh3LX6SIqF0utcsBIZNhU_51jYiQRosjFcvM_v_V-MqDF0ewQORvIFGM1s8u1t6CRdKG3sy5t8b8zCqDOEcr2rfz28dN1Rgka7JrxUvGwH2VUihOoWiPHNaQqNgeHxwKiU-wzuIATibg5TW5jxyK_iQb8r4rwA7Wj9m6vodgrVxr4EIIUpWVvZvI1a4G1YMR1QoSdAcgyjSngSTcKFMaztwQs1AhMQoKR5dpSOtG7gWIOjqeQYHvp5LYg-o4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علم منتظر معجزه نمی‌ماند!
🔹
واکنش کودک هنگام استفاده از اولین عینک جالب توجه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/687350" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687349">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c946fa0b1.mp4?token=etdiBpOnURIhFlaGKB6uD__9nZEehi3fXapou_uNIVwAqwSwKkei_Yvx816v9qHBX0cESoMMCrN_fQ-ot5MofFrU3udWd6Y5w_o08RH0odQ10AF5orkhqHChQgm6kNvrxbZi_I6d93qVtl1LCHcqr_FBX4n3oqAJoKPbZL9Czz642uHcSkiX2JP6vciEU3ws5gNQ8YTna3LM_alzK2xJhyuFkFONqOYyfiw2M6ogn2a4vy9AcimkM1hZneAtvfe8taQMrhomy2a5Iadsg2UuKpXHIDGXZN5WrDHg77nthj2ybHv5NRFASTyW6uY0P4GZh977jHy-ZPbwZDhjxYgwgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c946fa0b1.mp4?token=etdiBpOnURIhFlaGKB6uD__9nZEehi3fXapou_uNIVwAqwSwKkei_Yvx816v9qHBX0cESoMMCrN_fQ-ot5MofFrU3udWd6Y5w_o08RH0odQ10AF5orkhqHChQgm6kNvrxbZi_I6d93qVtl1LCHcqr_FBX4n3oqAJoKPbZL9Czz642uHcSkiX2JP6vciEU3ws5gNQ8YTna3LM_alzK2xJhyuFkFONqOYyfiw2M6ogn2a4vy9AcimkM1hZneAtvfe8taQMrhomy2a5Iadsg2UuKpXHIDGXZN5WrDHg77nthj2ybHv5NRFASTyW6uY0P4GZh977jHy-ZPbwZDhjxYgwgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات جدید از حادثه نفتکش در خارک؛ تلفات گزارش نشده است  طبق گزارش منابع محلی:
🔹
نفتکش هدف قرار گرفته‌شده در جزیره خارک، یک نفتکش کوچک بوده است.
🔹
بر اساس این گزارش، این حادثه تلفات جانی نداشته است./ خبرگزاری‌دانشجو   #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/687349" target="_blank">📅 11:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687348">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
توییت «زینب عواضه» خبرنگار شبکه المنار لبنان(رسانه رسمی حزب‌الله): اعلام سیطره بر تپه علی الطاهر من را به شدت یاد اعلام سیطره بر تنگه هرمز توسط ترامپ می‌اندازد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/687348" target="_blank">📅 11:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687347">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2894debbb1.mp4?token=eJ4Uq8dnPyF9f6r7aJSUJyp0llFlNRQpNZaBtObxtB7s6pck6d3Gmc_pwkmLHMCtsIASr9OwYUMnhd73dEfcVg6uo7_-J1zw9EC_zXbYzdSMTp3WdYVDY-PDIUaAAMMr1SPZYoMtXyCVJfJM3mvzlLKyzJydZn326IB6HXJJGMGgk4yeorbQkhmZ26ZxOAG1ezfGmCMTvf-3OlSDBcWO1wMXsm9rNLaq77Fi-y8qNRdpei5Sxw8-mYvazCpg_jAvweuJrV-BqgXghXn80g-Dv_-DUsrGuGaxriu1W76ROoo-MgewxWBvDHpBg9-cxzV4CCvBVgA5oznX6ZB9Pujdww9C0na2b5lUJSZ2s-2U0iNCpkh1Ox1h1u-sUbJPSFcLe5Ay6LGwQutxWDjFLoh31U4xu_gmaAA1i51jV9lfaNkyIEMJ4_9_X4INiqUoYlnt6RILWGbJpLVLElDeAwo-eDB4sbIP1WjA7BCXWsIVXjbYz9wX2rB5N5CF2UKjhaCCH_BeqpGdON6iFvmc_GBYuELlgYvKFR3RMYtHAbFxjmrfHRkHCf2SGCW9M2R6P16_sXO5ikMzHrUMLAQKUGHz7L9I6xHsTnDZrvVHPJa0MgsuzXSbqjbL0E2EOopKd4u-GlIF02gEDs3v54lSsRjUStMe6XPAER_Kt6QzCrm-sOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2894debbb1.mp4?token=eJ4Uq8dnPyF9f6r7aJSUJyp0llFlNRQpNZaBtObxtB7s6pck6d3Gmc_pwkmLHMCtsIASr9OwYUMnhd73dEfcVg6uo7_-J1zw9EC_zXbYzdSMTp3WdYVDY-PDIUaAAMMr1SPZYoMtXyCVJfJM3mvzlLKyzJydZn326IB6HXJJGMGgk4yeorbQkhmZ26ZxOAG1ezfGmCMTvf-3OlSDBcWO1wMXsm9rNLaq77Fi-y8qNRdpei5Sxw8-mYvazCpg_jAvweuJrV-BqgXghXn80g-Dv_-DUsrGuGaxriu1W76ROoo-MgewxWBvDHpBg9-cxzV4CCvBVgA5oznX6ZB9Pujdww9C0na2b5lUJSZ2s-2U0iNCpkh1Ox1h1u-sUbJPSFcLe5Ay6LGwQutxWDjFLoh31U4xu_gmaAA1i51jV9lfaNkyIEMJ4_9_X4INiqUoYlnt6RILWGbJpLVLElDeAwo-eDB4sbIP1WjA7BCXWsIVXjbYz9wX2rB5N5CF2UKjhaCCH_BeqpGdON6iFvmc_GBYuELlgYvKFR3RMYtHAbFxjmrfHRkHCf2SGCW9M2R6P16_sXO5ikMzHrUMLAQKUGHz7L9I6xHsTnDZrvVHPJa0MgsuzXSbqjbL0E2EOopKd4u-GlIF02gEDs3v54lSsRjUStMe6XPAER_Kt6QzCrm-sOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طحان‌نظیف: طرح جدید مهریه در نوبت بررسی شورای نگهبان قرار گرفت
سخنگوی شورای نگهبان:
🔹
طرح جدید مرتبط با موضوع مهریه و احکام پیرامونی آن به شورای نگهبان واصل شده و در نوبت رسیدگی قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/687347" target="_blank">📅 10:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687346">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171ae681fb.mp4?token=lB7OrpaGayCfadnOrMNWB_3WNFpVYjvYN8ACOIAh6GGGZx6X6EErA5HCeDZyC25FH6ZrCSy3vCLA5apqWDKA9DNAmF8x3zUi3B9j3zd50rlzoYwc3leDVMrjQBw3sxrm2_of646ztaRZm83jiW4DOSKIA0sGKygnww9bPz0j5W6Vl1aIf7tLyIWBa6RlTup0RjDdiBAxQbdBM89iJ67Jtc1rBOjFmivzPzNkzbGWyd8_2BYmYplyVLehlKFRPrxh3rSWrPG5QA82mx34ogAUdkWAX_VQZmZjmCWtloiZXiLwsqCBZIy9kLn-vNWyHa5uBy4ZH0FVnwfKiqqhn7U1Al0OmMYxD9SOuwytYudoXsmSwVwbWSzQhU6BSVcvlZ8c0nkr8Ql1yexr3qop0CG94F1EclwuyqE2aNVSc5ZFIzxcoEt5BtsoIEYysGJ5WStz_GCf-ZLRA5GX_nlh4BafvHrIRI86x7zTP5PzS7t3wxAnqPMOxIzKKzlBFNdOy8yC5srCkcEH2lhXMVYSnYGkudPzRcu83tLf2Jpo7hgbHijAO7-ZFMK6mwMHzWebGXtYzavIygIPHmUGGyRIIB1cand3uiwC7_t_3ECzpOIM7r6eG57WwZ5hYs1AQ8SbPgcwctkNswf33-jAvUtwFjzySlZU-lg7Nj_rYS1yFovU1DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171ae681fb.mp4?token=lB7OrpaGayCfadnOrMNWB_3WNFpVYjvYN8ACOIAh6GGGZx6X6EErA5HCeDZyC25FH6ZrCSy3vCLA5apqWDKA9DNAmF8x3zUi3B9j3zd50rlzoYwc3leDVMrjQBw3sxrm2_of646ztaRZm83jiW4DOSKIA0sGKygnww9bPz0j5W6Vl1aIf7tLyIWBa6RlTup0RjDdiBAxQbdBM89iJ67Jtc1rBOjFmivzPzNkzbGWyd8_2BYmYplyVLehlKFRPrxh3rSWrPG5QA82mx34ogAUdkWAX_VQZmZjmCWtloiZXiLwsqCBZIy9kLn-vNWyHa5uBy4ZH0FVnwfKiqqhn7U1Al0OmMYxD9SOuwytYudoXsmSwVwbWSzQhU6BSVcvlZ8c0nkr8Ql1yexr3qop0CG94F1EclwuyqE2aNVSc5ZFIzxcoEt5BtsoIEYysGJ5WStz_GCf-ZLRA5GX_nlh4BafvHrIRI86x7zTP5PzS7t3wxAnqPMOxIzKKzlBFNdOy8yC5srCkcEH2lhXMVYSnYGkudPzRcu83tLf2Jpo7hgbHijAO7-ZFMK6mwMHzWebGXtYzavIygIPHmUGGyRIIB1cand3uiwC7_t_3ECzpOIM7r6eG57WwZ5hYs1AQ8SbPgcwctkNswf33-jAvUtwFjzySlZU-lg7Nj_rYS1yFovU1DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال مردم هند از اژه‌ای/برخی از هندی‌ها دست رئیس قوه قضاییه را می‌بوسند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/687346" target="_blank">📅 10:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687345">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
منابع امنیتی عراقی: پایگاه هوایی الحریر آمریکا در حال تخلیه کامل است
خبرگزاری المعلومه:
🔹
منابع امنیتی اعلام کردند روند خروج نیروهای آمریکایی از پایگاه هوایی الحریر در اقلیم کردستان ادامه دارد و انتظار می‌رود این پایگاه تا پیش از هشتم مهر ماه آینده بطور کامل تخلیه شود./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/687345" target="_blank">📅 10:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
حسن روحانی: امروز باید کاری کنیم که جنگ عزتمندانه پایان یابد
🔹
حالا شاید کسی بخواهد تا روز قیامت بجنگد!
🔹
یک اقلیتی بوق و بلندگو دارد و سروصدا می‌کند، این افراد غیر از اکثریت جامعه هستند.
🔹
تنگه هرمز هم نباید تنگه جنگ باشد؛ از تنگه بی‌رونق که هیچ کشتی عبور نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/687343" target="_blank">📅 10:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687342">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp9SKvdSY4iHnjPJo71qvNBVN_Yy8UwjhjHylW9S0fvLTZdUSEoJKCyua8cLrWOr9wBEHFCGCdEBIuLUgqbdPS6HCC0IvuTlrjtHvy0OffvONks385FJo_RKL-XGe0oQua7Y7mZ_YU2IPMdvEBtZNsJ1PCvJLRzXs_2RMFUZNLPD17Q0AYQ1ItOeoBztWAYDdT4clQAKiXpRdMMOR6qEasf6h-SN8HhLLtvFFvKR1QhaM5GYVtcQIN813jlQPeJwBmGR7EQSp7KdC7u7xdo0mvTwoVYdHxCURQ5uWTMOc-jKeaE5-f_uuJtjkkNlavq3fXCuRLMN5FmINMmkyVYrjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موسی رضایی، رئیس‌کل بیمه مرکزی: تحول دیجیتال؛ یکی از برنامه‌های اصلی صنعت بیمه است
🔹
دکتر موسی رضایی، رئیس‌کل بیمه مرکزی در مراسم امضای تفاهم‌نامه بیمه مرکزی و سازمان نظام صنفی رایانه‌ای، گفت: یکی از برنامه‌های اصلی صنعت بیمه در دوره فعلی، اجرای تحول دیجیتال است. در همین راستا، سند تحول اقتصاد دیجیتال صنعت بیمه با حضور وزیر امور اقتصادی و دارایی رونمایی شد و برای اجرای و پیاده‌سازی این سند در صنعت بیمه، دوره‌های زمانی سه‌ماهه در نظر گرفته شده است.
🔹
رضایی افزود: روندهای دیجیتالی‌شدن به شفافیت صنعت بیمه کمک می‌کند. در تدوین این سند تلاش شده است از کلیه تجربیات گذشته بیمه مرکزی، پژوهشکده بیمه و سایر ظرفیت‌های موجود استفاده شود. یک کمیته تحول دیجیتال نیز تشکیل شده است.
🔹
رئیس‌کل بیمه مرکزی تأکید کرد: از همه ظرفیت‌های فعال بازار بیمه استفاده شده و بازیگران اصلی تحول دیجیتال در صنعت بیمه، اینشورتک‌ها و شرکت‌های بیمه هستند. مسئله امنیت سایبری در شرایط امروز از اهمیت بسیار بالایی برخوردار است و هدف ما، استفاده از ظرفیت سازمان نظام صنفی رایانه‌ای در مسیر تحول دیجیتال صنعت بیمه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/687342" target="_blank">📅 10:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687340">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
حاوی تصاویر دلخراش| ویدیویی وحشتناک از یک تصادف!
🔹
هنگام عبور از حاشیه خیابان بسیار دقت کنید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/687340" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687339">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیریت بحران استانداری اصفهان: صدای انفجار جنوب اصفهان؛ انهدام مهمات عمل‌نکرده است.
🔹
رئیس قوه قضائیه: از اعضای بریکس می‌خواهیم در کنار قانون بایستند.
🔹
انفجارهای مهیب صهیونیستی، «زوطر الشرقیه» در جنوب لبنان را به لرزه درآورد.
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/687339" target="_blank">📅 10:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687338">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ماجرای ۱۴ سکه مهریه؛ پابند الکترونیکی جایگزین حبس می‌شود؟
عاطفه حاذق، وکیل دادگستری:
🔹
مهریه ۱۴ سکه نشده است؛ بلکه کاهش عدد ۱۱۰ به ۱۴ سکه، مربوط به ضمانت اجرای قانونی و شرایط حبس است.
🔹
به گفته او، مهریه همان مبلغ درج‌شده در عقدنامه است و زن همچنان می‌تواند تمام آن را مطالبه کند؛ ۱۴ سکه فقط به بحث ضمانت اجرای قانونی مربوط می‌شود.
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/687338" target="_blank">📅 10:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687337">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e280b2a3f.mp4?token=jAyTeJsMHJSnFec264sBs_MqnlTM093yABZOED1x82GWtlVWkedZqu-w5cGVHgYVh_SbHsxJ4iLG9j2CJQnRnY4ZPEq7Or0AmgmccM8U59RrODAXWKf2Y-B_-ODHXW_wXrRRFVYHcIkdcRrTFAM7S0Ks_285fvWL2RUtJDciukb1B8JxZ3pTXHLvQ4p1mbB4vj8-EVCUpn8ltaKA4XqOEi4Md6bBK5M4eoIkd1u6w-QQNSeuSF4Yd2ihu3Cy-0Ds9IX4QkUKEjj4eghS1w-wnUprcvNfiErIbBeNDSazi5A0BSSk2Tck0WChfDk3FtC63wJpc_GkxDw3ji3WpRIT0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e280b2a3f.mp4?token=jAyTeJsMHJSnFec264sBs_MqnlTM093yABZOED1x82GWtlVWkedZqu-w5cGVHgYVh_SbHsxJ4iLG9j2CJQnRnY4ZPEq7Or0AmgmccM8U59RrODAXWKf2Y-B_-ODHXW_wXrRRFVYHcIkdcRrTFAM7S0Ks_285fvWL2RUtJDciukb1B8JxZ3pTXHLvQ4p1mbB4vj8-EVCUpn8ltaKA4XqOEi4Md6bBK5M4eoIkd1u6w-QQNSeuSF4Yd2ihu3Cy-0Ds9IX4QkUKEjj4eghS1w-wnUprcvNfiErIbBeNDSazi5A0BSSk2Tck0WChfDk3FtC63wJpc_GkxDw3ji3WpRIT0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین بازی ویدیویی جهان! ساخته شده در سال ۱۹۵۴
🕹
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/687337" target="_blank">📅 10:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687336">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
رسانه آمریکایی ام اس ناو: درخواست نظامیان آمریکایی برای خروج از ارتش در اعتراض به جنگ با ایران ۶ برابر شده است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/687336" target="_blank">📅 10:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687335">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
نفتکش ایرانی در جزیره خارک هدف حمله موشکی آمریکا قرار گرفت
🔹
بنابر گزارش منابع محلی یک نفتکش ایرانی در جزیره خارک هدف موشک نیروهای آمریکایی قرار گرفته است./ خبرگزاری‌دانشجو  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/687335" target="_blank">📅 10:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687334">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbd885974.mp4?token=u2kfAwoOISlMqc2LibIHhNr0_JI2Rs-WreIqRcIVQwLaMbhyHAMzz319Ctsz0Gs9Ay1kX_0B9nYt4r2r7qALKqLbG_QPaHa_2aIQIwhEL_sdJfEvB2w21OiYhXvlH6zfNKcATj93OWLfhunFMZHlUeOUyd1ssE7B0trKsXsYumTYH6gxGJllGntyjSQglqpdf9yImnGCKBs-OnWHzq2HSmQaqEG_njbKU5wTI8vu9PvwqmMMPqcQe_p3evX5cIwuCZ_ihOhPdU5rYwrpSQ8sV2ryX-lxALhmNF1EPiIUWM4FN29F_njOnHJcIxZg3PtzzDCqNAmsU_K6NG5_4NEeRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbd885974.mp4?token=u2kfAwoOISlMqc2LibIHhNr0_JI2Rs-WreIqRcIVQwLaMbhyHAMzz319Ctsz0Gs9Ay1kX_0B9nYt4r2r7qALKqLbG_QPaHa_2aIQIwhEL_sdJfEvB2w21OiYhXvlH6zfNKcATj93OWLfhunFMZHlUeOUyd1ssE7B0trKsXsYumTYH6gxGJllGntyjSQglqpdf9yImnGCKBs-OnWHzq2HSmQaqEG_njbKU5wTI8vu9PvwqmMMPqcQe_p3evX5cIwuCZ_ihOhPdU5rYwrpSQ8sV2ryX-lxALhmNF1EPiIUWM4FN29F_njOnHJcIxZg3PtzzDCqNAmsU_K6NG5_4NEeRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوتلاچ یک دسر ترکیه‌ای خیلی پرطرفدار و خوشمزه مناسب برای صبحانه یا میان‌وعده
😍
مواد لازم:
🔹
برنج نیم دانه ۱ لیوان
🔹
شیر ۱/۵ لیتر
🔹
آب ۱ لیتر
🔹
شکر ۲۰۰ گرم
🔹
وانیل ۱ قاشق چای‌خوری
🔹
زرده تخم مرغ ۲ عدد
🔹
نشاسته ذرت ۲۵ گرم #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/687334" target="_blank">📅 10:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687333">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b50a317b.mp4?token=GHF7rfNgX_MALevzM0mRL5ST7_RVVbLk47AH52CmEk8-7DBDNvG_q73uld3Uxw868gc9VLCyJAZWYmaKcHjJWLFMxeLdU9uwBXsQntvIqLfAE8N3kOvU7o54L84u1-YfUEAjEHC86gn7c52eoNSVoSTUaFcabnzuIUm1mhx2OFXykbaJC5DTZXLRkgkyvIQKW_Au06y3h2MYZO5sQga46NMHStNFmEH3PBaD2zkh-M0f7s-wZ45ug2zULT92_tcUjRIwZTFgIbEuC2o2DHMgBVpELQGjgK-b73lQEwxihTBq5p2r6fyyKSUCYCp0q1UNt6_zIrwTVFEybvUe90mWyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b50a317b.mp4?token=GHF7rfNgX_MALevzM0mRL5ST7_RVVbLk47AH52CmEk8-7DBDNvG_q73uld3Uxw868gc9VLCyJAZWYmaKcHjJWLFMxeLdU9uwBXsQntvIqLfAE8N3kOvU7o54L84u1-YfUEAjEHC86gn7c52eoNSVoSTUaFcabnzuIUm1mhx2OFXykbaJC5DTZXLRkgkyvIQKW_Au06y3h2MYZO5sQga46NMHStNFmEH3PBaD2zkh-M0f7s-wZ45ug2zULT92_tcUjRIwZTFgIbEuC2o2DHMgBVpELQGjgK-b73lQEwxihTBq5p2r6fyyKSUCYCp0q1UNt6_zIrwTVFEybvUe90mWyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
𝟲𝟬% و %𝟳𝟬 تخفیف تمامی کالاها
در جشنواره پایان تابستان «چرم مَنطِـ»
➕
𝟮 میلیون تومان هدیه اسنپ‌پی
با کد: 𝐏𝐀𝐘𝐂𝐖𝐆𝐙𝟓
در تمامی شعب و سایت
👇
🌐
manteofficial.com
با اسنپ‌پی بخر، 𝐁𝐌𝐖 ببر</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/687333" target="_blank">📅 10:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687332">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/687332" target="_blank">📅 09:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
چراغ سبز آمریکا به فروش میلیاردی تجهیزات نظامی به عربستان، عمان و عراق
🔹
منابع رسانه‌ای گزارش دادند که آمریکا با مجموعه‌ای از قراردادهای تسلیحاتی با عربستان سعودی، عمان و عراق به ارزش بیش از ۶ میلیارد دلار موافقت کرده است.
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/687331" target="_blank">📅 09:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687330">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
نفتکش ایرانی در جزیره خارک هدف حمله موشکی آمریکا قرار گرفت
🔹
بنابر گزارش منابع محلی یک نفتکش ایرانی در جزیره خارک هدف موشک نیروهای آمریکایی قرار گرفته است./ خبرگزاری‌دانشجو
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/687330" target="_blank">📅 09:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130280e12c.mp4?token=JwB3JBojn3jHjrrivUIb5to1TjdBLSEx0aNMHiTjvS4tnmSD11CjA-1NDuS2iwRQY4OZgUl6LZ_tszraNd-h0QNLqOOUFxemIDvEUjxR4AbtBQ6_BlQ7bGYmCj3GqQG5y-CBxj38KzLher1bIOPubSKK7e9t0HZzxygyr8Zk7cBQPxHG0X3ahoEr3L6FllbxhfEg9e8bKK_UaGPhoWqY6YxFCafl_EIU1R9ILVNHBXOaeFRdnvCX0vvIXlUPjkcI4WOFdnZM7ZgLNAwgTKsz7YX0x5VbpzIPxX7158iPrQr7iqBLqog-p0TbLMCVO23X8tcwauXbCDBL1C7tvZdPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130280e12c.mp4?token=JwB3JBojn3jHjrrivUIb5to1TjdBLSEx0aNMHiTjvS4tnmSD11CjA-1NDuS2iwRQY4OZgUl6LZ_tszraNd-h0QNLqOOUFxemIDvEUjxR4AbtBQ6_BlQ7bGYmCj3GqQG5y-CBxj38KzLher1bIOPubSKK7e9t0HZzxygyr8Zk7cBQPxHG0X3ahoEr3L6FllbxhfEg9e8bKK_UaGPhoWqY6YxFCafl_EIU1R9ILVNHBXOaeFRdnvCX0vvIXlUPjkcI4WOFdnZM7ZgLNAwgTKsz7YX0x5VbpzIPxX7158iPrQr7iqBLqog-p0TbLMCVO23X8tcwauXbCDBL1C7tvZdPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکله بندرگز؛ قاب تماشایی خلیج گرگان
#اخبارفوری_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/687329" target="_blank">📅 09:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
عرضۀ واکسن آنفلوانزا اوایل مهر
سازمان غذا و دارو:
🔹
با وجود تأخیر تولیدکنندگان خارجی، افزایش قیمت و مشکلات نقل‌وانتقال مالی و حمل‌ونقل، واکسن آنفلوانزا از اواخر شهریور و اوایل مهر در دسترس قرار خواهد گرفت.
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/687328" target="_blank">📅 09:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687327">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f22774836.mp4?token=Y0tgvfezHh6DwBByOCWhZjcPlj5hwPwDtjHlJIJA7DEFJ3JUg2C44riBYyEZRWbNSWqwkjF-0OGSi-FlxdGn2bghP611CoQgWlDWK-sRStR9QAYcObCjxVXwkWUfo5U29vYIrvinEcJ7Sc-p_jzUpqiUa3QVCtvpVMOOJhkSO0p589pVhgaOWjXr2Oh4c7EWBey0yMAa1hufYlD6BRMUw-eM3GDTp8pjVWm1EAy9OcUUYwcLTlnP3Ozf-Eu5qmLhvm97IqHEJa6scawaoINaoEyt1vG6K3J3wEKaF-sfFgOxSPwyyn_K_jb9bQnRNEZnjqtJIbqF8byacEgzupWW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f22774836.mp4?token=Y0tgvfezHh6DwBByOCWhZjcPlj5hwPwDtjHlJIJA7DEFJ3JUg2C44riBYyEZRWbNSWqwkjF-0OGSi-FlxdGn2bghP611CoQgWlDWK-sRStR9QAYcObCjxVXwkWUfo5U29vYIrvinEcJ7Sc-p_jzUpqiUa3QVCtvpVMOOJhkSO0p589pVhgaOWjXr2Oh4c7EWBey0yMAa1hufYlD6BRMUw-eM3GDTp8pjVWm1EAy9OcUUYwcLTlnP3Ozf-Eu5qmLhvm97IqHEJa6scawaoINaoEyt1vG6K3J3wEKaF-sfFgOxSPwyyn_K_jb9bQnRNEZnjqtJIbqF8byacEgzupWW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: همه بدانند بنده تا نفس میکشم، اجازه نخواهم داد که بیگانگان با مصالح ایران بازی کنند/ من هم که نباشم، هرکس دیگری در این مسئولیت باشد، همینطور خواهد بود/ تا اصل نورانی ولایت فقیه در قانون اساسی هست، نخواهند توانست بنای مستحکم نظام را متزلزل کنند
🔹
انتشار به مناسبت ساعت ۰۹:۴۰ صبح شنبه؛ ساعت شهادت حضرت آیت‌الله العظمی سیدعلی خامنه‌ای رضوان‌الله‌علیه
🇮🇷
‌
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/687327" target="_blank">📅 09:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687326">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0znptqbaPKlxqsThNIBlDYXfgKK4hur-E-DsHbX7ySKnNkC4PaBY2PigJDfzjC1B8nXoYHUE6H4BjTpbDJqZlotHB35q6SSCfC7OdU2N3u2GBw9_egjF1qvHittYJ58AMQWdgystL3Oi4H-nq1YnVUe4OwFiliPRuvhomzhE2VUka8lRQtav3XvICvz40KFXK96zwJP4Uyh9nIgMyoqCQRA57boA2DCEh-BxL7TyeqzcjWt4fQHX5w8KKSX_H3zWswOxbnIhu2evXUTUn01hQiArl7m5QXksXS0aq4vMkch9mIPqeVauDiJgzESWeVFc9YuSe7xcboLV2P7LkyJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراقب اکانت‌های بدل تلگرام باشید؛ دام فیشینگ در یک پیام
🔹
هشدار درباره شگرد جدید کلاهبرداری در تلگرام؛ هکرها با اکانت‌های مشابه و استفاده از حروف غیرانگلیسی مثل
g
، کاربران را به صفحات فیشینگ یا فایل‌های مخرب هدایت می‌کنند.
🔹
پیش از کلیک، یوزرنیم فرستنده را با دقت بررسی کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/687326" target="_blank">📅 09:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687325">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAri4dnOsswnkYuzBnYJBRfpraFoi390qJjd56_EfJr4Ch7_MFYZv6IyzAftP8YXzElOBApcProjapcpnnLPYwTtyzyHm_VIg57SCxG1sIBbuWUm-hxa7pjIjfQvDUK8xcQjh-q20v4-tTYiE2ExyMHjrFwVfZf5DT1nICROVzQ0dvcjlobDDTtIthRsmRe7xnZltz12hyZG2K4v75BUkkQ9_EVDoDyWtXoVEv_m2N1gZ86pgfMI-2PxjXX_wyy4QvxZ9krkuAFup-w54h4uWsQeD8qT8UYQcJ3EiIuC9xoKJXD7IujyHKVJwGGnPqzAsH3uFByfM6f3MVcc6XVumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/687325" target="_blank">📅 09:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687324">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsWASrxK-HCxCAlbmxsaf-fRkS9CnRIU2LAMtou1xT0miv2RxHLDVYPd-tBVknZNdqSfdJkgs7BcARZOFVBLLFnQoO-PSNzlM4uGLP_aXXSUo7xi6hPpIBwNaWf-Bn784IhXQZBQ8__WpyhSBzEh7E-Uk33UxgyGGryI9LHu0ur9kE-dKkgokfVVL-0B9O3FbGlTNjLZLjInZWgGlsviAgxHPHS2dBGRRC1fSxN7IA3t-w6uk_jInhQOUckpnyOZGotvWgJ4CbWLOPknsSFzvjtMOIxMSZX2FLGOU87A_fGMX0y-WAx5dFUGHGKMrT1J5rblkll86cKdjRQLaJ9YYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۱۲۰ هزار واحدی شاخص بورس تهران
🔹
شاخص کل بورس تهران ۱۲۰ هزار واحد رشد  و به تراز ۶ میلیون و ۶۲۴ هزار واحد صعود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/687324" target="_blank">📅 09:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687323">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06634bb837.mp4?token=kUBbru0q6KzrTY8Zpipl56hbfpwdMgOAd_jHj9RIidyg6UQaUlZJhK5A0hrQ0cOfgArR1uiYFjEXqoNwa8Az984UJusbQQIg-EErFwa7gwXxUDs-WVyWc43ARRYTvFcDQwjkndTJtkyU2VUqe98HdKbbgGA4wZPTOxROHHX1wCA4ie1NY5Q0fTCibUrnO6diQuHph0aDsokIX0v9TeyhEZ54lLBhekBRAJ3Gt58sZHXzX4swfVqAl6TwmkCCDoa7PUr984IUwR8p9O9bafXimRqr54_K-CrqZ_0P7k3gLk54e1iBODuqqQNB10jOnRNKl7geDpDBiyCydN83sSALdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06634bb837.mp4?token=kUBbru0q6KzrTY8Zpipl56hbfpwdMgOAd_jHj9RIidyg6UQaUlZJhK5A0hrQ0cOfgArR1uiYFjEXqoNwa8Az984UJusbQQIg-EErFwa7gwXxUDs-WVyWc43ARRYTvFcDQwjkndTJtkyU2VUqe98HdKbbgGA4wZPTOxROHHX1wCA4ie1NY5Q0fTCibUrnO6diQuHph0aDsokIX0v9TeyhEZ54lLBhekBRAJ3Gt58sZHXzX4swfVqAl6TwmkCCDoa7PUr984IUwR8p9O9bafXimRqr54_K-CrqZ_0P7k3gLk54e1iBODuqqQNB10jOnRNKl7geDpDBiyCydN83sSALdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاح مخفی واشنگتن؛ از ترور سیاسی تا جنگ مواد مخدر
🔹
روایتی از جان کریاکو بازرس اسبق کمیته روابط خارجی سنا در مورد اینکه امریکایی‌ها تعمدا اجازه گسترش مواد مخدر در افغانستان را دادند تا بخش مهمی از آن به ایران و رسیه ارسال شده و جوامع این کشورها تضعیف شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/687323" target="_blank">📅 09:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687322">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ae739fa6.mp4?token=o5U5xhC2Vf1wmkn0c2n6oDBxPVpQgsxdd68pLVtlohr0sXqFhnIBO2AHOy7qw4zuJziN5nm71NDiIr8gom-aVVy91ojvg849r6S9VkzsSL5mwjMsMfwqpgq9fOAoQuktv1sRFxuG5dZYVlmJfsaj-oZBqtxxBP9pYVzIdkrs3PLvev3E7laSGCKstVsWPpZBfOeNDm5Rx8SEj1ctwwXacI5BNm7Wqb865_h2_uHS5EIxDh2Ue9qF1C8gGakCRUPU2ptU-5SGjQ9HF7KoKN1VzbmUdepZvWMqiSFFnfEbuzR_lEk_RSuFJ8Dz5EKU5gHbWpKHSYFkutoEqDo2G5lYaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ae739fa6.mp4?token=o5U5xhC2Vf1wmkn0c2n6oDBxPVpQgsxdd68pLVtlohr0sXqFhnIBO2AHOy7qw4zuJziN5nm71NDiIr8gom-aVVy91ojvg849r6S9VkzsSL5mwjMsMfwqpgq9fOAoQuktv1sRFxuG5dZYVlmJfsaj-oZBqtxxBP9pYVzIdkrs3PLvev3E7laSGCKstVsWPpZBfOeNDm5Rx8SEj1ctwwXacI5BNm7Wqb865_h2_uHS5EIxDh2Ue9qF1C8gGakCRUPU2ptU-5SGjQ9HF7KoKN1VzbmUdepZvWMqiSFFnfEbuzR_lEk_RSuFJ8Dz5EKU5gHbWpKHSYFkutoEqDo2G5lYaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکسی‌های هوش مصنوعی تسلا؛ بدون راننده و فرمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/687322" target="_blank">📅 09:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687321">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
افزایش ۴۰ درصدی تقاضا برای خرید کالای دست دوم/ واردات لوازم خانگی دست‌دوم از طریق بازارچه های مرزی رونق گرفته است
🔹
جهش ۲ برابری قیمت لوازم خانگی طی یک سال اخیر، خریداران را به سمت بازار دست‌دوم سوق داده و رکود تورمی این حوزه را تشدید کرده است. فروش لوازم خانگی دست‌دوم در یک سال گذشته دست‌کم ۴۰ درصد افزایش یافته و برخی پیله‌وران بازارچه‌های مرزی نیز به واردات این کالاها از کشورهای اطراف روی آورده‌اند./ روزنامه اطلاعات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/687321" target="_blank">📅 09:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687320">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b3176880.mp4?token=VpXgwP73yVg29bMsoZZFNN5Qcl9yBcEFhdFNdaU7OfpT8jBbrFh7vAR4X41pI0dcAY3l4PiGkD6VP7PmGn53r_Js1W-P4diIQZOjstWedvK34NCYgdFy8GU7xqFNi0vAPNxg1sIwGMIIpf5nP6r1rTTma8Mz4rRHS6wnTLi37gO3dxt7bNCQjlk7nm5yqW5WFWEnODbZt0DhtcZRE94vTZY-m6YgvxtFGTZH1rA9enN8yHS0QE1sEWV-kSqU369_pwqGCs-J-ZC-IaQebrqab6JXYLwRd2u-1_N0TlzWXt1fEJoSOtkr0JCxbFh9r4e5kIrqWqik5kafSjZ8SFjFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b3176880.mp4?token=VpXgwP73yVg29bMsoZZFNN5Qcl9yBcEFhdFNdaU7OfpT8jBbrFh7vAR4X41pI0dcAY3l4PiGkD6VP7PmGn53r_Js1W-P4diIQZOjstWedvK34NCYgdFy8GU7xqFNi0vAPNxg1sIwGMIIpf5nP6r1rTTma8Mz4rRHS6wnTLi37gO3dxt7bNCQjlk7nm5yqW5WFWEnODbZt0DhtcZRE94vTZY-m6YgvxtFGTZH1rA9enN8yHS0QE1sEWV-kSqU369_pwqGCs-J-ZC-IaQebrqab6JXYLwRd2u-1_N0TlzWXt1fEJoSOtkr0JCxbFh9r4e5kIrqWqik5kafSjZ8SFjFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه قضاییه ایران در اجلاس روسای قوه قضاییه کشورهای عضو بریکس حضور پیدا کرد
🔹
حجت‌الاسلام‌والمسلمین محسنی اژه‌ای که به هند سفر کرده در روز سوم سفر خود در محل برگزار اجلاس روسای قوه قضاییه کشورهای عضو بریکس حاضر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/687320" target="_blank">📅 09:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687319">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نایب رئیس کمیسیون کشاورزی مجلس: کمبود نهاده‌های دامی نداریم
🔹
مدیرکل صنعت برق تهران: قطعی برق صنایع از سه روز به یک روز در هفته کاهش یافت؛ حذف خاموشی‌ها به‌زودی
🔹
انتخاب رشته داوطلبان آزمون کارشناسی ارشد ۱۴۰۵ دانشگاه آزاد تا ۲۰ شهریور تمدید شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/687319" target="_blank">📅 09:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687318">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
فردا کالابرگ خانوارهایی که رقم انتهای کد ملی سرپرست آنها ۰، ۱ و ۲ است و نیز خانوارهای حمایتی و نیروهای مسلح، شارژ می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/687318" target="_blank">📅 08:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687317">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
فردا کالابرگ خانوارهایی که رقم انتهای کد ملی سرپرست آنها ۰، ۱ و ۲ است و نیز خانوارهای حمایتی و نیروهای مسلح، شارژ می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/687317" target="_blank">📅 08:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687316">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge77OwNiSflrNI5VC-peURPLVyNvZ2N-2YIckjPB4izZpIUZeLb9Jgwinqmv9XqLuIbDVNJmwxRCMKZu2cdCXTzxqhuZuxc1Vddk6YATeHXCSQbtt-9Zem14mcOx9DnB0ySnrWQ940J9gjgqWlj9Jkq1xPtl2QuEZ6dUQZK_hhqY70_J8cTz-OuG8QXtKRtFefAFkoCOvJ9i7XUc-xzY9SOpRhZ_HVInN6kSA9pQV5yinMCaTfo-1XZYSWhxJoiWeRF5_mY2YBEppnJ6PwuE_s0-xjWOjvN9kIMsxIbR5FBqcNDhOsjhSOO-TsT0Mneqxa4iRm9IU0sT87C7WTpbsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از رابرت دنیرو ۸۳ ساله در کنار دختر ۳ ساله‌اش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/687316" target="_blank">📅 08:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687315">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
انگلیس: جنگ علیه ایران اقتصاد جهانی را تحت فشار قرار داده است
وزیر دارایی انگلیس در گفت‌وگو با فایننشال تایمز:
🔹
تداوم درگیری میان آمریکا و ایران، اقتصاد ما و جهان را با چالش‌های بی‌سابقه‌ای روبرو کرده است.
🔹
آنچه در خاورمیانه در حال رخ دادن است، مستقیماً بر نرخ تورم، میزان رشد اقتصادی و هزینه‌های استقراض تأثیر منفی می‌گذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/687315" target="_blank">📅 08:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687314">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd9d5689cd.mp4?token=Cu58DwY1rbIPOXvoZUxuxAqMgB3oozmS9Cmy8BOQENmc4ben3JKvJaxDRCCet1KH0PeD2L5LvGt75t0zbiju5ZPr7gRHP0yYGqwUZfW4WJBVXySp6KEax429b7lvI7Kl91BJK2CILhbYASDBhyBGpKKt21aiRd1yMsOw3oAjoCTL4gykljxr99GV12cNuB5XhZSnSFqa-DfulX7hp8fqszv4qKw854M5Jq8xHgpay4tobRsPuTk2sZGJZ39cFbQSPlQQW1a_TAXjjD7sVo7ncXfNODhTllFITq6nR1CJIRUOGOylknfRn2i8bty1-pp2uygbVSPaMRblAegDMp4EdJm61DhpAQ2yjQG1KlpTxbOlOMzhqr7h6lXHdJAELAyNEsxPNb6BKRWq8TntDlMXWHu__6QKbFKs1hnKWvcNSWJwHq3vzrm2I4h7_fEkU0zbgxotFUFhuA2-VHubd8E-zDbcB-laMhdFMxwPYcvfeSPE8lfBpYwFpdtNs91AaeB8j4V-UOiuTUSlYIiYS93y6dgstOSZjWz_jtLv2mcvhglC8VbVIX02ErQ-9pGPJAgeUEkDo6EtNXlbGBi_2JBK9po8C-_I0665oVZ-B7HR3DmoqlBM3dy8vbBFfob41mnPadNpeO2guTbygrbLkcdSA3JjQKdXhrm7EtA-UAKYQWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd9d5689cd.mp4?token=Cu58DwY1rbIPOXvoZUxuxAqMgB3oozmS9Cmy8BOQENmc4ben3JKvJaxDRCCet1KH0PeD2L5LvGt75t0zbiju5ZPr7gRHP0yYGqwUZfW4WJBVXySp6KEax429b7lvI7Kl91BJK2CILhbYASDBhyBGpKKt21aiRd1yMsOw3oAjoCTL4gykljxr99GV12cNuB5XhZSnSFqa-DfulX7hp8fqszv4qKw854M5Jq8xHgpay4tobRsPuTk2sZGJZ39cFbQSPlQQW1a_TAXjjD7sVo7ncXfNODhTllFITq6nR1CJIRUOGOylknfRn2i8bty1-pp2uygbVSPaMRblAegDMp4EdJm61DhpAQ2yjQG1KlpTxbOlOMzhqr7h6lXHdJAELAyNEsxPNb6BKRWq8TntDlMXWHu__6QKbFKs1hnKWvcNSWJwHq3vzrm2I4h7_fEkU0zbgxotFUFhuA2-VHubd8E-zDbcB-laMhdFMxwPYcvfeSPE8lfBpYwFpdtNs91AaeB8j4V-UOiuTUSlYIiYS93y6dgstOSZjWz_jtLv2mcvhglC8VbVIX02ErQ-9pGPJAgeUEkDo6EtNXlbGBi_2JBK9po8C-_I0665oVZ-B7HR3DmoqlBM3dy8vbBFfob41mnPadNpeO2guTbygrbLkcdSA3JjQKdXhrm7EtA-UAKYQWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روتین حرکتی منظم می‌تونه به حمایت از سلامت تیروئید، بهبود عملکرد گوارش و کاهش بعضی علائم مرتبط با PMS کمک کنه  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/687314" target="_blank">📅 08:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687313">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f38265c8.mp4?token=EwAsZ9ny5djtASbzM2kC4aoN1vhGrhiiSZBzjAPg4zY7JdEFA4-Irg3NF8ejejv2nlrgLWRsa5fpoNXuIjiw4hgz7knBE_ecATAW_Y96gcSzI-KJOxpSx0GY5j2eMPWfRJb7BIZlEWHjGsxetDfmINyn-7S7EyIZep_w4UhjAuYqlTEe8JyA9nAV4irTLoesAoTJmpEnyz46xK-1W4djIDPSKyhSAjnoPe2Deux9ERy5BSngMKwk8uFljv0DP2586RtiYfvXR8H-4wB5KfoIhaw--1BM7J0lKL4ntE88yWqdmCDiJbTTGZJiEwT9RPspiOEul8tGwVZZyzLx1BN1Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f38265c8.mp4?token=EwAsZ9ny5djtASbzM2kC4aoN1vhGrhiiSZBzjAPg4zY7JdEFA4-Irg3NF8ejejv2nlrgLWRsa5fpoNXuIjiw4hgz7knBE_ecATAW_Y96gcSzI-KJOxpSx0GY5j2eMPWfRJb7BIZlEWHjGsxetDfmINyn-7S7EyIZep_w4UhjAuYqlTEe8JyA9nAV4irTLoesAoTJmpEnyz46xK-1W4djIDPSKyhSAjnoPe2Deux9ERy5BSngMKwk8uFljv0DP2586RtiYfvXR8H-4wB5KfoIhaw--1BM7J0lKL4ntE88yWqdmCDiJbTTGZJiEwT9RPspiOEul8tGwVZZyzLx1BN1Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رانش زمین، رودخانه‌ای در نپال را مسدود کرد
🔹
رانش زمین در غرب نپال، بخشی از رودخانه چاولانی را مسدود کرده و خطر وقوع سیلاب ناگهانی در مناطق پایین‌دست را افزایش داده است. مقام‌های محلی از ساکنان خواسته‌اند در آماده‌باش باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/687313" target="_blank">📅 08:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687312">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر خارجه عمان: با وجود تهدید همیشگی جنگ، ما از میز مذاکره عقب‌نشینی نخواهیم کرد
🔹
جوی پایدار در بیشتر مناطق کشور طی ۵ روز آینده؛ رگبار و وزش باد شدید در برخی ارتفاعات.
🔹
افزایش شمار قربانیان سیل در نپال به ۱۳۴۲ نفر رسید ۴۸۹۶ نفر همچنان مفقود هستند‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/687312" target="_blank">📅 08:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687311">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ab3d214a.mp4?token=OCK7dTQ5_uk9Hdhny4nPCnNmiOIq3oYb2gB6SmOe4uMP_256oUPoAOoZMXHmXRSfu72mn-QojBcfBsMo_4__ehQHrw7cIDGg-V9uZz_gs_GpJxnvEkuYewE22rfcAVrVAalUC48d9jhJBk2_i5x8UwCF8HgJQXmtcI-qZDbgundi3D1bbLdF5e_zB6oqGQDPUIwjkxQuIApq5W4o7tMK63iA2Y38IjmEDRsdSEW59rDr2k_2bzKtY0-yXwrLUFBF0aKVOC27TvFEzuRJCNfZ0e5ahPFuHUl-aE0o4VhfDi1bPJY2cpu5H6PWXM5ebD8acFcFhhT1E_zS-4BFGzCIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ab3d214a.mp4?token=OCK7dTQ5_uk9Hdhny4nPCnNmiOIq3oYb2gB6SmOe4uMP_256oUPoAOoZMXHmXRSfu72mn-QojBcfBsMo_4__ehQHrw7cIDGg-V9uZz_gs_GpJxnvEkuYewE22rfcAVrVAalUC48d9jhJBk2_i5x8UwCF8HgJQXmtcI-qZDbgundi3D1bbLdF5e_zB6oqGQDPUIwjkxQuIApq5W4o7tMK63iA2Y38IjmEDRsdSEW59rDr2k_2bzKtY0-yXwrLUFBF0aKVOC27TvFEzuRJCNfZ0e5ahPFuHUl-aE0o4VhfDi1bPJY2cpu5H6PWXM5ebD8acFcFhhT1E_zS-4BFGzCIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از نزدیک‌ترین‌هایت شکایت نکن؛ هیچ اختلاف مالی ارزش از دست دادن خانواده را ندارد
🔹
یک وکیل روایت می‌کند که با جلوگیری از جلب برادرِ موکلش، فرصتی برای حل اختلاف مالی داد؛ چند ماه بعد، برادر فوت کرد و موکل هنگام خاکسپاری به اهمیت آن تصمیم پی برد.
🔹
توصیه او: تا جای ممکن مقابل پدر، مادر، خواهر و برادرتان نایستید؛ بعضی فرصت‌ها برای جبران دوباره برنمی‌گردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/687311" target="_blank">📅 08:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687310">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84dd2e621d.mp4?token=Am1EMsP5oz2DTL0gF_GxGUGvdYH-R20Tpxt40V59-7f4rFPB69Z3MQJa4ddM1hC1A7MaDFVDVea6UlcCwTJnS71MPBIGz8JgRDoFW4E5N7wRpfnEtOn-VZ_UaxR58elIf1Rs29dIIRGxuArLnHVWaxKyz77KAX6X0crx9wwHe7CdiiCT_fa84X9S5dEnT98yaO3RmJCG6N60SZ9TKX7ck6x9vIxrKV_Zk2wtk-fzUWvDCnlZ9Uih1MYibGL4nxJjvM_mvOEEL2XFQCx5-ycZayfFdlgHa9QPBEF1-Dkr62fbCyRsSO2tDB4c95CbYqp5edID3GrUr-VLsenQErMX-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84dd2e621d.mp4?token=Am1EMsP5oz2DTL0gF_GxGUGvdYH-R20Tpxt40V59-7f4rFPB69Z3MQJa4ddM1hC1A7MaDFVDVea6UlcCwTJnS71MPBIGz8JgRDoFW4E5N7wRpfnEtOn-VZ_UaxR58elIf1Rs29dIIRGxuArLnHVWaxKyz77KAX6X0crx9wwHe7CdiiCT_fa84X9S5dEnT98yaO3RmJCG6N60SZ9TKX7ck6x9vIxrKV_Zk2wtk-fzUWvDCnlZ9Uih1MYibGL4nxJjvM_mvOEEL2XFQCx5-ycZayfFdlgHa9QPBEF1-Dkr62fbCyRsSO2tDB4c95CbYqp5edID3GrUr-VLsenQErMX-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی سیل‌های ناشی از طوفان به جنوب چین، خانه‌ها زیر باران‌های سیل‌آسا تخریب می شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/687310" target="_blank">📅 07:57 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

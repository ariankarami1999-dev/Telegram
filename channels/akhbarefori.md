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
<img src="https://cdn4.telesco.pe/file/XsC6sW3Ug4EOkokJQpk_lMnxVg9_YQ0I4pzD-VZsv1pRr7dvE1TahgD4Brr_EZbxf47ZbsGbKd6K3AgHnImN6wUt4VZ8nGqlOmHEzKTUptt3oEB0AKU-HeL5Y3YLeB2LZFRCGsSul7ZKgIuELS1FMsDvFADoh8vOcBlxewx5omDIpF3zoCBX5L24X2lIlHRzrauF6-Oy_y-TaId4HRaV0aZ_BhaWIQFaZfbWE-ppm8oatz-G-iUXwNWAN2EOByoXic-e4iwxL3e4J-yaM24SeLM9YrsMiMBJ1oDPCdQG5FNx56XGii6V83gZKJ4CIEfKrnDOWIzqkTakku2YyHnuVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.29M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 17:24:51</div>
<hr>

<div class="tg-post" id="msg-672608">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3h6IPYG-aPdM-F_-x7Unp8Yrtm4SSFTJtww0I9aG_PW-rvIcK_64phd1wVoSNwzo3jDzZCBBK0lhgz9Evw4bQ6eQl_vd6vwIOYTSesDffVm4ReHCAr0snozqG_6E_Nu-yFs0mzMW6JY6DdSyBpunvxjmZSdYazq6TrTP8WyMY-x30zgQ_NKw3bcsEDOJkD2AJDGMMp4B70pLfsHjg3gwTH23FAmaEYvnp2uqKAAmwaq6Ju2R2mi0yjQJfndrb9dCCP59nG9cS3eZxG6UttXLPnoQpU8rgPHLGa9iYpqYibSkAm46nrZxXKjLXfChYz9y5u9BElXbBedXcpiPNKcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع انفجار مهیب در جنوب لبنان توسط رژیم صهیونیستی
🔹
گزارش‌های میدانی از وقوع یک انفجار بسیار بزرگ در شهرک زوطر شرقی در جنوب لبنان خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/672608" target="_blank">📅 17:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672607">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
پس از ناکامی سیستم پدافند هوایی پاتریوت آمریکایی در برابر موشک‌های ایرانی، کویت ممنوعیت تصویربرداری را اعلام کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/672607" target="_blank">📅 17:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672606">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
۱۳ نظامی آمریکایی در حملات ایران مجروح شده‌اند
شبکه خبری فاکس‌نیوز:
🔹
از آغاز حملات ایران به پایگاه‌های آمریکا در کویت، بحرین و اردن،‌ دست‌کم ۱۳ نظامی آمریکایی مجروح شده‌اند.
🔹
طی روزهای اخیر دست‌کم سه پرواز برای انتقال مجروحان آمریکایی از منطقه انجام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/672606" target="_blank">📅 17:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672605">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfGp99tXwiWqUdLMtHI_A3ZI_88oC_HN-4dWyjci-8VauLVYzTFh1kj76gMhUdnRF1JGX-iCQ0lhi9DybXIbylWdFY1ydmetNOjPjhlnueVKF17YSslEKFGyEVnbnhsw6Ka4eB1qZq46wTGJcnTmlYWfiu6UTvxldkE-LlO1ps_s-gJFBb9VnbKwf8AHY7ty5ua0ZAVmEdRVhnJebHvZATu-BPk4kn45Q0NtpJYkLttXZD7MgD9HmNMKgi6MCWgXq8EGdEgnITsHDNOxTunXr3NUhO08em59QcWr_PHbegXlHjbCgoYKcTTc8yY5zPtJoCwmlXfQKF-b7mjfKCy-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اسنپ‌بیمه قسطی هم بخری، تخفیف داری!
💰
برای خرید بیمۀ بدنه یا شخص ثالث تا ۲ میلیون تومان تخفیف بگیر و هزینه‌اش رو قسطی و بدون سود پرداخت کن.
✅
کد تخفیف: GT3F
برای استعلام و خرید به‌صرفه بیمه، اسنپ‌بیمه ۲۴ساعته کنارته
💙
برای خرید بیمه وارد لینک زیر شو:
👇
👇
https://l.snpy.ir/z0kq4
https://l.snpy.ir/z0kq4</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/672605" target="_blank">📅 17:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672604">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
در صورت حمله آمریکا به زیرساخت‌های ایران، فرودگاه‌ها و بنادر امارات باید فوراً تخلیه شوند
یک مقام نظامی:
🔹
اگر امشب آمریکا به زیرساخت‌های غیرنظامی کشور حمله کند برای حفظ جان شهروندان از حملات متقابل ایران، فرودگاه‌های دبی و ابوظبی و همچنین بنادر فجیره و جبل‌علی باید فوراً تخلیه شوند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/672604" target="_blank">📅 17:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672603">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SP9MsK7hFNC2qeY7tHdpx27IX_1_f4Zrrpv0RFV5uIVd7eW2MqjA99mT27PhmQtrLXowqqe3NunCgw8eSlhZ_RFYb9Ti1IxnVYoyd5zyvKHInHOZYyCVkASSeuSte7ZP6UHa-KcVF8eyZQU_7zNB_4JJALZnHLqZH2jngx_8NmHb_w0PaZA7RXQ5QNEZXJJGKDiuAHBU-Tqau2pFA7EkdgkWhOvNFPtjWXrZUEi4mX8g6p6XwcyOdKOLj26Mhq7kgpkyXNJnPMBjR-u_1h46dey4pztRY9JltYIPpQtRUossUsgacL3pN2jPFM1mAupkfVOneo7deiNKsnTIiWHkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروگاه شعیبه کویت منفجر شد
🔹
این نیروگاه با ظرفیت تولید ۸۷۶ مگاوات برق و ۴۵ میلیون گالن آب شیرین در روز به عنوان یکی از شش نیروگاه اصلی دولتی کویت، نقش حیاتی در تأمین برق و آب شرب این کشور ایفا می‌کند و از نوع تولید همزمان برق و آب محسوب می‌شود.
🔹
نیروگاه شعیبه بامداد امروز هدف قرار گرفت و به طور کامل منهدم شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/672603" target="_blank">📅 16:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672602">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
آکادمی امنیت کویت در پی حملات گزارش‌شده موشکی و پهپادی ایران در آتش می‌سوزد
🔹
این مرکز خسارت‌های گسترده‌ای متحمل شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/672602" target="_blank">📅 16:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672601">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-BgzSFVIPbxQ90qb4Z_CuaTapXfdapih4_onndx7l01UmLF55nXMYWl_eoGcaSHBeAt1IgJMP6OV9gc2K42d1U4eFRPpGrSIJppBuA3cUZcCmmECEU5rOL3NHnRrrcewdG78jD-V8rD6UOkJX7FHJh08yx2ax9a23XxhlpYwU78lheoFX6-tAGo96TtQJbRj0AvTuqHwNDMu5gUYP9cnpgm_1tAIp1jJQEso-z5hVIMjjfJxI4_CGwHzKuksRaz0OscBsigIGHmLULA4nnd9GadKU2RdQXVnjK4dUxiRVbgTu5uuS-XxbTJHcn7eG5soJNY0eyqz89XLEx2yAljMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه DD Geopolitics: جمهوری اسلامی امروز به طور کامل پادشاهی گوجه‌فرنگی را در هم می‌کوبد
🔹
ضربه‌های مستقیم به مجموعه‌ای از دارایی‌های آمریکایی در اردن.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/672601" target="_blank">📅 16:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672600">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3655956b73.mp4?token=KLr13sYUUh01FjrDvesNvewHbuz4nte-5rKxyyNBe6U4X8_xr0QyK9ivsSWTOcOEvlqJEqk4n1IqSvr3Qbis14gzrMgnBzMUwEM2MmGaowoPQ96ufMKOlH4aB1spDGFENYw_wrvK6eowP_RG4aUdlth1IqLb174X1_WnlyGiVAWHNuwDjfbDnJxYHqtyZmf4kQKrp6d8f8L4G4C4zpmAFtMsPB0tBnZFdsA6KJMxlDjloSs_RbfUmQ7fZxI4eNpVH1QUNqRI_XFdyVpsJIzj5f-xnfiOjoaJFZSohrsmXFkffkDb6LorfTQ8smOin8HEZsVAOSmQ1_5_u91K7Bba3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3655956b73.mp4?token=KLr13sYUUh01FjrDvesNvewHbuz4nte-5rKxyyNBe6U4X8_xr0QyK9ivsSWTOcOEvlqJEqk4n1IqSvr3Qbis14gzrMgnBzMUwEM2MmGaowoPQ96ufMKOlH4aB1spDGFENYw_wrvK6eowP_RG4aUdlth1IqLb174X1_WnlyGiVAWHNuwDjfbDnJxYHqtyZmf4kQKrp6d8f8L4G4C4zpmAFtMsPB0tBnZFdsA6KJMxlDjloSs_RbfUmQ7fZxI4eNpVH1QUNqRI_XFdyVpsJIzj5f-xnfiOjoaJFZSohrsmXFkffkDb6LorfTQ8smOin8HEZsVAOSmQ1_5_u91K7Bba3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار جمعی مسافران از فرودگاه کویت؛ ازدحام بی‌سابقه در پی حملات کوبنده ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/672600" target="_blank">📅 16:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672599">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hurRiBH9hV2VjBIZvSCzFjEQ2QatdZ0Vvv_vdnVmxd3RQ7bZM1skC3GFS24jn5Vq_tRId6ZccRRjz8ttLY5r3-XAgynz420HSCkUzAB7NsdpDlLhjthEywD1Yewur_CDmI7Ij6qgJ2ugXrK98ROwzXdv0CGFBIaE9tA7N9CAA-QoM41ZA-BoxCe3tx3R_1695ZTT7eI700d6aIqvUIiboq0B3GAwLgZV8qJPUoHxmfRc9hy8-IeemCekhKzx5WCX7BQwu7QfJBP7KmZi0yW9SYCojWmi8XGgtxx3g8xRYo0reIbcqoEgpq4e0mLfRiY1VWjhpXhujrxPshmH3oskJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیسان قشقایی؛ همراه همیشگی سفر
خرید با شرایط متنوع:
▪️
نقدی دو‌مرحله‌ای
▪️
اقساط ۶ ماهه بدون بهره
▪️
اقساط ۳۶ و ۶۰ ماهه با نرخ ۲۳٪
▪️
تحویل ۳۰ روز کاری
مشاهده بخشنامه و ثبت درخواست خرید:
🔗
https://arinadrive.com/qashqai_landing/
آرینا درایو؛ همیشه رو به راه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/672599" target="_blank">📅 16:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672598">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
آسیب سخت به نظامیان آمریکایی در پی حملات ایران به اردن
شبکه ۱۲ اسرائیل:
🔹
ایران طی هفته جاری به دست‌کم دو پایگاه در اردن حمله کرده است که در پی هدف قرار گرفتن این تأسیسات، تعدادی از نظامیان آمریکایی زخمی شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/672598" target="_blank">📅 16:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672597">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس دادگستری هرمزگان: مردم هیچ نگرانی بابت ارسال کالاها و خدمات بندری نداشته باشند.
🔹
نشت گاز در محدوده بیمارستان دی بدون حادثه مهار شد
🔹
ستون دود در منطقه گیلاوند دماوند ناشی از آتش‌سوزی است
🔹
شهرک‌نشینان صهیونیستی: در صورت بازگشت دوباره نتانیاهو به قدرت، مهاجرت می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/672597" target="_blank">📅 16:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672596">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwuQnvUwZH_IIm0zRoQV98ROyT1_6-q0uMgA05z6QquqPXOXPHMQCmEQhjoHyU-L36pwp42dj3o7YTMq9heiGTEJuckJp1aaFqw4cgxaAM0wR1iaSuHAfmhcb-yyT1YT7av-Xf_hQL_YawIzh6fHM63VRdzPEw6XOWrWXx4VOH08UDjjJBDF_N81ZNyAlA2ReI7VkKdnuowODl7n9AClkFB8gDp5sOc8Rw10V3ci1g06zcocQF3eZYf_EO-en2nJhl7yxTVvxPxD7ENiSLEODEHaMccy_GhXBkM8EcHKM8aYxDeesTy3yRdwc0NfB7zEj8gVRsVzGrB9c_Hhp6f6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
العربیه: بار دیگر، آژیرهای خطر در بحرین به صدا درآمدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/672596" target="_blank">📅 16:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672595">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To7Y7gN4-T_Rjyqbo_KVNR8QhJ1oRAMzTSgmwsFlfyci4SAH0Rys3VLumDlwgjHVz4kkbo4LbV93TG-KD1TlYR1n3bH6YlmD8DmQAoPYwQjot5lJj5VKFJGj4gh5ZSflqCyZ7xi107DQYr00VIkGswE45PWMip1xHFnv0kZfE-XqqVfV3aeEFTU-XBWIl_zIPOUCwDbUIZYKmKSHV5UgsEgv8CpMNXeLxpj1HrUOJOZZniv8Db39m2APH4sslyupKj6dKZrilsmIVerh19kHMD2NrAgF_SBbDuwFQ8M1kCsBji7IpQqfXl0na0Pl_bK3ZKJ8dmVvs_mZlXe0LgULJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به تروریست‌ها در سلیمانیه عراق
🔹
به گزارش منابع خبری، در این حملات، مقرهای تروریست‌های تجزیه‌طلب ضد ایرانی هدف قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/672595" target="_blank">📅 16:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672594">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c37398e3f.mp4?token=lwcj-Be_jkKL33I0OTKH-aUo_c8FX-FgjPpmjZ-4hdoDWWzbEG7ND3WcW-0P0RXnE4wfaXBW6ADvx8LXy6QM_bq188neqs2yICF9JyXpVi6DPZ6fLEGDtsHscX5C6pMlYWs7BMPOxcByv3vU_QLj7fpffb66C-hMOE1Y1s6SxTFISjfHKe1pZS4r4weDxBcFSo75TO7th_IxzOXdyNfwOSDOIxHK8ZtngNtuXQZ7xOoLCRw1BDZ6B7KsxDgaKB54atYIAUFxApJD8p4Kz9nBizaJcd14-YCbBbNl8ZJiIG-HrLBAa63xUsJFr7b8nxlvq4xeGdOyw0msu9OYW46MjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c37398e3f.mp4?token=lwcj-Be_jkKL33I0OTKH-aUo_c8FX-FgjPpmjZ-4hdoDWWzbEG7ND3WcW-0P0RXnE4wfaXBW6ADvx8LXy6QM_bq188neqs2yICF9JyXpVi6DPZ6fLEGDtsHscX5C6pMlYWs7BMPOxcByv3vU_QLj7fpffb66C-hMOE1Y1s6SxTFISjfHKe1pZS4r4weDxBcFSo75TO7th_IxzOXdyNfwOSDOIxHK8ZtngNtuXQZ7xOoLCRw1BDZ6B7KsxDgaKB54atYIAUFxApJD8p4Kz9nBizaJcd14-YCbBbNl8ZJiIG-HrLBAa63xUsJFr7b8nxlvq4xeGdOyw0msu9OYW46MjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ضربات جدی ایران به پایگاه آمریکا در کویت
🔹
شدت آتش‌سوزی به حدی است که دود حاصل از آن از فاصله دور قابل مشاهده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/672594" target="_blank">📅 16:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672593">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOff3LgKtqXsNDhkKP9CiwsFzVKw5mF8Q74Xc_n-mMg3q_n63nlsZId_YZoDh_mHGMITvbvX15FbwY3toGfe-BakCN4timN83ptAsa22N6o-PjqpepAmQ8S_938foI5blHj_LY707UojhRb9yvBrO2JSvOpSVtLHyEBddRS8S9wMbHbjy306hyaPIctpf91vA5EdBAYi9_K-kG0Vx-ZuIHAQio926shhQ_hGot-OazescyN0aqdpJOlIEA0BwbIPEw_BAts7r7D1PP3asgpYGJD1XWm-HDlCnwqda5KzGQFwAzvHXCwR7Z2rwezP2sCo6YMbS7r-30PoxHhHmfo79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل‌گر اسرائیلی: هیچ نیروی نظامی در تاریخ با چنین سطحی از دقت و اثربخشی به نیروهای آمریکایی ضربه نزده است
آلوهن میرزاحی:
🔹
آمریکایی‌ها حتی نمی‌دانند رویارویی با یک ارتش واقعی یعنی چه و آنها در حال نابودی هستند
🔹
ایران مانند یک ابرقدرت مدرن می‌جنگد، اما با روحیه یک نیروی نظامی مقدس و بومی اسلامی. چه صحنه دیوانه‌کننده‌ای.
🔹
ما شاهد بزرگ‌ترین و حماسی‌ترین نبرد از زمان شکست نازی‌ها توسط ارتش سرخ در جنگ جهانی دوم هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/672593" target="_blank">📅 16:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672592">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
♦️
منابع عربی از حمله به پایگاه هوایی شیخ عیسی در بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/672592" target="_blank">📅 16:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672591">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49795aeed3.mp4?token=cer86MjNba6wljQldpQFaLLuXPNl2ZsvWIYw7e2dNy82rhmgizSLUM1w6oUykVxBFu2YfDdlDwK5z_qu4xt-aW2pgJ5e8KESeIhQfgql1O1huBCsW5ZmleWi7NtMUC0NOOH3JpVqzKhNRovWJ_j0exRtQ3dyM0-sfyektqpuvQQwkgC9nSPDmF589xexZ0AAn0yOMg0vJbYFngCuZ-rjoxkmmDHGlz42kJS-rfmQVHjhIB6M4OkbtaWCDwJzwl1YW0dl5F2S-hVf6EpS_3rILlFcrJ0u5LrtIdJN6Ibv0-mFX7xXufJ8bNtX6oyK7vbE_M3wsiTtvouNDyjj7mFWuLlKrEPeZ4eCN0AKR3ZAR5JFgtfdfwIwNYPJuPAK8if_xRW50OLf8eriMu556-ymgtvCUERyoDRV9ZN8gqc_U445Pi9ncXTWU47QuRz5VwzmZRp2CGuOdz0NuYtIKv_c72KaKucTNqrfrji1zMiZBbTI01UPajxmQm4hGUEz_r_4sm9lM-AgJPliCn67YzQb4t2dNq9r-6Rax9y4G1ZXVr0leWEs1N_umxhL3U45PxezqUNz8GMmbAZgnylkDtoQm4FsC-ebNbt_dtX-_5vueQkK_yr_aQs81_XTutOXyh6OVbh-wkxbvBZak0Ej21vuF9zW2OohQp28dCPy9wreX7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49795aeed3.mp4?token=cer86MjNba6wljQldpQFaLLuXPNl2ZsvWIYw7e2dNy82rhmgizSLUM1w6oUykVxBFu2YfDdlDwK5z_qu4xt-aW2pgJ5e8KESeIhQfgql1O1huBCsW5ZmleWi7NtMUC0NOOH3JpVqzKhNRovWJ_j0exRtQ3dyM0-sfyektqpuvQQwkgC9nSPDmF589xexZ0AAn0yOMg0vJbYFngCuZ-rjoxkmmDHGlz42kJS-rfmQVHjhIB6M4OkbtaWCDwJzwl1YW0dl5F2S-hVf6EpS_3rILlFcrJ0u5LrtIdJN6Ibv0-mFX7xXufJ8bNtX6oyK7vbE_M3wsiTtvouNDyjj7mFWuLlKrEPeZ4eCN0AKR3ZAR5JFgtfdfwIwNYPJuPAK8if_xRW50OLf8eriMu556-ymgtvCUERyoDRV9ZN8gqc_U445Pi9ncXTWU47QuRz5VwzmZRp2CGuOdz0NuYtIKv_c72KaKucTNqrfrji1zMiZBbTI01UPajxmQm4hGUEz_r_4sm9lM-AgJPliCn67YzQb4t2dNq9r-6Rax9y4G1ZXVr0leWEs1N_umxhL3U45PxezqUNz8GMmbAZgnylkDtoQm4FsC-ebNbt_dtX-_5vueQkK_yr_aQs81_XTutOXyh6OVbh-wkxbvBZak0Ej21vuF9zW2OohQp28dCPy9wreX7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه طلایی بخریم که ارزش سرمایه‌گذاری داشته باشد؟  #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/672591" target="_blank">📅 16:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672590">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9rNFWn0FK5RQY7ps5cXsyw-qRGosoTmW4IO2j1beO5fwOVsEFd1Gi_rX9uYYyomn_-fPPTTtYFZMfE65gpk-8IaP7dVbLrdw0yeZ8INKDyF05rbuJ-AArdogqrvyBmIEM4u21K627b8sPsJId7QNlgzXssNeWrRIUGAv4Kxinl6aaeRcumIcv-9EDzv2tgGwHnZKckyPwdEPRYFIPfwuwyJlNwtwDT0DDO5HuODFr7KcLTwEvVDd0PApx3jQo0HFKAxCRL49_jOQRkoexs5LBWH5TYiA6msB_wZmrBEweb-wTl5QygSsBXPiy3ZcZEM1-mreIzqI-4wWGRQZqsP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش اردن: پهپادهای ایران را رهگیری کردیم و اصلا هم دردمون نیومد
🌟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672590" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672589">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4acb113fd.mp4?token=b5zd9x6NLIkF2MqzuygsvF7fQ9y_G1I8gQl-DDPuThfsOxUHuS1FUpFFcTsfA1x8ToM8t3hiP8KySGEuHutUsMBUEr0ESv05PfYFTkvB5qnG_MDGsU1FgzVJWXQdQFA-qIaniKEa81aDBtvv9yeBu6Zl0ko5qrr3NtZqkZR8I1yGNFhpVzLF4cm2yusZefMnWk0M_phN28KlGwLMmtUKdz0F5nxUvQgJpP2nSiN71FuIIPbez4rHYLwv7nXU_sODA_KC_27-L-EfLsP9VE8ZYqUHAUkkOoQqiymoHPBiWa81ZoPnNB97vA7kM_qOWbSm6GjLPTAkL6n9haDJlZGl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4acb113fd.mp4?token=b5zd9x6NLIkF2MqzuygsvF7fQ9y_G1I8gQl-DDPuThfsOxUHuS1FUpFFcTsfA1x8ToM8t3hiP8KySGEuHutUsMBUEr0ESv05PfYFTkvB5qnG_MDGsU1FgzVJWXQdQFA-qIaniKEa81aDBtvv9yeBu6Zl0ko5qrr3NtZqkZR8I1yGNFhpVzLF4cm2yusZefMnWk0M_phN28KlGwLMmtUKdz0F5nxUvQgJpP2nSiN71FuIIPbez4rHYLwv7nXU_sODA_KC_27-L-EfLsP9VE8ZYqUHAUkkOoQqiymoHPBiWa81ZoPnNB97vA7kM_qOWbSm6GjLPTAkL6n9haDJlZGl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت مستقیم موشک‌های ایران به پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672589" target="_blank">📅 15:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672588">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIMSGOF1v10VKmw1xeYFSkbJa0KvYS-jZdPP3LePw0z3-dvLfm-T1N9NL84wX3nsAGbJc8-wn2P0-CSWR8aU4qE4ruN3RhxAVdYaDu1EaunT3ljR5jdhLpKkWVeC9hm_XH2cbIl59eqp8bs_NOYjOLIosMN-cqhVncPB8Zg7HO-W9nwFYK6APbcEYJaqbwKbsUjrY208pcfpZZ6g2adSRX6OTYUon0F5ccHrxMkbcla5XScOiQCkS9jXS3X-0lIEUWVtwK7ueYLa6vyy5A32VSVRIv2Qfq6W-xc9L_-DZnxV3e1rpiBr9WJTpQxXSGMGC9ScBlBqZvuYR6Ai_G-8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل هیوم: خوک هار تمایلی به دیدار با نتانیاهو ندارد
🔹
اختلافات جدیدی میان واشنگتن و تل‌آویو درباره نحوه برخورد با ایران پدید آمده و روابط دو طرف وارد مرحله‌ای از تنش شده است. این مسئله همچنین به کاهش سطح هماهنگی سیاسی میان دو طرف منجر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/672588" target="_blank">📅 15:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672587">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
۱۱۶ دکل مخابراتی هرمزگان در حملات آمریکا از مدار خارج شد/تلفن ثابت، همراه و اینترنت ‌با قطعی مواجه است‌   مدیرکل ارتباطات و فناوری اطلاعات هرمزگان:
🔹
بر اثر حمله شب گذشته آمریکا، ۱۱۶ دکل مخابراتی در شمال بندرعباس و حاجی‌آباد از مدار خارج و تلفن و اینترنت…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/672587" target="_blank">📅 15:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672586">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
دانیا ظفر: تهران در حال ایجاد سطح بالایی از ترس در میان کشورهای خلیج فارس است
تحلیل‌گر عرب:
🔹
درگیری‌ها میان ایران و آمریکا از الگوی «چشم در برابر چشم» پیروی می‌کند؛ به‌ گونه‌ای که حمله به زیرساخت‌ها نشان‌دهنده تشدید تنش است، اما هنوز به معنای بازگشت به «جنگ تمام عیار» نیست
🔹
در اهمیت حمله به آب‌شیرین کویت، همین بس که این کشور بیش از ۹۰ درصد به آب شیرین‌ شده وابسته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/672586" target="_blank">📅 15:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672585">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
غریب‌آبادی: تعهداتمان در تفاهمنامه اسلام‌آباد را متوقف کرده‌ایم
معاون امور حقوقی و بین‌المللی وزارت امور خارجه:
🔹
آمریکا تمام تعهداتش در چارچوب یادداشت تفاهم اسلام‌آباد را زیر پا گذاشته و همه را متوقف کرده است،  ما نیز تعهدات خود را متوقف کرده‌ایم و در حال اجرای آنها نیستیم و مشغول دفاع از کشوریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/672585" target="_blank">📅 15:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672584">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
صدای آژیر خطر بار دیگر در کویت و بحرین به صدا درآمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/672584" target="_blank">📅 15:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672583">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
العربیه: بار دیگر، آژیرهای خطر در بحرین به صدا درآمدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/672583" target="_blank">📅 15:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672582">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عراق به سوریه هشدار داد: از پرونده لبنان دوری کنید
🔹
یک رسانه لبنانی فاش کرد که دولت عراق در روزهای اخیر پیامی هشدارآمیز به رئیس دولت موقت سوریه ارسال کرده و از او خواسته است از هرگونه ورود به پرونده لبنان و همراهی با فشارهای آمریکا و عربستان علیه حزب‌الله خودداری کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/672582" target="_blank">📅 15:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672580">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9ILfuPW-A0-ks9eo-UMcwfwKbTgaSKC5371eal0yHvZFb95SttmzBp08qFzXpVxKHYxfdKTeaKBxb2w5q4Fr4HTr8czXoMUPVySiLZDhf5FoUxkZ7HiEOsurNvLCVHDpyXLiMY5teYfdHkvEFwvFIV_7TsDDr1mgzl3v59V4zRzLGUxHpQb0-Az8UdBD5qrm6UmjHKPs4w4aUusSRpJjjaL-VCRnv3BI1RsrXogrU5p7Ofr30QfDM68wDzwguZ7bEabJm1e-J3uDQ-g9p22zVpmtjv5zBta3-_k8fVPyQPWObVOgvgLxAkWz-YgUOq0s8P8Tgfq94cMU2zL6r9jOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممدانی: جای نتانیاهو در دادگاه لاهه است
🔹
شهردار نیویورک، زهران ممدانی در مصاحبه‌ای با روزنامه نیویورک‌تایمز گفت که درباره این موضوع که آیا اختیار قانونی برای بازداشت نخست‌وزیر اسرائیل را دارد یا نه، در حال «رایزنی و گفت‌وگویی فعال» با اداره حقوقی شهر نیویورک است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/672580" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672579">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5afb3ddfbf.mp4?token=XXyWZw5zL1OQJ5UqT3aYrF2rJKCG2xkLpvzGKcWlZBEBlCHLOR5EG6d0T3_YaNUY9WiFoJ5CdqQ4ri0GLxJF8Z_bjF4jcjdQa3oo0qaP1HXoO-S8f7MI2PY7HCxU-jCif2eGXlznCoZ0qgm1DIV1Hr3I24r99j5WJhF6Q9SfagNuqqZ0ImvmdeQSDtp9FmWI4KU8nB1WQeA7f7OuOV_EuY8DqWX0ppb_j0CJYgvnJGGVeCRxddpHbTGDt1HHTMY3FS-n5RLMdIjL68SVmOYFgOdgMqKyjK8YZFzXGfQOIiGu2IKu0PX6xRK0IcnIoFw-vMP51xfDdRUSwz1fJF4COg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5afb3ddfbf.mp4?token=XXyWZw5zL1OQJ5UqT3aYrF2rJKCG2xkLpvzGKcWlZBEBlCHLOR5EG6d0T3_YaNUY9WiFoJ5CdqQ4ri0GLxJF8Z_bjF4jcjdQa3oo0qaP1HXoO-S8f7MI2PY7HCxU-jCif2eGXlznCoZ0qgm1DIV1Hr3I24r99j5WJhF6Q9SfagNuqqZ0ImvmdeQSDtp9FmWI4KU8nB1WQeA7f7OuOV_EuY8DqWX0ppb_j0CJYgvnJGGVeCRxddpHbTGDt1HHTMY3FS-n5RLMdIjL68SVmOYFgOdgMqKyjK8YZFzXGfQOIiGu2IKu0PX6xRK0IcnIoFw-vMP51xfDdRUSwz1fJF4COg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار هرمزگان: با وجود تهاجم به آب‌شیرین‌کن‌ها در ۲۰ روستای شهرستان جاسک، اختلالی در روند آب‌رسانی به مردم وجود ندارد
🔹
در روزهای آینده آب‌شیرین‌کن‌ها وارد مدار می‌شوند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/672579" target="_blank">📅 15:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672578">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02387c752.mp4?token=GYaY4StNP-Mfn_nk-mxeRup7TzrOenShcPJEaGoizE2LpzLZSnriJZhgJK0JydYqctmjSaoeBjaHcdHvRheCofac1nHhhiQVQsHxqxkq3BYRzNqmB9NH5d5PokJ5KHK9pJm-nXZm9jmp3lTLfVpUaLnEqVxa7hUUKLAOQrDZCCtB6p4ZTBmfDCjKHvTU_fTZklPP8GhMRuRxmL5cIMJB7EoEYeikZk-ZM55zp997xdM2Fpx-Rbt9x3vItsqHgDRNNKdsbcszufX8Cg4oBBBQmr2dtIdgKWhhA1ZCu2q4Y8ZSIRtuS6z4ukP0mhdcL7ADvKPln9ZFnvlDqPj45ykNfJDEqpv0xMGi353hxOH7aSh5hlaOnXMAniJ_xQaJnhDiC4Hgum-nH3OyWfNGOsCCPsdUPzXqnbXhYX3uarzXyx-ao7APf-asZrLTaRdufi2aWu9oBpRWhA68hgYcaTYhAaLqpfFp7_17R8VWz-Mt-RIXeM1gnO6ukAl_2HHG1of_V40RYgjoGNBBepOqe4WSAYF97QqJLHQeJOcvTx6nA4eJDj08bfGzjchXdYrXtLh-ueedrEJ6KxG2aPd6cqep9VF58kGnGFrJskh1A3WBvznzYXP_ReB2KrpefJaKqWaY5O0M3cvehRzTsWEaDYZ4FzsGO9MPyRCCUPVthuRfnjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02387c752.mp4?token=GYaY4StNP-Mfn_nk-mxeRup7TzrOenShcPJEaGoizE2LpzLZSnriJZhgJK0JydYqctmjSaoeBjaHcdHvRheCofac1nHhhiQVQsHxqxkq3BYRzNqmB9NH5d5PokJ5KHK9pJm-nXZm9jmp3lTLfVpUaLnEqVxa7hUUKLAOQrDZCCtB6p4ZTBmfDCjKHvTU_fTZklPP8GhMRuRxmL5cIMJB7EoEYeikZk-ZM55zp997xdM2Fpx-Rbt9x3vItsqHgDRNNKdsbcszufX8Cg4oBBBQmr2dtIdgKWhhA1ZCu2q4Y8ZSIRtuS6z4ukP0mhdcL7ADvKPln9ZFnvlDqPj45ykNfJDEqpv0xMGi353hxOH7aSh5hlaOnXMAniJ_xQaJnhDiC4Hgum-nH3OyWfNGOsCCPsdUPzXqnbXhYX3uarzXyx-ao7APf-asZrLTaRdufi2aWu9oBpRWhA68hgYcaTYhAaLqpfFp7_17R8VWz-Mt-RIXeM1gnO6ukAl_2HHG1of_V40RYgjoGNBBepOqe4WSAYF97QqJLHQeJOcvTx6nA4eJDj08bfGzjchXdYrXtLh-ueedrEJ6KxG2aPd6cqep9VF58kGnGFrJskh1A3WBvznzYXP_ReB2KrpefJaKqWaY5O0M3cvehRzTsWEaDYZ4FzsGO9MPyRCCUPVthuRfnjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای آژیر خطر علاوه بر پایگاه پنجم نیروی دریایی آمریکا در بحرین ۱٠ هزار کیلومتر آنطرف تر در وال استریت نیز شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672578" target="_blank">📅 15:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672577">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPWZPoM6PGjiZIBSR0p6hj74paQsW1y9KapTvjq4pwGNdRIwZLt3hVfm8OqaUEFdH6CvRsk682oeHiXktDtziZo14QDvSP9svCrvM9KK_TDqvA8eYXd8847mkwoUIlJzwfkvPVS5R2_nwfJYNDF6Z97QQ9KQKRkKmTzmTELLc3akOYOnpg6WzqXHugdUTQCiN82j6CsUFTAfktdFBMfD74rmuJ3699-n4xsmmCsRmj_GSc7qkIlfpxA7Wc4rqMVdQfSanXXq5y-fbr3_IBBrEsY1w_ydAh8v3Pb9n3Ch4tkQPVPnNK3N7gIqn58PKGSRbiuzHdkbdA6j7u0J7SS8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صندوق طلای رز ترنج
؛
یک رز و چند نشان
🟢
صندوق طلای رز ترنج امکان سرمایه‌گذاری در طلا را بدون پرداخت
مالیات
و
اجرت
ساخت فراهم می‌کند و دغدغه‌هایی مانند نگهداری، سرقت و تشخیص
اصالت
طلای فیزیکی را نیز کاهش می‌دهد.
🟢
ترکیب
بهینه
گواهی سپرده
شمش
و
سکه
طلا در کنار استفاده از ظرفیت بازار آپشن، به «
رز ترنج
» کمک می‌کند تا از فرصت‌های بازار برای بهبود بازدهی استفاده کند.
🟢
برای خرید با حداقل مبلغ ۱۰۰
هزار تومان
، کافی است از ساعت ۱۱:۴۵ تا ۱۷:۰۰ نماد «
رز ترنج
» را در سامانه معاملاتی تمام کارگزاری‌ها جستجو کنید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/672577" target="_blank">📅 15:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672576">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a571e5b933.mp4?token=tqwi_HhAEpXorGV_WMTQEMXFnGQV9XCpNtkK5RsVjyWGrdLCgC_64VN10lH3RAhqlIGD6ejFiKre6d19nCZVHO5QHhyNQ_7r7nPThcCbxeREY1EP_g4LTTz0lNFNVc5o6fj2G5xqdFWQuTti3uy-FPLYbk1Q16f3d2z_reGJoZgD3e5yvfvLWqD7iig2F7EW4zQt3OeuMdBIX9dt8HNm8kbXK98yW1QtzZB6Tezi2oQx_s01fTkXwqs017XCN30KWSU3Xp5_hLNfG3wRyuO86VjYmvvubFDe2cwIT2WYwUzPwQXDvoZ9VCy-rBQ2d0poS7dzS04UWot_dCz6GVNbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a571e5b933.mp4?token=tqwi_HhAEpXorGV_WMTQEMXFnGQV9XCpNtkK5RsVjyWGrdLCgC_64VN10lH3RAhqlIGD6ejFiKre6d19nCZVHO5QHhyNQ_7r7nPThcCbxeREY1EP_g4LTTz0lNFNVc5o6fj2G5xqdFWQuTti3uy-FPLYbk1Q16f3d2z_reGJoZgD3e5yvfvLWqD7iig2F7EW4zQt3OeuMdBIX9dt8HNm8kbXK98yW1QtzZB6Tezi2oQx_s01fTkXwqs017XCN30KWSU3Xp5_hLNfG3wRyuO86VjYmvvubFDe2cwIT2WYwUzPwQXDvoZ9VCy-rBQ2d0poS7dzS04UWot_dCz6GVNbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان اردن در تسخیر موشک‌ها و پهپادهای ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/672576" target="_blank">📅 14:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672575">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
♦️
وزارت دفاع کویت: یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/672575" target="_blank">📅 14:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672574">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efb89dac2.mp4?token=F7Jnb-HDHKYZ4Dc4-Sef-sWoEral27U9dThcJWScLQRhrN2VJR0UZbiEzt1Zw_-1164Gms7Ij3MQaaapWxx15hUHD2iAkabEpU6w8olTntU0pAgocQPb-A5JxIZwyK6yF-_gxGtEoiVWYch1VJKhEDwb5b2Q7ua7KkQQCdqrAywplNt6vkm9lmcoJMQzRUCJEGyg5DZ_jobX60jLbYAVGkxykegnvYS31rYXFDZ1nvFnNTOGO0Cz1rOJgwFEFisgqEhVHlHIr7RKtisVVVrYzyKjWw5ZygQhRFt6j4Vyaq_-Rfr4QtsNyIWAHMifJfVeuoUKZZ5cPvVp0c9BwC2IKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efb89dac2.mp4?token=F7Jnb-HDHKYZ4Dc4-Sef-sWoEral27U9dThcJWScLQRhrN2VJR0UZbiEzt1Zw_-1164Gms7Ij3MQaaapWxx15hUHD2iAkabEpU6w8olTntU0pAgocQPb-A5JxIZwyK6yF-_gxGtEoiVWYch1VJKhEDwb5b2Q7ua7KkQQCdqrAywplNt6vkm9lmcoJMQzRUCJEGyg5DZ_jobX60jLbYAVGkxykegnvYS31rYXFDZ1nvFnNTOGO0Cz1rOJgwFEFisgqEhVHlHIr7RKtisVVVrYzyKjWw5ZygQhRFt6j4Vyaq_-Rfr4QtsNyIWAHMifJfVeuoUKZZ5cPvVp0c9BwC2IKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان اردن در تسخیر موشک‌ها و پهپادهای ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/672574" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672573">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
وزارت بهداشت
:
در حملات هوایی ۶ تا ۲۷ تیرماه، بیش از ۵۰۰ نفر مصدوم و ۵۰ نفر شهید شدند
🔹
در میان شهدا، ۵ زن و ۲ کودک و نوجوان زیر ۱۸ سال و در میان مصدومان ۳۲ زن و ۱۸ کودک و نوجوان دیده می‌شوند.
🔹
تاکنون ۲۸ عمل جراحی انجام شده، ۴۶۰ نفر ترخیص و ۳۷ نفر همچنان بستری هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/672573" target="_blank">📅 14:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672572">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
۱۱۶ دکل مخابراتی هرمزگان در حملات آمریکا از مدار خارج شد
/
تلفن ثابت، همراه و اینترنت ‌با قطعی مواجه است‌
مدیرکل ارتباطات و فناوری اطلاعات هرمزگان:
🔹
بر اثر حمله شب گذشته آمریکا، ۱۱۶ دکل مخابراتی در شمال بندرعباس و حاجی‌آباد از مدار خارج و تلفن و اینترنت این مناطق قطع شد. عملیات بازسازی و اعزام تیم‌های تعمیراتی آغاز شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/672572" target="_blank">📅 14:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672571">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
فواد حسین، وزیر امور خارجه عراق: عراق نقش میانجی را بین ایالات متحده و ایران ایفا خواهد کرد و من به زودی به تهران سفر خواهم کرد
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/672571" target="_blank">📅 14:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672570">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd951247a.mp4?token=GUINbyAgM4As3mzGtgJCg7z-1b_LQFPDziMZK01Y8UvdH236iaap5UCcHyAdJsXkLWGwCL9L7_y9ujaGoeffGj56aPco92Z09o0h9vjUKaouhPHEOGNwP4x_KPgiURMhLlETTknSRALByhUvM8JwLMZyJBcEKekpfSDW27JnxJybpCvFuqPI8rqSu0AOUS_FE250ePtSHmAMP28yMhj-B5OvF9Rdqp57pnlIFZMbxvhMLgzPxoNrIH30gBqDsTDJyBmCczQj03zLeFYQ1DXfK9I3nkfXyy8wyAplAl-4U2TFsc3M3P_gnThxvH_Qaiq-zP7oNPmGRqykd7zzQIhH1Eu_lEf7iXo2kitZaMM3kssC7q3Zx6zx0vma__U3AgZMWH4Nh0DSoEmCWr4F2mP3f8Yjd2a2fRvkYYSdRjQ4xGGbSwTcLzz_9lcTaCp5v6Pn-9Ync6a1oiXeBodzz8ICqawAQMeeH8htwo1wnxf1AQY6f6zjimLWZtss63w9wpI9GFqptUhwUOamYvFZo2u5XJoHmfXVSUUGvkIo4FzZCN4kG2R4gG2arjiJYblTdbjNQ2MdkECe1oRPibd5SeIrcorNWEYGpLyE87JQFWiEOQS9EPl62grgN6r4gv0DAs0HyOrQnW8wSJLR57tzeC8viToof8JggiOFSrVoumd-FXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd951247a.mp4?token=GUINbyAgM4As3mzGtgJCg7z-1b_LQFPDziMZK01Y8UvdH236iaap5UCcHyAdJsXkLWGwCL9L7_y9ujaGoeffGj56aPco92Z09o0h9vjUKaouhPHEOGNwP4x_KPgiURMhLlETTknSRALByhUvM8JwLMZyJBcEKekpfSDW27JnxJybpCvFuqPI8rqSu0AOUS_FE250ePtSHmAMP28yMhj-B5OvF9Rdqp57pnlIFZMbxvhMLgzPxoNrIH30gBqDsTDJyBmCczQj03zLeFYQ1DXfK9I3nkfXyy8wyAplAl-4U2TFsc3M3P_gnThxvH_Qaiq-zP7oNPmGRqykd7zzQIhH1Eu_lEf7iXo2kitZaMM3kssC7q3Zx6zx0vma__U3AgZMWH4Nh0DSoEmCWr4F2mP3f8Yjd2a2fRvkYYSdRjQ4xGGbSwTcLzz_9lcTaCp5v6Pn-9Ync6a1oiXeBodzz8ICqawAQMeeH8htwo1wnxf1AQY6f6zjimLWZtss63w9wpI9GFqptUhwUOamYvFZo2u5XJoHmfXVSUUGvkIo4FzZCN4kG2R4gG2arjiJYblTdbjNQ2MdkECe1oRPibd5SeIrcorNWEYGpLyE87JQFWiEOQS9EPl62grgN6r4gv0DAs0HyOrQnW8wSJLR57tzeC8viToof8JggiOFSrVoumd-FXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت صحنه اکران ۷۰ میلیمتری فیلم اودیسه نولان در سینمای IMAX
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/672570" target="_blank">📅 14:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafd5b944a.mp4?token=AWT8tAVT5-ARtss4D2DSLMNjBVDgmW_aGtWgzcRYD4aCS3gkC7EoeHqdq2HclV857HcRoj1AA-suP9I08c6HXzb9zXZ1QmogfrmaaF5QKN-8GM7eDYK2XYegExhNGvcknoCt5DV7sqQQlFoZmNg0ezgvC58dSf6fEDDh0TltVKkT3X5ju1vNw5YJNzM19ALXmzhS4oOakK6aHZhkV7g3551ni_PsxqhdQgHwOJmdVA2kkfYtAyu11ZCFKaFWtunwqv0JzcuBIHMuwGCtZRhyANrW5DeLJ-yaLdMwtJfGQscSQ_B9R5qeJIIE8S8U8lfa4liS2I0g8kBAfwOJE8l_e1k0sC3l1OOt_PZjgiqPu5GhDofl5BsHf9k95wp7SuWBz472tOWLzVxB2JHnNOAmcNoKcXAsgpI2CqDyRYRti4ciKY3JJJhTuvNrSkhNdNr0EBiKb_Fw9Nui3_4hf20Rq7NsYtdoikWfr0nO-lN5rVlaHAXm-i2fVG-TDxM-2Rkk9lXOJdQ59IWKZ09CB35Bqn-0TOOQdl_zZNEmEW-uwCl3clzuc5IE8kK--0PzYioSu1eSTEyhW0mzglteTWL_gReHmfQfE55pFcssH2qGAReeDLOGuxFluy_gulkekOcvlTxIuL-mw4d6SufnCqAvLLo6uK9RdHOa6obSVg2D7X8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafd5b944a.mp4?token=AWT8tAVT5-ARtss4D2DSLMNjBVDgmW_aGtWgzcRYD4aCS3gkC7EoeHqdq2HclV857HcRoj1AA-suP9I08c6HXzb9zXZ1QmogfrmaaF5QKN-8GM7eDYK2XYegExhNGvcknoCt5DV7sqQQlFoZmNg0ezgvC58dSf6fEDDh0TltVKkT3X5ju1vNw5YJNzM19ALXmzhS4oOakK6aHZhkV7g3551ni_PsxqhdQgHwOJmdVA2kkfYtAyu11ZCFKaFWtunwqv0JzcuBIHMuwGCtZRhyANrW5DeLJ-yaLdMwtJfGQscSQ_B9R5qeJIIE8S8U8lfa4liS2I0g8kBAfwOJE8l_e1k0sC3l1OOt_PZjgiqPu5GhDofl5BsHf9k95wp7SuWBz472tOWLzVxB2JHnNOAmcNoKcXAsgpI2CqDyRYRti4ciKY3JJJhTuvNrSkhNdNr0EBiKb_Fw9Nui3_4hf20Rq7NsYtdoikWfr0nO-lN5rVlaHAXm-i2fVG-TDxM-2Rkk9lXOJdQ59IWKZ09CB35Bqn-0TOOQdl_zZNEmEW-uwCl3clzuc5IE8kK--0PzYioSu1eSTEyhW0mzglteTWL_gReHmfQfE55pFcssH2qGAReeDLOGuxFluy_gulkekOcvlTxIuL-mw4d6SufnCqAvLLo6uK9RdHOa6obSVg2D7X8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازسرگیری آمدوشد در محور رفت تونل ایستگاه شهیدمیرزایی
🔹
محور برگشت این تونل هم که به دلیل تجاوز هوایی دشمن مسدود شده بود، تا فردا زیر بار ترافیک می رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/672569" target="_blank">📅 14:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672567">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
پزشکیان: اژه‌ای و قالیباف با تمام توان، همراه ما در مسیر احقاق حقوق ایران هستند
رئیس‌جمهور:
🔹
امروز باید مراقب باشیم اقدامات ما از انسجام علمی و قابلیت استناد برخوردار باشد.
🔹
در تاریخ انقلاب، چنین انسجامی میان قوا برای پیگیری حقوق ملت ایران بی‌سابقه است.
🔹
اژه‌ای و قالیباف با تمام توان، همراه ما در مسیر احقاق حقوق ایران هستند، هرچند گاهی حتی با نقدهای غیرمنصفانه نیز مواجه می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/672567" target="_blank">📅 14:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672566">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
۹۵ حمله آمریکا به ۱۲ شهرستان خوزستان در ۱۰ روز
/
۸ شهروند شهید شدند
معاون امنیتی استانداری خوزستان:
🔹
در ۱۰ روز گذشته، متجاوزان آمریکایی به ۹۵ نقطه در ۱۲ شهرستان استان خوزستان حمله کردند که در این حملات متجاوزان تروریستی آمریکا، ۸ نفر از شهروندان خوزستانی به درجه رفیع شهادت نائل آمدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/672566" target="_blank">📅 14:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672564">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8c90faa4.mp4?token=Xzgqnp_hJEu2Gxl-T4WnWgj6jkUYxNwjYGrJYj-dFy20yenqRMq_noOLeyqlzbFJagE8zFk8ftOJR29EWmpiQDLY1R08V-UvbLksRxWOWx4UrzGNIuxwPnj50yFqBRA2Z9zTfc5itEGvNHsVr8wzltzTxdAx68AhUCuQ_f3xHhRJ-mKmnz9r3jXszE6zWdNdLAGPeZE03Z1k4htaJNW5do-XPrhQ4hyWlLBxVeG3jn-GUPkl7_cwLnBEaIV9T0P1AJBCrv1SELlw9A97X1PFDj7KqFUq_bmW49kwskQJ_JJM8GlVKm6hbfaDCxt4wCSGcDXPAuaUX0KGdv3kq4p4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8c90faa4.mp4?token=Xzgqnp_hJEu2Gxl-T4WnWgj6jkUYxNwjYGrJYj-dFy20yenqRMq_noOLeyqlzbFJagE8zFk8ftOJR29EWmpiQDLY1R08V-UvbLksRxWOWx4UrzGNIuxwPnj50yFqBRA2Z9zTfc5itEGvNHsVr8wzltzTxdAx68AhUCuQ_f3xHhRJ-mKmnz9r3jXszE6zWdNdLAGPeZE03Z1k4htaJNW5do-XPrhQ4hyWlLBxVeG3jn-GUPkl7_cwLnBEaIV9T0P1AJBCrv1SELlw9A97X1PFDj7KqFUq_bmW49kwskQJ_JJM8GlVKm6hbfaDCxt4wCSGcDXPAuaUX0KGdv3kq4p4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر لحظهٔ پرتاب موشک‌های خیبرشکن، ذوالفقار، فاتح ۱۱۰، حاج قاسم و پهپادهای شاهد در موج‌های ۱۷ تا ۲۰ عملیات نصر ۲
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/672564" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672563">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff94ca366.mp4?token=PVIGXtCJYS9MenzFzD2ahQEnUI6bi1JQSavXdjtQFqyhyx0_UFGBAnArTZBJzsviyk2AxE_GcSalJA0RZVAud25IuINwoKV_BMw4oTghaNF1WtcR4JkqAexXX2suNSuiZ9j8PWljS8dDGP0CzKkfwVeBqD1eICNQx37IM8XZSDfzBPoEDDK2m8JSy7LB0g0XPQv1Fz2VHVKVzWjuIL858AZnDenIAI4XSsbeqshpj8-wiDiqJjJLVlqYDz89advm0ja74rWrwIeFly8XBgl0ZzPKSFrtfa0c-BkqEHHS6g8O1fbO7xPj34mDqkKlCGh0MLbPv1pX7tGTGa4NhSaU5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff94ca366.mp4?token=PVIGXtCJYS9MenzFzD2ahQEnUI6bi1JQSavXdjtQFqyhyx0_UFGBAnArTZBJzsviyk2AxE_GcSalJA0RZVAud25IuINwoKV_BMw4oTghaNF1WtcR4JkqAexXX2suNSuiZ9j8PWljS8dDGP0CzKkfwVeBqD1eICNQx37IM8XZSDfzBPoEDDK2m8JSy7LB0g0XPQv1Fz2VHVKVzWjuIL858AZnDenIAI4XSsbeqshpj8-wiDiqJjJLVlqYDz89advm0ja74rWrwIeFly8XBgl0ZzPKSFrtfa0c-BkqEHHS6g8O1fbO7xPj34mDqkKlCGh0MLbPv1pX7tGTGa4NhSaU5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتیجه نقص‌فنی و سقوط موشک پدافندی پاتریوت در کویت روی خانه‌ غیرنظامیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672563" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672562">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تیزر قسمت پنجم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای طیب پیشداد که در حین عمل جراحی رخ می‌دهد و به دلیل یاد نام امام حسین (ع) هنگام خوردن آب از کودکی، با عروج به تمامی آسمان‌ها ، یاحسین را شنیده و با همراه شدن توسط روح پدر همسرشان، جهنمیان و چگونگی عذاب آنها را درک کرده و درنهایت با دیدن فرزند سقط شده‌شان که از عمد انجام شده، حال خوب ایشان دگرگون می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: طیب پیشداد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/672562" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672561">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6358d8ec15.mp4?token=VeEOSWpakurUPdEfaUD7N8H2iP9AxmPfkad-oEMeeByrMlvsRKsnwnKzFybwhIlQsXofR7K87AzhT838kKkMquvJM6SvCI-TN1SHmj7p-KDRxD3Z_gf40p3DOoZvzdTiYtltRVOhs809TcqnBaSRaakO3k58HWmolvDTL9o6g-Bd-wUzf-lbH2ib7yG8SQA0rm2RhudFG7c20apnB2VtfUeGi3_6Oh6xidSZ3ycLlmp77T0NttAHL1xe2VF50NIzKsoQy-V-XrCTWMm-Gcager7GkeGVt4Mtm-1V9egN667--TwPs3QQ5gnECL2yrZ8p7gaECJ6arQAVO-ZmtKIgqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6358d8ec15.mp4?token=VeEOSWpakurUPdEfaUD7N8H2iP9AxmPfkad-oEMeeByrMlvsRKsnwnKzFybwhIlQsXofR7K87AzhT838kKkMquvJM6SvCI-TN1SHmj7p-KDRxD3Z_gf40p3DOoZvzdTiYtltRVOhs809TcqnBaSRaakO3k58HWmolvDTL9o6g-Bd-wUzf-lbH2ib7yG8SQA0rm2RhudFG7c20apnB2VtfUeGi3_6Oh6xidSZ3ycLlmp77T0NttAHL1xe2VF50NIzKsoQy-V-XrCTWMm-Gcager7GkeGVt4Mtm-1V9egN667--TwPs3QQ5gnECL2yrZ8p7gaECJ6arQAVO-ZmtKIgqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩺
سلامتی رو به شانس نسپارید!
فشار خون بالا معمولاً هیچ علامتی ندارد، اما می‌تواند خطرات جدی برای سلامتی ایجاد کند. با یک دستگاه فشارسنج خانگی، هر زمان که بخواهید در کمتر از چند دقیقه فشار خونتان را اندازه‌گیری کنید.
✅
اندازه‌گیری سریع و دقیق
✅
قابلیت تشخیص آریتمی
✅
تشخیص فشار دیاستولیک / سیستولیک
✅
حافظه ذخیره نتایج : بله
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
💰
قیمت قبلی: 1,698,000 تومان
🔥
قیمت ویژه: 1,398,000 تومان
📦
همین حالا سفارش دهید و با خیال راحت سلامت خود و عزیزانتان را زیر نظر داشته باشید.
https://memarket24.ir/product/brief/37832/180124/</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/672561" target="_blank">📅 14:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672560">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N67zYranmSAgQEW01D-FS437rO-RcrgvxDILi-f6MU6wGMRyubdY-__rex_0JG_bL6HzCzKErlNWVIH-ls0VloWJB5kiCXTtESv_1OJf1ZpbZwgf_cyNBDzW8SD66xsV3e-frRYfl-UbZ72wbY_oVFyj9Sr8m2C_0akaPs5sRvOZAv6Uf1vFbG48FLafrT3Y2Uphr8SOGND897sfHsQxGwKWZ4c6rjJL_-iuNIstbz3fVZArnBJZFUSAyi1ZHrfz8vdXxL39vutEyrNlT8Dts8CXvJ3L9lYH3gJ7ODaQkhjgGrPkQpYdFqjfp2y4GWJB8vq62MU6CvUAVBtq7JlGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا هرمز سفره ایرانی را نجات می‌دهد
؟
🔹
تاثیر اقتصادی مدیریت تنگه هرمز بر اقتصاد و معیشت ایرانی‌ها، از افزایش ثروت و افزایش درآمد نفتی تا بی اثر سازی تحریم‌ها
🔹
تنگه هرمز به عنوانی بخشی از سرزمین کهن ایران می‌توان به یک منبع ثروت برای مردم تبدیل شود که شرط آن حفظ مدیریت ایران بر آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/672560" target="_blank">📅 14:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672555">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pF8ZMQvsaFOAitPILtA3wWXGYqXBv54MnH3BCdzHhTSliEM15UREZmGukVRtwEi4p9OLDk-RQAMv8HQJwJufHLUhXRzMrfizjTjIpNFUeOnUAbZpqDte7o5ufD4Wo2XSQK4ZKDkEKEBVA0o5JczXb7ATrpwCCz7jp1Yk_Zxm5YtMSCttgL5L21DZ9ykM02Qz60816iSnVKqdt2vqpFBoS1efbY582VmbUr9CLHK1mADsMBfyDDc7rtb_8t8A9wuIepEPbD7MWizBuYmchSBDRyJF2pUVrFDmTiExrWfr5hoaETlSU2hS7Y1QZH8HfQvvBLXrsKoMoPqbEzfQiTkXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8vn03wVEApelMUcEXjTo4GoUipBjiXw9H9dh5khJwkGudCjSHdSReGRdu4PrcPgJhoAvnUM418IJ41_iDdh0wxUm4DFd-QtAzmLKrVpXb811flU1U5H85ZrIJCPyUyyXEwX3NTFdRiiJlA3J6mzBeGlHDkilpQ4o1nGJ_tgeoYn6Q-8ctkiQALRdh35BhXqImcG8w65l_9bXXplZO22Pxp2Ya3X9sRLZxSDfcBNHFKj5Y0C_UCdhTrEVXZlyaieCCIFHZbdo_8l_VZALtiBEhVPgtAdnfeFvG_uga88ytrcO6cI6g3isfDbJuPnB4EeRu8Cl3CTRx1CNVD7LX2ddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBa_XvHwPsq0biNdoqIoGHdlFTKJv6mcPOmP2bocgeOU0THIj3k7T2fcjtvm2Xw0RqODE25S6QSf3eJ_hJQ7Yt_PqAk4nRIRYYzEiwg214ayt2tCmbeK3BZqHUdcCKoqLTJr4gRBxnk0ebQbdGhj24710AFIASea-xrIwaaBjf3w_kX5443RJKUoYFu_flyjb6EKSSIf4RE_oNR2lujzC4maW1pMJMgtlI3D74uCp58LvIrMEaKtUUL_0HcJRZ5yiCouDxdfUzfBVV2qr_FVkB_4QL2ZRfH8wZkMbR3RYDxYN3g9xTsBhezYwI7UJFGGZV3KxIKEs5Ei0KkHwurVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7cNTtEV3bFWpkebFs26JB71Est4aa8HW2_ysQOAXnsu8bqEQB1cjBzNtj4efBkN0UXd1rpsLslk3XlQnHTC5e3tm66pXpBwIufL5l_SJ9ZRMF75L7X9a0Rn8pn1GTTq4g6PaYD5K8FKzc-5IFbP8ezEKkHCbo2KQYeZQhqJTohg_UU-2Kd0In9_8NjTDKDYtCE0ooQaY4FyTp4jjqjd6IqLTzsi7RNrKRvuFr5L98nxxCPa-sRE85901rGbKVaMROdjnJPOSynQcotlNCrCwGyloxUuHXMEVnBJYV1bdYAD20UliAZGIVRxu6Q9prkl09znzOybknglz8altRnM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAROHBSgBqI28yIQrjE37s9UqUpaPveOMp9h1QLKtUhP3nk1WdtLP9mO8ERoYbIl_eCjkK2Df3_4Ofnm9dFsKQEGijXecaswz0kHkXHt8zupkt1lRWu7HaJFxvOxB1lR5Ncek17OPQyDFiH8uEH6ovAMeGUsosKGyb_hzuyq6hTqntxWy37GBJkiwKXOuFgEUpV1814-SNV57FOJDj9picT8wSXi9jKmyVyF33EERD7t5dSJv2sihWfNGHa3pdJFlg4rZjyGiueUWaVvk96wWKT7q3FfG1Zjqlr_v8YdAnJDXv7yuCzXg6zAfD_J-ErdZA_7_jyZZWYh8S6sInRn2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کفش مناسب، رمز یک استایل جذاب و حرفه‌ای؛ این نکات را از دست ندهید
👠
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/672555" target="_blank">📅 14:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672552">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرفوری
pinned «
♦️
وضعیت امتحانات و کنکور در جنوب کشور چگونه است؟
🔹
سهمیه مناطق جنگی: برای داوطلبان کنکور کارشناسی ارشد استان‌های جنوبی، سهمیه مناطق جنگی در نظر گرفته شد.
🔹
تعویق امتحانات نهایی: امتحانات نهایی ۲۵ و ۲۷ تیر پایه دوازدهم در هرمزگان، بوشهر، خوزستان و سیستان‌ و…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/672552" target="_blank">📅 13:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672551">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
وضعیت امتحانات و کنکور در جنوب کشور چگونه است؟
🔹
سهمیه مناطق جنگی
: برای داوطلبان کنکور کارشناسی ارشد استان‌های جنوبی، سهمیه مناطق جنگی در نظر گرفته شد.
🔹
تعویق امتحانات نهایی
: امتحانات نهایی ۲۵ و ۲۷ تیر پایه دوازدهم در هرمزگان، بوشهر، خوزستان و سیستان‌ و بلوچستان به زمان دیگری موکول شد.
🔹
دانشگاه‌ها
: امتحانات دانشگاه‌های هرمزگان، بوشهر و نوار جنوبی سیستان‌ و بلوچستان به‌صورت مجازی برگزار می‌شود.
🔹
علوم پزشکی اهواز
: کلاس‌ها و امتحانات حضوری دانشگاه علوم پزشکی اهواز تا پایان تیرماه تعطیل است، اما آزمون‌های کشوری طبق برنامه برگزار می‌شود.
🔹
امتحانات معوق
: زمان جدید برگزاری امتحانات نهایی هنوز اعلام نشده و متعاقباً اطلاع‌رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/672551" target="_blank">📅 13:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672549">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIYJctFCkXTbSL8_H0_8sVdxnAQ2uSHccrT9nB9RfdE2zvJrD-W5UCBiSmuz4FiUgAgeSRgVwibRHAIqwpebj0_PQT7n2Q4nTS6qAQdIs4TA6RHJprjuMTCDOTBKzUOp8t4z7ESoFe5nIHSgxX-69aBx72DD0IlhYgPd8_SBPhEwKhh-A7xwtorlblRF17xHO4wHiN2WLxuzRCk0LMQ4QuTar304HrqxoQZgj7IPxnhigvqUyOxj6GBjGoQPnAGyS_BmOuF_Xgcu_Cyj5YtP8CC8Ju6U81XpmU28f_8BZvLmTbwktL0F21Gorx7TR3bWtN236roIY4pejPJau6r7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با بسته شدن تنگه هرمز توسط ایران، میانگین قیمت هر گالن بنزین در ایالات متحده مجدداً در حال افزایش است و به زودی به ۴ دلار خواهد رسید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/672549" target="_blank">📅 13:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672545">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
حمله جنایتکارانه آمریکا به آب‌شیرین‌کن بونجی جاسک/ ۲۰ روستای ۱۰ هزار نفری بی‌آب شد  مدیرعامل شرکت آب و فاضلاب هرمزگان:
🔹
آمریکا در حمله تروریستی به آب‌شیرین‌کن بونجی در غرب جاسک، ایستگاه پمپاژ و ترانس برق آن را تخریب کرد. این تأسیسات روزانه ۳۱۵۰ مترمکعب آب…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/672545" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672543">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
منابع عربی: پایگاه «الازرق» متعلق به نظامیان تروریست آمریکا هدف حملات موشکی قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672543" target="_blank">📅 13:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672540">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
امتحانات دانشگاه‌‌های ۳ استان جنوبی مجازی شد
وزارت علوم:
🔹
امتحانات دانشگاه‌های ۳ استان هرمزگان، بوشهر و نوار جنوبی سیستان‌وبلوچستان به‌صورت مجازی برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/672540" target="_blank">📅 13:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672539">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رویترز: کویت یکی از بدترین شب‌های خود را در حملات تلافی‌جویانه ایران سپری کرد
رویترز:
🔹
کویت یکی از بدترین شب‌های خود را از زمان آغاز درگیری‌ها در خاورمیانه، در جریان حملات تلافی‌جویانه ایران سپری کرده است.
🔹
در جریان این حملات، دومین نیروگاه تولید برق در کویت طی دو روز گذشته هدف قرار گرفته و حریم هوایی این کشور نیز بسته شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/672539" target="_blank">📅 13:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672536">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF9G99nnS94uRXLsjmJ2J6OZyRxC_V94dHlu2B_9ov9z8YWB5qFRN5VKj_J9OMt7aF-xgqiQQYKuTF8g1AD_ZkcXlDWok6bqkXPREjOlwLz_uOGZa9IalxFgGpWdbYC_8bhFYtRr1fIs_t7E-BBmf2tTliEFOJ4931Kz_t50igJIfXtqjqXgdGZ0Dcaa7_I7pJG45elLEU1sWhLfHUmeIAP5tKhqC7395hDfu6tR1qZa5FkcuyZ0-rIEG3KtXZC23bw2pA43Q2tv4UZRI_hi9NhSIcCkiBRw8OoDBtzqmLA-hiotGp0Laor5WRiH8ux15IrUl88o8kg06675qHD18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام گروه سنی ایران بیشتر در بازار رمزارزها حضور دارند؟
🔹
آمارهای منتشر شده در گزارش دوسالانه نوبیتکس نشان می‌دهد که ۳۵ درصد جمعیت کاربران این صرافی در بازه سنی ۳۱ تا ۴۰ سال هستند.
🔹
آماری که نشان دهنده این است که حضور در بازارهای رمزارز عمدتا توسط افرادی انتخاب می‌شود که در دوره ثبات مالی و شغلی و اوج توان تصمیم‌گیری اقتصادی خود قرار دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/672536" target="_blank">📅 13:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672532">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
گوگل با هوش مصنوعی یکی از گل‌های خاطره‌انگیز پله را بازسازی کرد
🔹
هوش مصنوعی گوگل موفق شده تا یکی از خاطره‌انگیزترین گل‌های پله، اسطوره فوتبال برزیل که هیچ ویدیویی از آن وجود نداشت را فقط با توصیف افرادی که آن را دیده بودند بازسازی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/672532" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672531">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده جاسک: آمریکا‌یی‌ها زمینی بیایند با تابوت‌هایشان برمی‌گردند
عبدالکریم هاشمی، نماینده جاسک در مجلس در
#گفتگو
با خبرفوری:
🔹
زدن راه‌های ارتباطی بندرعباس، حمله زمینی نیست و دشمن می‌خواهد ارتباط بنادر و دریا را با مرکز قطع کنند. احتمال حمله زمینی را رد نمی‌کنم و اگر این‌ها پا به عرصه خاک ایران بگذارند، باید انشاالله تابوت‌ها را به آمریکا برگردانیم.
🔹
هر راهی که زده شود، راه‌های جایگزینی وجود دارد و انشاالله به مشکلی بر نمی‌خوریم و ترمیم خواهد شد. اصلا نیازی به خارج کردن مردم بندرعباس و اینگونه اقدامات وجود ندارد و راه‌های جایگزین برای خدمات، کمک و پشتیبانی وجود دارد.
@TV_Fori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672531" target="_blank">📅 13:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672529">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj0jNGtZFprJJO3BlRNxRgDnNbnwTkzmxUFlNqUaXWHjIqhTCl72fLnfaOF0brzlqO0H8zz632IloaRHZjMQsCOYDJZ9BRnYpV7NsVhUqyFwQxErQUHcMk_aEM39siZdH757i67KJUiRZADAh77pGXJLAHoiEb2F0slgw9M-2Z_b4vL0a2lS6A4KFTtR5WOwkN1rRrktETNq-zScI4Eam40s1W_0qqb-4nzrY9rCvPjz5SXH0UVb-HU5o31kFFwHXcnI5TQpSR1OQibRCENL_DZcefGRejZGn8n2pcr9CTysv-xTXT_VbaV0_3zRA3DYjDacKTyAEJBaJECr9SgBRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه ۳۴۰ نفر در دوره مدیریت پیشین کیش‌ایر در این ایرلاین استخدام شده‌اند؟
🔹
پس از انتشار گزارش‌ها و نامه‌های سازمان حسابرسی که از ابهاماتی در مدیریت قراردادها، کنترل هزینه‌های مشاوره‌ای، اخذ تضامین، رعایت ضوابط معاملاتی و انضباط پرداخت‌ها در دوره پیشین حکایت دارد، اکنون موضوع استخدام گسترده بستگان، آشنایان و معرفی‌شدگان مدیران و برخی مسئولان در بخش‌های مختلف شرکت نیز مطرح شده است.
🔹
بررسی اسناد موجود نشان می‌دهد که در دوره مدیریت پیشین کیش‌ایر، هم‌زمان با خروج یا منفک‌شدن حدود ۳۶۰ نفر از کارکنان، نزدیک به ۳۴۰ نیروی جدید به مجموعه اضافه شده‌اند؛ جابه‌جایی گسترده‌ای که به گفته برخی کارشناسان، نیازمند توضیح درباره منطق مدیریتی، فرآیند تصمیم‌گیری و معیارهای استخدام است.
🔹
اکنون مهم‌ترین پرسش این است که آیا جذب نیروی انسانی در آن دوره بر اساس نیاز واقعی شرکت و معیارهای حرفه‌ای انجام شده، یا روابط و معرفی‌های غیرسازمانی در تصمیم‌گیری‌ها نقش پررنگ‌تری داشته‌اند؟
مشروح خبر
👇
https://B2n.ir/fd6213
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672529" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672520">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjRrW3KgiJLt6rzKz_IjQzB8LiXxbw0tq7HjZeWzTMLEXx4D6R8rU1-S9kbIhszEvfRw-O2vgCRwFECfkvKLi6lSWPMeiz7Xe5P3Ha-IdeFqvZXSVvMNPc19ejt7ds9nPXydYI-mngdVlDfSw6Bo5EH-6AQGRNVxwXm30DxdUo3KpxOerYRGkXzwuo3fekDULXC0Qe31RzN5mhhb1x-lXx-6ufyUcFS42I-IUW66xhVDMzLhXSIpS6G5Eu-T2MGu3www70yRetR79QWqLBbtoyVSot6kIqJ9zr5TUhjbJJ_Bj5KX4gvD5BUSGlM8jLA8sP4LVfLoBlhSJGdfR2gRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4U6_tIB0V98zzaunOKdYRgJTuzYZHXcw0mNSj4m-wHoWi8IcftvDfOEdZBJYzY1PwJ2KwI9t27p_ZXqi3EP1I6SsQ2ojbUIp-0cT_eGSGl-5IdT3S5RkV4AXEYsHtsyta9PzYVlfuLLfMTiJoR_biwAliC_xOfbvsPM9Eyepv7Pk8TGWTEPyVz6WQG_xbs2H8ZzpYGi9R6iEfkAZCJaadWjbXSglZQUQ5rxN2JmRFDGa4Zp4cdVKqBU0QTzZTXspidYCcw2Ich0xKM_c0C24_zGrjJ4lB7_CH2Jm4CXL0CN3E7NgZnCGDmZTSumSn3S5vYhoixxTcokZRnWWQ_nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kD1L-lb75V6qlOP2P-cpSjLSzGa9cFwYvk5Vp_GfTuNhVrQddMlRESUfvZwkrzm0Z6A78X7-5JO5wdVi3tRAQpbt2ZHHQZHxJXm-3wt_uYD2hqTN2JTuSMCpqaq_yJDZVn8oZQQXoEKa5u0jMJlxUA6gFS0n916r75Acs-tPqMyq2Uin3G7p1eSkmAwyde5bY6ay3XkXbDsx-q1KFww0qgMgFZkPR9s0soE6mdWBHodcSg5lfy4PI_GPDxmgxcLBaWEwFdx8UFCGJCqxwl5xqIjY1C0F9no30-tWagM8numJ6SIv2XTM69tUWO9NzIEUw3hp_gddhLtYJNz8hr2Bnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phZVUd5V9HGi3R3Qg4XLJoVTzakJVBovohpOyzoWuQqG2DPhBA5niUeImYrJJxIAQjI6vNWwhJoLP553GcG_coDL2ejnGVg7JjNp_tqq4LelJxfkmj8h7N3STfxf6PQCy-RY2jGPKIKtEbMWWWNtOXQU3mAsHrSoKSfbrp_qzAcRcgSQFDoAkVcWSm9Vs6IJoECHYdd4c7vvMV32lwouKJZh16u_uXIDskcXkAAJVVnlGPd3e6BnlIsRti0yjNjl7hhCmmVTyAaTi-w5Ev3NUSGhcM5U9L971EJg9XnsFVPk5oHEhvP0zwfuAc9c16tZuGkcPnW3SnhdTZ8-cwkPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBryRxvwHghYdIjHTTK2056VU1ZpCpO5f05A2bGV30VOZZzXIJOvgwNgoioRFphLRCpXEu54NCadGO0B0gxwy00Zu9tBO4oQkno2ad9r4-gLhF9KcpkjMQugYu-t-Af4BzwJQRCrgYfVh56vFExyd4IlLo70Hk84jgDk4gKZcobGWKLamJAUNAEKP2N-qsMv1vytq0_XhSzIxWIB16wJF0w4znc188o_AsU0Fn7QHZHKcrmjgD-D2QTxZOQrUXi_Vhnd6IQdkwZWLgVVdkJxcLoU20_MO5cvvcD-Y3AGRkGVWYGpWxjUrkcrrhEHyHStbW0tsl4k7v-x7I-gFq9GOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiBfiReZYPRvmr3bvm_hPHOXsGShe4oXoyUxfUIrl757JJ7wWeY4aeNoS6GSvHzfbQH9AQxZ3GlV8JoML8LueSlHXr5yT89azS8TElJsVgOTu1-3zqwMRk4QpFsv6KevKospJQwdTBqQ_NrMpUSTell1klgg0xBh1xPa-msrNfJIoeOeLqDePdfATMvxRIEwguZkg8qnWjnOmAeQ8AJjH_FSsJYspYxLEH1DZLbj8HW1KieiJi4c8t1qojYGdB1cbUK-AeqsDe6Ol7OpM2qfK7aBxkW3hzqAbUOIBp3nZjQMXyLj9JQn6kTOZ3nmUg9TBIsQ1DBNz3OP5S_wDJl5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9pMiAbzv69hwHglLgkk1uC6uO9IFnoL31WYBMzADvBmkAMlhhYi-gsiiVOMCX_E0HY7uzXhvUwKhdkkaGandkr_HDo2WnUooc62GWgtvcmnZmlFTR-5GHa1fuFr6OE9k8meNHdW6HCgAtKFOVy_DLKIv7IBr6GQje401vl-lqh9rdfQjHTu5whjeAjMZMad297HZaNtqVvs3v_0-TH5c38IHu13omsAiOTn36HDGyNNI2rDu-b-qVY3uV4XB4DGlX8F88OaUI9EdooMG_EHsumLjZsp4VKF6hKyFMWmMqcuuCm-IB5c4wkVrFpbV95EWfkB3UAT6iRUjIhYtQ3zVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJTJX644fwwCfomfRM6UFjJ964nIA2tbKvSZsqH58FEjBlX0d-sIJftMG2_XR5RVSyl_qOerW7UhJv12UafpO-WQVy3ZTGz31169WBxsBtV8BUbDRr1ow5e9AR-KBp38L8srXC-dYT90O6eE2PDHGWDIIecUloJExOtCtJl9V_dYvDLoyETseBrVWua9ePvOSouj6PYLjcHnZlq9wFhYfJ6T69_uiR8LpEF9Do6V2OO2arzhHHcTOemHiLeQPdNSgrW-QSFDgFlIk2IIqclIaBooQtlKzHKyTiRKZ7R51jHbwSBWnMFkdlGkAn3th6BuTBK4r6Hy6g5A_Lbprm5YVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وضعیت پل محور بندرعباس به رودان بعد از حملات دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/672520" target="_blank">📅 12:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672519">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران؛ مشاور کسب‌وکارها در مدیریت نقدینگی و عبور از بحران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه مدیریت مالی، به بنگاه‌های اقتصادی کمک می‌کند با مدیریت جریان نقدینگی و اولویت‌بندی هزینه‌ها، تاب‌آوری خود را در شرایط بحران و پسابحران افزایش دهند.
برگرفته از ویژه‌نامه آینده‌نگر «
نسخه سخت‌جانی بیشتر
»
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/672519" target="_blank">📅 12:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672517">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6dbe7790.mp4?token=MTdjaGjuIaRQfVcztzWGVGJpbiB5LkOjQeioE4QOAQ-YZl61yr80d5TbJ1ZYMqG5wXHiWVLTel7-MxWlX5Xldkp4obZtQYNB69ik5sTiFzvvybfiYr2jP8jBjUmG0llgDpkpDzTMECO1MEnw63e-9JREOv4uEOzbYvtA5FxRK2k8btgmJ8nIJwc3FGoNMHxnwzCuOxy6PV_19aZN4EmUBv18nvPcvDIG0_CMFGkxCJQ0p9dDPc0Ki-N7q-ud_aD7TiPkcQ05cNXKCoT3E5vS2UnHyZuIq72Rk7Gl1UBJWGXAUF3e4EsJWgrtaAMB2F_Wo0neIp9LhBJLJLxxE5tI9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6dbe7790.mp4?token=MTdjaGjuIaRQfVcztzWGVGJpbiB5LkOjQeioE4QOAQ-YZl61yr80d5TbJ1ZYMqG5wXHiWVLTel7-MxWlX5Xldkp4obZtQYNB69ik5sTiFzvvybfiYr2jP8jBjUmG0llgDpkpDzTMECO1MEnw63e-9JREOv4uEOzbYvtA5FxRK2k8btgmJ8nIJwc3FGoNMHxnwzCuOxy6PV_19aZN4EmUBv18nvPcvDIG0_CMFGkxCJQ0p9dDPc0Ki-N7q-ud_aD7TiPkcQ05cNXKCoT3E5vS2UnHyZuIq72Rk7Gl1UBJWGXAUF3e4EsJWgrtaAMB2F_Wo0neIp9LhBJLJLxxE5tI9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسمت چیه؟ احمد نادری
🔹
کلاس چندمی؟ دوم راهنمایی
🔹
کار تون چیه؟ دفاع از خلیج فارس‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/672517" target="_blank">📅 12:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672516">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKj4wkMRsyU5r5EYbpso_p5YlGisnv07oFUvT09R0Z1I5roiS6c78nh4QaJKG82P8PgckXzoMF0l7Rqjf7ztsz8HoZbHAnL9mCfhYfaVrgBKp3rLtpQr86qO7rLtWsI4ZyN9xKZhnj1_ms7nSAQlj6jSukPlxlq4Qe6m37RBCd56HeaO7ve5X6Ej5n58ohq37U2m4sdb7ZYCzYzDi-zEboAdQpxKH7RVQvc5MZxoM9G9_Ry5vT6bYZJnkMnC2lqDRFq8duq-XsX7DIgTQ7izpc5P2SAg_t2JxOAg-godyx7cXx_UppPwFF7EE1OmFLSfJs8KDT-jiSJL224XOfOXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۷ تیر ۱۴۰۵؛ ساعت ۱۲:۳۵
🔹
دلار امروز در بازار آزاد با جهش حدود ۵ هزار تومانی، معاملات هفته جدید را در سطح ۱۹۳ هزار و ۴۸۵ تومان آغاز کرد و همزمان، طلای ۱۸ عیار هم با رشد قیمت به ۱۸ میلیون و ۷۸۰ هزار تومان رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672516" target="_blank">📅 12:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672513">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0935780bf5.mp4?token=G0vL1eUXvzMbFLbAtC94cE2PPDgsU4b-UuTIgtfRcSl63BAe2USWMvEG4b6NSkjKCHkFeaiCx44cRwFRpHR42Du2dZiCPB5GwgSiEIZLLTMqug2-D5NBOy6VOYCbLKSoJ_VDPkG2oGH7u_k-0vN5Q_cL4e3W_8tOJmyOXw2lS2g4ln5u-H41Qn1RbGtewmTiL1WIIxKCE7kOyIBxGmkmiecTOJlApYTaVLjFZVPHfeEAvzQkd74u1kpdfBpFFT1bkVbhIm_odMHImBHsxk1h1xZOekA2pokqyjWyBkH_5F3GAbxLJOrWW77a1EzJZKCta7Y0idzUMO2cpc_20VNfMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0935780bf5.mp4?token=G0vL1eUXvzMbFLbAtC94cE2PPDgsU4b-UuTIgtfRcSl63BAe2USWMvEG4b6NSkjKCHkFeaiCx44cRwFRpHR42Du2dZiCPB5GwgSiEIZLLTMqug2-D5NBOy6VOYCbLKSoJ_VDPkG2oGH7u_k-0vN5Q_cL4e3W_8tOJmyOXw2lS2g4ln5u-H41Qn1RbGtewmTiL1WIIxKCE7kOyIBxGmkmiecTOJlApYTaVLjFZVPHfeEAvzQkd74u1kpdfBpFFT1bkVbhIm_odMHImBHsxk1h1xZOekA2pokqyjWyBkH_5F3GAbxLJOrWW77a1EzJZKCta7Y0idzUMO2cpc_20VNfMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوستالژی موبایل؛ وقتی اریکسون با کیبورد و باتری غول‌پیکر پادشاه بود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/672513" target="_blank">📅 12:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_IMP9jAGV67O6Yk_ofMTbxDv9T1ZfRgA34_T2OAJ6UxPUZyTH4LnwSl51Wu6qSUQ3TP4iyF-s7MmHrxoqIx9a_yB48gX6oP_J_XWgzeVQrKS3mPm2vgu_8FuDhmU-yIfs5NKnAH3xXFX_zxldxrw2UQOuuX2nCeeaYUeeOraFp_v818kNxtI7Rkx0ZLE_Wqw7xkTPiosRadLXkYzi9PCRcnNdWkA0dB0Qh0FKOzOHwl0KxpvmLilbndX58C0sFF4j1PlaRew_mOO9QAIFX9HiCHkAW6SrX-NsYnmBy-AYIhQyMjnH-GVWHurFEhYK4H0KCmD3qpLWyNoEW2Ve6PhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خانوارهای شهری در سال ۱۴۰۳ به نسبت سال ۱۴۰۲، تقریبا ۲۰ میلیون تومان بیشتر می‌توانستند پس‌انداز کنند!
🔹
طبق گزارش مرکز آمار، در سال ۱۴۰۲ هر خانوار شهری سالانه بطور متوسط ۲۵۶ میلیون تومان درآمد داشته و ۲۰۶ میلیون تومان هزینه زندگیش بوده اما در سال ۱۴۰۳ این آمار، ۳۴۳ میلیون تومان مربوط به درآمد و ۲۶۹ میلیون تومان مربوط به هزینه‌های زندگی گزارش شده است./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/672511" target="_blank">📅 12:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sG0XlMomey6oXJKBG1cLN5Oc2XxbITMISrakUXjhg-y8ycbB6SqYDRwe4QjRtlah6oxfDpwele7XpKYSSYREcQHf6jVIj7uqr3XY4mwnFgCT2HDmqsCDMOZKwuCQ3fz2GyGd74AJriBnaskzvCpabnCSB7nSd4ry9525-rP99lraWdaiWznpacBLnlPkpg-eZY2E643c3TYkoXkN5h7yJFqc4oRHbJYTQt4Ev4mruSRhgCfYqL43QU4bXNvEuYrwQav5fyEBjtt1YwtNf00WpL4d2QeFu8wXKz1l0k6DM6-38P9BMQEJorNOQms70Gwn05s27nXJQYoYnonQcdcCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lf2-DPRg3Gat5jSgYTe8oqCs9t7tfJjpOYoE8wWzGIz7EAfdfONWSlo4aCwkV4v7uMPCr0ziuLjAa_ylm_hDHrKly-SozyjP2ddomGHbS5ExeUAlncSq1q51YK_i6qI6a9cOscK-3OVke0rODb-HjprkI94EYR1AkS85Rjn9RRNFv6Axp40X7LfGGokd1-VSo2re-t82F22TQFPFVOMcWG6ytogfOU6-xrMnXoyrQ1ujdliKw4wn8NXAbUtY9bsbbgb7un-Syp57je3rhHMKboXOp8yc3I5jjVicbTAzZkaPmzuze2WLpVKSz4FzfjI-URGNixMztl1gjVwBiLEKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNaRXi6HeY7VqcVVHIklJ4ZV9j92mGL7aL8qSu6DrEqomcBQS8_R9F4uRhE-jkG0fCWssEZYhoiRPtxTCJbV42sXnr5qRYZOyfLAx-FLwPXIn_lZ_kvbfXSwQr6oVdLx6oUrI0KUvoA6govFPEeZ1WAic-dsDa6DpxrMs_PX8OulpLQgzwd3I_EwUCnYwgWUpTL1vE1l6skxAWqbhjRcAwHs2VVxgQQhiXoU0MDW5F_Td4x2WAjsQL00UOdCvGtyzOMtpBMyWbpuzSQmKrUgBYsnh64KIjVbyzMfIP-kWBgzL8tJMd3mnGHtzeT1MOWomr49uhANMlf1j6nhxwusnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvid42XnNkeJkTmyLhZVTBfeMP-ayry1qZ9c24UIu41T1HAV_d0dKIMd84pg8z_wniC1KszVQ_91zCw7JqlqdseOHwOf-RXeJP8CX2N_m38-UB5as7TbAJoGeD_P42Wtvz73jUHJTo-SDCdSbmlquBYh-ViPwrUmRaQDfRjo1z9fAWXWAAwIp0nVgjqwaFzNvBD9PKblgUdBngXuz-802HWakFPptsaNrzcRRbqfzeB8YGZzm-sTti5rGgWY6oRx-KdiMGPGEduGEdcOzPcZfe9WvfZMo7yxaCbo3ISHmGsGRUQOkGb0xoREuT3JRRLS-k94N3BjatGLIaW31aGftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CgXulAwc5Z16F9tMI_zP6hgFsVnbRh8h5nR-fRsnczQPySEqMWHfQ-aP_8oms5V1yKutaWdy8_YDBsaoyH7vLqo_h7GniEnzmR6ROgzlHCW7T0FtTIZxdf2IHcoRpwh4zcPSEFeRobbYNzhc7MCGPWZrcHHWTnxBbSFAHMJyjFZnM9fwmCgkvYdN-lXOfCcHhMIvhQkdqS-X_37Fsx_BebdENPfFTSO5Tbm3fMhhZN0TEHbSoWuGaO-ZssSz9oLNNiF9K0oLnML7UCb-Gy-pQ0fXkq1emVjvErkQFjWtHSLbPpUGCdxG0dhq3vN78AlCGIJTMOna9Ft8eRL311l79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAw0E6Et0KaJ9r7quVygt8nL3eEFggbcB4rRLbQ1-epLefWkIVJi0qKECKQwzFUAy316Y9O7fXMxzNBF1bIqmcDS2xEtXvFC9I0RG6xElbKRUb8Tqz7-JsN5iZisxwGpjKEJKaDjVws-1Ds8dCAQgFK63z4sY_trKC6pNV3aShS6iOX71GgyiRhJzdR2vciwUPrdc4tdcRV2JU54JzkK3SVClm5AaRu-Z1DHSVaEK_5hcr9e2o5LgTHuu3Pf600F6yC7-ZdDigYebdAXx5BQ3ghd2fN6-AskPVI6wUhcGFEVQDPH1qVfarKh0X1GxnJ8xfeaBEicZWFvECb-5_mi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgC3FhryYXh3v4_SYUnv8ctA6_P9Mi66gmK_Cp7A0ywYVvF_wJbqiLxdtBMAjE8jU61m5g9Xcs3xjN95RC7Hs_U4_DtWQP9knUbMkxsuyhYgwmh3f2Z03EgeFn5pZ8t9MR8FhmW1eMyR5o-mZzKEltF-YY-9hCn9gYWXH6anBcEYA-d0i5lfd-JXEb8l-44IXziBaxLAeyvxi203wFuLiQaTh09f7dn8JzAAju_lTlw0fOMvOAMjrdXoVvU4g-BUh6zLKmItJmBxK5E67i5D2AWRZF9h8y0Q2lAb1A-kYnt7tUNwm0xPmH4jakfcWIgab0ZAMQ4QhgyoPNQuRWP0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcEabckDRa49xbH9puuaiE6MKdPwPrnm0QFEt0eEGI8q-q3RgTSCQUMvuLM5Arg2VI8gugrDLOquvVdlm6efh1d8gcB8raiCH0x5dk44IirjYrjcZCxFKGNAYluv2IJPXW_E6sjJ7quuhTaveQOy5CFY8HXcML5X1KEz9E2F9Gi-r0fR8dCGxMFbet3Iecq5CWZwURXu-CjyZoYbXJzFmKSYthBOkGxdlnq17svxnZDvBSzsp-pLCQFotMNHbSP6xZl5KM35ixswymV7uuddj9WD2RspU27K-HQb6BI2WLxDL0HbGRNdvfWqqPF9bdSaLq-NiwGOAZtksIk_NPTMdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌱
کمپین «نه به پلاستیک»
🔹
تغییر، از یک انتخاب ساده شروع می‌شود…
🔹
در ادامه کمپین «نه به پلاستیک»، تعدادی ساک پارچه‌ای از طرف خبرفوری میان مردم توزیع شد؛ با این هدف که استفاده از کیسه‌های پلاستیکی کمتر و یک انتخاب پایدارتر، جایگزین آن شود.
🔹
هر ساک پارچه‌ای، یعنی یک قدم کمتر برای مصرف پلاستیک؛
و یک قدم بیشتر برای حفظ طبیعت
🌱
شما هم با کنار گذاشتن کیسه‌های پلاستیکی، به کمپین
#نه_به_پلاستیک
بپیوندید.
#نه_به_پلاستیک
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/672503" target="_blank">📅 12:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
اسکای‌نیوز: آمریکا دروغ گفت، آنها به مدرسه میناب حمله کردند
اسکای نیوز:
🔹
تحقیقات تازه و بررسی‌های مستقل نشان می‌دهد که برخلاف ادعاهای دونالد ترامپ، شواهد موجود مسئولیت ایالات متحده را در این حمله تقویت می‌کند.
🔹
به گفته هفت کارشناس مستقل و سه منبع نظامی، حمله با موشک‌های کروز تاماهاک و بر اساس اطلاعات هدف‌گیری قدیمی و خطاهای اطلاعاتی انجام شده است.
🔹
همچنین مدل سه‌ بعدی تهیه‌ شده با همکاری Forensic Architecture نشان می‌دهد مدرسه هدف‌قرارگرفته دست‌کم یک دهه از محوطه مرتبط با نیروی دریایی ایران به‌صورت فیزیکی جدا بوده و حملات نیز کاملاً دقیق و هدفمند اجرا شده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672502" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672500">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoyAJ-Qg5urryuRjSgILPvuaNWOCmN6eO2VGujINS6udnqjm0-X0ivOCfJetFIAhp1mOJUzax2o_FN0wX0tgj6CoyG29gQJCdhmEbUT0a6ICqa1rsdX7P4Xoi_pzx0Lh5A3PedE0wpvqyLR77vwUN4fSuLiPfaUmFUNemvgawXJH1yCXOTTY232n7maMYv4y-7DcPaKwiuKkDNjk76JHZi6rdl0_oDrpJA0PdWzwQ4MMPDDG1bcXLZJLz4QmfSSqXo8_Nz_2GdnbKbvteq0k16qOr28ymC6sZVwR44_lwoEixLn_Mpd-244uRJOCRH3XnzhRl_DWPJh9DTAcl_Q7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی جنایت جدید آمریکا، آب شرب ۱۰ هزار نفر قطع شد
🔹
در پی حمله وحشیانه آمریکا به آب‌شیرین‌کن بونجی در غرب شهرستان جاسک، تأمین آب آشامیدنی ۲۰ روستا با جمعیتی حدود ۱۰ هزار نفر به‌طور کامل مختل شد.
🔹
این آب‌شیرین‌کن با ظرفیت تولید روزانه ۳۱۵۰ مترمکعب آب، به‌طور کامل از مدار بهره‌برداری خارج شد.
@amarfact</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672500" target="_blank">📅 12:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672499">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6084cddc9.mp4?token=eJmdy-fLCwihoPerlKj4zJIImT9Mnx8YdU9GzEVJhIl8i7BGBGSesBhWj_W2Bg9OBaxYscmsv70OcQ3hE3sL5CsosEorGW6wvzlm7aWTjGbO1k3MLdyIoJGFQYdXZXsd5_yapB89-8DipFuimdwiP782rOKwEBp0pYgJhFrX6fgkBHx3puTpctPBPOYC4jNDmF0UKpWioCDCPjjkpxBZR8Gto9vDfeS86ltOrDI7LwuwcsNSaUWSWLJmmU3DRD3zDJt22DOb8cZK25kbsqa0ul-NEliNfbgfXWPQh2kKobl-noXgqckrGPsDuZ9baITsooXhQLrw29tS6CMEKuDCa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6084cddc9.mp4?token=eJmdy-fLCwihoPerlKj4zJIImT9Mnx8YdU9GzEVJhIl8i7BGBGSesBhWj_W2Bg9OBaxYscmsv70OcQ3hE3sL5CsosEorGW6wvzlm7aWTjGbO1k3MLdyIoJGFQYdXZXsd5_yapB89-8DipFuimdwiP782rOKwEBp0pYgJhFrX6fgkBHx3puTpctPBPOYC4jNDmF0UKpWioCDCPjjkpxBZR8Gto9vDfeS86ltOrDI7LwuwcsNSaUWSWLJmmU3DRD3zDJt22DOb8cZK25kbsqa0ul-NEliNfbgfXWPQh2kKobl-noXgqckrGPsDuZ9baITsooXhQLrw29tS6CMEKuDCa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهندسان ایرانی شاهکار کردند؛ مسیر جایگزین محور رودان ـ بندرعباس در کمترین زمان بازگشایی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/672499" target="_blank">📅 12:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ggtI16y3OrLwBUzkt1A0QLfvNBFCGQSZlBnWmkx4p0DqrkGg-c6N8JVn1A-PgBZ6tOa0zg7nqv_FTOCiopwvNy_jewUWx21OU4ykl_s9wdLQiXV0Mb_cXndptVxdhz16rtPGOkVMhmn5wlNu2UWNa2_z3L3EM08PG5etz3DlGKsYUe3yaGUu-K9ZiCkKKcLrLLdOuyplSABfvQvqU4B18KOfzIitjPeJDZKBeaV-6KOOkvV17ni5CzdwLUU8hNTl0phVp8MfNgLCa6i_uztWWYQ2HKAgJi_ayB6-NkhvOZERZYTD17jIfSZyZRlNjxeXts-9-GOf0HXHI3FPtBTsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رقابت حساس و جذاب فرانسه و انگلیس برای کسب مقام سومی جام جهانی ۲۰۲۶
🇫🇷
فرانسه
⚔️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏟
ورزشگاه میامی | ۰۰:۳۰
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/672496" target="_blank">📅 12:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c9cc90b41.mp4?token=gBP4MXURUgNtuS4Qgz8yNrgTErgAGtQDM0myejxpl37ZLzptfrXIUdr1yUDPgC10ml1FcnIM_yadqOy9ClUR0X2Mix8vPw_2QuLLv17lkCRiofE_oL5kaND3vSljhKP-cjqbkbYr2Rq8qtQWmQuiET61X-cL-b34Hwyf7EQip0MAIVQmELY_n2nzKzpl3ssyXFkEHW5YyZsd4cxU5_MvDMkoMGM88XrnMqG9rJk8IVRVymtxa7zbW7McVkz_Dr_m59vACxhxtbz0TLo2vqggFE3isyi9y6lxa9_8CwPbK3HA6sJk3eV4-Lho9_W7OvLK3IX0MEM-AFm6cUL78YOOww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c9cc90b41.mp4?token=gBP4MXURUgNtuS4Qgz8yNrgTErgAGtQDM0myejxpl37ZLzptfrXIUdr1yUDPgC10ml1FcnIM_yadqOy9ClUR0X2Mix8vPw_2QuLLv17lkCRiofE_oL5kaND3vSljhKP-cjqbkbYr2Rq8qtQWmQuiET61X-cL-b34Hwyf7EQip0MAIVQmELY_n2nzKzpl3ssyXFkEHW5YyZsd4cxU5_MvDMkoMGM88XrnMqG9rJk8IVRVymtxa7zbW7McVkz_Dr_m59vACxhxtbz0TLo2vqggFE3isyi9y6lxa9_8CwPbK3HA6sJk3eV4-Lho9_W7OvLK3IX0MEM-AFm6cUL78YOOww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعضی آدم‌ها موقع آهنگ گوش دادن تو ذهنشون سناریو می‌سازن؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/672493" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672491">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
عراق و آمریکا ۴۸ توافقنامه و یادداشت تفاهم اقتصادی امضا کردند
🔹
این توافقات شامل همکاری در بخش نفت و برق با شرکت‌های بزرگ بین‌المللی (مانند اکسون‌موبیل و شل)، راه‌اندازی خدمات استارلینک در عراق و احداث خط لوله انتقال نفت میان عراق و سوریه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/672491" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12c4ff35.mp4?token=Vurrh1_k47v3eJHTeV8oC6UtaYTiiF-Qgy4VNVRnfLJ0J07_vPuWd1MQd_WlDRScY9BIMF2SbTZpl8Jfi-Pzr3y0BjQmXFBn70x47sHzKGPfXde_eGotkM4MMV450qT-GW4uvkFDiCJb60hHbQ1Dmar8Ej5Imlj7-5_bYJ1Vl5LtarDtomfS4lNmzK8RKMqT9amqia9bfFIRCIz08F5HhjC_kSYtt62j9Yrk9IDsem_7f-fhXZ_fsPWdaR7ab7E8uIgNbeyYANlGcGVyO66q0K11qzqy3ARbi7FYhJQFLg35uPQ7Pus9FIpIfyhyEXp4Uk2Rdqhs0zdboTd2Kv44IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12c4ff35.mp4?token=Vurrh1_k47v3eJHTeV8oC6UtaYTiiF-Qgy4VNVRnfLJ0J07_vPuWd1MQd_WlDRScY9BIMF2SbTZpl8Jfi-Pzr3y0BjQmXFBn70x47sHzKGPfXde_eGotkM4MMV450qT-GW4uvkFDiCJb60hHbQ1Dmar8Ej5Imlj7-5_bYJ1Vl5LtarDtomfS4lNmzK8RKMqT9amqia9bfFIRCIz08F5HhjC_kSYtt62j9Yrk9IDsem_7f-fhXZ_fsPWdaR7ab7E8uIgNbeyYANlGcGVyO66q0K11qzqy3ARbi7FYhJQFLg35uPQ7Pus9FIpIfyhyEXp4Uk2Rdqhs0zdboTd2Kv44IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله دشمن آمریکایی به دو پل در جاده بندرعباس–حاجی‌آباد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/672489" target="_blank">📅 11:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672487">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971fac3a64.mp4?token=HxhrfgANYqqaoV4EstmYuht3KEx3QfFVw4PdZkWASvzxEIGX55fnT2vD0GC1EZKSObZMuQgpVZpMjJCO2moHJHHXa3SMwpBTbuaxrB_tRVN943fY2KsiAqCj3_W9EFBeZVawjyv3EoZlVy1QcLEesrH9Jg0a1-XAhfvCX1MBgxCMr6mHS88iaGsM2-U0LQIpMmmeDt9wfbaGPFAGLn24NuI7eUViEJ2f91ejokv87dDHKa3uqF55zdZaCOtZEe61mw5WeD8qLtvJgMLk8Y4VMTcBZRpCGwCxA3reB_Jmf9fKoT1r8PV0SOyaP3Z5ZhO6KOMBOvy5tvVK2jCJK1e8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971fac3a64.mp4?token=HxhrfgANYqqaoV4EstmYuht3KEx3QfFVw4PdZkWASvzxEIGX55fnT2vD0GC1EZKSObZMuQgpVZpMjJCO2moHJHHXa3SMwpBTbuaxrB_tRVN943fY2KsiAqCj3_W9EFBeZVawjyv3EoZlVy1QcLEesrH9Jg0a1-XAhfvCX1MBgxCMr6mHS88iaGsM2-U0LQIpMmmeDt9wfbaGPFAGLn24NuI7eUViEJ2f91ejokv87dDHKa3uqF55zdZaCOtZEe61mw5WeD8qLtvJgMLk8Y4VMTcBZRpCGwCxA3reB_Jmf9fKoT1r8PV0SOyaP3Z5ZhO6KOMBOvy5tvVK2jCJK1e8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت پرونده خاندان پهلوی و عوامل اینترنشنال
سخنگوه قوه قضاییه:
🔹
با اعلام جرم دادستانی کل کشور پرونده علیه رضا پهلوی و تعدادی مزدور دیگر تشکیل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/672487" target="_blank">📅 11:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672486">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c62b1093e.mp4?token=c2z6ykJ0PatR4WDXcpQks06o_AYhlo5e0T6AikrpKcuPtGLcV8yOrzYE5c9jBWURJSpYh4Z-5E64p3cCaapwXKKhWD7nBOwg8QQhEIIcvpqw4Z-TiUJGf9jiENHD95lwbj9zWvvanqzCrziCjLEq5TkLIoGIGxWj4yKZkoU6fHqRK1-OVnjZyYwwv8ucuS7EXV5M4VT8GHLoUDlwqVRZifLrxSWtuEJiOzk5z1XngeLsdlRE41vrguJvvhBLzNOfHJY4mz7QMX05HMFjo__-nW_CKva8KWog5rOyT1Xp2IknV_4T2-TaugIuI9V2Fx57ImsLAYa1ek1skaPbPl9A9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c62b1093e.mp4?token=c2z6ykJ0PatR4WDXcpQks06o_AYhlo5e0T6AikrpKcuPtGLcV8yOrzYE5c9jBWURJSpYh4Z-5E64p3cCaapwXKKhWD7nBOwg8QQhEIIcvpqw4Z-TiUJGf9jiENHD95lwbj9zWvvanqzCrziCjLEq5TkLIoGIGxWj4yKZkoU6fHqRK1-OVnjZyYwwv8ucuS7EXV5M4VT8GHLoUDlwqVRZifLrxSWtuEJiOzk5z1XngeLsdlRE41vrguJvvhBLzNOfHJY4mz7QMX05HMFjo__-nW_CKva8KWog5rOyT1Xp2IknV_4T2-TaugIuI9V2Fx57ImsLAYa1ek1skaPbPl9A9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بی دلیل نیست که بعضی‌ها اینقدر از پله برقی وحشت دارند
👠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/672486" target="_blank">📅 11:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672485">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cceeebfe.mp4?token=ErRpcPFxn5cji0Obd9gJWJwLut7EGrrhw_EfPwcgRldjQxUNcwldlgNAR0evTqfT28uB-9iTmbgjKJYvHU-EtZCvTc31Xxa_PccnZZdyyNeoKk4WkRJSXFwa96USMnQ2FwAdefEnLSOPAYGT-s5Ms7axlw6xlioUbEWyeCZduFJIGv5FC3XxjZF_uLSn3K3f3HiDFsSS73-xGnkG3W1DHhLoQKVShnZiOQOc0mKaRvjz-0Sx-oz6br8EPRsVLlFtLRisvDyCN3Y7kkwFRDqtEIpDHo-MLIxSPS19gYyDQ8FjdehMbRBVG5uyNQt5q7cRqNgPwSNd-lMBVCvEtzi8XbGTI2zMOxuOxQuRbFOSQvIntjjZChvx0UPyaQp6iKo-dEL6VeTNjw3O7wBcnDjaNtaTmLitwILeE6xvRwkTLdjQGzqsHt6acD2kgR_Wnwhw0c0bdXS1IeV4BOf2kpZmu00R_LsesVYNvsyuR7no7s-piENu4ZlML_KSwWB86FAC5AuaNLUeUhDOIBYIHW3Nhb_Bjw3T183I1ziXxzS5F2mk97q7CL8fABVxRuqQJXFNAIFSlLT5f_YcZQULl7bN2Mv0QJ6kK6pgmrW-oNcUlwrzogCrcsw2sXTirh2RbOL1PKNeHGL8IvSqtEItVcYB4SwogYBBolU86B2599-r3Os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cceeebfe.mp4?token=ErRpcPFxn5cji0Obd9gJWJwLut7EGrrhw_EfPwcgRldjQxUNcwldlgNAR0evTqfT28uB-9iTmbgjKJYvHU-EtZCvTc31Xxa_PccnZZdyyNeoKk4WkRJSXFwa96USMnQ2FwAdefEnLSOPAYGT-s5Ms7axlw6xlioUbEWyeCZduFJIGv5FC3XxjZF_uLSn3K3f3HiDFsSS73-xGnkG3W1DHhLoQKVShnZiOQOc0mKaRvjz-0Sx-oz6br8EPRsVLlFtLRisvDyCN3Y7kkwFRDqtEIpDHo-MLIxSPS19gYyDQ8FjdehMbRBVG5uyNQt5q7cRqNgPwSNd-lMBVCvEtzi8XbGTI2zMOxuOxQuRbFOSQvIntjjZChvx0UPyaQp6iKo-dEL6VeTNjw3O7wBcnDjaNtaTmLitwILeE6xvRwkTLdjQGzqsHt6acD2kgR_Wnwhw0c0bdXS1IeV4BOf2kpZmu00R_LsesVYNvsyuR7no7s-piENu4ZlML_KSwWB86FAC5AuaNLUeUhDOIBYIHW3Nhb_Bjw3T183I1ziXxzS5F2mk97q7CL8fABVxRuqQJXFNAIFSlLT5f_YcZQULl7bN2Mv0QJ6kK6pgmrW-oNcUlwrzogCrcsw2sXTirh2RbOL1PKNeHGL8IvSqtEItVcYB4SwogYBBolU86B2599-r3Os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش جنجالی CNN از ویرانی پایگاه‌های آمریکایی از حملات کوبنده و دقیق ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/672485" target="_blank">📅 11:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672480">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اطلاعیه شماره ۲۸
♦️
روابط عمومی سپاه پاسداران انقلاب اسلامی: اسکله پشتیبانی سوخت ناوگان آمریکا، محل تجمع پرنده‌های جنگی دشمن، مرکز داده‌های اطلاعاتی دشمن، یک مرکز سیگنالی و مخابراتی آمریکا درهم کوبیده شدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/672480" target="_blank">📅 11:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672479">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
اخطار به نانوایی‌ها؛ نرخنامه حتماً در معرض دید مردم باشد
🔹
مردم هنگام پرداخت کارتی دقت کنند که تعداد نان ثبت‌شده در دستگاه، دقیقاً برابر با تعداد نان خریداری‌شده باشد.
🔹
سامانه ۱۳۵ تعزیرات و تلفن ۱۲۴ وزارت صمت آماده دریافت گزارش تخلفات مردمی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/672479" target="_blank">📅 11:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672477">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ-Coh-o6FT1NAVA1ImsxMDjLzM2ofGjbYbBjgjTtCxWCX3ZLBj_hF8S-SVU1Kxg_xLzLNGq4S3G52ooQvtT376BVgYPcvAjrvygAt8jeoT7LG-Yxo16_315j7Sn1T4DvQd9loiTGdwOdZJSdYN9Ymea_5zsL523zLiJae1PQM6e8PVewiTWWsoldmSMjRGjlu3P1INtDttQXtroIXUEjpw4IQ4SzNJj8L3vP0sT-Mz8g1-9pLNfQ8FHhl8Ntprm68IXWgsG52ptF9npIf_ssYFU5N3TV_Bv62PjKvf5mDb1xD434oYpKrKVJ-bzYJurmlHQzPRn7FX3eIOKWzdlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf4c412ca.mp4?token=W6hGM5h8q1zjXQ_26g-UdlVZ6ZDTf_R2cSmQDWQGuyY9Bmo_IE8Q_r1_CkB9Wxt1mmvy5TC2C4Qm_hPh_I1LbZLE9uJIV91v4fOO4mBXIFBk1tFEzBykf3SJcszvmiURJKoJJ5fl4rY51ia0HG7BK4XhAGerdMniu2X6qHcV-y114_Gf3oNCR9pltLwaA7MIML9B--oHwrx9Hv8b9FN4tGqR9iKc1VW_BjzkpNrEy_lBnhCslwagaM1M1pMYZKocudk7JbM1Zbl_pOpMmMDEQLtQp2HxAcXT3iiI4nqtt3vJ2begteHuaJS8YBqk_jiZezptYhCmjGwDc0sZGtISFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf4c412ca.mp4?token=W6hGM5h8q1zjXQ_26g-UdlVZ6ZDTf_R2cSmQDWQGuyY9Bmo_IE8Q_r1_CkB9Wxt1mmvy5TC2C4Qm_hPh_I1LbZLE9uJIV91v4fOO4mBXIFBk1tFEzBykf3SJcszvmiURJKoJJ5fl4rY51ia0HG7BK4XhAGerdMniu2X6qHcV-y114_Gf3oNCR9pltLwaA7MIML9B--oHwrx9Hv8b9FN4tGqR9iKc1VW_BjzkpNrEy_lBnhCslwagaM1M1pMYZKocudk7JbM1Zbl_pOpMmMDEQLtQp2HxAcXT3iiI4nqtt3vJ2begteHuaJS8YBqk_jiZezptYhCmjGwDc0sZGtISFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادهای اوکراینی به بزرگ‌ترین مرکز خرده‌فروشی تجارت الکترونیک روسیه، در  مسکو حمله کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/672477" target="_blank">📅 11:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672476">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/X6f2jgFCraIAzrHuQLpBKarEXtemcK9-JND2tYKMuWmwYTgikEr1GLAjhRHLXAOZyPGrEUkZgfOTtUS_fBHPwuu1flVNFZIPnTv0RF79LZQcjv38AFjytdcJ_A3rZRVAAUYoPkXFaWOPwXqReWU5Uk20PRr0mafOqkoRfPbEpVD6hv5hDnq9NF1gx85ioStvdihIkwolaOBlgA3t2xrTKDgQ7Ysrj5WFoZe53kH0dsPdjqm_KLbhkMvxJDkdhSR6-QFlFMrXLLJz0_JYbx1SoMVWMBaCTL_GnLtSLiEUUmxJyFQkiRh0KlQdl_6GN5omHse16GwaIylbHXObMgIsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با افزایش چشمگیر تمام شاخص‌های عملیاتی: ‌فغدیر از ۳۸۰۰ میلیارد سود دوره جاری ۳۲۰۰ میلیارد سود توزیع کرد
‌
🔹
احمد صادقیان مدیرعامل شرکت آهن و فولاد غدیر ایرانیان در مجمع عمومی عادی سالیانه این شرکت از ۸۱ درصد رشد سود عملیاتی و ۴۵ درصد رشد سود خالص در این شرکت خبر داد و افزود: در سال ۱۴۰۴ فغدیر رتبه اول فروش و رتبه دوم قیمت آهن اسفنجی در بورس کالا را کسب کرده است.
🔹
صادقیان افزود با ۳۶ درصد افزایش در تولید آهن اسفنجی و ۵۲ درصد افزایش در فروش آن، این شرکت در تمام شاخص‌های عملکردی و بهره‌وری رشدی چشمگیر را پشت سر گذاشته است، همچنین گندله‌سازی این شرکت علی رغم محدودیت‌ها و طی کردن مراحل راه‌اندازی حدود دو میلیون تن تولید داشته است.
🔹
به گفته مدیرعامل فغدیر حاشیه سود عملیاتی این شرکت در سال مالی گذشته ۲۰ درصد بوده است در حالی که بر اساس داده های کدال میانگین این شاخص در‌ شرکت‌های مشابه بورسی ۱۲/۸ درصد بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/672476" target="_blank">📅 11:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672473">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3e9f4994.mp4?token=oExv7ZJlTVR9AZe3gEbZLryICABsFEucWCyt63ggyCkrmXnp-vLYrhE8AfEmY3cdoO0dYLeYim2kSoSecSnO7K_Ynd6I-SAykj4O-zE8PlQE5B3PQklwikA2xSzf7tJgvzpH-4i1qkBxKt6ivWBAL3bX2T3PrraDWC0CN8iDEFJx8uVs1oVWjN-ccMMR8zaCdKC76A8tW5xv0dlKk1U1GPa6drwbFsIxWMaUAXDH7UN52pyPfgx7JgZcLDaocni_flEU4daqu94B30h3rmXiO_AeJu2RcbAh0J1YghdNQKJ6bj-phKtTWoK4_UsQtCfxbGChBGZp_IUjzTkh6cZ4sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3e9f4994.mp4?token=oExv7ZJlTVR9AZe3gEbZLryICABsFEucWCyt63ggyCkrmXnp-vLYrhE8AfEmY3cdoO0dYLeYim2kSoSecSnO7K_Ynd6I-SAykj4O-zE8PlQE5B3PQklwikA2xSzf7tJgvzpH-4i1qkBxKt6ivWBAL3bX2T3PrraDWC0CN8iDEFJx8uVs1oVWjN-ccMMR8zaCdKC76A8tW5xv0dlKk1U1GPa6drwbFsIxWMaUAXDH7UN52pyPfgx7JgZcLDaocni_flEU4daqu94B30h3rmXiO_AeJu2RcbAh0J1YghdNQKJ6bj-phKtTWoK4_UsQtCfxbGChBGZp_IUjzTkh6cZ4sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک پایگاه آمریکا در کویت، همچنان در آتش می‌سوزد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/672473" target="_blank">📅 11:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672472">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فیاضی، نماینده مجلس: وزرای کار و آموزش و پرورش اولویت بیشتری برای استیضاح دارند
عبدالوحید فیاضی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
در پاسخ به خبر منتشر شده در فضای مجازی مبنی بر استیضاح وزیر آموزش و پرورش، کمیسیون آموزش جلسه‌ای در این باره برگزار نکرده و من در جریان قطعی بودن آن نیستم، هرچند احتمال آن وجود دارد.
🔹
پیش از این، استیضاح وزیر نیرو در دستور کار مجلس بود و استیضاح وزرای صمت و جهاد کشاورزی نیز مطرح شده، اما به نظر می‌رسد در حال حاضر وزیران کار و آموزش و پرورش اولویت بیشتری برای استیضاح پیدا کرده‌اند.
@TV_Fori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/672472" target="_blank">📅 11:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672469">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSl6UJC529s36wYAZ-NaBy6dUiPU3ryUA7QoTuSiiw9Cgx255Va_7wtoaEDDLuvlGKshhIgaMR8KAIDj9_KP7pSKZNaXN4sRq1T9fAN2etRvJV8hci7DGY0KyBjgcm_scU1OFZOAfP9bHBRzWPRRyD_geUJf2Rhz4kz9u7vkMN9pLeMqODSVb9qI_SOQyqyVGecX6QBMF4yRC05KO1w4EERURaEv-sEwPgDKQyvUpzBrMy6CKVtKpVvT4oXCK7jLvYZhB1riuwt2ERGBOkzli3Mzzi9APwOkiSOa-4EoAkEpWBpcRROY5t-JIt9nTYtqWH_8lmb9kZePtmQllQR6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منع ستاره اسپانیایی از ورود به آمریکا به خاطر سفر به ایران
🔹
کاپدویلا اعلام کرد درخواست مجوز سفرش به آمریکا (ESTA) به دلیل سفرش به ایران در سال ۲۰۱۶ برای یک مسابقه رسمی رد شده و به همین دلیل نمی‌تواند همراه فرزندانش به تماشای فینال برود./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/672469" target="_blank">📅 10:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45cfabfdd6.mp4?token=MZC39RoLt7ZwYYpV3XYlTREAV1P8HC75pgoFB8AcDCd6LK0z9PVHvqPDH-kFp9Z7XlNGPRRQqBkK9piT3FsTQqnowSN6c1-HjE6a_C_UGu6vPKj_-zJZRrcd62xygckXdl4ewkoVTtLcxkNulfDpbw2DjSHNgG7upGsLtpztIZTrfyYvE01UtGUQC98rJlia5a5rJqIf6gC_jKOdWmSnYSqV1Vb080v0FGsaeoZi0JB7-n1LBBa370FqnEoyQ2Pu1gKri08j_Y-8cizRtMwg2QvGigKrdN1kKdJz73MAKlrqXOMvBaOdG2zyJ-iNcZdC_6aQcpa2l0g4wz2W_h1SMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45cfabfdd6.mp4?token=MZC39RoLt7ZwYYpV3XYlTREAV1P8HC75pgoFB8AcDCd6LK0z9PVHvqPDH-kFp9Z7XlNGPRRQqBkK9piT3FsTQqnowSN6c1-HjE6a_C_UGu6vPKj_-zJZRrcd62xygckXdl4ewkoVTtLcxkNulfDpbw2DjSHNgG7upGsLtpztIZTrfyYvE01UtGUQC98rJlia5a5rJqIf6gC_jKOdWmSnYSqV1Vb080v0FGsaeoZi0JB7-n1LBBa370FqnEoyQ2Pu1gKri08j_Y-8cizRtMwg2QvGigKrdN1kKdJz73MAKlrqXOMvBaOdG2zyJ-iNcZdC_6aQcpa2l0g4wz2W_h1SMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موسسهٔ تحلیلی در بخش نفت‌وگاز: تنها مسیر فعال در تنگهٔ هرمز مسیر ایران است
اچ‌اف‌آر:
🔹
به‌وضوح مشخص است که آمریکا نمی‌تواند کنترل تنگهٔ هرمز را به ایران واگذار کند زیرا در آن‌صورت ایران به قدرتمندترین بازیگر نفت جهان تبدیل خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/672466" target="_blank">📅 10:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98aacbd36.mp4?token=Gz3dwO7f_O4c4YmzusEYqxsuEap4gr1U9SEzgh16Pr2wG2q8MVuWd2AjmSt2vPCBFAd_q67daDCQcUJmatgf3zm3vx-JTZSVL-zhq3BKZbblP54Uhw5CIUQMZAYk-MJTEsbzek_lKCavIAjvfueynneZ2T4Db6sD0UrN8zpBP_7_LbPASvYnDAS9RTQKexaeii921dmKVHlfxdCu3c3xVKk4YIYuUAwEl3NZZGVu_ltAXuRjzhCGkXxyxmMQW_1Bk-xoWZ3bPzlhHrIHMpJ1GTm4SS_AkTUnj86tZSrWUA5xPMAzD3Uct4c85eVJaxmbq67B6bkJ6DnrUQ9d8bvXA3FkLq4oCIbIeyrVYiZWLdzfr8pq1PqdBrGbxw3vZ7ZtMGS0mkKJWGeL82FuUTK8rCJfFz9aOg9fWIfHgwpIaKOXPOaK_YdEfIx8dAOwyI557WbDlDZSxczCByAf54mpjzeZkcbvQcGLTavERbt_Ds4zeTUZDbjRbstSARE_obPrvl9nfgsAmHrvm6AmHfwdzfvgSpbD7AE1cdMpV9VgtZ3DOTOrCEY4WQizBsgJe30XywLJKq4jy5JlGDAvzN9DU0vGoEfEyYwTRXobl3IJeXJvOz_wHi4Nuyun2M5txck7tKpJD95xgXrXZqDY5Gc37f_Zmq8JAzWEn6Nr6H7wpV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98aacbd36.mp4?token=Gz3dwO7f_O4c4YmzusEYqxsuEap4gr1U9SEzgh16Pr2wG2q8MVuWd2AjmSt2vPCBFAd_q67daDCQcUJmatgf3zm3vx-JTZSVL-zhq3BKZbblP54Uhw5CIUQMZAYk-MJTEsbzek_lKCavIAjvfueynneZ2T4Db6sD0UrN8zpBP_7_LbPASvYnDAS9RTQKexaeii921dmKVHlfxdCu3c3xVKk4YIYuUAwEl3NZZGVu_ltAXuRjzhCGkXxyxmMQW_1Bk-xoWZ3bPzlhHrIHMpJ1GTm4SS_AkTUnj86tZSrWUA5xPMAzD3Uct4c85eVJaxmbq67B6bkJ6DnrUQ9d8bvXA3FkLq4oCIbIeyrVYiZWLdzfr8pq1PqdBrGbxw3vZ7ZtMGS0mkKJWGeL82FuUTK8rCJfFz9aOg9fWIfHgwpIaKOXPOaK_YdEfIx8dAOwyI557WbDlDZSxczCByAf54mpjzeZkcbvQcGLTavERbt_Ds4zeTUZDbjRbstSARE_obPrvl9nfgsAmHrvm6AmHfwdzfvgSpbD7AE1cdMpV9VgtZ3DOTOrCEY4WQizBsgJe30XywLJKq4jy5JlGDAvzN9DU0vGoEfEyYwTRXobl3IJeXJvOz_wHi4Nuyun2M5txck7tKpJD95xgXrXZqDY5Gc37f_Zmq8JAzWEn6Nr6H7wpV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت آسیب دیدگی تونل شهید میرزایی «گلوگاه»
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/672462" target="_blank">📅 10:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daRZBoVMHPKvJ40bHLYoV1pSqBSRpXQci1Q110rXobLIwT1wpxIhPvqNZZVYbdLhmgAOnZldXu8cflz2ZPhx-kSYO1vgnswXO97rz9SAstxEoWCPK6BueI-35VzFwcEJ4aHjtWgdpJHryF5BFMfeIVsE31QAKjsXNlwzVlvLIVsEnRl9iEljaEPptgzPPJJrjLFIr9RJ1JDSa9QBMgVTaGWWaJH66zklIEYxMw1ryZ5Z41A5TKopHAIICkpPzE93HhwIAQDeHWy8k2NTtzEAoTqaMEWLN306MpsRF43oyQajyYmn5dgVLDlONLjIg3M1Oak7g3kUWLgxmr5putsb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ اشتباه رایج در مسواک زدن
همین اشتباه‌های ساده، لبخندتان را از بین می‌برند!
🪥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/672460" target="_blank">📅 10:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672458">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEB0F2Mv74IrE2bbXJLX9KZEJa1dGtH0Ulev_A8jGKclLb3iV_AkAlFKiifQhDqJ8o_QX4yE2EgsNZgFQMD6fR06VG4qvLaku7YoYWOZlkfr2tDdkBxoTqPNgGmgEvIW8w21zIPot4vjHs4WRoIg2yQNXw_sNPch8MDDAylITpofqR2-yndRelCPGFCf_GCf-0Uii6dI1F6G6xiDP2GKyaBEuRyUn4f2n_hyiPSgdhczGiUTE0d4YzICNtUNmGfjcNtLBHPugYV42YGKKO8fBbAsR1MzAjEk65uvsBDZEP3aIC9Upk_2YsZFNF99ymdXmYGQBtzTT72n9JWUdSfXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/672458" target="_blank">📅 10:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672457">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTZdCae-ql7McKY8ls4XfgTN1_WY_NSQhcGPU-AFbrCjCvuCV5Dsj5q-azJ92xVupYKF5v-67aO5LM1dn1pyu1pnyb60CHUuYGMcEhvlCqjIqDd3ZHr8MP9R3MoOoaeZGk_nSAooYT6VeLoVThClxWvDp7u46GJkoLrqwgYJwKbiacLH2KjEhG1f3_8cCxOvghQ-7VARUu1TZ2T8fwx-DzA-XHi3ESp1BWLz-Lc9TE5bUXqEFHIQMmeD6wuROpdTrpJnahcyeAYarVZby3s5w7ks8e5eBpogHhM7gYB9NLPEvwQtzHg_PhwYtAGcWtHoCwkgGynlh_fEJs-gEYJNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل در اقدامی هماهنگ با ارتش تروریستی آمریکا، تصاویر ماهواره‌ای مراکز حساس کویت را محو کرد!
🔹
گوگل تصاویر ماهواره‌ای با وضوح بالای نیروگاه برق الشعیبه، تأسیسات آب‌شیرین‌کن الشعیبه، چند پالایشگاه و مجتمع پتروشیمی و همچنین بندر الشعیبه در کویت را محو کرده است.
🔹
این تأسیسات در هفته‌های گذشته هدف حملات ایران قرار گرفته بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/672457" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672456">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d419140269.mp4?token=SU65-liw0weIsDKu9I6BaLRMZRM3_LZq0VDtMFIe9ACaO9Hrjj5eC9tC5a6VnjhkSdXlQrcIi7RxrJNR2_JHwcFMdOkYd92toOhtFtwysX93dsHrdOK6VOarABoTceIENCIqz0yJn4y2jSE_HZL81vuAXbmF16Tmwe_BSlKtMYXSZ_mnylJ5a0kOrvZB-tndr9tWU3mjpYX_K18eNsijXsUD9SK5LVlBWJvD6sinKjW0ANtDD-pdb5bU1MaMTW_30mE0rTNjVpBbhNEGsqsiYOgfUHwhtroa6rOC_0gkyXVzrmCMEFfnZqItXWuacArKE4cktkWarnUI5MR9LTdEC7PElmLabLvfnPBncVnMazp6YrZu57N_4y2n_hH1xPDlX1d5HoxvuifTnqht5kiEggGYkEdgacxDMQJBWBKQV2UmhVoKFPnfjvcJX6vLQuzMB43BULcr4plr8jJhGrd_bZG56kfOuM0GmqtEkQI7xrRj0TDLTS-7p4v_T4Uj6I5HHbetxKin5k5Ht0GC0FFfao7ChaJlr9RdfZiEigsrtFfhKMDX5ZDW34cRV-Ur4ftaul0nns-6atZn3cU0RxTcLlSIQhzt0ZagStafhKX_yccM2i73utjIFeLbxNKox7hwgwzS13xVq9HIwQa0MkerZyQcT7cIv8XDnjqZe5aXKjs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d419140269.mp4?token=SU65-liw0weIsDKu9I6BaLRMZRM3_LZq0VDtMFIe9ACaO9Hrjj5eC9tC5a6VnjhkSdXlQrcIi7RxrJNR2_JHwcFMdOkYd92toOhtFtwysX93dsHrdOK6VOarABoTceIENCIqz0yJn4y2jSE_HZL81vuAXbmF16Tmwe_BSlKtMYXSZ_mnylJ5a0kOrvZB-tndr9tWU3mjpYX_K18eNsijXsUD9SK5LVlBWJvD6sinKjW0ANtDD-pdb5bU1MaMTW_30mE0rTNjVpBbhNEGsqsiYOgfUHwhtroa6rOC_0gkyXVzrmCMEFfnZqItXWuacArKE4cktkWarnUI5MR9LTdEC7PElmLabLvfnPBncVnMazp6YrZu57N_4y2n_hH1xPDlX1d5HoxvuifTnqht5kiEggGYkEdgacxDMQJBWBKQV2UmhVoKFPnfjvcJX6vLQuzMB43BULcr4plr8jJhGrd_bZG56kfOuM0GmqtEkQI7xrRj0TDLTS-7p4v_T4Uj6I5HHbetxKin5k5Ht0GC0FFfao7ChaJlr9RdfZiEigsrtFfhKMDX5ZDW34cRV-Ur4ftaul0nns-6atZn3cU0RxTcLlSIQhzt0ZagStafhKX_yccM2i73utjIFeLbxNKox7hwgwzS13xVq9HIwQa0MkerZyQcT7cIv8XDnjqZe5aXKjs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پل‌های غرب استان هرمزگان که مورد حمله ارتش آمریکا قرار گرفت
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/672456" target="_blank">📅 10:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672455">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxQdGkrHF5uThoqEPyTlJ-Ov8Lr_hEG4zSjKvDGrjzgWDmFlNxmdAZJ0heJPJP3gDr9qKT3HImD2XV_QWghCSf_8HUKNqJpY8eWe_FPERMpXMWoQAX-lulFwpi3bwm1n0aKEpLqn618LQ8uO3i7tOKW3m9PrDBifQeeTz_taXrXYyALVpmmny7wIu9qfEy-wET54bbuGMC1IjXrC8wlQDM-4o92xXE4W2fCzlKJA7eR1gehcx6jYYE2RKujbeog8QGDF5hRKsW0rZT1hoWBZBNWuKC7_20bvW4v6_mMdHnhIMvzPZtcP8EEC0low2aP75jF0QGO36FUn06Mi4POxAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این‌بار پاستا رو به سبک انیمیشن باد برمی‌خیزد درست کن
🍝
مواد لازم:
🔹
اسپاگتی ۲۰۰گرم
🔹
گوجه‌فرنگی ۴عدد
🔹
سیر ۲حبه
🔹
روغن زیتون ۲قاشق غذاخوری
🔹
ریحان تازه
🔹
نمک و فلفل به مقدار لازم
🔹
پنیر پارمزان اختیاری
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/672455" target="_blank">📅 10:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672453">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای کویت درباره حمله ایران به نیروگاه و تأسیسات آب شیرین‌کن
🔹
کویت مدعی شد در جریان حملات موشکی ایران، یک  نیروگاه و تأسیسات آب شیرین‌کُن این کشور به شدت آسیب دیده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/672453" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672449">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYH8ElMt-L4XzSFoBDxWUfaciyyL8_nNTyvoCQe21XkZ-F6_tlibE1haVMhB5Don8Axc7aY1RjdGuEBAwJ2DBaz-gXSNdGbVERKCSZYAEDI1eKKl0i1BaFZ1CsLl_IdtDXOhRNgjd2F-BS12IACdZ0Us84yQdxUCRuMLsD5o-HAdybIyordQnLVE9grbLR7PSszSYK_ysUo6RzRjEOtWBNGo0drynkg1uEwnCU6iI4O9XE1EadhB5y51gXxXFmtauAehb99s4pJl69k7yH6exqu1Rb9qG1DngrqfTY9nwCXEqJjylTcLig_D2PJkpzSu9FVz7-GjiGKQx-da8m3xvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqe8wEzIfJDXmYuJjGzrf5PRZ4J5GzjwyYPuo9GctDoLH4L_6j55uM8uYUexpvpKScSLC1Zzf1-howf5rPljJO8kifEI9vt9n41Hi4VmGVQrHR1dZZ6N3hOM5r96SCJDtUS1WXE6e8GMHygfTbfI20R3z5GR0OPvrYbMKkJV9OBK0ksFKO8JwWe1K9kTcOi8IL6fScxpvxWb9JXkNZ7Gce_AbFSBYn3uszNvPBiy7BASw9B9E-46SQynO6oL-j_RPiQyD5tQh80NglqwcyFMmM51Y0Owag7XqYzHrrTG4FAsmeCLDW4IdLrohSOAt09fLbzYqJ6ST3oywQNAid5FBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iL_Eucv_U36snKhhaK-9UsN9c0xLV0NhyE61ffaP8da_7kH8TqTQLHNrUqE0rT9iUHM473HnVLheL4gdO3gvIp5ku8EXI5bRQY4O8gubd6XjT7AUl2UNeCqIPoZ6-iPNYhDupndjmGwOlP7c3yH58cnH1JOLW2L68ZdZ2mRjcC9nkdK6QuVBmq9LCwEhcWgiGr-hxbFDbqlwrb4zODzQYKeipSW8bPkbtwUZYIkeJftksghcuSUbMW6SmrqtmBe4wU7E0vjnDIeJBO7vwxhyR5gqwDthnQHV-9DUJx23VQA_vFoUlNAKRe6jWFnnM9P-r2BAJTqgWTckPu-QaoB_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XR-azpkJQxqz_FEbridrWfNuQ6S95fdaacRDn9xjSHxAii36kW3XqIMkOzc_RGP30ZrK5_mtIZMgfMyE45qiDLsZOSnKIbhmvO9klZ8eNVG9FEvfsM5ly7F1MAYFnb4iaCq7r4XTOY12ArdTItyKksJb2wdIVhQTL7OYbniKMVjo6z2TqHOMi2bFvnh8bpsHnPXKQsVvmoTPs_P32IX13-UhmGlN10vNH4h5CCIiCCbZwX-XbNjQJmFZR6EKEKc9ApVp1gYYVtL4xUxnHxp_l6QDmgiQcecokwdBXitFXIt1q1SOjKcns_SgtbBmnCW7EhbLWaI6W1MQ4LOYL1x4Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمله جنایتکارانه آمریکا به آب‌شیرین‌کن بونجی جاسک/ ۲۰ روستای ۱۰ هزار نفری بی‌آب شد  مدیرعامل شرکت آب و فاضلاب هرمزگان:
🔹
آمریکا در حمله تروریستی به آب‌شیرین‌کن بونجی در غرب جاسک، ایستگاه پمپاژ و ترانس برق آن را تخریب کرد. این تأسیسات روزانه ۳۱۵۰ مترمکعب آب…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/672449" target="_blank">📅 09:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672445">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2139743d15.mp4?token=RuJq0WJlElAvb5NLKqSZCYyVRZ8sDZss5VelnQ2xliUNnd9N2QqJHa-s_RQulzkqYW7vGdBa2ijKceN8hnUfO-92FpGaqA6dxn0yThxR8KPucwop1QJYdn6MKYpwL5hjijRW6Q7hHgcgzUT_ZyIPLuyRx_ue7_3-oRnYCwLt08Dymiz6dTIE17end7mxhuXs7SM2tkWfgd8rJqHsfjHjLY5vWVE1wFeweua6wNMjg21vAniVBrYgHEQbURqwo7EtdAhwWNBNeP-qJzYBc4DXkN666aeEpVeh0fTQqxxk8rIw4zHfN6LrF_3nFXfqJtk2it5TEZeufWBagJgyHdko6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2139743d15.mp4?token=RuJq0WJlElAvb5NLKqSZCYyVRZ8sDZss5VelnQ2xliUNnd9N2QqJHa-s_RQulzkqYW7vGdBa2ijKceN8hnUfO-92FpGaqA6dxn0yThxR8KPucwop1QJYdn6MKYpwL5hjijRW6Q7hHgcgzUT_ZyIPLuyRx_ue7_3-oRnYCwLt08Dymiz6dTIE17end7mxhuXs7SM2tkWfgd8rJqHsfjHjLY5vWVE1wFeweua6wNMjg21vAniVBrYgHEQbURqwo7EtdAhwWNBNeP-qJzYBc4DXkN666aeEpVeh0fTQqxxk8rIw4zHfN6LrF_3nFXfqJtk2it5TEZeufWBagJgyHdko6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تقابل تاریخی در فینال؛ مسی و یامال: از قاب سال ۲۰۰۷ تا رویارویی در جام جهانی ۲۰۲۶
🔹
سال ۲۰۰۷، خانواده لامین یامال در یک قرعه‌کشی خیریه یونیسف برنده شدند تا نوزاد ۵ ماهه‌شان برای یک تقویم خیریه با مسیِ ۲۰ ساله عکس بگیرد.
🔹
۱۹ سال بعد، آن نوزاد و مسی، حالا به…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/672445" target="_blank">📅 09:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672444">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
دود بسیار غلیظ از کویت به دلیل اصابت موشک‌های ایرانی
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/672444" target="_blank">📅 09:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672441">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b204f4e610.mp4?token=ufdBDeuF15nqp79nk8Km5hkb3guIcG2ia1qN1fimMqFDK10C9sLepC4PrUpHGAWd8gMeVOfgBC7bdNEyPnOJETQImeuMRZs2dDYXCZex3SUg82Nksm4NyFhEv8Hcfcja23rrKmCVCV3yNnRHcpb8gm_85nI86w9PYnMkR3tgZmIUDWmfX72e7rRbMvKlYIS0_8HeyIEMqIsNrPMd8MrKyZj70Qc6kQFKpfaSjcreQgAYxFAy_LX3ohkBcjohBJ_EMZw39CaIMiFmo_Gq5HWPYCLykrfWMr7EmpmClcWAL8JxRIk_1UN0W13PRkDHv1GJSFpqoEb1UvWdHWmLFDbU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b204f4e610.mp4?token=ufdBDeuF15nqp79nk8Km5hkb3guIcG2ia1qN1fimMqFDK10C9sLepC4PrUpHGAWd8gMeVOfgBC7bdNEyPnOJETQImeuMRZs2dDYXCZex3SUg82Nksm4NyFhEv8Hcfcja23rrKmCVCV3yNnRHcpb8gm_85nI86w9PYnMkR3tgZmIUDWmfX72e7rRbMvKlYIS0_8HeyIEMqIsNrPMd8MrKyZj70Qc6kQFKpfaSjcreQgAYxFAy_LX3ohkBcjohBJ_EMZw39CaIMiFmo_Gq5HWPYCLykrfWMr7EmpmClcWAL8JxRIk_1UN0W13PRkDHv1GJSFpqoEb1UvWdHWmLFDbU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود بسیار غلیظ از کویت به دلیل اصابت موشک‌های ایرانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/672441" target="_blank">📅 09:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672438">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/257aca5779.mp4?token=cj2bD-hW9fetgJrCuCRxqqU-RA6mhxjLeC0j-ZynGuDGnWgK01vqqAqq9gH6O-0J37L5K374RoqNQutmVD0aAzPsBpnhuGIEAWGoISjKOfQ-IXoB-bYdN79rTMWpthAzy2g3yzEb_t4oXUGjmDQ9XWNUsXntbzmLta6mOI0GtfTLH6_R2RshCYfxK2T3V5nbVF_agDau_3QTTD532-Dkelcfo5cSgvK3J7uZIWE7J2eK3oXHQ5K5GKkifFQZ-kYZGo-yHlk1QM39jekC16A6gCw1JXYZde3G0i5B_s5vtjhApq5NVhSA8PcrVL5I8vVst6yBnYl5SZhLgV8mcQB93g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/257aca5779.mp4?token=cj2bD-hW9fetgJrCuCRxqqU-RA6mhxjLeC0j-ZynGuDGnWgK01vqqAqq9gH6O-0J37L5K374RoqNQutmVD0aAzPsBpnhuGIEAWGoISjKOfQ-IXoB-bYdN79rTMWpthAzy2g3yzEb_t4oXUGjmDQ9XWNUsXntbzmLta6mOI0GtfTLH6_R2RshCYfxK2T3V5nbVF_agDau_3QTTD532-Dkelcfo5cSgvK3J7uZIWE7J2eK3oXHQ5K5GKkifFQZ-kYZGo-yHlk1QM39jekC16A6gCw1JXYZde3G0i5B_s5vtjhApq5NVhSA8PcrVL5I8vVst6yBnYl5SZhLgV8mcQB93g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو ادعایی سنتکام از برخی حملات متجاوزانه بامداد امروز خود به ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/672438" target="_blank">📅 09:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672436">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM-A4p06iTZpmGNchPvRBsK7BCFOlVJ27CzpPf7YO4BZuPk7Xo190Xff4FEZK95QQ4aCjJZCYX5IfHLofMwGKASxcTbiEnBbZk1c4kR1Dh1YYWIWkDkWgd5LRtVPyl26jADe7K9yaSE9CWXs_b-b_7w8A8nf6cAPD8rAHWKepmRSuDiEEOTCr_PSOKGtj52WzNjSFW8gK8jrWxdk0Srpx8KZudwT7eEqVqxJKnf9w8s86ureu-lKYCt9CFZCxTv9YBYl1wDWcT43ESQsVvHlgaXzG6A4Lfx7mEAlR5lRLLTZmci1cKyJkYctvuyPnF73uSOwmQPZemD6TVro40WSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعلیق فعالیت فرودگاه کویت
🔹
هواپیماها به دلیل تداوم حملات از ورود به حریم هوایی کویت اجتناب می کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/672436" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان: جنایت جنگی دیگر آمریکا این بار در جاسک  تأسیسات برق و پمپ‌های آب‌شیرین‌کن اسکله روستای بونجی هدف حملات موشکی قرار گرفت
🔹
بر اثر حمله به این تاسیسات آب شرب چندین روستا در غرب شهرستان جاسک قطع شده است  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/672434" target="_blank">📅 09:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672428">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cab861f1.mp4?token=Xfa6ZK17wQ6q1WHBEINSp7VbVi_Swxc4dKNRAYoiwEQ825ody73S-bF780zbokUKLUtq2PS-Fp9Nltdw3mD6kOhxuwLmgG1Lt_7ccusq3VzUikWaXGCCU8Yj1NC5fthfqgN8YU-0t-95IRWbsdMFmf-zn5HjSe4fELjDBG2RN81C6QIgciIqH8wyuwiogY3zBCAoknr4zU5Ce0tJW7XbV5qnyQzVo4nSFqZBWFjr4FrEYgNLo0ECDgWahZzvk1OvQ11-aaytFeKTMs4pFOAaBx0BAJOY-yZlYfren5zfTp330xyIHYG17adXAQcvTNn57hz8_Jx635wJrv0HvZC6Mw9DtT7a0CKi2KxH87vm-3RBuyW_GQ_SUp2aYvRYmWL2yJweemAnQyGsNR8gESaYxF9bR-BAJRuUMybl3stHWZrwqhWR7axmoUdwmBF2pWVegXMEPeGh-6gTlqyqj_K32XPgMs3FKnumSrJfXj5NsKyf4b2nGODC58HpFM_Ua40wZFsAPQfaaBlEamGPG6_lQDSeuzfhb_6759qHNPSJ8i3QteMAQlzobRUs5dsjftYRvAwOa7-gRcOeFu8c2OEtqSYMkksWVgqM76oprtu7V_BXxUFGtmaIQpf9VOFYQAdiz0RCqfGSTcG_AIYcccv2cHOR9g-4g6pRsVswHmr1RWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cab861f1.mp4?token=Xfa6ZK17wQ6q1WHBEINSp7VbVi_Swxc4dKNRAYoiwEQ825ody73S-bF780zbokUKLUtq2PS-Fp9Nltdw3mD6kOhxuwLmgG1Lt_7ccusq3VzUikWaXGCCU8Yj1NC5fthfqgN8YU-0t-95IRWbsdMFmf-zn5HjSe4fELjDBG2RN81C6QIgciIqH8wyuwiogY3zBCAoknr4zU5Ce0tJW7XbV5qnyQzVo4nSFqZBWFjr4FrEYgNLo0ECDgWahZzvk1OvQ11-aaytFeKTMs4pFOAaBx0BAJOY-yZlYfren5zfTp330xyIHYG17adXAQcvTNn57hz8_Jx635wJrv0HvZC6Mw9DtT7a0CKi2KxH87vm-3RBuyW_GQ_SUp2aYvRYmWL2yJweemAnQyGsNR8gESaYxF9bR-BAJRuUMybl3stHWZrwqhWR7axmoUdwmBF2pWVegXMEPeGh-6gTlqyqj_K32XPgMs3FKnumSrJfXj5NsKyf4b2nGODC58HpFM_Ua40wZFsAPQfaaBlEamGPG6_lQDSeuzfhb_6759qHNPSJ8i3QteMAQlzobRUs5dsjftYRvAwOa7-gRcOeFu8c2OEtqSYMkksWVgqM76oprtu7V_BXxUFGtmaIQpf9VOFYQAdiz0RCqfGSTcG_AIYcccv2cHOR9g-4g6pRsVswHmr1RWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل به طریقه گلاب ادامه دارد
🔹
فیلم دیده‌نشده‌ای از زیر قبه‌ی حرم مطهر حضرت عباس علیه‌السلام هنگام طواف و گلباران پیکر رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/672428" target="_blank">📅 08:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672425">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eo7LYL-DUC_eYX4JjLqdBx_cPNn86pstImCQ6eIMhdvVl2SHl-Ez4KJlwUewRZMNYU2F1IkXsiVAY0CSWbbnOY8wC_VtigtagFSS5XjXsr69ogyVCIP86t68Qucs4CFF5cuXqdKTmpjakqGBFDhnQSoU7NxSi8zsgRhAaFMBoROq1RtiI54el8X9ygtU9wvsGoebJ9zt0iZE_i2DdWWsJNJ8rdX8Ioesms7H2Ijm6JvONQ21hNqWeWSVZvWxVCzBYroKOSw_4Bl4SNY3kPX5Vz9XvLrw78EOB6ZJwt0lgqoEVxehjSG5etu6ixK4r8A-La_bcN8vGpwJ0pPh76vvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W9PBaRhSeb8V3YyfivLdzROnBd6lVn3ptRcjw5DBsMojejJZm-2lq1Z8XD-t5UIss9ufuWP_zoEAZiyL67S4AExFM6XXtpv2asPlw7xzwxp0Vr5EkHqRa3Y4zHgm_LdqQouNP4Wo1VkHhxNYF12D4QxfHwe8A6psf8IWttygiQY1X0fuuLJnHO8fPtfUq9cZ9rLqvljF3tKIEEpBbpo4Uu4GvoOJ8fdmiC2UiOJBAzJUDGk1E9lJOi7LVufGmklBoqKXH0JNgxNxscA-DJ3VlVYDE815ewwT2X-NVaw-lVMH98cZtAbCHBEUpvQie_-eOv-VPOD75SI9ocpPwYGdtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر ۳ تن از شهدای حمله آمریکا به پل بندر خمیر
🔹
این ۳ شهید اهل روستای نیمه‌کار بودند که درحال رفتن به منزل خویش روی پل به شهادت رسیدند.
🔹
در جریان این حملات ۸ نفر شهید و ۱۹ نفر مجروح شدند. #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/672425" target="_blank">📅 08:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672424">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اطلاعیه شماره ۲۸
♦️
روابط عمومی سپاه پاسداران انقلاب اسلامی: اسکله پشتیبانی سوخت ناوگان آمریکا، محل تجمع پرنده‌های جنگی دشمن، مرکز داده‌های اطلاعاتی دشمن، یک مرکز سیگنالی و مخابراتی آمریکا درهم کوبیده شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/672424" target="_blank">📅 08:34 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/HtnMrrJ1lQeqaBJfVORtEqAYD1FzMl5-eR46MYMvY2NoziFLXbZyteJ5aV3F6m7RWX99xkXjAlMzccdjhd3sOiNZmaSezJDjku012F-lBnqk216XSOWqECb-N8-6Fla_3b0ybkf1TksxBx_PzePtgo08ACORPe3bn-VRZ_99DqvuxbSRUUvrVM6bztzx-pev0a9VBcaSuIYYqbCIUHzrNeRpRfoHhnuxPwz4tuOhR11v1dMHOOSsvEtIfY61rcHxzjcLbMYhNH15tO0MaMjgoHDn74zhdts16ihTwN4W6G2TqZ4EpQ8MGocn-dKt1-hQjsVH65wLeCGQsnTbH6yUcQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.2M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 20:58:30</div>
<hr>

<div class="tg-post" id="msg-664676">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: هنوز وارد مرحلۀ مذاکره برای توافق نهایی نشده‌ایم
🔹
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آن‌هاست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/664676" target="_blank">📅 20:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664675">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه:  اولویت کنونی ایران، حصول اطمینان نسبت به اجرای مفاد یادداشت تفاهم است
🔹
در رابطه با تعهد آمریکا طبق بند ۱۰، یعنی فروش نفت، مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم.
🔹
در رابطه با بند ۱۱، یعنی آزادشدن دارایی‌های…</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/664675" target="_blank">📅 20:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664674">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه:  اولویت کنونی ایران، حصول اطمینان نسبت به اجرای مفاد یادداشت تفاهم است
🔹
در رابطه با تعهد آمریکا طبق بند ۱۰، یعنی فروش نفت، مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم.
🔹
در رابطه با بند ۱۱، یعنی آزادشدن دارایی‌های مسدودشده ایران، نیز فرآیند اجرایی‎‌شدن آن درحال پیگیری است.
🔹
در این چارچوب، همین هفته هیئتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/664674" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664673">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
معاون سیاسی نیروی دریایی سپاه طی سانحه رانندگی درگذشت
🔹
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان جان خود را از دست داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/664673" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664672">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ae4c4e4d.mp4?token=iMsGHXQdLAli6DUIQjoyMHvUVibO_Ppd5RHakcL7-6e6eAF17_k1rs0N7LcUUvElcYAFJ6G0LWS7ruGlRT0ia3RK_0vqUy6gC0zypRGs6y8B_II94jYBedwvIq2xLPsS_kPzV4-B_6IU4O3E0g2calr8eQGhJIcY4KREk_oaWqHX6aNVbThTwFlGkJKn2Yzs_jWjkSAFDWWsj2F5umpLaAoZyNaCYhBj-R4BbJqys7HOCmYV3lf1RrGhKycPKY3RfZ6Q52gqiISx1uDvqHl5HL95Is5694SwhGkTPews3XQT3SCm8BDTtjBCbcoZDnGJJBlIWpC5a_u3cxmMXLNfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ae4c4e4d.mp4?token=iMsGHXQdLAli6DUIQjoyMHvUVibO_Ppd5RHakcL7-6e6eAF17_k1rs0N7LcUUvElcYAFJ6G0LWS7ruGlRT0ia3RK_0vqUy6gC0zypRGs6y8B_II94jYBedwvIq2xLPsS_kPzV4-B_6IU4O3E0g2calr8eQGhJIcY4KREk_oaWqHX6aNVbThTwFlGkJKn2Yzs_jWjkSAFDWWsj2F5umpLaAoZyNaCYhBj-R4BbJqys7HOCmYV3lf1RrGhKycPKY3RfZ6Q52gqiISx1uDvqHl5HL95Is5694SwhGkTPews3XQT3SCm8BDTtjBCbcoZDnGJJBlIWpC5a_u3cxmMXLNfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار خرس از گربه که در شبکه‌های مجازی پر بازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/664672" target="_blank">📅 20:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664671">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
عضو رسانه‌ای تیم مذاکره‌کننده: تا الان هیچ مذاکرۀ هسته‌ای با آمریکا انجام نشده و تا عملی‌شدن شروط ایران هم مذاکره‌ای دربارۀ موضوعات هسته‌ای انجام نمی‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/664671" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664670">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyt4SePEYe7MGg34q5Ph_NkMLBj_uYwG1gT3UNUma7coYIZ6FjDywt7TJIC02peTljUn2j-ECC9JUUOThmKyEmG--HJ74m7sPtMuaNQzFr_M7r2Aec1JKIgBRouPA54zA5Tfq8mpMm4XK0saRxTUOnhr92m_YTmKAccnRJSceo1mETrhWHyPAFXM8Rc--T63NUNsZzymSDKak1UgD6Y_u_S4W4sX8sWJHkdmkSBSCFod9ElKEyhel1bQ4HeFCZA-ikhoAW0AAQbiSKKkfhfW9mkwkpIse9qqUFA9sw7IlJBC9IHBXqzYaX0H3i6y7DeJBWtodP3gvIN3dfA0EqJ8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینوستوران از مرز ۱۰۰۰ میلیارد تومان تأمین مالی عبور کرد
🔹
اینوستوران به عنوان بازوی تامین مالی جمعی گروه مالی پاسارگاد، با عبور از مرز هزار میلیارد تومان تأمین مالی، به یکی از بازیگران اثرگذار حوزه تأمین مالی جمعی کشور تبدیل شده است.
🔹
اینوستوران تاکنون ۵۰ طرح را تأمین مالی کرده که ۳۴ درصد آن‌ها در حوزه‌های دارو، سلامت و امنیت غذایی بوده‌اند. همچنین ۵۴ درصد از مبلغ سرمایه‌گذاری‌ در طرح‌های این سکو به طرح‌های دانش‌بنیان اختصاص داشته است.
🔹
در طول مدت فعالیت اینوستوران تاکنون، ۶۸۱۴ نفر در طرح‌های این سکو سرمایه‌گذاری کرده‌اند که ۲۷۶۲ سرمایه‌گذار منحصربه‌فرد حقیقی و ۷۵ سرمایه‌گذار منحصربه‌فرد حقوقی در بین‌شان بوده است.
🔹
اینوستوران با رویکرد رشد جمعی در تلاش است با توسعه تأمین مالی جمعی، زمینه رشد کسب‌وکارها و شرکت‌های مولد و موثر کشور را فراهم کرده و در مسیر رشد و توسعه اقتصاد کشور نقش‌آفرینی کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/664670" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664668">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
نیویورک پست: بنزین در ایالت کالیفرنیا بار دیگر افزایش خواهد یافت
🔹
قیمت‌های بنزین در ایالت کالیفرنیا در آمریکا در ۱ ژوئیه بار دیگر افزایش خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/664668" target="_blank">📅 20:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664667">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سخنگوی دولت عراق اعلام کرد: دولت به کلیه گروه‌های مسلح در این کشور تا ۳۰ سپتامبر سال جاری،‌ هشتم مهرماه آینده، فرصت داده تا سلاح‌های خود را تحویل دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/664667" target="_blank">📅 20:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664666">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
روایتی تکان‌دهنده از تجربه نزدیک به مرگ؛ از دیدن عذاب گناهکاران تا چشیدن طعم میوه‌های بهشتی
🔹
00:06:00 حسابرسی نیکی کردن و شیطنت‌های دوران کودکی
🔹
00:12:40 چشیدن طعم میوه بهشتی، مانع خوردن میوه دنیایی شده است
🔹
00:24:00 اطلاع از زمان فوت دوست در کما
🔹
00:29:00 سفارش به ادا کردن حق دیگران
🔹
00:35:00 دعای رفتگان در حق بازماندگان
🔹
00:49:20  بخشش اعمال در حق‌الله و برپایی عدالت در حق‌الناس
🔹
01:05:00 کسب معرفت از محضر اهل بیت در برزخ
🔹
قسمت بیست‌وپنجم (طعم میوه)، فصل چهارم
🔹
#تجربه‌گر
: عبدالکریم حاجی‌زاده
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/664666" target="_blank">📅 20:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664665">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyncNvNjnkBg2GoNvYB_CeVal4GNBv2kSOX0F0qzEAsdgXgcRnB71BP2w36dNTKfCDDyfyQa85OByTNB_F17IOuYZ5z5yBWw8CzrJBgnb-xBLOZYJwCMOjyO_VshDF3RMDMb_VlTGpWH6z0SvUdpwe5Yu_fcWUFIQKQZKmmAbWFlVruCs7JZuVZv1sPM3_leKeaICaBqwmc8MwyzWdU9t5ZovxC-ZgAvqnhlRToepUyT0mAMJ2Zfy9wIVOHd2f7pudObyIQjQgC1Chlef6JGRfvsd_FNjR5BSiDXSz15ET5M_CyGAQV7ZFULMgIMjBcnlZHtyLA1cRJJS-Uy1Dm0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: مین‌زدایی تنگه هرمز فقط توسط ایران انجام می‌شود
معاون وزیر خارجه:
🔹
ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری میکند.
🔹
طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام میشود و نه هیچ کشور دیگری، اصولا اجازه چنین کاری را هم نمیدهیم.
🔹
شرایط حساس و پیچیده است. توصیه اکید میکنیم فرانسه آنرا با تحریکاتش پیچیده تر نکند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/664665" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664664">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
مدیرکل رسانه‌ای سازمان الحشد الشعبی: مراسم تشییع پیکر رهبر شهید انقلاب، به درخواست خود دولت عراق در این کشور برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/664664" target="_blank">📅 20:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664663">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شرط آمریکا برای آزادسازی دارایی‌های ایران به ادعای یک رسانه
ادعای نیویورک پست، به نقل از یک مقام آمریکایی:
🔹
ما به ایران روشن کرده‌ایم که تا زمانی که در موضوع هسته‌ای پیشرفتی حاصل نشود، دارایی‌های مسدود شده‌اش را آزاد نخواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/664663" target="_blank">📅 20:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664662">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9346a02d32.mp4?token=Tm5FQWcm7gHkNYqUtZfcHNu8YQ4bkTUagaPyYSjRxnGRF1cSANIaKi4VfQYmrhdcLTpeQmSmMtlU5zLW4sqFCJ8aCIriSlgWGYstVDCM_H4aYOjMw1iotKZC3IB1fl1zI8AEuK67k8GyJItrHGdkldI5ah2CtI1vchfY0waHowaw0mmkj0flSfmQn3PBHKwzCK1QLW4BiRhfT5tQufEeTWQYJRvpHCTpn-3nuTRmnNdaXMEvkkffF-_otkBjpCr35NlNAony69ZebV6pddc4kZ_J8ON2CGEJQVi9zHyKpk4d-fra8xb1w6FZIRFhf7HYfC7AR1zcJg-lbhERGoZuag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9346a02d32.mp4?token=Tm5FQWcm7gHkNYqUtZfcHNu8YQ4bkTUagaPyYSjRxnGRF1cSANIaKi4VfQYmrhdcLTpeQmSmMtlU5zLW4sqFCJ8aCIriSlgWGYstVDCM_H4aYOjMw1iotKZC3IB1fl1zI8AEuK67k8GyJItrHGdkldI5ah2CtI1vchfY0waHowaw0mmkj0flSfmQn3PBHKwzCK1QLW4BiRhfT5tQufEeTWQYJRvpHCTpn-3nuTRmnNdaXMEvkkffF-_otkBjpCr35NlNAony69ZebV6pddc4kZ_J8ON2CGEJQVi9zHyKpk4d-fra8xb1w6FZIRFhf7HYfC7AR1zcJg-lbhERGoZuag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالان انگلیسی، ورودی‌های کارخانه سازنده قطعات F‑35 را مسدود کردند
🔹
گروهی از حامیان فلسطین در اعتراض به استفاده از جنگنده‌های F‑35 در جنگ علیه فلسطینیان، ورودی‌های کارخانه شرکت «بی‌ای‌ای سیستمز» را مسدود کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/664662" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664660">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtMtTS7sKvsYLWI-XtvY4uK5lVJQ-gRDqVupe5SMW7huAv9KFhxfTXzRZZrTfreycN8wdOaKAf-PTq8fUIevr4b5pm654i88OBm8ZvDQlYsuJBxgCqufh7eS6AtWv5JHNlTOxHjbJOiBM8JQ44qGyTPgCuUbn6fe-2EpSG5kuSxkXWkyBDLmOrOpaS6yJlWGpnnHX9GThhhwcVvF0AieIAkcMqAChcAHkpMxnLEcdo6ppuLexu9oAlcL4qBjDJ-JobzfToFgydpjrukAsyEX8lnyOpL4F_gGqYPOS2f5sXZg4DbImbfnXx9u1KM46tMKEnUqb2IX8jLwi2j3lpm9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrXcdakADyIMp9knJoVccWs7ZSZgF_iWPi7lVNEP0XICp7uDtr4L_fI1wqRRT7Vah7cxgCbBM-gUPCsCgwPuHFfTgI3H9ogX94O6oPLMIGsabGqh2XXCM8gSyvhbQKPJJBHl40xwlWM6FoOdeqiwvcBW0WpsuNyhiAJn-MLgcXVpScRqSF6_mDsrn6H7MCZom25_e5WXPkUt7xXUf91EsrNmFeXrxYxjVImA_yjPmznGc4gIO19Gv1-usADOqYQWLL68yqDKIVhprGazuWl17a8ZVxRo1AV7oPp29_WQ8irrIe-VK_iVki8ShZZqmJaMxIDxXOwpuyvc58Xnj85STw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این کتاب فقط برای کودکان نیست؛ برای همه کسانی است که وقت کم می‌آورند
🔹
«مومو» فقط یک داستان کودکانه نیست؛ قصه دختری است که مقابل «دزدهای زمان» می‌ایستد؛ موجوداتی که آدم‌ها را آن‌قدر گرفتار عجله و کار می‌کنند که فرصت زندگی را از یاد می‌برند. رمانی خیال‌انگیز از میشائیل انده که بعد از نیم‌قرن، بیش از همیشه به زندگی امروز ما نزدیک‌تر به نظر می‌رسد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/664660" target="_blank">📅 20:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664659">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jR6FeKwuOM_rleav2RHDuukLG4SVYP1OJkvFrkaMf47Nvix0HOJqvRsdqOiMfP22U4tmv47PBUMt_U5wWizaWUYxBcSd-csJ2XXgmUPzMO-naB2a5VmK_4artW_uvuNvjblrdTMGY0KgYoYiNcEEfmvr8IZmIpRpucmJMEugAAlTcInCFg2FHm_DkHD09QtHgBrV0OCUC-dz51OPD-mOACAM1-iXIOVt7dNSVio5ejOQyaMENFQri0FrPIzILhl2pRj2eRKPoMtHY65QlBMvV2M1cMWfw6Q3w5vNXrdmuswi53Fi8Zd14-vMOvFAf3woyi0Vqyv2JRHk5pphIfaaJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدیه سلطان عمان به رئیس جمهوری فرانسه
🔹
خنجر سنتی طلایی دست ساز عمانی، هدیه سلطان هیثم به میزبان فرانسوی بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/664659" target="_blank">📅 20:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664658">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3764ca1156.mp4?token=Zti8oNVDWik-LpSEHz9R6c-4vj6uzinkSwlADfwkDHhnjDx7GTuI3cmpI4yPD7sJltmsNXmPHvsh2ckzAYNjz0NrWoYKSyjlDoBuwoIOb_he2TyNcWvw_OvQsq49Q4DAvjgQLa3Yk0UGbG1eTEYxXm5anKlCFwwJlYz4VQWu0z8YUzYwxNkjw22gPlzEp7jpgESf6B5laG5l9UYXRnXu54tyC6Sp-gFhyTQjW5f6khcChNssUMPL1_hQhhKch-RvY0aA22OKuvxS2vDszZkJBz-yaWs5L8sPOjlx7wIG4vP2TCx8xGXXC7I_bAOUWEh7bY5rR_CCoUS30wuFGQZePw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3764ca1156.mp4?token=Zti8oNVDWik-LpSEHz9R6c-4vj6uzinkSwlADfwkDHhnjDx7GTuI3cmpI4yPD7sJltmsNXmPHvsh2ckzAYNjz0NrWoYKSyjlDoBuwoIOb_he2TyNcWvw_OvQsq49Q4DAvjgQLa3Yk0UGbG1eTEYxXm5anKlCFwwJlYz4VQWu0z8YUzYwxNkjw22gPlzEp7jpgESf6B5laG5l9UYXRnXu54tyC6Sp-gFhyTQjW5f6khcChNssUMPL1_hQhhKch-RvY0aA22OKuvxS2vDszZkJBz-yaWs5L8sPOjlx7wIG4vP2TCx8xGXXC7I_bAOUWEh7bY5rR_CCoUS30wuFGQZePw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم هولناک از دوربین‌های مداربسته لحظه وقوع ۲ زمین‌لرزه مهیب در لاگوایرای ونزوئلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/664658" target="_blank">📅 20:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664657">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8730ecbe0b.mp4?token=SCHN-7sgqnz1sj8g6UOFjNhdMj_-6RgteDzIO7gYmxXL6RqUu2mpyGaobfb22oPhGd4ESjDlyWurDmxWgkK7cFYaucrCwJrxCRi7-iECMNet9BuhNCq8a2uYJe4hIRNGDi53RAtD7ol3S61mKf5tAvohaGmrfgAcwVtXFZUm8IqxX6frhheKMUiLu2hhBISZht5DQ9U5XdzyyfNCWdFwNprSDVpf5MSEX8Wvm6cHZjn_xab0GF99MRJbkwPZsiNoaqhPHpM_4_RwJhy_CnSgbiDeovVzAMVnol2q2H4fKhJQ6IwgjZ83bVYHpgTKdl9PLDZVArKrkLratEcOgY3IFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8730ecbe0b.mp4?token=SCHN-7sgqnz1sj8g6UOFjNhdMj_-6RgteDzIO7gYmxXL6RqUu2mpyGaobfb22oPhGd4ESjDlyWurDmxWgkK7cFYaucrCwJrxCRi7-iECMNet9BuhNCq8a2uYJe4hIRNGDi53RAtD7ol3S61mKf5tAvohaGmrfgAcwVtXFZUm8IqxX6frhheKMUiLu2hhBISZht5DQ9U5XdzyyfNCWdFwNprSDVpf5MSEX8Wvm6cHZjn_xab0GF99MRJbkwPZsiNoaqhPHpM_4_RwJhy_CnSgbiDeovVzAMVnol2q2H4fKhJQ6IwgjZ83bVYHpgTKdl9PLDZVArKrkLratEcOgY3IFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول پولدار بشم بعد بچه میارم!...</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/664657" target="_blank">📅 19:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664656">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سخنگوی کاخ سفید: استیو ویتکاف و جرد کوشنر برای برگزاری مذاکرات سطح‌بالا راهی دوحه خواهند شد
🔹
همزمان و در حاشیه این مذاکرات سطح‌بالا، گفت‌وگوهای فنی نیز برگزار خواهد شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/664656" target="_blank">📅 19:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664655">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سامانه‌های بانکی هفته آینده همزمان با مراسم تشییع و وداع با رهبر شهید ۲۴ ساعته فعال خواهند بود
بانک مرکزی:
🔹
شعب کشیک بانک‌های استان تهران روزهای شنبه و یکشنبه فعال هستند.
🔹
همه شعب بانک‌های کشور روز دوشنبه تعطیل هستند.
🔹
علاوه بر دستگاه‌های خودپرداز بانک‌ها دستگاه‌های خودپرداز سیار در مسیر تشییع مستقر می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/664655" target="_blank">📅 19:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664654">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
نشست روبیو و ویتکاف با کنگره درباره تفاهم‌نامه آمریکا و ایران
🔹
وزیر خارجه آمریکا و فرستاده کاخ سفید در منطقه قرار است کنگره را در جریان تفاهم‌نامه میان واشنگتن و تهران قرار دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/664654" target="_blank">📅 19:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664653">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3A5Q9mKF9SRtvQ_jC80wxFMTsE8Cw5ST8p3raU1-eNwDePlWdgWR6X2AIopahYaUbK13HFVLHP2EgUiZLWgSceKcMtmaDczzm5RoZply_M-bXWwZ3zXgtktr53HTcAvCqk05VoF8NSiCjd4hX2yzjT9wx2S1PdHb5e0mXz1CiUaCd_6ifGBC6Zt4ASXpGNZJQd8CXss22_FbfUllInJlPkpgsHE4UA0g6Ro6nkQK3OVwq0_fJTvHuPRSCZfZEYyjjsCvUL_9hsbiN4d20bta5YwMPagm88teOaCuThY49g-jyrSvJ3aFFr1V3nltUav73VOXPBbg0YO6bq6CAfHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏡
زمین را قسطی بخرید
بهترین فرصت خرید زمین
جهت مشاهده مزایده بصورت هفتگی به سایت املاک و اراضی آستان قدس رضوی مراجعه نمایید.
🌐
آدرس سایت:
https://amlak.razavi.ir/panel/auctions/#auctions
📞
شماره تماس:
051-91008003
#زمین
#مزایده</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/664653" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664652">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: بی‌برنامگی وزارت نیرو در بحث قطعی برق مشهود است
احمد آریایی‌نژاد، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در صورت باز شدن صحن مجلس احتمال استیضاح وزیر نیرو وجود دارد و نوسانات برق، شفاف نبودن این وزارت در برخی از موضوعات، علل استیضاح وزیر نیرو است.
🔹
بی‌برنامگی وزارت نیرو در بحث قطعی برق مشهود است و باید توسط رسانه‌ها این موضوع اعلام شود که وزارت نیرو بدون اطلاع قبلی برق را قطع می‌کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/664652" target="_blank">📅 19:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سنتکام: هم‌اکنون بیش از ۵۰ هزار نظامی آمریکایی در خاورمیانه مستقر هستند و در حالت آماده‌باش کامل به سر می‌برند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/664651" target="_blank">📅 19:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664650">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABccn4AG8j-0SYnWmTyj13pBcN2BXPY3Q2glPmqIZNEGcdovRLVseTLXLy5I6TieGP4CPcXheyWfmuh99ZVYn3a3vXDJ7bV9mTVmqFjyQmZR_iAionqU1Q49DdmLseCX7GNKgjC1hkd6HKBX5xehrFdTXOj09RZzbcdkfQG7Gxgw7V-PpJ2BLwhiuo-YkKHorWQzJctnjZAD-vAFtAEWnAq8Fi8r93pwfZK0x9SkCFjoXGAR6z-KvTjYS5uhKdTBUlf6-I61eQTpPvHHCOg1DhtHjjk1GSzeRGRB-uWc9S5jaj9pg2DZIsz8AW_S9MoCWlrMWcRElBdHhE5pjDhXlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ از پیروزی تاریخی در پرونده اختیارات ریاست‌جمهوری
🔹
دونالد ترامپ با اشاره به رای دیوان عالی در پرونده «سلاتر»، مدعی پیروزی بزرگ شد؛ وی این حکم را «تاریخی و بی‌سابقه» توصیف کرد و گفت این رای بر اساس ماده دوم قانون اساسی، اختیار رئیس‌جمهور برای برکناری مقامات قوه مجریه و منصوبان آژانس‌های دولتی را تأیید می‌کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/664650" target="_blank">📅 19:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664649">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
وقوع انفجار در جنوب لبنان
🔹
منابع خبری از وقوع یک انفجار در اطراف منطقه دیر میماس در جنوب لبنان خبر دادند که توسط نیروهای اشغالگر صهیونیستی انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/664649" target="_blank">📅 19:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqox_q82jcX6lT6iUMeWmsJYvfm9wx4NosjAtfXs5GDw4ubI_dhKhIm7MM3OgXPYdnJhP5KsA7sJZ6Zv6RKDqVolPnGNhdgYtvo2DZLLJtYrHt94FylJL9V3yo215Seni0Uar641wCp41FEgewxuN9uLVfuveNVr71U8hNeGEEYMKGFN4AvimUqsPNsc4Xomyyumc7obqSitl557tKC9AyYXoXAn8hEh729FDgcC7bX5lWpPNOwMC72WyINAQFHtCmtY12Ib-e55-fw0ixTlgfrrHus2wdzoDufYQeRO7Cvtb6LR7MhwQCk6sCOrNCX07Gq03gPhnJZY3XPiDY0gFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زابل؛ گرم‌ترین شهر جهان در ۲۴ ساعت گذشته
🔹
طبق داده‌های سرویس هواشناسی Ogimet، شهر زابل با میانگین دمای ۴۸.۶ درجه، گرم‌ترین شهر جهان در شبانه‌روز گذشته بوده است.
🔹
همچنین شهرهای طبس، بافق، دهلران و بم در فهرست ۱۰ شهر گرم جهان قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/664648" target="_blank">📅 19:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664647">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
خاطره روحانی از ایستادگی رهبر شهید انقلاب
حسن روحانی:
🔹
در جلسه شورای انقلاب گفتند اگر بخواهند کشور را بگیرند، من خودم تفنگم را برمی‌دارم و می‌جنگم تا کشته شوم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/664647" target="_blank">📅 19:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664646">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IddEKVT2c67Iz5uE2Loix_60X17gPoUM-WDp-75efjR0hUNKXk5HPyUmTxGgOeweLSJnW1GBwZ5QrZC4Tp9PeG90OlUAmT14iIsARwHoWNSgZsqIIFewwIiAEBOEgKD5be-RoqaR7P-q62EsKPGoUW0JUHIRS1TVBeT81Oql7wKKwt7oKu4re0JQJfchTiGCBXffbvsWyAOkTRNaTkCJmK3tQRW5cRozC7xUqAH4S8dKxuysvDNs56OEnrUt4evyQEVhvo3RJqjX0_2kb4lQdZQNiRkyrcRtTIdZRyVljzphDUvHIC_2_vEYVGWgPE_fzvrzGIFpEiMTMXzHcmkj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/664646" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664645">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYga1fs6b9ktnz1B6u5Kf1V1aAO7PKpUAKjpV0Ms86EhEC-Gf_dbh9vs3RWYxpov-pWWPXI2gFEGTiEXc6yPJ-XeP-g48Qo71KGaNybGYQ-qntP-S2MuQpF0uh0iCFCcWic1s_YTCe5YBqORGUTSSAExIgCmvBqupfy7YQekrEqp0ASNcri_D-ZAerXHmjkWlwIo-o8885TGvJ5yeDnamdVkfyvMJ8cgYnzunSdWRh9cB3yW_jeGOYByfVwXPaH9Qivg7SpHU21cZ7jOJXh-7yeA-D84535zBpYDCHk2n2sOkdGl8NGWi3WPrMJx2OHwmhWty0-LClYu3sRJsBfgGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«برد کوپر» فرمانده سازمان تروریستی سنتکام که به لبنان سفر کرده، در دیدار با فرمانده ارتش این کشور درباره سازوکار اجرای ضمیمه امنیتی توافق میان دولت لبنان، آمریکا و رژیم صهیونیستی رایزنی کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/664645" target="_blank">📅 18:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664644">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqKY9cNyrzlZJx2YtuONvSHwrw9JvIlDK9H0PcLVQ-nEYqzvJtEGiKItr7DFFiNY4BT1dhxHr8_YUjnQ-0yqijGCaaL7mFiYrGlLoj7YodDpZC9xuMErWe_CQPE_bJLYnGSVosZM1qAUb1ejA46w338WM6iK6NRNG6HKTU9pXYtwJXBDVDMmz2jt4fbxka9dvmghx_XdhpFMIExHRfuWv-uS4C6DX7btTP1nCImeEq2Sa9lexkgVJUP_5zUX7umxfVCo-NjIEHH0K8g8mAopO6WU0cxsHzcGj-iJzR4I-INEU_EFVeXDMNdMcEXjXnMDcxQxQMgvsaTp1c23vso2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا برخی از حذف تیم ملی خوشحالند؟!‌ | حذف تیم ملی جامعه را دو پاره کرد | دو روایت از یک شکست
🔹
فوتبال دیگر فقط فوتبال نیست. دیگر نتیجه یک بازی نود دقیقه‌ای فوتبال با عملکرد فردی بازیکن و تاکتیک‌های احتمالی مربی سنجیده نمی‌شود، این ورزش سالهای سال است که تنیده شده به حوزه‌های دیگری.
احساس شما از نتایج بازی‌های ایران چیست؟ کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3226626</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/664644" target="_blank">📅 18:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664634">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ocQkoUhPReXIjREIlj2raZpukBZ82iiPjxJSOgQ9p8ir1xFn__chnMbgW2t9Q9Z6IB0gc5rhDHz0h0yZn03synhAXl3XgdALl3bgOxmzWgQOtcZkjf2iE3xhWHlUZ5fcB_jObMiyLS7prZkHAXszphUTRSvZbvCqew4w359xLvq4dYWfNLKtd6YjH8ZmkPvOFtoptN_KOm-Ko8__hX1tCyXmGFZxfFxJDgYScgRQ654vJ_fFRKrtXTrtH4wqgMfsgC4FcsXnE_Vg901t_-TSZcqD9ANxAYAe-K4xFHYTW56PAlUV5snHzwrYlJIp8nimPlwEQZ8HWBlNwFV-PNsqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlhKOXAPr11VpS4M80pdoutheLHwUQ_QymUqx8gcPxQrncw2oGS88EZ--plqN9sspTi4EH9H11W0P7J1Ke7RkgKNr6w_ZW-TOG_Ozdl8Yq7i42saBEY6JjMpc3J1WStw2ZIAxCfEEdrAkre-kUU0HzQ25btb38zYXCuY7arA-poVwYuh2kubD8r2GREr9I_CeVGR7uODNMHJgDfj0btccpz-o15Ucof7pyog7Srp15I88GQU06dRcQ8XkIXWynlrtwPHC14lgXMyfvD2OrSK_8adslGyBJY9b_NosPEd9Bqo1qEaXu6tkd45GTOQobKrbtfh9HNRkl7pQDIMHquKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUBG8iAl9Ax7FRgTlkuyplcfGYqOF8gwC9OhrjKQzF_xIIXh9rqw3EG_Q3vffpjOBqGx2XDj-yNmZDLy-N7q03dswRtHJ_h4EKOeLcbY8YNAvPr0p0mT_Nm0vmOSAkZLhLmlPWd34sRbWCtFXvcr7dMKQJaCfZO5TmJJDkadttSWbxv-I5xkHPyus3h7SdL29nSjWTQhhgtXN2WmWrY3yn-7_X7P7skO0RaXaqwqfjU9F6JDNz7iRv9V1Z57zCTdJ0iAQ0n6Ddh1hoF_PRYvFSPUybJPEGkYpeuLJuI1vH2tjaJ30pT-u6ayI27N44EMlne04MbSo7vv1H0K0Ook8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtygKXUUY9RGWL_2YfWzy996X6c_2g6BrjskS3QD0lFEbCQI64XNhhBwmMgTMQlAFP2sxbjmyE5vHnDDpeS7eXIl6qmxs0RkRgppuRgua28F7Gex_6gZdBmCZ327p8bo4a8iVcGJMh_IWhaYr9Ha6n-5ruzJgTy6nOi0nQPUxcY1aXlTvvvRKiYyCO94dzpUXUT7YtbIgbnQMZsmMMYuSZ7-YgoBcWE0_VhfJb0TxvMwkjIgXjVgzquneEVWbbEE4HPATSd81uCHZBE8UzExTc88D8LobYBZ9KAaqbkh5Vy1fRww7ECKEZxbP7KFUDq95Xu8VyplfgFQEHiLMcHUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLLHwFanN8CdZrfbUyXhSfqS2rSw6iDQ7aloLW51JDZLkZA0t6Npy1V5aMm2OIKXQ4nU92UAUsAKkuvZ2Qo92w5jPm96XvhNvx9Y_AT1H_5gFOYYQV9No-uwTyY55fj9eeI0nzoF9vBocvcvw49qWXyyh2ZuwzGWYRg2wn6MR3LAbbDJeGBG3oRLQu0XHVAh0-CKlWRkW4ZpaNH0xh-9D7n3gAy8x8Pnc-Xwq4AR3xkUSOezsz_Y2cmGAt-WpqmGB1uVEhM0vGo0GsIAXy-KPovmVAdZyekavpAbLGhvDkS7US7XS2ymxgk74XaaJO7NXKnoGEP46m_vAWYS5jsdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRcC3S6-28X1dcmd2uRFjZs9L0jWW55qC7Ex0mPJzY2mXl1xK8MN9t9gowgNj6lvi8gdeMrd-gj_wqXvrh3YJPl1aQ7L9XiyIfvyy_IBG-asaQEulgtCqSqv20R-TzEpA9bIQnudtWxGFC4dPCumnhwdvMfVRasKFvmic9P_oGQm0xbzykTLYIvhSzw2gbY5RDNZfw-xG5VVkrx5iejWUs-eom8MuF7x2XgwBokf-CJRUsfIHocP-2-UDnJ6kRWixSCOEpXA54WdvEWz6ePCcQHcs8W9pRqNYoynDK82DXkPbX3T94yN8hWjarj8GYTdBYCO9w4GQ0XI3ockPEMt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DljyJWDzMHZsMkWYhstI2rfmWAAkMizbUKI8KLM8G04uP1oICm2y8PAWc-rKV9fX8sZDdcGCesHLl7XZJLfg6CRoFd1Ouw2jiDzOYT94eb6beY1u99eO88_mDnEjTt5SG4whHRhKGu9lQdPOlSmHbqV3hHiHk6OP_41oeurBFI50nkLDnMudGc0DdcxZI9kVZkE8mO_685Yn7INq9-hOQE1lBlDIJ7aMXYhbWgqAvlFGi8lTUvztSXLwGbAZh5wW4QSGxlqZ46ItHZSQoR8FeD1e_Rs6mBhMNgfzr65G1Dn_fYadg_UYLwL2ooraQnGgkRbQytghho44MhpKuB5UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzdBEiJOPucEpa4EaRRR9KPC1KPdNv_X06AZtln_Za_Gtw4VgB0VFOSGE985gKUMoNnig3Caibj4mrmy-DMAcofRvuyPiVE_q5MV3hDhJWRojscZr4sdbvyxvo9zs-JDzyMC8hikkgKeJJHW24HmrUG3I5YYq7Y4lUDlc_L_F0OwG9Z8Lm_EdmcEkfVLCMRUJmQ9sH2mgod3tRScAQ0mXq4Ie4z7SUmdsj2mB4qXIyBXXOUzCO7JEbgMyfo4ZXex2zorvtGCy-yrVEq13b4OJ_kpk017tpdfy6DpNE9OhD3mPIxl36zGvzSModlcY_iF267F9KL7JnqTZuHEwF7-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bzi_rEg5DkpdURDJG94gaopR3wOiKh9ZqBbKsopEyzi2EsfvoR0aIcLg5dmNYVMkwDbakxJnHbQkS4gAX-SzQ7chCrGHmXw1ihxj6gejU6y0FrPfmdWwZ-JyHY6-ODTTY_w_sTSmdUlB-RfSnCNnWd8HRomWCuOWw1_tQOHoNlCfWwBbd-8gQexwnFe2llpTJlWo8D4zb6PJLOZEi0tttrawyEBjkmIF8JO9x_ngqG6BrTNXFjgBOQBW-b8t3DOnHShx9TmfLtdShu3QzszZXil_O2dU_4G391QzHjHY3kYHFfoNHhyEpFcIbDMD-bajKR38ecjaYNdZEZ1KKnIVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAfH7aAJE7jjoD6Q0wB1BxrXcnsmjsexgQWnbSI0w5YaGWgfbKZSM1kOLo8c5IJS6c_FN8RsRDNMWZ_O4c_NW0bEsBka1pikY0Tq2NtoOTK1aG36ZA3K1JNZnKKQFJ-YPbj87SZcE7sRNz0OaeRvp3lqCAmNKAqKo8EkoAIm9BYcZeWhlT5-ykhudh-gA5jszVWN5eWWTKNDKNH8i1Kow4PKHqvHfdyPU_5-m0iHi8sqYKe0TiXkqo6_C93eYpFJrDbJwLJvj12B8FXcZkMgBp1VkXEcVea0c7gB0Lc9lx66xePEzbkK4iPaqMHi23zc0cgObFzibW1yH_laOmBbXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بخشی از پیام‌های ارسالی مخاطبان خبرفوری در خصوص اختلال اخیر بانک‌های کشور
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/664634" target="_blank">📅 18:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664633">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی اتحادیه نانوایان: یارانه آرد نانوایان قطع نشده و فعلا صحبتی درباره قطع آن نیست
امیر کرملو، سخنگوی اتحادیه نانوایان تهران در
#گفتگو
با خبرفوری:
🔹
یارانه آرد قطع نشده و سهمیه آرد در نانوایی‌ها توزیع می‌شود و در آخرین جلسه ما با نمایندگان مجلس و در گزارشی که دوستی، معاون اقتصادی وزیر کشور ‌داد، صحبتی از قطع یارانه نان نشده بود و وی قویاً تکذیب کرد و گفت الان تمام انرژی خود را برای مبارزه با قاچاق آرد محدود کردیم.
🔹
افزایش قیمت اقلام خوراکی و رشد هزینه‌ها، دلیل اصلی درخواست افزایش قیمت نان عنوان شده است. تعداد نانوایی‌ها، به‌ویژه در تهران، بیش از نیاز است و افزایش مجوزها می‌تواند با کاهش میزان پخت هر واحد، به افزایش قیمت نان منجر شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/664633" target="_blank">📅 18:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664632">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
کاهش شدید تردد کشتی‌ها در تنگه هرمز
موسسه کپلر:
🔹
پس از اصابت به یک کشتی تجاری و تبادل حملات جدید میان ایران و آمریکا، عبور کشتی‌ها از تنگه هرمز طی دو روز گذشته به‌شدت کاهش یافته است؛ به‌طوری‌که شنبه ۲۹ و یکشنبه تنها ۱۲ کشتی از این آبراه عبور کردند، در حالی‌که این رقم پس از تفاهم‌نامه ایران و آمریکا به ۷۰ مورد رسیده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/664632" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664628">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRmZHT36rxPdrmIPa5EnY2m7yiwxMTNdSQ4IRz5IO2vosUC88ZQmpavMMhyLs-cXBp8jjSJoQMEiKucVGNdXkDHjVBQ7H61uNXqRZ6t0ZMYG6DCq0Dm3tVWTlRzpNaql3CkFf5GNMZnS1JBNlyHN6uok-wGM6sCpWtc8MC4PU5fEWNnTxYzoA_1vXVLUgVGK3oFcjrNwFLYuZWrQAFEtT7Lh3q6LLHxt5x08_HuaM52LKyrw1bu3ECpeBaeLna28xVUqV15idNRCXdXKJpe9uozfX7lksJnLSFe_CG4sPHYMRvbAn_gl2_x_sdmH4NiqzwtxgmGyrVWDwM7fnJSgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe40c7f4c0.mp4?token=BLZ6YEi7FBcq3pl8KG_896pmbgm83L0sKInemvoebMZVsGScHolF_4b6yC9x15hW6Ve1YTmpYsrDQcCW6DpnXuT-Ngb9pvcdWZROGHFZFYPsJWzBSyuRKaeH-QsdKbgzoOgTHsjVVYfF2hXp2BrpUr1Vs7pIdAi5IEQC5yP4PZ3yE-J9k2OFAD888Fnx5U_HmYMDfQTfZw-f5ZyxLQ8sR5ePHsYN2VGSLQi5Lc4pTvZiUC6NCfBC2f5sH1A7Vxawlt5JdbWyyATmLIYmTFpqsaL7lmfgF-0gHiRzm13yDvM68BjtcKX7oHZ1OgzMOt4Gl7apOusalhKZl-tla6u3eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe40c7f4c0.mp4?token=BLZ6YEi7FBcq3pl8KG_896pmbgm83L0sKInemvoebMZVsGScHolF_4b6yC9x15hW6Ve1YTmpYsrDQcCW6DpnXuT-Ngb9pvcdWZROGHFZFYPsJWzBSyuRKaeH-QsdKbgzoOgTHsjVVYfF2hXp2BrpUr1Vs7pIdAi5IEQC5yP4PZ3yE-J9k2OFAD888Fnx5U_HmYMDfQTfZw-f5ZyxLQ8sR5ePHsYN2VGSLQi5Lc4pTvZiUC6NCfBC2f5sH1A7Vxawlt5JdbWyyATmLIYmTFpqsaL7lmfgF-0gHiRzm13yDvM68BjtcKX7oHZ1OgzMOt4Gl7apOusalhKZl-tla6u3eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت نماینده عراقی؛ کشف حجم بالای دلار در خانه
🔹
نیروهای ویژه ارتش عراق با یورش به منزل «علیا النصیف» نماینده پارلمان، او را بازداشت کردند. همچنین گزارش‌هایی از کشف مقادیر قابل توجه دلار در محل منتشر شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/664628" target="_blank">📅 18:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664627">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
دستور پزشکیان؛ برق صنایع به هیچ عنوان قطع نشود  آرش نجفی، رییس کمیسیون انرژی اتاق بازرگانی ایران در #گفتگو با خبرفوری:
🔹
مدیر عامل توانیر هفته گذشته گزارشی را به دبیرخانه شورای سه قوا ارائه کرد مبنی بر اینکه امسال در زمان‌های پیک ۱۲ هزار مگاوات کسری برق…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/664627" target="_blank">📅 18:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664626">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuJ7LoxCFre-7x9tKLLsURCB7kv6lJioi88ljwMlFB1jxYej5CTzocADsPU5bGnsJmL1FZ7mJOp0DMCErwuuHCVmsbw8Um9-v9euBZzf65Xd5C0jydMBt7OuETJuQHgubvS9wK8jdhz1iV9HAlxfXt4oZNSaZaBRn0oLquOs9CGjpOF8bGiBweo97lbrE4oHtncjGFn91hZmpHp1NG9GI302xBALWCL8qagkK8NXj_v1AMHTYyBNLdRp69xRoJyw5kW6qTkgRXAZRJDdnNxLr7qpod-4tWiQ7KudQ79MDhH5RpN4M4ETl-_oA-Sy1KRK2LNfqULAsjHD3dcCCwpoLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییرات ارزش طلای کاپ جام‌جهانی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/664626" target="_blank">📅 18:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664614">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
مقام وزارت خارجه آمریکا: نشست تلفنی درباره گفت‌وگوهای ایران در کنگره
یک مقام وزارت خارجه آمریکا به الجزیره:
🔹
روبیو و ویتکوف امروز درباره آخرین تحولات مرتبط با مذاکرات با ایران، جلسه توجیهی تلفنی با اعضای کنگره برگزار می‌کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/664614" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664613">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljNQ1Tb2XljM4xPPOuwURbqd_ArLfMng9f7xwHHt19-IPwjybHC2Uhc7TK7npo0RIzR590eSwfc18lcMsW1evkndmp-xRtskAiP2f0v6ih26SzdTFOigJ6N_WBVf84yTBX2G_QkoY02OAcrfyzFnW4Bx8XDNBUfcTJXAIdYfiXBWIrbXX75nqSfuF1Ki09dN7BYCWjegsU-A1RMdc5qSY7ZSC8zmaw88JIjmaloFGP5BSyRnRMDZTomJ500746z32hOfGRW7lzcKfJ48qhqJzBx2hCNBUdlceNq5GYlx6eNWLVSvjqgbFTmRHHzVn_Yq7xAZqLDohOSGW8RfXb7S_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«کوسه جن»؛ هیولای جدید اقیانوس های تاریک / دانشمندان با دیدن این حیوان وحشت کردند
🔹
کوسه گابلین که گاهی «فسیل زنده» نامیده می شود، تنها گونه بازمانده از خانواده ای از کوسه – ماهی ها است و قدمت حیاتش به حدود ۱۲۵ میلیون سال قبل می رسد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3226644</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/664613" target="_blank">📅 18:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664612">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22dc59eb64.mp4?token=CRcgtPhlbRa6z5nl3GJSMlwEC1I2z4ihMkBsGLD_8ulI8QW2nYh4vQaGLPHFPuNgVzrJDWXTsjX7WafK3cWEmmiTMh0twbXru4vbQmieb9rNPRc6qx-rA5rnKSK7uwaniCSaO0dZs-EyLM4M2d66yw3TTVl4k7F1irsbYBnngbov_5MAC_erriCmiTdByiergOZIv_AZ4thg6vQYQdBevg1t4KleK58FE5LS-mpOgXZUH5e5MljCT0jlN0dqQ_canq60OVCuLfshpE0LInVDURS0CsyZMUZVonpIJx6dm5LZQy7AFKVmETY9h4FPgxvo-TCwf_BS9UiHPT2Vr4X-PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22dc59eb64.mp4?token=CRcgtPhlbRa6z5nl3GJSMlwEC1I2z4ihMkBsGLD_8ulI8QW2nYh4vQaGLPHFPuNgVzrJDWXTsjX7WafK3cWEmmiTMh0twbXru4vbQmieb9rNPRc6qx-rA5rnKSK7uwaniCSaO0dZs-EyLM4M2d66yw3TTVl4k7F1irsbYBnngbov_5MAC_erriCmiTdByiergOZIv_AZ4thg6vQYQdBevg1t4KleK58FE5LS-mpOgXZUH5e5MljCT0jlN0dqQ_canq60OVCuLfshpE0LInVDURS0CsyZMUZVonpIJx6dm5LZQy7AFKVmETY9h4FPgxvo-TCwf_BS9UiHPT2Vr4X-PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کتاب «میان‌وعده امروز» با طراحی آینه‌ای و تکنیک سه‌بعدی، تصاویری خلاقانه خلق می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/664612" target="_blank">📅 18:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664611">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nijHrC0frGRpy_xCFkRjg4cI6T3sMLDmMaPTsW3uHqTfX9vKEtQITy2KwhmvbGSif6mUGZ-_hsUfZp0cHjtiRQn2PfMleASmXmJxDBQsDSdK_hLOaYfjIVu0vyAaXf5bcul5qteM8Fc13zYQui9iiUJ1BIbCGM2kgSgnDcDzcjiQDDDZKsDX51Upaf0xDvnD2zisM9O0a-nCfRKfWgE0btV8uCq4tejGhyRyuA5GWXKS5iyJST6zqlkH0JmSZUX-q0TeieE2IoSmQ9nYpPGF8WXQu00ZZQg8aX46khXHQsPvrixic9FOoRJOoR2ZzPx6THq72WeFqHUe6CiUtbWPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهشتی؛ اندیشه‌ای ماندگار
🔹
سید محمد حسینی بهشتی را بیشتر با نقش او در انقلاب اسلامی و بنیان‌گذاری ساختار نوین قوه قضائیه می‌شناسند؛ اما کمتر کسی می‌داند که او سال‌ها در آلمان به زبان آلمانی با دانشجویان و کشیشان مناظره می‌کرد و اندیشمند اسلامی روشن‌اندیش…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/664611" target="_blank">📅 18:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664610">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
قطر فعالیت‌های دریایی را موقتاً متوقف کرد
وزارت راه و ترابری قطر:
🔹
برای حفظ ایمنی عمومی، تمامی فعالیت‌های دریایی در این کشور تا اطلاع ثانوی متوقف شده و از مالکان شناورها خواسته شده موقتاً از تردد در دریا خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/664610" target="_blank">📅 17:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664609">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
دیوان عالی آمریکا درخواست ترامپ در پرونده «ئی. جین کرول» را رد کرد
🔹
دیوان عالی آمریکا از بررسی درخواست دونالد ترامپ برای لغو حکم پرداخت ۵ میلیون دلار غرامت به «ئی. جین کرول» خودداری کرد.
🔹
پیش‌تر هیئت منصفه در سال ۲۰۲۳ ترامپ را در پرونده سوءاستفاده جنسی و بدنام‌کردن این ستون‌نویس سابق مجله Elle مسئول شناخته بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/664609" target="_blank">📅 17:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664607">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEhtq4TVscvsVm8W4H4xp5d_W9rE0Qt3Xb0XIqDjqh8kl_s9nThMTEQLiUAIjrkf520kQZBWSvTzzaI1dwjP0Tx-KQQ9lcPICypw_97o8RcpW6NiJUCYYTm0sfVYohG7Mx25j0q1f5ZLr69J5VbhF3mtx2W67PDwAvTxDNp8v7m36Dz3yAmTVpIBXqhGcTGAvPtRSzxFSZEBQOuQBKucX6CCWKHp3AseAlzlqeKSFYlRNNntHAO0Svh1gC0osxo74FKVJG9Q96LmEwJaPnItwLJYQklHSc2tItuv39vwvcPeUZX6_ZnAK6vdwTH6L7Gl0RwGqcQnyTX-oqwYlcmW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واضح‌ترین تصویر تاریخ از کهکشان راه شیری ثبت شد
🔹
تلسکوپ فضایی «اقلیدس» متعلق به آژانس فضایی اروپا (ESA) با ثبت یک موزاییک کم‌سابقه، باکیفیت‌ترین و پرجزئیات‌ترین تصویر از راه شیری را منتشر کرد که در آن حدود ۶۰ میلیون ستاره قابل مشاهده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/664607" target="_blank">📅 17:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664606">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تنها ۲۵ درصد آمریکایی‌ها جنگ با ایران را ارزشمند می‌دانند
🔹
نتایج تازه‌ترین نظرسنجی مشترک رویترز و ایپسوس نشان می‌دهد تنها یک‌چهارم آمریکایی‌ها معتقدند جنگ با ایران ارزش هزینه‌های آن را داشته است. این در حالی است که نگرانی‌ها درباره دوام آتش‌بس میان تهران و واشنگتن رو به افزایش است.
🔹
بر اساس این نظرسنجی، توافق موقت اعلام‌ شده از سوی ترامپ برای پایان دادن به درگیری‌ها، حتی در میان بخشی از حامیان او نیز با تردید و عدم اجماع مواجه شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/664606" target="_blank">📅 17:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664605">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
افشای تخلف ارزی ۱۵۷ میلیون یورویی در شرکت پگاه
🔹
بر اساس سندی که به دست خبرنگاران رسیده، گروه صنایع شیر ایران (پگاه) از سال ۱۳۹۸ تا ۱۴۰۳ بیش از ۱۵۷ میلیون یورو ارز حاصل از صادرات را به چرخه رسمی بازنگردانده است.
🔹
این شرکت زیرمجموعه صندوق بازنشستگی کشوری و وابسته به وزارت کار است و حدود ۳۵ درصد بازار لبنیات کشور را در اختیار دارد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/664605" target="_blank">📅 17:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664604">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM598rEquyI9ZsGT9VYoNhfPL-t621u2VrbXmRP-R1AN9MU877T5NRhojBhusC-fyEhDNdB7xOy0EJcW7XIcc1e9OX36-Qmat6K0jQSO-bFynzvBvdNWuWn5GiAxNVsfvjGpRINVMq6zPd1akh1Z4fpRhTUpjU14JbzNp_VtQrMQlXyOpnBuY0lCPKjETtetOxv0rv-ykfNa_RR-3zE9QNraDZyVYu8igc_3X4Rc322VW8LRnQpH-qe5hAjJaGe5jEhfvtuRntF79Mf3q3x-2_e2r3eWjIHs2Mw5gZjdf3ad028qRZnDuYlulxjB6K53LeBQzNeG1Rc7FpS16GY0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | اختلال در خدمات بانکی
🔹
اگر در ساعات یا روزهای اخیر به‌دلیل اختلال در خدمات بانکی با مشکل مواجه شده‌اید، تجربه خود را برای خبرفوری ارسال کنید.
🔹
اگر انتقال وجه انجام نشده، کارت بانکی‌تان دچار مشکل شده، از خودپردازها یا همراه‌بانک نتوانسته‌اید استفاده کنید یا هر اختلال دیگری را تجربه کرده‌اید، جزئیات را در کامنت‌ها یا دایرکت برای ما بنویسید.
🔹
نام بانک، نوع مشکل و اینکه آیا تاکنون برطرف شده یا خیر را هم ذکر کنید. روایت‌های شما را پیگیری و منتشر خواهیم کرد.
🔸
تجربه خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/664604" target="_blank">📅 17:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664603">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
جزئیاتی از نامه ترامپ به رهبر شهید درباره حمله نظامی به ایران
در کتاب جنجالی رژیم چنج که این هفته منتشر شد آمده است:
🔹
به گفته یکی از مقامات ارشد دولت آمریکا، ترامپ کاملاً در تصمیم خود برای دستیابی به یک توافق با ایران جدی بود و این، برخلاف آنچه بعدها برخی ادعا کردند، یک فریب یا تاکتیک ظاهری نبود. ترامپ واقعاً اطمینان داشت که می‌تواند به توافق برسد.
🔹
ترامپ پیش‌تر به اعضای تیمش گفته بود که می‌خواهد نامه‌ای مستقیماً برای آیت‌ الله سید علی خامنه‌ای ارسال کند. ویتکاف و والتز پیش‌نویس اولیه را تهیه کردند.
🔹
خواسته‌ های مطرح‌شده در نامه صریح بود: مذاکره مستقیم درباره برنامه هسته‌ای، همراه با تعیین ضرب‌ الاجلی برای رسیدن به توافق. بدون غنی‌ سازی. بدون حرکت به سمت ساخت سلاح هسته‌ای. بدون موشک‌ های دوربرد و دسترسی کامل بازرسان به تأسیسات
🔹
ترامپ امیدوار بود این مسئله به‌صورت مسالمت آمیز حل شود؛ اما همان‌ طور که در نامه به‌ روشنی آمده بود، در غیر این صورت اتفاقات بسیار بدی ممکن بود رخ دهد.
🔹
ترامپ سپس پیش‌نویس را برداشت و تغییرات و عبارت‌ های مورد علاقه خود را به آن افزود تا به گفته خودش نامه زیبا شود. او با افتخار درباره این نامه برای اعضای کابینه و کارکنانش صحبت می‌کرد و گاهی آن را برای برخی از مهمانان منتخب در دفتر بیضی با صدای بلند می‌خواند.
🔹
وقتی مطمئن شد که متن دقیقاً همان چیزی است که می‌خواهد، از ویتکاف خواست به ابوظبی پرواز کند و نامه را شخصاً به رئیس‌ امارات متحده عربی تحویل دهد تا او ترتیبی دهد که نامه به دست آیت‌ الله خامنه‌ای برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/664603" target="_blank">📅 17:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664602">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0W-G2dnHy90UXLNF82lR8HdLqcvHGw3Icclj0UPVtIjlmdbZbw3HF171HzZrS4oyz-FyFp34l0wR8g2dw5_2ZQIgOhAgd3roZAUp4yQaTOgbIzERh478eh34JstXFanAxummgEuF_2zPl6cOiE43kJjeA1ZOfv0wgPZ5ZoxD1e9Bm6d7w-w6qIN_vTHr287OmHYelmx24iNpMQYWhlT8qrl-7__gOTBTGfrJHdXIYDurrbV2JdYri2v6fC3A9z0B9uJNw2Iny4lda_dfyGO2vB3hKcwxrtNgYHOtSim2denym7rzv-I03O_tW8K7TYDgy-uCRU_J2gglql1Nl3L5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای برخی تحلیلگران درباره پیش‌بینی رویدادها در جلد اکونومیست
🔹
برخی تحلیلگران مدعی‌اند تصاویر مندرج در جلد سالانه اکونومیست به ۱۲ ماه سال تقسیم می‌شود و به رویدادهایی مانند بازداشت مادورو در دسامبر، آغاز جنگ آمریکا و ایران در مارس و برگزاری جام جهانی در ژوئن اشاره دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/664602" target="_blank">📅 17:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664601">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk9Fy86jkCGN1w_RiKxBW8jyg34NekXS3lS9qiakEIGPf8d4FVAsDvIrJapyZy-BPoKrkJWuJK3t5BisS2mwdsO1ZN9uZAeNcqSqsCb1Kh9x1x3zm9FeW3I-n-k-Mapz6Q28E5cbRB4xmw1s0deJ084xA4Z-Ul26gM4wjYPtNWchETTkHPyuLJn2wmvcQ4gwaiFsyA6yny6QYr1cj_gSZcqwlI9f-fCWlLqz-3HIzsc_8dHkuHC4oLd0_Xsk5Eu9zdoD0_vMLNRF9Ved1WgDhmzt9TcuN1OKhPpbhbqIXIYZWQ8pnN5tQBxwYuCkzKO4e7GSNqQoiluGoqPkmWR9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک شهر برای جذب نیروی «بانکدار» آزمون استخدامی برگزار می‌کند
🔹
بانک شهر به‌منظور تأمین بخشی از نیروی انسانی مورد نیاز خود، از میان متقاضیان واجد شرایط، در رده شغلی «بانکدار» نیرو جذب می‌کند.
🔹
به گزارش روابط عمومی بانک شهر، بر این اساس، فرآیند جذب از طریق برگزاری آزمون کتبی و با همکاری مرکز سنجش دانشگاه آزاد اسلامی انجام خواهد شد و متقاضیان واجد شرایط، اعم از زن و مرد، می‌توانند در این آزمون شرکت کنند.
🔹
داوطلبانی که در آزمون کتبی حد نصاب لازم را کسب کنند، به مصاحبه‌های تخصصی و عمومی دعوت خواهند شد. در صورت موفقیت در مراحل ارزیابی، فرآیند به‌کارگیری آنان مطابق ضوابط، مقررات و آیین‌نامه‌های داخلی بانک شهر انجام می‌شود.
🔹
بر اساس شرایط اعلام‌شده، دارندگان مدرک کارشناسی با حداکثر ۲۸ سال سن و دارندگان مدرک کارشناسی ارشد با حداکثر ۳۰ سال سن (مدت خدمت سربازی آقایان به سقف سنی اضافه می شود) و همچنین داوطلبان صرفا دارای سابقه بانکی با حداکثر ۴۰ سال سن، مجاز به شرکت در این آزمون هستند.
🔹
متقاضیان برای اطلاع از شرایط ثبت‌نام و جزئیات آزمون می‌توانند از روز سه‌شنبه ۹ تیرماه به پایگاه اینترنتی مرکز سنجش دانشگاه آزاد اسلامی به نشانی:
https://azmoon.org
مراجعه کنند. همچنین این آزمون استخدامی در تاریخ 9 مردادماه برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/664601" target="_blank">📅 17:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664599">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
پزشکیان: برخی جریان‌ها در مسیر منافع ملی سنگ‌اندازی می‌کنند
رئیس‌جمهور در دیدار با آیت‌الله علوی بروجردی:
🔹
هدف دولت در مذاکرات و دیپلماسی حفظ منافع ملی و بهبود زندگی مردم است و برخی جریان‌ها با سنگ‌اندازی در مسیرهای سازنده به‌دنبال اخلال هستند.
🔹
آیت‌الله بروجردی نیز با تقدیر از مسئولیت‌پذیری رئیس‌جمهور در مذاکرات تأکید کرد نباید فرصت‌های دیپلماتیک از دست برود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/664599" target="_blank">📅 17:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664598">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d49d0083.mp4?token=cP2VE3JPvr4PKNC13kUK2iPqkhd8m3x46G3AlBueTsF2-o6Uj5lKOZ7KMkAm394yD4PZXOfAaEtdArB14zOD_EbjeB1kHEA6SSHBzEhbL2SMSoes4cmbNc8REyxlSliHx04quKfFw0nQH40kfjBUFxKh_DTKbLHQH0CIH-eTvv2S_k8UAW_NIim7YNRpGK11vjR3WohNSDfCb6_wFLklJ5Ucudsj1wfZxF6WzNNzq7w0M-wj90vUFQGPDzZzPsr3KMiH02HXgkdq1pcwq-H9QscR9QyW2LEPIT_ktLoR0HJB02yCx4yCN3Te0LPJwGkuc2GWQwpILhyrfXFJZY9AVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d49d0083.mp4?token=cP2VE3JPvr4PKNC13kUK2iPqkhd8m3x46G3AlBueTsF2-o6Uj5lKOZ7KMkAm394yD4PZXOfAaEtdArB14zOD_EbjeB1kHEA6SSHBzEhbL2SMSoes4cmbNc8REyxlSliHx04quKfFw0nQH40kfjBUFxKh_DTKbLHQH0CIH-eTvv2S_k8UAW_NIim7YNRpGK11vjR3WohNSDfCb6_wFLklJ5Ucudsj1wfZxF6WzNNzq7w0M-wj90vUFQGPDzZzPsr3KMiH02HXgkdq1pcwq-H9QscR9QyW2LEPIT_ktLoR0HJB02yCx4yCN3Te0LPJwGkuc2GWQwpILhyrfXFJZY9AVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از گردباد عجیب در طبس
#اخبار_خراسان_جنوبی
در فضای مجازی
👇
@akhbarkhorasanjonubi</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/664598" target="_blank">📅 17:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664597">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اظهارنظر وزیر خارجه عمان درباره دریانوردی در تنگه هرمز
وزیر امور خارجه عمان:
🔹
سلطنت عمان از اعمال عوارض بر کشتی‌های مطابق با قوانین بین‌المللی، حمایت نمی‌کند؛ اما احتمالا درباره سازوکارهای مربوط به خدمات دریایی، مانند افزایش ایمنی ناوبری و مقابله با آلودگی بحثهایی صورت خواهد گرفت.
🔹
سلطنت عمان مشتاق است که دریانوردی در تنگه هرمز برای همه ایمن و آزاد باقی بماند و طبق یادداشت تفاهم، تضمین خالی بودن تنگه از هرگونه خطر مین، بر عهده ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/664597" target="_blank">📅 17:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664596">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
سپاه هرمزگان:
🔹
از فردا به‌مدت ۲ روز در حومهٔ بندرعباس عملیات انهدام مهمات جنگ رمضان انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/664596" target="_blank">📅 16:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664595">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
نخست‌وزیر عراق به ایران سفر می‌کند
🔹
علی الزیدی، نخست‌وزیر عراق اعلام کرد که پس از سفر به آمریکا، در چارچوب تحرکات دیپلماتیک منطقه‌ای، به ترکیه، جمهوری اسلامی ایران و عربستان سعودی سفر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/664595" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664592">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6Jzw04QA9zu4e9n23M90WYH5qIzD7MbFdZLxkzfcBHTK3I9PwDRv_R6z_VenEPpfOtxzUDOmStviMaiWIt6Htkj41SopojUCyKZCXw9sWcI5BZu8B7YZ_FzzXICdFGz0hY6tF3ewVmfr39Q62KMsWpxCo0y5NpyM6ArDJ2TeE3phivwPY568iJ5MvZ2zbyBxOV_d7DDFQCfNjZae4ge8Z2RF8KUMr8HxNtfxKHhuEUx2XmQhYJeQCicET_PQSrjCbz9gR-smss6tgjYj4JW0JvXMxKjprC_ctA-ew599fJ1KreQiVmI7DF9RI99RNzZTI7v3WK6Fqm5z31kqvhnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUATcCCW66lbop-eiPEWZ9Kln7Xp15JXqD-T2RPqoC2_k1eon3xISWIb8_5N5LMfITH-6l05jwl81G4VVbC4h7crP6oyItOAel4bnN9B_Iw8jTDeGv45Eya20GxMdiy2PnEa7crELHB0e9xFdQ2DvjvePvVelJB61urQxlBskWs5R4PQt_F-yswa9y5ApY4PkgYCB0aJN3RLxEZkk62km04hYnQoAe_08TjHzI_KLJ3NCkOIrhgbXWlxriympsamygasesBvOc7C6clZAv1Yd5XFddVuhJdd3rTI0NeznbP4zVeLqA-Ma6mfATVLwXUyiFdoka2Q9oCs_nVnUripdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAIF7vNStojVdFxaZjWIRAsjMstd1Xx-ZwtM3t-chdXzsRxopToXCGmcnYQN6Nx4C_Vaqq4quEvcqBWyRjTHrrIccLKRjDr7mx2mj8IgW8sokznCXZKRcilEzOP4aqy5moYy5aP4u62O0M-8lJczXlyF9jgFoVjuI6QsqC5sQ4VwRuB4eYrGHLP6Wk3tPYxhcU_t-pDNVRiFUNF8D51HnuH02sYZyYFl3IIGFv4ZXV35x_dkHIX_CJ92A5GM5KpaQ7yyKzA807e7fgUby4HTkhgGnkuV863FmPfAyolfbQtnISye4ukflByL3_WJB138oM13mZknWVXK98vFLM3Bgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ظهور «ماه توت‌فرنگی» سرخ در آسمان شامگاه امشب
🔹
ماه کامل ژوئن (ماه توت‌فرنگی) امشب با رنگ سرخ و صورتی در نزدیکی افق طلوع می‌کند؛ این پدیده کم‌ارتفاع که هر ۱۸ سال به اوج خود می‌رسد، حدود ۲۰ تا ۳۰ دقیقه در این رنگ باقی خواهد ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/664592" target="_blank">📅 16:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664591">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
برگزاری نخستین نشست کمیته مشترک عمان و ایران درباره تنگه هرمز
وزارت خارجه عمان:
🔹
کمیته مشترک عمانی ـ ایرانی نخستین نشست خود درباره تنگه هرمز را در مسقط برگزار کرد.
🔹
دو طرف دیدگاه‌ها درباره مدیریت آینده تنگه را بررسی و راه‌های تقویت هماهنگی در موضوعات مرتبط با تنگه هرمز را مطرح کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/664591" target="_blank">📅 16:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664590">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نقدعلی: در صورت بازگشایی مجلس؛ استیضاح وزیر نیرو در دستور کار است
محمدتقی نقدعلی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
قبل از دفاع مقدس، وزیر نیرو به دلیل مدیریت منابع آبی مورد نقد جدی بود و استیضاح او در دستور کار بود.
🔹
مجلس بدون دلیل امروز بسته شده است، لذا اگر مجلس باز شود، استیضاح برخی وزیران از جمله وزیر نیرو در دستور کار است.
@TV_Fori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664590" target="_blank">📅 16:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664589">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDGf2XhjLyP-ib4fRbvnSnZSocIO59nOD6UDUkNxiyFO4H_SOEpBWPUFEaLA4WZkypOi6iaa0SwxhLo1UnOUi-Z8BTdj5HfbaAKsD_QCrG2bd901LasSwepRIvchAcu9xZTDs1TM0hmznKDu5PnEDqNQD-fYcI1AMU7xOx7plgaaBA96zWcL5oty8cn38bUh0mFixIJbq4jLK414w8Ovy29uQ_1UbsHVjsPAIeg12KQkx-Kmu4691WCNZkgG0nkmuqaR6MZQeAinzRQmBMUls76XDF5F64Ze3Si3PLDAbumiiCV5ncwg-zw-fPSK7yeZq_eE-yO-AETRzSqsiy0N9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فشار ترامپ بر سوریه برای مقابله با حزب‌الله | پیام محرمانه دمشق به لبنان | دلیل پنهان فشار آمریکا چیست؟
🔹
در حالی که دونالد ترامپ، رئیس‌جمهور آمریکا، خواستار ایفای نقش مستقیم سوریه برای مقابله با حزب‌الله لبنان شده است، مقام‌های دمشق تلاش می‌کنند به دولت…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/664589" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664588">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9487e29f6.mp4?token=PYRVT3ad3kIGTjaqTPe62jcQ1Zt7WgeGY5kfr8m5oPEUOzu7H2V4MK4wxmAbTraMCJ-mwjXAZXzWBF3vW6tu_nkkYajS4vKJL9ZPa_ANA_d94mfjve2ncs471sFJJO2VCVNVtB8SRixI1uSpAbYPq2C6EScGpRy1hDdKrQjkiQn2kl1IuBWwEzCrh4dMqEoA1lJGJLLw0JTf1LaRpemhpW2iSS7SpxH4YYBj3NCP30_RLnKcbEUjoCJai3ZRcRxKs-FBdQfo8OWFYSoce515SpOVBAh5filGENlIyHrFX6mhYERujhYIShzjwFR9UrzGrQkjcDpzxRIQb464E-Rqrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9487e29f6.mp4?token=PYRVT3ad3kIGTjaqTPe62jcQ1Zt7WgeGY5kfr8m5oPEUOzu7H2V4MK4wxmAbTraMCJ-mwjXAZXzWBF3vW6tu_nkkYajS4vKJL9ZPa_ANA_d94mfjve2ncs471sFJJO2VCVNVtB8SRixI1uSpAbYPq2C6EScGpRy1hDdKrQjkiQn2kl1IuBWwEzCrh4dMqEoA1lJGJLLw0JTf1LaRpemhpW2iSS7SpxH4YYBj3NCP30_RLnKcbEUjoCJai3ZRcRxKs-FBdQfo8OWFYSoce515SpOVBAh5filGENlIyHrFX6mhYERujhYIShzjwFR9UrzGrQkjcDpzxRIQb464E-Rqrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این کلیپ میتونه نقشه‌ راه برای زندگیتون باشه، اول تو حرکت کن، بعد معجزه را ببین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/664588" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664587">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esA9x42CIjtq6i_lND07QIYokRFu6DpvmTqDSztOhKTSLL1-H7R2mkPwy6dKljVv_8t8jZaruMywnfrJkwGcfZRXKyJWrkV-nUs1Lm8O_KoCbSa_tnCzLUSHJgWW7PJEnAauqmxd3iQLSLhRreLoVbChL3HzlRzoTLc_s8VCh0IoKp2ngjTOrkTfGAmwtcZ1bCSQ6XOTiYi4i_bIxvt3ts1iYJg1J9J-drUw7PCgCMHJAToi1B5p90eeKcvNfeKHV8Y0A1IhI7nI9LJ1waSLchG2pM4HfmOrMUiyttTsuuJdTGuZsLMyoOLVXv-TykAydMsKW5w6md9vj9r8Cd2MlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار تکان‌دهنده مصرف پلاستیک؛ سهم تو چقدر است؟
🔹
هر نفر، هر سال، صدها پلاستیک؛ اما تغییر فقط با یک انتخاب آغاز می‌شود  شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/664587" target="_blank">📅 16:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664586">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He9DFHYy8NaIRiZxDkgOqLzQVPbkaYMOKCI09K8U_HYgPI-LfupHggZaTKrFfUkEfjQQyP1Dh17o5sbwZ_dSsWVy4UhjUZzWBTUq84z7s3HMwOYL2-ZUJJFNmRBJr5uAdUr6UvR-NY8gFRGPAotMmWnV6VwjeU0BuECh0MhIb2Y80x2c1SUwFG_p2HHyTdO6FzHktqo9wUkrcUFXiTAUFARTfWn1yEdJ4TOrBOOl9DypFsjq7XyHpjmtsojSTCK2kzdvodeHzePRmqLbF22KZrxuvZ-82bqZ9IpD6JfgFlyQwk-cpSR5jrLmR69zI2Vgwh3BaFhIYg31H9RUKfNSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه تکنیک ساده برای تقویت هوش مالی #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/664586" target="_blank">📅 16:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664585">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9729d15bc6.mp4?token=ZZHO2eLKWZ-UoM6rVtyVidgcp53YYtCEX5-teA37MsqEygQz7buSi6eN0PeaMfh30uDWYud2z9B1jDSNbO_obCrKEaG-G-aIPZhjbYSKReCH8cEVlgfQ0M3kjvQx8-ycgI15SC41JQHkGatN9NNgvuXQcch_60OE-iTqaLYfYUZ_6BoqRemGQaTBNFIAKkLYxUrGeDE3obIH6zqzwrDobmCP9Y97S0j0TqJttbkVeUA-accDJTDAyTFvCrkSd136h6WD-uc4Y81UGBhC--8oBLWN4_EzlmQluzguszlofvo4EnmH6YYAk66if9lHFgy09ZOZ2MgGF3wV7SMotnNdDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9729d15bc6.mp4?token=ZZHO2eLKWZ-UoM6rVtyVidgcp53YYtCEX5-teA37MsqEygQz7buSi6eN0PeaMfh30uDWYud2z9B1jDSNbO_obCrKEaG-G-aIPZhjbYSKReCH8cEVlgfQ0M3kjvQx8-ycgI15SC41JQHkGatN9NNgvuXQcch_60OE-iTqaLYfYUZ_6BoqRemGQaTBNFIAKkLYxUrGeDE3obIH6zqzwrDobmCP9Y97S0j0TqJttbkVeUA-accDJTDAyTFvCrkSd136h6WD-uc4Y81UGBhC--8oBLWN4_EzlmQluzguszlofvo4EnmH6YYAk66if9lHFgy09ZOZ2MgGF3wV7SMotnNdDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایندهٔ سابق کنگره: آمریکا در جنگ پیروز نشد و ایران کنترل تنگهٔ هرمز را در دست دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/664585" target="_blank">📅 16:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664584">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای کاخ سفید: به تعهدات خود در آتش‌بس پایبند است
🔹
در پی حملات به کشتی‌های تجاری، آمریکا پاسخ داده و تأکید کرده است خشونت با خشونت پاسخ داده خواهد شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/664584" target="_blank">📅 16:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664583">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/005f8a8af5.mp4?token=pi8a1NiESFz1PKyySj8ZTmuoAJC-BUOS-aUFniQ2avoEgvAcxDuwqbHZM1gBgMU1VkS1JHBofR0wyxg3PjxluK7vzdgbQj5eBZgHiQTqTfy_rPRjACirhu-EEXn1yJBjb5VO7taGMwy5RZutGNs4wvyqhuylxJ2lFisuGpM9a_IhydOrb8GpyF9yMB-P0UvFg1GN-r0AEjKizxSi_2DbK4UM-VxtiYLT1lWf8DTXAZt8LX9LAmFdHBW6VbuaQ1MOTo_giWc_Fbd5NzUYy2oVRL9J4YzSimB_YblKh_fGSxeDbcCxH8iG39pOS4NoKAqYRqL_OnahaUXp9CJCjDWnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/005f8a8af5.mp4?token=pi8a1NiESFz1PKyySj8ZTmuoAJC-BUOS-aUFniQ2avoEgvAcxDuwqbHZM1gBgMU1VkS1JHBofR0wyxg3PjxluK7vzdgbQj5eBZgHiQTqTfy_rPRjACirhu-EEXn1yJBjb5VO7taGMwy5RZutGNs4wvyqhuylxJ2lFisuGpM9a_IhydOrb8GpyF9yMB-P0UvFg1GN-r0AEjKizxSi_2DbK4UM-VxtiYLT1lWf8DTXAZt8LX9LAmFdHBW6VbuaQ1MOTo_giWc_Fbd5NzUYy2oVRL9J4YzSimB_YblKh_fGSxeDbcCxH8iG39pOS4NoKAqYRqL_OnahaUXp9CJCjDWnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای کاخ سفید: به تعهدات خود در آتش‌بس پایبند است
🔹
در پی حملات به کشتی‌های تجاری، آمریکا پاسخ داده و تأکید کرده است خشونت با خشونت پاسخ داده خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/664583" target="_blank">📅 15:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664582">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
رویترز: توافق برای آزادسازی ۶ میلیارد دلار از دارایی‌های ایران نزدیک است
رویترز به نقل از منابع آگاه:
🔹
تیم‌های فنی ایران و آمریکا برای بررسی اجرای تفاهم‌نامه اسلام‌آباد به‌زودی در دوحه دیدار می‌کنند.
🔹
به گفته یک منبع ارشد ایرانی، این نشست با محور مدیریت تنگه هرمز و کاهش تنش‌ها برگزار می‌شود و دوحه و تهران در مراحل پایانی توافق بر سر جزئیات آزادسازی نخستین ۶ میلیارد دلار از دارایی‌های مسدودشده ایران هستند که در دو مرحله آزاد خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664582" target="_blank">📅 15:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664581">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فروش آزاد داروهای غیرمجاز و اعتیاد‌آور در عطاری‌ها و سوپرمارکت‌ها!
محمود طاهری، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
متأسفانه حتی یک‌سوم نظارتی که روی داروخانه‌ها وجود دارد، روی عطاری‌ها نیست و برخی عطاری‌ها داروهای ترکیبی غیرمجاز تهیه می‌کنند و به دلیل عدم نظارت، مشتری‌های خاص خود را دارند.
🔹
نه تنها عطاری‌ها بلکه در بعضی سوپرمارکت‌ها نیز، اقلامی به عنوان شربت‌های تقویتی غیرمجاز دیده می‌شود که فروش آن‌ها در داروخانه مجاز نیست.
🔹
برخی از این داروهای غیرمجاز به کلیه‌ها آسیب می‌زنند و بعضی از آن‌ها وابستگی ایجاد می‌کنند و مصرف‌کننده راغب می‌شود دوباره از آن‌ها استفاده کند و تنها اطلاع‌رسانی کافی نیست. مشکل اصلی، ضعف نظارت و نبود برخورد قانونی مؤثر است.
@TV_Fori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/664581" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664580">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOW5biuwyOlFKFvpLVhWyPn4e0sxA2-rsvNuK9VOWfSYnipPgFp_Uxc2Y5dBPk-Nu4F_-j-pjB_yGim5x5U_v4hGWE2pPuBlHDWvHDQQ-QYMUPnh2asIloF_R59D80OiH267SpNTJR9VEYsyEP9o6b5tRkPK-yRrW_-HtmHp6h3BxEVcdZwoQVu5Ducmo9fzgbdlYauGkBCcEnCuigQ0GFMffJsknkcp-jusDMgQ8uLv7rgKCIlo8tcO8vWFZtP_WUfmEjZziHx10aBXbHACJ7vD-fNKRzzTBq1c5Yus4ej-cpmvivlTsbTfslV5DjSYmmUJMQwM4KpR7vjkcWHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان اولین دیدار یک‌شانزدهم نهایی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/664580" target="_blank">📅 15:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664579">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fdf4ba5ee.mp4?token=kZq3yazbJxejXZbFTcyedwHskryFWZEXL4o85CAJzgV5_yh5WJB1AWY67LQLM8jtZQaEioaY0_GR4_4WbjY4GlGKLSDq9llUr_iA4IzNsHXMW6TU7ZtDeSE_8vZDj4IUYdVda2Wlh4MEF0gqlrhVZo5qPjIRq-4R_mamPoGkq92VvU5ar-Co806in8CGE9qXXLa6WBnF02PrVaY2Q-OYHqyyYzVv00hWBfO-jH9p9iL_vDK5pgT3cUZUvh7PIHAfFYVEWAumU9FfXfPxVGfdYI2eGt-5Jwc0djQTGgw0T9PCOhJmM_X1UEE1OluFe_DxDinGTmeUIg6lS6EsVdYhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fdf4ba5ee.mp4?token=kZq3yazbJxejXZbFTcyedwHskryFWZEXL4o85CAJzgV5_yh5WJB1AWY67LQLM8jtZQaEioaY0_GR4_4WbjY4GlGKLSDq9llUr_iA4IzNsHXMW6TU7ZtDeSE_8vZDj4IUYdVda2Wlh4MEF0gqlrhVZo5qPjIRq-4R_mamPoGkq92VvU5ar-Co806in8CGE9qXXLa6WBnF02PrVaY2Q-OYHqyyYzVv00hWBfO-jH9p9iL_vDK5pgT3cUZUvh7PIHAfFYVEWAumU9FfXfPxVGfdYI2eGt-5Jwc0djQTGgw0T9PCOhJmM_X1UEE1OluFe_DxDinGTmeUIg6lS6EsVdYhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار نیروی دریایی سپاه به شناورها در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/664579" target="_blank">📅 15:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664578">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LebrewVJ-5zYcbdWmL8ye_AN3mByAckQJi0tWeyuD9hnHDpQBEzPEy8TEch2dc64hH8Z4MNHPqVQLtU655kaDZ-LMFCKlE6I0duPrcZ7PbpjIKTadn2evq2b851t9nTi6e-JykkzbDP4Qsi_h_dc_F3L-QfrDTSRyyHux1rKuRopr6Hrq8RFCJE8sDQa5jCO_Tk_zCeWEPx6LEHXnFcOwwXu7zI277B1R7y1-aSav8HJfg3kFuJ6riMgjWc9OPngAT-VX8zUiVDpPZ0KYaTKL5gcABmp_hJlqKloC1PljwfEG8PkpCY0EsAfHroRb049ThpKI69xQhaObIZ1M9ZojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیئت منصفه دادگاه مطبوعات زیباکلام را مجرم شناخت
🔹
هیئت منصفه دادگاه مطبوعات صادق زیباکلام را در پرونده اتهام نشر مطالب خلاف واقع و اکاذیب، بر اساس اعلام جرم دادستان عمومی و انقلاب تهران، مجرم شناخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/664578" target="_blank">📅 15:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664576">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi0Pp9DmjeQ5OIpJHodZHodfR3x7z91Lv1kgGPrOPxQFRPdtsTR6AzkGQjS5Npr6lDP3_t-_EBoOmhVYX5tuv7eBUj5Zie303Bn1F3biO2RRB8HHkALCCo3sRot4H-ZCbcDHoIEhJ7-LiuJUQoCIjLYsnewNbrkfa7umkVuO3r2BudJmse0oM2ygJAkT9JDcXahUhmxJRMaIgeRBHr4-DNiloTOdwBaduPJNfIyR34g0Yvn0B9kmNhhRb23Uqnsf642tOdsBzlU0cbQcN_cTLp-BQqf7rRxfGcVL1Arid7DISM5ZUmnePZEsvCT6UCnZInOshX5xxLY_dssNvD9AMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جهش ۱۲۲ درصدی پرداخت تسهیلات ازدواج و فرزندآوری بانک کشاورزی در خردادماه
🔻
تسهیلات قرض‌الحسنهٔ ازدواج و فرزندآوری پرداخت‌شده توسط بانک کشاورزی، طی خردادماه سال جاری نسبت به پایان اردیبهشت، با جهش ۱۲۲ درصدی در مبلغ و رشد ۱۲۷ درصدی در تعداد همراه بود.
🔻
شعب این بانک در سراسر کشور با هدف تسهیل شرایط ازدواج، تحکیم بنیان خانواده و جوانی جمعیت، تا پایان خردادماه سال جاری در مجموع ۲۰ هزار و ۲۹۵ میلیارد ریال تسهیلات قرض‌الحسنهٔ ازدواج و فرزندآوری به ۸ هزار و ۱۲۳ نفر از متقاضیان واجد شرایط پرداخت کرده‌اند. این آمار در پایان اردیبهشت‌ماه سال جاری معادل پرداخت ۹ هزار و ۱۲۷ میلیارد ریال به ۳ هزار و ۵۷۹ نفر بود.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/664576" target="_blank">📅 15:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664575">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryxR3r9Ie6hV1iyorD9W07zTZktSQngWPOiojtpd2Ngbr_j_RIXTCqmiZEDZ3kjBJQUB-QCe75NFzCX0Jl7j-DrncIdMmGOFWO__j0gxQcUAbf-mtjpT2DEvkO7NH6RM4NzDty2ve7r128deBn-lTxw5KqprfvNSaEUQ4yNL922yzNGsKhonb3-O8ebByDDBCMS1b6a-HV5pSewhaXnqpkyRr-WT_1rHF5Ndm1AhbxTQnxnwZw6XnvCGR_M9pKZanAJR1iWZIDA7DNw8B6FCfHZx2Dmy0tYUQJmpfBIhJ3C3WfLddqb65OvEi8d8IWFXWaqkWEjPiVoODGR1vB_aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشاگری کاربران از رنگ‌های احتمالی آیفون ۱۸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/664575" target="_blank">📅 15:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664574">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ناکامی وزارت نیرو در انتقال آب ارس به تبریز
علیرضا نوین، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مشکل کمبود انرژی مربوط به امسال نیست و سابقه چندین ساله دارد و باید نیروگاه‌‌های اتمی هسته‌ای افزایش می‌یافت ولی متاسفانه نشد.
🔹
وزارت نیرو در انتقال آب ارس به تبریز ناکام مانده و علی‌رغم تعهدات و وعده‌ها می‌گویند باید اعتبار را برنامه و بودجه بدهد. اعتراض ما در بحث مازوت‌سوزی نیروگاه تبریز به جایی نرسید و هیچ اقدامی انجام نشد.
🔹
در روز رای اعتماد به وزیر فعلی نیرو باید تعهدات و برنامه‌های راهبردی را جدی‌تر می‌گرفتیم ولی این کار انجام نشد و علی‌رغم تلاش‌های وزیر نیرو هنوز نواقص همچنان باقی است.
@TV_Fori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/664574" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664570">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6tFUdS4KttaieK6MbFwNJoEPOzNzXUmOmIAshsAKeEOXWuTPfBND28qReZKg3ub6GNQo2N29AfKO6GDNN5_7VziicO96Eoct5tJ_ntTkE92MQW1CjIzkspoEBC_CCj-PsXgOWrASKKR2RbEkD958InFI-rONTIcVqFRFYht_SNrO8UKTc4IL4peXYsKMFzPMyUs2A7n-vQolRivq-VZICasoKffPUWAiZBjrPdxbWHAB-Bre5_D8rqKrD77SoHFiI7I1iIDjskGZuKPULOt1Zr2CwN85F5K2wYSkiRhMSzvX4SC_FnWunK6n5nS6I7HFqubNiQPHyc_550TQhNIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_xECjPmmUzaJJkDbGIEegQ8nQ9CL9WPoruluHt3n-IfdSRM1MrHqdUWinF1mf0Xq_F3cWDt3zvJzxEdxLgFyWZ21iIByip8aoTcNLDjdBrGmbSBRaKF02w0YPxYue58p6j7u2Z-pgg4gPOIsnkzKjuYkfH_b8GQC6Vdr7u1_ItqXR_8Mv_g1ypXmkDO5h_XqvGrb0bs4hSDftpRhyp4kwfv8fQHtbaIJw2eue41rlqeJo-6mN9pWHGLGwDZmRxNlPXIm0SFTQENIf9noOnJrVMAstDnMwVKK8jrn-fZ0aQxPMXZP_VRjs9UIbDte80ybdn2f7R_hZBX112984V-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsCeFnohopRP8X2uvVKB7TOUNzEVsKl1HnjtO_7muSKN76sOcjduK4lcwE76l5plTp3_hJlPmY2xxEcpQ0YaSEDOuDc0jYUuILWXxOcxIDBg3OafqPqzHdguuNzWbc-8YuLDrqvgfb8oZg6DKWEH8byI1xko8S8jAkbED34gu1FhPvcKi4bWKkW67SZyocUTAoSR-z4SK1Se6gGmIJW9G96Tssg4eH8--ZGPOM3PnbMpxA6LQDwJgd59Jx0A_etQJ0E03MjWDNKZFuHYyPzqGte_x1RxhZe1fgYm8MTI_oba1gTS7g_Dq-szE3wdkHQ06yCbHM7uuoeZ5Tnt0DbDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eudTthtShdUDFuYsrcMnk3VgHMXcfjzPIPIwJI1OYGSHaGIOTr07R3slPftrkEvpdOizeena5Tu3HY3lapK98yHtUKFYlcdm6u-DUF9ciJs32OA4CxgiuQMMohmQkckY8JHsWU19JELl-8C_7blxTEgKFoTduPWuXY6VArEHdxcHc-hd0tf4iO2gaRo_FPM1AfirBRfpd5-b8cQEYJcIbf5bp4fzD0x245bYIUx4aeINCp2vTkeH4HxyG6jztD0kNPG16oFwDimuhABu-ADatMDbuTwImbJtBx4Y8BjV9Muxll1P77SCx1elTAOkxRR9Ywobp1u5GkEChnZyrH74HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرماندهی جنوبی آمریکا: تفنگداران دریایی این کشور برای پشتیبانی از عملیات امداد و نجات زلزله‌زدگان در ونزوئلا مستقر شده‌اند
🔹
جان انسان‌ها را نجات می‌دهند
البته بیشتر وقت ها می‌گیرند...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/664570" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664569">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL6k9yw4lOG8zsch5AUfOw8prixEilaty-UCE_HpFBBlf-u2gKdlrhPhqD2ejkp1AljbnKCv8z3h5Cb0Jn191divXBfBXw6mEIHJiHC_zDaPNOHhQg_ub1EeqHhbWdXH1XPiDYDmfmUSQdXh3h8yys7ocrKlYLiDG3mCINGlKBMY88np9jhScaSlH3IEDxfBgDmLQdkeEziOLpCIKiIFogCMDSQD4UxbDxMO6mk-J6Ae5YcNpXTD2zs1o2Xe0z8uK9oIb1VRqVpnJeGYtGOC-4ApTFNeQ0QIFXhvf6fl5TF8YRMWpb7BmqOcYjKhXZ_oTcBbYfh63MHBl_599HKQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: دیدار ایران و آمریکا فردا در دوحه برگزار خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/664569" target="_blank">📅 15:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664568">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333a29ab62.mp4?token=VJ_QZRjf1dWOEvqPoY0Od4HjrPID2zDdf3CSuxX4_DzMAK6wwX11kxQpNik2wb9ydL0KzddiulK0URax1yIMOsJHt4UOPM58hMR9fCFqf2xRvtlxETB1sEukeDiNOxh2RG7G3XOguT1mnd3d4NCoaWPaEOp45OhEiJJGkMwhG09mJl45Q9kbZlAIusxzia7VLtgQL6lOW4Uno9K32343ESf7VDfg1SwYJObAivkaOf5fOw0Tb9mIMeD0HgLhXdWXOY6EueMFl2ZoMlNAw3fo0GSAR1uRktcSm_94f1vvbdZgpaehe3Jqg5gfeeOvulqUNJ750APx3lSd4jp4rrdu5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333a29ab62.mp4?token=VJ_QZRjf1dWOEvqPoY0Od4HjrPID2zDdf3CSuxX4_DzMAK6wwX11kxQpNik2wb9ydL0KzddiulK0URax1yIMOsJHt4UOPM58hMR9fCFqf2xRvtlxETB1sEukeDiNOxh2RG7G3XOguT1mnd3d4NCoaWPaEOp45OhEiJJGkMwhG09mJl45Q9kbZlAIusxzia7VLtgQL6lOW4Uno9K32343ESf7VDfg1SwYJObAivkaOf5fOw0Tb9mIMeD0HgLhXdWXOY6EueMFl2ZoMlNAw3fo0GSAR1uRktcSm_94f1vvbdZgpaehe3Jqg5gfeeOvulqUNJ750APx3lSd4jp4rrdu5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب بالن‌های حرارتی توسط جنگنده‌های اسرائیل در جنوب لبنان
🔹
جنگنده‌های اسرائیلی با پرواز در ارتفاع پایین بر فراز جنوب لبنان، بالن‌های حرارتی با هدف ایجاد آتش‌سوزی و تخریب پرتاب کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/664568" target="_blank">📅 15:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664567">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
مکرون باز دوباره با عینک دودی در رسانه‌ها ظاهر شد
🔹
برخی کاربران معتقدند که مکرون باز دوباره مورد خشونت خانگی قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/664567" target="_blank">📅 14:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664566">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6ZyIzHDMO2rD-dKVtwxLg2kjFNGFAeaTlfDiM0zET9za7RQVeHmUK2UB7wCWsneW68qZisH_7sqGD2aG5mf1UGIqer5uNuUhJaFOx2bQcyT53H_--iwFKIwALCe5OcFvQ8NYpaRBupJaspjFDbNUQIBTbMt1RYv1HwCvfefK2KuMSYJWAnF06A9MAEP3uEGnJxopRtsKlwhpZT5LdiubbKE0JQDcUjFwZZahD7cFavJThm46cqtUCiAlzOm-uK4Yb9LM9dvToAK59-gParNCyyoNtC2AljjCZZwwnzK7tmgccsQoA7LV4g1udcM-g-ygA_qGBCfOzyJY5S2O2SqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا نتانیاهو در اتاق جرد کوشنر می‌خوابید؟ | ماجرای اتاق خوابی که خبرساز شد
🔹
در سال‌های اخیر، بارها در شبکه‌های اجتماعی و یادداشت‌های سیاسی ادعا شده است که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در سفرهایش به آمریکا در خانه خانواده جرد کوشنر اقامت می‌کرد و حتی در اتاق خواب دوران کودکی او می‌خوابید.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3226332</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/664566" target="_blank">📅 14:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
فعالیت برخی شعب بانک‌ها در روزهای ۱۳ تا ۱۵ تیر
استاندار تهران:
🔹
تعدادی از شعب بانک‌ها در روزهای ۱۳، ۱۴ و ۱۵ تیر فعال خواهند بود و مراکز درمانی، انتظامی و خدمات ضروری نیز به فعالیت خود ادامه می‌دهند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/664564" target="_blank">📅 14:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b6ad5aeb.mp4?token=JRLp9TixwJ0G6tcn4bUdH79CCmBYblno7twDHHypY_2YGJ5YvMW189pWapfGccNeOJn_A3ZwEuOvRz0kMs6iO5U6uJiOgL-P7Bn2YER_6V7IB4teqEl3MBmNEA_ajcrGQDoIo69a-4HgLDcx1DS5MZhFm-AC0mNuM0jIopdjx0zpQh4KPRUJRuGFQ6drVYR5JSq9_X5LLVlR2InGF3sE7gv5ikfNMEyrNF8bPy2D0VNzILgj_SJ5XrPuo6vTgRMzSD_9Ux75vTmwOWuPFEIP-RaX808gPLE6X7t12lmFHt_1tkM93j4HWCIQN629AepKKW4xBGAfHGmuRn8USSM-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b6ad5aeb.mp4?token=JRLp9TixwJ0G6tcn4bUdH79CCmBYblno7twDHHypY_2YGJ5YvMW189pWapfGccNeOJn_A3ZwEuOvRz0kMs6iO5U6uJiOgL-P7Bn2YER_6V7IB4teqEl3MBmNEA_ajcrGQDoIo69a-4HgLDcx1DS5MZhFm-AC0mNuM0jIopdjx0zpQh4KPRUJRuGFQ6drVYR5JSq9_X5LLVlR2InGF3sE7gv5ikfNMEyrNF8bPy2D0VNzILgj_SJ5XrPuo6vTgRMzSD_9Ux75vTmwOWuPFEIP-RaX808gPLE6X7t12lmFHt_1tkM93j4HWCIQN629AepKKW4xBGAfHGmuRn8USSM-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنجال پس از گل سوم الجزایر به اتریش
🔹
در کلیپی وایرال‌شده، پس از گل سوم الجزایر، بازیکنان اتریش معترض شدند که چرا طبق توافق پیش نرفته‌اند؛ بازیکن الجزایر هم با اشاره دست، آن‌ها را آرام کرد و نشان داد بازی مساوی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/664563" target="_blank">📅 14:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664562">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnyT4hNAQ3CDIBFxcg0EqIsp9fLMiczXUkAdlHMGddDFsA96hEIKxTh_Vaiou0J5E01JBX36177QUOzOmnENnWRseZOJanxiIFx6x3KP_nVKryB-p2AMuA0msNAJTFG3CMSKsUUBxt4G0IVVq3frjGLvj3bebCJ7YxNl11S5pRB1smU3M03tGrC_7VybwgR3hot7j0TmS6PURetHmb2rrCuGlMewPIWGg29HVWIdKgafFsegEi41xt1naLdS8A3m_OCy77W7phZ5_3Oygt6AkKNLpFFvoYHqYfIiP7BOYCX2mZQ6z307lBEo7GJDcjKk8qf5c5LEqX84LT-vEFN89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ درباره انتخابات میان‌دوره‌ای: بالاترین آمار نظرسنجی‌ها تاکنون؛ حتی بالاتر از روز انتخابات، ۵ نوامبر؛ این در حالی است که ایران هرگز سلاح هسته‌ای نخواهد داشت!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/664562" target="_blank">📅 14:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
تداوم اختلال بانکی و بلاتکلیفی مشتریان
🔹
با گذشت بیش از دو هفته از اختلال در خدمات بانک‌های صادرات، تجارت، ملی و توسعه صادرات، قطعی و ناپایداری سرویس‌ها ادامه دارد.
🔹
این وضعیت علاوه بر خسارت به کسب‌وکارها، به اعتماد عمومی آسیب زده و به نمادی از فاصله وعده‌های رسمی با تجربه مردم تبدیل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/664561" target="_blank">📅 14:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664552">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5uarq7sdeD2nlO6RUic_rp07WcLR7WLgeJ1-zlUQGzTOboKE068JaASva9WTF4fb9Q7ogwcTe9yYXABpGM5e0LYfVKWVyGrb5pM6EdvuxVKcIoqZvzFw_yuQYvyyp_7mBVC2Kn-w1ZMarzRsPFmlDNAI1fkDp7oehiCMA5hVwYSEptWZL84G3NYrSLhoXK0JUqTjqHE0F92gHmaWrhoPLecI677s9xHzmKnpv31ducfgFVHuoUwBtO8qoSs9Avg3hb8sQVwUZgdDev2f6e7miSqK5X_-gHAyeE9MQbBY9LlYuHSaISB9qtOpIVMRX6c9UYv3_vbSdKQ3hRIyGk8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecjKfIipRtaClNbqlzdGAT48sbFDrKrejFjhqODdee45ksz6UkrwT2fDtUIx8SoN3Bx3r30Iji-NwJh5vKg57_kItTbU4AFtudQT9Wj9vtICjYM50lTriCpWfKN9IzhPJhDirsnroaJCwwpr6I1Lt7dg48ejJb1LRWJ3nz0yubzWHfijJHWkvublPlOdf5bFibyo6-XKUA6Dr8KeN6t5JUwrZslREzfvTDukGI2UZ4omhmjtk5giFHHIpIZISBgyaFq8JYVZRG8l8QGUqRG3B4F-OoM87gVmYloQXkjzc3D3TP0bCnlvwjhKzn10XFmVqm3Km_JYqFYJ9KmqVxeDJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بارش ۵ متری برف در یکی از استان‌های ترکیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/664552" target="_blank">📅 14:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664550">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وپنجم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای عبدالکریم حاجی‌زاده که در روز ولادت حضرت زهرا(ص) و بعد از دل شکستگی و بحث با مادر در اثر تصادف روح از بدنش جدا می‌شود و شاهد عذاب و سوختن انسان‌ها به دلیل گناهان مختلف آنها شده و با گذر کردن از آن بیابان به باغ پر از میوه قدم می‌گذارد و با چشیدن طعم به یادماندنی میوه‌های بهشتی بعد از بازگشت به دنیا میلی به خوردن میوه‌های دنیایی ندارد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: عبدالکریم حاجی‌زاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/664550" target="_blank">📅 14:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664548">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ee6d61a4.mp4?token=eHJCFhpB5tPjCyIIiRrO3e4hJmDdgBuQrixzh5YyuEmoZFJy9Nf4XHP58ymdiDyhNOVjbCKgdxDjdlP1ZFw6BLUmxpqv99HQgXy6MUplGD6eL8P593ANk8oEm8PeSrz9iVC33RqJ3umycRRe8KvDQ2ZvUHACJ0VvzyWL6VkBe7dKzlfYi3l25pW82s9_1oYOTxsQe5oll4oOx1_q7qZfazBjezHouRmrPNjnXrya3SeyHBmvrsGkt_7oN9N7Wm9gkcN09q3EeYyeQr6g7yLBoE2A0b0n6tvMTQYjyFXeU_XwbeL0itgFGDdZsuWT-ilkKljlynIFGLR36tsQZ55TpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ee6d61a4.mp4?token=eHJCFhpB5tPjCyIIiRrO3e4hJmDdgBuQrixzh5YyuEmoZFJy9Nf4XHP58ymdiDyhNOVjbCKgdxDjdlP1ZFw6BLUmxpqv99HQgXy6MUplGD6eL8P593ANk8oEm8PeSrz9iVC33RqJ3umycRRe8KvDQ2ZvUHACJ0VvzyWL6VkBe7dKzlfYi3l25pW82s9_1oYOTxsQe5oll4oOx1_q7qZfazBjezHouRmrPNjnXrya3SeyHBmvrsGkt_7oN9N7Wm9gkcN09q3EeYyeQr6g7yLBoE2A0b0n6tvMTQYjyFXeU_XwbeL0itgFGDdZsuWT-ilkKljlynIFGLR36tsQZ55TpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری جان کری از اصرار نتانیاهو برای بمباران ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/664548" target="_blank">📅 13:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664547">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9bedbfb78.mp4?token=C4MNic8bddl5wNR3oLEtW5vHFL4qPZVnGAFsj6kl5sxWof4W2B3IBfrkF6CzOelfa8HzrBUphP1kwYRIFqX0P-_cabvTgiaJY-pu-B-_gJDiLFu8emN1pUjyq82OjkcLxQE_Enq6lHI5QKNQ8LFUjL0mUJu1jp2mK50SF8jbnohzscdDqKhCpKZ6BgOi9nSw5aom4HR2yO1TiuVzNYeUXlizxs2B8jJYpPuCUCShRKOvFhfuwLL_vpn5R2ineExxpfhaKI3bHW1P7LlHXBeiTYbrafU0_7essqRqC0d_88bnZW8JfYRVb7Eq6kk_Eh9W_Gq6XnSMzEvQbGI1mkdfhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9bedbfb78.mp4?token=C4MNic8bddl5wNR3oLEtW5vHFL4qPZVnGAFsj6kl5sxWof4W2B3IBfrkF6CzOelfa8HzrBUphP1kwYRIFqX0P-_cabvTgiaJY-pu-B-_gJDiLFu8emN1pUjyq82OjkcLxQE_Enq6lHI5QKNQ8LFUjL0mUJu1jp2mK50SF8jbnohzscdDqKhCpKZ6BgOi9nSw5aom4HR2yO1TiuVzNYeUXlizxs2B8jJYpPuCUCShRKOvFhfuwLL_vpn5R2ineExxpfhaKI3bHW1P7LlHXBeiTYbrafU0_7essqRqC0d_88bnZW8JfYRVb7Eq6kk_Eh9W_Gq6XnSMzEvQbGI1mkdfhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان کری، وزیرخارجه سابق آمریکا: تنش‌ها با ایران قابل اجتناب بود و ترامپ تنها باید برای مذاکره بر سر تغییرات مدنظرش اعلام آمادگی می‌کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/664547" target="_blank">📅 13:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664546">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏆
به انتخاب فیفا؛ ۱۲ گل برتر مرحله گروهی جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/664546" target="_blank">📅 13:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664545">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90205e642.mp4?token=BFoRLmSHTmIdowIMGtzjq6lvUbQorQVEK1p-AyMQaJNbqJw3bSPTZFlaLvA5RGs7Jr9wEjikwPfXTAjwpMbUcL5PjNgmsD4naFJxC_mUHtt0c5n2HoBe83g2tf6RAXdmZ8Ll_xFPHog9EWX3xI8jA0Xnq-6kA_eAEo7S66lKdFt4-q0B6fnRLIwyrPa0zA90CJ94TY8RU5OKFnRgUEhLZcJlh8lcv6ZypCjHIr1A7_hIBCRfAteTtCXswgKru2bm_yoShoQ0HGE5QfJ6AepmwdO-idXh6IW0vnVm5u_b2_2V4mjy7iwG7OGvZL4javy58ACXfG3HrFjeMW2mHqt6xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90205e642.mp4?token=BFoRLmSHTmIdowIMGtzjq6lvUbQorQVEK1p-AyMQaJNbqJw3bSPTZFlaLvA5RGs7Jr9wEjikwPfXTAjwpMbUcL5PjNgmsD4naFJxC_mUHtt0c5n2HoBe83g2tf6RAXdmZ8Ll_xFPHog9EWX3xI8jA0Xnq-6kA_eAEo7S66lKdFt4-q0B6fnRLIwyrPa0zA90CJ94TY8RU5OKFnRgUEhLZcJlh8lcv6ZypCjHIr1A7_hIBCRfAteTtCXswgKru2bm_yoShoQ0HGE5QfJ6AepmwdO-idXh6IW0vnVm5u_b2_2V4mjy7iwG7OGvZL4javy58ACXfG3HrFjeMW2mHqt6xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳۷ سال برای ایران؛ روایتی که باید حتما دید
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664545" target="_blank">📅 13:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
غریب‌آبادی: نشست فنی این هفته برگزار نمی‌شود
معاون حقوقی و بین‌المللی وزارت خارجه:
🔹
نشست‌های فنی کارگروه‌ها این هفته برنامه‌ریزی نشده و خبر برگزاری گفت‌وگوها در دوحه تأیید نمی‌شود؛ رایزنی‌ها از طریق قطر و کشورهای میانجی ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/664543" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664542">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4543ba32.mp4?token=ama8Fpn_YUQgTpJzXrIec3y7QZUdxOR3vKPXhyOEbHcxB4u6gCBw3dLiVBZ5dj4EXoCvAdKll5CkSw8krexjJLPz5O57U7I3i0AJawA36nVX-u6CHQ0G0BWBfzH7pHc2vbameQNB7DLlGUIkCpQD9L_iAneWvR_t5T4ULqZXpFtkHNEIcmHl3ej_udxl_rUvzLmO7cWvyaeapYO2AYnVXmv89OInCvgoGc6C7eW9jG5HVPo0PLzA0SBmy7yOhYyF8JGZhLi3KfXFJxpA-ZOxr9p6oZZEpOut6Kk4md_Nd3LLYLQFgevNrBqKRujrosyl6NIRvkAJfz0CDJi17B39wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4543ba32.mp4?token=ama8Fpn_YUQgTpJzXrIec3y7QZUdxOR3vKPXhyOEbHcxB4u6gCBw3dLiVBZ5dj4EXoCvAdKll5CkSw8krexjJLPz5O57U7I3i0AJawA36nVX-u6CHQ0G0BWBfzH7pHc2vbameQNB7DLlGUIkCpQD9L_iAneWvR_t5T4ULqZXpFtkHNEIcmHl3ej_udxl_rUvzLmO7cWvyaeapYO2AYnVXmv89OInCvgoGc6C7eW9jG5HVPo0PLzA0SBmy7yOhYyF8JGZhLi3KfXFJxpA-ZOxr9p6oZZEpOut6Kk4md_Nd3LLYLQFgevNrBqKRujrosyl6NIRvkAJfz0CDJi17B39wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای جالب یک دستگاه سی‌تی‌اسکن بدون پوشش بیرونی و اجزای داخلی آن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/664542" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSvZwgkSBMeEjVC-aFTUcyndz-c3_XKZZb8lYmJVwUmzVFj7Ge2Wa34KNRIrBWWAHwKEki1ohofcy6d3CbZIUy5my-lCLNlE_mGmeqdFYb3af1ey_0H3UWHJ-FuX_VrjeSzVvyedjmU6cbYxg_TVUFqHiyCdcWtv-Ma2XEpXJCm_9e3O5_-2v_Gr6SsvpJlS2YMzkvaNbvmOJQXqmb5aZ0k0USHPh-6oK0mbYDtV7Y5c9M8Q9wpimdkpK_ah_XaPMlase3T5bXMbwEU8B7akzOFE1St5pHZVSLr7zaiQ0RMPfajZq01AqVp5FL9fz07VCd46TGwe6HyXel_8ZkMnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام اژه‌ای به رهبر انقلاب: خود را ملزم به اجرای فرامین واجب‌الاتباع حضرت‌عالی می‌دانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/664541" target="_blank">📅 13:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664537">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL_K_9giA6TZ14GGMkuhWVNB7CYK6GFZ9WnlfkxuCLGOyc19OUZfB2BECN-a7JAbgb6tzYzwcbdTqngzgiEM3Igs5FULkYZQ6xaeusoUGm8tnpYzQZ6C_c3x30loyLA-jZQB84kYDCte__5FmKER1jLoNKhxjlAoudb_iNqi4D1TOcB2iVoytlOhQKmx6cmU4Ds7_w-5-k4eojbq0YJPkLWPlUtSLJDWaU8mhbtv-yS8ftDhkGJZ0I-y_oI1qz6_BuZUiVePTFiddL-bHJb_5nKEzNP0UMV4MemcxEpJTE_-6_VUV8aVLn2_i0DsINj4mP-AOa9JLOSGPvJpLw-_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش مهدی قایدی بعد از حذف ایران از جام جهانی
🔹
عشق به این پیراهن، با یک شکست یا یک حذف از بین نمی‌رود. ما کنار هم ماندیم، چون دوست داشتن فقط برای روزهای برد نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/664537" target="_blank">📅 13:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664536">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره محیط‌زیستی اتاق تهران؛
خدمتی برای افزایش تاب‌آوری کسب‌وکارها
🔺
اتاق بازرگانی تهران با ارائه مشاوره تخصصی و رایگان در حوزه محیط‌زیست، به بنگاه‌های اقتصادی کمک می‌کند با مدیریت بهینه منابع، هزینه‌ها را کاهش داده و تاب‌آوری خود را در شرایط بحران و پسابحران افزایش دهند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲ (۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/664536" target="_blank">📅 13:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664535">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiO4h3KgBaAm9Mzc0Y_1gYiVe6cUd_yHbqPrhTNOj62798i4DO2fqtHTE1RgqnuKvyb6hiSrqe2ySRwXvu44pv9bIaoqORBG6gHbI330_DeQCwLX1ZzMvBifnZuEPX5I7q4ntADZPr6tLFYB7MfR17WxLkNW0Kjz9vL1RU6x1okxPngCLeyD8rbWN2y4WB4CSiTizAxzTNGEp7s40je5ti-FwXzSZi--xWIwioS5jb31k95K6yXnoIPHZHH1iWfkqLa-xinyVPUzLqgBSsjk18NrHrwIqlJ9tu6uUlYDJvOp9CLry5w1d09l5g-7yvHtMBgoscQaGEkxVtB43tezlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حضور سعید عزت‌اللهی از تیم ملی ایران
🔹
رتبه‌بندی فیفا از ۱۰ بازیکن برتر در بخش دفاعی پس از پایان دور گروهی رقابت‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/664535" target="_blank">📅 12:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664534">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1e624ef0.mp4?token=d4OR1T6O-FV_rrGD0v5k9wrdb-jI0GzJkQRVgAXa0rSDARUb8Z11EaZ3TqZTeltcec6N2b06kBU-W3uKncifWTdA1naEIidCLAEDPE6LPhdjxnq5qAlaqqyTfL-YMuxGWnTzQop8W4QjqSSU4ooXZnFjVHQklS8wvvcp8kjI6faWyOveVd5iy3tqKFXs59NHzTIc5HvoeAHEa4c1f5nTyuBBjXl9zGwuSG66SgYqOV7gw9S_UsmtejRwbAdkGReNTg9Zw7HlitMkd68zEEXLZ16Q_MpME6nnWnh_43AY0KUITGK2d7804e2liHLb96i4BWPgnEWbtLg49kln6nvOKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1e624ef0.mp4?token=d4OR1T6O-FV_rrGD0v5k9wrdb-jI0GzJkQRVgAXa0rSDARUb8Z11EaZ3TqZTeltcec6N2b06kBU-W3uKncifWTdA1naEIidCLAEDPE6LPhdjxnq5qAlaqqyTfL-YMuxGWnTzQop8W4QjqSSU4ooXZnFjVHQklS8wvvcp8kjI6faWyOveVd5iy3tqKFXs59NHzTIc5HvoeAHEa4c1f5nTyuBBjXl9zGwuSG66SgYqOV7gw9S_UsmtejRwbAdkGReNTg9Zw7HlitMkd68zEEXLZ16Q_MpME6nnWnh_43AY0KUITGK2d7804e2liHLb96i4BWPgnEWbtLg49kln6nvOKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور ترکیه، اردوغان: آنچه در غزه رخ داده یک نسل‌کشی است و اسرائیل قطعاً بابت کشتار کودکان و غیرنظامیان پاسخگو خواهد شد؛ ما نمی‌توانیم در برابر این جنایت سکوت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/664534" target="_blank">📅 12:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664532">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00387c6b1.mp4?token=TUJ3BuhWmeemTYIdiiZQJePV_fH-vuCdfaYY4gXhM5wphrwLddXbefz_6T_DgfnrYDNO4UwW-K8AhdEikMqbNb7OnB-B60kpICe0AiYzBoBYUIrXvjaU1omPTiL90KKeCYNSxKTYyfmB9GMNXMFlnv-Jb2eI6EpizCq2udckWSL5AAGCLHh7T4-YlN6VjgpSPupA_H5xhBxQW0ODVTEMBriE9Aja1HHNAXuQNPPJScVLPuzmWlV_Lw2PEijybOVYjpCEls9YdVlk8pkNK7Uhd6mxD3o5ob_AbB1tf6YDPJ2XQMiUUdywdVSgdpgsEQDfFDXVzWnfBwOOvuFlh0mLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00387c6b1.mp4?token=TUJ3BuhWmeemTYIdiiZQJePV_fH-vuCdfaYY4gXhM5wphrwLddXbefz_6T_DgfnrYDNO4UwW-K8AhdEikMqbNb7OnB-B60kpICe0AiYzBoBYUIrXvjaU1omPTiL90KKeCYNSxKTYyfmB9GMNXMFlnv-Jb2eI6EpizCq2udckWSL5AAGCLHh7T4-YlN6VjgpSPupA_H5xhBxQW0ODVTEMBriE9Aja1HHNAXuQNPPJScVLPuzmWlV_Lw2PEijybOVYjpCEls9YdVlk8pkNK7Uhd6mxD3o5ob_AbB1tf6YDPJ2XQMiUUdywdVSgdpgsEQDfFDXVzWnfBwOOvuFlh0mLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بنزین هم در روسیه سهمیه‌بندی شد!
🔹
پس از حملات اوکراین؛ روسیه در برخی مناطق بنزین را سهمیه‌ای و سوخت‌گیری را به ۳۰ لیتر محدود کرده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/664532" target="_blank">📅 12:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664525">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGue9mktf_kTLURL1NLnacIPDxgbCvRaQ7M_HyKkYQCVLmqrycqz16wFcJkfksO-faVCplKuPDbH8YakMMm8VK-bwOBJX6MZr4OTyquhmKvHwVWT-sLAhhyEeQb7Lj6tE6u4XR08oZ1EKwDhGLKqpjEy_m5-Wn3v4SWSSKLHCwh5Fr_yX0jv8nGmL8VD3RGEWCr1onH-66rvHvzMyBg1qU7urFuzvQS-vngJm0kFyCWtoKdBnJ34tNhZ8BWdlsx3Hte0ram2KsTQI1EgBzNSI3hQZh2e5S_SnUBbZjUn635WB0zW-kwfD7zSQI0cN0SDcJiEHYcZ7X0DLMoDQ_ViPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBFF1k0OZMDT3NeLDSeP6cum4Ywf9N9ZzXwzRATcO8vK_eWV43kjmZAecRxauMVq8NUs97UT3PKWqcXhD1fILbNwJc9GLmZgOH1ZRKpoTAPSqI4Xo7ZsgGABzzqkGzteQQHMLIzjcTLOoTGq1_dJq8fEWBZPDxlfMKDwsPYEwAZ41p2FaTEzoE94689wUe33SbxktsDVq0-kdonJXv26Cxd-_3fYnjZ8vpCZGhksoFmIn39rK6oQSblbmGCGy4cWP-prgrpc6aXXhUpifzpo-GEEqwL50nfazDZaJQlOtbI5D5FKZQR8-I2Jr-ngSqxnngeudOs9vQK_u5s9xyokOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCt6oZXoNMRzgPl6Z--zHqf2l8bw5vydAxCv7Dg9iDCJcmJGE0UF9bJBcRpGvXe7rzD5Zbvq4UVMdu3qreGrLNAe9w6RlB6k60EM3YRyMV1-KKT2uOCCS6bLJJjwKbXsV3bOrwzPGaBayKisn5wZkGJIbwKYzk-Db2lFaAa-IXRsQcVwLY4LZrCbbqxEPk7D-AwBpgLDLuamk2dd4dAujynCRDYX5LVMvvTH37FQQtxG9-w2UWT71TlktS6r6q5Uggz3tWcY96eS-Z0nfl9T_vG5ctU0rifpr9dzZeKS2G8wIJMCJbCEjzf45Cw8mP8sWpSfp4uPyZ8ZV7AUf7t_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RL8jMJAOSoXp_EnARC6C4JEjospsx9vMmIOqIq1VSSSQ-asQuNysLOvS5IipXclmMel_gVw3NcVVtu6iNgyEvWltExbqV03v46Avq66OUNDWHyPgSFAbEPm-TrOkQfkLHWbLZRg1Hbpizgf7BnqTInpfWqDqXf_nLOhhCcmnOPmQ1FtWzLjoaHCuO7pzgdMNBamuYvp1eppoIIBbX2XmqibHNkXeAgdHypL50riU06R7wXBiLgj3S9C5aknifCD-Zeuo83eGd_u04pMk1UB-CUS8yEpI8DLIXFV4sCjuL5p9zv8IjLA5UibB4JCi558eJ_bVGVpMMDbdr-iEp-4ZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiOSRsJhcsirItK_Ejd6Z6cubRl0PNBCpBoQbHK1bWUpRi2To3aUt6XOZGrxTNeYyoSZunUgd-wPTFg869TWj1raYYXJR69nX1rM3wq0oUHR8KA3y7-tyC2OPdWuk6OZLKmROI5VhFcoLmjpBic1-7xBGDdx9-7zd2mMpZs-n0mKzz_mowvpyME50wdyObwF4lti1YoG9iW-6splF_pTOuMGRI13JXdMeMSdHvwfKWQ6j2JyPs-q4EveD1rdanYcd91j_9liFXpZf-zPr0ediYQhhSp7LjZ9MH_d9RGXWMF59sOF-msonUnJyjOpZkfgTJVY7J0w8ARYk-VPYw_Nbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKlamH1Brhw7fM4b3QFZaKH1uALb6aczPPbl0ALDBJ9QjznMvoXtuFCB6uWK3bp55HG6J04P2eIiBCJcgu84cSRjlbTwYcF7GLyEcJH0P-4X4DHAFlfdLxdt4HcqieYTBHI9fQSHnDqg6OJ_Y980_vgydh4lnKq2C-wCw1XUacZa3ysp7gsr20ndZiCdaZH5GivPFOStmWg6WFffd2EFhX304mIhEmZo2mmX0wWEipvp6F10EOGUbMeHiq0zDi9qylV0I1RjWEoc0THeqS3Bwj0se5SO8eHDWpNiALf7eetB2Id1Nh1D47NWtixvslu7rx95zYxKL62Dhd1Khh2MZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbzh2SBwJfmKmpCaqZPLHx0lav5zJY-aCvdlajDYDoNJvBqaZSN37OP9aqJD7tpWU5p8LMCN_pykxxrT5u7kckAZtyA1e3PpmqxYzKVPg8DR_Kuyh8zSMHY8VO8-LWSXiX1u9thjtyAGrmZf-uwnLrjlESuSygOCjlrfa4BDj_SvmilqXR6RCreeNW8jg0_i17afxA8r-zSYs729uBEQC9JYjGCjl98V6P8nKb2hx8fwD_JfStKdGm6WBLXJahUmDy_lfk1wbJZioD0UC3V8iJZv2cImFlxqte9F6576CtcL3F3xOWOetfRC6JGBcxE1daj5xPHgxsslFOcyxlpQfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان حسینی
🔹
قاب‌هایی از شهر شما؛ خانه‌ها و کوچه‌هایی که با پرچم‌های عزای امام حسین (ع) رنگ و بوی محرم گرفته و جلوه‌ای از ارادت حسینی را به نمایش گذاشته‌اند.
🔸
تصاویر خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/664525" target="_blank">📅 12:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664524">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae801529a.mp4?token=hYj1YrMl6hm5bcxcm32X7j8mhQ1S8keyN9IKmaMtzeYo9O-XYodr3c8YOEd8x_XvBUbJpPiQrQA2wv1-A35UEo2ZiQCBmZES_VzG90Q8Y9YNOYF1o_Q0shO9ItNd_hIc5o5j0mzQL7OegnUEO0EJibLn6ZF-LI_BrxQRlKN82VhN-UWQha07tNXJlT2cSpGaDeKzsxrAiGgOEgcqH60iqbxXCS_i55DvNLrpxM84Lo3vJPJhxu489NX69vLOQiBYA-MBMnZLKeg8DcsU_fEfoX3tfdXw7iC53iMzg3itDstuFsicdsSCqKZFk52qv6as6Nzlx1RSBuX8-n5OmcqnNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae801529a.mp4?token=hYj1YrMl6hm5bcxcm32X7j8mhQ1S8keyN9IKmaMtzeYo9O-XYodr3c8YOEd8x_XvBUbJpPiQrQA2wv1-A35UEo2ZiQCBmZES_VzG90Q8Y9YNOYF1o_Q0shO9ItNd_hIc5o5j0mzQL7OegnUEO0EJibLn6ZF-LI_BrxQRlKN82VhN-UWQha07tNXJlT2cSpGaDeKzsxrAiGgOEgcqH60iqbxXCS_i55DvNLrpxM84Lo3vJPJhxu489NX69vLOQiBYA-MBMnZLKeg8DcsU_fEfoX3tfdXw7iC53iMzg3itDstuFsicdsSCqKZFk52qv6as6Nzlx1RSBuX8-n5OmcqnNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از پیامدهای غذا دادن به حیات‌وحش و رهاسازی پسماندهای غذایی در طبیعت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/664524" target="_blank">📅 12:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664522">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mteA5hPbaMgAmdkuWgXokHjiQQ44I_Ix-519p5kodZgVm6LnrsKVcsqXyoL-K4CmsACZLWnzhyyWnjUdDVtswwuLj2Ld2H3Z8M984z06MmNc6U-OLPf-URwaZF4vaWwMRD5VgV3bBhaKmU3nA9KReHOGwpRfTDkGm1RXxfvTmFSQfiEhwnrn0FCYSlRHMwlm33JnKeF9382biaaRA_BzcjjhDLzNn3ws3vBOMeuMBcKZbPgbqgblxqvI_6Gp_vhpkX3_jS5-B9QrbCClrkcUeGdDI9VweIba6ZA4KN5ZPjphDPPk_LiavYD6MI6uidJHvWcw8aFGbE6DgEnkRQc_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای رابطه جنسی آقای مدیر و منشی‌اش/ دوربین مداربسته همه چیز را لو داد + عکس
🔹
رابطه جنسی یک مدیر با منشی اش سبب یک رسوایی بزرگ در عراق شد.
اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3226323</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/664522" target="_blank">📅 12:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664520">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdeLzSIGZ6hj67PHIMDoIjbIqtSuLdM_SyxNKJO7jjmzcMpYmpLZUQ2hv_RkF7bQfSIyaR2GiIHgRr2ApALm0xxpvt0Z0tYSlsIvZjPzGKeZ_AOQGdbHLXxD5Wba11B552xBOWXBR-vHJvzsykawD2Oil1ZmyT2t05ry1Wl_kFCkZ_9grZ-bFtTQoYSnU6tM6VWKnwmRz6nYi0i-wCRJF74UPaYOAF-CRrak55IFoKZJeUH219uCMGIyvZeYJDTXv765A6NrvR129f69kcK1WWiW_f5nd5KJ1tiDjXrj99LoB2NmJBTP157YotsMNcNnDb0R7ngagjWQUEWlZTOM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از یک پست تا یک پرونده؛ ردپای دیجیتال چگونه زندگی ما را تحت تأثیر قرار می‌دهد؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/664520" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

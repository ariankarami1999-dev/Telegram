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
<img src="https://cdn4.telesco.pe/file/AISTfjBj_wPqBOHU0SBZqdOVDami_CwZ3xI_njsOFyyzxr_Y1SmbENZ8jRcnadOBhR_PN4SHZLb2oVdOlEAs1oqlos-FkDk94Ilx1oOG2g7HnhpbRIfyuhSDUVWTkxm-p8Oz9BwP5oSG14NlDWRiEwMwCWAoBFfiwJJ4ByNHhmRJDZWRMNgDsDKpiw7jV0TigOVapRJYPAXds6nUQ_5iEiLyUDnetGQRT3ZnkxmmenOe0whvL37POgd2QiWJYBmezwoaqLanmG1SoG4LeWlfhnoBxMYPsrA4_0NMXW1jHD4DnOk2PS4Xe8yN8V3pjBZOrSctAl3Os2-x2KWKCq_0eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.23M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 03:27:50</div>
<hr>

<div class="tg-post" id="msg-680171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/equWS9ykgq5iCtSAC72EuBNKvfdCSE7Kqbgbtj_c84mrIHtU3dp3ASQqkyFqAyTUN-Mmi7TXuhKSCbu7LWMJWoSmA4WTxcyBL8cmU0lCD7wZiryVpkNl3xexW5geYYJn1GmT8gDJr3e2kjGbB50ErAViOiOO3P_SMPwFsUS_UgaxVYrE9T9DEhGFomjDN2ORWJLFDl93I_G5hLMCthx3kU1O9YGJEPKEuTRJO5ad8C7wJ14WpIqNE6gQbQv9x1CtL8BTN6PK14vczY500lnxUOfsWrOi9LEzB_Jk7Qm5WJCd_K2Lgkis3WQd6jjpwgmOUeHWH4nOLYbQyScBJArvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حرکت نفتکش‌های خالی عربستان به سوی تنگه هرمز
کلش ریپورت:
🔹
بیش از ۱۵ نفتکش مرتبط با عربستان سعودی، که اکثراً VLCCهای خالی هستند، به سمت شمال غربی به سمت عمان/امارات متحده عربی و خلیج فارس در حرکتند.
🔹
ناوگان ترانزیت نفت عربستان توان عبور از باب‌المندب را ندارند و در تنگه هرمز هم باید ترتیبات ایرانی را رعایت کنند‌.
🔹
به نظر می‌رسد این نفتکش‌ها برای بارگیری نفت در خلیج فارس یا انتقال کشتی به کشتی در خارج از تنگه مستقر شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/680171" target="_blank">📅 02:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در شهر  مأرب یمن
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/akhbarefori/680170" target="_blank">📅 02:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680169">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
کشته شدن یک مقام ارشد نظامی در شرق لیبی بر اثر انفجار
🔹
مقامات شرق لیبی از کشته شدن فوزی المنصوریفرمانده یگان اطلاعات نظامی  بر اثر  انفجار بمب دست ساز کار گذاشته شده در خودروی وی در بنغازی خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/680169" target="_blank">📅 01:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در شهر  مأرب یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/680168" target="_blank">📅 01:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c50bf2a37.mp4?token=hXa1CeGCBbbYlTu08gIbdPYNyCSiceDoLT8p2qvHxQEICp638vfKCmz8uxAebA0GcYEt9S26wO5sqNyp7WAf5xPu6HB2z1clYc2Bg4OuNE-2vxk6c1Y7AdRK61GDxcMBXmRsZcESnjmHLUfkuZPYdYd_WRugIFfjm3DpK8Rgwph9U0TQecNAw5OVkj62AEXZhovK64JD8FSUmFtgFLHqiJlQyA8rIr1pmX53BW-Mu0dciU3rqPsuQj4Y4TtiWqTo9hwGk6f3gCpC9kKnaQLEGuqF-ZbavEY1V4QFiiat_V4stvlGKde2w7yIAY0ylYDam7QQcRbz9k8zj-kX8EIZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c50bf2a37.mp4?token=hXa1CeGCBbbYlTu08gIbdPYNyCSiceDoLT8p2qvHxQEICp638vfKCmz8uxAebA0GcYEt9S26wO5sqNyp7WAf5xPu6HB2z1clYc2Bg4OuNE-2vxk6c1Y7AdRK61GDxcMBXmRsZcESnjmHLUfkuZPYdYd_WRugIFfjm3DpK8Rgwph9U0TQecNAw5OVkj62AEXZhovK64JD8FSUmFtgFLHqiJlQyA8rIr1pmX53BW-Mu0dciU3rqPsuQj4Y4TtiWqTo9hwGk6f3gCpC9kKnaQLEGuqF-ZbavEY1V4QFiiat_V4stvlGKde2w7yIAY0ylYDam7QQcRbz9k8zj-kX8EIZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع چندین انفجار در مناطق مختلف کی‌یف پایتخت اوکراین
🔹
منابع خبری از وقوع چندین انفجار در مناطق مختلف کی‌یف پایتخت اوکراین خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/680167" target="_blank">📅 01:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
حکومت نظامی در شهر عین‌العرب سوریه
🔹
نهاد امنیت داخلی حکومت حاکم بر سوریه از منع موقت رفت و آمد در شهر عین العرب (کوبانی) خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/680166" target="_blank">📅 01:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادامه آتش سوزی در یک مخزن سوخت در پالایشگاه زاویه لیبی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/680165" target="_blank">📅 01:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R26vwlxhNlWw1vSVsKzKl5pFSM_0RkbmXUcZdgqZAw1Wrl6DrzQORSxFOKV5jmPnHWmz-isj-q63zztNqURNm5j2VgsnyUq5m-esk92vXjaG9JUwntaVr6f1pVBIv5I4auns19vwimpxT0Tz_9CBuRZ0b4L_1BXmNo5bgW3VPq1g6qteYmkrBiJCcufmR1xs6XiXJZk4vO0cTh-1gja-OdLgqdd5wy4xzK9e9kEREeIUbfXDKMBwvuWLm12UaLWiBuvw9f8Ts2vjBlX5ceQckhs2g0nPD78NqjpjCNXd371vQfjgaBDEp1spS0GJtCOMOKARwM6XjCkj_uapC01mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لشکرکشی نفتکش‌های عربستانی به سوی تنگۀ هرمز
🔹
گروهی از نفتکش‌های مرتبط با عربستان از دریای عمان به سمت تنگۀ هرمز روانه‌ شده‌اند.
🔹
ناوگان ترانزیت نفت عربستان توان عبور از باب‌المندب را ندارند و در تنگۀ هرمز هم باید ترتیبات ایرانی را رعایت کنند‌.
🔹
تنها راه بدون نظارت ایران و محور مقاومت برای نفتکش‌های عربستانی حرکت از کانال سوئز، دورزدن آفریقا و گذر از دماغۀ امیدنیک است که طول سفر را ۲۵ روز افزایش می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/680164" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrQlz-V4HlXPEXhhGKjoR1YEE6AqOsNvJrTqrITZSy6RzbGFV3k_PtqTXoB3O4THpXm1Kd2uHRzxMngxYoLFkf-YUi_tImjBpyHCr2DG__6eeGmDHEr3OLJv6fwdeAoLveYLH6qSN76FriJSeMW8tx7YACBAp_UkDuWb1_FUF_Lh-olwxSuAgP1xDcuAVOcG0hCIONFczd3lOdfUa03Fb-9tu463PRffhZMjRCeaaFwhR94F-JpnQDgKl0akY9wXXhs1l7jQc73ndiKISKvOoVuiMoABvb6scGx-5O40BReaOFroBtWR4Ep4Sy25GKwr87FgMH54TTfXTWsXwBUD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرایش جدید فرماندهی
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های شش تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند. بر اساس این احکام، سردار سرلشکر خلبان پاسدار علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح و امیر سرتیپ کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح تعیین شدند.
همچنین سردار سرتیپ پاسدار احمد وحیدی با اعطای درجه سرلشکری عهده‌دار فرماندهی کل سپاه پاسداران انقلاب اسلامی شد و سردار سرلشکر پاسدار مصطفی ایزدی مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفت. در ادامه این احکام، مسئولیت فرماندهی نیروی دریایی سپاه به سردار دریادار پاسدار علی عظمایی و ریاست سازمان بسیج مستضعفین به حجت‌الاسلام والمسلمین حسین طائب محول شد.
🔹
هشتصدوسی‌‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/680163" target="_blank">📅 00:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سردار دقیقی، مشاور فرمانده سپاه: نباید اجازه دهیم دشمن با دوقطبی‌سازی میان جریان‌های سیاسی، وحدت مردم را خدشه‌دار کند/ قدرت نیروهای مسلح، مردم و دیپلماسی باید در نهایت به تقویت امنیت ملی ایران منجر شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/680162" target="_blank">📅 00:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
حملات توپخانه‌ای مزدوران عربستان به روستاهای تعز یمن
🔹
شبکه المسیره از حملات توپخانه‌ای مزدوران عربستان به روستاهایی در استان تعز یمن خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/680161" target="_blank">📅 00:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680160">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9009082601.mp4?token=jTCBWjq821V79TYGGTEJO0xB4EBOswfsGgWIcK1w-81e-GlPcZaaadhf5rt37ieR2kKfRuxsj62_8GZR72eNxhIdZO3IqAogCEOXGC9sIszEugguAW17r8m5xOKKP-ZoF9aWOJWONVVQt6UzV6QqOfz_ewatJZx4oklFIUfEZUjwbPEAgqjc3k_mksLFwOP4iMXg9eCy9n53fYSvlCbcZOV3GkjujVAre533pBMZF51zyB4d4epuijux_84aTFLQcMREws-gBpufOXBEd2LITpj2AwAusV6a4n89HmU92hJCL8VQt5lo4lDm4WkqBIhMpoxxQPWkoRUlDeZuenaoHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9009082601.mp4?token=jTCBWjq821V79TYGGTEJO0xB4EBOswfsGgWIcK1w-81e-GlPcZaaadhf5rt37ieR2kKfRuxsj62_8GZR72eNxhIdZO3IqAogCEOXGC9sIszEugguAW17r8m5xOKKP-ZoF9aWOJWONVVQt6UzV6QqOfz_ewatJZx4oklFIUfEZUjwbPEAgqjc3k_mksLFwOP4iMXg9eCy9n53fYSvlCbcZOV3GkjujVAre533pBMZF51zyB4d4epuijux_84aTFLQcMREws-gBpufOXBEd2LITpj2AwAusV6a4n89HmU92hJCL8VQt5lo4lDm4WkqBIhMpoxxQPWkoRUlDeZuenaoHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان حضرت ابراهیم رو اینجوری نشنیده بودید!
برنامه متفاوت پُلاریس رو در تلویزیون اینترنتی مدار ببینید
👇
▫️
https://youtu.be/4feAD2lqlHI?si=8_SmjCmzNJ7rwuSR
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/680160" target="_blank">📅 00:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680159">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12023699aa.mp4?token=d4L2A9tL6bkRptt2xkxmTjOYYPz26bcjj4fZByAbzb_FzI7xYX2-aGWAeeJFalrXhlxz7QPD6Vo1XK9ix3ACbGHr1TticACjsSgizY8hxnUmmm6gHeMRfKNY_d53Kzw2b4OhN7vBTNNlOnMS6YHy97DU4lQF3iwXVyAiDzrZm63M3vI1QUjXWzVVRK5SusIod47T6TYlT7mvZnk0-j1YQzwKvDHmseH3kzePZdxkLv-m87cpuzbnr0WW6V_15dpa_M4_REaRPS0sdUDQXt5beYAPg6cYo0NELUYsxxWbabz9FkHNk-m01oc3PolECXHcTxj2mfxL6CSSXnRk9LY2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12023699aa.mp4?token=d4L2A9tL6bkRptt2xkxmTjOYYPz26bcjj4fZByAbzb_FzI7xYX2-aGWAeeJFalrXhlxz7QPD6Vo1XK9ix3ACbGHr1TticACjsSgizY8hxnUmmm6gHeMRfKNY_d53Kzw2b4OhN7vBTNNlOnMS6YHy97DU4lQF3iwXVyAiDzrZm63M3vI1QUjXWzVVRK5SusIod47T6TYlT7mvZnk0-j1YQzwKvDHmseH3kzePZdxkLv-m87cpuzbnr0WW6V_15dpa_M4_REaRPS0sdUDQXt5beYAPg6cYo0NELUYsxxWbabz9FkHNk-m01oc3PolECXHcTxj2mfxL6CSSXnRk9LY2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز تحقیقات از متهمان اصلی پروندهٔ حمیدرضا رجب‌زاده / در تحقیقات اولیه متهمان به قتل اعتراف کردند  فراجا:
🔹
پس‌از دستگیری متهمان اصلی پروندهٔ حمیدرضا رجب‌زاده؛ تحقیقات و پی‌جویی، توسط کارآگاهانِ پلیس آگاهی در خصوص علت و چگونگی وقوع جنایت در جریان است. همچنین…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/680159" target="_blank">📅 00:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680158">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
اسرائیل در صربستان کارخانه تولید پهپاد تاسیس می‌کند
🔹
رژیم صهیونیستی قصد دارد در صربستان کارخانه تولید پهپاد راه اندازی کند.
🔹
شبکه ۱۲ تلویزیون رژیم صهیونیستی در گزارشی اعلام کرد که این مسئله را رئیس جمهور صربستان هم رسما اعلام و تاکید کرده است که این کارخانه بین ۱۵ تا ۲۰ سپتامبر راه اندازی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/680158" target="_blank">📅 00:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680157">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
گزافه‌گویی‌های فرستاده آمریکا به سازمان ملل علیه ایران
مایک والتز، فرستادهٔ آمریکا به سازمان ملل، در مصاحبه‌ای با شبکهٔ فاکس نیوز:
🔹
وقتی ایران پای میز مذاکره با مذاکره‌کنندگان ما می‌آید، صحبت از پول، پول، پول است. زیرا آنها بمباران‌ها را تحمل می‌کنند.
🔹
آنها به دنبال دسترسی به پول نقد و دارایی‌هایشان هستند که ما مسدود کرده‌ایم؛ این همان نقطهٔ فشار است.
🔹
این فشار همراه با محاصره، چیزی است که در نهایت باعث می‌شود ایران عقب‌نشینی کند. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/680157" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680156">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
رامین رضاییان: کنار خیابان می‌دویدم چون ساپینتو اجازۀ حضور در تمرین را به من نمی‌داد
بازیکن تیم ملی:
🔹
وقتی به استقلال آمدم به شرافتم قسم خوردم که با تمام وجود بازی خواهم کرد و خواهم جنگید.
🔹
واقعا تا زمانی که در استقلال بودم هم جنگیدم هم بیرون از زمین تعصب این تیم را داشتم.
🔹
قرار شد ۵ تا ۱۰ میلیارد بند فسخ قراردادم باشد اما مدیران باشگاه گفتند نیازی نیست و بند در نهایت ۱۰۰ میلیون تومان شد. جام جهانی را مدیون فولاد هستم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/680156" target="_blank">📅 00:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680155">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55b6ea6438.mp4?token=O9otvLXZhWva46RlaGtt8ENgWnQz9h8yr_GZZ3Td_usmj25OsWPIkpGm1KDc-lMtcSKxygBzKmo5Z3WH4yFdG1AJv47BcNcWGQwNUbZ1BQ8FX_xEGc5wDcjnL3F94uw6Y16TO7c48dxScQ50b9BvF4hjHUU0NxX37rvqdXltgIzr66xnpezdxiNVqhsLks-TuY0TCEpW--LkzRJs_5vj-2xWO8aRCOVh5C_XO--rROkMR0c7U84Xke5mYufsImsmmYQZokN9W5FH0b-1Am6EmdQSwV5QPSAVYOYeY1blRhC8U9xkAu3ju0enxUmjCn4k_SjFBh76nPUBOtWbklic9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55b6ea6438.mp4?token=O9otvLXZhWva46RlaGtt8ENgWnQz9h8yr_GZZ3Td_usmj25OsWPIkpGm1KDc-lMtcSKxygBzKmo5Z3WH4yFdG1AJv47BcNcWGQwNUbZ1BQ8FX_xEGc5wDcjnL3F94uw6Y16TO7c48dxScQ50b9BvF4hjHUU0NxX37rvqdXltgIzr66xnpezdxiNVqhsLks-TuY0TCEpW--LkzRJs_5vj-2xWO8aRCOVh5C_XO--rROkMR0c7U84Xke5mYufsImsmmYQZokN9W5FH0b-1Am6EmdQSwV5QPSAVYOYeY1blRhC8U9xkAu3ju0enxUmjCn4k_SjFBh76nPUBOtWbklic9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع انفجار در یک مخزن سوخت در لیبی
🔹
منابع خبری گزارش دادند چندین انفجار در یک مخزن سوخت در پالایشگاه الزاویه در لیبی رخ داده است، هنوز علت انفجارها مشخص نیست
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/680155" target="_blank">📅 00:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680154">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2ba2f533.mp4?token=kZCClHO5gVEkE9Fv5_jHrpb1K-2gV_Edeo94k29onbPZUvnTCdkQ_6L8IPxKb7Iqd-1iXDqsnQSxObv2KdS6Q04FvPHkUvm8cW-ENovYzFDGm2Pg-l-xjVsOaUPZdlLPI_19H1uC3-0ymeFIL-kT-hI8fyBmK9lUsvXIFps_kW2oRBcWes38s9UmzkO-jY7AiERpe5qjmfnWpnG4N3thb3AVeQ4ngf72fQxXN9PfFqyBQ1t2U_YXCpRWFZXiX6mJv1TT_QMN6TgctpHuAl0VNQRNijxzAYxSgzgPjSBajaa8KKIoLJeDukL33jNV58Enfp6dGjeRw_ZKqQ7VUAkQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2ba2f533.mp4?token=kZCClHO5gVEkE9Fv5_jHrpb1K-2gV_Edeo94k29onbPZUvnTCdkQ_6L8IPxKb7Iqd-1iXDqsnQSxObv2KdS6Q04FvPHkUvm8cW-ENovYzFDGm2Pg-l-xjVsOaUPZdlLPI_19H1uC3-0ymeFIL-kT-hI8fyBmK9lUsvXIFps_kW2oRBcWes38s9UmzkO-jY7AiERpe5qjmfnWpnG4N3thb3AVeQ4ngf72fQxXN9PfFqyBQ1t2U_YXCpRWFZXiX6mJv1TT_QMN6TgctpHuAl0VNQRNijxzAYxSgzgPjSBajaa8KKIoLJeDukL33jNV58Enfp6dGjeRw_ZKqQ7VUAkQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بذرها روی خط؛ گامی تازه برای کاشت منظم‌تر و بهره‌ورتر
🔹
در این روش، بذرها با فاصله‌ای مشخص روی نوارهای زیست‌تجزیه‌پذیر قرار می‌گیرند و سپس نوار در خاک کاشته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/680154" target="_blank">📅 00:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680153">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONGkQRrsN4R0Lq5DyARi1-22eyFHtI762BacF7jCjeYmzILkxiFhfChWilCspQvQow3dZ3cD1a2OOcwO407yC3A09zhMORjn0Egz31vNoPlg5xc6nYyo1pTDhe_7anjAcxbzY9qq61gc_ow_-E9xddZi341eDLOtM84w6QhSvKUpFH3EqwIu5y8q4PoEdOziA07H7XpGahxYi3C3o9xx6lGfm4UNg0fUaCrUFLK4pwdcSMMay8nQdlaPwtRGAeZ0rTaC9ZJLNkefn4KlWj4CgTyw3pJ8vmYyoTT2cpD9P4SSCQRCqzlovNc-yf3fm4GnRTROaF-cthGA_B2mTqNvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/akhbarefori/680153" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680152">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
صندوق‌های طلا به صرفه‌تر بودند یا بازار فیزیکی طلا؟
🔹
دوره پساجنگ برای صندوق‌های طلا نیز با بازدهی منفی همراه شد و هیچ‌کدام نتوانستند عملکرد مثبتی ثبت کنند.
🔹
با این حال، افت این صندوق‌ها از عقب‌نشینی بیش از ۸ درصدی بازار فیزیکی طلا و سکه کمتر بود و بخشی از زیان سرمایه‌گذاران را محدود کرد.
🔹
عملکرد صندوق‌ها در این دوره بین حدود ۲ درصد تا بیش از ۸ درصد افت متفاوت بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680152" target="_blank">📅 23:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680151">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
رئیس فدراسیون فوتبال: قصد داریم قرارداد قلعه‌نویی و کادرش را برای جام ملت‌های آسیا تمدید کنیم
🔹
به قلعه‌نویی ۷۰ میلیارد تومان پاداش جام جهانی دادیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/680151" target="_blank">📅 23:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680150">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سقوط صادرات فرش ایران از ۵۰۰ میلیون دلار به ۳۵ میلیون دلار
سپهرزاد، رئیس کمیسیون فرش دستباف کشور در اتاق اصناف ایران در
#گفتگو
با خبرفوری:
🔹
طبق آمار گمرک در سال ۱۴۰۴ میزان صادرات فرش دستباف معادل ۳۵ میلیون دلار بود، در حالی که در دهه ۷۰ و ۸۰ این رقم برابر با ۵۰۰ میلیون دلار در سال بود و تنها یکی از تجار ما در سال ۳۵ میلیون دلار صادر می‌کرد.
🔹
در سال ۲۰۰۰ سهم ایران در صادرات فرش در جهان به ۳۲ درصد و سهم هند به ۱۴ درصد می‌رسید و در سال ۲۰۱۹ این آمار برای ایران به ۸.۶ درصد و سهم هند به ۳۵ درصد رسید و در سال ۲۰۲۶ اصلا در این جدول نیستیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/680150" target="_blank">📅 23:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680149">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
توافق محرمانه آمریکا درباره سایت هسته‌ای سوریه
پایگاه خبری آکسیوس:
🔹
آژانس بین‌المللی انرژی اتمی به زودی مواد هسته‌ای ذخیره شده در یک سایت مخفی در سوریه را پس از دستیابی دولت دونالد ترامپ، رئیس‌جمهور آمریکا به تفاهم با سوریه و اسرائیل، از آنجا خارج خواهد کرد.
🔹
دولت ترامپ و آژانس بین‌المللی انرژی اتمی برای دستیابی به یک توافق دیپلماتیک جهت ایمن‌سازی این مواد و جلوگیری از تشدید تنش با اسرائیل، سوریه و احتمالا حتی ترکیه بر سر این سایت حساس، تلاش‌هایی انجام دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/680149" target="_blank">📅 23:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680148">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c45736caf.mp4?token=VbonF1QueRbExBpeqzYLxYELIUos4akwPI8aYadWpf462i20nXhBiWH0AGy7UlPs9_VN79qSOrpJVvgNy4AaiSfVJR5riNPHLIUn8sTsxO8p4z5hRhH5PCVGTOgFdLn8zfgLZFrpaE3wfBNQN_vbwGXXLCAC0N5U2iDf_aJlK5LaCG1OAYMywiBKKbc9gWKSBhY_bN4_Tf0NedkEYzwNXKTkd1y7MfUkUzVmN7mfSVLX-ZOazfMZiTMBlkZy1dLJEwkyFQhGtqVsceTvcTfrHGNi6X_wmuRyVIx4Mn99KnSx_g5frstEb4Y0WTLt5u6v-1H3mp106vw6qFTFp-UeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c45736caf.mp4?token=VbonF1QueRbExBpeqzYLxYELIUos4akwPI8aYadWpf462i20nXhBiWH0AGy7UlPs9_VN79qSOrpJVvgNy4AaiSfVJR5riNPHLIUn8sTsxO8p4z5hRhH5PCVGTOgFdLn8zfgLZFrpaE3wfBNQN_vbwGXXLCAC0N5U2iDf_aJlK5LaCG1OAYMywiBKKbc9gWKSBhY_bN4_Tf0NedkEYzwNXKTkd1y7MfUkUzVmN7mfSVLX-ZOazfMZiTMBlkZy1dLJEwkyFQhGtqVsceTvcTfrHGNi6X_wmuRyVIx4Mn99KnSx_g5frstEb4Y0WTLt5u6v-1H3mp106vw6qFTFp-UeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیاست ترامپ دیوانه: هر جا خوابت آمد؛ بخواب| وقتی رئیس‌جمهور آمریکا یک چرت مبسوط می‌زند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/680148" target="_blank">📅 23:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680147">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رایزنی تلفنی عراقچی و وزیر خارجه آلمان
🔹
وزرای امور خارجه ایران و آلمان، عصر امروز در تماسی تلفنی درباره تحولات دوجانبه، منطقه‌ای و بین‌المللی گفت‌وگو کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/680147" target="_blank">📅 23:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f223948e9.mp4?token=iTHNR6R7QWjAF57xzYmrAcCtear6MlUzxo22H6O2g4G5dTNST_FtiPEsBGVxEdYA5q1FHkISkYZ6L-38VNXikI7oQ-wuW2ViiWY3u5rzN0BuXuCSBSG36Je1TPo2azScmnB-4lre4OsEVNZVeGtNAmQ3F6K1gc8sExP6jBJMESJzEl8nGS28RWOTFQXFxBK9Y_Jm5Tu_BTz6HMiuOBJosayJOqvjoUHjvEGfFmxMULk_l3LXtz1ACnVwc2LgK-F34XDr9A0JhtomuXJFvDknwI2ax2v-l035m3EKDWdsNkpv8QwMJMmCdEbgaJA-xgO3O3JdkW3t16tuWZ3dhp65jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f223948e9.mp4?token=iTHNR6R7QWjAF57xzYmrAcCtear6MlUzxo22H6O2g4G5dTNST_FtiPEsBGVxEdYA5q1FHkISkYZ6L-38VNXikI7oQ-wuW2ViiWY3u5rzN0BuXuCSBSG36Je1TPo2azScmnB-4lre4OsEVNZVeGtNAmQ3F6K1gc8sExP6jBJMESJzEl8nGS28RWOTFQXFxBK9Y_Jm5Tu_BTz6HMiuOBJosayJOqvjoUHjvEGfFmxMULk_l3LXtz1ACnVwc2LgK-F34XDr9A0JhtomuXJFvDknwI2ax2v-l035m3EKDWdsNkpv8QwMJMmCdEbgaJA-xgO3O3JdkW3t16tuWZ3dhp65jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کُردها پرچم شورشیان سوری را در حسکه پایین آوردند
🔹
شبکه کُردی «روداو» گزارش داد کاروانی از اهالی شهر «سری‌کانیه»(راس العین) در استان حسکه پس از هفت سال آوارگی برای بازگشت به شهر خود راهی شده بودند که از سوی افراد عناصر وابسته به شورشیان سوری مورد حمله قرار گرفتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/680145" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680144">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
افزایش نگرانی آمریکا از دست یافتن روسیه به موشک‌های پاتریوت
«استینگر» خبرنگار بلومبرگ:
🔹
نگرانی‌ها در دولت آمریکا مبنی بر این که ممکن است کیت‌های حساس نظامی و موشک‌های پاتریوت به دست روس‌ها بیفتد، افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/680144" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680143">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
معاملات ۵۵ میلیارد دلاری ایرانی‌ها در پلتفرم‌های رمزارز خارجی
🔹
داده‌های سال ۱۴۰۳ نشان می‌دهد حجم معاملات کاربران ایرانی در پلتفرم‌های رمزارزی خارجی به حدود ۴۰.۵ تا ۵۵.۵ میلیارد دلار رسیده است.
🔹
به گزارش TechRasa Insight حجم معاملات در پلتفرم‌های داخلی بین ۲۷ تا ۳۷ میلیارد دلار برآورد می‌شود. دسترسی گسترده‌تر صرافی‌های خارجی به معاملات آتی، اهرم‌های معاملاتی و ابزارهای حرفه‌ای ترید از مهم‌ترین عوامل جذب معامله‌گران ایرانی به این پلتفرم‌هاست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/680143" target="_blank">📅 23:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680142">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۵۶۸ هزار نفر در صف وام ازدواج هستند
علیرضا نثاری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مبلغ مصوب تسهیلات قرض‌الحسنه ازدواج ۳۵۰ میلیون تومان با کارمزد ۴ تا ۵ درصد است و حدود ۵۶۸ هزار نفر در صف انتظار دریافت این تسهیلات هستند و تنها حدود ۱۲ درصد از تسهیلات مصوب در چهار ماه اول سال پرداخت شده است.
🔹
بانک‌ها موظفند قسمتی از منابع داخلی خود را بابت پرداخت این تسهیلات به انجام رسانند و بانک مرکزی باید سهمیه‌های بانک‌های عامل را مشخص و تا پرداخت این تسهیلات به متقاضیان نظارت لازم را داشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/680142" target="_blank">📅 23:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680141">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9c6bb8.mp4?token=TwYgVwL3wOnXV5NGIQ4qDTOWyePGcMiQ1CuA_wmDz7LRZHjcf8etsW_JXgWKOqC0oSkKsgt3x8j2ADGEUghmboVFzrW_2TbkIfz2103ZUoP53zt3-Y50_eDO0uCxLiO5f9M6BGvPce5pSTPyayAhFDA2aHOVjY1TPvnH9qPey3nOmY4QSIUe09IxrGRliVJkWagAxdyNmU_NjfSNgeHKYbBznELimXPOFVl0bG4J01T3lJ8zSVGpaywnlJ29kWoajUVW-dFFD9lHEdEXACdbCgZ9gffdGd2AacOPGCAyZZNRfekHJLlY0cj3M-zI5GaL9YoNo-RLYj5ZpxfwjJRyxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9c6bb8.mp4?token=TwYgVwL3wOnXV5NGIQ4qDTOWyePGcMiQ1CuA_wmDz7LRZHjcf8etsW_JXgWKOqC0oSkKsgt3x8j2ADGEUghmboVFzrW_2TbkIfz2103ZUoP53zt3-Y50_eDO0uCxLiO5f9M6BGvPce5pSTPyayAhFDA2aHOVjY1TPvnH9qPey3nOmY4QSIUe09IxrGRliVJkWagAxdyNmU_NjfSNgeHKYbBznELimXPOFVl0bG4J01T3lJ8zSVGpaywnlJ29kWoajUVW-dFFD9lHEdEXACdbCgZ9gffdGd2AacOPGCAyZZNRfekHJLlY0cj3M-zI5GaL9YoNo-RLYj5ZpxfwjJRyxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشگر: آیا پاسخی به نتانیاهو دارید؟
ترامپ:
🔹
من امروز در شبکه "تروث سوشال" (Truth Social) پاسخی را منتشر کردم. پاسخی خوب دارم. رابطه ما بسیار خوب است، بله
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/680141" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680140">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9343495b20.mp4?token=vdXJVVVKZAmnFP_MyEL-HuXD2XtHL2C5ptEsSi2tk3nea_iqudn-r_c1dCbua-Z4odmB_XPjjU4BKFBmLdQn6EngNOw4RMqe_zpf8FcBsUtCcGat-XOIBd4qMx7Ty73rK7rqCUMqgotFkjZH4pU8rFaJ1jx-rLeSu2z3q3CTfZH8iyiosrqZL_C9ZauFp0pSbgwazJg3jBlan7yYkV6s1-mOoJfd4lMttLzdDmJ30dWidnqVt3x1WpCKH5C5JyMOQs_3cIywCu6lIEk0L5EQkciG2Un8kX5VuahDWhwvV2qUFIP56-JcqMaBSyJft7k2XW1SAEcdXH36sdHH9TUvwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9343495b20.mp4?token=vdXJVVVKZAmnFP_MyEL-HuXD2XtHL2C5ptEsSi2tk3nea_iqudn-r_c1dCbua-Z4odmB_XPjjU4BKFBmLdQn6EngNOw4RMqe_zpf8FcBsUtCcGat-XOIBd4qMx7Ty73rK7rqCUMqgotFkjZH4pU8rFaJ1jx-rLeSu2z3q3CTfZH8iyiosrqZL_C9ZauFp0pSbgwazJg3jBlan7yYkV6s1-mOoJfd4lMttLzdDmJ30dWidnqVt3x1WpCKH5C5JyMOQs_3cIywCu6lIEk0L5EQkciG2Un8kX5VuahDWhwvV2qUFIP56-JcqMaBSyJft7k2XW1SAEcdXH36sdHH9TUvwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی اساس ترامپ دروغگو درباره ایران: آنها می‌توانند مشکلات ایجاد کنند، اما ورشکسته هستند، آنها پولی ندارند
🔹
ایران کاملاً ورشکسته است. آنها به سربازان خود حقوق نمی‌دهند.
🔹
نرخ تورم آنها ۳۰۹ درصد است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/680140" target="_blank">📅 23:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680139">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697393a302.mp4?token=L6PuCi8L3dEQpp8DvRfubP0qwMEGFVqG3qe0CxHsqCHdcd4iMon0Cg5EdXWMKwcrsuyiJtPgUP2tuFACFvc1c168Hq91SZuaVsVFPAdrRqWNH9x4SoENrN2Q3kzzcdkgGKF29r7A2hxC0NXInYw2cO2oIEXvOogb5VIgAxBt9OPMn5n-eC3Os4oe8fmDt7r-QyBmkDH64qBd1PdJ7FiNRUs6HSXxUOUtVBg9ZUCmrSADSBOZbH0LFnHafP0HqYQ4VQKI8a1leoTapyiuLO7J6Uany3sFafPRi2VhLHDacy6NvViy96DPtHH1H2dR2sXFyQaXAlbk26CtgJKa6yrecQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697393a302.mp4?token=L6PuCi8L3dEQpp8DvRfubP0qwMEGFVqG3qe0CxHsqCHdcd4iMon0Cg5EdXWMKwcrsuyiJtPgUP2tuFACFvc1c168Hq91SZuaVsVFPAdrRqWNH9x4SoENrN2Q3kzzcdkgGKF29r7A2hxC0NXInYw2cO2oIEXvOogb5VIgAxBt9OPMn5n-eC3Os4oe8fmDt7r-QyBmkDH64qBd1PdJ7FiNRUs6HSXxUOUtVBg9ZUCmrSADSBOZbH0LFnHafP0HqYQ4VQKI8a1leoTapyiuLO7J6Uany3sFafPRi2VhLHDacy6NvViy96DPtHH1H2dR2sXFyQaXAlbk26CtgJKa6yrecQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات مضحک ترامپ جنایتکار درباره ایران: ایرانی ها صدها هزار نفر را به قتل رسانده‌اند
🔹
اکنون آن‌ها در حال پرداخت بهای این اعمال خود هستند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/680139" target="_blank">📅 23:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680138">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f23aa183c1.mp4?token=i2jw1WzJHCsSy1iwqK4VnmqpCJP-3NnqHyUyCtV5ptoLCd388iaVzi4cdlxXjh1kmBsZ7sLhDKA6u3m9VnXKU7nwRg7sowI1yHAXNA8K65aFiHkGZmw025LiE5ERSlEz_hwXhV2H2_7x77J3IJwgdRObxJqnL-ZwBIqFtZrzFVYKRZ81f2hbIDw6oTjI378xzoswG6WkXI6G7tTLD-SIrGpc8wiSJGCrzYtDsO58lqUHgj8z_9LVcc6uL6pxhI26sWlucGbFo9O-8Uw9gKU49jryuBNp2zOnZQ7PDDq7waWz5DMZdu5bVsKyV3MYy_TSeYvnvGyMXU75l8DQXrtCZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f23aa183c1.mp4?token=i2jw1WzJHCsSy1iwqK4VnmqpCJP-3NnqHyUyCtV5ptoLCd388iaVzi4cdlxXjh1kmBsZ7sLhDKA6u3m9VnXKU7nwRg7sowI1yHAXNA8K65aFiHkGZmw025LiE5ERSlEz_hwXhV2H2_7x77J3IJwgdRObxJqnL-ZwBIqFtZrzFVYKRZ81f2hbIDw6oTjI378xzoswG6WkXI6G7tTLD-SIrGpc8wiSJGCrzYtDsO58lqUHgj8z_9LVcc6uL6pxhI26sWlucGbFo9O-8Uw9gKU49jryuBNp2zOnZQ7PDDq7waWz5DMZdu5bVsKyV3MYy_TSeYvnvGyMXU75l8DQXrtCZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشگر: تنگه هرمز چه زمانی باز خواهد شد؟
ترامپ دیوانه:
🔹
الان باز است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/680138" target="_blank">📅 23:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680137">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c51c663d55.mp4?token=bVUqEOZRM7EUqAAdz7oeS3fy3zEcr8ecqhSZunnjiYUL0RIG9RDh_caXWuJuFhmLkUpvdNtmDE-POz1CC-F68Rgwm2plPW5GH7VmiOHbwVxjqbCUggeYKVlXQ0HmADroE-lAYM2SEnQcRjHkBeReEIDJsPQREBVgA5pWKS7xkT8hfUsUdXDnqZRMcNw4gC_qSG-O-SAHdySl2AAAmVfj0Mu_BVzMUDIPhxu-3OUkLhSRpUZyDZTWxh8yx32kpLSMFILs2K73zvvjTtX0X-WKdOA9sQVDQNzdek6XoY42MQC1cQstcO_QwSnM3oZhE_ftr8sCn4k4NdECr1TBhmjApg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c51c663d55.mp4?token=bVUqEOZRM7EUqAAdz7oeS3fy3zEcr8ecqhSZunnjiYUL0RIG9RDh_caXWuJuFhmLkUpvdNtmDE-POz1CC-F68Rgwm2plPW5GH7VmiOHbwVxjqbCUggeYKVlXQ0HmADroE-lAYM2SEnQcRjHkBeReEIDJsPQREBVgA5pWKS7xkT8hfUsUdXDnqZRMcNw4gC_qSG-O-SAHdySl2AAAmVfj0Mu_BVzMUDIPhxu-3OUkLhSRpUZyDZTWxh8yx32kpLSMFILs2K73zvvjTtX0X-WKdOA9sQVDQNzdek6XoY42MQC1cQstcO_QwSnM3oZhE_ftr8sCn4k4NdECr1TBhmjApg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات ترامپ شیاد درباره ایران: همانطور که احتمالاً شنیده‌اید، ما تمام تنگه را پاکسازی مین کرده‌ایم، شاید شما این را نشنیده باشید
🔹
ما کنترل ۱۰۰ درصدی این تنگه را در اختیار داریم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/680137" target="_blank">📅 23:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680136">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44cff11291.mp4?token=JzIqrMz06W_dT_3yqvsSAOOGXwLlknbXB_oYmZg82CHF_e3llwW0xHglgxXw_3Q0jIXdE5CBHEMICy2gQt6MvxloN7-KKdHeYMKtJVhaBKA1GiJ5RcRIfup0eq3Y-8sM0DdKdrFUvZnTN4aiGDIL2b4qwDv9bGNU6Btq56BhrSTkLDo9Y4v0hNydvwgW2Jm90FrkkTeC1YQl_SBjfQbymRB0xfqnHaJKx4SiXHW8jbzfhEwEvO-tklRcViT3C9soUfXAvOZx53SPrbcYodEAuF6rwagfUFNPTaTZJcbLzefQZw6iesltfzH_N-y2Qsye7yurX3IQnnOLBssCRNcWog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44cff11291.mp4?token=JzIqrMz06W_dT_3yqvsSAOOGXwLlknbXB_oYmZg82CHF_e3llwW0xHglgxXw_3Q0jIXdE5CBHEMICy2gQt6MvxloN7-KKdHeYMKtJVhaBKA1GiJ5RcRIfup0eq3Y-8sM0DdKdrFUvZnTN4aiGDIL2b4qwDv9bGNU6Btq56BhrSTkLDo9Y4v0hNydvwgW2Jm90FrkkTeC1YQl_SBjfQbymRB0xfqnHaJKx4SiXHW8jbzfhEwEvO-tklRcViT3C9soUfXAvOZx53SPrbcYodEAuF6rwagfUFNPTaTZJcbLzefQZw6iesltfzH_N-y2Qsye7yurX3IQnnOLBssCRNcWog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: گاهی اوقات دوست دارم من هم سنا را از بین ببرم، اما این را نمی‌گویم، من این کار را انجام نمی‌دهم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/680136" target="_blank">📅 23:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680135">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f8a136fe.mp4?token=D7t5y_5hA1lWiqcEYLooIiSvbgJtmhMJYORcNaZdIifjWGzJZNqvpe35icKgVcidosnfnOZFJqqGY6qlaXCLa42FZbK0vN4QbAOsT69EciFm5nLOKA1g44VBQaL-bhWyyXIxgsYMdFS0Rv0s-nx-tDsi4-hgnXeZeuxu3CfYitOJ5bwCtSpQAQ2uh7_v-qELNAGbVRaG7Oed-iXDcy2NtGxLtfHhID1TQz-ZF77dRpdg5sqyHl7DPCuncvA2H9o_M1hxrdFNRny5-E9mK84ByCAjPVEw9EuS0eMLqhrSQsZjNCl805NUPFiXwxns-lvPtsWp1C2dcxXBPH3J2x686h4UnVqMxq7UKlUvh7-_dfwklXfuHBLL1weJYJ8B334BFbw0Mz6ny2Q_6eOQw1MBjvOuTR6x7HgtzSc1B3w4GY3bXF7ZuarJNx8QFADVkYiYICE4Val0NRrB556dDzSXQOlD6Z3A8Hnbb6qQUqxw1HXC0iJirOqQWSDhVxgjLfyxNnyMLbEIEg_5p7T0Q9G8yLq8H_Hc1QgHReL-fQ78mG0bFcLNIuKWQjslyOfFiKXSY-UZOZtciTZNzyiiB-H8kitxzVFpS7PIGDDX2OEeNZGdL-uBgX5Sa04zBn4ylQsM3gzGlaCZHcCTFyf-Da8O_PPp_RUHgDv2ZtIIsPG90ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f8a136fe.mp4?token=D7t5y_5hA1lWiqcEYLooIiSvbgJtmhMJYORcNaZdIifjWGzJZNqvpe35icKgVcidosnfnOZFJqqGY6qlaXCLa42FZbK0vN4QbAOsT69EciFm5nLOKA1g44VBQaL-bhWyyXIxgsYMdFS0Rv0s-nx-tDsi4-hgnXeZeuxu3CfYitOJ5bwCtSpQAQ2uh7_v-qELNAGbVRaG7Oed-iXDcy2NtGxLtfHhID1TQz-ZF77dRpdg5sqyHl7DPCuncvA2H9o_M1hxrdFNRny5-E9mK84ByCAjPVEw9EuS0eMLqhrSQsZjNCl805NUPFiXwxns-lvPtsWp1C2dcxXBPH3J2x686h4UnVqMxq7UKlUvh7-_dfwklXfuHBLL1weJYJ8B334BFbw0Mz6ny2Q_6eOQw1MBjvOuTR6x7HgtzSc1B3w4GY3bXF7ZuarJNx8QFADVkYiYICE4Val0NRrB556dDzSXQOlD6Z3A8Hnbb6qQUqxw1HXC0iJirOqQWSDhVxgjLfyxNnyMLbEIEg_5p7T0Q9G8yLq8H_Hc1QgHReL-fQ78mG0bFcLNIuKWQjslyOfFiKXSY-UZOZtciTZNzyiiB-H8kitxzVFpS7PIGDDX2OEeNZGdL-uBgX5Sa04zBn4ylQsM3gzGlaCZHcCTFyf-Da8O_PPp_RUHgDv2ZtIIsPG90ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ما شاهد انتخاب افرادی هستیم که دیدگاه‌های جهادی دارند، تقریباً در همه جا، ما با کمونیسم و جهادگرایی روبرو هستیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/680135" target="_blank">📅 23:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680134">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/856b799e72.mp4?token=sbxWZLfdMow7sOf-dL1KuDuTGzpNeB71ejKqpIauidZUVERa0eSOjAm8oOEB8VvvXjw-cEjBMKdnJLQ3Ybgz_lmE2RR_-jPfMq8dKdrKg3ZKs8QsNyzLQQgeXdXbMmnDwjHfvXnmdrb6OHN59IoGreqGrJDYBNrmGarqX8QTyJgMY40ovWDo_zFbuUS-4hG8Obt2Bq05tZ4rpox6lntyWT44eAtXRit9ITTLhLe5yYn_70ByArXTHAF1LGGtEykpuIQupAlV1BZyKP-ONAcsRpkD9VMICyebgqo03SxfgOG8M6e0CnfmkLr5PxvBPzWoybZ3AfHIvEwQgXig4tiAIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/856b799e72.mp4?token=sbxWZLfdMow7sOf-dL1KuDuTGzpNeB71ejKqpIauidZUVERa0eSOjAm8oOEB8VvvXjw-cEjBMKdnJLQ3Ybgz_lmE2RR_-jPfMq8dKdrKg3ZKs8QsNyzLQQgeXdXbMmnDwjHfvXnmdrb6OHN59IoGreqGrJDYBNrmGarqX8QTyJgMY40ovWDo_zFbuUS-4hG8Obt2Bq05tZ4rpox6lntyWT44eAtXRit9ITTLhLe5yYn_70ByArXTHAF1LGGtEykpuIQupAlV1BZyKP-ONAcsRpkD9VMICyebgqo03SxfgOG8M6e0CnfmkLr5PxvBPzWoybZ3AfHIvEwQgXig4tiAIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دروغگو: رئیس‌جمهور بعدی، اعتبار زیادی را به خاطر کارهایی که من انجام داده‌ام، کسب خواهد کرد
🔹
لطفاً به یاد داشته باشید که این کارها را من انجام داده‌ام، نه آن‌ها
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/680134" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680133">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1030697b.mp4?token=g-cd_y_fAq2h0Lq3dYkjhJ_57vap2Ih8XquZKAJ1nX9XkxMO_cWutLkaQZefY8iPB3HD59JId_veug_G6HKGdkBgdiU8_-A1UJ1PtBKNRMsqk3ekm_bDlM9RWZmkqJuSQHPQ9_Tri4-gBKCBL2NdxrxjOl9Z8V-m4L4K3qccD94Ck_EFEjxLlFrhrdvkH5F5S1oFwFZ8HtyHfMeWxgP8t9YzqDnPadpDtxj38PHfqOB-HONzQ2z7b7emQ2HjDgYeQeyyHn4JJd63Z0sD8SBnTV6QGBjOF-2-xeNH1n_1g5G9_cGusUs7x1ET3vSqnvYscPTSlIKRodBnZGL4uJCK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1030697b.mp4?token=g-cd_y_fAq2h0Lq3dYkjhJ_57vap2Ih8XquZKAJ1nX9XkxMO_cWutLkaQZefY8iPB3HD59JId_veug_G6HKGdkBgdiU8_-A1UJ1PtBKNRMsqk3ekm_bDlM9RWZmkqJuSQHPQ9_Tri4-gBKCBL2NdxrxjOl9Z8V-m4L4K3qccD94Ck_EFEjxLlFrhrdvkH5F5S1oFwFZ8HtyHfMeWxgP8t9YzqDnPadpDtxj38PHfqOB-HONzQ2z7b7emQ2HjDgYeQeyyHn4JJd63Z0sD8SBnTV6QGBjOF-2-xeNH1n_1g5G9_cGusUs7x1ET3vSqnvYscPTSlIKRodBnZGL4uJCK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ شیاد: هیچ اتفاق بدی از کارهایی که ما انجام می‌دهیم، نخواهد افتاد، هیچ اتفاق بدی رخ نخواهد داد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/680133" target="_blank">📅 23:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680132">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b9a07b7a.mp4?token=fQV_RG63GuKTMDN9MbtKHLiw0yV8euhu2jG_FxXuDNeQ6dUeStQvXLbcxxt3ormJs-laUF8sLJpjvZx3h6TBcZZmYXZxuFINWW5GzSfKua1DFdl9quZoFfuJXKS8ryesEi3QbiDKjLRb2xOJEU2AkruVY1Iiw-EYg0vLbUlu3LFKgvzKMjXS4wi-rTAljk9GqAufFO1FOYSCylGKnQIQlJ5coAwUrNsEFMQyXBPWALsH-U-5c6kruqVOhsPTBRfOx4SuqYgTUdnKJ1rtZ4GBtRaHv7SuuxLuDVDKDTQmFnmWjzPm4PnaJEcxiUjfU51EeD3eFEzDoei106FY4zTDVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b9a07b7a.mp4?token=fQV_RG63GuKTMDN9MbtKHLiw0yV8euhu2jG_FxXuDNeQ6dUeStQvXLbcxxt3ormJs-laUF8sLJpjvZx3h6TBcZZmYXZxuFINWW5GzSfKua1DFdl9quZoFfuJXKS8ryesEi3QbiDKjLRb2xOJEU2AkruVY1Iiw-EYg0vLbUlu3LFKgvzKMjXS4wi-rTAljk9GqAufFO1FOYSCylGKnQIQlJ5coAwUrNsEFMQyXBPWALsH-U-5c6kruqVOhsPTBRfOx4SuqYgTUdnKJ1rtZ4GBtRaHv7SuuxLuDVDKDTQmFnmWjzPm4PnaJEcxiUjfU51EeD3eFEzDoei106FY4zTDVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: برخی از گروه‌ها تقریباً هیچ مشکلی با اوتیسم ندارند
🔹
این گروه‌ها، افرادی هستند که به شدت به دنیای واکسن‌ها علاقه‌مندند.
🔹
هر سال، میزان ابتلا به اوتیسم افزایش می‌یابد، و این افزایش روز به روز بیشتر می‌شود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/680132" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680131">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa584be63.mp4?token=QlU5x0Y2x5m0YDoGIuQYSsTDJFPAca3DxIBphdeOCw6UfuktDc1P_S87d76wJcH1xalXMiHKr7cJQ1aFgykoiiIWB-3vhpDC2FhUBZ3hAj8jfmqbWfYLCkWd_rWwuGdm4y5PL7ASGHINrN58bhesI3VHWZnVKT1U8xMci7EG2yfANRrOlD6DNXmaFBh2Xk6JFz3NjhpSFX8MvhQBkWawgVdLOtlSEoOlttKjloGTdgpheQ4whFqW54-Ph_oIBqUiTsl5pbtg2qeyvyGQW8wMpb_K1S-xAdrudlUqCkrcDJac9AtWDps2dWXvruaAwe4NUhGubZKonrUjoyA4_m4JRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa584be63.mp4?token=QlU5x0Y2x5m0YDoGIuQYSsTDJFPAca3DxIBphdeOCw6UfuktDc1P_S87d76wJcH1xalXMiHKr7cJQ1aFgykoiiIWB-3vhpDC2FhUBZ3hAj8jfmqbWfYLCkWd_rWwuGdm4y5PL7ASGHINrN58bhesI3VHWZnVKT1U8xMci7EG2yfANRrOlD6DNXmaFBh2Xk6JFz3NjhpSFX8MvhQBkWawgVdLOtlSEoOlttKjloGTdgpheQ4whFqW54-Ph_oIBqUiTsl5pbtg2qeyvyGQW8wMpb_K1S-xAdrudlUqCkrcDJac9AtWDps2dWXvruaAwe4NUhGubZKonrUjoyA4_m4JRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ده‌ها سال پیش، کودکان تنها بخش کوچکی از واکسن‌هایی را دریافت می‌کردند که امروزه مورد نیاز است
🔹
در آن زمان‌ها، مردم بسیار سالم‌تر بودند و البته، میزان بالای اختلال اوتیسمی که امروزه مشاهده می‌شود، وجود نداشت.
🔹
دلیلی برای این میزان بالای شیوع اختلال اوتیسم وجود دارد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/680131" target="_blank">📅 23:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680130">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02f617be6.mp4?token=kDoDhzFWz_QalZGYWP2rExennIjxyi0N5DGsK8iLQpaOS2E9hUQk8bmZjJzt48IPRmyJAYKYwmqCdqnETjAfTvTzFW6qWhGH9ipHRX9L4lhcg_g5oG-9hV4Pyn9unc6HCOX5sNRXGOpNzZNmr3JxpqZnpPRPu2Tmu-smuBpLIMyiBxfFcVZnCk09cKVo88COlJN8gHuu2LX8aBH0rVVGSfRUzIBqCXIPquQk2VaXxhqiRpVFgL_guUj4_9yXg83vUOe8WYK-U502oJrkgA4tuK7Nif_7dtTaclabDzTgdG2OR7Jazh_zXMDuyFrDyalWkGkLuNwM54qB2ktvtcI2bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02f617be6.mp4?token=kDoDhzFWz_QalZGYWP2rExennIjxyi0N5DGsK8iLQpaOS2E9hUQk8bmZjJzt48IPRmyJAYKYwmqCdqnETjAfTvTzFW6qWhGH9ipHRX9L4lhcg_g5oG-9hV4Pyn9unc6HCOX5sNRXGOpNzZNmr3JxpqZnpPRPu2Tmu-smuBpLIMyiBxfFcVZnCk09cKVo88COlJN8gHuu2LX8aBH0rVVGSfRUzIBqCXIPquQk2VaXxhqiRpVFgL_guUj4_9yXg83vUOe8WYK-U502oJrkgA4tuK7Nif_7dtTaclabDzTgdG2OR7Jazh_zXMDuyFrDyalWkGkLuNwM54qB2ktvtcI2bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دیوانه: واکسیناسیون برای بیماری‌هایی مانند هپاتیت B، کووید-19 و آنفولانزا، و سایر بیماری‌ها، دیگر برای همه کودکان توصیه نمی‌شود
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/680130" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c3bdfc9.mp4?token=NPzUbCgRncQBI16gm0a8TdAgjW5tzMHiHY2imXsZ72UBlsi22zc3pYA0uXQudk2NaEm8ZFLWIcWWV0IyaGOB6Gr4J5w2SvpPbcVjue7b88XhGA7swUlsUOG4Le6WlBf-tZP61nkHo2BdhXVB7YAIf-TbsLsrfduDplgC4Z3sDWQvLfc596lw7teOCq1VJHYT-TryyyiVHxE1nnMZW454iNGS-kT03orpJ6elt8dx7PJNlD_-pdr3GfxSMpO_mKCRNrgffLU_QMmUrQH91Pz0ae1axXpeSxAx9c2o5szUbsIHgaSBP3SH_7sduoay8z9yMRDZe1SvMYUPqZoimnlbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c3bdfc9.mp4?token=NPzUbCgRncQBI16gm0a8TdAgjW5tzMHiHY2imXsZ72UBlsi22zc3pYA0uXQudk2NaEm8ZFLWIcWWV0IyaGOB6Gr4J5w2SvpPbcVjue7b88XhGA7swUlsUOG4Le6WlBf-tZP61nkHo2BdhXVB7YAIf-TbsLsrfduDplgC4Z3sDWQvLfc596lw7teOCq1VJHYT-TryyyiVHxE1nnMZW454iNGS-kT03orpJ6elt8dx7PJNlD_-pdr3GfxSMpO_mKCRNrgffLU_QMmUrQH91Pz0ae1axXpeSxAx9c2o5szUbsIHgaSBP3SH_7sduoay8z9yMRDZe1SvMYUPqZoimnlbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه اتفاقی خواهد افتاد؟
ترامپ:
🔹
شما متوجه خواهید شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/680129" target="_blank">📅 23:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2443a36c99.mp4?token=j2zKSPL2XXcFKbJuxZwoWnJ4F5gGn3tHUlRr7d35xMtFPirg5d9LYuJ5fqI4FcN_84TWqXn3J1kdj1MXMarMHalUpWRiqj8Cx8NuMp-SnhxZ6PektZ9izFKYp6AHCaornBEtRphKOY04yiAKgFoSZsgggrxAHd2g_srJ3-KW7uwRIzXvkJLSA33B_mD5C81NPMFnY_ixTDLUCl_QrKrO71z0ADFd8eGRO-xBJJ9nlT9N5JUKFa_prD3r6nKYjZXblpvXsVNhQTKO_nYFIJVYJ7cIbUes_RniEZ-QJ1fvmR8VB53aWl0aky5kkRAv7SfNwA-OC9Jp3pDM0uGM-LphCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2443a36c99.mp4?token=j2zKSPL2XXcFKbJuxZwoWnJ4F5gGn3tHUlRr7d35xMtFPirg5d9LYuJ5fqI4FcN_84TWqXn3J1kdj1MXMarMHalUpWRiqj8Cx8NuMp-SnhxZ6PektZ9izFKYp6AHCaornBEtRphKOY04yiAKgFoSZsgggrxAHd2g_srJ3-KW7uwRIzXvkJLSA33B_mD5C81NPMFnY_ixTDLUCl_QrKrO71z0ADFd8eGRO-xBJJ9nlT9N5JUKFa_prD3r6nKYjZXblpvXsVNhQTKO_nYFIJVYJ7cIbUes_RniEZ-QJ1fvmR8VB53aWl0aky5kkRAv7SfNwA-OC9Jp3pDM0uGM-LphCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات ترامپ درباره ایران: اگر خساراتی باید پرداخت شود، به نظر من ایران باید آن خسارات را بپردازد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/680128" target="_blank">📅 23:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3TFgYaeUaNaX4JCXNIFTAtx1k5Rc-DOWuSBIs37iXHEFU9QoEw7B9phi0Vy0SRKJMM0guOiEv2eJr35QfokP4L4RFcIHHbQEnb79lQC4n7CofRfVGdSuEuqixWX2k-ycBwPqNyM3xXKCamPDe83CFblO0HH_1nKkYF8bRtCK0ZiRedXg0T1YlVJ5IfhX70C1WMoV5AwnMj0WXkHBBkkhRrNe3BoAgLKcKQ0MMaN87VkkKhi_mc96kScp8uyIL0GSVu6v7qrOVwzEQLdHxG_P_xLH4Ay-U06IOSEL6ovV0wAk4VMZZr7KtwRmxBvQAoI3K3u--oz3lxVM2HrjH8QQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه ایران: وزیر خزانه‌داری آمریکا به «خفه کردن» ایران از طریق تحریم‌های اقتصادی افتخار کرده است
🔹
این ادعا، فراتر از تأثربرانگیزی محض، گواه روشنی بر اعتیاد اجباری آمریکا به تحریم‌هاست. هرگاه واشنگتن ناتوانی خود را در پیگیری دیپلماسی نشان می‌دهد، به تحریم‌ها پناه می‌برد و هرگاه این تحریم‌ها نتیجه نمی‌دهند، صرفاً دوز آن را افزایش می‌دهد.
🔹
این دیگر «سیاست» نیست، «عادت» است؛ و خطرناک‌تر اینکه، اعتیادی است که جای تفکر را گرفته است. ایران طی دهه‌ها نشان داده که با این لفاظی‌های فرسوده خفه نخواهد شد. خطر واقعی این است که سیاستمداران آمریکایی، با چسبیدن به این عادت بد، آخرین شانس‌های باقی‌مانده خود را برای خروجی کم‌آبروتر از بحرانی که خود ساخته‌اند، از بین ببرند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/680127" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
آژیر هشدار آزمایشی فردا در جاسک هرمزگان به صدا در می‌آید
🔹
به منظور آمادگی و ارزیابی عملکرد تجهیزات، تست آژیر هشدار توسط نیروهای نظامی از ساعت ۱۰ صبح سه‌شنبه در سطح شهر جاسک انجام می‌شود.
🔹
این اقدام صرفاً یک مانور و تست فنی است و هیچ ارتباطی با وقوع حادثه یا شرایط اضطراری ندارد و شهروندان نگرانی نداشته باشند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/680126" target="_blank">📅 22:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8ae789ba.mp4?token=IjLUipfISLWvZtMOtTQuC1LuXWdyrSDpmjYMwbzjLmrMLowLCQQsGg5qGCHaw4i8UL9v39b_PB_0nQgnU8iBwQDoTSdvrXWrV55F9_FvhhCcjKZfRN58nzWbwLwxkZiyxTeMnoALJjJNHo-dyLIOv1VafBN0b8KgJ23VGWnMmqgvJclfTifEo3fcbajwii7lZyRUv05c4OE4CdDrl2t_vnfkdYutzXIeLeXa60BksQpq2qdw1dobwzG8TlEWTCEzyCnh0rHHIoBiYerYOd0IghcP9mLME0cgIGbUTZPLr2LY_uH0Gy5uMYRqM6NEQUJEI8l9bDy9UUsTSihQmcaEeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8ae789ba.mp4?token=IjLUipfISLWvZtMOtTQuC1LuXWdyrSDpmjYMwbzjLmrMLowLCQQsGg5qGCHaw4i8UL9v39b_PB_0nQgnU8iBwQDoTSdvrXWrV55F9_FvhhCcjKZfRN58nzWbwLwxkZiyxTeMnoALJjJNHo-dyLIOv1VafBN0b8KgJ23VGWnMmqgvJclfTifEo3fcbajwii7lZyRUv05c4OE4CdDrl2t_vnfkdYutzXIeLeXa60BksQpq2qdw1dobwzG8TlEWTCEzyCnh0rHHIoBiYerYOd0IghcP9mLME0cgIGbUTZPLr2LY_uH0Gy5uMYRqM6NEQUJEI8l9bDy9UUsTSihQmcaEeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرت زدن رئیس جمهور متوهم آمریکا تمامی ندارد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/680125" target="_blank">📅 22:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680123">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
دست و پا زدن‌های ترامپ برای فرار از معرکه جنگ با ایران
🔹
بر اساس تازه‌ترین آمار، ذخایر نفت خام راهبردی آمریکا به زیر ۳۰۰ میلیون بشکه و رقم ۲۹۸.۷ میلیون بشکه رسید، که پایین‌ترین سطح آن‌ها از سال ۱۹۸۳ به این سو است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/680123" target="_blank">📅 22:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680122">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b99cc09220.mp4?token=jotNA5rKibylGlgjWM9D8PB0BPhdBfSU1X9XoCHxQD_RLR0x9vnu1EjHNLG5ZgcchwzHwYu6m_Zl81W5tVB1B5oSgz5WyG76aamhrc2GCiymtDPDJGKTaGtgshHTg8nJY2TRobwC4QVBX0o-vXuxt-Pb0Epdd9ucicf7Ck3kUvdv0ocHhnrguIxCsfwi5Xp93oLmAiHn8UFKNDA29fCYeA0qmmmb3_3stNlDGoP7hws3Qc-AI5XIFiNeYJ7jep5HVYYgZ7EMxvssNNgcGDKcqFQtVCDi3_3QMCeh6f9N7UZ6I7iQT7vgHUX-beAWHPSIlOpXlV7E4G_RFwzA2_l2bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b99cc09220.mp4?token=jotNA5rKibylGlgjWM9D8PB0BPhdBfSU1X9XoCHxQD_RLR0x9vnu1EjHNLG5ZgcchwzHwYu6m_Zl81W5tVB1B5oSgz5WyG76aamhrc2GCiymtDPDJGKTaGtgshHTg8nJY2TRobwC4QVBX0o-vXuxt-Pb0Epdd9ucicf7Ck3kUvdv0ocHhnrguIxCsfwi5Xp93oLmAiHn8UFKNDA29fCYeA0qmmmb3_3stNlDGoP7hws3Qc-AI5XIFiNeYJ7jep5HVYYgZ7EMxvssNNgcGDKcqFQtVCDi3_3QMCeh6f9N7UZ6I7iQT7vgHUX-beAWHPSIlOpXlV7E4G_RFwzA2_l2bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراحل درست کردن یک شات قهوه به صورت متفاوت و جالب
🧋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/680122" target="_blank">📅 22:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680120">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc5a794ee.mp4?token=FUSQcxsN83T3024-geM6-5-jp1l3ICZ1BG2PyVotRe1y_c-brwND4oYrwbuRLSdN7hjK3YXwN-dDNtPxg1Dx5ptxrAaDywusp9tZ3UFKhZakwWcD4Je50mX0WhFk9eejsUjdI0V5tze1W4UMpFMaf1aWf0YcfsNQiluMtfv-RfCgjU1m4A1_x93kqMqrUgP_2k5VYplbBUi8xGg0TZqBOAtKJOugP9sfQl-s2Ia6EmE3M29x0W7-PHz0p2H6fDwvRkdrOa1RrTo-owmeF8aFHTWsRFwlXY-Qmg7Ki2LHdjmIX_pZPUBITSevLb93NI698Qk2wFuFZPo9ZT7DxtRv1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc5a794ee.mp4?token=FUSQcxsN83T3024-geM6-5-jp1l3ICZ1BG2PyVotRe1y_c-brwND4oYrwbuRLSdN7hjK3YXwN-dDNtPxg1Dx5ptxrAaDywusp9tZ3UFKhZakwWcD4Je50mX0WhFk9eejsUjdI0V5tze1W4UMpFMaf1aWf0YcfsNQiluMtfv-RfCgjU1m4A1_x93kqMqrUgP_2k5VYplbBUi8xGg0TZqBOAtKJOugP9sfQl-s2Ia6EmE3M29x0W7-PHz0p2H6fDwvRkdrOa1RrTo-owmeF8aFHTWsRFwlXY-Qmg7Ki2LHdjmIX_pZPUBITSevLb93NI698Qk2wFuFZPo9ZT7DxtRv1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پورجمشیدیان؛ رئیس ستاد مرکزی اربعین: هنوز شرایط حضور زائرین در عراق با خودرو شخصی فراهم نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/680120" target="_blank">📅 22:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680119">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf02b7944.mp4?token=Plh26WTQuO-JE51FaHOa6hl0PScT-mjpvnD3rpHEB5uQK3Kh5unWIQYKuM_S9eDopuBOTMFwucogMpRxTd2qDwk_dZi6Am7zuGxP6OJdlUorZJns3a24f4vWMla0vzf-gAyx0isWFh_mMx39oS-qfCJV5Z7M8jsZ14keCDbXwxZOwT9SqXpG_dJ615egZHCNF9wGNamE3z91zpAdWVSk7pUGVdS9unLePkmrh0jlrzRsSAF92sWiV8l2vX8dC2bUzHJTKhqbYRyPMwDa66tTW_bWtrMa-aZKSCU-WPD2Zh0RUBh3_iQKyi6HN5FonLnv218KpQ12Q271GwUV9_1aQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf02b7944.mp4?token=Plh26WTQuO-JE51FaHOa6hl0PScT-mjpvnD3rpHEB5uQK3Kh5unWIQYKuM_S9eDopuBOTMFwucogMpRxTd2qDwk_dZi6Am7zuGxP6OJdlUorZJns3a24f4vWMla0vzf-gAyx0isWFh_mMx39oS-qfCJV5Z7M8jsZ14keCDbXwxZOwT9SqXpG_dJ615egZHCNF9wGNamE3z91zpAdWVSk7pUGVdS9unLePkmrh0jlrzRsSAF92sWiV8l2vX8dC2bUzHJTKhqbYRyPMwDa66tTW_bWtrMa-aZKSCU-WPD2Zh0RUBh3_iQKyi6HN5FonLnv218KpQ12Q271GwUV9_1aQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد ۴ تنی با ماه؛ فالکون ۹ چه بر سر سطح ماه آورد؟
🔹
ماه حالا یک زخم تازه دارد؛ بقایای موشک فالکون ۹ اسپیس‌ایکس با سرعتی سرسام‌آور به سطح آن برخورد کرد.
🔹
این برخورد که چند روز قبل رخ داد؛ اکنون نخستین تصاویر از دهانه ایجادشده، توجه دانشمندان را به خود جلب کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/680119" target="_blank">📅 22:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680118">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFd9HswKgN4A9ZK7N8JeVGkXboOF6ptG8ddNIQ_u8gGxrI-JwrsC5gsIueVpvDitkW1Pas0fu_IzrZi7wQ77bDW5ev5gzIyL6Uox889igIf9gHoR33SnEByi8Z2eh6M7YU4gGGXPOmq28wtF4UIVYXBhjCYT0jiX8ItWmQnvScQ77Y_hLgNx6k-jlAcCedBh3KSj28goNcWTNTwrFq_Mc9IXEc8gmrhJXCucWEKfSjtprNukuzjZ0V8zsq61tgi2f1q893maw7kq0uv5LdXW3aQXu-j51Twsg4d2icUAavFgZRxBo6X7N7D0pcez52Su2_zWYMWkwRUYGJLRDsepSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قواعد دیده‌شدن محتوا در سرچ گوگل تغییر می‌کند
🔹
گوگل در حال تغییر شیوه ارزیابی محتوا در جست‌وجو است، تغییری که با گسترش پاسخ‌های هوش مصنوعی می‌تواند قواعد سئو را دگرگون کند.
🔹
بر اساس گزارش Search Engine Journal، گوگل برای سنجش حضور آنلاین برندها و محتوا از سیگنال‌های بیشتری استفاده می‌کند.
🔹
به این ترتیب، موفقیت محتوا دیگر فقط به تعداد کلیک‌ها وابسته نیست و میزان دیده‌شدن، اعتبار و حضور یک برند در پاسخ‌های هوش مصنوعی نیز اهمیت بیشتری پیدا می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/680118" target="_blank">📅 22:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680117">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رسوایی امنیتی در نیروی دریایی انگلیس
♦️
شهپادهای انگلیس داده‌های خود را مخفیانه به چین می‌فرستادند
تلگراف:
🔹
داده‌های شهپادهای نیروی دریایی انگلیس به طور مخفیانه به چین ارسال می‌شد. با وجود تضمین‌های امنیتی ، دوربین‌های نصب‌ شده روی ناوگان شهپادهای نظارتی انگلیس حاوی قطعات چینی بودند.
🔹
تحقیقات نشان داد که این دوربین‌ها سیگنال‌ها را به یک آدرس IP در چین ارسال می‌کردن، که وزارت دفاع  انگلیس بعد از آگاهی از این موضوع اتصال آن‌ها کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/680117" target="_blank">📅 22:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680116">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
موانع واردات بیشتر شد؛ انتخاب مردم کمتر
🔹
واردات خودرو که قرار بود به تعادل بازار کمک کند، حالا خودش به یکی از گره‌های اصلی این بازار تبدیل شده است. جزئیات موانع تازه واردات خودرو را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/680116" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680115">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d40ed29a.mp4?token=NB-u-HgocqGIp8_VOsyRM_8GS3JBKP75Nnj6Outjb9TR8q3aO8z3a_jY-ONDU5rqBO9Y25c92NOUcmlKFkg-HgPJuD6ZwLmnPYlKu3l48E5qsCQyPjs2HVh1VrwJ1ydRBugcaJ47GVGSUC8pgHgfJFz4VsX_kGM7f8xRLREKGF6Cli5QPUQXMF0Q6ADg58-RXOJqvMFk8PEcj3P-gx2B5CRqaSkilWcIyN5om2AEuU_gLcQrIsC3_8NXrvGGHKQ8oB--vchfdIIQ9LEzw3Za-aMBtZki5PbDVH3R1gDi-XImlWA27Q0Xsa0hCSvYxZzUDXf2Z2gkXbESPNPjDgAiLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d40ed29a.mp4?token=NB-u-HgocqGIp8_VOsyRM_8GS3JBKP75Nnj6Outjb9TR8q3aO8z3a_jY-ONDU5rqBO9Y25c92NOUcmlKFkg-HgPJuD6ZwLmnPYlKu3l48E5qsCQyPjs2HVh1VrwJ1ydRBugcaJ47GVGSUC8pgHgfJFz4VsX_kGM7f8xRLREKGF6Cli5QPUQXMF0Q6ADg58-RXOJqvMFk8PEcj3P-gx2B5CRqaSkilWcIyN5om2AEuU_gLcQrIsC3_8NXrvGGHKQ8oB--vchfdIIQ9LEzw3Za-aMBtZki5PbDVH3R1gDi-XImlWA27Q0Xsa0hCSvYxZzUDXf2Z2gkXbESPNPjDgAiLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنج و دمام‌زنی اطراف حرم مطهر رضوی
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/680115" target="_blank">📅 22:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680113">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd1qbGTZiDL7SVGPZg46lrMVQ-ey1-1xzRdhiVODCRKg-Sse3tD8A_yaUsiE7WEWHlwvd4ufggmrFluEK1vhUSevgVos6x1nOFb_hYswT33pD6FoirJRHjxbncIuitwcTKNo567eJWyd1aJweQEiWOykTozyFtUtvIyj5EvdtpQSQfeSd2DrF6GXfkSxa8PYDueZ3g4K_OA4tIt4AGCoA4w4SeivVkfQnhT36_GSGwgPnV7rFvetcOYqACrLpGONmGgZvAt6vP0sU-VSfjuY4cdHl2qWMy73CSSYWdCkT-zEwxTUc6QN0693R4k2Cb3lEFcc9snhYLPrdSVBXz4UFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خردمند، پیش از سخن گفتن می‌اندیشد
🔹
امام علی(ع) در حکمت ۴۰ نهج‌البلاغه یادآوری می‌کند که سخنِ سنجیده نشانه عقل و پختگی است. انسان خردمند ابتدا حرفش را در ذهن و دل می‌سنجد و بعد بر زبان می‌آورد؛ اما سخن عجولانه گاهی در چند ثانیه چیزی را خراب می‌کند که ساختنش…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/680113" target="_blank">📅 22:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680112">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ob30-pJvwmZqRcbNWnccrl1tHvhMlliN6JHH8IgfcLa9x32iQ8MktvimSDqidflEkShVdTW_pok1hOzsMd3w3fhhAH9RYfqE0e3OnH_R60H4iiCsok9QkMuqx5Iz_bvISaDtQbRWN8CFasP15A5TxQSPYj5xfzPI987cD2uC35TYGw-D1ievNwmmmQEpBf75qYLDYZfYX7LEUhbUajmVyZ8YAOob7XNWbnzGKWnW-hzx_mdE0Sv5oEYAF45S7I2IbBGNhy_9lDvJXlgVBksmiCfBTJBBxq6S2ktq-epZ9Y5I2-otUd3sf47q129hYzayrud_7brpQxdO4ShOGtW8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوراکی‌های مفید که برای استخوان‌ها خیلی مفید هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/680112" target="_blank">📅 22:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680111">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4143c1388.mp4?token=DnqSrIZX9UaEvLKYbHh-1kxw34_voRw0vCFeQSSc8fufU9rSLj_276he5G6Ct0itDLpqb79wGxgTMOqkXeFzo75LHcw0oAuWoTgQgHZRD90h96eXIeJiXhUkhTcjFNEOCFjq5i5qv7-r3DYmybU-j7Qr6pU7EHToCNLOhtiulJOLvy2eLKcbip2MVmlrZN1bIQ7qFiD-ELhqZp_oOJjtIw4nlibx4dsRu3QRiyi6nCpmkf3A_J8Kp1VbJbbb3NfgEJwoYzqB3NzKfPNoGOwgjVcE2fAm-XScBSCpRgiMe99nWOrFsc_rsY7jBOCxfS5PbG_JK5uaBjR2xB7B1-GekAqhaop5gAdsm7e8ZkX-42_nPxADOV6yzclVVUeHMf8KfaoXqKQduPHyw7fCQgTgAUyEyLAeDwJqmAXIKRDVkqvGoHJAH_vF5pw9KGRwIqOa4y9Zprg-Wqx0nm8jYVda-Ct1PAP0hOcGCiew3s-jdV8nzeh4b4jRBrIX8vpuQMk2bnI-OB00usYVnsO2Gr8IFAF7f3qRzEfKKhhiHgrQfV45CXbU36_Hw81RzgOECU-MkXORgGTWEOPIp3OWXvIxaWyjZ3HsfH8yWQLtG1tTExNaSt35tXHdV7bByqcK8JvWvQ0tuhaOdJisOiE_DgVFSkfoIPEGTZCaujgYmO52RTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4143c1388.mp4?token=DnqSrIZX9UaEvLKYbHh-1kxw34_voRw0vCFeQSSc8fufU9rSLj_276he5G6Ct0itDLpqb79wGxgTMOqkXeFzo75LHcw0oAuWoTgQgHZRD90h96eXIeJiXhUkhTcjFNEOCFjq5i5qv7-r3DYmybU-j7Qr6pU7EHToCNLOhtiulJOLvy2eLKcbip2MVmlrZN1bIQ7qFiD-ELhqZp_oOJjtIw4nlibx4dsRu3QRiyi6nCpmkf3A_J8Kp1VbJbbb3NfgEJwoYzqB3NzKfPNoGOwgjVcE2fAm-XScBSCpRgiMe99nWOrFsc_rsY7jBOCxfS5PbG_JK5uaBjR2xB7B1-GekAqhaop5gAdsm7e8ZkX-42_nPxADOV6yzclVVUeHMf8KfaoXqKQduPHyw7fCQgTgAUyEyLAeDwJqmAXIKRDVkqvGoHJAH_vF5pw9KGRwIqOa4y9Zprg-Wqx0nm8jYVda-Ct1PAP0hOcGCiew3s-jdV8nzeh4b4jRBrIX8vpuQMk2bnI-OB00usYVnsO2Gr8IFAF7f3qRzEfKKhhiHgrQfV45CXbU36_Hw81RzgOECU-MkXORgGTWEOPIp3OWXvIxaWyjZ3HsfH8yWQLtG1tTExNaSt35tXHdV7bByqcK8JvWvQ0tuhaOdJisOiE_DgVFSkfoIPEGTZCaujgYmO52RTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: حدود ۸۰ درصد واردات کالاها به کشور از جنوب انجام می‌شود
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
درحال حاضر حدود ۶۰ تن کالای اساسی نیاز داریم.
🔹
فردای روز تشییع رهبر شهید در مشهد، راه‌آهن تهران به مشهد مورد هدف قرار گرفت که کمتر از ۱۳ ساعت دوباره شبکه ریلی را به مسیر آوردند.
🔹
با فرض اینکه در جنوب محاصره دریایی شدیم و نتوانستیم کالایی جابه جا کنیم، به راحتی از شمال و کشورهای حاشیه کریدورهای زیادی داریم.
🔹
کریدورها نیاز به ساماندهی دارند و میزان فعال بودن آنها کم است مثلا با پاکستان خیلی محدود می‌توانیم کالا ردوبدل کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/680111" target="_blank">📅 22:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680110">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2xLDNbyX_9cVouc_H9yxkx5Rv4qdSswXSYXFJ9N-GI_oNGSBViAHnZQP6Up-o_tCiPnlMWO9oQE9QeBQ1aYSu0DKsQI95NwHLBtAm5u0qofu1jDW4o9vt4_Q_mArISf5gmHRnysu2NSk9AbH9pZSfem_gShX9VhkFm4OVAQ-PmC6hZkB1y5kxpvtEqYO3fl6i-3cFtqLjomSblYVHWyE0q20ZeveOVBg-NI2qIzmtGZ3DdbM2Y48su2nMyiuOnjPvKTw8mlUl8W-U3kbQSGGCoSlv-ddiCdpEF-NJ83T3YCvolw-XuiqRcZLwjMU--PTpu-yrxAT7UVqTeeTNrtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
خبر فوری برای مالباختگان گوشی در سراسر کشور
🚨
اگر در ۳۰ روز گذشته گوشی شما در ایران یا عراق گم شده یا به سرقت رفته است، همین حالا از طریق لینک زیر سریال (IMEI) آن را در سامانه همیاب۲۴ ثبت کنید
تا فرآیند ردیابی و اطلاع‌رسانی کشوری برای گوشی شما فعال شود.
📲
ثبت سریال و فعال‌سازی ردیابی:
https://hamyab24.ir/l/nzw
https://hamyab24.ir/l/nzw
⚠️
توجه: اگر گوشی شما در همیاب۲۴ ثبت نشود، فرآیند ردیابی و اطلاع‌رسانی کشوری برای آن انجام نخواهد شد.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/680110" target="_blank">📅 22:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658af79ef2.mp4?token=eeO4PcliHCA7d5oJYv95k64MjBorPGcEu1INvAPdT93IeMFtvUb2DJ211pmBvbAvdpTSO6yagw5Q02V0--pXBfwIvM8Is5WBGDgdpNjDZwuZ8Zku36G2rsmFXLZmVf7Q6xXMt9vRJ8DEQKOGT-lFGEqySz9T_JsEpezhPitKWNArisscFuF_6QiF0G257UdTAizseYdqJ_dh0mmD8txYb5qZxYMriFmFn8QRomVuRKrdaGsyBfXf9zUeqdd9KF66kz5mkP5vCWBvz-4v3KE3Bd5Yqp27cs_C0tksjXYYXrPmgRxwsjhK-QYKZGNnbFLujTTG9URb3gK4uqKvM1roTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658af79ef2.mp4?token=eeO4PcliHCA7d5oJYv95k64MjBorPGcEu1INvAPdT93IeMFtvUb2DJ211pmBvbAvdpTSO6yagw5Q02V0--pXBfwIvM8Is5WBGDgdpNjDZwuZ8Zku36G2rsmFXLZmVf7Q6xXMt9vRJ8DEQKOGT-lFGEqySz9T_JsEpezhPitKWNArisscFuF_6QiF0G257UdTAizseYdqJ_dh0mmD8txYb5qZxYMriFmFn8QRomVuRKrdaGsyBfXf9zUeqdd9KF66kz5mkP5vCWBvz-4v3KE3Bd5Yqp27cs_C0tksjXYYXrPmgRxwsjhK-QYKZGNnbFLujTTG9URb3gK4uqKvM1roTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع انفجار در یک مخزن سوخت در لیبی
🔹
منابع خبری گزارش دادند چندین انفجار در یک مخزن سوخت در پالایشگاه الزاویه در لیبی رخ داده است، هنوز علت انفجارها مشخص نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/680108" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d62d01e2d2.mp4?token=NDMTicVo2Wg4PWWUiOD9SKbj02hQiaeL3j-SV374WdKh34v_UBY6X5mP9__rtX7AUIFeB7g-WYPKsEIfMS19hC747uR37uq6BfJhNQvIeuQ_P2LCYnNmpF_csO1IdLhJWtbILpPtLN7Xn59iSPKYiMYXhEW5Tgf5tU3NoTAz0pmYxrHUMUmSgCVslkmoy96bnR-cuGY43MPnYD1gSrf-w2RuPu_JwFlHaZ-uA-1NI1MoERJVN7zrN-rKZoIOIhJCjtzx-NkwdgAeyGnf21fZWBlgHtRDD2cukQEXnsCwBRNEk7xVxUVO9KhsJYpCLxT8Fa2mOLnZP046_OoNFjo19A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d62d01e2d2.mp4?token=NDMTicVo2Wg4PWWUiOD9SKbj02hQiaeL3j-SV374WdKh34v_UBY6X5mP9__rtX7AUIFeB7g-WYPKsEIfMS19hC747uR37uq6BfJhNQvIeuQ_P2LCYnNmpF_csO1IdLhJWtbILpPtLN7Xn59iSPKYiMYXhEW5Tgf5tU3NoTAz0pmYxrHUMUmSgCVslkmoy96bnR-cuGY43MPnYD1gSrf-w2RuPu_JwFlHaZ-uA-1NI1MoERJVN7zrN-rKZoIOIhJCjtzx-NkwdgAeyGnf21fZWBlgHtRDD2cukQEXnsCwBRNEk7xVxUVO9KhsJYpCLxT8Fa2mOLnZP046_OoNFjo19A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میگ-۲۹ اوکراین سقوط کرد
🔹
یک فروند جنگنده میگ-۲۹ اوکراین در جریان یک مأموریت رزمی در منطقه اودسا دچار سانحه شد و سقوط کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/680106" target="_blank">📅 21:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
نظامی سابق آمریکا: روند خروج ما از منطقه آغاز شده
اسکات ریتر، نظامی بازنشستۀ آمریکایی:
🔹
ارتش آمریکا بخش قابل‌توجهی از ذخایر موشک‌های دورایستا و مهمات دقیق خود را مصرف کرده و ذخایر تاماهاوک نیز کاهش یافته.
🔹
در نتیجه آمریکا برای حمله به اهداف عمیق در داخل ایران با کمبود سلاح‌های دورایستا مواجه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/680102" target="_blank">📅 21:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3fe4fef4.mp4?token=Z1GyQ6EgwRszSFAMR7Xm9BuYJC0LZdzhWc0kpw9MxTYWvKkcoSkzEBTXwG4SMZOe02YfHgefvzeJmrURXLZn21CQKxrUhAZ5gyzYIQFXyS_ax1nUe9j-FVvcFRCWbBSntbt4r1BIZtU419Ne4bvyp9OvdlUV7UPltwKKTeRuXkezzGWSILYuduiv8zBG9sgtiv2_69Pzi3sHJ92dbFXDN1MiyGZIku8mPi-Hwe-pxwlsPDfX3o_OEQ2UxQxgmJ0XSQ1_WIu04HQSC_o4MCOB7fG7sDItuZzA8aNRUgGOm8Iov7mvk4EzfQRCd72hNxQuF88hfd7enJy3G2oIFQjPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3fe4fef4.mp4?token=Z1GyQ6EgwRszSFAMR7Xm9BuYJC0LZdzhWc0kpw9MxTYWvKkcoSkzEBTXwG4SMZOe02YfHgefvzeJmrURXLZn21CQKxrUhAZ5gyzYIQFXyS_ax1nUe9j-FVvcFRCWbBSntbt4r1BIZtU419Ne4bvyp9OvdlUV7UPltwKKTeRuXkezzGWSILYuduiv8zBG9sgtiv2_69Pzi3sHJ92dbFXDN1MiyGZIku8mPi-Hwe-pxwlsPDfX3o_OEQ2UxQxgmJ0XSQ1_WIu04HQSC_o4MCOB7fG7sDItuZzA8aNRUgGOm8Iov7mvk4EzfQRCd72hNxQuF88hfd7enJy3G2oIFQjPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی پزشکیان و حداد عادل با معادل فارسی پازل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/680101" target="_blank">📅 21:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680100">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/680100" target="_blank">📅 21:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ایران از اوکراین غرامت خواست
ادعای شبکه سی‌بی‌اس نیوز:
🔹
ایران از اوکراین بابت حمله مرگبار به یک کشتی ایرانی در دریای خزر درخواست غرامت کرده و ادعای کی‌یف مبنی بر تصادفی بودن این حمله را رد کرده است.
🔹
در حمله ماه گذشته، یک ملوان ایرانی جان باخت که اوکراین بعداً آن را یک اشتباه اعلام کرد. از آنجایی که مقامات ارشد اوکراین به انجام این حمله اذعان کرده‌اند، تهران انتظار دارد کی‌یف غرامت پرداخت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/680099" target="_blank">📅 21:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxwBP_f_oWe2GyoTqLv0MC88WXTiXUoYyTn-IlmPFODLO0pje2UcK4ahGD-Wnv1zVNVLvBtiSE4gxJbypZH523w8gz9CBICrleJqpdXTK72Qkgoyw9CWtuzuNN0gepfvLxeK0sv7kEzNXDcirsvyVJSsY4ZvBtF278vulzyIP7CNaIbC69MQ_luFQ7ChGAw6GCopVCSTNZNcczMtzTx0cpfAIji5lBStgi-3RKkHIGtFmo83M3tlcn9QN9i3wdHmVNvUHjYjNOMxM1CqM5UQ6BPdRY2u8ThtR0Sg6QltBodSueIqyULaCgD1K0dTU8_5DSf1pFdWxCUGJ7TtugAqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش مراقبت سلامت همگانی در کشورهای مختلف به چه صورت است؟
🔹
مراقبت‌های بهداشتی همگانی بیش از یک قرن است که به اشکال مختلف وجود دارد؛ آلمان اولین سیستم بیمه سلامت ملی جهان را در سال ۱۸۸۳ تحت نظر بیسمارک معرفی کرد.
🔹
امروزه، کشورها از طریق مدل‌های متنوعی از جمله: خدمات درمانی ملی، بیمه سلامت اجتماعی و ... به پوشش همگانی دست می‌یابند.
🔹
ایران از پوشش گسترده سلامت و شبکه مراقبت‌های اولیه برخوردار است و خدمات اولیه در شبکه بهداشت به‌صورت رایگان یا با هزینه بسیار پایین ارائه می‌شود، اما همه خدمات درمانی برای همه مردم رایگان نیستند.
@amarfact</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/680098" target="_blank">📅 21:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
قیمت نفت همچنان در حال افزایش است و به ۸۷ دلار رسیده
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/680097" target="_blank">📅 21:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680096">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEoqro6qUKyWAGMtEgEagdjv67IS6EjkrYLVCtfDiMpvauQsU_SyeeMAOlGofSrqvCqZIlQMJBXY-cICW1yWXencakF-15v8Bgkyg2SR38bxAu6qLv7KBvvKjGjRCwl8YUikorRVYml-eGEjjoOESqP4dv_Uas8qiFawxNC9IC4iSy3qPOXLNmfQyECdATefqg50jw_RJcywGXduG17pLdxuNlDdrvKX33MQ7NFwZ6DaGIgIcB-5XOl_ZzCVJ8mfYqoc2gSll7LxxoaPzxxQDzgyy7HbMltMo6d0D-TzwxC67vdzSRk2214yvZqcYOPJmdH_gVr5YEwoMsurZKFi7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ به نقل از یک مقام کاخ سفید: ترامپ مهلت اجازه به کشتی‌های خارجی برای انتقال نفت و سایر کالاها در داخل کشور را ۹۰ روز تمدید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/680096" target="_blank">📅 21:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680095">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44abb3be14.mp4?token=SqK5rbYRvAMHVrINiJPKQIwudc5hDZEGfm3GBOiWb8RAr7wFF2VCnKWcqB-6_HMq3A-dlcc2qLbz_nv69F__tJ1y7r-pSXrIucj2HK1zIuhrt7-HCG-yW8xJR5ZxnGP-tKAO334dPzAwcgfK0TgVzqY_FG6hE3pkMeX5P3TcFd-ciTzo0azoAgIiyLWn_e8CjqrVhGHUMhyOGDDbnFIVY1wIoZXAmqpLPmIAWsFKVCmYoHqwqRy9FzW5R9nDRYlC2sBYl0t07TtHgeO0fxA2eddn8wTf-HPpAIzgDFdfKRUV7-WUrtW37LHnEc7Q2-4M2HRkzXLqe6hSIZrpuDhnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44abb3be14.mp4?token=SqK5rbYRvAMHVrINiJPKQIwudc5hDZEGfm3GBOiWb8RAr7wFF2VCnKWcqB-6_HMq3A-dlcc2qLbz_nv69F__tJ1y7r-pSXrIucj2HK1zIuhrt7-HCG-yW8xJR5ZxnGP-tKAO334dPzAwcgfK0TgVzqY_FG6hE3pkMeX5P3TcFd-ciTzo0azoAgIiyLWn_e8CjqrVhGHUMhyOGDDbnFIVY1wIoZXAmqpLPmIAWsFKVCmYoHqwqRy9FzW5R9nDRYlC2sBYl0t07TtHgeO0fxA2eddn8wTf-HPpAIzgDFdfKRUV7-WUrtW37LHnEc7Q2-4M2HRkzXLqe6hSIZrpuDhnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد هواپیما با یک خودرو در فرودگاه میلان
🔹
یک خودروی خدمات فرودگاهی حین مانور در فرودگاه «لیناته» میلان، با بخش جلویی بدنه یک هواپیما برخورد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/680095" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc830b3a13.mp4?token=mTHjpa-5tnOs2L3vA_YLI296Q_qtCueBi2rdv_Horbmi1y-I8HRQGzA7I7V8kvu9jVFDLfineXpPFkjlnrtUfoFvP_CZrfsdNwpE8R6uCMTMnf5fkVa7h_7Hr8OjUF0IFckPdLBEYwPVrzqa7AZLOKPFL4WbKEMePby7w3Y8o93olDwjZ9tN5tgMBTXMvL0pDCB_Cu9tXcYZHp3Z0pC5WqYAmatUKgFoHadvr3giXEr2sw_cdG5sHEU--PVkWm6HbDkPv-T2wHYhennn_rCBHtLMlzB8zyHmnA3ijqZ1wxC2bTCjso-EXUQU1tNBpLiia8KgX7VgI3E8bkzjkRmTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc830b3a13.mp4?token=mTHjpa-5tnOs2L3vA_YLI296Q_qtCueBi2rdv_Horbmi1y-I8HRQGzA7I7V8kvu9jVFDLfineXpPFkjlnrtUfoFvP_CZrfsdNwpE8R6uCMTMnf5fkVa7h_7Hr8OjUF0IFckPdLBEYwPVrzqa7AZLOKPFL4WbKEMePby7w3Y8o93olDwjZ9tN5tgMBTXMvL0pDCB_Cu9tXcYZHp3Z0pC5WqYAmatUKgFoHadvr3giXEr2sw_cdG5sHEU--PVkWm6HbDkPv-T2wHYhennn_rCBHtLMlzB8zyHmnA3ijqZ1wxC2bTCjso-EXUQU1tNBpLiia8KgX7VgI3E8bkzjkRmTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی مرعشی با ریش یوسف سلامی: بهترین ریش دنیا رو داری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/680094" target="_blank">📅 21:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyD20qz43MkXAT-uVOQEWhg2te0FqavQncLyjfTD5O7hMubftQBgVzyDBFy2-8LQkOH5s-X0GtedJzkKkrexA3-oEbqjAXqTGbJg3DbVEannyDIvsUk1Ujr4PIzM152l2LGf8sKRaa-9p51XYkNcUOouS1LuplU5bbb8ghgpAOO4l5alQSn1tp5rpzKXZ9beEB524tkGGTAQ6qdTv-stCfF_iQ5thj5Oq3pdFjSaSOSvT34KgGOOdwhD5yuq3TVNTxRHDxlFP8ZcllS-i6VRSjrOTkGoMZ0CFQb1X_ljCXWVNyjBm1pqKjLn2on72AqVXL23MlFspdMZE_7o5SEs0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متری شیش و نیم
🔹
کارگردان: سعید روستایی
🔹
ژانر: جنایی، اجتماعی، درام
🔹
بازیگران: پیمان معادی، نوید محمدزاده، پریناز ایزدیار، فرهاد اصلانی و…
🔹
خلاصه داستان: یک پلیس سرسخت در تعقیب یکی از بزرگ‌ترین قاچاقچیان مواد مخدر است؛ اما این پرونده خیلی زود او را وارد…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/680092" target="_blank">📅 21:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680091">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رادیکالیسم؛ پاسدار اصول یا مانع وحدت؟
🔹
این گزارش با نگاهی تاریخی؛ جریان‌ های رادیکال و نمونه‌ هایی از تقابل میان جریان‌ های سیاسی را بررسی می‌کند و در ادامه به این پرسش می‌پردازد که در مقطع حساس کنونی، فضای سیاسی کشور تا چه اندازه به وحدت، گفت‌وگو و مسامحه میان گروه‌ های سیاسی نیازمند است.
@TV_Fori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/680091" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680090">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxhi3rPI1B9QFJ7BjZhG0eHdCxXqLAp2j2uKikjsJe3kvaZN_MUMsehSRFtZwaTkYylhw6QWDaUpK5gMRaZOr4T9C3-O1WZmQFd_weEQtF6GQyI0pu_Ses_DTxo3r0Jc40N203mgtOYTENsTgSd2TpNRADWUZvbjAFlPc-GYOf5BgHSkaQsEIub4rjm3eKHF9uJfFirwyI3hbWgUZ2fncpr6sz_v3X7lS4UTNhXp42EsVgxM_M_BIX0voS2DqEDYo73OOulVrVsD7UL-ZTABVaYgyddkS6xKnIWnh3je6nAqMVJaxEoEbVfFKhjN7zUf5ZuOrBNfcfuWcYPvZoHUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت همچنان در حال افزایش است و به ۸۷ دلار رسیده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/680090" target="_blank">📅 21:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680087">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323c86efd9.mp4?token=f5FjRX7WDVkzRbKBWtjlNoGC0AmKlQOfypY0W2Oya0_9oaS-Mcv7NkJN0LGjTzpTI2iQiC2kIIIym7DnFOTFoPDN631d5pwTWsSYGJs5fecJJVBrQvauVZoURRjjQ9TTorQemNOGTeT9EqaiaJLm1EMWeT4sPXUP-WNxte1p7hWOe5GB2GLR22Gva46jjai3YVXJe8rSOeQlqkX2HyfFvp1MelWwKFQpyX9ca2LQIWluH28LCXxE6Z8y427gb2dpb7Hn14kyrpT-TO0tH2n1V2hT7G--nKH_F9-zPpsWphG-4vBxmy6jGVIrwuEWEVG47zClbNl0-aYTMAuPdHWS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323c86efd9.mp4?token=f5FjRX7WDVkzRbKBWtjlNoGC0AmKlQOfypY0W2Oya0_9oaS-Mcv7NkJN0LGjTzpTI2iQiC2kIIIym7DnFOTFoPDN631d5pwTWsSYGJs5fecJJVBrQvauVZoURRjjQ9TTorQemNOGTeT9EqaiaJLm1EMWeT4sPXUP-WNxte1p7hWOe5GB2GLR22Gva46jjai3YVXJe8rSOeQlqkX2HyfFvp1MelWwKFQpyX9ca2LQIWluH28LCXxE6Z8y427gb2dpb7Hn14kyrpT-TO0tH2n1V2hT7G--nKH_F9-zPpsWphG-4vBxmy6jGVIrwuEWEVG47zClbNl0-aYTMAuPdHWS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر آخرالزمانی از زلزله عظیم کلمبیا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/680087" target="_blank">📅 21:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680086">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
رایزنی تلفنی عراقچی و وزیر خارجه آلمان
🔹
وزرای امور خارجه ایران و آلمان، عصر امروز در تماسی تلفنی درباره تحولات دوجانبه، منطقه‌ای و بین‌المللی گفت‌وگو کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/680086" target="_blank">📅 21:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680085">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تصویب منع تردد تجهیزات آمریکایی و اسرائیلی از تنگه هرمز
سخنگوی کمیسیون امور داخلی کشور و شوراها در مجلس:
🔹
بر اساس مصوبه امروز کمیسیون، عبور و مرور امکانات و تجهیزات با مالکیت آمریکا و رژیم صهیونی و کشورهای متخاصم از تنگه هرمز ممنوع شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/680085" target="_blank">📅 21:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680084">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee69767cf2.mp4?token=qtLNV64RRvBbesdtlraGWLZegLCEz9Uw2HWXc4KriVcv4OHyMEUlDspu76oDgPXjx_GNpJ4G0YjS-Htk1KSy7yr-Lp0kSq4PoSbwAAC1F6by9ipMb2nawzr5jOohRqCBPwLSXJvMe4Wqp1mlF0sLVbQiuSDcviItp9aCv2mn6nIxJf9eRpozxSv-NVOSUBcujTqyGM3201ylDmkIHQxB7bdzet0_8sgILFbWefQ_hdXB25goIO4P91YNPJXLLl5KETBz9eOO5Jz070HS6N_4CPc1gqJJduU0masz9gVf6pjSXfQKnuprrLOWwIFGSMIZaZJWHv73TctyTu7TP_RsxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee69767cf2.mp4?token=qtLNV64RRvBbesdtlraGWLZegLCEz9Uw2HWXc4KriVcv4OHyMEUlDspu76oDgPXjx_GNpJ4G0YjS-Htk1KSy7yr-Lp0kSq4PoSbwAAC1F6by9ipMb2nawzr5jOohRqCBPwLSXJvMe4Wqp1mlF0sLVbQiuSDcviItp9aCv2mn6nIxJf9eRpozxSv-NVOSUBcujTqyGM3201ylDmkIHQxB7bdzet0_8sgILFbWefQ_hdXB25goIO4P91YNPJXLLl5KETBz9eOO5Jz070HS6N_4CPc1gqJJduU0masz9gVf6pjSXfQKnuprrLOWwIFGSMIZaZJWHv73TctyTu7TP_RsxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقام اطلاعاتی اسرائیلی؛ ایران قطعا تسلیم نمی‌شود
رئیس پیشین بخش ایران در اطلاعات جنگی اسرائیل:
🔹
در نهایت، این یک انتخاب ساده است یا پذیرش کنترل ایران بر تنگ یا تشدید تنش و ورود به جنگی که هیچ‌کس نمی‌داند چگونه پایان خواهد یافت؛ اما قطعا به تسلیم ایران منجر نخواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/680084" target="_blank">📅 21:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680083">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سی‌ان‌ان به نقل از یک مقام اسرائیلی: در حال حاضر هیچ تاریخ مشخصی برای دور جدید مذاکرات با لبنان وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/680083" target="_blank">📅 21:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680082">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1739212760.mp4?token=IMuhzpL4_RuAqfNE04bKgW7ZH__WjJYVspqczq5Ghk2fksUKmrWFiw_uG6ABS0bWZYnpcc4C8kqK3T7-veuNN_pl7-6sVq1IIoIaxgHpw63Ona1NjVD_6UbTUsA5tSJF6njEZ1Qj7cqjDoF5Im0Rh_3huC61Y_GyvXg2VCcQdbqSnVHHAbowRUhMhGcK_3CayFYZskN4o8t068Z1hNEU3Rsftn54VTcY1coXP2Kp3DN_YhC75Yrg3i3HI6trgoxtK1_qC9h2A7DUcS6Ho7EmWuEWyjnlo7tJTCIeiDIyY3xYFSDaLhBFqsi91ZDLby5yvaVqvD5QTN1ZZfRKwfkN5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1739212760.mp4?token=IMuhzpL4_RuAqfNE04bKgW7ZH__WjJYVspqczq5Ghk2fksUKmrWFiw_uG6ABS0bWZYnpcc4C8kqK3T7-veuNN_pl7-6sVq1IIoIaxgHpw63Ona1NjVD_6UbTUsA5tSJF6njEZ1Qj7cqjDoF5Im0Rh_3huC61Y_GyvXg2VCcQdbqSnVHHAbowRUhMhGcK_3CayFYZskN4o8t068Z1hNEU3Rsftn54VTcY1coXP2Kp3DN_YhC75Yrg3i3HI6trgoxtK1_qC9h2A7DUcS6Ho7EmWuEWyjnlo7tJTCIeiDIyY3xYFSDaLhBFqsi91ZDLby5yvaVqvD5QTN1ZZfRKwfkN5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ راه تشخیص زردچوبه اصل
🔹
رنگ زرد مایل به نارنجی
🔹
در آب آرام ته‌نشین می‌شود و سریع رنگ پس نمی‌دهد
🔹
عطر تند و طعم کمی تلخ دارد #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/680082" target="_blank">📅 20:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680081">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMB_q0ZmYINo5V9kv7hs5Kmp41HChaKi6FN_U0CDkNxs18RrFx62PgpGIsL5PvAcSY-_tu94E6bKqqwLYWT65EKeF2rXEnjTpp6T1YVRbF-JUu4e3ZTUP86tI1mbq-lpnEm4CGOtHt6SH7rxPZpwh1GfebrTQck6oVime1MNpDi_Q1PcuDb5919puRwZYrDW00UuUNNUaqi5RTDuRoua2rHSxbD28qnRZAzh4-W6gFjSv1-2chG1qbEDq8VAJNuV-LF2jcMbu5Oz5r7R7D5vn2y_lhG6gfkMAj4yfVT5xPnnRowBq_pZ7o4n0JnlPkE9mNOYwdTE3ps64G1rUQa6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینفانتینو به رابطه غیراخلاقی با یکی از کارکنان یوفا متهم شد    نشریه انگلیسی «تلگراف»:
🔹
جانی اینفانتینو متهم شده که در زمان تصدی پست دبیرکلی اتحادیه فوتبال اروپا (یوفا) با یکی از کارمندان رده‌پایین فیفا رابطه غیراخلاقی داشته است.
🔹
گفته می‌شود این خانم در…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/680081" target="_blank">📅 20:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680080">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سهمیه سوخت سالانه تراکتورها به ۲ میلیارد و ۶۸۰ میلیون لیتر افزایش یافت
🔹
توانیر: قطع برق پتروشیمی دماوند برای حفاظت از شبکه بود
🔹
مارین ترافیک: تردد در تنگه هرمز به شکل قابل توجهی کاهش یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/680080" target="_blank">📅 20:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680079">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f2fb02188.mp4?token=gTGJMPJLA5_M2zJ_tvRIe0fbd_evVScPhXZQwcJIWiL65dQInS6xz5vVwplE4I9eRgYSFe2TCyCWqm1TxBReJll2bjtRmwmJ9YP5P3f7qi3mmqGvkLo9CYObFbWuIxnAItc1NbwRXn06jRh8wxUMuLli81I6D0uyGV0W1zcnlkOdl5z6QsuRNrnHChZZeFknXw3tagaonYQz8hi_4g4rDuKp6aDRav6ssVe9wk68dUAHDBxOQXel2GYEpN-JneKyoYF-58J7HfaaSSg_tD_lbSUpWDz5_NZJq-rMFggWTmicItu1yfXqAfxpsNmMCDQbYKmn8UBi9pddT6p7j41E4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f2fb02188.mp4?token=gTGJMPJLA5_M2zJ_tvRIe0fbd_evVScPhXZQwcJIWiL65dQInS6xz5vVwplE4I9eRgYSFe2TCyCWqm1TxBReJll2bjtRmwmJ9YP5P3f7qi3mmqGvkLo9CYObFbWuIxnAItc1NbwRXn06jRh8wxUMuLli81I6D0uyGV0W1zcnlkOdl5z6QsuRNrnHChZZeFknXw3tagaonYQz8hi_4g4rDuKp6aDRav6ssVe9wk68dUAHDBxOQXel2GYEpN-JneKyoYF-58J7HfaaSSg_tD_lbSUpWDz5_NZJq-rMFggWTmicItu1yfXqAfxpsNmMCDQbYKmn8UBi9pddT6p7j41E4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب حجت‌الاسلام ‌والمسلمین حسین طائب به سِمت رئیس سازمان بسیج مستضعفین سپاه پاسداران
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی حجت‌الاسلام ‌والمسلمین حسین طائب را به سِمت…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/680079" target="_blank">📅 20:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680078">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319955d4cd.mp4?token=U2jEAQPSelnBCu7BhGau719pAqk3yAsXs2hlgYtMXGEiAhFgnSaQstUVAJdr8cgHLm27zX_C9SY3ZjtsePbjSNK7ChPBnaj1ViTM8IyFeyUJWlWVICWVNb4nlvP77yc9Tu7f3z5YQvSUP0bUuSd2mN-Lzl5xdbHFmvT2mp_ppEjz9CnfHUhqPnDGSECYc_Be25dj9ZWtqyMc238-BpAao5A0uQtY2Ox9xionYzWWwCE2YEQWY-FFRiAZpNkmdj_zWHxmmvhrC4Y4tC5PKtYF-oTobcBrVjnLY7oN7iEPaR6nP6s2ratqBiuv4xkG2HNixQN6rL3TUjkqmGpSflhnrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319955d4cd.mp4?token=U2jEAQPSelnBCu7BhGau719pAqk3yAsXs2hlgYtMXGEiAhFgnSaQstUVAJdr8cgHLm27zX_C9SY3ZjtsePbjSNK7ChPBnaj1ViTM8IyFeyUJWlWVICWVNb4nlvP77yc9Tu7f3z5YQvSUP0bUuSd2mN-Lzl5xdbHFmvT2mp_ppEjz9CnfHUhqPnDGSECYc_Be25dj9ZWtqyMc238-BpAao5A0uQtY2Ox9xionYzWWwCE2YEQWY-FFRiAZpNkmdj_zWHxmmvhrC4Y4tC5PKtYF-oTobcBrVjnLY7oN7iEPaR6nP6s2ratqBiuv4xkG2HNixQN6rL3TUjkqmGpSflhnrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سردار دریادار علی عظمایی به سِمت فرمانده نیروی دریایی سپاه پاسداران
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی سردار دریادار علی عظمایی را به سِمت فرمانده نیروی دریایی…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/680078" target="_blank">📅 20:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680077">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فعلا خبری از تسهیلات کسب‌وکارهای اینترنتی نیست
رضا الفت‌نسب، رئیس اتحادیه کشوری کسب و کارهای مجازی در
#گفتگو
با خبرفوری:
🔹
کسب‌وکارهای اینترنتی نسبت به فعالیت‌های سنتی، هزینه راه‌اندازی پایین‌تر و امکان بازگشت سریع‌تری دارند و برخلاف مغازه‌ها، نیازمند هزینه‌های سنگین اجاره و راه‌اندازی نیستند.
🔹
با وجود پیگیری‌ها از نهادهای دولتی و حاکمیتی برای پرداخت تسهیلات به کسب‌وکارهای مجازی، فعلا برنامه جدیدی اعلام نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/680077" target="_blank">📅 20:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680076">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a82ea307d.mp4?token=uDFuCcP7kvSNC6VIwBBSo2IMNSmam9PVpBIIpuSoAq5N0mCHmzZYLM3QZSpRf7nxknhfXotuEtpSxOpgjh_j2EoP7iLBC8Hof2drx9rDGWlC96OCzuFxJVusOOWoTDNQzs46N5amqrgJAfOcqWkRePMUIOVDzf5bWmZm1ML90udVeWbuSBKaDkqvjqS7zImlQJYayZfkeTOGcO9MwQ_muDbQy29yrVd1daNQtCnVCvRCqEvg5bo2eR0QvCdt3FBeMYS8hG_jkU4mYTvpVM23kGdyk3_A-V79UB1YYBA_TOqu8BKR4GBfuZUmYjj_H-WY_rSHULnmyFABBaRr0nBEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a82ea307d.mp4?token=uDFuCcP7kvSNC6VIwBBSo2IMNSmam9PVpBIIpuSoAq5N0mCHmzZYLM3QZSpRf7nxknhfXotuEtpSxOpgjh_j2EoP7iLBC8Hof2drx9rDGWlC96OCzuFxJVusOOWoTDNQzs46N5amqrgJAfOcqWkRePMUIOVDzf5bWmZm1ML90udVeWbuSBKaDkqvjqS7zImlQJYayZfkeTOGcO9MwQ_muDbQy29yrVd1daNQtCnVCvRCqEvg5bo2eR0QvCdt3FBeMYS8hG_jkU4mYTvpVM23kGdyk3_A-V79UB1YYBA_TOqu8BKR4GBfuZUmYjj_H-WY_rSHULnmyFABBaRr0nBEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب امیر سرتیپ کیومرث حیدری به سِمت جانشین رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی امیر سرتیپ کیومرث حیدری را به سِمت جانشین رئیس ستاد کل نیروهای…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/680076" target="_blank">📅 20:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680075">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb31addbe.mp4?token=h7IZgaiIH_GloYCpuoSJ35MYQ9ttOyps66XG3OLBawlQk9XuwnBG0JQSAr7V6nfrsnLm-q3XmweU9PbYw4-elZghcylRHrNqFgsfbcreS7UNJMiGdE5cdCKm3-uymcX5yt4Yy5YsSUJOzYZKoffF2S4eQhW4uHnXQVWYOEyqnd8CYa4o0_h23gdPi3PmR8UIC-6gk3HQX8x0DAfy1mMpEFXXES_3bQn9rQGaVUOqahdFpsxWy_OIAfxhD0VW0FnJWx2A-Q_GcVX9Oz45fhcChu_xnu5dI8DehVz00154oPo5naBvj-6hzTp97njkWHp-gLmROLc5t-zKqf50q7dhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb31addbe.mp4?token=h7IZgaiIH_GloYCpuoSJ35MYQ9ttOyps66XG3OLBawlQk9XuwnBG0JQSAr7V6nfrsnLm-q3XmweU9PbYw4-elZghcylRHrNqFgsfbcreS7UNJMiGdE5cdCKm3-uymcX5yt4Yy5YsSUJOzYZKoffF2S4eQhW4uHnXQVWYOEyqnd8CYa4o0_h23gdPi3PmR8UIC-6gk3HQX8x0DAfy1mMpEFXXES_3bQn9rQGaVUOqahdFpsxWy_OIAfxhD0VW0FnJWx2A-Q_GcVX9Oz45fhcChu_xnu5dI8DehVz00154oPo5naBvj-6hzTp97njkWHp-gLmROLc5t-zKqf50q7dhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سرلشکر علی عبداللهی به سِمت رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده معظّم کل قوا در حکمی سردار سرلشکر پاسدار علی عبداللهی را به سِمت رئیس ستاد کل نیروهای مسلح…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/680075" target="_blank">📅 20:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680074">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwYx96E6CCzhnFP0DqKaRjsDQ1EOWeB6crGr2LvlZVIqul3M3NeOtAc7ilFDu6Z8ngPAhKtAoslvVVQklNpQCIXAI9vun-0gTkZi87_-KdMHl68A8fK-w3uFVxvi6Oa4XFiHK-BpSCE134qxOyD7UPOxW0hIoCnijiAqFL2LuqMLn-wrKIr-fZKQ5cS2FHDaTZZF_AFbiV3JRxAwG7zteLI69aKVYMF9mBxWOCvjkL1wLqk0gKNS9RVDXlSzWvV_4qMSEibgOlbv9y3FehlSmFMgaqEUN7IFBda6i-BtjI3DncTNx2Cie-ETm1DAZLk5Nz3QbA5bks2mjiWipmg_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با صدور احکامی جداگانه از سوی فرمانده کل قوا صورت گرفت؛
📝
انتصاب شش فرمانده عالی‌رتبه در ستاد کل نیروهای مسلح، سپاه پاسداران و بسیج مستضعفین
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های شش…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/680074" target="_blank">📅 20:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680073">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvPt4c7Y4LLoUhvFAeMcrolfkySdBxXH-TzUbkpI_GSisN40YPOMRcRWA34CmVMY1gpMzTiJFbOjlATc1FVQNQLXQ6jtHcyI6t7IlZHEy3_VTXZtrwmImp3uBt3C_JB8agGpRFhrFa2Xf1e1ASljglKx3_LDwdaG1vlEvKSQG2HwKl6L7EN3yjVX48cagQWQrH1GznNFUdggfltFypZTySY8UZQ-Kca_wRztYnhZRxzQpecGWWe7vdxNUvxtRg30Pw6ydUiVQ3koEo-ymHvr8dFXgNlDueAQqI25mw8rUTof6RCSeZQsoCviEyw-epTPlnvxyQbfPSVY1WGlnV8S3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ایران قوانین را در هرمز تغییر داد/ عربستان، ترکیه و پاکستان به فکر افتادند
الجزیره:
🔹
خلیج فارس در حال تغییر قوانین برای ایران است. ایران از جنگ به عنوان اهرم فشاری برای کسب برتری بر تنگهٔ هرمز استفاده کرده است.
🔹
اکنون عربستان، ترکیه و پاکستان در حال تشکیل یک ترتیبات امنیتی جدید هستند که می‌تواند تا حد زیادی مانع از پیش‌برد مزیت‌های کسب‌ شدهٔ تهران شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/680073" target="_blank">📅 20:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680072">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
وقتی از کما بازگشت؛ روایتی عجیب از شفا و یک سفارش مهم
🔹
00:12:45 صحت خواب مادربزرگ از حادثه تصادف
🔹
00:23:40 هم صحبتی با روح فردی که در زمان کما بودنم، فوت کرد
🔹
00:31:00 حضور فرد نورانی و دست کشیدن به شکستگی داخلی بدن که بیمارستان متوجه آن نشده بود
🔹
00:35:10 سفارش حضرت موسی‌بن‌جعفر برای حق‌الناس و طلب حلالیت
🔹
00:49:50 کارهای خیری که نجات‌دهنده شد
🔹
00:57:30 رؤیت سقوط افراد عریان در دره‌ای خوف‌ناک
🔹
01:03:05 اهمیت دادن به خواندن نماز اول وقت بعد از تجربه
🔹
01:12:00 نیکی کنید و بازتاب آن را ببینید
🔹
قسمت بیست‌وهفتم (حلالیت)، فصل پنجم
🔹
#تجربه‌گر
: سید‌ امید متقی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/680072" target="_blank">📅 20:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680069">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URZBPHxwuH9LDpfNEOIUd1ZEuK01VGH7CLW-mVxHKVlTD2PURG9LDbRV8MCTgnLNzRZT4TKpMdHXuf81w6MKMJAEBprTF0kBSpCUwx6kW5cKTchCHmVkQFe6ZAkgbtdpNN0BCF1N3C8lfHm6R4qLiHWPhaAtnwowCprPn0aAciENg7CF90SGcVboak4CDVkP7TIeMx2D71AVGx5lJhLX1KqF19uRWF0_hXvFBANWgQzWUefCtMKZmqjunGlt8ummwfMntOg92bnT_XzcCl8RkMU9jG-PRPHLG3-97n4dw-h7IcEA1VQUQNBjmcn6MruFZh2J5KkYYYxXuDa_8KaD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمرکز؛ قربانی اول استفاده افراطی از شبکه‌های اجتماعی
🔸
در این نظرسنجی بیش از ۲۶ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۴، بله ۲۸ و تلگرام ۱۸ درصد بوده است.
🔸
شرکت‌کنندگان به ترتیب: افت تمرکز، آسیب به ارتباطات حضوری و اخبار زرد و شایعات را به عنوان بزرگترین آسیب‌های استفاده بیش از حد از شبکه‌های اجتماعی معرفی کرده‌اند.
🔸
استفاده افراطی از شبکه‌های اجتماعی می‌تواند با پراکنده‌کردن توجه و کاهش تعاملات حضوری، زمینه را برای مواجهه و انتشار بیشتر اطلاعات نادرست و شایعات فراهم کند.
@amarfact</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/680069" target="_blank">📅 20:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680068">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJXFhi3cX2CgqPNPJOgy00s0sHENr_xYjmGZDOOS75LitGmwU-cl6pCH3k-SILqy5AfMWGig9_f7wDoyq-n_D1kAipILhZNjXrFO-zc76Yu93pniQS8ECZyMtQ4JdzDKS9we5wZbX566Ud7dTZhU1kEHFn7L6bytlxyj_vWo5o6JLYAAC4--RvoBSXvgeB0P5OJgYImG9gt-2IyHSNLInhEH9wg-fSmaguvtkS4QE6oVsCMEFfdBlgSmym4wJ5G-ztwiMAfYe_M-f-TyqFhTKWyasoGYjiIv2eV5VX-kGJgpweWyT4LuzPdAyADK3ZTqTrnltGqsKRaHtgFWN_CJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد: من هم از ایران می‌خواهم خسارات ما را جبران کند
ادعای ترامپ شیاد :
🔹
ایران خواستار جبران خسارات ناشی از درگیری‌های نظامی پنج ماهه است و من نیز از آن کشور خواهان جبران خسارت هستم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/680068" target="_blank">📅 20:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680067">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg3P0RKaesqaYjrnrAlR_LYiqZ6GozErv3Rb5J2HEFz38p-AHY-umgGQys8pLMuxtI2C5RvPUMgjFAo6MjatYrfBoPN1X_PpdunYkWBDoThB2YKnyV7m2-irKVpA3MTwivtGmHMLdEv6GRZ2NveAfbDwzpehVk_bwJ9iZSIcYKdMRAsCEOV1S0LPKFz99xG0tiYSbj-eZlAWv1Utch-202LYxeuEEINsnBwlQMbu67-XYoSorI6VMaz7B8oy4zwmmBr8N6AreP3XB9exDTTKTtF8yumt3pdU8zUPCRGlpASkAuDpX8s3_J1zxB4L7TBR-Vu8RWkPyR9V6Jm5devF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/680067" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680065">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcZ7eU_wILpQijxXTSafgl4JJvDOpOQUfVcKRGU2kavCX4HPwa__Ie6uq1I1GJj922d5lyZWEW0zeC2E4HkHZAtzpKi5ws86j3_-XozKvcBwbaBeP2T-VeKCWh6ZmGsgFJTXC8r-pNMUM6WuHfr89d-n0UUmnpfoB6GPSOJzFnoepjMd8BT0rETRhMXPQZjHin6SVLbK-3cWa0t6NF5sJd7DglLt5oUl_MAAsnjQ_K1xyyeVwYmvikUVNsGs7xAdVHTENl8y6YAJ_0UF797cdUzzui_Bf-l2BuliAI34g3FV_vIGtlADlq8unP-CdTUIVf6AQsHGYgw7PVNilFpYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی: ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج شدن برای یک حمله برق‌آسای بالقوه احتمالاً در کنار نیروهای اسرائیلی علیه مردم ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/680065" target="_blank">📅 20:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680064">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2fc31183.mp4?token=CJlJZni7DOF_d4AB-puEhx3pk8Q7V4jLJjtFZZxB5IvTJT9YpFRHfQLsH1w4qjvJaEJ-Y3-2o9WS4Z5FH0jHf1JyadBg_fKBL_Pykl8dcI_ZGwzrYHhx3gpXU1nu3HGaLtUwhASAYmh8bOK_OOTPEE7iraAYKqALDtZju6YJDgSu-ShlseeXQURwx7_E6cMzFXr2ZZQbM263V4CQjI-4sNpDeLRL51FfzOUwmMKvzbcrQFt7u1jptzJkJiCrGNB1IzfnN82FpZAQuhR8aU-9QXmbbaSehb_CwqNSm7nsdcWykkOu18pe-aHihKwe5e3OCb1CzH2AkJ0c6NDyxZMmkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2fc31183.mp4?token=CJlJZni7DOF_d4AB-puEhx3pk8Q7V4jLJjtFZZxB5IvTJT9YpFRHfQLsH1w4qjvJaEJ-Y3-2o9WS4Z5FH0jHf1JyadBg_fKBL_Pykl8dcI_ZGwzrYHhx3gpXU1nu3HGaLtUwhASAYmh8bOK_OOTPEE7iraAYKqALDtZju6YJDgSu-ShlseeXQURwx7_E6cMzFXr2ZZQbM263V4CQjI-4sNpDeLRL51FfzOUwmMKvzbcrQFt7u1jptzJkJiCrGNB1IzfnN82FpZAQuhR8aU-9QXmbbaSehb_CwqNSm7nsdcWykkOu18pe-aHihKwe5e3OCb1CzH2AkJ0c6NDyxZMmkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسر بازنشستۀ آمریکا: ایران معادلات را از هسته‌ای به تنگۀ هرمز تغییر داد
ویلیام پاتنم:
🔹
هدف آمریکا همیشه این بود که ایران به سلاح هسته‌ای دست پیدا نکند اما امروز تمام تمرکز آمریکا روی بازکردن تنگۀ هرمز است.
🔹
اقدامات نظامی آمریکا تاکنون نتوانسته به اهداف تعیین‌شده علیه ایران منتهی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/680064" target="_blank">📅 19:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680063">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-0EfHWFBC7uWxkUEONlSn_aWaHXrKQEKXFF6vNVQtrie-aQ5OSISkMj9B4iQGXt79L8QczZop773D4zQNT6FFld57tnigVJdIAqB0r3pQlxHNJeKIW_mRYtawDWQtcKaAc3oHz5XTRQ3W_KNjv7I2I_8EPtRxvZ0Zdt1_kNxb5m2Cvc1R-1fpbGfO45NQjAhoQAStQ-OaM9qtbZ-nqNMvPmmymgXrwrJaAhP7osKSpiFe3lBQCwkNJAvsmxWzWSSWlxOYWFQ1DBMd-E1qwoVdSBk8EmFHaERLqf6BDQbjm5UrvSCunZivmtqhS0SSZOh7_s-EYVVm1sOHOELVenMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر برای نوشابه‌خورها؛
نوشابه چگونه می‌تواند به گسترش سرطان کمک کند؟
🥤
🔹
پژوهش‌ها نشان می‌دهد فروکتوز می‌تواند در برخی شرایط به رفتار تهاجمی‌تر سلول‌های سرطانی کمک کند؛ اما این به معنای اثبات مستقیم نقش نوشابه در ایجاد یا گسترش سرطان نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/680063" target="_blank">📅 19:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680061">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
کاهش سوخت‌رسان‌های آمریکا در فرودگاه بن‌گوریون
شبکه ۱۲ عبری:
🔹
ارتش آمریکا روند خروج و کاهش تعداد هواپیماهای سوخت‌رسان خود از فرودگاه بن‌گوریون را با شتاب بیشتری ادامه می‌دهد.
🔹
گزارش‌ها نشان می‌دهد شمار هواپیماهای سوخت‌رسان آمریکایی مستقر در این فرودگاه، به عدد دوران آتش‌بس (حدود ۲۰ فروند) نزدیک شده است.
📲
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/680061" target="_blank">📅 19:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680060">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQTtCoojAAyXBaZp5wGDDd05NIzoIkJ4z8a-azBRM8VoMXvH4y5p3zLYGbWq03mCQSdbvMroapm0jNBMeR9Gtx3yFKn9-i3VF8P5afZXHWf0XbIAMYo1zDLBqwDDIVdHcxCF_eh4w5NnPWdB8ml9XmyhVwPJdPD-nHkr8N7aOizCGswbCcjt9K6YuoVTDeMRlFUHBSsn_4wPxVRoq0EAcmm6GjDrhOfRERpk7pWi_l4uQERjCQn4D2KjXVka-uis1lFxFPtcV04bs4yyd81CJYTQMCCpwZiObSW-u7mWjnbRl1JiT7GqiK3U3fELEL5VZD5Jn2TwwRqwBwxWNNSQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سرلشکر علی عبداللهی به سِمت رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده معظّم کل قوا در حکمی سردار سرلشکر پاسدار علی عبداللهی را به سِمت رئیس ستاد کل نیروهای مسلح…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/680060" target="_blank">📅 19:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680059">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcsVTrBpQ1F_LYi55wcPVT4ODdJT4WghlJsvWqlCpw_NtDw4yvxtsVabcWZNH14RfAOkiDcOnWjJyiLlrHGKCJAyWLcj2qEDMYplznbxITCVm17RqGAkv82BKhNCJ-9GB-gQa3H_yv9TlA9RgQsvrqVsq5pXMwNswUMe4jcL9SuyetbaDrQklxnAgLLQ6kVHFVT4uwpfv5vhKoNnzpmr_JU94tKBr8ohb2ca3m4HGsL_s_rFj6eAVKzO45sfI0FQ3fsiIbjZSLrGuTOt6Eore7VidngMc9Hi6zE01t0nZ9iApm8naB1JD2oIbeoBzPM-_QXn6l5nWwUJQvpdj3dTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی به Word اضافه شد؛
چگونه آن را فعال کنیم؟
🔹
افزونهٔ Autopilot را نصب کن، درخواستت رو بنویس، نامهٔ رسمی‌ات رو آماده بگیر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/680059" target="_blank">📅 19:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680058">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJLi4guRrQml5Umhc5AFT2NDYkD0_YFR_-_5MlGRrYAmf2ev_gGpc7cWdt180GRQkh8KMSmBZWyHHDwuQZxtlG3-jPQaQJrk8GmfbtQj5WcRmKWkvlKYCxrA8j2ijYyIVLHk1d8Z2Br1tkBSN5yeT_bNHdIfjJi6ZIji2C2UES4Z3c6vKdi6Dv2_jXPLQIAH-zKSQoSbyaWk2Ji-S1HaEFcT2Lkp42E-UY7mqxjHiPozJ5EKSrKqyTwiXiQnQ-dwxfAjgPUW2Ww8SLjMOwMISazUrzJTZnTxRj0ZNIhOqa7sQIIkItgpiVOav9UUicvQ6R1wKwyyz1pec41BFlS2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنگه هرمز؛ اهرم فشار ایران برای بازگرداندن ترامپ به توافق
🔹
ایران بازگشایی تنگه هرمز را منوط به اجرای کامل تعهدات آمریکا در توافق ۱۷ ژوئن (رفع محاصره، لغو تحریم‌ها، آزادسازی دارایی‌ها و عقب‌نشینی نظامی) کرده است.
🔹
مذاکرات با عمان نهایی شده، اما بازگشایی فوری نیست و به تحقق شروط ابلاغ‌ شده به آمریکا بستگی دارد. کارشناسان می‌گویند تهران تا حصول اطمینان، این اهرم فشار را حفظ می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/680058" target="_blank">📅 19:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680057">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36a60f89dd.mp4?token=ormAawlbf2IzJxRQuFCsXTZdbIdIxCJ9PVdP7QN4g1LBXiSK5Xcp4_Heap1Ev4r-63tUcI6n0sygUSIaAQYN7ZJGwzzSwqiOKE_UBsd3XaWVEu3BHogeQdtO_WvNRBdU9DfeNAVKM7cnqbbv1LNdTSoQzoW1SURlxXCDcsYihG2xRYe2JhjO8szU8pnnDFoVtwaP9n-lugXK_m6HappfaTT_TpgpICZXAz7aLfs7479HENQELSGTjtmkgYy2zivyrRb3-Ijf8cQmudSwcqWro0ggcKIZ9-R7FK9sHtFwXi7ayjQI009fQt_qFgHxKfFyATDohLe1yhwmN9Xg46SopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36a60f89dd.mp4?token=ormAawlbf2IzJxRQuFCsXTZdbIdIxCJ9PVdP7QN4g1LBXiSK5Xcp4_Heap1Ev4r-63tUcI6n0sygUSIaAQYN7ZJGwzzSwqiOKE_UBsd3XaWVEu3BHogeQdtO_WvNRBdU9DfeNAVKM7cnqbbv1LNdTSoQzoW1SURlxXCDcsYihG2xRYe2JhjO8szU8pnnDFoVtwaP9n-lugXK_m6HappfaTT_TpgpICZXAz7aLfs7479HENQELSGTjtmkgYy2zivyrRb3-Ijf8cQmudSwcqWro0ggcKIZ9-R7FK9sHtFwXi7ayjQI009fQt_qFgHxKfFyATDohLe1yhwmN9Xg46SopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجموعه‌های تابعه شرکت توسعه نیشکر راهی بازار سرمایه می‌شوند
🔹
دکتر علیرضا کاظمی در حاشیه برگزاری مجمع عمومی «شرکت توسعه نیشکر و صنایع جانبی آن» راهبرد جدید این شرکت را ورود مجموعه‌های تابعه به بازار سرمایه دانست و افزایش NAV را از نتایج این استراتژی برشمرد.
🔹
مدیرعامل «شرکت توسعه نیشکر و صنایع جانبی آن» افزود: در همین راستا خبرهای خوبی را بزودی از طریق اطلاعیه‌های مندرج در کدال به استحضار سهامداران حقیقی می‌رسانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/680057" target="_blank">📅 19:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680056">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6888c6d752.mp4?token=LFGIYXptTPrRU2r9qbPiMVvEEsLdE7-_YYrft7MhVhZ7ORNxqiJsJq8g6ruc8xtYLDuWM3FpiNg8vxIA6C02B7a-ZP-jqRwFnUN13gJAK8rTcNvHXHHjSPUQKiYetg0jeNdPlB-E4w1EwH0GLWdbrU8O4jf4ETuPaqUXiB3uFdMDsRu2kshT7BnXenUsoRoX_VRx1A0wtSfpAZM_rfl5f_un-NPuK_Wc67ZyKg1Opqd3OZS086BYj_TcCfpZWWIoLNHJvuERrn3W79iCpdOWtOZE7Yge8wVLTnYG8e1NABAPPtmjZX9OrgpHEEz4iYM3yH6datFIcOM3G6GHEz9BTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6888c6d752.mp4?token=LFGIYXptTPrRU2r9qbPiMVvEEsLdE7-_YYrft7MhVhZ7ORNxqiJsJq8g6ruc8xtYLDuWM3FpiNg8vxIA6C02B7a-ZP-jqRwFnUN13gJAK8rTcNvHXHHjSPUQKiYetg0jeNdPlB-E4w1EwH0GLWdbrU8O4jf4ETuPaqUXiB3uFdMDsRu2kshT7BnXenUsoRoX_VRx1A0wtSfpAZM_rfl5f_un-NPuK_Wc67ZyKg1Opqd3OZS086BYj_TcCfpZWWIoLNHJvuERrn3W79iCpdOWtOZE7Yge8wVLTnYG8e1NABAPPtmjZX9OrgpHEEz4iYM3yH6datFIcOM3G6GHEz9BTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران؛ قدرتی نوظهور در باشگاه قدرت‌های جهان
!
شبکه آی۲۴ اسرائیل؛ دکتر محمود افندی، کارشناس و استاد آکادمی روسیه:
🔹
آمریکا نه در یک باتلاق، بلکه در یک فاجعه گرفتار شد؛ زیرا نتوانست به هدف راهبردی خود در برابر ایران دست یابد و حتی نتوانست توان موشکی و پهپادی ایران را از بین ببرد. کمبود مهمات مورد نیاز این جنگ و فرسودگی توان پدافندی آمریکا، واشنگتن را به سمت راه‌حل سیاسی سوق داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/680056" target="_blank">📅 19:34 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

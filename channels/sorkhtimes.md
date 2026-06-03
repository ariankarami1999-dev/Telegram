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
<img src="https://cdn4.telesco.pe/file/aOPv305zWY44xK-1CFCpqMVw2x5H_K6811fyCdn0xkptRT9FY-rEmcEmixJBBPT1uV2NoksL5q3Yix84M7cWpJC9qEG-XgpgWfZnQTIYBfR1NQtyjiBU0KNjTQa7gjZjsqKKQY4CADVHB1xrX1PsHEWjfaS-GlAM8IZvu8y88juDVvS-Y6hZBbGJqL0QMIQbUTTcCRlyMzjDufD-1Ab9S1o4vjSyWk0rxdUqoh_uObCZZwRjSawf_2mw7WALh93x7HKlPB7WpnGNKSENaLoBwXyrwND-QuMGZLE0kn8Vmhx-j72GSJmh613pn-WN0Sd2gc1hoJost9FTCCx9tJqxFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-132692">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06335497.mp4?token=aKoYRcsqRfpzyCDBrulirQ4eSbIxF3H5DVsd-oc7LZmCgDmVrzeIcfLvRaET-6N3CxWbnybo7CnyQwp5ENFd2sVVMVHvwsdTtLebdeicL1tdoYk0WRMH7bFGdFNtKBmrbBd5z1CPJvvwyjiSBxFGjifIn4akACxziStl9hes7yaZvFvTmG6wx5wQE2WezgUahSSN06pdicSJx-NdUhJvRBb6LldLi6KhylSVqgG5IUTN7EkDlwLcMjcCvy3k7fOet2IUQSMuxia-q65li0ESyvBd7f7utAG_TV9yOXdIM8kBRLgaRUiYPfVYcnikLD_5hJIHlCTJ0kij7vrUxRlc9SnaNjhx38HuHgZxyugCceaKZscMiBoODY1ozYv9jMffS4IFvqSJXslwt9dxgTeqV7O5iSX-OGti9PoH0Osy7gUgf35zk-pnX-ni-Xdkt4cxYtwBtoOiyb1R7gU9lkLpehC9SkqtYnjyX9FQhrT4xH16V8Ua0-ReXuAT2uv5MKZFKplbLiH4gd-JLlYph0Wx5-_ujQ_vJTZAtkBxxvvySRNWYlqUtFVAYmgSbS6Y2CW9LXHHdmc6-tzEVdC27X-zqvMgWfwvJjaahBLKQwOdJ7KvyZG2GB1gGxnBJb-PHrWDnvzuTRQ9uTxNVtLV4s0tjic4NwHLu4dQ-LEFKD7O3DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06335497.mp4?token=aKoYRcsqRfpzyCDBrulirQ4eSbIxF3H5DVsd-oc7LZmCgDmVrzeIcfLvRaET-6N3CxWbnybo7CnyQwp5ENFd2sVVMVHvwsdTtLebdeicL1tdoYk0WRMH7bFGdFNtKBmrbBd5z1CPJvvwyjiSBxFGjifIn4akACxziStl9hes7yaZvFvTmG6wx5wQE2WezgUahSSN06pdicSJx-NdUhJvRBb6LldLi6KhylSVqgG5IUTN7EkDlwLcMjcCvy3k7fOet2IUQSMuxia-q65li0ESyvBd7f7utAG_TV9yOXdIM8kBRLgaRUiYPfVYcnikLD_5hJIHlCTJ0kij7vrUxRlc9SnaNjhx38HuHgZxyugCceaKZscMiBoODY1ozYv9jMffS4IFvqSJXslwt9dxgTeqV7O5iSX-OGti9PoH0Osy7gUgf35zk-pnX-ni-Xdkt4cxYtwBtoOiyb1R7gU9lkLpehC9SkqtYnjyX9FQhrT4xH16V8Ua0-ReXuAT2uv5MKZFKplbLiH4gd-JLlYph0Wx5-_ujQ_vJTZAtkBxxvvySRNWYlqUtFVAYmgSbS6Y2CW9LXHHdmc6-tzEVdC27X-zqvMgWfwvJjaahBLKQwOdJ7KvyZG2GB1gGxnBJb-PHrWDnvzuTRQ9uTxNVtLV4s0tjic4NwHLu4dQ-LEFKD7O3DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویزای اعضای تیم ملی برای حضور در جام جهانی صادر شد
⚪️
سفیر ایران در ترکیه: ویزای اعضای تیم ملی برای حضور در مکزیک، امروز صادر و تحویل بازیکنان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/SorkhTimes/132692" target="_blank">📅 15:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132691">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🖍
دو باشگاه پرسپولیس و هوادار تهران برای واگذاری امتیاز این باشگاه لیگ یکی به باشگاه پرسپولیس به توافق رسیدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/SorkhTimes/132691" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132690">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
تسنیم : یحیی گل‌محمدی به جز باشگاهای عراقی یه پیشنهاد مالی خوب هم از تراکتور داره و ممکنه بره تبریز!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/SorkhTimes/132690" target="_blank">📅 14:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132689">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR6IAGs43A2aooBy8soRpWK1wFowUasx3Gwe21hOFwxeZ80Jxv2qnzHsiUKJ4PwZedoQt8-5PVqb-vk1UUeewsOY5Q5rFLORDKQrsH8HbosFEzUnbF6aZ0dvYRtTsW80h3wGq1rM543usqHuUqj8f8AmJxRcYKshdW23EmJQ5KHl-DqGDhWxYzIgomJ-DuKb9sQIoFmfxcCnuzNn2afdWQjgqpu6BovT9m7-4wt_XWwbUzVNeZBszCdFMn6tiPDyNijH31bmVua3YjaTJYgxa4lLEPj7e-3ab9xfD-Z-PjpikSz6dFSN9_kCUIFX74fYp65PNfGnD22bSBz2LiJvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
رقابت جذاب و حساس برای رسیدن به نیمه‌نهایی رولان‌گاروس، دیدارهای هیجان‌انگیز امروز تنیس رو با آپشن‌های مختلف در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/SorkhTimes/132689" target="_blank">📅 14:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132688">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oThl3KHz3ZlH8uqmkX8CxeuxAh9pOTGCCJW22PJzLu0xmqn6G0AdHlOAMoZt8siyoWNDCsS7TL4rcqRQsXC-hJNE8jr8R2xbPxNh7NQd4NUAeesZBJBp_womVdtSOWBAJQ9OJDVqdPJkF4oqSgv7-BlYHQWDM76YrMfoK_MdYchk-PLLmRbnsVC2B1TQa_djgKLxjWJPNquDXo5St4ILNRcYUPZmreY2w5fXkDab4xKogM4Pfkp4Akf7jBmNTBlsgE88rF8KQZu788feCdFM9hFpn2KwlmnWmrVHk2H2zJxnbNk5fVWHlaHfdnAsTsEyl1GVT0q3ZYVA8Jei79BxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
روز کارگر که ترامپ گفت ممکن است محاصره دریایی ایران را لغو کند 4 مهرماه است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132688" target="_blank">📅 14:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132687">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
ترامپ   به نظر میرسد که ما با آیت‌ الله رابطه خوبی داریم دوست دارم او را ملاقات کنم. احتمالاً در مقطعی او را ملاقات خواهم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/132687" target="_blank">📅 14:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132686">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🚨
ادعای ترامپ:
🟢
شاید با مجتبی خامنه‌ای دیدار کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SorkhTimes/132686" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132685">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
ترامپ برای هزارمین بار گفت؛
🟢
ایران موافقت کرده سلاح هسته‌ای نداشته باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/132685" target="_blank">📅 14:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132684">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
ترامپ برای هزارمین بار گفت؛
🟢
ایران موافقت کرده سلاح هسته‌ای نداشته باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SorkhTimes/132684" target="_blank">📅 14:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132683">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
‼️
چین از آمریکا و ایران خواست آتش‌بس را حفظ کنند.
پ.ن: آتش چه بسی هی همو انگول میکنید
🤣
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/132683" target="_blank">📅 13:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132682">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
25 گیگ 300 30 گیگ 350 35 گیگ 400 55 گیگ 500T 100 گیگ 750T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود  جهت خرید از پیوی =>  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SorkhTimes/132682" target="_blank">📅 12:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132680">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOMyg1eWW3EQuJEnK32G4H_z1FPsugq9B2lggwXBe1cpe-LCLgq70DobkcaPRMX3EYzuClavdQm1aJkm9FVv3Nrluw12NdaYj2ykN1cpgKyswjrcMJCKFVI34Ma2bBbbW0LBQ33IWCw57whViK5za1_OvlD14oxy3N3qYtC0Lm2-pFtEJHr4Z-psR9Dn7AGt_KtQ-v13ubLwginOx3t_IRwYmebNNTcV2T1h0ej_SdK4LEMC3IsUKGR79H5jjV6JkgA7xUothvB1Ybst4FkvM-smXDFoVBe8rrS0LIPEgjN4My_zQSvu8roy7xr6ydI_pneIYgsjjHP_Sk9hOHZlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mflcbqo0HYFfWZny1jmRk2ynvOuvGppgciEZ2F4DUCkhYWo3tbH5x0XjK9kk_EpwcEkcxRMM2BC4xwDs4dKOXczI3CKYhyR6um4uOSkm3otVovDr09VCDSahaf5p4GoZfVDW6MXWFsjvuaO6hCuPQASBfdNEq96lknY4abbUspvs2N9wAFGSsCHGrun3YW5WU7Qzavu--X3MeydIeQgj98gh8bbJfzhzuBw01dhQcraQlS7kTkJ_EkuGM2JACoA3MMSgQnR7FJeSxMdfLarr15aTr4nn4evuOkQmDDlxvQdfssSgctTSJr24jLr7PhLLUhQvJFK8h2HyO2QABc97bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وضعیت فرودگاه کویت بعد از حمله شب گذشته جمهوری اسلامی ایران
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/132680" target="_blank">📅 11:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132679">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REkkoD49IHPGp_ULJnsN9GcOZLAyfVPbJpFZEGqgH_nPUcdzPgVXGGmXOj6wqnb82C_LDd1cRyakMG_9CQ5TfSm--GpuE-wo4pv_SGDXB7yhmsquPXROw5og_2byi0xhb1VHppvAaOVn6wXtgoFulS-zh63mAGWDguUASeXo8o_Eq_d2kPUaiHE_qJmXfDo9hujld2mya7hz2rJjCIg3AnS-2a1Fwp_whbFResE_b7Z1hya8k0ghVAOUw8_6E-stWDEeNLuOCPjbm0wSU6W_NU6HmwsdMpWtVffphX2n7aVBI61WCKCPf6yGxg1U75TLetthWBwq-N6OcGvBo-tiFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
دو باشگاه پرسپولیس و هوادار تهران برای واگذاری امتیاز این باشگاه لیگ یکی به باشگاه پرسپولیس به توافق رسیدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/132679" target="_blank">📅 10:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132678">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
توییت مهدی روزخوش، مدیر رسانه‌ای باشگاه پرسپولیس در واکنش به صحبت های زارعی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/132678" target="_blank">📅 10:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132677">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c58750c58.mp4?token=hShpwCIpm4r10VYkfCBY2U42LgC7a9Hp3rtV-LQAt3yBg8DExFryTqlsxfP_I6BJWvsUNGVtdgwBm_kkymnApcRv040NOKx_xIg4qSgTK_VtNoO_iJ2_a3AmGNeg8rduV62edIoMZ4BBTynZrjEfKtWluDvWHvk0omgfWlNWeOraGgMFRTNLNJsrBmC3EYsd9kjPq5quGIeFHhO_h9lYLDBsMaIth-4Jlaxk9LDZwOcLY4dP153gbThuYp5NPxjQ20kwsCHAWU-CWi-uJX6HjIWUHOVxiHFOE7a9iHJ9yTKrMj5hhLhikZ1VI_991xAW-vOtMaK1oHsUb-eqLMZKdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c58750c58.mp4?token=hShpwCIpm4r10VYkfCBY2U42LgC7a9Hp3rtV-LQAt3yBg8DExFryTqlsxfP_I6BJWvsUNGVtdgwBm_kkymnApcRv040NOKx_xIg4qSgTK_VtNoO_iJ2_a3AmGNeg8rduV62edIoMZ4BBTynZrjEfKtWluDvWHvk0omgfWlNWeOraGgMFRTNLNJsrBmC3EYsd9kjPq5quGIeFHhO_h9lYLDBsMaIth-4Jlaxk9LDZwOcLY4dP153gbThuYp5NPxjQ20kwsCHAWU-CWi-uJX6HjIWUHOVxiHFOE7a9iHJ9yTKrMj5hhLhikZ1VI_991xAW-vOtMaK1oHsUb-eqLMZKdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موضع باشگاه پرسپولیس نسبت به معرفی سهمیه های آسیایی؛ لیگ نخبگان یا لیگ قهرمانان 2؟ سخنگوی باشگاه: فرمول ها تعیین می کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/132677" target="_blank">📅 10:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132676">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
25 گیگ 300
30 گیگ 350
35 گیگ 400
55 گیگ 500T
100 گیگ 750T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/132676" target="_blank">📅 09:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132675">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
صداوسیما تأیید کرد که نیروهوایی ارتش دقایقی پیش مقر تجزیه طلب های پانکرد در اربیل عراق را مورد هدف قرار داده اند
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/132675" target="_blank">📅 08:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132674">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c3edbb36d.mp4?token=h4P6La33zm-RLtjCiFQY9is2wUkY7iPGTs1nGbmNy_cVzZC9AuCbCPGF99AKgw9kSaAxh8cMNTCSIfs9G-08XnTc9jmwuVHQzRSDwQutXYd2XgIYyQF1Vcpp4pkQBEoSXHyt3hLn8UmrxdKLiV5BiIXgewLXXC91dFAas73unhRtTd2ShM6bf9LbLQ3Vhkw5ft81p0y-LcBMcljRmBAR4dFVMJRcCmfiFF6_S4ppCF9tX3h_aVjfGV-7sdMqe0fpGq5vBGrYsTkMrxEQbjvx1roSLgUMa8VaB4xVajXZu9DOBpPOiFZRVaMETstrFgPyyxmQ8sLs-w9Qeam0EmEJ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c3edbb36d.mp4?token=h4P6La33zm-RLtjCiFQY9is2wUkY7iPGTs1nGbmNy_cVzZC9AuCbCPGF99AKgw9kSaAxh8cMNTCSIfs9G-08XnTc9jmwuVHQzRSDwQutXYd2XgIYyQF1Vcpp4pkQBEoSXHyt3hLn8UmrxdKLiV5BiIXgewLXXC91dFAas73unhRtTd2ShM6bf9LbLQ3Vhkw5ft81p0y-LcBMcljRmBAR4dFVMJRcCmfiFF6_S4ppCF9tX3h_aVjfGV-7sdMqe0fpGq5vBGrYsTkMrxEQbjvx1roSLgUMa8VaB4xVajXZu9DOBpPOiFZRVaMETstrFgPyyxmQ8sLs-w9Qeam0EmEJ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
انفجارات شب گذشته عنيفة تهز الكويت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/132674" target="_blank">📅 08:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132673">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
🔺
در اواخر شب گذشته
ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگه هرمز مورد اصابت پرتابه هوایی قرار داد
که این نفتکش از محل موتورخانه دچار خسارت گردید.
🔺
در پاسخ به این تجاوز و نقض مقررات تنگه هرمز شناور متعلق به دشمن آمریکایی صهیونی به نام پانایا مورد هدف موشک های نیروی دریایی سپاه قرار گرفت.
🔺
دشمن آمریکایی در تجاوزی مجدد یک دکل مخابراتی سپاه در جنوب جزیره قشم را هدف پرتابه های هوایی خود قرار داد
🔺
در پاسخ به این تجاوز،
پایگاه هوایی و بالگردی آنان مستقر در یکی از کشورهای منطقه و همچنین مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند.
🔺
پیش از این
اخطار داده بودیم که در صورت تجاوز پاسخ متفاوت و سنگین تر خواهد بود و همینطور اقدام کردیم.
این پاسخ ها باید عبرت شده باشد.
🔺
تکرار می کنیم برهم زدن امنیت تنگه هرمز تاوان سختی برای ارتش متجاوز آمریکا خواهد داشت.
و ما النصر الا من عندالله العزیز الحکیم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/132673" target="_blank">📅 07:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132672">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmsvI6g0ux-IdI0mvPUo9CK7mzDHsGEd3cT7m8YapQt-CsQ_k0PMfPWSB1kBY-8Gk0RJY30pPmBLa88zAh__nY4kgJDrLPIta6VYEeyU_s6-BWLGJLb4fRTddBpmVk-S7YV7HWnKYbW5b2hfW7D2lJyjrUFn7X2ueqJ5Z0Z_j-5o2QNoYrNLRlbToFon7iznMyFRlB_ggFtYH3cWLXREo23kIce5Y8JT2VXKfcz4TZquvkQVv3lE33ZGZ-QsocqqMnNIRUCzUnVQQtaeFpbjKj5kxPpcdejCsV6zIdUg84P8i6aZW7mV2gicpudwHKDWTVXgcLXdizrwcFh4NC_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/132672" target="_blank">📅 01:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132671">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
با توجه به اینکه قرارداد سروش رفیعی تا پایان فصل به اتمام می‌رسد و باشگاه هم علاقه‌ای به ادامه همکاری با این بازیکن ندارد، احتمال تمدید قرارداد او حالا از بین رفته و با پایان نیمه‌کاره لیگ بیست‌وپنجم، به‌طور قطعی دیگر جایی در لیست پرسپولیسی‌ها در فصل آینده…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132671" target="_blank">📅 00:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132670">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
حدادی: تمرکزمان این است از بازیکنان با استعداد خودمان استفاده کنیم. عنایت زاده، سهیل صحرایی، براجعه و صادقی و سایر جوانان ما با استعداد هستند.
🔺
یکی از سیاست های ما این است در ۲ یا ۳ پنجره نقل و انتقالاتی میانیگن سنی تیم را پایین بیاوریم و هم به سمت جوانگرایی…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132670" target="_blank">📅 00:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132669">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚩
مارکو روبیو، وزیر خارجه آمریکا:
🟢
جنگ در ایران به پایان رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132669" target="_blank">📅 23:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132668">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
داستان سروش و پرسپولیس تمام شد؛ پایان زودیاک!
◻️
تمام شد؛ داستان سروش رفیعی و پرسپولیس به صفحه‌ پایانی‌اش رسید.
◻️
درحالی‌که در ماه‌های اخیر بارها درباره ازسرگیری رقابت‌های لیگ برتر اظهارات متناقضی مطرح شده و شب گذشته هم مهدی تاج، رئیس فدراسیون فوتبال اعلام…</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132668" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132667">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
یکی از دلیل اصلی که می‌تونه منجر به مازاد شدن کاظمیان و سروش رفیعی بشه درگیری وبی انضباطی این دوتا بازیکنه
🔴
اگه یادتون باشه این دونفر تورختکن باهم درگیری فیزیکی داشتن وبعد اون اوسمارهیچوقت مثل قبل توتمرینات راشون نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/132667" target="_blank">📅 23:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132666">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e855e53fd2.mp4?token=BLtR3P1z9oZI3HWJk1LNZX9sCuzVn9Qf0kKe2UgVoiU_c_X7RF7qW11rGpITwCizsoAMAj3pZ2SC0RtMwCmd3iWY5MdlAAUWzm_PdGl8B_sSORo8AKn_-iYhWGIvfkslvn2Ib_RrSD0aBbFiUqXGE3PfEJ2agDpLF0dRN40a1WmKJ49CWrxgOJ6Hkyl1BByOFkIvVcOX-0p6S_xsQKnBDHYbGl674QFnuvo2zwOCR_pvms1UD_NZsQ6JZSiGTsvTP7swoQkcPF7wtcOD-1Q5vDTqf8rSddwA0UD5_KSq7ZH3SpQPcCY08wPqY5RCfe0cPM-jON6IawWA_TOKxo7UlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e855e53fd2.mp4?token=BLtR3P1z9oZI3HWJk1LNZX9sCuzVn9Qf0kKe2UgVoiU_c_X7RF7qW11rGpITwCizsoAMAj3pZ2SC0RtMwCmd3iWY5MdlAAUWzm_PdGl8B_sSORo8AKn_-iYhWGIvfkslvn2Ib_RrSD0aBbFiUqXGE3PfEJ2agDpLF0dRN40a1WmKJ49CWrxgOJ6Hkyl1BByOFkIvVcOX-0p6S_xsQKnBDHYbGl674QFnuvo2zwOCR_pvms1UD_NZsQ6JZSiGTsvTP7swoQkcPF7wtcOD-1Q5vDTqf8rSddwA0UD5_KSq7ZH3SpQPcCY08wPqY5RCfe0cPM-jON6IawWA_TOKxo7UlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
کفاشیانم آبشو داد میثاقی بخوره
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/132666" target="_blank">📅 23:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132665">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
حسینی؛ سردبیر خط انرژی:  متاسفانه تابستان بسیار گرمی در پیش داریم و زمستون سرد ! توی جنگ اخیر به شدت بخش انرژی ما اسیب دیده و الان اگر چیزی حس نمیکنید بخاطر این هست که فصل گرما شروع نشده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/132665" target="_blank">📅 23:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132663">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
ترامپ: اشکالی ندارد که ایران نمی‌خواهد صحبت کند؛ فکر می‌کنم ما زیادی حرف زده‌ایم!
🚨
این به معنی شروع جنگ نیست. ما فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم!
🚨
هر چقدر که آنها بخواهند می‌توانم صبر کنم. این آنها هستند دارند ثروت زیادی از دست می‌دهند!
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132663" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132662">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
25 گیگ 300
30 گیگ 350
35 گیگ 400
55 گیگ 500T
100 گیگ 750T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/132662" target="_blank">📅 22:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132661">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
شرزود تمیروف مهاجم سابق پرسپولیس با ۲۸ گل در ۳۲ بازی، آقای گل لیگ عراق شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132661" target="_blank">📅 22:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132660">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
حدادی:
تمرکزمان این است از بازیکنان با استعداد خودمان استفاده کنیم. عنایت زاده، سهیل صحرایی، براجعه و صادقی و سایر جوانان ما با استعداد هستند.
🔺
یکی از سیاست های ما این است در ۲ یا ۳ پنجره نقل و انتقالاتی میانیگن سنی تیم را پایین بیاوریم و هم به سمت جوانگرایی از داخل آکادمی باشگاه برویم.
🔺
از فصل آینده لیگ یک، «تیم پرسپولیس ب» در این لیگ شروع به فعالیت می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132660" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132659">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏆
رونمایی از قوانین جدید جام جهانی 2026
🔺
مهلت پرتاب اوت (پنج ثانیه): اگر بازیکنی عمداً شروع مجدد بازی را به تأخیر بیندازد، پرتاب اوت می‌تواند به تیم حریف داده شود.
🔺
ملهت زدن ضربه دروازه توسط دروازه‌بان (پنج ثانیه): در مورد تلاش‌های عمدی برای به تأخیر انداختن زمان بازی هم چنین چیزی اعمال می‌شود و این می‌تواند منجر به دادن امتیاز کرنر به تیم مقابل شود.
🔺
تعویض‌های محدود به زمان: بازیکنان تعویضی 10 ثانیه فرصت دارند تا از نزدیکترین نقطه زمین را ترک کنند. اگر این کار را نکنند، بازیکن تعویضی حداقل به مدت یک دقیقه نمی‌تواند وارد زمین شود و تیم باید با 10 بازیکن به بازی ادامه دهد.
🔺
درمان بازیکنان در خارج زمین (یک دقیقه): بازیکنانی که توسط فیزیوتراپیست تحت‌ درمان قرار می‌گیرند باید به مدت 60 ثانیه از زمین خارج شوند. البته استثنائاتی نیز وجود دارد، از جمله برای دروازه‌بانان، مصدومیت‌ها و اگر حریف کارت زرد یا قرمز بگیرد.
🔺
پوشاندن دهان توسط بازیکنان: هر بازیکنی که در موقعیت درگیری لفظی با حریف دهان خود را بپوشاند، ممکن است با کارت قرمز جریمه شود.
🔺
بررسی درستی ضربات کرنر: اگر VAR (کمک‌داور ویدئویی) مطمئن شود که کرنری که به یکی از تیم‌ها اعطا شده درست نیست، می‌تواند دخالت کند و آن را لغو کند، اما این کار باید سریع و قبل از شروع مجدد بازی انجام شود. این اما شامل برگرداندن ضربه دروازه‌ای که باید کرنر اعلام می‌شد، نمی‌شود.
🔺
بررسی درستی کارت زرد دوم: بازیکنانی که به دلیل دو اخطار از زمین اخراج می‌شوند، می‌توانند کارت زرد دوم‌شان مورد بررسی قرار بگیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/132659" target="_blank">📅 21:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132657">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PI-WgLoNN2EsZmh-msTeGdpvS4JkkVoEOm2333i7LvVdpRECdIo6xPbPEVeR5vsE14HYArkGrbQ3ANKAd_n9Eeje0Jt_E-9Uz3ajn3MhsS4UXYT_zk9nYl7rx8EeNN7nUbhPTDIdTXGXUyeO8YCYfRNHalge7DRDnpWnyY_iNA79xdulEiE1uRbM14bnO6X9HlfDPRb80wBETYjbJuB0KhzqZavYc_x_l7G0pKrFIGORLqWhxmNvg5x_7OS-96RLi_TDcCdOibaoQkLdnd8DzQ9mI888bkK2F4m1rYmcQZlEEv7lPKQ4qisWJyaj84nDFhrsaF0EG5_vLjWAwAn_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⛔️
معمای بارگذاری مدارک استقلال برای آسیا!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/132657" target="_blank">📅 20:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132656">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">▪
︎با این وضعیت اینترنت،
ربات تلگرام وینکوبت
خیلی کاربردیه چون براحتی وارد سایت میشی.
▪
︎هم ثبت‌نامش سریع انجام میشه، هم کازینو رو داخل خود تلگرام میتونی بازی کنی و عملاً کل سایتو داخل ربات داری.
▪
︎پیش‌بینی، بازی، واریز، برداشت و همه‌چی همونجا انجام میشه و خیلی روون‌تره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/132656" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132655">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a6eda933.mp4?token=bi5gzQ3Tmt2eNYZkYo2TBpvvbMwm-KypLiqKnvi4t6LUCO8qNCsiPo6i3b8vwmw6O_XZDpoexUUssy8CO-K75WQTJXeKMhfIKZqeVr8uzhtEStxR4VT1sTR8dFKMfVrL7xopSdpKht4PnFUAKERoFVIwa2CcRVrQ29z-TwGGUJurEMxlt7aIhe1d7HC7jJbBxQeMx0If_3ZxHRlOOAp1sAPEzX6xQ8Rv5StvFOpWwWmEb55IIFG8nULIOdQ9MIuSr__6ExwnkJnIQKglGE7ajQRr9F3q_yk5jIU6fgJNrG83RZ3qZP-qti5F-_3cX11L9UclWQJ3CDkEvuEqP3TgxL9PlQiN0HXINuRgUmRW-p8qEwBATcGgU5tvOoRjkonCwr36Tg_oBPx_7ECbwQZpuuS073XQvWlO8UO9NSjLKgB7q6-01YtdkkzkYfyCuLzamSdrMGWkmn8HyUd-JuwEdmSNji_AwqLbBcDRzptBCXGNeKVQwOe18pX8P29VdLStywnWSCSFszO7-ZudHAzCIMitEv1b5qqeVwdnyU-UgrOgw72esAOaBaiCPMfnjVA_7q_jzkNU5nnz70Bx9iSVRFuJBZ3wO7d4jQM1_lAPY9Vl7uH-52FwLqBHJ-5XaaCCPC5HklbOpOdtlAmGGc9BzCSZ-YZmnOhpcmvrib4USlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a6eda933.mp4?token=bi5gzQ3Tmt2eNYZkYo2TBpvvbMwm-KypLiqKnvi4t6LUCO8qNCsiPo6i3b8vwmw6O_XZDpoexUUssy8CO-K75WQTJXeKMhfIKZqeVr8uzhtEStxR4VT1sTR8dFKMfVrL7xopSdpKht4PnFUAKERoFVIwa2CcRVrQ29z-TwGGUJurEMxlt7aIhe1d7HC7jJbBxQeMx0If_3ZxHRlOOAp1sAPEzX6xQ8Rv5StvFOpWwWmEb55IIFG8nULIOdQ9MIuSr__6ExwnkJnIQKglGE7ajQRr9F3q_yk5jIU6fgJNrG83RZ3qZP-qti5F-_3cX11L9UclWQJ3CDkEvuEqP3TgxL9PlQiN0HXINuRgUmRW-p8qEwBATcGgU5tvOoRjkonCwr36Tg_oBPx_7ECbwQZpuuS073XQvWlO8UO9NSjLKgB7q6-01YtdkkzkYfyCuLzamSdrMGWkmn8HyUd-JuwEdmSNji_AwqLbBcDRzptBCXGNeKVQwOe18pX8P29VdLStywnWSCSFszO7-ZudHAzCIMitEv1b5qqeVwdnyU-UgrOgw72esAOaBaiCPMfnjVA_7q_jzkNU5nnz70Bx9iSVRFuJBZ3wO7d4jQM1_lAPY9Vl7uH-52FwLqBHJ-5XaaCCPC5HklbOpOdtlAmGGc9BzCSZ-YZmnOhpcmvrib4USlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا پرسپولیس به دنبال جذب لیموچی، ایری و آریا یوسفی است؟
🔴
پیمان حدادی: با هیچ بازیکنی مذاکره نکردیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/132655" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132654">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1124c640f.mp4?token=M0HWItkrSiqXZzlx9s_tNUMMenfqJEN7V9o8E-i90FZ1_a6JS_L1L06Qb1gRL3rA1PQ1fTbcjYS1QAnQM3BgNE_8hBDX9wEjL8zAJ1fIwosHl2Cnjzf2ujJGILdBe3-HmU1_ZYFiNOy_iKnAw-0BEhw2Mcyk7DmRWeWUPg-IBWocnBMIQqSfJRmdY9W-X47Vrd25ML9YEPR3rJMCQqIGaeFtcnfWdrKHS6YXoqITvuzCmISFSsjohm76ZJVmPjep7qVjSNRPZDTbGl0ljcD1qRgggsgAOrO4-jI0nN68MxOaAEf-7qQ839M2A0w6wQGS5_QiCu6xpLfiMqtIgUIeJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1124c640f.mp4?token=M0HWItkrSiqXZzlx9s_tNUMMenfqJEN7V9o8E-i90FZ1_a6JS_L1L06Qb1gRL3rA1PQ1fTbcjYS1QAnQM3BgNE_8hBDX9wEjL8zAJ1fIwosHl2Cnjzf2ujJGILdBe3-HmU1_ZYFiNOy_iKnAw-0BEhw2Mcyk7DmRWeWUPg-IBWocnBMIQqSfJRmdY9W-X47Vrd25ML9YEPR3rJMCQqIGaeFtcnfWdrKHS6YXoqITvuzCmISFSsjohm76ZJVmPjep7qVjSNRPZDTbGl0ljcD1qRgggsgAOrO4-jI0nN68MxOaAEf-7qQ839M2A0w6wQGS5_QiCu6xpLfiMqtIgUIeJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل باشگاه پرسپولیس: از فصل آینده لیگ دسته اول تیم پرسپولیس ب در این لیگ شروع به فعالیت می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/132654" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
پیمان حدادی
: با هیچ بازیکنی مذاکره نکردیم هنوز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/132653" target="_blank">📅 20:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132651">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی باشگاه:
🔺
ما باشگاهی هستیم که به خاطر سابقه، به خاطر حضور هوادار، به خاطر امکانات، به خاطر شرایط حرفه‌ای سازی و موارد دیگر حق خود می‌دانیم که در فصلی که نیمه‌کاره مانده بتوانیم در رقابت‌های آسیایی فصل بعد حضور پیدا کنیم و برای موفقیت کشور ایران در آسیا بجنگیم که نفعش به همه می‌رسد.
🔺
ما در این زمینه از حق هواداران پرسپولیس کوتاه نخواهیم آمد و تا آخرین لحظه از حق خودمان دفاع خواهیم کرد. خیال هواداران هم راحت باشد که ما اجازه نمی‌دهیم تصمیمات خارج از زمین گرفته شود. همانطور که بارها اشاره کرده‌ایم، از نظر ما پرسپولیس می‌توانست در هشت بازی باقی‌مانده شرایط جدول را تغییر بدهد و به یکی از تیم‌های بالای جدول برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/132651" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/132649" target="_blank">📅 19:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uinC8hn7KwByG5bA_7WkIJLZ9AmUCg85bgfewpBbwggprL5DPXuFmNNhaI88MiiRRnpvhHZZXvYcBCvLXDm6cw7A_kEpXB_kpHSs4O5TrYkKIkYCO8FNVQgDCmJgNdDWCv8ucrET-6QOccnj4khcphM0rJWxMdsIxGfj5qTGggTAQhBEbfFVIUJskpnCAlfsiuuMoaS60d3SbFnKIE3HpKN2UFC62DNFWhBylUkslatWdLqsMWDmkqKSZYhd9rxqGyWptGpMmwCDpaEcPlX9SQ06i6dSrjzx_XzEePA2aurAC5yRTl5KHLkI7Ntwph4dkhNVqZ2UY0tbDntmFJB91A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
گل محمدی هنوز تصمیم قطعی خود را نگرفته و می خواهد پیشنهاد تیم دهوک  عراق و شرایط موجود را بررسی کند و بعد تصمیم بگیرد.اخباری از سفر او به عراق در پی پیشنهاد تیم دهوک منتشر شده است
/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132648" target="_blank">📅 18:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132647">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7awmuOmpZyKHAJk9v6oVpxZs_Ba-SJSbF2XZ1COI9-jbvCXe0CmQjAjujAChL5umeEsVr6TBdYdN7Ck6mzTGzi7nYb2OzfU4CQFNNVlzZH1us6QZPZcAYaxY2uTLmHCIG0BSe8IVPTUwNVnxoGF6cLpQk4A1pIwaV1EvtTjUjML9BOBktG4-NnoNW1-X3yRMdvAqoDmrLR6TqEo6PgxUMndv4NfJjy0zppF3MlWZ_dSjw7SNpUyeDoOF4tXRraQdGcGDpx1JAYZYw69JeBuvGn2sgG91q67ECaq-dgnZog90jaRhLS7X5PRUF24Vt7VpbDexQ8CFaD8OkR64kbYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
برگزاری مراسم تجلیل از مربیان بازیکن‌ساز آکادمی فوتبال پرسپولیس
⏺
باشگاه پرسپولیس برای نخستین بار، طی مراسمی از مربیان بازیکن‌ساز آکادمی فوتبال باشگاه تقدیر کرد. این مراسم با حضور مدیرعامل، معاون ورزشی و مدیر آکادمی برگزار شد و از مربیانی که در سال‌های اخیر نقش مؤثری در پرورش استعدادها و معرفی بازیکنان به تیم بزرگسالان و تیم‌های ملی داشته‌اند، تجلیل به عمل آمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/132647" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132646">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
روبیو:
🔻
ایالات‌متحده همچنان در حال گفتگو با ایران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/132646" target="_blank">📅 18:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132645">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
🚀
خبرگزاری فارس: مذاکرات با آمریکا به بن بست خورد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/132645" target="_blank">📅 18:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132644">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vky8rIHcWpS7V2K0XjTJHb68yiN_ohuGRQFM5r5p99a11wkeY3O2v8ek1pr34djnb_IL5rGI33iNpLnwS9miskSSo3RGvHwUwQoCcUbH8UmQcIbR0GI_KZxgUYLzakwtueAtjoGPdasqKGgvuva4EwAuBbRFqECgssu6XZGBLYflMT3Pr2UAWKcU7qfjZzhJSd0Fy1AqIDEQRg9UGYohaDRNEVp3WSBBIb9mrVdoDzz8RznM5ASPZjajjFG3oKbPayftw5tYHCBaDyi09i2VXyM-IKL7YLJ9luYSRxuh_hmpH2ze5vYxYYOL79OQdVhRjeiCP9lSP_SMMLvoGBmNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت مهدی روزخوش، مدیر رسانه‌ای باشگاه پرسپولیس در واکنش به صحبت های زارعی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/132644" target="_blank">📅 18:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132643">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
🚀
خبرگزاری فارس: مذاکرات با آمریکا به بن بست خورد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/132643" target="_blank">📅 18:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132642">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxvCENunENTakEqvKGW8k92JVZKxZWnnOJXjXfABb_DHz-1yuXPCt6XOrT77dXr1A3KxY8ZfNN1p1qXhXL7Y8x9o5QayXauHFvIvkBTH_hK0Iqbea2VIYmU4bwAIHcOgI8desFvCJy0D0xNuvcHniWxImqTNK7kLcshwT0TvAxf77WBaR_UIufsh5oBtqDbAJwPjTgAhKhk0SIuQASHinktddSmu44W6L9gzyv0wQeWrP0aMjWcMMbTMpANPp3JgiehWGDeBcjDTGdqtp3RGiROof38NwIPNsCKoxTB-GXK9yw1allWV6mSk8WdzWYwvz399y0glXqGKrWHielPztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با مثبت شدن دوپینگ یک کشتی‌گیر روس در مسابقات جهانی 2015، ایران به عنوان قهرمانی رسید و قرار است جام در رقابت‌های مغولستان به ایران تحویل داده شود اما مسئله اصلی اینجاست که ایران باید کاپ سومی که تحویل گرفته بود رو پس بده اما کاپ سوم گم شده و کسی نمیدونه کجاست
😐
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132642" target="_blank">📅 18:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132641">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
🔴
امید عالیشاه، بازیکن تیم پرسپولیس: در روزهای اخیر خبرهایی درباره سهمیه‌های آسیایی شنیده‌ام که واقعاً ناراحت‌کننده است. از همان زمانی که آتش‌بس اعلام شد، ما خواستار آغاز دوباره لیگ بودیم و حرف‌مان هم روشن است؛ نمایندگان آسیایی باید در زمین مشخص شوند، نه پشت میز. فوتبال باید برگزار شود تا تیم‌ها بتوانند حق‌شان را در زمین بگیرند، نه اینکه بیرون زمین برایشان تصمیم‌گیری شود.
🔺
واقعاً تعجب می‌کنم چرا در اردیبهشت که فرصت کافی وجود داشت، لیگ را برگزار نکردند؛ در حالی که بارها نامه زدند که مسابقات شروع می‌شود و ما هم بر اساس همین نامه‌ها تمرینات‌مان را آغاز کردیم. کشورهای منطقه هم درگیر جنگ بودند، اما لیگ‌شان را برگزار کردند. چرا ما این کار را نکردیم؟
🔺
تا جایی که می‌دانم مصطفی زارعی مسئول صدور مجوز حرفه‌ای باشگاه‌هاست و نیازی نیست درباره پرسپولیس یا نحوه انتخاب نمایندگان ایران در آسیا اظهارنظر کند. تصمیم‌گیری درباره سهمیه‌ها باید بر اساس رقابت واقعی در زمین باشد، نه حرف و تصمیم‌های بیرونی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132641" target="_blank">📅 17:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132640">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
اولین بمب تابستانی پرسپولیس؟
🔴
ادعای سایت هفت ورزشی؛ اگر اتفاق خاصی نیفتد آریا یوسفی را باید اولین بمب تابستانی باشگاه پرسپولیس برای فصل آینده لقب داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132640" target="_blank">📅 15:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132639">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552e7d620b.mp4?token=YXtp7MYLOW3fuGkzMfQLcZvE0_gXKemelCgF9fSrT5diOIqpFjw8VOYBHMRbKVgstywbzUtw46ky_CoKWJQ3hxSj7vhy9-X-BfhcnjncfJ1xdrr4A-7day5bVeTaJFHVvXXVFyAWuJA0D9Vf-bxJFXtpumrJbmTr9M2wQHdsCCZ2OhBDr6Aj5UUMNAniSItO4Cd5CDoq5_8_TURh1MjxbZtC_9Ekg_gkWNi4YXBLjen7GqHmxqU1UBlFvAzAA4R1Zhj2x4Ut8Ubr6NpH_WabN-4lydljLt54jpZTNpIGz0VFEkP531qgnHIfKiMs8ASeDvROmuIUo3cbzOPRxN0l0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552e7d620b.mp4?token=YXtp7MYLOW3fuGkzMfQLcZvE0_gXKemelCgF9fSrT5diOIqpFjw8VOYBHMRbKVgstywbzUtw46ky_CoKWJQ3hxSj7vhy9-X-BfhcnjncfJ1xdrr4A-7day5bVeTaJFHVvXXVFyAWuJA0D9Vf-bxJFXtpumrJbmTr9M2wQHdsCCZ2OhBDr6Aj5UUMNAniSItO4Cd5CDoq5_8_TURh1MjxbZtC_9Ekg_gkWNi4YXBLjen7GqHmxqU1UBlFvAzAA4R1Zhj2x4Ut8Ubr6NpH_WabN-4lydljLt54jpZTNpIGz0VFEkP531qgnHIfKiMs8ASeDvROmuIUo3cbzOPRxN0l0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
واکنش مجری تلویزیون به آسیایی نشدن پرسپولیس؛ آیا یزد و سیرجان هتل 5 ستاره دارد؟ باید میانگین امتیازی سه فصل اخیر حساب شود که پرسپولیس بالاتر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132639" target="_blank">📅 14:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132638">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
الهویی، مربی تیم ملی: امیرحسین محمودی  به دلیل مسائل غیر فوتبالی و شرایط غیر  عادی کشور از لیست تیم ملی خط خورد!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/132638" target="_blank">📅 13:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132637">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
مبارک اونایی که تن به ذلت "اینترنت پرو" ندادن. بنظرم کانفیگ فروشا باخت ندادن چون بازم برای اینستا و یوتیوبت بهشون نیاز داری و تا الانم حسابی فروختن.و اما تویی که فکر میکردی خونت رنگی تره برو با گیگی ۵۰ هزارتومنت حال کن نفس
👈
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132637" target="_blank">📅 13:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132635">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
باشگاه پرسپولیس از زارعی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132635" target="_blank">📅 13:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132634">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=XDmwCnJXgvKLflhIDkWwYK_RWvkPV3Ve-f79EueOIeXhZrTDv-0kEgDdkfiSCtZLMjaFjunwPzKwUK-1dzCz1vy2kndvKv-oeIJU_yD9mg85Z4xgSl0Qdkp3XAuu1MXI1PURUV5pc8YbaSsayBDimGV75Qm_q3cwj-bqPnCZafOuUWPY6HnE0keaswvgzD3klUF1NUif00Q5Pxn7uFMwv_n8Jx-tCEmc8mHEvoJH_qvFgMaQx8QN_IuGWRTWonTQEn5T_nek7uzSwU_dAJrm3AfvQp57AJQaooGNKigzWb1gV9mO7rHPKbj6NMvBiOyHJ0K57iycsxuZXe40k1oX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=XDmwCnJXgvKLflhIDkWwYK_RWvkPV3Ve-f79EueOIeXhZrTDv-0kEgDdkfiSCtZLMjaFjunwPzKwUK-1dzCz1vy2kndvKv-oeIJU_yD9mg85Z4xgSl0Qdkp3XAuu1MXI1PURUV5pc8YbaSsayBDimGV75Qm_q3cwj-bqPnCZafOuUWPY6HnE0keaswvgzD3klUF1NUif00Q5Pxn7uFMwv_n8Jx-tCEmc8mHEvoJH_qvFgMaQx8QN_IuGWRTWonTQEn5T_nek7uzSwU_dAJrm3AfvQp57AJQaooGNKigzWb1gV9mO7rHPKbj6NMvBiOyHJ0K57iycsxuZXe40k1oX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132634" target="_blank">📅 13:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132633">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
زارعی رئیس کمیته صدور مجوز حرفه ای :
🖍
پرسپولیس به هیچ عنوان نمی‌تواند آسیایی شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132633" target="_blank">📅 12:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132632">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132632" target="_blank">📅 12:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132631">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjWBuxm1tKsMO3AjjYAMahZ1Gz5AsqMRjKxApc53wUepy0C-tNaxnCeuP6E-KopxLtXKKEK9K_1GG3PLYg9aLWmoUi37eyX4EZCA8ZmWjUVe469OXljMlAtHULcdby5Zqq3AavlcTt2rhcpZHKcRKSd499P2DsOru21-dfEQrsfCSfqjiF3O7DHets-YCTe3sukCF-jIWOnkiiWHK19wz-drN6_zE6qlaOylYVnJa1d3QWEvySTkXxpR3fpN38LZsLotWkn8Jq1Yf7odGpwQNJ68Zy1_lgrU_wxf8vB1mPFUnSggJr3gwNlGosb-m04tnSM2ugsy63IK7QcAoa6hLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه شایعاتی منتشر شده که اوسمار
شاید برنگرده و جدا بشه که امیدوارم دروغ باشه وگرنه دوباره وارد دور باطل عوض کردن سرمربی می‌افتیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/132631" target="_blank">📅 12:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132630">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETBeRxX8ppSLgmlwJpkPvcXWydPCQ-DM-ICng663YBqnUyNoe1ecgRrIhDkxmhwRBnf4Y6lAPRbSiV1A_TAwV_4KEbxhnpkPP-rhm-Z4NQKi-LWpNf9rQ_zg0oULPSehT-tc80aKgwb6F4P3R7T86ASQyBbrtjN9InmSmDT4XD0MtOMCYhHN6nlyu5mK1mV0OxV82d3HmYZqKCMvTkpIyCAx9b6s4hn_BSoKS2w5GNb8d_BZ7ESAEx-2b79KK_nJ6KutO3yw7lWxv7bHme4Bg8MX56KYmSND89DMqYP8rVsSjGSutrvWqOR8VcJmP0D3OaIn61ArROfmeibs4qOeng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
مدرسه پیرمردها رو نوسازی کنید.
🔴
#فرهیختگان
: پرسپولیس با ۸ بازیکن بالای ۳۰ سال و میانکین سنی ۲۷/۶ پیرترین تیم لیگ برتر شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132630" target="_blank">📅 12:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132629">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
اوستون اورونوف و ایگور سرگیف در لیست نهایی ازبکستان برای جام‌جهانی قرار گرفتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/132629" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132627">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
سر تیتر روزنامه‌ گل   پ.ن پرسپولیس از خودت شاکی باش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132627" target="_blank">📅 10:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132626">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgVTYJK6qwTxd3znxvdKgo3mf5HkW1xwOvR2aKkYXwNyy9QuOgCsSZhzSI4K1kTDQYraP2b06kGQiNw20Bj3F4EvZkG0kU93XX2M2x2V_1nmZmO59Qtqeou46EqvDIrXQyAUzKbFjDsF2WSqGh7PsFJi1mb9nfGQkosM6pQW8pkQpWSa0FgVetdMtSreE6u3Vibb1ZGnGZJc4Nzcbal7uRMrI7FaLdbsHmtcKVh8kZ1_7oMi8M1ic5AUiMzxv2DJUM_CVa7R9Kd1kuMZtOZg5f1r4HIQJrcCOajoO7XEqI71BeW1QyoK1ePjbYDtOmjslugbG3TwUH1kyE8As3_AwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سر تیتر روزنامه‌ گل
پ.ن پرسپولیس از خودت شاکی باش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132626" target="_blank">📅 10:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132625">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
تسنیم: مطابق جدول فعلی گل‌گهر، چادرملو و پرسپولیس در رده‌های چهارم تا ششم قرار دارند، تورنمنتی برگزار خواهد شد تا تکلیف سهمیه سوم و جایگزین سپاهان روشن بشود
🔴
مشابه این اتفاق در پایین جدول نیز اتفاق می‌افتد و قرار است تورنمنت چند جانبه‌ای برگزار شود تا دو…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132625" target="_blank">📅 10:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132624">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132624" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132623">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=p3bKJi27YYq8kT_elNX_NWKkjlakOujjpzdRgaXqDAIAKzhd2re9uR6H6cd29egnwFdbPUUIU-IAs8VOi4jS_peeCCwiI0cuDwZQoNRkG1VWmNtfwgpDFqNb6TK63h2O4AfZK46qUQu7Q5sQWsXJFtLvhqxqVYV7Jrh2ZDoPmpC17nZ-TTNqCz4EQAUUbTuuCiD1NHxb6rtQBh7C9aN90ScLGN9cc1UfIB9RBZZcmxFo74aRTOdXLJ9WENs2RJDsfKuelx_OOAK4cOf6WKN7jEzH_DJ13OgZL2e3RW53UF2l1-Dlm5dhjUPC1TseNF-JJHx_2LOzfdiJmMeiI1Faig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=p3bKJi27YYq8kT_elNX_NWKkjlakOujjpzdRgaXqDAIAKzhd2re9uR6H6cd29egnwFdbPUUIU-IAs8VOi4jS_peeCCwiI0cuDwZQoNRkG1VWmNtfwgpDFqNb6TK63h2O4AfZK46qUQu7Q5sQWsXJFtLvhqxqVYV7Jrh2ZDoPmpC17nZ-TTNqCz4EQAUUbTuuCiD1NHxb6rtQBh7C9aN90ScLGN9cc1UfIB9RBZZcmxFo74aRTOdXLJ9WENs2RJDsfKuelx_OOAK4cOf6WKN7jEzH_DJ13OgZL2e3RW53UF2l1-Dlm5dhjUPC1TseNF-JJHx_2LOzfdiJmMeiI1Faig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132623" target="_blank">📅 01:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132622">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت
بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132622" target="_blank">📅 00:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132621">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
برنامه های تیم ملی تا شروع جام جهانی از زبان تاج
🔴
بخش دوم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132621" target="_blank">📅 00:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132620">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
فدراسیون فوتبال: در صورت تمایل امیرحسین محمودی رو جهت حفظ روحیه بر خودمون میبریم مکزیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132620" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132619">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28a044344.mp4?token=VlaVVRNMDDhmlzhaX_7RElVuQniDBmv_RhHN_WClGR5-mRPFdesLyixJvtienHlKe-EvSo-PYZkbuK3jpnqS0n-PuBBAM7lNGh3-us-zJHBFxcIUjsAd4Kf6fuNVHyhxTlKhh9EZjaKlOrKhCSh2L39xOFna356dRRxmXSFIneLmn69CM11BP5DLTjHaXWqQwCtw0EWUB77_C2R6waZ2FOqTEK9PaP2d2ACmk1nlqKkzWDbtVFuWXMl-JOM6gGJaTEGpbf1cHixvACJ_Cd8l027wnioSPJbc4j-7u0WuX0oFpvh0vtLqfAseh2z70LGgw-vYHbDvEbI5REKw0fecrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28a044344.mp4?token=VlaVVRNMDDhmlzhaX_7RElVuQniDBmv_RhHN_WClGR5-mRPFdesLyixJvtienHlKe-EvSo-PYZkbuK3jpnqS0n-PuBBAM7lNGh3-us-zJHBFxcIUjsAd4Kf6fuNVHyhxTlKhh9EZjaKlOrKhCSh2L39xOFna356dRRxmXSFIneLmn69CM11BP5DLTjHaXWqQwCtw0EWUB77_C2R6waZ2FOqTEK9PaP2d2ACmk1nlqKkzWDbtVFuWXMl-JOM6gGJaTEGpbf1cHixvACJ_Cd8l027wnioSPJbc4j-7u0WuX0oFpvh0vtLqfAseh2z70LGgw-vYHbDvEbI5REKw0fecrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132619" target="_blank">📅 00:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132618">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2531fbac09.mp4?token=aU1QAgV0VNAhC584YU17gD9Az3E69z9I-QcL223sivuumSMgTV_h5d9IGQtzxoYHoD0tJYzA03oxnD0t-T-wJP6PwzBUUt6ADhLMb0Ar3zC9e32_AlUmiWjbRJSlTySRyl_9BXtMth1ZtxqthLLBS1BTIV2Ot2Tqz-HiChXP0Pi4tMhmVZ_G9ExV_3Y0VEDt5Lon7pTfbs1ykj8rV0FfqUUo_8S5kQ7DawQmIdxl0U1oj3NQJ7WG5gvndnU3VX1nsKKjX6YcOIfXKp2Yvan6QJOBxLLjgIgCRP6rfpRhpZgsqSIel_vPYK9ge8HhCUHQtKvbu97VaFsJOAdfJL65Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2531fbac09.mp4?token=aU1QAgV0VNAhC584YU17gD9Az3E69z9I-QcL223sivuumSMgTV_h5d9IGQtzxoYHoD0tJYzA03oxnD0t-T-wJP6PwzBUUt6ADhLMb0Ar3zC9e32_AlUmiWjbRJSlTySRyl_9BXtMth1ZtxqthLLBS1BTIV2Ot2Tqz-HiChXP0Pi4tMhmVZ_G9ExV_3Y0VEDt5Lon7pTfbs1ykj8rV0FfqUUo_8S5kQ7DawQmIdxl0U1oj3NQJ7WG5gvndnU3VX1nsKKjX6YcOIfXKp2Yvan6QJOBxLLjgIgCRP6rfpRhpZgsqSIel_vPYK9ge8HhCUHQtKvbu97VaFsJOAdfJL65Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
با اعلام تاج امیرحسین محمودی و مابقی خط خورده ها راهی جام جهانی میشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132618" target="_blank">📅 00:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132616">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988a98ef48.mp4?token=TFdZioV9p-WWmQc-2emXjApIxMPQhlPoaLiyJeqoWgt9sT-MFD31uFQ4Ysz47WFzOGQ-jtlWwVH9MyiX1cLowshVdW-UwaRm94--XXC0Zjp-pE3-5G108_DRfLAwJTKeJBu4r3sp5w062el3WMyJakmiex0yPKiNcYmyaE0TsgnVpLPxQDAFI6dWCYpecKobAr0q0ZUZupDoAeDwEFu5I-QF1rRyQWHyIL_rfqEOQivx0-5ZQaNl5Oc2ASzBQQtVjVLXftx1sUy1JEatyARXyel2o8M0zdr_Q26BBnrwqDtyn3MuAIXzx6W1QAdXktXZ_POIif05FBdbT-GdhkijAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988a98ef48.mp4?token=TFdZioV9p-WWmQc-2emXjApIxMPQhlPoaLiyJeqoWgt9sT-MFD31uFQ4Ysz47WFzOGQ-jtlWwVH9MyiX1cLowshVdW-UwaRm94--XXC0Zjp-pE3-5G108_DRfLAwJTKeJBu4r3sp5w062el3WMyJakmiex0yPKiNcYmyaE0TsgnVpLPxQDAFI6dWCYpecKobAr0q0ZUZupDoAeDwEFu5I-QF1rRyQWHyIL_rfqEOQivx0-5ZQaNl5Oc2ASzBQQtVjVLXftx1sUy1JEatyARXyel2o8M0zdr_Q26BBnrwqDtyn3MuAIXzx6W1QAdXktXZ_POIif05FBdbT-GdhkijAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تاج: ۱۰۰ هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132616" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132615">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132615" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132614">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🟥
بانک شهر طی اطلاعیه‌ای از تاسیس نئوبانک جدیدش به نام (رد بانک) خبر داد که تمامی منافع این بانک متعلق به پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132614" target="_blank">📅 00:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132613">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e411950a.mp4?token=sKX8vfu3OieSGrfn52WFUPcHDZtxNNrdM7c8kmjWrwDObg36UWpE_xAy4hEjD8D8VFvmdx_enpdtu9qD1HTOTtNMMRQY_xdVO1CQ-5ZIsH71tO8nNKfPvnKPiDqUnR4z_PpMXaiR3oc9HwRUPpDg1DqVXqyUea1miQaC5eLZFkqh-wi0RS55TeG99kvC3c0-uzsI41qWRTC-NgTHqgWno2y2qZmpAcZ9qAvyx2qGGBJ7SCKupGokppYA7beXDbSHvhgraEpleRPykil_h_CGRpbeO7tO-i6zaR1imc3VsMSCrLj8CdJUgGq--2Ry57dGYWN7c5SGFFH-v8Tks6e98Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e411950a.mp4?token=sKX8vfu3OieSGrfn52WFUPcHDZtxNNrdM7c8kmjWrwDObg36UWpE_xAy4hEjD8D8VFvmdx_enpdtu9qD1HTOTtNMMRQY_xdVO1CQ-5ZIsH71tO8nNKfPvnKPiDqUnR4z_PpMXaiR3oc9HwRUPpDg1DqVXqyUea1miQaC5eLZFkqh-wi0RS55TeG99kvC3c0-uzsI41qWRTC-NgTHqgWno2y2qZmpAcZ9qAvyx2qGGBJ7SCKupGokppYA7beXDbSHvhgraEpleRPykil_h_CGRpbeO7tO-i6zaR1imc3VsMSCrLj8CdJUgGq--2Ry57dGYWN7c5SGFFH-v8Tks6e98Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مسن‌ترین تیم‌های حاضر در جام‌جهانی؛ ایران در رتبه سوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132613" target="_blank">📅 23:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132612">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
حدادی مدیرعامل باشگاه پرسپولیس: سروش رفیعی همچنان بازیکن تیم پرسپولیس است و با شروع تمرینات باید در تمرین حضور داشته باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132612" target="_blank">📅 23:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132611">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:   «مذاکرات با جمهوری اسلامی ایران با سرعت زیادی داره ادامه پیدا می‌کنه. از توجه شما به این موضوع ممنونم! — دونالد جی. ترامپ»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/132611" target="_blank">📅 23:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132610">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVFmI9JvofsawSyM4o-GOXsDxE6Zu1qUJa5OGqXp7c74y3jV_0ladejcPhRpF6R2YX4k3ImyFP592mMyrOZykTITzVl6gJZfmtue4OPCxWGnKV7ZhfHgOnDeXNr7wp-Erqt3HoTDU_hFf4Gd7fiBeuSXmG5crfRQEo0plA2gDQ1irjrqbTlmZ6Gdey969DA-gEN2tSGvvDwN3rN-10TT5Zug8wEhvXDEZPz_I_YzEMt8FMtN6aUE6harpm8Jo-m49LN7ffYuR5EDj0vku_pf26t7e8yiD3S6gO3MjATuEk9a0y9zXjPQrhbQji3AP_neQAqxJzZ9-bRICxbfT6oyMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
بانک شهر طی اطلاعیه‌ای از تاسیس نئوبانک جدیدش به نام (رد بانک) خبر داد که تمامی منافع این بانک متعلق به پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/132610" target="_blank">📅 22:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132609">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cignCqFrAFrOl1xfVK4HB8p7BfDTcnIJR2yOJl2TR-cAg--xv-SCj-xNPvYSkjMPLkzsfY0wCSV5UkVDaiL4DNq9TSYCmcLou8e-ZkTla2J7kBA29yHq2PLB3zFDFKZ1PFkYHkjODMz8ohaiM2uyNqvyH_PnyLwThRK3-oT37P9O2GhjD1K8iob2i1K0RQxjiHvj_XIgF5gy6B3eOci9JprV1H6fqidkIXu3YQ_R_0wYUrPmXc_J9bYWGNif7gjI_0_Smt-MzcTeTHXBYQpblrvFF4d3p1acR-XZOWL4lsoGh95O1ct7x-hdH92RBV-Oy0rJPT_I6hWSbDjFhCzHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«مذاکرات با جمهوری اسلامی ایران با سرعت زیادی داره ادامه پیدا می‌کنه. از توجه شما به این موضوع ممنونم!
— دونالد جی. ترامپ»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/132609" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132608">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🟡
سپاهان حذف شد
▫️
گل‌گهر یک بازی اضافه داره
🔸
چادرملو از بازیکن غیرمجاز استفاده کرده
🔴
پرسپولیس برای ۳ امتیاز بازی با ملوان شکایت کرده
⁉️
باید دیگه چه تصمیمی گرفته میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/132608" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
هوشنگ نصیرزاده، وکیل بیرانوند در دادگاه CAS: چه قبل و چه بعد از جام جهانی هیچ چیزی بیرانوند را تهدید نمی‌کند. اغوایی توسط تراکتور انجام نشده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/132606" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💢
ترامپ: من یک تماس بسیار سازنده با نخست‌وزیر بی‌بی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردن…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132605" target="_blank">📅 21:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bMxhxdn-XojuU5dsuueI94sQ2KVu9p12ihXan6LUWkug1UVAiLxNqCbBYSm7ILNB1CA-PmOFbRrhipJkUiq2KOYK1_fYJJEtHXaoBZEHcnR_G1TJEZcBpDYyI3EpBJw0OYxy8swx0LnwPg_c_VsQO0xEnQrPvZLTgjIWhxXrtjcC1ba6gx2bno716jH6wlacM4IHHDU0QYOgVONm7h6HaNV46MnBP9cd9GIh046s4jvRLcISGvI2uYCZKBNDeLy1jjOEQLgEOMDLt-QC3eZj7IFL-_CRPItHp5LoWnvRey3D7Pn4oWTZV6L-h21wqzRg7jNoJBBpO_VJKlrkDhzkHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
ترامپ: من یک تماس بسیار سازنده با نخست‌وزیر بی‌بی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردن که تمام تیراندازی‌ها متوقف بشه؛ اسرائیل به آنها حمله نخواهد کرد و آنها هم به اسرائیل حمله نخواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132604" target="_blank">📅 21:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
ایسنا: احتمال برکناری محسن خلیلی از پرسپولیس وجود دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132603" target="_blank">📅 21:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132602" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
لیست خرید اوسمار به نقل از فوتبالی:
🔴
اوسمار برای هر پست ۳ تا گزینه معرفی کرده و حتی اولویت‌بندی هم کرده
✅
دفاع راست
✅
دفاع میانی
✅
هافبک
✅
دفاع چپ
✅
مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ‌</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132601" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
از جدول ناتمام تا شهرهایی که آماده میزبانی در آسیا نیستند
‼️
چرا میزبانی این دوره از تیم‌ها در قاره کهن امسال برای فوتبال ایران مهم است؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132600" target="_blank">📅 20:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKICgcCPOcsowj12xQqqO3wADZf7xj5RDYbDTOhQRc--FRisjp5ZIz3xSLOabUA8-EBypVO2DEW9mA6c9rMiZX7EprhKi1nx5uXhn8glwYPn_5x0vTgEQiEhESIagZ3vmV9TnVgi6tFmUuitPSQrINhUgG4u3991WoQ_tESor9kJaBC5Y7YL5SjF8UrVOLjuMGHS83YQCuoCvu6BZo7bGsZyAXI54AnGdDvy8bpFflsmcFuusLx1JjwA3WI1P2SPd6ygSIlNCeV0YyqaJtXgUgbz8W0qjuWJa9l-wJ2FgBmsrfI9sMVnGeDNYHc6Gce3mXqHeuAVEgHCtcR-R3c0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132599" target="_blank">📅 20:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
محسن خلیلی: باشگاه پرسپولیس حق دارد از حق و حقوق خود به هر طریقی دفاع کند
◻️
متأسفانه در روزهای اخیر شاهد آن هستیم که برخی افراد از طریق مصاحبه‌های رسانه‌ای و به صورت غیررسمی درباره نمایندگان ایران در مسابقات آسیایی اظهارنظر می‌کنند. این درحالی است که طبق…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/132598" target="_blank">📅 20:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132596">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚩
ترامپ: فقط ۲ چیز از ایران میخوام، تنگه رو باز کنن و بمب اتم نسازن، بعد ما میریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132596" target="_blank">📅 20:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132595">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufj_CZ2NhXKu2KHKikgUyGSQHmkIurCZrtkuU1wy1iuizlIS1XdmvtZWlO1zOUy4W2K_InjMjjaF_GpBUtCRwjc293wd-UlHK4lH6xlZXh6I0LnLawgVMZhFyDz6ZL17vrDLlf7kfGaBd6aKLh5XR6R-fVAKhiB_nYefckyFxos5bgRYR0jA-pnHHgyxnebxpwdZgH6L3bjeZXoRntGLobPE_uBcwwBHnO15zDBt0lmU8WpHLOM8rXUqGSWbVRacQrwqLV0G_XnuviALOrKg3RJgvyhOcol9P1mU7RvE071jQqRglYGCa5k0LWzzPBhmGUpQkWqmwtXuoTqHSRmf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
آندرس اینیستا با قراردادی 2 ساله سرمربی گلف یونایتد امارات شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132595" target="_blank">📅 19:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132594">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a1bce686.mp4?token=azWmixJ4a5vEIJ2qgkNRyq4KmQAr65zY08Zx6WlBE8P1b5qxLxgLmQMZqH_kologZb9UUrbRuJ2hP_D21m-Oh38I4YLSIEMkRfEwh7evozY05WCmch5pH5RzDkV0czGEjbUKaFeQn_SP19QpkUQEvMsc1X7FOlrm_E3RC1LpZKJDt5kHPk7HqfUUBgd46dRGR0P3Ue_mNCcRDWagOUaDjaHObK8QYf3cusHAsHfD9nkirBvGtTPpG5SdYE-ofqHkvpBuTM0y0QisOrUZWsK5nPJvTktCq42cwKihEiLgxxR7o4Wg7yrWoWEw8ZSvjPkcE1K5g9HU6kIa-X-eFQGjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a1bce686.mp4?token=azWmixJ4a5vEIJ2qgkNRyq4KmQAr65zY08Zx6WlBE8P1b5qxLxgLmQMZqH_kologZb9UUrbRuJ2hP_D21m-Oh38I4YLSIEMkRfEwh7evozY05WCmch5pH5RzDkV0czGEjbUKaFeQn_SP19QpkUQEvMsc1X7FOlrm_E3RC1LpZKJDt5kHPk7HqfUUBgd46dRGR0P3Ue_mNCcRDWagOUaDjaHObK8QYf3cusHAsHfD9nkirBvGtTPpG5SdYE-ofqHkvpBuTM0y0QisOrUZWsK5nPJvTktCq42cwKihEiLgxxR7o4Wg7yrWoWEw8ZSvjPkcE1K5g9HU6kIa-X-eFQGjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دو سال پیش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132594" target="_blank">📅 18:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132593" target="_blank">📅 18:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132592">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
مهدی لیموچی با ارسال درخواست رسمی به باشگاه سپاهان، خواهان فسخ قراردادش با این تیم شد.///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132592" target="_blank">📅 18:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132591">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132591" target="_blank">📅 16:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132590">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132590" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132588" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132587">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132587" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132586">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132586" target="_blank">📅 15:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132585">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiplZEngla9DpfkQGqdtMzLFk4rFtS2XBigvtCUVml-fyjEfWpwurnU8D84_Bf5HPKnp_Z26EGQrwtjUa4gk5w0NaY6v9Qhiny6IumjsHp9kh1M1xal2jfE1qIQ9Z98K_5ZOQdgbN8wnbn5RMG-sVqRzHH96BNKv-w_Hw8Rn8Wk1ZU44K1Gqo_XdPtSNRUDslTzRGRIJgxo_4WrDMDr88Pi3uL8wnUAmxtQGWPwR6azFEaPerhGbMWMxY-zA_sFxBLua_sRprQUvAHRLWusA5HDDuJdAWfIlXrvVnTE0RxesR4Qh8XMMaL6ijZs6jT1snSYEYRFhoVb8CUYGT3qeig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132585" target="_blank">📅 15:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132584">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmYYrnpVBrPfDaxG6NXCVna6uZUit8NQ7Y0VRCMS4x7Ok7DORv7Rq-1bZfa6t-VputTBPfOg0Kt8vA-cb4QuM4UAp0_2nkMvi8qf1gYY5CPVreCWGIiBY7zHPAVrO0dsZYuBG1GJxiNi2zq-dons7AQ7kuBbw0nfsDg8OXZ2AIP-7BbJuxTaTIubTfsDjwSJBjKZnzaVkhcQIyQzajAQ3MjhvE5-4tYs8Ogy3x1ZtwRGL7z3VLaLFHUgHKyLg_HqdjRcKd66BulBqbzWdIu4ovHZB16xT5-i9lNLBQxeamWF8WbRCb_D_JPJ_19pCnQt9HXC22yesrL9_HpWV4MjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مراسم معارفه مصطفی میر ابوالحسنی به عنوان مدیر جدید حراست باشگاه پرسپولیس با حضور پیمان حدادی، برگزار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132584" target="_blank">📅 14:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132583">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky4Hgysm_DGa8epWNeg1LNGNThaxg24itvKNw-vh3eXUtPEXNbXr6_SnrFQpe8QuWnkvcX6BFOVZxV75v9q7EHWbcou9BBTxI3tEkSf8inrMJx-My0yUbNHsGMrDpbS_YBOfSWzPUgt9Lrrlh67aGAQ8pBVY7_Lc21lXL8hOSfru3Dl3jbEs7Q8ln5d6NmnUdh6gwMrngTN3qig5WGQa42gaUTCZZPH0tx6_9jdwe9AemdLOziutnrcYNkymB9DVJ0-UyCrcTpPGCQdQ3Pq6pnkiBXVHYNy_POKa_Efqq_aBuytIFfTMxBW8FLVyue8d6_HV-hKgzAwyq7tfxD0O2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132583" target="_blank">📅 14:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132582">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
لیست مازاد فعلی پرسپولیس به ادعای تسنیم:
🚨
سروش، پورعلی‌گنجی، سرلک، بیفوما و گرا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132582" target="_blank">📅 14:05 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

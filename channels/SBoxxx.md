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
<img src="https://cdn4.telesco.pe/file/gxVW7ZEPggv6eT10KhCJrOlfpaCAZ0GwGJFG664uS2nKVNPZJCWFpfpWdeEof3yGXbZ86A_UOkQLFjTNalUtfiNV_3nyM-CRSfkd9OveP6n7lEIJu6yTgKSnYY8SkPB0QOpPmuPVpo9lD6Z5hFTiCa-fQETVyApz2sr7lpS_Lg5VT2-08hrozC-KGRU6zqk7N8D13Jre8cl79YYrYu1wEZSFAToGt9vOPohixRI8OhncAAd4wxKjXWfIuYl7NVGWNEyNkp5y8MNG7fCxF2SLw-V6wHjuRglTTte0c5AUGEqBf1_dLL04n-4g0MuUAlteUigJNCor9dwc2Wgd9YM7GQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 20:55:21</div>
<hr>

<div class="tg-post" id="msg-19944">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مدتی نخواهم بود...</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/19944" target="_blank">📅 16:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19943">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLIYLgvLK_nGyXzdNOdgFZmO8Z9No9sBc72wTClqvlVq-8CnyjY26TyqttLGJReKQIGdRmKJr9O6AMAoyHv36s3tnAUn6B1Y8HgOqjHgrK1gqUhr2JIoeTNb3hjnSnmuHwS-RSZXK2l-2vP_rNcQNR1TbKAXBxi-Y105LCgOtnYUuMfagFcdNIyxw3kvFZJ--IDspvkZttJ6AsGWdNrcz-hirTVS5AjtjUO1WBYtJEX4IZvSDLt7bmnx3TBnHxqc_5FhHNCvaSEAOpxyq0XxdREP8SHeuD87qvaxWNOOUuVOZ_mTmoIcfmZz4Yfin5mYuEHIPOgqe14WsoloWuGCyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه به دنبال تایید ایالات متحده برای ارسال ذخیره‌ای بزرگ از سلاح‌های ساخت آمریکا به اوکراین است!
این بسته شامل موشک های اتکمز و ۴۷,۰۰۰ گلوله توپ خوشه ای است که به گفته منابع، ارزشی حدود ۲۵۶ میلیون دلار دارند.
واشنگتن آماده تایید این انتقال است، اما سازمان دیده‌بان حقوق بشر از کنگره می‌خواهد که جلوی آن را بگیرد و به خطراتی که سلاح‌های حاوی بمب‌های خوشه‌ای برای غیرنظامیان ایجاد می‌کنند، اشاره کرده است.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/19943" target="_blank">📅 14:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19942">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">چقدر خوشحالم جای پاکستانی ها نیستم؛
فردای امضای پیمان دفاعی با عربستان، یمنی ها یک کشتی سعودی را زدند که در اثر آن چند پاکستانی کشته شدند!
الان هم سه روز است میگویند ایران و آمریکا دارند سازش می‌کنند اما ولی خب</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/19942" target="_blank">📅 14:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19941">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:   فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند.   ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/19941" target="_blank">📅 14:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19940">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آذربایجان در پی دریافت کمک‌های ایالات متحده در زمینه فناوری‌های پیشرفته برای پاکسازی مین‌های زمینی است.
دهه‌ها درگیری این کشور را به شدت با مین‌ها و مهمات منفجر نشده آلوده کرده است.
باکو امیدوار است که روابط نزدیک‌تر با ایالات متحده بتواند تلاش‌های نقشه‌برداری و خنثی‌سازی مین‌ها را تسریع کرده و بازسازی پس از جنگ را پشتیبانی کند.
منبع: آکسیوس</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/19940" target="_blank">📅 14:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19939">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند.
ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/19939" target="_blank">📅 13:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19938">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اردوغان:  «توافق مکه» علیه هیچ کشوری نیست و تمام دولت‌ها می‌توانند به آن بپیوندند  نباید این توافق را به بعد نظامی محدود کرد، زیرا هدف اصلی آن تقویت بعد بازدارندگی و امنیتی است</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19938" target="_blank">📅 10:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19937">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حالا باید ببینیم ائتلاف «مکه» پاسخ می‌دهد یا صرفا برای دوشیدن گاو شیرده حجاز و نجد تشکیل شده.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/19937" target="_blank">📅 10:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19936">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حجم تحقیری که ترامپ به عنوان رییس جمهور آمریکا دارد می شود کم نظیر است!  پس از افشای داستان فرار ترامپ از ترکیه با یک هواپیمای فرعی — آن هم داخل کامیون کترینگ هواپیما ! — دیروز خبری منتشر شده که ترامپ حتی داخل زمین گلف خودش احساس امنیت ندارد و همانطور که در…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19936" target="_blank">📅 08:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19935">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">— کریس رایت، وزیر انرژی ایالات متحده:  به لطف تلاش‌های هماهنگ ارتش ایالات متحده و متحدان ما در خلیج، میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.  وقتی این مقدار با ۵ تا ۷ میلیون بشکه اضافی در روز که از طریق…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/19935" target="_blank">📅 07:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19934">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-z3_ct29lK9g4CPxsLr8kWyd26oPzDBLEuLLF1V4MXtWIpYqENimkBCKZ4VjvU3C1Vr5aP_6uHtvmJrLRR6HOZR-DpWbhH-OxGO2pCJMAmIqmoXsVuFObDzxhm52_x0HmKZX7X_Yam2AaWY43RR-cqo1ibkTYBFi2SyORaL2dRrpN6Q1Dxnvz98Lp6ZPpxXoDos3oElCwMNLAQ53zFggxt2Dl9DG2H8XHCkVp3u1xPiUfvi_g6J95f2zxVC768f2LKnx1mApKK7uTDxfZXAuJAm7Qy1U5Q_tNjmngVzCKguP_UMvjyEwoFDFV2oWd-O4fY2MqzyKH0-O1S7C5oI7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— کریس رایت، وزیر انرژی ایالات متحده:
به لطف تلاش‌های هماهنگ ارتش ایالات متحده و متحدان ما در خلیج، میانگین هفت‌روزه نفت خروجی از تنگه هرمز در حال حاضر به نزدیک ۹ میلیون بشکه در روز رسیده است.
وقتی این مقدار با ۵ تا ۷ میلیون بشکه اضافی در روز که از طریق خطوط لوله و تأسیسات صادراتی تازه ارتقا یافته از منطقه خارج می‌شود، ترکیب شود، مجموع جریان‌های نفتی در حال حاضر به طور میانگین حدود ۱۵ میلیون بشکه در روز است.
فقط در روز یکشنبه، بیش از ۲۰ میلیون بشکه از منطقه خلیج عربی خارج شد که این رقم بالاتر از میانگین پیش از درگیری است.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/19934" target="_blank">📅 07:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19933">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کوشش ژاپن در تقویت توان دفاعی  ژاپن با تأکید وزیر دفاع خود، شینجیرو کویزومی، بر لزوم تقویت و تحول توان نظامی این کشور با «حسی بی‌سابقه از فوریت و بحران» اصرار می‌ورزد. گزارش سالانه سفید دفاعی ژاپن، منتشرشده در ۴ اوت ۲۰۲۶، بار دیگر بر تهدیدات فزاینده چین، کره…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19933" target="_blank">📅 06:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19932">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صدای انفجار در شمال غرب تهران</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19932" target="_blank">📅 02:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19931">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">صدای انفجار در شمال غرب تهران</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19931" target="_blank">📅 02:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19930">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">▶️
An oil spill has reportedly polluted a coastline on Iran's Qeshm Island.  @PressTV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19930" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19929">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPress TV</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de69aae9a6.mp4?token=vjp7-VXPnOsFQZguG136D8Kz602rPbhIX-8HI2qFCYMWOb3zEGhqC93zzWykfp7u_mX6R3p8spBarJiLcHAejfbYmArmlMW-BQh3N-FGrTV2rKqQawJeAOrYv4IkdNgtvnzxb-ljbdoBIq_7blZ95itFLrGEpDIxITBNw1sBIGfqkk7CQc7gYiQuzPUv9w5NI27EquDfNiRHOvQN3frY54XDEDZfJ9px8fOmiasYLHTN2KCaCJYhdW4NkswT-SG8Z9giaH0kgL28d5jyuQwhIpmL-KUEV7IUyelMCgsV4YqS2yWAt0VmA2i9qmf6ozAcyWsz4K0GuI1e-NAdO2Mtog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de69aae9a6.mp4?token=vjp7-VXPnOsFQZguG136D8Kz602rPbhIX-8HI2qFCYMWOb3zEGhqC93zzWykfp7u_mX6R3p8spBarJiLcHAejfbYmArmlMW-BQh3N-FGrTV2rKqQawJeAOrYv4IkdNgtvnzxb-ljbdoBIq_7blZ95itFLrGEpDIxITBNw1sBIGfqkk7CQc7gYiQuzPUv9w5NI27EquDfNiRHOvQN3frY54XDEDZfJ9px8fOmiasYLHTN2KCaCJYhdW4NkswT-SG8Z9giaH0kgL28d5jyuQwhIpmL-KUEV7IUyelMCgsV4YqS2yWAt0VmA2i9qmf6ozAcyWsz4K0GuI1e-NAdO2Mtog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
An oil spill has reportedly polluted a coastline on Iran's Qeshm Island.
@PressTV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19929" target="_blank">📅 02:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19928">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKSMtqvjhY6C8-Fqr8hNjOvmysQIJOqo-SiDTUGKQ4GeoW_rYupRsFXY9urTkqZajc4LKawXpus42sKPJ3DrExskbGEraHeXgVtOnDIStqAXY3enI94j1heJeKzrjuEZblZPEP6wl22LbcOiYlzOu7E4RoaVwll9O70uVnUMZRcCuaffXn6PmXD2xBzSo0jwRY3fyPdkH_fgAK_rF22jkcIj4biDEKa7f3KypacKqvlSkWuUy-WfDPRpbZXkYjNt0vKxhLSzDjGm2wQcvD72UEZ7vR6aWE2sZzD84vb33XadLRZHRXxZKCaqM5Wr8jUx8FTxen_rNx8jhoVOxqbY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19928" target="_blank">📅 02:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19927">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19927" target="_blank">📅 23:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19926">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این ترکیب و چینش سیاسی و نظامی خبر از جنگی شدید می دهد.  تًن ماهی یادتان نرود.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19926" target="_blank">📅 23:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19925">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اساساً به حمایت خاصی نرسید که برای خرید اقدام بشود.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19925" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19924">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrDXnUqwIrBVL3nzfO5vopNcMs7hSmLwgr41tk7dj2G1ZZmNg6Dbm1HR9KAveXd4ioNMYu3IgFGrdiAMFQ9aog-cmxcGaWBXAXTnk65nx9b5WdUdYAVLiRF3dSlEelcCFufgxSK1ng9KktkfYWFEGzTyZZef-4JN46C_4Ky0XKAA07IJjF7sWoHs4Qvm5YVXVADFpfGapPY_gU_INyY_8wRPrVmHowA7LMgvzuENClFg5LvO67BBgabOLZAagup1FteYwqYVw58gGMzyCii6CKUPMYDEEo82K7oTQBV4-oZD3s4OHP9vtBqZMaLcjTSGduVhrynEFzEC7zjE3iceCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه ای قرار دارد. در چنین شرایطی سیگنال قوی خرید یا فروش صادر نمی شود و بهترین راهبرد از دید من خرید در سطوح حمایتی پایین تر است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19924" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19923">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بازآرایی ساختار نظامی و امنیتی ایران؛ حرکت به سوی فرماندهی متمرکزتر و مقاوم‌تر   ایران پس از تجربه جنگ‌های ژوئن ۲۰۲۵ و بهار ۲۰۲۶ در حال بازطراحی بخش‌هایی از ساختار نظامی و امنیتی خود است؛ بازآرایی‌ای که به نظر می‌رسد مستقیماً از آسیب‌پذیری‌های آشکارشده در…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19923" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19922">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گریدم به اسلام آباد و توافق ش. نفت را دریابید.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19922" target="_blank">📅 20:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19921">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران:  پیام ایران روشن است: تنگه هرمز تا زمانی که آمریکا جنگ و محاصره را پایان ندهد، دارایی‌های مسدود شده ایران را آزاد نکند و به آتش‌بس در کل منطقه، از جمله لبنان و غزه، موافقت نکند، باز نخواهد شد.  تا زمانی که تمام…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19921" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19920">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">محسن رضایی:   تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19920" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19919">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این خواهرمیانه درست بشو نیست؛ ببینید کی گفتم.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19919" target="_blank">📅 20:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19918">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3df015c88.mp4?token=Dl4fi-Urq7WCEolwcXrqKTEjItrMV9dKm-m718yVZnVlos8KIH89cyEpm1kJBvhYxUernhzsTeydY9dvDwRJ0XEY76dWSoGnQuFsg7SON7Rwp-Z_fleFhoxrbXrTaRQbCPLgyxu--i1W9aHAztRYHSqY9SOVDZ3Rgs7wu_lX8CJROWLM_q3DAxD5Cod3ODRt8C1YDRjqoxfi86hYLbfZXB30J6hvsyKTBC8UVQO6ug8-OcriRzajjun2UBt3QBBPIzBK0hudAuA0BdSFS9l0D35iGHXCBcbUt5PD1dp4FGuIhE0Ajr_zziGIDtyrbpuoX1edXWVqWL1OLq2uGVBlbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3df015c88.mp4?token=Dl4fi-Urq7WCEolwcXrqKTEjItrMV9dKm-m718yVZnVlos8KIH89cyEpm1kJBvhYxUernhzsTeydY9dvDwRJ0XEY76dWSoGnQuFsg7SON7Rwp-Z_fleFhoxrbXrTaRQbCPLgyxu--i1W9aHAztRYHSqY9SOVDZ3Rgs7wu_lX8CJROWLM_q3DAxD5Cod3ODRt8C1YDRjqoxfi86hYLbfZXB30J6hvsyKTBC8UVQO6ug8-OcriRzajjun2UBt3QBBPIzBK0hudAuA0BdSFS9l0D35iGHXCBcbUt5PD1dp4FGuIhE0Ajr_zziGIDtyrbpuoX1edXWVqWL1OLq2uGVBlbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی بچه های تیم New Castle !  همه هم پنج سانت و ده سانت و …</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19918" target="_blank">📅 20:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19917">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حجم تحقیری که ترامپ به عنوان رییس جمهور آمریکا دارد می شود کم نظیر است!  پس از افشای داستان فرار ترامپ از ترکیه با یک هواپیمای فرعی — آن هم داخل کامیون کترینگ هواپیما ! — دیروز خبری منتشر شده که ترامپ حتی داخل زمین گلف خودش احساس امنیت ندارد و همانطور که در…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19917" target="_blank">📅 20:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19916">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ:   ایرانی‌ها با ما بازی می‌کنند، در اتاق‌های جلسات موافقت می‌کنند و در رسانه‌ها رد می‌کنند.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19916" target="_blank">📅 18:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19915">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ: ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19915" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19914">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkrOaPwhwPS25hF4WjT4QRSJMTc7Y0-ShU8HcgEa_LAQHUwwSfHqaIWToIw93f8SvUCk-pRLHD6fPcvE0IKblIG5SDsFDDVUC4b7J99w5vje7Jr4dPBdWZ9_0M6VQkT3eDf4VyciyxxtimcoMmB_Xtw1V5OIVHiJcfCZOR8HlfzBk6g-gRV7EYjRdQpLSE4MEWHknvZESwPpncbmmtrZkdA78RKsASv5cfjInA3_2ZEZth-OG6sMy6aIHycrfjnLcq6lA_bZOSrp2iAGieoDv0cPCqNX_PRUiEoe_RU3DGxXvSMUyOq68iBH_GoYdo91HeQDSiK7982WL29MQE3y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط کم‌سابقه قتل در آمریکا
داده‌های جدید مربوط به نیمه نخست سال ۲۰۲۶ تصویری کم‌سابقه از وضعیت امنیت شهری آمریکا ارائه می‌کنند. بر اساس داده‌های Major Cities Chiefs Association که در نمودار نیز منعکس شده، در شماری از شهرهای بزرگ آمریکا میزان قتل به‌شدت کاهش یافته است.
این کاهش‌ها صرفاً محدود به چند شهر نیست. تحلیل داده‌های MCCA نشان می‌دهد که قتل در مجموعه شهرهای بزرگ آمریکا در نیمه نخست ۲۰۲۶ نسبت به مدت مشابه سال قبل حدود ۱۷.۲ درصد کاهش یافته است؛ بنابراین با یک روند گسترده‌تر در سراسر کشور مواجه هستیم، نه صرفاً یک اتفاق محلی.
یکی از عواملی که می‌توان در این تحول مورد توجه قرار داد، تغییر شدید سیاست مهاجرتی دولت آمریکا تحت رهبری دونالد ترامپ است. دولت ترامپ از آغاز دوره دوم ریاست‌جمهوری خود سیاستی بسیار سختگیرانه‌تر در قبال ورود غیرقانونی، بازداشت و اخراج مهاجران غیرقانونی اتخاذ کرده است. بر اساس آمار ارائه‌شده از سوی کاخ سفید، دولت در کنار کاهش شدید عبورهای غیرقانونی از مرز جنوبی، تعداد اخراج‌ها و بازداشت‌های مهاجرتی را نیز افزایش داده است.
از منظر سیاسی، دولت ترامپ این سیاست را مستقیماً بخشی از برنامه بازگرداندن امنیت عمومی معرفی می‌کند. افزایش فعالیت ICE، تمرکز بر افراد دارای سابقه کیفری، مقابله با شبکه‌های تبهکاری و کارتل‌ها و کاهش شدید ورود غیرقانونی، همگی می‌توانند از دیدگاه دولت نوعی افزایش بازدارندگی ایجاد کنند. داده‌های موجود نیز نشان می‌دهد اجرای سیاست‌های مهاجرتی در دوره ترامپ به‌طور محسوسی تشدید شده است؛ برای مثال، یک تحلیل مبتنی بر داده‌های ICE نشان می‌دهد تعداد بازداشت‌های ICE در مقطعی از سال ۲۰۲۶ نسبت به نیمه دوم دوره بایدن چند برابر شده است.
با این حال، نباید از نمودار فوق یک رابطه علّی قطعی میان سیاست مهاجرتی ترامپ و کاهش قتل استخراج کرد. روند کاهش جرم پیش از آغاز دولت دوم ترامپ نیز شروع شده بود و خود آکسیوس نیز تأکید می‌کند که کاهش جرم در دوره پایانی دولت بایدن آغاز شده و سپس در دوره ترامپ ادامه یافته است. علاوه بر این، عوامل متعددی مانند افزایش یا بهبود عملکرد پلیس، تغییر الگوهای باندهای جنایتکار، وضعیت اقتصادی، کاهش خشونت پساکرونا و سیاست‌های محلی می‌توانند در این روند نقش داشته باشند.
با این وجود، از منظر سیاسی می‌توان استدلال کرد که سیاست «مرزهای بسته‌تر، اخراج سریع‌تر و برخورد سخت‌تر با مجرمان» یکی از مؤلفه‌های محیط امنیتی جدید آمریکا است. کاهش ۶۰ درصدی یا بیشتر قتل در چندین حوزه قضایی، همراه با افت ۱۷.۲ درصدی در شهرهای بزرگ، نشان می‌دهد که آمریکا در حال تجربه یک چرخش مهم در شاخص‌های خشونت شهری است. بنابراین، حتی اگر هنوز برای نسبت‌دادن این تحول به یک سیاست مشخص زود باشد، دولت ترامپ اکنون می‌تواند این آمار را به‌عنوان شواهدی از موفقیت رویکرد امنیت از طریق اعمال قانون و کنترل مهاجرت در برابر منتقدان خود مطرح کند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19914" target="_blank">📅 18:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19913">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ:
ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19913" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19912">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.  او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19912" target="_blank">📅 16:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19911">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">محسن رضایی:
تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19911" target="_blank">📅 16:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19910">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.  او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19910" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19909">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.
او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19909" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19908">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک نفت کش که قصد داشته محاصره دریایی آمریکایی را بشکند هدف آتش نیروهای آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19908" target="_blank">📅 16:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19907">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بازآرایی ساختار نظامی و امنیتی ایران؛ حرکت به سوی فرماندهی متمرکزتر و مقاوم‌تر
ایران پس از تجربه جنگ‌های ژوئن ۲۰۲۵ و بهار ۲۰۲۶ در حال بازطراحی بخش‌هایی از ساختار نظامی و امنیتی خود است؛ بازآرایی‌ای که به نظر می‌رسد مستقیماً از آسیب‌پذیری‌های آشکارشده در جریان حملات آمریکا و اسرائیل، به‌ویژه عملیات هدف‌گیری فرماندهان ارشد، ناشی شده باشد. مهم‌ترین تحول در این روند، تلاش برای ادغام ستاد کل نیروهای مسلح و ستاد مرکزی خاتم‌الانبیا است. ستاد کل مسئول سیاست‌گذاری و راهبرد نظامی و خاتم‌الانبیا مسئول فرماندهی عملیات مشترک در زمان جنگ است. جدایی این دو نهاد از سال ۲۰۱۶ یکی از منابع بالقوه موازی‌کاری در ساختار فرماندهی محسوب می‌شد و اکنون ادغام آنها می‌تواند با هدف ایجاد یک زنجیره فرماندهی کوتاه‌تر و منسجم‌تر انجام شود.
منطق این ادغام، صرفاً اداری نیست. ساختار جدید می‌تواند هماهنگی میان ارتش و سپاه را افزایش داده، کاغذبازی و بوروکراسی نهادی را کاهش دهد و سرعت تصمیم‌گیری در شرایط جنگی را بالا ببرد. اهمیت این مسئله پس از حملات «سر بریدن» بیشتر شده است؛ حملاتی که با حذف فرماندهان ارشد، توانایی ایران برای هماهنگی عملیات تلافی‌جویانه را مختل کردند. بنابراین، ایرلت ظاهراً در حال حرکت از مدلی است که در آن بخشی از ظرفیت فرماندهی به افراد و نهادهای متعدد وابسته است، به سوی ساختاری که بتواند حتی پس از حذف بخشی از رأس فرماندهی نیز به فعالیت خود ادامه دهد.
انتصابات جدید نیز همین جهت‌گیری را تقویت می‌کنند. علی عبداللهی علی‌آبادی در رأس ستاد کل قرار گرفته و هم‌زمان نقش او در خاتم‌الانبیا، وی را در مرکز ساختار فرماندهی مشترک قرار می‌دهد. سوابق او در سپاه، فرماندهی انتظامی، وزارت کشور و ساختار ستاد کل، ترکیبی از تجربه نظامی و امنیت داخلی را فراهم می‌کند. در کنار او، کیومرث حیدری، با سابقه فرماندهی نیروی زمینی ارتش و فعالیت در خاتم‌الانبیا، به لایه بالای ستاد کل اضافه شده است.
در سپاه نیز تثبیت احمد وحیدی در مقام فرمانده و انتصاب مصطفی ایزدی به‌عنوان معاون فرمانده، نشان‌دهنده بازسازی سریع زنجیره فرماندهی پس از ترور محمد پاک‌پور است. انتخاب ایزدی، که اخیراً مسئول حوزه سایبری و تهدیدات نوظهور خاتم‌الانبیا بوده، می‌تواند بیانگر اهمیت فزاینده جنگ مدرن، حوزه سایبری و تهدیدات نوظهور در معماری دفاعی جدید ایران باشد. انتصاب حسین طائب به فرماندهی بسیج نیز نشان می‌دهد که بازآرایی نظامی با لایه امنیت داخلی و بسیج اجتماعی پیوند خورده است.
در سطح امنیت ملی نیز تغییر دبیر شورای عالی امنیت ملی و جابه‌جایی مشاوران ارشد، بخشی از همین روند تمرکز قدرت و هماهنگ‌سازی ساختار تصمیم‌گیری است. در مجموع، تصویر ارائه‌شده در انتصابات اخیر حاکی از آن است که ایران پس از تجربه آسیب‌پذیری فرماندهی در جنگ‌های اخیر، در حال ایجاد ساختاری متمرکزتر، یکپارچه‌تر و کمتر وابسته به یک فرد یا نهاد منفرد است؛ ساختاری که هدف آن افزایش سرعت واکنش، هماهنگی ارتش و سپاه و حفظ تداوم فرماندهی در صورت تکرار حملات علیه رأس هرم نظامی است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19907" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19906">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNTc8giodxi2Kdf5WKt6gQnFsdMLxPOxA62X0HEHbbDgIWdwgd5UHJoF-7lTqHwT7fr9ksfo6XSxKro8onBxBM6R7tDj8jJSwGVmN5uHRGf96AG9f_sxe3x47iji1jbCD0TXxTIqjnuIb76Qth1VFtHtzjmZ-QBmF5OlTgUS57lFGkNw2PHKzKqhJCyHQa6GE8I5o0HBwDhx6nXazUrtgFLpk_3HyLy_Y9-q5uowCtu1XjMS5nJc3VZ0qJ--Pshaczdd_mnWjxFcrlZwo0BSk_vR0IhpZxP9Rn7OT8zmTkb4D8YTJnr1QvLDP34dKJFewB1ElfGTO3JP_o4W0Ov5Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه درگیری های میان انصارالله و نیروهای دولت رسمی یمن</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19906" target="_blank">📅 15:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19905">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845af07e2f.mp4?token=WEJFL6H0wcM2awfa0JFLgJbkBi4W4dteEm6JboYFrUAEcEK--hSm8C4KHxWY5NNtNYXwt87TeHSK6Vz8ffw4F7L3FRvTkeypQbUOTtFRMY3WeyZBG181N-nsnIJW2EM0PtU6zlRKmHjdpZgRTD4mmLStFOr6q5aaEtHLfwFa_li7wskHfQ3zeM5wfpWgTy4fp371ZC1R2HbwlSchgwtXaO0ItUZ6wzIEpytIH4yrzB6vjCbbd7mGpHahkbuNPERlZrAsqn9fyewoT55idpj8K1f05glc96SSf7PqNwzZ39HWGY6jb22aVUA_YQMEStJ2fwuiunNyuyrHscItqoXKaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845af07e2f.mp4?token=WEJFL6H0wcM2awfa0JFLgJbkBi4W4dteEm6JboYFrUAEcEK--hSm8C4KHxWY5NNtNYXwt87TeHSK6Vz8ffw4F7L3FRvTkeypQbUOTtFRMY3WeyZBG181N-nsnIJW2EM0PtU6zlRKmHjdpZgRTD4mmLStFOr6q5aaEtHLfwFa_li7wskHfQ3zeM5wfpWgTy4fp371ZC1R2HbwlSchgwtXaO0ItUZ6wzIEpytIH4yrzB6vjCbbd7mGpHahkbuNPERlZrAsqn9fyewoT55idpj8K1f05glc96SSf7PqNwzZ39HWGY6jb22aVUA_YQMEStJ2fwuiunNyuyrHscItqoXKaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:  برای هر اشک یک مادر اسرائیلی، هزار مادر لبنانی باید بگریند. تمام لبنان باید بسوزد!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19905" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19904">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">302.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/19904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 23</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19904" target="_blank">📅 14:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19903">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">صد رحمت به جنگ (تحلیل ژئواکونومیک محاصره دریایی)  مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، طی گفتگو با خبرآنلاین با تاکید بر ضرورت فوری پایان یافتن محاصره دریایی بنادر جنوبی ایران توسط سنتکام، گفته است: این محاصره باید پایان یابد؛ با مذاکره، خواهش، تهدید…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19903" target="_blank">📅 14:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19902">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19902" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19901">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 23</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 23
سه شنبه 11 آگوست 2026</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/19901" target="_blank">📅 13:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19900">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟  ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19900" target="_blank">📅 11:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19899">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sX88V8V6L26CEUc5aDM8B3Cp3yiR1Z1xr3X6qd_fs_bKGEgSMc24PDCXktBjaROsjPxahB0QdZBQ8-WEZk7VB3MexFof5m7yd5m_nuoVkhy-C-U3YI7i1N4HD39fhFejgcsEL3Ovt0p-_pQwq2EIcHZQXMb7ihbtncCL--tdhppLLROOPATyk6PJYdK3kUK_gTahWrPQ7hgGCXqsFyYKsr4s4LVYan_LLZRFeQIMYjtyzbF0FnPbeClYX6sxOXkZ6hfeKdKfdddFFzakfSibn-dHVFRvTBvkgUZ08Svj8isnbTLa8YlS1GivHaiPI6adJtnh6vcLpRLtk6W6PMgYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه ای قرار دارد. در چنین شرایطی سیگنال قوی خرید یا فروش صادر نمی شود و بهترین راهبرد از دید من خرید در سطوح حمایتی پایین تر است.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/19899" target="_blank">📅 11:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19898">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtgAItEgZEzSb63sfr0woX5a_jsmos6gSJ4P3fIbt1c73qe71XhdQBk7gfNisP5y_9rIENfzGL7ZOTfSEUSkGhA15sG-eo8jpUEtkpAgjGbf39f9WfOWldBfUizLOuphujqLstZel2eZvJZ3IzSPiWo_Y1g2mwxs_TZgEeFM1dQacvlp1Jeee_He6vIZXGpNFtLQsq6PnqefK5qzqO-JwP-QjFesnjxSRCPUVgbFycyCSY27DmoDNhsUqFhH-oFiCkPPOqyaFxgdzKyYyfsVz5CsODz3eskBMQak-rCmV1TjEx9ugiXpPoJhfLiD9FNoT04ezGV3EWQ03PMjOLiBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با برجسته کردن بیگانگی فرهنگی امثال این چپول عرب تبار با فرهنگ غربی غالب در آمریکا به دنبال کاهش امکان شکست جمهوریخواهان در انتخابات نوامبر است.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19898" target="_blank">📅 11:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19897">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انزوای روزافزون در جهان   کاهش اهمیت راهبردی خاورمیانه برای واشنگتن و برونسپاری مدیریت خاورمیانه به اعراب مسلمان  قدرت گیری روزافزون ترکیه و محور اخوانی  نیاز به حضور مستقیم در بازی کریدورها</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19897" target="_blank">📅 11:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19895">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGw6Y8MH_iH00JmD94ChyFWof0-gH8zYutvulO4m9vaiMCydts5-gCa8hkN3-GAN3fV_j9CY-JkKplAnZavBwKaeLSFUAmOctpp9ixQbWe4PvB9dCbYHxQnG3DLyu0An_IKoZONRhw6vTSBCv7toN5_-LhuEQk-nQSOxm_pMMZpK4uOp6l1ntH4bvc0C5JPHB9M2TDenaLLX3y8JUGnjH6xQOWN--GlonmUkiZ_GboF4P3qnwB2CHS-wQ7mgujfQu3yNTT4NLFzYcohFyApT19Z6SnP-w6jZs0fTnHjyvQZAOt3ihISxaSmS9Y97nvx640Z4W73NKsaTBiBhAIN45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGCqOhLP1pJo1PNuFk9jgQRdGJ1zVNpoYGGlo4OrTB7CfI3tS2_5ch6otjYHrnyfhTDB8nAhYU7clofvS2L-J4C35GRdZ6Yb-RXKM-dbSudFrQexoJXRT6BwH9bEXuBcg9X-L9-gFcCkLgYJtn4NNvuxOEEK9O2gXf9HH-IDpSEMxW6MhETTgY-UvGQr7RI5_dKMvLKEUhi2LIzEK7fH8ICW22JCF--2PO0ah_Lf62pRxHwXpnU8xH5NbXrv1b97AaxvYZdFkMdw21iaql8AUooNGRLn8xL7npkj8KEkCx4MLsFOcjHVWzTqdv3_ULeVGRzQCYn27aebcyusBAszzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش واشنگتن پست، دونالد ترامپ، رئیس‌جمهور، ماه گذشته پس از نشست ناتو، به دلیل تهدید ترور از سوی ایران، به صورت مخفیانه با یک هواپیمای C-32A نیروی هوایی ایالات متحده از آنکارا، ترکیه، خارج شد، در حالی که کاخ سفید به صورت عمومی اعلام می‌کرد که او با هواپیمای…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19895" target="_blank">📅 11:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19894">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انصارالله یک کشتی تجاری عربستان را در باب المندب زد و ۳ نفر کشته شدند.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19894" target="_blank">📅 10:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19893" target="_blank">📅 03:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">طبق گزارش واشنگتن پست، دونالد ترامپ، رئیس‌جمهور، ماه گذشته پس از نشست ناتو، به دلیل تهدید ترور از سوی ایران، به صورت مخفیانه با یک هواپیمای C-32A نیروی هوایی ایالات متحده از آنکارا، ترکیه، خارج شد، در حالی که کاخ سفید به صورت عمومی اعلام می‌کرد که او با هواپیمای…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19892" target="_blank">📅 02:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8GNZ5D335zMdH90lJ0ybd1Z1mFSk1hpUI19vEr6YpfLPGaUqZx8m6gowSQqLUG1EFCVSbmIvP9JLlHIjjsoifeqEvDVj1wJzlASWuQQq4Iz_aVM5Ma_yTxljDhpt6b6-SI2QWFDmrfVGKVlZety-sOYmdoq6Zlk-nT9WWYW7vD-kY02SgpzqNTI9fFJVvGoOSOM7C8FD9Ra_ygxh-OjeKz2LFCVFZDlXcBrJ2qAkqEyQ8YDS8X3HuOPoueE4nWs8O8CZ8QInCWJFjzIePd9HXc-Nna3xQ5b3EOVcv3f9gW99DkAu8TVTcpkP26t8qiWNxMFkQYSBReTAoxNMJzA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می‌شود ایران در جریان سفر ترامپ، رئیس‌جمهور آمریکا به ترکیه، تلاش کرده است او را ترور کند.  اطلاعات ارائه شده توسط یک منبع خارجی که به مقامات آمریکایی در مورد این توطئه ادعایی هشدار داده بود، باعث شد تا در آخرین لحظه، هواپیمای مورد استفاده رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19891" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCAy1w2gtW4ySwMsFo6XlCtM6eEVf74eL4zGK0SqsY1c8ukLVd-mvFYqlj3y-JVFJFRaDP-j4DxhIpt6pjGxiCrQ6el2X0nVPe1uZmKEHb5ZO-DbQwnFpz03csJDy9Ma6WiKVIGB2LxBNpVN6gC0AUCkYgn1xi02upsGExmui0tfX47WnuQ5sBb0j075bCVbdWjSVFis6mnDSJC94hQuohzGLdrcNj7QeAeSh0ijCJ23Ita7H568ztz-QwfHYN_xhcbPh2rNngGdJVhWT7683wQVgSoY1JKippXLlcRKwts4tkitzPUCRRb_zIdah_ik4a1stfpTr3wvjUQVIYfFqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19890" target="_blank">📅 02:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19889">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg0pxC__fuDSvRRHUPcMLzYq8tz9PlJIiTxxon2_hV6FodTKCs-KS7gbgyJ7CcIb-sDXClOhkraZv3ttGbPjMrXiZUDWYommJPIxZ5ICEKI6q895vBbPdyYTipu1WMBxCMUhY6L7n40_iAfazUP8yRjMygvMEziTXeL5xdgyl8G8KBOc6F6NO_mC5BLyYxuK0Sy8POI2i8hX0d9HQiEj8vKyGphieJK-b_XKplbkBuye1m-TYVMIGBNKFpIk0WwftgjxiRdiXusMesymZ3IEVjMo14GNIjNiKDQD325e20hO-DFufjM52jo5ARAY73I9LQuW9qAaT3qW-FoD4AcVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان آغاز جنگ ، ایران بیش از ۲۰۰۰ حمله هوایی، موشکی و پهپادی در سراسر خاورمیانه انجام داده و حداقل ۲۰ سایت مورد استفاده ارتش ایالات متحده در هشت کشور را آسیب رسانده است.
این حملات تا ۱۳ میلیارد دلار خسارت به تجهیزات ایالات متحده و تأسیسات نظامی وارد کرده است.
بیش از ۴۲ هواپیمای نظامی ایالات متحده نیز آسیب دیده یا نابود شده‌اند، از جمله چندین فروند که در پایگاه‌های هوایی پارک شده بودند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19889" target="_blank">📅 01:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19888">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e06c6847.mp4?token=QnqlBAZrUp-obxTj539493yHzHIJhDx3l5ugxTL4T2d7xlEDCd42mldFlQLbeX9c8XJoh2KsLKGmg5D_46SZ6_gNtwXMQyGt_8PQ1w4zXLGF2sw8nloRij-Zy27lCYk67lTweXVz5Th8GsfMYHtdx5cwr2JwhCfvcuJZIp491X3y-8gUJqqiFg9Adp_u8GAhlKAjXQOg-ZJNKcEX9Gvt80KcT44g7fwNFw-wMaZocyuXwIY_BPi_WtArBr61Se5bzW6SzgV8M5g7usVoUn04_HhN-0BLU2JoWrcwl8Mpt3C8AsmjENckeAUhajjjXRGnxCYXyYcZ9zQ_8oPcebg4AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e06c6847.mp4?token=QnqlBAZrUp-obxTj539493yHzHIJhDx3l5ugxTL4T2d7xlEDCd42mldFlQLbeX9c8XJoh2KsLKGmg5D_46SZ6_gNtwXMQyGt_8PQ1w4zXLGF2sw8nloRij-Zy27lCYk67lTweXVz5Th8GsfMYHtdx5cwr2JwhCfvcuJZIp491X3y-8gUJqqiFg9Adp_u8GAhlKAjXQOg-ZJNKcEX9Gvt80KcT44g7fwNFw-wMaZocyuXwIY_BPi_WtArBr61Se5bzW6SzgV8M5g7usVoUn04_HhN-0BLU2JoWrcwl8Mpt3C8AsmjENckeAUhajjjXRGnxCYXyYcZ9zQ_8oPcebg4AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی بچه های تیم New Castle !
همه هم پنج سانت و ده سانت و …</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19888" target="_blank">📅 01:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19887">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌توانند دردسر درست کنند، اما ورشکسته هستند. پولی ندارند.  ایران کاملاً ورشکسته است. آن‌ها به سربازانشان حقوق نمی‌دهند.  تورم آن‌ها ۳۰۹ درصد است.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19887" target="_blank">📅 00:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟  ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19886" target="_blank">📅 23:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19885">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟
ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19885" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19884">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایران_تا_چه_اندازه_می‌تواند_تنگه_هرمز_را_به_یک_سلاح_ژئوپلیتیکی_تبدیل.pdf</div>
  <div class="tg-doc-extra">538.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19884" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکات بسنت در مورد تنگه هرمز:  تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.  آنچه در 2 سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19884" target="_blank">📅 22:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19883">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7qo8JU3H9Re2KH9CUB-jil7STUfTPav0ji5zyYtCCYyOyA0NemdpMtBpU9XF934UWo99azlKfCpdMmSrQEsgUzyCghiC0hLB6OK9TrU-V6JiWdR8jdfP_n93124iyLo6YMVP8xQrwoxcQKlNMrEKaHiE3aHUPvE9peK6uFB6ofH_z8pDQFxaB1oBlSG2WoV-41UonBzz5eXb7wItmnRdGMFTUuFqsGileqmiAmEdgfdVATm2zYiUDuVj9cT0oVJymYbukKTDAn71hnihz2NrXAzwKyHjrS9LAkXlvfvcvbqDOJDR4im5MKQ140D-VH2VC-m-jvt8n6dYqFVeBzZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی است و لذا اصلاح های محتمل نزولی طلا خرید دارد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19883" target="_blank">📅 21:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19882">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">302.5 KB</div>
</div>
<a href="https://t.me/SBoxxx/19882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 22</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19882" target="_blank">📅 21:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19881">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آمریکا پس از سوگند یاد کردن آبلاردو د لا اسپریلا، که با حمایت ترامپ به عنوان رئیس‌جمهور انتخاب شد، متعهد به ارائه یک میلیارد دلار کمک به کلمبیا شده است.  او وعده «جنگ تمام‌عیار» علیه تروریسم مواد مخدر، سرکوب نظامی سخت‌گیرانه‌تر علیه گروه‌های مسلح و روابط امنیتی…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19881" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ:
🔹
من متوجه شدم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماه گذشته به آنها وارد شده است، دارند (درگیری که به این دلیل آغاز شد که "آنها نباید سلاح هسته‌ای داشته باشند"). با این حال، این موضوع در هیچ یک از…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19880" target="_blank">📅 20:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شرایط ایران برای باز کردن تنگه هرمز</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19879" target="_blank">📅 20:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔖
واشنگتن پست :
پنتاگون به مدیران صنایع دفاعی ۲۱ روز فرصت داد تا طرحی برای تولید سریع تسلیحات ارائه کنند</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19878" target="_blank">📅 18:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19877">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4Exa65HcsEYY5QzDYsfW5_8Ya0GjutfF4cLXgXcBR3ym-5iZ96DklHpfGJ-pCqoBMoxCW87O5rvqg20dkFTzkQU5iUQDK0UCzXkuNPkFUtHgxjxDUtKTEe39dpQ9xDxspY9kO11dAQpyKZLuvglqFJC2-GEiD4MGFad5O1wghDL5sEXvIZL9ivLUDxU0RgTK0kMSgjx3X-FkI6ZPVB4M1_Nfhq8iEg2KN2SorgsGCkD5OxNPc5gn9JqIWQZSpI0xvREGL1orlKUxJei8NE58E5CxdeG-aiZmHEltNpR1sxfOUSeqsuzx_RNQnWHPknSL7lmQo3Uv_i8B5hRZK-UQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
قانون «لیندسی گراهام»؛ تشدید فشار بر روسیه و ایران و آغاز یک جنگ اقتصادی با پیامدهای جهانی
قانون لیندسی گراهام با هدف تشدید فشار اقتصادی بر روسیه و ایران، تحریم‌ها را فراتر از کشورهای هدف برده و خریداران انرژی آنها، به‌ویژه چین و هند، را نیز تحت فشار قرار می‌دهد.
اجرای این سیاست می‌تواند جریان تجارت انرژی، قیمت نفت، تورم، نرخ بهره، دلار و بازارهای جهانی را تحت تأثیر قرار دهد و تحریم‌ها را به ابزاری برای شکل‌گیری یک جنگ اقتصادی گسترده‌تر تبدیل کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19877" target="_blank">📅 16:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19876">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXPuK856U3QRpi6G-5QA6ajnM8fAxgLN6OxHXRF4y23CiWD9xyo8gXodV4iUyyTxSlXrijVBKOyERwH9sudcXZ2wXtGeZ3Di8D5dcDFr3muYoWSgBUK1fpYoeDFo4kHWC6uWHCia19OhWDwfz_FhmWqquK4zMYhW3KTui7RllmpdQFovSb_mPtWDWmk-oxwC2VIpW98eQUaxljSe4zfu003mB3ag8PG2Pyp1cepVSTrOWgP1EeqxKf_GMhZGm19MDnzGvhC5JbGa0Bj-zzulwFUb6Ioe60U5SOx1QMm_v-5x43YRn2IacyONJG_2mbwZqOGgj4JFWhN0VfghPZIhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:  علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم. ﻿</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19876" target="_blank">📅 16:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19875">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 22</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 22
دوشنبه 10 آگوست 2026</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19875" target="_blank">📅 14:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19874">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">— وزارت کشور عراق:
«هر پهپادی که بدون مجوزهای لازم پرتاب شود، به عنوان عملی تروریستی تلقی خواهد شد».</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19874" target="_blank">📅 13:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19873">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19873" target="_blank">📅 13:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19872">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19872" target="_blank">📅 12:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19871">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مایک والتز، سفیر ایالات متحده در سازمان ملل:  "عربستان سعودی، ترکیه، پاکستان و احتمالاً مصر در حال تلاش برای تشکیل یک ائتلاف دفاعی برای مقابله با ایران هستند."</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19871" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19870">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktuBo6EsoO99Nhpjfyz7fBNxgWoU6EKSTRnX_wOSIAiKmJ7IUnLFlyRfen43I_4w2kDgE7gQ3OMNwRRQ0iJlAQycFxeDrUr8UPNe8ew-dUhhCrFjjBSjivDpFt1jjsO4YddxD7Z6k4Ka3prG5wgblZP0W5OTRUi7MV8uKIxni6iVWzm5PeXOm7RKS8Sw6UgnhdPD9uPHZ1zZf4VW9BdKiP_GKBJ6su0s5Qm0P7mVXuz2ISJqn2zR7DRNhY7wsO2tyWvv7IwAYpzKMFxXMYuU2IJRo7cZwsgYrkbnO4ToLcytNn5hncpX07Vzaoa5z0TsDIvDLa3VFPyXTjF01H4r0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل جدیدترین و پیشرفته‌ترین زیردریایی خود را از آلمان تحویل گرفت
شرکت آلمانی
ThyssenKrupp Marine Systems (TKMS)
در اواخر ژوئیه ۲۰۲۶ زیردریایی جدید اسرائیل،
INS Drakon
، را در شهر کیل تحویل نیروی دریایی اسرائیل داد. این زیردریایی، ششمین فروند از خانواده
Dolphin
و سومین نمونه از نسل ارتقایافته
Dolphin II
در ناوگان زیرسطحی اسرائیل محسوب می‌شود.
دراگون با طول حدود
۷۳ متر
و جابه‌جایی بیش از
۲ هزار تن
، بزرگ‌ترین زیردریایی ساخته‌شده برای نیروی دریایی اسرائیل تاکنون است. این زیردریایی توسط شرکت آلمانی TKMS ساخته شده و از سامانه پیشران مستقل از هوا (
AIP
) بهره می‌برد؛ قابلیتی که امکان ماندگاری طولانی‌تر در زیر آب و انجام مأموریت‌های پنهانی در فواصل دور را فراهم می‌کند.
ارزش این زیردریایی در منابع مختلف حدود
۵۰۰ میلیون یورو
برآورد شده است. طراحی پیشرفته، برد عملیاتی بالا، سامانه‌های شناسایی مدرن و ظرفیت حمل تسلیحات مختلف، INS Drakon را به یکی از مهم‌ترین عناصر قدرت دریایی اسرائیل تبدیل می‌کند.
ورود این زیردریایی به ناوگان اسرائیل تنها یک ارتقای فنی نیست، بلکه پیامی راهبردی درباره حفظ برتری دریایی این کشور در محیط امنیتی متغیر خاورمیانه و شرق مدیترانه محسوب می‌شود.
در سال‌های اخیر، افزایش حضور نظامی ترکیه در شرق مدیترانه، توسعه نیروی دریایی این کشور، برنامه‌های مربوط به زیردریایی‌های جدید و رقابت بر سر نفوذ منطقه‌ای، اهمیت توان زیرسطحی اسرائیل را افزایش داده است. زیردریایی‌هایی مانند
INS Drakon
به اسرائیل امکان می‌دهند تا یک ظرفیت پنهان، دوربرد و مقاوم برای جمع‌آوری اطلاعات، عملیات دریایی و ایجاد
بازدارندگی در برابر رقبای منطقه‌ای حفظ کند.
اگرچه اسرائیل و ترکیه در مقاطع مختلف روابط امنیتی و نظامی داشته‌اند، اما اختلافات ژئوپلیتیکی دو کشور در موضوعاتی مانند شرق مدیترانه، منابع انرژی دریایی، سوریه و نفوذ منطقه‌ای، باعث شده است که هر دو طرف به تقویت توان نظامی و دریایی خود ادامه دهند.
تحویل
INS Drakon
را می‌توان بخشی از راهبرد بلندمدت اسرائیل برای حفظ برتری کیفی در حوزه دریایی و تضمین آزادی عمل در یکی از حساس‌ترین مناطق ژئوپلیتیکی جهان دانست؛ منطقه‌ای که رقابت قدرت‌های منطقه‌ای در آن به‌طور فزاینده‌ای در حال افزایش است.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19870" target="_blank">📅 12:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19869">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، چیکلی:  اتحادیه مکه یک تحول بسیار خطرناک و نگران‌کننده است.  عربستان سعودی اساساً روی دیوار نشسته بود. آن‌ها قبلاً یک توافق دفاعی با پاکستان داشتند، اما به محض اینکه با ترکیه‌ای‌ها که در تقابل مستقیم با ما هستند و این تقابل می‌تواند…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19869" target="_blank">📅 12:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19868">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بقائی:
بازگشایی تنگه هرمز به لغو محاصره دریایی آمریکا مشروط شد</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19868" target="_blank">📅 11:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19867">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdqM2xuEe2EpOLGGSGCSTfyBAv8RL-EPRDy5BrjOFByBkbFmfB_ZlKeHsCQOl88t6xu4pfpRnHTOGxIvSZCRDqS4z_8QykUtJChfBmryZtr895KSmCc1f2Y-2jcFTJ1kK_iogBEF7UHIiOpnVjnLB_S8CE0C14KK4UC7MQHa_CNQlc_jo_p9FnmQ4_QyoppGlM2DESRWO_JVS7v36fz5nGZOfBA0Q80QvFAYB4dk_V5TVd4vmLqJlNgkOftvibwcswrAzmfHYtaePmwJzRXqL7LiMD0IR5mTndHDPlv5kXwscKFgW4MDH-5KItoXWTl6IpUJIeK19oHZw7uBY5OzCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی است و لذا اصلاح های محتمل نزولی طلا خرید دارد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19867" target="_blank">📅 11:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19866">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/klfqjMP5h3-v2WfXDzWk8tp3qkKG9vYRL3qV-455z3gBNy-d6YEhuC5vTfsfVUwhOyeD0hyCvtB1nM5NzJIs1jAoe65Q8hHO18p75rYrxqtg1UixNj2GX39VF9jOwp2GrTwV8wOUN_dwv6GqhCzcGYgFWSbRxnMh54REMbke8MfSFXn5aUmZuEZigDMxzOLW2kCrBc7xAwMOdkKs8vwy4HCIPOElo6qTys_Dc9okD0g8bV3y0uKU-1q_olRWCkosHoPM_0rWZDWlfOh4zCnZQlYd6cGTByskRGyIQmEtJrw3POYDWq-r2YVACHt6zh_idiEabcb8I8oCVPGKwJF0NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بشکه تاپاله
که گازشو لیلاز خورده
آبشو میثاقی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19866" target="_blank">📅 10:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19865">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سرنگونی یک پهپاد ناشناس در جنوب کشور توسط پدافند</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19865" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19864">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">احتمال پیوستن مصر به توافقنامه سه جانبه عربستان، ترکیه و پاکستان   «هاکان فیدان» وزیر خارجه ترکیه مدعی شد که مصر ممکن است به این توافقنامه مشترک به محض حل و فصل برخی مسائل فنی بپیوندد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19864" target="_blank">📅 02:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19863">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سرنگونی یک پهپاد ناشناس در جنوب کشور توسط پدافند</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19863" target="_blank">📅 01:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19862">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ما فقر شرافتمندانه داریم پدرسگ!  در ضمن علم بهتر است از ثروت!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19862" target="_blank">📅 01:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19861">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ما فقر شرافتمندانه داریم پدرسگ!
در ضمن علم بهتر است از ثروت!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19861" target="_blank">📅 01:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19860">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQlIuEPgeFd-74b7XBsSar2fEIrgEWbDIQH9wIAVSYp6GMvw6p_GpnHDssjf0O4QN9sYze8ukI9SJlxhlfa1fIkXkY_vegyPCVZmsQ6vmoBp4BJrkGwYL2ahRHC8ReVGNU7f6b3eZfZMCJ5VayhPa08uolhnUVybwq5l5yu_G_4DDVI9kdVJJo8lCnPeksxZKBbb4gftY71ijdHRiMKvRy4lHuJAvCdyd8CsrDL0YhgE7eEdLArmnHzOsv24V8bKmWb9ZiIW18oBIAZ0Ar37XoJRbXsIceHiYw9CK8UwAcdEXoOQK1afGK9rasUObDAh_03JnIw4F45lHKB5Mhq9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب محسن رضایی به عنوان دبیر شورای عالی امنیت ملی با حکم پزشکیان  معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور:   با حکم ریاست جمهوری اسلامی ایران دکتر مسعود پزشکیان، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد  سیدمهدی طباطبایی نوشت؛   نظر به…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19860" target="_blank">📅 00:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19859">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQtUhNY6Lhr0cHu6bO7HpWt-MtmBrfF8RM97xNJGg05JlqlEG1n3revEQ7Rs8Ky6x7EpiFm2ir9VXo58FXYtz4yxxT6Lp1sZUXH35SOgdhkk8iPwN04N_PRS_WXBQRO4Xpz-QVncrB_PLFIoauMSBDwLXujGqQbirKGgmyOUJQKb36zlSsr7x6Bv_SK0beOMCk81fQbjGhsk_QfgVIgMsaWnakx1-WhzlZU6jP8S06j0mAEM8AzasdNEvm9PA5QCPZ6rFzGl3HquWyrz0-l1vzKkWIBYfE8LiSL3Mu8CdE5QWbEF-nFC8JX3ENhMGhm7fH2SCyq67xvKrELvPcaltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درباره ایران:  ما فقط در حال مذاکره نیمه‌کاره با آن‌ها هستیم. ما صرفاً ایران را با تورم عظیم و واقعیت اینکه پولی ندارند، زیر نظر داریم.  منبع: آکسیوس</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19859" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19858">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بزنید شبکه آی فیلم سریال آیینه عبرت
عینا شرایط امروز ماست
سبحان الله!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19858" target="_blank">📅 00:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19857">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شلیک از سیریک به سمت کشتی هایی در هرمز</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19857" target="_blank">📅 00:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19856">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هواپیماهای جنگنده آمریکایی دو فروند هواگردی را که در حال نقض منطقه پرواز ممنوعه بر فراز ملک ترامپ در نیوجرسی بودند، متوقف کردند.  رئیس جمهور ترامپ در سلامت کامل است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19856" target="_blank">📅 22:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19855">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بنا به گزارش‌ها، ایالات متحده فشار خود را بر اسرائیل برای کاهش درگیری‌ها در غزه، لبنان و ایران افزایش داده است.  واشنگتن خواسته است که اسرائیل حملات خود را کاهش دهد، از مواضع بیشتر در جنوب لبنان عقب‌نشینی کند و طرح اعزام نیروهای چندملیتی به غزه را پیش ببرد.…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19855" target="_blank">📅 22:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19854">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بنا
به گزارش‌ها، ایالات متحده فشار خود را بر اسرائیل برای کاهش درگیری‌ها در غزه، لبنان و ایران افزایش داده است.
واشنگتن خواسته است که اسرائیل حملات خود را کاهش دهد، از مواضع بیشتر در جنوب لبنان عقب‌نشینی کند و طرح اعزام نیروهای چندملیتی به غزه را پیش ببرد.
اسرائیل با برخی از این درخواست‌ها مخالفت کرده است. نتانیاهو گفته است که ارتش دفاعی اسرائیل به مقابله با تهدیدها ادامه خواهد داد و اسرائیل این گزینه را برای حمله به ایران حفظ می‌کند، در صورتی که ایران از سرگیری فعالیت‌های هسته‌ای یا توسعه موشک‌های بالستیک را آغاز کند.
منبع: شبکه ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19854" target="_blank">📅 22:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19853">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59886795a.mp4?token=QNegktjHACL57r4I-N9OUBvf5FzFF0mQEAPmvAENh23N3Dmb0dnwVt665ExjxH_m73KwAR3b4Guoe1I7_uQiqqdcqw59o88Dk2mbm0eyskezEKnWTjFXxQVxakuYHnkyqPyMqWKQOe_cJIaWStkwLll2Xwpa-uItK9C-2j4eBJVkifDzsQTigRaeMgtjoOUTMRq3RRXsO5eW8YUhm_CoGJGnyoSxD0NI4lahIjbJ2oWnrL_WKPk-WD2ViDDGk3aYVyVydwXvMJ4s_3hMk6Oj_-mS3fSxHZ2NWU6NrdNUZz4UfKGF4-cEGgCCKY_wdH8uDs28AvqE62NTDb3yC0TbLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59886795a.mp4?token=QNegktjHACL57r4I-N9OUBvf5FzFF0mQEAPmvAENh23N3Dmb0dnwVt665ExjxH_m73KwAR3b4Guoe1I7_uQiqqdcqw59o88Dk2mbm0eyskezEKnWTjFXxQVxakuYHnkyqPyMqWKQOe_cJIaWStkwLll2Xwpa-uItK9C-2j4eBJVkifDzsQTigRaeMgtjoOUTMRq3RRXsO5eW8YUhm_CoGJGnyoSxD0NI4lahIjbJ2oWnrL_WKPk-WD2ViDDGk3aYVyVydwXvMJ4s_3hMk6Oj_-mS3fSxHZ2NWU6NrdNUZz4UfKGF4-cEGgCCKY_wdH8uDs28AvqE62NTDb3yC0TbLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19853" target="_blank">📅 21:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19852">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🟤
«محسن رضایی» نماینده رهبر معظم انقلاب در شورای عالی امنیت ملی شد.    شنیده‌ها حاکیست که آقای محسن رضایی به عنوان نماینده رهبر معظم انقلاب به ترکیب شورای عالی امنیت ملی کشورمان ملحق شده است. بر این اساس، هم‌اینک آقایان محسن رضایی و سعید جلیلی به عنوان نمایندگان…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19852" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19850">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🟤
«محسن رضایی» نماینده رهبر معظم انقلاب در شورای عالی امنیت ملی شد.    شنیده‌ها حاکیست که آقای محسن رضایی به عنوان نماینده رهبر معظم انقلاب به ترکیب شورای عالی امنیت ملی کشورمان ملحق شده است. بر این اساس، هم‌اینک آقایان محسن رضایی و سعید جلیلی به عنوان نمایندگان…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19850" target="_blank">📅 21:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19849">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔥
توقف ۲۲ روزه صادرات نفت ایران از خارک
🔹
ویندوارد: خط صادرات نفت ایران از جزیره خارک، تحت تاثیر محاصره دریایی آمریکا، برای بیست‌ودومین روز متوالی متوقف مانده.
🔹
هر سه پایانه غربی، LPG و شرقی خارک همچنان بدون بارگیری هستند. @khate_energy</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19849" target="_blank">📅 20:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19848">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7c7abbdc.mp4?token=W1kLZqH9Y4H4jr22Uxfy53BbYrgsytdTEf1dqels8qjjr0Z513s_yd0SViEjdIRomeYdvaFCV3ZJwFVwm3UjBz5s4hp6wmmoGnn-PoGrVc5w4tXSRuOL7yBCMYCIDzEawUWOTXgDT8BqAAynIo33dqMS9Zjiom4EUvk33rmzm_icwpDsoe2ZUwO3oEXqKmNhGMQa19YUks0m351QeBXyIe2i0BV36P2XvQFIwEgkWKP_zgGDdxDtxqIVtoZvXVEu7vh8A_OzNERsRLDZKsr5vo-UVMag4nexZh4TzFkhBs6GwbnrJ6BtWqiOCvSWocG4taxLWjwtF_zg4yIviScNWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7c7abbdc.mp4?token=W1kLZqH9Y4H4jr22Uxfy53BbYrgsytdTEf1dqels8qjjr0Z513s_yd0SViEjdIRomeYdvaFCV3ZJwFVwm3UjBz5s4hp6wmmoGnn-PoGrVc5w4tXSRuOL7yBCMYCIDzEawUWOTXgDT8BqAAynIo33dqMS9Zjiom4EUvk33rmzm_icwpDsoe2ZUwO3oEXqKmNhGMQa19YUks0m351QeBXyIe2i0BV36P2XvQFIwEgkWKP_zgGDdxDtxqIVtoZvXVEu7vh8A_OzNERsRLDZKsr5vo-UVMag4nexZh4TzFkhBs6GwbnrJ6BtWqiOCvSWocG4taxLWjwtF_zg4yIviScNWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز همین که ۲ سانت عسل هم داشته خیلی خوب بوده</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19848" target="_blank">📅 20:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19847">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ایالات متحده توانسته صادرات نفت ایران را فلج کند – فایننشال تایمز   این روزنامه با استناد به داده‌های ماهواره‌ای گزارش می‌دهد که ایران حدود یک هفته است که در جزیره خارک نفت خام را در نفتکش‌ها بارگیری نکرده است.   این جزیره اصلی‌ترین پایگاه ترانزیت نفت کشور…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19847" target="_blank">📅 19:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19846">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پزشکیان:  علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم. ﻿</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19846" target="_blank">📅 18:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19845">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پزشکیان:
علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم.
﻿</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19845" target="_blank">📅 18:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19844">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حالا باید ببینیم ائتلاف «مکه» پاسخ می‌دهد یا صرفا برای دوشیدن گاو شیرده حجاز و نجد تشکیل شده.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19844" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19843">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ امیدوار بود که بازگشایی تنگه هرمز به او راهی برای اعلام پیروزی و پایان دادن به درگیری با ایران بدهد، حتی بدون توافق هسته‌ای. اما تهران خواسته‌های خود را به شدت افزایش داده است.
ایران خواهان خروج نیروهای آمریکایی از منطقه، لغو محاصره دریایی، برداشتن تحریم‌ها، آزادسازی دارایی‌های مسدود شده و دریافت میلیاردها دلار غرامت جنگی پیش از بازگشایی کامل تنگه است.
این موضوع گزینه‌های کمتری را برای ترامپ باقی می‌گذارد. به نظر می‌رسد ایران معتقد است واشنگتن برای خروج اشتیاق دارد و از توانایی خود در به هم زدن تنگه هرمز و جریان جهانی نفت به عنوان اهرم فشار استفاده می‌کند.
با قیمت بنزین در ایالات متحده حدود ۴ دلار برای هر گالن و نزدیک شدن به انتخابات نوامبر ، ترامپ انگیزه‌های قوی برای به دست آوردن یک توافق دارد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19843" target="_blank">📅 16:04 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

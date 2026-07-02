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
<img src="https://cdn4.telesco.pe/file/NlV7tWPI4i7UtYqfvRK39N94SiKNNSvme42seUSfgtjMQhMnepg9V9onJQO4ILfpOFCsoI-z2IU7Ytvk1K4SSsb7NrKW5EPZ9_GcBroi8-brhzG4uTueyrjxcM0si5__XFnOcIBcMobVAMDrzj5XFNnnrNuwtZ-GkN53f-gXellLuq82tqcrTY407sEHNPhIQ-bOydzSG7MaI1HHHMns868Ju-7_2jxR8E_LxXUSaqRXc-7nrqGq72FlVE7T0fHFKQBS3NbSXqhdr493ec38N7zL2HErykkyIMR3_BWv-EzMvH7E_WNsoETdFi-_jZZcwaPs1PG7g_oyofWsiD67-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-18167">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🩵
کاتز ؛ وزیردفاع دولت اسرائیل
:
ما درحال توسعه لیزرهای فضایی برای تهاجم خارج از جو زمین هستیم
يسرائيل كاتز ،  اعلام کرد دولت اسرائیل در حال توسعه لیزرهای فضایی به منظور توانایی حمله در فضا است.
به گزارش اورشلیم ،پست کاتز در نشستی با خبرنگاران نظامی گفت: یکی از اهداف اصلی که نخست وزیر و من تعیین کرده ایم این است که برترین استعدادها را جذب کنیم تا امروز هیچ کشوری توانایی اجرای حمله در فضا را نداشته است. ما باید در برخورداری از این توانایی کشور پیشرو جهان باشیم
او افزود: اگر به این هدف دست یابیم این امر میتواند برتری بازدارندگی، توانایی حمله و انهدام و دیگر برتری های راهبردی ما را در برابر دشمنانی که از منابع گسترده برخوردارند تضمین کند
کاتز پنجشنبه گذشته گفته بود اسرائیل مصمم است به بازیگر پیشرو در زمینه توانایی حمله از فضا تبدیل شود با این حال این نخستین بار بود که به طور مشخص از لیزرهای فضایی نام می برد
اسرائیل هم اکنون نیز در این حوزه از کشورهای پیشرو به شمار میرود و سامانه موسوم به پرتو آهنین (Iron Beam) را به عنوان یک لیزر فضایی مستقر در زمین تولید کرده است
سامانه پرتو آهنین که اواخر سال گذشته به ارتش اسرائیل تحویل داده شد نقطه عطفی تاریخی به شمار میرود زیرا نخستین سامانه دفاع لیزری عملیاتی جهان است که میتواند راکتها پهپادها و خمپاره ها را با هزینه ای بسیار کمتر از رهگیرهای سنتی، خنثی کند</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/18167" target="_blank">📅 16:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18166">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فرمانده سپاه پاسداران قم
:
تمهیدات زیادی اتخاذ کردیم اما بصورت قطعی نمی‌دانیم در مراسم تشییع رهبرانقلاب چه اتفاقی خواهد افتاد</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/18166" target="_blank">📅 15:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18165">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه (۱۶ روز دیگر) آغاز می‌شود.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/18165" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18164">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔻
غضنفری ؛ نماینده مجلس
:
یک شبه کودتای سیاسی علیه رهبری نظام درجریان است - تجمعات شبانه نباید جمع شود</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/18164" target="_blank">📅 13:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18163">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دلار ۱۷۷۰۰۰ تومان!</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/18163" target="_blank">📅 11:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18162">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTPMuDoY3dZihaDJ1hSD0HOmClQQ7sHNz68BuNIWyJr-ieAtHLrmr-XzUzzhmo4TP-Zvnf8ytf1IK8JOABpJiKEa58PpxQ6ePub_gPx2ypy-mBI21C46TGzB4d024QNanc0CZkUpdEmL7Zp8q1IdmbOuAutziTkilU5BE7eJsb5aSpnpV-rKdVEYjkXeMhoFZ3ZZyyxTgh-MulzZYJS8_dMYNpzWL60TRdK8QhgKqmsJdHeDMr9qlHHQykEUooICdckT0iLqaO_Lc3gkSUkdEtHW_q8Arw7GzIcjO4UGTGPLyQNBx-sdH3Uopmal56fDZOfHkyViNBUSL-Y28nGiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیکی برای امروز در سطح بالایی قرار دارد.
توصیه می شود با توجه به انتشار گزارش NFP، امروز با کمترین حجم معامله کنید.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/18162" target="_blank">📅 09:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18161">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">جهش انفجاری معاملات شخصی ترامپ در سه ماهه نخست ۲۰۲۶!</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18161" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18160">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18160" target="_blank">📅 01:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18159">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آمریکا رسماً توافق‌نامه‌ای برای ساخت سفارت دائمی در اورشلیم امضا کرد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18159" target="_blank">📅 00:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18158">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سقوط بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده در دریای عرب
ناوگان پنجم ایالات متحده اعلام کرد که یک بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده که به ناو هواپیمابر USS George H.W. Bush اختصاص داده شده بود، اوایل روز چهارشنبه در دریای عرب فرود اضطراری انجام داد.
سه نفر از چهار خدمه در وضعیت پایداری پیدا شده‌اند. جستجو برای یافتن نفر چهارم در حال انجام است.
ناوگان پنجم اعلام کرد که هیچ نشانه‌ای مبنی بر اینکه این وضعیت اضطراری ناشی از اقدام خصمانه بوده باشد، وجود ندارد و علت آن در دست بررسی است.
این دومین سقوط بالگرد نظامی ایالات متحده در منطقه در هفته‌های اخیر است.
یک بالگرد AH-64 آپاچی ارتش در 9 ژوئن در خلیج عمان سقوط کرده بود که ترامپ گفت که نیروهای ایرانی آن را سرنگون کردند و خدمه توسط یک قایق بدون سرنشین Corsair نجات یافتند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18158" target="_blank">📅 20:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18157">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:  چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.  چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18157" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:
چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.
چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18156" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">موجودی نفت خام آمریکا در ذخایر استراتژیک نفت (SPR) در هفته گذشته به پایین‌ترین حد از ماه مه ۱۹۸۳ رسید - EIA|</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18155" target="_blank">📅 18:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18154" target="_blank">📅 18:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18153">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fsj8D1_T1QS80GSpZnUq5UZTB4dWh64XJQnx1LWB3AbeNFfO7BeQ6hJl20Ve0Ytzk72XzNKSuXz0qvySFL75ItOBPI1dl_S0ml2bQ-dWUqdxTRQ3nBsgl4w2zV1Jo7RDeKVz-qsdMkWUWNNitnbez-dk-OF87mJvgOFkw5roLBxj2XiuX5BPLlIUj7Uz_V9nou3TPzdFzCMA-BLlQ6o2s33TvYdce0JKVWCQF7V7b8volVsgcDedsuU46KHS0kAeZTBkK5S9WL64QqferrhrBLbPgVuabWH9LE2TwCxhFI3mJg58sSIZvG4dQODR_EfTS10Bmmvu5GxBZxT9-z0NSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای سومین روز متوالی ، امانوئل مکرون با عینک آفتابی دیده شده است.
به نظرتان کار آن عفریته زنش است یا صبیه وجیهه رفیق بهزاد؟!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18153" target="_blank">📅 15:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18152">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گفته می‌شود با اجرایی شدن این توافق، قیمت چص فیل در سرزمینمان بزودی ۹۰ درصد سقوط می کند</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18152" target="_blank">📅 15:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18151">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">به گزارش العربیه، آمریکا و ایران به توافق اولیه برای آزادسازی ۳ میلیارد دلار از دارایی‌های مسدود شده ایران دست یافتند.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18151" target="_blank">📅 15:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18150">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18150" target="_blank">📅 15:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18149">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiUhQbzLVvkMQXQG6FV9-VDh5-aFuQOdx-ATtMdSZdblUtpOPLc_IU-tjljuubfCVcFkveE3jKy_Ksv6db6sAMBS1Ix2zFmDtRzgPZco0HaAFhKf6lB7GCNaNxhXvUcjLjMk_W7ZQfTLmavNiHrb8URaI5GaaYeXOfTwWtMrOfvf_FIhmKJv_ndiDmpVFAGB3OivnqZXZB6P5hO7m2hMZKPg6gcjlZrC0_s1mKufq8pmUZMwWgpy_teANGgkCRFY0Qm9v2mh-L8H0QHjUzSYS5tfBfEvLDqpfvxz44EaAMvPEqOm9WHIrovp6co4hWfa4tJOBC20ryyfCnrLUY2Hkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد دارایی های ریسکی و افت بهای نفت!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18149" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18148">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7rTXn4pG-Li1AYsnZsdfBGRh2zHwdZ0vpQm3V0vutdiTrvdBN3_gUsO_0zvzjbynvniEfpYisgtmXxtCwqWx-bJhGJnig1Um7gvzFkmCfCZm9ImUqFh-K4cCL-jPS9A85x5qckVJUQPk7ZLqXmiQrlYYm59aV7pkW_Z40RnYZ375yamgcmjxLtORQulbQhiJSJWPZ6XJ4ZQprESF7PwZ7BbuzPSXugpmtGBy1K-1sTF9gpADXWkDANg6JyuL3kRb1CkjU9xWyJWmepccT4_lIbQczmNSK8Jvqno5LUvRAeWDLfhlcFZC9U7M64cf5FVVd4uVzAoPlbdREu1fIHnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18148" target="_blank">📅 14:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18147">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عراقچی در پاسخ به تهدید کاتز برای ترور رهبر جدید ایران:
شرایط تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است.
رئیس‌جمهور آمریکا متعهد شده است که حیوانات خانگی خود را در تل‌آویو ساکت نگه دارد. اگر آنها به ارباب خود توجه نکنند، ایران به آنها درس خواهد داد.
هر تهدیدی علیه مردم و رهبری ما پاسخ فوری و قدرتمندی دریافت خواهد کرد.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18147" target="_blank">📅 14:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18146">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=KPAVU31X_h-xX-kawGE1NbpXhouG0mYwdD0T1QiHwgaapshCbuAE9mvEjrNayKakSnoze1OoTcRxkBGen3D-O0q2pydQvASAQ46y8dYnjP1c242z1GvBUxQm6Wdeead8IB_A_Lr7Jzi0U8GB5i00Qf6U3U1bXAwAssl7go8dKe8SmcKKKA6dz-wXc8kdkDdETqcZTfWRb7Nk4QK2HhgVZ13XvDhdxCBJx5N0QaQas2x-hFTwP8Tr2Qa2OBbjq6BgZXE3lVgK5OJBWwSob3nJeQMASldo0SMd-Xxlk6DyXRYPbx65P6QJ8SIvJFCqzgxMVtiPNkdqquQewFOaBTFvwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=KPAVU31X_h-xX-kawGE1NbpXhouG0mYwdD0T1QiHwgaapshCbuAE9mvEjrNayKakSnoze1OoTcRxkBGen3D-O0q2pydQvASAQ46y8dYnjP1c242z1GvBUxQm6Wdeead8IB_A_Lr7Jzi0U8GB5i00Qf6U3U1bXAwAssl7go8dKe8SmcKKKA6dz-wXc8kdkDdETqcZTfWRb7Nk4QK2HhgVZ13XvDhdxCBJx5N0QaQas2x-hFTwP8Tr2Qa2OBbjq6BgZXE3lVgK5OJBWwSob3nJeQMASldo0SMd-Xxlk6DyXRYPbx65P6QJ8SIvJFCqzgxMVtiPNkdqquQewFOaBTFvwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18146" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18145">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">محبوبیت فردریش مرز  به پایین‌ترین میزان خود رسیده است!  بنا بر گزارش بیلد و با استناد به داده‌های مؤسسه تحقیقاتی INSA، حدود دو سوم آلمانی‌ها از عملکرد صدر اعظم فریدریش مرز ناراضی هستند.  این رسانه اضافه می‌کند که حدود ۷۰٪ از شهروندان آلمان از عملکرد دولت ناراضی‌اند.…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18145" target="_blank">📅 14:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18144">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💳
اعتراض عضو فقهای شورای نگهبان به بازشدن اینترنت بین‌الملل
🔹
مدرسی یزدی
:
باز گذاشتن شبکهٔ جهانی اینترنت بدون ملاحظات کارشناسی دقیق از جانب متخصّصان متعهّد، به انواع بهانه‌هایی که نمی‌تواند جبران‌کنندهٔ آسیب‌های همراه آن باشد ـ از قبیل آنکه کسب مردم آسیب می‌بیند یا حقّ مردم است یا خلاف وعدهٔ انتخاباتی رئیس‌جمهور محترم است ـ کاری بسیار خطرناک است. این کار، اقتصاد کشور، امنیّت شغلی مردم، امنیّت داد‌و‌ستد‌های تجاری، امنیّت نهاد‌های مهمّ کشوری و امنیّت شخصیّت‌های مؤثّر نظام و سلامت روانی اقشار مختلف مردم به‌ویژه نوجوانان و جوانان را در تیررس دشمن آمریکایی صهیونی قرار می‌دهد</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/18144" target="_blank">📅 13:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6v8Dsi5kaDDhO4_qS8n35DcWjfV4Ajm6EGafTlq24rmHGhddspS9SZuvHHi_W3Iy3t5XoGbeYYuyVkdqFIjMVlEizcD2PLbDU7YtyuG3IB5WNssShVDK_7umFE1LOH7dXd54_AD4H90BlUeSCpGuLZQKvZMRVTn61IEZBi6MUnYfLtwxyZ0b5mpegGqX7AWixkvxwKJHR3fCnaMpI13uajinXuffs6dt_VND0FZWwk94GFPTcdYIDbV4u96pRZHitZAEbB55nJn7LoBUrnURUqAwzs-szYBghS_UQVpiimGP3fHLoyhC1wDHdkHGmEQdL9HvFHpevv_JLBTtE4s3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/18142" target="_blank">📅 12:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/18141" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">Secret Box
pinned «
🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/18140" target="_blank">📅 11:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه
ژئوپولیتیک و بازارهای مالی
ارائه خواهدشد.
یک
شاخص ریسک ژئوپولیتیکی
هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/18139" target="_blank">📅 11:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDpRshZ9gOK0MRZJNAkyVGRx0eVB_I5u4wexgxvZrYaDqi3e46k4672vKtAY1F5pa4uy_8WKbZj2wR23dJLWbLtHcpcZnoF8IG98zI5FDfP8LfdBetKiVx9A5ZYF2c1i1mnshE_f8Ji5lvLsNjJkQHZ6QkJpvnmNbVE8BXfPUJ96H5WjNnRzYrFUjwDbI3rNE8fusQLBRyK27oRYsuAhsWvXSX1ievt3Z_x7qUdjfPt_eTROox9yv9UL0gPo562iE9QFnrBOQi8EpVYOGsF9CHlTQPYx5vkrXRLUWA5jxEu8PDTOG7H3TxDk79H4CioHnvUP0P468mfd2KdxLMgeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اظهارات جدید قاسمیان:   واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18138" target="_blank">📅 10:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اظهارات جدید قاسمیان:
واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18137" target="_blank">📅 10:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kts56006gXhVzhnb6Br0esXZrdUbhKDswIU0b-ELvV_QO5uqcvClFjBNnXViv6pjWqy2GAdscUwgqQplG6kEU7dcdRLriPge_EhxKZ8qeLhODaOt9FaKCccgJnBs5sMmDFNNbEXzrJmzSnHvQu7kyh6tDdxirSJrEbrEcGVPrVhSfBQO6wEbVgIhykSztsT206Fu58Wxo5PwWLtRF9RAex8zgz2NkARBbNx-w2X1C8-20dKrJqE8KWaOj6pV2ys3h1gi738U-iESVTD5eH0yIFYOUU355QcxTtPQSSM2UyxCAuYxL4koUNbWmR45fe_ly8_6d3Y8zqYEmMBve7jAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18136" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGxc-PtNLXLe8kDmJ2PGX0pJgVXHJoolwyd3tS0sqPLbYtjbZrDuQJrUGYJzSjBkg4QcqoNL5SBZJrWkg1xv6FcC9YeMUcjhB65ET6LuSyYIiL5dhFKhIZ9avNQluYTxESja5x90G4UOL4w0yEqOKc9RcqJtmetc2nSvoiY03zF1Bxnbjl2b-cpwbdcBXmHObxv_eI5vAwpGOmVx7AhZHR91vLj3aaydRSzH7NKE7ZvoIRZHpOi5t3d2oAdGA_VI6nyjE6IFYHSl9LvKWSUy-5j9mMFTJg6E4FKg5-SrOnIySR4rIXIls3etuxKanRplBKfkjxsNWM-mACGFcWtOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد دو ناو آبی‌ـ‌خاکی آمریکا، باکسر و پورتلند، در حال حرکت به سمت خاورمیانه هستند.
این دو ناو معمولا برای انتقال نیرو و عملیات آبی خاکی و ... مورد استفاده قرار می‌گیرند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18135" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18134">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فراخوان‌هایی برای اسکان مجدد در غزه پس از مصاحبه نتانیاهو
بنیامین نتانیاهو در مصاحبه‌ای با «پاتریوت‌ها»، بازگشت به اسکان یهودیان در غزه را رد نکرد، که این موضوع باعث شد قانون‌گذاران برای تبدیل این چشم‌انداز به واقعیت و اصلاح «ظلم تاریخی» جدایی سال ۲۰۰۵ فراخوان دهند.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18134" target="_blank">📅 09:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18133">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">— دو عضو سپاه پاسداران در یک حمله مسلحانه در شهرستان پاوه در غرب ایران کشته شدند و دو نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18133" target="_blank">📅 09:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18132">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46100c7aab.mp4?token=m-L1iQmMnN-oYEf_EaoCmgUsYPv82a6_HydKeXHQnbMJlWocLFaJLIbbCsDc4hSR5Yk_T323ROgNjiGzI8XxDutljMFpySoQL7ofBqX4-QUAyNAS7tooXi3yPg_XQI2csw60rQSos12KU_oCdCcwaUzLaPYnLDYdYR7HcNf7AcMVZnokv7rcvZF2DmUpe3m2U_xNKSIQR8nDGwjIwKmawMc8Iaw8z2SFWhldsNODukgN0kuFsf14V19n_cWesktEmVBRXnlA0fK8szDzxtjkNluj5ZAd6A_i7JHB3NqgpQyZ2x_FRXI7M-dLNAemKODAdginVTtMaRkm8vNzmp09Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46100c7aab.mp4?token=m-L1iQmMnN-oYEf_EaoCmgUsYPv82a6_HydKeXHQnbMJlWocLFaJLIbbCsDc4hSR5Yk_T323ROgNjiGzI8XxDutljMFpySoQL7ofBqX4-QUAyNAS7tooXi3yPg_XQI2csw60rQSos12KU_oCdCcwaUzLaPYnLDYdYR7HcNf7AcMVZnokv7rcvZF2DmUpe3m2U_xNKSIQR8nDGwjIwKmawMc8Iaw8z2SFWhldsNODukgN0kuFsf14V19n_cWesktEmVBRXnlA0fK8szDzxtjkNluj5ZAd6A_i7JHB3NqgpQyZ2x_FRXI7M-dLNAemKODAdginVTtMaRkm8vNzmp09Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد خوش چشم:
«یک چیزی از آقای حاجی زاده بگویم که احدالناسی نمیداند جز خانواده اش
که آنها هم به من نگفتند!»</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/18132" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18131">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جِی‌دی ونس درباره ایران:  یکی از چیزهایی که درباره ایرانی‌ها برایم هم جذاب است و هم ناامیدکننده، این است که آن‌ها می‌گویند «نه، نه، نه، هیچ گفت‌وگوی صلحی در جریان نیست»، اما گفت‌وگوهای فنی بین ایالات متحده و ایران درباره توافق صلح در حال انجام است.  این یک…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18131" target="_blank">📅 23:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18130">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ادای تنگ ها را درنیاورید و بگذارید رستم بخسبد</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18130" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18129">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قالیباف رئیس مجلس ایران:
تحریم‌های نفتی برداشته شده و ما نفت را ۲۰ درصد گران‌تر می‌فروشیم</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18129" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18128">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db8e4f93.mp4?token=CV8YyjIqFIE64Z85Ed2oQ65ecHq8AjTSP_V965Mk28P-tYDa2wQY_imL5LTIjSeRLBlW5mdbFjIQnUF5oRBZgJQylE4D_kmcFtph7a-30Ji2tfyA5iHj9b-m6CCHxPrHQTdG3mq9vcJPzKZNNqY4KnqUOz3CBlPfxwtkwH6CsVeRnDGUtDoYb5_eTDZz_wmUpc0BWaOLkKl4ZZh8ip7auCspFTffiitlHxJdGk91iOP6BhqwatQRnlABGDCwiZ47eqvI3cuvf4vFWISPK6lIfFl7Fo1vojEqyU5DjBqAo0n90h7d-ivGxp7-jTSs1GAKNfXNUVsJErWsrSat298RnJkZJLycL0Pg-8T2DYkIu3ghwx90ZU0r2w5laloVJtK7_h7DFtzXt7BmD9m9IKxQ14iZ2texKjstkWK57xe3VwWVeRcj0Fyr32bAdD0bvFQwYX-7RwtjcXPJYjJYoNaS2oJcqlX9HA6ClbuQieYMEBcqK5fwLp-hmbgRoxHSWDBres0cTpnaGD6uOT5762MbIusJqSa9h8aKT9vuRI3UE9PrnzVudP-NHuwLjzzr1XraZ1yHCGZcuo8zEZI5PLjFA_SVFF7Pt3dOtwR6YJqvad8Zbp7fCspb_VRv58M31XNyN5SKhy0ZdE1JUTOolHtmd1zx0KYNPu22NX1OOXhcVXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db8e4f93.mp4?token=CV8YyjIqFIE64Z85Ed2oQ65ecHq8AjTSP_V965Mk28P-tYDa2wQY_imL5LTIjSeRLBlW5mdbFjIQnUF5oRBZgJQylE4D_kmcFtph7a-30Ji2tfyA5iHj9b-m6CCHxPrHQTdG3mq9vcJPzKZNNqY4KnqUOz3CBlPfxwtkwH6CsVeRnDGUtDoYb5_eTDZz_wmUpc0BWaOLkKl4ZZh8ip7auCspFTffiitlHxJdGk91iOP6BhqwatQRnlABGDCwiZ47eqvI3cuvf4vFWISPK6lIfFl7Fo1vojEqyU5DjBqAo0n90h7d-ivGxp7-jTSs1GAKNfXNUVsJErWsrSat298RnJkZJLycL0Pg-8T2DYkIu3ghwx90ZU0r2w5laloVJtK7_h7DFtzXt7BmD9m9IKxQ14iZ2texKjstkWK57xe3VwWVeRcj0Fyr32bAdD0bvFQwYX-7RwtjcXPJYjJYoNaS2oJcqlX9HA6ClbuQieYMEBcqK5fwLp-hmbgRoxHSWDBres0cTpnaGD6uOT5762MbIusJqSa9h8aKT9vuRI3UE9PrnzVudP-NHuwLjzzr1XraZ1yHCGZcuo8zEZI5PLjFA_SVFF7Pt3dOtwR6YJqvad8Zbp7fCspb_VRv58M31XNyN5SKhy0ZdE1JUTOolHtmd1zx0KYNPu22NX1OOXhcVXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیریت Secret Box حدود ۲ سال پیش این ایده را مطرح کرد که این روانی عوضی را در قالب یک معامله بکشند که هم برای ایران خوب بود و هم برای اسراییل و اتفاقا ۴ ماه بعد این فراخوان لبیک گفته شد اما سوگمندانه ناموفق بود!  مردک حمال یک دیوانه کامل است و می‌توان او را…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18128" target="_blank">📅 20:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18127">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وال استریت ژورنال:
اولویت‌های متضاد ایران مذاکرات صلح آمریکا را به خطر می‌اندازد</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18127" target="_blank">📅 20:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18126">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نتانیاهو رفته از جنوب لبنان بازدید کرده!
از این جهت خیلی شبیه احمدی نژاد است؛
منتهی احمدی نژاد سفرهای استانی اش به شهرهای ایران بود اما نتانیاهو عمدتاً به مناطق تصرف شده کشورهای دیگر سفر می کند (غزه، سوریه، لبنان....)</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18126" target="_blank">📅 18:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18125">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسپوتینک:  اختلاف با عربستان، جنگ ایران و تله هرمز عواملی که ممکن است امارات متحده عربی را به سمت خروج از اوپک سوق داده باشد  دکتر ممدوح جی. سلامه، اقتصاددان پیشکسوت نفت، به اسپوتنیک گفت: «مدت‌ها قبل از جنگ ایران، امارات متحده عربی به دلیل اختلاف با عربستان…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18125" target="_blank">📅 18:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18124">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بقائی:  ما هیچ برنامه‌ای برای دیدار با طرف آمریکایی در هیچ سطحی طی روزهای آینده نداشتیم، بنابراین چیزی برای لغو کردن وجود ندارد.  آنچه احتمالاً فردا در دوحه برگزار می‌شود، گفت‌وگو درباره اجرای بندهای یادداشت تفاهم، از جمله بند مربوط به آزادسازی دارایی‌های…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18124" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18123">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بقائی:
ما هیچ برنامه‌ای برای دیدار با طرف آمریکایی در هیچ سطحی طی روزهای آینده نداشتیم، بنابراین چیزی برای لغو کردن وجود ندارد.
آنچه احتمالاً فردا در دوحه برگزار می‌شود، گفت‌وگو درباره اجرای بندهای یادداشت تفاهم، از جمله بند مربوط به آزادسازی دارایی‌های مسدودشده ایران با طرف‌های قطری است.
بنابراین تأکید می‌کنم که هیچ دیداری با طرف آمریکایی در هیچ سطحی برای روزهای آینده برنامه‌ریزی نشده است
تمامی مقدمات لازم فراهم شده و امیدواریم این روند به‌درستی پیش برود و به نتیجه‌ای رضایت‌بخش برسد
رقص و ابراز شادی مقام‌های آمریکایی از صعود نکردن ایران به مرحله بعد جام جهانی، با همه معیارها و اصول پذیرفته‌شده میزبانی مغایرت دارد
هیچ درخواست رسمی درباره بازگشایی سفارت کانادا دریافت نکرده‌ایم در صورت دریافت درخواست، آن را بررسی خواهیم کرد، اما تاکنون هیچ درخواستی به دست ما نرسیده است.
﻿</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18123" target="_blank">📅 16:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18122">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFJks4ARCtIQczWXJv1PMH6e6dcdk4s95TnZHh_8c2YFZFS4gRW4Lj2p0iCbVxW3r2d-MWIuoWDh58svQxBWZ2wZwneD35yQSjwtC7AKRQPK_IYKRPAcTsO_04H8veA1hbQQfuIbs99PBD_DXgWtJmYxzhyTyo323WYwE0OfkTJqHfibU9kotoO3oFZGo5wlqsLE3qmRLNr64a4ve60T5kV7fsbusGtZvaX9oETVdana2RGH5bVO5BFZV0ZuTS5jifJClMA7rQaaItbS5QREwpjTUNkEH9EZ2O0d_mA8197ToSFQnWt5aUC7NKmU5mfPLPfAyNE5rM0KwCFQTwkyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر می‌گوید فرستادگان آمریکا، استیو ویتکاف و جرد کوشنر، در دوحه حضور دارند اما با مقامات ایرانی به طور مستقیم گفتگو نخواهند کرد و به جای آن با میانجی‌ها دیدار می‌کنند تا درباره پیشرفت مذاکرات بحث کنند.  سخنگوی وزارت خارجه قطر گفت ۶ میلیارد دلار دارایی‌های…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18122" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قطر می‌گوید فرستادگان آمریکا، استیو ویتکاف و جرد کوشنر، در دوحه حضور دارند اما با مقامات ایرانی به طور مستقیم گفتگو نخواهند کرد و به جای آن با میانجی‌ها دیدار می‌کنند تا درباره پیشرفت مذاکرات بحث کنند.
سخنگوی وزارت خارجه قطر گفت ۶ میلیارد دلار دارایی‌های مسدود شده ایران هنوز منتقل نشده است و آزادسازی آن‌ها به پیشرفت در مذاکرات بستگی دارد.
او همچنین گفت یک خط تماس کاهش تنش به کنترل تبادل‌های هفته گذشته بین آمریکا و ایران کمک کرده و قطر با عمان هماهنگ می‌کند تا عبور ایمن از تنگه هرمز را تضمین کند، که آن را به عنوان اولویت اصلی توصیف کرد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18121" target="_blank">📅 14:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دونالد ترامپ، کمونیسم را بزرگ‌ترین تهدید در تاریخ ایالات متحده توصیف کرد — بزرگ‌تر از دو جنگ جهانی، حملات ۱۱ سپتامبر ۲۰۰۱ و حمله ژاپن به پرل هاربر.  در این بیانیه، او از اصطلاح "دموکراسی اجتماعی" به عنوان یک واژه پوششی برای کمونیسم استفاده کرد. به نظر می‌رسد…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18120" target="_blank">📅 14:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVn-yTbhI6d4DJcfy5OGQROovWLT0zAQ5nu1f7hUORTgVMAvSmIUOohSjsCjNDAAPSZ0wzoNyvSQEYQ0SjvE9o32p-81rjSZnbxKjPjga6YSAc8Sj6HJCXcp9m6NeO1DPZVfhngznge4_avdETvatqIvo3hOd9UubZLc3MeuSIma_zWkb1wrjGYxsON3MP4FAtc-6OvOXYfROEQsAVzcroCnF94EykNLK1rvMnwVYMQIJhylERj5GbS_s2h4hYDkS1nIQ7vPvmn7WdtfTRDXrcoPl5nYNNP6atYvfAoWhe4TbYpBwQ7V5Ee41betOQ97oDORzRS9RhAsTczuj5_qMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، کمونیسم را بزرگ‌ترین تهدید در تاریخ ایالات متحده توصیف کرد — بزرگ‌تر از دو جنگ جهانی، حملات ۱۱ سپتامبر ۲۰۰۱ و حمله ژاپن به پرل هاربر.
در این بیانیه، او از اصطلاح
"دموکراسی اجتماعی"
به عنوان یک واژه پوششی برای کمونیسم استفاده کرد. به نظر می‌رسد این اظهار نظر علیه جریان‌های سیاسی داخل ایالات متحده هدایت شده است.
طبقه‌بندی کمونیسم به عنوان یک تهدید وجودی، حتی از خطرات کلاسیک امنیت ملی در فرهنگ حافظه آمریکایی نیز فراتر می‌رود.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18119" target="_blank">📅 14:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18118" target="_blank">📅 13:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCBwxSYlHUEx8N0ru395lZUgoUC3AwB3kFdviIXmVp0BvpnbpXCdPdiqzMb29RODLHRJUTMLmUYwF84-9ZvSxB3RscAtuaNFuIxwsesOZ9wJXxCzH3aZnd9La0qGYM9e78By3pLTR8tccycb_2KqFKAYNyApRygeqbd31mwvacAbzL_ICd-QADBQh1YDgsdCYzF32RMGMNRBOrTosJhRm5hujCpQGMmCpo89zLsLZGCg4WZBTIvDbQu9Ohwr5HmVGl_cxcKRSgpA4GVllRaZkUIyF0ADnyR4nX1xZcZ1G6zw665du06H3s9A4OaaJFS_X8ROH6-jYcSmIYNKFsgzwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18117" target="_blank">📅 13:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
قنبری ؛ سخنران صداوسیما : ترامپ جنایتکار باید ترور شود تا رهبران ما بتوانند از مخفیگاه خارج شوند که اگر چنین نشود آنها باید تا ابد در مخفیگاه بمانند</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18116" target="_blank">📅 13:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حملات سایبری ایران به اسرائیل از سال ۲۰۲۵ سه برابر شده است  یک مقام ارشد امنیتی اسرائیل روز دوشنبه گفت که حملات سایبری ایران که تل‌آویو را هدف قرار داده‌اند، از آغاز جنگ آمریکا و اسرائیل علیه ایران در اوایل امسال به طور قابل توجهی افزایش یافته است.  یوسی کارادی،…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18115" target="_blank">📅 12:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18114">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حملات سایبری ایران به اسرائیل از سال ۲۰۲۵ سه برابر شده است
یک مقام ارشد امنیتی اسرائیل روز دوشنبه گفت که حملات سایبری ایران که تل‌آویو را هدف قرار داده‌اند، از آغاز جنگ آمریکا و اسرائیل علیه ایران در اوایل امسال به طور قابل توجهی افزایش یافته است.
یوسی کارادی، مدیرکل اداره ملی سایبری اسرائیل، به روزنامه آلمانی
دی ولت
گفت که مقامات اسرائیلی در ژوئن ۲۰۲۵ حدود ۱۶۰۰ حادثه سایبری خصمانه را در جریان جنگ علیه ایران ثبت کرده‌اند.
به گفته کارادی، این رقم به طور چشمگیری به حدود ۴۸۰۰ حادثه در ژوئن ۲۰۲۶ افزایش یافته است.
کارادی گفت: «برخی گروه‌ها بسیار ماهر هستند.ما می‌توانیم با آنها مقابله کنیم، اما باید آنها را جدی بگیریم. برخلاف حوزه فیزیکی، در فضای سایبری آتش‌بس وجود ندارد.»
کارادی اظهار داشت که حملات طیف گسترده‌ای از نهادها را هدف قرار داده است، از جمله سیستم‌های زیرساخت حیاتی، سازمان‌های بزرگ، کسب‌وکارهای کوچک و متوسط و شهروندان خصوصی. در میان اهداف کوچک‌تر، شرکت‌های حقوقی و دفاتر حسابداری نیز بودند.
او گفت: «تا کنون — و امیدواریم که اینگونه باقی بماند — ما موفق شده‌ایم حملات به زیرساخت‌های حیاتی را دفع کنیم.»</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18114" target="_blank">📅 12:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سردار محمد اکبرزاده، معاون سیاسی در دفتر نماینده رهبر ایران در نیروی دریایی سپاه، در یک تصادف رانندگی در استان کرمان کشته شد.
اکبرزاده یکی از معماران کلیدی استراتژی ایران در تنگه هرمز محسوب می‌شد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18113" target="_blank">📅 09:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">— دو عضو سپاه پاسداران در یک حمله مسلحانه در شهرستان پاوه در غرب ایران کشته شدند و دو نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18112" target="_blank">📅 08:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">غریب‌آبادی :   اگر عمان به هر طریقی تمایلی به ایجاد یک رژیم مشترک برای آینده تنگه هرمز نداشته باشد، جمهوری اسلامی ایران این امر را به تنهایی پیش خواهد برد</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18111" target="_blank">📅 23:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">معاون وزیر خارجه ایران غریب آبادی:   ایران تلاش خواهد کرد تا عبور هرگونه کشتی‌ای که از مسیرهای غیرتعیین‌شده توسط تهران در تنگه هرمز عبور می‌کند، را مختل کند</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18110" target="_blank">📅 23:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دکتر محمود سریع‌القلم:  دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.  مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.  اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18109" target="_blank">📅 23:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دکتر محمود سریع‌القلم:
دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18108" target="_blank">📅 23:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4HqmitEhaDu7eD2mPpoIEpMr13MbXcnN47LiHXkB2cMatiz2pb7aPoxWHurD8DjTuwdSVtQxgcGTC11ICPFklaGMyy3CZTdt2W0nCCZEQ23e6nz13X1ciVYWYxigqYMhpesNfEbNLIZobfzyjOXc6_3MY84p045UQD_Dh1tT_szkAdgh3Yw10unj6GW4Ea6K8K1gbk3jK0s0gP8P5ZbI44ES8WDAJrCuIq6Ry7N9RGg2hTQfTwJhuPAAjseCPDPcJ01FL1DVWjQJax9eHgXSXuCamdNWMouoR-lIqeXKBc6Qgf0sKJ8oUkNclemixS-zjLFxwR8S3L5VM078LxlXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18107" target="_blank">📅 21:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">معاون وزیر خارجه ایران غریب آبادی:
ایران تلاش خواهد کرد تا عبور هرگونه کشتی‌ای که از مسیرهای غیرتعیین‌شده توسط تهران در تنگه هرمز عبور می‌کند، را مختل کند</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18106" target="_blank">📅 21:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مکارم شیرازی در دیدار با پزشکیان:
اگر بدخواهان مانع‌تراشی نکنند، توافقات اخیر می‌تواند آثار مثبتی برای کشور داشته باشد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18105" target="_blank">📅 20:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPvxobj8nciuCx3761KSsopXMpqe8tM94ZCSNMSSrHek_WTzjKgx6u72Q0hWYwk9zrGsQca93kvYwwJH_DgW0DUNG89MZjuZcZ2RP70ujmLLRqOCfwP4vrZiLZbX_tua9_Knl_LB-IplI1A18OEAVa_-WkeI8xAcodwxUjxiIyv_N44Dj39ut2fCFsoEVPfCgEdlHMjOCvJi9aI-jq81-Ks4qVHYmBrppN1irew8577VmJHBrXOc0QxV_FSucvoPrvsTttmoTnNe9YsNDER2jMKbmFq-ae7GEv5jSwbjyku3lSkCxoS9YGqac_Kz4b2ydAAsAea_kBUKhU6779vJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18104" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18103">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایران می‌گوید برنامه‌ای برای گفت‌وگوهای مستقیم با ایالات متحده در این هفته وجود ندارد، با وجود ادعاهای مقامات آمریکایی.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18103" target="_blank">📅 19:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18102">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18102" target="_blank">📅 19:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18101">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18101" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:
«من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18100" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18099" target="_blank">📅 19:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:
— حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران
— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی
— توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله
— آماده شدن نیروهای مخالف حوثی ها در یمن برای حمله به انصارالله</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18098" target="_blank">📅 19:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18097">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18097" target="_blank">📅 18:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ادای تنگ ها را درنیاورید و بگذارید رستم بخسبد</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18096" target="_blank">📅 18:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18095" target="_blank">📅 18:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18094">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18094" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18093">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رستم را به زابلستان بازگردانید!  ترامپ گفت ایران درخواست دیدار حضوری در دوحه داده است!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18093" target="_blank">📅 17:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18092">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMvABmALSsOgnlbtczRwfboxTVKHsbq197IYVtdcBcZHrQZ3IMj_fzpWUjYjVUmDAidfb18HLRakRcDr3J_ZuEbMcxcVyvglAo2MmbJof_tHDaeMd6IhO1FELv1pWcgeQ38rVf3RUEuOLAriTkLzQ3wHmHtxVeBbkrqowxC4QkzQf2QKXlK3a9_9C5D7Cbr9GUhnWJ655Xl0slMJc2dnG5UZOKboJCSQhqTYXzn7rQ59bdFbYQes1RcGtY3GvyCGXvRUgFQQSRamHIVJ8BtNFLn9Aqktf01naJoHCBNlBZ4eSk1IVGRnSlog_2b5y5WfP8s-EXMxECCGmKb8SDnY3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طنز بانکداری ایران  به دلیل حملات سایبری به دیتابیس بانک مرکزی شما به پولتان دسترسی ندارید ،اما بانک بابت اقساط به پول شما دسترسی دارد.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18092" target="_blank">📅 15:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18091">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp0ubg9dMC9vZjVR8vlru4tMVqtLK0t7XDyVU8XGc3friDbajIQ3YwAPLr5rju3uvaQokfjaKG7mh5lvHqRldBP-Z0qZf9a3srlB7GKrO1x5cGU8uCFir8krB6zbcychd8EK7gPSODk_fabvvEgOxorn_sQ9JUog8GYB4BmLmsyk52LaTd8qri2z2OYa_VUtZ5Uc7ceKhGTBUnurdxvzjo25aLNORl5ia43_gMJk32pwImkPMqCmsL1SYKa5fLvbrkFWQcyqKL8dgikLs0gxKc1JkkL0DrjEI8w-UVc49ZrNFyQLi9zI0RjOOg_LmBBQIVQKx1SlvimHIRimWOcZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینطور که بویش می آید بایستی بزودی رستم تهمتن را دوباره فراخوان کنیم.  فقط فکر کنم عینکی شده باشد که ولی خب.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18091" target="_blank">📅 15:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18090">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ایران: هیچ گفتگوی فنی با آمریکا برای این هفته برنامه‌ریزی نشده است - تسنیم</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18090" target="_blank">📅 14:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18089">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4Q5sEE8m3NVjFEYuTx_L5LOG3w8AXbn-1R2mZT14TZ524gAe_uux03-I5qm67EjHCyleVSgpCRow5wUAXGcm-i2afwEu65NWM4G8dJTFuDsSRU-Ih0sohXvEpEiIV196N4RY6OUzg7PSvYbHDCg2KHT5MwHvGrMlSbeytxbrhFhXZWp5HJ8EADrfZwPWHhAIMCvs2jalDUOQ2QSCkWRpXfjs3ohjYOq-5yT7NE55UCo4H6j_7b05bnNYGOUaXmKiXbcGGzyBMkmAgXbYnuMpjKxgTyrHSnRh0r3BeqpCOZvZ-VU1I8KlpmrOHt6oHV4P72hPloBwt2jp78gdDr0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت اسرائیل پهپاد به شهرک نشینان در کرانه باختری اشغالی ارائه می‌دهد!
منابع محلی می‌گویند که پهپادها برای پرواز در ارتفاع پایین بر روی چوپانان و کشاورزان فلسطینی استفاده می‌شوند تا دام‌ها را پراکنده کنند، فلسطینی ها را بترسانند و اطلاعات جمع‌آوری کنند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18089" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18088">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ایران: هیچ گفتگوی فنی با آمریکا برای این هفته برنامه‌ریزی نشده است - تسنیم</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18088" target="_blank">📅 13:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18087">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الهام فعلا استراتژی مالش را آغاز کرده تا مثلا خود را در دل آمریکایی‌ها جا کند، غافل از اینکه ارمنستان با چرخشی عظیم به سوی غرب، در دلبری از واشنگتن و تل آویو ، گوی سبقت از باکو خواهدربود.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18087" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18086">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هیچ حمله سایبری در کار نیست.  MV = PQ  وقتی M را با چاپ پول برده ای بالا و از آن سو Q هم اگر افتی نکرده باشد دستکم رشدی هم نکرده، قیمت ها یعنی P باید منفجر بشود. پس تنها راهی که داری این است که از سرعت گردش پول یعنی V بکاهی و آن را بندازی گردن اسراییل و نت…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18086" target="_blank">📅 11:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18085">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN61QpENz7evXU9pTJ-uEIOGXX2vrO57jRJnCg5h_tr0BUMrqnUvNR9uyrgDbji3iFmre-3x7YN0buNYvf02AzN7oaVnN4kwHOkhLnK-drBIinbGL0DB4JuLGYHzk1SnRh8buUik63LtPfX-pAvb5K5l8K6_G08PxBfRLr3sggufay2tDJKio1NhFYP8QrmY4LzuLg7KPvp_ezVQn5rfT8a9g5zPClVeE_Wvr9WcPNRzPCcHgyhcdMZ6kF7jIVWA7FbUv1b1PbEsx3RpYiPJyEP57vGI5kVPZ4DU22s9kyeKCIf8_gnMFKEVyyulZPUtWLs2sFWUtSNBIgee1ULZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا رقابت هوش مصنوعی میان آمریکا و چین این‌قدر سروصدا کرده است؟
رقابت هوش مصنوعی آمریکا و چین فقط رقابت فناوری نیست؛ هم‌زمان رقابت بر سر ارزش بازار، سودآوری، امنیت ملی و برتری ژئوپولیتیکی است و هر جهش جدید می‌تواند انتظارات سرمایه‌گذاران و موازنه قدرت جهانی را تغییر دهد.
مدل‌های ارزان و باز چینی در کنار جنگ تراشه و محدودیت‌های صادراتی آمریکا، معادله اقتصادی هوش مصنوعی را تغییر داده‌اند و ابهام درباره فاصله واقعی دو طرف، به مهم‌ترین سوخت این هیاهوی جهانی تبدیل شده است.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18085" target="_blank">📅 11:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18084">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pySKgZvBxjCSU80aE8qx3Wd8NuLJ2eEnS3Jul_R8UEvv1wv3dB5l02bfWRv2xMlRbJk2RS9fY9w9mlG8IsyNu5hYwxZf33uo5_ZslmDYqhvgfc-3Db81wa9vqnTKTopWrvjEBHFaJtNVlxYCZFrsX9earer9exH7114pFPVbiXWJ9Z7mu9uKbG6k9ixVRMmJij2kkQ_nolSZhib0if56CIaShGWGVq00hymvX4iQ0W7h2QRPuFDIqnBucRNF18JtpAT3Rt879_dzDOx1MZe3WpebyGfYbm7ywQpykhSQb7eRHFMkOXcuVk4nQDxnZFP7WL4SeVsEOZcLXmoRRsk_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عبور کشتی‌ها از تنگه هرمز به طور قابل توجهی با ترافیک سال گذشته متفاوت است.
پورت‌واچ آمار جدیدی درباره ترافیک کشتی‌رانی در تنگه هرمز منتشر کرده است. در ژوئن ۲۰۲۶، ۵۰ نفتکش و ۴۰ کانتینر عبور کردند در حالی که در دسامبر ۲۰۲۵، ۱۱۵۰ نفتکش و ۴۰۰ کانتینر ثبت شده بود.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18084" target="_blank">📅 01:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18083">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حمله سنگین اسرائیل به منطقه "مجدل زون" تو جنوب لبنان</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18083" target="_blank">📅 01:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18082">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آکسیوس با استناد به مقامات آمریکایی  ایالات متحده و ایران توافق کردند حملات را متوقف کنند و گفتگوها را در این هفته برنامه‌ریزی کنند</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18082" target="_blank">📅 00:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18081">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترور یک عنصر ازبک در سوریه  بنا بر گزارش منابع محلی یک عنصر ازبک با نام خالد الجزراوی روز گذشته روبه‌روی منزلش در الفوعه در حومه‌ی ادلب توسط افراد ناشناس ترور شد.  برخی منابع محلی این ترور را به داعش منتسب کردند، این در حالی‌است که داعش هنوز مسئولیت انجام…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18081" target="_blank">📅 00:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18080">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترور یک عنصر ازبک در سوریه
بنا بر گزارش منابع محلی یک عنصر ازبک با نام خالد الجزراوی روز گذشته روبه‌روی منزلش در الفوعه در حومه‌ی ادلب توسط افراد ناشناس ترور شد.
برخی منابع محلی این ترور را به داعش منتسب کردند، این در حالی‌است که داعش هنوز مسئولیت انجام این ترور را بر عهده نگرفته‌است
چندی پیش یک عنصر چچن با نام مصطفی الروسی از اعضای نیروی ویژه تحریر الشام موسوم به العصائب الحمراء نیز ترور شده‌بود.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18080" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18079">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18079" target="_blank">📅 00:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18078">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آکسیوس با استناد به مقامات آمریکایی
ایالات متحده و ایران توافق کردند حملات را متوقف کنند و گفتگوها را در این هفته برنامه‌ریزی کنند</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18078" target="_blank">📅 00:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر علوم و فناوری  اسراییل، گیلا گملیئل:   وقتی که از رژیم ایران عبور کنیم، نوبت به جاه‌طلبی‌های امپراتوری عثمانی می‌رسد که به دنبال گسترش و نفوذ خود است. شکی نیست که ترکیه با آرزوهای گسترش فراتر از مرزهای خود و رهبری منطقه بر اساس دیدگاه خود، تهدید واقعی…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18077" target="_blank">📅 19:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18076">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcTGZwK2olB-hEN8G-gGjD4KXCsw4MJmVKJkuVCZR7WmDQ11Af3iwUrr-2g-L-fboAl9z2ZcGPfQ5xI1BChnZsaGCaWqyvreFphbyOvp9bOxf0u2tXhtBWJQx5l3GkCTAoBcsA4RqgyNCKuFlux5cbToSpn9v58Zj0g2LTuwlsIeiRsfw7XKLnq1Nyb-kzA9lKsGTHaSWv2-gioEkq4Dmi2GAwKJdUynj_6NbsFeS_qsm5zt3EKOUr80Gggk2-FSP_IxnjPa2arsVAcow6Vx6yeWWJaTFSvCaIelm8xBftxv0JNK5U44JjKpf141MM_NYEgRZKNfpSEobQYoIARJDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا شاخص سهام کره جنوبی در روزهای اخیر ریخت؟
ریزش اخیر کاسپی بیشتر از اینکه نشانه ضعف اقتصاد کره باشد، نتیجه هم‌زمان فشار روی سهام نیمه‌رسانا، نگرانی از تداوم نرخ‌های بالای آمریکا و خروج سرمایه از بازار بود؛ بازاری که وابستگی زیادی به سامسونگ و SK Hynix دارد.
با وجود شدت افت، کاسپی هنوز فاصله زیادی با سناریوی «ترکیدن حباب» دارد و سؤال اصلی بازار این است: آیا چرخه رشد نیمه‌رساناها ادامه پیدا می‌کند یا قیمت‌گذاری این صنعت زودتر از انتظار به سقف رسیده است؟
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18076" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18075">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هندی ها جوری هستند که یکی شان میخواسته از بانک پولی بگیرد به او گفته اند برو گواهی فوت خانمت بیاور و نداشته؛ رفته جنازه زنش را از قبر کشیده بیرون کول کرده برده بانک که پولش را بگیرد!  حالا شما فکر کنید بین شمال تنگه که پولی است با جنوب تنگه که صلواتی است کدام…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18075" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18074">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن، می‌گوید دولت جدید اسلوونی به رسمیت شناختن فلسطین را لغو کرده و سفارت خود را به اورشلیم منتقل خواهد کرد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18074" target="_blank">📅 14:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18073">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بحرین می‌گوید حمله ایران به ساختمان مسکونی آسیب زده است، تلفات جانی نداشته است</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18073" target="_blank">📅 14:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18072">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b2ebb26.mp4?token=vzFlKurR5ccwSLCrk8c08iqDNtTF8lEfmAa7buluP8AEanUULr_NeNi3EUQ4laJSI_4IqEHkqEoFJBZjoFDyMLszSWZArA6SCj53zrckEbAIBjiVWyIAhMh_cr251UeGdmRTiE88EeUf216aTej0-yKzKcrGzXde4DJeYYGeUN_mvr-nzEUNX7Bctc0OxzLxNRWToaKUxFsMAm8D-iuSDdHodwPF6Ei0wquAneXz2iNJECug2t_Sx4wB8E_nvV77bDSP4XIIRw4sGP4o7GedkQUaJbz6NZxcWGYfbh1MLFJ6Za5Nk0WdkpgbKIkbwQkJOPi625Dujm8WDfmuOpmD_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b2ebb26.mp4?token=vzFlKurR5ccwSLCrk8c08iqDNtTF8lEfmAa7buluP8AEanUULr_NeNi3EUQ4laJSI_4IqEHkqEoFJBZjoFDyMLszSWZArA6SCj53zrckEbAIBjiVWyIAhMh_cr251UeGdmRTiE88EeUf216aTej0-yKzKcrGzXde4DJeYYGeUN_mvr-nzEUNX7Bctc0OxzLxNRWToaKUxFsMAm8D-iuSDdHodwPF6Ei0wquAneXz2iNJECug2t_Sx4wB8E_nvV77bDSP4XIIRw4sGP4o7GedkQUaJbz6NZxcWGYfbh1MLFJ6Za5Nk0WdkpgbKIkbwQkJOPi625Dujm8WDfmuOpmD_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی نجاسات الجزایری پس از خوردن گل تساوی تیمشان از اتریش که باعث شد تا در مرحله حذفی به اسپانیا نخورند!
بعد پروفسور جمشید خیابانی به عربی از این نکبتها درخواست بازی شرافتمندانه داشت!
حق شما همان گیوتین فرانسوی بود و بس!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18072" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18071">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18071" target="_blank">📅 10:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18070">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18070" target="_blank">📅 08:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=tX-vNb2WBEELjiM9f6u8HBLpim9l2hbqBQZvhDXb05vQU4poSmkQfk_4-1YZqMY14aPy0R4-ub-8barVykeLrjINjDLVIK93lJkjwqm9uaZGklXigz_neKb2zCkR9lxcXTIm39vc8YazVA3n2aqUz2YNAsCz1ZtIFfTIuWW4Jq8lXzXYxiu9_Np5TQwvQiFl6NWC5-TlrKTUrW_8TRD6_vyx6cq7L5Yvlnc1yelr1VE6Z7T5PUsjvVL7n22DC4r2Ahxpj8q4Vk6a9RMUSU2OUFd5eJDIhrbox-zdmGyZrn94fa_1ZhqUNLBuMBfg1aadPkp6tjwjYiJEvfft4AMX5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=tX-vNb2WBEELjiM9f6u8HBLpim9l2hbqBQZvhDXb05vQU4poSmkQfk_4-1YZqMY14aPy0R4-ub-8barVykeLrjINjDLVIK93lJkjwqm9uaZGklXigz_neKb2zCkR9lxcXTIm39vc8YazVA3n2aqUz2YNAsCz1ZtIFfTIuWW4Jq8lXzXYxiu9_Np5TQwvQiFl6NWC5-TlrKTUrW_8TRD6_vyx6cq7L5Yvlnc1yelr1VE6Z7T5PUsjvVL7n22DC4r2Ahxpj8q4Vk6a9RMUSU2OUFd5eJDIhrbox-zdmGyZrn94fa_1ZhqUNLBuMBfg1aadPkp6tjwjYiJEvfft4AMX5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/18069" target="_blank">📅 08:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارشگر صداوسیما یک دقیقه قبل از حذف ایران از جام جهانی:
یک کشور مسلمان، کاری کرد تا کشور مسلمان دیگری صعود کند!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18068" target="_blank">📅 08:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شبکه ۳ بعد فوتبال یک روحانی  را آورده او هم آفتابه را گرفته روی همتی که چرا گفتی از دشمن گندم وارد کنیم مگر گندم تراریخته نشنیدی!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18067" target="_blank">📅 07:53 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

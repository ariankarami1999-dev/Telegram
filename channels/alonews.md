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
<img src="https://cdn4.telesco.pe/file/V06Vx_Ph5BJQfpTsFpQ0v7ibQsHa9vyUH3fIz-peco3MCJtmg48yka9YWNBke_-xPIK520J9ni9vJr_Fn2TCPS-udygPuRmnYg0s3RhI3WH8SWny_FXHWfXbX3dHugoutq4rIPR5OsvnU-xg9YgZFFGtu2wTZ6oFDM3Yk95Ip7MWRoATknTysgzzQKPq67NVpdyIrxlsF9_yN7bZ04etDVjTucwjzaPgDY9gk9i-772r-9j1nsLYsjxgpEQDYPiuz_YccWpXIerayTMXUAqpayIFAG3pwMdn0UBSCbfmsQ04MbhxWCh6ycomDaBdYRHg7kTC19vzuGye5fCbPzMsJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-148925">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
افزایش میلیادری قیمت ۴ محصول ایران‌خودرو
🔴
قیمت ۴ محصول ایران‌خودرو امروز حداقل ۷۸۰ میلیون افزایش یافت؛ میزان افزایش قیمت هایما 7X به بیش‌از یک میلیارد و ۲۰۰ میلیون تومان رسیده است.
🔴
این افزایش قیمت خودرو درحالی اعلام شده که پیش‌از این ایران‌خودرو توقف تولید محصولات خانوادهٔ هایما را اعلام کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 21 · <a href="https://t.me/alonews/148925" target="_blank">📅 13:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148924">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آکسیوس: شورای صلح به ریاست ترامپ طرح بازسازی غزه را به ارزش ۲.۴۵ میلیارد دلار اعلام می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/148924" target="_blank">📅 13:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148923">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hitsj-UQcuOMd39vWOJmiqKVzrNxdAp5e2K6MFDxQlNvf1OZLegXVgXFCJMO_BVi2roNiEFC0k3mNqt4CEIzJu15NaK6On1v4srsq6JdT7NnQ8fBrBOF3gp0zgVXvC_6b3LdR9_gWds5Oq3vdJ6WEVxzihBymw3B0SJKYOHpIQgWEeN0xHfz1PThNIMCkY8q-qh5o0T2xF9zQJEcV6j1RUWjMijZbTD_vsdEzVKZckNgAlZJvTjy1Wiy0s5HQlMkkxbmVXuy7S-0DbGg391_978sqpmjAQc3F0f-95AP0y9M0jhbaHMm7HraYUYXjaufGC_PIn5fP-PuUJbquK5J-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون‌نویس بلومبرگ: عربستان سعودی بارگیری نفت خام در پایانه ینبع جنوبی در دریای سرخ، یکی از مراکز مهم صادرات نفت این کشور، را از سر گرفته است.
🔴
تصاویر ماهواره‌ای مورد استناد مربوط به ۲۱ سپتامبر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/148923" target="_blank">📅 13:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148922">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
فایننشال تایمز: برای نخستین بار، هزینه اجاره یک نفتکش غول‌ پیکر در مسیرهای میان خاورمیانه و آسیا، از روزانه ۱.۲ میلیون دلار فراتر رفته
🔴
حدود ۱۵ درصد از ناوگان جهانی نفتکش‌ها در سواحل عمان منتظر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/148922" target="_blank">📅 13:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148921">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کرملین: «ولادیمیر پوتین آماده دیدار با دونالد ترامپ است، اما برگزاری یک نشست بدون انجام هماهنگی و آماده‌سازی‌های قبلی، اتلاف وقت خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/148921" target="_blank">📅 13:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
هک گسترده اف‌بی‌آی!
🔴
یک گروه هکری با نفوذ به سامانه‌های اداره تحقیقات فدرال آمریکا (FBI)، اطلاعات شخصی هزاران مأمور این نهاد را به دست آورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148920" target="_blank">📅 13:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه
:
«اگر سوریه به مرحله‌ای از ثبات و امنیت برسد، از فعالیت سیاسی کناره‌گیری خواهم کرد، در انتخابات ریاست‌جمهوری آینده نامزد نخواهم شد و قدرت را واگذار خواهم کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148919" target="_blank">📅 13:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148918">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
فرودگاه بین‌المللی نجف: پروازهای ورودی و خروجی این فرودگاه، از جمله پروازهای ایران، طبق برنامه‌های اعلام‌شده ادامه دارد و تاکنون دستوری برای توقف آن‌ها صادر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/148918" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148917">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
جنگنده‌های عربستان سعودی مجموعه‌ای از حملات هوایی را علیه دکل‌های مخابراتی در استان الحدیده یمن انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/148917" target="_blank">📅 12:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148916">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: رهبران قطر با ترامپ در مورد پیامد‌های جنگ با ایران گفت‌و‌گو کردند
🔴
خوشحال هستیم که شاهد از سرگیری تعامل میان تهران و ایران هستیم
🔴
تمرکز بر باز نگه داشتن کانال‌های ارتباطی و ادامه تبادل پیام‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/148916" target="_blank">📅 12:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148915">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
معاون اول پزشکیان : از مردم بابت گرونی‌ها عذر می‌خوام ؛اما در حال حاضر. راهکاری برای حلش وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/148915" target="_blank">📅 12:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148914">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMr3L3rRiW5pr3ROWrj3DVN3xhgCJE0HvQPiyXMAULJ4YiMo2UI4jhI66XXj9FUZvD6ssy_gQb0BMb3LcnIv2q-o_HeXEzeugEKiSjuNI9JaGTtGuW4MWujjrCabR32ikz_Hieb4C7gIxRGViWJ-iqUwskbFb0ht9ZkHMEosag7LisfjnoBKiwZyB1hsmf1wCpcHImn7oBHlC7RAC4fDtZFB7OOlTlaHZq-qTP4fvdto4_QU1J0g8eURUZQp9qZ98bUm_x837eLUSO8IR1tywynrV3wBkDheZQGKTiDZZ7q43Lkh_cdeWxlDtCcldUQ6RupS6-_hKNKX3zVDsO-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لارنس نورمن: در خصوص هر آنچه عراقچی در نیویورک بر سر آن مذاکره می‌کند، به نظر می‌رسد که او از حمایت نهادهای امنیتی برخوردار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148914" target="_blank">📅 12:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148913">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خبرگزاری فرانسه گزارش داد: یک هواپیمای مسافربری ایرانی با وجود تهدیدهای واشنگتن به اعمال تحریم، در چین فرود آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148913" target="_blank">📅 12:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148912">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx4BeWZjppDBN-_XSS1Yg9sXrY22wKbMh12p2iItZAbYC8ktK267JfS4gSkgY-ldQzbZw8kBZ7sRmA4l7_fgE0xuzieNtvPFmq-LyrTk1B20OTdmAXCwVnhrTP1F3S7m1n_ne1XMvPrrC6r-5axQBOoVpKnna_yJqYaBrbgw3rm7qLhAw6MLnbuTVcumZm9sLKtR7YVg8GuXoMhNWm5oNjR2LIyQmt-IttrPBdUiYWReGPTneJXdqx3fxMsXBhGqBSNRWBjzHPQQ-3AwZ-7AYoKppzfB31lU1MGERqCE-y5RAodxOBkqNWV_C3HNkPRJHEXVqMLgBwFe6essPh11_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم: با جنگنده‌هامون میتونیم محاصره هوایی رو بشکونیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/148912" target="_blank">📅 12:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148911">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/677484de4f.mp4?token=Tk5fjANsZUMmWKiJZ5h648Md3kvCaozipSTG-hruL-MDN3LGU6QTYFxsnR0hIfb9hDdPS-fcBqgp3nI-f2bNEsiRiF_r6fLF6Jt_k5zx8oFGTI3xJmLv26Dmcq3avNZOkBhaog6ZMgpvChaXF2MoaZVMqPGrcVbupf36hZGSh3jpqXBkucFjwNI_fgfBMwLUGaiv774IQBWKBlGugS9eP79tukRfi0bpzriAwztNCMW0uSSCz2lzvJJxO8bDlk1md1pN1os42NpzIEf5y6TJpc5lgrkIRS0O85p6XaKDX_E0CXar5s0wNyjcgIa7mkGkqq7z5mrRzz4zqQtnh3ZP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/677484de4f.mp4?token=Tk5fjANsZUMmWKiJZ5h648Md3kvCaozipSTG-hruL-MDN3LGU6QTYFxsnR0hIfb9hDdPS-fcBqgp3nI-f2bNEsiRiF_r6fLF6Jt_k5zx8oFGTI3xJmLv26Dmcq3avNZOkBhaog6ZMgpvChaXF2MoaZVMqPGrcVbupf36hZGSh3jpqXBkucFjwNI_fgfBMwLUGaiv774IQBWKBlGugS9eP79tukRfi0bpzriAwztNCMW0uSSCz2lzvJJxO8bDlk1md1pN1os42NpzIEf5y6TJpc5lgrkIRS0O85p6XaKDX_E0CXar5s0wNyjcgIa7mkGkqq7z5mrRzz4zqQtnh3ZP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنی سندرز، سناتور آمریکایی: «ما در ایالات متحده باید تمام کمک‌های نظامی به دولت نتانیاهو را متوقف کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/148911" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148910">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfotMKjS2QVcompYY_3ekpucYzGvggLq98pwc-707eJlxiv5ajBYPwPAwe7lwBmY_dUz6sLnQ6q6RIMXInGJhXpi83jyJo3juc0G5EgpovkBX4I53zTvez14qBpU9zhRk7NsBYMB3U-7IZCczblMKLubbk7eTzHi1ncPgt8tV5-HMSavEWF8PZ9sPLxvOYVasyEa7bglCyHrVbd8_ozbyyBJXOXa_HVKLgK5h6WkpnvjCkm988d1gOQHiTOX2n24FRuI3pstIQeIX-2ODi9lNTeoicBm735payZc6mxXXo6DhTQPtX2FJEXY4l1RtfQ0zTh41-cKEo6DfuHd1eFQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازنشر کرد:«ائتلاف نتانیاهو در تازه‌ترین نظرسنجی انتخابات اسرائیل پیشتاز است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148910" target="_blank">📅 12:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148909">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پزشکیان امروز چهارشنبه ۱ مهر ۱۴۰۵ ساعت ۱۹:۳۵ در هشتاد و یکمین مجمع عمومی سازمان ملل سخنرانی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148909" target="_blank">📅 11:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148908">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / گزارش شلیک ۴ موشک به سمت تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/148908" target="_blank">📅 11:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148907">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: سقوط یک فروند اف-۱۶ ارتش آمریکا در آلمان هنگام پرواز آموزشی
🔴
یک فروند جنگنده اف-۱۶ ارتش آمریکا در پایگاه نظامی ایالات متحده در غرب آلمان سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148907" target="_blank">📅 11:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«نشریه اکونومیست، دولت اسرائیل را — توجه کنید، پس از سه سال جنگ — به‌عنوان یکی از سه اقتصاد پویاتر جهان رتبه‌بندی کرده است. این باورنکردنی است.
🔴
از نظر من، این موضوع کمک الهی نیز هست، اما در عین حال نتیجه سیاست‌گذاری است؛ به‌طور ساده، نتیجه سیاست بازار آزاد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148906" target="_blank">📅 11:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148905">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQVShZKZ8gejhyGFOJxA8eJKTG2Fy2MzxceP1QjOf0lMlqEkyYQ_aBB06x9ac_0ecr9S_6v_DUG7eXx8PTz5fgcC5VrqtzDbmJigv7gMuWuIt2OsjDZWc-Rj5rmGr3k6IGcx3Z4B0zLiK0uariDak5S4GNW2H2Fsx5N9S6pOQcQ0SCvXfq6VUZmIy7KfrsBOhrbrdVHBZYhVjVhyUbaCymWqkIoTQZqB35l7D37r3cmXJrcHSrrnZmWiQwwtAuZVxFWRC1B2KtE8iOFQRrWL1Ks8rrdr_d7cCW5mAZd2EOwnslmfprU_QNY0MT69JdDZzamVget68vk4BMqZxhILxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سوخت‌رسان‌های آمریکایی در آسمان امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148905" target="_blank">📅 11:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bab278fdf.mp4?token=AVGHhPwILU7p-vdgNEZSlyOcQbNs3YJ9wF2UiIXjTMYk3DuQtCDM9NjxRi4j6m5R6vFm-xn0HyCNzSyhCN5bJVSBs2x6wHDZQEsxsLu2ziHFJkQiCO1bOtTPrJMtBs5zDN1MvdH-GH9eakchaOC4ia0FfS357J0dJqAsw8ulzZM5URqtVvR5qVIB_GM5z7c6Dcjs9uOrLLe-gPfJIPBK_zO0G82iVYozfb3jmL0uzUKkUFW3vcrlMPBAs9KbemlQZlG19w82qAgjla-gtYpVGDyr7lqQHdcIUaX08bA0UeKesv0UZx6HFOhnsl1l7gMRUpboxB4S5FWbkEEqec6ZDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bab278fdf.mp4?token=AVGHhPwILU7p-vdgNEZSlyOcQbNs3YJ9wF2UiIXjTMYk3DuQtCDM9NjxRi4j6m5R6vFm-xn0HyCNzSyhCN5bJVSBs2x6wHDZQEsxsLu2ziHFJkQiCO1bOtTPrJMtBs5zDN1MvdH-GH9eakchaOC4ia0FfS357J0dJqAsw8ulzZM5URqtVvR5qVIB_GM5z7c6Dcjs9uOrLLe-gPfJIPBK_zO0G82iVYozfb3jmL0uzUKkUFW3vcrlMPBAs9KbemlQZlG19w82qAgjla-gtYpVGDyr7lqQHdcIUaX08bA0UeKesv0UZx6HFOhnsl1l7gMRUpboxB4S5FWbkEEqec6ZDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی جشن شروع مدارس کلاس اولی‌ها رو داشتن توی تهران برگزار میکردن که به لطف اداره برق، وسط شعرخونی برقاشون کلا رفت.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148904" target="_blank">📅 11:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148902">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
طلا و دلار دوباره صعودی شد
‼️
اگه نمیدونی بخری یا بفروشی حتما به اینجا یه سر بزن
👇
https://t.me/+sN8qmnF1jDJlZGRk
https://t.me/+sN8qmnF1jDJlZGRk</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148902" target="_blank">📅 11:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148901">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
افشای جزئیات مکالمه محرمانه داماد ترامپ و بن سلمان
🔴
نشریه آمریکایی نیویورکر فاش کرد که طی یک مکالمه محرمانه میان جرد کوشنر داماد ترامپ و محمد بن سلمان ولی‌عهد عربستان نقشه وی برای کنار زدن محمد بن نایف پسر عمویش از ولایت‌عهدی در سال ۲۰۱۷ بررسی شد.
🔴
در این گزارش به نقل از یک مسئول اطلاعاتی سابق در منطقه آمده است که کوشنر به بن سلمان ابلاغ کرده همه در دولت آمریکا به جز سرویس‌های اطلاعاتی از وی حمایت می‌کنند.
🔴
این پیام به مثابه چراغ سبز واشنگتن خطاب به بن سلمان برای اقدام علیه محمد بن نایف تلقی می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148901" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148900">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: رهبر جدید می‌توانند درباره سلاح هسته‌ای فتوای جدید بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/148900" target="_blank">📅 11:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b004f0a6b.mp4?token=Cx2YXv5rsRdHybvyUSdIp5sWthh-Az5veeAOUgqrYr_aVeIimYLfUXAULgB29u1A-8ZswVzkVJTd41oR12k3iIGq4Nl6W3Hei4NIjB7s0KwQStqfbq5T6D4CS7m-RTTE1393dzJEPP6hHcEO7npKX1q2MpVWg5KeVOPrJMusNdvLEsS3j1fG-w-SobmXEKETx1NXW5k0-_Q-XfW3pC-2Iavs9wZJn2EXj1qF02-TmFvSrbIwArdHl4q6g9E-7g_XsKdTKEw__n31iN-_PkFWovtgGf6eFXys-d2-u6iA0Dx_2P1_NVrpca0iHxvdcxum3hgapm_kpvf4ylPvbtb3HiQDV2piR4hGdAZluLWVdq4UO3mXXKN8sMojRiuC_nFb9Tzta8oYzcQxQRqGyTpVAS2Og_yi5-eeSwuqEY7wS2j0LyqLzmQ1EZSSqvkhtlU_vwDJ46dLRruYFDoksxRHogHNtnvsAAp6ZFdcCw8F7uDzwUeP2cmu9fv8jumek9wZQv-NGUePGKbRJ48Xr4QHiKBByiblwvkbRE8ib6n2wtKXXel0_rvrYtH4G4zHcNa-rIziRPNqfJBiBbcrbI8zLrsSBRV8b4nMdny0dcmS0Bt_3Q4li55lHD8K4r3_pjCcVqeAWIqMZGit0iznMxA4FinR9UozpHLhGEgYaywMZ70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b004f0a6b.mp4?token=Cx2YXv5rsRdHybvyUSdIp5sWthh-Az5veeAOUgqrYr_aVeIimYLfUXAULgB29u1A-8ZswVzkVJTd41oR12k3iIGq4Nl6W3Hei4NIjB7s0KwQStqfbq5T6D4CS7m-RTTE1393dzJEPP6hHcEO7npKX1q2MpVWg5KeVOPrJMusNdvLEsS3j1fG-w-SobmXEKETx1NXW5k0-_Q-XfW3pC-2Iavs9wZJn2EXj1qF02-TmFvSrbIwArdHl4q6g9E-7g_XsKdTKEw__n31iN-_PkFWovtgGf6eFXys-d2-u6iA0Dx_2P1_NVrpca0iHxvdcxum3hgapm_kpvf4ylPvbtb3HiQDV2piR4hGdAZluLWVdq4UO3mXXKN8sMojRiuC_nFb9Tzta8oYzcQxQRqGyTpVAS2Og_yi5-eeSwuqEY7wS2j0LyqLzmQ1EZSSqvkhtlU_vwDJ46dLRruYFDoksxRHogHNtnvsAAp6ZFdcCw8F7uDzwUeP2cmu9fv8jumek9wZQv-NGUePGKbRJ48Xr4QHiKBByiblwvkbRE8ib6n2wtKXXel0_rvrYtH4G4zHcNa-rIziRPNqfJBiBbcrbI8zLrsSBRV8b4nMdny0dcmS0Bt_3Q4li55lHD8K4r3_pjCcVqeAWIqMZGit0iznMxA4FinR9UozpHLhGEgYaywMZ70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرود زیبا و نرم هواپیمای حامل پزشکیان مورد توجه دنیا قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148899" target="_blank">📅 11:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148898">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQrbDoUCjeSc5sS05FEIjUn0sh5kddaSOpI9Vi2ZjooJdX_C8fnFZL32zJ976wmNq88hxLbwjm5XD4QXpYmudxAaXxT3TJnVtNj7H2AQyGlMMn4Bq6MwXow_7qzGfOJrgE951huWkN9r9zQXAy3Zoqb5mcIclSMiPM1vnEAmRNpUkIA1Cc9T_dCv_JjnbCJZb-lJtr9XDcg3YqufelFKRqenVd6I84791eS0Ltd3htG0yohPBW1-unQMmXxBXtNoU2VQxLJy8uP2OH9_crQ4_r5I0IoEukWn2z0dvgUefMYcbzgvfNCjYukT__X5LDezYQvWFrRbllA_B8Xz2HQQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم امید ایران  ۴ بر ۱ به امید کره شمالی باخت و حذف شد
جوانان ایران قرار است بعد بازگشت مجدد به پارتی برن و دختر بازی کنن و تو دلشون بگن کون لق فوتبال
@AloSport</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148898" target="_blank">📅 10:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148895">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bb721a98.mp4?token=vA8GywJtccxhUhvwe5bYQEzpT06sODLm5jxXaVG_17ntO_pC1lUotTqvjRvtCxceaAbbg67P9NpU6wFmI9OufIcF7MWDuC9jYeblb-hBlkRkmwpnuKSayL1kGhoG52GP8GJ79cCg1RAHoKIb8n7vFT8NETEUR96FyO3f0yg-FicsQQrSU33CcGqI1qqD5WsJEdqnUGJP4HG0tFD61mEVrCsj7YXgvm3axRv-6oBnwSFYf_L8QWR9SbNIOw70dZ8JxbupbVZoo2LBwv3Kgc4rIGo6vxZKbX3MaNxieZeGaEgg2MVxgLtcG4OxGsD9XjTb19jECo0jIcIfmGEKXG21WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bb721a98.mp4?token=vA8GywJtccxhUhvwe5bYQEzpT06sODLm5jxXaVG_17ntO_pC1lUotTqvjRvtCxceaAbbg67P9NpU6wFmI9OufIcF7MWDuC9jYeblb-hBlkRkmwpnuKSayL1kGhoG52GP8GJ79cCg1RAHoKIb8n7vFT8NETEUR96FyO3f0yg-FicsQQrSU33CcGqI1qqD5WsJEdqnUGJP4HG0tFD61mEVrCsj7YXgvm3axRv-6oBnwSFYf_L8QWR9SbNIOw70dZ8JxbupbVZoo2LBwv3Kgc4rIGo6vxZKbX3MaNxieZeGaEgg2MVxgLtcG4OxGsD9XjTb19jECo0jIcIfmGEKXG21WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله اقلیت یا همون امت معکوس به ناصر اسدی نماینده ایران تو سازمان ملل بخاطر اینکه موقع سخنرانی ترامپ سالن رو ترک نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148895" target="_blank">📅 10:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148894">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فایننشال‌تایمز: بی‌میلی ترامپ برای مقابله با انصارالله، اعتماد ریاض را تضعیف می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148894" target="_blank">📅 10:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148893">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063d554ef6.mp4?token=IHZ2y89Tl1OthXBN1nyUeoPe35McKOr96OpSWkoUmY35h-KOvkQJEoyocoSra_Ki7biBSTa_f5WOH2P1izIqyH-WVkXa4Ih60uOSgehdIUrYPEVO1kaiQ8V3UEts6eoGKSmqB3MgySulcevnPZeMezXV14JkFbuA5sj_knF4r8Px-GYtNSACUQbOTQjFUARlIfDCWz81G5CkDs-9u8LmJkMjResK0c-FhtX0MYqvOA2N8qtR_D3710Ls1ysux2SW9iGqUP6JEQwNv05XgBHPhV018e5f7N57y_85TbKiVqb61FSIBTYPP8InZq_Ke0gCGz0gUe_WJpcdWkjQ2S4n6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063d554ef6.mp4?token=IHZ2y89Tl1OthXBN1nyUeoPe35McKOr96OpSWkoUmY35h-KOvkQJEoyocoSra_Ki7biBSTa_f5WOH2P1izIqyH-WVkXa4Ih60uOSgehdIUrYPEVO1kaiQ8V3UEts6eoGKSmqB3MgySulcevnPZeMezXV14JkFbuA5sj_knF4r8Px-GYtNSACUQbOTQjFUARlIfDCWz81G5CkDs-9u8LmJkMjResK0c-FhtX0MYqvOA2N8qtR_D3710Ls1ysux2SW9iGqUP6JEQwNv05XgBHPhV018e5f7N57y_85TbKiVqb61FSIBTYPP8InZq_Ke0gCGz0gUe_WJpcdWkjQ2S4n6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
رئیس‌جمهور سوریه، الشرع: وقتی در کاخ سفید با ترامپ دیدار کردم و او گفت که بلندی‌های جولان متعلق به اسرائیل است، به شوخی گفتم: «چرا نیوجرسی را به اسرائیلی‌ها نمی‌دهی؟ تو مالک بلندی‌های جولان نیستی که آن را ببخشی، اما نیوجرسی مال توست.»
🔴
فکر می‌کنم نیوجرسی پر از دموکرات‌هاست و آنها به ترامپ رأی نمی‌دهند، بنابراین خوب است آن را به اسرائیلی‌ها بدهی. حداقل این چیزی است که مالک آن هستی. ترامپ مالک بلندی‌های جولان نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148893" target="_blank">📅 10:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148892">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b063fe34.mp4?token=vyiyznIpzQfsXKqLBCg-Hm5XQUqXIeVVbuInBMETOEwcDg51RE7n6LcxA8fy171KRQyrrUmK7d4diOV9bqMITYTdyBklvepdDdzQQ1lITVxxA2BNDBkNUUqThDgZ-5nOtHJQhwuR83yAxK1Bbxy4iOHW2yRNrLO1coPq0Rk87y8zljCwv4ZMCaPDjMVvg370ErJjXWvxXD4C0nB7iAFp2K3cQ7BHP-qt0W69Ev1U8e-VPnqhtV72ec7OQUInGuAIZuo5WzxD7Us04q5cX_ypeLOBkojd4nk9-Ilq2V7PjoDiHRJQLrwsRo2htDoUYICkwfRhJdNH3DEbzBwlx6VAbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b063fe34.mp4?token=vyiyznIpzQfsXKqLBCg-Hm5XQUqXIeVVbuInBMETOEwcDg51RE7n6LcxA8fy171KRQyrrUmK7d4diOV9bqMITYTdyBklvepdDdzQQ1lITVxxA2BNDBkNUUqThDgZ-5nOtHJQhwuR83yAxK1Bbxy4iOHW2yRNrLO1coPq0Rk87y8zljCwv4ZMCaPDjMVvg370ErJjXWvxXD4C0nB7iAFp2K3cQ7BHP-qt0W69Ev1U8e-VPnqhtV72ec7OQUInGuAIZuo5WzxD7Us04q5cX_ypeLOBkojd4nk9-Ilq2V7PjoDiHRJQLrwsRo2htDoUYICkwfRhJdNH3DEbzBwlx6VAbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورود باشکوه و ناگهانی ترامپ به نشست الزیدی، اردوغان و شماری از رهبران خاورمیانه در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148892" target="_blank">📅 10:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148891">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9jbe1TGb4iBaGZUiURB6DcPdpKpUXtf8_S8gxwOOMpPjtLABwJ-xDGTw9G-sAw3_HTojh1naHuLE0RqmvUMVC78jGpjRSRrHPI3t-ttULls7KdVG5pv8bT8SM0IU5tweN0c55KnSFc5clk7YNPQ-ExsxiVoWt6u1Eh9ghkbS-cGRiH9_QxIn5t9vGrecD9spPCtKDvtUC9T4P-MK3411xwNPJPwYsfS7FEktjcP4n0pZC79kBPzkhwnz7fqtkWx1LXZt6GVBEA-uHV2hULBMVPd_d3oDE5sgZm3zdek4aAQgHAhs1Y907pnk4EFPJ20fCeorBWZxSFF6ixRQJT6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
پزشکیان باید تو سازمان ملل به ترامپ سیلی بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148891" target="_blank">📅 10:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148890">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
داده‌های کشتیرانی: روز گذشته ۳ کشتی باری حامل کالاهای اولیه از تنگه هرمز عبور کرد، در حالی که میانگین متحرک ۱۰ روزه، حدود ۱۵ کشتی بوده
🔴
داده‌های مربوط به عبور و مرور دریایی نشان داد که روز گذشته، سه کشتی باری حامل کالاهای اولیه از تنگه هرمز عبور کردند؛ این در حالی است که میانگین متحرک ۱۰ روزه حدود ۱۵ کشتی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/148890" target="_blank">📅 10:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148889">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ddf2a0d29.mp4?token=KUZ6kUmFfMF8NQokxf7xkAQvhA4GUFPweAnUvuwp6D-P75UgyEvA_ewkoSkOSUT_p8FmrGMJqEdEVfRnoPxlGpeSWwOXSaBuNHR1IFjzogtZw13E_PcDWB-pLmDyza1fXG2xiWDARcZyk5klERqedzHx9Izgr0aTIGcG2maKtUfrKaTxLa2VqaLPVl7rCXeepEb1M_tdIXY-7zehvt65Axlc61jy2uYujGA-yvTyb-hUBA5u4OliUm82z9JxXqCzhzbTVMPzRo5YzbTgENTUmHa62kk4cmzDKXRxbhvYXttxsUm7l2WC1rFLkF4NyQ6hBJGY6-PEb9-9CL20dQgC3zBys29jJiFFxzX3kEJB7VSkWQiElGniCbT2NLPK9XRFhJOdocNGHFAmgyIjI8fq8yUO_MZDcD6pRQ2AqonbS-3QpiKWo-4Ki3yzlJRqED993ef7kUWPVAajOMoLRWXhQrcnpX54542Wdo8uKQyST-7Tnw-VXI4eJeeoFaojDvVPedjSSiK3kXybk1vWpNO4WLJtuq2tsKbljsP7adgBOmYDZ22_IKw4m4D1Mb6gbfKQTBFuNx602W3alGgpg91F7wVYiAWevxUbrcouKYLsNs9Etuf8jFou9SFIMV169GTptUGUtVG5-LMKDYrIx8EsQgJEv6sGhpLOUvnW2IGrm38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ddf2a0d29.mp4?token=KUZ6kUmFfMF8NQokxf7xkAQvhA4GUFPweAnUvuwp6D-P75UgyEvA_ewkoSkOSUT_p8FmrGMJqEdEVfRnoPxlGpeSWwOXSaBuNHR1IFjzogtZw13E_PcDWB-pLmDyza1fXG2xiWDARcZyk5klERqedzHx9Izgr0aTIGcG2maKtUfrKaTxLa2VqaLPVl7rCXeepEb1M_tdIXY-7zehvt65Axlc61jy2uYujGA-yvTyb-hUBA5u4OliUm82z9JxXqCzhzbTVMPzRo5YzbTgENTUmHa62kk4cmzDKXRxbhvYXttxsUm7l2WC1rFLkF4NyQ6hBJGY6-PEb9-9CL20dQgC3zBys29jJiFFxzX3kEJB7VSkWQiElGniCbT2NLPK9XRFhJOdocNGHFAmgyIjI8fq8yUO_MZDcD6pRQ2AqonbS-3QpiKWo-4Ki3yzlJRqED993ef7kUWPVAajOMoLRWXhQrcnpX54542Wdo8uKQyST-7Tnw-VXI4eJeeoFaojDvVPedjSSiK3kXybk1vWpNO4WLJtuq2tsKbljsP7adgBOmYDZ22_IKw4m4D1Mb6gbfKQTBFuNx602W3alGgpg91F7wVYiAWevxUbrcouKYLsNs9Etuf8jFou9SFIMV169GTptUGUtVG5-LMKDYrIx8EsQgJEv6sGhpLOUvnW2IGrm38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه، درباره ایران: «فکر می‌کنم پس از آغاز جنگ در اواخر فوریه، اهمیت تنگه هرمز احتمالاً دست‌کم گرفته شد و امروز باید این مسئله را حل کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148889" target="_blank">📅 10:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148888">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این وسط ماهم 1m شدیم
✔️
مرسی از بودنتون
❤️</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148888" target="_blank">📅 10:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148887">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKUoNHWz4Nf_VI93OoybYX-QIz65ElCrTv41I0dabDHnZ15CC9UHczOZ41dgjcPSbx6j3JOGUbTcjZQHc07U6AaDtWmWn8yMPacQzKyKLGDAfw7uLIG4vFFbo8rcjjQfnmam-xuBCEVsIyV_fyNVq0pCR-r4fiYiWHv4dQvxCCHT480lhwg2Z7n7WkOBqAg-tKng5ypCkWCKQUGZYpXLq_LFB6RIWIGlUE7nGvzK75nlXGZlnDCFppqAfUQk4N-fmcZ391sKCrhHShzUN_g7NXO8OsnW9UMOP-Nsa4NasdwOT_clqVXqgtzGRA2-NQiIjXKiyrPtAo4jiLiFh1DZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجولانی: به شوخی به ترامپ گفتم «اگر می‌خواهی سرزمینی به اسرائیل بدهی، چرا نیوجرسی را نمی‌دهی؟ چون تو مالک جولان نیستی»
🔴
جولان سرزمین سوریه است و درباره آن جای بحث نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148887" target="_blank">📅 10:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148886">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3982b6a001.mp4?token=gftl_bUPy-4oOrpE0Re4ZkMon_emkS4iJG4TUk-jE2sThWvSPsPO2bhcJOEYvSoKcbZ6t_ieUMcrl5dxEUmyBEXfhefdhYZ5TG2lcFIRcdMJxOWQc4EY04NZMsbuWZyOgVFM1qOq5I9oa3kugMfD6fQd_kXuR3w6y6udfrKdT8mZL13RNhTF3vZYgV_TVY7WMSIZ7qcZLVqKxEksXuFnH78Si1nOp0u7dveICYHSGAAQwyJ857Y-CYIA9cuOaYhqzMjq4vXL2amKShewmWRf9ITph2SG62iyCv4-xRCGUp_nHh3Us24N2HKNeO2yZNlRPvp8X_Xi7aan6EiMjrfoFr5IVdTz-XZrK6-5pmYhg86b8DMkFOeuU65NIkJjQdWHzEqG72_f1b1lmdPXfFY85lSq7L02qyFccBVzEYWwVHXhEk4jd7a4kh0FNx8ivg5vdWVv3_MUGZv3KfsCSabmhFga7vInLB3fkVJC1iJayjoy0Hwn8CrkguA93FmnUIVD_wCLs4mKuRugNGkj184FQHtSbebMJMgiSiJx2a8VZUH2XlULvwwuLxrzatALTqRDbsHPtf4JYnETK47WwPlxBcmSHnzNCCygiuMRZqjNnnnIpCSLoPd2okr1ROn91ACh-iEg_fhmN2ZaF2qzxlVwMt-Ypfix3k_Cd5AefcGGp8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3982b6a001.mp4?token=gftl_bUPy-4oOrpE0Re4ZkMon_emkS4iJG4TUk-jE2sThWvSPsPO2bhcJOEYvSoKcbZ6t_ieUMcrl5dxEUmyBEXfhefdhYZ5TG2lcFIRcdMJxOWQc4EY04NZMsbuWZyOgVFM1qOq5I9oa3kugMfD6fQd_kXuR3w6y6udfrKdT8mZL13RNhTF3vZYgV_TVY7WMSIZ7qcZLVqKxEksXuFnH78Si1nOp0u7dveICYHSGAAQwyJ857Y-CYIA9cuOaYhqzMjq4vXL2amKShewmWRf9ITph2SG62iyCv4-xRCGUp_nHh3Us24N2HKNeO2yZNlRPvp8X_Xi7aan6EiMjrfoFr5IVdTz-XZrK6-5pmYhg86b8DMkFOeuU65NIkJjQdWHzEqG72_f1b1lmdPXfFY85lSq7L02qyFccBVzEYWwVHXhEk4jd7a4kh0FNx8ivg5vdWVv3_MUGZv3KfsCSabmhFga7vInLB3fkVJC1iJayjoy0Hwn8CrkguA93FmnUIVD_wCLs4mKuRugNGkj184FQHtSbebMJMgiSiJx2a8VZUH2XlULvwwuLxrzatALTqRDbsHPtf4JYnETK47WwPlxBcmSHnzNCCygiuMRZqjNnnnIpCSLoPd2okr1ROn91ACh-iEg_fhmN2ZaF2qzxlVwMt-Ypfix3k_Cd5AefcGGp8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه، درباره ایران: «این درست است که ما در این جنگ حضور نداشتیم؛ نه به این دلیل که در کنار آمریکا نبودیم. ما برای آمریکا احترام قائل هستیم و فکر می‌کنم متحدان خوبی هستیم.
🔴
اما وقتی می‌خواهید کشورها و افراد را درگیر یک اقدام کنید، باید با آنها هماهنگ و برنامه‌ریزی کنید و پیش از آغاز یک جنگ با آنها مشورت کنید.
🔴
ما تصمیم گرفتیم به این جنگ نپیوندیم، زیرا معتقد بودیم — و من همچنان معتقدم — که گزینه درستی نبود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148886" target="_blank">📅 10:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148885">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIHL-swpUvpkb60lxrHPXEgp82JO7fJ8aQU-PQKqlwko8weglAlvQmrDmhF_6W17BAErhIrnxoYnEtUc94VNs8IR_VVeZ6R49Yt_jcsc-ScJ7bYH-jLe9m6AmFkh1IVAvQu_tAj-Od7PdDL77_aec1e4bBXa9Fl0TDPlEUJuf-DZQ5h5gwo39hg1-lFoZmXq8kS7CoGu-OYjMhw_257P_fAv0dp5u8JIg5-nJmFDgHvOLOdCt4UAL4JbIu-WnMLBPUhug1Bk--YdNQH75gDuv8qc-tgMmLAICtVc5v56i-CBcNEnDNAMU9IyVTI8uZ9bRq7Ssgo8-5MtKJ7hpWVqhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا: «تمام این آدم‌های پست، مثل کیتلان کالینز، خبرنگار درجه‌سه شبکه جعلی CNN، که واقعاً فردی ناراضی است، گفتند قرار نیست من را پوشش خبری دهند
🔴
پس چرا در محوطه رسانه‌ای سازمان ملل مثل دیوانه‌ها فریاد می‌زدند و جنجال به پا می‌کردند؟ او آنجا چه کار می‌کرد؟
🔴
او به «ترامپ» اعتیاد دارد و CNN و MSDNC هم همین‌طور. همه آنها بیمار، خائن و دیوانه هستند!
🔴
«خبر خوب» این است که آنها یک قاضی بسیار خوب، البته برای خودشان، و کاملاً بی‌وفا دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148885" target="_blank">📅 09:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148884">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=kMLcYOSP3sUMwyOQQMkKzG-5cwPovH5xGGEEtDu_4ol56Ak8a3vSSW1rng7gnBdlyxoZDhdfXAsyPiPNGHMxeGhJPqcmRiEqFCtsmiSLQrGqHdefQ6cH3_Nt6ze_hhhQtODqyUYqzxjOA9hsffo52rFqroqC4o6VtAfKTnvN-sc9rmTpnlmiA_Q-flD-rEQv2fcrnfNFDy3wOiqS-d3rXBjTSrLKdetn7FvfsQ_VdzJi8-rf3OhJFiE2Fn3VcXytSSSkVMl2F9VdxzbCoN-NydfyrEf17cIC3gmtuley9Ve0M58XckDwR-7VlGx5VFjWLvsvUddi7rEsLcuY1kiJjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=kMLcYOSP3sUMwyOQQMkKzG-5cwPovH5xGGEEtDu_4ol56Ak8a3vSSW1rng7gnBdlyxoZDhdfXAsyPiPNGHMxeGhJPqcmRiEqFCtsmiSLQrGqHdefQ6cH3_Nt6ze_hhhQtODqyUYqzxjOA9hsffo52rFqroqC4o6VtAfKTnvN-sc9rmTpnlmiA_Q-flD-rEQv2fcrnfNFDy3wOiqS-d3rXBjTSrLKdetn7FvfsQ_VdzJi8-rf3OhJFiE2Fn3VcXytSSSkVMl2F9VdxzbCoN-NydfyrEf17cIC3gmtuley9Ve0M58XckDwR-7VlGx5VFjWLvsvUddi7rEsLcuY1kiJjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان اکنون برای شرکت در مجمع عمومی سازمان ملل در نیویورک حضور دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148884" target="_blank">📅 09:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148883">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شی جین‌پینگ رئیس‌جمهور چین به آمریکا سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148883" target="_blank">📅 09:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148882">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c86473b8ba.mp4?token=nfn3KR37AAToyMnbnzXp0KER_kZUByOm9Hpw8nNqAlFV67KqVO6IsA3U98T1Ntuv960QzidMVtsdBfKi14POQBLz-23t_IeJjCrwjQ4J0aLJinVC7JqMnxLdSWOF_Iwub4EemNVAYZyEarEffs2tD8ETPQ6gePmTLqFGYl3OTxhGyV5IDHZc-DAfMt74g-iqxBDwOmF5MkcxYuFGwh9axQtu30Z2NQIuVnOmAkDnlwa7OtbgqWouuzD1fsmnxBjhmCJevV7w0ghVJz5wppHPGg7tv0N1t9-xBdmVlZYIRmxzCxueTF56bTUmk6EAaH-1wmtjeGFlioQHInGwKShBIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c86473b8ba.mp4?token=nfn3KR37AAToyMnbnzXp0KER_kZUByOm9Hpw8nNqAlFV67KqVO6IsA3U98T1Ntuv960QzidMVtsdBfKi14POQBLz-23t_IeJjCrwjQ4J0aLJinVC7JqMnxLdSWOF_Iwub4EemNVAYZyEarEffs2tD8ETPQ6gePmTLqFGYl3OTxhGyV5IDHZc-DAfMt74g-iqxBDwOmF5MkcxYuFGwh9axQtu30Z2NQIuVnOmAkDnlwa7OtbgqWouuzD1fsmnxBjhmCJevV7w0ghVJz5wppHPGg7tv0N1t9-xBdmVlZYIRmxzCxueTF56bTUmk6EAaH-1wmtjeGFlioQHInGwKShBIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اندی برنهام، نخست‌وزیر بریتانیا:
«
ما نزدیک‌ترین متحد آمریکا هستیم.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148882" target="_blank">📅 09:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148881">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ماکرون: جلوگیری از دستیابی تهران به سلاح هسته‌ای هدف اصلی است اما تغییر حکومت ایران با بمباران گزینه درستی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148881" target="_blank">📅 09:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148880">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
کرباسچی: فرض کنید بجنگیم؛ تا کی بجنگیم؟
🔴
نگران تحقیر از طرف ترامپ نباشید، پزشکیان بلد است پاسخ بدهد.
🔴
خسارت‌های جنگ، در نسل آینده هم معلوم نیست قابل جبران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148880" target="_blank">📅 09:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148879">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCQHjCdY-gzVagc0Wfr-JLiIrVe0nM9fLzPhMpwxhhaORmMCpBLhC-edHkF9Fk7glDHlaKcuRkGk8GbmRqW4oIZfQuWK3h_eI0RjvqKAcOcPlBieFzBU82Bo9L-gc6o5w-DAp6ZzlebcCLH2DNui7Oi9jeYHT-pidm1ksRui21QTbSrGHwlO5NzPQp-Lg25l93cCtItEpCFEq9bHbIBnlsMOyRtOcvnPWtQx6ygJSWhJrLJ6e3OQIOCks8tz5pnAT3pNk2c85NeQb_UAZdvnMhX1Ry06RkzmWWnKVVBTNpjg5ZP7Ma0T_TUzboRqSfWTXLlryuMiQZZk949AArC5qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از گرمای شدید تو هفته اول مهر ماه، اواخر هفته دوم سرمای شدید داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148879" target="_blank">📅 08:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148878">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd370cbed9.mp4?token=tyFdMqfA0GI6tsVC-GiY4LoC9a2GwmLQtWwT6qE4V4rZZH6N__DXSAyxdTHuMlVVZ6dXFfKntbZTsGQ6wVs6n9yNYbIeaa_85O6f_1aWHlVsOu71E0cu6kl243Ge053t4lqdmPErI4N8M3dIyQJHfL81waWpeOZWnwmxwcqFg1zrceFcDxCI2Celmgck-5IRBA5bEUsp_yyR7sDyQqWl7Ltaxo1lMM2jUjMICPxpuKIuYoCzFiQASpWT5qeTp2ka0_WcttfofNJavwPM2ThMyuAMO7f5SYZ2Spzgxk9ZHZf6EVanQOBdFm6mRQ1xo06-WEVby_UCruXTh3X7M0os1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd370cbed9.mp4?token=tyFdMqfA0GI6tsVC-GiY4LoC9a2GwmLQtWwT6qE4V4rZZH6N__DXSAyxdTHuMlVVZ6dXFfKntbZTsGQ6wVs6n9yNYbIeaa_85O6f_1aWHlVsOu71E0cu6kl243Ge053t4lqdmPErI4N8M3dIyQJHfL81waWpeOZWnwmxwcqFg1zrceFcDxCI2Celmgck-5IRBA5bEUsp_yyR7sDyQqWl7Ltaxo1lMM2jUjMICPxpuKIuYoCzFiQASpWT5qeTp2ka0_WcttfofNJavwPM2ThMyuAMO7f5SYZ2Spzgxk9ZHZf6EVanQOBdFm6mRQ1xo06-WEVby_UCruXTh3X7M0os1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پس از پیدا شدن یک کیف مشکوک در نزدیکی مقر سازمان، تیم خنثی‌سازی بمب آمریکا اقدام به مسدود کردن خیابان کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148878" target="_blank">📅 08:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148877">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz8QqW6Sfhw57psK7MOsTQN3fvFNz7Ixe5t6S5MpBh0HdJshR_q8RzSpYBw6pefHPQxEfwFBxWQE8R398kMgBkk7qi2sleuzGW-e91E1CKIwI_93a8U7epzj09w3_osFPNteMtbcOQ89EZ9v1Cv_NxCUPgImZAM556Y8nq5Y85FW5aWcG_WW3-ZP874Fviq5mcTE1nrw0cy_2Nr0m9byZCYK_zw6BXw4pPZwfG1Y3UrimT8nnzkbBohUw-6BOmT-R4B-zw9nVhT5ocBawyg49t3sMvGWhxI3E-CsnSNqzhNTkdp0OqYTaNMDQHpWcBM5jbXQK0GhTuWHic-K0dFMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در نیویورک با دِلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148877" target="_blank">📅 08:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148876">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کیهان: برای جبران فشار اقتصادی باید از کشورهای عرب حوزه خلیج فارس پول بگیریم؛ اگر ندادند به زیرساخت‌های آنها حمله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148876" target="_blank">📅 08:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148875">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhC5_tyS4EdYbvqfku4ogyd13pX4QZ4UiylFd_HdfvkVWsAeyyTp1-LpoQMEvbC7nExyTnuklCL6ZSa6SH6pjYcnm1f3C242Qv9ErMMvQP1vrKqof47JPKiAU8d5E7wUJmT2P98vv7i76dUlAcGUHgZvV60Npt6HOyctmSgfON_dUe_471NdKmLvCaNMnNGCiUJlLQ9pOnJVxfHpzXTYtsQO1V96KmTlQGWRKcDbBtg33y5PsEZiCpJg9C0o1qA52yGtfIMxZucgSMIdr7H1U608LIq7WrtFC1gZSEJqfT9eN3QH88MqerMB3XpxbZjCjn5vvkmUSHPCB7F5c7-obQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استیو ویتکوف، نماینده ویژه ایالات متحده آمریکا: امروز، در حاشیه مجمع عمومی سازمان ملل متحد ما در گفتگوهای طولانی با هیئت ایرانی از طریق میانجی‌ها شرکت کردیم که در طول روز بین دو طرف رفت و آمد داشتند.
🔴
آنها یک دور از مذاکرات را با موفقیت به پایان رساندند که امیدواریم سازنده و ثمربخش باشد. میانجی‌ها به کار خود ادامه خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148875" target="_blank">📅 08:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148874">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
خبرنگار الجزیره: مذاکرات ایران و امریکا در سطحی پایین‌تر، اما مهم، در جریان است و باید منتظر نتایج این دیدارها ماند
🔴
نورالدین الدغیر خبرنگار الجزیره نوشت: در بحبوحه تنش‌ها، دیپلماسی میان تهران و واشنگتن از مسیر نیویورک بار دیگر از سر گرفته شده است و مذاکرات در سطحی پایین‌تر، اما مهم، در جریان است و باید منتظر نتایج این دیدارها ماند. فضای دیدار ایران و آمریکا مثبت گزارش شده و یکی از میانجی‌ها نقش مهمی در این روند دارد.
🔴
العربیه به نقل از منبعی بلندپایه: نشست نیویورک میان هیئت‌های آمریکایی و ایرانی، مذاکرات را از حالت بن‌بست خارج کرده
منبعی بلندپایه به «العربیه» گفت: نشست نیویورک میان هیئت‌های آمریکایی و ایرانی، مذاکرات را از حالت بن‌بست خارج کرده و موجب تحرک در روند مذاکرات شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148874" target="_blank">📅 08:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148873">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7832e2a810.mp4?token=i1w0fIFbeNUrUyRMmJQbW8E0e34cddBgz6vmXPHYulOt4tTc3d05eEcrteX4udxrhrHSHTnzfh3q2NqOJsjwRI54VSyenSwmwbhJAOFhcQbya8E5_9aTLEdbL-YRvDDeJjc-SCbO8tgl8vKv1azyn2H2qCcpLX14NBiwoXPHyQ9-FK5KmIC3eDBOjlFP4ikC-1vgtmvdXtVt04MdiVcH78s2EGez61FbyOOV8nfcuc1m3zjb66L2iDf743KhZfNnUS3Ui8QbWU7YO9hkytK2Dvzk0rY7kgjLROKnkPyBYHUYGHGQeG9MxwWi52HvUka-ME44h6OhR1uEEreK0Ie5pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7832e2a810.mp4?token=i1w0fIFbeNUrUyRMmJQbW8E0e34cddBgz6vmXPHYulOt4tTc3d05eEcrteX4udxrhrHSHTnzfh3q2NqOJsjwRI54VSyenSwmwbhJAOFhcQbya8E5_9aTLEdbL-YRvDDeJjc-SCbO8tgl8vKv1azyn2H2qCcpLX14NBiwoXPHyQ9-FK5KmIC3eDBOjlFP4ikC-1vgtmvdXtVt04MdiVcH78s2EGez61FbyOOV8nfcuc1m3zjb66L2iDf743KhZfNnUS3Ui8QbWU7YO9hkytK2Dvzk0rY7kgjLROKnkPyBYHUYGHGQeG9MxwWi52HvUka-ME44h6OhR1uEEreK0Ie5pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو در مورد ایران
:
اگر آن‌ها حاضر به قتل عام مردم خودشان باشند، فکر می‌کنید با ما چه خواهند کرد؟ یا با اسرائیل؟ یا با همسایگان سنی خود؟
🔴
همه بر این باورند که آن‌ها نباید سلاح هسته‌ای داشته باشند. تنها چیزی که تغییر کرده این است که ما یک رئیس‌جمهور داریم که حاضر است در این زمینه اقدامی انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/148873" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148872">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkq6URolNFwjr_RqduBKeJBak4JPoMlBD5JTHA8a7wQoBNsRluhiaf4x_CfYJLyIyGUiaH1KS7TUqkqvDwJfrTbf1lHzysFcgjQ_SLnKCfRPJ6nQRAVokb7Lr-hmJJ_hxlv2JrpIOWhg_ypURMxZKucdFKeZF9f7K8MAcGQcZMDlKEgYLRvlsUQz4XnI6j3Zc3ZTpPZez3RK0EGEq3dU58tX3h4gEw4dS6kPG_cV4B2e9ljRaGVJYdK1jVykXb4XxwqFaIKvGu2fJdIrwV8XiA6ljdIKNACouNd_353pV2CMgwgM6rquH2EwHGkbIFVZgWlKk1kpUq3alLC8xObPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: ترامپ گفت که مشاورانش را تشویق کرده است تا ممنوعیت صادرات گازوئیل را تصویب کنند، زیرا قیمت سوخت در بحبوحه فشار جنگ‌های ایران و اوکراین به شدت افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/148872" target="_blank">📅 07:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148871">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/148871" target="_blank">📅 01:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148870">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
یدیعوت آحارانوت: سخنرانی نتانیاهو در سازمان ملل متحد، غافلگیرانه و بر ایران متمرکز خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/148870" target="_blank">📅 01:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
چندین انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/148869" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148868">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nsff2OkMSucQdTOf01eOHmAAWnjxZEwZxca4qHnjDNeXNtK8aotafsI3sJVUVR9fmYNyq2JsasYjxPJMQ3N0s24Vz-0UiCmxabErZGvxficgEnR6tMwG1NJAB4p_AGTA2jMUxfFnDNBpDKFN7ybB0JRuelKqflnvkEHWRK1XVwMqB7lr370gtGDkwBbomkKFXdNi7mdhCfjMtIyns8GDLwOji42uw7yeSTgVy4ztR38BGNh215452y3U294YDBx6gLsPicrC58YHwz37MAQ6dGIHRgxJcxkR4m3f7k6CD2hr8VYHkN2-sQNw6csC-cBgbkfBXHDigK6sC_ZG0MhGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان تا دقایقی دیگه وارد نیویورک میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/148868" target="_blank">📅 01:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148867">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxDaBpg8rMnzD0rH8qQqcduIAc55ZDybNzSmwUHmBaS1DXzOxsQHuSJR1xE7KdrPTRk1G_sKuu68vNXRSZjMoHCZEw3ZeL_5QNegRmXRsGib6iIFOzOrum40FzI_GT2vakn0UzxUFJHqQrATH1SwNGTr5JZeTeg6Vx3K0hn9w-60xOUsLbz_VAbXCyCn7fhun7WuB5XcSOq9B7oyd5f78N3GdKXM6ySKQ064Od7LHND4hkITC1bUyjBFa0o-rN5e5a4mg-akJUlFGVrxrP2VU5sp6xQvYhpZcAJWRp8eViEQ1dOYt7daaoibPqcvVvruH8ohVkDKIBVJvJgAcXsdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صف پمپ بنزین کارگر شمالی تهران پس از مثبت ارزیابی شدن مذاکرات
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/148867" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148866">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
باراک راوید: کشورهای عربی در تلاش هستند تا جلسه‌ای بین ترامپ و رئیس‌جمهور ایران در این هفته برگزار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/148866" target="_blank">📅 01:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شلیک موشک به تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/alonews/148865" target="_blank">📅 01:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148864">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9VY8B3YgWknt5qZ3I3t-ry_UU5v8SmMLj-kSMrCcsU2iOk1LtO6rAZTfU5G9-iPtShLoduicZkykToeZNWdJypGKggBBGXhgk9TShqpsPMVjO6bDTFpVAL8EiXzYOJcbUfXc_WywczM5KseJ9dbzydbkF3luoHSFEhucpJpAh6k7AfCkw1qYSQ-W_Fvjv21gsWbTjfM4UqT741vk4Np72e9MClHXtY3024yNKxxKBXx7Fp2YtLP9gBdjr2oP4TJ3LuWHV36u286C52oohNW7eI4mC2UKOXL2MU9qRVwrThKPla4jK8BFPFKyf8gmKfFnDcKeVv_zvd8y6DTYH2JzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‌‏این عکس رو یادتونه!؟
🔴
‌‏۶ مهر ۱۴۰۳ ‌‏نتانیاهو بعد از سخنرانی در مجمع عمومی سازمان ملل اومد و از نیویورک دستور حمله به ضاحیه جنوبی بیروت برای ترور نصرالله رو صادر کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/148864" target="_blank">📅 00:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148863">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/لحظاتی پیش یک منبع آمریکایی که در نشست با هیئت ایرانی در نیویورک حضور داشته اعلام کرد:
ترامپ درخواست ایران برای رفع محاصره دریایی و هوایی را نپذیرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/alonews/148863" target="_blank">📅 00:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148862">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c7961ee3.mp4?token=naruiFfNS8slLxT-G2gs3OZ67yfyFkRZeOcVM6NovrpP7efd6fTwCq6w_h1uXvzt9Nx8FeE80FT0cB7YuAMSsGBh7PO0UZswkRzmBCgx98wj8oI1HtrTMEkxPhvmhyedOpxMlhlZw5kDH0RqC0toOtXiUv1GNs8xb5jr4YzltMpB4OHXIkjnsQpf52OCMkFRrTs9NanpXfSwKDAm4OUokodsNpje5wE-RTpDkdkosXOcWT7lE2ldWKNctTqz6cbeztI6bECFQXQsJmVM2AfG8D9AjygVPjjLoh4vATnUB7sDu3ShjQECURx33IYx6TtOL-zfSyVCO-E7ehH4vYneoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c7961ee3.mp4?token=naruiFfNS8slLxT-G2gs3OZ67yfyFkRZeOcVM6NovrpP7efd6fTwCq6w_h1uXvzt9Nx8FeE80FT0cB7YuAMSsGBh7PO0UZswkRzmBCgx98wj8oI1HtrTMEkxPhvmhyedOpxMlhlZw5kDH0RqC0toOtXiUv1GNs8xb5jr4YzltMpB4OHXIkjnsQpf52OCMkFRrTs9NanpXfSwKDAm4OUokodsNpje5wE-RTpDkdkosXOcWT7lE2ldWKNctTqz6cbeztI6bECFQXQsJmVM2AfG8D9AjygVPjjLoh4vATnUB7sDu3ShjQECURx33IYx6TtOL-zfSyVCO-E7ehH4vYneoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست وزیر قطر پریروز گفت ایران صلح طلب نیست و ... عراقچی هم الان دیدش و اینجوری پرید بغلش
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/148862" target="_blank">📅 00:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148861">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یک منبع آمریکایی که در نشست هیئت ایرانی حضور داشته است به الحدث گفته است:
فرص دستیابی به توافق محدود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/alonews/148861" target="_blank">📅 00:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148860">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
تتر وارد کانال 223 هزار تومان شد</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/148860" target="_blank">📅 00:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148859">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
تنگه هرمز بزودی از حالت ناامنی توسط ایران خارج میشه و محاصره دریایی هم لغو میشه
🔴
مذاکرات هم شروع میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/148859" target="_blank">📅 00:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148858">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
هم اکنون شاهد هجوم امت معکوس به عراقچی بابت دیدار با ویتکاف هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/148858" target="_blank">📅 00:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148857">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری و رسمی/از همین الان محاصره هوایی ایران اجرایی شد
🔴
هیچ پرواز خارجی‌ای انجام نمیشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/148857" target="_blank">📅 00:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148856">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تابستون هم تموم شد، ولی داغ دی ماه هیچوقت تموم نمیشه.  [@AloTweet]</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/148856" target="_blank">📅 00:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148855">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رسما وارد پاییز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/alonews/148855" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-148854">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: ما به دنبال جایگزین برای حکومت ایران نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/148854" target="_blank">📅 23:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رسانه MS Now:  به گفته یک مقام آمریکایی، ترامپ اخیراً حکمی را امضا کرده است که به‌طور رسمی و دائمی مارکو روبیو را به‌عنوان مشاور امنیت ملی ایالات متحده منصوب می‌کند.
🔴
روبیو پیش از این به‌صورت سرپرست این سمت را بر عهده داشت، اما اکنون این انتصاب رسمی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/148853" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTQ4KY-DnnpcvGSEpG1sr9-rZQ925zlGJn3tA_1WymLTtUD5r8jnunsx_bn1sZSTxJVbH3EwaMSnwlqSOUePpahlcg40-QmnuYTFzDaEvpxnQLPGaM4rkLGdsSV9j20nceeuR5mWe2MEdRcS-eym3cF6e1CSD0aa-SziddALNwZscZdlVe-CFmPA-QVQtAJLXadW89c02AbhjMbRROATBMMZFv8sISFJRgsn3WZ4GzogkLtoFmOsUeDUfy4VZkiKtmFoxFjueTKoz7hDUK5cnjqAcRVw-WsY0EBApVbBQE3bh8lg2scB1PCicwDjZCBdcaRoQwWDVx6wkEyPlpEZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای پزشکیان تا ساعتی دیگر وارد نیویورک می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/148852" target="_blank">📅 23:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نیویورک پست: رژیم ایران پسران ۱۲ ساله را برای آموزش در یگان‌های «ایثار» یه خدمت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/148851" target="_blank">📅 23:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148850">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
عجیب و ترسناک
‼️
🔴
هر وقت عراقچی فضای مذاکرات را مثبت ارزیابی کرده بود بلافاصله جنگ شروع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/148850" target="_blank">📅 23:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
الجزیره: فضای دیدار ایران و آمریکا مثبت گزارش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/148849" target="_blank">📅 23:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: ما ایران را منزوی کردیم
🔴
تمام کشتی های نیروهای دریایی ایران نابود شدند و شرکت های زیرساختی آنها نابود شده است.
🔴
پول ایران بی ارزش شده و تورم بسیار بالایی دارند.
🔴
ما ایران را ایزوله و منزوی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/148848" target="_blank">📅 23:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
واشنگتن پست به نقل از مقامات آمریکایی: پایان دادن به جنگ با ایران اولویت اصلی کاخ سفید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/148847" target="_blank">📅 23:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری / ترامپ درباره ایران: یا ما به یک توافق خواهیم رسید، یا این موضوع به سرعت و به طور کامل به پایان خواهد رسید.
🔴
این موضوع آنقدر سریع به پایان خواهد رسید که سرتان گیج خواهد رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/148846" target="_blank">📅 23:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: نیروی دریایی ایالات متحده تنگه هرمز را از مین‌ها پاکسازی کرد و ما توانستیم بیش از یک میلیارد بشکه نفت را از آن خارج کنیم!
🔴
نیروی دریایی ما عالی است و محاصره ما عالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/148845" target="_blank">📅 23:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148844">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ درباره اردوغان : دوست من از ترکیه، او شخصیتی قوی است. با او شوخی نکنید؛ او فردی سرسخت است.
🔴
او یک شخصیت فوق‌العاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/148844" target="_blank">📅 23:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148843">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبروکر ایکس چیف</strong></div>
<div class="tg-text">🏆
ایکس‌چیف برنده جایزه
«Best FX Service Provider»
شد!
جایزه «Best FX Service Provider» به پاس عملکرد برجسته در ارائه خدمات فارکس، کیفیت تجربه معاملاتی و تمرکز بر نیازهای معامله‌گران به ایکس‌چیف اهدا شد.
🎖
یک دستاورد تازه در مسیر حضور جهانی ایکس‌چیف؛ این بار در Forex Expo Dubai 2026، یکی از مهم‌ترین رویدادهای صنعت مالی جهان.
هر جایزه، داستان یک تفاوت است.
ایکس‌چیف؛ در مسیر بالاترین استاندارد خدمات فارکس.
@xChief_ir</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/148843" target="_blank">📅 23:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148842">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ : اقتصاد ایران در وضعیت بسیار بدی قرار دارد. ما ایران را از نظر اقتصادی کاملاً منزوی کرده‌ایم.
🔴
رهبران ایران باید قبل از اینکه خیلی دیر شود از این فرصت استفاده کنند.
🔴
ما معتقدیم بحران با ایران می‌تواند پس از انتخابات میان‌دوره‌ای آمریکا پایان یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/148842" target="_blank">📅 23:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148841">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ درباره تنگه هرمز: ما هر شب 25 تا 30 کشتی را هدف قرار می‌دهیم، گاهی اوقات در طول روز، اما بیشتر این عملیات‌ها در شب انجام می‌شوند.
🔴
این محاصره، قوی‌ترین چیزی است که تا به حال کسی دیده است. ما به آن "دیوار فولادی" می‌گوییم.
🔴
در حال حاضر، حجم نفت بیشتری نسبت به هر زمان دیگری از آغاز این درگیری، از طریق تنگه هرمز جریان دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/148841" target="_blank">📅 23:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148840">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / ترامپ: اگر شاهد فعالیت‌هایی در آنجا باشیم، ممکن است به کوه کلنگ حمله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/148840" target="_blank">📅 23:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/148839" target="_blank">📅 23:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148838">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/148838" target="_blank">📅 23:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148837">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما آن‌ها را به شدت تحت فشار قرار داده‌ایم، اما در این باره اغراق نمی‌کنیم.
🔴
امیدوارم آن‌ها کاری انجام دهند که واقعاً به نفع مردمشان باشد، و من فکر می‌کنم که آن‌ها در واقع این کار را انجام خواهند داد، من واقعاً اینطور فکر می‌کنم
🔴
گزینه دیگر، گزینه‌ای قابل قبول برای هیچ‌کس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/148837" target="_blank">📅 23:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148836">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26bb6cce1.mp4?token=X7wKEfLaxv2jjlk-wxJSXvfXE168iklFymBiN1eC5RYOw-cHizauATmWjyDoF_mBFHYMtzpXFWwl91Nevb277rJeszEX1qwDl36QyrrvNAnuvoyLnCLGzo0YeGUKLgWHLNAV0T9bFQ12KEcIb1dVs4XaV48TSQKqkihE7jIu3b0FrKAsudPCDfmBewellY6-zE3DCSGM0WoO28bFPf73E2olrCxmkQHQgh5GuX1xQs52zpn7pR39duuu8gzR7A49-t772NLpGIuRBdJSOnSIs_SXzrHiwR0oR1l21jr3dPEegNEa05yv95pbqpLzzPNwNT5VwLtdoqKGAEFH723JRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26bb6cce1.mp4?token=X7wKEfLaxv2jjlk-wxJSXvfXE168iklFymBiN1eC5RYOw-cHizauATmWjyDoF_mBFHYMtzpXFWwl91Nevb277rJeszEX1qwDl36QyrrvNAnuvoyLnCLGzo0YeGUKLgWHLNAV0T9bFQ12KEcIb1dVs4XaV48TSQKqkihE7jIu3b0FrKAsudPCDfmBewellY6-zE3DCSGM0WoO28bFPf73E2olrCxmkQHQgh5GuX1xQs52zpn7pR39duuu8gzR7A49-t772NLpGIuRBdJSOnSIs_SXzrHiwR0oR1l21jr3dPEegNEa05yv95pbqpLzzPNwNT5VwLtdoqKGAEFH723JRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره قایق‌های مخدر در جلسه سپر آمریکا: به ما اطلاع دهید و ما آن‌ها را از بین می‌بریم.
🔴
یا خودتان آن‌ها را از بین ببرید. من این را حتی بیشتر دوست دارم.
🔴
اگر نمی‌توانید، ما به جای شما این کار را انجام می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/148836" target="_blank">📅 23:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148835">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d942437d.mp4?token=FM8ktktfaUs3ySfttha8NEPiP8cupq8fweRpIioQxiPlyE1mUurBeHKMT4n__3QN-UK7XnBm4bIvrN-4MwvOcN1SBJGywhucU9AJS8rcEQqS2pEbH6gPY0hBVpxmjeFzUsEXERj90amUnxyOdgSs2Ol7Sz9fNMZ8ScZD1QKZIQzd28s78Mb19BcglqywjYZ6p7vzMhyJ2sX9T6IYNsIM-cJney__Yq6sQOxrA3fvT291Tb6DBDBZK-r7eLgLCGMtbOv2uLx4FkdvbXnMwUSRO-ThtLOIlODr2o6bTPpZvKYm9Y4hC4xv6pogNYc5Gs8AlLz2ekeUrKjnD8LpyoGeVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d942437d.mp4?token=FM8ktktfaUs3ySfttha8NEPiP8cupq8fweRpIioQxiPlyE1mUurBeHKMT4n__3QN-UK7XnBm4bIvrN-4MwvOcN1SBJGywhucU9AJS8rcEQqS2pEbH6gPY0hBVpxmjeFzUsEXERj90amUnxyOdgSs2Ol7Sz9fNMZ8ScZD1QKZIQzd28s78Mb19BcglqywjYZ6p7vzMhyJ2sX9T6IYNsIM-cJney__Yq6sQOxrA3fvT291Tb6DBDBZK-r7eLgLCGMtbOv2uLx4FkdvbXnMwUSRO-ThtLOIlODr2o6bTPpZvKYm9Y4hC4xv6pogNYc5Gs8AlLz2ekeUrKjnD8LpyoGeVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
استیو و جارِد امروز جلسه‌ای بسیار سازنده با دو میانجی از ایران داشتند. خواهیم دید که نتیجه این جلسه چه خواهد بود.
🔴
به نظر من، یک حرکت قوی برای رسیدن به توافق وجود دارد. این چیزی است که ما از همه می‌شنویم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/148835" target="_blank">📅 23:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148834">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری/ترامپ: شتاب قابل‌توجهی برای دستیابی به توافق با ایران وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/148834" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148833">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RQhpgNV9zF4EvvXHbc8uCGhhyxvssqC7i6_EkEPUZUY5mht7k19AZbJ2QbU2VDNpt8RQFNlWZ7Xod9qOqBd7J8oK_0B9ZpMa4Agf-JQmRLvfR0X4NVVx6fHzBHrjK8SHq9AlU7DbzM0xyXWTG2YilI5qg3nbU3ZOEOIvMaBufSivtrw30yARxW4pIVFRIgZKgS8aV8wFJ2fpuk3vtb7WefYoYi1NgYoifgIVh_SDqF3DzpxWpPHEFVlDp5bMw_uh7S1W3ybfliaDi4jnP8NU8bzqsItb_eop0OuEbCM9SMOFOxzMhtQmHWo7dhvAwgvlm_Nja8ah5zNlnuocHMS43Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما
: با خایه مالی آمریکایی‌ها، عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/148833" target="_blank">📅 23:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148832">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
مدیرعامل شرکت ارتباطات زیرساخت:
۱۰ درصد ترافیک اینترنت ایران به استارلینک رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/148832" target="_blank">📅 22:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148831">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ ریاست جلسه‌ای خصوصی را بر عهده گرفت که در آن نمایندگانی از کشورهای عضو شورای همکاری خلیج فارس، مصر، سوریه، ترکیه، عراق، اردن و لبنان شرکت داشتند. این جلسه در حاشیه کارها و فعالیت‌های مجمع عمومی سازمان ملل متحد در نیویورک برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/148831" target="_blank">📅 22:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148830">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
العربیه: ویتکاف به طور مستقیم و بدون واسطه با هیئت ایرانی ۳ ساعت گفتگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/148830" target="_blank">📅 22:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148829">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اتحادیه اروپا تحریم‌های روسیه را برای سه سال دیگر تمدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/148829" target="_blank">📅 22:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148828">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
یوسف بهرامی فعال اقتصادی مدعی شد عباس عراقچی با استیو ویتکاف دیدار ۱۲۰دقیقه ای  داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/148828" target="_blank">📅 22:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148827">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
اسرائیل هیوم به نقل از منابع آمریکایی:
جلسه از پیش برنامه‌ریزی شده آمریکا با تیم ایرانی عراقچی، با حضور نخست وزیر قطر، در مورد از سرگیری مذاکرات و باز کردن تنگه هرمز بحث شد؛ هیچ توافقی در مورد مسائل مورد اختلاف حاصل نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/148827" target="_blank">📅 22:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148826">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
روزنامه نوبنیاد به خاطر حضور عراقچی تو سازمان ملل اونو «بی‌غیرت» خطاب کرد و خواستار استیضاح و برخورد با وی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/148826" target="_blank">📅 22:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148825">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ویتکاف: دیدار با ایرانی‌ها خوب پیش رفت و در حال حاضر احساس بسیار خوبی دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/148825" target="_blank">📅 22:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148824">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
خبرنگار i24: استیو ویتکاف و جرد کوشنر، مقام‌های آمریکایی بودند که امروز با هیئت ایرانی دیدار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/148824" target="_blank">📅 22:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148823">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpNiO9owtqtIMIRHYK04SGMGV-x3oawvMZXh-jmOAG77Lmzoz9bIfsWnLcaNUwvn_IcPHOJobHaR8qqh9PHMBdxGHSvsQRGD5ybl0hxEgm_OXppaYN2vUgwvoPbk0G1mZYYATTLx0121FSVHGf1tCHg-r5GVXVhZGVKfYi_X_wowsFREA0zySG5ERiHN6TJm8D1Zqww0EEamoJCfn6DT9baji-gNbxVCTxdGe0Ub1snFvgIVezCnmqBqtJmCT5tAnKcigrVJjJ768z9V4zjKIlFh_new4lzGwc3fvIs1aj_DpJSsiuBwiR7D4t9ZIhzqvzYUaL7HWEQAzjzJalcjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش سنگین قیمت نفت بعد از سخنان ترامپ درباره ملاقات با ایرانی ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/148823" target="_blank">📅 21:53 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

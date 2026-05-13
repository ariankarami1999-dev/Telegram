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
<img src="https://cdn4.telesco.pe/file/K6c6mUwPQd0sfinlMqfBSi3WaD4Y5SSte_QDDGR9Jv81crmdO3tPxy1smpU047XvXtd_7QiSi4ihUsrlN76BIKkED1TMQhlaN0hxb8EP76eN8Fel5frFo9yo3k18NnJg4EFbCwx2ABToIsgRa88a9Mm6NAFmpL2_IW2ZCR3r9nn4h06icNoxWD7S1ikGLDJBUlNzyhwW8Kicu0pi-cZIIBOLQB4BxKZcnl3aEre8vhpkyil1ctzsxep8YPiHuHMwEizspbck60qA3avqE3WN50UlP2aQr8SW5Rxhfynn-Hw7bx9NbqtZCqAFlmqGIExAgGU0Yq4XEbneGATKsFmV1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 12:53:21</div>
<hr>

<div class="tg-post" id="msg-131595">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
ترامپ رسما اومد گفت انقدر صبر میکنیم تا ایران تحت فشار مجبور به توافق بشه.
❗️
یعنی ممکنه تا شهریور تو همین وضعیت بموییم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 45 · <a href="https://t.me/SorkhTimes/131595" target="_blank">📅 12:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131594">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
طبق شنیده‌ها سروش رفیعی برای حفظ آمادگی نزدیک به یک ماه است همراه یک تیم دسته سومی کانادایی تمرین میکند و ممکن است فصل آینده در کانادا به میدان برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 267 · <a href="https://t.me/SorkhTimes/131594" target="_blank">📅 12:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131593">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🔴
شنیده‌میشود محسن‌مسلمان فوق ستاره سال‌ های نچندان دورباشگاه پرسپولیس بزودی به کادرفنی این تیم برای فصل بعد رقابت‌ها اضافه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 381 · <a href="https://t.me/SorkhTimes/131593" target="_blank">📅 11:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131592">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj56zhQg7hZAqvT0vAu_sOHB6nnsnzUjeYPT98UmYI5tsqccCJzYGsf9dpGslb92gyRsQ5Fe4vz-p-mN03xxsmOoMTcxb0OG9bCkBiU2oelfeYDS9VdjD2ix4Lk1GtMqb2zMi2gEwzavhDBiV1V7jUnATyWmFkRfW3qvb8nHgcTAE5y1VDhjWgJ0v0q4z0ZPZsP4tFvvxMH82v51Bwt3Xfj2i-GPt28EeRVEjaLY7PeWsyboA2aOe4wXxe5dCMxgibg2wawtfd3xWTd45Q3imqvsAawwCAt1RbtBdpBJY-A9Yc-njNpd3SAME7xRbr3GaPGlWQL-KrahLl2kL0eJsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پپ گواردیولا:
من بی طرف نیستم من طرفدار فلسطین هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 391 · <a href="https://t.me/SorkhTimes/131592" target="_blank">📅 11:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 1.4T
10 گیگ 2.4T
20 گیگ 3.6T
40 گیگ 5.7T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 467 · <a href="https://t.me/SorkhTimes/131591" target="_blank">📅 10:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
🔴
مارکو باکیچ تابستان گذشته با قراردادی «۱+۱» به پرسپولیس پیوست که طبق بند الحاقی قرارداد، فعال شدن سال دوم منوط به حضور او در ۶۰ درصد مسابقات رسمی فصل اول بود. با وجود مصدومیت این بازیکن در اواسط فصل، طبق ماده ۵ آیین‌نامه نقل‌وانتقالات فیفا، مدت زمان مصدومیت از مجموع مسابقات قابل محاسبه کسر می‌شود؛ به همین دلیل باکیچ از نظر حقوقی به حدنصاب ۶۰ درصد رسیده و قرارداد فصل دوم او به‌صورت خودکار فعال شده است.
🟥
در نتیجه، قرارداد دوساله این هافبک مونته‌نگرویی قطعی و لازم‌الاجرا محسوب می‌شود و ادامه همکاری او نیازی به تمدید یا توافق جدید ندارد. همچنین اگر پرسپولیس قصد کنار گذاشتن این بازیکن را داشته باشد، احتمال محکومیت باشگاه در دادگاه CAS بسیار بالاست و باشگاه باید کل مبلغ قرارداد را پرداخت کند. از سوی دیگر، تاکنون هیچ نوتیس فسخی از سوی باکیچ به باشگاه ارسال نشده و تمام بحث‌های مربوط به «مشروط بودن» قرارداد، با مفاد توافق و استانداردهای فیفا همخوانی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 535 · <a href="https://t.me/SorkhTimes/131590" target="_blank">📅 09:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131589">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o44Fd3ETaNPNukEWSnlsIPq1lm-eKYB8Vgz_JcyPFADXgM4WozR6KyqkVmLSeUnEq977E0tp2QiKizeEWa3oXB_vL-rRjPLHNIgZnZj-NDFM310_v5vq-7xSbsTEbuut04GnuPd1srzGnYd7rp6XkyZrYZ0xR7JWlsSvEnB0t5_WmUMO5060heGUgmyojwrsUT-I7dzGAVyGYl0hWRDwuL-h9I8U2XnL9Jnw8PHK5qoryfIo_0FFf3RpViRbZ_o0F1Ufw2p1n6e48uOzjqztuR_fpzcn6vFSbwIb2_OGw1lTz-2j5IeScmobU9ZrS3diFQpnVvSVeNwBf0rnp_8EpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/SorkhTimes/131589" target="_blank">📅 01:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131588">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
همین زلزله رو کم داشتیم وسط این همه تورم،جنگ‌ و بدبختی، فیلترینگ و قطعی اینترنت!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 631 · <a href="https://t.me/SorkhTimes/131588" target="_blank">📅 00:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131587">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
جزییاتی از زلزله شدید تهران   بزرگی و شدت: ۴.۶   محل وقوع: مرز استان‌های تهران و مازندران، حوالی پرديس   زمان وقوع: ۲۳:۴۶ عمق زمین‌لرزه: ۱۰ کیلومتر ۸ کیلومتری پرديس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/SorkhTimes/131587" target="_blank">📅 00:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131586">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bs5HOPiXHyPWAgafqnMT7N7N6EtKfEiL1jUdbaiqAkcBeZWP_4JRENAw93a557zXNri3dorw2eEJKt2XqDAg9VX5rcUWY8O1zj7gtEhf8Fs08QqSaONETUdmp7Jkhedmj6Lf_2vM4ED3rMzfAzPr07KozclgtfOy73lbQc-Bpwt17gFRbXeEt6xukbFhfy6Bg208BccBHEjI-miefooW1LM9iVyfsQDT-OT8XmScUtVWyBODgQx5IlReQlvOB4rNzfe5PzeuGMD5Ia6TAEPMucmSZXovY_bBOqghKFTc4LL-1ycpg7KFgt9R6vfKEgZnE2C2h_wdFntrixZCZiiOgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جزییاتی از زلزله شدید تهران
بزرگی و شدت: ۴.۶
محل وقوع: مرز استان‌های تهران و مازندران، حوالی پرديس
زمان وقوع: ۲۳:۴۶
عمق زمین‌لرزه: ۱۰ کیلومتر
۸ کیلومتری پرديس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/SorkhTimes/131586" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131585">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
کانال ۱۲ اسرائیل:
🔴
انتظار می‌ره که ترامپ بعد از بازگشتش از چین در پایان هفته، تصمیمات نهایی و جدیش رو درباره ایران بگیره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/SorkhTimes/131585" target="_blank">📅 22:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131584">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/SorkhTimes/131584" target="_blank">📅 22:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131583">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
درگیری لفظی چندین خبرنگار با فاطمه مهاجرانی بر سر قطعی اینترنت
🔕
مهاجرانی: ترامپ گفته آتش‌بس به تنفس مصنوعی وصل است، کشور در جنگ است! امنیت مردم مهم است و تا وقتی سایه جنگ از کشور دور نشود وضعیت اینترنت به حالت عادی بر نمی‌گردد!
💬
وقتی مردم اینترنت ندارن…</div>
<div class="tg-footer">👁️ 750 · <a href="https://t.me/SorkhTimes/131583" target="_blank">📅 22:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131582">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=UN3nUDvT5SvRXnn1mgR5iXUEDMh5mqSoiOKfAB4xby0qGbM23eNvSulpvLH-WbCHaTkTFLePEa9XNnh3LPc-y7zS1HojHN4htwu14c_J3Wt2mL166l1ywXIKoAMG8kNcHj7RmIX3Y7ePYHS9Hx3MdmHebnJHrgWoqtlMnwJifEv6mh4W4FrvJ8GP9107BWxRyJFQQA6U47dA9QBohBhrwV1X8aOvfMZKrPYSmDHrsXZt6F5RAXsBqoSRbWNFQCj_8bX2O9TjJQe0mlm2NPbb4l1vt6nOpHUP7c7eL-SkNNhHUYN_pITeN7pDMPeeZSHkJplNvF_0xGchBSnTh803u0NDKxgq_wtI79xvFsm7kTEzaWTwmNMG9F6--71UQFWHJB8xClKA1ovcIYfMviAk-4tzYouMYdttAP5DfVmCNjfOfX67VNcmooCt3Ot5AMqb5uW5F0QJ54mfc76QYOBBv7skbmJHxwNUBRDmSDEhp5XJlRM4LGMes0m84uAd8P5pzvjAoIT5NWjeUBUA--EOl5he3RLrblLdfs29k2EWCFfQgXK5_02DXVHBKzH1XY4UTHRmQ11ZKFwMYG35l-8MU370qTgqz26DE_OrY8LHrnI6Wtn3txRodWtodWJ_Fk6pizGBLQIKqxFAB-cxnEi-J8LUdQSIkxaUnJHJzddcoKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=UN3nUDvT5SvRXnn1mgR5iXUEDMh5mqSoiOKfAB4xby0qGbM23eNvSulpvLH-WbCHaTkTFLePEa9XNnh3LPc-y7zS1HojHN4htwu14c_J3Wt2mL166l1ywXIKoAMG8kNcHj7RmIX3Y7ePYHS9Hx3MdmHebnJHrgWoqtlMnwJifEv6mh4W4FrvJ8GP9107BWxRyJFQQA6U47dA9QBohBhrwV1X8aOvfMZKrPYSmDHrsXZt6F5RAXsBqoSRbWNFQCj_8bX2O9TjJQe0mlm2NPbb4l1vt6nOpHUP7c7eL-SkNNhHUYN_pITeN7pDMPeeZSHkJplNvF_0xGchBSnTh803u0NDKxgq_wtI79xvFsm7kTEzaWTwmNMG9F6--71UQFWHJB8xClKA1ovcIYfMviAk-4tzYouMYdttAP5DfVmCNjfOfX67VNcmooCt3Ot5AMqb5uW5F0QJ54mfc76QYOBBv7skbmJHxwNUBRDmSDEhp5XJlRM4LGMes0m84uAd8P5pzvjAoIT5NWjeUBUA--EOl5he3RLrblLdfs29k2EWCFfQgXK5_02DXVHBKzH1XY4UTHRmQ11ZKFwMYG35l-8MU370qTgqz26DE_OrY8LHrnI6Wtn3txRodWtodWJ_Fk6pizGBLQIKqxFAB-cxnEi-J8LUdQSIkxaUnJHJzddcoKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صالح حردانی میگه ملی‌پوش‌ها از سربازی معاف بشن تا با روحیه بهتر فوتبال بازی کنند!!!!
◀️
شما چه گلی به سر کشور و مردم زدید که درخواست معافیت دارین؟ کدوم قهرمانی رو آوردین که اینقدر وقیحانه درخواست معافیت دارین؟ چرا یکبار درخواست شما، رویکرد مردم نیست؟ چرا همه چی رو فقط برای خودتون می‌خواهید؟
❌
جز اینه که هیچ جای دنیا چنین پولی رو به شما نمیدن؟ هیچ جای دنیا به چنین ثروتی نمی‌رسیدید جز ایران!!! باز درخواست معافیت سربازی دارین؟
🔴
چه تفاوتی با یک جوان کارگر ۲۵ ساله داری که اون باید بره سربازی و تو نباید بری؟
⚠️
تازه سربازی شما که مثل بقیه مردم نیست، میرید تیم ملوان یا فجر و بازهم فوتبالتون رو بازی می‌کنید. خبری از پادگان نیست. چرا همیشه طلبکارین و سیرمونی هم ندارین؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/SorkhTimes/131582" target="_blank">📅 21:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131581">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 732 · <a href="https://t.me/SorkhTimes/131581" target="_blank">📅 21:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/SorkhTimes/131580" target="_blank">📅 21:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131579">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f2cd4206.mp4?token=b2zCNzUjMe1YVxh9wuyerjVPcDT4o-_yjQiMiUUxZ3HiVFG-evHDZhr7L66MTohIbjLxQQOgSYgAUwAzrVw-tNJWo2FWpdeFpY-XykOMNj5g1Hl198Fghlm7TQ3qXALo622C5q6Tak14gJtPGj4aelGyBkomhIxKXEo4wG1SZymPnEPX2h4zkjO0yD4pxzJ8nmBRN5l2lzYJWz9iHbuRnxUl3Q-YjHO5jBHv0LDZKflKg9zZgWZOpBMzBjOrpPLIpWNwb3Q6asSSpjFD9jJ8rYFhJ1_18O1tUnUEiPmFa2tPAxC0sBjl1oDXKGFxSJRjO0aQAorHKzU72hzrq_c0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f2cd4206.mp4?token=b2zCNzUjMe1YVxh9wuyerjVPcDT4o-_yjQiMiUUxZ3HiVFG-evHDZhr7L66MTohIbjLxQQOgSYgAUwAzrVw-tNJWo2FWpdeFpY-XykOMNj5g1Hl198Fghlm7TQ3qXALo622C5q6Tak14gJtPGj4aelGyBkomhIxKXEo4wG1SZymPnEPX2h4zkjO0yD4pxzJ8nmBRN5l2lzYJWz9iHbuRnxUl3Q-YjHO5jBHv0LDZKflKg9zZgWZOpBMzBjOrpPLIpWNwb3Q6asSSpjFD9jJ8rYFhJ1_18O1tUnUEiPmFa2tPAxC0sBjl1oDXKGFxSJRjO0aQAorHKzU72hzrq_c0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
گلزنی علی‌علیپور در بازی درون‌تیمی ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 711 · <a href="https://t.me/SorkhTimes/131579" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131578">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🔻
فیفا یه قانون تصویب کرده که بازیکنای خارجی که ۳ سال سابقه حضور تو لیگ یه کشور رو داشته باشن، میتونن واسه تیم ملی اون کشور بازی کنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/SorkhTimes/131578" target="_blank">📅 20:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131577">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs8fk__1ltwsRUPomzNHSt8exHklrmNrtTJ0DbuOnQzfKbVhoRVJ8kULoomw6FWHM_NpYgrGZn7Bk9b4iWtDarmV0HSgcZ4bsxj4esmBk-08YAL5lw-bJHE8dFSlDH6a2fqRbm0jloU48aoqDBIFcqLIzncqNVmP18PytEBy4WQ_Eni82V26oMIC1O0eYVoNVGin6gcESmiy4UT221f7fmbEb0aH1J3TYqme7oX-r6gzUw8AwY4dy3fhS1CvZWG_Rv64BIYddtSjmJv7BJeEs7ncdOZ7YHIFhiqVh6J9cFnX6h43ftSndzxSs_Z4IOHi7Fmb16ySzkYeTGDCoyeB1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
پزشکیان توییت زده قول داده اینترنتو وصل کنن
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 750 · <a href="https://t.me/SorkhTimes/131577" target="_blank">📅 20:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131575">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
باشگاه پرسپولیس کارهای تشکیل تیم دوم خود را انجام داده و «پرسپولیس ب» در لیگ دسته دوم فعالیت می‌کند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 765 · <a href="https://t.me/SorkhTimes/131575" target="_blank">📅 18:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131574">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚪️
تاج: تیم‌های راه‌یافته به لیگ نخبگان و لیگ قهرمانان را انتخاب خواهیم کرد
🔺
شاید بتوانیم مهلت معرفی تیم‌ها را یک ماه عقب بیندازیم.
🔺
۱۴ تیم مخالف برگزاری ادامهٔ لیگ‌اند؛ موافقان پرسپولیس و گل‌گهر هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/SorkhTimes/131574" target="_blank">📅 17:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131573">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSG_q9t_131Cfj-TtqUDLQIjaDYCYMmzvmMNBacWK09fy6uFhBdblFq5B-OjmHms9uXsXsbTDCC-9y2hsun5Q--LeP7hnPvYZY4VwqniMCgTLgW9EDhaUc09hHsuMlyjihmjLiZsdHeyV5Er6BADa9ruKsfxDbunqbaW-5mFZYsmn8Semci4SdEM_QOHnfdj9Jw2iiOA4uHAfJfrKxsoVjxSyl1uudpvA06mQe8-vfl1ovQXV6Cr8rMbtf9h3ESLLgOPyxbabeVVCYkrJAcXtG3sAKXCwRRYUtFFVoItg2jnPrP_oOj90pw-LesX9edCEC2Y0ahq665pZMkqMDTwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اختلاف میلاد محمدی با مدیران باشگاه پرسپولیس تنها 3 میلیارد تومن است و مدیران باشگاه پرسپولیس قصد دارند با پرداخت این مبلغ قرارداد محمدی را تمدید کنند
/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 737 · <a href="https://t.me/SorkhTimes/131573" target="_blank">📅 17:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131572">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس خواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 634 · <a href="https://t.me/SorkhTimes/131572" target="_blank">📅 17:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/SorkhTimes/131571" target="_blank">📅 17:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131570">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw-2w1AqUtcj7_fz_xh8C9c-VcrGWZ_kzxfRIAHCHQ3NAUi_BSMt_geov0zmQRiRr5EH-_zvHBtLd-fjKgr_kmB84zu-cyPmM0slk96a_yu6qZ6oXXeAnEfYYLoZCHlxjmqXhyqthGN8TXDm4Xb-I1JxHAuZRphU9D6PHJAzWJlwfgi5bhDBw7g2WGgP1cVfkLNlQMjbC0YUTYd1JZBS55dqoLFfsdf_crT6aBwR-ml4S36FeVL3uCg5xloXsQRhSBIIXOB7miWujXBR3UCBe_dkeYNav8W5aCJMbDBw7hYuqp_w-NPaYkaXMcqpzwAJ8ydqU8m6gBwwkRgUhDMItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شباهت عجیب لوکاس برالدو و محمد خدابنده لو ستاره های خط هافبک پرسپولیس و پاریسن ژرمن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/SorkhTimes/131570" target="_blank">📅 17:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 627 · <a href="https://t.me/SorkhTimes/131569" target="_blank">📅 17:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131568">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🔴
سهیل صحرایی ، فرزین معامله گری، علیرضا عنایت زاده ، محمدحسین صادقی ، محمد امین قزوینه و محمد گندمی به اردوی تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/SorkhTimes/131568" target="_blank">📅 17:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131565">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚪️
ترکیب دو تیم تیم‌ملی برای بازی درون تیمی
◽️
تیم سفید: علیرضا بیرانوند، دانیال ایری، حسین کنعانی، علی نعمتی‌، رامین رضاییان، روزبه چشمی، امید نورافکن، هادی حبیبی‌نژاد، مهدی محبی، آریا یوسفی و علی علی‌پور
🔻
تیم قرمز: محمد خلیفه،‌ شجاع‌ خلیل‌زاده، عارف آقاسی، صالح حردانی، احسان حاج صفی، عارف حاجی عیدی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، امیرحسین محمودی و کسری طاهری
⏰
ساعت ۱۸:۰۰
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 767 · <a href="https://t.me/SorkhTimes/131565" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131564">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
درگیری لفظی چندین خبرنگار با فاطمه مهاجرانی بر سر قطعی اینترنت
🔕
مهاجرانی:
ترامپ گفته آتش‌بس به تنفس مصنوعی وصل است، کشور در جنگ است! امنیت مردم مهم است و تا وقتی سایه جنگ از کشور دور نشود وضعیت اینترنت به حالت عادی بر نمی‌گردد!
💬
وقتی مردم اینترنت ندارن کسب و کار ها با اینترنت پرو چیکار میخوان بکنن رونق کسب و کار اینترنتی به مردمه.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 773 · <a href="https://t.me/SorkhTimes/131564" target="_blank">📅 16:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131563">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
شهبازی مجری شبکه 2 : اگه اینترنت،تلگرام بدون فیلتر و مستر کارت میخواید و این چیزا براتون مهمه،برید همون سوریه،عراق و افغانستان
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 816 · <a href="https://t.me/SorkhTimes/131563" target="_blank">📅 16:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131562">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
پزشکیان: نمیذاریم بعضیا از وضعیت جنگی کشور سواستفاده کنن و برای مردم مشکلات اقتصادی و معیشتی به وجود بیارن!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 766 · <a href="https://t.me/SorkhTimes/131562" target="_blank">📅 16:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131561">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
وزیر جنگ آمریکا: اگر لازم باشد، ما برنامه‌ای برای تشدید اوضاع در ایران داریم!!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 790 · <a href="https://t.me/SorkhTimes/131561" target="_blank">📅 16:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131559">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_lrepUCFUU2-fJ1XI-tSGlIegEFXZTYzrf7UItWRFLOulY1oy6pj362BBCceBZ_mgLuix9u65qpYyo22drZvnWajZ5mKqTHXjzj98ZKOi7stTCav04KMzaXENrg0GgjD5aYxHdwUdE9dnDB-FQAeoDM5thqPUH0m5BhJkTcH_6BLZnCfTmUT8-y5jLusT4AJR_0xRxQrfq9sxxhSyAv4HmuqpIQokttqUwNWrwdUkEvX8YisVLBiu0BjXHTm6xNIyD3LjLD8Z4Eu35AHcaHKDSJbScI2jDiveLkGbxJdhnGe8f8glODz5NZ6QFbLobY7Fn2Vw3TcNF8QgmOiZXRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/SorkhTimes/131559" target="_blank">📅 01:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131557">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGuaQrmkrUR13g5gf1UCJCbc2WDXjwfIzzVw6sBS_2njw5Qqo_3cdBZyM9NW71vYPqVOKid-oIDYpvPzsWRBt5sx8rKkIxETux4FDf6hwfahBFdqZRF6X9er374M0Hut2FL6oQqxN8oOGfYxtdOFTIqaCQLdsmld7yKzkTzLK8wh2sTVr19K0zbf4HHUAZ8s0RRsqFec5g61Ljeua6CSGBEJD6EJEdJDOxDQcy2GMwqb2KP693CU1HKUZpP7Qudw4oiK60JZQJrWlxXI8QIq9TkP3NVC9_TjEIRvC_n1xd4kc1YCTVgmmFB8CdEl52pPLtMAxJAbEf6No_nJxZtZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سپاهان مجوز حرفه‌ای می‌گیرد؟
🔺
کنفدراسیون فوتبال آسیا (AFC) به درخواست فدراسیون فوتبال ایران برای تعویق در معرفی نمایندگان این کشور در رقابت‌های آسیایی پاسخ منفی داده است. این موضوع به شدت بر وضعیت نمایندگان ایران در لیگ قهرمانان آسیا تأثیر خواهد گذاشت. سپاهان،…</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/SorkhTimes/131557" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131556">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🟡
سپاهان مجوز حرفه‌ای می‌گیرد؟
🔺
کنفدراسیون فوتبال آسیا (AFC) به درخواست فدراسیون فوتبال ایران برای تعویق در معرفی نمایندگان این کشور در رقابت‌های آسیایی پاسخ منفی داده است. این موضوع به شدت بر وضعیت نمایندگان ایران در لیگ قهرمانان آسیا تأثیر خواهد گذاشت. سپاهان، یکی از باشگاه‌های مطرح کشور، به دلیل مشکلات مالی و عدم توانایی در تأمین شرایط لازم برای دریافت مجوز حرفه‌ای، در معرض خطر قرار دارد.
🔺
بعد از آسیب جدی به کارخانه فولاد مبارکه، سپاهان با مشکلات مالی جدی رو به رو است و هنوز نتوانسته مطالبات این فصل بازیکنانش را تسویه کند و احتمالا هم با توجه به میزان خسارات وارده، حداقل تا پایان سال بعد، قادر به تسویه طلب مربیان و بازیکنان داخلی و خارجی اش نخواهد بود که همین موضوع قطعا بر روند مجوز حرفه این تیم تاثیر منفی خواهد داشت.
🔺
از سوی دیگر شرایط اقتصادی صنایع مادر باعث شده وزارت صمت نیز محدودیت‌هایی برای هزینه‌کرد باشگاه‌های صنعتی در نظر بگیرد؛ موضوعی که می‌تواند برای سپاهان، گل‌گهر و چادرملو دردسرساز شود.
🔺
نکته قابل توجه دیگر هم این است که با توجه به وضعیت منطقه و کارشکنی مسبوق به سابقه از سوی کشور های حاشیه خلیج فارس
،
قطعا بازی ها به سمتی خواهد رفت که رنگ بوی ورزشی نخواهد داشت و این بازی ها یک میدان است برای دفاع از نام و اعتبار ایران و حفظ ابروی ایران بسیار مهم است.
🔺
در این شرایط، انتخاب نمایندگان مناسب برای حفظ اعتبار فوتبال ملی اهمیت ویژه‌ای دارد، تصمیمات فدراسیون، در روزهای آینده می‌تواند سرنوشت فوتبال ایران را رقم بزند و بر روند آینده باشگاه‌ها تأثیرگذار باشد/ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/SorkhTimes/131556" target="_blank">📅 00:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131555">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فوری ؛ ایران به شورای امنیت سازمان ملل اطلاع داده است که در صورت اعزام زیردریایی هسته‌ای آمریکا به خاورمیانه، سطح غنی سازی ۱۰ تن اورانیوم باقی مانده را به ۶۰ درصد خواهد رساند
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/SorkhTimes/131555" target="_blank">📅 00:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131553">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
🎙
میثاقی: امیرحسین محمودی با 5 بازی لیگ برتری جوری درخشیده که الان داره میره جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/SorkhTimes/131553" target="_blank">📅 00:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131552">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
محمد انصاری که در تیم جوانان ایران به عنوان یکی از دستیاران حسین عبدی فعالیت می‌کرد هم اکنون یکی از گزینه‌های جانشینی او در این تیم هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/SorkhTimes/131552" target="_blank">📅 23:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131551">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
میثاقی: کارهای اعزام تیم ملی به آمریکا برای حضور در جام جهانی در حال انجام شدن است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/SorkhTimes/131551" target="_blank">📅 23:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131549">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🛜
معاون رئیس‌جمهور: نظر دولت بازگشت اینترنت به وضعیت عادی است
🔹
حتی در شرایط جنگی هم بستن اینترنت راهکار درستی نیست، چرا که دیدیم وقتی اینترنت کامل بسته بود هم ترورها ادامه داشت
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/SorkhTimes/131549" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131548">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
ترامپ:آنها تسلیم خواهند شد... من با آنها معامله خواهم کرد تا زمانی که به توافق برسند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/SorkhTimes/131548" target="_blank">📅 18:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131547">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
ترامپ:
آنها تسلیم خواهند شد... من با آنها معامله خواهم کرد تا زمانی که به توافق برسند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/SorkhTimes/131547" target="_blank">📅 18:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131544">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Crd-C6dUf4QB3H9kOv_9nqks26CL6W8-NNPvKbl1qPYRwJWfh_j4F-VHWZo9OcSAs-VP23Z-DJPX0inCw0prRToMDFSGbFSn10HCNxdVmU9Z2SS0VR9QL35_4yl7223YHYsf9S0iTrIcowppRZwZrfbe7P2ajg2f-lbqucZZbCaBtjtKZWVCyUC5qs6wLmB0n32qcz0dOxN9KrmwMsuYrtYgo5PtNfA2TMu6pptk7NsRG6LhrpBgaybGjRWIdrKfKwVq3xrLshuYec1os0U4i3_c0P6M61iThyuWpq0aVbovlCQt8EVvIpome5IaqYRvXoUC0mrm5wcp9j4FXymzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/SorkhTimes/131544" target="_blank">📅 17:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131543">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 773 · <a href="https://t.me/SorkhTimes/131543" target="_blank">📅 16:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131542">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
سروش رفیعی فعلا قصدی برای بازگشت به ایران نداره؛ حتی اگر تمرینات پرسپولیس بار دیگر از سر گرفته شود!//خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 792 · <a href="https://t.me/SorkhTimes/131542" target="_blank">📅 16:32 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131541">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
سپاهان  اصفهان دچار کمبود بودجه برای فصل آینده شده و از این رو قصد دارد آریا یوسفی را به فروش برساند تا بخشی از هزینه‌های فصل آینده را تأمین کند. ///خرمی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 714 · <a href="https://t.me/SorkhTimes/131541" target="_blank">📅 16:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131540">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
سپاهان  اصفهان دچار کمبود بودجه برای فصل آینده شده و از این رو قصد دارد آریا یوسفی را به فروش برساند تا بخشی از هزینه‌های فصل آینده را تأمین کند. ///خرمی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🔴
@SorkhTimes</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/SorkhTimes/131540" target="_blank">📅 16:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131539">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
هیچ فردی به کادرفنی اضافه نمی شود/ محمدی و رفیعی بازیکنان ما هستند
🎙
لیست مازاد در پرسپولیس شایعه است چون ما هنوز ۸ بازی دیگر داریم. میلاد محمدی و سروش رفیعی بازیکنان ما هستند و چون در تمرین غایب بودند جریمه شدند
🎙
با شروع تمرین در خدمت آنها هستیم. سروش رفیعی یکی از کاپیتان های ماست و حتما مسئولیت پذیری او باعث می شود در تمرین شرکت کند
🎙
از یک ماه قبل از شروع مسابقات تمرین را شروع می کنیم. در حال حاضر هیچ فردی به کادرفنی اضافه نمی شود. برای مجوز حرفه ای شرایط خوبی داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 730 · <a href="https://t.me/SorkhTimes/131539" target="_blank">📅 16:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131538">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
🟡
نتیجه‌ای تصادفی یا سناریویی از پیش طراحی‌شده؟
▪️
سپاهان در دیدارهای اخیر خود نتایج عجیبی را ثبت کرده است: تساوی برابر گل‌گهر (دو بار)، شکست مقابل تراکتور و پرسپولیس، و بردهای حداقلی برابر چادرملو و دیگر تیم‌ها. این آمار بیش از آنکه تابع منطق فنی باشد، روایتی متفاوت از لیگ برتر را به تصویر می‌کشد.
▪️
در پشت پرده، پرسپولیس سیاستی شفاف اما بحث‌برانگیز را دنبال می‌کند،تثبیت سهمیه آسیایی خود، به شکل ممکن فوتبالی. برخی فعالان فوتبالی بر این باورند که هدف اصلی از برگزاری لیگ چیزی جز این نیست و نتایج اخیر تیم‌های مدعی در برابر سپاهان، نشانه‌هایی از یک طراحی نانوشته را به هواداران نشان می‌دهد.
▪️
اکنون باید پرسید: تکلیف معرفی نمایندگان آسیا چه خواهد شد؟ اگر قرار باشد تیمی با لابی و سیاست‌گذاری راهی قاره شود، احترام به ماهیت رقابت‌پذیری فوتبال کجا خواهد رفت؟ فوتبال ایران سزاوار شفافیت است، نه سناریوهایی که اعتبار مسابقات را زیر سوال می‌برند.
🔺
سپاهان ۱ استقلال ۲
🔺
سپاهان ۱ تراکتور ۲
🔺
تراکتور ۱ سپاهان ۰
🔺
گل گهر ۱ سپاهان ۱
🔺
سپاهان ۱ گل گهر ۱
🔺
سپاهان ۱ چادرملو ۰
🔺
سپاهان ۰ پرسپولیس ۱
🔺
پرسپولیس ۲ سپاهان ۱
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 715 · <a href="https://t.me/SorkhTimes/131538" target="_blank">📅 16:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
بزیک، مدیرآکادمی باشگاه پرسپولیس و سوال در مورد همکاری با مهدی مهدوی کیا: من با مهدوی کیا مثل برادر هستیم و شروع کار ما در کیا با هم بودیم/ او اکنون با تیم بزرگسالان در امارات کار می کند/ لازم باشد حتما با مهدی مهدوی کیا کار می کنم و از تجربیات او استفاده می کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/SorkhTimes/131536" target="_blank">📅 15:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131535">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
🟡
حذف سپاهان و سفر پرسپولیس به آسیا
🔺
فرمول جدیدی که از سوی مسئولان چند باشگاه ارایه شده، احتمال حذف سپاهان از بین نمایندگان فصل آینده فوتبال ایران را تقویت کرده و استقلال، پرسپولیس و تراکتور را راهی لیگ‌های آسیایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 696 · <a href="https://t.me/SorkhTimes/131535" target="_blank">📅 15:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131534">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
محسن خلیلی: پرسپولیس
همیشه خواهان جذب
علی قلی زاده
بوده اما خودش نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 677 · <a href="https://t.me/SorkhTimes/131534" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131533">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
دیگه لازم نیست دنبال لینک سایت بگردی!
📌
فقط با یه کلیک از داخل ربات وارد وینکوبت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
سریع، مستقیم، بدون دردسر
📌
بدون نیاز به جستجو یا لینک‌های پراکنده
📌
همه چیز داخل ربات آماده‌ست:
▪️
ورود فوری به سایت
▪️
دسترسی راحت از تلگرام
▪️
بدون مراحل پیچیده
🔗
ساده‌ترین راه ورود به وینکوبت همینجاست:
🤖
@Wincobet_bot
📌
میخوای با تحلیل جلوتر از بقیه باشی؟
برای دریافت آنالیز بازی‌ها همین الان جوین شو
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/SorkhTimes/131533" target="_blank">📅 15:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131530">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
🎙
باشگاه برای توسعه آکادمی برنامه بلند مدت دارد. از شاهرودی بابت زحماتی که کشیده تشکر می کنیم. امیدواریم ریل گذاری که در آکادمی شکل گرفته ادامه دهیم
🎙
امیدواریم بازیکنی مثل امیرحسین محمودی را پرورش دهیم. سرپرستی در پرسپولیس؟ فعلا تا پایان فصل در خدمت هستم. برای پایان فصل و فصل جدید حتما در مورد سرپرستی تصمیم گیری می شود
🎙
جلسات ما با اوسمار هر چند روز انجام می شود. چهار روز قبل تماس تصویری با اوسمار داشتیم که در مورد شرایط جدید با او حرف زدیم. در مورد مصدومیت براجعه با هم حرف زدیم. اوسمار منتظر تصمیم سازمان لیگ است
🎙
او گفته در صورت شروع لیگ از اواخر تیر تمرینات از هفته اول خرداد شروع شود. جلساتی خوبی با سازمان لیگ داشتیم تا ببینیم بازی ها چه زمانی آغاز می شود. حضورم در معاونت ورزشی و سرپرستی وظیفه ای است که مدیریت به عهده من گذاشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 676 · <a href="https://t.me/SorkhTimes/131530" target="_blank">📅 13:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131529">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">📍
محسن خلیلی، معاون ورزشی پرسپولیس:
🎙
در مورد نیم فصل که بازیکن خوب جذب نشده باید بگویم که سرگیف را جذب کردیم. وقتی نیم فصل بازیکنی جذب می شود اکثرا قرارداد دارند. بازیکن آزاد در نیم فصل کم است
🎙
یکی از شروط ما برای جذب بازیکن این بود که در فصل گذشته حداکثر بازی ها را کرده باشد. مذاکرات خوبی برای پرسپولیس داشتیم اما شرایط کشور باعث شد تا نتوانیم لیست اولیه خود را جذب کنیم. فرزین معامله گری بازیکن با استعداد است و در سه پست می توانیم از او استفاده کنیم
🎙
دنیل گرا را هم با توجه به موجودی های بازار و تایید اوسمار جذب کردیم. بارها گفتیم نقل و انتقالات با هماهنگی کادرفنی انجام شده است. در مورد نیم فصل که بازیکن خوب جذب نشده باید بگویم که سرگیف را جذب کردیم
🎙
وقتی نیم فصل بازیکنی جذب می شود اکثرا قرارداد دارند. بازیکن آزاد در نیم فصل کم است. یکی از شروط ما برای جذب بازیکن این بود که در فصل گذشته حداکثر بازی ها را کرده باشد
🎙
فرزین معامله گری بازیکن با استعداد است و در سه پست می توانیم از او استفاده کنیم. دنیل گرا را هم با توجه به موجودی های بازار و تایید اوسمار جذب کردیم
🎙
بارها گفتیم نقل و انتقالات با هماهنگی کادرفنی انجام شده است. ما همیشه گفتیم عدالت باید در بحث قهرمان این فصل رعایت شود. ما به سازمان لیگ گفتیم از کجا میدانید پرسپولیس تا آخر فصل در رده ششم باقی می ماند؟
🎙
اگر گفتم عدالت را می خواهیم باید جدول نیم فصل اول لحاظ شود که همه تیم ها با هم بازی کردند. امیدواریم تصمیمی گرفته شود که به نفع تیم هایی باشد که شانس حضور در آسیا را دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 765 · <a href="https://t.me/SorkhTimes/131529" target="_blank">📅 13:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131527">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🟢
هنوز برای ورود به سایت دنبال لینک می‌گردی؟!
✅
دیگه وقتشه ساده‌تر وارد شی و با ربات وینکوبت، فقط با یه کلیک مستقیم وارد سایت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
بدون دردسر و اتلاف وقت
⚡️
بدون لینک‌های پراکنده
⚡️
ورود سریع از داخل تلگرام
⚡️
همه چیز داخل ربات برات آماده‌ست؛ سریع، راحت و بدون پیچیدگی.
🔗
اگر میخوای بدون معطلی وارد سایت بشی، از اینجا شروع کن:
👇
🤖
@Wincobet_bot
🟢
تحلیل بازی‌ها و آپدیت‌های مهم رو از دست نده:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 827 · <a href="https://t.me/SorkhTimes/131527" target="_blank">📅 04:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131525">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
صدا و سیما: ایران آخرین پیشنهاد آمریکا را رد کرده است.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/SorkhTimes/131525" target="_blank">📅 01:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131524">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYLZFMd1yoV6kmjoNP6riXr-RRSwyPly03i4hxAweWXenCE1YODOWaBQBIbjVAzZKcTp9wOTDaqu2uh5Mglu-ES8XbX35s2piQDrAnBMwsms6Uw3C22_8-V-qd86jKoQrgwGIL3WCms-CjDDsXlM-DQO01w23ENQVezuIliWQrYPoWVZrUyJS40Mc_qfCTp41LlQHbwYKpXLrqsKR-T7cWOSQRF4DNpTwh7OiJuNrYsK39nQ0uGSPA80pxzJRkFTMkxIvAZHLJvIT8SI6hQoQm5viEVY2_kLexCVyok6iABNWBNDGs3lN1hF9CsSD1ebqIvnX8LGZMYzvb0u_XJDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مصطفی نجفی مشاور محسن رضایی: بعید است مذاکرات به نتیجه‌ای برسد، چرا که شکاف‌ها بسیار بزرگ است. ایران علی‌رغم آمادگی جنگی، راهبرد «نه جنگ» «نه تسلیم» را دنبال خواهد کرد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 799 · <a href="https://t.me/SorkhTimes/131524" target="_blank">📅 01:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131523">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlfFCLewZeTeVRNdvzpecd_7ZdP2_grpNlaWEZkP9NLeJ7ZbVU-visKydvmg6_vQWHuQx29sp_r3bYjf6m4wjDOGc-YxBfnXlrPGgtemNDfVaY6EkXr_bF5z63caorPk8LqE8uldBe6piUkJs__oZLTzWc5Nfl6UAdTI-jdur8JmuszqlbtbagwkFoz3sxFKYI9pE2ZJbMCgEOZDnuHmP3S5O8o86mYCcs2frBRy65xcFWHt9Z0HJmkMXAu5vv6BlLKYZTOuqlnj_pKM9VAXOnloVAqeWxvSQqAHYfEOmts0h5MYJZz9dbD5AKCgJNISVOQKSp1U8O0PkKHf7dyc2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ درباره ایران، اوباما و بایدن که بوی تهدید میده؛
ایران 47 ساله داره با آمریکا و کل دنیا بازی می‌کنه؛ هی امروز و فردا می‌کنه، وقت می‌کُشه و معطل نگه می‌داره.
تا این که بالاخره شانس بهشون رو کرد و اوباما رئیس‌جمهور شد. اون نه‌تنها با ایران خوب بود، بلکه عملاً طرف ایران رو گرفت، اسرائیل و بقیه متحدای آمریکا رو کنار زد و یه جون تازه و خیلی قدرتمند به ایران داد.
صدها میلیارد دلار پول و حتی ۱.۷ میلیارد دلار پول نقد رو با هواپیما فرستادن تهران و دو دستی تقدیمشون کردن.
اون‌قدر پول بود که انگار بانک‌های واشنگتن، ویرجینیا و مریلند رو خالی کرده بودن. وقتی پول‌ها رسید، مقام‌های ایرانی خودشون مونده بودن باهاش چیکار کنن!
تا حالا اون‌همه پول یه‌جا ندیده بودن و دیگه هم نخواهند دید. پول‌ها رو با چمدون و کیف از هواپیما پایین آوردن و ایرانی‌ها از خوش‌شانسیشون شوکه شده بودن.
ایران بالاخره بزرگ‌ترین آدم ساده‌لوح رو پیدا کرده بود؛ یه رئیس‌جمهور ضعیف و احمق به اسم اوباما. اون واسه آمریکا فاجعه بود، البته نه به بدی «جو خواب‌آلود» بایدن!
ایران 47 سال آمریکا رو سر دَوونده
اما دیگه قرار نیست بخندن!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/SorkhTimes/131523" target="_blank">📅 01:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131522">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZJ4J-ZAV5a4Fwn2HTVMGuNPuydzg3d1EOm4rmuK78bfcJOrCpLe2zEia4Cg_gNBlyEhVwwL3fNOjN_JpwrDvfFOucoqWMuIDbTHXRc5g-31J9oLwRUbxGKMYDVaXoPy4mra4YFBUXhCuDIuejxLxrRQO115AuNJZlRHzi-sRDkQJa0Bogl5-0sTR64hnH9q41AjdokO6SVbuzZe2QpD_T5nI-U4lhf2krYawOBE_AmXcuMpbNawGE7p6VsQhDWefMPOKXsoHat9KLH7d0302ey48OMrPDVdJPXrwQesbPUYqeNXgMZwnUBwy5XFlDBesBeGQAdTFpXwz240rkrSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ: از پاسخ ایران راضی نیستم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 705 · <a href="https://t.me/SorkhTimes/131522" target="_blank">📅 01:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131521">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
منابع دیپلماتیک به المیادین:
پاسخ ایران شامل درخواست برای پایان دادن به محاصره و آزادی صادرات نفت است.
پاسخ ایران که از طریق میانجی پاکستانی ارسال شده، حاوی بندی مربوط به آتش‌بس در لبنان است.
گنجاندن پرونده آتش‌بس در لبنان در پاسخ ایران، جزو خطوط قرمز تهران در مذاکرات محسوب می‌شود.
تهران برخی از تفاهم‌های مطرح‌شده را به تضمین‌هایی مرتبط با پایان دادن به تشدید تنش در لبنان گره می‌زند.
هر توافقی با واشنگتن باید شامل پایان فوری جنگ بلافاصله پس از اعلام آن باشد.
ایران بر لغو تحریم‌های آمریکا و آزادسازی دارایی‌های بلوکه‌شده ایران تأکید می‌کند.
تهران خواستار لغو محدودیت‌های «اوفک» (OFAC) مربوط به فروش نفت ایران است.
پاسخ ایران بر مدیریت ایرانی تنگه هرمز در چارچوب تفاهم‌های مطرح‌شده تصریح دارد.
توافق پیشنهادی شامل مذاکرات ۳۰ روزه پس از توقف جنگ برای بحث درباره جزئیات است.
ایران گام‌های متقابلی را برای آزمایش جدیت واشنگتن در اجرای تعهدات پیشنهاد کرده است.
مذاکرات بین تهران و واشنگتن در حال حاضر به صورت کتبی و از طریق میانجی پاکستانی ادامه خواهد یافت.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/SorkhTimes/131521" target="_blank">📅 01:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131520">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
اطلاعیه رسمی ارتش:
ساعتی پیش یک فروند پهپاد شناسایی دشمن متجاوز، توسط سامانه‌های شبکه یکپارچه پدافند، تحت فرماندهی قرارگاه مشترک پدافند هوایی کشور در منطقه جنوب غرب منهدم شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 749 · <a href="https://t.me/SorkhTimes/131520" target="_blank">📅 01:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131519">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 809 · <a href="https://t.me/SorkhTimes/131519" target="_blank">📅 01:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131515">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
بهزاد داداش زاده: علت عدم نتیجه گیری پرسپولیس افشین پیروانی بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/SorkhTimes/131515" target="_blank">📅 20:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131514">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اوسمار هنوز قولی برای برگشت نداده!
✅
🔗
شرایط بازگشت خارجی‌های پرسپولیس فراهم شد
🔺
فرهیختگان
: تیم پرسپولیس در نظر دارد دور جدید تمرینات خود را از اول خردادماه آغاز کند و در همین راستا به تعهدات مالی‌اش در مورد بازیکنان و مربیان خارجی خود عمل کرد.
🔺
این باشگاه اواخر هفته گذشته طلب خارجی‌های خود را از طریق صرافی انتقال داده و گویا هنوز این رقم‌ها به دست برخی از آنها نرسیده است. هرچند با توجه به شرایط سخت حاکم بر منطقه و تحریم‌ها، احتمالا تا دو سه روز آینده آنها به پول خود می‌رسند.
🔺
البته اوسمار و دستیارانش هنوز برای بازگشت به موقع در تمرینات سرخپوشان هیچ قولی نداده‌اند بلکه با بررسی شرایط قرار است تصمیم گیری کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/SorkhTimes/131514" target="_blank">📅 20:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131512">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⏳
لیگ برتر برمی‌گردد؛ حتی وسط آوارِ بحران
✅
مهدی تاج بالاخره حرف آخر را زد:
لیگ بیست‌وپنجم قرار نیست نیمه‌کاره بماند.
🔗
در هفته‌هایی که خیلی‌ها پیشنهاد تعطیلی کامل فصل را داده بودند، فدراسیون تصمیم دیگری گرفت؛
نه خبری از لغو لیگ است،
نه قرار است فصل بدون قهرمان تمام شود.
🏭
کارخانه‌ها زیر فشار
🔺
تاج می‌گوید تیم‌های صنعتی دیگر مثل قبل توان هزینه ندارند.
از فولاد و پتروشیمی تا آلومینیوم؛
همه درگیر تبعات جنگ و مشکلات اقتصادی شده‌اند.
کنایه تلخ او هم جالب بود:
«در دنیا تیم‌ها کارخانه‌داری می‌کنند، اینجا کارخانه‌ها تیمداری.»
📅
تقویمی که به‌هم ریخت
🔺
تعویق لیگ فقط چند بازی را جابه‌جا نکرده؛کل فصل بعد را وارد بحران کرده است.
نقل‌وانتقالات،شروع لیگ جدید،
و حتی برنامه جام ملت‌ها،
همه حالا به تصمیم تیرماه گره خورده‌اند.
🔥
سناریوی ۱۸ تیمی رد شد
بخشی از فوتبال ایران می‌خواست این فصل بسته شود؛
بدون قهرمان،
بدون سقوط،
و با لیگ ۱۸ تیمی در سال آینده.
📌
اما تاج صریح گفت:
«امکانش نیست.»
🌍
چشم‌ها به جام جهانی
🔺
فدراسیون فعلاً همه‌چیز را به تیم ملی وصل کرده.
برنامه این است:اول جام جهانی،بعد ادامه لیگ.
یعنی شاید بازیکنان مستقیم از آمریکا وارد مسابقات باشگاهی شوند.
🎭
فوتبال ایران؛ بین جنگ، فرسودگی و اجبار
🔺
واقعیت این است که لیگ دیگر فقط یک مسابقه فوتبالی نیست.
بازی‌ها حالا وسط بحران اقتصادی، تقویم فشرده و فرسایش عمومی برگزار می‌شوند.
اما ظاهراً تصمیم نهایی گرفته شده:
لیگ باید تمام شود؛ به هر قیمتی/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/SorkhTimes/131512" target="_blank">📅 17:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131511">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📌
خبرگزاری ایرنا:
تهران پاسخ خود رو به متن پیشنهاد آمریکایی از طریق پاکستان ارسال کرد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/SorkhTimes/131511" target="_blank">📅 16:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131507">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lALx5AOMklCMNTj92QVSOFn51X8IcClJbD4IpJBsL-70Ww5kAsJXY8ehRcS55jXoEp8w0tF_w7Bv3wBNpPAQuLEpRUNskA_feAPhDhqGoqPGtDLhZvImZGEVAEYWaGMyVRnw0Z8epmcomMDgUlnLU7PGsQPu40J7IDx6MvlgBjg_SfW681A8nXG_r0RTaiaDhsbBEs4AcOhrDtZ2kVpTKxrqvs2fyq3T7z-N_51jQzFZDygUbnNozrcLpuLhqUNiZU2jTdbCFCadtP9U8FfFZVSNrWhKAQmKGKMztQB_GVwHwTHvJLzvRcryMXvYV1XhNLJNS0nMPSL63GJR0dlFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ایگور سرگیف در گفتگو با رسانه‌های ازبکستانی اعلام کرد که به قراردادش با پرسپولیس پایند خواهد بود.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/SorkhTimes/131507" target="_blank">📅 15:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131506">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2FzwhacTtxLmoY8x_SkNS0Epm0kNalik9RyDvejh1K75s7MwxsJE74WD5KOKoM67ailo-aoIKHTVK8x0chPs8yCoRQCtUrUWMmZ0YzAx_ZewpR_YtyOB2zCoeZVo7gly5s144i6Rtg3ZRO6o-IT_kGscwU7E4W8tYFHYMhWv_gMtnA2ugSI-hJtAFsX3GrjgM3lx2-2-pr7a6Iyb_5C9ebanqhV16FzXBOzHIeu7EL9RjNo7Rb57_BIk26LmSqw5LX0zkhtAFh5Vcrs9PuqwoXZcttMe4M9r1CzFJpNzKLB3BDa5I0qBUCpw6gZWyFWmkqzW1DtCeDoherq96oamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
برنامه بازی‌های ایران در مرحلهٔ گروهی:
▪️
۱۹ دی: ایران - چین
▪️
۲۳ دی: ایران - قرقیزستان
▪️
۲۸ دی: ایران - سوریه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/SorkhTimes/131506" target="_blank">📅 15:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🟢
دسترسی سریع به سایت وینکوبت
✅
کاربران عزیز، برای ورود آسان و بدون دردسر به سایت وینکوبت، می‌توانید از ربات رسمی استفاده کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔹
ورود سریع و مستقیم به سایت
🔹
بدون نیاز به جستجوی لینک‌های مختلف
🔹
دسترسی راحت از داخل تلگرام
📌
همه چیز به ساده‌ترین شکل ممکن داخل ربات برای شما کاربران محترم فراهم شده.
🔗
اگر دنبال یه راه مطمئن و سریع برای ورود هستید، ربات وینکوبت بهترین انتخاب شماست:
🤖
@Wincobet_bot
🔗
برای دریافت تحلیل بازی‌ها و اطلاع از آخرین بروزرسانی‌ها، به کانال رسمی وینکوبت بپیوندید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 796 · <a href="https://t.me/SorkhTimes/131505" target="_blank">📅 15:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131504">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
فوری/ رویترز: مجتبی خامنه‌ای به نیروهای مسلح ایران دستور ازسرگیری عملیات های نظامی را داد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/SorkhTimes/131504" target="_blank">📅 14:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131503">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/SorkhTimes/131503" target="_blank">📅 14:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131502">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClgsVWztNhvKqZdfi4b6lTJoEuvxR5MGUwkCYhRkt5Dr3nJphJl8GqBIUbOhIGgdBdCR5nxyjGrBUUuxnEu26IS-LCDo5_rt4Xp0YGwDMV6aC5j53Z1jZFigkaErVZcOWrSYvCtEw6Dy9NBA1I7HAytXrQi3fD9Us7Yj5_69KS1FthXaey0fGYqava3JoOs9jxIBhQhVGbNgQKd9lg95JQpHKU3oD1JpQ131vS3Ws4Wkh51qY9dsfGuMIZKt5-DEbboXWVUIG_RMdgaj1J2T_48zFj2raI9f1pXWJd5wUoNd8iPN85_hIIfZa6Dwowxx24-DeF-hEQ_BM6YeKPMUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
افشای رقم رضایتنامه ۳ بازیکن برای پیوستن به پرسپولیس/رقم پیش پرداخت به ۲ ملی‌پوش مشخص شد
🔺
باشگاه پرسپولیس در بخش پیش پرداخت‌ها، از پرداخت مبلغ ۲۵ میلیارد تومانی به باشگاه هوادار برای جذب محمدحسین صادقی، پرداخت مبلغ ۲۵ میلیارد تومانی به باشگاه خیبر برای جذب حسین ابرقویی‌نژاد و هزینه ۲۲ میلیاردی برای به‌ خدمت گرفتن امین کاظمیان خبر داده است.
🔺
همچنین پرسپولیسی‌ها در این بخش، از پرداخت پیش پرداخت قرارداد ۱۷ و ۱۲ میلیاردی برای پیام نیازمند و میلاد محمدی خبر داده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/SorkhTimes/131502" target="_blank">📅 14:49 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131501">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚪️
مهدی تاج: 10 روز است که از کانادا برگشته‌ایم ولی هنوز چمدان‌هایمان را نفرستاده‌اند، نمی دانم سرنوشت چمدان‌های ما چه شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/SorkhTimes/131501" target="_blank">📅 10:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131500">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
دیگه لازم نیست دنبال لینک سایت بگردی!
📌
فقط با یه کلیک از داخل ربات وارد وینکوبت شو:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
سریع، مستقیم، بدون دردسر
📌
بدون نیاز به جستجو یا لینک‌های پراکنده
📌
همه چیز داخل ربات آماده‌ست:
▪️
ورود فوری به سایت
▪️
دسترسی راحت از تلگرام
▪️
بدون مراحل پیچیده
🔗
ساده‌ترین راه ورود به وینکوبت همینجاست:
🤖
@Wincobet_bot
📌
میخوای با تحلیل جلوتر از بقیه باشی؟
برای دریافت آنالیز بازی‌ها همین الان جوین شو
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131500" target="_blank">📅 02:04 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131496">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎙
⚪️
قلعه‌نویی: نمی‌توانیم از الان بگوییم قهرمانی می‌آوریم یا خیر
▪️
امیر قلعه‌نویی پس از قرعه‌کشی جام ملت‌های ۲۰۲۷ گفت:
▪️
پیش‌بینی فوتبال سخت است و نمی‌توانیم از الان بگوییم قهرمانی می‌آوریم یا خیر.
▪️
دوره قبلی هم شانس و لیاقت قهرمانی داشتیم اما بدشانسی شامل حال ما شد.
▪️
فوتبال در آسیا پیشرفت کرده و تیم‌ها به هم نزدیک شده‌اند.
▪️
امیدوارم در جام جهانی و سپس در جام ملت‌ها نماینده خوبی برای مردم ایران باشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/SorkhTimes/131496" target="_blank">📅 00:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
‼️
🇮🇷
نیروی دریایی سپاه در بیانیه رسمی خود اعلام کرد: از این پس هر حمله به نفتکش های ایرانی با حمله به مقرهای نظامی امریکا پاسخ داده خواهد شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/SorkhTimes/131494" target="_blank">📅 00:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5suYF_DJyrmeHUJ3qj2zR1R1JjtVXWL-2sCosjtP55wbqTYuUdvv4dCrJD-opsjXS5OQL0ecaC0h0GHFf980KoCwKwziJbZCHrS13Uxr3sjAbTF06sqq_cMxIJ6WQ0qDP1Y15SMxhnTfQXUW1sJPTZZhiX7MWfRBSillkqydLP9b0Peh-ApVTaWfT3jikxrirY7qoBSdEgDHVOZmjVOXFGMJ9c52DqlY6kA2269yMk2P8cCsHq0HRzR4AelzckocjOIXUHPappoKRjHonFTb_SbksZi-Kk2FARQ6qN9rfLqGIKI3o2bh8L6o7nIEtuQZL_trkhUTskbJj0PS38r5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توضیح علی بازگشا مدیر روابط عمومی باشگاه پرسپولیس در مورد وضعیت خوب مالی باشگاه پرسپولیس و پرداختی‌های باشگاه در مدت اخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/SorkhTimes/131493" target="_blank">📅 23:59 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131492">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
قرعه‌کشی جام ملت‌های آسیا انجام شد/ ساده مثل گروه ایران
▪️
گروه A:
🔹
عربستان
🔹
کویت
🔹
عمان
🔹
فلسطین
▪️
گروه B:
🔹
ازبکستان
🔹
بحرین
🔹
کره‌شمالی
🔹
اردن
▪️
گروه C:
🔴
ایران
🔴
سوریه
🔴
قرقیزستان
🔴
چین
▪️
گروه D:
🔹
استرالیا
🔹
تاجیکستان
🔹
عراق
🔹
سنگاپور
▪️
گروه E:
🔹
کره جنوبی
🔹
امارات
🔹
ویتنام
🔹
لبنان/ یمن
▪️
گروه F:
🔹
ژاپن
🔹
قطر
🔹
تایلند
🔹
اندونزی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 920 · <a href="https://t.me/SorkhTimes/131492" target="_blank">📅 23:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131490">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🔴
فوری
،
فاکس نیوز: اگر پیشنهاد امشب تهران برای توافق با آمریکا منفی باشد جنگ به سرعت آغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/SorkhTimes/131490" target="_blank">📅 22:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131489">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🔴
اگر علیپور از خواسته مالی خود کوتاه نیاید قرارداد وی تمدید نخواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/SorkhTimes/131489" target="_blank">📅 22:03 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131488">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOuLWT0pGxUQB4JzrmPrfV1JdHkROZpUIQp6_fS5BQA8k3rb5hsL0bmjnjGtejG2QslW9VX5gWQMsm9fdlkU1VzGg5F9J-UOcRMYXLLfcr1rDNjTq4qKPGoSnZNom9Y94cbX0azobWLdXhJN2CuhIZEE-kT5iGRKODexwx0UO0O9gH3CEDu2_-j3pdUYkp3wzb3RtAMAZcV7qnPNZDOU4_T9_j9MzXBpM00r23DuceV1usjthpnaOh-TUz5qNDRyq3fSC8fRDLCE6UqoSsvsJYie5gVwry4_6PXOV8lU7psSOLcWDbVSe5SSXFs2DvQDJpjJqKPPmRlGxyAmZjbKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگر علیپور از خواسته مالی خود کوتاه نیاید قرارداد وی تمدید نخواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/SorkhTimes/131488" target="_blank">📅 21:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131487">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
اردوغان: مخالف گسترش جنگ در منطقه هستیم. ترکیه نمی‌خواهد جنگ آمریکا علیه ایران در منطقه گسترش یابد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/SorkhTimes/131487" target="_blank">📅 20:29 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131486">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBsWbwfXjgjsWMB3Lxb-hB_LPFEYFZSoZdvkH9FsyK9BRtTFd0Dfx3zUx5SH26yevQ_VHo91tLtdMzYzKo6UtJALKkZSwbraaYf3NIIS0cpJw4eUkmQ4-n3SAO_dghhlcfoMbkcOgOYCYxy4u1JQq8re-rhrJj3TpnB1RWZVmqdgIxdxHYhN9XAie_fUBWppvxy2ZGjWU5cBqEhvk6cuVw2Pmg6Ur_peZPSSFwImg9kI8PjBj3nlPirbxEbzM9egUnvpxtSlSDNNqfohPf-2inNI1V-P-t3qnH-fASrRCTEgN4j-xbC7aDqDJqmYHr9X1dtQ1COvM7pNLzehweomLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ManCity -
🔴
Brentford
🟣
پریمیرلیگ انگلیس
⏰
شنبه ساعت ۲۰:۰۰
🏟
استادیوم
اتحاد
⚽️
شاگردان پپ گواردیولا حالا پس از درجا زدن نابه‌هنگام مقابل اورتون؛ با یک بازی کمتر نسبت به آرسنال، با تیم آرتتا پنج امتیاز فاصله دارد و اگر توپچی‌ها تمام بازی‌های باقی‌ماندشان را ببرند، رویای قهرمانی منچسترسیتی عملاً به‌باد می‌رود. سیتیزن‌ها امروز با برنتفورد رده هفتمی بازی می‌کنند که در فصل جاری، عملکردی فراتر از انتظار داشته و بالاتر از تیم‌های نامداری مثل چلسی، نیوکاسل و تاتنهام قرار گرفته‌اند. البته آمار کاملاً به‌نفع سیتی است. شاگردان پپ در ۳۴ بازی، (یک بازی معوقه دارند)، ۶۹ گل زده‌اند و ۳۲ گل خورده‌اند. این آمار برای برنتفورد، ۵۲ گل زده و ۴۶ گل خورده است. البته بازیکنان کیت اندروز، در شش هفته اخیر فقط یک برد داشته‌اند و چهار تساوی و یک شکست را هم مقابل یونایتد، ثبت کرده‌اند.
📌
در
ربات
وینکوبت
ثبت‌نام کن و با شارژ از طریق کریپتو ۵٪ شارژ بیشتری رو دریافت کنید، همین حالا شروع کن:
👇
🟣
[
برای ورود به ربات کلیک کنید:
]
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/SorkhTimes/131486" target="_blank">📅 20:29 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131485">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔰
سرور یک ماهه Open VPN فقط تلگرام نامحدود ۱۳۰۰ هزار تومن
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 840 · <a href="https://t.me/SorkhTimes/131485" target="_blank">📅 19:20 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131483">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq09wiZdjjNY7IttD4nD66XrE9dP3LW75mAeXXPmhd3BjBO1cY3QKUQuD-llaWML0U_3Uss2hHhCO4zDKWd1nScUn388J_JdbtC9vi5lpVkNmVwtP6qKXHxWMLTAoDaL1K2cyfj7JH2dBulr-FBBITwX5tuSa3cCEMEyGndbcLI9dg9wWjFyTEO0n-R-y4ldRoG9SfFX3styzqgeU6ussgjZWUWYMwKvO-cOozd7o-Z-4y8El3O6bcoGzEzsZLWKBh8bfNznrdGoEPJTLxtSbtC8zwPG0Cas8htIXCI8kHcNqmn8sdWfnTEIa-IWLR9f9Jqi_Kptcykz6BfL_P3mIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
روزخوش، مدیررسانه‌ای پرسپولیس: اوسمار لیست مازادی نداده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/SorkhTimes/131483" target="_blank">📅 17:59 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131482">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkyfDGl3bR4OM238aX3kwqZmrnwBi0VKd-2MsuQMMFJxxqgKFmkpXYK7eTnC2gQm3XwoZsZMMh_lqG1nxr79731Er5OnIar9jy1BGzVVoi_KhhwnnAoCY0MKUS3YawMbH3YM_HkkpaCbzMt8ZVgdHVt9_HYIWESXlzhGC9DvYwGLbb7N4oyH59E7Qg99PleB7GeaOzXVsWC-wUS5kW_7U_tPdJvbAsjWD3bBA91Zq37h_74F0iRGfyvPebku_HeywvrENt2JzoVIb7yjIQDuMF8aV03BXk-SwGGu2-zXLeJHmoHmPr9LEJmtqXaWF5LoJIQqgPcLjSn7-ACezM5HOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
حمایت مورینیو از حضور ایران در جام جهانی ۲۰۲۶
◽️
ژوزه مورینیو در گفتگو با «فوتبال ایتالیا»: سیاست یک موضوع و ورزش موضوع دیگری است. تیم ملی ایران همچون سایر تیم‌ها شایسته حضور در جام جهانی ۲۰۲۶ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/SorkhTimes/131482" target="_blank">📅 17:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131481">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‼️
🔴
باشگاه يرسيوليس پرونده مربوط به بازى  ملوان با استقلال و تراكتور را به دادگاه دادرسى ورزشى بين المللى (CAS) ارجاع داده است. اين باشگاه اميدوار است كه با پیروزی در اين دادگاه، دو امتياز از تيم هاى استقلال و تراكتور كسر گردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/SorkhTimes/131481" target="_blank">📅 17:54 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131480">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
⚪️
درآمد ۶۵ میلیاردی پرسپولیس در دوران جنگ تحمیلی
🔻
باشگاه پرسپولیس درآمدهای خود در دوماه اخیر جنگی را افشا کرد.
🔻
پیش از این باشگاه پرسپولیس درآمدهای ماهانه خود تا پایان بهمن‌ماه را منتشر کرده که در آن، درآمد تیر ماه ۲۱ میلیارد و ۷۰۰ میلیون، درآمد مرداد ۳۲…</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/SorkhTimes/131480" target="_blank">📅 16:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131479">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
⚪️
درآمد ۶۵ میلیاردی پرسپولیس در دوران جنگ تحمیلی
🔻
باشگاه پرسپولیس درآمدهای خود در دوماه اخیر جنگی را افشا کرد.
🔻
پیش از این باشگاه پرسپولیس درآمدهای ماهانه خود تا پایان بهمن‌ماه را منتشر کرده که در آن، درآمد تیر ماه ۲۱ میلیارد و ۷۰۰ میلیون، درآمد مرداد ۳۲ میلیارد تومان، درآمد شهریور ۷۱ میلیارد تومان، درآمد مهرماه ۷۰ میلیارد تومان، درآمد آبان‌ماه ۶۹ میلیارد تومان، درآمد آذرماه ۷۴ میلیارد تومان، درآمد دی‌ماه ۵۹ میلیارد تومان و درآمد بهمن‌ماه ۶۹ میلیارد تومان گزارش شده بود.
🔻
باشگاه پرسپولیس طی عملکرد ۱ ماهه منتهی به ۱۴۰۵/۰۱/۳۱ معادل ۶۵۳,۹۵۵ میلیون ریال، درآمد داشته است و در مجموع تا پایان ماه فروردین، میزان درآمدهای پرسپولیس به ۶۴۷ میلیارد تومان برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 893 · <a href="https://t.me/SorkhTimes/131479" target="_blank">📅 16:32 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131478">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
تسنیم: سید مجتبی خامنه‌ای به بهبودی کامل رسیده.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/SorkhTimes/131478" target="_blank">📅 16:18 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131477">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
خبرگزاری ایرنا : به دلیل قطعی اینترنت ، این روزها خیلی از آنلاین‌ شاپ‌ ها مجبور شدن تو خیابون و مترو دست‌ فروشی کنن.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 893 · <a href="https://t.me/SorkhTimes/131477" target="_blank">📅 16:14 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131476">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس خواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/SorkhTimes/131476" target="_blank">📅 16:12 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131475">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKal9rBTChEkDF8RZElJq_eT0VMVsfuiCKK0A57vgKj-DwqWxTZy-kKd-e5r9P9x-WGIWnn-MRcqah_mZ8qZGJk5UuuO-zKMOBmS7PRshqrtqxGzV-T3RzCt3vCz7xk_W8DOuugs-AFctr1D5jQcrmzm-6Y40qhBpjbYE58b3tEXiRHPFNmW_QHQlhLtsuycnYExXlNdVhjSOZgnk_ODyHKd8VacMUX8WEThwNo1TcBy5xd19VLWDVwUzfh8wpzxr0P9HXy_tqvAWJI_9SNcaduwanoa2_-kH1eyxu9iL0lOI3PMQXJ4Fqbgofh6HnYt6P4R8bTakelvKXKnbf_uCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/SorkhTimes/131475" target="_blank">📅 16:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131474">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
کانال ۱۲ رژیم صهیونیستی:
◽️
اسرائیل این پیام را به واشنگتن رساند که بازگشت جنگ باید شامل تخریب زیرساخت‌های انرژی ایران باشد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/SorkhTimes/131474" target="_blank">📅 15:59 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131473">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
⚪️
فدارسیون فوتبال اعلام کرد، در جام جهانی شرکت میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/SorkhTimes/131473" target="_blank">📅 15:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131472">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚀
تلگرام در عراق رفع فیلتر شد!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/SorkhTimes/131472" target="_blank">📅 15:55 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131469">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
تاج: به دنبال برگزاری بازی دوستانه با تیم ملی لهستان هستیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/SorkhTimes/131469" target="_blank">📅 11:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131468">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
باشگاه پرسپولیس پول پرداختی به خارجی‌ها را به‌روز کرد
🔺
باشگاه پرسپولیس در حالی که تاکنون 70 درصد قرارداد بازیکنان داخلی خود را پرداخت کرده است، به تازگی مطالبات بازیکنان خارجی خود را نیز پرداخت کرد تا دریافتی آن‌ها طبق قرارداد به‌روز باشد.
🔺
این باشگاه طبق قرارداد بازیکنان و کادرفنی خارجی خود، باید اول هر ماه مبلغ مشخصی را به حساب آن‌ها واریز کند که این اتفاق رخ داده و پرداختی تمام بازیکنان خارجی به‌روز شده است. همچنین سرخپوشان طی روزهای اخیر آخرین پرداختی خود به کادرفنی خارجی این تیم را نیز انجام داده‌اند تا طلبی به آن‌ها نداشته باشند.
تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 898 · <a href="https://t.me/SorkhTimes/131468" target="_blank">📅 10:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131467">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq4yqh0bZip0Ac35IgsjpY2kKXCqoXv8iML7U5Wg7OSYG5wVzc_zOw1E5HDsWK0NdeB9T6A8Vc-C1PttVED37YOYzVn-YTDusmU4YnO3HmFxJCU-o5QzLnHN9s1_ERyxKH-G_jfdsaISsnm161Nc6zwOwddncUoiO7mM5gUDtNiV3MlNVQmlwGJt6qN7HGHslYzBHtbjiM_v7gmqBnfOLX3gPJTj-MT88422RyZeB9o9Wk7-AJMxao0qWvMpO-R5wVJtTffVM4bPr5OHHdYNfYu6TC8c3kZyLfPxP6VIpFqaTPIrs1gR2-CA0HWL3GsXxjwV9JA5uRsApW_p1r_TIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاربران محترم برای دسترسی به سایت وینکوبت فقط کافیه از طریق ربات وینکوبت وارد بشید.
🤖
-
@Wincobet_bot
🤖
-
@Wincobet_bot
📌
بدون نیاز به جستجو، بدون لینک‌های پراکنده، همه چیز از طریق خود ربات انجام میشه.
📌
ویژگی‌های ربات وینکوبت:
👇
▪
︎ورود سریع و مستقیم به سایت
▪
︎دسترسی راحت از داخل تلگرام
▪
︎بدون مراحل پیچیده یا ورود جداگانه
📌
اگر دنبال یک راه ساده و سریع برای ورود به
وینکوبت
هستید، این ربات ساده‌ترین مسیر دسترسی شماست:
👇
🤖
-
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/SorkhTimes/131467" target="_blank">📅 01:27 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

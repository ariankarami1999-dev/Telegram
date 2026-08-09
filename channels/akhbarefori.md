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
<img src="https://cdn4.telesco.pe/file/T8fTVauWYWc2vY7wODxtSi6FWD2eMVKWjWNo9xHMIyh23g5Eiu08EEhFl9vJMJHlNW6bfD-9rOMu0-I0md56QAgVzmlEx6mUqPFUaUakt4sqlOd-7uHila4RW7nKZEU85dBABMhgFl4zlhPv5mGK8LiDNbcKj_zk5PVOM2R9xG_1Wspz7SwEmmLSG-9uyleQ7GDR4nHNoo7U45n0r6pSz9SL-1J1SpqD0MTEyIEDdpL5UDAa2vncgmaq-xoSzUJHxNzMLEUYqpnC13C4rp5hS892e8OeGmog6FYTdYBxdggrGdXUg_ifllO6pfBJYp32DWMLJ9Ayhut50M1HwA6M1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.19M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 21:25:10</div>
<hr>

<div class="tg-post" id="msg-679778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa5gi5INOOdcxU2Iee198BNObY0fW8cIlFLc8uTSO1QuKG5qwF-WqugQ0ubEIdeiB9xrTKpTOuMQ_vE_LZMPb5yxuevWoG9NtuMCOFT4gnmHURJDYqq1Qf3i6cEgifUecddte_Yrm9XsApunMdu5qCipOCF8rsOcjNeVE7LE03DePQI_19bo_AFcs_ItfMrSA59tNBuFcBtY8VOd0Ca3k2GuNSKGTPXUVeET7Jo8UVSkcmj6fl-1RGORqZv5DIJthLFHDlRfGoWVWrb20LRa6s9LkUURj0107UTi7I7wGM53hoKhbKY3WC27wikiPWgUBR3nSDTw4v8VmvmHp3ZRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حکم حضرت آیت‌الله خامنه‌ای محسن رضایی به عنوان نماینده رهبر انقلاب در شورای عالی امنیت ملی منصوب شد
🔹
حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر انقلاب اسلامی در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند.
🔹
باتوجه به…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/679778" target="_blank">📅 21:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
انتصاب دکتر ذوالقدر به عنوان مشاور سیاسی رهبر معظم انقلاب
🔹
رهبر انقلاب اسلامی در حکمی آقای دکتر ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔹
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
بسم الله الرحمن الرحیم
🔹
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر؛ باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/679777" target="_blank">📅 21:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
گوترش:جهان باید بمباران اتمی ناکازاکی را به خاطر بسپارد
دبیر کل سازمان ملل متحد:
🔹
به شدت باور دارم که جهان باید بمباران اتمی ناکازاکی (توسط آمریکا) ، قربانیان و بازماندگان آن را به خاطر بسپارد.
🔹
۸۱ سال پیش، ناکازاکی نمادی از بشریت تخریب شد.
🔹
امروز، هم به عنوان هشداری و هم به عنوان راهنمایی ایستاده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/679776" target="_blank">📅 21:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUnfz6rMb0-QnfXfKEkKbYyIvX6JafF6NkbHJlJYcLYQk8ul6fIeRtTpSdD8ss6qU29KgOWtEiczcgxAuzpze_zRiwNnNczBXW9qvWC7bfWt9BNLPVgsP-z-_3sGFCLGvaivXvaF05aH1DeB98iTQHKSHyzzhFVyMGMaD_qyonWSZEkDLZsT5kKKyaDGpp_khJCzV0-hRYPhjQwgkgj1ZAWOHmT9lYxGf1gA6ooFw4jHfjX306AyoE60fjL649iMD5QWKv_6y-graHh1nrLUzQmzBlm_9alH2_QPDxD8ykFqA5dkV33kfdOyjR3xBqsgDfEQidwo61WdHgvqDcQY7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگاری که نامش با «روز خبرنگار» برای همیشه ماندگار شد؛ محمود صارمی
🔹
محمود صارمی، خبرنگار خبرگزاری جمهوری اسلامی ایران، در سال ۱۳۷۷ هنگام انجام مأموریت خبری در مزارشریف افغانستان جان باخت. شهادت او یادآور خبرنگارانی است که برای رساندن حقیقت، حتی در سخت‌ترین…</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/679775" target="_blank">📅 21:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HITaXt4GRrvl3SG1fgSVmx3OqpFKKAQowSBubHPO3ddpyjfodHAJ6ZEP01NTPCbI8bzE199d9N4COUq1rllS_CSdj454asQZROWQDFzWahkrzQ9_0uXnkwkmrHWsG4LM-QKuIY6fem6g88GnyIxLolKp4u7d-EvooV4BYb6P2kNRMhyDAy-lX8IyI_YhbCngkr9etVntU9UOMbad89z5i2ltPr5O0Woy2gMkrPE7-5o7s6LrC7zZiKmhIn2SEwPF_wlNkAyoekdw53F_Lt5gsK1FJW1Z3wBTnvEKNQXZPpei2PunWIMWCIlYrOFHwDe9aAoW7bAJDa0TyvF6ZvTGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📍
📍
فرصت ویژه دندانپزشکی
📍
📍
🦷
در کلینیک
سرو cip سعادت آباد
✅
۵۰٪تخفیف لیست قیمت
✅
۱۰ سال ضمانت نامه و پالیش رایگان
✅
شرایط پرداخت اقساطی بلند مدت ۱ تا ۱۲ ماه بدون سود و بهره
✅
۲ واحد کامپوزیت رایگان
✅
تخفیف‌های ویژه محدود
👇🏻
👇🏻
برای
✨
۱۹ نفر
✨
رزرو امروز
همین حالا به آیدی تلگرام زیر پیام دهید
👇🏻
👇🏻
@Sabericlinicvip
شماره تماس
👇🏻
09384307498
📩
ظرفیت پذیرش شرایط ویژه محدود است
پیج ما رو دنبال کنید
😍
✅
👇🏻
https://www.instagram.com/p/DblisM0iNTa/?igsh=YXZ3MnZ6d214Y2Zr
sarv_royal_dental
✨</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/679774" target="_blank">📅 21:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679773">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-vmwuXECtFfqh4Br_JDGY3XVQp5HBtyUQXoqOBCACB2Qa_sRY3EuRcxqh-g4fzI9PbsY2r8cuD0CZO5zN0taaBTDXG3pXH16INPBqhDGZ3SYREhxS0gZfzDa_O0Q-QmYEF-jrq5XIv_hdftXeTIdAooymfmttlENXswtmGCRvE3P3CfEwBu-q5X4z50F-gnaHlwAKj-6RwQNJbEA_--LinAxdrT_jBzs_otp9i0Tc5zGvcKFsXE09Uu3rC2ekRQuhrMVOkAIgIUnFKoifrOLDFIEVufiHVawEaESjqfpjt399E-FVxRAICqLCdwCWrglF2uSC4lvSVK8A0E5Dp3eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی ابریشمی، انتخابی مطمئن برای معاملات ارزی شما
✨
💵
خرید و فروش انواع ارز با نرخ‌های رقابتی
🌍
انجام حواله‌های ارزی به سراسر دنیا
🔒
تضمین امنیت، سرعت و شفافیت در تراکنش‌ها
✅
اعتماد شما، سرمایه ماست
راه های ارتباطی با ما:
☑️
شماره تماس: 09158516875
☑️
لینک کانال  تلگرام :
@abrishamiexchangee
لینک واتساپ :
https://wa.me/message/32HOPV4AHR2HG
اینستاگرام :
‌Instagram.com/sarafi_abrishami</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/679773" target="_blank">📅 21:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679772">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvArDR8_4UYLfigJudaO5chgQF8Siv7h1gZtWXT-WaeFbOd2Gq2yuyLgN737hkupBU0fjSMERVI0WeG02_ZofmS-aShJgB7JCbzrS6Fp8G0mpbcjZwzAEHioIr6TnaahiKS3qcGnef4uxQViEkUpKqeQTFFF_WCjoNcGdlNxr-NF51wsTyKOCwahAFyPH0lVLXJBsq38HaDjpPxlHKHx82peMEi21jwlqmv6guqWuIc4YD42eQ9AGc-6v4ZqYXaJ54NSSsY-6l0LvJuC1g1ORMHYXQQDwoYag6iKfYnTcYL0UCfEdd7YW8mvbuWuxdfCIyR6AHAbWhDRbtjxPAUTCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز عجیب پنجه‌های کوالا؛ اثر انگشتی که با انسان اشتباه گرفته می‌شود
🐨
🔹
کوالاها اثر انگشتی بسیار مشابه با اثر انگشت انسان دارند، طوری که اگر ناآگاهانه توسط یک محقق پزشکی قانونی بررسی شود، او حتی نمی‌فهمد که این اثر انگشت انسان نبوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/679772" target="_blank">📅 20:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679771">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
احتمال پرداخت معوقات افزایش حقوق بازنشستگان تأمین اجتماعی از ۱۰ شهریورماه
🔹
پزشکی قانونی: ۴۰ درصد از شهدای دو جنگ اخیر با استفاده از علم ژنتیک شناسایی شدند
🔹
رئیس لالیگا: دوران اینفانتینو به پایان رسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/679771" target="_blank">📅 20:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679770">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwBjgq7bRXSmyw8LfF3eTPZfhUo3QOACFGfB7RfxB-PQN4Mo26hK2SA2GXrni_HgWZ6VZCp8cGQqoHhqLVwiWC-UCtp6MlIpFV_9il4AL8hU5ce4cUGMode5bkurwjqqmnCp12vTQhLr0Drjkd3MW4algO60zwhensaAEsi9a43b1SqY19vxUPtwsqr8rLxD3tAga_UaljIWCvKPkzPNWw14kVtOS2CLkpkgKATPf_OwR574GBI51hx4FPfpF8vC9bRVLLjIp06viEJFlGvLfv3dyd5eAESEcGOnkIdwJtxRwMko9kkN4WtOgnG_sVVutZT07A5g8rInlaEbduxF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
هیئت غریب مدینه برگزار می‌کند؛
مراسم عزاداری ۴ شب پایانی ماه صفر
🔹
سخنران: حجت الاسلام دکتر رفیعی
🔹
مداحان: کربلایی جواد مقدم و حاج سیدرضا تحویلدار
🔹
با اجرای: رسالت بوذری
⏰
از دوشنبه ۱۹ مرداد - ساعت ۲۲:۳۰
📍
مکان: حرم مطهر رضوی - صحن غدیر</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/679770" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679769">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار مهیب در حیفا
🔹
شبکه ۱۲ عبری گزارش داد شهرک نشینان مناطق «حیفا» و «کریوت» در شمال فلسطین اشغالی، دقایقی پیش از شنیده شدن صدای انفجاری مهیب و احساس لرزش محسوس زمین در این مناطق خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/679769" target="_blank">📅 20:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679768">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای اکسیوس: میانجی‌های قطری و پاکستانی اطمینان داشتند که این توافق روز چهارشنبه اعلام خواهد شد، اما از آن زمان، چشم‌انداز دستیابی به توافق کم رنگ‌تر به نظر می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/679768" target="_blank">📅 20:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679767">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: ما فقط تا حدودی با آنها در حال مذاکره‌ هستیم. ما صرفاً داریم ایران را زیر نظر می‌گیریم
🔹
ایران از نظر اقتصادی «در وضعیت بسیار بدی» قرار دارد و پولی برای پرداخت حقوق ندارد.
🔹
محاصره دریایی آمریکا نیز بحران اقتصادی ایران را تشدید کرده…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/679767" target="_blank">📅 20:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679766">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
با آرامش با ایران تعامل می‌کنیم!  ترامپ جنایتکار در مصاحبه با آکسیوس:
🔹
ما با آرامش و بدون تشدید تنش، با ایران تعامل می‌کنیم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/679766" target="_blank">📅 20:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
با آرامش با ایران تعامل می‌کنیم
!
ترامپ جنایتکار در مصاحبه با آکسیوس:
🔹
ما با آرامش و بدون تشدید تنش، با ایران تعامل می‌کنیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/679764" target="_blank">📅 20:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuNc3zR6eoQRZCmpACo8XnNTFLqc_AQzf1MWMfUPOalYCt-gXGW4wYc3lRl-QgemM9F29ayJOj_yILH89gMkBHx_cWKJlI9uwr_0YGrXa2H2Dow4gzj9rv01Fc0gF0TWC048h-3eNil-HtXj00v7o2lknTPNJvTw57pbsgb7xJvKUQsOH9eUQ4xKJP73h1ztqqyWtepOtj1wSkJhl0br0egBTKRs2qLTUsrtwp7iVhLca1bb5ccGJFHUBHWS4zyqAFC8GAfQlKglm621xLFUCcA3N7hCvVSi7FyPparUsSo_OY2B7wBgfUMszTBeC0PFtpTqELn6t52qTi5pRrjK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حکم حضرت آیت‌الله خامنه‌ای محسن رضایی به عنوان نماینده رهبر انقلاب در شورای عالی امنیت ملی منصوب شد
🔹
حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر انقلاب اسلامی در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند.
🔹
باتوجه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را که از پیشگامان دوره‌ پرافتخار هشت سال دفاع مقدس هستید، به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب می‌کنم. امیدوارم در انجام این مسئولیت مهم، کمال موفقیت را کسب کنید.
🔹
ضمنا از تلاش شبانه‌روزی محمد باقر ذوالقدر تشکر می‌شود. إن‌شاء‌الله تحت توجهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله تعالی فرجه‌الشریف همواره سربازی مجاهد برای ملت سرافراز ایران باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/679763" target="_blank">📅 20:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
روایت تجربه‌ای متفاوت از دو مادر؛ از جدایی روح تا بازگشت به زندگی برای فرزند
🔹
00:07:00 حضور ناگهانی بدن‌های انشایی در همه جای اتاق
🔹
00:24:40 ارتباط صمیمی با موجود عجیب بلوری
🔹
00:33:00 بزرگی روح و سختی ورود به جسم
🔹
00:45:40 قدرت چند برابری در وسعت بینایی و شنیداری
🔹
00:50:40 تأکید هدایت‌گر به خوردن سیب بهشتی و امتناع کردن من از آن
🔹
01:03:45 ادامه یافتن صحبت با ۲ هدایت‌گر برزخی بعد از بازگشت به جسم
🔹
01:13:00 رعایت حجاب، نماز، اطاعت از همسر بعد از تجربه
🔹
قسمت بیست‌وششم (نخستین نفس)، فصل پنجم
🔹
#تجربه‌گر
: منیره محمدی/ نفیسه متعبد
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/679762" target="_blank">📅 20:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/babc1bf377.mp4?token=vQa1kw5fdUenyLK_4sGnv3Q9w6v3YZ0Wjnl7X3CCpUO-jjvJPiszhGPvhjramyxkVkyXT9nH9Bx7eONYs9SY4CQw9dERSfX3WOFaTJKm5jvB6CXVS_zUv0H6TzlurEbYWkRG2-_-Y8KCBo5YQVagKkx6ps12gFcKVFJ1-c1xbcIDnAzHKn9pi9pFXGZQplv82dfuZ7OiB9_fDm2jAg6ZteT_uZbxPbgdBvZ-LdDGQo3FtWTbNentOO_LjbQoseiXhvlwi_c3J8KvouCmNExL8sj2JSPoZkreqZCh_DVeWwpN72ftUlJRnc9J2yIDNIvbuQEKc4cz3HE95010Drpuioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/babc1bf377.mp4?token=vQa1kw5fdUenyLK_4sGnv3Q9w6v3YZ0Wjnl7X3CCpUO-jjvJPiszhGPvhjramyxkVkyXT9nH9Bx7eONYs9SY4CQw9dERSfX3WOFaTJKm5jvB6CXVS_zUv0H6TzlurEbYWkRG2-_-Y8KCBo5YQVagKkx6ps12gFcKVFJ1-c1xbcIDnAzHKn9pi9pFXGZQplv82dfuZ7OiB9_fDm2jAg6ZteT_uZbxPbgdBvZ-LdDGQo3FtWTbNentOO_LjbQoseiXhvlwi_c3J8KvouCmNExL8sj2JSPoZkreqZCh_DVeWwpN72ftUlJRnc9J2yIDNIvbuQEKc4cz3HE95010Drpuioi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی مهیب در مرکز خرید نیپاه در ماکاسار اندونزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/679761" target="_blank">📅 20:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y60jqdpp7umfQmu5fD232zUDU_V8rrXZUPlOx0seOPf7P-_CTDUukuQ3URpDEtu88As3UQZsnBAKDuev48L9otMmDbpuXPdgAIFjktXvqbgoypfs38ft8yMCJPhGbOGkxgDr-e1G9ETP_7Uw5rC8ku5iNNu2PkPAKDhTjK8QvoE1EyRcVIdCLSPDMP64HtwA5A3RUv2lJB4jTn-sEYF--_5rZo-_FjSIXxMJVdXGuAa8VgjvJNoyS_t0p8Asn5yPDpmUCx2kI8nLkukCyhEWg_qGhDVmK-ngpmUKCnTALsAcqfNLK0CN0yypT7SI6hBNzZ9-drIBkt9GVNbeJNbJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنجال جراحی زیبایی ۴۰ میلیارد تومانی خواننده زن | چهره او چه تغییری کرد؟ + عکس
🔹
ابرو گوندش، خواننده شناخته‌شده موسیقی ترکیه، بار دیگر به یکی از سوژه‌های داغ رسانه‌های این کشور تبدیل شده است؛ اما این‌بار نه به دلیل انتشار ترانه یا برگزاری کنسرت، بلکه به‌خاطر تغییر محسوس چهره‌اش پس از انجام یک عمل زیبایی.
بیشتر بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3236501</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/679760" target="_blank">📅 20:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d57f2083b.mp4?token=voJIb2TUMjgCGS9xwFakcK5bxLSmC5R1JfLM45gk7LqGFq94AyAu4m16bBrN6PRfj-r6OvOR8DS3E9_zCSW43LnNmRKIbcf04yYhbpi-mBkkB0b6QVeW_aZn2Kr8ybbJ0pm6DBitr4MtJGeH0Zxnntv_B-XS3jr7gEYQD8gMqTPaM8cy30dvSFUhmlNHb97uzMFDobp_yHa4SG07Hih58Ytk28hUBxjV6k3f7RBScFRP3c64lhy42Hb58lB0UiUjoSmweZxKQ1PdnCm94QTM6tv_hYH1q3Jt1_o2qpOIx0yPG683x-hsjfiPcCZN87n3amFpcpWc4bHcDgm3SxG6KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d57f2083b.mp4?token=voJIb2TUMjgCGS9xwFakcK5bxLSmC5R1JfLM45gk7LqGFq94AyAu4m16bBrN6PRfj-r6OvOR8DS3E9_zCSW43LnNmRKIbcf04yYhbpi-mBkkB0b6QVeW_aZn2Kr8ybbJ0pm6DBitr4MtJGeH0Zxnntv_B-XS3jr7gEYQD8gMqTPaM8cy30dvSFUhmlNHb97uzMFDobp_yHa4SG07Hih58Ytk28hUBxjV6k3f7RBScFRP3c64lhy42Hb58lB0UiUjoSmweZxKQ1PdnCm94QTM6tv_hYH1q3Jt1_o2qpOIx0yPG683x-hsjfiPcCZN87n3amFpcpWc4bHcDgm3SxG6KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ ترامپ در ایران فقط بنزین را گران نمی‌کند؛ همه‌چیز گران‌تر می‌شود
الکساندریا کورتز، نماینده مطرح کنگره آمریکا:
🔹
ما آمریکایی‌های عادی می‌توانیم شکاف بسیار بزرگی را میان حرف‌ها و عملکرد ترامپ ببینیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/679759" target="_blank">📅 20:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
دانیل فریدمان، وزیر دادگستری پیشین اسرائیل: احتمال می‌رود توافق درباره غزه در نهایت به تشکیل یک کشور فلسطینی منجر شود که از سوی تمام جهان به رسمیت شناخته شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/679758" target="_blank">📅 20:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
گاردین: ایران می‌تواند افغانستانِ تازه آمریکا شود
روزنامه انگلیسی گاردین در مورد شکست آمریکا در افغانستان:
🔹
آن جنگ به قیمت جان بیش از دو هزار و ۴۰۰ سرباز آمریکایی، ۴۵۰ نیروی بریتانیایی و ده‌ها هزار غیرنظامی که آمار دقیق آن‌ها نامشخص است تمام شد.
🔹
اکنون و پس از تصمیم احمقانه و غیرقابل‌خرج ترامپ برای حمله به ایران، همان الگوی فاجعه‌بار در حال تکرار است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/679757" target="_blank">📅 20:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boHXMkW7prRPXZISfBqhwvCEqkYQ0rx8DhdkYm4t8tIYwQdRbHhjVl4ymuYfoAq0bephJf0uMuMxks7g2kei-M3Nnaij3XIXfSEBPdyyN8XhPaB6VGshCZxeycq35SA2ruKF-is5O3004pkI6tVpsM2BvZUh3wHxcRHcvI3ZrJdlZE4ObialqtQ9kcj0Kl6b0DUOID7ErKdqsn8yIg7q27E-55Zgr1c1K2n4Y837SLjRoD8gOyFIZwzYb85VoqttqV1W9ansHKerKT2bpVMkiJ7VBXmvZlQrW933-ngDYYT5xFygbGUhYIGJLAd7Re4H6AIOIsDI0ctPh85JDxzvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسواییِ دشمنانِ ملت ایران با انتشار تصاویر حضور امام سیدمجتبی خامنه‌ای در میان مردم و جلسات با فرماندهان نیروهای مسلح در آینده
🔹
جانشین سازمان بسیج مستضعفین در آیین تکریم و معارفه معاونین نمایندگی ولی فقیه در سازمان بسیج مستضعفین:
🔹
تصاویر و مستنداتی که در آینده از حضور رهبر معزز و فرمانده کل قوا حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای (حفظه‌الله) در میان مردم و کوچه و خیابان و جلسات با فرماندهان نیروهای مسلح منتشر خواهد شد، بار دیگر موجب رسوایی دشمنان و بدخواهان ملت ایران خواهد شد.
مشروح خبر:
👇
basijnews.ir/00f14B
🔻
کانال خبرگزاری بسیج:
👇
@Basijnewsir</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/679756" target="_blank">📅 20:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXc1ouhso4SqHLRgCWsIaP4QgwQqQw6GfIYzjZ2BZQBRyQ5_2h2NumNTn_4AxShx4U5_mrD5bIeGb1kLdhBx1e7dc7cD7WNtOuq1XEkFv10MLUNUZ48TSJGG1clI2WfdPTgDJMKZmviXHZI3OQ7F7kiMuTARoRzx8z2DOp4hcipGyt-eIwsdC3V8WIm8vQ7EiLJ6v5U8utAFRbv8sZT3uj7FrDyJVyQZgEsxZF-R0_fQqZQu0JcmREWlv6NvgMmXpwwqZGYgD_q2-1LEJpP7grhjmeNve1IydcVKOI2qjc1ss7bqCp1moo3_EolhFksnvKCzM2U4B3cDYDK4gT4Q1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی صهیونیست‌ها به شهر المنصوری در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/679755" target="_blank">📅 20:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713efbba80.mp4?token=QTBIgMRdnLXbkGrXKuf8MjiWJj4uE_Sfw2KwnquvXYJqxXCZ7eCHjVfFM1njeRT2Pn6N2-wqj9eVz0aXUN2iYnQ69MDQGqnnp1lNV4xWY2htOK1i7YJ92bj69K6vw7t8nzw8v2zV0hnGg-f5yc3fiESKFBiBF-N5zNF1RBpBEVqvNHufPE-NbTH96e0Ukbe1wiCZ59g3_mCyc2-B1RksI3KOhDgTYFMubcuFDr44BNqDXMI0oTf_tG_FzIAnB9jPrmNRkV2GuE7BbjqOyXaZDl16uWzmwdfkMAFBtX3ABDg7VMl0QuDjSTLyXnjpPQfcwnO0kW11pwIf5oRQIZejLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713efbba80.mp4?token=QTBIgMRdnLXbkGrXKuf8MjiWJj4uE_Sfw2KwnquvXYJqxXCZ7eCHjVfFM1njeRT2Pn6N2-wqj9eVz0aXUN2iYnQ69MDQGqnnp1lNV4xWY2htOK1i7YJ92bj69K6vw7t8nzw8v2zV0hnGg-f5yc3fiESKFBiBF-N5zNF1RBpBEVqvNHufPE-NbTH96e0Ukbe1wiCZ59g3_mCyc2-B1RksI3KOhDgTYFMubcuFDr44BNqDXMI0oTf_tG_FzIAnB9jPrmNRkV2GuE7BbjqOyXaZDl16uWzmwdfkMAFBtX3ABDg7VMl0QuDjSTLyXnjpPQfcwnO0kW11pwIf5oRQIZejLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی مسئولان خبرنگار می‌شوند
🔹
دیروز به مناسبت روز خبرنگار این دفعه مسئولان از سلامی، خبرنگار صداوسیما چندتا سوال پرسیدن و باهاش مصاحبه کردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/679754" target="_blank">📅 20:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پزشکیان: اگر به امید کشورهای دیگر بنشینیم شکست می‌خوریم
🔹
هیچ‌کس خود ما و مردم ما نمی‌شود. ما امیدمان را به خدا و مردم بستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/679753" target="_blank">📅 20:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1f26d72f.mp4?token=EPkUvGxCG9qsuPIK4oOAdJU6r0OSk9B3hl-t9YWJ98lgXQxZfanVr1Ld72MSwqSgS0eu813kUhlEEk2TdJUvmzVctEei4JTQdRpnz2vUy7SgR_E6S2nE73gCGhHMwedVq4UAONxL4v4ukmBS75xZCHGpIcoJ8_-V4PMAg4bWB49PLfAPiDKb4I3KGLmmsZEXHLQGnyVOu2Njedc6vbCCTBe6Q2L_NfKOMEE8lbqe40wwkjUAMu0yrF69fHm85co6aZd89N1E7k6INj-LeTurSRC-ccjfNXQZvjTIttzmr0cf-GoilmpKSQhTsUkiUAuGXwikMYTW-lkGZ2qOMeOfnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1f26d72f.mp4?token=EPkUvGxCG9qsuPIK4oOAdJU6r0OSk9B3hl-t9YWJ98lgXQxZfanVr1Ld72MSwqSgS0eu813kUhlEEk2TdJUvmzVctEei4JTQdRpnz2vUy7SgR_E6S2nE73gCGhHMwedVq4UAONxL4v4ukmBS75xZCHGpIcoJ8_-V4PMAg4bWB49PLfAPiDKb4I3KGLmmsZEXHLQGnyVOu2Njedc6vbCCTBe6Q2L_NfKOMEE8lbqe40wwkjUAMu0yrF69fHm85co6aZd89N1E7k6INj-LeTurSRC-ccjfNXQZvjTIttzmr0cf-GoilmpKSQhTsUkiUAuGXwikMYTW-lkGZ2qOMeOfnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت ۴۲۰ نفر به اتهام ایجاد آتش‌سوزی‌های گسترده در فرانسه
🔹
مقامات قضایی فرانسه از بازداشت ۴۲۰ نفر به اتهام نقش داشتن در آتش‌سوزی‌های اخیر این کشور خبر دادند؛ بحرانی که کارشناسان آن را شدیدترین فصل آتش‌سوزی در فرانسه از زمان جنگ جهانی دوم توصیف کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/679752" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVO-gxL-4dFxegdJWkIdrkKjy27J2v11YFK4PFS2Y6ihyK8_qFdHZ1mQYBPCgYbJpW7po2rM21awPJW_8Pgg8MQivOOPaqwFIHk7lf9lY1o3AG0P-v36s7Oetv7NkfNoE6JqyPnBDhKaZta3Ge31tShswduj4u5lkaY4-yZQnZiz2_5QkaYifhqbFiYOjrnyiI8sB6P62IxyUQ5Z32a3RKDtLtUfC00DPQhip_WqOAw0CjP3RQxmS5cOEyGZ3rzEaGfGPD_dLIFC3LhBPeipCrTXU8NPhEZCc8irJkGq7kPuPJMBYbEptplDofKyGURoVB7XeXRzWYz-qyb1rPM-1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/679751" target="_blank">📅 20:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae43e83853.mp4?token=iwiScd6E7ImvnNjQyhicYeXEWoPvda4Me4udMqeYqf-6TyZrnQZhNBZV87miNPoK4vwmYBr0qzmKyMy6nt7gWnU7mC7BBPTJCYcQyw7WFNYz2fhqmI-HCpIIh3nsGPHqT3Pc3tjt-nC1sOBiZ2w4KEoFKqzOIoF5JzUh2iFM2CVD9C0Pk9eRSiOEX-rtRgy9dRGrbN34ajEqdzNCrQv_OBXMTv2Dja1FmbU5xUkxtrOa9Gya-Qyh67tP4qMMCQMlibyxPLuGYVKZyRG0_txxvT0EpGTxREohIsHlnq3z7f1W7-qzmj28ynqhFGwsfdhxPvUQY_LN3R9nY_qXZQel0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae43e83853.mp4?token=iwiScd6E7ImvnNjQyhicYeXEWoPvda4Me4udMqeYqf-6TyZrnQZhNBZV87miNPoK4vwmYBr0qzmKyMy6nt7gWnU7mC7BBPTJCYcQyw7WFNYz2fhqmI-HCpIIh3nsGPHqT3Pc3tjt-nC1sOBiZ2w4KEoFKqzOIoF5JzUh2iFM2CVD9C0Pk9eRSiOEX-rtRgy9dRGrbN34ajEqdzNCrQv_OBXMTv2Dja1FmbU5xUkxtrOa9Gya-Qyh67tP4qMMCQMlibyxPLuGYVKZyRG0_txxvT0EpGTxREohIsHlnq3z7f1W7-qzmj28ynqhFGwsfdhxPvUQY_LN3R9nY_qXZQel0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باوجود پیچیدگی دیپلماسی پس‌از جنگ، ارتباط مطلوبی با کشورهای منطقه داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/679750" target="_blank">📅 20:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaDGA9AnnVxjbHOHKU3yFUiKBvBopWpZSB3kEJ0yeO7jRAnv2uUVnrfZKkVb_sL6255meqjr6vkyo1Eg51Kj4ATzZ_NXzlW1oXoIkCSWt1Z46-ByZd7hupOqBD1uYTwWJhjwXx3ZwtppeynhAc_IE6yS1_ARzbLljxIuZN11DfJagfwPH_tw82sFgyB_qLHZCppGNkBlXJ_q4TzkediGTk0gRY8R6KD6Br5DnLKFPc_AxLxZkKoZUtKH14whYb45cDlbcPQWfoqMmNGTh2QOuK1rjt89CKCb0kzw4cG6rtS2GFRIRSIFL768pcbhQsYQI-eGlYVSJDj-G1czqcQJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
مام اسپری سورملینا
💥
✅
۱۰۰٪ حذف بوی بد عرق
✅
بدون حساسیت، بدون لک
✅
مناسب برای خانم‌ها و آقایان
✅
ماندگاری بالا با یک‌بار استفاده بعد از حمام
🔵
🟡
بسته ۲ عددی با رایحه اسپرت و دلپذیر
🔥
سفارش با تخفیف ویژه از لینک زیر
👇🏻
https://yeklinks.ir/mamtele?utm_source=foritel
https://yeklinks.ir/mamtele?utm_source=foritel
پرداخت درب منزل +ارسال رایگان</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/679749" target="_blank">📅 20:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ade5f0d0.mp4?token=O1wPh2xJ_bp8LP0qC8s0025kknfv_bf31Y87be5M-GJAVF3NvecCzBD1Fjj4vKqVZzpLXnYtjwQPZZmPrkmpbsuK73bmwYy5OHc5U6QBwqV-Js2xboFxfdOhkdmSvruT0d85RcL6lbmclwkHa_Tk4YUD8FjhSqL-j_uj1Ta8Sqc1Q4Q_a7MHJcYvkHizhaKXnOR5gIkKWMglw8O1IqPRhVOdNti7i3sUWWZZN4OgDjJyC0jP8qVpvtGH1byOrV0p8j_DkxPMPF6HEuHpoh8A6oveO9gxrwgTYW4nBBql8xF78D5ZolO9y8SI6-lZ2eQzTJbUiZKqCSRrBMG-CBDFMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ade5f0d0.mp4?token=O1wPh2xJ_bp8LP0qC8s0025kknfv_bf31Y87be5M-GJAVF3NvecCzBD1Fjj4vKqVZzpLXnYtjwQPZZmPrkmpbsuK73bmwYy5OHc5U6QBwqV-Js2xboFxfdOhkdmSvruT0d85RcL6lbmclwkHa_Tk4YUD8FjhSqL-j_uj1Ta8Sqc1Q4Q_a7MHJcYvkHizhaKXnOR5gIkKWMglw8O1IqPRhVOdNti7i3sUWWZZN4OgDjJyC0jP8qVpvtGH1byOrV0p8j_DkxPMPF6HEuHpoh8A6oveO9gxrwgTYW4nBBql8xF78D5ZolO9y8SI6-lZ2eQzTJbUiZKqCSRrBMG-CBDFMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ ایران هزینه غذای مدرسه کودکان را ۴ هزار دلار افزایش داده است
کریس مورفی، سناتور مطرح آمریکایی:
🔹
همین حالا که داریم صحبت می‌کنیم، این جنگ [ایران] دارد خانواده‌ها را به ورشکستگی می‌کشاند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/679748" target="_blank">📅 19:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a9797194.mp4?token=BAMXmvW7Yv7tDWO3-ei29AGIN9L54B_C_ZilKpHHKKzl4muI7MXMcX6KEGHE1rTXgsRHpAzpc1RHGJNh-2cCAsAy0pFO-JcM56rob9GiRzln8GcWa01LXLyeZcYEVzBmmAtjdVbVsuN8FvqoJaiP4spI6mp-KAs1BISwmPHpgxfmPn28KjvII38PTcA0LhS5hJ_-QtuFuvAUKY2FHaJokiA9r5l4BznlSLl8k9V-qFCUnVmrCWNCh9i1VR601YbFXHnXP4ckSKsQbuDrGzUiPPiHLLcuCAxoAm5iND2-M5gsN4gFwHpYk0J5DspPQOUnkdKpO9y9C6eBhlQNOcB-1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a9797194.mp4?token=BAMXmvW7Yv7tDWO3-ei29AGIN9L54B_C_ZilKpHHKKzl4muI7MXMcX6KEGHE1rTXgsRHpAzpc1RHGJNh-2cCAsAy0pFO-JcM56rob9GiRzln8GcWa01LXLyeZcYEVzBmmAtjdVbVsuN8FvqoJaiP4spI6mp-KAs1BISwmPHpgxfmPn28KjvII38PTcA0LhS5hJ_-QtuFuvAUKY2FHaJokiA9r5l4BznlSLl8k9V-qFCUnVmrCWNCh9i1VR601YbFXHnXP4ckSKsQbuDrGzUiPPiHLLcuCAxoAm5iND2-M5gsN4gFwHpYk0J5DspPQOUnkdKpO9y9C6eBhlQNOcB-1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: کارها را به صورت چریکی انجام می‌دهیم / هزینه‌های جنگ از هزینه‌های یک ساله دولت بیشتر بوده است / همدلی سران قوا و رهبر عزیزمان موجب تاب‌آوری کشور شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/679747" target="_blank">📅 19:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtKLZB5nVWPewoShOxy4FNdhLvDDwugZDWhWj76SscsThvJQ8nL3d4cEpZtm1XgXGzW5ZCkvJWauwtHTasZQ2GJhm6LL5f6RD6RUXJbQa5uN7m0GjkGbP1bA0iKfwx6xOB67IJZMKVwhdy_knMfx5soCFDpvmTTsjkVaBupLgDbBypekyoLYcxEzgYaZyUP97sPwyQuMV0c_jsIydkHsjf6mDLSOpco_Zma60JQqjcRVnuhR6Oan_nYKBohgNiT7yOz7pLhLqXVk4A739SAe5o1mZBhqrWRCgRUGwag2KmBMVh-282R2G416EnLMmQqI2tvuxOh39q-tBrmr0s0sLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل تعاونی لنجداران: ممنوعیت واردات لوازم خانگی، درآمد ملوانان و شناورها را کاهش داده است
مجید کردوانی، مدیرعامل تعاونی لنجداران بوشهر:
🔹
از زمانی که ورود لوازم خانگی باتوجه به بخشنامه‌های اخیر ممنوع شد، شناورها و لنج‌های سنتی دیگر امکان واردات بسیاری از کالاهای مورد نیاز را ندارند.
🔹
با کاهش حجم فعالیت لنج‌ها، درآمد ملوانان و صاحبان شناورها کاهش یافته و مشکلات معیشتی برای آن‌ها ایجاد شده است.
🔹
مسئولان باید فعالیت‌های ته‌لنجی و ملوانی را گسترده‌تر و آزادتر کنند تا امکان ورود کالاهای بیشتری به بازار فراهم شود.
🔹
افزایش تردد شناورها به معنای ایجاد فرصت‌های شغلی و درآمد برای ملوانان، مالکان شناورها، صاحبان کالا و سایر شهروندانی است که به‌صورت مستقیم یا غیرمستقیم در این چرخه فعالیت می‌کنند.
🔹
کاهش هزینه‌ها و تشریفات گمرکی می‌تواند موجب شود کالا راحت‌تر و سریع‌تر به دست مردم برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/679746" target="_blank">📅 19:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d719b401.mp4?token=N88AZxTY0ZuXRzd3NlWYHw9H0TQ5K0kftGhpPxJEHMIhdOA5-iBqB_-Kn_1KzP_FrWcinXvdM8IkjbzlYC8BW0IyUIsL4DHsuVFyA2qK52gLoyyKCFvtuNuh9iW4HGaaWaHy1B7JYfbgFrUU4D5p4krNfYouLiqU1MOpc05Jv4ROVbX_kGRySbcaoQUcFwHGHgg9Z69mu2Cuh42zABlbpS5JYSS2hgeT2OCxn_uZX2AB1zmDrBX2oXPcWh5XH_Hhtw33dq5UsINl35RZQxgHvtFJDMUcHy9EYWqRTANdjQEXIiGIPqJQifLy1lE0s6_6HQjOBqReZDQ3DCYxd_dN6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d719b401.mp4?token=N88AZxTY0ZuXRzd3NlWYHw9H0TQ5K0kftGhpPxJEHMIhdOA5-iBqB_-Kn_1KzP_FrWcinXvdM8IkjbzlYC8BW0IyUIsL4DHsuVFyA2qK52gLoyyKCFvtuNuh9iW4HGaaWaHy1B7JYfbgFrUU4D5p4krNfYouLiqU1MOpc05Jv4ROVbX_kGRySbcaoQUcFwHGHgg9Z69mu2Cuh42zABlbpS5JYSS2hgeT2OCxn_uZX2AB1zmDrBX2oXPcWh5XH_Hhtw33dq5UsINl35RZQxgHvtFJDMUcHy9EYWqRTANdjQEXIiGIPqJQifLy1lE0s6_6HQjOBqReZDQ3DCYxd_dN6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری آمریکایی به یک اسرائیلی: دیگر نمی‌شود از شما دفاع کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/679745" target="_blank">📅 19:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679744">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
پزشکیان: بیشترین دغدغه من مشکلات جوانان است / ما نسبت به سرمایه‌های جوانان قصور کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/679744" target="_blank">📅 19:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
یمن: علت قطع اینترنت یمن توسط عربستان این است تا فیلمی از نتیجه حملات منتشر نشود
«ضیف الله الشامی» عضو دفتر سیاسی جنبش انصارالله یمن:
🔹
قطع خدمات اینترنت در برخی مناطق ساحل غربی یمن، با هدف جلوگیری از انتشار تصاویر مربوط به آتش‌سوزی انبارهای تسلیحات و مهمات انجام شده است.
🔹
نیروهای سعودی نگران انتشار گسترده تصاویر خسارات و بقایای به‌جامانده از این انبارها هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/679743" target="_blank">📅 19:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327f3411fe.mp4?token=ZMhukPSLnYvHrCTmEZuZwXbMdgMqowLGglGM5JDDPDHbpeQaapM9N4Q1C1RUd4NeftzrpTR0hHE1vVTWKSzkLMLWFK0bWeOoG3hcddvZP1vsn_zg5D1TCZbGRJqIZPvFosJ6bRnjwYlPhoiA2wmrkgBQ4r3gMN27AbdA3SpW2iCmeZOydJaMLMguS_LIL-Bsf_LLds7hNUZZKLjQ58aD7SCKKTyzlv9ammVh_JoHrvBwew9bdkuVtLv1wXJb0OMq929fdbwJ7M_tVC1FL3SOQ5MTvgO8rqYj6jwnWlU0_11Lzi0zZnhVe7tKV6uebCXzwAzuMmO1W1i1RqZojrhJQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327f3411fe.mp4?token=ZMhukPSLnYvHrCTmEZuZwXbMdgMqowLGglGM5JDDPDHbpeQaapM9N4Q1C1RUd4NeftzrpTR0hHE1vVTWKSzkLMLWFK0bWeOoG3hcddvZP1vsn_zg5D1TCZbGRJqIZPvFosJ6bRnjwYlPhoiA2wmrkgBQ4r3gMN27AbdA3SpW2iCmeZOydJaMLMguS_LIL-Bsf_LLds7hNUZZKLjQ58aD7SCKKTyzlv9ammVh_JoHrvBwew9bdkuVtLv1wXJb0OMq929fdbwJ7M_tVC1FL3SOQ5MTvgO8rqYj6jwnWlU0_11Lzi0zZnhVe7tKV6uebCXzwAzuMmO1W1i1RqZojrhJQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۱ برابر شدن حرکت قطارها از مبدا چین، تلاش برای بازگشایی مسیرهای آذربایجان و روسیه  رییس‌جمهور:
🔹
پیش از این هفته‌ای یک قطار از چین می‌آمد و اکنون روزی سه قطار می‌آید. در حال بازگشایی مسیرهای دیگر مانند آذربایجان و روسیه نیز هستیم. اینگونه نیست که آنها محاصره…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/679742" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نایب‌رئیس پارلمان عراق: با تصویب قانون حشد الشعبی موافق هستیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/679741" target="_blank">📅 19:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
دنیس راس: ایران اهرم تنگه ‌هرمز را در اختیار دارد
مدیر پیشین اداره سیاست‌گذاری وزارت خارجه آمریکا:
🔹
ایران تحت فشار است، اما اهرم تنگه ‌هرمز را در اختیار دارد.
🔹
ایران همچنین توانایی تهدید تأسیسات انرژی همسایگانش را دارد و می‌داند که ترامپ به شدت مشتاق پایان دادن به جنگ است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/679740" target="_blank">📅 19:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ca40c39f5.mp4?token=nb0jPUwkP6dBvFcGF9KYxIz_1qBA5zbffeslNHc4hAyz_2wF9kzhJaT2m3wE04ydxBIr-xwF8nXKYBMuORoawXkU2P1wWBFDzif-_ALZQ3qmQbrG0lJvU1sbKjMr5GDL9XqO9L04hXykfIdEQi_uxjQKfYtKyAZn-kqZTekxZpU77dPORetNOFXvLhzmEzTrj9ko_DM3kgIcZbVkVqorw1zGx8lnIHRj8nLERqfgTjLEH4bZKbsTYIIyJRyFHjL75blYBbI8m9rHG0gQKql_taUIsbgpnaUQbdejrRMK18R4UnRuqZXuYU0HIn2b4hql7liuEquUaK7Yawg9KJd3Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ca40c39f5.mp4?token=nb0jPUwkP6dBvFcGF9KYxIz_1qBA5zbffeslNHc4hAyz_2wF9kzhJaT2m3wE04ydxBIr-xwF8nXKYBMuORoawXkU2P1wWBFDzif-_ALZQ3qmQbrG0lJvU1sbKjMr5GDL9XqO9L04hXykfIdEQi_uxjQKfYtKyAZn-kqZTekxZpU77dPORetNOFXvLhzmEzTrj9ko_DM3kgIcZbVkVqorw1zGx8lnIHRj8nLERqfgTjLEH4bZKbsTYIIyJRyFHjL75blYBbI8m9rHG0gQKql_taUIsbgpnaUQbdejrRMK18R4UnRuqZXuYU0HIn2b4hql7liuEquUaK7Yawg9KJd3Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملۀ پهپادی موشکی انصارالله یمن به مواضع عربستان در المخا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/679739" target="_blank">📅 19:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
۲۱ برابر شدن حرکت قطارها از مبدا چین، تلاش برای بازگشایی مسیرهای آذربایجان و روسیه
رییس‌جمهور:
🔹
پیش از این هفته‌ای یک قطار از چین می‌آمد و اکنون روزی سه قطار می‌آید. در حال بازگشایی مسیرهای دیگر مانند آذربایجان و روسیه نیز هستیم. اینگونه نیست که آنها محاصره کنند و ما دست روی دست بگذاریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/679738" target="_blank">📅 18:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679737">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ترامپ می‌خواهد به تقابل با ایران پایان دهد
‏
🔹
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد دونالد ترامپ قصد دارد بدون دستیابی به توافق هسته‌ای، به تقابل با ایران پایان دهد و این اقدام را به‌عنوان «پیروزی» اعلام کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/679737" target="_blank">📅 18:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceacac0b90.mp4?token=Vd0fTl0PT3OGIR6B5b7GYGu-rmevxdemfCHuufZfc6uoEG_m3Tvy1RRm3ZRaZgJURCOGChA--KTRkeCODHNMxxqeVSit6ZpYQUiZUNtQLEH_eqtGJn6nyz7i8r56fp-hv7zqlggCA-5cnZ6Bd5nB550LR1yZ7OtvYPFTdkMLsUyyX6bLda2pTgnwl-T-_5xgXDMHugj-izvy9wqOIrev0VHcaFIq6wmAqSSbxUXV880JeOaPjW_aZLrfcDHhd_5S2AqJjPGP7wurJoI0R9IVVHSu6wfH-reAYz4zDZjOVNC3ia_wXWvhpfwFHhtSOSuMYLD-6Pa4f2bLql37ee5jwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceacac0b90.mp4?token=Vd0fTl0PT3OGIR6B5b7GYGu-rmevxdemfCHuufZfc6uoEG_m3Tvy1RRm3ZRaZgJURCOGChA--KTRkeCODHNMxxqeVSit6ZpYQUiZUNtQLEH_eqtGJn6nyz7i8r56fp-hv7zqlggCA-5cnZ6Bd5nB550LR1yZ7OtvYPFTdkMLsUyyX6bLda2pTgnwl-T-_5xgXDMHugj-izvy9wqOIrev0VHcaFIq6wmAqSSbxUXV880JeOaPjW_aZLrfcDHhd_5S2AqJjPGP7wurJoI0R9IVVHSu6wfH-reAYz4zDZjOVNC3ia_wXWvhpfwFHhtSOSuMYLD-6Pa4f2bLql37ee5jwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیف رهبر شهید انقلاب از تصویری که از شهید حججی در اسارت داعش منتشر شد
🔹
شهید حججی مثل شیر نر دارد جلو میرود و اعتنایی به کسی ندارد!
🔹
انتشار به مناسبت سالروز شهادت شهید محسن حججی و روز مدافعان حرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/679736" target="_blank">📅 18:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679735">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرهادی: امسال آزمون استخدامی ماده ۲۸ برگزار نمی‌شود
🔹
یمن: عربستان اینترنت ساحل غربی یمن را قطع کرد
🔹
آیت‌الله آملی لاریجانی: ایران از تنگه هرمز عقب نشینی نخواهد کرد
🔹
توافق دمشق و مسکو بر سر وضعیت پایگاه‌های نظامی روسیه در سوریه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/679735" target="_blank">📅 18:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679734">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
یک منبع ارشد یمنی در صنعا تاکید کرد افسران عربستانی و تحرکات نیروها و مزدورانشان از ضربات موشکی و پهپادی ارتش یمن در امان نخواهند بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/679734" target="_blank">📅 18:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679733">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
انبارهای مهمات مزدوران سعودی در «المخا» یمن همچنان در آتش می‌سوزد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/679733" target="_blank">📅 18:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679732">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYFo65fwESPb77rf3MlLYF4xUjjbGE_cJe9V2SXHfD9_BYZMMoZfVc1iUYEAk271CXDiJ78x4H15I9jur_Z8cBHWxNDX6LwkygrJYNyCfaVQ6WcJaqkcXqGq22oKnRuOZPHjsZ0buEv4ftvMeW_tAPnFVfckZ-YiJUDWMAeZr2Ne3Ka45NJJjCsZ_47Pk_8MTam0sxkT9AuAaco7xskYUnrMR7twrkGZkFyq0v5SbYHutHR2dmT59alS-PwjSEq1GwrKZa4lw_lpjlAeCG-b22ITz6ixXKxsEMW3My5HfHnMOerKeb_Z5R78hdTnYFfAZbnkb5ArokKIcNeQdetQZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سلاح‌های خطرناک ترکیه/ آنکارا با این چند اقدام مرموز می، خواهد قدرت اول منطقه شود
🔹
ائتلاف مکه می‌تواند در بلندمدت، تحولاتی عمیق در روابط ترکیه با دنیا ایجاد کند. ترکیه از طریق ائتلاف با یک قدرت هسته‌ای مانند پاکستان و یک دولت ثروتمند مانند عربستان می‌تواند قدرت خود را بیشتر کرده و همزمان، قدرت نفوذ خود در شرق را بالا ببرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3236597</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/679732" target="_blank">📅 18:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سخنگوی فراجا: در پروندۀ قتل رجب‌زاده تاکنون ۵ نفر دستگیر شده‌اند  سخنگوی فراجا:
🔹
در پروندهٔ حمیدرضا رجب‌زاده تاکنون ۴ مرد و یک زن دستگیر شده‌اند که یکی از آن‌ها عنصر اصلی دخیل در قتل بوده است.
🔹
بررسی‌ها نشان می‌دهد بیشتر ادعاهای قبلی کانال ضدانقلاب جدیدالتاسیس…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/679729" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff5a9b291.mp4?token=eK_4i7rsZjuL31OGayHiFkLRDJNdaZSzwAHdYBYb8E59mk9Fo-dqBsA_uM3RTR_TkZTI-doe_-_YoJGnlPXgxSnPPuFw9wNA3aj0XYNX3UCcqJPjOfUIVJw7xIqWmTiWXc6UwOLy7nMPomV0c8om0Ra4nBw2AfLqvgQLxDhMSftFoT16hRNC_ErxmZubRHvNaOmCeV9AdgHwWvRoc3hY7IH7MSqkvmSF9KDtzF18CBnOLl__jwAiOdej1BLXuFZ-uz1VhC91ZjeyGJxGhoN5su6lrwuhOURr6sUeVicPaxcJ46sJWVX3iIeMGW3KrFv0tM5TQjUQKwUVhQuXOSuGMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff5a9b291.mp4?token=eK_4i7rsZjuL31OGayHiFkLRDJNdaZSzwAHdYBYb8E59mk9Fo-dqBsA_uM3RTR_TkZTI-doe_-_YoJGnlPXgxSnPPuFw9wNA3aj0XYNX3UCcqJPjOfUIVJw7xIqWmTiWXc6UwOLy7nMPomV0c8om0Ra4nBw2AfLqvgQLxDhMSftFoT16hRNC_ErxmZubRHvNaOmCeV9AdgHwWvRoc3hY7IH7MSqkvmSF9KDtzF18CBnOLl__jwAiOdej1BLXuFZ-uz1VhC91ZjeyGJxGhoN5su6lrwuhOURr6sUeVicPaxcJ46sJWVX3iIeMGW3KrFv0tM5TQjUQKwUVhQuXOSuGMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از لوگوموشن کنسرت‌ نمایش «سیاوش»
🔹
«سیاوش»؛ حماسه‌ای ماندگار از شاهنامه فردوسی روی صحنه می‌آید
🔹
کنسرت‌ نمایش «سیاوش»، سومین اثر حماسی و یکی از تأثیرگذارترین داستان‌های شاهنامه فردوسی به کارگردانی حسین پارسایی و تهیه‌کنندگی سید محمود شبیری و جلیل کیا است که با نگاهی هنرمندانه برای مخاطبان امروز بازآفرینی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/679727" target="_blank">📅 18:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679725">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuxVJVGhTF7dnxFGifQ_Gn3f39FRQYvssVOAfCuXeaS7DgVJHSHH3FP2fHQRdLMzaCwseypCDXI0X8PWtSiCumynSlNLpFmEL7_0SIxuKrRA3cWIp-ripOpi6jGWjX_-fnd55HJ2zLdbDr_AzvQP_F73CBht2BeYf5S35_qGGcIc50Y_4lmwtK2C6GowPvhLkS8ivamgo6SLYJ9obvpSWuvlxyxetE_B6A1zadV1aDjjiPSG4Het8A-AeWDUPr082F45lST0naoo0sQ-khsLhw3SrQM_nKFmqGHZN6Br4pV3igqBc5XxTLJFyktaiqMwUN1cFe28FoUugZUbs_hY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پردرآمدترین باشگاه‌های فوتبال جهان
🔸
رئال مادرید با درآمد ۱.۱۶ میلیارد یورو در صدر فهرست پردرآمدترین باشگاه‌های جهان قرار گرفته و تنها باشگاهی است که مرز یک میلیارد یورو درآمد را عبور داده است.
🔸
پس از رئال مادرید، بارسلونا با ۹۷۵ میلیون یورو و بایرن مونیخ با ۸۶۱ میلیون یورو در رتبه‌های دوم و سوم جای دارند.
🔸
حضور ۹ باشگاه از لیگ برتر انگلیس در میان ۲۰ باشگاه پردرآمد، نشان‌دهنده قدرت مالی بالای فوتبال انگلیس در مقایسه با سایر لیگ‌های اروپایی است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/679725" target="_blank">📅 18:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679720">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14113d78c.mp4?token=g8QR3-BALztoQ-JZY5J13Uwq2LHx209OXhpkkWBuf_MZCzAryD1QXodm30xXhIaJHTm59aMTgFHIPCQrRoKiskf63WZ3CcN4TWEf6FbwAV1CBtxK1lsa9q1Yl56Fpgds6BFJ-uDX-IVYKzynI9wif4X8QkHDb1fon-q15QKzBALkMXcxRrf3yXQl3i8NSMmY8LNBQL9An5UAUA3UftP5jqHBbz0lpqpKumFAjJ5fCS_KXO_w6PwyAU9cx0TuugDLrXlzB8_HJYEyHeQ4Nitrko-1_h_dTvWBZo-oA-AgWaZ_zpbbMjl--jXf8bHBGY_H1KMvlY2jL1Eo1uDzmE-Ruw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14113d78c.mp4?token=g8QR3-BALztoQ-JZY5J13Uwq2LHx209OXhpkkWBuf_MZCzAryD1QXodm30xXhIaJHTm59aMTgFHIPCQrRoKiskf63WZ3CcN4TWEf6FbwAV1CBtxK1lsa9q1Yl56Fpgds6BFJ-uDX-IVYKzynI9wif4X8QkHDb1fon-q15QKzBALkMXcxRrf3yXQl3i8NSMmY8LNBQL9An5UAUA3UftP5jqHBbz0lpqpKumFAjJ5fCS_KXO_w6PwyAU9cx0TuugDLrXlzB8_HJYEyHeQ4Nitrko-1_h_dTvWBZo-oA-AgWaZ_zpbbMjl--jXf8bHBGY_H1KMvlY2jL1Eo1uDzmE-Ruw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از شادی گل تا سقوط در تونل؛ بدشانسی پشت بدشانسی برای ژابی
🔹
ژابی، مدافع کوریتیبا وقتی که از روی تابلوهای تبلیغاتی پرید تا خوشحالی کنه داخل تونل بازی که به سمت رختکن قرار داشت افتاد و گلشم به دلیل آفساید مردود شد و خودش در اثر سقوط مصدوم و تعویض شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/679720" target="_blank">📅 18:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULJfgHzFCotcLcIXRafb7d3p-l-jkRd-vfTzkqlQ49zoFaVxuc1J5bNl6NFspMInFGaPP1PcnJIaLAgmY3nSoBYKz0d_lGdUNwcU6lNneISxAsRhfuNB80mOiMph0blnfWqZEcm1UpzF8fzQr3ZrDjEALUxq2Oh-rRO2w87pCZ_01EkCX4_af70ERrbaGNKDh21cU3vQtxUTlgi6afFvFxFlavh_Y5kJua2j7aCdhzJXJCGULQHHd7laezPAiR3PJcSUv6VQIUpyDngQWnA-h1HavCCsr-VS6M2MGPA21lrX306km4y1Vddg_TdudlX0k_-QycBCD7_Obfp2N9NKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عددی که همه را غافلگیر کرد/ راز سود ۱ میلیارد و ۴۰۰ میلیونی هر کاربر اکوتراست در سال ۱۴۰۴ چیست؟
🔹
به تازگی مشخص شده که گروه مشاورین اکوتراست موفق شده در ۱۴۰۴ سود میانگین ۱ میلیارد و ۴۰۰ میلیونی به کاربرانش برساند! عددی هنگفت در بازار تورمی ایران که کل جامعه به واسطه اتفاقات آن، به دنبال حفظ ارزش سرمایه خود هستند!
🔹
حالا اکوتراست برای ۱۴۰۵ طرح ویژه‌ای گذاشته و به کاربران تازه‌وارد ۵ روز خدمات رایگان‌مشاوره سرمایه‌گذاری می‌دهد!
برای استفاده از نسخه ۵ روزه رایگان اکوتراست همین حالا کلیک کن
👇
👇
لینک
لینک
لینک</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/679718" target="_blank">📅 18:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679717">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
۶ سوخت‌رسان آمریکایی آسیب‌دیده از جنگ علیه ایران برای تعمیر به آمریکا منتقل شدند
🔹
دست‌کم ۶ فروند KC-135 در جریان عملیات علیه ایران آسیب دیده‌اند؛ ۵ فروند در حمله به پایگاه شاهزاده سلطان عربستان و یک فروند در برخورد هوایی بر فراز عراق.
🔹
سوخت‌رسان آسیب‌دیده برای تعمیرات اساسی به پایگاه تینکر اوکلاهاما منتقل شده‌اند و دست‌کم ۲ فروند دیگر نیز در حال انتقال به آمریکا هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/679717" target="_blank">📅 17:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679716">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/679716" target="_blank">📅 17:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679713">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تجرد قطعی در ایران؛ از وضعیت فردی تا سبک زندگی
🔹
به گفته یک جامعه‌شناس تجرد قطعی در حال تبدیل شدن به نوعی سبک زندگی است و بخشی از جامعه تمایل بیشتری به مجرد ماندن دارد؛ آمارهای رسمی از بیش از ۱۸ میلیون مجرد قطعی بالای ۴۵ سال و بیش از ۲۴ میلیون نفر مجرد…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/679713" target="_blank">📅 17:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679711">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/679711" target="_blank">📅 17:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679709">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
حذف بنزین خودروهای فرسوده؛ خودروهای تولیدی سال ۱۳۸۵ به قبل دیگر سهمیه سوخت ارزان دریافت نمی‌کنند
🔹
خودروهایی که به سن فرسودگی برسند، سهمیه سوختشان قطع، ترددشان در کلان‌شهرها ممنوع و نقل‌وانتقال پلاکشان متوقف می‌شود؛ در مقابل، برای نوسازی مشوق‌هایی در نظر گرفته شده است.
🔹
این اصلاحیه برای سال ۱۴۰۵، شماره‌گذاری خودروهای نوشماره را به گواهی اسقاط منوط کرده و استفاده از خودروهای فرسوده در سکوهای حمل بار و مسافر نیز ممنوع خواهد بود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/679709" target="_blank">📅 17:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679706">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ_gsbQNBAAKzruZOY7dSqHvN51XNLqOxJsaLwCIq-fJTv_CI3j5jtGU2yT_8LkgxTDkGXsbof_AFg4fr4AoXdmN2qlJDAwkl1cZuW2qZ3Xh5qMf5O0dGoEjU0QupZ9XCKJoqHb7YYxTy1FOF2qyoi4uU0SpkJC1K0dJXX1snZkHnihTy7sbJaBl-tIrPj7gBblDfttf8970l9k0q2z5Dbfa891RWz3wO7HyuMc5RFoTRZLG1P-jyVRICqBbY_3eBDiHsIyMF9aSVK3nIhZMlAATGGz0De09O9VJ7cuu0Sg5J6nytSc-q2LQ751XPCZo95Y6iXnhZhM2jyLXgs0aew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از نیمه دوم سال، طلایی شوید
🔵
اگر قصد سرمایه‌گذاری در طلا را دارید، بهتر است پیش از آغاز نیمه دوم سال و قبل از انعکاس عوامل اثرگذار در قیمت‌ها اقدام کنید.
🟢
بازدهی مثبت طلا در بیشتر نیمه‌های دوم سال
🟢
افزایش تقاضای ارز و اثر آن بر قیمت طلای داخلی
🟢
سرمایه‌گذاری در صندوق طلا بدون اجرت ساخت و ریسک نگهداری فیزیکی
🟢
پشتوانه فیزیکی شمش و سکه در انبارهای بورس کالا
🟢
ترکیب بهینه گواهی سپرده شمش و سکه در رز ترنج
🟢
شروع سرمایه‌گذاری در رز ترنج از ۱۰۰ هزار تومان
🟢
قابل معامله در تمام کارگزاری‌ها با نماد «رز ترنج»
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/679706" target="_blank">📅 17:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679703">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2ca95668.mp4?token=h4EkLXTPZnnV8iQCXHUrc5uVriblsYP2XgJuqJ1Zf0s_PVwz7ab8XkfG7L18s_kUiUWiud-5nZ2HNYFYrJvljAUDuv9iwzD9hvITJRzESKXrFWhFoZIfsi4gq8TZrfP6oqMuoC3SiNdDwlh20rkp5vJRezn5q6o4MdUJzzINyqFcAyq4-a67eaqaepnJQ3RRDw6DVEVXE5iDchxfwPla6Sg_Ymxkzl9Fg-ChRf54WFa9V6YkH7gMzQhMHw48eYSSQKBYulwQP9qmwtDggpwY9v5yXwZCxlCsmuRSa62ZhKKnldkGJspUvi4LEtgraVvph5l41q9JFhNVhXXIeZuR6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2ca95668.mp4?token=h4EkLXTPZnnV8iQCXHUrc5uVriblsYP2XgJuqJ1Zf0s_PVwz7ab8XkfG7L18s_kUiUWiud-5nZ2HNYFYrJvljAUDuv9iwzD9hvITJRzESKXrFWhFoZIfsi4gq8TZrfP6oqMuoC3SiNdDwlh20rkp5vJRezn5q6o4MdUJzzINyqFcAyq4-a67eaqaepnJQ3RRDw6DVEVXE5iDchxfwPla6Sg_Ymxkzl9Fg-ChRf54WFa9V6YkH7gMzQhMHw48eYSSQKBYulwQP9qmwtDggpwY9v5yXwZCxlCsmuRSa62ZhKKnldkGJspUvi4LEtgraVvph5l41q9JFhNVhXXIeZuR6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکنیک سنتی که توسط چوپانان جوان قبیله بنا اتیوپی انجام می‌شود
🔹
چوپانان جوان برای مراقبت از دام‌ها و دوری از مارها و شکارچیان روی چوب‌های بلند راه می‌روند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/679703" target="_blank">📅 16:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679702">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
بیانیه شدیداللحن سازمان حشد شعبی عراق و حمایت از فالح الفیاض
🔹
سازمان حشد شعبی عراق اتهامات مطرح‌شده علیه رئیس این سازمان را افترا خواند و با تأکید بر اینکه دستورات هوشیاری و آماده‌باش پیش از حمله صادر شده بود، از پیگیری قانونی علیه شایعه‌سازان خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/679702" target="_blank">📅 16:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679701">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sa3kddMkGv45JHanzQSDgVWWTNGsK0Ga1hgGOvp482hFICeOOic5_qgd304hGcEE4sn71WKF24be6WFX6iZDcALxrOgInlcynCTKPfZt7sT6wSmJHOFv2HZwS-fP_RI1FMmDmb9nEfMM7SonS0atajCfikPxGsFCdYjnYItocvkWjaO-k0lXxQqpTiz2scs0Nay8AEXHzkWwn1DiSXoFOR8imzuDFKdsd703KiqK-H_fo0rz9Na6c24FLAD1Id7uyD-wJ-92IQ1NrR0NNHdAFpRg3MieaK4NQd5poua5nf_AozIF-pIJ7XU_KjkLlU03N8NGksy-rK9b3za0o7CegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
قیمت طلا منتظر جمع‌شدن پول ما نمی‌مونه.
اگه خرید طلا رو گذاشتی برای وقتی که پولت کامل جمع بشه، باید بدونی که با ازکی‌وام امکان دریافت اعتبار خرید قسطی طلا تا سقف ۲۰۰ میلیون تومان رو داری و می‌تونی آنلاین طلا بخری.
✅
فوری
✅
بدون نیاز به چک و ضامن
✅
با اقساط منعطف ۶ تا ۲۴ ماهه
شاید این همون فرصتی باشه که شروع خرید طلا رو دیگه به آینده موکول نکنی
👇
https://azvm.co/ptw0</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/679701" target="_blank">📅 16:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679700">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b463873e3.mp4?token=lhGwyay97ab50Qz9HPSYeMK6bSHjjZ79Cv01J-6ceigPxgVspdNTOu-HGAQGQXe8xU04YWym40d2kRzOQ2gHfPEPn3RnUjRFy6hJ59WfvQhrT7WN-OZJAQaShCn0JDi7kzvjfrVLrsULqwVSGbEXLJR6sHrHc2Y2FX7DOZbD4qoowGq-h4lm5iu8iNpSJplMfx-gy3BCqL_oQtDF9QdNZeaK3c34zHYZmXOhG5zHIuAZuOdItNZjn_iB4-V7oxhEbdRcXO1WCtJuta-Lsp9qbVX0kvtVDCY324nB8kDFU9nNuMeePpyhxzRIe5jFZjnHEaAmfLNf2YfqChPGK4BNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b463873e3.mp4?token=lhGwyay97ab50Qz9HPSYeMK6bSHjjZ79Cv01J-6ceigPxgVspdNTOu-HGAQGQXe8xU04YWym40d2kRzOQ2gHfPEPn3RnUjRFy6hJ59WfvQhrT7WN-OZJAQaShCn0JDi7kzvjfrVLrsULqwVSGbEXLJR6sHrHc2Y2FX7DOZbD4qoowGq-h4lm5iu8iNpSJplMfx-gy3BCqL_oQtDF9QdNZeaK3c34zHYZmXOhG5zHIuAZuOdItNZjn_iB4-V7oxhEbdRcXO1WCtJuta-Lsp9qbVX0kvtVDCY324nB8kDFU9nNuMeePpyhxzRIe5jFZjnHEaAmfLNf2YfqChPGK4BNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های خارجی درباره جنگ ایران و آمریکا چه می‌گویند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/679700" target="_blank">📅 16:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679698">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c1573314.mp4?token=BHz4oh2YQm5J-qbq33CkMmvTEroogblRbybZRx8NYQVkeQBuluydBVwGXVP2jhs8O1ybwrn3WqnM8Qd3PUyeg9_bsXGghewGNtbKvsX9XBkfknBeTkKHYu97ltF1kfxwo6-6WVHH9h6upWnrR12U-xWl-e69aHvHFkubRtecKPYC97cEZCZSK8IA_6mFef-30sdPVLkUc1HP0O8M2NFwn6n7gOH1c-ghicqta9uDOnNj9X4P29u6hk266SpxSOpp9Kj5IZwCbsvWuqDDUgvRCmJb1SFVCxvUUP-zw7c3FsLJ1Jg2U_YIw1BwIsKfRoj7MjohjF8F2XLRbXBrkyMLqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c1573314.mp4?token=BHz4oh2YQm5J-qbq33CkMmvTEroogblRbybZRx8NYQVkeQBuluydBVwGXVP2jhs8O1ybwrn3WqnM8Qd3PUyeg9_bsXGghewGNtbKvsX9XBkfknBeTkKHYu97ltF1kfxwo6-6WVHH9h6upWnrR12U-xWl-e69aHvHFkubRtecKPYC97cEZCZSK8IA_6mFef-30sdPVLkUc1HP0O8M2NFwn6n7gOH1c-ghicqta9uDOnNj9X4P29u6hk266SpxSOpp9Kj5IZwCbsvWuqDDUgvRCmJb1SFVCxvUUP-zw7c3FsLJ1Jg2U_YIw1BwIsKfRoj7MjohjF8F2XLRbXBrkyMLqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور بعضی از خرید‌های ساده به‌جای این که پولدار نشون‌مون بده، تبدیل به یک سقوط مالی میشه؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/679698" target="_blank">📅 16:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بورس کالای ایران: ساعت پایان معاملات بازارهای مالی بورس کالا به ۱۸ افزایش یافت
.
🔹
عضو هیات رئیسه مجلس از وصول ۱۰ سوال نمایندگان از وزرای آموزش‌وپرورش و راه‌وشهرسازی خبر داد.
🔹
پاکستان: هدف پیمان دفاعی جدید، تقویت صلح منطقه‌ای است.
🔹
انتشار اطلاعیه ثبت‌نام آزمون دفتریاری ۱۴۰۵ در سایت سنجش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/679697" target="_blank">📅 15:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679695">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
چرا سقف ۲۵درصدی افزایش اجاره رعایت نمی‌شود؟/ مالک می‌گوید تورم ۶۰درصد است، چرا اجاره ۲۵درصد افزایش پیدا کند
علیرضا نوین، عضو کمیسیون عمران مجلس:
🔹
افزایش سقف ۲۵ درصدی اجاره‌بها مشخص است که رعایت نشده و در عمل مالکان آن را اجرا نمی‌کند.
🔹
باید با متخلفان برخورد جدی شود. اگر ۱۰ متخلف را شناسایی کنیم و محل فعالیت آنها را ببندیم و حتی روی آن پلاکارد بزنیم که این واحد به دلیل گران‌فروشی یا اجرا نکردن مصوبه دولت پلمب شده است، دیگران نیز متوجه می‌شوند که قانون باید اجرا شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/679695" target="_blank">📅 15:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679694">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رئیس اتاق تعاون ایران:
بخشی از سود سهام عدالت ۱۴۰۴ تا هفته دولت واریز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/679694" target="_blank">📅 15:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679693">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY9aF2x4i1WDyzFS_7bd1KDk4bEw5TnsDEnJ-8PP9_sW_2vX8gHL1QakW7MRsduGCu279hH7ElMNETMIZzEZFmwz8_c2YpljgsSRYGVnoIs09YAbR5Y_u98paZsIkRkxSpaXS-eSaNHlD7KfKdAb4IwBSE6hlIi8hbdMUeTbyLsJi0G7ngu-B3E3eLz9K-ICwXPODMYfKRnK262_safqpcJo76zvOSoG6LE8MYPa7PQu0m7ebmF_8HncyldjGCoHUiix-tmDDSenc43xsMrG_KCLJWp9VHSKZv1Gp-AzmFF0cfRsbD5xXJmtAp97AvbpXAgBV1vAgErD79le038jEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک سوءبرداشت تکراری از ردیف تبلیغات در صورت‌های مالی فولاد مبارکه
🔹
هر ساله با انتشار صورت‌های مالی شرکت‌های بورسی در سامانه کدال جهت ارائه به مجامع عمومی، موجی از تحلیل‌ها از زبان برخی تحلیل گران بازار سرمایه و در رسانه‌های مختلف شکل می‌گیرد.
🔹
یکی از بندهایی که همواره و در سال‌های گذشته نیز مورد سوءبرداشت رسانه‌ای قرار گرفته و این ابهام درباره آن هرساله تکرار می‌شود، ردیف هزینه‌های تبلیغات است. تحلیل‌گران شتاب‌زده معمولاً کل این ارقام را به پای هزینه‌های جاری روابط عمومی و رپورتاژ رسانه و یا تبلیغات رسانه ای می‌نویسند، در حالی که ساختار تفکیکی این سرفصل‌ها ماهیت کاملاً متفاوتی دارد.
🔹
بخش عمده‌ای از آنچه در گزارش‌های مالی گروه فولاد مبارکه به عنوان هزینه تبلیغاتی ثبت می‌شود، در واقع بودجه باشگاه سپاهان است. این بودجه در قالب یک قرارداد رسمی تبلیغاتی ثبت می گردد و ماهیت آن با هزینه‌های مرسوم تبلیغات تجاری کاملاً متفاوت است.
irasin.ir/xKCh
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/679693" target="_blank">📅 15:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679691">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
خاموشی‌ها تا دو هفته آینده به حداقل می‌رسد
رجبی‌مشهدی، معاون برق و انرژی وزارت نیرو:
🔹
خاموشی‌ها­ در مناطق عادی ۲ ساعت یا کمتر است و مناطق گرمسیر به دلیل شرایط خاص، از تخفیفات ویژه برخوردار هستند.
🔹
عمده مشکلات ما برای تأمین برق در ساعت ۱۱ تا ۱۸ است که ساعت ۱۵ تا ۱۸ اوج بار را تشکیل می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/679691" target="_blank">📅 15:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679689">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: تهران برای بازگشایی تنگه هرمز ۵ شرط کلیدی تعیین کرد
وال‌استریت ژورنال:
🔹
ترامپ امیدوار بود که بازگشایی تنگه هرمز به او امکان دهد پیروزی را اعلام کند و درگیری با ایران را به پایان برساند، حتی بدون دستیابی به یک توافق هسته‌ای. اما تهران خواسته‌های خود را به شدت افزایش داده است.
🔹
ایران خواهان خروج نیروهای آمریکایی از منطقه، لغو محاصره دریایی، برداشتن تحریم‌ها، آزادسازی دارایی‌های مسدود شده و دریافت میلیاردها دلار غرامت جنگی پیش از بازگشایی کامل تنگه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/679689" target="_blank">📅 15:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCeUeL4aYEwsIhEkDTAkZVJW_t2z052LtDeG4Y4dcNFEpKwenoLFwEcTyyjTByRo63XJhT61qIsGHcqda_FqporaDVCxHP_8r1mqJUEAPyDKMYZ9cwyXzZi0IvfsoIa5A_l8P-H6yWaZ94X3cHdA4W9mjGLOAbyI0X5kxxTM4jAoYaez-sVrsOvq_kZm56J5HMrJ1HZP6pAb6DiV1BCf_4UGanjdVdVGfd59z6zUC1bnd0BUVe8fI3T17Xhw5AMoqYqLE3uM9YWmuRD-bwxXzA7dc4-btiunPhuhTxCT0y_vGgJJLO2zBT4Ss808mfi9DImn5g-QDJv1401qSTvBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
‏
استوری بهنوش بختیاری: آمریکا در هیچ مقطعی از زمان، دوست هیچ کشور صاحب تمدنی مثل ایران نبوده، نیست و نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/679687" target="_blank">📅 15:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679685">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1NELEV8tUCLLHRRuZb7UpjA_qDqGSLGMKmZN-ZuQTdG0OyohZsiQgrVqFd2s8Ha2IjaR6_gVfBbt7CFCwHpc-zB6_VpSL6jWXTH6r-CVtQ728fZDeIFx9_nFJu6hPIBx5nFHt-kzGWOJJIqeRt28dA3BBZFxU_TOzuGrgo3Fv_oFjwIRDzEEKs125jwz0QPvvAGmaGKB9QVA3Uq2geGrpiwZwEb5pA7V2uN3-jaqRKStB7--5PdsgU5a7Mf_hFXNPuJYaTWXRlMRDO4Pad_kCMCvjjo-soIyX6kmpHRC3BTNK6nsGSVoA-fOkj4whdqUuJq73urPGxwgjSXyuZpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۲
🔹
سپرده‌های بانک کشاورزی طی سه سال گذشته ۳ برابر شد
🔻
حجم منابع بانک کشاورزی با افزایش ۵.۵ برابری طی ۵ سال اخیر، از ۱۷۹ همت در تیرماه سال ۱۴۰۰ به ۹۸۳ همت در تیرماه ۱۴۰۵ رسید که ظرفیت این بانک را برای ایفای نقش مؤثرتر در حمایت از امنیت غذایی کشور با تأمین مالی بخش‌های مولد، به‌ویژه کشاورزی و صنایع غذایی تقویت کرده است.
🔻
شتاب رشد منابع این بانک در سه سال اخیر، به طور محسوسی افزایش یافته و از ۳۰۲ همت در تیر ۱۴۰۲ به ۹۸۳ همت در تیر ۱۴۰۵ رسیده که بیانگر افزایش ۶۸۱ همتی و رشد بیش از سه برابری سپرده‌های بانک در این بازه زمانی است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/679685" target="_blank">📅 14:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bd56a25b.mp4?token=uUZJAR__eB3L5kh8I-QHbpxomRfAxF0rkmxh-kUhCO0AHecaklcswAgjbM9fM_uzs8LSM8uhvgZEuhy4rvB3IZi4x_ZKtgUid4Me8uWP6OQ6Mtj7YvWtxCpV5nJuPya6Upc-PyN2qGZqu-8-H6Yghu-ReViRBKnfsA-Uz5dqf612ihihVNMB9EmG37XBV9NL0ybuc-jBadEYzycFejS4VIMWv-ONUZnp4XfC6BLsst0_DefnTB6jFFyzsFdfReGIZkPgNeFBcT89ElgTUQuxYDhlXu_rUoU1y2gOkwgt1inc9h5akqhCcRQ7RyOvotTOYGTnrT2QX7XlkNFzYBnNz1wWLiaAPyUCwNbbdvfPdObvz6O-9JVzTYwNFAjkqbm4ggmAGu7a1IZK-3fjDd4_6OqOcw5g73UQn96SNS-ETT0Lzr1Zs4_VWtMqnH4Z-Y0bzxV8bwYxEGm_5Eb4OL5RB_yXI2uUs1CN2CzC8Bm-6cvFwg2jfyRsXv_PwPXL_AOwGCVqIQ-jRTFSUjElCH7EwUqYM99UY-nuBb_GwGBoUagd_2Q0axfrnUPyvrU9eBnIFhwn6Qu1_Ct8XSi1sL87ELU_Mm51yVVQwtLnQCmLryniUIq8ecPtb-b_LZVktJ-M5M5VymLSU2ol9eTNMrSzS1zNfo2KVpo8hEm0tJ4cs1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bd56a25b.mp4?token=uUZJAR__eB3L5kh8I-QHbpxomRfAxF0rkmxh-kUhCO0AHecaklcswAgjbM9fM_uzs8LSM8uhvgZEuhy4rvB3IZi4x_ZKtgUid4Me8uWP6OQ6Mtj7YvWtxCpV5nJuPya6Upc-PyN2qGZqu-8-H6Yghu-ReViRBKnfsA-Uz5dqf612ihihVNMB9EmG37XBV9NL0ybuc-jBadEYzycFejS4VIMWv-ONUZnp4XfC6BLsst0_DefnTB6jFFyzsFdfReGIZkPgNeFBcT89ElgTUQuxYDhlXu_rUoU1y2gOkwgt1inc9h5akqhCcRQ7RyOvotTOYGTnrT2QX7XlkNFzYBnNz1wWLiaAPyUCwNbbdvfPdObvz6O-9JVzTYwNFAjkqbm4ggmAGu7a1IZK-3fjDd4_6OqOcw5g73UQn96SNS-ETT0Lzr1Zs4_VWtMqnH4Z-Y0bzxV8bwYxEGm_5Eb4OL5RB_yXI2uUs1CN2CzC8Bm-6cvFwg2jfyRsXv_PwPXL_AOwGCVqIQ-jRTFSUjElCH7EwUqYM99UY-nuBb_GwGBoUagd_2Q0axfrnUPyvrU9eBnIFhwn6Qu1_Ct8XSi1sL87ELU_Mm51yVVQwtLnQCmLryniUIq8ecPtb-b_LZVktJ-M5M5VymLSU2ol9eTNMrSzS1zNfo2KVpo8hEm0tJ4cs1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرزند شهید لاریجانی: شهید لاریجانی درباره حوادث ۱۴۰۰ [ رد صلاحیت] گفتند: «آبروی هر کسی متاعی است که خدا به او می‌دهد و ما باید وظیفه خودمان را انجام بدهیم اگر وظیفه را درست انجام بدهیم خدا می‌داند کی و کجا آبروی ما را تدارک کند»
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/679681" target="_blank">📅 14:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaAH7EGaSzhwr2iNuxq8mPkoiHNycr84bUYxUJwocofoF6wo9jRFiKXlXqU7NB6Fe4qxDBPk1k8MaOw6JBAapbz9KBr_SPYlHKh0bfM_85NhZzZQ1GF0gxmaVyqSe_xG4tWZ5TcOjykD9UHej4vYVlPqd4WOvMSOeGqf923leeuLb0uNBrlIqTdrh-Q37LsDAR5S_KBxMYo52deSSfqQX1DRyscQhNlyc256gVNuqbcoXaX4QgufU_q45KONsTrvL5X3c_lUu5qJCCyDDWsGqR5APsySCPcgopA0ECS8C820egqJIwY638ayJX1bR2YMc03Hc46b4QLNK3PqdSr1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قریشی: تصاویر حضور رهبر معظم انقلاب در جلسات با فرماندهان منتشر می‌شود
جانشین سازمان بسیج مستضعفین:
🔹
تصاویر و مستنداتی که در آینده از حضور رهبر معزز و فرمانده کل قوا حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای (حفظه‌الله) در میان مردم و کوچه و خیابان و جلسات با فرماندهان نیروهای مسلح منتشر خواهد شد، بار دیگر موجب رسوایی دشمنان و بدخواهان ملت ایران خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/679680" target="_blank">📅 14:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679679">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcKP7evuI99gs1KwAAqPgW8DVmvn7E4hDJfzVvtv_VE0XQR3W7IYwo0XlwMFjoZ_e1GUnrl6xZUUiBvo0D1s3oIPCs5gblLue2Q3gLmPOxTP77wRblSbKs0Y-XHy_8w5qyTBze_uQleBv55WeHg3m2xuvi3dE0tawuwvcP9Xwo_KpPpeYaOSMcjSMU8-8ijoSPmDTMctt8Csv2QzYPElvJGRJD_XQJJs5MVdyijpT0YnLzEL02GCjwWpr_5ra068t4EuialrZYqqVMKPMB54byIvcwBD0EGV1OaXDi4ErWAtS2YIKmPTp4G-_CyAkV5fyR9u5AO0a1gDA-Y0qnNaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
۳ ماه استفاده رایگان از سوپرپوز بارکد!
اگه دنبال یک راه ساده‌تر برای مدیریت فروشگاهت هستی، سوپرپوز بارکد می‌تونه مدیریت فروش و صندوق رو برات راحت‌تر و دقیق‌تر کنه.
🧾
📊
❇️
حالا می‌تونی با یک پیشنهاد ویژه،
۳ ماه رایگان از سوپرپوز بارکد استفاده کنی.
⏰
برای استفاده از این پیشنهاد فقط تا
۲۴ مرداد
فرصت داری.
📩
برای اطلاعات بیشتر، روی لینک زیر کلیک کن!
https://Snappbarcode.com/product/superpos</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/679679" target="_blank">📅 14:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679678">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما بزرگ‌ترین آسیب استفاده بیش از حد از شبکه‌های اجتماعی چیست؟</h4>
<ul>
<li>✓ افت تمرکز</li>
<li>✓ اختلال در خواب</li>
<li>✓ اخبار زرد و شایعات</li>
<li>✓ آسیب به ارتباطات حضوری</li>
<li>✓ کاهش بهره‌وری</li>
<li>✓ سایر</li>
</ul>
</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/679678" target="_blank">📅 14:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679676">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcacf87c4c.mp4?token=vaYpcNabbFNi5vLBL0t87GdE4J5PwFrkPe9hy1gi-iGrBX1O2fD4klyj3LhlNOkIX-YmPXCFj2m3vvA-v5y7_bvwuDSHM_1oqg3o2OcNReri9NiNWGCz7F5kkWezMyEu8sVaG8KmuvuH7jDv6qkZwAMk8ZJqVdL2z4Yl3P0yiH3hoZDm7bj_RnjYWnIfIH1mkDfKZy-ePl-1IK7QaXc6Xhg-YMsYMrscLOKApD2crUKh6Ni5BpognsYRZgN6gPR9QRNzmQCN9AHPaau5-nMq1dGdJmJD9MvEBAZobnJIZeXZYidg8wLVuGGS4TRaAeXio7j_QEaupZaUKE4DECZqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcacf87c4c.mp4?token=vaYpcNabbFNi5vLBL0t87GdE4J5PwFrkPe9hy1gi-iGrBX1O2fD4klyj3LhlNOkIX-YmPXCFj2m3vvA-v5y7_bvwuDSHM_1oqg3o2OcNReri9NiNWGCz7F5kkWezMyEu8sVaG8KmuvuH7jDv6qkZwAMk8ZJqVdL2z4Yl3P0yiH3hoZDm7bj_RnjYWnIfIH1mkDfKZy-ePl-1IK7QaXc6Xhg-YMsYMrscLOKApD2crUKh6Ni5BpognsYRZgN6gPR9QRNzmQCN9AHPaau5-nMq1dGdJmJD9MvEBAZobnJIZeXZYidg8wLVuGGS4TRaAeXio7j_QEaupZaUKE4DECZqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: دشمن آدم‌هایی را ترور می‌کند که گره‌گشا هستند
🔹
برادران نظامی در سپاه و ارتش کاری کردند کارستان؛ با ایستادن مقابل دو قدرت اتمی، دنیا را به حیرت وادار کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/679676" target="_blank">📅 14:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679674">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/560ac12c6d.mp4?token=V4Fsq01Pv_mqesKZp3gz7bOkpceDD6oNuSdKovue88o08vz99PHmPLkFbk5FAKpdzJuNHKRI40tG_yi7hewSVgpo2gxq7RM-dy0ZBvT5qUQELNvHue9GkRMNiWIX_Z6ajPsYwZMf6fPF603jAutMksbCFyAcjFsNc_mlEnpqOtsFilzOX_MsBGoCbGAv9UQQ-E_rwXq2meTmACEzpjlg2TTEDlCuY--hMFCFtL4MPDaN1i8QKYiz0szd5Tr6eZnfRNoKUiUbFe5Bq85Y4NVbfTN72SWIKmaxJ98c7qiEiErTND4Dco3ufFCFfWFf2VYsyWzn4mT__kMnh4QBlqNcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/560ac12c6d.mp4?token=V4Fsq01Pv_mqesKZp3gz7bOkpceDD6oNuSdKovue88o08vz99PHmPLkFbk5FAKpdzJuNHKRI40tG_yi7hewSVgpo2gxq7RM-dy0ZBvT5qUQELNvHue9GkRMNiWIX_Z6ajPsYwZMf6fPF603jAutMksbCFyAcjFsNc_mlEnpqOtsFilzOX_MsBGoCbGAv9UQQ-E_rwXq2meTmACEzpjlg2TTEDlCuY--hMFCFtL4MPDaN1i8QKYiz0szd5Tr6eZnfRNoKUiUbFe5Bq85Y4NVbfTN72SWIKmaxJ98c7qiEiErTND4Dco3ufFCFfWFf2VYsyWzn4mT__kMnh4QBlqNcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرشایمر، استاد مشهور روابط بین‌الملل:
ترامپ فهمیده امکان پیروزی در جنگ علیه ایران وجود ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/679674" target="_blank">📅 14:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679673">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f7a472772.mp4?token=dISdG4DFEttwUbPytxVcj5O85O0JbdX_Whpqwwt-7pvV6-nz_E3_fftll9Z_kFwU9VYoUasyNtqcVyO86iH3YW4y3WV7mAHOxxdYn6KKNRFogBLgMhhOyKW3YM-u8QxjrSz9kfNltxbykJOz4X9q_nj8OPC5rIh-H-PGCLGzhIZ7SAdsFNDA-kZz8K4N84dSiNjNh3hoE_V4v9cTGjyJjN8Cu1eeNExvwoH0eCg3JWhxdqbiW3XR6pPHVODLx1G8P6MWh-N_dvgkwWkzgrnYDpnX9O-HwvR0gBCY7oWHAlX9ajzsVaWGsV-OSeqdGgj9y0q-nJN8PY0SlhGHn742UYS-MpgnJM1HyiYOmccmpf8Fz4WdQIsDXC8uDx8NNstAri4ixA0oGYnAZ8djV0B5ujKyv7-GwEnZsiZp3VUR0Wlyqa5vtOxHf0HiS9xKhMOg0ThwWRI9MKq1XiHf1ZcKEclRvWkXQvgte9uywhW1V41lJ_0jxOEheTWkheme0xoKuK7buYoKDg5wMjzjh_xibnEkb9GGbjBc3zGDARwQ-VqMitiqxcs5hnjNs9NCVXNrUFxQ9LjQYqqVd57mtRHWgRUOKS89gyhCumboJYtJUqGEge0VoHClb-XTkRQVDDFCPdHyF6IaP2vhYeX1Wmh8S_5K5AR1JtwBQ0QhiLzuNTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f7a472772.mp4?token=dISdG4DFEttwUbPytxVcj5O85O0JbdX_Whpqwwt-7pvV6-nz_E3_fftll9Z_kFwU9VYoUasyNtqcVyO86iH3YW4y3WV7mAHOxxdYn6KKNRFogBLgMhhOyKW3YM-u8QxjrSz9kfNltxbykJOz4X9q_nj8OPC5rIh-H-PGCLGzhIZ7SAdsFNDA-kZz8K4N84dSiNjNh3hoE_V4v9cTGjyJjN8Cu1eeNExvwoH0eCg3JWhxdqbiW3XR6pPHVODLx1G8P6MWh-N_dvgkwWkzgrnYDpnX9O-HwvR0gBCY7oWHAlX9ajzsVaWGsV-OSeqdGgj9y0q-nJN8PY0SlhGHn742UYS-MpgnJM1HyiYOmccmpf8Fz4WdQIsDXC8uDx8NNstAri4ixA0oGYnAZ8djV0B5ujKyv7-GwEnZsiZp3VUR0Wlyqa5vtOxHf0HiS9xKhMOg0ThwWRI9MKq1XiHf1ZcKEclRvWkXQvgte9uywhW1V41lJ_0jxOEheTWkheme0xoKuK7buYoKDg5wMjzjh_xibnEkb9GGbjBc3zGDARwQ-VqMitiqxcs5hnjNs9NCVXNrUFxQ9LjQYqqVd57mtRHWgRUOKS89gyhCumboJYtJUqGEge0VoHClb-XTkRQVDDFCPdHyF6IaP2vhYeX1Wmh8S_5K5AR1JtwBQ0QhiLzuNTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وششم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ دو بانو که هر دو بزرگوار در هنگام عمل جراحی زایمان روح از جسم‌شان جدا شده و موارد ماورائی از جمله جسم بلوری زنده، هم صحبتی با نوزاد در حال متولد شدن و رفتن به مکان بهشتی و رویت درختان رنگارنگ و آب روان گوارا را مشاهده و لمس کرده اما به خاطر وابستگی به فرزند، بازگشت به زندگی دنیوی را از خداوند طلب می‌کنند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود
#تجربه‌گران
: نفیسه متعبد/ منیره محمدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/679673" target="_blank">📅 14:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679672">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
دیدار و گفتگوی رئیس‌جمهور با رهبر معظم انقلاب درباره مسائل اقتصادی و نظامی کشور
🔹
مسعود پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفتگو کرد.
🔹
در این دیدار به تفصیل درباره مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آینده پیش‌رو، تحولات حوزه نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/679672" target="_blank">📅 14:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679670">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13d19fe1d8.mp4?token=b0i1vPtBLogPGLGc4zTi5bpx5gIkUVwcNNP23U1Evm0DqD89lworBoWcvVNJCoV9YmSWXxduYhYgzw5wtjG1f358tRigV-ZE1pWPlstNNsIhGt04JoMNKzNiPuxTi5LMoPN-XZLyEikAKKrIXcw6v0SWdE5naNB3A8ABSFQhUj6lIpzzeYm8hgj3-MVN17Vuvl0zbWI1Nc-r6y9VHTt9PkGqFc_WOfupPOZve4DC4gYMLtUEAadH88qQmVyYTMIYY2_7tjIs10uT5K9jj_FrSd8BohvVi5uN_lbheLUpcHC__9zJzmYiS7094-AHb96QF1Htl4_JjVnhC3pd-aCQgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13d19fe1d8.mp4?token=b0i1vPtBLogPGLGc4zTi5bpx5gIkUVwcNNP23U1Evm0DqD89lworBoWcvVNJCoV9YmSWXxduYhYgzw5wtjG1f358tRigV-ZE1pWPlstNNsIhGt04JoMNKzNiPuxTi5LMoPN-XZLyEikAKKrIXcw6v0SWdE5naNB3A8ABSFQhUj6lIpzzeYm8hgj3-MVN17Vuvl0zbWI1Nc-r6y9VHTt9PkGqFc_WOfupPOZve4DC4gYMLtUEAadH88qQmVyYTMIYY2_7tjIs10uT5K9jj_FrSd8BohvVi5uN_lbheLUpcHC__9zJzmYiS7094-AHb96QF1Htl4_JjVnhC3pd-aCQgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با هر رنگ شلوار چه رنگ لباسی ست کنیم؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/679670" target="_blank">📅 14:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679668">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6880194a73.mp4?token=vrvtqV1CUTMLLtst4nVv0rUNHaYL8kGyC525KnsTyXD6YtI_A77bN0b539JMNFiQvchCeik_CnqLWKVAReG7reIBJ5CclVGOIuSfvUpAT5qrFa99CNUCB97w0Z6lUYCi5hKsHynDTScAOvB6L2p739qSNSP-9kA374MWZ8gtHYfAPNa378Nfsy6ibxRuJS2SnH7bCqTiZVFt3bwoac7h38xPblgfYEMcTHuWo3oU9Z-eX7QueGllB0XX4xXb8gL03a9IV1Ecv6crOxE1RxB3E-RKfNzuECT1fulIxs7zE5JvjnZOOduzek-3kbm9_aQJvF2Hzzo6qSrk-vs9YyHVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6880194a73.mp4?token=vrvtqV1CUTMLLtst4nVv0rUNHaYL8kGyC525KnsTyXD6YtI_A77bN0b539JMNFiQvchCeik_CnqLWKVAReG7reIBJ5CclVGOIuSfvUpAT5qrFa99CNUCB97w0Z6lUYCi5hKsHynDTScAOvB6L2p739qSNSP-9kA374MWZ8gtHYfAPNa378Nfsy6ibxRuJS2SnH7bCqTiZVFt3bwoac7h38xPblgfYEMcTHuWo3oU9Z-eX7QueGllB0XX4xXb8gL03a9IV1Ecv6crOxE1RxB3E-RKfNzuECT1fulIxs7zE5JvjnZOOduzek-3kbm9_aQJvF2Hzzo6qSrk-vs9YyHVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیکنی از باشگاه برزیلی کوریتیبا هنگام شادی پس از گل، به داخل تونل رختکن افتاد
🔹
پس از این حادثه، گل مردود اعلام شد و بازیکن به دلیل مصدومیت تعویض شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/679668" target="_blank">📅 13:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679664">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFoZiW3wIfZPfsaxeGhbfn4LZdfsOG3-5yd-wAiKBOZc_VI3sDnWlZd7HsNDhGL4Zuf4T9v2kWWTvHlGe7ALI6tNCSPYuohA1Cp56mGG70iJ7QaJQjvr7eQ3CgKZ65SwvQ8BGTM8Q_JCSM2wBHc1f8Rme3ltazmYAs_8zaHQLZKBgHV1FxJUAtra1pI2P7Y_A38PxnF31W5RumtzsmlORbhsgGIixvCiNrX5EkFHyQHMvtey0yhWOlwcUSPP3WIhtVbMHKIVlCNMKJrePIBqRnKS94DiO8KcfMxJ757DY1QLBxAmIzpMGCb-VHPLww2K839Pglr_9mfgckMpKrgZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۸ مرداد ۱۴۰۵؛ ساعت ۱۳:۲۵
🔹
بازار ارز امروز تقریبا در سکون سپری شد؛ قیمت دلار که روز گذشته نوسانی بود، امروز در پی ابهامات سیاسی و رویکرد محتاطانه معامله‌گران، با تغییر کمی نسبت به روز قبل به ۱۸۶ هزار و ۴۹۰ تومان رسید./ تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/679664" target="_blank">📅 13:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679663">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
توضیحات سخنگوی وزارت کشور درباره پلمب برخی کافه‌ها به دلیل بی‌حجابی
🔹
تغییری در تعلیق قانون حجاب بوجود نیامده است.
🔹
این موارد پلمب در شورای امنیت کشور مطرح می‌شود و در مسیر خود پیگیری می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/679663" target="_blank">📅 13:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679661">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزارت نفت، نهاد ریاست جمهوری را به پرداخت ۱۳۸ هزار میلیارد تومان خسارت محکوم کرد!
🔹
در‌ یکی از کم‌سابقه‌ترین‌ دعواهای حقوقی در دولت، شرکت سرمایه‌گذاری اهداف زیر مجموعه وزارت نفت، نهاد ریاست جمهوری را به پرداخت ۱۳۸ هزار و ۵۶۰ میلیارد تومان خسارت محکوم کرد.
🔹
طبق گزارش سایت دیدبان ایران؛ این دعوی که در شعبه ۹۲ دادگاه عمومی حقوقی مجتمع عدالت قضایی تهران علیه سازمان‌ خصوصی‌سازی و نهاد ریاست جمهوری مورد بررسی قرار گرفته بود ،ششم مرداد منجر به برائت سازمان خصوصی سازی و محکومیت نهاد ریاست جمهوری از سوی این دادگاه شد.
🔹
وزارت نفت به دلیل از بین‌ رفتن وصف مدیریتی خرید بلوکی ۱۲ درصدی شرکت صنایع پتروشیمی خلیج‌فارس ، ناشی از مصوبات بعدی هیئت وزیران که مابقی سهام دولت در «فارس» را هم به صورت بلوکی عرضه کرد ،شکایت کرده بود.
🔹
وزارت نفت (شرکت سرمایه‌گذاری اهداف )تاکید کرده با استناد به وصف مدیریتی این سهام در مزایده سازمان خصوصی‌سازی در آذر‌ ۱۴۰۱ این معامله را انجام داده بود و با مصوبه بعدی دولت در دی ماه همان سال حالا نمی‌تواند برای ۱۲ درصد سهم بلوکی خریداری شده یک عضو هیات مدیره در شرکت صنایع پتروشیمی خلیج‌فارس را از آن خود کند.
🔹
این رأی در مهلت اعلامی قانونی ۲۰ روزه قابلیت تجدیدخواهی دارد و باید دید آیا نهاد ریاست جمهوری این رقم هنگفت را به زیر مجموعه وزارت نفت می‌پردازد یا این دعوی حقوقی وارد فاز جدیدی می‌شود؟/منبع: دیده‌بان ایران
https://www.didbaniran.ir/fa/tiny/news-328534</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/679661" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679660">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53546a9df0.mp4?token=XmJmuc9iumVX5AFMbRTAa362pQ_CTdjRCOj4vUToqIMlL3XHsK2zhjmF-myB_j5fB0Juy9p9QjgWj902DXx2T0O7NJga_Ri6KEv6n3LxaebB-fBzwfforZrbP7vSoralCg-WYszysVMkflBileA0bXXQpcYzpinSIwKLSnhaioda2Sd9Tf5sOZMGRobqRMXj5fqXBVNlD-n7j0gI_0-wRocYgG4uRPV7UNRbfS6LDqbEplx3SorH_NHlB1oTYGdxdeVGkK9h76sAJxNnjh7MPIOJcOaLusPo5ZHVljCqokjBeZ-SVUPJ6956IOvrPzUt98ovRXN7RlXPJsSo1InYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53546a9df0.mp4?token=XmJmuc9iumVX5AFMbRTAa362pQ_CTdjRCOj4vUToqIMlL3XHsK2zhjmF-myB_j5fB0Juy9p9QjgWj902DXx2T0O7NJga_Ri6KEv6n3LxaebB-fBzwfforZrbP7vSoralCg-WYszysVMkflBileA0bXXQpcYzpinSIwKLSnhaioda2Sd9Tf5sOZMGRobqRMXj5fqXBVNlD-n7j0gI_0-wRocYgG4uRPV7UNRbfS6LDqbEplx3SorH_NHlB1oTYGdxdeVGkK9h76sAJxNnjh7MPIOJcOaLusPo5ZHVljCqokjBeZ-SVUPJ6956IOvrPzUt98ovRXN7RlXPJsSo1InYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده نیروی زمینی ارتش: پای نظامی آمریکایی به ایران باز شود، آن را قطع می‌کنیم؛ به هرگونه اقدام دشمن، پاسخی قاطع و بازدارنده خواهیم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/679660" target="_blank">📅 13:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07b738d82.mp4?token=EZaTZY6n0E7NoO5vHmGUHwnJ6FGFRSRV2N5ve19LvGw9gidzK0fZPIXj_j-zX-xFMgKa2kQVp33pMyojIQ0bTL_4COCnCW3OKsRhoI5IY-k9Z78up-5AosDd8DepMRRBG03cJLdKZs4wZA3xihBgV0d0mNZET9uXCNLWExewqHPNiD4MtHMKsVZ16FbmwaU59DHOdVb5BN1BqqULu5F36LTWSjvsqeKBYlCrmZROIGOxkQ-CGx9CRYbyAAdm9hofkIN15tROI0HIcK9k_wj0Mm81H8wB9luK5vjCIa1tVBQw8LFPvC6pK_B4zGZubbJr4Xw19SmL_gmUvG1fvUS4cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07b738d82.mp4?token=EZaTZY6n0E7NoO5vHmGUHwnJ6FGFRSRV2N5ve19LvGw9gidzK0fZPIXj_j-zX-xFMgKa2kQVp33pMyojIQ0bTL_4COCnCW3OKsRhoI5IY-k9Z78up-5AosDd8DepMRRBG03cJLdKZs4wZA3xihBgV0d0mNZET9uXCNLWExewqHPNiD4MtHMKsVZ16FbmwaU59DHOdVb5BN1BqqULu5F36LTWSjvsqeKBYlCrmZROIGOxkQ-CGx9CRYbyAAdm9hofkIN15tROI0HIcK9k_wj0Mm81H8wB9luK5vjCIa1tVBQw8LFPvC6pK_B4zGZubbJr4Xw19SmL_gmUvG1fvUS4cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه وحشتناک حین مسابقات سوارکاری در قرقیزستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/679655" target="_blank">📅 13:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/672ca2289c.mp4?token=vVIo4VHszlmglr746oe0YcrNv5RwU36c5x4yx_tdAQsamCsC_Kj_BxI97IZDBhybotILIg_zCRLO5TOVnZCnxa-RwsHTylN2mpgyVVdZL7aMz4yL8yegXKEIJH_a4yTs1kx5s2Mp-1siyLyWCx7ONRGXlp1IJidz8QdDplP8SGJH34W4iFa16-Dg6zCafTdZnsqGm3L8jz0AQdfXvYaY3KL2_yNXoVVhtcDFHOOcQj-vVAziqXrCUuBa_-K_eFrWUUrbXdpMGlPigv61-10UBQ4FZgENyc0zAKyrx-hbR_IxZi8CmYJy6nIIU--FxqaCKYQmNdpSPXMo2HZrLQxYTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/672ca2289c.mp4?token=vVIo4VHszlmglr746oe0YcrNv5RwU36c5x4yx_tdAQsamCsC_Kj_BxI97IZDBhybotILIg_zCRLO5TOVnZCnxa-RwsHTylN2mpgyVVdZL7aMz4yL8yegXKEIJH_a4yTs1kx5s2Mp-1siyLyWCx7ONRGXlp1IJidz8QdDplP8SGJH34W4iFa16-Dg6zCafTdZnsqGm3L8jz0AQdfXvYaY3KL2_yNXoVVhtcDFHOOcQj-vVAziqXrCUuBa_-K_eFrWUUrbXdpMGlPigv61-10UBQ4FZgENyc0zAKyrx-hbR_IxZi8CmYJy6nIIU--FxqaCKYQmNdpSPXMo2HZrLQxYTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنرنمایی آهن و الگوریتم در فنجان قهوه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/679652" target="_blank">📅 13:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7cf5c281.mp4?token=IXj-FaEGkyYLnyUZlURM-rJrm4633VuNErlME75V9zUqqMA8KHGQEA9uzfasXRjE7qj4Hngw1zNY_t-7khfAxoPyOFWyorhO0zGroUYDYuW-tYnMcWlEWomxJTMKNq1grnmDyuybBbhHxfMFbvX_15zLDceLk5uNqaUvpqFR-gbWd3kOHwmpZmIhtAN3NqOIVYYJfzVdF1xJzd9iYwnN8oAaQYFbuMLBCkvEpvI0GHKT4JFpj7LbOpvAceplQ6LYaAgIjUCI64-j1rBkrC_iOTVir6jjV1jeNkK4kT5exJBrJfrTGUZG8l1eduiiI6Ds1Ew3xrfeJgoQjvlof8vHxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7cf5c281.mp4?token=IXj-FaEGkyYLnyUZlURM-rJrm4633VuNErlME75V9zUqqMA8KHGQEA9uzfasXRjE7qj4Hngw1zNY_t-7khfAxoPyOFWyorhO0zGroUYDYuW-tYnMcWlEWomxJTMKNq1grnmDyuybBbhHxfMFbvX_15zLDceLk5uNqaUvpqFR-gbWd3kOHwmpZmIhtAN3NqOIVYYJfzVdF1xJzd9iYwnN8oAaQYFbuMLBCkvEpvI0GHKT4JFpj7LbOpvAceplQ6LYaAgIjUCI64-j1rBkrC_iOTVir6jjV1jeNkK4kT5exJBrJfrTGUZG8l1eduiiI6Ds1Ew3xrfeJgoQjvlof8vHxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرزند شهید لاریجانی: شهید لاریجانی درباره حوادث ۱۴۰۰ [ رد صلاحیت] گفتند: «آبروی هر کسی متاعی است که خدا به او می‌دهد و ما باید وظیفه خودمان را انجام بدهیم اگر وظیفه را درست انجام بدهیم خدا می‌داند کی و کجا آبروی ما را تدارک کند
»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/679651" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679649">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f3dde333.mp4?token=Dsisq19lh0-nbFUPZjEuTetSgTjhIVdAGCwF0TVgPjHRD9rodauMlq0OrBVW_Lr6acPKo4_n240creB5fT3mMOJ3xuNAGRnXG90KBzAEkGJHolU6iXxgRgxOoJn8JfYoRNIbeX4uj9jXquuJs1eXAQY9ZGvvAaWJLezGBPDD4Ck_FKK1a8sRzxhEMlhX28YgYkLrkitfcExpA1LQn8UrLxf_G4PXu-OpYHp6_MQNFHb3cEWSUK0Oj6y3PMkSaH-9WamZ7ugPqW9EzIQLrn5nvl7ER_Z6wRpOVugibwERmKWsu1efIv4rzrs2xwFurFL5xd9jPUYDcdvo9EOnJlErTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f3dde333.mp4?token=Dsisq19lh0-nbFUPZjEuTetSgTjhIVdAGCwF0TVgPjHRD9rodauMlq0OrBVW_Lr6acPKo4_n240creB5fT3mMOJ3xuNAGRnXG90KBzAEkGJHolU6iXxgRgxOoJn8JfYoRNIbeX4uj9jXquuJs1eXAQY9ZGvvAaWJLezGBPDD4Ck_FKK1a8sRzxhEMlhX28YgYkLrkitfcExpA1LQn8UrLxf_G4PXu-OpYHp6_MQNFHb3cEWSUK0Oj6y3PMkSaH-9WamZ7ugPqW9EzIQLrn5nvl7ER_Z6wRpOVugibwERmKWsu1efIv4rzrs2xwFurFL5xd9jPUYDcdvo9EOnJlErTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از سرگرمی‌های تابستان برای بچه‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/679649" target="_blank">📅 12:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679648">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمرکز اطلاع رسانی بانک صنعت و معدن</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoXSO7E1ETtP5VL9RS0ABopTextNtRaL4LY4C6Fm7Dp8tgLWdba5h_lpHGkT1mZh8NZmff7paMKwupX4_ePF1qQtVWDZkD0_KBDvMqnS-Hopb3iwn6uCmuRb3W3P302iQIIhn42W-bR9OFZyTUNSGGIX4h5so2NmOl0a1A2HhtJW7cC4Hz7nEuAxkxichC7W0IM5L-3Sys9RZuIVJE191MVTL15aAknWeI3D5ptj0R8FRvcOqy0Ak4NS2dueGTIsCx2MjFamz7C9TzflEHnI0mwck-OIw6muZT4VFTaT4VWz_KbvzvZTd3GG8zUspey2VZBo97uayJBAjmZ4Zd1sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بانک صنعت و معدن؛ پیشران تأمین مالی صنایع راهبردی و توسعه تولید کشور
🔹
بانک صنعت و معدن با تأمین مالی هدفمند در صنایع پیشران و زیرساختی، نقش مؤثری در توسعه تولید، تکمیل زنجیره ارزش و ایجاد اشتغال پایدار ایفا کرده است.
▫️
بیش از ۱۳.۲ میلیارد یورو تأمین مالی ارزی
▫️
بیش از ۲.۵۹۲ هزار میلیارد ریال تأمین مالی ریالی
▫️
ایجاد حدود ۹۷ هزار فرصت شغلی مستقیم
▫️
این حمایت‌ها طیف گسترده‌ای از صنایع از جمله نفت، گاز و پتروشیمی، فولاد، نیروگاهی، صنایع شیمیایی، غذایی، دارویی، خودرو، ساختمان و صنایع فلزی و پایین‌دستی را دربر گرفته است.
سایت
|
بله
|
تلگرام
|
اینستاگرام</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/679648" target="_blank">📅 12:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679647">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
دخانیات پای ثابت ۴۰ درصد سرطان‌ها در مردان ایرانی
وزارت بهداشت:
🔹
۴۰ درصد سرطان‌ها در مردان و ۲۱ درصد سرطان‌ها در زنان ایرانی با عوامل شناخته‌شده‌ای مانند مصرف سیگار، قلیان، تریاک و چاقی ارتباط دارد.
🔹
دود سیگار، قلیان و ویپ بیش‌از ۷ هزار مادهٔ شیمیایی دارد که دست‌کم ۷۰ مورد آنها سرطان‌زا هستند؛ قلیان هم برخلاف تصور رایج، گزینه‌ای کم‌خطرتر از سیگار محسوب نمی‌شود.
🔹
در گروه سنی ۱۸ تا ۲۴ سال، مصرف دخانیات در زنان ۹۰ درصد و در مردان ۳۴ درصد افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/679647" target="_blank">📅 12:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679645">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی وزارت کشور: توهین به رییس جمهور جرم است.
🔹
اعضای باند تولید و فروش سکه‌های طلای تقلبی در قم بازداشت شدند.
🔹
ایمان انوری، مجروح حمله اخیر آمریکا به سایت راداری جبالبارز کرمان شهید شد.
🔹
نخست‌وزیر و وزیر جنگ اسرائیل دستور دادند که تاسیس شهرک جدید در منطقه رفح غزه آغاز شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/679645" target="_blank">📅 12:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679640">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svWbvSigPHf3P0GBVHRjuBANFPUugoqsfsmY8sG9BsYURRXdWug1jd5GgyTZAgy8KNPhMds-7y7toluKJsDMxZfaFFB-zGtGp9nDXeOom77jt4F-iE6D8oA6f2HEok-7CGvK-b8snmPebGsVOfgJm3myZkH4bJ-l9btQbEo-eFr8iOuDFe7hAtNjEdgpRXfF1XkH_QZoqacnAYQ8Jn3OH2c0ZM4Lmr290QhSH0Zf2yh7r0ekDeR6JtsDm_OAk1qxXBqwdNuGw3L-bB0WIbj7MBFmL0Dafp70ZKQ62Tf_gN3yLig-jSj2tl_Wwe4SajuPfA4umB47PJvZ6PHoyIIL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۰ ابزار عالی و رایگان برای دانشجویان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/679640" target="_blank">📅 12:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679638">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9172d880e3.mp4?token=e5JloZQ7U4qiPVxhFxKDHyY4CGo-3axGTviNoWH66eOhkWYT4q9l5Vbf913F7J1Pstwe28zE8xXmtYQpHeHKaLbdEFi593zofNz5TP76XUTstVicuzybZcsN7iXLcWvjnfR9TZQmkvEAL-_SWkQZddW2BtE6M2WRex6VlFy9D0CntArKU2eny3dXezZDo-h4Ph5qmg-h4XX8meHRN-IHqMxvJ0XF4DpavGop1IJeGqOVrhZHM8SNHNm-99szMARZ-r93pWWifqDilCFAg92ipZGUGpyi4P2QTVzbcoB0cfUaQd8ZS_iVLe_aS6omrgeyo-NWqrQqEN9rHHBRM3AUSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9172d880e3.mp4?token=e5JloZQ7U4qiPVxhFxKDHyY4CGo-3axGTviNoWH66eOhkWYT4q9l5Vbf913F7J1Pstwe28zE8xXmtYQpHeHKaLbdEFi593zofNz5TP76XUTstVicuzybZcsN7iXLcWvjnfR9TZQmkvEAL-_SWkQZddW2BtE6M2WRex6VlFy9D0CntArKU2eny3dXezZDo-h4Ph5qmg-h4XX8meHRN-IHqMxvJ0XF4DpavGop1IJeGqOVrhZHM8SNHNm-99szMARZ-r93pWWifqDilCFAg92ipZGUGpyi4P2QTVzbcoB0cfUaQd8ZS_iVLe_aS6omrgeyo-NWqrQqEN9rHHBRM3AUSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از حملهٔ سنگین دشمن صهیونیست به ارتفاعات علی‌الطاهر برای اشغال این منطقه با سو‌ءاستفاده از فرصت آتش‌بس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/679638" target="_blank">📅 12:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679636">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEcWRMmRNUQRWXEJ5BPLy31OhH4V31dX8rWvVJYBEnli8RBySkQGy8h7cV_lp6l5K0mPum280P9x6CvU9pm32BIaikwfBYShsw_fwzQfmHi_3Fvw1hvMQIVF8Sp4DYurx1bC85XbBLrTZ-ppaL0gNs481wLE3PAtKoghb_ZoJN48_OBk8qu2rzu5d3Z5wfgdGfn0K_2PK_TKmLP0ccPN94t8ktuyAlN4WQfNqrMr3fw9NReXZ3NPJFglyPYYRYznE1pUobxOG8nvYCwwbZ2UqDjCgTZ8INWQGcLArX-qkVGYVhDwd4dqVvdDw8-wI4kWWOdvJyBd68YXN04nN_OLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این هفته در دنیای فناوری چه گذشت؟ #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/679636" target="_blank">📅 12:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679635">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6949e4f923.mp4?token=fc4668iEvgja1I5n0nn_vUfj266kPzMoAEpbqbq6yTtNGvO6EOd2V848nk5Ooo5X7NOw6j8MCABupKndxWJmthMo-8jMhXdmR81ADliKFXZMyOXgwidEUot8CQNheRGvGe70E6uMCzVX11v65S205BpbREyUW07if0x5U6FvvY_VQVR0vI_YJpNTN-gyda4KtNCefgJ9h6S8jDpDc2qMgHv1fOsa1jt8SbR24gym-3tIbXdXU4lqcOP4BQZw_1uE1Vji_ERkX01TJ86Mu2vqWRCElJAl8XAERbtcLiElYt872zCC0tqYueskXdGcp_V5WTd_bP7gaCivmwSu0Wemv19uPLHM2-nl-zzTEpOfpKIVY3UMRhMAS3vrqixcEdNMpP78IVC19cshGNOGHakR6rw9R8bI5F7H7MKy89dWcQ1JG-yLUmX6I37RlxodOLpNDlgt13L9usFpHvyufXZAQkrj_HkwcHAeVvXNa9oKM6VsmFz8AG2NEXGNAkZJ-BKctQ4FjdkEL5LfxOKMRcXaQAxLZulUIqZ2AvcIdhaxyT5rs3WyO0ItaQoKYm5XVMy05CFHygAQCtLvsdvDD3cNQBpyGdFvgapD_fSo-NaOmXrxix0GOpLrG4baj0vXDusmBOQBDDo_gGp3SAM4WWX1GX8rdekYRCHuyQxXvjoEHDU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6949e4f923.mp4?token=fc4668iEvgja1I5n0nn_vUfj266kPzMoAEpbqbq6yTtNGvO6EOd2V848nk5Ooo5X7NOw6j8MCABupKndxWJmthMo-8jMhXdmR81ADliKFXZMyOXgwidEUot8CQNheRGvGe70E6uMCzVX11v65S205BpbREyUW07if0x5U6FvvY_VQVR0vI_YJpNTN-gyda4KtNCefgJ9h6S8jDpDc2qMgHv1fOsa1jt8SbR24gym-3tIbXdXU4lqcOP4BQZw_1uE1Vji_ERkX01TJ86Mu2vqWRCElJAl8XAERbtcLiElYt872zCC0tqYueskXdGcp_V5WTd_bP7gaCivmwSu0Wemv19uPLHM2-nl-zzTEpOfpKIVY3UMRhMAS3vrqixcEdNMpP78IVC19cshGNOGHakR6rw9R8bI5F7H7MKy89dWcQ1JG-yLUmX6I37RlxodOLpNDlgt13L9usFpHvyufXZAQkrj_HkwcHAeVvXNa9oKM6VsmFz8AG2NEXGNAkZJ-BKctQ4FjdkEL5LfxOKMRcXaQAxLZulUIqZ2AvcIdhaxyT5rs3WyO0ItaQoKYm5XVMy05CFHygAQCtLvsdvDD3cNQBpyGdFvgapD_fSo-NaOmXrxix0GOpLrG4baj0vXDusmBOQBDDo_gGp3SAM4WWX1GX8rdekYRCHuyQxXvjoEHDU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط در ۴ دقیقه با ترفند‌های مختلف شعبده‌بازی آشنا شوید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/679635" target="_blank">📅 12:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679633">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHM6iFbsg64ZDJqE_HcJb1oI7iJMZ3Vk3oFla9HwvnxM5IlDwBf4saYbItUqgznEq92jl6QtorB0s9ZeZFNjeh_aOxFWOjIG6_YAbfVGkHvTC98_n3STK88r32B9s_f_LSy4YEiHknkbx7EBlcOAPdVBbaFuLYe-eryp2MFwMHrK0oYxzr9_Asq2pcJ9bpHjUK6KA4XoqXmSciFcv_0YXQBM39taNswWZYIb27zNLAu86ca0Q98cTa8Ci8VO8aski2zy7XtQEQU1s12FXvxftsXL9JBRjQbt5ZPM8j2Uxr_JW__aGx4OF08jiSium1jF_CShBU68mQ4P8JCdnI2Xgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ب
رنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🏸
شروع روز با انرژی و حفظ سلامتی
ورزشی |
#ورزش_صبحگاهی
| ساعت ۸
🍱
انواع دستورهای خوشمزه
آشپزی |
#آشپزی
| ساعت ۱۰
🧠
سبک زندگی بهتر و ذهن آرام
روانشناسی |
#سلامت_روان
| ساعت ۱۲
✂️
آموزش داشتن استایل خوب و مناسب
فوری استایل |
#فوری_استایل
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
💡
معرفی انواع ترفندهای کاربردی
|
#ترفند_فوری
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/679633" target="_blank">📅 12:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679631">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9c3b5e72.mp4?token=iGfiXa4OWkbeA0ZF18IbxM3OeZ7p8vsgOsdnqhVa7Mw_OJRc5zsfUogf3pXp5y96b68Cf9w0CPW5s6IVvx-v5asFplbA9TThxpxqEtFV8yE0M9OmG7i4eXFkn7SjAz4JRS04_3awKkyIf__ldFExWnmuprmc6h8RIW11ne14vdUNSxNfcz54-Z0wmEpqK7hkvdZluHU1DLGO9a5HYFdKcZ9WL5FwcIQ6Rgin5S8YJwsUD5mbmrrnnLP6Ajsd46v-On38lNS1Kj0gFBaf_9tR19c1qJ-jVCeOprF6TiO2vc9tpYQy-HVFAKjRjOcVN1bk2aR1BtHzzcOejbbrJURfdr2UX4pR2SRciW6YUtWL3akwY4svrglJkf8TDEPH1eCqpwVf2Oz9AlayFf4i6dcNNlxN04GY7k7rGummmaML4ohv46ZpV0SvrujXceoz0tvPBxOkUK8bXFBifvbPRvu5hBkab_nOR_J5oxHgmSxq8wpF2A5_a0vhxrNtI17yfg7IS5BmzFBE5uVdu5erFcNZneWJccGVk5YutwBrW2TgA-CF9OHxOa8rVkjlOEHZAqHtyig8IU02_TBtW1MubEng4E6dcB1sZR0gDJTRaAN3VoDPQK37vVkS00ve9Enoy0kRpchEYpGsSBfKOEIWt2Oherw_cXgJjF8YSu4frgrFlnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9c3b5e72.mp4?token=iGfiXa4OWkbeA0ZF18IbxM3OeZ7p8vsgOsdnqhVa7Mw_OJRc5zsfUogf3pXp5y96b68Cf9w0CPW5s6IVvx-v5asFplbA9TThxpxqEtFV8yE0M9OmG7i4eXFkn7SjAz4JRS04_3awKkyIf__ldFExWnmuprmc6h8RIW11ne14vdUNSxNfcz54-Z0wmEpqK7hkvdZluHU1DLGO9a5HYFdKcZ9WL5FwcIQ6Rgin5S8YJwsUD5mbmrrnnLP6Ajsd46v-On38lNS1Kj0gFBaf_9tR19c1qJ-jVCeOprF6TiO2vc9tpYQy-HVFAKjRjOcVN1bk2aR1BtHzzcOejbbrJURfdr2UX4pR2SRciW6YUtWL3akwY4svrglJkf8TDEPH1eCqpwVf2Oz9AlayFf4i6dcNNlxN04GY7k7rGummmaML4ohv46ZpV0SvrujXceoz0tvPBxOkUK8bXFBifvbPRvu5hBkab_nOR_J5oxHgmSxq8wpF2A5_a0vhxrNtI17yfg7IS5BmzFBE5uVdu5erFcNZneWJccGVk5YutwBrW2TgA-CF9OHxOa8rVkjlOEHZAqHtyig8IU02_TBtW1MubEng4E6dcB1sZR0gDJTRaAN3VoDPQK37vVkS00ve9Enoy0kRpchEYpGsSBfKOEIWt2Oherw_cXgJjF8YSu4frgrFlnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختلال اضطراب با بدن ما چه ‌کار می‌کنه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/679631" target="_blank">📅 12:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679630">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
عراقچی: باز شدن تنگه هرمز منوط به یک سری شرایط است
وزیر امورخارجه:
🔹
مذاکره با عمان درباره تعیین مسیر دریایی جدید در تنگه هرمز است. ما در مرحله پایانی هستیم.
🔹
مسیرهای قدیمی با مسیرهای جدید جایگزین می‌شود. متخصصان در حال کار بروی مسیرها هستند.
🔹
البته این به معنای باز شدن تنگه هرمز نیست. این توافق ممکن است صورت بگیرد اما باز شدن تنگه هرمز منوط به یک سری شرایط است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/679630" target="_blank">📅 11:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679629">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سخنگوی پلیس: نفر اصلی دخیل در قتل حمیدرضا رجب‌زاده دستگیر شد/ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/679629" target="_blank">📅 11:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679627">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f780ae15a.mp4?token=MpVMfQGoitrogE9dj5VjkTDGoY595YS4yAZDZxKuoGR_ZjlO6AnvnPzCTxZxSy8MndD3UxRH-2xXb3z3Z9qUAVb43Xmzov5MHMD8LPsIrvgkpubxAiGA6PcUSYdOewYECgQkNQQG8DJIB49oE-STShvV9ll6q_k8UQZFzMSRNuTRJPDEiBHrxm8merD8VeXxiPRZryEkqjznvRew7Y5qJe7XB9FH-aByH3pzf2sA7eEcl8ur1gPTgzF447JgReEbOfC3YuYJlaf3fVO0rKsP9bYmWpJoKh83v-M0N6cphMBDItx_ftjF9UZl54EJtlWTGjx2dRIvNIdOKTGWMurdK2EXaQ1lt2ChGmKaY-7HNLq9dbeF93f5uJp-RPYK_raehkBrR10gqEdfaJo2q2OemRa-r73Yn-SUxifFY6vKW9Hj23SuM2Lt-vnqCGphjDoXIw-kDyKrwNy5GRSJz-lGKzuVNo4ZqwN8h4W4NF0_AzBpus46umhSVe0exEBc24z-Ocwv8AjSt_oRV2f5xomulh0fs71QUnBn5x-Bz7MFzsv4djXz-fykldyIiFeUD5m7Wwhle6kNa21BaMJtdMs2GWDPha_lOqUhjFZsB-EfPvztcRs4AcGnziialoBRtDNq5U6aldjc8quyw7v2kJRyLxstxaY_eqLJOdlNfmQiYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f780ae15a.mp4?token=MpVMfQGoitrogE9dj5VjkTDGoY595YS4yAZDZxKuoGR_ZjlO6AnvnPzCTxZxSy8MndD3UxRH-2xXb3z3Z9qUAVb43Xmzov5MHMD8LPsIrvgkpubxAiGA6PcUSYdOewYECgQkNQQG8DJIB49oE-STShvV9ll6q_k8UQZFzMSRNuTRJPDEiBHrxm8merD8VeXxiPRZryEkqjznvRew7Y5qJe7XB9FH-aByH3pzf2sA7eEcl8ur1gPTgzF447JgReEbOfC3YuYJlaf3fVO0rKsP9bYmWpJoKh83v-M0N6cphMBDItx_ftjF9UZl54EJtlWTGjx2dRIvNIdOKTGWMurdK2EXaQ1lt2ChGmKaY-7HNLq9dbeF93f5uJp-RPYK_raehkBrR10gqEdfaJo2q2OemRa-r73Yn-SUxifFY6vKW9Hj23SuM2Lt-vnqCGphjDoXIw-kDyKrwNy5GRSJz-lGKzuVNo4ZqwN8h4W4NF0_AzBpus46umhSVe0exEBc24z-Ocwv8AjSt_oRV2f5xomulh0fs71QUnBn5x-Bz7MFzsv4djXz-fykldyIiFeUD5m7Wwhle6kNa21BaMJtdMs2GWDPha_lOqUhjFZsB-EfPvztcRs4AcGnziialoBRtDNq5U6aldjc8quyw7v2kJRyLxstxaY_eqLJOdlNfmQiYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: اکنون هیچ مذاکره‌ای با آمریکا نداریم
وزیر امورخارجه:
🔹
واسطه ها همچنان دارند تلاش می‌کنند تا راه‌های مذاکره را مجدد پیدا کنند.
🔹
تا موارد نقض یادداشت تفاهم از سوی آمریکا به پایان نرسد و آمریکا انچه را که نقض کرده جبران نکند، از نظر ما امکان شروع مجدد مذاکره وجود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/679627" target="_blank">📅 11:45 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

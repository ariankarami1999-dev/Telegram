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
<img src="https://cdn4.telesco.pe/file/KAyfCbHIOFfzUwuAWOtccekW7gSsx-stCduXDCrodh-7kyzXjoigPxJV3SoIxHA8zxdpbPHeSLGw87HKbbk0w_NYDX6jk6q7R4fR1vVZa3RYWxDi9eczWZ6PIDy3_ZwZ1OLRA0f76ELPIV9CkB0bOk7G4qAxI5CvleCQcDzKvTQ0NCXV23UOSDhGblymCezE7Ray9RdV_PI8AXxe9EQRUaFFu5RUS26QLQhdftLtta33xT3ZLGZ5BbhJObLvZA5btKT_-Ir4QwG_BESiYNcxMrjeoFpjeR6HScg_lo_hhR87rgIs0O76k4Y2LGNOeQx6I3N9x1522ijtmO7QrfPMzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 13:49:48</div>
<hr>

<div class="tg-post" id="msg-7802">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔥
دانلود فایل های پولی، کاملا رایگان
- بخش دوم
خوب سری قبل گفتم تورنت چطوری کنیم لینکاشم گذاشتم، حالا یکی میگه من حال نمیکنم تورنت کنم چی کنم؟
یه سایتایی هستن که سرور های قوی دارن مخصوص تورنت، شما لینک تورنت رو میدی به اونا، اونا خودشون  فایل رو دان میکنن، بهت لینک مستقیم میدن!! و شما به راحتی با لینک مستقیم دانلود میکنین!
سایت سیدر یکی از از این سایت هاس برید توش ثبت نام کنین:
✅
www.seedr.cc
✅
با این لینک برید ۲.۵ گیگ بهتون فضا میده، ولی برین تو بخش Get space میتونین تا ۷ گیگ افزایشش بدین با انجام کار هایی که میگه
🏃‍♂️
خب حالا من لینک تورنت رو پیست میکنم تو این وبسایت و فایل ها رو بم نمایش میده، روش میزنم copy link و لینکش رو کپی میکنم، و میام تو تلگرام وارد هر ربات url to file بشین جوابه مثل ربات زیر:
@uploadbot
لینک رو بش میدم! و به همین راحتی فایل تورنت اومد تلگرام.
برای تست فیلم سریع و خشن رو از تورنت میارم تل که ببینین تو کامنتا شمام تورنتاتونو بفرستین
❤️
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 692 · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSfAnvOiCg2Ry8M2EhS-y4_z7yWLU30EF5N25eTGJcV9gYptuumX0muxINgZe9YeyPJAbJImy1SxB-e30YG6bld8AtsNwS1iq0_8jh8xTUFL9HnKdWUv9jjTfyJTFI9KtW2BcSrf6-muiIKiZxipNbZEIL6u4WLIyKFNFKmLSNTqKJns7w6SMONwFGU2Z65VPWMmWZE5A38UGvwVrtboCanhAblpg7jzA3tuBaImAJVnBMdSDveg8ZkduovY88AkKduquPqT8eESSe2wrGdms8vHB-es1tTpPSYVqmZs7rJFrnARCwu5pKsnPPv9GLzJ61QsZZIcVp6zt_Qrehlrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دانلود هر فایل پولی، کاملاً رایگان!
🔥
اصلن به این فک کردین چنلا و سایتای ایرانی(فیلیمو، فارسروید، سافت ۹۸و ...) اینهمه فیلم خارجی و برنامه های کرک شده و کتاب و اینها رو از کجا پیدا میکنن؟
بعله منبع ۹۰ درصد این فایل ها چیزی هس که قراره بگم و کاملا رایگانه!
از جدیدترین فیلم‌های روی پرده با کیفیت اصلی و دوره‌های آموزشی چند صد دلاری کورسرا گرفته، تا برنامه‌های کرک‌شده ویندوز، اندروید و هر محتوای پریمیوم، نایاب و بدون سانسوری که فکرش رو بکنی
🔞
💎
( آره حتی اونام اینجا کاملش هس
🤣
🙈
)
اصلاً داستان از چه قراره؟
اینترنت یه شبکه بی‌نظیر داره به اسم
تورنت (Torrent)
. اینجا خبری از سرورهای مرکزی و محدودیت نیست! همه کاربران دنیا سیستم‌هاشون رو به هم وصل کردن. وقتی تو فایلی رو دانلود می‌کنی، در واقع داری تکه‌های اون رو از هزاران سیستم دیگه در سراسر جهان می‌گیری و همزمان بخش‌های دانلود شده رو به بقیه هم میدی. نتیجه؟ سرعت بالا، بدون قطعی و کاملاً آزاد و غیر قابل فیلتر شدن
🌎
🔗
🛠
قدم اول:
نصب کلاینت
برای وصل شدن به این شبکه، به یک برنامه نیاز داری که کار جمع کردن فایل‌ها رو برات انجام بده. کار باهاش به شدت سادس؛ لینک رو بهش میدی، خودش بقیه کارها رو میکنه.
📱
دانلود نسخه اندروید
💻
دانلود نسخه ویندوز
🌐
قدم دوم: لینکای دانلودش کجاس؟
لینکا اینجاس
🤣
آقا یکی میگف من با تورنت حال نمیکنم. میشه مستقیم تو تلگرام دانلودش کرد؟ بعله اینم تو پست بعدی میگم. نحوه انتقال فایل تورنت به تلگرام
😜
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7800">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🤖
JIJI AI
مدل‌های موجود:
⚡️
GPT-6-astra
⚡️
GPT-5.6-sol
🧠
Claude Fable 5
✨
gemini-3.8-flash
🚀
glm-5.3
🔥
deepseek-v4-pro
روش دریافت API :
1️⃣
وارد سایت بشید و با گوگل لاگین کنید
2️⃣
وارد بخش API بشید و کلید جدید بسازید
3️⃣
شناسه (ID) مدل‌ها داخل پنل سایت مشخص شده
Base URL :
برای GPT:
https://api-slb.jiji.cc/v1
برای سایر مدل‌ها:
https://www.jiji.cc
🔗
www.jiji.cc
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7800" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7799">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSKLzDbGZadirfB1m8jkUmRT_jeN8GyjBI0sqiJ2b1G8JHtv7n588rhbsrkJK4HPUuNuRsEAHbyj2ZfKHOvoMMjB5yMpe7rO3vy4C-Eec-WL5zoJSStH_APh81HK5vswxNMt45JwPHt_jJK10RcF-fyY2uvZi2dRMLFjHPlxZrjNWfwnw5mmFdOKFrJdCrMtn6drRn3qei9j-mYTWGWGne09HtASrSax32nbRrLI5QwbxYv2Z9j5UgzN1Tdc_rQNd2fpyeBWi3XHplLQUjFQoE85FcBdn-6TaZRzaU0O3mtTnaDCs29aprmxI_KXGWLuSmROdgR98JofDH1bklrQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNKHIp4MMqpfytigYsO6blb2dVkqUNOugNwyz4I8z4_EPMpSIiz53iQfuoSniHpXJ2zRRrxBQ9WKdcQay1DARqm1XX6U9-ritiKBSOnRp91vgVltHzwdDDTkB8m1yLLJ9dr5g3Wr4aQOMwJROOhHHHZBBZCkWzSqQzv6xZ1b2qjvz2xMLIW987vJjhfiMin91tmnaX4Ni8S_5u2dl44UNc_FyiC-6Cc5nivWIeVbOYJL79ezJRM2GP5Dn9POdbP2MoYMalGZZq3NDN_DbRoZxJdXBoyVRVt7yGdZJ741II1EpFzFNgD_df18ONB2CafSJ4RSAVCQb8F_eT-VlcyWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUhZXuu5sj74Tar1FT2ceq04H7UCnTM61KSN0T3F_AMFLTiATqjGX7eJJRYOAIQf8Yo44sQfZKTrqdUo_itXW7ZwfV6wZrVrxRXKO1duIICIrntYeu9yS0lfG_29gwi9g6BMcXCpNtHTcmRzl0DWBcCCOyuR6q8CJPiOLf1t4Xw4H2SDG8pgmJ5iN2ni3HxRMycaifcAV9ik94MZyO84Lxy9ByjXwGlgwk5Qxb4OgRTNG1enOT0Nbx7I0i4NMcOE4bMcyRSe8uY7Ix5uKQj1m-SgbADAN7LLJj439ooRaBfOMmyYvrEJB4WqLLQBp-bETegYfcU0fqMQ6Pd09C1-yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل GPT-6 ASTRA به صورت رایگان در MiniApps در دسترس است!
قدرتمندترین مدل شرکت OpenAI، بدون هیچ هزینه‌ای.
آنچه دریافت خواهید کرد:
✦ مدل GPT-6 Astra به صورت رایگان
✦ قابلیت‌های استدلال، کدنویسی و انجام وظایف پیچیده
✦ اجرا در مرورگر، بدون نیاز به نصب
نحوه شروع:
1. این
لینک
را باز کنید.
2. ثبت‌نام کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7796" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7795">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsWMU-LRSitytYCDmeKbvGBsSJ1djTetMmamWZaGCftixASQOEkcnG03YZTppsIIg0Sb06uacbJYpkJsulWrSVxNLL8fvCzNe3NwSOZ4fLoNmPMztBZfQVTNbDtQwpHoLGhIQf5GBJqR1nk_9KHrVcNVFfNzfuee02zqpOPzZQW5KF_IfqKtLFDUZZxD8oavbO3V1zQDJ4LXYjqULecdaXDj1rcl4hF4qKUDc6fro9rKRRkovrRBEs7YXWYDYHHhcdER63vNXcV8sqNeDxjSOmHH022Eg7M1gHrCodjL29Rha_VYfa10y1xgaC-hbTg3ExQ2o_pTu4NK0B5ds7_VSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
مقایسه‌ی تصویری GPT-6 Astra Max در برابر Claude Fable 5.1 Max در تست کدنویسی Code Arena
به طور خلاصه: Astra در انجام وظایف تحلیلی، محصولی و محتوایی عملکرد بهتری دارد. Fable 5.1 در جنبه‌های بصری و تعاملی عملکرد خوبی دارد.
در حال حاضر، GPT-6 Astra Max در مجموع، رتبه اول را دارد. می‌توانید جدول رتبه‌بندی کامل را از طریق
این لینک
مشاهده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7795" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7794">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_b00W4Ro7nIRbgld_cWkwA3qvZ8wL2yicP_X_wO4BS4VwWoU3fcCmWiW35hRlVuIhVEW_kAfNks7lujNBHEXAAcZ2Us37FnQJixFmiQN6wrxRBk-1qVBRa41UM_OEUiuhi2hnvGJt0MLyB88cySMKarGaQw6S-nPyqaECbz_hVV8w7Gq8kd7RrSNCS10vKzRPWIW7s3fFa_CkoxxRaW2_t2j9QPHPKbn7Xx0HTLlqIGOyXo9fEy5KMp_W5yZvbPdAWptG2SRQN0VdAHNxByuzfVjXhVBg9WajHbB3Ar5OScG-uhwGqcb4ml8bV0Uer_ZGmy-YLEvZsFeheD8ylQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
؛Qwen3.8-Flash رایگان تا 30 سپتامبر با 0.0× اعتبار
مراحل:
یک حساب کاربری شخصی در
Qoder
ایجاد کنید یا وارد حساب خود شوید.
یک محصول واجد شرایط از Qoder را باز کنید و Qwen3.8-Flash را به عنوان مدل انتخاب کنید. برای اطلاع از قوانین این طرح، به
صفحه رسمی تبلیغاتی
مراجعه کنید.
از Qwen3.8-Flash استفاده کنید. نرخ 0.0× به طور خودکار در طول این طرح اعمال می‌شود، بنابراین استفاده از آن هیچ اعتباری مصرف نمی‌کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7794" target="_blank">📅 15:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7793">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDkKq-DpFR1RmKMyFIdkT7J2kLTdO0XVeE5QtmQgY_mU4bqZ-jT6ItWRMrKr5zu5wNSi6diG2igew-ZKGgFokTujxEIKrg-pXgl4nmCVajSCB0krj0GX7fVvPfe_qjCxuLVmK0IeRt1cA95N5vBKpHPd5985DAN4MTVV6uo9zrI4nCyMho8fG_U9mkqmGuvc_tGo0FaiS2ZQ4Kv3xwYcmOU4DA6BDqxVuniy5lH9lsadz7sdWXiEsaTTgPDqv7ymi4631Di5QMD11tfsliFbuLLh0CcWc8iUgNTOZmG8vlf41oobdcsn_hcTp1FQ-uHkJ2BqMYf-sPOa2vH9shQtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
چت + تولید تصاویر و ویدیو با Kleo
🔥
آموزش
مدل‌ها:
➡️
GPT-6-Astra
➡️
GPT-Image-2.5
➡️
Kling 3.0 Pro
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/7793" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7792">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=P_gsD8kSoIce6NkRSiYAyuX-MobqS6xzupue5vGA2U12SUHNosZXFpBj9p_F01-7BiLn-mr3StLCINK6rZec-ro6ldGoHuipa7ZbOkFnPg2Kmu-I2HpvwZaKJdaLWlInwZ0WZPi2S0Fy6Piq3eCAKNDSTOwZzeB0YV42rIlkRjUBFALJSYZJBYt_xglUzD2icKvufzLmaxMd7jhRJaOFSZsan98JOm34_J-HAcv2LdWGW-zFa9XNGMYoGcxfg3wRwlMqNkc4VTq9PeSvUnO8NX9deqg2D9MTNwvoiRCHHA56xD43mtWoHmsb9IGNN9mODM9JHm9uLYgjhfUNTAwAQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=P_gsD8kSoIce6NkRSiYAyuX-MobqS6xzupue5vGA2U12SUHNosZXFpBj9p_F01-7BiLn-mr3StLCINK6rZec-ro6ldGoHuipa7ZbOkFnPg2Kmu-I2HpvwZaKJdaLWlInwZ0WZPi2S0Fy6Piq3eCAKNDSTOwZzeB0YV42rIlkRjUBFALJSYZJBYt_xglUzD2icKvufzLmaxMd7jhRJaOFSZsan98JOm34_J-HAcv2LdWGW-zFa9XNGMYoGcxfg3wRwlMqNkc4VTq9PeSvUnO8NX9deqg2D9MTNwvoiRCHHA56xD43mtWoHmsb9IGNN9mODM9JHm9uLYgjhfUNTAwAQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
مدل Kimi K3 به صورت رایگان در Cline Desktop در دسترس است!
🤔
شرکت Cline به تازگی مدل Kimi K3 را به خط تولید مدل‌های رایگان خود اضافه کرده است.
🤔
دسترسی رایگان برای مدت محدود.
🤔
از مدل Kimi K3 مستقیماً در داخل Cline Desktop استفاده کنید.
🤔
مناسب برای برنامه‌نویسی و گردش کار هوش مصنوعی.
✨
؛Cline Desktop همچنین از سایر مدل‌های رایگان نیز پشتیبانی می‌کند.
⌨️
برای شروع
اینجا
کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7792" target="_blank">📅 13:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7789">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/CFqw5kx1X5CLJBE4VWyYjwirI8CKtyuAaDMI0A1DWbTDfIbTIGRNiqt6Aq-1ArZnGST7MSn9TSNhvNbZ-lh--5igbBYEZp12mCFlP8VztyBy9HIxYQnX5LdXPCZ_Nts28cjFV8pK3Gjrtw3ToDzxi83XcDEDnRcydU9wGVx_w23upcZ5cT_ViP3cfUCoBexJgghlzSI6vG0qsJqSOyavWTFWXlLMN4QLJesCvz9SHw2Illb-YtuzMlMS5FfiQi1GrLezjvYNPHXkgH2029J_4l6Gv6UvCrg1vLXeEhHcCD0TwMXR3VxmJVwRGr3hf2NIajOjSXZ0cB4XVRigSzTM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNz5Kz2DtO4LeKyRUHkB1jsLsIJiDH_yF1EXW3oY6U5M9Uarp70VBU0CMRLhJjydjj3QaFk3tqjj0HHFq7fe7HpbPgKa_-rHtzy8tqiN9iRreM9xHmAUAaYVal6ncpy7l8S1aaffMHLDoodi6HyIY-s0gM7vW4-lPkZcHR40xI3vq-WSQFnD-B_RVB2hbGPSv6ModxqfRtFdH8pLicpktFb2kAwNk9eapvO51TSuUceIJrhpCtNGi1HNC3QO6wxqNhs9pIfvPy63UGyCfxefxO31AdoOj7rHPdqKfXuXc27D4fr3-I7i_u7G6uDgK3y1QrKwn9yvuHB9tcZgSdqbZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">seekAI
$2,000 credits
API key:
sk-Ok0xV7Zp4vfigk6qXL8M6hQSeVGa5cRhhfkZ06yre2RUIAfN
base url:
https://seekai.cc/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/7789" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7788">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/of2UganOX8zrbDC9fllFMH4d9rNvzljSgZTkWFYuYwFEEjJxJQW984mSemkYy57KzW0-Gu3T98TTwNqzV4G84o5BXQ5J9I4oNbQp9cLNR2-MDEKPde8kf04IT_XXAqXWh7Bn5OBwz3gw4LHCvA_Zw5-Y5wucziS0-CTi7WeDx723FSIacbpBdpUKHrXWwU_YLvML9ilsbRAjM9Go5lHRscGO1z-9S1aiF0Bn0O3OOj9vn6S2YKeQWF_pvqw0A1scekk4GF0CRNOqcq0b5AUZNLo6SEa5bB0nfU5T0DckJ3TygmFj_5EtokuZ6j4kbT2jmL6WZMPzyyVIPnWfhp-Hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Fable 5.1 به صورت رایگان در Freebuff CLI در حال حاضر در دسترس است.
👾
📢
؛Freebuff یک ابزار کدنویسی کاملاً رایگان است که در ترمینال شما اجرا می‌شود (مانند Claude Code / Cursor، اما با قیمت 0 دلار)
🆓
✍️
مدل‌های رایگان دیگر موجود:
🔍
🤔
GLM 5.3 Flash (پیش‌فرض، بدون محدودیت)
🤔
DeepSeek V4.1 Flash
🤔
MiMo 2.5
🤔
GPT-5.6 Luna
🤔
Solar Pro 4 (به مدت محدود)
🤔
Muse Spark 1.2
📌
نحوه شروع:
🤔
ترمینال خود را باز کنید.
🤔
؛Freebuff را نصب کنید:
npm i -g freebuff
🤔
به پوشه پروژه خود بروید:
cd your-project
🤔
دستور زیر را اجرا کنید:
freebuff
🤔
از لیست مدل‌ها، Claude Fable 5.1 را انتخاب کنید.
⚠️
نسخه آزمایشی محدود — فقط 500 جلسه در مجموع (1 جلسه برای هر کاربر)
🚀
از این فرصت استفاده کنید تا زمانی که باقی است!
⭐️
🔗
اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7788" target="_blank">📅 11:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7787">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگه موقع ورود به gemini یا سایر سایت های تحریم به ارور ۴۰۳ برخورد میکنید، میتونید از dns های زیر برای دور زدن تحریم استفاده کنید
👇
dns 1
111.88.96.50
dns2
111.88.96.51
dns1
45.155.204.190
dns2
37.230.192.51
dns1
83.220.169.155</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7787" target="_blank">📅 11:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7786">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♊️
جمینای گوگل سه شرکت واقعی را هک کرد !!!
جمینای در جریان تست امنیتی ماه مه ۲۰۲۶ به‌ صورت ناخواسته به اینترنت دسترسی پیدا می‌کند و شرکت خیالی مورد نظر خود را با شرکت‌های واقعی هم‌ نام اشتباه گرفته و با استفاده از اطلاعات ورود لو‌ رفته در سراسر اینترنت وارد سیستم‌ آن‌ها شده و نفوذ می‌کند،  پس از پی بردن به واقعی بودن شرکت‌ها، خود به خود عملیات نفوذ را متوقف می‌کند.
گوگل اعلام کرده هیچ آسیبی به این شرکت‌ها وارد نشده است
✅
منبع
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/7786" target="_blank">📅 09:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7785">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سلام بِرارون و خوارون عزیز
حال دلتون خووِه؟
🌟
فردا یه آموزش خفن داریم که حسابی به کارتون میاد!
🚀
مو فردا مِخام یَگ آموزش مَشتی راجب «تورنت» براتون بزارم که کِف کِنِن ینی قشنگ بِتُم مِگُم چطوری انواع و اقسام فایل‌هارِ، هم اوریجینال و هم مُفتِ مُجانی گیر بیارِن و حالِشِ ببرِن.
😎
🔥
بِراگَم، گیانِ دل! از بهترین کیفیت فیلم‌های خارجی بگیر تا همون فیلمای پرده‌ای که تازه لو رفته... اصلاً هرچی برنامه کرکی، موزیک، فیلم و کتاب نیاز داری رو یادت میدم چطوری سه‌سوته رو هوا بزنی!
🎬
🎵
📚
پس فردا حواستون به کانال باشه یاشاسین بچه‌های گل خودمون قشنگ هر فایلی که ایستیسَن رو بدون یه قرون پول دادن یادتون میدم دانلود کنین. منتظر باشین که قراره بدجوری بترکونیم، ساغ‌اولون!
💣</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7785" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7784">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
Ashna AI
قابلیت چت مستقیم و یا کلید API
🤖
مدل‌های موجود:
⚡️
gpt-6-astra
🧠
fable-5.1
✨
مدل‌های متنوع دیگه
روش فعال‌سازی:
1️⃣
وارد سایت بشید و ثبت‌نام کنید
2️⃣
اطلاعات حساب رو تکمیل کنید
3️⃣
از بخش Integrate وارد API Keys بشید
4️⃣
روی Create key بزنید
5️⃣
گزینه Dynamic model routing رو روی Off قرار بدید
( نیاز به تایید شماره نیست ولی اگر خواست از این
سایت
دریافت کنید )
base url :
https://api.ashna.ai/v1/api
🔗
app.ashna.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7784" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7782">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTgUh3qdteVsPAdnepkH4Tl6kdV3YcT1Ss6wpcPk2Dkk6NlxN43_wQJQdsYhYQ7PQ9HhwBYi_2CTQaWHXdVD9dSPU2JcbTBn7Aq1GiDwdDnbpcZTmWRRrZ3ObtiRIotMpQMgaMLFH9UmzLBXcnh_3TRTUorEyYiyQROLuSTvEfmCSunhDhW8-5H7s5ZQF2Ke9TWdvtKOQak-D2f7t-cWaGvI3e4nyZztWDTKskF2j9ffbx8d3nAIhOjWFZ53N_ybAc5hyFvi7vrvOiyh23y0CGOisf0rXR-8JdX1Z1JaiIZhXAoKSdVBCVH2gSEl56l-In-ZpajdbC8ni4L8MXz9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gemini 4 pro is out now
💪
😎
گوگل بالاخره پر قدرت به بازی برگشت
تست کنین نظرتونو تو کامنتا بگین
(این پست طنز میباشد)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7782" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7781">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJp4dbpnQdW-v7zWAgAhUeoaXEvHcb0rpjuU_SAOlLycPXo6GnIdbGN2r0GIZdVE3Wdt6Wm2-5IfbDmt9eWh5VljuXo-eBuT2aoK6CP27KfEMLfBDb_Zsiog_wPtLzT9ECXgdlK7GahU1tDaZiUF-0lDCQ_R24Va7Vn_36nA2aiRMekqq9wP3jE5sEO6oUfS_nccEmo0VNW3zaFI_kPs1IyiBuxqnwM4tLX-kLDCECj-bXlxfOdi9wtrJzmnh1KIiP-RlC3YnaI0tvhUhZxAebnYiS8cBgjrGOW27XxCPJz6xH-4_2VpW7EBLqFRXQ__nGERxZPFvkvalqcd-8s_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تبدیل ایجنت‌های هوش مصنوعی به کارشناس امنیت با ابزار Cloudflare!
بچه‌ها کلودفلر یه اسکیل امنیتی خفن
منتشر کرده که در واقع بیس اصلی سیستم کشف باگ و آسیب‌پذیری خودشونه و هوش مصنوعی رو به یه هکر کلاه‌سفید تبدیل می‌کنه.
✨
ویژگی‌های کلیدی:
🔺
ا
دیت ۶ مرحله‌ای:
ایجنت رو گام‌به‌گام از اسکن و تحلیل کد تا شناسایی عمیق آسیب‌پذیری‌ها جلو می‌بره.
🔺
گزارش‌دهی کامل:
در نهایت یه گزارش تحلیلی، تمیز و ساختاریافته از تمام باگ‌ها تحویلتون میده.
🔺
راه‌اندازی ساده:
کل ساختار در قالب یه پوشه از پرامپت‌ها و دستورالعمل‌هاست که راحت روی ایجنتتون سوار میشه.
💡
نکته/استفاده:
خوراک دولوپرها و تیم‌های DevSecOps که می‌خوان قبل از ریلیز، کدها رو با ایجنت‌های متنی ممیزی امنیتی کنن.
🔗
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7781" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7780">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">💎
دسترسی به مقالات و کتاب های
پولی خارجی به صورت کاملا غیر قانونی
https://libgen.im/
https://z-lib.id/
https://annas-archive.org/
https://sci-hub.se/
https://libgen.is/
دوتا اولی فوق العادن
😱
، علاوه بر مقاله، کتاب های پولی رو همشو داره. هر کتابی بخاین.
کاملا غیر قانونی
😂
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7780" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7779">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ارسالی
http://64.23.188.133/v1
gpt-6-astra          ←
⭐️
تأیید هویت شده
gpt-5.6-sol
gpt-5.6-terra        ← سریع (۵.۳s) و باکیفیت
gpt-5.6-luna
gpt-5.5
codex-auto-review
gpt-image-1.5
gpt-image-2
API key خالی
سریع بزنین تا تموم نشده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7779" target="_blank">📅 17:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7778">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgZHpVWfpH6S9bz2xkcVlX8cuUtb0DKqKLpYEhSBbbCF0jCRN4RVkRrTE5nqaYzZx9QtSoqfJVz99UtqnmPnkIAg70yIn_Y8Jwt6maNHRKw5DnUTAhtIJhBRC4oIEqbhxvGvQ-9Hzb-mrrqbYk8V1IQWG8lX_hCzXmGPNfmIX3u1HbAVIXJpviD4xhojL9u16GPdwCsCDV0PanOKTmGzfbI4BESaUHXIj41w2a6xYu0eZZuSr3GwG6yHzdvOj4WzyF1BEZsDJfJMeRWBzyktD8WyTFbCL_QOVM8F2Jxzqu_ZuQknBsFpiviWloDLxzVEAnzszr1Qdg-UkpJMUNjxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جنریت رایگان تصویر با مدل جدید GPT 2.5 SUNBURST!
بچه‌ها پلتفرم Weavy داره کردیت روزانه میده و می‌تونید جدیدترین مدل‌های تصویرساز مثل GPT 2.5 و حتی ابزارهای تاپی مثل Topaz و Magnific رو رایگان تست کنید.
✨
ویژگی‌های کلیدی:
🔺
کردیت رایگان روزانه:
فقط با اولین لاگین ۱۵۰ کردیت هدیه میده.
🔺
مصرف اقتصادی:
هر جنریت با GPT 2 فقط ۱ کردیت و با کیفیت بالای GPT 2.5 فقط ۳ کردیت کم می‌کنه.
🔺
محیط نود‌بیس:
دستتون برای تنظیمات دقیق پرامپت، رفرنس و تغییر کیفیت کاملاً بازه.
🔺
ابزارهای پیشرفته:
به ابزارهای محبوبی مثل Magnific و Topaz هم داخل محیط کار دسترسی دارید.
💡
نکته:
وارد سایت بشید، یک نود از مسیر image models -> edit image -> gpt 2.5 اضافه کنید، پرامپت یا عکس رفرنس رو بهش وصل کنید و ران بگیرید!
🔗
لینک ورود به پلتفرم
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7778" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7777">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lb1ovft0PfoU50q7JoVqBYIaxxaVebQTRbUJ6RcB-668l6aVcxrXI325BWlCa2Q8JudBHG2VXQKWPAockxSLQEGVTfrRvSIB4iDlmJmGkMqJ-XhQv4R5fVjPn2o7mSlDEuSJ6v05SJoVmYsoGtlxRM-pI0umZM3fzTS5KgBolcZr6KqEoKwJs9NZBeBrw_gjv4_3iT_cYy2g8qp13sfuQbUTuBQgX6_upAiEhOBKbmp31HAniwedEiMIdUYTneFmcH-CH0I4D-6NEJBK72bxVDLwcws3bcF4dipsQpGHBTFs7-fLtQP_rc1BNXSg1bXXT0cLP5KjUECWWT4mEUWdlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
یک میلیون توکن رایگان GLM 5.3 Flash
برای دریافت
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/ArchiveTell/7777" target="_blank">📅 17:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7776">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jPQ8b6K9k209tR8bpSJVCoN7ewT5Mrak8PjCNOiC4e4wqHfdQB66LBpGhOQ7if432WXTZfVV9a6MpfleUqPv-yPNlhFM7KZLrGYD4GRFyz5mEjVPUwwfPKapv0GR-Y_wXjXfSM-KXj7CEnUDnRClY8vEViNwYsmZQ-iH2WloJInFpoiKKtHc--uizUPWEQp-CSuyJyT7G_zMWpjWw1oktjmkRItcrIu-Ik7H9kQFxJdHX2Ej_wdrhNDD83ZsiJcMPRmzsrwSV0NhlaGmYaX9tIjBDtRifGr9si425oQb9ue-o423_Y2peCkzA_akRZ3zQs0iPU3Ryvh85m0VlVOEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
6 مدل هوش مصنوعی رایگان که همین حالا در Cavoti در دسترس هستند
👾
📣
دسترسی رایگان محدود (تا 25 سپتامبر)
🤔
Hy3
🤔
MiMo-V2.5
🤔
DeepSeek-V4-Flash-0731
🤔
Qwen3.8-Flash
🤔
GLM-5.3-Flash
🤔
MiniMax-M3
✍️
آنچه دریافت خواهید کرد:
🔍
🤔
استفاده کاملاً رایگان
🤔
؛API سازگار با OpenAI
🤔
مدل‌های قوی برای کدنویسی و کاربردهای عمومی
🤔
نیازی به کارت اعتباری نیست
📌
نحوه استفاده از این پیشنهاد:
🤔
به این
لینک
مراجعه کنید.
🤔
ثبت نام/ورود به حساب کاربری خود را انجام دهید
🤔
کلید API خود را ایجاد کنید
🔑
🤔
هر یک از مدل‌های رایگان فوق را انتخاب کنید
🚀
⚠️
دوره رایگان در تاریخ 25 سپتامبر به پایان می‌رسد.
⌛
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7776" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7775">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWMJORPWnWF6icn0Nlt7tpmgLO3emZqMLHPIuDD044EFroSiaNiO8ZCUKqYLnTalXiI7XnFwi6vnLiF-jyn6fqLsY6TFzzdCjUOFqLAx52IgyB2XbKkBhC4G18j0-83k7iSNRB5fNBp4f-i3uCTRxYI96AlwJc4yTU9Gi1ga_g1wEpcSyVioZK0P8pfkw0--z5YLufMFNZLfFtezBSadZO4CouDzW1VCm_ubdZ6Qt6CRqloioHyOrFYDk04wFKNn09935WHvKT8t_QiabVHoHr98KTkZmLYtGymbvvsQH-_TVWfnXOe-QN6iqiA5ELefURQ87N5vB5MhfhRqjQlOxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تبدیل خودکار هر مقاله به ویدیوی کامل یوتیوب!
بچه‌ها این اسکیل جدید کلود رسماً برگ‌ریزونه؛ با
Anything2Explainer
کافیه یک متن، مقاله یا موضوع بهش بدید تا تحویلتون یک فایل آماده MP4 با موشن و صدا بده.
✨
ویژگی‌های کلیدی:
🔺
فول اتوماتیک:
سناریو می‌نویسه، استوری‌بورد می‌کشه، انیمیشن می‌سازه و زیرنویس اضافه می‌کنه.
🔺
صداگذاری اختصاصی:
روی ویدیو با هوش مصنوعی نریشن و وویس باکیفیت میندازه.
🔺
کاملاً رایگان و متن‌باز:
با یک خط کامند راه می‌افته و خروجی تمیز بدون واترمارک میده.
💡
نکته/استفاده:
آماده‌سازی کل ویدیو با تمام جزییات حدود ۱ ساعت زمان می‌بره و همه پروسه صفر تا صد توسط AI هندل میشه.
🔗
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7775" target="_blank">📅 13:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7774">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6370f25b3.mp4?token=F56otGWf5Ds47MtOax38UcWRD5XamNdBK4fVYhNLHjOt_xFyCLrS29wAKy7IhjzxipdCzHBvTfUKTDh6CvbN0AY-tWeQakiih2jaEBs0c-GxAylPunmQp7aS_v8NCpD7Ivvi219gxfB4FGXza9uxkyc-C1_mnF3OiQv_ZfOgmcENAE8TuhzTgkVWRWF0oObpYKvqLJ6P7kY2yX-YzrMy0AbGDmrI94VydkiQppBj-p_7n0-LiD_PuvbTLSapYVdhSwZW_rFyd70gYnZmlf3hKWtxiv95uwYxOFZTCdWO6Vl6e8zCSuEjEoxLiLUgfzn1YHW-4svQWPUow-i57CmRwKFauMMfAOopcJua4ghZqrsxdtxk4aHOw33E_QQSxdO0_FepnUKpcfdJ0NvXWulQr89s8Fkp9pkXVthF-z-L63I_N7RiN4MANY6VukXHDGMBi-8iGMrrje0IdSRB7qN3tmb7hJXpvYLXtaAo8vIc8UNpy48VuPmBNHDsV2eeA5ZgneOD58YjhTNHmBOBoMdiS1VA_Vs-HqM0orJtMhbVqmmsjt4I4ohNI_eSFkSjltHtCaZ4o8mbMkHEQarpHDAgFkr5MN0H6OvznGOcuwKVELhFUixZjHDy8j6LUSwHyYJfXAwrEvJCi5fXKFsV5tQsZRi4PKL_m-qDD76KVX299-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6370f25b3.mp4?token=F56otGWf5Ds47MtOax38UcWRD5XamNdBK4fVYhNLHjOt_xFyCLrS29wAKy7IhjzxipdCzHBvTfUKTDh6CvbN0AY-tWeQakiih2jaEBs0c-GxAylPunmQp7aS_v8NCpD7Ivvi219gxfB4FGXza9uxkyc-C1_mnF3OiQv_ZfOgmcENAE8TuhzTgkVWRWF0oObpYKvqLJ6P7kY2yX-YzrMy0AbGDmrI94VydkiQppBj-p_7n0-LiD_PuvbTLSapYVdhSwZW_rFyd70gYnZmlf3hKWtxiv95uwYxOFZTCdWO6Vl6e8zCSuEjEoxLiLUgfzn1YHW-4svQWPUow-i57CmRwKFauMMfAOopcJua4ghZqrsxdtxk4aHOw33E_QQSxdO0_FepnUKpcfdJ0NvXWulQr89s8Fkp9pkXVthF-z-L63I_N7RiN4MANY6VukXHDGMBi-8iGMrrje0IdSRB7qN3tmb7hJXpvYLXtaAo8vIc8UNpy48VuPmBNHDsV2eeA5ZgneOD58YjhTNHmBOBoMdiS1VA_Vs-HqM0orJtMhbVqmmsjt4I4ohNI_eSFkSjltHtCaZ4o8mbMkHEQarpHDAgFkr5MN0H6OvznGOcuwKVELhFUixZjHDy8j6LUSwHyYJfXAwrEvJCi5fXKFsV5tQsZRi4PKL_m-qDD76KVX299-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
با این مدل، هر عکسی رو با یک کلیک تا 4K آپ‌اسکیل کن!
بچه‌ها اگه عکس تار یا بی‌کیفیت دارین که می‌خواین زنده‌ش کنین، مدل خفن
Crystal Upscaler
دقیقاً همون چیزیه که دنبالش بودین.
✨
ویژگی‌های کلیدی:
🔺
خداحافظی با ماتی:
عکس رو مات و غیرطبیعی نمی‌کنه و جزئیات واقعی رو حفظ می‌کنه.
🔺
کیفیت تا 4K:
رزولوشن رو تا بالاترین حد ممکن بالا می‌کشه.
🔺
عملکرد جادویی:
خروجیش رسماً شبیه زوم‌های فوق‌العاده توی فیلم‌های علمی‌تخیلیه!
💡
نکته/استفاده:
نیازی به سیستم قوی نداری؛ می‌تونی مستقیماً روی بستر وب و از طریق FalAI آنلاین تستش کنی.
🔗
لینک تست و استفاده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7774" target="_blank">📅 11:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7769">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1mW9kG7YwkxLqutaIUuI2E8yo9qnPqtA97dRv1Bbb06gBJy_ZgxOMlS7CzzceidkjMi2TzREsp_L9u6AxaVaFMe9TyuA53OUEfZWG5ygmZwzYzC42eCpSNb2ej8ddVQnPcMD5jb2OqpBS2jWdNwfger8E1Es4NRrmqKQK8lwVwFDuJ2cDOX6zRxHm_q7inDftQHmvWPniGYP8WFNznWF50gkwHdp0uXtHcQq0TZpYSRz7JXEO3JA0f9sll7HKS1L7uLaxywLlfSGv8z62aAh8QtDdkMWNlm570WpYtElPMCwOZpYA2UwnXTILLMptjzPB17mQj558W-PpRhf_TPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTr4lQZhJ_ffmwRAsi7ifU4x9Ssmh8VhQ0jL5PZ8QBdxPvyCXDJkfO3KabkHqEshGywwSf1jV7NisBRs7HwQsS4dtnad4JrsW91apMAQAebgI6bOGDy0WzJoW2T1fcB-FVwwNMh4AKnja4Gst5p3D-enY0ba2nuxW9jLJjXFruaCi4jkT7B4WnFKTOvkpnPPEr6a_lVasX70FqiZnZ77C44oNiKZ0JBbn9xfPOV8jRjmatoEnib7TUzkjVyaQPgz9MbQrbuUqMi00NeSzRpdwVtZhjAIUc9OnSAiHtonlBN8JnCfVwrDVEif6VXnfbS91rzJJ2Bhbb3rwAkCAjvjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1fGxw7tM1liz7yDijkqNV72JCHnn7P5XZB-vkPPpSVhIdVXTd46SJUKTErSwT-eUF3HtPPzZNfnqbSwE50BA5pR0pIwktV0MmdfR6e9YB3v9ZXxS3XtYMaqfT4mqtSLK4KGIojDdab2TkTPFuaF2P0WYE_ddIbOgp6ffFYFhTBjL5KKRCC-xhiutm-j-ovbouyn9o_Cy6GD-cXoLJF0HKEF2TwuFllv38Gaqc-lhlaL2hD4BrQCfTJOyZJFDboT27_NpKlR7D0K1sI64RTvYM37YmrbbcA6QnUoPd5vywYxzI1ZzZrSuVpOEt9rBruLd7iXoSjV6QZobF0zCMMR_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=RkscjhMx7rXTEKMvnEbDw_Y5oygJkKijg4fDOvVJM9clMjaCTEFOmmLk2-dBhG6kNqCZP28so47U7ohpflQyT2zcs0ysUoCa8dXjMt4UI5ARr6Z-q-tjBFipE83jsTKHXwfBrAZv-dHV84JnBwUdUn-PWPZLw8odxEzoVM37tlGfI3sCMB282PwPl-91Qlh3belCAyn_TryuQtrwoLH8ShZs6WbqmSzXFcEi99i5n57t5P3lbRgf-CQRZ5exoGWuyYY02mN_qtex1nF43F7552Wmu-AzxmezE-bzhz9qpfUE5Jd5IS6DWGCApitpWU2OohSI7tvMkQVTrDp0UmyhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=RkscjhMx7rXTEKMvnEbDw_Y5oygJkKijg4fDOvVJM9clMjaCTEFOmmLk2-dBhG6kNqCZP28so47U7ohpflQyT2zcs0ysUoCa8dXjMt4UI5ARr6Z-q-tjBFipE83jsTKHXwfBrAZv-dHV84JnBwUdUn-PWPZLw8odxEzoVM37tlGfI3sCMB282PwPl-91Qlh3belCAyn_TryuQtrwoLH8ShZs6WbqmSzXFcEi99i5n57t5P3lbRgf-CQRZ5exoGWuyYY02mN_qtex1nF43F7552Wmu-AzxmezE-bzhz9qpfUE5Jd5IS6DWGCApitpWU2OohSI7tvMkQVTrDp0UmyhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
Arrow 2؛ قدرتمندترین مولد تصاویر وکتور!
🎨
‏مدل
Arrow 2
اومده که کار طراحان و تصویرسازها رو خیلی راحت می‌کنه و ساخت وکتور رو به شدت سرعت میده.
‏
🤔
کاربرد متنوع:
ساخت انواع آیکون، لوگو و اتودهای گرافیکی با دقت بالا
🎯
‏
🤔
خروجی حرفه‌ای:
تبدیل پرامپت‌ها به طرح‌های برداری تمیز و قابل ویرایش
📐
‏
🤔
تست رایگان:
دسترسی به دو هفته
trial
برای شروع کار با ابزار
⏳
‏این ابزار خوراک بچه‌های طراح و گیک‌های گرافیکه
🔗
لینک دسترسی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7769" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏Union Alpha امروز روی OpenRouter و OpenCode در دسترس قرار گرفت
✨
‏چیزایی که داره:  ‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)  ‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7768" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7767">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyREGspPQnLQRoP_zKS8IgAtT57WGvSUtTGbysGfV6LOShnglzSF_Adoq9d4Q91BcrhMquspv8Xro7NNp_5VH307KNkRX4InGkHNzcJLqX05q-Hmi27zf6k4GG2ccpH0FP4MtIeduxnUB6xB5jVa-iFAq3oHAoEJMupYvKvoV8Drzv3K0bPngbcdLm2hoGOEgpn4RFMlYZl_F1knm3t7LWbT8yCaK4gV2E3r-4d9QN-QbTTXkzXbpczQVXa0_fGi96Dvwi6UqnasCiip5OeAIreQrP4Pk7XJobUBWMaI9cgg0vuE3Ian7QA2cnC3uUVzs6nfe-aOwf0zRx19TuoKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏
Union Alpha
امروز روی
OpenRouter
و
OpenCode
در دسترس قرار گرفت
✨
‏
چیزایی که داره:
‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)
‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام هم می‌فهمه)
‏
✅
Tool calling و structured output
‏
✅
بهینه‌شده برای کارهای agentic و کدنویسی خودکار
‏
✅
داده‌هات برای آموزش مدل استفاده نمی‌شه
‏فعلاً کاملاً رایگانه
🆓
‏
🔗
لینک مستقیم:
‏
https://openrouter.ai/stealth/union-alpha
نظراتتون رو بگید
👇
🔹
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7767" target="_blank">📅 21:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7766">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">😎
یک میلیارد توکن Muse 1.3 به صورت رایگان
به کاربران جدید، تا یک میلیارد توکن در Muse 1.3 ارائه می‌شود.
(این توکن‌ها از طریق API ارائه نمی‌شوند، بلکه از طریق وب‌سایت توزیع می‌شوند.)
اینجا
ثبت‌نام کنید (از VPN آمریکا استفاده کنید)
بعد از ثبت‌نام، در تنظیمات، کد تخفیف زیر را وارد کنید:
LYA0IL
+ در opencode، این مدل به صورت رایگان ارائه می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7766" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7765">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚀
بدون یک خط کدنویسی، برنامه‌نویس شو
😱
(جادوی Vibe Coding)
دیگه لازم نیست ماه‌ها وقت بذارید کدنویسی یاد بگیرید.
الان فقط کافیه با زبون آدمیزاد (فارسی یا انگلیسی) به هوش مصنوعی دستور بدید تا براتون برنامه بسازه! به این کار میگن
Vibe Coding
(برنامه‌نویسایی که میگن الکیه کیفیت خوبی نمیده، حتی اونام از این استفاده میکنن
😂
)
برای اینکه مثل یک حرفه‌ای خفن‌ترین پروژه‌ها رو بالا بیارید، این ۴ قدم رو پیش برید (پست رو سیو کنید که به کارتون میاد):
۱. اول نقشه بکش (Deep Research)
همون اول نگید "فلان اپلیکیشن رو بساز". اول بهش بگید:
💬
"ایده‌م فلان چیزه. بهترین روش پیاده‌سازیش چیه؟ چالش‌هاش چیه؟ برام یه دیپ‌ریسرچ (Deep Research) انجام بده."
۲. گیرِ تله‌ی پایتون نیفت!
🪤
هوش مصنوعی عاشق پایتونه، ولی همیشه بهترین و بهینه‌ترین گزینه نیست! بهش بگید:
💬
"سبک‌ترین و بهترین زبان برای این پروژه چیه که اجرای اون دردسر نداشته باشه؟"
(مثلاً خیلی وقتا یه فایل HTML ساده که تو مرورگر باز میشه، کارتون رو راه میندازه).
۳. لقمه‌لقمه پیش برو (توسعه ماژولار)
🧩
بهش نگید "یه فروشگاه برام بساز" چون قاطی می‌کنه! تیکه‌تیکه پیش برید:
۱.
"اول ظاهر صفحه رو بساز."
۲.
"حالا کاری کن دکمه‌ها کار کنن."
۳.
"حالا اطلاعات رو ذخیره کن."
۴. ارور دادی؟ فدای سرت!
🐛
کد رو زدی و ارور داد؟ اصلا نترس! تو وایب کدینگ، ارورها بهترین دوست شما هستن. متن ارور رو کپی کن و بهش بگو:
💬
"این ارور رو داد، مشکل کجاست؟"
خودش باگ رو پیدا و حل می‌کنه.
🔥
با چی این کارا رو بکنیم؟
با همین مدل های زبانی هم میشه انجام داد ولی ایجنت های حرفه ای مثل Claude code و Google Antigravity هم میشه استفاده کرد.
👇
تا حالا با هوش مصنوعی چیزی ساختی؟ تو کامنت‌ها
معرفی کن رایگان تو چنل بزاریم
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7765" target="_blank">📅 18:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7764">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پروژه bkup یک پروژه اوپن‌سورس برای اینه که فرایند بکاپ‌گیری و بازیابی پنل‌ها، ساده، متمرکز و قابل مدیریت باشه.
🎉
نسخه 1.2.0 منتشر شد.
⚙️
تغییرات این نسخه:
اضافه شدن
Restore
برای بازیابی مستقیم بکاپ روی سرور از طریق
SSH
پشتیبانی از
3x-ui، HM Panel، PasarGuard, Rebecca
برای Restore
پشتیبانی از بکاپ‌های حجیم و چندبخشی
➕
امکانات کلی bkup:
بکاپ‌گیری زمان‌بندی‌شده، ارسال مستقیم بکاپ‌ها به
Telegram
، پشتیبانی از بکاپ‌های حجیم و چندبخشی، مدیریت بکاپ‌ها، تاریخچه و لاگ‌ها،
Reassemble
فایل‌های چندبخشی و
Restore مستقیم بکاپ روی سرور از طریق SSH
.
همچنین امکان نصب خودکار پنل در زمان Restore، خروجی گرفتن از تنظیمات و انتقال آن‌ها به سرور دیگر و اجرای پنل به‌صورت
PWA
هم اضافه شد.
⭐️
اگر bkup براتون مفید بوده حتی یک STAR
روی GitHub می‌تونه بزرگ‌ترین حمایت برای ادامه  توسعه پروژه باشه.
🔗
github.com/AliRezaC-xrol/bkup
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7764" target="_blank">📅 16:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7763">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGApA0cJyerPjSod7x3llmOn3RMIlj6WriKEf73vBVXys-f0QUE_EUK9NOBld6cyDLCTDp3ml6gXCa5admYMYrFJzElxVzbcULsbWwCxjBst2det7y0EMoFAnqJtMYtTUsaLfMmN5Io112-mQKT38WZM_i6Vi8_rjXM_NAwCJp9K4puaXuyZFV2ITi2UBDGpbYHjaI27iT7uertqgjt9PrPWPx84k2mhDDJd7OXRW-dQDsJoUEt_EQ_zJZTWs5-lA5Ffg695gdxBJpo58Kdc25VxSIwId_h9JUtOEEqwY7uOMDo94LEXULRPmW3Lq9Fxn2xN6J3tY0gPC7wpzFfSDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل جدید دیگری از شرکت‌های چینی با نام ATRIA عرضه شده است. آن‌ها 100 میلیون توکن را به صورت رایگان برای هر حساب کاربری ارائه می‌دهند.
اینجا
می‌توانید با استفاده از حساب کاربری Gmail خود ثبت‌نام کنید، یک کلید API ایجاد کنید و از آن در صورت نیاز استفاده کنید.
نتایج تست‌های عملکرد در تصویر نشان داده شده است.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7763" target="_blank">📅 14:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7762">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⌨️
آدرس‌های ایمیل رایگان برای استفاده‌های مختلف در سال 2026: یک فهرست کامل - بیش از 60 سرویس
▫️
تکنیک "نقطه" در Gmail - اساس همه چیز
username+anything@gmail.com
→ همه ایمیل‌ها در یک صندوق اصلی. استفاده از IMAP از طریق App Password. هزاران نام کاربری فرعی. محدودیت: سیستم ضد تقلب گوگل - حداکثر 20-30 ثبت نام در ساعت، تغییر IP. سرویس‌های Oracle/Webshare، نام‌های کاربری فرعی را در مرحله اعتبارسنجی مسدود می‌کنند.
؛ SmailPro - آدرس‌های
واقعی
جیمیل ایجاد می‌کند، با بیش از 5000 آدرس در دسترس. تحویل در کمتر از 10 ثانیه. از تست‌های تشخیص ایمیل‌های یک‌بارمصرف عبور می‌کند، زیرا یک جیمیل واقعی است.
▫️
تقریباً همه جا کار می‌کند
؛ SimpleLogin —
نام‌های کاربری فرعی نامحدود
(در اکوسیستم Proton)، فوروارد و پاسخ با استفاده از نام کاربری فرعی. متن باز. نسخه رایگان: 10 نام کاربری فرعی
؛
addy.io
— قبلاً AnonAddy،
رایگان‌ترین سرویس
: نام‌های کاربری فرعی استاندارد نامحدود، متن باز، امکان میزبانی شخصی
؛ Cloudflare Email Routing
*
@your
domain.com
→ فوروارد به هر جایی. رایگان، بدون نیاز به سرور. ایده‌آل با دامنه .pp.ua
؛ ImprovMX — فوروارد رایگان برای دامنه شما، 25 نام کاربری فرعی
؛
33mail.com
— نام‌های کاربری فرعی + پاسخ‌های ناشناس
؛
spamgourmet.com
— نام‌های کاربری فرعی خود تخریبی
؛
erine.email
— فورواردینگ خصوصی
▫️
ارائه‌دهندگان ایمیل IMAP (غیر موقت، در همه جا کار می‌کنند)
-
mail.ru
-
rambler.ru
-
yandex.ru
-
aol.com
-
gmx.com
▫️
ایمیل‌های موقت با API (قابل اسکریپت‌نویسی)
-
mail.tm
-
1secmail.com
-
guerrillamail.com
-
temp-mail.org
-
mail7.io
-
anonaddy.com
▫️
ایمیل‌های موقت بدون API (وب)
yopmail.com
·
temp-mail.io
·
dropmail.me
·
emailfake.com
·
emailnator.com
·
mohmal.com
·
tempail.com
·
getnada.com
·
inboxkitten.com
·
mailinator.com
·
burnermail.io
·
fakemail.net
·
tempmail.plus
·
mail.td
·
mailpoof.com
·
trash-mail.com
·
temp-mails.com
·
emaildrop.io
·
temporarymail.com
·
generator.email
·
mailsac.com
·
tempr.email
·
atomicmail.io
·
emailondeck.com
·
crazymailing.com
·
tempmail100.com
·
tempmail.ninja
·
boomlify.com
·
tempmail.dev
·
internxt.com
·
adguard.com/temp-mail
·
webmail.raoshahzaib.site
▫️
بات‌های تلگرام برای ایمیل‌های موقت
@e2tgPM_bot
·
@mailtemprobot
·
@hidemail_bot
·
@TapMailBBot
·
@botmail_io_bot
·
@temp_mail_bot
·
@fakemailbot
·
@etlgr_bot
·
@DropmailBot
·
@tmpmailbot
·
@TempMail_org_bot
·
@TempMailer_bot
·
@smtpbot
·
@SenthyBot
·
@TempMailBot
@telegaemail_bot
·
@hs_temp_mail_bot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7762" target="_blank">📅 14:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7761">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">😎
دسترسی رایگان به FABLE 5، OPUS 5 و GPT-6 ASTRA
مبلغی معادل 1 دلار به عنوان سرمایه اولیه ارائه می‌دهد، اما با توجه به ضرایب، این مبلغ به موارد زیر تبدیل می‌شود:
🤔
Fable 5 → تقریباً 7 دلار
🤔
GPT-6 Astra → تقریباً 18 دلار
🤔
Opus 5 → تقریباً 20 دلار
استفاده از چند حساب کاربری (Multi-accounting) امکان‌پذیر است.
————————————
📝
نحوه کار:
1. به
وب‌سایت
مراجعه کنید و از طریق حساب Google خود وارد شوید.
2. یک کلید API ایجاد کنید.
3. آدرس پایه (Base URL):
https://www.rsiai.net/v1
4. برای مشاهده مدل‌ها، به وب‌سایت مراجعه کنید.
————————————
💻
نحوه اتصال:
Claude Desktop (Code):
- Help → Troubleshooting → Enable Developer Mode
- Developer → Configure third-party interface
- مقادیر زیر را وارد کنید: baseURL، api-key، model-id
————————————
♾️
دسترسی نامحدود:
1. یک پروفایل جدید در یک مرورگر ضد تشخیص (anti-detect browser) ایجاد کنید و موقعیت مکانی خود را تغییر دهید.
2. یک حساب کاربری جدید ایجاد و کلید را دریافت کنید.
3. کلید API را در کلاینت خود جایگزین کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/7761" target="_blank">📅 14:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7759">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/k0RZPPxB9-DkxdvB-sNcLtea2IsiheIiizpgNNgoHOqXanXsxkzqVNnuMQ3JCsPWdXuUxPiW3Cy14mY0K4MWjVvfx44FuxRjQuL_dHa2cW2JpCpyC8_B3cgYynCvpqc1V4ZaiiZ9R45HbnHoPMEih0rtEPFWBW40pby-r1h8iqNNmzgsBZ4UZuDlhYyhMXhGuGaTL5rMOpT4Qsh6oeTzlCRmW6XgJpw9YLVyk_dlQcHkeILqsjQ6O8TytjtwmgPWsJS8CLJKl1tBfNHvAxj_o8OSt4SITS2wD-LvMQpxxbHehj5bHkA99arHDLnWU5EJ03v4UsIdX1rp7mNQgp3oRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/kNnMqXV9T1A2S5F-kPxG1m8E9CE46gtEAT7sO0ovmZxcrAnO4Ut0vZeBbdixwR4UTKQBPac489KztrEQwasDd8P5uYkrU6iz9cpnaXchqveevLSXK8_FqBl88fMJTfCQ9jYJrOvzo2mmzwjNAoUt1Fi3I_II4LGQ1q5Hdgj1w5w1wPkx6LQu0-1GdP-czZLFfjG3Xut4Ndx2ookngl4XUU3mb2mX-5xEGqGUW-vhzevBGUFCOhnNClSEbIGzoOgHixNQ130AWhFwoDPotQns_NuMsP7TEDw7GmFKzL2MJu7rNlX5Sx_LLh2Ih2d-FhaBVwVlkyhwk751k7k6qK0ltA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔥
کلونر اتوماتیک و خفن تلگرام روی کلودفلر!
‏بچه‌ها، این ابزار Serverless روی ‌Cloudflare Workers⁩ بالا میاد و خوراکِ کپی کردن و همگام‌سازی کانال‌هاست؛ بدون نیاز به سرور و کاملاً رایگان.
‏
امکانات اصلی:
‏•
🚀
دیپلوی تک‌کلیکی:
بدون دردسر و سریع روی زیرساخت کلودفلر بالا میاد.
‏•
⚙️
فیلترهای پیشرفته:
می‌تونید فایل‌ها رو بر اساس نوع (ویدیو، عکس، سند) یا سایز دلخواه فیلتر کنید.
‏•
🤖
چند بات همزمان:
هر تعداد بات که خواستید اضافه کنید و تسک‌ها رو بدون محدودیت مدیریت کنید.
‏•
⏱️
همگام‌سازی لحظه‌ای:
هم بکلایت تاریخچه رو انجام میده و هم پست‌های جدید رو هر دقیقه سینک می‌کنه.
‏می‌تونید سورس کاملشو از گیت‌هاب (‌
iamLiquidX/telegram-clone-worker⁩
) بگیرید و با یه استار حمایتش کنید.
⭐
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7759" target="_blank">📅 12:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7753">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/DIV2jo8c24Ljvs_akcjcomLwSenq8ckaaB4UEmQW3ubWzd81SlhPvm9oNHuRbTjgb_zeVEe7WsW6bkm4FWvbm_laRK99d4mNwPmyw3HIM1lcD0ju_jIkvVeaN5Ug8smk8WPf3jG40p6YCn68Ru2cO8ii7BLRVfFJdQSQ609HTTonNOomo7deRNOCJvUgVAZxCbg00qziT4VJJM_71gZU5GlNhdT5kiGDK3wNi23g4ifdGqv0W7bCkc2aD7EuLiMMTwb3Dl4vShHrEzgHpH6bT974uAsaQcWadIdVgVXFPEWgCMRzp5auLPM3jSPcQAvQ3QaS-0X5DJhZnc1ax3xpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/XwVgd-SGGDunYK9moCQ8kT2ZsMEXXqsnLE6oXZVg0Y_4zytrQqyVM9Ad3kfGuzXE0xo9ECasrUhU9BGMm9mgcJwNmMlyjOqFSNXDWpbsAp18m6ZB6qK2-PKnOROL0b8OqSIQxvT740zXCUHY-0P0zIcRunsYM7KwmDbrsoHgxX8XidtkfLPql5AlQ4OW_DZddYz9Knr2xwqsru5x8UY2eVv4pCZHXr8QLR4-fzl_HLIstj6Pv7JHVQie1M1YjJ4TWGW0hfHA-bA0ldgVusqG2ibzggVdMiUL_k-PnY06Ifweri4IpwXmpuHYXILtamdjbipE0yPPrFdVk_FEd6J5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/sVURyNlHuPslYSq2CN1T7A7MR-BXRCIl8pMVXm9YfqQ8ubinqeYMx9RPlPoRT7t3Bfb5upeXm3SOpUpaiG7GKgFcjCFNNUcylDQBOU1kPFOvNSdDGcASQuIOV1Mz1Xpl1O4_7zUkoMeWScwn_BDZ66ueg_Em5pTarJan7DdBOsICgsScZEQF_7l89ionKgvAciNI_TBF8Uc__pLKNNRGJ0A3G139KG8PR3O25GreDCVp10T0mKetwj9fj48ziYzgBcEWzquSFZn6ucRSb6cbsvSJ2-7TsT1iAza9V7jsBqL-vPkONCHmdQEnsEaysjuS8GrPKPur_8DqpKS2OAY_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/hLfEAkHzqD9lwT08IPaC68VD0fumEVTbX4Y0rFgIO45txEc2jzfAvI6bDUDOO8UMpXF_rI48TVpJPBVRBDIYuh7xsShVJ0VZeVMwaqtR6yB9VKqNObCNEj9ZSAL4lkiQbBddf_0I_GhwFgD_L5obUDtXNZfQRvsDH48-SGRvg0MzopP-sObHRt1HJCoBOCq4u4CK1VVyzK0eTuJZlzgB1uKWYaNcuYrqCE5rgEXZQLfpZb_HNhkZM7apE3L5STguZFbixi0GNN8jZFbIKXxaTCfZDViwWCdinuTdc2V1bUFyDOH0YGsLd2bgXRp9VhYXqbRk2_3k_75kPb_YRO1GnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/vAVUPfdkZ9sWeq6_euKTs4BQVEWNqAWTambUn4CZxrjJkBU42W0ViMJZzzNPgEfr03Q805eIPSSroLiBhE6n8QvfakaZIWC4Hu3g_Plkiu8zFNNDMEl2qC1YXMaeOVJUHgqVrLyh0FzTH3pib78-l2_BPosf0_7_BcUwQLavw49ZB4lBxN9V7RFuvLGvK8hCZ21p_kWhirQnnKBkPjJn43Gy5YwrsWc-gfLx2W8VCkS03vEGhhsFFGNK26FnuOqFPVyESHJ5_12QhfJDHvWT_koAOew7kO3t5NUlJku3FsLjTMuPv7sLFzMPLlzBFsXlPI7hCY00TysaHdTvSlwvYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Oqw80sK0AYMJg-zPJQCtvhTU5B4JhIwpkmso5aJxeIkfBLVVQNYBDHDjjFkbx6S3aJjk3VRXm_AXTAslkjHsLnFSwb_9FdnyR6wisO8Gu4d6pjpQpSxZ3hjfV2WtODHVLC9bVEp8vqMKNP7ydUKM13EFyUL0cJ2FB6dHR2K4CRuaqZRbCXLE-yjPD5mrusXxEcA126pZiZV3nSzYFivb7h_1Qpy2X8ObpfoyfuAw-VbUse_7HEr9SczrQWRbirjXRS2E8QLufyuxA1uTCPxOobViuPX-B_ugoH7oed6db4FeF8zPoWbGtpBeAHs_eE5qXlBPgSGyncUlwX-Dg-mvTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.
یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار بیشتری به دست آورید. نیازی به کارت اعتباری نیست.
1min.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7753" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7752">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⌨️
؛ DeepSeek V4.1 Flash، Muse Spark 1.3 و GLM-5.3 Flash به صورت رایگان در Cline Desktop
​تیم Cline یک برنامه دسکتاپ جداگانه با تمام قابلیت‌های یک عامل مستقل را راه‌اندازی کرده است.
​
📌
امکانات برنامه:
🤔
استفاده از ClinePass یا کلیدهای API شخصی
🤔
انتقال یکپارچه وظایف از Codex، Claude Code و سایر عوامل
🤔
برنامه‌ریز برای اجرای پس‌زمینه عامل
🤔
مدیریت سرورهای MCP، پلاگین‌ها و مهارت‌ها
🤔
مرورگر وب داخلی و ورودی صوتی
​
📌
مدل‌های رایگان موجود:
🤔
DeepSeek V4.1 Flash
🤔
Muse Spark 1.3
🤔
GLM-5.3 Flash
​
📌
نحوه شروع کار:
1⃣
دانلود برنامه:
https://cline.bot/desktop
2⃣
نصب و اجرای Cline Desktop
3⃣
ورود از طریق حساب Cline یا اتصال کلید API خود
4⃣
باز کردن پوشه کاری پروژه
5⃣
انتخاب یکی از مدل‌های رایگان از لیست
6⃣
ایجاد یک جلسه و اختصاص وظیفه به عامل
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7752" target="_blank">📅 01:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7751">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaIauEwEvBd4HDVizJvkJB2F3zzLcXHcKGZtuNITlGaMD_IGYV-PBRlBGDulQTVb5LVsGPbLxLUENJIesJiSbA9m8nj6BeRLFFdi8CjMoZcxv7JtOUvSsjy3MBpsx2wpkz5k_aZt3fWAkL3nDjr5KAjK7N6q-Rj8AF9djp4uHHSdGqDjsNKsseO535OcEC8O93Ke4Q0bGCKF-s5RsaxrBFFY5JGLAikilulC26fDGOLhtNu9MGhPz4tEvhQbyT2vUuFW4GbQc_nlhrAkycQYlEiNuJb_qYmJt376F2H1fdK_3yo29j81RwrmITMqJqCAPOKK-EZrnAoC4WHqZ3WsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
؛ LIGHTVELA - یک هوش مصنوعی رایگان که 24 ساعته در دسترس است.
4500 اعتبار و 100 میلیون توکن
مزایای طرح رایگان:
🤖
1 هوش مصنوعی
💳
4500 اعتبار در ماه
🖥
2 پردازنده مجازی + 4 گیگابایت رم (محیط تست)
💾
50 گیگابایت فضای ذخیره‌سازی
🌐
دسترسی 24 ساعته
📱
ادغام با تلگرام و سایر پلتفرم‌ها
نحوه دریافت:
به
lightvela.ai
مراجعه کنید.
یک حساب کاربری ایجاد کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7751" target="_blank">📅 22:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7750">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانفیگ مخصوص چنل -
سرعت خداا
vless://e4b11ac9-46f7-4cc0-92ed-bb9dfaaf3600@94.237.92.65:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=lkMM9FR-o7Z6NwmmQVK8rLhCQR1mbJTgjY_0upeS2SY&security=reality&sid=0436301fb0178b&sni=google.com&spx=%2F442987454d44398&type=tcp#@ArchiveTell
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7750" target="_blank">📅 11:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/C3CLFZXk-umP5bjIw6wG3SYthAzr4C9IvnnsA00Q4qiKlpnpjgBbohxgAtjdyYOZTDql3OlSn4GV8vZeT-EneSX9M--LTrQBlX3Ut62qMLpQNjg9svqk0WbQIHKthbckv3htuxGq3vcgs3QRJ_RU7qd4Zx7wW1Pa2E6by39TzCUiJ2E2xJoHGw9ku_QGwVTT7Z_8ZYyqqwXg1mWXNoSEEB0qR74tbRty2QP3wHNfgl39cbT0RrgYnj_NHPGg2aC3dLWf_KU83FHGWDSezy-gXHLLrFf_SI7qiEN0VjG69jd0p_hP3Z9rO0Wu2pE8QWEqaYH05-soS_KUpQ-DyDs2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
از تاریخ ۱۴ تا ۱۶ سپتامبر، با ورود به
Z.ai
؛ ۶۰۰ میلیون توکن GLM-5.3 به شما تعلق می‌گیرد، بدون نیاز به اشتراک.
🔗
https://autoclaw.z.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7748" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7747">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AqFf5GU8NzCnxme5tNr-2K3ZbZx-GfANG0mqPqOnp4RcTkKK2yq98E2WtWIsq5dBxNJaR_LHcj7VYEcZhrsJWfb04w7SSgxv_CVZUsHjXyS2kJCOLWdE8B6dIx1_vrMnpGrH-M-El23QQbHhL9LYmCFMyfTlQytXwqSDKnHtpuFMBJoqDgdgMKJLHyfbfumZgb6p-DgGZgDjVilY9syqGSVMKSAoKuGO1hJiV-4HFrGgeSKTROsu-dz2X2fWLc2YXBqbjBDSWA6Ktt1OEU3uVNyQ5tYD2hb0A0p4VsjGdT-VyMnTqGuhF8GvnMIAo0hvwEUZldTw6NkhN7HzmtPwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔓
رفع فوری خطای ریجن و تحریم Antigravity
اگر موقع کار با هوش مصنوعی Antigravity گوگل با خطای تحریم ریجن یا گیر کردن روی Eligibility Check روبرو شدید، ابزار متن‌باز
Open AG Patcher
در چند ثانیه این مشکل رو حل می‌کنه:
▫️
رفع محدودیت ریجن:
بدون نیاز به دستکاری یا تغییر کشور اکانت گوگل
▫️
پشتیبانی کامل:
از Antigravity 2 و Antigravity IDE و ترمینال (CLI)
▫️
امن و خودکار:
اجرای پچ با یک کلیک + بکاپ خودکار برای بازگشت به حالت اول
💡
نحوه استفاده:
ابزار رو اجرا کنید و شماره نسخه مورد نظرتون رو بزنید تا پچ در چند ثانیه اعمال بشه (سازگار با ویندوز، مک و لینوکس).
🌐
دریافت ابزار از گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVzwkRpWmKwBR-U5cu-Fy0q5q9IRuW2fsioVumMP5ti2LJYqs7UBW-yBaMqAxQGBCDOBxpgDE4NuyumbcOGA92O19f_DxnA0arahK5E4TZgpqTiR40PyB03X231SLlp2c7FiA9qr6YoQdMUl_Hq7oeix0kO75affuAGy1Q2hN_VAoWvtjd5vVDvmFk-gtsOFX1zoQ0fmj7us_aUhrugBFAKIeBLbSsttTUGgzgTOhYs2keaH5VwG-QfHkidi8tdaNVpU0aC6k0dSKgzc582ncQAUhXGjQfwbqQYAVg99WSeo3QpvPi-LBXoZ933HyXCLnjdWm8Zc9tcWRv_DqKC5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نحوه استفاده از Claude Opus 5 و GPT 5.6 Sol
به صورت رایگان
📣
حساب‌های جدید در
Verdent.com
، یک دوره آزمایشی 7 روزه با 100 اعتبار رایگان دریافت می‌کنند
💯
🆓
🎉
✍️
آنچه دریافت می‌کنید:
👀
🔍
☑️
Claude Opus 5 / Sonnet 5
✅
GPT-5.6
☑️
Gemini 3.1 Pro
✅
GLM-5.2
☑️
Kimi K3
📌
نحوه دریافت:
🔥
⚡️
☑️
به
➡️
🔗
https://verdent.ai/
مراجعه کنید.
✔️
برنامه دسکتاپ یا افزونه VS Code را نصب کنید.
☑️
یک حساب کاربری جدید ایجاد کنید
✉️
✅
مدل مورد نظر خود را انتخاب کنید.
☑️
از اعتبارها برای شروع استفاده کنید
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7746" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7744">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔥
KiraAI
روزانه ۵۰ میلیون توکن رایگان
🤖
مدل‌های موجود قابل استفاده :
⚡️
kira-3.5-pro
⚡️
kira-3.5-flash
⚡️
kira-3.0-image
🔗
kiraai.vn
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔎
scite.ai
— موتور جست‌وجوی استنادی برای تحقیق جدی
۷ روز اشتراک رایگان (تریال رسمی سایت)
📑
Smart Citations
نشان می‌دهد هر مقاله توسط مقالات دیگر تأیید شده، رد شده یا فقط اشاره شده — نه فقط تعداد استناد
🧠
Assistant
پرسش پژوهشی‌ات را می‌پرسی و پاسخ با استناد واقعی و لینک به منبع می‌دهد، نه حدس
🤖
دسترسی به مدل‌های تحقیقاتی:
Claude Sonnet 5 | Claude Opus 4.6 | GPT 5.2
🎛
Personalized Feed
فیلتر و شخصی‌سازی حوزهٔ تحقیق ، فقط موضوعات مرتبط با کارت را ببین
🔗
Custom Dashboards
داشبورد اختصاصی برای کلیدواژه، نویسنده یا ژورنال خاص + هشدار مقالهٔ جدید
📊
Analyses & Topic Classification
دسته‌بندی موضوعی، شناسایی روندها و گپ‌های پژوهشی
آموزش فعالسازی
🔗
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zr4gWdpHY4PdL9iYQAD5pPUpJFIZDenhuUWrXGM-TlrFqzSzoZj-3XG2Kc7ct_onI58u6OuXbawJtwbgQ47XjFQk2Kk831C7w5nl2oP2d6-nAVJl5mBDrIoLkI4eOuCQB8xWKYilEEn2GI1oUfEVbfzrmAqTOP5adYenBD4EmcrZlWfez-JtTEn9gwHUNzy7DYou5l7_Rc-3K6nrUi39BRk81AWxUzMKppQou3Vm384hFWp5HKO0jOrWJ7Ltt8KNQsAf-ssWT4R_GimFOWNt1yf3r_Q0HukhD6QNFLnnve-stKH-Lfo2kyE74f9yUP_fMSuT_CAxEaPsI0oa6eAGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">keys.txt</div>
  <div class="tg-doc-extra">2.7 KB</div>
</div>
<a href="https://t.me/ArchiveTell/7741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان  claude-fable-5 | claude-sonnet-5 |  deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید  @kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url: https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7741" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7740">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDkbqq6MSYe9c8GB5x3z7JyEGelOk7p7ioVTSHLwGXXCzpL_xOLSphbXQc4sNEDbKk36MQOyzonKEO25bk4EaXAooZkay9D3ptxJuLhPvtU6gTS2qsZSuCmZpCirLrIvQsWcgXLtohbtq5R03K_ZDOTPwHpUIn5i4nL_zQT7i9zIqjUn2_fQVrMHNJBapgvLkBjSbf4PXSNhNDst0EdujHrPd53lyqGI9hTPSNXtWaoBUpZAql3_3RATWgar3Bl4EFWpSMnsMRRLN2bcWMCEoVWGzupvSAapUoVLntEFlPBMnBpskXb7X1M7_p_A97agPfaXUTq0Dnki9Z8K2STT7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎁
دامنه رایگان همیشگی بدون کارت اعتباری!
‏بچه‌ها این
پروژه گیت‌هاب
با نزدیک ۲۰۰ هزار استار، دامنه‌های رایگان دائمی میده که واسه پروژه‌های تستی و سایدپراجکت‌ها کاملاً خوراکتونه.
🚀
‏•
دامنه‌های متنوع:
پسوندهایی مثل
.us.kg
و
.qzz.io
بدون هزینه فعال می‌شن
‏•
کنترل کامل:
دسترسی کامل به
Custom Nameservers
و تنظیمات
Cloudflare
دارید
‏
💬
نحوه استفاده:
کافیه برید به سایت پروژه، اکانت بسازید، دامنه دلخواهتون رو ثبت کنید و نیم‌سِروِرهای کلادفلر رو ست کنید.
‏
🔗
سایت پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⌨️
ترجمه سریع و هوشمند، بدون دردسر!
اگه دنبال یک مترجم ساده و کاربردی هستید که فقط به یک سرویس محدود نباشه، پروژه Translator می‌تونه انتخاب خوبی باشه. این پروژه با پشتیبانی از سرویس‌ها و مدل‌های مختلف ترجمه، امکان ترجمه متن، استفاده از قابلیت‌های صوتی و مدیریت تاریخچه ترجمه‌ها رو در یک محیط مدرن و ساده فراهم می‌کنه.
🤖
قابلیت چت با هوش مصنوعی؛
با استفاده از API Key با مدل‌های هوش مصنوعی گفتگو کنید و پاسخ‌های هوشمند دریافت کنید.
🔑
همچنین امکان استفاده از API Key و ترجمه با سرویس‌های هوش مصنوعی مختلف رو داره.
🌐
نسخه آنلاین:
https://codewave4.github.io/Translator/
🔗
سورس پروژه:
https://github.com/codewave4/Translator
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=Aw20ukVHtnJ-kZ8MWmjaV7YF5iTSC_aYZdWtd1177kAuRWC-eeVIH2O9J9QWrCX6wHKp3bs3aWyz-bacBtpI12o8d5tc30-seXSbPwx-xy58Jgn7RHpdjnLuGcDeLT93nuC1EI1rWEG8t9vm7CmK3VSW42GHVFDkefZPwROruI23Mqk8Gte9JS_HqHxkqUsIBkO_NTqlqsm_1VCzzDUfnykesq2o-YxzR-wsXsWUOvl76IAhoScMu4GsaljpxniIpk6seentiBA8_RT3FBIORrQ3flLM-0qYT4B50xJ1_rcXkMYIpoIdK0mBxBxoJMyVVlgSt01EZvwnSjIlJjYcmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=Aw20ukVHtnJ-kZ8MWmjaV7YF5iTSC_aYZdWtd1177kAuRWC-eeVIH2O9J9QWrCX6wHKp3bs3aWyz-bacBtpI12o8d5tc30-seXSbPwx-xy58Jgn7RHpdjnLuGcDeLT93nuC1EI1rWEG8t9vm7CmK3VSW42GHVFDkefZPwROruI23Mqk8Gte9JS_HqHxkqUsIBkO_NTqlqsm_1VCzzDUfnykesq2o-YxzR-wsXsWUOvl76IAhoScMu4GsaljpxniIpk6seentiBA8_RT3FBIORrQ3flLM-0qYT4B50xJ1_rcXkMYIpoIdK0mBxBxoJMyVVlgSt01EZvwnSjIlJjYcmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🎬
ساخت موشن‌گرافیک حرفه‌ای با یه پرامپت!
‏این ابزار هوش مصنوعی کل فرآیند ساخت تیزر تبلیغاتی، از استوری‌بورد تا تدوین صدا و انیمیشن رو خودش انجام میده و خروجی رو با بیت موزیک سینک می‌کنه. خوراک بچه‌هاییه‌ که سریع میخوان خروجی باکیفیت بگیرن.
🔥
‏
⚡️
دسترسی به منابع غنی:
۱۵۷ مدل سناریو، ۲۱۴ استایل بصری و کلی الگوریتم انیمیشن آماده
‏
⚡️
شروع سریع:
کلی تمپلیت آماده‌به‌کار داره که کار رو برای پروژه‌های فوری جلو میندازه
‏
⚡️
عملکرد هوشمند:
کافیه ایده‌تون رو متنی بدید تا در لحظه ویدیو تحویل بده
😎
برای دانلود ابزار تولید ویدیو
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">1.7B token MINIMAX
url:
api.minimax.io/v1
key:
sk-cp-k8fnOYl1xeWGiSNy7qWxNP3Gu-nkuMKLaAFl7ZoCnGiqA2sabKF30eMTQNurXcyGtgGdbM168WEvBhyTOo2WQaE9RoXzVPAyyG3CYwZuybXzDILyBEBc5nk
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7737" target="_blank">📅 14:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7736">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECRHPlG4PjaTQRbfMc0FJQKgGNlnHotT1do8l8uRF5yf1PQHixGULtt6AJYb88RN3lKCy12Kaf6hlsAJ5L1Nfa6RLsvO4Q3N3HnXl3Doeg0HfM4uGbwt09PPxNSQXfCDDVop966wbyh87JJY9ZpSj9Downt-K1Gvvx1L_6K7qEcrgpk53jV9bRQovp6-I3OVWXksIfDkgFi84qYNmnLiBttfxhzRjrni8Pm_Giwazly4fxRsZAtN6MgCzho_H-GvDWmh_g9JjODhrpW_PeuMV1yeNKhMhuIjjikA40c0tR6ywRe-dh_cDAho3AOn6YfLwWJIyq_uu2XZjkNs5oMRVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
مرجع خفن اسکیل‌های ‌Claude Code⁩ و ‌Codex⁩!
‏سایت ‌SkillsMP⁩ یه کاتالوگ تر و تمیز با بیش از ۳۳ هزار اسکیل آماده‌ست که تو کار با هوش مصنوعی کلی جلوتون میندازه.
🤖
‏•
دسته‌بندی جامع:
از برنامه‌نویسی و ماشین‌لرنینگ تا امنیت و کار با ‌API⁩
🔍
‏•
دسترسی سریع:
لینک مستقیم به گیت‌هاب برای هر اسکیل
📂
‏•
کیفیت‌سنجی:
دارای ایندیکاتورهای کیفیت برای انتخاب بهترین ابزارها
⚡️
‏خوراک بچه‌های وایبکودره که بخوان پرقدرت‌تر پروژه‌ها رو ببرن جلو.
🚀
🔗
skillsmp.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🛡
دیگه ایمیل و پسورد اصلیت رو به هیچ سایتی نده!
حتماً براتون پیش اومده که برای ثبت‌نام در یک سایت مجبور شدید ایمیلتون رو بدید، اما بعد از یه مدت صندوق ایمیلتون پر از پیام‌های تبلیغاتی مزاحم شده یا اون سایت هک شده و رمزهاتون لو رفته!
ابزار جالب
AliasVault
دقیقاً برای حل همین مشکل ساخته شده:
💎
این ابزار براتون چیکار می‌کنه؟
⚡️
ساخت بی‌نهایت ایمیل دائمی:
برخلاف ایمیل‌های موقت که بعد از ۱۰ دقیقه می‌پرن، این ایمیل‌ها
کاملاً دائمی و همیشگی
هستن و برای هر اکانت می‌تونید هر تعداد ایمیل دلخواه که خواستید بسازید!
⚡️
دریافت کد ثبت‌نام داخل خود برنامه:
نیازی نیست برید یه ایمیل دیگه باز کنید؛ ایمیل‌های تایید و کدهای ورود مستقیماً داخل همین برنامه براتون میاد!
⚡️
مچ‌گیری از سایت‌های متخلف:
اگر یه سایت ایمیل شما رو به تبلیغاتچی‌ها بفروشه، دقیقاً می‌فهمید کار کی بوده چون برای هر جا یک ایمیل اختصاصی ساختید.
⚡️
نصب روی گوشی و کامپیوتر:
هم اپلیکیشن برای موبایل داره و هم افزونه برای مرورگر، و خودش پسوردها رو سر جای درست پر می‌کنه.
💬
چرا این ابزار فوق‌العاده‌ست؟
•
ایمیل‌ها هرگز منقضی نمی‌شن:
هر زمان در آینده بخواید وارد سایت بشید یا رمزتون رو بازیابی کنید، پیام‌ها باز هم به همین ایمیل دائمی میاد.
•
سقف تعداد ندارید:
برای ۱۰۰ تا سایت هم می‌تونید ۱۰۰ تا ایمیل مستعار و رمز مجزا بسازید.
•
کاملاً رایگان و امن:
بدون هیچ هزینه‌ای، امنیت و آرامش صندوق ایمیلتون رو تضمین می‌کنه.
🌐
ورود به وب‌سایت AliasVault
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nODZgrV3vTwObR2CVJZTVx-6lWOulG8mwew5yzVTSqzoywFatNugNCvkMKxv_nB18fPtZjbJhWsb25o7d2B2dHXGLWZOZADbc_ZXbV7cfUyXHuPfleljVORBjNeqKD8J5m4rIVuqzptm-akRroT38G9M6uYyEJ0-MbU-7FiLNzymY3KAUG0y-IYH8HfVp4CkbjwXXh-TqTuJBgM9XMNlzxFmX65t9I7Ojo-c5Xg6V7fqw8EArb8p5TRsYyifAgyyO4g_RVqzr3zfrXuPizLIzVEW2j03yQHkDsHMamjlgZ3yow1LL1x16xPsmeZsPbEuSdSJ-cItz4D4cXpyY_nqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سایت، ده‌ها مدل و ابزار با اعتبار رایگان روزانه
🎁
💬
Multi AI Chat
GPT، Claude، Gemini، DeepSeek، Grok، Qwen ، Llama
همه در یک چت، با امکان مقایسه جواب‌ها
🎨
تولید و ادیت عکس
تولید تصویر از متن (Flux، Stable Diffusion، Ideogram…)
حذف/تغییر پس‌زمینه، حذف اشیاء و متن از عکس
Face Swap، Upscaler، تبدیل اسکچ به تصویر
ویرایش عکس با دستور متنی + تولید تصویر سه‌بعدی
🎬
ویدیو
تولید ویدیو از متن و از عکس
Face Swap روی ویدیو
خلاصه‌سازی، زیرنویس و ترجمه ویدیوهای یوتیوب
🎵
صوت و موسیقی
ساخت آهنگ (Suno، MusicGen…)، Text-to-Speech با صداهای طبیعی
شبیه‌سازی صدا (Voice Clone)، تبدیل ویس به متن، حذف نویز
✍️
نوشتن و تولید محتوا
تولید محتوا، بازنویسی، خلاصه‌سازی، ترجمه، گرامر
تحقیق کلمه کلیدی و تشخیص محتوای AI
🌐
لینک سایت :
app.1min.ai
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎁
دریافت 20,000,000 توکن رایگان
claude-fable-5 | claude-sonnet-5 |
deepseek-v4-pro | muse-spark-1.2
✅
وارد ربات زیر بشید و api key رو دریافت کنید
@kiro86bot
💡
سازگار با همه سرویس‌های OpenAI-Compatible
🌐
base url:
https://api.xpiki.com/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🆓
هوش مصنوعی رایگان  — بدون ثبت‌نام
Kimi K2.6 | GPT 5 mini | DeepSeek V3.2
📌
امکانات:
⚡️
چت هوش مصنوعی نامحدود
⚡️
تولید متن و محتوا
⚡️
بدون ایمیل، بدون رمز عبور، بدون کارت بانکی
📌
نحوه استفاده:
🔗
وارد
این سایت
بشید مدل موردنظر را انتخاب کنید و شروع کنید.
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoSwDGBkz8ScenLgAeif70gmGZ9Cdz6I7YOj2w5enftpZUROoLGbV5z_bO_M4gJvsyU2mAoT1T5abZ9auWHroGitXzBubqJMagIYkz-mumMs-a9SpWNJwXeIwLP5L-zMON9vHq4nIhp-AvwyGi-2dgvlOHQiapLnXXsA6pzhYJbCCh613yCq8LGLX_6XX9bkrwJUYRvCTHlbHLFz66nwDjUodOrG3VBYsH3PKf45mQ4-gWNvPjVy18E_vNjVyJ7an5hsYR_1StuPHPZcA2NW1oQ48cjndR3mKU9fiQJP-wS_lDEYusmHgYQAwZ86cUF9fdgngDotUOAzqJQvn4djVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
۵۰۰ مگابایت پروکسی رزیدنتیال رایگان (
proxyma1.io
)
یک سرویس پروکسی رزیدنتیال که با ثبت‌نام از طریق تلگرام ۵۰۰ مگابایت ترافیک رایگان می‌دهد و API هم دارد.
📌
نحوه دریافت:
1️⃣
وارد سایت
proxyma1.io
شوید و ثبت‌نام کنید
2️⃣
پس از ثبت‌نام، یک پیام برای استارت ربات تلگرام نمایش داده می‌شود که داخل آن یک کد هدیه قرار دارد
3️⃣
ربات را استارت بزنید و کد را برای ربات ارسال کنید
4️⃣
۵۰۰ مگابایت به حسابتان اضافه می‌شود
🚀
📌
ویژگی‌ها:
☑️
پروکسی رزیدنتیال (Residential)
☑️
۵۰۰ مگابایت ترافیک رایگان
☑️
پشتیبانی از API
☑️
ثبت‌نام آسان با تلگرام
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxP2dMfshgwbCx6YWVVkUIAhv543vJaVwjahHsTpX-9f6uY4pxchqqA9EEXW80xhRLLfU_OqtwWRpROTXgVZbj5B716XJ0EEqaBCmxnx6JY0kxop46fV1k2saC9m6s4AP7_LMUH2-nlKBylltyT1vFtkow9XyW0zYfi-HNS_3tjgWgfrO65QzIKTv91Cb-JkVi2xdKt7g6v1XFiqUfoFKu_VUcP4ZsLo7LSGEfAnNnZLBoiDKddpzKqvOuNHXj0o_nlVxYyUBqrS3LIS8cNWzDimF4JREgCLFpCkesPn9h9fzB3C0Fjs7lqNFZgGb4otXX8j9_3GZl5cknHRnVQOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
۵۰۰۰ اعتبار رایگان برای مدل‌های برتر هوش مصنوعی
پلتفرم جدید در شروع کار ۵۰۰۰ اعتبار به شما هدیه می‌دهد تا با قدرتمندترین شبکه‌های عصبی کار کنید: تولید متن، عکس و ویدیو در یک جا.
📌
امکانات در دسترس:
☑️
چت چندمدلی
☑️
تولید تصویر
☑️
تولید ویدیو
☑️
موجودی اولیه: ۵۰۰۰ اعتبار رایگان
🪙
📌
روش دریافت:
1️⃣
ورود به
getunikey.ai
2️⃣
ثبت‌نام یک حساب کاربری جدید
3️⃣
ایجاد کلید API در تنظیمات پنل
4️⃣
استفاده در رابط چت یا ابزار های واسط
base url:
https://getunikey.ai/v1
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔍
Hidden File Hunter — شکارچی فایل‌های مخفی ویندوز
دنبال فایل‌های مخفی و سیستمی توی ویندوز می‌گردی ولی پیدا کردنشون واقعاً دردسره؟ این ابزار دقیقاً برای همین ساخته شده
👇
؛ Hidden File Hunter یک برنامهٔ دسکتاپ ویندوزیه که تمام فایل‌های مخفی و سیستمی درایوهات رو پیدا می‌کنه و توی یه جدول مرتب و قابل مرور نشونت میده.
✨
امکانات:
✔️
پیدا کردن تمام فایل‌های مخفی و سیستمی در همهٔ درایوها
✔️
نمایش نتایج در یک جدول مرتب و خوانا
✔️
خروجی گرفتن از فهرست کامل مسیرها در قالب فایل TXT
✔️
کپی کردن خود فایل‌ها با حفظ ساختار پوشه‌ها در مقصد دلخواهت
✔️
فقط می‌خونه و کپی می‌کنه — هیچ فایلی رو تغییر نمیده، حذف نمی‌کنه و بهش دست نمی‌زنه
✔️
ساخته‌شده با Python و PySide6
✔️
تم تیره و روشن
✔️
رابط دوزبانهٔ فارسی و انگلیسی
یه ابزار ساده، سریع و امن برای وقتی که می‌خوای بدونی توی سیستمت چه چیزهایی از چشم‌ها پنهان مونده.
🔗
لینک گیت‌هاب:
github
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
اپلیکیشن Bifrost (بایفراست)؛ پل ارتباطی فوق‌سبک تلگرام بر بستر ورکر کلادفلر منتشر شد.
بایفراست یک بریج لوکال (Local SOCKS5) مدرن و بهینه برای اندروید است که ترافیک تلگرام رسمی را از طریق پروتکل TWP به ورکر رایگان کلادفلر متصل می‌کند؛ با پینگ پایین، بدون قطعی و با سرعت دانلود فوق‌العاده بالا.
🔒
بدون نیاز به VPN، بدون روت و با مصرف باتری نزدیک به صفر:
این پروژه کاملاً متن‌باز (Open-Source) است و برخلاف فیلترشکن‌ها از VpnService استفاده نمی‌کند (هیچ علامت کلیدی بالای صفحه نمایش داده نمی‌شود و اینترنت سایر برنامه‌ها کاملاً دست‌نخورده و بدون تغییر باقی می‌ماند). مصرف پردازنده در زمان عدم استفاده دقیقاً ۰.۰٪ است و امنیت و رمزنگاری پیش‌فرض تلگرام (MTProto) نیز کاملاً حفظ می‌شود.
📥
دانلود و نصب برنامه (از گیت‌هاب):
https://github.com/Qorvhex/Bifrost/releases
⚡️
کانفیگ تستی برای شروع (بعد از نصب، کپی کنید و داخل برنامه Paste کنید):
twp://telp.qorvhe-x.workers.dev?clean_ip=1music.cc#Bifrost-Test
🛠
سورس‌کد اسکریپت ورکر (TWP):
https://github.com/Qorvhex/TWP
📁
لینک پروژه و سورس‌کد در گیت‌هاب:
https://github.com/Qorvhex/Bifrost
لطفاً تستش کنید و سرعت و عملکردش رو بهم بگید!
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🖥
مرورگر ضد ردیابی Private Browser Pro؛ هویت جعلی و دور زدن بن شدن اکانت‌ها!
​بچه‌ها اگه نیاز دارید روی یک سایت چند اکانت مجزا بسازید بدون اینکه سیستم‌های امنیتی بفهمن همه‌شون مال یک نفره، یا می‌خواید ردپای دیجیتالی‌تون رو کامل مخفی کنید، این مرورگر اوپن‌سورس ویندوزی دقیقاً همون چیزیه که دنبالشید. این ابزار بر پایه نسخه فوق‌امن Ungoogled Chromium و Electron ساخته شده و از زبان فارسی هم پشتیبانی می‌کنه.
​
🎭
جعل مشخصات سیستم (فینگرپرینت):
شبیه‌سازی کارت‌های گرافیک قدرتمند (مثل RTX 4090، سری RX 7900 و تراشه‌های اپل)، اضافه کردن نویز به Canvas و AudioContext و هماهنگ‌سازی هدرها برای عبور آسان از سد کپچاهای Cloudflare Turnstile، hCaptcha و reCAPTCHA
​
📁
مدیریت و تفکیک کامل پروفایل‌ها:
امکان ساخت محیط‌های دائمی (Persistent) برای ذخیره دیتای هر اکانت در پوشه جداگانه، یا حالت موقت و یک‌بارمصرف (Ephemeral) که با بستن پنجره کل ردپا پاک میشه + دکمه پاک‌سازی آنی
​
✅
پروکسی پیشرفته و ضد نشت اطلاعات:
پشتیبانی از پروکسی‌های SOCKS5 و HTTP (با یوزرنیم و پسورد)، حل آدرس‌ها از داخل پروکسی جهت جلوگیری از DNS Leak و غیرفعال‌سازی WebRTC برای مخفی ماندن کامل IP واقعی
​
✨
محیط کاربری تمیز و دو زبانه:
کرومیوم دست‌نخورده بدون واترمارک‌های تستی، تم دارک با کلیدهای میانبر سریع و پشتیبانی کامل از منوی فارسی و انگلیسی
​
💡
بهترین سناریوی استفاده:
ایده‌آل برای مدیریت چند اکانت در شبکه‌های اجتماعی و پلتفرم‌های حساس، تست وب، ریسرچ‌های OSINT و حفظ حریم خصوصی بدون نیاز به خرید اشتراک‌های گران‌قیمت مرورگرهای ضد ردیابی.
​
🔗
گیت‌هاب
​
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📥
تبدیل فایل‌های تلگرام به لینک مستقیم نیم‌بها با ربات Leecher!
بچه‌ها اگه کندی دانلود از تلگرام یا قطعی فیلترشکن موقع دریافت فایل‌های حجیم کلافتون کرده، یا می‌خواید تورنت و ویدیوهای یوتیوب رو مستقیم به فایل تلگرامی تبدیل کنید، این ربات لیچر ایرانی حسابی به کارتون میاد.
🇮🇷
لینک مستقیم با ترافیک نیم‌بها:
تبدیل آنی فایل‌های تلگرام به لینک دانلود پرسرعت تحت وب (سازگار با دانلود منیجرها) با محاسبه مصرف اینترنت به‌صورت نیم‌بها
🌐
دانلودر همه‌کاره (لینک به فایل):
پشتیبانی از دانلود مستقیم لینک‌های یوتیوب، اینستاگرام، وب‌سایت‌ها و حتی فایل‌های تورنت و تحویل فایل داخل چت
☁️
اتصال ابری به گوگل درایو:
امکان لینک کردن اکانت شخصی Google Drive برای ذخیره و آپلود مستقیم فایل‌ها در فضای ابری بدون مصرف حجم گوشی
🎁
شارژ رایگان روزانه:
۱ گیگابایت حجم رایگان در هر ۲۴ ساعت بدون نیاز به پرداخت هزینه یا خرید اشتراک
💡
نکته کاربردی:
لینک‌های ایجادشده بین ۶ تا ۸ ساعت معتبر هستند؛ کافیه فایل رو به ربات بفرستید، لینک مستقیم سرور ایران رو داخل IDM کپی کنید و با حداکثر پهنای باند خط‌تون دانلود کنید.
🔗
استارت ربات
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqJw_RB2_BFQhht1HX4sMSQrmH7AXgpMXtvPbiMfL8IA5943Wltw3_7zVA7hl-DA_Ra7ekHb28U7WC7h4Nc7UCy0KcGo1SBJAveO2EWXUtOmSjBQiVuENF-g2ZuWtzZw9bYtA0eV80zhrbsD1Hx2t0EHwIrO6RayQx1lMoZnhiz5SO_swbbYc9HINk3GRUZ693QYNaKvObhVKbxkswUdtxkBqHMyUOsCeEDZZVxlwCjRFqtlGmE8x27OKOKZPaY39VuLApSpKBDifbA_FPwqyY2-rHEb6Etn3adPXVYtIjEVfbn6X-zEVKEBwjGna50bilgl0_QOm1sgrJLuqpdM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید (1.8.0) برنامه MSN-GUARD منتشر شد :
💢
BOOM
💢
تغییرات :
1- اضافه شدن متد اختصاصی SHARD برای اولین بار
-_-_-_-_-_-_-_-
2- دسترس‌پذیری کامل و پشتیبانی 100% از صفحه‌خوان TalkBack برای عزیزان نابینا و کم‌بینا برای اولین بار
-_-_-_-_-_-_-_-
3- آپدیت هسته
-_-_-_-_-_-_-_-
4- اضافه کردن قابلیت Backup و Restore و Reset Factory از تنظیمات برنامه
-_-_-_-_-_-_-_-
5- برطرف شدن مشکل دکمه Reconnect در نوتیفیکیشن
-_-_-_-_-_-_-_-
6- اضافه شدن Theme کاملا روشن برای استفاده زیر آفتاب
-_-_-_-_-_-_-_-
7- برطرف شدن باگ اتصال خودکار پس از قطعی اینترنت و چند باگ دیگر
-_-_-_-_-_-_-_-
6 روش دسترسی به اینترنت آزاد:
1: متد Masque
2- متد Wireguard
3- متد Warp On Warp
4- متد Psiphon (اختصاصی و اولین)
💯
5- متد Tor (اختصاصی و اولین)
💯
6- متد SHARD (اختصاصی و اولین)
💯
💻
ریپازیتوری گیت‌هاب (متن‌باز):
https://github.com/mbm110/MSN-GUARD
📌
لینک مستقیم دانلود :
برای گوشی های 64 بیت
برای گوشی های  32 بیت
برای تمامی گوشی ها
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7723" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7722">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✉️
؛ Turbo Mail ایمیل موقت، سریع و بدون دردسر
اگه برای ثبت‌نام یا دریافت کد تأیید به یه ایمیل موقت نیاز دارید، Turbo Mail یه گزینه ساده و سریع برای شماست.
⚡️
ساخت فوری ایمیل موقت
👌
بدون نیاز به لاگین و ثبت‌نام
⏳
اعتبار ۲۴ ساعته
🔒
مناسب برای دریافت ایمیل و کدهای تأیید
🚀
ساده، سریع و بدون مراحل اضافی
کافیه وارد سایت بشید، ایمیل موقتتون رو بسازید و استفاده کنید.
🔗
https://mail.turbocenter.shop
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7722" target="_blank">📅 18:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7721">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎧
دستیار هوشمند و همه‌کاره موزیک‌بازها؛ دانلود با کیفیت FLAC با ربات MelodyAddict!
بچه‌ها اگه عشق موسیقی هستید و از دانلود تک‌به‌تک آهنگ‌ها، افت کیفیت یا پیدا نکردن موزیک پس‌زمینه کلیپ‌ها کلافه شدید، این ربات فوق‌العاده با پشتیبانی کامل از زبان فارسی دقیقاً خوراکتونه. همه‌چیز از شزم اختصاصی گرفته تا رصد خودکار پلی‌لیست‌ها رو براتون یکجا جمع کرده.
🔄
سینک خودکار پلی‌لیست‌ها:
زیر نظر گرفتن لایک‌ها و پلی‌لیست‌های Spotify، SoundCloud، YouTube Music و Apple Music و ارسال خودکار ترک‌های جدید با امکان زمان‌بندی ارسال (۳ ساعته، روزانه یا هفتگی با دستور /digest)
🔍
شناسایی جادویی آهنگ:
پیدا کردن نام و فایل موزیک فقط با فرستادن یک وویس کوتاه، زمزمه، فایل ویدیویی یا لینک ریلز اینستاگرام، تیک‌تاک، یوتیوب و توییتر
💎
کیفیت استودیویی FLAC و Lossless:
قابلیت تنظیم کیفیت پیش‌فرض خروجی برای گوش دادن به بالاترین بیت‌ریت ممکن، با سرعت عالی و کاملاً بدون تبلیغات
📂
مدیریت پلی‌لیست‌های ابری:
امکان دسته‌بندی، ساخت و اشتراک‌گذاری مستقیم پلی‌لیست‌های شخصی داخل تلگرام
💡
نحوه استفاده:
ربات رو استارت کنید، زبون رو روی فارسی بذارید و برای شروع کافیه وویس یک آهنگ یا لینک پلی‌لیست موردعلاقتون از اسپاتیفای یا ساندکلاد رو براش بفرستید تا بقیه کارها رو خودش اتوماتیک انجام بده.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BRw1IRvioqvTZpsg9COwdAXXuOxhrV2H0KL7p49ooczXudUyj9xNBxF19yLuMQoayyWPEiHzCTnoYx6FZI-S6wkkjoDmntU708A3s6HWrjUKmT36QRzKcVYtP5rBWdt1nhr0pcYyFqQoNlD3rMubtAxUZwYVzR1GW-en0jUD3Fd9jhX0RdGSji0Yg-_YWgXQA5tXFCMbB38_KEKmtQjzujmnNJisU3Ow3FAqhKqJTfRS7iJ4uv09g3EkAdaGQPEG67Eq1s5_sL81wWKehjeg0ngccgqDaKcrLKABYTrQn8tZgExtKSMxBAU0ZWLLK7zd5rjzBQAc3U1TMCMcQk2sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید ArasClient منتشر شد!
نسخه جدید با اضافه شدن بخش Free منتشر شد و از این به بعد این بخش به‌صورت مرتب آپدیت میشه.
📱
؛ ArasClient یک کلاینت سبک و کاربردی برای مدیریت و استفاده از کانفیگ‌هاست که تمرکزش روی سرعت، سادگی و اتصال راحت‌تره.
🆕
اضافه شدن بخش Free
⚡️
آپدیت منظم کانفیگ‌ها
📊
تست و مرتب‌سازی هوشمند سرورها
🔄
انتخاب سریع‌تر سرورهای مناسب
📦
پشتیبانی از نسخه‌های مختلف اندروید
🔗
دانلود نسخه جدید:
https://github.com/ArasTey/ArasClient/releases/download/v1.6.8/ArasClient_1.6.8_arm64-v8a.apk
🔗
سورس پروژه:
https://github.com/ArasTey/ArasClient
💬
نظر، انتقاد یا پیشنهادتون رو کامنت کنید.
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtRhsH9HcRxPooyF6huy0bHfELmS1ajHXS3dZiS0jSlVgdz4tzeXOTW88gNOxrjOyVLJ8TnwSwlRkKKaJZn05_soEpt7AF_utDslSFGpwJEbZA_pLSzEwbf-byCX36HtN3zE4kzIhdz_siYX_IDXwqLUPuUdxBxwHIgMFGK-ctUJWbLYW3qaUJlMmp4awmxV9Uw_l_HxR2knSKu2QlPTG_RaWmgqFTZjaJAkS9usx9VwSnL9nqPvrS5vyFkJD2xPMrfGKF5wkgNfWlhY3CaVWWy0EQP3Ev2970_XfJTEukt4GatC-n8jwVwTccxXOyW202RrZRL9eMirHAAGnATvUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
اگر می‌خوای شبکه‌های کامپیوتری رو از پایه تا سطح حرفه‌ای یاد بگیری، نت‌داد دقیقاً برای تو ساخته شده.
از مفاهیم بنیادی مثل آدرس‌دهی IP، سوییچینگ، مسیریابی و امنیت گرفته تا شبکه‌های مدرن، همه چیز با پروژه‌های عملی و مثال‌های کاربردی آموزش داده می‌شه.
✔️
۱۰۰٪ پروژه‌محور
✔️
۵۳ درس تخصصی
✔️
۱۴ بخش آموزشی
شروع یادگیری از اینجا:
🔗
https://netdad.vercel.app
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAzFRj2xtHSnXxNfRAETBg-o9_1n9-2iDXYSrpa7M3AtOcaEk6vEFGj5dRQdTe25EedVM2izLin8egHHXi5Mmu_X8ES6tF937sqIuO_aXHSRN8QNhyCDwUSpjle1WkjrX_OH2jm8bWJ8I3NA6oQPfPb31aEb2Ixo6Cnwb06te-InMguZjghydy2jgkGMMdwy2ivoTKJm7YfhS7HDVjlP6A7tD47OXTvBvwfChg6asNpgqbmR3Yhda1vFiKdc1TZOgtl6ho33qWXK3gGG5yLYVcmPc4kZCTaZKKbPxzJbxZl4pOVD68ze7OS5crye-PIldBkcz1ksrvXdLDcjrdyM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQYuyjLyWtV_TCnQ2F6Mg0rInn764KjStgNn1EujM7PIz_PiIorRh9H_JQFA6W6poJ3uG0O3p2YHFDLKlhu6OVubRk9wue67i31plRCVmoNI847hJ2i0gSQt__ez05MaYTchxB5s0GKS-pz1TTQ9qwwfQuWUBiTsCrXDyMeg5NsGeUnX9s0Tdkx4wSiRI_KyvRtR4O7IggR2tCa9yZQg4fqetVXvJsC5MdY0aySL4BYx8bWZekm31nxZFFmL-oB7OhrN6frMPNaHQHFWOfyDusdthqMAm_LjjppDMT8VqfH050SSO5KAEy2J7IV6ikN8CZVUazJ0KgpZL1cYqAWi_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥁
کیبورد لپ‌تاپت رو به یه درامز حرفه‌ای تبدیل کن
پروژه خفن KeyBeat یه استودیوی درامز تحت وب هست که بدون نیاز به هیچ نصبی، مرورگرت رو به یه ساز واقعی تبدیل می‌کنه
🔥
یه پروژه اوپن‌سورس عالی برای برنامه‌نویس‌ها، آهنگسازها و عشقِ موزیکا
🔗
لینک سورس کد و اجرای مستقیم:
https://github.com/faithsaly5-stack/Keybeat
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_P5RpT4Q9oUzx7ENMVQnYKYZvqV4jm7Oi6iYctDVqm-Eeq7UXPGNap89S9U6QfsBgKA82cQnt53e2fteplogdFSR4rRkzQlj7TE0H3iDqKDCPuDQClpEE4xySqfSWyOeQ1eEsMKvIK-4Yf3K_8R3n7vrGzgeT5Kx9kcOTFcuW8SCAUkdX5wtYdaurIt7MYCd9e-QsykVL8hLbnoqHWgwn7-y155EYCw1RCCNpjMrboT8Q-2OqXPgp29xB1T8AGHANlEG8d6IUu0vjHfZCj10XfjHZQHCZcJMAfOwcYlrkW53a5YDQ8h0PFf0OM9rrDtuxLtTsSuTQOjG_JgIDKMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
دریافت آیپی رزیندنتال رایگان
💎
با گوگلتون سایت زیر بشید و روی claim offer کلیک کنید.
بعدش برید بخش proxy generator و پرش کنید و بزنین براتون 300 مگ آیپی رزیدنتال میده
🆓
http://rainproxy.io
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7715" target="_blank">📅 10:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7712">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpDOtm6SBb9IjSD44Y7P-RQ9ZeJ9g0djgKxFMjaI9aE-AUe7nL37jMMuAUAPAcfGI5wO7eI54vUZ6ID4tv7Rm22AOHe65yW0fgLI71LEtCl6E5ityWUZHwYq3CJ1xW1cLZ3XuruVQk9n0pguwfykAnoI75qWpmMnXZVVZ6yr-V-ZclZv4mRUODN3SkDs3jlZHEL142C4YVoUDuWk_hFKAYodorlLXgOjMaPKUcI_vKho-5mfFh5cXGRnz-GlZT2-n8XraWbFIRwukwxEcKI3-bAWFYyFLaJGqw9NdrbVd2Mv67QgnvbKP1UeWsjktYX8ZuDM9lShs1xrpnO3BHMJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
15 دلار اعتبار رایگان برای دسترسی به بهترین مدل‌های هوش مصنوعی
استفاده از مرورگر به شما 15 دلار اعتبار می‌دهد تا مدل‌هایی مانند موارد زیر را امتحان کنید:
• GPT-6 Astra
• DeepSeek V4.1 Flash
• GPT-5.6 Luna
• Claude Opus 5
• Grok 4.5
برای دریافت:
🔗
browser-use.com
با استفاده از حساب گوگل خود ثبت نام کنید و شروع به استفاده کنید.
برای دریافت اعتبار بیشتر، از چندین حساب استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🧰
جعبه‌ابزار همه‌کاره و فوق‌سریع تلگرام؛ معرفی آپدیت بزرگ بات Amir Tools!
بچه‌ها اگه کلافه شدید از اینکه برای هر کار کوچیک (هوش مصنوعی، استعلام قیمت ارز، دانلود یوتیوب و تبدیل فایل) یک ربات جداگانه استارت کنید، این بات همه‌کاره دقیقاً خوراکتونه. در آپدیت جدیدش کلی ابزار مدرن با رابط شیشه‌ای اضافه شده تا از ده‌ها بات متفرقه بی‌نیاز بشید.
🧠
هوش مصنوعی با حافظه اختصاصی:
مکالمه پیوسته بدون فراموشی کانتکست چت، سوئیچ خودکار روی مدل‌های پشتیبان و امکان ریست سشن
📥
فایل به لینک مستقیم و دانلودر یوتیوب:
تبدیل آنی انواع فایل، ویدیو، آهنگ و ویس به لینک مستقیم پرسرعت + دانلود مدیا از یوتیوب با بالاترین کیفیت
📈
نرخ لحظه‌ای و چارت زنده بازار:
استعلام آنی قیمت دلار، تتر و ارزهای دیجیتال (BTC, ETH, TON و...) همراه با نمودار اختصاصی و باکس High & Low
🤫
پیام ناشناس امن و دوطرفه:
ساخت لینک اختصاصی با آیدی تصادفی برای دریافت متن، ویس و عکس ناشناس با قابلیت پاسخ‌گویی مستقیم
🎁
سیستم قرعه‌کشی خودکار کانال:
ساخت مسابقات و چالش‌های گروهی با دکمه شیشه‌ای و قرعه‌کشی کاملاً خودکار و عادلانه بین اعضا
🛠
میکروابزارهای روزمره:
ساخت بارکد تصویری (QR Code)، پسوردساز غیرقابل‌نفوذ، مبدل ارز به تومان، هواشناسی و مینی‌گیم‌های کوئیز
💡
نحوه استفاده:
وارد ربات بشید، دکمه شیشه‌ای منو رو لمس کنید و بدون نیاز به رجیستر یا مراحل طولانی، به تمامی ابزارها به‌صورت یکپارچه و رایگان دسترسی پیدا کنید.
🔗
استارت ربات هوشمند
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByV-pR0-MUmclnAmzKtyOyBqXqS-GFMVY3EX_YgSNsT-sc6pTUysfLQHBVB7uRBb2PjBrYnQBV34gHtd6qI9z-yM-pTjO5hkvGfD-NKlovBjMJonU3deueB2fHeH3BWSjmazqwS_bX_IBp45o6flh1zmd4RlIz0wuRiL-bz5TTVXEKTWxckvNTSSh1KWnIsatM8KurZVvKNl_uafvQOev3E2szffxlJp2MXH_I3gMvKBlr1BNVmaYjN-1GqO4AA1FRyCI29cPbzr_VWwPBgc8neMRzktOqguAptkmGKm-7nRETWsp3nnu95H8Lz5RmmSD7mM7-jJmg8ZhncXlRXuRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل:
① به
https://arena.ai/
مراجعه کنید.
② حالت
Direct Mode
را انتخاب کنید.
③ در لیست مدل‌ها،
GPT-Image-2.5 Sunburst
را پیدا کنید.
④ به مدت
72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود
.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neh01YiCBmkbrx5VcE6HK9VRLHsaUCLD_heRZx61T0sXAWFW2FSUFcrgPcx8_uQmSr4zEPKemseZRk5QMq7jnkM5zQuhVhRkVjwdr1PC8SuhrYinB43qG8B-rzO3V-qjJNeRexJlKFicuGvMCmgx4jMuYbbKUYGiYqpV0Swmu95YYLx-FiLXIaVJj4flAPbWqNtprUwVKdEYvULRYQTFSxbkjKpAOD15FrTQBSLkARrrXf3eoHJldX5esylGWYQHryfcyOH6oI2M_Wntq22XN6q4aYoYKUaHsusM44Zpm5z7-s3UHBPbzX9OuILR_BA1W0xsPAKs5YvxCxTxUci4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek V4.1 Flash به صورت رایگان
💥
🆓
این نسخه ۲ روز پیش منتشر شده است. دارای ۱ میلیون توکن متن، قابلیت‌های بصری پیشرفته و کیفیت مناسب برای استفاده در سیستم‌های هوشمند است.
🚀
🔺
رایگان به صورت روزانه
🔺
پنجره متن با ظرفیت ۱ میلیون توکن
🔺
سهم استفاده روزانه هر روز ریست می‌شود.
هنوز مشخص نیست که این سرویس چه مدت به صورت رایگان باقی خواهد ماند.
‼️
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7705" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7704">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWeG8lPSkzXXjE1UWjvDCrs24OH1hIWdmwluGqLGI_uUuEdUS-iRcChYKviLl2dgv-1SAkd0lgNDS5AAuSB-r6XMzRrF-OGB_76xsr-JcoFS13cKEmD9xASBTyiqloH4-lMCl0rZ7tHblFeIZ0YMCwCk7Tk03uuGxu2721mAG-DjRt59R0GLLBFSMXVJjZ28L96lJkSTl2oAZyixgx9TDViL3ghG0X-FaoNL2JzmfSgGRKzWdqiXBqG0KvdL5OO8y824dCs5UniCYxHYiVRmmUJFm2fpBA5_3WRUdTgOWN8DTjFnFHGng9ELTVt7XAk2Bs8MFFUi_b8FgvDu2jtwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به غول های هوش منصوعی به صورت رایگان
💥
🆓
با این سایت میتونید 5 دلار اعتبار رایگان برای بهترین مدل ها دریافت کنید همچنین این سایت 3 مدل کاملا رایگان بهتون میده
💵
😎
Kimi K3 | Deepseek 4 Flash | Mimo 2.5
✅
📌
Base URL: https://tokenharbor.ai/v1  با جیمیل…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7704" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7702">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1s8skIYiVZn_HMrSFCGgkXQUhOI7h2pdGw-KEvOuYCGxSWMQ-yi-fcIfMib0U6adIR597RYnVysVjtTetbKh4WsQnHvJfYaPQAzUjqGNLZuCSU9w9WUGRe_8UGGuMRD2g8ZRMEGjqCsA5xKAxngDpGLtdQUK3Sd256lOuEejyprEjygHQN-KzXx0QSGCOU7U-Yq2H4kyLUjQLd7tlpXiltVzB77KRsAi1ev5ktUV64lZIaXUHliml38q9XXJgiWxz2wzY5UAGXdgpW31vk3tfrJfTNdAyW_PV8N7dIxsfhh3HIypwgzvOEnQx_BYlSLgLfEUkbxyZFAqo1ylCxGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBLlMh_JjYuW7o3WRDtg-6ti_9Dcemktxn3j6wnc2h2PBai6Fa4dO3_budhCwMe7Xq8hgbfhMNkpwpZmUWj4-GE25psq6Jwe754mmYBVtysrYxn2F0xsnRnc6nHK1xfr03_IWW_CY6oX1EzbvKIptvZeyVAsl81Np-lOnNODVZhOF3Tlw8DB-_glXPBKwz2zh8MiGY11hv6at5SOYLyK3tsCEhxm7kQ0ijajAW_fi6iuPB7JdRr9GVbAoKJhuE9RueoJ9PGj4eJAt6pxfvkKuOxVnQmjcSSib3WU99RBlSOhiZgQZa87Y6b20xy9rVnWVMVQesfK7ZH7QOs0fSOSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">150 میلیون توکن رایگان برای مدل های زیر
💥
🆓
GLM 5.3 Flash | Qwen 3.8 Flash | Mimo 2.5 | GLM 5.3 | Hy 3 | Qwen3.8 27b
✅
وارد سایت زیر بشید با جیمیل ثبت نام کنید سپس از طریق منو 50 میلیون توکن امروز هم دریافت کنید
✅
‼️
نکته :
از مدل های با پسوند Free استفاده کنید و احتمالا این دسترسی شامل محدودیت تعداد ریکوئست در دقیقه باشه ، همچنین ممکن هست هر لحظه اشتراک رایگان بپره
📌
Base URL :
https://kiraai.vn/api/v1
🔗
لینک ثبت نام
🔗
لینک گرفتن کلید
🔗
لینک دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🧠
پروژه OXYGPT — یه ربات تلگرامی که هوش مصنوعی رو حسابی جدی گرفته!
بچه‌ها این صرفاً یه ربات چت نیست، یه اکوسیستم کامل AI روی تلگرامه: چند مدل هوش مصنوعی، مربی‌های حرفه‌ای تریدینگ، sandbox واقعی لینوکس، اخبار فارکس زنده و داشبورد مدیریتی. خوراک کسایی که می‌خوان یه بات production-grade بسازن نه یه دمو دو ساعته
🔥
↔
مسیریابی چند-مدلی AI
: استخر کلید Gemini + سرویس‌های سازگار با OpenAI، round-robin می‌چرخن و روی خطای 429/503 خودشون فالبک می‌زنن
🪟
پنجره‌های مکالمه مجزا
: هر کاربر تا ۵ چت جدا با تاریخچه و state خودش می‌تونه باز نگه‌داره
🧙‍♂️
مربی‌های تریدینگ (Persona)
: چهار شخصیت آماده (ICT، Quarterly Theory، Matrix/369، Price Action) با یه دستور سریع صدا زده می‌شن
📓
ژورنال معاملات
: ثبت و پیگیری ترید‌ها با قالب‌های اختصاصی، مستقیم داخل تلگرام
📰
اخبار فارکس زنده
: رویدادهای پرتأثیر Forex Factory رو با تحلیل کوتاه AI نشون میده
🖥️
قابلیت Sandbox واقعی لینوکس (E2B)
: مدل می‌تونه کد اجرا کنه، پکیج نصب کنه، ریپو کلون کنه و فایل بفرسته/بگیره
🔑
قابلیت BYOK
: کلید API خودتو وصل کن، از محدودیت پیام و quota عمومی بی‌نیاز شو
👁
مانیتورینگ کانال با AI
: کانال‌های تلگرام رو زیر نظر می‌گیره و پست‌های مهم رو تحلیل و تحویل میده
💡
دیپلوی با یه دستور روی Docker/Railway انجام میشه، و هر ۵ ساعت یه بک‌آپ خودکار از کل دیتابیس‌ها زیپ و برات تو تلگرام ارسال میشه — دیگه نگران از دست رفتن دیتا نباش.
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rdu57tL9dYYaxc2_WuIqCJHI58o8isBi3IQjFI8XWFjOR5snQzdQ2kmvpvcVuxmu9XJ2I4jHQvoHg1PyYVW2dtcytYAnHME_lcPhpB912hOXG-hQpAsRbisHFxXj9PZCDdqdogg888Tkw4-KFqckQcZULwbLOCcpQ1UZksuyft9hgDun3nwPl695rjenZ0plO0JKvUKxMaGIJ6H8eljZOyZBMO758pfqzZWEXWsnFHonpveLTqgOZ2oZooXHWph2ydOoQasWsSkTMN1S-eKA3NO5EQIVAspEr8rave4XXmbE4h-eZFHeVYw5L8ApzLu-SVTAYPxA71yTQOYKJgqooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8yjd97D1ZQ0NyfQIaYntdxTxa_OrWmW9EOr-crLZOUMx_c9YNYxBbsnC-fer22BCWxUjOpy_dP0F-ReidndN51Jn63kCTdklk4Ze70sh-svBJEuhu84d8q-qYdpyjs21tZ8zm-bpDmxJxP69cFNDa7m-pwnRiNIMND8buEmqLeUjfcLpM824I6yjR8rz7Ar6W0GQg_sFbZWqnt71tpN2NXZu_hnM0F7yi-xMk8ylp8gDh6r6GM8KGjomo9cwd9P9v5Aj3qmO-paG5CvSRQYKdCk3siP0xiCkd0ynM9cTxwOmQIbnvSDhpuQkSDgIGjBjV4mL9McaI13okCJEDoGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزانه 1 میلیون توکن رایگان برای مدل‌های زیر
💥
🆓
Gemini 3.8 flash | Muse Spark 1.3 |GLM 5.3 Flash | Deepseek V4 Flash | Deepseek V4 Pro | GPT 5.6 Luna | Gemini 3.1 pro
✅
وارد سایت زیر بشید و ثبت نام کنید و یک کلید دریافت کنید
✅
‼️
نکته :
با هر آیپی ۱ بار میشه ثبت نام کرد اگه میخواید چند اکانت بسازید هربار آیپی هارو تعویض کنید
📌
Base URL :
https://apinex.bond/v1
🔗
لینک سایت
🔗
گرفتن کلید
🔗
دیدن مدل ها
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7695" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7694">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvgM_sos1bAU7Vuk6EOFoIKO-IUoscFJtbMmFbf4cY9GhvWx1JzqgVJuQSmLxXfJUyAQrq1StunSTmTudj9VYf6scPo5hosKcjQyKa8-vkmUclJyKk7kaRy11YeSK-O2uH6d4dNQPn4eoxFCOO_NADzOMwFx0sJjuN8jiKjknDOT2XpMzTZFuDtGRbz92NZflPz0c-RCkXh4VbDa9hS6JSaai8dYiBIBXYjLLq_uvv67G6ONbkeN_qB9Tf-fm0AO7lds7hE1h1lwauTwbPOQPktIB9sWiDPj_10mJMR0Gk8k771mF5fa_56pFZMGZ7H_ik3-RJ0b5HS-nMEoJvG6dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 میلیون توکن رایگان 1 ساله
💥
🆓
Fable 5 | Opus 5 | GPT 5.6 Sol | Grok 4.6 | GLM 5.3 | Qwen 3.8 max | Kimi K3 | Deepseek V4 Pro 0813
✅
برید داخل
این سایت
ثبت نام کنید
حالا برید داخل
این بخش
پلن سالانه رو انتخاب کنید و این کد تخفیف رو بزنید :
DEVWEEK
بعد اینکه تخفیف اعمال شد تایید کنید و تمام ، یک api بگیرید و استفاده کنید
✅
📌
Base URL :
https://codecraftapi.com/v1
اکثر مدل های جهان رو داره میتونید از Playground چک کنید ، چون سایت شلوغی هست طول میکشه تا ریکوئست ها جواب بدن
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7694" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7692">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBtn_v1AKTStixVguvEdBZ4dz6UVYZ-bt8Z1pe--KluB6N79StPOUO6s66sWwESKtfGkd7F0jUz4LQzyaMVNOUCNIObSOaIC07vKukEhZptEg-VDti_l8F8DZBEaUlcQTNFWyhkkGRURHUjc1sfgnZ4Uy4GteoSCkQU8eq5RhaEmqE0S37BVf1EV4JrZynvaB65uK69m0HI6v3VD2zWplu20hygFoN9oxcLTWcCVunaPblsmjxDcZWyp1dLOceNUwnHAGEkMswYjKNwwXUn4BqgJR1Cn_psg8mGr2vK_aySOfl7V31jigfHH4u8hkOMJwrwfxgeatnvJyu-jpxUdFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
تغییر ریجن گوگل در ۳۰ ثانیه
⏱️
با فیلتر شکن کشور مقصد یکم برین تو گوگل بچرخین،
بعد به لینک زیر بروید، ریجن را انتخاب کنید، دلیل تغییر را بنویسید و ارسال کنید.
https://policies.google.com/country-association-form
حداکثر تا ۲ ساعت ریجن به جایی که میخواهید عوض می‌شود و ایمیلش میاد
✅
بعدش میتونین به راحتی از antigravity و سرویس های دیگه گوگل استفاده کنین.
از توجهتان ممنونم
🙏
✈️
@ArchiveTell
|
#method</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📌
Model :
gpt-6-astra
📌
Base URL :
https://api.eirouter.ai/openai/v1
sk-e76d452dff7eccef0a1b6bde4f8262c7f628f4f2991676cf3188d0cb68023b3f
sk-778bbaffd07397311260074542e405ab11833bf458e0250363ac1afd7db02297
sk-b028d3f23d96d0b0fc96a24985164437fcaf272276caf33548a664a0df424dc1
sk-1f153c31ccd2448b30c2f56287d5dc8fcc8ddafa579d12a797450321d86e9d29
sk-3334618935b09f67a70938d3379971e3ad350fec1154008d3abbaa07565c00b3
sk-242582ef9fc5e53351eb2fd67178b83033a450a61d048cf66be6aacf98a9e2bc
sk-db726cb7cc5b14160f9d8900455fcd34fd56cbb94f3afac65494a5161eee35b6
sk-7e85fc089be2d58f76c236c8ae1efc6062f68a459bdc9f87bcbe896c2d7307e2
sk-cca857a86f2c62b5d704f2234ed5632f8ef4dfbfcc0da509fe0e021516a0406d
sk-3c3eb497a104328775de0ddb333c7c8d596c20a89e25bbe7e204318f35e2b050
موجودی هر کلید هست 5 دلار ولی نکته اینجاست توی سایت قیمت هر یک میلیون توکن این مدل هست 1 دلار
😁
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7688" target="_blank">📅 22:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7687">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=Kj3HgjAVrlCJpyZVSWbOcEJPILCISP2EiSKJRGHX3Rcii8yLMf_bSkwy_BZA1jSJKBkTdflONiG80GT80KyqL2J28SCOUmIrF5TXCCxPODHBPENaAD_oTn5xTdo1QcjKlHobgyYAlehfgm6ixY8tR1KR9R1SNZXJjz7e-7CZngj9_VT0Y3DWg8xtceX7Fru5wihsQk1dOUr6W_AMixMtXQQKRYdh50yZ6HmtN1D2N-dS8BNkMQbpXaCZaCQWY3HOJlMZavKtCEEN4ihj1EnbDY2w-v_ZNmibnbSRzzSMjh0AJSKH2ZK3fiDqM7pJEHZZZz9DDxAKyjxMxukAzgqvkR45Nq_DaZy_P-CUZvZPBvdIo2vfpu0bCeQVOgwDFP6XkcKdgvVokUuWLEdP6Fi--0uk51H-7WxuxMQKEylIpAa-F-kNDFj1dUPrHD2-jGVpD7UivCI-W8B4CALw-JELjnqGt07dMFNaYWm7g9-PtfrJ70vO0YiN-HAUEF-OJG9qj2TNl6Qwfs9tSQBl34KO7H1TudnB5HBnLDepYfM1V8Gc_ANeJYxSB1Kqp4YZy5FS4HBYNMaxZxO_hZWGXL_KDR7Hc6bwTADgNZQRXynqImPez6_zSV3DiSPV72uZ_ZALB7y4Aum4xScAHN_wPHlciVsGWCoxCxNoBMDceslvXJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=Kj3HgjAVrlCJpyZVSWbOcEJPILCISP2EiSKJRGHX3Rcii8yLMf_bSkwy_BZA1jSJKBkTdflONiG80GT80KyqL2J28SCOUmIrF5TXCCxPODHBPENaAD_oTn5xTdo1QcjKlHobgyYAlehfgm6ixY8tR1KR9R1SNZXJjz7e-7CZngj9_VT0Y3DWg8xtceX7Fru5wihsQk1dOUr6W_AMixMtXQQKRYdh50yZ6HmtN1D2N-dS8BNkMQbpXaCZaCQWY3HOJlMZavKtCEEN4ihj1EnbDY2w-v_ZNmibnbSRzzSMjh0AJSKH2ZK3fiDqM7pJEHZZZz9DDxAKyjxMxukAzgqvkR45Nq_DaZy_P-CUZvZPBvdIo2vfpu0bCeQVOgwDFP6XkcKdgvVokUuWLEdP6Fi--0uk51H-7WxuxMQKEylIpAa-F-kNDFj1dUPrHD2-jGVpD7UivCI-W8B4CALw-JELjnqGt07dMFNaYWm7g9-PtfrJ70vO0YiN-HAUEF-OJG9qj2TNl6Qwfs9tSQBl34KO7H1TudnB5HBnLDepYfM1V8Gc_ANeJYxSB1Kqp4YZy5FS4HBYNMaxZxO_hZWGXL_KDR7Hc6bwTADgNZQRXynqImPez6_zSV3DiSPV72uZ_ZALB7y4Aum4xScAHN_wPHlciVsGWCoxCxNoBMDceslvXJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده:
جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch:
کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی خودش اونو به آرت نهایی تبدیل کنه
🎯
ادیت موضعی دقیق:
امکان هایلایت و تغییر دادن فقط یک نقطه خاص از عکس، بدون دست‌خوردن بقیه جزئیات تصویر
💡
نکته دسترسی:
تعدادی تمپلیت آماده هم برای تسریع کار اضافه شده و این مدل در حال حاضر به‌صورت عمومی داره برای تمام کاربران فعال میشه؛ حتماً حسابتون رو چک کنید.
🔗
ورود و تست در وب‌سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7687" target="_blank">📅 22:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7686">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⭐️
۶ پلتفرم برای تست رایگان GPT-6 Astra
دسترسی مستقیم و استفاده از API مدل‌های پرچمدار و سنگینی مثل GPT-6 Astra معمولاً هزینه بالایی داره و اگه حواستون نباشه خیلی سریع اعتبارتون رو صفر می‌کنه!
💸
با این حال، یه سری پلتفرم کاربردی وجود دارند که اعتبار (Credit) اولیه یا سهمیه تست رایگان می‌دن تا بدون نیاز به پرداخت، بتونید قدرت این مدل رو توی چت، کدنویسی، پردازش تصویر یا ساخت ایجنت بسنجید:
1⃣
پلتفرم Vercel AI Gateway
یکی از مطمئن‌ترین گزینه‌ها به‌خصوص برای دولوپرها. این سرویس هر ۳۰ روز حدود
۵ دلار کردیت AI رایگان
به کاربرانی که حساب فعال دارند میده. محیط Playground، پشتیبانی از ایجنت‌ها و سازگاری کامل با فرمت OpenAI API داره و برای ادغام با پروژه‌های شخصی عالیه.
2⃣
پلتفرم Brainbase
اگر دنبال کدنویسی پیشرفته، تحلیل ریپوزیتوری و ایجنت‌های خودکار هستید، اینجا فوق‌العاده‌ست. بعد از ثبت‌نام اولیه،
۲۵ دلار کردیت رایگان بدون نیاز به کارت اعتباری
دریافت می‌کنید تا بتونید تسک‌های سنگین برنامه‌نویسی و اتوماسیون رو با مدل پیش ببرید.
3⃣
ابزار Roboflow Playground
بهترین جا برای محک زدن قابلیت‌های بینایی ماشین و پردازش تصویر (Vision). توی این محیط می‌تونید اسکرین‌شات‌ها، نمودارها و تصاویر پیچیده رو بدون نیاز به کلید API آپلود کنید و دقت تحلیل مدل رو با بقیه ابزارها مقایسه کنید.
4⃣
سرویس CometAPI
اگه مدل رو برای اتصال به ربات تلگرام، افزونه یا اپلیکیشن خودتون می‌خواید، این سرویس کار رو راحت کرده. بعد از ثبت‌نام کردیت رایگان میده و چون ساختارش دقیقاً مشابه API استاندارد اوپن‌ای‌آی هست، بدون تغییرات عجیب غریب توی زیرساخت کارتون راه می‌افته.
5⃣
پلتفرم Imaginode
یک فضای همه‌فن‌حریف با محیط تعاملی Canvas، چت، API و ادغام با پروتکل‌های MCP. بدون کارت بانکی کردیت اولیه میده و هر پیام با این مدل حدود ۱۲ کردیت مصرف می‌کنه؛ بنابراین برای ساخت سناریوهای متصل‌کننده متن، تصویر و اتوماسیون حسابی جوابه.
6⃣
سایت Vibany
ساده‌ترین و دم‌دستی‌ترین راه برای تست تفریحی و سریع. در بدو ورود حدود ۳۰۰ کردیت رایگان می‌گیرید و هر بار اجرای مدل حدود ۱۰۰ کردیت کم می‌کنه. یعنی حداقل ۳ الی ۴ تا پرامپت عمیق و جدی می‌تونید بهش بدید تا خروجی رو با مدل‌های قبلی مقایسه کنید.
✈️
@ArchiveTell
|
#AI
#API</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🧠
شیائومی وارد میدان ایجنت‌ها شد؛ معرفی دستیار همه‌کاره MiMo Desktop!
بچه‌ها شیائومی رسماً وارد قلمرو ایجنت‌های سیستمی شده و یه دستیار دسکتاپی معرفی کرده که مثل ترکیب Codex و قابلیت‌های کنترل کامپیوتر Claude عمل می‌کنه؛ این ابزار خوراک خودکارسازی کارهای روزمره شماست.
🖥
کنترل کامل دسکتاپ و وب:
اجرای خودکار تسک‌ها، کلیک، تایپ، کار با فایل‌ها، پر کردن فرم‌ها و امکان ضبط و اجرای مجدد فعالیت‌ها (Record & Replay)
⚡️
پیش‌نمایش تعاملی و ادیت موضعی:
رندر زنده سایت‌ها، گیم‌ها و داشبوردها با قابلیت هایلایت کردن یک بخش و بازنویسیِ انحصاری همان قسمت
🧠
دسترسی رایگان به مدل‌های نسل بعد:
بهره‌مندی تسترها از دو مدل معرفی‌نشده و پرچم‌دار MiMo-X-Pro-Preview و MiMo-X-Flash-Preview
💾
کشینگ فوق‌سریع تا ۹۹٪:
فناوری بهینه‌سازی توکن برای تغییرات مداوم پروژه‌ها جهت جلوگیری از هزینه‌های اضافی
💡
نحوه ثبت‌نام در نسخه بتا:
ظرفیت بتا کاملاً محدوده و اولویت با کاربران فعال اکوسیستم MiMo Open Platform خواهد بود؛ فرم درخواست رو پر کنید تا لینک دسترسی و مدل‌های جدید زودتر براتون فعال بشه.
🔗
فرم ثبت‌نام در نسخه بتا
🔗
صفحه رسمی معرفی
🔗
صفحه رسمی قابلیت ها
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=eU_f9d0kAquGCxqOv-_QY3CmqOqzSKoEofGvjtdXVeF2Dk89Z68xeQmui3Ja8w4Y6kvrshs0MCk_QUkl-LMNELlTmO40TSdKAdSJvcB_lSASMIlEmCZfhgJMDWtitofPM60KbApxgajcd3bUpefu9B0A0GOk75rcSjtXOg_FGwh4HXrFxY8N8YFZAsKClQR7mSKMQ9iAGm0ivAuYC_LkllvH5rGzW-VZL8hBVuM7Lf1sgSneisQwFWd-54TmXjpL338z7F0yzIBhjZjEzjhC0Ct6WfaKAkn3wlEg-WUhUSmLFf90sKlNX7v7aDIHbnkx49JMmxL_yDqQV7mosK9Rab7jdZSlZt_wyCXocxWGEdnsv5Xp_jGG6T8bdCL8WrimhE3tzEV3uoMQrVyJjUaRvJRjOuuNqARLmPlDMTGYLtMAT8OQn2nF6_-DFR7gPRSd7V8UhulrV_Cql8ETwQbyEvQpdRfAXMathBV8ZrGdJrlPEs3IKz3Z2h3Ub2RfnpnvGeQR78fRB2FFhgLdZUTeGMdUU6UnBMBOLCdomt2cZ1JpO05E9wnS1FZq3YBTlxgXX-GtV8O8O_vKfhbgtHpbDb-1fs24UYwpw6IJHq7LaGniERJ0QcjBIBSo5U0U4vZBds4eJQKS114SZvPpl646yekOHvp4P3GTqDeF2_QGSjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=eU_f9d0kAquGCxqOv-_QY3CmqOqzSKoEofGvjtdXVeF2Dk89Z68xeQmui3Ja8w4Y6kvrshs0MCk_QUkl-LMNELlTmO40TSdKAdSJvcB_lSASMIlEmCZfhgJMDWtitofPM60KbApxgajcd3bUpefu9B0A0GOk75rcSjtXOg_FGwh4HXrFxY8N8YFZAsKClQR7mSKMQ9iAGm0ivAuYC_LkllvH5rGzW-VZL8hBVuM7Lf1sgSneisQwFWd-54TmXjpL338z7F0yzIBhjZjEzjhC0Ct6WfaKAkn3wlEg-WUhUSmLFf90sKlNX7v7aDIHbnkx49JMmxL_yDqQV7mosK9Rab7jdZSlZt_wyCXocxWGEdnsv5Xp_jGG6T8bdCL8WrimhE3tzEV3uoMQrVyJjUaRvJRjOuuNqARLmPlDMTGYLtMAT8OQn2nF6_-DFR7gPRSd7V8UhulrV_Cql8ETwQbyEvQpdRfAXMathBV8ZrGdJrlPEs3IKz3Z2h3Ub2RfnpnvGeQR78fRB2FFhgLdZUTeGMdUU6UnBMBOLCdomt2cZ1JpO05E9wnS1FZq3YBTlxgXX-GtV8O8O_vKfhbgtHpbDb-1fs24UYwpw6IJHq7LaGniERJ0QcjBIBSo5U0U4vZBds4eJQKS114SZvPpl646yekOHvp4P3GTqDeF2_QGSjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آرشیو ۱۵۰ پرامپت آماده برای خلق ویدیوهای سینمایی با AI!
بچه‌ها اگه با هوش مصنوعی ویدیو می‌سازید ولی خروجی‌ها تخت و مصنوعی میشن، این کالکشن خفن خوراکتونه. یه دیتابیس آماده از ۱۵۰ پرامپت تست‌شده که دقیقاً دستور زبان کارگردانی و سینمایی رو به مدل تزریق می‌کنه.
🎥
کنترل دقیق نور و دوربین:
پرامپت‌های تخصصی برای مدیریت لنز، زوایای حرکت دوربین، نورپردازی و دکوپاژ
🎞
همراه با نمونه ویدیویی:
هر دستور شامل پیش‌نمایش رندر واقعی است تا قبل از خرج توکن، خروجی کار رو ببینید
🎭
تنوع ژانر و اتمسفر:
پوشش کامل انواع سبک‌ها، سناریوها، اکت کاراکترها و فضاسازی‌های سینمایی
💡
نکته استفاده:
تمام پرامپت‌ها آماده Copy/Paste هستند؛ فقط کافیه کپی‌شون کنید داخل ابزارهایی مثل Runway ،Kling یا Luma و المان‌ها یا کاراکتر مدنظرتون رو با کلمات کلیدی دلخواه جایگزین کنید.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh5imGRsAUMsf2sgW6Wl6-lpWY4_R8w1EPKkCiwVVXpb2ue6Ez_42Es60sDb1_nPEjSCVoTmTuzFFjAx0-6xUrqGHz7xNzDOpNV8F0VL7WK7EK34GPpDPqV9My_5BatODHj2iaSMUtKN3oETtJVz_pb2-lmsG7WjTzbWGvrH7kd6SqISQxQgeJM_J4vWra0kOqivmeNwlR4_iFqi2iKemA5YwWN__KNjoWG48dWNyCuclpJ5M9uCxE17NJrjKPMZYCuo3p2Gdd_lh_UF3NKww2xRsUe2VANMGgHvrVYjWO_eOtplwh9G6bYymo6jfVNHcrmoa-GDHgWdMLkDmfnYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مایکروسافت آفیس رسماً مرخص شد؛ معرفی غول اوپن‌سورس GenOffice!
بچه‌ها اگه از خرید لایسنس آفیس یا برنامه‌های سنگین خسته شدید، این پروژه جدید خوراکتونه. یک جایگزین کاملاً رایگان و متن‌باز برای مایکروسافت آفیس که ایجنت‌های هوش مصنوعی رو مستقیماً آورده داخل اسناد، جداول و ارائه‌هاتون.
📝
پکیج کامل و همه‌کاره:
مدیریت بی‌دردسر داکیومنت‌ها، شیت‌های آماری، ساخت اسلاید و کار با PDF بدون نیاز به ابزارهای متفرقه
🤖
ایجنت‌های تحلیل‌گر:
اتصال مستقیم به مدل‌های قدرتمندی مثل DeepSeek ،Claude و Kimi برای تحلیل داده، نگارش متن و تولید محتوا
💻
آزاد و مولتی‌پلتفرم:
پشتیبانی رسمی و نیتیو از مک، ویندوز و لینوکس بدون نیاز به پرداخت حتی یک ریال
💡
نکته جالب توسعه:
جالبه بدونید نسخه اولیه این پروژه رو فقط یک مهندس، توی مدت یک هفته و با سوزوندن ۱۰ هزار دلار توکن هوش مصنوعی جمع کرده! ریپو تازه پابلیک شده و سرعت استقبال ازش وحشتناک بالاست.
🔗
گیت‌هاب GenOffice
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7683" target="_blank">📅 14:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7682">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=OCX7vWPV2mXO8Wq_nkfafVdbnuTCpLJlDYzIgVUAhSQFqtd-B0wttLCENSzJmykrd_QliHfBll78Dmg7BBDekrdSary4qJLDL94LhZymMwKGKmFUYR3wUIJo_HsoMwJ0seENrChhFfJzlgoY84NwHgJhd2AyjJTEh0BPhWmVej6xTZysDlfBQTgr2V81XQN99xf19KOxosckbIKn56_GVJkO0hplchNauO9MGLkf_JCmz7xwge0WNaNewRUdkSpMPHC-Ew3qAYEqy4oTEqiL_aIfR_Rc7OGBck9ccwWnQjcmb_1coYyzeqcu2e5xy5FzsCom8PTFc0bvwITefadiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=OCX7vWPV2mXO8Wq_nkfafVdbnuTCpLJlDYzIgVUAhSQFqtd-B0wttLCENSzJmykrd_QliHfBll78Dmg7BBDekrdSary4qJLDL94LhZymMwKGKmFUYR3wUIJo_HsoMwJ0seENrChhFfJzlgoY84NwHgJhd2AyjJTEh0BPhWmVej6xTZysDlfBQTgr2V81XQN99xf19KOxosckbIKn56_GVJkO0hplchNauO9MGLkf_JCmz7xwge0WNaNewRUdkSpMPHC-Ew3qAYEqy4oTEqiL_aIfR_Rc7OGBck9ccwWnQjcmb_1coYyzeqcu2e5xy5FzsCom8PTFc0bvwITefadiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خفن: تبدیل هوش مصنوعی Astra به یک بات بازی‌ساز حرفه‌ای!
🎮
🔥
داستان از این قراره که یه دولوپر، Astra رو طوری شخصی‌سازی کرده که عملاً تبدیل شده به یه ماشین بازی‌سازی. اصلاً هم شوخی یا بازی‌های دوبعدی و پیکسلی دم‌دستی نیست؛ کیفیت کار در حدیه که باورتون نمیشه کل این دموی سه‌بعدی خفن فقط توی
یک ساعت
جمع شده!
👀
⏱
سازوکارش چطوریه؟
🛠
همه‌چیز با یه اسکیل (Skill) جلو میره:
* اول Astra باهاتون گپ می‌زنه و از بین ایده‌هاتون، کانسپت اون بازی رویایی که تو ذهنتونه رو درمیاره.
* بعد طبق همون پلن، توی ده‌ها دور آزمون و خطا پروژه رو قدم‌به‌قدم کدنویسی می‌کنه و می‌سازه.
پرامپت استفاده‌شده برای ساخت این دمو:
📝
Prompt (high effort): /dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
🔗
دموی بازی توی مرورگر
🔗
خود اسکیل Astra
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7682" target="_blank">📅 14:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7681">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKF2B-teWCXyLE1LB1D2_AIgONZstUzFO5oC604N9bScTTqnD2gzhuN98T7k0vd5JQ8A65-kSJq7_b02wLHP8ulPqmE12XcfHXcvsbSjRXfEf4sDy8SQgcyFBGj0a2bKjLEvf34qkxcLEVfZrvfa_95JyNnhiK8EqiiMpB02Libmi9kaj4SvjXTO9Mz4HAfdzjF197UDXuahdPS-vuoHOm8wSuB-EKEsHIQgIRYkGuo2eG2bEnu2-JQMWANzbupn__HbvxOU-3vRGrPF7lVRfFv9r1jndRYHzX0z8eLZAuVLLf-8QqRlLvuXbRE9Y7XPZhIy1E7qJbQzuBKbddqe0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
باز کردن بی‌دردسر فایل‌های آفیس روی اندروید با OpenDocument!
بچه‌ها اگه فایل‌های متنی یا اداری دارید و دوست ندارید برای باز کردنشون تو سرورهای ابری آپلود بشن، این اپ خوراکتونه. تمام اسناد OpenOffice و LibreOffice رو کاملاً آفلاین، سریع و بدون نیاز به اکانت باز می‌کنه.
📁
پشتیبانی کامل از فرمت‌ها:
خواندن بی‌نقص ODT ،ODS ،ODP در کنار فایل‌های رایج DOCX ،XLSX ،PPTX و حتی PDF
🔒
حریم خصوصی واقعی:
پردازش کاملاً لوکال، بدون اتصال به اینترنت، بدون ترکرهای تبلیغاتی و بدون نیاز به ثبت‌نام
⚡️
سبک، امن و باسابقه:
یکی از قدیمی‌ترین و پایدارترین پروژه‌های متن‌باز اندروید (فعال از سال ۲۰۱۰)
💡
نکته کاربردی:
بهترین گزینه برای کسایی که با فایل‌های کاری و اسناد حساس سر و کار دارند؛ با خیال راحت می‌تونید حتی در حالت Airplane Mode به تمام داکیومنت‌هاتون دسترسی داشته باشید.
🔗
گیت‌هاب پروژه
🔗
وب‌سایت رسمی
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7681" target="_blank">📅 13:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7680">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=h0IplmRf3Etr1x9pykPKW5dR30VdrHkuaXV3ohWx2L-7-ut5dC4o9JbQIZJaBG2T5mw49orLY8FAPrJv9b1GsdXndjye-RYYZyX6rY_XjQ9t9uVQ0Aj8LNeOfMdymWth5q_CrVrrmlJzEo3pdqoLM5r_zqhnQPvODSRDxHopgAU1fGsCrEGxJL9EKc9so7r_-tVMHe2wWdC-lE0jh2T0-M0GnhlIUqYnE-M4ljFzjaoMwOQJOeQCgwU_DRmh4a4KeKrR-wSqWtxRKLqXItNfNHRw7fookTefWQsjVS_iKzI--qHygrc-awquylIoYBbRyPVy92BaA1vkJKFS2T8vDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=h0IplmRf3Etr1x9pykPKW5dR30VdrHkuaXV3ohWx2L-7-ut5dC4o9JbQIZJaBG2T5mw49orLY8FAPrJv9b1GsdXndjye-RYYZyX6rY_XjQ9t9uVQ0Aj8LNeOfMdymWth5q_CrVrrmlJzEo3pdqoLM5r_zqhnQPvODSRDxHopgAU1fGsCrEGxJL9EKc9so7r_-tVMHe2wWdC-lE0jh2T0-M0GnhlIUqYnE-M4ljFzjaoMwOQJOeQCgwU_DRmh4a4KeKrR-wSqWtxRKLqXItNfNHRw7fookTefWQsjVS_iKzI--qHygrc-awquylIoYBbRyPVy92BaA1vkJKFS2T8vDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📍
با GeoSpy لوکیشن دقیق هر عکسی رو دربیار!
بچه‌ها اگه دنبال لوکیشن یه عکس رندومید یا اهل چالش‌های OSINT و ژئوگسرید، این هوش مصنوعی خوراکتونه. حتی اگه متادیتا (EXIF) پاک شده باشه، از روی خط‌کشی خیابون، گیاهان، معماری و تیر چراغ‌برق مختصات رو براتون پیدا می‌کنه.
🌎
جست‌وجوی جهانی (Global):
پیدا کردن چند تا از محتمل‌ترین کشورهای دنیا حتی از روی اسکرین‌شات یا عکس کراپ‌شده
🏙
مود شهری (City Search):
اگه شهر مشخص باشه، با عکس‌های خیابانی مچ می‌کنه و آدرس دقیق پلاک و خیابون رو میده
📸
تحلیل چند زاویه‌ای:
امکان آپلود تا ۴ عکس از یک لوکیشن برای بالا بردن نجومیِ دقتِ حدس
💡
نکته طلایی:
کیفیت عکس اصلاً مهم نیست؛ این ابزار حتی فرم شاخه درختا یا مدل آسفالت رو می‌فهمه! موقع ثبت‌نام اولیه هم یه سهمیه سرچ رایگان بهتون میده تا تستش کنید.
🔗
وب‌سایت ابزار
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C88lxz1ECiSahz1t83RyygwJcJc0zyvBtgFBrPfcGSBL0O695odqW-RlLG2jQEf05i2LrTnhHev-8GYx-0JfHspJqofeFI3dfD0YcHs0BJIji6IeAzXGO7OIvZ9NVFnr0O8_Udb5hu-BQMyQfWxlCYjbfP6fIorH9SQJU8LDs3r--pmJbK6K5Ivv0bDHhRfcqGULAccGneSPgIMKOIdgzdkU-WADdfjUTa0OCzAc6FSSIbUrIwKx_KkzyKVXztKSHEZrSKOh1tExg6H3IFPaG9K_Ic5rZ01Kfp74PvyJbukO10CBCJO-S_n04pClRD_FpfCg7macI21HK0OiFwpdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕸
با SpiderFoot ردپای دیجیتال هر چیزی رو توی اینترنت بیرون بکش!
بچه‌ها اگه تو حوزه امنیت، تست نفوذ یا اوسیانت (OSINT) کار می‌کنید، این ابزار دقیقاً خوراکتونه. اسپایدرفوت یه ابزار متن‌باز و بی‌رحمه که کل سطح وب رو شخم می‌زنه تا تمام ردپاهای دیجیتال و آسیب‌پذیری‌های یک هدف رو دربیاره.
🎯
تارگت‌های همه‌جانبه:
جست‌وجو بر اساس شماره تلفن، ایمیل، آیدی توییتر و تلگرام، نام، IP و دامنه‌ها
🤖
اسکن تمام‌خودکار:
جمع‌آوری آنی داده‌ها از بیش از ۱۰۰ منبع اطلاعاتی بدون نیاز به سرچ دستی
📊
نقشه ارتباطات بصری:
تحلیل داده‌ها و نمایش گراف‌های دیداری از اطلاعات لو رفته و پیوندهای مخفی
💡
نکته و اجرای سریع:
راحت‌ترین راه اجرا با داکره؛ کافیه دستور docker run -p 5001:5001 spiderfoot رو بزنید و پنل تحت وب رو باز کنید. (یادتون نره، فقط تست امنیتی قانونی و اهداف آموزشی!)
🔗
گیت‌هاب پروژه
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7678">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4lftfdPjFNRKOjFkKC1k4MXuWbpAR6e092x9DlTaF0ZqEaiWJy1qET83OKuWtRhpBumCggefGui1dczNR-0DUb4O0CEozBQSnQrtQrDWdYU6V6s-euTJBKM7Vbcf8ktp6lLyIGy1jshvS6jsuXapTv2ysSqpNXS-GOCf73wfvygyL_3vq99PVIP5hQaI_ggmqFHYW2zem2omPb7B2-VpemPRCCFW8vY3wJsD1yK2zD8HdDoj6vQYNJDNJG9hnAIGMmPmv47gTRxlJVcj7duAuvjMKaSdLJ3t_ytaKXX8Zu-Swqc6Xtis3kqqvUGJpi2m6Ul_kR9UlIpKbJ4Dgkm2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توکن‌های نامحدود برای Claude Code با شاهکار مهندسان اسپاتیفای!
🚀
🧠
پلتفرم
Portal
مثل یک مدیر هوشمند عمل می‌کنه و با واگذاری وظایف ساده به مدل‌های ارزان‌تر، تا ۹۰٪ در مصرف منابع و توکن‌های هوش مصنوعی شما صرفه‌جویی می‌کنه!
🔥
🔺
تندخوانی با Gemini (bulk-reader):
فایل‌های حجیم و چند هزار خطی توسط Gemini 2.5 Flash آنالیز شده و فقط یه خلاصه مفید به Claude تحویل داده میشه.
🔺
کدنویس روتین (code-writer):
تولید کدهای استاندارد، تست‌ها و تنظیمات خسته‌کننده به مدل‌های کم‌هزینه سپرده میشه.
🔺
تمرکز روی کارهای حیاتی:
با این روش، Claude فقط درگیر کارهای پیچیده و استدلالی (مثل رفع باگ و طراحی معماری) میشه.
💡
در
نتیجه:
یک ترکیب هوشمندانه از چند مدل AI که باعث میشه هزینه‌های شما ۹۰ درصد کاهش پیدا کنه و خیالتون از بابت محدودیت توکن‌ها راحت باشه!
🔗
لینک دسترسی و پروژه
✈️
@ArchiveTell
|
#TOOLS
#AI</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7678" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

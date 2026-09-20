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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-7803">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRSC-DhaEVeD60kgbs1yIIvUByCA9IqoxTP-VeefAwFAUyqGSqwzq1XqRsMOWeL8hUWf-KCy6gxLPchOS9gvHCCJzeY7ns5PNcj5UQtKLKmyMBhsn4RbcbT11Mvc2A0nu7FcVN_P2cq6hNKl0U06yrysR0ddaF7VbuYmVpDoE9QTJjcuPV-8ffXeK_VHBIP5SFprduJmbs1KqtaDSL1P3h5Wg1OhXaHFimYu-O-0q2HfXAKZ_topIIKGrCV60Rh-N2-dmyTtpc1BtPLvxz6uctfgNtERUnb-s2P7OiDF80Dkfb6SHTrbAAPwCgU8K7-RXX6UoZQXEC8a25a7s64hEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج طلایی API هوش مصنوعی | قسمت اول
🤖
سایت‌هایی که برای ثبت‌نام اعتبار هدیه می‌دن!
بچه‌ها یه لیست پر و پیمون از سرویس‌های ارائه‌دهنده API آماده کردم که بهتون اعتبار تستی می‌دن؛ خوراک استفاده توی کلاینت‌های مختلف برای دسترسی بی‌دردسر به مدل‌های پولی!
🔥
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
سایت Modeloc
👑
└ خفن‌ترین گزینه لیست؛ همون اول
۱۰ دلار
اعتبار تستی می‌ده!
2️⃣
سایت AAAwinn
└
۱ دلار
اعتبار هدیه ثبت‌نام
🤒
اکانت گیت‌هابتون باید بالای ۹۰ روز عمر داشته باشه.
3️⃣
سایت Jucodex
└
۱ دلار
اعتبار هدیه ثبت‌نام
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
👀
قسمت دوم به‌زودی...
سایت‌هایی که مدل‌های
کاملاً رایگان
دارن و
هر روز
بهتون اعتبار می‌دن
🔜
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/ArchiveTell/7803" target="_blank">📅 13:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7802">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7800">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7800" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSKLzDbGZadirfB1m8jkUmRT_jeN8GyjBI0sqiJ2b1G8JHtv7n588rhbsrkJK4HPUuNuRsEAHbyj2ZfKHOvoMMjB5yMpe7rO3vy4C-Eec-WL5zoJSStH_APh81HK5vswxNMt45JwPHt_jJK10RcF-fyY2uvZi2dRMLFjHPlxZrjNWfwnw5mmFdOKFrJdCrMtn6drRn3qei9j-mYTWGWGne09HtASrSax32nbRrLI5QwbxYv2Z9j5UgzN1Tdc_rQNd2fpyeBWi3XHplLQUjFQoE85FcBdn-6TaZRzaU0O3mtTnaDCs29aprmxI_KXGWLuSmROdgR98JofDH1bklrQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNKHIp4MMqpfytigYsO6blb2dVkqUNOugNwyz4I8z4_EPMpSIiz53iQfuoSniHpXJ2zRRrxBQ9WKdcQay1DARqm1XX6U9-ritiKBSOnRp91vgVltHzwdDDTkB8m1yLLJ9dr5g3Wr4aQOMwJROOhHHHZBBZCkWzSqQzv6xZ1b2qjvz2xMLIW987vJjhfiMin91tmnaX4Ni8S_5u2dl44UNc_FyiC-6Cc5nivWIeVbOYJL79ezJRM2GP5Dn9POdbP2MoYMalGZZq3NDN_DbRoZxJdXBoyVRVt7yGdZJ741II1EpFzFNgD_df18ONB2CafSJ4RSAVCQb8F_eT-VlcyWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcsoYAWVhNbkjhapusaZiVQEIuZTQcDKzT6eA1KZcPbzAAOQebGOfI6E8QDukpeHPWFiKTkIqae7efUVbIQtzqXj55rrclB8zTyXrt7lW2m94pPhuKSO4_1m1HtBdG6S_Puwp27RF8ZqXVVfTQbklPHh9WbBnPjFsPJBo_ukUU_YmNeGlhyeO1HYpD5_U2nHc3yM0CZkm-HMsLXMtKJauCgR41ENLndwqr9oL225E0YMUCubvYBo6RLmjU7Tgjp0fd1YgVQDYOPDz5vSfweLlcrID1CqoM1eMCwNZc8rnb2-EH8aQPLX78M9IhjUye5hRYJhTwv--Y5Idy3ovFWfjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7796" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7795">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhKCeCcYLAtQm0lQ49bgKTVLo24c4hZZ3MPrN7dM4LqRtcqZ-Clalskx2iQN9lGpo1ZuC12TgUIHJfoictulikHBE_MiQRFkZTwgm-jttbYEf41JfmzwFb5iWSL_8_SMxKGWaXl7nncxHh_VN6ff_dGM3dVyuQbewhkhLxn0A0JYtSedMy7rsI-ssQxYw0eDN88WGDtHibkB5gpVCzhcWRgivTmAeeI_RT87lIr6P6w48vb2l71A3wGw7si8j-KtPCs2fKoCrgi0ly5q1okCYClQeKuHsMXzsAUvdaT5m7p7hn9xfbEjc8Onpmq1XmgzRn10YPH9_Z5Ri3cC_S7vCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
مقایسه‌ی تصویری GPT-6 Astra Max در برابر Claude Fable 5.1 Max در تست کدنویسی Code Arena
به طور خلاصه: Astra در انجام وظایف تحلیلی، محصولی و محتوایی عملکرد بهتری دارد. Fable 5.1 در جنبه‌های بصری و تعاملی عملکرد خوبی دارد.
در حال حاضر، GPT-6 Astra Max در مجموع، رتبه اول را دارد. می‌توانید جدول رتبه‌بندی کامل را از طریق
این لینک
مشاهده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7795" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5NKwLgxDjcrbpxZl16w9_WqqENXjJ9yipFilLNzqWmoTXZ5Lyt-grzYyLnp6cAkMhWVcZFzbKFAggjMLZG7PKrb1Cn_IPDBwCkw0qNVN8dfLbgt0MckFPAk0DTWYFE_eO9cLXSbPd_3QYXXtdlAC4qMuEj1w4K8eCdEviZ7Nt3vDzt1vomgSSpSy3JNIng04l_Xy9k6QOvWCf6WV_-6sl85te1pXRC8V9XcuTvddF0uvUW0VNcomWLhD-3LwtTIk5ohFnQ1j2CJV1a7PA_ObVvMkngL86obG7kQP9n7QEwvJ_tX2TImh3q3Cb27m1ymymNYiyZnYseNssIDNTUhDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7794" target="_blank">📅 15:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6VhSPQE91Q3iMaMfXfYVI0jbRCdTJp_XFa6_sSosKS7Q6Jh6EDLwITXU96VJLRxiAAngU4TsyNIiEmr50tVcqHyZPEtaFrmsEk9Sr-tWHcbbDJrahOKm9v4NcgsAycfLDiaQQ1iCJ4yCqiDg3qQZwI2Lwp9asxOmPBTEElrX8pnTxT1cd1svw53olFq4LbrAyvZYD85xnoShgjdnY13-4OS0db1Bn2SQoMf-4m_bHV5lGMq4XQNAplBBxshCitfumH4R7rot4KviCM-N8qKDiH5qJM6Pp8dPifSU9DAGRy7OIjzbfsJOCZgVPHgQNUReJG7rlH4h6byXIokt4N_lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7793" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7792">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7792" target="_blank">📅 13:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7789">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7789" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7788">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7788" target="_blank">📅 11:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7787">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7787" target="_blank">📅 11:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7786">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♊️
جمینای گوگل سه شرکت واقعی را هک کرد !!!
جمینای در جریان تست امنیتی ماه مه ۲۰۲۶ به‌ صورت ناخواسته به اینترنت دسترسی پیدا می‌کند و شرکت خیالی مورد نظر خود را با شرکت‌های واقعی هم‌ نام اشتباه گرفته و با استفاده از اطلاعات ورود لو‌ رفته در سراسر اینترنت وارد سیستم‌ آن‌ها شده و نفوذ می‌کند،  پس از پی بردن به واقعی بودن شرکت‌ها، خود به خود عملیات نفوذ را متوقف می‌کند.
گوگل اعلام کرده هیچ آسیبی به این شرکت‌ها وارد نشده است
✅
منبع
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7786" target="_blank">📅 09:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7785">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7785" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7784">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7784" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7782">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTgUh3qdteVsPAdnepkH4Tl6kdV3YcT1Ss6wpcPk2Dkk6NlxN43_wQJQdsYhYQ7PQ9HhwBYi_2CTQaWHXdVD9dSPU2JcbTBn7Aq1GiDwdDnbpcZTmWRRrZ3ObtiRIotMpQMgaMLFH9UmzLBXcnh_3TRTUorEyYiyQROLuSTvEfmCSunhDhW8-5H7s5ZQF2Ke9TWdvtKOQak-D2f7t-cWaGvI3e4nyZztWDTKskF2j9ffbx8d3nAIhOjWFZ53N_ybAc5hyFvi7vrvOiyh23y0CGOisf0rXR-8JdX1Z1JaiIZhXAoKSdVBCVH2gSEl56l-In-ZpajdbC8ni4L8MXz9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gemini 4 pro is out now
💪
😎
گوگل بالاخره پر قدرت به بازی برگشت
تست کنین نظرتونو تو کامنتا بگین
(این پست طنز میباشد)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7782" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7781">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7781" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7780">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7780" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7779">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7779" target="_blank">📅 17:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7778">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlOnRZ9sTfMhv63vubjQqCdNlDfwVgPWuA50HNo19ifllcsNXbY6pUtgnlh2uuDEWDxJC_fvCZw6Z7RlyI7lGaBsdo-z4qV-H95mQmKQMbYLJ_Fwg1EXLP4Dx6T68ErIfrBKnmsz4bC75Jqz4FYmxL3SNoYoBFIrHbzMMSr-1YVsQK_OnsF16tEpwRCQheKm0w70RalKQ9BuSIvqsvE65c0HdAPUWybb0NZu-gZ1d3i-UjxYAfeGaQmheRwJzHzrtNkfqjlq8irPF1Ww_oogvqzO80XBYvtGuHHJ3DTKQGmjftA6I5FnS9xvrcKZOHHSB2J0nPttWsuD14PdvN1aCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7778" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7777">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pUvwYLDuOIpiC7nXFVE4Ug1r0J_mql2QnHUomG5QaSRtenoNImNlcg-t1o7KUv4UdajIzTzYqgMnOjO_UOqoH8YvJ20-3E-TidKt7aORnHJuhRx9bCgXpsL_zvzV4C8v7LKOfTYo-BIh2-TGRDi2InEDuJadlstTrELy5b8Dns2RR60fiV_So1Sar2KQpXYxy-olyJM2zFvukpFcIeOV4YiGPlghbxWAoRawhNn82lSP64ZigPSko-f8a-WnoxKcx1BZn0djSLbDE1eHLbDEDhENVoNf7JDlwbjO8zVO3YhfqQ5IUNgNNZovKmAsnUNxno4Yk06quoRgMBhI8I0F5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
یک میلیون توکن رایگان GLM 5.3 Flash
برای دریافت
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7777" target="_blank">📅 17:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7776">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Je7rGv1p3Rwv1FIKdggLQPhJ_PsyHLP0-Q7pjvEVIUQ6eXSt9KOdQPaQ-OaQKPImafBYLvEZbn5uYenGa_MZZbEXunSwaFB4wiVHKZYDbAzcGS0SzSB-YoCJh9OihUJ8ugf0BxyWZNVjQC35z-rLFNuxXzQ7KFN7LNCiE_Wmt-N-IAczCkKjeNG8WntYVRZ6KwnlUP3Lfa1HOCQr6gMHLwvgdhqKmMIAYhO4sfvBZyc1XPacSNvVl0oBueIbz1YiALu4OY2g_xfaFSAMjmSzg9Ga-L6M2cE9qDA6lhJUtMR5n31XaQHJWUKpZ4DyV3Yp4rQPnuql5zTplnx0nzss6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7776" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7775">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf48d-W8YEH4u0U4S1ZjxBTn8RRnOB3ORzC-yPPu_FjOi-psZuXkYGn6Ir-P5vzYWxhPx_t_uj7tObnFGKLuQWdLSINoiPMxrOTJqq8vDrWp7iwLQ8ulI9NhTMrLiW6TMfg8QG1fe9NByF2DhiFFV6Iq3Lw8BubgiAre7dOjjzg8oQJ2hLO9kFrPvXkDpK2Pfcg2yu10A4MKawEggtOL6CIyJZDLIKph-tooHTOw6FFT1cM9_hNiCCYj_mPlXRe-aTv2Wd8Fgj-F9m7x5bbfdlpPoXL7snoa7wmmUoKBoWqU4EkaupaxGCN75PoO4fRUKdLoiufRGrXeAIMz-TQ0Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7775" target="_blank">📅 13:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7774">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6370f25b3.mp4?token=UjZ3oMFwQiJAphd7lUSeRaeEiH3CHA5TdELMAuMLxGtgqBvwYVTtmYNEwioJexMtSb0MFRAEKFRTYjWtrEHAiPYAuu_YS1nIi4fFLdDEwNm5oV_zqCezkbtzZ80c5dZl4VuRlVmlB4DalkryonaF-nJ1y0F8huKtVGRv4cuPONmzqpWKQyWzi77cWbl9IAHEl6VwEohBaB1WiqbyLctd3_wzqI9z6P7_81uhvax0RjqOXxKriR5CsvunkQ_XrkRwM4tdhtnvj2GA-OI7Mmj_xtrb1KHpnCO66WY2Au18L06obl4600rKMESkEk7t0iuBQkVT-E710dp0wanOmwInFUhL5O4MfFLQbI_jNfKS173Va8KeS5KgSVespnZVznpIM33H1pYVKWl4Y0gTZlTcHuU8XjlFQ0KxtYCRwY6np-EbuoX4whQVAVTzJnJcX5oY003n1s7-f2TgZs97BQGybAAfKk2nu3FVVskCRQ5I51cD-GgW7_znYtYJXewpvrj47y8RVTaJWm7aJSIUjrymoiAsZNhOTuYr1rsIS2tpTzkUYQTSSgLdgBLrqwF9M3ddhnY4tc_QYsOX0m67QuJtR9AzI_o6XCAVWT2IIU4GHsjoOJTOIWbHV85Zx6rdkQTb7WCOS8u1v6BHZ4VNPtnRElBqOzp20oBwyLgKMH5dN-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6370f25b3.mp4?token=UjZ3oMFwQiJAphd7lUSeRaeEiH3CHA5TdELMAuMLxGtgqBvwYVTtmYNEwioJexMtSb0MFRAEKFRTYjWtrEHAiPYAuu_YS1nIi4fFLdDEwNm5oV_zqCezkbtzZ80c5dZl4VuRlVmlB4DalkryonaF-nJ1y0F8huKtVGRv4cuPONmzqpWKQyWzi77cWbl9IAHEl6VwEohBaB1WiqbyLctd3_wzqI9z6P7_81uhvax0RjqOXxKriR5CsvunkQ_XrkRwM4tdhtnvj2GA-OI7Mmj_xtrb1KHpnCO66WY2Au18L06obl4600rKMESkEk7t0iuBQkVT-E710dp0wanOmwInFUhL5O4MfFLQbI_jNfKS173Va8KeS5KgSVespnZVznpIM33H1pYVKWl4Y0gTZlTcHuU8XjlFQ0KxtYCRwY6np-EbuoX4whQVAVTzJnJcX5oY003n1s7-f2TgZs97BQGybAAfKk2nu3FVVskCRQ5I51cD-GgW7_znYtYJXewpvrj47y8RVTaJWm7aJSIUjrymoiAsZNhOTuYr1rsIS2tpTzkUYQTSSgLdgBLrqwF9M3ddhnY4tc_QYsOX0m67QuJtR9AzI_o6XCAVWT2IIU4GHsjoOJTOIWbHV85Zx6rdkQTb7WCOS8u1v6BHZ4VNPtnRElBqOzp20oBwyLgKMH5dN-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7774" target="_blank">📅 11:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7769">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XhuXnIMC1hzZ8ewALh3sG2tSPicithJDt6bT4br9srGmLViA-c9aasUMxqG08zE8aOkBDqEqRPwrT84wes1Ejf46LUNjO5Kwv_9R_bcPgkJeAbv3zn1bkth364vvO5m6TvgrHQ7XAk9-zrEfZkdRGNyix7HbrGO-_TQn6GGUYy11XwWvd0IMQQ8TA2urtIK1P6fMeeCXVloFkNxK8DRpcEodmVA_1s-gC-I2alKMtUoHc2aheeOQaSAhr8XB217eVKJJ92hNHAy3n19Dyr6aKLBbHYFtyEd_cd_7RtAakkiwxq1XlHqBQ6YyU9lEgFTnZE79jtPIURibxbmc3TTqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gv86nzW_oyytm6GWMduIavbPYqludhQUU1jQ2UsQyxERK3Lvpq7MLdAhKXEWUq5YXFMqAzC6g7nPwO_nydU5fWLDyuCKPbdxvJZ6zSvq_DhTuFBjSxT4o7f03v_7Hm5oA2Q1EuHxuewZGEE5Cb7IWXSHvgzYf438dBZM-PSoxvR16snpDbWVedg-TnxgswkJq9vn24MBFShpzXymeF4su_0NZv6j8yk2PEq-NYKVFT9UwgyZG92oS2SK9_a-oxj8iYtrGAW4qURWsxwR2Nrv60iPFk4-RcwhWZcq1Es3fBwDFx0veAIDqgTleFpvUSwIkAaCkvMKN6LXLSsMKnmWug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zl7u6PZ1uqcgN_H4069gI3opnFG4xEcbFRoKjTVOhhN2yaT3IR1Keyb5_SoE1MaRPcc2JEHVKP9W-gvD2cyYwUVFpHMjHrGTd9fN0L7QzHQrDaJKRR84L96TLMrreB9aU43g-ScfflrO8vkQfMPSP2DHnmh9E0oIN2OKusT_9--6a9zZQcQCQK4YK3k4l9Fyu4Lk_Wb7tlcvxPyWEb7yP8Bn33aRgF3v-VPcKCHpiKecGgZmc1uVN9pPUam7WchOJuLlytvYl-lXQUvKMg77cy_ysTnvwzuQf6w_61zxOrm1E6skZAsI_6utUDK_RFK8F1bXc3jjTkgK8nTDXOCdww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=HueCzLvEZEZ2jDi1GOjq79UZivxnti5R0ixPoQ_w28-L_GI22tSS1Ad5MmsgfdE7secf7KkG-zRf0Xe6jfbHBZGe97aDXqo4krGZ1sIHhjesgJZ7My7dmEZVlv8OhhwHY0h0hjWnhI-uhLnaNhkdcH2jYtf2k4r9097t6UYbzNYMSTEIEl6C9uLwNSIdEnkLj6cgT0nzqp0PnD_zpKMORSydE4YlwEyzNROYfwKPD1m750_TVmKy-EzCOuXptqBLcAebe9cD3HO57QCS1pBNSKJjk5JqWI9bhdC8Gt9FMPRKkpKb9YjkolUb0AR6MFbD5kh7hr97ERk9LtVoGrnu_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3248c435c.mp4?token=HueCzLvEZEZ2jDi1GOjq79UZivxnti5R0ixPoQ_w28-L_GI22tSS1Ad5MmsgfdE7secf7KkG-zRf0Xe6jfbHBZGe97aDXqo4krGZ1sIHhjesgJZ7My7dmEZVlv8OhhwHY0h0hjWnhI-uhLnaNhkdcH2jYtf2k4r9097t6UYbzNYMSTEIEl6C9uLwNSIdEnkLj6cgT0nzqp0PnD_zpKMORSydE4YlwEyzNROYfwKPD1m750_TVmKy-EzCOuXptqBLcAebe9cD3HO57QCS1pBNSKJjk5JqWI9bhdC8Gt9FMPRKkpKb9YjkolUb0AR6MFbD5kh7hr97ERk9LtVoGrnu_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7769" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7768">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه مدل جدید و قوی برای کدنویسی اومد و فعلاً رایگانه
🔥
‏Union Alpha امروز روی OpenRouter و OpenCode در دسترس قرار گرفت
✨
‏چیزایی که داره:  ‏
✅
Context ۲۶۲ هزار توکنی (تقریباً کل یه پروژه‌ی بزرگ رو یکجا می‌تونی بدی)  ‏
✅
پشتیبانی از تصویر (اسکرین‌شات و دیاگرام…</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7768" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7767">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWf_yaaw2NKNJF1NcUfEpfkGGQa9cpfhURGlpN7zSxW0K2qcGmrSD1xqchc1QDdW8jpoSo0fWoKMGs8juqlomJpJGyHei60nkOYH81aIN6hFg0WAeGea7xfFnmlG4xMjrdIm7eXOQhKq0nbXY0L4MDZk9ZSkQfB65Qj6Dnac18WPjn2lgj3-NHKT76DGFB5cSq4VgQbSXnomw4fbul16wE6Jp4MNRv6c-ZL9OZ9IBv_mge18uZHSSfOIeVTCS3XbIDNMWE_rJnNP-wU9gxkM0hSMSaIUbW8y-DUTlttBehlTb_ych7kUiZV_IiP-K2V7Gn19gh7mE-1voqINqpGSww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7767" target="_blank">📅 21:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7766">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7766" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7765">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7765" target="_blank">📅 18:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7764">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ql9YInHHZrTTUABxT8cedBwR-Bj3MNffX_2UEWE-u8-70CnhgH7ypD39-C8O2Q01n_fVMdyzu5ddOptUkWuMRhwCE_pkWvmPcIIy4EmfQ1qabd7w9OXTWOweQJ8exx6rg0AHEq7YiWu57DZ13sLrnBEdBmpUWQX-K5s-N8GQP7k2uE4cwh8h-7od1nMomeao4T9xxtcMOqwnIPWqHnxOdAafxE4FML-UXk1YcPYDBfJlT7dFIV4a9iMTR7QGvU1EYFrNKDeYJrs1pX0xFdEXMBEEagrMw5JbJO7_vVY6wY5_re2suWLYxSLIskVDXBu0Z1jBUreATenhbpT98VGc1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل جدید دیگری از شرکت‌های چینی با نام ATRIA عرضه شده است. آن‌ها 100 میلیون توکن را به صورت رایگان برای هر حساب کاربری ارائه می‌دهند.
اینجا
می‌توانید با استفاده از حساب کاربری Gmail خود ثبت‌نام کنید، یک کلید API ایجاد کنید و از آن در صورت نیاز استفاده کنید.
نتایج تست‌های عملکرد در تصویر نشان داده شده است.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7763" target="_blank">📅 14:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7762">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7762" target="_blank">📅 14:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7761">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7761" target="_blank">📅 14:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7759">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/UP7GgwVG7WVGjOq87RQVv3vlc2xl4QBTfDV961VCh-Ur8C0e9PZ4bHO33_OcUWiVMauqznhhbHAtikj2FRurFytIkl_KRrKI_klyrydqzkQAc0c4ZGx2zH-xj03ubmkfMeaWTZfYsd9nckrhoGMzsEU6RBUeV3uYOdEBkD65HoSGfUqqZw_3fbsS1ALWNWCAV2bsi4n9KcrKwwlTE7Ew_mwB9jOL45An-37bo7Vku5U6Viu-CrEvHtbhpWEy-W5fayEjrBxBEIR9bO3LDuaFmSfKnn4EGYrkKzifP-n3AI8LDDFVY2JiRrASJsVEv7XH3orqkRY4sLYgsgrpr_KagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/U5kQZthD7s72wVZcZIFvokU5FKLb8DNLqC61q01fGpPWbSu40-Bjm8XaMqUH3UDAixNY-WHshTMTzgugCK_RqtoqRiQb6kP-Pr30t4HrwSTJg6JpYWbT4n7vqZScDv_AMrPhrepDzV1g0Od5HM8i_SPbL9BZ_richr49zw8NwdqjzEVBMjLCUS3qckeclTVmDBt-H_5T967nPBjSMVkkLD43zVv_PlsTchlJe-DC9kiugTtRH2G_yFnOd4LYtQQwMZOzila4_WLW79YFd8BymWjRWUu9hSILdHGJuXhpsh3C1g5MRjV52mSuYsQDO7sLJtXtQPfX8MoKFerMalVfqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7759" target="_blank">📅 12:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7753">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/DIV2jo8c24Ljvs_akcjcomLwSenq8ckaaB4UEmQW3ubWzd81SlhPvm9oNHuRbTjgb_zeVEe7WsW6bkm4FWvbm_laRK99d4mNwPmyw3HIM1lcD0ju_jIkvVeaN5Ug8smk8WPf3jG40p6YCn68Ru2cO8ii7BLRVfFJdQSQ609HTTonNOomo7deRNOCJvUgVAZxCbg00qziT4VJJM_71gZU5GlNhdT5kiGDK3wNi23g4ifdGqv0W7bCkc2aD7EuLiMMTwb3Dl4vShHrEzgHpH6bT974uAsaQcWadIdVgVXFPEWgCMRzp5auLPM3jSPcQAvQ3QaS-0X5DJhZnc1ax3xpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/XwVgd-SGGDunYK9moCQ8kT2ZsMEXXqsnLE6oXZVg0Y_4zytrQqyVM9Ad3kfGuzXE0xo9ECasrUhU9BGMm9mgcJwNmMlyjOqFSNXDWpbsAp18m6ZB6qK2-PKnOROL0b8OqSIQxvT740zXCUHY-0P0zIcRunsYM7KwmDbrsoHgxX8XidtkfLPql5AlQ4OW_DZddYz9Knr2xwqsru5x8UY2eVv4pCZHXr8QLR4-fzl_HLIstj6Pv7JHVQie1M1YjJ4TWGW0hfHA-bA0ldgVusqG2ibzggVdMiUL_k-PnY06Ifweri4IpwXmpuHYXILtamdjbipE0yPPrFdVk_FEd6J5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/sVURyNlHuPslYSq2CN1T7A7MR-BXRCIl8pMVXm9YfqQ8ubinqeYMx9RPlPoRT7t3Bfb5upeXm3SOpUpaiG7GKgFcjCFNNUcylDQBOU1kPFOvNSdDGcASQuIOV1Mz1Xpl1O4_7zUkoMeWScwn_BDZ66ueg_Em5pTarJan7DdBOsICgsScZEQF_7l89ionKgvAciNI_TBF8Uc__pLKNNRGJ0A3G139KG8PR3O25GreDCVp10T0mKetwj9fj48ziYzgBcEWzquSFZn6ucRSb6cbsvSJ2-7TsT1iAza9V7jsBqL-vPkONCHmdQEnsEaysjuS8GrPKPur_8DqpKS2OAY_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/MsJ1866xt5i7vYNJxaoVip_oe2o-razu9SXW4vVxmHW_q-a0MKCWnjCpyPLS6a0JF8m6r5KktgaKcCqILvjDaQMfslTcgrcOQ6sbIQXNr4Io3jYWgHgG4rXL-sYzOPmAaOVXQy9gbbkubUQoDG0IUKxapJI4BaA2EBVfe0cSORm69CGM89NTvPGhsspsDAwhIZnTUdbD1wIzxt00lT78M_fNA9s6td4i-xX8cIyWp5J_s1ieCuIK2nLz-MMDu-MKZ_cW7PvuqA7viO6ZoCNpwR9NMzoV71P2Gnu-6WVqAsbdI--UOCjIzu2KGU9KJ15paUqN7_QDEhuIAlsPHEhVEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/vAVUPfdkZ9sWeq6_euKTs4BQVEWNqAWTambUn4CZxrjJkBU42W0ViMJZzzNPgEfr03Q805eIPSSroLiBhE6n8QvfakaZIWC4Hu3g_Plkiu8zFNNDMEl2qC1YXMaeOVJUHgqVrLyh0FzTH3pib78-l2_BPosf0_7_BcUwQLavw49ZB4lBxN9V7RFuvLGvK8hCZ21p_kWhirQnnKBkPjJn43Gy5YwrsWc-gfLx2W8VCkS03vEGhhsFFGNK26FnuOqFPVyESHJ5_12QhfJDHvWT_koAOew7kO3t5NUlJku3FsLjTMuPv7sLFzMPLlzBFsXlPI7hCY00TysaHdTvSlwvYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/isEWXdBWkp887VzEa6VW8U6PkavONhkT4OO4KfxwgoTSpKSIiY_-aDaVdBOFJiGBO9cloHIED_o5ITOaxGZJ3UsGSW1-HzwAiErUW_FqNUp86WaQ_dgmKMK8q6jX0DrAlLj2C0yqQfKXClhpVTkxWDiAdtVyan9lfD_SRrAxIIRhd7IiPhBFiyrdlQ21JFpi6ZJNBwbqjtei4c2SQdfdcwQ-_n5yf2JtYa8GpeO5jY-5YD1HrCIf6PVXHFABKzOCQ2MQ115XgA0f9FCGuXoXLk_LSxAjTkzoYpFA5EArQarYLfOrq1vIuQziZTjKMiQgEsbtsr1z5w7zuqvtuuCBCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.
یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار بیشتری به دست آورید. نیازی به کارت اعتباری نیست.
1min.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7753" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7752">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7751" target="_blank">📅 22:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7750">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانفیگ مخصوص چنل -
سرعت خداا
vless://e4b11ac9-46f7-4cc0-92ed-bb9dfaaf3600@94.237.92.65:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=lkMM9FR-o7Z6NwmmQVK8rLhCQR1mbJTgjY_0upeS2SY&security=reality&sid=0436301fb0178b&sni=google.com&spx=%2F442987454d44398&type=tcp#@ArchiveTell
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7750" target="_blank">📅 11:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7748">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7747" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7746">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7744" target="_blank">📅 23:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7743">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7743" target="_blank">📅 22:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7742">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APFuSAigeYwKxxGgOMJx3OyhraNSoE4tcx1QyeY8jHGitc7bJH2GSPobYH9Lc82AlmVKPaVFC_StloeJbw2rFJHUyj39i2XFgkVTHt8zYduXZBPNQG3_UyjTbDeQgl6EmYqiUNWcfYXdeYrgq3DqrsnoTzRn463tmcBNJl-wA8FmWEz6aMRwXuVgo3O_XRhCdUryrZQ3AVZA3rhcbA1nce4kPHGxFbfj2aByk8uSOsiQ9axJk3CbOgxHCe7qxXvcHQwNcbpErVLOClwfed3Sycy7zIPEHjSCD6FV_Qoa6tCcMgHxcup6rw7rFqW0HqXgoZzpN9Nu0nIOHj8FYEUehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
دسترسی به Seedance 2.5 و سایر مدل های تولید ویدیو، عکس و اتوماسیون
آموزش
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7742" target="_blank">📅 22:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7741">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7740" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7739">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7739" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7738">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=qtp-_f0T2aHhchsISCYkd52A8c04OtK9_8t15G8_kCzR2EJRnHcKWjNHsjEB4ngKdHniCfj3paKDjqmPrj-5Wgs_9NXRogDtYPlwjOy5taTIj4TZQHhUkGgNegw77PR2DMMsnI663x28DYkebLGgyVksNTUhDfp4c69Gq187UM-URtQCW7H8gHJvhP-tgsWu-kMPfwBdyQhpfo55_vNb4hy_MKKtzXXQCVJXZvUmKCL-LMQVX-PrVk0SjccU7JNJTJslX88chlbuIZRCgulgYx4K5ZC2FyI2SMyx5Tn0_47MUW2zBAy1QB3CZ0BP99N_HO_cuzK3Mf6kjS2e1HBSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087627b2c4.mp4?token=qtp-_f0T2aHhchsISCYkd52A8c04OtK9_8t15G8_kCzR2EJRnHcKWjNHsjEB4ngKdHniCfj3paKDjqmPrj-5Wgs_9NXRogDtYPlwjOy5taTIj4TZQHhUkGgNegw77PR2DMMsnI663x28DYkebLGgyVksNTUhDfp4c69Gq187UM-URtQCW7H8gHJvhP-tgsWu-kMPfwBdyQhpfo55_vNb4hy_MKKtzXXQCVJXZvUmKCL-LMQVX-PrVk0SjccU7JNJTJslX88chlbuIZRCgulgYx4K5ZC2FyI2SMyx5Tn0_47MUW2zBAy1QB3CZ0BP99N_HO_cuzK3Mf6kjS2e1HBSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7738" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7737">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kp2KvZ216v_zCdK42WUgbRp01fw5hZnbh34YUogQIndZ-OZE9NF6qTUPqRtmhyS30nK0bkfYRv3n6ZDJ5VTvHcw-ITGVkbRrC0iXl8l_klxFN2eY8JsyaB63D0EbmpvJ47mrI6jCwY9dQBuRhQ0BDbK7JgNVWFNUguaAIicKPGHgjB0c9GZe0ctxOpOH56tP1sj8W0hhhcCPHRdDlkVW2jOkGAZXs-UejZgdnnlQCNe1WGv7Llcz3q41UZbMPCdGdyr2WjLZzj40FkLg9Cu81z0s3_6q5Yf7UfPoeeb-Eh-uVHn97ow-8QHTl_6A_EoXM1KK7NEA0rzOlIecUF3DWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7736" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7735">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7735" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7734">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7734" target="_blank">📅 12:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7733">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7733" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7732">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7732" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7731">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETphFjboXbgOSfwREjmI4PH2yuDg43pn6bAB_7PmaIPW1nMUh58tlYs0uG7_VYT7syJZL-GaahmiU5ZEfmEr-EkBapTfntZmiwt2LjsjhCwa8QuTqudjsSMwxu5gAuvcL5OyQjWwZOht9aAxxwxsO6bs18lB4aALtcMdlp9eYAHE-6JTN8HUhENosVU32SnVkt_FXzQqhD5vJ19qJ0JCrwLPspovJY6BOCybx2AvuKXguLnr634UjzhYV2jLjMLT0AWzlcVekvc9-mRLWovRnlkR7nqQi6y1_fgHEY2xNawJzOTL8Gxik-3kq3jNAu4wTIsqTSUfGmh_0GIamhfPDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7731" target="_blank">📅 23:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7730">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoJSljeYD9SxhuqNop63DEp2q8Uk9WtlcnFw0Yp_V_SHGoOAuemY7iHmFRkl7KtDutcT3N5jM-3oj-TMGfz_pXkTdg_cTL8NDUNIucFY2wT-ef7x2cuklgnIil6jBwG7WD3tgznpilWsoW-HCV4us6Fecg-2UzGT7o4l0fAMIm_twkQ9sovIrfchCGotP7-xYYy5ulQeDeDU_WqsoJtPqUicp_A_E47Nl8VWtYPueckrbI8CY9wibkbDWbo0lmsXfcTdDdR2wyrSnJoxdjEmOnNw0b2PVrht_pTYDVnrhgQXum4XwoctNV4GqWpAhxmwdM46Y7ebnfcztN5WoK61yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7730" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7729">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7729" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7727">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7727" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7726">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7726" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7725">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7725" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7723">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jR8v-Dp-YXdQGfmAcr7ji_hU0uKahN8FsHJ4N-0r_cBauLxH4R6BEp1YWnZms0MroeO176oxFh_ybmHbN1sx1-2J-JTWCJzBANP4Yh05bxfYebPvdigmfGGEm65SI2DUUm_9GLrLVazRm-Pok-u0atsJNs0f3nn3w9m0zMx47G1ktCS06yloqhfH0nNzq06AUnis8ce2NRrE-nu5_YtS5S5TGa78V7KtyDqKtkrs-qaX5VT6DKOIDnIxWt-Xj1XDDROMYuMoS6_4MGb797xj3DLV-T1q5AchUOrSLIJr8KgKRWp3X5FOf6ofkCEB-6_HhOt3f8u8xWmKHqPU3KYOCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7721" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7720">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N0z1XgR5ODvwmwSM3m3E416xJbiUzO-_wYUuoF1t-5DTqEBLNXWH0-CxQLXd89kh91hMkU5sP0GGdP2e_JfP44b33Nye5CBs0u5DcrZDQRkxTSJ6qpjYQurQd3iVdaRekiYZrGN69PnwjeUhfh00Huw275BmvHVW7F326-YoQFsu1nFEZTBGG5YpNQEqjTSZ9W2nEOPfhdEd-RNnnV3aViQF_OmxRTOa_nBJVo5XiLDiQCQJem7Vabo5B3nHONnEjgeibNxS0QFVUXl_tLVJm1VTTt3w6xXZEjPZO93-brjK8tvE0di2Ep3AeOsX8UtF-PvYUB6QoRDbQ5mANR695g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7720" target="_blank">📅 15:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7718">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxrFtIHpp7v50hPb63rTgixKWmhTQap1LGH_R5vQbQGKTyHai8d4dOMyH8TAwLY0XWpsCz2X7E-sNj3LdlBZzm9BteXy-UakAgGawYyCIudBWmEzNjxHGRfrilFq31qwIUzGCV91k9gFyebriOHDo0XDdRhfzhg8T6elk7okvdcJcuzlSD9bV-2K4-Cd2yTMmnXxCMM66Xab-PXy_TT9g6yBYegkf8nROe_owDsBREhBmwU1UYd_bsTYyqUHs8PvtUeLrSK3ocC5snj67pJ0k5i-tbMAKrGjHyt0jIaxgTkkh4tUDhmhn3mFfVASam9kDYzqpQlvqZ_Sw5rJna-6xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7718" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7717">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StpSHRDhvQgyFrU0TKoVaz8_Kks7IvlyxwnDMTlHEgqcv4Tx-mIQSdBp-XGu2gxp5KrvkcfeWkeGyGVsoW3lMpSZKdoE4sNbuANktqB1zpDYxLfu46L9BX4iPA12bo8BzVlBtBecpBguAtUa06ahfdNnUpHCpqoYVUInfFrNCpWV4aCm2TSvcpOKsNvE8BivJnYKkC3ThAs2HEWI0lbTW4syPPFGsaxe3ZGrSebvyH6xPIsYtAv7KBCx3BSReOl0_WrV-kW1cIY8Mgo1R5clXWyC3tIEEufaM4jPvp3oLvBiHGH3kaazXTKrafb20x7SVR08ea2XQf1E8LUYPcsUjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
100 میلیون توکن GLM-5.3-Flash با ثبت نام در AutoClaw + ZAI
از تاریخ 14 تا 16 سپتامبر (دوشنبه تا چهارشنبه) 600 میلیون توکن GLM-5.3 و DeepSeek 4.1 بدون نیاز به کارت و همچنین یک کد تخفیف ارائه خواهد شد.
این پیشنهاد در
اینجا
قابل دسترسی است (در حال حاضر شامل ۱۰۰ میلیون توکن می‌شود)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7717" target="_blank">📅 14:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7716">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTsH5Xil_k45uhqwHozSJPB2ymCKV4XgGHSoXsqxAfXRKPXy6xZrj56h4fUmzBBZbqEJuyPbbO63aA8R3hBN2AHoWLU3i8YnZzLcC8oft3gj-nMRvTVy5EI_6SNZ9EVj8c-CO9JkASvCTzcKfpBSA1E72GSg5QUdCizIGl4kvfuNaPppFfryRPmQY6HfS47Xisn18Ztz_6ga1nXNvNCVaG7jhDbirAQthlKhsknWR_eqNY70Q5b-iLE_H8XLaNPCGKYVgyI8-_RxqbgkTjnjNuUwTM0a4N9uUzActegKS5fAFbgSJW4cVwdNe_d9gU60oHZS1prxGsbedoxyLYqZDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7716" target="_blank">📅 12:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7715">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7HrSRdhe0V0MYJ4q7i_ksTdYLDcCut4a95uLJwS86jy2Odc5ai0tbXQ6G5i66iCrsNIvpuZoLY7d60YDZcU8RmiqLyoX2r6YCOo0khkbYnU3oYRTcIrWzOqShlNf-eugdRu8PAJJXzIdaBVgn_a2v4Iyajkz0fTaivqD9lPxRWNJM7f9jhSJXGd0nY7uzg3VjDQxVeBpbc_hgQSXEBakfkZD3XFvDr49ecjBu67MB_HlmLXD_l9Cvq3aPisWjiUnAYRhdYU5FwhjsBIJYEaPA9UvXAV1xDZoWv2Q45pSg-1L4ebldvFKMhJ-96Ge0MfCgvC85wegIHfvcfyBlOViw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7712" target="_blank">📅 21:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7711">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7711" target="_blank">📅 20:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7710">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚀
دسترسی رایگان به Claude Fable 5 از طریق GitLab!
💻
✨
اگر می‌خواهید به صورت کاملاً رایگان از قدرت مدل هوش مصنوعی Claude برای برنامه‌نویسی، ساخت سیستم‌ها و توسعه پروژه‌های بلندمدت استفاده کنید، گیت‌لب (GitLab) یک فرصت بی‌نظیر ۳۰ روزه برای شما فراهم کرده است.…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7710" target="_blank">📅 19:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7708">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">😎
دسترسی رایگان به GPT-Image-2.5 Sunburst به مدت 72 ساعت
📝
مراحل: ① به https://arena.ai/ مراجعه کنید. ② حالت Direct Mode را انتخاب کنید. ③ در لیست مدل‌ها، GPT-Image-2.5 Sunburst را پیدا کنید. ④ به مدت 72 ساعت، این مدل به صورت رایگان در دسترس خواهد بود.
✈️
…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7708" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7707">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت گیت‌هاب قدیمی داشته باشید و از طریق این لینک وارد شید
✅
🎁
با هر رفرال شما 100 دلار و شخص دریافت کننده…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7707" target="_blank">📅 12:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7706">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5bR6-Lbe1uCRCRSLWaJFsMtSnjuF1obmtOQo3TaTLt2dtVQmhgPPxcG75B1hoVlNx7C-BRU-nIgHsFPrsyVyfS1Il6_3jcb-ZNbrng2JaJVLm47j318pVwmMDEiyvXxrya4oieBlK_hb8bWfoxsiF3eXTa8DYI_iskeogdFD_D11BzdoR6qfLwpVzXLAmDBO-zikvhJiTJTFYw7O-scPqAhAnnMJBmhbmOK4pvdEHD7PhOushT7Hu6za7p2ol2xAtx6tTbbYBpRvFOCF7OBDTrkk_EwwcWSD1dEVCuEgx5DWu-NzApC7-gOVYPlebNHb0r5XZAKbNJEx2Q3M_dPSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7706" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7705">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0fLX7Zqlyr-EOz0zY6bmulDRib03UkEFRjdERkRKUZ1RsY88b45HvWsy6uYIMZM39GbAsvvz2tZBs0f-qTFBfExb_Ms-yFRX2kU_C6pQiZD0zqZn10CuDBZyBNY-CLKE_GAFuG45AFkuEBDciOibZe8YkUPNoBTpmV7cghOB6UoZ9ezBOi3ahI46R2AdTXwYMi33bTdJHanHJIpCZ7F5t_LTzmzJOf4-ySO3hiZEvbK5o1lR-w63ST4_j3gWRBSHXlFhKaJWZLNwMJUqAZOi14PNeCt-t9m-948nTa-gkC1eIoP2u5l_ji1rUtO6LpOWQPd-hNEKMY1Rr72U9bTgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjtopFVrgJTyi97SYvaI7ulT10YJMhqXB8IohEF-HPda0iUvV63Fdc89MOvk6bKaIbS939ZfOcSw7mPAd1B24kG0LMLTmc5ufC7un-lldD4qH3qTXlbrAedgBEHMshUJyP5CvoAtiJLlfv7kb4yodsOnL-jTnJ2X6W7M8_ggALhpIhW9qfkWqXXPHpclCdoEXDaiUppl4XDz1oZDwjUSjSHv0WzExv1_QV1_KkttoxlNs6DFkp8Mw0cg6dU0theZKJmdsGH5ezfT-NqFdJ4UmCyqldofSSmiRoA2_bE8HA7K4jg-Sx-JYCEMqj3Gqkqp9AHPW2A45QqQR_Yv0o7WLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi9cUVh2fxcvHv2TyOpFf3CpGIkbp2RwSo7PEf2tDQOK4PpgaK5OTqBFS2sz3bYoko0K9lg_MyjXOXF1WUAG4qSxIBXsWiZkwZOjD84T3xA6fBlU6lfeEL764X6vfVkwKLNQCqSqUsLcAWsB_sWWlheBM8dYPruVu7VNNsMzUenARfj5gQcnjOcbOK4XMHJMA374vtTAJJhfnBMLrNUqzH4iFkUR6FFcUPLqcxufxYUueU73atvtvF9-Tp123G4XuNmWqql0fsmcYmpFyxyvPT-eXOVgMCnUI5wSOZZvd-bFq28VAJDGO0wcO2nJMMg-BTyJHM5H7ccYuaTWN6gdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GPT-6 Astra
1 Day Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=gpt-6-astra-medium
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7702" target="_blank">📅 19:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7701">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqP3uCfBt7gckjnGby42W2XzrI1BmA9lfcs2ENOTGTlnhRxydMmCRQ1CZ776H97ilQ7DaBuGvOvQexlf4J6K8RSbcgR6H8eoiNBj-24aD5EqPzIOxED_uIQ9RQtLkUUm_IfXxySDTP0-kPzdsFijj6RdK1u0LZns7fwlLegUd3pZPt6__SIPZCe_-xjCljs4VG5ufWSMTjC3O9qYpjo1khEEKxXPbCFzpYbcQW1LiKXhdPiroTKixy4nijXZb2H9RUaqRy_0xdlSbQbhF2mrlRt81t0MNLDCctkEcqVWRxkZIk_AspkAwDsQSjywFMRFNlx63AnvSYRIXnDF_gmkNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7701" target="_blank">📅 18:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7700">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7700" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7698">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7698" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7697">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzsbU0jJpFOu9RWsAjs1aEeyWR7HLVB-manXZkr2s4UN4Iyo9hqP7_oJ8HDZQw00kWl8RH-zRUcjVh2h_aHRg8Y0FS38n8r68l2_3vaz9A4PETKK2uPggzob8UBBFrKiClk6kqU1TwdrYhb5dC-PbrqzqdZYbSnS60we1nxmxh6GNXpQ6KLiUkbWJyXjbDKxnPxBJJapN-71Xxa2wBj-gDO0NNoqRVQb8fayK-oGwNDs0KkOyvKX2Zcg_vax_hsNOdffVTdOXaVCxplhthRYwsR3boq-bdrIjb_vObDZf1Hc6l31EmePF4tPyUwgvBWOA-KXkumJsJH3M9I1MDKPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 میلیون اعتبار رایگان برای بهترین مدل های هوش مصنوعی
🚀
Opus 5 | GPT 5.6 sol | Sonnet 5 | Kimi k3 | Gemini 3.5 | Opus 4.8 | Grok 4.20 | Gemini 3.1 pro  همچنین دارای چند مدل رایگان :  GLM 5.2 | Deepseek 4 Flash 0731
🤖
|Minimax M3   به این سایت برید یک حساب…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7697" target="_blank">📅 16:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7696">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
دسترسی به بهترین مدل‌های هوش مصنوعی به صورت رایگان    Mimo 2.5 Pro | Deepseek 4 Pro | Minimax m2.7 | Mistral Small 4 | Mistral Large 3 | Mistral Medium 3.5
✅
برای فعال‌سازی فقط کافیه یک ایمیل داشته باشید و از طریق لبنو زیر وارد شید و سپس لینک ربات تلگرامی…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7696" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7695">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fktcM0ROgUajVx0d_LdkqeCryZeGi7BL4CdeoU8PkRd3BIl9wEi1cQAypouHEW5ZtgY1Uo1xC7knG-cMv4FJH5OuvPOtjn03AzP-uXKkGq2M_RI52EYnlrQxOxGThzptT7zGxYVrWV-M4z1AC3bKBG7fsSFe1c2UU3k5xgUIEtjHxNreAHkSFgImeLx0cojHcFjzbLfHG1fPA8r7ldVZyFhsVCOtAVT9cjTBCsq9Xs9TNStnq1PRh0CyoV3egB-LcvRokL1ZYE4HXToJ8qxOdQq4rmJUxe1oyyQe5hukHhu7YEtTs8u6cUM5HQRNNXKaw5Un577rsEKEu2q9PCpyMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpuujZOo7W5lMBHPBhAg32NuYRRDrSRErPYKSPVZfJgDxpyqQbf21v-dNpJ5hBvrSxuOW40SGlchHN5nKuF3Abxvotq8QSL3nrSfJ3hjZrKIAJa659TzpzjlA5ZHrf33UfI96YMQXM_nEB3NHd0TFQZcenKyxzx89soa3Odj-Txs8m30mfXnm9gouO7QTve6-7ruUOee-8PSI9YpafFIUOndIEu5zR7ZcOkWcjepmoWR0w68U7QCa1NJ0pGfpA7yztMt89sHnlBg0pRgrBTMJwAYKn3I5KSkPkkq7LdM7s2c3KaBAwTszQf951v7nB64UHVWa0oRBcDEkburMpODjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXEWy-z6BvYow--kJX_OCMgVlOSxJjSTbBsMEnaZ2T-UQgLNaBipeE9B4BqJ0ov1S_aEiYG2hyQlJBKH11sEw4xu0fp6C2YsKcLHM56eneaV5PIk-90RWcowsW2BRJNvWd-WlOXHGDosY1Ef3SjkEjHScy8-OZDVIf35h2WjbvHgcYn6MDQCfr3eQn4ges2yhTNFXjfo7dwAdpIYMCRxAZrXVZhn4xTWsRQ_Q-E7SqW-x7gTLsa1REbMpxoSVrghKEyZMJPDPtFxp6YuzLU1TzHUO-viUmEyKLT5iM-MnyJBIWtHSN61j_1A0UtVkePA945ucRILsVU7zCrAyVLu4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">DEEPSEEK V4.1 رایگان
🙂‍↕️
🔗
alysiscode.com
✅
50 کردیت در هر 30 روز
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7692" target="_blank">📅 11:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7691">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎨
غوغای جدید اوپن‌ای‌آی؛ مدل ChatGPT Images 2.5 منتشر شد!
⚡️
۵۰٪ سریع‌تر با جزئیات خیره‌کننده: جهش بزرگ در نمایش طبیعی بافت‌ها، شکست نور و واقع‌گرایی رنگ‌ها در نصف زمان قبل
✏️
قابلیت جادویی Sketch: کشیدن طرح اولیه و ترکیب‌بندی به‌صورت دستی، تا هوش مصنوعی…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7691" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7690">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7690" target="_blank">📅 23:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7689">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7689" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7688">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=Ny8k397zPNciTtz8Mp-ksYpdHdlUfcGl-MxsvwnhuZSfVmGFwiV_eLQhoQTB2XGmbGV9_W_j4R07-NIGDPsUoUoTVLRGubVaTZYeqvramlwcq3V272wlSbpZ9gGIneSDyfMKcepFCjoQ8c_qUjMITYiIRo5XahJYrxFsoOZTI2fQIKJZa4sN7CguXIGOL2MpTP2yGiLsePzAB2hbN2dePZvHRBd6PD6uSaGiNeOkizNPfrhFe4UBFghBzgNRjaUx6JXWsNW0gbjXxKwrwTH0vRUHhrsyX81aYQVUagQYpq014yChfWhZLjxB8ZV7GfmQhia4jvtDD__GIuMBVL8cgGi5bT5xvh36peecGcMnR5Nk4h4sWyDEkTnyvftR2fhFAc4-ieEjuO1m_SqWuZRyVl2As81tDBTEd-SpDaA6jymBwIof2kVViHu4bhR5_N_cUjy2yoIzqiiuKYtkjyHo1NRA5KGKbD6kPrQLyj11G0EitDrQcBtYclu2w1ixSuigq-nPGgdx9osC6ckNX4KSjHQzXGPQNzCV55fsnFBhWlA08CazMdgu-M5RYOkB56o6ZkYgpgZdhhJTcRo-KUuYYjP5FNRVff52x8HvC2YfWILq8Z82tgocKy_IMd6aUAci8HQLp5DSVVF63mIjwlDni08veMhbsVBbzcHzd2UfZTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9374b9e092.mp4?token=Ny8k397zPNciTtz8Mp-ksYpdHdlUfcGl-MxsvwnhuZSfVmGFwiV_eLQhoQTB2XGmbGV9_W_j4R07-NIGDPsUoUoTVLRGubVaTZYeqvramlwcq3V272wlSbpZ9gGIneSDyfMKcepFCjoQ8c_qUjMITYiIRo5XahJYrxFsoOZTI2fQIKJZa4sN7CguXIGOL2MpTP2yGiLsePzAB2hbN2dePZvHRBd6PD6uSaGiNeOkizNPfrhFe4UBFghBzgNRjaUx6JXWsNW0gbjXxKwrwTH0vRUHhrsyX81aYQVUagQYpq014yChfWhZLjxB8ZV7GfmQhia4jvtDD__GIuMBVL8cgGi5bT5xvh36peecGcMnR5Nk4h4sWyDEkTnyvftR2fhFAc4-ieEjuO1m_SqWuZRyVl2As81tDBTEd-SpDaA6jymBwIof2kVViHu4bhR5_N_cUjy2yoIzqiiuKYtkjyHo1NRA5KGKbD6kPrQLyj11G0EitDrQcBtYclu2w1ixSuigq-nPGgdx9osC6ckNX4KSjHQzXGPQNzCV55fsnFBhWlA08CazMdgu-M5RYOkB56o6ZkYgpgZdhhJTcRo-KUuYYjP5FNRVff52x8HvC2YfWILq8Z82tgocKy_IMd6aUAci8HQLp5DSVVF63mIjwlDni08veMhbsVBbzcHzd2UfZTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7686" target="_blank">📅 16:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7685">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7685" target="_blank">📅 16:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7684">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=imDTCcg3qjWfUynUgAcGXHcWZXTlDtmEahxJFDYNZ6E2APZXMqUfZSFmAd74veDbrgNT99M5Eb_aWx_jkerRT3XFbxwAEmE1uvq3t7CoJ28754vlmF1hovXHQu-M-y2iMbM-tUuKDFDK6p4na3PBEYBRZBIXsNLfYj6GgcLYJkX1PuIsMU7n1EUjb46XlmxpAK68WdGx5-idVXRTnZiqzAwj8uvy1Qy3ntOQESq1A6w6doM2OlmMS_30FxbDTSfpZaUF44E4mAZzFRr9yUA7iYtWXgdMJ5T6-Zo6DxU2nGPa9R71EqHHt9OCNwE92W4ERCH_vOyj6p1tVrzBuwl3v0UwkQ2DJjQTROeTgeqj10mL_ITbZNQPpe3nSELCkU3H3AjNdCYsd--RSBFoOU4PkWt6YkohN78NbTnL9HD0FZuxrvscXavZ5uCnaz1SuVy086tXIlojL5yfCSJ95UIspdny9j24n3kE1EuWANohaCMXO67iOzRg-y71cNYbRcdMC2FmtKhlqwaGM92eodcbsPdyBh9wjD78LeQvl3eyLjpwwUfl23dmmB7yqE61rEhY6xT4SBFc90FAdunfGSso4x0kJuiaLG4f-__hwveqpvBhF11bPDihy4xEpt1Q27qNNjKAy0AcClFp0VGhAtBvR2SANTTn73Fui-FuyoXCUOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc89182f1.mp4?token=imDTCcg3qjWfUynUgAcGXHcWZXTlDtmEahxJFDYNZ6E2APZXMqUfZSFmAd74veDbrgNT99M5Eb_aWx_jkerRT3XFbxwAEmE1uvq3t7CoJ28754vlmF1hovXHQu-M-y2iMbM-tUuKDFDK6p4na3PBEYBRZBIXsNLfYj6GgcLYJkX1PuIsMU7n1EUjb46XlmxpAK68WdGx5-idVXRTnZiqzAwj8uvy1Qy3ntOQESq1A6w6doM2OlmMS_30FxbDTSfpZaUF44E4mAZzFRr9yUA7iYtWXgdMJ5T6-Zo6DxU2nGPa9R71EqHHt9OCNwE92W4ERCH_vOyj6p1tVrzBuwl3v0UwkQ2DJjQTROeTgeqj10mL_ITbZNQPpe3nSELCkU3H3AjNdCYsd--RSBFoOU4PkWt6YkohN78NbTnL9HD0FZuxrvscXavZ5uCnaz1SuVy086tXIlojL5yfCSJ95UIspdny9j24n3kE1EuWANohaCMXO67iOzRg-y71cNYbRcdMC2FmtKhlqwaGM92eodcbsPdyBh9wjD78LeQvl3eyLjpwwUfl23dmmB7yqE61rEhY6xT4SBFc90FAdunfGSso4x0kJuiaLG4f-__hwveqpvBhF11bPDihy4xEpt1Q27qNNjKAy0AcClFp0VGhAtBvR2SANTTn73Fui-FuyoXCUOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7684" target="_blank">📅 15:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7683">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-5nYH9VjBiLbspVYCDKM42xXQ3nPfQj6zyoN1N1UykodjeGzUTayuV4MM_Y4b5wLfB6Xl821EVusEgYN9gUqEe8NFh0bvVTeK1EfLk-KL4CY45EYJaVoPk8vohprlL_6utw4I_GECjrqqU5W2zNtV5Zp5idENdyn_6wmBJ-L9cDCxo8hONd0bySeZBT9KmSzkPAV6uR_czZ0ka2-1KWDmZ7e3ceBXDNzOSAxvfb6_u0qJGaQ-I8oQ9BkMGdng-i-PQrQplfIJa4mBEOpM4DoYH5KPqPKBKxCWvr2zZY034EXqKbyFErmlu14SpyxYOYym4LPcEPUuMk-dRfXEKxlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=Ahde62XwWVPOn0O9H7kazy-2TlE8Eo491C4lXcxma80PIO2MVCnJcjc9yduQJ4ftcoh4Y0r_v8C71KXBV0feDEB7Gf1ZcFKtaYyB7BqtP4-3Wn8Gxz1iHmfFmkdfC_4yy-Au8jKlpAG639zIG1aeKe676osL2Ak7L0e8aGav52_J_v45MbHOkzQ5Cdp-UyYWosJV4sEsx2VjafDs40Aq89eMAZrgY-CgdbcL4QAgDsD8catv6kvXqEjO6Ql48X0XVhLa4rvcJ5D5lbBmj5LePwpwEWB8XuJO6kiEkBuBy7hMiM6s6lngaRVxpmHq02tGQi5w86jxSUtxsLm2oEPcNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e226c05d7f.mp4?token=Ahde62XwWVPOn0O9H7kazy-2TlE8Eo491C4lXcxma80PIO2MVCnJcjc9yduQJ4ftcoh4Y0r_v8C71KXBV0feDEB7Gf1ZcFKtaYyB7BqtP4-3Wn8Gxz1iHmfFmkdfC_4yy-Au8jKlpAG639zIG1aeKe676osL2Ak7L0e8aGav52_J_v45MbHOkzQ5Cdp-UyYWosJV4sEsx2VjafDs40Aq89eMAZrgY-CgdbcL4QAgDsD8catv6kvXqEjO6Ql48X0XVhLa4rvcJ5D5lbBmj5LePwpwEWB8XuJO6kiEkBuBy7hMiM6s6lngaRVxpmHq02tGQi5w86jxSUtxsLm2oEPcNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS0HEK-udl_NHRBXPBYmiq8Gntoww1iA1woLz9v5vnHA7PGJM-oXL8-5cedcyGKp5zSFk53ggBWQPKmQv13XYj2BeWhhf_wAUtNFbDhqqd5XI9Vs7QY5Jxp_4n3X0YGLTVWH_sinkeJ-pl-yrXkGKfXJ1CcSsfzc1YrHEefPV4WFzd3iY9mo8C6idv-5UrnT7tAA_E2ExSc8dJ4SaL1u99ltOWAXcVOoxegcs65x-9gIT-DvhiOLVUXQKfV0B0S-jBhvjS9sxPqcyoQQAV9yk9ApLqYPzi68MH0U_32D8R7bpytSDT7udFwO_8_UAhSjFZxrg4c2Mx_RHgd9py_Pag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=AREbGpOCMY8bcKnYcXz9p6TRQ-HOc-ceXA_QUzEqJrrHsdwY9HNgKiekPJCzs6k_085NexXBY2fFmmUeD-74POmlDLthrfDobYQa9P-z5DVNjZubvqeyJ9DjJLnMaPwwoUm_RHnUKvn7Ufv8OuLXaRgoT0jMIXB2IMviUxcxGFzlF1S-7vn0nYl3tMIxd_Jg7ulYzU9NzZ4kPaUqRbaD3v7rzpYKFelNv0SiTVUcrRFvqR5fvBPbNR4-XPBe3o9ijxDDyRJYychevqgun718qr_2eHEZDn6vTxyncYh2KU8bHVIGTR_CFzphj1OBgN3aktHej48ZrKMsLiXWu9eKoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c846b7bad.mp4?token=AREbGpOCMY8bcKnYcXz9p6TRQ-HOc-ceXA_QUzEqJrrHsdwY9HNgKiekPJCzs6k_085NexXBY2fFmmUeD-74POmlDLthrfDobYQa9P-z5DVNjZubvqeyJ9DjJLnMaPwwoUm_RHnUKvn7Ufv8OuLXaRgoT0jMIXB2IMviUxcxGFzlF1S-7vn0nYl3tMIxd_Jg7ulYzU9NzZ4kPaUqRbaD3v7rzpYKFelNv0SiTVUcrRFvqR5fvBPbNR4-XPBe3o9ijxDDyRJYychevqgun718qr_2eHEZDn6vTxyncYh2KU8bHVIGTR_CFzphj1OBgN3aktHej48ZrKMsLiXWu9eKoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7680" target="_blank">📅 13:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7679">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCmZzZV4OJXh6pHHAWadAJEDj6gzVs42dQorYcTA9CJcUSh5MSMjaHjXcjbtI9hZilwxt75MUbF8VoW-Aihgqjb4zcQQqJyit5zLCvfACTKhopIZ28wcM0VBoXnYbj-YN9Wn0WIqJDlA778HMv1uY3UBuBmVtcNMpzx42Z9RPcvhz_M8vvnQ6MRTS517o6QqhrLJQqPudaaP_w3ptL_oa2L9TkeF4Wava9IxD-1NV3lmq4kIfinTXT9vD1-oloDmwEP5S9rGpIY_2f5pofO-R4RFSXLaC2D0g5t6wY3HuQ2F6L2TkE9vEdsHdUh9gzarWCXNrZgGJTq16-cTw2Pd5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7679" target="_blank">📅 13:33 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

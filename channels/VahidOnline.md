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
<img src="https://cdn1.telesco.pe/file/obvX0CH09Z3BTM1XYPcrBaHChPR4apsSftw8SH8kg_71RD46aoQBwQGYgIv-rrdKGHHyRnSgBPkaqHfuiPCStL8_fObZ1MDwpqPNhWSvuckhAkF9HE78AHxhottA6pAp4eA24ZW110f0QjoYko37b9tLDWJh1Y_M4KAZjb0iUWPHMxIMUg25h8OcFwcEQuQ_B1tjrXY4irnfS0jMmJNnKHCTkVY4PZGDFz6fZLpzEFCdABMH1EfjLojlbuiJ43s3onznJvP4HI9QXj7mR3PCU9Ux4vM-YqfCFpAP7HQdaTi0GvZUIVs55NyN_11r6eedN9j3hpTsDWrwEGvEBEc6uw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.43M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 02:24:00</div>
<hr>

<div class="tg-post" id="msg-77487">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpqKnpbhnnrBcdS-NYA2gPX3Vq8OINzLoav5CQi-AVlIiDRfzpkvGjwjVvw_e_zWsZ_vgYTQFodpmkuok6pCKraTwCjpM2w6uAqFz5jSAqPSU1E9zH7XAC-nc2LiIw6fQZbk-LrYE3A91u_W3Q2XcUGWRZarsCs-AKMfJWOEUCqCU0z8K8ww0ngJUGJCsyot3Y-by9sovgPlDPYSiKT9Hy6iiJqs9qUAs4H5gucJYIm2ehotAl5uZUMPcYf9X2SakFXXyIXrtb2gMFIDochQuIno-48Rji_yEIzoM9kEl6826dbBF5VJIoMudgXMNoARSwHNGV_5A03EWdfkjrNFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مشترک نیروهای ائتلاف، جمعه‌شب، با انتشار بیانیه‌ای اعلام کرد که در پاسخ به اقدامات «بزدلانه و شتاب‌زده» شبه‌نظامیان حوثی در هدف قرار دادن کشتی‌های تجاری در دریای سرخ، عملیات نظامی متناسبی را علیه اهداف نظامی مشروع این گروه در استان الحدیده اجرا کرده است.
ترکی المالکی، سخنگوی رسمی ائتلاف، با تاکید بر اینکه عملیات پاسخ نظامی طبق قوانین بین‌المللی و با تحقق کامل اهداف عملیاتی به پایان رسیده، تصریح کرد: «بندر الحدیده هدف قرار نگرفته و تمامی بنادر یمن از جمله الحدیده، راس‌عیسی و الصلیف برای کشتیرانی، ورود کمک‌های غذایی و سوخت باز هستند.»
او همچنین افزود عربستان سعودی همواره در کنار ملت و دولت یمن باقی خواهد ماند و هشدار داد که در صورت تداوم اقدامات خصمانه حوثی‌ها، فرماندهی ائتلاف برای حفاظت از کشتی‌ها و منافع ملی «بدون هیچ‌گونه اغماضی» مجددا دست به اقدام خواهد زد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/VahidOnline/77487" target="_blank">📅 01:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77486">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWsw86BZjW2Pqd2oXndpVUSlLmUtbh6u5fX7OxDA2c9dOYFYX07aH6ydjW5Q-TDDHZHCz7ACXx-rttvOHw3pmgkWMRMOa5WqD9AEIYd-WWvhoVXhFBEi-mskx3AYKgLMAgr8ppRbCJQil_iF_67RixjtvaMQaLvFFk27PTCP_uvOHiIyqS6pkYOJIE2jdGLSjKhl6ZsfqqLSokNHrhAv9aAiH55pk214CWE9AypgQYcdreA1UDxAGyiORCft70zOji4B2-ow9o34BTqEL7tLNRApTBesPPBrVF958deEoWP0S28rpvG3MhKhIINwQwhMYSrLVtiVHtZI0EeuU6ZfJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
اربیل، عراق (خبرگزاری آسوشیتدپرس) - ارتش آمریکا روز جمعه اعلام کرد که به یک کشتی تجاری دیگر که سعی در نقض محاصره بنادر ایران داشت، شلیک کرده است....
...
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی ایالات متحده، به خبرگزاری آسوشیتدپرس گفت که نیروهای آمریکایی کشتی M/T Lavine را در خلیج عمان پس از آنکه کشتی حداقل چهار بار تلاش کرد از محاصره عبور کند، از کار انداختند.
هاوکینز تأکید کرد که به خدمه کشتی هشدار داده شده بود و آنها از دستورات پیروی نکردند.
سپس ارتش به موتورخانه آن شلیک کرد.
این دومین کشتی تجاری است که از زمان اعمال مجدد محاصره توسط ارتش از کار افتاده است.
فرماندهی مرکزی ایالات متحده اعلام کرد که 12 کشتی را نیز تغییر مسیر داده است.
....
apnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/VahidOnline/77486" target="_blank">📅 01:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77485">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سخنرانی ترامپ، بخش‌هایی مربوط به ایران، ترجمه ماشین
متن زیرنویس ویدیوی بالا
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه دوم مردادماه در کاخ سفید به خبرنگاران گفت به‌نظر او جمهوری اسلامی ایران در جریان مذاکرات با واشنگتن «هر روز جدی‌تر» می‌شود، هرچند تاکید کرد نتیجه این گفتگوها هنوز قطعی نیست.
او با اشاره به اینکه مسیر مذاکره را ترجیح می‌دهد افزود: «دو راه وجود دارد؛ یکی را عاقلانه‌تر می‌دانم، اما راه دیگر احتمالا ساده‌تر است.»
رئیس‌جمهوری آمریکا با اشاره به حضور مقام‌هایی چون جی‌دی ونس و مارکو روبیو در روند مذاکرات، گفت موضوع اصلی «پیچیده نیست» و تأکید کرد که ایران «نباید به سلاح هسته‌ای دست پیدا کند.»
ترامپ همچنین مدعی شد در صورت شکست مذاکرات، آمریکا می‌تواند اقدامات خود را «به سطح بسیار بالاتری» برساند و افزود تهران در شرایطی قرار دارد که «عملاً مجبور به توافق» است.
او در عین حال گفت عجله‌ای برای رسیدن به نتیجه ندارد و تأکید کرد که باید این روند «به‌درستی» پیش برود.
@
VahidOOnLine
گفت که به سخنان شی جین‌پینگ، رئیس‌جمهوری چین، و ولادیمیر پوتین، رئیس‌جمهوری روسیه، مبنی بر ارائه نکردن کمک و فروش سلاح به ایران اعتماد دارد.
این اظهارات در حالی مطرح شد که پیش‌تر پیت هگست، وزیر جنگ آمریکا، در نشست پرسش‌وپاسخ سنا گفته بود چین و روسیه در سطوح مختلف در حال «تسهیل» اقدامات جمهوری اسلامی هستند. با این حال، ترامپ به خبرنگاران اعلام کرد که رهبران هر دو کشور به او قول داده‌اند در این موضوع دخالتی نداشته باشند و افزود: «فکر می‌کنم به آن‌ها اعتماد دارم. آن‌ها نمی‌خواهند باعث ناامیدی من شوند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/VahidOnline/77485" target="_blank">📅 01:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77484">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TndcvBTzPEleCaIA5_BZZl188mv66F01aL2rTH76BKXPtpTr8CS00EtJpJVnnvG4BugOz-9zp4ZFOcQuxbVkxSOq3ev_tdpOx7ZZfgnjyTvMiouEcHC9EAMRXI968QRKC8SPuVkWZbAn7mgSvNfmgOPKVix2siCm4MGHmyAunqGcQ8WjzTbKNmNq06DCg5oxMfAhKO3UOSPT4Ls6DN_-ZQ0Ac6iJutc-y5-xWsMwF51D8KmUfIhmvjaHIBG1WQQiwkZTKYltJVjZO98wMlGhvvlqqJW6JBN8kHe-1iEKr7jqOhqL0K1iOIYJajP4HVSkW2cH2-vtvYi3au3K6lrnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون روز جمعه دوم مرداد در ۶۶ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/VahidOnline/77484" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77482">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aMYvyPFFxR2WQ7sIoxvBcJJqKN3-1_JsQ2sjyqE5Msgy_jBYEMS1EtbMo1_paGH8Ur9bJcenK_luRG1RwBrx5CrY9ugkALIJZ84J8q0q-9IgjKt3l4kwCmL97HolJ20KHPeAUQ-VN-338jJdEMLXtCx-b6vI2O8Jykji9_3031XFH8-OdBqzM72pjDTjgfsfz77jo8NLhTyPojDnTsPB6Bv4bOyn_LFe3cpzhAukfj_TFm9IiXtBKmsxrK3ltFZpG2VE1LMmlTyihKoHdONiYn-UjH_yzgNl_gKxgr1RQ882TK9Bzrq5nQwg8YPUbLiOGzqapQdRsie2I7E0YzxYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P98e0zLdJokzExb8QJMojNjXLFlo9bF7FJWsBhODGjcYgUv90HrNleZbkkDmnQWP5pixDyaCQ5VRHTRvQbXTQZ2tlIEOVnkZ2ZFEIiLW7yaZXMhswYvjqwyFmzsempWJYmgzM3yQAXfPVJSki2UZ1mb4n392VmsncnAtadOl1wbVbdZbF3lAfecqhKxSMy8oWIPULapqGHQNi19ljToQiESVA7_hRmTlLeqVUAAATolZM5V77cKXuiC_m0la4sLtsDcz0UA4gkZli2VX9co5iw9CSFd-W2K1_YyTcgPU0SQ5xsF9F2DP11HwEkMuIdttQNoTJiwshPrDgJmvO0A_ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده روز جمعه دوم مرداد، از اعمال تحریم‌های جدید علیه ۹ شرکت و ۴ فرد مرتبط با بابک زنجانی به اتهام دور زدن تحریم‌ها خبر داد.
بر اساس بیانیه دفتر کنترل دارایی‌های خارجی (OFAC)، این تحریم‌ها فعالیت‌های وابسته به هولدینگ «دات وان» (Dot One) زنجانی در ایران و چند شرکت پشتیبان صرافی‌های ارز دیجیتال او در ترکیه و امارات را هدف قرار داده است. خزانه‌داری آمریکا اعلام کرد که زنجانی با بهره‌گیری از سبد سرمایه‌گذاری متنوع شامل خدمات مالی، تجارت دارایی‌های دیجیتال، طلا و پروژه‌های زیرساختی، اقدام به پول‌شویی و انتقال مخفیانه وجوه برای ایران کرده است.
@
VahidOOnLine
تبلیغاتی که در کانال‌های تلگرام نمایش داده میشن به خود تلگرام سفارش داده میشن و صاحبان کانال‌ها ازش بی‌خبر هستند.
دیروز ده‌ها بار
تصاویری
رو دریافت کرده بودم که نشون می‌دادند مجرمان تازه‌ای حتی از آوتار خودم برای نمایش تبلیغ‌شون در اینجا سوءاستفاده کردند. ولی من امکان جلوگیری از نمایش اون رو هم ندارم.
تبلیغات مجرمانه رو میشه با کلیک روی اون سه‌نقطه عمودی که زیر علامت ضربدر در گوشه کادر تبلیغ دیده میشه به خود تلگرام ریپورت کرد.
فقط اکانتی با سطح ۵۰ می‌تونه نمایش تبلیغات در کانالش رو متوقف کنه. چیزی
نزدیک به غیرممکن
.
من در
سطح صفر
هستم و حتی نمی‌تونم رنگ لینک‌های اینجا رو عوض کنم چه برسه به استفاده از ایموجی‌های اختصاصی.
این چیزها ربطی به تعداد دنبال‌کننده یا بازدیدکننده ندارند و باید هر روز از بقیه التماس کنی که کانالت رو بوست کنند.
یعنی حتی اگر به سطح یک هم برسم باز برمی‌گردم پایین چون باید هر روز بخواهی دوباره بوست کنند.
با روحیه من سازگار نیست.
خیلی زور بزنم، برای درخواست ریپورت سوءاستفاده تبلیغاتی از عکسم می‌نویسم: ریپورت هم میشه کرد.
از این رو محکوم به سرنوشت مشخصی در این زمینه هستم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77482" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77481">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oXtHMJUYMrct7b7wzv6pRj0uGMotXlrPWaa-59yhTx26O2sJyYTPKdvIvlajXphIM8nx7R_H49TaOBVW5o63jKUHI4YPzh2u9cHg6_-Jz6bftPBSssoemsl_J_-6OMHLsJBvVNB0i4lNOOHripTpkx-SPMAbFUE7KJA53r8f3pc5wkm4obScWgJmnk3uVjo1rIcFNSRSMEY5_emtMFKUNhbYHYe1LBOtPbq12dbYbG0dSfkpaLXJv6YooevAgMipC6guq8vV6vzfCgySL44b1ID_WiXIArVzmJWyfQF1sVIOSASKHJv6TCW2y_aI3mZ-6skfBlgRe2NoY8eBvTswKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رئیس‌جمهور شی، در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت — و این اظهارات شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، حرف او را باور می‌کنم و علاوه بر این، من نیز لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
همچنین، رئیس‌جمهور پوتین، با وجود جنگ وحشتناکی که در اوکراین جریان دارد (روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز برقرار است)، به من گفت که به ایران سلاح نخواهد فروخت. او می‌داند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را پرداخت می‌کنند و اینکه آن سلاح‌ها چگونه توزیع می‌شوند، هیچ اطلاعی ندارم.
بنابراین، دو کشور بزرگی که مردم اغلب در ارتباط با ایران از آن‌ها نام می‌برند، به نظر من، در این موضوع مشارکت نمی‌کنند. اگر چنین می‌کردند، برایشان بسیار بد می‌شد — و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77481" target="_blank">📅 19:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77480">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUofpEChwS5RwFBkkU92sdd02CMcuJiFbhhsUOjCFpE1Dq3at_rDGREsN1yrU2zs39sHu8g9zpiUSHjPY6joA6zwTjTF7ZbktRJ2DHvQbED502hq8lo5fKlT1hoQu4SVTP8nykjs_lak0xiVxHhyhZI3hgPW7Qh0CtVHb2QL6NOnDbXKKC9CQrNn5EVsCCwW3POMcWUQ9TCTKxEZ-moWLpS6v4XjDNdLRS_V5SGccUv4tXJZ7diWGdyH6tmxIELiqoMPlGmO0_4llYcQ8gc7v6XDEilLRC4e0MlxV8Qfk_g-StfM4T7BQQ5N-12C-5lBvpYsONkmlN6ND8chZ5XRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای اطلاع‌رسانی دولت روز جمعه دوم مرداد، با صدور بیانیه‌ای از اقدام سازمان صداوسیما در سانسور بخشی از سخنرانی مسعود پزشکیان در روز ملی صنعت و معدن، درباره اجازه رهبر پیشین جمهوری اسلامی پیرامون مذاکرات، به‌شدت انتقاد کرد.
در این بیانیه با اشاره به سوابق مشابه، از جمله پخش نیمه‌کاره مصاحبه رئیس مجلس شورای اسلامی، سانسور سخنان رئیس قوه قضائیه و پخش نشدن مصاحبه‌های وزیر امور خارجه در طول جنگ، رفتارهای صداوسیما «گزینشی و مبتنی بر سلایق سیاسی یک جریان خاص» توصیف شده است.
شورای اطلاع‌رسانی دولت تاکید کرد این اقدامات وحدت‌شکنانه دقیقا پس از پیام رهبر جمهوری اسلامی مبنی بر لزوم «وحدت کلمه» صورت گرفته و نه تنها شایستگی این سازمان را به‌عنوان «رسانه ملی» زیر سوال می‌برد، بلکه تهدیدی برای امنیت ملی و انسجام اجتماعی محسوب می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77480" target="_blank">📅 17:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77479">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bon5_c7cdI529RPGXdkk5SJ3wvry7NOGW82jEMgcdunlaLTaKMeHkBPtC5PCllF_bn9cHVnZmNlKjkxtQMyDJGktSu1TcozpWH28DMIWwGn9pfMF9TAiietZwRDB330O1G0NzDAGT5xoKtjKo1-Tvn59TzXhTC6-UlAspAucfGbPDOtEbmj3Hr-6ryjjG-s4_aDyWjbvg8Yf7iAW2viMgC4k9vdGJ0MZn2iwTa7NDy7jHMS5gSi7gSilw87FdzzeSI-XcNd1c8SvZsYJXIBbIqoiPXNGRzg148ofE7Q0G-kn_fmk-HtyorrxRAzaBLtV6dB3dpPoo7P3rZa-8EYJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین (شاهان) علیزاده آذر، زندانی سیاسی، با اتهامات سنگینی مانند «توهین به رهبری»، «تبلیغ علیه نظام» و «سب‌النبی» به دلیل «توهین به آدم و حوا» روبه‌رو شده است. او دی سال گذشته نیز بازداشت و به «تبلیغ علیه نظام» متهم شده بود.
این شهروند ۳۸ ساله و مهندس نقشه‌بردار، با قرار وثیقه آزاد شده بود اما بار دیگر در ۱۳ تیرماه مقابل منزل خود در اسلامشهر به دست نیروهای امنیتی بازداشت و به زندان تهران بزرگ منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77479" target="_blank">📅 17:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77478">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwFRJdkAEcIs_36O6WzxF3LNgNRXwHTtZ62xG-msamWaQZdm0MWrXmhNaEhMG47_8qeLkqczhyvR2i69bHCStDNoNjafUTSHnw-AlKiYeVNyfDGi9HKooZviVgQyEhmZt5oG12LcRis5gAu-QpqgU-Xbm5hO1BEXUje67tGVO9lUdKFx-WCRFGrspbKka60Zm4yHmjq8ChcHOUyJfqmWE4gYAXcsH2wdN3kXKFlE4e8RdQygAhx2-QekTPEoypSwqB3rAJxIgUQ5qPe4y1rMiIVFk5o3fhe0ijELlFpnm38hWjeVqVNc3JfYJBt76AmMZjtLqH51Mqh8eRViBodkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی وال‌استریت جورنال روز جمعه دوم مرداد به نقل از «منابع آگاه» نوشت که دونالد ترامپ، رئیس‌جمهور ایالات متحده، در روزهای اخیر نسبت به این‌که مذاکرات با ایران بتواند به صلحی پایدار منجر شود، بدبین‌تر شده است.
یک مقام ارشد دولت آمریکا به این روزنامه گفته که «ترامپ معتقد است تنها چیزی که ایران می‌فهمد، فشار نظامی است» و افزود او در برابر تهران در «حال و هوای انتقام» قرار دارد.
این مقام همچنین گفت رئیس‌جمهور گزینه‌های مطلوب چندانی جز ادامه حملات نمی‌بیند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77478" target="_blank">📅 17:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77477">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLP4mPTfVy1kSVy0ACdgt4bhpYV_oHm24Ci0JcQCVe1buKIH10TLx4Sv35vgcMtp-RWrqw9LKV3DALCfXa6eVl2ZCjwzizCgViekR4poAMRLjZyx5tinrlp9-tm5Cq2oN8bCPQPV1MNsSw78n7Prg2_5WGukOYSoe_nkTNwiZuJF6Nix_A-5SmL9LUJ7LlY-etDag_jRvX6KtuF2LBS6SAndClOTYyeM5XoOAVkC1VkV5dsmQkPG2x2UkaW1SwODN91wmR0Tcz3YH2O4rU-0dYO8ysH6zN8xbwz_K6CoN09BzXKxC3-V7Xj2rXdG1rfJ9c-VsT7iUUBa7F_lAOGKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت بریتانیا اعلام کرد نیروهای مسلح آن برای حفاظت از کشور در برابر هر حمله‌ای آماده‌اند.
این موضع پس از آن بیان شد که سپاه پاسداران انقلاب اسلامی هشدار داد نباید به بمب‌افکن‌های آمریکایی اجازه داده شود از پایگاه‌های بریتانیایی استفاده کنند.
سپاه در بیانیه‌ای در روز پنجشنبه اعلام کرد آمریکا از پایگاه فرفورد در جنوب‌غربی انگلیس برای انجام مأموریت‌های بمباران علیه ایران استفاده کرده و افزود هر پایگاهی که برای چنین حملاتی به کار گرفته شود، هدفی مشروع خواهد بود.
اندی برنهام، نخست‌وزیر جدید بریتانیا، هفته گذشته در جریان این خبر قرار گرفت که لندن بار دیگر به توافقی با آمریکا برای استفاده از پایگاه‌های بریتانیا در چارچوب آنچه «دفاع جمعی از منطقه» خوانده می‌شود، رسیده است.
یک سخنگوی دولت بریتانیا گفت: «نیروهای مسلح ما آماده‌اند از بریتانیا در برابر هرگونه حمله‌ای، چه در داخل خاک کشور و چه خارج، محافظت کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77477" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77476">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htegh97GqUGNUjLTFMccmgqQLcLvcsWgD00-dEW8jdwhVh7v238GPBvG0xJ3SwKFMjHhDIWbbprTj1k9k6wXAdBhqFm8OI51fSjx8jPcam4L0zFGuQ9Bmoksby4GLDdeXumBI4WTnynCSBLi0zXc0J85IK4dm1ODsvV0wXWSyapeV46lpRs758fgCMqHSV9XTanEO_P5qpZnaxgsKu9a4BSTtFfJT2NGTvGERQSH_qs7XJezjEBm7Q40qzRhWPq3nX7rL9S3IWwH2RHzW1Tz7RXI_RoDdb1NADfgT6JFFXgi2ArF21hXyEBgL66DSzX1dheZMndsOHUqlTD64pv8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران روز جمعه ۲مرداد۱۴۰۵ با انتشار بیانیه‌ای مدعی شد در جریان عملیات موسوم به «نصر ۲»، ساختمان باقی‌مانده مرکز داده‌های شرکت آمازون در بحرین را هدف قرار داده و منهدم کرده است.
سپاه در این بیانیه ادعا کرد مرکز داده آمازون نقش اصلی در تکمیل اطلاعات ارتش آمریکا را بر عهده داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/77476" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77474">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XDD__vS-ljQEF63meh8yb7J7YYaj4w0550-kv178irJTWDk382Vu_CH82Np5C9qW_J-wh2Mca0mdU-qITZ7ZOGuH-q3KwuXNJC2TJ3WpwEq5UVk1is7UCgt4A5GtUSkhh6vySg-WFaS_i6n8-8pfxVrIytt3bX_ThtlIGdqWnStDE1tY1_vdh8I5wbm0jHhrnvSY8Oz6eHDZgQSx87BdRdkIYy4lT5lU_76qt9B1Kp3bnuPU4NLLI1SDKmN4thNq0yZeC2tGZfG2rtf64UtdLA7PuNdPhP7RjTFIkvaopB6bhpvAiCE-hbSxC2k9pMPRfedSwsyOuGx9dpLlA9yPUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CXTyGZSnYrzmq4Z0h32dXRkknLe5SGpx0Sll1K8PGoR9t5iY22zNHYRX4Bghv-YsSmf1UtmbAPeQuvxwZLbfKKRhG8d2V0lyfNx0Lns5CxMHzLuwrYQae9aq8OD6f7OCNIjkpzqFHQRy2e72a7WnfegXThuplt9PXXqGNpfDcCUfOwkdBmRcqfH4CZk0ejpK5TAmfgpUpL1TqLAkEMF6rQTuQUZBnm4jcvhzvpkF8Zr4RiaxtKehMNHtzDzn9p0q059zgpx8m4QCCN-qR9MVcdLXztAXJPLPXo3Av96YchZLdcx8eGjFKHbk9XPlVMutX8mGpsYYhcjxcZ0qxH622w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه نیویورک‌تایمز به نقل از چند مقام ایرانی و عراقی گزارش داد که جمهوری اسلامی ایران پیشنهاد آتش‌بس از سوی دونالد ترامپ، رئیس‌جمهور آمریکا را رد کرده است.
بر اساس این گزارش، پیشنهاد یادشده در جریان سفر علی الزیدی، نخست‌وزیر عراق، به تهران به مقام‌های ایرانی داده شده بود.
آقای زیدی در جریان سفرش به ایران از جمله با مسعود پزشکیان، رئیس‌جمهور و محمدباقر قالیباف، رئیس مجلس شورای اسلامی دیدار کرده بود.
جزئیات این پیشنهاد آتش‌بس مشخص نیست اما مقامات ایرانی به نیویورک‌تایمز گفته‌اند که این تنها پیشنهادِ روی میز است و آن‌ها علاقه‌ای به توافق موقتی که مسئله کنترل تنگهٔ هرمز را حل‌نشده باقی بگذارد، ندارند.
@
VahidHeadline
دفتر نخست‌وزیر عراق گزارش روزنامه نیویورک‌تایمز مبنی بر انتقال پیشنهاد آتش‌بس آمریکا به ایران از سوی علی الزیدی، نخست‌وزیر این کشور، را تکذیب کرد.
دفتر رسانه‌ای نخست‌وزیر عراق روز جمعه دوم مرداد در بیانیه‌ای اعلام کرد ادعای مطرح‌شده در گزارش نیویورک‌تایمز «کاملاً بی‌اساس است و هیچ ارتباطی با واقعیت ندارد».
دفتر نخست‌وزیر عراق در بیانیهٔ خود مشخصاً گزارش مربوط به انتقال این پیشنهاد از سوی آقای الزیدی را رد کرده و درباره وجود یا عدم وجود پیشنهاد آتش‌بس آمریکا به ایران توضیح بیشتری نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/77474" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77473">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0055dbc0e3.mp4?token=Vq5EIqn_mY3AnSXNspT6InyzPiDEubbg4TmguA0hfl92OfkcFETSEz1sjh7JJjn-BGpZYQavEhWq1WPLrDqE8aTkWKAlwxKEEal21WLwMAt_7nTZ-9X8AnOll7KMO1Jqw80ZKNmQE5eaAx4tjxmouH-Pdmh-l_6cmKVVJ5Pw-q4pl_PilYKVs5vxX2i0siUnXNVSeuYbzVfcu2vzfkQdVDutT7FoGMXgnssAxp1RHdh-_zkSK3z9FXInzoQjQ-uUBmlGC8bkYoGay47L5oBR6l2hiY5wldTQyXAFX8Ew0hwef0k9dTpQq6Rh3a-d-4DHR1zw8CH1PRmBlPDlbmfeAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0055dbc0e3.mp4?token=Vq5EIqn_mY3AnSXNspT6InyzPiDEubbg4TmguA0hfl92OfkcFETSEz1sjh7JJjn-BGpZYQavEhWq1WPLrDqE8aTkWKAlwxKEEal21WLwMAt_7nTZ-9X8AnOll7KMO1Jqw80ZKNmQE5eaAx4tjxmouH-Pdmh-l_6cmKVVJ5Pw-q4pl_PilYKVs5vxX2i0siUnXNVSeuYbzVfcu2vzfkQdVDutT7FoGMXgnssAxp1RHdh-_zkSK3z9FXInzoQjQ-uUBmlGC8bkYoGay47L5oBR6l2hiY5wldTQyXAFX8Ew0hwef0k9dTpQq6Rh3a-d-4DHR1zw8CH1PRmBlPDlbmfeAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون سیاسی و امنیتی استاندار گیلان از حمله موشکی آمریکا به مقر نیروی دریایی سپاه پاسداران در زیباکنار، در صبح جمعه دوم مرداد خبر داد.
باقری گفت: «حدود ساعت ۷ و ۳۰ دقیقه صبح جمعه، بخشی از تجهیزات مستقر در این مجموعه در حمله موشکی آسیب دید.»
معاون سیاسی و امنیتی استاندار گیلان همچنین افزود بر اساس بررسی‌های اولیه، تاکنون «هیچ‌گونه گزارشی از تلفات انسانی» دریافت نشده است.
@
VahidOOnLine
مدیرکل مدیریت بحران آذربایجان‌غربی اعلام کرد حوالی ساعت ۹ صبح جمعه ۲ مردادماه، یک نقطه در شهرستان پیرانشهر هدف حمله هوایی آمریکا قرار گرفت.
پیشتر اخباری از حملات هوایی و موشکی آمریکا به اهواز، قشم، بندرعباس، تهران، امیدیه، اندیمشک، خرم‌آباد، خنداب در استان مرکزی، نایین در استان اصفهان، تفت و شیرکوه در استان یزد، فیروزآباد در استان فارس، کنارک و زیباکنار منتشر شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/77473" target="_blank">📅 17:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77471">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqwKXg5h_uk3RHIeTyILqG-RF0grxt3AZ4oT9njOltR8MQlpHe4i80CDiqwdn0_1NpGRwLYYaKW5K4RvMq5Q2OBIacd_RIzDwY_MlcS5DqjV3CLUzOnRYDsP3fKKOSLfGA5BQdhWtMGh61FA-TQ54UEC2uGZteBqr0novrZF4lqAvNR5-Lgby4eo1u7XuDJ1WPHFZQ9g0aoXvFuoGVwKt-Uq7mIk7_nrgtA5cCKZpaIWvkGWO0clYh4G15yljTWS4x1UgQ2iTr6Rn_DHsk5HPrk6S-0HZnNgp6-K0zeyJih5bbKIQRceRwqbe9083BuRZZqMus8EY_21B6kyNygH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u36brCeuPbn4EGeeIdFj5lsqv36rVIXTyA08bgdfTSrlt2pVtWzu6ewQnVhz8eYXhH3OMrlymM9Ayg3PADosQGr1SbMLxGkNAF-yc2eonq-AaZVEPE_2YieyCbUIigj_Cvozj_lrCBSH_9drj4BIXIKdfAqxuUi1_292fyaCamPaNby8gT9ZexK_j7clvezGw_luyC3_4c8xXXeFKsNOKxYKG1baFnwHg2NVOnYOsWCkJzuJJz5E-5M0zZzGV11Hm0rI8_fTp2SmWYetLKAFJ_C2VUGRuIXh0tarWEUnghCxa55xvDa6EhAKpdsPTIpbMmEx2tFwm2pmeFz0qxKg0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عفو بین‌الملل روز جمعه دوم مرداد از مقام‌های جمهوری اسلامی خواست که فوراً هرگونه برنامه برای اجرای حکم اعدام بنیامین نقدی، ورزشکار، را متوقف کنند.
بنیامین نقدی ۱۳ دی‌ ۱۴۰۴ در شیراز در ارتباط با اعتراضات سراسری بازداشت و به‌مدت ۵۳ روز به‌طور قهری ناپدید شد.
رسانه‌های دولتی ایران یک روز پس از بازداشت و پیش از برگزاری دادگاه، «اعترافات» اجباری او را پخش کردند.
این ورزشکار بعداً در ۲۲ اردیبهشت امسال به اتهام «افساد فی‌الارض» به اعدام محکوم شد، با این ادعا که از کپسول آتش‌نشانی علیه نیروهای امنیتی استفاده کرده است.
عفو بین‌الملل می‌گوید که حکم اعدام برای بنیامین نقدی پس از «محاکمه‌ای به‌شدت ناعادلانه» صادر شده است.
این نهاد حقوق بشری با استناد به الگوهای پیشین مقام‌های جمهوری اسلامی ایرانی در گرفتن اعترافات اجباری «تحت شکنجه و سایر بدرفتاری‌ها»، ابراز نگرانی کرده که «اعترافات» بنیامین نقدی تحت اجبار گرفته شده باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77471" target="_blank">📅 17:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77470">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2OSwxsphK6JWXfb3N-p2AaTELOGm7CJs6KnuDUKpOfOsX8j9dmLg2U95YzhP2WDGug8yZCy_GFbalIABOkKbMS0O9nroC4G7hOb1zixzfIhXsQBAV_D72xfMbgwU6zJN62T84Ldgaz0gam6tBjCFWxzGkl-F2MEJm0k4Q4J_o9tRRO2CrPIgSoIVOAjLDSPYw1-emaNObTt7r05OAOGO8FvQvUaZ3ZDY6jOQaPo9rcB0S1b7TbPB2WesU3L-bTsvKJwzP5gprrD63S83GWB7mg39PNUhTB7zI3lue4M3afk5RE9_AJUoKrULopesBAFUJeBTHBZCKcsfSFLo3xwww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته بود:
از این پس  خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
واکنش عراقچی، ترجمه ماشین:
مصادره دارایی‌های یک کشور دیگر برای پرداخت مطالبات نامرتبطِ آینده، بدعتی آتش‌افروزانه است.
کسانی که از چنین منابعی استقبال می‌کنند یا از آن سود می‌برند، باید به یاد داشته باشند: وقتی دولت‌ها مصادره را به امری عادی تبدیل کنند، دیگر دارایی هیچ‌کس در امان نخواهد بود. هرج‌ومرجِ متعاقب آن نه زیبا خواهد بود و نه مسالمت‌آمیز.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77470" target="_blank">📅 06:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77460">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u8S9YALhdBVK-apVopRePOqTdqqkDgI9iEDRzL8A5Nee44lcw6gLXk3snNK2KJ_ppZ553dyEeXzIJFaoFYL_VpUBUC0J2jMqd7jbzSVfKLTKr9CkpvHLt2NMLHr-ExMEYlbV3NKroK7iOzBcCY98B9rIEGLknybLMKpU77flMGFXrv5oXhWfan7Mjr_MOzrmJ3Z3RFBik7AB3cseaoWp-X570Y5eHjYWhbaYArlmBHqPMvt6C3POEPlY8WEzDlSv7CYLT3h4xr3RmrMjahnxY1IEPb1aWM3NFikXf6xe-1weMZ_RAaEy7k9ivHI9sUg_ACxQbC0GscFBj5-Y8bD3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QjxSCbJ1cG5FUHiQmJBnoNjt-Eeb38OpYtgze_1IebKWU0wB5_KSanIOP62OJassCd9LHRmJ1PtUkHyWYJ3kf4mqYAtsY3edPJGQ6uzyWOBS60diK28eNarQHJ44_Eq8rg66abZqx0bss6KVa7nRNl7_MkbCJa0ttnS_BgEGTGd1ieRwvLQN_lWEcr61aDqk4DwIX-NoSXkGPyRnB0-y3fPrOLsZSRBCj5Io6nSDIZqHrSzmp0_wr0l0wE2AOQRY9twQw19FYJrfjJ-LIeRXgaj7oxk-II6UcnQ_Q2j8zzzaqfxQv7M6qOTjmYGwi9odeMje3dGQ7yfodgVLM_RA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uA3fd1QuiImiV1Elf7wenXgjN8vuzuTX2h1Yvd1psiS0bRlBpMn98ECWlMtJM6AIYcatrfRRebU2ood6Jd5ObupaCDZToOxsZMsnRhiNOXa1s_SJg2_zXNlWA2YLYW8U5WkbZGICcrcT7WntpzSQVATe_0GkUE0mRuVCOODwWsacemQUhMta9mEN8DyhTIe96xspowTbX2G_gKlB4v8GlK5GlpiKA45dFfsIRom4AanJFgnYb6xZ4WROeM5a6b3Mx-GhH-uBKD1qUZ_Uv8GapWgGtwf6scxf7LQA0H5e6K63DlJapJBEvqkOF-TrAP8O8iCPR4ltjZUkERkSzYA3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BtoxMDdisan8xWX1-NmrWMFpnEOgZfRFkP3B6z-ciT8Cq7csdOM6Lep6xDZDZC1hvK_QHJa9nBiYJ9HfIQP5CEELeHM13n3cIQZ-HS0YmDkHNxDFxG4d9AFb23kiztVTkaKemUTzcQkrT5Hp_ztmFnCDg7BvqxIE63RsvoO9m8wCLM51ZQV_08QnfYrCn4Nnb2GWmGdY8zp0dn-nUS7u6acIJfT-rPgyqa2cJv4x9RGn_43uKmhTO1hlv4YIMbebTNMc7xd32YzILrFeXRrPJZ6Jloa3NAuIsm4kmKrlgRbkcapRrg0_1QOkeddVFXXanMWC_KEvRdlN1a3wG6rBTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hDvGMjKqY9UK5S5B8R7wAQtXD19z4NtaBnghMjt6Jt5XgGMTuw6JdVi7RrC2Ovk8SsOpjWGLMYihri53g2o0shOTlc_gR9nk0DGdTH2ZQvneFXkkH7P5BRIS_q1y_fMe3e4EpBjiCWpuAxoOM_4FzrcSOlDtTKWKyU9zWiHvW9EVdc2Zoalgz01Of65Kgo9Bags4FvekPVuhuigREt5CoxbCJ4FCL3uEWuFUfQ8cG8RyOGL2P5v6LIYVJ7u4sD5ubePwSU7zUmBXfv52tK6qZVr9W5idDmr6NTHpDwGJCQcxpArzAUgi9wsDfIXbkSJqrWx9gxErpngPI8J5huVr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o6kVlEKcx97qTGhxkFcM04gSDI5GoVi8yj9_JI8BtuEle6-SuY1xCTdoJdMjjos5duRh5Z2uzLQERG1zmRQdNBQOeH2zqT0HiOO61f2SaBXcD1cllI9IVRsLVMuOr84ZZ5IUfG6ZgXmTOuskO-8cZZSV7tNDI_XGCT1JFAQSzcVLPI8Ic2wwbHa8ozfSOEO56oq75Q-GLaaHlbXrAFbzT_dgaq21FtkohNhwAqX25X7LfVZ3mhJL_TMa47xWwqSi1cjU_TcEXq4Kfp0eRaiFX89KPtt-Ovi0k1BFP92hMNLovin1gD9Mu6_S69di_XOQ6WrMw0bDzXu7z8xE4izxtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=tvsNyvJg--GLdmZpVAEzuNT-TOWwSSxRPlTgvlilXeEN3UARzH7qc44nkkSj_Md4oXkbjiHL9XuOUmgL5nTqDmAiWVuCol99i_t2biETROz_CS7ZfLSi2JcwRy-1CJ8mNb-EVBpRUGoX6KadnxvzcO_fhjKP5YgfS_PIL5p7VtV1qTA52FsCGYxhMTYWR-vpjQN1-d_vQPGceGDBinP6GE0FhLcxnvTpqM-gpU1U3cRKQvS3X7wSCKHByW4LZ1rqniYxSToRRww5OhJ6BaI_0WKz1VfTwpkfOJWcaKHJiUSMzJS5sFyt13-xY02wewXb9rj4X3o_7qNDzmNpeLRspw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=tvsNyvJg--GLdmZpVAEzuNT-TOWwSSxRPlTgvlilXeEN3UARzH7qc44nkkSj_Md4oXkbjiHL9XuOUmgL5nTqDmAiWVuCol99i_t2biETROz_CS7ZfLSi2JcwRy-1CJ8mNb-EVBpRUGoX6KadnxvzcO_fhjKP5YgfS_PIL5p7VtV1qTA52FsCGYxhMTYWR-vpjQN1-d_vQPGceGDBinP6GE0FhLcxnvTpqM-gpU1U3cRKQvS3X7wSCKHByW4LZ1rqniYxSToRRww5OhJ6BaI_0WKz1VfTwpkfOJWcaKHJiUSMzJS5sFyt13-xY02wewXb9rj4X3o_7qNDzmNpeLRspw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: پرتاب موشک از بیدگنه، خمین، نجف‌آباد، شاهین‌شهر و...
تصاویر بالا و پیام‌های دریافتی از استان تهران:
همین الان از ملارد موشک زدن
همین الان ساعت ۵:۵۲ از بیدگنه موشک زدن
سلام وحید جان همین الان موشک از رو پرند رد شد
سلام همین الان 5:51 از ملارد موشک شلیک شد
از بيدگنه موشك فرستادن الان ساعت ٥:٥٠
شلیک موشک از بیدگنه ملارد ساعت 5:50 بامداد
۵:۵۰ دقیقه از بیدگنه موشک زدن رفت بالا
سلام وحید جان از [....] بیدگنه الان موشک هوا کردند بعد جنگ ۴۰ روزه این دومیش بود
سلام وحید ما فردیسیم همین الان از سمت بیدگنه فک کنم موشک پرتاب کردن و صدای شدیدی اومد و لرزید ساعت ۵.۵۱
5.52 از کرج موشک فرستادن ردش هم تو اسمون افتاد
اشتباه نکنم از بیدگنه
وحید جان سلام.  رد موشک از سمت اندیشه  شهریار خیلی صدای مهیبی داشت همین الان ساعت  ۵.۵۲
آقا وحید سلام ساعت 05:50  از بیدگنه ملارد موشک رفت
سلام. روز خوش از بیدگنه موشک فرستادن
جمعه دوم مرداد ساعت ۵:۵۳ شلیک موشک از [...] بیدگنه واقع در ملارد به سمت جنوب غربی
🔄
وحید جان همین الان دومی هم فرستادن ساعت ۶:۰۰
سلام وحید جان همین الان موشک از رو پرند رد شد
شلیک دومین موشک پیاپی از ملارد
از ملار یکی دیگه شلیک شد  6:00
دوباره موشک زدن از ملارد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77460" target="_blank">📅 05:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77459">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=oYioFfo0aHYfsEGbEtiJX-r2E_4QEWJ1jAqfcZ1wnYKH8pDiza9QmJf1I4j24srgVOvF2aF5NogyyVDEwi_wLBDoROGSejdUA2FtfpkvnGRHGimn3Fq54xumaN0mrJJz0HKB3ZXWewfLJK_Kis3tx1H_0W2Gt5_TlOkU__-r5VhRXx7jERcMEPXuFrVue02kKBCK8w5O4K4cMCCWRIfMZh_ctUvk1Y-tVhyqpEUWkUVvtpvtmdovy5c2k9oOJPGeAWAeMCW4HdZCc1UHjidlGWI1yK3ABCkKgWGfY7lSpYKOLc1LZ0xeolHx3tk7yodsdmdQDR5BQlLsBTXAktBrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=oYioFfo0aHYfsEGbEtiJX-r2E_4QEWJ1jAqfcZ1wnYKH8pDiza9QmJf1I4j24srgVOvF2aF5NogyyVDEwi_wLBDoROGSejdUA2FtfpkvnGRHGimn3Fq54xumaN0mrJJz0HKB3ZXWewfLJK_Kis3tx1H_0W2Gt5_TlOkU__-r5VhRXx7jERcMEPXuFrVue02kKBCK8w5O4K4cMCCWRIfMZh_ctUvk1Y-tVhyqpEUWkUVvtpvtmdovy5c2k9oOJPGeAWAeMCW4HdZCc1UHjidlGWI1yK3ABCkKgWGfY7lSpYKOLc1LZ0xeolHx3tk7yodsdmdQDR5BQlLsBTXAktBrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند"
پست سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۹ شب ۲۳ ژوئیه به وقت شرق آمریکا [۴:۳۰ صبح به وقت تهران]، سیزدهمین شب پیاپی حملات علیه ایران را با موفقیت به پایان رساندند.
سنتکام مراکز فرماندهی نظامی ایران، تأسیسات نگهداری پهپادها، شبکه‌های ارتباطی، سایت‌های نظارت ساحلی و توانمندی‌های دریایی را هدف قرار داد تا تهدید ایران علیه دریانوردان غیرنظامی و کشتی‌های تجاری در حال عبور از تنگه هرمز را بیش از پیش کاهش دهد.
این آبراه بین‌المللی، با وجود حملات اخیر سپاه پاسداران انقلاب اسلامی ایران، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با پشتیبانی نظامی ایالات متحده همچنان آزادانه در این تنگه تردد می‌کنند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه در حال فعالیت هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77459" target="_blank">📅 04:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77458">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان همین الان صدای انفجار خرمشهر
درود خرمشهر صدای انفجار ۴:۴۰
خرمشهرو زدن
سلام وحید خرمشهرو همین الان یه موشک زد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77458" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77457">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان یزد صدای انفجار اومد
سلام یزد رو الان زدن
یزد یه صدا انفجار اومد ساعت ۴/۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77457" target="_blank">📅 04:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77456">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">چند پیام دریافتی از فیروزآباد در استان فارس:
سلام فیروزابادو هم ساعت ۳:۴۵ زدن
صدا اومد فیروز آباد فارس خونمون لرزید
نزدیکی فیروزآباد فارس چیزی شبیه انفجار رخ داد و موجش بد جور گرفت مارو
الان صدای انفجار فیروزاباد
ساعت ۴ صبح
انفجار مهیب
سلام  فیروزآباد در خونه داشت از جا کنده میشد
دوسه نفر  میگن پل احمدآباد بوده که راه ارتباطی هستش به سمت جنوب
آپدیت ۴۰ دقیقه بعد: صدا و سیما
شنیده شدن صدای انفجار در فیروزآباد فارس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77456" target="_blank">📅 04:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77455">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت 3:43 صدا پدافند شرق تهران اومد ولی کم بود
ساعت ۳:۴۵ صدای پدافند شرق تهران فعال شد. از حکیمیه صداش میاد
پدافند شرق تهران فعال شد
سلام صدای انفجار در پردیس تهران [لابد انفجار شلیک‌های همون پدافندهای ضدهوایی است.]
الان هم پدافند زد
پدافند پردیس فعال شده.
شرق تهران صدای پدافند
[+ پیام‌های دیگری که با تفکیک اسم محلات مختلف شرق و شمال شرق تهران دارند فرستاده میشن و دیگه نقل نمی‌کنم چون همین محتواست که هی داره تکرار میشه.]
آپدیت:
بعد از چند دقیقه تموم شد.
🔄
ساعت ۴:۱۰
دوباره صدای پدافند شنیده شده در شمال شرق تهران
🔄
ساعت ۴:۲۲
پیام‌های دیگری درباره شنیدن صدای پدافند در شمال شرق تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77455" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iv8Z2PmRAyjIrJyLUKFID9qgxtZ36uShZgVunGAn8JeF-xWCS7QKtQzIMVeeB--jz7_JcqPJYRjLDIloVr9_lhgu45itDADwypDeVqs2ObRxiZed8Lf07Wj813zTpEigyuC7wxnHKdJQLAyYVWlRbH46hcQsM80lHL5wO-X8kvTk810Qn31hQ3HsLvdUSPnvauYTrfRE5a17I0BcsYmovTrqwc02yzX5nLSUW6GiV0tlkFvvS53a22zqVmEm_mpzjISv2bUjfGyh6QYYQllpPkIeBrHHxgXLd5VIU2WWKhvRpX8Uvp_zEtTXBPBXFy7PKXqLmRTNa-lZL47MdZKSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: تفت در استان یزد
پیام‌هایی دریافتی و تایید نشده درباره مناطق مرکزی کشور:
ساعت ۳.۰۵ دقیقه شهرستان خنداب صدای انفجار خیلی بلند اومد
سلام خنداب و زدن 3:05
نزدیک خنداب صداهای وحشتناکی میاد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استانداری مرکزی گفت: یک نقطه در خارج از شهر خنداب دقایقی پیش هدف ۲ پرتابه دشمن قرار گرفت.
———
سلام وحیدجان همین الان پایگاه نیروهوایی انارک نایین را زدن
آپدیت چند ساعت بعد: منابع حکومتی
معاون استانداری اصفهان: ساعت سه بامداد امروز منطقه‌ای در شهرستان نایین مورد تجاوز دشمن متجاوز آمریکایی قرار گرفت.
———
تفت از یزد هستم
از سمت بام تفت - شیرکوه رو بد زدن
خیلی صداش بلند بود
ساعت ۳.۳۰ دقیقه تفت صدای انفجار امد.
دکل تفتکوه رو منفجر کرد
سلام ۳:۳۰ تفت استان یزد صدای انفجار مهیبی اومد که از خواب بیدار شدیم. از کوه های اطراف نور و گرد و غبار شدید بیرون آمده.
داخل شهر نبود
سلام وحید جان .ساعت ۳.۳۰ تفت یزد صدای انفجار شدید اومد و خونه ها لرزید.
صدا از تفتکوه محل منطقه گردشگری در حال ساخت بام تفت بود که از اول جنگ کلیه نگهبانان و پرسنل را سپاه تخلیه کرده و هیچکس اجازه رفت و آمد ندارد
خبرگزاری‌های محلی میگن موشک بوده و جنگنده اصلا صداش شنیده نشده
آپدیت: صدا و سیما
صدای انفجار در خارج محدوده شهر تفت در استان یزد
———
بروجرد انگار زدن صدای انفجار اومد. دو انفجار پیاپی
بروجرد زدنننن
صداش وحشتناک بود
بروجرد صدای انفجار شدیدی اومد
دو تا پشت هم
آپدیت:
در بروجرد فقط صدای عبور جنگنده شنیدم
اما صدای انفجاری نشنیدم
از باقی همشهریان هم پرسیدم نشنیده بودن.
صدای جنگنده شبیه  جنگ ۴۰ روزه بود که بعدش خبر بمباران خرم آباد اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77454" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs2r6eibGRTEbPH15OU-CfMU5i5OqQbmHJUSzWV9-7VwXncLU0pOF5-AKbY4l9FMGT5WifVjsUYOCqIyZHyVxBmks35I6_hBZhO4Ux2b6nbygdwc6VI2M8o5OHTnne7FXoBDoNPBnMq_eF9ktwJsV13V24CXwMH6RO-tHSPs4v2d8DyxOtzQUh1BQlwlTTjHMnai3-eex3cwHQ4KWu7Icnhxqk_4sAkjmjjKfh1NiX-GmJaHbJscNXu7bYdwTGruzThF9ctEoFQojxxRzghKaPQ7uWViywfyyDsUbKUhh6L1lfoaOGi-uAXJxxtwhN4Q0f4ucocj2YGREy0-7BsO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، معاون امنیتی و انتظامی استاندار خوزستان اعلام کرد که ساعت ۲:۵۰ بامداد جمعه، نقاطی در اطراف شهرهای اندیمشک و امیدیه هدف حمله موشکی آمریکا قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77453" target="_blank">📅 03:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77452">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام‌های دریافتی:
خرم‌آباد ساعت 3:19 دقیقه صدای انفجار شدید.
خرم آباد الان انفجار شدید
همین الان صدای انفجار خرم اباد ۳:۲۰
سلام خرم آباد همین الان ساعت 3:19 دو انفجار شدید
سلام خرم اباد وحشتناک پنجره لرزید
خرم آباد زدن یه حالت لرزش هم داشت
خرم اباد وحشتناک شیشه هامون لرزید
سلام همین الان از خرم اباد موشک پرتاپ شد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استاندار لرستان گفت: یک نقطه از شهر خرم‌آباد دقایقی پیش هدف پرتابه دشمن قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77452" target="_blank">📅 03:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KUH8i6_5blVyK_bP09ppM41FosTTlY_nwnO8rsHYCGTcU5yX3Et-a9SrhyFUtQ-2Kga6V7-FP3w-GIKQCiIX03aHQNUuybvvdmUaoaDSJnA-3opfxudRv8IGfusALGt0Ne0PIqswkgurZNZIEkLbdYlyaWVqQGMZUYoXS6GNQ8Zt9P07F_wxiIY0CBegvAUJ6hMqRXiR4A7XkXvjr2zQSjpwzoBVEs6IOTpKs5fcSqil9z00v6VrViwTxm22JvlreQAAOAOtQd64um7yjUDKcgCnnlKsXRG34gR-TpYL1Ko-qJqGx1j3wivCZ1hd3NaZruv22gYL-RgrvDd79dylyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77449" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gPyD4-w42je2L1Xdr3uEfrJG3IE2Q--xMCdIQoJ53AvbFlusLribAHVX5LEEutG4q6HhoxegSmom1jUp-6bC4Ppv4em1Xp0yRqF7VWbvP1vjyP05PKDsfWa0la0x4n6IMh8tRlBxEvxHOKFt55MOQVbAnq9RbgIz2idpZY1GQBDVfRF5gkm7alETTz_H-p4J1DUVyr3APS07w3RMIeuWDGgVii6z917GsV25uXXxn1qRaDOZPhHalsCNOKwIt_uukHvgf9U-qTUKD5t7U0mFBueKMqYHJZxFcleixj9XwLlb2UmPjz4Gm-RyyDTfwAPwJRTxa4ocf4LZaXAjEJybog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: سیزدهمین شب حمله را آغاز کردیم
ترجمه ماشین:
نیروهای آمریکایی امروز ساعت ۶:۴۵ عصر به وقت شرق آمریکا [۲:۱۵ به وقت تهران]، دور دیگری از حملات شبانه به اهداف نظامی ایران را آغاز کردند.
این سیزدهمین شب متوالی حملات است که با هدف پاسخگو کردن ایران و کاهش تهدیدهای سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77448" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=XOcDpdDVA04EZnExX6Od4pwZ1Ej5tlgrtPNC6Ea7pJXLWJc1K83vXnHcqqTpcJxzbcDIdaWMeKHcLSa2j-lm1aqmmZ4XIfq1a4WdBt-_3rH-oMtUlX9U0DdndJr9lu8AawGJORE6xGhqRHVrgQ1e-8EcJFpp6GY9ivSBYQkB5jUFs6beDC7fVydu-KVvtikb5WDZ6dp38k7lko1S-WMBJUat_eIT2_lJijRk_83NwELIJQKv_cs8YvpRLN8Y-Z1EkjC0IKEZL77-dwf-otW9omjiRIBE8gu2ovWPAAPg-fSx0muGk9ZAMWceVdlbiMzuyui7Z7LMKJVTiWffcOIM6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=XOcDpdDVA04EZnExX6Od4pwZ1Ej5tlgrtPNC6Ea7pJXLWJc1K83vXnHcqqTpcJxzbcDIdaWMeKHcLSa2j-lm1aqmmZ4XIfq1a4WdBt-_3rH-oMtUlX9U0DdndJr9lu8AawGJORE6xGhqRHVrgQ1e-8EcJFpp6GY9ivSBYQkB5jUFs6beDC7fVydu-KVvtikb5WDZ6dp38k7lko1S-WMBJUat_eIT2_lJijRk_83NwELIJQKv_cs8YvpRLN8Y-Z1EkjC0IKEZL77-dwf-otW9omjiRIBE8gu2ovWPAAPg-fSx0muGk9ZAMWceVdlbiMzuyui7Z7LMKJVTiWffcOIM6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
داداش
بندر
زد
همین الان
بندرعباس
سلام بندرعباس همین الان صدای چندتا انفجار پشت هم اومد
ساعت ۲:۴۱ دقیقه صدای انفجار بندرعباس
سلام بندرعباس انفجار های شدید پیایی غرب منطقه ۴
بندرعباس 2 انفجار
سلام وحید بندرعباسو زدن 2:41
بندرعباس ٠٢:٤١ يه صداي انفجار خيلي بلند كه مركز شهر  قشنگ حس شد
سلام بندرعباس همین الان چندتا زدن خیلی بدد برق قطع شد صدای انفجار بد بود
🔄
بندرعباس صدای انفجار بلند ۲:۴۱
2.42 چند انفجار بندرعباس پشت سر هم سنگین
3تا دیگه
٠٢:٤٢ سه تا ديگه پشت سرهم
صدا و موج زيادي داره
سلام وحید بندرعباس انفجار وحشتناک
دوباره داره میزنه خیلی بد میزنه
بندرعباس ۲:۴۲ صدای انفجار دی در پی
دوتا دیگه پشت سرهم زدن
۵ تا انفجار شدید  بندرعباس مجدد منطقه ۴ ۲:۴۳
سلام یه صداهایی میاد بندرعباس فکر کنم صدای انفجاره اما دوره
وحید بندرعباس ۲:۴۲ صدای انفجار بدجور میزنه
ساعت ۲:۴۱ در خونه دوبار لرزید
غرب جزیره قشم
بندرعباس همین الان هفت تا هشت انفجار خیلی قوی داشت
آقا وحید بندر خیلی شدید بود بیش از ۵ تا بیشتر.</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77447" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=RvIevNtSLYzdnsFuq-thoXGiayt6KefmAkPdNDQZa3GYYfbLtpf2oEqHaDusAtcPyxjdM3n-W1O9ULC7cFBzr6gPAI7l7W7OBs0ZgePMqN0uFBObhXtaADd-Flehd8OyYeQ_01ADYmDXGTFrtxKjDMX0hdM02SdQ8dO6nXxg7mA74WVs6lgoGWwxA86iRvQNj7T3w5AEdfLc-qJ0J-FRUuA2ohQQyaXFm6bAnfI5f9Q_Cftlkz4EX7tEB2_2LWQ57dvvpyz0r5t-6kh0wJEDY1bmdz4J3cRmKYSETZQYazpm5g3HweMxkx-2ZmFgC217iWfbnr3tkkiVH6T8B3NtiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=RvIevNtSLYzdnsFuq-thoXGiayt6KefmAkPdNDQZa3GYYfbLtpf2oEqHaDusAtcPyxjdM3n-W1O9ULC7cFBzr6gPAI7l7W7OBs0ZgePMqN0uFBObhXtaADd-Flehd8OyYeQ_01ADYmDXGTFrtxKjDMX0hdM02SdQ8dO6nXxg7mA74WVs6lgoGWwxA86iRvQNj7T3w5AEdfLc-qJ0J-FRUuA2ohQQyaXFm6bAnfI5f9Q_Cftlkz4EX7tEB2_2LWQ57dvvpyz0r5t-6kh0wJEDY1bmdz4J3cRmKYSETZQYazpm5g3HweMxkx-2ZmFgC217iWfbnr3tkkiVH6T8B3NtiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌‌های دریافتی:
اهوازو زدن
شدید زدن
سلام وحید صدای برخورد اهواز
اول ۳ تا خیلی دور بود
الان هم ۳ تا نزدیک بود
اقا وحید همین الان اهوازو بد زدن
اهواز انفجار ولی دور بود
اهواز ساعت ۲:۲۰ صدای انفجار اومد
اهواز صدای برخورد اومد 2:21
وحید رگباری زدن اهواز
ساعت ۲.۲۰
ساعت ۲:۲۵ یک انفجار شدید اهواز
سلام وحید ساعت ۲:۲۰ اهواز رو زدن
داداش اهواز صدا انفجار قطع نمیشه تقریبا ۲  دقیقس پشت هم داره بمبارون میکنه یجایی رو
اهواز ساعت ۲:۲۱ خیلی زدن بیشتر از ده تا
۰۲:۱۹ اهواز زدن
آقا وحید اهوازو شدید بمبارون کردن هنوزم ادامه داره
ساعت ۲:۲۵ یک انفجار شدید اهواز
انگار یه چیزی خورد زمین و ترکید
انفجارش طنین داشت
چیزی مثل رگبار
انفجار در اهواز 2:25
سلام ۲:۲۱اهوازو زدن از گلستان اهواز پیام میدم دور بود خیلی ولی کاملا صدا و لرزشش اومد
سلام وحید جان، اهواز رو زدن
خیلی شدید بود ساعت ۲:۲۲
سلام اهواز شیشه ها کامل لرزید مثل یه باد شدید بود
🔄
ساعت 02:24 مجددا شروع شد.
مجدد ۲:۲۴ انفجار شدید
یکی دیگه دوباره زد
انفجارش موج داره
ساعت ۲:۲۴ یه انفجار دیگه شدید بود
۲:۲۴ دوباره اهواز زدن
وحید دوباره صدای چندین انفجار
اهواز هنوز داره میزنه
اهواز رو پشت سرهم دارن میزنن
درود وحیدجان، ۴ ۵ تا انفجار عجیب در اهواز رخ داد، انفجارهاش با همیشه فرق دارن، با اینکه دورن و صدای کمی دارن ولی زمین و شیشه‌ها رو میلرزونن به یه صورت دلهره‌آوری
سلام اهواز ساعت ۲:۲۴ دیقه فرهنگ شهریم صداش اومد هرچند کم بود صداش ولی مشخص بود بمبه
انفجار ها توی اهواز همچنان ادامه داره
خیلی شدتش بیشتر از روزای قبله
کل خونه و پنجره ها دارن میلرزن
اهواز زاغه مهمات انفجارات پی در پی
اصلا تمومی نداره
۲:۳۲
۲:۳۳
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77446" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77445">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tQyEHBQgNG8LEb6LNvwvYdNP3thfwP7AZjLwwSqGpfFa_qsHvFU_G321iemfsR2rqHcnsL5974TwW5zQiXeZNdhKsE4szzOKb0AvJ6WuQRsb3vwn90iAYgH1qnySLUBY5KMAEspVEkdRiZlKsik7uCgwLNyJLBSj-5LN-0ogrntyYWRBIP16I6fl2hUSovOziMOloEkGt-330u_dJUWgQ1PRashHOTJ7QEkDnXI2YnIo1ygVVFWEkiQGDSHUQSIun1e9VgeXChSkg0G3abU5ROEWitl2kB57F8Y4lBvZtRB9rJes6-rl0vco-lvHJp56RfqcxMIU_mvb8F69vfY7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
ترجمه ماشین:
لطفاً این بیانیه را تا اطلاع ثانوی به‌منزله اعلام این موضوع تلقی کنید که
از این لحظه به بعد، هزینه هرگونه خسارت واردشده به کشتی‌ها، محموله‌ها یا هر چیز مرتبط با آنها، از محل پول‌های ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
این خسارت‌ها ممکن است بسیار قابل‌توجه باشند، اما با وجود این، این کار منصفانه و عادلانه است.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77445" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77444">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NER2Supd3-BHwZddSRbORpq7oGX3egjg6MKg2lU1At9_GcSAvLYCjRFHlWLuYIUuv8jGUryiyElS0iejZgeykNrjAljhTPgV9FWHrVQcPWdqhk0WWWsYpR7lJ3YZ7s286EMMqSFfuITn2ZX3ZLhIPkh_fqJQst0lE4_tD1ep7-s9NXljLFXNVS3rwYGhUI7iOOegsxLz68Xw9DtRHr9_WsYpc_yVIX4WQcTLQVf8UeCEgCeT-0mrj2mLZRQT_LjeIn1IN0eqquNf_YyJzryDR3yI7YpN5_-IiOpeDGnA3HKTb7TSD2M03fzF5n_TQRrd-AJ5SqVE1b-MYoswG_94Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم: اصابت ۲ موشک آمریکایی به محدوده روستای مسن قشم
گزارش خبرنگار تسنیم:
🔹
ساعت ۲۳:۵۰ دو فروند موشک در جریان حمله دشمن آمریکایی به محدوده روستای مسن در جزیره قشم اصابت کرد.
براساس اطلاعات اولیه، این حمله در محدوده روستای مسن رخ داده و دستگاه‌های مسئول در حال بررسی ابعاد حادثه و ارزیابی خسارات احتمالی هستند.
من یک پیام داشتم ولی اون رو هم ساعت ۲۳:۳۳ دریافت کرده بودم:
سلام وحید جان
ساعت 23.30 صدای دو انفجار شدید  ذوالفقار قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77444" target="_blank">📅 01:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77443">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77443" target="_blank">📅 00:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77442">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=ScYnV6Ub0Wi_781WLZQ4zmDll6FhjxVXJUQVCQxyCF9EdOMdqspsff3_EdnIucQ8AQe-iV4r6QuXNQ0DEPUOm_8vp_ia1Yvr78lXSyzvZHbuFJMa6I34u8oepvdLRg4EnD7IuPNICWhJqSvAjnVBjEWOOisCdF49zJ_aupcV1mvKDRmbee8LLasBqYaH79Q0ACyiVReuHIfhDsrG9XjT5NjWCITdhTT-k5y6cvRWpr901e8pSAmhQA59oYy8zNlGvzCoMJL-Ca6uPH1UVMu1EzDRWPhuVKpvQqCDY8E-pThPdk-21TuPDM91YQw_CcJC6vAXjqSWrg-7OihKe7LBwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=ScYnV6Ub0Wi_781WLZQ4zmDll6FhjxVXJUQVCQxyCF9EdOMdqspsff3_EdnIucQ8AQe-iV4r6QuXNQ0DEPUOm_8vp_ia1Yvr78lXSyzvZHbuFJMa6I34u8oepvdLRg4EnD7IuPNICWhJqSvAjnVBjEWOOisCdF49zJ_aupcV1mvKDRmbee8LLasBqYaH79Q0ACyiVReuHIfhDsrG9XjT5NjWCITdhTT-k5y6cvRWpr901e8pSAmhQA59oYy8zNlGvzCoMJL-Ca6uPH1UVMu1EzDRWPhuVKpvQqCDY8E-pThPdk-21TuPDM91YQw_CcJC6vAXjqSWrg-7OihKe7LBwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش‌هایی مربوط به ایران، ترجمه ماشین:
ما در برابر جمهوری اسلامی ایران بسیار خوب عمل می‌کنیم. عملکردمان فوق‌العاده خوب است. آن‌ها دوست دارند کاری بکنند، اما من می‌گویم هنوز آماده نیستند. به مقدار بیشتری از همین رفتار نیاز دارند. هنوز آماده نیستند. نیت‌های شومی دارند.
نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند. اگر همهٔ این کارهایی را که درباره‌شان صحبت می‌کنم، از جمله کارهای مربوط به مراکز دادهٔ شما، انجام دهیم، مگر این موضوع مهم نیست؟ وقتی شروع کنند جوامع را یکی پس از دیگری نابود کنند، نمی‌توانیم اجازه بدهیم حتی به داشتن سلاح هسته‌ای فکر کنند. دقیقاً همین اتفاق در حال رخ دادن است. در دوران من هرگز سلاح هسته‌ای نخواهند داشت.
ضمناً، این کار باید به‌دست دیگران انجام می‌شد. تقریباً سه سال است که می‌گویند ۴۷ سال گذشته، اما این کار باید ۵۰ سال پیش به‌دست رؤسای جمهور دیگر آمریکا یا کشورهای دیگر انجام می‌شد. لازم نبود ما این کار را انجام بدهیم، اما ظاهراً اگر ما انجامش ندهیم، هیچ‌کس دیگری هم آن را انجام نخواهد داد. من انجامش می‌دهم و هیچ‌کس دیگری توانایی انجام آن را ندارد.
ما در دورهٔ نخست ریاست‌جمهوری من بزرگ‌ترین ارتش جهان را ساختیم. کمی بیشتر از آنچه فکر می‌کردم از آن استفاده می‌کنیم، اما اشکالی ندارد.
ونزوئلا را داشتیم. کریس در آنجا کار فوق‌العاده‌ای انجام می‌دهد. هزینهٔ آن جنگ را چندین و چند بار جبران کرده‌ایم. میلیون‌ها و میلیون‌ها بشکه نفت برمی‌داریم و آن نفت به هیوستون و لوئیزیانا می‌رود. خودتان می‌دانید؛ آن کشتی‌ها را می‌بینید که صف کشیده‌اند.
باز هم می‌گویم، هزینهٔ آن را بارها و بارها جبران کرده‌ایم و رابطهٔ بسیار خوبی با ونزوئلا داریم. مردم ونزوئلا اکنون خوشحال‌اند و نمی‌توانند آنچه رخ داده را باور کنند. بزرگ‌ترین شرکت‌ها و بزرگ‌ترین شرکت‌های نفتی جهان وارد آنجا می‌شوند و به شکلی تجارت می‌کنند که هیچ‌کس تصورش را نمی‌کرد.
ما هم سهمی برمی‌داریم؛ باید هم برداریم. آن‌ها هم سهمی می‌برند. بسیار جالب است که اکنون پول بیشتری درمی‌آورند. کریس ارقامی را به من نشان می‌داد. ونزوئلا اکنون بیشتر از هر زمان دیگری پول درمی‌آورد. ما هم پول زیادی درمی‌آوریم و فکر می‌کنم حقمان است.
بنابراین واقعاً اتفاقی بود که [نامفهوم]. یک جنگ یک‌روزه بود؛ یک روز طول کشید. مردم می‌گفتند: «قرار است آنجا برای همیشه گرفتار شویم.»
اما می‌دانید، ما ۲۰ سال در ویتنام بودیم و در آن جنگ هزاران و صدها هزار نفر را از دست دادیم؛ دست‌کم هزاران و هزاران نفر. سال‌ها در افغانستان بودیم. در تمام این جنگ‌هایی که درباره‌شان شنیده‌اید، سال‌های سال حضور داشتیم. این‌ها همان جنگ‌هایی بودند که من آن‌ها را جنگ‌های بی‌پایان می‌نامیدم.
اما این بار چهار ماه است که درگیر هستیم. دیروز روز بسیار غم‌انگیزی داشتم. به دوور رفتم. چهار میهن‌پرست بزرگ آمریکایی کشته شدند. این یعنی ۱۸ کشته در دو جنگ. حتی یک نفر هم بیش از حد است، اما شمارشان ۱۸ نفر است.
در حالی که در ویتنام ۲۰۰ هزار نفر را از دست دادیم. هزاران و هزاران نفر را از دست دادیم. در افغانستان و در هر جنگی هزاران نفر را از دست دادیم. در جنگ کره نیز هزاران نفر کشته شدند. همهٔ این جنگ‌ها سال‌ها طول کشیدند.
ما می‌خواهیم این را تمام کنیم و می‌خواهیم درست انجامش بدهیم. اما باید کاری را که برایش آمده‌ایم انجام دهیم. نمی‌توانیم اجازه بدهیم این افراد بسیار خشونت‌طلب به چیزی که می‌خواهند، یعنی سلاح‌های هسته‌ای، دست پیدا کنند.
[...]
بنابراین فقط می‌خواهم در پایان بگویم که حضور در اینجا افتخار بزرگی است. اکنون می‌روم تا دربارهٔ موضوعات گوناگون صحبت کنم. یکی از آن‌ها جنگ ایران است که باز هم می‌گویم در آن بسیار خوب عمل می‌کنیم؛ بسیار بسیار خوب. می‌گویم بهتر از چیزی که هر کسی انتظار داشت قابل انجام باشد.
نیروی دریایی و نیروی هوایی‌شان را از کار انداخته‌ایم. تمام رادارهایشان و بخش عمدهٔ توانایی‌شان را در زمینهٔ تولید از بین برده‌ایم. توان پهپادی‌شان ۸۴ درصد و توان موشکی‌شان ۹۱ درصد کاهش یافته است.
بعد روزنامه‌ای نوشت: «آن‌ها اکنون در موقعیت قوی‌تری نسبت به چهار ماه پیش قرار دارند.»
نه، این حقیقت ندارد. درست نیست. باورم نمی‌شود حتی اجازه دارند چنین چیزی بگویند. نیویورک‌تایمز نوشت: «آن‌ها اکنون در موقعیت قوی‌تری قرار دارند.»
آن‌ها ارتشی ندارند. نیروی دریایی ندارند. کارشان تمام است. ۱۵۹ کشتی داشتند که همهٔ آن‌ها در کف دریا هستند. ۲۱۲ هواپیما داشتند که همه از بین رفته‌اند. رادار ندارند. پدافند هوایی ندارند. هیچ‌چیز ندارند؛ جز اینکه خشن و باهوش‌اند و هنوز مقداری توانایی دارند.
اما چهار ماه پیش، باور کنید، بسیار بسیار قوی‌تر بودند. متوجهید؟ می‌خواهم خبر واقعی را به شما بدهم.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77442" target="_blank">📅 23:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77441">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
افراد نفوذی در دولت آمریکا سرشان را زیر برف کرده‌اند.
آن‌ها واقعیت‌های میدانی را نادیده می‌گیرند و به نظر می‌رسد فقط روی سال ۲۰۲۸ تمرکز کرده‌اند.
تجاوزگری بی‌فکرانه‌ای که از آن حمایت می‌کنند، تنها باعث خواهد شد رئیس‌جمهور آمریکا برای توافقی که در تلاش برای دستیابی به آن است، بهای سنگین‌تری بپردازد.
Compromised individuals in the U.S. administration are burying their heads in the sand.
They ignore the realities on the ground and seem focused only on 2028.
The mindless aggression they advocate will only ensure that POTUS pays heavier price for deal he's trying to achieve.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77441" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dKxzQqDJIVLCTPnIphhzdzPDTImLgWglbNkdZzC2mSULRFTpn7UW3jWeJLuhGeT4KPh_S5gtY_4xx1rYN0gnZfBDk1Y_L_LGEos-Wx42vuUYW4RUYFXGAjGGsyx1hnBRc3anyiHSb-gtrmeAq-grey_vUkk-OeFTs4zqTj3xc5X3Vhgbz6y-ChaDHJIzydmT1PtbguqwGlmQEhBTO7enjpCz1FrdPXeJF8o-mlBnsduz7dCgXtqeLb09dPfSIfMLOQiswrpZ2XgvH9a1dhNwJsxJioXlOs95VWun8sZqUK5DLN_sSn0EoilA8Tp2AAntT8BC-wRkeDi35Aq0F5PWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
هم‌زمان با پیام‌های دریافتی درباره پرتاب موشک از اهواز
آپدیت:
ارتش کویت پنج‌شنبه شب اعلام کرد که نیروهای نظامی ایران بار دیگر خاک این کشور در حاشیه خلیج فارس را هدف گرفته‌اند.
رسانه‌های حکومتی در ایران نوشته‌اند که هدف این حملات تازه پایگاه علی السالم کویت بوده است.
در همین زمینه ارتش کویت در شبکه‌های اجتماعی از جمله شبکه ایکس خبر داد که موشک‌ها و پهپادهای ایران توسط ضدهوایی‌های این کشور رهگیری شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77440" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=atphgefyV3iYKtyloL9ljvaUDN193tpWb8V6E5emvhDT79EkqMFHtDWGJshMqmUBv_Op8UM9dYLdq9ayZI0G7JT92AiIGYQZ_nEcGIkWv48MUmbJ2C-9SuIPUDkP9pD3OKQVR0tdtQwBH48i0nGEf9okub3dixwREcGSaFQjidpkD7gIHrW7J0n4sFG6du-GYQ_JQkzA2IXqKvilHJ2uFtyoX34QXJLg5Vexa7rJkNs5XmtpQ1sKYnEMVSfZIgYVP-7BRW2tjKact0LHOEC16y1tFuUpQ8v_MBHN4hN5Qz5SY8zvinSQn0wgVVTvG_-rGZ-9DOaN5Z2eMSXeFM3gIH6Rk59BQTNkSPAtXrbFEUwZ8zdgSwrZQVvUvKyx_qN99zYstZHrVJNp2D1VEcakLni6sinrjG8jSPSn3RTJ7u5Gn8_pxtT6BowUjeOEMMJ7kJ_VOH-VxDmixJA5oy5zEcRGQ9Z2gBJTSW_qvM1qBvWdskEz0qJsNUxI6OkwTJTl9PCbBxOf96MdC9hKxWMZ1BofQOpv44J4pb4J5PtZsi3J8nJv2OUvsXYeKv5bb3ndG6ipYLTxOOfoENdmfuTaKVAhfOx8Y8HQa_bgCnIC4nxGwedDvILv52-F9Ed09RA_ZFPowbksQE_iKkZTQ8lcrIDfa9jY8VBshxgV7gpKs8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=atphgefyV3iYKtyloL9ljvaUDN193tpWb8V6E5emvhDT79EkqMFHtDWGJshMqmUBv_Op8UM9dYLdq9ayZI0G7JT92AiIGYQZ_nEcGIkWv48MUmbJ2C-9SuIPUDkP9pD3OKQVR0tdtQwBH48i0nGEf9okub3dixwREcGSaFQjidpkD7gIHrW7J0n4sFG6du-GYQ_JQkzA2IXqKvilHJ2uFtyoX34QXJLg5Vexa7rJkNs5XmtpQ1sKYnEMVSfZIgYVP-7BRW2tjKact0LHOEC16y1tFuUpQ8v_MBHN4hN5Qz5SY8zvinSQn0wgVVTvG_-rGZ-9DOaN5Z2eMSXeFM3gIH6Rk59BQTNkSPAtXrbFEUwZ8zdgSwrZQVvUvKyx_qN99zYstZHrVJNp2D1VEcakLni6sinrjG8jSPSn3RTJ7u5Gn8_pxtT6BowUjeOEMMJ7kJ_VOH-VxDmixJA5oy5zEcRGQ9Z2gBJTSW_qvM1qBvWdskEz0qJsNUxI6OkwTJTl9PCbBxOf96MdC9hKxWMZ1BofQOpv44J4pb4J5PtZsi3J8nJv2OUvsXYeKv5bb3ndG6ipYLTxOOfoENdmfuTaKVAhfOx8Y8HQa_bgCnIC4nxGwedDvILv52-F9Ed09RA_ZFPowbksQE_iKkZTQ8lcrIDfa9jY8VBshxgV7gpKs8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجریان فاکس‌نیوز، متن زیرنویس، ترجمه ماشین:
مجری:
بیایید نگاهی بیندازیم به نیروگاه‌ها و مکان‌هایی که ممکن است بتوانیم هدف قرار بدهیم. لوکاس، وقتی به این‌ها به‌عنوان اهداف احتمالی نگاه می‌کنی، فکر می‌کنی اول از همه کجا را ممکن است بزنیم؟
لوکاس:
خب، نمی‌دانم نخستین هدف باشد یا نه، اما نیروگاه دماوند ۴۰ درصد برق تهران را تأمین می‌کند. نیروگاه هسته‌ای بوشهر هم احتمالاً هدف قرار نخواهد گرفت. روس‌ها آن را ساخته‌اند و هنوز هم اورانیوم با غنای پایین در اختیار ایران می‌گذارند.
مجری:
چون، لوکاس، باید بگوییم که منفجر کردن یک نیروگاه هسته‌ای خطرهایی دارد.
لوکاس:
بدون تردید. میدان گازی پارس جنوبی هم روی بزرگ‌ترین میدان گاز طبیعی جهان قرار دارد. نیروهای اسرائیلی در ۱۸ مارس، در آغاز جنگ، آن را هدف قرار دادند و ایران هم با حمله به بخش قطری همین میدان گاز طبیعی پاسخ داد.
مجری:
اگر بخواهیم در همان تنگه‌ای که آن‌ها در آن به کشتی‌ها حمله می‌کنند پیام بفرستیم، آیا آنجا جایی نیست که باید سراغش برویم؟
لوکاس:
چرا؛ فقط سؤال این است که پاسخ ایران چه خواهد بود. دیده‌ایم که ایران تلافی می‌کند. تأسیسات گاز طبیعی قطر و میدان‌های نفتی امارات، نگرانی اصلی همین است.
مجری:
یعنی اگر ما یک نیروگاه را بزنیم، آن‌ها هم پاسخی مشابه خواهند داد؟
لوکاس:
بی‌تردید. تمام این مدت ماجرا همین مقابله‌به‌مثل بوده است. نکته قابل توجه درباره اسرائیلی‌ها این است که آن‌ها پاسخ‌هایی نامتناسب می‌دهند. احتمالاً یکی از دلایلی که اسرائیل دوباره وارد جنگ نشده همین است. ایران از اوایل ژوئن به اسرائیل حمله نکرده است.
مجری:
ارزیابی تو از شیوه‌ای که اکنون عمل می‌کنیم چیست؟ فکر می‌کنی پاسخ ما نامتناسب است یا می‌توانست نامتناسب‌تر باشد؟
لوکاس:
پاسخ ما نامتناسب نیست. نکته قابل توجه این است که نیروهای آمریکا، پس از آنکه یک پایگاه آمریکایی در اردن هدف قرار گرفت، به پادگان‌های ایران حمله کردند؛ همان حمله‌ای که سه سرباز ارتش آمریکا را کشت.
مجری:
پس این همان نیروگاهی است که ممکن است هدف قرار بدهیم. این مهم‌ترین مورد است. برویم آن طرف نقشه؛ اینجا «کوه کلنگ» یا Pickaxe Mountain است.
لوکاس:
ارزیابی اطلاعاتی آمریکا این است که ایران احتمالاً چند روز پیش از عملیات «چکش نیمه‌شب» در یک سال قبل، بخشی از اورانیوم غنی‌شده خود را از فردو به کوه کلنگ منتقل کرده است.
این محل بسیار عمیق‌تر از دیگر تأسیسات هسته‌ای است. همچنین اینجا کوه‌های زاگرس است و با سنگ دولومیت بسیار سخت روبه‌رو هستیم؛ بنابراین حمله هوایی به آن بسیار دشوار خواهد بود. این یکی از دلایلی است که شاید از نیروی زمینی استفاده شود.
در واقع، چنین مأموریتی برای نیروهای مأموریت ویژه ارتش آمریکا است؛ نیروهایی مانند دلتا، تیم ششم سیل و اسکادران ۲۴ تاکتیک‌های ویژه نیروی هوایی.
ریسک ماجرا این است که هیچ‌کس دقیقاً نمی‌داند داخل آنجا چه وضعی دارد. هیچ نقشه فنی‌ای از داخل کوه کلنگ وجود ندارد.
مجری:
درست است. همین را می‌گوییم.
لوکاس:
آژانس بین‌المللی انرژی اتمی هرگز به این محل دسترسی نداشته است. بنابراین با اطمینان نمی‌دانیم آیا سانتریفیوژها و اورانیوم با غنای بالا به کوه کلنگ منتقل شده‌اند یا نه؛ اما این محل زیر نظر است.
شنیدیم که رئیس‌جمهوری ترامپ گفت به‌زودی کوه کلنگ را هدف قرار خواهد داد. بمب‌افکن‌های B-1 را دیده‌ایم که از بریتانیا پرواز کرده‌اند و البته بمب‌افکن‌های B-2 از پایگاه هوایی وایتمن در میسوری برای همان پرواز دور دنیا که در عملیات «چکش نیمه‌شب» دیدیم، برخاستند.
مجری:
و نطنز هم هدف قرار گرفته، درست است؟
لوکاس:
نطنز هدف قرار گرفته است. فردو و اصفهان هم هدف قرار گرفتند. این‌ها سه محلی بودند که در عملیات «چکش نیمه‌شب» در یک سال قبل هدف قرار گرفتند. با این حال، کوه کلنگ تا این لحظه دست‌نخورده مانده است.
[جملاتی که در ویدیو هست ولی برای جا شدن متن در پست، اینجا نقل نکردم.]
مجری:
و حالا تا جایی که می‌دانم، این نیروگاه برق [دماوند] دو میلیون نفر را تأمین می‌کند.
لوکاس:
بله.
مجری:
و خارج از تهران قرار دارد.
لوکاس:
اگر رئیس‌جمهوری بخواهد پاسخی بدهد که تا حدی نامتناسب تلقی شود، نیروگاه دماوند را هدف قرار می‌دهد. باز هم می‌گویم، این نیروگاه ۴۰ درصد برق تهران، یعنی برق پایتخت، را تأمین می‌کند.
تنها سؤال این است که آیا می‌خواهید برق میلیون‌ها ایرانی را قطع کنید که با آرمان آمریکا همدلی دارند؟
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77439" target="_blank">📅 21:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77438">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcNz5gE8JDhrA_9zOYECFjJzG2WsFzHO3VkJhzCD_YqZzt9EZfWJaBsyaEUqzpKBJwE4rt3zvTmGBO5DvqQU9lFJfxoO85Tr3E-A8q-UZP4pSkFE_lVIA2i3R7zLuy36NXiapeqoRCb0RgeA7S1kJ6xmbi4FrzelY_-B0afd73bgnEbgbspJkjX_mj3UU5rQbHGC5mbEncn-_j6KARbE6PKWivMtrFfHVzk2exIP1k8glwcmvpEZjw3L2l-j5ZqfMTj9_hDT0NlpfFpzv2lvgA1mdxYofYX_rMIXR-a9xwCw0uHkfxVleZ2caoqoQ2ZgIvJwFQa8pCg8DnvVuMnshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش کویت عصر پنج‌شنبه اول مرداد اعلام کرد که یکی از گذرگاه‌های مرزی این کشور با عراق برای دومین بار در یک روز، هدف حمله پهپادی قرار گرفته است.
ستاد کل ارتش کویت با انتشار بیانیه‌ای در شبکه اجتماعی ایکس (توییتر) اعلام کرد: «گذرگاه مرزی العبدلی عصر امروز بار دیگر هدف حملات پهپادی دشمن قرار گرفت که خسارات مادی بر جای گذاشت، اما هیچ تلفات جانی نداشت.»
ساعاتی قبل کویت اعلام کرده بود که آتش‌سوزی ناشی از حمله صبح پنجشنبه، مهار شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77438" target="_blank">📅 21:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZ9Py0AtxxrQO4TxF7muyJx_8Bn3ouaivX8T4onUbpJFMZnjY6OSj4YgNGGYvl7dfHPhzP96Fg8CQHT_O38jb9QnVjktCAqVjNrsDXUEK8JCo6UlRfhev1s4W35gWEB2VGwPFkIIewiAxFE_qojwR9cIh-J9hH-4IaetJt-YuSZqdGy2sjoxGxwawTBQiNlsJqueiSpQDYhskhUY71l7AeH-KwTd8mSO6dX3khXcvDWhGQPHiYmsCJxQGfx90zekcpuq1ztd8Et7S4y6TXSMeH7smT2vDjk8wdLwPpOk7Y-Sf5-k7nj1hYPOKzPHPdgrbMibztZxtYVPNWZ6EBFeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره
این پیام‌های دریافتی
:
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد ساعت ۱۸:۵۰ عصر پنجشنبه در پی حمله ارتش آمریکا، یک فروند موشک به نقطه‌ای در ساحل شهر سوزا در جزیره قشم اصابت کرد.
تسنیم نوشت که بررسی ابعاد حادثه و میزان خسارات احتمالی از سوی دستگاه‌های مسئول در حال انجام است.
خبرگزاری صداوسیما نیز از شنیده شدن صدای انفجار در قشم خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77437" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-GsIQVy6gjPDbbglQM8SW-yV_FLeF22rWsO-Ofys-dEZTJHR84ycZubV1H6NqxSX3j0-8nMuEBGsPDDPkDb1cDj4LfGobT3qz_LS-w5yVfeAkRA-dTJFc70-hzsq4v5_IS8i7IZhAM-Fptro1PxigUZ7hmn9mtKJfoZNQlHKlrNNPy6XHMnl_5u0iQ4xM0FOIRkQPnUyF6D96cMBnr22GtSKRBlj0DyK7Ed-GlQWm94Z9J8SrBP5S9MdWc63ahLY3-OvrLP4RTU-AeycyF_qiUQGuTg0eN8S8LL19Esq6oh_cAdSVHErJmBBHyHqxpRYWWSAM6PVpc2mET7xLX-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران روز پنج‌شنبه ادعا کرد که پایگاهی را در خاک بریتانیا که بمب‌افکن‌های ب ۱ آمریکا از آن بلند می‌شوند برای حمله «هدف مشروع» می‌داند.
وب‌سایت اکسیوس پیشتر به‌ نقل از مقام‌های دولت آمریکا نوشته بود که ارتش این کشور در دور جدید حملات به ایران، روز سه‌شنبه برای نخستین بار از یک بمب‌افکن دوربرد «ب ۱» برای حمله به اهداف متعلق به سپاه پاسداران انقلاب اسلامی استفاده کرده است.
اکسیوس نوشته بود که بمب‌افکن به‌کارگرفته‌شده در این حمله از یک پایگاه هوایی در بریتانیا به پرواز درآمده بود. اشاره این سایت خبری به پایگاه فِرفورد در جنوب غربی انگلیس است که در حال حاضر ۱۸ فروند از بمب‌افکن‌های ب ۱ آمریکا در آن نگهداری می‌شود.
حال سپاه پاسداران در پیامی این طور نوشته است:‌ «هر پایگاهی که برای حمله به خاک ایران از آن استفاده شود برای ما هدف مشروع است.»
سپاه در پیام خود ادعا کرده است که در پی ازسرگیری حملات، آمریکا ابتدا با موشک‌های کروز از روی ناوهای خود در اقیانوس هند به ایران حمله می‌کرده، اما در پی خالی شدن انبار موشک این ناوها، به استفاده از بمب‌افکن‌های خود در بریتانیا روی آورده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77436" target="_blank">📅 19:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77435">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QzBy0w7CT2aduyF1VMnbQ0w42ZKDuM6n1FuAd3R0EDTqkoNeP38auG_qwcMPqHPWafSzwNHxor3SXLX-bS9gbqR6efOrb23s1BjZ0sM_MmYP_nYFINZZRyviBAanIEkZ_sJwZDQ9kAWbqZTvwf4eHe-MmONtzKPiKbapGS5q7aS3FUz3Dn-VyNCgb9o6Aak1NwMsGgoLHmGXfSqOLFoMMtq_v6MZ5MrEU9stDgbfvBuMc1Lfaf9sitCdYs6ybtXu07chtyy0u0yqkDezwdgmUWorqVpzUg5N_ydho0SKsbf-2Th7TbnkS-LDeJPq81PcFnpSO6I-s7uHIAYZUo2YkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: ترامپ می‌گوید به تصمیم‌گیری درباره «حمله‌ای عظیم» علیه ایران «نزدیک» شده است
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنجشنبه به آکسیوس گفت که به‌طور جدی در حال بررسی ازسرگیری عملیات رزمی گسترده در ایران است؛ از جمله حملاتی که از عملیات «خشم حماسی» بزرگ‌تر خواهد بود.
چرا مهم است: ترامپ در مصاحبه‌ای کوتاه اذعان کرد که چنین تصمیمی پیامدهایی خواهد داشت و تأکید کرد که هنوز تصمیم نهایی را نگرفته است.
ترامپ برای تصمیم‌گیری خود مهلتی تعیین نکرد. دو مقام دیگر آمریکایی نیز تأیید کردند که هنوز هیچ تصمیمی گرفته نشده و هیچ دستور تازه‌ای به ارتش داده نشده است.
تشدید تنش‌های کنونی تاکنون باعث شده قیمت نفت از بشکه‌ای ۱۰۰ دلار فراتر برود. بازگشت به جنگی تمام‌عیار در آمریکا به‌شدت نامحبوب است.
آنچه او می‌گوید: رئیس‌جمهوری آمریکا گفت: «من در حال بررسی یک حمله عظیم هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام شده است. به تصمیم‌گیری نزدیک شده‌ام. ما کاملاً برای آن آماده‌ایم.»
ترامپ گفت اسرائیل «اگر از آن‌ها بخواهم، ظرف دو دقیقه وارد عمل می‌شود»، اما افزود که برای آغاز عملیات تازه علیه ایران «به هیچ‌کس نیاز نداریم».
او همچنین گفت پیوستن اسرائیل به این حملات «پیامدهایی» خواهد داشت و تلویحاً به احتمال تلافی ایران علیه اسرائیل اشاره کرد.
تصویر کلی: ترامپ گفت ایرانی‌ها «می‌خواهند مذاکره کنند»، اما در حال حاضر آماده توافق نیستند.
او گفت: «هنوز به اندازه کافی درد نکشیده‌اند.»
دو منبع منطقه‌ای مطلع از تلاش‌های میانجی‌گرانه گفتند رهبری ایران تازه‌ترین پیشنهاد ارائه‌شده را نپذیرفته است.
یکی از آن‌ها گفت: «داریم تلاش می‌کنیم، اما ایرانی‌ها همکاری نمی‌کنند.»
محور خبر: آمریکا طی ۱۲ روز گذشته حملات خود را تشدید کرده است تا حملات ایران به کشتی‌های تجاری در تنگه هرمز را متوقف کند.
ایران تاکنون هیچ نشانه‌ای از تمایل به تغییر مسیر نشان نداده و خود نیز حملاتش در منطقه را تشدید کرده است.
شورشیان حوثی مورد حمایت ایران در یمن حمله به کشتی‌های سعودی در دریای سرخ را آغاز کرده‌اند؛ اقدامی که تنش‌ها را در یکی دیگر از مسیرهای حیاتی انتقال نفت تشدید کرده و بازار جهانی انرژی را بیش از پیش بی‌ثبات کرده است.
ترامپ در حساب خود در تروث سوشال نوشت که اگر حوثی‌ها بار دیگر به کشتی‌ها در دریای سرخ شلیک کنند، «ایالات متحده ایران را مسئول خواهد دانست».
او گفت حوثی‌ها نیروی نیابتی ایران هستند و بنابراین «مجازات نظامی سنگینی علیه ایران و البته خود حوثی‌ها اعمال خواهد شد».
آنچه باید زیر نظر داشت: ترامپ جداگانه گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، قصد دارد هفته آینده در مراسم وداع با سناتور فقید لیندزی گراهام در واشینگتن شرکت کند.
ترامپ گفت: «روابط با بی‌بی بسیار خوب است. اگر او اینجا باشد، با او دیدار می‌کنم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77435" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77434">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید قشم صدای انفجار
الان دریابانی سوزا رو زد وحشتناک
جزیره قشم ۱۸:۴۰
ساعت 18:40 دقیقه قشم صدای انفجار شنیدیم
وحید جان قشم صدای دو انفجار از راه دور اومد ..
🔄
صدا و سیما:
شنیده شدن صدای انفجار در سوزای قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77434" target="_blank">📅 18:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77433">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YAO7dMmgjUHJDGmX-08tvtNqyZFmBwcYRcL1y-7RDpL0AaT0ZDT_MI4rb7tqTJqPmVn0VovfAsfQsRLr_M0Cxiw6RgV5Zh2sC9XDQyQ8aa-HM-jXuK6nPstIRl5ZzKJdSnubHbCTHFJKJNh4sCkSWEyXGy7_XVRiervAPLkU4a1mOsHTjuu3CVPDzMW_ecxwhkB6WxTDZPXRTKxygWVs2ulqNLuGvbN0emSXQoGTVdAbPSv5xSSwLPJBOVEieUTS-U8ufWd1M7C2-SlMMIDr9aA7RCX7th2QBFanp1SX2fNJbDCjoZFIwplr2AG4vRdAeopnzqLVmvaS9O55OHgAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
می‌خواستند ایران را تنبیه کنند.
در عوض، خودشان را با قیمت سه‌رقمی نفت تنبیه کردند.
استراتژی ۱۰ از ۱۰
👏
👏
👏
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77433" target="_blank">📅 18:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfVHpN1auBLqfeOTYKljzz43y18eD0oxI3LHThTAOGauBW044DxABZGeqg62DD6UpWYYcwG3-qQ3BVh8BiJMLHhrCfoFFMAW37RkqyvwRYxDtlvylXuCRE5ktlw8eOoai5UwSt5jrIiawPCy7-S2YinLuLVYa5gR-Q30MKenjQhgsS2VqzT8GnJQ2AU2FuF2tfiGmlf056PKoX4APigRYkLuR2T-YTV0SmeIDZ7PtUBAwUXxwTlkX7X0XfO9QSbHaq6RI3fU-Sqq0wUm041nUr4F-LTYomrI9WSFOcw0gQWd51wT0i2unLtAkeo990sxQXGGYy4UVApbRylfLRs-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ روز پنجشنبه اول مرداد، در پیامی در شبکه اجتماعی تروث سوشال با یادآوری حملات نظامی ایالات متحده علیه حوثی‌ها که سال گذشته انجام شد، نوشت: «حوثی‌ها از آن زمان و در جریان درگیری با ایران، رفتار مسئولانه‌ای داشتند، اما متاسفانه با تیراندازی شب گذشته به دو کشتی عربستان سعودی، بار دیگر دست به حملات زده‌اند.»
ترامپ هشدار داد که اگر این اقدامات تکرار شود، آمریکا جمهوری اسلامی ایران را به عنوان حامی حوثی‌ها مسئول خواهد دانست. او تاکید کرد که در این صورت، مجازات نظامی بزرگی بر ایران و همچنین خودِ حوثی‌ها تحمیل خواهد شد؛ گروهی که به گفته او، تا پیش از این حرفه‌ای و هوشمندانه عمل کرده بودند اما اقدام اخیرشان مایه «تاسف» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77432" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osj-GIjKkzwKd0cioMIdr3NtOKLoPG3nS2v7Ah-f-gIkYT444xOuEKsimMwdFLYfNh_beopkSVo5S0aMPqDpJDsnfiPMWO3vv2n0WXLi8o33amnSQ0yhP33nudUXL9tNLyDVDi2ASylIDZloGMJZVRVGj8nizdYkzkM8tjsGY3bCGlT28-SLHQUbRdJb4McW5YC5kGN8TMy6jcwUTbkYswidKCjrKJBTYv7eFmCU9Ra4XV_UvPZ-4Uo74apKRUS3vkYonyO98viXAtxW9Tm1pWvBHkLoMN-j05wWQXsrvJcaUmQ-rIDgoB7wTSo_DWfq0pYjlsFtZKkvfe1hxtHILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد امیرحسن اکبری‌منفرد، زندانی سیاسی ۲۷ ساله محبوس در زندان اوین، با حکم شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، از بابت اتهام «بغی» از طریق عضویت در سازمان مجاهدین خلق ایران به اعدام محکوم شده است. بر اساس این گزارش، حکم دو روز پیش به او ابلاغ شده است.
هرانا همچنین گزارش داد امیرحسن اکبری‌منفرد زمستان ۱۴۰۳ همراه با پدر، برادر و خواهرش در کرج بازداشت شده بود و سه عضو دیگر خانواده بعدا با تودیع وثیقه آزاد شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77431" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SmC6i7z1ULu0asfG_Dvj4bf-M41kf8LqkFxCNrT2qWFxcHg6pidbCU3ZFy5LDMCTEF0vj6a_lu0nH2xTZrq5-zN_PeBWD8s6ywK4Grxnldsbjce9OtX7l2VvDXNJjYZJHjBqPD32U7V-q1ez7Vn82JdRhi6a5e_gAwjEa1ihMfNedYKxWDjh79ETDxXIxjZBP2peCl2kYebPlo6swz17e1bVcr5bZgvwsAiKuZ5OkkjZzhrcKZjLnfaFkhD0dbr_aB7MLdQjhlxNaO2wSJDxzhIPNbUPDBcFoFcA-4v61C1Gq4BtLRCuuA3ORgqRG1uYrBXTAhsCdeFj-TMNV0zWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dvD3_BkQpba5mGogSQzZ1a0oraVeM0OPCE8yZk24gaVTAtwqJuGwcsLF9k__14fXmOuo_E6SQJh1csP19ThmvJuofAv8hmPhe-_tQJxCLZ9lNdkDDQoU_1leq_e62dS-D7mm4qXPqpOAPJlB9BDyPcw_jqYh9GTrRhLTjisPux3RehGeWZyDIhnYVdCwVmGoeD16P5tBaG0DQC0ngb2Qmxdm4tMiP6KxZVMo6cmijrCw77rmpbkPO57CU5_JT8vUM-EopI1jPLFGkn_YGMiM15yKSnf7MErNJvVDayrMaP8oUhZkVDOndtPxGwRB5hFGxACVNTB84j8odr65mvrJzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اول مرداد ماه، در پیامی در شبکه اجتماعی ایکس اعلام کرد توافق هسته‌ای غیرنظامی میان وزارت انرژی آمریکا و عربستان سعودی تصویب خواهد شد، اما این توافق مشروط به پیوستن ریاض به توافق‌های ابراهیم است.
ترامپ در این پیام با اشاره ناگهانی به «غیرنظامی» بودن برنامه هسته‌ای ایران نوشت: «توافق هسته‌ای غیرنظامی که میان وزارت انرژی ایالات متحده و عربستان سعودی در حال انجام است، تنها به استفاده‌های غیرنظامی، مانند برنامه‌هایی که ایران، امارات متحده عربی و دیگر کشورها دارند، مربوط می‌شود. اما این توافق کاملا مشروط به پیوستن عربستان سعودی به توافق‌های ابراهیم است.»
رئیس جمهوری آمریکا کرد در این توافق «هیچ غنی‌سازی مواد [هسته‌ای] وجود نخواهد داشت» و آمریکا با تاسیسات هسته‌ای غیرنظامی و بدون غنی‌سازی مخالف نیست
@
VahidOOnLine
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل پنج‌شنبه اعلام کرد پیوستن عربستان سعودی به توافق‌های ابراهیم، تحولی تاریخی در مسیر صلح در خاورمیانه خواهد بود.
دفتر نخست‌وزیر اسرائیل افزود اقدام نظامی مشترک آمریکا و اسرائیل علیه جمهوری اسلامی و تضعیف محور «تروریستی» تهران، زمینه را برای گسترش دایره صلح فراهم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77429" target="_blank">📅 17:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAAT_LwkkxM1B5q7Gl6yZt8XZPk130UvAhzlk1A3rPcSxYAZDiwR1r2baBrwtPOyY3THVAl-163SPSdUC1Vn8qsl6y5IrPGwmC6p1zVOS54Bj3GkpHMq4OPmqPDGAc0VcHZbykyzwUCHdhukpKCh8PkWm0ilaJgVw-kwyJ1IsalIccrUJzTwOsxl66CQzt6Ju4jkz900qYk72f_AnGbdx_QNvzYEwW-N2bpvEZdOxrTBjyfHhCHpXdpkZGX36DgKWK2jW31OpYvYegYLnxnUVSEVPVqo6_QU2ka8wOiqSo07x_00vnrCuKUYytXa7Co3Abr1x17l9qoUlZZR_KjJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایلنا در گزارشی از ادامهٔ بحران کم‌آبی در زاهدان و برخی مناطق استان سیستان و بلوچستان خبر داده و نوشته است که شماری از شهروندان در برخی محله‌های این شهر با قطع آب تا سه یا چهار روز متوالی روبه‌رو هستند.
بر اساس این گزارش که روز پنج‌شنبه یکم مرداد منتشر شد، بسیاری از خانواده‌ها برای تأمین آب ناچار به خرید آب از تانکرهای خصوصی هستند و برای هر بار پر کردن مخزن خانه بین یک تا یک‌ونیم میلیون تومان پرداخت می‌کنند.
ایلنا همچنین به نقل از شهروندان گزارش داده است که برخی خانواده‌ها به دلیل ناتوانی در پرداخت هزینهٔ خرید آب از تانکرهای خصوصی، ناچارند چند روز را تنها با چند دبه آب سپری کنند.
محمدرضا کوچک‌زایی، عضو شورای اسلامی شهر زاهدان، نیز در گفت‌وگو با ایلنا با تأیید بحران کم‌آبی گفته است این شهر با کمبود حدود هزار لیتر آب در ثانیه، معادل نزدیک به یک‌سوم نیاز آبی خود، روبه‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/77428" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77427">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSUC6aDG-i1Xb16B4k_o5PKNFXg6hii6Qp3poMn7Q_RQ1aHJnNQEt6eJ2VYFd90HK7GXBqgEHJXtSg8J88uofiuShvLj5UYPRMjDUCa29nCu2wNnCAIkS8LlrgrhWZHP1HQKOArikebHPpPMFZyD8GINaHkb6_a4EGQZls8MfzI01WbAxZQKnUCsF866WtcyX3yuw8nfvv_VqPGPbqiIk3lBbOS895JKDtc9tCG-4CX9P2T92i806gi6nl_bV_xK0XIBdT6_9CwAVD-b1tUY4bZoASTRkJOlu3hHiMkOiPxklosz6SIBJlqp9xS_R1LQxTwlr5GdqWl6RDPkH31Mfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما و خبرگزاری تسنیم، روز پنجشنبه یکم مرداد ماه از شنیده شدن صدای چند انفجار در شهرستان کنارک در استان سیستان و بلوچستان خبر داده‌اند.
خبرنگار صدا و سیما در گزارش زنده اعلام کرد، صدای پرواز جنگنده‌ها نیز در این منطقه شنیده شده است. به گفته این منبع خبری،َ انفجارهای روز پنجشنبه، اولین حملات آمریکا در طی ۲۴ ساعت گذشته به این شهرستان بوده است.
@
VahidOOnLine
من هم حدود ساعت ۱۰ صبح پیام‌ها و عکس‌های مختلفی درباره کنارک دریافت کرده بودم + کلی پیام از چند شهر دیگر درباره پرتاب موشک
پیام‌های زیادی هم از دزفول و اندیمشک داشتم که در اون مورد پیش‌تر اعلام شده بود قراره  مهماتی کنترل‌شده منفجر بشن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77427" target="_blank">📅 17:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAg7-xDit7xwDVCiqnoEm9l9JAKIkLWd11GEezvC2OQrNBDUp6AAJBZH1j36HcnUyxi56safr9lMy_NHgEjuJ3mDpSrP9uwVj225edntw6U8oHbz-GEv4YOb32Nwa6ZCCeMUueTn5inUPt3Qxly8gc03EeepOfkGXPjLAoSbcFlHHNOuHL4LBBsBELE8-bRQdMdIQE10bZ0jHc6_IAsQhV0bfixradfAQ_K71g6URp2BUqvx7EIFc-q7scDkI4goZK-p8DgQFclsPuGbeTjg2yvyjoyrfWDRwSGhtXqjh2z_aaw7CD9g4pmADRImhz7cffQNVmTKyFVjsDJUnWcgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماری
از داوطلبان آزمون کارشناسی ارشد در شهرستان‌های بستک و بندر خمیر استان هرمزگان به‌دلیل تخریب پل‌ها و بسته شدن مسیرهای ارتباطی پس از حملات آمریکا، از حضور در جلسه آزمون بازمانده‌اند. به گفته آن‌ها، با وجود اطلاع مسئولان از وضعیت منطقه، هیچ راهکار جایگزینی برای برگزاری آزمون یا انتقال داوطلبان ارائه نشد.
کانال تلگرامی «
دانشجویان متحد
» خبر داده است که شامگاه ۲۶ تیرماه ۱۴۰۵ و هم‌‌زمان‌‌‌ با برگزاری آزمون کارشناسی ارشد، پل‌های محور بستک–بندر خمیر–بندرعباس در حملات پهپادی سنتکام هدف قرار گرفت و مسیر ارتباطی این دو شهرستان با بندرعباس به‌طور کامل مسدود شد.
در حالی که حوزه امتحانی داوطلبان این مناطق در بندرعباس تعیین شده بود، بسته شدن جاده‌ها باعث شد هیچ‌یک از آن‌ها نتوانند خود را به محل برگزاری آزمون برسانند.
به گفته این داوطلبان، آن‌ها تا آخرین ساعات پیش از آزمون بارها با اداره راهداری و دیگر نهادهای مسئول تماس گرفتند، اما هیچ راه‌حلی برای انتقال یا تغییر حوزه امتحانی در نظر گرفته نشد.
این دانشجویان می‌گویند ماه‌ها برای شرکت در آزمون آماده شده بودند، اما در نهایت به‌دلیل شرایط جنگی و نبود تدبیر مسئولان، فرصت حضور در کنکور را از دست دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77426" target="_blank">📅 17:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDfLtZWrKrgXmBSTS9x7TvRlyJI7BXPTDjY-3T3E9kJhuYZfhzzokdbEL_66TknI3Mczw8Yf35Zs4dDr9Y_v1YI3LKrhFSEpZrCrxsJYXSXN2VRHeSmDNssMl0i85JRAqDEVCY1pz18g9_YeViVWFn95wCct7TtCnMy24m9bPZ1VcRRlmTUvIcOegEvabXqx10pTGrXEjmbSbcVe9bCTmuNoWTQZ97KZ0V1elb80luuRftmc_Lob-zfMO6HHGWK0L2SDMUOWTm8jyKyTrrm6Up4qGOEe6bBJjZqDtZwNClrtpQkS62MyXv4OrWrN7g3noP3GD-De7OseA7ypq73kMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا، در حاشیهٔ نشست آسه‌آن در مانیل، با تکرار اظهارات پیشین خود مبنی بر «آماده نبودن ایران برای توافق» گفت: «آن‌ها هزینهٔ این موضوع را خواهند پرداخت.»
مارکو روبیو روز پنج‌شنبه یکم مرداد گفت «هزینهٔ ایران هر شب بیشتر می‌شود تا زمانی که به خود بیایند» و افزود: «با وجود جسارت ایران، آن‌ها به‌شدت در عذاب‌اند و این رنج همچنان ادامه خواهد یافت.»
وزیر خارجه آمریکا در عین حال ابراز امیدواری کرد که حکومت ایران «احتمالاً به‌زودی» آمادهٔ توافق شود، اما تأکید کرد در حال حاضر به‌وضوح آمادهٔ توافق نیستند، «حداقل نه توافقی که حاضر باشند با آن کنار بیایند».
روبیو در پاسخ به سؤالی دربارهٔ اظهارات اخیر دونالد ترامپ دربارهٔ پرداخت هزینه از سوی ایران در ازای کشته شدن سربازان آمریکایی و حمله به کشتی‌ها در تنگهٔ هرمز نیز گفت سیاست ترامپ «سر در برابر چشم است و ایران هزینهٔ سنگینی خواهد پرداخت.»
وزیر خارجهٔ آمریکا همچنین با ابراز امیدواری نسبت به توقف حملات حوثی‌های یمن گفت: «امیدوارم آن‌ها تنش‌زدایی کنند، ایران آن‌ها را فریب داده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/77425" target="_blank">📅 17:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77424">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZnNNTT6JyGfo8s4cWhBNm5uYDDGfw2nPqX5K3MsUwEdVaUnsNa0nKtZTkAu_9_NdvHm36bIZpYdb48K0_hWJe-yYl6jDmIDPHNLp0Q-vDCXPYJhvW2DNuaDgEuE1P8aflJsuY5AG1LiwwnO1PeJrDKHUWZWGdk2I_iJwDhAtYsoPse_tz6EL7zuHeQ_xjMG5AVAvT9ET9tL0uAn2W0pqP2cW9lQTddYN61K04blHsXnnaOjI0lKVn-jQwtGVcn-8_gS5RccTsRbun6lXS72gzY2k6pq8GothZ5Fc7zweWWmvrEViOu9s89azXUjFPSomZ_XORXB5aCGlgsxcp2HsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگاه قضایی جمهوری اسلامی برای دو نفر از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ احکام سنگینی صادر کرد؛ مهنام نواب‌صفوی به اعدام محکوم و حکم ۱۰ سال زندان علی صانعی نیز در دادگاه تجدیدنظر تایید شده است.
مهنام نواب‌صفوی، محبوس در زندان دستگرد اصفهان، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد با اتهام «محاربه» به اعدام محکوم شده است.
در پرونده او اتهام‌هایی از جمله «محاربه از طریق مشارکت در تخریب اموال عمومی»، «تبلیغ علیه نظام»، «اجتماع و تبانی علیه امنیت کشور» و «تشویق مردم به کشتار یکدیگر» مطرح شده است.
هم‌زمان، حکم ۱۰ سال حبس علی صانعی، دانشجوی ۲۲ ساله رشته کامپیوتر، در دادگاه تجدیدنظر تایید شد.
صانعی اسفندماه ۱۴۰۴ در ملارد بازداشت و به زندان تهران بزرگ منتقل شد. شعبه ۲۸ دادگاه انقلاب تهران به ریاست قاضی عموزاد او را با اتهام‌هایی از جمله «توهین به رهبری»، «اجتماع و تبانی علیه امنیت کشور»، «تبلیغ علیه نظام» و «همکاری با اسرائیل» به ۱۰ سال حبس محکوم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77424" target="_blank">📅 17:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ciyOE8ROpSAEj4XODHnlu_p2QPx80wh1v5FU3QeZJvBGGyY-Uy6YIQbEw3bFQCNPimTWD5Kn5dofjhUB9HF6Kc0R1HbkQ50osuttI7E3Uq6aRAG36sDBAShzLQEqJLt9KrWbtvsGi41Pz_on_9l0KaszbuJB0frTqHFeqUfoYBn8h8HBAl7yfjQQF6LxakRZ8SaEMHU0YsrTmhFJm7_DasnNasa9SJkuTa_81fst253ZdGA000X7F7Wz-EJ8493znxGuvibESMJjuBDospLi7XMln0nY6Szid-vJdIJsTDkRZ1ZYkJ32V0UUqgPhXrYNX2RoVGcDCyHZ8wGQE_cfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: آمریکا هم‌زمان با تشدید حملات به ایران، بمب‌افکن B-1 را به‌کار گرفت
ترجمه ماشین:
مقام‌های آمریکایی گفتند ارتش ایالات متحده روز سه‌شنبه برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران از یک بمب‌افکن دوربرد B-1 استفاده کرد.
چرا مهم است: این نخستین بار از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش بود که آمریکا مأموریتی با بمب‌افکن B-1 انجام داد.
استفاده از بمب‌افکن‌های B-1 که می‌توانند ۲۴ بمب ۲٬۰۰۰ پوندی یا ده‌ها موشک کروز حمل کنند، نشان‌دهنده تشدید و گسترش قابل‌توجه کارزار نظامی آمریکا بود.
‏B-1 می‌تواند در ارتفاع پایین با سرعتی بیشتر از سرعت صوت پرواز کند و در میان همه انواع بمب‌افکن‌ها، بیشترین محموله بمب را حمل کند.
هم‌زمان با ادامه افزایش حضور نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان در حال بررسی بازگشت به عملیات رزمی گسترده علیه ایران است. مقام‌های آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
اصل خبر: بمب‌افکن B-1 مأموریت خود را از یک پایگاه هوایی در بریتانیا آغاز کرد و در وب‌سایت‌های آنلاین رهگیری هواپیما مشاهده شد.
فرماندهی مرکزی ایالات متحده (سنتکام) در بیانیه روز سه‌شنبه خود درباره حملات آن روز، به مأموریت B-1 اشاره نکرد.
در این بیانیه آمده بود: «دارایی‌های سنتکام مراکز عملیات نظامی ایران، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز بیش از پیش تضعیف شود.»
مشخص نیست B-1 چه هدفی را مورد حمله قرار داده و آیا این مأموریت عظیم از دیگر حملات چند روز گذشته مؤثرتر بوده است یا نه.
آمریکا در جریان عملیات «خشم حماسی» چندین مأموریت با B-1 انجام داد و پایگاه‌های موشکی، مراکز فرماندهی، تأسیسات نگهداری سلاح و سامانه‌های پدافند هوایی را هدف قرار داد.
وضعیت کنونی: با وجود گسترش حملات آمریکا، به نظر نمی‌رسد حکومت ایران موضع خود درباره تنگه هرمز را تغییر داده باشد. ایران همچنان به حملات علیه پایگاه‌های آمریکا در منطقه ادامه می‌دهد.
برخی مقام‌های دفاعی آمریکا می‌گویند توانایی نظامی ایران در اطراف تنگه هرمز «تقریباً از بین رفته است»، اما برخی دیگر می‌گویند ایران همچنان قادر به حمله به کشتی‌ها در این منطقه است.
رئیس‌جمهور ترامپ روز چهارشنبه تهدید کرد که اگر ایران به حملات بیشتر علیه کشتی‌ها در تنگه هرمز دست بزند، پل‌ها و نیروگاه‌ها، از جمله تأسیساتی در تهران، را بمباران خواهد کرد. ایران نیز در پاسخ، زیرساخت‌های کشورهای حاشیه خلیج فارس متحد آمریکا را تهدید کرد.
نمای گسترده‌تر: همچنین روز چهارشنبه، شورشیان حوثی برای نخستین بار از زمان اعلام محاصره بنادر عربستان سعودی، به کشتی‌های سعودی حمله کردند.
یک مقام دفاعی آمریکا گفت حملات حوثی‌ها، پس از چند ماه که تقریباً به‌طور کامل از جنگ دور مانده بودند، ممکن است با تحریک ایران انجام شده باشد.
این مقام گفت ایران می‌خواهد با استفاده از حوثی‌ها، علاوه بر خلیج فارس جبهه جدیدی در دریای سرخ ایجاد کند و بر یکی دیگر از مسیرهای حیاتی بین‌المللی حمل‌ونقل نفت فشار وارد کند.
روز چهارشنبه چندین کشتی تجاری در حال عبور از دریای سرخ دیده شدند که از بیم حملات حوثی‌ها، مسیر خود را تغییر دادند تا از تنگه باب‌المندب عبور نکنند.
آنچه باید زیر نظر داشت: مقام‌های آمریکایی گفتند میانجی‌های قطری همچنان با مقام‌های آمریکایی، ایرانی و عمانی گفت‌وگو می‌کنند تا به توافق جدیدی برای بازگشایی تنگه هرمز و توقف درگیری‌ها دست یابند؛ این موضوع را منابع مطلع اعلام کردند.
یک منبع منطقه‌ای گفت رهبری ایران تازه‌ترین پیشنهاد ارائه‌شده از سوی میانجی‌ها را نپذیرفته است.
مشخص نیست ترامپ چه مدت به تلاش‌های دیپلماتیک فرصت خواهد داد. ترامپ چهارشنبه‌شب در سخنرانی‌ای در جورجیا گفت: «آن‌ها به‌شدت زیر ضربه هستند و می‌خواهند توافق کنند.»
«اما من می‌گویم آن‌ها آماده توافق نیستند، چون هر بار توافق می‌کنند می‌خواهند آن را عوض کنند و همه‌چیز را تغییر دهند. آن‌ها آماده نیستند. خیلی زود آماده خواهند شد.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77423" target="_blank">📅 07:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sgyuUWLyI75-7B3YTHbQCvR4386n8T7ivEx5JEmNIhgseAQVOaEPzjJof5Dbco3j1DnqL8-caZbW7BuDpDvv0g1h_tbfUXP7x4UvjN-XhHPR4YLPrj1euu-CF78wL5hOArSfK4ta-TlINYAaL--2fQDdkv8hinsD5iET71G_W4PxRWetXMQzNmVhIS2YR7gFxc9gy5Y7bgjLyg2sg-KHeueyG6CVOWbVJVX-nczg-OuNZhGl9otmWq6opk_0G7s7vBQxtHKZVQzQoSLvSr-83OEzkKcepuTKJQgU-T-VozxtZxaUo7m8pI-Pnnhn_Xh1Bm1cN_rOrEjI2Cx5FfNx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان (واس) تایید کرد که کشتی «انسیلیا» متعلق به یکی از شرکت‌های سعودی در دریای سرخ هدف قرار گرفته است.
به گزارش واس، در پی این حمله، آتش‌سوزی در بخش جلویی کشتی رخ داد، اما همه اعضای خدمه سالم هستند.
یک منبع در سازمان حمل‌ونقل عربستان نیز اعلام کرد نهادهای مسئول اقدامات لازم را برای تامین امنیت کشتی «انسیلیا» انجام داده‌اند.
پیش از این، حوثی‌های مورد حمایت جمهوری اسلامی اعلام کرده بودند که دو نفتکش عربستان سعودی را هدف قرار داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77422" target="_blank">📅 07:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/111a8149da.mp4?token=I3UGsL4W-5hgp4ymd8z-8sY6QRuIpqO83_qFuprFJyDFFgSafAn77y8tVzUwFVlRJj2y8GZX6TPGL6WJI2RmU4UZdcJM6Sd5mOwipFOl0LzrDcI1Kko0wbFqNNSn3wq0fvb-3PtEFFAyetDjCZci4rxip3_fspgMa0an82kiJhBxYJRGJqa6bbgdEPwjI4qrER465b_QLL8TyOS0Z80irGXw74lWpW0meg5oYjV8xrn8xR1B6rtxrdlCqVgWbktz4CHTadFFl-fYQD_xn8gZ_Hy1cP6eGTJ3PfBtStzQRm_BZdp16a9irm7smxJE4LZBtUfXXUu63VwLJg6Grr6SgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/111a8149da.mp4?token=I3UGsL4W-5hgp4ymd8z-8sY6QRuIpqO83_qFuprFJyDFFgSafAn77y8tVzUwFVlRJj2y8GZX6TPGL6WJI2RmU4UZdcJM6Sd5mOwipFOl0LzrDcI1Kko0wbFqNNSn3wq0fvb-3PtEFFAyetDjCZci4rxip3_fspgMa0an82kiJhBxYJRGJqa6bbgdEPwjI4qrER465b_QLL8TyOS0Z80irGXw74lWpW0meg5oYjV8xrn8xR1B6rtxrdlCqVgWbktz4CHTadFFl-fYQD_xn8gZ_Hy1cP6eGTJ3PfBtStzQRm_BZdp16a9irm7smxJE4LZBtUfXXUu63VwLJg6Grr6SgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام تازه‌ترین حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰:۳۰ شب به وقت شرق آمریکا [۶ صبح به وقت تهران] در ۲۲ ژوئیه، برای دوازدهمین شب پیاپی، دور دیگری از حملات علیه ایران را به پایان رساندند.
نیروهای آمریکایی اهداف نظامی ایران، از جمله توانمندی‌های دریایی، تأسیسات نگهداری موشک و پهپاد، مراکز نظارت ساحلی و تجهیزات پدافند هوایی را هدف قرار دادند. این حملات توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری را بیش از پیش تضعیف می‌کند.
در ماه جاری، نیروهای آمریکایی ده‌ها مرکز نظامی ایران در خشکی را هدف قرار داده‌اند و هم‌زمان محاصره دریایی علیه ایران را از سر گرفته‌اند. تا امروز، سنتکام برای جلوگیری از ورود کشتی‌ها به بنادر ایران یا خروج آن‌ها از این بنادر، مسیر ۹ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته است.
بیش از ۵۰ هزار نیروی نظامی آمریکا در سراسر خاورمیانه در حال فعالیت هستند و همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77421" target="_blank">📅 06:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OpGPQbDetYRm0BEq1qtl8sr1jjT6GLhdVbFbqmc2ccoSEKVlX2xLS3QzQxhQhI6tkSR240QZHULYtMZr4X7gGLzeNNXXFLb4mklGa9crV46JTLt69bnJrTXkgdgxRl6xL5NiZ9HjNbwvZd8hg68GUyMnbl3iSL5xEYY2nCL_ZA2h303I8sDQpvsEUNT7j_jK4Cj2LXhKGIFloxovElIhC2xP2Des5aik3YMkn3fEg3tFw22bVK1j2P9DvpSmP9WgGDIMWbaD85ZkaAJ3NNUE6rQ5LE4b_xVwbmeNpSGEniJcJv8wy6XjogdPGZiXdi3OlE2gRyyHlwwRgxxwa9LFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه پیام دریافتی از ساعت ۵:۱۳:
دوتا انفجار سنگین پایگاه دریایی ارتش جاسک
جاسک ۲ بار زد
جاسک چند دقیقه پیش دوبار زدن . سلام
🔄
دوباره زدن
صدایی شبیه به جنگنده هم میاد
یک صدای وحشتناک انفجار جاسک 5:30
همین ۱ دیقه پیش دوباره جاسک زدن، نمیدونم دقیقا کجا ولی صدای خیلی شدیدی داشت
باز انفجار مهیب در بندرجاسک ۵:۳۱
جنگنده بالای سر شهر در حال چرخیدنه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77420" target="_blank">📅 05:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77416">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BLhXu24PtYGPtZ4W2_NVhMzoELAfhPcD7rqwyKmD2Goh_NVuQlqV1H8YqVvU_J5frqOt6U7tyXSfO-d2p39P-OFHAv-hI2qj-vV9y_o5Y-RPCDOLetc1TQHbWGthq7jiyf6BIT6px_0Z9iedW9I-8e2zvsxXbZgW3FKuKi2rp7XQ_8VRt8EVcHCP23IjISEPPUzV2Ylir7u1vxm14C71vKK4IjfuJerVz1WGTIB7ekoTXT63z7Q_s6SSFU2uaosO3D_iwaVffQBMo1vuxJLGfQZBnCn-ml-JRfkekPMT_VRXqdC76kwvkxrGSGaa4WFGO559kzlvC7aAPWz35KZBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FBRmBDnrLXHaosCGRMxqvPmDlW1oKh6sEmMzlXWPss10JbKrk7LUiWqR4NjXoqAMj2RnViPq5WPiRH-l3tB1WrjLrLAxcvuDGK7F6VYuccG_z-fKAZRAFZzR5lIxnWGB3HpmjaYC8LbUFHH5o4Q1NRz-lSkpkdZW7i0Z5Jai8w0AiRtOTTbqn8zjTHIGE-39GOr3h7Kt_hL77D0BMhxU_X6ryhbveLjdz8N3oKwZcQRJhB72YY7sdgCZHlysnbAC9sEP5Gv7iAvisZW_HZoPfAg4hJSIYAB6NvWFMztdxApup-QiA5RM6ktJumkmlzY-pY-mSzi2PD7_afLM_DLtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/reMnsgmhLjnNGifB_1t0m52GofZPwqsSRqYxft2LJWjoQSgh23p5zbTZzhtj7Od3j1bYQiJynXEP4yedw-RMpoo1t-6lNjg8iQqnJW-TJ2gblwpIrk2My33OANlHrwpliW1xz6GwlH_uE8i5PxYUv7IwtEsu3-Q5OmZAhGA00gl6doeLKTw09UH_pGHx7EK2ESDpF1-S9KS-4MYxn3W-JNZTpQSTXvHaw1L3SvOAoR0FEvGSalFbhPeKbdpvbcwsN9x-bI847H1fz_Fcnwkbp_UoQ26ndvNhj45bOKYf66LRhi10rrfDU5R8tR0Y99SyNv6zMJCKl47SY26N-FFb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Aq8e1Z2JNDQqbtPoi23IsF1wqNJI8T4HUvWaV58RFd9KtorhPuaJLjnVt28NyjfPE2BREgqSWD8oANZqVqKli2bL2DuRgj7AiUGfH36VK4gyx01QZvNoLnLzY0LKCK6LiSvuJ8BUlpMHKXIwDmxj3QMU0X9U9f6jUjUhQwS_JwEiMva0xngF_gHbJeUaEy2tSu1DXHYiuxVZsQjiTdU6CrJfTm1cMCMUeag6EdTNUmb2aI8Terx19pJcRkIk9NQ5ocJ5FBjBM_ldtTOOky3Z8ufii5Hu4-DiTZi8O__u3Kj4EN8PzIJkGmM6CC3yuctN4Xiawu28VjY_F7Px0FDoXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر پخش شده با شرح: انفجارهای حمله به  اسلام‌آباد غرب در استان کرمانشاه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77416" target="_blank">📅 04:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77415">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCIiPHEPDp7XGvZKz2cMCPUHfKFvntLcvkMXMFknSORbD0dbtAcNQe3HpHG0PNuWz3rxooSl3DY00HNnGaun_HUzV4Qph2cvhw0qY3UZoIvxn18DeHZ7GvbxI0E2yztVUc_Ahl_JkoWLdUhanIuSX87KyBRm1rbsdFJuIpfvZyoGJ4vhOzxMZZxTdALz9GbVTpsdhsgggmm5dmb-4--7pdECz54725-XoxellHl-b3KErF-9OAzOGzqyUGi7M4Duu4tYtphZp0mQFhlw01KztEVPl7Px0C0bPvRSHTMBmpOEoqHYGsgukd9ZxciBLEQoanndyMhTLdIM_JcR9Zpg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش تسنیم، معاون استاندار خوزستان اعلام کرد یک نقطه در اطراف شهر اندیمشک هدف حمله موشکی قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77415" target="_blank">📅 04:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77414">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9aaff68657.mp4?token=afECZNYYjamYHXKw7EK5avGXPzQZhHIpTnzOf7D1MenyxrxKioro40f6wzBYaqcfLv5A_b1W3pjhR12Fse_7amVO6OJTy_ULsc3xvnbviU_dYLv7x-DBvBXh8CK8zN_OMAKFxBJOjAaWtzfuI56wTLhQvlLn1bq-wyjEbTg-uUg03bNDlAtPNLSvUp6e8JFswtZKHxIsmGbuudM3CM7Q4qmEbaTOZG2tFW3ESQ9teBGchte3CDqgEGdBwDn6r3UH6DrcW85Kx3wVtLehu5zoxaI1pbbkj6D6yup0fFKNTU7Rv7qQpufUtab2cu68tgjc3Mgfnomu11nNOrK4Kib16Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9aaff68657.mp4?token=afECZNYYjamYHXKw7EK5avGXPzQZhHIpTnzOf7D1MenyxrxKioro40f6wzBYaqcfLv5A_b1W3pjhR12Fse_7amVO6OJTy_ULsc3xvnbviU_dYLv7x-DBvBXh8CK8zN_OMAKFxBJOjAaWtzfuI56wTLhQvlLn1bq-wyjEbTg-uUg03bNDlAtPNLSvUp6e8JFswtZKHxIsmGbuudM3CM7Q4qmEbaTOZG2tFW3ESQ9teBGchte3CDqgEGdBwDn6r3UH6DrcW85Kx3wVtLehu5zoxaI1pbbkj6D6yup0fFKNTU7Rv7qQpufUtab2cu68tgjc3Mgfnomu11nNOrK4Kib16Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
وحید بوشهر زدن بدددد
بوشهر انفجار خیلی شدید
😐
دستم میلرزه بزرگترین انفجار
سلام وحید همین الان انفجار خیلی شدیدی بوشهر از قبلیا خیلی بدتر بود
وحید بوشهر زد ساعت ۳:۵۹
بوشهر چند انفجار وحشتناک همزمان ساعت ۰۴:۰۰
بوشهر زدن ساعت ۳:۵۹
سلام وحید الان بوشهر رو زدن و خونه لرزید یه صدا خیلی زیاد هم اومد
انفجار سنگین شهر بوشهر ۴:۰۰
سلام وحید جان
ساعت 3:59 بوشهر رو زدن صداش متوسط بود
بوشهر صداش خیلیی بلند بود
همین الان وحشتناک بوشهر زد
همین الان بوشهر زدن ۴:۵۸
وحید جان بوشهر پایگاه هوایی باز زد الان
درود، همین الان
3:59
بوشهر رو زدن صدای مهیبی داشت
وحید جان بوشهر
همین الان زدن دقیق ۳ و ۵۹
یک انفجار نسبتاً شدید ساعت ۳:۵۹
۰۳:۵۹ بوشهر صدای انفجار خیلی شدید و خیلی نزدیک اومد
سلام بوشهر رو الان زد
همین الان یک دقیقه پیش انفجار وحشتناک بوشهر خونه لرزید
از بوشهر همین الان یه صدای خیلی بلند انفجار دقیقا نمی‌دونم چی بود اما خیلی بلند بود همه از خواب پریدیم
ساعت ۴ صبح انفجار مهیب در بوشهر
چندین انفجار بوشهر
یکیش خیلی بلند بود و لرزش داشت
داش بوشهر بغل خونمون انگار بمب اتم زدن
بوشهر صدای وحشتناک انفجار، گمانم پایگاه هوایی بود... ساعت ۴ صبح
همین الان خیلی شدید
از خواب بیدار شدیم
بوشهر
صدای انفجار خیلی شدید از پایگاه هوایی بوشهر
سلام همین الان بوشهررر صدای بدی اومد که همه بیدار شدن
تک انفجار ساعت ۴ ولی جوندار زدن
آپدیت:
پیام‌های ساعت ۴:۴۱:
صدای پدافند بوشهر
وحید بوشهر انفجار
ضدهوایی هم کار می‌کنه
بوشهر پایگاه هوایی صدای پدافند
بوشهر ۴و ۴۰ پدافند پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77414" target="_blank">📅 03:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77413">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">استان کرمانشاه
فقط سه پیام دریافتی در ده دقیقه:
انفجار کرمانشاه ۳:۳۶
اسلام آباد کرمانشاه رو زدن
سلام ۵دقیقه پیش اسلام آبادغرب در کرمانشاه را زد ۲تاانفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77413" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77412">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppkocPz2Q104_OjTOXUrY42SfXxqa92EeWJjnWROcUc5gZjZMpeO_0hCIKuKvKhlVCBow2iTnIY_XOSORzQ1-q-1355xDoK1actshiFb3RGvUMd3qCxDF2gJxQHks7chFRjwPB5ngh7wR2AjzxoLpTKVd02RXBBy5IYCBVSh7xVUrAZylYdJt4iuRIOgOhGmfIurAes44F53P8SI_CUrA-j-uwG8fQaF0zACCX8uP9Qlbo7jgY_lZNTPQURQMHgP2mi04fHFaIATXn1UQHxVu1UqfV62Zyn0ZfQ1EbWTbgt7URhRTxrkhEQqRLT29jf_RsfHef5NWUosArQLjg9x2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران صبح پنجشنبه در اطلاعیه‌ای گفت که سه کشتی قصد عبور از تنگه هرمز را داشتند که یکی از آنها آتش گرفت. سپاه دلیل آتش گرفتن این کشتی را برخورد با مین عنوان کرده است.
سپاه در این بیانیه تاکید کرده که کنترل تنگه هرمز را در اختیار دارد و هیچ کشتی از این تنگه عبور نمی‌کند. در عین حال ارتش آمریکا می‌گوید تنگه هرمز باز است و هفته‌های اخیر ۹۰۰ کشتی از آن عبور کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77412" target="_blank">📅 03:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77411">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/733c9968e4.mp4?token=Nr0sN44WU0LFb13P-_byB-dXDo4Tu8g7C4cba7D9yCuBbhoHo5Gys1Knx-S8ni8JLYv3qfrgX6gPnfsQTLKA5N6048Hd_5rDuZCEjT8Uh1srqlP-gEYReEo30aRqpzdZe38MCoOtl6dfz1FQmcwSExPl6GD32X-Z5y5LvvzIBiafZiDlzy3WtGkMFx7HTnreYmu0GPcuTrGRYLlGSXQYqkzLIoGb-q_jqu37xo-04QNawy-H_7_p37ume-E37ATOB6Tm6r4vdeU2HiwJAmhyHmFTGUsTvOlz92O3uTAQLCL3cD1LzGL5ogj58mEbM5yDrsrLRnP7e05ou1gMMK8UEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/733c9968e4.mp4?token=Nr0sN44WU0LFb13P-_byB-dXDo4Tu8g7C4cba7D9yCuBbhoHo5Gys1Knx-S8ni8JLYv3qfrgX6gPnfsQTLKA5N6048Hd_5rDuZCEjT8Uh1srqlP-gEYReEo30aRqpzdZe38MCoOtl6dfz1FQmcwSExPl6GD32X-Z5y5LvvzIBiafZiDlzy3WtGkMFx7HTnreYmu0GPcuTrGRYLlGSXQYqkzLIoGb-q_jqu37xo-04QNawy-H_7_p37ume-E37ATOB6Tm6r4vdeU2HiwJAmhyHmFTGUsTvOlz92O3uTAQLCL3cD1LzGL5ogj58mEbM5yDrsrLRnP7e05ou1gMMK8UEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای منابع حکومتی: حمله موشکی به اطراف پایانه مسافربری در مرز شلمچه
ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: دقایقی پیش اطراف پایانه مسافربری در مرز شلمچه مورد هجوم موشک های دشمن تروریستی آمریکا قرار گرفت.
به گفته وی، تردد زائرین بدون مشکل در حال انجام است.
منابع حکومتی: کشته شدن دو نفر
معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: تاکنون ۲ نفردر حمله دشمن آمریکایی به مرز شلمچه به شهادت رسیدند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77411" target="_blank">📅 03:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77410">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SDHn8YDNJPDuRkMap2Q2CFh2gh2PDMnyxrxFbtIlrDfGI7JFekGeW8EZu3qEL0DeYga0gLMkC-nIQejd33ErvGT0CO0m4tTaL79FJFEk5E-0PRQCoZQzRi-2YNTLCcgHpz5uAI9V7sb6dSwM1nwH0Ex77eSqBkvgrHuHL--2UnfU5bPWN9YIC-x-y7Ax93Xwma0wfbbpp36PBln5mUTuCXJwKsXM4uKKYX0c7sCMrGAjKUNxm-AtxGTWr7gAKBACy_a-QpftPkXhWt7CaeOCWVwGoKRezDFLLKCWkf-z1uVbzC0NS7vQFch0XpTmzeyp68wXnZys2E8QB7gv3Xp-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا گفت تفاهم‌نامه با جمهوری اسلامی بر پایه پایبندی به تعهدات بود، اما تهران آن را نقض کرد و در نتیجه این توافق دیگر معتبر نیست.
او افزود تفاهم‌نامه شامل بازگشایی تنگه هرمز و تضمین آزادی کشتیرانی بود و جمهوری اسلامی باید حدود یک هفته و نیم پیش بیانیه‌ای در این باره منتشر می‌کرد، اما در همان روز به یک کشتی حمله شد.
وزیر خارجه آمریکا همچنین گفت واشینگتن همچنان از دیپلماسی و راه‌حل مذاکره حمایت می‌کند، اما به نظر می‌رسد جمهوری اسلامی در حال حاضر در این زمینه جدی نیست.
روبیو افزود، چین نیز با اقدام‌های جمهوری اسلامی در تنگه هرمز و اعمال عوارض بر عبور کشتی‌ها مخالف است.
به گفته مارکو روبیو وزیر خارجه آمریکا، جمهوری اسلامی با مشکلات اقتصادی جدی روبه‌رو است و شهروندان ایران با تورم بالا و افزایش شدید قیمت مواد غذایی مواجه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77410" target="_blank">📅 03:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77409">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنرانی ترامپ در ایالت جورجیا، بخش‌هایی مرتبط با ایران، ترجمه ماشین:
...
اما میلیون‌ها و میلیون‌ها بشکه نفت در راه است و ونزوئلا هم اکنون بهتر از هر زمان دیگری عمل می‌کند. شرکت‌های بزرگ نفتی وارد می‌شوند و قرارداد می‌بندند. کریس رایت روی آن کار می‌کند، داگ برگم هم روی آن کار می‌کند، اسکات هم با آن‌ها کار می‌کند و واقعاً فوق‌العاده بوده است. آنجا ذخایر عظیم نفت دارد.
در واقع، اگر آمریکا و ونزوئلا را با هم حساب کنید، حدود ۶۲ درصد بازار نفت جهان را در اختیار داریم. بنابراین ما به تنگه‌ها نیازی نداریم؛ به هیچ‌چیز نیاز نداریم. به تنگه هرمز نیازی نداریم، اما وارد عمل می‌شویم، چون مجبوریم؛ چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
در قبال جمهوری اسلامی ایران نیز در حال پیروزی هستیم و تضمین می‌کنیم که آن‌ها هرگز، هرگز نتوانند همان کاری را که با بسیاری کرده‌اند با ما انجام دهند. می‌دانید، آن‌ها بیش از ۵۲ هزار معترض را کشته‌اند. افرادی که اعتراض می‌کردند کشته شده‌اند؛ ۵۲ هزار نفر در چهار ماه گذشته. هیچ‌کس نمی‌خواهد درباره‌اش حرف بزند. رسانه‌های جعلی آن عقب هرگز به آن اشاره نمی‌کنند.
[ + جملاتی مربوط به مراسم سربازان کشته‌شده آمریکایی که در ویدیو هست ولی در پست جا نمیشه.]
---
بازار سهام رکورد زده است؛ آن هم در حالی که این درگیری کوچک در جریان است. من آن را یک «درگیری کوچک» می‌نامم. این درگیری کوچک ما با جمهوری اسلامی ایران است.
دلیل اینکه آن را این‌طور می‌نامم این است که، بگذارید بگویم، آن‌ها چنان سخت هدف قرار می‌گیرند و می‌خواهند توافق کنند. اما من می‌گویم هنوز برای توافق آماده نیستند، چون هر بار توافقی می‌کنند، می‌خواهند آن را تغییر دهند و چیزهای دیگر.
هنوز آماده نیستند. خیلی زود آماده خواهند شد. با وجود اینکه این وضعیت همچنان ادامه دارد، بازار سهام رکورد زده است.
---
نفت نیز پایین خواهد آمد؛ قیمتش سقوط خواهد کرد.
سه هفته پیش فکر می‌کردند توافق کرده‌ایم. گفتم: «فکر نمی‌کنم با این‌ها توافقی داشته باشیم. آن‌ها هر توافقی را که می‌بندند، نقض می‌کنند.»
اما مردم و نابغه‌های وال‌استریت فکر دیگری می‌کردند. قیمت نفت خیلی پایین آمد، بعد کمی بالا رفت، اما دوباره پایین خواهد آمد؛ شاید حتی پایین‌تر از زمانی که شروع کردیم. فقط کمی به من فرصت بدهید.
من همیشه می‌گویم: «کمی به من فرصت بدهید.» به کشاورزان هم گفتم: «کمی به من فرصت بدهید و ببینید اوضاع کشاورزان و مزارع چطور پیش می‌رود. این کشور با قدرت در حال پیشروی است.»
---
فقط در ۱۸ ماه، این کشور را به شکلی متحول کرده‌ایم که هیچ‌کس پیش‌تر ندیده است. فکرش را بکنید: مرز ما امن است، اشتغال افزایش یافته، تورم به‌شدت پایین آمده و کارخانه‌ها در حال افتتاح هستند.
سرمایه‌گذاری به کشورمان سرازیر می‌شود. گفتم: ۱۹٫۲ تریلیون دلار. ارتش ما با فاصله‌ای بسیار زیاد از همیشه قدرتمندتر است. می‌بینید؟ ونزوئلا، ایران.
آمریکا بازگشته است. از همیشه قدرتمندتر است و به شما می‌گویم که فقط در یک جهت حرکت می‌کند: رو به بالا.
تا زمانی که همین طرز فکر و همین نظام کنونی را حفظ کنیم، رو به بالا می‌رویم. اگر راه دیگری را بروید، هیچ‌چیز موفق نمی‌شود.
یک بار گفتم: «در کمونیسم، همه‌چیز به گُه تبدیل می‌شود.»
بسیار خب؟ حقیقت دارد. چیز وحشتناکی است.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77409" target="_blank">📅 03:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77408">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuFGzqSg8RiXASvBv8PN4DH54xu7Z5U9ol2oNXhfplHEpLonb3YZpL4ArzYRMQXFDzWQ4YljDJgdE-JfcKxmP1jvW7-7qbZgQ3k20x94OtVG8BTaoJ83avJ_n672DDShjh8rFzMxjDStRBuQAbv4pMB4nv9Qx4Nfb2Ky27zfk-9RVyKRUnFPzSZbPrtMM5PD8KuQEctKB-lzwnj3k0T0Wv64GPJzHNXQNGayf0hMtuusZjuifC8rh1Wsv_4AhNV-WHIqzgxI2bHcHobyQQj_ksibtR8h6gQ27eekEATqZRvRKY6OeaOI6eUzP0NwwXmLyf9RqMbQD2OdoRPdm0_BTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ستاد کل ارتش کویت، بامداد پنجشنبه اول مردادماه، با صدور بیانیه‌ای اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات پهپادهای «متخاصم» هستند.
در این بیانیه، این حملات تاکید شده است که صداهای انفجار احتمالی، ناشی از رهگیری و انهدام این اهداف توسط سامانه‌های دفاعی کویت در پی حملات «تجاوزکارانه ایران» است.
ارتش کویت همچنین از شهروندان خواست ضمن حفظ آرامش، دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای مسئول را رعایت کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77408" target="_blank">📅 02:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Samo0LRrMPT7ybZqzMqw79g-HqdKKOQUiZr5HrFbMkKP_WmY2G1-Gqmr5fyWzujq1ad-SrI-tqLe6NlsrEPIO2lQOfQi3p4xnIpNKO3JYPJygKyvntdFELJQO_ZugfrXahOlH6YG3AXJ3Ii-HtsadWqFNlnX6HFrsxi2Q3xLHMkeqQPCUBeddNthFabnNsGVvy3robAvmI6JbGPxf3r7PdetOsTHd3v0FHwVGZgh9JaCmov9SSVt4M9jY8PvoDaQZy2Z2Nef-fTLKVQgtaB76f158kp31XWZ9V6PWIHk5nsMYiFXExez8tqEwAaXlvSm1pljTCOPo7nIqTzfoe8Wkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۵:۳۰ بعدازظهر به وقت شرق آمریکا [ساعت ۱:۰۰ بامداد پنج‌شنبه به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور تازه‌ای از حملات علیه اهداف نظامی ایران را آغاز کردند. این عملیات ادامه خواهد یافت تا توانایی ایران برای تهدید دریانوردان غیرنظامی و کشتی‌های تجاری در حال تردد در آب‌های منطقه بیش از پیش تضعیف شود.
CENTCOM
نکته قابل توجه این که همه گزارش‌های امشب درباره صدای انفجارها مربوط به پیش از ساعت یک بامداد بودند!
حالا یا ساعت رو درست ننوشتند یا اون حملات کار آمریکا نبوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77407" target="_blank">📅 01:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77406">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sj3GoMx_ejhteHFO6RbnGG903oOFd5Fi-d7ffoB17Ga8EZrTbjfoWgd4x6FdMeUSLZV9FIwQ8boIgMtW_v-1Ydm0l8Uis16JjA-WzJLhmHmCEXecDtgwzVAWakyo_1qRFk6z2iyynLj88FV-PNpbxWwL036obuv5Ia9tJ5yZG-fLVE4-7Bj_rkEWghiuPY_aQxxSbDZErhYhNbh__WWKUmgH70v3449oA4qLhLlSbrD78RW1hs_7iv6qRmvHqLu7NbHWrk_B1qEiIpDLjQlCm632L-Ed6SSIJYfepe6pYEZwPLMeS8MNH6yeJ9I3nkFkwPgM2yQA4Ok9r-EMtz_8zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت گزارش در تصویر: ۲۳:۳۰ چهارشنبه به وقت ایران
یعنی قبل از گزارش‌ها درباره شنیده شدن صدای انفجارهای خوزستان و هرمزگان در بامداد پنج‌شنبه
ترجمه ماشین:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در ۷۰ مایل دریایی جنوب‌غربی الشقیق، عربستان سعودی، دریافت کرده است.
ناخدای یک نفتکش گزارش داده است که یک پرتابه ناشناس به کشتی برخورد کرده و باعث آتش‌سوزی در عرشه شده است؛ خدمه در حال حاضر مشغول مهار آتش هستند.
هیچ تلفاتی یا پیامد زیست‌محیطی گزارش نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77406" target="_blank">📅 01:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیام‌های دریافتی:
سلام بوشهر دو صدای انفجار ساعت 12 و 49
صدای دو انفجار بوشهر 0.49
بوشهر و زد همین الان
سلام وحید بوشهر همین الان دوتا پشت سر هم بد زدن
وحید بوشهر زد دوبار ۰۰:۴۹
خود بوشهر زدن ساعت۱۲:۴۹ دوتا پشت هم
دوتا انفجار خیلی شدیدبوشهر
پایگاه هوایی الان
همین الان بوشهر ساعت ۱۲.۴۹ سمت بهمنی رو زدند.
وحید بوشهر پایگاه هوایی زد
سلام،۱۲:۴۹ دقیقه دوبار بوشهر رو زدن
بوشهر ساعت ۱۲:۴۹
سه صدای انفجار
۰۰:۴۹ صدای دو انفجار شهر بوشهر
بوشهر دو سه انفجار بود خیلی صدا داشت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77405" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77404">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تسنیم:
شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد.
دوباره، تسنیم:
بر اساس گزارش منابع محلی، ۵۰ دقیقه بامداد صدای انفجار در سیریک شنیده شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77404" target="_blank">📅 00:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">در اهواز صدایی شنیده شده.
آپدیت: چند پیام هم از رامشیر، ماهشهر و سربندر داشتم.
پیام‌های دریافتی درباره اهواز:
وححححيييد
زدن
بعد از روزها..
اهواز ساعت ١٢:٠٩
اهوازو زدن
اهواز انفجار ۱۲:۹
وحید جان اهواز ۰۰:۰۸ صدای انفجار شدید
آقا اهواز زد دو بار
اهواز انفجار ۱۲:۹
سلام ساعت ۰۰:۰۹ اهواز صدای انفجار اومد
سلام وحید اهواز همین الان صدا برخورد اومد
۰۰:۰۸ دقیقا
سلام وحید اهواز یه صدایی اومد ۱۲:۰۹
اهواز ۱۲:۱۰ صدای انفجار
وحید همین الان ۱ ۱۰دقیقه بامداد انفجار شدید اهواز
وحید داداش ۲ تا انفجار ۰۰:۹ اهواز
اهواز به نظر میاد ساعت 00.10 یه انفجار مهیب بود. فقط لرزش رو حس کردیم.
سلام وحید جان اهوازو زدن
00:08  اهواز انفجار
وحید اهواز ساعت ۱۲:۰۹ دقیقه ۲ بار صدا انفجار اومد
سلام اهواز صدای یک انفجار شنیدیم
اهواز دو تا صدا اومد
وحید الان اهواز ۲بار پشت سرهم صدا اومد
تو اهواز دوبار صدای انفجار اومد
🔄
منابع حکومتی:
ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: یک نقطه در اطراف شهر اهواز توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت.
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77403" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77402">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErUdGD9XEmBa3dM8WDvVCFj47MpGAN1QjmyqmEEUW6Np42KnwZQinOdbpD6WC3ChT0exZNegc-bbpUNGgoryZ00urR1awx5NuJovkpRKLKDEL05TeCmPM_kxdSeMueTZ4tv9XQyVO6YSStPszyFblFpTBWrfj60E_idBza-p8Fs9zjpPAa0KkjxYePwZaqduLLle6HmovUFsXOhFbSxPJSbXaSSMt9iHXVwwUn54nnKDF0euHqDnEGZSe6srbIdTZB5xbHEidlKpPPc0UFnEjiN8xEr9jcd2412rVstlyCffqzb__87FrPJth0YJUS9LvtPOYfQZ19tQYFgcgDcVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: امروز نیروی دریایی سپاه پاسداران انقلاب اسلامی ایران مدعی شد که ورود و خروج از تنگه هرمز را کنترل می‌کند؛ ادعایی که نشان می‌دهد دریانوردان بین‌المللی فقط می‌توانند از مسیرهای مورد نظر سپاه استفاده کنند. این ادعا نادرست است.
✅
واقعیت: ایران تنگه هرمز را کنترل نمی‌کند. این آبراه بین‌المللی، صرف‌نظر از تهدیدها و حملات سپاه، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با حمایت نظامی آمریکا همچنان از این تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77402" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77401">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
دکترین دفاعی ما روشن است: چشم در برابر چشم.
هرگونه تجاوز علیه ایران، از جمله علیه زیرساخت‌های ما، با پاسخی قدرتمند و قاطع روبه‌رو خواهد شد.
کسانی که به هر شکلی در چنین تجاوزی مشارکت داشته باشند، آن‌ها نیز اهداف مشروع تلقی خواهند شد.
Our defense doctrine is clear: eye for an eye.
Any aggression against Iran, including our infrastructure, will compel a powerful and decisive response.
Those who contribute to such aggression, whatever the kind of support, will also be considered as legitimate targets.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77401" target="_blank">📅 22:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77400">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اکسیوس:‌ رئیس جدید موساد با رئیس سیا درباره ایران دیدار کرد
ترجمه ماشین:
به گفته دو منبع مطلع، رومن گوفمن، رئیس جدید سازمان جاسوسی موساد اسرائیل، دو هفته پیش برای گفت‌وگو درباره جنگ در ایران و برنامه هسته‌ای ایران به واشنگتن سفر کرد.
چرا مهم است: گوفمن یکی از نزدیک‌ترین مشاوران بنیامین نتانیاهو، نخست‌وزیر اسرائیل، است. این نخستین سفر او به واشنگتن از زمان تصدی این مقام در ماه ژوئن بود.
خبر اصلی: سفر رئیس موساد درست پیش از تشدید تنش‌ها در تنگه هرمز و ازسرگیری درگیری‌ها انجام شد.
یک منبع اسرائیلی گفت یکی از اهداف سفر گوفمن، هماهنگی با کاخ سفید درباره مذاکرات با ایران برای دستیابی به یک توافق هسته‌ای بود.
پشت پرده: منابع گفتند گوفمن با جان رتکلیف، رئیس سیا، و همچنین مقام‌های کاخ سفید دیدار کرد.
در حلقه نزدیکان ترامپ، رتکلیف یکی از صداهای تردیدآمیزتر درباره یادداشت تفاهم با ایران بود.
او پیش از امضای این یادداشت تفاهم هشدار داده بود که ایران این توافق، از جمله مفاد مربوط به تنگه، را متفاوت از آمریکا تفسیر خواهد کرد.
سیا و موساد از اظهارنظر خودداری کردند.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77400" target="_blank">📅 21:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77399">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پست قالیباف:
معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت. اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است. بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77399" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77398">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fdcc2765ea.mp4?token=rr7zWPyBLK0IOwHuI_-CeZRsYjRt3HfH8hfB_FxQMOodS1FFp_dRYtJ7MEyaBBe4j6LOzsgROF9ko-KsVRguxe9ZkHgxPQwGid-Q5MW0jWyYai60Acp1GW5e7_CP5IW217NqPmWLia-Uao4L78WSCNXh3x00w4pOuV7XwbhBycSNfuLQ-Rhp30CyuyC5IScKGXtpNGKvafL1pgdei1NDvpPAt3DsuWiSMBYDamOW7RhXqr_1YZeelo0XXUD2WHNOMUcZU2SBtWbu4VSdUV_ZZatxYcdX31n5aryzgMUVHYH3X_AXdqPKxw4xAhxL62RQS7-p5QjLghlK1FZmR5Bn_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fdcc2765ea.mp4?token=rr7zWPyBLK0IOwHuI_-CeZRsYjRt3HfH8hfB_FxQMOodS1FFp_dRYtJ7MEyaBBe4j6LOzsgROF9ko-KsVRguxe9ZkHgxPQwGid-Q5MW0jWyYai60Acp1GW5e7_CP5IW217NqPmWLia-Uao4L78WSCNXh3x00w4pOuV7XwbhBycSNfuLQ-Rhp30CyuyC5IScKGXtpNGKvafL1pgdei1NDvpPAt3DsuWiSMBYDamOW7RhXqr_1YZeelo0XXUD2WHNOMUcZU2SBtWbu4VSdUV_ZZatxYcdX31n5aryzgMUVHYH3X_AXdqPKxw4xAhxL62RQS7-p5QjLghlK1FZmR5Bn_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ کاخ سفید را به مقصد پایگاه نیروی هوایی «دوور» ترک کرد تا در مراسم رسمی مربوط به سربازان آمریکایی کشته‌شده شرکت کند.
تشخیص و ترجمه ماشین:
ترامپ:
برای ادای احترام به قهرمانان‌مان می‌رویم؛ و آنها واقعاً قهرمانان بزرگی هستند. واقعاً. آنها گفتند، و همه‌شان با قاطعیت گفتند: «نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد.» آنها سلاح هسته‌ای نخواهند داشت.
بنابراین می‌خواهیم به آنها ادای احترام کنیم. این برای من یکی از سخت‌ترین کارهایی است که یک رئیس‌جمهور باید انجام بدهد، اما باید انجام شود. فکر می‌کنم، همان‌طور که برای ادای احترام به این سربازان می‌رویم...
خبرنگار:
آیا درباره تحقیقات، اطلاعات تازه‌ای دارید که مشخص کند [چگونه آن‌ها در اردن کشته شده‌اند]؟
ترامپ:
نه، دارند روی آن کار می‌کنند. نتایج منتشر خواهد شد. می‌دانید چیست؟ ایران...
خبرنگار: [گفته می‌شود ایران پادگان‌ها را هدف قرار داده].
ترامپ: نمی‌دانم. خب، آنها بهای سنگینی خواهند پرداخت. دارند... در حال نابود شدن هستند.
خبرنگار:
قطعاً در میان خانواده‌های این سربازان، کسانی هستند که با این جنگ مخالف‌اند. به آنها چه می‌گویید؟
ترامپ:
خب، آمریکایی‌ها مخالف جنگ نیستند. یک نظرسنجی... یک نظرسنجی همین حالا منتشر شده. آمریکایی‌ها نمی‌خواهند قیمت بنزین بالا باشد، اما مخالف جنگ نیستند. این موضوع در آن نظرسنجی کاملاً روشن بود.
هیچ‌کس نمی‌خواهد ایران سلاح هسته‌ای داشته باشد. شما می‌خواهید ایران سلاح هسته‌ای داشته باشد؟ فکر می‌کنید خوب است؟ بفرمایید.
خبرنگار:
[نامفهوم]؛ به آن چه پاسخی می‌دهید؟
ترامپ:
تنها چیزی که خواهم گفت این است: «دوستتان داریم. فرزندتان را دوست داریم.» و آنها برای خانواده‌هایشان همین هستند؛ آنها فرزندان‌شان هستند. هیچ بازی‌ای در کار نیست، هیچ‌چیز. او فرزندشان است. و تنها کاری که می‌توانید بکنید این است که هرچه در دل دارید نثارشان کنید.
متشکرم. بسیار متشکرم.
خبرنگار:
پس مذاکره با آنها در بحبوحه جنگ چه فایده‌ای دارد؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77398" target="_blank">📅 18:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77397">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l9nX8PSyBDh3lg93QkU44RN21ztG7ITrX-tdy3z3v0JBpG-l_FnmIEjDMLyhZK6a37fIyI3RKhX3PAbobrfOFk5BE11VYgEW931utxc0F5LmvIrZzK4N5bmd0jLjGaiLThBdEG2nWAoDThO8YrcyuQ2_LsPodZiMsZRv67Tq5gNUpYQ1rNDuA-4mCW4iuzjSi--tpQGINf51xUhYfpnBqOBj1J2rQYY3syjTWXkSnd-ca1yLjjIyCsP-DcEgWeVU_C-x83qVfCW81NgMDuKIJnn9trvx-3ajL70sXk5l-pzXII9QwPqSQYZoUcDVeAiZOtsEv2HaRhlYSEdJRvBG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز چهارشنبه ۳۱ تیر، گزارش داد جزیره لارک در تنگه هرمز ساعت ۱۴:۴۸ هدف حمله موشکی آمریکا قرار گرفته و به گفته ساکنان منطقه، صدای انفجار شدیدی در حوالی این جزیره شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77397" target="_blank">📅 17:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77396">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eubOsOY-17Fq5l66kFce5Uweri5lNGeEvO39IiCcPC5Y7g64y20jkz8Vy5l2efdK2tzUAK79G1r1WeUzeqUU1KzB5fopel-bGBqalWue96bIT6BA7ScKL0G9Hy8Vh4cfCf9fBvbZEoEreVUwT-TTAgOxY4vWw4LohQYG1S_KXXQ5SnGlh3M18H5ZqMmzf3jEUmrlsn16iSHeVyx-A3ru54uttIwaDM1AZA33gu2alR80brtWSoUNUyNi0zy46jmTLTsF5l76NTFUcBR4Eony0b8EPzG67Lg4hPqeO_mRtYHw9VVq6zMVz4UswhoeXj-6mIhf7O6f4uhp4pgBppP9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
از این لحظه به بعد،
هر بار که جمهوری اسلامی ایران به یک کشتی در تنگه هرمز شلیک کند
ــ چه با موشک، راکت، پهپاد یا هر وسیله یا سلاح دیگری ــ
ایالات متحده
یک پل یا نیروگاه برق
را بمباران و نابود خواهد کرد؛
از جمله پل‌ها یا نیروگاه‌هایی که در نزدیکی یا داخل پایتخت، شهر تهران، قرار دارند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
From this point forward, any time the Islamic Republic of Iran shoots at a ship in the Strait of Hormuz, whether it be by Missile, Rocket, Drone, or any other device or weapon, the United States will bomb and destroy ONE BRIDGE OR POWER PLANT, including those located next to, or in, the Capital City of Tehran. Thank you for your attention to this matter! President DONALD J. TRUMP
realDonaldTrump
پل و نیروگاه برق رو با حروف بزرگ تایپ کرده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77396" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77395">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mJ6uOuD8FYFvwGPccMGYX1gjDPREzg3pIege0NakfC3T30AwBTFthymP0znBcYZ4win5asISfz2xqLp1TzYpHP6DYzYRrf4Qmf7PzAjBKMdJUB-RJU8tKDVTqtXEeMIoZL7UxL9nJvqGU3BSycqzwWwjAUHRIUaV6YdP6ZdyqzEjKaoMFk1X10GVEsZ_nv4XSojRGOI7OhO_tX_yL21A8bzCtoH04mrEejXV4YErRfy2RmzT4KDn2GGFJR-qVYmk9DTLE5zz-J7DJ5kyARwlz13ep1lIemxl4HWleezmH5G2mzc2DAGH6dj9l34Bq-lOiDARqZrtlyfdhB1_HsW7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز چهارشنبه ۳۱ تیرماه با انتشار پیامی در اکس نوشت که ایران هیچ فعالیت هسته‌ای در «کوه‌گلنگ» ندارد.
این نخستین واکنش رسمی یک مقام جمهوری اسلامی به گزارش‌ها از انتقال هزاران سانتریفیوژ به کوه‌کلنگ در پاییز سال گذشته به شمار می‌رود.
بقایی در این پیام نوشت:‌ «حملات و تهدیدات مکرر ایالات متحده علیه تاسیسات هسته‌ای صلح‌آمیز ایران نه تنها نقض آشکار اصول اساسی منشور سازمان ملل متحد، حقوق بین‌الملل و قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، کنفرانس عمومی و شورای امنیت سازمان ملل متحد است، بلکه دشمنی ریشه‌دار ایالات متحده با پیشرفت علمی و توسعه فناوری ایران را نیز آشکار می‌کند.»
دونالد ترامپ، رئیس جمهوری آمریکا روز گذشته و در جریان دیدار با رئیس جمهوری لبنان گفته بود فکر می‌کند به‌زودی ضربه سختی به این تاسیسات هسته‌ای ایران خواهد زد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77395" target="_blank">📅 17:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77394">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6910775c10.mp4?token=FbPv26DluMWIolEQoax7ecdjLphCSDQALLF2P4km70AY4cb3xa35LRV8nr2YLaX5H129tUPdYn05JGu281Cf5TOJst3tmKcE0MNxLllOMlDQqjskJvq2kfAKF3JIAuSkUb6OhK6s_4EhA2Th5XA4aNUnz9TC90WBGv5t0M-D5FaewRrOgUk8VBsbWcc8N-0J8gF4GS_7Zh07V8lrk5mWCWfsbzd9aLQwpXq958dwy_zaIBtjbFHqSb3yWl2kdphkW-pjcPkTeLnkAEyHO2iIqa0KcLRktWGSbzqaYTWMR2hR_75Wg9u9uuSYyLsKAyW6j3yWwBsAKZqKRxd9zNzi3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6910775c10.mp4?token=FbPv26DluMWIolEQoax7ecdjLphCSDQALLF2P4km70AY4cb3xa35LRV8nr2YLaX5H129tUPdYn05JGu281Cf5TOJst3tmKcE0MNxLllOMlDQqjskJvq2kfAKF3JIAuSkUb6OhK6s_4EhA2Th5XA4aNUnz9TC90WBGv5t0M-D5FaewRrOgUk8VBsbWcc8N-0J8gF4GS_7Zh07V8lrk5mWCWfsbzd9aLQwpXq958dwy_zaIBtjbFHqSb3yWl2kdphkW-pjcPkTeLnkAEyHO2iIqa0KcLRktWGSbzqaYTWMR2hR_75Wg9u9uuSYyLsKAyW6j3yWwBsAKZqKRxd9zNzi3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجۀ ایالات متحده می‌گوید واشینگتن برای تعامل و گفت‌وگو با ایران با هدف حل‌وفصل اختلافات آمادگی دارد.
مارکو روبیو که در مانیل پایتخت فیلیپین به‌سر می‌برد، گفت مشکل این است که «تهران در مورد گفت‌وگو جدی نیست».
وزیر خارجۀ آمریکا در دیدار با همتایانش از کشورهای جنوب شرقی آسیا عضو آسه‌آن، که نسبت به دور جدید درگیری‌ها بین آمریکا و ایران ابراز نگرانی جدی می‌کنند، گفت: «اگر ایرانی‌ها جدی باشند، ما هم جدی هستیم. اگر آنها جدی نباشند، آنوقت برای حفاظت از منافع‌ حود و متحدانمان به هر اقدامی که لازم باشد، دست می‌زنیم».
مارکو روبیو در این نشست همچنین گفت باز گذاشتن دست ایران برای کنترل تنگۀ هرمز، «سابقه‌ای خطرناک» را بوجود خواهد آورد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77394" target="_blank">📅 17:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77393">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0ShxsoPFfdXNSs0AYq0X9PFFGYEs8hhA8BoqNJd-AlHwBRgqnSL7ZR2HvmUeWTB2C5vBPyq3Nz7aH02O_gdHm9ye6wsHnrSfvGWMdNL7KuooolEr-Mxc4X95kLZlIqxWJ2MvdDJ8wGZZstz9Gf22oMrQgQAbpZk36a9jBuq7KZUW0LlJjrxOBoEng2DVGteRDFaDQpQjHyLgQI6MHAKTXE24CJdO6FwyxMm0ZnGqb9HFUn0tf25-8Iq-vBzwWBNaqCTY6O1P0MEpFfLGHsTiWpDcQ6N8lfxy01ZgTPN_bic8PXgwhnUDez4A_OsOp60T4rdA3ED3lT5gXklZ5GX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعدام آقای مهدی خانکی؛ از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴
🔸
مرکز رسانه قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام آقای مهدی خانکی، از بازداشت‌شدگان مرتبط با اعتراضات سراسری دی‌ماه ۱۴۰۴، خبر داد. این نهاد اعلام کرده است که وی پس از تأیید حکم در دیوان عالی کشور اعدام شده، اما زمان و محل اجرای حکم را اعلام نکرده است.
🔸
قوه قضاییه مدعی است که آقای مهدی خانکی به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا و گروه‌های متخاصم» و همچنین «ساخت، تهیه و نگهداری اسلحه، مهمات جنگی و استفاده از آنها» از سوی دادگاه انقلاب کرج به اعدام و مصادره اموال محکوم شده بود. این نهاد همچنین ادعا کرده که وی در ۲۱ بهمن ۱۴۰۴ در کرج بازداشت شده و در بازرسی از منزلش سلاح، مهمات و مواد منفجره کشف شده است.
🔸
با این حال، جزئیات مستقلی درباره روند دادرسی، مستندات پرونده، نحوه اخذ این اعترافات و دسترسی وی به وکیل مستقل منتشر نشده است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/77393" target="_blank">📅 17:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77392">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">معاون استاندار همدان اعلام کرد در ادامه حملات آمریکا، ساعتی پیش نقاطی در شهرستان کبودرآهنگ هدف حمله هوایی قرار گرفت.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
پیام ساعت ۳:۵۹
آقا پادگان نوژه همدان شخم زدن
پیام ساعت ۴:۰۸
سلام پایگاه نوژه همدان صدا انفجار پی در پی اومد
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد آمریکا ساعت ۰۲:۵۵ بامداد چهارشنبه ۳۱ تیرماه یک نقطه در خارج از محدوده شهری بانه در استان کردستان را هدف حمله قرار داد.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
وحید بانه رو زدن
صدای انفجار همین الان اومد
بیرون شهره نمیدونم کجاست
بانه صدای جنگنده اومد
بعد صدای انفجار ازدور  میاد
همین الان‌۲:۵۸ دقیقه
برای سومین شب متوالی
گردنه خان بانه رو زدن
همون تایم
پیام قبلی ایشون (شب قبلش):
رادار گردنه خان بانه رو زدن
ساعت 2.20 نصف شب
چوار، آبدانان، انارک و دینارکوه در استان ایلام نیز هدف حمله قرار گرفتند.
فرماندار آبدانان گفت این حمله‌ها هیچ تلفات جانی نداشته است، اما حمله هوایی به منطقه انارک در چوار باعث آتش‌سوزی در زمین‌های منابع طبیعی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 515K · <a href="https://t.me/VahidOnline/77392" target="_blank">📅 05:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77391">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پیام‌های دریافتی:
من تهرانم دوباره صدای پدافند داره میاد
پدافند مشیریه
دوباره پدافند داره کار میکند شرق تهران
صدای پدافند شدید افسریه
فعال شدن مجدد پدافند همین الان خ پیروزی
فعالیت پدافند شرق تهران. ۴:۵۱.
ساعت 4:52 دقیقه فعالیت پدافند شرق تهران
جنوب تهران پدافند 4:51
وحید من منطقه ۱۵ ناحیه ۴ تهران هستم محله مشیریه ۶ انفجار اومد پدافند به شدت فعاله ساعت ۴ و ۵۰ دقیقه
[صدای انفجار لزوما به معنای برخورد نیست. توپ‌های ضدهوایی هم با صدای انفجار شلیک می‌کنند.]
🔄
سلام وحید جان منطقه ۱۵ تهران همین الان ساعت ۰۵/۱۵ پدافند مشغوله
ساعت 5:15 دوباره صدای پدافند در مشیریه
سلام باز مشیریه همین الان صدا اومد
😂
😐
سلام الان ساعت ۵:۱۴ دقیقه صدای توپ های ضد هوایی و پدافند از جنوب شرق تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 484K · <a href="https://t.me/VahidOnline/77391" target="_blank">📅 04:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77390">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82b30de17d.mp4?token=pTR6eaDe2_9Zpca6SRbTexIdPoir2t-UYZDO5eOgKnPVKAqNQawukCKzI1M6hct9h0N6TrvJ9eqhGn_JRJmD5682QwlN_TnCpFF1Ov5pVSMCJPTNmdM9_As__kWmsCytxSXeu7dqagczhnJzzHE6aJ0KesCrWFFSyNVylN-hCsRf8P4KfVHDmVDwf_fw03tX5IqKcPi6vrea7nQxecFxaTfatXAx-ZG9HCrx25Mx-0dlKouY1RLWyFv7-EAUgTGTBQZv24iorcWU2a4vemOI40cp878YaCv9-CC3ag6ewMkLrsSvo8nG6t5Gu7ijnoY4PIhLuknCJTH3oFBrdYXbPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82b30de17d.mp4?token=pTR6eaDe2_9Zpca6SRbTexIdPoir2t-UYZDO5eOgKnPVKAqNQawukCKzI1M6hct9h0N6TrvJ9eqhGn_JRJmD5682QwlN_TnCpFF1Ov5pVSMCJPTNmdM9_As__kWmsCytxSXeu7dqagczhnJzzHE6aJ0KesCrWFFSyNVylN-hCsRf8P4KfVHDmVDwf_fw03tX5IqKcPi6vrea7nQxecFxaTfatXAx-ZG9HCrx25Mx-0dlKouY1RLWyFv7-EAUgTGTBQZv24iorcWU2a4vemOI40cp878YaCv9-CC3ag6ewMkLrsSvo8nG6t5Gu7ijnoY4PIhLuknCJTH3oFBrdYXbPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا یازدهمین شب حملات علیه ایران را به پایان رساندند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۸:۱۵ شب ۲۱ ژوئیه به وقت شرق آمریکا [۳:۴۵ به وقت تهران]، یازدهمین شب متوالی حملات علیه ایران را با موفقیت به پایان رساند.
تجهیزات و نیروهای سنتکام مراکز عملیات نظامی ایران، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز بیش از پیش تضعیف شود.
ایران طی سه ماه گذشته به بیش از ۳۰ کشتی تجاری در حال عبور از این آبراه بین‌المللی که برای تجارت منطقه‌ای و جهانی حیاتی است، حمله کرده است. این حملات بی‌دلیل، صدها دریانورد بی‌گناه را به خطر انداخته و آزادی کشتیرانی را تضعیف کرده‌اند.
با وجود اقدامات تجاوزکارانه ایران، تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. از اوایل ماه مه تاکنون، نیروهای سنتکام به تسهیل عبور حدود ۹۰۰ کشتی تجاری و ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/77390" target="_blank">📅 04:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77386">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec4c08a6e7.mp4?token=GzZy7uujDOB2MKwrQaoLzGFx6TR5PoDQQpJlN3GEUTqzeOdruosHIXpX74ZWo40iIdfO2QN_QQWiX7Bj_UUe18z-hFH2E1uJdZcGsdISAzieWW6vERPwD4mw7hJAQ1EH_GMc4B3eHjSVL08s-Z8fbskE63olljvjxwa0kNz3xkOVaJl06fdAYUeocdVNhX8I6r52OCCpF00vB41kCk-UKKFUVp73X1gwQ4vkcPIFCSHg159o5401W0O2LtcYJNO5oqCBTlb8Ytkj8HhzzwfurI0wv14TbaGR_qiH8dZ4lsU-pqHDSCVTL_5cawdB3RGrh8MO2MWcF2l5UafkjSfyKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec4c08a6e7.mp4?token=GzZy7uujDOB2MKwrQaoLzGFx6TR5PoDQQpJlN3GEUTqzeOdruosHIXpX74ZWo40iIdfO2QN_QQWiX7Bj_UUe18z-hFH2E1uJdZcGsdISAzieWW6vERPwD4mw7hJAQ1EH_GMc4B3eHjSVL08s-Z8fbskE63olljvjxwa0kNz3xkOVaJl06fdAYUeocdVNhX8I6r52OCCpF00vB41kCk-UKKFUVp73X1gwQ4vkcPIFCSHg159o5401W0O2LtcYJNO5oqCBTlb8Ytkj8HhzzwfurI0wv14TbaGR_qiH8dZ4lsU-pqHDSCVTL_5cawdB3RGrh8MO2MWcF2l5UafkjSfyKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی با شرح شعله‌های انفجارهای حمله به 'پادگان بخردیان در بهبهان خوزستان'
چهارشنبه ۳۱ تیر، حدود ساعت ۲:۳۰، هم‌زمان با آغاز اعلام حملات از سوی آمریکا
Vahid
📍
میگن
اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/77386" target="_blank">📅 04:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77385">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پیام‌های دریافتی:
سلام اصفهان صدای پدافند اومد
پدافند اصفهان فعال شد . سمت بهارستان و صفه
اصفهان صدای انفجار اومد الان چندتا پشت هم ولی از خیلی دور
ساعت ۴ صبح صدای پدافند جنوب شهر اصفهان
جنوب اصفهان شهر موشکی رو به روی بهارستان پدافند فعال شد ساعت 4:5
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77385" target="_blank">📅 04:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77384">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/47e213b66e.mp4?token=PZ1sUu2JRRGqKEkWd4cdfqRQn4hBpbRxSna8yZFchu19Tsv-azKO9ACv3MYLHUTMsgOQBuh0djyI-_s5gsP_89A-1S_IgDmFBUp77pELxAt2KoDkzB4xsGneZNv9velWsXNHEnMV7miElELNuqN6cTEK1Npf9ywsYmcNKfhww1QfkPGRZywrXkyDdJ8YVuUEAtn6mBeE4k3LwXk8SBN4X3Aa1nJPwAS0mOUmYPQPRfe7SeGBdk6wkUQEEkOdY1RXkKwIBoHm_3vL9iK1X6bqmATy_IplHBP7lDxjnGakVbizKcB_sOujDEUPC_ex1jpLjJ5toScZbglVUTvqxWYPRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/47e213b66e.mp4?token=PZ1sUu2JRRGqKEkWd4cdfqRQn4hBpbRxSna8yZFchu19Tsv-azKO9ACv3MYLHUTMsgOQBuh0djyI-_s5gsP_89A-1S_IgDmFBUp77pELxAt2KoDkzB4xsGneZNv9velWsXNHEnMV7miElELNuqN6cTEK1Npf9ywsYmcNKfhww1QfkPGRZywrXkyDdJ8YVuUEAtn6mBeE4k3LwXk8SBN4X3Aa1nJPwAS0mOUmYPQPRfe7SeGBdk6wkUQEEkOdY1RXkKwIBoHm_3vL9iK1X6bqmATy_IplHBP7lDxjnGakVbizKcB_sOujDEUPC_ex1jpLjJ5toScZbglVUTvqxWYPRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی ۳:۱۰
دوباره پدافند شمال شرق تهران فعال شد. شدیدتر از دفعه قبل
شرق تهران صدا پدافند
+ ده‌ها پیام مشابه از شهروندانی که همین صداها رو در محله‌های مختلف شرق و شمال شرق تهران شنیده‌اند.
🔄
ساعت ۳:۲۶:
ده‌ها پیام رگباری دیگر درباره صدای فعالیت پدافند
من حتی نمی‌رسم بازشون کنم فقط از پیش‌نمایش دارم آخرین پیام هر کسی رو می‌بینم باز هم کلی عقبم.
پیام‌ها رسیده به مرکز شهر و حتی مناطقی در غرب تهران
گرچه همیشه هستند کسانی که هر صدایی رو به برخورد تعبیر کنند ولی از حجم پیام‌ها واضحه که صدای پدافند شنیده میشه در مناطق مختلف تهران
آپدیت ساعت ۳:۴۰:
تا الان به طور پیوسته در هر ثانیه کلی پیام میومد. الان داره به حدود یک پیام در ثانیه کاهش پیدا می‌کنه.
همچنان درباره صدای پدافند در همه مناطق تهران
آپدیت ۳:۵۰:
سکوت نسبی برقرار شد. میزان نوتیفیکیشن‌ها هم به حالت معمول برگشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77384" target="_blank">📅 03:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77383">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای سنتکام امروز ساعت ۷ عصر به وقت شرق آمریکا [۲:۳۰ به وقت تهران]، برای یازدهمین شب متوالی حمله به اهداف نظامی در ایران را آغاز کردند. این حملات با هدف ادامه تضعیف توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77383" target="_blank">📅 03:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77382">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فعالیت پدافند در شرق شهر و استان تهران:
پردیس صدای انفجار و پدافند
همین الان شرق تهران
پدافندداره روی شهرک خمینی اتوبان بابایی کار میکنه، فعلا انفجار بزرگی نشنیدم، ممکنه هدف خجیر یا پارچین باشه
صدا پدافند زیاد میاد
ما سمت پردیس هستیم
سلام پردیس صدای انفجار از راه دور اومد
ساعت ۲:۵۰
سلام وحید جان از پردیس چندین انفجار شنیدیم الان
وحید صدای انفجار و پدافند شرق تهران همین الان
سلام تهران حکیمیه ۲:۵۳ دقیقه صدای پدافند میاد
سلام وحید جان همین الان  ساعت ۲:۵۰پدافند پارچین فعاله از پردیس مشخصه
صدای هواپیما میاد
همین دو سه دقه پیش
بشدت پدافندا فعالیت داشتن
پنج شیشتا صدای انفجار اومد
چندبار صدای پدافند سمت شرق ته
ران ۰۲:۵۰
پردیس صدای پدافند و انفجار اومد
شهرستان پردیس فاز ۱۱ از استان تهران صدای مکرر پدافند.  ساعت ۲:۵۵ صبح
شرق تهران(لواسان) صدای پافند ۲:۵۲
پردیس شرق تهران، چهار پنج تا صدا شبیه انفجار واضح ، ولی با فاصله شنیدیم ، حدود ساعت ۲:۵۳ صبح
سلام وحید جان  ساعت ۲.۵۰ دقیقه صدای حداقل ۱۰ انفجار از خجیر  که از حکیمیه شنیدیم
درود وحید جان ساعت ۲:۲۰ دقیقه ما پردیسیم
یه صدایی اومد گفتن سایت هسته ای پارچین زدن
پدافند شرق تهران فعاله
ما پردیسیم
اطراف (احتمالا پارچین)صدای انفجار و پدافند
[+ ده‌ها پیام مشابه دیگر از مناطق مختلف شرق و شمال شرق تهران که دیگه نقل نمی‌کنم و ازشون عبور می‌کنم چون تازه رسیدم به پیام‌های ۱۰ دقیقه پیش و از پیام‌های تازه‌تر بی‌خبرم.
هم‌زمان دارم همه پست‌های قبلی مربوط به شهرهای دیگر رو هم آپدیت می‌کنم با پیام‌های تازه‌تر]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77382" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77381">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر انفجار
همین الان بوشهر صدای انفجار
بوشهر یکی سنگین
۰۲:۴۸ بوشهر صدای انفجار اومد
سلام خسته نباشید بندر گناوم چند بار موج انفجار اومد ولی نمیدونیم کجاست
بوشهر صدا و انفجار خیلی مهیب اومد
بوشهر صدا اومد ۲:۴۸ ریشهر
بوشهر صدای دو انفجار ساعت 2:48
بوشهر  انفجار فوق فوق سنگین ۲:۴۸
وحید الان ۲:۴۷ بوشهر زد زمین لرزید
وحید جان همین الان بوشهر عاشوری صدای وحشتناک بمب اومد تمام خونه لرزید
همین الان بوشهر دو انفجار بزرگ
بوشهر الآن صدای انفجار اومد، ساعت ۲:۴۷
ساعت ۲:۴۸ بوشهر صدای انفجار اومد!
انفجار وحشتناک بوشهر ۰۲:۴۸
خود شهر بوشهر صدای انفجار
۲:۴۷ بوشهر، یه انفجار خیلی وحشتناک و مهیب
سلام وحید جان همین الان بوشهر صدای انفجار ناحیه پایگاه هوایی و دریایی
سلام بوشهر ساعت دو و چهل و هشت دقیقه تک انفجار
بوشهر 2:48 یک انفجار مهیب محدوده بهمنی
ساعت ۲:۴۸ دقیقه بوشهر رو زدن صداش خیلی بلند بود
سلام آقا وحید، بوشهر ۲:۴۹ یه صدایی اومد و در های خونه کمی لرزید
بوشهرو الان ۲:۴۸‌‌بد زدن پایگاه هوایی
سلام بوشهر ساعت ۲:۴۸ دقیقه انفجار شدید
من یه سر شهرم.. دوستم یه سر دیگه شهر
جفت خونه هامون لرزید
بوشهر - چهارمین انفجار «مهیب» در ۲:۵۳
برازجان (استان بوشهر) تک صدای بلند و لرزش زمین. 2:54
وحید صدای انفجار شبیه شلیک موشک برازجان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77381" target="_blank">📅 02:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77380">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c6ad0edf20.mp4?token=LDr3Bp9IvKZo9yeSdR4DX6uwLT5Wz3JpR6MCWSgIN132n7QFXx4--fsiXwalCoDf90o5WDMily4ZGSywg-VAnf039pUitJyspa4IPiHbuNmsSxJB-xRDJ5-qgFHDEyqkQGh6C49uZwuyWko4sK__sAsviuwkiiLRvNTEOxQM72kwyGcaA_BJq92XZnO7xjAoHrd0nfeVyuxH0ztVAe036p6i0dWFORROGuDj4kYlSvcznQQWGCp4privpxSjbNG_mFE1cuSN41BOWRBsl7PJTrOYGV2QuIo-Moq7o-uBHru5Ug0A-VTA21m1W7nENNhD0DaayzFTqSiughA2Wf5GIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c6ad0edf20.mp4?token=LDr3Bp9IvKZo9yeSdR4DX6uwLT5Wz3JpR6MCWSgIN132n7QFXx4--fsiXwalCoDf90o5WDMily4ZGSywg-VAnf039pUitJyspa4IPiHbuNmsSxJB-xRDJ5-qgFHDEyqkQGh6C49uZwuyWko4sK__sAsviuwkiiLRvNTEOxQM72kwyGcaA_BJq92XZnO7xjAoHrd0nfeVyuxH0ztVAe036p6i0dWFORROGuDj4kYlSvcznQQWGCp4privpxSjbNG_mFE1cuSN41BOWRBsl7PJTrOYGV2QuIo-Moq7o-uBHru5Ug0A-VTA21m1W7nENNhD0DaayzFTqSiughA2Wf5GIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
تبریز ۶/۷ تا همین الان  زدن شدید
همین الان شیش تا صدای انفجار تبریز اومد
پشت سر هم
۲:۴۲ از تبریز ۴تا صدای بلند انفجار یا پرتاب موشک اومد
سلام همین الان ۸ تا انفجار تبریز
سلام 5 انفجار شدید تبریز
سلام ساعت ۲:۴۲ بمب باران تبریز بیشتر از ۱۰ تا
۷ انفجار تبریز ۲:۴۰
از تبریز فک کنم موشک زدن
صدای انفجار از تبریز ۲:۴۲
وحید جان انفجارهای خیلی شدید اطراف تبریز ۲:۴۲ دقیقه
همین الان تبریز ۶ ۷ انفجار شدید
ساعت ۰۲:۴۲
ساعت ۲.۴۰ دقیقه تبریز رو زدن،حداقل چهار پنج تا صدای انفجار اومد
تبریز صدای ۵ انفجار توسط جنگنده بود
سلام تبریز ۴.۵ تا زدن
سلام همین الان صدای ۶انفجار سهند تبریز
ساعت ۲.۴۲
۷ تا انفجار شدید تبریز
همین الان2:43 دقیقه
پنج تا بیشتر زد تبریز رو و مشخصه سنگین بود و عجیب به مرکز شهر نزدیک
صدای انفجار از تبریز
۳ یا ۴ تا با فاصله خیلی کم
سلام وحید جان تبریز 2.43 شش هفت تا انجار وحشتناک بلند خونه لرزید و از خواب بلندم کرد
وحید تبریز ۸ تا صدای انفجار اومده
شدید و مهیب
تبریز موشک نبود. رادار رو زدن
سلام همین الان ۲:۴۲ بامداد ۶ بار سنگین زدن تبریز رو احتمالا سایت موشکی باشه
🔄
وحید دوباره تبریزو زدن
تبریز دوباره دو تا شنیدم اما دور بود صداش ضعیف میومد
دوتا انفجار دیگه تبریز ولی دورتر بود
تبریز دو تا صدا اومد
ادامه انفجارها در
#تبریز
سلام. الان تبریز پدافند کار کرد.
بازم تبریز رو زد، ۵ انفجار، شدتش کمتر از قبل بود ولی؛ ساعت ۰۳:۰۴
۵ انفجار یا بیشتر تبریز ۳:۰۴، یا شاید فعالیت پدافند ،(غرب تبریز)
تبریز بازم داره می‌زنه ساعت ۳:۰۴
۵ تا انفجار پشت سر هم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77380" target="_blank">📅 02:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77379">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
چند تا صدای انفجار چابهار شنیده شد بنظر کنارک بود
چابهار صدا اومد.
سلام وحید جان چابهار صدا جنگنده و بمب اومد چند تا هم اومد از 2/5 شروع کرده
صدای انفجار در چابهار
چابهار همین الان چهارتا زد ساعت ۲:۳۸
چندددیقه قبلشم یکی زد
چابهار وحشتناک. داره میزنه
۷ انفجار رگباری پشت سر هم
ساعت 2:30 چهارشنبه چابهار یه صدای انفجار سنگین شنیده شد
الان دو سری 4، 5 تایی پشت هم زد
چابهار همین الآن صدای چند انفجار پشت سر هم
خود چابهار نبود
صداها دور بود
ولی تعدادش زیاد بود</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77379" target="_blank">📅 02:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77378">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بندرعباس الان سه تا پشت هم زیادد زدن
بندرعباس پشت سر هم داره میزنه
بندرعباس سلام صدای چندتا انفجار ساعت ۲:۲۷.
سلام وحید جان بندرعباس صدای 3 انفجار
سلام وحید جان همین الان  بندرعباس صدایی وحشتناک از سمت اسکله باهنر اومد ۲تا صدای وحشتناک
وحید جان دوتا انفجار پشت سرهم بندرعباس 2:38 دقیقه، دور بود
بندرعباس ۲:۳۸ چند صدای انفجار شنیدم
سلام صدای انفجار بندرعباس سه تا پشت سرهم همین الان
بندرعباس ۲:۳۷
سه انفجار
بندرعباس ۳ تا انفجار پشت هم الان
سلام آقا وحید ساعت ۲:۳۷ دقیقه بندرعباس صدای ۳ تا انفجار اومد که اولی از همه بلندتر بود
سلام بندرعباس الان صدای ۳تا انفجار شدید ۲:۳۷
سلام بندرعباس 2:37 حدودا ۴ تا صدای انفجار اومد
بندر عباس صدای ۳ انفجار ۲:۳۹
بندرعباس صدای انفجار اومد الان
میگن سمت اسکله باهنر زدن</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77378" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77377">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سلام صدای انفجار یا پرتاب موشک از کنگاور
سلام ۲ و ۳۵ صدای انفجار و لرزش کنگاور
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77377" target="_blank">📅 02:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77376">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ماهشهر دو صدای انفجار از دور
همین الان یک انفجار دیگه
سه چهارتا انفجار ماهشهر همین الاننن
ماهشهر ۴تا موج از دور ولی حس شد
بندر ماهشهر ۴ انفجار
سه چهارتا انفجار ماهشهر همین الاننن
سلام ماهشهر الان ۳ انفجار
وحید خسته نباشی بندرماهشهر الان چند انفجار اومد
سلام صداها مثل ویبره هستن انگاردورازماهشهره به فاصله 2ذقیفه
ماهشهر صدای انفجار ساعت ۲:۳۱
🔄
اقا وحید ماهشهر دوتا دیگه زد همین الان 2.48 دقه
باز ماهشهر دوتا زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77376" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77375">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پیام‌های دریافتی:
سلام خسته نباشید همین الان بهبهان رو زدن
چهار بار زدن
خیلی بد زدن
خونه ها خیلی لرزیدن
وحید
بهبهان رو زدن
۴ انفجار محکم
بهبهانو چنان داره میزنه که هبچ وقت اینجوری نزده بودددد
انفجارها انقدر قوین که تا حالا همچین چیزی ندیده بودمممم
بهبهان ۳ یا ۴ تا صدا انفجار خیلی شدید
پشت سر هم
۲:۳۲ دقیقه
خیلی شدیده
🔄
سلام بهبهان همین الان ۲ و ۳۰ بامداد ۴ انفجار بسیار سنگین
شد چهار بار دوباره اومد
بازم زد
بهبهان 4 موج انفجار 2:30
4موج انفجار نزدیک تر 2:34
۷ بار زدن بهبهان رو
سلام منصوریه بهبهان هستیم
همینجور صدای انفجار میاد پشت هم
سلام توی همین ۴ دقیقه ۸ انفجار داشتیم
همینطوری داره صدا میاد
درود وحید جان ۷ تا انفجار پیاپی و سنگین بهبهان احتمالا سمت پادگان بخردیان
دود از سمت پالایشگاه بیدبلند میاد نمیدونم کجا رو زدن
حاجی ۱۰بار زدن در خدی که زمین لرزید
بهبهان وحشتناک دارن میزنن
سلام ، تا اینجا حدود ۹ صدای انفجار اومده بهبهان
از ۲:۳۲ تا ۲:۳۵
بهبهان ۲:۳۵
صدای ۶ انفجار
همین الان بههبهان زدن صداش خیلی بلند از استرس تو کوچه ایم
سلام سپاه روبروی بیدبلند بهبهان رو حدود هفت بار زد
سلام صدای های مهیب موشک در آسمان بهبهان
شایدم انفجار
بهبهان درب خونه ها از موج انفجار چند بار لرزی از خواب بیدار شدیم وحشتناک
🔄
پیام‌های حدود ساعت ۲:۵۰
بهبهان بازم صدا انفجار
قطع نمیشه
خیلی شدیده
حاجی هنوز صدای انفجار میاد
بهبهان بازم صدای انفجار میاد
۴ تا پشت هم
بهبهان دوباره داره صدا مياد، 4 بار
دوباره دارن میزنن
بهبهان دوباره زد
۴ تا انفجار
۴ بار دیگه الان بهبهان رو زدن آقا وحید
۳ انفجار بزرگ دیگه همین الان
داداش وحید سه موج بخردیان بهبهان رو زدن
۲:۳۰
۲:۳۵
۲:۵۰
همین الان بهبهان،جدای از اون ۸ تا الان ۳ تا دیگه شدیییید زد
ساعت ۲:۵۰
بهبهان دوباره دوتا انفجار شدید
ساعت ۰۲:۴۹..دوباره ۳ انفجار شدید دیگه بهبهان.
سلام رگباری دارن بهبهان رو میزنن
بهبهان تا الان 11 تا انفجار شده وحید
وحید جان از ساعت ۲:۳۲ تا ۲:۴۷ دقیقه صدای ۱۰ انفجار داخل بهبهان اومد
سلام وحید 2و50دیقه دوباره 2انفجار  بهبهان زدن انفجار خیلی مهیبه
باز هم همونجا رو حدود چهار بار دیگه زد بیست کیلومتری شهر هستش
بهبهان پونزده بار تا حالا زدن همین الان صدا ۵ انفجار دیگه اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77375" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77374">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در بخشی از نارمک تهران صدایی شنیده شده که معلوم نیست مربوط به چی بوده.
پیام‌های دریافتی خیلی کم:
سلام شرق نارمک صدای خیلی بلند مثل انفجار
من سمت نارمکم الان یه صدایی شبیه به انفجار پهپاد شنیدم
شرق تهران نارمک شیشه ها لرزید و صدای انفجار
تهران الان صدا اومد فکر کنم زدن
ساعت 02:01
سمت نارمک ساعت ۲بامداد صدای انفجار اومد
سمت نارمک صدایی شبیه به انفجار  بود ساعت ۲:۰۰
ما هم شنیدیم ولی انفجار نبود یه صدایی مثل زمانی که پدافند می زدن
🔄
پیام‌های تازه:
انفجار گاز بوده
سلام انفجار گاز بوده میدان ۹۵
انفجار نشنیدم اما ده دقیقه پیش صدای آتش‌نشانی اومد تعداد زیاد
نزدیک نارمکیم، گلبرگ
نارمک میدان ۹۵ کوچه مهدی
ظاهرا ترکیدگی گازه
کسی صدمه ندیده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77374" target="_blank">📅 02:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77373">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6HAnlpI48fg5ThV5RhyYOWHeG53wsUNu8MT5HvYohUYd3xe-J-71LvA-nl9Tliv4M5gnY9TGTp9aJ02-ODh5Y15ZjFGuKWQ9qXdkyCrFOsJAHDn0fBCvUWdC_YnMCILuKdsxdtliXpi4i3pgL0XSjcEr0HorsbKGX9XC0UQvg3YxkLJsJWCn2xz74AbRlcMvAPbe_7_EkIjQPPrZ9IOJv3Ykhjw18xsV8UYdnRc60TR5I22LzbpTqeUdjgLdbbSOsAQF0RrmNSTMGibspytTkwagIb4LIDj5phzH1NOtj0SfUE3SEgEDiPwkM8vkkaWfQo8ZC3Aw4sMxTGusFwVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد کل ارتش کویت، بامداد چهارشنبه، با صدور بیانیه‌ای اعلام کرد که پدافند هوایی این کشور در حال حاضر در حال مقابله با حملات پهپادهای متخاصم در پی «تجاوز گستاخانه ایران» است و تصریح کرد صدای انفجارهای شنیده‌شده ناشی از رهگیری این اهداف توسط سامانه‌های دفاع جوی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77373" target="_blank">📅 01:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77372">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">منابع حکومتی:
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): تعرض به مراکز هسته‌ای ایران، پاسخ گسترده نیروهای مسلح را درپی دارد
🔹
آمریکای جنایتکار مراکز هسته ای و حساس ایران اسلامی را تهدید به حمله نموده است. اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله ای بشود، آن را به‌عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77372" target="_blank">📅 00:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77371">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwXanHApGMl2cSGnRfK2LPmNg7bquZVoiCy3XcUNjirAUkrkA3xJbDm7l4q_AUIYVAgsRNxYycexsUsML-YiuoZCgKD26-8VElSbEiV2qIQRoNeiP54CCCK7-ENTDa5cGOvQ_xeqph6fRlgBM9ZVBwoyaY4O_eRh25FZ48CGI6jaf_bwMdhgZUp1pNQYNXgBl0-9b99lviUs_ElRax4xSgmmtcYGSzLVDEy-rwjB3ZjUsKv9KNffgokFysOQ6b-vaBiImRL2s8LT-kBtGStfI_AxXZBaYGxOV2eMkPQB1TFx4NrLrULn3OA5dm6ncWdni11Ckfai6ktmHvnx2_sRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع ایالات متحده می‌گوید جنگ با ایران تاکنون ۳۷ میلیارد و پانصد میلیون دلار هزینه داشته است.
پیت هگست این موضوع را خطاب به اعضای کنگره اعلام کرد؛ آماری که از افزایش نزدیک به ۸ میلیارد دلاری هزینۀ جنگ، نسبت به ارقام قبلی که دو ماه پیش اعلام شده بود، حکایت دارد.
وزیر دفاع آمریکا البته تأکید کرد که این رقم تازه، هزینه‌های پیش‌بینی‌شده تا پایان سال مالی جاری، یعنی ۳۰ سپتامبر مطابق با ۸ مهرماه ۱۴۰۵ را هم شامل می‌شود.
از زمان آغاز مجدد درگیری‌ها بین ایران و آمریکا، این نخستین بار است که پیت هگست وزیر دفاع ایالات متحده به همراه ژنرال دن کِین رئیس ستاد مشترک نیروهای مسلح این کشور، با حضور در کمیتۀ تخصصی کنگره، ویژۀ تخصیص بودجه، به سوالات اعضا پاسخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77371" target="_blank">📅 00:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77370">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PcbSVBKR722rYcf74jNpXu6L71vUgY6NuvXiR03cr1ViYpQh_D5l6WdZRrGiankppOwac0PWBXEiUt_meXU8gmeEBr8q-7TsrG42lX96_njuGit5HRryhOm3Xce0bdFOGxuTGG_lO2EifOOtG3OdakuqfxJj2h99GZvhHVBSOU5XJFbhzJRnNccGcQBXPoDS8aVrSkAQ97iWWQ0HWOIcwSmb5PGpzqDILabr0XjBF6HZTDo7CRf2XsKqcz0RHQSItRQiz-xAeXxmCsOVzxECrW7jLQteFg6u6LYexnqxIXgwJ5dZP6-khjhZLG__LXD4fGQjtHwdJxucpZeDXdbb3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
جنگ افغانستان: 20 سال، 2,000 کشته.
جنگ عراق: 9 سال، 4,600 کشته.
جنگ ویتنام: 19 سال و 5 ماه، 58,220 کشته.
جنگ کره: 3 سال و 1 ماه، 36,574 کشته.
جنگ ونزوئلا: 1 روز، بدون کشته.
درگیری نظامی با ایران: 4 ماه، 18 کشته.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77370" target="_blank">📅 23:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77369">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5abf96fd5e.mp4?token=hoVbOV4qktO69ReqfiA874JE7fuCC33ZkhrObwt8zMMBhOv9y-UtPOywwz7WXJ9MIMBhZ4X6tfrVyYPYBlZpCcwjp_jfMpWGpPJVuyD1OdceKGRzN4Yvf6rL2CX5woADo6bPRMz4po5Lppyzk4-BbEtRhWhxLLQh7bhyBeaYC74MckpxTpOrphiCnxIQJ3V1dH0Vnp6EO2pooicofSE1dX7L7vRmYsPhLNU-WmuheAI-UGW9Z4V2MhnRVLxxLyabkatqNkeCys2brNLn-elMnYV0jfQrBiuLM5PJ0sKdp870f2sp5kzQM7g4Bzdzf1EVbLQ8gxEpWR3eqkZGOQE-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5abf96fd5e.mp4?token=hoVbOV4qktO69ReqfiA874JE7fuCC33ZkhrObwt8zMMBhOv9y-UtPOywwz7WXJ9MIMBhZ4X6tfrVyYPYBlZpCcwjp_jfMpWGpPJVuyD1OdceKGRzN4Yvf6rL2CX5woADo6bPRMz4po5Lppyzk4-BbEtRhWhxLLQh7bhyBeaYC74MckpxTpOrphiCnxIQJ3V1dH0Vnp6EO2pooicofSE1dX7L7vRmYsPhLNU-WmuheAI-UGW9Z4V2MhnRVLxxLyabkatqNkeCys2brNLn-elMnYV0jfQrBiuLM5PJ0sKdp870f2sp5kzQM7g4Bzdzf1EVbLQ8gxEpWR3eqkZGOQE-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز، ترجمه ماشین:
خبر فوری: معترضان چندین بار جلسه ادای شهادت پیت هگست، وزیر جنگ، در برابر مجلس سنا را مختل کردند و پلاکاردهایی با نوشته «نه به جنگ با ایران» در دست گرفتند.
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
پلیس کنگره هر چهار معترض را از جلسه بیرون برد.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77369" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77368">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ4gyYByaKrxoPzRluMbcx5j5XBQ3Nqd-7wVvvFBsOHAoMZ9QeW4XrZs4R1etBdSo8dbFCRajwwtvrZX7OUi7Wv2Lv5SRYsxYNHGIr73F2fBY5SxsYlj3xSvO10dKT4Urz-fkpaPtb-xrYw207KN7W6BH7dzr2doFGpiSBTkovpHPPsoO5wJAM_o1ixRlCWQ8hqN__etbVcXVL98zBG66BYRKW-qmcBHdp0wyshYNdr2rX0mBkW2V3Lrk9jK-rdPZ8g9ZSJkCY5wsDRUnDJfcWR1zGulKrZzdDaqfKjko4cr9GgT4ZRku9e0bZ6jnoF0jjw0l0azGRKw4pga786Mpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز سه‌شنبه ۳۰ تیرماه گزارش داد اندی برنهام، نخست‌وزیر جدید بریتانیا، با استفاده ایالات متحده از پایگاه‌های نظامی بریتانیا برای آنچه لندن «حملات دفاعی» علیه ایران می‌نامد موافقت کرده و بدین ترتیب سیاست سلف خود، کی‌یر استارمر، را ادامه داده است.
این خبرگزاری به نقل از منابع آگاه نوشته که استارمر روز ۲۶ تیرماه نشستی با وزرا و مقام‌های ارشد برگزار کرد تا سیاست بریتانیا پس از ازسرگیری عملیات آمریکا در اوایل این ماه بررسی شود.
این منابع افزودند که در آن نشست، وزرا تصمیم گرفتند سیاست موجود ادامه یابد.
بر اساس این سیاست، پایگاه دیه‌گو گارسیا در اقیانوس هند و پایگاه هوایی «آراف فیرفورد» در گلاسترشر انگلستان می‌توانند در اختیار هواپیماهای آمریکایی قرار گیرند که مأموریت‌هایی برای مقابله با تهدید موشکی ایران و نیز اهداف مرتبط با تنگه هرمز انجام می‌دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/77368" target="_blank">📅 22:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77367">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R1iDFgj-nn1GMeGVcweBAgPgk-sR2UTYFjdQ25pdTUJkVIDC3vwAywLz0lcZQAF0SAk1ZLCXSv9bf9skWSaRH8lXbS7NnRhGepEGFWqO--qeDHOl272IjB10c_-07m9E5ORdzuFE94BrvXMUPkarBhxkCMRQuqBW2HKNACADESH6_ZiC7V73wIopqxEVm3QdhLy-79S3IIH6vK_nbRTy8V4LRGqxls5kFZhAZSxOPVv9JQ6BH4FBQwhOwi-OjXRfqzdR_VQjHxpuU_Vf6Wiv2bOUXVGuztzA55zeNbkneHX6CxK-nhb25dnxZtT42pRgPBursnueX9fmaEWMaF72xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیته دفاع پارلمان بلغارستان روز سه‌شنبه ۳۰ تیر با طرح دولت برای استقرار موقت هواپیماهای سوخت‌رسان و نیروهای نظامی آمریکا در پایگاه هوایی بزمِر موافقت کرد؛ اقدامی که با هشدار جمهوری اسلامی به صوفیه همراه شد.
بر اساس گزارش خبرگزاری رسمی بلغارستان، کمیته دفاع پارلمان از پیش‌نویس مصوبه شورای وزیران حمایت کرد که بر اساس آن، حداکثر هشت فروند هواپیمای سوخت‌رسان آمریکایی و ۲۵۰ نیروی نظامی این کشور می‌توانند به طور موقت در پایگاه هوایی بزمِر در جنوب شرقی بلغارستان مستقر شوند تا از عملیات آمریکا در خاورمیانه پشتیبانی کنند.
بر اساس این گزارش، آمریکا درخواست کرده است این استقرار از ۲۴ ژوییه تا اول اکتبر ادامه داشته باشد.
فرماندهی مرکزی آمریکا، سنتکام، در پاسخ به پرسش شبکه سی‌ان‌ان درباره این استقرار اعلام کرد: «به دلایل امنیت عملیاتی، درباره جابه‌جایی نیروها یا آرایش احتمالی نیروها در آینده اظهار نظر نمی‌کنیم.»
ساعاتی پیش، جمهوری اسلامی به دولت بلغارستان هشدار داد از خاک یا تاسیسات خود برای حمایت از عملیات نظامی آمریکا علیه ایران استفاده نکند.
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، گفت هرگونه مشارکت در برنامه‌ریزی یا اجرای چنین عملیاتی به منزله همدستی در «جنایت تجاوز و جنایت‌های جنگی» خواهد بود. او همچنین از پارلمان بلغارستان خواست با این طرح مخالفت کند.
بلغارستان که از اعضای ناتو است، بر اساس توافق‌نامه همکاری دفاعی دوجانبه با آمریکا که در سال ۲۰۰۶ امضا شد، پایگاه هوایی بزمِر را به عنوان یک تاسیسات مشترک در اختیار نیروهای مسلح دو کشور قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/77367" target="_blank">📅 21:56 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn1.telesco.pe/file/iVDIzHTnA6Bx0wDy9jhHLPzIno91DSQ5qWnm0OutHprHfJx2iM6m1P39MMN53HOMiMLHiRa8pXgRIyFza_0GIcW-QxWe8B0psbLybC5oC6-se16MOTsFPMvoKi3GX_m2XgluU20cVg77U4eX7PQxXMBY59FItFxsDoGRS0BilHGVG0IwK9Atz9BTz17vyJhWK9x6Vrk6F3ur9F2ZoKIo_qYnCS_TYUy2RB_MdDOKSxOJBqgcNBh8qOM0fj8JwOhisXX1D33MG8ztSmteyIiSCLBk1oyUofMhqARQ72sNXuFMKk29v0Hv_1ZO4p77Fl1jnfgnXU2A5NpjluZxqhct-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 14:07:51</div>
<hr>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RfcLZ1JlWdVbJYrvk6bSLr71RgjR3sJH0MTW_A_TjpKh-4AFWMazW9_IzRtKKZ3a05fwdGHhXb1Q__fWLgEGinb23kVMgRUUxsMjZ3fKXUKczkohW0dDYd9xlV9vPyP7e9nVN5YsQqZFTmGJWjVt7BWlJt_QG2YeHjk904foeD8j915nqku7ak2WvXH_b8_QzMkCS0Z3Kq98pnQpGPAQNtJ98ySAjcOmU9k_GK3Vuv7IlS9w5i6hJ0gMgD2LF0z-oRLKBMUCXQcbrkiNxeQgbaK16i5d16ViquBmYSLnBaX_YUnAYd7JEOXVeb5SMr4m4Muq0KIlFpySd9w5OWKYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUsDThUj9MXLgT78QPv677ygLEANDFJ4U_u-gRwU2NSrEMICAwav1Cqoh-9g7GS_e7u54QbfH4hT_Gh98YoQEKxVVWEj0Ncqlg-2rQcoK1PyrAUo-ymUwOXxUis1h3yxgmV5c5uyy_VSgwjJR8LCLuqx1G1y7TsD21STp5sSl1nQAWBfwnrw3vPpZVWhtYvfMtLBUzuNbwLQUHaVwE2QohwIUMhi8sVmK18I9sYkkRf0E_4vKqaNSiqUN__wdvAIOP8oTziA3qf9UB954pR6wOnHytqIwR39R4xcmes_4MVvn3VrbPGNyQwELe1FcpQYW8xxZc_IRmCBXkU1pdQs4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=p4PAmYrEDwO5UIMtQDO3FAi3DGcuEACQb8t-yk3MRm9lkJFZSP1q_mYUDd9V7kfs3KnudCK_aIEeevN6BQU63kWbrYJvDCUNIy-wYhttUEVn1cTCwTGnLTeY9fDe4bwJOnzEKRwXVjmjjhXRnclUpjRkdMBbhy118tYFD9IPnPCKauUS0qGQdIV8HZWTCfD_U86xHslQUU7RjJTo4lJjDBs2T7QxROXAH7-rbAdy6On4Wf_8UT7rBetlxFb6-JQyLjsJZlibB0feRncDHRiOq4Rx2tMxQSzPJoXyliqc35Sp1MIoYUIbHjamVHMeOh1eCFEfmYtsHyq4cpdw4Ze7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=p4PAmYrEDwO5UIMtQDO3FAi3DGcuEACQb8t-yk3MRm9lkJFZSP1q_mYUDd9V7kfs3KnudCK_aIEeevN6BQU63kWbrYJvDCUNIy-wYhttUEVn1cTCwTGnLTeY9fDe4bwJOnzEKRwXVjmjjhXRnclUpjRkdMBbhy118tYFD9IPnPCKauUS0qGQdIV8HZWTCfD_U86xHslQUU7RjJTo4lJjDBs2T7QxROXAH7-rbAdy6On4Wf_8UT7rBetlxFb6-JQyLjsJZlibB0feRncDHRiOq4Rx2tMxQSzPJoXyliqc35Sp1MIoYUIbHjamVHMeOh1eCFEfmYtsHyq4cpdw4Ze7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hruE5TqlVCrbcaAFuaN2tlRsJobuvOupi_kE03cYbtxcgdcE9_PXshcovUUK8btnt5JzBsTQxssh3m4398ktSMMly2yr0FNaAPpmzi2cwXlrC3g-r_LzYY9CbSivli-OkStI_amBiOdGdYmunGsDq9SLEt27wzp6azIf8mQ0ELpp13_jiRPg1heo0TCHN0iabMHHICDk1RAXUpWD4wwXm-I6abiKxxjArValBZEd8NeNyfehaQMQhLQnomQckUu-WySD_gIDVguBHj3k4GCrKL7hrw4CWZmhQA-o9K_fWNfK5OSCY10WPfEucCacleiiOv0Hj1AV30lxbuCegZ7EIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/km85LbQfl3DiQw2-2tFCpru4eTIpn-6HoFA-DXZFUOm21dvOKNt0QxFCcJuVXFYWUcG_xHZQ6IhBL-48dWgN5HJz2kh5rrGGJa6Lr7FRxMlrKiFwPjjY3yyPrlg4UNNyWpXHya--pdb8XjTFkWD8n-Z0ykvCMRCIUo_O1k6ov2Ui8OoO7BVuuROJ5hNiQ_T3Gp2wr-lNLKxB0wojrXxr8B5-XbXRXDg-HT3kdnS80_neGVN6w087WmdCYPLU1ClfFTMHMdyJu0uZkABhImFrfVPqw-4i70sOhYM-nbhLVRaTCesqXfVIFAe53x290ykcwRWaDH_RKaFbVNS-1BgfZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'آژیر در كويت'
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/megbstfNZw6UBRCri-TwjWHlnWravmCREW9enruJpQFwoWnIzr6YtZfmT--LevzKlrwThHJcQpmuPt2TjmE8t18KxLjIYWcOQD3HfFaLISYEPE6r5VuYdrvOnsb-hCcacjG8xeYzMpSJE8QEd78CcO8fvvM5dxL2EmSel1xJSgzP48x_n5CYaz4sA6vYU6Dgj65MHT1vGypLAWN_qFvo0udS0klvD0fG_z7KHyKoOwft9DpW6ij1mvaChyQoBh02qUIcMDNViD1kIYNmyICYT3b1lmviewUHFmAarxwP7DtdM3H_nwI1wLd6W1mUfHDuRfubqskiUjBYMrVRJa0Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=W43QFpJr7tcJbtW5a9cGocmfzg0x7OUU_PemUZlq-vdA5qpPviZyW77O2TJ_mtFT9Y7b_bhAk8Gstv4Hr2CnemMOlGlI7HNLs0M3U248WLh6neVHQQI_GgIKRBhZLitFQX6mZlLSdHxaC7BfF4rPXdAFRqkdAAlTgqOmlJEFkiyYGlbZRX1LvZCxqgbgXY8w1tRg5Bl3h3e11Mg_VnWlQfe1aodzHeGJSt-9wBdSjkNewK1cuDuT83kdTcEU8dvESNr7Gfi4MCmxd-7wa-plw7kUwZuGtYvH0K3ydeTj0M9DAYqVcyxoLeiTcZ5vtC-zkD7jHtfpgSm-oar6fQapDw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=W43QFpJr7tcJbtW5a9cGocmfzg0x7OUU_PemUZlq-vdA5qpPviZyW77O2TJ_mtFT9Y7b_bhAk8Gstv4Hr2CnemMOlGlI7HNLs0M3U248WLh6neVHQQI_GgIKRBhZLitFQX6mZlLSdHxaC7BfF4rPXdAFRqkdAAlTgqOmlJEFkiyYGlbZRX1LvZCxqgbgXY8w1tRg5Bl3h3e11Mg_VnWlQfe1aodzHeGJSt-9wBdSjkNewK1cuDuT83kdTcEU8dvESNr7Gfi4MCmxd-7wa-plw7kUwZuGtYvH0K3ydeTj0M9DAYqVcyxoLeiTcZ5vtC-zkD7jHtfpgSm-oar6fQapDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=qeVNmGI6qjtgvzsN8Or1H_0Q_ANtSTg4UNqD3PrQ2QpNQdol6KgkCINw29V3ut6HbPXpMWV-O5TZY47uiG3uL1qbEZ201HvOrbCOmN5seWn_GdRV40RbI7iQa64AG5rc6IdYoacNTdMnXonwSaCGamFzafaCN70vQJJyRTf0Sq-ogF9eO4GfDD1zmtmMtgUGfFNKy3Ja552Qzgpprgt6XDAYV4VSWCp9s5SJLFLwWmyA5Dr6Z496lB3H5TPMxT-pI__YlM9ACDplKIwhquQ71cJ7s1ihNGy1VElW11CgsLZdXqr9d4rHVaP0Ku5MCFHG9m1Vey1JVIUQMOdOqGsoxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=qeVNmGI6qjtgvzsN8Or1H_0Q_ANtSTg4UNqD3PrQ2QpNQdol6KgkCINw29V3ut6HbPXpMWV-O5TZY47uiG3uL1qbEZ201HvOrbCOmN5seWn_GdRV40RbI7iQa64AG5rc6IdYoacNTdMnXonwSaCGamFzafaCN70vQJJyRTf0Sq-ogF9eO4GfDD1zmtmMtgUGfFNKy3Ja552Qzgpprgt6XDAYV4VSWCp9s5SJLFLwWmyA5Dr6Z496lB3H5TPMxT-pI__YlM9ACDplKIwhquQ71cJ7s1ihNGy1VElW11CgsLZdXqr9d4rHVaP0Ku5MCFHG9m1Vey1JVIUQMOdOqGsoxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HO3TIcG4J5Xn_4g0X3SO86HI-ULX2qFNDIhmQiXBYJFhBJlSxfKgG8DTR0UgMUiDa25s5PJptuM7_JVHyXuQ4iIvfd-REhkHB9fDenEB-GJFlQRfcbCg8LhkZSTU7rTKYI3NebdrbYxI4of_qAvYzGPjgV4aALThQX7at-EuAfsXgOVsdqG76g96EMe11C-fQe2XWk_d75QyzM7y5pa3GQ5-eogRVr6T1SUudOukCtzJOSwf21qIYHENC05ecBWwzzmW-vQxgGO-v7Rp0zfraOY__-Sj27koIysuJnW71SiGCd7-rbIvPeiLZzuoAtyxnQTb9qQiEQWF99hr0xnW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Up7O-uxOzergf33zCbeDxQjpYvKyXabdKyTZHVAau3eHF3p7kR_nGy4zQixu2oNF7Nj_kFKjvsWomsJHOqgUXeSIsYSqhkjBhHDwm92y7qFnGmCETj9R_xtDKn6dmHuXPIjNeMv_Xp4vUGVxmvUwhBwN44h_H31TyKutu4VotyrMUtp8Y5WiTdUP6P9QJfC8Qc6EOk72JyY1Uw_AuOxqvkzJCd5JKXmNp5HPDqeM3yoTa4F3A4c28sdQCIxE3D_uw08hfsmMKJ3eH3OwyA-0qRll5-OIwm_oaw-UiydQHGz1lhMapK8lz2_1g2kmr6ai2iacVc4f3qWq6SrbV0bgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sj0zCfbqSCJT3DOubigNgptIENIHIUGEy4E79_5Brc-k_0Obkku0niON84i0IdkNZ8WZNoy4LYfDoQ0wVzOmN788O8yI_97ypRILWO_R0TzHNB8Ap3IrnprAECANcME-3vT_oORYQ8yzhcjPpAzwKGyIpjtsJkiy8CfL93GYs2hM2iLvOAILU70TfL7TTYWmlSP8oFz5eqDm6-jCka_Tw3Bv1U3bAF9DA4YxB96E9Bpl26JOGqIPVcnFeV568k56b508qZHYHEmGVKlkHJasqj6e6HwGbwsuTeqgIFUuKfGasUfe667oNobdcryW4Gn3PYN6w9NwQqvFgeVF8PYOdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=XSOnOEANUGdoU390cK4EgUaqzg-Hr25VKY9HddJSWzXbJExm2thwgcFcqTUNV3VG-LxjX29CAVpZeQz_gAoz73F1jaUCkBK8fuF7b2oNu4A5IXU4v4K-FWOEo7L-k2mJ_NlUhQATcSEk0nl_HjVwPVhDlg7YkaiFLHwNJldrxaeRE_1VuCJ4NOQu6go2HpaHmvTmhuZGOh6giY_Gpp2uWlFbNl-YPhREC6tvXMArP2yvfFnUAZGmK1OWHAOa05GNWxbfM4AYpkfXyHTxUAJvthNYtK8smKIG0xnMGLE7gYiQpFE6balOStSbpFbP9KMflCZ1dX7moOzg9I6a8vdFKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=XSOnOEANUGdoU390cK4EgUaqzg-Hr25VKY9HddJSWzXbJExm2thwgcFcqTUNV3VG-LxjX29CAVpZeQz_gAoz73F1jaUCkBK8fuF7b2oNu4A5IXU4v4K-FWOEo7L-k2mJ_NlUhQATcSEk0nl_HjVwPVhDlg7YkaiFLHwNJldrxaeRE_1VuCJ4NOQu6go2HpaHmvTmhuZGOh6giY_Gpp2uWlFbNl-YPhREC6tvXMArP2yvfFnUAZGmK1OWHAOa05GNWxbfM4AYpkfXyHTxUAJvthNYtK8smKIG0xnMGLE7gYiQpFE6balOStSbpFbP9KMflCZ1dX7moOzg9I6a8vdFKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pa2hXd6GTLn7T4kzyYS7J5ESTntMkUAbNsoqpily2k_ZpF2TKVphrJYmL2UhrxKwZObj2TkM0ngB9hbG3D8as8ckVqihuI7S96N_SNK_Fwt86bhbfRjo-QioPqPcKZg0jd7EH_9wUsyvwoyGlmn7Xnd1CEdfTy6_1_Y6k5Y0w_9peP5hJ-MbEUDJ3iOrDTO_E5qag0YRjNZFy1qsdacIJs_qKlJ-KQT-hGVL0oltCa1vdE2SIkGDvpmorAIJAK5OAn0k4qmnMQjmiZBxPftFRgIgNlu-x9KhsqrOinu2pmJl_xJOQuRxGt6PHk2z-YNRHKekyThciOImzR3ZjyflmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUxJ5NSONGkVCfCwvJ3XEndA_hOMqc4ZJd_u2cITANvfksKO5rtShdhR3m1QvxMHEZDw3VrpcYfgE_RktPjeQzKrMHtiqei_45CkcAEAl8apTb8u9Gu_UlzQaiKiDhLemv6B2m-yFrdVGIlisbBR39ApBHt_tMFZfTLjqxnkFGUJ-Qy0xUMZj8UiI88Qta_iDVdRr7HdeKs42Za2DPBO4NR5-dhGblDHCi224KYm4MXee2xAV4Qks-ds2SZ-BNF5AJ8AAbEhFMR6bCLp67mW7qJemDHtn5dzl-VMOapjl7Fm6qNf_lg0p_jpOmQzUZQrF7WmGNJWrBJFryItQin0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDmykcD3JBBz-QRuAWOFF6OFIUIKf7aeR0DdQfOsb35FIw5gulA_p2ECkJeWCDi4eLTzPUzhUDlC1W3cMDLr08XxTfm4NbFBfypgDQ1j2Z2KXxdwnaYO6w9dzkQINdi17wz0ywd5ItLb3sAkSxgkKSNi7NNzIRhOhR_udXx4VEgHzsLXVtce1Nf4RMr-LKHbOU8MPjqfMoSpxP0uWBoBGTN2k5AyU7gGTuIyB0FDSJAqajMlq2ws-3LeI6pviVclokL8eTMGYnhy6Y2H2MtfsWzI7Y9t4tczn7Crr7b92zQHIJwJBZQe-SnUJkhbwNfnhFLfPHp3NpeGIvBz30PAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckQCCVMuwng-XF388QmIlHM4inBnt411SFdYMzri1ER01QaU1UXunKGIq5QthfJ7UnURWaBj0HEeFj8IzxOGEqiKWZw0O-NfXgy2r8zzEcU6P-CJv-uboWI_WmamgPQlYfRMpQeQxwAdLVRD0TD7CSb1LUvEsSL8WNmrPxc1RDmRiyBNNATGw2jiM-mRAmhroemPuREvSH5x4PiBp-AFv9-NgBx_GQ2vRba4L_0iFZTQYzbSM7Dol2bKcC3uB48E6-umft5tfhmM84iBf5tev9akoNkPH0JQMssu3WVmmmp9EHKVpe0kPpkhNZTyyaTykyz0zX0EKbZ3ZD9UTQDoAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_vcM0ijmYGEH4sonxiHbnXruk54ZBt7LC5LSKygAw2rolBW_AZpzVTVAZydT5bnYOL_e6MSh8eOd7TT6I6DFgCMVIaKFryncyZHfJzZbV4FsmOz2MD_rwJGA7RJrrFrDHY1fYmAgQOLZhoLdLA6MJ2y-xfkGq54QFeEeK9AMvsBz-PeB8yxQ2vPn1bI7PradQkN5zoM3EYA7b4E8PTZR-qGwNbixlANXFDLDONzVzxYbz4GTOZYDNJ__IKQczQ3Vl1rE-4eiif2d_eMrEZSLtxRNtQ6OLduaugbQdFlwnHhPnM0SI6Hprupu5ii4QGrmc_-7klxkvf6Qbsk5TpQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FmrR0Zoog4nWrWebI8KpRp5y9yBis5WMHh7lJPbU2QRmH_rGLkKJoEZ0t7jCu0jjhBNM2CqetaL9kJN3e0pnupyTglzyYy4cqRuNXSxYBQS7A-LBxOmh90eT1Y25WJtyrLxxP6nZg-W6gijGprTloT5tgjIVGq8vYC1b-JEySudSd59I6UiaZp-X6g6QRJ4KsByz17ETV6wBZYVsq8_qh1k_atGXi7CPTm4ZIkzDZV8_NJDZJD3oyuWIuntQBiJzKEYNZGebA77m-meeJArWzPMLFlZpXhE6Igk5dfeaV5s2vN_PhWIdw4vvx3FoQbkWgINQDlr2cdswwuAFgDeJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MrqnM4sXaqNY5vH3xTmjhZ92CX1Drb0Xjym7tMbBuB_WUvVHMUE4qbPvNQ1AUIBQ6-eUe3S4ASMA-f8_spOAXwLUXcyTfjy0E_QqEHO7wSGuLq4jyNGKwRHc2_Dj6SPB65v7_aCgcoOSSXneo9e0oOxfYXW95neJxiRur2U5bPgZ_pMw4_pM3ps0ef6iBkS70OvJ8ZlKtOr-mx9Tjy9DwQuP0ZnRuIt7uDzQJPEmwCfLm2lA0hWszBF8WevUEewr6eWrkima7VCatYet7oXRgC2ouhTcy1vA7GUo6G896nWN3U96bFsMIi7OAFaeRECX-iNhag1vikXfCbklWjZ48w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I4VrRE8ts8JyMwWJ6ivxkZ8bB_ufGyRIXNG29ysKMjB1VuORWnBtg7Duvo6WVNJxLOa-Fp4ORaBVmFyUd_sMXOLPAa6dt8ZrGfVPs2yVrJjlZ548cIosWfscHMguHeVPDaC-oxZOEdnWMos3wsQkgv9hk8ABq0AegxiuiiaK5LDm0KUDIWb3m4g3LKIq1zM248ElJ5rf10fM8FE0Yr0H6NDTJH9G5M6TP9VzpBcL-bTaJaN8ERSn67mtBBtE_P37eeQGcq8RKCzg_FKq2bhF2sX9ixl0vOBJpY68IWYGiJLr4b2Rsanp9ZwxU3cUYh6tkeTrCFtnhEk3Xn2wklYe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=TO7afqoq2VQprpTyV8J77VGXxOfaTkQ9NIYDLrMnSl3jBe5xjFhKvHLTkdpXHiv-oMf4QFPQgH0F7oU8qqTeUQjbh6-774ZI_NrDXgQ8sfH_2ilT92yhRprufv2nSI_l3sK7S9CK0JIUy3XvOiUBhuGdKeW0Cf9un5d4gYwHrPAN3VpXxFxKWkhCACqL-fGqAKdrwWJDp1x04gLbZMRv1z9O58yBJBJRxPk9PTTfXRo3hEcy_Jud6_F1FLRTjUqSqjiV6BI_jViWP5XpA5e_f6cRv3BEgffr2StrqtaCkPe_O-bEcWCxaSSg2TLjOxWSVl2_1YkpxKOTXLeQTh2G8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=TO7afqoq2VQprpTyV8J77VGXxOfaTkQ9NIYDLrMnSl3jBe5xjFhKvHLTkdpXHiv-oMf4QFPQgH0F7oU8qqTeUQjbh6-774ZI_NrDXgQ8sfH_2ilT92yhRprufv2nSI_l3sK7S9CK0JIUy3XvOiUBhuGdKeW0Cf9un5d4gYwHrPAN3VpXxFxKWkhCACqL-fGqAKdrwWJDp1x04gLbZMRv1z9O58yBJBJRxPk9PTTfXRo3hEcy_Jud6_F1FLRTjUqSqjiV6BI_jViWP5XpA5e_f6cRv3BEgffr2StrqtaCkPe_O-bEcWCxaSSg2TLjOxWSVl2_1YkpxKOTXLeQTh2G8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db2iytxJkVfyr_Ht17PgINx5WNEVLBqFY8m4C8XVh9jHP32gSU6fSxoKXSVxXrTltUGkvwBrcXAZG9UCw_nUVjjkLqSAwHTODHDqG_2AUvM3eB0yPrfoutgU9c2OCBPf2utqOeitfMBEzzMbsrNU8YXarga1hLEJdmD1hovuEzQVcj1I9tdias-XqA51bLuguiDVgUqimNlvlc1oezyVHQgy9pC8Z7zqC5dpNkSTU5YSbft9E9d8nXXdvjsvUl8uCEPQ9XczzUTrR6_UWIt1w-N-6zR7BFafheAq7J_-loKS-0slalSHjqUM_WiTrQSe3Qs8T-0qsBKi3AXPlFos7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WRjhv1AAexRkZedNxa-LegsDMf9Vful4VgTq4E10ph54bDZ5KGglVj3RoaL_MEldj2k-jalZylwVivPjnoP5rktsuZS8bq1cwuLZ_7ORuf-IxPxEy6QlrocqiivvtvCIdwr5h2tSTYOruSvhaBwTrEx8ayjh3ssiJQ0hR0xUK--o5QY3N-9oiKSjvXGmKale_J_jcF3iEjhNbY3WNb-pD6LKtG6rgnRevvSCZhdWY7PwnhH8txIH3P476uZGldJD95pVDdrQjrRpO1K9_oqV72aM9FSj_-D6pU64ADQuIDv49pi8XUrlf5_lA_14W0YaKpRuEeRmWJebWMC_50uklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EspN4YELIqw-gJkW2ooO7TuTZgJX0ZZlPcvX_jVDfT2S_V8SSThFO_OaRnIuTmMwHOc6GD5AeGn7qyKbw62wpk2CFVoMdmpSuXPH2zqPjKs55lrXEcoU06za_O2c4B4qyY8HzSp-azzPyr3O9-9Gq1OZBIFEXBzhZJ4FIuAVTfmTz0Q6W04CTqtRPtzDfj-FGhXdAiR9t5-V0ERTi45pMGtkIkAu0fR7aDMKbA3l8vl20WikACzQMybZTbpjXUkA-hZjiZm2ireoceDwT2UFqviy1bsGebpW3-AH8r2FsVQW0qwWRRtU8qX5GUSt0dgLroi4N_EMmnEUnTyK6GVtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NQEW3zZ_wM99zFC6GHivARUCjQJIRsqwbZjPMkF3kogsem15PHW3KNrizbtUsx4ZXJw43JNoGGKcwXxJ4VQbrV7fRHsxXjR9Qb_HN6f_JcrTMen_iDWyal_31KqiGy7avPcLafYz8Rh1g9nyayc76o1roDdaEOEBlrUp-FAVSnbKopHpCTNDJhhX8EAaVjAE4-ziluRppagbAgIEo3PaUpiSzcnXDqdIm1B-XlE0D_6qm-KEchEe_Flls10iX2k3Rvxq381ehtvEcdBGsY2pjo5cz3hXSiumIkvBwzod-wiG1NzkhOIFb6qt7znCakCJwGP0aLhrmUhAvF2O4PaFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OAGOEupLKlfCC4vJauv0i7eP51Pjr_p4jJS770Dg_HwwnVIlMsw_v6U9vgK33RvVEaVGlmZZkrYAzqCa2ZnQaj_63HkWX8tsWlbPQXuwUhb8pSK0kocRKQxv26MlL-WqencJq7qT2L2xnAfX2S8rtL7zmwup5m81l4o_2bREqbxSX_0U97B36hfD55Rhv5BayEGnP8pvlMve3Pyyv-C-p2bw1mOGSSP5Ova1_SCgKRtq15Q8tRLWxkBXAIMbSKGMnxyYf5AmlZEBcF8qGqdNrzW3vwCV59jB4bB1_WZ7tJqz7Q8y1ZifLjkeZZOc8e7OA9sXrVrmkZhRHAkmoEer9jI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OAGOEupLKlfCC4vJauv0i7eP51Pjr_p4jJS770Dg_HwwnVIlMsw_v6U9vgK33RvVEaVGlmZZkrYAzqCa2ZnQaj_63HkWX8tsWlbPQXuwUhb8pSK0kocRKQxv26MlL-WqencJq7qT2L2xnAfX2S8rtL7zmwup5m81l4o_2bREqbxSX_0U97B36hfD55Rhv5BayEGnP8pvlMve3Pyyv-C-p2bw1mOGSSP5Ova1_SCgKRtq15Q8tRLWxkBXAIMbSKGMnxyYf5AmlZEBcF8qGqdNrzW3vwCV59jB4bB1_WZ7tJqz7Q8y1ZifLjkeZZOc8e7OA9sXrVrmkZhRHAkmoEer9jI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qtXXRiBxXVnDBtTAcG1M1fMSri-ulBck5oj2Vrqk1xIRwJyuVvvEdx99rSxj4ICuEQEPpObubXcMt4S8xglzKH5Ewsf-kAfLf2NnCLtIvxTwaQZ52GhWxmGZeW7Cu42e3_ZOjwpLIZfRH5QMdZVSReJlJn89l2RH6GuWuyajxQOdrt1qUxtMkcpkcRlJBAmavXCuYFFfvFo0dgUbZSdaJ7wQza2rXslI1JvLRsFOOy5-GtIMs51Rk5Mum59cI5bsmkCDYvsiRth2_zylawqzOgg-tyQEWVff-SwP-ChoLXq9A0QkZlDfzZDQEaGD1-IjBxYZsJUEiNZNjnLMEQdHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/frYnVVjZHayHBgKoZBEf0VjEWQRteuvWsA_sZlQCOOk5KVlg2Rw_qHKKGlXMu-96ia4JoO-wFetFnfa7bPqi1Y2m5p-FuiaCaHpngiuVnGjtTdfBL3HbRMT5reUqk9iLZAyOvfljxLw3ybK6Eac6YG8WfrNoUiultFixRvMOBmp8nbiXS4ahNJAr3uvFii-yXqc6NwJTyjq8PLvRdx2VkQkW2C9EbUmSDpeZGjfSCJzKBgE7x8j6EHYxZWkoTCYVe05h976Zok6TRp2enrJOULAg339GgoABfc_bMhS45IineNk6pjb2scEQGYsr5StVirlgNTyo4xfB2aFPlaIapA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=DN6qd20Xi3m_ui03h-iuQGNfYPQdg2O5dw1Uy4dHh4CgDAkgSFJ4WAK552kQNIr9Jpd6DHJNPvqZgGkKprLsDzi-G7HM0E2Ui0cc4BF31wXCtNwFkaaPTcjumVWBpr3fhB5dy__fEh0T3TR_eT50YTWCsLsouOnRiuvSh-TcgrtgQDk06XiuAJikhzVPgJ2e_yFiJDGCEW_fzmZgovchwM94QcJVk9VoufxprqVeuHMjr-_llN5X-3U1z8pr6KVkTA9McDdkQM56-VYaXUNbk0RgpTazvEcPyl58CEnQ3wJEHR2gVJwzQnSLRuXy-cLAJ45uhzb22QcgSVyYq93g3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=DN6qd20Xi3m_ui03h-iuQGNfYPQdg2O5dw1Uy4dHh4CgDAkgSFJ4WAK552kQNIr9Jpd6DHJNPvqZgGkKprLsDzi-G7HM0E2Ui0cc4BF31wXCtNwFkaaPTcjumVWBpr3fhB5dy__fEh0T3TR_eT50YTWCsLsouOnRiuvSh-TcgrtgQDk06XiuAJikhzVPgJ2e_yFiJDGCEW_fzmZgovchwM94QcJVk9VoufxprqVeuHMjr-_llN5X-3U1z8pr6KVkTA9McDdkQM56-VYaXUNbk0RgpTazvEcPyl58CEnQ3wJEHR2gVJwzQnSLRuXy-cLAJ45uhzb22QcgSVyYq93g3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=HNFjwSdz4S2HETaTUf3vaChNCmeo2CWO0WsfpyCor4c7JRnsKgu6SHAfvW8L2h6OepiQLWw0WAQ895UVAZCUa-Z25QHDUn2qv-J15wWqFgOyaUYbeF3BNcZb-JYhg2qPBbAJR3bk0d3vwcUqLv7emPr4GgK8NrdkXgGJj5e5sOr2Yf7NXvaU98ni4p6A98isaXHOrxiOo05n_cLsChZIuOqcoDRU7iT0YgnU6meQfSJe0WsVGLJInQXOPjVxsZtTRAbSOviM-w_oGavgz4GwyqRLyLmuEpH2XIqQifYrGL8ZEENhfc0Vo-zMWa-g_swSeaXiNS6n_dGQbmJTF5IY7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=HNFjwSdz4S2HETaTUf3vaChNCmeo2CWO0WsfpyCor4c7JRnsKgu6SHAfvW8L2h6OepiQLWw0WAQ895UVAZCUa-Z25QHDUn2qv-J15wWqFgOyaUYbeF3BNcZb-JYhg2qPBbAJR3bk0d3vwcUqLv7emPr4GgK8NrdkXgGJj5e5sOr2Yf7NXvaU98ni4p6A98isaXHOrxiOo05n_cLsChZIuOqcoDRU7iT0YgnU6meQfSJe0WsVGLJInQXOPjVxsZtTRAbSOviM-w_oGavgz4GwyqRLyLmuEpH2XIqQifYrGL8ZEENhfc0Vo-zMWa-g_swSeaXiNS6n_dGQbmJTF5IY7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=TdQ5DAOt7_ukYND7jwtRlCGFYuO0uV7EXMBpeUo5VEse9B0_5JKArLqHMBaIuc4hnQoH6s0NM8AFm5uSVBoOQz9euyN2vP-7qcHugOquQ04OKeLWU1lpCdcbD5nFqu-9trUNBR7C7lLKqPysB32t0HTq-ZdQRnjEeZc4dmT2N6wsvUKqAnWX0s0XAeychTyoLydAyJNzWkg2sOai8USVz8kXbwKnBGh5vRlWWd40jHDbwRrck-d9FLrRAlOQULRaYUg3RKCK5ZI8XAloE9Pya2aqUT1YT_-EihX-D15Va4xv_BoAtD4T8AjTbHu7PMytyaKob7AZ4mDK8YmWbs984Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=TdQ5DAOt7_ukYND7jwtRlCGFYuO0uV7EXMBpeUo5VEse9B0_5JKArLqHMBaIuc4hnQoH6s0NM8AFm5uSVBoOQz9euyN2vP-7qcHugOquQ04OKeLWU1lpCdcbD5nFqu-9trUNBR7C7lLKqPysB32t0HTq-ZdQRnjEeZc4dmT2N6wsvUKqAnWX0s0XAeychTyoLydAyJNzWkg2sOai8USVz8kXbwKnBGh5vRlWWd40jHDbwRrck-d9FLrRAlOQULRaYUg3RKCK5ZI8XAloE9Pya2aqUT1YT_-EihX-D15Va4xv_BoAtD4T8AjTbHu7PMytyaKob7AZ4mDK8YmWbs984Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0UmAjJ8DI4UeP-UyzoJdaIhRzOoE9rbAcu2N0yLnNBQMC6_A6xzoj9nmjUSzv6NiSDE01gWZMyq66hCVy9Rqn90JyMkRTRorcTRXtW0ePCQm-MhIor_bLKxCaPS2I8w8huoZil6xUAyyzUT20mi17URpryXoI1EtTyFJUDuB0kmTmGeQ_g-6f-jhpJ4FJS7awUbVzGAdBN3ITx7XZicD2qpDAh9m4HJ1AFOhZ-nafHXS0KoQQw6MEgc5GASX7mgA5u7OjnhKn1kA07jo2yKiUtdEbU_Zo-vl6wvuJxcqKUQabciTKOiXgqXV0fJCdQ5pPrnLciGrou0KxKJyQQBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qwKoURkHn0OZaMZGpgoFvecsh2ePi4E59y7aj44z4c_vqnCBT1j8i2aWlvgSMwgE1fy6wKJq04rAI2vz6XzAM9ox-3ks4tQGF9-q8u39ornBbPd1vwOdfJvfBejZyEE0t5Nbrkws-Aj62ExUI-UwtfF6BuhWZygTD8P1xHjGjP41UCS5QPvjL4l1P__zCoWSr5Ox-qU-syywu6Yf3Gt53qBawiP393i7N6AH0WYHmpYFQMpDQxtiB8cUfDT9Aqcy65AuTbCafI-gYYPJTKh4zQqIOgjKoyY8PEs1zUoBTSLX7SI9wrmnmIpL8wv0hDEAJdR4oPbQfao1xMH-zr1HNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI7LYr9VsxlKDkUiCq8hI2Z3oU9SXAKAoQVD6wRgxkmkUFFkBH3oGSY5jQjeycM2EtT2NoOYBNYNSQQ9yirLbLajfliH3H4qYiDJQ9F0CKXBni_Zmc0OahBLIdUAH1Ry3LLr5P0yScmSh2IwMeumG6h53Er05s_wmKRCkbzm3QuEHwMGv5KXLzS3-eHeqoUgsBDL6R1tQkBfTbAJTS0FzwkEuPBjHUxGv4SQpYuQIm1QHfYrj0phvYN7M8wACSVusMM-Q87NUtPHlvpKWi--PmFjtUS5Ayj4I-7QCaPmmOHt7E5UwS-N0oscJh5yn_CYd5DA6MQppX1Mg88dR3MY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HdRojgGXvoMXznSIItjbdAWYCk-82wc_MUdG97IFVz_831NCScKWuTJ5tG-g5kGO6gJdqoKTX8Sj6q2oR6P3BxzTutlafHj8pYv5sr3cSH1p0NgnyxnnU0goyVxdL5lheWNMKa3gysJO2dyRnT2WMtwuh6omn6xHRBlo_bno1dtb8W7MqSDR8EnauEIsD98T5DcpFc3hGqIdW4Q_kgUxmVfs40X84s3zmR7VrisZlziEhLv4YxTU01NrYK9G0TzzUW6Lh7IHYn8qeOadEy1rp7efMyRX3Ap8M6zzzFzjux4Sb8wdV76bbH1DM65A2-rHvgFLjNwLb1Aire8wBqmJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b3pv-4EHwJa4UufgHle0SKZhANBXcgeCPM4R1NBmIetn1c3zZYM9hixhvs_QiAgNnOeb5BdCniMlyBsewzP2859HyiJudz9VVSFFUHAB1GUWSRN0n5ZqbbI67cbtKotnsSrFoClz4xZZtd04ob5nv5ocWkj06OZgYtmB7U5y5rJwKkzpWoKEALZ5te7PrROBJD8lMAg8ghtus9mZM5-39JIfMfczYOyaZZ2G5CUtWnxa5M4H9KCGy9GlIerW5jminHu92h8u37b8m86lteCbmvCJhCk3XewjXNIoA1cjNkClpXlGhB_6fWTCvBlbFUH3Dmg6zspbZQsGL-ERHt1wDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B-01rOy8rXWIxjyVevwdtCWy_FzoECXl9G5bb08Bxs-z3HnsUDGpNTauEmiXXSio_ShlOWdoUVSxATIrtYtQBtWDUiDWx4k1ZVfuTSRK4Oj89M7PxO39M8GasP-XcWNFUTYmDqw3PUKuvg4eNk4EHJu6y2i43c0Fd0oDosSTaLW1Jxy731ggoH8Co4LZF6yk2T4rlzlidHiM7jwH86BoEeiTfRwiA-K_RnN_deXhqOxiSig-PqS7JAgb5MIkeeYxVegbmJhui_zMEqBwgW3NuEp2rUfOkjxOp-vmCtKxEg31YIuT-46FjlJgiv417jLD5bBc8vp3zC3N8reJqkiq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vUmL5Pq75h8orb0AGe9dBoPr4_E69fkifiZnsLtLHut44ZQNUMDQ8PP6alhZ2HHY0e-JqjdlkE2N8MJw994VIsyN-REheVFp_n_gRxtDn-DXzRpuXp_ES2F94zETtD0y-ldP9zKFazrTb4Kve42UfQaTy2G_12tW57v5QkCz7rDcF099zNK9iYXPJEtfPBLYuCeaUsJhz9zfWXRjTEoq-Nfz_3T_rdKicNNNOyOZEArb2ZaX5CcSvqP7FhkC8-BkWUsgOf8Med0gdU0X7g_OfPpg8oWgygNVscFjQFgvL0qsNNCq_FoiBhPyavkYwmD2thSyTpuJ8wzem3ctmdUMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QlNCAiRZjCDl5t1t5ZdaR0XJsNHZcrWFXufAeqfrHx8y0ok45uIk-PNCvgn5n5fou_nvr1tSx7LEBpIF3K5YcO5j0lncwqL6U-EQaoEuyFoCGo-amcfgfDx6cC_L6iT4XtJ6bmBaKF17dnEnRewSYR-3sjr7fEUvg11IL6_aE0PSUEAzQxP4Up5lt1evvuIs37BcTI9rPb637aK7b_SWzx6NlQ5DeymPkVOCrk-uS_98lIGZWOI77wY5Mtdv0UeaftKPxV-iRgNnOtJqq7MtqcHCuDdCrd8g4AQ7lS0fnbM7ybwDw7m5a4sENXxTd3kkti90iuAf6HkITT2vCppIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PlAGvGAhpG8tAiwmMFsmO9y034oXTljkCRh9E2RWCmVE2B6dqWAGxnKQsT9gscrpphWvwfjrlmdgvGdlNY3KTiRgzdVROMMdQ7_5cCffVzTWZ9kdfWbw2uXQIb_1c-4gfQFdofrzmQScD7J7xWSSSSn-icg_KYqAeUOWdMxjBPxbtFv3GgqR4K29sF-qxJO2v2Le5i6OmCAdz24OcnZUGhLiLT77c37ELSrOcoT1j7p3EzIkfeYzgp3DoMb5w6IaMv-4ALL0HBHr9bpe5V3GQUsuM-qWRtfivNwm2I-GjmR9JcvXIBuQYDMUTtFPRA7Vo_quUpo0lKWl5dmiKbHyRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hAcF5_ZXkAktDcBFoiliRDWV6SamBTGyyX7kq5OtU4gFEVj8xZj9WuS9jOqGy7lMje31vnsLUTCQrnpDU9clyzc2h3QBWkIz67Rf-_DOg0SpYABkDRkD5XpY1O1W4Oj87eO8-d0OhI7pXApfoXAtI_70fef09k7R3x_FE4fJHqly2CEq5MNjcTSJjlsLeQczhPi61kKTrSf4BcKULd41tq2Rgz-x618cBJexclHN9bR69gCwKD9FrImyhHn7nsUyDRqw9eAkq90sbVdK1nQf31rpe5dMN_zq7CLDREJ6XWbPRWAkD-_0S130AZTsYu3JRf4hdIDmoDWJvdL6FQbTSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gG7SSnnp3SM0dFo0EEXwBjiDhjZFv7FunKFaJM4zrVfzCpbnby2h6ISUOaqPVOF-8Il3L0iCbjRCUQVAUpc83wPVPVa0WOnHtulBIbihykZxNFAST3QjFcjse8X2pC0o7oK95WeH4bRUG01MAKADaGrjwYV320cr4pO936Lpi8fATeuQttFRj0bopJjA6k-AiAZa-RnqgPZ2MSPYycQ1GYdpb9h-CqILjgn91Vk59QHurII3QkOAvXDE7roGKqWgsRh9Da7DN_GRzSFv3vAtx3GwRIhkACkWJS63IhOAelUePOteZHm9QGFhFo16TxnP84lmPyNI8tulVlVSsVM-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iagWkgq-kFR35jA2nExmngugIqOBSIeS9O6US5T4HQ1l8TCIjwwgn5h3gSBK13Ljzh-1h0nQNdC9Y2tqdKKS9-hSLTsiK-qoAlmAXxsoL3dVUCNLdTJnbEypJ1Zix52juh29LnGoNhaHU3J4nQ-cRUbOl2gtxuU9k78Mc801dtFz5l71ssunJquo6jYipC1xnld5WTPvMhOs6RaBsBdrh7eMJ4fOfcxR1Qy1VFpyrrkbSCNWN4IVDyCABFAmoOT6RwB7tBDS3GAkynkoItrUStqbYqEi41UauuqGqIjyObOYxCuniGg6VIkHdTnJYgvOSe2IfWBkQVhI-iN1UG2vBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0UOa_dmKJ5U5MwPqftTaK31uc4CQU4Wtzdz6DuSweOamxmlJSLeYkLZvCEl-foxz-elzBYKXTdF6tiEiXkrmZiLlX8NYcrImMjvZA--HQ2uCPeAlCIhLTd8ff3bMQLxVlFAlVICo_D5yv4j7hW7vQXYpcj-KcprfevsqXoTHmzJzPMRHlKOMwmdCN7PIrJrSX1SJgZXQhJxt5CnRpiEfEZkjLmrDb8nk93Gq_X_KvQ4riPc_gSu81XSyJslVkA7w3KNGd7XgcP66IhsY8UbnJoLC7Qym4-QmMSXC3wOO86twHCeLDazALtSpObrPnaDjo78Hfx0qbm_HjUZ6BLyVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8oGMk1Pms3MFQdjnPqUaM3uFTcKycwO-WK6z26P9Xj8wzAZ4onLbqjOBjr9MtoMU4yy-HlTZanL1WURTBwCQjj1jH8p61deWOGv6LqxwN7JiK_Bh9CqLg-5phpZZzrBY-mguGqnuhzrjkj6itIlM7n1aknQK03hbwGD4zaRhxgMVX4hKSL75S7Mqz5zwWhpmzQeYBQvWiyyp5OPMwhnACJfEAS5nDB9Hz4wgxIFJo5pdDLeEApLTfGCE-FyVqGd26iyPLq9XaovhGAXQzfSfv3aQHu_iEfDqHYFyNzPBwBHHEZma8ovSMOrcJrj4KcUeh7uUSrn2mMx_FjeaYA2vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=U1j3woCntwx3Jcba3IZf1BC6nT__6nqHDk_1Pt-SNRCEEd0L8E4n3l4S5nd3acKC5jJX_eZpnk_e1GHxKl9Fj31pLfapyccBc8EXeyoBoBpRcGnCBE1dCnriv7g7RHslBimDDU0nN98zg8UERZMdwP9zyto1NLQ-KVXrbToG8w57SFats5ar2EP-THe4TcKYgqBFPbRLDUqFYp_d8zzHtyJ7fLmeD8qMtGk5JyTVLyg3Buzuqyh18QVsP9oLm-x8MaCV_nY5KOZK-jeWkq5O_EFbyYU4qmt9fJqVgE1HiOAoccDbXsyo8MsF2Jz1FDVputLcdmyUidyI_DOe4n-S_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=U1j3woCntwx3Jcba3IZf1BC6nT__6nqHDk_1Pt-SNRCEEd0L8E4n3l4S5nd3acKC5jJX_eZpnk_e1GHxKl9Fj31pLfapyccBc8EXeyoBoBpRcGnCBE1dCnriv7g7RHslBimDDU0nN98zg8UERZMdwP9zyto1NLQ-KVXrbToG8w57SFats5ar2EP-THe4TcKYgqBFPbRLDUqFYp_d8zzHtyJ7fLmeD8qMtGk5JyTVLyg3Buzuqyh18QVsP9oLm-x8MaCV_nY5KOZK-jeWkq5O_EFbyYU4qmt9fJqVgE1HiOAoccDbXsyo8MsF2Jz1FDVputLcdmyUidyI_DOe4n-S_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kimP1OX3i2dS0oh5kljm53dJE5RZK9prIN6GVarNOqnnsx9M51Z1f66FazLtzI1MZnKnALkNlylh2taDtJK3MZf-nAsgMxoQSa1F5U6krJ5Z_iiMi4XTd9MN6S4OheiuLkepsUSbcqA_dSCcCbfQUEQXymK0PgSwCy6JGxiRemI5sS6kKALTdkAgf689f20z3tOWdCf2worDzNU20CnPHG3bZOZYVjQFyVv2CAfXaYoDDwIZVGvuXWUQNzWbz5WSjFz9a80x4MEFfWSdb-SueRVJYW-0sNqf1NF3LNE0guQv-8kGXvyw6CIltxcDtVFbqtTx7L1pKs83sksXUUVl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kdxEX9TGhu5zFYC-BjbWq0xJkeh6iemdro-qL2tlqX_yUf8OUaJyqJ-Mr8JzDHXUSBDkoTKiADOzllgIKrPN2lFvVWf4ltkgnHee7AGaJcDBlrZG64LRKSm7W6D-YpZBCDZII2d8zrcHIMIQcqQTkz6phz_FR1DMyPfCjmcta3KW61aRj8KE0zLEcoAsQyHCGw5KvGlavGv97y2qicZHOrPCV7I0txDI8_pbsUfRtjM23oG-xZv_OtL0MVtZm6pFTTOyhtvafzfmPjR1LisuhnWvA9cQLsuKWbJfYODSXkw30axVUfkx-lxXDH2zBPT1mR_-BIhiqNr2UeXGLgAFYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B-N5FJlbkA2twz8Pt7HiNJYJksGGSedDMoI6OTwO7V1_vwKQH3aKq5dSSbVJKH-n1uSLaUgOpSrkv4bF2whlU2XhcOv5fIbU1nrAdirviOzaHDCVaSAPI8ikWsElP2aeZujlbAXtGOoErgQkscr9W9PK7ev2YEOtc8tTsn6wS79J6aGZYx_dxOCFAqzU3S8dhNQcOVh0KGsVD4Y3Ex1jCoJ2x4yH4aI0StuNq23ToBT9U6hTZ_drqJP8VD4SCk_C1SpNk-PbAnQh0e7OCRwlEnzYCxCA1339jC4LtsqKK0D_QzaHsjHfizMT7UcPt3dmRFLqVWo81ymnxjkGwPbsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RFLYuFC5VRtaLJFv1L_E5viCE68K6nFmaOOyd_MDCMTkHPBtgTaegXGPu_wP-F-E82HWKNHiAjskUW6X74RBxa7_HRV9HC4dfBqID-WsIcU42kgZXJOR3cgqNXkf6PZINyJWTMFLE3IjHvRUH4uOfWeac24vonDeUeCJcb8Mo1ISO0l9mSq3hoCrMYdk9TGMZg0DYgoa-esDKi7IY5fUgWl5bh3SF35QCSDjWzU6RMpt2gy6h09uUYuBQRG529jXxCbcEO5sHTPXiRGpX01tRYe8BzRrL7-yifvFWnJ5QK9wtPsKSxF_nKh38gSqMvIkJBGm_4eAB-SEbQkYLLgt8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KdA1hc7W90n2QE7stkCQGVEmAoNdGLjSdP8gaW9xbSkzZWkhfYvLuYpitKLvkDsbNDHIaJfcrd2P-k4aWjMjZhGXtvYUg8V5atZM6Yq3jS6HV2Qnsy5U6uD7VVyf_Nf4sZZLcmxmdXDL7S19L-c6u04B3TWr1R8REn8sCo2CJsHgCEo7chr-u393JaAfJE4eb34sWOJyxbc8Chm9iceN59WqAJ8j8-P_tOXBDMB3JGcLWq379wsDoEdR4GZ_tHF1BJPOsGkOLp3KCH0LMbsXWWbUWBScQBPu7G2IgiYKVJPKW4xTY1w1prVVKuh9ZTfw1-v2usdDV7bAmhK0m6Nl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mvpxDbPvH1xI0giVX44_fUINHUkBOy7-NoYZkCqH73oja-Row_9Co5xIAVOsncY4Qps8sMxsfSHZpwGoVjimtwwVObCq2G0fuecaWJHhK7O4s6QW2_881_NoCAF9QUBWCRbi5u-QyK7nSXo0K2LTikhtsAOFIguWfkiDMPwlNdLf_pS5Zx6P9eDY1uanCQ4QjE9NDJ9GeVgqLC17NTUOEHWiPETZIUb4sLlrrmZCoPvyOiUnuy61IE7kJb6HkfWz-u2CX9PDw5uTAYjOpasdqmISTnnEaeym6muA6H-xSj11ehzBreIktHkdHviduJb8OvQKJeVNDMRVzv5olL6EGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=TC4uck27JjrMTd7hChjHAB1R5uy283XQn777SIUa5cTLfJVw8mg09e80VDr5-cuKXlMrFowF4HYUcmxpDumnqADIthIhmwzqBUywP7JvR3QCrnF_pcvzkj0LfDjUTvONWwmcrp3pQeZmjeeo1xzu9Dlz__J8FB4SrzEWvD4mqFXbwLpIfTJ1Dr6JdxCUdasqntaK9ciXbM6Xd8HuBUoWtMWh3DTm9vzsgdcnp6oynN796dlcE5ThJBoBMFs1mTqML5Fl_9I5rpVSwrrR6t2OQAcNbNqqmJAS-7omYWw_PdSGvzymkge4iFpCNDZRpa-ESp471nutFc6YXQC8QQ0cgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=TC4uck27JjrMTd7hChjHAB1R5uy283XQn777SIUa5cTLfJVw8mg09e80VDr5-cuKXlMrFowF4HYUcmxpDumnqADIthIhmwzqBUywP7JvR3QCrnF_pcvzkj0LfDjUTvONWwmcrp3pQeZmjeeo1xzu9Dlz__J8FB4SrzEWvD4mqFXbwLpIfTJ1Dr6JdxCUdasqntaK9ciXbM6Xd8HuBUoWtMWh3DTm9vzsgdcnp6oynN796dlcE5ThJBoBMFs1mTqML5Fl_9I5rpVSwrrR6t2OQAcNbNqqmJAS-7omYWw_PdSGvzymkge4iFpCNDZRpa-ESp471nutFc6YXQC8QQ0cgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qy5mtxw0Ip4zHWIHxkoQ3zwPMbJ5D8uDb2ubJZFeNfZ9JFoC1WmEkVhuBvhOePV3v2d5HE58PFEsEtjb9Zt1ziUkG_i6CinB_HIGzpWb6xDV2DgLjbpT97-rWYkHVyXpHR6Jiu8PMoMLm_akWANMMu6wDYCOfVmRZQC4gFvoBSvzml_Il01Q0uStBHMME-lt6l770MNDqQwkDab-PwND1NxJLNVWbTHVqy3uooVp1xQoCPNpeil93Ap2LBPA_WEUp7lYS7UOJjDzhAe6s72xvqC7c-cT79Ua43eMZ9QeH-cuaHaRcwXL3dOqu2v_fMr8EUiGPBIXO5MtnfF8edtsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=SgkjxRSuHs_51nc4vI4Bj4XwPAMaooADUrW2Nnxk5MXK6kXoNgccB3nRoL8mM4kpO_oZcLhiYjI1v5noH_zqM6odxK52MzB64_t8lLmjIIRyLtqcrKhmeeK2gJ1cyqLttPnd3W2aVKrBcwJ16qXLl-iNTUf2EtP3Yr50DB5r_3VWjMgJAAeRIqcWrpyBbSHWSYHsCEioezhKkFkc322bvsVwKYVe_O6DaYrZaCSGv2N1g2tZdChnh8RIbQVbsQkm2OePqNjpL179lXeYDMcBAps5sh6bO0lui381kISVfGk00-sgz9tKO7plic7gN4uqAfSSpWD5IzmGbGbZSmlryA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=SgkjxRSuHs_51nc4vI4Bj4XwPAMaooADUrW2Nnxk5MXK6kXoNgccB3nRoL8mM4kpO_oZcLhiYjI1v5noH_zqM6odxK52MzB64_t8lLmjIIRyLtqcrKhmeeK2gJ1cyqLttPnd3W2aVKrBcwJ16qXLl-iNTUf2EtP3Yr50DB5r_3VWjMgJAAeRIqcWrpyBbSHWSYHsCEioezhKkFkc322bvsVwKYVe_O6DaYrZaCSGv2N1g2tZdChnh8RIbQVbsQkm2OePqNjpL179lXeYDMcBAps5sh6bO0lui381kISVfGk00-sgz9tKO7plic7gN4uqAfSSpWD5IzmGbGbZSmlryA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtMwVRgf-SKgl6UOfSH0D3FwrgePV9xO_TmiC6W_UMVhrxvAFiFF2NYMShL1t-sl8ehdrWVgr4F5X2jX-nnw_W7lDQqdi-Gbh5qnXdcP7OS6EKLDcgPZHb3QoeE5ym7nkWdbJuuE1MY-VeKTUCj2YVZ6k61j-QJeMiY-vrb3A5En6eM8P5xliethcsM39OihkEgCE5raZWOzNi4ySz5Vk30jbWoOxNd_EDNpA6roq4ZloGi0SqI1F2uutR_wtb560Xv8UkXweAITJY1It1ZkBNK0WenhY_An9a6ifdWbpu1R1JQ0Xue9lR66BYLSS7E9vcTRjsLaeYl8Ig9Zz9jcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j7vcE9OGsGx8HeS483NQIehPGujE4cJyq5O_7TysNHAruj7vbgXRgo5hHrKdie1HaMjQe6SCYowEcEaWQNxps4VlfEM8YFRMQVXMGRvU0OwuSofg3IVVMunbPXgguflXbl1VLSYeieib8lJLxT46IJ_2qrXpyJG4nguIt0OXr01oGNlJJceM7nP44feG6wNPykbFJbz1tScJ03v4OzqegQCk264Yx5cB95iIphIz-VWMcsfL4NPwjKkD2CHXlxXPVxtZsYHnaLA0uvzCIkwodnjusvEZVLa1Ym2nRddQMT2turyOyDl6x2saTX_IkkZBshoiic9WFhY9g_axWz6qpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O05f10guNXkrFpUuL0wmnwC3qg2aCRqO3hS33hXqAT1sFEzDqhLyT4ClCkqO-C3dD9x2nfffoBnD2gZxG27kvlT6ZZ4eTYTXeWT0c6LnqAqG6SkSI0hl9qgMuGeDWPYB-oqz8UGx6QJ2X-z3aE02lXlORXCc8IlGH2kfM5S6PghKcxiNvxTWqLgoqUuAjPGzHuo_sWRa_OiswV3hz6pzGeEeqHoS0XqHLVF_iJRFWg_xB28V_PV9xIdDb4GLeuakUJiQ--Uj3DmXcJlIGoUFIb1G6xfFI9Ght2M1r8T4O0DrzEZUuIXL643nrapoSCFpfyaHkDQJ8qL6dVJFAe3evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvyCZfKbWwy4SgPsLUv850Xc2MzHLHIhy1uq3mvK64pPrfyHl_fx6lD3WM9difZd0b1ZNWNg3LEYgish2xuxbo3ZiQjUPnyHrGqEu9U4ycXIoGsfaYXoYBeE95zMVeKi301PkKOy-4a8sXItNRuQS2WJ-5mm3Zzd7RPrHlOcZh8oMA_SL-qVJazPiszlG5glFvIoApe8Mg2VnY14Fs2Kbw5QUrl9GkUVn24IcXeas1FrCUgvozV76d3EISNinNykUsc3PwCoaBniImLZwu-ANSZuaTDBSJu2CN03ehRKzbOQE38oH2WsNY7zYrTxdcegXV_XWtSPIGX3rn4-NULNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/llQVGkqxclKImJtYuXm2ANcDkafNbsMegJoCSOX8EufLM8UPLgGFlJB0JOpSk1zrgV2eUPFbKUVIaQcTSNlrP056ydhMrCR9g4rSf8XBkt3GQ8lV9lJGUFPTJpecAZvOgxqr65Cf6Z9-OQlw3bMFK3Ssv6hOklTMEdcdiG_jCdule6zEba2xLK28EsZ-OHsvEkM9Ho5baXpa9lFbtORhz8DuCLIAuJFukB2sxNl9RE7pkF3QGG8LgyuqFu2n7DDhTmo4w5RqoSnjnAjA5wy9lfQXHHfdnQOA4u6lh67pUVxHBZrhFlk7qSJpXZR8fS89VxVCfdhyVNVBRENEpKkq_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=UrJkC5B-b7aQP5Ebam6lMkngS5VKhm5-1M_pec5S0JLFDZAcS1kzjEGttK8i8Ucf7RsNn06-gEH0EPJQNjebhf6_1yIkJIdKyhfu2R7pPRtZHUMKdEEIOOtkLdYJXKOM1CNXsonJSeiTQEz3f2ylDXCOsa8dmmpY9LFO6MHia6d_jQW6vrhHVZNXkQG2D9wo7-RLJ0FIQUzSHgpDA0LTzhbHDGJdicyQsz9eJLg2MvZePVEb02oiQbDTuAfP7trf3Dkd0EEug4OABq1WJnAJ7gu1_gZIjU3SCBQv_ZBxd-hGzIV3GZY521W-cnKOUL9DX4aGYZBOhzMqyMWqRyapyY_CguCj9SlmTYJMYaDOyPHQQ2qLz-yF03KSeEBTYhSAP3rcqQ1m_YDN1ouwV2i7OiSO1Upjb-kfb8Gxc2HxI9f3-QYZR_X3l_KYNXmrtkrJxiHjEsNblA1nZrBP2OE-VpZNLLQgzIrLJhcrDSPDidPqfe_Y9RLjvdDvWgVX-t0mGMjVRYuxGTFYYYxGt32a50zuZPEsApkqrolIFk1LHO4b4A4G50PvYT1ex6M8RO-zDcySO2nF-QLLJHSYEiuuaYXtHGHjMkH28T6iTlOEDEBNBDxCwmBeZAo3Dt2CPEP-5eczyopIRrdSwOdbDop_d-nOY4FqzlsGET302fHjyj4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=UrJkC5B-b7aQP5Ebam6lMkngS5VKhm5-1M_pec5S0JLFDZAcS1kzjEGttK8i8Ucf7RsNn06-gEH0EPJQNjebhf6_1yIkJIdKyhfu2R7pPRtZHUMKdEEIOOtkLdYJXKOM1CNXsonJSeiTQEz3f2ylDXCOsa8dmmpY9LFO6MHia6d_jQW6vrhHVZNXkQG2D9wo7-RLJ0FIQUzSHgpDA0LTzhbHDGJdicyQsz9eJLg2MvZePVEb02oiQbDTuAfP7trf3Dkd0EEug4OABq1WJnAJ7gu1_gZIjU3SCBQv_ZBxd-hGzIV3GZY521W-cnKOUL9DX4aGYZBOhzMqyMWqRyapyY_CguCj9SlmTYJMYaDOyPHQQ2qLz-yF03KSeEBTYhSAP3rcqQ1m_YDN1ouwV2i7OiSO1Upjb-kfb8Gxc2HxI9f3-QYZR_X3l_KYNXmrtkrJxiHjEsNblA1nZrBP2OE-VpZNLLQgzIrLJhcrDSPDidPqfe_Y9RLjvdDvWgVX-t0mGMjVRYuxGTFYYYxGt32a50zuZPEsApkqrolIFk1LHO4b4A4G50PvYT1ex6M8RO-zDcySO2nF-QLLJHSYEiuuaYXtHGHjMkH28T6iTlOEDEBNBDxCwmBeZAo3Dt2CPEP-5eczyopIRrdSwOdbDop_d-nOY4FqzlsGET302fHjyj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeRQP9PW-Y4pttBtLZgGNE-fl5Ul1hEMz3R8iRqxuy_Bs__iMc5eG_9JN8-OzOPwuIRBm6zG82mjaEGStbRVfpvJ9TmiUp2p1KqUHMxJqtiHVtmk22dejXBrHPWck2JaeMgDTvbCZo3Wdgo7b1VBFiqXCYD5XADKlHyMkqLhdr9YY1XlmxtC3ojXhCxEwC7Gka8ZXlVwol-d8p_tUxk9_KPYnLLA8WsVwIo2MUX-Vz7R7jqzj5B5qu8XEM1DhvOU8y8B-xWveHrgQlprBDUd8emrpW3XtptrJPbX1yFDbjOCsyf9yBNf7ahB8weQzGJmNsPSPtCeXiNoHngANWm9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=oLp8eBS1c60dJMb0GDpsa-Zeiq8UImIybarP9jlLSSFET4T2Ne-ADl1M0TmuvTWw5UV_IMWVrsG7wL-r4YANyRLeFskrQ60KwQ7yfNkLhBybiHPn-Uj4KcduM2uoLnXfDGCzTQRtKb3RY1W1zfjbbmt6m-b6SGTqRbryEI6pKm1rfPe0JIgG8miCCZAQjWKRsakgQjwxMju_l-wDo0T8TGm0gzZSpa_sL3M_x6rt9LfxZ4IpI0wQIlddZPOF5ztfqjBE_Iq2y3eue-1klLQhFXCViQwJgDJRKIWGua07jAtWCmLSgXCQx5a4Jsn7VaMderSJR-kpe1TfIVetsLtOJw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=oLp8eBS1c60dJMb0GDpsa-Zeiq8UImIybarP9jlLSSFET4T2Ne-ADl1M0TmuvTWw5UV_IMWVrsG7wL-r4YANyRLeFskrQ60KwQ7yfNkLhBybiHPn-Uj4KcduM2uoLnXfDGCzTQRtKb3RY1W1zfjbbmt6m-b6SGTqRbryEI6pKm1rfPe0JIgG8miCCZAQjWKRsakgQjwxMju_l-wDo0T8TGm0gzZSpa_sL3M_x6rt9LfxZ4IpI0wQIlddZPOF5ztfqjBE_Iq2y3eue-1klLQhFXCViQwJgDJRKIWGua07jAtWCmLSgXCQx5a4Jsn7VaMderSJR-kpe1TfIVetsLtOJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=IpyHkzZgKgtfAtCzCGR1zloX-jH9Kk6QNshCtsBaiy9xgVyFxaIvwJkgErJGWHidotH8W84VNMUarqoZZ2OMyV_1lY99MxvhOun8r7o2YE6npo-GIJEJTqw3JQ3yNm0L1R2AOy-D7UpOZHVSp6M845466wRGxBWY_LLQcr6C4XOl2PZ_5rhHJgbk0qTqp0sxDezD5PbwrqxYln0noQgBXZBPTGuT7Y6NQ8MIA9Hna1d_PT4XUym-5jmIhtrlYchipPrqZ99j4wTGuYw0vr-SbQKqSOvukYhKjWTQwjesN5RQ-SJT_p1U68XwniBPRKnkcXp7DPNUA1_7sgELmNq56w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=IpyHkzZgKgtfAtCzCGR1zloX-jH9Kk6QNshCtsBaiy9xgVyFxaIvwJkgErJGWHidotH8W84VNMUarqoZZ2OMyV_1lY99MxvhOun8r7o2YE6npo-GIJEJTqw3JQ3yNm0L1R2AOy-D7UpOZHVSp6M845466wRGxBWY_LLQcr6C4XOl2PZ_5rhHJgbk0qTqp0sxDezD5PbwrqxYln0noQgBXZBPTGuT7Y6NQ8MIA9Hna1d_PT4XUym-5jmIhtrlYchipPrqZ99j4wTGuYw0vr-SbQKqSOvukYhKjWTQwjesN5RQ-SJT_p1U68XwniBPRKnkcXp7DPNUA1_7sgELmNq56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=ZeYu41Wh3vgGvOnyQQyrRATWYU198mf70YJ6bdSN71NM4BTret7HYbwE5FFQBy1EbZuDmltsvckts3IHKmlIIbNo6O8K4gvZ-831TlPH1xin7rQ30v2m-JN14Th9PttnA59fuUpP4gTjMMuitUs-XZkciYk8awSzKK1ivTIBA_NbmIW9TkGSDLzgEMvQqXsZZVBD3hHi0QR0lRaGAd5IJFghKkEk5awuBPh4INmPBTKQkFzjl9JHoPFDg0ATSzXdcLw7by7xBjBiY7KZqSkOzdvJUBPpjIO3pVcALavartLnErvD2pyzyLU3OyTEtzThYZepb1YkMa8FatxhNcApVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=ZeYu41Wh3vgGvOnyQQyrRATWYU198mf70YJ6bdSN71NM4BTret7HYbwE5FFQBy1EbZuDmltsvckts3IHKmlIIbNo6O8K4gvZ-831TlPH1xin7rQ30v2m-JN14Th9PttnA59fuUpP4gTjMMuitUs-XZkciYk8awSzKK1ivTIBA_NbmIW9TkGSDLzgEMvQqXsZZVBD3hHi0QR0lRaGAd5IJFghKkEk5awuBPh4INmPBTKQkFzjl9JHoPFDg0ATSzXdcLw7by7xBjBiY7KZqSkOzdvJUBPpjIO3pVcALavartLnErvD2pyzyLU3OyTEtzThYZepb1YkMa8FatxhNcApVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=i0UL2gLnbidSb0UjWiEUKtYm052-ex3LPA6Xe5vhpSmoNJFVJLnXSnntqJ6hVDmSsvtfx6atD8rJUjmTWznzixl2XvG1POlOV_D_fMZtUNhIwwaYJoU4f4x0g4MSCIFuNd1DIn88XiUmwS0M5z0vPlspLxjJm10okBC5k-mTmRZpztUTT6wp4s9CG2gajHAOIlS-8d5Z3UiFW_DmrBNdrTWzwMdxEq9D3_y5DbppeEjr2_VmOrq7zxSEuNcbFELO5GzdxZzSvfPugN9qKDSoeKlTbU17YGX4KRxx9Uyv_qT-uMsFXL479PNL8cv-lQwkSB2dcEB_Q-60wh86yywbvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=i0UL2gLnbidSb0UjWiEUKtYm052-ex3LPA6Xe5vhpSmoNJFVJLnXSnntqJ6hVDmSsvtfx6atD8rJUjmTWznzixl2XvG1POlOV_D_fMZtUNhIwwaYJoU4f4x0g4MSCIFuNd1DIn88XiUmwS0M5z0vPlspLxjJm10okBC5k-mTmRZpztUTT6wp4s9CG2gajHAOIlS-8d5Z3UiFW_DmrBNdrTWzwMdxEq9D3_y5DbppeEjr2_VmOrq7zxSEuNcbFELO5GzdxZzSvfPugN9qKDSoeKlTbU17YGX4KRxx9Uyv_qT-uMsFXL479PNL8cv-lQwkSB2dcEB_Q-60wh86yywbvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtpQDtX5Funab08WmGAN7KYrYaS_OaeaIkPLzdNmZuS1yNtcAX0JP9UdCs9sqIxHMquD7AXL3nrBqWYXJVn-TqwyiVcFapHUnSwh4m6mwXAHk-EmnRSv4eda7-LW3Cc3_DXQRWK5LM59VrZMUxnC10Zaxmq8pyv3UbGj-a2oKOnfNKZ5bNWYHf8n7CAKcwUdjCce5pfVUixq-QDo4trpDrq-xZKgqwgmmRmlnwQ6Z3BUzkyc_8GZWzTheWtbcKAxWtgWaiCLbur7HOWgLuUKZHUbom_O5qMu7uidhrb8aOet7WUoLBewdgq6j8Y1s2H6iGRuA46pSV6N0FPu-CXJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaZJ2SKieGPLokW96LUVxhjT2LY0iO8sQHqLxF3E2uXxUDICyWZMDdFfLzXV_OCmSpdFihyL9vg7ihwfdh0tw-17M5HFQgIWPY4zKbw2AW1jZBJKvb45VbVFu13-I_r5_nP--HQGv02UqVkBjalcnCpFaXvx2eK9RKYVHahYR1Og6RghJbRBDgbPlqmjDbXYenm7oQcYX8nIK7KLbcH_P2Ljb96WfU-vEae7GShcnKOqrVPW_EHwQcOsGCaPN6exMeVWqgMUAbgZmr-XeQ9nF_EEFRRFE0eZSE3pYrEAoSYoHsX2KDZxleQci-M1kxm4VJlqdqHdFOQd4WZ-fwAi1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOU3tkXdMMyg4xRZzRi00KuFKuF8scUiVR8_qRkQUsiCV5tJblqcukOaVHckirLRFtcmX1QVsaBeRz0NDKbPgJFVjZJti0WcKImHvEjifd_m867NP27m--Ike8OErEdia_xujBkclkpGornbpXKzsAt8cMGBbthmvYEW7-5BXWpISq84cU1ODvOnTMss6si-Wxa6h75Q93nL-5pBj1zUr05X3IwXqkBu362S9xd8pnG7K-4bZD_LPzdkCxNQJK-v8uSp7ZEuQXbtZltVRmYYJvqPucMeCYwYocPQU7zI24Cxs0bAfBeBefL6FWe_YOtDpt7Fqsi2LbLdVKVQZWx_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1bpq2CGGxomjzwwYLoNY3CJo2nYSlzCeOS8LhHLNVM-0poXWl9RjTfElKPnpWVhq7gOMbIG5UxXHarpCr-p8HK9Bu5HHD1VmObAR6GmHEfrYubmBwo0xKsdMnv6Ax6_YDvSqjuNvuUBF51rxx1ex1TVm2t1AGsNb4IWpdeDVFSwg1vRyhnxGt8BtS5scLsSO6BpmtESW8BChX_ZdRJEX3lvWrXKpZtB-i3fM677pxxb-6yqM0ddrdo9NoL8IW56VePCUlOufnpCDgAYt50_rn9MTKXWzA6QDQpSYZrMY6hijSTA_w7UUS8sUaseEx2yOiudQytQ9dk7Vg2HXcbndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s0WE9dk84oQpn_dRsClF0-cjtyUmmetqkbM-8L0wfuGJSN8HMCNZZ6_5An-KPJTV9Pv5uVUxhMXmaMqehfzsz5j2wIvr1mBZ599s87PVnzv9LrXhcA2hoz-wf0MrL6a2BUAdRdBYC97U0C3rxNqtultsdv4AvQm-j57ilCvarLAmEURL4CIN7oc6qcZ6ww40CJcq4RgURbnlUhh1SdSBj87_2xNuD2vGWrRywWppjkEaQk6nQpOa5M-nPT6YzkYzu0ApK9kuudAEbCWCOwbFnnfTnA18B8xYMxqUYVHyC_wvozRykfB0UOTIruVJ1GNGvCGSp2gwhcaVR8m9XpmvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhOcITc3CzqCv2P6sCKuOrXM0SWXRXQ6ZNW0ZqHaVVlNmX5mlZZQb-rdUiL0EATIPPvlm0JrYAAke3V4P-Fd2ZHyoKqLs_uljyFqbjjDJk_XzcCXFD90ADySa2UR6Agbq6hqtYpZbqVMyRN2_x6lyW0t8Oda_4jv7LJDhS48D-SpFEum83mpxTG5Y3y6I_OWxJAdskoxUwu1Gml05vNjOaQWrC4ly8fxOZPYFbnhBdolGo0va54KQoebL195nCO1HNfNPxUa4iXG3bg2vNsBr6oIsnrgyLQ8KQ50H-lLrUg2a95-UOzKdtceauO6HBIxs1KjL9gwvxSJU9d9z90QLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQO9MB_ke37kRKpsefjOFlhtfrPuI1JQGOtSMPmHZWH09Pmrk9xQbaJ58S1IRS7BeasKOX2xQOs_5K0wM0Kic9ijoWDjt66s0RTyTX04Rpnx08H9GhZNxNnjHCJ9xcZDNUe2O3g66ZpU-XkuVNfhiiY0_Mzb-ckvn1cNlkUZfsqLQQ6mvgH7U7ugLTUTqgpxb3lbPX40UyyT76AxN_QEFOJN0JU2zogzgikna39Cad-JZmiVCN-3LDiJYeF6k9QUOb7USOrB4blQHkLnbG7JQvimmNxMWUycHrefPSr_YOkKfW3E3NRC3uXLG8liCYtZTQrwhmQx0Jp9DuyVIhH2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkuJ8DljUMOAouYJYlepYWiQmyrCPUKtfHXHi7Si7FgX_TgrZM6eTLcaBUJegtfj_o98mF3CWDV9jV1HfbmfLCm1KtTiVS07UcCGLnrxK1qkxru88Wr-8OF17MPWH5tyu8wjP_YZ4oqX3ghIVlfhdrU-xNR-lmqbKh_yAMP7u1amCIOTVL2QkySSKlOGZRzXgBKeZ9qrdzuB8TsX8rp1NoFFJFZfVDVCfLNPN3z7WQ89M8NPZkm73v9LsbjwRuEn2bwe7h_R8KaivuKsSvQtXGk32fH6CWgPKQKUleNbvbx22KzCXk8ednAvHePpsZcqHcgtsup94TAcYInNJzD8pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qz5mr2HzoapYfA1cEGLcBOgM2bIbmzXlBC3tSu_CsGmaehB-t3MQDf7PBqsiG7JyDWWerMuTh4au9w7emLA0ZtYmrJ8UfTP55gXMvEkONyo27Awfj7U3pUp5CFiPWAD5jqFNFa8_Rq-Sil08kULSkL9r8vJsC8gXNwyy07zyRzeOHyVtwJ4SOy2BPBnru2eFI3JlpgJzqi-KL3Bbu_0a74sn-7Dt-XkMWA_y00EVh6f1NOPwZyGS1G9OKanQte1WhqYNp-8wFhJbEAa5ZMXKfnHeTinDd4FYvzauUk3Ty1gkQUxG4XBMG25YLldkTR9gtnxd8OeHlvMz9WAqrpd78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2P4Tqz9rXxBmPtPz-ZJ9sWOzNbfF0iww_N95ZpPUKrPNGLRSTPl-PynppFMZL9qoQ0gEFTFB32hu39kgf6lmZE8vZWYkx35UTpwx6PHJldNv_xkheX08tYHpS-EkA1jTlrGGWebhVOfLzudV5nYGZ60tpLYLefPk402VQO6XH9L0dKKOqOn7UeLuMSKttiNrE3bAXZK1UahAvOXmmZAXOYIs6VygeUy5tp0jXV73BAnmfLKhoFPpxDYys2UmRCzJZ4gKeiQxbaLKMXLINubC1cNZGZ2HTlcWx6LuSnOqX8oNGShNO6vebMSqC1MSdo0h17YGn7oXb4OE41ZaC0C6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUb_fmqwJaQkc-wUdb6p8P3hK5ykKIWmzXJ8sPsDblejqgJ8eCmifM2QVUEYvtpwv2s42KtpviS7CBiyYz_Q1yJD4OafMC-QRpm99usMsGRnkZeXNJPqdlMMg6pemf2RzE1oHpwWjC1oq72uOwaZu4ACX55HJHJIyDFZD6RVpTMF8mfWunLg1A5X2lx2GkE2dA_bEUWpVmKVp4Wt9DU05YGUOIyqOxLjB6XP6ZNXrCL9a64_KEFl3v3LrIp7Iv-INX_ZjP46nDLiTOdw2qTXdsKFH_Tbx3VlbmN-HkTL1Fr8qq1bKaKmInxAVXUBgPNyAGB-wrcrFPRZQbarM-L_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Exi6G-vQ0WU-2WrUc1luZj235udqMMfyGpv9n2ake0tOnppqERc7bhOb_Ri40yK1WqIkmBp9Cd_BMF4nmM05TdoijZI75TfG0kXIWqMWczPoTyOuK4ZXii1Jdq7U9WYjL1Dvk1uVDLRT51yhQO2WC1e92cUYZxsYixCg_1Co3u37Uh5h-0oCl0spWJ8_-IPEiEcb1Qi534XZjV4M3CyiRoImYcuiS_vgI7b5bG-shCbikElR1TlIDY6qGRXd3BeGTDRMnSFpW14guEjYOaKZVdENT5jFT5QH_VJylj5HvpUvnOAg4wT1KAQsX8zcFALOGOJCI98t0ssdp5P-K2oItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDEbj3Cdand9a13azIm7yNro6m_5CbJ177X4GwIHcXQWbf0l9NcR2qdgoO3pwd5qwszx7l9j2Uz3Bj_yF3NIimVql6mhVoypvMWNEk22O9kwhC6yjvq024l-TcS0VstzizUxVog65E1IqWOjL6g9C0IiwMsQIePPuagXjULSWR_Df5gpiYcnbipqWCyEkucgK7_Bfe8soXsVG7jfubYRZaKnphwseJ4--Hibamz8Wu6CpqYbPMaqUJv-1AT3XjC9gus__kLJoyJR3bv_xlZ3l9Rr4LhX2IHp8QyevQ6AxD6vP6OYqAW5G0J5gsgEK2D5xXWnIyiCfcoJi-sUz1EZlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1dFcpQZAhDlEae38GNMkneBkOjlApz-kIFpzNWz20nSju6tJcNTuqxwUWlfxzIVSnnbUNpJZM2FDed2T-ztZC2y3uRYFrE2mienRgFt6WmbguBCzn-KzC9unvHZ4E3c2KpnhtPRij6HSi7RLPZqAv-sKUB6JGS7gKr8X77EjXWoQ-jbktvn_fnE51MHz8uJYrrfSU0Zyr48F0Rn_V_P8b3CmbKFaflD3jfWWXABldAICvz8wi4KM6we3CB4W9s_92j8P0Isr8CzLWyi4q4GghT8hESyiIZfy5ovC-3whi9ZD9WkcrBbgw4F23sNjnRvWY8mwI1DpiuTyyvAc4kusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uA1GPwo4E93VcFm1pjSC1NxjZR3MydITxQ1jNE_em0C3g1Rl-aUg5TcnNNxI-hTuTXQh9-fkdDvSNbGNNPKCiIAWurFalctHESvdW7FzzyWfTL90awzEA1bugl8719OqrPjsmlWWufWAFhhIoCtfXZ8-e2xpZH2BIIGetFdMzqhCR4Pf7BrNxfQ713cEWtFakmSfcah1DfG4awfzQvR7lok_RskEKRGpF6efdISO2vbzmBFy4xSbDZeZizKgJdxU4s9XsVSvTGlzs4lobgVx5rYhNoLlqg_KuZctNwomCaznfFTXwgjSDtR3rNZ59Ryz3rOov6HTV8s7CttVL9j0Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=hDksgCHs1j_IQp4u3PEXbZX7AhD0Vv2yIdwtuwjteVbWUbzRmplhDcn97q7_t6G-6dQSKiulYPqn4yTPFJKXCWSmGe-m2QVgUPiEY_Wb26wjtK3kx8HO6Cfn1YByaNehkOZHO1pHk0RLg7UBQBFeTRWv1_M4kZcJUBqICJ54bTFcIA_wFgnu1N7O7mrvCXGb2GHP04FdUDGoW0aQUHkwao4TvJ4Z-Lft4AISHf0-ato8uoPUnoYyXNG5g3nilQKMVfpS8jYeaJEjxOpjT5EObQe9MxnnBN5yKbNhbctULHGa6ZSkSu1wsMgOXjLOWUzPWEZbv0u8AMzugo33a00XAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=hDksgCHs1j_IQp4u3PEXbZX7AhD0Vv2yIdwtuwjteVbWUbzRmplhDcn97q7_t6G-6dQSKiulYPqn4yTPFJKXCWSmGe-m2QVgUPiEY_Wb26wjtK3kx8HO6Cfn1YByaNehkOZHO1pHk0RLg7UBQBFeTRWv1_M4kZcJUBqICJ54bTFcIA_wFgnu1N7O7mrvCXGb2GHP04FdUDGoW0aQUHkwao4TvJ4Z-Lft4AISHf0-ato8uoPUnoYyXNG5g3nilQKMVfpS8jYeaJEjxOpjT5EObQe9MxnnBN5yKbNhbctULHGa6ZSkSu1wsMgOXjLOWUzPWEZbv0u8AMzugo33a00XAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NSoIUN1Xf5pj1mtVFAxHAxISxW9Yb-NOqoAepYvbVpzfoHIS6kGy9Ah9CYfwe0p3KjfkLT3qVvFP9QqDAMRpkqBep-o94vmBL2mZ6N6r4aesI0GflzNJPXGyXnQSd8AYopyCaZv-TSA5r5NF6hUJ7RSLQVPrHmtaUC0UBCk3xLWiL7lF_e6ZpN2pYiTGF1IytRfrJaA8d9pNS8QW2NMfShskBvL8K2iZTjVJeg6NfDE0IgWLDRjiOBl_FfQYLArHQ_OhUZraHdj_5Jsh0f1YUGq-e-jdCLkA1qlHJ1naD_MhH4OcY6pgBVVi9DHQ3At4WusAm4fnMEOqcz79YNv9YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUw86b9p_TxsMe5eI9zoAZZqXJgKEl7KXEdNhZtF8hpj365iPkIiaIJjzhZWhdUHG6FsNwXsKuF3vAFpvjVZrkLH59DqV9dxwISGiBwswglCX5Pof4o-5-15EVowXJOi9bgKWbPGUCIB_pXM6reY2PF5d9bBq90zYrbokl00Vp1ehwGwVJSwpgKi2DcO0ja82syGwpfRmYRPVUfcpFiwnMqt6aUhLqh8I7egLsZRdwjy9e6BFTXSnseet6ncK3tOXeYuqW3cmg8YS_dxh_YBJ66HjtCm1oUCSb7SGTl-bhu_0VGVjhgMZ-XDC0ULLCc-Mogc21-_5zPKyKrOncTG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=Oeph9hKkE0EUtdXmjljECVghtbVjmy60Fi0j3wqTIwdBJfu5Z88VxM34hcG4gZtnRKCvLc_QB3xGO1ATXJpXU_E0Lll-thkBUPl2Xj9PhblRIKHhKN2XFg4PGuxROsKNK4dOAyo9-NSndSgj82-YGozQgi9PSFzMUzjhpNocOa2UNSC1RNLM69oLx_TkuHVqcCG-ltkygf-PtrvwCsInQXRcbSlahDxU7lQXzozmovaAC4HHyLCvG4ZNgc7Tukhd0opgdpZ3VFvNtemxmSVJsxJI_xgM_ATNRW7Vdz4C2O7jF-gmsyb6ukRYMACDl8DPkzVbEZnq-h0JQQVF1Pb7hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=Oeph9hKkE0EUtdXmjljECVghtbVjmy60Fi0j3wqTIwdBJfu5Z88VxM34hcG4gZtnRKCvLc_QB3xGO1ATXJpXU_E0Lll-thkBUPl2Xj9PhblRIKHhKN2XFg4PGuxROsKNK4dOAyo9-NSndSgj82-YGozQgi9PSFzMUzjhpNocOa2UNSC1RNLM69oLx_TkuHVqcCG-ltkygf-PtrvwCsInQXRcbSlahDxU7lQXzozmovaAC4HHyLCvG4ZNgc7Tukhd0opgdpZ3VFvNtemxmSVJsxJI_xgM_ATNRW7Vdz4C2O7jF-gmsyb6ukRYMACDl8DPkzVbEZnq-h0JQQVF1Pb7hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=rxxps9qsKP69bI6iuD3RaWCqUdQjP9bpbDthHRgox44f60SRoM4urIDrBPYUK3nPsfF00cJv82PFWMXIgfsznzZp20sqe0Q6GR-9zuCbXN1_Ym6zrtfzS49qQTUivyNnMNx8ozC0r-SNciWIkUl_kHgZPTM8ys_uS2pMM02Hep2od_giFmAlYKPyfc7FgCl0v_5CMZNHb04sUY7edX6OIWgLafV2XnGutHq4K4EOj2ObrWlQV3eXEF-tdIktkAh7vu4N6EsxumaoOkIcGte2dgWj0sQBSxml3pEVljvNrU6yLEWqVgKl05XUNpfEKWO6Oh972MRWTbWWuqvb5sFNTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=rxxps9qsKP69bI6iuD3RaWCqUdQjP9bpbDthHRgox44f60SRoM4urIDrBPYUK3nPsfF00cJv82PFWMXIgfsznzZp20sqe0Q6GR-9zuCbXN1_Ym6zrtfzS49qQTUivyNnMNx8ozC0r-SNciWIkUl_kHgZPTM8ys_uS2pMM02Hep2od_giFmAlYKPyfc7FgCl0v_5CMZNHb04sUY7edX6OIWgLafV2XnGutHq4K4EOj2ObrWlQV3eXEF-tdIktkAh7vu4N6EsxumaoOkIcGte2dgWj0sQBSxml3pEVljvNrU6yLEWqVgKl05XUNpfEKWO6Oh972MRWTbWWuqvb5sFNTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF7jL7ov4Te36hT1NdXRpl05WAxYq5ydJNTYQvRtRzmxRtYWgUu6jUBwd10fHzVf2CQgxRWBFSpgUJB6jJyPyvxQ2VI2LTcpPxwUkKy0Lc0CeZpXSkL2xH9f1XuqfQb68w1_CZYYHPaooFd8GRXs4d0VRzSyo9oaoSP7HlwwZKqdU76UphovVXlnl7g8HciAR0lFgXFcQar5hmUASMS4qtYqlEqMiUOGF2u495zj-3CVU3WpR6V2zrNdUnTtDRsuAitie44CidopDhVKwXP11pDVLcFnUZa5x9-4i1Yh7rlHNFv1l1UYIQNH98uZKw5QBZPItuWrJD5z5rqRjEoBFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=o0y8702M0DITw1i9Vinp7KxrCeH5-ypL4zsCh3y894GNcmCktIafR--M6RNjxP1MaQ1oayrS5ee5wWBGLeyynQHFyPVDKX9bHvdy8KEur7tM-Gx87zOlZLZR6A0ni1GvLDxX4nI7PCL5uX60ZDL1q1Q6YnYUA8hP1idp66_GKJKREcOmfXyeSGgVbgo3u3m7QI7TtvVo_bLZQlqmLv2U-eYNibRlrjxZJC5T_ArtiMBXLKs_HWKXdCOj_WBJhXnc9L5dHhoc9NPA7aFwMWne_jqFuF09Fx4_LnkWKGeNZZK-WeT8La375_1jZ5NyqAzKXgx-5eLY2eNyhWEG3dHqhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=o0y8702M0DITw1i9Vinp7KxrCeH5-ypL4zsCh3y894GNcmCktIafR--M6RNjxP1MaQ1oayrS5ee5wWBGLeyynQHFyPVDKX9bHvdy8KEur7tM-Gx87zOlZLZR6A0ni1GvLDxX4nI7PCL5uX60ZDL1q1Q6YnYUA8hP1idp66_GKJKREcOmfXyeSGgVbgo3u3m7QI7TtvVo_bLZQlqmLv2U-eYNibRlrjxZJC5T_ArtiMBXLKs_HWKXdCOj_WBJhXnc9L5dHhoc9NPA7aFwMWne_jqFuF09Fx4_LnkWKGeNZZK-WeT8La375_1jZ5NyqAzKXgx-5eLY2eNyhWEG3dHqhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVb67_mkr71d1-tKg7i3k7gY-kVqg9s2SePZWuEBFdkQAik_s87Cl60ULcQT8xdFQbngX_qDfPwWZGOlHlHwkZNKenWx2v8AWpHMQ2DFWYo4ccBfPF2ESpCJ0Fr44tLkXna3m2FMa2OueLVZFeVfFWuijtJCvOQibumPpDkdtfyuDffW8Krq62sbw0w-42Xw_9gjCjRLMEov5MwpdyTZK717bY2SMJhxogVPnUKU5O4GYOycg-JUBlUVMeWOntGBwQGuKeGMpPIPpNWvO1gC2563O8Mdm7UybrnqoMQTuX75OLt6PfXBPtn6rRns4BYV-0re8zNKblk5NtPmxIeDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، سه‌شنبه به شبکه ان‌اچ‌کی ژاپن گفت بازرسی از تاسیسات هسته‌ای ایران انجام خواهد شد و هرچه زودتر آغاز شود بهتر است.
او افزود اولویت اصلی آژانس، شناسایی و تایید محل نگهداری اورانیوم با غنای بالا است.
گروسی گفت آژانس بین‌المللی انرژی اتمی به‌زودی با مقام‌های جمهوری اسلامی درباره زمان‌بندی و جزییات بازرسی‌ها گفت‌وگو خواهد کرد.
او تاکید کرد آژانس این بازرسی‌ها را به‌طور مستقل انجام می‌دهد و نیازی به نظارت یا کمک دیگران ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76630" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CLs9LZ5B2VltBHy41CvWZIbHMBFRyqM6w3oDAweoQ8S7h64oaBu58-Il1KyanZTwkmLy92sqn9LbGfYgzj5ERPQzoWXomaTi5SQlLw-8dY5kbVOLn-EorghOmZVFToD0JjuH_-hyM_qwObquHDfbB7tC016nn4GYBCRECrxa72JrgiprSLP2QZYxW4ZJesKOrksUXwqUj6nZw6rmUIqVmXB6y3i88UqHCZl1_xoAn4eHw6LIBKkhufmAIOudJDzZnv_GDHbVwmxD-YBQ0KAcvNrXLpJoccR4bX2CSliqwCprRiAam0cwaTEA9heLZZD_g5gdTkcu2UG09hWKNBPkYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا می‌گوید تا زمانی که گروه‌های نیابتی مورد حمایت ایران به حملات موشکی ادامه دهند، دستیابی به صلح پایدار در منطقه غیرممکن است.
مارکو روبیو که به امارات متحده عربی سفر کرده است، روز سه‌شنبه دوم تیرماه افزود این موضوع «در زمان مناسب» مورد رسیدگی قرار خواهد گرفت.
او همچنین تأکید کرد هیچ کشوری حق ندارد بر تنگه هرمز عوارض یا هزینه‌ای تحمیل کند، چرا که این آبراه یک مسیر بین‌المللی است و بر اساس قوانین موجود بین‌المللی حفاظت می‌شود.
تنگهٔ هرمز از زمان آغاز حملات آمریکا و اسرائیل به ایران در ۹ اسفند پارسال، از سوی سپاه پاسداران مسدود شده بود و تنها هفته گذشته پس از توافق اولیه بین تهران و واشینگتن برای پایان دادن به جنگ تا حدودی بازگشایی شد.
وزیر خارجه آمریکا در مورد لبنان که برقراری آتش‌بس در این کشور بخشی از توافق بین تهران و واشینگتن است، گفت که ما قرار است مستقیماً با دولت لبنان به توافق برسیم.
روبیو تصریح کرد که «آینده لبنان را مردم لبنان تعیین می‌کنند و پرونده لبنان از هرگونه توافق با ایران جداست».
@
VahidHeadline
فرماندهی مرکزی ایالات متحده،
سنتکام
، با انتشار تصویری از ناو هواپیمابر «یواس‌اس جورج اچ. دبلیو. بوش»، در شبکه ایکس نوشت که این ناو در
دریای عرب
در حال فعالیت است.
سنتکام افزود دو ناو هواپیمابر آمریکا همچنان در خاورمیانه مستقر هستند و نیروهای آمریکایی حضور خود را حفظ کرده و در حالت آماده‌باش و مراقبت کامل قرار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986282857.mp4?token=rV40J3sF7AO2qNaVupHcwaCNksIRx7O2TFGRViHC14uW5RZx5kcEb6roX9gt-ctDN3uDwx2mAC2EofESSww6N_pGeRkg87J8ROL8YJDf8-zfn0DonGjO_zud9iBqgq_2iODOYmJk2mnrwMQRShwVXFuFFrtXb2ldl5lMCjBgG_cimFK0tGsNWD4qmg8i-2jtEZDzUTkEYO5vIY3Z90WdO-6DmQRtgmF0e-B1fTf7cXBiY5Dgu0L-K8RsRz2kHY-GBXi_yf4NOTsprsSHkTViLzYaeVK8D5WScdcB4QWb1VvF7_zhzJAAAwhKzQ3ZVtixoUacwtWfBlEmsL-tGVoWtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986282857.mp4?token=rV40J3sF7AO2qNaVupHcwaCNksIRx7O2TFGRViHC14uW5RZx5kcEb6roX9gt-ctDN3uDwx2mAC2EofESSww6N_pGeRkg87J8ROL8YJDf8-zfn0DonGjO_zud9iBqgq_2iODOYmJk2mnrwMQRShwVXFuFFrtXb2ldl5lMCjBgG_cimFK0tGsNWD4qmg8i-2jtEZDzUTkEYO5vIY3Z90WdO-6DmQRtgmF0e-B1fTf7cXBiY5Dgu0L-K8RsRz2kHY-GBXi_yf4NOTsprsSHkTViLzYaeVK8D5WScdcB4QWb1VvF7_zhzJAAAwhKzQ3ZVtixoUacwtWfBlEmsL-tGVoWtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ai_P6SqJ_OttwH929y13j8awGCBWyePUe3eNTaSjLkzbobofwVwMQlgfws-DWr6itm19LDG2qPNNwifKgLlgjcwA4jqrfOqdhnWTNDtfB5lccfb7B_o2XBl8FPVjYz36sD0S08DAcFX1EGHSBbHbR7rSCpg4KpGlhVo8nLEbaCLVBFX-tbp-m6sr_5fYNwrhPLtvqEUePR5Yn1XvR2BOe6NCu7cjFaGjqiMK-UUdSRIVwfp8fXWijj2p-p78VRRRpU31cdr-mJ1WDcu5ZxbXBjmZeVGnXCrpIO7PCBOy4yYrjshD360XZt-4htqmnfHIPyJRVGUJVjW5ky9dmdo47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثریا طالبی، مادر امیرحسین موسوی، فعال فضای مجازی مشهور به «جیمز بی‌دین» که از آذرماه ۱۴۰۳ در بازداشت به‌سر می‌برد، می‌گوید پس از پخش گزارش تلویزیونی از فرزندش در جریان جنگ ۱۲ روزه، اتهام «همکاری با دول متخاصم» به پرونده او افزوده شده است. مهر ۱۴۰۴ صداوسیما با پخش ویدئویی از اعترافات اجباری امیرحسین موسوی، او را به «جاسوسی و همکاری اطلاعاتی و امنیتی با اسرائیل» متهم کرد.
پس از آن امیرحسین موسوی که با نام کاربری «جیمز بی‌دین» در شبکه‌های اجتماعی فعالیت می‌کرد، با انتشار نامه‌ای سرگشاده از زندان اوین اعلام کرده که تمام اتهامات مطرح‌شده علیه او «نادرست و تحریف‌شده» است. آقای موسوی نوشته که پس از ۱۴۸ روز انفرادی، بازداشت همسرش و تهدید به تکرار شکنجه‌ها، وادار به انجام مصاحبه‌ای اجباری شده است.
ثریا طالبی، مادر امیرحسین موسوی، در گفت‌وگو با «امتداد» با اشاره به وضعیت پرونده فرزندش گفت که امیرحسین موسوی از ۲۸ آذر ۱۴۰۳ در بازداشت است و خانواده او همچنان در «بلاتکلیفی کامل» به سر می‌برند.
به گفته او، فرزندش هنگام سفر به کیش در فرودگاه مهرآباد بازداشت شد و خانواده تا مدت‌ها از محل نگهداری و نهاد بازداشت‌کننده او اطلاعی نداشتند.
مادر این فعال توییتری همچنین گفت امیرحسین موسوی حدود شش ماه در سلول انفرادی نگهداری شده و پس از انتقال به بند عمومی، از او مصاحبه تصویری گرفته شده است. او مدعی شد به فرزندش گفته بودند این ویدئو صرفاً برای آرشیو ضبط می‌شود و در صورت همکاری، طی چند روز با وثیقه آزاد خواهد شد.
به گفته طالبی، در زمان تشکیل پرونده، اتهام‌های «اجتماع و تبانی علیه امنیت کشور»، «فعالیت تبلیغی علیه نظام» و «توهین به مقدسات» علیه فرزندش مطرح شده بود.
او افزود پس از جنگ ۱۲ روزه و پخش بخشی از این مصاحبه در بخش خبری ۲۰:۳۰ صداوسیما، اتهام «همکاری با دولت متخاصم» نیز به پرونده اضافه شده است.
طالبی با انتقاد از نحوه انتشار این ویدئو گفت: «فیلم به‌صورت تقطیع‌شده پخش شد؛ به شکلی که این تصور ایجاد می‌شد که امیرحسین در زمان جنگ اطلاعاتی را در اختیار دشمن قرار داده است، در حالی که او در همان زمان در زندان بود.»
او همچنین از شکایت خانواده علیه برنامه ۲۰:۳۰ و رسانه‌هایی که این ویدئو را بازنشر کرده‌اند خبر داد و گفت این شکایت در حال رسیدگی است.
مادر امیرحسین موسوی با رد اتهام‌های مطرح‌شده علیه فرزندش تاکید کرد: «انگ وطن‌فروشی به امیرحسین نمی‌چسبد. او یک فعال توییتری بوده و اگر کسی با ادعای ارتباط با اسرائیل برایش پیام فرستاده، بلافاصله آن حساب را مسدود کرده است.»
بر اساس اعلام وکیل پرونده، جلسه رسیدگی به اتهامات امیرحسین موسوی روز ۱۳ تیرماه در شعبه ۱۵ دادگاه انقلاب به ریاست قاضی ابوالقاسم صلواتی برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLRIarr2kXyv99u8m4qMIoNOxZE9EP3KYqo059U02f7LHI8fOwqGvi2bpzU1ZTJdCnL251mQDUIStP88ANxmCxCSoQpS_qwXpPbLkrXQSiKX4eAPIN8GkGRxY-a-1C8ff4wTXynsAGnoXkyq0ZTe9IVodesMHARK4q1JTPae98CtoYlERhKPGqpAnPXsu-00SCh2P_Wqd2TscUaAbMo23BYcGOb54bA4YSh3cxfAFx9yPuBRj4QFdPZaal2EbBBcIRWDtQkbaMk8MMnGYLSsaPslIS-TO6IeTSKnr0uGp-u_9o54MjDD2oqTgzg5va3WmWNMJi7_HKAlbUDarZtgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O314dk-UMFJLn-Ru4vAcHkVHt_-e2TbE_wNJ6j4n6oZejHwzK8D7wi4curgACCwmykEoYTOyigdU4bt20Xtd8aIyLhq9YxzrlyKOMI4L1QA5aZl0XluX9mZ49aeyRVq7y1OsdqSKW-iX0O3Ksq6c1Voa6-7TSKWBFYmctH2Ahj7htq4mh1O5Q_L86Wjep5_WYaLJy-PPSxGhKKjFASDK8sz8844M0K74BuVVIdVhb0HLDIaqtmvzfl6YQyxkUrhwZsyr-9eORHJVh8Fnpcjb4noRz0ttIBqsIwzWTsrRQV-NdnTzNtTUn6kNpimCNHNIswqIYXYnehMtEquRF3Z0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EO5PLb_Bwd1MuaLmKM5yTTCce0AFx6hC_WAD_dfnjLitYiiv0bK38EN6y-_b1m1ZBxfjJ8nFGkipYQm1AB25gJqhEl32O26IMNxVU0B8u5ar_5VOF5tWWdz5lDMxInyXMQh1o0dbL-W8LQeOAsUk4ankCRORQH_luJvIIqLJIYoGVJ9sLAvoirKzLNrADre9TsjzuUpDHHsZeL6gCCANcW3nZALUxRkNs_CajiWzg6w3DnLdsGoMxyPeUGK02gioZGf9_PT-JcNE0_EY0uViZbmcf-3Lv1BvoJzM2U4Jz7gNs2w9r6J7o3PGb4yi4RaNzRBue7xnGVAwcNI7QstfpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KvkW1jvbyOj2V1Xql-QxQ5GvDd5DHX5qq12LzFJ6wy2wNIY2IFhIMOTeLeS-AxyGpUG1FrIeQ2RB8ivq0o592lds8ElZgsie5G76rjVkow5Q0Q-_TwNwQ04MyszD0vLyFjgSHVLVRrk8rx3_0q-Qr8jRLB5BNXDWhRDW5sZQ_-s-WxNdG2l0dgG7o_pjChYV8T17w-Ah3Oba-fLWCiGGA-sy-VR30Gl3kTKiYfPNujAkGHt8M3y9vVTmg12YLe6gw4GvRZ-NjXzWtKYCtshLR5iJwqtnJy_wpTxkvPAbB2kku4555glN-CEA6_OqkLRAj_Ns0lG3eo3ZOmLBI0AFtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M36jKEW5kW4sA-hvdecs7KxHlS5QGQd4hpQCl2rTa1Wjwby8nmY3IulHN1r90DncmWM-SEnyzrl-N1X1icR8mHXF08AbfmTgk0IR5y4KsPkfamaK1tYDSZUzsC_57UnECsvyHVDiqeMODei6qOya8ov5hDWiQAm91avatgI_sDqIp_XOKD5zS7d3Mv0b4HU5NCGVfN55CIRKEyGyJH5C_wZQoRF0VIo9_LA7Fr9CK9yuZtZ45V2ZaOgyXRAZrG6mcfCdcyvDaNCtQm9UbBXTY5v3bfXotFdeIAGhwGlT5ogwB14Mf8ASOB4AsZnIOZEsF2Yt9wOYxK5bqJ47h1tOVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌های کاربران از بروز اختلال شدید و قطعی در سامانه‌های آنلاین و پایانه‌های فروشگاهی (POS) برخی بانک‌های کشور از جمله بلوبانک، بانک کشاورزی، بانک ملت و بانک رفاه حکایت دارد. این اختلال‌ها موجب شده مشتریان در انجام تراکنش‌های مالی، خریدهای روزمره و استفاده از خدمات غیرحضوری با مشکل جدی مواجه شوند.
@
VahidHeadline
گزارش‌های مختلف کاربران در شبکه‌های اجتماعی حاکی از اختلال گسترده در خدمات بانکی چند بانک بزرگ ایران در روز سه‌شنبه، دوم تیر است.
بر اساس این گزارش‌ها، پرداخت الکترونیک و انتقال وجوه در چند بانک بزرگ مانند ملی، تجارت، صادرات و ملت با اختلال همراه است.
خبرگزاری‌های فارس و تسنیم، نزدیک به سپاه پاسداران با تأیید این اختلال‌ها از احتمال حمله سایبری به مرکز خدمات پشتیبان خبر داده‌اند.
در همین رابطه شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، با تأیید انجام حملات سایبری، گفته است که «شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است.»
این برای دومین بار طی دو هفته گذشته است که خدمات بانکی در ایران دچار احتلال می‌شود.
چندین بانک ایران اواسط خردادماه هم با قطع ارتباط و خدمات روبرو شدند که به گفته مسئولان دولتی به دلیل حملات سایبری به زیر ساخت‌های خدماتی بانک‌ها بود.
تاکنون گزارشی از عامل این حملات سایبری منتشر نشده است.
@
VahidHeadline
آپدیت:
پیام‌های مختلفی دریافت می‌کنم با نظریه‌های توطئه که فکر می‌کنند بازار ارز و طلا و...  قراره نوسان داشته باشند و نمی‌خوان کسی بتونه خرید و فروش کنه و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG2beWskw0P1v_urs3PGmuYik_4L7HwCQ-sNbTjMyeKhq2DcLH4WORM74cn88spV_23bExoawRqOW2cZjlap1egs8RJlZGCHhw2mY090vmikmjGd8usDBqci-_3ByeYFkkJFHTWvC01Ox7_TvEIMh7gx5nF-46exNlolq-nYaKp0Ipk3pg2yQ5DZKD8HZdYdho2i2KirJdnRVWYAMsBUlXOFWQkon-wTkso31RrutyapSa6iHSvC3lHvkZJotNHmXuspr1Mr9O-87MRpDYzyrOQw8rCD9KGu5YvF1znQGjGrUHQZp2hXcAHffRN1F_AisbTHjg3YwqwhSnGsQOwJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان و ایران روز سه‌شنبه دوم تیرماه توافق کردند گفت‌وگوها درباره نحوه اداره آینده کشتیرانی در تنگهٔ هرمز، از جمله خدمات دریایی در این آبراه راهبردی و هزینه‌های مرتبط با آن، را ادامه دهند.
به گزارش خبرگزاری رویترز، در بیانیه‌ مشترکی که پس از مذاکرات مسقط منتشر شد، دو کشور اعلام کردند یک کارگروه مشترک با مشارکت وزارتخانه‌های خارجه تشکیل خواهد شد تا این گفت‌وگوها را پیگیری کند و همچنین با دیگر کشورهای ساحلی و طرف‌های مرتبط رایزنی خواهند کرد.
این اقدام به نظر می‌رسد اجرای بندی از تفاهم‌نامه‌ای باشد که هفته گذشته بین ایران و آمریکا امضا شد و بر اساس آن، ایران موظف است با عمان و دیگر کشورهای ساحلی خلیج فارس درباره مدیریت آینده کشتیرانی و خدمات دریایی در این تنگه، که مسیر حیاتی برای انتقال نفت جهان است، گفت‌وگو کند.
این توافق پس از سفر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، و عباس عراقچی، وزیر خارجه ایران، به عمان اعلام شد. این دو مقام ایرانی با سلطان هیثم بن طارق، پادشاه عمان، دیدار کردند و با وزیر خارجه این کشور، سید بدر البوسعیدی، نیز گفت‌وگو داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/76621" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GdIhd-HsgOwgAmc45_qYDS-adGeWvnPHdWGsB_DfXnJK14PtdSebWdMtTrQV_vqS00N0msEB5JWAGbkc4NZe09_6haeZyqTNSJ7XOyIX7XUFu8UdHCq8DIEZzAvi2VCBbX8QngyIpDvMn2k9-8em4wVrv7Fr5M-Fta7VIGBcesCxa-3QLxSIL0cmIeXfcqezjyPvLWRbio6QR5tnMsDtwnNgXg7w1Y5wmJ4RmDvkrn40RDYEWkwQL9RTHmv1RBCyMCiU0p6P7TNyWRsh24pW3kSiqJGtDKQ3pMBcASxcs5DbcxbhzelMWgUY-HJweUjsIi1BAiHHRZ0jZtjAVH_0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=DhXz9ZcXYmaQlmPeQzFYB4kAH1F0AiS-bxlboF1lRmy6X1Mn4WpcB6ElqnsXSLhB_72nr52SHwhpfd3ERSt7d1sAqDmeqK6IWSuoLwgPFnBpAxEry1Qwc1lFlSeREbQJ_D7wUNvOB7ujFDiNg8bQLJ8dvJn3X4WJqj_9KWWdmY9euc1iK4ULr4i8XLOnu0O6LUNN5VzyZJlMwb__Ge8sxBZX9Dj_dsKxXOKoP7aBHPVoL1F0OSlmcSDgT3HDMIlX9Ldr8XSQa9uzdsbVhue6RcBkvtT8XFl_4nJSE3Q2cym5q-CTdXNonroN7vvHv9zROONssCcZrmpwS0kxAxnwcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=DhXz9ZcXYmaQlmPeQzFYB4kAH1F0AiS-bxlboF1lRmy6X1Mn4WpcB6ElqnsXSLhB_72nr52SHwhpfd3ERSt7d1sAqDmeqK6IWSuoLwgPFnBpAxEry1Qwc1lFlSeREbQJ_D7wUNvOB7ujFDiNg8bQLJ8dvJn3X4WJqj_9KWWdmY9euc1iK4ULr4i8XLOnu0O6LUNN5VzyZJlMwb__Ge8sxBZX9Dj_dsKxXOKoP7aBHPVoL1F0OSlmcSDgT3HDMIlX9Ldr8XSQa9uzdsbVhue6RcBkvtT8XFl_4nJSE3Q2cym5q-CTdXNonroN7vvHv9zROONssCcZrmpwS0kxAxnwcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامران غضنفری، نماینده مجلس شورای اسلامی، در شبکه اجتماعی ایکس از برنامه شماری از نمایندگان برای «تحصن» مقابل ساختمان این نهاد در اعتراض به ادامه تعطیلی آن خبر داد.
او نوشت که «چنان‌چه مجلس بسته باشد، تا باز شدن مجلس، در همان‌جا تحصن خواهیم کرد.»
شماری از نمایندگان مجلس به تعطیلی این نهاد طی ماه‌های بعد از حملات اسرائیل و آمریکا به ایران در نهم اسفند ۱۴۰۴، اعتراض دارند.
حمید رسایی، یکی دیگر از نمایندگان مجلس شورای اسلامی، یکشنبه ۳۱ خرداد با انتقاد از ادامه تعطیلی مجلس گفته بود در صورت ادامه تعطیلی، همراه برخی نمایندگان مقابل ساختمان مجلس جلسه برگزار خواهد کرد.
حسین صمصامی، دیگر نماینده مجلس شورای اسلامی، نیز در پیامی جداگانه در شبکه ایکس، نسبت به ادامه تعطیلی صحن علنی اعتراض کرده و نوشته است: «بیش از ۱۰۰ روز از تعطیلی صحن مجلس می‌گذرد و نکتۀ تاسف‌بار آن است که در سامانه قانونگذاری، امکان ثبت استیضاح وزیر و صدور بیانیه مسدود شده است.»
انتقادها در این زمینه به خصوص از سوی نمایندگان نزدیک به جبهه پایداری با پررنگ‌شدن نقش محمدباقر قالیباف در مذاکرات با آمریکا، افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/76619" target="_blank">📅 17:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0ZrJLRSrN9HdmNavPVUPqcLXhDC1NmbJ9BuP35kHev4xemKvxL9pdCk_kRobYjA9ovSpeR0Ot3ucqzMV2kJhk5vl93K7sbPNgMuMfs4rPxpvKETZb6nxbjDGRj-h2MN3wa743XUU8sadLKjBka33zJj67sMWIfqww55AcQKQ49jj3UH7S45MPSnS_A64L9B-RaoF32o10bLb2J0rbFdK_e2_nZ-qUxB4X8pqEI0Ir_1dw7Hyv2JGCHr3wIvIwrctJyWYKqBtLVmTGhPtoemHe6n1O4jVs0l8qi3hVqo9H2oKpX041d2Mb76CdGdPEEZFm3W5E8uu7ixf8M9NvS4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون فیلمسازان مستقل ایران، ایفما، در بیانیه‌ای نسبت به احتمال اعدام علی صفری، بازیگر تئاتر و دانشجوی دانشگاه فرهنگ و هنر هشدار داد.
این کانون با ابراز نگرانی از طرح اتهام «محاربه» علیه او، از مراکز سینمایی و نهادهای بین‌المللی خواست تا برای نجات این هنرمند و سایر هنرمندان در بند، «فشارها بر رژیم ایران و قوه قضائیه آن را بیشتر کنند».
به نوشته این نهاد، علی صفری، بازیگر جوان و ۲۳ ساله تئاتر و دانشجوی دانشگاه فرهنگ و هنر در جریان اعتراضات سراسری ایران در تاریخ ۱۸ دی ماه ۱۴۰۴در شهر کرج بازداشت شد و «تاکنون اطلاعات روشنی درباره‌ی روند پرونده‌ و وضعیت این بازیگر منتشر نشده است، اما اتهام «محاربه» در تاریخ ۹ بهمن ۱۴۰۴ به طور رسمی به او تفهیم شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/76618" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d9TIuxevs1MkE9SUNMRC9k2KSrIUr5UvDzzJEoY9TZ80Nr4DnX_w93IfID2QNN9jWKc-S3vGSivaDxDkXNQYPeI_HqeiVNjuQZLrjgiA5MO9RGv4v9yG5uUuMnsjq3Jlw2-c6utDscfyUw8kprpm6gMsSBheNhHbJ73cyz7wEbriiqLx_dauDIP6zS8JtsV0WmLSdGP57F6C6l9QF8WIrg7BkEXNgUZksOodHRqBABPEs6YMnryRCLip-IozZiLqgHnWEKida_58UVxYvSilIC51g8G7OasLs7L8h8VsSwFAhWQMNkYQ_NTHFhPJ-zOKoovdAIZsxMRvDO2CUETSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11113460cd.mp4?token=Uh58SEvlX--IVTZ95_v81zUEmJSOIfkluP3hOrE1aO9Odug7MDuy-G_ys5Yywk9THP-EOVr6gpXc8CBTqlEWCb2HkfW2LYukDA1d0MGOB38Y3LurcqX8nHDNUGvKVAZer9MvAzhGsrVJ3JUY4apwlLmUl_GVgk6fA2tqPx712R59EB34VQTSjaWA7KLqOeWNIqsOt03yNLvbxqdu49sU3RoN5AeoYDI8Du17qmNuGfR6dc0yPZ0fV594PxQYHfg0hi5tO5y90De-0_50axExP5U-So9pdSubLVqiGNjOgQETIE0M-p85tazBVThpRKVWZZiz-y-3iKLV1zo8ebTqDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11113460cd.mp4?token=Uh58SEvlX--IVTZ95_v81zUEmJSOIfkluP3hOrE1aO9Odug7MDuy-G_ys5Yywk9THP-EOVr6gpXc8CBTqlEWCb2HkfW2LYukDA1d0MGOB38Y3LurcqX8nHDNUGvKVAZer9MvAzhGsrVJ3JUY4apwlLmUl_GVgk6fA2tqPx712R59EB34VQTSjaWA7KLqOeWNIqsOt03yNLvbxqdu49sU3RoN5AeoYDI8Du17qmNuGfR6dc0yPZ0fV594PxQYHfg0hi5tO5y90De-0_50axExP5U-So9pdSubLVqiGNjOgQETIE0M-p85tazBVThpRKVWZZiz-y-3iKLV1zo8ebTqDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه دوم تیرماه بار دیگر تکرار کرد که ایران با بالاترین سطح بازرسی‌های هسته‌ای از تأسیسات خود موافقت کرده و این بازرسی‌ها «تا ابد» است.
دونالد ترامپ در پستی در شبکهٔ اجتماعی خود، تروث سوشال، نوشت که با وجود اعتراض‌ها و «ادعاهای نادرست» ایران، و «هم‌زمان با جار و جنجال رسانه‌های جعلی که هر کاری می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند»، ایران «به‌طور کامل و تمام‌عیار با بالاترین سطح بازرسی‌های هسته‌ای برای مدت طولانی در آینده (تا ابد!!!) موافقت کرده است».
به گفتهٔ او، این امر «صداقت هسته‌ای» را تضمین خواهد کرد. «اگر با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد!»
نخستین بار، جی‌دی ونس معاون رئیس‌جمهور آمریکا بود که روز اول تیرماه خبر داد ایران با بازرسی از تأسیسات هسته‌ایش موافقت کرده و این امر ممکن است در هفته جاری رخ دهد.
با این حال، مقام‌های جمهوری اسلامی بویژه سخنگوی وزارت خارجه ایران هرگونه بازرسی آژانس از تأسیسات هسته‌ای را رد کرده‌اند.
@
VahidHeadline
پست‌های ترامپ، ترجمه ماشین:
با وجود اعتراض‌ها و اظهارات دروغین آن‌ها در خلاف این موضوع، همراه با هیاهوی مداوم اخبار جعلی، که هر کاری می‌کند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهد، ایران به‌طور کامل و تمام‌وکمال با بالاترین سطح بازرسی‌های هسته‌ای برای مدت بسیار طولانی در آینده، یعنی تا ابد، موافقت کرده است!!!
این کار «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این موضوع موافقت نکرده بودند، هیچ مذاکره بیشتری در کار نبود!
بر اساس این موضوع و سایر امتیازهای بزرگی که ایران در حال دادن آن‌هاست، من موافقت کرده‌ام اجازه بدهم تنگه هرمز باز بماند، بدون هیچ محاصره دریاییِ دیگری. با این حال، همه کشتی‌ها در جای خود باقی می‌مانند تا اگر لازم شد، محاصره دوباره برقرار شود؛ چیزی که در حال حاضر بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که وزارت خزانه‌داری آمریکا آزاد می‌کند، به حساب امانی منتقل می‌شود که تحت کنترل ایالات متحده آمریکاست و صرفاً برای خرید غذا و تجهیزات پزشکی از ایالات متحده استفاده خواهد شد، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما.
این‌ها چیزهایی هستند که ایران به‌شدت به آن‌ها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است همین حالا، پیش از آنکه خیلی دیر شود، کمک کنیم.
گفت‌وگوها به‌خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد؛ رکوردی بی‌سابقه در تمام دوران. قیمت نفت به‌شدت در حال سقوط است و جهان جای بسیار امن‌تری شده است!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76616" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HM1k0Yl_oluIG55aMY-0BCcdlBGszb0SqprjdRmj9V09vk_WJ7C8Yu893fAj42qHv6nw5FWOEHJ4Nq1wNN6D5vf28GfQHxZOrLweAjcG6nioF6ZqXXeiQoNFl43BWnY029wInqHUYfka-x3NnAV43djIxfHxgvDcxK4EZLctw8tEcizUeiG40cMNFXA-c6GLRfezV7eUpZS02bHQ7gPlw5_hMrpQTnQZ3frw_grjHw4gLbpU9GG-YnknsWs2Rxx_WHne5UTmb0qsoxFhCejoN5fTrM-UKq6paH3oylJFqBCky-UFW2U4w2hZ6WwvNdiVhcPh6TV2QIzc_NyYqK81fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر سه‌شنبه دوم تیرماه گزارش داد قیمت  [نان یارانه‌ای، نان یارانه‌دار] در تهران و ورامین افزایش یافته و در برخی موارد به حدود دو برابر نرخ‌های پیشین رسیده است.
بر اساس این گزارش، قیمت‌های جدید از سوی استانداری ابلاغ شده و از امروز روی دستگاه‌های نانینو در نانوایی‌ها اعمال شده است.
بر اساس نرخ‌های تازه، قیمت نان لواش به دو هزار و ۷۰۰ تومان، بربری به ۱۰ هزار تومان و سنگک به ۱۵ هزار و ۵۰۰ تومان رسیده است.
محمدجواد کرمی، رئیس کارگروه آرد و نان اتاق اصناف ایران، نیز افزایش قیمت نان را تایید کرده است.
در ورامین نیز رئیس اتحادیه نانوایان از افزایش ۹۰ تا ۱۰۰ درصدی قیمت نان خبر داد.
بر این اساس، قیمت نان لواش از هزار و ۴۰۰ تومان به دو هزار و ۷۰۰ تومان، تافتون از دو هزار و ۳۰۰ تومان به چهار هزار و ۵۰۰ تومان، بربری از پنج هزار و ۳۰۰ تومان به ۱۰ هزار تومان و سنگک از هفت هزار و ۴۰۰ تومان به ۱۵ هزار و ۵۰۰ تومان افزایش یافته است.
مسئولان صنفی افزایش هزینه‌های تولید، از جمله دستمزد کارگران، خمیرمایه، حمل‌ونقل و اجاره‌بها را دلیل این افزایش قیمت عنوان کرده‌اند.
رئیس اتحادیه نانوایان ورامین نیز گفته است اصلاح قیمت‌ها با هدف ادامه فعالیت نانوایی‌ها و حفظ روند تولید و عرضه نان انجام شده است.
این افزایش قیمت در حالی اعمال شده است که نان از مهم‌ترین کالاهای مصرفی خانوارهای ایرانی محسوب می‌شود و در برخی اقلام، نرخ‌های جدید نسبت به قیمت‌های قبلی نزدیک به دو برابر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76615" target="_blank">📅 17:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vIk2dBe85WxaqYS63gAagNX1G_ikyT2y-sHXEOUNsDWeGZcDsTYSNPm2s5hf_72lPW63MLdfy84pRw195YHu-yQ5UZ-V3y8DCH53Qlaud2dz_1eU75v6YzaKAjrEzEnxHV8KSes3pDZjwrrU76EPY56xaiSx-hEHSbymeVpC__wqzmjjm2UJx7BMlPo9lrsJKEUoIgeQkpysn9GCW_C27UCSxPSOF-Rg62E3PPzct97qrxgdVyvW5FjueY8YsOLF0fVgsGXccK4Wbs83HRWe2HiscnQPLnnaVESG8mlBTSN9jfh6rYMrwZevjutOK6XVxvj4vo5Bg-grywwGNA-ZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nXlZ3MNQSv0CwrmuMS241ZmWTG2hb-M77dxQQHpcllbsxCjVPpbZi8toqQZ5ehgYRKjT5RLcsuNoLSfdRrc8ZP5oRuFqntKvOHje6akA5_ZXgna9SIrs1o8AqQIWW1DZk2Em4nxiw4M0v5h3KpKVVb3bI_osBhJe4S2Z70KfMYXely8kxVOiwsUMsjasJTQwmAd0J5MLimDjYGMxity4qO4Pm8ZjX_jUn_RQ8Zw3etT6EmxzjPi4syghCsucxQuZy1kxL81wQMBXssVKTZ4U0FUTaDTjpWfD19FRnEidImwggQiKaTkQDFtcvssehzKdrNSuPLS2JIKMkoE7QaNevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rn-YeQPbN-Z0EqtK5C1z5LSfDs83_WOoUGD5OMY-78c8JVpGTXJ15mJgnAjlXejQp3t3WM7DEv9XzO3MDIvz0NCcwPDkZoxccFvUPeKBNZBHsqq0R6s5KDNNMEHILcDpkKutaZmE9XAGg0VSiRm_VP29e35TIrICPJ_QfgxaKOYS9l7h5P18hpVRn8RPh6RXVoWWFsVJfdT-mKSzoeZ89pMyBS5eQAST1O4WNrfZGBDTWtCuhK6YKxSsQDUrvQvBNzH-lVQW5pTaHBg9NxxjB2dmq3K6m13KLJKZRe2uNGcnPd360kYupfw2qsqljwRYTXSpRP3Nr7c55QGNV0bvVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=EE8VrsNxIRm0R5Uf9sxHOjECSdeWmOB0cBO5mLzBlm-VfAeMmXSsYPPWO8-WfqsGiUCN6qZimDshb_QsyVVHfj6kQPUZy8YNHctPBLEfrujbC-yC5ZowVkL9jpPv9yneHxyA9SKF3Auyl3cb49ome5wgPb5qv5fm2md-pPzDXU2ty2QAlhk3_prML4fCbgxAqrVzDyGXFjiYYcNCMdc6jidoVyvlUDbvdw6KFzcAa1fkKKCSkbJM_STd2mlv22qhRjyuolS0g6OGqaYRuHghT_jtKaDtDHWUrOilq84le-40qhyozbuYlgrkC_vxjI9vnw9RO9pZAacKA8D9YSS54w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=EE8VrsNxIRm0R5Uf9sxHOjECSdeWmOB0cBO5mLzBlm-VfAeMmXSsYPPWO8-WfqsGiUCN6qZimDshb_QsyVVHfj6kQPUZy8YNHctPBLEfrujbC-yC5ZowVkL9jpPv9yneHxyA9SKF3Auyl3cb49ome5wgPb5qv5fm2md-pPzDXU2ty2QAlhk3_prML4fCbgxAqrVzDyGXFjiYYcNCMdc6jidoVyvlUDbvdw6KFzcAa1fkKKCSkbJM_STd2mlv22qhRjyuolS0g6OGqaYRuHghT_jtKaDtDHWUrOilq84le-40qhyozbuYlgrkC_vxjI9vnw9RO9pZAacKA8D9YSS54w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«امیرمحمد هموله» ۲۴ ساله، ساکن شهرک صدف شهریار، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ بر اثر اصابت گلوله به ناحیه سر به شدت مجروح شد.
او پس از تیراندازی به بیمارستان نور شهریار منتقل شد و حدود ۵۰ روز در کما تحت درمان بود، اما سرانجام در روز هشتم اسفندماه ۱۴۰۴ بر اثر شدت جراحات جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76611" target="_blank">📅 17:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OzwKS4_adgJ_t6hP55gY9At7Q-9vt_82KAiQmlFfY0BxNpdyBn3PDBPgLxMqJie-KZntPpvidLZogA2fLlLtFwvyzexbwAvo5Ae0OiY6rMqHrxwbED3zQKYWjW36c7eOzlDqZEI8Zkf4nQM2YmXWIrwYrG4mYXGluzeRbeuUOLwD8qe3crxLveN1_i62vSxdSRKrTsXI_xZ5ilWZ7VXbm1rNpDI_l-icWqxZ8iszcZFmAPqMILr1U2sOlui0zk_ktnhH51tdFNWPZv5LsP8OI-Rs9RtfvA0K1jfgd0eM4l_Yyeu7eqLrVN01kg4sDO3dCBpBmE7KLBd4rusfSEFV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JmyEtCGaWm3yF4kclAjAQG6TznFMdGnNFrYNncrf2AWEisiXbRJXJYtnOpp5aKrOhQzayVF6DzTK__1vzX8mPyyvY7fNllQ4Gn37PvH6cXtz2NvUJd7-HwYr7KOMK1LnhAC6jRYoomOymL6mzh3eHgQphPNOL5wMWEOVtL7xwxQwErzr-BAQ9NQd8xW1HiNaGU1sbqhAh8Xxh_cTQlXbSOQR8rPFEfoq6Ixfg4QVTNNh8qrRA5gT2NP1JsRTy_mRhPvcPybE8PmCMlWe2EL6lqI7TriFLIWL_OYSH33qVv44u9zLTxrenSE7qtY4V0wh5dv_pp6FOrjLY6Y6bju6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WL6LM3kAKbh7TGbVs4aT3M2QjArDnoxz_0gXp6pKSOWznOkTk9e30rh-z9-kIrMOz3ldxjOYy6rpjIBRUGytKJaVdgPtfwPH7esAq_Hz-GxxpZuuC_6PJ4leATsMgdjQI819Hx7Wxa2LTmYzxKwXsUXvzgHoxjUFCAiAgOqtbCnoV4Rip6tRGSOMOmitCEqtNCnhpdAduzufIbkBumqh_T3JuCGvLb9Busrrs-VNTsHF3KSe3dJjHtPnA_xxTkR00EuOzcD8D6iuoMxBXy30BSaLw5jU9d72qoi_dgNXZanFyWWJsva_HiAsO_eemXb47PQnjpuJo-l0LOU8mRllyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pqTz6DderZCXyoevFBtxISly0l-2DPwqSiC0oLbJOJCz7QIYNzcsoSFCt2UG8oPEkXg8dX3HEq7kva12rMv6u3aTVbE7VU3m5ar39cEpiSmFYqKaUW_0NNz9D00w7Hx_LP-jzHDTQ9rB56SztNtO1TItzmWrd3kY4g6GoILgaGqdYa6jT6zTwPFdmGt2l9rmrfbzUSIYB2bS8WpCVdFPvQNfsn_grU3ThWZIWYkTUV4bPLC5Q0o9ddBSXqIUwh3ADhgUk78t3ld_c5ZlZuYlPn1U49-FFdgCM7-6pT2eIKxvoe4anEoxEah7zlaamOALZGFOIZYFdvNajmVDmNy7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gTFOewlofTi9OZ6_3hwIj9LZqk2EeHNEIfkOQ8ytCVEbhKX7M_gmDYbMoyqWwv3tDvROQwoh_voROdgoMYOC5qP5Fu3m_ixJdoWiadX8-8ui9iT2Ny2R5yRqw3qblBE747qVjSoU4xqPcXh7hMXf4EsjkpDUwdq439rMg-LUCHnnYUHEJQ1pKSwdGG2j_iPKujMiLghhU2prIhdXd0elHxwZnq7UEl7dDJ-e6uR3_y1xJp41wkTzuMDFjtVIjt4t9DsjmBMmpez3iWbRIcXInfZF3tCoUvoW2so5XzrOmnEnq7_3KN9ORytr6TQdaBWKIkcYepbksBol98w6tX0Apw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XbwAPRIJ-8yWsYKrYuOIjKFus2GuMDEfC-XDACD4Lz_hJmWx5YFD9-C9Xq2ZwArG5luGY9SmN3s0xf_9uDFBzyCxsKteg9oh2ZONlz1_CKJmEQCfp5h0DjY0vNNL1CDsrVs1t_kpvIabbES77tMtP3RE1YSjemOXHMVCtJXe6hJkSaYhcC0MCiKO0kebhQvTsPIGnl47jBOH6dzPZODpfni0Q7H6Gqb8rRq4oAIUJZ_P7NJo-j6vbvQCT8_n98csgVJtlY4HJ1L_I2cznTKMtwhgWTd5HrBgkBLqA9g2MaxcxHpxibLoFZtb1XTtJvd3X3hO6B5PGOt05t920M-hrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DlkdDjBbsewtDQmOAn0y5C2_aMIA_9P0SW7Zp3Wn7RD7i19KLkFS_4UH5fqrmyH3zfPL5VLCeYo4JNX2InF5xEXPn7NRXHfXf4mOSFE-QkbLr-JPh7IehmyapuBd_vUe1jjDgbmCO1U5RSwGQTa5JHSDT-2oE_qraK2ZagbVyxlQ_VxH8ayjIX8Kg3Fxfxs5zwRfc5vd3rCe_fTn_lIsGHBY0aA410tVDknYVluiHgy9nIgoXALWfRzGWWpldZLGOgr6-ExHN2LUsdyvr3l0HImOMZgPJei93QewldQdmvU7k_YWA7RKH18pD676LZ4YzaDcao38XAnnMSeugBTcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kf2GGPiraaKPK2WhUn-t9hLZSDvVmlSXSdiFQISwWJ8Nk2O4dL0Kt8GcthSB0XlQqexQeZA4vMTiHKyx9QyRL-7Q-4u8kCDt5LR3RnX1qICfteAwIePhZNm5RG-3_QmrrMmehpmcNHnIUQkxfyKIbdc9cBxl3iaJ-ZnFhZUw934G6nJTdZEzaICXZNZtGU0VGwl7LSBa5V0vMnMy_wNHfBy4nSkzp6UgF-RoGbpx3lsCKI-EknNnyci12G0ozw4yV8JSOvFO5jgUTmdf05x1sZKXqDLDOUetQ0OOnjCTsD3-tBFX8Z285I_GeZ7gGROKaPsxSXqMTS7romP3CiyEng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ پشت سر هم پست کرد + ترجمه ماشینی
دونالد ترامپ، رئیس جمهوری آمریکا، دوشنبه عصر نتایج چندین نظرسنجی مختلف درباره توافق با جمهوری اسلامی را منتشر کرد.
از جمله یک نظرسنجی مشترک «سی‌بی‌اس نیوز» و «شرکت یوگاو» می‌گوید که به عقیده ۸۰درصد جمهوری‌خواهان، این تفاهم‌نامه «بهتر» برای آمریکا، و یا «خوب» برای هر دو کشور، است.
در یک نظرسنجی دیگر، ۶۷ درصد می‌گویند از تفاهم‌نامه اخیر صلح میان دو دولت حمایت می‌کنند.
در نظرسنجی دیگری نیز ۴۷درصد گفته‌اند که این تفاهم‌نامه اثر مثبتی روی نرخ تورم و توانایی مالی خرید مردم آمریکا خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeMNZ7YdGkY_VZQLfu03PeGpkB1OPTCy5qsJIa-3gYCP44dH--vqU4OIitDekD59CjG-QEnDLmqZ654Eb8lhinqvr2Gnxma5gb7F2MLriVeMUJTFYrJJiauKVtBL7_6GIUl1GSR69Zm6eZLEwWpg9w0_cRCtrMl3Gd3yePsReat_b38nz6XpluZQio9AOZ2z6PGaMCFUPCRXdPUkSir4E3GoopIy8UhiF8o-jwO7jA3nGqR9_TCMwN4OBhtkFf2sKMhFr3-H0qZrTdZ9Bx7m0lJ3V6SMSxazGYM5yFh1VESzlPXVnk1UxwtTlrfkbglBXhmR3PIoZ18xi8WCuQKdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ: اوضاع ما  ‏در مورد تنگه هرمز خیلی خوب است.
‏دیروز نفت بیشتری از هر زمان دیگری از تنگه عبور کرد؛ بیش از   ‏هر مقداری که تاکنون از تنگه عبور کرده است.
‏احتمالاً این را می‌بینید.  ‏ما با یک فوران نفت روبه‌رو هستیم.
‏تنگه کاملاً باز است.   ‏این را می‌دانید.
‏خواهیم دید همه این‌ها چطور پیش می‌رود.
‏اما ما دو چیز داریم.
‏ما یک تنگه باز داریم و کشوری داریم که   ‏هرگز سلاح هسته‌ای نخواهد داشت.
‏هیچ‌وقت، هرگز، سلاح هسته‌ای نخواهد داشت.
ویدیوی بالا:
به تشخیص ماشین، حدود ۱۱ دقیقه از نشست خبری ارتباط مستقیم با ایران داشت.
متن فارسی اون دقایق
ترامپ در پاسخ به سوالی در مورد تنش‌های احتمالی در تنگه هرمز گفت
تا زمانی که ایران به ما احترام بگذارد، نمی‌خواهم بگویم از ما بترسند، تا زمانی که احترام بگذارند اوضاع خوب خواهد بود. 8:15
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه عصر گفت اگر جمهوری اسلامی «به توافق خود عمل نکند یا اگر رفتار مناسبی نداشته باشد، من کاری را که باید انجام دهم انجام خواهم داد.»
5:00
ترامپ: نیویورک تایمز جعلی گفت، اوه، وضعیت تقریباً همان چیزی است که چهار ماه پیش بود. نه، چهار ماه پیش، آنها یک نیروی دریایی داشتند، دقیقاً ۱۵۹ کشتی. آن از بین رفته است. کل نیروی دریایی از بین رفته است. آنها ۲۵۰ هواپیما داشتند، همه از بین رفته‌اند. ضدهوایی آن‌ها از بین رفته است. رادار آنها از بین رفته است... همه چیز از بین رفته است. رهبران آنها از بین رفته‌اند. کل کشورشان از بین رفته است...»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=JqkIRDWobZaBo3ZO1c00SZ4OPRl4a463uQVA80WTxDhFv7vSOuAylZjkkbPa4VMl4oy-6AWTIbNYL9SU6jwXnzLU9VlH0J4xqYrw-IVWlFVWb9vijEBKiTJDk2kuAWcxCW8pZYjl5XtsrPtuQiXSWopqu6SxmtSyfOZSbY2wOqZFW32h1zJzhpueGSBbdWfWL7lfylCYj-AqHyay4Zu2uidx1prN7fSP24i0Vx-XczmG6xpHU2hdCLU8u5yIPfO2zwNwrhAhsxGCLR9eMNd3GTx77ZV3TJBT9PAj0pdTBM7CiNi_PaYTNK8YBIooDArOzr4IrK6hG7vR1vzE3C8LaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=JqkIRDWobZaBo3ZO1c00SZ4OPRl4a463uQVA80WTxDhFv7vSOuAylZjkkbPa4VMl4oy-6AWTIbNYL9SU6jwXnzLU9VlH0J4xqYrw-IVWlFVWb9vijEBKiTJDk2kuAWcxCW8pZYjl5XtsrPtuQiXSWopqu6SxmtSyfOZSbY2wOqZFW32h1zJzhpueGSBbdWfWL7lfylCYj-AqHyay4Zu2uidx1prN7fSP24i0Vx-XczmG6xpHU2hdCLU8u5yIPfO2zwNwrhAhsxGCLR9eMNd3GTx77ZV3TJBT9PAj0pdTBM7CiNi_PaYTNK8YBIooDArOzr4IrK6hG7vR1vzE3C8LaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس، ونس هنگام ترک سوئیس، ترجمه ماشین:
🔸
سازوکاری ایجاد کردیم تا مطمئن شویم نه‌تنها تنگه هرمز باز است، بلکه باز خواهد ماند.
🔸
قیمت بنزین همچنان کاهش خواهد یافت.
🔸
سازوکار درستی ایجاد کردیم تا آتش‌بس منطقه‌ای تضمین شود و درگیری‌های اجتناب‌ناپذیری که پیش می‌آید مدیریت شود.
🔸
ایرانی‌ها اجازه داده‌اند بازرسان تسلیحاتی، بازرسان هسته‌ای، پس از مدت‌ها وارد کشورشان شوند.روشن است که ما این رژیم بازرسی را تقویت خواهیم کرد تا مطمئن شویم آنها هرگز به سلاح هسته‌ای دست پیدا نمی‌کنند.
🔸
بخش زیادی از تیممان را آنجا گذاشتیم. ایرانی‌ها هم بخش زیادی از تیمشان را در آن اقامتگاه گذاشتند تا کار را ادامه دهند.
🔸
این دارد بنیانی می‌گذارد برای چیزی که می‌تواند خاورمیانه‌ای واقعاً دگرگون‌شده باشد.
...
خبرنگار: آقا، خیلی سریع؛ دیروز لحظه‌ای بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما دست ندادید و بعد او از اتاق خارج شد. آیا احساس کردید به شما بی‌اعتنایی شده؟ آیا فکر کردید این کار از طرف آنها عمدی بود؟ شما آن اتفاق را چطور تفسیر کردید؟
باور کنید، در چند ماه گذشته زمان زیادی را با ایرانی‌ها سروکار داشته‌ام. گاهی آنها را به‌عنوان مذاکره‌کننده‌هایی بسیار گیج‌کننده می‌بینم.
اما ببینید، ما یک نشست خبری کوچک داشتیم.
آنها آشکارا در ایران از همان حمایت‌های
متمم اول قانون اساسی
که ما در ایالات متحده آمریکا داریم برخوردار نیستند.
ما با شما صحبت کردیم و بعد چند جلسه واقعاً خوب داشتیم. چیزی که برایم کمی خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی توفان در شبکه‌های اجتماعی شکل گرفت که همه می‌گفتند ایرانی‌ها می‌خواهند بروند. و بعد ما حدود ۹ ساعت دیگر با آنها صحبت کردیم.
بنابراین فقط به رسانه‌ها توصیه می‌کنم کمی به آنچه از شبکه‌های اجتماعی ایرانی می‌بینید بی‌اعتماد باشند.
آنها می‌توانند مذاکره‌کننده‌های گیج‌کننده‌ای باشند، اما احساس می‌کنیم در حال پیشرفت هستیم. ممنون از شما.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v3MpxTm4Iw11KA71sOG4UJtXApq-XwuAHiGTTJJGX2rOvS5SBgtgeJey13npzd8AAbyEEpsp8JZddry-5K3iCr0y3FxQAzH_u26U53KTvMEsRTRw7lO3sozCeLZigelBbmpSqhkHXsl2XjIgdjJmYqu-gNWhE9xGEwniVOdeuNan6doYZ08lWVHPFhYHqejR57e9lw9vlEyKU__FBPdGakCTxKk1-zohXRPM5QMmKT4cvp-aLETYvfE3OCowfSNJQy9ckKLbf6BGSdYYn_v33s-t7meh8PTC5DDwnQiNXp-vp3Onsaei6ifX-mpHeaET-zKNaBW12zr29XByr8o9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvV74hMOX73z15rTEYomx28rOkRCfN4OpuxC2hK68X2ZeSrB5qaS-7MVO9UDgS1qyNthjcJlvlhxM-nR-UPqvPZ9iytr4XBPGeRydLjkiKlIswpj3dG10rPUHuiSLlI5cwGONhiXY616L7pFTPGPMr_DWemXfC9jnUM49QKkhlLk52JRmkxQKAUk9Sq1cBZghj3y78IKAxsymE_sxvWvl35ByuyyzYFLg-V1_nh4Pt-KisncdkXJ8-CnXYFJwITxuMfqEbJYQ1DlBrRIBWn57DvJ1oHqW5q9E_JJMTZKwoOjKM7qLJIrfJbiWZpzwT0pUDkZ6AG6h-XpYp-w1k8lZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، رسانه‌ها خبر دادند که محمدباقر قالیباف، رئیس مجلس و رئیس هیئت مذاکره ایران، که تازه از سوئیس به تهران بازگشته بود بلافاصله برای دیداری دیگر به مسقط، پایتخت عمان، رفته است.
به نوشته روزنامه هم‌میهن، قالیباف در سفر به عمان به همراه عباس عراقچی،‌ وزیر خارجه، قرار است با هیثم بن طارق، سلطان عمان دیدار کرده و در زمینه ارتقای همکاری‌های دوجانبه و تشریک مساعی «برای تثبیت ترتیبات ایرانی»‌ برای اداره تنگه هرمز گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76598" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/APxNLQ989Ucr0LDVB0JpQJ5R1Qhi_5mpMO06YOFv71o6qpFi-E0aYASLplYcK_bZBnBSQmlWiCFTeRdP251AoCdwFUabzwkloU2Jh51Rsd1Pm-ohARIQqxQgy7AnvGJKAsUk2hQcUyl93IeH-JDRkBzeufZX787Zb0II_wyQqDD2Pzn7broIGngn3UYbTTmuQELyMW8lEjbSzO5Udds6h3nZIM3OWwH7vPgeawiDy33BD-fGJYPkR6_EaFChIfyrF8tPyDB-Yw03K0cDteDbo008rvOX8zT830HMl09ZDunnuABmpaiNwmabGA4THbKF011z2xj6Le85DezVgfSN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نوشت اظهارات جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره بازگشت بازرسان آژانس به ایران کذب است و در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76597" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=Asa8losjo0vMk8k-3nkwK7QmsgTD8xUseFU1Iv8suuw9p1VEK4LSUQO8foiUPiowpe66Si3y0nedcde-H_7eAPOgtvz3l5sbXm6ePP3RJaxqLxG0XIvUGVJ_jcOurYwPthEY56xSnY_OS-rnuKu9UmiBco9sz7tDwTIENVRkMyIyWlpopVUIJ0oOAh71l9Yeqbvd36tlWjb_l9MW6UXGu7oVWnQbYPiBAh1FvuRkvMGaQi5pcSkXtN7i0GoSrBzVRawwylAR6qlsAxQRfG8ItjnV363eJ1_F76T3B4nBgFZtyhEijMuy4AeptHVRuh-owI3mazqoe4oOF4NFnfblpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=Asa8losjo0vMk8k-3nkwK7QmsgTD8xUseFU1Iv8suuw9p1VEK4LSUQO8foiUPiowpe66Si3y0nedcde-H_7eAPOgtvz3l5sbXm6ePP3RJaxqLxG0XIvUGVJ_jcOurYwPthEY56xSnY_OS-rnuKu9UmiBco9sz7tDwTIENVRkMyIyWlpopVUIJ0oOAh71l9Yeqbvd36tlWjb_l9MW6UXGu7oVWnQbYPiBAh1FvuRkvMGaQi5pcSkXtN7i0GoSrBzVRawwylAR6qlsAxQRfG8ItjnV363eJ1_F76T3B4nBgFZtyhEijMuy4AeptHVRuh-owI3mazqoe4oOF4NFnfblpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تا وقتی که لازم باشد در جنوب لبنان خواهیم ماند
بنیامین نتانیاهو اعلام کرد که موضع و دستورش به وزیر دفاع اسرائیل تغییر نکرده است.
نخست‌وزیر اسرائیل نوشت: «نیروهای ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم علیه خود یا ساکنان شمال را دارند.»
او تاکید کرد که ارتش اسرائیل «هیچ محدودیتی در این زمینه ندارد.»
نتانیاهو بار دیگر تکرار کرد که ارتش اسرائیل «تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهد ماند.»
در مذاکرات ایران و آمریکا در سوئیس، هر دو کشور تاکید کردند که حفظ آتش‌بس در لبنان از موضوعات محوری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76596" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VtwAtkx9ZzRi-7Cl81460kZXfZi7M6_2A63tLnpwnuovAie90EQlpLscSJCAt-PUpjHlm3uKhjAhh2nminp3npO90R50Mr5-tT5UzJ7T7Hv5edO86t6XuWwANmpNv2kFNoWX-Mn9unZXnahWO1ozSe2sV4XeBOg_6qiy8OfXE047_uEjZ5SbyWiDjeW8oU9Xt0R9emsACXDjDiglerzOx6uCLYjtnOPOwrgbzDLv0FiqRuZ017nqPUHeDtrddLWtkUkXaAK0hUKgsdl-81q8FTA2g6CoRJCv6HDGaAJN_mT7A1SMF1NSQd6zmcXVKRSfiKpy_HymhdJ4V2dj8cCpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا با صدور مجوز عمومی، تولید، فروش، حمل و تخلیه نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران را تا ۳۰ مرداد مجاز اعلام کرد.
بر اساس این مجوز، تمامی معاملات و خدماتی که برای تولید، فروش و انتقال این محصولات ضروری هستند، از جمله بیمه، مدیریت کشتی، تامین خدمه، سوخت‌رسانی، ثبت و پرچم‌گذاری کشتی‌ها و عملیات نجات دریایی، مجاز خواهند بود. این مجوز همچنین شامل کشتی‌هایی می‌شود که پیشتر تحت تحریم‌های مرتبط با جمهوری اسلامی قرار گرفته بودند.
در متن مجوز آمده است که واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران به آمریکا نیز، در صورتی که بخشی از فرایند فروش، تحویل یا تخلیه مجاز باشد، امکان‌پذیر خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76595" target="_blank">📅 16:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rpJthtlpLrxCZ8_2ZQPdPlwULb56Jfvc__sFaTrZXcDhYUzKJIrvF8BaZvkuU2WV9tQ6_YJ6pj-fzM_LboUY5xY29FdPtwoggChlOXWcomL-mvEddOtyhgzbobr15HPhmmbRnTdLsSZSXrw2Rz22_IG9BX0V2OAxmpjsH1Ua37RHMA8da60vBfnQfMt8vBHKgmr1-AJ7CGZH49H8D_lKSqujo9ftXie2vRoe-_BcigWz-zO8-ylGni59nbHPkojLr87BIVe4CVjwADn_McL3WcQI37bXaPWfTpoHnsqmNPl_3q4odzd2-hEYq_HZJKg-8NPAPx8Y9Rxbv8O8y-zEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش هرانا  در خردادماه ۱۲۷ حکم اعدام اجرا شده، ۱۹ نفر به اعدام محکوم شده‌اند و حکم اعدام ۱۲ نفر نیز تایید شده است.
هرانا همچنین از ثبت ۸۰۹ مورد بازداشت در حوزه آزادی بیان و صدور مجموعا ۴۹۳۳ ماه حبس، ۷۶۶ ضربه شلاق و ۵۱ میلیون تومان جزای نقدی برای ۸۰ شهروند خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76594" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/shHHIsqYJWSO9xSqEx6Usj89Hx0xTn-G4Q_cHSHGMELL4EPTBOa7islTzdefR5jGxAc0Fa3uwMS2ZgjC6yboLANmP59kjptqw0K12rUe-f5aj3ZeiLEBO3m6m1pBs4X7RnmPzuz9dnVfyLvHdX8OizaSIZMc5LsVe9__JFgwrnjCrD_gtZo2E8GSwZarlP8nB59VG5vtqobw59pijRSPzfGAEFjabIjv1ml7TH-sc2M25jycHDtkomyBy3UO9sGMNHFbOFysy2kfFw_RKH5Qx230qRto3YtjnFL-IHFnQESRoOZxWHwzjvMZbw8zIx9tW5A50lZpPVZeF1xzxrsEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nH0Eat-RcKRYzZRhK5sziH2uTLOtAgVcIz_QSkWNjCHcrhxPjxcZUoTbmkYEGTdwL5tZT0GcJzWQ9PKBveIPd6w5sAymfRjilJ_4pfeB-EsfxiZM0shdrUiVGvBmDjD4ALaJskprzqk4KsNIT05aiJEch1YedAkah28Vu2sPTQ4BssuE4Zhi-YYC881wQXIFHvx6LL4jDHm5O6WhHwmyXXWgpEZbwKRJHfEUf-0QjZEmVJo4L6OkyWqV_bH5UJ7w1O2zCfscByh_mkHC8y402TiKumJzILZAhYaLMHz0rkLYjn-gfm5xn7rQOy4Iwz5O1SIKqfLCXs2WI844eyaWfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BhYdmvbhHMim0AnyJpdDtBzCRoq3_SJEU_inaxFSRtABmqfVMJjbUqX8bTqBLdrkSYRmMV4pk4VngePk6Tf9nUDsqK_LpG5GHIe9pjxU-uiLpislQA3---PG5kFDoO_52N8J3wE-tf8lEHbIRyrtDquGl7uGmlsF6J1H5y2WQS_Ra4iyP46G-d5PTidsXYKJ2tL5vEXq8sLSA8dTrYM-YIkhygmI-yYNgha9_kgXWIwk_2bmQmW6gbQl1NOgp-D7zDFKNXkxNoJo0Fw9rlOUwQwEmPQfvSWkxCXqwZRgvyQByXCcTJqm3Y3RzT2zIjWrMpRqUous-FeD61exJaa1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UfKhIk9e6lh0kzO6p0gKLjRu-T4BBdz4Vc8Y5tccHBlhw3oOmtD82G9qcVoKh5eQGVwBORqvmRnsyV5hLkc_l0AbMQlbcWHTh19nRYuyllyLyl-YaPXdYl9ZSGcEEKthWXQiMtVguPaaBsjUqfq-ouL6eAz-LlbZKDwXxCsksguY1BWSQgExjwuRqe63qrMgwmGY9gXdD-bnFh1zx4YL2OvKUtW5q9cgikOMJgpem77sJUUR3pEkeqyWwrfBOLN0Dhu-bimDy8itVa0XcEXkiH9z4K7cjCfNGhEC2rf-D1vhmJSUlO07OjW5LeZUvsH-NqwokYrPFszvc9cBYRBlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GjwF7kuzr15zjyOrrhFzTMrBe-xcn5jdeW7r0beBCdbsKKBIOjuP__FsoqTu6r7eiF2HjB5S4zqaZJVXKJancpQc7hFAukG7yIDPeM43ybbN8FCDhxYqMmQgnCCkdNfujLmQ17PC-Z5TR8RCUBeeJz06_khreWjcvYJG0N2zcOPtyftJyXqeFajsd7FvAk02HYDlA2IpZ-j7fpcfORzhuZgB3VrPVTJi6kyJFA-tOXSAn5lofOlOX-huehFSdcj3N8pB7T5rIyZiy3ErnMcN6Biz5vuzPTxE3fHnU2k9IWyBE8NRqWiIPVjMwcJYHYJFKXetaThZvD1-OcJ82KZ3_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=SOH_e-FVm20hU2Qheg7zYsjI3Q0pTMmECwJdjWSuQHC-x84DveSJCzdMHiqI-bxYwhbWRs7wICpN4NEMAZIZSJYCgFDN-F8k9gKKiC4GR5pt-L4PfMup5qGdyG3nQIPNFTWcp4gO_TsC4V4UiqUGrq8B8JxCI-vdoQrTndb2p5lrwBbduV9DBz9TUQEpZT7SkBIFssZrybg7z9i4nAU2gy3lq5pPSY5Yzg_Fch7Go-QIyyp0z_X6YeKmLBCPhgHH6D2eFhCJ73Pnn6GGCGBmfg8nRsAw-IJX7-TXUOluOW-z6H8Gs0e96eB1Sxyz8zcUSX07fNia6yxfwczPeUkJAg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=SOH_e-FVm20hU2Qheg7zYsjI3Q0pTMmECwJdjWSuQHC-x84DveSJCzdMHiqI-bxYwhbWRs7wICpN4NEMAZIZSJYCgFDN-F8k9gKKiC4GR5pt-L4PfMup5qGdyG3nQIPNFTWcp4gO_TsC4V4UiqUGrq8B8JxCI-vdoQrTndb2p5lrwBbduV9DBz9TUQEpZT7SkBIFssZrybg7z9i4nAU2gy3lq5pPSY5Yzg_Fch7Go-QIyyp0z_X6YeKmLBCPhgHH6D2eFhCJ73Pnn6GGCGBmfg8nRsAw-IJX7-TXUOluOW-z6H8Gs0e96eB1Sxyz8zcUSX07fNia6yxfwczPeUkJAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی گزارش داد «تحریم صادرات نفت و پتروشیمی تعلیق و محاصره دریایی برداشته شد.»
علاوه بر این، عباس عراقچی اعلام کرد برخی از دارایی‌های مسدود شده آزاد و طرح بزرگ بازسازی و پیشرفت اقتصادی ایران اجرایی شد.»
آقای عراقچی این موارد را در پستی در حساب کاربری خود در شبکه اجتماعی ایکس اعلام کرده است.
@
VahidHeadline
معاون رئیس‌جمهوری آمریکا اعلام کرد که در گفت‌وگوها با حکومت ایران پیشرفت حاصل شده و جمهوری اسلامی با ورود بازرسان هسته‌ای به این کشور موافقت کرده است.
جِی‌دی ونس، روز دوشنبه در سوئیس گفت که گفت‌وگوها درباره بازرسی‌ها ممکن است از همین هفته آغاز شود. ونس درباره زمان آغاز کار بازرسان هسته‌ای در ایران تأکید کرد: «احتمالاً همین هفته، شاید از امروز.»
معاون رئیس‌جمهوری آمریکا افزود: «ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم. گفت‌وگوهای فنی در هفته‌ها و روزهای آینده ادامه خواهد یافت».
@
VahidHeadline
معاون رییس‌جمهوری آمریکا، گفت یکی از اهداف واشینگتن در مذاکرات، ایجاد سازوکاری برای نحوه استفاده از دارایی‌های مسدودشده ایران در صورت آزادسازی آنها بوده است.
او گفت هدف این سازوکار آن است که اطمینان حاصل شود منابع مالی آزادشده به مردم ایران کمک می‌کند و صرف حمایت از فعالیت‌های «تروریستی» نمی‌شود.
ونس افزود جرد کوشنر با همکاری مقام‌های قطری طرحی را ارائه کرده است که بر اساس آن، در صورت آزادسازی دارایی‌های مسدودشده ایران، ایالات متحده و قطر بر نحوه مصرف این منابع نظارت خواهند داشت و باید آن را تایید کنند.
به گفته معاون رییس‌جمهوری آمریکا، این منابع مالی برای خرید محصولات کشاورزی آمریکایی از جمله سویا، ذرت و گندم اختصاص خواهد یافت تا در اختیار مردم ایران قرار گیرد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در پاسخ به سوالی درباره تهدید تیم مذاکره‌کننده جمهوری اسلامی به ترک میز مذاکره، گفت: «آن‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم در شبکه‌های اجتماعی چنین تهدیدهایی مطرح شد. اما ما دیروز تا مدت‌ها بعد از ساعت یک بامداد در حال مذاکره بودیم، بنابراین آن‌ها جلسه را ترک نکردند.»
@
VahidOOnLine
گزارش‌ها از سوئیس حاکی از ادامۀ مذاکرات فنی ایران و ایالات متحده، به ریاست کاظم غریب آبادی، معاون وزیر خارجه ایران، است.
رسانه‌های جمهوری اسلامی نوشته‌اند که قرار است دوطرف روز دوشنبه اول تیرماه در مورد سازوکارهای اجرای یادداشت تفاهم اسلام‌آباد و تشکیل گروه‌های فنی مربوطه با یکدیگر گفت‌و‌گو کنند.
با این حال تیم اصلی مذاکره‌کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سوئیس را به مقصد تهران ترک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76588" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X-GsyKcCgMPhhGkOHo-A92I-usWhAPOOtFG3C4izwFAh9tAY8JMlhYDqw7PpR59PWlg63sL_er6Kee0zhDjla1HL4S5FJESGCnmeyIpWEzzOapf7jfu_83rSiWMp1g8mQT65AptxaYIgUjDHLDgR1S325DoY3wl1TWFe4pGzQHq6ERRg6VhSfzhsI676poomuofB0UfXsabpk4ZChmsoAfFocVTWx92CTNcgARAncM4Loqp65A2xYNqpqzP9RL9hqVKXInPlxMMZuiC2YMubq5ZsMaWNYbhfiJw2nko0rGhuRPn1pQftScgq9YckYuzdD9C425xbdJvrjJDdl62bLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانجی‌ها اعلام کردند ایران و ایالات متحده روز دوشنبه اول تیرماه توافق کردند خطوط ارتباطی مستقیمی برای باز نگه داشتن تنگه راهبردی هرمز و پایان دادن به درگیری‌ها در لبنان ایجاد کنند.
بنا بر گزارش‌ها دو طرف از طریق تشکیل یک کمیته عالی مذاکرات، بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیدند  همچنین قرار شد گفت‌وگوهای فنی از همین هفته در بورگن‌اشتوک درباره همه موضوعات ادامه یابد.
در بیانیه مشترک دو کشور میانجی یعنی پاکستان و قطر آمده است که: «طرف‌ها با تشکیل یک کمیته عالی موافقت کردند که مسئول نظارت سیاسی بر روند میانجی‌گری خواهد بود. مذاکره‌کنندگان ارشد به‌طور منظم به این کمیته گزارش خواهند داد و گروه‌های کاری مسئول موضوعات هسته‌ای، تحریم‌ها و نیز گروه نظارت و حل‌وفصل اختلافات را هدایت خواهند کرد تا اجرای مؤثر تفاهم‌نامه و دیگر مسائل تضمین شود. کمیته عالی بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیده است؛ نقشه‌ای که زمینه را برای آغاز فوری گفت‌وگوهای فنی بیشتر فراهم می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76587" target="_blank">📅 05:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vbmFbSknV6vUrFDxuUJc7DYFZ9WMyoVdc3lEgAsvfWffVwwsu39fiRZPRQ6Vl49t29q1oN1tYLfi5qci-vy-JiZwHV-6Z8iZT3TZzggZrFa3hF4XTjxplVQpBCv3FVNRiWCbYq6ydxLCDTggVa4ua2NDidrZJz3K6r7jgTtCZp1Zc16lEPWrPTykeXF1UQpELk6j3ur7EOgbjNR3Y204Apj-SYb4eI4CQLSsng2ktfKxa3mVbr5Hu1tsvYq0jpIlACsJcoHz7Plyca4ke6lUQ3zuZKvxRrh81ra0OtHj5yuxzhJHFQTgMbWK5RJnt3exA1WKVwopl042vo8Q_4tujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین: ما این‌طور از سرزمین‌مان محافظت می‌کنیم. mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76586" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/izzHsm2o5DhyunTRlTCWxNbjKQI_aJSOYK2n-r4S21PDuIA0ODGJiJoli2BgLiKlBnZz0-CRk7rzCk4Vg3fMSBX-oDTA7BB7J0oVai7QAa6-v-OnxFq8nS8kEWj0L4J1VFFX8E1vaLwBjd-CFNEeemfqGDQ6Xcrs7fa6k2msVIARFIjUBDUbOOIbvRtZ_6-aOHYk45jaeXMt4mmKFLdSTrgLBOJIYBQUI_ghJglGgX66-IG0q-K9nlaG3irN3cbL3PWREzKEgod0zR69NG-jGWUX8xpwgrbyYO7NorWiQZHejTiVNZyX_5CZ23Whp9pdidTrzUoFud-mU_nHhZiRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MgGaGcE57YNfBHXfbsW0Atq7Yd2trLsnRdjosuBocQjI8o701eJorBOYLUIpYniEsl1zDQ0USc-MuPV88mdS95DoHPZ3Owi5YRGpx2MNshFKPP7T2DCxe1HfDQBryTOWaKJXaBbYjs1uHJcGba5ynezBGdPfm0anEI4OUKJu-KY5YieNtUJHuuwjJLt00701OUL6JIED-XOPUFQ-oVdUesyz4a8DEPSdUiweDBInVL26U8iu75fXVlcIFMLpjtOfXEKVtWj1xiBS8jBYXr39CjvQV4WSAGUV-XrWt1uEgPgWSuNOrWcrrOyBPhreyDSPv-0sY7u9hGOqzS868KOAYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، اعلام کرد مذاکرات سوئیس با «پیشرفت‌های خوبی» همراه بوده و گفت‌وگوهایی درباره پایان جنگ در همه جبهه‌ها از جمله لبنان، فروش نفت ایران، آزادسازی دارایی‌های مسدودشده و سازوکار عبور کشتی‌ها از تنگه هرمز انجام شده است.
او گفت درباره صدور مجوزهای لازم برای فروش نفت و آزادسازی دارایی‌ها پیشرفت حاصل شده و قرار است سازوکاری برای موضوع تنگه هرمز نیز تدوین شود.
بقایی همچنین تایید کرد هیات جمهوری اسلامی پس از انتشار آنچه «اظهارنظر تهدیدآمیز آمریکا» خواند، از ادامه نشست چهارجانبه خودداری کرد و مذاکرات از طریق میانجی‌های قطری و پاکستانی ادامه یافت.
به گفته او، تهران بر اجرای تعهدات طرف مقابل، به‌ویژه در زمینه آتش‌بس و تعهدات اقتصادی، تاکید کرده است.
بقایی افزود گروه‌های فنی دوشنبه مذاکرات خود را برای بررسی جزییات اجرای تفاهم‌نامه ادامه می‌دهند و قطر و پاکستان نیز متنی را به‌عنوان جمع‌بندی توافقات حاصل‌شده در جریان ۱۸ ساعت مذاکره منتشر خواهند کرد.
@
VahidOOnLine
تسنیم به نقل از بیانیه مشترک قطر و پاکستان گزارش داد که نخستین جلسه مذاکرات نمایندگان جمهوری اسلامی و آمریکا در بورگن اشتوک سوئیس و با میانجی‌گری پاکستان و قطر به پایان رسیده است.
در این بیانیه فضای مذاکرات «سازنده» و روند پیشرفت «دلگرم‌کننده» عنوان شده است.
به گزارش تسنیم، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
براساس این گزارش، «مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.»
تسنیم می‌افزاید: علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.
@
VahidOOnLine
عباس عراقچی بامداد دوشنبه، با انتشار پیامی در اکس از پیشرفت‌های حاصل‌شده برای پایان دادن به جنگ لبنان در پی میانجی‌گری خستگی‌ناپذیر پاکستان و قطر خبر داد. وزیر خارجه جمهوری اسلامی نوشت: «صادرات نفت و پتروشیمی معاف شده، محاصره برداشته شده، برخی از دارایی‌های مسدود شده آزاد شده و طرح بزرگ بازسازی و توسعه برای ایران آغاز شده است». عراقچی با این حال تاکید کرد که اولین آزمون واقعی و جدی این دستاوردها، عملکرد «سلول مدیریت منازعه لبنان» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76584" target="_blank">📅 05:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiV-cdmRr1v34mrdPoNTHBXm8EeCcsXdNVrWIAfGDLKfJFsYTHUrCOYfOIi-emEGdrSqCtaDDe7dFjjVvWuKuJRhf7hVseiahdo7kdtf1mAZ5M9ZVhCGsIX_JdUB6rb29Q791GPU8uCvLGnS-_PpWafOCxmn8rfONhSNpaWVjTE_eRcDj-Oe_XQzJ8TACY4bL7KQumxuCNVDxwkZjn8OuTWbpUP0SxmShGF78XwHzpW26Khpx6sLS760wTYzBaRGsZmCBb3woqjb1P5Ho_LC70JTUVumVlEOTiq07cyOI_t0u1HfZTU0-WYPC_wpiaEf68c7dKMA8KeIcOvsVIYHww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، از دو روز دیگر، یعنی ۲۳ ژوئن (دوم تیر) در سفری دو روزه به خاورمیانه به امارات متحده عربی، کویت و بحرین سفر خواهد کرد.
در این سفر، آقای روبیو درباره مجموعه‌ای از اولویت‌های منطقه‌ای گفت‌وگو خواهد کرد؛ از جمله:
تفاهم‌نامه میان آمریکا و ایران
تلاش‌ها برای تضمین عبور کامل، آزاد و ایمن کشتی‌ها از تنگه هرمز
اهمیت حفظ صلح و ثبات در منطقه
وزیر خارجه آمریکا همچنین در بحرین با اعضای شورای همکاری خلیج فارس دیدار خواهد کرد تا درباره اولویت‌های مشترک کشورهای منطقه گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76583" target="_blank">📅 01:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GzWtff-cqXZ9ImtAqfVBhbPqoyuPqGyeCWaEWJvM64G-bumfzj4Mize4GRNsy4vlJDr6zxCG9_HTJTDygDTc0WZJ9JfZgj_Ynp4nhzenluL4gaMqwYt5hsQ_wrNAWd-_QiOvjLbEIO9huJt0CoQ-P-HQKRg1r3pgAvaqEMtDmk8KL22uXpL0vWUOFkVw1dVlbwqN7FxV9m4Oz1yvAFhL1CLovQEJZ6hOsqYD2ol_9jX8d4x9j6TlGBby6X7pNyNNUZ_Q5YiNOPo0LBN-imUHOzTXIxL9b36oOtbAEQWTrLbntGvm5kHMLsLlQPaLgCXU-GvRZhzPGiehX8WtJyMAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین:
ما این‌طور از سرزمین‌مان محافظت می‌کنیم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76582" target="_blank">📅 01:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r0V7i7aJ9nE4HjXNw_xUUIAjd6P8fFyWsvIwCwAIKY2EIXuvXX5np28ZIl_PBIaCCRhal9lEApmtIqY7sxq0rJcr2wMymyf3EzWB9SIKnU6A2BDlmq2Io16IV5nVkeRBknzkoyS_Y6c3lZacaE8zoVMSumaCtY-f0Epa9moeLg6Y5MS_kzgtSVL4mO2fMTudbwk4yMItpkh7cpk8phpMWlP81raNL6ZgTyADGVxSWTYKf2KOtJnNsc9dzfO4QxFJniU3Grdos7adN4PiqIFf0gtRuS4dBO7m5NlfWukYNYUTgzRl041Cmf2k2rTyu43W0cGAn-4P3OgBXgefN4HO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست ترامپ علیه نیویورک‌تایمز درباره اخبار جنگ:
تیتر نیویورک‌تایمزِ فاسد و رو به سقوط این است: «بعد از تقریباً چهار ماه جنگ چه چیزی تغییر کرده؟ تحلیلگران می‌گویند نه چندان زیاد.»
واقعاً؟ ارتش آن‌ها از کار افتاده، نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آن‌ها تقریباً نابود شده، دو رده بالای رهبرانشان از میان رفته‌اند، تورمشان به ۲۵۰ درصد رسیده، اقتصادشان درهم شکسته، به سربازانشان حقوق پرداخت نمی‌شود، تنگه هرمز باز است، نفت با شدت در جریان است، و بازار سهام و اشتغال در آمریکا به بالاترین رکوردهای خود رسیده‌اند. این‌هاست آنچه تغییر کرده، ای ترسوهای فاسد و بی‌اخلاق، و حتی بیشتر از این‌ها!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
نحوه پوشش خبرها درباره ایرانِ بسیار ضربه‌خورده و آسیب‌دیده از سوی نیویورک‌تایمزِ فاسد و رو به افول، از طریق «واقعیت‌های» جعلی و ساختگی، به نظر من «خیانت‌آمیز» است. من همه گزارش‌های دروغین و مضحک آن‌ها را به شکایت چندمیلیارددلاری‌ام علیهشان اضافه خواهم کرد. آن‌ها مجرم‌اند!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76581" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NhOOvthNYUH38nZdzoFUyG-ZsCiVfvbKJL66Yz4KBG3cCFCObYUMzB5ghWUWWVUZ5Rq66ivD_Tru5KJVftIhO4rLsNk2223ubgSTDVFS4dAwmb41dSAr7PPxw8Qze-8byF2DuvIRSODOCSSWnMNncwFclkQgQPHDyp6Te2x9FiAShCgSJdm7HQ0Xa7pDXrsAQI07Ms9eIbJ4WGoAvkt68alf5rtw0iMG__LCwsFet55Q8688S3_6JB3B1TFC1zRA09g-PamLf_eu0b3ZIfkaETxwluN0bA7NzZXed8aPwug0Z-hLAye3GIIvLugEenNmIVLtM5LGKYsxhWQYYHe5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B-le7SkEhoUZ917byLd800SMvupRUVNaaD9UZh4XtlaA1G-oCMHFpRSXVN8eEQNxwPJjIUWKWVrUEyed_vfVJ_QatYMN6AMTXQdu8gUSfKVBV-FpDhDxe0X6kWZk9IsmlPDaEsVYpItbOABiYc3wQQi_g-E9t2rnwYGi5n0qxmJ0laM3KqYZG9eACzweOZDwHA1Z442LUAvKKKNRLb57744IlSElNwqg95mPoYu_s9R_5pjt3Y33OaoUwlmkIfhbqDWpblRZbU_IS9PhtSFtpLwc01CcrGbFEfI9H3ybL9N3ajUNmBHcMPYn0EucygJJuTsvay1_pfYr_Npw4wC4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lNTRNBMyE7kf8E1dtwOenS4w2rB4SL9iOsKBCy7LRATjWPKvjyfEGMcTPSpeaVQ84hu6oUYFuy6uwtFMqil-e6emwayA9NCjV-iMwWafQVaQYkqi8IfBTipT-SMBpw6r6ev85UKR2TFqYPbQNWvIvAQe_q3DHzvcNkL0KxEVt4bxxiQKui7942b9A0Q9-Fm-KHbGE89EwVOA6AG9--vW10nY59EixJmRj0tvBsHca0QbqIm-nhAKl7cxDJlKcA_LIT9CB6yqupnPc6cvbOJhnf43hEgSIjnCWyxZ2x9YpER7EMVzprApW5PueiB0mn48ke4EsG1CINXb0ClZjFPxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rwKeQTuryvQ7M5WHwS7n-bNFBjH3HfPtrGrrpK08gBcnGy2QtBAyShMseXJLHLOtZGrub3K-A5Z1Pr4L1rkR1ByTevkdQwpOh05jKYMnmSrI1IeKGZrnLDj-BuJXtOqF2ZxNK3XL36L6UDV3T_nZ9Amzx4g00_SMFIwjLaV5eYvQyvThFQRQB1XHP9gTlJoPEomiePZ0eWXWx41GCYfBk7adezr5h7BsRkZuHngRRmCg2YnBLF0jz3l0n9s6WcfnI72Y4t6ycp7hsET-Zg5sjCwvNhgpZ3YVu_ram2gLticI7NnkwMHEe09yBch-HY4HO6govrWL0n4Axpco9ZNJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k9H1d7gZSEAeEklHsFgb2uEA9JEdVxBj7elUvKj_YxgTESUKzFK08OEXv9prlkG2JSiuA1GN8h3kHwP6-CZels-VsWhZo7o6O10GteDYfeGCtdxvcFFeJle7zblaKAaM-8Zz_Yq4SDcgKOhGsQ3P3xbLJXzRbddU8g1UTLABPQ4cn71RhGE9YoBNUJJpsW4W293VqZRO0xUFMIGa8QmuIe-pPuSWlGCg93TxSfWlY_TRnvUUXKftv-y4B8Y14IpuzHAYTqfBB8xWHGjrPhyi3PtbcpAzYMTKW4FXcGUQjkoEYvZwrm_dosqEJXE81YBnXROjo4ADuMWFCbHSJc359A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kev9ua_qWGQN4r9c6TS3nPXc_KWOIdU-2szR0IGBf9aueQlMu6weON61jhFd_VkBlm9W-yeoTS7_A-1HXV8iGz6kfoIUxfuJB5Yqfexv2R6o5M7sTaeSd-mdMzQeBu6ofkb0JN_1XFYM5BS0mFMPoG4feBBidQ98OiwiCH-5sPbl0-fL55OGca3zWJ_aHnP7FK-rmQqQ_BwaLfAhuKZkSQpFYgu559s9MChiTCAPZE4Ppwt3ttskEEGQg-okKCFbFw7T4jZl4iOD-f6jd4X8wJC9PRhn_nkwuPJkTeJe7NTfSE2hkasDVKNnZh8pq8oSXti_r3e4z38cgD1uBYQOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NZMzMVIiYAUndAtK_9tajOYW8eA0dLp7d6dgUQuyFRMBHy_0VQmO4wYNhFQfGNijVufGFn2FYrolbQiTPx2pcH7LB0ksdh9y5C49nLzuuE-Yrq3OeH5Z4_cExjlTlGLrneFEJxvw_PpBYORJAvfxTr8_NOhJignC8aRNIjcUMLcytBn9J6Dbgyrlwk0coF_5IUZTso1XJ4PtYa6yRBvAwMPZaP7sFalAejXI8CcBY6VEh-FK3bR_ghpt-LeASImEWphO5--PwiYfBqjoPANetLajsC_28MuWJlOQrnAPCeFSHPS7EqVMKpa_R8wVOUeBbB4IRjqnSpMzzQJIxHUT5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=HLwFq_e2fySyZNv59W8HHb2McdOkodPjeaTIAgVsS_9_DHQK6FmnO72T67a8ryBglcxy9JH22p0qLFF0KPcuw7Bv63U3MehK71VAcDRr49NNfxVufsn36IVplkwXpT3ki5D8oVFym3WygiK3Upt8yLdFPmQJA0DbmXhSX5O_REUP7PJXgtbUUPp1b8nKkE-qtNOBQRe2IWR4KilYpIeJKExMrlbkzqKskKFSAIMrYsVWrjBQQp8OoIxzEPe8CDUqm5krjzpU5OjscaIVS9X9nTVMg-Oz1vQficZFP50l-ygj7lQLaZ03yEbZRih2CTJ4n1-80jLgVhd_ggfHtR9C5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=HLwFq_e2fySyZNv59W8HHb2McdOkodPjeaTIAgVsS_9_DHQK6FmnO72T67a8ryBglcxy9JH22p0qLFF0KPcuw7Bv63U3MehK71VAcDRr49NNfxVufsn36IVplkwXpT3ki5D8oVFym3WygiK3Upt8yLdFPmQJA0DbmXhSX5O_REUP7PJXgtbUUPp1b8nKkE-qtNOBQRe2IWR4KilYpIeJKExMrlbkzqKskKFSAIMrYsVWrjBQQp8OoIxzEPe8CDUqm5krjzpU5OjscaIVS9X9nTVMg-Oz1vQficZFP50l-ygj7lQLaZ03yEbZRih2CTJ4n1-80jLgVhd_ggfHtR9C5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال ایران در دومین دیدار خود در مرحله گروهی جام جهانی ۲۰۲۶، با ارائه یک نمایش دفاعی، در ورزشگاه سوفای لس‌آنجلس مقابل بلژیک به تساوی بدون گل دست یافت.
مدافع بلژیک در دقیقه ۶۶ از زمین اخراج شد و این تیم ۱۰ نفره به بازی ادامه داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76571" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/adeEkQH5wyTcg76AX593--I4zrH9ivpQVoRHEneIak0T2kr1E0_gaMBXrVf-IQd9IEwFBvUuTZMvzi_PABdw1Rt5ELnrK0bYmuinQ1vThmSIv1OaIV9inezmgjx408Sjg3hNdh53fxY2huMkSLy9h4a4z-eDbzoq8ZVOkuNGsbesHSi3fOgpNecLuMtLvgz2X6maIu9Wcpn41Lbcuxvp5HzTBjsbpa0VzIvwy8KPuCDE4T0g9Wr6BsR9l2LjLItClau67yPOr0axEhSnQsm5C5vBOGMIVrSaKCRlSCs26PjAsEOKE0Ni_1sd7GlmGrPTA-EYxQCDupniUyWzX4IUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
بعد از آن‌که تریلیون‌ها دلار خرج ناتو کردیم، ایتالیا و نخست‌وزیرش حتی فکرِ درگیر شدن با جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آن را هم نمی‌کنند. دهه‌هاست که ما از آن‌ها دفاع می‌کنیم، اما وقتی پای آزمون به میان می‌آید، آن‌ها برای دفاع از ما و بقیه جهان حاضر نیستند. خوب نیست!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76570" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ISKo1fenqriH0wAzMzf4j5Z5ZOg9k5779jFeHLx8vuNb7ddjZhENNFE3fX7PWvVYc4TXl-ENETcGtxNYKYKmjdqWCe5diqvfN0Fr_YSQNpSYwEj51G5UlTtcA6TMCR43xyMCSwsSg0thS778w2arShH7pXklwbV2TApevkpZQkAw139eZpEqG7b-bHcyoHZ-xqpV4NMwxq7UM3o5T81Fis9NRo_Ue4GvEa73-F4I_-Tb58awzGYqU4okZI-5MfCbZpaqm5pad78A6tpsOOUWKnCTbjjXSzEjQMQNvjNC-XprFroaXgeUlATqUDgFCbGjsibe-fPdxclI34WytyT9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ک مقام ایرانی یکشنبه شب ۳۱ خردادماه به خبرگزاری رویترز گفت مذاکرات میان ایران و آمریکا در بورگن‌اشتوک سوئیس متوقف شده، اما پایان نیافته است. این مقام جزئیات بیشتری درباره علت توقف گفت‌وگوها یا زمان از سرگیری آن ارائه نکرد.
این اظهارات در حالی مطرح می‌شود که گزارش‌های متناقضی درباره وضعیت مذاکرات منتشر شده است. پیش‌تر باراک داوید، خبرنگار آکسیوس و کانال ۱۲ اسرائیل، در شبکه اجتماعی اکس به نقل از یک دیپلمات حاضر در مذاکرات نوشت که هیئت ایرانی محل مذاکرات را ترک نکرده و گفت‌وگوها همچنان ادامه دارد. با این حال، خبرگزاری ایرنا دقایقی بعد به نقل از یک مقام هیئت مذاکره‌کننده جمهوری اسلامی گزارش داد که مقام‌های ایرانی پس از دومین دیدار با هیئت قطری، محل مذاکرات را ترک کرده‌اند.
@
VahidOOnLine
خبرگزاری ایرنا، رسانه دولت جمهوری اسلامی، گزارش داد هیات جمهوری اسلامی پس از دیدار با هیات قطری، ساختمان محل مذاکرات در سوئیس را ترک کرده است.
هم‌زمان، یک منبع نزدیک به هیات مذاکره‌کننده جمهوری اسلامی به شبکه سی‌ان‌ان گفت گفت‌وگوهای میان جمهوری اسلامی و آمریکا در سوئیس متوقف شده است، اما پایان نیافته است.
به گفته این منبع، گفت‌وگوهای غیرعلنی همچنان ادامه دارد تا طرف‌ها به میز گفت‌وگو بازگردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76569" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

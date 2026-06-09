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
<img src="https://cdn5.telesco.pe/file/OZ0kO7YCOaPhZVJM_qAYITFKP-GQ9UlfiMZcIVc_7r0_QuK1_2pIqB99mHEcVlFPCmFIXPEloULgymVVa238xJETU1OrUXKYP13cGRcqu23592m5HkSwGE7x3IMWhoRoy8TJqSSae24QcxJ2dSX6rK2-BG6ZIPZOUEf4A9edlz-ju4KUTkydvvuFEgeskiETUcQYAoloZhWz-f6lKruLI04oU6SFSQassomQRIMXDwrv5B-wTg5o16Y8WdU7HLSUqTWTxw_Wwuj9YvgVR-sdR3pvVIwuwNSnEMPtApcomS4RdFDD7gGVCwpNreLjj8WGu9aoiUSJY5YOQI5UxSsWuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 301K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 21:58:03</div>
<hr>

<div class="tg-post" id="msg-91744">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGqg9ncPNTWJ4oMY_qwa0Wvst1Rpx6V5r8hXKnSongtUS0UHju6vHr3Y47HWAMusR4mVdlGx7q7MR2QiOBFlBdg1-Y7TweRAQk1y13kdN26ib4lzebQ-NClgsiNkT_UhgoqFYONyHkrLPgRFkYJT0ZJTAVWM4Ve0EyE1_71ZV0W1_BWJjxWX8_V5xukfpUhQAhP3effV5hlRyappCO7m7qCI4zHVeoTRLkdur18y_Vooecg5RhDL2TM6_IHQkra-yoCkEpcurishRtnpRVPBMUao1BZxAW1ykjR6jqftbM_B8_89ufli9zcayF84a_ELZaBpCwe_w8u4U4yh8aRLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بیانیه مجدد اتلتیکو مادرید:  «پی‌نوشت: با استفاده از رابطه خوب با رئیس جدیدتان، بیایید ببینیم که آیا از «دزدیدن» بازیکنان از آکادمی ما دست برمی‌دارید یا نه. خیلی ممنون، رئال مادرید!»
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/91744" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91743">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
#فوری توییت اتلتیکومادرید:
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/91743" target="_blank">📅 21:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91742">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LQ5q_PEpIz77sYlQuoMAv2JybnI5DD13NNh_OgMiTxBKIxnvQ7kTY2FbpRI1jV1RMv-4yiab1UrTZHBNBmcUrBKv9YXZ1wAQEkVgYpOEP3ACYTj3N0ychl43KUtw2T1f-HauYbg-Lgk5uXng0FSEPPWHV05SWpPJ55vHAGoKP36bdrlov2FuC5dfzJljvKytv5khZlH2DqQeT82agaau-XviBXPjoJjs5JL7LiLoUKGLY4eDREW9bZgLIC_UnlYdGEPeKbHMtpX_I08HewbGx19xjlQ2qx-0Qhvnrv44GYxNlSbLcHIbJlBejfIE7XUYVYEHIKm5As84Mm0rM4iKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/91742" target="_blank">📅 21:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91741">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adQPFJsfE5nsszSW_3rmNYurMl0bihsJge5i3o0jmjYosjv70AYCjG3okgKna8tcy0MikSTGFeD5TYLalkCiiSYT3WApPsxfwwELiTdv_0BHODA_WAW_ASpbEiwohkHK-aw37x503B3nlFdCFYhiIMy6V7ZJXKS43ApQdTOZXXE5ia04cFBk-DFb0KWr2zUxP_L_QpL_ijNrmQ7VEr9I1IeGUMFjdUDtuAzpusEl518VWYAoukYjoE35uUg7pjETQh-PvJZ_k82cRsmk1QV1mUKlK1oKtObJoCaJw4ntPrchcrEo_UhRMREljv2qwkPQ7cA5phyX-EGvAi30Nc-GQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/Futball180TV/91741" target="_blank">📅 21:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91740">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0NDnAF5rOV0Z1lR_IH_fXSGlQ50nzzqDQM3DIggX6IBc1oyhPCXhy3B6ANOqAmTn2rcELb51zK6-3mpFMxSgDYP0zz96AsUSINfP3saLocEeF1myPXWlWdM9A5dnBQ7v-xJ27kbF5SsNjl9Kgifq0Vem5SY2j0gXkNLxt7rKhXcF5hzyPMMZA4fReL6fecvB_f2enavYV4Uj4282je2t4rmxl68fFlC6p-48Jlr1vP9_Rwkjcf-X0zp7Mt03FdIVPXOxk-oEZjnNwUcFrRE0hH8dognKIJRZ2bUq0bJ4lwl4KaTntWuHlyQ-YplzvZ5MPtNxOiPl6ibk3wbK92s7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
روزنامه Ser:
در بارسلونا تأیید می‌کنند که مدتی است می‌دانستند رئال مادرید این اقدام را در مورد جولیان آلوارز انجام خواهد داد و این پیشنهاد رد خواهد شد.
و معتقدند که این موضوع تأیید می‌کند فلورنتینو پرز بیشتر مشغول آن چیزی است که بارسلونا ممکن است در بازار نقل و انتقالات انجام دهد تا تمرکز بر تقویت تیم خود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/Futball180TV/91740" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91739">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/91739" target="_blank">📅 21:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91738">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!  +منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/91738" target="_blank">📅 21:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91737">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
بیانیه جدید رئال‌مادرید بعد سه هفته: با نهایت احترام اعلام می‌کنیم که قرارداد آربلوآ به عنوان سرمربی به پایان رسیده و‌ از تیم جدا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/91737" target="_blank">📅 21:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91736">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تو تاریخ‌فوتبال بین باشگاه‌های بزرگ هیچ تیمی روز اول ارائه پیشنهاد بیانیه نداده که پیشنهادم رد شد و تمام. پرز با این حرکتش هم یه ذره میخواست رئالیا رو آروم کنه هم کیر سفتی حواله بارسا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/91736" target="_blank">📅 21:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91735">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXZo6JGkfwlMVH5LI0t0GLsOU6iGfCfLdaohJ_lwDWt_4QiApD2wXbbOtKeufFWrvrUNnake6Z1oWHbgLxLCF4DH0mRvly4PwZfXiqk_hWltyP0b2UqRQYB_aHXHMR9qLTfqGRYVdAFvRJDGQYe1MM6TiqGrmhSR-O_KnG7Tle8O3FeVhiUvzM_BOOmDJegNoWviYHdAJ1J8EPfohCNPPdtbfKcDVbGI_tkw0ASXseuXcIqL-ZPz6dwyVXqTNwPzEjQq26JFUtdfPkNvX6C8_EsHDc_Y9yyhNfsvy3nqMGAYNhXhnrZvWcBc6P5HMxlE06RUKYBErNq19gKlPr57TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
لامین‌یامال: نظرت راجب مسی؟ امیدوارم اونقدری بازی کنه که نخوایم به بازنشسته شدنش فکر کنیم و‌ بابتش اشک بریزیم
وقتی به کمپ نو می‌رفتم تا مسی را بازی کند ببینم، چیزی بود که شاید مردم به درستی قدرش را نمی‌دانستند، و آن این بود که در هر بازی که می‌رفتی تا او را تماشا کنی، بازیکنی بود که باعث می‌شد از جای خود بلند شوی.
همیشه عالی است که هر بازیکنی گل‌های زیادی بزند و پاس گل‌های فراوانی بدهد، اما کاری که لئو انجام می‌داد بسیار دشوار بود، و آن این بود که در هر بازی چیزهایی به عنوان یک بازیکن منحصر به فرد ارائه می‌داد.
فکر می‌کنم مردم وقتی او بازنشسته شود این را درک خواهند کرد، و این چیزی است که آرزو دارم هرگز اتفاق نیفتد، این چیز باور نکردنی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/91735" target="_blank">📅 21:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91734">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ولی عجب کی,ری زد پرز به رئالی های که بهش رأی دادن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/Futball180TV/91734" target="_blank">📅 21:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91733">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/91733" target="_blank">📅 21:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91732">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
رسمیییییی :   اولیسه ، وتینیا ، نوس ، پدری هر کدوم با ۱۵۰میلیون یورو به رئال مادرید پیوستند
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/91732" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91731">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🇪🇸
#فووووری؛ اتلتیکومادرید اعلام کرد که فروش آلوارز در گرو پرداخت ۵۰۰ میلیون یورو از سوی باشگاه خریدار هست. در غیر اینصورت زنگ نزنید مزاحم نشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/91731" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91730">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/91730" target="_blank">📅 20:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91729">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🇺🇿
#فوووووری
؛ ماشاریپوف بازیکن استقلال بدلیل مصدومیت جام‌جهانی رو از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91729" target="_blank">📅 20:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91728">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/91728" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91727">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw3CqJb3g_VO4oIYzRHkgkjphRmHfHNo6wkZRUFmhaiOh2lDIQUzU8BnuaWvumgn1smIiSaq1bwslk6AkRYfuRn7bIVr68ReBKYDxPXir4zcJUgWle6amMtRRtDbL6th2ITmEScPFXLgxEx4XkDP4YFW6tyo6stHouUkPIdMpZ7ASeLLixjeoZOXHWFxNQXHFm9ldvWK9HbwRMfFTbZpUWu2Jbbe2vKSUoRIEtLRSH25EkbJ8DWFLA5U2Gm3jN2bGorVsG-Kx3rUxHdL81DCu5WSn2ZkNsgcZ-ukm5KuoT4Ub1xYHJBVWevXby0WENv8U3hjbuddyUXMlPpZrrgbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/91727" target="_blank">📅 20:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91726">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol29XM3-8cw09S0gOlE9YCuv3JXLQGZDpsLUtMoNAFGWJ_TlYaNM35X0AnEDeEJexQ9Zrfn7Z99Rw5PXRGjIX9SuqrhXt5tdlWo1H88BXDLUWu9gBEmTZxlzXrzTmifkyscKfzCSjAm43VpDM12-krMQldSlgM6ahdtQep0m5w4lewzr-lO2ogCEDSnQ6suMQfsVWN33tEc8R46kbXEveThLKGG9JaN0aY6rmla4EHgQu2OZwpyL8yvDkRjtv-Wp0Odeq56K3uvUzdQSiVtMtrPfoUOPXJUDADA6tBLYp-RacHO4xiSD0LHKQCao4-Mr8jhIZufWOqRcCpQLg_0XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری
؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/91726" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91725">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvZFJd-gra8HQwOEB3QipviotTLIuNDlwV0H4ko6N1zDrZCl4lT26nX27WHGbXKG9TPvMCmkXCur1rUZoVweaRy9G1j9Phitl5tdEyovapTThC8AOHQBqF51ay1C-AtV_4B3BBxc5AKX4gdtqv5aNmaduVMYZD37-jl8Xenj9IKQMf0sygL9x5FGiTvbV2cUXs0hnmPB0giCOl8_1zCpKjBzrJrdyKfZrIV-W0Z70mNjxVWPL2Yh2awjesfG7459dkMGkTC788wXMdKSgALs_dvN2E7ANd_09kyDRSqK3ME8tzjQI5HCTGS7UBJ534oFxX9MqcU73D4p5CpRmG1o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو ناتالیا اکس نیمار
چه جواهریه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91725" target="_blank">📅 20:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91724">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:  «همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن. دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/91724" target="_blank">📅 20:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91723">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5kjlJU8_fIZEEHGGa0TT-gmB_XjUgvh_n3BY4DbcTaAl8Xh5VtB_iLQ2eZ9-5TmiC33-maLFNe8mV92DXY49X3Rk1xOjZn9oYYz7wPXc0C5hGeA3-sBwnTqdeWHpbOemnU3Rj8Ns4Ik_ARzRqa6nucIAzrVsyVe5ufkRyW2JpKo-E3E2kio0VHdFIC2sm3s0EHq34rMvg4d959xzmqxFtwc0_5w0uC_r8ujjC9ZRz1I3A6zXrFFGDtKnX998tEGbSZc47aJ3-85Ge6eS19zqjNqYNfrvhbkok6_3QfTok2ZbWfNxfRT4ckM8WVoRfljA3wYhzU-8Qg8DxpkhrNz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:
«همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن.
دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91723" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91722">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgeExQTIDGEQH_g3LewxxiUssl51JXyh4tlC_l9RJAPIMsxUgmcpE-GvR6hrbgm0W2sfWoZGghAIgt_bTLPzEUQ5o0OO1BKyVc0yf1JzVSovC7HqI-avCVa6DE6E1mrO3osYQEJOMB-lilF_4aw6UkD9NkgJTyeox7y25qHhuTm2wQgPJPSuvhXrZx0aY_pC7aQrWdtEffco42JCcl89k2hgF4hmV4-j2yZ7IvHmojOv_5FZT0bBw-_d7pI_SO-_0gSt_S0Wi3xk7VCwZG0UaauZh4Z3jDkZ5lZWri2xQKWA8oed47Kbe47C1Bh7K5ggB9xwNgkmkZK93SSlc0QdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برندها با بیشترین تیم در جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91722" target="_blank">📅 20:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91721">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/itCNQ8gL7P-auI0udxrpdGTuKNGpZLBPehy4ukUg-Hcrj3TS5Y2yaOpaYs3onydo1aeFdk17fHw6M30x7d_2FcVKNte3hedSC9irjisoZRsK_t9ZAqLx9Gy_JoKckF_EW3trxKDL9CjQDDcyzJspcDrsCGwtoRLZ-h3FEJeYsvyWuLDQjJhR8sNU1JquIVi_jHQeYVurLCxpaITfL5qzZtrh9QIfIQAlyBBrX70J2DBBbUHyw5tTKEnSTag4IPyfEetypqQZtxBQePEnfyMqbfsyp0RLIA5mtd9HXhJnqTdV6rRsPuTXTMlPZQy8xPOk2b0lWENC92AObF7XH_2Lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
فرناندو پولو خبرنگار موندو:
⭐
-
برناردو سیلوا هرگز اولویت بارسلونا نبوده. برناردو خودش رو به بارسلونا لینک کرد و گفته که رویای بازی در بارسلونا را دارد.
بارسلونا سیلوا را فرصتی در بازار می‌بیند اما بدون فشار یا عجله! مدیریت دوست ندارد بازیکن از نام بارسلونا برای بهبود سایر پیشنهادها استفاده کند، اما این به آن معنا نیست که او به بارسلونا نخواهد پیوست
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/91721" target="_blank">📅 19:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91720">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7285144264.mp4?token=AJaHQPkoRSwe8wAhoupnjE3pe-W7mp2PFzp_JbpeBNwNCFGV-JQzsEkGyfksmBaTfkFX18pukKU-uilcsK3zTcApYpXeOL6CE_qu6lWD5R5b--0Ba7I_mgR0o0YIbHYo5w1r2rX9DrldfOiMo5H9S3F5UyoXN6N5lEFgJ17C5wRZiELB9lsy-4kqbDXfsBVG5YZSvlmawTXDLlRPFfG1QiSF1C4CahWQ8BsDJMpc-d-6nKDpW4nkAkbiqpcHAb8XW8fcft038fFUF__sehq7fCxv3qTMvivGNL-qFL9J9s2cCIJ51Y5wYPVk__QaqPKtju5DhGwKBMAOjEX_G_7i6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7285144264.mp4?token=AJaHQPkoRSwe8wAhoupnjE3pe-W7mp2PFzp_JbpeBNwNCFGV-JQzsEkGyfksmBaTfkFX18pukKU-uilcsK3zTcApYpXeOL6CE_qu6lWD5R5b--0Ba7I_mgR0o0YIbHYo5w1r2rX9DrldfOiMo5H9S3F5UyoXN6N5lEFgJ17C5wRZiELB9lsy-4kqbDXfsBVG5YZSvlmawTXDLlRPFfG1QiSF1C4CahWQ8BsDJMpc-d-6nKDpW4nkAkbiqpcHAb8XW8fcft038fFUF__sehq7fCxv3qTMvivGNL-qFL9J9s2cCIJ51Y5wYPVk__QaqPKtju5DhGwKBMAOjEX_G_7i6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
این سوپرگل تر و تمیز رونالدو به عنوان بهترین گل فصل لیگ عربستان انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/91720" target="_blank">📅 19:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91719">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
وزیر ورزش:
به فیفا اعلام کردم اگر تو ورزشگاه‌هایی که در جام جهانی بازی داریم پرچمی غیر از پرچم جمهوری اسلامی بیارن یا شعار علیه تیم‌ملی شریف ما بدن قطعا بازی رو متوقف میکنیم و از زمین خارج میشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/91719" target="_blank">📅 19:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91718">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNTy1o1gKSap6KOtIkDkYWpstzSgY_w_bAhZbvJWuyyLceBR3Euv0LgkNf7YXvdJOUkaa2aiwZGRfZsNBgnQNVRPAEdyQbQQ3eCXfQLuxGL35ugTdbxers2hax0IE4Z7C6KVjUYMoPjUiUTFpMhzCJjbXMJSOKNQo2NVE-55zmXjb2MSFGvdFyth2_4DToA-1w5sDko_EO0P9_0jZw-kZ0tJ74DZAu6lniJ4H4ZpVWirJQMcUVMP8APfnATnuaPLIC9VlhJ3dhk9gIzPQjSsEeZuUhvfZbm9KnWa_JNv24B8afyUVYqsouwXhTjYaXFPA6qMBvB6--ZhXtXcSJKngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم غنی شده که تو پات نداری داش دیبروینه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91718" target="_blank">📅 19:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91717">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
فوریییی
❤️
🇪🇸
یه خبرنگار نزدیک به اتلتیکو خبر زده آلمانی مدیر ورزشی اتلتیکو به دکو گفته از جذب سیلوا کنار بکشید تا ما آلوارز رو با ۱۲۰ میلیون بهتون بفروشیم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91717" target="_blank">📅 19:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91715">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PenFtPvUyRB6rlI48eTpIFURySt2LPbsz1eWQPxwBIhchx5K1pU1OclPzOSO7Vkr5_rDdcSuHXsotsD13cD_3suFAU9aPLKapLlYxmuslfhg0LqITBP4PB42E15QGach-cK7OWBsQXVAm2S_pYR-Wq9GOltvqLg_UCs8Kl6qbdPP7PPRL_uu_n-XhZpIypIn13fAyKK7BHWQJu71A4Mz228RJJ3FsKZYDPPC6VHVeKmFItGmq1lJgmikj_UDRY2eaUrQW6rKNks32vzfL-QlwLro4ACxdFKrWcxEEHx1A-D1MySuyHUjVO57UMVjzl_PNM6LJV7AGtMhr7gQiLZ5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgUxyv85noRDZEZ1hB0XZp-GB2XL9x-MBUxWu9Mp0B6Fn_-NXaSUST9cWAefj2PYqkgfdFtp-rx7FIdQZQEHgux1lAs_MEEY5PJ1dZLGMMm-Tykb4oqbk19BObbrZA5W8x54EcH16Tc3YA9CNSmiPNJ9H5d0TOVe2VFKpWv2oru5E8rTDbwYVa932WQnmqclZMXAx4-AWwRkbcthGezFiPtPdCo6tr4GpwGCqpl18reD5vf3gZ50l9k4m2jCOQuVl1nGl_SFNLUKx4A75cLKLiGKVywCm0a68O48VuUUcXRob3jgzNlCohN728RajF6SqmL7TkYrt5Fu2U9WcbMcjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😀
🏆
- ورزشگاه مونتری (Monterrey Stadium):
مکان: مونتری، ایالت نوئوو لئون
افتتاح: 2015
ظرفیت: حدود 53.500 هزار نفر
🗣
با منظره کوه‌ها پشت جایگاه‌ها، به‌ویژه کوه Cerro de la Silla، که یکی از برجسته‌ترین طراحی‌های بصری در مسابقات است، شناخته می‌شود.
🗣
استادیومی بسیار مدرن در مقایسه با سایر استادیوم‌های جام جهانی (کمتر از ۱۵ سال پیش ساخته شده).
🔺
چهار بازی در جام جهانی میزبانی خواهد کرد (۳ بازی در مرحله گروهی و یک بازی در مرحله یک شانزدهم‌نهایی).
🔹
مهم‌ترین بازی‌هایی که در این ورزشگاه برگزار خواهد شد:
🇸🇪
سوئد × تونس
🇹🇳
🇹🇳
تونس × ژاپن
🇯🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91715" target="_blank">📅 19:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91714">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حالا فکر کنید روی بازوبند مشکی حاج‌صفی اگه به فرض محال که اجازه بدن، قرار باشه بازوبند رنگین کمونی ببندن. چه شبی بشه اون شب
😂
😴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91714" target="_blank">📅 19:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91713">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQL_BFuiCXPo5sBLbXd5g-xld3stCG9OjnyK0p7fbQsbZkwdETp2zsZTkwPkkpXJLDNuvtApQoFznXK9-ukn_cw485e7HoJVfUquPH2Yab-qBJKMby_bS5sJ0VpjcWkQiTpfq93KohoNFarEpXxJGsf6Smb_5dfVW9yEmaUwxgJfx6vslIoicmQMeYxu2Pvk_hG7IxdkTGkxGz2Nq-G2shcMf3bR4XKkB9yVu7EVZ2smihPI4yjEqPdTat9TxMPEDeRiftWKd7zvnaz7L7C4mBmjRoFZZqm2dPooOAQFbOqGtqQkParE_QJVHDC-HIkPM0hDpZ5U8o53SeY7a2DFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مسابقات افتتاحیه جام جهانی:
◉ بزرگترین پیروزی در بازی افتتاحیه:
🇷🇺
روسیه ۵-۰ عربستان
🇸🇦
(۲۰۱۸)
◉ بیشترین گل زده شده در بازی افتتاحیه:
🇩🇪
آلمان ۴-۲ کاستاریکا
🇨🇷
— ۶ گل(۲۰۰۶)
◉ معروف‌ترین شگفتی افتتاحیه:
🇨🇲
کامرون ۱-۰ آرژانتین
🇦🇷
(۱۹۹۰).
◉ از جام جهانی ۲۰۰۶ به بعد، کشور میزبان به طور رسمی بازی افتتاحیه را برگزار می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91713" target="_blank">📅 19:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91712">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcYCMDuMQmimkEUKiNFWHEGzLHYc9Kvo12oKwhWfmtsIfUGFC33a3J93clY57AL2BY2KEkRorPAo9Vn5F3JzE93Rv8eQFH9yxPWEbHxtqBM-aKnKO4cQAedeS7ThqadofAJOfwH7WZxTYAg2PaAD8fJTiDsMV34RX5Ib8OYiLg5RWuYTOXFMWEHXKD8FBcZAzQFE0K3Dl6WVackEBLwyFlJs-vYat_dE2i1yWGN6QE99nH38zj3mWqZBGH0OJP4YZmlaOvK9DClq7YisJC1vzQuXk2Z7DSmzoNwywWbpd-GpVdNn5cdZER6jpk1MC03cap9hnat8U-KqZkJK1KKO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
| آیا می‌دانید؟
👀
از جام جهانی ۱۹۳۸ تا جام جهانی ۲۰۲۲، تیمی که برزیل را حذف می‌کند، در سه تیم برتر مسابقات قرار می‌گیرد.
🤯
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91712" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91711">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYzOPOvYFX1Kx9nwhcTh2l_q2Zd1H4z2LLOYyoGj8alNQeSjukbO0OoVg9UC6NmD3q0MvOvQC4WEJiOlQFTi-x_tzDq5a21mcSm2N0-mSjZ3B0CLdDHfqfZ8nZlpFmO4Ki4PcAd7n5qhyuy-e_2A-yBtGqfAOyaJa1cXXJUrQ4c7JBSJmgQcd3SXRmdncl1l2kktzijeFeD97MIZXRl2oONl-XxWHjFXzhVH3j2kxonwFxvLm4obBSR8kKaILeUpS2RHFFzCzZqfjYFRWiWmkP5ZNdNUSCKGejJMxmIeNNZ_HaibG7OTKjDkqMlZWsiDmxYc_i9yndwDaHF9bOq82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رونمایی رسمی فیفا از جایزه بهترین بازیکن زمین جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91711" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91710">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqcMINlpeOOpkby8v_O9cdCe7qaxTL_oFs4of08ExyQOkBQt2RIR9bMjHtcDd9QWVv5tP5UC24CRPUyjeoLlUOcsQpqC60cVNZXFyfcbK7l48L5c0Vj5vUmAyB-gANt7C9FGKXxkW0wst5FaVsVseTY2M0ALJ5OIhPfBl1buW_m-M6v6KB7UOdy-5Y9XfBsFbaKTE5qRCqR_rupLBp1TrHts0pI0RHUbx9NxkJvy8y3o5U0FPZ1DORKxlfSOXnECBjy6DjnYycGcRyzUSxEs2gHnhhGlJ3h4-9nY98O5zVUhLxmJL5k8CFAZCCGE2piQJQ217phh_RIbKHSA7w82mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو :
🇪🇸
🇮🇹
یوونتوس خواهان جذب براهیم دیازه اما تمرکز بازیکن روی رئال مادرید مگه اینکه نظر باشگاه دربارش عوض بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91710" target="_blank">📅 18:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91704">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJE5UmgIdCbBOXlbaRR0tuP8GCtEH_spAOMRVJavsRYy5jc1p3XMkNDnZrP9ouU-yuXr-1v-dkMNXPYyJKpd-gezQEVd3j-HfFQ6zI5Qt8JNRYiCN9m8JJa0hP-oa2TX3cIdOtftj4YI4AjPAp3PGz_ZdT2k_eIPY-F_jopoxKsRmjVXK2OZRx2fH8LiAE3XJcn4DeCVDp3Z8hPUnK4oipfu2gS-89E42BWFhjdVmTs1wPCb2Y8F-JbubNGGtPg-Fm3yXPo-LIPMTCXPI4BiM-6yC5SMK3Dw6DIWvDh31rXScJPsGw0p6glhTMAK2vAoDnKb_6NUbltwUFG8CGUd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6vuGVqjnt2GrcPyFSpF_1wIXc9ITXC-Z9ArZ8xuU_pzPn3G9rox_iJVAQ3kmqMRF-VmiE8L54BofSc-SlIpFIPeQuIjK3QHAVrBxp44lkN2q5JYFocDMiRsAK1POgDxKFoEgx95HBHPufJ6aasr-p6X-_gucocXEcV3lCMQBf8ca5oqkyyfDubJ3ZTK6GEcTZSBluNKNruPg-epyF8Ul2CvyiMohH3lMqfShdx8FOXfls2hziIhFQ7Kv8oH4_OPa6o-SIj3E7jIhPH2PIr-uYXXba5MkIKu5X0Ikk1uZq9vlm_6U39vfYCq-KK2CZMi2veN8nEZfyZRZGXWWNc4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/An_2pUkQeRblHAyI5adBc9ABOZEssIbt8pzbU4huOdyz-tYMLLXO2qIXUdan7KfDHdQjCVhoOYg3KoRrKno91zqpN315x0db4H7cr2GGnx97FSofxocFEabdzwIo_6___kPbNXOVeoi-OAswMxPNxaOe6DdQ-DbbLqXw7_s03UgC4MBQxYGVFFSDKplWslpmeKky4pKu8TV1mr0DBg4bSV3oFnw7iwi1QRfIeGQR4Mj3yDWehhmIV3gv5vSJQ7zEZ6tnz4WqAcDTOHAGpZj69hhCllR2nOObRKyc0-ekXqDts0L090UV9CFgq2EIQM2b4J1Tu8LOc4rbxaCRJM814g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این دختره توی اونلی فنز فیلمای لختیشو میذاره بعد یه پسر برای قدردانی و تشکر از اینکه دختره باعث شده خود ارضاییش لذت بخش باشه یه BMW آخرین مدل براش خریده!
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/91704" target="_blank">📅 18:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91703">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69522e0ec.mp4?token=icKzd1mSdipLtWzrmvGqQ-5c0cjGskuj5qCbdM5wofkDpdo0oaO72vHjHNTOSdZLGok9pHL0Qq_Vgp47pvX0KWDR4F_Pel4nPDqm0y6XzJYnDqevSwanGL9K867P9yOaZUYbaCtpiFo7xmx976Ij-bldCCsI_Vsvyz9YbxwbkF8X4wbYsfxLhgcPobzIyeMqOnI9RhbPPDzEwJpVmiqBnkaZp_sOkB1_6wb_TMjjG4oSRe8rfNlZeBORHCVFvpstYa1VzEnSNEADaMMCLJ3zmaaVuaZ6fJeJXozOwIxOtvyqeOAbrJmNjzv2G0wrFmPQSvXrTbEztFR6LsbDjI1zoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69522e0ec.mp4?token=icKzd1mSdipLtWzrmvGqQ-5c0cjGskuj5qCbdM5wofkDpdo0oaO72vHjHNTOSdZLGok9pHL0Qq_Vgp47pvX0KWDR4F_Pel4nPDqm0y6XzJYnDqevSwanGL9K867P9yOaZUYbaCtpiFo7xmx976Ij-bldCCsI_Vsvyz9YbxwbkF8X4wbYsfxLhgcPobzIyeMqOnI9RhbPPDzEwJpVmiqBnkaZp_sOkB1_6wb_TMjjG4oSRe8rfNlZeBORHCVFvpstYa1VzEnSNEADaMMCLJ3zmaaVuaZ6fJeJXozOwIxOtvyqeOAbrJmNjzv2G0wrFmPQSvXrTbEztFR6LsbDjI1zoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
۸ سال گذر زمان و تفاوت از زمین‌تا آسمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91703" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91702">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWcO_6XhbNfbVokkXUP9dnsXnlMDC4WRP72h7uDJHvpshUsqGkikTHKxbGJe_aOmNWIivg-BBzXsS6kxUYAdwO4wloPFlalghgIkPQt-HbMLcmY8nY4gNkvJqZbapJ4c2qulEd-K-q7zJhrpbmULwyKwAzYU6tHEJ3O4n1rxS_N9U9sxnbzzxJvxtZ5zgUvNTHFm9-qLLloTQOsP0sg1lspxGj9Z0AVY1llmM_kJ8efnP56_bupNaFbtu3TkSNEUJ3QKHb8IHiJzsCSHF4Ih4FBNkFj0PnIxreo6xfOgpBFPC-VPox3DrXf1BxHyyPSn-fhAxY3JwKlWXJCSU8vVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوریییی
از رومانو:
⚪️
🔵
نیکو پاز ترجیح میده به جای اینکه الان به رئال برگرده یک فصل دیگه هم در کومو بمونه!
تصمیم نهایی با ژوزه مورینیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91702" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91701">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGhMWR27ExtypUUi_XyIswpDlFHP4hkvKd9biscXAErr6EkqEKgG9ECvsq5G5s5QKDOrcgDxDsDBCsl8J5rocawOadh0KjB6Ew0Sdw7-65VjAPFOTyCqxDXWJGMX2rvbGV96gJBdHCcHri0vM6ulpb7uGJvs88ir4h0SofVTh1XZUwK-jmnHAXysDYHNk0LaPPxDMA9z6zfoNsoztyHVTYZIW4RRVZkGWtsy8Lah3Ezj992i_H5bajzMP1oGbKquvNibcRi6pTGpzbcEGmS3Dp5wxXmCnsoQGlGFwY2cJtcxNFDcPyt1rEuiARK3M_hwvBhgaEB-DyleKaXkTqODcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توتواسپورت:
پاریسن ژرمن طی چند روز گذشته افتاده دنبال جذب لامین یامال و میخواد شانس خودش رو برای جذب وینگر بارسا امتحان کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91701" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91700">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUhBBKXcXNK-903q1eluScstDSuSaNB9CyQV5jaBjU4oE7z0mo6dS3sqV-nwc46k8BVJb2R_4g5tFo4SzENkNV-rA3GPsUoVrfh6vgBoArmeZiaMsXOqhxwJfhMFQJBpHYApEuxFMWtyErMBrv-cWSxe1i0ejWw6sbXHxA5PhYFTfezb4GJg1ZzgvWuda_ojWeeF3UBToMjshIqMwn-AD7fXPwvU7ssXj91GOBXpF4rfxW9DVfRtpFp2EPdWc9y8Q8wbpfiXYb5mSgtsrJYPrOe1n1DTyMQR_RslDFTtrAhBmohfX8tdn7mK39dbi8MWdwQeSjEd9UbVyD91TEhyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
تیم‌ملی ژاپن کمپ تمرینی خودشو که داخل مکزیک بود بخاطر شرایط بد و‌ امکانات ضعیف به آمریکا تغییر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91700" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91699">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fba6ae20.mp4?token=gQye3WSxSWCTnzNOU4VTCwh-OZRnw3Box0VsOOcclFPRAo8SpBEYcNQIL9mKMsP3HK5LpEa_KZKuW6fLQ2mgLq-m99anv4MpS902r5QqnqF-ZD98mKLu8MvY0rrcRCsSSyX7wYe-IbAUGU1qlf2YA3AYhQQzVyhuiI6vWpZf7aBx_9zcowAyxiCKbSEAoDGgWegOcHPQNSWbdXQezk3xd8_gmOSX4f-oWfi7WxEob3SeOsNiDWwSq9xw21zAE4WXU4RVeYJGeNk442DhGmst8Tc7JrfGFAj_dn-r6TRMbJeWMGae7_cs5XSVgETBQv7KiaAZFHyO1BNWZBkwf-Hukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fba6ae20.mp4?token=gQye3WSxSWCTnzNOU4VTCwh-OZRnw3Box0VsOOcclFPRAo8SpBEYcNQIL9mKMsP3HK5LpEa_KZKuW6fLQ2mgLq-m99anv4MpS902r5QqnqF-ZD98mKLu8MvY0rrcRCsSSyX7wYe-IbAUGU1qlf2YA3AYhQQzVyhuiI6vWpZf7aBx_9zcowAyxiCKbSEAoDGgWegOcHPQNSWbdXQezk3xd8_gmOSX4f-oWfi7WxEob3SeOsNiDWwSq9xw21zAE4WXU4RVeYJGeNk442DhGmst8Tc7JrfGFAj_dn-r6TRMbJeWMGae7_cs5XSVgETBQv7KiaAZFHyO1BNWZBkwf-Hukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو تیم ملی نروژ برای جام جهانی به سبک وایکینگ‌ها
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91699" target="_blank">📅 17:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91697">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvBVH7OgosdUF6QoqRIrrl-D7kAHxn2jd6Cmx8jS0rYtwMa3r8mGj0Y5PwQ5BXNXxXPKFs2MwTtmD0VnK2faDsiR6y5DUfVWO3RDasf2T3AgTD6rGpVv_OHGWZEEdRVIGwrqu5T3cYqeoSgODINj0WQoHgmXL_vFXN34Jn-d4kMlXFX9os2nYJrcyhHlJUgW0TSrIhnwGg1OkhZB--l3Ic6wjrHv3C_JEpxg_VNEJV8BGTJRxao7_JhejBVczhq86iES2IsfkjCfDv0sIQ3T_AfBWNPiZFFWL3s9sbNxLKIbgsvNgBOf9vumQxEpFbU4GpcvKZJgVIa1-5GkJ11l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AgVFP4fqujq_epa72sWQt0IowgOs_c7uguqdpTsw2o9quAv3RrM-aKdj6dsrPqJfQTG58qPj9eXoHoRY_9s2l2zAq8edo212YKqmIgpdvj3R0ux8TgDtDAhAO_ZVce_OlQ9OukxItaqMR64QNFXcFZA_0wEw6RWhRKUgH2y7JUAAoH1uPWW3PvZWv7nNGWskC0401PAfA-EAtLGTU7W4nU9hxDU_8Zi_9JwvNJSs71XFNTpQNoW2-AQEDUJH_6CdJ_6iOV3QNca3vpC6qI4JZkafNiBfUCZxHAJiqJ6cwVX_KAuI12ByjHhFvRXRJ2lGz2sYfOWU6namJ39dhKoWlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Newcastle
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91697" target="_blank">📅 17:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91696">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8Vdt3J2M6ATTCGcNDN84iUKqSj6r4VOVO_IO5nf4pa6AOtbZ6WjlanTWEctALrAg_QNbJzNWmuPTftgYeL5igxE3RXJAjJtbfZOtRJea3AOjP9Et22DwCc1b3bx2l-4_gQDcFNBMZZHEzEBZmVnHPiClnzngrl6F1cEGQf9SIgj8ZBNynhL9FVVOXHfDqhPURX-11zltSvxhvZ1tNtRfUv3TMmE0Xgm_F-RlnN_ZpDsZD0RdksrWSEF7FPaJhzmk1-6wOq34B9wW3ICN5BxMb-p42ASJgoMCjeD4gkcCUsTRd65fPKDdRMm-rGeJWqy6vVL1AX_HlrYtD5OH8VJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گلوبو: نیمار ممکن است مقابل مراکش به میدان برود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91696" target="_blank">📅 17:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91695">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrN-VdvS-XDHGSdFvbp32o4LbgK2n4XwNtZGOgU4nAyR_DhmZAq-IZ-vaYhAy0RrCUVuao9m1UUTfoX2aQhn76aaG7aPd3Fh2ppxUmIbl4S2pghvKZmHFZIUGve69jq7xB6S2thuzr83o75ioE_IFcoVV2xd-1xNf1HG1AJRuMn_Xonuz1nKAqqIvrBCldkuP9wH03X84X_ty7_MLAhVKx-3yGhOdCmrv0xz85C78eYJYMvGqb1-OHDdUzLcovdyWq-81BWaoY-oeu32rsyAScyu_Oqr126_YbZEJQG9VN-Jkx4rtaoh2kJg5qaeDpUfrA23dpjK71jeWn8tzSgxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: منچستریونایتد درحال مذاکره فشرده با وستهام برای جذب متئوس فرناندز هست. رقم درخواست وستهام ۸۵ میلیون یورو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91695" target="_blank">📅 17:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91694">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VqM0i662xW1FKRfKGyzOj-E67uKWOZM1H-w81DPQaH64PApf1EngPXpLB3X_mtGklLvycXFwCnbhjje3Ql5JXEVh847TvroS9NxovOCvRdNG9uMavKuQh55YIqVCl1UTJoPXi7HvUF4rbe98_59uU9lYzxkD_1odUJVjQO5sowwAAYb3XiJebpKSu_JFn724Xgbzq37PJnpEjWnA-YkfRAm5Z9LYeYUP1_MPQ0njmAPLovU865Sk1fOjLf_zeX_dMDeofrIDqIWrS5S-hyXF1tEskYvkaQVZhhsIcR251BG8TQtZlBen8a95o3CKIjwQZxv1-TgmKyXGd8_c1EJKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
⚪️
رومانو:
براهیم دیاز میخواهد در رئال مادرید بماند و برای جایگاهش سخت بجنگد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91694" target="_blank">📅 17:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91692">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTTEpr19roIJngD-vaP7V4m4CWhHvaapMAg7DPKtSzmEDgTpFW8f6mXxFyKzEdFwq3gz5OmPmJkltmBJWAGiRZ_ZcwyC0r7ykGF-DiJvsQmA0nU98hanBhfl4pIAgJhLky9VY8DSxKkQfsTOH6jW0h_2bgOtxYDBmqi5KbJOYcm1rGuI5wfyXftOeSoVjJX0b_wAD0B2r9ghBHpb8QcrpwjNiC0ZwvdtM3LlCxPHP-mGTbxKAZshWcJ4YltKcCO1UaezEYqKMffJMUi1uG_qVFuDUvG8yAV6HILd9Na8S7L9-8MIOnw43sfmby6l6N9piq1AWjWittjfFdQzBupg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgV5CQ4dAoilV2W2I-goxi6Kd3Tv16NANO076bZ-iwxztTPyAQz8z8IQmmE6UEUrQaGNJDlwWAQpFM0kMfrirzdmfv1Uxktb7wjkZT5pwGHNDunsXkuz6t07_y3zP1GGxBS5Ls_vChZLeRW1h2oGsQGVrFCqhgfQOyurh0mobbiAvrmbJaIkMisDOTXzGwIWJqKqdBeOrmIleNFhozbVJrd5ux95PiSUsRcr9-hq9L-bssFweZ920j6fb0zyQLauJ66HZ3p4dLo1bJamZv_SLxlcwJWshonLnbSOvcXZ0Qr-9abMB2L9PDl0GozvLpRls_uUIfoI2e7UaT6BKgh2pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاینات پزشکی رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91692" target="_blank">📅 17:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91691">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
#
فوری
؛ پس از اعتراضات اخیر دانش‌آموزان، تاثیر معدل سال یازدهم در کنکور مثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91691" target="_blank">📅 16:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91690">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f1cc690c.mp4?token=tKPTJHPFfsmtTv2fE2A_NGYGWS-4y1JgotNHwwMsFHlbzEj1wn4mkM2p1YGhstne3fa8D9i0MEnEXQabedBK9ZwLTyqX93rxlLAmVn3EGoxCefTuV-1hQS6VQdyfrX0aLJgwfUvegQLCuD83TuVisNVuSWy8OfIS3fD2oqXukr12aY7MPZ1A6hzGhAUai3cTks4mmBRnPRwABddbA0ZPHd9WcVdrzPKV0sS08PDEbVcCVbwJZ7yOYF64fYi0nTsotfTQtBO5uhHr6rIbWPFzmxczvAZB2uZKowWmpiU77kxwpSrQCAJ808UJ3O7pP1uQ5wsONijOjyTbbLaqK9n1zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f1cc690c.mp4?token=tKPTJHPFfsmtTv2fE2A_NGYGWS-4y1JgotNHwwMsFHlbzEj1wn4mkM2p1YGhstne3fa8D9i0MEnEXQabedBK9ZwLTyqX93rxlLAmVn3EGoxCefTuV-1hQS6VQdyfrX0aLJgwfUvegQLCuD83TuVisNVuSWy8OfIS3fD2oqXukr12aY7MPZ1A6hzGhAUai3cTks4mmBRnPRwABddbA0ZPHd9WcVdrzPKV0sS08PDEbVcCVbwJZ7yOYF64fYi0nTsotfTQtBO5uhHr6rIbWPFzmxczvAZB2uZKowWmpiU77kxwpSrQCAJ808UJ3O7pP1uQ5wsONijOjyTbbLaqK9n1zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیروز وسط‌تمرین یوگا‌ کف تهرون و صدای پدافند؛ چه ترکیب متناقض و عجیبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91690" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91689">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871f3caa0a.mp4?token=c0oa4eQDsnmCBiu2qvGwpGwDHBqgD0MjfPzso4fpEXlcFGA9vC-t-zzXySsr81SzEIY5bmPHGYp2jExf8twxi1kh0gYxjnt6bdXW-t5WqLkO9rSBLrBEYMkd7t1epMVgG8US3ozjMBUrnsWKptDoU4SUWjSG6fN1y3orv0OkRtHtV8Amo45uXzVHlITIh7sphZ9_aFs-AntJFthCOtsYnXbaPJta6QoatTCIGMJDdiShKN3GSBmrX6LULQkKhQeaPG3NTzWU0M2WoH-jWUUNBcdp-_KTXqxhBlnrF3EArkpY7WW17miOFLdkwpAeNH8j48YzQvnZxhIyAmT2dbEIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871f3caa0a.mp4?token=c0oa4eQDsnmCBiu2qvGwpGwDHBqgD0MjfPzso4fpEXlcFGA9vC-t-zzXySsr81SzEIY5bmPHGYp2jExf8twxi1kh0gYxjnt6bdXW-t5WqLkO9rSBLrBEYMkd7t1epMVgG8US3ozjMBUrnsWKptDoU4SUWjSG6fN1y3orv0OkRtHtV8Amo45uXzVHlITIh7sphZ9_aFs-AntJFthCOtsYnXbaPJta6QoatTCIGMJDdiShKN3GSBmrX6LULQkKhQeaPG3NTzWU0M2WoH-jWUUNBcdp-_KTXqxhBlnrF3EArkpY7WW17miOFLdkwpAeNH8j48YzQvnZxhIyAmT2dbEIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ازبکستان روی سکوهای استادیوم یه‌ پسره اومد اینجوری از زیدش خاستگاری کرد که دختره کاسه کوزشو شکوند و جواب رد داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91689" target="_blank">📅 16:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91688">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9aa48bcb.mp4?token=XOhH28LXskNzg1nnyTUslpV1_Qzgu6l2XSV2n_LPp3nwUPqRunqx3xmmYTQV7FtTmkQ2Jj6xplO04AbiBCM0_Fiq-hk5m1yPKTrXYQcvHVXT7o-TuppNWkXfOVjsrJPmZ9yoefZYzwQMZiaKJC35u3J0rI39fHPamI5R2UA_NOVQtu6dERY5OcHyhe19r_0IdgfKvfQUrU8Z6VIMfgB5EsY7q2q2yA9uRBFNIuO4o0LbH-Ww4BE60k5ryKUKnFlFJCbYODH4BBB0VRB9TOvZyVczLTXvUWnNrKRfsVZevsteKZ1igH7uUxdcpgkc1l3Quvx8S0fRUJG2-qoft6k1dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9aa48bcb.mp4?token=XOhH28LXskNzg1nnyTUslpV1_Qzgu6l2XSV2n_LPp3nwUPqRunqx3xmmYTQV7FtTmkQ2Jj6xplO04AbiBCM0_Fiq-hk5m1yPKTrXYQcvHVXT7o-TuppNWkXfOVjsrJPmZ9yoefZYzwQMZiaKJC35u3J0rI39fHPamI5R2UA_NOVQtu6dERY5OcHyhe19r_0IdgfKvfQUrU8Z6VIMfgB5EsY7q2q2yA9uRBFNIuO4o0LbH-Ww4BE60k5ryKUKnFlFJCbYODH4BBB0VRB9TOvZyVczLTXvUWnNrKRfsVZevsteKZ1igH7uUxdcpgkc1l3Quvx8S0fRUJG2-qoft6k1dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکم رونالدینیو افسانه ای ببینیم
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91688" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91687">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813a70ddec.mp4?token=LE1rw-0Rz4EdBgPfvi5mjgbKLzePJm1GGDX4Q4E5HffTShEPN22kx5sdzwqOdC2_pFITYmY1T09ziBBA45tgTKVGb9vMcPqPj5Brt1-KBLvsivN68udzVhDLMZw9z_OifL1moa_0QsoqRv-GE4LQfiupVYYFAxjLcX0UY0_bkLBkmYGKSoyTJuFt39WfUNazFcjpufXOoXrgcbH6oyxv7Vj2b8XBXOnjBi7b6166GZhIYshWReBNvw1d_ECoOFXLzmcLlz4J0lQYeWino4tExnZmaczAsoJznPfNBCyMABw39BdXIrcUw3dej-sN_FHXXJaA8LcdJYWxrXitpBjyuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813a70ddec.mp4?token=LE1rw-0Rz4EdBgPfvi5mjgbKLzePJm1GGDX4Q4E5HffTShEPN22kx5sdzwqOdC2_pFITYmY1T09ziBBA45tgTKVGb9vMcPqPj5Brt1-KBLvsivN68udzVhDLMZw9z_OifL1moa_0QsoqRv-GE4LQfiupVYYFAxjLcX0UY0_bkLBkmYGKSoyTJuFt39WfUNazFcjpufXOoXrgcbH6oyxv7Vj2b8XBXOnjBi7b6166GZhIYshWReBNvw1d_ECoOFXLzmcLlz4J0lQYeWino4tExnZmaczAsoJznPfNBCyMABw39BdXIrcUw3dej-sN_FHXXJaA8LcdJYWxrXitpBjyuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
الهه منصوریان بعد زد و خورد شدید و فدراسیون ووشو: من در برابر بی عدالتی سکوت نخواهم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91687" target="_blank">📅 16:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91686">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=j7YLHWyzPl0MN45pCmEwOXHa9vBawr5dweme1bfc2VwNbvmV6CgXBwtu1GEJMkOLqxEDkUvjExrNeZDJMRF9EQ48NzTx-wZhA1LatKHhdXzY4EYoKkTQBp2H0IIPltZFY7DTdpT1YI-zmXiu-zfge6CZI6IQ18JdhAlkiqyCYbO9zVziApeax9y9yKxdNA4lFC6jLPOjOI-vkprpf7rBQO5dTTKBSVQpHSAz4xRAxIwdf7VjJ0wXxzYMyy5Heq4uMSPhDLRnXKPpLyvbhWa2gWp-ASqJXSUrijjFADmoo-XBhBdF0k3HNDdhY-FOizIVvXystR1tknoWKS3z3DsODw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=j7YLHWyzPl0MN45pCmEwOXHa9vBawr5dweme1bfc2VwNbvmV6CgXBwtu1GEJMkOLqxEDkUvjExrNeZDJMRF9EQ48NzTx-wZhA1LatKHhdXzY4EYoKkTQBp2H0IIPltZFY7DTdpT1YI-zmXiu-zfge6CZI6IQ18JdhAlkiqyCYbO9zVziApeax9y9yKxdNA4lFC6jLPOjOI-vkprpf7rBQO5dTTKBSVQpHSAz4xRAxIwdf7VjJ0wXxzYMyy5Heq4uMSPhDLRnXKPpLyvbhWa2gWp-ASqJXSUrijjFADmoo-XBhBdF0k3HNDdhY-FOizIVvXystR1tknoWKS3z3DsODw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بازیکنای برزیل یه دروازه خالی گل میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91686" target="_blank">📅 15:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91685">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfdTEEQ1z0SxFlJZu6_fus4wzp7ikHpvu_QckU4NhECW8djBcxfk-8RoC1no0_M3HEaCxGoJ0Q2Wf8ss-53jXh-jCwMKLdRzcCTtLkkyAWhD7tUsQGnLnMi82iHZd4KbA-_gz9khfw2yOL3i5qb_jj0nfMggl5TGRhSdMNKVMGCHkv1umJNsVhvSsvPvUSkkvqdlPEL8vGAT4oQn7BNQXjlzFOaQicNnRVdMtg55zyWMUG6GpadEd28jsqXv_DVwDryVQSlHVGCtB06MdacjystJVZ8F4i_iLK5gf9zFucOpJxHIAFLQgaaUv2ewVZSMTDr_Ch-UHNhqM22sV4L5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو وارد مادرید شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91685" target="_blank">📅 15:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91684">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd169632cc.mp4?token=Z6iVhDlumtaKWb6TiTjs7fgQaeDaNBN3kWvTVxWodlWU3GtxCOzP2Ltg-uUmNxFodcoK5Pmjkv-U7RYW2JVcSvMJa1TylVg_bP8QCf9ViKtdpOBNZdU6OJNUIASMPmjXgA3ESZxClOEZT7fbPLcEx85WEM54XJFl7XDGyhlZxc1AvKXMlVT97VuwyN5SQsWE_2err-WxXzgJPwKD4PhCGK8skqyFeQ4KB15AoJwt03tIPd9tRgkTblfGKLNZ1bIg-4FgDx6UF6wNYOfyFT6RzVvN2HMzj_J_2wdMxgiQXnkUw_JyAhDhxAlNY5WwQs8WaoqDFV6SHxi0kvuvZkhQRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd169632cc.mp4?token=Z6iVhDlumtaKWb6TiTjs7fgQaeDaNBN3kWvTVxWodlWU3GtxCOzP2Ltg-uUmNxFodcoK5Pmjkv-U7RYW2JVcSvMJa1TylVg_bP8QCf9ViKtdpOBNZdU6OJNUIASMPmjXgA3ESZxClOEZT7fbPLcEx85WEM54XJFl7XDGyhlZxc1AvKXMlVT97VuwyN5SQsWE_2err-WxXzgJPwKD4PhCGK8skqyFeQ4KB15AoJwt03tIPd9tRgkTblfGKLNZ1bIg-4FgDx6UF6wNYOfyFT6RzVvN2HMzj_J_2wdMxgiQXnkUw_JyAhDhxAlNY5WwQs8WaoqDFV6SHxi0kvuvZkhQRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی اینو با این افکت صدا توی تیک تاک آپلود کرده:
صبح بخیر عوضی فوق العاده؛چه حسی داره به عنوان خفن ترین
مادرجنده
دنیا بیدار بشی؟
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91684" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91683">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0ie8OM9GQ23vUsxxU73IqEJyC_vev0c89Bu0KufxutDh8rj4UwRw55Z6A2yxfWnGCN2rV64CEgdP8Aye-TR3hC6T1vbYHYuoJ48HNYd2EXYMJs-5iW3KF6TAiZ1SNXrYl_cEIDW3Zco5x30nJZe-clAnrh5X8PExN7Uikgfq3IUUZ8Trg2oL_BBSI-YGVmmoNxH5npx8bBKCXAfhK_plA6VA8GAxR_IYjLHJQvE6drfkgv4FVEb9HrNS3SVadZCNpt2bbBjSudUkbra_giBVIlyy9a65I4-tqI-uMgcWGFn4ruVUO-_anZ_KtUawGAI58_GnVrmHb9zzshVtIaBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
خوزه آلوارز خیلی نزدیک به لاپورتا:
🔻
بارسلونا همچنان روند جذب آلوارز رو دنبال‌ می‌کنه. ۱۲۰ میلیون دلار حداکثر پیشنهاد بارسلونا برای آلوارز خواهد بود. مذاکرات در روزهای آینده انجام خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/91683" target="_blank">📅 15:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91682">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAyMpZnL_zpYfjlJ6A_7SnSJBLrTOX67u1IuhBwJmHeTo20HIK1qmbQxmZSN5t_bI5Yt3rGDm8loNWwiCSKAognq1hzJqTHjAImrJ2vrO855kXHPG9znCAs-HoVEIULvbqGyC5GlV7L2r_rYxluPpOKMv-Gj11woXvkoOB6bPLWX9fwm4Ipg4iYn6vS6CQbO7lBxgBJUjCMrOWgfqkhStSate1_0Wh4D_NdV01Tzg21ZA_GR8p7YqW6HGr2aQGn92SFlK99GxiCg_orNQA2nLM4VyG4Gg6VHE18yhTerSIOen1UPXbxMHtlG5II62Bw92KcAX9xqLxKQogb6x_CyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
خدای جام جهانی؛ زاگالو با ۴قهرمانی جهان با برزیل
🥇
۱۹۵۸(به عنوان بازیکن قهرمان)
🥇
۱۹۶۲(به عنوان بازیکن قهرمان)
🥇
۱۹۷۰(به عنوان سرمربی قهرمان)
🥇
۱۹۹۴(به عنوان مربی و مدیر فنی قهرمان)
🥈
۱۹۹۸(به عنوان سرمربی نایب قهرمان)
🏆
اوبه عنوان بازیکن، سرمربی،مربی، مدیر فنی قهرمان جام جهانی شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91682" target="_blank">📅 15:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91681">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15a705f7b.mp4?token=QZgxDYbP-ZkipTiOm2rOnoSlFtzoEAkrzPrnjXEA6BjbMqdfUlcDHFALQlK4AjW_VE71xhdKmpZJwVkeGYOnt65WqjeUpEtkhTTmJzUiypxxxS_riuAWAsrjX6r4l3LFCUINbBGKyDaFRXZqjhxLFkFoFhzJVDEGQcic2jI1tLAvI8PUfC_FIPm7rYT6OUZ6AZ6_iFbAT6G3RdpCqZj7g4IFJLON1HmXwg1p4_0S2EaovyyUDjLhhP-5WuU9xkOXL0X0Ebvu4zo8rX8I2kz_olkV4LwSKTPu8Ewyh4l2fjKSYLi6PK-ZRstHjMXIOlraCafuIHFmSYCKfP3QjMVYRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15a705f7b.mp4?token=QZgxDYbP-ZkipTiOm2rOnoSlFtzoEAkrzPrnjXEA6BjbMqdfUlcDHFALQlK4AjW_VE71xhdKmpZJwVkeGYOnt65WqjeUpEtkhTTmJzUiypxxxS_riuAWAsrjX6r4l3LFCUINbBGKyDaFRXZqjhxLFkFoFhzJVDEGQcic2jI1tLAvI8PUfC_FIPm7rYT6OUZ6AZ6_iFbAT6G3RdpCqZj7g4IFJLON1HmXwg1p4_0S2EaovyyUDjLhhP-5WuU9xkOXL0X0Ebvu4zo8rX8I2kz_olkV4LwSKTPu8Ewyh4l2fjKSYLi6PK-ZRstHjMXIOlraCafuIHFmSYCKfP3QjMVYRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیکی‌ها این ویدیو رو‌ از اعضای تیم قلعه‌نویی منتشر کردن و‌ نوشتن که تمرینات فوق پیشرفته ایران در اطراف استخر برگزار میشه و اینقدر امکانات اونجا درخشانه که رو دست نداره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91681" target="_blank">📅 15:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91680">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39f457cd6.mp4?token=fKtwALGzyZwCiFHXl9BIxuHF8yMt_CxpKTyiBFuoQbAlDNeXELo0bRjz8ApaKCdZj30H_Gh_6SvigqRH164qfrT5jAXTK6nn4SYx7D0ekXgRjvUy0ceXxZnBl2_qBzvmq97A6arPTSQkicVEZSD8BpxZj_EmU2tY9reUc_UbKRMenaMCjhABmU9mV2VE1aVa_nlFBQ_nLbLjbZkhrekyW_b_FXNJLf3pSYj_Q-XWAva-LqS1qFV-b1f5m9GTuLo50dZTnHgaZqQIALfRppu9pZY3tgFZkovQTx8izZ19tCYm9Mlm5AMjvu4lyqR-qVJ3YijeAy55yRTjq4L9lSYBBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39f457cd6.mp4?token=fKtwALGzyZwCiFHXl9BIxuHF8yMt_CxpKTyiBFuoQbAlDNeXELo0bRjz8ApaKCdZj30H_Gh_6SvigqRH164qfrT5jAXTK6nn4SYx7D0ekXgRjvUy0ceXxZnBl2_qBzvmq97A6arPTSQkicVEZSD8BpxZj_EmU2tY9reUc_UbKRMenaMCjhABmU9mV2VE1aVa_nlFBQ_nLbLjbZkhrekyW_b_FXNJLf3pSYj_Q-XWAva-LqS1qFV-b1f5m9GTuLo50dZTnHgaZqQIALfRppu9pZY3tgFZkovQTx8izZ19tCYm9Mlm5AMjvu4lyqR-qVJ3YijeAy55yRTjq4L9lSYBBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ دیشب رفته بوده فینال NBA ببینه که باز انگار تو حالت چرت زدن سوژه شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91680" target="_blank">📅 15:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91679">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZkpkUNNsyI8Ue9EE7zTR4X2ZuIXMT35QirFIdXEhMflgNS6imHlg_3Q_sRdwdxNq2j5dQfEk4eouWZBXA_MREZeF-3THNCwxX5jw6uQTiQK_Rv6eHK25-djcFcdjsMgKZyfJ_FDQ5WSrgsajTPOYSgMZ0_OYQgPTSk2R4UDfCVCtyeM2mqiI5npul8gzFK50AiXcNMveORLeakU602KpsJKa4KuX38J1lVHbgwckw9ouGJOrgyoRFgx6vKXUgD9cdI5LbqbaUIbHFhYYWKv0rvvBiHR6ehSyx-qpRKpcZ1W5pY3nsRKV3rdOC4opLY2i5jRQNa_cS8hQtIfoTORlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دوست دختر رودریگو دی‌پائول:
«بعد از جشن قهرمانی آرژانتین در جام جهانی، رودریگو مست به خانه آمد. من مجبور شدم مثل یک بچه از او مراقبت کنم چون نمی‌توانست جشن گرفتن را متوقف کند. به او گفتم که دوستش دارم تا آرام شود. سپس او پاسخ داد: «من هم تو را دوست دارم مسی.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91679" target="_blank">📅 14:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91678">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏆
اینفانتینو رئیس فیفا درحال خط‌کشی استادیوم نیوجرسی آمریکا در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91678" target="_blank">📅 14:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91677">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rbf-g6wucchLW3Y89XDYZEkr00CG3Cuie2Tn9jFsb1QOqB0UXT6b1Si1CJpbsUgfbds6prJ810eW-H2bui6_M5T-MamiEjkGjfcggNUMzitK6WhMlPXoXqw_9s6HCR84whmD4ggzVFChwxyZiHB5_jOFgWErdurNGTUTTLD9c-I_LGA__xj3xYs28vAnWHyNzXjgVwxpH7mI1fUxgDrHTfgpvASXHX7son_Xji04lF9sxgy7KBqsTASAuggwllsjrnAQ4HkF9apb_B2fqq41E7zXDogHcDs18V-vPnQolagDivgqWLL93ti_jA_5utZKmbq6c-y6dpgJt5n-Z0-xlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر نیمار به همراه بچه‌هاش یه ویلای خیلی لوکس و خفن تو آمریکا اجاره کردن که تو این یه ماه کنار نیمار باشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91677" target="_blank">📅 14:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91676">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📰
⚪️
اسکای اسپورت: هدف رئال مادرید اکنون قرارداد با ریکاردو کالافیوری است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91676" target="_blank">📅 14:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91675">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJJkSn36yijw7Yg9TBTWATdWGSxh7GI90jdVmgU7l-KdskFZ5GB40iqUMQTOU3JokGPPUDWRabXqmgs2a6m_-TpbIUL1Ix9tN5Gzs8pzzGDew5mqM7VgZ9Wf_9werJXFC_17bYavOFdehQMttVB1KQd4YZk95MgKAFpek1dbOZnjT_KHzxc0pDqpWSjN4ozi3-lFBQ--GBac7Xv414f_SRBOILVbHrjK9gXiUJulEOQD8sbPyfGZor1ep9eT7YVb3NOB-lnjFheJKU4J1UUSHByEQ2GQr_naGTrNkDWygnybL9izvISW86BRMwT-w-R_ng-Nw05yWqKpmHq7ENhPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
⚪️
اسکای اسپورت:
هدف رئال مادرید اکنون قرارداد با ریکاردو کالافیوری است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91675" target="_blank">📅 14:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91671">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qx-ZOtRTbUydYNYIJjPvJpJjI4DNWkZ7jpACOy7Ncz1fwrGnHmZ1X78l2uiBO6hHi1fWd5zeR-RoC7I62dxbUXmMkuUBFj-Ydc0qTwXCwL9znp5WBy9boPRuzvmDFxwzMQtOtHdsgTYMwlNDkx0k6gS6zVf3HExIyzdBpFf3Ji064ES2C7z2ZO-G_BS-6MyNnUxegXVWqV8tMXfEA3qv7y5VWqFHuzMtXrBXcQqHh05MJjikzBrXra_NUMft46wTvsTk8F5T4DEql2yuHMXOB1rJHIMsxLazUs7-TWkhBED4uK6cA-YqoHJpV34t96M8gb27giGExr2-B3-QFqAfPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBOS3D4jxJZz-Fb0cos7xvQnHthPzI8z9c13Pu2LCLuk9GHg9DqREXHjqCO2pMVEgz2VdABkHyKDVKcgKfR1gsc6VhWDyqBY2wxygG3DTZ9mN9mS-8HglOnODnAZlj0PW7jRfj3qDNIQKtjpcj0Dn8xKCke6WnmqpBB3tPP0k0kvo7wO-C8RrGOh9ZgmSRoyPmRLB2L68eomDFWV8oS19IMdPIc4LMB5oMS_GgqrCHpz5Qb5QWvVlemb3sS3-PvYz9E817b2ldjBdFkKstfCJubo50jXeplVJKgkl-NVU9eciH2Fq7SE6oArf5qC-j3Mc1_gBXRZFzrxqdcuuC0J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5mzdCf1ZSF3kW5Ykovu_qiiGDpvvhlYX-M7AsYUmxoibdiYlHPguCgdz7fbgwMQqhMSjPuFdVRJ8L1gM5Hx-UrnIlUFxFwUhlahMgaR0IiYjZEP1jpQYwkLlXxpODIEtA3ioj-BFIuiScxSt9cAsEvKrLxbyKn2JoR9Xj0_xefUWEDHOMV8ty_aa-POYXb594om4T3rUIhaYbqj_lqs0E5GUh1JOvH3D8sUDpIyITYupuhHze-xgGdqPfx1WUUOcLGQ4uodOBqp42H3bAdcQMqa2YuIibCksQLPzo7MQeOlrkoYeHbePdjl9VCC6aG4ZefqdX7FgxnBg2-18mVU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5xj9y41_EjbbdpStZIv2sSnz-pVzui-lpWuY-apbIgs8ahyvnxS-OoMNQj6eAkKKb3eHyqhyb_LxAVSSw8F6P0bUPvti2KK-CYP6NND6NR3KUTPdFNhjgvJnyMVAgQ-sntoAzEd5KWhR0HUoNvnH729Q2AJyeXGTZrqys8nVPa_qIG_uOdDTmf870VsZEkXYFRyW7L3achE6qVuStgvG2cpCfSuNZuwzMvFJY7F9ri9N6-nPRfgXHRQHtClYB3EoSdBT9ZnwW10Z6FS-Bf0cRjLCGTiDS2n6kB1Li_UG_TqtTsjuVxZ4TtaP6XIacTepz05F5qx3o4hf_VEXQWe1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجری داف و جذاب شاختار هستن.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91671" target="_blank">📅 14:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91670">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43f043a30.mp4?token=XViQWDVAwDbK-J8sBXu3fJav4MXCoU_bSoWwOAmUpMmvNsWnshBNSYez0weKTG9441e0ACl0D2F7zfB9BInQO37d7j_-0SGA5W0xA21zbQ7ps0IOCUJOI_u47nrbd2dTLVq5PO8_qh1s3xpSKVPHCEklQbLnS60S9VrHHBiQsAa_AAZhxdyzl6Wy9BlSCUBCNKe7asGpnfNsZ01bL7-CUDMDyOxM_QujbCtwJWokzp57-SgaPtrTjkRJ63JjzTdfdSRBT1EJkwc9b2mYfqulyrbke8AaPcNx-_HZbyQOzO9_rSAlWr3-bBqdz1legkVyDpRVnX_lLhX2zLrgY7qUcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43f043a30.mp4?token=XViQWDVAwDbK-J8sBXu3fJav4MXCoU_bSoWwOAmUpMmvNsWnshBNSYez0weKTG9441e0ACl0D2F7zfB9BInQO37d7j_-0SGA5W0xA21zbQ7ps0IOCUJOI_u47nrbd2dTLVq5PO8_qh1s3xpSKVPHCEklQbLnS60S9VrHHBiQsAa_AAZhxdyzl6Wy9BlSCUBCNKe7asGpnfNsZ01bL7-CUDMDyOxM_QujbCtwJWokzp57-SgaPtrTjkRJ63JjzTdfdSRBT1EJkwc9b2mYfqulyrbke8AaPcNx-_HZbyQOzO9_rSAlWr3-bBqdz1legkVyDpRVnX_lLhX2zLrgY7qUcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
صحبت‌های عجیب و کنایه آمیز شهربانو منصوریان: من راه میرم روزی ۵۰ میـ‌لیون درمیارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91670" target="_blank">📅 14:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91669">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇯🇵
تیم‌ملی ژاپن کمپ تمرینی خودشو که داخل مکزیک بود بخاطر شرایط بد و‌ امکانات ضعیف به آمریکا تغییر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91669" target="_blank">📅 14:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91667">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhWwJCqpsK0zG0fEINWB0ofNSpEKjQgO_-OPEcErjTWocYiz5LgLlk9jPAWrIhlON9GOmL_gj4PEEn4gOjphJgzKxOD00lmgBKxp4fiywNo3nXE_e2jh2Ko0TLvWlqgsRoRF9rvP0JGLKMu5RG8NTLZBOzIfZUa2uSHsKU4vNh0yvvWrF6a3Z5KnNgrc3FKwoK5CvNMMYsZoU_qz0RDbzJxIlyEGIBpyrW8QHR85_paEgQ_qRLzHMRIOyfjTw0Kgi7mISQ78wjZQEGZKmtQvSLYvPyC8M0ifHzr0NsWJ_ln-ygxPxKVtKxrFmkJcM8IpPyxS-KQnyiCthkI4Dt-qgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNPD4zZ-n9vty5GoaYoygjQsHMX9Yw4LV1iQNTW-pQhvGy2h-3N61cobuWWbmSNwc51YZhlDRkTOzCMOg_JDPHhnW5YubcmvMScOvJynXmPvKBetbK9wfQEcji8c0BN6_lRR8Ae2mc-UqGnhriHb7RuFO3ssVqbP8Izbj2Z_ok1o2zhicGWHYcs58FPRZ6A2WDb5XRmVv5u03j8v_5FaNSwwMyDeaBMn052c8i4J3RKS0KrWtXMyyJ6YunsWieUQRrovY4aRfs3R4NGh4-s8jxbYnlYAE_6pSzouUG2BBOkH56kSXgoKox_6VcuDDAsn511OXiZFpOAT6Kryy6pw_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
مسی قلب‌ها تو تمرینات آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91667" target="_blank">📅 14:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91666">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7LrFZux3HAFkw6VAZk-6mgnygmgkyz9QzmKiQKdn_gMMrGERPmB0P6nT00p6S6IzxsPCbu_sbRtTOjtCp1Uv52Izc00UbcQ5EnoupU6S1Ib4ifNtQC6PSoEWP6zLp7AnUM7Ul13u4hqWJFJbEC-LzH1QmirN-gKMPccqet0XThkPJSoZ_8QVLSCFNG1n5i5keicVPF2WLqonYtqCW-7lijBDLM6G9GlhqYdPTmwxHcNB310JMmtHuNcwsZfhnDkXUYMliWEE1xnc45tnxWWuh1CebuzYtCYhp9TlqkjCzvJteZCv4G5DE4OOBSnkgWR5NQuxzmFRLl5utMF9WHH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین بازیکنان تاریخ جام جهانی از نظر امباپه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91666" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91665">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c3ac63bd.mp4?token=BceQVzd01I6cHokEzYmYzOIbXl2NwRxYlZgbUcmZzhcI_BL7GwOlFo4Q_beV9GZs8sb5g8NyphA6gr0QeHXxuGsooZpaPRRMAca9KinTzrI23kHZZALlPrqwrveLgEK6RAI7hx5J0k2DYqKVT7jeDTQj6Cam-ZhedwFK67DTeVODhajkhJdJOlxNIkNwTKm704KIjMKGhGKaDdo5B_RFNOHQ6VjwsGzYk1xdA6XuSl5EfcZan3kOzYoLdJDuiRKNCBJqDKkk0DWJv8BFF6HrtEh5Y6Rsfr5rkRvKtOyP1AJrCdRlZxkS2VwJff5233rm3nSVWoauVAhuareSfgUzEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c3ac63bd.mp4?token=BceQVzd01I6cHokEzYmYzOIbXl2NwRxYlZgbUcmZzhcI_BL7GwOlFo4Q_beV9GZs8sb5g8NyphA6gr0QeHXxuGsooZpaPRRMAca9KinTzrI23kHZZALlPrqwrveLgEK6RAI7hx5J0k2DYqKVT7jeDTQj6Cam-ZhedwFK67DTeVODhajkhJdJOlxNIkNwTKm704KIjMKGhGKaDdo5B_RFNOHQ6VjwsGzYk1xdA6XuSl5EfcZan3kOzYoLdJDuiRKNCBJqDKkk0DWJv8BFF6HrtEh5Y6Rsfr5rkRvKtOyP1AJrCdRlZxkS2VwJff5233rm3nSVWoauVAhuareSfgUzEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
💥
بعد شکیرا، اسپید و شیدا مقصودلو، حالا نورا فتحی هم موزیک‌ویدیو جام‌جهانی منتشر کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91665" target="_blank">📅 13:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91664">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520253fcb9.mp4?token=O4TCLBgNrmDreT2Tf-4NhFNUSIplOv8GIFwJKyXAvKayYGr-ReyvzkXT1t3NtiRoAjZqS-zM-2_aNUlY7a_pDWmA61Sj7InG6e9JFJ1trzBT8zvEWYd6r3ASvEyvKZi7efiDjaHpSZEJcFVcSQEuaszooxJXLCoX67Xvm5ihjKjLDvCPY8BEBCP9yi9QKjWsI3ljvK7mFKnxqfJ-5xmrsEEMjmCzWgfD6siTDCjMbPXFL_ITObBvTG2kobkFHiZ5XZ1oM3SqAIww-lCHWa04dURpv8qqIWCWB-5DLkAOqdd-VJeuSDN2FO-tJUI0oVMYX66aWBBN46Cg3yVTfO26cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520253fcb9.mp4?token=O4TCLBgNrmDreT2Tf-4NhFNUSIplOv8GIFwJKyXAvKayYGr-ReyvzkXT1t3NtiRoAjZqS-zM-2_aNUlY7a_pDWmA61Sj7InG6e9JFJ1trzBT8zvEWYd6r3ASvEyvKZi7efiDjaHpSZEJcFVcSQEuaszooxJXLCoX67Xvm5ihjKjLDvCPY8BEBCP9yi9QKjWsI3ljvK7mFKnxqfJ-5xmrsEEMjmCzWgfD6siTDCjMbPXFL_ITObBvTG2kobkFHiZ5XZ1oM3SqAIww-lCHWa04dURpv8qqIWCWB-5DLkAOqdd-VJeuSDN2FO-tJUI0oVMYX66aWBBN46Cg3yVTfO26cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
آموزش رقص در ایران با موزیک دای‌دای شکیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91664" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91663">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIikM8wV3crsQJQQg_H3p0ycIkBdSqPKehnx_TVsLquPFbPxZG-5KUy1o286w4JhFBryixPg3sEyV0ERQM_Ta_EPZsMux0MwSdBXi4ppBSeswy4EfZGz9JetZOxlauyi2Rs-AmwE0pydMf3WBhtfvZTP4lrpSTf2NFqKxhUlBrBxw9nV5d05iosuyghPT5F_SONrWbIbI4ykQWvk1IlIUYakDE2E1-nrBDMEB2B4VMSu2cCunaNe6Mx_hOuolRSmrBPHF3P7k-LWbz94A8STaH7ZsrvaKAifSod8DfOOUbCymhfPde1drAwb-3YMWft_wyMl7KfrSX9YLaIh3lD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
✔️
پسران رگنار و عکس رسمی برای جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91663" target="_blank">📅 13:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91661">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d43531369.mp4?token=Q8K2RSoWOOClZsxrOWcRvUjNazzrmNq-KDPQC1sGn4PlFmbSF53MWO2N8BlQ13LVg1Xdy6ysThiDE7B-9v1RBVGEFIGVRlCtcxLKaGExHoLt9BE0OLdGZjkZAJKRE2iUrSTra3q1upmsZuODAp4CPNLUZtt6W7Sd98xv0FcHa7t4jaSbOzSbDGayKRkODs43qOBdm9ggBoxrXkWbmzqS4IyS7vGLmCO8EX7bHtgpDtW-23dQk7OcxT5mh25GVPdfUTZKH9cYvQ9ujGlLPpgeTustZwVGQkzIouVlQSYgGtpKaRUwCp_hc3KIXPukU2T2NVK5P0JMkvqqE6xV2ahrSzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d43531369.mp4?token=Q8K2RSoWOOClZsxrOWcRvUjNazzrmNq-KDPQC1sGn4PlFmbSF53MWO2N8BlQ13LVg1Xdy6ysThiDE7B-9v1RBVGEFIGVRlCtcxLKaGExHoLt9BE0OLdGZjkZAJKRE2iUrSTra3q1upmsZuODAp4CPNLUZtt6W7Sd98xv0FcHa7t4jaSbOzSbDGayKRkODs43qOBdm9ggBoxrXkWbmzqS4IyS7vGLmCO8EX7bHtgpDtW-23dQk7OcxT5mh25GVPdfUTZKH9cYvQ9ujGlLPpgeTustZwVGQkzIouVlQSYgGtpKaRUwCp_hc3KIXPukU2T2NVK5P0JMkvqqE6xV2ahrSzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
صحبت‌های یه خانوم دهه شصتی که ده تا شکم زاییده و میگه هنوز این تعداد بچه کمه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91661" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91657">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgDdoonFd-dEKfwnRpmOqSsO8ZmzJRSpqmKKEYJo3HI6YCmTN6wCuysv-6-wh24jGEPGynk-Iu8ejHZpoVBNm6J8xK8RGiijXEADTwVQyVS40PFnDPA8uC4DZuMORioTqMVW-PoWJSv-S7CfXZBMR2_oRg9ypucRjWJgikG34CO0PRCSRhgN_AOJjvLQrdyAo_T3S3zaiRyo0aZ8IfJbUX2uQgAtnegLZuUvd_2_3QIwqOLkYx_Rg2rW7U1hOEIYMiv3X5OkjPA7W6L9xh23-Yn6vQkZvlA88FFZ0b9fJZDMo8fVL5Pgh-OxaLImrKV1gQXBUVsdrfQVn6zAOBnvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgMO_f20lAjJ-EGSNmdpezG8X4O-BMq9YpTXCWwfGq0q60ZYkY_PFqqmtCB_RIoax1e8WXkqC2sEFj6IC2nUWhIrpOymGxSnofCLKRlL2FfklLMP-xA2n8yq3HTlWdpXAkJ3w6CKNjumBfbKNQlJz0mNVQZ7P7eaDrNupZHGYAlqfv8xZNjGfqXgtFeTdRXw1W8B_tzGI_ykkw11h2iA7Xq9he8fdBzmuvJS_yYi5bW8eCPUslEacCxEYCNEDuR8UM2xLctbeGaJwHBi7hhUqFf1XozAYj4PBH_IEmjfrJGn-byGb_18CrwsLOCgUj_QA8FluQyicfdehlQG2P1uVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxZnRcGNTVtPeH5f2R8dt1HOjNl0hqtEXdX6hfOp6k0kfuqnJqHaehdhFHvthhVa48XsxrNsisiGJJfPAPYs5D0Y5NipBmI_siwXgtkgDtlTPtOMuwgdQVLboqASGCeuOpk-ey2TIt2TgXSTe-XWcM4mAaJf_zr8mggJBz9D5zuGjO0IPy9LX0Se4tuBM-bf30RqJ4AMYy_PPHBH-A-FSpRZNUOqLzSwfAtaTQ-_RCpE8EeprKyUrwdTXHWGLFOQ5uXcJ-Z9ubi_5eqtkEdO-aAFvlWiOdvs9Zta4ul7NvhjB4yu8hDeklbtuqg7A7NoK2ekMOAvFSDbqFItwWbV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEq1ImJjp73g5-qaHcbfsbR-Ox_x6e66pAI1jNjETDvwQDF1PprZmFt3ENNz-Ep2BOYM2ZvKjbi137_Dt02TWeNkVqeGfA8bIR6phqBs5VT1tapHOpRhQ-8hnvrKTeZCYQ7syDDAvSLaIsTX52kD51_t_X7pWwm34hKkLQgRcdPjg6QdkLPb56_TDaCj-QeAzrZzxsC3VBA2NDfEPzXaIesPAy_IQP4kE56EUaXqVaFQ9vELa3sjkLkicD7gGeQa-r1N1TnpngdnHwsAysbbwuJvgwqwVhLdjmpNnoQe6ODRyTL-J2zkVvnUcAJS9C191M6eS42Sfc1bKf4gQ1QY5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
داوران چهار بازی اول جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91657" target="_blank">📅 13:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91656">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3909e54d84.mp4?token=VUX_D6fUmnAVDJDmh_NwVr1ZM2ZkqztD9HH3y-LxkmuZLsnTmg4ggWV0Dn4JVa3uYPb2L-7RDLIhjuwZ9ycMP8PTnyULvw9cdP4AVBM0ryXiCeSxpgIj2S16JEgR3a7GRQupsAb1tnridoeItoGdhYQthbpTNNfs3-9qln5dcX5YhVWNXO9fWlKpwL6X3khB7wVEcToU86NN8Er-SM2OzIfrArd96UvO8dBaSfYMF0maB6iYhnYSIuPPZuJARkaA0rOBBlMpJ-nxHeHDAIwTXs4j8zJPvYd-6Qj_d-q7wWJVgM1jQRatH5h82X_DHlGonOmS3zYqry7FuK4tMNkbxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3909e54d84.mp4?token=VUX_D6fUmnAVDJDmh_NwVr1ZM2ZkqztD9HH3y-LxkmuZLsnTmg4ggWV0Dn4JVa3uYPb2L-7RDLIhjuwZ9ycMP8PTnyULvw9cdP4AVBM0ryXiCeSxpgIj2S16JEgR3a7GRQupsAb1tnridoeItoGdhYQthbpTNNfs3-9qln5dcX5YhVWNXO9fWlKpwL6X3khB7wVEcToU86NN8Er-SM2OzIfrArd96UvO8dBaSfYMF0maB6iYhnYSIuPPZuJARkaA0rOBBlMpJ-nxHeHDAIwTXs4j8zJPvYd-6Qj_d-q7wWJVgM1jQRatH5h82X_DHlGonOmS3zYqry7FuK4tMNkbxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار حمید سحری راجب وضعیت اولیسه و ری‌اکشن پرز
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91656" target="_blank">📅 13:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91655">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
ادعای
مصطفی پوردهقان، نماینده مجلس: رفع فیلتر واتساپ و یوتیوب در دستور کار قرار گرفته و بزودی این دو اپ بدون فیلتر در دسترس مردم قرار میگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91655" target="_blank">📅 12:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91654">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68f156545.mp4?token=P0m2489kkdRzanggozQc6KIZVClC8FcVbpreqRWcedS5ZivvQ1jRSoHhVXwT3-Wz5NfIsCyf7dmNDHuo0jag6MjeVThwvi_nm7Xdl5yHG7v7HLJ6OSjwgUekyzxUuj7YrbvoIwRZPk1knCCtU-H2T_6rvxivUpjzu5_Mmve9SLL-SrIkc2QrYbIpM_R_OPOl2qdKtACQmp9R2KdmHW-Mbg6GFkrPMGV4yXYEunC-Oo5LfhKedv4XNg32sF2v_RFmk4VilwFM_ghzE7ohsM4AJyMbYdOL-iqoar2scEfsnL5iR7gDqyclmg_g_118sP3kyVf6KcHbQKGVBB57YRMWaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68f156545.mp4?token=P0m2489kkdRzanggozQc6KIZVClC8FcVbpreqRWcedS5ZivvQ1jRSoHhVXwT3-Wz5NfIsCyf7dmNDHuo0jag6MjeVThwvi_nm7Xdl5yHG7v7HLJ6OSjwgUekyzxUuj7YrbvoIwRZPk1knCCtU-H2T_6rvxivUpjzu5_Mmve9SLL-SrIkc2QrYbIpM_R_OPOl2qdKtACQmp9R2KdmHW-Mbg6GFkrPMGV4yXYEunC-Oo5LfhKedv4XNg32sF2v_RFmk4VilwFM_ghzE7ohsM4AJyMbYdOL-iqoar2scEfsnL5iR7gDqyclmg_g_118sP3kyVf6KcHbQKGVBB57YRMWaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
لیونل مسی: «از نظر اهمیت، بهترین گل دوران حرفه‌ای من در وقت اضافه فینال جام جهانی مقابل فرانسه بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/91654" target="_blank">📅 12:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91652">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4bB0kIcJrxYcnwQ4ZOrdSfoe58o7-9IBnQ_JdMmOg-fSa342MftQXgpQGx-9XkypvBYScSOPSDt41qF9Q4HqEO_Npo-PLT6Yxfm83MxQ_qBqMWYuw1k7UABrFsVlFooFaboKNlLqvNAHZOQjvkn2EwRiQMhizPDpSvACZGL3CxoPjYQ6nI59oaSMq78PtIyqzSWWFPGoAVDgiMuC2o1FLz9I-DecoPE4wlDv4aIHLwh37_9Mzycm0Q1GWQyy408z0AHlHtyjNX0GmduCbE4OYLtd3VpCzWG_bOLxHeragONMIt4jfvqKK8pcSBQ5fimmVcw607fTEbrZKpmJj-jCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔙
هواداری که به خاطر نوشیدن ۳۲ بطری آبجو از کشورهای حاضر در جام جهانی مشهور شد، دوباره برگشته است…
🔺
این بار او ۴۸ بطری از هر کشور حاضر در جام جهانی ۲۰۲۶ دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91652" target="_blank">📅 12:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91651">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6zxFPCvq8M3gXfmQmsajs6ddK4e2ufDDdLkCqTa3r4Zo0Ba1y5nxehY1P2i-a7eebdpt1UXXUqgjGbAl49oIaKRbWbMyJ7WhNNn4ckBIoNpgBv0WhD3Nzv8Ga4prLlS5avdFKfomkSI3HMIAXq2NKy7_1wkx1uXAgJ-dU0mncSd2A7i3sxkMWBbqiWQM34elW8hOs75XokfS2QgC947QnqPI5IlWbgr6ZaCgt-3qCaP1IzgwWXE6CGTGfMcotGZ9vWjbMCo1FHM8tTiGajDfdq0vRJ05-T0fSQ9-P_xBJ6HlR6VcxA5q7loIXN-wBsg7L4ci2OR_SrawRfGpgvwjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژوزه‌مورینیو دقایقی‌پیش وارد مادرید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91651" target="_blank">📅 12:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91650">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4RSri3jAxED26WfO2VUPaGG8eNurHqMlInimvi4jVKrYEBWKmYLitbz8-KmlDu8iwk7suCyNa-Vrz_nDK1uWhoPHs7fG7KckZc-7w-pjd_1UYr-7YE1VJwN1HNUmnqZvwno8kY3M8UIUK3YsxVgLif7kf5_XJ_WWXEqwHtjlagfhaHPC9Ayi8amLBHvQw8Nhb5o53op2Ma5qFR_cHrT-Cplhd_PQOhy7S9gekFyeph0gQ9-t2XtK24C3shXbHk8TkSVamXATT6VEL0jCYHG0SOi6IOxP5BnJkLX1RxYb_Hk8L2-ZU3qk_NMkje36YsYwme6v1xmLSR--O49s7ywMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی فرانسه در گذر زمان..
انگار دو تا کشور جدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91650" target="_blank">📅 12:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91649">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fSVSEexb03bgUXWpLmpKhqBgcIgpHL1lSr2BJRBF3kC7r-yJqk2nJbsavgPbeshzqdoquKlCtT9WvW2VAfF8Ub56lVbWswlMlA2juRN1oM2AyxKZGp0gzWrrzyaIWiUq_UsDstIn4TjoKRP4FSIW-U4ZyJppLB4n66NrD-GS8SwuwhJGNPBX5QS5BXHZ2nZVwjLbx48AMqPuN09Pq_8_ujQjFPboo1wLeY9kwMFfuBM-1KEKOoaE2-nbmcG4zqYlqQe3XfV3k4C1zphfvm9kOSzNDiQALlXbmiWZYoz4tvk2-IU6FE9iNqNHeC9jMn__cVgLhux1hJ4VFKUzzrPiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
ترامپ دیشب سر زده بلند شده رفته فینال NBA رو ببینه که باعث شوکه شدن افراد حاضر در سالن شده و از نکات جالب اینکه تمام ستاره‌های دو تیم فینالیست توسط ماموران مخفی آمریکا بازرسی و تفتیش بدنی شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91649" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91648">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b81ccf3378.mp4?token=GisWupMCIiulyjas1zLZNZbAs6IuuJdFTVN45jo2iVkQTaUWTJzneeOo80axUi8uDbRQZw4oJMHCWLG-gO2V7p7Um3f4r7YtATTxia06FqGtk_6hm9vGboyS8ALt3-U_PZGEBes6_PRqEp7ZRN539cbo957O3Dd-SAt_2g6Rv8xZ9M3QHPnq-WuiWhJI5RuafJvNIYJhshx3IDI_uAtuMCNPjtHTQXXcpI2eQyit-_nX9pByQ1z5acu_4MTH9P2w7gwI0O6Nx6wCkogC031Nr89XK_ZXRgB5_Le5oz3icCqJQRfbG5L5hMjOBZDj9vn21Xto3qS2gxrzfubn1p6sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b81ccf3378.mp4?token=GisWupMCIiulyjas1zLZNZbAs6IuuJdFTVN45jo2iVkQTaUWTJzneeOo80axUi8uDbRQZw4oJMHCWLG-gO2V7p7Um3f4r7YtATTxia06FqGtk_6hm9vGboyS8ALt3-U_PZGEBes6_PRqEp7ZRN539cbo957O3Dd-SAt_2g6Rv8xZ9M3QHPnq-WuiWhJI5RuafJvNIYJhshx3IDI_uAtuMCNPjtHTQXXcpI2eQyit-_nX9pByQ1z5acu_4MTH9P2w7gwI0O6Nx6wCkogC031Nr89XK_ZXRgB5_Le5oz3icCqJQRfbG5L5hMjOBZDj9vn21Xto3qS2gxrzfubn1p6sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
حمایت و تشویق کیم‌کارداشیان برای لوئیز همیلتون دوس‌پسرش بعد نایب‌قهرمان در رالی موناکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91648" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91647">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔥
🏆
برخی از درخشان‌ترین سیوهای تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91647" target="_blank">📅 11:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91646">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
تیم ملی جمهوری اسلامی به فیفا درخواست داده تو بازی با مصر به خاطر عاشورا بازوبند مشکی ببندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91646" target="_blank">📅 11:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91644">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIFOnNFqNkCIedtFtlEF3WuXbGtgtrmeM7VTy7ygP4m-Fap_F5ZuBu9F80aYFZoMUoJ8WxMGbHcwyGaXxEH5Q1xVFbGBQw5YRyQeyVen0ybMBmWNtnvDLO4TX_v7YtjbRCzd-gGW27VRBqrT6HWura91ricv6BfV8jtmRa-Gh4xWlryULNuiaYrBsoBPzkOFCm9iIUmi6xb75XRT_icpTW42DJ8z4RATv8jIKZu5N9MhuqsZLWeaQZykHrWFafbB-posR6fdycEQF_scASrn0ZdaaFFuFsh_dKqazBAAvRju_cLHJkmzmXeaQAXGzVWlyR70iHLcPh7NQZXWhDzmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇩🇪
فوری از اتلتیک؛
بایرن مونیخ هم به جمع مشتریان یوشکو گواردیول مدافع کروات منچسترسیتی پیوسته و قصد داره برای جذبش تلاش کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91644" target="_blank">📅 11:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDXFKyNNw0RwbszSE5J1yGs0fFdeZNCrrsPBw_0-m74S0Y0PQYQ2xfOuM6gUNRNBoWSKWZJcOuuMXr35HIlfcSzndYFJntZTr5lxd2L2kBNuv4SMBYcpsIFwNwOcHRftaEUZ1vT83bW25ZRgnZtLMDHFfO6XRvbz7s_75GaBi9mK8UWrKsj_e7pf3syokU0W_RIGUISzmOloqOhK6lgnwMGXudBKblUdiiAxnXHWWNh7gKK3_FvcB0z-0aBD5L10w5yLUc33Rfqs2iEYuMaR1Qd073rL0dlmitVoxVxQaoC57KR06miY8XzHwMZz6mkmDmWWHJtx6lKwKtMI7pspUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🔥
لامین یامال از زمان جام جهانی قبلی ۱۰ سانتی‌متر قد کشیده است. یامال که برای اولین بار در ترکیب جام جهانی حضور دارد، با قد ۱۸۱ سانتی‌متری خود جلب توجه می‌کند.
✔️
در سال ۲۰۲۳ که به تمرینات تیم اصلی بارسلونا پیوست، قد او ۱.۷۱ متر بود، اما با برنامه تمرینی حرفه‌ای و رژیم غذایی مناسب به سرعت رشد کرد و به ۱.۸۱ متر رسید. یامال که هنوز ۱۸ سال دارد، پیش‌بینی می‌شود تا ۲۱ سالگی قدش همچنان افزایش یابد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91643" target="_blank">📅 11:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91642">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
تیم ملی جمهوری اسلامی به فیفا درخواست داده تو بازی با مصر به خاطر عاشورا بازوبند مشکی ببندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91642" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91641">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🙂
دیوث بازی مرحوم مارادونا در جام‌جهانی ۸۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91641" target="_blank">📅 10:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91640">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
ویلای ۳ طبقه علی کریمی به متراژ ۱۱۵۰ متر مربع در شهرستان لاهیجان توسط قوه قضاییه مصادره شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91640" target="_blank">📅 10:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91639">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ade73f00.mp4?token=OLV34l9aSKTzdKVl3N00G9VTCwAlaRQQXfgf7NscAT3Lh4mHVOdbxRplTSVLdnQFKq6-SjXnOeA0FZL9BFOq_KkwfnrsLsXW5O1WlgQ1Pu12eFgKasu3H7BY52IQHAzh9iD80Jm6V5KRj_2r7QX-z-zQzh-NFpS51HrDHxs5y57Zc7UcljAbQ6YfR-rySHxst3tGiudrZF9D84A8iPv8fA6nTQM0vjJlK3UASlszLWxv8_Sgc7zzIIQY5pXz9SSUaiSLZgkxPBd6jst_lcIX8UsY_6ta_rhxEwyWvoKsYarTsRhYCZeX2SlNKIWUevjubq1k-NvWeWO4A8JXKCrGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ade73f00.mp4?token=OLV34l9aSKTzdKVl3N00G9VTCwAlaRQQXfgf7NscAT3Lh4mHVOdbxRplTSVLdnQFKq6-SjXnOeA0FZL9BFOq_KkwfnrsLsXW5O1WlgQ1Pu12eFgKasu3H7BY52IQHAzh9iD80Jm6V5KRj_2r7QX-z-zQzh-NFpS51HrDHxs5y57Zc7UcljAbQ6YfR-rySHxst3tGiudrZF9D84A8iPv8fA6nTQM0vjJlK3UASlszLWxv8_Sgc7zzIIQY5pXz9SSUaiSLZgkxPBd6jst_lcIX8UsY_6ta_rhxEwyWvoKsYarTsRhYCZeX2SlNKIWUevjubq1k-NvWeWO4A8JXKCrGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🙂
سوال روز مخاطبان فوتبال: یعنی آنتونی گوردون با ۸۵ میلیون دلار رفته تو پاچه بارسلونا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91639" target="_blank">📅 10:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91638">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ایران میخواسته یه بازی دوستانه با کشور گرنادا که کلا ۱۲۰ هزار تا جمعیت داره برگزار کنه که لغو شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91638" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91637">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d23ccc5d.mp4?token=noYH1wDWXoO5QgEws9_xAubaNg9zP962p8aP6O5M7vHDwnRcYlFD03iMsxLl60tAOyCT8Yq6q9NRvwmMX-ZA0a1C1euhUKm5f_wf0Pyyq_nhWH1MJ_s3pP9pPcANs_4wizaxd0Dl_AAlxKgtaZMFZUPjeOBWBTDY1h4ajGbWwR1WtlfTqmCswGWAZqy4oL_YQ5uWl16sFwsd-Cd9FqBlA_gb76B-OCcSAqyo4YUvIv0MEAJimaRsb3eH4Pkn05oW-0d30w2mwQzmAVNxsCTcYKQOmsy7ETRaVU5AZTt7DjwIRmFKORnQSdZIwa4iomKKnj4Xy0twe0EMaCP3LzeAUZU7trq5dzo9MT6vXS7xouboSUNDP6ZXKytL2chEy3CfTqDpV81fCUcmRes8_AtGTfqy0k36P6ca7UQQ4ZqQGeuuPG8jRCu-5SVkb7sWcEcnzUVfCH15xAqoCdC9HNvLGNOZKFECc6IFsGgka_eg4SPTc3RdNtLrfEG2Gm58xJJcC_ygS__jaPWK5CHBqwnJdCv1L_ShrymfVxfIvtozUQjLxFGlSiEOQFZJEibXETsIf2hmXpp2otGvqj6mFJHTwDBxlL2j7X-nAHyr0MlCVfLwOm8ACsZBidF3ufFu5-3pFF60f3Fc8GocSB-gVFXo_-TyVJv0NIOR8WQEbfc5rYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d23ccc5d.mp4?token=noYH1wDWXoO5QgEws9_xAubaNg9zP962p8aP6O5M7vHDwnRcYlFD03iMsxLl60tAOyCT8Yq6q9NRvwmMX-ZA0a1C1euhUKm5f_wf0Pyyq_nhWH1MJ_s3pP9pPcANs_4wizaxd0Dl_AAlxKgtaZMFZUPjeOBWBTDY1h4ajGbWwR1WtlfTqmCswGWAZqy4oL_YQ5uWl16sFwsd-Cd9FqBlA_gb76B-OCcSAqyo4YUvIv0MEAJimaRsb3eH4Pkn05oW-0d30w2mwQzmAVNxsCTcYKQOmsy7ETRaVU5AZTt7DjwIRmFKORnQSdZIwa4iomKKnj4Xy0twe0EMaCP3LzeAUZU7trq5dzo9MT6vXS7xouboSUNDP6ZXKytL2chEy3CfTqDpV81fCUcmRes8_AtGTfqy0k36P6ca7UQQ4ZqQGeuuPG8jRCu-5SVkb7sWcEcnzUVfCH15xAqoCdC9HNvLGNOZKFECc6IFsGgka_eg4SPTc3RdNtLrfEG2Gm58xJJcC_ygS__jaPWK5CHBqwnJdCv1L_ShrymfVxfIvtozUQjLxFGlSiEOQFZJEibXETsIf2hmXpp2otGvqj6mFJHTwDBxlL2j7X-nAHyr0MlCVfLwOm8ACsZBidF3ufFu5-3pFF60f3Fc8GocSB-gVFXo_-TyVJv0NIOR8WQEbfc5rYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از هواداران ایرانی بانو شکیرا هستند
🐸
😊
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91637" target="_blank">📅 10:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91636">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🏆
🇺🇸
🇮🇷
کشور آمریکا خبر داد که تمام بلیت‌فروشی هواداران ایران که از طریق سایت فدراسیون تهیه کرده‌اند برای جام‌جهانی مصادره شده و حق حضور در خاک آمریکا رو ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91636" target="_blank">📅 09:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91635">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/devSPgum0p5Yud8HTX3f1NhT1w7BZawmLBtPun5-HGd8ANq5N-xAfVjvoAI-ahtKUhGGEdwo7tzZCwthpY-CNY4RXu21rpD3wK7aZ6zoj66LuKMRNiieO9WF3V4l_1jKM_qMHDuQOCu_Q6QVN_x8sIddaRr2eaqJOGO0X3RQiiozivUkkKM6ZDfuQ-guQIwMijlE8Be9v-1j2CylU3G-eyqEo5LWAcTujE45gfTOjSp_qwEgdp6eQzC6sFcBpYYgUxbnEbZQoMkcotry6VxLfGYQpxTrYoyMGO7OTXiw_NI7QLyiruRrhTH4PDfmEAFDmbqhBW8DmLWo-aHmPpUsuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه مدل موهای نیمار در یک قاب.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91635" target="_blank">📅 09:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91634">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eabaeab.mp4?token=i-9NH9-xCErep_vsuuuKWRZVX8U5EvCPI1VFVNCton-Tx2TLcNAWk3D5w4zrTM9o32D8sH4-fpetdq_PzkqI87iIYXwFzT35InjcgnoLX6Ohf-XYc_KwB2KJVacD4waQkHkzHAPpIVmCTMp0j5hDt-g5yvh_oH7DI1d_ZjZ8IYPbTJv87gTrnBpN9p0KjBRbla6cCZ1nMyyWRI5o19kSMoAxnkPq1rU9OFaadJtQPIrtNc264i3m74qaNBnz1_408qI4eaW9tuN7bNhz-MKcDQDSX0zhRGQ65T1EPFWG5uo2Ys7643kXMgMCC_XJFTADLWj44xpQQjZ75cnWVaIDVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eabaeab.mp4?token=i-9NH9-xCErep_vsuuuKWRZVX8U5EvCPI1VFVNCton-Tx2TLcNAWk3D5w4zrTM9o32D8sH4-fpetdq_PzkqI87iIYXwFzT35InjcgnoLX6Ohf-XYc_KwB2KJVacD4waQkHkzHAPpIVmCTMp0j5hDt-g5yvh_oH7DI1d_ZjZ8IYPbTJv87gTrnBpN9p0KjBRbla6cCZ1nMyyWRI5o19kSMoAxnkPq1rU9OFaadJtQPIrtNc264i3m74qaNBnz1_408qI4eaW9tuN7bNhz-MKcDQDSX0zhRGQ65T1EPFWG5uo2Ys7643kXMgMCC_XJFTADLWj44xpQQjZ75cnWVaIDVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب و عجیب لامین یامال ستاره بارسلونا درباره دلیل بستن باند روی دستش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91634" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91633">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b5e13b24.mp4?token=E8pnkI9dUIR4O2exJGmVR5cGOFVtpgrqN6D1RTAAoxpcpV31AqXsg-_JPwKbXPh_s-KslqWwN7vIPmVAueZQmSdBtok5XvnEgSpyIv2EWkKT1BpENJf132Pov9V5nvRdSB9oF9fBwyZ2Gqybqh69IwwNSSCcz7WS9-FlSMWgbhqJHzszCbw6c_aYMaOLGfIIVw8Q9bPKxlvk9CyW3lVn1lCi2ASHHgpYe-eCpl2r0OgYpsYxBfztt6w-HVkJ035hlkMUaaBaazA3aJIoAvuItKxWMMUOZIiYCcz_UCDQSn0DDBATtbCQkYp69pSdsW8Xm8im-b6rDWtng85B7ppsgn8NlUOysjbL0ao-AbbE_hrmc5m_EPFs30NPMUCptXZh4McYqB7YoFZUwDeCAYUaGcEAQt4Z30wUOByxLTNHpYopeUGus0Sd1Vx7-eCogyyvR0LPFeF-jqpJFVwM24ofG_xobCIORMgxqzJMEmMqY_xm7yPpZ4w7ZzDACgV6q5E4QYvOhNDbV6aEBZbWhqzFGdL1NmD6UzojIxfg5A344_N76TVx-3M4DowOGLD5kaTcQP9SqLZjo8VGJI0s-YLQtIdTmvyeOUxCskHBtukz2Lb6xgRxcDTgVMArEk6ypZVw_9WpMvAe-OO5qPzshb920VPQf3olZJxFczHdE5d48GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b5e13b24.mp4?token=E8pnkI9dUIR4O2exJGmVR5cGOFVtpgrqN6D1RTAAoxpcpV31AqXsg-_JPwKbXPh_s-KslqWwN7vIPmVAueZQmSdBtok5XvnEgSpyIv2EWkKT1BpENJf132Pov9V5nvRdSB9oF9fBwyZ2Gqybqh69IwwNSSCcz7WS9-FlSMWgbhqJHzszCbw6c_aYMaOLGfIIVw8Q9bPKxlvk9CyW3lVn1lCi2ASHHgpYe-eCpl2r0OgYpsYxBfztt6w-HVkJ035hlkMUaaBaazA3aJIoAvuItKxWMMUOZIiYCcz_UCDQSn0DDBATtbCQkYp69pSdsW8Xm8im-b6rDWtng85B7ppsgn8NlUOysjbL0ao-AbbE_hrmc5m_EPFs30NPMUCptXZh4McYqB7YoFZUwDeCAYUaGcEAQt4Z30wUOByxLTNHpYopeUGus0Sd1Vx7-eCogyyvR0LPFeF-jqpJFVwM24ofG_xobCIORMgxqzJMEmMqY_xm7yPpZ4w7ZzDACgV6q5E4QYvOhNDbV6aEBZbWhqzFGdL1NmD6UzojIxfg5A344_N76TVx-3M4DowOGLD5kaTcQP9SqLZjo8VGJI0s-YLQtIdTmvyeOUxCskHBtukz2Lb6xgRxcDTgVMArEk6ypZVw_9WpMvAe-OO5qPzshb920VPQf3olZJxFczHdE5d48GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
مستند کوتاه و دیدنی تلویزیون اسکاتلند از تیم‌ملی فوتبال ایران در اولین دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91633" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237827913f.mp4?token=g7psEmOx65d_ALloT4d1VJgmFMciO2iP9hIxCSWDB5DkFg1vhjEcwY1q-KXOHqnT36gQwpCtYdAG4qBh0GHnEKg5IeJXc088s_eBj9DGM3Kd9emKojaiC30sqGbEpVoRtc49llfapbzCPt559k7yNmXWLUiTAaxybB1L1x6RqhqL5CT84ztZ0ke7eaRbbPFzmRNBWWejg41VNeoLyUElTb6EEs8tXpFUYmHy8l6T5tC7zwHqGNw26wyAm5EcJuwdvhFUPrTH1IGvjiP6G6mA6FBlpxacXYP585T25uMWMQiWIOjJBH5w-XBP6-BvBQasIjUbMTL3-q-krTMvEj4dq4bgwLsvPObsOS43Q1yST7bairKNSNpSxUPKIUvLa3SSv1xi3ZlDzwHYEBibqmGT3VH7Bh5_9RxtcEcS4leK1p2c5NWzigDpU4Wlw53JtRR2AaXXb_XNKX36OZLytrdiC1G7Rjj2YbxVaMdlOEzo6sCBV4iiGfxcf8sc44j55mp0b2GHvipPc56gn6VvdZEsPQsDpwV7i5oetVKtYvNw0XZ2kuA85wQZWWRswYRf7JhGNQgSNd30NMic5Klv0hM8Ef3tXUa2OieUlR8zcTcfdLC79PIKfqmEMBcolUHPf9ffEwrnx_gQOiPzrPvV42OUUVWRO_AUlWDHZmVvO-t1FhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237827913f.mp4?token=g7psEmOx65d_ALloT4d1VJgmFMciO2iP9hIxCSWDB5DkFg1vhjEcwY1q-KXOHqnT36gQwpCtYdAG4qBh0GHnEKg5IeJXc088s_eBj9DGM3Kd9emKojaiC30sqGbEpVoRtc49llfapbzCPt559k7yNmXWLUiTAaxybB1L1x6RqhqL5CT84ztZ0ke7eaRbbPFzmRNBWWejg41VNeoLyUElTb6EEs8tXpFUYmHy8l6T5tC7zwHqGNw26wyAm5EcJuwdvhFUPrTH1IGvjiP6G6mA6FBlpxacXYP585T25uMWMQiWIOjJBH5w-XBP6-BvBQasIjUbMTL3-q-krTMvEj4dq4bgwLsvPObsOS43Q1yST7bairKNSNpSxUPKIUvLa3SSv1xi3ZlDzwHYEBibqmGT3VH7Bh5_9RxtcEcS4leK1p2c5NWzigDpU4Wlw53JtRR2AaXXb_XNKX36OZLytrdiC1G7Rjj2YbxVaMdlOEzo6sCBV4iiGfxcf8sc44j55mp0b2GHvipPc56gn6VvdZEsPQsDpwV7i5oetVKtYvNw0XZ2kuA85wQZWWRswYRf7JhGNQgSNd30NMic5Klv0hM8Ef3tXUa2OieUlR8zcTcfdLC79PIKfqmEMBcolUHPf9ffEwrnx_gQOiPzrPvV42OUUVWRO_AUlWDHZmVvO-t1FhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
رفیق خوبه اینجوری پایه باشه. حتی وقتی موهات سفید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91632" target="_blank">📅 09:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91631">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Fifa World Cup 2010 (Playing Football Games)-[www.Patoghu.com]</div>
  <div class="tg-doc-extra">[www.Patoghu.com]</div>
</div>
<a href="https://t.me/Futball180TV/91631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🏆
بریم به حال و هوای جام جهانی 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91631" target="_blank">📅 05:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91630">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gL11gRZAA1cBCHs1s4CCbXLu6_C3nydJJl3BDPcYgpvhra89Sv1efnx8IM00ZlKxA16uM409XWDq_im-3wmVZPd-ICBkR4R3INU2isLJ3pxDqzHKV288LvHLmOlQ22ephGkndz0gkokrKaNl3KfJD1wc-hfK2a4jUaGq5xvj6ChiCyTXQu7yV30dBi3aYMgDrQCC-WS8-kjfwnKMyx44hyH5US-4GcBBq4JZqf0ZZTD96ub1nLxA_9d297EWNtCDCPFdOjNroFCCukIStwmM8OqXUR13YDkabUK7VLEOangIGLlYP-lSyP6gj4aNNzRAa_XmZGUaB1QnmoCMFWUtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورییییی
از موندو:
🟡
🔵
الهلال و النصر پیشنهادی به ارزش ۸۰ میلیون یورو برای جذب رافینیا ارائه داده‌اند؛
با حقوقی چهار برابر حقوق فعلی‌اش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/91630" target="_blank">📅 01:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91629">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ-EOmBldVnqM7OwiYIUiQIvjzBh8Nas-zdsdvFAd764eqXaPjF4gS8RipdVlPTJwp3vJHowVNfsdXDhIKY5Nsq4bJmJY_Pnhd26yRK68EXsH5vygIqfbOvqppls7rLPzQDFV16IJzfpxK1rjCEnpTRFlvCyJRXYsTKws-c0E04y-lRTaAwYgTFehU1vQY_PBavh_hXHkjlGfbFTBnQmsYbTe2DC0cHeiJIZ_1il7QdTyAvCpeMXstIDyc0bI_0NRgLCvuJTyBR-EjZP81N-jVxS0urq8YV28tGDsnEG_ZwanA81jI8Tk2xjm199QR_YSt_1foVMWe3jn9p-P7_4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
رامون آلوارز: بنظرم بازیکنی که پرز قراره براش 150 میلیون دلار هزینه کنه خولیان آلوارزه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/91629" target="_blank">📅 01:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91628">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nt9duSkvz8BOCTaMdxg1R55LuaqZQeWzb2qq6-Wg8MrpYcLpwTLpjIWFIdEiySivQZpNFM2Z-iHhZ8RASl-6QwJjkTzzUMscUHjHznwzej83RwUQefK5u3_tQhw8jO2cWh0mkVtdIEawfhvet0cVOvQA98VxUSaiyLUb5jHaFtLKeJAdLOLVgUpIpdH-Xl8DyiGRD3JJttypIQdL8Embci8CgUeHr7dqgKr4I6xWBaKsZNo5AOIahtgorSKN6hAsvxDRtnKuUVTLGb_tIQ9dv-7fcAODeJ6e3dIcg5hnp6DhjYjDHY2uT0z1yr9EmH1CuhpyvP3xMHp01OX1zQrLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو در کنار رئیس جمهور پرتغال قبل از سفر به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/91628" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91627">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عمر آرتان، داور سومالیایی منتخب فیفا، از ورود به آمریکا منع شد.  او قرار بود اولین داور کشورش در جام جهانی باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/91627" target="_blank">📅 00:59 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

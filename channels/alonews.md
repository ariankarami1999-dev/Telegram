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
<img src="https://cdn4.telesco.pe/file/gu3ReaQ210xuXWBZ65JMG5L_UroZ2TFDjTLLnKhhmpiPvIhQz-KbFtg36yWhT6mkFSxKdrLsQysiXaINAukkcVmuhMdkuTIGWMg4DXwYAuhrT8lgaE2EW1i4aPcvCz069Cz9w8Er5h95hzvrpKHazTEM_Nq9dr3LsPT2sGDdlu2yEh7iHzZnw-fzY7Mc6PGJ7kVAAqsFcZjQB0fr3h9j74Fg0zycHqcC_Rbc8dRjOTjmP2l7ZZolDMiS5D8EO1Sjo6ut57EDT1MTN2_inl0vCiBGwEGLul-VwqoHtNuaFSoVUWnRUhGnTIHxEQAFw09rmGywmnLweQXLUI3MpC37jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 953K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 10:49:23</div>
<hr>

<div class="tg-post" id="msg-124697">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
هوای مشهد برای چهارمین روز پیاپی در شرایط ناسالم و غبارآلود برای تنفس شهروندان قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/124697" target="_blank">📅 10:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124696">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نایب رئیس مجلس: موشک‌هایی که به بیت اصابت کرد تنها چند کروز بود نه سنگرشکن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/124696" target="_blank">📅 10:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124695">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
روزنامه اطلاعات: ۸۵ درصد آب مصرفی کشور به بخش کشاورزی اختصاص دارد، آن هم با قیمت بسیار پایین/ معلوم است با این قیمت آب را هدر می دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/124695" target="_blank">📅 10:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124694">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خبرگزاری فرانسه: کابینه ژاپن ۱۹ میلیارد دلار بودجه اضافی برای محافظت از خانوارها در برابر تورم مرتبط با جنگ آمریکا و اسرائیل علیه ایران تصویب کرد.
🔴
دفتر نخست وزیر سنائه تاکایچی گفت که بودجه تکمیلی به طور رسمی در جلسه صبح چهارشنبه تصمیم گیری شد.
🔴
سخنگوی مینورو کیهارا گفت که برای به حداقل رساندن خطر در بحبوحه ابهامات مداوم خاورمیانه تدوین شده است.
🔴
تاکایچی ماه گذشته گفت که این بودجه افزایش هزینه بنزین، برق و گاز را کاهش می دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/124694" target="_blank">📅 10:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124693">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
تبریک ترامپ به «آبلاردو دِ لا اسپریِلا» به دلیل پیروزی در دور اول انتخابات ریاست جمهوری کلمبیا: آبلاردو خستگی ناپذیر برای کشور و مردم بزرگ خود می‌جنگد و عاشق آنهاست، درست مثل من برای ایالات متحده آمریکا
🔴
نتایج این انتخابات برای آینده کلمبیا و رابطه آن با امریکا بسیار مهم است
🔴
حمایت کامل و بی‌قیدوشرط خود را از آبلاردو اعلام می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/124693" target="_blank">📅 10:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124692">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خبرنگار الجزیره: بمباران اسرائیل با بمب های آتش زا به شهرک الحنیه در منطقه صور در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124692" target="_blank">📅 10:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124691">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOXkQvf0NbTTr9OGYaV08F7lUITrqNRBKpUyaab2I7LA2lv32-89c6ii9NPgA9orwuN8tqx15c_nW5Ulm3eDt0_g6jwarty6Y_9B6QckLAkMJsPBjegCniic67s21dURk83amwX8ZFvoXtmnLK2Nn0Q4_80QdRSV_1BceMkp7TgFT5Dw1EoePQIZyLAwD-HAGpZRb85sahEPVMfDYOoul2dykZ5BDVYlbI1nx0C6EN1IFbDM0_hRY3auct2mzAAO7Qq1zrCZgBOFXG9cgrF4it-UGCOMdAMpkLIklhN1pU7Xdoj-CJLbLl4qMyfISfpcUtPdxcZpOfJLoivYAl9UyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از قرار گرفتن نام چهار صرافی رمزارزی ایرانی در فهرست تحریم‌های وزارت خزانه‌داری آمریکا، نوبیتکس، والکس و بیت‌پین در بیانیه‌هایی جداگانه اعلام کردند دارایی کاربران در امنیت است و فعالیت پلتفرم‌ها بدون اختلال ادامه دارد.
🔴
این صرافی‌ها تأکید کرده‌اند تحریم اخیر به معنای توقف خدمات یا تهدید مستقیم دارایی کاربران نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/124691" target="_blank">📅 10:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124690">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7l_YOgsuvgjLCs3b25FQefmmY6GgsXLuqV8Xdiu6EcPXX14bdXiR4s0Y4K4i1OU8vTuJFeDaiky9w-RhluTsqll_VWR7tp8ZAjuqPi67ovNuWWHX2DYydlbssIUva5B-IMj-KXNDzdDn1YvFP-A2h6_cjxOQfEHw2NbkQlhxG0e1KB3cIFADvCRpOhvLrCcgvub_ohjwFuPSxtaWKMA050Xij9LMCmnHh9H6E8bpa45x6p1KsEi4dJqhBgZVybvV6iwR99HX2-jWVwm7anPRNKDBNZa62fcVpHWCP991AIEfBBx-mqzzYnqYRTx7rdAyTVTg3R1ER6dmYNGvMRr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عضو کمیسیون اقتصادی مجلس: افزایش ۳۰درصدی قیمت مواد اولیه داخلی، قیمت خودرو، لوازم خانگی و بسته‌بندی محصولات، در موج جدید گرانی در راه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/124690" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124689">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
پرداخت افزایش حقوق بازنشستگان در سال ۱۴۰۵  به تأخیر می افتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/124689" target="_blank">📅 10:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124688">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP1Qh-yQZ4s5iPamI-_LCkVIkmbIWxT3iruhDaL8eFLQk61_PruRf7KtwUcc9kU4yz_jktnD6SSLF2I44c1FhPL_lDhT9DxUV4Bjo8lyc5UvQ71viYKOmc6IjKfO8Ni0OEk5aCAAm-w2LrROxoozLt3QRBHwFpBgBVKoe-hUQ2ogN7SABtNzFbCtif62rLZUFWzby4YxrQPxzRczy1XCMtdo0FcGB-H_8Cm_6FZohfFvcGgUw_uxYi3zQkvbLBgeHm-k6FB165UHf7aL3jIybHOlqFC-YbpJUUpJ8NO-EH-qEiEdwURmesY4s7Z1iw6-9QO43uHiBKEA-RZ68oZtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک ماه پس از آن‌که دونالد ترامپ طرحی را برای اسکورت کشتی‌های تجاری از طریق تنگه هرمز اعلام کرد و سپس از آن صرف‌نظر کرد، ارتش آمریکا در تلاش است با روش‌هایی کم‌سروصداتر از شناورها در این آبراه حیاتی محافظت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124688" target="_blank">📅 10:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124687">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
جنگنده‌های سوخو-۲۴ ایران مواضعی در نزدیکی اربیل را هدف قرار دادند
🔴
گزارش‌ها حاکی است نیروی هوایی ارتش ایران شامگاه گذشته مواضع گروه‌های مسلح کُرد مخالف جمهوری اسلامی را در نزدیکی اربیل، مرکز اقلیم کردستان عراق، هدف حملات هوایی قرار داده است.
🔴
بر اساس این گزارش، بمب‌افکن‌های سوخو-۲۴  به پرواز درآمده و اهدافی را در چند کیلومتری اربیل مورد حمله قرار داده‌اند.
🔴
این حملات تنها یک روز پس از برگزاری رزمایش‌های گسترده و تمرینات آتش زنده نیروی هوایی در مناطق مرزی با عراق انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/124687" target="_blank">📅 10:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124686">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نیکزاد ، نایب رئیس مجلس: وزارت خارجه اذن تشکیل کارگروه تنگه هرمز را از رهبری گرفته بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/124686" target="_blank">📅 10:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124685">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فرمانداری دزفول: درپی امحای مهمات از ساعت ۱۰ تا ۱۲، احتمال شنیدن صدای انفجار وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/124685" target="_blank">📅 09:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124684">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXIxHkuXVQXrlfrfSI7JuHijWmIWLh6Xtthw8viWKE3YcMBDi_8XfYStxXBM8ICXLthCvEyAt5Yf1d_B9JH-_VCigdPSccRFofR69uFpf-LXw0_C8TbfUX0spi7UziHeA3bT6YSywoiTyYSjMVTRxD8IRgzwxmiypD9Fa2MxpLD69GhcBden3zTYJuvTfmRcrSD2S7xiTgb89cU0WXOreGusEgA3JvhofBb-0JXlqmdLkOi6rPQMapVevox8sxNmGRWfBKsBFXsrMbI7grPlZ27y3tN7KnjzDWFWkh8jupi-Gp_hMNoQWZDyoIOl1WD3ufYwCvgUqOKrEYES3rS6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس تهران در دقایق ابتدایی آخرین روز کاری بازار در هفته جاری ۱۷ هزار واحد رشد کرد و به تراز ۴ میلیون و ۳۶۱ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124684" target="_blank">📅 09:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124683">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4f12ee39.mp4?token=BKWkB4t6L-JPPbuNvp-yTO7AYDsm5lxoau_1ppnrZ1sk25mlgoppOwaq0DnimTjjCIVrYplbwCsCy5deN1ZVMPuwlaf71ArapRgF84MjhN4bZjz3N77UGJHLZlzINIiHB6F28UTdb5yGGa9gQ3KWcZ73ems98aZyeqgSreqfu4_FC19XXQ0swuv8fWQuuOFduKsRs-SMUCWAWqlyRRuFZCoHyzTnlOU0K3RErWuXd6M1Q9sQlGEhf0oiYjVfGRSTsdgam2b1_9k2TgoZjc2DYuJDYhZCUfN15gWz8Pj1a38V2jGrM8-CSrv3REueoVv8HybneV2bxO8r4Gj3668s2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4f12ee39.mp4?token=BKWkB4t6L-JPPbuNvp-yTO7AYDsm5lxoau_1ppnrZ1sk25mlgoppOwaq0DnimTjjCIVrYplbwCsCy5deN1ZVMPuwlaf71ArapRgF84MjhN4bZjz3N77UGJHLZlzINIiHB6F28UTdb5yGGa9gQ3KWcZ73ems98aZyeqgSreqfu4_FC19XXQ0swuv8fWQuuOFduKsRs-SMUCWAWqlyRRuFZCoHyzTnlOU0K3RErWuXd6M1Q9sQlGEhf0oiYjVfGRSTsdgam2b1_9k2TgoZjc2DYuJDYhZCUfN15gWz8Pj1a38V2jGrM8-CSrv3REueoVv8HybneV2bxO8r4Gj3668s2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساعتی قبل، حمله پهپادهای اوکراین به سن پترزبورگ
✅
@AloNews
خبرر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/124683" target="_blank">📅 09:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124682">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سازمان هواپیمایی کشوری کویت همچنین مدعی شد که هدف قرار گرفتن فرودگاه کویت منجر به مجروح شدن تعدادی از افراد و وارد آمدن خسارت‌های شدید به برخی از تاسیسات آن شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124682" target="_blank">📅 09:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124681">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نیویورک پست: خلبانی که در ایران سقوط کرد و‌ نجات یافت همان خلبانی بوده که در کویت و بر اثر آتش خودی سقوط کرده بود. دو سقوط در ۴ هفته!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124681" target="_blank">📅 09:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124680">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ix2xlhS3bn1-yHueMHxIV1LUhuV-86caJp_MpVV6BqrzRutrJ8lNWFIabJahmAct4NTuYnH-IJCItmqP3ElK6GA01X8Z39ECeJb1Op6QD36YM9UOd0c44qaRoiFXFvq4slEWQ1hYFAns0gkykWgIy4cMXBO08OTKjy-r0jVaXrA3bU5LYwldhZrXIL3SF9NAZbMH0RvKc6lAxTSB1l7SvNgH_pt7LfQQhLEH4KdeHRCKaUhvRVjt49CAv8GKdcPjBOUV8hO4YTMnyxMRijHi0oT2FJQBSJDjf3nFbVDIbzwcAsWAcYD6CzprxhIEBdB-Zo6DKY3ZNysJreJ6CZ0YdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله گسترده روسیه به کی‌اف و دیگر مناطق اوکراین دست‌کم ۲۲کشته و بیش از ۱۰۰زخمی برجای گذاشت و هزاران نفر به مترو پناه بردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/124680" target="_blank">📅 09:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124679">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/172cd75cc3.mp4?token=PnQ9-zz35JtuZ2ZBE3ZhooUJzHH5GIl02KRsbKnBv78L5emS-ZMCz_-NtpjDmdawRuXaA_D2JIkIn_YLq1u5MWc8I3Fup1oAP8-_ByNi-dMBhF4K7O6kblhv-EAdVq2uiDY40ChEAd2wjXjHUtNRwUsbA7PHldpfRwie8Ot4HZmx9gYjf1YFvz_Q0q1JWMujm-5Kr7gdCmZnGqviJGh7-E3jVnMtoMMWia365NrS35BOmYrLhDoIeQgiTJ4pinRQq7xE-Pw3BbDH6D9TJsV2BoyQK3a2RVjo5ZOSYQ2kJBgcwzUm_G9ptIwZ0WrlxRGnhgbUxA8Hyw6JlgvbusdDUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/172cd75cc3.mp4?token=PnQ9-zz35JtuZ2ZBE3ZhooUJzHH5GIl02KRsbKnBv78L5emS-ZMCz_-NtpjDmdawRuXaA_D2JIkIn_YLq1u5MWc8I3Fup1oAP8-_ByNi-dMBhF4K7O6kblhv-EAdVq2uiDY40ChEAd2wjXjHUtNRwUsbA7PHldpfRwie8Ot4HZmx9gYjf1YFvz_Q0q1JWMujm-5Kr7gdCmZnGqviJGh7-E3jVnMtoMMWia365NrS35BOmYrLhDoIeQgiTJ4pinRQq7xE-Pw3BbDH6D9TJsV2BoyQK3a2RVjo5ZOSYQ2kJBgcwzUm_G9ptIwZ0WrlxRGnhgbUxA8Hyw6JlgvbusdDUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوثری: آمریکایی‌ها جز زور متوجه چیز دیگری نمی‌شوند
🔴
عضو کمیسیون امنیت ملی مجلس: برخورد با آمریکایی‌ها باید تشدید شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124679" target="_blank">📅 09:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124678">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq1o1un1yPqwaiRWIgOnpxHuONbLLDwvzhaHINe8zwokWZqWLSL6aKbD1D63iEMrQD9g8xjfR3yks_RrNpXU82plYS4G5Z4WScLZ5JQJEu_AksyPJv_rDtv0npU15nrcbE3CSTc6lZGTUXlEHVMHvFyqDCNX4DHhWh5LBcy-LHJLWWoLZUdq8WL80M96e62NA1C1xuZ7wonV8Y4js9w1JBagya_58b8x-GaKFt6tmXwDuog2W46X42EmgpT8k2AKTqHzd97srptmD57QrMSzSeOqEWGchkrzfVSOHvjam_0y-IezN5eA8Gp7tf1mzgbADIxip5HklKaDp1ENXXi_3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی شهر تهران:
ساعت ۳ دقیقه بامداد امروز حادثه خودرویی در زیر پل استخر محله تهرانپارس به سامانه ۱۲۵ اعلام شد.
🔴
آتش‌نشانان پس از حضور در محل مشاهده کردند یک دستگاه خودروی MVM با دو سرنشین که در روی پل در حال عبور بودند، به دلیل نامشخصی با گاردریل‌های پل برخورد کرده است.
🔴
پس از حضور عوامل اورژانس مشخص شد که متأسفانه هر دو سرنشین جان خود را از دست داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/124678" target="_blank">📅 09:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124677">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
حمله اسرائیل به حومه بلعت در بخش مرجعیون در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/124677" target="_blank">📅 09:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124676">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
روایت سی‌ان‌ان از درگیری شب گذشته ایران و آمریکا در خلیج فارس
🔴
ایالات متحده و ایران در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
🔴
به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
🔴
در پاسخ، ایران اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
🔴
اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ایران را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ایران به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
🔴
ایران اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124676" target="_blank">📅 09:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124675">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده در محدوده جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124675" target="_blank">📅 09:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124674">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8556c515f.mp4?token=lSYXIrRIAt9tiDsay8r_fLxeeN6fT5rJy1joDjQQ5TlDJeIHLcOxHnoIZoVzqarpWgPZ-EWIVMrUcC8trbb1sfosNd1q7CmPU7ExvJW8ck0tXu2uJGUK2S75HiXicRJhA3uJ9Ar4Q5XDsvVpDdMAOc-kQFt-96_lfTtFzKDMcfqSspV1eNk3x3YtncOGtbzyuTy9kWGI4x2VIy3W5mbcGNOPXG3Om17dRd6z9MRPEjIkKo8e5yRiTS2pbU2G6nnG1uRsrjat1wG1yHiQWiOqBMHmIQb1G8SutFFYry8KbCCVQnv-CN3r5t2cChu3LG__FjrBSx-fCd_nUPGsWDCRUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8556c515f.mp4?token=lSYXIrRIAt9tiDsay8r_fLxeeN6fT5rJy1joDjQQ5TlDJeIHLcOxHnoIZoVzqarpWgPZ-EWIVMrUcC8trbb1sfosNd1q7CmPU7ExvJW8ck0tXu2uJGUK2S75HiXicRJhA3uJ9Ar4Q5XDsvVpDdMAOc-kQFt-96_lfTtFzKDMcfqSspV1eNk3x3YtncOGtbzyuTy9kWGI4x2VIy3W5mbcGNOPXG3Om17dRd6z9MRPEjIkKo8e5yRiTS2pbU2G6nnG1uRsrjat1wG1yHiQWiOqBMHmIQb1G8SutFFYry8KbCCVQnv-CN3r5t2cChu3LG__FjrBSx-fCd_nUPGsWDCRUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی آتش‌نشانی: صبح امروز خودروی نیسان در حال سوخت‌گیری در جایگاه سوخت گاز واقع در بزرگراه یاسینی بود که به‌دلایل نامشخص دچار انفجار شد.
🔴
در این حادثه دو نفر مصدوم شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124674" target="_blank">📅 09:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124673">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvsrR-wMOhKuQiaPqLvE_TkGkRZXoo_NKofPzzXZnxAB1ZxzmS3NLU-D-D5waJckY2yHLsyRTGfcm1GYKGs4OXEJi-FaAMTzZD9W9XEXAApeMVn-v6-fVlcb8LzwyRrtJiPseELT-uhPpDs4vnEO4mTMrST2de2RdxXA5xaYrOFJXDN8fBr6caDGywpvpqkkSyUFD-12pfTB_D_77A_WFgfhqGMxHe11VQUeMUiPAptHjOPxaMTXUAURsjEnIDnp4E24WErOoaIKfCx9qoVz6-J1bFKiQGnjTq_-HWXZjL0gMbDxJXCJSbPdnAruufnpzq6epEvGhVWDa6HeFhcETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124673" target="_blank">📅 09:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124672">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ea3b0851.mp4?token=V7SPxsXORw6_EQEYUtF6p1tkHgLwNV1ClUyp57vgrJuzuMdrHUPemorVv6nysbtX6VXNSO1WPVG6_Z3wuxh48uZo-HWg59MLpf6tXxmDLeu_-Onb5YTeCN5ehs3iT3FWSBJFzSCbE6i7qLSulpTOin5LjvYoTY-x93rb8vRtFObUd_mW-mRzG8MdkIa2v0V5TcQV7XzagEkSZSYhHLP6HoXNQizQanzP19IOdcVF6iZPnj4k593_-Fq2btWoYjlFeKigMc0vrs8Z20FNFT8L0HOzo-O16MAuCHF7ViWcQVSgnutkB-sk9nFxijq3vs0JO_7Nu_tPki5INW4MsVfblQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ea3b0851.mp4?token=V7SPxsXORw6_EQEYUtF6p1tkHgLwNV1ClUyp57vgrJuzuMdrHUPemorVv6nysbtX6VXNSO1WPVG6_Z3wuxh48uZo-HWg59MLpf6tXxmDLeu_-Onb5YTeCN5ehs3iT3FWSBJFzSCbE6i7qLSulpTOin5LjvYoTY-x93rb8vRtFObUd_mW-mRzG8MdkIa2v0V5TcQV7XzagEkSZSYhHLP6HoXNQizQanzP19IOdcVF6iZPnj4k593_-Fq2btWoYjlFeKigMc0vrs8Z20FNFT8L0HOzo-O16MAuCHF7ViWcQVSgnutkB-sk9nFxijq3vs0JO_7Nu_tPki5INW4MsVfblQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصادف در خیابان های کویت بر اثر تماشای موشکهای سپاه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124672" target="_blank">📅 08:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124669">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d64d3e9109.mp4?token=hFzIbEI5OyYhvzxG_TV-skxb1wysCfvjmc_5GQ677yBs0wJ0KUcWswidAZP83SmOjqfxLzREyTMoRd4_QHQotktUnByAoXYM7PZwkBlDYgbqHL9RZmJ8__CCddylPJyMfU3us8ERmCn3ERHxb1as9fnEPyZlCdmjq3bnt7mFR3T_2jXq0R6VlqpSoydgolQObVqma2FjnXVFi5PJBFC8KlUfyBEdSvzjUOOl0w2DAk6xgHlgQdtK0rN8uNYDQRcidq9brHasj1Yq2eMEvFBUij5XZdYXIZL0nDX3xVc56AhNsDrX9qKxInDRyp7L5VfHEAil5ILkyJDyByV3RBLIgw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d64d3e9109.mp4?token=hFzIbEI5OyYhvzxG_TV-skxb1wysCfvjmc_5GQ677yBs0wJ0KUcWswidAZP83SmOjqfxLzREyTMoRd4_QHQotktUnByAoXYM7PZwkBlDYgbqHL9RZmJ8__CCddylPJyMfU3us8ERmCn3ERHxb1as9fnEPyZlCdmjq3bnt7mFR3T_2jXq0R6VlqpSoydgolQObVqma2FjnXVFi5PJBFC8KlUfyBEdSvzjUOOl0w2DAk6xgHlgQdtK0rN8uNYDQRcidq9brHasj1Yq2eMEvFBUij5XZdYXIZL0nDX3xVc56AhNsDrX9qKxInDRyp7L5VfHEAil5ILkyJDyByV3RBLIgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب ، حمله‌های ارتش اوکراین به روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124669" target="_blank">📅 08:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124668">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FELQ_zqskKwOsiISIM_kYizfYAZGArlSewpVcqDBR51KGsTnreM2P9LeAIQDaEgCEEZ62Ex9sVENlVtEZw3X57V3QrZwQb6k_mDPzkrF8eNEsFGJtB-ftAyXUfCVY9y-OEXO03t_1CBAqygZ4wAE4wI_IxIUUXSZKpCeBdjZX8mq2npC5teruMx-F8QtTyASUsA9mdjiVFZYluDd0ceo0BWjhw3t49ZuHaTU44LkAqrOrQhdI40BChctJ2Dj2fmtckOaXSKf83jvGNBz1eDnVgOcFikpFJeuqSMlukzQO3lpKphNcooKC3bU1kBePA1EykxVQYXqAt0gdb-8_KRVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک اطلاعیه پرواز (NOTAM) در اربیل که در روز یکشنبه صادر شده است، قرار است در صبح روز سه‌شنبه از ساعت ۰۷:۰۰ تا ۱۰:۰۰ به وقت محلی اجرا شود. دلیل ذکر شده یک تمرین نظامی است که به دلیل ماهیت از پیش برنامه‌ریزی شده‌ی آن، احتمالاً صحیح است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124668" target="_blank">📅 08:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124667">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7930d04e12.mp4?token=hTMt5LWVz_GYoWCngZognXvMe43VjfqdCgJLPIaokPx6sansTtMw1lO6xbfAbn_T3WgdV9U_qoX5B5Iu9MSjcN9fvr6kDTZJiELxY2N_Ni51A7FRNCiQgKwDxA5vh9ZfPcd2HiA8va-nZp7mHYRaYlIdXTeZNiNVgVMo4vLFYk5vV_hMWBUHFtGc0W4vgPahG1C2xbY2h1ji6m-83DdfrGB4st2eM0SVy3yCxUVJsDveSZ8TiBBdWTy_-5bKGuDDPGABfojrfLXhYaQXHo_T8MwUilvPkuXSuWhxhS8dzd_-IyvNeTXr1BfrRDm1leZ9aSnVpR67fK1i0BACX-x_7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7930d04e12.mp4?token=hTMt5LWVz_GYoWCngZognXvMe43VjfqdCgJLPIaokPx6sansTtMw1lO6xbfAbn_T3WgdV9U_qoX5B5Iu9MSjcN9fvr6kDTZJiELxY2N_Ni51A7FRNCiQgKwDxA5vh9ZfPcd2HiA8va-nZp7mHYRaYlIdXTeZNiNVgVMo4vLFYk5vV_hMWBUHFtGc0W4vgPahG1C2xbY2h1ji6m-83DdfrGB4st2eM0SVy3yCxUVJsDveSZ8TiBBdWTy_-5bKGuDDPGABfojrfLXhYaQXHo_T8MwUilvPkuXSuWhxhS8dzd_-IyvNeTXr1BfrRDm1leZ9aSnVpR67fK1i0BACX-x_7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر تکمیلی از رهگیر شکست خورده موشک در کویت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/124667" target="_blank">📅 08:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124666">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=RPNJVtDgAkF8A-0WySahR81dnxy23HfcrhG3T031fuHRxPgafZXIz9-udfBvMdBZZAQPLXPUQT34Y7HhBAX9F1Zg6fgRr8wOPkVZ9w4nG_jP7s39GecnIwNHRqcQNKy6ZPvmLW9n9p34tUAYQTT0VZb26e2x2t8FfXFydBJUGlx9ULnyByvyeziTpTOSl0JPx1xm98uuO3edLeyXawgQftdxA9ITCK6CtnOzX_nFe4bIs3HEeI_95trbm3zBwS-g2IT-3ccDxW42ssCVVL2knz22DnZU59MSolGVfRmGJ_dSxfLXegGRANh0nUhL0wouNhaOHGInggtjDfP4A4b_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=RPNJVtDgAkF8A-0WySahR81dnxy23HfcrhG3T031fuHRxPgafZXIz9-udfBvMdBZZAQPLXPUQT34Y7HhBAX9F1Zg6fgRr8wOPkVZ9w4nG_jP7s39GecnIwNHRqcQNKy6ZPvmLW9n9p34tUAYQTT0VZb26e2x2t8FfXFydBJUGlx9ULnyByvyeziTpTOSl0JPx1xm98uuO3edLeyXawgQftdxA9ITCK6CtnOzX_nFe4bIs3HEeI_95trbm3zBwS-g2IT-3ccDxW42ssCVVL2knz22DnZU59MSolGVfRmGJ_dSxfLXegGRANh0nUhL0wouNhaOHGInggtjDfP4A4b_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/124666" target="_blank">📅 08:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124665">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سنتکام: آتش‌بس همچنان برقرار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124665" target="_blank">📅 08:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124664">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رسانه‌های عربی از توقف کامل فعالیت فرودگاه‌ها و تمام پروازها در بحرین، کویت و امارات متحده عربی به دنبال وقوع حملات هوایی خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124664" target="_blank">📅 08:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124663">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OheoOQR-xlwjUWqNX_H2n3YUvypuaWS7CoTAZAAZRDHDpNsRA6oe5yG_w_HSCzSQP5d2lFTI6Qk0Cw_UhAoqiaJAZfamgB2Sw1z7Yp6FSgzoK8diosvJgxAwCC8JBBMo6x5qITjNUj0vdxHFGTR_XGwUpstBalnobJCfv-FZ8ZGsRXRK3aQzwsodx7DlIhwmTSLGuQLtmysyrGAqDB5BilAkmfK8aHbZokSPjwbz527nW_ZHNTUCN0zBJyazVyYZmGMW1ODCubeKT2F6TT_uUN2hBs4YG9QqwzXKW01jbDdel7MTeaZLlCqjrqSmtc_ZGpBXJl0YkQz4BgbRy9zzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) گزارش‌ها درباره اصابت حملات ایران به مقر ناوگان پنجم آمریکا در بحرین را تکذیب کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/124663" target="_blank">📅 08:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124662">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وال استریت ژورنال: حمله سنتکام به جزیره قشم، قیمت نفت را صعودی کرد و چشم‌انداز بازگشایی تنگه هرمز را کمرنگ ساخت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/124662" target="_blank">📅 08:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124661">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QN6b6u09zMzaZmGa3veara_QdJ0h6slOnB0H7pFHnHtECzKDgQQIpFKZ48mQdS58rzIW0YRYcyNCD_HMy1zykkRWQfaFjpLMVNu8N37nTl2mzdfMAbt2omuDP0V-6KTGqG2dtgsS1AL5e6ya9c6fXc8IwpmppKt0YHYMOftkOxHjQS1ee9CgIM1FoMiTzmTwuerjiG45A-k7YNM9rjrN5jFyb0fI6-oGxDj1JA-xOMVyz8eoX9Evfuh0_hJmWyCzjCk5hJWiRmjKlq1Od4z8ciESgDHUjC-SlDKZJdThc2TGRKLzuJRlP-5mRcXPT4yULHMMUq-26ecPceQWvdCrig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی هر بشکه نفت برنت از ۹۷ دلار فراتر رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/124661" target="_blank">📅 08:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124660">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ddbf62de1.mp4?token=TeFZDB8lnEvlJbiCrZfm4DnyKBCFkRtfG_8WqJv0MRw8LxnfTYjoWy_Aa-IC3dwLV8h3w7jLPUab200hVOLz5-mfRdfCNUZVBA6SnUwSByaKK76kDa9zPLsoV5vzfBuUHAjs9cBoYEwjPZn4ug7iq6MHna-ScAQx6Rk5qgnahp4JlOWc2I83rn5vzqdqOXUKa76lLkoYCYWw0gto_0l3KpTi2mvuJyaiQY4pyDRszktYzbyI-pX2uCZQwiN1Rky3Gj8T3tgaR4DGlePvFRhwzMn65IopSPpwDW9xF1Zh015DOsuVto01yigKt3a6DrRfYUmpaaYsKFnvGJqRzFCu2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ddbf62de1.mp4?token=TeFZDB8lnEvlJbiCrZfm4DnyKBCFkRtfG_8WqJv0MRw8LxnfTYjoWy_Aa-IC3dwLV8h3w7jLPUab200hVOLz5-mfRdfCNUZVBA6SnUwSByaKK76kDa9zPLsoV5vzfBuUHAjs9cBoYEwjPZn4ug7iq6MHna-ScAQx6Rk5qgnahp4JlOWc2I83rn5vzqdqOXUKa76lLkoYCYWw0gto_0l3KpTi2mvuJyaiQY4pyDRszktYzbyI-pX2uCZQwiN1Rky3Gj8T3tgaR4DGlePvFRhwzMn65IopSPpwDW9xF1Zh015DOsuVto01yigKt3a6DrRfYUmpaaYsKFnvGJqRzFCu2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما: کوروش و ایران باستان تخیلی هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/124660" target="_blank">📅 07:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124659">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDmTBRPi2sP7DjShBZOmrWE2EtSwfCD03OUa6QCR5QA77dlygGwzrB7h10DtfDjvk8vp6_Pevp7rNvg4VRrNiZqKLUVCh4HJ55x_Byd8cpo7nb3zHkkW_nnbf3wfzOSWhchTnuVNXz5sDZVRea9Ann7UcAYW-3NQ2XZT9KUccbXG_b36p-KXy9aXATPSPmBiWlOgOKCL2sLH1Kh2hvnB6JN020b7JPn4_C1ifdwBf0ncQB3VH8liAxSEQRuGkAoN6F1NyYE6jVCPqhbJiVUypm8SLQsHmgt50b-IJLJDPH4YaZSzyC9kCKsyCfhlfodEMzkIGvPcha0awvWcfzefUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/124659" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124658">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رسانه‌های عربی می‌گویند که حملات موشکی و پهپادی به محل استقرار نظامیان آمریکایی در کویت و بحرین ادامه داشته و آژیرهای هشدار قطع نمی‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/124658" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124657">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/655265e96e.mp4?token=h-MYqbHpe333H7g9k1IhvLis6azSvSHgauirgqLb_E-kGz6I6tOMfcx1L0to8g-mC_j4uYABS-UIGOvcoLmm9ZdO33VAc22sPqiO3gbT0Nc_yD6Frh1mJBN_8f814a5aLg76m09I6YXxIV90edyZvJroaTILum2knfznp1m3OU5c83n1IJazgLoQvfdlcp8tciB1pAgoSpJzlcT1DcGHfPL8p2KpcnIa71kROigpHsecAwJAT8Kax4OCRsoprKVfQJQO3AOgYw1zUBMlTTFAH5DBpH78qvZ_3x9s1dzXJa8uTemKYHYUoOtqPXrEw6MD5QY2vLBpdRtkbzOn8GYWkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/655265e96e.mp4?token=h-MYqbHpe333H7g9k1IhvLis6azSvSHgauirgqLb_E-kGz6I6tOMfcx1L0to8g-mC_j4uYABS-UIGOvcoLmm9ZdO33VAc22sPqiO3gbT0Nc_yD6Frh1mJBN_8f814a5aLg76m09I6YXxIV90edyZvJroaTILum2knfznp1m3OU5c83n1IJazgLoQvfdlcp8tciB1pAgoSpJzlcT1DcGHfPL8p2KpcnIa71kROigpHsecAwJAT8Kax4OCRsoprKVfQJQO3AOgYw1zUBMlTTFAH5DBpH78qvZ_3x9s1dzXJa8uTemKYHYUoOtqPXrEw6MD5QY2vLBpdRtkbzOn8GYWkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدای پهپادهای شاهد-۱۳۶ در آسمان بحرین شنیده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/124657" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124656">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
جت های اسرائیلی بر فراز بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/124656" target="_blank">📅 02:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124655">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گزارش از حملات متداوم سپاه به بحرین؛ کویت و کردستان عراق ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/124655" target="_blank">📅 02:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124654">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تاکنون ۸ انفجار در بحرین گزارش شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/124654" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124653">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
آژیر هشدای موشکی در بحرین مجدد به صدا درآمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/124653" target="_blank">📅 02:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124652">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dfa8aff350.mp4?token=e76Ytlqgiv7oX1Lr8fNhKrcrR9jvQ9SciQD4aKCDAWjuUNUXQqdjfiwAqIiIPhIvMfGzh7p8h4draUFZUOfXKluVhzEYXkP5QdWPQ3uV7jUT4afiYIMpgNrtoGwJpMP05MRLTg0jSVLmVg1VqW9CK3NqKLXPysoMhcyjmBG-AwpAvK3CD0PQq8QFWu1ig_JdaDEDl9jrAPvULzCclA4bHmkaa3RTSs52yG3TdjK2vdioQLLaMIo66TRs418rUqGxtR7puqy3jIGWwBYCup6yl9NW5Su4cSKDxahYaMCU0KIbM3sRBZwtH_HzcO_aMY1U29nHO_OmX40sK4jLsgj7_J_eNN6Vku8t99eeQPqf1YXk1RRSZOWyhhEU-1vCQPAcS2FEZU5r_leMuJ55HDkYTlwnXAh6pDYdESoAuAzcJNm0ebl48GSCb8YmpR24RCyXQWEpe7LL5ifxmnT65MlW2JyKjcQ6qy0cMLpx5fO_nd2gt83VyyguPtKJrknAyT_Llt-NCVuTQRMic5-K77NJLV8MUat91xQz5-mAXXNEx2g_VmeG5HbiNDNEja0EIv2IBYxhfBjdLObBt21LDjJIPTHttT1mSHvpbRYLVp9Xe0Hma_1wjYmu34ioFDdHup6HlJ-tbsl3wG83oArthCRin4loVy2kPTI06znBkjaR004" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dfa8aff350.mp4?token=e76Ytlqgiv7oX1Lr8fNhKrcrR9jvQ9SciQD4aKCDAWjuUNUXQqdjfiwAqIiIPhIvMfGzh7p8h4draUFZUOfXKluVhzEYXkP5QdWPQ3uV7jUT4afiYIMpgNrtoGwJpMP05MRLTg0jSVLmVg1VqW9CK3NqKLXPysoMhcyjmBG-AwpAvK3CD0PQq8QFWu1ig_JdaDEDl9jrAPvULzCclA4bHmkaa3RTSs52yG3TdjK2vdioQLLaMIo66TRs418rUqGxtR7puqy3jIGWwBYCup6yl9NW5Su4cSKDxahYaMCU0KIbM3sRBZwtH_HzcO_aMY1U29nHO_OmX40sK4jLsgj7_J_eNN6Vku8t99eeQPqf1YXk1RRSZOWyhhEU-1vCQPAcS2FEZU5r_leMuJ55HDkYTlwnXAh6pDYdESoAuAzcJNm0ebl48GSCb8YmpR24RCyXQWEpe7LL5ifxmnT65MlW2JyKjcQ6qy0cMLpx5fO_nd2gt83VyyguPtKJrknAyT_Llt-NCVuTQRMic5-K77NJLV8MUat91xQz5-mAXXNEx2g_VmeG5HbiNDNEja0EIv2IBYxhfBjdLObBt21LDjJIPTHttT1mSHvpbRYLVp9Xe0Hma_1wjYmu34ioFDdHup6HlJ-tbsl3wG83oArthCRin4loVy2kPTI06znBkjaR004" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله به بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/124652" target="_blank">📅 02:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124651">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
بیانیه صادر شده از سوی فرماندهی سپاه پاسداران انقلاب اسلامی:
🔴
بسم الله الرحمن الرحیم
﴿قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ﴾
(خداوند بزرگ و بلندمرتبه راست گفته است)
ای فرزندان آزاد امت اسلامی و مردم مقاوم و سربلند ایران:
🔴
در پاسخ به گستاخی و تجاوز آشکاری که نیروهای تروریستی آمریکایی با هدف قرار دادن حاکمیت ملی جمهوری اسلامی ایران در جزیره عزیز "قشم" مرتکب شدند، نیروی هوافضای سپاه پاسداران انقلاب اسلامی، به فضل خدا و یاری او و وفاداری به عهد خود در حفاظت از خاک وطن، با حملات دقیق و متمرکز موشکی، پایگاه‌های نظامی اشغالگران آمریکایی در کشور کویت را هدف قرار داد که منجر به نابودی موفقیت‌آمیز اهداف و شعله‌ور شدن آتش در دژهای متجاوزان شد.
🔴
سپاه پاسداران انقلاب اسلامی ضمن اعلام این پاسخ اولیه برای ضربه زدن دو برابر، هشدار شدیداللحن و قاطعانه‌ای به دولت آمریکا و رأس استکبار جهانی و هر کسی که اجازه استفاده از خاک یا آسمان خود را برای آغاز تجاوز علیه ایران می‌دهد، می‌دهد:
🔴
هر حماقت جدید، تجاوز دیگر یا حرکتی که حتی یک وجب از مرزها و حاکمیت ما را لمس کند، با پاسخی لرزه‌انگیز، خردکننده و قاطع مواجه خواهد شد که از قواعد و مرزهای معمول فراتر خواهد رفت و نیروهای شجاع ما در تبدیل تمام مقرهای متجاوزان و منافعشان در منطقه به خاکستر تردید نخواهند کرد.
🔴
زمان "بزن و فرار کن" به پایان رسیده است و نیروهای ستمگر باید عواقب وخیم نادانی و ماجراجویی‌های بی‌محاسبه خود را بپذیرند.
﴿وَمَا النَّصْرُ إِلَّا مِنْ عِنْدِ اللَّهِ الْعَزِيزِ الْحَكِيمِ﴾
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/124651" target="_blank">📅 02:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124650">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
این نخستین تشدید تنش بزرگ از سوی ایران از زمان آتش‌بس است که به‌طور هم‌زمان سه کشور مختلف را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/124650" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124649">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/868e61e684.mp4?token=ru27l1WTVWR1BXDQe6D4061m_tYUSV6lbMeyKDz9rBH6kdNLOh_iMcYWZ-_uTKiTiwx_fC6WQq0ejhZ-FlW4QBbi565IRqAVeI9sYLcLKRzSvlBIoVMACTh3T2KCEPpByp8SBEpNwv699CHzK9gqG2inwWtSNqLKSMiVKggzMt4qYrW20MFkcStJw-wOJ9ML1pR1UcYwYSEw6AbHajHY2pUEciKcbmldbOf_9OHWw2l8p1r2p0gTBs2xwXSRU_DTKXJ23lQ1SUHneG5hc3cPFyxxdmktKc1FBDDvieJljIpT_PcattlCKikF5TrDuXQ_Fjg9V8w8jRmzr19Wcioj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/868e61e684.mp4?token=ru27l1WTVWR1BXDQe6D4061m_tYUSV6lbMeyKDz9rBH6kdNLOh_iMcYWZ-_uTKiTiwx_fC6WQq0ejhZ-FlW4QBbi565IRqAVeI9sYLcLKRzSvlBIoVMACTh3T2KCEPpByp8SBEpNwv699CHzK9gqG2inwWtSNqLKSMiVKggzMt4qYrW20MFkcStJw-wOJ9ML1pR1UcYwYSEw6AbHajHY2pUEciKcbmldbOf_9OHWw2l8p1r2p0gTBs2xwXSRU_DTKXJ23lQ1SUHneG5hc3cPFyxxdmktKc1FBDDvieJljIpT_PcattlCKikF5TrDuXQ_Fjg9V8w8jRmzr19Wcioj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسمان
بحرین.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/124649" target="_blank">📅 02:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124648">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
حمله موشکی ایران از استان بوشهر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/124648" target="_blank">📅 02:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124647">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سامانه‌های پدافند هوایی در بحرین فعال شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/124647" target="_blank">📅 02:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124646">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شلیک موشک به سمت پایگاه‌ آمریکا در بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/124646" target="_blank">📅 02:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124645">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KH8zgpqxC99kJ-QRi-8krZJo3J3DfEOmm0-w86CGpB75D1Ifwb_L4PDidXLUTab2989XELssAC33MoBW09ZCWiV4w5Jjc-QPeerK3xKew6zoLthcjWkIh9EWOT8_K2lzZrkTI1mVFV4wLWoEihmPiVY-TYaQZZQo9K1N2P33ZG1EZkDmC9X2OB9t__zhEpqAMu7ylWFym3gBs4mmh213BY7DYhhJNc8DTk-IkznM01XDjDr5Eng4JUkHaO7lqwiDB1xOTpERfdBRFoDs42EomKmFep0a_hyGj4PEaBLxCAE4S0mSWP6MAKVvRM-7fEg1w4Jpeu4UHsQUFsZ8b3YImg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/124645" target="_blank">📅 02:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124644">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
تا این لحظه حداقل پنج موشک به سمت کویت شلیک شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/124644" target="_blank">📅 02:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124643">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
مهر: یک پرتابه به ساحل ایران برخورد کرد
خبرگزاری مهر گزارش داد یک پرتابه در محدوده ساحلی بین شهر سوزا و روستای ماسان برخورد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/124643" target="_blank">📅 02:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124642">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سه انفجار دیگر در کویت گزارش شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/124642" target="_blank">📅 02:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124641">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d3ab2f07.mp4?token=FFFwSbpWUdgjpQ2CFmzu1zNeomRS1Sn6-_IgI_2dDVQoX2v2W5TU7yK1g4wo57qU0NJ6xSSEz1GNH5I_obAIhks3wCGzhATKmy1QHis4pSU1FF2V99mVzbl9FsxMc5_f23hG1HJkVE7t8ydzY20usZMYmcMa3GQGkzNfi9Yvlivr9FnvxGE7lXBCqiiM8fWFRxkyGK80jai1PWc7JHV9Wzrc8BOslI8BuImJVd9kM8MDWQJKpkC_kU0CUhXekxq-LOYL4RdtUIzS4sQXSuRC1IxNNB7SIfxU-fpWWgTE0vWaz_drajPel35WJFqDAEt4rGqatCPW5b-IGMI-dvaXWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d3ab2f07.mp4?token=FFFwSbpWUdgjpQ2CFmzu1zNeomRS1Sn6-_IgI_2dDVQoX2v2W5TU7yK1g4wo57qU0NJ6xSSEz1GNH5I_obAIhks3wCGzhATKmy1QHis4pSU1FF2V99mVzbl9FsxMc5_f23hG1HJkVE7t8ydzY20usZMYmcMa3GQGkzNfi9Yvlivr9FnvxGE7lXBCqiiM8fWFRxkyGK80jai1PWc7JHV9Wzrc8BOslI8BuImJVd9kM8MDWQJKpkC_kU0CUhXekxq-LOYL4RdtUIzS4sQXSuRC1IxNNB7SIfxU-fpWWgTE0vWaz_drajPel35WJFqDAEt4rGqatCPW5b-IGMI-dvaXWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه راننده کویتی از ترس صدای موشک رفت تو بلوار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/124641" target="_blank">📅 02:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124640">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">💢
فووووووووووووووری/همین الان چند جنگنده آمریکایی در مرز ایران درحال پرواز هستن
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/124640" target="_blank">📅 02:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124639">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آژیرهای هشدار در کویت بار دیگر فعال شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/124639" target="_blank">📅 02:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124637">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
اسرائیل هیوم:
سپاه پاسداران به صورت مداوم در حال شلیک پهپاد و موشک به سمت اهدافی در اربیل و کویت است و تاکنون شلیک ۲۰ پرتابه تایید شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/124637" target="_blank">📅 02:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124636">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArnLiLICV4MKJad95HAHx5OwiivRMdw2yo_TC7pjpDUTjyFYeu3Tci5RiTcxDB_Cjglq1fgSQT3aRNt2BsOu6TXLgGm9keFZ6mzP5FpqLnt5n_tm8cuqdkL2VOYX07wi1kMxrwINRbgUzrOEqivTqeknUiRg4JmqPlUN096p0vuampEBf6vBRCDyD-WuNLdHdyCxTrrndrMapLh6JqREYdMDCUVcK3QdxvTXnqLfMMIfGHDA5zKHeiOQW5dcP7WpuKBw1Z2n0X7oPNF8RMR0sZ__cG8PiTXDh5rYSmxkTXOU1JugKL-pVivA3dOCcJ40JhgwI1YhFoUyJIwYs0BrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما صدای انفجار در قشم را تایید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/124636" target="_blank">📅 02:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124635">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f746e9b10b.mp4?token=SaN9nx3uLDp1KkLPPgKm6l_wlCcmGLeZrW3zoNCesMdS893lm_uKZ0t9z4ZqNiPKBBPc7Ha5OAkOhP1Ji_r9XYmRv7nNc0kZwUfWpJZh0xi6HpvJQ5meY0VbaO0lpmvCQdw5uelfvUbjWP2Hpfyg7clU0Tikx78FYVVZdPEZ6P94VRUcmQpeYFfRqV6tudKYujQCKoRASiWeow2a1XaDIp_grfl5BN14hBkGqQCKDoeB2cBjdkkPcgNy2jHlaJxU9Hb8B82oFYMwcnAJJqalTKcGE4CCTG17Ew6JWsTqv0oNEefHqWacPANfbfHBNqodl6tjTvonwrNfkOw0vdfZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f746e9b10b.mp4?token=SaN9nx3uLDp1KkLPPgKm6l_wlCcmGLeZrW3zoNCesMdS893lm_uKZ0t9z4ZqNiPKBBPc7Ha5OAkOhP1Ji_r9XYmRv7nNc0kZwUfWpJZh0xi6HpvJQ5meY0VbaO0lpmvCQdw5uelfvUbjWP2Hpfyg7clU0Tikx78FYVVZdPEZ6P94VRUcmQpeYFfRqV6tudKYujQCKoRASiWeow2a1XaDIp_grfl5BN14hBkGqQCKDoeB2cBjdkkPcgNy2jHlaJxU9Hb8B82oFYMwcnAJJqalTKcGE4CCTG17Ew6JWsTqv0oNEefHqWacPANfbfHBNqodl6tjTvonwrNfkOw0vdfZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از تکه‌های موشک‌های رهگیر که تو کویت افتاده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/124635" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در کویت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/124634" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124632">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پرواز جنگنده های نسل ششم f4 فانتوم ارتش برفراز اهواز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/124632" target="_blank">📅 01:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124631">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ec38fee8.mp4?token=iNn0tgTi-c7X_OKaI2KEoTbZ3JubGf80qNN9itHjJZfK97F9gUB0RgJtHtictT4FJztTcE9YE5L8bzfO7Mnp7I3DkfgbMYf7XGkHszX_nD_JXiICq5dxidl9p5QILeixM8WR3BZz7MFW7P5YnPePdtRzhqK5fMuscZCszcOHj0y8aAZji8fi35S_WxeZ7oQM6nbw8r_TxDLWvGpUmzgpBvl23jt927aUc4uezGHlFhvg58I_UZ2kVfaQRjgzIbpSycOMLa8pzhDol1yDlxHijZjD-JL-SwUqTbqeQwyMCzSaZ-xtjJd4E7XSsmvzK8W-czMPV1ODU7F3z6XhAGWRsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ec38fee8.mp4?token=iNn0tgTi-c7X_OKaI2KEoTbZ3JubGf80qNN9itHjJZfK97F9gUB0RgJtHtictT4FJztTcE9YE5L8bzfO7Mnp7I3DkfgbMYf7XGkHszX_nD_JXiICq5dxidl9p5QILeixM8WR3BZz7MFW7P5YnPePdtRzhqK5fMuscZCszcOHj0y8aAZji8fi35S_WxeZ7oQM6nbw8r_TxDLWvGpUmzgpBvl23jt927aUc4uezGHlFhvg58I_UZ2kVfaQRjgzIbpSycOMLa8pzhDol1yDlxHijZjD-JL-SwUqTbqeQwyMCzSaZ-xtjJd4E7XSsmvzK8W-czMPV1ODU7F3z6XhAGWRsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسمان کویت لحظاتی قبل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/124631" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124629">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⌛️</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/124629" target="_blank">📅 01:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124628">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ادعای وب‌سایت عبری حدشوت بتخون:
🔴
نیروهای آمریکایی چندین موشک از خاک کویت به سمت جزیره قشم در ایران شلیک کردند و سپاه پاسداران ایران بلافاصله به مبدا آتش حمله کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/124628" target="_blank">📅 01:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124627">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
شاهدان عینی از کویت:
🔴
خونه ما سمت سفارت امريكا هست سفارت امريكا هم داشت موشك میخورد صداي انفجار خيلي بلندي بود.
🔴
انفجار های سنگین در منطقه سورا کویت با چشم قابل رویت بود.
🔴
همين الان اژير كويت فعال شد دوباره
٦ تا انفجار خيلي سنگين تا الان
توي اين ٣ ماه اينقد صداش سنگين نبود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/124627" target="_blank">📅 01:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124626">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6773c885.mp4?token=RGXoGcciO4Cc_8sfnmNqfl9MB5M748ElTea9gq5nnd5NLMt0s_wYbZoi4XVCV-9owcK8Fk5LS37BZhSXLZS5HevGcqMvz2fL6cdA_0l6-E_HoEtn9aSkY1u6hvzHcwwzqHHna7-WDMlf7NRgMFiMsb025hxmHw6wPbedLmjmBNMxIZv3drERR9pn-cWKbTiv7SpEH7HZJjZjoFP2hbo57q4KiYW9hX4L8Oep7b6QKg05SbD5GoaxQWij_sw_L9eiEyDa0ENcgyt2E7fOxuTTIaq0BLLcZXV3YK_I7U2DkX7ci1d8fHL2zVVwlY17DYpXujexr2N-sP2W9Rbe2eCj7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6773c885.mp4?token=RGXoGcciO4Cc_8sfnmNqfl9MB5M748ElTea9gq5nnd5NLMt0s_wYbZoi4XVCV-9owcK8Fk5LS37BZhSXLZS5HevGcqMvz2fL6cdA_0l6-E_HoEtn9aSkY1u6hvzHcwwzqHHna7-WDMlf7NRgMFiMsb025hxmHw6wPbedLmjmBNMxIZv3drERR9pn-cWKbTiv7SpEH7HZJjZjoFP2hbo57q4KiYW9hX4L8Oep7b6QKg05SbD5GoaxQWij_sw_L9eiEyDa0ENcgyt2E7fOxuTTIaq0BLLcZXV3YK_I7U2DkX7ci1d8fHL2zVVwlY17DYpXujexr2N-sP2W9Rbe2eCj7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کویت لحظاتی قبل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/124626" target="_blank">📅 01:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124625">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
گزارش العربیه: ایران در یک حمله واحد، هم پایگاه هوایی علی السالم و هم کمپ عریفجان را هدف قرار داد
🔴
ایالات متحده و ایران در روزهای اخیر حملات کوچک مقیاسی را در جزیره قشم و کویت رد و بدل کرده‌اند، اما این حمله بزرگ‌تر بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/124625" target="_blank">📅 01:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124624">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پایگاه عریفجان در جنوب کویت، نیز هدف قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/124624" target="_blank">📅 01:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124622">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5101dc61.mp4?token=O54FuY8frFYjehMtWygIFkVPSDwLOmI2x_mYUg0__-14msDdx_cKnMtholal8Q3T8PTA-4Ka-lEh6pDonU5SBZQwQf13BbswoeCDRZbS3B9q7CSLIj3Z0xGtKKwdDHTN9OrxmVJwAsr852al4YBYXvrjG7KCCm_cigQyY9NHdQ9p9_J5Kt9BM0glAWXmWawp_qiTkfqtTcQaVUwhip_UV8mMBIwq2w9tGur4H6syXp5tsuUkGgSti3nV1un8lw-e85eQfcBnihEhIARu7qiYblI7OhZDI1wkXdgW318T6PDjpXxccX-bDoXUmQcwJuMaVyr4J3aSJRJmKWO1Ds7zhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5101dc61.mp4?token=O54FuY8frFYjehMtWygIFkVPSDwLOmI2x_mYUg0__-14msDdx_cKnMtholal8Q3T8PTA-4Ka-lEh6pDonU5SBZQwQf13BbswoeCDRZbS3B9q7CSLIj3Z0xGtKKwdDHTN9OrxmVJwAsr852al4YBYXvrjG7KCCm_cigQyY9NHdQ9p9_J5Kt9BM0glAWXmWawp_qiTkfqtTcQaVUwhip_UV8mMBIwq2w9tGur4H6syXp5tsuUkGgSti3nV1un8lw-e85eQfcBnihEhIARu7qiYblI7OhZDI1wkXdgW318T6PDjpXxccX-bDoXUmQcwJuMaVyr4J3aSJRJmKWO1Ds7zhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوئی از انفجار تو کویت، و فعالیت پدافند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/124622" target="_blank">📅 01:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124621">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdtjT9r3jdia20IqAH42NljY9fvc3I4ZAsoRO5rieSo2gBYoYW047LZvYfPV9D7IciilcgH3_kZ8G4a8nTDRjIIAIZfZ_t107unZPVPIt1058jJu5nezcWv749MVjP3WYSJUX7rfxLtI5AuHicclvT9J8deltPHPGtLNPgOZKWIrsBsasF_On4ZlrG66bh50AwYL-qhRcNhE6EJvm_E833i_NEufDHhB9aZtk26or924K7rcAyGumSE3Ugh6hZ2Aj6ngCb_qNN7WYsJ39DZuA96ANyH1pjqmiRIELgu-gvgb-hkdt91ZCXC6ZYATnGIMqk1uMmwrGK1m12Saz2jcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رد شلیک موشک در آسمان شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/124621" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124620">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری/موشک‌های بالستیک ایران پایگاه هوایی علی‌السالم تو کویت رو زدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/124620" target="_blank">📅 01:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124619">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrrdgTPLl6WPnFsFaoDRjhJGHkPvOyetNLDSZ_76CG0dQJmcBKeHc47iauIiP9wt2VZLV5vqmfNJ8sRVuFlY9A6xmQAEUYUdDsDxZ0x83WN3F_L8dLIKcwq5Qx3UQNNe9QIdYMHgVTn5KOZVfbpMpFQwKu_hInVwTXAG4fnB1dIpFVuVkEAA2qF7BgBCbLGEhzznHtI5_6BNgRvTW8U8AufoFdwI7fzK881KU0K0bXnmPHGclToYwyx8ErAsRemuYZeD8wcyyvHTYVGHBQpjmAtB-eaDqOZCL4szEkbG5kbdhXFG-c-n4ZUmsfa3SM7wLxBtqBu09MuiPtc1updq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دفاع کویت :
- پدافند هوایی کویت در حال حاضر داره با حملات موشکی و پهپادیِ دشمن مقابله می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/124619" target="_blank">📅 01:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124618">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
آژیر هشدار و صدای انفجار در کویت
🔴
رسانه‌های عربی از فعال‌شدن آژیرهای هشدار در کویت و شنیده‌شدن انفجارهایی در این کشور خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/124618" target="_blank">📅 01:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124617">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در محدوده جزیره قشم
🔴
بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.
🔴
پیگیری‌ها برای کسب اطلاع از ماهیت دقیق این انفجار ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/124617" target="_blank">📅 01:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124616">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de528efdc.mp4?token=ICsEoFnVFPmb03QZ_6M--bL85O0coU4-sd4wnk8WURtQeOYKNnSi6QFA2lEl2rxz_afV2FGEe7uCbHaLOU6OodVNwGX_bsz3U8ypYpIGcYMZTqhCUPNC0J3dUE5stXdOCeSscezp7nPd-SJ4BpE3x30Wno_cJaSV6oVqerJNs7lp72v-jonehhA4g7IYLJEOH_Epa629tBkEkUgK5v4YS6ciH-CJdD7SWApt22xV_673eCvXsTaBafILwuhsclFNv9JqfUbChTm5O3z0r3Kq4aGwj8JyJhaxSh2-xbBgF-aH2Y7Tuq1CnvS1VzowUldZ0sKgBD5YfoLzJFiNTfLQgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de528efdc.mp4?token=ICsEoFnVFPmb03QZ_6M--bL85O0coU4-sd4wnk8WURtQeOYKNnSi6QFA2lEl2rxz_afV2FGEe7uCbHaLOU6OodVNwGX_bsz3U8ypYpIGcYMZTqhCUPNC0J3dUE5stXdOCeSscezp7nPd-SJ4BpE3x30Wno_cJaSV6oVqerJNs7lp72v-jonehhA4g7IYLJEOH_Epa629tBkEkUgK5v4YS6ciH-CJdD7SWApt22xV_673eCvXsTaBafILwuhsclFNv9JqfUbChTm5O3z0r3Kq4aGwj8JyJhaxSh2-xbBgF-aH2Y7Tuq1CnvS1VzowUldZ0sKgBD5YfoLzJFiNTfLQgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
امروز نیروهای آمریکایی یک نفتکش بدون بار را که در تلاش برای حرکت به سمت یک بندر ایرانی در خلیج فارس بود، از کار انداختند
🔴
فرماندهی مرکزی ایالات متحده (centcom) اقدامات محاصره‌ای را علیه نفتکش m/t lexie با پرچم بوتسوانا که در حال عبور از آب‌های بین‌المللی به سمت جزیره خارگ بود، اعمال کرد.
🔴
خدمه کشتی هشدارهای مکرر را نادیده گرفتند و چندین بار در طول ۲۴ ساعت از تبعیت از دستورات نیروهای آمریکایی خودداری کردند.
🔴
در نهایت یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت و مانع رسیدن نفتکش به ایران شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/124616" target="_blank">📅 01:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124615">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8t-iZarvpv3H1pEmyTiVbSw0vchfMmnFefKfGSS8cabvEAMG0QcuBl4TlOd6UfCBkQBncrN-pKH7UiD5IzOg5e9czSvdaddm1v9EOsy05usTO-DX5dCVBB3HrNuhpxoz5QOXDwVeoiyh_Ll6jQOVyArBYBL1nuvRGfkY-jf0_DtPW-aKxOVgpF76bM53eBOwLtB5tx6OErlTj0Epv2qyTJJG21ndd6a4Yvwetzp0eU3lROi5rH1w2bxA5L94FdKNrm6ONfYtq7n24s97TToxNphoWE9bq7q48PzAL7E2zxWmWbiRS4xA9kbu4fVQovXlzby7sIP2XtgkkuEzQ8QBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران دومین تیم پیر جام جهانی شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/124615" target="_blank">📅 01:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124614">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb87b1576.mp4?token=oGwHzbCPd631nejIMtkg7z4Z65flHZjZrTET_gAN5ozkLo6bHsOK5oKj1_opRcxnDbw0C14EUJ2UC7DXXIDpmNEyoNTeXgPjf9oUHi676CXqIx0JB7FFgkszTlUqv804fXt4QnaA2d2lbVqDHlfKlXxZO92Jyd6IbK5g5WcWU6c-ynaFiQWXnftK7XQHoXXJqIETask654Mg6M2N-JCafuwSec6KxyTRaSKJw7kjf0vFiMorv_3msfBuD60xaqztjUWy0mADZNdnPp0sPGrLEjCIjzOFj8TNgtZ35wG-AIbL4sFFvgnOs29dtBwNU0phHVolBBV0AsstYjVPme2r7BW824ozky4Qbe1bNJjWVXrS7B1PlRdifXz2N8KFW3ZoiyROTyc0oAZab_8RJqpyxjBfuNIF5RXNYOvbU2PCvZLZ9XzuEp-pTCjvGWE48Wjj-b0sW8lMVU60iFz8omvADpnNjjyKKGHikCiv5fyHVfoS2icDsQjHmao9wFpMmLkGuNWkElcFDpTWK47jlR7gAvdW4WnRK8Z4gLqxO_Jzr2CBK3ESN9XZSRQHl4-4arNmzT2VO1YqmK82k6HlrEVGKnXkE5rtcG-jjhc_9L7V_k5Bkc24SVaWjoEmFf50oSrKQpFG9eZkjXtbG7dyRL_BLt5Bdl3WZteu3_-CkiHro4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb87b1576.mp4?token=oGwHzbCPd631nejIMtkg7z4Z65flHZjZrTET_gAN5ozkLo6bHsOK5oKj1_opRcxnDbw0C14EUJ2UC7DXXIDpmNEyoNTeXgPjf9oUHi676CXqIx0JB7FFgkszTlUqv804fXt4QnaA2d2lbVqDHlfKlXxZO92Jyd6IbK5g5WcWU6c-ynaFiQWXnftK7XQHoXXJqIETask654Mg6M2N-JCafuwSec6KxyTRaSKJw7kjf0vFiMorv_3msfBuD60xaqztjUWy0mADZNdnPp0sPGrLEjCIjzOFj8TNgtZ35wG-AIbL4sFFvgnOs29dtBwNU0phHVolBBV0AsstYjVPme2r7BW824ozky4Qbe1bNJjWVXrS7B1PlRdifXz2N8KFW3ZoiyROTyc0oAZab_8RJqpyxjBfuNIF5RXNYOvbU2PCvZLZ9XzuEp-pTCjvGWE48Wjj-b0sW8lMVU60iFz8omvADpnNjjyKKGHikCiv5fyHVfoS2icDsQjHmao9wFpMmLkGuNWkElcFDpTWK47jlR7gAvdW4WnRK8Z4gLqxO_Jzr2CBK3ESN9XZSRQHl4-4arNmzT2VO1YqmK82k6HlrEVGKnXkE5rtcG-jjhc_9L7V_k5Bkc24SVaWjoEmFf50oSrKQpFG9eZkjXtbG7dyRL_BLt5Bdl3WZteu3_-CkiHro4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چرا پادشاه بریتانیا اسلام رو میراث بریتانیا میدونه؟
جواب رو از آرش اعلایی بشنویم.
🔴
نقش برادران شرلی در پیدایش و رسمی شدن مذهب شیعه در ایران.
🤔
آخوند انگلیسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/124614" target="_blank">📅 01:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124613">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
مقر گروهک‌های تجزیه‌طلب کرد هدف قرار گرفت
🔴
منابع عراقی از انفجار در یک مقر گروهک‌های کرد تجزیه‌طلب در شمال اربیل خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/124613" target="_blank">📅 01:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124612">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQlpLsCDgBs1nmtUmYLH1bW9HXCMPvZPf8hCjlegLsDL-C52IZvYtxYmZaC_MkItNBn86mJVztrW3pVXUujrESjG-8GHde8Rtoi5d3llB8dab-grvT-OuKbKon1bt7VfeMzKKfaobhylOnok30GerYl3ShMcdH5AKu5AL8ymfh8TBQzLT8u7vwTTeYWP8tE7vyICiw0Dl7wzrywfmfwQt8E7cT8xLhVuhlj7777GUpIjMMrVeZz8jADMEO27UI6dyNTi-nxAVTJHe7E9Kt4mp7H1-lB05ygoYUpsPo8vRlMkc8UbAGhzGYBPs-ds4RhpMYhFEV7pSKk0rXXmn1_DMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد ماهواره هایی که شرکت های مختلف جهان در فضا دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/124612" target="_blank">📅 00:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124611">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ادعای رسانه بریتانیایی امواج:
یک منبع ارشد سیاسی گفت که هیچ گونه قطعی در ارتباط ایران با آمریکا از طریق واسطه‌ها صورت نگرفته است.
🔴
همزمان، قطر در کنار سایر واسطه‌های منطقه‌ای، به طور فشرده در پشت صحنه کار می‌کند تا از شعله‌ور شدن دوباره جنگ بر سر لبنان جلوگیری کند.
🔴
منابع آگاه عرب و ایرانی گفته‌اند که یکی از نزدیکان نبیه بری، رئیس پارلمان لبنان، به همین منظور در دوحه به سر می‌برد.
🔴
نخست‌وزیر قطر نیز امروز با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، دیدار کرد.
🔴
این تحرکات در مسیرهای موازی اما به هم پیوسته نشان می‌دهد که ممکن است در آستانه یک تحول مهم قرار داشته باشیم.
🔴
با این حال، آنچه بیش از هر اعلامیه‌ای اهمیت خواهد داشت، اجرا و عمل به توافقات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/124611" target="_blank">📅 00:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124610">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=ikbFpJc5Ro3neyelKaVD_Snjwy305MrtzgjkeZmfv9FVm7mSlz01wBJEIRObnIF_Klzo2aC2DL8Bzoq2OOMUEgQ7vUdvXdBJzRKrA_jz9QVHFd5kmQuajmDEN0SYwEhSMr4klqgGdo-BvaHb4hZFor-DT6nDws64mb7QzTKhydxVnfdQ7fYXyyx_9P9wP9bjIag6IKwuHWBcioYwlnhVoYeq0TLwNpEhMp1bbsfIRW8-EpKc-CBSGIaFrFm5kZPTE3zzwgPclAlip1R8ztc8rw42n-DuBMwCsuHLAqhjwxSgdPnakb4yflumc4jw_ubRxlveb29Mw-YmfQ6V5_ppQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=ikbFpJc5Ro3neyelKaVD_Snjwy305MrtzgjkeZmfv9FVm7mSlz01wBJEIRObnIF_Klzo2aC2DL8Bzoq2OOMUEgQ7vUdvXdBJzRKrA_jz9QVHFd5kmQuajmDEN0SYwEhSMr4klqgGdo-BvaHb4hZFor-DT6nDws64mb7QzTKhydxVnfdQ7fYXyyx_9P9wP9bjIag6IKwuHWBcioYwlnhVoYeq0TLwNpEhMp1bbsfIRW8-EpKc-CBSGIaFrFm5kZPTE3zzwgPclAlip1R8ztc8rw42n-DuBMwCsuHLAqhjwxSgdPnakb4yflumc4jw_ubRxlveb29Mw-YmfQ6V5_ppQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش آمریکا به یک کشتی دیگر شلیک کرد.
🔴
بیانه سنتکام : تامپا، فلوریدا — نیروهای آمریکا [امروز] ۲ ژوئن یک نفتکش بدون بار را که قصد داشت به سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/124610" target="_blank">📅 00:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124609">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
توماس میسی نماینده کنگره: فقط کافی است کمک‌های خارجی به اسرائیل را به مدت یک ماه قطع کنید، آن وقت آنها بمباران همسایگانشان را متوقف می‌کنند - صلح فوری برقرار می‌شود، تنگه هرمز باز می‌شود، و قیمت بنزین در هر گالن دو دلار پایین می‌آید. اسرائیل بزرگترین دریافت‌کننده کمک‌های مالی از جیب مالیات‌دهندگان آمریکایی بوده و همچنان هم هست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/124609" target="_blank">📅 00:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124608">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b65xi_UwdTOgZfd7K4Jf6Ob4H3pycymK4ND-vtKziodR18i75D__lwiYlx14-4Wn2WHSoumti9Mbk5I7sGBbaLxH47yJmH60GaXfyHyUCG7zNsdjK_5hQYUYzl2bvyGo7GCgiZ57pkVcxrWfO9TaZzJh1DPhnSY5y7RcqgT76aYj1MqJOBp1er9TfdVuZUF2dSGgBcop-0EF7XrDM_llIO1pin72Hl6mOFkGZ6NkSoXnCS_O5NSWzjm5FTvDdtwVPj_lYLudm7kyWJzKSyAR7Nwz1MPDM0BUvnENi-5gbqG_oWUq7gB7_ba54JFI6345bPGX0BIua4MtS37apqLONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیری‌ابیانه: نتانیاهو فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد!
🔴
علت جنگ آمریکا علیه ایران این است که نتانیاهو علیه ترامپ آتو دارد و فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد و نتانیاهو این را اهرم فشار علیه ترامپ قرار داده تا هر کاری اسرائیل می‌خواهد، آمریکا انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/124608" target="_blank">📅 00:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124607">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
گلرو، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس : تیم مذاکره کننده با قدرت ایستاده تا آمریکا به خواسته هایش نرسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/124607" target="_blank">📅 00:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124606">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r93Pp1rHO0Pdo2NmgV1jXH8nTylESfjQlLjtxeNQGfdn0frbOxPDgzf_qeZL-c8_AyAiKSsMRGld_8TkJL9m9cHv_L3GM-HJWGZAhi0qeNs3TpyGQPEnz4PuumNxT44zMfEhiw0z6vqFSBvvAdFiB5KUu4J5RDLeDKTZN8DPuAxI94l1-gTImdrDEPXZON2Dkw0rnNaDEjjx3lACoYKI9watnOruWYTCFKxg0QMUnkgxC4FfRGEmUEhwnNAnXU0e_cypaFWg2lHF5oF1Q-7Tv6qjWEzxjeWCRb5zsomMNeMFwhLKTpE-KEAuQuNQ56IlFhbO0KXhdRQ0STT1MRfqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آسمان منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/124606" target="_blank">📅 00:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124605">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
الحدث: وزارت خزانه‌داری آمریکا اعلام کرد واشنگتن تحریم‌های جدیدی مرتبط با ایران را وضع کرده است که افراد و پلتفرم‌های تبادل ارز دیجیتال را هدف قرار می‌دهد.
✅
@AloNews
خبر</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/124605" target="_blank">📅 00:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124604">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رکورد تورم در ایران از زمان جنگ جهانی دوم تاکنون شکسته شد.
🔴
بر اساس داده‌های بانک مرکزی، نرخ تورم نقطه‌به‌نقطه در اردیبهشت ۱۴۰۵ به ۷۷.۲ درصد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/124604" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124603">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHuGkvh33nqmG5tKBDT4kRfgez2oye91NUTi3YQUBPnKlw6kVn9kCOCmf1a5jp8ijiqM1PmGw8MMY2w4HSqty6oRS7Ifh7hJFeUXbeNNXywsTCNe6rfdW_Tiiux5cWlaG-i_d9seB444byZ3UaYVxx784LOVPlH39ArmJGveIeXDCS8frqSnsP-3woWJUAfKwRC-TkNPuY3l9LgEwlq2oZFGlmG9KOihQU9bn4mmNPpLXoxP8kE-V7xjMmf2Pl0vDOEQcILGBG5KDHo9tYxrBjduTE_AeIBOFfWWUBdc6uIiPyQTlAZIvU_LCoDXWEukwmvsC7xJi1O5rW4OTm89OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بررسی ورود سرمایه‌گذاری خصوصی به بخش برق ونزوئلا در مجلس ملی
🔴
مجلس ملی ونزوئلا قرار است اصلاحاتی را مورد بحث و بررسی قرار دهد که در صورت تصویب، مسیر را برای ورود سرمایه‌گذاری خصوصی به بخش برق این کشور هموار می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/124603" target="_blank">📅 23:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124602">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
العربی الجدید: مذاکرات لبنان و اسرائیل در واشنگتن به پایان رسید و قرار است فردا ادامه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/124602" target="_blank">📅 23:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124601">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ریزش 2 هزار تومانی تتر در پی خبر تحریم نوبیتکس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/124601" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124600">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a44b2aef3.mp4?token=NESBo-exC6naaufoYpw_EByKNWaAB9V_CDKSI12oTyHxnGzF0cwgEwONpJgQqV0XaxjWAE-NDwXueyCkDeMKSM8i5VGcnFHYQgfd6RPQ8wyTtyscKjGhlFrushBxpl6YbnXiLWhqvHGqf2lZGfeuBo769W08aIugEA1F-fYFwJpJzukHukNKSjDPG5g4kIJm_N829SJ_EHqPEHPW8H1qzCBA-wo05-k2NX1gOfYcdJLdj_UcfOhLxftM_x3IbtEVz3Hu1yF1q7eYy7bhd2lVxcaAp26jR-7UrTUGFwK9bm4ZsVLkJ8obj-GBaBG3pUHe8STXBdq14T-2_kqTUDA8aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a44b2aef3.mp4?token=NESBo-exC6naaufoYpw_EByKNWaAB9V_CDKSI12oTyHxnGzF0cwgEwONpJgQqV0XaxjWAE-NDwXueyCkDeMKSM8i5VGcnFHYQgfd6RPQ8wyTtyscKjGhlFrushBxpl6YbnXiLWhqvHGqf2lZGfeuBo769W08aIugEA1F-fYFwJpJzukHukNKSjDPG5g4kIJm_N829SJ_EHqPEHPW8H1qzCBA-wo05-k2NX1gOfYcdJLdj_UcfOhLxftM_x3IbtEVz3Hu1yF1q7eYy7bhd2lVxcaAp26jR-7UrTUGFwK9bm4ZsVLkJ8obj-GBaBG3pUHe8STXBdq14T-2_kqTUDA8aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلرو، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس : تیم مذاکره کننده با قدرت ایستاده تا آمریکا به خواسته هایش نرسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/124600" target="_blank">📅 23:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124599">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فیلترشکن گیگی
8️⃣
هزار تومان
😂
❌
فیلترشکن گیگی 20 تومان دیگه نخر
کف قیمت فیلترشکن
👇
3️⃣
0️⃣
💿
2️⃣
8️⃣
5️⃣
💸
5️⃣
0️⃣
💿
4️⃣
5️⃣
0️⃣
💸
7️⃣
0️⃣
💿
5️⃣
9️⃣
5️⃣
💸
1️⃣
0️⃣
0️⃣
💿
8️⃣
0️⃣
0️⃣
💸
برای خرید پیام بدین
👇
🔤
@MrTh_Vpn
🔤
@MrTh_Vpn
🔤
@MrTh_Vpn</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/124599" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124598">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
میدل ایست آی: مالک برجسته کشتی‌های یونانی حاضر به پرداخت عوارض عبور از تنگه هرمز به ایران است
🔴
غول کشتیرانی یونان و مالک بیش از ۱۵۰ فروند کشتی: این عوارض می‌تواند «خسارات» وارد شده به ایران در اثر جنگ آمریکا و اسرائیل را جبران کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/124598" target="_blank">📅 23:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124597">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941e46de05.mp4?token=ajufrXcLXMwn9mMGyVw6vCVXWXj4-8mAAy10PnebiUg48LBOW95VKwI02kd_nalilAWxPVOw1EdGgeys-8vLIEdvO026LDGLtywp9ZqSjMGaJk0DM2JRp2CYE9tfKxh669c2MwuLuLM4E0o_Hf0BdKJK9czb_d5npsG0c8F1WK8LqwvrZPZKWVEfETdW5Lz7oV3xzel_o6g2F7B7idKMWri1gBbn7F8MW_exgtI2AxuLqB1UsAts3ke2ngnAro_H9Q2BO_7ZZVQRsNBnK703JSjzM7KAkqIug4rMjoGAeybiNlipgHk1wFgNA1LPpMiBJNImFKUJGvBR54bQ80QH7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941e46de05.mp4?token=ajufrXcLXMwn9mMGyVw6vCVXWXj4-8mAAy10PnebiUg48LBOW95VKwI02kd_nalilAWxPVOw1EdGgeys-8vLIEdvO026LDGLtywp9ZqSjMGaJk0DM2JRp2CYE9tfKxh669c2MwuLuLM4E0o_Hf0BdKJK9czb_d5npsG0c8F1WK8LqwvrZPZKWVEfETdW5Lz7oV3xzel_o6g2F7B7idKMWri1gBbn7F8MW_exgtI2AxuLqB1UsAts3ke2ngnAro_H9Q2BO_7ZZVQRsNBnK703JSjzM7KAkqIug4rMjoGAeybiNlipgHk1wFgNA1LPpMiBJNImFKUJGvBR54bQ80QH7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمود قیم، مداح: کوروش اگه سگِ آستان اهل بیت نیست،‌ پس خاک بر تمدن ایران باستان
‼️
🔴
پ.ن: محمود کاش اون شب بابات میرفت داروخونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/124597" target="_blank">📅 23:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124596">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvUmp0mUz4NE5cGJICEFjjKYwlotF9YRoNxPOLYZ4SDSMbZVylbkdITyDnROEDGe55A07HGshevJQ372-JY2YETHhVbsoMX6PRbmBX4OWWOa7eoLOoO7tAqB3Er21SGvfDYpqnlqQZcb2MLm9gW-Y1k3LSwqRouZieCNuKVJXov68DEHDvUOgOhFKp1xdgZCn9Yl54HNwTQJVAE2KnIu4IvCsj9E9uuGn2y4gIJEaPxYPQChPGO4gI43Ua-6QxYosBDdf4bPQ7s1RS0t7XGJOI37UR37Qo3MtrNgPP2h6HEIB-lf8mN6fgCtW_iZHEDysN9dmrnAb9_C0ZbP4RfHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تسلیحات و پیمان ابراهیم؛ پیشی گرفتن فروش سلاح اسرائیل به اعراب نسبت به آمریکا
🔴
آمارهای جدید نشان می‌دهد تحت تأثیر پیمان ابراهیم، میزان فروش تسلیحات اسرائیل به متحدان عرب خود از میزان صادرات نظامی آن به ایالات متحده فراتر رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/124596" target="_blank">📅 23:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124595">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یک سرباز ذخیره ارتش دفاعی اسرائیل (IDF) امروز صبح در جنوب لبنان توسط یک پهپاد انفجاری حزب‌الله به طور متوسط زخمی شد و سه سرباز دیگر نیز به طور سطحی آسیب دیدند، طبق گزارش ارتش دفاعی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/124595" target="_blank">📅 23:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124594">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
آمریکا چهار صرافی ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس و 6 فرد مرتبط با اونا رو تحریم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/124594" target="_blank">📅 23:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124593">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
معاون قرارگاه مرکزی خاتم‌الانبیا :
اگه هیچ چیز هم نداشته باشیم، با سنگ به جنگ با آمریکا میریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/124593" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124592">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f53317d490.mp4?token=H_1te19m6mWr5pz3P09HlXyJt7N83xpyUdNrB4cKp9ruGZ_RsXd2y9fXZ4qFOe-X2wi36fEMnXwY_cCFDq6c9NG-wNVJpXGTh1Zp0zCHFP1kO8DRi6euub0WZ7q-P70P2rbNk0_0WlwWNRpiQqzoWpn3ejWK2dxwGsRrSaJiUckZMDxrMo8nyQKF1p34GW9iEQTv4UlYhBV8jmuTfa0KfH-PGHztMIBNaBWPK040k5KnclgkHRl8A7Enx4NhXpvik6EWAXmKMawW5YEmvGUj2eH-OVtedDppQ1j3I4_2ZLyTWPAvzvTZk3Xy3P_i0Udd2ubHpkCH1b38CbPm1lG3vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f53317d490.mp4?token=H_1te19m6mWr5pz3P09HlXyJt7N83xpyUdNrB4cKp9ruGZ_RsXd2y9fXZ4qFOe-X2wi36fEMnXwY_cCFDq6c9NG-wNVJpXGTh1Zp0zCHFP1kO8DRi6euub0WZ7q-P70P2rbNk0_0WlwWNRpiQqzoWpn3ejWK2dxwGsRrSaJiUckZMDxrMo8nyQKF1p34GW9iEQTv4UlYhBV8jmuTfa0KfH-PGHztMIBNaBWPK040k5KnclgkHRl8A7Enx4NhXpvik6EWAXmKMawW5YEmvGUj2eH-OVtedDppQ1j3I4_2ZLyTWPAvzvTZk3Xy3P_i0Udd2ubHpkCH1b38CbPm1lG3vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز شبانه جنگنده‌های ارتش روی کرج، استان البرز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/124592" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn1.telesco.pe/file/jYlQNFRhHaysJHAl1yM2x8kGVvmdMbFp5WhccHokBGRcObvzphywRL45Y6EKLJtjxZQY3fLVCzhjwtpdUSbib4y5Co6WmnsUoR2GmFFmBhNOGeM-_iZYhlFzIe83GLoF_ACKBM48fDLmmJufRSnxCOSZZoRAIlk6I-AB3-SwxaSSaEzV4NJNs2CbGbeP2ozzE65HxdWV54blMAHfGImUepBlOwwtwp_AjXCeM70HysWe9MCXpNMr_qPsHcnTRGFXADHucM2yVaNoZR8EP7_3W3wx6sIt9oF5INbfWoL-gRItlIlmVQCDgmYncHiojSVWpy3aQLhW_wWf7FyomYcfZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 01:04:23</div>
<hr>

<div class="tg-post" id="msg-77405">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/VahidOnline/77405" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77404">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تسنیم:
شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد.
دوباره، تسنیم:
بر اساس گزارش منابع محلی، ۵۰ دقیقه بامداد صدای انفجار در سیریک شنیده شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/VahidOnline/77404" target="_blank">📅 00:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77403">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/77403" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77402">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HabxSSSz17rywZtQvlLn5xZFfvvu36IBJrRUkGAjT344DzmeYyPOg2cQndXyQMTJcbtNKNdnmCk5ZqMvpAcbV41HvXn42Le7J6GEuAaZaV8Uyat2BBay9oF4MM-Dv-DvnnSiYA9Xz_C_uuptcwMs9qUqmr4K8rQHq_zubepccku6yAjeOPRZmkC2zvHugax7tC48pz633MRIwfUGs_-j_OfqCbSPT1Poloa-_IpU8fZlgjC9MoDzFoUxGEGNJh_BXS5PB776fMgHUboQ1UUWBNcqJly_MGWqowkm3q2dPkeUSLIxQvaAe1SN-0IuSpGY9d0xejOgSRL9389iHaAfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: امروز نیروی دریایی سپاه پاسداران انقلاب اسلامی ایران مدعی شد که ورود و خروج از تنگه هرمز را کنترل می‌کند؛ ادعایی که نشان می‌دهد دریانوردان بین‌المللی فقط می‌توانند از مسیرهای مورد نظر سپاه استفاده کنند. این ادعا نادرست است.
✅
واقعیت: ایران تنگه هرمز را کنترل نمی‌کند. این آبراه بین‌المللی، صرف‌نظر از تهدیدها و حملات سپاه، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با حمایت نظامی آمریکا همچنان از این تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/77402" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77401">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77401" target="_blank">📅 22:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77400">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77400" target="_blank">📅 21:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77399">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پست قالیباف:
معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت. اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است. بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77399" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77398">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fdcc2765ea.mp4?token=MFov2Lc4Lpe_66w6SE1BNvUnak3MSJRGqi8ayY5lGFA2Q6-H1U6UxBDi2Z4oAmhW18abR7XDcsyG-fMBw7mYgmenIjgKGJNsyzoURT531G1MWHbqRPsERhkdDGgt1f_XjS0MoRYdlFpt48BjyzA7MMcyI58Uh7Azae7Dc6edPqgVqpht5E9e-jBZjpJmQWpC8Dl77c8zpWW9VZMD5DEzMO-CpztEr8CPfakOaYPYD296_FR_Wn_MO1k-53PLBKlQMrezcDuYfiMBoWGhzPGrkmmxPNiRrmbWaA5Hp_Q7opymp5zAzTILSik2G2Ysxvba7tGA8kfPu84Atja_whBLfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fdcc2765ea.mp4?token=MFov2Lc4Lpe_66w6SE1BNvUnak3MSJRGqi8ayY5lGFA2Q6-H1U6UxBDi2Z4oAmhW18abR7XDcsyG-fMBw7mYgmenIjgKGJNsyzoURT531G1MWHbqRPsERhkdDGgt1f_XjS0MoRYdlFpt48BjyzA7MMcyI58Uh7Azae7Dc6edPqgVqpht5E9e-jBZjpJmQWpC8Dl77c8zpWW9VZMD5DEzMO-CpztEr8CPfakOaYPYD296_FR_Wn_MO1k-53PLBKlQMrezcDuYfiMBoWGhzPGrkmmxPNiRrmbWaA5Hp_Q7opymp5zAzTILSik2G2Ysxvba7tGA8kfPu84Atja_whBLfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77398" target="_blank">📅 18:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77397">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NT8egVpnSSRjNMCDTNGpAUjhYkJhHpVBkpOIoscVyUNcsDwX-EtuJJMckbA2L2XTLuJvkUFfe7XKxVz64Tt0n9NX-6kUKTmzmUqRmzMOE0TrYjHqCPnFJvJfrlYiGtxRhWg-NGNjKbs3bEyCO5TIoIALJB55l5llIZMisDWmHuYqhUsNHYJAe_TLk24bSGyXn2aUpc2wd2Krxih4X41UnRNgnKEOt2DMQgg_AdjaAQ8vvRBI3Pxf3AQGwHmHuW1R44y_L90L_ZRAO_3TMllbO47VWqGRMLGhIxm7aEWHi0I3J-cv6RQn640d5ucX8Ah2T-2GAKu5X23r1fP6K718Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز چهارشنبه ۳۱ تیر، گزارش داد جزیره لارک در تنگه هرمز ساعت ۱۴:۴۸ هدف حمله موشکی آمریکا قرار گرفته و به گفته ساکنان منطقه، صدای انفجار شدیدی در حوالی این جزیره شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77397" target="_blank">📅 17:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77396">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYGeKkzEXDx-i9etGzvpMxCQQvEZGLzIHrmIh_cHInScx2qKMLwAya1LvshAc2kLiCHoJFsxcgJAJj17-YmXsi49Ts9OjLh8fSSXzrpIxfaa3WksIbTAnd6KnujR7qIgI6njtAcb_sCj2jXLmYlRgCH-6CmHs7N61a_HiZefWhmzdr4xK01tmYHX94swr7eVATQYB-RUJtiLTnaobL2QfdvwzSndtUJ_ygpSwkqrOgL2FW6x5sU9fup8hCZ9pScX20lVfc9ZwPrfrLb2LgeoxysYf8WSjEd0qsRd9FzpWfn7WQDr2JN33NFbtqrmf7F2VshaRyaf0oxAkXf5Vbbwlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77396" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77395">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FvG8fzKgVl-BiTeehBjfB310d10m_OsL7Tuj4mqeDpCZyn4IwAHiQ0FxpNmLBoPlzQLb37YzZlkX8fZNAo8jI-JXS9eGW6CZEw2V81xK4R4molwMX-hPGWrL7UKNIzKCIXF6-9C_xF-LCPvxPo_zm4JnXxwTvdR1HWPr87ddB7vgpx1bdwZyDfsvS4yZTRf8khbTlQz9oAz9gsFVWQlSRZM4BKnxhyd4VTfANKkgpKpg8esHiHCOXegQ7FHY0LmPIOOHYgdFE9a2Z8ePCr1AzQNC9IQQ7Iq-A37BTZeE2nNu-s8TSFgeNOg9qwBUl1qzTPz1qbjECvTsbCIb9D4Rpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز چهارشنبه ۳۱ تیرماه با انتشار پیامی در اکس نوشت که ایران هیچ فعالیت هسته‌ای در «کوه‌گلنگ» ندارد.
این نخستین واکنش رسمی یک مقام جمهوری اسلامی به گزارش‌ها از انتقال هزاران سانتریفیوژ به کوه‌کلنگ در پاییز سال گذشته به شمار می‌رود.
بقایی در این پیام نوشت:‌ «حملات و تهدیدات مکرر ایالات متحده علیه تاسیسات هسته‌ای صلح‌آمیز ایران نه تنها نقض آشکار اصول اساسی منشور سازمان ملل متحد، حقوق بین‌الملل و قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، کنفرانس عمومی و شورای امنیت سازمان ملل متحد است، بلکه دشمنی ریشه‌دار ایالات متحده با پیشرفت علمی و توسعه فناوری ایران را نیز آشکار می‌کند.»
دونالد ترامپ، رئیس جمهوری آمریکا روز گذشته و در جریان دیدار با رئیس جمهوری لبنان گفته بود فکر می‌کند به‌زودی ضربه سختی به این تاسیسات هسته‌ای ایران خواهد زد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77395" target="_blank">📅 17:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77394">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6910775c10.mp4?token=apjULYnyScUxn7OK0wwCXQPM_G_RGWF7PQyfHDiyrVbRR-0mRDrGW5f6_qaJ0mlI-orYkC9MYvTyIPq0qzj9JhJz7kBqKjmvTZuET7HXd9xkuSYM0Q9_CdjVZzNhk4W-K_f55Kpd5ZqLT9TQHjSVW74UOQliZ8TlqsUWRjrdQBhJxqSnA_hz5Si-7H6vD1O6AcPBTXqMCIZp1wKZoQKXlLGN-ax6s_5ge88m4g4rRHOxDjTQQZCylqHF-F52nwn6r-XBSlTiQL52uidV5SbxtGNeq5P4RC3IkIQZ85X0aE1-T8KvslZsGH77vLkffbVzuS8mM88sgr1VgIcGWuPZrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6910775c10.mp4?token=apjULYnyScUxn7OK0wwCXQPM_G_RGWF7PQyfHDiyrVbRR-0mRDrGW5f6_qaJ0mlI-orYkC9MYvTyIPq0qzj9JhJz7kBqKjmvTZuET7HXd9xkuSYM0Q9_CdjVZzNhk4W-K_f55Kpd5ZqLT9TQHjSVW74UOQliZ8TlqsUWRjrdQBhJxqSnA_hz5Si-7H6vD1O6AcPBTXqMCIZp1wKZoQKXlLGN-ax6s_5ge88m4g4rRHOxDjTQQZCylqHF-F52nwn6r-XBSlTiQL52uidV5SbxtGNeq5P4RC3IkIQZ85X0aE1-T8KvslZsGH77vLkffbVzuS8mM88sgr1VgIcGWuPZrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجۀ ایالات متحده می‌گوید واشینگتن برای تعامل و گفت‌وگو با ایران با هدف حل‌وفصل اختلافات آمادگی دارد.
مارکو روبیو که در مانیل پایتخت فیلیپین به‌سر می‌برد، گفت مشکل این است که «تهران در مورد گفت‌وگو جدی نیست».
وزیر خارجۀ آمریکا در دیدار با همتایانش از کشورهای جنوب شرقی آسیا عضو آسه‌آن، که نسبت به دور جدید درگیری‌ها بین آمریکا و ایران ابراز نگرانی جدی می‌کنند، گفت: «اگر ایرانی‌ها جدی باشند، ما هم جدی هستیم. اگر آنها جدی نباشند، آنوقت برای حفاظت از منافع‌ حود و متحدانمان به هر اقدامی که لازم باشد، دست می‌زنیم».
مارکو روبیو در این نشست همچنین گفت باز گذاشتن دست ایران برای کنترل تنگۀ هرمز، «سابقه‌ای خطرناک» را بوجود خواهد آورد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77394" target="_blank">📅 17:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77393">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UynULF7thKILzcRU5fP2qvzEdT-BL6Ff109Gu5aQQpDV2x0IHHa7mCtKwDzMgWmK9bi1h2bnjkh8qqTJXJ1CEYKrL4jaeY6EsNo9gL75kJcv5VtsBPB79DcDA7CRvr51e46XwXQzl-uJDRrBKdcBw80jGyUSfrV1pQ1DD_dD2fUU4Fce2ZuWb-oUa0Mk08Htogl3_8xfKT8GnSAft2LwE_ibjnbNLR7yfq1q5ofPIF-iajd4ppMJVozvSGseT-Tj0-yToog7LQJe4uU_YwMMyFWLAPkQWeEF3sU5Wla9EQvGxyhc9H7t_OH2EpGQdAmlO9mXx7xCcNSUvJcYjZYFDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77393" target="_blank">📅 17:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77392">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/77392" target="_blank">📅 05:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77391">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/77391" target="_blank">📅 04:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77390">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82b30de17d.mp4?token=Az6mK8ED3k1_sCvO-PQOFz3LG14yNeeeG1ClfEoQmwpFsuwuEucJR_uKB3V4MnnFGOwaZM2jwhv0oCUsotNEuom1gRXux6TI4lcv63FQQmbPaj3uvOrodFUunFi3-6QJxx1vP2ROi4RApIZGuB3BUP287vON4Dp9NBjjHG-FY6Uj6adBnuylSw5GmZFGGXv2UzRGnr4B9zaZglAgsHvTQYXarH61rS2l8wANgqVayxv7GC6o7hCX-iwvd0XFJArLt4suK3nyfCZM3vuTrHfjIDd2fEIPHkMkYyIUs16Q1bzXvyuiEZtkQULUzjyZ3UdODpKH85EFqPwdoRYChpAzxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82b30de17d.mp4?token=Az6mK8ED3k1_sCvO-PQOFz3LG14yNeeeG1ClfEoQmwpFsuwuEucJR_uKB3V4MnnFGOwaZM2jwhv0oCUsotNEuom1gRXux6TI4lcv63FQQmbPaj3uvOrodFUunFi3-6QJxx1vP2ROi4RApIZGuB3BUP287vON4Dp9NBjjHG-FY6Uj6adBnuylSw5GmZFGGXv2UzRGnr4B9zaZglAgsHvTQYXarH61rS2l8wANgqVayxv7GC6o7hCX-iwvd0XFJArLt4suK3nyfCZM3vuTrHfjIDd2fEIPHkMkYyIUs16Q1bzXvyuiEZtkQULUzjyZ3UdODpKH85EFqPwdoRYChpAzxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/77390" target="_blank">📅 04:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77386">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec4c08a6e7.mp4?token=uNEBbmIpM035aca4yDmsY0vgCuM3mgwyXMT3tzFY52yxyj-xTw7EzbVqu6EnEUGzDs-TkhlKYDLxVBVxx32oQhy6FSmXQMHuSuivIt8axjuKYlcj9HnJtHvy1hsKkw1ncNmBGwSS7LF1nBNk4tHW3lDqJGmCvg8RddDABCKA5SqLXtevX3fDE0gYblkfmG_lgocLGa08DXUAh0C5RXv8X47OBTweH__AElCCPfg-a1-LQ_C6Q3CArz8sZG4n_4OW8Bgq5bb1NeMk3lpoH732YMJ2sTTVLSCoULpSInBZ1ds2mjYi3F4FiuUOQfr80hjSWAhfsiLAwTn_bFI49a_Dtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec4c08a6e7.mp4?token=uNEBbmIpM035aca4yDmsY0vgCuM3mgwyXMT3tzFY52yxyj-xTw7EzbVqu6EnEUGzDs-TkhlKYDLxVBVxx32oQhy6FSmXQMHuSuivIt8axjuKYlcj9HnJtHvy1hsKkw1ncNmBGwSS7LF1nBNk4tHW3lDqJGmCvg8RddDABCKA5SqLXtevX3fDE0gYblkfmG_lgocLGa08DXUAh0C5RXv8X47OBTweH__AElCCPfg-a1-LQ_C6Q3CArz8sZG4n_4OW8Bgq5bb1NeMk3lpoH732YMJ2sTTVLSCoULpSInBZ1ds2mjYi3F4FiuUOQfr80hjSWAhfsiLAwTn_bFI49a_Dtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77386" target="_blank">📅 04:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77385">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام‌های دریافتی:
سلام اصفهان صدای پدافند اومد
پدافند اصفهان فعال شد . سمت بهارستان و صفه
اصفهان صدای انفجار اومد الان چندتا پشت هم ولی از خیلی دور
ساعت ۴ صبح صدای پدافند جنوب شهر اصفهان
جنوب اصفهان شهر موشکی رو به روی بهارستان پدافند فعال شد ساعت 4:5
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77385" target="_blank">📅 04:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77384">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/47e213b66e.mp4?token=rSHuRQNHqS9BdYm8I0Zv3bPVeI6BE-9bMr_aDeYPFQiBR9BrkQNL93_Kfyjst5lB5wBpY7uMW0LsiTQZQ_V-y2mdZB9yanyB0Ds0KSjHch7a3wSYH6d0-EAMCqLOc0CBqJQIe1my-gFlwpCvdiSSLttLH8DqixbbVMM-IPbxbzjA8u6QvQJwPNjh-Na-dF9OArjJcldJVLyPjEkx8v6Sn7-WIVSOvPUTmwE5FHeA_NLOt838f4bWgKD4lXpzR4cht51JssfT-jSUPfC4DJ-0Hdct9zjjtRzv3yhtO-JXyiW5MOVQ7QSlPQgNWo8faL2V3fPc7_Bs1JZYtSj3a90U5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/47e213b66e.mp4?token=rSHuRQNHqS9BdYm8I0Zv3bPVeI6BE-9bMr_aDeYPFQiBR9BrkQNL93_Kfyjst5lB5wBpY7uMW0LsiTQZQ_V-y2mdZB9yanyB0Ds0KSjHch7a3wSYH6d0-EAMCqLOc0CBqJQIe1my-gFlwpCvdiSSLttLH8DqixbbVMM-IPbxbzjA8u6QvQJwPNjh-Na-dF9OArjJcldJVLyPjEkx8v6Sn7-WIVSOvPUTmwE5FHeA_NLOt838f4bWgKD4lXpzR4cht51JssfT-jSUPfC4DJ-0Hdct9zjjtRzv3yhtO-JXyiW5MOVQ7QSlPQgNWo8faL2V3fPc7_Bs1JZYtSj3a90U5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77384" target="_blank">📅 03:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77383">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای سنتکام امروز ساعت ۷ عصر به وقت شرق آمریکا [۲:۳۰ به وقت تهران]، برای یازدهمین شب متوالی حمله به اهداف نظامی در ایران را آغاز کردند. این حملات با هدف ادامه تضعیف توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77383" target="_blank">📅 03:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77382">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77382" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77381">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77381" target="_blank">📅 02:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77380">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c6ad0edf20.mp4?token=UenKQuRa9PK3EVVtG6TylZWDwGoSIDo2jLIpDazrkGwDboWBRSIseG25npcNdiOiZoDBar5s5w-HLC45b2-6AxQumiUcXKF2GHojFo_DCOUwFIeT_6XHqGHnCSOXP0vzuh0XsHvwZbc9cYgk7QmfxdbpZULyIqH5YMIwpAZLsw7Hp0GZtcGGXSKZVj8zxA80juVLh35-4hzWqJfi8uUpsB4N_4-1uPNIudCQ1qUV0JmpMCYy_2Un91eeztOQwxpdoAQ1CRx42_lgw4-dcTNMoXDi9AtP1pSFCQdo_8lU5Id8bQavFWHXUVj2q-fN8aIJy58Hmk5lKLYMk3az0vHPBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c6ad0edf20.mp4?token=UenKQuRa9PK3EVVtG6TylZWDwGoSIDo2jLIpDazrkGwDboWBRSIseG25npcNdiOiZoDBar5s5w-HLC45b2-6AxQumiUcXKF2GHojFo_DCOUwFIeT_6XHqGHnCSOXP0vzuh0XsHvwZbc9cYgk7QmfxdbpZULyIqH5YMIwpAZLsw7Hp0GZtcGGXSKZVj8zxA80juVLh35-4hzWqJfi8uUpsB4N_4-1uPNIudCQ1qUV0JmpMCYy_2Un91eeztOQwxpdoAQ1CRx42_lgw4-dcTNMoXDi9AtP1pSFCQdo_8lU5Id8bQavFWHXUVj2q-fN8aIJy58Hmk5lKLYMk3az0vHPBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77380" target="_blank">📅 02:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77379">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/77379" target="_blank">📅 02:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77378">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77378" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77377">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سلام صدای انفجار یا پرتاب موشک از کنگاور
سلام ۲ و ۳۵ صدای انفجار و لرزش کنگاور
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/77377" target="_blank">📅 02:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77376">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77376" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77375">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77375" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77374">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77374" target="_blank">📅 02:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77373">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi_00YA6S9tlvJyiM8PedtHllxQqDhEqS5oi6byw1DkExEzNs_FV2xPz3vOBt9Nsv66aC5r9eMltDKtwFgU9nv9JqBfFb71EriIAs8iG7smxGTpX_lgA5Na2lqQgn9i96aGRx_ApL6YnenL0h758XLvlL4VVclwVIzR2xo5OS0C56rbvzqQzMg4tfclEUXraHh-9veTcKqp3pjF-7judzeT8RwR_ap7H_3Q3ep6a9L6GXPfU3tufOe7y-jMJ2BZtCEts4PZ5ooYyukGFqrgZPrwmwG42Ubl32duyhBe9KovVamJ7m3I1RPg1oGN16NuUSMdqi1jV6qY5CiaUpJlAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد کل ارتش کویت، بامداد چهارشنبه، با صدور بیانیه‌ای اعلام کرد که پدافند هوایی این کشور در حال حاضر در حال مقابله با حملات پهپادهای متخاصم در پی «تجاوز گستاخانه ایران» است و تصریح کرد صدای انفجارهای شنیده‌شده ناشی از رهگیری این اهداف توسط سامانه‌های دفاع جوی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77373" target="_blank">📅 01:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77372">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">منابع حکومتی:
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): تعرض به مراکز هسته‌ای ایران، پاسخ گسترده نیروهای مسلح را درپی دارد
🔹
آمریکای جنایتکار مراکز هسته ای و حساس ایران اسلامی را تهدید به حمله نموده است. اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله ای بشود، آن را به‌عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77372" target="_blank">📅 00:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77371">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgtALmKXgMy_-WpHpS0tIXxBHhLOpx6SKm7AD2La9Ch0lHgyvvnvRxS9eHs_x596mO7IKxQnpUVe7qyykFMAAkBPAJBwwz33fjUUwsoxc9oZcngi8I2exsHFESi0KLxw55_ScFhjIJmhqdNW1E6a8Fod_P5tugb4hx-YtxF18kGkiX2Gy07N9Xsi3Yriegaq6_3FqgjGaGSV5S76qEG-9ImGtEs8jHxisPC2PFrTpziqbiwf2xlmebyK0ZrdTtr34ZhyJnXys6NSLPperyliNMrB5Ci4wGyIq3OfRxv9eY3J0OhdeBf0li99dqcPUpvA-_9BbeXEDTq9Zh5a3pItMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع ایالات متحده می‌گوید جنگ با ایران تاکنون ۳۷ میلیارد و پانصد میلیون دلار هزینه داشته است.
پیت هگست این موضوع را خطاب به اعضای کنگره اعلام کرد؛ آماری که از افزایش نزدیک به ۸ میلیارد دلاری هزینۀ جنگ، نسبت به ارقام قبلی که دو ماه پیش اعلام شده بود، حکایت دارد.
وزیر دفاع آمریکا البته تأکید کرد که این رقم تازه، هزینه‌های پیش‌بینی‌شده تا پایان سال مالی جاری، یعنی ۳۰ سپتامبر مطابق با ۸ مهرماه ۱۴۰۵ را هم شامل می‌شود.
از زمان آغاز مجدد درگیری‌ها بین ایران و آمریکا، این نخستین بار است که پیت هگست وزیر دفاع ایالات متحده به همراه ژنرال دن کِین رئیس ستاد مشترک نیروهای مسلح این کشور، با حضور در کمیتۀ تخصصی کنگره، ویژۀ تخصیص بودجه، به سوالات اعضا پاسخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77371" target="_blank">📅 00:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77370">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jI9L1a0_Cjygyl2s1nKyucPYtFm7g4UOBE0wnYnrumxFnE0KmPDOc2Sh6RVNBt_baSp2Qygx4J3MGPTvDf2W3rKf8TM4umfrhn5HiJZD7VR0gKzKh08LWIpYv6u7UK8fM4_FhUcMJrOZCgMjG_YgCVTvar9OO1EcCW8Zh03mxxhEGbtWLxu5u_mLhiU6NxyeMEVh5ZzJd_JlEL4Uw2qaHfel3tjp-7C_ES9JPMbQXDEaeIaTzlIeyrJ2K1WeO0FGHjv_OxHxq7WqGoMyw9yFyDoCjtTUsLlremKFE3nhLda21eWaXYBnQJnFTa9U1vrJqt0_pb6TClHMU14oSd8FMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77370" target="_blank">📅 23:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77369">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5abf96fd5e.mp4?token=hWnnywMG3QFQqAxVbQu1kL-YmMG3FubSTwj4dJY6gnP9PW5rILNDB_Mh-HfFqMyb-O_u--SW5RLFDALLWlrvSUz_kO-gZnPoIRn0g63uCjY-7bLSSvwUGMtSb1HmpGIgoaaGKRiNjNtOMv9GFuMQFDv9Cs_BnkLi4xiFI0yyXI5m2ObjaBBnLPRvc0FmdqZfRL3ONtDcFa4q4DLNTm8eGHANbK3PYi8nyU8PT70bsq2MbKfuIJNYXZ8Ft8BCXt0rH_WN9iMX7a1LawHrTPaNNdSD1Pg3kxQmb_DrDWDyg4TDtDAzbAx7uD9WHfswWpA2cKyoin63wox9SwY5vAjTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5abf96fd5e.mp4?token=hWnnywMG3QFQqAxVbQu1kL-YmMG3FubSTwj4dJY6gnP9PW5rILNDB_Mh-HfFqMyb-O_u--SW5RLFDALLWlrvSUz_kO-gZnPoIRn0g63uCjY-7bLSSvwUGMtSb1HmpGIgoaaGKRiNjNtOMv9GFuMQFDv9Cs_BnkLi4xiFI0yyXI5m2ObjaBBnLPRvc0FmdqZfRL3ONtDcFa4q4DLNTm8eGHANbK3PYi8nyU8PT70bsq2MbKfuIJNYXZ8Ft8BCXt0rH_WN9iMX7a1LawHrTPaNNdSD1Pg3kxQmb_DrDWDyg4TDtDAzbAx7uD9WHfswWpA2cKyoin63wox9SwY5vAjTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز، ترجمه ماشین:
خبر فوری: معترضان چندین بار جلسه ادای شهادت پیت هگست، وزیر جنگ، در برابر مجلس سنا را مختل کردند و پلاکاردهایی با نوشته «نه به جنگ با ایران» در دست گرفتند.
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
پلیس کنگره هر چهار معترض را از جلسه بیرون برد.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77369" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77368">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kL50g0D7KpvTdgvKFKRoZJCVkoEdl8v-_QoBViqCVdV--GRfXZRasPla_Ec3UJs1ppjztJJ487EVPPk1Cehelvb5IgHwmrraPDxLV2ZDbvKlWKQR3tcZe5YrQ_K_KCuU7uzx_v-940TxMR_Z1JonUDLc5Dy9YYcykI8bZdYqoRRUMKvzVolZIct-6qRQL0P1La6icMsoj-tHc6XIhxpfLgV2x1l49G-ucVD7iBfgTIQsej6-N2MN5koCjpPvQixWZvw4knyHX6uTA6nOkh-uIvSKqERZ_4iCATMH69EHyx3fBZep7SEWgv_jVu0KWEJTG3cxCX8Bhx_1z5xqr2Inqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز سه‌شنبه ۳۰ تیرماه گزارش داد اندی برنهام، نخست‌وزیر جدید بریتانیا، با استفاده ایالات متحده از پایگاه‌های نظامی بریتانیا برای آنچه لندن «حملات دفاعی» علیه ایران می‌نامد موافقت کرده و بدین ترتیب سیاست سلف خود، کی‌یر استارمر، را ادامه داده است.
این خبرگزاری به نقل از منابع آگاه نوشته که استارمر روز ۲۶ تیرماه نشستی با وزرا و مقام‌های ارشد برگزار کرد تا سیاست بریتانیا پس از ازسرگیری عملیات آمریکا در اوایل این ماه بررسی شود.
این منابع افزودند که در آن نشست، وزرا تصمیم گرفتند سیاست موجود ادامه یابد.
بر اساس این سیاست، پایگاه دیه‌گو گارسیا در اقیانوس هند و پایگاه هوایی «آراف فیرفورد» در گلاسترشر انگلستان می‌توانند در اختیار هواپیماهای آمریکایی قرار گیرند که مأموریت‌هایی برای مقابله با تهدید موشکی ایران و نیز اهداف مرتبط با تنگه هرمز انجام می‌دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77368" target="_blank">📅 22:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77367">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XzxZF9e-nk_cTG9345khozmGm02Zi8-2Lw_NnFbIMejHrYhZly9qEitV2Fc576H5HW5stLSpUMPz-yA3FcQnAkup2DeM1hnRzJXSSCzA7qySGQPtFhgSAXPC3bqK6dad_7t-aaITg0VKbk3bLK_e70V5_73uxKybWFCzML0iJO7ddyUaMprwq6hSc53bkHjl1quXh2o_WCGGW7X7Cyw3d5aqXuui4vtNr8aTbhwQRBqa286BnE91uynNHbAbEyWtjh62sOzJ9tywO6TfyoUmrADuq9Yx3Ebu-lbNbd8O58SY65-9bvhNEhs_df5L0CnaSuwIrU5Xm9USd-wtz4m90A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77367" target="_blank">📅 21:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77361">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HXraqJ_xV0eYFBIi3a5Xvt1w6OiqFFYcblzHSEgURCRdf5ENN1vaxEyIdLwh2tJfwRF6RFwhPY8Z7CajW0Wq51qTY20miGy6TOVqWPFCo74DZTiH7wKuaIACBnLkeF5s5Ih8nknDS9-Apzw-ZBrShZafRC5gV9nminlY1xdqFrsHzTGfHlLsnxy3vBrZMCUs9jiE0jas7bBEvSlv-aN1DgkS-J5CdKj3C-vE2sjwuKIAs-aQ2WpeWqiDQSdJ1bWCpdIu3yw68YLz4-k7hHCKUDDNfiYma17gmRSsaGuj-mvLOzt3ETnzs8RBEL_njgV7ihzEmRN8L9fJYOC5NHmVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KRVNZ7UtPL6Ee91o7iIPlQ5SgQfORnJ9YprEoUKilg8jGSw7fBN6nmanBvNMD_iDXUpTYp9S9MrlQtyZVNejD2Fqm6gl4tjQvUYvSQwr372njhA26hgdyLFxVq1D7O4OieRT1Y2oca5UoL1yMerGon7cQzafRzvV9ff4qKjypJ0BtFKeicv6g31voHGBmCiyTBOJ3i2q-UDuK1AMh5BW8NesJJtKySFtr7jhhC1sj8i1IHOD1B94ti_Zp8ThYNxdsaCXbrwUvnlrS7o1-Zsn2ULitFUgTN5-GhgBh7kgd5yVfwb2It6CJGCiRnqkF8RW5yUaS1iec4zBO693Ek9IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sg528jWgcg7Y56fgKqgSPw7qM78ADtr4KYlObzLFIGJX4TNGlRttHDOONO-JxdFDgNDgkWn2QRzfwjEGhWYMBww-JDl92oscFiF3GH5YpA8DAjysUZtv0Z2PTvXEUhkZhIhNxh6pHuRLKpZMXgtcOArszQvaBDpuTTKj0hoprc1gCmQ8dsS4TKZzc45htc1puK3EA92go36mcLptEftTzfk0x7Z35fCuOnL9sGkuUBAw-u3vaxnz7FxHGgRqaAeIERLfz16Cyp-sWlBgIb6Ru30akVGFWQFB7dWeLQDIQx1gRRZcpHKLR-2UbRJYeFmUco6myqM9q6TPvFNV_Hae6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JRy3A3yeXBEXUGPbHsW3ej8NlHEnKIYiVuJUJSQnJ55uwpoTb-Qg4yJvFNO0D_jJ3QWNA2iMVEvHy7FL5jYbcvmmMhv2iMxjwoVHo55hnkNT9dnSMSoh1sMGCrL3zya7UpXQ2gOW4oLOJQjQds0D48AOmLGttDEnUfviVv9GbzSOVYb9vC3fJRxI9HTTv0L-kbk4kAU5dKHdus-TJhG95amRUVVnsZxvkBADdqS1Jd1gf6AHMdsNopJCBmZyyfSH-gstKVQ9-vtLOnTiyBNR2-mA9pLayv1wRtw7PzQIs5wKkp9oYjj3ceKIgZHiix3FTrJ7YPIGsYSUGOtjP2ZD0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4477673f76.mp4?token=kT1t-WTTGqRDhJjThuoEpUO1gejsxrIU01Ve7ytt_-5Oy_4KymjjR8XVJaZwYwyAVAfjJ4IP9Jvl13vIDUcT4_SiIeUdOOE8bbSMrMY4r_hc9bNb4IPhBxmq3QN9N7xHzU06hsVuw76I3i2YR4bi2VaKXyWo2Fu7_Tl_EhAq2NajthFjaUkeQX2b4pT7sHpqHxXIouiIFqi-DOWYutF7OdO4j38e5S8jwTLSCCGefrvd8yb2plXOlX9toysOEHq-Ur8kRNRmIn7haJlGtotO-6Lhkv-6eoTQNG808_i0rMJAEznGDT947RW4miudAlIWKZ-1HP3mAaUi5tSQwYmwaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4477673f76.mp4?token=kT1t-WTTGqRDhJjThuoEpUO1gejsxrIU01Ve7ytt_-5Oy_4KymjjR8XVJaZwYwyAVAfjJ4IP9Jvl13vIDUcT4_SiIeUdOOE8bbSMrMY4r_hc9bNb4IPhBxmq3QN9N7xHzU06hsVuw76I3i2YR4bi2VaKXyWo2Fu7_Tl_EhAq2NajthFjaUkeQX2b4pT7sHpqHxXIouiIFqi-DOWYutF7OdO4j38e5S8jwTLSCCGefrvd8yb2plXOlX9toysOEHq-Ur8kRNRmIn7haJlGtotO-6Lhkv-6eoTQNG808_i0rMJAEznGDT947RW4miudAlIWKZ-1HP3mAaUi5tSQwYmwaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی  در شیراز
دو تصویر اول منتشر شده در سایر منابع
سایر تصاویر دریافتی از شهروندان،
سه‌شنبه ۳۰ تیر
گویا تصاویر بالا دو نقطه مختلف شیراز رو نشون میدن: کوه دراک و کوه نزدیک دروازه قرآن
آپدیت:
به گزارش رسانه‌های ایران عصر امروز سه‌شنبه(۳۰ تیرماه) آتش‌سوزی گسترده در ارتفاعات دراک شیراز رخ داده است که همچنان ادامه دارد.
خبرگزاری ایرنا گزارش داده است که شعله‌های آتش، مراتع ارتفاعات دراک در شمال‌غرب شیراز و کوه‌های نزدیک به دروازه‌ قرآن را در بر گرفته است و «زبانه‌های این آتش‌ از نقاط مختلف شهر به وضوح قابل مشاهده است.»
رئیس سازمان آتش‌نشانی شیراز گفته است: «۵۰ آتش‌نشان به همراه دو تیم تخصصی کوهستان در حال تلاش برای مهار حریق هستند.»
هادی عیدی‌پور به خبرگزاری مهر گفته است: «به دلیل صعب‌العبور بودن منطقه کوهستانی، وزش باد و وجود پوشش گیاهی خشک که موجب گسترش و شعله‌ور شدن آتش می‌شود، عملیات مهار حریق با دشواری همراه است.»
دلیل این آتش‌سوزی هنور اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77361" target="_blank">📅 21:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77360">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf4d005f22.mp4?token=CMw1c-W4-kFXxun1RNps-3LlxFzosT_Gc1ejQcnFkR6qYE-yVVZLT855wTvlu145eRgYYE3JnlmYea3bUPSCWyGN8dm_XHn0khd8tvj0NIg70_RcZWd4iCqiilbUP7BG00T0Hilxh95dOq7_-c2IuVzzmxcGNmh1digUOBgUDFfn1HF_iprkZla5vXLKDAEXLk_UdyWiA3xZCP1d_AD33lUDlnb-fI5BQ_-8Oglze1Opifj6Ye9kyEnAlONNiXQjA_-vct2vJTbJXFM9bZqeU921JXJEI_KhRG0KHcQwDa-5Q6wCiunGa_p-sbZXxrHPW3LWWcbIwo9HeZDbrBXaQBKrphWxjTUX7jF_vQa8Dj25w04XJNxHZSv-1NFFNpQS98mgQJaFFz_nb1O_3Gb0Ri6NBuRqV8NvXuoEdb3pPWT_8Enl8L1vwlW0NkFQ_jzquQcUBzrx8plSIRtDDupbLZkRPpLARjxHJkos3o1LZ1lErliC5xDurzrPY-eksGO8d3WNJHCqtXEhmaGDMpTlzFRaIpCjNbiCVQWpmww6-4RdvsJ3pfrxyz7LMOYmrw0rixS08SbrAR4Z_klVMR7oK8tnMaiBUa8NWw_3_26N_GW_BBq4FM-XtQIWlnMj2yviWLsicK9WBE9EOWTUm7kIf39yPyqwGc-ds579v1XoVQE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf4d005f22.mp4?token=CMw1c-W4-kFXxun1RNps-3LlxFzosT_Gc1ejQcnFkR6qYE-yVVZLT855wTvlu145eRgYYE3JnlmYea3bUPSCWyGN8dm_XHn0khd8tvj0NIg70_RcZWd4iCqiilbUP7BG00T0Hilxh95dOq7_-c2IuVzzmxcGNmh1digUOBgUDFfn1HF_iprkZla5vXLKDAEXLk_UdyWiA3xZCP1d_AD33lUDlnb-fI5BQ_-8Oglze1Opifj6Ye9kyEnAlONNiXQjA_-vct2vJTbJXFM9bZqeU921JXJEI_KhRG0KHcQwDa-5Q6wCiunGa_p-sbZXxrHPW3LWWcbIwo9HeZDbrBXaQBKrphWxjTUX7jF_vQa8Dj25w04XJNxHZSv-1NFFNpQS98mgQJaFFz_nb1O_3Gb0Ri6NBuRqV8NvXuoEdb3pPWT_8Enl8L1vwlW0NkFQ_jzquQcUBzrx8plSIRtDDupbLZkRPpLARjxHJkos3o1LZ1lErliC5xDurzrPY-eksGO8d3WNJHCqtXEhmaGDMpTlzFRaIpCjNbiCVQWpmww6-4RdvsJ3pfrxyz7LMOYmrw0rixS08SbrAR4Z_klVMR7oK8tnMaiBUa8NWw_3_26N_GW_BBq4FM-XtQIWlnMj2yviWLsicK9WBE9EOWTUm7kIf39yPyqwGc-ds579v1XoVQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به زودی «کوه کلنگ گزلا» در نزدیکی نطنز را هدف حمله‌ای شدید قرار خواهد داد
06:33
دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۰ تیر در دیدار با جوزف عون، رییس‌جمهوری لبنان، گفت جمهوری اسلامی با «درماندگی» به دنبال مذاکره برای پایان دادن به جنگ است و هشدار داد آمریکا به‌زودی «کوه کلنگ گزلا» در نزدیکی نطنز را هدف حمله‌ای شدید قرار خواهد داد.
@
VahidHeadline
رئیس جمهور آمریکا در پاسخ به این سوال که آیا ممکن است ایران سانتریفوژهای خود را به داخل تاسیسات کوه کلنگ منتقل کرده باشد، گفت:
«ممکن است کرده باشند ... ما اطلاعات مستندی نداریم ما فقط در اخبار جعلی این چیزها را می شنویم. اما سانتریفوژ بدون مواد هسته‌ای اهمیتی ندارد. ما مواد هسته‌ای را دنبال می‌کنیم که اصل قضیه است. آنجا را می‌زنیم، احتمالا خیلی زود. معمولا این چیزها را اعلام نمی‌کنم. اگر فکر می‌کردم می‌توانند جلویمان را بگیرند نمی‌گفتم.»
@
VahidHeadline
ویدیوی بالا: قطعات مربوط به ایران به تشخیص ماشین
متن زیرنویس ویدیوی بالا (ترجمه ماشین
)
تیترهای پیشنهادی چت جی‌پی‌تی درباره متن زیرنویس ویدیوی بالا:
▪️
ترامپ: ایران عاجزانه خواهان مذاکره است؛ هر تأسیسات هسته‌ای تازه را به‌شدت هدف قرار می‌دهیم
▪️
ترامپ: اگر امروز هم خارج شویم، بازسازی توان ایران ۲۰ تا ۲۵ سال طول می‌کشد
▪️
ترامپ: ایران هنوز چیزی ندیده؛ به هر محل فعالیت هسته‌ای حمله خواهیم کرد
▪️
ترامپ: محاصره ایران مانند دیوار فولادی است؛ هیچ‌کس عبور نمی‌کند
▪️
ترامپ: ایران سلاح هسته‌ای نخواهد داشت؛ برای حملات سنگین‌تر آماده‌ایم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77360" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77359">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5ebdb6d740.mp4?token=S3W1ZdvnKEg9CpKIRz-1RQfVquqf6zbO20kVhqqBgbvRr5tLQDj7B71mzh4DdTA6gq0WDZk-WjyBhHe4dWBmLzHcYjiD-EsZ69cL9SSjgFxXWBjNJahZpbY6qrvPPFyXER_I0hG4F_xcIfuszZLWgkwy58wzz1b9VlVCG-61I_aFPXKQRb-H2_78tvczz_Q6RLYucn_gZdNbeCLyjIspee-L6XPSier3cBptb2kh4-ULtNlZ7bye05LPpBg-yGAtKjerQ6YbbK2vNzgG5Fk578eihWc6Euq3HiKNL35RelHNrdJFxBtyrgW_0NgcNYxBe5ES8SKeCJ-jFEfZ5fo9tw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5ebdb6d740.mp4?token=S3W1ZdvnKEg9CpKIRz-1RQfVquqf6zbO20kVhqqBgbvRr5tLQDj7B71mzh4DdTA6gq0WDZk-WjyBhHe4dWBmLzHcYjiD-EsZ69cL9SSjgFxXWBjNJahZpbY6qrvPPFyXER_I0hG4F_xcIfuszZLWgkwy58wzz1b9VlVCG-61I_aFPXKQRb-H2_78tvczz_Q6RLYucn_gZdNbeCLyjIspee-L6XPSier3cBptb2kh4-ULtNlZ7bye05LPpBg-yGAtKjerQ6YbbK2vNzgG5Fk578eihWc6Euq3HiKNL35RelHNrdJFxBtyrgW_0NgcNYxBe5ES8SKeCJ-jFEfZ5fo9tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، روز سه‌شنبه ۳۰ تیرماه در یک مراسم عمومی با بیان این‌که «سطح دسترسی» به مجتبی خامنه‌ای افزایش یافته، گفت تمام اقدامات مربوط به مذاکره «بر اساس رهنمودهای» رهبر جمهوری اسلامی انجام شده و از «اظهارنظرهای نادرست و بی‌توجه به ابعاد مختلف» در این باره انتقاد کرد.
مجتبی خامنه‌ای حدود ۱۰ روز پس از کشته شدن پدرش در نهم اسفند ۱۴۰۴ به‌عنوان رهبر جمهوری اسلامی معرفی شد، اما از آن زمان نه تنها هیچ فایل تصویری که هیچ فایل صوتی هم از او منتشر نشده است.
عباس عراقچی، وزیر خارجه ایران، به‌تازگی اعلام کرده که «هیچ‌وقت» مجتبی خامنه‌ای را از نزدیک ندیده و در دورهٔ رهبری او نیز جز معدودی او را ندیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77359" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggIHTCGLVjdrQalYISA94Y9_5pLn5K1E_pX6j0-28JPlaC7MNbW_JdeWYrGjgLUEwkOJ8Gn0eFqsiUhsS2GY-VfUkEEyExIJeJwcwTHykkfc1FhTMPcz5ntTL4P05S7A7OPqZlD1OMSwhG_6--xeis8ea2Sh4YvIxl4gVbaGJfg37UfnKp93XVs7XHc6FkmtxRJtBYwz77L8Cp5PDA7EMBWWHZLqANCHBl45bATS9MPqhIKRyvfsydBryVHYKBkV7JI7zfSQGna7HSDtEivtXzEej3Bj2Yb4My5iW-u9Tu6ZqvNlYUuuhIUxn8eS31Up6GnzIOmi7inN2yiE0KTt5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، «شیده توکلی»، شهروند بهایی ساکن تهران، را به ۱۱ سال حبس تعزیری، جریمه نقدی، محرومیت دائم از اشتغال در خدمات عمومی و دولتی و مصادره بخشی از اموالش محکوم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77358" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77357">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad05dc08a.mp4?token=n6uThbD-n1hQ276wf8ccvcdu3DI9sgX0qQBHcDkoiFuu4OfDjsLcWNTuLBqkJBd2AeoG_NxtSJj51ULmqNS6tJSuNPfXDZ4vAsZVfcOPUu1it4SFCXr2SfGoSrZKK8L_ifL9sR4ODByBuzJpevWsDD1IDMuDNh0tg0bFkpD0s-_r0IEscMBZshphd87aQdKh0wf0HaY-cEeNrykHyiUJlLGJT5EY5R892_Wq4hzKMt_rR-4VCz6_wjSTYGIhkt6ZaHvZGvuIA40XkjUUNvflisDZGwrsJjJz1KNFBzFssDGmgsQpMzzkpKfXZW_b0E1VxjB_xBWpUuSJK45XnSv1YJu6js5lLieDopt6FHu4uePH0PTVuzmoSta6q-dElBGPlr4-qlWieYFAOXP-lS-6POMB8eJptdV3whLFZ4B1fQQ85iCzjbikD82Oa7ukxcajOOVs_-ljZrwM5aqse5ksdeoBNrmD2RAQ8AQOZHlINmrCXpFHWG4ehgyrJZfdmjXOzVa7Lwn1SFUiFPzWzoaDBqJFQ1lYu2M5OWY1q7qhTu20H8yPL4UTxJ9RIgpGuQmLmSvi_5JY5NVh3sKuG26yiaMkxmDb5v0j8gVk7riV_TmZSH4rdVXtEqZNX1wiVM1RpIHeXJu7ulWlLe1lmuuqCmdm6QNTqN8GOkJHff4y1uM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad05dc08a.mp4?token=n6uThbD-n1hQ276wf8ccvcdu3DI9sgX0qQBHcDkoiFuu4OfDjsLcWNTuLBqkJBd2AeoG_NxtSJj51ULmqNS6tJSuNPfXDZ4vAsZVfcOPUu1it4SFCXr2SfGoSrZKK8L_ifL9sR4ODByBuzJpevWsDD1IDMuDNh0tg0bFkpD0s-_r0IEscMBZshphd87aQdKh0wf0HaY-cEeNrykHyiUJlLGJT5EY5R892_Wq4hzKMt_rR-4VCz6_wjSTYGIhkt6ZaHvZGvuIA40XkjUUNvflisDZGwrsJjJz1KNFBzFssDGmgsQpMzzkpKfXZW_b0E1VxjB_xBWpUuSJK45XnSv1YJu6js5lLieDopt6FHu4uePH0PTVuzmoSta6q-dElBGPlr4-qlWieYFAOXP-lS-6POMB8eJptdV3whLFZ4B1fQQ85iCzjbikD82Oa7ukxcajOOVs_-ljZrwM5aqse5ksdeoBNrmD2RAQ8AQOZHlINmrCXpFHWG4ehgyrJZfdmjXOzVa7Lwn1SFUiFPzWzoaDBqJFQ1lYu2M5OWY1q7qhTu20H8yPL4UTxJ9RIgpGuQmLmSvi_5JY5NVh3sKuG26yiaMkxmDb5v0j8gVk7riV_TmZSH4rdVXtEqZNX1wiVM1RpIHeXJu7ulWlLe1lmuuqCmdm6QNTqN8GOkJHff4y1uM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند  از ابتدای سال ۲۰۲۶ تاکنون اعدام دست‌کم ۸۵۱ نفر در ایران مستند کرده است که ۳۲ مورد آن تنها در ماه ژوئیه انجام شده است.
🔸
بر اساس قوانین بین‌المللی، مجازات اعدام تنها به «شدیدترین جرایم» — که به معنای قتل عمد تفسیر می‌شود — محدود شده است؛ با این حال در ایران، جرایم غیر خشن مرتبط با مواد مخدر، بیشترین سهم را در آمارهای اعدام با این‌گونه اتهامات دارند.
🔸
طبق داده‌های گردآوری‌شده توسط بنیاد عبدالرحمن برومند، نزدیک به ۴۵ درصد (۲,۹۴۶ مورد) از کل اعدام‌های ثبت‌شده در بازه ۱۰ ساله ۲۰۱۶ تا ۲۰۲۵، مربوط به اتهامات منتسب به مواد مخدر بوده است.
🔸
سوءاستفاده حکومت ایران از مجازات اعدام به حدی وخیم شده که زندانیان واحد دو زندان قزل‌حصار ، بزرگ‌ترین زندان دولتی ایران برای دومین بار در سال جاری دست به اعتصاب غذا زده‌اند و حتی برخی از آن‌ها لب‌های خود را دوخته‌اند. با گذشت هشت روز از آغاز این اعتصاب، هیچ‌یک از مسئولان پاسخگوی وضعیت آنان نبوده و به خواسته‌های اعتصاب آنها توجه نکرده‌اند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77357" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77353">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SljygkgCX8qNiAJ71lI7HxnDpgAtRKmLrpSV-3WfkR2i5oFwzxPbUEINJ-5c40SQjelt8umMf-AKvncbWk-imwnjoibu2K2IVGheOU-osnrNdHIll9I5rBhuwNGQvzkt5_Vfbh0IivHgCYAT1N2Mi5NeelnZASEn7pU_9S8z52Uv9_JWXhpIu4hPS7FaBQ6wNnqC-e5bCXyB6EU9UOio7DJN_XQgfuP1uXF_jtQ1WqAnr8tYNfNOPKTvL7w8BbXIZYvgdNyISC5LnyTEDqofpRdOupvlWo1IioUdHcYilae8UjJn32m3YKsy4MV8v0sgLlD-xQgUfx-bivE2pnK2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a9_NvMKRxKuk-yTIAGQ1rbqbxpIW4ePdqju1Aj5YWs19EtbdC1SfS1H07usWAHLBXzzkC0AhwHTna4_HlgMxmRoahdP4HYpRMAu__3G0JWGb9tTmaq-Hl-AlMu4pfe4u_cOYsOXcV-rq7tMXBAlbbtlKgVKDgkomX92kKvwWX_ZHdSR87X94T40Um1Hp_ixs9IKCIoynrFLZc4mP082XVLFQKXFvcqGKTDAGkAOPphEwtbwYFACI95WqmtF-jt20djoBGvt4h9UQ4HP6rBXaOCPdpkSAgmBJnNmoMVmXQ1TMU3t18DiCJDAkR1VZbKQYPuyJJkJXkGIbAZIYZ8I8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nuv-WDZQscI5jMcytmlRGV07tgnFAIN2FsJgiJqgrN_91qlp_FTNEPj5MLRHryNayV8HEMVHxxEqewXM6Foyy_IjMx7-UP0a4q5Rn2xZGTnwWNAer9jYlUZvRNNXD617SlHBgeNlNFxbu53GOjyXPC1zMNrbDGj_ed3Iyu-mQw3LhJcFnZCWB227ta0mqHh9QDWQIn6vGrjXJshjCwF7yDTg2AnATg8JeCPOzzd8Hc8Fqtzi721YJk1h-ZsxW7nC1Cv24GHqMAiH0JX6D-l3UxI1oaM1QyVmuePMOzOLHzS4z2pDTm-aVjYthxCkXjA-Q0extRl6Ci_MefQkdC5TIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bizaiAC2VAb8SOniQjc3fDgGSqk0BejqP-ZuzR9fk9WGb7_Bfz0mCS33GXPbLfYipGEhbpbEsfQAqWwlvoEX9vfrrqPTqPE-64EFCfVh4pYmnhAJNS-CU6dnkYctqmbRRv0iEKYMla68LhdDlH7dDM-WJuzwuhAzyaW0qEwN1nwxNgxlNou02p9--8G_UNREea04pHo2bM-JxpE4pnCwPYLowGhYh6NufG3uEtW0WYeCeA3s6WEXk_km7ZoqkcNXU__c48wX7nkwUF_CrBk8xiO-AbzKCdrZH6Bb91TUWyCJCroWMhZFDg7M5nya__yX_gJmF_Ji8b2lWjNw8lWWsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز سه‌شنبه ۳۰ تیر با انتشار چند پست مختلف در شبکه اجتماعی تروث‌سوشال با بازنشر تصاویر و نوشته‌هایی از دو معترض به تازگی اعدام‌شده در ایران، مقام‌های جمهوری اسلامی را «وحشی‌» خطاب کرد.
دونالد ترامپ در یکی از پیام‌هایش با انتشار تصویری از یک پیام منتشرشده در شبکهٔ اجتماعی ایکس که به اعدام گل‌محمد محمدی، یکی از معترضان پروندهٔ موسوم به «میدان علیخانی اصفهان» اشاره کرده، نوشت: «آخرین مورد از ۵۲ هزار معترض بی‌گناه، و حتی بیشتر. وحشی‌ها!!! دموکرات‌ها کی از خواب بیدار می‌شوند؟؟؟»
رئیس‌جمهور آمریکا در پیام دیگری تصویری از یک پیام منتشرشده کاربری در شبکهٔ اجتماعی ایکس را منتشر کرد که در آن در کنار تصویری از عرفان اسفندیاری، معترض ۱۹ ساله اعدام‌شده در پرونده علیخانی اصفهان، نوشته شده که «لطفاً کمک کنید. لطفا صدایشان باشید».
آقای ترامپ در پیام دیگری، تصویری از یک زن گریان را بر حاشیه‌ای از پرچم در حال سوختن جمهوری اسلامی منتشر کرد که پلاکاری با این جمله را در دست دارد: «ما را نکشید».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77353" target="_blank">📅 18:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77352">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پیام‌های زیادی از اصفهان دریافت می‌کنم درباره شنیدن شدن صدای انفجار و لرزش شیشه‌ها
پیش‌تر اعلام شده که:
صدا وسیما: صدای انفجارهای کنترل شده مرتبط با مهمات عمل‌نکرده از ساعت ۹تا ۱۶ بعدازظهر امروز در جنوب و غرب شهر اصفهان، بهارستان و محدوده‌های صفه و شهر ابریشم شنیده می شود
مردم نگران نباشند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77352" target="_blank">📅 09:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77351">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8SxEZH0RAV9TqFIVkkdBd2ed7-o7XA19B2HJ3lOzr3pYXi1X8I2ojp7ugL8ts2xAfhoEICfgtcI1dAs6wTQz9MC3mjm-zz-AZRGL9Ormf7tCLvoGMc5SfVxgfe00nGIvLUNokIaIPoV1bvdOVRNStLH02Omx584X59-6ppR39Fs3CK5NORXncBSROAB_3GGl7SpiWEZ7usW4TvPrw-w7-zqPiSGNQ92UV7LowaqY0Eop82a24FiTbbdjcop4GUabQLdw5cDNt3sFbb6cevee2AO89YsbFn_7lmX98q0mK5cZOfHFZ3Ti8IYJs-gqq7ITGPA2oXMQJJSn02lmUdRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای سپاه: سامانهٔ راداری دفاع موشکی و یک هواپیمای اف ۱۵ در آشیانه دشمن در اردن منهدم شد
خبرگزاری فارس:
🔹
روابط‌عمومی سپاه: ملت عظیم الشأن ایران اسلامی! با استعانت از خدای متعال، در ادامهٔ عملیات پاکسازی منطقه از رادارها و سامانه‌های پدافندی و هموارکردن مسیر حملات موشکی و پهپادی گسترده‌تر و تکمیل شب سیاه راداری دشمن آمریکایی، رزمندگان غیرتمند نیروی هوافضای سپاه در ادامهٔ موج ۲۴ عملیات نصر ۲ در حملهٔ موشکی به پایگاه آمریکایی در اردن یک سامانهٔ راداری دفاع موشکی را تخریب و یک فروند هواپیمای اف ۱۵ را در داخل آشیانه منهدم کردند.
🔹
این منطقه جای متجاوزان آمریکایی نیست، ارتش کودک کش آمریکا برای پیشگیری از تلفات بیشتر باید منطقه ما را ترک کنند.
📝
گزارش تکمیلی این عملیات تنبیهی به استحضار ملت شریف ایران خواهد رسید.
ادعای سپاه: زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین ویران شد
خبرگزاری فارس:
روابط عمومی سپاه: با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای سپاه در ادامه موج ۲۴ عملیات نصر ۲ در پاسخ به تجاوز و تعرض روز گذشته ارتش کودک‌کش آمریکا به تاسیسات در دست احداث و غیرنظامی دارخوئین، زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون را در بحرین با چند فروند موشک کروز مورد هجوم قرار دادند و آن را ویران نمودند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/77351" target="_blank">📅 09:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77350">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فرماندار آبدانان: آمریکا با موشک به نقطه‌ای در کوه‌های اطراف آبدانان حمله کرد
خبرگزاری جمهوری اسلامی، ایرنا:
🔹
به گفته فرماندار آبدانان، ساعتی پیش دشمن متجاوز آمریکایی با چند پرتابه مناطقی در بیرون از این شهر استان ایلام را هدف گرفت.
🔹
بهزاد نورمحمدی صبح سه‌شنبه در گفت‌وگو با خبرنگار ایرنا اظهار کرد: دشمن آمریکایی با پرتاب موشک، به نقطه‌ای غیرنظامی در کوه‌های اطراف آبدانان حمله کرد.
🔹
وی افزود: خوشبختانه این حادثه هیچ‌گونه تلفات جانی در پی نداشته و دستگاه‌های مسئول در حال بررسی ابعاد موضوع هستند.
🔹
نورمحمدی یادآور شد: دستگاه‌های امدادی به محل حادثه اعزام شده و مشغول بررسی دقیق ابعاد تجاوز دشمن هستند.
پیام‌هایی که من از یک شهروند دریافت کرده بودم از ساعت ۲:۴۱:
سلام وحید جان صدای دو انفجار اومد چند دقیقه پیش
ما آبدانان هستیم ولی صدا خیلی دور بود بیرون شهر بود.
ظهر هم رد موشک تو آسمون دیده میشد
الآنم یکی دیگه
2:49 دوباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/77350" target="_blank">📅 06:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6445e1dc2.mp4?token=aZbxtMcUqEva1pzCd8d1Bfbok0oqalOzfN3zhu0qD3dPMGSvEil8xrG3lD3eg9b6d5dZf4_rZUMb4qxtTJoNNgDeSDppzUgQ05cb5AXbZXm7bZmNi3fGKR5xu_kLOy1dZLS4KaVwL1u2J7o318fy2cXTU5Bf9eCq_EhsIXagS7em_dj7bo4Y40fiYgUGjEBFeeR4AppRBY3sgjBldeaFVxbiP_C40wpPmi6jpuW_kmRuKOLIUhBGVXAF6M1-eKy2F_oBmECThPX4hswu6W4nXHaOnrnyqT_Ykk7YAWVBZXLmiJ1MocirnVC2jyclpgKdYrlotHgoDG2k_a16IkNo5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6445e1dc2.mp4?token=aZbxtMcUqEva1pzCd8d1Bfbok0oqalOzfN3zhu0qD3dPMGSvEil8xrG3lD3eg9b6d5dZf4_rZUMb4qxtTJoNNgDeSDppzUgQ05cb5AXbZXm7bZmNi3fGKR5xu_kLOy1dZLS4KaVwL1u2J7o318fy2cXTU5Bf9eCq_EhsIXagS7em_dj7bo4Y40fiYgUGjEBFeeR4AppRBY3sgjBldeaFVxbiP_C40wpPmi6jpuW_kmRuKOLIUhBGVXAF6M1-eKy2F_oBmECThPX4hswu6W4nXHaOnrnyqT_Ykk7YAWVBZXLmiJ1MocirnVC2jyclpgKdYrlotHgoDG2k_a16IkNo5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع حکومتی با انتشار ویدیوی بالا: سه پایگاه مهم آمریکا در کویت، هدف حملات پهپادهای انهدامی ارتش قرار گرفت
مرحله نوزدهم عملیات صاعقه ارتش
روابط عمومی ارتش:
🔹
در پاسخ به شرارت‌ها و نقض عهدهای مکرر شیطان بزرگ، بامداد امروز و در مرحله نوزدهم عملیات صاعقه، ارتش جمهوری اسلامی ایران، ساختمان‌های اداری  و آنتن‌های جهت‌یاب در پایگاه عریفجان، پارکینگ گروهی بالگردها در اردوگاه العدیری و ساختمان اسقرار نیروهای ارتش تروریستی در پایگاه احمدالجابر کویت را هدف حملات پهپادهای انهدامی خود قرار داد.
🔹
پایگاه عریفجان از بزرگ‌ترین مراکز استقرار نیروها و ستاد فرماندهی نیروی زمینی آمریکا در جنوب غرب آسیا و پایگاه العدیری محل استقرار بالگردهای آپاچی، شنوک و بلک هاوک نیروهای دریایی و هوایی  آمریکا است.
🔹
پایگاه احمدالجابر نیز نقش محوری در آماد و پشتیبانی ارتش متجاوز آمریکا در غرب آسیا دارد و تاثیر عمده‌ای در عملیات‌های هوایی و نظارتی این کشور ایفا کرده است.
🔹
ارتش جمهوری اسلامی ایران اعلام کرد، امنیت منطقه در پی شرارت های نیروهای تروریستی آمریکا مختل شده و  نیروهای مسلح جمهوری اسلامی تلاش می‌کنند در نبرد با آمریکا، امنیت و آرامش را به منطقه بازگردانند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/77349" target="_blank">📅 06:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77348">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/841c527612.mp4?token=RIz2guPQtw2wMFjZhTCl-AjSWLJFjn8FwMvYHz4Uww0DQHFnoxtJhhnSlOR_eHZProJofXEirV-m2lSLrejYvPbgdG_2KtoOca3Oi-tXIw9c2QU_DKq09lgt6NeaO5Jrh_vR29cyVe_E_L3hi_AAE02X3QuUAFY_OtDfIoy0mawumgpF7E3CyeOSkss3Zkm3Td_HI2vBhVWZ3t82WOzb9zO7bhCFZJLDusDGe8K2L7MEWmCzHmrxOG7OHaPDjBdFD5VtGWfnPolt9jzaEwFYXRMRSHa0vtnYZz4amgBqkaPZQKPVm_B9TBs4R_V_02ognovCmOrCIgycH5DJP8e3EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/841c527612.mp4?token=RIz2guPQtw2wMFjZhTCl-AjSWLJFjn8FwMvYHz4Uww0DQHFnoxtJhhnSlOR_eHZProJofXEirV-m2lSLrejYvPbgdG_2KtoOca3Oi-tXIw9c2QU_DKq09lgt6NeaO5Jrh_vR29cyVe_E_L3hi_AAE02X3QuUAFY_OtDfIoy0mawumgpF7E3CyeOSkss3Zkm3Td_HI2vBhVWZ3t82WOzb9zO7bhCFZJLDusDGe8K2L7MEWmCzHmrxOG7OHaPDjBdFD5VtGWfnPolt9jzaEwFYXRMRSHa0vtnYZz4amgBqkaPZQKPVm_B9TBs4R_V_02ognovCmOrCIgycH5DJP8e3EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: نیروهای آمریکایی مراکز فرماندهی نظامی ایران، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد و سامانه‌های پدافند هوایی را هدف قرار دادند.
ترجمه ماشین:
پایان تازه‌ترین حملات آمریکا علیه ایران
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دور دیگری از حملات علیه ایران را در ساعت ۹ شب ۲۰ ژوئیه به وقت شرق آمریکا به پایان رساند.
نیروهای آمریکایی مراکز فرماندهی نظامی ایران، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد و سامانه‌های پدافند هوایی را هدف قرار دادند تا توانایی ایران برای ادامه حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز را کاهش دهند.
عبور کشتی‌های تجاری از این گذرگاه حیاتی دریایی بین‌المللی همچنان ادامه دارد. از اوایل ماه مه تاکنون، نیروهای سنتکام به تسهیل عبور حدود ۹۰۰ کشتی تجاری و ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
نیروهای آمریکایی همچنان در موقعیت و آمادگی لازم برای پاسخگو کردن ایران به‌دلیل تجاوز بی‌دلیل علیه دریانوردان غیرنظامی که در پی عبور آزادانه و بدون مانع از این تنگه هستند، قرار دارند.
CENTCOM
اطلاعیه شماره ۳۵ سپاه:
شب سیاه رادارها و سامانه های پدافند هوایی آمریکا در منطقه
روابط عمومی سپاه:
🔹
ملت عظیم الشان و مجاهد ایران اسلامی؛ حماسه حضور در میدان و ۱۴۰ شبانه روز ایستادگی بی‌نظیر و پرشور شما چنان روحیه ای به رزمندگان اسلام و مدافعان از جان گذشته وطن بخشیده است که با لطف و امداد الهی هر روز حماسه‌ای نو خلق می کنند.
🔹
ساعاتی پیش عملیات بزرگ رزمندگان اسلام برای تنبیه ارتش کودک کش آمریکا به خاطر برهم زدن امنیت تنگه هرمز و تجاوز به نقاطی از میهن عزیزمان آغاز شد.
🔹
فرزندان شما در نیروی هوا فضای سپاه شب سیاهی برای رادارها و سامانه های پدافند هوایی آمریکا در منطقه رقم زدند و در موج ۲۴ عملیات نصر۲ با رمز مبارک یا رقیه (س)، به منظور هموار کردن راه عملیات گسترده آینده و از میان برداشتن موانع اصابت دقیق اهداف یک سامانه پدافندی و یک رادار آمریکایی در المحرق بحرین به طور کامل تخریب شد و از مدار عملیاتی خارج گردید و همچنین یک سامانه پدافند هوایی پاتریوت آمریکا در اَلرفاع بحرین هدف حمله همزمان موشکی و پهپادی قرار گرفت و نابود شد.
🔹
تنبیه متجاوز ادامه دارد و گزارش آن به استحضار شما ملت عزیز و قهرمان خواهد رسید
و ماالنصر اِلا من عند الله العزیز الحکیم
اطلاعیه شماره ۳۶ سپاه:
یک سایت راداری برد بلند، یک مرکز مخابراتی و سامانه های دریافت ماهواره ای، یک رادار دفاع موشکی و یک سوله آشیانه پهپادهای MQ9 منهدم شدند
روابط عمومی سپاه:
🔹
ملت عظیم الشان و قهرمان ایران اسلامی؛ در ادامه عملیات تنبیهی رزمندگان هوافضای سپاه و در راستای هموارسازی مسیر، برای دفع موانع عملیات هوایی و موشکی گسترده در مرحله دوم موج ۲۴ عملیات نصر۲،  امشب یک سایت راداری برد بلند، یک مرکز مخابراتی و سامانه های دریافت ماهواره ای، یک رادار دفاع موشکی ارتش کودک کش آمریکا مستقر در کویت مورد اصابت موشکی و پهپادی قرار گرفت و منهدم شد.
🔹
همچنین یک سوله آشیانه پهپادهای MQ9 نیز در پایگاه علی السالم مورد اصابت واقع و تعدادی پهپاد منهدم شده یا آسیب کلی دیدند.
🔹
عملیات تنبیهی فرزندان شما ادامه دارد. التماس دعا.
و ما النصر الا من عند الله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/77348" target="_blank">📅 04:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77347">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ICe2GEfg_3p-D6Lh6B8HBGZQZs_0i_qlMb6BUonCMYYzIKBWCjnRKLTww_VdXIa6KQqu1VfTdtt5q6G3zTs0zu2ErmyGOSUYNN9fHjcKMjYVY9M8ioqkhQWvdMDR-eUQRIPh8OBtHCPt-cW3_3n8QgUOHBwDJ5PM_QOX-UOzuvSOv9BdPKiqhBiwxjpW8QxUqMrPd4YZJTbFqPihEX-jLQub6FHyq-oSipMOiS_0AqGEk0R7PLbc6W177uPdYk7lkgA24cT8cmene2Za9-aU3LIiQRW3Ky8Yu05GJJk-8zVFLOuXAMSkR-aUW4qiROfjpLkf6tX9MVubt-nC63HG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
خبرنگار صداوسیما: حوالی ساعت یک بامداد در برخی نقاط شیراز صدای انفجار شنیده شد که بر اساس گزارش‌ها یک نقطه در شرق و دیگری در غرب شیراز مورد هجوم دشمن قرار گرفته است.
چند پیامی که من دریافت کرده بودم:
شیراز رو باز زدن
یجوری شیراز رو زدن که شیشه ما بدجور لرزید
سلام صدای دوباره انفجار در شیراز
شیراز دوباره زدن
خیلی بد زد
شیراز 1:21 صدای دوتا انفجار خفیف دیگه اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77347" target="_blank">📅 03:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77346">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5Px43ke5yJRD5IMqy21MWQNJy3NjLNG4ya5-1dPsAm5GmwYfkwIqiVCFfigG7le22JF3IvYKWJjqdOnPb3pmyIBXeuC4ZwhMMhoLFOjx6txp-f-X8_i5OTOmKIOcy7SBZdV-Pl5ny07Sy9xksmdACMt88N5sUDASERnRufY7HkMioXdJ9s-uOA9oT2-cAxiOxgJR3ZaaDCGcs9yvAyj2Q17IeYsyB09LU4U-GVXo5TndnTR29ztJ87EkKH7TEw-a-r4-IAxVMCPoZFO7UGEtzLNC_3qvaravZP7btZq_YujzBC0szViZbFeVfV5ZequlDRIWpajR0hoYQrr1BXh4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درباره تماس با نخست‌وزیر تازه بریتانیا: درباره نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌روبی تنگه هرمز و بسیاری موضوعات دیگر گفت‌وگو کردیم.
ترجمه ماشین:
گفت‌وگوی بسیار خوبی با نخست‌وزیر جدید بریتانیا، اندی برنهام، داشتم. درباره موضوعات بسیاری گفت‌وگو کردیم، از جمله روابط فوق‌العاده‌ای که با بریتانیا داشته‌ایم.
در آینده‌ای نه‌چندان دور برای گفت‌وگو درباره موضوعات مورد علاقه مشترک دیدار خواهیم کرد. نخست‌وزیر کار بزرگی پیش رو دارد، اما قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا نیز برای کمک در کنار او خواهد بود!
درباره نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌روبی تنگه هرمز و بسیاری موضوعات دیگر گفت‌وگو کردیم.
این تماس جالب بود و بسیار خوب پیش رفت. برای نخست‌وزیر برنهام آرزوی موفقیت کردم: موفق باشید و خدا به همراهتان!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77346" target="_blank">📅 02:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77345">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKMYSFkgPQHdjCb6zoFPG6Xl8qFLLkMEX5LLZucbZaZz6IV7ZvyVjtOhoqNLhGIK9p7GzXkzUGKHeh6h70Sj2NurPae5k77yAabm5_5R56KIpHvd2w3XtYqMCu5L8P0pZ2f8p8NJJTgG-ry-3wiLteoCFKz6bU3vBJxEIdfUPNhmc5yArkuwS7L8ZZRbcigX6FqMGitfQqn-CHVRZBFBly1nf1Z--HbPtVBU-249P4Q61Qc-df6y2QgwA5ZjGq5OOOwheJwGiuVi5UsXpxkmcaUcKllF4K7xDgzrsARJyLGyUzviJVDyQ3iZzs4App0rRtjfMlK62YnekWaAyFDi4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد گزارشی از یک حادثه در فاصله ۸ مایل دریایی شمال شرقی لیما در عمان دریافت کرده است.
این سازمان افزود گزارش‌های متعددی دریافت کرده که بر اساس آنها، یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده در تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77345" target="_blank">📅 02:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77344">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس پایگاه هوایی ۲ انفجار ۰۱:۴۷
بندر ٢ تا شنيدم ٣٠ ثانيه پيش
1:47 دو انفجار به شدت قوی در پایگاه هوایی خیلی شدتش زیاد بود بندرعباس
بندرعباس ۱:۴۷ دو صدای انفجار شنیدم
درود آقا وحید دوتا انفجار وحشتناک ساعت ۱:۴۷ دقیقه بندرعباس
همین الان ساعت ۱۱:۴۶ انفجار فوق شدید بندرعباس
۲ تا انفجار وحشتناک بندرعباس ۱:۴۷
صدای ماشین‌ها درومد
صدای دو انفجار الان بندرعباس ۱:۴۷
بندرعباس ۱:۴۷ صدای دو انفجار
تک انفجار شدید بندر
سلام الان صدای دوتا انفجار بندرعباس اومد
سلام وحید جان صدای دوتا انفجار پشت سر هم اومد بندرعباس
ساعت 1:48 بامداد
بندرعباس ۳ تا انفجار شدید
صدای ۲ تا انفجار سمت پایگاه هوایی بندرعباس
سلام صدای دو انفجار بسیار شدید بندرعباس ساعت ۱:۴۷
درود وحید جان وقتتون‌ بخیر
بندرعباس ساعت ۱:۴۸ دو صدای انفجار بلند.
بندرعباس ساعت 1:47، دو سه بار سنگین زد
سلام وحید جان الان دو تا انفجار سنگین سمت فرودگاه بندرعباس آمد که شیش ها لزیدند 1:48
سلام وحید خان بندرعباس ساعت 1:46 چندتا انفجار پشت سر هم
سلام وحید بندرعباس همین الان صدای 2 انفجار خیلی وحشتناک
اقا وحید  ۳تا انفجار شدید قشم ساعت ۱:۴۶
وحید‌ داداش
حوالی۱.۴۷ اینا دو انفجار مهیب. اومد
فک کنم پایگاه هوایی بود
ثانیه پیش هم زدن
حدودا ۴ انفجار شد
تعداشو دقیق شمردم کمی با هم فاصله داشت
در حد هر کدوم ۳۰ ثانیه
ولی همش از یه سمت بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77344" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77343">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیام‌های دریافتی:
۱:۴۵ قشم صدای انفجار همراه با لرزش
قشم من چهارتا صدا شنیدم، نمیدونم توهم زدم یا واقعی یود چون خیلی خفیف صدا اومد ۱:۴۵
چهار انفجار فعلا بندرعباس
وحید جان
قشم چهار تا انفجار ۱:۴۵ دقیقه
صدای انفجار بندرعباس ۱:۴۵
سلام وحید جان ستا انفجار همین الان بندر عباس ساعت ۱:۴۵
بندرعباس الان دو تا صدا آمد ولی صدا دور بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77343" target="_blank">📅 01:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77342">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">منابع حکومتی
منابع محلی لحظاتی پیش گزارش دادند برای دومین بار طی بامداد امروز صدای انفجار در بندرلنگه شنیده شد.
چند پیامی که من دریافت کرده بودم:
سلام وحید جان بندر لنگه دو بار زدن
صدا و لرزش زیاد
ساعت ۱۲ و ۴۰ دیقه
ساعت ۰:۴۰   صدای انفجار در بندرلنگه شنیده شد
درود وحید جان
صدای انفجار در ساعت ۱۲:۴۰ بامداد از بندرلنگه اومد ۲ بار
گویا هدف، نیروی دریایی سپاه بوده
صدای انفجار ۲ بار در خونه لرزید بندر لنگه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77342" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77341">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پیام‌های دریافتی:
۳ انفجار در کنارک همین الان
۵تا انفجار سنگین چابهار ۱.۲۷
مجدد چابهار صدای چندین انفجار میاد
چابهار ۱:۲۷ دقیقه صدای ۲ تا انفجار اومد
ساعت 1:27 چهار انفجار پشت سر هم دیگه چابهار
کنارک 1:28 دو انفجار
۱:۲۸ دیقه کنارک دو بار صدای انفجار اومد
🔄
کنارک 4 انفجار دیگه
خیلی سنگین بودن این چهار تا انگار خونه رو سرمون خراب شد
۴تا دیگه چابهار همین الان ۱.۳۰
۱:۳۰دقیقه ۴ بار چابهار زد
نمیدونم کجاست اما از سمت دریا بزرگ دورتر
۱:۲۹ چابهار ۲ تا انفجار دیگه اتفاق افتاد
دوتا پشت سر هم و باز 3تا پشت سر هم 1:30 چابهار
صداهای شنیده شده در چابهار و کنارک: ۵ انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77341" target="_blank">📅 01:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77340">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wgd8KewQExeEWnfzOEeBD3kCqpPAnDgfSCcAz4m7oLRso84uCqRkTMZI1Xed9Fbh7nonwRYOaoZReig07ShnGUKSou15AfNZAayq9Yip27IQIj082_0erUWv-CjZaTcbl49BOd0oaAnE8JNek_I4My9g6ph7dxUeJ0BWIJEpNqEnt71EOIUmvjm1ZA0BxqcejlHQxdf-DbbdMCfXj5eQFoUHeO7M5gwUWBfSSUp1xZfFbApHCDSKEgVagWHSbj1KTINitD9IPfniwxyVjHMcKSYU2JtdipmvAWjG70DqiMD8y28rC4EwyE9p6XTzJ2O7aCE55WtvUnnoF7rM8dTJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر از شنیده شدن صدای دو انفجار در شهر اصفهان خبر داد.
دقایقی بعد، استاندار اصفهان اعلام کرد که امشب حمله‌ای به شهر اصفهان صورت نگرفته است.
@
VahidOOnLine
فارس:
استاندار اصفهان گفت: امشب حمله‌ای به اصفهان صورت نگرفته است.
وی ادامه داد: در حال بررسی علت شنیده شدن صدای انفجار اعلام شده از سوی شهروندان هستیم.
تسنیم:
معاون استانداری اصفهان: هیچ گونه تجاوز دشمن یا انفجار در سطح شهر اصفهان و سایر نقاط استان نداشته‌ایم
من هم چند پیام مردد داشتم و از این رو فکر می‌کنم صدایی شنیده شده ولی مطمئن نیستم که دلیلی نظامی داشته یا نه.
منابع زیادی هم هستند که هر روز کلی خبر دروغ تولید می‌کنند و از این رو اعتنا کردن به پیام‌هایی که بعد از چرندیات تولیدی اون کانال‌ها ارسال میشن هم خیلی سخته.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77340" target="_blank">📅 01:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77335">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NIRkA-yQXWyA36EANPdDCAh7-8D6SSG5N8OcfRVn_BYFmmLcUn3RWQlEAcr5Uo28R8HuKtscX52f-UpxQfNBEAkwDJIckL8hzs0yIvowAwpN3WtJuxqagehXM_1grepoi17ZoYmRqGJoVA07zrmp7PrNgtlT1_t9lDihodNOSfoVGuthMR6nOWNPK-ZURAJbz9MPgf1Ja07A-i_5gcX3KcEBloQxZEfKjd0x6aOvUu9-l0KlG_0TWBQjMDQNh2bA_3lVKdNlzltJVpVVZTIPxp69miF7QJngkkHKgy1idfo07ZL4FI0a_u5P_dl4gKhgz6Nl5kXa4nkQOQktNyXpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UJO4YYkAoMIa9YokZB_esc7fHeJIjeFqwi8tqb_iguXsZJ__eLCcNlEGVjVEE_OCowUJGsq8EBbwIH4nnUnLRE6HHRdkkBUJb96Z5WMLXqo0XzLZjdKjaGenxMLsk4gVOPnx7ug5i2AVQMDNBusRiBEwx9svGiFEN0PLG4zxzscKoHoHP0iBSHTHsI86BlNbPK2-grGiWHJGkSnr9SPf7yRR3xXQVkfotm0HJ0WKNvHftZphNxId3vXR3g28LmUlunV_UtPqTwyr9uOZoII_2adPxvgUpphjOsw96rw8TXAfr6uvi_guTjUKAwVICOdq_8I_MSwg-Jb1d0W4DOpRSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kiuKIcg1QKKrqskDkvTnqB_0NTnQUh4EkIl7-eSXhr1gWdw8Oy-hgGrINxI6Hg1cq1oid50wLyo7DBwSItki6wLKoQa4xXQ4Pr4po1WQnXW-oDDOzIz8w5iGS2tfuT-6PykkZb9m4fSDjDbNNfW4kXyasL79TUQKj1DU_Yw1SPiCKMCDXyaD89sRCh6x6Sdxb7LSHlKKTiiGHdjA9gIyyhILOyzt5zzuT7o76ndoDxcwmk8avM5bmSPMEUGFiDk8o2fQnu4XVzWwfLZ_M-27y5RI5Bjx0xj2MkVxZWLKwo5XITQjjWvZHO8tWrNq09EZixcbr07HUlmRlrE09rXN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c2WAPrdtqnmbVXEm_kqJcbSM6Vi81E4Xc7A5Bu_Du1E9yug4MXRnqHC3FCN0BDjwZoZ1YL-Z5cy4aqPWRul3ZINOR-2dINUXv6r3z8LcsuuJ98wjTmlAHi9-_Rf1UsVfMUaaYDaU_G3QbBzZwL0X0h8wptKBKss3AZLNq95WUTlUL1Ldex6YL8HoXzWZoY38eE4G_fNt8I5FqJECzmkxQGw_4l2UI6HKnYinVQLy2oH5e_3IMu5BuQmhCU9hxxsRXked95DPqciPWIT5-S4CltGrm002ycNpUixmWUUaRfWzJ6oTaol3LKyUIk-caaGY9xKknQd3_C1eq0N48N5ihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tOs3MEBM2hNS0udkP-mQ5a9bNHfWhdnkEFxZ34Y2ZPbk4mCvpv-SaYR7VUynbs3DI_OT0MPJdQMg86tBKHmjJx03G0Ud5L-NAajJidLm-YWZ8Usf48j9iMgZyjT6mKh5FAMQw49_5PNUWLjjaSGxh4TfxSuzNRssU77LD2lpFExN94fXDu0lb6bXNAKz4yjbRzvy2k5U95wYY5nw6Lf7dwNBBHZS3Sw3TOxncQ7igv6KLpPPR5q8eF_WTakNYd_EEovNTczTQRAJ4qL1KxHIucm3QjxacLemI6ZplaDrhhvo9w9-iEUmMYCAX7tKMcxjA4B6lXkp8R7cPW3rOdWoSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Vahid
'هدف قرار گرفتن نقطه‌ای در کوه دراک شیراز'
تصاویر دریافتی از شهروندان با شرح بالا، سه‌شنبه ۳۰ تیر حدود ساعت ۰۰:۴۰ بامداد
Vahid
📍
میگن
اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77335" target="_blank">📅 01:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77329">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PTkqPXP-xtpZOA9aGKRFrxN6ZoAKBd1U5YLf_-oZu3FxDMARgBXpBL-Y3Z3qPEV_xatc8G5HcK5UpgeMB4srbRNiHinwXunXajJXVNPi9nq9gBsklhpUI158L_XpUHCwyKpOxkbPO9vXemHeoEyBZfxF9hPINNHa1RPLvo8D1tFv8F8kscrV4wIFiqUgawHvCNrENwTvlNHwY5zHJY_tzVRBlSvkMeQeDB-p4Nw8DEUsGnXfZIw_mQA8IyzV4DLLK75ka3cboOMQwtIRczv6brCXp_Bd1zyPA6qPvRxBAuFwJ8UvQZE8o_out9K8BEMQbbkwmpNOeIR17nQ2Hz5kUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TkheQUqzLbkNjwjB4DickaCESdxiUDzDMJylqhkZKDY2MMEXtjargGrqnQJgGdwsfuTWFc-U8_1mAqGKxp5AUZn4kYdzb7jsrzvjPcWo4HYibiGClL7lZsENOXnLYxIdu55VCVk2RGKe7xmN-_ZAgL613tZ5V9bex1UupVx1xiEnc7UaEytQTuDLTBNCVB8i-jJDGW5trSoV_bTV3XJgf6FEP4qpqtiraUyARUBHoQyHSI5TauKcLS2QlwMGNUwBghguz7IZLPtTKm2DvPyBSYzaQohqBiZFiaBlCkCmVZDRf9LKnVO31KzwloW_Qj3FcXcJ511VrMHyIa0pERF0oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی درباره صدور هشدار در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77329" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77328">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده ده دقیقه پیش:
سلام شیراز همین الان صدای انفجار اومد12.37
شیراز همین الان صدای انفجار اومد
شیراز همین الان صدای انفجار مهیب اومد
🔄
پیام‌های رگباری الان:
همین الان شیراز و زد کلفت
همین الان صنایع صدای انفجار اومد
سلام وحید جان
شیراز سمت صنایع رو زدن ساعت 00:45
00:45 شیراز صدای انفجار
فکنم صنایع الکترونیک رو زدن
همین الان شیراز صنایع رو زدن
شیرازو زدن همین الان
سلام وقتتون بخیر
ساعت ۱۲ و ۴۵ دقیقه بامداده
شیراز همین الان صدای انفجار اومد
شیراز صدای انفجار
همین الان شیرازو زدن رکن آباد خونه لرزید
فرهنگ شهر شیراز صدای انفجار مهیب  ۰۰:۴۵
شیراز صدا اومد
سلام یدونه تک انفجار صنایع شیراز ساعت 0:45
شیشه ها لرزید
ساعت ۰۰:۴۵ صدای انفجار از شیراز
شیراز ۱۲:۴۴
احتمالا صنایع صدای انفجار
درود وحید جان
الان صنایع الکترونیک شیراز رو زدن
این دومین انفجار امروز تو صنایع هست
شیراز الان 00.46 زدن
12:45 معالی آباد صدای بلندی شنیده شد ( انفجار یا بمب نمیدونم)
چهل و شش دقیقهٔ بامداد صدای جنگنده و انفجار در شیراز
سلام وحید. ساعت 00:46 محدوده صنایع الکترونیک، صدای انفجار شنیدیم.
شیراز صدرا همین الان صدای شدید انفجار اومد
شیراز صدای جنگنده اومد روی کوه دراکو زد انفجارشو دیدم
همه فکر میکنن صنایع رو زد ولی بالای کوه دراک بود
امروز ساعت ۵ هم از بقیه شنیدم که صنایع الکترونیک شیراز رو زده بودن
سلام شنیده شدن صدای انفجار صدرا ۱۲:۴۷
همین الان صدرای شیرازو زدن
شیراز صدای وحشتناک بلند همه جای شهر شنیدن یا صنایع بوده یا کوه دراک
وحید ساعت ۱۲:۴۵ بعد نیمه شب صنایع الکترونیک شیراز رو زدند صدای انفجار اومد
۰۰:۴۵ صدای مهیبی اومد، ما ابیوردی هستیم ولی صدای انفجار تا اینجا اومد
سلام همین الان حدود ساعت ۱۲:۴۵ شیراز صدای انفجار شدید اومد
سلام الان شیراز صدرا هستم صدای انفجار اومد
شیراز  0:45 صدای انفجار اومد
سمت فرهنگ شهریم ما
سلام ۰:۴۵ شیراز سمت شهرک گلستان صدا انفجار اومد
شیراز زدن نمیدونم کجا بود ولی من از فرهنگشهر شنیدم صداشو
سلام وحید جان  دکل مخابراتی کوه دراک شیراز رو با جنگده زدن ۰۰:۴۰
من رو پشت بام بودم دکل کوه دراک رو زدن
صدای جنگده اومد بعد زدن
خونه ما معمولا وقتی صنایع رو میزنه صداش نمیاد، این انفجار مشخص بود خیلی عمیق  و بزرگ بود که انقد واضح صداشو شنیدم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77328" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام‌های دریافتی:
چابهار صدای جنگنده سطح پایین میاد الان
سلام صدای انفجار شدید در چابهار ۰۰:۰۲
۰۰:۰۶ دیقه صدای انفجار اومد کنارک انگار دور بود
چابهار ساعت 12 شب دوتا سنگین زد
🔄
چابهار دوباره صدا جنگنده :۶
انفجار سنگین :۰۷
الان زدن چابهار 12:07
چابهار الان صدای انفجار شدید
درود چابهار الان زدن خونه لرزید 00:07
دوتا دیگه هم زد
چابهار همین الان دوباره زد
انفجار خعلی سنگین ۱۲:۰۸
وحید ۰۰:۰۷ انفجار شدیدتر
کنارک همین الان صدای سه انفجار
سلام چابهار الان ۳ تا صدای انفجار اومد۰۰:۰۸
چابهار همین الان دوباره زد
۳ بار شد
🔄
صدای ۲ انفجار دیگه در کنارک
همین الان یکی دیکه چابهار
صدای انفجار دوباره در چابهار
صدا جت امام علی زد یکی ۱۲:۱۱
باز یکی دیگه زد همین دقیقه
پشت هم داره میزنه
جنگنده ها در ارتفاع پایین در حال پرواز هستند
داداش امامعلی چابهار رو مثل اینکه زدن
سلام آقا وحید طرف های امام علی نه خود [پایگاه] امام علی رو زد
دو تا چیز شبیه فلر از سمت دریا اومد چابهار
نمی‌دونم چی بودن
منابع حکومتی:
فرماندار ویژه چابهار از حمله هوایی دشمن به شهرهای کنارک و چابهار در بامداد سه‌شنبه خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77327" target="_blank">📅 00:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WWUlVTdihMcndKHMr7I6x-kiT8bNInGus1UihQIW9zec3Iwkijya7mcLOoP1J-4uYpsW6LoTA61JZySye64V2IJ_j4r3bs3sBBtGIHinan99wPEo6XyTlIFqM-1uQyuOeCtDz4iG4Hju3DEwii96m4xypwMfAKKm472PBKfvmyKRNek1-J7ct5oIJ8uzzqd2LNPXbumirPjDyT2h1-Lv-6dmuV0k6UmdMwlM3MeDmlmWms-hVNRn2cCz0P290wDUv2yKacSEUs0VGWvBeMx_X0Mw28bbHwnme64Q9fDtc87SLICuzaRaAwCpv0NSTGguCxf4uBq8OgEnmtMqln4_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۴ بعدازظهر به وقت شرق آمریکا [۲۳:۳۰ به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور جدیدی از حملات علیه ایران را آغاز کردند. هدف از این حملات، تضعیف بیشتر توانمندی‌های نظامی ایران است که برای حمله به کشتیرانی تجاری در تنگه هرمز به کار گرفته می‌شوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77326" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پیام‌های دریافتی:
صدای یک انفجار الان بندرعباس
صدای انفجار مهیب بندرعباس ساعت 22:33
همین الان ۱۱:۳۴ بندرعباس صدای انفجار شنیدم فکر کنم
سلام وحید جان ، بندرعباس صدا اومد الان
بندرعباس انفجار همین الان
سلام ساعت یازده ۲۳:۴۳ بندرعباس موج انفجار
انفجار در بندرعباس
بندر انفجار ۱۱.۳۴
ساعت ٢٣:٣۴ صدای انفجار نسبتا شدید بندرعباس
انفجار شدید بندرعباس ۲۳:۳۴
بندرعباس الان یدونه صدای انفجار اومد
بندرعباس ساعت ۲۳:۳۴ صدای انفجار شنیده شد
۱۱:۳۴ صدای انفجار بندرعباس
وحید سلام ساعت ۱۱:۳۵ بندرعباس یه انفجار خیلی شدید امد
بندرعباس صدای شدید انفجار همین الان 11:35 الهیه جنوبی
سلام صدای انفجار بندرعباس ۲۳:۳۵
بندرعباس الان صدا اومد تقریبا شدید بود
بندرعباس صدایییی وحشتنام ۲۳:۳۴ دقیقه دو تا انفجار
بندرعباس ۲۳و۳۵صدای انفجار اومد خیلی سنگین بود
سلام آقا وحید ساعت ۲۳:۳۴ دقیقه صدای انفجار اومد بندرعباس
ساعت ۲۳:۳۷ دقیقه یه صدای انفجار دیگه از سمت دریا اومد
یک ربع پیش از پیام‌های بندرعباس خبرگزاری فارس نوشته بود:
دقایقی پیش صدای چند انفجار از حوالی سیریک در شرق استان هرمزگان شنیده شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77325" target="_blank">📅 23:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XFyPZBf9qQUpsTsKq-yPm28VTZAWX5ZC6mz1v5GvUhZ67g8f9TCaktbSYEVQP73270RiVVvVrGjTOzLxHWmQhJb41IVtpf87NO5SC95ZBrfxk-Em7sQy6EFUG58eghfx6IGW9U2Sf7N4_MluqduaQeLxZuxz5iOF8afyMnNvttkDTyZfI1YjEcg-j7iyo7db9oNUx9dY7Xfv2AGweMYn50sJoJ2FGj_aYwKey1ZeQYHZbz_oDGoxLICOtrDlM_bxjCWf3aryOsxOadbC-wor6SQ6bb1R5-5-t0UpWFatDyWcpwqDg2WT_x1-VlqZdUAEnJxz8oDStEoB7_KeVoAFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب فارسی وزارت خارجه آمریکا شامگاه دوشنبه ۲۹ تیر با انتشار یک هشدار امنیتی از شهروندان آمریکایی خواست در پی افزایش تنش‌ها در خاورمیانه، هرچه سریع‌تر ایران را ترک کنند.
در این هشدار آمده است که وضعیت امنیتی منطقه همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد.
@
VahidHeadline
خبرنگار اکسیوس، ترجمه ماشین:
یک مقام آمریکایی درباره گفت‌وگوهای احتمالی آتش‌بس با ایران به من می‌گوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را به‌دلیل نقض تفاهم‌نامه و ادامه اقدامات تروریستی‌اش در تنگه هرمز مجازات کند. علاوه بر این، رئیس‌جمهور ایران را به‌دلیل کشته‌شدن اخیر سربازان آمریکایی مجازات خواهد کرد. این ضربات ویرانگر تا زمانی که رئیس‌جمهور صلاح بداند ادامه خواهد یافت، اما گفت‌وگوها میان دو کشورمان همچنان در جریان است.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77324" target="_blank">📅 23:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b98202fb7b.mp4?token=h8RPIIGjcZZt1SxFiSUvo3ug6ZXL6lrD7lGdtrLDqhEZOuPQqzDT7jHmv8BHL5EAOSB0BelBdl84AQcfdxunAwURk4gVEQgygxHmvEqFk6WXJ2fG5PYAaUDCpZB9tMXV18w2z0UAs79gaAtasOQY-Z9HdY1V4IeTzzA7rKjGgHW0Zu8A3aBWFJiVqCo3BQg6O6KmBb5pbADn99OvJgYDofLIX-rO43Jnr8NE1IBc11t335Na5uyZXeJHcKqvHfmBR23girl8785YnWKd_dDTBKxBssHlMYXEfvQ9ZJVj72AvaT7jljOmTu2tSgS5mwAs3UX2yinLLubSWKHTZjwSKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b98202fb7b.mp4?token=h8RPIIGjcZZt1SxFiSUvo3ug6ZXL6lrD7lGdtrLDqhEZOuPQqzDT7jHmv8BHL5EAOSB0BelBdl84AQcfdxunAwURk4gVEQgygxHmvEqFk6WXJ2fG5PYAaUDCpZB9tMXV18w2z0UAs79gaAtasOQY-Z9HdY1V4IeTzzA7rKjGgHW0Zu8A3aBWFJiVqCo3BQg6O6KmBb5pbADn99OvJgYDofLIX-rO43Jnr8NE1IBc11t335Na5uyZXeJHcKqvHfmBR23girl8785YnWKd_dDTBKxBssHlMYXEfvQ9ZJVj72AvaT7jljOmTu2tSgS5mwAs3UX2yinLLubSWKHTZjwSKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهرداد گودرزوند چگینی‌، نماینده شهرستان رودبار در مجلس شورای اسلامی می‌گوید که در تحولات اخیر، این ایران بوده که ابتدا توافق آتش‌بس میان ایران و آمریکا را نقض کرده است.
او در پاسخ به سوالی درباره توقف مذاکرات به دلیل نقض آتش‌بس گفت: نمی‌دانم گفتنش درست است یا نه اما اول ما حمله کردیم و بعد آنها سیریک را هدف قراردادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77323" target="_blank">📅 21:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77322">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82071ea2df.mov?token=d4HKRMYZrsB-2lPYO80qZaEYZhphz9HvNoMRNuSeejPoHIXlcz9NWPqU3tIoPi5Pi8nGwbenGm-8PsQCc5_b6Qvqtw1XBPlLrdkq_bnehR6YIaYQ4U729k35scMNcW-vF7oYZAxOvw1M37sws5iFKpY75bOCDMBADd5Mqj7JtD2SeSUlw9ArPF0UAwqiC-fFG3MSL48I_PMfb6jjbwo4wucwjbwpqYV422yH_vDw6EFCP4Sc67LDoZGYCO8wu_UIApYyUIzqvCDnWZVTYMBhcnRwm_S8qfEDHPnASu_Gzd0vtpDMpp-ESh3YEmkSpw860vDkydzFAlmc-xUM1oV9OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82071ea2df.mov?token=d4HKRMYZrsB-2lPYO80qZaEYZhphz9HvNoMRNuSeejPoHIXlcz9NWPqU3tIoPi5Pi8nGwbenGm-8PsQCc5_b6Qvqtw1XBPlLrdkq_bnehR6YIaYQ4U729k35scMNcW-vF7oYZAxOvw1M37sws5iFKpY75bOCDMBADd5Mqj7JtD2SeSUlw9ArPF0UAwqiC-fFG3MSL48I_PMfb6jjbwo4wucwjbwpqYV422yH_vDw6EFCP4Sc67LDoZGYCO8wu_UIApYyUIzqvCDnWZVTYMBhcnRwm_S8qfEDHPnASu_Gzd0vtpDMpp-ESh3YEmkSpw860vDkydzFAlmc-xUM1oV9OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: موشک‌هایی در آسمان ارومیه
آپدیت:
ارتش اردن شامگاه دوشنبه ۲۹ تیر حمله موشکی به این کشور را تایید و از رهگیری موشک‌های شلیک شده به سوی این کشور خبر داد و اعلام کرد که سه موشک از مبدا ایران که پادشاهی اردن را هدف قرار داده بودند، سرنگون کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77322" target="_blank">📅 21:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb11afb901.mp4?token=RLUxCYEN2aiPIJZZKCwGLdkYq0LOiR9oCsWJ2G9edJEHUn2AfPP3VzwdPAAz_5TMf0g8suQ1t58cYcSGxzQca-_-yPKrGh9I_ZuuX4feAxfcx-uYhfQmbCqhaSGvR2APgkd0PW0ZN6scM76-uVATjSANjX95OFzDNWn0a3BMd_vHGUBU-b-oTmm_gfDAWR1_8_yOMmTYhsZJaqCeKYQBSdGFBTnVjmgyeEcB-qnoWQj0kOgAo_B5lu-Zja4Rly-FQoN63Sq8YLOBMav1Nz5vojKUxxHjYmSugOUqnctSr7onTq-JbyCS63Lq3NvP4b5_YvYEyiihQOQ-wE1gQ1opFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb11afb901.mp4?token=RLUxCYEN2aiPIJZZKCwGLdkYq0LOiR9oCsWJ2G9edJEHUn2AfPP3VzwdPAAz_5TMf0g8suQ1t58cYcSGxzQca-_-yPKrGh9I_ZuuX4feAxfcx-uYhfQmbCqhaSGvR2APgkd0PW0ZN6scM76-uVATjSANjX95OFzDNWn0a3BMd_vHGUBU-b-oTmm_gfDAWR1_8_yOMmTYhsZJaqCeKYQBSdGFBTnVjmgyeEcB-qnoWQj0kOgAo_B5lu-Zja4Rly-FQoN63Sq8YLOBMav1Nz5vojKUxxHjYmSugOUqnctSr7onTq-JbyCS63Lq3NvP4b5_YvYEyiihQOQ-wE1gQ1opFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره پرتاب موشک از تبریز
ویدیوی بالا: شلیک موشک از [...] تبریز ساعت ۲۱:۲۴
صداشنیدم تبریز موشک زدن 9:25
میگن از [...] بلند شده
همین الان از [...] تبریز ۲ تا موشک فرستادن. ۲۱.۲۵
همین الان دوتا موشک از تبریز فرستادن  21:24
از تبریز دو تا موشک شلیک شد الان
صدای شلیک موشک ساعت ۲۱:۲۵ از تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77321" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77320">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c8221ff7b.mp4?token=IZCMzQnheqkIzVtgl1Yp3JmGfYgmRx-jsc3LtDWFnh3dxkQiLQW6gOpjhGY1SAg1G6Q_sOPGYRvAqH5ZlIZCQgTK3slttysHrU4RJ_ijcupffFcxQlfxMxXLasvWF8QagxxyVysflOpEwwBtcQ7J6T-dX_fyfZtOXyAVS1Q6B8YcofaqJmQhW6Yx3jmbxDH0BQGrImiaYjCOSPB_mB8oXkSqDH5aOiaNZ0Oye1zqv8sq-G-hApq9LgjRF3TlwKdou7kIYXTqH1Aw5LoF8uDtfhRMYotbBfP4RJ8c_NJxQVesmKrpDFbUNZ-8-20UVecjN5bpUmlHBxyWFeelWjIiMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c8221ff7b.mp4?token=IZCMzQnheqkIzVtgl1Yp3JmGfYgmRx-jsc3LtDWFnh3dxkQiLQW6gOpjhGY1SAg1G6Q_sOPGYRvAqH5ZlIZCQgTK3slttysHrU4RJ_ijcupffFcxQlfxMxXLasvWF8QagxxyVysflOpEwwBtcQ7J6T-dX_fyfZtOXyAVS1Q6B8YcofaqJmQhW6Yx3jmbxDH0BQGrImiaYjCOSPB_mB8oXkSqDH5aOiaNZ0Oye1zqv8sq-G-hApq9LgjRF3TlwKdou7kIYXTqH1Aw5LoF8uDtfhRMYotbBfP4RJ8c_NJxQVesmKrpDFbUNZ-8-20UVecjN5bpUmlHBxyWFeelWjIiMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل‌ها و پل‌های تخریب شده در حملات آمریکا، روی نقشه
در جریان حملات اخیر آمریکا که عمدتا بر جنوب ایران متمرکز شده، چند پل و یک تونل و یک ایستگاه انشعاب راه‌آهن در استان هرمزگان هدف قرار گرفت که خسارات جدی وارد کرد.
این پل‌ها و تونل در مسیرهای دسترسی استان هرمزگان به استان‌های فارس و کرمان قرار دارد و تخریب آنها باعث توقف تردد در مسیرهای بندرعباس به سمت شیراز و همچنین استان کرمان شد.
تونل شهید میرزایی در محدوده گلوگاه در مسیر بندرعباس به سمت حاجی آباد یک روز بعد از تخریب هر دو دهانه رفت و برگشت باز شد. در مسیرهای دیگر که پل‌ها هدف قرار گرفت، مسیرهای جانبی پل‌ها به طور موقت مورد استفاده قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77320" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77319">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omMQmBGTcm0Xs0klLW5k60HgV3jX_DFFcR0dTeVl63JTX29c0KMEe5zfKKGLr8uXAmIOI2ywVc2HFP1Bdjmbaq1vpCAoNRnqJ_mAF17H9siKr6QV9mV_brk8vBegl-aHT--yzzn8UfkJkmmnYfY7wQp4Bzubxs__v8RgDJEr2hfVSTwzYlYAIyDNXK5bs9M1UWa8dOh73Z1Pi-s5Fe1A76TNQSocn_g1gaVWgw6OWMHJWxaQ02buVjvYB_-K7pDYo74MTauykBiNL47-C5zBBK35s2qYlcyx5c6JmUlij885cCINblS0ziQYZZ9Qvtlox6dVBP0utNtSqVn-t1_z8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین برابر خواهد پرداخت! این دستور به پیت هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک ارتش، و تمامی فرماندهان نظامی ابلاغ شده است.
رئیس‌جمهور دونالد جی. ترامپ
Every time Iran kills an American Soldier they will pay for that killing many times over! This directive has been passed on to Secretary of War, Pete Hegseth, Chairman of the Joint Chiefs of Staff, Daniel Caine, and every Leader in the Military. President DONALD J. TRUMP
realDonaldTrump
ترامپ در پستی دیگر نوشت:
بنیامین نتانیاهو تحت هیچ شرایطی، به هیچ شکل و طریقی، در ایالات متحده آمریکا بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را کشته و طی ۴۷ سال گذشته سربازان آمریکایی و دیگران را به قتل رسانده است.
تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این
چرخه بی‌سابقه مرگ و ویرانی
کشاندند؛ موضوعی که رؤسای‌جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!
رئیس‌جمهور دونالد جی. ترامپ
Benjamin Netanyahu will not be arrested, in any way, shape, or form, while in the United States of America. He is fighting against the Islamic Republic of Iran, which recently killed 52,000 innocent protestors, and has spent the last 47 years killing American Soldiers, and others. The only ones that should be arrested are the people that led Iran into this unprecedented SPIRAL OF DEATH AND DESTRUCTION, something that should have been dealt with years ago, by previous Presidents! President DONALD J. TRUMP
realDonaldTrump
پیش‌تر:
زهران ممدانی، شهردار نیویورک، اعلام کرد در حال بررسی امکان بازداشت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در صورت سفر به این شهر برای شرکت در مجمع عمومی سازمان ملل متحد در پاییز امسال است. ... @
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77319" target="_blank">📅 20:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77318">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bDQSIip_MPYH2JO4Jdb8hrS-FxZ7mg-JV28bbTEEenHREqL9PWCE3Bz5Q0nA4Z3FeUd3WHROqiHePBez5-31cXqIE5qk1UWW8F6oF5V7GBKBQ2KN1Lm2A_HU7PzKPgA0JBsKszgBra_Ux5aoAATVsVdAQe-6NfYCn48_JJsM-HmLB_evk9NOsPsbExYN_LfWpWPvzRN8I9pSigFRcwPg5iKI39noVuRMv71D9--9RIyJVmeFxszSMWGdLyc78Sd6f4K2lc6cQfTkGEDShsYgPXHGllbKGPVdLLheT_lUV8aqHyTuUxOBeANaQT0whRYEqgd2vAJliY_xrHOgjmB7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند پیام دریافتی تاییدنشده با مضمون: کارخانه نخ شهرستان خمین رو هدف قرار دادند.
هم‌زمان منابع حکومتی:
یک واحد صنعتی در حومه شهر خمین هدف حمله دشمن قرار گرفت
معاون سیاسی امنیتی استانداری مرکزی در گفتگو با خبرگزاری صداوسیما: این حمله حوالی ساعت ۱۹ روی داد که تلفات جانی در پی نداشت و خسارات احتمالی در دست بررسی است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77318" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77317">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWLNh-oSajbgxIhiN0LU6OrPl2kp9NhJLqNMFBVYw4X0GtfPFDWLq1zxXGtqmqmxlfx91MEZF0j0RJEYG5jGStVUJzLMr3NeMIcBwE2eh1EMI7h5OOeD5rRe-1FTxkqCqJtD6qtbrUtexR8dHquGA5bMLjSxO98VDVDkUkGgd7mpd8MoKHr1Drjk75osJtc4m7SgX2khAvGII14VKh2wWavBPcFLU9F06poMq5eFKkrNJh-FkeUnZnMGkbtFnCsWGEWc1cDzPp-GFO_bbD6iqSxO0DzYVMLEZcxgchq2lAEovIe2ejHnYmxFeT6Kl9EXwe1pt1mLHf6ehN-YUS1vLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژان نوئل بارو، وزیر خارجه فرانسه، در شبکه ایکس اعلام کرد که دو نفر از کارکنان سفارت این کشور یک‌شنبه از سوی نیروهای امنیتی جمهوری اسلامی مورد «تهدید و رفتار ارعاب‌آمیز شدید» قرار گرفتند.
بارو گفت این اقدام نقض آشکار مصونیت‌های دیپلماتیکی است که این افراد از آن برخوردارند.
وزیر خارجه فرانسه افزود: «آن‌ها بدون هیچ دلیلی برای چندین ساعت بازداشت بودند و مورد بازجویی قرار گرفتند و یکی از آن‌ها نیز مورد ضرب‌وشتم قرار گرفت.»
او گفت: «آنها سرانجام توانستند به سفارت برگردند و اکنون در آنجا در امنیت به سر می‌برند تا در ساعات آینده به فرانسه بازگردند.»
بارو تاکید کرد به عباس عراقچی، وزیر خارجه جمهوری اسلامی، اطلاع داده‌ که «این تعرض غیرقابل‌قبول به سلامت و امنیت کارکنان ما، بدون پیامد نخواهد ماند».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77317" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KnOhGN2SY27tl2XtXMBkmfnlqrdYEQ0nngAXzU_NLFyvVrAz1vIKxJ-mqIwHtVhiHWhK_h-GuKj183LrfptwaqEX3IrD-kR9aWbTv9hjpRsVFEVIHVjPpUgP6XVtBsh60CYaFUZ2sKoCYZpcKBP-z8cvzwbfSzi6Cw5zPT4U6UYfXWAYdBagX3JSe_RiNX4Vv6hIdxf89HVoSnL5EjrZH4R2DDstuu040hg1pvipIn-tC75x9_EaR_5_gILpFLTXslFMT3dUBOyFXOziytQkOpnsmP5RSeGotxR_97lxIiO8I4Hhm4HfDapIAjtPh0uYMM3zug0s-hVTEFERGkUioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز، ترجمه ماشین:
خبر فوری: پنتاگون تصویری از سرباز ایزابلا گونزالس، نظامی ۱۹ ساله آمریکایی اهل کارولتونِ تگزاس، منتشر کرده است که در حملات موشک‌های بالستیک و پهپادی ایران در آخر هفته کشته شد.
گونزالس در حال پشتیبانی از مأموریت آمریکا علیه گروه «دولت اسلامی» بود که هنگام کمک به دفاع در برابر حملات ورودی ایران کشته شد.
مرگ او در حالی رخ می‌دهد که درگیری‌ها در سراسر خاورمیانه همچنان شدت می‌گیرد.
نیروهای آمریکایی نهمین شب متوالی حملات تلافی‌جویانه علیه اهداف ایرانی را آغاز کردند؛ در حالی که دو کشور همچنان برای کنترل تنگه هرمز با یکدیگر می‌جنگند.
FoxNews
آپدیت:
خبر فوری: رئیس‌جمهور ترامپ در مراسم انتقال رسمی و با احترام پیکر دو سربازی که در حملات ایران در اردن کشته شدند، شرکت خواهد کرد. این مراسم فردا شب در پایگاه نیروی هوایی دوور برگزار می‌شود.
کارولین لیویت، سخنگوی کاخ سفید، در پستی در شبکه ایکس نوشت: «رئیس‌جمهور و تمامی اعضای کاخ سفید برای خانواده‌های آنان دعا می‌کنند.»
رئیس‌جمهور نیز در پستی در تروث سوشال نوشت: «هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین برابر خواهد پرداخت»؛ در حالی که آمریکا به کارزار نظامی خود در خاورمیانه ادامه می‌دهد.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77316" target="_blank">📅 19:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6cac939191.mp4?token=s7v7I8GeIWjMU8tq3rNeuJGa7LbqFANJAPi7CigAmm-JOfY4eqJ-avx0vZ0IiVUyB0wy4ShPVJ2wGbDhCYiM23G0V_AvDFMMQTTJdh7u9KOcxTkn_5ooHGWpo3nkXFMZ51vfPyk-eQkkFf1xwrcURrus4L4zvYwHBbcisfUzHFpj-ci7hbYDZECfXJf4giA8jS0G95SVsmvObPWLoAkgHPL_DOYDLqfFYIbe9rlgiHNZQMQ2MLQ3aC-Sj8mUV0G-U9RMu8QwFjDMjnr95qCx1HzauORoy4pRgyOE4PKwn1BtnoJe_kLMDtTGEqIEkP-E1BTvJBiNE_uWTUl-C-mWhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6cac939191.mp4?token=s7v7I8GeIWjMU8tq3rNeuJGa7LbqFANJAPi7CigAmm-JOfY4eqJ-avx0vZ0IiVUyB0wy4ShPVJ2wGbDhCYiM23G0V_AvDFMMQTTJdh7u9KOcxTkn_5ooHGWpo3nkXFMZ51vfPyk-eQkkFf1xwrcURrus4L4zvYwHBbcisfUzHFpj-ci7hbYDZECfXJf4giA8jS0G95SVsmvObPWLoAkgHPL_DOYDLqfFYIbe9rlgiHNZQMQ2MLQ3aC-Sj8mUV0G-U9RMu8QwFjDMjnr95qCx1HzauORoy4pRgyOE4PKwn1BtnoJe_kLMDtTGEqIEkP-E1BTvJBiNE_uWTUl-C-mWhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پیام‌ها و تصاویر دریافتی: پرتاب موشک از حوالی لار در استان فارس، دوشنبه ۲۹ تیر حدود ساعت ۱۹'
هم‌زمان: پیام‌های دریافتی از صدور هشدار در بحرین
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77315" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رسانه‌های داخل ایران از پلمب چند کافه و رستوران در مرکز شهر تهران خبر داده‌اند.
براساس این گزارش‌ها جو کافه، ۱۴۰۱، سام‌کافه، دو بار، نووک و تئوری در خیابان‌های سنایی و ایرانشهر پلمب‌ شده‌اند.
وبسایت امتداد نوشت که به هریک از این کافه‌ها دلیل متفاوتی ارائه شده است از جمله «حجاب، داشتن ساندویچ در منو و صندلی در پیاده‌رو».
پلمب کافه‌ها و رستوران‌ها به دلایلی مثل حجاب یا موسیقی زنده سابقه طولانی دارد.
@
VahidHeadline
پیام دریافتی به همراه تصویر یک حکم:
چهارشنبه (چندروز پیش) به ۹ تا کافه داخل اکباتان فاز یک حکم پلمب دادند بدون هیچ توجیهی (فقط گفتن حجاب رعایت نشد) و همه کافه ها رو پلمب کردن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77313" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77312">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWF8mZeH-CNSEYAjwMU617ZFVGi2zXvgRxQbEMAaY4nhoA2LZutRB3paYg_nk2Tmtjjd3-1v2YrzNM_Pkm9-o80rLMie-MXoC1kx5NXNZ-I92N59sA7xswAsvB_wMRJ_Gos5YTsc-y9baedOWwf51q6zPczMKxcltPO3T9Q6-5AQI0l5s1nF34ua9mBC3WitFuQj9Xh8Nio0VCNd1Vmzr5kX4bXECaEUPSONVaUrF0y-_Fq6vPTdQoEqryBVPPpVzqL2Mw85lZFMFvhSDs76mc9z8aAglEdIy7VfPZmwbSE6SEP7YSrSfiHruOmwlWLyX4vOJn6V9W-DkpRC6JYcYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسکندر مومنی»، وزیر کشور جمهوری اسلامی، در راس هیاتی از نمایندگان دستگاه‌های اجرایی، به دعوت همتای پاکستانی خود عازم اسلام‌آباد شد.
رسانه‌های ایران روز دوشنبه ۲۹تیر۱۴۰۵ گزارش دادند که هدف از این سفر، بررسی راه‌های توسعه همکاری‌های دوجانبه میان ایران و پاکستان است. جزییات بیشتری درباره برنامه دیدارها و محورهای مذاکرات وزیر کشور جمهوری اسلامی منتشر نشده است.
سفر مومنی به اسلام‌آباد در حالی انجام می‌شود که وزارت خارجه جمهوری اسلامی ساعاتی پیش دریافت پیشنهادهایی از سوی کشورهای میانجی برای توقف درگیری‌ها را تایید کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77312" target="_blank">📅 18:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYxNyjbi4pZZG3QE4Cs4KrUVlXjsWnRiOgbPmmc6nG0ANNmQJ8OXUnO23cr4xXuqn70MbClYHtJ6NgOGD2CpGuaB24YSlwpzzeZ2vhixUeqMGPCMjjMU3qgweV7wAnc4W8Vu1Ym7HzymZ_91Pj_r7M7oLphJVoQ_ZX-oOkSnJdSKYOeE8XEoYJCtSYvqDkhuOI8HkOHzU8z1fHA5Hr2GbcVWufENCQkaPnbrE74cyKnMQ9TAlTqaAOpZ2zId4p6BhJP6JlcOrcvKsgznR-bOeBslkeXsU-XUd_wozwjd8i-t58BknNpdPSHr-oHnTUOpbERsz1mb_uptmnxpbGCEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدباقر قالیباف»، رییس مجلس شورای اسلامی، با انتقاد از سیاست‌های آمریکا در منطقه، با انتشار پستی در حساب «ایکس» خود نوشته است که واشینگتن هم‌زمان با ادعای تلاش برای توقف جنگ، به انتقال تجهیزات نظامی جدید به منطقه ادامه می‌دهد.
قالیباف در پیامی که دوشنبه ۲۹تیر۱۴۰۵ منتشر کرده، نوشته است: «آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند.»
رییس مجلس شورای اسلامی همچنین با اشاره به آنچه «آمریکایی‌بازی‌ها» خواند، نوشته است: «آمریکایی‌ها روی هوش ما اندازه آی‌کیوی مختصر خودشان حساب کرده‌اند. جمهوری اسلامی در شناخت این رفتارها «به مرحله استاد تمامی رسیده و بر همین اساس برای مواجهه با آن آماده شده است.»
قالیباف در پایان نوشته که اقدامات باید موید ادعاها باشد، نه ناقض آن‌ها.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77311" target="_blank">📅 18:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/octMswWME5wfquZ5R1IHf2ZW8FvviuR4jpl_1T8Ajv04l_0i8QNKpiW8jWlGyoNwPpn0i_0saoK7mfGQCdQ_Sv64xOiEaSPWz2q1zo_KwEfIe4NN-I3YBJ7SuNjw3tPJWcH-SOH-2iMFCccI3iEFjVHREZ92QaVrE3CxyGBIj_m_k9sjV8VUmXRrusXa4Aer3OTJgZ1CsaPB_rJKi4jVT15M8FYlXsRTBYpT_34WEPF3PvOJATNO9HZ9kKVbtbxcqrWXxUilPxNjhfpIh7NXN_Y2BalKCgzgBDTRWf5wg98fHhDQZvFt2ACuAC_zhIvk6aEvLftSjeLbohGIxgKY7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت کشتیرانی یونانی «دایناکام تنکرز» همزمان با بالا گرفتن درگیری‌ها میان ایران و آمریکا در منطقه اعلام کرد که دو نفتکش تحت مدیریت این شرکت روز دوشنبه هنگام عبور در آب‌های ساحلی عمان، هدف پرتابه‌هایی با منشأ نامشخص قرار گرفتند.
شرکت دایناکام اعلام کرد نفتکش «کاوومیلیز» با پرچم مالت هدف دو پرتابه قرار گرفت که باعث آتش‌سوزی در اتاق موتور آن شد و خدمه را ناچار به ترک کشتی کرد.
این شرکت در بیانیه‌ای گفت: «پس از فعال شدن سامانه اطفای حریق کشتی، ناخدا تصمیم گرفت کشتی را تخلیه کند.»
دایناکام افزود که تمامی خدمه توسط مقام‌های عمانی به سلامت پیدا شده و به ساحل منتقل شدند و این شرکت در تماس نزدیک با همه مقام‌های ذی‌ربط منطقه‌ای قرار دارد.
شرکت بریتانیایی مدیریت ریسک دریایی ونگارد اعلام کرد این حادثه زمانی رخ داد که کشتی در فاصله حدود هشت مایل دریایی در شمال‌غربی کُمزار عمان در حال عبور بود.
سازمان عملیات تجارت دریایی بریتانیا که پیش‌تر گزارش داده بود این کشتی دچار آتش‌سوزی شده است، اعلام کرد هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77310" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PsLf2HyKJl8FMxIjQmuVklKcZ9BT9kwS5U--Crjbunm5At2AGT1yz_pPFbkFmckiHc90MSPDt4pe9KnG-YQHow8WIzhgaYlNLBMruo-BusPGYPSy5Rop40ladYhEyXB3SrFAKcmeUL0qV3HdL-NS2DX3NdKh_AhXwfPvYtgmFWUVNubsj2gedR6SefpOlZOH10mdHhQJivgamcDQC67wnnjGhYup7QyWbLALiJ_IPC2tmJXVk6bTtSB4qZkj3zhFuwUevoGaaASeEkpfpP4DEmO6exYzKGWdSwrNF8IBxirIaUGD47hWcPFBbkgUs7fJm3Rqic3Qzjlc4WxMytkedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/biAb3hiqRFPwpnFE__UnSmcTSyhIr-YJyQGRAgvtoC4yj7JzOf56c-XX0ZaVaS91BowjVMaqfXD_EuJBbQjUjz6HrO_1C7WWCgiVCL38YAI2gLxWCKEvVCqfUrz4hjwX9obpi_5d8L40C-6AicOS7mcwBFjEDo0VNwaBZw0MVSNl5tuAl7ow2Ut_D2Q8_pLw4BmlVLu8AWDejLBlx_NdmAzhqF9Anmmtw8wltyH1Axuvz1dzMVrlPtUOP54Z3o54kGJLr6N5krfwD0Y1O6f5tSBkg6jPzrbWCjl7EFjl6ZMLob_b0m3SFRXJgz03lZBwsalN_emmMA3KvjuAYI4IQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری رویترز به نقل از یک مقام ارشد جمهوری اسلامی گزارش داد که میانجی‌ها پیشنهادی را به جمهوری اسلامی ارائه کرده‌اند که هدف آن کاهش تنش در جنگ با آمریکا است.
بر اساس این گزارش، این پیشنهاد شامل یک آتش‌بس ۱۰ روزه برای یافتن راه‌هایی جهت احیای تفاهم‌نامه میان جمهوری اسلامی و آمریکاست که ماه گذشته حاصل شده بود.
پیشتر سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد که پیشنهادهایی از طریق میانجی‌ها دریافت کرده است. این اظهارات در بحبوحه تنش‌های نظامی میان آمریکا و جمهوری اسلامی مطرح شده است.
اسماعیل بقائی روز دوشنبه در یک نشست خبری بدون ارائه جزئیات افزود: «اصل موضوع که در این روزها ایده‌هایی از سوی برخی میانجی‌ها به جمهوری اسلامی واصل شده، تأیید می‌شود.»
تنش‌های اخیر پس از حملات جمهوری اسلامی به کشتی‌های تجاری در تنگه هرمز آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77308" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چند پست بعدی مربوط به ساعت‌های گذشته هستند.</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77307" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77305">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iErF69yyjRn3OxD5KkmUR7zHsxiz9YYJjAYYJPU1d_zlsMq1eF_5PqOE27onTfd_JdamRldcwM--jH5zT5333W-Htwo0fum5ptx0iDXYEZ_sfCG0DwCtQ4TqYueHyWRPXKXiWVBOel7H48ZpjLn1w61fOscvgd4bmRSkxDfEbQZliu_xjKBxpHdgwqW8WxZqBv9DGS9YWex2mAv43hf_9Qtu3RAUEuKGTci93Ixpzp7qzR1jsTnDFr77LWCnq0c5BKqWKy8eoX2NXD1M6xYNbovv2Pb-xEg2LZnjsN8uyRpWgqVVvsguixZYPHqXQgGkD8-TsY2n0NgzbYquRdLjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q9VpGq99CVXwwFihyHjG2UZnyUzJWy1Uk6CcqzMVeEcfbRusBo6OVHWOuYprtpU6PrrHr8oMiA3n1-Tetd_JNV-4hm4jr_l9GNwgIpAfK6meeQaDKXFEfkxCWBmDfRJMsj3hiVKG4N6tgiPZ01f8DnI7XIe1WsGVxIzxXXczJIwI6jmZLM9XDucfOoW-MFyU-gLvyGwppgIZKOZb94Mi8GE1vNgzCQwkXbHbdON5XdbhVYq0pGA27ocK3Oy7DYdrgZA3vMuJM8wnoFG5SUjo-77lpbRCZOk8pTXZOnFO4WI3x4PXyhYeBRm7IHDEOmIZ6a85d-ZyklN_wWrvJv4bgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
اسمون شیراز الان
ساعت ۱۸:۲۵ از شیراز موشک شلیک شد
سلام وجید جان شلیک موشک از شیراز 18:17
درود وحید جان
۵دقیقه پیش از شیراز موشک زدن
[بعدش کلی تصویر مشابه دیگه اومد که دیگه پست نمی‌کنم]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77305" target="_blank">📅 18:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77301">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s9lj75VwDOSiGlblWif8NwHTz7pprdZNbP06xs4ogFfRM5kwyQlFL_zpMzs3lC_4_-aWzRXpSJaUqQYKESc_tb1Ssd5HYT_BulLpbXWMczSFIzccZY4dHwsGMviBy6LvqRVOU5cX46RSvDdAUbNA9f3J-vJRpzbkft_Yyiur4WINSSblkmCEzwwkkxVEeyMzio1XDCKL-uJK5KjdgbexUVb1iAj3cLENVv05VcA0KLOGc8UhwOejzQkrBqojoXvZgkq4RlraOK9x8p-dE_NR14jjta90OtZ4zyOpEe25N3owfG8mpk1fPMDC1SPYurtYgWpj-U4tomFCD2sZ_H2zIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bHuoUUuMncJqsHXAIN-m5PhW-Ko8Md2I3rH-9kVu1QL2k3O3Hr0XueTwTuHE8kjojkhC8lPNecUpEJj0hxSvn16V4BHnAGSrNUACRD1hBYFZW6DYmXNmsq0B-3DLVuT__5TvjkXfTsVrPEY1lkHvzOn1VB_GQXXXsnJiZAdFzSBsRMqGhISsg425Bn2Zx7T_8c8bNoY_lTUf5M-yuYS3Yxw4JdCpGgPnJ2B-7yK0kzTX4YMkDnjZizC_p5igMPRkfJHnSgc6KKPJncimzJTas2-xZZlzh4istG-Z3ixLCuYkckAnet7iMbjpj68bNgC38XxyfwURgk3knn7vHoNqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pbcYx55IAUPH0kPuzO5QoXZWxumtYQnmmunUiwIPOnuvcKQIvtb-68yG0EnQIwgZMHZ-wZ-LcQdaGNajcfNQAeDwrEqhhREAo2P6EtpQqlyBGwP6R2AnqAtQp-_WSPU_TuuTdpw3vaBcX55AaCEc9nxhkhuzulaA3EW5Oya4UNVL11d4Z_kqR-Q-AFV6w5LqhI1i7vsbMBso5h4R0C9q_QjBmzAm06Dnc9leYzDIQQH5h-pkDs7-QL61ttCTkUUz6oISkoPKL5KR3o80t4hqb-3tR7hLSGy_S_KP1eG99UKVJhbe1rKAWChR6tDKlQyUlw1oco5j19IxuFU1qR6D8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KB78PdNZGQPnFtAjgRTShTHGmf7BkAAVXC8nUcK5uX2wNnU4zTBrzDbSuIk4PaR0kefKO9qUglfeuOZ1MQsrUiE3AAPsgBLKUPETvYOG5LmXDVzCAKTZecOm8DsA1tf02a18qazQH2ryydIwC0-3LJFbvtP3XZtoiaXRI6jLMTTth8Ue8uXI1Say5GdCAD9TwnAQs4qQLHYuk1CcrO8RZCecfcRSK_ReVoE1Hc3u1kmzkwyDxf_m6mh_eZKjqTDzct4CXS9H97-OCXZfMNN72dNr3JbyZWcl6pW5mWGp0q8hSlVKMc7NlF89IxHpG5InalrEr9Yp8oYyCsG-bvQPxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی از شیراز پس از دریافت پیام‌ها درباره 'شنیده شدن صدای انفجار سمت صنایع الکترونیک'
دوشنبه ۲۹ تیر حدود ساعت ۱۷:۱۰
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77301" target="_blank">📅 18:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77300">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شیراز، پیام‌های دریافتی از ساعت ۱۷:۰۶
سلام ساعت ۱۷:۰۶ شیراز ،صنایع الکترونیک زدن صدا انفجار لرزوند
صاایران شیراز رو زد پنج دقیقه پیش
صدای انفجار و دود
صنایع شیراز
ساعت پنج
سلام وحید جان من شیراز هستم همین الان سمت تاچارا و معالی اباد صدای انفجار شدید اومد فکنم صنايع الکترونیک بود
سلام وحید جان. شیراز ما خونه‌مون نزدیک محدوده صنایع هست. ساعت ۵ صدای انفجار اومد. نمی‌دونم زدن یا موشک پرتاب کردن، ولی صدای انفجار بود.
سلام وحید جان ساعت ۱۷:۰۷ شیراز سمت صنایع صدا اومد
مطمئن نیستم افنجار بود یا دقیقا از کجا بود
ولی صدای بلندی بود
شیراز صنایع رو زدن  ۱۷.۱۶ دقیقه
وحید ساعت حدودا ۵:۱۵ عصر صنایع الکتریک شیراز صدای انفجار اومد دود بلند شد
شیراز صنایع رو زدن انفجار
صنایع الکترونیک شیراز و زدن
سلام شیراز صدای انفجار حدودای ۵وربع سمت صنایع
آپدیت:‌ منابع حکومتی
شنیده‌شدن صدای انفجار در شیراز
دقایقی پیش اهالی بخش‌هایی از شهر شیراز صدای انفجار از محدوده شمال غرب این شهر شنیدند.
خبرهای اولیه از حمله به یک نقطه در شهر در جریان این حملۀ هوایی دشمن حکایت دارد.
به گفته استانداری فارس، این حادثه هیچ گونه خسارت جانی درپی نداشته و تیم‌های ارزیاب در محل حادثه حضور یافته‌اند.
📍
میگن اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77300" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BCHjSXVKtewAvbW7-iHykLgM29VdCA3D-OHtSF9CuO_Ly0QAdLurtz-P0uJqyb3Sv3QyN1m4a1QaM1PjvrF7bJg2XC4gu38WUy3yFVz2Rgzsb71HF6C8PbzuViEaJoAVBgpkPHj0MpizTARcoql_qiY8upwpQSSTX5ZpAtZ3ZL1Nw3IJkonjIGedUAgdmvJ8fdwYeZGn-Gj_vuYyolzxpfJpiM0klb-wlmRVaeRVLNFf39RHtiJsPHaKNm1dg9kIj7-0Kdkw3lq9dxRDeb8ODxJb-Ut3pIxgUPwjxQ_B-BTVX4eOq3SVgQu1sFs4jjsW2uj0aVpvSmznyefw9mGxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ها در کرمانشاه!
آپدیت: دو زلزله به بزرگی ۵٫۲ و ۵٫۷
📍
در عمق ۸ تا ۱۳ کیلومتری
کوزران
پیام‌های دریافتی:
الان کرمانشاه هستیم
کل خونه لرزید
زلزله بود
سلام وحید همین الان زلزله اومد تو ایلام
کامیاران سنندج زلزله هنوزم پس لرزه میاد
خیلی بد زلزله اومد
کرمانشاه
کل خونه لرزید
اینجا جوانرودزلزلە اومد شدید بود
سلام ایلام حدود ۱۰ ثانیه خیلی بد لرزید
سلام وحید، زلزله سنندجم حس شد
سلام وحید همین الان ایوان غرب زلزله آمد خیلی شدید بود
کرمانشاه زلزله اومد
درود کرمانشاه چند ثانیه به شدت لرزید کاملا حس شد
سلام وقتتون بخیر همین الان زلزله اومد استان همدان ملایر ۷:۱۵
زلزله نسبتاً شدیدی سمت کرمانشاه اومد
همدان هم ۳ الی ۴ ثانیه لرزید
سلام همین الان زمین لرزه اومد جوانرود استان کرمانشاه
سلام اقا وحید، ما پاوه هستیم تو کرمانشاه خیلی بد لرزیدیم معلوم نبود زلزله‌ بود یا چی. از شدت لرزش زیاد از خواب پریدیم. ساعت تقریبا ۷:۱۴ صبح
کرمانشاه اسلام اباد غرب زلزله شدید
سلام کرمانشاه خیلی شدید لرزید حدود ۶. ۷ ثانیه
سلام من کرمانشاهم حدود ۱۰ ثانیه شایدم کمی بیشتر کل خونه لرزید
آقا وحید ما مرز مهران هستیم، استان ایلام اینجا هم لرزید ساعت 7:15دقیقه
🔄
دوباره لرزیدددد
یا خداا بازم
دوباره اومد
دوباره ایوان داره می‌لرزه
وحید خیلی شدیده
وحید بازم داره زلزله میاد، ایلام
همین الان سروآباد استان کردستان لرزید
همین الان ۷:۱۹ هم پس لرزه‌ش اومد
پشت سر هم زلزله بالای 10 دیقه کامیاران داره پس لرزه
سلام وحید جان
مریوان دوبار اومد ۷:۱۴ و ۷:۱۹
وای دوباره اومد اینقد شدید بود
سلام وحید دوباره کرمانشاه لرزید خیلی شدید تر و طولانی تر
سلام ایلام دوباره لرزید
۳ ۴ دقیقه پیش پاوه لرزید
یه دقیقه پیشم لرزید و قوی‌تر بود
درود دو مرتبه پشت سر هم داره زلزله میاد هنوزم ادامه داره
خرم اباد ساعت 7/20
همدان دوباره بدتر لرزید
کرمانشاه زلزله بود
همین الان کرمانشاه زلزله خیلی قویی امد
کرمانشاه بازم زلزله شدید و طولانی
سلام آقا وحید کرمانشاه زلزله قبلی حس نکردیم الان ۷:۲۰ خیلی شدید و طولانی لرزید
ساعت ۷:۲۰ همدان لرزید
زلزله بود
اراک همین الان ۷:۲۰
چنننند ثانیه لرزید
سلام 7:20 اراک خونه لرزید در حد تکون شدید
همدان الان کاملا لرزید برای زلزله
قوی بود
وای ایلام بد لرزید
عجبيه اين زلزله خرم آباد حس شد
جالب اينه چقد ادامه داشت
سلام وحید خرم اباد لرزید خیلی کم لرزید
سلام،همین الان پشت سرهم دو بار زلزله اومد همه مون از خواب بیدار شدیم،جوانرود
نهاوندم لرزید خیلی عجیب بود
دوباره کرمانشاه زلزله،
از دفعه اول طولانی‌تر بود
۷:۱۸
زلزله شدید دوباره کرمانشاه
سلام وحیدجان همین الان اراک لرزید چهار پنج ثانیه شدید بود مثل گعواره خونه میلرزید چه خبره همه جای ایران میلرزه...
سلام وحید ..زلزله خفیف ساعت ۷:۲۰ همدان
همدان شدید لرزید چند سال بود چنین زلزله ایی نیومده بود
وحید جان سلام
اینجا الشتر، لرستان، ساعت 7:19صبح لرزید و قشنگ حس کردم لرزش زمین رو
سلام وحید جان ۷و۱۷دقیقه ب مدت۶ثانیه زلزله خیلی شدید از کرمانشاه همه رو از خواب بیدار کرد
کرمانشاه با زلزله بیدارشدیم
سلام وحید جان زلزله خیلی شدید همین الان کرمانشاه
سلام داداش کرمانشاه برای چند ثانیه وحشتناک لرزید
سلام بروجرد هفت و بیست دقیقه لرزید
سلام ساعت ۷:۲۱ همدان شهر همدان یه زلزله خفیف اومد
سلام بروجرد هم زلزله اومد
زلزله یا چیزی شبیه به آن در خرم آباد احساس شد
کرمانشاه زلزله وحشتناک اومد خیلی شدید بود
کرمانشاه زلزله آمد
منم قروه کردستانم
خونه یه ذره لرزید
آپدیت:
گزارش مقدماتی زمین‌لرزه
زلزله به بزرگی ۵.۲ در استان کرمانشاه
مرکز لرزه‌نگاری کشوری مؤسسۀ ژئوفیزیک دانشگاه تهران:
محل وقوع: استان كرمانشاه - حوالی كوزران
تاریخ و زمان وقوع به وقت محلی:
۰۷:۱۳:۱۷ ۱۴۰۵/۰۴/۲۹
طول جغرافیایی: ۴۶.۴۳
عرض جغرافیایی: ۳۴.۵۶
عمق زمین‌لرزه: ۸ کیلومتر
نزدیک‌ترین شهرها:
۱۷ کیلومتری كوزران (كرمانشاه)
۲۳ کیلومتری گهواره (كرمانشاه)
۲۶ کیلومتری روانسر (كرمانشاه)
نزدیکترین مراکز استان:
۶۵ کیلومتری كرمانشاه
۹۸ کیلومتری سنندج
كوزران کرمانشاه دوباره لرزید/ اینبار زلزله به بزرگی ۵.۷
مرکز لرزه‌نگاری کشوری مؤسسۀ ژئوفیزیک دانشگاه تهران:
محل وقوع: استان كرمانشاه - حوالی كوزران
تاریخ و زمان وقوع به وقت محلی: 1405/04/29 07:18:49
طول جغرافیایی: 46.48
عرض جغرافیایی: 34.57
عمق زمین‌لرزه: 13 کیلومتر
نزدیک‌ترین شهرها:
13 کیلومتری كوزران (كرمانشاه)
22 کیلومتری روانسر (كرمانشاه)
25 کیلومتری گهواره (كرمانشاه)
نزدیکترین مراکز استان:
61 کیلومتری كرمانشاه
94 کیلومتری سنندج
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 471K · <a href="https://t.me/VahidOnline/77299" target="_blank">📅 07:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8AJQAnMDTD6jwAReMJLfWUIv2w8BCmfvrWpRzV4CFNXhQCkHr82CJHph6pZ3IyH04jgR8ZwpLjxLYYIw43VEth1agXE6g8TaDHAJm5yxeidQAhIFizvOxKdPNFXx5Eruv39kGD0lM6S182vekGblj3x1NJDhPQB3QLvmZkFf94qTYeX9Xl3G95-p-_SP0vOlz5B7HK_xCC9_aAXNU7D8HIu13CXTSX78ESkiCF72rrZm0nSy0pmYNaYNh0TPwOQ6XuDjzZT0xgaKWfQn9DkPf1Pk8nFV5Hls8F_Jtltz6YVcat8VM_C2JQRRFKLejgRVDSSdnWS5aPbqBVM7WZd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
مارکو روبیو، وزیر خارجه آمریکا، روز یکشنبه گفت ایالات متحده آماده دیپلماسی با ایران است؛ هم‌زمان ارتش آمریکا نهمین شب پیاپی حملات خود را آغاز کرد.
روبیو پیش از عزیمت به مانیل، جایی که قرار است در اجلاس اتحادیه کشورهای جنوب شرق آسیا شرکت کند، به خبرنگاران گفت: «ایالات متحده همیشه برای رسیدن به یک راه‌حل دیپلماتیک آماده است. ما چندین بار با ایران تلاش کرده‌ایم و به تلاش خود ادامه خواهیم داد. اگر آن در باز شود، از دیدن آن خوشحال خواهیم شد.»
روبیو از ایران به‌دلیل حمله به کشتی‌ها و ایجاد مانع در تنگه هرمز انتقاد کرد. تفاهم‌نامه‌ای که آمریکا و ایران در ماه ژوئن به آن دست یافتند، با هدف گسترش آتش‌بس و ازسرگیری تردد در این آبراه کلیدی تنظیم شده بود.
روبیو گفت: «اگر آن‌ها مفاد این تفاهم‌نامه را نقض کنند، نمی‌توانند انتظار داشته باشند که این تفاهم‌نامه همچنان پابرجا بماند.» او افزود: «آن‌ها همچنان پیام می‌فرستند که می‌خواهند گفت‌وگو کنند و مذاکره کنند، اما آنچه ما به آن پاسخ می‌دهیم رفتارشان است، و رفتارشان این است که موشک‌ها و پهپادهایی را علیه کشتی‌ها، از جمله همین امشب، پرتاب می‌کنند.»
کیت ماهر، خبرنگار سی‌ان‌ان، از روبیو پرسید اگر تلاش‌های دیپلماتیک شکست بخورد چه خواهد شد. روبیو پاسخ داد: «فکر نمی‌کنم برای ایران خوب باشد. منظورم این است که اقتصاد ایران از هم پاشیده است.»
CNN
مارکو روبیو، وزیر خارجه آمریکا، گفت حادثه‌ای که روز شنبه در شمال عراق به کشته‌شدن یک نظامی آمریکایی انجامید، یک «سانحه» بود و این نظامی هنگام خنثی‌سازی یک پهپاد سرنگون‌شده ایرانی آسیب دید.
روبیو روز یکشنبه به خبرنگاران گفت: «هیچ کاری که ارتش انجام می‌دهد بی‌خطر نیست. همه این کارها ذاتاً خطرناک‌اند و ما فقط سپاسگزاریم که چنین آمریکایی‌های قهرمانی با پوشیدن یونیفرم، در خدمت کشورمان هستند.»
روبیو درباره حمله ایران در روز جمعه در اردن که به کشته‌شدن دو نظامی آمریکایی انجامید، گفت: «یک موشک عبور کرد. تقریباً همه موشک‌ها را سرنگون کردیم. یکی از آن‌ها رد شد... این دلخراش است.»
روبیو گفت که «برای خانواده‌هایشان و آمرزش روحشان دعا می‌کند.»
تعداد نظامیان آمریکایی که در جنگ نزدیک به پنج‌ماهه با ایران کشته شده‌اند، اکنون به ۱۷ نفر رسیده است.
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/77298" target="_blank">📅 07:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان چابهار 5 بار زد 5:50
باز داره چابهار رو میزنه  لرزش ها وحشتناکه
الان دوبار صدا اومد ساعت ۵:۴۸
5:49 دیقه کنارک صدای انفجار اومد
هنوزم صدای هواپیما میاد
به عنوان آخرین مقصد اینجا رو میزنه
کنارک صدای جنگنده و انفجار هم اکنون
۲انفجا کنارک نیروی هوایی ۵.۴۹
صدای هواپیما بازم شنیده میشهه چابهار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77297" target="_blank">📅 05:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ddbd450c.mp4?token=ZikASNsyK7XYhYu-10-f6sr9QMvYeq0y9SdDtx5ysLF3-LCuUVCo4gYh-Dmy-Hey9RRLSaOAI8p-7hkFZ6tyYIIt5DT6ZCg8HPR4QfVR5m8haUL0CJmlJxDrsT3WsG1PB_-Q-VWuVm5TUX6LRQTeIYo3uMoURysUdO6aPMTxLmGUV9lSDzUl3YY6xu6wrplJ7VUVnMDiGpqJFSYahXnz0FfKq6LM_kax5I80JIn6VS-vCTIXc6entLEdzRtIOl7Nl00lNrA80RzcpIsqt7ITYyuEEP5eXqLBfEWTEwgHGe2NtoTHE_BKq27cEJJXOjIP3ufp4iDGOd8B21h2zWIUjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ddbd450c.mp4?token=ZikASNsyK7XYhYu-10-f6sr9QMvYeq0y9SdDtx5ysLF3-LCuUVCo4gYh-Dmy-Hey9RRLSaOAI8p-7hkFZ6tyYIIt5DT6ZCg8HPR4QfVR5m8haUL0CJmlJxDrsT3WsG1PB_-Q-VWuVm5TUX6LRQTeIYo3uMoURysUdO6aPMTxLmGUV9lSDzUl3YY6xu6wrplJ7VUVnMDiGpqJFSYahXnz0FfKq6LM_kax5I80JIn6VS-vCTIXc6entLEdzRtIOl7Nl00lNrA80RzcpIsqt7ITYyuEEP5eXqLBfEWTEwgHGe2NtoTHE_BKq27cEJJXOjIP3ufp4iDGOd8B21h2zWIUjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام موج حملات آخر هفته علیه ایران را به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) نهمین شب پیاپی حملات علیه ایران را روز ۱۹ ژوئیه، ساعت ۱۰ شب به وقت شرق آمریکا، با موفقیت به پایان رساند.
تجهیزات و نیروهای سنتکام مراکز فرماندهی نظامی ایران، مواضع پدافند هوایی و نظارت ساحلی، توانمندی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و شبکه‌های ارتباطی را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی عبوری از تنگه هرمز بیش از پیش کاهش یابد.
ارتش آمریکا به دستور فرمانده کل قوا، ایران را پاسخ‌گو می‌کند. نیروهای سنتکام همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی می‌مانند.
CENTCOM
منابع حکومتی:
اطلاعیه شماره ۳۰/ دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند
روابط عمومی سپاه:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی؛ اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک کوش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگه هرمز را داشتند منفجر شده و از حرکت باز ماندند.
🔹
اینجا سرزمین ماست و دخالت ارتش تروریستی آمریکا از هزاران کیلومتر آن طرف‌تر هیچ وجاهت قانونی ندارد و با قطعیت با آن برخورد خواهد شد و تا زمانی که شرارت های آمریکا در منطقه ادامه یابد این معبر برای عبور کود شیمیایی و حتی یک قطر نفت و گاز امنیت ندارد.
🔹
ارتش متجاوز، آماده عملیات تنبیه ما به خاطر این تخلف غیرقانونی باشد.
قدردانی سپاه از اطلاعات مردم اردن؛ هواپیماهای بزرگ ترابری C17 و هواپیماهای فرمانده کنترل P8 ارتش متجاوز امریکا در فرودگاه عقبه هدف موشک بالستیک قرار گرفتند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
إِنْ نَکَثُوا أَیْمانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَ طَعَنُوا فی دینِکُمْ فَقاتِلُوا أَئِمَّةَ الْکُفْرِ إِنَّهُمْ لا أَیْمانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ
🔺
مردم شریف و ارتشیان مجاهد اردن، با تشکر از همکاری صمیمانه و اطلاعات دقیق شما که موجب هدفگیری دقیق رزمندگان اسلام و انهدام ۲۰ سوله محل استقرار نیروهای ارتش کودک کش آمریکا در منطقه الازرق و کشته شدن ده‌ها نیروی تروریست آمریکایی شد.
🔺
رزمندگان نیروی هوافضای سپاه در موج ۲۱ عملیات نصر ۲ با رمز مبارک یا رقیه (س) و تقدیم به دختر بچه های شهید جنگ تحمیلی سوم، با کمک شما، هواپیماهای بزرگ ترابری C17 و هواپیماهای فرمانده کنترل P8 ارتش متجاوز امریکا در فرودگاه عقبه را هدف حمله موشک های بالستیک قرار داده و به تعدادی از آنهاخسارت سنگین وارد کردند.
🔺
نظامیان متجاوز آمریکا که طی چند دهه اخیر به بیش از ده کشور اسلامی حمله کرده و میلیون ها مسلمان را کشته اند و حامی اصلی رژیم کودکش صهیونیستی در کشتار عظیم مردم غزه و ویران کردن کرانه باختری هستند، از لحاظ شرعی مهدور الدم هستند و هر مسلمانی، هرجا دستش رسید باید این قاتلان وحشی را بکشد.
🔺
با تشکر مجدد از تلاش‌ها و همکاری‌های شما که با انجام تکلیف شرعی راه را برای آزادی قدس شریف هموار می‌کنید.
«إِنْ تَنْصُرُوا اللَّهَ یَنْصُرْکُمْ وَ یُثَبِّتْ أَقْدَامَکُمْ»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77296" target="_blank">📅 05:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94bb518d25.mp4?token=TgCNfsJhRFq3ScH7BPJDmu4pFLRCFVvDdAphNqi9m-q2eA7HAZ1F6ZJ7_JpDUOe21qpVRXdeMxah6Le_68rXruZ9TY5mlwSldHrJpezBDTeLeJZYFyddT04I-EqG17cYBmC_Bw37ZgrJtWE5RyZ59eZIn4pV7Zc3Ct4m0mJt6ZUkCpxL40FZ4lUf-qnusfYX_IZOpZ5cungsQl4p7p_fkb9aCOkhcSfNaF7DTPwpS05oT8Yv6dH-LXJa2E_Vm9jgpXErQbtSdQF8mVpqBnHT838kcsTG-RrF09Sj4RgW99Kmx2Zc7Gu24r-tNfHGlDyobLwwVdoSIq860W9qKyF4tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94bb518d25.mp4?token=TgCNfsJhRFq3ScH7BPJDmu4pFLRCFVvDdAphNqi9m-q2eA7HAZ1F6ZJ7_JpDUOe21qpVRXdeMxah6Le_68rXruZ9TY5mlwSldHrJpezBDTeLeJZYFyddT04I-EqG17cYBmC_Bw37ZgrJtWE5RyZ59eZIn4pV7Zc3Ct4m0mJt6ZUkCpxL40FZ4lUf-qnusfYX_IZOpZ5cungsQl4p7p_fkb9aCOkhcSfNaF7DTPwpS05oT8Yv6dH-LXJa2E_Vm9jgpXErQbtSdQF8mVpqBnHT838kcsTG-RrF09Sj4RgW99Kmx2Zc7Gu24r-tNfHGlDyobLwwVdoSIq860W9qKyF4tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: کاری که اکنون می‌کنیم این است که هرگونه امکان دستیابی آن‌ها به موشک هسته‌ای را از بین می‌بریم
مصاحبه ترامپ بعد از مراسم فینال جام جهانی، ترجمه ماشین:
ترامپ:
به کشورمان افتخار می‌کنیم. به کاری که همه انجام دادند بسیار افتخار می‌کنیم. به جیانی اینفانتینو و تمام کارکنانش برای کار باورنکردنی‌شان تبریک می‌گوییم.
این یکی از بزرگ‌ترین رویدادها از هر نوعی بود که تاکنون برگزار شده است. بنابراین خیلی خوشحالیم که این‌قدر موفق بود. مردم از سراسر جهان آمدند و کشورمان را دوست داشتند.
می‌دانید، این رویداد کشورمان را از زاویه‌ای متفاوت به نمایش گذاشت.
اتفاق فوق‌العاده‌ای بود؛ یک رویداد عالی بود و خوشحالم که همه شما از آن لذت بردید.
خبرنگار:
شما گفتید آرژانتین باخت.
ترامپ:
این را شما می‌گویید؟
خبرنگار:
شما گفتید آرژانتین باخت.
ترامپ:
نه، چنین چیزی نگفتم. فکر می‌کنم هر دو خوب بازی کردند. من می‌گویم اسپانیا واقعاً بهتر بازی کرد.
هر دو خوب بازی کردند. منظورم این است که به فینال رسیدند و واقعاً بسیار هیجان‌انگیز بود. به نظر می‌رسید اسپانیا مسلط بود، اما مسابقه بسیار نزدیک بود. بنابراین عالی بود؛ یک رویداد عالی بود، بله.
خبرنگار:
[پرسش خبرنگار نامفهوم است.]
ترامپ:
خب، احساس بسیار بدی داریم. اما می‌دانید، آن افراد بزرگ، آن میهن‌پرستان بزرگ، در تمام این مدت جنگیدند تا ایران نتواند سلاح هسته‌ای داشته باشد.
ایران به‌شدت، به‌شدت آسیب دیده است. تقریباً همه توان نظامی‌اش را از دست داده است. چیز بسیار کمی برای آن‌ها باقی مانده. تعدادی موشک و پهپاد دارند. مقداری توان تولید هم دارند، اما زیاد نیست.
ما تنگه هرمز را در کنترل داریم. آن‌ها هیچ‌چیز را کنترل نمی‌کنند. پس خواهیم دید چه اتفاقی می‌افتد.
امشب دوباره ضربه بسیار سختی به آن‌ها زدیم و این کار را به احترام آن میهن‌پرستان بزرگی انجام دادیم که احتمالاً سه نفرند، نه دو نفر.
خبرنگار:
پیامدهای دخالت چین در انتخابات آمریکا چه خواهد بود؟
ترامپ:
بعداً درباره‌اش صحبت خواهیم کرد. با آن‌ها گفت‌وگو می‌کنیم، مطمئنم.
خبرنگار:
می‌توانم بپرسم آیا با کارنی، نخست‌وزیر کانادا، گفت‌وگو کردید؟
ترامپ:
بله، کردم. بله، صحبت کردم.
خبرنگار:
گفت‌وگو چطور پیش رفت؟
ترامپ:
خوب پیش رفت. اما به او گفتم باید جلوی ورود دود این آتش‌سوزی‌ها را بگیرید، چون هوای ما را مسموم می‌کند. هوای ما مسموم شده است.
من رابطه خوبی با مارک کارنی دارم. اما می‌دانید، باید آتش‌سوزی‌های آنجا را متوقف کنیم. اگر بتوانیم به آن‌ها کمک کنیم، کمک می‌کنیم. اما شاید باید بابت خسارت‌ها چیزی به ما بپردازند، یا شاید ما باید تعرفه‌ای وضع کنیم.
وضعیت وحشتناک بود. کسب‌وکارها تعطیل می‌شدند؛ به‌ویژه در میشیگان. اگر به دیترویت در میشیگان نگاه کنید، مجبور شدند همه‌چیز را تعطیل کنند. مجبور شدند کارخانه‌های خودروسازی و بسیاری مراکز دیگر را ببندند.
من هرگز به یاد ندارم چنین اتفاقی افتاده باشد. در چهار یا پنج سال گذشته این وضعیت کم‌کم آغاز شد. پیش از آن هرگز به یاد ندارم چنین اتفاقی افتاده باشد.
خبرنگار:
آیا فرصت کردید با نخست‌وزیر اسپانیا هم صحبت کنید؟
ترامپ:
بله. با مقام‌های اسپانیا صحبت کردم و بابت داشتن چنین تیم بزرگی به آن‌ها تبریک گفتم. با افراد زیادی صحبت کردم.
خبرنگار:
پیش‌تر با اسپانیا تنش داشتید.
ترامپ:
نه، هیچ تنشی ندارم. با هیچ‌کس تنشی ندارم.
خبرنگار:
[پرسش خبرنگار درباره اسپانیا نامفهوم است.]
ترامپ:
خب، [نامفهوم]. می‌دانید، توانایی زیادی دارد. اما تا جایی که می‌دانم، ظرف حدود یک ماه [نامفهوم] تا آن را به حداکثر برسانند. بنابراین قرار است آن را بفرستند و به حداکثر برسانند. فکر می‌کنم حدود یک ماه دیگر.
خبرنگار:
آقای رئیس‌جمهور، آیا با نخست‌وزیر کانادا صحبت کردید؟
ترامپ:
بله. همین حالا داشتم پاسخ می‌دادم. درباره‌اش با او صحبت کردم. گفتم: «باید جلویش را بگیرید.»
مسئله در اصل مدیریت جنگل‌هاست و آن‌ها باید بدانند چگونه این کار را انجام دهند. اگر چهار یا پنج سال به عقب برگردید، به یاد ندارم هرگز چنین مشکلی داشته باشیم. اما حالا این مشکل را داریم.
فردی در محل:
از این طرف بیایید، آقای رئیس‌جمهور.
خبرنگار:
شما گفتید جنگ را ظرف چهار یا پنج هفته پایان می‌دهید.
ترامپ:
[آغاز پاسخ نامفهوم است.] کاری که اکنون انجام می‌دهیم بسیار بزرگ‌تر است. قبلاً کار محدودتری انجام می‌دادیم؛ می‌خواستیم مانع دستیابی آن‌ها به توانایی خاصی شویم. حالا داریم کار را تمام می‌کنیم.
بنابراین واقعاً همان موضوع قبلی نیست. کاری که اکنون می‌کنیم این است که هرگونه امکان دستیابی آن‌ها به موشک هسته‌ای را از بین می‌بریم.
اگر نگاه کنید، پس از یک هفته و نیم ــ نه چهار هفته؛ یک هفته و نیم یا دو هفته ــ جلویشان را گرفتیم؛ احتمالاً... اما نمی‌خواهم از واژهٔ «احتمالاً» استفاده کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/77295" target="_blank">📅 04:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iszhx07Pk7VRJTggxjcSa-c8ILyFYh9I0T118KIc6hMZ77Z2WIcVlxvyq4T_PkXLYvop54mtrVQ_3XN37VMZjNfI3JeKXmu1BluT44wp-2VU5jL6ec95u13SlhyFFtvSwW-FF7sdTllaggqaOakPHgyUU4qPwrNgd0WjGQBI4ZvItf_2A2xUJja2bTy0o4Snfdowe2JIwo6hRieYk7za8y3S8QA2vrM0d1isvSB689fRc3_nufc0PR7bWFSnIplJ8euWKie3swIRX55Oryz0O2QIN4VPcScV7HItoc6FGyoH1HUTDlMVO1m2_WjjnGObumglrvxQM8EAomj9aF5s2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت: تصویر منتشرشده با شرح کنارک
پیام‌های دریافتی:
بازم یه انفجار چابهار ۳:۵۱
کنارک صدای انفجار(دور بود)
و همینطور صدای جنگنده
نیم ساعته از بعد جام جهانی داره چابهار و کنارک رو سنگین می زنه. جاهای مختلفه و نمی دونم کجاها بوده فعلا
دوباره خیلی سنگین زد
چابهار ۳:۵۱ صدا اومد
همین الان چابهار دوبار زد 3:51
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77294" target="_blank">📅 03:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzPYVY2bkMG12zkTiIK3_rgyiMEt-blcFB6Q5jYziR4ieP3MBm-I5aXtNExbn5QysV8JFbaIDVuP89-dBPlKon_2QNNX88QNDDOh2beMtkzxRbW2WenmMEDpfnGXwMMfxYbYxxPity6l1PMzGzf7rkDODBVU4wFX8uCT9rm0xPqgi40_IyY855VuxHTa9LhMez3w122salbgULFaiXoCBfELv5aIX9qE3iw_pxzxNswgY-bkE1LsWKm0fcay4p_2QftGu0YpXN7N_Qp9xcEg8rrHn_g2Wk8Honu36HTy66LPSkeyVlXbnYNIa_HNggt6iDRmadVpcCZURGo4BEgOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با آغاز نهمین شب حملات متوالی آمریکا به مواضع نظامی در ایران، بامداد یکشنبه، فارس از اصابت چند موشک و شنیده‌شدن صدای انفجارها در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر و بندر خمینی در خوزستان خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77293" target="_blank">📅 03:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیام‌های دریافتی:
سپاه خورموج توی استان بوشهر رو زدن برق ی منطقه هم رفته
سلام وحید  ساعت ۳:۰۷ دقیقه
خورموج پنج انفجار شدید
همین الان خورموج پادگان سپاه زدن برق هم قطع شد
همین الان سپاه خورموج زدن ساختمانش کلا صااف زمین شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77292" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پیام‌های دریافتی:
چندین صدای انفجار پیاپی، سیریک.
ساعت سه و پنج دقیقه بامداد شهر سیریک ده ها انفجار بسیار سنگین
سه تا آخری خیلی بد زد موجش زیاد بود
احتمالا اسکله بوده باشه
۳:۰۵ تا ۳:۱۰ چند انفجار سمت سیریک (طاهرویی) خیلی شدید
سیریک صدای انفجار پشت سرهم خیلی بلند، صدای جنگنده‌ها هم میاد
بندر عباس ساعت 3:11 دقیقه چند انفجار پشت سر هم و طولانی رخ داد و تا دو دقیقه ادامه داشت
بندر جاسک همین الان دوتا صدا اومد
بندر جاسک دوباره صدا اومد صدا خیلی وحشتناک بود
سیریک حدود ۸ انفجار شدید شایدم بیشتر  شیشه های اتاقم نزدیک بود بشکنن
جاسک جنگنده بالا سرمونه
۳تا انفجار تا الان
بیشتر از ۳تا شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77291" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fzdw2-5xREz93XQeRMYabJBxswdR7TLe_nqq3wdghXqcbA4QP_N1oJkjmjtGgN7vsHOiLC_CIDyPlqJFY6WGikh_kgth50cLdste-L7J0AFba642ZjhmV7mRvOJV2ct1H-YEk5IFldTHhaVtVLcSFgk5xAimB2fsZ_5AlC3Z63SbHefh9aBdRtuoVI-RN55rvZXvsM47piQQEz10rqfohGM7Xiubi-dznfSaWf9ec-gXuhD3PLGRJn_r88x6x3i9AGCRlsODrw_1vwpWTMmJl_1ju3wfNDlDLDVbEYH2M3oU3fTUYbatAksBAjLG9XtYLk0gzGodong83exfrImA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'سربندر ("بندر امام خمینی") ساعت ۲:۴۰ دوشنبه ۲۹ تیر'
Vahid
دوباره زد
سربندر خوزستان 3:08 دو صدای انفجار و لرزش شدید خونه
وحید جان دوباره سربندر دوبار محکم زدن
وحید سربندر رو باز هم زد
تک انفجار، ولی خیلی سنگین ۳:۰۹
۳.۰۸ دقیقه سربندرو بازم زدن
اقا وحید ماهشهر دوباره زد
شیشه اتاقم لرزید این بار
صدای انفجار قبلی رو فقط شنیدم
خود ماهشهرم، سربندر نیستم ۳:۰۹
وحید ماهشهر یکی سنگین زد
سربندر دوباره زد صداش بیشتر از قبلی بودد
ماهشهر دوباره شدید ۳:۸ دقیقه
ماهشهر رو دوباره زد ۳:۰۸
همین الان باز ماهشهر دو انفجار شدید
سربندر ساعت ٣:٠٩ دقیقه دوباره انفجار شدید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77290" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=BigrnLtbmn59ML3AMSF4b-dDCe-Ym7Sl0ITfyNfZAo1r3_btx8FFdHpmpUrFUm_gYROeVPvP4_GvhO2fqRbMOKlhGy3xq_r9MW9bnIYxumpV4GHiGbNcyj6YTLmtz8Fw7UIXVcE3XuMTM8N1gPlNwOSIPxvn4JbOHKPjnS-J3kIQZC6eJ7Q4BoKovO2DRUSfim1uOn1PzHxpCxSKAdB5vN0v4ijnYxRG8AovktVRlld92ULg52tE5l8kcOhIABaB8JSwANPviefv7005skQQqU138VrWd_fI9JKam6UlL7AhsnwjJcRlWsQDNN-e6-JYHCuiIPkcdyE6RkElN7YEwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=BigrnLtbmn59ML3AMSF4b-dDCe-Ym7Sl0ITfyNfZAo1r3_btx8FFdHpmpUrFUm_gYROeVPvP4_GvhO2fqRbMOKlhGy3xq_r9MW9bnIYxumpV4GHiGbNcyj6YTLmtz8Fw7UIXVcE3XuMTM8N1gPlNwOSIPxvn4JbOHKPjnS-J3kIQZC6eJ7Q4BoKovO2DRUSfim1uOn1PzHxpCxSKAdB5vN0v4ijnYxRG8AovktVRlld92ULg52tE5l8kcOhIABaB8JSwANPviefv7005skQQqU138VrWd_fI9JKam6UlL7AhsnwjJcRlWsQDNN-e6-JYHCuiIPkcdyE6RkElN7YEwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'سایت موشکی تبریز'
دوشنبه ۲۹ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77289" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/028b9087f7.mp4?token=EtS_4nzTzrFDPZsSch3BOskyk8JYH-RCHSGWvNEVe_5ndBTQV4QDUq5tbHoyYBWZxpOVJGFWIKgW3GxL9YoUjhBMMoUtMKQpup1RXUjJKU0NspX_v-IEH2wv_4QDW0SHSTYejA9iSJzu8Qt1EN4KSdmZJqcjBVejBu8HZU8z8cF4LxWKD8uyHC3kFtIYebPPq__Cb_BcV6mknZE7h2m-I5lDi-floigTcLn6WtwO8YbCL99RRtScQJ7FVhV37ZbzPekbT95gVIpq6x2im3YzVYnbbuytVK4k34hhc5zplP61XT2-OkYO382RDAar1HYBOhWWkm7EWy8eynfbWTu9Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/028b9087f7.mp4?token=EtS_4nzTzrFDPZsSch3BOskyk8JYH-RCHSGWvNEVe_5ndBTQV4QDUq5tbHoyYBWZxpOVJGFWIKgW3GxL9YoUjhBMMoUtMKQpup1RXUjJKU0NspX_v-IEH2wv_4QDW0SHSTYejA9iSJzu8Qt1EN4KSdmZJqcjBVejBu8HZU8z8cF4LxWKD8uyHC3kFtIYebPPq__Cb_BcV6mknZE7h2m-I5lDi-floigTcLn6WtwO8YbCL99RRtScQJ7FVhV37ZbzPekbT95gVIpq6x2im3YzVYnbbuytVK4k34hhc5zplP61XT2-OkYO382RDAar1HYBOhWWkm7EWy8eynfbWTu9Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'انفجار در
#تبریز
'
بنا بر پیام‌های دریافتی از شهروندان حدود ساعت ۲:۳۷ دوشنبه ۲۹ تیر صدای چند انفجار در تبریز شنیده شده.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77288" target="_blank">📅 03:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77287">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hax0nD4takpSnaKkW3ETVhsi7Gy2xau0aSU5yAxzF8jJVY9c-rJ-Yppc3-A0gTDca_XVM1H-7LU9AN_bpZiZJVdph_nROJtlP6xdwm4ZWKEIq_o4uaaSzmO56DyC0ai86l5iHQtRfdmC9Nmlt73ZhvsMWTThRWCNKT6MosTG7cLk0sOZ9EI7pWjw6l7zFkvk_Py1shBY1rwhf2UsHdloOK977PEXEdZMAIlASeAYY1NZ3xdTGh2xrdP3lqY1GUlFi4elrJlUk8Wd5o17fiDBle2KB1x6YQstsy-XA3Vyr3BgScOUmQmI6vS30aD0-QVvs0AYaPPkrpaoU8QJsYjwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
سنتکام امروز ساعت ۷ عصر به وقت شرق آمریکا، برای نهمین شب متوالی موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات به تضعیف بیشتر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی در حال عبور از تنگه هرمز به کار می‌روند، ادامه خواهد داد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77287" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌های دریافتی:
۵ ۶ تا همین الان کنارک
خیلی خیلی شدید بود هنوز داریم میلرزیم
۳ تا دیگه همین الان
چابهار الان صدا انفجار پی در پی اومد
2.43
چابهار 4تا صدای انفجار شنیده شد دور بودن
چابهارو الان زدن ۲:۴۴
چابهار صدای انفجار اومد
کنارک 2:42 سه انفجار پشت سرهم
کنارک ۳ تا انفجار
سلام بازم دوتا قدای انفجار ساعت ۲.۴۵ در کنارک
خیلی بد داره میزنه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77286" target="_blank">📅 02:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام‌های دریافتی:
ماهشهر صدای انفجار اومد میگن سربندره
سلام وحید جان
ساعت 02:40 سربندر صدای وحشتناکی اومد.
آقا وحید ماهشهر همین الان چندتا صدای مهیب و لرزش شیشه ها رو داشتیم
همین الان ماهشهر رو زدن
سربندر ۲:۴۱ انفجار شدید
سربندر دو سه تا پشت سرهم یکیش خیلی نزدیک بود یعنی پدافند رو زدن
چون تازه دود دیدم از سمت سایت پدافندی  نزدیک خونمونه
وحید جان همین الان سربندر خوزستان  شدید زد
وحید جان 2:40 سربندر انفجار بسیار قوی
بندر امام خمینی، خوزستان
من ماهشرم، هیچ صدایی نشنیدم، شاید سربندر رو زده باشن، اما ماهشهر هیچ خبری نبوده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77285" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gv9CGQIUdU1WJy-f83L-hW4Nfb9wR_mifaS5EaYfAHQd4Tj1JLWgX910Sr_Dgoy942-QLCMCs_vIRInq-JQCeA8-bHasJEAvTmEanpJOv830ZNMjFAM1O6ylEKZ4k2SkCJJ_m7hSkooK5E5H5w9oEcwuqUqwKarzWzPYzoLW0FE7QpVkIP6_SPGBIeLkihfvvoGGmT62LMboMmbBJ-MJuDBbTUYrIyNEykscDCNDmaVYk6hZyCuhNabAgFyBFQXGkkReRcWFCLNgnpF4kZnZIBUUPqbLf5rd2s5ez_9BSA-67a6G4y-Kt8z4jNPzYeVSJ-fjhcB8ZQtWi9GhxyNKSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
وحید همین الان صدا اومد از تبریز ، ۳ تا
تبریز همین الان ساعت ۲.۳۸ صدای انفجار شدید اومد
صدای چند انفجار وحشتناک از تبریز همین الان
تبریز سه چهار تا صدای انفجار ا‌مد
سلام تبریز الان صدای ۳ تا انفجار اومد
صدای چند انفجار پیاپی - تبریز ساعت ۲:۳۷ بامداد
وحید جان تبریز 3 باز زدن شدید
سلام آقا وحید 2:37 صدای ۳ انفجار اطراف تبریز
سلام وحید. ۲:۳۷ انفجار در تبریز
ساعت ۲:۳۸ تبریز
چندین صدای مهیب انفجار
وحید تبریز یه صدای مهیب اومد نمی‌دونیم چی بود ولی انفجار بزرگی بود
همین الان تبریز پشت سرهم ۴ تا صدای انفجار اومد
سلام تبریز زدن ساعت ۲.۳۷ دقیقه
مکانی که ما بودیم قشنگ لرزید صدای انفجار هم اومد اما سمتش نمیدونم دقیق کجاست
سلام آقا وحید. الان ۲:۳۸ تبریزو زدن.
سلام وحید جان چند انفجار پشت سرهم در تبریز ۲:۳۷
خیلی شدید بودن
سلام تبریز صدای ۲ تا انفجار اومد
سلام صدای ۳ ۴ تا انفجار پشت سرهم  اومد تبریز
وحید  ۴ انفجار پیاپی تبریز
همین الان صدای انفجار تبریز ۰۲/۳۷
تبریز صدای ۳ انفجار پشت سر هم،ساعت ۲:۳۷
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77284" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/668363f045.mp4?token=I02lMNkN_vdc3J_kDfs-mxQQu7ENHCnjqO32DvN4k6RFirbHA17_NYZoqTcgKZKATJm7oKDADhdW6r-RWCfkiA3kckEZ6fK9uJdlfy6yYc-IyxNrziITeIbLDkQexH7mZfMnETwknm1qVAwa6CnWDg8Xs6LnioTBEEcUd9mkpKKt9NrLGrRT_NffsTQH2pOi9tuuCPR5SKK3g_1AuyYnxxyx-mOS9bj_UyQaFg6d62xPIM09e-Ovjt5qynWwrcJYpDFDPqzfk260kGb-UPGHd3AIkDcNKZHXh1T4x1qKpO3UXG3ez4pms85pMRnAujY5lkOIe6opWrsLTj6MXSZ2cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/668363f045.mp4?token=I02lMNkN_vdc3J_kDfs-mxQQu7ENHCnjqO32DvN4k6RFirbHA17_NYZoqTcgKZKATJm7oKDADhdW6r-RWCfkiA3kckEZ6fK9uJdlfy6yYc-IyxNrziITeIbLDkQexH7mZfMnETwknm1qVAwa6CnWDg8Xs6LnioTBEEcUd9mkpKKt9NrLGrRT_NffsTQH2pOi9tuuCPR5SKK3g_1AuyYnxxyx-mOS9bj_UyQaFg6d62xPIM09e-Ovjt5qynWwrcJYpDFDPqzfk260kGb-UPGHd3AIkDcNKZHXh1T4x1qKpO3UXG3ez4pms85pMRnAujY5lkOIe6opWrsLTj6MXSZ2cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال اسپانیا با تک گل فران تورس در وقت‌های اضافی آرژانتین را شکست داد و قهرمان جام جهانی ۲۰۲۶ شد.
این دومین قهرمانی اسپانیا در جام جهانی است که این بار با پیروزی مقابل مدافع عنوان قهرمانی به دست آمد.
@
VahidHeadline
تلویزیون سراسری در ایران مراسم اهدای جام جهانی فوتبال رو به خاطر حضور ترامپ پخش نکرد.
ترامپی که حتی موقع ثبت لحظه تاریخی بالا بردن جام هم حاضر نشد از کادر دوربین‌ها بیرون بره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77283" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c82cf41e.mp4?token=genDqbXzBA2nfABmxVPqFu__HObr8oTMiXQXT1P_XQEaVac_IpgST5c9bu3vAJB4Cy6moimoqyyIC_SirjffioT4oBmHHSV20rWDbpoOuusysg-wPdOkLa6UK2E5zSVt0djybhJkHanPa4RfoVpbSKnqAi7lFVJWoothcXM5vTUrieOtA-d3j8UNq2caBXxtmkG2YFUKMUngu8xd8ZOQhiljZ854s0xwEFjqJSk9racDUcX2m3ZA6mwBzExMT5n0uqQ0TmaontkLFDvCeyzAvvSCv7FRqk0Wuh61IPKzhNt1CgBI9Qt_Krvny9SMFS_Kr_OtG2hAjEIVWfoGw15SyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c82cf41e.mp4?token=genDqbXzBA2nfABmxVPqFu__HObr8oTMiXQXT1P_XQEaVac_IpgST5c9bu3vAJB4Cy6moimoqyyIC_SirjffioT4oBmHHSV20rWDbpoOuusysg-wPdOkLa6UK2E5zSVt0djybhJkHanPa4RfoVpbSKnqAi7lFVJWoothcXM5vTUrieOtA-d3j8UNq2caBXxtmkG2YFUKMUngu8xd8ZOQhiljZ854s0xwEFjqJSk9racDUcX2m3ZA6mwBzExMT5n0uqQ0TmaontkLFDvCeyzAvvSCv7FRqk0Wuh61IPKzhNt1CgBI9Qt_Krvny9SMFS_Kr_OtG2hAjEIVWfoGw15SyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی از قم با شرح پرتاب موشک
سایر پیام‌های دریافتی که شاید درباره پرتاب موشک باشند:
وحید شهرستان محلات صدای انفجار مهیب اومد . همه جا لرزید
23/44 صدا انفجار از دور ساوه
ساوه ۱۱:۴۵ دقیقه
صدای انفجار
سلام وحید جان صدای انفجار ساعت ۲۳:۴۰ ساوه
نزدیک قم یه صدای انفجار اومد
سلام وحید  الان صدای جنگنده خیلی نزدیک  دلیجان
صدای دو یا سه تا انفجار شنیدم اما خیلی فاصله بود. فکر کنم خمین با اراک بود.
ما خنداب هستیم.
قزوین صدای جنگنده [که معمولا با صدای پرتاب موشک اشتباه گرفته میشه.]
از دلیجان موشک پرتاب شد
ساوه صدایی اومد. مثل انفجار. ولی انگار از دور بود
اراک هم صدای یه انفجار از دور شنیده شد
وحید جان ما اراکیم یک ربع پیش سه بار صدای انفجار اومد اما بار اول صداش خیلی خیلی بلند بود
🔄
منابع حکومتی:
فرماندار اراک اعلام کرد که صدای شنیده شده مربوط به اقدامات آفندی در یکی از استان‌های مجاور است و جای نگرانی نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77282" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceJgXw2M9z1KIREOqQs30ZBjvgWVRCM8OEIuAgezINvbtmJMgYWJVEHtOBNEWbMsdHvXNb4VP6EjvYpY6UiXZ_d-3ilAoa4CvTP58kPNLyrDRUXLROocDzszYvMGwKIWMIHYCbKyDjzKzc9SJSH3PcdSrmCIWFC145K2E7tCIgSv2Xre_9zIqfcfg2diVxNFd2s9GFnQpBKc8LwxGZ035d0vMBM3JVl1KT7yoDznUUezwRMOmn6A0kKIGqrfyWHQdu0uP1AT1ImahZhSox-JwgzgiJCSY8G81DKFo16pIPdFKIIwSsYvm8td9ULXyxGPmfoCt2EluW8l4Y7dAAtTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
به‌روزرسانی سنتکام درباره نظامیان آمریکایی جان‌باخته اخیر
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دیروز اعلام کرد که در پی حمله ایران در ۱۷ ژوئیه در اردن، دو نظامی آمریکایی جان باخته‌اند و یک نفر نیز مفقود شده است. پس از جست‌وجویی گسترده، نیروهای نظامی آمریکا اوایل امروز بقایای انسانی ناشناسی را در محل پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق روز ۱۸ ژوئیه هنگام انفجار کنترل‌شده مهمات منفجرنشده متعلق به یک پهپاد انتحاری سرنگون‌شده ایرانی، در جریان عملیات کشته شد. یک نظامی دیگر نیز زخمی شد و همچنان برای جراحت جزئی خود تحت درمان پزشکی قرار دارد.
سنتکام به احترام خانواده‌ها در جریان روند اطلاع‌رسانی، از انتشار اطلاعات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/77281" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0zDOPuP1TV7DCBHvmQVJi081KW2hkZFD26E6QBmeTrbYfB-VN8QECKx-Fpa4C4a70b3hB5wHqCQ5fvvr7djq6lw-jGnRz1_VXqkpJiBvnWA_ze41GIdqXaA9rIScIKp7S_mttKjhBrinnKMP_SuHO5mEsj0kb5Nn0lAeIxiZF2XpbkJC2eUakb4Q9iNJdm5D9eOML09-ouhKdZ7WmeHDWWhOgIOzUJx4EqRpfHgvkBCyRqIZchwwIlxq7C5V2pZ7c30QKq2ejJKk2W_eckktYLF9L9NRfYWCb4y0yjTmVNWZlgdCvE9AePvrs9o4hdNZO4b4mQQUgYayZ7umtbusQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران گفته است آمریکا بامداد یکشنبه با «تعدادی پرتابه» به سایت در حال ساخت نیروگاه دارخوین حمله کرد. دارخوین شهری در بخش دارخوین شهرستان شادگان در استان خوزستان ایران است.
آژانس بین‌المللی انرژی اتمی اعلام کرد که در حال بررسی این گزارش‌هاست و یادآور شد که این نیروگاه «در مراحل بسیار ابتدایی ساخت قرار دارد و در آخرین بازدید آژانس، هیچ ماده هسته‌ای در آن وجود نداشت.»
آژانس افزود که این حادثه «احتمالاً هیچ خطر پرتوی ایجاد نمی‌کند»، اما رافائل گروسی، مدیرکل آژانس، با انتشار پیامی در شبکه ایکس «خواستار خویشتنداری نظامی در اطراف همه سایت‌های مرتبط با فعالیت‌های هسته‌ای» شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/77280" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/PJw9hkxK_oTU-YohH67SUMYd7y6VaqZqaijXf5hO1KbKVPMnOeUbPPaFcvz0lKF8Vq9SAIQxJd3a8VjAyBi95faCcwVmTvVhe-oa43jjGAutPA8nSmsmUZTVoXbDXJ_Hd93aRJsMDBNxO1be_FMGVmurilMr4JYkHPCcijkNDEiZ4IvBVVJry949_Og_ay7ep-rutdtGhB56aurCqFYahifU3bWeb7T8Lhuj3SYLR09iIFDDCWTiTCDiMqI_CwKpQhRkDnz7QsdtZz18SXmVp0TZpo9RM0zuU7IdbncxCrIT94f5gvCG95gyYaxYYblEeALDoQ8H-eewyAoJQ3N5ow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.87M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 10:35:22</div>
<hr>

<div class="tg-post" id="msg-653963">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E25LQ5aaV4sQeQM_1tcZ5CQbhIgFW2Q_W0cf7fHIdf2MHMFQoh7ewR7YcFk7KF3y0vFrfiCRcRbTf-HsyI1CxmjZw1daApPJl7zULRgtO2VqyPuuQuTfzDpIGfFYLwWCN_SthyZn9XNO-MnjoCJ6Aa8rhuXzjCT1tdEnQFnBEBJUzMih1lUTNG4GWmNyYio1RxxINTc8laTc14dEv3yJlNoByyQd9jl0G91HH01RCK9WwgJY1VyknSy74qS-yBv8sVtkSlisFjdCxgfxbBhhLGUFZKAwZVuwjLl6Su3zd--4wPOsu8TEQlznOO1nS5V0xdrO-U1MPneI5nWElwOlyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه عبری: استراتژی نتانیاهو در برابر ایران فروپاشید
🔹
روزنامه عبری «هاآرتص» گزارش داد: سخن گفتن از «دستاوردهای نبرد»، برای گمراه کردن مردم است؛ استراتژی نتانیاهو در برابر ایران فروپاشیده است.
🔹
از سوی دیگر، روزنامه عبری «معاریو» نوشت: حزب‌الله به دوران تحمیل معادلات بازگشته و نگرانی، محافل ارتش اسرائیل را فرا گرفته است.
🔹
همزمان، کانال ۱۲ رژیم صهیونیستی تصریح کرد: طی هفته‌های گذشته، نظامیان ارتش اسرائیل گفته‌اند که به دلیل آسان بودن هدف قرار گرفتن آنها توسط حزب‌الله، احساس «اردک در میدان تیر» به آنها دست داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 332 · <a href="https://t.me/akhbarefori/653963" target="_blank">📅 10:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653962">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
قالیباف رئیس مجلس شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/akhbarefori/653962" target="_blank">📅 10:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653961">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5275bdcf0.mp4?token=C2ViB7Tj-R3OuhE_7x7fKAQ32_cP-yQuo52vO8qRH8jiYTPnOUyi14EozHKiX_FeJiGP-eC-Mx2WGw_v9hd5oJkXv1AIkjmr6sz_aPOvg4mU_AcgPwYrnIRfXfdtkb-HoREYxi0yGjE8zmv8CTkfBVUPtOnNYDyHX2M59DUhUPSSEHgWirO8Ipk8Pf1lVH0R6JutWFUZyTOxu85ATnAOUmjTWWjyMwoINu8l663Hh1gwJsAqE8F97mJ1-N3mxFSbr5XdwyiyoXcJ57JUoLCsmrMipbDfBM3OJXLLR0sFaNjTrwtomUw8X52FWjSoR-rXC6x9CeXCC_3tJ_TcGseZEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5275bdcf0.mp4?token=C2ViB7Tj-R3OuhE_7x7fKAQ32_cP-yQuo52vO8qRH8jiYTPnOUyi14EozHKiX_FeJiGP-eC-Mx2WGw_v9hd5oJkXv1AIkjmr6sz_aPOvg4mU_AcgPwYrnIRfXfdtkb-HoREYxi0yGjE8zmv8CTkfBVUPtOnNYDyHX2M59DUhUPSSEHgWirO8Ipk8Pf1lVH0R6JutWFUZyTOxu85ATnAOUmjTWWjyMwoINu8l663Hh1gwJsAqE8F97mJ1-N3mxFSbr5XdwyiyoXcJ57JUoLCsmrMipbDfBM3OJXLLR0sFaNjTrwtomUw8X52FWjSoR-rXC6x9CeXCC_3tJ_TcGseZEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمریکا به دنبال باز کردن تنگه هرمز به هر قیمتی
🔹
سید محمد مرندی، تحلیلگر سیاسی: آمریکایی‌ها نیاز دارند تنگه هرمز به هر شکلی که شده باز شود. می‌دانند با نیروی دریایی یا هوایی نمی‌توانند این کار را انجام دهند. چند هفته پیش عملیاتی برای باز کردن تنگه آغاز کردند، اما پس از چند ساعت ادعا کردند که به درخواست پاکستانی‌ها فعلاً متوقف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/akhbarefori/653961" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653960">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtXzF-iG8yuuj78LAoYJktl17fI_q1peemJXNH3BIrNTolY4kfN4-zFOMBJNBdrDF-Fh-x3jcBqTKBI1EJsNgHp4bYn5C2f3fgMVnaGoDOM-K7ONpMA97MttVN-61Bz3wqmZD6MRSTG77EdmVMt6mZgiyPq8JyodazHww2x1wNI88lSEMS5JuNr15_yv7COThHE-PAbLRz0GQE-7loSHbz4g077ObQzA6Hmim9lSK8rEXv9W2SpIYfXGlvGIAhwPbGPk8mlCNNuC-OfLm3-oZI4Il2jsIf8XhogScIJLDXqPoXrX9ly9wfAtSfBzhFiTF8dWSEE7yjzoCmyCp95jFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا منتظر بنزین ۶ دلاری باشد
🔹
سخنگوی کمیسیون امنیت ملی مجلس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/akhbarefori/653960" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653959">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
از قبض برق تا قبض روح/ مشترکان پرمصرف منتظر صورت‌حساب‌های سنگین باشند
🔹
مدیرعامل شرکت توانیر در پاسخ به سوال: یکی از برنامه‌های راهبردی شرکت توانیر، رعایت عدالت در توزیع یارانه برق است. برقی که در شبکه سراسری توزیع می‌شود از یارانه‌های دولتی برخوردار است و طبیعتاً اگر مشترکی بیش از سهم خود برداشت کند، هم در حق دیگران اجحاف کرده و هم در تامین پایدار برق برای شبکه ایجاد مشکل می‌کند.
🔹
اله‌داد در خصوص گروه‌های هدف برای اعمال محدودیت‌ها: تمرکز ما بر مشترکانی است که بیش از ۲.۵ برابر الگو، مصرف دارند. اگرچه این گروه تنها ۲ درصد از کل مشترکان را تشکیل می‌دهند، اما بیش از ۱۰ درصد از برق شبکه را مصرف می‌کنند.
🔹
هم‌اکنون بیش از ۸۰ درصد این مشترکان به کنتورهای هوشمند مجهز شده‌اند و در صورت افزایش مصرف بیش از الگوی تعیین شده، برق آن‌ها محدود یا قطع خواهد شد. مشترکان پرمصرف باید منتظر صورت‌حساب‌های سنگین نیز باشند؛ چرا که قبض برق این دسته از مشترکان ممکن است در برخی موارد به «قبض روح» تبدیل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/akhbarefori/653959" target="_blank">📅 10:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653958">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
وزارت امور خارجه چین: جنگ ایران هرگز نباید اتفاق می‌افتاد و نیازی به ادامه آن نیست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/akhbarefori/653958" target="_blank">📅 10:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653957">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKse0ItxA2DVP_6pw9U0wjZBkyKq_ez63X-gtqSsF-jxUsa95xB4vMaXpkkvofc2Tjo_lruOEZcg7txFQ0S7pnyna7q6ZPEyVXQPyFh8VsijVSZBFVQH0kF9b99WlVB7B8X_l4GzPtf8i7LbuUZnIYXzRnPnirk7AjXxffzkfOnPzck-vmEaYDBpOz3AAnIQC9cE5bN7EXXk-_WNVneem_8RRHn1_MyB43sLEVPqI9CitUURKu_qK623sLJJMAYeX0ECH6JCI9Sf8JiIRa6vKsN6VGbHU3ETshC7WJEfnHtfnVE5FmtUCjbPcHmyBpEzuxBqbu-06TqhpVQGy2sN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان وال استریت ژورنال به جاه طلبی رژیم صهیونیستی در غزه
🔹
روزنامه وال استریت ژورنال فاش کرد که رژیم صهیونیستی با نقض مداوم آتش‌بس در غزه، کنترل بخش های بزرگتری از نوار غزه را در اختیار خود گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/akhbarefori/653957" target="_blank">📅 10:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653956">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8NsJdgCUULE2InnpeIRzClnQQp63f7sxRemufN1sXpW7JSckyxBQ3X44ASsFIVf0wLa3_P93TYARUob3sisioNNYza5Z6eJQyWd2GKUsu6wkviWMEygNe14IfxxwGkzPjUAd-6dO_SqChIi-L-FebP6mPg4F1x8PJY8ISysF3BnsIEYkJkFwXhvmLlRSSL7hZRt7NfXCzHgeJFlyrVp35eHj2SRmaCN1nJG_2dVKV2IFWzdzMYSnIAZ5Mpen17yLDetyXSYuEinCPBwRP586u-59S369j_THCfodBdYrE0eZIXBLiICSfkQnYjfeM4-2Vo0qrh4es7HmkEJo6Wu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مناسک حج آغاز شد
🔹
همزمان با فرارسیدن یوم‌الترویه (روز آماده شدن برای آغاز مناسک حج)، فرآیند انتقال زائران حج به عرفات از ساعاتی قبل کلید خورد و مناسک حج تمتع امسال وارد فاز عملیاتی شد.
🔹
۷ هزار زائر اهل سنت کشورمان با اتوبوس‌ها از هتل‌های محل اسکان خود خارج شدند و حدود ۲۳ هزار زائر دیگر هم امروز به مشاعر مقدسه منتقل می‌شوند تا از فردا خود را برای دعای عرفه در صحرای عرفات آماده کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/akhbarefori/653956" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653955">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDT9O94aRDmpKxTmLPRfSNP_J-lhgFyLpTyA0icIU6K-2rdW0Hao5pX6_qDPAIVjEOWF_wDXF-Y2mCroLIEAip22K9s8G6WxyfOHBrkAAaIiZl0UqhXaub4Ajt9TQlbvIxFXPR7Ef0GSUKnxIvswi11W9k--sxigmZoDaXKQbww33Ppc6LzbvKiF2LNboTfAdOh-26ImxvFEI7RTPpZbr3fi5CkDON29HknC5F8YJYnDJN-0mvB-0Z61lkuFfcFYxlEhL169dBYxS4_aDTggnBqm2zCDSSVNvlgl3kgaxaV5sS49TivbfXoxnJ_vM6bOh7MFcLGrWZtYMRlE6j6j_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: مقاومت امروز همچون خرداد سال ۶۱ و ۷۹ زمینه‌ساز آزادی قدس شریف است
🔹
فرمانده نیروی قدس سپاه: حماسهٔ ۳ خرداد ۶۱ زمینه‌ساز حماسهٔ پرافتخار ۴ خرداد ۷۹ برای حزب‌الله قهرمان بود که رژیم صهیونیستی را از جنوب لبنان اخراج کرد. ارتش رژیم فراری شد درحالی‌که ‌بیسیم‌هایشان روشن و همهٔ امکاناتشان در سنگرها جا مانده بود. مقاومت امروز فلسطین عزیز و لبنان قهرمان هم باعث آزادی قدس شریف خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/akhbarefori/653955" target="_blank">📅 09:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653954">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رژیم صهیونیستی هشدار تخلیه ساکنان ۱۰ روستا و شهرک در جنوب لبنان را داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/akhbarefori/653954" target="_blank">📅 09:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653953">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMZIOb2zt_EPtVzmOHRp47t-pXF0vUwrWXLo6ZOATTp2JBt73s4reMgPCGyKO5cL0NASndpQhS34pcnNjZU4HDDkczNJwP6A4syYVSW8CZRZcJjvPxRJrlV3dIF-xqicVbCGnrq_a0K1RXUhYIlU59rbQv97mxYe5DJI2A1_ODJF27qNaoqynGWDrBdhySPjlv_yN4Tw71dbQZxHN131CZncBnPS2n6wYOjW2wCIADMt-Xm6O0UoTblup-dVVK9HNyDVHDavnMieqj-g_SK5LX-dVjbcLN0lOfdFNs--JGRnM7lZk1AkTbhALKSO1RgAmWrqtt6XDG56K_lwEj_FnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود پلاستیک ممنوع
🔹
برای کاهش آلودگی و حفاظت از محیط‌زیست، باید ورود پلاستیک‌های یک‌بار مصرف را به خانه‌های خود محدود کنیم  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/akhbarefori/653953" target="_blank">📅 09:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653952">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
دادستان تهران: بیش از ۵ میلیارد یورو ارز با پیگیری قضایی وصول شد
🔹
دادستان تهران از وصول بیش از ۵ میلیارد یورو ارز به کشور از صادرکنندگانی که نسبت به رفع تعهدات ارزی خود در موعد مقرر اقدام نکرده بودند، خبر داد و گفت: بیش از ۲۰ میلیارد یورو نیز تعیین تکلیف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/akhbarefori/653952" target="_blank">📅 09:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653945">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hg1GrvOyz4UGv7ZErrqCaFFV7E8txUA9qe0eYAGePXBF5tbPQo_Td8UvHikIbbJzejZi-aCYe6OHvtRXK3sQgpjOfTUKh2InUHU3Jo0wdqg7rZ3Dnjc8tQl8nAcPzXDwghiv94yQQ0-m8SMcVogyxVr-77lgIF6L8XiqpJLYku7gLpvtZrdyZkC5pUpz6EbafLNWTVLFVnogY2ssqBXvM-bus6yLV8qflAHJFH2ATBfj5N7pRK2k2fCxPE0q_c8opbM7Vd1-6EGfEIXDltfhpaGY3J85M72plFW7kvMA6-aShK8xvAqV8fJEXXwoLRKxrpgPjKwF0DQ15kWcFkGsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRfz1GyF4FoZEp-7Ae-bpo_9WfkylGTph8UiDvRmtug1UXhCDER12m8AVQNnDT9BC-5nbhPgIleebDqCvwyufVBrS0QdPtrgoKdziPpwVrA-CBEVdVhnr8UbbrZwieP0C3Vczo3n2owhA4ZajDnlJrSVQwqL2YXQJXybEPMWoGDikMkwpaMieRs-EnijncvvoTBnMlrY3ioHoylyp4olZ8dBnQIYsMKKDHbjFnk0V4i2BWiaoBb8G59k7S9aEVIcoJ_kjXh3BMhGYifar0cq22elcccpdf-c0tLh9YaBEPiTil5_g0lOL_bh-DV9q-EESVXZYIceNHcUboX8-qK-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZNTLeSEWn5MIYhB5HkOGoCKK7FftEBruE_jPUS85tPvtiZX9EijwktttPPhQXjm9v4y-zWYDFIaKJKD9kJNqH2yQ8MQz5jTTG-QfhzA4CYe_Y9a40DGG2Rl7dzjarv2cTrI5WDUK0dkkvSWEoJtNVlja1CWHamfngROZue--id34kY5fT2oEsYvFSBCMPfGv5Q2BVFNAZnwzCjyaM-tC--ElHYAKIanPqUCwZ7j6iOzAm-G1C_a0iU1Ppi3AnwQ-F5ORWuAtcyPc6-2NxVaweMY7AEdrbz0hsv0r1P4ESef6ipwbf9IXH4GBIVNvyUwfA16lWpSPWkwwfqKUqCz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETcyCx1Q0WgJNhoK8wye7vIgXr9TRlw84zFhaq-UueSN0TwcCWz2tkcNa4oRB6-ezfWrl8YzJTwjJGqwPEDZ_V3pjU5niLuPctTEgsZtPuP97f9t_Jjn0-JxazRUsXXVT0eAbMt84BA4nfUcP7FV1WKZwb7vHOVSpt3Zlhcn3fk_vieWG7_pH9AlqkC99kNzkJE59c3LgKzvhueILI5_pBt1ojLO1k1oGVgCjoHtesMRVqnQ-AcrFZ3eRwpVQ9WCJBdxONeMHl8yQjIyn1XMJmKUUkXvMyIyq6todZsslU6cFSQGGoIYIDqBcGN9QHylHVYQxe6Id-7wFVKpU5Ce9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gngDuSqmnw0sxXbGJkNJ0jg5FA4eCx5krxcMQcfLGmZlNsMxPu9Lq-S2uatkzPRCI-AC8itrSvQMMIqYscmvsYCJMHfR1QBjsQBCx7Qxsu2p1GwHBYPTpRgJ1PTKoiyfcXNaOSBAgaSLSHZGCAxByKP5xsbH4nqUH0zgHEz1kVVjCO9NIKzrm8-Wwh_YdRll9tk402PyEv0S8ClRzwIjCTolP3MVSYkS-3ACZPscCxCgTIKk6HxYB7ZUSQEKFHb4WmgviVK_oGFrXAUNtolE76NQRyAa3iAERtXa7jgEhICxcxMgE75p_BVEnyxH7-qFlytWGzcLsulpJCIh_8hUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PNmQrO4R9gfkWFOg7fB2cU-9ZsUysm-244W6MeOl6jDj3HVLKASFOJU3un4NHoxclm2d8av471s2-R1paw20A82zgBWSJqbLUaTJa7Q0lONgy8BQzwuN_hNoYbiDq5coLJ5JceF-nLeiyJemAhT8qnpQ3E0nUHMQx15ttFqDyCh8REbQgG3TSHTr7O6l36RIjm5PaLGQq59vmSwIdAauvlbQ-ZQKdC11hkC6xr7IY0vFQiIzE5z41LI62NlNNnK-9MRP0AAbiwixal3bMRZaonb-J48oxWPj1_xx75dn0IT1ybBBCuixKET4OAQ26D8NvtLLqE2BEP962g5zvvzqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekgCJsBMljAYM-MfelpSP7ZRmsKRmVo5KZT2uKdGpMxe5gbeyMmr5t_0XU_44njEk6ISihJ22bhXFCWeLBuuRUMqlS80LZZesWg2_ZCm8uYqIDKKZJjqaEgVqDSF7XUHftwWpuy6LoZewKCo1TE-ZH1s_7pS-GtwtBmvsmsd1MU4oiwoe5yhcz5nuoY1wP2YfY_T8bL00G28AMCQ7vVLUh_Ol3codOW6VClk-hH-1r-lD3shlVal-QWI1SVEJZbPF98MrBwr0-uDYPtyAOqL42dhL3nXBc1sFjWIqncWSJ5KMFCVPpvQhe8EGbF-1xB7qM735IksHrH3pp7Eb8V6yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از آثار تجاوز آمریکایی صهیونیستی به واحد های صنعتی تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/akhbarefori/653945" target="_blank">📅 08:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653944">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b82ad759b.mp4?token=kU8qT7plBsAeZFdj8ngkAna2Zcmqbkl8G_vVPeewkkYlFXGICxN406E1GfXNecAKTzsFSV-ExnNNjkinENUF1nzLVph8jWFPbunEzTiCePEUwnmiHZ7lJvv8LNe-VPHtrgcxIh3QJ7wALHKTMtWrrfAj0ntYuU_jislJ_lsDUpOUIvRIHWvIr6RtlholDRum7nHH-WcR1LE3xgdspSy4Hw5Hso17PLJbPL16qF8Hf6voH3tw6n7-0FSl8r3U53wBmuOfeh2lF4Q6D3DpH4OSI394I39sPLD5YspKgRnLf2k8JMe57cwcnx0b0YTuFKropGMP48ueWiJFLWOb_nwWMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b82ad759b.mp4?token=kU8qT7plBsAeZFdj8ngkAna2Zcmqbkl8G_vVPeewkkYlFXGICxN406E1GfXNecAKTzsFSV-ExnNNjkinENUF1nzLVph8jWFPbunEzTiCePEUwnmiHZ7lJvv8LNe-VPHtrgcxIh3QJ7wALHKTMtWrrfAj0ntYuU_jislJ_lsDUpOUIvRIHWvIr6RtlholDRum7nHH-WcR1LE3xgdspSy4Hw5Hso17PLJbPL16qF8Hf6voH3tw6n7-0FSl8r3U53wBmuOfeh2lF4Q6D3DpH4OSI394I39sPLD5YspKgRnLf2k8JMe57cwcnx0b0YTuFKropGMP48ueWiJFLWOb_nwWMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ قابل توجه تحلیلگر بی‌بی‌سی به مجری این شبکه که قصد داشت مقصر جنگ را ایران نشان دهد: نمی‌توان انکار کرد که هر دو جنگ اخیر را آمریکا و اسرائیل شروع کردند و آنها بودند که به ایران حمله کردند، گروه‌هایی مثل پهلوی و طرفدارانش هم از این جنگ حمایت کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/akhbarefori/653944" target="_blank">📅 08:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653943">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKyZcwLf-sgKZpXtK14FKRUp9LMalADuFl0BLb3h7m4_8dT9W67wx73bx6t3yMYJWDyfmVFHcLNqHyy3LuHKGhYOk3P-5qDBK_60YD8Qu6pcMgFX4w9F_N3_s1M7mtrLxqBBLlVBw8fOdgB2tb0QNpVlgc85GwwkG-V_o7L6aD1SymVkD3mZ-MPk96h0EVcRMk61V1CJDRflkt-10-HNyKBewQ3X-BcSOMKj_GX6N8c3GXyzJ9gJQgKx9n3MaQdPp-Zku-vPSq7sXt052z3_ZSwAHrCHCz6BthVfGrvcOpqw8bCNgFYVqJETXICDYhzOHYv_5cjBpF-w2mX3W9f-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العربیه: ترامپ به ایران ۷ روز فرصت داده تا توافق را نهایی کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/653943" target="_blank">📅 08:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653942">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw5m0VeWCLN5J9VKh88vIZ6tLRbAqYY-BoaQjYhQIFYxcycjmlFvVqsJGA3tLfdjd4YQKDbw2FEdTGN-ka8NW6h_dErknYqbT1KoEfbLD03yeLqRtELotTLG82f4-yXq-BgWr4s7x_MZtHZ5JoOzD_p3E3hDplv8mp1A7yFPC0eOmONRYLSx4lyBYIQf8Gu9L9TItdpRevAxo7hf33bUN0VXTYlzZ83UiOwPdbTDwuu6VG2IUVhbmlaR6gUzCtPOeSs-s2RY-ccW75xDqdx0VhhZTrAeU3EHFsjY_QkRABX9E5tbzGKkq3jjy9cgrAJ2sGIJxTdt1oEIb-LG_vRisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ رئیس کمیسیون امنیت ملی به تهدید اتمی ترامپ: قابلی نداشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/akhbarefori/653942" target="_blank">📅 08:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653941">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2a076d66.mp4?token=vjc9q8SHkp7fwcBArjafmlaL6bFZxnK6QEFJ_GRA23xIda2t8r-rPTvj7KmG45YZYpiLGytvtm17N9nXFwr4uQH7ByaX2oXJoOJ7k3yqV7U6NvtrzQ47QEGrexJY1E-6cmCg3qYpJ0tk34yrTjKWJyynv2CAWT2AoFd8cw4l69vEL0aNJpiylUmTGHyEA2dsR-lVaTXPeb41ECQv5SCQngf2L1tTZ15eh_NjLySAZ202HJSkp8A_xxFxSAoj2OvUu1AP3uXLfxWtjHKO87MPlPTs7oILCgD_bQVkMLxgFzULcolKGCAQI0iuGCAzAsU_TtpSw1x2_OOy8MQlEZMWpm96Utq1kPT8fV1_1FXSlrJnzrJ_d2GQzMSwnJkCAvCgPhSYBzh_5nyT5wuOz4RcAe0J6a97e-jA19TZqcM_qEkXpgPAocmVqcNw8_ZXzaRIO86gJ-NC2XAbDmrzIW5WV73SMB5-zFUFlGyaZmQTNQGHLHCa069_-WwqkZq6M59xqJW53CLDw7vYeaO0j_qC2bULKKhDpxFNs7F_pycqn6LFF8FEYDUQvZ9Gw6M7p7ZEnjYc8wPGy1olT55WbhVoUNelPoOhqtu8vPaJIRLTfv1DvFMSKl-bitrYa4ieI9tHne6jsF2lb9r59EkJRiAhferMlMPd8dwD4NHpp8p8L3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2a076d66.mp4?token=vjc9q8SHkp7fwcBArjafmlaL6bFZxnK6QEFJ_GRA23xIda2t8r-rPTvj7KmG45YZYpiLGytvtm17N9nXFwr4uQH7ByaX2oXJoOJ7k3yqV7U6NvtrzQ47QEGrexJY1E-6cmCg3qYpJ0tk34yrTjKWJyynv2CAWT2AoFd8cw4l69vEL0aNJpiylUmTGHyEA2dsR-lVaTXPeb41ECQv5SCQngf2L1tTZ15eh_NjLySAZ202HJSkp8A_xxFxSAoj2OvUu1AP3uXLfxWtjHKO87MPlPTs7oILCgD_bQVkMLxgFzULcolKGCAQI0iuGCAzAsU_TtpSw1x2_OOy8MQlEZMWpm96Utq1kPT8fV1_1FXSlrJnzrJ_d2GQzMSwnJkCAvCgPhSYBzh_5nyT5wuOz4RcAe0J6a97e-jA19TZqcM_qEkXpgPAocmVqcNw8_ZXzaRIO86gJ-NC2XAbDmrzIW5WV73SMB5-zFUFlGyaZmQTNQGHLHCa069_-WwqkZq6M59xqJW53CLDw7vYeaO0j_qC2bULKKhDpxFNs7F_pycqn6LFF8FEYDUQvZ9Gw6M7p7ZEnjYc8wPGy1olT55WbhVoUNelPoOhqtu8vPaJIRLTfv1DvFMSKl-bitrYa4ieI9tHne6jsF2lb9r59EkJRiAhferMlMPd8dwD4NHpp8p8L3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر محمد مصدق، معمارِ استقلال نفت
#پادکست_کافئین
| قسمت بیست‌و‌پنجم
☕️
در این اپیزود به سراغِ مردی رفتیم که میز بازیِ یکی از بزرگترین امپراتوری‌های تاریخ را به هم ریخت. پیرمردی با اراده‌ای پولادین که در برابرِ انحصارِ مطلقِ بریتانیا ایستاد و غولِ استعمار را در دادگاهِ بین‌المللی لاهه زمین‌گیر کرد.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtube.com/@caffeinepodcast2025?si=CNnq-Y7JNjOTm0Z_
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/akhbarefori/653941" target="_blank">📅 07:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653940">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست پنجم | پادکست کافئین</div>
  <div class="tg-doc-extra">دکتر مصدق</div>
</div>
<a href="https://t.me/akhbarefori/653940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
دکتر محمد مصدق
🗓
وقتی تصمیم می‌گیریم مستقل باشیم و حقمان را از یک سیستمِ انحصارگر پس بگیریم، چگونه باید برای فشارهای ناجوانمردانه آماده شویم و چرا در این مسیر، بزرگترین خطر نه از جانبِ رقیبِ بیرونی، بلکه از سوی «موریانه‌های درونِ تیم» است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/akhbarefori/653940" target="_blank">📅 07:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653939">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggFpQ8otwjVeLLw5ULryxvQ-vrOF02EmntEjUe2KclaDyPUrUksuWw0hgapZbIVCtytBHM70O_42Lf9Lc_ipJvn5-8ZFEBs9YLfB9laJZVSQ78pvRFbu7LKx-hcv88mj6TSxOTNWCDQgzhLJSoRmGEgCo3A4FfX_tf-yl4wowFSQxmdzlzi2wTVmcldxjxIztm9luiJwQBZxO2_7vkTSlEmznfTliLl2d1FvNmr8c2A0rDUJaq7C3ijkj3OHLeaFlmQDu5zJ5HMCKojsGPOpPoVTzGfgahFyKGl_yZcOTo3Ir4ud-Y5KJvB-mWhig3h34XCv9JDRf35ZbXA1tRo5Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام آمریکایی: نهایی شدن توافق با ایران چند روز طول می‌کشد
🔹
در پی انتشار برخی گزارش‌ها در رسانه‌ها مبنی بر حصول توافق بین ایران و آمریکا، گزارش کرد که نهایی شدن یادداشت تفاهم میان ایالات متحده و ایران ممکن است چند روز دیگر به طول بیانجامد.
🔹
او دلیل این امر را فرایند طولانی کسب تأییدیه ایران برای متن توافق عنوان کرد.
🔹
بر اساس گزارش، انتظار می‌رود پس از حصول توافق نهایی همه طرف‌ها، مراسم امضای حضوری میان مقامات آمریکایی و ایرانی برگزار شود و بلافاصله پس از آن، احتمالاً دور جدیدی از مذاکرات بر سر مرحله بعدی توافق آغاز شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/akhbarefori/653939" target="_blank">📅 07:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653938">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سدهای کشور تنها ۶۷ درصد آب دارند
🔹
میزان پرشدگی سدهای مهم کشور ۶۶ درصد است اما پنج سد لار، دوستی، پانزده خرداد، بارزو و ساوه کمتر از ۱۰ درصد آب دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/akhbarefori/653938" target="_blank">📅 07:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653937">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN4BYlLdssdp0jyZa0jzFSPrUnj6_BR93OMZ9Y53chv1kxqlEHJgxvEoSExceKiGFNOgWu4y0QIY8e5SO32hjRogNb03i5Z0N2sS2r7uo8hLJxXZW5ZpfT52ebZLLX5EWhYuAg7EKvhQtYN_POJ-BdzDxgc--0FX3Msx7cHgaKmh9QC76YpAmHWdJ0lj-j7XppXkoDqdi-SFtPZZJBjXUkX3rN-NRPnza-mf5PrIVCpk_vrgYLmwS7UPBgi4_Vf6v3Zcxyw592ETMAFzSxJnvu0vj_-YAXHVaOB8_MtOYrE-urYnOI86ydYBtKgPYerptueg67U63mULVQKj8sk9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۴ خرداد ماه
۸ ذی‌الحجه ‌‌۱۴۴۷
۲۵ می ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/akhbarefori/653937" target="_blank">📅 07:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653936">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcpPZ-rzr7DPKGe5_J7-C2onbA_0JSCP2eJnihxM4qFGcHseqUBpAS4LntVgHODodKhgEXno5JbFEgd8QuqEjie_tYkFvCmvOl78O7FP4TUZTDE4e4f9UlQva5UXEAGHCbxfXpiUi8EeGBVcqu3US-TxvDWLWJVqTsZwE-ECUJNUAqX1HMIpf3SuoQXiSq-9zJ7O_voJVVahG8s73iGEbXSNQJhuT4Aznc5fo-xN1SoDFQg_hd_mJQEwuGKrrgHupL4-yR49BxcBCyJGeYsldZ4iW7EQWUjfvhUemuSaNPFaOGsW2nD_KnvhfM7tFGBAWd0UGllMFLOaOFwadjOhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان ثبت‌نام‌های مشکوک در قرعه‌کشی خودرو، با ورود دادستانی
🔹
پس از تکرار گلایه‌های مردمی مبنی بر اختلال‌های مکرر و تکمیل‌ظرفیت برق‌آسای سامانۀ ثبت‌نام خودرو، دادستانی تهرام ضمن صدور دستور قضایی برای رفع این مشکلات، خودروسازان را مکلف به برقراری عدالت در عرضه و بازگشت به سازوکار قرعه‌کشی در صورت تداوم شرایط نابرابر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/653936" target="_blank">📅 06:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653935">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
فاکس‌نیوز مدعی «پیشرفت ۹۵ درصدی تفاهم اولیه بین ایران و آمریکا» شد
🔹
شبکه آمریکایی فاکس‌نیوز مدعی شد که تفاهم اولیه درباره حدود ۹۵ درصد مفاد یک توافق‌نامه حاصل شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/akhbarefori/653935" target="_blank">📅 05:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653934">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سردار نقدی: عملیات براندازی به عملیات تحکیم نظام تبدیل شد
🔹
مشاور عالی فرمانده کل سپاه پاسداران با بیان اینکه ملت ایران بزرگ‌ترین پیروزی‌ها را به دست آوردند گفت: با وجود تغییر مداوم راهبرد و تمرکز بر ترورها، دشمن در دستیابی به اهداف خود ناکام ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/akhbarefori/653934" target="_blank">📅 04:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653933">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
خشم شهرک‌نشینان شمال فلسطین اشغالی از رها شدن در برابر حزب‌الله
🔹
ساکنان و مسئولان محلی در شهرک «کریات شمونه» و دیگر مناطق شمال فلسطین اشغالی با ابراز خشم از عملکرد ارتش رژیم و کابیته نتانیاهو، اعلام کردند فرماندهان صهیونیست در جبهه شمال، نیروهای خود را در برابر حزب‌الله «رها کرده‌اند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/653933" target="_blank">📅 04:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653931">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riRY3FxvNsNzcMlsJv_9UveZ5Vjsu8-me7brKA7pSXLK8MdWLLIOgyj5KJahchQ4hf9bx0YzqZC6NGNbNwQQE0HJyKQ0ZU97IFsSlk7OzyVmNlg15RJqVCPCXqOF8Q3Hxjp4itWK-fVCBJDYZL8-yUTUfNrpvBvT36s978CBBjbqPhLaHt81iA9jqPR5O3isjKJixDKyNJ_QzhifPrbRTMw3DDRujEYz-EpOzqHhE1f6UxNhMJ5_BOV3flA36N-u6wLJSbiquzA27wJxlK4CnLbyO-yNI_S8YHBnYgcuX-gxFiSZBJm2gbeOISQMoblyNQDdVAJ7CW1yqnaoHA5n6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز: شوک عرضه ناشی از جنگ ایران، تولید در آسیا را برهم زده است
🔹
کمبود نفتا، یک ماده مشتق شده از نفت، که مستقیما ناشی از محاصره نظامی تنگه هرمز است، زنجیره‌های تامین در شرق آسیا را به شدت مختل کرده است.
🔹
ژاپن و کره جنوبی که به شدت به واردات نفتا از کشورهای حاشیه خلیج فارس (به ویژه قطر و کویت) وابسته هستند، حالا با قطع کامل صادرات از این منطقه روبرو شده‌اند.
🔹
بیش از ۸۰ درصد از خطوط سنتی تامین نفتای ژاپن به یکباره مسدود شده است. شرکت‌های بزرگ مواد غذایی مانند کالبی (تولیدکننده تنقلات) و کاگومه (تولیدکننده سس گوجه‌ فرنگی) مجبور شده‌اند طرح بسته‌ بندی محصولات خود را تغییر دهند و برای صرفه‌‌جویی در جوهر، رنگ‌ها را حذف کنند که نتیجه آن بسته‌ بندی‌هایی با طرح‌های محو و کم‌رنگ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653931" target="_blank">📅 02:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653930">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10f1b43b4.mp4?token=uuVHimZtEVLXhstlv0mHE1416UnR0fgqn53ODh-LN3Y_U-oXwtXFsk-hg_gMArm5qoKP6afX6Z70NfXKquCC-MDJ-rfxAopxchniQVs22i5abNen-8aqm_bDOCD6XkaSz9FopkAUOy8OB_hf5uokCgxd589RktDVk94QHG9pgegbJHWhpqiUXR3T-QSJRqPUy3ctSBgO7P7cz0IxqaXj1KMVj8H0Q5TaJu189pb79j-bu23R_XmX9RPXM3Wudjw0yMHNF_YNXBUHcXjQw2mRDgqJ2HRd8269DlDCxGK28R6dTuvNwy4ksmJpbyKvUf3dDL9_D9Kq1SitDIwr3-0x-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10f1b43b4.mp4?token=uuVHimZtEVLXhstlv0mHE1416UnR0fgqn53ODh-LN3Y_U-oXwtXFsk-hg_gMArm5qoKP6afX6Z70NfXKquCC-MDJ-rfxAopxchniQVs22i5abNen-8aqm_bDOCD6XkaSz9FopkAUOy8OB_hf5uokCgxd589RktDVk94QHG9pgegbJHWhpqiUXR3T-QSJRqPUy3ctSBgO7P7cz0IxqaXj1KMVj8H0Q5TaJu189pb79j-bu23R_XmX9RPXM3Wudjw0yMHNF_YNXBUHcXjQw2mRDgqJ2HRd8269DlDCxGK28R6dTuvNwy4ksmJpbyKvUf3dDL9_D9Kq1SitDIwr3-0x-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت دکتر کلاینمن، پزشک آمریکایی و عضو ائتلاف پزشکان علیه نسل‌کشی از رفتار وحشیانه رژیم صهیونیستی با اسرای ناوگان صمود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653930" target="_blank">📅 00:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653929">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c25a3cd81.mp4?token=doxA5ZQWCsA0Jl1EMALiSkiuczKd_xwTPVZ2zfmo-ZJBhgLcl7OcUhpEvHQdL45neIhu299icJMJHmkjZEIEzv52cX5gT2B3CuaG09C4ntV1X0cmkGiXx_leh3pTkGZwsvsYnN1XxxDRZG3WmjCSOXDTnV9nYumR9Qasdh37g1fNRV5xbgaj4b1P-yYlPNhqenHiij7xIBDTGzwxjIsdn0xmJ8_u0eV2Wso5mCQHVywo0meTT_lmy_b6sKj977CZc-jSnKsD6Ch-ns-mwsIiDe3sBEIWl00uwA58KN3qxESivmzk9oIS5cheihSY1Nmp1Cg2TVj981EU4VAy_Uq6vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c25a3cd81.mp4?token=doxA5ZQWCsA0Jl1EMALiSkiuczKd_xwTPVZ2zfmo-ZJBhgLcl7OcUhpEvHQdL45neIhu299icJMJHmkjZEIEzv52cX5gT2B3CuaG09C4ntV1X0cmkGiXx_leh3pTkGZwsvsYnN1XxxDRZG3WmjCSOXDTnV9nYumR9Qasdh37g1fNRV5xbgaj4b1P-yYlPNhqenHiij7xIBDTGzwxjIsdn0xmJ8_u0eV2Wso5mCQHVywo0meTT_lmy_b6sKj977CZc-jSnKsD6Ch-ns-mwsIiDe3sBEIWl00uwA58KN3qxESivmzk9oIS5cheihSY1Nmp1Cg2TVj981EU4VAy_Uq6vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوش‌چشم، تحلیلگر مسائل راهبردی: تا پول بلوکه‌شدهٔ ایران آزاد نشود، هیچ تفاهم اولیه‌ای با آمریکا در کار نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653929" target="_blank">📅 00:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653928">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پست جنگ طلبانه ترامپ در فضای مجازی
🔹
رئیس‌جمهور تروریست آمریکا در ادامه مواضع ضد و نقیض خود، بار دیگر پستی جنگ‌طلبانه در فضای مجازی منتشر کرد؛ در این پست، تصویر بمب در زیر هواپیما به چشم می‌خورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/653928" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653927">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob3e99Ix6edlTt2-zpozgQRpRWfRBojZ2FGcLVFlU6UUPl96w0y3i8qLr9l_SfsTW-9-H2szP-Y-uKojhsWihIQlFS4cbvlPOFjRMaskqDiYf9MZY4im_yiBKftN6puGMP4sGFtK0x-KR68Cuoy25amCbwOaPFhmvjJGmwlRzjfyyYfw23fdUwmHE5j1h2DWOVO-aXBNtItVTXLGdtSd7vNtLXqf1QEXYhoo_xZY8djN7cWLNJpX3PdYu5fHQrwaQOW3xSuq_V3keMRJyulcLnr-sG7OX_m-n4n5eXmANayjJlmv9xzOnHFOs4vai62jcX2UqTWRqpjMV6SMRIfhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور آمریکایی: ایران کنترل تنگه هرمز را حفظ خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/653927" target="_blank">📅 00:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653926">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
آمریکا با انتقال اموال بلوکه شده ایران در قطر مخالفت کرد
🔹
«سید رضا صدر الحسینی»، تحلیلگر مسائل سیاسی در گفت‌وگو با شبکه المیادین: آمریکایی‌ها روز یکشنبه مانعی در برابر انتقال ۱۲ میلیارد از اموال بلوکه شده ایران در قطر از طریق مسکو به ایران ایجاد کردند.
🔹
آمریکایی‌ها تعهد خود را امروز نقض کردند و شرط گذاشتند که این اموال با پیشرفت مذاکرات با ایران منتقل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/653926" target="_blank">📅 00:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653925">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: سلاح در دست ما می‌ماند؛ ایران از جنگ سربلند خارج می‌شود
🔹
۴ متهم پرونده شهادت آرمان علی‌وردی به اعدام محکوم شدند
🔹
بازتاب روزانه جنگ علیه ایران در رسانه‌های جهان
🔹
موحدی‌آزاد: در تمام دنیا مجازات جاسوسی در شرایط جنگی سنگین است
🔹
رضایی: امروز ارتش آمریکا در مواجهه با ایران به بن‌بست رسیده است
🔹
عبور ۳۳ فروند کشتی طی شبانه روز گذشته با مجوز نیروی دریایی سپاه
🔹
ابهام در مسیر توافق؛ روایت‌سازی واشنگتن و واقعیت مذاکرات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/653925" target="_blank">📅 23:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653924">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
۲۸ عملیات حزب‌الله از بامداد امروز علیه صهیونیست‌ها
🔹
حزب‌الله طی ۲۸ عملیات خود از بامداد امروز تا به الان از هدف گرفتن محل تجمع نظامیان صهیونیست و مراکز تازه‌تأسیس فرماندهی در مناطق جنوبی لبنان و نیز مقابله با جنگنده و پهپادهای اسرائیلی خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/653924" target="_blank">📅 23:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653923">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b9d939e3.mp4?token=E3mJPRhKL3XzmZYcvLEFWIhEBk1r_tVfWLon83jwYNgEddIjXpPm6hV-e9GV6JOUotzPKMWg7yg6js-jtkSNHvoBzb48TkrVJvjZdiq_ZeylArlT05cs7W0FfBs8vzpxdGIDPkbb3bUvi__sy-VA-K3PPrmH49NJkbvmMuBIF1KH_6ZdvQV8sItd5cqka4YL1kxQxxeeXKARvoexgR0eyHaBL0Eo789a94O8_0oqRU73EjPw5oD2E2vlrj90F7t4fXJ_F6WV7Qf4_YHWJmI2qqGo_shaU7J-F68Z8Qn0NdL5D5BXNjw2nz5PN_l_lgKKoR-QAXUmZIya_jRrss6eIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b9d939e3.mp4?token=E3mJPRhKL3XzmZYcvLEFWIhEBk1r_tVfWLon83jwYNgEddIjXpPm6hV-e9GV6JOUotzPKMWg7yg6js-jtkSNHvoBzb48TkrVJvjZdiq_ZeylArlT05cs7W0FfBs8vzpxdGIDPkbb3bUvi__sy-VA-K3PPrmH49NJkbvmMuBIF1KH_6ZdvQV8sItd5cqka4YL1kxQxxeeXKARvoexgR0eyHaBL0Eo789a94O8_0oqRU73EjPw5oD2E2vlrj90F7t4fXJ_F6WV7Qf4_YHWJmI2qqGo_shaU7J-F68Z8Qn0NdL5D5BXNjw2nz5PN_l_lgKKoR-QAXUmZIya_jRrss6eIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت شکست آمریکا مقابله‌ی مردم با تمام توان بود
🔹
سردار نقدی: همه نیروهای مردمی با هر سلاحی که در دست داشتند به هوابردهای آمریکایی شلیک می‌کردند. ژنرال آمریکایی در گزارشش گفته است «ما از همه طرف محاصره شده بودیم و هرکس با کوچک‌ترین سلاحی به ما شلیک می‌کرد.»
🔹
علت شکست آمریکا این بود که مردم با تمام توان مقابله کردند و ذهنیت غلطی که می‌گفت «ایرانی‌ها منتظر نجات از سوی آمریکا هستند» برای همیشه از بین رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/653923" target="_blank">📅 23:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653922">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353232745a.mp4?token=hc2bn7PJngdOK8SsNMtkZwsrvS1yDu9rvQFNz5QYmaEOhPHclTK8U5BHbws0RTYVpo1zvwbrlx241e2LrflU7S6w4EiclwvGISwZ30rueVt3JiC7vbfJfTq9VmdXpe9dIczE06kLkf89VC17B123BUwELTodAm28bYwNijE370sibzPavc8v7lHB2tZY5shL2NmMlC7VITShDi8uME7b-hU-POMjMuFfWMT_jWvcv3P6iTPtZrSsCOGjc0kwa51z5s5yJvp2K_M8dWek0ydEZXVdbjsMOSKHv5uCnuL5zv9d5bjU1hVVUSmkj3BM9y9U2AvSmJWHZhpJs4Vsl7IJyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353232745a.mp4?token=hc2bn7PJngdOK8SsNMtkZwsrvS1yDu9rvQFNz5QYmaEOhPHclTK8U5BHbws0RTYVpo1zvwbrlx241e2LrflU7S6w4EiclwvGISwZ30rueVt3JiC7vbfJfTq9VmdXpe9dIczE06kLkf89VC17B123BUwELTodAm28bYwNijE370sibzPavc8v7lHB2tZY5shL2NmMlC7VITShDi8uME7b-hU-POMjMuFfWMT_jWvcv3P6iTPtZrSsCOGjc0kwa51z5s5yJvp2K_M8dWek0ydEZXVdbjsMOSKHv5uCnuL5zv9d5bjU1hVVUSmkj3BM9y9U2AvSmJWHZhpJs4Vsl7IJyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: دشمن ۲۱۰۰ پرتابه و ۳۰۰ موشک زمین‌به‌زمین به جزیرهٔ بوموسی شلیک کرد اما رزمندگان ما بدون هیچ ضعفی ایستادگی کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653922" target="_blank">📅 23:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653921">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c1b495ff7.mp4?token=qkzbhp8fluP9seq7BWYzFsKUg5YYlSf2jZOcA087Fqzv2maWlGRxCHilUsDUYqVt73LHNSUz5jOOUvFQ_yjNVRdgUIDRiSAwopbVhon3GLkKvEo9RgHR9kBhrxNSCrGl6T91AAtMXD163DHjLqY5WGu8vHnLT-RqaPsSP_DAkowMFN9-9NM-fEGSgjBFnHqoELT_utoeDMZC6wOz5AdfFzRTbWdKtp_ojaEe0tOtVvDPuUy8qwGb2yTHO1o62-BPNZUkQ7fhjOMsaivdo2ZCrbpzYiI7_jhhEi1SBDlznp0J8qMOmpsBWpf376J_oItUIf3I74dYhX5Y_Sy8PYm4Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c1b495ff7.mp4?token=qkzbhp8fluP9seq7BWYzFsKUg5YYlSf2jZOcA087Fqzv2maWlGRxCHilUsDUYqVt73LHNSUz5jOOUvFQ_yjNVRdgUIDRiSAwopbVhon3GLkKvEo9RgHR9kBhrxNSCrGl6T91AAtMXD163DHjLqY5WGu8vHnLT-RqaPsSP_DAkowMFN9-9NM-fEGSgjBFnHqoELT_utoeDMZC6wOz5AdfFzRTbWdKtp_ojaEe0tOtVvDPuUy8qwGb2yTHO1o62-BPNZUkQ7fhjOMsaivdo2ZCrbpzYiI7_jhhEi1SBDlznp0J8qMOmpsBWpf376J_oItUIf3I74dYhX5Y_Sy8PYm4Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه: ۲ هزار و ۱۰۰ پرتابه روی جزیره بوموسی ریختند و نزدیک به ۳۰۰ موشک زمین‌به‌زمین به این جزیره زدند، افراد داخل ناوهای آمریکایی تحت فشار روانی از حملات موشکی بودند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653921" target="_blank">📅 23:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653920">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEuGoMgfzz5DELiHiWKAP5G9jQEhzf5xR53Spe_jU2gru5S2C4kpn4sw-ge2IC9PJVAzmj6e-r3gqsyUAEIaxpVI7TgE0GgSqbYjkJf6fRi-Lo_g3cyW6Uvkgf2U8otJ0CWUZA9aGunAfpjIxOl26XNurbA6DX38TuRjtSVtgm2Bo54G4BkU1j0peRPpnNBwdjKLIlh8_DepLWsDTA-GRrNlQrxBs3DvVKimdUDg3g_b395kjoYKfQji4wiYrstJ2OMXC_rHKiyh6eWpFc-uc6S-Lzb8A57e1BaJLyYlFQH8s7Ip_YAh-MI_m6DhJyGSSoSMEPmMUlkzV-HK--KDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خیلی دور خیلی نزدیک
🔹
از شب گذشته زمزمه‌های رسانه‌ای درباره توافق ایران و آمریکا بر سر یک تفاهم‌نامه با میانجیگری چند کشور به گوش می‌رسد. اعلام محتاطانه ترامپ این گمانه‌زنی را قوت بخشید از دیشب رسانه‌های غربی و داخلی طیف گسترده‌ای از تحلیل‌ها را منتشر کرده‌اند؛ برخی آن را گامی موفق در مسیر دیپلماسی ارزیابی می‌کنند و برخی یا نقد به آن آن را فاقد تضمین‌های لازم می‌دانند. جزئیات تفاهم‌نامه هنوز به طور رسمی اعلام نشده‌است. در این فضای پیچیده آنچه روشن است، ایستادگی مردم پشت وطن و حمایت از تصمیمات مسئولان مربوطه است؛ مردمی که همواره پشتوانه محکمی برای نظام در برابر تحولات منطقه‌ای و بین‌المللی بوده‌اند.
🔹
هفتصدوپنجاه‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/akhbarefori/653920" target="_blank">📅 23:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653919">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj5oxPWnMVJsy1NCg7UH1LodIT2fxjssyyv7898UG_4_TakhiL4_sy4CYdpw65f69bx9SfJyYhuL-kVMjpDNOx1PATEyYPwh7dgfzV5lJ0limUU42QpGEqBqyaSclvsll2qDZbgP8I_onfbOuTz0GSsVsMDw20VIX6w39dlLP5RbUVKhVd38ksJ3bc-8nH_-xVhc4isqsyQDui5mHDLrcP1QDsy-twpS_4Y-jktilzzrqOZdy8aKYF75S45ZUU8YX5HP0bJSSbRufp8mW0OsSMdP2JV1ZNcLlIi30WXsVdnKU9GS_QgbNMBQsvzMWJC8xSdFUICP9zn9QlCsb4QxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پترائوس: آمریکا در مقابل ایران در وضعیت دشواری قرار دارد
🔹
فرمانده پیشین سنتکام: فکر می‌کنم ما در موقعیت دشواری هستیم.
🔹
مقامات ایران می‌دانند که رئیس‌جمهور آمریکا با انتخابات میان‌دوره‌ای روبرو است.
🔹
تشدید بیشتر تنش از سوی آمریکا، موجب خواهد شد زیرساخت‌های حیاتی در کشورهای خلیج فارس که قبلا در طول جنگ آسیب دیده‌اند، بیشتر آسیب ببینند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/akhbarefori/653919" target="_blank">📅 23:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653918">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm5Z3M6gIcxkyCNhfO92LC3dpbnOOLlVYrhjccjiD09QgSc5t1gvnM1xkoueJCQ7mUdv5aHujkn-USazt7Eo7V82akutVX1Nyoc43V38AvQBnybYmGbWnWIL9Y49phQuS5q4gQG9H5nvlA8GjMqZVd1H36AgjW5zKH_2RSDvupt44KDG8vuQHSSnEu2gKGKw4XHIuxjh1tSJhAirTo0Xid5bvSeSENSPPliornSwUQzL0QsIQjLyi14Epcnup6cA31BjcS7sBHMR720dZw-qTh-46-8iqUqfMoV6fqoLPLatuG3zHOlkYx7D0EjniNMReZPAN9xECjcpoXzvUcNC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضایی: اداره تنگه هرمز به وضعیت قبل از جنگ بازنمی‌گردد
🔹
سخنگوی کمیسیون امنیت ملی مجلس با تاکید بر اینکه اداره تنگه هرمز به وضعیت قبل از جنگ باز نخواهد گشت، تصریح کرد که این تنگه تحت مدیریت ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/653918" target="_blank">📅 23:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653917">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4b4de4f2.mp4?token=nSsZk3WW71CmAY8erPCjM1kW_5LYaadCOttdAH9ZPccwAirZUJ2p9Uo7fFtNRQLPn_JeuB1fDlf3utJYYT9gWqm2LKT9PUkrIqzv011w3jQqnrol-aZot_WrWr0cY2EAImCkaf8GHoIZmawL_CCSMKvM5Uwf1w1d2Mc74c4Y-bfvcqzNrXXjcyUEcn-2ypHIRjDGBudjJ9iWoeTLVREB66zNcracqFQuzGNqam2eoUBTbATTit7c0zfVcYmfXPkeriMUQaI8rKUQg2TQqDlGVTrQMAOwQw8gN0oUXZMT4gCjIqzZyo64goK1SrFhBjA0ziO5kGIpDrm_uAYDDAduv1MvMHA1IrbUYXrJRzGT3dCQfMwbZ7z8mpfoLdRhDECUU_yiU-KMoHAw8urIfFszCrltpt8O9WA4ho7K9h026bvXZl7jBUb4-rAvbQH_tVQmfA8USqHL27gseOJNRzeJzeA5fmlBYPyrQRgF49C-hZ3iT6Ia-uR0IWYMLODu3WEnVLVAYXho6_kAGf4AEtA7x5WZi_J0VFlPSswt4ZXvoiiBfupJkYw4GrDQrNTcdQjjQRW3JLAv9p85uu9jemEPC1sabKFwHwE2ttBZlriJJXu_kaS54BLfAj-RIp3AL0FuHZfCR--PG6BX2OsUIX4mT4UG1Rdxuq4o1mNziCQ9DCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4b4de4f2.mp4?token=nSsZk3WW71CmAY8erPCjM1kW_5LYaadCOttdAH9ZPccwAirZUJ2p9Uo7fFtNRQLPn_JeuB1fDlf3utJYYT9gWqm2LKT9PUkrIqzv011w3jQqnrol-aZot_WrWr0cY2EAImCkaf8GHoIZmawL_CCSMKvM5Uwf1w1d2Mc74c4Y-bfvcqzNrXXjcyUEcn-2ypHIRjDGBudjJ9iWoeTLVREB66zNcracqFQuzGNqam2eoUBTbATTit7c0zfVcYmfXPkeriMUQaI8rKUQg2TQqDlGVTrQMAOwQw8gN0oUXZMT4gCjIqzZyo64goK1SrFhBjA0ziO5kGIpDrm_uAYDDAduv1MvMHA1IrbUYXrJRzGT3dCQfMwbZ7z8mpfoLdRhDECUU_yiU-KMoHAw8urIfFszCrltpt8O9WA4ho7K9h026bvXZl7jBUb4-rAvbQH_tVQmfA8USqHL27gseOJNRzeJzeA5fmlBYPyrQRgF49C-hZ3iT6Ia-uR0IWYMLODu3WEnVLVAYXho6_kAGf4AEtA7x5WZi_J0VFlPSswt4ZXvoiiBfupJkYw4GrDQrNTcdQjjQRW3JLAv9p85uu9jemEPC1sabKFwHwE2ttBZlriJJXu_kaS54BLfAj-RIp3AL0FuHZfCR--PG6BX2OsUIX4mT4UG1Rdxuq4o1mNziCQ9DCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: نمی‌توانیم از خون رهبر شهید انقلاب بگذریم/ حتما انتقام خون رهبر انقلاب را می‌گیریم و نمی‌توانیم در خصوص این موضوع حساب و کتاب کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/653917" target="_blank">📅 23:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653916">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بودجه کالابرگ برای همه مردم ۹۶۰ هزار میلیارد تومان اعلام شد
نادرقلی ابراهیمی، عضو کمیسیون محیط زیست مجلس در
#گفتگو
با خبرفوری:
🔹
در قانون برنامه و بودجه ۱۴۰۵ حدود ۹۶۰ همت برای کالابرگ پیش‌بینی کردیم. باتوجه به تغییرات قیمتی باید رقم کالابرگ تغییر پیدا کند.
🔹
در بحث کالابرگ با یازده قلم کالای اساسی نیاز کیلو کالری روزانه هر فرد به میزان ۲۱۰۰ کالری تامین می‌شود، اما متاسفانه حتی آب آشامیدنی و نوشابه را هم در کالابرگ آورده‌اند.
🔹
در سند امنیت غذایی یازده قلم برای کالابرگ شامل تخم مرغ، برنج، شیر، گوشت قرمز، گوشت سفید و ...است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/653916" target="_blank">📅 23:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653915">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTR4AQAbM5PZZMfxO3-CU_MCbsU1AIZ1r8SeSdfBeSGG8o_uXX24iyt-aKMKsy3PXQdQgkABSI91mXyRx33NXMR8XKKWqxXFFBLWhH2F67oPw-h7qgzaed-_lEOKp-usRJ2R7jE8-f_DSB4rQ0Tp2hFTuvxz4dNQ-v94YKwRZBAIyCP1GuzH21MqMnxiPwDX32Jc0JLPlnOb3dR_ERrc91MsmTvSFjP3oXNsPC0ipDkl8KffrgnWGNuKrqrYe88T7d60iQCl2q1pG4oyOMYVTpCUayDEtLNUqSy3r7n6myS6NIEt7txr84FQheV0QO7yHEQhgNhJusjFBUrkFf6BBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوشحالی پسر ترامپ از توافق با ایران/ ترامپ جونیور: منتقدان تا حمله زمینی راضی نمی‌شوند
دونالد ترامپ جونیور با انتشار پستی در ایکس، از توافق هسته‌ای پدرش با ایران دفاع کرد و نوشت:
🔹
«این یک پیروزی بزرگ برای آمریکاست. ما باید افرادی را نادیده بگیریم که تا زمانی که یک حمله زمینی به ایران نشود، راضی نخواهند شد. پدرم قول داد ایران را از داشتن سلاح هسته‌ای باز دارد و این دقیقاً همان چیزی است که او به دست میآورد!!!»/خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/653915" target="_blank">📅 23:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653914">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a88e17fd9.mp4?token=knG0gqTnkv7GJirp9G28mPQRtvVT9NCI5eh7rUPJiX_XXRHRxX6ZhY3BakUOJcyPxhRP5jKewHpZhFpsQxuZ3-Pkz0sX9XCNASjz_PEinWj228ElLBaSmC8DDwj9SPZFVnDGBkRkq0521f2twd0aKi8gdJcCb1FkUcycCZ0ipsXVCT4IoHwOSba_Xcmwu0CuteqhryOhEwrNsQfTtWnjQmb7CMY4bYrzVJy-ZlZtSc0q-8eTYohvL9lki1BQajWsFTHV4dXsTzI4Aezqq1oRSn4Q_oPXGT3-xukvAnYvfp56fS6Kotp8bevmpnHk-hrAlaYl1S0mei7f9rVLrp_EEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a88e17fd9.mp4?token=knG0gqTnkv7GJirp9G28mPQRtvVT9NCI5eh7rUPJiX_XXRHRxX6ZhY3BakUOJcyPxhRP5jKewHpZhFpsQxuZ3-Pkz0sX9XCNASjz_PEinWj228ElLBaSmC8DDwj9SPZFVnDGBkRkq0521f2twd0aKi8gdJcCb1FkUcycCZ0ipsXVCT4IoHwOSba_Xcmwu0CuteqhryOhEwrNsQfTtWnjQmb7CMY4bYrzVJy-ZlZtSc0q-8eTYohvL9lki1BQajWsFTHV4dXsTzI4Aezqq1oRSn4Q_oPXGT3-xukvAnYvfp56fS6Kotp8bevmpnHk-hrAlaYl1S0mei7f9rVLrp_EEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه: ترامپ نمی‌داند خارک اصلا نفت ندارد و مرکز پمپاژ نفت به کشتی‌هاست
🔹
تمام پایگاه‌های نظامی در خارک را بمباران کردند و بطور دائمی بالای سر خارک جنگنده پرواز می‌کرد.
🔹
از ۲۸ اسفند تا ۳ فروردین بر روی راهبرد نفت بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/akhbarefori/653914" target="_blank">📅 23:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653913">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3869eef77.mp4?token=Rvtp6XlHKGbXotZ9e_v_c5zKngfWkG4vOrDyRqHL6IstpIy8P_H9m7BahSiZgIGm6-v3fDsrXqD_JZaO8MCmRl7eRx9MKdj0mmIIsZ__REfW60trtB_8SGZbSw7Adkw8GpCmJIsn6J7YeiJv17u-O7yuODCpuxvmFLf_DUNBZV-_PpJGCqhi4zPQIT2rFUrdtfHuB3Cxnsou8LNiORXVLujHf3MZsF2cRrvML6SVkouXT_bJYlbEI7j_yPcF7B5iwsi7Xe3jB3iMFEbzTt96xjfMFv8SiuKzD2Ly19CscQintlmaKpeazjdZNvHABm-rPGCC0coq8gHZYwhnLEQWrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3869eef77.mp4?token=Rvtp6XlHKGbXotZ9e_v_c5zKngfWkG4vOrDyRqHL6IstpIy8P_H9m7BahSiZgIGm6-v3fDsrXqD_JZaO8MCmRl7eRx9MKdj0mmIIsZ__REfW60trtB_8SGZbSw7Adkw8GpCmJIsn6J7YeiJv17u-O7yuODCpuxvmFLf_DUNBZV-_PpJGCqhi4zPQIT2rFUrdtfHuB3Cxnsou8LNiORXVLujHf3MZsF2cRrvML6SVkouXT_bJYlbEI7j_yPcF7B5iwsi7Xe3jB3iMFEbzTt96xjfMFv8SiuKzD2Ly19CscQintlmaKpeazjdZNvHABm-rPGCC0coq8gHZYwhnLEQWrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه: از ۲۵ اسفند تا اواخر سال بر روی بحث ترورها تمرکز کردند که شکست خوردند
🔹
در ترورهای هوایی کم‌تجربه بودیم.
🔹
نتوانستند برخی از شخصیت‌های مهم را ترور کنند. مثلا اقدام کردند برای ترور فرمانده سپاه اما شکست خوردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/653913" target="_blank">📅 22:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653912">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
دفاع رئیس مجلس نمایندگان آمریکا از توافق ترامپ با ایران
🔹
جانسون، رئیس مجلس نمایندگان آمریکا از حزب جمهوری‌خواه، با ترامپ گفتگو کرده و او را «مصمم مانند روز اول» توصیف کرد. او قول داد که دولت مسئله هسته‌ای را حل کرده و تنگه را بازگشایی خواهد کرد و پیش‌بینی کرد این اقدام باعث تثبیت بازارهای جهانی و کاهش قیمت بنزین در داخل شود./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/653912" target="_blank">📅 22:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653911">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4bf900486.mp4?token=GZ1c46LUXHe6uLGbAsn2P1qxGeTmdNhFdH5dQHJ30mIKcQK1ay5yx-DUuB7qaJhApiMyWejCK8mcLxaCuudN1F92NofvLILQHccvkqJOgL3HafatdLeheoiOAvg8N6ZnC-sZqTG6UZ10QR5E82NYcjdpOwZDWBRCxp_R10E_psecE1F_15LOIVdcAAkerlagnRTlYfbogmHyMIhE4JcGep_8yq4g8mlM7vgz7-aX9XgTdsLuhQ9Yw4qZFjhZx_rwV7YQ4Mrdfim594tQLAyWWY3oGkHGV6rvSXaZbg2uJqWOy0DolzYIYbCfQLcFcuul240gPRUUZSuqcIqiVgA09DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4bf900486.mp4?token=GZ1c46LUXHe6uLGbAsn2P1qxGeTmdNhFdH5dQHJ30mIKcQK1ay5yx-DUuB7qaJhApiMyWejCK8mcLxaCuudN1F92NofvLILQHccvkqJOgL3HafatdLeheoiOAvg8N6ZnC-sZqTG6UZ10QR5E82NYcjdpOwZDWBRCxp_R10E_psecE1F_15LOIVdcAAkerlagnRTlYfbogmHyMIhE4JcGep_8yq4g8mlM7vgz7-aX9XgTdsLuhQ9Yw4qZFjhZx_rwV7YQ4Mrdfim594tQLAyWWY3oGkHGV6rvSXaZbg2uJqWOy0DolzYIYbCfQLcFcuul240gPRUUZSuqcIqiVgA09DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه: از روز ۱۷ اسفند دشمن اقدام به بمباران سنگین نیروی دریایی ارتش و سپاه کرد
🔹
با پدافندهای غیرعامل نیروی دریایی پیش‌بینی شده خیلی از امکانات خود را نگه داشتند.
🔹
۴ ناو امریکایی دچار درگیری‌های داخلی شدند که به اسم آتش‌سوزی وضعیت آن را رد کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/akhbarefori/653911" target="_blank">📅 22:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653910">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDgnRIo8Hy23_noQvTmgFmbOg-sektAR5avk0K0QRLC-uPyGipkjINA05yMMGB6_kD8Zu6OxvRoY5ydpGJtXpFlqmXVt6f3mmM-hZxaUjr3gUCHt-S58QoQtU6t8ZsUNQ-zAckSbPYCViguMr4jZFDsC6ZJQfRgu-gapaQuxKIIBePvycWx229BRo7UVntGKnTDg3VmKyU5fTWYE_5gss7srNEq-vKHc3BWtokPG7-pTrKInzLcfJ5PzBR5uFEtkXHs_GxrHWlW930l7l6Br_IuV5OeFDKD59SI_97DFoaAaQ-oQ13HL7LI2V4zLPUsk8_JBEipKjlgWxbi5cW0V9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا جنگ افروزترین کشور ۵۰ سال اخیر
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/653910" target="_blank">📅 22:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653909">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">روايت جانسوز پدر زينب، دانش آموز مينابى:
" اين لباس هاى سوخته تنها باقيمونده از زينب منه"
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/akhbarefori/653909" target="_blank">📅 22:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653908">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnJIn_HVYB6mAhScr5UD783XVO6GYq8S3_Ng-53coGJju51UoNhaN-EzxDcZL5sELpL948rt2VJXixkJIofnDOEF7-LEhTO9Niz69l6gpiSOi-e8w42oI9LbiI9peWjLm8IGrbucOou3rlZK1bKtdLK_xRcDMaNxgMZ2QwxDJhYlkAMqG4KMEZY2XlzjE9lN2JwntHD5txwMKAKOGwmS8rSUlTPmryq1QJ8mZJvhbpMZ9IQUs2NyBTd83Zp9tpbvdSaccT30_RKbP07SCjX1xgdxyACUx-kKl6w2ZAVwnxgUcZdZc1vjOxfMroNdM3Ce-i9V_5llbp_YN0Wtxn5_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیل: ترامپ با فشار فزاینده‌ای مواجه است که به هر شکل ممکن تنگه هرمز باز شود
🔹
ترامپ در جبهه‌های متعدد با فشار فزاینده‌ای برای اقدام جهت بازگشایی تنگه هرمز، مواجه است، زیرا مردم آمریکا با بالاترین قیمت بنزین در نزدیک به چهار سال گذشته روبه‌رو هستند.
🔹
نظرسنجی‌ها به وضوح بد هستند. قیمت‌های انرژی این هفته افزایش یافته است. واکنش نامطلوب بازار سهام و اوراق قرضه به وضعیت موجود هم شروع شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/akhbarefori/653908" target="_blank">📅 22:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1MDIQ5t9CMGBU7BeIzkkpDnHLRQDKkczckgDiHbX6LUXPnXgNrldxeyIK_nsHoH4oVRR3ctdMRfZhMT5d2bZY5WpZTfbThWjc4BvYK0uQ1hvUkPDG7PiGv57b3gUdzGl1ZAuGinxpRIGUlmNiPvbB9RMjv4_Xs7WxLFaUtG1PrclUhFvpcuAI38a9P2JUwvgjeGH1my86REFjO88CDlhsuUf3plYbTTlF48EleIjdYpa_n0TyJHpyL6FT0vEwAJe1SC1y7CykROsiHMkLYC69V-i4IiLqO6E-p2N1mEDJz26YLfp9ZqrtsktejurYUFB-amBiB9kKnNaWrxeLS89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XM2GSXbQCldwRFG3YULovktZ8NY9mhs1Vb8WJKPjXnKla_No7E4ADGhq5FtxGNMI8AHEYfcakuTeL-PnFF4Vqp-v78opaSHsKKNugQhOb1yMad6aHPIfvS76HaHzP7N5wOGV8rf6fIN8lqdmzyR5OLSKi5caNE__PxNopSwfKfO2T1hwZq2sPG1HyHTmW4SM1JTnKSkdtVyybx29_Kl9ILHAOEsCLQeUFVkYJ6vLAXE8TILpAqwVk0eqdbHM6eOk8LgMzZrH2y03L8g6PbFS5E4d1r5btf2rp-4TNsi9FIIqZWZ6JxSEsGdtjAAZg5GxQ6zGE009YmdGKj5zX8Jbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRDLgVJKQ__OJMtGeoHjK1OJsjW2deans3wtX7ptxdg3htZWxMPv310Wnp5W7DCk7ZVrPMSzDDOY6-faLBMCFZxJzqD8LpD0i2EmzlAZZg6KmEFsjVFBxFomnQDOVHsAT7R-Ox0EOx0NkDxuYJEcFxOkvwORaVdiDTx18BY0WeKUH3k2fL1kJScq8uIojSQLljpq0vzvHP4fSC6K_yUyZLFoZ0dUrrtqm22dNTqrEuk4iH9CJ3-T11vZzrdmf-Byhi0wk5iOVBFgeZTdj36SlO9pXRqfMeyxfVW7W-64f7Og6uHMInDAkBgwMMX1QRjvkNxOT3GorGFMA5QSQNiF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkLBhmEolDY5zDdxpn2186lr1PD5jPUkRnpr3ECjb3n_f0MimHU-YB3tCLF8AHQP4wWv8rMC6GRSfxOT3dYX8itXHT9df6_0nLQj5W48Fp1MYBsfGkj-DWytSZnGho2zMun3FmB0LmM4YBERcD8JPemwJ0mjPldhuZStxfiSwc6YVdK-1xde_XIXrzetAMbV38Pb3fTX85i_Noje-uqqk7-laebYnyblAayz12rah-9ArRTmC6pLUiblvPNPRwllaKJBg3wTGyxRFJ42HjuP3OBXW_xVDSlghMvcuYxNt9NDr6qx_qTpdd4SBZRux-B9OrVfCTTzwP8lJleXxAu1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwkO14wGMlcH8IdDPVO1EWou_gxWONCgR3ywfw_dX_W9IWw4Y2Vo9Cluob5Hq2C070QyQtZ8e-NFp3B9dBWQqvW_ZMH9W7VFKbUWGxt-_lFy4f509WIR5z7CPX-dVXh8W1X9uqU_XpOHg7mW7GsrysMu75U7r5KY-hqf1tNTGXmnUlEsJ94vKoEHNui4MoapVadDerVpjLULI3YRYrGzxwA6flm61JUQ632DZOdiv29WwnutWAFkZFYA49os7tYQOyRuqRVlFR-i3Hgxorob2zDjCMf_4JnQTvIDtUaFE1X4F16gTvhuaKMT4sxqkklQ_c5_nV2QHfPW4O_AhiR9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kItW6ab2SohMmedw2--q0XMulUskzuLusv3Qna0EyZj_2SH7bfGC4nnhmfvH6ZrOk1_Fe9nZczlXFlOP_A53-q4fE6wTpCyWRtZJYy6wO5jSkE2sf9qqQZwj7woolN_4Y_FXkw71OvMgLNzgsE9CqgsNZ1oXxjNZddLosou80NqOt_8qvCNsJ-5d-e1g02G5HiNpBSUbMOlMqY-9AX453S3dAp0Tcx-1vNQWa_YnMyhx3IIYdOF5FN_ANtD-y0Na_Ru810uAknH7KK6vKaVtlFkvtNg6ZjI_CSsD2FgxbgMDuTfgIDT8abC-B4z430ep6Vlj_yP7NWScax5-iRE7wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBTCbV8zo9v-2qZIfXhE0q9WAHCyQaT4yZlXlWkhz0xlFdporVHWNi6m41eATwfxKhBbmnDahr5sp98CkiNRrV70XJ9rje30zgXHsgbwf-_Sh8ssb0CRwkrwrQ-F3cj0GO6QAExYqIsT1is9tsHGnWGHbaGOivuTHq8nZKOmDNFv4NjKECJAWZ7oerpROO2f9W8rFRpvH30ZSAXW1Cyhl_JXsC43vDyqeJXbzd7Ilb_bXwqweG9Heq5JCJppb8I7YJ9N6K-aX8edKkSqlqgG4uU6NWh8KTzjxoXUNKaKCvSmnm-91x6sHg3bXTDPxGT1aRfIX4BaFgqmHd9pNAzRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oY_91s3ALaA_Sg5Z9Yar5Iqp08W9qXd3soNDz8plIb6tuTDnplf8s_HuuKirM-BkaAPNMbUV7DR5AYuN575vELVMXpmrHlKPeGw9AJCWVnxFUyP3ZFDiNrri1pGnck01L1bdsuagENWQIFqj8uVhXXbbc-88cMdCZC3iyYTOcnk0b-Y6p9_W9quQlllPn202LxEUw1maEbPpoW-L2N0eeCgBEZj8OcEb9fwKoMMhCsWFjfrZmXdOqTswK7IeHcRilNvWu-MTjhJOnuhq6vMRzd9iC6XKPCbrByKPPB1MMx4VJN-RWiWw7yvDXzdxroFTaKc8vsfjf6-CQUsiQSgboA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت سهم‌های کوچکِ ماندگار
💫
✨
این روزها،
#همدلی
فقط یک واژه نیست؛
حضور مردمی‌ست که کنار
#هیات_قرار
ایستاده‌اند تا هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی، قدمی برای حمایت از خانواده‌های ایرانی و خانواده‌های حائز صلاحیت بردارند.
همدلی شما، ادامه‌دهنده این راه خیر است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/653900" target="_blank">📅 22:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu39Xq_atCNK93SNrCmfcin2L-nzoCnU6jITH23f4NNhYwxF8uPkeWf37Igje3-xfWLrsL_NOViVDm-AEBVDyMUgFl6rGjNHHoZR4-v_tS4xOiYJzmL0JDwiVTDmgDiQrSNXr0TOIz5XRywoCexkON1k54aP3W3qNMmvBb9stTeY_tqHYzvw-wtG57juizcMGTCHLd8x01WwPnvSBJSMSS-rJl_yZV-yq7cEUbsXVgcC7NiGUdWElRbepHLNGcmEiSVo8lMKIzSsgsUmOyKCnZG9x3iC2PY-lUyRm1F4O1W0Mgy5zs-K-djQGXaY2N82DNNWrn8FI0O7Oe3AofXTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: اگر توافقی شود، دقیقاً برعکس برجام خواهد بود
🔹
دونالد ترامپ با انتشار پیامی در تروث‌سوشال بار دیگر به توافق هسته‌ای پیشین ایران و آمریکا، برجام، حمله کرد و مدعی شد که اگر مذاکرات کنونی نتیجه دهد، توافقی «دقیقاً برعکس» برجام به‌دست خواهد آمد.
🔹
وی با انتقاد از رئیس‌جمهور اسبق آمریکا ادعا کرد: «اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد.»
🔹
این در حالی است که آژانس بین‌المللی انرژی اتمی و حتی نهاد‌های اطلاعاتی آمریکا تأکید کرده‌اند که ایران در تلاش برای تولید سلاح هسته‌ای نبوده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/653899" target="_blank">📅 22:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653898">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a41c67cb6.mp4?token=p1yQL7phinI3VrEriuAVdzQQ5i3mveb7Ymf_YWW0i6pWy1d6e8WlYBqJojF6QuInUIdCgT0tP7pc9Tej3HWjvgb6kz-_FPSMupjwd5289htoAgfHmwRO7-CCIZEVnDgt8osE7p2tjEYxxV8eORP4yeD4b8lQa8V-KI3JFaOGruQ1_JtjDzeY01bsaw5eDtiQnzSXcLSyYEyPblSwLBtjy5Q9samW59Ukv9pQBCLwtQr_XgG2Tf7Cfslq6h-HbhXpL6DdZ5lsesjUb6r_pKasIaJVRPgEy6xUOS25J16bFfRJvu0rXTyX5yNpJg3eLrPcTLEG9n15Cc19BLVQi0BHLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a41c67cb6.mp4?token=p1yQL7phinI3VrEriuAVdzQQ5i3mveb7Ymf_YWW0i6pWy1d6e8WlYBqJojF6QuInUIdCgT0tP7pc9Tej3HWjvgb6kz-_FPSMupjwd5289htoAgfHmwRO7-CCIZEVnDgt8osE7p2tjEYxxV8eORP4yeD4b8lQa8V-KI3JFaOGruQ1_JtjDzeY01bsaw5eDtiQnzSXcLSyYEyPblSwLBtjy5Q9samW59Ukv9pQBCLwtQr_XgG2Tf7Cfslq6h-HbhXpL6DdZ5lsesjUb6r_pKasIaJVRPgEy6xUOS25J16bFfRJvu0rXTyX5yNpJg3eLrPcTLEG9n15Cc19BLVQi0BHLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه: ۲۸۲ نقطه حساس دشمن منهدم شده است و روزانه یک آمبولانس هوایی ۴۰ تخته‌ از امارات و یک ۱۰ تخته از کویت هر روز در کل دوران جنگ مجروحان بدحال را منتقل می‌کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/akhbarefori/653898" target="_blank">📅 22:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653897">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMhUR7Jg2g0l2J-QZwkiPYXnxWetJDAjw2Fv4LAtPCWQh9Iw7LvkA_O8REGu0cTDcRtlxTqRYuidNh4xaWiR00cO-0JMYYRJCezMu8fpTzmj_FQYSxCaxfjcdzEJeuOJG4LhtTC8KtKcTdBAjzAecTG9GkKMHfCTO83M6i0Moi3QfRoj3J9MazAWOYJt7jHMewAa88lwNDCaHaC0jIC2jXA7spi29ZoswhVxDTYr7yzM_PasY6uSdUOT6E8Fx38ftlswAU89YatOBIKeY8dQ3rPLr2NNTZ_1opmfBjt2ZY5ZrMiYvm2P8P0AHiMgmEcBQNLJ4-AZJAvI27tWMRIHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادستان کل کشور: در تمام دنیا مجازات جاسوسی به‌ویژه در شرایط جنگی سنگین است
🔹
آمریکا، اسرائیل و هم‌پیمانانشان با تشدید دشمنی‌های خود زمینه‌ساز رخ دادن جنگ تحمیلی دوم، کودتای دی ماه سال گذشته و جنگ تحمیلی سوم شدند.
🔹
این ایرانی اسلامی است که به پشتوانه مردم، سربلند و با اقتدار در برابر تمامی این حملات، جانانه مقاومت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/akhbarefori/653897" target="_blank">📅 22:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653896">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 56</div>
</div>
<a href="https://t.me/akhbarefori/653896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وششم
رائفی‌پور:
🔹
0:11:25 رسالت حضرت علی(ع) چه بود؟
🔹
0:30:00 چگونگی مسموم کردن حضرت محمد(ص)
🔹
0:43:20 دستور الهی در اطاعت نزدیکان پیامبر از حضرت علی(ع)
🔹
0:59:20 منتخب شدن هارون و فرزندانش توسط خداوند
🔹
1:04:40 دروغ کلید تمام گناهان است
🔹
1:18:00 عظمت و صبر حضرت علی (ع)
🔹
1:20:40 اهمیت انتخاب اسامی فرزندان
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/akhbarefori/653896" target="_blank">📅 22:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653895">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
معرفی قهرمانان کشتی فرنگی توسط حسن رنگرز سرمربی تیم ملی و حمایت‌های مردم/
تابناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/653895" target="_blank">📅 22:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653894">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تلخ‌ترین اتفاق این‌ روزهای موسیقی ایران
🔹
در روزها و ماه‌هایی که تب و تاب خبرهای جنگی بر همه چیز سایه افکنده بود، موسیقی ایران تلخ و شیرین‌های ماندگاری را تجربه کرد.
🔹
برای شما کدام‌شان ماندگار بود؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/akhbarefori/653894" target="_blank">📅 22:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653893">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCxSDl4vEDy3E_QgEei4Xg0ycydkA7HLqRqseVJhTvMyfKKmRHN-pjtoFCa9Md8wCyAEwdsttL3w19K9hUEOJppacsRs3bsgVx9-CvsxTV30s8MdeboR0qCCIpwmd3YIaWWO8HHE2yVCLdy6ewrxoV-60EQ3qHCp-ufGAoQme0vho_oQiKtNscEN5244-FDoCS5PpUSL1JwNj2XmVakDKvILqrUNo4GdbWPVODviSMTN3zMdegfSDzlucKO8IMetxVxqcRJ_4AM6IZsf7M2mUx_fcy2vSVuShtYaIwCKwP5MkpbuvquK7_JLvaDApg7CfbAwJj0cZacXhGYP0Z01sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
تهران را «با هم می‌سازیم»
سخنگوی شهرداری تهران با اشاره به آغاز پروژه بازسازی منازل آسیب‌دیده تهران توسط شهرداری و افزایش درخواست‌های مردمی برای مشارکت در این پروژه از رونمایی سامانه «با هم می‌سازیم» خبر داد.
مردم می‌توانند از طریق مراجعه به آدرس
BAHAMTEHRAN.IR
یا ارسال عدد ۱ به سرشماره ۳۰۰۰۱۱۴۱۱۱ در فرآیند بازسازی تهران کمک کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/653893" target="_blank">📅 22:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653892">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
«خفه شو بچه»؛ جنگ لفظی سناتور کروز با مشاور ترامپ بر سر توافق ایران
نیوزمکس:
🔹
ماجرا از آنجا آغاز شد که کروز توافق احتمالی با ایران را «اشتباهی فاجعه‌بار» خواند و هشدار داد تهران نباید میلیاردها دلار تسهیلات تحریمی دریافت کند و همزمان راه غنی‌سازی را داشته باشد.
🔹
الکس بروزویتز، مشاور ترامپ، در پاسخ نوشت: «هیچکس از تو نپرسیده داداش.» کروز بلافاصله واکنش نشان داد: «خفه شو بچه. بزرگترها حرف می‌زنند. من داداش تو نیستم.»/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/akhbarefori/653892" target="_blank">📅 21:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653891">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93edb5d38.mp4?token=FL2yCo1x7Oto0oSpB4-sj7iljt9af-qamjIQhUdlICGZO337AYgfMDlg57JWv9msds4h2YtX4EjBcdXG_vdTfxDnRGSQWJzWS0n7l1NpsDwNUVw7sPGjErJEm5qGgNWxlbN6oenoQCKp2bKcf7Yn8E6idnw8nu7bSfKAI-xZkdB6Rqa0WanWaI5CElMp0HXoy2m7iPKfgKP2llt7IEZC-MdCVg1iHZABIzx6lrek2Ga8DP7dozdkMjRKW3JW46A7TAdJzwLHYHLOm0v5H6BYSwIxSXkiistj_vv7Ff3ACE7x2B0nBla8Xteokk64wS8sgAkMLakGzY7L4IRkywIU5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93edb5d38.mp4?token=FL2yCo1x7Oto0oSpB4-sj7iljt9af-qamjIQhUdlICGZO337AYgfMDlg57JWv9msds4h2YtX4EjBcdXG_vdTfxDnRGSQWJzWS0n7l1NpsDwNUVw7sPGjErJEm5qGgNWxlbN6oenoQCKp2bKcf7Yn8E6idnw8nu7bSfKAI-xZkdB6Rqa0WanWaI5CElMp0HXoy2m7iPKfgKP2llt7IEZC-MdCVg1iHZABIzx6lrek2Ga8DP7dozdkMjRKW3JW46A7TAdJzwLHYHLOm0v5H6BYSwIxSXkiistj_vv7Ff3ACE7x2B0nBla8Xteokk64wS8sgAkMLakGzY7L4IRkywIU5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر عابدینی، معاون سیاسی رسانه ملی: در یکی از سرخط‌های خبری در خبر ۲۰:۳۰ و ۲۱ به موضوع صرفه‌جویی می‌پردازیم، چراکه کشور در حال جنگ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653891" target="_blank">📅 21:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653889">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
الجزیره: ۲ چالش در مذاکرات ایران و آمریکا وجود دارد
🔹
اولین اختلاف دربارۀ لبنان است؛ آمریکا خواستار آن است که نوشته شود اسرائیل می‌تواند «درصورت وجود تهدید» اقدام کند، اما ایرانی‌ها این متن را رد کرده‌اند.
🔹
درباره دارایی‌های مسدود شده، ایران خواستار آن است که در چارچوب همین تفاهم‌نامه، دارایی‌ها آزاد شوند اما آمریکا اصرار دارد که این اتفاق در یک توافق نهایی رخ دهد.
🔹
انتشار روایت رسانه‌های خارجی به منظور اطلاع مخاطبان است و به معنای تایید ادعای آنها نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653889" target="_blank">📅 21:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653888">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
طلا گران می‌شود یا ارزان؟
کشتی آرای، عضو کمیسیون تخصصی طلا و جواهر اتاق اصناف در
#گفتگو
با خبرفوری:
🔹
بازار جهانی طلا در روزهای شنبه و یکشنبه تعطیل بوده و قیمت جهانی طلا تغییری نداشته است. در بازار داخلی قیمت سکه حدود ۸ میلیون‌ تومان و طلای ۱۸ عیار حدود ۱ میلیون‌ تومان با کاهش همراه بود که به علت کاهش قیمت‌ ارز می‌باشد.
🔹
قیمت‌ ارز با توجه به نشانه‌های صلح و روند مثبت مذاکرات، مقداری واکنش مثبت نشان داده که باعث شده قیمت ارز با کاهش همراه باشد. باتوجه به کاهش قیمت ارز، تقاضا نیز با کاهش همراه بوده.
🔹
روند بازار بستگی به مذاکرات دارد اما غیرقابل پیش‌بینی است. طبیعتا اگر روند به طرف صلح باشد، بازار هم واکنش مثبت دارد.
🔹
باید در نظر گرفت در ماه پیش‌رو، هم حجاج می‌آیند و هم قبل از محرم است و خیلی از خانواده‌ها مراسم دارند و بازار طلا رونق دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653888" target="_blank">📅 21:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653887">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4db43f7f.mp4?token=Iwmt9w5qSUqT3xwwKkQ7KOIjgKkhG8FNimvyz6dOqCesZPFMO8FCXH1-UVyN8gBLKNiNEmWBnhFD0sq3PPna6YH37AQ_l2CHnICNhf3M-0uWBgTCqm5P-OY48voyFkIXMUqYIfWmzY7Amf1IGPfRsUrxIjjEpkJv9V7vZXhJA8c-3KafRKk40HaVAeaGFB-4GxQhtp_3L6NvzALBpiVYYZkrLBMGIFW-I4UoIMAy6My5X6QzKScHt7eE4VijXcnskNrOKQeh5_LoBuqZmSsA5mNRYnAXzAFPz_wzKFoDYMQB5L8KpAlQx_hG4K5RFRsxgEsDBGn6Z-8eqiQyTbYjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4db43f7f.mp4?token=Iwmt9w5qSUqT3xwwKkQ7KOIjgKkhG8FNimvyz6dOqCesZPFMO8FCXH1-UVyN8gBLKNiNEmWBnhFD0sq3PPna6YH37AQ_l2CHnICNhf3M-0uWBgTCqm5P-OY48voyFkIXMUqYIfWmzY7Amf1IGPfRsUrxIjjEpkJv9V7vZXhJA8c-3KafRKk40HaVAeaGFB-4GxQhtp_3L6NvzALBpiVYYZkrLBMGIFW-I4UoIMAy6My5X6QzKScHt7eE4VijXcnskNrOKQeh5_LoBuqZmSsA5mNRYnAXzAFPz_wzKFoDYMQB5L8KpAlQx_hG4K5RFRsxgEsDBGn6Z-8eqiQyTbYjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعدام، عاقبت خائنان به وطن است
🔹
مجتبی کیان، که با لودادن محل ساخت قطعات لانچر موشک‌ها به دشمن صهیونیستی خوش‌خدمتی می‌کرد، به سزای اعمالش رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/akhbarefori/653887" target="_blank">📅 21:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653886">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7722c4f35.mp4?token=vHMdLd6Q3FtW8rHUapOPeAALNO7YwkKaV6n6JmfxDXd1GPzwVgroDQ2_CGtFaKZ05l8qchG90glRDfqd4cFsoZJ4ln6Fz3diUIVSMNiFBmUTC9MvebKwotqndu_ewAxsoG7mFfBWgjViaqHXBm3xccQj5DHMrclSsiXAM4ZJ2V9CM9rJN5qmpRSFDI611O4BD_-ErGYaMYO0G0CHAYMCaWGpAYjkXE6A7IVTUwUbQxemj_qnQKSYwpNfz5NLNglOdGjHyvRnFWbCcyROpy6b5npqz0cEdlJ6lKISicEwdpfpTl1koG6h5Md2Of00PXxw37kDtETAmi3ySzlDfc85Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7722c4f35.mp4?token=vHMdLd6Q3FtW8rHUapOPeAALNO7YwkKaV6n6JmfxDXd1GPzwVgroDQ2_CGtFaKZ05l8qchG90glRDfqd4cFsoZJ4ln6Fz3diUIVSMNiFBmUTC9MvebKwotqndu_ewAxsoG7mFfBWgjViaqHXBm3xccQj5DHMrclSsiXAM4ZJ2V9CM9rJN5qmpRSFDI611O4BD_-ErGYaMYO0G0CHAYMCaWGpAYjkXE6A7IVTUwUbQxemj_qnQKSYwpNfz5NLNglOdGjHyvRnFWbCcyROpy6b5npqz0cEdlJ6lKISicEwdpfpTl1koG6h5Md2Of00PXxw37kDtETAmi3ySzlDfc85Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتظامی: یک عده فکر می‌کردند آمریکا به هر کشوری فوت کند آن کشور نابود می‌شود اما ما هیمنهٔ آمریکا را شکستیم
🔹
معاون وزیر فرهنگ: اسرائیل دولت نیست یک گروه تروریستی است؛ این‌ها از اول فقط ترور انجام می‌داده‌اند و به‌همین‌دلیل سیستم ترور قوی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/akhbarefori/653886" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653885">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
۳ حادثه امنیتی دشوار برای نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری گزارش دادند که طی امروز یکشنبه ۳ حادثه امنیتی دشوار برای نظامیان صهیونیست در جنوب لبنان رخ داده و این امر به خانواده‌هایشان نیز اطلاع داده شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/653885" target="_blank">📅 20:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653884">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
لهستان: از ادامه مسدود بودن تنگه  هرمز رنج میکشیم
🔹
وزیر امور خارجه لهستان: بسیاری از کشورها از بسته شدن تنگه هرمز رنج برده‌اند. امیدوارم  تنگه هرمز باز شود و ما خواستار آزادی دریانوردی برای کشتی‌های حامل سوخت در این تنگه هستیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/akhbarefori/653884" target="_blank">📅 20:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653883">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2261645d3.mp4?token=I89-50B2pqM4aAaMRJF2Zzl2ezxyVDS2Jg-HyJ3K2AwidZ5AGrtZM-f6s_fdlw0jCXvMht7dVZNzccLuJtwvaq4ctcBYTWJgaaamNCnF49D5ynoEkphsKEYh8eQ7751ZXw-WYwwUN3LcbyLppvg177nmvUSMWcWy6GT_bItT43jZjE8CkLut9HdOruosIjkd9gJuHH8NXA8jT7k4m1stwxVkSRvonEdO7chJGJztiTPrPvAbEJjKcIaiJFgg1gs5RoJD3MwAhYUmw2etKFvQ-i_3wxy-8AIei4_Rta6vfL77eFzUOaqYUE8Qcdxx89sG7EEfdzkhThk_avke5yIlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2261645d3.mp4?token=I89-50B2pqM4aAaMRJF2Zzl2ezxyVDS2Jg-HyJ3K2AwidZ5AGrtZM-f6s_fdlw0jCXvMht7dVZNzccLuJtwvaq4ctcBYTWJgaaamNCnF49D5ynoEkphsKEYh8eQ7751ZXw-WYwwUN3LcbyLppvg177nmvUSMWcWy6GT_bItT43jZjE8CkLut9HdOruosIjkd9gJuHH8NXA8jT7k4m1stwxVkSRvonEdO7chJGJztiTPrPvAbEJjKcIaiJFgg1gs5RoJD3MwAhYUmw2etKFvQ-i_3wxy-8AIei4_Rta6vfL77eFzUOaqYUE8Qcdxx89sG7EEfdzkhThk_avke5yIlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محل غیرعادی سکونت یک سوم جمعیت تهران!
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/akhbarefori/653883" target="_blank">📅 20:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653882">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
‏مصادیق جنایات جنگی آمریکا و اسرائیل در حملات هوایی به ⁧ایران⁩ در جنگ تحمیلی سوم به روایت تصویر / فقط در ۴۰ روز!
🔹
‏از کشتار دانشمندان، زنان و کودکان تا حمله به مدارس و مراکز آموزشی، ساختمان‌های مسکونی، دانشگاه‌ها، آمبولانس‌ها و مراکز امدادی هلال‌احمر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/653882" target="_blank">📅 20:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653881">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d90f726e3.mp4?token=BbFhF0KR0jrEPAvEqPU9ixDm5cBIMxStBD56Rt7_NWVla0QjOpRiCF4FVRKSBLddsn19I_obG9COBrqHMtbwBlIPP9BtH6Gluqh28YEFLA-cVnZuuUuUeTQaIbQzCpnp66hdmehPjO5_4A-D6gcFpNnli4GzSDOB134gPhp4BMCXJgWGPIIftF5piUTKFHK5QonfSbLu-GhR8OU2AmTp_6gczIFGg_d4ukzcowsmIVX4pvXQ9G1KAPypv1yt2MX726QsNB1NW44yNqLk4FSUI30JRC7oOZRqSAtJaza8GfgRNqNryUuuRwXY6-VyjVn5FXAAHQu0MHZktM5PPURjTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d90f726e3.mp4?token=BbFhF0KR0jrEPAvEqPU9ixDm5cBIMxStBD56Rt7_NWVla0QjOpRiCF4FVRKSBLddsn19I_obG9COBrqHMtbwBlIPP9BtH6Gluqh28YEFLA-cVnZuuUuUeTQaIbQzCpnp66hdmehPjO5_4A-D6gcFpNnli4GzSDOB134gPhp4BMCXJgWGPIIftF5piUTKFHK5QonfSbLu-GhR8OU2AmTp_6gczIFGg_d4ukzcowsmIVX4pvXQ9G1KAPypv1yt2MX726QsNB1NW44yNqLk4FSUI30JRC7oOZRqSAtJaza8GfgRNqNryUuuRwXY6-VyjVn5FXAAHQu0MHZktM5PPURjTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتظامی: یک عده فکر می‌کردند آمریکا به هر کشوری فوت کند آن کشور نابود می‌شود اما ما هیمنهٔ آمریکا را شکستیم
🔹
اسرائیل دولت نیست یک گروه تروریستی است؛ این‌ها از اول فقط ترور انجام می‌داده‌اند و به‌همین‌دلیل سیستم ترور قوی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/akhbarefori/653881" target="_blank">📅 20:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653880">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وزارت بهداشت لبنان: شمار شهدای لبنان در پی حملات رژیم صهیونیستی از ۲ مارس ۲۰۲۶ به ۳۱۵۱ نفر رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/653880" target="_blank">📅 20:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653879">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5Hw9xsduHQHneGIcIkcqiS6hNYi31JjVMwPN_vsKA9vgnhnlJpfz-MM-7arCIRzrQBdlPrS18hXckac7JYFq7JFT_CRFbQueThwP_zMptp5FZa_oQp_9sOC-dngzGDARuvV9M34fxo_HMW0_M4Mz-BPZ53n7IFCw_zUIG5zYc2qQ-wddn-P5aLIDnkIOgnDVyN27a4Jnq1_qbXopx3PQCqmYRHWRGoaZY5yuXavRZhPhgRuifCNp5UE1SQ1wtGqWhJaQBkG_XvpWhGeFhyou7z68XmGgQCxprRwiN053YzMeyort3KUbJL7qRWMfl3Yi5N4yMKECdM3Emr-DSX1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حبابی به نام «توافق ۳۰ روزه»/ به این دلایل توافق ایران و آمریکا سر نمی گیرد
🔹
برخی مفاد مطرح شده در توافق احتمالی دارای ابهام هستند و تضمینی برای اجرای آنها وجود ندارد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217596</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/akhbarefori/653879" target="_blank">📅 20:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653878">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
واشنگتن‌تایمز: آمریکا و ایران پیش‌نویس توافق صلح را ظرف ۲۴ ساعت آینده اعلام می‌کنند
🔹
یک منبع نزدیک به مذاکرات به واشنگتن‌تایمز گفت که آمریکا و ایران تا بعدازظهر یکشنبه نهایی شدن پیش‌نویس پیشنهاد توافق صلح برای پایان دادن به درگیری‌ها در همه جبهه‌ها را اعلام می‌کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/653878" target="_blank">📅 20:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653877">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0081d835c4.mp4?token=czyZdK4Nqu3QjYxQf8e7u2ykk6bR1vqZKNM3PczskuIO4aKHjpwKahjaROVVDwLCwGn3Lx3H5i-Xm6piTsWjBmCpGkGWcbWXKEJjPz8RAFgjDaA2M5PlE2V5ZUz8oQ1MWTm53I1DgWSsTmvG50wb54iGpjVjXnrlqRSpJbeu3WpTKQOxCq6Xm9qvYKVv7WttV_oj_zp_cuU3xlVF_LZ5AB9xsdtxTJTvkCfeXR8L9RYRlhMl44MOT00FLCG2e-ndVVIf2EwBKNrepBbWnlYiQjktrNfMOjQMww7E4yZka2hs3H3gn5yTpdqAjWhVWCCTVZLMt8fRe1Ir_qkDVaJqYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0081d835c4.mp4?token=czyZdK4Nqu3QjYxQf8e7u2ykk6bR1vqZKNM3PczskuIO4aKHjpwKahjaROVVDwLCwGn3Lx3H5i-Xm6piTsWjBmCpGkGWcbWXKEJjPz8RAFgjDaA2M5PlE2V5ZUz8oQ1MWTm53I1DgWSsTmvG50wb54iGpjVjXnrlqRSpJbeu3WpTKQOxCq6Xm9qvYKVv7WttV_oj_zp_cuU3xlVF_LZ5AB9xsdtxTJTvkCfeXR8L9RYRlhMl44MOT00FLCG2e-ndVVIf2EwBKNrepBbWnlYiQjktrNfMOjQMww7E4yZka2hs3H3gn5yTpdqAjWhVWCCTVZLMt8fRe1Ir_qkDVaJqYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتظامی: من از تعداد، پراکندگی و تنوع قدرت‌مان [تا قبل از جنگ] اطلاعی نداشتم؛ حجم بازدارندگی توان موشکی ما بسیار بالاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/653877" target="_blank">📅 20:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653876">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPEN0FuSFRJQcPjEwhKcy5yel9QYFkvoMMsyizG4SEZ1ZfNEukum1bREgDwneZ6M87w4iQbpK46k5KC_TmpLe8OXSh0Jq-aFVXlGVm4qibCRvuYuu0B9GHu9YqMtqdVTWrZngS-54Muyp3xipJfEKb-CxPVfQIgc4LaxWRBSiXrrhdkoiWh3J7cGizstqL1Vtr4acx8iE33cPOCot-3PQ4ESEs98EWYf7kOOLaTKyhIH54cF2FkzF9Zo-ewJKVVSwX-qVJ4t0SgR2w85n5a3o6TnXAJlriNBrfYbFayT0SjpJHc1gmFQLGQk0UDds4EAv3smKDhL6iIAnT2tfEEkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلاکت یک خلبان صهیونیست در شمال فلسطین اشغالی
🔹
کانال ۱۲ رژیم صهیونیستی از هلاکت یک خلبان جنگنده نیروی هوایی این رژیم و فرمانده سابق یک اسکادران در حادثه سقوط یک هواپیمای سبک در تل عدشیم در شمال فلسطین اشغالی خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/akhbarefori/653876" target="_blank">📅 20:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653875">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
کارشکنی آمریکا در برخی بندهای تفاهم تا این لحظه ادامه دارد
🔹
کسب اطلاع حاکیست که علیرغم برخی گفتگوهای امروز، کارشکنی‌های آمریکا در برخی بندهای تفاهم از جمله موضوع آزادسازی اموال بلوکه شده ایران همچنان ادامه دارد و تا این لحظه این موضوعات حل نشده است.
🔹
بر این اساس، در حال حاضر همچنان امکان منتفی شدن تفاهم وجود دارد و ایران تاکید کرده است که از خطوط قرمز خود برای احقاق حقوق مردم کوتاه نخواهد آمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/653875" target="_blank">📅 19:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653874">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
رکورد شکنی شاخص بورس/ روند مثبت بورس ادامه خواهد داشت
🔹
تالار شیشه‌ای تهران در هفته‌های اخیر و پس از پشت سر گذاشتن دوره‌ای ۸۰ روزه از تعلیقِ فعالیت به دلیل متغیرهای بیرونی و ریسک‌های سیستماتیک، بار دیگر درهای خود را به روی سرمایه‌گذاران گشود.
🔹
برخلاف گمانه‌زنی‌های بدبینانه‌ای که فروپاشی یا سقوط‌های هیجانی را پیش‌بینی می‌کردند، شاخص‌های بورس با «سبزپوشی» معنادار، گامی بلند در مسیر بازیابی جایگاه خود برداشتند.
🔹
عبور شاخص کل از مرز ۳.۹ میلیون واحد، نه یک رخداد تصادفی، بلکه برآیندِ مدیریت هوشمندانه و پیاده‌سازی زیرساخت‌های پایداری است که وزارت امور اقتصادی و دارایی با راهبری دکتر سیدعلی مدنی‌زاده در پیش گرفته است./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/akhbarefori/653874" target="_blank">📅 19:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653871">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
دبیرکل حزب‌الله: تحریم‌های آمریکا هرگز ما را تضعیف نخواهد کرد؛ اگر آمریکا بیش از این خوی وحشی‌گری به خود بگیرد، دیگر چیزی برایش در لبنان باقی نخواهد ماند
🔹
مقاومت از سرزمین و شرف خود دفاع خواهد کرد و با هرکسی که در برابر ما بایستد، همان‌گونه برخورد خواهیم کرد که با «اسرائیل» روبه‌رو می‌شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/akhbarefori/653871" target="_blank">📅 19:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653870">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5722bf4152.mp4?token=RzNRX-NWKJXQdNOZGyoG6ShoAXRtukxnwPp3BLp7drmzFtf2AqJJgwE06PbW8zfHVkuQhg65dyqKjJyx8e9nUrTmB19jQxUWP6J9rLvK2zMd32oKK7zNMLiUs7q2p21gOPpXTmFH4_KMbbNXByUbFuW6QVqSRyJVCJtmoR5qLeLP_htEhtr0NVtw85lI2iqjxfgLxd8Vclb_KUXujva3f4hPmLM2f9pav69TjfQRfVTnj689V1Hj9bzBMpJAsTIMn-XwkQyZ4iKRpk8OPcCF0IWyH3Fwi56DpDWOg5S-spmT6ql3RUpvU-NcmFETRnvzLo46P1zICPSoGY4ADMql4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5722bf4152.mp4?token=RzNRX-NWKJXQdNOZGyoG6ShoAXRtukxnwPp3BLp7drmzFtf2AqJJgwE06PbW8zfHVkuQhg65dyqKjJyx8e9nUrTmB19jQxUWP6J9rLvK2zMd32oKK7zNMLiUs7q2p21gOPpXTmFH4_KMbbNXByUbFuW6QVqSRyJVCJtmoR5qLeLP_htEhtr0NVtw85lI2iqjxfgLxd8Vclb_KUXujva3f4hPmLM2f9pav69TjfQRfVTnj689V1Hj9bzBMpJAsTIMn-XwkQyZ4iKRpk8OPcCF0IWyH3Fwi56DpDWOg5S-spmT6ql3RUpvU-NcmFETRnvzLo46P1zICPSoGY4ADMql4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جواب نظامی به یک سوال دیپلماتیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/akhbarefori/653870" target="_blank">📅 19:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go-gVBVw1WZshos8mry6rdJPj3gBeVZa36uV4ozzT2K99mAyoI--Bu3upVmuW-CMn2xK9kRWHENumQCATi5ET8Onc0JUeCEKhwZKt_Cr71SP5Oj-sqWCFJiU-8quenIkNr83phv3hensy8c6kuGxNWiDqbcGy-uUZaYq7YHLidcD3PoxDjMAHZelxV9FqijNozAm00PKQAyleO3cybcVv1AYESdS3D8wKa1tL8W4kRA-lAGqoQ7O9d_ySWm3LbnlxLSRX42elNjZ9ZmzOenZ-hskAPC5JyKl1WiKUINrQLfUq_AH27yf17-KBPPEVy0mjX9mwoyj1_BxgZ8uEUy07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ابتکار بزرگ
#بیمه_البرز
برای تحقق شعار سال با بیمه‌های زندگی پروژه‌محور
بیمه البرز در راستای تحقق شعار سال «اقتصاد مقاومتی در سایه وحدت ملی و امنیت ملی» و با هدف ایفای نقش موثر در فرآیند بازسازی و توسعه اقتصاد ملی و تقویت اقتصاد خانواده پس از جنگ تحمیلی ۴۰ روزه، اجرای بیمه‌های زندگی پروژه‌محور را به‌صورت ویژه در دستور کار قرار داد.
مشروح خبر:
https://alborzinsurance.ir/PublicBlogDetail/5035</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/akhbarefori/653869" target="_blank">📅 19:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653867">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
المیادین: بخشی از توافق ایران و آمریکا، بر اساس طرح چین است
🔹
شبکه خبری المیادین جزئیاتی درباره توافق احتمالی ایران و آمریکا منتشر کرد.
🔹
به گفته این منابع، توافق ایران و آمریکا شامل بندهای مورد توافق در طرح ابتکاری چین است.
🔹
طرح چین شامل ۵ بند بود که در ۳۱ مارس پاکستان در جریان آن قرار گرفت تا یک طرح ابتکاری مشترک را تشکیل دهد.
🔹
این منابع با اشاره به اینکه تفاهم‌نامه کنونی در بند چهارم طرح ابتکاری مشترک چین و پاکستان قرار می‌گیرد، تصریح کردند: بند چهارم این طرح، توسعه و امنیت را به هم پیوند می‌دهد و شامل ۵ مورد است:
🔹
اول؛ توقف کامل جنگ و درگیری نظامی و تضمین عدم از سرگیری آن.
🔹
دوم؛ بازگشایی تنگه هرمز از دو طرف و خروج تجهیزات نظامی آمریکا از اقیانوس هند.
🔹
سوم؛ آزاد کردن بخشی از پول‌های مسدود شده ایران.
🔹
چهارم؛ لغو بخشی از تحریم‌های یک‌جانبه اعمال شده بر بخش انرژی ایران.
🔹
پنجم؛ عبور محموله‌های انرژی کشورها از طریق هرمز، از جمله ایران.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/akhbarefori/653867" target="_blank">📅 18:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653866">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivGEwMWLx5pmfmckgL0bvsYxxLZtMJyUNE9fz5Wfh0xHf0Vy-rQbimxidVnpQQC6ZGSwG4EYODQPRHZrnc1K8Etush2LZv-7MLTmGMq8-YYIyIK3_n0xzJF6OlkzP1dPBNwLSHHb3hqoDFlGyiK0dCxKGNmyie_h98NXV1SK4zRpA7Yf-_5bLoPwQryegeiBftQ_re9Sd7mih7pO25jZCV6cO9W4M_cyIy8bo9btu4A4mNQvrTZy1zz2_ECF8Sf3lHa88b79Y02k0dNKEPuC1h-TpVv5Oa8jw3sGjNO_9X5tex86_05sPEd0M5OVV_eMm22YgwCMVFyUvKiwBbLKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حبابی به نام «توافق ۳۰ روزه»/ به این دلایل توافق ایران و آمریکا سر نمی گیرد
🔹
برخی مفاد مطرح شده در توافق احتمالی دارای ابهام هستند و تضمینی برای اجرای آنها وجود ندارد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217596</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/akhbarefori/653866" target="_blank">📅 18:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653865">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
پیشنهادات جدید شورایی‌ها برای رایگان شدن مترو و اتوبوس/ بلیت رایگان برای دهک‌های ۱ تا ۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/akhbarefori/653865" target="_blank">📅 18:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653864">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjX2G8tJ6ayGFvNZ_qwHrpz7exLuWD9H1QjOSty4yKlO4nonwJUXifwMa3giafwtgxh9kNf6QeAkbIuFr1MeDrMCMySceXmZdmV30bBDo2FIzPzMGnTQIzVfvKbWASFJSgWzD-1DxEM8kILuoBNqwpiamJQpvy4znTBtqUw7iSegvrHV4H-BSrTB4Gz61tG2QpVPB3NEPCHsUXvaagjId0uJyiTBF0Vd7VZc0sakHSYB_z6pehpySAz0IXxFEMaAbjO3tbHV9YekAK0LxKnXcPpehdLM0C69RrIWXPdFKbuZD-2ZXDmG321UvfvgIYcXkpN0RqBCFbbsBSl_WguySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: اقدام تروریستی در راه آهن کویته را محکوم می‌کنیم
🔹
سخنگوی وزارت خارجه: این اقدام تروریستی به جان‌باختن و مجروح شدن تعداد زیادی از شهروندان پاکستانی منجر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/akhbarefori/653864" target="_blank">📅 18:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653863">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB3tWFnPlHC5XFG3vGvMxPI78E1q3UBMpyE7zFsYvaa3OWATRjEqApgn23QTb4_BtkJt48_wS5uzm_yrNuQHuKaYest1aHgTgtD4QOL2craqzKdQEaqDZ5tzQ3kJpZGdoDWe-q7rbXFbE3KVho0nXC5mz0ny2zFK7-jeWr0lsTxQbXBnJlj5ZcCtsY_tqWzWyql2ayOAOMfDAp5pUHnjczCGQLrDmlxeOdRgntO5jwj3usjOeSjVo2K6OWwRsKlUkm46oW_glQZLNxU63sQWH_X_kYyzTMecypMnQkZDkPKGjU3vV_hQa8H85Q8FRrFoYzKBmpWjKDRLeMXEwxp35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب آبادی: برخی کشورها بعد از دستور دیوان بین‌المللی دادگستری، کالاهای مرتبط با امور نظامی به رژیم صهیونسیتی داده اند
🔹
معاون وزیر خارجه: تعهد به پیشگیری از نسل کشی در کنوانسیون ۱۹۴۸ تعهد واقعی است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/akhbarefori/653863" target="_blank">📅 18:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653862">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNwmJMZOZiskmtAH9gOKEaTeL0R5LH7kd3VwE2xclI6nCUMHRsunTDA8RexVOJMWFu8OaD5jtwhFfVA1k8SXNhk9MtjN7RvRcbFXDZgwPwmi1-GfAaF2gnlESdb_DgRM-Ixi3koDbbgAg_SGiIBSH2g1sUeQlCqKXFX3xEpuMJufI8WkTUn0neeUIC49YyCbUV8tu-5saSecc9TxWdjz9KeXCUilkgpUeMaSU1EN-uRUcOa0CvJGSa7vnWyROSLXW8zEWVi0fiwzHly7QiEQ0L8oINVoWetQz3icdlIG59jtFwsiDYCEi56fv7IapOroq8lmoYHwSoxsCMurkCeEvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید نتانیاهو کودک کش با عکس ترامپ: ایران هرگز سلاح هسته‌ای نخواهد داشت
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/653862" target="_blank">📅 18:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653861">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
حجت‌الاسلام اژه‌ای: وحدت رکن اساسی مقابله با دشمن است
🔹
رئیس قوه قضاییه در حاشیه مراسم بزرگداشت شهدای جنگ تحمیلی سوم:
🔹
در هر سه رکن «خیابان»، «میدان» و «دیپلماسی» باید به مؤلفه و عنصر «وحدت» توجه ویژه کنیم و در هر سه عرصه‌ مذکور، دشمن و حیله‌ها و مکاید او را بشناسیم
🔹
قطعاً ملت متحد و منسجم ما و همه مسئولان و کارگزاران، دست از مبازه با استکبار و ایادی او برنخواهند داشت و ما اعلام می‌داریم که «تا آخر ایستاده‌ایم»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/akhbarefori/653861" target="_blank">📅 18:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653859">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPsgMwd4WZDRXC4bzwB0EOj4UeLVi-5uTPZrGfLVTz1IQ3v3Bq8OzFWB-_NNklcTlHTBFK8QEY3J83wM20SuEi3tXNP5uzHAbqTgKOxogMAxjoJSXOYU5ysiAd2tBN4vOm_36frhzrvE_WMyWSiy6kx3UQIKEAJitBC9e9dUvsk3hmA0QqhzaQ17Ux9Q29OCvz_KA9xAyM9tlErMNTjFJ-UPY6bVj9lGjadxv9XLwlH3x2j8ASoEZVgTEz_5bEBP9j9bCubSufkYiurdwPiv3C4jwQXgs96VXGiemJ0op7Moc7oGw51fXi2ttfOjnS4kx3MjS4FJPE47NN64L6qe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوفوها، بشقاب‌پرنده‌ها و پرده‌های دود | چرا واشنگتن شیفته موجودات فضایی است؟
🔹
در سال‌های اخیر، موضوع بشقاب‌پرنده‌ها و موجودات فرازمینی از حاشیه فرهنگ عامه به قلب سیاست آمریکا راه پیدا کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3217529</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/akhbarefori/653859" target="_blank">📅 17:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653858">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
دو بند از توافق احتمالی آمریکا و ایران به نقل ار فاکس نیوز
🔹
نیروهای آمریکایی به مدت ۳۰ روز در مجاورت ایران خواهند ماند.
🔹
به عنوان بخشی از این توافق، ایران معافیت از تحریم‌های نفتی دریافت خواهد کرد. همچنین میلیاردها دلار از دارایی‌ها و پول‌های مسدود شده ایران آزاد خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/akhbarefori/653858" target="_blank">📅 17:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653857">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75595ea0fa.mov?token=mwwQjBjD5kzqmNe30KGygdP1hiYgFMTtL2M_ouyvJb-EkQ-OiNHSEhTdrEgFMFzDDa5ERTpUJ5YJzREyw-Ix9uqXs4MsYLx4iq4umiMNqLZvI6-b65vl6qQxyw7mlMg2osvCRQEGdjb8y2sMdXfqDRvqkxCxYK_2X-T5nafSDtB_d2RyWBEXzWvuQ8eLwfCr4ree_DsrgtIFD4XGgrR9yksbjrvk9RPkEnR4kiyLdgjfsMb2pU3L4eW0ve5yYDnXtDj1c7IR-zg38OjtC8ALC8xtuRZkHTnh91uLXszpZbCaj97wT3_YoAz5BIzszeHhh2V5LXltaF0N7aV6rmTsQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75595ea0fa.mov?token=mwwQjBjD5kzqmNe30KGygdP1hiYgFMTtL2M_ouyvJb-EkQ-OiNHSEhTdrEgFMFzDDa5ERTpUJ5YJzREyw-Ix9uqXs4MsYLx4iq4umiMNqLZvI6-b65vl6qQxyw7mlMg2osvCRQEGdjb8y2sMdXfqDRvqkxCxYK_2X-T5nafSDtB_d2RyWBEXzWvuQ8eLwfCr4ree_DsrgtIFD4XGgrR9yksbjrvk9RPkEnR4kiyLdgjfsMb2pU3L4eW0ve5yYDnXtDj1c7IR-zg38OjtC8ALC8xtuRZkHTnh91uLXszpZbCaj97wT3_YoAz5BIzszeHhh2V5LXltaF0N7aV6rmTsQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: فرماندهان آمریکایی فهمیده‌اند که باز کردن تنگه هرمز دالان سیاه و تاریکی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/653857" target="_blank">📅 17:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653856">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آماده‌سازی‌ ناوگان‌ جدید به‌منظور شکستن محاصره نوار غزه
🔹
رئیس کمیته بین‌المللی شکستن محاصره غزه: آماده‌سازی‌ها برای راه‌اندازی ناوگان‌ جدید به‌منظور شکستن محاصره نوار غزه آغاز شد. متوقف‌کردن یا رهگیری ناوگان‌ها از سوی رژیم صهیونیستی نمی‌تواند به موج همبستگی با نوار غزه را پایان دهند و تا زمانی که محاصره این منطقه ادامه داشته باشد، این تلاش‌ها متوقف نخواهد شد.
🔹
رژیم صهیونیستی هفته گذشته موجی دیگر از کشتی های ناوگان صمود را توقیف و فعالان سرنشین این کشتی ها از ۴۰ کشور را بازداشت کرد.
🔹
این فعالان پس از آزادی از آزار و شکنجه خود توسط صهیونیست‌ها خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/653856" target="_blank">📅 17:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653855">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ترامپ از کدام خبر خوب صحبت می‌کند؟
🔹
ترامپ بعد از آنکه تمام اهداف اولیه‌اش از جنگ شکست خورده به ای‌بی‌سی نیوز گفته است:«من نمی‌توانم در مورد این توافق صحبت کنم؛ کاملاً به من بستگی دارد و اگر خبری باشد، فقط خبر خوب خواهد بود. من توافق بد نمی‌کنم.»
🔹
قرار بود حاکمیت ایران نابود شود حالا ناچار شده در مورد حاکمیت ایران بر هرمز پای میز مذاکره بنشیند.
🔹
همچنین قرار بود نفت ایران را غارت کند حالا باید در مورد پس دادن دارایی‌های بلوکه شده صحبت کند.
🔹
قرار بود تمدن ایران را نابود کند ناچار شده است به مذاکره با همین مهد تمدن تن بدهد.
🔹
اخبار خوب مورد ادعای ترامپ در گفت‌وگو با NBC را بیشتر لیست کنیم یا بس است؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/akhbarefori/653855" target="_blank">📅 17:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653854">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
‌ سرلشکر رضایی: اگر دشمن به تنگۀ هرمز حمله کند، ما محاصرۀ دریایی را می‌شکنیم و ممکن است از NPT خارج شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/653854" target="_blank">📅 17:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653852">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ایران بساط سواستفاده دشمن را از تنگه هرمز برخواهد چید
🔹
پیام فرمانده قرارگاه مرکزی خاتم الانبیا(ص) بمناسبت آیین گرامیداشت شهدای جنگ رمضان: در این مراسم شکوهمند که بر تداوم مقاومت و پایداری و هوشیاری و هوشمندی برابر دشمن امریکایی صهیونی تأکید دارد، با تأسی از رهبر عزیزمان، ایران اسلامی با شکر عملی نعمت، منطقه خلیج فارس را ایمن خواهد کرد و بساط سوءاستفاده‌های دشمن را از این آبراه برخواهد چید و آسایش و پیشرفت را به نفع همه ملت‌های منطقه رقم خواهد زد.
🔹
به دشمنان هشدار می‌دهیم که برنامه‌ها و راهبردهای رهبر انقلاب برای مدیریت خلیج فارس و تنگه هرمز، آینده منطقه و نظم جدید منطقه‌ای و جهانی را در سایه راهبرد «ایران قوی» تضمین می‌کند، که بیگانگان هیچ جایگاهی در آن ندارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/akhbarefori/653852" target="_blank">📅 17:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653851">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c518857418.mp4?token=ol0Pywhf8UMGj-XkF4-FnoqDuQr3S0slbAJW4n2WPCXVTd4x0HmAf_oBw8hbqn9mQcORbvtB7o_OW_naEcVviuTqTHPIilPWrmE-jzDO-REvI5NT-_85zp2oYjBjWfrvQHvKZLRmjqi3qqc12w-G57cJoMcsS-lAMeFwg88Onywz42E3G557vIuRUGQu5Wv6jO-mUeEy00byMv1cr1AaPXZwxOXER656FfNi2MoBrpItbtLAMDzi8frOSAIB039YvJOy3WhQvGgAlzyldw5zFebdHFhwuq7BmtlJP5hOFyFsHcqYirJMXOeB4PvudicqVFgrxKJ_szz7lstozMLmDijz6TFLHE4x0rOyIh3NgFsTZIMKp-jLCOD10xmTqBOX2T6Tb75q-v59oK5bKEjRAirqKuwA-1mweldy7aD0i8Np6fOG5tWy9SzN0fiXRjAexEv9BdoiCFDvITdQHJRCZyR3z9K9YwOOGz4t3s19hUEYj5GGlmk408lOVHX4KICzg62VQsOzo5msjf9LwC9R62GTdczATMYRbATIw-I5tMx0KeRZf_OPTWlWYxj5nS5lVOC4zghj-2kBTjXXHEn3pYmFnRQXQ-nNv9D6CCHXfmEjRCJKeaN2WwIBs2MQoc-ZeAM2h3GCSf9_d0xxJbY3fSCsKL9HT6gI18awyaa3udg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c518857418.mp4?token=ol0Pywhf8UMGj-XkF4-FnoqDuQr3S0slbAJW4n2WPCXVTd4x0HmAf_oBw8hbqn9mQcORbvtB7o_OW_naEcVviuTqTHPIilPWrmE-jzDO-REvI5NT-_85zp2oYjBjWfrvQHvKZLRmjqi3qqc12w-G57cJoMcsS-lAMeFwg88Onywz42E3G557vIuRUGQu5Wv6jO-mUeEy00byMv1cr1AaPXZwxOXER656FfNi2MoBrpItbtLAMDzi8frOSAIB039YvJOy3WhQvGgAlzyldw5zFebdHFhwuq7BmtlJP5hOFyFsHcqYirJMXOeB4PvudicqVFgrxKJ_szz7lstozMLmDijz6TFLHE4x0rOyIh3NgFsTZIMKp-jLCOD10xmTqBOX2T6Tb75q-v59oK5bKEjRAirqKuwA-1mweldy7aD0i8Np6fOG5tWy9SzN0fiXRjAexEv9BdoiCFDvITdQHJRCZyR3z9K9YwOOGz4t3s19hUEYj5GGlmk408lOVHX4KICzg62VQsOzo5msjf9LwC9R62GTdczATMYRbATIw-I5tMx0KeRZf_OPTWlWYxj5nS5lVOC4zghj-2kBTjXXHEn3pYmFnRQXQ-nNv9D6CCHXfmEjRCJKeaN2WwIBs2MQoc-ZeAM2h3GCSf9_d0xxJbY3fSCsKL9HT6gI18awyaa3udg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: متجاوزان در دام راهبردی تنگه هرمز گرفتار شدند
🔹
بررسی تصمیم‌گیری‌های ارتش آمریکا نشان می‌دهد که آن‌ها نبرد ۴۰ روزه اخیر را تنها برای چهار تا پنج روز و در بدبینانه‌ترین حالت برای ۱۵ روز طراحی کرده و متناسب با همین بازه زمانی نیرو گسیل داشته بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/653851" target="_blank">📅 17:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653850">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee39774246.mp4?token=SMVKNKaUEQSOgQfzctWtB-e9MB7c5fYB_NULGDHnRMI15O-JIWcHLJTUWPj_NPqPS2K4H8xNAHjgruq1_htc1UbFb8VzXxG640JNgy7fma-2cM5fSPeoa_c6q6DsPf6Zr71uJGGa-FhfYhaPHCPco2Zi4I83pif676MM9h8sXB5je0qh7drPZIX7z_XiWDpVpVqzT-h65oMexV5TAYG77UnXU9cYz5GnhA5OhwzhB1w6wRwRe891w6EyWC66JqcsqsZvllfEjnUevoZJ9Ae7VGGiT3i7T1A9xQ45tI22UMaxKQNMlvi9rJO4oTQbZvZ1jlV7aJwqfq0CNXS50Fvajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee39774246.mp4?token=SMVKNKaUEQSOgQfzctWtB-e9MB7c5fYB_NULGDHnRMI15O-JIWcHLJTUWPj_NPqPS2K4H8xNAHjgruq1_htc1UbFb8VzXxG640JNgy7fma-2cM5fSPeoa_c6q6DsPf6Zr71uJGGa-FhfYhaPHCPco2Zi4I83pif676MM9h8sXB5je0qh7drPZIX7z_XiWDpVpVqzT-h65oMexV5TAYG77UnXU9cYz5GnhA5OhwzhB1w6wRwRe891w6EyWC66JqcsqsZvllfEjnUevoZJ9Ae7VGGiT3i7T1A9xQ45tI22UMaxKQNMlvi9rJO4oTQbZvZ1jlV7aJwqfq0CNXS50Fvajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: ممکن است از ان پی تی خارج شویم، راهی را که آمدید برگردید
🔹
اگر محاصره ادامه داشته باشد آن را می‌شکنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/653850" target="_blank">📅 17:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653849">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed16233809.mp4?token=cZh3UXIQct4vWqJbr0yyg7_vkRVZtujUp251j_gjl2F_4LPzkezmiLew_kGWkzQQ4PvJk3dlrNzKWZqj2jHcc2z0AcVmwGFAMXqO2zDRsjT93AvM8TK_FA2e8G0c6DqCIBDiNo5iJw3kz1meJ52SDEUEMvRE9qiFvBlsZRHsFf8EwWt5arhqsvUi3WZXp4Das_e92RFGQK7YW5e9ANPfXrcGL27G5uBRbLNL_VAffvDec0aYcAotWTJd7yTQXbpWrnYT-LD8UYV91pXK0MUslzCzRfRCMVjdpLIvjWGFi60VpCZ-9UBveZRgVTmx88aytiJPASva5dQBbU2jmiXgcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed16233809.mp4?token=cZh3UXIQct4vWqJbr0yyg7_vkRVZtujUp251j_gjl2F_4LPzkezmiLew_kGWkzQQ4PvJk3dlrNzKWZqj2jHcc2z0AcVmwGFAMXqO2zDRsjT93AvM8TK_FA2e8G0c6DqCIBDiNo5iJw3kz1meJ52SDEUEMvRE9qiFvBlsZRHsFf8EwWt5arhqsvUi3WZXp4Das_e92RFGQK7YW5e9ANPfXrcGL27G5uBRbLNL_VAffvDec0aYcAotWTJd7yTQXbpWrnYT-LD8UYV91pXK0MUslzCzRfRCMVjdpLIvjWGFi60VpCZ-9UBveZRgVTmx88aytiJPASva5dQBbU2jmiXgcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش امیر سیاری معاون هماهنگ‌کننده ارتش به اجرایی شدن توافق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/akhbarefori/653849" target="_blank">📅 17:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653848">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d37bf7f5f0.mp4?token=vWpA118a3c7Y7PifKjH8-n9FGXyivvbi56M6J3UUDJRxyJsjY9GouNCyjK2AFjvPB9Isvtg06jpT0RSuvo4caz2zGNusg-hWkqMGTd2iOFGoSDUgdNwHxp-bnv-VhbyGhiF1dOLTeodO60CwkS2q-GH-jGSMRJvjyjHJ1hi3NZyRT-aIgPn5nuXxR6WDRxLeu7BYCfhsXK-uGNIP2YowkkmFWMWqeM7Wz_OHubxurmPIQMFgZdYjA5iLV3orxQrfcbdUtAavNiuUi7yfTX72Yl_r2YGyUFiAVvCeshE9BUAJO-APB2E9W3epiDblDnPVbUSTV4sihNz3OQKdm02Wpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d37bf7f5f0.mp4?token=vWpA118a3c7Y7PifKjH8-n9FGXyivvbi56M6J3UUDJRxyJsjY9GouNCyjK2AFjvPB9Isvtg06jpT0RSuvo4caz2zGNusg-hWkqMGTd2iOFGoSDUgdNwHxp-bnv-VhbyGhiF1dOLTeodO60CwkS2q-GH-jGSMRJvjyjHJ1hi3NZyRT-aIgPn5nuXxR6WDRxLeu7BYCfhsXK-uGNIP2YowkkmFWMWqeM7Wz_OHubxurmPIQMFgZdYjA5iLV3orxQrfcbdUtAavNiuUi7yfTX72Yl_r2YGyUFiAVvCeshE9BUAJO-APB2E9W3epiDblDnPVbUSTV4sihNz3OQKdm02Wpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از کشف لاشه پهپاد متلاشی شده اربیتر که در آسمان هرمزگان درحال جاسوسی بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/653848" target="_blank">📅 17:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653847">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
محسن رضایی: برای اولین بار بعد از جنگ جهانی دوم ابرقدرتی آمریکا دوباره فرو ریخت
🔹
آمریکا بعد از جنگ رمضان دیگر به آن آمریکای سابق برنخواهد گشت و ما افول آمریکا در خاورمیانه رقم زدیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/akhbarefori/653847" target="_blank">📅 16:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653846">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1242bf8da9.mp4?token=bJUSj60D_NOvcZdtMHU8cQR3luVJYvJXZJNDMF9tHAw6pviI0ypHEkdMCoM5KExrDJoqBHmj3g5ochLtczRTjEAeTM0NJwxm9pL5eBCiLVCgPw0dMVYFkRHM2QKeFOLZ3Kb7Awxk_C-lMUyLrKfqcaIgPuh601VOauRe4DBuEv9h7COeWc4O5DpJ2xi2oIhkIXFbsoILwPGTaREGNZ3B_VRSGFFfcfQAK3rRz1ZwYbzpiZUhU55YdsljGpoKKGtb_0yQYiGULdAnxeS7hIWZQtHj98Xp7L_vyjr6qfdgrB5VbTs2mkA3OMXof-jwkV2rLT76-M4V2KwdwW-luXzhFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1242bf8da9.mp4?token=bJUSj60D_NOvcZdtMHU8cQR3luVJYvJXZJNDMF9tHAw6pviI0ypHEkdMCoM5KExrDJoqBHmj3g5ochLtczRTjEAeTM0NJwxm9pL5eBCiLVCgPw0dMVYFkRHM2QKeFOLZ3Kb7Awxk_C-lMUyLrKfqcaIgPuh601VOauRe4DBuEv9h7COeWc4O5DpJ2xi2oIhkIXFbsoILwPGTaREGNZ3B_VRSGFFfcfQAK3rRz1ZwYbzpiZUhU55YdsljGpoKKGtb_0yQYiGULdAnxeS7hIWZQtHj98Xp7L_vyjr6qfdgrB5VbTs2mkA3OMXof-jwkV2rLT76-M4V2KwdwW-luXzhFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار محسن رضایی: دست ما روی ماشه است
🔹
کاری می‌کنیم که امنیت کشور در ۵۰ سال آینده تامین شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/akhbarefori/653846" target="_blank">📅 16:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653845">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
امیر سیاری: در صورت تجاوز مجدد قطعا آمادگی وجود دارد
🔹
رئیس ستاد و معاون هماهنگ‌کننده ارتش: روش ما این است که راه شهدا را ادامه می‌دهیم. اگر فرمانده‌ای شهید شود فرمانده بعدی جای او را پر می‌کند؛ ما الحمدالله فرمانده لایقی که بتواند صحنه ها را کنترل کند زیاد داریم.
🔹
توان نظامی ایران بستگی به اراده مردم دارد، وقتی مردم در صحنه هستند همه توان‌ها وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/653845" target="_blank">📅 16:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653844">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
گرانی قیمت دارو به تغییرات نرخ ارز و تورم عمومی کشور باز می‌گردد
🔹
وزیر بهداشت و درمان در جلسه نظارتی مجلس: گرانی قیمت دارو به تغییرات نرخ ارز و تورم عمومی کشور باز می‌گردد و تلاش داریم این گرانی‌ها را از طریق بیمه‌ها پوشش دهیم.
🔹
راهکار اصلی این است که بتوانیم تمامی افزایش قیمت‌های دارویی را در قالب بیمه، پوشش بدهیم تا فشار مضاعفی بر مردم وارد نشود.
🔹
علی نیکزاد نایب رئیس مجلس: سازمان برنامه و بودجه اعلام می‌کند ارز ۲۸ هزار و ۵۰۰ تومانی حذف نشده، بنابراین دارویی که با این نرخ ارز وارد می‌شود نباید سه تا پنج برابر افزایش قیمت داشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/akhbarefori/653844" target="_blank">📅 16:53 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

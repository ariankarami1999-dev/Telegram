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
<img src="https://cdn4.telesco.pe/file/Lym_dcOQXWsF_VmRN1_gihXvKoSBq_mwDQe0GkDvQevnF1oxcQurBQ6Wmu8wey00Ym0hH_6LlQT9d4LK_DewhnlPj_m85LgO_V7zcxj93fYEhR83A9YxvJmZJrsiXhnNQ1d56jASgwupaHCvKf6-F57xGRqC7X7OlnzFyDQn_9NL-Xx3l7hk7eI-ZGmkkMu4iyznv1h1RSGa8Asux5aP3v0e7NNp_s3ADvpu5l1Ud8UL_2u9pVMLK9mFJR4Tul8V-UVKRVYhRrv34oOYGH7cCmzQ5NA-4peqOo8-SyPrMno5PRKx32CvNXUZ91yBasYXVaDw0EddgHp0W19AIlIJfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 22:31:10</div>
<hr>

<div class="tg-post" id="msg-685404">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ایران دلار را از کجا می‌آورد؟
الجزیره:
🔹
با وجود تحریم‌ها، ایران از مسیرهایی مثل فروش نفت به چین، دریافت یوان، صادرات غیرنفتی، صرافی‌ها و واسطه‌ها، تجارت با کشورهای همسایه، حواله، طلا، ارز دیجیتال و تهاتر به ارزش دلاری دسترسی پیدا می‌کند.
🔹
چین خریدار اصلی نفت ایران است و بخش زیادی از معاملات با یوان انجام می‌شود؛ سپس شبکه‌های واسطه‌ای این درآمد را به ارزهایی مثل دلار و درهم تبدیل می‌کنند.
🔹
عراق و افغانستان نیز از مسیرهای ورود دلار نقدی به منطقه هستند. در کنار آن، صادرات پتروشیمی، فولاد و محصولات کشاورزی میلیاردها دلار درآمد ارزی ایجاد می‌کند.
🔹
در نتیجه، تحریم‌ها ایران را از دلار جدا نکرده‌اند؛ بلکه مسیر دسترسی ایران به دلار و ارزش دلاری را پیچیده‌تر و غیرمستقیم‌تر کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/685404" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
غریب‌آبادی: ایران آماده حرکت در مسیر تقویت وحدت و همکاری با کشورهای اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/akhbarefori/685403" target="_blank">📅 22:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: ایران در شرایط سخت جنگی، برای اولین بار در تولید گوشت مرغ خودکفا شده است و به سمت صادرات آن در حرکت هستیم
🔹
تولید گوشت قرمز نیز افزایش یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/akhbarefori/685402" target="_blank">📅 22:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
غریب‌آبادی: ایران آماده حرکت در مسیر تقویت وحدت و همکاری با کشورهای اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/685401" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685397">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">السلام علیک یا رسول الله</div>
  <div class="tg-doc-extra">ماهر زین</div>
</div>
<a href="https://t.me/akhbarefori/685397" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
به پایش ریختند از نور‌ها آن قدر از بالا
که سینه ریز خورشید این وسط ناچیز مثقال است
#پک_مولودی
ویژه ولادت حضرت محمد (ص)
مرجع رسمی مولودی و مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/685397" target="_blank">📅 22:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685396">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2d0487e0.mp4?token=Rmp5d2woqEcgAIa4P-ZN-A40QjZDD2hyYsbL7ioeTxrxwKry7HQoliLeh7QvYUBFzG9Y0sJCX-EOjbwgaFVdI4xhf5aer5PzDjvPEAOrp5npHIW31KoOj_iQMWbCRuRhKC4oHj4fz8b7O_mNEDSMNME7ypdX2yl8QEjjWB4HNVohgdoxv3il4J452C9z0tqoTvkLI7KzMXqJLp5zxWKnYXkvAhMTxMS9PLO9-EYzBm8PLjwXtDAvmJbTdJ0JRErBV21e60nGSdTceQwkhIwQF7Wvg5RtNlycoRq6--MvXeNiOHgYcYQud5iOQCo1xYymAcTLtA-eIUxzBoDiaS9Llw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2d0487e0.mp4?token=Rmp5d2woqEcgAIa4P-ZN-A40QjZDD2hyYsbL7ioeTxrxwKry7HQoliLeh7QvYUBFzG9Y0sJCX-EOjbwgaFVdI4xhf5aer5PzDjvPEAOrp5npHIW31KoOj_iQMWbCRuRhKC4oHj4fz8b7O_mNEDSMNME7ypdX2yl8QEjjWB4HNVohgdoxv3il4J452C9z0tqoTvkLI7KzMXqJLp5zxWKnYXkvAhMTxMS9PLO9-EYzBm8PLjwXtDAvmJbTdJ0JRErBV21e60nGSdTceQwkhIwQF7Wvg5RtNlycoRq6--MvXeNiOHgYcYQud5iOQCo1xYymAcTLtA-eIUxzBoDiaS9Llw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان زندگی هرکس مرگ اوست، جز مرد حق که مرگ وی آغاز دفتر است
🔹
دست‌نوشتۀ سپهبد موسوی فرمانده شهید ستاد کل نیروهای مسلح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/685396" target="_blank">📅 22:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685395">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXEKAptPPKkdsvVd3798tkBIi3DDMoF0eYi9qo4zQ0pEd3oMc-4lcMs5gtqFYzAiHOhSbXIVxUWSdprCBcbiTU2Bivh6GwTRY9lUFS9Z_la901gerv15DDzwhNoou8Wud0uXo_BOeCv9XdPsoZlQzIs0A81HErK9Kwu-8SvKtOYSEseOpkjOFBH8bXvB6yUfvm2D67BqBKOPhmm6azeU1Pbb-moVL3mNK1TlhKSQ8Mwwt-AhGDiZv8xClyXFwJTbkDLHxXiIHn1uRpjZvA-KL6B2pOEtuKhlG_lpz9DP69P3cnVejMrnmhn1Eoe3drLe8eXJZLCdNeJklzajef2gKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایالات متحده تهدید کرده است: با حاکمیت بریتانیا بر جزایر فاکلند مخالفت خواهد کرد اگر انگلستان هزینه های دفاعی خود را به ۵ درصد از تولید ناخالص داخلی خود برای ناتو افزایش ندهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/685395" target="_blank">📅 22:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685394">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMo-f0I_HiYVvZ7UIS5z9YKiY5GQGNwWZH8bIDuVdLFW8FLx3179rc24hYYxFfgEyhm1oHeu7xv3L83Gcae9X___9kwD7klXqUQ8jv39gaYYCjI2Cd_EGX9F0koH_1SqskP2nPJ6mOAFJsts-C75TqrBwpgwYeGaejL9kKIUk_5aH5Aj8szEtw77JuHe-aQ2X5cn233o7CnGk862Yq0ncl_T4Zs4UAR_WWBcYdQk6QpzFzPxqEFPkVEfO6w4qC2suwTYfstYSCj0FzNSEGUS3KubKo74Yd6R-miGvQnQptpecIdflIl8KHp-6LthHs7JURKckuKq8fOAjbI6Yg2QFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده مجلس: بدهی تراستی‌ها باید دلاری تسویه شود، نه ریالی
🔹
رحیم زارع، عضو کمیسیون برنامه و بودجه مجلس، گفته بدهی تراستی‌هایی که پول حاصل از فروش نفت را بازنگردانده‌اند باید به ارز و با نرخ روز تسویه شود و تبدیل آن به بدهی ریالی قابل قبول نیست.
🔹
وی یادآور شد: در سال ۱۳۹۶ نرخ دلار نزدیک به چهار هزار تومان بود؛ یعنی یک میلیارد دلار حدود چهار هزار میلیارد تومان می‌شد، اما این مبلغ تاکنون تسویه نشده و با احتساب نرخ ارز به رقمی بالغ بر ۲۰۰ هزار میلیارد تومان رسیده است. یعنی ارزش این ثروت حدود ۵۰ برابر افزایش پیدا کرده است.
🔹
این عضو کمیسیون برنامه و بودجه مجلس بیان کرد: دولت باید بدهی خود از تراستی‌ها را به نرخ روز ارز بگیرد، نه اینکه معادل ریالی آن را دریافت کند. اینکه دولت بگوید معادل ریالی ارز را از تراستی‌ها می‌گیرد، درست نیست و اقدامی اشتباه است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/685394" target="_blank">📅 22:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685393">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVzSlGDWFYIyw6sL_60hHcl3DkW3tC75KOtO7LVNWtFi6mG9nTSMOxSwyb5NWzdP5oDzsP1DTpf0wdPrf6qxZudowaRTmjmmACGtHdceadzJz60URmIJdkng7w_VTn5FoUTxj8HbvqQT7tt486FxkR3tER84-bIx059nht71XuCl2vPJ33a7o6aSu9pIlbxKfGQdorbGq5aSyrOLz54oEHTVfJpX5872MdXZ7mst0tSUR9FJ7CFEP7NzUZL58eVK_DuslWxoHt1UFFamtknNqsLHGZuNXqwzpcICE1dpMYKB-GECMx2G6Wgwuj59GIe8h2dCv7d62IQBWvg5z7i5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیفت دفاعی ایران آغاز شد/ استراتژی جدید ایران در مقابله با آمریکا: درگیری مستقیم، حفظ سایه ترس و دیپلماسی با همسایگان
🔹
اکنون، ایران در سال‌های ۲۰۲۵ و ۲۰۲۶ در دو جنگ دیگر شرکت کرده است و درس‌های جدیدی را علاوه بر درس‌های قدیمی فرا می‌گیرد. واشنگتن باید به این درس‌ها توجه زیادی داشته باشد، زیرا آنها استراتژی ایران را برای سال‌های آینده شکل خواهند داد.
ترجمه گزارش پایگاه The Dispatch را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3241350</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/685393" target="_blank">📅 22:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685392">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef7f9f7d3.mp4?token=DOsnoMkBaLNEOjxqNe7zYsfp2j1Xg-FjEPmzjQqFcdFJSS4tM_chynt-NemYGqr1w3QpGBvMgyIHMY5D0YiYq8w2LY4Hzi_In8oPg5ZxVgP1nzlhRk5u1Fsv2AC4eD4HI7ZkIy95pkAbxJBdR1H4GYIJB8VtnMYQrTCwnxav9f1cDTgj4s1H44aVuFOA5PixXryovQirSlLjyga_ZbOg3EpTvvrS6Y2HppnnPDtjdQCsOpgci6ssVcrWs6XnPcoKdxHxoVrH2jk-srOPEHCP938Z51IiMDgOyrmdY8WLbPjlr3_tsO_ZWU0aRiQDBMYgpxo9VSJkUDZ8MCRFKHDm9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef7f9f7d3.mp4?token=DOsnoMkBaLNEOjxqNe7zYsfp2j1Xg-FjEPmzjQqFcdFJSS4tM_chynt-NemYGqr1w3QpGBvMgyIHMY5D0YiYq8w2LY4Hzi_In8oPg5ZxVgP1nzlhRk5u1Fsv2AC4eD4HI7ZkIy95pkAbxJBdR1H4GYIJB8VtnMYQrTCwnxav9f1cDTgj4s1H44aVuFOA5PixXryovQirSlLjyga_ZbOg3EpTvvrS6Y2HppnnPDtjdQCsOpgci6ssVcrWs6XnPcoKdxHxoVrH2jk-srOPEHCP938Z51IiMDgOyrmdY8WLbPjlr3_tsO_ZWU0aRiQDBMYgpxo9VSJkUDZ8MCRFKHDm9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلویزیون دولتی روسیه نحوه نابود کردن بریتانیا با بمب اتم را بررسی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/685392" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685391">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkEEUC2RFvXoKqH3mum7TWKO1ghhbEWfpVzu80q_BgfcKnO-9wm4P4XBkM6Fn3mVxUAmBhS_hBlXTbnNyPOl-SDJHEytKYfQXew29dbEGcc75QiO46SEIIE5tlKQx79Pdnj44p0HdrAlRTv1ijHLuFIL91t4xhm33tXdntr6_L6vvWAAtVEb-rp7h5ppusuGdOISsomj-JBBQxixPc6Vi2e6jlLV73qlLtc8Ce86oxnIincjQkdSE7Xahc5zHNtVoug8pxi9mRpqZn4VvwiXW7ObkDOKo4g_WwtUU8Qr0S76khCwIr2FtoykRrs4PSdHjqr6a0uYb6i652DP-dDiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبر، فقط تحمل سختی‌ها نیست؛ انتخابی آگاهانه برای رسیدن به چیزی‌ست که ارزش انتظار کشیدن دارد
🔹
امام علی(ع) در نهج‌البلاغه می‌فرماید که صبر دو گونه است؛ صبر بر آنچه ناخوشایند است و صبر در برابر آنچه انسان دوست دارد. گاهی باید برای عبور از سختی‌ها صبور بود…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/685391" target="_blank">📅 22:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685390">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
اروپا علیه شبکه‌های اجتماعی برای کودکان؛ اسلواکی هم وارد میدان شد
🔹
دولت اسلواکی در ۲۶ اوت طرحی را تصویب کرد که بر اساس آن استفاده کودکان زیر ۱۶ سال از شبکه‌های اجتماعی ممنوع خواهد شد؛ این طرح نیازمند تصویب پارلمان است و شامل سازوکارهای احراز سن می‌شود.
🔹
نیوزیلند نیز همین هفته طرح ممنوعیت استفاده افراد زیر ۱۶ سال را مطرح کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/685390" target="_blank">📅 21:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685389">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4eecac98.mp4?token=RWOBphbVAb--yM10jqmFXdkJ5CiJbsi1td_NGKBi6dWUlGoqBsETGRVH2HWCHTbTzLtdnG04QYVskAKxRDSIBPubvvj2qv3cCybVFjDSDHS3KRJxgqCn-tGFK8UJyivLSZ6HbIfHJpck8de2P6ybno5iQ-JePkppC030ly_PEP42RwrGs59ZbOtrwSG8vV7gl2SLrkABZxTjzIkUcAIkpit6Ge0ROaRvnvuvJzMzjytzWuApsUDSB3nvduZaToY7xI0MjScHNT0uf_ohHwwG_ZkaTuA61XW9drU4eF-gKru84UwWbZSTt1JZOkDu3Qo1bIzQ5AxXdKRF0y4nEBKJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4eecac98.mp4?token=RWOBphbVAb--yM10jqmFXdkJ5CiJbsi1td_NGKBi6dWUlGoqBsETGRVH2HWCHTbTzLtdnG04QYVskAKxRDSIBPubvvj2qv3cCybVFjDSDHS3KRJxgqCn-tGFK8UJyivLSZ6HbIfHJpck8de2P6ybno5iQ-JePkppC030ly_PEP42RwrGs59ZbOtrwSG8vV7gl2SLrkABZxTjzIkUcAIkpit6Ge0ROaRvnvuvJzMzjytzWuApsUDSB3nvduZaToY7xI0MjScHNT0uf_ohHwwG_ZkaTuA61XW9drU4eF-gKru84UwWbZSTt1JZOkDu3Qo1bIzQ5AxXdKRF0y4nEBKJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
اگر عاشقی کنی و جوانی
عشق محمد بس است و آل محمد
اینستاگرام هیئت قرار را دنبال کنید
👇🏻
👇🏻
https://www.instagram.com/heyate_ghararr?igsi=YXZnNWZhaHRycTlm</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/685389" target="_blank">📅 21:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685388">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992b33ce12.mp4?token=QQG27vifPhN8cVZ-lue3CMu_oh8xnq4t4zXJs1HuqM0pGXMwFeyvaKXBpsffQeyll1OD_Z7NHsFxGPNEjB1GJCCZmXoZD9HHtNmPUUQpCF43_TmsT1DghmhPuvjzDA1mSIJ0abbc5SjUkb6kOq7r0756NUiIBGYWN_VCR-iftbxfEL-no9zKW1hp2dF9klpQRVeLUURIe8bSnvi3Kygy68V1MZkOvcJaBI_k3DHSIDCnAVcYNoukq7H8UnrRfCGy628VjfF9uy2QFrcWbfQbvHaJaWjAIqBG6it0SKKO0nJQcmFyYImVaF3exmQrEb1WpWbVEAvnYPkCv0kzXaX2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992b33ce12.mp4?token=QQG27vifPhN8cVZ-lue3CMu_oh8xnq4t4zXJs1HuqM0pGXMwFeyvaKXBpsffQeyll1OD_Z7NHsFxGPNEjB1GJCCZmXoZD9HHtNmPUUQpCF43_TmsT1DghmhPuvjzDA1mSIJ0abbc5SjUkb6kOq7r0756NUiIBGYWN_VCR-iftbxfEL-no9zKW1hp2dF9klpQRVeLUURIe8bSnvi3Kygy68V1MZkOvcJaBI_k3DHSIDCnAVcYNoukq7H8UnrRfCGy628VjfF9uy2QFrcWbfQbvHaJaWjAIqBG6it0SKKO0nJQcmFyYImVaF3exmQrEb1WpWbVEAvnYPkCv0kzXaX2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشور: تفاهم‌نامه اسلام‌آباد بهترین توافق تاریخ معاصر بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/685388" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685387">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR2e0ipjQAMpv6XERjYQ3ccJ13pVcjQ4ZvEEJHjlGeinD29VE5iio2yW-h_lvM8UCw2DUtJiGm1iJ0tqn5D24u4i-4g0opXzCMuAhh9e0mxfG4_a-Dd-XzRrGHI_wkPHgdE4gHtL-iPpklS9OtBvcEYTklitdBwy7CI-iB9LwRO6topXLc6ywI6aOMT7eJpWYK4oOW1kzsKYdJuXATNLHXtbd5IfuR2Au82ClJ06mHlhcljdXEiEIdzND8IN78Gi_eva87ETwvBEp1qGH909GbxrAML4Y8d_q3N9pkjF_2GtR2QJ6E4xzGpVAsx4g1T6S5-CqquEACr9O8zIuH45hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت صبح فردا مصادف با میلاد باسعادت پیامبر اکرم(ص) و امام صادق(ع) همزمان با قرائت در اختتامیه کنفرانس بین‌المللی وحدت اسلامی، منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/685387" target="_blank">📅 21:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685386">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvAhpo5E83TPGmVfbsUg8yOHLbXp7Q8Yhfzkv_7a003fln-gwEVq0NXbCdhOpXBUUsWWBwPFPBAZDaDsfK1-B7Akmy0HTTGaMStmIAsW2_DtcGPqn5gBJJRpgvU36YigfqbG5E69_3RXGmDcuu1MP9jbK_hWxKJakJXgTXhdKQ6BeLW2K2iCknIJmUtCsh9OCShkj9hdxdzG8DLtL_pzLBiwtusNCnPclhFyuO4c-oZc-skychiQnCJYbWovrJ8Kcy2d0bPYICd9xDo2smfP_dnHwXyJxMkZwxQUMOuxHC22hcZUyXwCRabBHq_ACTAw07j9z4q7gluCUNlILv5JEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرسپولیس قبل از دربی درخشید/ بازگشت شاگردان تارتار به تنظیمات کارخانه
🔹
تیم‌های فوتبال پرسپولیس و ملوان در هفته چهارم لیگ برتر امروز شنبه ۷ شهریور و از ساعت ۱۹:۱۵ با قضاوت سید رضا مهدوی در ورزشگاه شهدای شهرقدس رو در روی هم قرار گرفتند که این بازی با نتیجه…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/685386" target="_blank">📅 21:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685385">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4StMquAmCDj4ik6lzjiTNJmzq94T1LSGYjoLDXPuautC4h7m0EpKF1gTk4IwMgi8g3T4HTCVfGoQIfPZYW9BmIyp5Hofa-cQNy0yTrN2FMWQx4SLgImkhm_k4yCYWexxCeP0NfNFbGUIQ-ZWGR1AOolaFx5saFS9ulhfEx4O_w9uFbYlXElrD6QoDe1_RxVXSnH8DFApWYYsAmWGDuRT8SwchTIoOnks-ZIaJzX9lSMCGvRKhR4xAXS5IxeeYXI0vAWj_TWrev3_hIzm9S7WrgRxiHJyXJ4681siHcuvth7iTzq5Yi962HWnhs6XMOhhB3S5hUl7itU4xO13C57uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریچارد ژئوپلیتیک و سیاسی: خودکشی یک هژمون
🔹
جنگ ایران به عنوان یکی از بزرگ‌ترین اشتباهات راهبردی آمریکا ثبت خواهد شد. آنچه به عنوان تلاشی برای نمایش قدرت ایالات متحده آغاز شد، در عوض محدودیت‌های آن را آشکار کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/685385" target="_blank">📅 21:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685384">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx2Unt0f2zKnWA4TRPqszE3vptIFJvmEfnhzLQho3FiYQika0i0rN-YY_rJ6WFzJPxERvRtmd1xP8wztgXRujrdoE1u3dtOr0M01A0gkMdLGbEKhDO_Ow1PWxnKTAh58NZTq_dd6Q5xgfWgFuyjW94UEIND6JK9DX_3Cc_uQCV90YJhrLv6OlAeXCxDmaja3yTu-JV_cILEGELVh68SmAapPXooAAHcxo5Ves-mDiAo95ASWwr0PmXqcaswJC3eLGswPVhZIxA_gEsa97cknF8pkziL_KbsZ4Ek3jjZlL6jEAuuI97gw9bBjj2rSP47vdM1vuHX92xagOcmg9sW_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
باراک راوید: دو مقام اسرائیلی می‌گویند ابتکار بستن تنگه هرمز از سردار علیرضا تنگسیری، فرمانده وقت نیروی دریایی سپاه پاسداران، بود
🔹
در ۷۲ ساعت نخست جنگ، ایران اعلام کرد که تنگه هرمز را می‌بندد و هشدار داد که نفتکش‌ها و کشتی‌هایی را که تلاش کنند از تنگه عبور کنند، هدف قرار خواهد داد.
🔹
اما به گفته مقام‌های اسرائیلی و آمریکایی، سردار تنگسیری در پشت صحنه دستور استقرار مین‌های دریایی در «طرح جداسازی ترافیک» (TSS)، یعنی مسیر اصلی بین‌المللی کشتیرانی در تنگه هرمز را صادر کرد که وضعیت را به‌شدت تشدید کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/685384" target="_blank">📅 21:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685383">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
دولینگو (معروفترین برنامه آموزش زبان) اعلام کرد آزمون‌های این برنامه از ۱ سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/685383" target="_blank">📅 21:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685381">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESw1tpLYlmNfRfvosPMSn-2p_D2g7il38U3XGx9liSrQPd3kp79JQtXoPHVFRTYdDjPset4VUn-6drJbVktITDRmwUo5roB4Itrde16qsKpV-32ySmVJBA6VTWXMPUfEkBfYS-qsTAVkOKIEAPno0Hxr8iCFMxVscPVFTE7SNGsiUpJ6hb3p0ohWwZFJcaggGPtFG3SQjVeyfrez88le9qoQa1k2rDr7NdXvLtFYzYn-L88ViH497SA1AFPmXecsKldIwzalakgHre8O4WjC37P37QrIhyix9e9bZ9VDuKj65kWyWXzLVYok-FnfTGyGgQunj-cxDw6-8oEFitUjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل سوم پرسپولیس به ملوان توسط علی علیپور ۵۶
🔹
پرسپولیس ۳_۰ ملوان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/685381" target="_blank">📅 21:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685376">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZMl1xtxyL2xcv2bd_sFvDmzON7GJNwACNXKNVdbq37bGageln2plwJhYNn6soRgdLmwMvv9vyNym3kjlxDvjtnJN_qDHT9ocdB4KPFlpbtxrAIfG1gzRCJ5Eqm1EE_0zM4MfZS-e9bFpeYshuneiIODfY7j4XJR3gbmGoup5bO_n6WB_nIkMBe1KRZWkNfyxetD_D0ENwMf6cZSy3PrawAk5mkfKYVW1Ao5O1q6UYhBXNJcAOxjdXtBeUUUJuQY3zDsWmKeI_IykN-k7kuxEqc4D2NCvOh_CuOcH7KyaB3nNVfbUzZNqwRnXbLILhtyI_9dUBePgL7XPbKOUkMCDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLtvjI4PllOQ596NKKcgCKyZFmHtWRGOC6QF9-kcfoMVxdnNwvhKxdUEsLAtcqjDe8-sn2CyOuE41TCZNcczasbGZoRXkOzsu6e1GIuR4QR88XnTB0RizaM4jHwyFNcHxHSewXXVuZSfIEz5JUlwwPlAnJKLaf5zyrdk2jH44arb5Wd5Wie54iZQUAKsO5d6aFBU78IvTcimyHI_EA7EeQjqESoC9tNu1C3UVQ3Yuc4etePSHYeOrrNCtnP9b1WNmzYDOZD_kfjFqSteHnAtwwSg631AJlL981VBMi7DfsPDnPwsPBursj2RZimVx2PDKdx7bYEjCV7T9RvfgC_k9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیگه با کپ کات یا اینشات ویدیوها رو ادیت نکن، چون هوش مصنوعی واست اینکارو انجام می‌ده #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/685376" target="_blank">📅 21:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685374">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHQ6RWuemk9tUlDgcpGaruaRruPlvPnTk6-qtbznUfXxOJZ4Qx5STpsdTY--4vRXLEeIBIugfx7SgJDrwnPnEVYagBDxRlTYt0ENCsXrMx6vwuhShbDzEtAK1vylEZ3zsSIxohFowVf3JwBWrmoNjvY1CmoCRbUvB5WpLuXkyh_wm7SOKNlMR0Tn6tyru8k9PF2tEwD9meNwJGmOXKjO_M-dGTa2w5v5yZLZFPdoDAIFH3d-jZ9r9KmPW75lZTltQz3MdBcw1NaP5KbhF7wTHWlrNrA_H0-YrYZtjT8JSEQl2I_hOpwzx8sOGcmelo8ovGSvR_uIR3A5UIZRcXFg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ایران قوی، ایران علمی
💠
اعطای بورسیه تحصیلی و صنعتی دانشگاه بين‌المللی امام رضا علیه‌السلام به داوطلبان سال ۱۴۰۵
🔹
ویژه داوطلبان کارشناسی ارشد مهندسی برق
🔹
ثبت نام تا تاریخ ۱۵ شهریورماه ۱۴۰۵
🔰
جهت کسب اطلاعات بیشتر در مورد شرایط و نحوه دریافت بورسیه با شماره‌های زیر تماس بگیرید
👇
☎️
05138041 داخلی‌های 1421 و 3108
🌐
imamreza.ac.ir
🆔
@publiciriu</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/685374" target="_blank">📅 21:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685372">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG-dgo1jKl3xYwjG7l5DhU51jTXUi-qCiTWdvz_qz8VCmp6HJwE46OyR5T2t-wMv8o1CFYIZi9mPl2p3ycoODdZnImhjvg_z-70bUX8mtzjz8eNSULvmXFclAs01SmOuI_pPd4CdqZLB2piRzNB6LFHZDd9rk-DgwGkjdyNPWy6DcskiK-KKbQ2Gf82oo8jnl0hEARdKl7sjW9EdQDYWmJU_EjZkTR1ghm8FlGqhiRbJXbjvnmpH-pVOnF6nAhYqZGB7IlN6A06yTfp-oiL6nLtxs0aNVA2NNr5pYmzeJvxv5kIJSK20fY9uqRIXY8v6zlPqnBIa8THA73Z4xPyEBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه، به‌طور کامل بخشیده می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/685372" target="_blank">📅 21:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685371">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f5fdf48.mp4?token=CXvsOkHAKkb9ZPeDj_f3FJYB8_TpOVg0INzLNCMCxHyycDYb7whZyx4y9aYPvUsWUZPM_KbszAMzeN7EbW4d-8Oqf--es2w_grG1Av3h19IJ7oBkTiq5IqCtUNLgpYY_EmG7xyIzIHLZqtpAfDkcBnaxifWzFPno6lXcw6PIN-Kc4wo29n9LBym0-USAXnRvXFVQ1KEHCn_POxUF79AUffMCvX_XBsy8xCKWxIBHhrfvJ-C1J80baNR9gDXjV8kOxFD2aiSe5KFM3OfQnVeUHDyo4b-NjzTFI489Ek3_IBoGZVolGG4rrzarjJcSVIsqBW9E73CG2pmHvRDlj4F0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f5fdf48.mp4?token=CXvsOkHAKkb9ZPeDj_f3FJYB8_TpOVg0INzLNCMCxHyycDYb7whZyx4y9aYPvUsWUZPM_KbszAMzeN7EbW4d-8Oqf--es2w_grG1Av3h19IJ7oBkTiq5IqCtUNLgpYY_EmG7xyIzIHLZqtpAfDkcBnaxifWzFPno6lXcw6PIN-Kc4wo29n9LBym0-USAXnRvXFVQ1KEHCn_POxUF79AUffMCvX_XBsy8xCKWxIBHhrfvJ-C1J80baNR9gDXjV8kOxFD2aiSe5KFM3OfQnVeUHDyo4b-NjzTFI489Ek3_IBoGZVolGG4rrzarjJcSVIsqBW9E73CG2pmHvRDlj4F0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان سرخ در حمص
🔹
طوفان و گرد و غبار قدرتمندی آسمان و اطراف شهر حمص را در سوریه سرخ کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/685371" target="_blank">📅 20:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685370">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/276adae82c.mp4?token=j46kau0oT3EXbrft7Favh5r-679BC_ebzRqFcQYtuYIhEQ74_GAoHSZx9HZwlkoYEwbuA086Rq6oGw9wOuqJAvqMz3OoBgYVXoBIn_sxI7shnZ8od34lUBL6elJufh99YCPpZDUlO_GixITq1rjlYpwmnUPLoEMq8X5X7u2DBpdrcCk2zjby6dkiZYXbHncyjPx2jFb7Xm47qCpCSmFWcxUuZj3QPoNFaeRRGSgoRlrvCabVs0goxE7LE3r-Z_D4qZlfI3eEM9Mnb3M-PIhmBDmSiRIPPFBvimIQp0cuWWqZ4O4aPXSeqxqwR40xFzdITQeAFBArb2pObf30R9JKiahB9EdxQ5Npc1jMl-kQUt_dXqMt1TRB6sr9lvRhBXd8xaZjKabbU7xhRoDbmcEoYV2NaX4hxejx9l2WGee0973l-DatZQRajDIHesCWoxMuKjF9KNbQZDejl91KKM_2rXW-0DMwhZUBY_PAizF0pvE_Iuw6QLlySvhMreMf7zrH4SyADkgFocPdokvSbcsMffgsMP28tVeFPin6OBcDXysH-Gqj6p7XGDeGr_8eTtzH8ootVs9mlI10zykZ17R1eRRdU0mXvhoFoEFt2YjNg0MesuKlBUs_T1IyiLG1ArhspIxAwPy115PcJodDE2KDudHB5Z455Wa7DM_3zbg7sVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/276adae82c.mp4?token=j46kau0oT3EXbrft7Favh5r-679BC_ebzRqFcQYtuYIhEQ74_GAoHSZx9HZwlkoYEwbuA086Rq6oGw9wOuqJAvqMz3OoBgYVXoBIn_sxI7shnZ8od34lUBL6elJufh99YCPpZDUlO_GixITq1rjlYpwmnUPLoEMq8X5X7u2DBpdrcCk2zjby6dkiZYXbHncyjPx2jFb7Xm47qCpCSmFWcxUuZj3QPoNFaeRRGSgoRlrvCabVs0goxE7LE3r-Z_D4qZlfI3eEM9Mnb3M-PIhmBDmSiRIPPFBvimIQp0cuWWqZ4O4aPXSeqxqwR40xFzdITQeAFBArb2pObf30R9JKiahB9EdxQ5Npc1jMl-kQUt_dXqMt1TRB6sr9lvRhBXd8xaZjKabbU7xhRoDbmcEoYV2NaX4hxejx9l2WGee0973l-DatZQRajDIHesCWoxMuKjF9KNbQZDejl91KKM_2rXW-0DMwhZUBY_PAizF0pvE_Iuw6QLlySvhMreMf7zrH4SyADkgFocPdokvSbcsMffgsMP28tVeFPin6OBcDXysH-Gqj6p7XGDeGr_8eTtzH8ootVs9mlI10zykZ17R1eRRdU0mXvhoFoEFt2YjNg0MesuKlBUs_T1IyiLG1ArhspIxAwPy115PcJodDE2KDudHB5Z455Wa7DM_3zbg7sVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحدت؛ توصیهٔ رهبر شهید که رنگ عمل گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/685370" target="_blank">📅 20:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685369">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVFb4Ik943PXeBYb-WpK0v7ZPbENwk1loVRWNFSae-Zl215fehymGOeCEmfPUmO_AvUVVwTBphP1FoDyY9J0UA-oNBkK7gyrjMjrKu_X3Zi-gO2ffqQnLMegYQ4EcxYQaC8VIE0zR4hLItEcd6yKDUAWwZ4VhC_CMdMUucA4XFSn3hON_-EBHw5fAPXdODV9-T3QvG7wpktd1rDXTNul4XNSUssdZAPsaeC91fktqesHNHeQuEw-2kyFf4V5FkDdW6Qbk9Ml4JcaqCRBBJGDfaXh99jisnWKBxWROe7jg4rTQYrdchPGeVz4LvSr-KzPKRmJaMHvvJn6JEncXnDtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری این‌بار از نزدیک با شماست
✨
🔹
بیست‌ونهمین نمایشگاه بین‌المللی الکامپ، فرصتی برای دیدار، گفت‌وگو و همراهی با تازه‌ترین جریان‌های فناوری و تجارت الکترونیک.
🔹
در غرفه خبرفوری منتظر حضورتان هستیم...
سالن ۶، غرفه ۳۲
۹ تا ۱۲ شهریور
ساعت ۸ تا ۱۵
نمایشگاه بین‌المللی تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/685369" target="_blank">📅 20:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685368">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef114bf55.mp4?token=qDiIOysZWtfM3TyNxLfCAMzmM7QeEpoukCypE2zhke3dPbLqjMc2PLAzHB5Lyvezt4DGds3hVQiahjK6F8CmxR8wDQAUlS07C9C8YzqYIB6QiHu1E6OtWdxU0S3in_J2SedkF-k5_8S5ms6BgoUHLfCdDgsgK0g1YwbgGGX_U3P__Roq8ZQC4nOex9Kl-6Z8JRUs9_nN8409LKDKwRy1m67cvbnoqj7SLzvKln6AaOokoyLUzTyWGH_TMF6Sy3MsTBWnAOkWGfaSo-PdwQVqriKsnfVMVhYgVVIm0IgivEO82o3IdtLH2TNc8d9mi6i5qmhgyUigHgfnFgi7PA5Vaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef114bf55.mp4?token=qDiIOysZWtfM3TyNxLfCAMzmM7QeEpoukCypE2zhke3dPbLqjMc2PLAzHB5Lyvezt4DGds3hVQiahjK6F8CmxR8wDQAUlS07C9C8YzqYIB6QiHu1E6OtWdxU0S3in_J2SedkF-k5_8S5ms6BgoUHLfCdDgsgK0g1YwbgGGX_U3P__Roq8ZQC4nOex9Kl-6Z8JRUs9_nN8409LKDKwRy1m67cvbnoqj7SLzvKln6AaOokoyLUzTyWGH_TMF6Sy3MsTBWnAOkWGfaSo-PdwQVqriKsnfVMVhYgVVIm0IgivEO82o3IdtLH2TNc8d9mi6i5qmhgyUigHgfnFgi7PA5Vaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: حالا فقط یک اقیانوس کم دارم!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/685368" target="_blank">📅 20:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685367">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e809ca549.mp4?token=DH3ptzF5SO4WT7AVHh7kDNkgrXfv53bLnqFgypWRaJAYAsPNuwWWcHMSZCYzZwPtE_mpZVJkAwyWu4PNl3oVHPenNukZUwZcwM9o5i1nJm1wnYELdC54Hm7oioj8Q1XjuTJKo7-jMm_DbT4AvCGA71Wrm3jD0j8_Xnhz5Xk_Puv1HZdTFaClB8jkZ_mdH-iOHJFWorcKxW7856U4pkVJrj8jRDDD2w6LQYlbKuv6jCN-HS9XJdA7FcnHtiify4r_lmnNx09WjGXro6Ho93K9DsTH-LTqesg2HIDY3akEEXx-Wuak4Ug_5QWePc0JEzToY3ZZHl451QxvoKbmzrLuF41shyP3yq8OpM4BVnBT998-qfMdJg8B9jCSa5HfR6esPTkDshXKJYUE4oybe2gsIHBqACURun0jkEo3tlgZxF8f5CPCJeTva6aFrQrJkDc3sewKCmWWByJX1h_IeIVlzvX2gPGD7h9XvJEtOp-cKwUBGB_Ru7rodxVL6afeYVl0m_9cj_mtQBJffv2_dy77UzyTdgY4iTEInLZloKJmbXdbo4T3cf6s7K4YstaGXIkuN7UV34EVx3Au-cf2e3002UVpUnnqLb6cK-lorseilBTXohDnNasgyCM8Kgu9Toath0jKXmDNGDzRm24CtAMg_-3i7oUjKFi-0rEb8LEI2PM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e809ca549.mp4?token=DH3ptzF5SO4WT7AVHh7kDNkgrXfv53bLnqFgypWRaJAYAsPNuwWWcHMSZCYzZwPtE_mpZVJkAwyWu4PNl3oVHPenNukZUwZcwM9o5i1nJm1wnYELdC54Hm7oioj8Q1XjuTJKo7-jMm_DbT4AvCGA71Wrm3jD0j8_Xnhz5Xk_Puv1HZdTFaClB8jkZ_mdH-iOHJFWorcKxW7856U4pkVJrj8jRDDD2w6LQYlbKuv6jCN-HS9XJdA7FcnHtiify4r_lmnNx09WjGXro6Ho93K9DsTH-LTqesg2HIDY3akEEXx-Wuak4Ug_5QWePc0JEzToY3ZZHl451QxvoKbmzrLuF41shyP3yq8OpM4BVnBT998-qfMdJg8B9jCSa5HfR6esPTkDshXKJYUE4oybe2gsIHBqACURun0jkEo3tlgZxF8f5CPCJeTva6aFrQrJkDc3sewKCmWWByJX1h_IeIVlzvX2gPGD7h9XvJEtOp-cKwUBGB_Ru7rodxVL6afeYVl0m_9cj_mtQBJffv2_dy77UzyTdgY4iTEInLZloKJmbXdbo4T3cf6s7K4YstaGXIkuN7UV34EVx3Au-cf2e3002UVpUnnqLb6cK-lorseilBTXohDnNasgyCM8Kgu9Toath0jKXmDNGDzRm24CtAMg_-3i7oUjKFi-0rEb8LEI2PM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم پرسپولیس به ملوان توسط علی علیپور ۵۶
🔹
پرسپولیس ۳_۰ ملوان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/685367" target="_blank">📅 20:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685365">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2512adc8b.mp4?token=kG-f_H5hxBfTeQpL2UFncNKyicPd93JrW0uDcDeF9Z9YEJ9bD44L250wSUE1Wrbd_L_uNPQLa_cmIiEuOV7IWYDZqDQ5-NZJpo2ph02NP3ScaULgML8T-9A3nC3mWdyYzNKCxoaz0rPRTFtkHg8GHvNLGJcEVTG7bNQ_sZxeZTjWBmi_qtwONbQlAqZXMH8xnhx18uSryq42aRN3EVm5jjuqR5Tl1v7E2-zDP9A4wEe0fllFg9sTr_GIu2Am_zi5QVhhCN0m7AVcMHTg0K7lhg285y-_zTbtPIuYTQNG7_peprnK73OZTnDFVowe1kWtEsZ2tpiCvbfa9SN6R3eMow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2512adc8b.mp4?token=kG-f_H5hxBfTeQpL2UFncNKyicPd93JrW0uDcDeF9Z9YEJ9bD44L250wSUE1Wrbd_L_uNPQLa_cmIiEuOV7IWYDZqDQ5-NZJpo2ph02NP3ScaULgML8T-9A3nC3mWdyYzNKCxoaz0rPRTFtkHg8GHvNLGJcEVTG7bNQ_sZxeZTjWBmi_qtwONbQlAqZXMH8xnhx18uSryq42aRN3EVm5jjuqR5Tl1v7E2-zDP9A4wEe0fllFg9sTr_GIu2Am_zi5QVhhCN0m7AVcMHTg0K7lhg285y-_zTbtPIuYTQNG7_peprnK73OZTnDFVowe1kWtEsZ2tpiCvbfa9SN6R3eMow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکرار نقض چندبار اسرائیل این بار
با
حملۀ رژیم صهیونیستی به یک مرکز نگهداری سالمندان در لبنان
رسانه‌های لبنان:
🔹
رژیم اشغالگر اسرائیل یک مرکز مراقبت از سالمندان در شهر حولا واقع در جنوب لبنان را منفجر کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/685365" target="_blank">📅 20:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685364">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
منابع آگاه به روزنامه «الاخبار» وابسته به حزب‌الله گفته‌اند که نبیه بری، رئیس پارلمان لبنان، اعلام کرده است از جوزف عون، رئیس‌جمهور، و رودولف هیکل، فرمانده ارتش، تضمین‌های روشنی دریافت کرده که بر اساس آن‌ها ارتش لبنان هیچ قصدی برای تسلیم شدن در برابر هیچ‌گونه فشاری ندارد و ایده رویارویی با حزب‌الله در دستور کار نیست
🔹
گزارش شده است که بری و عون روی توافق اروپا و آمریکا برای حفظ یک نیروی بین‌المللی، حتی اگر صرفاً نمادین باشد، حساب می‌کنند تا بر اوضاع جنوب نظارت کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/685364" target="_blank">📅 20:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685363">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80057e224b.mp4?token=XcCN9L7n8onutt5ZcrRDQqBjOS_8njLU0YdPA15-BPFJUY_d6hJCpbrvpXUyRMNgMGL4LjoOgVP2NFlGTMHADIVFJxdwDRwzW8Z4DmWVYErf8M9gTNSJx7s3s78QOfPQKmzFmKb7GHKip5-bHaVoxaj2sHoWs9legssXZ00lEB51WULbFNF0NPQsVSy4CXZ6M_jDNh-ZScg7eaM5gVxv0utZHJ4araMdylk54MRnBReCcB0ZYBTP3NusLlAGdhLNLy0V4jyUD2Mosx-BNXwB3tWq174DCQqBWvTgGrpQBtpBCVB6DTYEXDMKiJbrw6_VipGLJpPVTWOPzF6ahUyuGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80057e224b.mp4?token=XcCN9L7n8onutt5ZcrRDQqBjOS_8njLU0YdPA15-BPFJUY_d6hJCpbrvpXUyRMNgMGL4LjoOgVP2NFlGTMHADIVFJxdwDRwzW8Z4DmWVYErf8M9gTNSJx7s3s78QOfPQKmzFmKb7GHKip5-bHaVoxaj2sHoWs9legssXZ00lEB51WULbFNF0NPQsVSy4CXZ6M_jDNh-ZScg7eaM5gVxv0utZHJ4araMdylk54MRnBReCcB0ZYBTP3NusLlAGdhLNLy0V4jyUD2Mosx-BNXwB3tWq174DCQqBWvTgGrpQBtpBCVB6DTYEXDMKiJbrw6_VipGLJpPVTWOPzF6ahUyuGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرسپولیس به ملوان توسط تیوی بیفوما
🔹
پرسپولیس ۲ _ ۰ ملوان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/685363" target="_blank">📅 20:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685361">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سازندهٔ چت‌جی‌پی‌تی شمشیر را برای ماسک از رو بست
رویترز:
🔹
اپن‌ای‌آی قصد دارد ارائه مدل‌های هوش مصنوعی خود به «کرسیِر»، ابزار برنامه‌نویسی مبتنی بر هوش مصنوعی که اکنون تحت مالکیت اسپیس‌ایکس قرار دارد، متوقف کند.
🔹
تصمیمی که بار دیگر اختلاف طولانی‌مدت میان ایلان ماسک و مدیران اپن‌ای‌آی را به کانون توجهات بازگردانده است.
🔹
این شرکت دلیل تصمیم خود را نگرانی دربارهٔ نحوهٔ استفادهٔ اسپیس‌ایکس از فناوری‌های اپن‌ای‌آی و تجربهٔ قبلی از نقض مفاد قرارداد توسط برخی شرکت‌های متعلق به ماسک عنوان کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/685361" target="_blank">📅 20:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685360">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e66bb35c.mp4?token=k0BHE4gTO-VFH8B5pwglo7NBXazUSUa3k6Fq39Y_7AS2yP44zdZpf-fjN3HA9r0LrJzGA5oIgMiG1dv643UZd4Iv3snxHi7ertulJjOXjMiKa5soM0ljtZpntIXbKxYjSyMw6vPuk8gpI0XgbWSSFdjxmO2SsisYdkfai2HSG8eTXhRHetp5Zw-M6ZxvBulDLVECM_1CLY_cNDHtY9RcOYkOVB_rVqL2xOyq52UL2J3SVUaslOu4TEf-RY-gVnWV_HsskqBBm_lAYErbS_3zjUltepxRXbYL4ssZkjuL0m13flAUxiSVBXSJ_2Px7LFaF4pClWbLc8RjLdUpWDtkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e66bb35c.mp4?token=k0BHE4gTO-VFH8B5pwglo7NBXazUSUa3k6Fq39Y_7AS2yP44zdZpf-fjN3HA9r0LrJzGA5oIgMiG1dv643UZd4Iv3snxHi7ertulJjOXjMiKa5soM0ljtZpntIXbKxYjSyMw6vPuk8gpI0XgbWSSFdjxmO2SsisYdkfai2HSG8eTXhRHetp5Zw-M6ZxvBulDLVECM_1CLY_cNDHtY9RcOYkOVB_rVqL2xOyq52UL2J3SVUaslOu4TEf-RY-gVnWV_HsskqBBm_lAYErbS_3zjUltepxRXbYL4ssZkjuL0m13flAUxiSVBXSJ_2Px7LFaF4pClWbLc8RjLdUpWDtkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر بالگرد چینی از سرچشمه سیلاب مرگبار در مرز چین و نپال
🔹
یک بالگرد چینی خود را به نقطه‌ای رساند که در آن یک یخچال طبیعی فروپاشیده و حجم عظیمی از آب آزاد شده بود.
🔹
این پدیده که به آن GLOF (سیلاب ناشی از طغیان دریاچه یخچالی) گفته می‌شود، یکی از خطرناک‌ترین…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/685360" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685359">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTLeGbHucf1R0a4hAoU2qRdP7f3FeTzZCtX27qA8UfViTiIRH2HvZHzAsmEebA5wgI_SC-dAPbb3yx6Mo294Q4iPTuwf7YN8dBkJfNRYlvWH7y1LHL3XzYPyZ_l8u9IZOTG3AugQ5Dm9tRs_6pfYqBO9nT-Q7FqWsXDILcv1EXg72ZL27T4eUapINH5syyJ1qsOn7s8dkrhPbTqOCP4DjIFIaCW8LbMFpnCxVVJvAKj9_vge3gAw5Qbk1nBd6wnOrI1rIP_tVY2iGPf4S5K3uporoRF0V0scbYnfXlX_dfHJcrtCPIVQbvAOZbWIUxYB6EEB48AE2GlsKL4KZMoo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روغن، رکورددار تورم نقطه به نقطه مرداد ماه ۱۴۰۵
🔸
بررسی آمارهای تورم نقطه به نقطه کشور در مرداد ۱۴۰۵ نشان می‌دهد که اقلام خوراکی و پروتئینی بیشترین جهش قیمت را نسبت به سال قبل تجربه کرده‌اند.
🔸
در این میان، گروه «روغن‌ها و چربی‌ها» با ثبت تورم ۲۵۸.۲ درصدی در صدر رکوردداران گرانی قرار گرفته و بیشترین فشار قیمتی را به سفره خانوارها وارد کرده است.
🔸
پس از آن، گروه «شیر، پنیر و تخم‌مرغ» با ۱۶۳.۷ درصد و «دخانیات» با ۱۶۰.۹ درصد در رتبه‌های بعدی بیشترین افزایش قیمت جای دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/685359" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685358">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4508efc7.mp4?token=QGC4VKL5p2bchAdtDPlYwXABbNZGPw0FLSbv9euMyukYGv3Kf0UtviGZTQOg00Jis9qPCAQLCas00FJ-8eY0uydN_x2oRd3xM0E-Qg8N80Ot7Pg2Vh-Cm7pC2G_HHPhum4G6TCZ2bk0uwwsCGv9GnCUKTgLbhSK-qp3HQRwYKu1ZnChuHszqs9jg_oYUp3R_6E5mzfw8sF0h-ZF6Mgy2OW91fu_78DVjmHIuqMuap2F3oUqAsdQGAj2ayC9FkyVPSdRbapFMubQpoEJaP-uKNoTltlABRKz7QtqxiZ8C9Jf7NQIQps3k7eMcRvUQaelN6iSSLQmXgLV9K9YWLSUy5iEpUnRsVkHISj4frZhZDDVAuU4ZfEL8en_v2ABaap1IQf_MlqqO2nSp5BcLCFxE1czgDcu54LOmL8U7wxqEj3ul1jN_2dIn7Qwgfm1Md_wfYJi1dIIYZFOD5NNG9wNQAkDudNFFxlaZYALZjTslR6K72HiFU4LicgauprHZ4EE2DiHrzTzjD9hDajzAgkfGumZMQ-QbsFQSTIFM8-1pi46_uZYwIHZVVU3O1ZhP4QFoRQsgNVsF_za2V0T1wkjRCOk0bPP4vO9oBE9RbmaQp8RtHKB-c9eIRr2c3hCG6rA02MSMFhoemUMVlndaHgSMf4YqYrbXLqpT-FpNbfjt7ec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4508efc7.mp4?token=QGC4VKL5p2bchAdtDPlYwXABbNZGPw0FLSbv9euMyukYGv3Kf0UtviGZTQOg00Jis9qPCAQLCas00FJ-8eY0uydN_x2oRd3xM0E-Qg8N80Ot7Pg2Vh-Cm7pC2G_HHPhum4G6TCZ2bk0uwwsCGv9GnCUKTgLbhSK-qp3HQRwYKu1ZnChuHszqs9jg_oYUp3R_6E5mzfw8sF0h-ZF6Mgy2OW91fu_78DVjmHIuqMuap2F3oUqAsdQGAj2ayC9FkyVPSdRbapFMubQpoEJaP-uKNoTltlABRKz7QtqxiZ8C9Jf7NQIQps3k7eMcRvUQaelN6iSSLQmXgLV9K9YWLSUy5iEpUnRsVkHISj4frZhZDDVAuU4ZfEL8en_v2ABaap1IQf_MlqqO2nSp5BcLCFxE1czgDcu54LOmL8U7wxqEj3ul1jN_2dIn7Qwgfm1Md_wfYJi1dIIYZFOD5NNG9wNQAkDudNFFxlaZYALZjTslR6K72HiFU4LicgauprHZ4EE2DiHrzTzjD9hDajzAgkfGumZMQ-QbsFQSTIFM8-1pi46_uZYwIHZVVU3O1ZhP4QFoRQsgNVsF_za2V0T1wkjRCOk0bPP4vO9oBE9RbmaQp8RtHKB-c9eIRr2c3hCG6rA02MSMFhoemUMVlndaHgSMf4YqYrbXLqpT-FpNbfjt7ec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله نظامیان صهیونیست به خبرنگاران فلسطینی
🔹
نظامیان صهیونیست در حین تعرض و یورش صهیونیست‌‌های شهرک‌نشین به بخش قدیمی شهر الخلیل، به خبرنگاران حمله‌ور و مانع از پوشش این یورش شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/685358" target="_blank">📅 20:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685357">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5cd16df0.mp4?token=NtkN2OPhK0j2YhfPCQeCDkewAD5XKhrYE08IKuPlNhoh3dr6oJ71_i3uePEWG6B5xU_MQEcnqcolJEuuv_QOpSd6dnn6ttG62-vv5a25OGvaARCFZ-_YTQgm3A2no7JnLqlvHN2Yj59y7tisW4QFIlE-u-_IGJLpyyihoFIHRDqOgleOUuq2JjE0vwl0VVOuXanOSyn4yB6IXGP81BR8r1hjfGhrKUTqluof04XNseO_TMk2Jyb9eBQMOk-N6vsZtoE4pomrB0WmxG-kwm-7rvf3FJa4Ek1hbVItLEzgI8PJ4G3gr6UtfX9byK0Zrt0riWaFDN3xXKtkndcUYFaPwJUGmCSyLX5wnGeHYtIx2voVK0fxy_l9RTdkjWgKHCnneCGJc6wT192bzmLD6Roa5XJXepKtjn7sjdAC2ekbQU623nmhiSb6qXWwIZsXcITsNIHcLxrWjGmMiP-FIwKvLoYBxPVRd7SM8ahuw3nHTLcyWYrMgW0Wl_VGNaEoBVPKkXYNYr2PZm1-smAc6B_g5LNAOJzybV7Dsw5pU4UtYZoO0zsqNvfF3UsKXKTXtSXtSEK6mD55g8G8_rAhongC7fuZ9T2rotKidGLrrOoUckao7jJXQKWIvLbm526zGCf42o4SsgztlSvpEe-tjC5OsmfJ9uyyg2oa8S4FDHjxQdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5cd16df0.mp4?token=NtkN2OPhK0j2YhfPCQeCDkewAD5XKhrYE08IKuPlNhoh3dr6oJ71_i3uePEWG6B5xU_MQEcnqcolJEuuv_QOpSd6dnn6ttG62-vv5a25OGvaARCFZ-_YTQgm3A2no7JnLqlvHN2Yj59y7tisW4QFIlE-u-_IGJLpyyihoFIHRDqOgleOUuq2JjE0vwl0VVOuXanOSyn4yB6IXGP81BR8r1hjfGhrKUTqluof04XNseO_TMk2Jyb9eBQMOk-N6vsZtoE4pomrB0WmxG-kwm-7rvf3FJa4Ek1hbVItLEzgI8PJ4G3gr6UtfX9byK0Zrt0riWaFDN3xXKtkndcUYFaPwJUGmCSyLX5wnGeHYtIx2voVK0fxy_l9RTdkjWgKHCnneCGJc6wT192bzmLD6Roa5XJXepKtjn7sjdAC2ekbQU623nmhiSb6qXWwIZsXcITsNIHcLxrWjGmMiP-FIwKvLoYBxPVRd7SM8ahuw3nHTLcyWYrMgW0Wl_VGNaEoBVPKkXYNYr2PZm1-smAc6B_g5LNAOJzybV7Dsw5pU4UtYZoO0zsqNvfF3UsKXKTXtSXtSEK6mD55g8G8_rAhongC7fuZ9T2rotKidGLrrOoUckao7jJXQKWIvLbm526zGCf42o4SsgztlSvpEe-tjC5OsmfJ9uyyg2oa8S4FDHjxQdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روحانی: رهبر شهید بارها نگذاشتند جنگ شود/ در سال‌های ۶۹، ۷۷، ۷۸، ۸۲، ۹۲ و ۹۸ تا مرز جنگ پیش رفتیم و عبور کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/685357" target="_blank">📅 20:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685356">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2LR9xCmgNVPUREZC2Ai0WaAoq2rEZNoEtPgMwDM-LLTR0iPXBIaOhyAn5LM5HzQ1Y1dYbfa5kbaXG9bUv_MoUDdeN8c7lEF1snRoFfGmoJDRS08m14QQ1On9pb_5LnbkRdDpq5nBA-BWh37OeDCXi3YlukO0ohmNT5uWQopcGfLOSSVd1gjPWtF1RNSdBYQBTY5Z9QdjmiI9G5ymByYipDx2EH0EtIe5RLbPnJjt-d_UOVdvt73txiluaYZVM-pAoNmuz8jaioHCWk02qpV2ador1Git5cKkvfhOjRThWT5KcaIUNTwCuxC16G4GQMrx-WQw3zCLgttgeqCqNNOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ خواستار تغییر مدیریت و مجریان CNN شد؛ به‌جز مجری‌ای که از او تمجید کرد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/685356" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685354">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cdccc011.mp4?token=TW5b7VmTUXgi6YJqvBn-P5J-v-0R-EpRBrFGAhUzNsfgZ2wuckvcteOJ9z9ii4zeYVJiszAvNliwfD2YOPta8MKnO11IgOwNLuHRjSFra96mF28oOa-PLBZkZePnCWaFOopcDnHY-3ZVFs5MCau3CxpOL7AqiFfupXgrPT_Yw9Mbsg0d7gUFjDuYGFQh9IE57V46WRE-ZBrOXeGDMX7ex5W4eFOFdCXPREDkX9WvuRkjLMzod-zW9PBK5hvFOLWvo4Q_mgJj6HQByYgMoEN02AHGr3cxRpCqUfRzWiJIODuHGDMCmZB6_D5nJpLiJzutQrTjAehQ2Rx81_IGoYy8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cdccc011.mp4?token=TW5b7VmTUXgi6YJqvBn-P5J-v-0R-EpRBrFGAhUzNsfgZ2wuckvcteOJ9z9ii4zeYVJiszAvNliwfD2YOPta8MKnO11IgOwNLuHRjSFra96mF28oOa-PLBZkZePnCWaFOopcDnHY-3ZVFs5MCau3CxpOL7AqiFfupXgrPT_Yw9Mbsg0d7gUFjDuYGFQh9IE57V46WRE-ZBrOXeGDMX7ex5W4eFOFdCXPREDkX9WvuRkjLMzod-zW9PBK5hvFOLWvo4Q_mgJj6HQByYgMoEN02AHGr3cxRpCqUfRzWiJIODuHGDMCmZB6_D5nJpLiJzutQrTjAehQ2Rx81_IGoYy8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آپدیت جدید تلگرام ویرایشگر متن پیشرفته
🔹
کاربران پریمیوم حالا می‌توانند متن‌های طولانی را با ده‌ها ابزار قالب‌بندی و کمک هوش مصنوعی، حرفه‌ای‌تر ایجاد و ویرایش کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/685354" target="_blank">📅 20:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685353">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">07-2 Ane Manaee (1403-09-01) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/685353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هفتم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
زنگار دل، قصه‌ای از چرک اعمال [00:50]
🔹
وقتی قرآن هم بر دل اثر نمی‌کند [5:37]
🔹
از ترک عمل تا خروج از ایمان، فاصله‌ای کوتاه [6:38]
🔹
آنجا که زکات و انفاق، آزمون بندگی است [10:05]
🔹
حج‌گریز در شب اول قبر: انتخاب بین یهودی یا مسیحی [12:30]
🔹
بخیلان کافر؛ فراموشی فضل الهی و وظایف بندگی [15:17]
🔹
حسادت؛ زمزمه‌ای از کفر و جنگ با خدا [17:23]
🔹
رجب‌علی خیاط؛ مردی که با فرار از گناه، چشم دلش گشوده شد [19:55]
🔹
انفاق؛ آزمون سخاوت یا سقوط به کفر؟ [21:31]
🔹
عیب‌جویی و فضاحت‌طلبی؛ قدمی به سوی ظلمت کفر [23:50]
🔹
احوالات حضرت زهرا (سلام‌الله‌علیها)؛ تصویری از باور عمیق قیامت [27:34]
🔹
محشر حضرت زهرا (سلام‌الله‌علیها) در صحنه قیامت؛ هفتاد هزار ملک، عود، و پرچم‌های تسبیح [30:18]
🔹
قیامت در التهاب؛ روشن شدن آتش جهنم به خون‌خواهی فرزندان حضرت زهرا (سلام‌الله‌علیها) [37:27]
🔹
محشر در حسرت: ای کاش ما هم فاطمی بودیم! [41:44]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/685353" target="_blank">📅 20:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685352">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tURStc0mxS0RZ1aeG_3SeWdrlv1wWOISRBeRnseIYzUNI13xmu5Ltgbur7tmKfflkwjgrN0RWOoEUjUWt7UHbW7nsrlFaaiO2ZLqffsfJmEiA0UnRDvaY2F6yvXtrHuH70C4eVg-MT93oxU02NY_1_jqBH73sOLjX6110UEDJhsYJBHZvKLH38iBDsMvstL3BTBDBnF-meWb7XzmVpad-PLcddN6V5XHR9u1MO7n0d38XHyUj-Lsr6SNvbIuuJaooo7oTWdVspvWcAV2TkJmKlJHJ1M2cvtn875NVaE9UogrVPLKzWBF5lxjmEB8WdBi707G9cTosAQ5EBOFMsq3Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند تا ترفند که روزی به کارت میاد #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/685352" target="_blank">📅 20:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685351">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eob_HCvC0-la2h7tWWpEyo4_CZtSWPkKvHQKdvoIgkuUFq4sLlRtbKo3kYVTuPLr5lIobLQFipoln7ibdRYCvYo8pjpZLH6Zh6qxo8DxZ5Vi9bKj749oWtkDie_JTY9T0kWIT8ZrnjGHD19v7NjC5unEe0o_tGeac1b75BPNUaQmDInvPl6SjQYlSs8zLZIVf5a_7jvRSBedCz3RJw1ejrbBtUvMQwZudZBOSJIq3Re8MPrJPbfrZCd4K-6QHU9IXYF64DeaIgYu6AHDgSefh56NC-VsJO2hE2WVsKa4Amv63OgYiLr35DCq6fih0DgYdgHvmE73-3ECq-7RIXe7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
به مناسبت هفتاد و پنجمین سال آغاز فعالیت بانک صادرات ایران
🔵
اهدای جوایز ارزنده به کاربران سپینوی بانک صادرات ایران با برگزاری کمپین «۷۵ ساعت تا ۷۵ سالگی»
🎁
بانک صادرات ایران همزمان با فرارسیدن هفتاد و پنجمین سال فعالیت خود، جشنواره «۷۵ ساعت تا ۷۵ سالگی» را در نئوبانک سپینو برگزار می‌کند. کاربران می‌توانند با شرکت در این رویداد ویژه، یکی از ۷۵ برنده جایزه نقدی ۷۵ میلیون تومانی باشند.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#سپینو
#جشنواره
#جوایز_ارزنده
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/685351" target="_blank">📅 19:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685349">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8aac8cd06.mp4?token=TkiE5BEJ9gk334T0FowCaEIYKpEF0WSKtwWmAYlbXpHGM2lEIjDpcyh8c5xkxJowMIRzedcA6ZelHyV6zhhlXYRAnN-jp7rX6sDgMWVgISq8kNqX7-hN8lQnrrZt_HXds_YjEX2Xs8Uu5Cw_TO439ATURVwt7KUfgoDQyEjTJhkN0ObpZC573cybC2Ltu-4pSJKNvtBeBZkm6l9YG4maY8UyyhOheP1ElA9gcFwXk2jZszq8nYtj7O2-bFa0tNPTEgKCsOW97hZaS8_z_XSJx2VypAm677USBry1BL5c9ptwEJMQ0O0YhTgaFueWXGyQbAKwmb9-IjK_cEPBe_WIsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8aac8cd06.mp4?token=TkiE5BEJ9gk334T0FowCaEIYKpEF0WSKtwWmAYlbXpHGM2lEIjDpcyh8c5xkxJowMIRzedcA6ZelHyV6zhhlXYRAnN-jp7rX6sDgMWVgISq8kNqX7-hN8lQnrrZt_HXds_YjEX2Xs8Uu5Cw_TO439ATURVwt7KUfgoDQyEjTJhkN0ObpZC573cybC2Ltu-4pSJKNvtBeBZkm6l9YG4maY8UyyhOheP1ElA9gcFwXk2jZszq8nYtj7O2-bFa0tNPTEgKCsOW97hZaS8_z_XSJx2VypAm677USBry1BL5c9ptwEJMQ0O0YhTgaFueWXGyQbAKwmb9-IjK_cEPBe_WIsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی والیبالیست‌های نوجوان ایران بعد از قهرمانی در جهان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/685349" target="_blank">📅 19:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685347">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17b66253f.mp4?token=eBWuehNxN23GdhsMhNbDA8nuZUf0KjE1AnGzhMVIeUeeChq7iLDswx_POTgfeNkKybWmPkJhoB6kE3uaaEv0QaJG9Ni4vbWXhOYC3ehuvHD8xwRaveJ4dG8B_odmmWrpyqMV_nmuJq49TZqENks3dQOqPoEwaAR6JOR_E3J_Pc7pdBBMSffYAcnpAvwS5691Vs5e3duERqz1ri54kFck7hCUikLZ40SiboigSRJB6C8uRppgfBmrto3aewzCaWcDtLOBTYFcc_02IY4uzrY0jAntz9AfNAsJ3TbihAQD3TRT-q-ji9w8fknIOA_AAQxXerFci-MNcvAPdProbWaq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17b66253f.mp4?token=eBWuehNxN23GdhsMhNbDA8nuZUf0KjE1AnGzhMVIeUeeChq7iLDswx_POTgfeNkKybWmPkJhoB6kE3uaaEv0QaJG9Ni4vbWXhOYC3ehuvHD8xwRaveJ4dG8B_odmmWrpyqMV_nmuJq49TZqENks3dQOqPoEwaAR6JOR_E3J_Pc7pdBBMSffYAcnpAvwS5691Vs5e3duERqz1ri54kFck7hCUikLZ40SiboigSRJB6C8uRppgfBmrto3aewzCaWcDtLOBTYFcc_02IY4uzrY0jAntz9AfNAsJ3TbihAQD3TRT-q-ji9w8fknIOA_AAQxXerFci-MNcvAPdProbWaq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرسپولیس به ملوان
🔹
پرسپولیس ۱ _ ۰ ملوان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/685347" target="_blank">📅 19:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0835b0d18.mp4?token=Sb840zkE-bfouQpCUuL5lCGz5NdDENQ32z83jWgSgTG83flkvESF6fnNYvYUwZePvA9i57bh1L0iIITABKklXjgsQ8bEEBPntjIdoWxJPHASY-RKQ_tGbvxUhAsMghTZlXlk0RhShdlWNkhPPW66d2BpFK_KEQW75Czl36ahe_X-GfK1TLSd3KuswnxpVcQJKGK8oYE5Ai0GVRU36ghL59m-lw9vV-abI3-iPjpbm2pJAzdgLSqsreX98Li9eXkmvA_XJGdyQsUbPbkhOjRgGOW667tYvNQYTl43JNVoQf64sklMLzSgH2yCa70bn7WlFKMiYpkAy3CeIhFSuMheCIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0835b0d18.mp4?token=Sb840zkE-bfouQpCUuL5lCGz5NdDENQ32z83jWgSgTG83flkvESF6fnNYvYUwZePvA9i57bh1L0iIITABKklXjgsQ8bEEBPntjIdoWxJPHASY-RKQ_tGbvxUhAsMghTZlXlk0RhShdlWNkhPPW66d2BpFK_KEQW75Czl36ahe_X-GfK1TLSd3KuswnxpVcQJKGK8oYE5Ai0GVRU36ghL59m-lw9vV-abI3-iPjpbm2pJAzdgLSqsreX98Li9eXkmvA_XJGdyQsUbPbkhOjRgGOW667tYvNQYTl43JNVoQf64sklMLzSgH2yCa70bn7WlFKMiYpkAy3CeIhFSuMheCIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای نخستین بار
/
لحظات اولیه حمله به انبارهای نفت تهران در جنگ ۴۰ روزه
🔹
این آسیب‌ها، بخشی از ظرفیت پشتیبانی و توزیع سوخت پایتخت را از مدار خارج کرد.
🔹
انبارهای شمال‌شرق و شمال‌غرب تهران، دیگر در چرخه تأمین سوخت قرار ندارند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/685345" target="_blank">📅 19:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4s7aCocXBh5Mdhq85zD_4TZytx_KI0fg3csivsedPGji3ogRCe5F8ORu2U_DgpZjo2iecSOgEeYgYSeQeHDyhHEcJEAptO2azqZhnUF3Jrr-tCi9QGTVUUCva2agws9ASXHACSP6P4MFcp3AYoNaBUcsFgRVKeN4wZ7pgllcWu4cYYNe5wg2QCLOgMyAKlssIM1bUyxhAkyI8DCVlyOLXS7oE3vzdR9KioTBzmxk7qUUETqh60QDxf39DqS1DM9yQYmI4au_0hn4dpNYKXzVYXgiAmfDD9Lg6tL4Z5uD0n-8XzW6T82nw9jWp2h0P9-ucb7omRoACc5CTBIH6mb5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف به ادعاهای وزیر خزانه‌داری آمریکا پاسخ داد: «ای دروغگو!»
‏
🔹
رئیس مجلس، در واکنش به اظهارات وزیر خزانه‌داری آمریکا درباره ایران، با بازنشر مقاله‌ای از پل کروگمن، اقتصاددان و برنده نوبل اقتصاد، عملکرد بسنت را مورد انتقاد قرار داد
🔹
قالیباف با اشاره به ادعای بسنت درباره عبور ۱۳۰ میلیون بشکه نفت از تنگه هرمز طی دو هفته، این رقم را با دو «۱۳۰» دیگر مقایسه کرد: ۱۳۰ میلیارد دلار هزینه جنگ با ایران و ۱۳۰ میلیون دلار ضرر یک شرکت فعال در بازارهای کاغذی نفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/685344" target="_blank">📅 19:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78351ed32d.mp4?token=OkWkOdi-TElLjdv5uTnFyoNvdmPeQmORKWaucz8zYWZzO1XeUko9GxmvBpimDfy25p6YumaQQkAl4bT9C1VNqtoiXbONZBpVXQinFbJ27VVKYbSegoukIpA4nFPfqyciO_2jzXzeTxkQFG38aBx5RwX5wuC_XGAAPizueCjptsv2NCv2USijoy5MtdtCGJwExzq-B1M5Mg-vQDz_ONYEUAoJt9uwYiF1XSF7rvYSOkTdhkSBXiWsKCaEb-J3bQ2e-9XuPuZOt5hbvaAqP2vF7a1LYB-TzTaBNA9n-AahObRK0QDHAAQ84_o6HxwF7YnTKs3UDP3jYS69IYudLVtpFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78351ed32d.mp4?token=OkWkOdi-TElLjdv5uTnFyoNvdmPeQmORKWaucz8zYWZzO1XeUko9GxmvBpimDfy25p6YumaQQkAl4bT9C1VNqtoiXbONZBpVXQinFbJ27VVKYbSegoukIpA4nFPfqyciO_2jzXzeTxkQFG38aBx5RwX5wuC_XGAAPizueCjptsv2NCv2USijoy5MtdtCGJwExzq-B1M5Mg-vQDz_ONYEUAoJt9uwYiF1XSF7rvYSOkTdhkSBXiWsKCaEb-J3bQ2e-9XuPuZOt5hbvaAqP2vF7a1LYB-TzTaBNA9n-AahObRK0QDHAAQ84_o6HxwF7YnTKs3UDP3jYS69IYudLVtpFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرسپولیس به ملوان
🔹
پرسپولیس ۱ _ ۰ ملوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/685343" target="_blank">📅 19:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685341">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JH9P2Pi21h5aD9DhPZYe8L8JVQRDGurDfyc3VkjzGJzWXNlKoXUEpPXd8maMsuYZJBjBc3h_lhms4LW3JuCFjDxIb7XS1D-gJ6IhBiQVwO7N-wiUdFLJ1okcw6OF7pG1t3_pIYdkiD0cUA2i1OPGy8iSKuGOhjUps-_ofyz67AOWTctV5E3z8ggiMUlGmUFQpkbbVDWc91aomUnNhiW9cqHcwX2qIDGkY_uuPu_vV3BrAjVIf2dX5t9krdc1ZaCM3JE8dsR3QNVn_LbhCJjJNQNbidQe-Ge0RY72sTzV_levq3KIPo-nK8MK68HElldTdLES-ggi6zmC-p0xeYx7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری ؛ درد دارو
🔹
اگر برای تهیه داروی مورد نیاز خود یا خانواده‌تان با کمبود، گرانی، نبود پوشش بیمه، نایاب‌شدن دارو یا سرگردانی بین داروخانه‌ها مواجه شده‌اید، تجربه‌تان را برای ما ارسال کنید.
🔸
در چند خط یا در قالب ویس حداکثر ۳۰ ثانیه‌ای، روایت خود را همراه با نام، شهر و نام دارو برای ما بفرستید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/685341" target="_blank">📅 19:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685340">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e872d9b3c8.mp4?token=n-sMqXpvfeUBqAb5Kn4KwuAl2G23LD9RTCipoKmAUZkEyaWIe58JpfSLbsW9gbS2R45i2GXSI_sO-QgoCfQu8gjRVTfGw8EaZljQHeoMCTG_8a0WSzo-Js1qltw8nsPG2OaGuzCILuPzLCWI4EkxQj6VFDUtNhUzGBRcCRJWgiDS2OLbnkDuuDJ5IdKhbBAj3vobrFg2MicHyT2FkpKbFF804O-m2KG-rq3Yr0CuqOYX3AbnKr47cpAZF6349zExZexLDRV8gaAdWekD4slWHH26ix-1DWpRcRIWsoPh2f3yr3Xw7AsWlW-v-sykmlQQ3rGBmtH2sOpfimILiDJ6kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e872d9b3c8.mp4?token=n-sMqXpvfeUBqAb5Kn4KwuAl2G23LD9RTCipoKmAUZkEyaWIe58JpfSLbsW9gbS2R45i2GXSI_sO-QgoCfQu8gjRVTfGw8EaZljQHeoMCTG_8a0WSzo-Js1qltw8nsPG2OaGuzCILuPzLCWI4EkxQj6VFDUtNhUzGBRcCRJWgiDS2OLbnkDuuDJ5IdKhbBAj3vobrFg2MicHyT2FkpKbFF804O-m2KG-rq3Yr0CuqOYX3AbnKr47cpAZF6349zExZexLDRV8gaAdWekD4slWHH26ix-1DWpRcRIWsoPh2f3yr3Xw7AsWlW-v-sykmlQQ3rGBmtH2sOpfimILiDJ6kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی والیبالیست‌های نوجوان ایران بعد از قهرمانی در جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/685340" target="_blank">📅 19:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685339">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/000f0a3f47.mp4?token=JAiOCAqsm5YXPLdr6Ttl9TSlgeJCRGS1CFMcFYT1U7jLYEIzX1Tcn3HkL5MBALZI6Wt7q1Z6GaPbyoBnPVXd-DYIbMPBZ-JlFgoS500Cqc8CMNvVdNbHQ0x0-S4MNddEAHjqVftYfBTvKROYYjGx8FuPo09r5lL_yQhmk6ErlDWHGPdnYUkJumTdw674lbfENFzUVueoELHiRlgUmQLBwmgYc1vQsVhuvdnA9eUci4CkEnh0s3H4K0WPHN23nEDRQMnm6rtG8b47SuC4fxqXeUX-cPWZSaFW5vYSPFUlrmCTVIsB-Unio_qXo08q8mjhcnpOhj1Kii5Nqwg2G9w_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/000f0a3f47.mp4?token=JAiOCAqsm5YXPLdr6Ttl9TSlgeJCRGS1CFMcFYT1U7jLYEIzX1Tcn3HkL5MBALZI6Wt7q1Z6GaPbyoBnPVXd-DYIbMPBZ-JlFgoS500Cqc8CMNvVdNbHQ0x0-S4MNddEAHjqVftYfBTvKROYYjGx8FuPo09r5lL_yQhmk6ErlDWHGPdnYUkJumTdw674lbfENFzUVueoELHiRlgUmQLBwmgYc1vQsVhuvdnA9eUci4CkEnh0s3H4K0WPHN23nEDRQMnm6rtG8b47SuC4fxqXeUX-cPWZSaFW5vYSPFUlrmCTVIsB-Unio_qXo08q8mjhcnpOhj1Kii5Nqwg2G9w_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوجوانان والیبالیست ایران قهرمان جهان شدند
🔹
تیم ملی والیبال نوجوانان ایران امروز در دیدار فینال رقابت‌های والیبال نوجوانان جهان با نتیجه ۳ بر یک مقابل فرانسه به پیروزی رسید و قهرمان جهان شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/685339" target="_blank">📅 19:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
احتمال درگیری تمام عیار بین رژیم صهیونیستی و ترکیه وجود دارد و آن روز پایان ناتو خواهد بود
دکتر بیکلینی روزنامه‌نگار برزیلی و استاد روابط بین‌الملل در
#گفتگو
با خبرفوری:
🔹
این یک احتمال واقعی است، چون رژیم صهیونیستی همچنان از حمایت ایالات متحده و متحدانش برخوردار است. در سال‌های آینده حتی ممکن است شاهد افزایش تنش میان اسرائیل و ترکیه باشیم.
🔹
همچنین رقابت و تنش میان اسرائیل با کشورهایی مانند پاکستان و ترکیه می‌تواند بیشتر شود و احتمال یک درگیری گسترده‌تر در منطقه را افزایش دهد
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/685338" target="_blank">📅 19:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/072008c1e8.mp4?token=pqtarN-Jqespq14Lz_WGll12YqlxLxci3ivYrvdk7z1HFuL5RXHtSYtbtvAYSbOxTPpKRJr_4OupeVplNAiyoQK95n8CtTE98ZMaFmOlFXRymu12KuTfsmDDM1HF0Zum-q3DkL696lILy16qxZ4q7_PyCpC9f_s6kSE4PGwDlgIm85QmctoA3sOLJzxXuhyjbdx8hXmCsFavdmuLNm-LbWn0L5E6kQrwsdX8fINXDMqSCusyZWHITADBUDT2_PhPSYFO62MdWWiUPQo34mQKE5c3STDCJEY_gpj_tq5r-mTXA0JzZ5y3o4EJe8LHl8hnYdq-pCjLM0i1ThIdDwgrXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/072008c1e8.mp4?token=pqtarN-Jqespq14Lz_WGll12YqlxLxci3ivYrvdk7z1HFuL5RXHtSYtbtvAYSbOxTPpKRJr_4OupeVplNAiyoQK95n8CtTE98ZMaFmOlFXRymu12KuTfsmDDM1HF0Zum-q3DkL696lILy16qxZ4q7_PyCpC9f_s6kSE4PGwDlgIm85QmctoA3sOLJzxXuhyjbdx8hXmCsFavdmuLNm-LbWn0L5E6kQrwsdX8fINXDMqSCusyZWHITADBUDT2_PhPSYFO62MdWWiUPQo34mQKE5c3STDCJEY_gpj_tq5r-mTXA0JzZ5y3o4EJe8LHl8hnYdq-pCjLM0i1ThIdDwgrXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلاب در مادھیا پرادش در هند
🔹
تصاویری از منطقه چترکوت در استان مادھیا پرادش در هند نشان می‌دهد که آب‌های سیلاب تا ارتفاع نزدیک به یک ساختمان یک طبقه بالا آمده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/685337" target="_blank">📅 19:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685336">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ضربه مهلک مرزبانان هرمزگان به شبکه قاچاق سوخت/توقیف۲ میلیون لیتر گازوئیل در خلیج فارس
فرمانده مرزبانی فراجا:
🔹
مرزبانان استان هرمزگان در یک عملیات مقتدرانه، ضمن شناسایی و توقیف یک فروند بارج یدک‌کش، از خروج ۲ میلیون لیتر سوخت قاچاق از کشور جلوگیری کردند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/685336" target="_blank">📅 19:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685335">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgqYnK1GVANxhYqel_LAwKrGHts848lTHcvVTpxkZySEvh8D775wP5eMfxWWUW0hzuS2KzAwPMUT5eJhvxrVIDksCtZmi4E2dOSASschjnx_9B6v-ANBCVNM5_Z4Tf0UcZVYVh0KW5L_vOGgzCFmOqRyzdUIELKSRTkaMjGiKsk_y7ibaagG4e-q4PmA3zBwazk65K6QR11ylEBAr6t6OdM6hqNHsF5jdIKmpA1lcXL2HVTLQjiOvPpq-CtHQ4sxTefly_Jy0cdL1q1zSh2-I1U5HVyaMsz6A0Feh8NTRGvbyo25VpYWe2PSoVKZM2JB9qppTjUHbDtyiDo1fC-64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میوه‌های خشک به جای دارو!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/685335" target="_blank">📅 19:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685334">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp9fGXaUiB1FlspbPspw4Ak0Y15eysIBYBpUV9u8PBvkhYM0eUAjP4FLVAzOBoAND7vZtw_96oLYQWZWOR5XbZLgvD5t3z7EsjVMRC_piI90ex17y4pgUMSc4SP057CqNrNQzO4gFz744aNk_OTwOVUj1pLKQYL37fkvUE4Z35wSnGGveK3QjjQtkIvtkVU_EFCbfNohpU_lZ8pYtR4WilnTB_bDqiON60fIIli4H1G-122oqJLoDO1wsKALs2NVbhNMmriipu7v0OZdkQxLPiIta_bQptj8zrRE0tm5YuLo99oGCB83oQ0Lo60bywilpn39zc8Wk6Rohuhf8q4Xhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
خوبا زود پر می‌شن
زودتر قسطی اجاره کن!
🔥
🏡
ویلای استخردار تا کلبه جنگلی
⭐️
اقامتگاه‌های کمیاب و پرتقاضا
⚡️
رزرو آنی و قطعی
مشاهده اقامتگاه‌ها
👇
https://www.jabama.com/landing/jabama-best?utm_source=telegram&utm_medium=social&utm_campaign=news_0607
@jabama_com</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/685334" target="_blank">📅 19:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685333">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPeLI9OL8lk6ZZNCwWZHtVQSH3Cww3my8BAM5eIC-kz2mAmbEQFW3VzpSct_TRk0ucphyjuo5FZsru50lRI7bQJVBp3RZLsV1Zt1LFQ8NM0mL5gJPk8VFVpSaLHASz_lagO9_4myQ-F1Z3TbB0yyYIXf38OosE-wo0WQpfwLk62WXkGMPx7VnowxS_qblY0PGUXbsvh876vVIPyw0SVUL8_lfOawdbGLjJig1GnjBVOx8uxeZPFOs75dqtT5gzlSfYj2gGEFg3eU7VErdHD9KQDsqhE8JCpR1h9bA1145N6Xz2riKloCkL_wieIQoPa82nmM2Q8YGINAL7fkOt5XMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه کریس مورفی، سناتور آمریکایی به پدوفیل: تنها دلیلی که قیمت بنزین سر به فلک کشیده، این است که رئیس‌جمهورتان جنگی را با ایران آغاز کرد که هیچکس آن را نمی‌خواست و او به هیچ‌وجه نمی‌توانست در آن پیروز شود. انتخابات ماه نوامبر، همه‌پرسی درباره بی‌کفایتی او خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/685333" target="_blank">📅 18:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685332">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ba8def8e7.mp4?token=YEJtP8ztjjQdX1VXHTbhkRwJ6inbpqAtnSViPZ6TH3mlI9Nqzg_T3ExHaDlYzLEpodPeVwiYTz1VSgneIR8H1fuQcYWn53GwRnnvhEnFrYdkMjsPxjFXhyR3cUc5F8WPQfU1f3ErsQMkge8DcJlF3gRlCI4ZiCaYAPSfGloE10dYvmmGEfu6zy8ZMAWPqf3vZV5ysaI6NY58p4AqbRNIo0vRvuD8UkCmqLs8Oo8y1YA0uNz2XDMy6N4sL0fRUMpD-jjHc2XGlMee_Et1JaWderGVVOQvyUixPylHRDRcFcmWVJukhXfSlaLqC4MnK0MOnVwvUjTwq84ZYCbHZWIjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ba8def8e7.mp4?token=YEJtP8ztjjQdX1VXHTbhkRwJ6inbpqAtnSViPZ6TH3mlI9Nqzg_T3ExHaDlYzLEpodPeVwiYTz1VSgneIR8H1fuQcYWn53GwRnnvhEnFrYdkMjsPxjFXhyR3cUc5F8WPQfU1f3ErsQMkge8DcJlF3gRlCI4ZiCaYAPSfGloE10dYvmmGEfu6zy8ZMAWPqf3vZV5ysaI6NY58p4AqbRNIo0vRvuD8UkCmqLs8Oo8y1YA0uNz2XDMy6N4sL0fRUMpD-jjHc2XGlMee_Et1JaWderGVVOQvyUixPylHRDRcFcmWVJukhXfSlaLqC4MnK0MOnVwvUjTwq84ZYCbHZWIjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راسته میگن پول رو بذاری رو جنازه بلند میشه؟!
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/685332" target="_blank">📅 18:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685322">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIfGPiSOUVhH9CYa8FkxXKuv_g4n6D_NBZE-qbqINnJZwq2HfsXNDUwVxQSsNoBktgAfFxasgfm6k3RfCJhgaWpPdpWSSWAg71YKTPevc-YypHdLsAFpUQqf0CDk0BXBHnXdkPEwrhN7HMLQ0IYxZpaR4UaClVF9CbLubR35F7jzfIPmmI3Ub35d6FdoP2_oDMDXW0Ulovg2TuRC4LuMmR7HGbpCJFDf3g8iTfZTrlgiGPZnAVNz31NRHk0LgWulooNNXlf4oaamYHsYyOAS3fxXYeanvRKeWSsSROzS2QHxInNILCpKbOVGp7ou77L1osyXr7ifOAiYYFPv2co2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMEVyb1lF6Am7fncZS3C83r66j2-AqWQ7hS6WSy8Q7RHQATdjYN7Avp_XD-rGRunt7MooCcMQsInCcg795dgazxlCSI16ENfIBzvRKUIhYcCjfdjDaAF-Bvrpt34wALH3DvIR_ePlUTQEIjWvvjwbUkdtNGP0MciRCYQ5zptqCKdvv0WYZCpmEv_OuCMKDMHS_YMcyEwdiC3F2_0ayCQEPZricYy1O7VyZK7yS3CBrU2hq5fM76veYwLEx2AmTvB2N_mCk6iMpFfP8RUu-poGauG7kcpfhqRvX_p02LMBQs83ELO6jEUVd9ZX4Yko6ElZqQST0AtJwko21vCp4ep9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Si-u7AW4x6BPW6GtUP0zfmkAjVfzblWTkZAh0HCJ416k5pzEhQSdrF2ZObuhYabuoYMZC53VCB5VsnO4D7IMLRxitMMgScpqksQfjpB_HxG1ePxyhHFWl3xHN4OAfucuU0u_8DlRhMvnT1SEQZyHybvedDNvfNyQPWZCL689K2ZdE7dol6Fgj8yEQ861wr3u02jxERU7CkCECQdAgKRgSa812tLB2VPja8F7CoatlUXpNP3IHQgSz73ujRTW7n70YQJTAWL1B_bfCeqCQxKvNdPtWJd18rKHrWB7c44VHjlshmm78HZcS1dqvRFCHlu-G9DJpKwhTdalRcN65GX61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6Cxa4Z8AxHnDRgMF3-9F1HWlng7QTDd6P-KM4gG3fjySKtY13OQ1Rr0J80gQUX8BFWg-QBVuN8tDSwp1dGoZE86iHr64VEDByUb9lxE2jpbV1C78SuvwEbZEHVbZIoqa3vSB-Cbbe-TfI8ptNSJZ99Qjv_A_PDwuQM-mI2MEnEIXtw72TAG54tHnDwimNQ7BS567ILN3PtvfhET9f58tyuibhJp7Ofa0HjgnMsZiiWezqpAEqDYGN0uuZuQCki3NCg5bD1z5uZpoXkRO4-t9U9pZtkEEm9W7haaBy_7DmYC6fwQYALFrcnnciHX0Wcwx9yqTEqazy0GZlf84DaPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3JtvDocuM_68SaWCALc9GTHaK-a_DGEimGlMJhu6s0BnQ_ZqRwU30PZiLp5-BKBaFXjaSixXjefCiGLhA1RIedlXZPVfGzHZSNsp3CmxwWQfEjIr-m3uqnet3M1NJrkn5JijgeJ9kWv7ir_tn__g2P9-jKoNRjD6tpm1g5-WwKc5smSgedx9DaArDW08_nVc-fMeGpy-jtqgUcBqS82IHQjy5kLffn-dZZbstQFUecs2v-sWYPqCbJyUfIpR9kPmNgI14pIkSYiLW83uNObFsG4UmbXhzSkClqp2ysOLLfWkWF75IxHCcLBIeGhSV2kYMico5CqkrTeapn3BbV0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJZ8SA2GQBhjQlTZDP7Qh3DVxZHN2ivzg0YqD8ZOeFZ48P53QxH87pFRjqdtmQTUGRqrNrQpK3jj2blqjQE1gzr-Xn8EFXwSRvHQLXHHyhFxqV1RgH9DYvkUBRX7PsKNoOqbo3hNxP4MxG8mTr907V6u-u-HkFu7nD5qNP4vb-rB2rioEze2Vwi5olGOLuW4_Fk5XvbsAV0_LkOfjhS2pMbWoloq_QQ3p-BIWasRJMy0IJctYc-WMdzfieRxRaf0EW-N9fQCxw3fuFlr57yQkzGSTdDwJtKNbaS5VtMhviKaHc4a7y0WyiFhmYfB6CEshfXydYweuNy6RDTf6JIgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3Z47lEaSOvlkEJ6417awittXyh5tEsZYMeOktOBgA3-HNh5uYeKc6RjN2TwVjZ6eVkwVcHXh8dprOenohBrXO3ReJxpcUkjuUtbv-9nKSW-k2Bi6lKwlGU7dpSrRTMKzTIAPdhBUtW3nu-203Hyu3YeouHRYq8ZqliHoJahdW_0_jqNd3wi5mqXNHajPr2tZFNMqsfS9WVz4Q8imUCjxDDexUjEMxGX-Hw8Yi6yxNUCERNIM2VkTlcOouCHlm8Fxiwsm4t-Ri1CfipfsAlbPeVsiF1H7sPKwHaTfV_5StUwfuAIPUU9FWfjq5jQVSIrohh97tBuROoNmJNpWFLCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AznZDHy1275cNVm7i7Tg3gEbhLOkiw6mAmjrIFLVAWuDLpf5m8-UosLcezbmONmyAnMTcyHvstcG7Cn1UCr6fAAcKCZHH5F1imHFOwX2mfi3MfOeInGbCnP1tfdCnqC1-U4dVkdVyWfwju5fS1xerbxjyw10MnHzmAYbSR3uGcoyVARVqYlT0h6neFGz3K1rD4VrrrI9zK1nzGGHYFMgtRw6N85m48JvZPxyExMqAk_b2aw7fAjew3rZ2ZqaifjpJprwOFSUuy2nbM8KHVF5nDVvazD2ojcisxmLIK-drTlIl8sVXJ7FS9FgpEBfrqbAvoM39YNSViaS4NSlPgiTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdUosus-67wcMffmKdorzJiNO-pWH0fx8mWzSrlkzD1GEbShIiny1jfTKMjXR7JN-orLSPsrCtE_g_kjaYTzfk57P0RWLlWh7SNHAeefcoy53QvYnAaSy0OyPuGNeQYpLTYM_weKspx3NS7rIY9ZRjBwjoF-AqzKtX2_JFgTZYymUVTcIZ9aAEiXIldTqMsGrVtxUPVOIg-M7EEa7coKi_gasQ9mpPmfeUGJ8gncRSVQDJcYIlj_WwyK0bnYGffP5pjz9tQYoORqwygqC3neluFHqqUA6OUMj5C2WbxEMpHxPkqLHcyVOVMNYozjQGj_ew762B8aQ_UVvZS3u-WA5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت دل‌های هم‌قدم
💫
✨
وقتی دل‌ها برای یک نیت خیر کنار هم قرار می‌گیرند، هر قدم می‌تواند بخشی از یک اتفاق بزرگ‌تر باشد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این هم‌قدمی را ادامه می‌دهد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/685322" target="_blank">📅 18:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685321">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
آخرین وضعیت توزیع بنزین در جایگاه‌های سوخت
سخنگوی صنف جایگاه‌های سوخت کشور
:
🔹
تامین و توزیع بنزین کماکان بی وقفه ادامه دارد
🔹
امسال به دلیل شایعات فضای مجازی تقاضا برای مصرف افزایش پیدا کرده است.
🔹
احتمال می‌دهیم از مهرماه با کاهش سفرهای تابستانی، شاهد افت مصرف هم باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685321" target="_blank">📅 18:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685320">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مصطفی را وعده کرد الطاف حق
گر بمیری تو نمیرد این سبق
نام احمد نام جمله انبیاست
چون که صد آمد نود هم پیش ماست
میلاد حضرت رسول اكرم (ص) و امام جعفر صادق (ع) مبارك باد
🌸
✨
💚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/685320" target="_blank">📅 18:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685319">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
نتایج امتحانات نهایی اعلام شد؛ آغاز مهلت ۷۲ ساعته اعتراض
🔹
رئیس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش از اعلام نتایج اولیه آزمون‌های نهایی و آغاز مهلت ۷۲ ساعته اعتراض خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/685319" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685318">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f82268e2.mp4?token=q4knbE8LK_bh9nynUOdPTr_NBDq8K7FTRII-iIuFvEA0hUxFRhLdelsipYbR32KEuHmDxgtJsYSvXKqpa5Kay-uD_RWceFb9cQu4X-FPEAQ-rkvAnewtVveL3sj0RcFuP92tEiz6c-eGS3OoRBiWGSpLLSHZwo0eP7l2PQ9qFREvTBCbFKoGyWZYUamaSAshsqTRiDYC-1Er3CxqBvGSscexMHMCjHzC7MGCYDmRl8Gvix7GmX2exV7UDV4nGtGitXB_nO6w42EM6R3N1k2LhybCEv5QjSTvFBan8WwQ2ebuG69-O1Xhddv1_CfJ8jA1K_t9ICLgxoViMnSEX4aixA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f82268e2.mp4?token=q4knbE8LK_bh9nynUOdPTr_NBDq8K7FTRII-iIuFvEA0hUxFRhLdelsipYbR32KEuHmDxgtJsYSvXKqpa5Kay-uD_RWceFb9cQu4X-FPEAQ-rkvAnewtVveL3sj0RcFuP92tEiz6c-eGS3OoRBiWGSpLLSHZwo0eP7l2PQ9qFREvTBCbFKoGyWZYUamaSAshsqTRiDYC-1Er3CxqBvGSscexMHMCjHzC7MGCYDmRl8Gvix7GmX2exV7UDV4nGtGitXB_nO6w42EM6R3N1k2LhybCEv5QjSTvFBan8WwQ2ebuG69-O1Xhddv1_CfJ8jA1K_t9ICLgxoViMnSEX4aixA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تگرگ‌های غول‌پیکر در ایتالیا خسارت به بار آوردند
🔹
یک ابرطوفان شدید در شهر برشا و مناطق اطراف آن در شمال ایتالیا، تگرگ‌هایی با قطر حدود ۱۰ سانتی‌متر بارید؛ اندازه‌ای نزدیک به یک کف دست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/685318" target="_blank">📅 18:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685317">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAX3HsMZ6XHH9-EISRU4bacqSMQPeW4DTvDvWkHa6F4CfqXae-3vnvZ-z7e54i9IbXW4g0raHTB3DhB_vIlkKIBeGFbskVfgVBhNUpOa2MwicIsajgNu3rfiYkiicPAZcz7iAlE0GZtqqBWq17PUu2xYz5Zuf3Hpfk-o8D44_5VqERLSuOxnHWPKXrW1s2-OEHddMmnV19y8wQAXNGwNjyewaJGQQArzIGjHNNLOyTF8igdltrr4ZbI_RmDAn5vTpztqKq2vbOi24RRRUNactwy5_j6HEYxEFGXMBrtOgyKgOt8oFDv1NLpaWm70U3KnMGrCyg6Zv29xGzKK1Dn7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوق پرواز
🔹
تیم ملی والیبال زنان ایران برای نخستین‌بار در تاریخ، با صعود به جمع چهار تیم برتر آسیا و مرحله نیمه‌نهایی قهرمانی آسیا، دست به افتخاری تاریخی زد. ملی‌پوشان امروز هرچند برابر چین شکست خوردند، اما عملکرد درخشانشان در این رقابت‌ها باعث شد با کسب مجموع ۱۱۵.۷۲ امتیاز، سه پله در رده‌بندی جهانی صعود کرده و از جایگاه ۴۰ به رتبه ۳۷ برسند. در ادامه این افتخارآفرینی، تیم ملی زیر ۱۷ سال ایران نیز با پیروزی مقتدرانه ۳ بر صفر مقابل آرژانتین، راهی فینال قهرمانی جهان شد.
🔹
هشتصدوچهل‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/685317" target="_blank">📅 18:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685316">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOiDUWyjiBsf6Hg_XFe3tOY9tt935C9YeO2R1fJbO9ohdJOhI1yaHZBVzpnR_C9KpYoaoUBI1APb9FX05zSxTZVzdKesEHvXsGEdtZ1WWyeccX7ayuYSSc2FsL4XpWVesjK_P71qRMb8asELEc45OJAarlF4pyrZwIbtNKeQmD_Vp2-ZELHgD3VKx26wYbFfuzM2EukNm7zKW8s2QPds2WdV1OKv-r8QtJ4iPSIs0Apjw4Pj8Bl1DZPMCU9tNoSw6mtzrFn_JahkLqcSMvQsFlfoadDOkDTtIfiRKHapDwsBAW5ls6-BUX9oVI4SUFNM_i31iPSD-SwdYF_9r-Sy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685316" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685315">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d1c31f.mp4?token=AYSDcXVm2EWj721pG4wCEE_iZ691VC73tc7H2eiS4Xz4VBKuwk4DwHscbUQCHwyD-neqhNCTZ4D5XrQNOXfRQ6lxceqRZ41QMXZIc3r64ekFyxstgDCqkntdIAIpaqHs0_3pzdEndE8mZvmSgYld1WYG2_xvduXZMyoPQVjwv7G1xSkUocZAndGS4_s_lgwi9pQ3vSxovGp53u8STG3uWUKlAWsxF47OnqLn0CIwP1vYN9DmL1ACgxIV5wq6jLSnuQlLtO4YoxQ6OCAvMpYIc2gQZcV7ObewNB8Y6g5L4CS1jxNe31kCDZMvW-HKPipNRT9lVo-aBU4i0NXRuPd91Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d1c31f.mp4?token=AYSDcXVm2EWj721pG4wCEE_iZ691VC73tc7H2eiS4Xz4VBKuwk4DwHscbUQCHwyD-neqhNCTZ4D5XrQNOXfRQ6lxceqRZ41QMXZIc3r64ekFyxstgDCqkntdIAIpaqHs0_3pzdEndE8mZvmSgYld1WYG2_xvduXZMyoPQVjwv7G1xSkUocZAndGS4_s_lgwi9pQ3vSxovGp53u8STG3uWUKlAWsxF47OnqLn0CIwP1vYN9DmL1ACgxIV5wq6jLSnuQlLtO4YoxQ6OCAvMpYIc2gQZcV7ObewNB8Y6g5L4CS1jxNe31kCDZMvW-HKPipNRT9lVo-aBU4i0NXRuPd91Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
#تیتر_مستند
| قسمت اول: اقتصاد خرج‌های بی‌صدا
🔹
بخش بزرگی از درآمدمان نه با خریدهای بزرگ، بلکه با هزینه‌های کوچک و پنهان از دست می‌رود.
🔹
در این مستند می‌بینیم که این هزینه‌ها چگونه شکل می‌گیرند و چرا به چشم نمی‌آیند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/685315" target="_blank">📅 18:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1IzRkZkVrGcJuVFWqUiiY9T6FN_3ZzJMBpBNIH2yiCKrOJftHn-vSajehoPZ8wyaxoYA2KKoh7sZv-M9C1NvLfE4rwnVeDtA9yVUjYQ4YY6Yd4Wqp5O906fDfrfYUMAkFB4Up8uwbY-4BP92C9FSV7rOdmlTzQA3FDRih3UvuY8nhwbXbZg2YBYsSNzgaibIvyvaW0_kC48-t_rpACbbsiqS4d_yw27OipZ-0DI0AbW3PAO1UbRf0GRgg2rSq72oBPm8XNOs65DV6Gq1tHkllnFWtJPYI7o1Yy9jZgZBcVQGMRyxBr2BxYSyZMkamjAR93U13y5ayTK_7xif9ZFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igtwU94qBVTqdqqVW-WpD0XFd3TyjYObVfTdAghb1ENIP5da_wUrocidkRLUULbvEIifAvrVeJ5ciCihTrB7ur_-lP5sEavK5QaLoyj8TwbQIrhaI0ZZ2NoBL2z1LFQTTPuCaKWowcIMmuqGCSZNtTNa_NvmsGy4TPre8a8mnf90EZ9lJxkef3PmENeauQs2I_XTfE_JvRtcakWXYs-mCdJwzHV0fmYAREzdew1xYA6I--uMwibHPczKaqj1ieBLuEFyfXVJ3SwhRUudC0_OWWvJdAl6bFZWLZmnIGQu1hAWwTBW4CihrVP1T7qNBt9mrirRpYhnAmj-3Begg5Xulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axXAwg8-JYeB7qSuwRYv1ncVp81D2EUNWg4mN73FfPZ8FdXPaIesZkUYEVvPZTmNwUX9MlC3L0zOZvfF0W0B-YQvOsVGI8zabjLmuhEVghqjptrDUCyKmJw1thAV8QvZe-6CiHxOKmS6BdWhxPel2DOujcJ7Xzhq05UIXmJaSIdrSdrE21IJ95WLPRBqqABzrba2iRRjofge0QQ5A2zI4HcV9kOLLRdSpYA1UISnndfo8mntJHlSw2bsDI2bPfajMaaOoQtbpjI-DTnEbire8rwXrxJtC83zeNj0AdBgHqb3qxWIHpCBwFgV-zkwsVNG9ObYhk3CL-q9GyWYH88uXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Be1WnCwX5i4XKiIdM4IIiP9f1gQTelI-ZlLsGva0njWlyxuICKTGwLmDL8h9vxxYmHoDTQCnWCimcNdNQZ2MOKhTsKc53Zfr95QovzECkcgCR1KaoIpDDNdgEU-LD732bBlORbTSCs-GyWX3dLb3kDIc0u4CKzkf-BIy5ACnLmvdiWV3iakawLh9clv0pKfo4f4t0NCxrFavc6a3AFeQSezssEt6NOgQcM2u9Q7e4jdFJ9fiO4ne4TWtGUy4w_Qfg8OH7AMdcasJ71o4vp_iAsGUfr7s8DeJ92-2VYiwvOl8J6xEqCD8vRC1E1mjr6JCI2oX2KepCWGpevp2yDjnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEw-20bMjOf0a99HRmtWw237k5wTmfpqch5FKSOUIQhJ0y12S0xI47kfExEevl9LCkVe5-FH1NZnc8Daxaxa-FN4Dk7lH0kNYhVWsTd2JbJvcmhPv_8ldgryLTkrdvPq7qxlIbEvcgJkWO5P7X9o6Cz1YzruRIaoKYqfwPfIu1Ic9qi8pAW6hkUgbLHzr3J-a3XL9sDxWYXoHN6wYIsliegLZWDLqVgBg0RcVOmiAMuGc1cXZwUgH9T9yQp3RMkjAXHhfd2MZ93FfhoW9_8uSwBnjmqkLdY_TKBrzxCoBBk5I3gfmDQHI-Pf2pTkQCRP8vsVZBZY92KGkFDDIgVXQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر می‌خوای انگلیسی رو درست و اصولی یاد بگیری، باید تفاوت این سه مورد رو یاد بگیری #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/685310" target="_blank">📅 18:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685309">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e51a21852.mp4?token=jkZEvJOWZF_vns3msU56V86PDZmHtzI8OtR9JPa9DpMVNimDJo_NSQRB78MUpn9BiWoqkYWWBg6wMHQlYSgIALmjO0mZItNOdI_usEI4rp7uu9kNYqh91FtwBhufa4R0sQX4VjS3Y5qDUJKUo71i8f_rzEsAmVEkdGihjL83D1_iePzAABxFUGBR2weu7jZFse4AMCvZhDsZU6eip-xTdnb8v9ltKvw9Z838__7trSLEAjCyFKgurX7--7Naa0yj66J413-7aVoAbTXPshFKwL9veN3yEBtcJL-xpxyuPlqAey7bv90TpVZ0e2T9OUmW1rYvXPEZseEy7Xqc6eWNoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e51a21852.mp4?token=jkZEvJOWZF_vns3msU56V86PDZmHtzI8OtR9JPa9DpMVNimDJo_NSQRB78MUpn9BiWoqkYWWBg6wMHQlYSgIALmjO0mZItNOdI_usEI4rp7uu9kNYqh91FtwBhufa4R0sQX4VjS3Y5qDUJKUo71i8f_rzEsAmVEkdGihjL83D1_iePzAABxFUGBR2weu7jZFse4AMCvZhDsZU6eip-xTdnb8v9ltKvw9Z838__7trSLEAjCyFKgurX7--7Naa0yj66J413-7aVoAbTXPshFKwL9veN3yEBtcJL-xpxyuPlqAey7bv90TpVZ0e2T9OUmW1rYvXPEZseEy7Xqc6eWNoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی دست استاد خود را به نشانه ادب بوسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685309" target="_blank">📅 17:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685308">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
تصاویر هولناک از سیل روز گذشته نپال
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/685308" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685307">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77a4fd2672.mp4?token=G5NhE3tGSq1zFFIkspvklZQBEkxc_ys6YHUFiV3PbLPXDof7XIKt3QL9G_YI9_UYoaXRvuxSI92YOFygyA1s_S9fJPXBkDa6gQh9JMY2R7XOYluuYhEuKpoZQAGofzEubUhC7C3E5BVPPEyPotLzzDwTo31gVELkxuOVA60Lf6FgokiTLzEzZlHdd0xslfcy__hAh0sCfuMl4iEpVIPEHCLlz5YKpCdCrNPXhbf_Js-0gkfFCYqKx97wjxc7qBfLYHWpHDl79WnDDwOfy_iBs6Lkx2Kfm-eza_PnEko7rhzQolkSHeYomydYyIDECkkBW2g3LU3AUzMbeZl_XPfPrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77a4fd2672.mp4?token=G5NhE3tGSq1zFFIkspvklZQBEkxc_ys6YHUFiV3PbLPXDof7XIKt3QL9G_YI9_UYoaXRvuxSI92YOFygyA1s_S9fJPXBkDa6gQh9JMY2R7XOYluuYhEuKpoZQAGofzEubUhC7C3E5BVPPEyPotLzzDwTo31gVELkxuOVA60Lf6FgokiTLzEzZlHdd0xslfcy__hAh0sCfuMl4iEpVIPEHCLlz5YKpCdCrNPXhbf_Js-0gkfFCYqKx97wjxc7qBfLYHWpHDl79WnDDwOfy_iBs6Lkx2Kfm-eza_PnEko7rhzQolkSHeYomydYyIDECkkBW2g3LU3AUzMbeZl_XPfPrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روابط نزدیک ایران با چین و روسیه می‌تواند فشار آمریکا و تحریم‌ها را کاهش دهد/ آینده اقتصادی جهان در آسیاست و ایران، قطعه کلیدی آن است
دکتر بیکلینی روزنامه‌نگار برزیلی و استاد روابط بین‌الملل در
#گفتگو
با خبرفوری:
🔹
اگر ۱۰ تا ۱۲ سال گذشته را دنبال کنیم، روسیه و ایران بسیار بیشتر از دو دهه قبل به سیستم مالی چین متصل شده‌اند. امروز ارتباط اقتصادی در قاره آسیا بسیار بیشتر از حداقل ۱۰ سال پیش است. من معتقدم چین پروژه‌ای برای تبدیل‌ شدن به بزرگ‌ترین قدرت اقتصادی جهان دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/685307" target="_blank">📅 17:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBxWpWavJtUr5IoFSu4EHGtZIcKekShavLsQtfpPH68CpQQQSCYkie7Xw4Nf-HygQNBN0uX2PKBumXphN-zYI3yU05FAVmMNs9cjdfIsLcHYeJRMMDpskPqClujWtxdcjQ-wtMFtjzswKkw2kDIGtxz6q13EWXuZgotvR_QUgM6hHFhOUdWPnPbWccY4u668nhvW6aCz2oh5fZ25KLplQPwu5EtjoDJIzWrqE9pi-kJzFFxJqyCapgWQ55u8X8YI3OG7Ywj5EPlRpeC7K_3dsJBSUIgqu89JF7JYBzSuRB07caZxGSxtaQ7Bl56CFhue8z1_T2vzQX0P-2I_8DVmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نکات مهم انتخاب رشته کنکور ارشد ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/685306" target="_blank">📅 17:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817d078ff7.mp4?token=avmXYOQtD7S0GOJ2pS9e6I5QdlQiG7Sch68Btkic23SLyfvcGmRF3o-QNuu5VS8dQPCQePUI8t-LDryL00EnNpIsY1o5cgJ8_ab34WLqTn6sZnqvS0RTtmTRloY8NHf5F0QhtjxXXDhWbe9u7nzhFbbZPLXMz9N_3463Y4xErd2Ce9Uh3BR461bOHXp_r2qBPshei5HLwYDhDP3yuUnb3ZN7sEO6Xl0GJjXJmgQXQDWAlN2xPXzXAgKnAbYY9uxRyxSn1MzeBfOcB0uY31JwXUdaVVEXWOlcqunt_FYwUSgU-23s6q5eQvXKPEIAUWzDkQtAz_OxD72oDQB1R6HSuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817d078ff7.mp4?token=avmXYOQtD7S0GOJ2pS9e6I5QdlQiG7Sch68Btkic23SLyfvcGmRF3o-QNuu5VS8dQPCQePUI8t-LDryL00EnNpIsY1o5cgJ8_ab34WLqTn6sZnqvS0RTtmTRloY8NHf5F0QhtjxXXDhWbe9u7nzhFbbZPLXMz9N_3463Y4xErd2Ce9Uh3BR461bOHXp_r2qBPshei5HLwYDhDP3yuUnb3ZN7sEO6Xl0GJjXJmgQXQDWAlN2xPXzXAgKnAbYY9uxRyxSn1MzeBfOcB0uY31JwXUdaVVEXWOlcqunt_FYwUSgU-23s6q5eQvXKPEIAUWzDkQtAz_OxD72oDQB1R6HSuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد علی ضیا به مدرسه‌های غیر انتفاعی: ۲۰ نفر از بچه‌‌های کلاس دوم ابتدایی را به خاطر نبردن برگه چک ثبت‌نام، به کلاس راه ندادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/685305" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/710bec86ee.mp4?token=a-3jH_GXuwCX8F2ci09cxt1nXAWC5r4mrBSQDjmtTu_sGuRexp8jiuF1ACd6m6Cwh_2PGsLt1gaaAiqMDDlHRjeBCs40WYUcOM2yAib-hJ9nUEbCT9NdJyC1Bn43Q-TF5ecy1A7dxZJWS36eqNVxzOJzbeU0jYQmBoGVXQr0KeOQ4y3CkQbzismcf6dkkmC4yzN_BcD3fw-CBNCSk3A041LIZzA6A6LIP-7ruAOnYi65xM9IjkuZva-Tz26VvhGTEx09hzO9S0rBJzognb_GVv8UBYxwVl-nftJBKan3Sb1NeMp7aHdq1DQ02lZlbBMvpbFHvAHtBvP5CV84n7-LIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/710bec86ee.mp4?token=a-3jH_GXuwCX8F2ci09cxt1nXAWC5r4mrBSQDjmtTu_sGuRexp8jiuF1ACd6m6Cwh_2PGsLt1gaaAiqMDDlHRjeBCs40WYUcOM2yAib-hJ9nUEbCT9NdJyC1Bn43Q-TF5ecy1A7dxZJWS36eqNVxzOJzbeU0jYQmBoGVXQr0KeOQ4y3CkQbzismcf6dkkmC4yzN_BcD3fw-CBNCSk3A041LIZzA6A6LIP-7ruAOnYi65xM9IjkuZva-Tz26VvhGTEx09hzO9S0rBJzognb_GVv8UBYxwVl-nftJBKan3Sb1NeMp7aHdq1DQ02lZlbBMvpbFHvAHtBvP5CV84n7-LIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرز تهیه کرپ چینی فوق‌نازک و ترد به سبک حرفه‌ای‌ها؛ یک صبحانه متفاوت
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/685304" target="_blank">📅 17:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685303">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkkjT9Pe5Iwsl7beYWA272vEyFmMkfkbHoN9RjjIyLe4cYpHz9X5DNOq3mEyM7713BagXCgAKvCl17nwxParkZmz0fF9SzT2lRwavnJCF56X4f9pnZBOw3j3Tg6NlQiOfahIA_tPjIik5EiNaJdGMuCmxNOBp_CRhUfa_vurAXNaXkgrTWcZmtFdOqdbRb_EIaJgPPs4oeXJl-5G3SdbbgJxqH6ZwVlMolnHUh5ZS-XaTWlf8dWfY1Ue3Y55Wd8fIogYLJJ4Z_5hBeErSc6igaFGcYZVBhRo_z02t6aj3xnFeX8UFnzNB7UrTXQfPN-8Sm8CbABWQT_GZUn5_ZKY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلایی که ترامپ از آن می‌ترسید، سرش آمد
🔹
جیمی کارتر، رئیس‌جمهور ۴ دهه پیش آمریکا بود که ترامپ با تمسخر ضعف‌هایش، برای خود در انتخابات رای می‌خرید و می‌گفت که نمی‌خواهد شبیه او باشد.
🔹
دو ضعف بزرگ کارتر که در تاریخ آمریکا از آن یاد می‌شود، عبارت‌اند از: «شکست در جنگ با ایران و تورم برای مردم آمریکا.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/685303" target="_blank">📅 17:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685302">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/685302" target="_blank">📅 17:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685301">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8l2ADyhr-c_p8l7kOXHPYQ5SjwIoum3RUCcxbtv9agg6Ep60vFOg0-EG-54Ca23fofwm-TVUkzvfBiHTEYuU4XOp4CtxV-JNppVb5pAB3BLOCzAeMn6U4ciLHBRfbtcAGgO21BElaHykb2qpHtEEiOVpwImBxdzlBuZ-Xbu3Rl7TKf1OJw50zyYgbhTCgX9zP02x0Ym70F9dkTJSQoKHq5x_EFaO1qyAPYN4p-FecTwHkEZL-vKG0BfnNqFJlE_tv0yjpK1Ckh46HnmyHsaDsrpJ2SGe1XUZP8gR43sHnaayca53fXw2u39rf1Pqrcm_2oQA5xYcvsVYdkZj5mAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستگیری یکی از سرکردگان شبکه تراستی با بدهی ۷۰ هزار میلیارد تومانی
مرکز اطلاع‌رسانی پلیس:
🔹
شخصی به هویت معلوم «الف .ل» از سرکردگان شبکه تراستی که طی سالیان گذشته مبادرت به دریافت ارز حاصل از صادرات نموده بود.
🔹
بدهی این شخص به شبکه بانکی بالغ بر  ۳۰۰ میلیون یورو یا به عبارتی بیش از ۷۰۰ هزار میلیارد ریال می‌باشد و تاکنون از اجرای تعهدات خود امتناع و متواری بود توسط کاراگاهان پلیس امنیت اقتصادی فراجا شناسایی و دستگیر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/685301" target="_blank">📅 17:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685292">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoPydUnolIMCgQpH2HuHjIIHCiO2tyJf4nzfx0oc73inV8-dUgcVD6kxF-xsqtz5tCqQQCJY2g2HbKX6u4cSZB7_g5B3ArPA1_v9G37nZbeW29K6oRnNzPtT5HHUrcBkmJuJar62rvDIlc5Q_PJSjskRwOuc61bRQ5FhUq1JUYdxywWMjPlx2MJpyNbI7NJx-106q9I3hjEstsP3TusP_bwT3tEV0gXyFEvTONXNqTj5LClU4-ehReza6FnAhUoBXRh5xq3OPtuCrgCux6xtPdqP4vxpk4GgI-bWDdciGF2A56tlGY_cTlpwWYOvhyRCD3GC8p-ytH1p_34wekvhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b36cc97a.mp4?token=GTFBalYgoJTBhQOROk-cfojQ1ftiyQhb4HN1YRxZjTER9KGwR9cwn9JC9BoBlFLbItltQ1ToNvjFiNwETZ5s44R4qyDiiqpZPgrYEFCLx4jRmlnQVYNPiXfuzOMgg97ykEHxKF7Anv9tS1381_Bvap5ZS39Z_cn_ZmcsHjUqck57nD_yCgPnc3Fz4AniXot-jqD_u88WQ1KqOHttP1E17ZOGoz3fAIZ5ycuu3QBmcCe6lUtYp1Jmx_jCZ60ursmINCB7jwPM6v56I50IiTJswlHu8bWKrdF9eGoXTYygSZH7Vv9G8zvozvXmbUE_T_Ki7_sM_NZhZVHQlGIToEKtbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b36cc97a.mp4?token=GTFBalYgoJTBhQOROk-cfojQ1ftiyQhb4HN1YRxZjTER9KGwR9cwn9JC9BoBlFLbItltQ1ToNvjFiNwETZ5s44R4qyDiiqpZPgrYEFCLx4jRmlnQVYNPiXfuzOMgg97ykEHxKF7Anv9tS1381_Bvap5ZS39Z_cn_ZmcsHjUqck57nD_yCgPnc3Fz4AniXot-jqD_u88WQ1KqOHttP1E17ZOGoz3fAIZ5ycuu3QBmcCe6lUtYp1Jmx_jCZ60ursmINCB7jwPM6v56I50IiTJswlHu8bWKrdF9eGoXTYygSZH7Vv9G8zvozvXmbUE_T_Ki7_sM_NZhZVHQlGIToEKtbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💚
#استوری
کلیپ های ولادت پیامبر اکرم (ص) و امام جعفر صادق (ع)
✨
از عرش پیام سرمدی آوردند
بـه بـه چـه مه زبانزدی آوردند
در روز ولادت امام صادق
یک دسته گل محمدی آوردند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/685292" target="_blank">📅 16:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685290">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0IMff-RKMILoN8ript04lkBt7Mblm3CLQn8Uz6lKuIN1B72MWxL-2lWiHSwFSEqZeIMyNcgA2eBh0rASC6ZYTaxkJg16jYxMWugPou5YNMGup6_uqTQ83af_vbNTs7QKdioNff_jq5wG037ZPScuNfwKBG0MQ3hxkZvZdHmFhyr56Iu4jYC6IF6jh4RdA8oM2uPu7oaCN-BFjL102_qzLntTbMn069z8h3UWtbmq0lI5FxVKgC98-YlB9P8ppINNxuXTDTN3My8ZpSLv8xIDRy1v5OaJkGTOwXMtRK6dKC1VQs-d6dVj6RKMTnxigBI340cATo9QHqmYbZ1e_CLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آب چغندر؛ نوشیدنی‌ای که از کلیه مادران باردار محافظت کند
🔹
پژوهشی روی ۱۰۸ زن باردار مبتلا به بیماری مزمن کلیه نشان داده آب چغندرِ حاوی نیترات ممکن است به بهبود جریان خون و کاهش برخی عوارض کمک کند؛ البته این نتایج هنوز اولیه‌اند و به تحقیقات بیشتری نیاز دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/685290" target="_blank">📅 16:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685289">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1e225587.mp4?token=sm6C4SaGtwwbIjrSPhKWvvrRjo828cm2hZFsmG37ajS-0OEi2kDdpnRUgRhDmlAFZLQ3nLxcHhgqMop6jfxlHc1CO88VBoGP4SXCQoo2fkuqgNYM1Jk6_tAqomf19ox9zghgPchQuGWmaZaevmh4jQEqbWdzY5NYpIkg37neBO1_3sB0VLQ2NlIQL_H87jpFB0On7EQ58DY4TzGjl6lzUJtgvpVqGozDJjJ8d_WGQNj7O1f-zwodW_YKnA9YeVPixGXUTwjB6CPgtXkcI3YEnn2QBrA5E_gguimXuO06zt-sbJLTx1rkwad83KXRx_iiO2VtfB81K47x3Syg2E_WCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1e225587.mp4?token=sm6C4SaGtwwbIjrSPhKWvvrRjo828cm2hZFsmG37ajS-0OEi2kDdpnRUgRhDmlAFZLQ3nLxcHhgqMop6jfxlHc1CO88VBoGP4SXCQoo2fkuqgNYM1Jk6_tAqomf19ox9zghgPchQuGWmaZaevmh4jQEqbWdzY5NYpIkg37neBO1_3sB0VLQ2NlIQL_H87jpFB0On7EQ58DY4TzGjl6lzUJtgvpVqGozDJjJ8d_WGQNj7O1f-zwodW_YKnA9YeVPixGXUTwjB6CPgtXkcI3YEnn2QBrA5E_gguimXuO06zt-sbJLTx1rkwad83KXRx_iiO2VtfB81K47x3Syg2E_WCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه فکر می‌کردند ایران ضعیف شده؛ اما جنگ ۱۲ روزه و رمضان تصویر دیگری نشان داد/ ایران قدرتمندترین کشور اسلامی در جهان امروز است
دکتر بیکلینی روزنامه‌نگار برزیلی و استاد روابط بین‌الملل در
#گفتگو
با خبرفوری:
🔹
بعد از تحولات سوریه در اواخر ۲۰۲۴ و تضعیف حزب‌الله، بسیاری از تحلیلگران بین‌المللی تصور کردند نفوذ و قدرت ایران در منطقه کاهش یافته و تهران دیگر توان پاسخ مؤثر به اسرائیل را ندارد. اما جنگ ۱۲ روزه ژوئن، این برداشت را به چالش کشید و دوباره بحث درباره جایگاه واقعی ایران در معادلات خاورمیانه را مطرح کرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/685289" target="_blank">📅 16:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685288">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67f6fc6f8.mp4?token=JGmbAUCcXrnbtVGp1-TDGh8PFEYGAwaGJal66vGRK_TinyVFlFbVb5Tao23Dlyz_u-E8LdiW39Yej9Z_JHNanel4ipQFvDq-2KiXd7gSFlu2Y-oytMmlEtYJpugqUazTorCyFfS_3ctfKZOj7xsANsdV2WmRH1cm8P7vWfZ0s6CljSAXfRy6x8W8LBzz8R3nuhbI1RYu0lidE2fUBmbULN9ZAmB4do6pLbq5jKceVYCDyBU4nFDnArFDdUiVP1dzIDry4ngNokUs_l4T4mg-XG7FnmKc9Z1Gaf1z0UDFsTiK28CJsEe97TGgMIb1h6VRRjPQe_5xRqXwuMIq4hkYZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67f6fc6f8.mp4?token=JGmbAUCcXrnbtVGp1-TDGh8PFEYGAwaGJal66vGRK_TinyVFlFbVb5Tao23Dlyz_u-E8LdiW39Yej9Z_JHNanel4ipQFvDq-2KiXd7gSFlu2Y-oytMmlEtYJpugqUazTorCyFfS_3ctfKZOj7xsANsdV2WmRH1cm8P7vWfZ0s6CljSAXfRy6x8W8LBzz8R3nuhbI1RYu0lidE2fUBmbULN9ZAmB4do6pLbq5jKceVYCDyBU4nFDnArFDdUiVP1dzIDry4ngNokUs_l4T4mg-XG7FnmKc9Z1Gaf1z0UDFsTiK28CJsEe97TGgMIb1h6VRRjPQe_5xRqXwuMIq4hkYZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای تکان‌دهنده درباره جنگ اوکراین؛ روایت‌هایی از سرقت اعضای پیکر سربازان کشته‌ شده
🔹
اخیرا مشخص شده که دپارتمان پاتوبیولوژی اوکراین تمام اعضا حتی استخوان‌های سربازان کشته شده در جنگ رو سرقت می‌کرده و به جای استخوان‌ها چوب داخل بدن می‌ذاشتن و باقی اعضا رو هم به همین شیوه سرقت می‌کردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/685288" target="_blank">📅 16:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685287">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pk82BLmZpCIobIhmpl4J1WwzyahZ1vb5JXU2Qc7IE5rgoKjLy0Fe6URB6RZnAT99ECR1BFRcj7SRWe6A59jlLSpWqUePZBqUiA5wF75Uqfu3hra-I0KYwDDqRtOY7xNXMDiQy_ENcXboyLMTiYTKCyVRCVoTIzmrzeh5ZDgfWgytEjk2D0I15EI2fS8tPMTzxEuHPB-csMctVz9xlvUBxxc-AIfTslm-_snT7QN_WgcOTJ0lb9RVvsWWOr67U9CT-Ea5-g7GzxOUOueFkBJI2nALotYr5w0uQjfy2H-5Ct-K815FYx9t6G2KeTZfOJnjgELjB7k_60a1Vazfg4iY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی‌ها چقدر بازی دیجیتال انجام می‌دهند؟
🔹
صنعت گیم در ایران به یکی از فراگیرترین سرگرمی‌ها تبدیل شده و بیش از یک‌سوم جمعیت کشور را درگیر خود کرده است.
🔹
بر اساس آمار بنیاد ملی بازی‌های رایانه‌ای، ۲۹.۳ میلیون بازیکن در کشور روزانه به طور میانگین ۸۳ دقیقه بازی می‌کنند که ۳۸.۳ درصد آن‌ها را زنان تشکیل می‌دهند.
🔹
موبایل با ۹۴.۵ درصد پرکاربردترین پلتفرم بازی در ایران است و از کل گردش مالی ۷ همتی این صنعت، ۶.۹ همت آن صرف خرید کنسول و لوازم جانبی می‌شود.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/685287" target="_blank">📅 16:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685285">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6939ca53.mp4?token=smeeKbG9HPS2keTIJUbMBhsN8lKO4-AtkRKhq5uMrVAckWnFheBuuRaxFK565QqnbdOLI4va2M3Xptjbf07TToer_UFK6cI9jj8IIjS6W6I188ICZfL6IqA-vVyie7V0auGRSMIgqxmxVkM9pe-F-ICUhYp3V525aeGX-Tyy-lLqsyf6xjxLxS_Qxd2TxFRrPILvTVyX8N4h9Oaas1OagS9lldyr_kBn1Ha7boedcEoOagM39LNrokKuhOf-9fsMBqiMruTYkjgo-bk4Sf6fR8Du3CqOZt-2WWmqOI-KPTwQis_fUIjXlRr0kwMoDqeMUU-qf7702_q0pv3ELoXpgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6939ca53.mp4?token=smeeKbG9HPS2keTIJUbMBhsN8lKO4-AtkRKhq5uMrVAckWnFheBuuRaxFK565QqnbdOLI4va2M3Xptjbf07TToer_UFK6cI9jj8IIjS6W6I188ICZfL6IqA-vVyie7V0auGRSMIgqxmxVkM9pe-F-ICUhYp3V525aeGX-Tyy-lLqsyf6xjxLxS_Qxd2TxFRrPILvTVyX8N4h9Oaas1OagS9lldyr_kBn1Ha7boedcEoOagM39LNrokKuhOf-9fsMBqiMruTYkjgo-bk4Sf6fR8Du3CqOZt-2WWmqOI-KPTwQis_fUIjXlRr0kwMoDqeMUU-qf7702_q0pv3ELoXpgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی تماشایی از قدم زدن فلامینگوها بر روی دریاچه مهارلو
🦩
🔹
ویدئو از حسین پوراکبریان
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/685285" target="_blank">📅 16:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685284">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
گام بزرگ ارس در مسیر توسعه | مروری بر پروژه‌های افتتاح‌ شده
🔹
همزمان با هفته دولت پروژه های مهم زیرساختی، ورزشی، فرهنگی، عمرانی و صنعتی در منطقه آزاد ارس باحضور دبیر شورایعالی مناطق آزاد کشور و استاندار آذربایجان شرقی به بهره برداری رسید.
@arasfz
.ir</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/685284" target="_blank">📅 16:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685283">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead0270f87.mp4?token=Ygq17anvG0-_LWXWYDJEkqQrHqA4zEo5NoxL4vdt7RkrYFzhfMKldpQUNaDQNr8E92Y2isSndbLOHGd2cIMfs6QQt8mbZ-Z83h5_rXt5RfaBueCjbCaAbFovHUYsF_fcTDQm6ui_sm0IGzLvWTf4k86C6fjg2q-lrLgK-KvrOdBAe_b6NInTZDpHUpQcLbHog9S-NhNynuQC7e_e-X6SvWKe0ieY5yxyEoKoKpWz0qiOLih7tgubkcQY80dj92ERLIqPt6DNxQCxsdHVZdh4G1RXoHPFAZ9uqtDvedd6DRwtgVBajrALR6iyQqIOsIpa5n7leqDOeQWWPA_f17nlCHVZwV5kfFi8ryAX4iBqtrwKK7oku794s23_suz5OxCvbfET4UHNW2WWTdtzvG8q8KC-uXgZOi6Dg1Wn06KCX0OVU1K67yX-ntbmSyGX5tv62EYl668zaH9i2I9nkB1KSUbLHPg5jWeQN0I856a_4FsMwM95jhn8m_dTSg31sqCEa5kYLNYKJeDZJEDPoN4bVFrpjqInnk7tg_cAyD59kFx0s7y_U_pGbajzz7Dk6XmCxNAZCpfDP5q09fy4l5HWQB3rUanzT-2CpbLwk-wyhMRHj9vXGcNiOpyf4vIORsyXB0z8IpgsuE6gX8DCgeOp6sWbCNLeSZkJVl-FJxnf8bE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead0270f87.mp4?token=Ygq17anvG0-_LWXWYDJEkqQrHqA4zEo5NoxL4vdt7RkrYFzhfMKldpQUNaDQNr8E92Y2isSndbLOHGd2cIMfs6QQt8mbZ-Z83h5_rXt5RfaBueCjbCaAbFovHUYsF_fcTDQm6ui_sm0IGzLvWTf4k86C6fjg2q-lrLgK-KvrOdBAe_b6NInTZDpHUpQcLbHog9S-NhNynuQC7e_e-X6SvWKe0ieY5yxyEoKoKpWz0qiOLih7tgubkcQY80dj92ERLIqPt6DNxQCxsdHVZdh4G1RXoHPFAZ9uqtDvedd6DRwtgVBajrALR6iyQqIOsIpa5n7leqDOeQWWPA_f17nlCHVZwV5kfFi8ryAX4iBqtrwKK7oku794s23_suz5OxCvbfET4UHNW2WWTdtzvG8q8KC-uXgZOi6Dg1Wn06KCX0OVU1K67yX-ntbmSyGX5tv62EYl668zaH9i2I9nkB1KSUbLHPg5jWeQN0I856a_4FsMwM95jhn8m_dTSg31sqCEa5kYLNYKJeDZJEDPoN4bVFrpjqInnk7tg_cAyD59kFx0s7y_U_pGbajzz7Dk6XmCxNAZCpfDP5q09fy4l5HWQB3rUanzT-2CpbLwk-wyhMRHj9vXGcNiOpyf4vIORsyXB0z8IpgsuE6gX8DCgeOp6sWbCNLeSZkJVl-FJxnf8bE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای آذر منصوری: پزشکیان گفته نه تنها استعفا نمی‌دهم بلکه برای انتخابات ریاست‌جمهوری بعدی هم هستم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/685283" target="_blank">📅 16:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685282">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceHRbWM8AQHajoXs2a6LQuGX05JkLzxR9G2414yyD2DSuxTT4j051Sws98Qxhyd7PyXFmHvUQYsv2ex-UdVhwPa2W5NiuYigkMgyJeLlplxlPaBKJCfIxkGQ_ywETXhbVoFtWZqRw84WycMhkUmiN6-Q4rSm6QN1SGciaR_rVAEVVZlxqiUR2JmgDtN6DEt382r7dmWvLbhrvRXDTHVuLKZ0r9K2jjUN09VzA_hRG30yssFXipinjzWtbGkCI554MRlGiTFUeIPXXeQ7aR-WmbVAyZKevL5_W9BPzyCq8K0QVPOv066xXkb3u8E5-a1CbIf7iSaR7WOnc-Hhnq6JzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدام عجیب دانشگاه اکستر انگستان: توافق با عربستان سعودی برای آموزش افسران نظامی!
گاردین:
🔹
در قراردادی، استادان دانشگاه اکستر دوره کارشناسی ارشد را در دانشگاه دفاع ملی ریاض ارائه خواهند کرد.
🔹
دانشگاه اکستر طرح ایجاد یک «مشارکت رسمی» با عربستان سعودی برای آموزش افسران ارشد نظامی و مقامات دولتی را تصویب کرده است؛ تصمیمی که به‌رغم نگرانی‌های دیرینه درباره کارنامه حقوق بشری دولت عربستان اتخاذ شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/685282" target="_blank">📅 16:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685281">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e0dfd548.mp4?token=RrmjcCGAi2Bo9bxV1JEVCgQg5LtPE4VBvwBnJc--hx8x7vNSNe0H2hflTSvgJuZdpELfMVtomOQDoC03jDw-PtzawqLKjk0RKhS6bgEAhYl4OI1916hjso5YlZ8ykByfI46FF_3PjcT2fCU9KnbyGiPCaYGopCkmqh1qTR2IZzGskXNO67QTPEpY1SNKwRbDdpHQm8-Hz7EnKK2mq7o6g0YWWJQGBfyb0rcGFs6mSlmRMjCr1TMHoDjzjEuW0g_yAVliE7mBPgMrv-o6HuzRC9LePWUE6ZRRsB10YnSxQ-QtTm-l6v3d3ZWBw6lvZ706W2pMEFwY3tGUWHpx_okCeYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e0dfd548.mp4?token=RrmjcCGAi2Bo9bxV1JEVCgQg5LtPE4VBvwBnJc--hx8x7vNSNe0H2hflTSvgJuZdpELfMVtomOQDoC03jDw-PtzawqLKjk0RKhS6bgEAhYl4OI1916hjso5YlZ8ykByfI46FF_3PjcT2fCU9KnbyGiPCaYGopCkmqh1qTR2IZzGskXNO67QTPEpY1SNKwRbDdpHQm8-Hz7EnKK2mq7o6g0YWWJQGBfyb0rcGFs6mSlmRMjCr1TMHoDjzjEuW0g_yAVliE7mBPgMrv-o6HuzRC9LePWUE6ZRRsB10YnSxQ-QtTm-l6v3d3ZWBw6lvZ706W2pMEFwY3tGUWHpx_okCeYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بخیه‌زدن بادکنک بدون ترکاندن
🎈
🔹
این تمرین یکی از دشوارترین روش‌های آموزش جراحی و تقویت مهارت‌های حرکتی ظریف در رزیدنتی و جراحی است. کوچک‌ترین فشار اضافی یا زاویه‌ نامناسب سوزن، باعث ترکیدن بادکنک می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/685281" target="_blank">📅 16:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685276">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdESKUkirgUT2MwTKH1s0Vjc7_xdOHchKpV19KVmD2sCBar2ixNau91wl8Uy4g6nwHwo8SabmbGfpeoakwMdIvr1f2-hLY1hDZ8_2an_oGzc0FxkSDEe9nxubNxXqBysEo7dqtJcMkPv0FhzEH00pQ9Vj0ECwP4xzMO8BLf5OzSUhlDDYWA2vZT_mqW0EFaDoodYnlSc-OPU3gLqFKWS1Wy1PNhazk66DtNGA3oIusWHQbZ5JBYeSldciAw7O1EkgkqQJxOoz9mpqaEvxDAZ1XFdn_BmBHbsiJu6W6ZpPDxXs7yK5w2ugMHn50QQCbLdoBWU9O3kblDNWso4mQecvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H8LZla2hMXPwmmjBTQhd_Y7WUKsyHYfRvXrZyi-uw6GT_f-8kl4Kvy3wpN5S3MIW0h6_h3C90wFTGybNmquvaA0EPB_FN0jZEyXEn6eSe1DeyNTwtTw1sZhYeYmpqdvniJ3drvMrUCK7UsA3W5HEXkecahlOrIbEDdTl_yRQ9-OJN7RXWvwb4NcdPGeEr0sMIvItcsAyzxqKDMwb4xcKVLdR3yoe7-aNqtOYpq5EDVcjMYV6a_BiCLNvKZsWBpU2fiz6_tWjV97hCEjyeAgfxPELjo_SeCxFFkDys6xYYwgElKVpQ6maFguUtzBBzwi8sdzrJ2wtWEadawwMoYeFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLeMByiloYpZx14DaYRVoD94-USIDYqS6s6v1abPxsoNxZfUqnPHWmw7QJKa-bzhf2qnNQbM2j30BxENEtvrnlRio9RDhASUkaTKLjd3AAB481svlejHOUg0GuLXW8HX_h32msI_e9fu3izSpS0IGf8XrSrb1D4NJgy9xaG6D5nnMEgfHr16uUAc5ex6TfEKtaxJlAkzG61f-irm29mmL34YrmdeITGKNXfk29CDOcvTv8An0R7G43lbBa12t36DqrtVnzMl5LdGBvwr6AKfVmuQgrW7bFu2Aw5gVS-1FkUo23RXRJOAKN4pG98WKUDWxbIzhQ6LvE-_dyqJv9YWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p8JB6hdeo7FHozC3NIzZydwum7kDCng5cixibniXBbrhZSykdzUraMsrXvAAjdWH7CA7Kem0w6c6FGlJrBL1DIW7x-RpdJAt9Lv6gR7kRKB6VXWXJPp7Om_2a5CAiDyQ00q7wB_XfMUpsYoa4Mx8rsgZ8mWqO9QfufuCfovxlXapjuJUJdn9zP509FCGYuTmjhfIcpX261STNNuK_6gdPImXwbWCk9eXYTs-3-q5qoax88yFNUduMaNCNvuV9lsR95ca6CjgeAzH42c_rH2ijVCXuM4JwwBsdVJNhuldvPQIZjAtI0jXeQ_EpEKW0dXoZTf142oehxhG1KSAxB1t9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تفاوت فارکس و کریپتو دقیقا چیه؟ توی این ویدیو چندتا از تفاوت‌هاشون رو ببینید #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/685276" target="_blank">📅 16:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685275">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKMC</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqQDKqwKQMUKKRxzFRvlMVnRPZ5UE-obYk4OxG45GpZjSa1kkJbkuckEoU-3RBx-kl8vv0p6jL4xQBbpQVu7yyVa1JaNuCKsEjCybiOIm_H-HAFZqjjDzJEwDr-PCfkjC4RnxkBPniKmjzTOz4v-bh7iuE-NLhUybE0UFTX4HuSviY3oWUH44tZ7UBu_NhsrylIsLqu3YENsl5oVdP1_42FcjgEZzzx17wKjZGeK9BFnfn02RwPbdffFf8ERyF5NJZjVIXvsR1sbqpCHV5xkOYRBYv7qhXach--KBH7PsxnyN7lri80S1CoWomefgxR01zVPKzveq0CrJvVrxayC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
پیش‌فروش  BAC X3 PRO
ثبت‌نام: ۷ تا ۲۱ شهریور ۱۴۰۵
پیش‌پرداخت: ۱/۵ میلیارد تومان
تحویل: اسفند ۱۴۰۵ و خرداد ۱۴۰۶
مشاهده شرایط فروش
#kermanmotor
#کرمان_موتور</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/685275" target="_blank">📅 16:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685274">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فیش معوقه فروردین بازنشستگان تامین اجتماعی در دسترس قرار گرفت
🔹
سردار ابن‌الرضا: از ساختن قدرت دفاعی ایران دست نخواهیم کشید
🔹
مخبر: ملت مومن و استوار ایران، محاصره را به شکست محاصره‌گر بدل می‌کند
🔹
شرکت ملی پالایش و پخش: کمبودی در تأمین بنزین وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/685274" target="_blank">📅 15:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685273">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e657f150.mp4?token=QVeKmYdFF_wtDSTtmMMMXWXSjODGxXMlSy1dTGxeEbrFZkIaziPD62ZHcCjeLxoAiUn7ib0BRQBBioLKSHnnmNVliXZ_FUr9OQaR39g4GAS7_V9JrOA8BtTuZ3KgFNA-WRSSNHLXtqD-wHFYgwFvBxe7jPdf7srkZqdxw7xY-5SCBMdLVtt-m_TL3Hnz4UcNB7DbCykNQT6aHTpcwbZDJyzCQktb_mroqKsN9lMbx1sLg0uL8f6HPzdSWufIKsHu4UrYX4fRPtCHMSFhRUoE1zYsQaGj1t5AFpjH7w7Kg1PlTE2gL8jybfGauBSOCH-MJ6Y0nMjiFhNksRO-Vra1xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e657f150.mp4?token=QVeKmYdFF_wtDSTtmMMMXWXSjODGxXMlSy1dTGxeEbrFZkIaziPD62ZHcCjeLxoAiUn7ib0BRQBBioLKSHnnmNVliXZ_FUr9OQaR39g4GAS7_V9JrOA8BtTuZ3KgFNA-WRSSNHLXtqD-wHFYgwFvBxe7jPdf7srkZqdxw7xY-5SCBMdLVtt-m_TL3Hnz4UcNB7DbCykNQT6aHTpcwbZDJyzCQktb_mroqKsN9lMbx1sLg0uL8f6HPzdSWufIKsHu4UrYX4fRPtCHMSFhRUoE1zYsQaGj1t5AFpjH7w7Kg1PlTE2gL8jybfGauBSOCH-MJ6Y0nMjiFhNksRO-Vra1xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور کندی: من تسلیح کردها را در نظر می‌گیرم و به کردها می‌گفتم هر بخشی از خاک ایران را تحت کنترل یا اشغال خود درآورده‌اند، می‌توانند به‌عنوان سرزمین خودشان حفظ کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/685273" target="_blank">📅 15:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685271">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7847268ce8.mp4?token=f5TyAunnLzJuO7rAOKULJUZxuyiLViIZz5SjLPX3H_kPlOuDrdKkbBrFeDo5udG9vsW08Sy36yAklSIneqfTPkwzy-H-9OQ0LJVCZBVw0EnH84C1S9JHDpD0nW0peQy0w5U6oibjFjtL7x0GERyzNSBla1LBtRBglEiSmbJ5Ejhhkqb2tFnCy9wf0JfgejqRu3g1BbXGhxTJAFHdwK4auA_H7wgfg0-N2logjB8AXyqEReRUUJgE6KFQjNvkEIQ8TVdAl7Sbbo7N7EcmlKTHehvNCm09SB1GjKZsYErHnMr9zOal1OOpyZRATqtWGbmS9hY_QwQJYr1Tvmp9qJgM_FN2h_q28Uq71YScKAryd97qOE9n7aADw7HNY28fRYeMwjt8-gUqnhg6OOAvjrd-XDgl0HcV6VJ9dJcr78MGfmW6ouKd_T6eh_OHXbJrmp5xVHpiMGBZPjjalBnM2T0rDjVJtuugDnopzBH9nBWwKuzqUREFZBnzOGZselUVsVxnY8rnvXYKXDQixHIGUPf-Lo37ma235y_3gxfD_OWcq8NysurNL_lHVCBG75l200kQ34jS5tsVlH18MJR-Li4Suj_ZBFABLA-4ihhHLQNo-Vkpuw4RsXV2r-b55YCG91aFIN-TzwQba_vbbpHarwfC3pvogbKTjxmOe0ZIRUuSLyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7847268ce8.mp4?token=f5TyAunnLzJuO7rAOKULJUZxuyiLViIZz5SjLPX3H_kPlOuDrdKkbBrFeDo5udG9vsW08Sy36yAklSIneqfTPkwzy-H-9OQ0LJVCZBVw0EnH84C1S9JHDpD0nW0peQy0w5U6oibjFjtL7x0GERyzNSBla1LBtRBglEiSmbJ5Ejhhkqb2tFnCy9wf0JfgejqRu3g1BbXGhxTJAFHdwK4auA_H7wgfg0-N2logjB8AXyqEReRUUJgE6KFQjNvkEIQ8TVdAl7Sbbo7N7EcmlKTHehvNCm09SB1GjKZsYErHnMr9zOal1OOpyZRATqtWGbmS9hY_QwQJYr1Tvmp9qJgM_FN2h_q28Uq71YScKAryd97qOE9n7aADw7HNY28fRYeMwjt8-gUqnhg6OOAvjrd-XDgl0HcV6VJ9dJcr78MGfmW6ouKd_T6eh_OHXbJrmp5xVHpiMGBZPjjalBnM2T0rDjVJtuugDnopzBH9nBWwKuzqUREFZBnzOGZselUVsVxnY8rnvXYKXDQixHIGUPf-Lo37ma235y_3gxfD_OWcq8NysurNL_lHVCBG75l200kQ34jS5tsVlH18MJR-Li4Suj_ZBFABLA-4ihhHLQNo-Vkpuw4RsXV2r-b55YCG91aFIN-TzwQba_vbbpHarwfC3pvogbKTjxmOe0ZIRUuSLyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنها امکان برای یک غرب آسیای صلح‌آمیز، این است که ایران به بزرگ‌ترین قدرت منطقه تبدیل شود
دکتر بیکلینی روزنامه‌نگار برزیلی و استاد روابط بین‌الملل، در
#گفتگو
با خبرفوری:
🔹
اگر ایران حتی قدرتمندتر شود، منطقه به سمت صلح بیشتری می‌رود. من هنوز معتقدم نوعی توافق میان ایران، عربستان سعودی و ترکیه، با میانجی‌گری رهبران پاکستان، امکان‌پذیر است.
🔹
اما امروز می‌گویم تنها امکان برای یک غرب آسیای صلح‌آمیز، این است که ایران به بزرگ‌ترین قدرت منطقه تبدیل شود، اگر مقاومت کنید و حمایت داشته باشید، می‌توانید امپراتوری را به چالش بکشید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/685271" target="_blank">📅 15:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eaad60905.mp4?token=AqywPrzQtLBRn1PbyjHOQkb51LeRstqyzZVk-U8GQMFUvAnDnCTVO9D1xiVA0gwboyM13vpJZqIYcTfl0U413Wa9rh-0VfJEClzg_OXvfR_CYH9SUgm0iggu61SWmJfgFHq6GthzbWVIW98Xsu_6lH1FQthb3X8wjPpC0_PSA-kYeJQSw7ATRzrN1x8AKHJRwaW-5wjC7f4MDSpiygdFk7wBnrbbbwXBwjNjrRynWt0xCadBwRglAIIV1mC9QMCWCTq4TqEf9VxlJwoFHKHcjNZHK1nNRdrftQsT_wXy_IF6Lxr7Qpx3Sd9PMEjKErOc1IWWpmrLLIKvFxBE9L4sMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eaad60905.mp4?token=AqywPrzQtLBRn1PbyjHOQkb51LeRstqyzZVk-U8GQMFUvAnDnCTVO9D1xiVA0gwboyM13vpJZqIYcTfl0U413Wa9rh-0VfJEClzg_OXvfR_CYH9SUgm0iggu61SWmJfgFHq6GthzbWVIW98Xsu_6lH1FQthb3X8wjPpC0_PSA-kYeJQSw7ATRzrN1x8AKHJRwaW-5wjC7f4MDSpiygdFk7wBnrbbbwXBwjNjrRynWt0xCadBwRglAIIV1mC9QMCWCTq4TqEf9VxlJwoFHKHcjNZHK1nNRdrftQsT_wXy_IF6Lxr7Qpx3Sd9PMEjKErOc1IWWpmrLLIKvFxBE9L4sMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید اتوی بخار چطور کار می‌کند، این ویدیو را ببینید
#موشکافی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/685270" target="_blank">📅 15:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOggXnkQ8oHmsO-mGFwgFfbD7w_8ROGTyYlk910QhPVDXoKhmxGMQxgcf1p3Ey6jNMAHfS-xJlpIEgN0z53cryIeFLEROl1kDQzsZJM-MqFyRa8JJAAuBisGx0rWHNNbNSss3kXDkbRhC_jkCFURBhnY_PilhKCHDY1ud774R20bP1WltMRL9dwSVa2wwPIG_R7dLglMz-kymv1gLCJ2PUtgMlHsSMQCnfza5of49hy_klOGeuMFDCqcqPQ_4ywzdTzBdpIvLLTCg4CIozGkg8TkHqX4UWW4dFqNP4nBKIEglgxITXsrpA-eYX_xp67Dbi59GLpt3D5Qk5y1H_OxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ جنایتکار با شخصیت فیلم ضدایرانی ۳۰۰
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/685269" target="_blank">📅 15:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685265">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ff27ae35.mp4?token=tSLxUWw0xXzlZILyrVs8StUNyiyL3Xr1y0cuxfj3xJ2JCDrvugjybFHUc6B8MywCj9B39YYU4Stp5owEb9BVXXACmBZbmKraR8O0w96RIK71hiN2Jp94bT6ve5HuJVfcvfb8KYVLVs3oRCS-VwvJbU285v_edCjyusQJaTFf56fx6dqh4JTi7hw_A29a8qzZ8MA3QC2MHBBxb34SIMs_uz__26ZMV15Kb9Zd64WWMfKYBQo3NY6zkEhC5NcUDBx9REqTuy22ZVGMMmnqNx1RWw60thXVoR9b-1kwEs3MhW6fUiODq8rdzuREVAowO0FW8UQPn0-NXvV-R8g48wV9Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ff27ae35.mp4?token=tSLxUWw0xXzlZILyrVs8StUNyiyL3Xr1y0cuxfj3xJ2JCDrvugjybFHUc6B8MywCj9B39YYU4Stp5owEb9BVXXACmBZbmKraR8O0w96RIK71hiN2Jp94bT6ve5HuJVfcvfb8KYVLVs3oRCS-VwvJbU285v_edCjyusQJaTFf56fx6dqh4JTi7hw_A29a8qzZ8MA3QC2MHBBxb34SIMs_uz__26ZMV15Kb9Zd64WWMfKYBQo3NY6zkEhC5NcUDBx9REqTuy22ZVGMMmnqNx1RWw60thXVoR9b-1kwEs3MhW6fUiODq8rdzuREVAowO0FW8UQPn0-NXvV-R8g48wV9Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌پرده تهدیدات علیه خریداران نفت ایران؛ بلوف سیاسی یا چالش جدید؟
صدیقی؛ کارشناس مسائل آمریکای شمالی:
🔹
تهدیدات اخیر خزانه‌داری آمریکا برای حذف «کشور به کشور» نهادهای همکار با ایران از سیستم دلاری، فعلاً در حد بیانیه‌های کلی و اقدامات نامشخص باقی مانده است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/685265" target="_blank">📅 15:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbdMTebjtUc_kqB48W3V0kAb7ohpBp_NJpbEP9D8j76L4guChYjF5qF-mHPkRpSeZwQybU6DGmUbJdQO76IIQ_-vptlt9XoQrjpGMgqORrw-fdmYVnDEj5RYUegNR0Bg_nO7N1cc5F0z30zTBCumDObSX_CwZj3v4w6Nsw6JjMwxt0cLWzj1HWR_KRMqoiBB6lPgE0sC6HipWa_bJ6CfFFVaayzjXJEmjdpjZhYEIfhVdm018t0etqt46ixX1jj_Joqap9tcGi7rtsOKfBsXHs9qW1ofDUpSwZCEJTNwU1pvUMZtzfwjJu3YQT2Rwt3zYE4jWDuBlCyQ6V1iCRjAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تذکر دکتر یامین پور به وزیر ارشاد؛ مخاطب دو قطبی نکردن دولت و دولتیان هستند.
دوقطبی سازی ممنوع
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/685264" target="_blank">📅 15:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685263">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcaIdypi2H5_o_UzGN9p0yzk0hbCtzi_2Mj4I9fOQDglLnpmnhvkFvIz-Dapcxw5UWti1ull2NSQg6xyNtJOpKkF3CLzY44hL21lOlVK890FcaUnQo3eNi4aTtbPLvabM8w7jrfX4D5Bu07FD9uow_f1KjhLIq3kCASctpgm5SovT9DgvLiQ5NFCD6TiS5Ejk-pqpf9b09WE9sry6MiylIG48dVOMT_xnSYpitvGk_wsK_eRIW794_9IC8uu5z-oqK5R1vGaN9XEIego43jqimYFo5amA3ltC7nh-BVTFgcp9ojehFczEuA4_AqGxAXNHxrR8YpZjcoPsuvid0MESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: بازیگران همسو با اسرائیل به دنبال ادامه جنگ هستند| مصرف‌کنندگان آمریکایی هزینه واقعی جنگ را می‌پردازند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/685263" target="_blank">📅 15:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685262">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXWpA6f1q30HqoylhyZ9zvFhBZtKsQ4tijeUJ8_Ut0oeyspS2QoOSvNR0U6b_RYr6G7ybzrMMP5Iv6wkc1Rchtgq0aPL3TJqSXyVUHa_ElWJV34YCeRiomT8MyNT_x4eTplI6D2ayy_CCLW-Bv8SOzlXFNkn4wtjSbg-u-VbZN50RkMhEMDv8pIMkiDf-hENZ-T9WQbKGjLMs6dgRroBa5xMru2z-3P5QdoBzpmbdLzw_-Hj6oHupPM9ywV6rxzzb-gXizNox8oi8Hz-8c6IRIC3VFjLpR4Wnr1IwSjiM49QAmwZ_39CYcGCKzEwdqHwxQ4-71qhGO8nz2hKNebMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوسف پزشکیان: ما باید هر کاری که برای تامین منافع‌مون لازمه انجام بدیم اگر منافع ما در غنی‌سازی است، دنبال کنیم. اگر نیست متوقف کنیم
🔹
اگر منافع ما در داشتن توان موشکی و پهپادی است دنبال کنیم اگر نیست دست برداریم.
🔹
حیات و ممات ما به غنی‌سازی وابسته نیست اما به توان نظامی ما وابسته است. این دو قابل قیاس نیستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/685262" target="_blank">📅 15:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685260">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cac48f96e.mp4?token=CNiMjip-7EpFTPQz6VUDmeFrmBd4zi5rGHDqjSyAmFNTpvHBLniEGdnRwZ2DufsHGGZ-oqXIGcySiJ1U3r9GfRkEAK1t6vsTXjGvJ3uv_j1GF1b4Wo0aUq2YEOGor3uQqgaw80QRGYFLaED3Cbc9d4Wj8mUaOAdfWgzFywcfdK6HEe08ykOkYFSE67NEYxDRZKrQqUxWT2GHx3kZ8gSfwucyYCKuIlWb4d3ljC5rVQ-CaUYLTm6A0p10zqDki8E-Idoqt4prT16ZpMl8fBgKwMhh6vI6WYaEfft33o97bitGnxeW6Ck9jm73aNLBcVVEO3JgsdWLH7BWRjNmQuzMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cac48f96e.mp4?token=CNiMjip-7EpFTPQz6VUDmeFrmBd4zi5rGHDqjSyAmFNTpvHBLniEGdnRwZ2DufsHGGZ-oqXIGcySiJ1U3r9GfRkEAK1t6vsTXjGvJ3uv_j1GF1b4Wo0aUq2YEOGor3uQqgaw80QRGYFLaED3Cbc9d4Wj8mUaOAdfWgzFywcfdK6HEe08ykOkYFSE67NEYxDRZKrQqUxWT2GHx3kZ8gSfwucyYCKuIlWb4d3ljC5rVQ-CaUYLTm6A0p10zqDki8E-Idoqt4prT16ZpMl8fBgKwMhh6vI6WYaEfft33o97bitGnxeW6Ck9jm73aNLBcVVEO3JgsdWLH7BWRjNmQuzMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معماری ایرانی یکی از بهترین نمونه‌های معماری در جهان که از دل اقلیم، جغرافیا و نیازهای محیطی شکل گرفته  #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/685260" target="_blank">📅 15:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685259">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206964d4e3.mp4?token=fymEnnyve-wEC2aAY5gaFTGUuZb10DCrmSq4Zdk3YTTrb64-hvhtcYEeYgSU0Gy9Pj9xWM2mvaAj6As0Q8QndJmVnNXW2XjHw8hCUKjTeOmkE-QRZzo_8qsAlNvopXtzT_N5a75OTH4jfOSqt1cdnRU39FuthqUhDDZrF2fw-j5VXlzeYRjpc6i5aLBIqqAb_whJ6s8WNd7auiSGsxGyoNU1jsaUh7JNLeT3an_G3n2iX4P6wqtgcmlpZBTAjpbo-7uoGjvbx210Y9KCmX28l78ykp-tEws3ol7fhw1VD0sdjq4lyj7fdXnAMJgAcIfHv7gXL4zPWdbJ9TTcYbCFBw5Jw2YkbAUimJsxM0NNLNnal9Yr-59My-qrdrfF5fHZ9VkYy2R9mDWsfy8z_pFCurbCKBaf4NaCXfe3eUN6GQElScvBMYM1ZZk1lfHT7GcO4GNSOl1-uVy98nFenW1scJxkbizS-qnzROBXFuDxyhA8QRk-9fHZ-tQbMrBjaDGjEOEkB6W1SgZskBPZVzZY2RNTD9ccEx6x1ESrQhW5t4rEMEb37TnFbiEMkgsEfW_u5Btt6Ya7mMCWzX8O9nYzDmuNjww1EDC9cL3pC-FyClcV8O5hNECg46ipEKq2Krcmv6r_QqAqwitLkRlvG1jzzkHHcbvb1y5An9OPq51Hxy4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206964d4e3.mp4?token=fymEnnyve-wEC2aAY5gaFTGUuZb10DCrmSq4Zdk3YTTrb64-hvhtcYEeYgSU0Gy9Pj9xWM2mvaAj6As0Q8QndJmVnNXW2XjHw8hCUKjTeOmkE-QRZzo_8qsAlNvopXtzT_N5a75OTH4jfOSqt1cdnRU39FuthqUhDDZrF2fw-j5VXlzeYRjpc6i5aLBIqqAb_whJ6s8WNd7auiSGsxGyoNU1jsaUh7JNLeT3an_G3n2iX4P6wqtgcmlpZBTAjpbo-7uoGjvbx210Y9KCmX28l78ykp-tEws3ol7fhw1VD0sdjq4lyj7fdXnAMJgAcIfHv7gXL4zPWdbJ9TTcYbCFBw5Jw2YkbAUimJsxM0NNLNnal9Yr-59My-qrdrfF5fHZ9VkYy2R9mDWsfy8z_pFCurbCKBaf4NaCXfe3eUN6GQElScvBMYM1ZZk1lfHT7GcO4GNSOl1-uVy98nFenW1scJxkbizS-qnzROBXFuDxyhA8QRk-9fHZ-tQbMrBjaDGjEOEkB6W1SgZskBPZVzZY2RNTD9ccEx6x1ESrQhW5t4rEMEb37TnFbiEMkgsEfW_u5Btt6Ya7mMCWzX8O9nYzDmuNjww1EDC9cL3pC-FyClcV8O5hNECg46ipEKq2Krcmv6r_QqAqwitLkRlvG1jzzkHHcbvb1y5An9OPq51Hxy4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از درگیری محیط‌بانان با شکارچیان مسلح در تنگ‌صیاد چهارمحال‌وبختیاری
#اخبار_چهارمحال_و_بختیاری
در فضای مجازی
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/685259" target="_blank">📅 14:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685254">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAQ1NXjrbcKEF-mIlVN5p_LMfYDRCgjHamlzZRmauJTaSNhO0wP2fQ0oXOrSYyB7UiHLUzUIs-VGz0mTtt5GPlOlEOglSujZnsNgjVsdwYWK78dVmckuTLC09WDmDTuLKE3IYaZcJjTuMlvWhg9jb1YzIyqzvZCF1t93dxLT7PbHCydSHhgZruWkKLtJFmHqA31kQ7j4ZBFSbG8qik0SBzbc5nHJecFYggp_qyjfVJT4SqIb-6mzzEWS2Z3jf_nK3WFDjgXDvY4n4OJ9ikMtN5MrmoBEfzrdQ761IHe4o4n39-GdEi9_bbXWDOIgQ4RJcaSjmkePAVWjhFF8ybVimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-vJev6NtZ2PLcDG1T29Xfv7nGbr8ZvfZTSl345IZ752KUl1NfwFmUTNDMhFrlHtpAbgOH0QWxdvfMiEuYzlVTmym0Fy6niVGQQSym0Fr1xGDPORRnz8WyAbR9zDf_2SUJUR_u80_SBTPKSn2dFAmwaALDpHTALEp7bNI9ejZbpH9d_vjBsUqXQA3EUv7c4OsZeWN3rdRObkEIyxOCdtjs3ziIQS_cLlcgzoJ55rUrIRRS-ohz-PG7qdaj5EkHUtfbLViBo9ZYEjoDZBHG08psrTEJ4ZmY1tVui9rPvFbAyxq03_Xgdy2V1MeC83WZUNQxvb_Pm3WzqpsKc4YDzpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7wFsO8VkRoaqrZ8qLycMd6ixx_H4B9BU9OZSRhHUYW5IHmhiQQ2JELd1iPD_zt_UtNbf_P9-9vlA78HkmNzhkeOwjS_g176dpYXHn9XObobVL_kfeHjx_AZT8SMmPLT7GOTYTd34_MFzz1_BydOL-If9RmSNd3V-oyhTPih0mgQgQb27SKy6ZCRBxd2EQF_u0hFrqKv07S5dMm1y8RvS1di0hMaZtv0ZVJ3C0D-MlMbwDOe0BzyASuwnUa5ZqGsCxOmIaOArigkl7FloQOAihpDfZEaLQlT4BYXUjBpoj4MuV_q-HEkogDf8qIQ1q11TxoVWhhIRWgyuWkuSwlUrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیست عجیب فرمول یک عربستان؛ پیچ ۷۰ متری در ارتفاع ۲۰ طبقه!
🔹
پیست فوق‌مدرن «اسپید پارک» در شهر القدیه عربستان، بخشی منحصربه‌فرد به نام «بلید» دارد؛ یک پیچ مرتفع که در ارتفاع حدود ۷۰ متری از زمین ساخته می‌شود و نخستین نمونه در جهان معرفی شده است.
🔹
این پیست ۲۱ پیچ، اختلاف ارتفاع بیش از ۱۰۸ متر، سرعتی بالای ۳۲۵ کیلومتر بر ساعت و ۸۰ گاراژ خواهد داشت و با مجموعه‌های تفریحی القدیه ترکیب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/685254" target="_blank">📅 14:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685253">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da07fe860.mp4?token=YHudjgE6c6KyX7uyJBsdqcu9_nHaKX-FeAJ12xLS7-TrBa1Uq1cC-TmIKkxitdsy5d5CspA8FPyYlINNFnBAi2cHEzpliXEY6_cRN9_S_ap1gkq31m0egm0RCfSdoqt3K9N0iDE_ID9O1GL8DMqQsbemoQhcmYo4Jnkh9MK68eS51t-fquI2Bg5is4XpljjVqkD9LGlECcXnBJQpunzTTPiGhw-mO6M2reJtA-nLGCePqZtJTFaqUR1F6nZ1YnJ_R6N7UZMtiVvnuCnNGzR49daAh3fCGnYCSfmZKgdwK0APcxUikRHYzd3J4GKdSRjFN1BBjlpDM3vuqtzQKRS0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da07fe860.mp4?token=YHudjgE6c6KyX7uyJBsdqcu9_nHaKX-FeAJ12xLS7-TrBa1Uq1cC-TmIKkxitdsy5d5CspA8FPyYlINNFnBAi2cHEzpliXEY6_cRN9_S_ap1gkq31m0egm0RCfSdoqt3K9N0iDE_ID9O1GL8DMqQsbemoQhcmYo4Jnkh9MK68eS51t-fquI2Bg5is4XpljjVqkD9LGlECcXnBJQpunzTTPiGhw-mO6M2reJtA-nLGCePqZtJTFaqUR1F6nZ1YnJ_R6N7UZMtiVvnuCnNGzR49daAh3fCGnYCSfmZKgdwK0APcxUikRHYzd3J4GKdSRjFN1BBjlpDM3vuqtzQKRS0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
مسیر ساختن یک کسب‌وکار از دل خانه؛ داستان‌های واقعی از کسانی که با اراده، ایده‌هایشان را به واقعیت تبدیل کردند.
🔸
در یک فایل صوتی کوتاه (حداکثر ۳۰ ثانیه) نام، شهر سکونت، چگونگی آغاز مسیر و دستاوردهای فعلی‌تان را بیان کرده و به همراه تصویری از کسب‌وکارتان ارسال نمایید. روایت‌های منتخب در مجموعه رسانه‌های خبرفوری بازنشر خواهند شد
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/685253" target="_blank">📅 14:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685251">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45f93b367.mp4?token=CFFiLkFqmVnRBR-UAQVQThcwgVtn-cGdI6V9kZA-ud0hmho_kLOk-a2UnSa_NrZ-XZfQlmsc4MudvfvUguyKR8WqvTmt-icbgrpG8OQO4LlrF0xIz6jOi3J5EY3e0cJ41NgEQQZvObMBxLmldXV9NHWXfywe39DqCQfeKFsozWMgyNhl5_VursXzo2WflMjyk5X_EAfO7LU2k5Z-5IXqyECRTIFlFkpeH_WCjL4dJDp3imuqzarrEl76ASziQBFQ07_tJjff-ez-cxJkIoCTsbjqG3JFvYdnoif9fKuX5oKKh1CqXQGzSKss75mhibS8yVtV1lnHY2ah8IPjl__5rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45f93b367.mp4?token=CFFiLkFqmVnRBR-UAQVQThcwgVtn-cGdI6V9kZA-ud0hmho_kLOk-a2UnSa_NrZ-XZfQlmsc4MudvfvUguyKR8WqvTmt-icbgrpG8OQO4LlrF0xIz6jOi3J5EY3e0cJ41NgEQQZvObMBxLmldXV9NHWXfywe39DqCQfeKFsozWMgyNhl5_VursXzo2WflMjyk5X_EAfO7LU2k5Z-5IXqyECRTIFlFkpeH_WCjL4dJDp3imuqzarrEl76ASziQBFQ07_tJjff-ez-cxJkIoCTsbjqG3JFvYdnoif9fKuX5oKKh1CqXQGzSKss75mhibS8yVtV1lnHY2ah8IPjl__5rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میز نسل بعدی: ژست‌های ساده، هولوگرام‌های تعاملی!
🔹
با یک میز هوشمند جدید، دیگر نیازی به ماوس و کیبورد نیست. فقط با حرکات ساده دست می‌توانید نمایشگرهای هولوگرافیک سه‌بعدی را در هوا کنترل، جابه‌جا و دستکاری کنید.تکنولوژی فضایی (Spatial Computing) که آینده میز کار، طراحی، آموزش و حتی بازی را متحول می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/685251" target="_blank">📅 14:17 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

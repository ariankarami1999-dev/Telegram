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
<img src="https://cdn4.telesco.pe/file/Gf-rcMXVJCuJnToOVVPNLAmNjJSvA1hmiwYb9mSv0eVxf7Qr0_jNEphKMHC5HJNQzFwzapeYW4y9zuHV9fq6uG68iNHQpvLk5WI61fO7RSFcKVWjEbGdsbVt1AMnlrD4gD9GGYxCMpRLaUor2MoGvEGQt8aspUL7wuV854xx1blxUl0rhPz29zpcUWo624d3vHdIcCOvvWnbAUrvjejJJEONMyjRIDqDmlwaWwuSJz-vUHgkFpsqFPTKJnswimYrrrAIZTI9XtWnN_DBtxi8GYTma8q-E0C8mhSrwadkIBwQXJbO0OloL0qG8VLtI02WJOpYEWmIP8OWQl8D_ndj3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 207K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 15:28:59</div>
<hr>

<div class="tg-post" id="msg-81183">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزارت خارجه آلمان از شهروندان خود خواست فوراً ایران را ترک کنند.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/81183" target="_blank">📅 14:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81182">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزارت خارجه آلمان از شهروندان خود خواست فوراً ایران را ترک کنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/funhiphop/81182" target="_blank">📅 14:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81181">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9BJQ2SyySbWmD5ZlrkBITx5rGklKsWdjghVqJNXaVDrY2S8TpDwg1px1_5hhbQlpOHyNFjqzbzYyvJ5oHQIM1GRugljsd1fIf2tFBG_TndE95m3XMq2uCYIACNUEjMGGBdUCCjrvSSBjT65ntDtvfpKJ7SJNgrs0oHteolO5jFMdN6VvjusH_WB3OmBEjuFfBFrdUdQO9KqcBB6SaVuFRt_gwDpQI0Hu1q3gFRvX86wgvmOXoei8W8YgzPFaSbE2H99hrkLTavwQn3gPr3nMKVpHbU9zxwXLrD1HpEG8qSzBTT8jnM9quglU1MGF2f1P3Z4KjB-rFR-2XUulI4PcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوند زمین و آسمان را شکر که زبان فارسی را به من آموخت و اجازه داد آنقدر عمر کنم تا بتوانم این محتوا را با چشمان خودم لمس کنم.
🙏
🙏
🙏
(
معرفی بازی رومیزی نجات کودکان از جزیره‌ی اپستین و رساندنشان به بیمارستان خاتم الانبیا سپاه با طرح جلد کیف صورتی معروف دانش‌آموزان…</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/funhiphop/81181" target="_blank">📅 14:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81180">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bcddf257b.mp4?token=t22gOw2XdMk6dgzfPqlZH58p6zFshySG1n_EBqnrJ2JhYaHT28j31a3Snpd0nb9Gl97GF-zWhPtNMTFUnsKzhCwok3hhuyzqXtjGixSlZFo7c0SH9Li5bRSX4-zuxcCKA587S6YAS2Xvh5CKQsHDaqqw9ELtK0ExZTDrjvg60GR7xOYGV_MTudcHuBxgjgnsd6zY34GMusaRotq3hvBzLXHOA2tPkkOJwQ0uEwoGM42yKC0b-tMC2L74IpBb97F4-DSVx70qcT6P0satFdbbUtwjRftTaNjMsZouszZDYvP9HMHlpvZ33OSUPk1sirakfjuRW6W6VGehbOTJALK0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bcddf257b.mp4?token=t22gOw2XdMk6dgzfPqlZH58p6zFshySG1n_EBqnrJ2JhYaHT28j31a3Snpd0nb9Gl97GF-zWhPtNMTFUnsKzhCwok3hhuyzqXtjGixSlZFo7c0SH9Li5bRSX4-zuxcCKA587S6YAS2Xvh5CKQsHDaqqw9ELtK0ExZTDrjvg60GR7xOYGV_MTudcHuBxgjgnsd6zY34GMusaRotq3hvBzLXHOA2tPkkOJwQ0uEwoGM42yKC0b-tMC2L74IpBb97F4-DSVx70qcT6P0satFdbbUtwjRftTaNjMsZouszZDYvP9HMHlpvZ33OSUPk1sirakfjuRW6W6VGehbOTJALK0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوند زمین و آسمان را شکر که زبان فارسی را به من آموخت و اجازه داد آنقدر عمر کنم تا بتوانم این محتوا را با چشمان خودم لمس کنم.
🙏
🙏
🙏
(
معرفی بازی رومیزی نجات کودکان از جزیره‌ی اپستین و رساندنشان به بیمارستان خاتم الانبیا سپاه با طرح جلد کیف صورتی معروف دانش‌آموزان میناب در صدا و سیما.
)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/funhiphop/81180" target="_blank">📅 13:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81179">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک مقام ارشد در کاخ سفید گفت که ایالات متحده یک برنامه دقیق برای سرنگونی رژیم ایران دارد.
«اطلاعاتی به دست من رسیده که بسیاری از افراد از آن بی‌خبرند، و من می‌توانم با اطمینان بگویم که ایالات متحده برنامه‌ای برای شکست دادن رژیم در ایران دارد. کارشناسان بسیار متعجب خواهند شد و سپس خواهند گفت که همیشه این را می‌دانستند. به سادگی، به آنچه اتفاق می‌افتد، توجه کنید.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/81179" target="_blank">📅 12:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81178">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tomPRArODosDOxiqifRkFLTdwucoFBOFLNDJscNOwoHdC8P9SAw4MV_aZnsxCD5jcNlewXpUEUPPyjYzYxiw3IAfXKlPd5HIzWk3oRyXHI1K1PlYxQCwwGyXCzQFeqS1xIc8MZb1XAStdHnAhPA9u4mdziOzUKEBYvQ3DVbG5tsaC47-JslEGB0UtB0-NoJ0gpqxU2iHAiUj9pNIEZPharrkiuIpoyvGKqWyFlk_t-aV5iIglY5CSW1RCRR9xaTtKHiJydd8AeieMJKjInq_38xuuOKncC7azLn-ARCSaK961HxcY3Dm4eMxRmjZejmuWxfDnTpJQD8R8BVgI1qLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه اهل وسط زاگرس نمیشیم یه نفس بکشیم با اجازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81178" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81177">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6aEtH8JPtsn_SBVZ3mUxYIErEiySaa7YtTjFSIW4J2EjtfvkAh_A47aOVYGYXbW2-oTyXhu8RK_z2SV43TLaJVfEypAik3d19olkNJ9heLXaYMQXZNiMOLGWZ1Usv0RA5UYNXSitVDm54h6O9QzMfgglP4QaTz0ftrJDLbC6eAqcWEQMtU-L6Pyd42E_zuRGUWfK6dOFi4Daz6e-o5pi6Z3uvoEZyeVVL3U5FIdSa3jNqWP1SAvrpYDuN24ebNr32xAXba94CxFTc3zzb-CKs9hWYK51sSdM9lXhs2H1vx4GEfkliMZOrsnnVKqcw7IEcWDSS9c9pWswJjiNVWG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
روزنبورگ
🇳🇴
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۱۹:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
منچستر یونایتد در ۳ بازی اخیر خود مساوی نکرده است.
✅
روزنبورگ ۳ بازی اخیر خود را برده است.
📈
میانگین گل در ۱۰ دیدار اخیر منچستر یونایتد ۲.۸ گل در هر بازی بوده است.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r2
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/funhiphop/81177" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81176">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L01mCkXKIyYObbyiILUnGs4VXuB_1FfMSgPt_CLhdYZ4vHWYZSgy1j9MPVsl7snTIgMCFUfAS0sNQqsI6z1FGsntijG_aKd2hv-I2tMwUWgFm3UIFUa5Vyw7s72VsgD_RiU6jg4CS0DRloY9QU0p87kZiGHwcG4lWG0bByIND7PDr9ou4lrVGN1R6cxZCiln-s1L31wklpBhMq8rQIGOippUgFvy3Zmlb40v1FrzG0-Xq4ox2j-6_vd4dlvnlh-gd-ttGFQwrEmy63qeSO5jKKgE-auAHRvya7NAA2C7KJTNGVRI03CLm-42TPINvBVNmeXmuR5OBsnTetZiS2SwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه
این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/81176" target="_blank">📅 10:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81175">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حملات امشب آمریکا هم تموم شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81175" target="_blank">📅 05:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81173">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فیروز آباد فارس صدای انفجار شنیده شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81173" target="_blank">📅 04:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81170">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وای
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81170" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81169">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بندرعباسم زدن</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81169" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81168">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اهواز جر خورد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81168" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81167">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باورم نمیشه ایرانیا دارن از فلایت رادار مسیر حرکت B1 آنالیز میکنن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81167" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81166">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اهوازو زدن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81166" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81165">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اهوازو زدن</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81165" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81164">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a5b222b2.mp4?token=vtwJENieN6GHz6jkUs2-43AzqyVro1r0FJp7MclhEItUCcXQKmbIh9cI9hJ8IoV87wSX7vno8XAnaYk0lmavUBkHdVtLAjcFr-gK5q2qP7EFar4qYZKFWu3T2TcrdwGu0GCXNPgHByaan9iasnbAPJ0ILT6qfJcyNv5tm0KvRmz2iYsxS6J5DIKhUXExWzTsLW7yctYd_W4wKpB365VCwvAqsj58yTsOvIxLuRrTG5m3P-xL-pOGru5LwyvHyJc5uJfwHloo2Dr9JBGPNm9qlfe4a5uzah2q9necFC3UNq0h1dWyWh387zKf7TgYbSWNph4nxuCxqc3WBNKDPiUlyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a5b222b2.mp4?token=vtwJENieN6GHz6jkUs2-43AzqyVro1r0FJp7MclhEItUCcXQKmbIh9cI9hJ8IoV87wSX7vno8XAnaYk0lmavUBkHdVtLAjcFr-gK5q2qP7EFar4qYZKFWu3T2TcrdwGu0GCXNPgHByaan9iasnbAPJ0ILT6qfJcyNv5tm0KvRmz2iYsxS6J5DIKhUXExWzTsLW7yctYd_W4wKpB365VCwvAqsj58yTsOvIxLuRrTG5m3P-xL-pOGru5LwyvHyJc5uJfwHloo2Dr9JBGPNm9qlfe4a5uzah2q9necFC3UNq0h1dWyWh387zKf7TgYbSWNph4nxuCxqc3WBNKDPiUlyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس: یک پرندۀ ناشناس پس از اصابت در آسمان جزیرۀ قشم، در حال سقوط است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81164" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81163">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بمولا این یکی یعنی تعویق.
ترامپ به آکسیوس: جنگ جدید با ایران می‌تواند از عملیات خشم حماسی که 40 روز طول کشید نیز بزرگ تر باشد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81163" target="_blank">📅 02:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81162">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ گفته ایران از این به بعد هر کشتی که تو تنگه هرمز بترکونه، خسارتشو از پولای بلوکه شده اش ورمیداریم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81162" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81161">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">باورم نمیشه ایرانیا دارن از فلایت رادار مسیر حرکت B1 آنالیز میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81161" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81159">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انگار قسمت نی اونموقع بمیریم، قبل اون میخوان بکشنمون.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81159" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81158">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw4u_xOf6ct9zzBuXIGabC6bv4erVGDQl4a0n9AyEWSuKXdJyWKV9feqUNp77KDQD82wOIqs-3XKR-VxfFBmslVjDlovIENF8pif7yeEDJ3nht07FiYHiKpqX32NKr0uHLIP_mIsjZ78sGUUGwT2ABLz5U7b00KzAFCKu0FdyN6jzd2b2uDLv6OUI8-mCi6dkKQRBVd00id388yRl5vhzWYxipSXYpI__n1qWJoEfIe6Jjq9vu3-Rx5zcAIRq41AdJI1BHLSj2ly7NSfe1GhMUwNo55xWerCkGQnXe3R5kVjV2FUZo79jOuA91PLO3geloWgQFF0YVJSvtXbyNZ4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81158" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81157">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81157" target="_blank">📅 00:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81156">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4V8NFFNLzzsjTvCSNfcL59ymU23OXrCexeLMB6q1lCHo6YloRz8BgTGYjwFL11yCVDdfAfMU_BZZiDVzOu1cmTh7VXJ63PkdeU34XO_iGwxfF_zYBxbN8JLt0Ci7vNZtwUKNw39tMefn-F2cvXU7baYAlK9hP2R6fJWyRZdilGp9YkTACXhYJp_2YGHRQVcJfaqAhLvgge_v6s0T3XHWIG6f2aoS5xabT6cp6qyC2iLA752l3GTCypSWig3XxiwPpoHA_J9mDu_RJ4diInP_DSnGRLHjbHa2aGFdHWLwO-3Khk83pOSjluIAF74LPuUq_UgnLHZ-LYdwJo2-xsH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر متکی نماینده مجلس: احضاریه پرونده قصاص ترامپ به کاخ سفید ارسال شده است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81156" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81155">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دخترا جنگ نزدیکه، لطفا مراقب خودتون باشید قربونتون برم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81155" target="_blank">📅 23:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81154">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سپاه چند دقیقه پیش حمله کرد به کویت و مدعیه تونسته یکی از رادار های تاد رو بزنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81154" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81153">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">امروز تولد 33 سالگی نوید افکاری بود، تولدش تو آسمونا مبارک، روحش شاد و یادش جاویدان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81153" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81152">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کان: از لحظاتی پیش تمام بیمارستان ها در اسرائیل دستورالعمل‌هایی را دریافت کرده‌اند تا برای فعالیت در مناطق زیرزمینی و محافظت‌شده آماده شوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81152" target="_blank">📅 22:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81151">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: ایران میخواهد از طریق مسیر دیپلماتیک به کار ادامه دهد اما به نظرم هنوز آماده نیستند و باید بیشتر تحت فشار قرار بگیرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81151" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81150">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یارو اومد گفت هر کشتی بزنید یه زیرساخت جنوب میزنم گوش نکردید نتیجه اش رو دارید میبینید، الانم گفته هر کشتی یه زیرساخت تهران بازم دارید کار خودتونو میکنید، وطن پرستای زیرساختی نظری ندارن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81150" target="_blank">📅 21:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81149">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81149" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81148">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی به کشتی های توی هرمز موشک شلیک کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81148" target="_blank">📅 21:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81147">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سپاه چن ساعت پیش یه نیروگاه برق تو کویت زده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81147" target="_blank">📅 20:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5dmSyYXFetQJux9MmsOCVdl04Znmj1vXgCwtdF-e-At-rn3aocGxKJjcsquus_HXl-TgO5Q9VrZ2xTsD65dYGl1bJ5M-NR1OjwdehqDygPOT4Z9peBMJiqZTJ6tMkcwYQNezR-0oEgBMWdAyyYo9B1nemMIBdTB9Yqpeucy9tqnHZHOzu0FxTGVw3yAhekOQlp4SqAPzvea6_8vx5-xiMarMigxKly38hAMSl9bnSkxgMHG4N-a8ErtLHrzt238mWIQSt6-uZ9TAyfy8ER50Rsiip93n_p51KBzjvR1-9GgVkFg_Vx39gAhrhqWEDq3_GrTNYGpcz19OyIRWzEKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال جقی قبل از معروف شدن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81146" target="_blank">📅 20:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81144">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRKOt_SkqoIpBzoWBKHgGQJMtvTML_DTqWWx6mrcxCxTgHMkYGtsxNq5o9Dg_wHgHYU7pJDB-mqbSe-B_8BQoCuzZOmote3rT4GfcKJrdvDryG-lZiImNYSIqk65gB50_rHA237AKytG83XV3qddZ4bieTPaZSAhnOtxqo67SrjzQRBRkN3--UJAjfa1f-TXRZnNednmzXmFQkqH3uVhy1DBRFi2qzf5IKLM8r3Y_--Y1sRdixZyz6DQLFWsI_w-aqGi4k8Rv2vx1px54sa1WNBODPBspCR07HkVIsm3EJIb2FTeNYg2qpRzenre1KgLxj-TkDFT4w9XeVQhxvJkdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jo1mj88rusKepi3pIMf4nmRpaIGJybPKj7JijcMlnasIw4cuzx7M_x8kx9WypadBRhO3nJUVnGr3k1cXaRkHI6dCprhnuwX5H_rQf2d1JuZc-Gi9UTRxN2TF-cCmCOEfc19tg20vmlFWiin9Ge2ek5rFZ6ap6lxFwjEM_5FSCn1GW94p6h_Olg6tqLy7Bh43muIP96BzlAaWesN71Ckf-6ntM08GZ9-YdZGByBbdlEdhZA2_v4FqDko6guwLyX8pOkEbwSrRi3QrW95NudKgC3-wpyvHpsIDItzDK39wDu-vnakuJTdI7RgLMVW2urFbN8cVZaWRO7I1pjF8OZPb1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جدید جورجینا :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81144" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81143">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG8I9TU-FjfHcQK8Pn0iLnj-9_bDucbsypFC-6vKb9CwVmtd1m1ZjEYEdFAu6ThlTwaIWHFgz2rT52dK8I0veIm4JiBZYixTv89XaMJ2qphOsAzSqTD-hyMJqisDdYfb9IXvtFl0kqPmiqeZYAN_9uyYECyA5890bk-dTldAoGWOL9-KG5xMcwDr2jLXmd479Uv7d55BAEcjiNivb8VLnDfC4xY9wOffjq5ogB3Tt_smzzSXW1QbyN1WsT7Z6csUhPjUNV7JjvCd29pn_7k_Ddm6BlQfJPuodRo1gkcRNPVC6InJDhUiNr6_jUrI2DILF2J-T8HusXMnsMVmba45Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ایسین به اسم دارک منتشر شد.
📷
YouTube
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81143" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81142">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وضعیت خزانه کشور.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81142" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81141">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDKgwXEqhN8u06-B_VfdvqoD0oeI5lWy2L2VDkf8K9qeXSgXDqIO3IA9cbAt6DQLs90O9ZbtCxqQSosoT3ZFEN8S6jyZ9esKkeSaqmLAI8c54YbS4_usg6sAq6sBFS7HZV5pNpFafrQlGfaZlyXE1y1-3Stjg7VT7C8_9O7ZCfGgE8-Hn5qoXWsuJGPUH7o3ZI5BISDELRXdw3DDbJaWer5U-DSv8RPQk4aoqE6dpMkVZeYIXVYuD8Y9Ut1ZN188HBNcwVsH8_xgwNG0VvIIhUAYjgx12QuUGf1lsRxuHwmY4yZPq9mO18ifQqe4gC3TKlY5aBYZLn2AUgK24vj9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خزانه کشور.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81141" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81140">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDoVidxHHiyJaS5pumG_FS8IEPNssEh0Dcljcz5bSCMZ1vmcR6nOM3g8ZCkVJMoFVL7Z1CegQ_1TMnqoZPMvn143tXZFQEkjlh7eW2JbsTXvG2L0B1qK0cEUQ2PmttrUB8rVtubhVWvSB3emAdYLkpkXvE8VXmmv9RainnNRM-VG2mOt0Xk4jOJ_ctxAAPlKiaRz6NK0lIUPMGB7PztWgEdZ5ATL53mqjfP18pVgd04KDfXJBQXhZY3vx-_W9lgxXGvrfoVsHyPFSa27MrZxukshJ5N1MeR6Sknh0JnMzCQPrlZjgdOBjFQHbqVUl9HNqJFRU36jc1Wjggb5ccMHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید کنار بیناموسا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81140" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81139">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6LN_fnIIpKJ93Du9B4IaATmOGnAjhvgYdXQYTGq4tDwmUmVCcWfkc_FDY5yDBym6eAxswSh6nXZj2AvE76iltvMPhmL_s14jRJPM_SiOklWDuPxpW8JviXplH9L_81JD20xkyUyhv2ah0g5C0yJSGMeA1D6sOtmc8bbBSZnFhA5hrDs8xRM8YUzCa49yarvJZHsTcVfAsUIQDk_4cdJ9FFbXdgeoiVFsW1tk0DhnzeqDNTN_pXQMtDq_chNd64TIX6e39dPCic7kDvsB3aKgAlb9psgLVSQzZZf0wIZMhdFfcQX7YuZQqpWkpNNw7E_W25GqH4TOhLHPIl0uuSZEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز به همراه ۳۰ درصد هدیه در بت‌فوروارد
🎲
⚽️
با استفاده از برگه‌های پیش‌بینی پیشنهادی میکس روز، میزان برد خود را افزایش دهید. با ثبت پیش‌بینی بر روی این گزینه‌های پیشنهادی علاوه بر مبلغ برد،‌ با توجه به درصد تعیین شده بر روی فرم پیشنهادی تا ۳۰ درصد مبلغ برد خود را به عنوان هدیه نقدی از بت‌فوروارد هدیه بگیرید.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/EXP
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r1
💻
@BetForward</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/81139" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81138">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آکسیوس:
ایران آخرین پیشنهاد صلح ارائه شده توسط میانجی‌ها را رد کرده است.
میانجیگران تمام تلاش خود را برای همکاری با طرفین ایرانی به کار می‌گیرند، اما ایرانی‌ها همکاری لازم را نشان نمی‌دهند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81138" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81137">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=Wlez1sW3cGfIJT3Si5HTFYmstY4uVbmDSIZWh5H-cdLK1sr7sF2C1HBe6U7NpqOvkyBzFOngH-_bc_wgMpFBqROTyyvuOMK8nkZ5z36NTE3mCE2-rgYUvPv53ig9i6G7VnjoLStCNcg8MIzOVH8zuYCy5JCttIyK8VxFZeaPXc9ENixSAvdo6ae7OCMCA6zuYUKRoCiE-OGWTSFmZjXoQKgopVD5I7KK7ObxARI-QPjTCMaC0zIpVhbOf332OD4fSk859W-gy3W6K8ZGJPA1EX3jaOOYTRiJZ0Jjk_FhysenbD-lH8OLWVx3ZkQ07dj5crwAjHGgJE6tYn3QZdcmiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=Wlez1sW3cGfIJT3Si5HTFYmstY4uVbmDSIZWh5H-cdLK1sr7sF2C1HBe6U7NpqOvkyBzFOngH-_bc_wgMpFBqROTyyvuOMK8nkZ5z36NTE3mCE2-rgYUvPv53ig9i6G7VnjoLStCNcg8MIzOVH8zuYCy5JCttIyK8VxFZeaPXc9ENixSAvdo6ae7OCMCA6zuYUKRoCiE-OGWTSFmZjXoQKgopVD5I7KK7ObxARI-QPjTCMaC0zIpVhbOf332OD4fSk859W-gy3W6K8ZGJPA1EX3jaOOYTRiJZ0Jjk_FhysenbD-lH8OLWVx3ZkQ07dj5crwAjHGgJE6tYn3QZdcmiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده کنست اسرائیل و عضو حزب حاکم لیکود جوری که انگار از دهنش در رفت گفت:
ما در حال نزدیک شدن به یک حمله علیه ایران هستیم، شاید حتی این آخر هفته.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81137" target="_blank">📅 19:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81136">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسما و شرعا توافق شد آقا
ترام به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم.
حمله‌ای بزرگ‌تر از هر چیزی که قبلاً رخ داده است.
من نزدیک به اتخاذ یک تصمیم بزرگ هستم، آنها هنوز به اندازه کافی درد نکشیده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81136" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81134">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRNrCMak24yWikmijiq3rhhSvBn7adJcrfYELVweddTI7h6-jkfIofo1IA-OYiXNWs2xGB4xKtaQdOGoYXstJqSrWMESbsVfHGFO_JbK3q6Vcp8nGrEhLH-pDL_ZzYfrXFbKbHh-9gro_b0yNpMAkm8-mdm13psNW38wd7Xxy2biSAP4xi5g8X42tBWZc_gpSuq7yUs_Ny5wZbeV13YEyy_6GcKNL0ZcMv2G86nTn7Y5YE5LFyFF6fh6w2aAS_64tRSSwlwI1EhMe0AzVZtWRZoHAYA063nbHaDOVz3reC9MKaptfLxlS_cBqtbQ1sTWUydFYfhYYPuKRxN-ABusaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا d4vd بخاطر قتل و تکه تکه کردن بدن دوست دخترش با حکم اعدام روبرو میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81134" target="_blank">📅 18:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81133">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7dbdOKgkrfeMCrJdOFLm7wgRbKudVnxS_-ysFFjKLxedH1f_cmr2cMhH3gsamOoyMVmcFmxjKPQ9QoaM_72YbZhR5qtV65UP3IfMxQaU9_KUlozhpC2pgK48gBW4GKIIAybRSiFn7JtOE1-tG3kgbC4UwtvE3RJooVZ1dMTkZq-IA0GFM9taAmfx6kKCbhUSG5-GxTWqUndbzKt6RS9631gBmzyM3BEA8L-5U517fHS_QvnCZu14aOg5Xfuo5Z7rmCV6239_DOfzR_4UCB2jNQLVwJ1tzSiWk1tyibDT8t29BdSnCjsWmuFGIKKgS9RgVLrHlDOMby3fEBlWLz4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روزنامه صهیونیستی جروزالم پست:
موساد گفته این افراد زیر نظر وزارت اطلاعات ایران و با همکاری سپاه پاسداران انقلاب اسلامی قصد ورود به اسرائیل برای کشتن مقامات ارشد اسرائیلی و انتقام گرفتن رو داشتن که دستگیر شدن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81133" target="_blank">📅 18:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81132">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=qKRHXPyefsUxEUldhMU3rN11g0I4Awuihex-0DPexNydA78JELU-gcBuy6PiKKpcH60zsVCRQ4B2OuCbZ9MYocYkUuMg7m718pKuA4jI4eMa9MdjBqz6V3VhNYSM1GVUXn_hIb_fh6O2mtFgAtDQa2MUw_PPJWfVvd2auKrtH5LOdKfbh4k7d7MI0htNWvubPRSWN-bnR6SEJNzaq2TkYeunhRb6RdajQxZJws5SRvbQmw6l3icYyQegey1T5eJqq_LTt_7L7BsfnQ0DdHEjtfTJuYyj-U4_m7TQNn_aS6ICXHarvUNOumpLAc7WPK8pHiqg8dFSBCfeo7FgB9SgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=qKRHXPyefsUxEUldhMU3rN11g0I4Awuihex-0DPexNydA78JELU-gcBuy6PiKKpcH60zsVCRQ4B2OuCbZ9MYocYkUuMg7m718pKuA4jI4eMa9MdjBqz6V3VhNYSM1GVUXn_hIb_fh6O2mtFgAtDQa2MUw_PPJWfVvd2auKrtH5LOdKfbh4k7d7MI0htNWvubPRSWN-bnR6SEJNzaq2TkYeunhRb6RdajQxZJws5SRvbQmw6l3icYyQegey1T5eJqq_LTt_7L7BsfnQ0DdHEjtfTJuYyj-U4_m7TQNn_aS6ICXHarvUNOumpLAc7WPK8pHiqg8dFSBCfeo7FgB9SgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش:
به نظر من بهترین بازیکن فودبال تاریخ پله‌ست؛ ولی اگه بخوایم این زمان خودمون رو بگیم به نظر من مسی بهترین بازیکن فوتبال جهانه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81132" target="_blank">📅 18:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81131">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk5-jntYoaFl9GQsyboUQhX6bFQg4uuuwuSNuJpf6kgCjLTUuUKLBeYwVZRYgHlw-ru0sAAbOU-5fqrCWjDPvzIdOpzO05Oqt0oq9s-ZVSAD9BOzLGdfuqSqHynjrCtT-57C8hZndWTf47_DTY0MzCqB0WyC7bcm70RXgCa-XzVO55NYJpYI3kpEhQgAUwwgkOmW0Pt4NnRl6-rqlut45sbCGXQ6SH-vo9CiaIeV6ZEVFIpyD7TQRQtzMytOInjXls0J-0KucJOkgbvmW_x5awh4MX6YUOV7_odB5ChGmQpay5vRrZy9CLvRbDk7MPz3UPiccC1RXcmZEpNVIcQ_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81131" target="_blank">📅 18:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81129">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">همین مونده بود نسخه مناطق محروم اسپید به قاف بگه کیری.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81129" target="_blank">📅 18:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81128">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=UBShd0l5tb0F-BIuyAt4VQvwlS9Y-tOGHf06VW1vRDml8RImlWvcKY2tO1FzZNtB9qr4_NExGP5gcUTR6S-f1sFBTAWxnDEYOIOf1fEREctlQTQklGpploluKrea2nGT8FVhbswqDppBp4-YrAhcoEJq8rBTFPUcWTIGKFKIwOTbMflvzWTzWZ0e1YscIK1sJyWdYoMdlbm4JoAuy8JA6lGFi-UNM5ca3qfU-LrOEbBWNnHgDUBlPkxI3v9XOEn2V2Lz7_QIcp0YUaj6thYum6CzKyY1M5T_wHfsTtQaWanoOK0XpoQ417P6xuf4OC8FO4boTww2_n-8uN_kOUf4aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=UBShd0l5tb0F-BIuyAt4VQvwlS9Y-tOGHf06VW1vRDml8RImlWvcKY2tO1FzZNtB9qr4_NExGP5gcUTR6S-f1sFBTAWxnDEYOIOf1fEREctlQTQklGpploluKrea2nGT8FVhbswqDppBp4-YrAhcoEJq8rBTFPUcWTIGKFKIwOTbMflvzWTzWZ0e1YscIK1sJyWdYoMdlbm4JoAuy8JA6lGFi-UNM5ca3qfU-LrOEbBWNnHgDUBlPkxI3v9XOEn2V2Lz7_QIcp0YUaj6thYum6CzKyY1M5T_wHfsTtQaWanoOK0XpoQ417P6xuf4OC8FO4boTww2_n-8uN_kOUf4aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین مونده بود نسخه مناطق محروم اسپید به قاف بگه کیری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81128" target="_blank">📅 17:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81127">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0183a12a61.mp4?token=kRNN1-ZYzNJJpjmNXxZyqL5lUvviWHf5ML6fpVbz_UeGKNrt18tolU0jxZ0TEWeJ1uaacap2auPW9LH3UtXwN3bmWCt-PMnICSgIbhquiKbw7G_XzNdkr3MoumORjpBqcdumeR0rD9p__9n2jltvjx-ysHIyQBRYTZXb7VHeDkiP0v5j9gGvLelMeP0k3XEjlbNVCsgPrQJLF2jFY8uV3l7Db7aX_M4kuapBQarj-fMg7nXP936GIQfq9Whego2CeYwFzQLzSrfiadOymbPbzDiinClYfHEY7S5C9aR4vuezhquskRJGp5326S_rR02io67FN3zsuLvTfDySAw3Jsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0183a12a61.mp4?token=kRNN1-ZYzNJJpjmNXxZyqL5lUvviWHf5ML6fpVbz_UeGKNrt18tolU0jxZ0TEWeJ1uaacap2auPW9LH3UtXwN3bmWCt-PMnICSgIbhquiKbw7G_XzNdkr3MoumORjpBqcdumeR0rD9p__9n2jltvjx-ysHIyQBRYTZXb7VHeDkiP0v5j9gGvLelMeP0k3XEjlbNVCsgPrQJLF2jFY8uV3l7Db7aX_M4kuapBQarj-fMg7nXP936GIQfq9Whego2CeYwFzQLzSrfiadOymbPbzDiinClYfHEY7S5C9aR4vuezhquskRJGp5326S_rR02io67FN3zsuLvTfDySAw3Jsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای شهریاری
❤️
💋
💘
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81127" target="_blank">📅 16:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81126">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترک جدید ممد به نام فول فورس منتشر شد.  SoundCloud  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81126" target="_blank">📅 16:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81125">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0qklb-RvRdWbRUQmVHLyulcbnHKm3EXlei-FISG_ednSR8Oou0yNh9KNyQWfGAJWOu6v_oNLNyTo4GU2jOHKb7mWldA8UOKzFyiB7GxGcRM9PyMj05Ddc8IQNruXrSXP5CK8TMDp1N4WtvjepLVxkok6ku2XJA1p5YeMfBnuFbGA5n6aUsjRtQNx-BTkhGMjVhi_JuVXBxNP_1rtC5bYlzrbucvVqFDlnLPm2r-QwXl0Ex0mYtcFZII8sI5iUImQX58gfBzqtU30bO5krbgSG6Evv-n3f2b1gsQjsHujVjLomX4dIGoXSz0fKPKnEiAkf4nrqaNTzIaX_TNCmVW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد به نام فول فورس منتشر شد.
SoundCloud
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81125" target="_blank">📅 16:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81124">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امباپه هم دستور داد کارکنان سفارت فرانسه تو تهران تخلیه بشه و کارکنانش خارج بشن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81124" target="_blank">📅 15:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81123">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">متاسفانه با اذان صبح، رومینا و ترانه رحیمی خواهران دو قلو اعدام شدند.  همچنین مادر خواهران رحیمی می‌گوید به یکی از دخترانش قبل از اعدام تجاوز کردند.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81123" target="_blank">📅 15:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81122">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSlUAZrubDt2cmsUjRhxPh4N4gKpmUTJg8dy953GB7_P-17EVcb8UPD0bs0rgGPD4ZnNAUV9Xqp-R0XV6CcUmYI8EY9wVjzHjFfdWa397LI69_zksqHib8jIXxXepDLGz2BEQV-VRVu6F68jD2GSzc_HfmjdGjW0h0jzwLl0Fq8ELAxCzc4Ny6FM2LwP7Ch-3nTS9l-HwVuhxpAWthZ7Oi8FSSqF6AhfQ-6besUxCTulh2wg03krAUre-RwfKgnsaOE5i9gX2tnabWE_DS64yLyLafqW4xHLtqFhTNs9XCR0a5iKFPtaYHZ6iad6pXKRXAuzW1LwWGWGyzz8DEejuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه بدنی ساخته دو رو.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81122" target="_blank">📅 14:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81121">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITej8heelieIFslL45QQFRQjH11UQBzZ8BmdhjFFBNthwZmAX-UX0ElyK6wm7zGgJIvQylncrxUohNsFriqzqmeCEY_rnalnXovvEl2hQoq4YhtAPIwVEVMxwsTB2TRLihWVB76TkbRV12vdvNluDRPPyrGgYxp3iHGnTnQADkTgkFdXQkHtc6BC5gLR8QExZU2rONRLpYJqxIBQgggsTHS_TRrBsxSa3Lt05vVgiYVNX9BIuGj_wWZJaCuREk0VfXoQogzaLBnO3qfmQYBa-7Kpw68fESg-yz5QcJZgxjWLwA0voSbcTolB_ysTC3YrPzyc-fLhXkDqnbXj-MF2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتای اینتر
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81121" target="_blank">📅 14:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81119">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KmNgwe3FOfYTO1yfu6ADxpqr-q_V05eM-IZ_FWPD7t8L5Ukz2MTV7Th6TV4qvqhocKsrX8sJDhUk-WW0vMsyA68MN6fuM_3CHdu4JUS51Xt85jbkpmL2viyDHopV3QGgxcSyqBt99kYC-Y5ajKB0jAaS4EIQNpfHq_m1l_S7TyJar4UuagqkLHlu7BWu-wcWZgPI_TQI8gLpuwfmHzSiQiKL0mvABmLyqIh1m9uk-NgRB8Dp_oSH6hKoyrJJ73eVtW4FtpXLDE_-3dXMw0MXT8wqYmgmIRhA6IbdrpMsQ-FEWzCtHSbTQ9o7AB8OcuyxQVm_wgXYewhKEItV_FNzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YG92Ec4f4VlJf7iuHAR1g5Mj54aXCH3iVZHy2LQ1ksJmJMAGGJGRYmstX08XJenV7_K3NaPUlYupuLyUW7326R-UmoheqzI3Gth1ueuaHAstlEYK5tofcXSTB32YzLT_KDxuj0oZytCEUR6FHIBiP32bR-wdJfcR09wFC4Ct6coOcjo1DGZmNMcJ1q-Onblrw_3a4lHQz9Z9ScAiXZyryb6vl14cAF0_xnfE-e5Klz4mWBVn7XVJ-k7PEBEj6witFlcGFXJx6gx7Q23dDpxRJpOs56uzyIyzgVyjpHcQxaIYzTyzQZ5tTdUPfX2FyFo3SYoz0Wyqkb-J3EBkn7IKeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیت دوم رئال مادرید چقد کیریه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81119" target="_blank">📅 14:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81118">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl19Y3er9xveQwAPIuvA6lClYTiqTn8VWSL2C0Ouy-cwPSMYgo6MJ7uuVESgKs8cELooMHc5H-fCQP6Tn9fNlB9DGQXYaKt53oI0LvjEE4d8xhwUOgASlCnHtaWLpA7iYmQAtuqhb44m8HyqKg78fCFCUElkFmKFa1E3kcYogk7KmmZ5FN6Fsqx4CiQP99s4GSKS3ATJxK5n6A0oU8SnC3IOZEDLtuUJJLhHbYQ3pxW0AJst49gDww8Tm0yt12OIpDBy4tD9ZL007pQbRBf1_q86IoE99gzCfGOgwHaPZzCH-1EFZTq2yMjYY8Rn310SHKjMIGUskTn7ZlcDBLt3Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
میکس روز به همراه ۳۰ درصد هدیه در بت‌فوروارد
🎲
⚽️
با استفاده از برگه‌های پیش‌بینی پیشنهادی میکس روز، میزان برد خود را افزایش دهید. با ثبت پیش‌بینی بر روی این گزینه‌های پیشنهادی علاوه بر مبلغ برد،‌ با توجه به درصد تعیین شده بر روی فرم پیشنهادی تا ۳۰ درصد مبلغ برد خود را به عنوان هدیه نقدی از بت‌فوروارد هدیه بگیرید.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/EXP
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r1
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81118" target="_blank">📅 14:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b89IbUQZI3Je8Yc0pjVkIUUq_i5_2DeLRgPYPLHXEmLWxrJDY0fCu_mHK10pwew_Zd0X7JaAhc9kOQC5YljwLTEJB-RmHK4_HCtEnXuC2aTDqPOMB6aNQey5-oNDTx97dvlkNIaXK6ras_ppIT_CXWKIKYie2eNcB-WaKtQgb-qsyolUZfuncJ3uvbRBds_rJgNcNrC0MvgW5oT7D2mtNPtD7Uan48hxIbTR71foANjWgxKHcmDt_trFKHuukDuulCQVFKR6yJWVNNIFiVxjIxbV5HdYP5hQ6edk_Jbw_4IBW1-z41dI1WD6Cln9V0VccyM9lTL1LS8OAAsprtErdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرصت ها مانند ابر میگذرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81116" target="_blank">📅 13:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81113">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxvqomBvRmiheamrJZ-T6Yisy9l7-hqapkBa95ewZAsPf2VLus1H302YEhZpvUQ3tXK-AgmLK3JdoBIrhZvakPTrkNQUUMyMRV2WvjyrrycnhzI_JDAflAMmp39zF4wYKh9EFs43l7dWsM0OfDsdhiasqJhWg4MdgYFdOemWVYV-DEsnlgKtdiuu7B9dZGAZ6oB_5jgx_R6uS_u8W64Oj-rDp0bZSt7nq1h2vi5eC8ib4_gCB1ZFEhMw8HEkbamjW-arzDX2S3lZPkAs48d7qSWtIpM-KrHQH5OaEcDlbY_MSzfi-m1c5eSCyhJ0E7piecTaGRck0bBILDjBfbl-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPCJTTghRY-TD4oyuEpDigD439mX1vRxj2QvZJxWHrzG1x7v4nI_aVhgqYuhyHBjYu2Mh0ptClzLsCPj9zZoEpvrPRCPs0CIda_kh9HsU5Kx0UNqlPkLTdgHrnf06sqhhSfYiqx0bzIJ5-hiwy8I1zTQfXkRnpGVsNhA76m6WXgYiHHDETXPBvB28ZY6NBO2be6QaXrOkXa3Z_oG0qApP-eVIlSWm1NewkU4W1E4QhywGrLqbXcBIGYhAWd6cc-_V4iE5RScSlq8iRK8Ir3PNYqet--yJiiy8iz9NhMybjKb10pgNcc7LsBzkUjRuIaAYY-iRQd8GU_wwnN7QeBksg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندریک بچش به دنیا اومد، اسمشو گذاشت کندریک.
@Funhiphop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81113" target="_blank">📅 13:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81112">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_fN4z8cs7rbYSPEhXz5aQMx-Zb0KGaYsKPQ8shYrFORfm7MB2G9wH0lJ8BB1g-CaXUmpjSAE87frO5xXWqQm65Jj-2cF0HbRU1gI2l5IvbC7JI6m7LHZmhAathNCjimkr8BzwgMWOqd5CW1JlNAJwgC-eDW4rigujDj88kXH_djY-QUpG0wABNVcoyK_T4VC-O7d5JndBOG7dfiCQBWfz0yXgGF8haN6l9YfwaJYRzmjKksYHjTtkTFa4r_O-MMCFQ0MbKVIfGfEZW2TTGwAtKd0wJQz6tAzvsigKVLYWh2knzRbLoQFY0OdkIsLMdcPQoC_RrD02MrWhJKOcElmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو شکیرا در کنار جوادسیوس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81112" target="_blank">📅 13:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81111">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترک جدید محمود به نام اما تو میگی نه منتشر شد.  SoundCloud  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81111" target="_blank">📅 12:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81110">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgSkNYyu9VG88eEDQbTfHmF3XJrJ2QyJH3uJ2gsM3sUonEw-uDYYePk6hBnD9iONrDYjEmoCQFoj-kbBG29QHLRoQQjN-4F8FdhtCKQu6MpYYFpmh1p0fkZmo9WMSCdu6exzH9IDxI46XwsgN9lJx8ZcJaRRxOi4JAp-zFdxMrtepcilXjgj_9EObMZkwH1qO2mHEEqJaIJoLEpcz5uAJ1tHMdL82kXDukScfEziq7T_TMJ68Yho1tT4_W-L2Ken7-d0w7K2UziuiSE24b8aneBTMh_ZuqHktpJo25-gv4LrTpJc3mSnnfB90s0ZqttpxX_RtQHQ54Rj0mrmQMJ18A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید محمود به نام اما تو میگی نه منتشر شد.
SoundCloud
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81110" target="_blank">📅 12:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81109">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riOwZWwVzkbecz1S5uFksTPQ-EPX-jfegTGVu-6iNhZ-Qk3sSfs9Lpp9l74RDmwgbxeX16uvrYtf2KdH9OeZ51aJJD6h8EwjNZB6neDGMHEKFNjf0JVn9f5bwPRwQkzCRQx1WKc9_ddplTq0_IPQZH26k8NbaxBRyiwW2FhTc4FQ978qXiajB3wltUC2sy8UJ_uu41bpFWZ9PlfzDiGwXRG_wkledj_uWt7HqftnBhxumVSIFoGmHwaj4Kf8LvkfPb3j6qsXJ2cVP09yRtCsawBtOBig2_dvG9I05s3as8Mg3m8QBcOJS3hTeWhXyTlmZRoJyE72jCSLVJOAA27UAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه با اذان صبح، رومینا و ترانه رحیمی خواهران دو قلو اعدام شدند.
همچنین مادر خواهران رحیمی می‌گوید به یکی از دخترانش قبل از اعدام تجاوز کردند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81109" target="_blank">📅 12:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81107">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مارکو روبیو:
عراقچی می‌گه سیاست اونها چشم دربرابر چشمه؛ درحالی که من معتقدم سیاست ترامب، سر در برابر چشمه، اونها بهای سنگینی رو پرداخت خواهد کرد.
هر شب بهشون ضربه می‌زنیم و این ضربه‌ها قراره هرشب قوی‌تر از شب قبل بشن تا جایی که ممکنه به یک درگیری گسترده منجر بشن، این اوضاع تا جایی ادامه پیدا می‌کنه که اونا عاقل بشن و بخوان معامله‌ی خوبی انجام بدن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81107" target="_blank">📅 12:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81106">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ازونجایی که فارس بیانیه ای از رادان پخش نکرده پس قطعا ترور نشده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81106" target="_blank">📅 11:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81105">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBCdIW3pOzpuyhiXCKIKNDLFidFfmPNR7BDda1po-krlnLKyORny1JhfoZRN9wt3_my9NtYPuC60S-yzQVI318vA1rqO0t9LQ2DqfX6QHesHLw_lYCysoX2vi9y_tzyxY5JBWNRoN0S-pmg-Owo8tzX4Ril63Nd6L9Ac45Qmf32mjaTpWH_gIdZIveOMTHhxC-saOBYTyUOjrZI1iTciDf84sYrbkzCGBQdygtl7YXFf8hCCng36nlov1TYQkUvFBBkA9xpl45EOZpUZtLBbejmK3sB47ew2B0jzMfApiQ19YzOksjOMZk8cdl1Wt-Fhb4RpIRF7eZ3SEIdwFM4tVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقم میدونستی ایران نباید هسته ای داشته باشه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81105" target="_blank">📅 10:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81104">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aacc4be5b.mp4?token=hO81Hd_TcR1-mPZFsRrfviCFY9xM3AOqbbw8qiyRW6-kzOdoCY3S56f_cSwMzy-oh1FHH6ntoZ8e2zrvsLzR2on7tQ7O6jLuz-827CySm7CkYsgjgK3Iq6RcNt24p8wZ2W4lhNCHczZaMaR3HoHWiukqmrv-DUx3I1con-lnlyx0Ixw-XAFjDkgnSAltYAYqhCcqwwOEdpHD6yQQzHEzh0sVcwS2k7sEe_P_lZN0FOiymeyHFruSod6EgOCMhoT5Tgbz_Wixzp2upqLjGZ07jQh-ZkTXiM1tfpbCR_e20EVgGpaqPAgdOz76KXZWpQHoz0DYdCF4D6mIYgu_6ZR6cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aacc4be5b.mp4?token=hO81Hd_TcR1-mPZFsRrfviCFY9xM3AOqbbw8qiyRW6-kzOdoCY3S56f_cSwMzy-oh1FHH6ntoZ8e2zrvsLzR2on7tQ7O6jLuz-827CySm7CkYsgjgK3Iq6RcNt24p8wZ2W4lhNCHczZaMaR3HoHWiukqmrv-DUx3I1con-lnlyx0Ixw-XAFjDkgnSAltYAYqhCcqwwOEdpHD6yQQzHEzh0sVcwS2k7sEe_P_lZN0FOiymeyHFruSod6EgOCMhoT5Tgbz_Wixzp2upqLjGZ07jQh-ZkTXiM1tfpbCR_e20EVgGpaqPAgdOz76KXZWpQHoz0DYdCF4D6mIYgu_6ZR6cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی مربوط به حمله شلمچه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81104" target="_blank">📅 04:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81103">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9LaLJTjAgYCCoYHLCn-DlT8kGrT-94zOL9vtjYdC-TBwYLuowp6gFuj33oEoT91nCHb9BeapkUmPS3qnOLPeFSK70ZzMmIHo7qKnPXc14NNgiNlcRJ-ZE10D3OObJ0QvsyqlJ2Hm1Ke9chjjfBTXjwqVh3htPBgohCReElwOYW_Z8GU3PHyozLZRIFM6Bv6HGfO3Mw24VXrjoLWhAwAzULym8R5pmnuY0GhwbHLzND_2Dc4hBXNy9OkbpJ43daWhHa0I0-a8Q1X3igZuyfVmuJFM9SHktepVjU6IqWypRwqy9lyqtdlILjpLqNskWmrQC_yx_mTyDdWsnm4pf4Nkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس امروز از رادان تو شلمچه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81103" target="_blank">📅 04:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81102">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امشب امریکا پاسگاه شلمچه رو زده و رادان هم امروز رفته بود شلمچه پس این امکان وجود داره که هدف رادان بوده باشه مگه اینکه قبل از حملات از شلمچه رفته باشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81102" target="_blank">📅 04:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81101">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg1prdlHweQdkhMsG1CvOrE2Q_HH1Y91AEqxM9AcRn0JgTOtwjndVLOVYJlsiABwPo6xUwylvmYh8SOivBne-X5oPeHlQRzJeBhNEE_ubt7nZDbS7gdt2D3mvoWtYEbV29CC75zgx6t5yOEERT713AhCGo0H_ogK8UoaMzAGd8_83YtyW3BuKitFbpLP55uYcJUOyi-TFj4yKgFuSwCkjTHq6OF-6z-RbR2wqPeWiofTLY4Pfo7YA3nKFsHn-GgoNyHT__huQVEYW6LRizkcyO1gIicLW7ZgRZWs9yTpX3sIytz5ZJ88BiGHex1tamt5UnxHgFevaJFtakaUKtfdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب امریکا پاسگاه شلمچه رو زده و رادان هم امروز رفته بود شلمچه
پس این امکان وجود داره که هدف رادان بوده باشه مگه اینکه قبل از حملات از شلمچه رفته باشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81101" target="_blank">📅 04:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81100">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بیدار شید فک کنم رادانو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81100" target="_blank">📅 04:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81099">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کرمانشاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81099" target="_blank">📅 03:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81097">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06dd48cfcd.mp4?token=UeGoufVXEccIA7C1DaAUJoWpOYHtB-XIBJKyrHoPkPS3G2UTGMwWOE5mVKsAWKa1SLvdsCDv-CNptLnKv5Bp9fS5RdQvJ082C9f-aEjh3D9KV4thhOzzju-7Vkj2X7Pt76lb-jfSjNI6Z9qjoFvRDR0qQJ2EyVH1FSkyGH5yW7vQztdJ9W9rAc00pNM69yUeTqrVnpLpANbKl84HQ2su8Vh-Zrml44XkMjUH3Vw-psHjAUtQklh_u4ok11sdKH99u1AsXrJOXqNHjlwUqgoJHnRtVXXZHq7KspTiNg82GXpjE7oRJQXeVPBLbOZ4peioPbmFFETREm0pPc-kPouyoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06dd48cfcd.mp4?token=UeGoufVXEccIA7C1DaAUJoWpOYHtB-XIBJKyrHoPkPS3G2UTGMwWOE5mVKsAWKa1SLvdsCDv-CNptLnKv5Bp9fS5RdQvJ082C9f-aEjh3D9KV4thhOzzju-7Vkj2X7Pt76lb-jfSjNI6Z9qjoFvRDR0qQJ2EyVH1FSkyGH5yW7vQztdJ9W9rAc00pNM69yUeTqrVnpLpANbKl84HQ2su8Vh-Zrml44XkMjUH3Vw-psHjAUtQklh_u4ok11sdKH99u1AsXrJOXqNHjlwUqgoJHnRtVXXZHq7KspTiNg82GXpjE7oRJQXeVPBLbOZ4peioPbmFFETREm0pPc-kPouyoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فردا:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81097" target="_blank">📅 02:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81096">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mASXiFXDh1Y8MMZYbc4kGFyvJBSp6yEdw8wTD1RBCz-am0Nh3aWtxegr-afVdRt16h4pV8uVJYKOV0vaGaN2s3AGIGr_XzBFr_Dr4bmATbdnuucZvvSkK9NghMbTDtufakv2_ameDB77ev7PP5x4Nbq43I0o2UEXznkQw7u3ePDvzHaccTN90iD4NnCpjwmxymE3z3wMHeX5TsF1JHB-Nr09HodHSC0jE8iPdJrok5cm4sfTacIzQGSnDtW9ohXEiGAHmcvfAzi-csUB8KbssITgT8xYQv2nKoN6qc0jGMK0SUVyRwvkvLDT0SKsYbxLm2xwRgRb1U0qUL3akxohEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا بودجه ۹۵ میلیارد دلاری تامین هزینه جنگ با ایران را تصویب کرد.
پ.ن: به گفته امریکا حنگ 40 روزه براشون تقریبا 38 میلیارد دلار هزینه داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81096" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81095">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سیریک
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81095" target="_blank">📅 01:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81094">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پرواز جنگنده های نسل 66 کوثر بالا سر تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81094" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81093">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOCTqWfFk2vIHzkTmjEyWbAWESHW6CTuf3P2BzxxQsYT970wiCAL4ZANy4oWuscsOjIcFb_c48wIy5f-dFNlIVgge7zyDVdxRkZPtDPFs2V1W8rcV30WIRuoyKMw2-QGQJlbo6CNn6Hu9NoTD5y6I7j8_2eWvMnlmaEzUXZLR_9HzH-Un0P-d9by_Ytx7BFePI-dGwiJGGoJyqA_rH65eTrfc9x-oI37CGyIkIBbIjxqf0KtoU5xss4QLHkpDtaUlV0zuYOU1R17FQROpAyaRTmfGpO88Na_5M0QJkt1A3uKPafBJJAVBZEykZpTjgKj0CIZXMcU8xnFcWHu-z2Y6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق مقررات جدید چین، استفاده از برنامه های هوش مصنوعی عاشقانه برای افراد زیر سن قانونی ممنوع اعلام شد
دلیل نگرانی سیاستمدارن چینی این بود که شاید افراد وابسته‌ی ربات شوند و تمایل به ازدواج رو از دست بدند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81093" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81092">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81092" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81091">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجار در ماهشهر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81091" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81090">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ میخواد در های جهنم رو به روی ما باز کنه نمیدونه ما خودمون تو جهنم زندگی میکنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81090" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81089">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ میخواد در های جهنم رو به روی ما باز کنه نمیدونه ما خودمون تو جهنم زندگی میکنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81089" target="_blank">📅 23:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81088">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کان نیوز:
ایالات متحده به اسرائیل اطلاع داده است که قصد دارد در روزهای آینده حملات خود را تشدید کند، از جمله اینکه برای اولین بار در این عملیات، از بمب‌افکن‌های سنگین استفاده خواهد کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81088" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81087">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چه بدنی ساخته دو رو.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81087" target="_blank">📅 23:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81086">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxGdrorT74Pqxsqo51E18a4mt3TdMMZppR7u11CnK7qvnZzi6mOEX-U1bVI_ogNsGg5IYACM1t7XGNbvZyyd_AQn1Sy4Q5UTlt8hO6Diore9y5hy4i1yAIiEpso_K37AzgujK1GUX4r8kAvu_QW21rOoZ7kzrmJo2oVcctEUyCBuzWYY5_GYJ-FRD_7ktj4gEXGqn_MyACe7pLrGAJBSzNvs7qHfy_su5mVdB7FMvs2bbfN_yMetjqKwa1oxZInq5IIsMFsCsXKHVjBNxHnxiiQByG-SbstHguSrY-j5EtkxwRYIim8mLAFOLYnpFaEa1jV3smp2BpH884cPjlyHow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه بدنی ساخته دو رو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81086" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81084">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiGJHUWCV9fQrNWesmwkh0wCoWcNN3c3F655qcxmNaieFwS_NWL9Gwna0fI-bgxzf53eTFHb5nocvIwzw48Umv8C8m04TseBBW_r-BgcHIJ1QrLUpPmPTihOiaieTOpHEfM1YPC-AGcDU-y7J5WW5FuxRht3czBO87ZnE2hs_UpK1NdfcB6qWIsNeGtIoyfGOMDfGrhXfBzY1PshuDHtKJP10ttMl-VgyW9kjqdBux-BN6z6wJOt9KbKgWtJQzNehqG6n9Z2Izzbc9xbZXLqT3C8j-BESEThnXTSKoQu4q6Dd-pp_0NUGrD7aFmbButlCMk7z8vO4_1_oeMacJ0o6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار جان پس اون پلا و نیروگاه‌هایی که کودک‌کشان تا الان زدن چی؟
اونا جزء تست رایگان ۷ روزه حساب می‌شدن؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81084" target="_blank">📅 22:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81083">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiCIKXZcnOA6cSXTFqQQB7Tiq7j1njNI1geJAeLW5WrrJ63XWluegqfGY6Ns5sBjPAo6ZHP1waiHaINExhDlfjsmejWB_e17OpDqtK9elAQmAoUxLTWnrMsxHPjZ9UNY-z5TXg8N59RsbRzRf7Z_a8sD-vONz7QFzaU1fToMzbj2tl-oU_rJv-azY4P0p6aiWi8_xyIzZSLcLFnbHcKZ_flFTVVJxlVuxaq9s1gVbPKFiA4eI1G3IpPXtIN5wipxsM69XTZUHX5HcuK_cYNUczBaRQka4u7XwR0yX8gk4L_ZBzo8QDwsX1MWjhoC87OKjB5jkAGexZXC05k6onCrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا نخوابید خیر نیست مثل اینکه
انگلیس سفارتشو تو ایران بست و کارکناش رو هم کامل از ایران خارج کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81083" target="_blank">📅 22:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81082">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvhbSaRkdZ0kBxa8P2CNYub7kdQh5B9qb4uU8TO9-S7-GAV6UQVxXrWDLAn7Pfj3bGEq9Fwryv74-dQojuD8ZaoTy6T5R-hFpZu1uQWlj39SJEhlPEokGDrzs7R9_ffcMQLQPC_hKKMlhoFx9yig4xhatQhIj4hVgvKQiNVo8U8f53uX-K8vxYjPoJi7zPVwuja7pr2Dazg2XJ3_MJBVPFIW8PS7Z7W__tWgIK9N_iAYbTvGvV5PJbSOM_XJ0elEttQ4vIgsZUEfhnP062yq6ZSA6UsMbwoHvrOIzHAv3Piq4u4esFeDa706-jy5nsluYRosnEMZZpU5uaofvOP0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینکوسمادر فرمانده گردان القسام حماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81082" target="_blank">📅 22:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81081">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a367c7357b.mp4?token=NDhKbITfYYWkDc8T5YoFIlDUidYiIh9U1x7vrbPTI6trP3M2dfyTr1IWpVXNgmn2ct7KWPL8BIAoTVVZP1Khg4_oCG-nCEwP4RasVGv8RdgNRWUrGD1R-39hJTTo7iTQJoYJ4zplHqUJaRjurGz_qeQTM7JZMWR7mtuld3a88V9oFNqRNyjPJcObVHRvxuc1006QeOIF93Q9xuzbMdrOzrbiiAQyx28Frdv1JyXIgN6QO6hSH7A8mcQ8YUEjoYh6j3E4WBQlhRuCHu2-baQb5sqK7ZMHF4BNXx9XjNJX9BswUPG8_6DTKAAZ3bIEuVPKXEhY6kKhudVA0wtKdUqr_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a367c7357b.mp4?token=NDhKbITfYYWkDc8T5YoFIlDUidYiIh9U1x7vrbPTI6trP3M2dfyTr1IWpVXNgmn2ct7KWPL8BIAoTVVZP1Khg4_oCG-nCEwP4RasVGv8RdgNRWUrGD1R-39hJTTo7iTQJoYJ4zplHqUJaRjurGz_qeQTM7JZMWR7mtuld3a88V9oFNqRNyjPJcObVHRvxuc1006QeOIF93Q9xuzbMdrOzrbiiAQyx28Frdv1JyXIgN6QO6hSH7A8mcQ8YUEjoYh6j3E4WBQlhRuCHu2-baQb5sqK7ZMHF4BNXx9XjNJX9BswUPG8_6DTKAAZ3bIEuVPKXEhY6kKhudVA0wtKdUqr_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر بار که با خودت می‌گی که خب خدایی این دیگه آخرشه، این کشور یه پدیده کاملا غیرقابل تفسیر رو به طور معجزه‌آسایی خلق می‌کنه و مثل جامپ‌اسکر می‌کوبونه تو صورتت که بگه گوه خوردی که می‌گی آخرشه، تازه کجاشو دیدی؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81081" target="_blank">📅 22:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81080">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">راحت بخوابید که شدیداً خیره و توافق نزدیکه  پست جدید ترامپ از تیتر یکی از خبرگزاری‌ها: پس از کشته شدن سربازان آمریکایی و حمله‌ی ایران، ترامپ به سنتکام دستور داد «دروازه‌های جهنم را باز کند»  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81080" target="_blank">📅 21:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXdx-jrQTtDH65GQxu6Tqd_8jiCbTWwMUp74GcUzjM2hlYnLWxbOrEos8nSEhwKs5VTrJgCXnBoJ9l2NJXzhPiHK_IjErSpeJqed6TLjwNYQ1pSEms06FSSA4zaa-oIh_cdmDjtcKMoTjPmplZoj0yf9xl55sSjRd-3na_IOur5eo9zwMZPRYQJ0CgNxQlOqTZhPOItVeyw98h9GBM2dSHi9C99LlYzWTxG1lDlXG3Dxq90xQs9T6Llk2rxid_iX5wNMmkibCSmaDV-70DRdY9pd2S7fy6LoYldHPzfM47t3r2q1cDX04f5uV7nJbsCRi4QZsry0j0nW-v47u9O78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راحت بخوابید که شدیداً خیره و توافق نزدیکه
پست جدید ترامپ از تیتر یکی از خبرگزاری‌ها:
پس از کشته شدن سربازان آمریکایی و حمله‌ی ایران، ترامپ به سنتکام دستور داد «دروازه‌های جهنم را باز کند»
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81079" target="_blank">📅 21:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حافظه تاریخی پرداخته ب فردوسی پور
برید ببیینید</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81078" target="_blank">📅 21:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81076">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پزشکیان دستور رفع فیلتر اپلیکیشن و سایت عادل فردوسی‌پور رو داد.
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81076" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81075">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">صبح امروز، مهدی خانکی، دانشجوی ۲۵ ساله رشته حقوق که در اعتراضات دی‌ماه دستگیر شده بود متاسفانه اعدام شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81075" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81074">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خودکشی جوان ۳۰ ساله پس از شکست آرژانتین در جام جهانی.
«سیمون حسین» ۳۰ ساله، متأهل و دارای دو فرزند، تحقیر ناشی از حذف آرژانتین از جام جهانی را نتوانست تحمل کند و تصمیم به پایان گرفتن زندگی‌اش گرفت و همسر و دو فرزندش را تنها گذاشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81074" target="_blank">📅 19:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81073">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وینیسیوس عجب کراشی شده.  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81073" target="_blank">📅 18:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81071">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vs5fwpG9wFW9sR5RGS6A0vhiT3eV2NcG2h4r1VDlIMTKYOuu3zS0E3xX7LilpCEy8X7jaEU3Qi1XiFAMGvVKcTDhru6ozyTWNQBrQ9bDG_SVZ6KFrc1qbbz2hb_qCxle7JsDe2GL31y1veFyl-gxxDS4ReNjFQ2agKe1SOpfvsZs1-gEO0yGf3d1kuqQpitys2s-tQpv8-jm40C6IaZRxm0Ei6fNREPsffY6fF6fWk034Sd2RZMw_5j5y22CUPMuojQ6GlTF9KjhQHyPKWan4PsRYl0EcLwP7xPUV_2sxWC05qzp6FsefNUWomMPD0WYDLa8savisX5XEmHbpLqsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkwS0lOPsfIshXqyXk9DO40lONhqvc8N3WFfIBmhKWKBNIv04BgOHf7yHMDhSn2OuJDNLXmGGyZEDZxvhKqWm61N0DoWFXV2BK5y2OZH2V2FgWf-3y1-v501mrojRyib9jJe9_wgCjuRbxsom-AzbmJM94CqrLzDqui2hYA3F2uC89_JvrIE2TqbkDPA9xc6J03G8WHwQ04Q2Dr2xD9R4WGiUR-cbTdvjCRt1Fho-hhTKMa_dUjt4RevopxOba84E0uLVhPO75Z21CRyKIH8Yb87VD1HAolfgeq7QdQa4ri025F50ocAEECVjrk2hZFYoByoUciYluAQ_XaJIFCRuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینیسیوس عجب کراشی شده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81071" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند.…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81069" target="_blank">📅 18:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">توافق قطعی شد اکسیوس:  ترامپ در حال بررسی از سرگیری عملیات نظامی گسترده در ایران است، که احتمالاً شامل عملیات مشترک گسترده با اسرائیل خواهد بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81068" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">توافق قطعی شد
اکسیوس:
ترامپ در حال بررسی از سرگیری عملیات نظامی گسترده در ایران است، که احتمالاً شامل عملیات مشترک گسترده با اسرائیل خواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81067" target="_blank">📅 17:44 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

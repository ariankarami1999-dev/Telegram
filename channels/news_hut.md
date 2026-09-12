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
<img src="https://cdn4.telesco.pe/file/jA0K8baJmMmMnPAfSP4H0MiMvLrasszTqdjZK5FYaHDGOOxHBYPwS88mWIkKOR9-cK3bJJJoMstjYhcz7s0r0l9PkuF6EuHXNwB9KXAp1SalohM8fj_Q8bSCu1KQaSxvKD2R_PeoluWq78D8rLBkU0T6m8AGo10pPdD6zoI-EgaqSA_LtMREWJpPr88mvxUaMnj6nN_OBZoBx8oUMr9OZeeubnPKo0lBXrHfERNrh_SMEVxNrMfXu9gvJfwqi8vD06YLx-piszm5F5hyZYy2bUqBMR7lKf8x9NMjYdKZxc3RYrYAld704pLKb4BjEgaOt1HC62tm3tG4U_o8HYK0qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 110K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 20:48:51</div>
<hr>

<div class="tg-post" id="msg-71540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=eYgvVlI6tzsDl-u6tIJMiOqQTZ2RsyCCs6mtYUnX2DfHCzz_N_P1S9FsEBMIAUVsjMkrXOAmDqFUzpI40q1OBPffvPwfKe_OW5PyIaPdznGcaWC_JaW9I73obiyJVfRFLaxZ9jVaoBb1VXpqKtWOlIdjEZVthq3wp5cYMoGWWmYiwTma4aFaN1c4nphpWbn9KTH9dahg4H-8kFmNRfk74j6p7UHLWNGLuSsSI9UtTId484XPzRgbarA7H1Wc4LYpGu1UWtZZZbIeFKmopJNjD3AiGLL1IHqbUWMg4FRX4ERPnUvYY1WvX0Tl4939vB6jgGwQpeBkWNPmXjbYBuZYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=eYgvVlI6tzsDl-u6tIJMiOqQTZ2RsyCCs6mtYUnX2DfHCzz_N_P1S9FsEBMIAUVsjMkrXOAmDqFUzpI40q1OBPffvPwfKe_OW5PyIaPdznGcaWC_JaW9I73obiyJVfRFLaxZ9jVaoBb1VXpqKtWOlIdjEZVthq3wp5cYMoGWWmYiwTma4aFaN1c4nphpWbn9KTH9dahg4H-8kFmNRfk74j6p7UHLWNGLuSsSI9UtTId484XPzRgbarA7H1Wc4LYpGu1UWtZZZbIeFKmopJNjD3AiGLL1IHqbUWMg4FRX4ERPnUvYY1WvX0Tl4939vB6jgGwQpeBkWNPmXjbYBuZYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
حملات هوایی جنگنده‌های عربستان سعودی به استان البیضاء یمن
@News_Hut</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/news_hut/71540" target="_blank">📅 20:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOQYGUII_C8KrED11cqdF92WAhDC3304dl8vZcFJz565oDSfE7FLf149WCJCI_ppJfYGEUGqZ0yN55638UQ3RavFm3mPTA-Q7fllyhJydQ7H5T8QdGG3uoKoAYw4dpUitW_-vNHz681b2LrAGxFksgdhj07xk6GvSqzmGfjQGhoLRI6mjLfGaTPV3b4woXNTMRD5qF1OF05SDOdac8o-wrtbX-WYxsF_I39OaZ71V_XX9S7cyyeAQgvZIIYMe8uqYeNuJGXmcxIXCTkshy1RprHVvFD5J0m8Sjtw6IYQPLitjzAyB4OXbu8KnKEN9UCy2ok8H2O5fFlczYMzTxXTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
@News_Hut</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/news_hut/71539" target="_blank">📅 19:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYiGxKxeuH8giuR2sBPwQl_-ODryehO_bVq1HnFFrf5zA3vZsee1B2pV_WtLzOHH6DZOgFSrFQDqGLJonMoqDYEvlkxRskVo5lmErHDAjK8ZgsRXJe3eBIoYD_coLJ584ah5Bj0ZcJM95hg3cQvA9w4FWlkXmXsWb3JfP19Q56Sm-zyAUb4xLDZGtZA1Rwd6_4SUNaLLCM8cB81hQqvzh9nbcs4B0jdPfjx1TH0_kkBj9zNrsX42ixGJcxn8SF29bX4oHwr_PdI5Yj4ivJmJLY2QJw6wxReyd5Kf2os9xHMRYpHmbK8Y8lkqgUoBncBURLLKCmYtd2LuAdo1CFQRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره موسوم به «دیوار فولادی» علیه ایران توسط آمریکا در ۶۰ روز گذشته، نیروهای سنتکام مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
حتی یک کشتی هم بدون مجوز نیروهای آمریکایی از این محاصره عبور نکرده است و نظامیان آمریکایی همچنان با تمرکز کامل بر این مأموریت متمرکز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/news_hut/71538" target="_blank">📅 19:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇧🇭
❌
🇮🇷
بحرین اعلام کرد تا زمانی که روابط دیپلماتیک با ایران از سر گرفته نشود، در هیچ‌گونه نشستی با این کشور شرکت نخواهد کرد و بدین ترتیب پیشنهاد عمان برای برگزاری نشست وزرای کشورهای حوزه خلیج فارس و ایران پیرامون مسئله هرمز را رد کرد.
🗣️
بحرین چهار شرط تعیین کرد:
توقف حملات
پرداخت غرامت
احترام به حاکمیت
حل‌وفصل اختلافات از مجاری قانونی.
@News_Hut</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/news_hut/71537" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71533">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=QnjeGk4JTy6kYDXd1kQ6jW2VXtQ5ZiPf3-d4JA-ILSVv-HHzsLmj4oZybtCKrMbtVG4zHpiSVVsq-Mz7DFzqi7fPElEORabgJCTVJBpcuCjrnyGpMoNwRkKaTIgxLgmZFkjNgotQhgbVTPNWgqUjR20dACjLiFqwbruChsRbLgKMTbeMNp_gZaB22-s61nk3P__JNWDRGYgtWUKbMyqJ3JA2sSpggjcdClz-9VDAhBL7Gy-YkNMjFJY9_f0Adz-AvhguJwO9_zOQetDSGrJu7YlxAEPa5bbW_l514ZLhsjSL_wQaubPgKQszZHqoANNcjfAFbg3XtHeDK582dVaNbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=QnjeGk4JTy6kYDXd1kQ6jW2VXtQ5ZiPf3-d4JA-ILSVv-HHzsLmj4oZybtCKrMbtVG4zHpiSVVsq-Mz7DFzqi7fPElEORabgJCTVJBpcuCjrnyGpMoNwRkKaTIgxLgmZFkjNgotQhgbVTPNWgqUjR20dACjLiFqwbruChsRbLgKMTbeMNp_gZaB22-s61nk3P__JNWDRGYgtWUKbMyqJ3JA2sSpggjcdClz-9VDAhBL7Gy-YkNMjFJY9_f0Adz-AvhguJwO9_zOQetDSGrJu7YlxAEPa5bbW_l514ZLhsjSL_wQaubPgKQszZHqoANNcjfAFbg3XtHeDK582dVaNbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین  به اهدافی در چهار منطقه روسیه حمله کرد که حملات ساراتوف تایید شده‌ترین و چشمگیرترین آنها بود.
مرکز لجستیک عظیم اوزون در ساراتوف (با بیش از ۱۰۰۰۰۰ متر مربع مساحت، بیش از ۳۰ میلیون قلم کالا ذخیره شده، تا ۹۰۰ هزار سفارش در روز).
طبق گزارش‌ها، پالایشگاه نفت ساراتوف (روس‌نفت، که قبلاً بارها هدف قرار گرفته بود) نیز آتش گرفت.
در ولگوگراد، فرماندار تایید کرد که آوار به یک مرکز صنعتی و یک ساختمان آپارتمانی برخورد کرده است.
منابع اوکراینی می‌گویند که هدف صنعتی، پالایشگاه ولگوگراد لوک‌اویل بوده است.
برخی ادعا می‌کنند که از موشک‌های کروز در کنار پهپادها استفاده شده است.
انفجارهایی در انگلس (محل پایگاه بمب‌افکن‌های استراتژیک روسیه) گزارش شده است، اما هنوز هیچ اصابت تایید شده‌ای به فرودگاه وجود ندارد.
بنا به گزارش‌ها، منطقه بندری کاسپیسک/داغستان نیز هدف قرار گرفته است - پس از حمله تایید شده شب گذشته به بندر ماخاچکالا.
@News_Hut</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/71533" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71532">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/news_hut/71532" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71531">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSWR8pwup2w9baJFdEILpUSt6j0G9gYMhCIoRIq6nxAYTNwQQuwtuWgV5A9zoi4EibyMMV5tC0NoM_HoO1T3BTCE0-E2mrYrtXHh1cKShWUbAKIVI5JRumpmrH_jvFFHawLyouDIl_8QUt0_99rJxbTiJx4E89yG_zq2NKO0RQgs15RDyhIV6ncZLQyyebrVOGyW7jIoQkHT8EZZ7K2iV8XN2RKAYkF087G0jUlS3nA7c4t25_Yk0FZte8eVU-lXfXsOqBVdgZCGMcb0wcKC1R0u1_KsVrrkUbaF8BnIjj1Ck59GUGUulmKd60d9bcNzW3Pmn-lgykuciKKFE7csjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/news_hut/71531" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71530">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554b629d89.mp4?token=rJ8ws2h0OoqP9hw5a8cfmVA2H8E7aVLVfGm-ByV7h7QgfWXXGGz2-dPb935EKIU64SQ-EUyWi_QkYFWmS_ek63KR-5SB3vdPvRrfDwOWXt4wNf1d8w3jF0FVb8aYV44V7T0uGp1VUIJr6MrLvYWZ9TSbJREDfdAGpZd-ByYKn4vVfMrI4oo7_j_ommMe5NFEpU6ln2oaD2-7ce5W-R11-t0dq1X-ymv9wYMmGb1LDE_hrSgowbFTuJee4bE7T9XD_sVZmv8Ihv2oc5lvIBw8uHB3yeRKkLU3g20VNhy42TiEJfw4wdyQsq4XGTE5pDCApooJCgqrToEv9L2WEGmMH3Qns49LrHnQcXDhfOo8B8qWBmQqZHZ0rO8lS4xaEzmu1wKjTX1nqZCYZ12Vp-UXxskvFJ12uNBwwxQjOclYcEakbAgG-zcnokgu07Ej0c9ubVoOasSwrpuvkom3uU8dqZRE3dfTvccVnHtfY3DP0ujps5IoFTLzP5EORfOuU4t6yxWFNdkfPdmeejEHx6Cf3vjj-csIAPlqUh2YJBp2ITmgW2Vz1eyVvHOv3csIi9vovuIgCf3lOyU2aycZ4FvwUg343lZgCyjDanHlZ7JenqM8nV_PpnQlwIV-F4r2ATMEtX9JQdYX5_JvisiDVHYwxFKwLpInwoIRAkRmRkP0_oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554b629d89.mp4?token=rJ8ws2h0OoqP9hw5a8cfmVA2H8E7aVLVfGm-ByV7h7QgfWXXGGz2-dPb935EKIU64SQ-EUyWi_QkYFWmS_ek63KR-5SB3vdPvRrfDwOWXt4wNf1d8w3jF0FVb8aYV44V7T0uGp1VUIJr6MrLvYWZ9TSbJREDfdAGpZd-ByYKn4vVfMrI4oo7_j_ommMe5NFEpU6ln2oaD2-7ce5W-R11-t0dq1X-ymv9wYMmGb1LDE_hrSgowbFTuJee4bE7T9XD_sVZmv8Ihv2oc5lvIBw8uHB3yeRKkLU3g20VNhy42TiEJfw4wdyQsq4XGTE5pDCApooJCgqrToEv9L2WEGmMH3Qns49LrHnQcXDhfOo8B8qWBmQqZHZ0rO8lS4xaEzmu1wKjTX1nqZCYZ12Vp-UXxskvFJ12uNBwwxQjOclYcEakbAgG-zcnokgu07Ej0c9ubVoOasSwrpuvkom3uU8dqZRE3dfTvccVnHtfY3DP0ujps5IoFTLzP5EORfOuU4t6yxWFNdkfPdmeejEHx6Cf3vjj-csIAPlqUh2YJBp2ITmgW2Vz1eyVvHOv3csIi9vovuIgCf3lOyU2aycZ4FvwUg343lZgCyjDanHlZ7JenqM8nV_PpnQlwIV-F4r2ATMEtX9JQdYX5_JvisiDVHYwxFKwLpInwoIRAkRmRkP0_oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پست جدید هیچکس (سروش لشگری ) توی اینستاگرام که وایرال شده؛
«هنو به یادتم»
@News_Hut</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/news_hut/71530" target="_blank">📅 18:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71528">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=usW4mDcrWQvbNLvtbFC4O7HJPK8f_8Zez61nj9SOu86gBSqxaXIuAqzNVYDMQrN6QNu6A_osDqjP2Yz8_f-S0llKC-asV0KZJiF3PPRDFGUVMiH3E7W97xL1V_2vszV8vutiSDiB5ykT6aIhCNst0K2M10yzv73YwlTNVjZDbyGAENhw6bop6PMdtEqJjf9Utw3m0Uu5hd7L8ReZupTW6N8_ljL3Uz43X1UR5JtY2quADL8hVR1MgLa4v2tsFCYpOkio03PZCyz9dMTm4JNRmNKrK1pyVeSWz722KoCcxffDsp8-ixDWgXSdQAYmnWbJIxOw4t5oEJ3APGRA9wq1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=usW4mDcrWQvbNLvtbFC4O7HJPK8f_8Zez61nj9SOu86gBSqxaXIuAqzNVYDMQrN6QNu6A_osDqjP2Yz8_f-S0llKC-asV0KZJiF3PPRDFGUVMiH3E7W97xL1V_2vszV8vutiSDiB5ykT6aIhCNst0K2M10yzv73YwlTNVjZDbyGAENhw6bop6PMdtEqJjf9Utw3m0Uu5hd7L8ReZupTW6N8_ljL3Uz43X1UR5JtY2quADL8hVR1MgLa4v2tsFCYpOkio03PZCyz9dMTm4JNRmNKrK1pyVeSWz722KoCcxffDsp8-ixDWgXSdQAYmnWbJIxOw4t5oEJ3APGRA9wq1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعار «مرگ بر روحانی» در تجمع شبانه عرزشی‌ها
:
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/71528" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71527">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=qPahvCUSqjpooTMom5B-FdEFqW-2gevF5hGwt5i9auiM_447iQd562pDuIMq53LIS4oYCCL42IHbwg1zLxkn4PxBp95vPP0_xkdNmrX9pQToAQ9hqNAWZO96WnCdLktANXuqkO8QD6pUua7dWrnUbhLMxddogJ8FkFhWN9kt24alAw_tZQRTW2KvgdvLfX3g4hlvG99Mss0o1sEEipbHsCAO-Ot3KJczq0MbtpNBcyajlth1eE26MwQ39za6aDzvWXZPGsFY0RqM6Gi4xFdOVVyO73oFnneP0LfBPCRuR0_zqBPMr0qns9CJPB6Ccr4FlA_uQaKo1sgE3ELTzZ3IZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=qPahvCUSqjpooTMom5B-FdEFqW-2gevF5hGwt5i9auiM_447iQd562pDuIMq53LIS4oYCCL42IHbwg1zLxkn4PxBp95vPP0_xkdNmrX9pQToAQ9hqNAWZO96WnCdLktANXuqkO8QD6pUua7dWrnUbhLMxddogJ8FkFhWN9kt24alAw_tZQRTW2KvgdvLfX3g4hlvG99Mss0o1sEEipbHsCAO-Ot3KJczq0MbtpNBcyajlth1eE26MwQ39za6aDzvWXZPGsFY0RqM6Gi4xFdOVVyO73oFnneP0LfBPCRuR0_zqBPMr0qns9CJPB6Ccr4FlA_uQaKo1sgE3ELTzZ3IZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
یک شهروند ایرانی با انتشار ویدیویی اعلام کرد ترکیه مرزش رو به روی ایرانیا بسته و اجازه عبور و مرور رو نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/71527" target="_blank">📅 17:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71526">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=tDdP_Ekrkqw_9ucqT2oYNN_TjH_XExS5v-Pj_FPvj9ghYm76aBUddVk40SvnWLZ0WnlUMyyWgfPhU7l7Z9DxmdoUjGXT6lVi1WbOC6TK1A8IT0a543GAunce2CW-74aPD8mZfkW8f7H7U3sSeBo6p-pu7rPo1322eVq5bwwLFkKNAh16ln32m4jOz-GxPmYvqTzz1yQXDjNG_qMzMgvePFkyOldu4D4NVZXW5ulciySVTIcShpaEo5fMqVgZNLmKwoSEWmkEaXInuL3A27PfIOxWGKJpu1H7GP5hvIX3dIUrtAInDEYd_Y1tl_7XrzRumfbWNUAJTuVvGyxLrG1T1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=tDdP_Ekrkqw_9ucqT2oYNN_TjH_XExS5v-Pj_FPvj9ghYm76aBUddVk40SvnWLZ0WnlUMyyWgfPhU7l7Z9DxmdoUjGXT6lVi1WbOC6TK1A8IT0a543GAunce2CW-74aPD8mZfkW8f7H7U3sSeBo6p-pu7rPo1322eVq5bwwLFkKNAh16ln32m4jOz-GxPmYvqTzz1yQXDjNG_qMzMgvePFkyOldu4D4NVZXW5ulciySVTIcShpaEo5fMqVgZNLmKwoSEWmkEaXInuL3A27PfIOxWGKJpu1H7GP5hvIX3dIUrtAInDEYd_Y1tl_7XrzRumfbWNUAJTuVvGyxLrG1T1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از عشق و ابراز علاقه زیبای یه پیرمرد و پیرزن ایرانی توی پارک خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71526" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71525">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=iUGpLS3Znua01q6C3F759PaNJi2j22scl3AXPURS9GuMp5AAAovk1dKtJpbdR-Qi805jg8s_Aoi3OO-vvvekd3JyL_rMDV28KcVuaVjydNM6CAfBCopA4SnzOaG8H-XPZ_D7iSUCIIYeipzl0PLg6fOkcDduX9BqO1frLXBBD40qyyQVrdKSIwzOI_NYP6mUzamS8bGGVs70Nvc13Wv0_2uLzEMkELPLMVbFIXa84ZjZ4WDT_Ph8lszAb4QaLacAKpFgo3I8XgOWjRIRyBu-OUbS7gqI8W3ISxy7v7xZdfAlpJAc6u7Sg_M2hmOXL4HD7JvZBzAadpcl9tborzb4pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=iUGpLS3Znua01q6C3F759PaNJi2j22scl3AXPURS9GuMp5AAAovk1dKtJpbdR-Qi805jg8s_Aoi3OO-vvvekd3JyL_rMDV28KcVuaVjydNM6CAfBCopA4SnzOaG8H-XPZ_D7iSUCIIYeipzl0PLg6fOkcDduX9BqO1frLXBBD40qyyQVrdKSIwzOI_NYP6mUzamS8bGGVs70Nvc13Wv0_2uLzEMkELPLMVbFIXa84ZjZ4WDT_Ph8lszAb4QaLacAKpFgo3I8XgOWjRIRyBu-OUbS7gqI8W3ISxy7v7xZdfAlpJAc6u7Sg_M2hmOXL4HD7JvZBzAadpcl9tborzb4pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
چرا پزشکیان ۱۷ شهریور که تولد مجتبی خامنه‌ای هست بنزین رو گرون کرد؟ چرا روز تولد خودش گرون نکرد؟
میخواین همه تقصیرات رو بندازین گردن امامِ ما یعنی مجتبی؟ کور خوندین!
ما دیگه فریب بازی‌هاتون رو نمی‌خوریم که میخواین علیه رهبرمون کودتا کنین.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71525" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71523">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiHwUTmtx9wTHrTXfmwoVM-NkAhi2hS1c-b74w_bwjzi1NuGBmeaFtcykvJlD29UHCQmQJ3h4bK09lb0Q1eB5DDbZDL6IN9kn4qZ7-vSxuQSwc75yYcdUxDjNASpZDWsdkgaOtVJkVqiztu9NbEyjo59uqfjsdjAj1hKO2_NsuchrU3Y_m-XfvpQxGp7NQuppAZnpO-VeySygRMEIwfrPq_M8URCEo3NU85zY2Sk8BHKkOrJHBDoCZM63EBOuFxTmgl-xgfOWG2zx0DdSqE3G-DEwu55q_opJHmKsmD06mCAVMYnVQK8EtdvX69CoO55B33IGtntr-TIRQDtpFcr4kgMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiHwUTmtx9wTHrTXfmwoVM-NkAhi2hS1c-b74w_bwjzi1NuGBmeaFtcykvJlD29UHCQmQJ3h4bK09lb0Q1eB5DDbZDL6IN9kn4qZ7-vSxuQSwc75yYcdUxDjNASpZDWsdkgaOtVJkVqiztu9NbEyjo59uqfjsdjAj1hKO2_NsuchrU3Y_m-XfvpQxGp7NQuppAZnpO-VeySygRMEIwfrPq_M8URCEo3NU85zY2Sk8BHKkOrJHBDoCZM63EBOuFxTmgl-xgfOWG2zx0DdSqE3G-DEwu55q_opJHmKsmD06mCAVMYnVQK8EtdvX69CoO55B33IGtntr-TIRQDtpFcr4kgMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره ایران:
«ما کنترل تنگه هرمز را به دست گرفتیم. تمام مین‌ها را پاکسازی کردیم.
من گفتم: «خب، پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟»
گفتند: «قربان، این مین‌روب‌ها زیر آب هستند. آنها همیشه در زیر آب فعالیت می‌کنند.»
گفتم: «چرا این کار را می‌کنید؟»
گفتند: «خب، به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه هم خصومت و درگیری زیادی وجود دارد.»
یعنی اگر در یک آبراه مین وجود داشته باشد، معمولاً افرادی هم هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
حالا دیگر هیچ مینی آنجا نیست، هیچ چیز دیگری هم نیست. و اگر ببینیم آنها [دوباره مین‌گذاری می‌کنند/اقدام به این کار می‌کنند]، آن‌وقت می‌بینید چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71523" target="_blank">📅 15:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71522">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=O_-rAhY26j4zX4JpW2icL67x8tZ9rKtKB0NpI-Dltpqpc0cpD-VNAds2yBkYgP4PZmSy59CM2hYmUIOSc_5jeJDY5aV4SLLFQ2OfLQzOdWgflJhyryaYeLPMavc7ZGy1MJazIxlzGzM3StXuH_hRg-XZpLFkG4j6WLZ5kkG99iDtENYqIwj1yDtU2RgNzNz83eJ859JMAIhuu8Uu2Nm7KTV6u9yY4S8MNWRMYm_Hsr56zLFtya4mE2ngcNzgWndWqRrpZpo7osO9Sq5wh6bueQrKa6bnoB2osyJ65PyMNAaqO3jkJlWmr7RjjiKYeAd5aKrnmY9yReNjPQsx0qmWZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=O_-rAhY26j4zX4JpW2icL67x8tZ9rKtKB0NpI-Dltpqpc0cpD-VNAds2yBkYgP4PZmSy59CM2hYmUIOSc_5jeJDY5aV4SLLFQ2OfLQzOdWgflJhyryaYeLPMavc7ZGy1MJazIxlzGzM3StXuH_hRg-XZpLFkG4j6WLZ5kkG99iDtENYqIwj1yDtU2RgNzNz83eJ859JMAIhuu8Uu2Nm7KTV6u9yY4S8MNWRMYm_Hsr56zLFtya4mE2ngcNzgWndWqRrpZpo7osO9Sq5wh6bueQrKa6bnoB2osyJ65PyMNAaqO3jkJlWmr7RjjiKYeAd5aKrnmY9yReNjPQsx0qmWZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هادی چوپان :
هانی رامبد از پشت بهم خنجر زد.
گفت پشت جمهوری اسلامی نباید باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71522" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71521">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh77uiDscwS5cFtxaX2vW6VHB4BwhI3-BY_7Pcnv4MHZO8HO3YKOp8hj-RQblogz3TjPXUe4GO9LG36H2W_n1x_LUqULZmBwVkiJVuYEHDM6FCFw82xtjt5CSiRbZKHuLFxxcTLoznjdrMHRtgtaFtLPgPdp0R9_Tr9qkuPQJg2HWAih2EIhrnmA-RurdL6tVxz3M2R1LVGfNNDjujKanHIhKo5u5bcSTCpYowa5Om8K6DrgF24d9ZrW8c9_wbRMT_r8VRldq66MSzXj3aA8iZWMDaqkSZF5sqpXLRQz6m7fLJGWhjPy08QILLmJTzLBOJdIn4Ntktimx87AwltJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
پزشکیان در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان رئیس امارات متحده عربی دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71521" target="_blank">📅 14:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71520">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=nhn5xTtLIk7S8wQqVakpL0gX1Aggg_STFJUuij1h8toRkTvHep_AB_kGZd6Z_9cI2UtAi-m2kfFxTmjuicyPZhbgtdO7qeYi0QUOicJ_LPFe959c6IR9oMV1_sf1gnf3jsyCNBz9J3kBUMrRkdlV3dNn5szbtXAadRqEiildySJNTeNKWTYNcH9eozoREmpZg2vhtBjqP-rHs1rPVQGHnThmfyKWlqIVfAyFcWM_8sF9cRdGdUEFfPnk5hqA4hF3M2gzpAsIpNznIgwq1xRavgFGHQnuLlfwiGnGOkqzuY2iUdDZoX8AX1oKOs5vM47jbJltqQP6NX-AA-9tHjB_vogp9fHqruN92u6IGJsy-0ZSW1Ctb2LX1jhuIhiQFnqlNPjn2TRGvC_Q0gAxKyPo3jEYcCMxqt5zjtQ2BKg8tjvl0Rcs5vzrgNuVQ1d2OA6hR6Pd4SNLLqUSODhzAfKsEE9ulSWisrqGudvFYIUdMSpvdfv4CLXdrv_pSfs-C_P0aHrumXF_JuKdZrRk1RPr_Dmp7nkfNYLUX1nKbvbME0cbn7xr9eaBNKJntsuVjcEXP1OpJusbZj2q7bKHFTIr58bVEqqERhR8-PkqarbywjPB3fQVUIRJtuiaAVfIpsItjLAqXfnB_mKlWBTXQpwRHz6qOTWvvPrhyy8ViiLMMKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=nhn5xTtLIk7S8wQqVakpL0gX1Aggg_STFJUuij1h8toRkTvHep_AB_kGZd6Z_9cI2UtAi-m2kfFxTmjuicyPZhbgtdO7qeYi0QUOicJ_LPFe959c6IR9oMV1_sf1gnf3jsyCNBz9J3kBUMrRkdlV3dNn5szbtXAadRqEiildySJNTeNKWTYNcH9eozoREmpZg2vhtBjqP-rHs1rPVQGHnThmfyKWlqIVfAyFcWM_8sF9cRdGdUEFfPnk5hqA4hF3M2gzpAsIpNznIgwq1xRavgFGHQnuLlfwiGnGOkqzuY2iUdDZoX8AX1oKOs5vM47jbJltqQP6NX-AA-9tHjB_vogp9fHqruN92u6IGJsy-0ZSW1Ctb2LX1jhuIhiQFnqlNPjn2TRGvC_Q0gAxKyPo3jEYcCMxqt5zjtQ2BKg8tjvl0Rcs5vzrgNuVQ1d2OA6hR6Pd4SNLLqUSODhzAfKsEE9ulSWisrqGudvFYIUdMSpvdfv4CLXdrv_pSfs-C_P0aHrumXF_JuKdZrRk1RPr_Dmp7nkfNYLUX1nKbvbME0cbn7xr9eaBNKJntsuVjcEXP1OpJusbZj2q7bKHFTIr58bVEqqERhR8-PkqarbywjPB3fQVUIRJtuiaAVfIpsItjLAqXfnB_mKlWBTXQpwRHz6qOTWvvPrhyy8ViiLMMKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
ببینید، ما کار فوق‌العاده‌ای انجام دادیم. می‌دانید، ما آنجا را تحت کنترل گرفتیم. ما واقعاً با اقتدار کامل بر «تنگه هرمز» مسلط شدیم و هیچ‌کس متوجه این ماجرا نشد.
ما کنترل بسیار قدرتمندی بر آن داشتیم.
ما یک محاصره دریایی اعمال کردیم که واقعاً بی‌نظیر بود.
ما تعداد زیادی از شناورها را بیرون می‌کشیم؛ به‌طور میانگین روزی ۲۵ شناور را خارج می‌کنیم که بیشترشان در شب انجام می‌شود.
اما به‌طور متوسط، هر روز حدود ۲۵ شناور را از کار می‌اندازیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71520" target="_blank">📅 13:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71519">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، جنگ در ایران چه زمانی پایان می‌یابد؟
🇺🇸
ترامپ:
فکر می‌کنم خیلی زود. گمان می‌کنم احتمالاً درست پس از پایان دوره [فعلی انتخابات] باشد. آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا وضعیت انتخابات را پیچیده سازند. اما فکر می‌کنم مردم متوجه ماجرا هستند، چرا که ایران نمی‌تواند سلاح هسته‌ای داشته باشد. موضوع بسیار ساده‌ای است؛ مسئله خیلی ساده‌ای است. ایران نباید چنین سلاحی داشته باشد. آن‌ها تنها دو هفته با دستیابی به سلاح هسته‌ای فاصله داشتند.
اگر این کار را نکرده بودند [و جلوی آن‌ها گرفته نمی‌شد]، اسرائیل را نابود می‌کردند، خاورمیانه را به آتش می‌کشیدند و به برخی شهرهای اروپا — و حتی فراتر از شهرها — حمله می‌کردند. و احتمالاً پیش از آنکه ما بتوانیم آتش را خاموش کنیم، به خود ما هم حمله می‌کردند. اما آن‌ها نباید سلاح هسته‌ای داشته باشند. با این حال، می‌گویم که [این اتفاق] به‌زودی رخ خواهد داد و قیمت نفت به‌شدت سقوط خواهد کرد. وقتی آن اتفاق بیفتد، قیمت نفت به‌شدت پایین خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71519" target="_blank">📅 13:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71518">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⏺
🇮🇷
قرارگاه قدس نیروی زمینی سپاه:
درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به هلاکت رسیدند؛ همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از مخفیگاه این تیم کشف گردید.
در این عملیات که تا پیش از ظهر امروز ادامه داشت ۳ نفر از پاسداران گمنام امام زمان(عج) نیز به شهادت رسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71518" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71517">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=HAQbzVITYPQPs90yV0PbL9NHxxZebMpzQxzZIwikWKa-lzKwvO_EpJnatr9K8_ptDgyp3oXLNGukxj72RlqvbsgjxLingXQOFAqDc-18JxdlXqHgvqhJvyf7eaEqIh9w-BWh5xzMawv1E6Wep4qrZZWlQZOsqNERuOtJN3InJuMBu6HOXYezkUAHVKkErcR_GnfGsg6MSBHxZtC-ZsZFHqoR0skZhinGWzyrDV687CzTxwXWR9Pr_rQ2cf1rgHi3wfIhyOHXyikpb98qEBuLGcfL28jkRn31NF3nWidALH5LtWt3cPdohhkZE8W5A3JxJFrMbZcxvy15KPPEJTVj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=HAQbzVITYPQPs90yV0PbL9NHxxZebMpzQxzZIwikWKa-lzKwvO_EpJnatr9K8_ptDgyp3oXLNGukxj72RlqvbsgjxLingXQOFAqDc-18JxdlXqHgvqhJvyf7eaEqIh9w-BWh5xzMawv1E6Wep4qrZZWlQZOsqNERuOtJN3InJuMBu6HOXYezkUAHVKkErcR_GnfGsg6MSBHxZtC-ZsZFHqoR0skZhinGWzyrDV687CzTxwXWR9Pr_rQ2cf1rgHi3wfIhyOHXyikpb98qEBuLGcfL28jkRn31NF3nWidALH5LtWt3cPdohhkZE8W5A3JxJFrMbZcxvy15KPPEJTVj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران مسئول حمله به خط لوله «شرق-غرب» است؟
و به نظر شما عربستان سعودی چه کاری می‌تواند انجام دهد؟
🇺🇸
ترامپ:
خب، فکر می‌کنم همین‌طور است. احتمالاً همین‌طور است.
آن‌ها در حال حاضر در وضعیت آماده‌باش و هوشیاری کامل هستند، اما فکر می‌کنم مسئول آن هستند.
آن‌ها مدتی است که کنترل آن را در دست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71517" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71516">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=KZcluJn6pHMRgV-77atGb8CBXA9ac9nZ_rE7iCL7ng0yPXKK5qEYisga6VWSqWYwN-LQOrF8BqGWoU4aZz8lzTs9GqGFJZ0LZjW9eGe5F1ywRZ09q3jru8XXC9WtneaRdDjop1s9NZY828GJTtoMa5h9d8DExs_vg7E993MGYe8H2yxCJBPj5zvzrQWR2aXLNmxsb9PeqxkvRS7fsgDUspxLZDcKTG651mmpMEWM83NTpYyWwNKwa2DGQ976Ejy_lZWjJNgz2JDaVVH6nLosiWa_xEkkp6w5qp28q0F_ZtCP3PI2Nhov8w79VHTiXVd_Y_EO2_sxAh0OTv4jfFE5RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=KZcluJn6pHMRgV-77atGb8CBXA9ac9nZ_rE7iCL7ng0yPXKK5qEYisga6VWSqWYwN-LQOrF8BqGWoU4aZz8lzTs9GqGFJZ0LZjW9eGe5F1ywRZ09q3jru8XXC9WtneaRdDjop1s9NZY828GJTtoMa5h9d8DExs_vg7E993MGYe8H2yxCJBPj5zvzrQWR2aXLNmxsb9PeqxkvRS7fsgDUspxLZDcKTG651mmpMEWM83NTpYyWwNKwa2DGQ976Ejy_lZWjJNgz2JDaVVH6nLosiWa_xEkkp6w5qp28q0F_ZtCP3PI2Nhov8w79VHTiXVd_Y_EO2_sxAh0OTv4jfFE5RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
این رستوران توی تهرانه
نوشته : هیچی کتلت بی بی نمیشه:)))
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71516" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71515">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=AXUUeMxVX8FCeWpMGk6tMYaLwo-GrAfRf-U9et-w7Ozm1jBX-EUNvjCOtUCTwbu89YeMqIieW8CujlJ-yBfRbgbrc6rSq0oO5U6QuqYxw1WN396IgOlX7fDgQARFGv44GOb_1PkLFAOUaX8XZ_8vpd8jA7PizprmEF8BY2VL-5JJ-5sGggL-sPRcqzDzfQbrlxaPEB8TgWnVaPnQqS1TCjb3qk3duK_1BV5vjkvcyjDs7Jx0HxG0gt7CHIRDmxM2zEPmf93VZ2UkLG9IVrNHZk998krN2R_YJ-uOz8SwO-r078GDicZytugC8gsFCD1ChkCijp9bri3CYkiYsyy6LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=AXUUeMxVX8FCeWpMGk6tMYaLwo-GrAfRf-U9et-w7Ozm1jBX-EUNvjCOtUCTwbu89YeMqIieW8CujlJ-yBfRbgbrc6rSq0oO5U6QuqYxw1WN396IgOlX7fDgQARFGv44GOb_1PkLFAOUaX8XZ_8vpd8jA7PizprmEF8BY2VL-5JJ-5sGggL-sPRcqzDzfQbrlxaPEB8TgWnVaPnQqS1TCjb3qk3duK_1BV5vjkvcyjDs7Jx0HxG0gt7CHIRDmxM2zEPmf93VZ2UkLG9IVrNHZk998krN2R_YJ-uOz8SwO-r078GDicZytugC8gsFCD1ChkCijp9bri3CYkiYsyy6LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
🇺🇸
پست جدید دونالد ترامپ در تروث سوشال:
با این رئیس جمهور بازی نکنید، زیرا نتیجه خوبی نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71515" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71514">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsXG0WlGe3znJbIqCF_brXEoPVyBT2lzLNyxUd8gsnPJZ-cICprOAoYb7OJLvlyRKQQwQWDoIS90bf2z3vyUdKFI9_12q8FbYpFL4SV5Sha-N_Nd2yIzio5Y0WTE-wxmdfe9Qod5bGTG5iHotjVEV67DhPTx6x5euwub1XvY8RPGaXqGkbC0gjR0Ug1dHqzjYicNc1JCo20aF3_73H72cBJt_E2d8SxiKbaEyWmiaqnUZY4N9e2qZf09GOU-MIsgZRvlJUttZLAuXX1ut0xGL6e3_EXAggbPlCphKEjor4KwFN_AFmag-Vk1S5JnvhBpoBfd8WOe1bXS3vVoROriXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها تو راهه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71514" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71513">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71513" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrDuqbNKLXhqc_lrNr75EoRL8zoozDnj40LIESNF1I3yOIGihs8UG_GOWHcmna531c8Dc7HZdc8xScUrJ15MthMrIRntZiVaOVhzV1RSdv-JC3k9aWKE1w5X6Bz33IDy5eCjITCxS7WlsjGhqRmoHNcBfnBhOw42Oe_ME8ltCc01MkNu7239lW1_MCWfpPdUF4buJyqlPM3amg5aqGK3diov9bpgnTJargefKsJv0Z4w5qoYNIOikCWIixFlhT4ROakV4cUbE-BbDy6TjJ2Fl3WOwK3vW95TujRHMDMZnzNl2UAIfOdTKVxxei8_suOrUOLn6mXF4PqOevaKOiWp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71512" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇮🇷
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان: محل تجمع اعضای «گروهک‌های معاند و تروریستی» شناسایی شده و نیروهای امنیتی در یک عملیات غافلگیرانه به آن ضربه زده‌اند.
در گزارش‌های اولیه، نام جیش‌العدل/جیش‌الظلم به‌عنوان عامل درگیری امروز به کار برده شده که هنوز به صورت رسمی تایید نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71511" target="_blank">📅 12:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=e_a2TXjA5kputxgMo6ZOy7UcC4Q4xP86MGYwvXDggqKvyzN80ps0knTWG6EVW9AZKPK4bZP8gZgCU-aVNRpssg_0vp1lkeKpZ0t8TY-nvuDDIdf0YwP07l538-1taw9ixd8KEJ0uwZ1bjdyVJizM-CaGiP2Jk-R2mzW4hmHs3OmVUQ7MsdnuUt0NSx0kINI_cV2wpN95oq7NDR9QtbwF1uK9zkFdyTYhX_gijG8F5fU-cMxKh4cbGOjbA1cO7G4kB5f8yz0rigSdi8SeyVw_2X9xEaD1PlKTJPq4976EaUP97FRfawTNfFFde0cJg0JlVHaT_zw-p5JgOh6hdSS6Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=e_a2TXjA5kputxgMo6ZOy7UcC4Q4xP86MGYwvXDggqKvyzN80ps0knTWG6EVW9AZKPK4bZP8gZgCU-aVNRpssg_0vp1lkeKpZ0t8TY-nvuDDIdf0YwP07l538-1taw9ixd8KEJ0uwZ1bjdyVJizM-CaGiP2Jk-R2mzW4hmHs3OmVUQ7MsdnuUt0NSx0kINI_cV2wpN95oq7NDR9QtbwF1uK9zkFdyTYhX_gijG8F5fU-cMxKh4cbGOjbA1cO7G4kB5f8yz0rigSdi8SeyVw_2X9xEaD1PlKTJPq4976EaUP97FRfawTNfFFde0cJg0JlVHaT_zw-p5JgOh6hdSS6Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درگیری های بی سابقه نیروهای جمهوری اسلامی و نیروهای مسلح در سراوان سیستان بلوچستان
ویدیو ها مربوط به چند ساعت پیش
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71504" target="_blank">📅 11:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71503">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:  دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود. این تصمیم شامل تردد مسافران و همچنین جابه‌جایی…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71503" target="_blank">📅 11:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71498">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=gzXkjx259SgSV9tABWZdtKPB-MEOrmjFakibXeTIdysti-Ao9SiZh-lm6xoPVunsZmKhQ6TxcsUhD-iqynqOQ1L6Ue_O3u1gRMTCuzRl8B1WEQ2hOuOK07Sa-Xz3w--OouuF_wIj_EecOEwCPoNWzJcLxUdaq9Siy-667iSrEAfa6RIqOCxYYEo6zyLwt2Uu_rCnAwp7PmdSClsh00lZwSjUbKGcsa3CeFwaTvWWMc-SwTnoDRXFc3xhClGUhI_9B-pRfz92WcoVBMg13B7hWj9bOfJ3dT8BUN2agZMd6q3BqfAG7U1g96hWi3zISrocigKgJFoMYazkS7Ql7Jugwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=gzXkjx259SgSV9tABWZdtKPB-MEOrmjFakibXeTIdysti-Ao9SiZh-lm6xoPVunsZmKhQ6TxcsUhD-iqynqOQ1L6Ue_O3u1gRMTCuzRl8B1WEQ2hOuOK07Sa-Xz3w--OouuF_wIj_EecOEwCPoNWzJcLxUdaq9Siy-667iSrEAfa6RIqOCxYYEo6zyLwt2Uu_rCnAwp7PmdSClsh00lZwSjUbKGcsa3CeFwaTvWWMc-SwTnoDRXFc3xhClGUhI_9B-pRfz92WcoVBMg13B7hWj9bOfJ3dT8BUN2agZMd6q3BqfAG7U1g96hWi3zISrocigKgJFoMYazkS7Ql7Jugwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر تهرانی بعد از اینکه با دوس دخترش کات کرد، رفته تمام اکسای دختره رو جمع کرده، واسش دسته جمعی آهنگ خوندن تا قشنگ دختره رو بسوزونه و عقده هاش رو خالی کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71498" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71497">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=IA9zrriYkZQ2e5AQ0dvjWtlXeYVndl5jEZKqVlIHH2rCRhF5GWAFaIsNVO7vA5fmUsFJ_qaS9j14vx5wEj0wh11Z2OdNxUMxtnmwvFkfB9zhSJxWi-LzNCVS3xZWF7V05bJdUbq0WBPArd43I-NBfc3EwWxSwJ2lBIktEVJ3ZBRYb1kQAB_u2LKEFNKk9KKeuW16fEVYsOXiziuRjzAi-6W_OZqiqe07bB73gO3Xwrr9jsaM393mKMI_w7PfaZ9VlY9pQliknhy0sKdA4fJKGn0Cks5ASY-wwzmIxGE0ytu-jpivE5CHb-mH0Do_UrPIhTudnTZB3y4Fb9Tv7C_WFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=IA9zrriYkZQ2e5AQ0dvjWtlXeYVndl5jEZKqVlIHH2rCRhF5GWAFaIsNVO7vA5fmUsFJ_qaS9j14vx5wEj0wh11Z2OdNxUMxtnmwvFkfB9zhSJxWi-LzNCVS3xZWF7V05bJdUbq0WBPArd43I-NBfc3EwWxSwJ2lBIktEVJ3ZBRYb1kQAB_u2LKEFNKk9KKeuW16fEVYsOXiziuRjzAi-6W_OZqiqe07bB73gO3Xwrr9jsaM393mKMI_w7PfaZ9VlY9pQliknhy0sKdA4fJKGn0Cks5ASY-wwzmIxGE0ytu-jpivE5CHb-mH0Do_UrPIhTudnTZB3y4Fb9Tv7C_WFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
یه گزارشگر تو شهر وان ترکیه طی یه گزارشِ خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده که حسابی وایرال شده؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71497" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71495">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=Uxnb51uYJVlRK1DRd4RMbLem4s8pGWkLCTG0jsqaLdkKbCHSqBpe-cyZrENcZRBalm6NBu9jFF1dEN70ikseXD-6nAWPPaaK1cyVPe_aPsVRtDT25wo5lfElr0wJBzjagXCWI1xPMza3B6GjOoFDKClmS0301aifk47oKE72mz1IE0WRVnHShIc-ldWrOJSuMyj--btBbsOXrIbqHXAFHhFu6i4fiS_K6oLUiNd-dY7RE-0CN41h8bORbGJeeilfB36Pkkugfcj3Aks6KRCkP8OdJb2UQf5hntKBriMZ9x6NiTEg5_-0s_BLW8spxTCQnQyUhduIL_q-kVcCSiWwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=Uxnb51uYJVlRK1DRd4RMbLem4s8pGWkLCTG0jsqaLdkKbCHSqBpe-cyZrENcZRBalm6NBu9jFF1dEN70ikseXD-6nAWPPaaK1cyVPe_aPsVRtDT25wo5lfElr0wJBzjagXCWI1xPMza3B6GjOoFDKClmS0301aifk47oKE72mz1IE0WRVnHShIc-ldWrOJSuMyj--btBbsOXrIbqHXAFHhFu6i4fiS_K6oLUiNd-dY7RE-0CN41h8bORbGJeeilfB36Pkkugfcj3Aks6KRCkP8OdJb2UQf5hntKBriMZ9x6NiTEg5_-0s_BLW8spxTCQnQyUhduIL_q-kVcCSiWwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده و پشم ریزون از کنسرت تیلور سوییفت؛
خودتون ببینید به چه دلیل وایرال شده
😏
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71495" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71494">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
خورلسوخ، رئیس‌جمهور ۵۸ ساله مغولستان، هنگام بازدید از یک یگان نظامی، حرکت پرس سینه را با وزنه ۱۰۰ کیلوگرمی در ۲۰ تکرار انجام داد.
او که پیش‌تر افسر ارتش بوده، نامش در لغت به معنای «تبر برنزی» است، باشگاه هارلی-دیویدسون مغولستان را تأسیس کرده و در یک گروه موسیقی گیتار می‌نوازد؛ او همچنین جانشین «باتولگا» شده است که خود قهرمان جهان در رشته سامبو بود.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71494" target="_blank">📅 09:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71493">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oXLinVcZbyZVgwtMiP55Okrtg0cEnUvyikaDz0lM1HdCbIUpgZZc2Zw1vJIsrsDyMyyVAtTJl8LoIrGnFubAPX5jCRdgZO7Eya5eoGKbD5nbYPOGqVaCEC2Wm19mn_xERVoMAvB32f7KuKvrN3ens4INCA1VeZ5vip6x9tkMTdDvG6vf7LHJUKV_OvaiQgeGha89wAwZka4dC1r56--JsHuuANJELHK7BV5C1sPqdWADdegBUXTKyHKVGvb62pc_37X3Gj--Y3CShO16Yl9IpALUBLs7uN2Z_pC2UJjhggF7zAZ16CjEFJiYNGw0MrXTT-jX_EBIVGZzY0AqJ_V8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oXLinVcZbyZVgwtMiP55Okrtg0cEnUvyikaDz0lM1HdCbIUpgZZc2Zw1vJIsrsDyMyyVAtTJl8LoIrGnFubAPX5jCRdgZO7Eya5eoGKbD5nbYPOGqVaCEC2Wm19mn_xERVoMAvB32f7KuKvrN3ens4INCA1VeZ5vip6x9tkMTdDvG6vf7LHJUKV_OvaiQgeGha89wAwZka4dC1r56--JsHuuANJELHK7BV5C1sPqdWADdegBUXTKyHKVGvb62pc_37X3Gj--Y3CShO16Yl9IpALUBLs7uN2Z_pC2UJjhggF7zAZ16CjEFJiYNGw0MrXTT-jX_EBIVGZzY0AqJ_V8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی خطاب به ارزشی ها : انتقام خامنه‌ای رو امام زمان که ظهور کنه میگیره
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71493" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71492">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:
دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود.
این تصمیم شامل تردد مسافران و همچنین جابه‌جایی کالاها می‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71492" target="_blank">📅 07:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71491">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71491" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71490">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVMzAd4wSGjRJaHpN08c8w7YQnsN2-b0OGS8O2P0JxIOihaFls_y7MqXGzPqiHXtBx4F9QtC0t0qb2DBB0QMoHvztPDC9xNYuiKU1t7C_AUTZc0_0jXIOeFjCtJI0grCYyj_aRgTj9UsUodsOFVRnFQEu0FkRLP3Yli7HQbNvgaGRHhzYVpHxzRT58PMMuK1qp9TJFZ3HUz7iNGFYxo4VctbgZhkna3MpccbCGKgS0zljflIMX-GFqLsxQzEkUHxrcMy8HBSWeJ14My6Ar-g9fQ3J0yyIj0O57kaM7QhQoWASy479YOc10rTy_Ur6PqecovXRiTGrciWWuymrMDcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71490" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71489">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=AlxdUmjrrWsp-jZ8HF9VCf-I9fObj5MQa9O9EBSeYbo4Z8AxF_T18ahxLbuGZNaFf9I1ApGuzCOjFqMPIcWUbURUI3UpTqoQTkQ7GPnuGycnr6JXLX0p_NYP--3DjsLPTXZR9uHlMXGIpGq9Dc67SxOtdYMeUj4IIUxoys2zNlj64UpxWIf_QpIrDUQRQiVV-Q5xTlk3BoZgLGc9bfdPXFKf9302kTVhsVKhanFh3Lw_N-EILy5-tl6dYBlnIB2AVzFgu4tiZ0y2uF1QxIP0cxi3zYUJE8mJ8IpVFmYp4P8hs0TpL_ggHTAlwjpIXMKON0BoA3UFYFP2kZBsVzhXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=AlxdUmjrrWsp-jZ8HF9VCf-I9fObj5MQa9O9EBSeYbo4Z8AxF_T18ahxLbuGZNaFf9I1ApGuzCOjFqMPIcWUbURUI3UpTqoQTkQ7GPnuGycnr6JXLX0p_NYP--3DjsLPTXZR9uHlMXGIpGq9Dc67SxOtdYMeUj4IIUxoys2zNlj64UpxWIf_QpIrDUQRQiVV-Q5xTlk3BoZgLGc9bfdPXFKf9302kTVhsVKhanFh3Lw_N-EILy5-tl6dYBlnIB2AVzFgu4tiZ0y2uF1QxIP0cxi3zYUJE8mJ8IpVFmYp4P8hs0TpL_ggHTAlwjpIXMKON0BoA3UFYFP2kZBsVzhXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
تصاویری از حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به بندر «مخا» در جنوب غربی یمن که تحت کنترل انصارالله قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71489" target="_blank">📅 00:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71488">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIDmMeufIKXNZ8R4XIz80JcYf863dpoC_D4fcDI8Lgw9Li3ldwM6GDJjELsjsXZYxu7SOSFCGT_mWNgKoOUOu8AqBK-nBHDHt9AKW0Guhv9UUV_oqKf98mHytoRg1zZoaoJLpAwWYJO6omdZICf6vHyuHgpeLM4mHG_BchmrAh1fVRcPcyyQfm4tn_vM0qiRIgbwWHS1RcFQ8OCkZ_2xgdSrdW6gHdGXZsz4xZywUb6zILa8KWdWu3sLq2AVHcm69f8xHzDHW3kX_QO50VweSILlMMqRE4Pj3Uo-XMWMQ9WfS7pKOu64clhENEppp2Xcxp1v4zMQqa-6RB3sfqIuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با پول ۲۰۷ در ایران تو کشورهای مختلف چه ماشینی میشه خرید؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71488" target="_blank">📅 23:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71487">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=TX-lY29P3dlWwOukpRW8BZZoEMM1Z_VEwqME_pWB6SGhYPrj1XAeoYdYO7-5LaGoA0ImoDWlPbpauH1X4V9ObRyMGDbA-6Ifwk-n6Kpr0hg0FzsL5IYRNG08PZYSAIYWmSVJq1G81DrmzmpWNFV3Mtk7DTYbhSK1A84Z4jW2gClahI6e4y7Mb515OizHYRNgXPn5cSiATXn97gXcRZXdWquPM24hadUe-zpA2BKilHfMkOoaekHMKOTUV86R7UQFEz8NuUt-yyQwv8h-bHhXaDxrGY_izOZhawi2rDGTpl-xO6d0gU4Q7Jp2xB74qPh_Zb_ESQsoXATgSCxhGLhctQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=TX-lY29P3dlWwOukpRW8BZZoEMM1Z_VEwqME_pWB6SGhYPrj1XAeoYdYO7-5LaGoA0ImoDWlPbpauH1X4V9ObRyMGDbA-6Ifwk-n6Kpr0hg0FzsL5IYRNG08PZYSAIYWmSVJq1G81DrmzmpWNFV3Mtk7DTYbhSK1A84Z4jW2gClahI6e4y7Mb515OizHYRNgXPn5cSiATXn97gXcRZXdWquPM24hadUe-zpA2BKilHfMkOoaekHMKOTUV86R7UQFEz8NuUt-yyQwv8h-bHhXaDxrGY_izOZhawi2rDGTpl-xO6d0gU4Q7Jp2xB74qPh_Zb_ESQsoXATgSCxhGLhctQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇱🇧
🇱🇧
رسانه های نزدیک به حزب‌الله لبنان وویس هایی رو از اعضای حزب‌الله منتشر کردن که در زیر ارتفاعات علی‌الطاهر در تونل ها گیر افتاده بودن و درخواست کمک میکردن.
همه این افراد بعد از حملات ارتش اسرائیل و نابودی تاسیسات زیرزمینی کوه علی‌الطاهر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71487" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=jdw2dpTGKLfatf7UBQOiarE1LHz7BngQG98-CikeYjwou0FcIkTbBEWQBmh9ySjDbtlSB8bH5QHnwHdtZLs_DGx-NiSNBsSqKIYtTBf27OPjz2I6UTLcLFLAmQIC0XaPxDPhRT1QtsM66NRO--jg39zShgqLRt_Ujj0VKq8UrSvOd0kJhOSST1Wg7sTNgAgCSROiQEMLM-jrbohWa5de14Vfd9HNW-t92Zw6HelVM_iMX8311YAVurdUtD551GK_J1Oh5WnhvHdvPZ1_-VwpDC0NW0dl5rc99WVU85lsxHZn2REVPD8JFotG7TUTAtkcIC4gtzZw2Y32tcKuzlNO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=jdw2dpTGKLfatf7UBQOiarE1LHz7BngQG98-CikeYjwou0FcIkTbBEWQBmh9ySjDbtlSB8bH5QHnwHdtZLs_DGx-NiSNBsSqKIYtTBf27OPjz2I6UTLcLFLAmQIC0XaPxDPhRT1QtsM66NRO--jg39zShgqLRt_Ujj0VKq8UrSvOd0kJhOSST1Wg7sTNgAgCSROiQEMLM-jrbohWa5de14Vfd9HNW-t92Zw6HelVM_iMX8311YAVurdUtD551GK_J1Oh5WnhvHdvPZ1_-VwpDC0NW0dl5rc99WVU85lsxHZn2REVPD8JFotG7TUTAtkcIC4gtzZw2Y32tcKuzlNO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71485">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=qvlaFC2XEZx1XEEdLOs1zuxjJaCtWNNvxkMq4aYy7q65hZwPBtM-2br85XflTHU3eMsWIKC8aNdin1ydx23zG41WVwcvtSZ4qYWln4zYkwgDFPz28wAKmPr8fFkPsBS5sbIfxGtL_Ws01pZO4t5vj6aEhK_lRzN9BSX4TEu8Gl72p0v49v-DeXeHEmSGCtuuFT_a_hlQRJFK8iR9b2ngCSi4-UhvKC8ZhFSOnB5vbYFEuDCNs6zolrWdRA5Tf89nbZXPjcUTOjjsWokS_ZIWwkCYFlQlOwA5IqXl32tyaa-J_OFxJzWlLjcbwDm_Poojn52IVa0f22lk1gJyky2J4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=qvlaFC2XEZx1XEEdLOs1zuxjJaCtWNNvxkMq4aYy7q65hZwPBtM-2br85XflTHU3eMsWIKC8aNdin1ydx23zG41WVwcvtSZ4qYWln4zYkwgDFPz28wAKmPr8fFkPsBS5sbIfxGtL_Ws01pZO4t5vj6aEhK_lRzN9BSX4TEu8Gl72p0v49v-DeXeHEmSGCtuuFT_a_hlQRJFK8iR9b2ngCSi4-UhvKC8ZhFSOnB5vbYFEuDCNs6zolrWdRA5Tf89nbZXPjcUTOjjsWokS_ZIWwkCYFlQlOwA5IqXl32tyaa-J_OFxJzWlLjcbwDm_Poojn52IVa0f22lk1gJyky2J4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای زن دعوت شده به صداوسیما درباره ترامپ و نتانیاهو:
ما میخایم با پول حلقه های ازدواجمون طناب داری بر گردن نتانیاهو و ترامپ بندازیم
درست ۷ کیلو و ۲۰۰ گرم طلا به قاتل ترامپ جایزه میدیم
ما میخایم خون بر شمشیر پیروز بشه
از مامان های محترم تعهد گرفتیم و به مقدار توانشون طلا کمک کردن که به قاتل ترامپ بدیم
از ارزشمند ترین دارایی هامون می‌گذریم تا ترامپ کشته بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71485" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71484">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇮🇷
۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران یک موشک کروز ضدکشتی را از سیریک به سمت تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71484" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71483">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=tMs3N5LKKnm39diOYF_3-0CsAywgPNxtKyY2kanAtUuuM41ZVqH4BbGs_jWBVBU4aiazGUdJsin8KkDZfEqXCMTyM_RTo2prWB-lUbGtQG5sjJb-v00nHFG6Vha1BWH_x4kTLQvNXIDozw8hSLh51LIB171Sp97Hb-nt4CSuHmLE98KNQIfJLr2uS3kwQoSO2A98oeuLR98jTb1jwZq8fcv-EBPwevk5nw61aRACdlZNoltPP1s8VN1Kg8qr-PoDgea64cT3emAZpXye2xphkoPFnaZCuOl6MzqN9Y_WJT1Voa2znEAz1sDxBArloXvqv5qWeEvOWqqHNy6NvLWaDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=tMs3N5LKKnm39diOYF_3-0CsAywgPNxtKyY2kanAtUuuM41ZVqH4BbGs_jWBVBU4aiazGUdJsin8KkDZfEqXCMTyM_RTo2prWB-lUbGtQG5sjJb-v00nHFG6Vha1BWH_x4kTLQvNXIDozw8hSLh51LIB171Sp97Hb-nt4CSuHmLE98KNQIfJLr2uS3kwQoSO2A98oeuLR98jTb1jwZq8fcv-EBPwevk5nw61aRACdlZNoltPP1s8VN1Kg8qr-PoDgea64cT3emAZpXye2xphkoPFnaZCuOl6MzqN9Y_WJT1Voa2znEAz1sDxBArloXvqv5qWeEvOWqqHNy6NvLWaDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71483" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71482">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d66564850.mp4?token=MyqIKiiBnNgMWNZ8xQnkWiWw48PiVfnu7F8OjypdV6_D18boelvCBEyVHHvwQ7DxGYgHLkI9ibWtZOMAHYl76kIMy5lSdpdHjWbDb7RWrklUCwn4O4JpEBAW-EBaoWb73YLNz5TUpA-02S9mX55_5VViyyg1nCTpbKLnlIVVqEhv8HLYX-opZB4dhCHUUWlD3NHnoy9xKBTL8wfImQgwZV_nE6ASxb2JcV-tSQwhSD8Y-Ivn6ho_CwN67dXI6ahHrdceqF8zyXy14EDjff-Alwg4FaefSwju21gxPq4T32Z9QRRWlBlprV0yrp7Tb2fbk5UK6NGlqvg10Z6Ik0x5xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d66564850.mp4?token=MyqIKiiBnNgMWNZ8xQnkWiWw48PiVfnu7F8OjypdV6_D18boelvCBEyVHHvwQ7DxGYgHLkI9ibWtZOMAHYl76kIMy5lSdpdHjWbDb7RWrklUCwn4O4JpEBAW-EBaoWb73YLNz5TUpA-02S9mX55_5VViyyg1nCTpbKLnlIVVqEhv8HLYX-opZB4dhCHUUWlD3NHnoy9xKBTL8wfImQgwZV_nE6ASxb2JcV-tSQwhSD8Y-Ivn6ho_CwN67dXI6ahHrdceqF8zyXy14EDjff-Alwg4FaefSwju21gxPq4T32Z9QRRWlBlprV0yrp7Tb2fbk5UK6NGlqvg10Z6Ik0x5xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت های عجیب
پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:
نزدیکان رئیسی گفتند که حاج‌آقا خودش اقرار کرده که اقتصاد متوجه نمی‌شود.
بعد گفتیم خب، یعنی باید برای رئیس‌جمهور کلاس اقتصاد بگذاریم؟
گفتند نه، کلاس اقتصاد که نه؛ حاج‌آقا ذهنش می‌پرد و خسته می‌شود. بیاییم موشن‌گرافی بسازیم.
ما یک تیم انیمیشن آوردیم که برای رئیس‌جمهور مملکت کلیپ‌های اقتصادی درست کند. قانون هم گذاشته بودند که هر کدام از کلیپ‌ها بیشتر از سه دقیقه نشود، چون ذهن حاج‌آقا می‌پرد.
ببینید چقدر این موضوع تلخ و «دارک» است که برای رئیس‌جمهور مملکت و بالاترین قدرت اجرایی، بروی انیمیشن درست کنی تا بلکه اقتصاد را بفهمد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71482" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71481">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=Wh0lJdcTKzT_VBmMdPA4K5TyARsUfTM5YF7wOkDWpNxBE-xm8ktKjfDFFHuGlL7_xCcF5cCc1H8krRiwdc3ov2ittUskQry6CAq6FNT8Cij2OJ4kctnpxHMW4wFdwDFbURkM5NapDZQhbFgbFqr-8xQ3HhAyOeaM5Q0f44P3EuIWfeZKZc8HEmfVt-j6aZV7Nw17R7fm3oEPO9D7CtIjYFvnuP1d2Pi8GW_dMlkXzAziQ77PTQ6_VtiKz1wTm_8f9ExG0dXUVqmGGBxVegPb7XJlVqe7mT-ij1RKF7IV1of6XWXZ0PBN-wZlVdYaDDWKZk6d-qoSDBzCZcfB9dPlAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=Wh0lJdcTKzT_VBmMdPA4K5TyARsUfTM5YF7wOkDWpNxBE-xm8ktKjfDFFHuGlL7_xCcF5cCc1H8krRiwdc3ov2ittUskQry6CAq6FNT8Cij2OJ4kctnpxHMW4wFdwDFbURkM5NapDZQhbFgbFqr-8xQ3HhAyOeaM5Q0f44P3EuIWfeZKZc8HEmfVt-j6aZV7Nw17R7fm3oEPO9D7CtIjYFvnuP1d2Pi8GW_dMlkXzAziQ77PTQ6_VtiKz1wTm_8f9ExG0dXUVqmGGBxVegPb7XJlVqe7mT-ij1RKF7IV1of6XWXZ0PBN-wZlVdYaDDWKZk6d-qoSDBzCZcfB9dPlAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین پایگاه دریایی نووروسیسک روسیه - بندر اصلی باقی مانده ناوگان دریای سیاه - را با حمله ترکیبی پهپاد و موشک در طول شب هدف قرار داد.
لیست خسارات تایید شده قابل توجه است
؛
ستاد کل ارتش می‌گوید سه کشتی جنگی (مین‌روب ژلزنیاکوف، ناوچه حامل کالیبر، دریاسالار اسن، و کشتی پهلوگیری پیوتر مورگونوف) به علاوه انبار سوخت مورد اصابت قرار گرفته‌اند.
اطلاعات و OSINT اوکراین، ناوچه دریاسالار ماکاروف، یک کشتی موشک‌انداز بویان-ام (غیرعملیاتی ارزیابی شده)، کشتی گشت‌زنی واسیلی بیکوف، چندین قایق موشک‌انداز و دو رادار دفاع هوایی در نزدیکی گلندژیک را اضافه می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71481" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71480">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71480" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71479">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfaB5A5bfV0lhZ7KS1lVZuSBTdoSHVb3PUzC_k8SX7lPFbFk4HUh1Zh1kein1XvDiO8BCtsLRE2VdpOY8cwxL8hoWUiTXlTZ0E_zX_Q_hV_IBlxOgZkG9nLdV-Po5tPmcXc2BVl8ymgS5V-TOXOZVqxBu_oz3p-eFqFTbw8CI0t6xtKON-BEnG7rmViNNLXl5OsnMc6Mi3lcPAZ-VUmSFGcPSiseMqAiyuwvr63eDp23AKFudBweSAhH7nFa5pxNbds3q4YtE2qzvvMcf2emGqCzlC0m2aXEYHo7GkArfL3c42mQJJrF2K_zP6C4uOb43fV8al8VcDYdjIewXZlLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71479" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi9B9FHQ1p1t_HkHxwVjt0qRxg-YsEzjZmak2tenFnqAOlLjpWI4b8CA2NYcusVVjOJKr3Fj1XGQKMPV77JJ7AP_N5n-lNSlEUtOf-PZImxak8d_oIx7StsfndcKZ0NJA0yEhAIdE-8LY8tcYxSXewF_JCGTMleBQNxxS11LsDrBoo5N1Bfi1zab7FR5etXfcd6OgvLveeWzzEK96Se86a_EuEW0Snv4StXnRGOrf8KEMZjAgX960ea0R2qJaiU_4N-dx-Nwl3cPvqITdwQGoiQ2S2OOPIFsukGrSSg9lpQKsbkuaLhEzO3GdmaQ7TCpV1d3D3skxJ17lPZqqqth5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71477">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=loI91KdJYk4B3-mTx0WIjbHt5LnZzWRRfDtmmmGZFv54-4rzRza_Hfwi4jvXehYEXT_S25djEHUrPPUx8fxn5jWNaVtRVEZNDN6JrK3bf7MiELTLFH0JHrzANMEV7wDtCKH38FNnRSvMhnipJ4DFIXbdLjlBqzZnyXWWPIQHYBle-7s-RKnUMG_clodkPylCbIKkjaViwUZZUtl7eDHvFtuUOAJoQbY1r2TARCfbfJZlqED9xg-kqqf-5nqKXR1w3uLOLVp6GuThlqh65ER1fUIIS5dqXY3VKO75owBgeFzY2H9aRipbbsn04iRgacpxUlXZzfFrs2I9sD2D8IC5xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=loI91KdJYk4B3-mTx0WIjbHt5LnZzWRRfDtmmmGZFv54-4rzRza_Hfwi4jvXehYEXT_S25djEHUrPPUx8fxn5jWNaVtRVEZNDN6JrK3bf7MiELTLFH0JHrzANMEV7wDtCKH38FNnRSvMhnipJ4DFIXbdLjlBqzZnyXWWPIQHYBle-7s-RKnUMG_clodkPylCbIKkjaViwUZZUtl7eDHvFtuUOAJoQbY1r2TARCfbfJZlqED9xg-kqqf-5nqKXR1w3uLOLVp6GuThlqh65ER1fUIIS5dqXY3VKO75owBgeFzY2H9aRipbbsn04iRgacpxUlXZzfFrs2I9sD2D8IC5xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به نیروهای نظامی‌ای که هم‌اکنون در تلاشند تا اطمینان حاصل کنند بزرگ‌ترین حامی تروریسم در جهان — یعنی جمهوری اسلامی ایران  — هرگز و به هیچ وجه به سلاح هسته‌ای دست نخواهد یافت، ادای احترام می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71477" target="_blank">📅 17:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71475">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=vOcEo1XB7k8lVrhhCkd5h1zXAtnHE_NiXXaYRxSc_3qgY23N_hp5Oaxglivmkwz3dCGHGaTkR6KrZT_rHQsonGhYFfILfDhQQ2I4d8tEH9rRAFD3djHDwO0sA8Hgt4Vb9Dy4feOSN_UgFkw6XrcJ8_DbVdNn41uZiFlje38mt5i5rUoKfmPJJcVwrkokgufeR6GjyqsrEl4Rra9YBH8Q_eWOtwUDo2qNkKLD5oOGHwHMEWYNAcz5Q63EYKxeX7ClE0NnGG-XbilGFysYtrG0--91iKdxdxp468MuARCI0lXD6SO7SSbJnxfOOUEm7bV5JWBLPQ2FRE-AVJaKvisd6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=vOcEo1XB7k8lVrhhCkd5h1zXAtnHE_NiXXaYRxSc_3qgY23N_hp5Oaxglivmkwz3dCGHGaTkR6KrZT_rHQsonGhYFfILfDhQQ2I4d8tEH9rRAFD3djHDwO0sA8Hgt4Vb9Dy4feOSN_UgFkw6XrcJ8_DbVdNn41uZiFlje38mt5i5rUoKfmPJJcVwrkokgufeR6GjyqsrEl4Rra9YBH8Q_eWOtwUDo2qNkKLD5oOGHwHMEWYNAcz5Q63EYKxeX7ClE0NnGG-XbilGFysYtrG0--91iKdxdxp468MuARCI0lXD6SO7SSbJnxfOOUEm7bV5JWBLPQ2FRE-AVJaKvisd6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ واقعه ۱۱ سپتامبر را به جنگ خود علیه ایران پیوند می‌دهد:
به همین دلیل است که امروز می‌جنگیم. ما چاره‌ای نداریم؛ تنها گزینه، پیروزی است. ما سرسختانه می‌جنگیم. برای پیروزی می‌جنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71475" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71474">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=s_SkeFWS3ohm_dRgrNXIKTqTjLVaa1xGVOf2x3s5nUi5XFGLjJ1ha_18Y0OPGyGN4iv01dH5hqJp9virKAqvjTQobfcTZ4GQhIG2CjXXWAoY_J9Z1FV9Dxuku0XnvCB-uQg-DQPQyEKB16pOSWqXr42mBIzv16SU0X3Envz-U3SFkwZwZxOUbKvhjrTPia6_Yqt9bin15Tjc8SretjlA0y4c50tol1kUAKJBCE15ZeEdWwX-8_GIxWTt1bLAEO-RSlTKiokjTxWC-4eQnnMg49A1tzAZxGpi-mJ1mjMvB8wdmKfm9RGrN-2VZYzz1wKM2m1yEC7igD63l366ghWutg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=s_SkeFWS3ohm_dRgrNXIKTqTjLVaa1xGVOf2x3s5nUi5XFGLjJ1ha_18Y0OPGyGN4iv01dH5hqJp9virKAqvjTQobfcTZ4GQhIG2CjXXWAoY_J9Z1FV9Dxuku0XnvCB-uQg-DQPQyEKB16pOSWqXr42mBIzv16SU0X3Envz-U3SFkwZwZxOUbKvhjrTPia6_Yqt9bin15Tjc8SretjlA0y4c50tol1kUAKJBCE15ZeEdWwX-8_GIxWTt1bLAEO-RSlTKiokjTxWC-4eQnnMg49A1tzAZxGpi-mJ1mjMvB8wdmKfm9RGrN-2VZYzz1wKM2m1yEC7igD63l366ghWutg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
آنچه اکنون در مورد ایران شاهد آن هستیم، حیوانی است که در تنگنا گرفتار و زخمی شده است.
این آخرین نفس‌های رژیمی رو به احتضار است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71474" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71473">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=kOfBlGpoBECaAyYgU0y2XTKFEsnnayyQ03HasBZtjgM0_b3NzEh6i_T4yuFVBohmg7q8J0ZBGEOMS5eFoupTzpLikrdDDbuNiK_gp6OxHiK3d88Q3DfRPgOSZQ1r8-d7_kNTwFBW3aweGpKOPPWSL-Hl4b45cPZnsO5897y9cJ3dASYRIEY1Cxy1ikesRjTG8I-L_Ivr9bsH0arPsopXA5Ej5IVMNgYEGPHaJzuzejDM8s075RhDjR5DfiDfIPBmN0i97fXpk1YJQQYSpSc-ZWVJYNyvub2NWCbBfrn5wcWLyqdFK3LyzsUAGruYFizDKhsZ9AKVCV30BpwxpeJj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=kOfBlGpoBECaAyYgU0y2XTKFEsnnayyQ03HasBZtjgM0_b3NzEh6i_T4yuFVBohmg7q8J0ZBGEOMS5eFoupTzpLikrdDDbuNiK_gp6OxHiK3d88Q3DfRPgOSZQ1r8-d7_kNTwFBW3aweGpKOPPWSL-Hl4b45cPZnsO5897y9cJ3dASYRIEY1Cxy1ikesRjTG8I-L_Ivr9bsH0arPsopXA5Ej5IVMNgYEGPHaJzuzejDM8s075RhDjR5DfiDfIPBmN0i97fXpk1YJQQYSpSc-ZWVJYNyvub2NWCbBfrn5wcWLyqdFK3LyzsUAGruYFizDKhsZ9AKVCV30BpwxpeJj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
اعتراض ربات های انسان‌نما در مقابل وزارت امور دیجیتال لهستان و سردادن شعارهایی با مضمون«ما خواهان قانون‌گذاری هستیم»و «از مشاغل دفاع کنید»
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71473" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71472">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=rAi8SBWcW2UZ9pFZrL6OZW-kzbzllvT29vZ4bYZWScf57_jLM4CtsggG6SVEdWXm9VXBcsgynMZmwXlETwiK2Xd9FOcMtsisOS4_5hbrphzIkbK2PrC-XkNsRQQBwfi5KqtwjunBL-t1lRbcfxJkU_a5OqwG2DavDvyt0I3GaxnASQnBjiEOJJBMmbUmznGPj0Oa9YZla7iWUjzp4ch75U7PKo2VCWSkQuysPkvC4b2JVp0Dd_OKtNU_v3R9b399B7p7nkESZuYOIqiMQRpbIwf9QlUEYnw9qTe7wQuD12YCMEOBJm3O2y8VjN6Z584qo8_4zPlrUaeDvne-7P62sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=rAi8SBWcW2UZ9pFZrL6OZW-kzbzllvT29vZ4bYZWScf57_jLM4CtsggG6SVEdWXm9VXBcsgynMZmwXlETwiK2Xd9FOcMtsisOS4_5hbrphzIkbK2PrC-XkNsRQQBwfi5KqtwjunBL-t1lRbcfxJkU_a5OqwG2DavDvyt0I3GaxnASQnBjiEOJJBMmbUmznGPj0Oa9YZla7iWUjzp4ch75U7PKo2VCWSkQuysPkvC4b2JVp0Dd_OKtNU_v3R9b399B7p7nkESZuYOIqiMQRpbIwf9QlUEYnw9qTe7wQuD12YCMEOBJm3O2y8VjN6Z584qo8_4zPlrUaeDvne-7P62sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇶🇦
هم‌زمان با نخستین سالگرد حمله هوایی اسرائیل به دوحه (قطر) در سپتامبر ۲۰۲۵ — که نخستین حمله اسرائیل به خاک قطر محسوب می‌شود — تصاویر جدیدی از این رویداد منتشر شده است.
این حمله، مقامات ارشد حماس از جمله «خلیل الحیه»، مذاکره‌کننده ارشد این گروه را در جریان مذاکرات آتش‌بس هدف قرار داد.
اگرچه رهبران ارشد حماس از این حمله جان سالم به در بردند، اما شش نفر، از جمله پسر خلیل الحیه و یک مأمور امنیتی قطری، کشته شدند.
این تصاویر جدید که منبع آن‌ها شبکه تلویزیونی «العربی» (Al-Araby TV) اعلام شده، لحظه اصابت را از زوایایی که پیش‌تر دیده نشده بودند، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71472" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71471">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e182f67792.mp4?token=sD704o0wkE0MY7Ruh3ZYvwKB8bWJDIjtP0SzBXF5RTqYiZrhxikLMPRyI9UlSWbT-c_keRGQs4DVTPmEIKfPRPjil6NHH8GZ6zTml17TzEeLKW-LeaU0oAAtIOdxm5rkeqifO1PPU6wnLPqo2Eogx1vklMqx1xNYtdGcnxXdqAYCIYl2L_k5_dQfb5hm6dnOFRKpiUsR1SmfLzup2_wqYj21_08yfBMLWcv6E_Pi-_dVvV5yoqEtUm9ipsJg9wbB0JBQkDV2so44F15iVNXETv_aKhrfIXuUjiL1_DGl9RWnGg2hG1MQw2korLQuHml0GREHYCdmXzj0QP9oEpd4xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e182f67792.mp4?token=sD704o0wkE0MY7Ruh3ZYvwKB8bWJDIjtP0SzBXF5RTqYiZrhxikLMPRyI9UlSWbT-c_keRGQs4DVTPmEIKfPRPjil6NHH8GZ6zTml17TzEeLKW-LeaU0oAAtIOdxm5rkeqifO1PPU6wnLPqo2Eogx1vklMqx1xNYtdGcnxXdqAYCIYl2L_k5_dQfb5hm6dnOFRKpiUsR1SmfLzup2_wqYj21_08yfBMLWcv6E_Pi-_dVvV5yoqEtUm9ipsJg9wbB0JBQkDV2so44F15iVNXETv_aKhrfIXuUjiL1_DGl9RWnGg2hG1MQw2korLQuHml0GREHYCdmXzj0QP9oEpd4xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه های این بانو درباره وظایف زن مرد توی ازدواج ۳ میلیون ویو گرفته واقعا مفید بود
😏
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71471" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71470">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=lIfmvMhlRRHsOrN4xSQjlLo8cL57jJkdiwTsmTH-8jx3z-RNLq2s8YEe5WPrxcC2pmHqqt9ue_oQF6Xx9g9Zg3fgiZzz--wjxI_geHJt4iwV2cGFhIMEeb0l6DS2GVC6570vaY6zi52GQAx4p27g3yt8lELVJPpnrPMUTm17NBxCN2hkuTvDTd-BHka8RCzEY0kiLTzq-0DK4bndRcWDCHese64314Yv51AYMd6_JGfHbU_ePABQQYmKc8of9piwWxwzZ05nhjOj88UrMobarqQEG8ju2TtpOwNlPhx16MbV9lmUCfIVIwIEM0_ta2Wrj-GCnEovtLxlU4SUjgX_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=lIfmvMhlRRHsOrN4xSQjlLo8cL57jJkdiwTsmTH-8jx3z-RNLq2s8YEe5WPrxcC2pmHqqt9ue_oQF6Xx9g9Zg3fgiZzz--wjxI_geHJt4iwV2cGFhIMEeb0l6DS2GVC6570vaY6zi52GQAx4p27g3yt8lELVJPpnrPMUTm17NBxCN2hkuTvDTd-BHka8RCzEY0kiLTzq-0DK4bndRcWDCHese64314Yv51AYMd6_JGfHbU_ePABQQYmKc8of9piwWxwzZ05nhjOj88UrMobarqQEG8ju2TtpOwNlPhx16MbV9lmUCfIVIwIEM0_ta2Wrj-GCnEovtLxlU4SUjgX_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شرکت پخش فرآورده‌های نفتی:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را بردارید
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71470" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=faPFkDX9XcCQo-uFpdBO2CqdFfKI2r6QZFntgMO8r6dNEECeT3ZGhFTsEUduDe1XOdg2-ptIztajM05sRjJ-7IZXy6xvDo1kGtN0bGEhpa2kR9oeqarCtXGpmsQXVVsdmwya2Qs-l23U9DavbgOKzjOEeuyV-9e8xWLmXpzazTQZpdq5aMpkubWqXNMBSLyEsro0P_j0-EgzPGAKG6Z8PXoB5bV2padgyIuk2VoLs1_w9-09SxRh6oWIMTY93prHhXl8WQNXSC-Mha9qZ-mMYYpFyaJbkTYuL2bcIrbWt4RFEG1EjmDTqVcC-ZM_CKQWJZgw05IPBhYn2y6642BU4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=faPFkDX9XcCQo-uFpdBO2CqdFfKI2r6QZFntgMO8r6dNEECeT3ZGhFTsEUduDe1XOdg2-ptIztajM05sRjJ-7IZXy6xvDo1kGtN0bGEhpa2kR9oeqarCtXGpmsQXVVsdmwya2Qs-l23U9DavbgOKzjOEeuyV-9e8xWLmXpzazTQZpdq5aMpkubWqXNMBSLyEsro0P_j0-EgzPGAKG6Z8PXoB5bV2padgyIuk2VoLs1_w9-09SxRh6oWIMTY93prHhXl8WQNXSC-Mha9qZ-mMYYpFyaJbkTYuL2bcIrbWt4RFEG1EjmDTqVcC-ZM_CKQWJZgw05IPBhYn2y6642BU4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=uD5xrcn59DnMq7KkBu7rylW2CA1RnbiCfgBbD0t0U0ta2IzVT2KL0epcsK1ixr4PnVFsPEWI8k0s-meaIDKEkn_yIRhdr_KurfyaIwfrKyo1GnN1KXOuF3qur_Oj4qKePjlvK8tERhg4_3pGm7NEtq19tWBMgunD_gvrd6VGD5uhLXDPWKFE5mUe1SzWw-UvNKv8qVA3PcGrfriLSGUicGQAuAp76xrGOkd23mQkuDzTOcPvi_93ip4RtsxcEgrvIH2zx6SxGbUXCe5QbqD0zWP5UI4A5zFbsh6RNRm2jhms3S6eoA8Riqxtn0Llyrgf2arQ9etIj4fSxOIQpWo1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=uD5xrcn59DnMq7KkBu7rylW2CA1RnbiCfgBbD0t0U0ta2IzVT2KL0epcsK1ixr4PnVFsPEWI8k0s-meaIDKEkn_yIRhdr_KurfyaIwfrKyo1GnN1KXOuF3qur_Oj4qKePjlvK8tERhg4_3pGm7NEtq19tWBMgunD_gvrd6VGD5uhLXDPWKFE5mUe1SzWw-UvNKv8qVA3PcGrfriLSGUicGQAuAp76xrGOkd23mQkuDzTOcPvi_93ip4RtsxcEgrvIH2zx6SxGbUXCe5QbqD0zWP5UI4A5zFbsh6RNRm2jhms3S6eoA8Riqxtn0Llyrgf2arQ9etIj4fSxOIQpWo1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=NILIZP6TYjgHBtRB-yZ-RmOPWkXx9arxjumF61KH6JSxa1VgN4V3iUrCA07oHopQHS9kj-Sd9uJ0s6i7jR1KFgLRBVGd0AGO34diQ8ZZtrjqYgHKNoKRaLSrTnh3XDZv7stREkgylzu4mOIRLozNFRjPkJJ2b5dRreM5mtdF0NST-Sl3ZhDIhFiuWoC2ZLsltTQ5Voi0Z2qtCZ_83nn5AzO1xpbvv83uD-eUAmuBhwbyFoXW3zBkngds4US6ORtW9kgrFG4Rog4eZx4QBXo58b4ZDhlR1KNOff6Zs3HSX3EOIYKcI2RWffkIQrXNedD4pUHpxfrASiH7IGUcqLlhJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=NILIZP6TYjgHBtRB-yZ-RmOPWkXx9arxjumF61KH6JSxa1VgN4V3iUrCA07oHopQHS9kj-Sd9uJ0s6i7jR1KFgLRBVGd0AGO34diQ8ZZtrjqYgHKNoKRaLSrTnh3XDZv7stREkgylzu4mOIRLozNFRjPkJJ2b5dRreM5mtdF0NST-Sl3ZhDIhFiuWoC2ZLsltTQ5Voi0Z2qtCZ_83nn5AzO1xpbvv83uD-eUAmuBhwbyFoXW3zBkngds4US6ORtW9kgrFG4Rog4eZx4QBXo58b4ZDhlR1KNOff6Zs3HSX3EOIYKcI2RWffkIQrXNedD4pUHpxfrASiH7IGUcqLlhJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnNMzo55puXpGaOjTBcCbpYFRmiZmMiGRfNBa36zyAMPZ-HUrreD7ySueScLLl8l7JikftKQZag_MFnmLBqgm5AVNfbndPws3oNnos1nf4okJNnYySiEvh5YtUnt4875rSHybD7OxSt4Cm-eDjV3BukDZhcamojnQ-sMIDPRyTyZkyoanKStSzXIev24A32ZYtil0hqBoz1JxYkXq0EFoTSGSDqY78Fr9qIYeNg9a5ERr7XSxvSeVzAh-JzSuAUUbqfuUykluRU0FJbMeP7mMpgaRG7kgoFV-KdZ2wq7eEojjG3AKPC6NVzfB6BBd7rwKV1LDE_rlo-hXHYpsGEKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9hsijUj2cmGp8U8zXNCYKhXrKzr2tSNxRw83qoOmERzrdDAzaLb5AS_vzLgDJ7jaVw2Rl-vI1u9GvKdgTcLP7gGZdDb_MChqzgpZbix_c1mvUmUi2wBLl18utJ5GKRClZM35sMOmdk5aPvG1EIQgV0G1mdnakHjfZ5wzfYOIOdvk9GCGGDdV9xyRfyj_UxPIwvyvcIQPz2obRMrcvk2NKjL0NoHGDPS8EnrDg4sfs8FvQ6wCiblaDQ0CsDqgggCz0BswYBfXi5BQgjWBXw9QWQdpAfIgbtNc_cibEEMajFbmxnUTHKKXJggiqHsZbpiy4ri7_Ul8LpKC5lhzLQ3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=ZL38Npc7Ds5eGrcI62Tvx4XHW81n6AaxwMfhx4FupG3G77HBtz74OeUcFxgdpqCbH8jmFSj3VsmIKWWwCP8mOQtdlVS1TJKycA7DpfCx2tv8daG8-m8DoZwyLqNvPgU8CcrpS0jE4LKy-71wNJB3qUNwnka998Wxi5noQI4N7gECVVJNNEXlFpp52PJzjXPv8uH0mee54vuiHvikDC8Wllwqv8wZQbhdvwulW6tzqPZRs7jIsK1sWExxN8NYSRxptKORNircRWFNKgixlTodJLjIXNF6HRF0_ZAJmmjEnpsYJoC5Ulfi-RM0nN_WTjuq1SfEdRYDJae6OlXRt_tCQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=ZL38Npc7Ds5eGrcI62Tvx4XHW81n6AaxwMfhx4FupG3G77HBtz74OeUcFxgdpqCbH8jmFSj3VsmIKWWwCP8mOQtdlVS1TJKycA7DpfCx2tv8daG8-m8DoZwyLqNvPgU8CcrpS0jE4LKy-71wNJB3qUNwnka998Wxi5noQI4N7gECVVJNNEXlFpp52PJzjXPv8uH0mee54vuiHvikDC8Wllwqv8wZQbhdvwulW6tzqPZRs7jIsK1sWExxN8NYSRxptKORNircRWFNKgixlTodJLjIXNF6HRF0_ZAJmmjEnpsYJoC5Ulfi-RM0nN_WTjuq1SfEdRYDJae6OlXRt_tCQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=va1xmx1EyLRH0fhOxGmt9aaUPMkZCO6HJ479_RtjRzFKsf9goLcF_8RMlF567yZyM7r-eSI52xH3_aS9fRLGV6mL_ISG7m9tcdzRnLMfkQlmAyVfYMFJ3S5UGb9jFioovURTPsBGsMfRhzSgdeZWWylJNR3gkozWpKgMNOv_49GsnpBZNk9UBxDBeNGTfp9FO3KxJMvCynoBDQDAKD3WfEDuT-uGJ_hpOqj-4ZEErq9p1aLfhsGkkekiMBgn0F56bE_hRKSUnnpbRQwAebjsvu294iJlBMegfbDo00lNd5reNP3Ijz8_U84Dnjt6VqlFZ7hNhns11HSgiop5a-WYVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=va1xmx1EyLRH0fhOxGmt9aaUPMkZCO6HJ479_RtjRzFKsf9goLcF_8RMlF567yZyM7r-eSI52xH3_aS9fRLGV6mL_ISG7m9tcdzRnLMfkQlmAyVfYMFJ3S5UGb9jFioovURTPsBGsMfRhzSgdeZWWylJNR3gkozWpKgMNOv_49GsnpBZNk9UBxDBeNGTfp9FO3KxJMvCynoBDQDAKD3WfEDuT-uGJ_hpOqj-4ZEErq9p1aLfhsGkkekiMBgn0F56bE_hRKSUnnpbRQwAebjsvu294iJlBMegfbDo00lNd5reNP3Ijz8_U84Dnjt6VqlFZ7hNhns11HSgiop5a-WYVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به زنش گفته دست پختت رو سگم نمیخوره! اونم برای اینکه شوهرش رو ضایع کنه، رفته غذاشو گذاشته جلوی سگ!
در نهایت سگه این شاهکارو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71456" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=rui6nd44G2-AiVn3NUOWAfzqrMnQvxpL9_m_kxLilQD9ka8RgaVlGe05rRRQq9FfeJSfW1OAP_yJ5NjyaV76_RUdc78t0msSBk_4H-rTRttn6l7KusxkBhq08HwH0Bgtl2rU4V82lPb9IQ4nr_sNn032eTZ07xcCbChz_6LnJiElj1H84opKe-C-TK-4V2nMcOtCeZpsI6RY4qX2UmWQX5_TZhE-yofIBG6Myz51m9lWUiTlvk1A554sZyNtkqLsV0lLLUGgzWeh_bz-r0_UbSg55GaQm4QSFdW1ltLgbmtHEvCS5ieq05bOwDzAGQXiPcMwK3NKImvcGiOwqieujQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=rui6nd44G2-AiVn3NUOWAfzqrMnQvxpL9_m_kxLilQD9ka8RgaVlGe05rRRQq9FfeJSfW1OAP_yJ5NjyaV76_RUdc78t0msSBk_4H-rTRttn6l7KusxkBhq08HwH0Bgtl2rU4V82lPb9IQ4nr_sNn032eTZ07xcCbChz_6LnJiElj1H84opKe-C-TK-4V2nMcOtCeZpsI6RY4qX2UmWQX5_TZhE-yofIBG6Myz51m9lWUiTlvk1A554sZyNtkqLsV0lLLUGgzWeh_bz-r0_UbSg55GaQm4QSFdW1ltLgbmtHEvCS5ieq05bOwDzAGQXiPcMwK3NKImvcGiOwqieujQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این آقا یه ویدیو از چینی‌ها گذاشته که یه شیشه‌دودی واسه ماشین ساختن که با یه بیلبیلک میشه درصد دودی بودنش رو کم و زیاد کرد؛
حالا به جای اینکه پشمای ملت از تکنولوژی بریزه، 98 درصد کامنت‌ها اینه:
بهترین مکان واسه اونایی که مکان ندارن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71455" target="_blank">📅 11:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=vwkdpIfyvQdF2th5PyXMTwxQQPQ27G8AQr3yt7BKqwuR9UzbSB2TpCaCVy3FwHKDdoH21EQML3fJAFDRZA3Xl0kCHBT8TEr1rb8Vdovehngr5hwSLzEEGcQbtIBkxj8eLnMGKBxOFQZB-oRlVwUe2qrC8L3cWd0MPDfNQzu_FmQ19KyUjwWJIIMVvrmN-7ZFLLoO_TfnHZ-ak9F_oNWeb9qGlb1FSRtRxF5MBVoNcjyPfNI6MJ2NMQQQ41aMmhsOHUfevPubwudPI9C254I6dfL2dSWrohC-lMAL7iThjm1B2DlywivVgwaDKd7lSIDPN6wCwVw_zd98N5jgxCo0jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=vwkdpIfyvQdF2th5PyXMTwxQQPQ27G8AQr3yt7BKqwuR9UzbSB2TpCaCVy3FwHKDdoH21EQML3fJAFDRZA3Xl0kCHBT8TEr1rb8Vdovehngr5hwSLzEEGcQbtIBkxj8eLnMGKBxOFQZB-oRlVwUe2qrC8L3cWd0MPDfNQzu_FmQ19KyUjwWJIIMVvrmN-7ZFLLoO_TfnHZ-ak9F_oNWeb9qGlb1FSRtRxF5MBVoNcjyPfNI6MJ2NMQQQ41aMmhsOHUfevPubwudPI9C254I6dfL2dSWrohC-lMAL7iThjm1B2DlywivVgwaDKd7lSIDPN6wCwVw_zd98N5jgxCo0jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از سالن زیبایی مذهبی برای عروسی رونمایی شد، از آپشن‌های خاص این سالن میشه به این موارد اشاره کرد:
رد شدن از زیر قرآن هنگام ورود به سالن.
عکس گرفتن با سران مملکت که کشته شدن.
پخش مداحی و قرآن به جای موزیک.
داشتن وضو توسط پرسنل قبل از میکاپ.
خوندن نماز دسته جمعی برای خوشبختی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71454" target="_blank">📅 10:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=LLXUIA0xUqfV4yQe3vv2mYWD5Y0depXbke92g0RteXumpNlCNlSm4mHIEeF4haBFyDLL4nF7JNqPaO9vpspcsqET4JcnrIuHSEybl_cwlX2SlBqaOQLku1swlflJC07I5FDoCey6tTLVAZUG1PTH1h8O1TYTC8Jwrn0IYnrNELp-8AbmjBSAcpuuzNgynVG7-ebEVkCuEj6XiBPAKmlBDWXmsX0FTfVveQDQ6rk8FbIb5FgtT21QwQhFLs3tH6GKUyGYQvl9xPFfShpAw2l28Os31eHEwllF6P6VNodmT3HFdqTH7dlwqhRmasg13unswHMLGk67J1NXum8LyG1MelAcIuXEbtMMsp0doits7Ra29x_xDOL5g60JDNlLt1f6insrBA3R1RVwWeWW2YIJEgiZEdXfT-npV4AgBa8KgYd5h4RfnXnp74UvGaTCJ-TnqHiX0hgc4NH5iq9S7uDZ_qAt7ZKjykUiv0cOVhKe59gWlbREUQgNQ33Jg2wA9EjJ0pgFCDL6lsfiELnply236AS0eh7treMv3kqZm042SyKsDCRpcls1OieG_1_R2eAGaKjmFzpYG7zcIeiWjaCvMDyvCn2N5vHogn78TQt4AIXJq6fauJ0nY0Hhq3X1J0RCg0IRvNwnrTJM6ebQbzCDM7Wul26V8WMWeHFIMJwuYwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=LLXUIA0xUqfV4yQe3vv2mYWD5Y0depXbke92g0RteXumpNlCNlSm4mHIEeF4haBFyDLL4nF7JNqPaO9vpspcsqET4JcnrIuHSEybl_cwlX2SlBqaOQLku1swlflJC07I5FDoCey6tTLVAZUG1PTH1h8O1TYTC8Jwrn0IYnrNELp-8AbmjBSAcpuuzNgynVG7-ebEVkCuEj6XiBPAKmlBDWXmsX0FTfVveQDQ6rk8FbIb5FgtT21QwQhFLs3tH6GKUyGYQvl9xPFfShpAw2l28Os31eHEwllF6P6VNodmT3HFdqTH7dlwqhRmasg13unswHMLGk67J1NXum8LyG1MelAcIuXEbtMMsp0doits7Ra29x_xDOL5g60JDNlLt1f6insrBA3R1RVwWeWW2YIJEgiZEdXfT-npV4AgBa8KgYd5h4RfnXnp74UvGaTCJ-TnqHiX0hgc4NH5iq9S7uDZ_qAt7ZKjykUiv0cOVhKe59gWlbREUQgNQ33Jg2wA9EjJ0pgFCDL6lsfiELnply236AS0eh7treMv3kqZm042SyKsDCRpcls1OieG_1_R2eAGaKjmFzpYG7zcIeiWjaCvMDyvCn2N5vHogn78TQt4AIXJq6fauJ0nY0Hhq3X1J0RCg0IRvNwnrTJM6ebQbzCDM7Wul26V8WMWeHFIMJwuYwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر موقع پریود اومده نوار بهداشتی استفاده کنه و با یه صحنه شوکه کننده مواجه شده!
خودتون ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71453" target="_blank">📅 10:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849173423.mp4?token=PlFCImvcgfNZnMShpfNqmoWB0VqcHJQwVcgfu_76sNmke_G5Z6Ssta8wTK4IwcVmmGtMYFi65rV-JaEtd8tfkz8jah3RQyttR3MyYxitUWuGU4Nvluu3MUGiJjG-nA8a7wbmtynhEAnZXXf47d_NuG7nEVGD2fXiDoOUd6cJlblsE25JHiHm1R66Dib_uDuO3uKrugnEB-eT6jgvH1PkpF7gwTmxh2y-ThryYCYkYy2ffUctWQ0gadDF0_LvAeWKyhh16AUHkullI8n7y8r5ybrb9TcoQt5gLtNbW4y9I-t4FHyQ-GDW5uzxihd-T9FoZ8CK04qu6kCMfmMsg7sff0sUWv1RUgFrgB1u_ihEVH_JPzd0jh-KjYsimWoEjtHYHs-eE_A6OkLEmX81fC-1aC3nQ-8FW9optg4P1EpKLsmJT-pMKljOtAUa8L13QDKjzRpKSEJcENb-CLJMz95Xcl4Lm8TIxHXrNNCwiZs9DKbzQsTzWF2RhRogMvjPQVQrnntP1cqJKRefO1HL9d2hJSlOBPXuiBOtSbZZToZqxk3MoFuB1WcR8KNPFzd7hxTkgmX4yy_M5jfSJmiOEnFDIXQClOeBaJ16Fo2-v4XCBsrQi9RhAmBADPD4FujXKTBZxhNj6z6mfLFzxOTPwvFPltp2XLKBHkOV4dDnRAB7LdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849173423.mp4?token=PlFCImvcgfNZnMShpfNqmoWB0VqcHJQwVcgfu_76sNmke_G5Z6Ssta8wTK4IwcVmmGtMYFi65rV-JaEtd8tfkz8jah3RQyttR3MyYxitUWuGU4Nvluu3MUGiJjG-nA8a7wbmtynhEAnZXXf47d_NuG7nEVGD2fXiDoOUd6cJlblsE25JHiHm1R66Dib_uDuO3uKrugnEB-eT6jgvH1PkpF7gwTmxh2y-ThryYCYkYy2ffUctWQ0gadDF0_LvAeWKyhh16AUHkullI8n7y8r5ybrb9TcoQt5gLtNbW4y9I-t4FHyQ-GDW5uzxihd-T9FoZ8CK04qu6kCMfmMsg7sff0sUWv1RUgFrgB1u_ihEVH_JPzd0jh-KjYsimWoEjtHYHs-eE_A6OkLEmX81fC-1aC3nQ-8FW9optg4P1EpKLsmJT-pMKljOtAUa8L13QDKjzRpKSEJcENb-CLJMz95Xcl4Lm8TIxHXrNNCwiZs9DKbzQsTzWF2RhRogMvjPQVQrnntP1cqJKRefO1HL9d2hJSlOBPXuiBOtSbZZToZqxk3MoFuB1WcR8KNPFzd7hxTkgmX4yy_M5jfSJmiOEnFDIXQClOeBaJ16Fo2-v4XCBsrQi9RhAmBADPD4FujXKTBZxhNj6z6mfLFzxOTPwvFPltp2XLKBHkOV4dDnRAB7LdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
ویدیویی پشم‌ریزون که ارتش اسرائیل از عملیات تخریب تونل‌های زیر ارتفاعات علی‌الطاهر در جنوب لبنان منتشر کرده
😨
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71452" target="_blank">📅 09:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=n1nZQSdavchS142xc7-paQcTQsKvqkECCGaCB6jvb-yjI4MmfDM0OBFtWqTkZY4iMFof5-dX4FED7QUeZAB6aQsY-Dv9Ef2btluiTR_i6c_kqtzzfKm2Ne_3AtwVMwtof6lUjj1A681XRy7txzI7zmAUHuFbI-IJMZjwJldly-AfhXdbl0gDix2xdOi3pDusPfmNj-430W9ufWTPhsYVnHuumu1DAVjAyDcdNVFfMbvt-bqzkX24l0rOCkU8fUoYhS8mtV-0QM6d_k9AXFXOVPfs2S9pbiD0XSOy8RoW3yirMQQvJsZr3_eTeWE6AVEo1e9-O7eV7_0WpYWrQLmdMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=n1nZQSdavchS142xc7-paQcTQsKvqkECCGaCB6jvb-yjI4MmfDM0OBFtWqTkZY4iMFof5-dX4FED7QUeZAB6aQsY-Dv9Ef2btluiTR_i6c_kqtzzfKm2Ne_3AtwVMwtof6lUjj1A681XRy7txzI7zmAUHuFbI-IJMZjwJldly-AfhXdbl0gDix2xdOi3pDusPfmNj-430W9ufWTPhsYVnHuumu1DAVjAyDcdNVFfMbvt-bqzkX24l0rOCkU8fUoYhS8mtV-0QM6d_k9AXFXOVPfs2S9pbiD0XSOy8RoW3yirMQQvJsZr3_eTeWE6AVEo1e9-O7eV7_0WpYWrQLmdMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «جناب، آیا ممکن است با هم دیداری داشته باشیم؟»
آن‌وقت رفتارمان با آن‌ها بسیار متفاوت می‌بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71451" target="_blank">📅 08:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=jZPFSgFvLOpNxRWEtzWsTaZ5VuAfcb1PTLiJM_In1AmLYW8oyRiSq8KsTEPAwAUVQL5K5FZbS3eRy6KlNvIXx9qs0SvdWBP-PiO5H1nMtqvbeznS_K8w00QtXN3T5xL-Ro_7J6Wt3To8GYQVw_22xyeEnNX5nS2SDkKQ8tB8VRyfey7NL5A84Ry7KTCmxLbGBl7n5Z-9bfvPe5oZFgyWlTXpTkNhRcCY3MMOsQfx-CgWy4NUl0LRvTyMnXGQc-5C6b80YCLDDvL6sZQK8hvDrSH1ubkpqkjjnajBTgkKbhDYYm47bCuI6Oey3Hd_guJ6H4Q7ba2LeS6hYiEGFnZovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=jZPFSgFvLOpNxRWEtzWsTaZ5VuAfcb1PTLiJM_In1AmLYW8oyRiSq8KsTEPAwAUVQL5K5FZbS3eRy6KlNvIXx9qs0SvdWBP-PiO5H1nMtqvbeznS_K8w00QtXN3T5xL-Ro_7J6Wt3To8GYQVw_22xyeEnNX5nS2SDkKQ8tB8VRyfey7NL5A84Ry7KTCmxLbGBl7n5Z-9bfvPe5oZFgyWlTXpTkNhRcCY3MMOsQfx-CgWy4NUl0LRvTyMnXGQc-5C6b80YCLDDvL6sZQK8hvDrSH1ubkpqkjjnajBTgkKbhDYYm47bCuI6Oey3Hd_guJ6H4Q7ba2LeS6hYiEGFnZovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دیشب ما ۲۲ قایق را از تنگه هرمز بیرون راندیم. می‌دانید، ما کنترل تنگه را در دست داریم. آن‌ها کنترل تنگه را در دست ندارند. آن‌ها هیچ‌چیز را کنترل نمی‌کنند.
آن‌ها تورم ۳۰۰ درصدی دارند. حقوق ارتش خود را نمی‌پردازند. حقوق نیروهای انتظامی‌شان را هم نمی‌دهند.
و بالاخره زمانی فرا می‌رسد که ارتش و نیروهای انتظامی دست از شلیک به معترضان برمی‌دارند. شگفت‌انگیز است که چطور آن‌ها [تاکنون] چنین کاری می‌کنند.
می‌دانید، چین با استفاده از تانک ارتش این کار را با موفقیت انجام داد. یادتان هست؟ کشورهای دیگر نتوانستند. ترکیه نتوانست این کار را بکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71450" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=lpKf-Qds1kNsuLZjFG9c9bQ7zhqKnLjyhbtXRlDUUS27elMrsA-vVA3yBqbjNWi1GrkqZ7HdJcOrbOY4RF--CaiD674zSSMRYsDoZRFXDxtlGBJp3jcue6kZKA7nbgzzAiX_fI0p8I1l--tVtDEIPIXMk8_lYmY-Aw2jvYkw8kAX0NSB0F9R-c_sarPUhmBfYd8zLmwJeGfP8KFIZw_IQDZQeMGEtUr4U7DmAJX0rOGqlszq16tg3-0HEEQvfFZHXHifngXTwRcBUPM-asXQVNf3kRRaD66FXsGhzOWrQPorfMgiECQhsBNmhTwDLSb14W-Wl2WcA9VGZDTz-2-0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=lpKf-Qds1kNsuLZjFG9c9bQ7zhqKnLjyhbtXRlDUUS27elMrsA-vVA3yBqbjNWi1GrkqZ7HdJcOrbOY4RF--CaiD674zSSMRYsDoZRFXDxtlGBJp3jcue6kZKA7nbgzzAiX_fI0p8I1l--tVtDEIPIXMk8_lYmY-Aw2jvYkw8kAX0NSB0F9R-c_sarPUhmBfYd8zLmwJeGfP8KFIZw_IQDZQeMGEtUr4U7DmAJX0rOGqlszq16tg3-0HEEQvfFZHXHifngXTwRcBUPM-asXQVNf3kRRaD66FXsGhzOWrQPorfMgiECQhsBNmhTwDLSb14W-Wl2WcA9VGZDTz-2-0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
حتی نومحافظه‌کاران هم می‌گویند اگر قرار است وارد ایران شوید، باید تمام‌عیار وارد شوید؛ فقط بروید و کارشان را تمام کنید.
🇺🇸
ترامپ:
خب، شاید به خاطر انتخابات چنین کاری نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71449" target="_blank">📅 08:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=CBtoo1C8iI--k3gbZZVP1NU6ftAyyufBmKw68mgyR7KZe3dAYvjH7pq7-5KBbBc2ArqNwvLN290ZYrUoyFMzJE3jFcMbayCDwrxE7UhHYWR26Y4-TmcRDCE_GsHrBCaWRe2-s-IBawRnXIw-TForSkb7LXlUjbeVwO0VTRZFiauq-G-TBc5Teq14cKK-3UvA0VP2OxTTACNcuX8ztDAPGgTwMsY_OIZTNMD2R1vEuap8OlUaixDyAMlnpUwtSn2a2WblC-KhGzcsG5Df8f4L-hzAN-k12nApj9ivDTkskr0wAsBFRMxjNc44Ue4DIMJSvX82xFY-811eoke2nYbfPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=CBtoo1C8iI--k3gbZZVP1NU6ftAyyufBmKw68mgyR7KZe3dAYvjH7pq7-5KBbBc2ArqNwvLN290ZYrUoyFMzJE3jFcMbayCDwrxE7UhHYWR26Y4-TmcRDCE_GsHrBCaWRe2-s-IBawRnXIw-TForSkb7LXlUjbeVwO0VTRZFiauq-G-TBc5Teq14cKK-3UvA0VP2OxTTACNcuX8ztDAPGgTwMsY_OIZTNMD2R1vEuap8OlUaixDyAMlnpUwtSn2a2WblC-KhGzcsG5Df8f4L-hzAN-k12nApj9ivDTkskr0wAsBFRMxjNc44Ue4DIMJSvX82xFY-811eoke2nYbfPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ما توان نظامی ایران را درهم کوبیده‌ایم، پس چطور آن‌ها همچنان موشک شلیک می‌کنند؟
🇺🇸
ترامپ:
آن‌ها همیشه می‌توانند موشک شلیک کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم تعدادی دارند؛ هرچند بخش عمده‌ای از توانشان نابود شده است.
تولید موشک برایشان دشوار است. بخش اعظم تأسیسات تولیدی آن‌ها از کار افتاده، اما همچنان موشک در اختیار دارند. آن‌ها همیشه تعدادی موشک خواهند داشت، و ما [موشک‌هایشان را] سرنگون کردیم.
آن‌ها ۱۱ موشک به سمت ما شلیک کردند و ما تک‌تک آن‌ها را سرنگون کردیم. البته اجازه دادیم دو تا از آن‌ها رد شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71448" target="_blank">📅 08:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=rC4Qj21NeGO9YE6emNJXQBHaVRNS-ifnwiYU1HPLOoIuAAtBJazBWQ3YEyeTBJl84HETi6adT5Fw-EzoU4VLOBmoGsNDx21w1HbIBHQIpc1-jVV_52yfbT_3XbNKFmUKumc3Nvk2ZD9c0ejq7BPPebDW-qG-jtr6gZ0sZzndDC0LXRcb98DmlPTNE20BqnZcL0GKRDoT4DZwBhRinX5HZbus_R_BG8dda4tpgx62vxYTK1xhrM5-GHy5qssbg0dv4Yr7Zpl_ZIFS8YSYGYO72eWXf8aTCaw4lb1tokieH3JbMHtGtEryhYUVl2ywiLMrZiew8TTxs-uE_TQ2SWdL5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=rC4Qj21NeGO9YE6emNJXQBHaVRNS-ifnwiYU1HPLOoIuAAtBJazBWQ3YEyeTBJl84HETi6adT5Fw-EzoU4VLOBmoGsNDx21w1HbIBHQIpc1-jVV_52yfbT_3XbNKFmUKumc3Nvk2ZD9c0ejq7BPPebDW-qG-jtr6gZ0sZzndDC0LXRcb98DmlPTNE20BqnZcL0GKRDoT4DZwBhRinX5HZbus_R_BG8dda4tpgx62vxYTK1xhrM5-GHy5qssbg0dv4Yr7Zpl_ZIFS8YSYGYO72eWXf8aTCaw4lb1tokieH3JbMHtGtEryhYUVl2ywiLMrZiew8TTxs-uE_TQ2SWdL5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ماجرا درست پس از انتخابات به پایان خواهد رسید.
نمی‌گویم چه زمانی، اما فکر می‌کنم درست بعد از انتخابات تمام می‌شود.
آن‌ها به‌سختی و با لنگ‌لنگان پیش می‌روند؛ در مخمصه‌ای عمیق گرفتار شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71447" target="_blank">📅 08:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=Y3PW0ySCnWUJXmp9E7gqO8rfzL8T4eoinATxdmjZCioUytMNL2FRSfaHWhVTM04FP6pwW_r5cD6oe5A5M2SQy16MW2-XTR0-UKWRRoxH-XovKVxDQRXFVwo0mEyUGzNGDU5xsaPfV5ushEzRl546pTNdUkTysmekuUIboYDsDumXxztHAVh_3H86zyrYIL-oRptq1OqHvbZLunccwZvp-syryeE0OitSCDKFOoIJMjzmIwUTETw64-BZEsb8J-g44aqw-RAPZ4MpRYfGanDA8Y89wSupP0Xrd6DqPmf33byrqJUfDeoAxeRcZiYYBjqC3bKhbSu99uNrD7I96xowTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=Y3PW0ySCnWUJXmp9E7gqO8rfzL8T4eoinATxdmjZCioUytMNL2FRSfaHWhVTM04FP6pwW_r5cD6oe5A5M2SQy16MW2-XTR0-UKWRRoxH-XovKVxDQRXFVwo0mEyUGzNGDU5xsaPfV5ushEzRl546pTNdUkTysmekuUIboYDsDumXxztHAVh_3H86zyrYIL-oRptq1OqHvbZLunccwZvp-syryeE0OitSCDKFOoIJMjzmIwUTETw64-BZEsb8J-g44aqw-RAPZ4MpRYfGanDA8Y89wSupP0Xrd6DqPmf33byrqJUfDeoAxeRcZiYYBjqC3bKhbSu99uNrD7I96xowTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ماجرای ایران پیش نیامده بود، با خیالی آسوده به سمت پیروزی در انتخابات میان‌دوره‌ای پیش می‌رفتید؛ ۲۲۵ [کرسی].» آیا حسرتی دارید؟»
🇺🇸
ترامپ:
«نه، من به واژه "حسرت" اعتقادی ندارم.
آدم همیشه ممکن است کمی به کار خودش شک کند؛ چند نفری هم این سؤال را از من پرسیده‌اند.
اگر قرار بود دوباره آن کار را انجام دهم، دقیقاً همان‌طور عمل می‌کردم. من توانمندی هسته‌ای آن‌ها را از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71446" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71445" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4LfYYY8c3T0T8iTxeCo1KAD_1LWpSFCo6jKwxLE23k7ZRLcJr6MiDz8o7JIZbeUITvJTABHcgR2vBXW_5Kv4tYRpCh_R7shBwLCds5at15RE37TdqiBACTbgUnqMa1JGX4eix2zlTOxPj08jzuwQIAPtVc5QXd4FtTJ3BuRIDqlvmNmSqkJKSLJltUdQivOB5zxjJU_O4E94zOyhs0djoo0IQNuOrN9xfdrmJXsuvpJc_MRUzozR4P3bhg2BoySTcn3edNvq85fgDkKQ3jgy9poteZZ0n6bM8Gn-gWvvD9dqz3fnv-I_RRet14ZY0Ccn7Xpon2Td7HBejAkX7kxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71444" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voM44l24jMTwS-CtiNxhUkCYrIxqPenM64kCrf6_a9u_v-H0RsUzMVezsBsR6V2fJ_ouc4DS0FkKORbc5n8jRsRNLCfTE1ZhjtnBIqajxT2KC1Yl217DXvuxBXjcXVkMBzxKPpD9uP90eARGOc14s4PF95RC-bQQw6czvfCVKOQemYfCoaOPr3F1Ah2lOs3BjLHRk5k6nLY5jaH8sJ-RGYIHwGq3sVJ4ky1t6GkwC551yl3TPUflfTtyoyyUhS4Un_f_evHHgwOnLSYD4NGpWC4VwfmVWYUM4MD3hn84jMgj7OJhN3pdeMder2YYTt_D3ckjVVlTu39tbOe7Qy4qvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
🛢
بهای نفت خام برنت به ۱۰۹ دلار در هر بشکه رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71443" target="_blank">📅 01:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4KYWHUNiuW9UHWHrgoUrICA6OjJl6yHcQniv1Ng_A1e7Uo7F_l4dmblC7W0qNq43ukV62dznp1ugo49AAGZBQmsKudBWSBtoBI60_d0E3OFqP5FaYvDoOdlzzCfR2BmALed1e72idSI0wdu_Q-yY8-m2rEy631loBRbU6Q_pWTPLrwHVf_bANdb7S4inDlGrJZIlBwNBG_-_Y6QzpURYR3sd_keXp49Fn-ayTPCSI9I6i1YpXIeqlZnxtwucYf7Q-UkXC2ssU-yCT-UySX-reifWRI0WzxpH6pMJsWpfBh9CGoA6NbDOziacOfSr5uphRS-a16wm5JOr1pZUet2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
❌
🇸🇦
میدل‌ایست:امروز برای نخستین بار، حوثی ها خط لوله «شرق-غرب» عربستان سعودی را هدف قرار داد؛ خط لوله‌ای که نفت خام را از «ابقیق» به «ینبع» در ساحل دریای سرخ منتقل می‌کند.
تقریباً هم‌زمان و در حوالی ساعت ۱۷:۵۶ به وقت هماهنگ جهانی (UTC)، کانون‌های متعدد آتش‌سوزی در شش نقطه از مسیر این خط لوله شناسایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71442" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBZaPDr8F_SwnvcQ4nk68O-soZmSZdDqOI379eh-Nt8EvFOIPoIN2c9vqELMXy5lQi16Ie-OaNOPwSG3u6u1AqCsEl-PvO9ZeC9SW9aySAIBxkZxDGKiFK_tHNNciUVVRVyDTKNuibuFRuvPHRmy_MPM5e2gG4Rp_931ibRQa2yHxGjBgRcx8LBo8-ve2GsTeU0Gd5xCx2Bz6El6A6krUByzfdlmTJvAajJLVS8YjDque1YSvbssdfFAGp6zUY3z4pZ76IoocgL9Vmt-HycUKL35po1WBN_RtbvfqqPcRV1kJIwFBJ9OMncYO3IFWfv5Qa5qb6Ln2aSg9MIGhLNkMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
دو شناور در تنگه هرمز، در فاصله ۴ مایل دریایی غرب عمان، هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71441" target="_blank">📅 00:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⏺
🇮🇱
❌
🇱🇧
ارتش اسرائیل اعلام کرد که برای تخریب زیرساخت‌های تونلی در زیر ارتفاعات «علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تن مواد منفجره به کار گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71440" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=JutoQ-1XN3BS26IYzxYQ325Xcq5XRp1n2Q68rPJjGPhOwFQY_m3BVR8M_Eh9af3HWRpIl7HMGIe3Ei2CjFvEc_3lYSb6x0bb4uehcy7qb8rUMBTFWopjlTZA0txaQ2jOZeL9C8AaguEsZMj9oGp14wP_Qk_9YQq0fUiLnW9Ae-o0I_bclQbJVgI0JaNojt01KUCXBZUOLZY0oDBFidwe9mb4ULKH8uVZkFiQvc4t8W9t0b0X39TAt8PXwZh-WSWD3r-c_VgX8av6NlIvBp359vZnr-zAzzFbH_N0DWUyxUPuIc24Jbh2oK2x6ghmlqCvZ2nzamFmDxOG-xGnIASXkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=JutoQ-1XN3BS26IYzxYQ325Xcq5XRp1n2Q68rPJjGPhOwFQY_m3BVR8M_Eh9af3HWRpIl7HMGIe3Ei2CjFvEc_3lYSb6x0bb4uehcy7qb8rUMBTFWopjlTZA0txaQ2jOZeL9C8AaguEsZMj9oGp14wP_Qk_9YQq0fUiLnW9Ae-o0I_bclQbJVgI0JaNojt01KUCXBZUOLZY0oDBFidwe9mb4ULKH8uVZkFiQvc4t8W9t0b0X39TAt8PXwZh-WSWD3r-c_VgX8av6NlIvBp359vZnr-zAzzFbH_N0DWUyxUPuIc24Jbh2oK2x6ghmlqCvZ2nzamFmDxOG-xGnIASXkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئو دیگر از تخریب کامل پایگاه عماد ۴ حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71439" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=VA9uCp6rhnkhoW2CR9R1-nExkxVXWQvU28iVF3Duf_Lbq_yTuBueNaNzO0hjQYGI8jtIORVzuw1cL8xH92d65hpqmhBWmCqbqsEplpK9wAQ_pefSSgTbVGvPvyjjf2l-vMJKTwMbe1ZrEncYKRnRaSkoZmPR3Li8GApTZ3zF4r-bxrFuaZQ1eDdD_nHZrwpDJxVve1SXct4csC5TmGK4983rf5vlY168GF-kcOyo3gRoMYWnbeVWiY1QGLi9jk877k3AkjfSr82rsV3FR4K07FD4jjCfFQoDCb6i-n5VhlG3wn-4ClBwVAROs4-NFwuN6iVSwnll807V9mn_feSxvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=VA9uCp6rhnkhoW2CR9R1-nExkxVXWQvU28iVF3Duf_Lbq_yTuBueNaNzO0hjQYGI8jtIORVzuw1cL8xH92d65hpqmhBWmCqbqsEplpK9wAQ_pefSSgTbVGvPvyjjf2l-vMJKTwMbe1ZrEncYKRnRaSkoZmPR3Li8GApTZ3zF4r-bxrFuaZQ1eDdD_nHZrwpDJxVve1SXct4csC5TmGK4983rf5vlY168GF-kcOyo3gRoMYWnbeVWiY1QGLi9jk877k3AkjfSr82rsV3FR4K07FD4jjCfFQoDCb6i-n5VhlG3wn-4ClBwVAROs4-NFwuN6iVSwnll807V9mn_feSxvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
#فوری
؛ارتش اسرائیل عملیات تخریب تونل های زیر ارتفاعات علی الطاهر را شروع کرد.
تصاویری که لحظه انفجار تونل‌های زیر «ارتفاعات علی‌الطاهر» در جنوب لبنان توسط نیروهای اسرائیلی را در همین لحظات پیش نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71437" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=Gd4Z_HBIwTii8McMjHm7Xk7VqxJhj-Sx7NznxbxwclE-KC1yQ--kpRCSa2iw89Ld2OFG52CCFqWDIZr8eDfMJ2w7YXZ2rbx5hcnx5gPag96Vd-hpjVyCgIABQ1sLCQ95YEXY8_FSVTDaAalrDJNn3TfFcRThl6gWR0pKP4SMjkYlG-vjvtGUxdl8DODgw910SlDcs6qAO0JKOW5wQM8vzXVYe00lwFZWwCHfHeKdPzdB4wA0Oa9fw1f5f5KK_HwL6Xz9y5YKS2maxvPgyWnOEDl9tUKpKCrj8T4LBV_u-y6-zaS0RpIwBtZP7cvO8gIHM2M1_H5RmCKquej-rDC2Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=Gd4Z_HBIwTii8McMjHm7Xk7VqxJhj-Sx7NznxbxwclE-KC1yQ--kpRCSa2iw89Ld2OFG52CCFqWDIZr8eDfMJ2w7YXZ2rbx5hcnx5gPag96Vd-hpjVyCgIABQ1sLCQ95YEXY8_FSVTDaAalrDJNn3TfFcRThl6gWR0pKP4SMjkYlG-vjvtGUxdl8DODgw910SlDcs6qAO0JKOW5wQM8vzXVYe00lwFZWwCHfHeKdPzdB4wA0Oa9fw1f5f5KK_HwL6Xz9y5YKS2maxvPgyWnOEDl9tUKpKCrj8T4LBV_u-y6-zaS0RpIwBtZP7cvO8gIHM2M1_H5RmCKquej-rDC2Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
رئیس‌جمهور ترامپ امشب اعلام کرد که ایران بار دیگر در تلاش است تا به سلاح‌های هسته‌ای مجهز شود. این سخن درست است.
پس از آنکه ما توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را از بین بردیم، آن‌ها دوباره دست به کار شده‌اند.
من اینجا، در کنار «دیوار ندبه» و در آستانه «روش هشانا» (سال نو یهودی) به شما قول می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.
هم‌زمان، ما در حال ضربه زدن به محور ایران هستیم؛ نه تنها ضربات سنگین در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات «بوفورت» را درهم کوبیدیم و اکنون در حال نبرد بر سر ارتفاعات «علی طاهر» هستیم.
اقدامات بیشتری در راه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71436" target="_blank">📅 22:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP0tM7hUtjOMQZ4JMgGnPluYmcN0B9IZ4FMakBOUQ5gsTe-TQDnKkoPTKtKLowepcnng-IF6pwdc81kyvSO0HCxFlhFwuSv-9IP8lV4lnljJqjvPWCeWFWpSiHvWNjYdCCZkJgnlOkbCsZQ0MSBdSx8zZnFi07VlWNUovO117FFeuk9F9-kLNwplcLxwfWwOMn9DcJBlyyWVN7yMyHqyjuUCD3CBprvuBLvuKDYkrvAuw59X9G1W0cBwDFEC5QAKWESkOs7NGQ9wi0HNjBiOhTwYnOyLO89u6TvnFgwoPHuzYoM2XasLogkjyWdxk7ugnE0hqcCfoCZt7Mz6azHwAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=rS3jKjM6F9TavHqZnMa_rwqqlbyQyrqGi9dBlIaAAE8S2u2X8ODUNYGZqfw87XEWmTBfte2EbR44UbXwjTLH1-uUg-gV1joBsgkGqMc53Uy_1GkdQAzpd0-Q3NzL0XZK5cfUYREbJXry0KDHPXPWQTYMYjR_ur_mkJA5rxMO3l09ynWDCAGOV26KwOixPdCaOoPSUmDri3B6ave4bgaQiwzJTbr_y2IdTTqkSRFR_SE9JgY150ym0QJsA9QLzUhyy7AIK35IoeWL36qrAkV_KlfPMnBJtioM8w28flpI0g2a00WieycsV1x7YAGYUat8IeESUwNYNcDMq9DyiAaa8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=rS3jKjM6F9TavHqZnMa_rwqqlbyQyrqGi9dBlIaAAE8S2u2X8ODUNYGZqfw87XEWmTBfte2EbR44UbXwjTLH1-uUg-gV1joBsgkGqMc53Uy_1GkdQAzpd0-Q3NzL0XZK5cfUYREbJXry0KDHPXPWQTYMYjR_ur_mkJA5rxMO3l09ynWDCAGOV26KwOixPdCaOoPSUmDri3B6ave4bgaQiwzJTbr_y2IdTTqkSRFR_SE9JgY150ym0QJsA9QLzUhyy7AIK35IoeWL36qrAkV_KlfPMnBJtioM8w28flpI0g2a00WieycsV1x7YAGYUat8IeESUwNYNcDMq9DyiAaa8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71431">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=hbX5uhdVdBw8871CfAm6xC0etaBPUvsuvIm3F36VwJ_GhGFiK5ed7DOO2fH9-UJBH4hgiSEvxkvoFq2pBQBG8oPaPY8Dk16Gi4_lUykifrrrMMHNmmBWsaUWDcHOa3WrvgaJzBPJyOf3ks1my6wTp1WKgKiMBngrUor0sqt_rrt_6XiT7ajIXfdtvhZSbwjzUytPJMN4KAGW1GMu8UbAWxReIvW28NjVw4ZZWusm8Sd9Hem_ggkd-zKua2PCes7JhGjpR06q6rmIiV9GuWCKkOLkazaDQcBXOUgYLktjS88dEzKqnLwqdLyR2c8Ebrvy3vhJQ2AeWyBf9Tu4fT_YgpHA0ygPmWfIGRToUima9UJ8-vS4bfNWgpkt61Oh4fOYLhM6qq3IVKVY8Leo4jfZh2GZoUjnxGZxcU_EL0WGy7tfsiqXd73neBcqTMIIfI_vp_a6wFX8zJM-DwiNvfb0FL_UQPB64bBjDBjgF6uhqJJl5OIBIi_9lS8pshNYIiCjtzJbjD_6bzxCqwIDT2OItMbOSshfiypEd5jSPeHokdP0SFe8D7-s5qzWxh1PTVx7Jt87681PxqNV-9MWL8kqLnvQHyIpMcKweh4nmIElfvI9kPazkdluVTSYwpC-QHy8Ntj9kCkWQo333daa3pkhFapfcyxUEBlXhGwYi3GKmv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=hbX5uhdVdBw8871CfAm6xC0etaBPUvsuvIm3F36VwJ_GhGFiK5ed7DOO2fH9-UJBH4hgiSEvxkvoFq2pBQBG8oPaPY8Dk16Gi4_lUykifrrrMMHNmmBWsaUWDcHOa3WrvgaJzBPJyOf3ks1my6wTp1WKgKiMBngrUor0sqt_rrt_6XiT7ajIXfdtvhZSbwjzUytPJMN4KAGW1GMu8UbAWxReIvW28NjVw4ZZWusm8Sd9Hem_ggkd-zKua2PCes7JhGjpR06q6rmIiV9GuWCKkOLkazaDQcBXOUgYLktjS88dEzKqnLwqdLyR2c8Ebrvy3vhJQ2AeWyBf9Tu4fT_YgpHA0ygPmWfIGRToUima9UJ8-vS4bfNWgpkt61Oh4fOYLhM6qq3IVKVY8Leo4jfZh2GZoUjnxGZxcU_EL0WGy7tfsiqXd73neBcqTMIIfI_vp_a6wFX8zJM-DwiNvfb0FL_UQPB64bBjDBjgF6uhqJJl5OIBIi_9lS8pshNYIiCjtzJbjD_6bzxCqwIDT2OItMbOSshfiypEd5jSPeHokdP0SFe8D7-s5qzWxh1PTVx7Jt87681PxqNV-9MWL8kqLnvQHyIpMcKweh4nmIElfvI9kPazkdluVTSYwpC-QHy8Ntj9kCkWQo333daa3pkhFapfcyxUEBlXhGwYi3GKmv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جورج دبلیو بوش درباره افغانستان:
این باور وجود دارد که همه خواهان آزادی هستند؛ و ما این را در افغانستان دیدیم.
برخی می‌گفتند: «خب، آن‌ها نمی‌خواهند آزاد باشند؛ آن‌ها... می‌دانید، اصلاً تفاوت را نمی‌دانند.»
البته که آن‌ها تفاوت را می‌دانند.
دختران جوانی که برای نخستین بار در زندگی‌شان به مدرسه می‌رفتند، تفاوت را درک می‌کردند. زنانی که پزشک و استاد دانشگاه می‌شدند، تفاوت میان یک جامعه آزاد و یک جامعه استبدادی را می‌دانند.
و متأسفانه، آن زنانی که در مسیر شکوفایی کامل استعدادهایشان گام برداشته بودند، دیگر فرصتی برای تحقق آن پتانسیل کامل ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71431" target="_blank">📅 19:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71430">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71430" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71430" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGXATOQcicVHihW_91oI8Zp9OoQQqDl1TXBojAUJcNXopkKPPOXPUGI_igClP5jgK2RwGM0oACCLjhqxBYLw1yGKx0uQYjPPc_MWWOIrhVSAo3g_9TRoRqMhXFGFpAHwxb1kQPUOXDSmsv5pICDVZTjLyW6AyBCamqz0SfqHHNoaYy4zrOKAZO0HdrMPqsFg67ZVmBtKvGSn5FXdd8RkSCWIMJ_oAb8oBVZQtX0PpwojuhOrWZFm9VWrYRe2DHZdk52tVovgYzzIu9xwbIhinLsDbTg9wXVoXeEkAXcXn-evAGnlx8pDEhHx496lFZLOR-pAG9peOOsef0CyLC6X8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71429" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71427">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=B2xLcMXaYkrVzvTgOzkUKYfqoH0d_WJRd8k10LYmNFzErjrAy3lSROXMKQpwIJWAafLp34Y7ymcliIa3gLBactyXCFrFqKZzMVvpjw8BeHsBc-G5neXN3mZxl30fu7pbYoRHFgGK99JPzR0mYnih8gcxplrgiag18vCIUIb3N-yBgRxqhf4zTDw46pHB2aLId1w9XKhW9If2yoTiPK-xz0BDKMUs_bxaaKZ32ACMS7MqNUCNv2IkLJzRJh1ojEFszjO-b0JJRZZprW4TT3QdLT7HhdD1AD4chGEgCbbrCOnwLrnrvQw5i8-IUkoivD1wOSD3G_7btsk3VYt3Yj9_rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=B2xLcMXaYkrVzvTgOzkUKYfqoH0d_WJRd8k10LYmNFzErjrAy3lSROXMKQpwIJWAafLp34Y7ymcliIa3gLBactyXCFrFqKZzMVvpjw8BeHsBc-G5neXN3mZxl30fu7pbYoRHFgGK99JPzR0mYnih8gcxplrgiag18vCIUIb3N-yBgRxqhf4zTDw46pHB2aLId1w9XKhW9If2yoTiPK-xz0BDKMUs_bxaaKZ32ACMS7MqNUCNv2IkLJzRJh1ojEFszjO-b0JJRZZprW4TT3QdLT7HhdD1AD4chGEgCbbrCOnwLrnrvQw5i8-IUkoivD1wOSD3G_7btsk3VYt3Yj9_rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇾🇪
تنش‌ها میان نیروهای تحت حمایت عربستان سعودی — یعنی «نیروهای ملی» (NRF) و «نیروهای امنیتی ملی» (NSF) — و نیروهای جنوب یمن که پیش‌تر وابسته به تشکیلات جدایی‌طلبِ منحل‌شده‌ی «شورای انتقالی جنوب» (STC) بودند، رو به افزایش است.
فرماندهان جنوب یمن مسیر عقب‌نشینی نیروهای NRF و NSF را در کریدور جنوب‌غربی «عدن-لحج-تعز» مسدود کرده و از ورود این «نیروهای شمال یمن» — که کاملاً مسلح هستند — به قلمرو جنوب جلوگیری می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71427" target="_blank">📅 19:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGsIBaK72vzHYMs0jIiviaVPRwzmLg0tg4sdANwUZrpECCurWEvXov8-ry4p2zVFtW-cEqFoj_HWHTYYksf_ISmsL3r9Yqap2pUCWwvUDBflJaq5WbLT4-f_oVyzkHVFCjWJto3zkOpUMxVIT15omck0NBIKuEKs37Ar161Q8n_puoxtSBUvRibQ6zAtT9ef0FqRRAUZIS9zhTYXHldJc5KyBBQS2c7dWZ7VSNhbn3n2qTRLJSn4ktPzHGi8Skd4LWU_4K-D69ZrYwcg_PyGhFUIs-exxvxXPvBFCYPaCLVtNXtvOZBhnwx-Wb_BKJctPK_4QJAVvET5zL_bbQdpbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PiR32k64kGT_iToXRmkOD3RBHJnzl83pDsdcFRYp-T1K7hpWW-bifGFgSE2AVq9M3-orgZQE6HtPeUNvsa0j0ZnrbCL2dwmNkGsPBiUfoS8Fb3AXmDFGnZzuiapCGE-EUIwV0ypVENT56veZztVigxss8LVH4SwynxKIgvcQV1cgZUGSy-vAININAt6iQ0doOe6ddW52gC6qjoypg3VLfXauWuYYjeZkhE1k9GvrOxuiqb2biXryO_6CUqLzpmF2lBrvBhThJr9a62aXqng4xQNeWOGr0LvkYzqOtC63Ih82RB1IsKOjMc9ycPH9EY1qd9y26qAZLWaJdA6dDWEsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0_52Zo2uWiqkfEIQDGnfPmAU7xaDAHinWhnUVba68kOflw5UQR-j303ErwZZfOqSJ_AkO6yJcpEHWQ9H5nnElDbSfCeW5xcj1VMTgV4dPUM8XLm636BnqHESzypiT5Dpjvuyo4l7W2mT6sXSz275R2uASLgbzXmHJJuMq3NxVfNcO3V2lnZBxuqWobig9YodKF-6enbhuMEmY5EtT3iWbTOp9P2UdZ_aMHIpbiTUCDIPIbBHHIQJtzpfWwP6SFuBDImF2qam87cWuM4x0rYdkB11c3UcU7BTwIcluxW_NNIgQGmoQJGB7tGr5eIeqwmiwzWgGxm5pjkOHP2k1iqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=AhrEgmgVuCJliKoGNWTI0aZqUCPvUgALt9nJx6UIqujWtEi9RYffa-GtCAYK9sF0a8DbMl0QIetjqn1tKJXPhdBecPOJSpz-ww92RKRqrU6mpNMDlgjdYsdZVedsEounbogI-IWvHkOMHD4SeaT027q8xt3MbLRweUD11F5n33jxu0DGStnds73yV9zmnTm-kqXlrmMPp-aUDRraTh7MjemWM6WPO3AfTgtrcH_2CIU_soELQo5XUL3OMDOfLBBbz65pzS6GkSu1vhs6ySJWdOExrTDfDVgPWLjI4Ul4cO9DnP42Cf0vVCgnMFCRsvW51sghZHZU3nRNfAg5HodRRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=AhrEgmgVuCJliKoGNWTI0aZqUCPvUgALt9nJx6UIqujWtEi9RYffa-GtCAYK9sF0a8DbMl0QIetjqn1tKJXPhdBecPOJSpz-ww92RKRqrU6mpNMDlgjdYsdZVedsEounbogI-IWvHkOMHD4SeaT027q8xt3MbLRweUD11F5n33jxu0DGStnds73yV9zmnTm-kqXlrmMPp-aUDRraTh7MjemWM6WPO3AfTgtrcH_2CIU_soELQo5XUL3OMDOfLBBbz65pzS6GkSu1vhs6ySJWdOExrTDfDVgPWLjI4Ul4cO9DnP42Cf0vVCgnMFCRsvW51sghZHZU3nRNfAg5HodRRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=n7TtmIiLMeiwnbS93tnlQn6rfNEFO8ERP8ABXy8LXR8tqoxnreNPHTLBe1IcR-LfMvGcBQsj6KF66S3OhKde58hDNLYskRoQkcSwyjM2cVLajCWI_FMyhk05B9nC3j5cNgvyrHlVU0sMDUu65FzPUTPw4Bnqby4HwULsv0Zo9fb4lF06gGdj3qjcyfMt9dvoECiTaS--ksNNWhJo4NqN6Bi7eVEo4TsnKY8EftwoNGtGGe3ml40cv2UzR64D3kgn1YZAOjZTtyiUuKTpOZ4tQZD6kCrY5YnzMuraFeLSesOaSQE5i_ryuRxB-XfOpZ3auZNNAh0hFBy3zYoaE1FidQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=n7TtmIiLMeiwnbS93tnlQn6rfNEFO8ERP8ABXy8LXR8tqoxnreNPHTLBe1IcR-LfMvGcBQsj6KF66S3OhKde58hDNLYskRoQkcSwyjM2cVLajCWI_FMyhk05B9nC3j5cNgvyrHlVU0sMDUu65FzPUTPw4Bnqby4HwULsv0Zo9fb4lF06gGdj3qjcyfMt9dvoECiTaS--ksNNWhJo4NqN6Bi7eVEo4TsnKY8EftwoNGtGGe3ml40cv2UzR64D3kgn1YZAOjZTtyiUuKTpOZ4tQZD6kCrY5YnzMuraFeLSesOaSQE5i_ryuRxB-XfOpZ3auZNNAh0hFBy3zYoaE1FidQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=Bh2gJGbzPgdpkaLewYRy7fSklIotw0FlJKO1Cr2wSpOsIHf6yaEyFOFjG-fx0ZCOChfwbodMl9fTnRiwyb1o8dGmpe9Vev66HJZD20PPBWD7HeBCLElNWr_jJafkBkOU8PSH78XxSNSXQrugdIl0zRXNH5CllGEx5cf2oMW9uWlecp5YOEA454wyzGro6uLdUEey2RF3tVWqjoLYGmQjePU1srUzM5dT1xffu-VHOuoQmcKcSragxcI1EjVV0lmhODe09X3uzPuS8NhnJVWw3Chs_emsWaD0A7hzG3ETHw0ONBvysowhRTStIk5N1utslPR78pzkXSvUWO0NUK5PbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=Bh2gJGbzPgdpkaLewYRy7fSklIotw0FlJKO1Cr2wSpOsIHf6yaEyFOFjG-fx0ZCOChfwbodMl9fTnRiwyb1o8dGmpe9Vev66HJZD20PPBWD7HeBCLElNWr_jJafkBkOU8PSH78XxSNSXQrugdIl0zRXNH5CllGEx5cf2oMW9uWlecp5YOEA454wyzGro6uLdUEey2RF3tVWqjoLYGmQjePU1srUzM5dT1xffu-VHOuoQmcKcSragxcI1EjVV0lmhODe09X3uzPuS8NhnJVWw3Chs_emsWaD0A7hzG3ETHw0ONBvysowhRTStIk5N1utslPR78pzkXSvUWO0NUK5PbzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=NhT0Jv82NsWcE1MLvKMTH5ztGWTeco6PPltnukHhNxG9zXl50CvsNJyZ4XbmAr6gh10lL7_Eo8A-lRK6SH5uYqOPGBIwJx3YgzCcyBVbPJYDFcaRkJVfyw555i7Gl2bRJFBbt7PTrIA2PEhm_f4M4xXvRnvSh1LGGCzmwDo-LlRygO-445lL0Q6Q-HsV9nPyxAvFNWPx4dpNiq5No0TK9vXweLNWxi7e3wnRDJNXORnhYBpuFSl5-C6iAov20uPjHk8dn55_d0pz28-WcPEyqwrrjKOeww4qq1Pw6V24fV9dPm3zhAq31WMSCBtdTK_eDPwDb_aWy1GnkX7fsMgm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=NhT0Jv82NsWcE1MLvKMTH5ztGWTeco6PPltnukHhNxG9zXl50CvsNJyZ4XbmAr6gh10lL7_Eo8A-lRK6SH5uYqOPGBIwJx3YgzCcyBVbPJYDFcaRkJVfyw555i7Gl2bRJFBbt7PTrIA2PEhm_f4M4xXvRnvSh1LGGCzmwDo-LlRygO-445lL0Q6Q-HsV9nPyxAvFNWPx4dpNiq5No0TK9vXweLNWxi7e3wnRDJNXORnhYBpuFSl5-C6iAov20uPjHk8dn55_d0pz28-WcPEyqwrrjKOeww4qq1Pw6V24fV9dPm3zhAq31WMSCBtdTK_eDPwDb_aWy1GnkX7fsMgm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=jT9GG-3183MPBNNBH6AuoQE-BeOHesmNYOHLTUwaP6LPu_Zk_xhkT_TuaQlqoq9X5ifwZj0eypkmnxPkYREsAg84s3w3Y-IHmX29NL4C18cIn7vRZJEa5LEIMWYxgMmxNcvN5iL1wxX2VjoeWf09s1InQXFwyFQuTlok1YzqFkIGqU-49I2Tb5-Oy5M4w-o5odx6Qkjb3rfjXk2IhTGGbfE9jnEVZEKIRgNk3J_CluJJfF6XQMIyaKetwET38D7RwEmt8lqz737SnVD3r2-CuQLKqThd5smnTfz6Vk_d5Uzs8TNCqMWmccAZgrK4QVeSo8jJJquLHJE4V6ga9Jh95A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=jT9GG-3183MPBNNBH6AuoQE-BeOHesmNYOHLTUwaP6LPu_Zk_xhkT_TuaQlqoq9X5ifwZj0eypkmnxPkYREsAg84s3w3Y-IHmX29NL4C18cIn7vRZJEa5LEIMWYxgMmxNcvN5iL1wxX2VjoeWf09s1InQXFwyFQuTlok1YzqFkIGqU-49I2Tb5-Oy5M4w-o5odx6Qkjb3rfjXk2IhTGGbfE9jnEVZEKIRgNk3J_CluJJfF6XQMIyaKetwET38D7RwEmt8lqz737SnVD3r2-CuQLKqThd5smnTfz6Vk_d5Uzs8TNCqMWmccAZgrK4QVeSo8jJJquLHJE4V6ga9Jh95A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از مراسم ازدواج فوق لاکچری «سامان گوران» بازیگر؛ کمدین و مجری صداوسیما
سامان گوران ۲۶ مرداد ۱۴۰۴ در صداوسیما: نتانیاهو از موتوری جنس میگیره که میگه برنده جنگ شده. نمیزاریم آب خوش از گلوی اسرائیلیا پایین بره.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvLOP8JgoCO9Yr1Co9a1nv5BP3HGHH9Al-SKVlq1l_ja6SL0KN913lbc03qbKb9hCV9NwSH9hfuEL0KzFLR4SrunNWc5PJ2DKE5pOEljaAIz7SKd6PA2wYcHhS6kQgI9WJk8V_tSI5I1ctjiLZpTLxAjQELwxwotIF1-dL6u02tIcyIdZdz4wgOz_n8QZeDm8suanS8HCdES-lH1__zs1zeMMxafMkY4SnoRKeiFzz7jU0eOhZaLEVy2sDb2VTTujAQasyJ55W-TVWO9NsOaYox9c3nGUOvc5F5mwsB4fKzE2VfqUqb1mM4vK-hHRPd385jPQSojmcIdgouQ0FNN_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpYksPrgeG1ze_I8Jyz-kse9TiACRoLUT9BuN6CaW6GTl67BZNZ5jGrWDV1NRgZ1Gus9BfkGApV5hsmiojO2QD2m6zv5MIEUHjSUNUqBtHXkYf5k6pfQj8r9yyr6LMo2vd22HmIzGP83naYprXovfdeVdVsh70FSp0VRVFhGl5do1u9u-38UT51tPVu323jnYnreJWSAub8hG-hrIdCyeMBj7Nwgqem-McM_oVUhSHi5F-MUMTeBE3Q8_0JHpZjwE1PQzb23XM7pg2rZ6-ZCAKteiyyeA4VhLEKviU7sZvshbgW2jW9mANzFl2kFNuW70C-EzqLa0FOV3XnueyPdUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhGdJ9GddktX9G9OsdOMVz-0fdf7HG2nQIn3ucDiyzpUuxlZTQhxsAdFGLJqS4SGCkJm_vAKFY2JV-UWV8HWyeL2fgn1wySJX1WSz7a2L4xDXf54eAMIeR-nG2ewOEXwwfhb-lR7T2cBBIPuYlIQewNelJm6ZRSQP7BESXIxpJEpOrfCVdK4PiVObDGiD5-7bOuVmq4hSUB3mS_HngR5C8QKADDRya6dV0Ew8B_t4u0gJFGDmKy1qdWimEc6vep0w8rKlhI3m6L06l6NVSwhm1nZOQcszH08U8rFh0svPb86076LFCkyUvdbIIM2NM_Tgt94i9D8yrpQE9JjEHmo3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDz7BcGE5n8rxCYegs6Eu4cNg2yjE5-JusY7tUMZ81zqPYee52gHxUGCxZxHq2sMGezaFm9MYn-6tmSlghL2oCZlqUjChiV71BXV6oulSM329tCBkwgRx3p3cgNejH8wpbeSrcJAoZR6ZXKjmt4BvnMfm3zF_rv-8NDI4f9Jf8L4AZuJkH-Ji8d25x0vgvob5iiW4_60UlOI_zQDgLzsWg9nwvFt67mjoG8vZftMHXT_j1c8bJY9bRiegbs0RLVZvqDk71IE74N9mzQcdFpPO2crIFsPvScQEJHJNDFvYmOxxYUvipnHGbGW2y61RcMSyaWtMpbqgYq8X4w5MfWnTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=gNroqwKVBsbBUhv1oBY7fRod4TZ2PXi4Hi9H3q0FmgRRHkVeU5hFUtEK30EDQMfVrBc3IxKax0A58Muzo5evJ8crg706F7A8rh_kP494PG1MNOTjnF2ct_4VuQvw8IxkuJz87z3Jh1NfQOIzcK7-U2r16ZUEiM0ze0s7Y1kGsq3Ndg50fFbprvvHJfnN4gMkKVnunGTEZxm7imXelKxntHjR790Qx6bd8sUEd_3jeI2hv98TBRvuApLdH0FX2oSzpq4wACkR83CXF51IktJcOQwBHcNmKUnYOAzMlVAUrvpDHpHnEtAp5vSG4mX9ujmOfPirbI-qUORFTFH0WQQyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=gNroqwKVBsbBUhv1oBY7fRod4TZ2PXi4Hi9H3q0FmgRRHkVeU5hFUtEK30EDQMfVrBc3IxKax0A58Muzo5evJ8crg706F7A8rh_kP494PG1MNOTjnF2ct_4VuQvw8IxkuJz87z3Jh1NfQOIzcK7-U2r16ZUEiM0ze0s7Y1kGsq3Ndg50fFbprvvHJfnN4gMkKVnunGTEZxm7imXelKxntHjR790Qx6bd8sUEd_3jeI2hv98TBRvuApLdH0FX2oSzpq4wACkR83CXF51IktJcOQwBHcNmKUnYOAzMlVAUrvpDHpHnEtAp5vSG4mX9ujmOfPirbI-qUORFTFH0WQQyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:
به مناسبت سال نو یهودی، می‌خواهم برای جامعه یهودیان ایران سالی نیکو را آرزو کنم و برای آنها سالی خوب و امن آرزو دارم. شما بخشی از تاریخ پرافتخار یهودیان هستید و همیشه در قلب ما خواهید بود.
و برای مردم ایران آرزو می‌کنم که در سال آینده، ایرانِ آزادشده از سرکوب و استبداد را به خانه خود تبدیل کنند.
با توجه به این احتمال که به دلیل خفگی اقتصادی و فشار سنگینی که ایران تحت آن قرار دارد، تصمیم بگیرند علیه اسرائیل اقدام کنند، به رهبری ایران هشدار می‌دهم: هر حمله‌ای به اسرائیل، به هر دلیل و در هر مکانی، با پاسخی قدرتمند مواجه خواهد شد که ایران را با ضرباتی سخت‌تر از هر آنچه تاکنون متحمل شده است، هدف قرار خواهد داد؛ از جمله تأسیسات انرژی اصلی آن که منابع و توانمندی‌های لازم برای ماشین جنگی و تروریستی ایران و آسیب‌رساندن به شهروندان اسرائیل را تأمین می‌کنند.
به دستور نخست‌وزیر و با دستور من، ارتش اسرائیل آماده و در حالت آماده‌باش برای اجرای این مأموریت است.
چنین ضربه‌ای ایران را ده‌ها سال به عقب بازخواهد گرداند و رژیم آخوندها را بیش از پیش متزلزل خواهد کرد؛ رژیمی که مردم ایران تا این اندازه آرزوی سقوط آن را دارند و مشتاقانه در انتظار فروپاشی آن هستند
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJUWYodSYyNt80Ui2qM6_dGRB_tfbtzVhz6OoJdYb3qrLx4BEg_QFeOB0mGm615F8u3ZbYopSiOwFDRNKlG1P770U4ex8JKdfj7lsZ1vMbdikNYOyqnE9Usj2fClKtMSqM16pC9x3mWnUjp-qAe9KPxHjI9ru5FLPuKEOoB96M9WnStbcGixWaKtVe-PvSlVDjMRs1YgVxHH6SVyXVCsoNOk5XpG5B_tjoG8esTDPXn4UuFmXfwGqngdHnZIMVucfmM995-LjizyLq0uYBo0ObfgiLFPX7WoK4KO_9mkDyP17YAlS_qlyxsZ4CpKszoyNiQXMhmndtOycF_AOw_zqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

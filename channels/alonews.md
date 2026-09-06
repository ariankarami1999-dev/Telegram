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
<img src="https://cdn4.telesco.pe/file/E6cKWQOx-yDAbk-v8gzhJlDanBJCqXifrCkbS27-ovHnwsD0DB_3GjzFkgbGGqAHTErkPoq6Ge-GpiReSDNavJJxu2HS5P64PMp-Y71jlRBWXawHpFzRtVnqYtiwNGEsoJ463ongW-X835ElEprmG2s7n7TT4XODT-ZHu5YONY4lrB_uBRNJOFNp1xzAf8WaBhDWHa3cbe2H1cd9W1JoQ_eRk1smpTsOZOi7SEPahnyFeu-i0gbYeuG09vLsiKQ6sCBiYakcuGEnZaYf8G-cpnbUFbhNpyhsreTwvzXbx1m51DshrhgmdJpJv4sGqMmBbZQufdwas8fEmmy7bHr0Gw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 02:04:26</div>
<hr>

<div class="tg-post" id="msg-146014">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH3IwQDGgfwmtLGDvPs16SFEhb7_PtsI1KFLYKp7N6UXd3CEJhynd5YRiT84OJx0K9ZO_Jq-KVFaMg-ZoYThgzhsiouuPgm9SjXMZCEceSuPWEFevaeuEDUTdbYWB9Qnr6UlDACGLgpoVogHTyAHo84mR1PNrcOwwIVfkOo01bP3e9ZHFk_XB4laIsi_pdrfIKExyXFGcsOGzAnOME7lRyaItIjPHNC0q8hk6TIMT7pj1mI3z9eAErbi4jMZ8ps1NDbHFLT3_j2hQ4tSP2GlAqBNCaREu7GnnUzFxX15W1glDq6YdTHahieAXao-CHEOtk6KWgilPwVdKVAwnxjJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">LIT VPN
نسل جدید فیلترشکن
🔥
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
🔥
فیلیمو
و
فیلم‌نت
و
نماوا
رایگان
‼️
سرویس نامحدود فقط ۱۷۹ تومن
‼️
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کدتخفیف ۲۰٪:
IRAN
❤️
ربات تست رایگان و کانفیگ:
@
litvpn_bot
🔥
ربات مخصوص
همکاران
:
@litpanel_bot
🔥
پشتیبانی
۲۴ ساعته:
@mahan_lit
🇩🇪
•
🇫🇷
•
🇳🇱
•
🇦🇱
•
🇦🇪
•
🇴🇲
•
🇸🇪
•
🇪🇸
•
🇮🇳
•
🇺🇸
🇨🇦
•
🇯🇵
•
🇹🇷
•
🇮🇹
•
🇬🇧
•
🇺🇦
•
🇷🇺
•
🇸🇬
•
🇪🇬
.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/146014" target="_blank">📅 01:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146013">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEl9xrNiRGk9XSUFmDPaL6OoEep2Npx3SpAcdeQKStCXos-6rXBG6xnCiC3-kIaUXTWEzz8uOfjoRKFxYbeEacgtCrAm-ppepuz0R8WWWBLJ1mBz5-5vcpHfNCecprESqYCRHvWP_Ta6SMFRFhFnwdkafwEL2OUbMNSO6MNcgvXLiuKV8-T0hORyGmLtnOPXa-aZFlpHa-CQwgmNAfT84GGGWPvE_zfn0Eyfsrx_lryEc2uvJB_GwqcFcFMLPNH7HT5teFoymPIo36dTaR7hxsPFZOtDF5JavCNqUbiKtQ7RJwL2VVoWuqTXOB1kYCdk1kDoyl78IpUD-byN9HqA-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش رویترز، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دستور تخریب سکونتگاه‌های غیرمجاز شهرک‌نشینان در سراسر کرانه باختری را صادر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/146013" target="_blank">📅 01:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146012">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e8536959.mp4?token=CLNWunLZph812ybxhwJrrDem8EkWKxho3_xfxgiTxnVa79DeaPg_xjEP5FFfROJ-xPqBGe0WTrj8gWEUh8RugXZZ1BuVgWaIi1qA6KwM0s46vIwElQmmw9O-2eBOO-jfqE-Wq2Dgl-quTYK0iERek3vSl-VJqC1k9HIUwA5OznKUbX6DyUEYBIU80vwxeg6lv4SeLzccZ-s9mzjfXpbxNowqjHa7rTdXREqJNM4uv3J7sqfPoPxQFLHC_zRdOUpol_eUmv2N1IN5sKp-BJiYIlhqZm0EckqGmE0IVJ8i3quZvtVOQOQIM915Rt5CkxUqqehjn2T-_EK0sv8kQlmsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e8536959.mp4?token=CLNWunLZph812ybxhwJrrDem8EkWKxho3_xfxgiTxnVa79DeaPg_xjEP5FFfROJ-xPqBGe0WTrj8gWEUh8RugXZZ1BuVgWaIi1qA6KwM0s46vIwElQmmw9O-2eBOO-jfqE-Wq2Dgl-quTYK0iERek3vSl-VJqC1k9HIUwA5OznKUbX6DyUEYBIU80vwxeg6lv4SeLzccZ-s9mzjfXpbxNowqjHa7rTdXREqJNM4uv3J7sqfPoPxQFLHC_zRdOUpol_eUmv2N1IN5sKp-BJiYIlhqZm0EckqGmE0IVJ8i3quZvtVOQOQIM915Rt5CkxUqqehjn2T-_EK0sv8kQlmsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز: پس از فرود اضطراری یک هواپیمای باربری آمازون در فرودگاه بین‌المللی میامی و عبور آن از باند فرود، دست‌کم پنج نفر کشته و پنج نفر دیگر زخمی شده‌اند؛ این حادثه واکنش اضطراری گسترده‌ای را به همراه داشته است.
مسئولان میامی، پلیس، آتش‌نشانی و نجات و نمایندگان اداره هوانوردی فدرال (FAA) در حال ارائه به‌روزرسانی‌ها هستند، در حالی که مقامات در حال بررسی این حادثه مرگبار هستند.
اداره هوانوردی فدرال (FAA) در حال بررسی این سقوط است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/146012" target="_blank">📅 01:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146011">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/om9w1K7Hv7AqvpgnwKu31Yk3nj1TnOVvAe9TWWRzt0Qbe7wSPI4z9PbxEd9yLCrtv3MWWL_Hd1XAnPWANV2iF1BFUMgVMOZtJItBfvAo1sraBg6jsfwS5A0KKniTj5wdcQ7Gxf4v8SEdRdLvBrPmAbBwMNNk4knCtbOU6oQeVqqJyeFaH2JHhszOT550uP49O1LeBn-qO2KWCCakiDoooAjH6gyEs7tygY29dlZDysj1wEsKY4ISZ9s1atyzPgvxhy2g78i4qa1v0OdxMHk5ZVClJLhVBJsZWW59hnpI7y0ndNXDFXeXRxA9yYzqRvL58J7HYtyFnSzwcpqq3UTJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور چهار فروند سوخترسان به همراه یک فروند آواکس در آسمان جنوب خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/146011" target="_blank">📅 01:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146010">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/146010" target="_blank">📅 00:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146009">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f53489458.mp4?token=T4gZuX6gOAne1I1acQkAyrB0sXntqJhIcxJBFmRzuSBaQhvkrd5OgCSuNcqxw8y32xEh9H8ZFeeUQRUd_sslU4Om9vwzpk3OTjWmXcWyc5-_9J86VfJNhHYrswHzwjSNiQS6lMsgqmWZNYUhsDG2ErdKZfHNIS1q-yrbuYYSzPT9YzmMUv55h6UkwiY4B18apsV05NzIazWkIO1UD2VcEt4_euiG3W5UUy8Yw2byZwpP5KoXoCAsdWmnTuPTgL10dRq2iKBD0LMipaBbNS45EMmNya1UyEzClKN3JmttxyrKJsYbMIzVioiXkx6uPBfsJTfecnua4szvlIn9NwOzaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f53489458.mp4?token=T4gZuX6gOAne1I1acQkAyrB0sXntqJhIcxJBFmRzuSBaQhvkrd5OgCSuNcqxw8y32xEh9H8ZFeeUQRUd_sslU4Om9vwzpk3OTjWmXcWyc5-_9J86VfJNhHYrswHzwjSNiQS6lMsgqmWZNYUhsDG2ErdKZfHNIS1q-yrbuYYSzPT9YzmMUv55h6UkwiY4B18apsV05NzIazWkIO1UD2VcEt4_euiG3W5UUy8Yw2byZwpP5KoXoCAsdWmnTuPTgL10dRq2iKBD0LMipaBbNS45EMmNya1UyEzClKN3JmttxyrKJsYbMIzVioiXkx6uPBfsJTfecnua4szvlIn9NwOzaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلایه یک معلم از آموزش و پرورش:
اگه مدارس امسال مجازی بشه، از گوشیِ شخصی‌ام نمی‌تونم استفاده کنم.
چون پارسال 4 تومن گذاشتم رو حقوقِ 14
تومنیم و این گوشیِ 18 میلیونی رو خریدم.
امسال همین گوشی 70 میلیون تومن شده!
حقوق من چقدر شده بعد ده سال تدریس؟ 20 میلیون تومن...
اگه این گوشی من خراب بشه، دیگه نمی‌تونم گوشی بخرم.
آموزش و پرورش باید به فکر تهیه وسایل آموزشی (گوشی و لپ‌تاب) واسه معلم‌ها باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/146009" target="_blank">📅 00:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146008">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">💵
ماهانه بالای صد میلیون تومان تو خونه خودتون با ارز دیجیتال پول دربیارید !
💰
🟢
‌‌‌‌‌‌‌دیگه مجبور نیستید برای دیگران کار کنید!
🟢
‌‌‌‌فقط با یه گوشی!
🟢
‌‌‌‌‌‌‌بدون نیاز به تجربه!
✅
‌‌‌‌‌ آموزش ۱٠٠٪ رایگـــــــــــــــــــــــــان
🟣
این کانال ممبراشو غرق دلار کرده با سود ترید
جا نمونین ازش لینکش
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/146008" target="_blank">📅 00:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146007">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2s7c0CVIkH7uWlAtaDge4MTnh935BCwcvzAMFSOZFAGqZR2Iqe-LFLQ65h8ASnfeaYn4m55DDKj0hR2gGjj3UrmQ6w_Y8mrJ7PrzAXz1y30i4xrXhN8TWGOBYDLQaKZUqdVUsI8OdOZY4j7CQ2grTmd9o-1k6fZl2DlhKcDGI__SRpx14XLaPc8bz282RH3aRV4osNmOfm5p1gK1Oy77kDLvCiCyrq4-zsKL0_43nYYNOfQv0KApSKJBw8wJJthv0izVGCgwfb28hepUNztXqwQpO10z9Nq9HfR8vBAYk6IYb0g81VxFVAAzh1CJr5A-_VSqpoPrcMPNzF44HO8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار در تاریخ ارزش هر درهم امارات از ۶۰,۰۰۰ تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/146007" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146006">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
معاون وزیر نفت : تاکسی‌های اینترنتی از تبعات افزایش نرخ بنزین مصون می‌مانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/146006" target="_blank">📅 00:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146005">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
متاسفانه امروز یه جوون توی همدان بخاطر مشکلات مملکت خودشو آتیش زد و زنده زنده سوخت!  مامورا برای اینکه خودکشی نکنه، کتکش میزدن!
🔴
حاوی تصاویر به شدت دلخراش، اگه بیماری قلبی داری باز نکن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/146005" target="_blank">📅 00:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146004">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffcc64417.mp4?token=ng7AZfC99MSSYXIR9zvjdpE06wyWXFAJ1KGBI40DGdLLY7hnuFPOxIr7yPj1LywbSSRnNVbpfHZby3pCHTbcFGGjYL7XkRqPVnBokIxanzVJXEWv6aoTPXTISiapvsLtFA5tDsxzYgeVyZZn3Qpep4xJXy2wZgfu5qQpbzHDEU6ji8RJ85bJTpasWoyPqhixnTp_HoLQvKlX5XMnbglE5LSVuDN80Jeabfk8tBQbYTcCZkWMyhWKTETlptSiB0-cF5LJV-JgYsSqShMPTtiwq10tW9CGtf81KZEJr68wtCCzFT2VmQ_c0-xC48xA_tWZy1Qgd-E5RAz0EZQ-_PwkVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffcc64417.mp4?token=ng7AZfC99MSSYXIR9zvjdpE06wyWXFAJ1KGBI40DGdLLY7hnuFPOxIr7yPj1LywbSSRnNVbpfHZby3pCHTbcFGGjYL7XkRqPVnBokIxanzVJXEWv6aoTPXTISiapvsLtFA5tDsxzYgeVyZZn3Qpep4xJXy2wZgfu5qQpbzHDEU6ji8RJ85bJTpasWoyPqhixnTp_HoLQvKlX5XMnbglE5LSVuDN80Jeabfk8tBQbYTcCZkWMyhWKTETlptSiB0-cF5LJV-JgYsSqShMPTtiwq10tW9CGtf81KZEJr68wtCCzFT2VmQ_c0-xC48xA_tWZy1Qgd-E5RAz0EZQ-_PwkVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های انتخاباتی پزشکیان درباره بنزین
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/146004" target="_blank">📅 00:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146003">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAhM7caZOjMI4wFGqwixkscbWB8OIp4wS8sVBUzEloFAU7WsTu9ATuoHOTdQAjRwUYcGTKsdKDONaxDmo3_sUj7dNaDSo8I6OQGzUbYOvSIO3Emk5NjtCoU3Pmls8Uf7H_i1l49VNlTIegZ0NuVHFwzq-TOdLsEzHhNlOfhOj_YcssHSpN3jHRnKvPg0E-AkxcK_SJLeedm4nBRSBlYeLKU4ExUbaG-StQ_w3GkegeGYH0GwbiPDNxUB4g3LnkplO39jZtPPQmZhS1dm6TWhvwMjQJRnGuQV7CTuBLciIdgFYWLQvsT0qIbW2RKrkoqo8P7V87aKCWCFMBMxOyk2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی درباره قیمت بنزین :
هم‌میهنان،
جمهوری اسلامی باز هم با گرون کردن بنزین، هزینه بی‌کفایتی، فساد و جنگ‌افروزی خودش رو گذاشت روی دوش مردم ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/146003" target="_blank">📅 00:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146002">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
معاون وزیر نفت: جزیره خارگ در جنگ اخیر 550 بار مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/146002" target="_blank">📅 00:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146001">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p0OqQC0s0LwfPUPpXMTNpJw-wF3Ltv9t90_b5ulni5pkmji030Hza6ddPr6l2VF1_mY9Jbnp4ZtylVFhJ1pKyhgVi63X_g670AEm_Vt-raK6cK2Y4sZiy71-N5r4QwlIHItlDjy87TjF8Pytwv_u1Nf4ZGm2HWquOORWHc50Qp6XEYVZRcrxytom5rZywgqsaGHqMxs1djGdcjr05qgJMtZ-QlA_oqW0ezVELUXHP8iznxOsd-cHJlynA5ZkVeMPSoZX1E-_YJ1TrXPMMNkHSC5ljrklpCTosvyMKTXosL15gB31-GjsxCGeD9UZOT2TF7sy2Y95tjVf2coIefLfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاپ لئو چهاردهم خواستار صلح در اوکراین شده است
🔴
او به طور خاص گفت که قلبش با کسانی است که "سال‌ها در اوکراین در رنج و ترس زندگی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/146001" target="_blank">📅 23:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146000">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e2881c65.mp4?token=o93o6iSFlVKAx0_08psy7OEOEfxGj3BOIL97lfO9oU_aUnlrwiwMLAvDbmhvL2wHPaNFj4LdY0kYLyNXZdJM7jAFEkG30J5sltrYZPh29dPcNlkoGF3ioIN42X0zJMc8juYPoyjU7S45dXGy7m8rukQaci4CVQH1LebbLeKH4dwg_LT8KJGqoHHrzJmzoglEhOwh_OcWCpA6t6MeY6Vk-lk5RV0926zaYcgzhuLzR6C3y4Ahzdga1MZvQpwtn5hBLcQPmlc6rf7AqtUb2Zf9x0Wpq4agJ84ut8D9Okl-P1hUPmkAacqZjI4GU9wGlskR7shgJZRFOGJU_9JTKxvodKKHiw9rTCBw4IT0Xv5S9CHOAPeYU-WmZZqWY-VeMN3eRnDJF6KMKS7UiZLs0xog1GGkgwLJYEkJzUXETx-v2Z6rjGG5w9mDGW1KbJmZoYW0VV6iVll__bRjdLgxlRTa75JOhwKAgVi0eKAZmTVDW-57a4i21Kr3vD3GAqETO17S9ALalvO4WNKd0s8JKWwrB6O7i20scFUo5LeYvRBbnNHDqk9X98Rz_LdWZ9j32wAMX27lS9s2f7zigVAy8fdazkegMNgfDDT6JRfVqFChwaL5nFz7-9IgB8rt_r-qBvKCgLGxfZzPHktKOYmNfj1EnqWlgT0GRF9AFKcsOZYmlmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e2881c65.mp4?token=o93o6iSFlVKAx0_08psy7OEOEfxGj3BOIL97lfO9oU_aUnlrwiwMLAvDbmhvL2wHPaNFj4LdY0kYLyNXZdJM7jAFEkG30J5sltrYZPh29dPcNlkoGF3ioIN42X0zJMc8juYPoyjU7S45dXGy7m8rukQaci4CVQH1LebbLeKH4dwg_LT8KJGqoHHrzJmzoglEhOwh_OcWCpA6t6MeY6Vk-lk5RV0926zaYcgzhuLzR6C3y4Ahzdga1MZvQpwtn5hBLcQPmlc6rf7AqtUb2Zf9x0Wpq4agJ84ut8D9Okl-P1hUPmkAacqZjI4GU9wGlskR7shgJZRFOGJU_9JTKxvodKKHiw9rTCBw4IT0Xv5S9CHOAPeYU-WmZZqWY-VeMN3eRnDJF6KMKS7UiZLs0xog1GGkgwLJYEkJzUXETx-v2Z6rjGG5w9mDGW1KbJmZoYW0VV6iVll__bRjdLgxlRTa75JOhwKAgVi0eKAZmTVDW-57a4i21Kr3vD3GAqETO17S9ALalvO4WNKd0s8JKWwrB6O7i20scFUo5LeYvRBbnNHDqk9X98Rz_LdWZ9j32wAMX27lS9s2f7zigVAy8fdazkegMNgfDDT6JRfVqFChwaL5nFz7-9IgB8rt_r-qBvKCgLGxfZzPHktKOYmNfj1EnqWlgT0GRF9AFKcsOZYmlmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی: افزودن متانول به بنزین به صورت گسترده صحت ندارد و یک دوره آزمایشی بود که تمام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/146000" target="_blank">📅 23:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145996">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XX8hMzzszurFD6ZmRj3GHXx2sByrvdDP0Am0LzSmJUMVNp26APlKmrh9Ukotz0CSGM3-a0L0P9H3fWX_UBipmqRxoze0G_eEyOQwjz2gRq9lUP4_BlTX3thwI4xQMgNYEtkEeE7nG8biXq2EsR4OME02DwHZtfr1hTMKUUh6f_5IP_9XfP9abPViVEKEg6Er8XqGWHiY2yRLOphQTgaVR7YRv7YttDSi4RAX-Un_JjxJGQ9mFYqHyOrabzluKXWsQPSnE8qkviw0IkOgu9vREHzSce6OAFybazjFxtj0CpiCkIlbq1GDMjFn1-1K2DhEhYUXHhdJFq7KvxQ8ibq7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8-82bWOQ9Sx41XjzG-24m2iReN82CBl9mHjMlyM9PC1mmz5tcx_-GHQ0QjAb6sMxQEBQrNT4-jDdrZ6PuNnZhTSjNZwgE3LoJPUaYS-YYA0y_1SBCD5NulhQQ8_u-yKXGLRmP5gRDzu5Q5mh5f2tjD5ax02czIBNTYpBRkEfRk2NP-w-V7XWqOVLwUWG2pC43o6r2nnrvl4zOcv_GFFh-rkmNkVUzTXpGHC6RRrhbS9ZobZoVfH4BcCoBNT8ArsReaBhkTIVtcAFFVrjEzM0h_KosSTcBkSc3PW9_qZTPInkbl53Hdb-1o8Gr0dgqqTW48gPNubqjtLDGuyqaNcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYMDZZoQB2TVt1PuOWnLvbS9CqCQx2upZ5TEDuQmZS4usl-ikOUKIb7KdOLivYtSi9z5Cd81paZj5K3vJ8z1-hUfJzX_b1ISwxLKxvy82ujreGnxGGTxVOzMvVOwIgUBE9cHfgyCF49dKgMeST76nw85TKVvk-VbbuF2MusUaNBwh2sWk5qY1QM48b63NIfEkSn9mvQaOZC5_ijgbbZ881hyo-9ua6qALa8k99MN_b5l1qU1VbWoD_kQdDD5d4xRSWu9rjlmaBTgmwhTH8dQBiZ46INXt8d5bqgA7yU7B9RXs6HnXcGDw8AhabRkCWSblytSy5c-hbnh9_1jqWqTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJA15-xi6BXkQuIKmsfkxHZkUzl0kh8kzoqnr2VukwigtcFn6a1hCLqmV4hskfWQThvRgqp_8zJVfPuVdbRox8OpQUCzrsM_CwsO31MJV0xfr80a1fGnYPaXT7EQxhHvlhmcHj3x2Qw_Q00HY0kanhHR2YwcuD1WONs1d6LSwwR07TATjwm34n_wmCpy3n7OSpINQfhI4Fx_uQzvGCLweHBQeJC2tRfVC_RUHD3i4inQAhb_YXOVfsuARjFYjNJ1B_8l0-FcJtpIJTWY-h_J-0k5Uz7_DXGZuDQyqjOcnYD7GOQOzzLt4PyVQcWasQyN2ln8Yp8wguu3zH5hywE9cA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ
...
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/145996" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145995">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c4b43fe31.mp4?token=oc7r8hJmsnzEu5bmzSd2GTMjqpWcH7f4ZYj15A8qfmsjbxZWKd1eTtKNOmsczxc1wPRya1zYJCOMPDOkSLIu6cKtze99N-z9CszkfpPdBXpUXxdpU8_iV-C_jijIDDyyvRQyIIxK-Wu32pJFunNTGMv3M5pKVzaMjrcH_isIDM86jon0olQEQNVEKDCujwyWgHO9QEjy_72A8Dv835M6AahvkSrPULAVLd5nFlRgcKDi7Jt3aHcsO2UdOWxvLY7PxHrWa7mhjo1_Yl1j20iRvwupA7SEgVd02M43LTDOFgdYf0008Xe2ySYHTx2aH51OhtbEbgzSE1CrYlD9s_nnJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c4b43fe31.mp4?token=oc7r8hJmsnzEu5bmzSd2GTMjqpWcH7f4ZYj15A8qfmsjbxZWKd1eTtKNOmsczxc1wPRya1zYJCOMPDOkSLIu6cKtze99N-z9CszkfpPdBXpUXxdpU8_iV-C_jijIDDyyvRQyIIxK-Wu32pJFunNTGMv3M5pKVzaMjrcH_isIDM86jon0olQEQNVEKDCujwyWgHO9QEjy_72A8Dv835M6AahvkSrPULAVLd5nFlRgcKDi7Jt3aHcsO2UdOWxvLY7PxHrWa7mhjo1_Yl1j20iRvwupA7SEgVd02M43LTDOFgdYf0008Xe2ySYHTx2aH51OhtbEbgzSE1CrYlD9s_nnJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متاسفانه امروز یه جوون توی همدان بخاطر مشکلات مملکت خودشو آتیش زد و زنده زنده سوخت!
مامورا برای اینکه خودکشی نکنه، کتکش میزدن!
🔴
حاوی تصاویر به شدت دلخراش، اگه بیماری قلبی داری باز نکن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/145995" target="_blank">📅 23:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145994">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thxnqaNEk81q1A1rkjrgEiqO6UiVPBRUgjDMf4DB0VkewY5-0KW1DkUrDzOUvCRK5exfjXJm7eruU2ExzjrMcQjzQN_BNDoNmiUyhS5mT57kbhcpnjup2HU2a8tb_C7YAoUnzCHvLByw-WeVhYjXOecbUVP2Aoc131iqK_tbN3vOSPL8FgXACTYcqlVMOOkk8vCt3vMot_7dAhIrJTc-fZ9Sv5yT9q1ZPNdyfNTp_vAmazySBiTyk1c8bKLdzt2gjhJCmQSLwgFZyJSQOiraIH70fnpzwPftgfsTQc1RMR4hCXBJT-rjjTPMHSPquHIKLmby4S84Rkzv9yf2wSyXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : ایران یک کشور در حال فروپاشی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/145994" target="_blank">📅 23:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145993">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNq_hQSVpHaosaeyJF5my0bAd4nPySiZyrqq1rJd_z7ixXbq2sLRUtk4_dXrh1sa8jXq6b2uGIV52r9mwexAPIIkOtNL6dYFETmZx57PTNA8Qs4HbRSY1peb9UE4PoHYn4MY6WQ2C26jJTx3v2V-FpJR9-ezOImQVonCZ7y5o8eVhfwMBFRfd2x8X7_RhU4xeNJmjAnTR_sM3IjeF3KnbO69K6wemCDaR2NY0AAlmiC68PwMVnl-GjmoAahbBztmbdg2QBghclZ97buK5L3HWaX-YK1A5twzON4jPB7DKJcyOCcqDp2Gk8xhNP1LtEIX4vOLZT9CuPtRQ8OV4lhq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب اما واقعی
‼️
یه دختر مدل اومده چت رامین رضائیان رو منتشر کرده که رامین بدجوری التماسش میکنه تا عکس نود بفرسته
😐
مشاهده عکس‌ها و چت لو رفته
⚠️</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/145993" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145992">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
مدیر شرکت پالایش و پخش فرآورده‌های نفتی: قرار است یک روز در هفته مدیران دولتی ملزم به استفاده‌نکردن از خودرو بشوند
🔴
توانستیم با برخی تدابیر ۵ درصد افزایش تولید بنزین داشته باشیم
🔴
افزایش قیمت بنزین به صورت تدریجی انجام می‌شود تا امکان انطباق برای استفاده از سوخت‌های جایگزین فراهم شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/145992" target="_blank">📅 23:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145991">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
معاون وزیر نفت: تاکسی‌های اینترنتی از تبعات افزایش نرخ بنزین مصون می‌مانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/145991" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145990">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f556fb6178.mp4?token=I_hri2zi626UsaAtKuvOdtQTcbF0ZmekIMZMVeyVEvAR9XOYHCw3J6MajNNiC8fSU6NsJBkCioFQPar2KuB4na67cvjNxfj8Nyg3mPgWYzBVx6j7HS1gqPOHBk1vgMof1l5zACwd_HD6Xjzm_fZZ1WSrI_hJGUz8TJWyOIapEnG6rZo_MLjA7S0YwVogRwRS4oXVXeNyHgHjL8VpRX_GFu0eC1CdoJuZT60eAPBmRfHtjn_s0kuOJZuwP5GYu0B1otp-R0A77MpJFLX7ytl-ksf5smvJdnDBA9yhicNgujxrUGnc8gKz8PPAfb3uQDb4EPPcA8KTdi4yxwQomZkrmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f556fb6178.mp4?token=I_hri2zi626UsaAtKuvOdtQTcbF0ZmekIMZMVeyVEvAR9XOYHCw3J6MajNNiC8fSU6NsJBkCioFQPar2KuB4na67cvjNxfj8Nyg3mPgWYzBVx6j7HS1gqPOHBk1vgMof1l5zACwd_HD6Xjzm_fZZ1WSrI_hJGUz8TJWyOIapEnG6rZo_MLjA7S0YwVogRwRS4oXVXeNyHgHjL8VpRX_GFu0eC1CdoJuZT60eAPBmRfHtjn_s0kuOJZuwP5GYu0B1otp-R0A77MpJFLX7ytl-ksf5smvJdnDBA9yhicNgujxrUGnc8gKz8PPAfb3uQDb4EPPcA8KTdi4yxwQomZkrmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی: به طور میانگین روزانه ۱۰ میلیون لیتر کسری در بنزین داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/145990" target="_blank">📅 23:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145989">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی:  تفاهم کریدور جدید تنگۀ هرمز که ورود و خروج آن با مدیریت ایران است در روزهای آینده امضا می‌شود
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/145989" target="_blank">📅 23:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145988">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6coTCCzeJaLjRPw89RhHDm93tCe2cO86kiJD1XjFJUWOiIjrT64WNWq8KnD5ixUEF8X_vM4y2yAeVrDqMuIHI3KpE-2B2f6qGjqc-kkWaMV-2t4PbgVc8J4Zs-aFS7r_lTGo49HvS60hi0P-oW2RUNVJUpO5eQdQPOWADk8KD03pEQvHVclm-zhoIr1jcdt5jUSr6L2QRcsihb93jQFI9DKeNziR7Pdi3mfIGKJkTg3Dd-ADA3j0J2ZO9sflBOGYmTJHeLxZQ8gQcw88wyAtOv1VoOK619Ie_4cuyZflRoXOjvRHSvE58XlM_VrJdN4jVaRwetcxZb31ODea0Csog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : من این کار را برای کشورمان انجام می‌دهم، نه برای خودم.
🔴
من صدها میلیارد دلار از طریق سرمایه‌گذاری در سهام و سایر دارایی‌ها برای ایالات متحده به دست آورده‌ام، نه برای خودم، و تنها کاری که انجام می‌دهم این است که مورد انتقاد جناح چپ افراطی دموکرات‌ها قرار می‌گیرم.
🔴
این بسیار ناعادلانه است، اما چه می‌توان کرد
✅
@AloNewd</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/145988" target="_blank">📅 22:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145987">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTkn2sXqsB3ytpcZmbZOJjDsNW37qguFow8UJ1v5Yu37n_J8QwdknU5ad3DSihpeau3brhhqRvqNQu630n656gEAFrGKU61R3KgHXK0KgIGx4g8fwe9D7iUznWTxFX3blv0vStV9OxpMrU19kw5cEvlif-zEIXLoRTMT7K59BCCMNlDaEr6JjNxeywLrFrfTM2_jusnbFxlfwVwWJFdT5pb6K5A6RBoo2X8S6CQBqLpXgcoadyQzyo1B7e-o5G_TJmin4Kc6Qbi5el7VI5d02uzurDMYsun1M7K8bBEvTYOHRO6T3XtAq1QsDceexSSSXLYf1yhct1HP-8p_7I2uoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر رفع فیلتر اینستاگرام تکذیب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/145987" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145984">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kopgMqE-NrlWJT7GksMy-li_UfkLOn2sMM__Eyt3GGi59puSiyYg3Gcbp5W2MSooRLB1T2atqdJM7vKvG6NGDhBWqqWo8opqmzxM7FDUyUYterpU4KoDi_WpbMbf76sUY4rIFLMYO-R4LTH8Yf7nzaGLhgqppP6P1POc7gcmI35bqv8lKPfOidcOfdIuxtuXSJXaF7bGf_IqRosrgJbTfC1tDlRjA5kcn--Qw8GMlSH6fnHLiZ9ESc6JHgLZ2q-V9_9bYL2dDJVv5XOGLUFyAmLbmYiCfU5mSard9ude_yehi18vqh52J1qUR13U8FXYsp_mzGqVVWGljeTt9Rkn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOgmJAJ5QBMxElXs0oSit3tXiaQjvY1hbJm7Hmn1zkj3tNUHmAzm9mLU_ONA2HR9lqDYrtB9C-tzL-_x0FUrkxPYTifzHMyaLuI7Fe5TydheB5tAViagwIf9rwl6NUBU6TS9haGKJ-g84RM1mjWlmhsSBiL_6iprc_m4fj1sp-2DyXsHCqHqN_A1SqGIYWf3dBGf6okgbYW7Uyme5Eqc1aVLE9wllzZZHubVfAttw17QO4RTv1QkCOdY0IhUaxW-v3vTmro8pMuYHIPo18gQI22A48-sFLtTyW_tGPysNJjwAtfZFtmynmdVa9wluMXVDe0hbzstcc5JcdLT0cSw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwpOyLGxCOR7xO0fVpPnDxDEyO368RWl11QEeDcN7EtJoh2RdNUlsnt6d2Nkn2Q6w5BP7ow3OZO2PsQ8jFRBAB5dlRWZdKdAI1V_vDrFTBQ6KmRGwqsigogPd4_lTcco2en2syvFJDsb0qfpexE7hzIMOBwWGVtBhT3wsmsSYFciQOLCbWJaD6zbt2mNVtUdnbRmi63j2e9BQDPYaTEpNzLWFkYbMZiXsnrrV38TAgeidn2NkYW1SQC0BXTac6QmL-MHChrTR4m2HMuRUAx96BAeJe1cgMFTrnY0PJ8QG4dfjw2-ur4cusEATPyuWzWQT95trUaO-1NlDJsMCXtqaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ درباره سقوط اقتصاد ایران، افزایش تورم، کاهش ارزش ریال و افت صادرات نفت ایران پست گذاشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/alonews/145984" target="_blank">📅 22:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145983">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv1O8oBrYDVyMr3_kMJJNqDoTK6Dytkg0FyGjgzVW6UphN03gfvs-w8DzOUbTbtSj3nG07817b1IYaR0kZlHp60yqyEDmvhpJ_PRteOKIqq6USYxJe6z1CGh0ZqrdHn_Nf-jeRGbBGG5nrIovUCynZP-DMsXD7vFFEqQsjpk6Os_jeZm_ZDxRZ_i9Y26Kx8kxU46VBVORk-1902AqzpC5AqfkS7fbvJsgaiX_3kUHwB2ngXoOgGj9iM2klpFxKVnotFqHtnJ52G3zt8TAMwXMG_VS8piOczm8pw2Ws89Jcx6penDulajjL4uRvD2e9bzJENN3J_hNQxl4AEvQ11lag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث: بای بای، خارگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/145983" target="_blank">📅 22:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145982">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
محسن رضایی: لبنان دوباره قوی میشه و اسرائیل رو هم شکست میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145982" target="_blank">📅 22:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145981">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فیلد مارشال گویا از تحولات خبر نداره و فانتزی‌هاشو داره میگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/145981" target="_blank">📅 22:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145980">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
فیلد مارشال رضایی: نیروهای مسلح  پایگاه تیتن آمریکا در اردن را به شدت کوبیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/145980" target="_blank">📅 22:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145979">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فیلد مارشال رضایی : زمانی تعهد می‌دهیم که تنگهٔ هرمز باز باشد که آمریکایی‌ها خرابکاری و حمله نکنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/145979" target="_blank">📅 22:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145978">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
فیلد مارشال رضایی : اینکه گفته شود محاصره اقتصادی آمریکا عامل قحطی بزرگ در ایران است دروغ بزرگی است.
🔴
دولت ایران از مدت‌ها قبل به فکر بوده و به اندازه کافی ذخایر مواد غذایی و اساسی را دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/145978" target="_blank">📅 22:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145977">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da6516527e.mp4?token=AfVIbUyI0SfwzQ-Arx8I4lFueP7FEvnMbrJtjCGceWMtMKYtr_S4BkWqXTbwgSdOhBatZ58LtnPxFwSjR6htoZv_urfm5rpt3B7Gk29ZAYBc5XPs55v83zawLTBAnDJ_kPg7_E2FZEK9VnCdOtBvatuOlTH2u_CqCiuH1xDTujtvntvyZau7ScwXXLgaEaGhwkBJd66oEnFO9DvMLus9Oie-4cjoORpr2atLV85bDYpOM8f636sScRlmavc3qTGhX-UZFe2c1AjQzx7U8KywRzQLNTGYcU7s6zLq7RWvhpyOhqtXoDRqxexx1aB5qEVpxHCe6_LqsixRjlkGhvnHvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da6516527e.mp4?token=AfVIbUyI0SfwzQ-Arx8I4lFueP7FEvnMbrJtjCGceWMtMKYtr_S4BkWqXTbwgSdOhBatZ58LtnPxFwSjR6htoZv_urfm5rpt3B7Gk29ZAYBc5XPs55v83zawLTBAnDJ_kPg7_E2FZEK9VnCdOtBvatuOlTH2u_CqCiuH1xDTujtvntvyZau7ScwXXLgaEaGhwkBJd66oEnFO9DvMLus9Oie-4cjoORpr2atLV85bDYpOM8f636sScRlmavc3qTGhX-UZFe2c1AjQzx7U8KywRzQLNTGYcU7s6zLq7RWvhpyOhqtXoDRqxexx1aB5qEVpxHCe6_LqsixRjlkGhvnHvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: در روزهای آینده یک محدوده ممنوعه خارج از تنگه هرمز اعلام می‌شود
🔴
این محدوده از خط محاصره نیروی دریایی آمریکا شروع می شود تا مناطقی از خلیج فارس را در بردارد.
🔴
هر کشتی وارد این محدوده جدید شود در فهرست تحریمی قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/145977" target="_blank">📅 22:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145976">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74089a78df.mp4?token=kXXgVI0-HGujxW6dymYEE7GTMRC4qTxJvJE6a4H_VjilzNxeusgu546MYDAwda4MNx-o-blV5ic_jUwVLvWZwim0y57h52U_5cm2GBn7mXJDb-pJvtMxQyNTjJfUsBSMm-OCn9V37o0beoiGqFJi-HPW3phAdVQ46RAZJV6PJPsbbXuPRfl0rrhT0pmau3Pp6EKuxZz17WdH0bCJT8LtbH3SjPoRBV7Ud3m9xAql_tFp4EwgJmSF-EzfW-Dm4We0nsvn8Bl84lxuhR_mwtUtD-bQ6f7JiAM6jBT4oUU50UfzoifIsG-jZnLlRK-7Yyng8QgeIGOvij-OhV4ioGXtVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74089a78df.mp4?token=kXXgVI0-HGujxW6dymYEE7GTMRC4qTxJvJE6a4H_VjilzNxeusgu546MYDAwda4MNx-o-blV5ic_jUwVLvWZwim0y57h52U_5cm2GBn7mXJDb-pJvtMxQyNTjJfUsBSMm-OCn9V37o0beoiGqFJi-HPW3phAdVQ46RAZJV6PJPsbbXuPRfl0rrhT0pmau3Pp6EKuxZz17WdH0bCJT8LtbH3SjPoRBV7Ud3m9xAql_tFp4EwgJmSF-EzfW-Dm4We0nsvn8Bl84lxuhR_mwtUtD-bQ6f7JiAM6jBT4oUU50UfzoifIsG-jZnLlRK-7Yyng8QgeIGOvij-OhV4ioGXtVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محسن رضایی: هم نفت می‌فروشیم هم پولش به ایران بر می‌گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/145976" target="_blank">📅 22:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145975">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71c571fed.mp4?token=XKPKy_uRJTdJGhS99JyXAkKAWZgydWx7uKX9aT4fGter1kJ8sQs0raWfkrnuHi5RDjmHo9XG-97VBXkoYBS_Jgt3eTgXh9iCLTlNhB7mmSpwFwCVsPB5qC80gihCxR5543K254j6L8GUUD_CnPe781XaRgNzNO3FO4Z-yrPE5gXC70RSq-mzW4_jxJJpSJ9kIGRXF-2pH2Gb2Q2XSD5pu7PLOAYCAg8ub9vZ5dnbeWHTHnqrVUxauhPBazVff8nAKxEzA7QmNRPM4aL2mGXH68xCQ9mCqzZhOaTGbFBp-KisKW7WwUuO4sUTQl65zlIRk9VB2vzvZ05lX2ikFgK5vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71c571fed.mp4?token=XKPKy_uRJTdJGhS99JyXAkKAWZgydWx7uKX9aT4fGter1kJ8sQs0raWfkrnuHi5RDjmHo9XG-97VBXkoYBS_Jgt3eTgXh9iCLTlNhB7mmSpwFwCVsPB5qC80gihCxR5543K254j6L8GUUD_CnPe781XaRgNzNO3FO4Z-yrPE5gXC70RSq-mzW4_jxJJpSJ9kIGRXF-2pH2Gb2Q2XSD5pu7PLOAYCAg8ub9vZ5dnbeWHTHnqrVUxauhPBazVff8nAKxEzA7QmNRPM4aL2mGXH68xCQ9mCqzZhOaTGbFBp-KisKW7WwUuO4sUTQl65zlIRk9VB2vzvZ05lX2ikFgK5vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظهٔ انفجار تانکر سوخت در سنندج
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/145975" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145974">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArQXi6gt9-VLPlbt59lJfn1F-mJ4jezUpMiLfDDeIBlVEaxTm1A7koxS86M6mhFW2g2o124Bv6DQzk8nPbkUITwSdOQewp4I5n12o_EndftJ7kcXi5fw48mJd-rmiOgVX9GJ75R6uQT1VW-MibRb2SOu8vvcgSbjdO4qdJbXliNeJvaFYF39E52MldesGiSgcUJgsO9IIe8Ve5eqAYRmZe70ANBGf32I-LzoIyb-CMCEDHXGlBN35pRsVSQfABoO8-gGYZ8htsF5aDN7qkhRQma1_7aGySr8kqK4JZoELvyu4nRO4GxMEXYkrbg4xmFDjrBox1Gw97rZWLzjyrgFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت اتاق جنگ اسرائیل چند ساعت قبل از اعلام افزایش قیمت بنزین
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/145974" target="_blank">📅 22:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145973">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
محسن رضایی: تنگهٔ هرمز کاملا بسته است!
🔴
بعضی وقت‌ها آمریکایی‌ها از صخره‌های متصل به عمان ۵-۶ کشتی را عبور می‌دهند و معمولا این کشتی‌ها هدف قرار می‌گیرند و هیچ‌کدام سالم نمی‌روند و معنای این بازشدن تنگه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/145973" target="_blank">📅 22:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145972">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⛔️
فوری/نرخ سوم بنزین ۱۰هزار تومن شد  @ramezanii_fx</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/145972" target="_blank">📅 22:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145971">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
از دقایقی قبل سرعت اینترنت برخی کاربران افت محسوس کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/145971" target="_blank">📅 21:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145970">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b309972321.mp4?token=bFpdS643P2tZHmiSrJyXJOpXgEPod1qZGV2WjuMhLVEiQQGScaS-YFXdVJaUSkswWCyWyMrb1lDdeybKp5wm-utwI-ekkkACbGzT2T5M2syN14uJ72GX6HrJMRvXQTiMH_zklagAzZJHcAjLSCfeLqhzZXn5gkgU7d31ZOBK-5dwZ3c0e-l1N2UiCc2k-BsFs-hkm6tbh5nRz0wDEzhXHDiUp28FM7Q2YbEp0VAkqZOUeC61_N__X6qN3DIOwOYI3ffc_-rrsTAUPkXGQukRP7SmCNLE-MHix-LtUvapw3-WMLDZ9V_14lxrAaiknKQqgkvo99DlPRvZY5R9zm-Xhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b309972321.mp4?token=bFpdS643P2tZHmiSrJyXJOpXgEPod1qZGV2WjuMhLVEiQQGScaS-YFXdVJaUSkswWCyWyMrb1lDdeybKp5wm-utwI-ekkkACbGzT2T5M2syN14uJ72GX6HrJMRvXQTiMH_zklagAzZJHcAjLSCfeLqhzZXn5gkgU7d31ZOBK-5dwZ3c0e-l1N2UiCc2k-BsFs-hkm6tbh5nRz0wDEzhXHDiUp28FM7Q2YbEp0VAkqZOUeC61_N__X6qN3DIOwOYI3ffc_-rrsTAUPkXGQukRP7SmCNLE-MHix-LtUvapw3-WMLDZ9V_14lxrAaiknKQqgkvo99DlPRvZY5R9zm-Xhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک هواپیمای هشدار زودهنگام آمریکایی بر فراز پایگاه هوایی موفق السلطي آمریکا در اردن به پرواز درآمد؛ در پی نگرانی از حملات احتمالی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/145970" target="_blank">📅 21:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145969">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
یه سری شایعه شده بنزین ۱۰۰ هزارتومن قراره بشه… ولی تکذیب شد فوری
⛔️
✋
معلومه با این ناترازی شدید انرژی بنزین نرخ بعدیشم بیاد… یک سال اینده بخش انرژی خوب نیست…دلارم میتونه دوباره بده بالا تا اسفند
‼️
@ramezanii_fx</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/145969" target="_blank">📅 21:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145968">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dlvb8daXPP1CEvRTnuW5TZey6QUAn0Bv7mLjaDHDya7OPs6IOMnRCEbtqyasmh-ZXt4T3SOIWulHLLbhb5ILkM8Fji8Gh0zWzN124MZVuE_FrIrKzBMAV2R9i915RDmps2WfEkUhLkHDT_zqBRZeP_rmsML4-ht08AaRtLrlaeCBt529yMrdtVNWOtMFhmLcfKOpCg84iAegvXNGroDYf4D9AKjGmvaT_GNGUyf1-d1H24qz0q2v2pMDx7lnXnsYbEAYo-DZOVuVwh_ty2wYVWjA1jjnZY_5Js0GoaH5YOjhRGRKPNq0M1TNckzYM36dqbjzRqMfLvVX7J4TpZ_ZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای آمریکایی وارد شهر جدّه در عربستان سعودی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/145968" target="_blank">📅 21:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145967">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvFwdtcOznSZrapX5DUCjQAB-tNFzP236nfRy3IPRryUvGppG45pjbP6b3pMdeMvfoPacBz4DyGe3mGdCopEAxfAtzgOt7TuyUaXeNlR3boNLvOjsm4HvXQ408FaRAGXUWBQ6DA0j_cLbx6cZ73OxPGiPdE-PegxDNAJnChknTOd_wswi4S6q8wPTNzV55noB73W8WPtFNyKxhPkNF_JP7VawZ02q_ureIOMRkJxrV-xDllQFT74S-w6_tjOCht44XxfQ52rpgvgnnhPx7W0pWXbJkO0yfLEN06jnZe9FcGgh6VBetaGxQ5XA6-T_EA7eeDdrKBCwNMC3PMOQZ0gaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ: ماه متعلق به ماست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145967" target="_blank">📅 21:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145966">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldwMKTtCHWoOrq324mCNjcjPQI2zC9_56IOvdhgRV59plhgO695KNxFxSKhS9QB6MNKNtZD75Ux72t9GPHB9gli6JJ7EWVmphuk2IMRRJNDC1yilekoKpE3u4u_h-ubj557arSWXyOsoqbOE-ZqpYu7vC2bMXcINf6Blw4jeB_pf8QhDuM2YbgthLp9LKLQKLwwpMc2NVVOJf_V0kjZ9_UxDBVLrfoB5-oTIGtNlSIHExTc2jb8mpBr1C3N044AnDT8ahKnXneCpwCFtkg73HtYPQRPzIImiQKOHyNv9T3mwT9uQtZLFp2pmYkUgKPCy6BXbTv0Tpvb9wRtbkXqfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145966" target="_blank">📅 21:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145965">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud0Vf4wBP_mmK-OPIuU3TIwRxq3qFleGfxX90ucezvkagPSREFmrmoN-WaQXptvTg23HPSm2bM30hZu15uByKc68HZZiM7CTc6DnfUeN-HatlZp_WdlkicwxREE6Io0VoD-tbD_5v8SRAicQ4io3txwVPyL-Axlq9Vt7fAanTkeq6wUDs4wB7TKZtpanWecUX7L21L8jKlNn1jPZjisusc9oUJmDAkuyIYbdkUxA4b_UtmvnJdsZQLwGo4uC18PMhOVthB3yIfEQa0tVZ4dTPIiPMyXccvjyLUwLuMUA-gsRSNIx_WIsv957-BxikR0M_pQhVMPPp-1XTAzfy4Oa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  نقشه ای را منتشر کرد که در آن ایالت نیومکزیکو با عنوان "آمریکای جدید" مشخص شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145965" target="_blank">📅 21:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145964">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJvruP8EiAYBr4sAalqAp1DzsoNvNuX77fh0RPW-Sh55LbQ8UJna2R8_JhO2M9222aEirH0pfP9Y8yOZM_Z5XN_zjfugZCRcHceASpwS4JGgXwjPzFlETz8xH4NbGg7kenQJs2HKbZmzXLZ8RHCK9nR9KjqZPVt34PrXT6qRm4wVLia2oikbrE3Fi3qRF4l0j4FTPhgzJy5OaRbiGwApa42lLFk9sQml0k50Yh7x4SGayMKnJ5Yo2GzEDfesGP7AykA36fG90CnzgVIfdtazexiA4A8tTvIviuxRP4EkSZO3jwwseGFPXYNz7YqqJQVBwbY8d9ZIuI_Q5GAHQCdqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، عکسی را که با استفاده از هوش مصنوعی تولید شده بود، منتشر کرد که در آن او و جورج واشنگتن سوار بر اسب دیده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/145964" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145963">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN-eecv20fBuCwz5ZKc2-1EbxIgg6WrHpu4zr9g9yBO4MR_bE6kCrTjjJ2zGiifFPqwy38bTn4bFNpoQ9_d9gt4h1SUYqvP1QD4quPjhHVUDzkAyJJnJvIk46sh0yqgzRwKNE-1_4uOHtt8rLac3e-OHqj9Zr6Tz6ecy2yhZGPUfqN5-YwfH5vkUatTYldYhvMVcL-hSAOeyhK9YAMwMal5RdyuDBWVvWrKAGzY69oDViBEj-A42Sk3wiYGBIfqKdS3Lwup2s-c1eybe77qi55HMfk3pOidLslQNH82aOHNiydLfijXy5AvOSKM26klppsYgB6N3FpYePrPqnEke2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  از طریق شبکه اجتماعی Truth Social: رئیس‌جمهور واشنگتن از رئیس‌جمهور ترامپ دیدار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/145963" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145962">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIivn2QldNm4hLwRkl6haoumXfM-fHz0a9ylLQIiuKQFSp9ohqwtBUxj1fZcuxiApggg5Ci6ooewYr7KeKcOeQnm8fpVL462dViyfREWSRIaQBfewZBO2TYTN2HcLPh0YchJlXMXLfj2Vjuft2pIE0k64mvsopDVMRZ5T9CF3ZHewwTGoJt5SJyM2r0ZT5T8nh7YFj1Rb7jejPwdF7RJ3BqDe08fWF-0l6bJT7l4oqnFV0jIrVLfEJazrZFsh2WGopACkDDX5OnGmlBErlfj5jha8QPandigtHNgzB_lTkxoSkm_Q192g6MOrIOVP5ePI6hjUrLnBYbn_T2MEvZ7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، گفت وضعیت ارزش دلار کانادا در برابر دلار آمریکا که به گفته او سال‌ها ادامه داشته، «غیرقابل قبول» است.
🔴
ترامپ افزود: سال‌ها همین‌طور بوده، اما دیگر این‌طور نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145962" target="_blank">📅 21:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145961">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be1197cb9.mp4?token=aYrrBJQg8qGrjFNdyk5bxWXDDzQyXMlbgmbPFDgLPxVM0-MgPTYjA-Xx7HtgqnKs_UxAMTNDJayiXk3g3K--1hOH9uJ_lKxdSeyBD_7yEDTOquHg1vzFot5BI1PXi1JMmqCDlu3xJ8WDy53GefF-flswDNf-sCjFTU2yeU_gkF-zcSpHa3NkRAsR9NamqcQCWnlCviFhpFio-nxjjP_4sNLg8zDOEuwm1xoF9G18Mcu6JY1Qpf1jMkakiwid3vD-fFZw-0Oz8mJ-RyjY3vDyGztkxXBc40LMs2BdlBnE8sKeVKRRqUrUb1xaPI0zh5ptrAc9LW80lxIG6oQxh4FM8ZXUgftW-JTvBFYOKZx4T1T5ymFIvmw3rQHF9gX7YsBqF29PQlZcpSaQfrVPTmGI2sevJfoxne2GeAe0qeFS_y_MrNTPkh_UeEZs1kn2HaGdBcByQiRrkydYg2zj6A3VR_v2hPzEDXB1BfpzR2z8dgJsDfxP6C-2-tT169UrqT9vd2ibvEO775kYCnefIoGuSbJ6za6V8qORq6lkwHMNxOSfluTAh2AHAdvTZWjsMqLt9XiBJ5sIEKBNtpj_KdSAIxosnZnBZO-Qb3JvxEqL0ahStWazUZWsRR4K8__T5UGLESMWL4XHfHMnwLG29EMbgjWYYR7G4FZX3-pXABa215g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be1197cb9.mp4?token=aYrrBJQg8qGrjFNdyk5bxWXDDzQyXMlbgmbPFDgLPxVM0-MgPTYjA-Xx7HtgqnKs_UxAMTNDJayiXk3g3K--1hOH9uJ_lKxdSeyBD_7yEDTOquHg1vzFot5BI1PXi1JMmqCDlu3xJ8WDy53GefF-flswDNf-sCjFTU2yeU_gkF-zcSpHa3NkRAsR9NamqcQCWnlCviFhpFio-nxjjP_4sNLg8zDOEuwm1xoF9G18Mcu6JY1Qpf1jMkakiwid3vD-fFZw-0Oz8mJ-RyjY3vDyGztkxXBc40LMs2BdlBnE8sKeVKRRqUrUb1xaPI0zh5ptrAc9LW80lxIG6oQxh4FM8ZXUgftW-JTvBFYOKZx4T1T5ymFIvmw3rQHF9gX7YsBqF29PQlZcpSaQfrVPTmGI2sevJfoxne2GeAe0qeFS_y_MrNTPkh_UeEZs1kn2HaGdBcByQiRrkydYg2zj6A3VR_v2hPzEDXB1BfpzR2z8dgJsDfxP6C-2-tT169UrqT9vd2ibvEO775kYCnefIoGuSbJ6za6V8qORq6lkwHMNxOSfluTAh2AHAdvTZWjsMqLt9XiBJ5sIEKBNtpj_KdSAIxosnZnBZO-Qb3JvxEqL0ahStWazUZWsRR4K8__T5UGLESMWL4XHfHMnwLG29EMbgjWYYR7G4FZX3-pXABa215g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری و رسمی/سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/145961" target="_blank">📅 21:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccQxygAv0aPSWLGjbrHXNi3EH_ScheiqqSHCKNzNLF-SAE4tT7Ha_ifGSpADCE-rOmfSIMOxLDh-KDIouBsHMoWP8SHGGzWKqGdJmXX1wy1b97qm5zN5lrb43wn1u_ontVz6hxEPKLzNbFDA0qFu7L37f9ikRm3za1X8_ciPLr65s7oVi450ZWmdZczVrMnj9aCIWSlb_qROdHLckLntSX5WU83CSL9vxGt-N-YTS2jyY2Z8yop-xhev5v2CxAPMp9RpEYtKV2T078cTlCDxCbW_Tn6a1-TPWXttKLvn9fvGy-RpjTe0p-GaFVZ8a5vqB-CXyCJOveY58wgfa5ZPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfrhMyRR2TpoNcFA2pMxTNtZnL0JOVWc1TZ9oZzf6HEHMpytN_wzMsbZe-hKBrO4hHa_OU6bo531SDQ6q5twJVBRWI5jE6yxbHlcpw6tjU1hxmGIkgQ5S5PER_tuXzBVj7HbnId7IJUnVjmJ_en4Qksn-ehTYxhSvQPiHfMQ7A3voCCVY_ZqCBPOP6xtbY2yTnR6uKViPPrb_vrBRzxPcsRdYlRv4sCNUytMguvoN9wXRONyz9SMqg8nofiyLaLxBpNpHqUT4aOE50B0ZbZdityKuAIesu5EN6JQSzkpQCNO2CYJLhRmTOdwtFYmDD-_yqLjcpZq7y6yZgufjIkYbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای P-8A متعلق به ایالات متحده آمریکا و سه فروند هواپیمای KC-135 سوخت‌رسان شناسایی شدند که در نزدیکی خلیج فارس در حال پرواز هستند. این هواپیماها از پایگاه‌های نظامی آمریکا در بحرین، قطر و امارات متحده عربی به پرواز درآمده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/145959" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145958">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / کان نیوز: ارتش اسرائیل قصد دارد کوه "علی الطاهر" را به کل منفجر کند و منتظر تایید از مقامات سیاسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/145958" target="_blank">📅 21:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145957">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر بهداشت: کمبود داروهای ما از قبل جنگ کمتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/145957" target="_blank">📅 21:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145956">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4de2185aae.mp4?token=HX-I9XdUvVtPDUVjgtNWjV4GFUmWXWjl1k_DLg8g-NuE4P_GuMKzaue8SXCZ_Vjs7_oRx5c8JkCNFcHvJ79GXgfX2WujkSz77I7_xhok-_QYPFJDqeB1Glfso7JgDvYt2WuYXwY5IvLA1aUcvg2fZEUOErVaTqu-Xtzzve2A2FaPdxCAcrg1VZbalrP6Wjd42gFtyhN5WFI73LMq7CHOUgYBy02-omxR_Z9SlhoxQ_ZB7B5e_263XBM5SlxazTPJweIIazKTPLAvnfsxpvJ5kcqXAtSloytWMMYQ62-QwCx8QIhuOkpPTAsWUu0SDfQylX6GVniiueSsCCG5xsY3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4de2185aae.mp4?token=HX-I9XdUvVtPDUVjgtNWjV4GFUmWXWjl1k_DLg8g-NuE4P_GuMKzaue8SXCZ_Vjs7_oRx5c8JkCNFcHvJ79GXgfX2WujkSz77I7_xhok-_QYPFJDqeB1Glfso7JgDvYt2WuYXwY5IvLA1aUcvg2fZEUOErVaTqu-Xtzzve2A2FaPdxCAcrg1VZbalrP6Wjd42gFtyhN5WFI73LMq7CHOUgYBy02-omxR_Z9SlhoxQ_ZB7B5e_263XBM5SlxazTPJweIIazKTPLAvnfsxpvJ5kcqXAtSloytWMMYQ62-QwCx8QIhuOkpPTAsWUu0SDfQylX6GVniiueSsCCG5xsY3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جارد کوشنر در کی‌یف: در این دنیا، یا دوستی ابدی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/145956" target="_blank">📅 20:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145955">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8283fd5109.mp4?token=US9P4tyj9w3MJjAEsImQC5K-RP9zimAZLPzpNaAs_FR2Lna9FhQ7qB3X3KpgFZ6zPWKkwKamF-EWZaJ6UniHUUrijHghFtU7GtX-KcB9Cjf0JBiJTHvbWuvwbM274HRaegJGl0jbhfcgvwd_fm4XwcjrLn9F4g_XOmyeR5hENZW0-ylcsaO8Q9dBj2SvOcZz-_L7KrMvlfhpVXt80sMb1dqxvjfPyC0rXBSNSz7Ukil3qFHxs9VERbewED8EUlh-TnU6lnEPJvHBLW40SzTWL8ih7_YmKfZN-S--rN7MAFj5h3xn7kXu1PwtOJ5FbnzBl0ur9zEj9pObjhvFkIhliA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8283fd5109.mp4?token=US9P4tyj9w3MJjAEsImQC5K-RP9zimAZLPzpNaAs_FR2Lna9FhQ7qB3X3KpgFZ6zPWKkwKamF-EWZaJ6UniHUUrijHghFtU7GtX-KcB9Cjf0JBiJTHvbWuvwbM274HRaegJGl0jbhfcgvwd_fm4XwcjrLn9F4g_XOmyeR5hENZW0-ylcsaO8Q9dBj2SvOcZz-_L7KrMvlfhpVXt80sMb1dqxvjfPyC0rXBSNSz7Ukil3qFHxs9VERbewED8EUlh-TnU6lnEPJvHBLW40SzTWL8ih7_YmKfZN-S--rN7MAFj5h3xn7kXu1PwtOJ5FbnzBl0ur9zEj9pObjhvFkIhliA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوشنر: آمریکا و اسرائیل درباره آینده غزه توافق دارند
🔴
جرد کوشنر، داماد و مشاور دونالد ترامپ، گفت: آمریکا و اسرائیل درباره وضعیت نهایی موردنظر برای غزه با یکدیگر توافق دارند.
🔴
او در عین حال با اشاره به شرایط سیاسی داخلی اسرائیل گفت: برگزاری انتخابات در این کشور باعث می‌شود تصمیم‌گیری‌های اسرائیل در برخی موارد «غیرمنطقی» باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/145955" target="_blank">📅 20:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145953">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802abf04ac.mp4?token=rFsiKwPiq81HxU_4LFyjWMvXIPuXqVXW5cJIF-ipSmrjq5zzv4-h8xVZ0-OdZoUIrpqtkYsSadAOZvSAp0NdHSLy7QKk9wZPe4BhWQeqidlq4ya5HXSpf563idOBWnL6xBgGfa48oFMsgKoWSCDMQL7CEe-vmW82esJdv6ZfgkZ32YZt0jYm-u7YeJEX1daGtDiFyqChyW0DOJJliZKrvc_1tekPYyobiXxWAclO7zDGdHyN06eHKXF-Fpm9KeRR5YcM5K9ML5pBQymzJtiLRNY1bus6SmoIc2SZtUiMKKFs0AwPqnFSqH4dVOfHrdLhpsfvGWBD87P-HUb-Xd6ADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802abf04ac.mp4?token=rFsiKwPiq81HxU_4LFyjWMvXIPuXqVXW5cJIF-ipSmrjq5zzv4-h8xVZ0-OdZoUIrpqtkYsSadAOZvSAp0NdHSLy7QKk9wZPe4BhWQeqidlq4ya5HXSpf563idOBWnL6xBgGfa48oFMsgKoWSCDMQL7CEe-vmW82esJdv6ZfgkZ32YZt0jYm-u7YeJEX1daGtDiFyqChyW0DOJJliZKrvc_1tekPYyobiXxWAclO7zDGdHyN06eHKXF-Fpm9KeRR5YcM5K9ML5pBQymzJtiLRNY1bus6SmoIc2SZtUiMKKFs0AwPqnFSqH4dVOfHrdLhpsfvGWBD87P-HUb-Xd6ADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/alonews/145953" target="_blank">📅 20:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145949">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcCWqwfRsMhPrNpcNa8WiQO_IuIQsAH5SkWA6eIu8qw97hulm9Sc9DpbvBgCwvUf8GAI1WXDCpa-nMGzYoqIIw14h9X3rMxmNelqp5jlTSFHCIhb7mmlZRhJJ2skCPMkSpBakS3Z-0fGowEokN4liPYvWgCQSt9Cg8MqNH0DUenqLgHFV2jQupAvX9_6EBOVCRuB4kNNi6cRJkFwGQ_DY3W5gxrlVdq5S5oRpv2ss82topSLc1gbQHtD6yIlKW0msWhJ7SvcLxlOqGpK_pUO5SRNsx10dt87B719xvW4t--4b06Vz-PqDZAoIthq3GNg9aIamsrMlOjxKlFNb2gXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PE5Ut2V0tVBr21-lvzTd4_D8PtqXaZd56cZ437D7jB1Gp5xq-1nVpUkirH7ZeCiExhJ0L1YnDsYUO6MHqbueLc52NKv5za0EWK1thH_vGIk-frrzTubxVpV1wGmQMEBn8JE-WRfRQi3z7qGmksEnx5ZFB9Ci86KP9BoYrD23Fd96IX78DIv-63dCQQPN4OIbrbn3P6HB36IFL5G7r8CWfLGxAJiluIFWY2f3Iqf0rGLpBa8GrFzCmUR_bHnzizyOedU0kzC1yovoicfDyL3dJKIUIkkmyhCd2loKW99h85kl3x-kL3P79LHjyJ_FWiYd64lehqQmpO0v0wqgf5Lm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWNB6v0R2sQfzUUqy5s_8WTwFdNLZHJAbB7aW_azrNYY2-_hx3y_U7_iqVRmmydTXz7grQyDrZ_kRxXGGX3_ifQvmEFms_DAVA7ENBHsOl1gp-dVraxtKJqIIrgUx5wEpyS4AYykecmW7k4R8izCGg4w9dslOsv5hAoo5tfXA3mDzWf7e2nGUe9Br3fpjmNWpYVlk6PIKaE7Pzm9877NDaK894v65a2kDgd29YZhBqopQSMUzIM0tQwvrIXKtfuskrcxMp6iHO5rWNeMCi-0Rtnc6lAlszXYDV4GtdqkivXk38PPuunq0rG06tsSL9q6p4xNyk7L1X_7ItI6MMUjvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ca623840.mp4?token=eIatAyo7ZDXcGJzO6LwiHwgFd_M0wqupy9csSaMIaVqTwt9dfhrKUPHxfevw9fpluoSIMOrzBcyDwqpgfSrVoNHftBxpc_R8_4NEC-gOW71St0mPMybvLhpBYBYsqQxSlr3_r114GX2EfyuYHx1AhZwc4PpLMZ8CcFCUris5bPumAffp8jjJ4b4mADw-mMROIyReKR39a3uFY9Em3kPndFuBDxq1RYtfAflicv109yJh3Xmr6gJG2ZK9b8P0iPPH26_I0e3K0i16Q-rc6WYE62WtYaqLJmMYnFzKTFviGRTnuPNpSkGx7nvk6bJLA_D1tyHAv6KWh-4UuFYEVPIDew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ca623840.mp4?token=eIatAyo7ZDXcGJzO6LwiHwgFd_M0wqupy9csSaMIaVqTwt9dfhrKUPHxfevw9fpluoSIMOrzBcyDwqpgfSrVoNHftBxpc_R8_4NEC-gOW71St0mPMybvLhpBYBYsqQxSlr3_r114GX2EfyuYHx1AhZwc4PpLMZ8CcFCUris5bPumAffp8jjJ4b4mADw-mMROIyReKR39a3uFY9Em3kPndFuBDxq1RYtfAflicv109yJh3Xmr6gJG2ZK9b8P0iPPH26_I0e3K0i16Q-rc6WYE62WtYaqLJmMYnFzKTFviGRTnuPNpSkGx7nvk6bJLA_D1tyHAv6KWh-4UuFYEVPIDew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات شدید هوایی اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145949" target="_blank">📅 20:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145948">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7befbd48f.mp4?token=J95X4VJCr4quRNr7HN0-_EuD9_44wUY4Zn-3aMDnGNLT0eZErxdPPFhTO53qTSe3E-VC4uz2p-hh9RmFQa-hH2uJ11kEzroN9tIG7gBHzf4CxKOqFxu1i5o3GOfRes9lTPZhqTyP3DPE2nVsG6z3Tk4rlNdPBq4CKfq7A0hJflWEr3ko61mlza8EeoKvPRVOJGogl-u_XMvHBo92uXabkd2iavI9puwvaBHh7xU9uvOWSQGr0M1CqD75GMroIwVqkImub8PBe0seC6PMqe8KdH-v9JUiJoSwr9mvHRavZeiQh4qiJJUoHTJ4gDwTXoTpxbnD4PGTnCmCh8YCI9P4nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7befbd48f.mp4?token=J95X4VJCr4quRNr7HN0-_EuD9_44wUY4Zn-3aMDnGNLT0eZErxdPPFhTO53qTSe3E-VC4uz2p-hh9RmFQa-hH2uJ11kEzroN9tIG7gBHzf4CxKOqFxu1i5o3GOfRes9lTPZhqTyP3DPE2nVsG6z3Tk4rlNdPBq4CKfq7A0hJflWEr3ko61mlza8EeoKvPRVOJGogl-u_XMvHBo92uXabkd2iavI9puwvaBHh7xU9uvOWSQGr0M1CqD75GMroIwVqkImub8PBe0seC6PMqe8KdH-v9JUiJoSwr9mvHRavZeiQh4qiJJUoHTJ4gDwTXoTpxbnD4PGTnCmCh8YCI9P4nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از وقوع آتش‌سوزی در پالایشگاه ینبع عربستان
🔴
تصاویر ماهواره‌ای «سنتینل-۲ال» یک محدوده سوخته جدید را در اطراف یکی از مخازن ذخیره‌سازی نفت خام در تأسیسات پالایشگاه ینبع متعلق به شرکت آرامکوی عربستان نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145948" target="_blank">📅 20:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145947">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: ترامپ ممکن است به توافق هسته‌ای با ایران دست پیدا نکند و در عوض سیاستی را دنبال کند که هدف آن نابود کردن توانایی تهران برای دستیابی به سلاح هسته‌ای در آینده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145947" target="_blank">📅 20:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145946">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
زلنسکی: جنگ با روسیه احتمالاً تا زمستان آینده ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/145946" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145945">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
بهنام صمدی خبرنگار بورسی: از امشب نرخ سوم بنزین ۱۰ هزار تومان خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145945" target="_blank">📅 20:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145944">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کوشنر: رئیس جمهور ترامپ می‌خواهد چارچوبی برای دستیابی به صلحی جامع و پایدار ایجاد کند، نه فقط پایان دادن به جنگ فعلی در اوکراین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/145944" target="_blank">📅 20:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145943">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ویتکوف: ما برای از سرگیری روند مذاکرات به کیف آمدیم و از دستاوردهایمان احساس خوبی داریم و مشتاقانه منتظر دستاوردهای بیشتر هستیم.
🔴
روسیه و اوکراین باید برای پایان دادن به جنگ امتیازاتی بدهند
🔴
ماموریت من و کوشنر این است که طرف‌های روسی و اوکراینی را گرد هم آوریم و شکاف‌ها را کم کنیم تا به یک تصمیم مشترک برسیم که به جنگ پایان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145943" target="_blank">📅 20:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145942">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0iguN-FFWOjtMxNmK38fb5OW7XJcRKDpBSOTSyPMjgoyiWBphwM-AEFXiHjk1AgghlNsUNY3XFzdP1k8jwzgYR4ZLJliCU67_6YY87_k3OdHCfAWFCaWkW84AVVvvY0ezKq5KghRzLmLRu9PPXg0_PNNSk5xinf_lkbB6NW2MufCYT8hOGB4xyIwtOiYEVDpHf3fwXIgw5WSUTheYgmvW7KTdfOAzY2Jqh6FV_WlLKMtboL4CxPr3H32jfJsSBK6XL-NvuIII8lk9-5b2XCdUuougS342rUq49R9_tVS3dnXOx9g10I9C6IvCt_ItCSBwg9acAFeCAiPLZGxrm5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: افزایش قیمت بنزین اثری بر روی صرفه‌جویی ندارد
🔴
افزایش نرخِ سوم‌ بنزین به «۹۷۵۰ تومان» اگرچه شوکِ ارقامِ دیگر را ندارد ولی چندان هم در کاهش مصرف سوخت اثر خاصی نخواهد گذاشت.
🔴
به دلیل پاره‌ای مسائل در کشور، نیاز به کنترل مصرف سوخت هستیم که این نرخ از پسِ آن بر نخواهد آمد، چون مردم از دیگر مخارج خود خواهند زد و به سبدِ هزینه‌ی بنزین اضافه خواهند کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145942" target="_blank">📅 20:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145941">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
در جلسه اخیر ستاد ویژه ساماندهی و راهبری فضای مجازی، و به دستور ریس جمهور ضمن لغو ممنوعیت اطلاع رسانی رسمی دستگاه های دولتی در پیام رسان های غیر بومی، رفع فیلتر پلتفرم اینستاگرام به صورت مرحله ای، از تاریخ ۱۶ شهریور، به ازای دسترسی ۶۰ درصد از سیم کارت های موجود شروع و تا پایان شهریور ماه تکمیل خواهد شد.
🔴
عباس پازوکی معاون ارتباطات دفتر معاون اول رئیس جمهور، همچنین از دسترسی آزاد به پیام رسان تلگرام در آینده ای نزدیک خبر داد.
🔴
در همین رابطه، پازوکی عنوان داشته است ریس شورای عالی مجازی و در ادامه سیاست بازگشایی پلتفرم های خارجی، به زودی تغییر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145941" target="_blank">📅 19:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145940">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از افراد مطلع از مذاکرات در کی‌یف: ویتکاف و کوشنر نسخه‌های به‌روزشده‌ای از اسناد قبلی را با خود آورده‌اند؛ اسنادی که با توجه به شرایط تغییرکرده از زمان متوقف شدن مذاکرات صلح با ایران مورد بازنگری قرار گرفته‌اند
🔴
در مذاکرات توافق کلی وجود داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145940" target="_blank">📅 19:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145939">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزیر امرژی آمریکا، کریس رایت: ما همیشه برای توافق آماده‌ایم. هدف ترامپ همیشه این است که به راه‌حلی مذاکره‌ شده دست یابد و جز در صورت ضرورت مطلق، از راه‌حل نظامی استفاده نکند.
🔴
رایت ادعا کرد که بزرگترین نقش نیروهای نظامی آمریکا متوقف کردن صادرات نفت خام یا محصولات مرتبط با نفت و گاز ی ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145939" target="_blank">📅 19:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1a155b4e.mp4?token=v2bFZHlW0VFWyTK2U2fuCvv1czbS5_KmVy2Hh5dSiviEQBQoTu3D0rENt1UAHoKrj4orlhiGCaa33hweU4iYK06wXjJwvKE4RcyO-LHN-OjwesvgAlJ66lLRa_8FMUxvPGIl-L6l37PGCTaVqCbH1F-Dc5cYSBIH9n5wPYbLeBLtSWArJ6k5dg7rgVpSQE4J9bQc8MkKOJVtUD0uX_Br6vwFhalJ7bN3GkGvHT-VWTEV2t_7GuSf2heKLZonlHpJJzGBTagprpPDdJdJozYTCApMiK2eZbusSTQUbRji_Bg5KaWf_YEcA4N-VTjpXErVhVrQ1O1p1M9hEgYQj82-LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1a155b4e.mp4?token=v2bFZHlW0VFWyTK2U2fuCvv1czbS5_KmVy2Hh5dSiviEQBQoTu3D0rENt1UAHoKrj4orlhiGCaa33hweU4iYK06wXjJwvKE4RcyO-LHN-OjwesvgAlJ66lLRa_8FMUxvPGIl-L6l37PGCTaVqCbH1F-Dc5cYSBIH9n5wPYbLeBLtSWArJ6k5dg7rgVpSQE4J9bQc8MkKOJVtUD0uX_Br6vwFhalJ7bN3GkGvHT-VWTEV2t_7GuSf2heKLZonlHpJJzGBTagprpPDdJdJozYTCApMiK2eZbusSTQUbRji_Bg5KaWf_YEcA4N-VTjpXErVhVrQ1O1p1M9hEgYQj82-LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، درباره ایران: آنها به ما حمله نمی‌کنند.
🔴
ایران از این کار اجتناب می‌کند و می‌داند چرا: زیرا اگر آنها مرتکب این اشتباه شوند و به ما حمله کنند، ضربه‌ای را متحمل خواهند شد که حتی تصورش را هم نمی‌توانند بکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145938" target="_blank">📅 19:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1caed26faf.mp4?token=ofkQmIcFJQ5XZbu84jogrK7xnH8WErskUIIHCiGScOg9U7eJtaMjRDkKX0PcbWkXA5clpHP6ID8E0EnNTteyJLd0xqg2ebk1hlRHLqrAh2qVCVuySE4MObVNziJYaj-TyA4SASkHiTaKBzlLY4muba-hW-tl9L0pOnGZ9P5OHzVemXY0-TIAd1aRokKMzqYAW2iaK1PQNxwpBnlQMorCcioNNGbosbMq24mlTiuuDSi2x9x7mWpSrAFl8ZnbPIKEoN0SqbL8slA3uvHN5vS9EjfA_gVBqI0u6FvOOZRGJeRttjWB6g-yrGAAn0fCfhbnQcIsQjwIAFP7h_eQel1qLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1caed26faf.mp4?token=ofkQmIcFJQ5XZbu84jogrK7xnH8WErskUIIHCiGScOg9U7eJtaMjRDkKX0PcbWkXA5clpHP6ID8E0EnNTteyJLd0xqg2ebk1hlRHLqrAh2qVCVuySE4MObVNziJYaj-TyA4SASkHiTaKBzlLY4muba-hW-tl9L0pOnGZ9P5OHzVemXY0-TIAd1aRokKMzqYAW2iaK1PQNxwpBnlQMorCcioNNGbosbMq24mlTiuuDSi2x9x7mWpSrAFl8ZnbPIKEoN0SqbL8slA3uvHN5vS9EjfA_gVBqI0u6FvOOZRGJeRttjWB6g-yrGAAn0fCfhbnQcIsQjwIAFP7h_eQel1qLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: هنوز کارهای بیشتری برای انجام دادن باقی مانده است.
🔴
این رژیم در ایران — پایان آن نزدیک است.
🔴
آن ضعیف است، برای بقای خود می‌جنگد، لنگان‌لنگان حرکت می‌کند و هنوز مأموریتی برای تکمیل باقی مانده که ما عزم جزم بر انجام آن داریم.
🔴
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/145937" target="_blank">📅 19:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145936">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f79f2049c.mp4?token=qHx9LUnpHBhE1mrVb1Kt00BE3ww3ufZKAkaj_P0LK-_LYl96nALqWSFtSI0i2B1PEmNgkV8haunSFeKYFnDx1A0IeDeAUD1SvDSUW_uFGiVnQ4qxe9eHuWwlv6LmsiFfdXTvQpZgdb6JAalpExk2KVbCf44AMj33cyDN2igtaWgUqz8ySKPXyytOJMUs14R2c7CaiE5y5gTb8YXQzxwPozlvq9VbC2fWZWMho2zjWcU6NlMu-WjtzisAvfFlFWc3JrOAdmWwKkqdnyHlKW4rpSuOZV6yNHM_QQSRymIn7TtagoRtCx_2g8NLLUKCmhTT33MoUmro-s9-1cQ6Kq-Zpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f79f2049c.mp4?token=qHx9LUnpHBhE1mrVb1Kt00BE3ww3ufZKAkaj_P0LK-_LYl96nALqWSFtSI0i2B1PEmNgkV8haunSFeKYFnDx1A0IeDeAUD1SvDSUW_uFGiVnQ4qxe9eHuWwlv6LmsiFfdXTvQpZgdb6JAalpExk2KVbCf44AMj33cyDN2igtaWgUqz8ySKPXyytOJMUs14R2c7CaiE5y5gTb8YXQzxwPozlvq9VbC2fWZWMho2zjWcU6NlMu-WjtzisAvfFlFWc3JrOAdmWwKkqdnyHlKW4rpSuOZV6yNHM_QQSRymIn7TtagoRtCx_2g8NLLUKCmhTT33MoUmro-s9-1cQ6Kq-Zpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: به دشمنانمان می‌گویم: با ما بازی نکنید.
🔴
در حال حاضر، ملت ما قوی‌ترین قدرت در خاورمیانه است و برخی می‌گویند فراتر از آن.
🔴
ما به‌طور مداوم تروریست‌ها را در لبنان، غزه و یهودا و سامریا ( کرانه باختری) از بین می‌بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145936" target="_blank">📅 19:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145935">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b463d6f5.mp4?token=bRxlKKdm_gLhP_WCeQc8SebXgz95TugJHz2SsETWPhM0c_kybMcuNWjZQHwzz98M2opxhrTnFCg_X7Ig7nB1tSsl7gUgBGQvyWHTJ4lZLHVsS9aq7jaFCEVwpoVUSy91dTmeczkEHsX9dl1py2NSS5Lia69DGEqiBjLn3p8mdOXtJgGwez-kt0V36uIWW5FeZatiCWLbaEEcFGbEoPel_Wi3tcYXkcAeDeyLGOwwiddTgKjfc2eTbjDvOSXfzNBV8zTxd4aIXoo4Iyr11j35KmSQwb9zTi64Y5Wgoudx63pUmwAw9VdA1izfWwr4xDpq2XLn81Uzgm7hUZ9du3KG1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b463d6f5.mp4?token=bRxlKKdm_gLhP_WCeQc8SebXgz95TugJHz2SsETWPhM0c_kybMcuNWjZQHwzz98M2opxhrTnFCg_X7Ig7nB1tSsl7gUgBGQvyWHTJ4lZLHVsS9aq7jaFCEVwpoVUSy91dTmeczkEHsX9dl1py2NSS5Lia69DGEqiBjLn3p8mdOXtJgGwez-kt0V36uIWW5FeZatiCWLbaEEcFGbEoPel_Wi3tcYXkcAeDeyLGOwwiddTgKjfc2eTbjDvOSXfzNBV8zTxd4aIXoo4Iyr11j35KmSQwb9zTi64Y5Wgoudx63pUmwAw9VdA1izfWwr4xDpq2XLn81Uzgm7hUZ9du3KG1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو
:
اسرائیل قوی‌تر از همیشه است و دشمنان ما ضعیف‌تر از همیشه هستند.
🔴
همراه با ایالات متحده، دستاوردهای عظیمی در رفع یک تهدید وجودی، از جمله سلاح‌های هسته‌ای و موشک‌های بالستیک، از بالای سرمان به دست آوردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145935" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145934">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
غلامعلی حداد عادل : آقا مجتبی خامنه ای خیلی ساده زیسته
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145934" target="_blank">📅 19:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145933">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که یک پهپاد شناسایی تسلیح‌شده وینگ لوانگ II نیروی هوایی پادشاهی عربی سعودی را در حالی که مأموریت‌های «تعدی‌کارانه» را در شمال مقبانه در استان تعز انجام می‌داد، امروز صبح با یک «سلاح مناسب» سرنگون کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145933" target="_blank">📅 19:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145932">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
حمله اسرائیل به یک خودرو در جنوب لبنان
🔴
اسرائیل در «النبطیه» یک خودرو را با پهپاد هدف قرار داد که به زخمی شدن چند نفر منجر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145932" target="_blank">📅 19:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145931">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIOkjNmZW5kpShPp_BEJOWYIjXqROdE7GHYPY5FxvXPV-2Yq9ow_rilFsNl9Dwt0_Ss6Qt6UedRQ2efFPLbGmovh5z6UMIkglH4CWsxXu8N-cYXxpZkSNq0GvMwl1LlZ8KThCXxEEAzWsP2HWLrJuOR1PDtjPM9LxYLat9Nvzw4AcqE85qiN1IMuwAU2g4krxoFPmaNWCYBisN-01CgOClHlD7OzAmAjWwnzw4gftiCoGbYJXk3lM1hUli0YTKz4Hts534fxlREQuWHlHWb9KRcPHHpOiggdAHn6XvqNVgXGYsOimc2WCE10wdX3DMCOb5-BgAMnNs27wKWETG3kNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طعنه اقتصادی قالیباف به بسنت: چرخ‌ها را بالا ببرید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145931" target="_blank">📅 19:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145930">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس اعلام کرده ماده ۹ طرح «اقدام راهبردی تأمین امنیت و پیشرفت تنگه هرمز» در این کمیسیون به تصویب رسیده است.
🔴
بر اساس این ماده، کشورها یا اشخاص حقیقی و حقوقی که علیه ایران تحریم یکجانبه اعمال کنند یا اقدام خصمانه‌ای انجام دهند، مشمول ممنوعیت عبور از تنگه هرمز خواهند شد.
🔴
طبق این مصوبه، عبور شناورها یا محموله‌های مرتبط با این افراد و کشورها از تنگه هرمز ممنوع خواهد بود و دو مرجع برای تشخیص مصادیق این موضوع تعیین شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/145930" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145929">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
روحانی : باید با مردم مشورت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/145929" target="_blank">📅 18:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145928">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ویتکاف: از مذاکره با اوکراین راضی هستم
🔴
«استیو ویتکاف» فرستاده ویژه آمریکا: از مذاکرات جدی و مهم با اوکراین راضی و به ادامه آن خوش‌بین هستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145928" target="_blank">📅 18:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145927">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/he55KwLXeJt-YxPG_tjRzyMc7eSIZSA9UN8fRI_F9SpJH2S2v6SfL0Et-T-dj-zRCchaxqxKGVDe6fKYF8TVA1ItOrHlYtdvK_qxTdun4520P_-zn1rKxsMh_1rb8JZZU6vIgelurYt6QsZIuET7eu1U_p26fsb1gEMKLc31xNGBWMITOJG6aTR_D8dmzAPUXOmvB6FO8HrTFQ7EBQa7vOjDBHW5mb4lldHgTf2zN5yog0KnX_jESBGkfyP80PnPLrwi1QNH1J0OYfKxbhfIvqLO4MaecWD7PXtk4XTuRrLinJ_-JH41YPO32wt2P4YhnsG47zqLrxg728fH8i_ixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انگار ترامپ موهاشو رنگ کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145927" target="_blank">📅 18:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145925">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=s_U18mMXngVNcPQSipc3FkVjwxArMwprkmZ_KlZ2N2QJNqv1Sn9eMTFmbXLOHrOu9NXL9E2jE_AFStf00oMV8sutDzfx2BuemM93CTMSzsPTHlZWT-lynY38Ix-gjGQ_rQIqMa6phPS1g5IJGXMs3fdhB2DshwwUYyBnmuekeAzCGWVaVo2HrhsrijmASvH9x31idqAskdlgBwiyabA5zjdFHDsOCK_RdETDiNt-vbgGNuhqbTgStuGQymCHKg_VpoI2qmfd4nqBI68P0hpAP659YnEr-16_hmH49zw_4wGTwUwAHaAnrMg725xypchUX4roklpVyHuwbYPnD0LdZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=s_U18mMXngVNcPQSipc3FkVjwxArMwprkmZ_KlZ2N2QJNqv1Sn9eMTFmbXLOHrOu9NXL9E2jE_AFStf00oMV8sutDzfx2BuemM93CTMSzsPTHlZWT-lynY38Ix-gjGQ_rQIqMa6phPS1g5IJGXMs3fdhB2DshwwUYyBnmuekeAzCGWVaVo2HrhsrijmASvH9x31idqAskdlgBwiyabA5zjdFHDsOCK_RdETDiNt-vbgGNuhqbTgStuGQymCHKg_VpoI2qmfd4nqBI68P0hpAP659YnEr-16_hmH49zw_4wGTwUwAHaAnrMg725xypchUX4roklpVyHuwbYPnD0LdZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک سرهنگ ارتش: یه قایق پر بمب با جلیقه انتحاری به من بدید تا خودمو بکوبم به ناو آمریکایی و شکست بخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145925" target="_blank">📅 18:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145924">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0406c9675d.mp4?token=VQ-uLc4JOmhgb5HJe7MWfRXugmAnq62lae9asqdbslm41RHuOJpxFKyxaYnh9WYBZ2hxO66wkqFP74jZH0m5lBE2PQJ9jJhXoFQA3-oL_JzNAGv1JUJInv_-E4dXh7czBXtO2UR2OLuLpOUiTWQhtAgf20Enj9Yic7EKnGoGTt2lTqmNK1SOq4ozvkc3B6fJXyt88F1tw1oLzbRCKNEKvaPgg_fVSLyZ1RMMfH2ewbwnZQG6xFSlmrQ8CDIijNVUvqRwai8cwihSWaTD4RtfeFbOjwHpoMTmrP7fc6a1RcHoceQvrofcD1Jmobuzd4COFAxQx0AD3hkaVWC7GOKqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0406c9675d.mp4?token=VQ-uLc4JOmhgb5HJe7MWfRXugmAnq62lae9asqdbslm41RHuOJpxFKyxaYnh9WYBZ2hxO66wkqFP74jZH0m5lBE2PQJ9jJhXoFQA3-oL_JzNAGv1JUJInv_-E4dXh7czBXtO2UR2OLuLpOUiTWQhtAgf20Enj9Yic7EKnGoGTt2lTqmNK1SOq4ozvkc3B6fJXyt88F1tw1oLzbRCKNEKvaPgg_fVSLyZ1RMMfH2ewbwnZQG6xFSlmrQ8CDIijNVUvqRwai8cwihSWaTD4RtfeFbOjwHpoMTmrP7fc6a1RcHoceQvrofcD1Jmobuzd4COFAxQx0AD3hkaVWC7GOKqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهران مدیری سال 1401: نمیخوام یک فریم از من پخش بشه
مهران مدیری سال 1405 یه سریال 15قسمتی به صداسیما داد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145924" target="_blank">📅 18:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145923">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
ترامپ گفته ایران دیگه نفتی برای عرضه نداره… چین هم نهایتا ۳۰ میلیون بشکه دیگه از ایران میخره.. محاصره هم دلارو قفل کرده
🚫
اوضاعی داریم..  @ramezanii_fx</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145923" target="_blank">📅 18:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145922">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2_uZrCSX-cRJIsvDF_RBkKqszeCb28qKws5rfelT3neHrIPWKh878zpHC0jKixXQpGKUK0rXJQqK5_pViQlieehAkbC84PDbUG5eRdvv9bjdq1HV-hh0MAzGtNl8dNnfv1q443gY4X1P72626MKCwS-0_prXQUgxdUT4_HC-aZuwYRMtAOJ-O6bh-Ykgktp0OfuPHIUs5zSQOjEiRlOvD6-f6HCMJjb-4YgGKHvK5X5qdQF1kyqj-hFBL9rrCRjYAFoRKixFly9zeGfYdPTlGhOaFGYnEiv26O1QDP3X0B2y7EMO3hQF69yWlzGiovMUpoxXeebn_f7sefp97GWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هیئت قطری به سمت تهران حرکت می‌کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/145922" target="_blank">📅 18:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145921">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
گزارش ایسنا: ۷۵ درصد کاربران ایرانی از فیلترشکن استفاده می‌کنند
🔴
نتایج یک گزارش از شکل‌گیری بازاری گسترده در پی محدودیت‌های اینترنتی حکایت دارد؛ بازاری که اندازه سالانه آن حدود ۱۰۵ هزار میلیارد تومان برآورد شده است.
🔴
براساس این گزارش، حدود ۷۵ درصد کاربران ایرانی از فیلترشکن استفاده می‌کنند و در دوره‌هایی مانند «اوج خاموشی»، قیمت برخی بسته‌های فیلترشکن تا ۲۳۴ برابر افزایش یافته است.
🔴
این گزارش افزایش هزینه دسترسی به اینترنت آزاد و رشد بازارهای غیررسمی پیرامون محدودیت‌های اینترنتی را از پیامدهای وضعیت موجود عنوان کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145921" target="_blank">📅 18:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145920">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj_Pz6CqR7u_EYKlN6diGg53WRwAv6_agKQFFVKWejwHYAABTTepf8TbSScdoqM6lqNF-UvU1eysvw4dfEFaoeM9ZhiW2-ArAiNLDdJU6aXyXS37vz83PhZDiponiCV2VPyKobvbgfWDsprjkpAczsAkYyslpXwjH3LqGZXXpl3v3Ob2R7nAdA1Hk2lBJdPOTK7tOqfmmiodkxLKSORJCvnR11ZnziGypjg-mmpfMlT8qYvbHlz_6MtKE97h6C-9qB02nuQy_REyj8C6VcdnMgZGJOCc8AAhXt3YQHvcKX8wIKSDKI-CVDjApqd-GmCW48LglaG4vg24hNUbj3c8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت داماد آیت الله روحانی
: علی‌الاصول، روی اصول خود ایستاده است؛ مردی که ز عصر خود فراتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/145920" target="_blank">📅 18:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
اویل پرایس: اختلالات شش‌ماهه در هرمز حدود ۳۳۰ میلیارد دلار به هزینه واردات انرژی جهان افزوده و حالا از عربستان و امارات تا عراق، کویت و قطر، خطوط لوله زمینی و بنادر خارج از هرمز به یکی از مهم‌ترین اولویت‌های امنیت انرژی و سرمایه‌گذاری منطقه تبدیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145919" target="_blank">📅 18:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
جزئیات عملیات مخفیانه مین‌روبی آمریکا در تنگه هرمز
🔴
آمریکا عمدتاً در طول شب، غواصان نیروی دریایی موسوم به Navy SEAL، قایق‌های رباتیک و تجهیزات تخصصی زیرآبی را وارد آب‌های خطرناک تنگه کرده است تا طی یک مأموریت چهارماهه، مین‌های دریایی را پاک‌سازی کند.
🔴
این عملیات دشوار برای خنثی‌سازی مواد منفجره، در زیر آب و در تاریکی انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/145918" target="_blank">📅 18:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145917">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
روزی که تلگرام رو به بهونه تاثیرگذاری تو گرون شدن دلار و سکه فیلتر کردن، سکه ۱میلیون ۸۴۰ هزار تومن و دلار ۵۸۰۰ تومن بود!
🔴
جالب اینه اون قاضی که حکم فیلتر رو داد بعدا به جرم فساد راهی زندان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145917" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
حمله توپخانه‌ای عربستان به یمن
🔴
منابع خبری از حملات توپخانه‌ای عربستان سعودی به شهرستان مرزی شدا در استان صعده یمن گزارش می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145916" target="_blank">📅 17:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عضو تیم رسانه‌ای قالیباف: بیش از ۵۰ روز است دیگر تفاهمی نداریم و نتوانستیم به حزب‌الله کمک کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145915" target="_blank">📅 17:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145914">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=bYc0pFxc5AHS2EJhchus5gXcoZTRQitkeu9Re6yUPyF-ujL1YLPmWd-c9CM83jwI2Rwc8Gq0FNIwU5IAofsiYLBR8SqA6clxyDxXAki-BRap9t6DXv8Cs93oBMgV_c9Vr_hI3rOPTZfAt1YakLwOIFPEQZKCBXYu6Whf8PCa1fXz2CLSjoWwHeYsqrOAVqiLft2shLXhf1J8D77e2BRKqnhSWLnYopYB7jMC2n-InTr3lrFm41ZOR7kJMigw0W15122JiZ-Er9qpLd-f7DrhJdrJX46rQuCt6P-gEvGbk1KSPMzPhXhWKfbkHV8mCUdHzscgbEOt8_opLwOhBsAczA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=bYc0pFxc5AHS2EJhchus5gXcoZTRQitkeu9Re6yUPyF-ujL1YLPmWd-c9CM83jwI2Rwc8Gq0FNIwU5IAofsiYLBR8SqA6clxyDxXAki-BRap9t6DXv8Cs93oBMgV_c9Vr_hI3rOPTZfAt1YakLwOIFPEQZKCBXYu6Whf8PCa1fXz2CLSjoWwHeYsqrOAVqiLft2shLXhf1J8D77e2BRKqnhSWLnYopYB7jMC2n-InTr3lrFm41ZOR7kJMigw0W15122JiZ-Er9qpLd-f7DrhJdrJX46rQuCt6P-gEvGbk1KSPMzPhXhWKfbkHV8mCUdHzscgbEOt8_opLwOhBsAczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد سامتینگ: قاعده بازی عوض شده و دوران پاسخ متناسب به پایان رسیده است
رئیس مجلس شورای اسلامی روز یکشنبه ۱۵ شهریور، یک روز پس از حمله آمریکا به چند نفتکش ایرانی در خلیج فارس، گفت دوران «پاسخ‌های متناسب» به پایان رسیده است. او همزمان به وجود مشکلات اقتصادی در کشور اذعان کرد.
محمدباقر قالیباف در سخنانی در جلسه علنی مجلس تهدید کرد: «هرگونه تجاوز به منافع و امنیت ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر دریافت خواهد کرد.»
قالیباف که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای بعد از آتش‌بس با آمریکا است، در بخش دیگری از نطق روز یکشنبه گفت: «نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشت مردم فشار جدی وارد کرده است.»
او افزود: «در کنار میدان نظامی، امروز اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است.»
این سخنان یک روز بعد از آن است که قیمت دلار در بازار آزاد ایران تا مرز ۲۲۸ هزار تومان بالا رفت و از سوی دیگر آمارهای رسمی نیز نشان‌گر افزایش شدید تورم در ماه‌های اخیر است.
علی مدنی‌زاده، وزیر اقتصاد ایران، نیز روز یکشنبه گفت واکنش تهران در برابر تشدید فشارهای اقتصادی آمریکا «مقاومت اقتصادی در کنار اصلاحات اقتصادی» است و این دیدگاه را که تحریم‌ها باعث تغییر مسیر ایران خواهند شد، رد کرد.
او با اشاره به اظهارات مقام‌های ارشد دولت دونالد ترامپ درباره اقدام آمریکا برای قطع رابطه ایران با اقتصاد جهانی گفت: «تصور اینکه بتوان با فشار بر اقتصاد ایران، تصمیمات یک ملت را تغییر داد، اشتباه است.»
وزیر اقتصاد ایران افزود: «مسئولیت اصلاح اقتصاد ایران بر عهده دولت و مردم ایران است، نه وزارت خزانه‌داری آمریکا.»
این در حالی است که همزمان وزیر خزانه‌داری آمریکا اعلام کرد ترکیب محاصره دریایی و تحریم‌های گسترده، صادرات نفت و دسترسی جمهوری اسلامی ایران به درآمدهای آن را به‌شدت محدود کرده است.
اسکات بسنت در گفت‌وگو با شبکه فاکس‌نیوز که روز یکشنبه منتشر شد، با اشاره به نقش چین به‌عنوان خریدار اصلی نفت ایران گفت محاصره دریایی مانع خروج محموله‌های تازه شده و برآورد کرد که «احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز نخریده است».
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145914" target="_blank">📅 17:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145913">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VroBZNTuIjmw8c83TybcR9bDaHzVvf08aVvOg2Uqp8ylc5e2QDWcZTXE1J02SMH4FL9jvBqUDdF88OyUn6-qk7GkSDKftn0BJ4CJ2wnv2AhF0INg5o7WTmVo6edkFmIBjmvtY-aE_67MHUnZkkmvPdwaAzRXdIfVxRfMCfb40o5qNQguO6e2OhIyKSsrVPg4q06c_22KzznQrjZUaUzVI3QMSnWjwRaZBQLVE0H0m6eStu5g7Ip88qQDv6k8NV-f0cTSDtUob2PdurWTHalLi0le0pPP1NFzXYsUD51ojaS3oFTCGyMRrqlSWtI5NIfsV3fLqdQs6szyeMzFfaXarw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
فیاض، استاد دانشگاه‌تهران: تو خیلی چیزا از آلمان و اتریش پیشرفته تریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145913" target="_blank">📅 17:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145912">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
طلای ۱۸ عیار 23,504,800 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145912" target="_blank">📅 17:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145911">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
👈
دبیر انجمن فرآورده های دامی:
به علت گرونی نرخ ارز، قیمت سوسیس و کالباس افزایش پیدا خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145911" target="_blank">📅 17:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145910">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: سطح ترانزیت نفت از طریق تنگه هرمز به طور متوسط ​​روزانه 9 میلیون بشکه نفت است.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/145910" target="_blank">📅 16:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145909">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پژو ۲۰۷ اتومات ناقابل ۳ میلیارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/145909" target="_blank">📅 16:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145908">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
👈
سی‌ان‌ان گزارش داد:
نیرو های تحت حمایت عربستان در یمن پس از درگیری‌های شدید با نیرو های حوثی،
وارد حومه شمالی شهر حیس در جنوب بندر استراتژیک الحدیده شدند و آن را تصرف کردند.
🔴
نیرو های تحت حمایت عربستان و امارات در حال پیشروی به سمت بندر استراتژیک الحدیده در سواحل دریای سرخ می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/145908" target="_blank">📅 16:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145907">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14170fc93.mp4?token=kJ-5pORtjR9xMUD3KCSeB54eBS1LaJzv5P2oPVqK8Z7fK_8ssShQ808DM-dDpeqD18YyBg5Vqy5Qpx573-fi2XImCx5BNUQ5vieXIjR4w5LlGatZg06szZSmfe1Elq067s6gMOa7YSg8D4zJ_hztsN269ocJECkEU28wvhnLx40ODXTw-2SWUAV5YU6AUXuiehEPWinVOAsO80O6xaFm99qmDfda4Rt9D16lmzUAZ1hBkfWwZaER1xXmNWmdG4VzKbmswNrxopvCx7pXrjC6sGcthPnWeN5xDehVkL4I7ju_-kdcjDiLplmKsEdxGXB1DCmFNusgcCZE1Za-FQrMww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14170fc93.mp4?token=kJ-5pORtjR9xMUD3KCSeB54eBS1LaJzv5P2oPVqK8Z7fK_8ssShQ808DM-dDpeqD18YyBg5Vqy5Qpx573-fi2XImCx5BNUQ5vieXIjR4w5LlGatZg06szZSmfe1Elq067s6gMOa7YSg8D4zJ_hztsN269ocJECkEU28wvhnLx40ODXTw-2SWUAV5YU6AUXuiehEPWinVOAsO80O6xaFm99qmDfda4Rt9D16lmzUAZ1hBkfWwZaER1xXmNWmdG4VzKbmswNrxopvCx7pXrjC6sGcthPnWeN5xDehVkL4I7ju_-kdcjDiLplmKsEdxGXB1DCmFNusgcCZE1Za-FQrMww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی دست هر پسربچه ای یه چاقو هست و هیچ برخوردی هم باهاش نمیشه واضحه که آخرش به اینجا میرسه...
کشته شدن پسربچه ۱۵ ساله توسط یه پسر دیگه با ضربه چاقو به شاهرگ
📵
هشدار محتوای حساس
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/145907" target="_blank">📅 16:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145906">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndI0LtfydNRDBq-vt_gRP-NidJwiuWvN-_uLb98cOoTp26yUHzrLjpJ4W5rP8b2twAr-QArS_528JSRdZfXgMecBoXPLuKs_SDIF6pMiVeRZReunk9XgCfQTZ9fzLFxt8PvJxzWd3V8yBrO-Za5JNJQW7Pc3TNQxpkqEWL3FyD_Q-FustDeU1F03csnD6SYmFny_LmUKTYDwh79pkXn1bKXY7zv6LvN1Hoy5oc9iHlBBBojcYD-xEN4VEfE9-YBzfHkNQKcsn1ugR4DE-SPZCpMI22ih5B4CKZAGYEGvB82ncYZEjCiltiF98itI-x3P3awWmehM1S7IAN3XZfE2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منچ‌اوسینت: از صبح امروز دست‌کم ۳ نفتکش هنگام تردد در «مسیر عمانی» تنگه هرمز، پس از هشدار نیروی دریایی سپاه درباره بسته بودن این مسیر، تغییر مسیر داده و برگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145906" target="_blank">📅 16:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145905">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">وضعیت جوریه که اگه بگی گرونی شده، به جرم تبلیغ علیه نظام میگیرنت
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145905" target="_blank">📅 16:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145904">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d924e78a9.mp4?token=seSiwnTMB95WcAxAnUIv5ddfUNQDcB-kxsSWI3YkQAbaZrdETqV81eRN8nurTVtBEsYIc4lnSycPdAXGE_l9rbrtFKD6CBT-LUrlJI3ThdUPW_gaeAB0fVG-YTQWT-stxiRpzWl4E0nnS_9wTaFKFxV0tiIiUNlYCAbKimtUjd8Xkapw32v4SG2NKKLjUp-5Ag04hCEu-HsPTfvwCPwqmiwMMB7ollSiq5sHHKxGg8YmYah5yb8auATUFmMIvqXwIpomT7qZ55ZYwihlT6Qyvlzo7mqe383SpkngZ-AAhePCwjonojsYB8_fsQ6IDrNmjZG_oY8Is3QYSpxgxJ4xtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d924e78a9.mp4?token=seSiwnTMB95WcAxAnUIv5ddfUNQDcB-kxsSWI3YkQAbaZrdETqV81eRN8nurTVtBEsYIc4lnSycPdAXGE_l9rbrtFKD6CBT-LUrlJI3ThdUPW_gaeAB0fVG-YTQWT-stxiRpzWl4E0nnS_9wTaFKFxV0tiIiUNlYCAbKimtUjd8Xkapw32v4SG2NKKLjUp-5Ag04hCEu-HsPTfvwCPwqmiwMMB7ollSiq5sHHKxGg8YmYah5yb8auATUFmMIvqXwIpomT7qZ55ZYwihlT6Qyvlzo7mqe383SpkngZ-AAhePCwjonojsYB8_fsQ6IDrNmjZG_oY8Is3QYSpxgxJ4xtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا شخصی که تو یه ویدیو گفته بود دوتا سیب زمینی شده ۱۰۰هزار تومن، دستگیر شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145904" target="_blank">📅 16:07 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

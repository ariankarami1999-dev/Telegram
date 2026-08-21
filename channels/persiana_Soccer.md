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
<img src="https://cdn4.telesco.pe/file/KNK2dGQNjCCP7P6Un-ca7UujtjM4aCAUfUkpa4_BQOx-MLG1jBpQiHqUEOf-qVpbzTb148cK9zK1fgY8aQcFqqqyYpCCgPPI4Esq8uRN6-WgxJspRnktqU1goSa47THEMSNzz50Wt59DERFwO7pkgalrSsbZ47FB2Iw3F_tJFtrUKJfG-BflO7hMpgzdgwhJKBDcbLxVms61RKWpTslv_aPFdZ2ATKWrF7YvGhczPrNInQuxe0f00G8qV7M0-4jTLbV1OR0asFk0bWtMdAzmZRlHnEQ9z_Kbu2n84vGO8H1kGv0HebA9ARey4rGuG0f-OV8UBy0uapSJtdvlLlnMCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 620K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 10:00:41</div>
<hr>

<div class="tg-post" id="msg-28165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035583e200.mp4?token=XreoU6Zip906zfORn8KjDym2Jji9hV7hAW0-41V88h1oSBZdgs81Cze0ZF2C9-JerL9D2-bAfmTGUDqd7h2YUjfn1R3XB-5zXLz8qj5iV9Rzo8E-011szOzMXQ4Hyw49_M124haOKG8hXE0nsQVEb5eFIEIQZpkC6J-B3RCO4CHxvgnGOuplO8FNOZjYLNHI2qJoPzLbKGxEtXxviyuPKAyivOw8b1bwIqc2WqTctl7WBbYAZ26h4bSegrxx2D7atotXW6QbmJhRA4YS50pKUhRBjG75uhlzImbuy4qxfilnP76izQTQ4dMDuE0ItP5P0gVBbmBwmvzM997ELg16YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035583e200.mp4?token=XreoU6Zip906zfORn8KjDym2Jji9hV7hAW0-41V88h1oSBZdgs81Cze0ZF2C9-JerL9D2-bAfmTGUDqd7h2YUjfn1R3XB-5zXLz8qj5iV9Rzo8E-011szOzMXQ4Hyw49_M124haOKG8hXE0nsQVEb5eFIEIQZpkC6J-B3RCO4CHxvgnGOuplO8FNOZjYLNHI2qJoPzLbKGxEtXxviyuPKAyivOw8b1bwIqc2WqTctl7WBbYAZ26h4bSegrxx2D7atotXW6QbmJhRA4YS50pKUhRBjG75uhlzImbuy4qxfilnP76izQTQ4dMDuE0ItP5P0gVBbmBwmvzM997ELg16YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیگه‌فیلم‌های ایرانی هم نمیشه با خانواده دید
؛ این سکانس جنجالی از فیلم «زنده‌شور» رو ببینید؛
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/persiana_Soccer/28165" target="_blank">📅 09:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28164">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1FnPo-88jyReNT5oseOtNnjR1WM0b3eAAWx2Jte_3iL3c8ASeFTCW--SUOQgGxQZZIDvFn2S4ykHmVoNaysaV6axQBc7szAec4IXOkOOTJuciLorARLp9tGehvndNRJycFffANKqg7YG81q9CpUWjnxYxX94fFc8P5_AIavAWW9Q66zPHQKALDKFPbh794tw02VAPKAdSxLp5bPHNe5g2b-Inoh2UepYy0Yyar8Ko3yaP89iK4NWuP0Q6ddgV7IiBS2xWB-oGWGjtFA3O6QasYHpNr3knJPhIJQXxwqhSMYuiPA34W2GrXoBPng6sWNN3-EbuJwPm2CCdBWtYpZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
با اعلام باشگاه بارسلونا؛ ژائو کانسلو مدافع راست تیم‌ملی‌پرتغال و سابق اینترمیلان و الهلال با عقد قراردادی سه ساله رسما به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/persiana_Soccer/28164" target="_blank">📅 09:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28163">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXJLcU6PJX9Qu1bav1uliTS1Ztyn9Cm_JEUrZqOanGQOSf9YdWWvNLF2h5ZvIVEysmgXwOAlWncVqxDxN0LEydr7raNnCxeb7O3gXVDGhGkyX_1euOcJVu7d8FJQcTvlKjPaM7F9qpHSlZF0hNgHao0Y1b8kUH6oxIbuQKkGM-hgW9p9o63u2r8BWbR7Dy1-PkWvytHrL72VqRgnSpPfCqe0a2Itdlt4-_eqbfoTOa0fQHClHDrctkCLZNuq8rinelsSh10H6PZMNncHS9u-727Zf16QO63g2TkYAnYNFBSeU44ttNlvk4LOAQZsQmNQiUjESgk_OQ6D00Dhh_P9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب بالاخره هر کسی هتریک خاص خودشو داره؛ یامال جان آروم‌باش داداش تروقرآن، هنوز 19 سالته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/persiana_Soccer/28163" target="_blank">📅 09:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28162">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc_ohDgGkYbPdKwRs8vKvKtkEuYaPPmLztoDL7x-H39KLZpqzbSQ5pR1GsWxKD4fRS9xOrcikIdC61CUlga57qylexwd6WwMSh0WQBLzLLxZQphQredqkZNFYZXA3oZSrIXdk364T-nQIngZtod_Cnj_fD6tatyte8JJcMlRhxOMZT_SQdv6E58BEKDj6s33Z337BOlF6i-P_g2xSANulaUAJCAjT22w6eiesSeNSGERzF1NrNIZTOg_JsE228l4eLqB08MOGUjRRng4AsMvbNnPB6WZK2CQUr0oJVz6m3qiI6bT3MzoegoQ9AMd8S0hUPptchJrahCC8wqgWeKTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
استقبال‌ویژه‌بازیکنان وکادرفنی‌تیم النصر از کریس رونالدو بعد از ازدواج رسمی‌اش با جورجینا؛ وایب صورت CR7 خیلی خوبه. حلقه دستش رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/28162" target="_blank">📅 01:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28160">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCPwkofKFJ1HCuiqSYiLg_BTEjEgg1pHYq2UeTEU8-Qm_XXWK7SbDgAZIEe1KNb-7q3kuwUBpKS3-aTOgThUHj87eQnbpwZtffqv4wa2QxLCzvFT-3zWgbw7kqoXT4NoQ1BK84vjYieOHGMv2Pv-f5Oo5s0a-7pi8clLHRuHTAUFKWkQT5bHB4WmYb0JQ20i5ZHheslWPLmrl5GTw2afgE-OwmSW4Rs1nL0PgeNjkYfkOP0FtoOlgFMtoLw53VoUOtmb7_7p347igFf2Z7E65FVkulo2fMkIK264m2z8-Ww2rGhQUV7OBuhrQNOm_q8TeHDcYcVeLP_JuEOA7Gg_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
بازی افتتاحیه فصل جدید پریمیرلیگ با دوئل تماشایی شاگردان آرتتا vs لمپارد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/28160" target="_blank">📅 01:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28159">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yb80RCWwg8nctE2kJhjFjQMscPV6QygmEwtUTSx7QdDPsY7ogCwZ9uN5Wy7IhGBojogwKSFIC1Gv3fOrRk_-M4-p6fNCpBV_V5cd_64zKccQOlC4TBkZnJt-GseI0kpnNvFHZ8fGdTCR42kZtLJ9FXu8c7Q10wwJk0VAmuudyVyDVPA62VvEPxLeg19oK0PlBXgh9dorc0Qy26ztAWDBs_NQ9cUB5cjDiwBEaUUFKLRp67Uxtlkuga5MD5dfOXlGa2ryq9nygEqbDrELC8gMXr-gK6HAOxBncwmhCML15ajtLSMQHZ7St7Qw4uNE6GGQ5S_xGXqXc9LJ9LBr93WrPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
آتش‌بازی لخ‌پوزنان در شب درخشش‌اللهیار و دومین‌بردپیاپی الهلال در آغاز لیگ‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/28159" target="_blank">📅 01:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28158">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5Spe96auE7zzbrUr6Cy6KUsP-tHeb1VhTy5PrzShdbpt09yGOKk_nKBRC2tNIakLRZq4aPYZxm11_TZu4PfXKGquP9EmDafbMavInQNhpvJEPhHbKSP2BCdsN7XrxwuSNzwwvRG1P1uerxsg-PLzrWQ8NcbPIuuwCNZqNOPeH9dLkIcjYlKVr-snQ2smw4fTxctQKlwKW5hO9ku7FxeDujdq4jznkt0hvGxATcwIyBJlBcqyzmXQ54IuVQKGUXkxVidt4lRCO238Y-SMTZjy7GfQVuCubIGkJvwDffXpK2aZtEHjcIcx2KRuGLyHPyy7RUG2ZFdjs66310uUGyg1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شروع‌لیگ‌برترانگلیس با‌بیمه ی
🤩
🤩
🤩
🤩
وینرو
🎲
⚽️
آرسنال
⚽️
✖️
⚽️
کاونتری
⏰
امشب ساعت 22:30
🚨
ورزشگاه امارات
🎲
با شارژ حساب کاربری و پیش بینی رقابت های لیگ برتر در صورت پیش بینی اشتباه تا سقف 50 میلیون ریال فری بت از وینرو هدیه بگیرید.
🔥
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sa29
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/28158" target="_blank">📅 01:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28157">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msM_kgdas-OS9lHUFrz4x1EyVcpQkatC_5q__o0_Rtd0rXZYGTRZhiuCa0ff0E0v2vIkWlOzSXDCcMjFV8ifkYaRIqMexCimL0ybV5jSb3JGMYbQ7nJXBuEbNXUjLPYqX87eZHj_iU8zECoC3PrGiFZphtptPzVFyFMCuIaQWD82eBDQ-8es5lsLDN3dp9eLETqwqyr29IBZYLT0CnPRx_5CvOPrJTB654Md2UtFuMARLbzMsndtU3u9ejuFmhQkLATyl6YK58WSbAuao8pgys333Tx5nft31on99zu3VtOYTfE2zKBxAZkZ7wGV83WySWE_bphN3zxr-uQxs8-u1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ علیرضا بیرانوند دروازه‌بان‌تراکتور رایزنی‌های‌خود را با نهادهای ذیربط برای تمدید معافیت‌تحصیلی او به مدت دو سال دیگر آغاز کرده و پالس مثبت هم نشون دادند و به احتمال زیاد بیرانوند شهریوربه‌سربازی‌نخواهدرفت. سهرابیان نیز به همین…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/28157" target="_blank">📅 00:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28156">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw8LMF8191XWCU5scm2Fkb1o121fujZQywyNtLxwl_hyER1e2jdH750rXSVWtKBU3BITmV6EYObvMEtHuWLKd6AlCJHxTVTMjm2AQSvm91c61JPYLr8a-vikLjHUN4RvmdmbeTedK2f-XqHvMJeuwQ_7fuXTL_YSeNuyySwQQdU_y9xWgWq3soYAw-uTeAxozxknvZRBnADYaF4BDawTHjbH8Z6sdd1t1i1yCmqJIT7K23Cdbpk1khwPrcJpwrRevyNw6lWxiW1GXPB-8Xvo8pAuZrGlO8zBqgmeofdPOUTU2anfxcpjAlBfmo7oN3EOO3MAbvr0RsnDogATOUb5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه الوحده امارات: محمد قربانی از تراکتور و پرسپولیس آفر رسمی‌دریافت‌کرده‌. درصورتی که بر سررقم رضایت‌نامه با یکی از این دو باشگاه به توافق برسیم محمد قربانی رو خواهیم فروخت. رقم فروش قربانی رو به دو تیم اعلام کرده‌ایم و منتطر پاسخیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/28156" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28155">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mf3NQmUbW0JPKO2-_xEGzdqnEGa6kGt9HO_uMNrYYJiADjpB4qLYLWlNpTGM6lJe8gd5iLwoqOQM7VXCWhHH1mxx7I4iVaY42AjSL4s7vcJvhIvrDGPWpt_QsmP2HcxgmtvW2r0bTCf3Cb0vk6smIsZh6g7NlMe0tH4HPBzFclVunvrJ_kJvXpwjDAj38delV3ZxjLQu_zDL-0B04lFGUvz-G5QyrXMjdq2jCeGoZagpJkJXmAp3ryIkSWfG9E_ni7Z1Dclzzk1DxCFK-iDLea5sqiCkH4z9jloCTIxTW_NQKFojCQnIE2LJkOoIYKU9zRSu3JNNU_FGP5sDvX4--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچند شکایت به جایی نخواهد رسید.</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/28155" target="_blank">📅 00:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28154">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4_x6fUaI39Wg_z47bm0tccYl9q1THSpLro4BB4phC_fDZczTvHNgJ1YhaRojPA3oODfodHiQDFNGPHzuIdCkIrsLQPtJ140luigidoOGdZZEiVepW3baSRFGJKNwstVPAsneiTkwBwOTlW0sEBpKLTMZkapmWF9HVtfVOgK7GndNARih6nZV9vxPekesPL8kD0Mxmoxlcywq1NWLk7NG_1X3aJyU-HFMpGkNFiSSlg4zlYBE42C77IM2Awr8orXci-1zeAQ4CJR2Ld_dLQimi7aTcIkulgoxdmE69iDvkiGQyboQ5jtRsDEmvA32BsgLi_gWqAg2eN_fJnrAB8N4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/28154" target="_blank">📅 00:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28153">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUTF1G3Hms7H5ZIB0L_O5SRnnahoa5wfFUzHSYn-OoDqkZnNEF-rGEaSugE_3k4dmz3dOpLg_XWea3ucqG1eqk3K94u1QAKlMkZbUoMhADKrNLuQCYUTOil-gWLbMtqzSfDvy2d1f_GlLXPEgH3pAGxZXsXc9naCLA1hEsKB9IBIEIGh3fomtV_H6ELWJFmuFwpmKOY23SeH1qq76HejBXniovz3JGqTqeTUeGzrzEXQ5l5IN56bfg29_P0YMBEEmlDuI9h47u31JKEj5KFmccoLOyJ7PptaEqVw3yx1xnB4xQ5QQLZ0PQ5v5coM6wMAHICGqRDYJAjXvQ4xlF2qfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلیلی‌سرپرست‌پرسپولیس: اگر استقلال تصمیم بگیرد دربی رفت 90-10 باشد چرا که نه ما موافقیم، ‌اتفاق بدی نیست که این قانون یکبار اجرا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/28153" target="_blank">📅 23:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28152">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7QGvai9vj6ZP108S1M2euhjQjJpZMZpYvKVK4ZiR8pX1G5r8G2mg8GvC59zW0NzJcupizaQRY5NmCZM6znHWcktRT7pAAm66WWgUh1TQMThcrjHO69DHjjFYX25dg5sdwgKKF5P5kC81uUWkauVcoVKoSH0iiefm5rfVXm1cDOK6gI8Y-WbzJeEUFpyHtOTm5nMg9Q7DBLUVXKWARqwmK6lu8HcJYdSmv9Hvy6TSA8HGgGUNccJ6Nj0FG2c9886sDxMaKYODPohBwzgiOtLlPWQabZVqLVzejHx5hs3PRvcuNap0Ku3SVT5rpKmQw0VnlHG78F5CXqsNhY3nrVrEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
باشگاه تراکتور با ارسال نامه‌ای به فدراسیون فوتبال‌خواستاربرگزاری‌دیدار حساس این تیم در هفته سوم لیگ برتر مقابل پرسپولیس با حضور حداکثری هواداران این باشگاه در ورزشگاه یادگار تبریز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/28152" target="_blank">📅 23:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28151">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClhIiHKabBHGCAlmfV1tqeDRTR0vIRCTc2-cu0Qfss0x26USf52H2c9f8mKHCVZIXo_E88UP3E3ST7jiSji9DxusPgPs0hIQjA8K1E6aYGIdjA1nDDW0EZJDSQQ2ShAEGVnxeet5rizO8HYqZYs9JcS3NInuGnIAnIZXbxP27isAQUz-2LnB1NpsAxlOyKVFrn3W0GMA6aPeDW6SR8ghva5l1rZ68QZKkmSFW-8rZWCWkOVpbZJq1UY6bnjBIvfdJfWqtl8dyI4CugFynmXAGig7pBOHrixjcCr3VKJYbdHSQy38uwWdb_tbxx-FzN3kHcH062cSa4rSb-xVBKvMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز اینتر میامی مقابل فیلادلفیا؛ بازی دو بر دو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/28151" target="_blank">📅 23:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28150">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dv9-K3oTui068ExHOaZSIEuaiBA6fb57dpgLr3JJQQcN5B3qnmpNaXZqOdoh93n9uD_5rDz9ZeITQk9lCjLpYVEzHePcYZRDhzub9lztOCarRS9PAw9E7tgQnlIP1CPnc8cp5sPbg3cdSVzdnz5tD41Wciv_qt9xJgmjs9bBJS8NLdA71hj_-ijyN3mBDNWhn4-6hhAjMgvL0iiXheUQlmrLX47eiMMxamHYVUXiuNxorzGi_aBD2qLYH1aLRe-U3h8AcyXmk0ZkblWQCt8tJMXAGfobKfRZax1uZcd76_tK-CHAm0SadunRfyzhdU3wRSEJ63bE8L1LkB3uhMRV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#اختصاصی‌پرشیانا #فوری؛ پاسخ‌ منفی ستاره سابق‌بارسا به‌تراکتور:برگردم اولویتم استقلال‌ست.
‼️
منیر الحدادی شب گذشته از طریق مدیربر نامه‌ های ایرانی خود به باشگاه‌تراکتور اعلام کرده باتوجه به‌شرایط منطقه و مخالفت همسرش فعلا برنامه ای برای بازگشت به ایران ندارد…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28150" target="_blank">📅 23:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qAh4IUv3DxlGQ3nUW2FnB0bJd-CJURv-yCsZ3PcVsh5dwyTtae8peehptdJpPjVDmghvQ9-nAjT8y08Sz4yBlFk2uXOVL-5M2ym9KfpirExisGPiq-HUklSod1_-248LLc7ClXvdyetLyJND4fb_TscoE5bgPjIv-xU44Unj-24A3dmOSW-61TRZ9A-EYRbdOz5QlLynWzOkek9V8CcXCJ6I4QEipwr4Q3mYBKqZSXdfaZCVJg9M56z31QkcwA5fRmVHwZj5KX6UvRE9fh5KADVMVlsicyWSwp1YB2WaVDVsMXvcC_ZcQexE1IzftjLCRtIsbG-Geeh5qNlRgsvJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0rbgYMXDT-_U6iKWqOAocH_u2AajKZMWZo1BlP_LxiZTmKrOhFmTVg0WzGBwH8j-0sBD9EEx9QeHqz52eHDMIvW4R8CcEzEPEAUTO5uN3-qetWDDAYdO7RNXcGq7yq7Ire8t05w003cq9nWYM5VLvIj9w6BwZaQ35HFTBZrUHHTJAx4jcPDfrpty-shwxWSVIV745aBeXk-JL_5D2W7rGV_JVIBqQwFK_HrLURTfr6kTM_f2upUJZD1zkr0_gHGDg2kxcAc9dpUBMWlMNqTpYJqa6UqkFZLjVuZ0Bg0lhlVtJitXRwcbKp9uaK9IVvp-c9dKSxHB2pakSb7sbvEKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری ویژه برنامه چمپیونزلیگ که معتقده امسال باشگاه‌رئال‌مادرید قهرمان UCL میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/28148" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPU_4rb1Qj7jt6Am_b9n2_7CFvdgXpLNKCi4Uvo_V0bHYaMwzMzpNFPFgYQ153eJqQWoURb1IeZ5eQvr6hVKHPZKNiNVVOrbbltS_UHxELnLxOzvnhq7qrcRWc4goDaq12XmPskdLEKFzDYgDjTDFjJzM6zER-2gi8FVh_2Jc0fmVxbVpD15Xd6qobkhUZ_mC3TcgYPOT8_Ly5qzohzHbwhxbb_EOGsL6mGJ8PptXAXzOMgtr_8LCyWIx8TfUmv341bVaCMCKmgpzptHXqDrNunUnnIN7EB61rMfJK9PgBpVkTuE2jPNhhU77fXQRlw_7F08got5NbA_4QRG3JJMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوسیل امشب درهفته‌اول لیگ ستارگان قطر به مصاف الریان میره و شش تا از بازیکنان فیکس این تیم ایرانیه: آرشا شکوری، علی نعمتی، امین پیلعلی، امید ابراهیمی، حمیدرضا فیروزی و فرهاد زاوشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28147" target="_blank">📅 22:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihGXBlsE3TdtYdT1RbqD5iAhdGPWf-MCz-N17DypXcaIJ7T2e5OEUXiymgLRbPmF7gsbxVa-jmU7TgmaXbfNV067t7svCUbbVjQWmWqU-B3fX69VDYcGtCADyoPlgjjeTjulA9cLTSls3HzO_mTR-gSzw5lmf8MRZ4SxZYc-VUXnNl5GnkQkLVjfKC9S_aV8IngJ6dFF-Ip7nom0f58bxhM2qz_fQKyW9Rhv2eGFYObcJCt1Oqupwpst2K5o7tkSbPx82UP4E2YeuiWi2DQQAbBLuOUdEUtFC9OXpE44aGEwgkGyQ1iShlrYPv5NgSp1PbOflXVZOXfxbZAERGEG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه الوحده بعدازچندروز امروز رسما تخفیفی 200 هزار دلاری به باشگاه‌پرسپولیس‌داده و بمدیربرنامه‌های قربانی اعلام کرده درصورتیکه باشگاه ایرانی یک میلیون دلار به ما پرداخت کنه رضایت نامه قربانی رو صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28146" target="_blank">📅 21:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAI_q3tkfDaVXhgb8LVxEoyqGVO-jld-YxKeBCPqeNZ_cgF8akO5s_SqH9tGZLbV8v94zE94TSSgfRYwBCEDV3Y8ZxJly7wSh1ffpVaOHjtmlN9_JCjgE3sW5tmUNnrunvkyzza-p8TPaHORyT_bXbsaZ11KfMxNM66YcYnR6dF9NjzLVXKWYrNwBRDgIVIqVIQmhcwhP3TZMY1N-xEpoDcWa7ywwdTIAo5DhGkfiuH3uDWOd81g9ucX5Ql8GBV5skseABYK2Zdz5yko84VD_EyILwszhtqog2gaxZo7PsMzTn39A1JUSIR8kI1Lwf2h7KqMQ_lxd7WqwmhljFvFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت‌امارات: مهدی طارمی به‌آفر 6.5 میلیون یورویی باشگاه الوصل امارات پاسخ مثبت داده و به احتمال زیاد این انتقال بزودی نهایی خواهد شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28145" target="_blank">📅 21:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519060667f.mp4?token=LBngDWDUPtfY9RQh5yET8959lFzZhCjKVjM6z0NZ31T1puOTrLC6oj3a8NkJf25-SDniwZVfSJII4gyjo8ehUqlizE4uf9OibMXjX6Tkho3MtjaXUxvxwMfJW_l4EjrPEU6mxqJNV7BNaHlBgYD1auo7dgA_n_PDLFy1Fw9xWKb0WNnRVMO9q-kZXHodv5qV38osL-D1o17lUQlJ5Fc-0KitpGRvkCAOwOG0eIksXN-DWcZtTlI5wwvqVn5ulqnt0jzKD9uOiLb1z6gQtU8T8EsQApDgr-wQjoUAugbrjkQw3HkSYIvgBe0ku-hwWAPalqNrsecA3zXSJ0aNCsfyPw4LnJtR4bNwhLVofagW1lT1fhnJv_ILNXsAZZbKtQeQ95ZGjHihepSYmdi70rTjta4OIop1QHOaSfYOxShecj6ANHeA3bKQXZbxqof4RO4y_mBvOMNgjN-iHJTR-X-Qy8mcW-XbA8EkLe24zB08TIBCze_H161cK3g0qQiGWuB2FmtoIdhp7keHufYxNFdpoNcbikNZnvFUWGOuhz1UgaNmAvLkP-RAErwI6pW1-c3S2pcmn7M3KZBv_DROG_OrT50b4VKSWndLUb3aiWUoO1FvP73RAsSv5qyMKxDVFzh5FEDHWF-OuOcvYc5GDgUID7BcNMk79uhLZP_zRlckbqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519060667f.mp4?token=LBngDWDUPtfY9RQh5yET8959lFzZhCjKVjM6z0NZ31T1puOTrLC6oj3a8NkJf25-SDniwZVfSJII4gyjo8ehUqlizE4uf9OibMXjX6Tkho3MtjaXUxvxwMfJW_l4EjrPEU6mxqJNV7BNaHlBgYD1auo7dgA_n_PDLFy1Fw9xWKb0WNnRVMO9q-kZXHodv5qV38osL-D1o17lUQlJ5Fc-0KitpGRvkCAOwOG0eIksXN-DWcZtTlI5wwvqVn5ulqnt0jzKD9uOiLb1z6gQtU8T8EsQApDgr-wQjoUAugbrjkQw3HkSYIvgBe0ku-hwWAPalqNrsecA3zXSJ0aNCsfyPw4LnJtR4bNwhLVofagW1lT1fhnJv_ILNXsAZZbKtQeQ95ZGjHihepSYmdi70rTjta4OIop1QHOaSfYOxShecj6ANHeA3bKQXZbxqof4RO4y_mBvOMNgjN-iHJTR-X-Qy8mcW-XbA8EkLe24zB08TIBCze_H161cK3g0qQiGWuB2FmtoIdhp7keHufYxNFdpoNcbikNZnvFUWGOuhz1UgaNmAvLkP-RAErwI6pW1-c3S2pcmn7M3KZBv_DROG_OrT50b4VKSWndLUb3aiWUoO1FvP73RAsSv5qyMKxDVFzh5FEDHWF-OuOcvYc5GDgUID7BcNMk79uhLZP_zRlckbqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گلزنی‌دوباره اللهیار صیادمنش برای لخ پوزنان این بار در بازی امشب این تیم مقابل تیم کلاکسویک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28144" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twl8zhxZTqeT55UhyOvwT6f2VG20g2viFYkaFX1ehhTzvq_3Rg_LJd4dgkeBfOaA9ZA2KvfIXluYisJenfcbEJoVROnOoOwyVVQiZLzpIdmm8cwMz271wafeLWa-x9y4uzOvYRASkziwprDEUSf-ojCldbpHyDafNmw4cEXMZSXG9s4DIv-FwJpz6VAZbJBxxJPPQhU2PEvQDSpUDIHl_54Yhv-CDzve5HOD5LQy_FeqTepUpZZaUJ72JIBv-qBPUzSOOb1ZlAx1DLa7TFFLZxC2GhOQviTjPLiu5xZXgc1J5iJsrDbmKIyJ1lDAMacxcY08KCJjgTZK_04ZN4dSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28143" target="_blank">📅 20:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28142">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d47c7d57.mp4?token=D7fK-3yzRPIUHzX8CdifdDfw_YBJVLUXRmYsYmsUpPfnmodw7X42ZUIA3vEvW9qRiqXOymao1cCJ5adQfA6X9hTGP-mD8UFdhLT_qpRdWBSzWHwgCCGueq82piJRd5c0rys7nCF2H14YdjeX7i5ph9d-J69Wx5OPsIxjJgHkqRom6P7Bu9ifjF7Tgc27sWkv_yY1Vmty59C1sg3Fh1DAfX-_tHlH21BNoUNwlcGzt57qhTMjfXsih81cgWz90_rzeqPolv_ZJWF6sG5Nt_lnRh5HtCse6vSHIgo-y84QLrOOb2E90RWKge2wbDnLaBHSZR9nz0Wsjm8vdr9pfRzt7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d47c7d57.mp4?token=D7fK-3yzRPIUHzX8CdifdDfw_YBJVLUXRmYsYmsUpPfnmodw7X42ZUIA3vEvW9qRiqXOymao1cCJ5adQfA6X9hTGP-mD8UFdhLT_qpRdWBSzWHwgCCGueq82piJRd5c0rys7nCF2H14YdjeX7i5ph9d-J69Wx5OPsIxjJgHkqRom6P7Bu9ifjF7Tgc27sWkv_yY1Vmty59C1sg3Fh1DAfX-_tHlH21BNoUNwlcGzt57qhTMjfXsih81cgWz90_rzeqPolv_ZJWF6sG5Nt_lnRh5HtCse6vSHIgo-y84QLrOOb2E90RWKge2wbDnLaBHSZR9nz0Wsjm8vdr9pfRzt7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیویی‌از عملکرد خیره کننده تئو والکات ستاره سابق آرسنال دراین تیم؛ به هیچ عنوان از دست ندید ببینید و لذت ببرید از سوپرگل‌هایی که زده‌. اگه الان میبود قطعا ارزشش بالای 250 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28142" target="_blank">📅 20:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a281101a.mp4?token=QRt7mSLlDwxLZJFwLwjAsd9DRY9BEe_IsjbXZDHVcUEb4uM3IHXB0_ib4R2vKgTbmOay7v99Ew5ou3z-8VM6lI7WFKpQk-5SK9lufmpV1YZz3b1NBmw9PiHf3ziE8Xnzf8MyFd32MrJT28HeylmBeoHAPqTtmCK4u2JLaLqnKpu7hqq_qGLrZDVA1G16Z6AyR7ec3Qr1aqzDaaTnHEA5gO-EhvrR4vbbPNAXHVU_kWOr_27A3L2nT1cAUihqIsdla8cCHaiTFUd3SYmagqmueZamoLt9LHP3O49jecHqQfzXeUBk9Yaj7BFrq_wKrITwpRvopPDPzK6CME1is5igBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a281101a.mp4?token=QRt7mSLlDwxLZJFwLwjAsd9DRY9BEe_IsjbXZDHVcUEb4uM3IHXB0_ib4R2vKgTbmOay7v99Ew5ou3z-8VM6lI7WFKpQk-5SK9lufmpV1YZz3b1NBmw9PiHf3ziE8Xnzf8MyFd32MrJT28HeylmBeoHAPqTtmCK4u2JLaLqnKpu7hqq_qGLrZDVA1G16Z6AyR7ec3Qr1aqzDaaTnHEA5gO-EhvrR4vbbPNAXHVU_kWOr_27A3L2nT1cAUihqIsdla8cCHaiTFUd3SYmagqmueZamoLt9LHP3O49jecHqQfzXeUBk9Yaj7BFrq_wKrITwpRvopPDPzK6CME1is5igBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فوری؛ کریستیانو رونالدو اسطوره تاریخ فوتبال: احتمالا این‌آخرین‌سال‌حضورم درفوتبال باشه و میخوام یه‌میراث فوق‌العاده از خودم به جا بذارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28141" target="_blank">📅 20:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28139">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4de76fc0f.mp4?token=PDY-exZc7My1C9Cgmv6qQ2mfB4-tGMWRuS1NXbuERgf0e4b3ShwyMTumciwcCBgdbgCG2h6HLc9vxuYVPDwun_iwqtTeSQYex-cEPlwk8PV0lsjtRnwXi-eZFcbY9YhHTBAA_6GRHBWywgFodwepkjJgD7ZXKk_R7-F4BoRjasgl5EE-Zc4W-x3hv-CvQfY1OF6bf4aI46BqWQXBc8oKLyzRaA6ZHZdeQo6dZmimrq5JcqvjLMH3gvQsEbXF5VYoeLNh7LHxb5ZPol6Ug8v-sTe6wby2QWhVcuF3i0elotuQMvhoOGM8ndPq3NBLeHsJ8ioPNrSgONrHIdyhB2AZ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4de76fc0f.mp4?token=PDY-exZc7My1C9Cgmv6qQ2mfB4-tGMWRuS1NXbuERgf0e4b3ShwyMTumciwcCBgdbgCG2h6HLc9vxuYVPDwun_iwqtTeSQYex-cEPlwk8PV0lsjtRnwXi-eZFcbY9YhHTBAA_6GRHBWywgFodwepkjJgD7ZXKk_R7-F4BoRjasgl5EE-Zc4W-x3hv-CvQfY1OF6bf4aI46BqWQXBc8oKLyzRaA6ZHZdeQo6dZmimrq5JcqvjLMH3gvQsEbXF5VYoeLNh7LHxb5ZPol6Ug8v-sTe6wby2QWhVcuF3i0elotuQMvhoOGM8ndPq3NBLeHsJ8ioPNrSgONrHIdyhB2AZ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول پرسپولیس به اس. خوزستان توسط محمد خدابنده لو در دقیقه 6 روی پاس علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28139" target="_blank">📅 19:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28138">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28138" target="_blank">📅 19:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28137">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBFMuwV7D1_yGvVevwC5UT8G6GO6nwCUCkgOG2zcMRZGx7IyARr6fGM57beOqY0mE3NmNo3CeU05hgS2UTkazibhbjrc7lOYr0uYYyNNbIs3Qp58ktB11Db5TRuqLJYnLmIPNJ1MUOq707-N3mJHFsL7aM6qSbgz3iL_Uy_POH6OM2J9HF4OjLg5v6rBExOyLURTfopGN4mlUPubu3OAFsDQI6byqJPjqKfRcaBQzteB6vHR1md4mC3dwFbjlu3MEgn3Ztge8gS52yBYue3rmzT_hz-AlNGoMS_YBFSCakYsuPDALfgxoD9iqSMSJ7yLVdxymWIdlJK9jFCr65NmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آلباسته برای منیر الحدادی ستاره مراکشی جدیداین‌تیم؛ کل دستمزدش برای  دو فصل حضور در این تیم 900 هزار دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28137" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28136">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSAtQM3F4a0eBlSEltBlrYs5CKkdpsWCZufZXWssxpbeS9bVb3D35v1tvW2rKGeOZnolk1nJeXKuuAUevddLAoaNwJYoxkLD9N9dfBObXyPckOmYj_oDrq3tAr_Jr12AFFUI1SDLE6K0GmmSWmS1mP5ytrAuhwSBs1VmUu81q7fl4cr3fAGqhg1aPGbdqPmpTz3h6VKlno8-Xn2LFS28owMbsA52Yx5Tp9ZVKX_U6RfCXjCQK_7Gzf56odHLwDCdvW_aTkLr4EiaRtTAv6-AXS7Dhw6SEEb4ElCSy9R9EjOAH_Gqkxx8k7ztG8OuR7BwVm9u7LgtRF5xRT0VC-Q1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ علی نعمتی مدافع‌میانی‌سابق تیم‌های پرسپولیس و فولاد خوزستان با عقد قرار دادی دو ساله به تیم لوسیل، قهرمان لیگ یک قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28136" target="_blank">📅 19:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28135">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJRizaq8bXt21RasQOXSZWR1WmO6vCIxNDgzLn3rtsFK_wTr4wj8mcLoiX0gHZQdyIOMGQkl6hKVNjGirrAPs8ty2-63gma-9wrMZl5sU2oRuBv0kcNZwiPghCChxkn4Cl79PQoeXiBSXknY7XNYYVi6x7nXEFy_z78ZfDO4hw5MLmdpH51IJtJmK0W3svKb0M8YHXY_DJ7cscJZvlnzKkExKEkPC5GPkPl4IPT8WQHppJg0t1VOgMgwT1Kroi8Wmdf9wHCy9NHWwxP_xSV8_JxufmgbkQQhLtxe0lvqXtu-WRq60QaHpuL4mTmKWmbpQ0_PTEBSGe5aWhOEWPpSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونالدینیو شاعر فوتبال‌جهان میخواد در سن ۴۶ به‌مستطیل‌سبزبرگرده و برای تیم راوانا در لیگ سوم فوتبال‌ایتالیا که بخشی‌از سهام این باشگاه روخریده بازی کنه. رونالدینیو اعتقاد داره میتونه کمک کنه که این تیم در سال‌های آینده بسری‌آ ایتالیا صعود کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28135" target="_blank">📅 18:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqghTluTIo9lufgcrRY4QMGy2Mz0seWQYdtIrrx0BpPuhSlBd-6IiFdsaP6JDugLjvFfCnKNXlrmJVMLbs_NTMHqPbRXunjpX0ODXuQF8vtIgEKdOwBTJ2w1VqBZ_d4at8aSUNnn4qpAMtN8QBBTCy-50eds5WsY3J477QQbAzwSrRE0R7DTtR_uPWgqRKEzQeTr4zuKE_iziug6BUIPjo8kqaBStnY58AvLVyumWavg3x45DdR42iwO_mgqj9q9RzCOKkyQc74pQy-fe728TPHNC8ZH8aGG7kcNcWrEzsKDRYCyb8nYmZgOJRlKB1nQsa-bQ0zg_OFckZL65KQA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28134" target="_blank">📅 18:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad771d7af7.mp4?token=n9g17yWcchR9O0qXqkWgrfZaUmfv4wNO6Sg3Co7-SSgzGnpQA2Vx2wafcwhNjFw__x0OghfqW7OrwFl377vZUMM49EmWj7d2cXQmZ23UjAuK-INA2pO0r108ZUJ1yvTm0t64F5box2AYkVTd1EEYW8_F31jO1-hGl5aK_o8hmKUzhyarqjI2ujn-ikboVdZb0jONyzEzwyMENbcUS9DDNSJedDEYeIQ0HxviUgQiTR5sRrnjl7uSmoUXep18u7uuOziqrhhGKNFFW1K-Tb9FahkdfyXdW5YNfv6VtccGA3NTH3mY9reWKDnUUcnO6c1D0Zj1AtYzEqtzObz4dbPWuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad771d7af7.mp4?token=n9g17yWcchR9O0qXqkWgrfZaUmfv4wNO6Sg3Co7-SSgzGnpQA2Vx2wafcwhNjFw__x0OghfqW7OrwFl377vZUMM49EmWj7d2cXQmZ23UjAuK-INA2pO0r108ZUJ1yvTm0t64F5box2AYkVTd1EEYW8_F31jO1-hGl5aK_o8hmKUzhyarqjI2ujn-ikboVdZb0jONyzEzwyMENbcUS9DDNSJedDEYeIQ0HxviUgQiTR5sRrnjl7uSmoUXep18u7uuOziqrhhGKNFFW1K-Tb9FahkdfyXdW5YNfv6VtccGA3NTH3mY9reWKDnUUcnO6c1D0Zj1AtYzEqtzObz4dbPWuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🇮🇷
تیپ‌واستایل روزگذشته رامین رضاییان روی نیمکت تیم فولاد 11.5 میلیارد تومان ارزشش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28133" target="_blank">📅 18:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJpMDXnwM5X6J44exGNGMRqV_YbFA93u259qmq6EhlcPtT8yt9SBvrwLkyJfpatczE340DPvWx10eh3Mq8a9kDhld2bv5q49ZKnqJnY-sTRT8B0sOCQMBo069HT4_l8s4Ci0F1CtD73GnOwEDhYZe8r1t-ybP0Rb3UZMznNfNmJi2-9IsYFcmZGyFCAOX7YitYu7605fi9LjIcr0njL4UDDthgSN3bw5WOXNHE5y3kK6F6YOwMQymBuDyRpmdDxOnJTn-KGqI0yaBYEFc-z1ih1PSt8jqkm5u4ieeqxJ27zvp89f9NLgVcY8titEfEdNHhTtzeOQbmLZ9IP2zGp7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28132" target="_blank">📅 17:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avd5XC3AjmjMlpxHBAsL807zYhxNzhyIn0-5Z07MzaX8_GQQGt4krGMt9fQe5SIbpf0_IVTzJIkAGNsweK7fEzCd51owJxJUvJfWpI1NXMZlV65k-xBGdOHCfXKkGW0yRhrAX7ZiKCKaXnVRsfCReECrmjfuFfE1ugqcHnmcHAVlH-63xOhHh5FXwQHHbx8IDf7GpzD74knku2ssMpOz2mPAnc0FaF2-54Lh-MrQPgimE8nJazZGEAhsuIsa7Nfx_vtIwQ5qXNgdiRBWOPW7vtrUytrp1-NzJwbfABVsu8XfMCeVpi6bQ2lq5hTacA9_Sb9YF934EBc1gKDdsRoeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های پرشیانا؛ باشگاه شباب الاهلی امارات پیشنهادی دوساله سالانه به ارزش 2.5 میلیون دلار به مهدی طارمی داده و به ایجنت او اعلام کرده حاضرند که رضایت المپیاکوس رو هم بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28131" target="_blank">📅 17:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqkO6n4nKRwZMRYov2ZN48CmuaKVHJqJm1bu9KflZJLikfmTJNT-GfnC26al942zlXBHP5Esl6DXF7LoFbp56zEOuUFqOZaLqoD98l1TQrRLkGXMYier6tfQExnha-s3Q9VgytzFCqnGZaiyJxFDBSjYH5U-76Z9FHD8zoIyaA_yfl-nXAN6NXXzMoU9N1b8BPgPYUvgpszImkE0mrH1spTtvh20SnxLnpSf9ncw3rqB7Ig5rINmhVBmIgnYGOV7XaH12nAFVTxlHFovL2oGBXpK-MKDNtupn32OHhUFDfWkDtg2TJWfZsoPG7-2nRM7NMZdk-96n6aXCcyf0Vh60g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ شهاب‌الدین‌عزیزی‌خادم‌رئیس‌سابق فدراسیون فوتبال روز چهار شنبه با مدیران هلدینگ خلیج فارس جلسه مهمی برگزارخواهدکردودرصورتیکه‌طرفین به تفاهم برسند عزیزی خادم مدیرعامل استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28130" target="_blank">📅 17:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90cdb5f68b.mp4?token=sk5NgfR9pjHBids_SooaCeDn5pz3jIS9uw0tFPfcxjdRfduUpvoCmVn0SaO9twnamRsYsjyySsIFelxGevlsRRoBIMNWv_q0Yn2p54MXN13Ygo3bchjGxdqEJEmdjOrBRYp63jYammvu3IPkSpNLeB471avSX81xXTr5eBAzDqNko2JyIZ5o0sV0layBgZaPvzneAJDaXCNAsysRM5Z4M2GbElyIJtsDF4UmRo0eUBlRRA6upim0lTeACiJ-5zw37U_4ulPVaHPA1CIcTRIFcNNOVo0S0PGlTGI7QFHy8V8oHMvi7rW_3X8YLQnKP570nQfHkuQHtzBPPu7XLfWbvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90cdb5f68b.mp4?token=sk5NgfR9pjHBids_SooaCeDn5pz3jIS9uw0tFPfcxjdRfduUpvoCmVn0SaO9twnamRsYsjyySsIFelxGevlsRRoBIMNWv_q0Yn2p54MXN13Ygo3bchjGxdqEJEmdjOrBRYp63jYammvu3IPkSpNLeB471avSX81xXTr5eBAzDqNko2JyIZ5o0sV0layBgZaPvzneAJDaXCNAsysRM5Z4M2GbElyIJtsDF4UmRo0eUBlRRA6upim0lTeACiJ-5zw37U_4ulPVaHPA1CIcTRIFcNNOVo0S0PGlTGI7QFHy8V8oHMvi7rW_3X8YLQnKP570nQfHkuQHtzBPPu7XLfWbvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رضا گلزاز بازیگر سینما و تلویزیون به این شکل از خودرو جدید رونمایی کرد؛ رولزرویس کالینان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28129" target="_blank">📅 17:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-yWfhSxQtDcd1pS1ngEojRwMHI1HWz7_2cP6w94boNf2uKsvZL8CgynUtnE6kHtrNr6eO7fUsJUyOPtD-TrAfTdpmNzR-6wCjc6K_t50jns1XPrxt5hd35b_tprigMUiaJ-SxAnGuZMa4UsDLGsliJKp9qOyNPX-YL9cpUx2NQX1H8dIvWOCGWfYWeg6HSVu2X9Bb9OOIfQ72qFMB1ClABDuJCOqoVtxvcGgiN6QJ882xezTJOxITimjQw10d865oSbqdSRQK7sgFg8cxAc54X6Dk54UHKeeBNFCc_RSzoULRJEUzbNkPXVhvDuhaD15H1D7PAjvmYr_pt69hCbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی؛ کادرپزشکی‌باشگاه استقلال در تلاش است‌که مهران احمدی ستاره آبی‌ها رو به دیدار هفته‌پنجم باتیم پرسپولیس برسونه. غیب احمدی در چهار هفته ابتدایی لیگ برتر قطعی شده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28128" target="_blank">📅 16:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG8z3GnGRxw7A1_cC_PmRZWhYgcgOfFcY-GpdKRtXVYBbo33EevJaBvtwQ2QywJAS39oKItthtuQN76y0dv3Ghhk6AUQetYq1Sx_fQqIt4JODsH4iAdMJvnqQCKgM9uGHwTw8nPS97_KeOLM_VqTGOHI8-aGgqH2l-mlJmSvUKpQqJAnFIqKSUVoMFatymMB1pTLs0ic95gHmYpBGm1Dch6L9KMGfJq0voXuYgv7Il3SqbPmFScMJw1OsUipOLa-is7LAYOdadbaKi5Q2kX8jvz2LmEkdfFKT0Joa3lhrWwrkDdqJWsG2G0An_0jEpb071Rc1UMed6r6Lg-dntsW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
با اعلام رومانو؛ ژائو کانسلو مدافع 32 ساله سابق اینتر میلان با عقد قراردادی آزاد به مدت 2+1 فصل به تیم بارسلونا پیوست‌. کانسلو پرتغالی فصل گذشته قرضی در جمع آبی اناری حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28127" target="_blank">📅 16:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28126">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWueI2J7NggooIFq79XeIXFb49j29duSqrnMSzhqG5xOep0ZhMWeMKxFr-8Dm3bBsMmKwQICdb7RiZBr3G66niq9U9FDLRQImKx-cJph1qY07bVJ_8lcHp7_DomcmyFFDiNrdakuyzA2S53gqXyJjd7NArjGfXgMSGOVz2V8mFE7LkwZg_dvpXlvL2hU9f45N0ijnhEMBOsbs5s0pHwJkQJGOIWqo1MWuTjmclLrq3J1yZoGBnpFanX9OElOr_fjSiNpaylN-Iyzu1Cg4c5sA0eacUsp6R5RWG6unTmSh2wcS2RcdFEul1waSX-FWzT9gtH_2Bfhn9LGWEWQJZrGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛موندو: دستمزدسالانه منیر الحدادی در آلباسته 450 هزار دلاره درحالی در استقلال سال اول 950 هزار دلار و سال دوم 1.2 میلیون‌ دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28126" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28125">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3278Td8rQwRigL2AoknwFuYMjuiXBtZTCjmIqhyuy0p1L61H6Fni7_8pkuXC8J-mHX0ytxZ_M6CICRswbd0GGRH86-5cE5ySkKWMUv6eJVCKlW83ChAVeKs-TT_DmImYuPJ5X_za5JUE9blvFkdX8Rt9nbiOsHMKIEJzgplXvuSB1_-xiJ1bdy34JSOYmLn2FqFfBNdWPLqfcq1Wv1Qf0O-HM7cxtuZhXs_wHJMYdDgm2UMZwE69xk9i7coRU1wtJ_w9F004RI4ZVr2224Jf35kCPnomlSQf9neklkm2JnsWGdHrChKKAeumMDOYwaHU9wG8If_l3m4m0he7FiZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری‌عادی وحید قلیچ پیشکسوت باشگاه پرسپولیس؛ رئیس فدراسیون روسیه به دنبال قلیچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28125" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28124">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXvCfD6bx-RBV92JewhoNLNJrci-cyeIKCqINkJT2P_lwc8xMXdtVe3ILRPtPbnzgjLRdAKJvIlovP2bbPVGyKJpiRIuXHcjsNo8G9XpV_JG_ITplwi4poKoyhjui_F2v1oImIfCn3C8BpGwK5IBFnXNWcH9AwjcUnTeCXSs_tLYospr82hwuD1r25E6DG8zcsHJsN5cuJdNPMVfAAcVZ1UGxJVRlHaU2e_oBPysYGyRfcq_cOx9mRAZ0DOuYRcpjXVkCiSzSr0zwkSU26Wel2vosN36t-BJoHK2TrwFbapfBh-Rq9vd3gw0RwgbNxQ0q8cR8LgRUYLoecPEVcGkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
هفته دوم لیگ عربستان
🇸🇦
الفیحا
🆚
الهلال
🇸🇦
⏰
ساعت ۲۱:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش‌بینی
💵
واریز و برداشت ارزی و ریالی
❗️
💰
۲۰٪ بونوس روی بالاترین واریز روزانه
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28124" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28123">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roBq4-5BlhoKpVHG23omFFK8eBjXINWmeQ6eARw1ibalA3sJrmrEZvu6Z_ZwpIXtQzh3vMBMHzPeL7mdXA-n5DParWrDbtBNE7R1HmkbU_gqnXfPdfBdVcnruvy2PXV-qlY5wni4GLRkEYY1NzzvmFErkZfRHW3W_wuo_ZhXBWGQdlZT0rQ1Qpu3Z0ASmCerOKXJc4osuU_4v8V5Wc5Ch0-u4cWJCQysNznEK7CLlM9ijURR99fYgEu_wT369UMKz809Mk9xsKacni4fcT_eZQuXp0s_gMXGx0j-QU3AiFfUIkm6dKKw0bkwWKmWmee_v6wPjHD8gg2GXozc4hj4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رودری با پیراهن بارسلونا پیش از دیدار با الاهلی مصر در جام چهار جانبه خوان گامپر؛ این اولین بازی رودری برای آبی اناری‌ها بعد از پیوستن به این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28123" target="_blank">📅 15:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28122">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEu_SIoe764S0D1ErWc6r9tdoiRh7owRVMMAV2VLKHTbTj_gU1_eJFZhsjK6_rK1oAUWpjQ_bCFOmyXOGcs6W_KYh8w0pN2RwX0zwtc7yt-ZTMLv9ftpv-zoTFFvpAYFGAdcVugdZq3j9MjGGaCcsjK3ZlAndIWOrnmffAACyRhqtzAAg1EsbjBkzmqaVev7zNwzpugqgmaOiLJ5iVeuDO7Sv705FHqwd_eg9lUQ_LXvkhHcn2mA2V2bFmQ7LG6VpRjHC1RzJMcBW6CLsICzzLx_0vlJ3QlE8CEVh-1UgE0z0p1N3OsxF9H2VIOE0HWvnJ5jdWOL2Tf7WJMdnOuPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
تنها سه و چهار روز تا شروع دو دیدار فوق العاده حساس هفته سوم رقابت های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28122" target="_blank">📅 15:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28121">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caedc143e7.mp4?token=MoAQu6Tb4O81BC1xwbkty-toHAaFBhBd7qcgrRbpYqm_AWaB8wuXIre0m2BzuFDhNa9tXi72xv__kRzSYH0Vr3TSrUzsFkgUBtswo49VRwF1GzfrT0GKXYxSgc4wcUx45uTSaAfyUP9-VjrDOnMrxXxKqnJdV7cZDmX10FAgQU86b1eSI_zvHU179dnT6y9A3iiclGkMUrmct6hoSK2ZMCIP71Ld89NvcEMnpjfs0grP_sqbEuzn54NWkzBQDS23IFsJfZeFKKckFx0SX82Jhk7xRh1vIX9RLgi2y5MPZOfjUNT3No78tpfQu4ThMTbMceNFgCkhVNakSo6uDEG82Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caedc143e7.mp4?token=MoAQu6Tb4O81BC1xwbkty-toHAaFBhBd7qcgrRbpYqm_AWaB8wuXIre0m2BzuFDhNa9tXi72xv__kRzSYH0Vr3TSrUzsFkgUBtswo49VRwF1GzfrT0GKXYxSgc4wcUx45uTSaAfyUP9-VjrDOnMrxXxKqnJdV7cZDmX10FAgQU86b1eSI_zvHU179dnT6y9A3iiclGkMUrmct6hoSK2ZMCIP71Ld89NvcEMnpjfs0grP_sqbEuzn54NWkzBQDS23IFsJfZeFKKckFx0SX82Jhk7xRh1vIX9RLgi2y5MPZOfjUNT3No78tpfQu4ThMTbMceNFgCkhVNakSo6uDEG82Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
لیونل‌مسی‌از وقتی‌باباش فوت شده اعصاب نداره بعد درحاشیه‌ دیداربامداد امروز یکی از بازیکن فیلادلفیا هم‌تو یه‌صحنه‌رفت‌رو مخ لیونل‌مسی اونم باپس گردنی خدابوند تو سر بازیکن فیلادلفیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28121" target="_blank">📅 15:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28120">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M97d_Ux5ZNk5AdUmk2DuWsfYifPrymKA1obKNfRdTAO5Qgk3omIIsUaeF3UVXE5a_kCO-9zRJwHOnQA9U1tDes_wtv99Y9Mjd6rxKP8nUfbDzZktKvespHelfi49cr6Nz0YXWlLsxpaY0FfE8xciNZ26w_305Ez7fUzAT9N3iEjKB1Qq7JcaHUmi4EEjxh8O83Z0DPBgrLaJHAS9SMdauhUjYfcEcXhVLiJUm0naCGgAX5hKnlq_e5dw4cuuH6N8zrO3xbL3wdPDXxSPGfID-PdnSklDMwG9bR_RRovKX5X7ytbft7nREQG72QUMfhl5uTLRC9AQfsS_U3U-DE-O1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حضور الحدادی ستاره مراکشی سابق استقلال در محل تمرین الباسته حاضر در لالیگا دو!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28120" target="_blank">📅 14:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28119">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deb1cfe6c0.mp4?token=qVy35lN2L5Brcamr2H2G3n0C5qOeeg78rgt5YMtPhHaxz6eI--OX_oyjjckBnTuKTzhmNb2nlgUFG5wQtJd0ncTDYRwM_Yn2pDNvi7TR2tL10SN9bC-JfJUx9pJ_sw7U_9bPbBGgA5Wo0PMgWsIPPVC9x1YgulDBurciQTQ8k9KhSovEnNRBwPV9FR1Mg0NX4FT-iKW_kb6EYpFqX7SZLU4gfKUKbipkSKDa7nn4yq3FoWZyLZa0RUE2NaMgY0n-bocEIBN70QD5saHz_e7OfNTXQ2xvW3U4xT_KwuraiaZfZfxWkj4hY0EZkcUm_UwCnwsD1D3yeL6KbWSDy-qrkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deb1cfe6c0.mp4?token=qVy35lN2L5Brcamr2H2G3n0C5qOeeg78rgt5YMtPhHaxz6eI--OX_oyjjckBnTuKTzhmNb2nlgUFG5wQtJd0ncTDYRwM_Yn2pDNvi7TR2tL10SN9bC-JfJUx9pJ_sw7U_9bPbBGgA5Wo0PMgWsIPPVC9x1YgulDBurciQTQ8k9KhSovEnNRBwPV9FR1Mg0NX4FT-iKW_kb6EYpFqX7SZLU4gfKUKbipkSKDa7nn4yq3FoWZyLZa0RUE2NaMgY0n-bocEIBN70QD5saHz_e7OfNTXQ2xvW3U4xT_KwuraiaZfZfxWkj4hY0EZkcUm_UwCnwsD1D3yeL6KbWSDy-qrkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های جالب پپ گواردیولا در رختکن پس از باخت ۲-۰ به یوونتوس، دو سال پیش: بچه‌ها، می‌خوام الان یه چیزی اعتراف کنم. من از زیباترین زن این سیاره طلاق گرفتم، همسرم، همسرسابقم! عاشقش‌بودم‌دیوانه‌وار، ولی دیگه شور و شوقمون از بین رفت. عاشقشم؟ قطعا آره. اونم عاشقمه؟…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28119" target="_blank">📅 14:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28118">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbdUOf-nhNaW7NpStb7LbOFyoIa2Iy9MFqfd7ClQ5Jy3GgCmU-L7_tIABvYAwz7kel318FcleiKIBQucjID6aJ-GrjDIJ-qIBdDDfFIHgR4k4V5odDfjqsN1DzDAtAda68vlxA12OZLeov3JhGeaLaBEq_ZFXJOwUbjfEL8lnYzb8FJr4gp1VyCkg2WcIdYB-UJMTfpuqA53nvXKLJRX8XeJQ1DIGdrOWUPa5edr8993dOXGGRtVbP8zZIQaqQz373kYF4qWrsQLGtRWj8fYK8Sa5tHR4u-gS_yWrs5iM54DzXapAqldsUo_BJIAULVDPNqGvji7m3EucE_Km_aGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای دومین هفته پیاپی؛ محمد حسین صادقی وینگرجوان‌سرخپوشان از لیست این تیم خط خورد. ابرقویی هم دیگر بازیکن خط خورده تیم تارتار بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28118" target="_blank">📅 13:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28117">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsPRbhgKLs_BwvWPbq8uSiV4I-9YlBbdXW8JlVOzrRZVZyHtlMiiXXQL86PPBTot9eDklv1Ao-cCCn546LaaAn-iFZ8ehm0voRxVyrNXyyspDaRLp5e_y1KXcYDNyVR3n7dR9J8Q7H0nP9VWKtU0ojPGLPy5-57RbEC0GQG6AojI1r9g_i3idq01JVNsSweZlXvM5mOriXJAbOR5O-EyeMpBLuNCNiDtFujeNqhs3Q0GXlt5o_soAmeM3KRk2gejEFEI6lWY6gf2AzDGdDGg-DzXwulogY7ltwRYOApqiqecV4vQQfOkLU5TRhgWNJ0rgZFqYDjoXEJ-Nj358ieZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
یه لیست دیگه از بهترین و خفن ترین نرم افزار های هوش مصنوعی برای‌کارودرامد و تولید محتوا. سعی میکنیم که در کنار اخبار فوتبال چیزهای بدرد بخورم معرفی کنیم‌. با همون گوشی دستتون راحت میشه بهترین درآمد داشت فقط کافیه اراده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28117" target="_blank">📅 13:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28116">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNoDOz0W6PPMYVAQ8SajoH7YtmXLmExZvNHEvCcjiB-4GqvTw4rMzm7CtMyQN7GuyvJwXyZGjuTus4ksOku9PrzxXkk_jnduHWO29eL8_8pr-wObETyaBTVqrXSRQLFWoPu_kI0ZtsbiAoDd8OrHCRdUhMjeCV4a3kFx2ww53i4GXTW0mG7FvBwpdfNYt_TblqgkTL_U2nQbbyVNcaULwenjs9JA_Ck8EB3X5pqgxwfgFxb3vERoSkSnxpVm6UGpQWj9bnSifsKJ4GvE_Ss22SRFawgYaUYHPKDbjMRvFGvEnyfbhvwzss7ZCFrD4ZjAlO7gsY6KebHr62YC0vwOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جورجینا همسرکریستیانو رونالدو این رو استوری کرده و نوشته تغذیه مورد علاقه‌ من برای صبحونه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28116" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28115">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g01WZOgJ1rIAwgAlNgkfOGvJxqXgfygZG-_k74IYrhFd8UHiVoAox5QC8ScGU9SxOpDsR10wukpffpsZGKiiaOO_xZ4ayXv072AcQ02r_70SpMTQXac2GzhPvDm7o_brR523K5NHCOi-iTLMBzEUUvu4QTgilglYn-0M5Etyyy6d5E1lN3DoaucvmzeJ7jiE6p-Yb1CpnurnoL4b8VlnvCcNjdg9nzYHvQjnk4Zwccb079FcTkdASD0EJA5ksJcmpq7DXMeb-WtcvRoMsPd1aCGeUyyiJHojtC4drNlFxYarAtv-Syhwg-U2nBN6OAx8brayxib0Xahrl29fc8v0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
رونمایی از کیت سوم خوشکل بایرن مونیخ برای فصل جدید در تمامی رقابت‌های بوندسلیگا و UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28115" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28113">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyBqobLlAlIdWqYbEmDQZVYdw8Mf8as8MJ0sYLGKetfLaUuz-g1MLXjsGPBAF90WtFTb9CEN4J_LP3cvlXk251IuRZWEOMz7bcbSe5igDUExOhEbySL66M7kpXkn5y2Sv5A1d21SkKIqtC_LiZn_6DNy4rq_12BpUtnwdtodQIIha09ul_PP54ToMBIWQZwbCUNC3jJ-6-s1i_-ARxho7rq3Y9W4MVkzEYbzAHwUR7gUkvmC91HPfpl-ffcySLt_NC4GxWuUJOO0FHnfiWE0H57n4SbKEZ7hTiPh7A9Thk2nyy658hgDzIpvOHPY1-sSq-NRVQR5oNNTfbaKOsBuKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی:
پدر رونالدینیو وقتی‌پسرش تازه داشت بزرگ میشد و دوسالش شده بود،تو برزیل با یه باند خلافکاری‌درگیرمیشه اوناهم با یه اتوبوس از روی پدرش رد میشن طوری که جنازش به زمین بچسبه. با تموم این‌مصیبت‌ها رونالدینیو به یکی از بهترین تاریخ فوتبال تبدیل شد و لقب‌شاعرفوتبال‌رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28113" target="_blank">📅 12:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28112">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKrkyr1dFKg70Wgwy3bx28JH0gD2r33CtFi5yKCc_ZmP0_i2arA7WtLNA648xZFidMVTHl_xM0FvDHU5tJgJkvuojuqQzm84vfdlZA0l0L8PxzgmTa_OQBkKOONElFzVzoB358O34pfwzrzNmNq0cVRRlOxxAmEt_08JS7j08rj6_DR0rpBUuGcy1yVUNYWE-Pv-ONKg7j1tHZtZmPMP7EZcR2uGJdsTIc801ou8Vlvhdc9P820Rc6cxo2CmtNm2OZbQVaHLlEpCsWjNeNswsTQhzb-GYaGa_VAb6evFJJnU8-rgvBNmxEKE6QT25iq-WDp2zZBEIxXXkPjkHfmGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیداسماعیلی بازیکن‌فصل‌گذشته فجر سپاسی شیراز باامضای‌قراردادی رسمی به ذوب آهن پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28112" target="_blank">📅 11:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28111">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En-UQpOD9x9od4J7EzkRo-zKp9I_EPl5hWrIuqgeR2wH4C_WlF5E385w8PvP1pRCkvTNCbONStE-vBhdwBV5s-Lf18vK_JjI8TAjb7kFdp-As7j2F5P9w6UyBDdFYN4jL0N2dG5S7N3LrGm2l8nT2uo8DidZaajdmt5rQnHIcs0pEUFvsycKneLr0hOPdUO3ytc2MQrs4u79bGvfci2JcNtzYwp9Q7t7lBHsDIUjrt5kJ3VdIlCyDx38UDJtykRhl3t4LYm_u6PxHQTa3FfBlDVwM2SCIrZoMT_RMSuX1D5G3Ea4fN9GfTw4zpMFyBtftdH1m6LYrgzPb6jOjTeQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
نشریه‌موندو: مونیر الحدادی در آستانه فسخ قرارداد بااستقلال تهران و بازگشت به فوتبال اسپانیا است. مقصد مونیر احتمالا تیم آلباسته خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28111" target="_blank">📅 11:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28110">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNIu-TiHZFPbVymscTAfw39AsAXE3lxXhpA0a_8DHzl7HzFGjRUpJWmr_GCRg8Z0sABpSF_ycWXpXHo-KeNNsSl9QSfE1aT0jcyR8kXA_-PfqAI_y-4k9i224J6G8yP3LSkaScMp0asMIf5oRkLam4sH1JCm6_1wUz0PD8jpZE1V6h3Ito9IJ4qSyfRO3kPZenXYjKDRag77pKu7BQbelHDEpMSvo8o3_TxpjCkoLaIEQJNb1ne_fNb84fXtE_-dls44onGrsP_siMgepSq_OIXvvZCzhf44QSa24u9-K99UzZfxzZM4zr5Cx-7J198tsqUzAwbQd-S4swtPhIzoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28110" target="_blank">📅 10:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🥅
کارشناسی‌داوری‌دیداراستقلال - نساجی، سپاهان - تراکتور و دیداردوتیم‌پرسپولیس - استقلال خوزستان توسط مارک کلاتنبرگ داور سابق لیگ جزیزه.
‼️
طبق گفته مارک کلاتنبرگ: گل تیم فوتبال استقلال خوزستان به خاطر اینکه مهاجم در آفساید بود و مانع رسیدن مدافع پرسپولیس به توپ میشه آفسایده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28109" target="_blank">📅 10:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f4df3199.mp4?token=tnWjlUn4SSiOilt2vbskDmBDT6s68QoV-9GgXxLXlEFqfdYR6xHTN4Dz8sVEvN7xKxufHTu4knlHeiQy1EHz8b7QLLYO_oj9FgO6L1Q2V6oHLBKr9gn1G_WIp_ziEIqBeaxOhdZic8dgV3OCyrs86FWVKQHtU527LAC0aAgCmGA9u226Lpj5ZOv90dXAZP11vXvF7zNqrd9c34wllC1F9jzYTzrFPErdlIgtlnciX3eXIr5mgRL1lV24QMJiaxLvGRts-TKOdWIkFFPF4U867NQsjalc1tNkK_BSfHtF-eJ1396J3dnjqf_Xs3-BYT76V6kk7W0IKIN-7iFHMT9_sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f4df3199.mp4?token=tnWjlUn4SSiOilt2vbskDmBDT6s68QoV-9GgXxLXlEFqfdYR6xHTN4Dz8sVEvN7xKxufHTu4knlHeiQy1EHz8b7QLLYO_oj9FgO6L1Q2V6oHLBKr9gn1G_WIp_ziEIqBeaxOhdZic8dgV3OCyrs86FWVKQHtU527LAC0aAgCmGA9u226Lpj5ZOv90dXAZP11vXvF7zNqrd9c34wllC1F9jzYTzrFPErdlIgtlnciX3eXIr5mgRL1lV24QMJiaxLvGRts-TKOdWIkFFPF4U867NQsjalc1tNkK_BSfHtF-eJ1396J3dnjqf_Xs3-BYT76V6kk7W0IKIN-7iFHMT9_sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
تاکتیک تارتتا دربازی شب‌گذشته پرسپولیس روی گل‌سوم و چهارم سرخ‌ها به استقلال خوزستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28108" target="_blank">📅 10:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e9ad128d.mp4?token=X4ZN9hClVw1x_IZ1OcqISy4wWllipgV93-enGz_zjXmLK5QNYwlMyVRRqZ_M-DJQ8LV150w7_RURL-K7-_KrsQIg1jRuTJLIMPNs36LeebAive0ZllyE8ZFFO3C6-TVR_l0tIQGoQFTRfVGmtQ7uoKVcyY77J47UES_sI3_6XtYjcYxiyYj-Rl-PeN9JKQhXo91DwQDyDpVgr2HCdSqAHJFgpr13QMlE0BbpC1Huqwkqs4AAy24KksQK6e1qgQSGqJrvOk67CCnvsUDLzUA968PV1OQyqR1bKFJQ_ZG-KMKkTgTeSmXDj7K5zB-VPtfwpVMOMYlp-Hrh1cQVSuSDgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e9ad128d.mp4?token=X4ZN9hClVw1x_IZ1OcqISy4wWllipgV93-enGz_zjXmLK5QNYwlMyVRRqZ_M-DJQ8LV150w7_RURL-K7-_KrsQIg1jRuTJLIMPNs36LeebAive0ZllyE8ZFFO3C6-TVR_l0tIQGoQFTRfVGmtQ7uoKVcyY77J47UES_sI3_6XtYjcYxiyYj-Rl-PeN9JKQhXo91DwQDyDpVgr2HCdSqAHJFgpr13QMlE0BbpC1Huqwkqs4AAy24KksQK6e1qgQSGqJrvOk67CCnvsUDLzUA968PV1OQyqR1bKFJQ_ZG-KMKkTgTeSmXDj7K5zB-VPtfwpVMOMYlp-Hrh1cQVSuSDgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال جام‌ خوان‌ گامپر؛ قهرمانی آبی اناری‌ها مقابل الاهلی مصر بادرخشش‌ستاره‌های تازه وارد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28107" target="_blank">📅 09:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d55041935.mp4?token=SFsDBtOY_PxTuklIAJad6wF1moFxqLxLw9XI-XUiU5GXgr4z8wvkveXwRo2WZRJlX6GAGDN6oH5oev0iyx3fjAc1DY3FWDJsQQMbIKw2hqFgBN8_k4Qn8pl998hYgYbkOyCLGCjfPQLXmRD6Axgt8ckPGqSSmwIdRSR0aAY8VwGzq9EtjY8YmNxQFlLAUpEgUbiVhL95E3YJu0jKmJfwn3RUN9Vwjo4pc7nQ80bv_qMJ2PP0vo2fMGIsO1glc6PkOHy7fvaJWOTmMqNbtbue9pYHBcKcICj2N2gZDBHLUph9-XTRmgDtuF5fq0xQkuIIsUAByT8nRYGwBZ4c21-icbZ-AkRYR9FPi5dLnucySt8CZo6qqBp8MtOC34w3RArsIsxpKc-sIt_VnuW6zerB9rHF8dj3qY9Q3PqV-kzR0lH5EN2bN3CUi_IthEJ07mxmFGMKjlDN5cQUW8dBmJGbm4g70l1HoOxDgosgbrxVGxNo1TUxFqVtszD3lO2_txqXOidPNDC4oawRU5MEsnHbnylOiHe247yJMG_Do-wjLgFla46HYR88HNZR1JPpLMxoD-bwF7sr-fnkq8ZBo4RLd1D29_sSm1Mi8wbSbaE539C3S3PlUB018FhCzfZPPWKlyLd_nqVFIAG7ilxia8UyUV69Pbsv5KfW74rVx6thAMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d55041935.mp4?token=SFsDBtOY_PxTuklIAJad6wF1moFxqLxLw9XI-XUiU5GXgr4z8wvkveXwRo2WZRJlX6GAGDN6oH5oev0iyx3fjAc1DY3FWDJsQQMbIKw2hqFgBN8_k4Qn8pl998hYgYbkOyCLGCjfPQLXmRD6Axgt8ckPGqSSmwIdRSR0aAY8VwGzq9EtjY8YmNxQFlLAUpEgUbiVhL95E3YJu0jKmJfwn3RUN9Vwjo4pc7nQ80bv_qMJ2PP0vo2fMGIsO1glc6PkOHy7fvaJWOTmMqNbtbue9pYHBcKcICj2N2gZDBHLUph9-XTRmgDtuF5fq0xQkuIIsUAByT8nRYGwBZ4c21-icbZ-AkRYR9FPi5dLnucySt8CZo6qqBp8MtOC34w3RArsIsxpKc-sIt_VnuW6zerB9rHF8dj3qY9Q3PqV-kzR0lH5EN2bN3CUi_IthEJ07mxmFGMKjlDN5cQUW8dBmJGbm4g70l1HoOxDgosgbrxVGxNo1TUxFqVtszD3lO2_txqXOidPNDC4oawRU5MEsnHbnylOiHe247yJMG_Do-wjLgFla46HYR88HNZR1JPpLMxoD-bwF7sr-fnkq8ZBo4RLd1D29_sSm1Mi8wbSbaE539C3S3PlUB018FhCzfZPPWKlyLd_nqVFIAG7ilxia8UyUV69Pbsv5KfW74rVx6thAMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
#تکمیلی؛ لیونل مسی در بازی بامداد امروز اینترمیامی برای سومین بار دراین مدت کوتاه پنالتی خراب کرد. سطح‌گلر اینترمیامی روهم ببینید عالیه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28106" target="_blank">📅 09:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53707ca2c.mp4?token=gKlslt2PZJv4vgS3ySBcLJwoiTDGSWjoIFTrSn1spnlkjskXREf5o-KosqmNW1Zu2-gcWPl2e7NFdnWUWGsxN5QE0s02f7rUjW3MBIOZTbUD1Xck_TcpjmRiLvie532g5v_TPIsTYKELKC6_j-b1AskMnnyktlizyiPGPGowHMZ4tSkLzc-JYw_Utr2OhSO_lFTGjFwsfrSLg-bq-y5-5amWGU_1oiYnTi_Sbol_jjc9CSFIyqvnSDChNSB_N0ILeQRo0_B2EcuLdKEiVpbCHnvYmyU1OTHSNCJpy7g4jkrwWLoSXp14vFowDHRF3Qpm7ZBwn3ETJaoPYl7XdaeV5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53707ca2c.mp4?token=gKlslt2PZJv4vgS3ySBcLJwoiTDGSWjoIFTrSn1spnlkjskXREf5o-KosqmNW1Zu2-gcWPl2e7NFdnWUWGsxN5QE0s02f7rUjW3MBIOZTbUD1Xck_TcpjmRiLvie532g5v_TPIsTYKELKC6_j-b1AskMnnyktlizyiPGPGowHMZ4tSkLzc-JYw_Utr2OhSO_lFTGjFwsfrSLg-bq-y5-5amWGU_1oiYnTi_Sbol_jjc9CSFIyqvnSDChNSB_N0ILeQRo0_B2EcuLdKEiVpbCHnvYmyU1OTHSNCJpy7g4jkrwWLoSXp14vFowDHRF3Qpm7ZBwn3ETJaoPYl7XdaeV5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نون‌بیارکباب‌وسط‌برنامه؛ اونجایی که السا فیروز آذر گفت میای کار داشت به جای باریک میکشید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/28105" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28104">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFRkgDQmKcK1uQLhXlk-1vapzeqzfikKQrPPOfMOcyAXDTQpPaRGaMV9hlQ-YZG3dmOJXQNoE4b8YunWQEkTbHwMwM2Z6KeODV_Ax8gOvXFzY3vgNAa02LTo_jAsAiVsbDpxRaZLP1sxQJFK4fUxmjppzrBaKo9O-GNIjDpwf3evX3-NVWJhuqM3pGaZ_ha3ZHLTu5yFuYtQEd2DsK8snBWJcEUlP7ik1fYnUEzc0TLOv-sR7xmlu-2kfO5vL62YVpBxkOc4gWG11LXraOxglVOsmL4oEli5ToBJgqngBSmI61PWCbOPa5T6SrO1dVPhyMA0CDHu1Gl5bPoM0IVwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار دیدار پرسپولیس
🆚
اس. خوزستان از نگاه ورزش سه؛ آمار متریکا آخر شب میاد اونم میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28104" target="_blank">📅 09:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28103">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFm4NXqufrQZrQ-mpSKvKwbVczex3L6esY-hLa9Ruj6Re2o0opbLsQVk66ILYbDi3uQMRcOvnRt-DMqy_jbBc7fR-vo6IBonForJ3hrndRZKXBAkpe-ZMwEyJGeiQS3POVJKcayFssWjYMTCLI9GJheNFsRSocYga88OwbraDWZqZ5ovazYhKEkajyAyqoqWVoH6I8K6kwMUs4u2w3lG_Ni3fX4ocIrOlIdh7_DudRK0CYBQGlxQ6LfgIpQmQ15wJjpavg43wG-yj4b-yliGfTn0VKKSpDiOU6X_X5lJ_dBw8ud7mBE-mTlozxNDIokczu1vHwYKvJ2UD_KyfRhqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی هاشم نژاد دیگر ستاره پرشورها نیز به دلیل مصدومیت دیدار با سپاهان در هفته دوم و دیدار با پرسپولیس در هفته‌سوم رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/28103" target="_blank">📅 01:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca4590fc2.mp4?token=Lza2ZS511SZ_mJDGxU9cjTCmsD8SXRH4g7mwblI9DlM1sBAIKRWF8rO4kNGU2VSf_Zei1jaWYNEiLXEIt6v5aEs6TtNkFG99xXsoIxkSKue-42RW-O_Ba7uk6cWzaoH6bABoJfJYeMLnEjNS3x8aNbcrC04e_6XOo_prAAdLG1jcshNEYFLtvxdy1k0W3ukfkCZEVstF9dN6qLVj0vvOz1axkluxMFRg7QbdWHAuF3z6nOo4veNacJ6RS2h9kK3_gBIX2LcWcT86TclVLRmm05WmhRMmK0NdCkkslwAUdaIHTP4RA5vdvEaXEc_MyNIokF9Dddt5yPoRP48fHq2kJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca4590fc2.mp4?token=Lza2ZS511SZ_mJDGxU9cjTCmsD8SXRH4g7mwblI9DlM1sBAIKRWF8rO4kNGU2VSf_Zei1jaWYNEiLXEIt6v5aEs6TtNkFG99xXsoIxkSKue-42RW-O_Ba7uk6cWzaoH6bABoJfJYeMLnEjNS3x8aNbcrC04e_6XOo_prAAdLG1jcshNEYFLtvxdy1k0W3ukfkCZEVstF9dN6qLVj0vvOz1axkluxMFRg7QbdWHAuF3z6nOo4veNacJ6RS2h9kK3_gBIX2LcWcT86TclVLRmm05WmhRMmK0NdCkkslwAUdaIHTP4RA5vdvEaXEc_MyNIokF9Dddt5yPoRP48fHq2kJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری از لحظه به ثمر رسیدن گل تیم استقلال خوزستان که نشون میده توپ کامل از خط دروازه عبور کرده و گل بدرستی به ثمر رسیده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/28102" target="_blank">📅 01:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28101">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omaYHoIVJxtuGsOWpEKb3zje7icaGAFkqMo6XOO6JIVMDT1ll5AqVUpHpRS873qYnJhD-Atu1ENkBohUYEwnfVI0Kq2ZnhOb8MVOh7ubBPPOV47lvMpXyhNP0mKwwiPE4k_xOGNHSamqk8XTrjSyTXOF09Vkt8EW1zAV9m4FLeP6UX2X3S9sHziXq0T5GrdAydO6cvtv8d6UgiSMUNF9zIa7oDQJBY37l4aljFx5yQmen0cAJcXMZIKFLyPWn1hFC1PD1_7BmH6BzutWOB56N5sZsbCsSWxgy83b_UTibJVDNOzfsfDiTCteh0fYhcOfXV4koUgnutUb-ZVsKCa-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف اینترمیامی با تیم قعرجدولی تا بازی‌ اللهیار در دور نهایی پلی‌اف اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/28101" target="_blank">📅 01:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28100">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxDK8EPMkSqpZ1nUuo0F7lJf8sOAHi9iAGWgNXEyiWX5mZie-n4jgOghlBdgFOC475QjYKGqfKYk8iDz3rqaVSMDfyXl1M7ZpwCxI9h3hhU8ei9h6sIiEtIAmuDOpQ1aCcyiO5ghTW0HTPq5_LGdzeTY9qBKayfSjDKvm98PzINmK1FoRX6C2wPxH4q3KUMlwtleWhVkfgKGwpnojd3STGVnC883TqHE75YtXALI5A0gHevfkBOFq047_G8gM3RphvwUaiM8W6LQ3fi5NF4N_CM-MOirqBmuihGZoCU8xYzhW7EIPqX0vYymsrKbPyM_Q7jdHyGA5CtR61woUAILbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
برتری چهارگله سرخ ها با درخشش علیپور و قهرمانی بارسا درجام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28100" target="_blank">📅 01:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28098">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebAGgHE1aA5VI3gQiAHkzrSSPdyJ4BQSV1ZrnO80se7vIaH7j1B6pw8W-NyM40ExUNsHJbJ3nDZQwCVDx7ePn7dfKAc7DbOwBesVJvVxLugbUeN7OPw5DJZ3VoxFsciJCWOwGUm0jJt5EHx30sRPJajRBw81_jV5ENYecx34CfChNPqMV_89I8gFrhBtr5T2RLvR9gJ4tdw6hUvHyV9VB2cuyqcdlo5x3N2J28axSch5oHARjsY1MAYU7mW6N5iv7qe_h5ovqXRwdxDo1u048JwJh7J_XLW3cLn8KzaiC_PXevyrJPhJ7PhElD1T_ezYqtBbp9DZDX6YwwwO9kBOHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/28098" target="_blank">📅 01:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28097">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c23a6de2.mp4?token=jDkEUtOKpZSeOGT_ncDfEIo3cIBIVVMvTRNawL94L0O7QQpEdEE3Qa7GMc1YcPAp-rtXgNRa1Ed8KoR9M7R9ji_iKtlix_K3zOlKkxbVuRfDdb_ZsrFmrQhzjyk20NRw4gJuexcFDan4_HR4VWikNiru4k2gFgNGXZuoNPYh431bEH7L7qDh8hYKWAcrQkYAGsRBqfABSJqY4KET3AprTaLmMFN6DXCJVnlkWEavqqxYqIKjX_Oa4SYLElwhUYGNymr9GAB0QS2GNNZC04VQltJlEdxx-FdB5YfMmDWQUrvzWtmUtcpRrNe6Z-JGxkazKWYWzsR5edJfd2EWVk_pLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c23a6de2.mp4?token=jDkEUtOKpZSeOGT_ncDfEIo3cIBIVVMvTRNawL94L0O7QQpEdEE3Qa7GMc1YcPAp-rtXgNRa1Ed8KoR9M7R9ji_iKtlix_K3zOlKkxbVuRfDdb_ZsrFmrQhzjyk20NRw4gJuexcFDan4_HR4VWikNiru4k2gFgNGXZuoNPYh431bEH7L7qDh8hYKWAcrQkYAGsRBqfABSJqY4KET3AprTaLmMFN6DXCJVnlkWEavqqxYqIKjX_Oa4SYLElwhUYGNymr9GAB0QS2GNNZC04VQltJlEdxx-FdB5YfMmDWQUrvzWtmUtcpRrNe6Z-JGxkazKWYWzsR5edJfd2EWVk_pLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی همین دو هفته پیش یک میلیون دلار پاداش از فدراسیون گرفته. جدیدا هم رفته یه رستوران که غذاهاش‌روتبلیغ‌کنه‌که یه مبلغ هنگفت هم گرفته. بعدشم میگه‌خدا با من ناسازگاری داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/28097" target="_blank">📅 00:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28096">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKOMnRyF2ywBIPA-zNn41ZyvJpUHB4bKT7ioOa1NbWSqTvZIMBbYoQBha6m6YLB1217c-WqEYqIUt-9vDWNdF96YYP-b0T5IeihZxale5iLxOfs9KVsqscjBLko37DHTHYgH9MrfJxOlzs0r5J6Yae6JRIUVNYWt_01eOx_9JH1QBCFrN92KvzWhMv-Q1vk4luJVQxLsd3Ri12hXezloeb1yf02AMzYJhJrNq_M8zeN4E9gIELQk1ZDJMrH-Y0ddCUQForzwIwFuB-6KUjNcMPwcj9A5M-NJ_W46xKYsnvRXSbbF9uTPz-RR6hb_gi2GMojpZStvT8fo3ZmrUgsWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه الوحده بعدازچندروز امروز رسما تخفیفی 200 هزار دلاری به باشگاه‌پرسپولیس‌داده و بمدیربرنامه‌های قربانی اعلام کرده درصورتیکه باشگاه ایرانی یک میلیون دلار به ما پرداخت کنه رضایت نامه قربانی رو صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/28096" target="_blank">📅 00:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28095">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8JPtlAMzhJq5rNrOjAOOhYt5s485a41_34u0gqjPQjLLhtOv1g4nmB12_Lz0d0joj_PLLtP5wd3aIG9sqq1Bj4aEnqfcKdRdbfdPLMBR2LSUhIgt9fpJK-ZcRokMHtjQR5AYZ140yueZakw-GbP0FF8VXztf-AGvhLuJlZrbuXMI4Q-LOprac1nIMgOQyjJjamlIL8oY-n_xxyze05olj-vCqX9DiG2-BFlPWF1DLKJCI2hIkEzXXeMQoVBIGn1EZw7ND05nkSQB17xAvtkJ2p0_wF23lnr9YEfudDeLS9-UZRJfI5bPOvrTGNUPJ9zkk3-vwvtgeO1jhDdKCSjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛به‌احتمال‌فراوانAFC ورزشگاه السد رو میزبان مسابقات آسیایی استقلال انتخاب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/28095" target="_blank">📅 23:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKhE2hIotK6XL-aQUdQQJSw2_3cPXI3I5Suy6MiK1cWenrstgX-zACSYbb1H6izqia-5jUdasrU3CB-Sj8lQSZ-sGz2bSyFDrUetEPwMlFJ5WLWR_em_fayjffv82OC4jJfQbbmLGaaDI3yVQl5QpCOxhvcNr3bznc-oQgrBGAG_azTFGCCRM0fKY8N8-AiKIlnP55m1ZEnyGNfS2n2Avx90HKJbGspXrUe42uJDRWIQlwfBgJITCRS6pHjiRbnvLDxrMjZqd6otVC1a94xhesIVQ68fNVzLmZp-JIU9Qk04kW_CxjeX7KlS8nWmUhrnqE7DB21uDvKt7_iOTOTWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛جدال‌پرسپولیس با آبی‌های خوزستان و مصاف‌بارسا و الاهلی در جام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/28094" target="_blank">📅 23:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2IfIsoBfaerjS9FJjsL2H-MaEsgL5G-8FNSbqsuSaHba6iQfJ75DVssVi1_6xcyVTkWLF9zx4Uatv0HQvEzlVnbycwPq6N4B5eKE4zbOkQGCv16Wwc4amRmTfN8QitzBHDSZd2LVbr4LxwlURix7bgdqfKJ_vxZ6-E43sOxg0-UmqVTXjSm7qK12Ve9gZFF9GNRz0575TgkUiG5h1BIRjmCNJ-m5Bpy-7XAknWTNDRvM6XBIU9SGIhIPzwbPO-dP4jsUSieMeyumICf01VYE3eXU1LmAry89oHiCfClqMMUDzoqHm4yYh8Rb8Tm9cl6RtAh6rBHz9KDVwnkg26ctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نتایج محرم نوید کیا سرمربی سپاهان مقابل تیم های بررگ فوتبال ایران: 6 مسابقه، 6 شکست تلخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/28093" target="_blank">📅 23:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8K5YORQgJqOkgOROFG46lXMTFmwmiR2OTlEzsSBAMmlVuyP0V3RXk-nfyLNXS2kRGs93IChVabH6Dg7UGzeNMuH6Bvz2--vmA0f3C_f1CJwuNxYoCuWuTVpAmMlFOQ59tEDuBGK5EE6h_PDMW2RymvESIHpq7uKzNt-pePFfi851nZnmXC4DKFLnlgBVCv99z-2mKajgpkFAPF4_1DONLWceUUZobDLWGLCXl1BwpheUFX0MAfhkCMzRHukzMPJ9onTIVzKicGyDjJmW8p3pRVVDkonLMScdaTpW20CRMX_oiKPqCNtjTBRlmWC-775BzjV4YW18hai0ikafntcQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رسمی؛ دیدار دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ برتر روز چهارشنبه یازدهم شهریور ماه ساعت 19:30 در ورزشگاه نقش‌جهان اصفهان به میزبانی آبی پوشان پایتخت برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/28092" target="_blank">📅 23:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flR76DyrYmliaSE6g6hSRKrhSN-yTB3QV8FmhCAsiPfOFaxEAtPYZAuaeEUvzH0EU7JFOgLLcYVQgQvuOEEN9nVaQk42BoaAcF1kCtjbk4G6NMJfnAVH-TOi0sZPFF4Bb13vrshyYvCN0VISPyQmWjsHfxzlZxWAEk0JMNq0QetzekLlmQRE1Xjy-ifIFbM_B8LPQHcjI_jhix1kqfDVQmV3rkT2XHRVUzuM9sL6nTsOO_MVjjQOsSOqHHwp9DdLvZXenj6-V71Ycs3UgCfEV2L98GVqSBNmHnsZpgqHpXztCExRYKgA2NfBaosX8L00vUjwoeVKI4vd6TwQsDgiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌وجدول‌رده‌بندی‌ لیگ‌برتر در پایان هفته دوم؛ هفته سوم تیم‌ها محک جدی میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28091" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28089">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPeHVZffnC4Y7rAxWAOboOeTXpc3BSOAszPbZGEedwUjU5DTISOdxs9yuA4iEAmk8O3v_LMixezn1NvFpw7VyVac6bBziJt8qemRlKA78vbzXqXI5R3jfkdbcZNxyuNTDe3ykRCP84EkNeMBywsCZyRfoRHinYgM9fv9APlnIsGrAVqEzoZYCyTn1flDR1zsKWEE22lPnOCUB_431JyGcEkD5k1r-o1JwYsJvRhlguY1FsjsExdE3K25GgTQDvCXuO_yeA3ifibXGz2cllwKlt0PFwFekAXtkaMNIFjLgpp9HZ1xk3YxAi2bh9ew9w33Z1dyhCrMHlTPlkLNpxzmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4AsyEaXZ6Z1rjPU3TTck9N32d9uXf_F83oH23JEVE9WoggXuuJT0UJ_AJapJku_oy08h98fbRcm1l65lDAnRQyxZQEdgOCkVBAZ2Atjfga21vQeGjSmraObPRAEos-USHJDN3zLh5QA0W14TPz387KsSyWg4pt4lPv1qsz_vZhThUrX6vQJe4wCPSmQ2wZQiAPUTXdK711h7p9qq9c-F6xhauqeyqIxkIaJOohmVJrZhTph7LfM2Ep345ypZOgEdiXI8GFuEl5gksZ_xbxdsLA-iSLpkeTMc5vuT23W7kBBiNLyhvNJmu7JS4oj36VORtWqOvdwxMPnl5gkEhY5wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28089" target="_blank">📅 22:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28088">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onQcTiD3coIoOv60_5JMeqFKkfDZfpAdXZsko627O5u5C9RG29BhkI5BnqkiHiLy6nMd4VdPa-Pqfd9Az2v7JPRaP2kbGMrBEfRMx5bag4A_eAc3ua8Opm7DZ8NRKYJb2VfHobJ4UiWUCa6j098S-wDWmXJSWYUZslXkq8tqTSL0L0P1UstgdFb-gjEOV7_PRKx-uEV1ir6B_Ho6kR4-JepT5vp1GXFWYHrs0uuKq00L4JvsqjxlMBy42FoQLYWa6VkbuX2WZ4EAcNJwHDiqkYZFf8dwlO8bFzCg92Gb64CbKqXYg_OVE242mwTLNRh-EmHXAUMYTjWOZnlKY60pWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آرسنال با پرداخت 45 میلیون یورو عرزی کونسا مدافع میانی28ساله‌آستون‌ویلا رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/28088" target="_blank">📅 22:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28085">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524ee90d80.mp4?token=OE4svvaaeCWDbbvagJgncLQB7bArY9sr4GryDWTXB5ns_QeEb40qp0N_mwWRItvXDS2rP92voLlQsVF-qZTB6MeYt2BBxxXQpIP0MOXsDRr3QzIOrdttllYTQrTx_qAZI_IsMyRN503MxHYAC4zqnWLzxSGyLtUFXlw_EKz-B8RfSnbACQYn0mZe0ChdHw37vYFjUIUiGZQxT_bEKhRISYa9Z5tMrY2r3x-9-jqKSUrjiJWlIFSFwCqU7Subxsws9BCWaKCREYP__mvVh_HxkbjCsSe7ewFxjc9Zzn8ElDNox439boxAirB1DbQpIAcMaWNr2yibbr7-RKB1ex0Fo7iy6_id_xolxI0MXsi72lTk5_XCZor3RIyOx_wSMIaPfJxEadRi2_puTvRk3lsKHmAQpas36qB8LyMmMJntcroCJSy07Z-XuOY9aN700jh5yUEJmY2dp-1hDfxxXu8vvJF8OPuOsI2cAxrNp8wyly8fkXloel8RRT8BnLkdVcS2lqpSh4fFynBsArd9r3gAOfJKqkw4ubVTfI5za8xl84JTmXe9qWyLp4Ho6DAH-3TmY2LSGA6xt1hPt9YTcxk-Sr7yjoMBaX1qYsq5SZ7NEk_iJZ1oN74CIBguacloXFeZ9zTpWR6Yx8sDNLlYljeitORdXtVtwA1H1fZicftIrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524ee90d80.mp4?token=OE4svvaaeCWDbbvagJgncLQB7bArY9sr4GryDWTXB5ns_QeEb40qp0N_mwWRItvXDS2rP92voLlQsVF-qZTB6MeYt2BBxxXQpIP0MOXsDRr3QzIOrdttllYTQrTx_qAZI_IsMyRN503MxHYAC4zqnWLzxSGyLtUFXlw_EKz-B8RfSnbACQYn0mZe0ChdHw37vYFjUIUiGZQxT_bEKhRISYa9Z5tMrY2r3x-9-jqKSUrjiJWlIFSFwCqU7Subxsws9BCWaKCREYP__mvVh_HxkbjCsSe7ewFxjc9Zzn8ElDNox439boxAirB1DbQpIAcMaWNr2yibbr7-RKB1ex0Fo7iy6_id_xolxI0MXsi72lTk5_XCZor3RIyOx_wSMIaPfJxEadRi2_puTvRk3lsKHmAQpas36qB8LyMmMJntcroCJSy07Z-XuOY9aN700jh5yUEJmY2dp-1hDfxxXu8vvJF8OPuOsI2cAxrNp8wyly8fkXloel8RRT8BnLkdVcS2lqpSh4fFynBsArd9r3gAOfJKqkw4ubVTfI5za8xl84JTmXe9qWyLp4Ho6DAH-3TmY2LSGA6xt1hPt9YTcxk-Sr7yjoMBaX1qYsq5SZ7NEk_iJZ1oN74CIBguacloXFeZ9zTpWR6Yx8sDNLlYljeitORdXtVtwA1H1fZicftIrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🟢
گل‌ های دیدار دیدنی دیدار ملوان
🆚
ذوب آهن؛ ملوانِ زارع بازی یک‌هیچ‌باخته‌رو دو بر یک برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/28085" target="_blank">📅 22:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28084">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUtm7v3b7yogqeyvlRDGJXFkMO_aExHBH5GE1AccRu1e_OjHsmiwOxvK6Z1w_Q3wNMTdJI8cAK117Lc8CwDRkd1CLFHn-WEt19edONGZ0y5rrxFA5MUzZaIck-slS8B-2JJvjks1JdKZM8n0JnoPLBFcR9B-oL8Zjq8vSvfcuL96uj1Yd7O8Nie7TpLj0PXYNYzEK-PVibS4bP1pBgjQeOmeAudovSBPh-WvrigF3HvkERtX-0_3ikmdtiu7hgAQF6Ox8CqiCy8bw7YnUFhgBniemyLEYdeyvabeLVj38zT-M9VeKP6NbPvmLGWodqKKwL3Vb297woeKPQkpYxNHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امید نورافکن ستاره سپاهان بدلیل مصدومیت از ناحیه همسترینگ به احتمال فراوان دیدار هفته سوم مقابل استقلال در تهران رو از دست خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28084" target="_blank">📅 21:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28083">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzT-wVX8n27Z9ixd8Rg8Ibst4A8gdGFUXXRRd4zhUQEhl2HzMAM1Dj8ssEgzfTVb_FDnXQv26wUQr9Up24aPdFKHlXrFSUDOadfWUm-D8PViXnG9tgZSYsdzKfCDGOTuWdFlzVCIvLnbGSa49a5-WJAYkU-Tmtx0SIfAUHwh-dVZvFceJlLcTS03uzqmnnQC9meghOfSmeV1-NHFMVN4we-A3ZJwQlC8KK-nPIEgPn-ytBR4RXtOP6edCW7J_65dLwTUEsOT0SpO4eh9wNUq8VOCq7Ug9z6rgTH1lPeinbySMHDyAAfUMij5T8gpCojngQAAb9RuaxUerWqToRF13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
🇮🇷
#تکمیلی؛درخصوص محمد قربانی تا این لحظه باشگاه‌الوحده‌راضی‌نشده رقم رضایت نامه این بازیکن رو از 1.2میلیون‌یورو کمتر کنه و همین باعث شد تا سرخ‌پوشان پیگیر جذب دهقان شوند. اگه طی ساعات آینده اتفاق خاصی رخ بده پوشش میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/28083" target="_blank">📅 21:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28082">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6602afdddb.mp4?token=FqsCSb9avixQ6HpZlrhmPhkiBUhmFATgpFV_tc8oPs-UrY9PMHev2lQSCcuo3gQMft2b0zvidjKRanhtZP8AW28IE003Vxz8Q5OqcRCUO3C4ktCK28c7OFToCiToC3VdeQ1nc1Ymj_oXyMLZ6AAZQJtmpXkqR7-OPFXvYcv_FRghd6p_KjOgw0v-Zp7iVXgsFTxu9UDyryTwvvL1AfPkhnhECN1cLRruoPSqgvXOBPEkxU-6kT3FD9kX2juJCttygZDVp8k6p2AvtOiOpLBz94xEe6Atvp71Yr9fxp-cdumhDSpFmhG2ark5HI1x70Tcc0PWSiKGN1mZaflvNhFHyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6602afdddb.mp4?token=FqsCSb9avixQ6HpZlrhmPhkiBUhmFATgpFV_tc8oPs-UrY9PMHev2lQSCcuo3gQMft2b0zvidjKRanhtZP8AW28IE003Vxz8Q5OqcRCUO3C4ktCK28c7OFToCiToC3VdeQ1nc1Ymj_oXyMLZ6AAZQJtmpXkqR7-OPFXvYcv_FRghd6p_KjOgw0v-Zp7iVXgsFTxu9UDyryTwvvL1AfPkhnhECN1cLRruoPSqgvXOBPEkxU-6kT3FD9kX2juJCttygZDVp8k6p2AvtOiOpLBz94xEe6Atvp71Yr9fxp-cdumhDSpFmhG2ark5HI1x70Tcc0PWSiKGN1mZaflvNhFHyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛جدال‌پرسپولیس با آبی‌های خوزستان و مصاف‌بارسا و الاهلی در جام خوان گمپر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/28082" target="_blank">📅 21:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28081">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRWfznaHxpa-Lr8JpxR_MZ3LhUEnl8O-ZYLCkwI2k_1YeyhJY1FXQ_oxMZMKOhSk1pqD8biuYIpxNYnKjh7Pz1N5Xhhv2SBNvCGPjnDK8imfo8SeNZbpaMJh7piX6-f3ZLhJyTq3KhzU28WzKA2-iSNV0jYhWAiZLoYHA24tiCpEww4fx4koAHrV4MZUnR8Z-3l91Gh9VweWMmDORdzrWMAqSBFGJWC7fgXENuWYnEEqIsAm1ZxjCWKGFcF4KceftN1vKjnf3VTJfrzlbTfn2U_TuE-6Ve_1KRVOk4P3QSJA4rWLxenAEn1DY8lS169XJ9w8_vr5g_2lQKPH1Jvpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/28081" target="_blank">📅 21:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28080">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkUserrerGkeLlICW9QpOixehY2A7mBVqusa_LnOf1C_FcEuZo1muGn86sMxSXHHsQori_PQ1mvbFDmrxuyRuaQMs_yFSnC5WnHpXQuQ7kb14OzcRkbk_rrETTjbKNr0F9nPEuChwRnsXxxCMo7Roh-a7k_iRYB2nh0p46bryDzJXodKC1NMsTOOPA_Z3cMIvKVhsNbqGTHck2Qkamny6BrGkvYkuDbwZbu4GvVd-BHPKfdHG3BIP-qKeoPriJ1iyrw5JQWKXrvPo_QZFv0ACK13uQhxgRoYeFKbzzsv3yXNpuPptfHItCqFl920a-AirDVwlDcTw_kX4c30eeiGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌برتر؛ دومین پیروزی قاطعانه سرخ پوشان در فصل جدید با درخشش علی علیپور؛ تارتار باپیروزی خانگی به استقبال جواد نکونام رفت.
🔴
پرسپولیس
4️⃣
-
1️⃣
استقلال خوزستان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28080" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFyNBk_wKAxzS79W39IiahW6eaGdybvgEd__rEbI55Ctr5NumgIXPckpFpvi9426OxAQH9VYOSL7eg19iYnHi0PtF5q5x2ymYG0Ciw6guxo65R8Cb_FVho-zUJ3P57rnBJaODeoHl-VN-wI1y9u6xCDlXCuH6O5oH2_Ld29zXqmaMfLbi1fBQocIhYRPLEyUMY2eisXfxnyn9XddOMs1mieK02jkVIiehpt6OUm1lDrijQldq8ZnhrrViU5Hq3jfErpAucKtAHvgTNnH9FW3FCuoIKRGChN9eCaxInh6RehJdRF076QdgvtVTRBwwyTZyuSOwaByXDpFS-wdviUs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28079" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f0b34890.mp4?token=M8_P6KxX0n5NzbZeFgPKOvCYOiFdIlgkxEE3G82KjXs2AKWAEpDooS_jUpArQB3cSTmZbFOKyEzI_Z1zaLr3IVyeZq8ycoJ0-KpAYSpOplqDzgWlFBIRPCI0KaQVeQT-njeFB6lXpay9g95KqHSE6occfUHB-MpjIkCOfT0u9fLl-Vip8_GB6mHIBlHiqwVkhamlxp0CnRN2oHaBhRxC4k7vMPzmcOOSUuOMNaUFkxIbWh8AF9K8VyvH3Ko1bRmbPp4rzbN6AOKfNxehPvHVIvcSNwHRzMONrw1ND_exIwL7jri3lPxfNcnrAzJTIAcJiSDJ49itqexqqzW9Q_yDgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f0b34890.mp4?token=M8_P6KxX0n5NzbZeFgPKOvCYOiFdIlgkxEE3G82KjXs2AKWAEpDooS_jUpArQB3cSTmZbFOKyEzI_Z1zaLr3IVyeZq8ycoJ0-KpAYSpOplqDzgWlFBIRPCI0KaQVeQT-njeFB6lXpay9g95KqHSE6occfUHB-MpjIkCOfT0u9fLl-Vip8_GB6mHIBlHiqwVkhamlxp0CnRN2oHaBhRxC4k7vMPzmcOOSUuOMNaUFkxIbWh8AF9K8VyvH3Ko1bRmbPp4rzbN6AOKfNxehPvHVIvcSNwHRzMONrw1ND_exIwL7jri3lPxfNcnrAzJTIAcJiSDJ49itqexqqzW9Q_yDgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلین شیت نیازمند در دومین بازی خراب شد! گل اول اس. خوزستان به پرسپولیس در دقیقه 64 بازی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28078" target="_blank">📅 21:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28077">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peFtzZeJKA6xGcG272VolwHbAvndLUrstyCFILDyuVtW5XDAUHy1qxo9ncPsFq_dlAYX8wKvckzeC0mrH40XJ4MG38Xz3RiVoon1Suao5_q6VC47HJpHmkQAyZtfKrFxxuykjflahUCrmmp7wY6wmN95swQZp1-foXkKzSGoVi2-OnacmQmzuGTGiT2B-5A9KWU6w_htFBQrdDAw6WlpcLszwMwvXc5fTUm0wu9q6QCB9PYU4pqT8iXA_0ohChn_WBT-oKQudgTtfBVbzhAV0EtlmPuT-jOmV5LJOJrT6Tj0vWyuVsQTHO6nY53MV8n_dvgo6_gNZEplgZigO3ajhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌ازگل‌های تماشایی رودری هرناندز ستاره جدید بارسا در دوران حضورش در منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28077" target="_blank">📅 21:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28076">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb9a3fa5f.mp4?token=VV4i6YoFkCS2wzWBJct9Ki1oGalQ2xWEFt4Nuu7ZP6oW8x3WcuesffSINfw2eXXn_gd-JBwZKW1lHwZYEJ2VvT2H694O_bAoxsKqjbF3bZ4kY2ziWvvpm5KGRbOfgB7pQJ35nSo2bjs0DdUwcqWV_M0Ns3YxFbex2d7K-dEueDCwzmCHFJmv0ra726aEuP0TNcZLN06xpUFwUnjFXkPGPbBDCo0Wtnw_Fc-RTWB6-AszaSBMM6359EnuSkYOqWt7y01Pkvp2sVcil0ETz6v4mlfABM9zeLq1kf63XKEiDPqKfdqEbv3P_1iRjT2UxFVH8j1xgk7rJWHIdVMi6dxGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb9a3fa5f.mp4?token=VV4i6YoFkCS2wzWBJct9Ki1oGalQ2xWEFt4Nuu7ZP6oW8x3WcuesffSINfw2eXXn_gd-JBwZKW1lHwZYEJ2VvT2H694O_bAoxsKqjbF3bZ4kY2ziWvvpm5KGRbOfgB7pQJ35nSo2bjs0DdUwcqWV_M0Ns3YxFbex2d7K-dEueDCwzmCHFJmv0ra726aEuP0TNcZLN06xpUFwUnjFXkPGPbBDCo0Wtnw_Fc-RTWB6-AszaSBMM6359EnuSkYOqWt7y01Pkvp2sVcil0ETz6v4mlfABM9zeLq1kf63XKEiDPqKfdqEbv3P_1iRjT2UxFVH8j1xgk7rJWHIdVMi6dxGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل سوم پرسپولیس به استقلال خوزستان توسط ایگور سرگیف '48 روی پاس هوشمندانه علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28076" target="_blank">📅 21:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28075">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef87ad1f3.mp4?token=abJad2E3O9Fh9NloOGqQeufDr4N2bRQAu54ldHnXL5JXK5NBWPlcddhMd8_0WTXQ8m22fAFB4LWRsCwYMXcgIO1LhtEibgHWwbwLJiB4gc5jwGqIIY0DI_TX7_kP4e2B-a8dS7giCKPG8mb528bb1d1bfJZiv2wr23ncfk8GT6BdQi86U_IlPsTdaYcSt7dYWjiWZHQxQT_6fu3-OUa0TuJjkB2fh2P-5lZLy8EVgd9XLXI-jjUP57PB8XiHcR9_oppuSGiQxOtzc9hG4hkdm02mAanpNqzjZr3kIG_GJkqElnZR_UqvqwPEIaknjv6w_j3P6mDB5EpelKPdjfnalg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef87ad1f3.mp4?token=abJad2E3O9Fh9NloOGqQeufDr4N2bRQAu54ldHnXL5JXK5NBWPlcddhMd8_0WTXQ8m22fAFB4LWRsCwYMXcgIO1LhtEibgHWwbwLJiB4gc5jwGqIIY0DI_TX7_kP4e2B-a8dS7giCKPG8mb528bb1d1bfJZiv2wr23ncfk8GT6BdQi86U_IlPsTdaYcSt7dYWjiWZHQxQT_6fu3-OUa0TuJjkB2fh2P-5lZLy8EVgd9XLXI-jjUP57PB8XiHcR9_oppuSGiQxOtzc9hG4hkdm02mAanpNqzjZr3kIG_GJkqElnZR_UqvqwPEIaknjv6w_j3P6mDB5EpelKPdjfnalg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به اس. خوزستان توسط علی علیپور در دقیقه 20 روی پاس مجید عیدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28075" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28074">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f80a1480.mp4?token=Q2J7sTWGU3n6ooajpnFnzC5Z2Glz1jIaYurrRTrbyYW9F9zaX4F8OHT8l_XKdfkGcWgNYtUseNR0CR94bARmnMBUpVLG08yRP64gAXD-GoS2Ivc_6Aol8c2hDIqdXwZGyxHb9sjDLe8BzQej1oKmp5A5xP0fifjWliWYn_QYkJm-Jya6MgDHQozIL8f9dumCqb52KiphLVB9jJEIF4OdgFIz94A2CFjL8SfNnj6l4i39838xqxXwPqK6fUNTnQCKOTffYUAheFdy1Y6ZyRwADX3SKna2_WlWu2NMH4h5ktGsI0KemPtLHBFbAioCJe4HySF8Zk1R7VxiQJIF7_4nBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f80a1480.mp4?token=Q2J7sTWGU3n6ooajpnFnzC5Z2Glz1jIaYurrRTrbyYW9F9zaX4F8OHT8l_XKdfkGcWgNYtUseNR0CR94bARmnMBUpVLG08yRP64gAXD-GoS2Ivc_6Aol8c2hDIqdXwZGyxHb9sjDLe8BzQej1oKmp5A5xP0fifjWliWYn_QYkJm-Jya6MgDHQozIL8f9dumCqb52KiphLVB9jJEIF4OdgFIz94A2CFjL8SfNnj6l4i39838xqxXwPqK6fUNTnQCKOTffYUAheFdy1Y6ZyRwADX3SKna2_WlWu2NMH4h5ktGsI0KemPtLHBFbAioCJe4HySF8Zk1R7VxiQJIF7_4nBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز منتفی‌شدن حضور مرتضی پور علی گنجی در باشگاه الطلبه عراق؛ رسانه‌های عراقی خبر از آغاز مذاکرات این باشگاه با سیاوش یزدانی مدافع میانی سابق استقلال و سپاهان میدهند. یزدانی از طرفی هم‌پیشنهاد تمدید قرارداد از گل‌گهر دریافت کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28074" target="_blank">📅 20:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28073">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpx0l_JZMSKfIUj0MrrZsA8hRqd2Vqbnz9XHm1yGM_7m0PNqstQnmeO5zAClF3IQTZ-rv1DT4Jq_5Ln2boFC6nsy2nNUhzpgaDde1sQvFFFuzpuKUkCQ1KIy1WPpybH7Ob_nN2uL_lDXGF8FMgi1Qm7MK_zF-mJ0ezCeYcHLqMyR8YFL0D4tjnONqvyaCcPhw9cowx3KX6omHB6Mes4tanl_MJiw41lSaBm0bmwFmk2ccz9tzjKKfNF3w3PF6-0ieCin8Y2kjxBuGG_ZvYQHVtHm5FMAo7TXm8oIIq9Pj9RQwqGa99LdYjQfDr-j64jRgH_0iVI8CjIWbNyCwwhNLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآستانه‌دیدارحساس باتراکتور؛ ابوالفضل جلالی از ناحیه کشاله ران مصدوم شد و فردا بعد از گرفتن MRI میزان مصدومیت او مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28073" target="_blank">📅 20:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28072">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aba5f2ad.mp4?token=ArqDjKgM_bpbstWO-mFygA2o242v4eVfCuPiUSRujG8BUvwXTleBZ-E5L0BMGYjny52DMfMWxzfsIb5Ig6RtUB-vt_fWtgWgL5mnK56FsUw40uWtGb8zZVA8uFKu2MO2M35gs7iIOzUckFaVF-qi7BUfyXhftLcB155NXrGenRPGcAVvJobxqdUXk4w-kPTshyqZKP_5dXdaPO_p5EXyEJ4VCmEjWYMN9MItNjdhfhtIvk5q2_T__n70qJqatbe-ROG25v3tvzfD5PUXTWx7Z-oAaNfwgosepgWwE7wAyMZXmBu1zWDClo1XvRLbGcvuhL9NaywDuocMH7ZxPVXZTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aba5f2ad.mp4?token=ArqDjKgM_bpbstWO-mFygA2o242v4eVfCuPiUSRujG8BUvwXTleBZ-E5L0BMGYjny52DMfMWxzfsIb5Ig6RtUB-vt_fWtgWgL5mnK56FsUw40uWtGb8zZVA8uFKu2MO2M35gs7iIOzUckFaVF-qi7BUfyXhftLcB155NXrGenRPGcAVvJobxqdUXk4w-kPTshyqZKP_5dXdaPO_p5EXyEJ4VCmEjWYMN9MItNjdhfhtIvk5q2_T__n70qJqatbe-ROG25v3tvzfD5PUXTWx7Z-oAaNfwgosepgWwE7wAyMZXmBu1zWDClo1XvRLbGcvuhL9NaywDuocMH7ZxPVXZTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
رامین‌رضاییان ستاره‌فولاد بعداز پیوستن به این‌تیم با استایل بالنسیاگا کنار این تیم حاضر شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28072" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28071">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG0Py9Vyfp2NMxtf6KvOeZGVK372pP36CelgbNoP6Mozu-y2EtPu_kFt2Rbl1820TF7SYnpESmZFCZgnP2XBwy-gXYAce8IiAzkkysuYIfIsiPzNf1FcFuSfF6FMdTxMqAN9iJzhyNk7xbumqmw26Nc1nRSobmLUBQbZKTTrcPwcDpx2Nwo6TrzA5ISY2i47NcAwuLHT1XesFw5lxbzkCedyTHpkqCCpNj__4D5HL6sBEp_tppa0w3MvJRJsCCbLq7Vod0Ug2NXWaAsWyiF9kzbXQOveTa0nV6sHeXU89eXcr3txa-r8O09Euopc39R89NEOnD-h9oMcapxuQ51ALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به اس. خوزستان توسط علی علیپور در دقیقه 20 روی پاس مجید عیدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28071" target="_blank">📅 20:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28070">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBxTMZqWH5_d4fxq6L4MgLlPlAAq7VtpTPtxmgZsk_XeK1QhSPMXHCgKq-P095Kipp7Of6BnDY_RPRi29TlJRxOXW3h3DEjws70w1Ue-Aqi-N4uFUiS9-0G-zYsXphP0iTdtKASPnYeOtu6XyNruI5jlTk98PfsfiTEYL7O839YAIpBkdJdvC_Nr76DAN_GUaEuHES5CcmdYBNI5HcvNEBx4quVre-E4ybuna0QLBWXSjS1v0E7ExzgusbJ6m2XKeIDJKmz0HOP9O-OP03jXXtAsoqot14bCO5S_JCf5Ip3dacmDk77IljPcTLQNwvfnZfX3LOMhz94sUmQYTUcfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآستانه‌دیدارحساس باتراکتور؛ ابوالفضل جلالی از ناحیه کشاله ران مصدوم شد و فردا بعد از گرفتن MRI میزان مصدومیت او مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28070" target="_blank">📅 20:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28069">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b577f54.mp4?token=br7GIWURiBAN7mJY-7dL9LfXsJLMww7K1XLSVX02lIWYe8E80Hydl7tLbZYrw8A08M0e2rmGrRRTV6vdfJrV34wgvFmZNLp5HqXv7E8Amq418lgvkQvxbhXL5cMcMlsc-gQRVAzsWtv9WCjD5z1i33s2noNylAqJdfL5B2-4j3hUu_MPGntIIJ9d42afHs8a7y2D_AXWvynNmpJU3il6kZQwBwxNcd0QF7OG4JBlnVor29YlzVH0uHpfgdN-i5xRWL2yhcE_RPKdvbdtzY5fcTqH4x_mEuErFF0J8eU9kq4WAjony0b6gp7htE7HBr7cZpKSUDiYuKU9EUGn8o6YyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b577f54.mp4?token=br7GIWURiBAN7mJY-7dL9LfXsJLMww7K1XLSVX02lIWYe8E80Hydl7tLbZYrw8A08M0e2rmGrRRTV6vdfJrV34wgvFmZNLp5HqXv7E8Amq418lgvkQvxbhXL5cMcMlsc-gQRVAzsWtv9WCjD5z1i33s2noNylAqJdfL5B2-4j3hUu_MPGntIIJ9d42afHs8a7y2D_AXWvynNmpJU3il6kZQwBwxNcd0QF7OG4JBlnVor29YlzVH0uHpfgdN-i5xRWL2yhcE_RPKdvbdtzY5fcTqH4x_mEuErFF0J8eU9kq4WAjony0b6gp7htE7HBr7cZpKSUDiYuKU9EUGn8o6YyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول پرسپولیس به اس. خوزستان توسط محمد خدابنده لو در دقیقه 6 روی پاس علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28069" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28068">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f85915bad.mp4?token=g5T4cchRN6dVlWANYYy87Mg1ffFFFd41bt8kVLnQyyTXwBpGm3WNNM-BWa9ZQul0YQh3yt9zaZxfMJjvzQ2iTft_iNBI58htpXhF1QdRZuBbIiOuonYAxMzQyGbq23uFs9fxZwxl4_J4E2gnO45JD6w1hNaoW2jciYVVpSm7pztWksouooIKgkhIweSU3rJrWwzKXrbfd1E65Ti-42XbExRqYUWZlxFCFJQqtltvmGZf0EjZja7ODiXulGoN9fxrnDiiFA0iPvPChBezmKVTbvNVHHDwIuvg2E7Twqa4Y65_Nps6y1MXxZ7Zx_-69krlfHf-xOfwuVt4x9ffYLJBaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f85915bad.mp4?token=g5T4cchRN6dVlWANYYy87Mg1ffFFFd41bt8kVLnQyyTXwBpGm3WNNM-BWa9ZQul0YQh3yt9zaZxfMJjvzQ2iTft_iNBI58htpXhF1QdRZuBbIiOuonYAxMzQyGbq23uFs9fxZwxl4_J4E2gnO45JD6w1hNaoW2jciYVVpSm7pztWksouooIKgkhIweSU3rJrWwzKXrbfd1E65Ti-42XbExRqYUWZlxFCFJQqtltvmGZf0EjZja7ODiXulGoN9fxrnDiiFA0iPvPChBezmKVTbvNVHHDwIuvg2E7Twqa4Y65_Nps6y1MXxZ7Zx_-69krlfHf-xOfwuVt4x9ffYLJBaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب‌پرسپولیس‌برای دیدار امشب با استقلال خوزستان در هفته دوم لیگ برتر؛ تارتار کاری کرده که هرترکیبی از شب قبل منتشر میشه اشتباهه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28068" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28067">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568f2b5232.mp4?token=C9lhvBVwTEhghRRZuO2vyap6cG5y6VOHSkL0K7vRmh3dnYI-zyE3p2nAjKSVSuiXZYu92-_qy6LzVcqFDabadnhaIQXoECmyOYj85CawWcoHYZLrFDGSx3uI4we-cub5D1OmYQAtqZO9cG9ryPw_8e8y4LUjpAD_DZgxLys4AR93xsm2gFTMr9BRelTZJif53LtHGgPsHsou4BAb4hKO6C06yoJS8f3DznL7Xw4UTIRdbfoAkLQaSGp8-mDXjFTk5H2oZeLo0uakGhfOObrwmgzZGG3cnff8L9BhKMHll032V_KBKMjlmWkRZyg3NuuVGqe13Za2OFPGE8xbIyG5Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568f2b5232.mp4?token=C9lhvBVwTEhghRRZuO2vyap6cG5y6VOHSkL0K7vRmh3dnYI-zyE3p2nAjKSVSuiXZYu92-_qy6LzVcqFDabadnhaIQXoECmyOYj85CawWcoHYZLrFDGSx3uI4we-cub5D1OmYQAtqZO9cG9ryPw_8e8y4LUjpAD_DZgxLys4AR93xsm2gFTMr9BRelTZJif53LtHGgPsHsou4BAb4hKO6C06yoJS8f3DznL7Xw4UTIRdbfoAkLQaSGp8-mDXjFTk5H2oZeLo0uakGhfOObrwmgzZGG3cnff8L9BhKMHll032V_KBKMjlmWkRZyg3NuuVGqe13Za2OFPGE8xbIyG5Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو و جورجینا رودریگز در اتاق نشیمن خانه‌شان ازدواج کردند!
🔴
هفته‌ ها بود که اینترنت پر از گمانه‌زنی بود درباره تاریخ، مکان و لیست مهمان‌ها. از جمله مهمانان مشهور شایعه‌شده از فردیناند تا ریحانا بودند. در نهایت، عروسی این زوج در یک تاریخ برگزار…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28067" target="_blank">📅 19:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkrhPGmGKEUN9KjqGPh9oxtQVhRRoI3gUejmEVZWAEnv-rNiJMc9WpQ20wEKeb3xiIEQBnoLOVeOFS1p9Ao0JUeb5hvnw9Lv69uPmupPGO7oQ6CwBFGJQYySk0qIuFmZyGuxdTmDy8CYjbL6mBiQhIsU8kRDZvdtC3MLGqeGglbziix7RApNNmjGgOU1ih1EQw9RT8QnbXdFlxphIHW5ziEnIaBrxGulUDYOX7AKD3TugTLesGVIpAcaW6ErMIPOfnbMSdSVu9mwLNmqnqu1DoOqt5J52ye-X6Oqu5Ze3WDlL9rxvTOUikIk6pTQQsfHzPBdKOwW6AME718glAFh1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#اختصاصی‌پرشیانا #فوری؛ پاسخ‌ منفی ستاره سابق‌بارسا به‌تراکتور:برگردم اولویتم استقلال‌ست.
‼️
منیر الحدادی شب گذشته از طریق مدیربر نامه‌ های ایرانی خود به باشگاه‌تراکتور اعلام کرده باتوجه به‌شرایط منطقه و مخالفت همسرش فعلا برنامه ای برای بازگشت به ایران ندارد…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28066" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28064">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLVD7ko4fr4XEajbvGpw_IaQ_5X-VLu8aU3Nb2F43DnHh38oYYJeCtsEnvXJR6cx8BNrE1wsP3ylxk7gRuTFmyeCUeYN6uoOKh_QN0xGB7dauKC4_5d_nU1X4e2PTLuCGeu-TCvOcTqK4XB4IDf7w4cHIbVNDc46lUV5OXJ-yOyNfYkZSxkKg26gslSKf7lb3TxR9WG5Z_OBneqPBway4vSuqSv71iVhbQdx2rMM2Fzl3TqTex0ElXAd3-x8sM39CkW0ijsV3MgEbBh7YCHiOQjtrjf1T43RKKK3uYZz-Pk-QFibuK4fcnM_YC2aTnpvByGXDmg4m0AMAdtSJVciSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGecqHRbkMExJ_KspwHZl-ay-E8Y4e7i2dE3UJrMpnZBcnOL_K2IRa1d3kKnJFvp_fRQOiXWRrtwLRpqc7HGSjQ5Hur_ritCOYIh3hsMFCjvTdwa9Nc6YZlJaBP_bTOQeggiBAqb4N4Ke33QoUIzTa92za7h1fizUdWueYRrAcBtKj4wOFbQ5HUe0PB1bp-Jq5nmdBqFhmAZ7G6xS7TbazmT0kqpb8133T84oyvh5lXwcyPqspCMp2t6eE-kShPk59QJaSRf7x61TvxzHGm-K4BhGkNTx7mJ99QdKQ1Lyl4supqsGhDecJNU2Iv_sU6hpW0bb0PfFee5d7CWb3SnNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
صحبت‌های جالب پپ گواردیولا در رختکن پس از باخت ۲-۰ به یوونتوس، دو سال پیش:
بچه‌ها، می‌خوام الان یه چیزی اعتراف کنم. من از زیباترین زن این سیاره طلاق گرفتم، همسرم، همسرسابقم! عاشقش‌بودم‌دیوانه‌وار، ولی دیگه شور و شوقمون از بین رفت. عاشقشم؟ قطعا آره. اونم عاشقمه؟ آره، ولی شور و شوقمون تموم شد. فوتبال رو چطور بازی می‌کنین؟ فقط چون بازی می‌کنین، یا یه چیزی از درونتونه؟ تو زندگی‌تون، هر کاری که می‌خواین بکنین، با شور و شوق انجامش بدین. من بازیکن خوب نمی‌خوام، بازیکن با شور و شوق می‌خوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28064" target="_blank">📅 19:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28062">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZRXDWsS-jT-GQpvudYj1jU4x16_E92bAHlIszhirHuUt_qdZL4GX0AHnUGk5kipApoG7A-C83_pLbTmWyZkUvBGPz64fOBL9f0tkgPTHypbngEmPKYt2b2Pb9hDMlyaDIUz1B_N-Y0ZlD0aJT2qxKP9wGx4sgK5gyioQeYm2TrsUyVcrY4t8RLiFNxVlTJUauPta_hadqeiLhxd5eDAoBWkbHM8-wneiv10RzJkfL_Q8yFJ3HQzUOFw7xYTPJpqgG7GGHHlCfaiTMi28I80QEoLawjEizuyzj6vssNI64W4ZX4pZ_IeZgDyMAkgzCRYEH9VzcYcGmmnL1jDvpqx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28062" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28061">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoTg6Cbl8s-DilPpiI3ofmfNnzegD38XHNZFHEH7I_Eura_exbF5qmHXwmAfFYUlFRn_CdKRcuZqbuYbtfLywSH0w9V8R9ztsgomItIda57GH4-T8jw-4I9N9ikxqNf7mfUm9AKxlE3LxrfH4PwSjDGpiIZzcZCixLyxcl6TH44YbeZVTF3ORGk6tDCMnlgrdA-OYPMokPMbAOCbd1515pajCaDuYnOUn27esBqgY5eLrXvRgisP1LR0mH2RU0VpnLeVjQUWUhmkj_tuYL8XI3ZZSod-fKmJXuJs9rCBScb5CulTUgEeV8ThCLcFLMnXNantO53mYxda-ZOp5Lq1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم لیگ برتر؛ ترکیب تیم پرسپولیس برای دیدار امشب مقابل اس. خوزستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28061" target="_blank">📅 18:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28060">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWo_usSqkGyos6L1QTiP0GK2Aogh8BaAR3X5NdA2I6zxsYP5O2NWhIxYimoQjHc6hiAdHwepm1N7Ps8g38XDqt4uMfS_KysV_LSudott2FQSzAASmSXUXvt-r6nAnKccOg07BFa3m8B_Yh_k0MaipIkQ_SjjIC24n7stag0wW5CJNW6-GmFieKTMjfdLRg0Zy1N8ZBC4Ik_zQF22wO04ewsYqWL7z-75A116HFbabI_OmqNT4T7Q4QS60A1EOpHrP6w9GeAtehTVDkilzK-pfWXMUSaF1nTxyGC5cALKq-e_wNtqpcZulttL3G6fIY9AuArfZoqxJktD37galNko_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه گل گهر سیرجان به خواست مهدی رحمتی با ارسال نامه‌ای رسمی به باشگاه پرسپولیس خواستار جذب محمدحسین صادقی وینگر جوان سرخ‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28060" target="_blank">📅 18:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28059">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPXF3M5a9AOXxQj28Ez7yMOw1kt7V0IO4gii5yUpRoZ1xvP5BkDkqPHM3qVKM57cWJCzlL2DZJAel0u2UV_bd1lu65uCdYR6slZP1Y0wnuRCbTlKUe6lgcG_osBv9L0_z5R8-AX3_VcxIgPN2_aH7GCYULA5ceuXedggh87Gd-VQnck4ueJIxNVNOrvuUj7AC1mW2lrjgz9Nzc7JkWv1PNw1aujesRt2_BJDLzjgV3N-E438Z1RaqBMvA6_yicnzU1xIlTilmPBskXbceigINf4MMp1H52O73qTznkyso_8nAacF0o7G_OBAuzqHBAV9_2CKDqg3ElJoVKJ79ZAFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 5 دیداراخیردوتیم پرسپولیس
🆚
استقلال خوزستان به مناسبت بازی حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28059" target="_blank">📅 18:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28058">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41809830d6.mp4?token=Ml6zQwhbf7ynJYIPQnbc83UWPBiCiCC2teD6h54DI_VT_5aYnrWZRDSc9pVm0bgwhNf5W1nKE2gMMrZo02JWVYU_Qq5eHwlt4mpBa2mviMP4OxQaHJYjlNu-fn_e6s1QwEbLZpuhaCYCDjoBdbAQdT6946u5-1wJpeQkIBdqXyvlGQWW29xAeZJq-pRp2PFoZIhFavf9oB8kwnsqprWPMPof_RLzFdaywqxoeSfsj9yYVJOVegh6Ms2vUk6YbbXVbPmresFhB5UP0zz2v5zJkSDYgxx9syfC7GBRGVYKLe-qV0gem-nnyKhdqoC-14t92K0cOQ_6JRnUN68g84-eFba3ku-96nAADCGeX9uD67I9gJp85778_CjMEn8OuXXNKePeU1lfoZoQEdPVUO8DvIbOGBCEcSUDcvDwqOrk2OZ2S_t32yRC8T8jzWkbB478Uyt31-Rhbkmg653yL5KoTSbMjz_jHdhSi_tyyY78JFiKVdIQPdTes45foxm-INT1gY0rQAzw4bWD5BcBbkpzqv-xYnTMnIwVNIzrfNN9sllIMGNLwVN1xgPxDVMBbN5KRerFeOa-kEX8l0YqUVL8epRiupdgjtJUrZdced2hdcjxkTMI_cM2QU5dHt-n-afvYOHAdUhGIpIhyzpcI08Zo6AuirOdim6M32uUZrXrMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41809830d6.mp4?token=Ml6zQwhbf7ynJYIPQnbc83UWPBiCiCC2teD6h54DI_VT_5aYnrWZRDSc9pVm0bgwhNf5W1nKE2gMMrZo02JWVYU_Qq5eHwlt4mpBa2mviMP4OxQaHJYjlNu-fn_e6s1QwEbLZpuhaCYCDjoBdbAQdT6946u5-1wJpeQkIBdqXyvlGQWW29xAeZJq-pRp2PFoZIhFavf9oB8kwnsqprWPMPof_RLzFdaywqxoeSfsj9yYVJOVegh6Ms2vUk6YbbXVbPmresFhB5UP0zz2v5zJkSDYgxx9syfC7GBRGVYKLe-qV0gem-nnyKhdqoC-14t92K0cOQ_6JRnUN68g84-eFba3ku-96nAADCGeX9uD67I9gJp85778_CjMEn8OuXXNKePeU1lfoZoQEdPVUO8DvIbOGBCEcSUDcvDwqOrk2OZ2S_t32yRC8T8jzWkbB478Uyt31-Rhbkmg653yL5KoTSbMjz_jHdhSi_tyyY78JFiKVdIQPdTes45foxm-INT1gY0rQAzw4bWD5BcBbkpzqv-xYnTMnIwVNIzrfNN9sllIMGNLwVN1xgPxDVMBbN5KRerFeOa-kEX8l0YqUVL8epRiupdgjtJUrZdced2hdcjxkTMI_cM2QU5dHt-n-afvYOHAdUhGIpIhyzpcI08Zo6AuirOdim6M32uUZrXrMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سم‌جدیدی‌که ازطریق هوش‌مصنوعی ساخته‌اند با حضور ارلینگ هالند، کیلیان امباپه، مسی، رونالدو و حضور افتخاری رامین رضاییان ستاره فولاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28058" target="_blank">📅 18:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28057">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCxU_ON23MVea2sH9O5GgxwzQmwyMv2O5q6kbOve26MFI9375u10OVO6yKeSprPeigIYgoYY5YyB8-nTVtcRm8rhisnyQ6G6YjJEqNGhnecat8iJUSLj4MdpWpMHxkuOD_Wnn3OjeBBQUO7S1gBURkTVmF8dWcCMwzVaMGlMKIR2sgze4p0XdF1fV82oA3xmvRCQXD5O1Qz5gOk5D1bf0d9ubEbBRVk9jJxNujQGiCsk3LnOmAiGdVpdoZV6ONS55GcV4YGYoZLjEMGv7ygU7igIfmik_20sQzqLh4DybWejp0SPByVOGZbD2RDnMqQ3eH7tpEyiKD40xRj7d4PZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اُما مودریچ دختر خانوم لوکا مودریچ که ستاره خط میانی تیم‌بانوان آث‌میلان بود با عقد قراردادی بلند مدت به اکادمی بانوان رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28057" target="_blank">📅 17:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28056">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMo1CakffnQLZIAtyfrrYfqV-daURNowQdXACNclYq4oKcQP6oNfWVwwXrAc0WR1fW4hpYljSTx1M2ZqN0VnaGP8WvLkqK3gT5Jc5jhYTNCzlmWIpnNsFoaYIhSrDUBHCBBg5epEx2U0Rlge1w--2S-kCDr9h1VsB4l0k4jBgSvdcGUU6rJXkK_u9Hr9DLV4O0gER2kgZVagw6mUdY0gy5NpALtbl5cKQ7xLI92vMl8BkgMfnLixa5BN9AFpdpodb6MORI99q7T1XIJy-r01MlSBkzKjt0YTMjZx7-ukVBZpNXP1IB_vHGZuCu40mVd-ezMOUd743QptjLn4qBicFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امشب مقابل اس.خوزستان در هفته دوم لیگ‌برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28056" target="_blank">📅 17:32 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

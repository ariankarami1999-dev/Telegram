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
<img src="https://cdn4.telesco.pe/file/s5lKNLKN_QUChbChMKQrt6y_rMJIgKRsieIlWeXi1R2DVBGMU_baC25V12IJ6GLOMgfAui7Vo2kNXjOMBMGupdKDFpmSM6z3GFYegW8tBoTMyyZx0KvtyP1FxBq1temqZ7Leo6na8bOG4sduRPXwFCkxpZm08nQQRpUbOZ13rXhfvGUHWXHwt0PW4j5DhJUw35ezan5SHlBtAloeH3vWq3nYMbYKLbvlGZNMT01v4fl5E4vPRMzAKrtAEHLOSSAqy_c_PPj_7aEmD_HuC0HYCzQOa2jVPL5CHB3sGNukvIgkkkloTG-pMgH0eMuWfKhNmPxg7ENvoC_UM3v3aTKsyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 141K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 03:23:57</div>
<hr>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=kiO49vuwQRLCeKCn_BELVoFGp3FR1XPfGBcep42A7N0Dy5rl7voLpoKL6fJM1fybqOfaFfa--1wSkm4CunCiutKhKutoZ6tdzxuQsUWDp_kDw7eTt7ZVIKdcJfDvp7zf-66vLfA-oNhP6VCrMYlSO07aYDBEjF2W2GUVXZNfTJHsfdh9fhiicsdFjfhZ5MIEyiwgZq1E7ajqE-6NUW7fzXEtIPedcmsTpUWksBvW44giRhCfki-IXMdPBvl0E-NyqmFU7qujwy3V6vGEV9HPLq_PsQ0qHF_DUcX4wM25a9iKjQDsBnXkWbqzyHTSy09G1JkHPrhuDAlQhwA8zh-6JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=kiO49vuwQRLCeKCn_BELVoFGp3FR1XPfGBcep42A7N0Dy5rl7voLpoKL6fJM1fybqOfaFfa--1wSkm4CunCiutKhKutoZ6tdzxuQsUWDp_kDw7eTt7ZVIKdcJfDvp7zf-66vLfA-oNhP6VCrMYlSO07aYDBEjF2W2GUVXZNfTJHsfdh9fhiicsdFjfhZ5MIEyiwgZq1E7ajqE-6NUW7fzXEtIPedcmsTpUWksBvW44giRhCfki-IXMdPBvl0E-NyqmFU7qujwy3V6vGEV9HPLq_PsQ0qHF_DUcX4wM25a9iKjQDsBnXkWbqzyHTSy09G1JkHPrhuDAlQhwA8zh-6JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-bB7Um9I0KKrCYrGKMWa2lth2iTkTi_Sx3PUR24dMsXUgqtL7JEZi_KCUkdsVbfuAU3XcwWSWRQ6P4wNCjwW-qLALsiGvtZvlsQ4ifzPJjSVTlEdyvgSPGmwkHEW_iMq6pencaEbcInWHZ3E02BPYo6h8d5vtfGMAHdsHpT4qFopiaDa3FmJ7NjYR5q4SZ25WTbVEVGHrh_T2t7pq9VW1yaeH1MBJK89QPBBLFaiHRdJBjC9OYV6eY7U0w9rzjJRK0c3MWTpY-XouBgzAR3iA6QfKCtUpTVFG5GuvDO8rPQWlHpdxcCyKoDvy6bE82Ug1Y1_5elVuEl5o499fL49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0hSuQicpecqXwzUfzH5r44cD98jx-sjsVXBeEEx0QkmdwkNOkXP5vqyzMZmfTPvSlF2YBxFfkFp1qYZyXjHQTLS3jOgf89y-WhiFR8OwTDsO38-eg6A8hETQ6HW1bGX_6Tcu8tLvoclqwOMV80Cej1ljJTz7IW81ksZN-_hSrVV94kxoLp0DWiWwCUWmg9SWHpB60e9phFZ2nt7uzdwCrOMzACZ-pZiqrIi8uhNVt-1k1Ul6Fc4mSG7OCsQl01wJZw9_-c_nB9f61tYv7jYZxaxfaOH59c-E0OsGWlx77_y4ImpzMhjwUVGcVT04LVA8bucyvcSKv9PqNW1fGawUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUu_isiW9ZD5lZd0-rUo5qQyyK6U_-DXtNOkLqeFD22xH485Qktu3u9P1yHNjD79V9ijjJmhUFhfldvwkrV30m40cZIHOHIt5o1ivwRfWSbBM7DWqMDGOrUmlqHgwwdPmT2D8q1V3RArKfwYl-qR51yk1oEl4CIXFhdkFebV8ClWLrhnmDHtLg4gjErpK-9HJCka8Tb-h1EIZ5Byn-_Dy9M5UKj-hN1pBzLFZgVbiF-b5-8b_mbIewG_-fWOnqKA8xX17zh3kyeUA3T8WJ5KxA0OykXAoPFz9GbLUh_c6-Vc0axa5g54Aejb0fIB9T928QdD60jL8DNcuLJPNE3roQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WskFvZjc5PuDqiTmuVnJGrfS7zCM9NjsTUYiFdZM1iLYqWS8wxRurfKZ2sdy9mch7vnxkPby2TzNVfhtJJMuuOO4wIDixeXPNZ-UKa7wKFt-11V-cyBKisxO2lCG4PbZW3sD-EcSpdCj-4f0yY1sc7MUqbaoebEiV7cu0u2bro1Z7nZLvnwZ6ppF8pGASxCIm0PHxmDh6FxpvHi6bhAKUjl8OFBj-XYFr_VgT0ZL6_TBAl0rOQU32cjrcsU6jHQnJ-xpy_o5_MT_r-hCKYMMN5TPdUIr0OV6YBBD3hgureVazMzd_tusAmtTC4duMbxMBo_6FCYQqd7azRtbc3aQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtXD5U62Vpu9_MlZ7SlEtV9SlploqfLmk8cuZvk3MxiTatUkOrljU74reomiaQ1RiiFuxNva3xtQ3Xy118ytd4oTnFghnMfgDREqA_z-Ivas-cqyfxZEb5jUIZm34pqWPDYnC-sFzqPkUA3p3NP7c7Q58Ri-8a0OhWeig-shLEsT4AdB7S0ZXyjIzaIJSZGWWZIBeRjBwZhUcEa-kZ_34htyGcmOWXh7Mc1yx6UanUOcTX0aK8DKZBmneRGM3tCNJIv9lIWnGiER0GtqmwVCXdpTyLU3gEmdkHv_Msc0yfKSq7eObIGkf9I9KHcrsvtoIo9Lmj9ssE7IsONwaWeIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjP29ZAcM2E_oKwzz53HAfJqD9Dzn5BusfKSsHJmNMaIpbO0D8GQQXt9lHMXaJRTpde1MzhztwzhipbQHyl_uXIwQ6EOsWjoE7fE6xCZE7WcJ1ricrDi45gkSmcnXnRGuC84U4YLNDIqNCSXrqsRdOj4WJ5jCONmd2dCdE5GkLTyBuyKcNtM0OJh1clv188ryQfV-yJbDfjDJkToyTC2jUGoVaIB_mf45-FkwcfdpRokx10aXPYahVajm96GLKVC4xrB8N2QDrTQkuHF68ds-AJ8GWPZetz9DW7RXU5I4VtzCiKGpg0yHo08EMZ7Y6XHg-pn1SkloUi1uj8hPUKJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4FSQkP2iisy4T5XNQp7e4vc2bSWBn7i4dY5V02LDFRCLoNsPA_xkK2h_z0WWg4MTADTOap2tP9S-bRi5uHz8gdI5CiUjunFOYyZll-uAa39f_uzqEeu9U-uo4BG2r7PdiyauF9SDxIh_Gl8tmDnV02hdGh9doTVECDLqSWsoohEBWurIDAImf_pQbODv0cqJf8lbgygntmUNjr0LimGtcqNupVZhcm2CC6zc5JAvbx7Xu_c9Kwvt3vE8sXav6GfGHh0XyJcwOT3o-iz2OoZc8h2EfkpQR3cC50aMTEbhn4TJhwZARsS7LOMrvMwuxj6hhTeIzkV1hh_TpjRToJhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i03Oo8aFkM40_XNhCWQ0EJCnJsSBvm8weXF_2UxjL36vULINRC3V5XhpbFP8TWv539C3jfAl6tcbV594IKinDH4bVNixeuAbpYUXREauyLQLxwPzRk5HMmAA8s6t0aBzWkRdloZ_i-E8b6CuT2A85L1Q5MoHtKAOl0l6eVPGdoMDFIoVgUaLnAD7Rf90Rl0_a0O7vF_J0kiRNnKl3rAGsfYZFru9hoiQHMBg8r_1mwY1XaAdZL8IQVtOgOCPU3rRdZz7hteBl5hcLiaEETJ5dCeU0pNVxLKIMmUkeDC3MIbhrxW4sdf0rm7bEvwHSHHMCnIc2Ur_3nG7z-F6R-BpuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=r-PAfB98gObFr4YLKhF7GJPvfJGbpGc762TOkcutOZLDLygDjSfe2IfXOnoIq59fjDjkmRBQqf9SiB7IMvz6-5gVf9abx95wng6bKhT-y95LF49SksgrE77v7UNGbpyFbutBZni9ZWflroO2AN5WM2c9LejZpHsF-tanP9TtQinChBdGfn4vP07cOF7lP17XZ3h7YwXwLSxFFSUqYtJccPRujM88bOnEWSs4cPpzjEsrS4uSfRoIyrERiKL78cba45uX_0MUEJ8Socii7H5ZpG_dXmHxwdzI85CmayOdpgVZAACi9OvMgg8lHrJqQiSHgSXHc9iPNElGyf_8SP9Y3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=r-PAfB98gObFr4YLKhF7GJPvfJGbpGc762TOkcutOZLDLygDjSfe2IfXOnoIq59fjDjkmRBQqf9SiB7IMvz6-5gVf9abx95wng6bKhT-y95LF49SksgrE77v7UNGbpyFbutBZni9ZWflroO2AN5WM2c9LejZpHsF-tanP9TtQinChBdGfn4vP07cOF7lP17XZ3h7YwXwLSxFFSUqYtJccPRujM88bOnEWSs4cPpzjEsrS4uSfRoIyrERiKL78cba45uX_0MUEJ8Socii7H5ZpG_dXmHxwdzI85CmayOdpgVZAACi9OvMgg8lHrJqQiSHgSXHc9iPNElGyf_8SP9Y3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=VlvOZO3HevsMRbK0kYeuvSaJ4sH4EJ9UFF0ADn8HriEKwKo7vx2rn2EJJEmt3RznvNxn62uyMJxY0Ehas1TxONOfiGeaQBBGyvDxf3iLh7Ov3Z_L82eu9uAqIY7xNoRzbPL00LsRHWJK0m8LlT766Mv_10lFXyvpj_SeIO7To2ljLU_7GPXVRCrNU0P6HWRYt1rJi9Vq0vs_xn0KXK6pKL5nVC9HQq0ItgabU2fOST7hI0c5O5HJnNxDHe9gMsBFGcJiuESeJ8Mc3NkOrnAV-v49scy--MgcwITtjVIT5DOd5XRF86EcLjptpNRS97XWxbF9aXxmr8M0B350ec_T8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=VlvOZO3HevsMRbK0kYeuvSaJ4sH4EJ9UFF0ADn8HriEKwKo7vx2rn2EJJEmt3RznvNxn62uyMJxY0Ehas1TxONOfiGeaQBBGyvDxf3iLh7Ov3Z_L82eu9uAqIY7xNoRzbPL00LsRHWJK0m8LlT766Mv_10lFXyvpj_SeIO7To2ljLU_7GPXVRCrNU0P6HWRYt1rJi9Vq0vs_xn0KXK6pKL5nVC9HQq0ItgabU2fOST7hI0c5O5HJnNxDHe9gMsBFGcJiuESeJ8Mc3NkOrnAV-v49scy--MgcwITtjVIT5DOd5XRF86EcLjptpNRS97XWxbF9aXxmr8M0B350ec_T8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=MIN2Q4qpeQcAz77JApFE59Y1OgJ8FoTXqIFGeRnEqzXnTAxHkdUC01MsPOu2Oa6E-FGyngFXg2kOHP3b9YdfqUra70mhvlrbQoyA1Qra-rLZTEbh7EYLCX8yLG3M9BLwpHtbzncHHeHBaU7gUcRVRqMQS_LJgZp7-K1XrajbFmsfBrK4RKYEkIuMP0IGH1ne2Toy9fH8oQMSZ0SWVK0iBaMbLI_BV2GPanTGBRTgdtX_KVFkBwYnBBy5KhXRns9oropJdBe7MGXhgXfN-IyswXEdA3r63sB9Jz0liuZTBl2rpSnYGUo5UnBwJSbutbm3ZvFx_ONneodb059jsS-zbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=MIN2Q4qpeQcAz77JApFE59Y1OgJ8FoTXqIFGeRnEqzXnTAxHkdUC01MsPOu2Oa6E-FGyngFXg2kOHP3b9YdfqUra70mhvlrbQoyA1Qra-rLZTEbh7EYLCX8yLG3M9BLwpHtbzncHHeHBaU7gUcRVRqMQS_LJgZp7-K1XrajbFmsfBrK4RKYEkIuMP0IGH1ne2Toy9fH8oQMSZ0SWVK0iBaMbLI_BV2GPanTGBRTgdtX_KVFkBwYnBBy5KhXRns9oropJdBe7MGXhgXfN-IyswXEdA3r63sB9Jz0liuZTBl2rpSnYGUo5UnBwJSbutbm3ZvFx_ONneodb059jsS-zbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=DsugY2u7-GPo76XzSdpo4lZgaRNXwtiHoaxIlX5feZFGeIKzSIF3JurARlIGaOqKLNbV86mSy4eU2-q225pCCRHYvt0VWkffY2g_xuZTCByasdaOH7WW9g-HdE_oTnlzDJvs5f902al9VkGfvD-k3HArQb2GGSOlCaDYOyO-AAxWNHod2PZN8-0BR7IGQ7fC2c7vX03B0UONro2htGREqlOdiNtUMAa3_4Fpfpux1n4QqpQS_NUlzCdqhHy2lVZg-kjzvYlX6NXr4HPgSHF4GRjfhETcYcTQIfJVyr7wr8yXz5FLjNR7lSVb9-dQCMdnYXl0qolmfgWsqoTy3bAR5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=DsugY2u7-GPo76XzSdpo4lZgaRNXwtiHoaxIlX5feZFGeIKzSIF3JurARlIGaOqKLNbV86mSy4eU2-q225pCCRHYvt0VWkffY2g_xuZTCByasdaOH7WW9g-HdE_oTnlzDJvs5f902al9VkGfvD-k3HArQb2GGSOlCaDYOyO-AAxWNHod2PZN8-0BR7IGQ7fC2c7vX03B0UONro2htGREqlOdiNtUMAa3_4Fpfpux1n4QqpQS_NUlzCdqhHy2lVZg-kjzvYlX6NXr4HPgSHF4GRjfhETcYcTQIfJVyr7wr8yXz5FLjNR7lSVb9-dQCMdnYXl0qolmfgWsqoTy3bAR5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbe_dp7zHRFNNDnTBZoHT2eXPCxYqwcRkwVE3_syVHsYxhr2BQ5dFPyQGCF6m64fDTfodS1GXjneaQU1mG3YrgM9kklmfRkk-QfjazTWlFh0PeQieiNpSy4nuKC3CcSkOPbXbyR86pDRt8HVY2jX8gvC1j3scZBsHw5Z7pCqW4rcaISCNzCHc1YUY_YRWT0LmtuD6nrEd8h7shxr1HjSHdjBqTAKuzi5Wnp8uS2t3LElCT4foA9mzlfbVLF8lRdvWY34tJ-Hu3_WwfrygrQ2J3ExOAG_qTfUkvFXUpQXYOxPnZF9mI_VEuGX8kYBMBSIAfj-9H_Xrn_Dm5llSFe0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoeiJM38lX7lmbVB827QkEmh63hh0GyxUpeO5FnSmIrlwMR68cXKmC-a6XDWaz8W4gAA11XWVi1EVzoOe1Yd8boMpj6Hd1EtSC0l7R-_27B3RALpq7Wjy02OC-_Y8LFkR-Ek_BPi_tdicKHMQ1_Yqma879szFpdicVmW-RF0q3wI4o3dvoMdVwGaVABqbG6o1uo_XbmlMwBl9QQ1ydghtPIUcjfeufvyZeZSEmSh_eYWTJR9_h2lx8-Mqya2hYB5W7pHrAXW3kE71JGrvM-B3uYgoO7oQTGOvr4ZHgIuqxWbWvz0ebULPAaWvyYuANyRgxmGU874LqPQcQ7yFH4d0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AGR6AeZjiNVyVJerOMlz2SI9oY5DBDpw9UeLQftHeItb4yckBM4kKF6KY2xLnUYGhLuZE590f7zgGyCEfMbAxFePSC1_0T7K8aFLKKIIGhEfzuSbHNRWWfeE7PhOtWI_pq7QIikrNmEv8a26Ra9l8hJAwWlFPBZpD8ufluiRLt9fH3Q47c4rwFbIiG65K39DUtPA2BpI8VMW2CBvnsvcSvIovR-N6OB0tkTXWxjlbA7tgr_xo05DATN9-W3NbbZl9wqUo5M9ZFB9rGP_mjLQKa4AZEBV1r02WFSfQtOv7utkumL0Lvmd8hl3JM81wzVJH8Tw7L81zF6ZC3dWfejpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=ES4GHh2yS1MA5XLpD7YR4OFLLPyEfRdRbwop7zuJvmobXXQYMLPrLFcvtrXoek7uS00UQlipM8UOWPZwjMvyvOYVeFLGnCuFMIlXqf42jp5f8GO2qTaihXNMG83k9wDxZfG0IDjDHt6S-KmWCHrXNZncyv4BMKQsWewknD0WLCUIofCs54baUOr-VMMLdebTN-GMdio08gyKVfdt6mB5q4wUp9LZODftH7uwSmf1ip1DTtIGD7kQfSWIg7ZDHTO94VEs4eZ5Ybjz2bOmN05Jj2rB5yjP95zjoPXudqUcJIsF-mhxdaNbgOwOg0vWHDhLSgZ5nAw3tLM_kRNiIPT7KZfH2MXU79_zlzhUBYbATJbFcCKBwi2HUdkO_jhWR3cYsnWdm1v0-oX5pgtVAgSkZ3F-Iqus8XXJ1wb4EGRXOG8fGejfxSPQSz2UUpv1Q9lkQjPjo4SEa1vc3fvAtmiqeWU42l-ff9oAYifwo-e2gcrPVPYw0nAoJk844BXOL3zj1WWrvSOKYDrImv-EEh5jkIAcC1opSSheL5qpPRbMMgZSEXhFIgRaWR5DlxNKhrlOKocJHiEED_BZOHFS0oBMxitnWQQJnmey8I8zTlnDDpuJ1BcELc_mUb5x2IANoX-7u5K2jL3jr7xngHCCBvbj4eTgIFpXNiWYOroZmtHZiGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=ES4GHh2yS1MA5XLpD7YR4OFLLPyEfRdRbwop7zuJvmobXXQYMLPrLFcvtrXoek7uS00UQlipM8UOWPZwjMvyvOYVeFLGnCuFMIlXqf42jp5f8GO2qTaihXNMG83k9wDxZfG0IDjDHt6S-KmWCHrXNZncyv4BMKQsWewknD0WLCUIofCs54baUOr-VMMLdebTN-GMdio08gyKVfdt6mB5q4wUp9LZODftH7uwSmf1ip1DTtIGD7kQfSWIg7ZDHTO94VEs4eZ5Ybjz2bOmN05Jj2rB5yjP95zjoPXudqUcJIsF-mhxdaNbgOwOg0vWHDhLSgZ5nAw3tLM_kRNiIPT7KZfH2MXU79_zlzhUBYbATJbFcCKBwi2HUdkO_jhWR3cYsnWdm1v0-oX5pgtVAgSkZ3F-Iqus8XXJ1wb4EGRXOG8fGejfxSPQSz2UUpv1Q9lkQjPjo4SEa1vc3fvAtmiqeWU42l-ff9oAYifwo-e2gcrPVPYw0nAoJk844BXOL3zj1WWrvSOKYDrImv-EEh5jkIAcC1opSSheL5qpPRbMMgZSEXhFIgRaWR5DlxNKhrlOKocJHiEED_BZOHFS0oBMxitnWQQJnmey8I8zTlnDDpuJ1BcELc_mUb5x2IANoX-7u5K2jL3jr7xngHCCBvbj4eTgIFpXNiWYOroZmtHZiGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=n0zWTDoXekeC2lk2tAVi5qdJDv1fl2BywP08xBEZDQlzA8V1LlKYj-p3M2kx2Hmji_JgHOzcvB4z6vuuGRXw5cigONyKW9lLCq2pFdgdhPvN22KmKzJfJItmwzw4R3iYEKvPMnDBuR7mItMKBMjrx-p0wJKMxb6sHYGh6PKeDik798SjbT80ypOJsl_zDRTqyCeNSwRSefKFIHBxz_NC-n5ss6kX4ksoG1ej3xg4eQ9sEl91ujKre4uXz-coGG_d1Ws4ontG6-nVbfldUMDD8w1aKUxrhg_819PICXEXqi3BMg8MIoXeV-OGX7Xny_y-SX7KPRMw5yyJvDdccdnFMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=n0zWTDoXekeC2lk2tAVi5qdJDv1fl2BywP08xBEZDQlzA8V1LlKYj-p3M2kx2Hmji_JgHOzcvB4z6vuuGRXw5cigONyKW9lLCq2pFdgdhPvN22KmKzJfJItmwzw4R3iYEKvPMnDBuR7mItMKBMjrx-p0wJKMxb6sHYGh6PKeDik798SjbT80ypOJsl_zDRTqyCeNSwRSefKFIHBxz_NC-n5ss6kX4ksoG1ej3xg4eQ9sEl91ujKre4uXz-coGG_d1Ws4ontG6-nVbfldUMDD8w1aKUxrhg_819PICXEXqi3BMg8MIoXeV-OGX7Xny_y-SX7KPRMw5yyJvDdccdnFMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA2dEwq0WLoQ_8QFAaYMdGzLbmXI8PiQ9iuWeUFS3q0f9T50rpv8d0oaPhISJ-fmBtJK3TAg8MajvCsWBqDfasrZk77dbSN_JISlo1ueysptnKIDpJaR4lLcOBN7PuIzGBfokIW5WFWnXBfuIWnvEGBwo1Wv5knQtgJhyHxkOpMPWGFCtx952aqjtkjZ0Q2Wi3c6xEzdSwWxzm4-0tkP58tiuSBOe1Tq9F1StYUxV9uLmpidR5jBRWX5VbYiL4OvcTpSrwz--qEADxQa_AvAelLPUzfSqgLUa4WIPwdOl0kmKT_-H679yb3xcl9kw2tM5dZzYGxTOzAQaz1ari3_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=dc0vCJ3XS4z3pRzzzl8Umrbcwgw8QQH5Szurizwbiroaz_ZjW3wTRNYPMceOhOocTbVMOq19bEdiUQkYVnPbNaLkw7ADyt_4k775o-VdLrdib7pB14Q6DvWldrSWdU4oDNVq8TQYcOMeCX9j6Jg8DphcAxX2SRtT3E7rynQOXAIiNLBPAagKdzj3MhW4dpjCEZI_Cyq-GwFkvhDaPgLxPk-kwFf3cWVnSAIvkJaWVGI6Qm7z1LHLUtpAZflYtVscVuIOSolHpTrB7wA02DTkES0fyffNeVLR6byjXlX7VC8fZBJ5yxSStM_4RT9oFZAIyzxx8B2z1F4y177DODV3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=dc0vCJ3XS4z3pRzzzl8Umrbcwgw8QQH5Szurizwbiroaz_ZjW3wTRNYPMceOhOocTbVMOq19bEdiUQkYVnPbNaLkw7ADyt_4k775o-VdLrdib7pB14Q6DvWldrSWdU4oDNVq8TQYcOMeCX9j6Jg8DphcAxX2SRtT3E7rynQOXAIiNLBPAagKdzj3MhW4dpjCEZI_Cyq-GwFkvhDaPgLxPk-kwFf3cWVnSAIvkJaWVGI6Qm7z1LHLUtpAZflYtVscVuIOSolHpTrB7wA02DTkES0fyffNeVLR6byjXlX7VC8fZBJ5yxSStM_4RT9oFZAIyzxx8B2z1F4y177DODV3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=QpWKW64Yc9ajc1oGc37xBgwg4V8CahOGw-viBMQNlcSpmGq_B_3RnK19AlzMWpmrJ6e3e3aWWdcPtljjmsrKTTcEvc-ULQ5EHMYhOQSJD13ndmJ6wPd4aSIf6qN8G0DQxzhXQK1wMknX9Blvwgb5dDpM9iCOBqu9KHuQQefSxXfv-kE4qI4bk6VZMaZFX_aykFuH8DarIKaeROcgeV8Jk1qun8QxgqQQk3W8j4KdlIZL4Ep_qWD_GNsMVSlpu0ZEgBbd4HlE17kAuAssr2Aepl2M94lCgo6dr0Mi5wMgiBGJSjNxtLz6cBQi7po-G8YSrJ6hJjfGOg5pIHCLmtBdCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=QpWKW64Yc9ajc1oGc37xBgwg4V8CahOGw-viBMQNlcSpmGq_B_3RnK19AlzMWpmrJ6e3e3aWWdcPtljjmsrKTTcEvc-ULQ5EHMYhOQSJD13ndmJ6wPd4aSIf6qN8G0DQxzhXQK1wMknX9Blvwgb5dDpM9iCOBqu9KHuQQefSxXfv-kE4qI4bk6VZMaZFX_aykFuH8DarIKaeROcgeV8Jk1qun8QxgqQQk3W8j4KdlIZL4Ep_qWD_GNsMVSlpu0ZEgBbd4HlE17kAuAssr2Aepl2M94lCgo6dr0Mi5wMgiBGJSjNxtLz6cBQi7po-G8YSrJ6hJjfGOg5pIHCLmtBdCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgRtorgWp9Ci8LaGTgdJtYeXlOEuDbcOA6IqKUe_ZOl-tcVaW8KR3DUYRDVoo7VKjQG1mu7h-6wKbo48XCg2tz4xw0d2w2tftc9XP5P43sKZrh6Lz_U3TbgjYk0VKDeKRiTD1g8QS5SWqKXomDEkzhYswL6zzRLUnRBar_j5Z-i_r7_IRRmtQ-oIf4fDte1xDueJyaPuRBmGn7gYqMrvA6KSKtqPMBF-uDB0a1t4H0bfveuURWegx-uk5lspP2D16rYRjQ69DeipOU5iabznGYOaZJ8LGwzrRHrREQqWGUYirlnRVXmX2iGWCrd04ddKDnL1Ra97uqYpofKYQ-upHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNX_bokSQAccR6kVHVtR474LHqOT503rw5_BHNFmPDgh-9onXXhj4aWTaYYIJJLk4BkUNuNCAoi0ESrGTI_mbG5uYdXIYrkXoAp1m56DaK3aG1PmlwP2bbO_NU3EKuf4dfvjRnALafAdSojIP13HA6vouFLQojtPpJBZ2AAQ24ntS6WIZ3qD_e0008met0oMEqQ7lFkiPll4ydg8oqCOwMaGJXAwyLTnZtSc0Z-gnPFERsFsZu8X728rG1hnBNxmI5LD9rNVeE9x4L21LF54tyAxhtHqP9iTt23U4sQHYh7VFkg_fRCCgnMXgQqA6koJV6qwBnS8Bl6C_aCwdyXl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MycRyAoWngXUzyWj0oKSRjEdj5Ia7IYP1qltZbNyVIOMuNAYJqcMe6smIG2tHabEUl8DjYhIyHs-uQ9C9y-Z0IO96hquwxW_mVdV8putds-RXuGe8UJQcRf6o8yfYwa2wqbnr4Rh4wpLwtu6h50IBrmfvbs623i0zqP8csCd29jsp2KHsf3XN_yCjT7LHKVM5eVtxGxJdBTTX3Mq88izNe0xZWpKpTDhKxbkU9qe6AFqX33erP-wh4PPp_IQu_PgTd7-nxjlkI3_x0Z0CZPRH6B_wJRcw50twa3whNPwQ1rpDF3IaKh45Efme3dPLmrzzfVXFDvar95UPql_Xg1NHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5BUkmqrRa0MpGi5ErXFKI-wILaVTYNDACrYEzty5lLiIfhJ28SgufF_b0M21RRnsrAM3lm5ZXFziEYt0wakRTbOyhjd3cHDZ8HtfB4VVndnDijytM9DZnpXjkfZ3UZczy3WeQsxDHah8z-20Gi61rDnKBVrjuPTNVqPgWDiWDdSrp8eam1SDkn9It56TYRWe2EhfpCuM_2Al4MMglpBMn5Mxp8lF9cm4dyuKza_KmPlZ8FhQMPLFP3X1hAoDIgJ-xwoAt1htOvI6FKgAQ0U_l0zmKyRjfEU3dHoauQkLoagCDLHW8Wg8U1qpwOS1njgQdxN6PqC0tLsQ7ZRWeNJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=Ej2QSbgIz5LVRgKDjA_ePPkYJBUGCDaemCp4JQG0SJAVwfengGM2Ohlfw9-Idm7V5g4rUy8UTB5_U5t6ME0rw-HPUKh6_H7kCDLKVN7fKaC7WZMPLN6hdR927UW-OHJsSOxPprVIbIXnFJx-Vvr92zZFcZJpGQ8JnEZEvHP21VKY_PTQFD8AEQGvk4-BvsKjexCSkGi-Rtpx-XsjcD6dJlHqDT-hHFfVasLK8oqbpr3xk8pV4vMEub5-EqzapumbC5b9HY-Q2bhFJLKufu2vnG01JFpHaV6rh5MEhgIb3KxGV-dlksu7tXwKA3RsKkfC8sCxSqoX9y7e6oL1IZ4VpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=Ej2QSbgIz5LVRgKDjA_ePPkYJBUGCDaemCp4JQG0SJAVwfengGM2Ohlfw9-Idm7V5g4rUy8UTB5_U5t6ME0rw-HPUKh6_H7kCDLKVN7fKaC7WZMPLN6hdR927UW-OHJsSOxPprVIbIXnFJx-Vvr92zZFcZJpGQ8JnEZEvHP21VKY_PTQFD8AEQGvk4-BvsKjexCSkGi-Rtpx-XsjcD6dJlHqDT-hHFfVasLK8oqbpr3xk8pV4vMEub5-EqzapumbC5b9HY-Q2bhFJLKufu2vnG01JFpHaV6rh5MEhgIb3KxGV-dlksu7tXwKA3RsKkfC8sCxSqoX9y7e6oL1IZ4VpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czrVqqFWjtdfPIgvGzUiYT2jcyD1s5TLFmmPkm42TnjfI3rs6JajebJzsPcpC-zVl_8vnxNqhhuUGTYZccnRuxDnuDRpqxNSm8DVj_Q0zS2IfnEJDTRDr8r1w74QTvxQ3s81LnAhO0EO_EYzbcwRjdDFzN7AeXJMEcyk3xbeHUspQYy7YJ664jEmAAluQxm7wl8hGLIcHVkZnfZFxjzjifkuIpQeXJZ_sjvEuCWbVV07cmxd9o-hO3djJz32czoa15uf0qq-kvbZu7lRjTP81GQY8KQD_9wsX-msG_pM13irT1zFJHpos57jbc6Spqr7Uw0ls5nn-VoDE3VFJdzL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=o0hf31UDR4vAvJi8fWk4DKLiOirMAlhmlS-Apq87P_6q_W6JatOfbv08I3i7d2l4wcq7l-jJ4iZ3nEJY5Ity_nQuNyv3lCzr7uDERsUS2LfaESZ4TxdV6Pt73pRKec4GCGpr84mr_Zj1BYO2PxvaupWGpGmkmXRVabUGWvCfXUf-3ri8xYPn2L_AGNWHsFCHsBrcR2Vtnfxqv14DeDQ3xBuJT6vMsesN8OCfOY5uelGpF16hC9DZ7FC2DS6Z-33JnRo2afu3cqhoWj3jycEv7eGQ6kEU-gqmydCtRVADugdrxA73dgfy5mYcklJLIuqFcHDw5mdXJHbCcBDFA19c_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=o0hf31UDR4vAvJi8fWk4DKLiOirMAlhmlS-Apq87P_6q_W6JatOfbv08I3i7d2l4wcq7l-jJ4iZ3nEJY5Ity_nQuNyv3lCzr7uDERsUS2LfaESZ4TxdV6Pt73pRKec4GCGpr84mr_Zj1BYO2PxvaupWGpGmkmXRVabUGWvCfXUf-3ri8xYPn2L_AGNWHsFCHsBrcR2Vtnfxqv14DeDQ3xBuJT6vMsesN8OCfOY5uelGpF16hC9DZ7FC2DS6Z-33JnRo2afu3cqhoWj3jycEv7eGQ6kEU-gqmydCtRVADugdrxA73dgfy5mYcklJLIuqFcHDw5mdXJHbCcBDFA19c_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=axBO2XWuaCc8uJ1rkPCrz8s_6Yo1TVdnQWZofAQIpAv7PLv9-fzqKGda0HcQ2yyvzcd53FLDbe_RBbtu2gHO4j6Yz6y8gFLtuI13YddLgmxzwv5Ut5uENZ9fNEHtStj97aBz3pIX5EZCyOdWouPwbHinzvA3y-Fr62UQhCA7gJmGTQL6FiBUUs-_Ugl8iT9G3ehTKJGsvMp_yNEkXiQIQ-A-1JU0sfUWtf9gknRMh77DS6MzW3afgFbrb8LIKqFOccGYvy3xmDgOqG08qSl4u74JsZZEWQgvJeZ6jZaUqgvwkp0-1OF0_Tc1vSQXtyP3NiSHbRkmdwGF76nLaj49Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=axBO2XWuaCc8uJ1rkPCrz8s_6Yo1TVdnQWZofAQIpAv7PLv9-fzqKGda0HcQ2yyvzcd53FLDbe_RBbtu2gHO4j6Yz6y8gFLtuI13YddLgmxzwv5Ut5uENZ9fNEHtStj97aBz3pIX5EZCyOdWouPwbHinzvA3y-Fr62UQhCA7gJmGTQL6FiBUUs-_Ugl8iT9G3ehTKJGsvMp_yNEkXiQIQ-A-1JU0sfUWtf9gknRMh77DS6MzW3afgFbrb8LIKqFOccGYvy3xmDgOqG08qSl4u74JsZZEWQgvJeZ6jZaUqgvwkp0-1OF0_Tc1vSQXtyP3NiSHbRkmdwGF76nLaj49Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZNIaNZz0Oy6Lm9J6RG6BdrpZiRj5dD1OBhv766NuxrZKYvBWbcR4Nn7TOZIXz5yusN3Wvr3s3rYY_al4h1kQtitZvIJ5vonjj24XYBBVKFSEOdOmJCJFmmG6TXVBRbeUqFW0w8CVTktKgmrYz6NBe7cLO4Zj7FAtaw_HFviIf7e9KM0M2VSmK8avbf061BeDV49m1j854gIw0ca1QTSoOgE_f1S-GBOu56YEExnqo-iGk7-4N_XUKxPV7UxSXV7mRjDoGACS2pbZsp-uooFFSijSa-SDgdAqIuCSWvzC4NxRKRHrYlmsDu6dbOVv98pkGsQlptRwmbz5nmxkUB-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=EvQviiwLYyrcCnQo9vHoap3M-JxbXaflgzuHYSGD3okdv9WEe0GMF5CCFgGm3zDSven8sTMgoKH8diKXxp7RrhI9MzFdLNLooFO7HP8FE1Woh9KQqgLLa6Lh1sadkMz4073BI0tnOrJRt0fSNLEHT_pELU6AC82-sVKpAS-5F38rcCUDqCrgEmi_mDH9xHthCyV-Rm2ZwYiXSfRkdIKv2vwmw9XZ16bZ4jBZqXCdPNzk95nyIk_baDraoRzsHR3A3ZhR6Pqh3Ju93C71cGMJ5fbbn7F7Cv-PTiOtvFxaYCoc6CDdmV8-crrZ8cOF5Cd-qRIQP_Xhq9_gE4zqkwHibw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=EvQviiwLYyrcCnQo9vHoap3M-JxbXaflgzuHYSGD3okdv9WEe0GMF5CCFgGm3zDSven8sTMgoKH8diKXxp7RrhI9MzFdLNLooFO7HP8FE1Woh9KQqgLLa6Lh1sadkMz4073BI0tnOrJRt0fSNLEHT_pELU6AC82-sVKpAS-5F38rcCUDqCrgEmi_mDH9xHthCyV-Rm2ZwYiXSfRkdIKv2vwmw9XZ16bZ4jBZqXCdPNzk95nyIk_baDraoRzsHR3A3ZhR6Pqh3Ju93C71cGMJ5fbbn7F7Cv-PTiOtvFxaYCoc6CDdmV8-crrZ8cOF5Cd-qRIQP_Xhq9_gE4zqkwHibw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3yQ7XtVXpBvkmeDcTOFyH5PfQV0AssujPWtZh23kdLPX4x-4GBNywM38bNm8GqdarAlz9V-fAzJnSHw0-ksy3FzsjA-1M5vhXg0rWJk0hUi0LjZVewXN3Lk5ETo3lI_XSrhymrOhjlBp-iSB2v6JO_oekxWrSwyx6JTF-1-oSLH25ap2w4dh1AB8JeEQwACp19WXTflxj3KXKdvq80L7f9MLYTCVzWn3cKJrgUsgGVoajn17IOwCjaMympw3jB5_SITOJyJzQCDJQer0aY_l6RwIiaeRwpI9xCgV0ZbCggGxBNekZ6lm8hOht-xx5P_Y4t1ETMFqvYkbMImo_Au-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmat-vP5wuYLrGF0sYu6pIHLvpjwhYEyKYC1vlYTzOvgrAHfwfdS0RCpFOdzCzxlQExiIbM0E38A0BLkMIjbNf6kVZ8nZU4ZGUf_qacp6IkZrfk_ruQ720aK6-Bu5_7lOtyYAryJD71iUNh1zB7hFgFzjh766edTR2f1iZ2UWEqpZVzsITwMFWUFDAOEzDC9HBaCp_3KtYEf_1bDbvMWebFX90I2OPqsnXThNIgawmzA0ngmDF1fDLNYm3v1nRGY1-yWK3gY8GIwY4xKiJ3viMMTob_2zKsmC-QNOEX_Zw5v11CuSFvvF5fyX3YupmwiVq3tdHHhrdxsuNyU9cGHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=sWg6SKkDTU1282XmqH70yNOH9hTnRyUe_Nmype0a5ZIQwfj7HQtdSMtuP3GPQeAGWPf9KXJJ9XqM0vkPl7E_xLEtmQSqOqrb1X52n5WxuPL_Vpk8vR7T96Mg_496eqqACWSmQ8_AYLwIPa1zLQKr7c8O-D24bF3qx949MwxmEzn8LPAVGYFavS9FWcu_CUThxrVHS3eZZETBmd8Q4mG8kBFlEvVN9QwndNjgk4GIEcuZMIkjnWaEwsRbknU_OO7jAXlSzVtBt6_ezY8-HzL1sJwQxVs9EmmocPTPE8rwaJvVmS4bxhC-nAJrdKcHoSo42bkSEDvouxw64nYenzNcaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=sWg6SKkDTU1282XmqH70yNOH9hTnRyUe_Nmype0a5ZIQwfj7HQtdSMtuP3GPQeAGWPf9KXJJ9XqM0vkPl7E_xLEtmQSqOqrb1X52n5WxuPL_Vpk8vR7T96Mg_496eqqACWSmQ8_AYLwIPa1zLQKr7c8O-D24bF3qx949MwxmEzn8LPAVGYFavS9FWcu_CUThxrVHS3eZZETBmd8Q4mG8kBFlEvVN9QwndNjgk4GIEcuZMIkjnWaEwsRbknU_OO7jAXlSzVtBt6_ezY8-HzL1sJwQxVs9EmmocPTPE8rwaJvVmS4bxhC-nAJrdKcHoSo42bkSEDvouxw64nYenzNcaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7msnE8Zq92XwNUsioGM4Cpf5UalClAf6ptIt3rwciBtSSJm1ZAP-kVXbEgswpJa2f_-M5qnTfVRqwBKG_sxDJv70h1aoyh0VNxqPwH2A5ib1ryfLNTSQNkrB5S9aUtTs2NmuMhvZhvaXDn_NVhTsqcORLNNeu0NRapUabyiaJ_srwaeparuk_niXRnK26LUlAZSJASN-b5XGxnJvKQF9RiJ_FwuEteiNVvFtZSAVxxiKpPHWyCE_TlaUZDgzrNWuc1VV-fuTx_Trpj3T-dcDuVjx2eSmcEKP_wkGWjCos9aUd4icU8UaTxGzfsNnyFAh1HTt2NUMjMXgFF2xTueZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roI9Mp1xDaTtkwG-EolI2A5Noy7Lq9yDamMxxyMX8CmYxGp3TkYk0ld1DS2Nbbw-DYU-7aVBf5slD-UZ7wafFCNF3Y28s0k1u8eJU2GVhETxb2ONm-bjCB6nJOj77R2UMEkxXzXCLbB-Xab7Dw1F8kUp5Mm7gCBGwyOjXmNcC9ngZkuCHGXwi_TolETk5-7vJdKvrvtYV0uKu5p1aJ1fImVFXZMsxCX3c3oKHG-9aN1JMK7eHH6YYAsxcxrCzztty6e7yC4Ytik4z4Xey-OjLlw2IwjiXDl1ZEI-7M1Dv2X2931FWOnZl3YQJi1aa2Npkz4ufDmV_ddIYSzWb-rtvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=gsqfXvmB4a44xxCultfOhKfUCd6Fqpj9fHaLBt3DXxGtYhTThPplWAxtCNoPTRssLOjc44Dv1TZ7UY2irZ-bhMJIUhVGly9TOX2f89HpQUUExZenSBmoCvWhcePuUZYQEz5sABYjgFBXoNF_CErD5ES-1HNgLdhjPoR2TTp70kVcyNKuCIXGZIAESInip5GmX157C-L_UntIhjhe5T2LLmbQch0U5bWoXJq-Rsv2NUVv_B-_ztlAo1YpAoLZpIp17ISfD_VTVVm9x4llrI8edUSvVkxInyJT2I4XnYPIef4uwg7IAcuu7H3FNo0AoYy7Bm7hNPCTxLockbCZsEBh4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=gsqfXvmB4a44xxCultfOhKfUCd6Fqpj9fHaLBt3DXxGtYhTThPplWAxtCNoPTRssLOjc44Dv1TZ7UY2irZ-bhMJIUhVGly9TOX2f89HpQUUExZenSBmoCvWhcePuUZYQEz5sABYjgFBXoNF_CErD5ES-1HNgLdhjPoR2TTp70kVcyNKuCIXGZIAESInip5GmX157C-L_UntIhjhe5T2LLmbQch0U5bWoXJq-Rsv2NUVv_B-_ztlAo1YpAoLZpIp17ISfD_VTVVm9x4llrI8edUSvVkxInyJT2I4XnYPIef4uwg7IAcuu7H3FNo0AoYy7Bm7hNPCTxLockbCZsEBh4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=iT6pOalokYG7vf4m_FfjHxxI5-QrsDpkHoMD45_0zVqbvrU1q0p9-S2ea3ZkhSLfR2WZ5dLfo18jPg_e0Mn4_OypI76hpUbLPVJWgghS41Ax9xBW0Iyo-r0CH53kjzti_H-i-HhZ5XgT4T7pEwFPbL5aLoA0bCWUAQRfkMNw1Iv8Nxm1oklLBckrUmWIzNSia4Ym9BQWi92dskx7bKGUHTW6T-8hs0Zwl6hvjH0-rz2JxwWP5UVMqtxymLPzaWhbzu7tCA_nkvTa1PqfvEI7PpmBLtJKSivy6uU2gutyWtDiSDsiWt-1e04kUBOffTB-B7AROUNH0a-68NtGItlNSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=iT6pOalokYG7vf4m_FfjHxxI5-QrsDpkHoMD45_0zVqbvrU1q0p9-S2ea3ZkhSLfR2WZ5dLfo18jPg_e0Mn4_OypI76hpUbLPVJWgghS41Ax9xBW0Iyo-r0CH53kjzti_H-i-HhZ5XgT4T7pEwFPbL5aLoA0bCWUAQRfkMNw1Iv8Nxm1oklLBckrUmWIzNSia4Ym9BQWi92dskx7bKGUHTW6T-8hs0Zwl6hvjH0-rz2JxwWP5UVMqtxymLPzaWhbzu7tCA_nkvTa1PqfvEI7PpmBLtJKSivy6uU2gutyWtDiSDsiWt-1e04kUBOffTB-B7AROUNH0a-68NtGItlNSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2IFGJxXHAGYOyDorjRZSCtsp4y3MMOM2ffSdL03NQfMTk9YGoqtv8fuqGKFJrluCtKdMaehMwVdHBBM4_hLHlH6AmuI_zD_SOvq_tf5dn7n9fosPhpQOgETryqiRlSpfxoxC8evdSJ-DIW2g244zt7VMFmgJlurX-dCvUasLAEDexgKm1e8ApSLU7cQjAF_3pesEGXr_BI2ET5c0r1cZG96MmXqfRdWXk0Sr4Y0qTAqeGKzyYFNNWLQXZnriKN2-KbxCrDQRncKAR36yYhwNtmzEcTbM_qKhKWN4SOMnGJoKOlR8sRuEKRPS0iux0uOnjNRjFDp7BAdLjRWnO2q_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=EI_rxo3YA_RtE2Bfm5nNg9F01XJuSUZtA3VIEfU7J1Qx0dOPtOamXgR5xnRQd6mmB2J6I1nc_jYroAEEIfmO5yDrU9DzdbZVkIvAw70A4IcrKAi5Au8FlMuqOXKZaHX8VKZGsO4tzUxDxrYrUVjkW9Bgdr1LcCZoy6ZTeEwSQnnGZ6orcuySMUSZUNaHiUzLHoURUdKkNeG6tTYmh0GRVDsZx1AT0UF4AS8oQ6cYTGWsLB7RHuFI1Ik567Pf-ikmESl-dcUZNLaqYbTbi2WAP5qzZidmc-x-B_g9cUkgOZjeCWwV32j9JJyzBNSM6ZDJ9lbQLWk39rsk8CE0t0gdig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=EI_rxo3YA_RtE2Bfm5nNg9F01XJuSUZtA3VIEfU7J1Qx0dOPtOamXgR5xnRQd6mmB2J6I1nc_jYroAEEIfmO5yDrU9DzdbZVkIvAw70A4IcrKAi5Au8FlMuqOXKZaHX8VKZGsO4tzUxDxrYrUVjkW9Bgdr1LcCZoy6ZTeEwSQnnGZ6orcuySMUSZUNaHiUzLHoURUdKkNeG6tTYmh0GRVDsZx1AT0UF4AS8oQ6cYTGWsLB7RHuFI1Ik567Pf-ikmESl-dcUZNLaqYbTbi2WAP5qzZidmc-x-B_g9cUkgOZjeCWwV32j9JJyzBNSM6ZDJ9lbQLWk39rsk8CE0t0gdig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=egbIiMsKjZBvwNMrGfWSBUK1F-6EuwpatPfU89kyrP0qKMk3uI6j3ke2IAI56_ImTRI2UzBVoabFxu8y9tlJOSeK1mPZ28OMpWz2Trjv05LL9J8HyZys1MuEZuuvIEa2em-2WSk8oBOvjqqhdJG3DmIFPKMSTjZyaXLWGqMJmVh_f7T1oQJCJJroa5YiX0-ucvgXlzMV4yNENfg77zrRl-WbkOC4sEGpfS1RkoFwffys__8gsmaxfw7r4Iy9-e9-gHO9AKCRdNL0M3ilSokjiziNcfezKHovgZfj_LDtRqitf2e5zMrqrhZ9rr9BGJ1PP1rAqOARVrluJyCa8_IK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=egbIiMsKjZBvwNMrGfWSBUK1F-6EuwpatPfU89kyrP0qKMk3uI6j3ke2IAI56_ImTRI2UzBVoabFxu8y9tlJOSeK1mPZ28OMpWz2Trjv05LL9J8HyZys1MuEZuuvIEa2em-2WSk8oBOvjqqhdJG3DmIFPKMSTjZyaXLWGqMJmVh_f7T1oQJCJJroa5YiX0-ucvgXlzMV4yNENfg77zrRl-WbkOC4sEGpfS1RkoFwffys__8gsmaxfw7r4Iy9-e9-gHO9AKCRdNL0M3ilSokjiziNcfezKHovgZfj_LDtRqitf2e5zMrqrhZ9rr9BGJ1PP1rAqOARVrluJyCa8_IK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=mYE1M_Q9RMQ-3lA6jfjQIwUbN2chD5qgB-374SZHEwBtxvYggxsFGbqjugPFjvmOz1msz6Gigy9HSWWxB8EoEpKFaZ9ETIuFDSqr3INeqSqoNNO2HZIo7qU0lC4-MWA-yciUhr4uT6xoLeG0glq2UaIzeya7OeRGzanTFZqEBA1LKm3jF2NjNmrICtrbXFHPblcUaKxj_sZH0pM-Ujm54fFog0g26VAZyniiOzJSvbrlFShPMaoViJD8_hUWZVOZStTYlHWlUct80OoEt-DYc0TJMw7DFA6rAmK_7AZUV4aBZrVmg8v65CAG49_AeZtgojLS1b6BJIySMp-CmrWD8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=mYE1M_Q9RMQ-3lA6jfjQIwUbN2chD5qgB-374SZHEwBtxvYggxsFGbqjugPFjvmOz1msz6Gigy9HSWWxB8EoEpKFaZ9ETIuFDSqr3INeqSqoNNO2HZIo7qU0lC4-MWA-yciUhr4uT6xoLeG0glq2UaIzeya7OeRGzanTFZqEBA1LKm3jF2NjNmrICtrbXFHPblcUaKxj_sZH0pM-Ujm54fFog0g26VAZyniiOzJSvbrlFShPMaoViJD8_hUWZVOZStTYlHWlUct80OoEt-DYc0TJMw7DFA6rAmK_7AZUV4aBZrVmg8v65CAG49_AeZtgojLS1b6BJIySMp-CmrWD8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=mNNcNSk_g_D4afhYK517IJJ9Y-hMD37s3WU_aswwQBUSbN0epB4Uf5Vpty3-IQGj1M9JDfIOkcjWPL7jSTab1wXlbrPBlFwoWVkvZtPTLkE8afbDEbgbXI7el31Bx14l88k5TTe5JD5vNFfBPlMlp9aJhUurvgbT9p8gdJB9p3G0FmGsLYvFN0A1DurHt2n4wA1hVJfrjNd8F67WPDmj2mG6FyzHTiOUOwkF3PWDThEjSrZC1kiqnV4EGD8U64Yy_X6Xb5aZN5D3F4H5bgmnM479uzgfeJl44YeJ8q_JZgf0OKMwvVCzVt2GWBpZfzW2a5-YGGKMu287FgLSlUL9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=mNNcNSk_g_D4afhYK517IJJ9Y-hMD37s3WU_aswwQBUSbN0epB4Uf5Vpty3-IQGj1M9JDfIOkcjWPL7jSTab1wXlbrPBlFwoWVkvZtPTLkE8afbDEbgbXI7el31Bx14l88k5TTe5JD5vNFfBPlMlp9aJhUurvgbT9p8gdJB9p3G0FmGsLYvFN0A1DurHt2n4wA1hVJfrjNd8F67WPDmj2mG6FyzHTiOUOwkF3PWDThEjSrZC1kiqnV4EGD8U64Yy_X6Xb5aZN5D3F4H5bgmnM479uzgfeJl44YeJ8q_JZgf0OKMwvVCzVt2GWBpZfzW2a5-YGGKMu287FgLSlUL9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB_l1EEgtzUYeN3OFVRYtzIHMPWXWbb71WDxXjgvQeJQaBBqoc-VojJa3PvX8GePdvtMXHJrpYZnnAwfHoGNZbsk3_vmdnvsTwnneDeK-6F-p6NmVmRLXhBBEvYTPqfVjHrfFMZkg3lMSM4rUcnDYN-6gFDkaH1vn8TIh0V9sngSTOqKLJGxiTsXMirhy8ycjKjr30xwOX1E-9xqAThKa5uCO2q12Ou0fdysWoGyCw_AZIOUPL_QoNQSYMImJqvBxjG_nXEdOMhDYDgSYSxsHvkOcUhvBzArsggOji0Zyj4J2ix9bGzpRsw5fhyU9q9RS1Y-z4VVMC0aSG1QProDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYGIJOnds559DsHUdW4YIVXihDIslIZwkYMsSOgQSZjjsbfIt1X1sxluVRyzPcQw7s9BPkG3yKosyiyK-JScwTft3dZogn83akuRa3cVCOYIsAlsZ25CqUl6ECMhpje1zMZMSY0OioHz_QibX-CNqbLZoh0vT6bXuUK-tNq_YgdhxhvS-AMJWhHMMRKc0ZmgAex-u0kNwNFsL_mm3jMLyW0jIkvlliaU58OswT6_PSmcSqNlqfyfRSa7npkZfgQIhxej6vkO344sj8DE_AEfJIT8N1qiD6N0vTvsJPe9IUMAcNryRQQWZf8on9D_IAGoTFM8eW8fcjiVzzb8RmBtDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=giwgE5XUMpfkp_o1GDyhZ8q7MU5vk7TjNFTsx5oJgvpj51AKrUyHVeWoLKrbR1_k2vgbSB5xu0BdlTPSVsGKgOFRxWkMU5oyjRL69Zc6xTmfNlmRN7j1KIx0DZHnpmV7HTbPcpSwf-ROXGolCHTPBrrXcsPNYVMihieU7UuC2El26wi8EEHoneCKaeY5lnGs4z9OgWZYXFadfTGkx0Q2pg0_knVHDG6cXmSLp7PWnwb6OIA4_yt7PppS-uKW776Ng71b8ejHsdwIGFwJ46a-1MK75UIWO6wmMMV6PAKC1KhiZxzwyLROpl3KbaL-kkmbhd_NX3tDJBYYvzKjwrhHmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=giwgE5XUMpfkp_o1GDyhZ8q7MU5vk7TjNFTsx5oJgvpj51AKrUyHVeWoLKrbR1_k2vgbSB5xu0BdlTPSVsGKgOFRxWkMU5oyjRL69Zc6xTmfNlmRN7j1KIx0DZHnpmV7HTbPcpSwf-ROXGolCHTPBrrXcsPNYVMihieU7UuC2El26wi8EEHoneCKaeY5lnGs4z9OgWZYXFadfTGkx0Q2pg0_knVHDG6cXmSLp7PWnwb6OIA4_yt7PppS-uKW776Ng71b8ejHsdwIGFwJ46a-1MK75UIWO6wmMMV6PAKC1KhiZxzwyLROpl3KbaL-kkmbhd_NX3tDJBYYvzKjwrhHmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRt5MAncJ4dhSf-Z_tgDZj3vcr09OhDkvLDqfikwQZUQYASQXlxLvhHhxesKJWUziZjRD_UySE-aNPoN6-Xt6H1qFO1W1G9B05bQ5jKFbJUBlYk3QxzsgQZFuA5fbc-X-N1mdIPOFxLhh3EI0A1mhDvStp7S-skffqe7pHH1sDEFgH_rN6ELFazXB-dZJxviw29iVRtHtalNHrr8d0ZPEn8hf5aZnZPivXD-LRXtt9hGPZC_AiaICFGxOdDRkK0hg4NfKFuGZFzgwVN0Ux0Jsb1z83lUlAKeEthuiSDDguVSDMKLvRu2d0vT_umXfrjeBS9d8wWechY-dg09_uhbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnOyyHbIw7Mw7S_mzhi-LisqcKBHokvnesJ1zDGzX-TFn3X3GcsQm8LjFM2NBSg4Etj4bZQl3bzGQNLS5bbVJB9ltkz7EIFC9ddKmrB_ZwdR96TJ2umiVFADSCVoxD4a9uXG76tPJAbAkAsbkoyLX5oPKQgTy4MBKENHLtCKkPKZ4wBgAqQOAVwAjLMsJF79AgLD7JVGzg46HdEY2TeDpzaER08j7eRvvkto5Ti5ny4ceAFHwjkOhdLlIVZbo9I1rGCy-Vs1Q6MEOGKsOaCTGbM74UK14cxXtAQ5CCdx_rq5lPNdpblD5ppYqTsc9R1Z2OuMCP09QyH7WfEi1Xg-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nMqDNTz_dBfhMEZVdpMaNGdhhCgpge0VdNfzj1LEgwPDj7x_rnUpMlyjhiODDjM52xIz35qhuR6D6HuiAGiRy5kQ7Je1YtL7spGoMfMVwQiWrhaONVGKFLuvCkgJfAeEGTyH-UQDWgYrEYoEcFotpHrmSvxGy0kJ5PR4vDHNGbrUDDuVD2_3yMr8LGcLRf2rOoF33eXlwHS0yF2IsROQxhRmL0WzPKIueIgtA_2-4w2L1fbxz4v9SL-9LRX8umprBddUWVzcFZoGdLiSXO6VFp5j0rUINfVNxKmxH2TfEHNcILwoK3HrIIJQN6Kvr7-HfYIdIqGpTuuCbLNDhvMeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZUvPLYSjUAJIMKTdypTc_Dfnrlxp9VoqyI1B4L21aT_07sIbOeTa46dN1Y20-B_bX0v7U42d9aRpmfIrIT0OuDQVf2PL3iOAKKuPGMi7FPY3YANSRT2pl7lGmNfEDNYH5bVvTcUh-JLFpyFFwFpNqJW9dyblhAKLauhXw6FJlNklZWRU7aMK6GptZqpoSp1zDS4mor2o73bLO0FYrA6kltEQ1COB6W7n1EI-SzMAb-E1PCUH7j2stkS7MbflPnwTtSSeTG9X0_IIV1Q3WcPdVv7_9OXPQjCMxRGi3RBi9qJfg2b_sSmmPgDaOpkSzEbOPnb8QtRJyoWMEzOqPXs8MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=b2jta5fGNa171TbTzHf793tTto4CAp2TopX-iW-abm4RVDmHwmBwaXXYGtYKfswTGInZWz3LPi2P60ZFX3vozlU8l0bBI5JAxoLplPTujWL8QKMV91ofHjawIPnbqEbZB-7xKlP_05kUhhfdihOWCE1QMuyW3Fr4Zq0qDyKmligtGs0jSUzRcFgTsGBtcfY6BCilWOlg1r8KCmST9oZjQh08OUFFOqOmrmVlKtVmrFzq4jJoievOR4NVkw7Tw8GOSgRkv7bjPvxJ-UgHE4E4wJD0saffs1SRf_lI0aAB_xXXhz4uJQuXb9gKCnOyhEBDeTzSE4fjepQ--oFCGc4r3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=b2jta5fGNa171TbTzHf793tTto4CAp2TopX-iW-abm4RVDmHwmBwaXXYGtYKfswTGInZWz3LPi2P60ZFX3vozlU8l0bBI5JAxoLplPTujWL8QKMV91ofHjawIPnbqEbZB-7xKlP_05kUhhfdihOWCE1QMuyW3Fr4Zq0qDyKmligtGs0jSUzRcFgTsGBtcfY6BCilWOlg1r8KCmST9oZjQh08OUFFOqOmrmVlKtVmrFzq4jJoievOR4NVkw7Tw8GOSgRkv7bjPvxJ-UgHE4E4wJD0saffs1SRf_lI0aAB_xXXhz4uJQuXb9gKCnOyhEBDeTzSE4fjepQ--oFCGc4r3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QrJHMtI-LMslHVICly_POQsfjJCJlWaHM7aYYKldMPVPTS-tvGvU6JJYH1VBIWCL5_SUjzoJfZOei1XQuyw6KCRfd54RqzkRwJZ3DA6ZjE7zsDrs_UcMa-60RWENJ2_n34RXqrMB1IN2OAYrqCK4sFnu_3bxAxGfOJu6r_4VVXz--ki_QKazd7LiwSxMDuhOYphobgJd6Esx1CUnfrLA13lIj_MrKiPitpjA42JJ2keMAyvPOXGLUVL5VK1t9PYz-RDE8yGHIjHmLvN3VJxkwlo4_tui_EYUlkmhELfl70L3eyMPXaTwXSvp0AEJaEsqdhqLSi-KjwZ38ZgvfUel4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=VXYyZRu2YAXC6y1ubr6mqEUp2a1IxChTm0GWmUkHzuYJ0I8Jd6UslyJS-uXjT_XeMnEa4tnikXLJt27g5RS7LWOKf_Mh7npLxjzb4gb_sIR03XKbF8TrxAO3lqsIKoQ2xtRn_u5ukH34aJbvVJ4g_-WY_KAYfWWR6ApVGdAL0vecrRVFThA0yHDOfTniRdgKVOB2iCWQRxWTGyvtPdhTIc41aiU85AxMQJKWbraApq3hKEC534eON1BPqXi7WN1mECFY-5X4_Le_iSxR2Q5UOEJCVFLHtJKV6rhkXFehIlcI53pPplEfCTZoCFqpuM3L4LoNTSFqGnjP2njBENSlNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=VXYyZRu2YAXC6y1ubr6mqEUp2a1IxChTm0GWmUkHzuYJ0I8Jd6UslyJS-uXjT_XeMnEa4tnikXLJt27g5RS7LWOKf_Mh7npLxjzb4gb_sIR03XKbF8TrxAO3lqsIKoQ2xtRn_u5ukH34aJbvVJ4g_-WY_KAYfWWR6ApVGdAL0vecrRVFThA0yHDOfTniRdgKVOB2iCWQRxWTGyvtPdhTIc41aiU85AxMQJKWbraApq3hKEC534eON1BPqXi7WN1mECFY-5X4_Le_iSxR2Q5UOEJCVFLHtJKV6rhkXFehIlcI53pPplEfCTZoCFqpuM3L4LoNTSFqGnjP2njBENSlNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXrN2CvKbdjSKYkS5Wshj4A-8uEHmhBLhUeKEJsIfrH33_YrYBku7JZNaydDUruWc555ohQRS-4Nt4k1X_GkLJEjkFT_hxib2FlBNhSUXJ1Ujt_F2MtrTaLjJF8i6-TA-kKkpajREiBaw7ckmEOSRE1GUdgUx2LVgMVjsZeRn493MH62uq0HlNuLZhEWMYpeKXSAXw-RAeKSQlsCsuilTNoR8XAxCLklEMpgfFs04aZoOnF78ra1niiIwPW2ThHpqCpd5MQzmV0QHxVo1I4lO-p6Bt4rkVJNIg_LRsx1-yq1bXb6i1DLploF8bFz5MaHT-fsQ4Acu3ropfuGjDjiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsoYgbbu-Hl3tYMtdllq1lgdy1hcfw6C0RBav4qq_RA9w6D5qgcG9AkmdU35PiLGA5QRCIOMbsWbW8ht5aQ10XIAUzSonlXlvo93H-eMw_uKn45TtTIftJ_CbvUncWICBMJCDBdUD-Wbq7qzN0vM-LToaHmH3NSftBBkaAeQBKIH4hVDOiA4pFCV1YIpcKbG5DD35vgaF0nsLEY8OzM2w1rAn27_Vsb1lqOhZ_IySJEGQQ7x3tuyi-_mjMqnA0uVEyzPjcJTxmPdTd-ZN6aDf64dM2AO-y2Dl4cO5-wVIG0dXPyx1VERXeip7CsXNUblQdcW-GK9k-mitrw8vu66RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=bDV7tj_YNrfIvse1E640voXgGapV53xsHDVycEAWkDSSxd3yk_XMbWMfz5kmBjG_6-TD31I5cv_86iUtIv8S7mw8ZJ_rJiU31lHZVkBEqyZ2rbl-ybLhlvRUBf4TNfuERJ2pjypYE5RBW-uZiQHfV2pBWA5HUMBeq2-LtHRkgOhCWXUUqMjz8d8sD2y6MGdF-JfMqRWnb4eUOTy6DMAVuaBjUqqXlL4YExMdlevPCDC3OS6D0oZvA3kbcVgk_IIFdHfKrZhe01ygaHzjsc_Y99VIGVx1zedP0NobURs_sJnDGF3RlxtKSOyCiFAgNGxtgEF8NrdDf-hl2YPBc6jtGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=bDV7tj_YNrfIvse1E640voXgGapV53xsHDVycEAWkDSSxd3yk_XMbWMfz5kmBjG_6-TD31I5cv_86iUtIv8S7mw8ZJ_rJiU31lHZVkBEqyZ2rbl-ybLhlvRUBf4TNfuERJ2pjypYE5RBW-uZiQHfV2pBWA5HUMBeq2-LtHRkgOhCWXUUqMjz8d8sD2y6MGdF-JfMqRWnb4eUOTy6DMAVuaBjUqqXlL4YExMdlevPCDC3OS6D0oZvA3kbcVgk_IIFdHfKrZhe01ygaHzjsc_Y99VIGVx1zedP0NobURs_sJnDGF3RlxtKSOyCiFAgNGxtgEF8NrdDf-hl2YPBc6jtGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDc9DC3xAVK8WIpnndTmM2t0zCKim9mMobcCoIplssOYvErNsECZ4P-T1nJynUbmLVpNah1TRaXc2LLfpn9tED2VaePtZ96lt8581P1pwWJKGYJduLOugblDCJmA4uJH9waQ4yjmboTrlvLK1PQdRD5ay1cA1phAYhkhnjxlpKYdi-2XawO9EbUufGwM5BAMLJcDHL8cAwguXz4h_FLT4rwQW18XwVP1GRP78rRoAy4mqy7pWvxuzPGhfFPhoWqwdcZWEWbCAZlOy4XMZNwPU31dLSY8MEpGoeZphJlDLEntiJ32YlJC5TGxhUngz0GmBv2KTHDCc2GvYt3QL3F8xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=r-u7UiEewo5Ykukm8R1DW9_gToM1ZGrIqsickY_vXVcm54gCCwtKKGrLbHTWNAKFA2RVqjRRvHds6oiJU8R1YXJ0HtF4cViQdMh17xv1AQ1YUkPz_MLCXQKdrTFJPSXhiUtTaYVKYdgrbRFm_5p2eU9D4RlCNT-7BHbHzZ0W5S0Gly36OtslvTDas_vjSY4qu1VB6AMb7ZIRW0UAaRPrcFSqvPQDYO8bDHoOHO6mZtp7098QbME2eCQnFAlFAux40UYPb6jqf1ERVgshSLBMr9ihy1t96miEjmK-l3smY2IAkMVnhypWklnkItQlkFGxwrN331dGnQJhv-ZPPhW-M0dWwe0hck4xSMMbkfop7oRpiVWgTViZFvpfZssXNAH5sO6pE0N5pEZ_j_TIJfIM0xlJ7onPeLZk6VhmH7j0WNh85BvL2V6NL0QcKG_VR-S4BtyOl_KfQoTPSer76z67qVWAHmthvPCGKwm1hA-lP6n6tWDDY1i9CxTF7bJbVgRvId_NMxjT1Yv5bfkeK5_Ciom89jUeyYZ8KCn3JwbTv46NC8IZVtFjbBY4ld9Iw_IEqoE5Zf5jSpL4ikesETLRwP7NqGLBRpVHPL0BS1_UaUr2xLT59w9BzuasT22uiTlDYVhEY9uCRLdh5l1yVa1NPZV1uROwVPu-vctYrpyvYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=r-u7UiEewo5Ykukm8R1DW9_gToM1ZGrIqsickY_vXVcm54gCCwtKKGrLbHTWNAKFA2RVqjRRvHds6oiJU8R1YXJ0HtF4cViQdMh17xv1AQ1YUkPz_MLCXQKdrTFJPSXhiUtTaYVKYdgrbRFm_5p2eU9D4RlCNT-7BHbHzZ0W5S0Gly36OtslvTDas_vjSY4qu1VB6AMb7ZIRW0UAaRPrcFSqvPQDYO8bDHoOHO6mZtp7098QbME2eCQnFAlFAux40UYPb6jqf1ERVgshSLBMr9ihy1t96miEjmK-l3smY2IAkMVnhypWklnkItQlkFGxwrN331dGnQJhv-ZPPhW-M0dWwe0hck4xSMMbkfop7oRpiVWgTViZFvpfZssXNAH5sO6pE0N5pEZ_j_TIJfIM0xlJ7onPeLZk6VhmH7j0WNh85BvL2V6NL0QcKG_VR-S4BtyOl_KfQoTPSer76z67qVWAHmthvPCGKwm1hA-lP6n6tWDDY1i9CxTF7bJbVgRvId_NMxjT1Yv5bfkeK5_Ciom89jUeyYZ8KCn3JwbTv46NC8IZVtFjbBY4ld9Iw_IEqoE5Zf5jSpL4ikesETLRwP7NqGLBRpVHPL0BS1_UaUr2xLT59w9BzuasT22uiTlDYVhEY9uCRLdh5l1yVa1NPZV1uROwVPu-vctYrpyvYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=qeg7-pVgcfjepATm_kO_xrZ7mltXk_1oN95BmKB_WQ4tKJsEAV4hdaJgDn7or79gfqzQdesu-IeLRR3Oe91FQEEQfJtGadEKqAUoYkAAnp668eV1aghbdFUM1x69xaNml6DarQLmp2NEHU5NacFUSpo8BuDWkQEdZkJsRCeDV9fN73F3UeNLiG1dRxkoZCukg7yn2d1Ydb2EKblbi3KtA1Api2lLuosY8Y7GkYxIvZdRLCFuR4odsgoON5o_4wXLxpY4bArfuuz4092BiiYW-NvjZ-t8SIXwFQybNflwzlN5kMgazecLYTWlw6PFf6TUH8anpFElR7IBRUJ9YThGpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=qeg7-pVgcfjepATm_kO_xrZ7mltXk_1oN95BmKB_WQ4tKJsEAV4hdaJgDn7or79gfqzQdesu-IeLRR3Oe91FQEEQfJtGadEKqAUoYkAAnp668eV1aghbdFUM1x69xaNml6DarQLmp2NEHU5NacFUSpo8BuDWkQEdZkJsRCeDV9fN73F3UeNLiG1dRxkoZCukg7yn2d1Ydb2EKblbi3KtA1Api2lLuosY8Y7GkYxIvZdRLCFuR4odsgoON5o_4wXLxpY4bArfuuz4092BiiYW-NvjZ-t8SIXwFQybNflwzlN5kMgazecLYTWlw6PFf6TUH8anpFElR7IBRUJ9YThGpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPXtK5WL5hB8x_6qT9mpqzBw7BckLYd8PJpUbiGsPj_4-u5jon7ksFH4Cp0LPGPq7d_WCA5Q4LdR1blIjQ7l4DuKMAnXp66_jvSFKzc9cUK9gGgUkunXZoXmuEnLicIs7NjjJub7iv7IVxxYDMh0hAm5OLsJlXs-cfKTmaZaM_oMzOpB-vFQaAnA6o_j0cdzR_2DYvfIGxK8TV6q4uZ7EaG_oizJxqY2i5F-RLDCtJaxXFHE1kO3NAXd2OWKZPmnkXh1-fXPzQH19NEAc82rFSM8wGw8Z1QFIeiuwQXOJ-zMc_OEe8pWyw7xIHUcRQuFGOe0bbk38_saMjOjTGZ5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=bnjbTY8PsXVYz2hmWeafR0eJ1ugArEtuVvLsI44C5iS2yjKFyugS3kh-UDu0BLlCv-TqjmyU2BY_abqHalQ12CsJp-hIrTPoEqho4S1z6JDtrJCmjzH22YjsYdsusxkY9ENzEoBRqJN7jdKc8Yzh3Jdh0pCJ8TGOyuZ6BN4LY-onRjc8VzUZY9SCxDvwl6dC_s0rH42aVXoJHIYLHgjQ3zz5YT7WqIXl5sZe3UiU6G0bJBVnoTlYhLoEigzb3CSpT4WE9LJCR5SXGsF8pkeCgoA2Pb7zOaq1KPRug9Mpn8wwSSiBIa9AxOkM5qc-BdY5mH8Pa4DOHREC2V_Qc7vPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=bnjbTY8PsXVYz2hmWeafR0eJ1ugArEtuVvLsI44C5iS2yjKFyugS3kh-UDu0BLlCv-TqjmyU2BY_abqHalQ12CsJp-hIrTPoEqho4S1z6JDtrJCmjzH22YjsYdsusxkY9ENzEoBRqJN7jdKc8Yzh3Jdh0pCJ8TGOyuZ6BN4LY-onRjc8VzUZY9SCxDvwl6dC_s0rH42aVXoJHIYLHgjQ3zz5YT7WqIXl5sZe3UiU6G0bJBVnoTlYhLoEigzb3CSpT4WE9LJCR5SXGsF8pkeCgoA2Pb7zOaq1KPRug9Mpn8wwSSiBIa9AxOkM5qc-BdY5mH8Pa4DOHREC2V_Qc7vPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=eE8hw3r4V705030InC16cAocmS6nPj2F71z-QHyhXfoLhCSPWS7-1vcUKAI8NZxJyKKOhUd3e0UgY24o1avSTRmvcYKUovzlwyGyJFtdFw78pIpHyrqWK73I0TC7as7xWN3qzJ2uZ3D2VgHp_hEo4n3zBtokGPbRv8nkiXIErEtG6G6SG8jin85iwDZ9TdJpPA-D4OARPNbACOUtY5g3Hcd7m4gXesLTJ-vcJGq3DT1-E2LYrbjnIFTcUIssnzWUlXIFVDoJIHAtHKX4eehGrvFbbN4OIZ0eVtJruq4ethF0D2_oe1jLH0tovd7m_hV5PYBhSLma9Gc0BnvDD-DQ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=eE8hw3r4V705030InC16cAocmS6nPj2F71z-QHyhXfoLhCSPWS7-1vcUKAI8NZxJyKKOhUd3e0UgY24o1avSTRmvcYKUovzlwyGyJFtdFw78pIpHyrqWK73I0TC7as7xWN3qzJ2uZ3D2VgHp_hEo4n3zBtokGPbRv8nkiXIErEtG6G6SG8jin85iwDZ9TdJpPA-D4OARPNbACOUtY5g3Hcd7m4gXesLTJ-vcJGq3DT1-E2LYrbjnIFTcUIssnzWUlXIFVDoJIHAtHKX4eehGrvFbbN4OIZ0eVtJruq4ethF0D2_oe1jLH0tovd7m_hV5PYBhSLma9Gc0BnvDD-DQ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ7PozJFK63TqQf2Uim39gSGcyihmVddQSn8tPa4HBbBXkn4UrXgpl_iuod88lT7cmS-4o7Lw0rhsSnqfrffL1vexMHFX7YwGyz7fJpWR0iFIVSBfX-3gLgMuE7V9j2kw2S2wYwHxhEQLP2oAa_nKTrkvhfiVEBZ3uMjaYnrwS56--PgrWye1AR28dLlY-4pXxg-01b3mmFMCDRZ3deb3ujvoo0eqEMPNXzsnn3Ud5y-1gagj1oNOJBIz74xB578KjAh-YLQsijOVtuZ6yRgCVb_f2w267hXO4ZFL_sW6DVBj00vizI0PWbjqWcKGGnX4iTRH92qm-MrAcbOEGgUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=qcqtAuE0ugLGc4v2SBdJRYyxIqj5DmniNyYCwbyEIIKFx_eOFi8DqX99KxuVgw9V6ITcYI05G6zTp6pmo5heE4HcNT1bxDvCXxYmb-trYPShSZHMMT0UahwMRjvjTIoC1hJgpMD-i4a--IeFfGYKCjtaZzIExLiSpD0VE-wAu_6QuICEiUmK_KvcflyoZgZWPdZMMW1R4oIeuQZPnO2G1zECY9-HRmhznYIw2IAfODI2fU_1gKYxUGsv5ZHhtV_beYjLjTb7JNHh-GN_JGFdULeAeZzaJ0KZwKH9oiLxwOhD_fuWqC4EHtVTJBUpryzd0uObSQqvb5rSSe5cASUwIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=qcqtAuE0ugLGc4v2SBdJRYyxIqj5DmniNyYCwbyEIIKFx_eOFi8DqX99KxuVgw9V6ITcYI05G6zTp6pmo5heE4HcNT1bxDvCXxYmb-trYPShSZHMMT0UahwMRjvjTIoC1hJgpMD-i4a--IeFfGYKCjtaZzIExLiSpD0VE-wAu_6QuICEiUmK_KvcflyoZgZWPdZMMW1R4oIeuQZPnO2G1zECY9-HRmhznYIw2IAfODI2fU_1gKYxUGsv5ZHhtV_beYjLjTb7JNHh-GN_JGFdULeAeZzaJ0KZwKH9oiLxwOhD_fuWqC4EHtVTJBUpryzd0uObSQqvb5rSSe5cASUwIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usLxbf_SbiftZrMLHfM7HqmRBrbq_nz3-2W9Pduhv4-8zqNfiLDD3h__piVuwn7hO3JlYnF0f64-7bDbrmay6IDg7Ic3hay10NrF02U2pAiN-CLJ4NXqgl0MipP0W0Krbg4EP0O0kL_uA_UVTpkmROvUvzw4tbXU4MCCRzdg9UFsP9jEzGNcQ_6BiQzOL7IKzU7C4si0700GSRtT-GpNmf5bAcMIJ9r0CBLWlZDD2whW8kZO141DXfIeUpgLteGeRhLQ6c4SJ9Cp16eCucOxYiojMXMLzQ5Ra3NvNkrmwh_n_0-3YOcHDyGQObUgee2G72P8OEOebb6g-vggvrx-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPtUJ-1LpXQR3y5gv241mtCu_BEfZz_se8PTH7KfbAFiwW5MhBw7D0POOyUh3AQ4WXNqlTYOKKpN3XeT_4kQiAdb0VvQPaq8mBqAI5D7DYKbvgh4d9AH4pb_Db-fO-kz5nTmCNAjHdBMNp_uVuS1vl6icLqChcER-9NNjZ0i5djD1MCSn0Ch9qmHmbbP60cR86i8LHyaEHYwHgMGRbjHnewWyH1Kcs7fOmQG_CtBy1BnqTzwrE72Bxi6x8gjCgHx0y_ctIiRPmrhTHQpzpHn5F_tXbaVYg3yHahBMvt05_lxLZLj3VD9fnhmhvCRG3XJ3Iggu9ek_KKeDi-NXU9uoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgPESANpXqO2RBwnCGzr0OO8mpFNxulq2FVcF3iUtBGfgSM4s8nAciJYjilunO-7yhajcOoEYCZ-O0GdXwG47hcfR_vN91ThYWQXFK1lhKvX4-7Vt4B3jhi7CJGaCGAKTTwpZlZJVVdXNyL3ZzIsWQDUZfNIDgtYzYxPccZ5a-6lIN7Kq9Af6p3x9fOXYEaYXR9_8VOXeIxnzx4k2A71werANnxi6r-d-67PpP3XX4vDXpq-sjRWXyt9JaRudr6UIlVmbzDSaEasSKsiE60zXGEdojgPteVFZ6hCrrVe-L57qI5CpvFNqSYwYT8ZGwxbBCa1nBkH_ruufEojoTnHIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCbqCpec78k-1sX95C9sl7WkRg5vRrez5qdfb-DRVFe8HD-By61Go-CmfsMPYPBGerSxugx1uxC0uV5IjsRxR_m9XDJYwaJh3N6tw4evSOcFB_zKi-9HBRk2eZBZCFeUsn7ilgnzR1Sw_jO0j91wsR2k0jAbWnr1s0tvjwBhOLhQItiocV5foGRi-TOEiX6LY3XJQj36EX27QVI7dJMp8b1HaFu8qzHC1VwcBoI7Jq0qP1sRAcBGUEbCOjNKs_1xXEb_XiRAoxuxsfuMFLZv8LMcmi9GK_7tkPjfLXRi2OU7Br_aXJiCrsI9_vmutYQZbwkYZDKuVyVzcSX2XpRJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=f21idjjaJnl5G-W4bH8Imw8clUoBmvmL2og_FFs51Z_OxLTLxukQhGu86fDPextjlxUE8Q_RkmK0qczCeNiYEJAKs5V1QX-lBrKAX91LnJrCfMiKk7xjuZe6sv9qu33ficrRNJrnOn2sycFXh7b0vJwu1AFZFH_A8lzDoR941rwbXuV1yBqsSQrQ0XpKzWQutBFymm3zxMACmGIpEufWOy0aA6RcjXZy441cuXaACAyKSF5l9KV07t6dJ13MR5aF2uA3axsWBgFI_hRUp360brbYuDg1rS1FVJgoxR4WOO7QfgtDA8n9uHZpxfjuPUbduEWw2cNIdYYkEoGKFOFsdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=f21idjjaJnl5G-W4bH8Imw8clUoBmvmL2og_FFs51Z_OxLTLxukQhGu86fDPextjlxUE8Q_RkmK0qczCeNiYEJAKs5V1QX-lBrKAX91LnJrCfMiKk7xjuZe6sv9qu33ficrRNJrnOn2sycFXh7b0vJwu1AFZFH_A8lzDoR941rwbXuV1yBqsSQrQ0XpKzWQutBFymm3zxMACmGIpEufWOy0aA6RcjXZy441cuXaACAyKSF5l9KV07t6dJ13MR5aF2uA3axsWBgFI_hRUp360brbYuDg1rS1FVJgoxR4WOO7QfgtDA8n9uHZpxfjuPUbduEWw2cNIdYYkEoGKFOFsdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kP5EJWElCPgqg6g2CHNa9WaLmqhicp_or4hfgOfRSEZH3U6q9Wivaq1Lvl88Z0mXnxCB4pamWwo5xEOr07ZemYLJBrN6QNz-2fnSfW_nav-jFKla-acMWPM6D1lImMjTPuNX9lKuMmTssUicpC8-70AzPPs8CN8XOhf1vHFaeArS802oZSFN1ZRYTHM9D2pkmg9Kri3_5Y9e3sY6OSBWfSqlcyHt6jJJeJFOhwBzAFB_RTsaTuZYHwajcMZ77ubYf1_8wbASxphVW5fTxN5gtNjykTAporX4RFGmfLMVJ5noV1FsKjpVgL7g2xo2Z0eK3U0ljMpZ6Dw-jkR9jTAT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=ORO_urr-8bhGv4vZiZEaZ00Pt-Vw11UAwv1gZC1kPysho8iJv6BCG24IjH-KRTIgesU0OEZ5q7Ykp5W-jw3q6zkz9R7JNEwt3nuuIZOPt8GhTxRekWAIBa4r4ACmOqUmXK79guVwH_Cjq4GaDwLAEbEBdqnnHGo4L1dLVffLNRluxYc5rdsT91Bq0QdgJOxU-Iy7DD1LZhFNXWiUN3bejfVreRLbgGuzIgcGvT3lZTZ57HngG-s4iAiyn_QEXoVClwJSOUpSnc-MYo0qB8InPRXhGFbtVGXea1yXrf6e7IEqN4uO5VYv3CWa02IQqIeFmSesvf1OuKakP8w3qD1omQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=ORO_urr-8bhGv4vZiZEaZ00Pt-Vw11UAwv1gZC1kPysho8iJv6BCG24IjH-KRTIgesU0OEZ5q7Ykp5W-jw3q6zkz9R7JNEwt3nuuIZOPt8GhTxRekWAIBa4r4ACmOqUmXK79guVwH_Cjq4GaDwLAEbEBdqnnHGo4L1dLVffLNRluxYc5rdsT91Bq0QdgJOxU-Iy7DD1LZhFNXWiUN3bejfVreRLbgGuzIgcGvT3lZTZ57HngG-s4iAiyn_QEXoVClwJSOUpSnc-MYo0qB8InPRXhGFbtVGXea1yXrf6e7IEqN4uO5VYv3CWa02IQqIeFmSesvf1OuKakP8w3qD1omQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-Sx5Qnu6tLo3DaADYOnh9APZUFtXjBCBQjcs4yTwp6Ay3D2xyKF0mSE6l2NMxXbYHCT72OOtHSTEwETAdJDcZlD3mqWkkFIjDBInTYp9HDQWXGDlv3kigmVQv98ftolZp99o1nVO4Ci8WlAIkgv3cW4zzerr1jk2IsDd-klTOS2uTTDa_YqjnnLl96_0itd-okuIc1v6A4h8gbA33qziFQkznbA0z-uIZF09cC9L0ZB6uvRjobVO3gBsXZJQ1ElSgKGlYarmrRCmCOlOX5nUYsKL2B4QI7U_I-9mzgGAhUYDUWa-HeS9XCC_TfP9v9myeXbaqHv63oojexZsb8ZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcfie-d6xHqzR1_FBeTjEwJLI9Q9_g5DTzizKEP0-IS3UlNdsl6lbnSpByDJp4UGQ4Qa0f9LJaPXlQ_oqrtwb1dyAnRH_Febn2bfNyMblVuLz_A-WBfhqXC6OxzPS9Uupsru6776HcwNPbu0oENR6974UC0a0wUHizLDyq0CgIpAfLGZBjRrlsynF1srBPKGAuwwXkTGNmoB7xdkkneEMK5BJtNLjYZL97hHgIngJoJBKmy_t5e8_e9qbfgqi8yUPD0msgILI7AnR6tVGYZw2c1KTCsVfptQ09Dd0ncFioX0gd-mGu2piQMk6X_nHPWsnWx-i_WeqRpAo4i5PO4WRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rFSFku_x4PSmq1ybJjFq3CCk1ujo5EZ25h06DUxy7mOUXsy1p3r4VVybqnKzsAymL6AyNWNPJj3fFNzNRm99F0MurZYRYjdCYLuBp8Xv6lGMzSP6GTzcyP86GtaD9lsqRm9qRcYB3txXBfpWkFaGAoD-j_ZzrYOTPJ3ISOKvPD-RmXaKuNxElbaLjTfgz_GNN9hFpMWcuyCLao_-18NPSN7dl5qOL7Nc6qrJJ-7CYErVzWiLZlzMapkzWyRyHdmXJh2cwA4RunKqdvqRdDWTlmsPn__DyDjfs1WUYkAW7y2HL_mprDNhDOVHJD1ObTsIcIUPKymVn0bqCyHkfF86mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nx4ilaBAgV-nRY8t6-ZbJvTC2iHVjR_Bml_5PTMug9LaLE3EG_iUl1UvrUAIZxGAL34IJl2w2skljiUXo7luGrMeG75LoN_QaFeTMZsbqXZN93AzcCA_nRPDsO4NsoOHnxSlv-cPi4bG_yfD-FEYseNP3Szducvjmr0vSqaOk0OdAcEou-5r2BfFs4PokojTG5o9f3PlmgXG4JjP6mV0h5yqkSwYv_tqSlypojBZPTXVoEyZ3B2nWhHcn-khI9nyKWJfEqVkmJexVF81w_umuleo5rlRKpmdoRSe-cwsH1QWjDTri1npVyLYN-ZP6DZF3Wxk_mNttCyCozpySy3rnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uGHFfcXw_499ddLi9diNSobTtMgqllh85mVz_bSAXlPp3DHkY6LszLoLZ7ukyiCdf0F-cgIL4bhU6LfeqbxGtOIUWeKQY07ZwymZheWAdjuq1PhkrqrJL_fc5VesRLHPsqKk6uSGcOTK8gxavF556nBX_AzKR2pwudQsRGdHKOwj_-NfnVOOsRgQwGFJ1tn44_yuwNfGWDCQas-lJerc7XTsf0y8dvqwq3E2hv7MtF7ZXRSSt5vxtmTdWaHinaEqZl8kXyMhXND7qlwbiXG3qxY_tmxQd2mNpv2HSYW-cgtmo88EEalkc56IVg-YQ4B0NwPQBQ_8yPAoIxrp3CoOJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUZuASPCTXBHfc50m-3FXdC9FluZ2MTBt8aTTA9v9Hyn083TAyAPLCjMW1_BQWP-vsilmJH1y5LQ1mUUCmFW1Z7nOkVOFDdpDVhUYoNGu2zhzS7x6v-3Bo7UocCVsnJpfYseabHXA7RD0epe4QLhIovkXCvNwE7O3jSUhFNUg2MACxWd2JJaG69hJFj6WR22o_I-BdgLmOpI7j4I2N13EYRKU0MlhuWp1kv-qVzYN8_eir9O9Ub0FY1ZgYoaTAWKgyJYpBENDxnVLO4hjP2-UU9s6kcXCW7DBHKvHU5-cPYE27EtYs8m3exT0We5K0IB_0nnmKd-kNX5N8oPF2ookw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEZ2TvLF3f8oXOf40atp-K04Q_MJRHxg_hs1G_9FG9Hj-5-x-1hLbNOVByt9Hamv886YgIR7lfVHg4Ur0PxN3XU6C8Zy6VYfeyruAe7FhVob7HwxH6IhQWoWyhWLryT0tzkfU3WTLP2FSE0rhiQLGr-b7oD9ZjVUVnXb8X2z4R-H2XKYYqrH_yE_dJQD4VAe66Zynfgh7t5z82wxP2f7TbPE44LemRJnwwGFdp2xQUTGDTtFhZJf-XcUWX1DBPMWf4oKnuiy3lghll4VuC18dSJPULxq1dadc98W6oeoWZUIYFpReYFdvOqbGUqR6q9AV4uE372pmZUkbeA1sGhENw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=r0_1ASS6xjMMUI518elp_k8szDXR1MYdfzriCazt-4ZmHZPs--nmWvmLzhS0x3PulhKhh9d3_Fz3TJUmRBP2A8NCs0ayI09yjZIKmaZYEUdd7LQiTbgGBXUzwAK6hU-ojA-zHCFkZUbKA88js0vN5VI4MhKwMaZ-nYF__Uok7OXsnO2q6N4AqOnqiZVvBk4uap5w5d-MImig_H9grNA_ghiDAVJe5xIoD8raRE0TjAQm8Fu7HHXo5dpEE6ZQ5sTCOxqQNaA18GTlD3uRCKB2q9mGK1OIfwfQVo46TGnV-Rv67uhvdAYtSuZmcjmk6CWegyUHadAlswRpfG0sqatsQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=r0_1ASS6xjMMUI518elp_k8szDXR1MYdfzriCazt-4ZmHZPs--nmWvmLzhS0x3PulhKhh9d3_Fz3TJUmRBP2A8NCs0ayI09yjZIKmaZYEUdd7LQiTbgGBXUzwAK6hU-ojA-zHCFkZUbKA88js0vN5VI4MhKwMaZ-nYF__Uok7OXsnO2q6N4AqOnqiZVvBk4uap5w5d-MImig_H9grNA_ghiDAVJe5xIoD8raRE0TjAQm8Fu7HHXo5dpEE6ZQ5sTCOxqQNaA18GTlD3uRCKB2q9mGK1OIfwfQVo46TGnV-Rv67uhvdAYtSuZmcjmk6CWegyUHadAlswRpfG0sqatsQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyYBqp70HM_48KcYu28JzqevnL0cDRd_sDX9Lb6aLDVFCs1ZpltgBxJKNhHX8TEFEGaJUP9qG3vapP5jpkl4ItmtBdfPDqAG-RIvFATcO8XXM5jvFPhJtJVZ7pcIgWyrHSrgo2_NWccnh-nxB5xXigseVl5Ht0eXzwhKOD3fmJ3CKKrmIm5sQ-thMimKyZmue9Q6ZFAFXxHVA8mRlqXatGhG9H2oXHYNMNLZYDt3j7NhoBLFMlp-ECuioN_tZfAbJJsgtwoOgA327AvEwRgDjlYbexGprA_DLgNpDLUZaEDNbsSwliqIvIUAFK82pZVPKlxcB-IEJvJtcJa59ZbdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=P-jwIo55XBOEzrDEXKOHlL-TJ_LUbmPErkYLcRgLd_oXoAiNhACGAZJDYxv5H7bVA6OI-TxbfhZJMLMqqkOX7IY4cz_5Mn9Tq4_2RoNbRqfAsTKkHAfW0b9Vq-rHGHP-5bEwNKUm91WI3_iCXN3DNQ1DuXtzni-9-TJlg9ptn5oR2YJZ8noyTysYWMuFTCLNdWqJz-MxBSOXrxcH34H6cQUOhColyDY9PzI0X-ZzwqMzeyqu8YmrokAGSoAmho9oU7CiR7mxsCZjN1GkIAQZaeMo8cb55XbGADpZZJlSN3cFY1Sw5SDw65Nd3CakSK7SHZFn2AFpeodnGhaiQNdJvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=P-jwIo55XBOEzrDEXKOHlL-TJ_LUbmPErkYLcRgLd_oXoAiNhACGAZJDYxv5H7bVA6OI-TxbfhZJMLMqqkOX7IY4cz_5Mn9Tq4_2RoNbRqfAsTKkHAfW0b9Vq-rHGHP-5bEwNKUm91WI3_iCXN3DNQ1DuXtzni-9-TJlg9ptn5oR2YJZ8noyTysYWMuFTCLNdWqJz-MxBSOXrxcH34H6cQUOhColyDY9PzI0X-ZzwqMzeyqu8YmrokAGSoAmho9oU7CiR7mxsCZjN1GkIAQZaeMo8cb55XbGADpZZJlSN3cFY1Sw5SDw65Nd3CakSK7SHZFn2AFpeodnGhaiQNdJvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=K8qHBGT_YYInjzA3NnPfhKlMkFsaeh1D1RcpjabXleIFI0sSPkV3kcPJosCr8-JaiqQItOBCc3eLJ_o35e-bqFEc6MKHGDLau_VniqfbI1UyUQ-rbqfNH3-cPtPXTy3Scnzy1Yfpp-36c58okHrhO5GY6xJAaumpMFFrxGb7AeoJGoCoq03XE9BaqEtvw4sStmJefYqwVceo4PRJk99pQrf40Y6UFEX9Qb8oJVSHW8UlCNIBl-sHkwEXSudkBIJb8rx4lE5V51qDrsixmxOucuBj0cyFSThcpMUVIpwUh1CfSw200YZS0lMB21_BHFbS-mpzeqoWNQQkNXbGf80Zkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=K8qHBGT_YYInjzA3NnPfhKlMkFsaeh1D1RcpjabXleIFI0sSPkV3kcPJosCr8-JaiqQItOBCc3eLJ_o35e-bqFEc6MKHGDLau_VniqfbI1UyUQ-rbqfNH3-cPtPXTy3Scnzy1Yfpp-36c58okHrhO5GY6xJAaumpMFFrxGb7AeoJGoCoq03XE9BaqEtvw4sStmJefYqwVceo4PRJk99pQrf40Y6UFEX9Qb8oJVSHW8UlCNIBl-sHkwEXSudkBIJb8rx4lE5V51qDrsixmxOucuBj0cyFSThcpMUVIpwUh1CfSw200YZS0lMB21_BHFbS-mpzeqoWNQQkNXbGf80Zkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=WV8-DTzcw-0dFmgEqsEFctbcjqfHca3gsi8KnQYs6A0GsWd30wWyZgr22wiInXy8Q9vjPEStItOxUqDsding9xhOwiOlf_7su_rvIGoS8L0mgx8lpf1Tnj3-1U6bCV1wdgnS-8eZnzBNSuJj3OnrvyzgmfsKOnBWTInY2pqtoMqodjo61JK4MzirItq0rAZbUrmCX9jzTOf_B-5FlxZ2j6X9kXauX-NLvQ6rDxpqsIP8wsJtN0UBz6e8wV1QoTl57DcvcEWBp1GhVV23Z4jNmtutLNVYhLMbVlTwIVy2jkYi82tnaUQb1fIkOKK3RCoVd9399kp-v8bBBxA0VSTIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=WV8-DTzcw-0dFmgEqsEFctbcjqfHca3gsi8KnQYs6A0GsWd30wWyZgr22wiInXy8Q9vjPEStItOxUqDsding9xhOwiOlf_7su_rvIGoS8L0mgx8lpf1Tnj3-1U6bCV1wdgnS-8eZnzBNSuJj3OnrvyzgmfsKOnBWTInY2pqtoMqodjo61JK4MzirItq0rAZbUrmCX9jzTOf_B-5FlxZ2j6X9kXauX-NLvQ6rDxpqsIP8wsJtN0UBz6e8wV1QoTl57DcvcEWBp1GhVV23Z4jNmtutLNVYhLMbVlTwIVy2jkYi82tnaUQb1fIkOKK3RCoVd9399kp-v8bBBxA0VSTIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=b9E-f6Hj1Bgi_GPiu8hV6RCWFtIwhjQmLRWB3hJ6j_ec4d_pv0_WTCshKeK6FCMcH_XIYLXVwJp6Ax1vCTPpWE3_b4Q9FEh9TLswg0T-Xw_D2PZuRZk4A9kfQF068RLjQplqxWrahX_88Zv17rINTN-HEQlP21q41b5AK0s7l1hgF9sBJLS7GcrVKfflj5Ei7NWWboujN1BBkuwL43IIdSTLyeTWbqbzBc9RtrPXTxSLSTjamRfsfsnZ0oQxcbkWVsaqB_BxcMa8C_GSn-buoS60I-wR-aQWqEvmrdaQq6r0ncClM49bQ3Vf2hOjdF5iJI-iBfwcRVBY0o8LY0CKyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=b9E-f6Hj1Bgi_GPiu8hV6RCWFtIwhjQmLRWB3hJ6j_ec4d_pv0_WTCshKeK6FCMcH_XIYLXVwJp6Ax1vCTPpWE3_b4Q9FEh9TLswg0T-Xw_D2PZuRZk4A9kfQF068RLjQplqxWrahX_88Zv17rINTN-HEQlP21q41b5AK0s7l1hgF9sBJLS7GcrVKfflj5Ei7NWWboujN1BBkuwL43IIdSTLyeTWbqbzBc9RtrPXTxSLSTjamRfsfsnZ0oQxcbkWVsaqB_BxcMa8C_GSn-buoS60I-wR-aQWqEvmrdaQq6r0ncClM49bQ3Vf2hOjdF5iJI-iBfwcRVBY0o8LY0CKyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpmBofJyxVfnsKwlyLoi-Ls8KaSnNbZfIVBykEcwX1bKH4aUlG3Hbi387RnB3yoScR7_Ilqo2wnEFJ6Fyv194FY67v9L8k-RX1HuMUU-UBYqYyvW36tMJYCUgXPVzyPzYX9RaOOKI5Y1_mpQFYLura_IxYEjRbY3FrKX8C8Tw8QVQiEhoR9l4DrjSt88lhQ10YdjSQ9OcRTFf4VCqhG8H-9j0FoMgqkUCvTa07SN-oTpPgkFKRA1Ir0jrE4y6kzr4PrKl3jJ_jyk3N6vUnNw-HMezcByMUamTS5nmlDOKiSTAQjQzVHMiqywFzqqOzH3TUjrClpJ3g1tCQSvB4O7oRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9HjpmBofJyxVfnsKwlyLoi-Ls8KaSnNbZfIVBykEcwX1bKH4aUlG3Hbi387RnB3yoScR7_Ilqo2wnEFJ6Fyv194FY67v9L8k-RX1HuMUU-UBYqYyvW36tMJYCUgXPVzyPzYX9RaOOKI5Y1_mpQFYLura_IxYEjRbY3FrKX8C8Tw8QVQiEhoR9l4DrjSt88lhQ10YdjSQ9OcRTFf4VCqhG8H-9j0FoMgqkUCvTa07SN-oTpPgkFKRA1Ir0jrE4y6kzr4PrKl3jJ_jyk3N6vUnNw-HMezcByMUamTS5nmlDOKiSTAQjQzVHMiqywFzqqOzH3TUjrClpJ3g1tCQSvB4O7oRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=uOEIOJb0gS5nL8g4sYzXRIyfX6K_SgUCicXpmnicgzRwVsC7fd8dWpIocKJf7OcCT19qVlVsN1mywAbU-XAMkc3CGHgCC5ypeOUudSq7ci4z122SsIUfexs0H-9Dz6dS4BJSI6cMLlSqEEUX1AwXzVrTWB9VVjXt5aO9HC4MuIYgoXk2q-6hSay6V3RbUQ1sxJZJMH2Nx1kWUxvz71L7YfmW2HmObpFcnSCD4m20sMkc-bc9oMyshucP-Erna0YxycEZHjGoIiQcCOOrcrBymDKaxG186X71N1EUL3f5-H7uOP2-FaURVhz30hA-xuU6j0saiR4GD6TIC7GDJbIz90YWAuQDIVC1SLBnxgPSltQtvhG9LO3d9qb6Nu5CFq_C47fpCGNmztOzXItmpLQ3P8HSMRx0qLoZ6cIrtvUqb6TxAytyRtzQfTGpa2tA2zZRvhWxnSxk2_3xC-0zJmTb5WvKk96trivIT9nfpNQmbjDdBD3mopN2hOi--PnrUpKuIGR2AJon1ha-RH9oN2bsGw_ktzvC9qZr4r1j0Yz4Ir67iXXT06SJoWvE0jVWoN9ixJ8v-tfJ1oDab3BrTaq46_kQQnAg4JDSJuRyBRqUVzMh8H_JJOuitUGaEGozUfp0qngYfa0PnQsipffMfE7LdpS-8V4fMptHK7OKM9QxeyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=uOEIOJb0gS5nL8g4sYzXRIyfX6K_SgUCicXpmnicgzRwVsC7fd8dWpIocKJf7OcCT19qVlVsN1mywAbU-XAMkc3CGHgCC5ypeOUudSq7ci4z122SsIUfexs0H-9Dz6dS4BJSI6cMLlSqEEUX1AwXzVrTWB9VVjXt5aO9HC4MuIYgoXk2q-6hSay6V3RbUQ1sxJZJMH2Nx1kWUxvz71L7YfmW2HmObpFcnSCD4m20sMkc-bc9oMyshucP-Erna0YxycEZHjGoIiQcCOOrcrBymDKaxG186X71N1EUL3f5-H7uOP2-FaURVhz30hA-xuU6j0saiR4GD6TIC7GDJbIz90YWAuQDIVC1SLBnxgPSltQtvhG9LO3d9qb6Nu5CFq_C47fpCGNmztOzXItmpLQ3P8HSMRx0qLoZ6cIrtvUqb6TxAytyRtzQfTGpa2tA2zZRvhWxnSxk2_3xC-0zJmTb5WvKk96trivIT9nfpNQmbjDdBD3mopN2hOi--PnrUpKuIGR2AJon1ha-RH9oN2bsGw_ktzvC9qZr4r1j0Yz4Ir67iXXT06SJoWvE0jVWoN9ixJ8v-tfJ1oDab3BrTaq46_kQQnAg4JDSJuRyBRqUVzMh8H_JJOuitUGaEGozUfp0qngYfa0PnQsipffMfE7LdpS-8V4fMptHK7OKM9QxeyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=ENBXIRDBaWnRcC79XcQ5jnD-mf3YVzGoad0O24Q9TAJx1-c1KNC0xM_fzVBrhuY29QTzBnizhV6Goq5YAEG6OciX4piJuRss5ZhE6FeGYiW2kXq5-Hj8P7jn4hqTe7iHAsqCMvxZ2aQDK3f6lbtoB41sYNIK0FJz7pETbdJTMWdFsIdleSh83TcY0qIPiG9b3YmC2j8BGIm1wH1kWmZ6AOrLRwTOwdDSaCs14G1ZLEjJQ7O4Z72YYJG-NJ2dlRuwvKslMVBxD-j99pHhNj4UAOYdg6EQQ4uwi9AH4-0zGVfUwsvjFf5_eg7QZcNo8pvr9vGt9xdf1YQVHpyp4FWkMTjpFaHykPhj8Pseyby1iNqmt0TXEJdSQki_OiHBxAwKZparlph0wrnE0M8nnrsT8R3XK3hhvghcwVvOLOiAipOVLCZfaRhND6QKnndnt4AQdjqlfIov8oWVwYPVqhFPTqZui71JJhDJYzr8oiARihxyFEvXeS52AIxUauUxLyoLLwzgZ-Hmo_skPdRzxzCDW0OZgI8oeuMpt8zaM3Ijb6vNO9WUrYcMt-Y4vPtx6VgSh-rLjzu8CA2bIRV8fDqenq5C7n_gXoLOVoGi-aHsS43dTjpz_QNkTNn3hbRrLDqtey8GA_1gYf3bN0ZHc85EHB3ArLs3tmFulcTRBuMM62w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=ENBXIRDBaWnRcC79XcQ5jnD-mf3YVzGoad0O24Q9TAJx1-c1KNC0xM_fzVBrhuY29QTzBnizhV6Goq5YAEG6OciX4piJuRss5ZhE6FeGYiW2kXq5-Hj8P7jn4hqTe7iHAsqCMvxZ2aQDK3f6lbtoB41sYNIK0FJz7pETbdJTMWdFsIdleSh83TcY0qIPiG9b3YmC2j8BGIm1wH1kWmZ6AOrLRwTOwdDSaCs14G1ZLEjJQ7O4Z72YYJG-NJ2dlRuwvKslMVBxD-j99pHhNj4UAOYdg6EQQ4uwi9AH4-0zGVfUwsvjFf5_eg7QZcNo8pvr9vGt9xdf1YQVHpyp4FWkMTjpFaHykPhj8Pseyby1iNqmt0TXEJdSQki_OiHBxAwKZparlph0wrnE0M8nnrsT8R3XK3hhvghcwVvOLOiAipOVLCZfaRhND6QKnndnt4AQdjqlfIov8oWVwYPVqhFPTqZui71JJhDJYzr8oiARihxyFEvXeS52AIxUauUxLyoLLwzgZ-Hmo_skPdRzxzCDW0OZgI8oeuMpt8zaM3Ijb6vNO9WUrYcMt-Y4vPtx6VgSh-rLjzu8CA2bIRV8fDqenq5C7n_gXoLOVoGi-aHsS43dTjpz_QNkTNn3hbRrLDqtey8GA_1gYf3bN0ZHc85EHB3ArLs3tmFulcTRBuMM62w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMus327v-fVB8Vih-xf9E6X1Crc6SqtozSNbDE61fiQPkDcKwEdLUnynVk-w98PGHDlyKdYqK1hA0LX2vxwW7FuLLlBVONZCc68KW8zTL6qDXZfSClGX9pIqhbjkfVtUz8VPnMsH1DZMyWDEkpeJ5zs6fAiAAKig_pE9irP9xOByqY14d_J55zoV84e5XCrDhb_d7LJJKhhlDSsucV8UjfMOqXm3S5UQl6bDwo9ENz5Tqr-mj_MTg2yiZV98Mj8qcMV5y2OiXgQgSXbNgaOscQHd2Xf3v65om-iiuD8cBVa2jjfPR17DrOuRjWTAnrtWBSWoYKJ-odfc07aonePzRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtTdrGbtMnK6Rj9lK2pY_i2_8enaivfqNZN5yosfwudC1eklCxIzv0rl1LEWFViL5OxX56gd5Fbj73uccaJD_dHvsjgfUB0iyZBA6RqAM2S8IqwWIcro2iD_HtbTM7543l7gSyymD9sxeE2IAl54hKIOTf9sxOrJkC4u9h1DSJcAYlok8UHtX6H5VIKyf5KBU-RaGjNSGwYpWBl_-zKEbVjsISfdrcysKrDXirozE9sSF153p-bifyi5sACtkt5giXMzcEOYfD8XKPeyM0iqt_TwB0JEd2LUNDUxR0LFd50TKPtOrxlSy4G4pkJ6zN__HYwTkSkggFUWLDZw3BWsKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=uY4yroUQt3LXlZlW-Dz2l81-IiUYbpBOS0_ZNSBtRQQXy66m6vSQC7H1bjSbDZ8iDpvKL7tQVR8yPbyQO4XMWK15HGXU2yAVCK6o0_a3iNaAq15i4F7U56oCTHyGNvPf4dyEsp6aGJemcjGs8aj_q-aKKSnG-pbegSmx_tDwQDdbG9-84V2zzSQzCy_Tto1MpKdrYEjQ9ly1iqLpuLpe3iYyJr9GzCDqBYnnLzgwdfXwBXhxZxCHpPyU3WtJNXIKmeaGcC3Ra79ELpgUlx8-KCbq42rGm5ysJAwZAWex2W_823mz86072U8cHfOqyfNahzF6ufsekoCI2OSAVx-saYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=uY4yroUQt3LXlZlW-Dz2l81-IiUYbpBOS0_ZNSBtRQQXy66m6vSQC7H1bjSbDZ8iDpvKL7tQVR8yPbyQO4XMWK15HGXU2yAVCK6o0_a3iNaAq15i4F7U56oCTHyGNvPf4dyEsp6aGJemcjGs8aj_q-aKKSnG-pbegSmx_tDwQDdbG9-84V2zzSQzCy_Tto1MpKdrYEjQ9ly1iqLpuLpe3iYyJr9GzCDqBYnnLzgwdfXwBXhxZxCHpPyU3WtJNXIKmeaGcC3Ra79ELpgUlx8-KCbq42rGm5ysJAwZAWex2W_823mz86072U8cHfOqyfNahzF6ufsekoCI2OSAVx-saYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=Gy_f2eKLBF7ekjrBP-G3sHxqKoIulGkHbyWUuaBkkUnp1KipSMrqGKje0pRo7ws5iezZCxAzeXXsgkegtb1mj-Ru6AYjfs18Ja-89QejV56Hldh_4ufiQXetCKm3Xy7Imin7HCUOX5lvPNpH5pqRY6U65KsdPtoOWY96_1elhCC9TKQd-SwWK2ULpqw9yJCL1mq4SHxS_dbkKhqftGyFOgRmxQrkQsLi6iEkJAo7rv7PAZp2RQ5fjab7RaMpxSzyyfTJ_1mhfE0I7VtxshuMd2Z1Vy2ULy06xCFu9bCxcCoqzusf4Ng12O4XDVpF8FCAPDRcc3dc3ANNwz3ZEDdSVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=Gy_f2eKLBF7ekjrBP-G3sHxqKoIulGkHbyWUuaBkkUnp1KipSMrqGKje0pRo7ws5iezZCxAzeXXsgkegtb1mj-Ru6AYjfs18Ja-89QejV56Hldh_4ufiQXetCKm3Xy7Imin7HCUOX5lvPNpH5pqRY6U65KsdPtoOWY96_1elhCC9TKQd-SwWK2ULpqw9yJCL1mq4SHxS_dbkKhqftGyFOgRmxQrkQsLi6iEkJAo7rv7PAZp2RQ5fjab7RaMpxSzyyfTJ_1mhfE0I7VtxshuMd2Z1Vy2ULy06xCFu9bCxcCoqzusf4Ng12O4XDVpF8FCAPDRcc3dc3ANNwz3ZEDdSVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/EU5c2yAGjUBlWox8KcvH719BvL-vjFYZQNAhIakn7AAq5HIIESIQ14X3JtrDHabn5MUrZmFP2Ih4jn_OnIUWroAlIA944hM19StBUUC16xcCq83NS9uz3_WV7XJyu-h6_4-I_OSZe1kr0f1H807Rfvo0kyDYGkK_RGEjYDBX14Jj2BM2P1x2dL67EIvzeTQGkeQ-_8ecNBSsISO0HWR3fWAygNbUzppnlKHMqwgKUqihvNsxLUrTeVJwMSyt-mecCY-BsVXdRO9BILqPmEfiGeTvbJSoq5LI_EACeEbdwrCESit2_AUK8B7k05npJKTkPvigpGnytCF7AWsyBdbpGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 317K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 12:39:33</div>
<hr>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvd_VYhXptc6rOMRBFaERu_fG2iTvM7R1mFSGNDrt1ttj7yGai7mPoS62P6k2qz1swxBUPTkiCVvoSiUeE7nZe1StlK_b-JMJH0aNbLhcLm0PnDJQZDiVEYl2ToR5BZSw6dQUd9p275fTlT6w8snfz1E9a4008s0Y9j8dI9C87xdrRZRg9oboTgn5XJx8seVjFvEeqlMH93Ugsk5TeRjzf8qyq46fvWvXVA7fLXDTkXjczz9rC54maXVc0r_AVWQzmzbGR__ThNa01EDBibsHZb79H_LpQBZCLzxqqj3RP0XMqJPWyT_GVFyRU5ZpWg0-Vi7Hatr_cQYoI8hXNr8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V12f2BdpS4D4FkCGuYkAIfXHRJC9WUdjZKHfM1OjuenfhIFNf72freQns5J31A53MrKpTLr8ZIMH8aUEsy6nqH8uBLLNsOPAVOPPpOuCGrRYuP2ik9622Xv6rrOMH2Ei4c2KwKAEjpCIWHN6WWVub7zAPGmChcUQZ3XzUFvTDENKFcyrPlM1BIEIxrnRXc0mbrDuhTnDIqYpCrxIJl19tKVATRLzNyxsjO1ZLsfdw5yoYGflEAeMqmuzSTayNpJZKfPfoWBFtoZS6V_jkld-x8nbRXOm_t4wKaRNZSJeiw9_bv8pgtTb8NFLSeqbT9DTepXb1s2pB-s5HeMMcrGlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thm8BtiyZ1Ud2gxucbnx8coPNxl9DLJlv_zKnLd7KWu-F8k0UWH1ngBm5uVf3wdWg2_eB1EEs7aAjZz7mJ8QzxDwQLFX4rpw6UrpDptLAAedmeuJdefVenTYEa1XtFze-OIUR12Ax__vM1FmclB0vd8v7DU7KlVWhYcC-T9_AJ86nWg2kXzlQRhUqRukh9HNjr9MVSTbSSye04VRnl9tMyOFGXKgrzca2kUI6fgv_GT6X3C2kRJFzKfXjN76uU2DCKgkurQ20WAdrGHES03rMNbpNWIbu-HhnYmaOevWKmiMMu7aQLyxKlyslr8VhGcenckFefHpwXmYJL351pg4gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B41mGB3Kc_RcDu0b0y8ujwIPdm-uIperSWRGY6pWXc7eY7nWQZTvVMfKibLCg6hxJEhwN_AUT4CsQkOBbtccnxeMdYStcn1xs1fr9Ux1A8BVD0hY-Meaa0e6RgChhc342I8uEVEuL1_leirTUINCL6RMdEAmD6AHGwLQ9HiQcEWEOc8C3woT65tMYGuvKBkiwOiREdIrTvQgsxpONY0a687E-kSfSHEDyVwqgS64S1IA3J9t1uinBFg6pRTNKXUKk4eCpr2sihO_OTx79rX_3q4fk73VHBUYTnOLJhjWTk3rsafbPLCTVeFHsRKgQI6coZoAdD-TI_q9WP90mLljxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-gP1YFiFvj0wgAFEXw0aZJNuKCE7hRE-JjTxd0vffue5qz7pqVuf54TzuOiBKoE4p9FBdhAv7aXyCXrIqSou38s5a3hz7KK1jDr5RCtPTIFC4_FlB0fXSHy7gOsS9WIInzugpbc5yA0eoO1L7EIYCedCeuOWrnixDbPCP3KvF524x0rIMyaurcdpzbZk8z12ONbL0q4UAmxxgEkVB1VwzQDk8lDkIE2VUTAVbrwEIDurUUp7wpgqY0nLoX2A4Zy1GjR9vjfhzGbl7Q1KX6lhJCtVLrXO_Z3EAMx45zF8-iUwQU9yTXkb_Jd2XEA95BNX_ncnFLLIkbU63D9HykhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=ruXP6QwfzosqaBYtY1LCeP3wGc9m0qkkffoMYEDmZmKIR-M1GWghX31UkRbCgn_OmKEPtMkqbMaewIg80iZy0ICcSGawkEVEpwzvu5zN4SfRNhip9n6CBxZyg3WD_8itMAWesF1NSu6-UZd6D7MuNF-eWAE41VQ_frwtCZGpkNtESseY7ySkupJO2PB1gsq4BK0Y9LhF74eW06ThfDGb4TuUNMBQvklK2Swu6ivTuLDYI4HJm_B7PIVLfWF_caqT0Du-U4T3km3mcIZlyICFWzewSVg3G-yqn44ofskGcJuBPOyghGXLgDD5__FtIjXQHIeSivW3twGln1FDE9Jo-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=ruXP6QwfzosqaBYtY1LCeP3wGc9m0qkkffoMYEDmZmKIR-M1GWghX31UkRbCgn_OmKEPtMkqbMaewIg80iZy0ICcSGawkEVEpwzvu5zN4SfRNhip9n6CBxZyg3WD_8itMAWesF1NSu6-UZd6D7MuNF-eWAE41VQ_frwtCZGpkNtESseY7ySkupJO2PB1gsq4BK0Y9LhF74eW06ThfDGb4TuUNMBQvklK2Swu6ivTuLDYI4HJm_B7PIVLfWF_caqT0Du-U4T3km3mcIZlyICFWzewSVg3G-yqn44ofskGcJuBPOyghGXLgDD5__FtIjXQHIeSivW3twGln1FDE9Jo-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=E6K0i-nAfZFlhw5NtmrJMa4DO8u5FkkfMsD24r4IDyN3xGgkyp3g2YuyceVCVSGYAht9Icek2HZA0k16ubOk8EAba2ny05L3jaoh1E68Zoo_CwEvpcv5_AVGx20gC8wH_GQE44hF2eOqVjensenRVkbDh-C8ljsCn0LR4c7B1vpvCnZCGPj8Oqd4it-Rli8Bjas4TcAN6ox8y-2wM53RYiyQsE3SDuOv68m9efn9mdVG54GDOIWNBnlZKrJw_ZwbdXvzcCW44tG6OuJwmK0pv1Kp37SFiMGjQ8FMkdJnefJWGflN_dTvkIJEyDthmxkMcKXikf0ql9Z0Mb8uzXh8aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=E6K0i-nAfZFlhw5NtmrJMa4DO8u5FkkfMsD24r4IDyN3xGgkyp3g2YuyceVCVSGYAht9Icek2HZA0k16ubOk8EAba2ny05L3jaoh1E68Zoo_CwEvpcv5_AVGx20gC8wH_GQE44hF2eOqVjensenRVkbDh-C8ljsCn0LR4c7B1vpvCnZCGPj8Oqd4it-Rli8Bjas4TcAN6ox8y-2wM53RYiyQsE3SDuOv68m9efn9mdVG54GDOIWNBnlZKrJw_ZwbdXvzcCW44tG6OuJwmK0pv1Kp37SFiMGjQ8FMkdJnefJWGflN_dTvkIJEyDthmxkMcKXikf0ql9Z0Mb8uzXh8aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cQpxDpGbqnlgkK3Rbxj2Q9dBwnOsoE3-D5JGXFygACicpziCHJ-9N2s6AsKZfEHsOCODzhh0RVdlEO4dplF9x1BSuauqIwBueXVpsyggjdBMjubB3JTeF351mQRuz5HM50t3ZOCEFxT73z2mQZJK-nHIAdnh70FcvP19POxMBD2SgQ-p6EXpyz91VutIb28UxpjJH5feoYsmSvJmz4UlBZEByfe_S0peqfNc93oVtjRrwCd8goYG9-MJq0nYlGluTZwjPEoxG0M2cev6QpcxvG5crMvFPG9yloMrFgvYoqDrCGdQ2WpcnqRjBzdLgNBLQpKvCgnI2fSiN4FYD94bDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود بسایت فیلترشکن خود را خاموش کنید
.
🌐
Link
🔜
MelBet1.net
🌐
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/24445" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_V3YceXbGAM0v0aXqm1KzXLZwW-S7oYD9algK7P6KH79pPTZwBWpF_RLRDFB_kBxuBz33ah7HdogZDBAcDGTsNbI-nnwGFekZQUBfyYzYcOsbdIGJDf0WZP59eibyu0UDMq01bHf2IKwme7vkE7J7u0GSBASKb7mw5_dTlcoR9xV78t-uo4s8NY4-zardFC6AEkt7OUsQqD9EJZwGcG8EixsfIoLMcYNxiR8VhHlpsPW253655gNv7NKUf-h1rEYc9THBOCdW68YA0K_ZuNXHHWguCWOdcVmmwuRKKJY4_i06Wvpv-GF3-uPKVukumNpDroWxvoaGZk9Jiyhsrt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWCPrDrMzlnNd1J7RXDliW_M7dZik636rgxceQ4-6oIipsIHY_mce3g_xYAdiCpb5oN03FmXFAzGSyG_b1smCSSi-Qa42Z2AHCnbv8_kMd0k5q1UvBEpOKlgMxTJaZEdvV3sxM1GH3-huC_SqjXe74pqEs2_J6jx1rxq2zffONTZrKsxSwPOpxU8mFzMweHpa_ETUYTpQds0VCIbNh0pepE0wFRbztzQ6W53rdIHDKwiXmsxNAtLvHroG3i3jCiiCKsqFgbvpu1E8gvsuw7gWsOxdtq3hb8u9-gFvndLb_WMm3qqInps4nRpd_rtqRa4twijk-LMBB51-wbfImgwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=U6z5saCjFHR6glbEuXFmN_o4hi_PjqeDgSDdgQSHPW1lrx20LYoWOqqCWwzdcDQymL0yPjr5WW__Q_6reGHDouCkfZKSxna9cbaIQFRUHDQm9rEuUZFkGKdvwgi3F9xJI8AWSzUa9Z62Ot3vY9QxzxWfieSULoroKnd9TOLxwa5nlh9GJRtAva1KOH9tqhwHSj-f5UPLgbfdrj8F1vjy-GrdooSkhFWKIYcTyfk7-zhaUlTgBGXMNRJP_UOjhKMoC3_Gn7C5M_mP6jK6WkGCRP5ZFx7OQrwe9Wp2OnwGAySBXMxIdz7mo_DtBf40n0nQHYU87oPrwGnbkKUjSGCcVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=U6z5saCjFHR6glbEuXFmN_o4hi_PjqeDgSDdgQSHPW1lrx20LYoWOqqCWwzdcDQymL0yPjr5WW__Q_6reGHDouCkfZKSxna9cbaIQFRUHDQm9rEuUZFkGKdvwgi3F9xJI8AWSzUa9Z62Ot3vY9QxzxWfieSULoroKnd9TOLxwa5nlh9GJRtAva1KOH9tqhwHSj-f5UPLgbfdrj8F1vjy-GrdooSkhFWKIYcTyfk7-zhaUlTgBGXMNRJP_UOjhKMoC3_Gn7C5M_mP6jK6WkGCRP5ZFx7OQrwe9Wp2OnwGAySBXMxIdz7mo_DtBf40n0nQHYU87oPrwGnbkKUjSGCcVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبع سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxXGRvLH8Snbgjd5mgOJVwonQH-f6_harj3PiecHDUsD9UjLLN5yThw3qkuTo9ZSYMKfma8tDPQOGM5YYMlMae4p92A-7mY2O1SSuOcPydKL0X-rl6K1zdM0yzZZY7aRSskwnTkOgNZ6KppQxqf46PuGVVD_4onzv6WHV-gu4Mp25RX6XoiNa4GDObUs258kDVsAP7AF0RXza55OfkNAIF8Ly8pzwrBRCmsngITqlAvE0VjmCF-YjwBrvsemM77cgejGvLZR7OUjMcufdbXhlsf8hw0InPWrvm8mRjsx1vyK1LR6L4fG4weVa2Fep6Ff4-lGC5ggoL7ZRn-8m8jSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXb_BbRGDBn4rTzXVb4XhwKGbe3TqhFfteOl781iitFy8lqLh6Mv06ezOu4KHFQ_tJdiF-1FlVVuwTTkd5MLAe-e9p8hOpOGgo_sNvwmfdirXuXF15t-toTQzG6N_obYkV25QrP4TrHI35Y4CYoaaCSQppkmRcrI2DEIvN55wMs0m-p7ZOzw_dasTcn7Df3sRcsXdgch6d_XIHb73wH12t_rLdUxp9m2CfZvbrqtD7F-gUD_JhdSCHPCNJSiQu3FLz6wzFtPgpNXwpm6f6seDf34CEeUaQY476T3jgCbaRL1iSXJ_ax19Jpp5wQzPw59DXDPF_NdkXi5nz-wY51sNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJJH6goyXjy6R9jZ3yBDy_xo8msXxmaqdexRl7xg3rICQQnCDGiohZblZFIPeN6mYbZ10rqra9Sxrk7RobvZgKbxk4J0xJKg4SxMdy4d27tWTmjmp1Omvcsaf84Vtm5I12c0bJhq1qdlsZ611AShhk3iYIaLJ73q5TRBUfeuXrFbcRwjJntnR8FsGjIF3FynMqyaHOTj0FtDRjJfm7cLMcMONp5HwzreHUe596-YrzZMnjVpTCny1x2yYec-Rlv3bEjtbsMw8JiYrp-5UGVHMb8OXnV4x14Cs4jkWoHwiUPx8xH9LZFM0vMIeYgNvWicTXHe7hB3e7lsJXE7txuBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzbT6Tk2ayTABkq_Wz2sGXnKdTdVY_87WOfL20Ojlqotz6Ar0oaVPqjuIdfNFXVnu6jDfMMkh8bXGTfun0_0xE1dDzq6i9OIDWoaitQWYN2yO7fg_sk06SeHoZ8bj2LSrqx9fJ27L0w1yGa4fVwhM4LK0clv36Fu2yETylR_p1WkdoozNLgOZOz7cQEzwfPSr-rEE4y9JirtMxMzS719Hju4z8L33sS3awE1QHLBvc3yxf8sILuH_S1Va9aMa5Okva-dQcbUUwxSJ_pnbsnSYSjqdCBMhS1FSMuEpeBCri02Rb3J42vxyO-aKW3U_y-vK4qVuORuiHBA0rVIC9D3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeElx7aN0rc5SloSe0hFJlGMVJuSTZmT59GoeUx6THAhJSY7BA_13RXwAi5glW5_YV-Dd-rKvf9xZGrwGcXe-LXofJkp62xtELnSl3L0VYIz2RiBbqPIluCByCwNy7EpWPp4d1DuaU9CSd1ILATJLAl5QyyfdJ7-bNlknMwKUsIMYS-e8zWO4NQVm3CPJ5tPcgu3VNxULHapNkGSeviJmbeUVul2SxB2I6NULIezzBPBZYPZU03PN8pxG4Orsw0kUcyk78q-XIn_2MzqEsjhP0DOsN-uIH24Dl2AqMA1oRjHKifvH6WiNP59ZPPVQo_oYJ0w8zvWFpaFY3pOaV2wAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwTVhMiKYofUrKnlTNb98vPqlSkxNDal1bvrw7u9AUsoWDAzd83MZMIw1VVApbSLyO-o9henudaRbXHeNN0CsYbXxbIpfQMPAALpk9gsCdsQXxc--upwP1ABMB5NL4vmNg7yYmuswFIOrHzK3m03MwmmMxudNYvHLwarwDVEfCopVYhPEZrnpjavLELW8uYDVEGGzkxfefdR-HaxJwd4_qhsV5xV0XdIgqxx0EIMVia_4VaTorvTDHV5lKp44d9L4mBmMa6wgFxKT4s7b3OdPyLxfJTarEs5PR_m7R2sFioyBmyM0ssYLdpeCqRGcNnUg0SFpZMBi9b66hiBU1s_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVjTH4lAS_MZm1ghiMkdw8DKjiWiJVXQ-RnAWYEZ3fn4D0O78WfFUhFHk4A-DEVua70gdD7La9hEhaRV8drZmHjN9U8FoU8zmg36dSL4ToAl6WmjrmSR-zoRFJbJxGUfwuR4SoHXiklBMDkrKOdknJDTJgProBS25jTpkgJV7vrTNH9ZuxZGO8qgyJiOX4LeWciYskw_fI3j_5pcBYENIwsNCGrUH2qnNDLj6rwG8u2WEfXyc7nSjYnvySAi_96KuUQsWh6vSWrdlRxQyjSru2ZqUUta-c3BZ0y5EhEhuYuimdy7xrQEfleFQyz7-x3LFrKdvkFx6dsF7Lo52dSlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1uJw8l4yODDIVpYehAUbLN1YWhVnj42aSVZLBIdsUkXqDzBLwMTOcxjTpTmfKM3Q3W4CL3Nv9iD1_0033dji1e2u3Y_Jh3K_G-X-YvpG3Njb4ryaGF6xIVyzkLgawNbic2c6YeuPg-nfLc3KLDMrUi2HFphWqg-8Ftc412BVrnrwrCQiLrHgL86gPab9zs2F1doRi1MkHrL7i3AeIlg7Uj1djesKydumdxJxAwjvoVk85wyP2Rt-47h9Zh4vgw2Be7Q1qu_-5MI4TvKj1Nvni9sB39Ny-QQ4P7-TvNkbHg0Zxf4U-ZJUlK982OdVivHqMjRiqO3uyKPQaYeirw1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RelPq8vYmQ4NTzaQvBninuixSa0yX9VcNmpn_mxuQdMITFQa9n8oYhidNx_2xLIw02NPXjfEGlCVcvtFcveqLj1FUTyP83QoMiwZdNmWGUpTnbSCscySzEQthfCZ1XoSBz-mOL3NH82szLsf9cJv6I8458qKlr5QI8YmHuSpoXCTvnpqU-sP3ar2uH7P3JKYI5wL0p3B8g6yMRemMTCRJSwI2lAUUQtkcXG7Vja2CBI46KmZx2xe1GmwTb77AhM6jyxWWrisP4AT2y-WAbjXSedZYukJvMRPLPhQg5nFRgi9Op0dQhUxd36WMg9CVQbXW9ik0hZUYpR8yHZ0TLemoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4HVPo3d4IfL61UK2ZeR1l6suOQfc3FVaJi56hjo4jEvDJ21ovvUuK-zpDKSUk69SOiUoHjgELHGzVxofax8L0qFK4jf03c8YPDQsLI_Z7ZZsbmbzNASSEQ4QObu67Zwm_RP2ouGLDyHhoUV7aeV2gfk-KWPrY27ew66_SPOpvrTsvA7cDE0ENPwmn0j0KEzQ4wH_BApNNM7jGV89ttphdHAcHJgKEKgALPWWcA96tsAGKolXNLstyXcW9n50fJjm7EFGSdjCGasnHmFRDJ1QWiCBS11kAGsoKYUUhZyKgt1zwm8ehzgK0BJUTiqXzIr_4MwJXXMWB6DQTapKtyVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEd8Ff4eC6XcCrFX1_oTzfdkdPSYvqpbA8kviTYfhLsrK5oGSXsIhPxfjbg_oEgzQ5r0wub1FpqwdY6ev6EXAH9GQC8UGVtaWyqNkTyQmf_mdV_Ubhh-jZyXA7com58ih-4QyP3N-hk2ZFt9jBddRKgUO3NP-DjDE5X_4ZH6QNe9JOdiSaUMrHJCKxcnUmh9T0N5DeqMLsPjpdW1i0vCYwTLbuwgbqcNHMoIfQFHq8SCZ55vSSKDNoclWh45Xjp6cFK6jMXOcoZIQIO_8djw7dCOJTN6v10j0JOjhVNozFjvkEyx0kGc2azRZFaX38sD18ALvALyTDh8IKxzmoMdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=L9b_biLFgo1tBln0nnlYA-jQYfMTiTfer1AS0W9tNgbR5q9jVIG3PNGsvYqhmPTeauAvKqFciw0aD7O2n_3tvJHLzFbr6w7tXwjMo2UIjGVl5HZhpIxCsOzk4Hyl0CEc66cIs094rvB_mFh488dCn4frCVW1BzjiUFGMh4RGY8h4GgFshySKoNXC1GU9IRrZqjau5S9PqDzVw98p3n3mDzWq_UcBrJ1gK0hWBxpZ2fBO8fwUIUr0WQKhOr3hPpsuAxW_GWigk-MMZxYxx6M7iKZpYgRl9eGfsMry2emLILkTTH2tTms98VVlcBGdxS4q46Irv8bMxh1QQQM7hZXj1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=L9b_biLFgo1tBln0nnlYA-jQYfMTiTfer1AS0W9tNgbR5q9jVIG3PNGsvYqhmPTeauAvKqFciw0aD7O2n_3tvJHLzFbr6w7tXwjMo2UIjGVl5HZhpIxCsOzk4Hyl0CEc66cIs094rvB_mFh488dCn4frCVW1BzjiUFGMh4RGY8h4GgFshySKoNXC1GU9IRrZqjau5S9PqDzVw98p3n3mDzWq_UcBrJ1gK0hWBxpZ2fBO8fwUIUr0WQKhOr3hPpsuAxW_GWigk-MMZxYxx6M7iKZpYgRl9eGfsMry2emLILkTTH2tTms98VVlcBGdxS4q46Irv8bMxh1QQQM7hZXj1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUNMOVAjKJFPpz9CLPzspDZE2TidhB729TLGLqwvsywXuRL0cjcsZ7ybOC7zp2M8W3Dkrp6CMDG9sjtwOBfg-jrqZWhdTX8rlCwjdNRsqZkkByK06bcMS3Q0HDXeeGWdSf-6WNjqO1wUkpjPDA9-E4276-ckSnjiVQKOrQ-EcIU3Q_FN9qoDD626prLxzEr00we2QeLEHAWYVcaDMInofkTCyjv368QImCj9QVhHaSUALwIfzyme-Rk-ySiSh8oUmKs5D0bGJl-ICsGxzJFF2HtKaZNtfoX0S92MR2bRbLoSsTxHLhFINVeug3okZY0kuVTayg1HXSUTbAS64qXG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ایران - مصر | نبرد صعود
دو تمدن بزرگ، دو تاریخ کهن، یک میدان سرنوشت‌ساز…
این فقط یک بازی فوتبال نیست؛ جنگی برای بقا، افتخار و رسیدن به مرحله بعد است.
ایران اگر این بازی را ببرد، صعودش قطعی می‌شود؛ یعنی ۹۰ دقیقه تا یک جشن بزرگ ملی
🇮🇷
🎁
شرط رایگان ورزشی
💰
۲۶ میلیون تومان بونوس
🌍
فعالیت در ۴۹ کشور
📡
رسانه بین‌المللی
📺
پخش زنده بدون سانسور بازی داخل کانال تلگرام
📅
ششم تیر
⏰
ساعت ۶:۳۰ صبح
⚽
ایران vs مصر
صبح زود بیدار می‌شیم، چون بعضی بازی‌ها ارزش نخوابیدن دارن.
ایران برای صعود، ایران برای افتخار، ایران برای تاریخ
❤️
🇮🇷
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24422" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzjtjrlQmDnNjls3-e6K0oc8ViJwjouX-s333Yl_ClDjrICLDIP_UT3SW1JNGSKjlLY-0jz4_YKmvwBeTTZ5UF-rvN7XrHZVtO0NsOmJPjiMvvnGMfPzmOngLuayQPM7MCL8QLUm4Vbhknuwdj9HoXb61siGlbhy4mLDHpApOqub57I5WRdqTYMfGp_mvxVDVbOCBfNbi9zd04FQ_pUsazuN3-p3HmCtefWdyIUXPYpkF3lEVR0V3V3HAq82i-oR9CVOfYHOpsur8G1xzMKgFfAQmHuR5Gzco1zSXnM_hl7m-AoZB3WjNYYC44GvI1P3k7PyjBR-AvtMyU1_MJILMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=ej3AHql7a4p7W8hrNJ1wxDrb1Genq5LRQjbWb7R-gcSv9wPkyBe4JOTd8K8jO2AfuVV0dte0EzTUM7fiOYewUBJcxbfi4VAUNKO6d0YAQ50bWkE-CqyUZACSHus_muMjsxLoRikTzUixecLqoUpqvur_FBChs7qko_fLvjjkmouRUXyq5GWJmICTjUqnced3veibETBLDnIEckoFqDZejozH4OLXhoaTbQuAYF9EjQDXBuI_OzpB_4sSX57CbmvCEBNh6e3af-56WRlfahvQ2cIp3kez4D0jRxy9ROxmT1WrgYhEdU8EWSfNNI6m957j7YK4mAQnnkoGT-CDa0Myog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=ej3AHql7a4p7W8hrNJ1wxDrb1Genq5LRQjbWb7R-gcSv9wPkyBe4JOTd8K8jO2AfuVV0dte0EzTUM7fiOYewUBJcxbfi4VAUNKO6d0YAQ50bWkE-CqyUZACSHus_muMjsxLoRikTzUixecLqoUpqvur_FBChs7qko_fLvjjkmouRUXyq5GWJmICTjUqnced3veibETBLDnIEckoFqDZejozH4OLXhoaTbQuAYF9EjQDXBuI_OzpB_4sSX57CbmvCEBNh6e3af-56WRlfahvQ2cIp3kez4D0jRxy9ROxmT1WrgYhEdU8EWSfNNI6m957j7YK4mAQnnkoGT-CDa0Myog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzomeDuZiv297ONE6q6-HsMqZ4Y3OdTItNwvt9wfNGRMW7Q3Q5vbrRV_QJlKFqH7zNyB4Xq6pcngLxNRCo2tqJ0sa7m3IhYfXCW4vjVK-bHVV6EOqqgY4CmQYBdYvcf1C-O-585VgsMw11mufv6R3pNRbWvquPyCNMfzlF9YPfVBcB-DfZcRMipqTqqZy1XFqAOT35ldan8rx-eghFJVnpMxksgVD0ZfwUXwZl1CVbSkxrDxjSj6iT5z6wF1Dla1CQjQtFf07bNDrg40Zg5NxhGfMegP6SQwDOdTBHstzwkWlnj_AhcqEEJot09UJGk6uQQ1OPuBqExG3UJSpsAitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد چهار بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1DnXo8_ROvbYaLUsrXO9HcFtFhyNJvFfYAip7TYj4ISG-_N6FdF1Mp3Mw-9yNr_7ThxX_9dPd2CvWEbP2eCiPGTAXCMdfOH8ORJCeEEEhwV2eZz2i9erkipxPoi-B_ia71zHJONZVEdJs_wZP6-s8b1VvLgCA4z9Ai0nab7SNtwRf7dkIC2YcAc0ZKNu6YSzTgjYowxNgOb8purfnvRjaKuYwbNPMivJQajBXaxX6LS4VT59mhhv_FV3pdZ-VXa9EakPIEG2iVzdGJZpt6nDVHPlqqRfICB7rx2HrgILjcku20lbRf-wF4RttTPTwaKYXpgB3V1Ava7qhiCfTd82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaimqWgzoEWszjoi3c83Wqk8Ai-8FculBEA60tzDEqS84tUS-xY6GV3u8TEcxF8UjURMeZ5su_1NoYRI2t8b7QxPSDoQnt7iXdAPr6RGvmP4QFLEkvOc3cE7o3WWuN2SHQTwj2o2LfRq6mWK8JLZEzTCaQq0IeWCJRf5kqzcixROadxJjGYcJC6wDZiHXSo49WE3b5HCGHV4sQua1qc2PzTkP0-xFmSi6lsnl3PqVyKcevrF-B5VKkj9fS_lZzpofM96SXNAT8yTNXLKR0WR581jnHMqeoGH_sz0Hee0v1BSQCyT0Tg3_WQz133P1ZIK71Hb3_J1Gpi_o1MMSi4ETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPldQeY7imV9BLF4qFclFd53CPbQFTmDWuJ3YLZpYi_CFoZji2U1G25w3_XO-qLh0N7WFL1-FAuQgpxy4DjCa9-scNNSdrZvwNJUftC4oq_ZNwNUc2TCi4CEMIBWUhPLPuYrLwdgfGTHFKmim76m_8jHHkGXWNs7TVFM-B2FT1l8t6Sn9R9CJU2kDvjptrXmDSqDcDzlPJAg7KYYkHz2ImYEWGDAayBTCws7vOmMYJcQgIHHOB-0TA6YBkOO82M08g1zmLmSHu-xRafsihiDWCvxPWjEdHDj-Ed-UrcQSLVT-XIdvh7U1FbkJ6mBOIcRtFC3pTg3OM2RScoiyX455g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3TtugJiI4DRn1b2w2vrTGqmHxAF3qA65CK9XGWKrWKqh-V28bcwsYKNmQ67uYBhSLi96aqcorUrX8VMfitkecUoRB0drR10_55HC9bmIkq79pGyXwDmNcl-N-J9pvjAXuc8q03YNwkLiIJ8z3QPZ4W9UfkMu-4VZKv_fyJJHV4P8K6FH2FeltBgPJ68eICg-0HkzgTtoG-O1QoVjPAomfdGqwDuxHBcbU2wwR9LU6E9jJ3ywLeFFtGou8R3ToaS8XMCtOTEaLXbWTCp-3C046RorLuZ3VNYEINkRNFnlWDYKmGlwdNJEO3_Z2ZL1tDIhRaC9LGI8CC2_iNhYMNDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDd1Y7vs8bTLfoO6MiUg_0iB8ywqJyj6k-p-as7GWN9yI_h84MFYzmY75CcISRgclAhcRXRsiT4rh2fUuOEQMdHtQ_410lqebZqUBtOilbXZKASJqEbyDS7VhVJc-LW_t04e1kL_w3ohGJMIr5BJPtqR-3l1xcfrPNrvguRhs7vrtz4DTJsN7_gtnpGUpHOIbPlWnzJRTHKCdTzhpJ09pLmIDbX-R71ofa4TP6ycWQaTd5f8WsZ7IIxawCuBVtlpzUBMSvoA3CBmeQCV5ZDcV6YgQHX8swGkthKU1wpSdjzYjUPvn2p61Z6BsTE55tk2IOnlFD8bj-G7BOP8rG9SQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khKSJC-hVW53aWxtw0_QsQEoxonrPXJA1Fyw_S4pVy_HEy8138r4wTYMfgHsujvNuw1_JTozYrVNAmNmXTTaBPgefTQA4IIebDm4xvsFi8IM-mZ71Xh0SSrJQC04tW6Di2k3BQPrhj1uZ_U3h0ew9Y7PTAmOJJcCBbIU_djPaFIxpHOkpHlfmaKLYcUVgCxzyB71N_tLluuX01VTUjBy1U1e8IkwoIlTa7Vm9S1Aw6bUbeFa7OBLG2k4qDWRmOvaeTS1p_kSIajLO7q5vVU8MKs0O0yjhWs92oPK5wEOrLWRZg5-HUJ2tOwCFaa0Xo9IdIRczK0PahgYOw_8ey8kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR19KrBS0voWMfhLFJMoHUtrDuwxSGQsRdyy4eCLUYjurSwLwKk60yd2gUnoICFXVEYGgEFOKGyzHZNVUj-lqttWk1CSI5JjAdDIIURPFrUDBAQ5uLvKWQwiAEivMo0MRqN6xF-74Nh-kYeLxIYMH4U9w4wgFMZout9GGC-uHWms4JVBW_f-JNcmNF0ArN3G8LrpB4NWycpjQhMRM3So2U3BUasKaENi8FeQCk75fkggCyc9HqsD-jQJPaS1BO55v3eB1AKKeWRHIQbKbgYQNSp5nmtBNBIlESdwyLbLtPovOOICM8vZDJVe4CYOMKjUSpMrVINGJoZBGwWaRNb0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد چهار بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_RZXn0mSUSfvmtCbGKLuuxjLsN7M32UO2Xu5RTWyAYzTm6pCO9z7073b4KcAlOM6H0lqHEXshoL-gzddFmM78MNxbCWGOgQ7l9hLW6TlaZTWBIBwlJHDh3fELQaSUDoro6QIaNwXQ44F4ymJcz-8QAKcOWbd6B2F0BTbNBtyzHJ_XDl9hZg09xMdB91K3UUR8te90Ha6RFG-xuWI5QnOrf98WJcvLz35FfH4JX1E-XAr3cGox2ASF9ZnmtKlYzEwmGUb_c4eeGY5y7y61tuNvhyFLD_4IVAZEcWRhbSvH55dpmJ6ciha_raYf8Pv39ur-_UIbZzSMzRy8i9HzMgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5l1yOIpGnMhBhzTBOvAd3-duBRR3zJ-o27Ikl7XACf3DRu2Nu9zr3X35cTYouwFs6f9KdMPkiOS7vmfh8jexCghI40l-adE2E9wFEwjmAOT4gZVX4o34hDP3EIIra0tNYYX7lrPfHsgolfc23LMRQ31PzfVJDzRXxpL1RUuoeGdpXmjKT7GJMVUoJDhXexZGqPOY4U0_5dddIjVQBxL8PR1CShcU-8OmLxC6ouzRtg_KqY1YtDlnaOH_OrXIUX9vS_B5N5GNpQK-oO-sb293XacxhefGcCQDLgQmdUpNjmg7lUgpm3MH5uER6DU2ftkEGYWLa16SPcE98DJXbddnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrghxVjyyvcvDzgUUJRGcoPegUObdojViEYJCuQmhY36QfWe9hf9uAQZidM4fFW-2qplk9Q0IgLWPs4kORwh1-Tm7vTPFt4mqrPwM5jsrAWh4toCeRTcjBzkuZntG56iUDMbv4ZTo4heufmDC25B4455w_8F16HiIqfad22jzx7MT7v8-j5kUZmhBdZ4AfiGFa1R-X-i0oKT92w0HRcve5NuLMS6kuKSskTGGxQ7YvCzHIMwTkI82WrnhgXYWsozzZuNuCAxc0cWEYjvUR3l2ERBRYHW9HAQWX9rwxf861CZD5-ciJdAYAORULAnZ5YJqXYfj21IizufgNgVKVjmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=pDJmbm0QpWyxzCgED9RXQ6GTFqeItIWSlETzLg1Ib6221GR46gpnDu5unkjMye5SjEYdlzecbbpt0M6FQCgrtgfn7poIQyrlRjcN7GuvQdMLG99ZTFTRsOMjCCOkTKhZBTB5lO5R7uDXxtbUtca-hTONLT5VTuitZhr4L_0XjpZUjao3secijbAVXI4pttxScE3fGOYlnV--JA1drJxXwOQJIeZrfrjZJ0bqH0hyitwQjbQsYOQGnF725oCoWSwEuobeIkQGwKCmKOqbKEkqUeqjpAU23Q4WziJunr4bFRTq6QkZBde9sBsC0nZuDffjgesE44sTZBnFZQcOP6gOwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=pDJmbm0QpWyxzCgED9RXQ6GTFqeItIWSlETzLg1Ib6221GR46gpnDu5unkjMye5SjEYdlzecbbpt0M6FQCgrtgfn7poIQyrlRjcN7GuvQdMLG99ZTFTRsOMjCCOkTKhZBTB5lO5R7uDXxtbUtca-hTONLT5VTuitZhr4L_0XjpZUjao3secijbAVXI4pttxScE3fGOYlnV--JA1drJxXwOQJIeZrfrjZJ0bqH0hyitwQjbQsYOQGnF725oCoWSwEuobeIkQGwKCmKOqbKEkqUeqjpAU23Q4WziJunr4bFRTq6QkZBde9sBsC0nZuDffjgesE44sTZBnFZQcOP6gOwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PboKlXenCmH_z-iOtAnAexb3dQEtwkYeig2_qEejQ34kjkF_yYLv2pviOVDApZHFAk-am-O5O6GydTw4s8ft4MXhz-Nn0z5dMHe1TtF68f_0IWzAqRS-ztO6NdX5aVjZXxiHqx7T3PB8KyQ1sdrHOoQDahIVzi_83fMIl1TGjkegSmw8A3S6kl5CbLFPFl_NyIPeUtrAtLt0SD5fnc-mRgGf9ZIH0ql3P4l7SOWw7_Uhp0lbQ05tynNy-6weK9OkAKP-AeqZPkSzPDmGLtH4znpemkfebZUTdKDxGalxUryumeMtqFu-m-yrN4SKsXwVclWbu4UvNtvsMPBOdgJdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=hapZ6bzzmb-EH6SlShrPt3R00MrElc_6HOfs-bNVPp4-JJhnvkQOHEqQ66kDQbY0nSgutwIaWpnu7N-S0wwFcERP1WD8FwziCfDW4jvGbFCDHiu7IB7bh7ZmUAWcftAldFSxEQjY4kOJ7y7N_B4xSGOnf-LLSItFdI4SfAG21E1hRvfnCfy4kpyBd9yIjUiSiKLwnRwnuSDpoFWdt1lOSdjIa43WXb5y5vq3Tv4JPDPDvN1Op_O2dPP51JPSttxvnpmtqkdVNRQceWO_yFoLrT8xitRuLM5p-nZ0t5munBDp6KbIowwmsgLUEFF8jTE3ERRPuvRVJ3TjjZMa-3UcZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=hapZ6bzzmb-EH6SlShrPt3R00MrElc_6HOfs-bNVPp4-JJhnvkQOHEqQ66kDQbY0nSgutwIaWpnu7N-S0wwFcERP1WD8FwziCfDW4jvGbFCDHiu7IB7bh7ZmUAWcftAldFSxEQjY4kOJ7y7N_B4xSGOnf-LLSItFdI4SfAG21E1hRvfnCfy4kpyBd9yIjUiSiKLwnRwnuSDpoFWdt1lOSdjIa43WXb5y5vq3Tv4JPDPDvN1Op_O2dPP51JPSttxvnpmtqkdVNRQceWO_yFoLrT8xitRuLM5p-nZ0t5munBDp6KbIowwmsgLUEFF8jTE3ERRPuvRVJ3TjjZMa-3UcZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=NB6PvQ2mi9OXD5aYnM_Y-45zyD5Z_W8kqNk7Vs2mywcsf0xjIjtQJlRchi-lzzhwcIk6xOFhMzH34tiADfnvn4nWJHWRGoPlSus461Qf9l4RQXZAH_kx7IPsqnUnhGkqeLtdLSNqPMbSrOc1oRQt_2MFvxL2m5omI2B7yXdUW9LGDl2chh4jzyVCSaYfGOICaHO2UKmu7s9pIOVI-FgxNhuJqf8Iu7iu5_SFH6luX0ZauQ5FgriC6RWHNaHovCdyDxFpLlJXHNc4u6OATv4V-jEYGw6xmMhpRjx74CioXr5SXrxDDrILkyBziuP-Wh5GahIP4krHgkBD7e2qelSGeVmS8993ceTIVdxiXCAxIDe2b5F3wU42UTDF193ulQLOCKDjhGUhAGuHIr3jtjGt6vL84AGy7xn-5FByRXgF1H1-FbSyGBfyLpE9_4ENkhEhAdkpFoPcO0UOqMrzqysaTDm_WGQS-CSJsScTce9Jj4m96ne5EXMux2YQq_PDikY_F6selqcYCP2GlI9dpfj-8vUYwQbHADCUBl7kYyxmQYXME83Cc2GAzxoCObBpnd5PIosgcQy-zkaU0f8_NAdGXmeOtr-M4-eINSrMwfmDxJMYanOYTkXSiwiH4pxV7d9v4W7pTIRvd2oDOVD39qtUkNlO4fcJ611bPw3wvgh8OHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=NB6PvQ2mi9OXD5aYnM_Y-45zyD5Z_W8kqNk7Vs2mywcsf0xjIjtQJlRchi-lzzhwcIk6xOFhMzH34tiADfnvn4nWJHWRGoPlSus461Qf9l4RQXZAH_kx7IPsqnUnhGkqeLtdLSNqPMbSrOc1oRQt_2MFvxL2m5omI2B7yXdUW9LGDl2chh4jzyVCSaYfGOICaHO2UKmu7s9pIOVI-FgxNhuJqf8Iu7iu5_SFH6luX0ZauQ5FgriC6RWHNaHovCdyDxFpLlJXHNc4u6OATv4V-jEYGw6xmMhpRjx74CioXr5SXrxDDrILkyBziuP-Wh5GahIP4krHgkBD7e2qelSGeVmS8993ceTIVdxiXCAxIDe2b5F3wU42UTDF193ulQLOCKDjhGUhAGuHIr3jtjGt6vL84AGy7xn-5FByRXgF1H1-FbSyGBfyLpE9_4ENkhEhAdkpFoPcO0UOqMrzqysaTDm_WGQS-CSJsScTce9Jj4m96ne5EXMux2YQq_PDikY_F6selqcYCP2GlI9dpfj-8vUYwQbHADCUBl7kYyxmQYXME83Cc2GAzxoCObBpnd5PIosgcQy-zkaU0f8_NAdGXmeOtr-M4-eINSrMwfmDxJMYanOYTkXSiwiH4pxV7d9v4W7pTIRvd2oDOVD39qtUkNlO4fcJ611bPw3wvgh8OHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=kn-jhp-cyxbgWi8Oj6vDJwRiKvnee6hXyKoeDjQXmx1JVBNAuIm869BU-C2ZOxTXvLZJ7STpEbMh3MDQvEuhWF3GQvL6JAWZn5eK5i6P51ugO2AL5dS2CKULaD2XwGqtM6iuzSO-cM2CaUltSx3jjzFR2fXlUhl_xEOm6H4_RHLyL_Qz4jyzKFppbcyHV0DxRA9OjZ5tpyCN2M_pjnGQgJXN8YtfZi_w8to4rMW9kjR-zT6ISJe0rzLdzO-dI7DCjtpcF8I2lK7UN97N6kq4hjyAdw70LtnN5oI6QZrVJWrU-HrfDLyX0BDHUCFsJt6Gqlvxr0hzMEbNbgBVk5tlww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=kn-jhp-cyxbgWi8Oj6vDJwRiKvnee6hXyKoeDjQXmx1JVBNAuIm869BU-C2ZOxTXvLZJ7STpEbMh3MDQvEuhWF3GQvL6JAWZn5eK5i6P51ugO2AL5dS2CKULaD2XwGqtM6iuzSO-cM2CaUltSx3jjzFR2fXlUhl_xEOm6H4_RHLyL_Qz4jyzKFppbcyHV0DxRA9OjZ5tpyCN2M_pjnGQgJXN8YtfZi_w8to4rMW9kjR-zT6ISJe0rzLdzO-dI7DCjtpcF8I2lK7UN97N6kq4hjyAdw70LtnN5oI6QZrVJWrU-HrfDLyX0BDHUCFsJt6Gqlvxr0hzMEbNbgBVk5tlww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=gmKn3uu3-C8mn9j_0PS-yrXntfSWV4TWlMeDbEJN2t0V_fz4kNN_lxmwslwia1Mn2dZqRWZ1Cv6BQ6Zdh_m7Ke7ix66uN4d6gORhNRnALLcWe99ZcGad4rroVlKP9NULkFb6QJo_957PvbBdRjpJwXSM1zaz7gpjftyngEqzHvlbhkANVnBgNTYZsDmut-wqfgGTqwPFgSSsAeoI7YNLGyARNhRBuaNl2Oou1kqMvliHlauspDTPdS_2g9KYO2rMlKWJWJalOpbYfnz-N0cvzgTby2610Vnd8RoFepkJn0oDgNZYS7AKOjWGvZNBqOVJjJ_WexyeZfk2Rx5-Zkus3kYk_AlUIICdgCALZsUpIyOu7NDthSxaGYJzsxLkCdjbqo6A8lEXp0kY3O8UqpMUxr9H_AbGaIkXLB4N3OXcBKEhY2xnj_iGISQObzZ14c1Mbx6--ZcsiBzL0ouu3ZEnhDLO_2b7pJ5LK3UF3xZ7SEtdcgymAWh64sZp1OoxKl2djuTtfq71hZafMghgyrFSk84zvss6wCpjYhaGYFmzC1TosymfVeIddiOdqN_W__6by_N1p3ao9kYai6-aRsx1dYomieIi9KxgGRsvADZBXzWA4jO--Y_Fg2LO-4wrLiAcNaCYAEzjkkNGh6lc4Sa6oRrFCBSHodJxj6o0FNgXzlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=gmKn3uu3-C8mn9j_0PS-yrXntfSWV4TWlMeDbEJN2t0V_fz4kNN_lxmwslwia1Mn2dZqRWZ1Cv6BQ6Zdh_m7Ke7ix66uN4d6gORhNRnALLcWe99ZcGad4rroVlKP9NULkFb6QJo_957PvbBdRjpJwXSM1zaz7gpjftyngEqzHvlbhkANVnBgNTYZsDmut-wqfgGTqwPFgSSsAeoI7YNLGyARNhRBuaNl2Oou1kqMvliHlauspDTPdS_2g9KYO2rMlKWJWJalOpbYfnz-N0cvzgTby2610Vnd8RoFepkJn0oDgNZYS7AKOjWGvZNBqOVJjJ_WexyeZfk2Rx5-Zkus3kYk_AlUIICdgCALZsUpIyOu7NDthSxaGYJzsxLkCdjbqo6A8lEXp0kY3O8UqpMUxr9H_AbGaIkXLB4N3OXcBKEhY2xnj_iGISQObzZ14c1Mbx6--ZcsiBzL0ouu3ZEnhDLO_2b7pJ5LK3UF3xZ7SEtdcgymAWh64sZp1OoxKl2djuTtfq71hZafMghgyrFSk84zvss6wCpjYhaGYFmzC1TosymfVeIddiOdqN_W__6by_N1p3ao9kYai6-aRsx1dYomieIi9KxgGRsvADZBXzWA4jO--Y_Fg2LO-4wrLiAcNaCYAEzjkkNGh6lc4Sa6oRrFCBSHodJxj6o0FNgXzlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGiLeKPwkzWQ9uUOPlEg5MKUzlxGR5N7QI2jsUvsp4bvdAT6SB3Ryw0sSJ9AR3yvOiYl9wDXyM8Wsqs9KxLgDg3yyB1YEpNYdHJsFjWTQYinVeWMxn--tYW7rU8Z1tiFKsOsJic44pc67gUPYKiu4M_bX771IymwtisuYgYK8g07KAZfcl8W5dyCCM299cRSd9I-9UYJhZPyif12j5tVeZ9LvgwUwTomefpq8avVKZTlGJW9TGoUQCgRie2c5RMRmd3g5_reprLNqinSFWUgxxwaD6Lmj7MjzyPdcZHCuFGirTd4n75PVPR8vjvBHuMfX3bErJUWnKLNH5OSMlrfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=WOWPbRYypYMThxrr4UYT7lzLb1Bqr82VgvASXXVC_yExpfT4VtXnci9TF304w_nK2F1tx7KZiXHmDGn4wgYbRJ4X7C109-jRYCd6DZ80qYubHkhChRbR5Pl8lbF7LyRVdlacax8-ZiiKP9oXzKOC28Xj5svJ1J88R9sbY6Z3BLyvoED0SHBGdmx0LqLpKzchUZc3gaqBCR4d1naw5Yfr3RaZWbIkUyGcSZxVoOv3cponPz3Jp3g5xW9PosxhrsMJ5gTAYnInFn_rvm0o5OwaSidSlJsybzLpup3GAB2RluH5udlfBPagmOOMmS07fYrhs4y9M3F5yh1g9d3tbYmP1yCx7MNSrrj8kCPzd___IjgQ52IQheDIsVBmDGbRww-ofk2yo-U5Y9yBRt1XwF3B-keaekeiMmqiNmVoGjCCY27Q4iZMILNvlAyN782NwtZ87MXpcBxT9d2gbXJkOsEeiEGv-vI5favMfKgdkWMouCwvDFvAkapQV5NESjk03fvDZA1mUhCUSzUyX3X1OpAeNw7uI9kPE1BLOeooUuTixKmhchkihrfAAw8R7AJcdxX9kZBd3wJrthhQzm2KqXyZrTWbS2xqywX2bhotiyefBe2bFvL_jR_Ps253MmAPzfTY63TZkMV4xW4SYI34SB594vMy8GyXZ1BLWSQYTZ68hY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=WOWPbRYypYMThxrr4UYT7lzLb1Bqr82VgvASXXVC_yExpfT4VtXnci9TF304w_nK2F1tx7KZiXHmDGn4wgYbRJ4X7C109-jRYCd6DZ80qYubHkhChRbR5Pl8lbF7LyRVdlacax8-ZiiKP9oXzKOC28Xj5svJ1J88R9sbY6Z3BLyvoED0SHBGdmx0LqLpKzchUZc3gaqBCR4d1naw5Yfr3RaZWbIkUyGcSZxVoOv3cponPz3Jp3g5xW9PosxhrsMJ5gTAYnInFn_rvm0o5OwaSidSlJsybzLpup3GAB2RluH5udlfBPagmOOMmS07fYrhs4y9M3F5yh1g9d3tbYmP1yCx7MNSrrj8kCPzd___IjgQ52IQheDIsVBmDGbRww-ofk2yo-U5Y9yBRt1XwF3B-keaekeiMmqiNmVoGjCCY27Q4iZMILNvlAyN782NwtZ87MXpcBxT9d2gbXJkOsEeiEGv-vI5favMfKgdkWMouCwvDFvAkapQV5NESjk03fvDZA1mUhCUSzUyX3X1OpAeNw7uI9kPE1BLOeooUuTixKmhchkihrfAAw8R7AJcdxX9kZBd3wJrthhQzm2KqXyZrTWbS2xqywX2bhotiyefBe2bFvL_jR_Ps253MmAPzfTY63TZkMV4xW4SYI34SB594vMy8GyXZ1BLWSQYTZ68hY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uan5GjPljwxSWYxX0BY2zGElv1zsf5YEhCN5SGwSlNcwAOj8AQHCkv8wz20Gx5NiQsVsshdj48HQfpeSaiN1UuOfNZsUALo5QRNPAVAl_rNcao5vF5yekR0wS98PRtlsfOTH_dEi__4kKbemB3xomjLVH-e8z3Na8kWHgy_EFJBVzp0EBeVCS-iUOFsVRtV6liRgYG5oCKb0xHx6jmJy2nfMzrIQNyXolS_qlpkCJdIkIPbjylYYVAJVEN84iutWBVOHkh9_aXJ2wwit6SF40VVxTMs18FHkgguJYG5Gf3y6xvXGmlKIFRBQBafe5jTu0XIlzWmQbD2gTNRpbNvVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-RUDcoXnH8pzKil41zqn3N5qvdUdrK2TMZTc0RRlPe37bK_lvSoD8J9_AYj1aBvuR7Wrw6vI6vjcQO6kR2CirdrzaUh1O94xr6hFsDjc__KmmRv9riHWX6YB1uzBpAKg6k8P99Xy_VPuXJqdBH26JKhNq-QbRs5nWqewsv_BzFjZShaD9g6b0G5EPoS4q03jVmYaJiu31UjgyL_jl1yJxbCpUf5eiMQdKDUP4VSl3cBpAtLcY4gAAWynYX7Bre2lWH5hh1X__ZvizAhZZKEbHniFSbm2hllrNQu9857LkD4h9294gA-V5jBd0lWhP5TOWSrbF3EZp4jkXWZOtYfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZxRWrtp7-avJBvdhvem3hd1eC0imTaLiq0tL9uaz903d1BznxXdgtoEKh4ZNX294ggaKCjSGd7JCx5kniED-kp9J9ilVGk_L5JDHT1BpoDsvcfDxre8Bqn_Mn2f7k8pY0TUmLCykDIuNul9GmZGpieSo8NafuN1MNjDcvRzuAHrKyLWa9mKbHArdLHp4--bjguBYbW73hEK_qwaXtiYq3ng4TmqlLyNJuOauUGC4S4Ll1uURkHCV-1xlKWzZds4q7HWjZtRFxJIrO4r0X-uYRmMTNB3RSI0lBsbvOFkEF__DIHNKt9eN4_53jra3xnF3wpdO1Z1Kp9dh81qu-7q2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2wV3ULVbhYfJ0bBYM-jK_DoxO5dc-NwBnEEky_YNzNacZMjGQkODF8I5ubkIp1wUd4g407I5ouZcYazemhXe9dqfQ9trwRulZzCBj4ePUWh-Q3IjAUBYXQf-bgYlFBD5fd4SslOTBrvHcbaVGo3Vsrqw4hdzZXJLoW3fFTnIwOOo5oXi2STAV4XoDUjqQLR5nV-pWJ8d6erFvyNkeg0fia2MNJPINl-J9mTnoRcmuKN9L2l6Ux8nsYwCe6QnYgD0EpYS5_v8oLYniAmByCQDiYdGCVw5hL8Caky9IsqhF-97XPzXDG0iu_KV3htRI1uCITbR3v09F6-m061zkPEnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co2FPdErwdQZ7v8eF7v13oyjGrxq_JWINsII2X3YoRMIucQOsiAlIm5VsnRQ-cL5kZqVFLXQb-5jKNCRbmpvM0uEGf0lZdsM-AFtL__XEeGj3MgH4-GesS65ubKGFzsOX0F9yojXohXYTYEP4U7uigRTBY8S5f0vaXZvnWJz3XIY8_qpflJAwOdlPuGWACwBYBOgOz7JaBvee0M9L_lEiMEbYdpihghm_wjIPj5x1nfh14RcmmSC71E9wkiDBeO2VZXJzfMv-0mE3Ol7t61edzbXvcDZbt0PIVmcdOTIG5-exNc0dsEQwGgay2iF1v161zDvnZXL7NPE4QidK-IWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJx6bHyJn0ythZNiS0_bq8HQHXv5lW4X2lu_plWvAS2nJvN3A6JAOKBndWV63haa481W8ISxU0LBP3Iuyd3c8j6YOmf-sP3iNCed-JukRLsXuecD9zc7ccnR0DaynwcmBdlanK4CKv5lScP9zkYrYSJ2uurLpV3XcM-0p_Z3MwGef4BzzCzIn2MZdCftwQXBvB96EsUkvtJoNOf6PbJfMxabGfHObTstyjHeKD0tAjbbITa-nPd-b-rBMSllv8vIHxxKNafq-1AF3oaOSO8DdJ0Bu3_r3xGGmRAaPM9AQdl8612y31mO9-0u49yesrHfjcrTnwRquryqdTDnqDOe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBnke9OAUBRhPlf6dZZVtPtEiCSX--pueqbfbN2U5kP7691uLs57wXtUurv82z8qCgUMnWUTTq9j6okU9z3PDkgjQe9FTIWuTen1NwnRCx2LBOhKc2ohp0EfqZVV9L5fbgGi6y7vj3VpugXWUPhQQ2wZH88g19wsaQG9IuSnH-J_c0LuRV478biK5KUJ49Ax6cMv3Lpo728qJYxNyvzv_X3ARupaVR8_Q8ZduMYCJEYc6FJ6xKmxQ-BAFcoI7MBzPeTjRTciLtmtoI_fZFwErqM89pwh5R9z4q14I6mGrdFOpgqt8ZL-txMXN5liQxnJP80Q3uXnzs5L5jg-E4-RNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuXO_sHl_1hI6XZhYWEAe4HIM72D7G4jRnPr1chPYYuP7ku3AjqB7Bi-MTggNdlHtoCVMsA9U_UMiBIlH2rSHw8S1OSW5FXIFqGIup7SO0lVqe8JInw68OXD18okc3qzPWTzRKq7wQH7ogq4GCbxfyq7oBWNajwLxpSmc9WkAGuvA8Tl29beQOF_Nexi91dkwelMucU_TCQ7OrzX1DDGnlao0axrRKW2LsbsxG6RRcpMFhOBJ8HVz6gZ91ucdZm_l1mnfoh0yuYv2qokCAqEJlA6vCgCVBAmyDKlCSWg8jihpNEWCxP61uQr6tnCjiHu2GHXuMNGRlkaLwmZ1ii5MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVDYr1qYP2urOOlNYwmQnSvW5nzC4Ts36YT-oH_IBpiX4CHKHas7N8Cdu4u4jvMystrOdumogEPQHFt8H-SmLihJ7sIuu9zO5qsbMz-oA-mC8hhUoizR8CvXwlk8UbBjvITutdtMxhTubkpXjAaHz174zR10zVp1xX56c83NA_PKwiM9CrbjzdafDJq31Lkfkg1x3nNWZUovA03wHk9-UB4R0vuVTo-n3scas9KnKdEjyhuekKrswppnjsXXSU0w1u7gyRfYCsfVgloVYtQYlQ7KpOA2NvMTGMhBxQDVVgLQY3anhHkVBhlL_e9XNwPMeN9XbXDUN1NeL7IkWn8FiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohIyVwV1s2ScsdzGQ9B5tpG4V-itc3qpu88rgaz30qfWMX9phesYX-yqsOydYVMrY6ikmyoqX2eiY6pnnz65h30ZGe_qgQrAC_0q_FFJ31fo9jy1-IVmuGtfD2aMFcxTlzaVb9V9ZZOkzmJAEz2wx1g34qQbXy_EBH4pxLMSEC459E0ifU658EjMub9NC-HCMuoOGt9l1zoUUQ08emXtIa4joOtSU7CPLkJNUq50Kuz-nUKSb3UUIUGSeplzBDzdSBUCk5EzePMzP7uwkFg8rO3h4rybvZePzU-D_7b-y9oUUdqxUUSv9bDcLATfGL8iNqPepDxj-0aXBjEW0_xN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stxqfAWEuU4eao3usK4uLriyDfvGdeNzeggeD-NqPb6CIM07uzJEHE0MgF-sFOPqCDG92mVPf9a9MY9pVABXZPjfILcwkMwY6I4rF2jCbN93ES1UxFUIcC3DalpYW2IpwPwbMipNKcyU2LEnKxzaQY5e4KZUVe_0rxIUYi0ig_8HA4ciK0MRwCpfrDBd_LyhDmjuJheBcTiqEBLUH9aKxj6A_WniYsC6_ngzrgbydG1l3bvHiiV4DIFL347tpptr66cqc62EZxbDxSC-rl5rPNcyXBU5ZyuZkhVdHrzo53wQAy4QOlXV1wAdQEPOlPy4zByUy9uP2_TdCi3_heKvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_nk4IVaMnbW6EtV3BI4LCmEzjoYUrqAfnj5ueXZPXRdHl7SEaQhtmHuZSmXLpMKcoNdFroViZ8W3OItKozRADsijT3rvFhWwwqeRVIAoVq5C7lWZrGVerL2bY5ZmcACnY3k4pfcZoFUtab6_YdCq9xs2hMP6Vj175BBB7XzRI3qmYnUP1tzK8afuRt6JwGHlc4tmSuCVSBl_vOveJEb1VyTt9xrbDHUhP7vSJ8K8tqjR9G2NMD2jRvPuqCUgBFpoQPSIwbrHZ-GK-I52rRp5473tVo5ekGrhLgozZu6iDbaLRmU1G7fkVsJ_UXccgbVd3UOFBIyonwkGRhe6BDOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO-2-SV4F7oaNnDtKaaAfHRO3pwdlh_Pa_gKcHgNEv6K3wnkWMH4KweNzU-nuCCvCohhaLtlwPQF5S6sn0yDLmSm73jS-Wnk3k0KX-BpPFfJjqhEM81DIBM5YKwTVAyl-MkjjNLO6gVg35TM4hVSB5OR0Bx8iavr75UkjpDOPtROOZSimxvGFcJmkgBEJc43BiK8U3MVJQkKCuRlK7czdgZAquL0zlO1bwr0YJ8UoqYFSeJBlXz50Cwn5OzyzK2buldrYJNyRUh-GuP3URofWkgMHFhXHm6dXRGjRcvtEm1S3tsYk4yT6vfwOrt4I46YSVyooV0WW8gGdim6q5HFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5c2TC56R9nHRzkvwjJCL6I84MZWWXQqNM4T732JkDj-8UCOK9g9k5SuakxHwCrEyDnJfpvurF-SaMm6k5fDFpQ9O1Y2RLRj_2dXyTTB7a2gWoSKKFNpeehHaxbIc37cOzx4ZS0IJHL4S4SZCIO33eZ5wZzVecq4dh7p8LMNtpzQtEmrb0aXGc57F4-bhL2EMM38fCOVFbDHNDXvLM7SPs4Qh78AmsTCnyFB0nAQP96HNnNXx8miQx6j_4tt2z4aUlcNK1nLlJlpRyJWtMhBB2pevRcF9BvxB3Vd77yIhkm8WWLiuMBznhbFEQMV_HAbXXioHGc8loz3Fqep_eQ5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBQ71_Xn1M9YMaBeoFYsrt1xtGAhojdJet15zz4xSCSnQEmdpBa4HBbVMQu6W4fsbKJUXpkl-GdXr9B3s-DOm57fvGypMhn8MksOg62ZQ4MQKz8SW4d1GmBXovH6eu8wVQo9zVUsozK8q6VS3XAa4Py2vrLCORbk9r-4PPHgSNjTK74Kzi-AC9RC_Z4ZTubqGX0nU3cunLaU6NHHVUoANe5XPLnGPmLrQscvmWKGiWD8SE9JhaMVNnmsEpb0wryW_gGYoE3DSBbVQixdZYYIefo0-fgLeCqnPdgk9jVmncJCWyOH9QIhqUBBp6PaiEVFDhU4GUPmNeTbUuN6pLkc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfNGSlcGV0AJL-HW2u8WuOnm4OYVVah1iXtLHLjvLVqsn9FQ3eHuuiAmZW9i_ZNIvy9fnBpxeT5swP5aMGOq347Ki_RXM8_ydJmtJl8aF14Ttqoo-sobMQpHYpox7HpX_TnqM9KGcQgsijPe6B3PM7N2K-VBeQp9jcYOp6GtB_zcLmS_AAU5MJRUSZreliSGpTZOVpCh_yNj3zud-ooyuSvEHOHOgYD81ShtR941TDbxIIMBoFT_6jlkQou3rIk4R2xACgxsKCLfMltZgjZQj_Ce6Y7HrJaP-8lQNPu2QTkd7dUeUcWZOXKG0ZZDtJ7S5aQ0oXelEajtLZvEguY3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=MiG0Qaf1SilIO0vJ0xN-rCouTU9GxRHY7I3K7WUckDID_OxTphIsPkgiLdMgBFtZhPzLDVgYKOo4IWuPqM8Qkunf5DiKIARrNdX7uw4tBAUDV8HNdz8qRaQqru2QuAal-2iM4G6jzP5qaLloyZtdcUELEZpX_MAM89cmzvVDzbzfd3WzqwxzESyUiTjTQdQdem6hE0APNUDYhe9rx9f5WCF_E7krrTciyGddjWSZv9-BeigR94CtmVZgyLfforp0e54hMf0KgL8uXVG3caOF15XsKvouAbiYLjw5YU5W45DGU2SA6uFP6CP2kPOafyH7Z2Ecwl7FVj-_mQ6_KOAV-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=MiG0Qaf1SilIO0vJ0xN-rCouTU9GxRHY7I3K7WUckDID_OxTphIsPkgiLdMgBFtZhPzLDVgYKOo4IWuPqM8Qkunf5DiKIARrNdX7uw4tBAUDV8HNdz8qRaQqru2QuAal-2iM4G6jzP5qaLloyZtdcUELEZpX_MAM89cmzvVDzbzfd3WzqwxzESyUiTjTQdQdem6hE0APNUDYhe9rx9f5WCF_E7krrTciyGddjWSZv9-BeigR94CtmVZgyLfforp0e54hMf0KgL8uXVG3caOF15XsKvouAbiYLjw5YU5W45DGU2SA6uFP6CP2kPOafyH7Z2Ecwl7FVj-_mQ6_KOAV-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0IHQsAxrEqrKKvF1JUhA1SdDltkQpgGfOS0u8zUcBIZKmOaj0gnCpkcvulaAq4mVEVAqJsCGk7r-4__EH8sSansyfFyEcHf1t6vUIL_Ez_RqVegEYRF8WiZ6vGkMS18ZHhP2fpY0Fhiwucw29pyWVmhJz9AHL_Euv-Wip-31IFdR2BQFeOIxchDpr4lQKOzsWEcmhAI9_PrVuFwmqu2IpKMBCmSz5QE2O1FLn0lf1fCHO8Al6Ka5Yg6VE3sTpGCYwpwEU0ARyqUNi4_pTezofKglzhTIU9swWN1UF_8vhetKfgnts_ogrJ7MmOWDK1dsIwX_Nt-bA3_V03xUINYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
🔥
باجمع‌کردن‌امتیازاین بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
فرصت‌رو از دست‌نده‌والان‌پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldcbHsr5n77Ru2-dfOXkH3XjCtAlF2YtvYQAKKg60Q3XJezPzc-fninvHSC78oi0Zb8qsLgzpsHnL4yaVBuGSbJOXLZ99fZ2KYzMIFcj9jRZqy1SpWDlXUg-nfolO27UkrIun88aRMoqY3-YAYEvMoL3dyfIdoQdH8V40JX2XTLe75y3nmU78jGb8M0RnIM84i1wsqJWtG4OCjLem-lZD4q_6QuXee5hBvPqgsJs8AueV5U6IdXYRWU69rVkci-eD1z97EJQ5NhVXqpAzqYIOfVX9ucSBr3PLszXQdhriDuo74OnC-Kn3ImoBwIMCj77LnrkvkLa0usqWweVTy6qXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzy8xlpQSzuVm12e9HfOdMB2HsPKI1RHCbueYla4FZEidWcmBu6KgjBuPfsovAWRQwOzVEyfAfEbimVL1rKCqiaCZm24uAJgUoBbd5UaObrlMBYoin1cb93c8dv_1FIoF_F0DNuO4LWkfJCQpRgt1We0RMyGhyn2YsF87RQ-pxQRrAQrJLjYcKl3tS1CMrKiCpUTIzy784TVbFIsw7ZUo0Mq6YEHd86hB2ZblRcTzHC85K7Bn8PrT6Cg-4r1keXawQX3WWk4KBDcl9YVGAM4JQL9KGOQGix-I98DPxMZXsMpvC1ojeQLhfD4GeNdAQnTMbuitvWyb1ZOk8l_PuAG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw-pJI4xKPJXtrZU3zF_ZKIGwCsCXHzuH6ffQBjFJxfWOahjQMLQNCG_yIVZI2a_NTwVoV3Pr-dHRz3Vngut26v1ieY8izM4LL0_t9ufGYkIbSKcmZQGYbseFdSGoKr45NlTqgMOAM6Ey3SkGD_9-E6FgrgSBW_vG28XGj9ZAOajZ6yfAJOBfDAQn0i7O61qs9mGYc502xtgq6K2OLzRNoskY__cA3ux0iMDjzhYwZn68llLUGa7ljU79-SbqSqxiAwTPEdXvbvBNa0R8XpT7NcTLHKos4KzSHhzR3B6YStgwEizCCsznuFCjYwfaVBUpe2scFS1Enlmup_sFWBfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=fxLOmzwfosFuxsXTlDwNxfElf9Mn-HRjTq_prJpA_4LsMmfX_p0CpuHf2tMzA0IFR6qE_TCNzb-V0Aq-gkx19jAPNu0iUIn-Snk0JRuCd0ni1YRS9RjuEM7GJ81ltcldKq886vo7MOetgFG8rfwFu4po-3B7IX0DYZyWDYb4JYTKVYvwVlwm2ATyyXu8uz4qftvbfYU6fS-PLqBDu0xIceF6JtjQtiE4NtFVPpp0VnFXCnaYK5kY52HQo6fZbmdWYD-YbKJzLxbwagcKxV-X1NAr7GY-Ksk0GJLHH62um8loDsP3a5UftPQDX8vOQ8Rs460AjCXUKf4gm0WhJukaIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=fxLOmzwfosFuxsXTlDwNxfElf9Mn-HRjTq_prJpA_4LsMmfX_p0CpuHf2tMzA0IFR6qE_TCNzb-V0Aq-gkx19jAPNu0iUIn-Snk0JRuCd0ni1YRS9RjuEM7GJ81ltcldKq886vo7MOetgFG8rfwFu4po-3B7IX0DYZyWDYb4JYTKVYvwVlwm2ATyyXu8uz4qftvbfYU6fS-PLqBDu0xIceF6JtjQtiE4NtFVPpp0VnFXCnaYK5kY52HQo6fZbmdWYD-YbKJzLxbwagcKxV-X1NAr7GY-Ksk0GJLHH62um8loDsP3a5UftPQDX8vOQ8Rs460AjCXUKf4gm0WhJukaIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=Ct2gADhGEzykLQ-AKgYtY732KguB-ljacOwRJn--mCT6dnKmhOPTzKvlKGSYdnn0kLU4Rt1LhomL8QifUBzlmpukGAdSgeLgZYhg5C9_jpXBYWUntrn6-_M2YERXR3wk3UwgqLofHM8nxkiIXApgwhArukGWLf5MBnGuWxGydU3Bba9sEJU2YNOmTajbCggQc3lkGE-notEjt4I-45yzxiZN4bdnvv1UKKLqSE-6O6tcNRw61BgITIdCXXCPkncL1PJYOImVzBXbzMtpN8Ui09hexYC8qKwNqS1ouQSqzx7-vxFp5MxAr6iv0lA59BWjlU50QmBflpsLaFadWGQB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=Ct2gADhGEzykLQ-AKgYtY732KguB-ljacOwRJn--mCT6dnKmhOPTzKvlKGSYdnn0kLU4Rt1LhomL8QifUBzlmpukGAdSgeLgZYhg5C9_jpXBYWUntrn6-_M2YERXR3wk3UwgqLofHM8nxkiIXApgwhArukGWLf5MBnGuWxGydU3Bba9sEJU2YNOmTajbCggQc3lkGE-notEjt4I-45yzxiZN4bdnvv1UKKLqSE-6O6tcNRw61BgITIdCXXCPkncL1PJYOImVzBXbzMtpN8Ui09hexYC8qKwNqS1ouQSqzx7-vxFp5MxAr6iv0lA59BWjlU50QmBflpsLaFadWGQB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_dVUwL3Gs0PNdud69a1TKCAhA9iKnZsha0zlLjiCmZDdIrLJkby_cQDeX_GkcS2xgBiMJVD6vu3YYzPP3NWSTOZgrsswIIKIrg26VDuEE9lNnB4WPiFjBRBKmvaO8xILLZEY2xL-a9_D4UdQ7IzjJCY-kSf0TC3TwCb4xAe1FC2SoFd9mwTy7-w3g9ie-KGUiBjFsuJSCEjkfOEocunomP_siBBdSBb7rFzUzNC1q3LRvDIhcYXRCXdUTxKQ9Av-sUh64UYAV7QOVKlBtJ4QgczhAAHSWuyLVlu7EgCDlE5VlMemLecwfwpoaQMQ3pTcVXQF8shtsHudhZ0m723Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnKifPRhpjIz9BnLGlKcD4v4hXS9lT7RjchVey_7awA_03gLv9DrUKDyLdMVGrulBjDskXlOw_i49BKxr7GplLmDagoFiks2hPCkzrRGa8DzZIyKAS6g2a_LQQyhn2qt7XJF7rCZ0bAtF0FVbIrFJEVqsJyuWm0bxnND8QZxd9Lw0sr3aDMfzaUQsYk8krgP5tUKLTPh0htVqjbcwS1gafflPqRvMJrIPpP3GsFRqz4pnJFGr39PSb1yQF50q1S6c0C7fMCyKl4nrke1Gz5lWxu0KLu14Y4v2DoHGVPqDAbDi-uU53bjRandceOxlghOGsV1iXGB0ub_su-Meb9_EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24370" target="_blank">📅 15:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qv1GZVFBD5rZnia9H5EwQx5qew12NdOz-YVuHWBRWuGhhmYZnaNN2M_WOKJCTHTG2T1PIt5XLKRyISrY49iU9fUUTeImDx1muf4mAlVaVwUSxawVGfDdnfwNeNB2VkG8h_npaq7ZOjkWBZmJyWmQsmZk63X_Hlj7W2NhXHI2lmhJCDSiJ3yYEdxIXRCogvJHsrx-ja8CJcc880l4lovxFpL9sgqh4cPpHcTpfudYaqjO91_mGkn7quxfRh8NGFB6SpALCd3teZ-2i_72OmqBIzcaIUWeGIP9PgUNLU566Im6hkHIzqYldjSBjfC9aiipPKLrbTqqI3Uh_18fykffiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=pgjf2E0m1xFVF30lj_7IjdTSdd1ekrbDvUxmGA2gE0MlYe-g0WhRwJ_8TR1FTtuLHSX9GLXB3pCIyvP38L_Wb2D1MJWDXMFA7Ndh6YUINm-s6qUwVnQ4AsGARjkrR7dkUNtm9iOatmUb5hpMarJDPUPrdEdG7t10I4F_QtnpOLK9DZiDhZJ7NDXsfkJREC92AuP5ZLRZkM2Qqh-67DKns29Yg4QGzkTHiTDLaqdo6K7hImeosw17FtC1bKBldY0h4aebDN29KkXexxKSZRvPd59UYR8Yvf25KDSVDnXlLBPffFXaqq-zt1bADrYPXtEU1zGEZPggzDPCyifeeP4Kig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=pgjf2E0m1xFVF30lj_7IjdTSdd1ekrbDvUxmGA2gE0MlYe-g0WhRwJ_8TR1FTtuLHSX9GLXB3pCIyvP38L_Wb2D1MJWDXMFA7Ndh6YUINm-s6qUwVnQ4AsGARjkrR7dkUNtm9iOatmUb5hpMarJDPUPrdEdG7t10I4F_QtnpOLK9DZiDhZJ7NDXsfkJREC92AuP5ZLRZkM2Qqh-67DKns29Yg4QGzkTHiTDLaqdo6K7hImeosw17FtC1bKBldY0h4aebDN29KkXexxKSZRvPd59UYR8Yvf25KDSVDnXlLBPffFXaqq-zt1bADrYPXtEU1zGEZPggzDPCyifeeP4Kig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=guohgrxlQ9aEgBmPoU3vi2U7Awk87ivxOIrYvbZSJRi3tc7ZAhn45FiUE0OrPdXotSrrHtSJ6XTdzO3zVSRydgBd0V5SrhnZR9mCHjH7WJYI_8h-fuP-KQLsj1PyOIbNBlnU28U4uokCu-NN1tgIQzoRXq_e67CbVlRJwMuKHmRVVH9nEqshyXbWyv15qcQevYoaSBZXcPMaOw3WNcYW8jpxQ-8ZQCmgFHiLHE0W9nsLNn_VhJbjy0Xxw7AHTjJ4K_TR2SbRsOlo3Rqy3AG4JDX4CcI7aM-hVi3Aepe_vcrwWeCHmaHDHditirFD6XlsdKIMXupuhnZrK6bKikDDnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=guohgrxlQ9aEgBmPoU3vi2U7Awk87ivxOIrYvbZSJRi3tc7ZAhn45FiUE0OrPdXotSrrHtSJ6XTdzO3zVSRydgBd0V5SrhnZR9mCHjH7WJYI_8h-fuP-KQLsj1PyOIbNBlnU28U4uokCu-NN1tgIQzoRXq_e67CbVlRJwMuKHmRVVH9nEqshyXbWyv15qcQevYoaSBZXcPMaOw3WNcYW8jpxQ-8ZQCmgFHiLHE0W9nsLNn_VhJbjy0Xxw7AHTjJ4K_TR2SbRsOlo3Rqy3AG4JDX4CcI7aM-hVi3Aepe_vcrwWeCHmaHDHditirFD6XlsdKIMXupuhnZrK6bKikDDnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwEWwtD10sS-Fm146bt7PbwuzRhaWnXqQ41MTR-W6BH5veJecwUttpLjZkTH985NqpuhUGi9fDY374SAhloarkxrjLJFTRxWiFdy6bk6H4XKIYl7ltf2UCariZJ-CtJg18xWikbHmD7QD-3sy7jrZ37aeiywTzr-0NSBmYcysOtGpIAI1uRG2cZ-b1MriZRHn0DHNz4gEmM5Apo2D5sdYNQle9E4q3AO5DXKZKqA2I1tZwlIVWnT2ejBFIdLQIWhXhgKJHbbsITSCciaNgr9XPqNJQPW3fhXzrjVvl4I642gbOpYOBOuJtAbHdFf_G1TFXG8HPtmi21xHLW7gFw0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcxVYO4gAMFktZq3LSx4QMOxQ46wlc-mcw7-KOeSzHlHxtIOxevorIg0jFXYiDHtXL1bwqPp6ev-n92SNaqfYg1EnoVnvFLXwSRYWs8vi5Klv1MDOgit2VBH9DS71zaq_1ukqTUvw2b_XpABmVM6gEIraQJmmuRNXgVYuZRwnasCHDCTxGtZAfUizWkjaDxpqHKVE-CA7SU2EqokKdSSSDMQlE8sklbA0sGJiCIWrb1zODa2GAT8P7hXzWDP46cdr4P6kZwL6kFy5CJAJy4c7oxgPPQiGFD_xppyif3UerK2QAlDeIs7Wu2LirUlqzS9q8F5adhF7VwJt2Y9SMIrjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXrWLs-agv4wMzHFhpAp65Bd3MLD5Dlgu4sb3Ur7zMMwDCAUGoLyc_UUZCTCgEO7aaCzMcYoYCHkcwq2taLSmb8E_ug348oB8RHp8Ymm6qb0yk1rubFtuvqCccXhrp3RdU1HUPDzW5KknHXBi0ZiT8gQSffcF-mzo13PpCSO8xX4JZyKLc9NIPqtpgFB1PLKfNqXg2Iks__zntGZ0iSJ2TG-rMRmzM5eIZxVX-AMv15mm3vr7Bzf2xTS1V3rB9EtFCBr6P_lAVDnMKRSDOQZL1FsgzQf4oOC-GnLBaU8ZRCeEaz2RY7r9qOXBcPhDHxhrNT1Cwxxr2gSX49ofcV3Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsJZEFdp7Uox9C0ZfnCz_BcDKygmUPXgEEuBnfHwIG2UPvV_B32-e0p1gMcX5pasUbIGHIcqT3wWaOqL9-h8Kc8kpkAZQq6yGE96xzVEccxhVMs_iWT7Ydgu6cVhKxhjTdhR2ZucJM1-sxrzI_F1Jd9m5EZ1agRignlI1612RB3XV2Ly0zwgCJYVOxRySR6KRaYREIJnQ-jtCSv1ag9wcWbZihZ_ao-BvhHmyj5MxzLWQRXk9bWuaPfzqtpp0lcORfdHq4P4hv54h2txKInqZ_O43Wf-Dobe_gSgzEZRoiloHcA1mKjWbwuo208C4yXV52PtjLBNOTdDhcIRpF74RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu5id_MECklvLVZFdQwlzouAymNxFHjejypcR4tXsDkpRM3yNNewGhL0Y2bFON_N493QDGbGXlQEZafFny2OtFeQPm8XvGnatCeqnia3rgZ7mo33aWqVY68rWfxAhXpSbbWQJfCDwjNVIGtNguV6NyOAjvIiHM_3jEld2H0jWjAzb7ZXFI9oikbeelKP2r7U8nfB_4yK0JVpzBZkY8KfiTiUxVYlgxpXv0FvjBsXFWHWpEcKwMk7Dx91RcphVOhsgOfANZTtUZymQsYsKV-lo1IPPnr4UbEEiEBLbtbUmwV1v0JOKlAj8QzSTSSwl0UeWYFsSEriP9MItvb7XopTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDZzz1JtGoTFIkTrBOAlt6HFRYcr2740TF-BiiCNJ5qxCFElEL-oQLwzULZpINOkg5UxGXKhHtHOGkAZGgzWG2I3mw5dgz5BD70EUUIdzYy6W-35UfSpjrOhQ77z3dee4cbYANkH_GMvVmYRgljwVc1FqkUBVvkXFtcm2-L6-8CGHHYPHA9tzkDhorWHCs0E-1rKBcW9Zuuw2sZVhUy6NkQlZafcBeJ3TNegPAaypibnVLJCxioq1qbqa5GUtabkEf41yZipMmuca5kfE_86psGGqJ8Hb80ONmRLTL6qux9CdetF8asa13mbVGMuXhRACHYNg-1lUR3jqRIfEJVW6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=MungvWYkb7-fUwtK54-0ej0hNOkaD5vguCd0gu9cN2jS2qYwR2yHMPBqprNDLzd2qcWKEwznYBfcuBLEgbZD8o3fkDYZK7Rg40NYxrWXgHGP1N_vyitxRdFWskSxXA79Q6h7copm8u9l2lankEHZIp7sO3GsqetvZSugPIPb1zXuuWdiC5d-uJwyg0knzygpy894ZkoTe_5oaFUsL0HcXqspgUgv49bTTNant92RRRfsX6uunsg2adkuhvnC_NbMNyK3jBWsJyzV0So9EdoDIXOktr80-Dc_VZVPD94kbEe3PfMDjEsh_UV6gIjJzz8ycoetvK-1BQX34FwaQv2ncQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=MungvWYkb7-fUwtK54-0ej0hNOkaD5vguCd0gu9cN2jS2qYwR2yHMPBqprNDLzd2qcWKEwznYBfcuBLEgbZD8o3fkDYZK7Rg40NYxrWXgHGP1N_vyitxRdFWskSxXA79Q6h7copm8u9l2lankEHZIp7sO3GsqetvZSugPIPb1zXuuWdiC5d-uJwyg0knzygpy894ZkoTe_5oaFUsL0HcXqspgUgv49bTTNant92RRRfsX6uunsg2adkuhvnC_NbMNyK3jBWsJyzV0So9EdoDIXOktr80-Dc_VZVPD94kbEe3PfMDjEsh_UV6gIjJzz8ycoetvK-1BQX34FwaQv2ncQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6FR4cY_W47eq-k3RGvTKuP7yziWKTn3r0fdWcDA7RUSD8RQ6Ow6NY5KZqvuEzV_Cun0BpccGGXNpVZUSRGg5XLomBAklG5A7_nIzDLwBjllXs0vYP1ut_6V92DeOse_IYArmRtPPdyTxXhy-YOMuDMO52yc5-gl5RCPPjjiAERIoe2vcozTbUm9553hdOUPsAT9V5sKryUFTDvH_kIgWMYf7XNMCNbucR7yjXwX4edDYyrLe8FsHZHaGc9KsYM4o6QB3ZTrBFxdvlL16vInhBZGIwkTvxQvN3Ydvktd191wimsTEhCbhj0ieNQEyb5_58_LrrMY-tF_IPur-baquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار مثبت 18 و جذاب جام جهانی رو در پرشیانا آنلاین میزاریم. اونایی که جنبش رو دارند اونجا هم جوین‌باشند. ادمیناپست‌های خوبی میزنن.
🫦
🫦
🔘
@Persiana_Pluss
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24359" target="_blank">📅 12:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5JfOyydwWLekoZTjNlcPS-Pi2oXKQVwoP2wzgNBxfMgNgHEnwf3CKukCcCTFaxS1gUVd6t9zUl7GOWfWLbwOl2wya1bLkD0Q_ZMzThq-ULUslVSoVzCYnUiBQN9cBsVVeL6qURWbeBNhWtGCg8UZwcLlCUynzByMlo49qI5PwhTv0W5myzikRQ_1bFOmOp0mqPLZ8-q8rCgzBoWlk_CXcpePpLWvrbfAP30XlqSbb7Qp0keyrHWsmtdMDQaTjRG9KZVpbHxQASgtJFmwO3_FmW7iknB0TfF6LRodcqNj3V7o7GMFduieQ6EpIhFVPD-yd2ELIl8RIavVaVpbFqY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس: دراوج‌فوتبالم و درسن 34 سالگی خداحافظی کردم تامردم روزهای درخشانم رو از یاد نبرند. موندن نویر درفوتبال درسن40 سالگی نه تنها هیچ کمکی به تیمش نخواهد کرد بلکه باعث خواهد شد که مردم روزهای درخشانش رو از یاد ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24358" target="_blank">📅 11:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5J2kYmbhHyt8CT5BKsv6BC7cGeZ40xmaayYWPSwijY2kadz7vit8BJODz_ygkmidFOY3fNx5T1ZGJxlYtQn0QRM9pKmXU9JtSNOI3YJW4EuQX1AhZsoC--YDlo5lv0z3pCuUGAwZJHQuC3fTgoX3piY7wmqat73BorDLYiDpmUD3aGv1-bdcpld19p8KGmLCzghN5ty6QxGaYaeUO4eb12dPiVbLEW2Ea58eY-Dp45vaWDon-AXACDnRRLs4e9ntya5wvQmAxjTOcssV8ZMWi3lT-TdcnrBxX2e3BjMIDwAF5bZbe9PSeeUgg-ZQVDFnKUvNjjMfVHwd2zC3EHloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الانگا بعدازمساوی‌سوئد باژاپن خیلی‌ناراحت بود و فکر میکرد صعود نمیکنن. بعد از بازی رفتن باهاش صحبت کردن گفتن آروم باش، صعود می‌کنیم. پاترم توکنفرانس گفت بهش گفته بودیم مساوی هم کافیه ولی یادش نبوده. بهرحال‌الان می‌دونه و خوشحاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24357" target="_blank">📅 11:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVN8PaEMohzGdjW2rMHGjaS5b2ZcHAZSMhUyTgu68IohLc45LoFu504ITEP70xTbsjczg0Vy7B6IZjXYH6c2rrFgr1_93LRBf16tEOpEeE3OQeYnMY4MnWST1PGMQrJOtHIFVBJbCyWzwzZuXhHqx9lN5Q-DTPAKX_SxNtCvIqaIyKfIe3f86DSNMvAMUoj7gZPTU39A90urvBAcU-q1MnDcQKiW8Q-BoG-0xGGLdr-EoNfM3_CgBI4eLpOumAVaH4etX8tUBJGjWx8V9BR3p62hDlnoeCR_gFGX5CKQfXWRsgFsVH_ylxXAjarHw2zOBfrLPS0pzE36TqsCyd8DuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
ستارگان رئال مادرید؛ وینیسیوس، امباپه و بلینگهام در این جام‌جهانی در اوج آمادگی بوده اند و ۶ مورد از ۷ جایزه بهترین بازیکن زمین را برده اند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24356" target="_blank">📅 11:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzhGWLKKm_R9mdsCKeP6bi9m7Al2s7T9UXSQsRrX1STD5q3TQyuF_XMieoaROZbt84K3fOqh7zb-IHlmkdZFS60WocvSm0ez7K5gGB9i2w6ZapuNvp_c3OvtLPGm9_lAfO2w7ezvuihfZ0PIm6nw7CG0kqI6c3vJmTPj4uqjLXchsaOJZ_QGzvoZ6wNDn9AbhdLwZy9zz6GNoZkgLJAgPZfqhIxkBDGIoUsjXQMdHPh62Y06MER4Vs4iFkNhLiCyDkBCEhSu3vuwyRmCuQhNe3P7_uLSjNAu1QpBWWsNmV8OljN5OQ4vPtvoQusUxRNUpHdYkBYc90oLAY-Xcj8-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مبین دهقان هافبک میانی الوحده امارات از وضعیتش در این تیم رضایت ندارد و به‌دنبال بازگشت به لیگ برتره. دهقان فصل گذشته قبل از عقد قرارداد با الوحده در آستانه پیوستن‌به تیم پرسپولیس قرار داشت اما عدم توافق مالی دوباشگاه‌مانع…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24355" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=D_Ik3A2GzKynshV5W44jTyLp6L7i-Nv6JJbY_ADJB9SxuZvVv4EJutHg6q8WFpa4UR74JOAJBqk8xFpMbXwU1Xz-sru0Wg6lyI-Jdw0wjLFuDkRDLmq45BX9LVSNEJpKSPuq6SJ0-aI4tpykbWDVR-2031HmtqO0L7QH7BpVJHSvlVlygILrLxtssdlcYgt2Z6CTrIHT5ebSrI5HuVRXW_tzxRyHriaS_dNj7smZxUPMS5Qf9b8mae_QI0c5jgIYXcds2U46wLpp13VsCmjGsuJY3Xxwj4G6jc-9jlxU56uDSSH5Q3oXZl3AZ6ELyMueilIE4BcgyApzcu9KXiSKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=D_Ik3A2GzKynshV5W44jTyLp6L7i-Nv6JJbY_ADJB9SxuZvVv4EJutHg6q8WFpa4UR74JOAJBqk8xFpMbXwU1Xz-sru0Wg6lyI-Jdw0wjLFuDkRDLmq45BX9LVSNEJpKSPuq6SJ0-aI4tpykbWDVR-2031HmtqO0L7QH7BpVJHSvlVlygILrLxtssdlcYgt2Z6CTrIHT5ebSrI5HuVRXW_tzxRyHriaS_dNj7smZxUPMS5Qf9b8mae_QI0c5jgIYXcds2U46wLpp13VsCmjGsuJY3Xxwj4G6jc-9jlxU56uDSSH5Q3oXZl3AZ6ELyMueilIE4BcgyApzcu9KXiSKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇸
ژوزه‌مورینیو:
من دوست دارم بازیکنای رئال مادرید درجام‌جهانی ببازن و برگردن به تمرینات تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24354" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇵🇹
🇵🇹
سوپرگل دیدنی نونو مندس ستاره تیم ملی پرتغال دربازی‌مقابل ازبکستان رو از نگاهی متفاوت ببینید؛ همشون فکر کردن که رونالدو میخواد بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24353" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0xHCBVLtRPCJ2ucnw-m3z23ZKxIGe9VwGGC0LFAT-8lFK3F_diG--lzGit0eNOx0xH6HdBB0phSaQQR7ZMGzAqK5PKTDd5ZFb5xyKvbs1AcGTXlCu0V4R-kuZeb88ugrx0HxhFh-H2a9rmqPNzav_i3L_4BgP1eBlE9ctUwUpzmNmn5YpW3AlTgMUWTBpRAn5sCu-Xpq89RYOdzVFno9AggZ2MlMpA8uPPB4600lNlfquaPZFtK2THKy9oMswjktrr9GAvVoUXLHJ-qNV3W8RWwHYGYoB6EYXO2RkUskJ3yrpNjv5fVn4pF7O7AfeTrfREUwas9_EQkQxU6qwsaWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24351" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIZIxBBfI9jxMQ1zVGsAJciuyRyZb9BAriodCTzavs30y7AnRPdV5aTsltKe73ZIa8GEe7jJhTXI0omVzFJocv1lYVS8sPwLCqKXZVxYLV82Pc0AR73uCRgSakSglebgF8vPXv-JkgtLr11iHzKU-cd6nNo2vQobtgoT8OZ5BfRKeBL9re1WdbuAlOuNg2KP6Rbp19gNjLSDUvkRLjwSqEYYwKo9UARYgV213UuTL6v6qiss_xEjm6Rgucb6PkRFQXL2sl9IY6PUJflh6u-1lDdIlP9IZyoPlz-w4izsFo7to_n6nvUS6v0mLEMah0Q2cjsEE7bEY5UaMMA6kopDRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ برزیل در مرحله بعدی به ژاپن خورد. هلند به مراکش.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24350" target="_blank">📅 09:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=iL4IULzbjgBl2ARiDm8d2-dOqHDkBYr9xPw_oSZDH9FfblzKBJWpzgJAO3qxM6ALoznKd3_zq8wRcQhEq7Zv076EX-TuuCcepTF9RnyHt_SDrOULCLFBQh5c-6FSYCknzDz_KnGcC-2INLK2eaarTuKseHSG4ziBdapiPN2gQrNr1YliHbL3vI_2wuZFxYvBMtNbemnFsRHjab3taowttnhbfxyfDhzmONIXHLD7SyDSP8h_lK1RTi8XYpxtA-EzriKQQVsxOJ3j7Vxem00L8BWeVWstIDv2WrC3v078V7hwpUCmSeLX51wtKfvsv9AQgIDZKj_goTbD_q1fuCH_oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=iL4IULzbjgBl2ARiDm8d2-dOqHDkBYr9xPw_oSZDH9FfblzKBJWpzgJAO3qxM6ALoznKd3_zq8wRcQhEq7Zv076EX-TuuCcepTF9RnyHt_SDrOULCLFBQh5c-6FSYCknzDz_KnGcC-2INLK2eaarTuKseHSG4ziBdapiPN2gQrNr1YliHbL3vI_2wuZFxYvBMtNbemnFsRHjab3taowttnhbfxyfDhzmONIXHLD7SyDSP8h_lK1RTi8XYpxtA-EzriKQQVsxOJ3j7Vxem00L8BWeVWstIDv2WrC3v078V7hwpUCmSeLX51wtKfvsv9AQgIDZKj_goTbD_q1fuCH_oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24349" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj3HaRssSLb6uW-ldKjLxF4KHtt7vLaS3Vs4zWIsEA_GUOhKZLLtdbqUIuJHq_WBDdQNwyz_4mGwZR09Z73-RyRFUBBjhHUacxHVCt51Xx0oU4yj4q1e1yZ3BaZe1RSbu9Gc9mXopia9mZyIZDSQ06GgVymgO8kJTWiOPmuVj6Tt95_k77D6Z4C2ik7yfdwQjZiEimnXpnU-fgHjQp7Tlkd4rMRcR7Rn44QXxf2L6fr9BMEqxy929xCX7Pk0kDfsVoUgl7KlwPzw5fDiXimYsX0fQzV5fFVV-SDq6OHpEa2WLsCfHvvplvUQjtnHgWARqLiwiEfkNAnlVuE1AJsBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ ۱۲ سال پیش در چنین روزی؛
آخرین حضور جانلوئیجی بوفون درجام‌جهانی؛ آتزوری فقط یک تساوی میخواست، اما ضربهٔ سر گودین در دقیقهٔ ۸۱ همه چیز را تمام کرد. کسی‌آن لحظه نمیدانست آن اشک‌ها اشک وداع همیشگی‌بابزرگترین‌صحنهٔ فوتباله. پنج جام جهانی، یک قهرمانی، و یک خداحافظی تلخ که هنوز از یاد نرفته. پایان یک اسطوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24348" target="_blank">📅 08:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtV9fLNnJhU26V2G1WB532bJE6vCy_oBc896jxvU41SOB62sQlWSZMvSAUCobs_QYaZuZIPM4qkwsAv-p7JfGTovWK76pLONysfe0eeSkURdFkk902gUPPTAs1SOy8GG-vSsTvOzm028bVjixkT9QN1IsAzaFgJvVfnN4BtvqKKdrqULc65KM2cQqr3QEQ85-QNo0hywbJfz1T9yP9t5CHtreiIcz5zXDsmpTC7bfPCUm7ANuyXQORjF31TJcG8cvcKhseyU3FZQoZskGPPjdgoikxtxX5ks4GGUsqVK0lGv7R9Mj1t1r6I3NGAuKJYutHKVqXckPdBFM8qcZVe3nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F و D رقابت‌های جام جهانی در پایان مرحله‌گروهی؛ترکیه‌بادرخشش آردا گولر سه بر دو آمریکا روشکست‌داد؛ پاراگوئه با استرالیا بدون گل شد؛ هلند سه بر یک از سد تونس گذشت. ژاپن هم با سوئد مساوی کرد ولی جفتشون رفتن بالا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24345" target="_blank">📅 08:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuDFc7mvsuMr0o9GeVz2_Hh1utXJCtw2dqjm4gR7d3Juu7NWSbxoNn_fdHFtKVTIVnbcUskFk3fjgRlxkRtWNk7vdCLOlIk2aFod7o8AjPBfT938QaPxqXryrdlGx4oVB0sYiSbZXW_3-_k24n5PJ1RnAGb2ibR4SdJK7a0oz4PIqX1M7pp8cF275SbyntfZxm9KUfS0ujfmMAxU9iLasstLetlrgP6Qr8OS1AFKWdhYAgFE8M1o58qMoffI4jnLflKqggF0i9eKbgd4iy6Ug837yLqJiiSMTJI1u2yIe9EhqTgnBdFiGPCMR2Oz3mNAb9eysnSpPeC_fAKNIYngIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛ از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24344" target="_blank">📅 08:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn_icB_Hubtmxss2vQ-7QeEHWtAEaswgdAo6NNdxeRPRLkxfVIoth4IXSpdlPCs8Gf82M6NgWQ8OjHG6fVZCXgLklUPnPc45db4gwgV3GVLhfQX7dFnvwY316MQzKGFu8CzOdmlqH3NZjd2x7c7vX-ywJAco-zRnbs-jrCZ_BRAiF0PnwCaxkAdy9tBa02TIpV3VQQhSzKBSjNzvA5yzYmI3d5TAK9M4b5vfxHsWxQLv12fsn2MBEBxK_iCnraTGtn9OCoSrVYb3drPoFiyb2VS1jMdDAvYx0xYYMtSvDjfAU8GDV7MQTqUX0B7V4fxJbycNK2jhh8mhv42XBb9wow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24343" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLQA8Dcwyh2wA1tee4oJChnsWbBgxbyPDNCvhyN9uyctGUMzBjrSb0QDcLUkTbv44k8BWlp3o89R2VMNKrnim7YBAKfYuh465oQgufM_vFd8BCN21YS6pXW4wRblff_VjgqZPqWTqqQa_8jJcXVZG6uDZ412CUMOoWouzZJK5K93bjlKKrCQ0CVjt-hUWzdBijJ89pK7vFmtQZY2xt-9hdDokwkTuoU6DnGyjlohAyYUsYbEVSrGheQJlD52RD4JFHGlDAc7EEJifclD7kAKBdl8qC4ouJ0SPMs4yv1FqWnsAGhg5useUYOnJ412JuVpw__W35Cp4KaAtMVh5CcAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛
از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24341" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24340">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMyCX5TvOJbK6L1YWTlFCBgbUXWKkZTWoOH53l5y6oCKsdkfcui4PDQDAS5vdSinCC5syjW6WTyMIcPThhDZ0gUEJdJpK95uOTmhPftz6O7XWtWhDOjj1Y09cy37o0Loq_RFAiACvo02NBU0KUXvr1x4TRkk61cgr4T82n9Ilb_cHDGNc3yK66FcW7VVTUtqYzB4etvIypImDHm6cUenWeL15EjjEhV8json1xFq5m8l1yECvA-2anV_7qI3O-udCsAjmPerDtVmK5CrrukcL_cmoYgLHhzW6g2IPmfK1qcUkwTfPf-WeTANSkRiPfPrFDZ6kLyz9B4sZVLbeSXoqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌ دیروز؛
از نمایش خوب شاگردان آنجلوتی بادرخشش‌وینی تا برد دراماتیک اکوادوری‌ها مقابل مانشافت و جواز حضور در مرحله حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24340" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24337">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24337" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6aS39Kw3EISLAWeasctekkeEOlEhK1rr6E1mwQnzLVXykigGy4Kr8pDmeQDhKTFwa2Yc8t2FFjpWKVxoN-ISysdrh3uNlpu3Qcvsea-jm-YkRqS8ogJjhis7j8_WUebC8VHkVO-6LROKnBt4JoHqFWqwyWpRKAId76SgUzpJUol-A2Eb_DcLr38HDUqc07UuQQFjEJFebjTQjDKnv3KpBTOHfTeqNiY37Fsb-sRr7CCXIHDAMalgj-qYL8c-w8f-LAeDjYb_bc_juXKUtWgEL4qXAt4f_yaUXSBkCPoNWCKgEtl4sWZ3GtfyZN2wABQJoCoBuuD-2zG9pIW4OB1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24336" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN4zjPRqogUs0bOtMCe_qBxtatg44sxzcVHrsRGUrRAbqQRoU8LeaZ_Qr55p1uQaMJ6sHa-MAMRCY_9OvF2z_EszF2MhOmR2j9seDalNhN56PmO7yos5w6XDa7RfvE0BGv3vqo9v4X0Es-0nTbSFsrbit9zNK465PD-LntzypcNwZZqZ58gGCnOgF1-dt1mCRGo81XQxTIcQNMmNtdUCAXa5BwmrCM7XwDyx85wVGcjTVmS1qNIWGMjTz5GMiimDbPosUgU3hNYIR6OdZNJK6N9CGytm-r2ZqN_eugixwYOcdhWhd0swx0Cs5DsecutKoA0bU6Tob5BF39qMO9mWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24335" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=ZLZAtNS9wbII2f8y2bbcE1LxCR_MCEXwm8YyW7QOjxX8xX7ZtCwfc3sijkPcxlYv60otv01hFLZiRiijuNKXUvChugRDo1OKsWR0EoR-UPLIzc8Ul-mfnzV6qhdp3qK6oJl6DaSmXEwMQd4iovHQiUPuLsaIiLe38n3ZHtbaoSf1LPuFIPq3gIHKGLXFDQCa5wwOCzArH5UAA6jnHhS6uEGrebftz-Tw9QrFhNrrEyiGl41c93Re8Xk6SDjTsoTQzzkgSfDv7uwYF7UXMSBEpjsVLfcUSgG8TPN-O9fJqiV1RvNzGiVKhJ3Uf9Vr3KWhcrNeYY1brCHsv0vqw6qE8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=ZLZAtNS9wbII2f8y2bbcE1LxCR_MCEXwm8YyW7QOjxX8xX7ZtCwfc3sijkPcxlYv60otv01hFLZiRiijuNKXUvChugRDo1OKsWR0EoR-UPLIzc8Ul-mfnzV6qhdp3qK6oJl6DaSmXEwMQd4iovHQiUPuLsaIiLe38n3ZHtbaoSf1LPuFIPq3gIHKGLXFDQCa5wwOCzArH5UAA6jnHhS6uEGrebftz-Tw9QrFhNrrEyiGl41c93Re8Xk6SDjTsoTQzzkgSfDv7uwYF7UXMSBEpjsVLfcUSgG8TPN-O9fJqiV1RvNzGiVKhJ3Uf9Vr3KWhcrNeYY1brCHsv0vqw6qE8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هوادار تیم ملی عراق که تو صفحه‌اش گفته دوتا از بازیکنان جوان اسپانیا بهش‌پیشنهاد رابطه داده‌اند‌. اسمشون رو نگفته ولی گفته جفتشون تو بارساست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24334" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTnRxuPzg1VOI_3nMjWLq9Dysk-MVfa_jRaEV34N1WTCsknm7BQrBF_dRY00IyJs3qQ9rWv8E-LKZSdmxtnJlA_Ux7HDyii5FhDAhOrEUV0Y46-nC2FV4POwJ8HdlhIVkQX0K0HWFWWsqdjjkWE4R2FNdcdnVZYcSyMkS93_JfUmGeB8WSU2XywL3WkXVIzSyKZREivx6LNiU14TkoKZ47xTqergRARb8uAjIWT2TRayABl4go4TIt7OWpjunIV-JN72c-Rg9O3k7OjrrS42MN9Q9oZk-hyFNPS3UPa4ylOCT-c4cUW4Cxy8ntAXh2vG9TGVgABMaDpFNDcMJ1sfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24332" target="_blank">📅 00:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgVTLot1hx8y3YD6-We5bE2QUtVbZnYhShEMW7pMXcDZYRZHBOeCa2vy7I_7ZM83ac2VaKqb2MA96bUhvTOnUF6vrwMS61LbaTEr9m6RIzb3PodsVFNZN2pLC7RhrjlBnzIhH3CuhfvZ3yHVplPcScNnJ3SAEPYczLEWAOPEyBdqVK4yVydUKBheVhUlX4HxGwpTQGSPuebRvIyCBfarmM2j5LFvdGYeF34biHrGqN1C9VtwcXTDsvTslFGBjw6s8YNAPPNsq4vkWo2hzrn6UR9hVMNhdLiNhiAkpaNC_f_I0U_RzMhEJnXH2F-R3a66UIPEIw4zltPrkTOhbyemOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24331" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

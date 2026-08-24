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
<img src="https://cdn4.telesco.pe/file/i8NolV736fDDHYAkbn6BJVxJg-uuHwB5UYaYqHAs73SnfTNY1bo1T8C__eqv0LTlMWJtfmXoFL93Uop4EkmyRc6ll4aLyt0mBWD-TvWmuj-7JZHJmzV_9oZf3Amb_BkGsjZtWlgusDvnEUFybwumK_NMjAjZr2yeM_LzlkUBMWCsjTmI9LJ86CGEJasvp3Aypw35RrG_DcNYrBhs3KUhpAPolnTLC4cegt11Ysn3VbFxDXo1YX833zd79ld6Pd4LJikKJLeYaES2J7sx1Df5Lp_ZxFy17zxv67q_OFHGJ0umbzLla8rrBJwa6mVRwnQW0_pcqv1JYy015IyUyTNJdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 442K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 13:07:10</div>
<hr>

<div class="tg-post" id="msg-21429">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUo6GJK6bDi8MyXmESylIXLZ3bkkXqeg7w0WBPjLWe5QPLEAv9GPJ4zsuspm9DHmtCyuY8JsgBhtgR-LIJ1tk1GsD3_UVv1NJWYulyU5km_7PhOVEjDkTYooiW0MRoOPGx4rHbd84WMN5odHuRdbsXbY4pw-8Y28V8Px56hbWbAXiuOqswfgqNvSTxEOBfjE7p9MJ5w1HF32lcV8yy5A_c8uiwiu-m9nHNsaqd04fpDqMfyDPYdL2_AuwNQvw42l5QbAN7gzxDIi5U2uS7SY5L-ddi3pIPNi5CtLLKyEl1Afkk0wnHUSI6jTR0LwGTPpu7203uye3e0Z40oU1ck_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب افکن مخوف B1-B از پایگاه فیرفورد انگلستان بلند شده و در حال تمرین است
@WarRoom</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/withyashar/21429" target="_blank">📅 13:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21428">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g14Bq21TKj7nBnIKbcEgzoryhUm9m6MZUpTCHDUEpGLWt_86l_0hzuWSxSwPJG1AE8du46RGBYyLv57io1V_G8NXSeqprZsZBdq4_XbAlxVOmYuv9VM3KHUE_lUf4vJ0EF9kWetuZPJyU83bDgeUvWD5n34d5ZLSDCKtiKLsHSAk33BEu6t4YlV4vU88oq2L03MEXkirHYExLYxk94c0erAVHjdZdqfNFGp2IibClqQA99wu3WvQ_xspO3BJDqE1TpdPZQ_fnR6LKBnrnRf2ZsVpwHSs4aqkfnkCpTHkc-EhRFdaSaB_Vi1fSXgvOxR7bl1iPuYBfiRivg_SNC634A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند
E-11A BACN
نیروی هوایی آمریکا پس از چند هفته غیبت دوباره بر فراز عراق مشاهده شده است. این هواپیما یک
گره ارتباطی پرنده
است که شبکه‌ها و سامانه‌های ارتباطی مختلف نیروهای هوایی و زمینی را به هم متصل کرده و امکان تبادل صوت، تصویر و داده را حتی فراتر از خط دید فراهم می‌کند؛ در نتیجه جنگنده‌ها، پهپادها، نیروهای زمینی و مراکز فرماندهی می‌توانند اطلاعات میدان نبرد را سریع‌تر و هماهنگ‌تر به اشتراک بگذارند. بازگشت E-11A به آسمان عراق از نظر نظامی قابل توجه است، زیرا حضور آن می‌تواند به حفظ ارتباطات و شبکه فرماندهی در عملیات‌های گسترده کمک کند
@WarRoom</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/withyashar/21428" target="_blank">📅 12:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21427">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یک حمله مسلحانه توسط عناصر در شهر زاهدان، واقع در جنوب شرقی ایران؛ بر اساس گزارش‌های اولیه، یک مأمور کشته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/withyashar/21427" target="_blank">📅 12:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21426">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نرخ دلار ۲۰۱،۶۰۰ تومان (رکورد تاریخی)  دلار کف بازار  ۲۰۵-۲۱۰ هزار تومان تتر  ۱۹۹،۹۹۰ تومان(رکورد تاریخی)  بیتکوین ۷۷،۳۷۹ $ انس جهانی طلا ۴.۶۳۶ $ نفت برنت ۹۱.۰۲$ @WarRoom</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/withyashar/21426" target="_blank">📅 12:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21424">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3_GrieD-AgP8ir0-sTq_XDxZx95ruNq53VxKM2-hrqxOOFXKBy4tA0-L9N1I_yX71SNxdoB_Y3tRTO6hVElYayz31NyTIuEQjrVRm59hauN6y37An4mWER8kFiKBrvG5TQFizOFNo6KsIQ-NRyY5KaoRsTuFvWnkoL7y2F4mkXfQkitGRpKbnO1v1nv-6aTH2mev7hpkBKqB1xB1POH8uQIYV5qkU0ZJCaUxWpUynLFMeRW4vexP1bWVnPyQUs07rG3vjbSng6yyLfL7NOK09PtrmePHNYH08Uzck-afuxGETqtutdtHrwd-gT01BpBKBO7o22gpn_Xf5npRugaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcMaVJsogQyRIy2Jgfy-ZVm6thbx_G0L1Vw4VUj9EmF5RaUOuonptIPQcrjEH3Imr4TbQAIVpnG5NjS2g9TjuG0Lw_yNgJlZqLBRKYDrNAe-BKjsGo-EyTcaL1qb5ynK34ti5gMaLilwz7xciXwIXoYrOsEwtIoCZctkF-UCTnz4gDaj6Mk9xjond6EtTq0iZnzxiY32zDI9PX3xwq1-whunCUcBoFWrZh3WpNIYYcvqTFKnRXs0Dfik6Wa_asgEngqZBeFFEV-YHcTj_H5OW8pssVMw25jJK5bG7vOnA7xXQGfBj7K0qN7LPpF68yd-C1fHu2-5X0aw8vozjHC0Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش انفجار شدید در ارومیه ، شدت انفجار در خانه را پرتاب کرده
@WarRoom</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/21424" target="_blank">📅 12:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21423">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الجزیره به نقل از رویترز: فرمانده ارتش پاکستان پیش از سفرش به تهران، با ترامپ تماس تلفنی برقرار کرده بود
@WarRoom
خبر رویترز که سفر کنسل
شده
فیک نیوزه ، خودتون اینترنت دارین چک کنید قبلش نفرستید برام</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/21423" target="_blank">📅 12:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21421">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نرخ دلار ۲۰۲،۶۰۰ تومان (رکورد تاریخی)
دلار کف بازار  ۲۰۵-۲۱۰ هزار تومان
تتر ۲۰۱،۵۰۰ تومان(رکورد تاریخی)
بیتکوین ۷۷،۱۲۴ $
انس جهانی طلا ۴،۶۳۰ $
نفت برنت ۹۱.۴۲$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/21421" target="_blank">📅 12:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21420">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC0S-HnVL-EpkK7WFZcMZxtC1jSY7YfspQmlx4e3zADFFLGtLy95XA1UD5kM9vDf_AvFCdIgKFaKQQF32QJ-95YAzwpYFkda351_zDp1bCCvrN4OPv8KOeDLoAi0w--7UErf0Es5z3QCS7Qf2rwibMa-fqnhphLU3kTneSefW4cCcBZD2S767Mnb_JzytFt9JOeK7pC8UjGUirlBuNot8c65l_OWWEA55G_2GJ7dyCllCXBY7fcQ6kRC1ZZyLxzwQXdgls-nbtIu0XDgRzns_lcuW1L1Dp9F_Ioxh32lcgd9AM-gN4VWhVO73bDzneHm6d5aL4wfNj5Wq1h_vdETcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم منیر به تهران رسید
@WarRoom</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/21420" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21419">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bExDlV4E9Hpihg57udsjYBmd7RVQr3xJvk6GPXbiS98XiLVewOqrZBHdi8_VlO2M5QtvdcxL0B2NradYwMRsdq1VEpMu0_iyaNWzkwkFpUWsArLk9oRzJUIzisbTz0SYi3pqnAVZDNTQIZUsyJNUpsOoaKNCaVEncDtnJXStfsVv8WXzgMsVkbnufnpAvtwtrpOcxPmMikhDX9ZL0kZsnMudVus1qMnGmguOY7IoKz3_8NwLrx4zaSLYuS17JmLQCn5ez0zi3jZ8zxYJuAA3Qp3TW68s17kgH0R36OHla25_eDk-8Ea90eH4C_b_lVBH6a8wTOhvOhJlb6dMLnxfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی : ما از قدیم شطرنج باز بودیم، در سالای اخیر پوکر باز هم شدیم، الان هم مدتیه که ترکیبی بازی می‌ کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/21419" target="_blank">📅 11:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21418">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqg0mzKGWqKoEc7yLe0ynFPaaa7to1AxW69sVgiyXHCOASmX0dKAwFqEX4GRk7qKGthPXRnLmwQIgMBCu6CCPm-ZlrqkxpzZO9QU7rIsYezxM2J-aUesNV7ZanvmdHbrY0fXraKk_-S9b4oZ0dmqMN8ACIYwXpt_LwFLVd9hbPPDRzBKx8r7tWpflGeUC7g8Q5lVyRqpkj-QpQdluzOqJjLjiw5LlwczrComq7PaqLB8skd-50LMkoTA4Gf_b1yaOURBzsAy0wVq3dcUANKyy4bx5byASw-mefATQbvJ2vs9ltwaV6ELacNLjKjXg-C-BYcJYIPnwC-dQdYHVfWu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریای بریتانیا: گزارشی از حادثه‌ای در ۶۳ مایل دریایی غرب ینبع، عربستان سعودی دریافت کرده است.
مسئول امنیتی شرکت گزارش داد که یک تانکر توسط یک پرتابه ناشناخته مورد اصابت قرار گرفته و باعث آتش‌سوزی در عرشه اصلی کشتی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/21418" target="_blank">📅 11:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21417">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نرخ دلار ۲۰۱،۶۰۰ تومان (رکورد تاریخی)
دلار کف بازار  ۲۰۵-۲۱۰ هزار تومان
تتر  ۱۹۹،۹۹۰ تومان(رکورد تاریخی)
بیتکوین ۷۷،۳۷۹ $
انس جهانی طلا ۴.۶۳۶ $
نفت برنت ۹۱.۰۲$
@WarRoom</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/21417" target="_blank">📅 11:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21416">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9bbfIz319v4uAGUvAF6hH3bB6-GWHofQtTp1SrqElyr4b7XKbcGYopAPPHOKo3JySFrklEh94Heg-2F68NaSdFMmSI8yU9W3Eaz9XvS8wzsfm4WwOy1qnAWH2V81d6lefv-CZbkWLGfa3prjWbfqdssAXLVbqlphtHv87wuTt73Icjilje83m5tK90_336mshuMTrctvUwwpsx7c0d0a4PgNongaHCWV4C0F9E3Qk_ISPsdTPuHIebzKkkjOMchDTj8DjqtNpjppmuvT_C1cRPeyD-xGvLe9twULFHiCsWpKRdkK4a12Yi4vq4yIjR68dm0wtuIl7wuOrrMcFI_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/21416" target="_blank">📅 09:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21415">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فایننشال تایمز: اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد واشنگتن وارد «مرحله پایانی» علیه ایران شده
و در حال آماده‌سازی گسترده‌ترین تحریم‌ها برای قطع باقی‌مانده ارتباطات مالی و تجاری تهران است. او هشدار داد کشورها و شرکت‌هایی که به حمایت اقتصادی از ایران ادامه دهند نیز ممکن است هدف تحریم‌های آمریکا قرار گیرند؛ اقدامی که هدف آن انزوای کامل اقتصادی و تشدید فشار بر جمهوری اسلامی است.
@WarRoom</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/21415" target="_blank">📅 09:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21414">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82cd04aaff.mp4?token=h9CfUvfztZMKJBJMQ4w3A0QYT38mpbduB0uqmDy_DHWAJPUvMofqRfTMz9maC9J9A7CZsyQCPiSCqoNNd_7crxGrMLjY0wBPcviNWEOu7D65RuXf-4ET-yCUpJXpRn6ghybAU38P3aqEkDesPS0juVqtPzmY73-d8s-sXOO5h07CjozGIBY9SyP1D1RZoro1HWva8XI1J0YKpCrKNhwVlvYWrPHVmym98s7FoT9edAcFVRkxNIgDAVUePiHggIJ8afbXm0vUr593pFezucWyvII_BqbMS-ITg0lO7GKThRPJKX_Q1OwVyzuJcyBI1ogKLSEEgKFPRAoZSx0F-t9SMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82cd04aaff.mp4?token=h9CfUvfztZMKJBJMQ4w3A0QYT38mpbduB0uqmDy_DHWAJPUvMofqRfTMz9maC9J9A7CZsyQCPiSCqoNNd_7crxGrMLjY0wBPcviNWEOu7D65RuXf-4ET-yCUpJXpRn6ghybAU38P3aqEkDesPS0juVqtPzmY73-d8s-sXOO5h07CjozGIBY9SyP1D1RZoro1HWva8XI1J0YKpCrKNhwVlvYWrPHVmym98s7FoT9edAcFVRkxNIgDAVUePiHggIJ8afbXm0vUr593pFezucWyvII_BqbMS-ITg0lO7GKThRPJKX_Q1OwVyzuJcyBI1ogKLSEEgKFPRAoZSx0F-t9SMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن کج بند رضایی : مردم خودشون در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه باید بکنند. @WarRoom یاشار : یعنی‌کوکتل مولوتوف درست کنند ؟
😂
😂</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/21414" target="_blank">📅 09:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21413">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNskO09tF02Gx-6sHW_0kQfU6TiKlqTM37yGEgiTiEG-IqYem2v2b_HKqfGLXa7I1wr-SvrSvAmTaoODuYBvggpclh1eGv6NQf747uyDpS5P3fTqFJzdJas2IA9D9mlt5SEpHBGrvQJDZG6HZBzwLmbH2quGz01GOxX5t-kFbrLqSgKr1AYGeRD9VftcRAFQqPjzKPL6iGbPw3GOnPeVqnVMQxqR4RTcnQAd8TJ42femRX9bsts9MKm-zLiXBYORZ76y5tL_LC28FqyRdFeqZ7tb0BaToWDlcEhzS7eTwzRAYsIaDRGDQRTW337b3gmUO7OX6ZGnk9KQ8HgA04bZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :از قول ممباقر ،رئیس مجلس ایران: «ما گرسنه‌ایم، نمی‌توانیم زنده بمانیم»نیوزمکس
@WarRoom</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/21413" target="_blank">📅 09:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21412">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281df71e3f.mp4?token=ed6ZaATMekwMgoFj-VnjUMdnuTl1zadjtswExOg_v1QAmHuc7y2Y_F80FAMNYDTkyCAZ24kGN--gSPF2LafsQKO6emC14shnTCvYT8IQGL1_AYgd_7SatNOLl352l6KIroucRHrujaxEI1v5b9VoWKojU5zE8htQRMRpF36jv_VwIYd1cxFPyL7MWcLaSC8lPQz4M98kszazdxdjo1GecbDLYBGvrV3WNgBeQage09v9zp_6rx6Ov7VEnvT813A4pdjbOQW0zkiJIKfDGC_SHveEE6XiGxP2Ktbaz8aqeZGGVIhs3sGUWCt4dQOnkdA8AUUBC7XUArHssvdW4ZrRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281df71e3f.mp4?token=ed6ZaATMekwMgoFj-VnjUMdnuTl1zadjtswExOg_v1QAmHuc7y2Y_F80FAMNYDTkyCAZ24kGN--gSPF2LafsQKO6emC14shnTCvYT8IQGL1_AYgd_7SatNOLl352l6KIroucRHrujaxEI1v5b9VoWKojU5zE8htQRMRpF36jv_VwIYd1cxFPyL7MWcLaSC8lPQz4M98kszazdxdjo1GecbDLYBGvrV3WNgBeQage09v9zp_6rx6Ov7VEnvT813A4pdjbOQW0zkiJIKfDGC_SHveEE6XiGxP2Ktbaz8aqeZGGVIhs3sGUWCt4dQOnkdA8AUUBC7XUArHssvdW4ZrRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر ایران به سلاح هسته‌ای دست پیدا می‌کرد، فکر می‌کنم تمام خاورمیانه از بین می‌رفت و قطعاً اسرائیل نابود می‌شد. آنها به من می‌گویند اگر دونالد ترامپ رئیس‌جمهور نبود، دیگر اسرائیلی وجود نداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/21412" target="_blank">📅 08:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21411">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">روزنامه یونانی کاتیمرینی گزارش داده که آتن پس از تهدیدهای تهران علیه پایگاه‌های آمریکا در اروپا یک سامانه پدافند هوایی Patriot را از کارپاتوس به جزیره کرت منتقل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/21411" target="_blank">📅 08:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21410">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏نیویورک پست با استناد به تصاویر ماهواره‌ای نوشت: فعالیت در قطب صادرات نفت ایران در جزیره خارک تقریبا صفر است.
‏داده‌های کشتیرانی نشان داد که روزهای شنبه و یکشنبه ۱۷ کشتی از تنگه هرمز عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/21410" target="_blank">📅 08:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21409">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏خبرگزاری مهر: آتش‌سوزی گسترده در چندین سوله یک کارخانه تولید چسب و عایق در فرون‌آباد پاکدشت، بامداد دوشنبه به وقوع پیوست و به‌دلیل وجود مواد قابل اشتعال، عملیات مهار حریق با دشواری همراه شد.
@WarRoom</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/21409" target="_blank">📅 08:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21408">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش های‌ زیاد از صدای انفجار بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21408" target="_blank">📅 23:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21407">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مایک پنس: ترامپ و اسرائیل دوباره برای «تمام کردن کار» وارد عمل می‌شوند
به گزارش سی‌ان‌ان : مایک پنس، معاون سابق رئیس‌جمهور آمریکا مدعی است:
«بسیار زود و پیش از آنکه دیر شود زمانش فرا می‌رسد که رئیس‌جمهور و متحد ما اسرائیل مجبور شوند وارد شوند و کار را تمام کنند.»
آمریکا باید نیروها و تجهیزات نظامی خود را در منطقه حفظ کند تا برای اقدام احتمالی آینده آماده باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21407" target="_blank">📅 23:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21406">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اناق جنگ با یاشار : این خلاصه از بهترین ویدیوها از ساعتی پیش که مسابقه شروع شد تا همین دقایقی پیش درست کردم که هیچ جا پیدا نمیکنید.
گرندپری «Freedom 250» در قلب واشنگتن و در مسیر اطراف نشنال مال برگزار می‌شود؛ مسابقه‌ای ۲۵۰ مایلی که نماد ۲۵۰ سالگی استقلال آمریکاست. ترامپ که با فرمان اجرایی زمینه برگزاری آن را فراهم کرد، پیش از آغاز مسابقه با خودرو ریاست‌جمهوری یک دور نمادین زد و پرچم سبز شروع را به اهتزاز درآورد. هم‌زمان، نمایش هوایی گسترده‌ای با حضور بمب‌افکن‌های راهبردی B-2، B-1B و B-52 برگزار شد تا قدرت نظامی آمریکا نیز بخشی از این نمایش ملی و میهن‌پرستانه باشد. هم اکنون ترامپ از جایگاه ویژه در حال مشاهده مسابقه می باشد. البته بیشتر در حال صحبت کردن با اطرافیان است تا این لحظه…
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21406" target="_blank">📅 22:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21405">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جمهوری اسلامی اعلام کرد از امشب هر نفتکشی از مسیر جنوبی تنگه ی هرمز(متعلق به عمان و آمریکا) عبور کنه جریمه میشه و یا خود کشتی توقیف میشه و یا اموال کشتی مصادره میشه.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21405" target="_blank">📅 22:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21404">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شاهزاده رضا پهلوی: قیمت دلار امروز از مرز ۲۰۰ هزار تومان گذشت. امروز قیمت دلار ۲۸٬۵۷۱ برابر زمانی است که جمهوری اسلامی به قدرت رسید. حاصل نزدیک به پنج دهه حاکمیت فساد و ناکارآمدی در جمهوری اسلامی، فقر، فساد و انزوا برای ملت ایران بوده است. تجربه این پنج دهه یک مسئله را برای همه روشن کرده است: در جمهوری اسلامی اصلاح ممکن نیست. قطار ایران در بهمن ۵۷ از ریل تمدن و پیشرفت خارج شد و امروز جمهوری اسلامی آن را با سرعت هرچه بیشتر به ته دره هدایت می‌کند. امروز وظیفه تک‌تک ایرانیان، از جمله کارمندان دولت و بدنه اداری کشور، این است که به هر شکل ممکن با اخلال در فعالیت‌های مخرب جمهوری اسلامی و تضعیف آن، زمینه برکنار کردن رژیم و نجات ایران را فراهم کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21404" target="_blank">📅 22:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21403">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مایک جانسون، رئیس مجلس نمایندگان آمریکا، به فاکس‌نیوز گفت آمریکا در حال ورود به مرحله جدیدی از جنگ علیه ایران است و دولت ترامپ همچنان به‌دنبال پایان دادن به جنگ است.
او گفت تمرکز مرحله بعدی بر
فشار اقتصادی و تحریم‌های شدیدتر
خواهد بود و دولت آمریکا می‌خواهد با افزایش فشار، تهران را به پذیرش یک تسلیم وادار کند. جانسون همچنین گفت ترامپ «شبانه‌روز» برای حل‌وفصل جنگ تلاش می‌کند. این اظهارات هم‌زمان با اعلام اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره اعمال
«سخت‌ترین تحریم‌های تاریخ» علیه ایران
مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21403" target="_blank">📅 21:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21402">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d23c54da.mp4?token=Rg9qwhoGYttfu1-wBR9VRIvkitfYD9G73QE7W8laU48BK7nArjSOxt1ZrdrzXCl_Nkfg_71HPgIFapodxtOSsrLdgls-xyw43WR-m8Bs8Z5AgXXvR7ElwrOrUpsQhkQycTFebiQ6bn3Vw20ct2107mQAnYFHMwlEYI3JyuQONF9emzgndNtQL-eDMxftc5tVcqYF5-y5B5hZGqoONmbgOZm1RMYuS7c0l94OG0TTO28VjOfjvqolBGjnfODvFUUBp0HUEtXZzmcyXJwI9_xlYJ6p5scm5ZLLlQ6HziB7e0KtFpj2FCmzHTHFkc83JRvn5yOE4V5qKFFNWyp9WzJr7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d23c54da.mp4?token=Rg9qwhoGYttfu1-wBR9VRIvkitfYD9G73QE7W8laU48BK7nArjSOxt1ZrdrzXCl_Nkfg_71HPgIFapodxtOSsrLdgls-xyw43WR-m8Bs8Z5AgXXvR7ElwrOrUpsQhkQycTFebiQ6bn3Vw20ct2107mQAnYFHMwlEYI3JyuQONF9emzgndNtQL-eDMxftc5tVcqYF5-y5B5hZGqoONmbgOZm1RMYuS7c0l94OG0TTO28VjOfjvqolBGjnfODvFUUBp0HUEtXZzmcyXJwI9_xlYJ6p5scm5ZLLlQ6HziB7e0KtFpj2FCmzHTHFkc83JRvn5yOE4V5qKFFNWyp9WzJr7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : از زمان ازسرگیری محاصره دریایی علیه ایران، مسیر ۷۰ کشتی تغییر داده شده و فعالیت ۳ کشتی دیگر نیز متوقف شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21402" target="_blank">📅 21:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21401">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">واشنگتن پست : تعداد مجروحان آمریکایی در جنگ با ایران به 774 نفر افزایش یافته است. این آمار شامل 18 کشته و 756 مجروح است. طبق داده‌های وزارت دفاع آمریکا، حدود 60 مورد جدید از جراحات در روزهای اخیر ثبت شده است، که شامل آسیب‌های جدی مغزی ناشی از انفجارها در حملاتی است که پایگاه‌های آمریکایی در منطقه را هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21401" target="_blank">📅 20:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21400">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نتانیاهو: ما به شرایط قبل از ۷ اکتبر باز نخواهیم گشت و اجازه نخواهیم داد هیچ گروهی در غزه به شهرها و مناطق اسرائیلی تهدید کند یا امنیت را تضعیف نماید.اگر حماس فوراً از پرتاب بالن‌ها و برگزاری تظاهرات‌ها خودداری نکند، هدف قرار دادن مسئولان این اقدامات را تشدید خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21400" target="_blank">📅 20:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21399">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سخنگوی دولت : خبر خوش برای مردم، سود سهام عدالت (۲-۳ دلار) از 2 تا 8 شهریور واریز میشه
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21399" target="_blank">📅 20:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21398">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اورشلیم پست گزارش داده است که اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه ۲۴ اوت در یک نشست خبری جزئیات برنامه جدید دولت ترامپ برای تشدید فشار اقتصادی بر ایران را اعلام کند. این نشست ساعت ۲ بعدازظهر به وقت شرق آمریکا برگزار می‌شود که با توجه به…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21398" target="_blank">📅 19:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21395">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اکسیوس: وزیر خارجه سوریه، اسعد شیبانی، امروز یکشنبه با رئیس سازمان اطلاعاتی اسرائیل (موساد)، یوآو گالفمن، دیدار کرد تا تلاش‌هایی برای کاهش تنش بین دو کشور صورت گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21395" target="_blank">📅 19:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21394">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21394" target="_blank">📅 19:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21393">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21393" target="_blank">📅 19:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21392">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بی بی نتانیاهو الان این شماره رو گذاشته  مردم زنگ بزنند اگه عبری بلدید صدای مردم ایران باشید
+972544700047
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21392" target="_blank">📅 18:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21390">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60dddfa42.mp4?token=irlMmnkPdlPmLwQstZkNX5-HifNoCZpb9qebKH5o2aKy4B6HMNQn10YRISrp4YEBroMM5bO_kgv67jlxoEBtKtTZ0T5TmFZMgYVpM9EgOdPJ0DlxGtK-qQuZX0_KI9g9TL_QunYeQLkLhIC0BMFibbHs8nO8EkWXmMvhYjjrLG_RcIg_uGi66NgWaWPXbdADW_4Nvfb8NIZnP_6s3ISFXv0Cw4Ccg6xs2ZRPah5KRimZk7c50xztHZK2opcimmY46rtJpilU8PJ8YLEowTsTUbWfqvHrih_VIYcv95nDViPWZ_U3Xn2bNvLCTmdpjzkgkCLJLnU3JoEoZvCwEaRioRB7a62YNHuN6ti2BQqhsiAIaJUpmNoXaShRs3LCggBdhba6rv_l0PsC3nK2VGSo9ykoGxxvlQpP5AvxPX6m9uY7iwWk62MlMU7J4q3WMNLMKEsGdwcofK0Nx0Ncxtrz9EtnbThMlE_Bwb3o3p5D7hjj2ii0gsiBmMhH6HHzVmG53QtBYifswhcm318S1fF4GI4CDhV23yfddd01fVk2tNbkc_19zUzLj_mimfzHWKrugd5Z6Nw-RsYVkQ261MYlZLKZbY7AKYA_eoO-KysdqxWDRiRgmvKrpy71qtRcpmh62Vp3-w_nsJJgmR7ppFTZ5oEgNsiwu-0W-_OFKhdPTAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60dddfa42.mp4?token=irlMmnkPdlPmLwQstZkNX5-HifNoCZpb9qebKH5o2aKy4B6HMNQn10YRISrp4YEBroMM5bO_kgv67jlxoEBtKtTZ0T5TmFZMgYVpM9EgOdPJ0DlxGtK-qQuZX0_KI9g9TL_QunYeQLkLhIC0BMFibbHs8nO8EkWXmMvhYjjrLG_RcIg_uGi66NgWaWPXbdADW_4Nvfb8NIZnP_6s3ISFXv0Cw4Ccg6xs2ZRPah5KRimZk7c50xztHZK2opcimmY46rtJpilU8PJ8YLEowTsTUbWfqvHrih_VIYcv95nDViPWZ_U3Xn2bNvLCTmdpjzkgkCLJLnU3JoEoZvCwEaRioRB7a62YNHuN6ti2BQqhsiAIaJUpmNoXaShRs3LCggBdhba6rv_l0PsC3nK2VGSo9ykoGxxvlQpP5AvxPX6m9uY7iwWk62MlMU7J4q3WMNLMKEsGdwcofK0Nx0Ncxtrz9EtnbThMlE_Bwb3o3p5D7hjj2ii0gsiBmMhH6HHzVmG53QtBYifswhcm318S1fF4GI4CDhV23yfddd01fVk2tNbkc_19zUzLj_mimfzHWKrugd5Z6Nw-RsYVkQ261MYlZLKZbY7AKYA_eoO-KysdqxWDRiRgmvKrpy71qtRcpmh62Vp3-w_nsJJgmR7ppFTZ5oEgNsiwu-0W-_OFKhdPTAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جنگ اخیر کی بیشترین پول رو در آورد ؟!
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21390" target="_blank">📅 18:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21389">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کمیسیون امنیت ملی جمهوری اسلامی:
دریافت هزینه خدمات از کشتی‌های عبوری از تنگه هرمز تصویب شد‌.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21389" target="_blank">📅 18:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21388">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a2f95843.mp4?token=agShzAAwLDohp3fETIugH-B2kPJ-blNjo1__iIuZqEIesFg4764lEJbjzmLgWclbr397W4qqyZDXxvTK6Kn2x1FTJ6kUPcToNF7VBBKw8M-Su9zS2qrjDWalpRgJWMBH3e4PapT6S6Hf4nInAueH4IYMRg-RMiWszlwAex9FKNdxJdUANvIc0gXMPZogGJnmBm7ulPyYPy8B_KDNnUTNthuTaSNBSZ1BBzUaLjibuHPbF4pz1HZNqUgSkDeZPwmjl_3Vuvlm3NsZ5pjjYLuHuM2nUxNjqpQyLPZMv0Nt2jrTtsL_niyorFZvRGn8h6MzsJpnDQL7k_VAYEBC6QPHaIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a2f95843.mp4?token=agShzAAwLDohp3fETIugH-B2kPJ-blNjo1__iIuZqEIesFg4764lEJbjzmLgWclbr397W4qqyZDXxvTK6Kn2x1FTJ6kUPcToNF7VBBKw8M-Su9zS2qrjDWalpRgJWMBH3e4PapT6S6Hf4nInAueH4IYMRg-RMiWszlwAex9FKNdxJdUANvIc0gXMPZogGJnmBm7ulPyYPy8B_KDNnUTNthuTaSNBSZ1BBzUaLjibuHPbF4pz1HZNqUgSkDeZPwmjl_3Vuvlm3NsZ5pjjYLuHuM2nUxNjqpQyLPZMv0Nt2jrTtsL_niyorFZvRGn8h6MzsJpnDQL7k_VAYEBC6QPHaIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زامبی ؟ بدترشه ، نسل ۵۷
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21388" target="_blank">📅 17:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21387">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بنیامین نتانیاهو:
«پهپادهای کوچک می‌توانند بسیار مرگبار و دقیق باشند و به‌سختی دیده شوند. ما سال‌هاست روی مقابله با این تهدید کار می‌کنیم و آن را در اوکراین، لبنان و ایران دیده‌ایم. حالا تلاش می‌کنند این تهدید را دوباره احیا کرده و وارد غزه کنند. دستور من به دستگاه امنیتی و ارتش اسرائیل این است که
خود پهپاد، اپراتور آن و محل شلیک یا پرتابش را هدف قرار دهند و هر کاری لازم است برای محافظت از شهروندان اسرائیلی انجام دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21387" target="_blank">📅 17:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21386">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">میدل ایست آی: ده‌ها پایگاه اروپایی در جریان جنگ ۴۰روزه از عملیات آمریکا علیه ایران پشتیبانی کردند؛ بریتانیا احتمالاً مهم‌ترین حمایت را ارائه داد و پایگاه‌ها و زیرساخت‌های نظامی آن، از جمله دیه‌گو گارسیا، در پشتیبانی از عملیات آمریکا مورد استفاده قرار گرفتند. فرانسه نیز به هواپیماهای نظامی پشتیبانی آمریکا اجازه فرود و استفاده از پایگاه‌های خود را داد. بلغارستان هم اجازه استفاده آمریکا از فرودگاه‌ها و خاک خود را صادر کرد و به این ترتیب، با وجود مواضع متفاوت برخی دولت‌های اروپایی در قبال جنگ، زیرساخت‌های نظامی کشورهای مختلف اروپا در پشتیبانی از عملیات آمریکا علیه ایران نقش داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21386" target="_blank">📅 16:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21385">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیویورک پست
: در هفته گذشته حدود 200 کشتی چراغ خاموش از تنگه هرمز عبور کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21385" target="_blank">📅 15:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21384">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دیجیکالا از دسترس خارج شد تا بعدن بتونه گرونتر بفروشه
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21384" target="_blank">📅 15:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21383">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">یاشار داش دلار تو بازار من الان 210 چنج کردم</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21383" target="_blank">📅 15:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21382">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏دونالد ترامپ در‌تروث با انتشار ویدیویی جنجالی از سخنرانی خود، به انتقاد شدید از تلاش‌های حزب دمکرات برای محدود کردن اختیارات نظامی رئیس‌جمهور آمریکا پرداخت.
‏او در این اظهارات طعنه‌آمیز گفت : اگر علی خامنه‌ای در حملات کشته نمی‌شد، دمکرات‌ها احتمالاً او را برای ریاست‌جمهوری سال ۲۰۲۸، سنای میشیگان یا حتی مدیریت کمیته ملی دمکرات‌ها (DNC) نامزد می‌کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21382" target="_blank">📅 14:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21381">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حمله هوایی اسرائیل به غزه
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21381" target="_blank">📅 14:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21380">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دلار کف فردوسی ۲۰۱،۰۰۰ تومان
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21380" target="_blank">📅 14:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21379">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دلار ۱۹۹.۰۰۰ تومان (رکورد تاریخی)  تتر  ۱۹۷.۰۰۰ تومان (رکورد تاریخی)  بیتکوین ۷۶.۶۱۶ $ انس جهانی طلا ۴.۶۰۲ $ (آخرین قیمت) نفت برنت ۹۳.۹۹$ (آخرین قیمت) @WarRoom ساعت ۱:۳۰ دقیقه تهران</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21379" target="_blank">📅 14:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21378">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دلار ۱۹۹.۰۰۰ تومان (رکورد تاریخی)
تتر  ۱۹۷.۰۰۰ تومان (رکورد تاریخی)
بیتکوین ۷۶.۶۱۶ $
انس جهانی طلا ۴.۶۰۲ $ (آخرین قیمت)
نفت برنت ۹۳.۹۹$ (آخرین قیمت)
@WarRoom
ساعت ۱:۳۰ دقیقه تهران</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21378" target="_blank">📅 13:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21377">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حبس مهریه بالای ۱۴ سکه حذف می شود
نماینده نجف‌آباد در مجلس اعلام کرده طرح اصلاح نحوه اجرای محکومیت‌های مالی در صحن علنی تصویب شده و بر اساس آن، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف می‌شود.
برای مهریه‌های زیر ۱۴ سکه نیز امکان اجرای حکم با استفاده از پابند الکترونیک پیش‌بینی شده است.
این مصوبه برای بررسی و تأیید نهایی به شورای نگهبان ارسال شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21377" target="_blank">📅 13:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21376">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رسانه های کره شمالی : دولت کره شمالی اعلام کرده است که قصد دارد توافق دفاعی با ایران امضا کند. در صورت نهایی شدن، این اقدام می‌تواند منجر به تعمیق همکاری‌های نظامی بین پیونگ‌یانگ و تهران شود. این توافق بالقوه در بحبوحه تنش‌های جاری بین ایران، ایالات متحده و اسرائیل مطرح شده
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21376" target="_blank">📅 13:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21375">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صداوسیما در اقدامی ، اطلاعات به ادعای آنها محرمانه و مکان‌های دقیق تردد پسر ترامپ و نقاطی که در تیررس است را منتشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21375" target="_blank">📅 12:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21374">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بامداد امروز یک شهریور، کارخانه‌ نوشابه‌سازی ایرانشهر طی حادثه‌ای در آتش سوخت. هنوز از میزان خسارت‌های مالی اطلاعات دقیقی منتشر نشده است. مسئولین این واحد تولیدی در حال پیگیری این ماجرا هستند. @WarRoom عمو نوشینیاهو ، بی بی کولا</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21374" target="_blank">📅 12:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21373">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رسانه های عربی : ارتش اسرائیل (IDF) مدتی پیش به ساختمان‌های متعلق به گروه‌های تروریستی در روستای زوتر الشرقیه و حداتا در جنوب لبنان حمله کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21373" target="_blank">📅 12:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21372">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دلار ۱۹۶،۴۰۰ تومان (رکورد تاریخی)
دلار بازار آزاد ۲۰۰،۰۰۰ تومان
تتر  ۱۹۵.۳۶۰ تومان
بیتکوین ۷۶،۲۳۷ $
انس جهانی طلا ۴.۶۰۲ $ (آخرین قیمت)
نفت برنت ۹۳.۹۹$ (آخرین قیمت)
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21372" target="_blank">📅 11:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21370">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_dvkpquqOxZ2tIgjJZKZNP79v0_kJFW5V71dHqvpp2EM8DTUcqYslVjqoNcLTY8S5X5BpChBglrD9xP50cGDpLsxqyJXonmkHXe8lXZcOcwKFPsmR6X3-NTA0CWx3Pw2AiDCbVYWbOCw41Al0cfT4NjS6Ml5EqV_mW1tujIcnbhAxH3Gn72amOcDUTo6kUlzpaDTE8YhjyGVY8Yiac7t7ajuhyAlGiUp57ihZQHwiscwFakvg5T22qSWSq_lMUFExPuqmLFdP4iK3o_h94pNJkqIcJh-MbC2phU_iDHuLy_iBC-o-o7d5W_wEYSuIW3T3-MgJM5WFmqPq70fgNNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بامداد امروز یک شهریور، کارخانه‌ نوشابه‌سازی ایرانشهر طی حادثه‌ای در آتش سوخت.
هنوز از میزان خسارت‌های مالی اطلاعات دقیقی منتشر نشده است.
مسئولین این واحد تولیدی در حال پیگیری این ماجرا هستند.
@WarRoom
عمو نوشینیاهو ، بی بی کولا</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21370" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21369">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزیر امور خارجه سوریه:پیش‌بینی می‌کنم که به زودی مذاکرات با اسرائیل در مورد یک توافق امنیتی از سر گرفته شود. ما دست دوستی دراز می‌کنیم و از اسرائیل می‌خواهیم که از این فرصت تاریخی استفاده کند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21369" target="_blank">📅 11:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21368">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">العربیه: فرمانده ارتش پاکستان، عاصم منیر، روز دوشنبه با پیام‌هایی از آمریکا به تهران سفر می‌کند.
این سفر در چارچوب تلاش‌های پاکستان برای شکستن بن‌بست دیپلماتیک ایران و آمریکا و از سرگیری مذاکرات پس از ناکامی دو طرف در دستیابی به توافق نهایی درباره پرونده هسته‌ای و تنگه هرمز انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21368" target="_blank">📅 11:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21367">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ4Y0mnqtr5W8Wlobn1m5dXl4QxrGg8hWiRCygl-uJTWQBAsSrWVrr_bAZn1O5EbVvt8BT9rvqnPjq0sWAyHnCyWUJRa_dUKaRRoCEqU0JnyGzP7AxCoAI6bDYyNsfbo2D_aLEU4EX4DUaLWuYdgkVLTo5MjQBxbXr1Ez-fTqvEQajmIduJ_rY6pjxNlCVdQ_0wvco4AvSgz9KXEbQwqNjEtL3d-SrObwj_Bh8ASv6vYqn57LweunaHaLD6BlGqH1VcgXXEWdRznUiqzx7fd2a1tppISKxLj0ezYz8-dlHfCTFM5fToM6yHnCXfWCm_dMd95xrcOW7D3cYdFg50wIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهده دایناسور در مناطق بیابانی خراسان رضوی تکذیب شد
دبیر شورای اطلاع رسانی اداره کل حفاظت محیط زیست خراسان رضوی
:
طی روزهای اخیر تصویری در شبکه‌های اجتماعی دست ‌به‌ دست می‌شود که موجودی شبیه دایناسور را در محیطی بیابانی در شهرستان بینالود نشان می‌دهد.
تصویر مذکور کاملاً مصنوعی، تولید شده توسط هوش مصنوعی و فاقد هرگونه واقعیت میدانی است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21367" target="_blank">📅 11:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21366">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">روزنامه تلگراف بریتانیا : هکرهای ایرانی یک حمله سایبری بی‌سابقه به یک نیروگاه در بریتانیا انجام دادند که منجر به از کار افتادن آن به مدت ۴ روز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21366" target="_blank">📅 11:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21365">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96ca1be3f.mp4?token=CD4jPW2uYUKH7VMdZlM2wB9RAZ3H6FYrXmWhA9stiUimzmuDi4ELtXAjDzPHZCH-hKFvK3IH1GPFEDlw4hzteA6ay4DXsuDH8Ul23283_IxAR1616hPs1IWnIm2c9IpwxEIzuf8hnNA6PiHVBRFQliuJl-15zNw6jxBtq5Sn633CslSgnf2Ak0gKssAPxQwInE1oHYIASZ3Qo1uUfHshNUdz70zGIwoaQSDhvUyZ62cKSoP3aYi6ufYcgAD3sP4_0vbwiEYoLtvLwP1Xy25dI4-JeBBYv87J6pwODKf8Myc54X6SPMsGj6IUNyiNp3mukDYge24YCnSSRZwKBTR7FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96ca1be3f.mp4?token=CD4jPW2uYUKH7VMdZlM2wB9RAZ3H6FYrXmWhA9stiUimzmuDi4ELtXAjDzPHZCH-hKFvK3IH1GPFEDlw4hzteA6ay4DXsuDH8Ul23283_IxAR1616hPs1IWnIm2c9IpwxEIzuf8hnNA6PiHVBRFQliuJl-15zNw6jxBtq5Sn633CslSgnf2Ak0gKssAPxQwInE1oHYIASZ3Qo1uUfHshNUdz70zGIwoaQSDhvUyZ62cKSoP3aYi6ufYcgAD3sP4_0vbwiEYoLtvLwP1Xy25dI4-JeBBYv87J6pwODKf8Myc54X6SPMsGj6IUNyiNp3mukDYge24YCnSSRZwKBTR7FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت من وقتی یه شب دیگه هم باز نزد !
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21365" target="_blank">📅 03:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21364">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLadan</strong></div>
<div class="tg-text">ترامپ فعلا داره با کانادا کل کل میکنه. توی کانادا همه از دستش کلافه شدن، دیوانه باعث شده وضع خراب بشه و همه چی گرون شده بیش از حد</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21364" target="_blank">📅 02:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21363">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چرا خبری نیست ، ترامپ آخر هفتست شلکس‌ کرده
😁</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21363" target="_blank">📅 02:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21362">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDvo3JUyXMpSCh_a3wHBPtrrUjodcpLu52PgV0D1yD6OWl73HZT52dg916xwCitQbS6J6ydo1YmXxKpB20v8hIYb183P1dF7K8vHz17kjZSWSN8VpPln4ysXTxheeALMU2PERjiTeHCwfIoLxJMRRrHWlJLWZ89G30bjlwTgtN9YRtFY9hoG1mjDRmHNmio-7-Im1LY5aqPZroRc4J3qL47F1TykggQEYFeyeLsEtStfHgE1t3iPNuQUy7teH2tl2vCcbt89AY7DBW0tYmbde3YVX2PsGcNf_G-JL2xfT-cV4dACOlqNm9uvO-PQrjnq7O3EDEuf0hZ02sTMDLjFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث دوباره انتشار داد : قلمرو جدید ایالات متحده : تنگه هرمز.
مقامات کاخ سفید بار اول که این پست منتشر شد به رسانه‌ها گفته بودند هدف رئیس جمهور از این پست شوخی است. خود ترامپ امروز به فاکس نیوز، از لفظ در حال حاضر تنگه برای‌ماست استفاده کرده و با توجه به نوشتن نام خلیج فارس، کاملاً مشهود است که این پست خطاب به حاکمان رژیم جمهوری اسلامی است و به آنها نشان می‌دهد تا زمانی که آنها هستند کنترل تنگه در دست آمریکا است .
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21362" target="_blank">📅 00:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21361">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LALNfoCaDvjYh0RP6-eBQfoBI0arDy-7foeP7lg_46QVFSzICuq6QVewt6gNQyYgGS1m-zGP5Uw7FoOoqzqE7i-eXnDdTOCUsijCUsv60dV0QI0vru44RZlZmss9ZbpZtvX6VirZ104LYxTuc1ZrwcC2kkTX7k1QnfXaBCbIgMu3wMYbT9USdsXzohsbCj57xsRCU8NWjJIFtQoUakVyRPxi-wf5CVevhDJoIYCxBnGLqATU8hTXzABd031Bilap1156BbYD7n5cuW8PCAzpcQ5ksfi2aZRNaH-r56An_c3V6ntxHA3dKgNfdj1WnPh-Rcrr6_YrwB7vOQudxK1hJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن کج بند رضایی : مردم خودشون در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه باید بکنند. @WarRoom یاشار : یعنی‌کوکتل مولوتوف درست کنند ؟
😂
😂</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21361" target="_blank">📅 00:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21360">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">الان ما تخم مرغ لازم داریم چطوری تخم بزاریم. یه امار بگیر اگه کسی بلده به مام یاد بده</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21360" target="_blank">📅 00:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21359">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">محسن کج بند رضایی : مردم خودشون در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه باید بکنند.
@WarRoom
یاشار : یعنی‌کوکتل مولوتوف درست کنند ؟
😂
😂</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21359" target="_blank">📅 23:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21358">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d5b2a1a8.mp4?token=JgrSKmt1mrIf8_3McJbqXd2cgHpqZ1OZckYurXwvBnR_j5ql-thPmlYQXygb3pyYVfrim0ipMb-SOfRpaZUDkO_R9sH77XGGwbl7bUHMfoGgNJDefN5VwSGALF7y4vDbMTecROrFcvG9tZ6ApCmWsSp0BhAnwN-3wg7QFn1LeUsd0nObLbLXVUekaD36TcmnzB1-R3HJp8sNwB7QvnqJboPcYtc-DIB640sCbal4AnkXb8AJUHo_Fvvo0J8zlowrgAwTm-f7AFK6xMgJhRdEnSlPPhddVquePvBP2tmFK5GIV-53YT0WongHxI0G5Vj5w5fVyP62QlOGP5APTD38cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d5b2a1a8.mp4?token=JgrSKmt1mrIf8_3McJbqXd2cgHpqZ1OZckYurXwvBnR_j5ql-thPmlYQXygb3pyYVfrim0ipMb-SOfRpaZUDkO_R9sH77XGGwbl7bUHMfoGgNJDefN5VwSGALF7y4vDbMTecROrFcvG9tZ6ApCmWsSp0BhAnwN-3wg7QFn1LeUsd0nObLbLXVUekaD36TcmnzB1-R3HJp8sNwB7QvnqJboPcYtc-DIB640sCbal4AnkXb8AJUHo_Fvvo0J8zlowrgAwTm-f7AFK6xMgJhRdEnSlPPhddVquePvBP2tmFK5GIV-53YT0WongHxI0G5Vj5w5fVyP62QlOGP5APTD38cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتشبازی برای اجرای‌حکم عروسکهای نتانیاهو و ترامپ بود
😂
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21358" target="_blank">📅 23:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21357">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش های زیاد از انفجار در تهران سمت انقلاب فعلا میترسم یهو میگن جشن امام ۱۸ ام بوده
😂
فقط بدونید @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21357" target="_blank">📅 23:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21356">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET3odEiWBhqe_MFm8ERodacVlAn8Jjru9ycZqOVOTojZ4YDvIyTx7VwZR7qjRiC_NqKg8JoVXxC2dT-WoGWfOWIqFeSE0c7I2tqgoCHu5eVcicWVCN81lGV3uCT2SPomHfXJurut78HAXNqndluV6s78yBQXr-uX1Oq14zZ95_t4oirCUvYpAvxwKwx0a96Be9lI-90dMeq-uv8h0bAgHn0NznZjsl6HgdzMcMVJPdYktXAPb_aZfBicx7dNl8MV8VFF7C6mvIHvs5yhrh5Dk-CmJ4ukBiWNhhNC9y4dQr1IG_KYByOlQ6oNSz6-86iZeAiLri9itg31ROxqX877mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش های بسیار زیاد ، ستون دود تهران از زاویه دیگر
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21356" target="_blank">📅 23:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21355">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b588a12e.mp4?token=eBkCaM5PsqtvBjsE5skifTK55wh2G1VNJde2zkUD-viAOkMnLBNohUUnqtGDTp1j-NwvVmryZkIPMAnoddkTq72X-XnuTRHDstpbTsHiYFG4oRahFGl1UedDWrA3L_iHhKvowGaLVwHme9Pig_5LH58rlvHwmVaYoy02QmEEF44lSeAn3ExC3ZDOP9pGLhu7j93dUksetK4uRKZcmemi5oq5h0Ny8M4PQQDejALJpcDkLGiDWeRrBpr8YxRb5J9T8WBDMofk9SKPJ-RSvECpbe-hyIkjKgrKtKUcc1iXJra7r1MJmPP09Zk6X0nySvFamOicqIU8enIxSfwTyuG2vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b588a12e.mp4?token=eBkCaM5PsqtvBjsE5skifTK55wh2G1VNJde2zkUD-viAOkMnLBNohUUnqtGDTp1j-NwvVmryZkIPMAnoddkTq72X-XnuTRHDstpbTsHiYFG4oRahFGl1UedDWrA3L_iHhKvowGaLVwHme9Pig_5LH58rlvHwmVaYoy02QmEEF44lSeAn3ExC3ZDOP9pGLhu7j93dUksetK4uRKZcmemi5oq5h0Ny8M4PQQDejALJpcDkLGiDWeRrBpr8YxRb5J9T8WBDMofk9SKPJ-RSvECpbe-hyIkjKgrKtKUcc1iXJra7r1MJmPP09Zk6X0nySvFamOicqIU8enIxSfwTyuG2vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای انفجار و ستون دود تهران ، دقایقی پیش
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21355" target="_blank">📅 23:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21354">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBD1MaPfX9H5ZDzN68Ha6FKwlAI3NXxewPeA9HIQXqAqVtRS_P25wG81Fv9zMXo5J9rXKezzftdMfZjs8MxDmGFZunH-vhU36xWIcwjU1mk0d1T7rteoJj9Zhcje60feqq5_kIVzMcsBgHm8iABcs6Ka_r8IRi0h_jX__gd2muhAkV4mMLJrCYq4glkD163QmbodYpVZRE1UkOW0AuKCB0-z4Q4n7RDOydXdB68ifUI940lXmHJAZMANgAslmvO1II4ge5RTmRwmWk6vxCAYk1YzR8Rgoe8Y-9ePOJeEt5dBjhavQTX-Ymf73cZ6FICwMgYas8IGD8whEBjc4IN2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم دودش ولی احتمالا بخار مال خشکشویی عمو خشکخشکیاهو است
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21354" target="_blank">📅 23:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21353">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش های زیاد از انفجار در تهران سمت انقلاب فعلا میترسم یهو میگن جشن امام ۱۸ ام بوده
😂
فقط بدونید
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21353" target="_blank">📅 23:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21351">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">موشک های کروز ضد کشتی به سمت کشتی های بدون مجوز در تنگه هرمز شلیک شده @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21351" target="_blank">📅 23:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">محسن کج بند رضایی : ما با عمان روی مسیر تنگۀ هرمز توافق کردیم که یک مسیر میانی است اما این موضوع روی کاغذ است و تنگۀ هرمز زمانی باز می‌شود که آمریکایی‌ها به تعهداتشان عمل کنند
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21350" target="_blank">📅 23:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21349" target="_blank">📅 23:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش های زیاد از صدای تیر اندازی در شهر اندیشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21348" target="_blank">📅 22:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21347">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محسن کج بند رضایی: در صورت ادامه محاصره اقتصادی شرکت های اقتصادی آمریکا را در منطقه خواهیم زد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21347" target="_blank">📅 22:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21346">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر اقتصاد جمهوری اسلامی : احتمال انحلال چندین بانک در ایران وجود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21346" target="_blank">📅 22:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آغاز موج جدید سنگین حملات هوایی اسرائیل به جنوب لبنان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21345" target="_blank">📅 22:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش های بسیار از صدای انفجار مهیب از تنگه  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21344" target="_blank">📅 22:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اورشلیم پست گزارش داده است که اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه ۲۴ اوت در یک نشست خبری جزئیات برنامه جدید دولت ترامپ برای تشدید فشار اقتصادی بر ایران را اعلام کند. این نشست ساعت ۲ بعدازظهر به وقت شرق آمریکا برگزار می‌شود که با توجه به…</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21343" target="_blank">📅 21:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21342">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش های بسیار از صدای انفجار مهیب از تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21342" target="_blank">📅 21:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانال 14 : تهران آماده است تا فهرست اهداف خود را گسترش داده و شبکه‌ها و تأسیسات انرژی منطقه‌ای را فراتر از مرزهای دریایی تنگه هرمز هدف قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21341" target="_blank">📅 21:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو: تا زمانی که من نخست‌وزیر هستم اجازه نمی‌دهم هیچ کشور فلسطینی تحت کنترل ایران تشکیل شود
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21340" target="_blank">📅 21:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21339">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QELs6r6F5lqkHZ5mc0egM_Yn1g9HQ3Hv0uacCGABKFfleQUreCaXNNdDK-UDMgkFcObOui_KIGey_ohNyhHdtncgpaQCPlIe7X1gHJNXe-XQro6LewpGXaKsu6mTyAajLGVqCw-215jAeT3M8ddVVE5YBVX7feQRx7OIF7VvoT7nwESWYFvNXRSi8u2T41wn4Uh5HrHxwdjFXmgXisqWp0qlqaon6h7PyvEiPycj4E9njHuL_IHQcRdskv8i5LnR8UUb-Jd6_2991J76HFGCeOXOVc9-4MDyo1LxKBdZDf6Q_l6aIbQPm_eSW-DYHkv2-MwYwJD812P8debeBzh1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل
یک فرمانده گروهان را که حملات تروریستی را هدایت می‌کرد و در تلاش‌ها برای بازسازی زیرساخت‌های زیرزمینی حماس شرکت داشت، از بین برد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21339" target="_blank">📅 20:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21338">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جروزالم پست در یک یادداشت دیدگاه هشدار داده است که اسرائیل باید گسترش نظامی ترکیه در سوریه و شرق مدیترانه را یک تهدید راهبردی جدی تلقی کند. نویسنده با اشاره به حمله اخیر اسرائیل به پایگاهی نزدیک ادلب، مدعی است
ترکیه در حال ایجاد سامانه راداری و پدافندی در آن منطقه بوده است
. او با استناد به هشدارهای کمیسیون ناگل، حتی احتمال تبدیل‌شدن تهدید ترکیه و سوریه به خطری بزرگ‌تر از ایران را مطرح می‌کند و خواستار تقویت نیروی دریایی اسرائیل و تعیین خطوط قرمز برای آنکارا شده است. در پایان نیز با لحنی بسیار تند می‌نویسد:
«از ادلب تا استانبول، اسرائیل در صورت لزوم حمله خواهد کرد، نه دفاع.»
این موضع، دیدگاه نویسنده مقاله است و اعلام رسمی دولت یا ارتش اسرائیل نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21338" target="_blank">📅 19:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21337">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeWRwCI__9ijb4gNHPNgOf_Z5ZvRVvFbZ3J4B1YmIqOJ_EcKAZTrf07xxliBmAwvK125EOuaTlURHgV-sjtC7wSQCUqAf3m6eNfk7PpXBpuZSfDsrwCAl57x0-gxH6k28QuKpDnJbtTCwpT3vY5AV7wqmwNwx5pWEFhbuSYfm2g9Jm7OIc4_akghYz42vlVPcICZGC3egZ16femLz7yUJV3FuKK9IlLEO0z0SZfpsOjv4P81Mu0VQk71UTcMhvPit0Mt8Cm6f7EHvvbKMaD3Ci8nPZzevOehTeGvuKuTu_gy05_hclGF_iuLk3tzh8NaASRdsJRds2OmDPzrsGZNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورشلیم پست گزارش داده است که
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه ۲۴ اوت در یک نشست خبری جزئیات برنامه جدید دولت ترامپ برای تشدید فشار اقتصادی بر ایران را اعلام کند
. این نشست ساعت ۲ بعدازظهر به وقت شرق آمریکا برگزار می‌شود که با توجه به اختلاف زمانی فعلی
، برابر با ۹:۳۰ شب دوشنبه به وقت تهران است.
بسنت پیش‌تر صراحتاً گفت:
«ما این رژیم را فرو خواهیم ریخت.»
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21337" target="_blank">📅 19:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21336">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی: حدود 40 تانکر نفت شب جمعه از تنگه هرمز، به سمت مسیر عمان و مسیر آمریکایی، عبور کردند. این میزان معادل حدود 16 میلیون بشکه نفت است. @WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21336" target="_blank">📅 18:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21335">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یاشار : کتاب اوستا ، یسنا ۴۳.۱ آمده: «اُشتا اَهمایی یَهمایی اُشتا کَهمایچیت»  «خوشبختی نصیب کسی می‌شود که برای دیگران خوشبختی بخواهد.»  @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21335" target="_blank">📅 18:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21334">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89d69f232e.mp4?token=oeXpTSOCpwBXM0lQsSy5pFKX9iFSqpr7Sf89apSL5j0mM7chcJaqXr-ec-wNWptsKUhJ2zffVxEkrVWm9OtWCFX1lznBVXh762kgF8V9Qo5b4oc7t_lysbLt0FZsW-Z7-UQvKlEJo4ztP5OjXfOhhaUBTZAZ7TBz_OB3a8lO4FvGXbpNWATfMqn6qkcaKHmlSPrczeL2f4Vmn2PPyL7-EoCOT-r7ghPILKjDgXrqeA1zH4ZFIQGkRdCZ-lr3SpPjPd4WBbH7MFLxG5-ONxG-R83Xy8kuxw5nStskGQ_sA02dCD3dZD9C_yzn4HDyM9PhoUrfZgOhTPKyf_Z-4gf1mw7UG3Qa4WBqL5Jyh9SjhFMA-nKcSbnACEPqXVfnrf9cARg4xtX7svGDZGlSvBEX57MoEIob88XeQVDVPTdxoA4BGaiN1U0fwLCAN-Sjx1P31902qiqKLnFPqIiEr3FHnx5pEK85Za4Q5yUFctwLZzDG6lNxisbuRlRzOdxTKm_svDeaZND2qFgxfuzZ7-J50SbzZ2Zaet5Zm_ZSWtrHJpzYiPvlT9Hj7hU29PWQXSl5bp8EeB-Fau_sy2j27Xo5o5owvjwEY1rmYM6Jvf-NbmbUsha4NUOf8lw_n9SeYD2YTxHViYaomy7Hdpcw8Onj--dUWJrDdZxL5cFywn2IsLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89d69f232e.mp4?token=oeXpTSOCpwBXM0lQsSy5pFKX9iFSqpr7Sf89apSL5j0mM7chcJaqXr-ec-wNWptsKUhJ2zffVxEkrVWm9OtWCFX1lznBVXh762kgF8V9Qo5b4oc7t_lysbLt0FZsW-Z7-UQvKlEJo4ztP5OjXfOhhaUBTZAZ7TBz_OB3a8lO4FvGXbpNWATfMqn6qkcaKHmlSPrczeL2f4Vmn2PPyL7-EoCOT-r7ghPILKjDgXrqeA1zH4ZFIQGkRdCZ-lr3SpPjPd4WBbH7MFLxG5-ONxG-R83Xy8kuxw5nStskGQ_sA02dCD3dZD9C_yzn4HDyM9PhoUrfZgOhTPKyf_Z-4gf1mw7UG3Qa4WBqL5Jyh9SjhFMA-nKcSbnACEPqXVfnrf9cARg4xtX7svGDZGlSvBEX57MoEIob88XeQVDVPTdxoA4BGaiN1U0fwLCAN-Sjx1P31902qiqKLnFPqIiEr3FHnx5pEK85Za4Q5yUFctwLZzDG6lNxisbuRlRzOdxTKm_svDeaZND2qFgxfuzZ7-J50SbzZ2Zaet5Zm_ZSWtrHJpzYiPvlT9Hj7hU29PWQXSl5bp8EeB-Fau_sy2j27Xo5o5owvjwEY1rmYM6Jvf-NbmbUsha4NUOf8lw_n9SeYD2YTxHViYaomy7Hdpcw8Onj--dUWJrDdZxL5cFywn2IsLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : ایران در حال تغییر موضع است، در حالی که دولت او خود را برای اعمال موج جدیدی از فشارهای اقتصادی بر تهران آماده می‌کند.
آنها اکنون در حال تغییر موضع هستند، زیرا وقتی کشوری دیگر نیروی دریایی و هوایی ندارد، حرف چندانی برای گفتن ندارد.» او افزود که «نمی‌دانم اصلاً با چه کسی باید مذاکره کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21334" target="_blank">📅 17:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21333">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی:
حدود 40 تانکر نفت شب جمعه از تنگه هرمز، به سمت مسیر عمان و مسیر آمریکایی، عبور کردند. این میزان معادل حدود 16 میلیون بشکه نفت است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21333" target="_blank">📅 17:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21332">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">روزنامه معاریو: آلون بن داوید، خبرنگار مسائل نظامی این روزنامه، مدعی است که مقامات ارشد ارتش دفاعی اسرائیل  معتقدند که نخست‌وزیر نتانیاهو در تلاش است تا تنش‌ها را در غزه افزایش دهد تا انتخابات اکتبر را به تعویق بیندازد.مقامات ارتش اسرائیل گفته‌اند که نمی‌خواهند وارد یک جنگ جدید و غیرضروری شوند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21332" target="_blank">📅 16:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21331">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYfbIu8oxKv6puIMAKkTjTKEbq0kMh44Lzcl7ITTosEc3n-ET0vVQwVSOK2Q0h0CqPtHsS9wA0L1BT2136a3NFiQxam-gBW1pDv5XyuvjKMemONTY4xGh9FCKysk7Ck6Fb__H99kwcJ_Dm8ZjP0Q050bNu4omrYj6vIKnbl9WYWzgiYyTIwSOZvE-5TUgRi3Xm3JzazyJ-ABgy8nLS4Fc39OB6JAklNZcz2dOE-42k4RiWKpWkWUfdcdpTO5J9Xr4sYIM1eIYUSwVC_gvEjH18exqtof8h3sxgy5bHDfUVPGmginjvpi4CXHYlvSg-xHcRzMreQDS6NXKRHxnT93SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز صبح انتقال سه تانک از کمربندی یزد بسمت جنوب کشور
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21331" target="_blank">📅 12:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21330">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رویترز : آمریکا روز دوشنبه تحریم‌های اقتصادی جدیدی علیه ایران اعلام می‌کند که احتمالاً خریداران بزرگ نفت ایران، از جمله شرکت‌های چینی، را نیز هدف قرار خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21330" target="_blank">📅 12:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21329">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7hRL87uQ5IuFtnjFfCkdGZaqbGOkyPQ9UFrw2DOy13VwnMgsDlP48k1azkFBtmmXZI85ArSGSL3JL5evNXH-EDKecXUtths36gZ3t991R3Ul7D4gunmUsytxsjX1NpLTxa9PuG-_8nh_lA9sQmwpO-UDJWj0_u4C7GIqC2Lm4-QUH9bU1IUUlpTrrQX09G3AyR7nJg5PyLTfS-WZQXraG5kia5it_rmwoJb7aDJEf694eneYGFx_Pq21YcJnL-V7JJle1Bug7hpxDuKaiP0iuhaKLhvtd-Wxuw7mgZH-jvzSvYfyZ7hnh7HqjuQN6O4TDgQpI2kPgBnq073TvEeuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">lكارنامه شاهزاده رضا پهلوی ، كتبى ١٨.٠٤ و معدل شفاهى ١٨.٧٢ ، انضباط ١٨!
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21329" target="_blank">📅 11:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21328">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUWE3MFQsoIoebZ7mqJGp0901fDMNCPo3S-6nXfzv4gIgM3ABDfSQjKxXxrJ5wI7gl07VKDLqQ51tTNzf1bIYnsOu_VwnGZHQrWILnxa9uOqnYnFurBuWvky_oIZUndUvH5Xo6ib-LvT55UVRu4CiDNlJ0J0KKqvClty92Pcy9bSvW4rZA9_LPMUolvR2-8260Uf-qBWiITdrCyHM3i00fw5ZfzV7AJXn7vESedykmcKAufxIgKf5lNIxy4C8HadLsn7pSfRN_HcZ5LAHcWd01q1MrYdE89dh1Fcai4yMVtLiWaGtQJr_FpcJ-7FE02jVFgoSGwq9KrdneNa39gkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تانکر نفتی، با نام "ال ماقام"، شب گذشته تحت نظارت هوایی شدید نیروهای آمریکایی با موفقیت از تنگه هرمز عبور کرد، در حالی که سیستم AIS آن غیرفعال بود.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21328" target="_blank">📅 11:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21327">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یاشار : کتاب اوستا ، یسنا ۴۳.۱ آمده:
«اُشتا اَهمایی یَهمایی اُشتا کَهمایچیت»
«خوشبختی نصیب کسی می‌شود که برای دیگران خوشبختی بخواهد.»
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21327" target="_blank">📅 11:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21326">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تابناک : گویا راه حل چهارمی برای بنزین پیدا کردن!
کیفیتو انقدر پایین آوردن که مردم از ترس خراب شدن ماشینشون دیگه بنزین نزنن… دولت با همین ترفند ساده، مصرف رو کنترل کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21326" target="_blank">📅 10:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21325">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مدیرعامل شرکت نفـت ستاره خلیـج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
انجمن خودروسـازان ایران پیش از این در نامه‌ای هشدار داده بود که استفاده از متـانول در بنزین سیستم سوخت رسانی، باک، فیلتر و پمپ بنزین، لوله های فلزی، واشرها و قطعات پلاستیکی را دچار خوردگی شدید می‌کند.
مدیرعامل شرکت نفت ستاره خلیج فارس: استفاده از متانول در سوخت در کشورهایی مانند چین، آمریکا و اروپا تجربه شده و این ترکیب هیچ آسیبی به خودرو وارد نمی‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21325" target="_blank">📅 10:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21324">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آمریکا و کانادا در تلاش خود برای دستیابی به توافق تجاری شکست خوردند و به همین دلیل واشنگتن از صبح امروز، 50 درصد تعرفه بر محصولات کانادایی به ارزش حدود 20 میلیارد دلار اعمال کرد. مارک کارنی، نخست وزیر کانادا، در پاسخ به این اقدام، تعلیق مذاکرات با آمریکا را اعلام کرد و گفت که کشورش به تعرفه‌های جدید «دلار در برابر دلار» پاسخ خواهد داد. این تصمیم پس از سه روز مذاکره متوالی در واشنگتن بین دومینیک لبلانک، وزیر کانادا، و جیمیسون گریر، نماینده تجاری ایالات متحده انجام شد ، تعرفه‌ها بر محصولاتی اعمال خواهد شد که حدود 5 درصد از صادرات کانادا به ایالات متحده را تشکیل می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21324" target="_blank">📅 10:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21323">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پاکستان برای هزینه میانجیگری بین ایران و امریکا ‌۱۰ میلیارد دلار درخواست کرد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21323" target="_blank">📅 09:51 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/Sj_AD5fqWsUfV7kg6KEA1B7cVyu8TYJ1u2kzHAU9h8ok4dRLkLTBW05a0r5ogGRzP_aZpEpDGK74TpFvjoHxrUHwUulemIxpci3uQ-b7uIX_1VerRCoaeCw1C-m0FSby-sld5P8ugtBMSRygfovWr8oqNGcx2DGL66u_P0rUSUxN2CrK3Hu9OcYxocAeXVNXQiwpEP0b060Ri6RGLCDXFyKy-FZAufaGhygqcaJA7cbOGEjYFxzx3uJveC40SuqLctIiCsepB7CqKHOdPykp_-4ebG3QV6kaxr4PFQ0bKdj8DsWvpjF3IA5N1DW-2CRd5bKkyKQZ-q6OrIXKkdhEJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 521K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 14:34:53</div>
<hr>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKJxFdbnyJ6dupTscX09lgsmAFZEkA1_uD-_Z9x9jjQEdC7b_kZmSYz4eH4-3e7mcdxsfuBAeQKEzzxtk0SwULlZVOpX0K82IPwlrL1hkCZn45CaKp0Iofb12-xdLUjKGekom3KVSlI90c9DK065Mzcqxn6ze2ecE-Wctg4SFmV-9kMEJBFkzvxFbYbmqkpMajhoVfcWQNBAhErB011nRHzPcjP2uQP7H6VT_IW8C-D9-XDHf_xvOOS5029jawh7nsxvcrC82h7iITZ0Nw0n9b1fzqgMljt1H-DIS4-_d9dS5-ccAFDN-rEeWCAoBZfWThgSig0HiMDBTpKWh1elfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKSvU9_f7j-XSaEso_a6Lw2QIu1ksAm4AIIc3E13AEQ3QUWMA7sIavj_NvwYZPm9AnwlZ5yavOhjrL3FEVoacRCtGnnb6Ib-ikXzlP-EIOeXCnhpVn__fcgFWfU8pqBWskiembmExN4V98a4zm9nqvbcZwQCpqURgeWbPsuYCWtc_H_0suLIhCHPcCcdlRa3TcDAnaiv-aW6blESvKU6Usw6InwNSL0Koeoiy2mVz7T94xJOV8k-kND1LwU32Vd7ZZvlhVZQxx-nqSTR0xwu-yuChx-YvmHP_tlQlGMuQOL5eiA7T4xNbMvq7lnOMpfpEqHAn6yw0DrIB_4S4DUDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq38ZDOVgkN3f8VwVkE8rOZX01pajxaN53NJ0tNwkwY3EMKu7eQPpSXQDNyMfHLCc8PtFK2WeiJhMBJMh5LrsjwhwMRtCJDGEimyQTqamNTGVvf7XLuQoAHw4yKjuGxhIveAg_i3qUwsQmBvmfznKc74f38iKyoeQwZT60X5YjEZZk6IFtJAhYrYEXIBSRX9_nLfVlicL-QLvaJnXQYWaZ641K2MIXa4s4kOWfrc3LyN8CUhEImRkJPG_z1VAyjrXtR3OaujuyGxsShCjCCQovQPrO1JomNyT3HhVOGJXzGzY8JOYEhL1zZlXgqnYTn8y0ivadxnYVYedwhuUCdknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpNbmGRMPp9tbNVKh8MpMqJqKs0Rk1VE30SaHFIx_FqjpCrVQ_rYbI-gZG3WOjqKff7CUYKuxRSCRZ3-D9TyimMzULDBPVsPApxhRjFLxNt7a0yC1dMgMfiUqCq7PcqiVkuTaUiJ6ZF1EhAH4TcNmoVOkFUjT8LwVMHVIE1jetLemMuyGt9u2okDkU3WQN6qZaHp6vb77foKD_HUp99cu6mU8bus8MYQsr8ReXG5GKXMFlrWs3w2xUTso3-MAax3XybtTxmoYGv6O4w7fV7JnRYRpKdARpveL2X5_IEvBRI2SQuWdXJ3qu1_qYqf30049eg_VqiiVhMJ4dv5kTfDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwB29TmiLX5uvyVLK-QwKSpLlNdnaBbu1VI8I4HTI7zUCu8yw8w5Vqm3nyLzuibja99by4ZyUcaXDevhyEqPqfiMOIF5YGd5Sl8_BT0Dnn65qEZH6nToOmvX7mji0qFEFPDe7FwjyBkqmrltJXR86e5Dr2RGdVW0c2un7i-CHUbseXhIm6AZ4qET5MBx8yb4-ET9wT-P0M_EuUDys98bRQJ1xY8UizMacj6mfQ40Pbda2ghd6BXdhgZdwtJGcjiRUkS5FBW2ZZHaBmS4otttZUZpPdL9jiYoqzAC5Ev-SDkqqwosWZkMpv4WLaWs6JeMR4WtXjhZbR3NrWSoeuQHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2h1Tzb1kgSK72MLoVWFIpLMQ81uPwLRWsyx7lCUu3ka2urr8WCmoOH8dWVtlFFSTcyUdriwisLZT5wxY5Dyo1smPPteUGqmrJdGqiYQjp1FKYAdfbGAuFjYV_WV2zkPmUvPsQrCYOHE0OOBDIA3pMYmO3LYjcs2r5gopZas_VocuZgblwFW7Br2EdMTazRr5ncjbEH2fIQNEiiSAcm5Jh6Az-WleKOMNavxa7s0q1a2mytlgHMDMifjluJ5_MBB0OyZgoGg_Byt0SZ31eULY5shuN1PWRuMgaGbbl0N8brj_PHFLQtemilPFk4WL0FEA3yVbMUIomm-qOD5nOoKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrUmBL0OI08C6JYdLdjE1p2ZTzItOdFZ68CHa0glmIuRsh0EewschSOAhk5Miv0aKTX9ZLlIt32ojsmpmzBgthXZygXzAQweeoFcSeeN3K-51FhP6IZd6TwngBT-UNHVtHhuEvO9vi3EYrS93hxBdOv7REConUjZZqOOt0voSqI4dr_Ba6zm8eUEbj_knWZVzRlvIgjMrR4g507vTlMv_SwwT4wKCYpVQgpWA--H9xEKtlY9Gxmj80MReg7lyyGCAZmlnv5ceIsX6S9q9XPJ0_7ozwmkNPPgvTPCRoGIqWBMLFvGMrm8koxl4RUvRYT2xafNcta2aT6FoAwLBIBusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nApOFO_sYBbSFk_Pva2Q4q7gwvAAYI9OyV0x3qbYPJqgT8Ps6wT1lNSTQYg45fCXUSCz21s6MTYF80hPHEaA5f8vEMRUdqhwngRynlP8N0l9mn9UqI1jrdwsTG9zafDbQXhzhtEzaWTyoqfxJgjrNvwCr0MeV3kBXf89BJXjX8K76v0UOvONPOfGi-kdmKBKn_05jhuRU26p3zh_pxEoA8TM1hLQCPYzltZezoPrqoIyxNPgSgbWPNlSogriC7JoRXodoFi0bq4i3GUSlgsj-2DHMyicKlQE7dcsIpWUR6RFPwTVTMo4_WdgKRBwZQcuHy2lYZVuynQg5B2qPJhcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYNoVGU2_YBIlp7PBA8RLt8p1lE26kXSsLAcywSRjA0luwxfprcjuWNM_-oCkqHN5LHiIvFMYLHyPjuA_uuHYTL6NCYQXZ_B7WTTjX_m7TIDcrBDW2bgUfFaPpyg5rDN_JZEeb_E1UMzhbyKyWDh4rDMIIno2VTEM971aOpDf4fdC8VWGhbivZbZEFmltNtjMabfoWSXF_3vaRc6HYL-CFRLxqVRw5wbQd0jvE83LD_rcidsXytUFV0zamTarnPq9Gh6PXYZ7E2uF3RZPekS6NN7KFYBXX-4RbbZUH5sZH5lf5pcUbnwKYCK98FEF15yVemaBrWXt-z9O1MzcO9MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgFaoQX9ImNhn9TSi1O-GFrLWQK5hSqwSbOjps3a_J5aVUIE4tyq9SMrWQtHFDKUOA8E-L7NNAf75AA2TMNRcJZtrEL5KJIiFot8zS8LUQnoHzLlMrC0E5B2ei8A_obUpsce-kbdzXpkzgoR2jehYyIpcivKMYjSkRRpGOijoufasTxZXn27w21oQdigqDQMKy1WyhRmJ0mtP20of1wXWwB_PFTt52cfAi57i0X6OtlU_2Me4JOCelWl16ip87-7aM0LQmLpTgtR6MxhZ9nRhMOO5fcBB-dpTOGAIaNyWHX2Bq7atXw2xNVT_EOPcsg8n0tStSWNpWi5EaeOJlB89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26043">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2k6inj52MHQE0E4qqpkQyDFXLTIMtc4Nb3AfM6YA2q1ztjgeLRQRcJ454zA7un74k_jAMULHpwDun6x-xmyVJg_4tMRl7EtWICnLF1vQxmmWwyAF7rESatGVIhI4vHBt5IX8Vu0uqKa2xX11faQSjbiAdxB_nCdoy2w8_0q-S7m0m8UXuLs8vwfQzOQjRogOJPI2ImILH61ni6Sx7Pr_A8pzZigaYdgRQHRzaP-eQt7OuUR5rRvd1omKp_iZ1Kjjb6ReowN9cgEul6k9gcP3DFy9gxRU0_NWruY7YlDb9lX7JcWkYIQUa47OnfjsKu91-ty1a5nw6ggKOLRAWs5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
برای اولین بار در ایران ، فری بت
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎁
💰
سوپر بونوس
وینرو
، پیشبینی بازی فینال جام جهانی با بیمه ی
200
درصدی
☄️
⚽️
اسپانیا
🇪🇸
✖️
🇦🇷
آرژانیتن
⏰
امشب ساعت 22:30
🚨
ورزشگاه مت لایف
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
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
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr28
📩
@winro_io</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26043" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=IgC5NHGSeHMOUQ-Eco8tg2D-YKvAWus2NaZWdudhcvvp931Z_ZeruWpAfbyw5nfzgxfSeq8Z1nALAJUncUpTSz8WWNnoQH85WRvqU3Tk3yNffFsX75tKieYzeum8PYOJwQyyD2upEjFhZ2_XWZ8LrgwVyXiyc7e24keqR_bC61Hl-TPA1Vgrqv7HzWwLylKHt6ih6Qzo94hmpJFsY0DkY69iHHJeOLmXNd4PNPRUowWyKNT64UdHC8IeeaWspIjtUgwzN5FoRO0uo25cfUFwFONuOBMwkqaJ9-fiNbudoCjoQZa8XSyxgpkmp2rEeRE4HqyCaEtNHTEelMRAhDTJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=IgC5NHGSeHMOUQ-Eco8tg2D-YKvAWus2NaZWdudhcvvp931Z_ZeruWpAfbyw5nfzgxfSeq8Z1nALAJUncUpTSz8WWNnoQH85WRvqU3Tk3yNffFsX75tKieYzeum8PYOJwQyyD2upEjFhZ2_XWZ8LrgwVyXiyc7e24keqR_bC61Hl-TPA1Vgrqv7HzWwLylKHt6ih6Qzo94hmpJFsY0DkY69iHHJeOLmXNd4PNPRUowWyKNT64UdHC8IeeaWspIjtUgwzN5FoRO0uo25cfUFwFONuOBMwkqaJ9-fiNbudoCjoQZa8XSyxgpkmp2rEeRE4HqyCaEtNHTEelMRAhDTJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVxzpmbEY6mITACJAKa9qjIk_hVZVBmbbDMuxOTgVyugreOb8Fzrx6-wGQ7IrtwpR_kENLRbdg40JcNCLh6-tNyLtVgDUozGdVzKmHebP7wQ-HP3AtUcsT7QXDSO0l7lxpZuzns5Ilh6HhZSs67lZSakB9Jv_BUUuNJb1B-WIuAAzz8SZuCGiqa5iFu0gL3FShKHur7frnFPdHW34SLajFccUUO10jEv9l4wqhVvLdgwRxvIH2Ri3FuP5r_eAqFuFpCL1KlrRXne11tgiTkjVCOV7YHZHbcmtLdccIbkR1iyi8Ye3jAHkOk4CiTV2NKUGroVLDsm5U1_YtDSpcRDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3fGNcp_ivrtnTPGV2mH9qSVIhLCb6xho4xLDmmYju3O3lDBIc0-9KyJd5nejcwfpNg4uDksrpbAGAnV2zEr1mjcT-esXOO_3LMlSzfHEltrsPB2KpXWDWRmGGWK00P3RVuaTrBDRW10fBBakJyJI9jtbJeKBv6dxtk_UWxV8finwRlvwActZUSD_22uD5P9B8W4U_dGUDB-PGm_gJ3yOZKxb1LJdX647lNRMIoE3GW_J9GH8hflf2sNK3MgylsWZ_-F1JispIfKKzjP3Z28q7Cn8NxVtQD37tEEp3c4ss1z3xBkfckSo1SQWCmJJyqVyIVasLt3PqY-hXQhVQW92g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcHflUBQBkS0ovX6xWDvoG59eNnbpxSEiV5916uIAHKkZSP0ScUjpDl4dv-5-N183t_5scp320xFPy_4p-GBCiDLbYBKSQZvFLLyy2A4413IUO_uPbfXPgsDOWJ8g0__6DOuA623ooAFofsJKkx6FWJ6Yv6Um7WadhnTEScprtsplRNA--E0UapT7ArhNuI1qzv11IpoynHtuLJQMwVC55YtQIwxPOd2sHM2LU6OZiiaVdgklbQPC5KOHOnXvImHEWP2qQ7COiGJI3Gt-JBh_vXkd1hPFPkh9zgKyvnqurvf_MRECvIP8MTJDqi0FRN0zpsPZa6cPSs-3zYuOpVCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=nxkTjt3JSyAt2-9uJ_vGLOZUPfNIeAhs8PflaX9-CFn1wG84NDs8LrDlGF9LI_Vcl8RO5cPPFNuxiQkq4Alsgz6Kv2WlPMSSAafoPJG_6GmVKeQ1gCjbyRCa3hIazflTnqM8-sOAQ2TCUxeCCvThaDp66rQxaea79PTMHdUwTP4PDW1b3sgJMdOLR-ltjgjtDdaF0cENw_a9nx3tqm8_IytLNvsTKm1e358zH8rZxfbixLhwvGDdiK4q2LIqckx9bsshsbMpPah78ubVZZ7Au9k71yR7FmAitSBTwemrt_oHgxGzSvMBulXAnL0ksNSIIzUBszbWTQaz0qOmNURjbr1s8rhls5qFtju2RZq33TDhZTEK-CNxSPE5SS2y1iaV2Jn--xJDVbaxc1S9-9Ab65wXDHwrM5CX4gQehx5Eq1_y7BiiSzd3CcBBS0uKciknd_JY0S_Cy78P5Aqn591XG1_dGkiiZ04ElThGzb4wzveK_4PFoywGNpt7Cmp7OyM-TiQMcq2Rw9uIjwTyEIVL7l51XgaTYXoMVn4Vj3MAqdAanfRuhRZ6dJErpVVBRiLryQGs8GRVJ3njy_G3nAnhI96IudS8M8H5SpDPmTJQlaMhudPsLUqwL3D0LjYBe5neGR7PIzMlwYPEHhZtyxetVEgAmp0gBSRfBhx0EhhPBA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=nxkTjt3JSyAt2-9uJ_vGLOZUPfNIeAhs8PflaX9-CFn1wG84NDs8LrDlGF9LI_Vcl8RO5cPPFNuxiQkq4Alsgz6Kv2WlPMSSAafoPJG_6GmVKeQ1gCjbyRCa3hIazflTnqM8-sOAQ2TCUxeCCvThaDp66rQxaea79PTMHdUwTP4PDW1b3sgJMdOLR-ltjgjtDdaF0cENw_a9nx3tqm8_IytLNvsTKm1e358zH8rZxfbixLhwvGDdiK4q2LIqckx9bsshsbMpPah78ubVZZ7Au9k71yR7FmAitSBTwemrt_oHgxGzSvMBulXAnL0ksNSIIzUBszbWTQaz0qOmNURjbr1s8rhls5qFtju2RZq33TDhZTEK-CNxSPE5SS2y1iaV2Jn--xJDVbaxc1S9-9Ab65wXDHwrM5CX4gQehx5Eq1_y7BiiSzd3CcBBS0uKciknd_JY0S_Cy78P5Aqn591XG1_dGkiiZ04ElThGzb4wzveK_4PFoywGNpt7Cmp7OyM-TiQMcq2Rw9uIjwTyEIVL7l51XgaTYXoMVn4Vj3MAqdAanfRuhRZ6dJErpVVBRiLryQGs8GRVJ3njy_G3nAnhI96IudS8M8H5SpDPmTJQlaMhudPsLUqwL3D0LjYBe5neGR7PIzMlwYPEHhZtyxetVEgAmp0gBSRfBhx0EhhPBA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=r95dhP_T6j6-e0Z2csynEm4Q9wlzge9DUBfWgStJruoFSXy-aLf5ke0dB8nY5QvjL_kGTQsZD4Xh-ulf7G3MopozgC5q4u3ghWSHqQ29YNm9H9qIZR1P4EKsGKtI0-_opA49W8na8T65Mu46u6ESXNcEKymhKWtmfmF6o2U7fFuDQaRNrIOeQsNQiOd-30V7c37ZNdddT-7azOwXUu614S86qjrrFrWTPejTOwIwQE0Q78OfDaYMj6hqH2F_13H9bHMkceC5LpcGWdkQHAtVsi7JWcJsXuTX96xeGgswdSOJq9n6CwqguAD1e8AAiG9WiNj20PT-mW9VeFT7hXl8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=r95dhP_T6j6-e0Z2csynEm4Q9wlzge9DUBfWgStJruoFSXy-aLf5ke0dB8nY5QvjL_kGTQsZD4Xh-ulf7G3MopozgC5q4u3ghWSHqQ29YNm9H9qIZR1P4EKsGKtI0-_opA49W8na8T65Mu46u6ESXNcEKymhKWtmfmF6o2U7fFuDQaRNrIOeQsNQiOd-30V7c37ZNdddT-7azOwXUu614S86qjrrFrWTPejTOwIwQE0Q78OfDaYMj6hqH2F_13H9bHMkceC5LpcGWdkQHAtVsi7JWcJsXuTX96xeGgswdSOJq9n6CwqguAD1e8AAiG9WiNj20PT-mW9VeFT7hXl8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9WDrmxR69nacbZj4X_MX7oY7FMjR8OMYScy3ULJoLavYphkfeW_qPLPe2C7GLsJqgwLuV3VOPh56QY2qH6HaPu3LvIYQkH8b3PADKchLinLOk_DkOTVJK0Jngq12fC1Asrqi8oNNi0dvOzD5jnINGIoS4ybz_e0Tl3ft1MIoRwKI2jux1rr3HIhEvuREB2S7CB7MsYiclWRpPwRRQDnZVOSwR4AGCzV37Nm1wCmQSirIPTtrvFnsybQ7e9Tcei90hwhbAIKYC8EZ9TPBeMYL0mp1r_LzjtVcvfLP-GIoT6MHrwfa9kHCA6-hakmrNJDCi5gYOwPs1Cln-1vjFs5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=vckIFbrN-P-ziZ7DaPS7wBRZ9ef4k9Ta5dudBWTfEM1clriSZQui1RsZalc5n6n_7CvbsJOY27gcM9j9Gb_X-fzuWMzeRoGuFGYuiS6DqzsH_7cfgDMXk7JQqjsKdzacg39bQAF4qm4YPo6mODs1kpqz1G5mjzhG-ELrph6Ol1tx6O0fXobNtvxcBME3tEjsFUmtFJYwGdKE8X1H-A84srqtLEzFArxuHyYUQY1Ys_aZbfe1S1GLMub3q08fl0BuMynXJQ0zehC66ma5OUDoLTUhTpaJ9Ih6g2e-m5u6ZXWMv4yxJPIfLEwPW7LLuyOeXubHfxNE_t0cg-aPVodbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=vckIFbrN-P-ziZ7DaPS7wBRZ9ef4k9Ta5dudBWTfEM1clriSZQui1RsZalc5n6n_7CvbsJOY27gcM9j9Gb_X-fzuWMzeRoGuFGYuiS6DqzsH_7cfgDMXk7JQqjsKdzacg39bQAF4qm4YPo6mODs1kpqz1G5mjzhG-ELrph6Ol1tx6O0fXobNtvxcBME3tEjsFUmtFJYwGdKE8X1H-A84srqtLEzFArxuHyYUQY1Ys_aZbfe1S1GLMub3q08fl0BuMynXJQ0zehC66ma5OUDoLTUhTpaJ9Ih6g2e-m5u6ZXWMv4yxJPIfLEwPW7LLuyOeXubHfxNE_t0cg-aPVodbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCLvKdbfZwUKDusPr7KabTaG7FCufB0HQAA1_PlEri4c6JmoiUJzN4i5756N8lAc5WfWsS1L27kTiL304mfa70cj08eqPyl2pAjCPL-jQPyl8Vbsb83UpDlrsEjsZJeTFtjr1bGG1KyoEo0ZkP9wYRQeqhxFYS6N_LYT0ECgbpqlHOf7vfd28pc9I1obh7jZCAOb6zYJPRRkMS9wmxsjC0ZE-IzgC5UN_WYhrsjIwBD70j1M7y6JFl0-9LCJ2rI4obf2Ly_iTp8iyDmjCMG2JBYkJm4rj_G4RAB1jaGpx4o_hHB9vmMwwKl7U3_IjR3b-7fKHRgfvLXdogcE7ic8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCIVQElwGvif36Gt-pe8Jl64JORjbVoZYiApau17GKRYkRtGfAdVM4gz4B9ScgOMOdbjghxjlBMm2awHVmLqK0AdMrYH46l_5X07-rnPIS62IuE9UfqFeL991AdbHh9FRQ_etU1t3oHidMQ952sGU9vEg-ow8iHyjYGO63FVG1NR3HxAHZKpV48gAVjUOGDtrhwWas3FtbkNOjEqfR5BsJDW4I6IP99txjmPixZ2SzTEZCbVEkz86gXLCiWljJuR60dzaWuRYJuQSAZAZKIXQ3giEQfeQDwaQnibZqAjQ-G-3SIHCwCK9ABsNbMxjY8eBYgoHPvKuTN2uKm-EsLJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geomUDSnfib7qmMPkfw3rjdHIPehTBWC49xC2bQJgx-RzlxE60AaMDBWvbF1C0pllWuTXPtzq1oArWmU1cIqK5xsarBBgDg1BaaMhlj2paRCuR7YN5TkcYlXz9vzqweoMbcZAwOvXHqMfhhY6I6-MvKZlY94eZbpy_OzeHjxejcCHCjvDaoZtkOcYw-aDKIsWSQcQqDejJaFO_P2pc38AgLjICKFeJM_pCgHz7Hnp12AfCRcSEw7j_1sF7vmDeauvtL8vuJa2bUMt5JdwQIgBsGxLxWDEfD7GqE-B5NlNYWbRst9Xs9pXA5jhNTZP-_kzA3HtJrBhyUXC9yrhxqKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=JJNL4f0S0BrD3PwBfozEw7VNldM8trSW49huOn0qwJEyxzMLos8BNYBpDuEP305KtcOuYAkcA90eaWYDP2fEjKSiZGzLcIWw5SxUStIUwzncfJgblQUj17at0LzX7YbfwZZhH16eS05wpgdVnHg1phej5NoYYcc-IZe_3kcHNWSaOXNiQKhB2zmeZqMuYRWoD1sMY49zwE8_-hDZ_osdIBpUjM0uwjka5o78cBpZOC0lyJ2KXPN_MxUl1HNFwLy20YgcuCfr_KmWbS-2HlVHgrQ6UMwu9PMkgwZJyxctddAdEhk9RE_8bzfhB5l4fBF8LQeOk-LnvDFs-mcAz9PhNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=JJNL4f0S0BrD3PwBfozEw7VNldM8trSW49huOn0qwJEyxzMLos8BNYBpDuEP305KtcOuYAkcA90eaWYDP2fEjKSiZGzLcIWw5SxUStIUwzncfJgblQUj17at0LzX7YbfwZZhH16eS05wpgdVnHg1phej5NoYYcc-IZe_3kcHNWSaOXNiQKhB2zmeZqMuYRWoD1sMY49zwE8_-hDZ_osdIBpUjM0uwjka5o78cBpZOC0lyJ2KXPN_MxUl1HNFwLy20YgcuCfr_KmWbS-2HlVHgrQ6UMwu9PMkgwZJyxctddAdEhk9RE_8bzfhB5l4fBF8LQeOk-LnvDFs-mcAz9PhNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=uNtZH2oB4M2vKsQXu6KWArDo9kg8RJikW5eNGZlz3ybcweOf9-gRKMPWBoEoq_d3O7TVa69n2UJpRwlPUGR68QjYMOuFAocjq6twtahOnlHGhhjS8xgTiKCBBNAHXsCa7maX8DLrEQnu_mgiZbWX0xdBH6lqg8d9bAJuxakYwPSntLxNakJIjTyZwhk3U3LfTk5gZ5M5NZiexyFSom61nyIOrj51-X0DygtUoBfbODQH-2bPAQy6F13gtDL3_6MHn-pdeurMNKUtykVJqMRyRqNTnwSb2uNAZfLBtuQk8pd0gNn7z4gV3Fk6dGwJnBWLBNTMRBQoGkBIlXTEM2Jdgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=uNtZH2oB4M2vKsQXu6KWArDo9kg8RJikW5eNGZlz3ybcweOf9-gRKMPWBoEoq_d3O7TVa69n2UJpRwlPUGR68QjYMOuFAocjq6twtahOnlHGhhjS8xgTiKCBBNAHXsCa7maX8DLrEQnu_mgiZbWX0xdBH6lqg8d9bAJuxakYwPSntLxNakJIjTyZwhk3U3LfTk5gZ5M5NZiexyFSom61nyIOrj51-X0DygtUoBfbODQH-2bPAQy6F13gtDL3_6MHn-pdeurMNKUtykVJqMRyRqNTnwSb2uNAZfLBtuQk8pd0gNn7z4gV3Fk6dGwJnBWLBNTMRBQoGkBIlXTEM2Jdgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBvQZHhpIs4uCpV0NG1aaYXoj34h1Oa2uR7odFjXJr6cbBAxMuXCP42hulwvwseEq1ONhaHYm66fOiJTiBylXmhbjbjmyXf9uOvbEQ50LuB43oIAId7cxumvNZpsazVuD28DP8439Q-2CoSXXSVllPb3weW4iz6ED2VfY5qxkkptpKeKqeKZs79xN4BWudPYrTCr2Ku4WVS1UBqd8bHGDXePwXTDkYaTZJslHblb-Ivg71fClno7lz6KynV9oSNACLnxK_1uqArR1oTp3CPqg3_I-QlnIn7nbajh29fb3_74rx2d-dHWft7TEBBzlMqGqal5kJnAOdYez-lUPK7gsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4VqMreHH4SOfD8MD54Ue1HInbjVULbc_7NDnOAEKp4iBdwlRg5jiSuD0GMcOxDCOemhNFjG6VtdviB9wVfMrse8q2ZxnP76wHnlsbBpKSyIX_cfo5gKArJ_A0Mh4J2uy2Cu1A_qE13dl7WUzUC8LuZ0uaAd6Wd60N6qWs6c3Hs82v9HVypZsd2CM4Wig9cqka9TCuXOzqn6zeu0vKD6XOtH5WGsfO_z7oKZ6uq3ediHON6It5C46jM2j8CMz30Pt7-izzy_1uyq6iOZO3OP6tBkuaKddYzZLOqkKmjSe-mSXBj5Dh6RCDbKaaF9M3JJ1AXzhrPzTrLotRCpir9eSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o88ctVucIVHT0TeIRcPlrR-TGSarP9j-6xuc2d5W34rJsNukqcVPovgyYN5zOBk-J9S-4pHLxgzRBVoEfnGLUD8usdTi0gRsqB-LLIBkhGbbETQfdnu2Ul0GQHbimdSeQhj_Na6HI3tlD38VZHrPbuKXfP-J5trlaSxFJZVYI0ZJmlgFUAlSKk6H1KeHhITHgjgMWVbJeNGeqWyRe61wGCy9SScf-PFVrLDU_pn3gf3AMg02VoiM6T9atvbrf4IuD1lLQ4mhQNAy26YG0Eu7oQqfpb_k2PsiRNm--CcKN0jcYCSFVqqHehEdH65sKxUVl8xxcIedVZhb0ZrK3nZN1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUrMUKNQPZ_ZZAUg3Lg6NFi8ZZy_Dpd7kpOpQXj52jiHAGPEH6UXjbhVz2nb4H7BTFeaqbzyU7IQ5j55OULyU1DfC0nTq5ZE3bdyah41gV6gqs_gU_KsG2YIghhMkYPQ_9UHOGhEM6SBA14cz-msQ06PnKwjklyEecbUIn7l729Lb7uqSjs0NCGUxe-n_XROgo68DGYruNKDjv2h0omzPrnM0-PkAW4oZ6zBxOuGrvTpvYjrU66n6_iQ-WqKQdUKRff8DupIJndt5WL26BhedvY6iEyQvejIDUyDx0vrpjSvh6Hc4cQ7UQ_8Sz6L1UfZ2E0dmQMwQnfKX1T38ZZzfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX7FeO7KMhppBB2wfqEsW1IN_NOqd3dTDYmQbWRkYd9Ykd5mvz7lqSk8S7aqN4zwZfFQPSweEnT1Cymlm-IKsuOMwLwEAvIVNOHJKBv1gWMuCbptVicfgM2EkSnAKYaaaftHH6PFAHPzBTf2nDVoPttunlI-DZTWbGiVYgO0N6k_tH0ggWsDugGn-D8JsDm-Cgh4aiYwpwDYr8FGGhTxFvzBY-PuY-mRUBICNiuegiVqooj_EOzmBPS4vW2Uj7HQ8lP15hz_u3N1Z9OV44NJAZ2pWbDkHFnos32VLgN_tKCO7Z2v9UsO7y8AbNTOwnZIp2h_66LH1WY2bD16J5ZvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdfb166IZZrRQET8ihoblW-Zz22bWLxco-R6fgEHY5wXsszJ281XxzNUbVf07QhUisRsA59BXUAnh20s3L--RrVDaxsu-ksSWFaZLARlXpoxaITlPavHHNxPRgLKnGI5T6ZKKkbwGf35oTzQHCpq1CB36LOcbwkrfjgTWw3Ow0hGoOg3PbIZH6nDSCSF16YHvCxtLHRQ5tNtvt6_Arb1tN4cV9qlYIwGSHXCBSGMKSysDunYkXcfi60g2fa1Ml875vlPy9f-Oc9hhr-uhxIhTyNkr_eZpg4CpC0A3EhLh3iFH4opxUfNtkifxyYqQ6Y30vR0vZLwmnVsQBcDAbqv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boZ6uFV8INrqZVFjW2xAYSuUed2dSGEnhH19YjBxGd_6QKQ677vmWzapDl82HKeVyrVB1x4cV1HfzYiqBzIMTeXhUpDw7L4YD5Gq8rupdEYYU22q2HLVnzQT9qXvyV3hFVgJHc8bwHUATWXKUEx2CKg7az6eo1zdqzL2oouwMSHoUtuAG8vpogUhBU7i_7wsxR4Hr1jshcBjVNi-5I0IebsZSg7ZEHkD952Nt-yAo6eYgabxjtmb_F_9iskxspw_RMlV69BICpwojL7lTsqavp4F1EiSoK3CEGhHBX8z-dfnBAa7j82c18b9pSlk35j2SfcoowYbexsRVUKSPnmj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNa-DZyhdu0zjaloaIhJVHNEkXK089UATrl5XA7xTLejZeLdB2lvpN6EH--EMB5_0sk4FVzLS1Qh2pUZfsUzlyEYe9yQrYiwpMWvcxXjyFLM4GxwtMOmkBY3YpE5D0limTeUYWQyQ7g3icPYJ-24CmRq4BhDyx3DIa11fy_C1S1n_1fvHtEOkZ638SnNvVScPjeDDvg88xL6H-zcP1WoRKdX8oOTsxcGz4TuYDFgwNf2M7alF59XRMz0Z2xTDcreMwS1qGviw1r_efgPaQVp7bkXjavT5gUp-6aZNSDhgbPV_xvLc-Bxj-usoEfO7WIT-P49yOA_TSYAQOLCesww3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUsD5BhORhVAWqemHOgNJOxVnSpnQ8fsQ9Yca_leShzJx5elYMoY6_0W-s7WJdRnuXdDLPpK4NcGEwgd8oDYzZnlQt-4ohgLMj9-kcwbnYeGMKeRHxr3MlDbO3Tl8BNDoMRfGjnm5YWNDdmCvEb1FruhQjaf4BSWZLcFLcxL5i8RWn80TJG6x7YTRnp5En25DEesoRiH4kg1DnKHvdqqyy86rvyy09KfjXpebyDAaY8yUXs4Q0bNCWTKAgY03_cKJK4-K5NmQ-Kjy6dmWi7Wd6FoFbpMinaVAiSqoRAGHxZSJycNsTC14R4XL5ehGG4yH62Ur47I6EDh9zz-0aoC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrbU4ft2RZkqOcAxqy64WMqvXMp77LOZ6hZRiOvhJLOwZYpdS5olLAZjXP2IAhYKoT6dDx5MNNyNQTKtSlJOReOvzzSGMuiVuctXawNqM82RfrZbfNt-WU5m-26laUgo1IOcNjPbi7gKseMTSCB3VlxrSg-UBmiD2QEzOZfGEPRLTCeoI2Z5uYE1Fblsl943QRf3PPHrgM3u-rwU8VeXYI0ElC1kkrqjjXth0-ccA6TN7OvV63DTC4Sk37NxhazSrXaNMuLy-m0YfdI7OuV6oZJz5W7cbFEv5ukwFg2qx1MbNPQuye1axSdzgNHly5ZHulk3hrEKELtzXTmtwpZxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy4Ae5fCdtjH0GR8iW-pi_VD8T_DJ2jCW0xRvcXEWxHvu5th5YJCaemBRccr_rdLLwJ4S-Z05YyPMrsaQAhaftnBIikzx4wLezJ_LwrFpyeKWB-AuIoR50ADyegC6unuomJiGxh08vU9Bpqtk_eNxoYey12sAi__PVRU3HwWM-VkUJxt8aJUKVr1WMeCiZhOdEnJ5pYUh6IFR2PFFbMW9mUAWUCJqZOpsTfkgfuKwF2amNN83BjkiJjyBTBhYKigZQCzClwDqne8ZnHIfOoGFpIFx38arFFkLxURFNzUwZjVM8XuTFWJ5vblTdMsX2u8BKltDmOt0QnwRuvLPJtxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=nuFIf8QsmjePisUFiPJ0f5o8nyF2SRxhVc8jqSi33vTDJsNZ3-vGF5KNjmF8BoWXGEuzpHL38ud8OiLEf5zsMGp9r3Ve3GLEVXa5TrKtoFKMD4xXixX2qmmSftiIkfnFCQlyQH4vaiJDMihPcvhnCyFbF2xXHT9EXrcTGbqbByyprNXm3YKa6nEq5enBQorx6k0OiGxwSGiji3B6ge3kiZ2rg1S7dCSz_-F670SIzWs-j45Cg8ZVFdlcpYtMyZ7GLgWm6DOmW_ApuTUfJNNvvD96YRv2nlWEjEQRnr2wGc1rhvu1dGBeYEtG6_rhhCYyQFYAgydUxkNgNQGNPlHx_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تو زندگی همه باید مثل علیرضا فغانی باشیم که حتی اگه داور فینال جام جهانی هم نشدیم از تلاش کردن تو زندگی ناامید نشیم. امید کلید پیروزیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV0bykgMIPge3TPs7ONxHCNsEW59pgU_WnGTk7UpVkf8LGoCPA6au6rQmB5prYXsjzXgREeAgLa3_mlTA18GXPkNwIlriN6JH5A572Id4MRzOSVSxqcIRgmj5BVY5HKvsiGRZ06g1bKEind6h6gyT4scIQjOX5Ux3nB8QPG0SQjr32ALXbEFbrmLfF1NkkwTo0J2-ftr8JeIA1W09zzyj6CoHdihdNDVDUBIxk9BJrWumIJrI-kdwHV6IM1SIyLtCJoyMfT4XYAKvd9CamaOAD7DQ04F4gd4cEq6qkp_m2z-iMxiYtBxUUJm7NAWvckL5FiB7MTzO1mZ-tFt4pu5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcMnVf1hDV7EOw8hBpUleVHFmZbYGh77HpPxXTOIjLGSuBNxf_EqQINrmiRsWV9HGwzytAkg3hnV1xCIoEJAnqFHRw6sDQ_AnE_QgZtbB30XzifOXCqh-qvpIavSweUrGhvP-c0_mlmL_pyR399BQlOUzoU0oO602fZoTfM9dIGuWr3OUpRGIXkNd711X5DpSW_BtR-6t47_vIjfi97AYL7IIi2FbJ9dHhT1l_rAYzgyu_wLLJx_4sp37mp3DryTQ1V5ih1UPuBwfzucejMJnsdYjCb5LGTFjiuFSNQz5eu0nOIbw_risM5dMFx1YAXXeCQgetr7QTfJxvZq7XnnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntVQhJnay-t_biNhDj-9PaycKdk6F8D7zLA9_xr529YRYZ6yf5M6hb3v8BRTyEGwYnMt2onqI3V1vGAUBM-egE-uRctI5iOm3r2TzrTWcLZL8fLvnlbWeDbnL05immLhCjHSjhyVfqcetQdBOhRZp8FUNfNNd_S7XQzyVVWn-5h30SzsfVjbHHcWzAXwbGpKkESl0A1aV2EDTQD6T54HQ9htSEn7__cxaLL498i-BpVxD_YozJCgl3FW4bpPhebUjM6lX88oLPNXwcJFmENf-kqFfRH8XHat5wPD-oquruKR9JqpYKBbBxR87mi1ZhDmtT2nlfLCRMH9SrTSJn1gcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNbS6FrDAXcvTuzmu8Tydtn4j5FiEyU7nLZUx-KYYNwcbxSJa0UboVHiBk8HnlINK-wBkJY5I8RdRMHrK2H2Vx14EAwCJyirJqU__9yzE4EEzWd7QK9QCLbyLFEbxCAFS7myOTbY6B0DonK2vq4mFF5TiV4HLh5Bg80lbmdsd7bgCTzQPYESo03QzbMshCt_FHHO_QMxLMuheVqfzeeSDY8HDl2jSama5-WTJGPOMG1VClPXlQxWmmEromiyrGOy2OZPPlrmOR0_9FAbyMzIVlzyJTTFpxZFNGGzido_yO973z5ck_hd-7EiICGXB7WvcGY08MQu-neTkqREr-gbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=EAMbJqf3oQ8sMyud_PqagSI86atBqirxrWb-vuKuQ_yIxNyg-0X4x6mYsc6q-Rsf2Epy3HaYzEhJJA-wXZwDTO2BDG4tAEpHBqSkEuxf9NAoJhnEjq3TA7UF00wf6OWKylyZsKjaSKkkZ046L7a-tBnqmi2JehZPm4OGNtelnPyYHl5iwjOPAP_qwcS0Yw0VPOLBDzwu0lz0hHT6HayVO-_VsPfmYBV3AkXtJYTvS5MGAXJBgDNXDDiVlwUm2tw9pq7onUERMX5GHlEVhu4Xi5s18_T4t0n6RXKduLa6_eS8k3NhAE77mzhxF_E0wX4Dnd0RG07qQiDjPW5E3P1bqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=EAMbJqf3oQ8sMyud_PqagSI86atBqirxrWb-vuKuQ_yIxNyg-0X4x6mYsc6q-Rsf2Epy3HaYzEhJJA-wXZwDTO2BDG4tAEpHBqSkEuxf9NAoJhnEjq3TA7UF00wf6OWKylyZsKjaSKkkZ046L7a-tBnqmi2JehZPm4OGNtelnPyYHl5iwjOPAP_qwcS0Yw0VPOLBDzwu0lz0hHT6HayVO-_VsPfmYBV3AkXtJYTvS5MGAXJBgDNXDDiVlwUm2tw9pq7onUERMX5GHlEVhu4Xi5s18_T4t0n6RXKduLa6_eS8k3NhAE77mzhxF_E0wX4Dnd0RG07qQiDjPW5E3P1bqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuAfZjPtzJExFzxg-B2ntzgvj7NJcA82yPuQvYgroIb2VtPOPWirRdyIxlrvcl0z0Ye2rCc0E7t_pGlR3W10L0nbJZ4EbfIoFHZXbeve1e5ft8ragpB-e9hBn0uY7t7rFadV-0_0uJp9p0SX8Xl3rJ03bxpfJmZ-1THWfCs6fkExgxSMSTkynLD9_sRQBCPfWK1XxOZ7FiolPyrB9pUtAVMhAmk6UpS7tBH2W7n7MWzRrkzMwLqm1IpQhHIXvI7j8191WZ2ftM6z1JvZeZxDw3N_3Ufs-co0QKWmGDWmtuHB276qBy4kkzGxkNenXMSeQvvBYTP5JfX07sRMZcn0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad1YR_91Rbyag2YfSWUIAAMKjgwroaw4L5L7ghluLFcJeua7SBUsa6GjUZFKyAaV0fQoa6rqdpO0sS08xXK0X8pAZbHOnCJkajSo4rRRCn_tEdc-Ba4tZ__NDzqRvF1izZi7Q_V0ksgcJWRgaSr1KUAFNr125mq-fiLutNKxwxRnv2f5vgiRqWMlCLeEjT1jvaOfVn6bVUBU50qdLSiVjcqTtR4b_GsNnWdVjf4n8Wsb5Y8GpJvF1LWxOULBRJgNmSQ9GPJfXd562ifh8D7ChUelcs0yB3VjPctzG_TNB7K-6eFQnfj9ZYUDya-siyLT3qJoagStzqGusk0udY4bKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K76ITIPye2q7Zd2O3zdTKd8-lXKjBaEEy7jKT3kxn162JPHvy13snh-os-4eoDv3vUXyJ71soY2FkqWhJZjmuGFqW5lY1agvxMp4DblpCWYzFPruoefe5Q11ap0puxZ46UUDe93XGR8jgmArDmnJnwh9BtlPOgYKjadMT6C3sPmpN0CDHYTp_pYaHXO4O9yWtskhIs158coVy6WOMgXmhzAMANSnGigPQ8BrGxh1eVT-KaT_yS8gVvpXnqAMiRjyloTzpiByyds3CZvqQLYs_L3pkcYYZyLvOK3RKRm-t6KvYnSLa4Li6IcqjPmzcy4UifW0QbbarAwzOt0qxsOpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQQwEkJlv71g1BV-WSIfFaGABErZ17w0RJnSYkqM3HzLf8FNmlNLipSRHRRPrlUr3p6gl75Gdpkm6R8ShYpBaHM9_1QJ1a3DhdGZQpuQbLBKgFtZEYJ3_JaECUgOGH1I96sYTdtRxYUM-GXmYKHePfjx2_yh8BFciYWRGIgZSNjZ5VsrbQOfY4qgLI_YL82FE7ye1PfxK71_22kg6x4k3EYn5L8h04b1zIGDwUyARkG3qc9RQfzAgAJ6pYdesoPElh-MQlqcD-WkhCO3Uip7xHdiKHKl1xGUzy1dTIm5K8yDFRxEG_uVI3Lj_NgbSSyB7v60rLnHuZ4IK-bCHy9uAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyDZUAa_VtdKW_bNSgMy6PxNeoPM4ESVmIWGTAAGGaxzQpq3m3a2IICX2Qwcifa1Y_BpT6zvZ72D3yQV5p3VuOwIKLD0JI_vlcwjN5acyem4mHmVtdIE2r6wPLdvACxvcnU8C_zcn3qh9Dr7oaM2sZtKNUBQxhooGJXStDWW82tvin42d9-Xcci6eesyTwqrq2N0_k5G-5yoCB11hOVxwDldmeNfLVWjEQ96kXeM99FkWm4nfSYUuyTXDhCaBLynJ7gfSQ8nm1xgez-2nM37gIPgZOlof_8WB6lTU9NegOkoPLgPuFexJvv7ou2z5xH7mQ3zra23Sixm_mLJFtCnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfHEcZQIiHq-oYa48qM3xYnESBnUbmYyWpqq_xsbxjdIlHqLcBVkiUSrGlH4qC-ZYDhVCC5bi6-oDo4TPYMu6oqse_s5krLEKW_wuZk0rj5vPGTfmwfTyLeXPy_F1JDrf4KOdI1S6bR2uXjen__bxsAjkDk4BO0xKCUfzEVZv1vYB5xQu39hKJn1hBC-9nn68jOtoXyrcQMdtuGZseeMPwr449jqwhTZcyU6YUhTkjJiilMQy2K1ogzGSxczPaceCvS4JVRNAGCz683pYKjAmBY-RRhTLgl3jsQbtNrHKhfS0aheo3ABCQkSnil0h3gPZ0Q-WkldlpGKHsbabNc02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc5zcuiReqPoyoaY3lYjl-6qtcTSPDYJn7nVx6fpBOJxDRf8R-evYb-2rB8GwLf81uJs1wNWVuM2kKRJ1rBPckk_Tb4BJMa49Owf6m8NDBVeyElEkrP4YreZ3npTYEOyCrMSTHI1Q3dR7OGfCkiFe1rFyMkDgOAKydaa_-dTCaI2fzCIOfV_Qc6SulWA1Zygys5CTvs_Z-q1GqVr1buBWzVrOhgkVkiQWzxCJvGe13FOna38RS9JGzkY7js5BeNMXrFASFDQn7EKSwLuiUGazKZsGpUQaGmZyd8BbTKE2DvMwTf9I351hV8HVtVgl89-h7eHXBVu4uApHbQ1XKuaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25991">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmnFIR_bQkyYZkmLqfVijCbpWm3UTJe9RDA-W9lcW-OhnKbavphUvxnPCrot_OyJd5rM_5fvPY3-Gh7Rscnk_6h_P0nfi3oudgJa6sh0UYdIzpiC7AbBQ8scd6b_zFHM0vMmb6X6CC9H1SEkCNTUGlQSVtUsjLsB1JStp50ZMwQ3220epAisvAjAn0k3tgGOWbMiytz16e65eUSa73iUKbpJDRrQPDlsFGCz5jym9HT9y-2ISF_KZZJ8o6311JWdr4Sa8RomMGtv3iXKba03bT-B9Wciae243gbYxtW3Lfsd5i84oHgHXIyilA72iNSt5F723ck9-l41BPuztbLOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ از طریق نزدیکان خودِ محمد جواد حسین نژاد درحال‌پیگیری‌هستیم‌که ببینیم طبق گفته علی‌تاجرنیا باشگاه‌استقلال‌باباشگاه ماخاچ قلعه برای گرفتن‌رضایت‌نامه به توافق کامل رسیده یا که خیر!
🔵
تااینجاش روخبرداریم‌که استقلال با حسین نژاد به توافق شخصی رسیده…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25991" target="_blank">📅 16:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25990">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCWbUZz_R8u0iAny-4CPqyWqJdWmlVKEHKPWR4pgoNSjrWL_8g0xiwBexQ-CKjAV7XSQda2oLUK6VvjvONteMfxRqhBIZkb5rU6wzy1DTxzAYhKfCZ9cGnOMgHKyGK_7UUY5sKztwG1ciXnLisq6Wo5Q-kJ2nYiDmgRdoVlD8_9QcbQdoxrkO-eUDPXc-rrazIgORZq4G6oH8h2yvyWF1ee7LaY8_sFeV3nHPcOHtFg-Ar4wagzMO2AmwfELyL1Q1hV7m_T-YIx25S_IlyhYAqr9EcFD3z8cDl2AvtJkWkhu6UXhK8khmvZtfBeuMRpUFYicKcdu7qmlazRF3LjW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25990" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25989">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6s2OxTMlZE8E39vPBYz6PhBxK5lBEVCY4g01CRIptUnGWo_Np85ncz_yLwbviV39eobuEjzDU9sKa8OLtbq3jpTjy4wAHenjgCYFCXVtdznoFXLKvW8FvYh0p6yCweRuQcv7K4C04BY8dHj6KXZo5aFIWCeQQ16OrU0n5ruWHu4Ekp5Zbri5b3W6M8q4ZEVKqmlKBHkHY0jueK-7Mgb8c-8Jug_K6evSgryy_4ujcYzbEYDMmYI9urf2H9PhRuyMvdsHa8zazmybHvAAKnl4JXAl0HJMeAFjo9GTSbfw_S9X4HPx41_JTbgyhVFALPvJL4eRYczuRFIvAP_Jgo_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25989" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25988">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdV0XKG_1etBuwYYj8dgZZ-xUPilW5P9WWsnOybHmsyfslHPVLAHlKhWNPmFlq93QCKNdFkopK0ts-av7j_T8pALAuStwG2j4qq6Tu0x3-8XCKuwwFYSn7Bu8212FZNX1myahXnxhGT6kqZRKWZ40faQLZhN4XG4epN-R0BWSehMjt7QxiZh0-jwwPQQsGTB0ewgxPNWMIjrLtyc0xOSz4TdCV-RHp5cXIzVIOgeDC7KFDi_IFc1Y-pZMKPiTO0TGxcoyEIZpgr0l1juBiSLmL0Ky9rI_i6S37ggsu2Tkv2K3zxzWEerR-AH8dJ-IT5KVIGtoHnx3qCu-shMYxJCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ یاسر آسانی برای فصل آینده حضور در استقلال 1.5 میلیون دلار خواسته و ازطریق‌مدیربرنامه‌خود به باشگاه استقلال گفته درصورتیکه بادرخواستش موافقت کنند حاضره قراردادش رو باآبی‌ها به‌مدت‌سه فصل تمدید کند اما در غیر این صورت ظرف 24…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25988" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/letSSacSNE1zBj5x7PYPzZgL9qAVbMr9fyqNKmZRiNTz_1K4tLThRojlrULGNDr7PukkhsStCsIrI69N51g2FcmMiNcYfot0937WID_NIfi4AqzAStXQNQ6SVH_ZWFJ-As3nxPvtPgTEmnopdtCYMEegmXBaOWBLXrNm4YSE0QmrcHxmyvpOcr6cf53R6AVRv8YS4h-ooPBZpuCjW3xM7nlwaK6PuBzRyQ6LGwF9J0O80nQ_ep15LJlpScEX8XjyZ6rYPtWOGCrBDPOINl7YU-BuyWa3bxjoWdavVD9sw-FEtbGwOaZqH-PqZ3cCK8veEk_LYJ7zilc82wTQR5vqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق جدید ترین شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ظرف همین‌هفته‌از تمدیدی‌های خود یعنی روزبه چشمی، علیرضا کوشکی و محمد حسین اسلامی رونمایی‌خواهدکرد. همانطور پیش‌ترنیز خبر دادیم تمام توافقات با این 3 نفر انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25987" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEoZq0kj_4D9q4FUo5unDigc1WS3cMz1yLIXJ6A3naWTrpWKYAGdVcVB2GOKO-frXKUFCq51D4Mf4BPRszZh4ihxOcObwA5_S9W_Cy60CfHSUNuDURNV59C7JJGGSptfimYII8cUbBIAuiqpqGyU-NXwi6jTzpk3cTif2gAXH_BQxLJKuZsfatPMTR2gDXDecnhncK7qvr0Wtmn9WaKL9wkVuLis6_Ys75V_DuN9W0-_-2tlr9aUnmOXkDBAc_bw00wfYb6QXYeyoNmQFAmH9dZ7Vo-Ct1Cq8Ysmz4wQVzl09bncadgGx3Qdd7MebzVTwQdTOrCEXm2wawIxDuv8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی؛ امروز حوالی ساعت پنج عصر جلسه مهم‌سرنوشت‌سازی‌بین‌مدیران دوتیم نساجی و پرسپولیس‌برای‌انتقال دانیال ایری و کسری طاهری به این تیم دارند. طبق شنیده‌های پرشیانا احتمال اینکه این دو انتقال انجام شود بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/25986" target="_blank">📅 14:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25985">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuurfHa7UQwOKLBKtCEJg48uKVLm2Dx-2EIKxI1dpnuK9MzxKBWkkVLrzxs0ADg-JYemP5UvdfeETZphUgjR0kxzjKjTjAlK5kwx8dwZKJiDk9H61UgYUOjdHFKVEmoJ6XACeEBy9W1orUk7gQlus5srAR5C-UqVKy_ZQ_T18yxloHfxkso6l_DqPC7G8sOIxTw5nhxiZTs3iwrlyxrNJyhnxp2XUEXmDlu-jeiaoQoc57gv8AY161NqpRPKIljBPo8HpqM4e8u4WQ8hiBTlapDEGdRe8ohbxSpKWV5bhbd2p8tLtNouXc6HkexmlyKhO3wyl6ZbVl_i7keVqsKXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/25985" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK-RTdjInVOeoDtvK9RMnzjW4XAO7DQmW1NMbuD_99aU28FhUWtxBXY0QbhrK9gMo8bpmeKze6Ic5XiaUeYB-VKed72bHXC867SaHR_1Bu3n3EXJ-m94Lb0x28Ix3jVLATMAu-WE062U0aLkQEnYJ5nn21wJaYBot1G-3U9lA4NsCIeBxDI8Ju1XiRV4FGFTMyH-faoTtSyL2fPoi24SSBMRDlh2SEIhiAzF4wFxkBXv3Vgcggjc74_TVAAi7pp01jbTXYCbg9MUhA1dqkYx0XkCA-sHAxoB-MarRoj8OcUXdxkqzrw0GMCqeKArE5Y6ZJXEB0JLPDKd3mqWRRF2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
👤
طبق اخبار دریافتی پرسپولیس؛ کسری طاهری از مدیران‌تیم‌نساجی‌خواسته‌ که کمک کنند در همین پنجره‌باقراردادی‌قرضی همراه بابند خرید دائمی به پرسپولیس بپیوندد. زندی مدیرعامل نساجی قول داده که همکاری کند این انتقال بزودی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/25984" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25983">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAh7unE6AtwOzXxr_uNUYke_cAeKmjsCPZiP3Tm_WhCVqPN7nP1wppFD_aqQW606xitvJ_NdvLso8d9SBy_XMXEw0X9Rcr2BSqHmc1qGp938hr4G99rRWfZk0WXrMdMcR-pUtHeEc6n_FIpqxqDyAl1u4_ZQJqqwDENMhHNr2kWDt6b1oXMHUacOq0Lx9TaAUrSiasENrV_-Nfw2p3AR2bwtjUhQUrtmalDsJc1hhwWhJ0TRU_vTexSiGMz-u051d8GQ9E84SSxBzyet9mUCjd7MaSnIX9CecoYHwlZ1kKAXPtFWQWxUFdA2C3KmjyeG0iVaL0p8m2cwJxkm_3odDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/25983" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25982">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikU1HCUL9NdbIj48lEQLhTP9hOUVB7n4XyoykrN7vusMrFAcRKVUN5X6Wb9m-abNzZEemU1DQPPzt8_pOe1rGjwmXHp6_rMcqf4nImFxgPQQru7hoG6ojiyvNis_6zYadHrmkCRIgtpEsYK9mwdtIKIP0IVtTkoY1NIbYU8zs5qJOt93cHeh6pKxqCnF-nfp0VBkbaNvnwNDtQcjr4S7mu3m3QriDYX4SHL7NKrWRR7EbbhSojbu3kaJ9f_kNiA8IpiuBRzfnzji6r36O2RpFTH4GN1HfviQiT90Uj6tTJAqfqrRPt43JcaIERAHEOCaaBLvIf3XvyBuDWGJG0_Hbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ تاجرنیا رئیس‌هیات‌مدیره استقلال: مابامحمدجواد حسین نژاد و باشگاه ماخاچ قلعه برای جذب این‌بازیکن به توافق کامل رسیده‌ایم و بزودی با حسین نژاد قراردادی چهار ساله امضا خواهیم کرد.
🔵
علی تاجرنیا نیز اعلام کرد که تکلیف نهایی پنجره نقل‌وانتقالاتی دوشنبه‌رسمامشخص…</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/persiana_Soccer/25982" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI0ceau6TzA5AhhLc4B21uZ8iHCY_Pl0Cg3vy9yln8j-0syQwveq2d5Vul-ICpQ4JFod26USHUf08bUysA5W0_YRAZETPM7Elmx-f4Bx5_3dWpUp19KodvZ-p7x6KC-qBl0j-oQf_ASVEvZ3fSZwjq0tYNmTn8e1_-NGF030Jy4giHbh6nvBMCr7sZn_Ujj81-5gFhS7BO21u_0GkIQQdKzJEqTlMuJducG_XD0ij2dWmX5aqKoLmQ0DronZiioShnDy3JOzNh2k-jXUVyJFzvKhEtWWJTJmKl0c0MFOVDTDJchP5f6u9-bR2-ZCDtBTPeh6veVAlDALgnGJYOG2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25980">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNoZoTdawhVPCDPOZlPPN4Ur1l2MNFJ0y-MeiEiN-o7mnjPDPxgAVSkygwJgfpEqdOTINdogrwfyBaCjRMQJMqG24alxV3GehoZVQDeYVa3v3TbR2BAlW02UmWUfRKqpBm7NOQbxHiXD7NbbMKIQ578VANYGAh8IB70qqK8W6fYFFd_HVftsWem9vtF4aSQq-RDqP2WMhSFwDFPXK01dg7tb_gJOgD2DSImHDM9SAfpEp58E9MrlM8wf4b660-HNnlHhIVqBGiXT3KZU9hijC5kU5tEcYkIe886w05XzDoZ5o7-4AVkGPMEDaTNrfaZ2qNu3PiQY2ZNE20k4kLZ4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/persiana_Soccer/25980" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25979">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-0lxUX1W39qB7nhuglGKKYurWjAeT-mQsKzYJ5DW_natEpRByDjm1sDAPwogkx3SXVJOPzQ2wQEXjpq9xwmixn1YemqvDutryTpRjcsEUFGzAw0rklW4Fil_UBNFPhh_cE7ssHtgo8wo7jIdA_EEdx9Dr8PrQJEXf8igEpjrj9la3p5ofNnlxD78wQcasvAT1IhhMzZqD2iv_UtgLJZQAaV7XTampvOvONKgQ7mAvkIFKKXxUl3ORPlccbSU36aDPxZg9aqNFpneLmCf_Yd1cbmnpLAVF96sntix4w7ZiPqhYbjqVTiQTUhM4e9BumXU5Fwm_FDY-skONpXq5iLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه تراکتور امروز پیشنهاد تمدید قرارداد سه ساله به مهدی هاشم نژاد ستاره جوان این‌تیم داده که رقم بسیار بالایی هم به او پیشنهادشده‌است. حالا دیگه‌باید صبر کرد و دید هاشم نژاد تمایل به ماندن دارد یا رفتن از تبریز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/persiana_Soccer/25979" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25978">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLnaBoB_S-leghoEejC7G-MytQy58uKimHdFaP-eXdcFhP1uC9ejjqruCJZzKdKXfCUAdfeFcg9Tfzm5ShZfeXxWOd3QmYauXYB4VrAe-6aO-2D4sL3NJT0u52kektQGIpATkuIB5r8JxTau066bms56B40mxNQZgwwOhJJFm-OLvRneoXrpw7oSztHTmIBfc6uWOI3d42fc_RWeFbxxmIHcc_ReQ-zQPUMrULDu3w59qkNQBH0hf2PxQUIOJDtxIgGyd_wPLeQbFl4oq6kmRYFFj-qjE360cs82fkDNtmuyaKsLKYuYDc-5fUXBxPBSHBFEc0cqXIwNlWQpdkjyUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#اختصاصی‌_پرشیانا #فوری؛ مدیریت اتحاد کلبا ساعتی قبل پاسخ‌ نامه باشگاه پرسپولیس روداد. این باشگاه‌اماراتی طی ایمیلی به سرخپوشان رقم‌ رضایت‌ نامه سامان قدوس هافبک‌ بازی ساز 32 ساله خود را تنها 500 هزار دلار تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/persiana_Soccer/25978" target="_blank">📅 12:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25977">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgMD_6oQXm3I04AEMVyrsR3ralPZgMqKoRK0ExVupBCrwj8hTdhBIXFvUdqtvY0iKfo0CmQz-_uyyfxcSMqRGBVXS8XYaEGTiIuvU7dDWNvxD0ME-Jo9Vncy-yklsNv4LoRN11pR7jkFumdg26-IMmdwQKUy22eaoL5dnWiUayG9ysE_2GOX8JtOJSrNc7Qt3SylWj1LpoGIrFp2vDapKifsH1PEogGgKeS5dts0XpEUFTDIrr-R2fJlxfXMu_y_lK3ni2Db7QaY8EzMVTVM6akgT6DEJQLU87NZnMUq0bDMHUz8vs60PrSBoUuGvnS9ExIHHZVqRN_QhhrC6rjELA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های…</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/persiana_Soccer/25977" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25976">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0vYObZ25CdA8U6B4KcTNgIbvDN8wypu9Wlk539XzAFHE9TcSgg4LxTT39YkRSwVAB6ws-OE2S_RaeO3hMdPckauMI3j06VtlxQQAF10q4iYyYoOHJZ_yDK8OY_5olBGGc0E2AQjH5DqBAyZmWHLeOH5NWptv4Ftz9IlNFmBy-fsG6brMlBrSJ-JZEYgm3pXuZcQ7bzob4lW2atf2F80CtF6AGQjH3XeRTcvgy9Ax_ucHZPLoh6tlYJfCCLkEY265O9aQ1DTCTuCWRqCByjVSpn1T0zZFuoMtzmU3aIBtwxFd7w7Tb-mbYEx98y54b-gzbVoV977c4eIULmFdhzgkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیربرنامه‌های یاسر آسانی ستاره فصل قبل استقلال برای جلسه با علی تاجرنیا دقایقی قبل وارد باشگاه استقلال شد. هلدینگ خلیج فارس به مدیران استقلال اعلام‌کرده‌اندکه به هر شکلی که شده آسانی رو برای فصل بعد نگه دارند. ایجنت آسانی نیز اعلام کرده آسانی هنوز نامه…</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/persiana_Soccer/25976" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHB6CV7OCEJCuIzOVYxNvV0f0MVNlLDsQjYuvmxKnE-21F3kysTxjUtagxirhI8kwLoMq50niLt0xMNHeCdBvIiF8MueQFhjQX9jwSEbE3d7bHgup2I7WLV5HBpEp2prdEXaEYJRX6dA9g3oiUquVSmrAk1T-UhtDAndy0IOYTFOWkpRD1aspqGakinf9JW_QFf04-v5e4SraieIU_pPMjk_JRHf1ivKMZRHr7aHxCHEUWpEBC4iNeosYcmBMzbR12KoWZwnlhyb9LTd8bZpAaXHHWouxkCqEPt6XfxSWR6NdM6nTNgofJUE72e_mk0YmNpw6wLn3VfnGQRl6aUJkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqVE-ex3Ah0C5jhOfVOQvKroTnPDuDbd2yzhu1mIDEJLkGetM8EJdwz8x34IUmxfV6nSjkMat9bLxgIpQOHps0dztb3c__E62hACySmCO7KtNwq0hoaDkKksbQm8SfFoDffZKHWqYNWPy_lUM6eivBOihO2c4XSlqDIZEkwes3IX6QyUeT-T3YfTDIOdCCQfOonOAaRIgSnV-i6fe8zx9IAIHSN5dpSGaDCcCFMgWNnfAh66K0twPZo0-vp2mrKbXOjMsqlo-5fasnIiHAFVu1hCww7vCTOHksh3IQGyFx8lzsp0MPwt8GbK1Ik8XF-5vCjcAWJxOfcT-ZKgIb_VWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=iPgwswqN--qb-iwAnaieaEzsZoTIC-u5aTDl3fTSSOR6swbo1-RsfVUfybVzRrkL1zHpWe13ZpNVkrGtLTcwKWk_HPH4lGvvxLiEsz_4VJu71UgiBMuMjKQ5XqRjTxbwJ_7ZuFmI4La83oEdv3OjKV4bCdtnjmFbaVIHE0lG9vFqeNUc249CQKbmf3ZFFfsSRY_rSRn1o9B09mKklC7KsPHX877qkULYAmpSAiTSFs8qQE3Bh3He0Gi6qgiiG8rMeVv4WK-5A3V16TRwZku8W4nWRaYpDoY14v3UJPKlOOJlw4KDlo93rOkygacT1ajuzfmTNuaL_rmSJhA2jolYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=iPgwswqN--qb-iwAnaieaEzsZoTIC-u5aTDl3fTSSOR6swbo1-RsfVUfybVzRrkL1zHpWe13ZpNVkrGtLTcwKWk_HPH4lGvvxLiEsz_4VJu71UgiBMuMjKQ5XqRjTxbwJ_7ZuFmI4La83oEdv3OjKV4bCdtnjmFbaVIHE0lG9vFqeNUc249CQKbmf3ZFFfsSRY_rSRn1o9B09mKklC7KsPHX877qkULYAmpSAiTSFs8qQE3Bh3He0Gi6qgiiG8rMeVv4WK-5A3V16TRwZku8W4nWRaYpDoY14v3UJPKlOOJlw4KDlo93rOkygacT1ajuzfmTNuaL_rmSJhA2jolYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین:
بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25971">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7xizDa-i_APBKGAhx5Zr9mf2HoQLxRl3vxPfDyclD6d_DvWZGQJdeLiC00sLIW2r4HkjGsHZtW712HSzvekn_BKC7dFiAgGhmSU1fUU5-EMm9Sxvl6i9ceth5Zmdq23_hx-IVmgxrEFSFwoAs8aRNQhfjvod4vn2RmpbwhuL1KQW6baxrxreVy46o__si5TQqX8_7UsBmMKFnVUtN1h2AQzKD-4NRQYY_vL_zxeJTMqL1WRJJmfGjB1IvR2m6TbrVWFugUCy9_M8T2Gy_G3icpSgP4NTk-w7GhYK0_VJMHRcree6cnNKMjL1aIw7HNfNJKnQsJScHgDjLNZEDk1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrxmIttW62KZQCGQsaP36QQVjN6FBmY-QFj72750LBOqIyeLeWEyT26vrSj8ETDBN2Z6uTLeTrl3_mbHP_l9fXUA0k2CylErxr_dWBPE2hkpuQtmmBB870K0N0iY-wC1vJeSITXi6x0V9uoJ_Ullk6kaOHR8O1xstazx8CEIy5PNq1aOM0HeZ1ssY1j1YRLu93Sw6E3HAS48Le-psNvw3cU30kIdHTdii-yWb7gmSb-SqSVUsK1tXO1Ox2wo3gQRp2-XBblhNk5h1RJWnGrPf7maAgLsGwO7eecvTnyWpQd0DtK8ZWJ4fMb-0kxyuidj26FX8W40pyzxns4lF5K7Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پیش‌بینی جدید پارتنر لامین یامال از نتیجه بازی نیمه‌نهایی: اسپانیا بانتیجه 3 بر 2 فرانسه رو شکست خواهدداد و راهی‌فینال‌جام‌جهانی 2026 خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25971" target="_blank">📅 11:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25970">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS8HK1WX3jYoUgG6sMnxxpbQL0Z9DBPjm_hQpT3fa5PaygLnJmFrbrXVZq_dO6fLcMnbiOHRhk_5Ie9OlGzY1yekhGoz9dycP3wv7oW7n7ogRgW67Jk_SAnxwYL7HyMw8XhmHH5Xkgsv4wjh_If8i5g5veJi7DKlxj4AuGXF9vafNfw-XNm_WSWb5Sj-USNgknclk4p4Dn3w2fiK0JWmeR3_DNpYB6s5nkLHo3PSpItmbXo9IVjR51qh6MYcTYA0s1Ni_dZCV8YIU5r9lcT3CtvEVeswsCgkndhs95KYPvn_ORRmf34UU9GsoX5Zz1MEdt1RgaHEbQtRmXhf7h0iGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/25970" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25969">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVM_2sQYYpHXfoI-lvCabHbQ1qLyMHomY-7lw62o7lYg5buh6o6Vpt9g09qHnpDvWJWcXY0BcEZ0AzwNQ0B63tnLazh3wNYPRKgIlckreGrQVbvV-AnEX_aOGq7qVztwfTLwcjiT3fRmi35JFUuYfj0MY78a43qEJCX0waSJizUbtbCAth5E57_uX7ZdxrCNsTyEzbPfhES6BbVWxXeOU9NzofdZqR1UqFtXw5iIfNgMG_jDvoxpLcolSa0sVskipZHrMA1Iqzjs44h5ONxpwSJ0uoJ9rMXmxBfaQhmkTuauc7EoWiGRXay8ZyEOW91L0Q5MuiGlWCSn0Pt6Cm6jxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25969" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25968">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4Wxs2ShVA2i8fkkN8dWl6JZ76N5Z13iNrcj3t4nV4Y_h_JJ_JkD-J9uvxBrIo2QugUNvX12HLzRS38NrVd_8cfcfF5bt-mpXFm1yfANPhDprfrL5tkIVd79CIN7WrrrnnbhSly-rtDTbfnHhDe6FmWlnzfOjy9Fry_OFkhiGRW2IH_wg24TB1EIGevDM8YlJE9De31Y1v0-61HoeuRf2ZGOBOPS3A8mnwHWUvpQF6AexwGqExGJl_SgKbzqxxsMnwg7ap-Au86HdZq5T44mpx_jgmEJKaqVHdzlMQ-lXq_NuTpmpxn4e3FPu2bUmkeGIJojAFH3HQOBvqj1jXzHtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25968" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25967">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=UYUlOXFGSQOLCEHiH3oqZtE1zhdQ-lWZ1bXD5z-VzMIDcVPvQ7Yhth3CgJ5DiXjbCziCvfFjBgxBPbg2sTcvgk0EVsG1zvOYow-R3Dmy66vYZJ4yPLFEgJDtXlDsFQ5u7GDrwUbYM-iI93Ypb9eB_up0FyHl3uqO3MTYdLoxkXKvzeLYItbpt93BRe7yjAxLpHzfVxDw8rn0IJpee-oTmAQyysTqiipfJ1i30FDQ2djH0sAlPteFx9KXIJUt97Ad3HvysahlkZU1_UhL3xbxtGqfcdoJLv7IxV2cnb1apyE0NbqdeePBnxsL0_pXlIsq88nonXXmjB40QiBu890Ifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=UYUlOXFGSQOLCEHiH3oqZtE1zhdQ-lWZ1bXD5z-VzMIDcVPvQ7Yhth3CgJ5DiXjbCziCvfFjBgxBPbg2sTcvgk0EVsG1zvOYow-R3Dmy66vYZJ4yPLFEgJDtXlDsFQ5u7GDrwUbYM-iI93Ypb9eB_up0FyHl3uqO3MTYdLoxkXKvzeLYItbpt93BRe7yjAxLpHzfVxDw8rn0IJpee-oTmAQyysTqiipfJ1i30FDQ2djH0sAlPteFx9KXIJUt97Ad3HvysahlkZU1_UhL3xbxtGqfcdoJLv7IxV2cnb1apyE0NbqdeePBnxsL0_pXlIsq88nonXXmjB40QiBu890Ifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25967" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjLr1CfTy9ALN6fwwVeq0f7FT2R1rOqUFG6Im8iH0vhcGeG2fAahzAUY-V5RMdKXsbVJG_uOaWBUeBQWm9reNQZyaT45UH0hWBCnrIdj-zWJjI1NnXc1CcJeVbN63_pdJiZ5EgWO-jkiTaXgUeax39Sy_WqY_-ZbbTYQexHgAPNHJKCKOF9ReAS1E0wjO0AAU187xxBtc1DPewqqXFHjNHs7fMQYMjONMXhMZ6k-f0mvAfWEY7zwoN1U2OcTx-cxDZcGwp4tbuDj_I_ws-XiTT_NZtr0zpimnyT7tfwQxaUVRoRc3CktZgzCNsakcYPCnORfZ0O3c_gAXVKqyZQkoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTXi8rzu5G6NhovjrdSSyP9ZNMc39mgIoxAGcrtupEyv7oUM0terdzWDnkHMzXf9ikUBoXEsCE8cNxn2FNCmIEKiXaBYYZa9YDpFvvgD_CUutUTi-JdsTDYa98eSW2hB6tUgyxpcYnfgLV1cRKswQgGUl-dKsPnh33E1SWggTvjephlTpnu9IoA1sIuYBF_sG4SuW7aSPBqPAUpzZ2q1zfMPlWfnUAByt2mGHvgD2H5byz1kVwIT4-0QWEoRun7DgWo0veXa1PDMpLNn1XtQFtq4EndJf7CGiBAqPuDZ3Tg1VyBE8CGZh6bLKSmkH8TR3DfpsGHaSkt6NbS_AZ9idw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=b9ZzzXacqVvbMIrI7dNjqNuQDEgHm__MAzY27E8RrTmg6kIVww5f6L01inQuKhgXr1EIn0IkoZTm4l2JcKwOn2CIytfLtVNDKSjgZMndn9rIjCl-h794eehvi7khonYYZPI6-FFhkgDP3EQX8hSuXLm5yVDDNRNtsK3qjmx172-sShBkjtI6EosmkoViMRnR6mnSlpdzwPwNW_ri4GIQ_i5HxjAsOhkDFqXlzc8TYGutDNBUqZ2mm1JcPBe8rQggT2MNI83h8MAJkTRvgBQdqqJGA2qazWIdhtV9XZZsaNa8rbhLStmZkRMwBPtnYKEyaMGPWNB_tD4DDwDppif2KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=b9ZzzXacqVvbMIrI7dNjqNuQDEgHm__MAzY27E8RrTmg6kIVww5f6L01inQuKhgXr1EIn0IkoZTm4l2JcKwOn2CIytfLtVNDKSjgZMndn9rIjCl-h794eehvi7khonYYZPI6-FFhkgDP3EQX8hSuXLm5yVDDNRNtsK3qjmx172-sShBkjtI6EosmkoViMRnR6mnSlpdzwPwNW_ri4GIQ_i5HxjAsOhkDFqXlzc8TYGutDNBUqZ2mm1JcPBe8rQggT2MNI83h8MAJkTRvgBQdqqJGA2qazWIdhtV9XZZsaNa8rbhLStmZkRMwBPtnYKEyaMGPWNB_tD4DDwDppif2KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1WRVcVRhLJK6tmgUxowBiwARoNgFOjmpTXUh-b0VP_3onpI6DYEHGX8SJ7lnob_6783c55Z7_S_f_NfU6ukv5JTvsiwaM9ikOnhdt46aoHg03CZxSnXbQGVlhl-KnUSjOhQh6hp9BGyNy11J7r4Q3ZogeXMFjr0I1v_zp77hoVNiIcpiwudTUVsQbFGYp5PjPxyE1d_ecCO0eL7E2QK8YaVzSKg4HS0G1-F4dgY5a6L6H4-gGCjSZ_qqgTYI35fL8yDBvs69YcdfeUmfpZJoxYRp67jTBSIo6EY6bsCMSmNuvbQYIv7xOBv-UBxbe8xuH_4vHh_7l0VaP2bOGOwMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx7A4N3JXSrKosh0xqqxdgIuH4EthevusAnNfWHixLy0Lv8aFQYMTgT7v6xK7GJtBzGjoCjNJm54ST6TUEqmb995GchnqGnC7liFKzXuOtJNLLGxq5E74SYhW-yRTpA_yd9ecHlBcRiPqnfi4klkewRpxmXdPenDsM2qpEatkJkPV0-8I-UjXGY5RnSGR8NG39Gnv8niHFjCnktGNvJefYemgpCfZ_cDCxUwaW87G9M77dHDenO5RcVPfdd4hYkRo3fa1JQGO7QpRz2vy7oP4qhqaqVOU2dYAyonAJZFjdrGCb6NWXTMwtl3y2RVclvIENOCYakgiKknKstZF8yWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdfsQgPggOiBQ-WhUTGSULiVmJ3zjh1u1ZpAR4jdJ_MHWpg728fYr9gBrtPNVA5_ja9TUKvG4K8kRz3RKTi6PW21Pd6gYyyva9mVRREIzG_vDObonL3HXo369u7uFbK0GG-3GY16pYfGKt-30N0Kp3-Y-QCZf6nVMF4DibU-jB7uVyxAJdmDgrQuIsirm7H5Ex_oCg8MLq5YSObRjdXOu_4CotHYBiRbFYS4c0hmigVtxtUSMWCwkPwb8kgPM7qpaqEF71R2KLQWGAwpaNCHuTaOc7LHCS4cx7hvri5moqdzLwEJFxi9b8CPAvQZ7yzLMxBWnvIjJCn3ljJwzwxrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUWTepYtfeLn7Gt4X4gZiq_qiw2RKvLtEEljibJj7rJ97gq-tdeSHUgAE2KCwGLLq8cxwnefzxZvfWgoZ5zrX8HzF-ySskemxBiCK_f2NphFTUU2vRfxl-fXhAfF9l_Z_WohGurH5V7ww3jkENqj3kFJtqZypcC5jP3W1FcMlX556vxm8fg3evQaUr028F3wUxI5o40sQA_v-Q1ozTL5uTnjLlUEPMavl12bPailak25jPk_LVMU3H-wAkdFJxeHortOSEWJFim3wlPm9tBUIOqrTIjU4aeAJHM9-9I3YNCA6NY_Q3MiAfdYEy1halCY1JCf3T0gFE5jD0Kpl2viwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=iAWuT_f6yUS1R4D21nq5sdY6tC03jRIknic3ibJ0bmdfVYALFCQP-LAgF0s_2RJi-d4PEegJuvPWzXjE30cuTcUubxRraeh0j4I73dOlLyAUfn6zXUETDrzybK0JXCnNUcdG1c4Ylwn8ji3jxApR5OScMJkVL5UJVfLUCP0mkHS51tooQklaFRaI7j1Y5vj-hcAFkI-2zWEvWlLwY2-8-k46Hc4YPU1hMnxi49Pu1747xXbK_I6wO8ene3H0FW4okyOPe7YUieuIQ2K7fy8bciHKNQkxLb6Rz2Zk3D9-4I_SeVnvNs_H4n45LTyLwaffuCR9WWWahgzZTmnD32IUFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=iAWuT_f6yUS1R4D21nq5sdY6tC03jRIknic3ibJ0bmdfVYALFCQP-LAgF0s_2RJi-d4PEegJuvPWzXjE30cuTcUubxRraeh0j4I73dOlLyAUfn6zXUETDrzybK0JXCnNUcdG1c4Ylwn8ji3jxApR5OScMJkVL5UJVfLUCP0mkHS51tooQklaFRaI7j1Y5vj-hcAFkI-2zWEvWlLwY2-8-k46Hc4YPU1hMnxi49Pu1747xXbK_I6wO8ene3H0FW4okyOPe7YUieuIQ2K7fy8bciHKNQkxLb6Rz2Zk3D9-4I_SeVnvNs_H4n45LTyLwaffuCR9WWWahgzZTmnD32IUFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌علیرضافغانی از علی آقا دایی: طبق قانون سه بارپنالتی علی آقا دایی رو تکرار دادم چون ابراهیم‌شکوری زودتر میومد تو محوطه جریمه من‌هم‌مجبورمیشدم تکرار بدم. علی اومد گفت بجون داداش تا صبم تکرار میدادی من باز گلش میکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhUz0pjHeSP2ePj6eG20gy0y6RiCqBy-k36Jl8giE14Rltm_-XQf7rInlAmvi4m0exfjL6hwMBmVwLwFcXt-ifyrx_4vTY--DxuxYAD9sixFkPFRDCkagFCgu_wJIHKtiHtbkjtVw54L56KFJ96oTFE_2lPR4QyAXYX22uFXaOg_19oO-1BcndaGVy3YC-rx1J1-B3MBovhsr2vR4uaW52X5RqNyNvcwdoHSXqyC0BEyy7x_AZFErlnGmDpDYXNlXMfpqQY7BJDPj7J8fQlNH5HM2GvRWyEii3BrQhqtQ1SEewG495D54P_md8gNoOcwhT5bD5c31PKqk3Vm3SAHuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRn5e9VUd7wpTuAw5QyxnYoCzO3QHc8l0xJXOHoykliPjlj0aGK8ksatrbEezcvefucTdFqKzN87eicjmwfx4XmK6GepIuLJzPiVlTU2H6ct6xUS4yYMbeYJJM7PK5tbNrFdPRO741Z8lFKBHfAlmgzS_DmhaHkCEEbv6smPCzfp4WIMFFC54yfM5XohCA6WCSxcJKpd0g0D_c8WmzKtT7b4mb-xSKrMUstf35IxKZ6FbZFM3owmMihjJRU2i56quXF0t09wgymg-YQbwXJQUeOCrB67oPfkPSo7gRwMwvKph4b_-ovzVqJTE_gkYUpwS7iFvGWjMXcVXVRIiEkxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp6zPw-PRQCINlVIEqcpJ3K3Jmt8qRpnYQjPeZU0OTFUFjAx9Wdlug7wQR8CoV6U57W5XGHf__NSo0SUdo38JWXADSwqTMCfCOkFMaNlM74mYxZQVHhMZxJLBMpIqING9PxYfd3kPOqvvfeoHTYALrGm2eVAnSbbEIgJy-8300rBV4Ibtms2CgYarkzL6Bc3vNIDFCzkdjzfm8yDs-0Lg6jovtJfAL2jR3EQ1kh2UBDfhYkOdpjSIC-RLI1ELL7bdw7hQMEKeKmKkW4eoX7aEaos1G0ArHyIrACbjFoeCr_zENlaictNhjYG6KcaoWpgJTies4KTnMcbqNwHkA5CNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okRBkETKLerQdTUUbZrO6AIoYvHV3NCyl1XAfjxX-KdHDn396Gpyt6h6UiN2FkXyJB5MU4M9D_S1v00MLlpzwg7MeYQygEUk499X62kKRXizXfBu7vXRFIfJJCe0EEAI9wprAVOnBataEs-Vuog0epHXeL2MjuV_trMysgsHI8DXnrhSXrtusm8yw87Sdo3UGf4Mbclir4vmraXl4611AKC7JWza92gtuBbXtAwaKfwqOqe2OSnPMXVjTvfU9LL9N4t4MHz0PRA59uQ5eJpgFg1vlgCswZkND1NpOzFSV9FLTtLVgeulbOW3zkDeIvS2Zm6l0Bf0hKtDvpN9GcofQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160628032.mp4?token=wBU7XysDpDyhp0FsGZnJjlVYnOowpms0sKVc6LCLly5-2a3_DMPRPgO_l65DOb0go1-3fRf60nMYBsZGFNNE3-ysDO9kd0npFlqQgcqKdDZawqIQB_uMfrQf5CanwL9bZRSo1XOBzsN2kEffzRM9poiwjPugUCGzb4DHEVVkOEWCiuA8ODRXoQZq_xC-wKGJ5WokS9C-pS1VBuf1iMaGp_Y3bV0RV1y039KPQPT2M5Pd26xXrh-R71m0fVSrMsDOCXyXqMMZWUcCgrtSlUCS1o-L_nDkV438ClFDhLVynSizBDQn_FzZTuVF7YYI_YXOBAuEg4wKQrMOhHIHPEWTHXBUOQVAG3glGIskVLkbQ3qtOQ4SmeDevVoc1L1Ut5G4JHSlyINmNHKrIEhZGO84avMT5sQNhXKmo9CkvZMhw6VcrbBs68sI5-cOGUC_XnoGY45yL1drcORb4FTjXl3EzlvmV8h5iTIxYDKiHV1B2mt2k6D_g1wlrxqRYzd9ftF0t0cBeAaq5Tarn9_yDiKoUvYUzJC_i4ivrIGhq0xG--ZEBVlMPfpj1LZPYy4KDL_hPlWZgR0Mp1o43YTCnzF2HlyKRlIYF4PxIfNYkzPH-gGRKePt8BLTF2Lsal0ALS_Ipw2U9ZkygixPwHO0SR4QAUKpatXdFmVZAOCQ8DSjU34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160628032.mp4?token=wBU7XysDpDyhp0FsGZnJjlVYnOowpms0sKVc6LCLly5-2a3_DMPRPgO_l65DOb0go1-3fRf60nMYBsZGFNNE3-ysDO9kd0npFlqQgcqKdDZawqIQB_uMfrQf5CanwL9bZRSo1XOBzsN2kEffzRM9poiwjPugUCGzb4DHEVVkOEWCiuA8ODRXoQZq_xC-wKGJ5WokS9C-pS1VBuf1iMaGp_Y3bV0RV1y039KPQPT2M5Pd26xXrh-R71m0fVSrMsDOCXyXqMMZWUcCgrtSlUCS1o-L_nDkV438ClFDhLVynSizBDQn_FzZTuVF7YYI_YXOBAuEg4wKQrMOhHIHPEWTHXBUOQVAG3glGIskVLkbQ3qtOQ4SmeDevVoc1L1Ut5G4JHSlyINmNHKrIEhZGO84avMT5sQNhXKmo9CkvZMhw6VcrbBs68sI5-cOGUC_XnoGY45yL1drcORb4FTjXl3EzlvmV8h5iTIxYDKiHV1B2mt2k6D_g1wlrxqRYzd9ftF0t0cBeAaq5Tarn9_yDiKoUvYUzJC_i4ivrIGhq0xG--ZEBVlMPfpj1LZPYy4KDL_hPlWZgR0Mp1o43YTCnzF2HlyKRlIYF4PxIfNYkzPH-gGRKePt8BLTF2Lsal0ALS_Ipw2U9ZkygixPwHO0SR4QAUKpatXdFmVZAOCQ8DSjU34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVLxDTYwjkXl-ZwuiEIKjQh73XkmER9xHu3pAkyAU1lM15Eh8V8R2Q-QWa2kdBcKqd189e-2EZ1KXCfvWmJfPQK8zl_4pIniFI3PsQKkUPHas-YRnCVImoKZP2FgqFo7HX2dCfpEvdaYXY-U3XWcrsHsv7eF7F3BQxpfZw_VQWoaLoJNUTfN939GQ9OXjkyUDqc19UblwBrEiImllInAAmvw7jIrfTi9M-mKnKD9EdNjSsJLrYm32nLKAguLGVfquWy0YzN3UpNTB-93pSZM5Fc2vGn_pFMVd2SVGATG1NKSSOLAgN_7AptMMeUSYb23czEiZFxwQpHt1XjFfanvUuE5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVLxDTYwjkXl-ZwuiEIKjQh73XkmER9xHu3pAkyAU1lM15Eh8V8R2Q-QWa2kdBcKqd189e-2EZ1KXCfvWmJfPQK8zl_4pIniFI3PsQKkUPHas-YRnCVImoKZP2FgqFo7HX2dCfpEvdaYXY-U3XWcrsHsv7eF7F3BQxpfZw_VQWoaLoJNUTfN939GQ9OXjkyUDqc19UblwBrEiImllInAAmvw7jIrfTi9M-mKnKD9EdNjSsJLrYm32nLKAguLGVfquWy0YzN3UpNTB-93pSZM5Fc2vGn_pFMVd2SVGATG1NKSSOLAgN_7AptMMeUSYb23czEiZFxwQpHt1XjFfanvUuE5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTHdA22DhGgk9UbSezB5SAxnMj_h4jtSN8RWAFRzGMOIu9KswXor2VvaWtVZ16BGUuO_mkaYGB6SUjA1wEvc8hJC70q9XkqOig0YAppROEr8Gen1aspBK7LpscLzRmEoPBCm2-b6n2kW59buBTKsgMHIi00Rk7lBUp1v_El7l4c8VEbVpPfIYk0XbW3h9fVvpTJD24Da8lTuBvxISYh0_0a7F37yRsuxA_9AXL7qfIR_wXlBIWTYkynoDP_1BsEfa8X6RlGuYBsl5JHH5BRCUFXfkSu1i8MMkIZBfx1y06LMF88CZRmC-Q9zkXqd8ZXOKaUGTrOsyjc2hffrTLZk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=P2V853RqePKJu3WH7SPWrx26QTkgIRcq19vybDFzLSeJvHG7y154RhwhAqoQz_sVgcgjSrpM3GmSQOuXooqP_Bq1v6Yn28m-gQVlOz4KYH9sYzPdA9kuCTQa7--6y9bhMHHx9hBX0mQH-eXI8T9Z4SeE0K5iO3lJe4yF7wMONrAM7psJhM28D5efveKXTQsFdTFhfEoU0s-Z1BLVnPEk4W9NTJHZE2NLsqQHmUVsgpOlD92chRGxsOKQeS-hU93IsHP2RLDMC14sSeDcLdWWdrWwJzh56A8MHhDpZ5lcOx5iSJ9fFm9F_Y67ViTNWJciZF_DmjSxHdft1d0KyoX7kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=P2V853RqePKJu3WH7SPWrx26QTkgIRcq19vybDFzLSeJvHG7y154RhwhAqoQz_sVgcgjSrpM3GmSQOuXooqP_Bq1v6Yn28m-gQVlOz4KYH9sYzPdA9kuCTQa7--6y9bhMHHx9hBX0mQH-eXI8T9Z4SeE0K5iO3lJe4yF7wMONrAM7psJhM28D5efveKXTQsFdTFhfEoU0s-Z1BLVnPEk4W9NTJHZE2NLsqQHmUVsgpOlD92chRGxsOKQeS-hU93IsHP2RLDMC14sSeDcLdWWdrWwJzh56A8MHhDpZ5lcOx5iSJ9fFm9F_Y67ViTNWJciZF_DmjSxHdft1d0KyoX7kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XW2JdUmXhcKeGHxVuqAPf55Uu0o9UFhGtIFlGSRY87P_8wsC8VYTTuuWcb1gGOryFX-YRQPZ6_mNyjqKnICStRNfh4R5ygwV-xkfX9d9aryD7By9hYEjDuPibpavEpRjaFiiPptjM94dulM38U01anP6I-mJHE4jogDWKGG75P-0cT6--BcuSdwoueKAE1Wd6oGo_QmnTIojnKtxgABGzKjg6WbGghASd-mcj_WLiZZeNAKgGXubdbN9XXIinsblawqt9t99YBUZnnYWZJ8ZTbkdI6vLJ5i_Lbv6pAjlqEgKQX4mnU0zoOvQ_n2h_4qONan65IytEvQx4F-Qa0tVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=A-twINDB9ENvHPr-ZeD60jm-pYY3sz7MaTe9ECjBqVJhmlqqwBUy_20m99ZhypDqbaghixXOpz8yYnOQbLxxA3W86AoPT0Jwh7qNmXpj2gxzZH_QZqW9qLTGahtXYOxDLH93dc4aTRAoPTkSCiEgYTvnYEFaqFkOKZm757bjmCeeiEE6Ds-gotItUqNa9cYS_mO4ysp2dcRbdKjRE2hmkoKb5E-Mr3ehuCB16vRtopCRYh3cUzPExDmkCgECYgfMRSaQKfd4QXb91CqtUjF8fBzcgDgqfsbdb-UTN_QGpXsa_m7ikHI-POdKLh9mngc1LwKSirOFqCqnjn23z-WJZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=A-twINDB9ENvHPr-ZeD60jm-pYY3sz7MaTe9ECjBqVJhmlqqwBUy_20m99ZhypDqbaghixXOpz8yYnOQbLxxA3W86AoPT0Jwh7qNmXpj2gxzZH_QZqW9qLTGahtXYOxDLH93dc4aTRAoPTkSCiEgYTvnYEFaqFkOKZm757bjmCeeiEE6Ds-gotItUqNa9cYS_mO4ysp2dcRbdKjRE2hmkoKb5E-Mr3ehuCB16vRtopCRYh3cUzPExDmkCgECYgfMRSaQKfd4QXb91CqtUjF8fBzcgDgqfsbdb-UTN_QGpXsa_m7ikHI-POdKLh9mngc1LwKSirOFqCqnjn23z-WJZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ رسانه‌های برزیلی: علیرضا فغانی داور استرالیایی علی رغم داشتن کفایت لازم، به به دلیل داشتن ریشه ایرانی از قضاوت در فینال جام جهانی محروم شد. گفته میشه دونالد ترامپ در این موضوع به دلیل درگیری با ایران نقش داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EezPv5alcIIoBLZW0IarWtfmnOtwRyaRySupI5-C5GzNc1ChpuZAOMZqmiVdQCdztEgesYxp8ov9vvukhalOZhCavOEJQyhlENMF1nb3UvQ4IZbayOVKypjfGxY6L6iReDZfSJXF_XhKGlZ_vSU50kVaJ0DPSb51Du-4EMXiBJsUbzaqnJ0m-EDlZvSQn0zWrwNpD18FV1liJjdiGnDLnEF-FW_6k1hmydgC6LY14jOJ-lY3vLjxF-oqhpp3AiJyIU4SbPzoxPTAtpW5ja1DZWglKar2iCJI1ziR_9f5HGrL3AiNv9kjNvcOPzNDNt1BJV7bC07BE04MgLRh2fgZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eeo3HtMX-nCmj5A--Vkbq5VThrFTJvHrPKOGVgH2oQl040eRglvM0yi8Tj8XoFi8Li28JCaZCsZNu4thpLANcQ-cwYdl7le0qNdcTk1a71xBC-qUxhxzWWh2zpZCnEMvtXS_FRhPEsFN-JIKki3-R-CHG6yJvFd_2LrQLO9gJhmjHAolLVdp8O7HJBK9w-x7egOd7hVx4wrHHqh_kR3ui48XDF_u0bEa_jlUSEx5M1BGfdiRRUJL66iBw1nTWTEtU5MQVOHVmF-xuzahSo5te7nPXVI4guDBOo677YDqB-cgORH27kTYdkAvDXST5lG9ukftTdt0p6ISiguGR9zbaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=FuqtHrHppoAvHAHgqUPh4q2JphGHYOLwd-QFA7VWPye16gydi7Tbqo_VV2_TpirxonXv_VhLlO5soUXotr4TsJJ-8z1-whAN3BEoqi5ENU9Lbo3NclQ-S88xENjlAyPRVTxkdQNsDeGBtxGjJ1-K37s9kcxDdweabCAivIaQIg2dSUcSpdr-pJkHV_EV2CxSmpVhBrcorNEUturGJBp6bDtEZNj8wCQXwZ76NTNUFJFk8JjQ5EYMJwylY4YbAYL01SPECwLEYA-jVuzPUxC1Yr13WqJdy4wInrAuYjNz1dV76fwS4fVf-3XnA6Ytdlqv1m1f7yvkU5XrfsLkgWSgoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=FuqtHrHppoAvHAHgqUPh4q2JphGHYOLwd-QFA7VWPye16gydi7Tbqo_VV2_TpirxonXv_VhLlO5soUXotr4TsJJ-8z1-whAN3BEoqi5ENU9Lbo3NclQ-S88xENjlAyPRVTxkdQNsDeGBtxGjJ1-K37s9kcxDdweabCAivIaQIg2dSUcSpdr-pJkHV_EV2CxSmpVhBrcorNEUturGJBp6bDtEZNj8wCQXwZ76NTNUFJFk8JjQ5EYMJwylY4YbAYL01SPECwLEYA-jVuzPUxC1Yr13WqJdy4wInrAuYjNz1dV76fwS4fVf-3XnA6Ytdlqv1m1f7yvkU5XrfsLkgWSgoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=dsoIMUk8jWZK1AWiptVLPiGWrIEj8j3pNvfnxhfy6GhG9bWbt2Ecntq_gBv3Qp6s4Bky0OqnjH-GKy7QJ8CZQrnB8JZDZMMWsJG4tGopvnlMehGKACQPOXyYgSOtX00KfRCUxd9_evoAhcRpwAaNVUGeJZg7RXCzYZOLWYBhHv90sFKoVHyW94bOsDNLs3tJqX4n86Q7BmmCLFZdQIu7EF7Je1XyY8L3Zai6yD3vEYvScZFjKrWXTEXx4pWPVo_HdND20xNpwYeYbPEIZ4evGmuczOvpQEvrYwz2E5Fv2G1_U4G3KCHFhkWiAzCyDGO1NJGvUbCB8wMntPB6heoLWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=dsoIMUk8jWZK1AWiptVLPiGWrIEj8j3pNvfnxhfy6GhG9bWbt2Ecntq_gBv3Qp6s4Bky0OqnjH-GKy7QJ8CZQrnB8JZDZMMWsJG4tGopvnlMehGKACQPOXyYgSOtX00KfRCUxd9_evoAhcRpwAaNVUGeJZg7RXCzYZOLWYBhHv90sFKoVHyW94bOsDNLs3tJqX4n86Q7BmmCLFZdQIu7EF7Je1XyY8L3Zai6yD3vEYvScZFjKrWXTEXx4pWPVo_HdND20xNpwYeYbPEIZ4evGmuczOvpQEvrYwz2E5Fv2G1_U4G3KCHFhkWiAzCyDGO1NJGvUbCB8wMntPB6heoLWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

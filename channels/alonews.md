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
<img src="https://cdn4.telesco.pe/file/OkNnPhH7KymmABjXjlJA3J4cTf_AikVTNSbnH1m4bDqm2NWJha84kZoIGCy220omjQvpXfiZyP81aMPa7vRsfjA6FFCglZgFwNTD1lEsxrrdfRZCyuPTiHl-w1JugPXxQBdJyt8O3VvwfxlTJ8-HKCcUMbDy0hbCyaKUBngeRLl-kFrq9TYzamj5_moK0N_dYiNJUTp22EzDwIzDnGIZf7YqE1_bnhlOTx7Sc2_7PCewFqGL2yFB7DQRmWj_jmERyePfxGyLKRZfWLo-rXS6wRiQmIV-r3yquTpWK9H5jgKKOhNBUHl_2oHGdCq9wVqJf05BrhR4d1eHTquHnYMBcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 00:22:32</div>
<hr>

<div class="tg-post" id="msg-135500">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iyyPCEzBqD0h7q-gvtWXC0gstvXWBK1I_xId_NuWrdYMBzRqSQ8KxUTt8WcKcjlCuaBZtRm2esa4VhkNh4vu5aF8fS-amFk_9LUrOsFtL3tSlsflfIgNi7p54KWp4uqw16JC1QtySEpQe1L5kyho1DSy9oIIrPJfIB9x2g9YUuPy2wGv8uPRK5JISW2_soycyjXAweRReazh8g2Z0eG3brlUJs-vfD4yOEKWvB17FRmfIUgV-2pZh3lLABiMfbJUVi4shklqouxCB6CYBgh842hA2Eh99r1j0aTmEz2Px_lVNc6a57HRWYloaolzsYnCxo80ljYWFNVYoW8YA42wQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TOfjiRLQIkbPr6z3YiNGyjRdCutiLlXEwQEErymLKufJKli4LnuGFiizD5EAu-qvEkvv7xF8nBtVyqSi43smXIWLOKlRdMBDwnXLyJouU1VBs4gY254-Rsxgl2b0jaLMjFJilZ0S5fORGmeEl1dRC-geZLkfHY-cvPgOv7Ho3c1NO3o4tBRTr3QNo1yGgw06uWN848pph-uFIjpx6I-xkGbX6yPlBJQTuQZ7ng_qClsHgBqjD-YQT83xuHy0oMjT8Jx9s65DhcbqDFFo5YGfCfffdtjBaZobzJiyN33OqTaK50rtT00qx4M8I5RZZprvbd5VtXwTI8zN3_rJnH85Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/seplKVYobZJWnMdQCmDSoArahx1BSqGD9jeUq0s-tGnu0kum141vx5PG-bJkP92KB5CfmNok0TOr2asVikW_hzkPCrHxQSIg-VlIn7tZwQBatUYQZtONuVbAKPiNExeKxmXwlt7iKevXuDBMW2dPOeidlKO-yUObWenLrty1IynjBlf7fmQjixOYlekNd4QisxkEH1ArQcda9sSeD_1hrCdVSfLbGAs4ALgmW8od3uNeVh5Kkb8GHpXlAfLAQkEY4zvjeIRaZkzJuDJHeSXy3fb1Tm4RIxcv3Ogha_5BCcTDvnIJ8ZIha-O6fXL8A2SPf3R5uzonbOLrubho3H-dmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E6eSCAA-NWGPDDMbZnWp8iFjG8H4wsm-XGOoF27zoCaFaGTAz4YvlgNaRhUhSMwDG5mNuaLo5Sfe5oedisWzWnjkMQIwVj1SBYygnd5UO7Hm2MGjX-x1VLISxSO9Dfa_C-Dv1Lkt_tsu2WOKMj8NUgoBYAKUy3pdGw6gWyN7d7DDPqNTibKtJQmnHCg3AnIbC2MInCCC6A7pYIkP3pNMMsOLJYqJkHEIiRPubLSW_X_yaj15cyMSmNw4iSBSBaNZ0ziUIr3e8teCqVyIrNn_4t_8zkgOIeZ7tBgbOKyYKClXQ2zyzPAzlq495RCKCxZ7ErVaxh2emC5yWVO_qMigpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور یک اردبیلی به عنوان مدل در برند dior
ملت هم ریختن کامنت گذاشتن و آبروریزی
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/135500" target="_blank">📅 00:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135499">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقامات آمریکایی: حمله ایران به اردن به تعدادی بالگرد آسیب رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/135499" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135498">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سی‌ان‌ان: دولت ترامپ توافق همکاری هسته‌ای با عربستان را تدوین کرد که امکان غنی‌سازی اورانیوم را می‌دهد
🔴
این توافق به عربستان اجازه می‌دهد برای برنامه هسته‌ای غیرنظامی خود اورانیوم غنی‌سازی کند. متن کامل شده اما هنوز توسط ترامپ امضا نشده و به کنگره ارسال نگردیده است.
🔴
موضوع بحث‌برانگیز این است که این توافق، عربستان را ملزم به پذیرش قوی‌ترین رژیم بازرسی آژانس بین‌المللی انرژی اتمی (پروتکل الحاقی) نمی‌کند و در عوض بر یک توافق پادمانی جداگانه بین آمریکا و عربستان تکیه دارد. منتقدان هشدار می‌دهند این مسئله می‌تواند مسیر دستیابی عربستان به توانایی ساخت سلاح هسته‌ای در آینده را آسان‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/135498" target="_blank">📅 00:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135497">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
فرمانداری خارک: زندگی عادی در خارک در جریان است و هیچ دستوری هم برای تخلیه صادر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/135497" target="_blank">📅 23:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPYsWvcCbYs-WAQn4S8MhPRdnXKGD4jH67YG__Tja6AwVCAIC1Ps8Yq8wyw7RNIIPVw5MOP88xlgF4v15y-eN0W1jRIiFKF7VsnklYn3h8rKldrc6ZQ3lSZAcNOSpbWt7ad_RHxEPimdskK0At1OOoIxrp-9pUD4mmyl-UnYAalrZ4y4uYsTHMU0NKu3-s1BYXBaKpXgiiDXXhgZPEyDQjH4CdmPG30GNIZCEKZ3YAJIe1HY1rs00ZIsfVcVzC1Mh_2NAhr4EP3xeRL7sPstJQSWbWSMZs9Q-SBUYKm-0BvWSYz6pVeYFMgdAU4WlY7q5N8_onxFvBt-lrYG2JKpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام : به اجرای سختگیرانه محاصره دریایی علیه جمهوری اسلامی ایران ادامه میدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/135496" target="_blank">📅 23:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135495">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
یک مقام ارشد شرکت انرژی آمریکایی به نام HKN به شبکه خبری روداو اعلام کرد که این شرکت به دلیل تنش‌های بین ایالات متحده و ایران، تمام فعالیت‌های خود را در عراق و منطقه کردستان متوقف خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/135495" target="_blank">📅 23:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b2f6992f6.mp4?token=VvzruHsgpEfj191jHOSW0_wpUoUIJK-wVtp0tR7w09rxKRuOHTctCip0awlXmDfWSKdcbaBj3BrkvDL3sVkdiTdL_hnCsu_YohQ5jdwVmI9oay2yppZ7z5cct8th0R7mE_OVFrDULsrM8YGTekASUdCUAhaVjfZjqPvKcV6uCdmtUWb3NY4_tKljOB3zYxnH-uMh-r1o-QZnyd6dmQoQimn8AyUlUgrjHG4MRwv9mO_BijQbWSnTOAGUVh9YFNuflEAxLUaWbr280g2gZi7EEPR_jwlqwtCMRfe7XwYPPKc2RDneCj7BvcmdLSTpcMJuwHHIHxTiCHgqNg5lp4cZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b2f6992f6.mp4?token=VvzruHsgpEfj191jHOSW0_wpUoUIJK-wVtp0tR7w09rxKRuOHTctCip0awlXmDfWSKdcbaBj3BrkvDL3sVkdiTdL_hnCsu_YohQ5jdwVmI9oay2yppZ7z5cct8th0R7mE_OVFrDULsrM8YGTekASUdCUAhaVjfZjqPvKcV6uCdmtUWb3NY4_tKljOB3zYxnH-uMh-r1o-QZnyd6dmQoQimn8AyUlUgrjHG4MRwv9mO_BijQbWSnTOAGUVh9YFNuflEAxLUaWbr280g2gZi7EEPR_jwlqwtCMRfe7XwYPPKc2RDneCj7BvcmdLSTpcMJuwHHIHxTiCHgqNg5lp4cZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز درباره کشته شدن سربازان:کاخ سفید اعلام کرده است که سکوت خواهد کرد، به این معنی که انتظار نداریم ترامپ امروز در هیچ رویداد عمومی حضور داشته باشد یا اظهار نظری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/135494" target="_blank">📅 23:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
امارات: از طرف‌های درگیری می‌خواهیم به میز مذاکرات بازگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/135493" target="_blank">📅 23:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بیانیه مشترک کشورهای خلیج فارس و اروپا: ما از ایران می‌خواهیم که فوراً حملات و دخالت‌های خود در ناوبری را متوقف کند و تنگه هرمز را بدون هیچ قید و شرطی باز نگه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/135492" target="_blank">📅 23:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135490">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1beb607113.mp4?token=LkmwsHQuXXwfx7hgAQEzikiGbYTQVOEMeF6leuUlU8oHb5ZpvHYgMc6UUQCkUW6gs13U77vgl4E0-N-dpzSbsmErchCGTWNqRNy8ZFgKsvGr7b_LvIDS8FibYqFORQR4AZ2qk3sTRhiL_hoqYaA5v-vvtiLkt20IfrREfGmoQchnl2azujGXubFIPv2D5WtWvxu1oeWlQzSur3S06sYrQjj16EIdXUs_jZUOyREcGlFa7ocsegAoUBoKH9qp8mNjgRVPxt_7l8o6Sb-vG7mTkdo-K46vwHILlNH-Z51oCTLaHdyYikfIl5MF86-rwEJ_Yv5r_49r4-BehsCFE8I_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1beb607113.mp4?token=LkmwsHQuXXwfx7hgAQEzikiGbYTQVOEMeF6leuUlU8oHb5ZpvHYgMc6UUQCkUW6gs13U77vgl4E0-N-dpzSbsmErchCGTWNqRNy8ZFgKsvGr7b_LvIDS8FibYqFORQR4AZ2qk3sTRhiL_hoqYaA5v-vvtiLkt20IfrREfGmoQchnl2azujGXubFIPv2D5WtWvxu1oeWlQzSur3S06sYrQjj16EIdXUs_jZUOyREcGlFa7ocsegAoUBoKH9qp8mNjgRVPxt_7l8o6Sb-vG7mTkdo-K46vwHILlNH-Z51oCTLaHdyYikfIl5MF86-rwEJ_Yv5r_49r4-BehsCFE8I_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آنیتا "خواننده اینستایی" رو گرفتن که بخاطر ویدیوهاش ۷۴ تا شلاق بزنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/135490" target="_blank">📅 23:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135489">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/135489" target="_blank">📅 23:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135488">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4uvkWSyDF2SNdvCcYSgJJtaHYCu9ZNn9gKHznF3Ig4sMANf1cyHYDEWiYrQKD3_uv4e3xSlGnvNE4yHyvcM2Rr88QfRUReHbrUnS86niUo13WAK5mHArcP2rRA1-UBZ0_WwPYdbVAKwv6Tyq7OaIw4i1esysnLHk3VKEq5KfFE_Fpny7j5N-NktP5isrr5yg2IaCFxlhhsGE2v9yO_CjyevYUlDQVivZCC9_uUxWlFmoGcuJKjmK2wf5SJQWU5vcP-Emg7MHMGplGilvoBATL39q1OvFXRXdSGMvQjJLLz_ndoZinvQrDQxvU7sdBUTpt6xBwskyynqtNVc61L1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار وزارت خارجه آمریکا : به همه شهروندان آمریکایی
🔴
مخصوصاً تو خاورمیانه، هشدار میدیم با احتیاط بیشتری رفت‌وآمد کنن؛
🔴
چون احتمال حمله به منافع و شهروندان آمریکا وجود داره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/135488" target="_blank">📅 23:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135487">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
عراقچی: روابط ایران و عراق نباید تحت تأثیر برخی اظهارات شخصی و غیر رسمی قرار گیرد.
🔴
ایران بر احترام متقابل، حسن همجواری و توسعه هرچه بیشتر مناسبات با دولت و ملت عراق تأکید دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/135487" target="_blank">📅 23:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135486">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
چت و ویسی که از بیرانوند منتشر شده تو دایرکت یه دختره حسابی داره........  ببینید این جانور چی هست که به اسطوره ایران توهین‌کرده
◀️
◀️
◀️
جهت مشاهده کلیک کنید  موقت هست و پاک میشه
🚫</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/135486" target="_blank">📅 23:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135485">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwu7BP_J_mEstobV8kph1y_zgJLASQ-_uPLZNco2QWwvUJjPTus6KjoCnqxJtOtRcYggRSl588MBWNxawvSwVL_617-bzTzSJhzZ8wTbam9-nYfTbC4SQPwWhVe22sip-gUOnTUj_zFWEFN92fyUbe-QsBMzIacR-VyyD_Km6-qI6ZnXuvrj80d78zUCZk7KznVEi8h4IHRyEZAWisOKhDTjEKYdxm1859FZaIe0xhyjGiH9u-ncG6knbbHM0JGJXq6wBQbfjPZPBHnmoZrQSTN3KwLOhnhIsYfC-aKEVCQho8MlLjvWlaLQ2Tx0MMyJSbzGh0GBpRZ6-UuYyvN_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین بیش از 300 پهپاد به سمت روسیه شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/135485" target="_blank">📅 23:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135484">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه NPR گفت:
«رئیس‌جمهور ترامپ دستور داده است که فرماندهی مرکزی نیروهای آمریکایی (سنتکام) در ساعات آینده، «دروازه‌های جهنم» را به روی ایران باز کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/135484" target="_blank">📅 23:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135483">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a6119426f.mp4?token=TzIybiTI5hdJ_s49a0PXqJ5mfCRAnSGyroJIR1lMzTZ7s9ziyJrm70ZaD56rv7Pw5Fy6H9bxtjsfFOF-4BPJsmP8vGpXI06h8M_V_KhVDaq8WXz8Hz7Qugm68tX-QkeumWZADXOo94IzCBLUUVegDJb-1OY5kHtX3QntnsvBrwOzEHV43qU4kvcnk8hSo61eyDYh8msTCPTvKQlHxeHDHdukv6P8-3SkXpt6_AmPymnP1V4kaD8nCHH8NQY1Usl1y_4NojeGN-Ebl-D97L1SG9nrjWVnVpK7guwwmu1OZrxIGbC-iacmc5oz0B5wCHRpqYpZARfwNM8NnMrdF_xVlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a6119426f.mp4?token=TzIybiTI5hdJ_s49a0PXqJ5mfCRAnSGyroJIR1lMzTZ7s9ziyJrm70ZaD56rv7Pw5Fy6H9bxtjsfFOF-4BPJsmP8vGpXI06h8M_V_KhVDaq8WXz8Hz7Qugm68tX-QkeumWZADXOo94IzCBLUUVegDJb-1OY5kHtX3QntnsvBrwOzEHV43qU4kvcnk8hSo61eyDYh8msTCPTvKQlHxeHDHdukv6P8-3SkXpt6_AmPymnP1V4kaD8nCHH8NQY1Usl1y_4NojeGN-Ebl-D97L1SG9nrjWVnVpK7guwwmu1OZrxIGbC-iacmc5oz0B5wCHRpqYpZARfwNM8NnMrdF_xVlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متکی: طبق قوانین بین‌المللی هر کشوری که در جنگ علیه ما، امکانات در اختیار آمریکا قرار می‌دهد برای ما می‌تواند هدف مشروع باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/135483" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135482">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وال استریت ژورنال: مقامات آمریکایی می‌گویند توانایی ایران در هدف قرار دادن اهداف حساس، نگرانی‌هایی را در مورد دریافت کمک از چین یا روسیه برای هدف‌گیری این کشور ایجاد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/135482" target="_blank">📅 23:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135481">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رهبر انصارالله یمن: اگر عربستان سعودی در حمله به کشور ما دست داشته باشد، تمام تأسیسات نفتی و حیاتی‌اش هدف موشک‌ها و پهپادهای ما خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/135481" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135480">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogdWWqRV6vkzuya71igIXHPfasUZNo34cCW2GZPCM0Gvy7LB6lkgeYAt5Pul3RFEN-U9zvc95FOodnPA7RnTuLyGhYx8PBxAlsugzBnU0IOVcIaVkygz-l8hwmIQEKFVpkVDvks5xO8J4N4hxVMqFqftCrrAGLyoDHSW-8FDv9Kq2dO8OdCsFsOgoTWySdllwqEpqGFy_QLNyl1iZd5OAAtfOXaVmd1sbbBFqGnVMNGh2qSYtyjeRug2k5KUrbkV_YyhnB6TfAXS9z0cP3dJpOmYgtcmvr9pOpLTFkDxnjkBq-cXaEMsPYDnfC5ewILVdqNaEy4wFirbm66V5BYVKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر ارتباطات: خبر قطع اینترنت پس از جام جهانی با دستور قضایی هیچ سندیتی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/135480" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYXGt2DSWl1U3hLmisfpY3k2yklux0jyahKJ9juNdSztSIt2IhWHb30kOVRMl7zc-2BkPN8OxD5sIKjKLfTyhYEgk1BfyiE7f9vj-qv8lmxAWRrPbtpJyeg66C4z0L85FoR07yY6fLfI9l_0gBniuiHKt89dNnZgjyF5OGWH57e_DbCnipZoWaMFqzayV6U24KhBDoAp8tZhlmUlNDfFkZ6dpAQahgAskSg6j1Fqikin2erVhFOzojqFmEM7Xglb6flccOH57B5SuaeW9-nodpMetpy8uqARinCQR7dfxSl-fG0y7AuQa3i7M3NGm2bwx1IqmU-tjLGFBtJFrJD2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت:
از مراکز نظامی هدف قرار گرفته فیلمبرداری کنید سریع میرید تو گونی و تا چندسال زندانی میشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/135479" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135478">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e0d5215ce.mp4?token=cNAzuQqW-qFpn5nHvRqJWH-y2rvH8fxzenOx-4WbMYczYNoZ6ggtdwxovHE_7uNdp_tRGPPtAsN2ZAqyjSa3TRclSquHCd3MyNuKIc38QNXX_9dvoO7uftScVpAvV-CngLtRZ0R0FJfPraS1TWbTU5kwyITBiuue7io71n5BLRG3rTlUphwwZunJJdIChF-OBonr54qCfYZlL5c3F53FGQyFMbsgx_08K6jDC3VTvXo7lXVCs3sOgfAnM6AM09foE81kC-G_YEEhg1nCLN9eGyxO8t64Bz9H0emcYzunOkmWyMe5kd0wn325DwSXtdnTTHI-dOS0w4D2oVXoJGPmKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e0d5215ce.mp4?token=cNAzuQqW-qFpn5nHvRqJWH-y2rvH8fxzenOx-4WbMYczYNoZ6ggtdwxovHE_7uNdp_tRGPPtAsN2ZAqyjSa3TRclSquHCd3MyNuKIc38QNXX_9dvoO7uftScVpAvV-CngLtRZ0R0FJfPraS1TWbTU5kwyITBiuue7io71n5BLRG3rTlUphwwZunJJdIChF-OBonr54qCfYZlL5c3F53FGQyFMbsgx_08K6jDC3VTvXo7lXVCs3sOgfAnM6AM09foE81kC-G_YEEhg1nCLN9eGyxO8t64Bz9H0emcYzunOkmWyMe5kd0wn325DwSXtdnTTHI-dOS0w4D2oVXoJGPmKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">-جناب شما جان فدا ثبت نام کردید؟
+بله چطور؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/135478" target="_blank">📅 23:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135477">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
ساده بگم، جمهوری اسلامی تابستون رو مجدد نمیبینه.
🔴
بزودی منتظر تغییرات خیلی بزرگ تو ساختار سیاسی ایران باشید.</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135477" target="_blank">📅 23:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135476">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/135476" target="_blank">📅 23:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135475">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💢
خبر فووووری/4000تفنگدار دیگه عازم خاورمیانه شدن
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/135475" target="_blank">📅 23:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135474">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1574a01f69.mp4?token=JcHIQGM7n_b8oAQ2kymc_AhaILHsynXWPyNk0RjgJFcEMQnU_qJ0MDw4ynjulooP3cnKviSVSyo6tJCddOg6kx2BSL_-xoCXdtglc1oLTZfq1eeR4FnYq5UdxKcN_wIgFsBjSFQLXaVfZsSjT5M1yNPBcB8HuJ5pDZeD3LS3e9QNUO6btsMPBbYI7YQm7BSH71LMRd7EhONrgosBtkEdAP6zpoQEmnOrYAgsr3KLokACrNGZXls-l2_InxHemIWMokIXUZ8lbLBFzboFFTMWEXpNZ1et8eBXcwA4JUR6lsXU_gKwul8HLl2xDMuINraEbrigbtPF7BfdymNktHg5IIuBwBmswqGXtkkD_uH1L2MRTJQYmymvDqHu-5MtaaiB3MN4pKslbFfqUGsstlhygkuyrfJvlcKp99pHJ5zwx0O_bCOoH3WK-dcO7QifEvYpv55wiOvwE7fK3Q_bMh_vTpfZTXFD3Zz4xZOim4y2yoHAdvLos2twjCbcFgQrG6URca_mriKI-AjTAe5hXVzG6oUaQR5XRFcthRoLGt-vHl1CtzvV1EYZuIPKMOVAZWKF-Acw7aSza4V6hV19gBnvuB8HPL_dJyPrZVDLgNFYOmMWfPqflR8_Zv73FPcuADsMxLUNVcJiLkg9Pyv8eG9Yf78YwfoSgBp2-RUcyOTg_vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1574a01f69.mp4?token=JcHIQGM7n_b8oAQ2kymc_AhaILHsynXWPyNk0RjgJFcEMQnU_qJ0MDw4ynjulooP3cnKviSVSyo6tJCddOg6kx2BSL_-xoCXdtglc1oLTZfq1eeR4FnYq5UdxKcN_wIgFsBjSFQLXaVfZsSjT5M1yNPBcB8HuJ5pDZeD3LS3e9QNUO6btsMPBbYI7YQm7BSH71LMRd7EhONrgosBtkEdAP6zpoQEmnOrYAgsr3KLokACrNGZXls-l2_InxHemIWMokIXUZ8lbLBFzboFFTMWEXpNZ1et8eBXcwA4JUR6lsXU_gKwul8HLl2xDMuINraEbrigbtPF7BfdymNktHg5IIuBwBmswqGXtkkD_uH1L2MRTJQYmymvDqHu-5MtaaiB3MN4pKslbFfqUGsstlhygkuyrfJvlcKp99pHJ5zwx0O_bCOoH3WK-dcO7QifEvYpv55wiOvwE7fK3Q_bMh_vTpfZTXFD3Zz4xZOim4y2yoHAdvLos2twjCbcFgQrG6URca_mriKI-AjTAe5hXVzG6oUaQR5XRFcthRoLGt-vHl1CtzvV1EYZuIPKMOVAZWKF-Acw7aSza4V6hV19gBnvuB8HPL_dJyPrZVDLgNFYOmMWfPqflR8_Zv73FPcuADsMxLUNVcJiLkg9Pyv8eG9Yf78YwfoSgBp2-RUcyOTg_vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوووووری/ویدیوی منتشر شده در اینستاگرام ترامپ که حاکی از حمله زمینی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/135474" target="_blank">📅 22:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135473">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری/گزارشات از تحرکات شدید نیروهای آمریکایی در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/135473" target="_blank">📅 22:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135472">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23a9e6418b.mp4?token=V46lHr3nF1qD-FDZLt1gbCfX1T18BR-iWxks6HWVMaBXRmXYAnNmP9iZdUsYsTHfQ-pFMPmKgzeQiE2Pjl7wi9AkfN5covg-XJ6e2xumq2Iya103kLfXWuu5hlhPiBIjjO0RZxdoQVWX_lD1gkmbYKNlXp7KiDSV6ApkvikdBiubSzdNSnc6BV3hW8rRFhet6u4wX2t5B8sD6QkRknccl36SDE0kdMfAHM2KMXZGVgnGasxEM3bg5c8ln3dLT3x70DkGxHoIbYr3WBbifTqdHp2gZPus5vQ1DCU_BOdQ1y48QaAYzrkRZMlL0nCG2Pt3-fcWl3mFEhiSsj5EhYpLHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23a9e6418b.mp4?token=V46lHr3nF1qD-FDZLt1gbCfX1T18BR-iWxks6HWVMaBXRmXYAnNmP9iZdUsYsTHfQ-pFMPmKgzeQiE2Pjl7wi9AkfN5covg-XJ6e2xumq2Iya103kLfXWuu5hlhPiBIjjO0RZxdoQVWX_lD1gkmbYKNlXp7KiDSV6ApkvikdBiubSzdNSnc6BV3hW8rRFhet6u4wX2t5B8sD6QkRknccl36SDE0kdMfAHM2KMXZGVgnGasxEM3bg5c8ln3dLT3x70DkGxHoIbYr3WBbifTqdHp2gZPus5vQ1DCU_BOdQ1y48QaAYzrkRZMlL0nCG2Pt3-fcWl3mFEhiSsj5EhYpLHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: مقامات جمهوری اسلامی، هیچ جوره از مقامی که دارن کنار نمیکشن، یا باید اسرائیل اونارو کنار بزنه یا عزرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/135472" target="_blank">📅 22:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135471">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/135471" target="_blank">📅 22:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135470">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
به بهانه توهین بیرانوند به علی دایی بریم یه افشاگری ازش رو بزاریم</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/135470" target="_blank">📅 22:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135469">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
به بهانه توهین بیرانوند به علی دایی بریم یه افشاگری ازش رو بزاریم</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/135469" target="_blank">📅 22:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6DVefhegSKKcmzjDGY_5stqXewnv2oInwA1SKCwNkFFs16Hk-Tu5Kwj9-NQ-9F0aEyzfcjKY7tvucxmoqN3sUpGsIWB6FkrQHK4deltMfR3TieIAeTVLdaUJYE7KZ-5L7-vOfmPkxhKqFDIxoYDgwAxaGSkhJnyPPRLuPSGG5eRsbNEKhwbNS-_1aBJU_zuaz2XAG8LKYpWJOJ03CfX0z-Hh2d0cIYu0z0WWa3VQfTKQrkZ6gksi5DaLb4_FQ0TYhgXzEqjqmH1XdzYBSanhxg6goUpnkpgyE8BXDzdC6Wb7ZtJ4HTGYlz_1LlCGmRGuwyOo2DfUEP1xj-FsO4wJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مردم تا آخرین قطره خون جلوی دشمن مقاومت میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/135468" target="_blank">📅 22:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/135467" target="_blank">📅 22:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/135466" target="_blank">📅 22:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/135465" target="_blank">📅 22:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فرماندار بوشهر: همه چی عادیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/135464" target="_blank">📅 22:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
گزارش صدای بلند در روستای لنگر شهر بجنورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/135463" target="_blank">📅 22:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmdV0K1cTjg4Tp3ThMH4SZmCM25-sdFKHPpRAKMmaMd-yI2p9hO70Nvre7kToiCxtlAWWcdh3QT9blRqCPwGVTl_wxxJ6Dmi8DLTqdcMepwB3f8IiBpyYwcbUGkL5T2ZSSXTa129P7-AiX5aGwDAU_jFE0h81ptJbaCv9KYnt2cmn3B92nAKVk2TgkM44op9elJE8ZWFWBRXCM0QV_dgkRR9ewpJ09fZn3rqMseK2NcmhP1hc-I-E53FlZ8FJv6n_WG3CrYJFPDX8cARKCE09CWOQkoU6aZ2rw6Deq7jIyrhnj8KISoIhDtfFf2Xe8hrf6cHn8hgx02zaWSRJzXaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سطح اختلال شدید
GPS
تو کشور‌های خلیج فارس :
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/135462" target="_blank">📅 22:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
گزارش‌ها از اختلال شدید اینترنت
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135461" target="_blank">📅 22:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et2GiiwfCsf27fUOAsdJffWYp9PVpMFK9voMeC9YDJAwdANn-YSFTP7X4R8OdUIxrht6PzlsZqJvHCFxIRfubF5bjv_deqT7Igsel_e6REAUqfK0dFCjAP_RzJq8E5c0BjSoCDygOTpXWrV88AI9SsUVdnYPsvNmN0DxKdaLgwNjbQYdXUoM63fkq2zyOWRNvmEWbAI-nQdMsGd5ADoAto0V9GCyqOd3LMyoGx_RP1j8F9D9M7p0FLYmTqtomVNKCvY2mvmohvM9_ACAyErmTlrFTzs7e2P6xb-SvV-KwaZDWh8pG4Tao6Xgb8Y1AQMAp_ATDj_52nTD0DtEQaMpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست : فداکاری‌های شما، تنها باعث افزایش اراده ما میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135460" target="_blank">📅 22:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0048d525.mp4?token=o6tQGH2KH3WI1dl6QJNn3_kcAhTKCZLdWu8pWe2IvJn9fpV1U-b7DyEokLwsX8OKR2BdnOLyKywEaFF0feHZioQbz-SB8ZB6bwovf9V4JykaV4KlCU1ieiSP4kjnJEi8Q5ZUIUzB1dpfcmk3Ri7eZ5YQSeHUm7onJlnbmB8KUBvrxH7CTO32huXUdguSuC56yhNaKIb1nMPmh9CYwWQs2go1_ZEKfusIaMU1Ngv3DSP7U6lxMThXE1hk7zVeWhJ2PinsBbw76Y3B9Eoy6MfwOrfDGOiRUHShz1hw2KdEfoK0fvez2MCWdf5SadOq8uyQu3YsCSPd7t5uWdJ0IgmrJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0048d525.mp4?token=o6tQGH2KH3WI1dl6QJNn3_kcAhTKCZLdWu8pWe2IvJn9fpV1U-b7DyEokLwsX8OKR2BdnOLyKywEaFF0feHZioQbz-SB8ZB6bwovf9V4JykaV4KlCU1ieiSP4kjnJEi8Q5ZUIUzB1dpfcmk3Ri7eZ5YQSeHUm7onJlnbmB8KUBvrxH7CTO32huXUdguSuC56yhNaKIb1nMPmh9CYwWQs2go1_ZEKfusIaMU1Ngv3DSP7U6lxMThXE1hk7zVeWhJ2PinsBbw76Y3B9Eoy6MfwOrfDGOiRUHShz1hw2KdEfoK0fvez2MCWdf5SadOq8uyQu3YsCSPd7t5uWdJ0IgmrJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما:
اگه اینا بیان جزایر ما رو هم بگیرن بازم دنیا به اخر نمیرسه که.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/135459" target="_blank">📅 22:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">وقتی به اعتراض میگی اغتشاش،
به جاوید نامان دی ماه میگی تروریست،
مردم هم به حمله ترامپ میگن کمک بشردوستانه
🤔
چیزی که عوض داره، گله نداره...
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/135458" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135457">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
استانداری هرمزگان: دقایقی پیش خبری مبنی بر حمله جنگنده‌های آمریکایی به مناطقی در حاشیه شهر سیریک و جاسک منتشر شد که این خبر صحت ندارد و تا این لحظه هیچ گونه انفجار و حمله جنگنده های آمریکایی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135457" target="_blank">📅 22:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135456">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wx0upt5R8nlXOJ7RXHwgzhiBeDZI0hcSaoYZOSYhxFpUhtUrFIj4td5ZvbqN983ic5P1YLUv1zHcECK1iRnBHagPSOYjoEa0i8FNFq1zmpRz6uo_BcB6Xg9ls20lS_uYgAYUZxGfjnGCLPwg_28iZKtZDqD2ZrtQVl9HLhQJ4HTZkZNalwuRUXT7RVaBHJdHCDBUDIW3-iIbr5mcZuUaT36f220sJrvxVLZCP6U-zhIRsVduoW9U_2SZ99Dke-pSodYJIY6FFRPmVG4GwojnGfPcizT8Ur7mCoAxSlqA4OO3BR58W0pR0AFOrv5finzDIKQhXAZ2VtXp7k5ibbKJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود از شهر جاسک در ایران به هوا برخاسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/135456" target="_blank">📅 22:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135455">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046a9a37f6.mp4?token=a_QKHIu15NbY0A09yK-e5swgxShpa4B4Ah2TxPT-jlgXj6fV_6a5BP4a_sLox-Ikk-s0ZzZpFKuKTQcYjR7qhIMVzGl0lJ_Ex9G4369XRmbJqY-alqDMTZjzMTR4TQWrknKwxCVutoFvXoZVrTGmx3SuAY0_DhPjk3lXAuUDfmU-dBu9ypYNrYPh9IqSx8jzdvWy3D1wLksqUFfz9mPwXwBhIAGr4uysydN7LtlZgBqdrKh-_G7rn1lk64hqyTpRK2dXqaivoapcMzdWvG-qmvdoztdAN83vCV3sWEZNzjCYKEMm5KZvoiwQOq5OuzXkvrQyBgw4T5GpWSJpZEwD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046a9a37f6.mp4?token=a_QKHIu15NbY0A09yK-e5swgxShpa4B4Ah2TxPT-jlgXj6fV_6a5BP4a_sLox-Ikk-s0ZzZpFKuKTQcYjR7qhIMVzGl0lJ_Ex9G4369XRmbJqY-alqDMTZjzMTR4TQWrknKwxCVutoFvXoZVrTGmx3SuAY0_DhPjk3lXAuUDfmU-dBu9ypYNrYPh9IqSx8jzdvWy3D1wLksqUFfz9mPwXwBhIAGr4uysydN7LtlZgBqdrKh-_G7rn1lk64hqyTpRK2dXqaivoapcMzdWvG-qmvdoztdAN83vCV3sWEZNzjCYKEMm5KZvoiwQOq5OuzXkvrQyBgw4T5GpWSJpZEwD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از شلیک موشک های بالستیک-تاکتیکی اتکامز از سامانه هایمارس به سمت اهدافی در داخل ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135455" target="_blank">📅 21:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
گزارش تأییدنشده از درخواست تخلیه برخی کارکنان و خانواده‌های آنان از جزیره خارگ یک رسانه به نقل از یکی از مخاطبان خود مدعی شده برخی کارکنان جزیره برای خروج تا روز شنبه تماس دریافت کرده‌اند. تاکنون هیچ مقام رسمی، دستور تخلیه عمومی ساکنان بومی جزیره را تأیید…</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135454" target="_blank">📅 21:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135453">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sih38NvYYzcl2QoXn4FQwK-N1lgV12keqh2RwTgJayadDX_u_07whNk9tu1EruPyb29FjIqKm3MFzml5WD1W1r8ldl97DZVaydc1aMF0SKji7qi24ilezYj94JsI54p8O7f30Y9l84VjYPgGZhD5k_uzvCX_9ZUoZQ6-u7FEibIC7jaT7RDskpcXr_zVXmnUA5YZ004_AsDP6d01KIU17FZYamQdq6r-S0-qr-MSBPXsqYF20O4wyMO2R1Wzel_i__Ln6OQ-vSRatgCVie-Pp0gW9zcHZTuUMnnBSSJJGBCq7rKinlLsnpWUbhayEaWsoNnf76HUGUmT9V_imV6vPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۹ هواپیمای سوخت‌رسان آمریکایی اکنون بر فراز خاورمیانه در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135453" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135452">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری/خبرگزاری i24news: نهادهای دفاعی اسرائیل در حال آماده‌سازی برای وقوع یک جنگ بسیار جدی در کل منطقه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135452" target="_blank">📅 21:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135451">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / رویترز: ترامپ دستور شلیک قدرتمند در ساعات آینده را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/135451" target="_blank">📅 21:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135449">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PDSPnfkxpE6jQavJA139mxfCItzgxCJ6GKK-qmby289D6grrlrncaWw9HsSCGYV9df2p1AU-JEBrYZwaTMVSK3nyE0aM7J_LikIhXknSdtv2c6tQYuXS6jO3bjg2dQeKZ5nfiBNovo-KF132XSmImR0E0b925N0rVKhFgbEybVdt2i3dPVaItcd8quWGRIuaD521qtVykC5dbAITJpI7KhMbeScSLaSyunPghgTqXcIufappMiWoVk1aJRH_U-wRDoSXUBzuIqdcEng3KhVqguJ5l5mVEs-f3Z0HcM08vT-gcfJ0w5Szp4w1JIWmFoXsDlMhzrAIMOFzg8aDb-eeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DbZBcjFYM8JJrNCwG2GdIhYhQvWxMZkF316N5owk2ogF71Un67QHGlpf2VBjM4EBS48BOXl4ZhL26MD-hMt0iqOTLu9BLyige-UNywuX0GxBI_U_ykHGTEQh9Y7e1UdEAbajxapr2qiIyDD6BJZaHIpMHYo463WlSWbttK3PSGaHR1qiE46FTbTGqa9EhhmKTNMpmkOZQPilG9uPzr9AzOo619GwpZ6ahft85akIcoqjeePLu7B1J_4h6yLzFyeIiG-bXzoJ1pOUF_ky03Bz6i3jma1vXR_KNt3oJksZo4-hNsrL9Tg1LtvdIHhiOpv_GAgOM6D4hv43U3JIFfgLxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای هشدار زودهنگام و کنترل هوابرد E-3G از عربستان سعودی برخاسته و هم‌زمان هواپیماهای سوخت‌رسان نیز از تل‌آویو به پرواز درآمده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/135449" target="_blank">📅 21:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135448">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d483a41c99.mp4?token=pwBXYOehSGZWfR8cMeRT8gccL3uru837tI7f2MaJ479eeUlSqbliH7EaHVg5XhVqu0DyugYgwpqw2LBeUjGmJzmblsG2WvHPObVul9KPqDDus_jABPv1KPE7Fp6lqW0CkIraAfjmaPi4XuMJEGgJYzCltkXlBWmw4oauGmrkwJAPYx1Ad1jFowePAuXg7yX4HlLoApTbQoJx2WqcLZ1eMYpHAuvVbI3TZb8jK35-nSBW9z9UVmDYvni7kGqRL0g0ufZCRXaQbVcxOlOESzxTzmTjM4Qa9ykyp1bpwPcY6LRvDQrzu-6Xt9AJFwiN21tZsuZ1T0tZl6f_vscJYXJY-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d483a41c99.mp4?token=pwBXYOehSGZWfR8cMeRT8gccL3uru837tI7f2MaJ479eeUlSqbliH7EaHVg5XhVqu0DyugYgwpqw2LBeUjGmJzmblsG2WvHPObVul9KPqDDus_jABPv1KPE7Fp6lqW0CkIraAfjmaPi4XuMJEGgJYzCltkXlBWmw4oauGmrkwJAPYx1Ad1jFowePAuXg7yX4HlLoApTbQoJx2WqcLZ1eMYpHAuvVbI3TZb8jK35-nSBW9z9UVmDYvni7kGqRL0g0ufZCRXaQbVcxOlOESzxTzmTjM4Qa9ykyp1bpwPcY6LRvDQrzu-6Xt9AJFwiN21tZsuZ1T0tZl6f_vscJYXJY-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک‌های بالستیک ایران شبانه به پایگاه هوایی موفق السلطی در اردن حمله کردند.
🔴
دست کم دو اصابت مستقیم تأیید شد، دو نظامی آمریکایی کشته و یک نفر نیز مفقود شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135448" target="_blank">📅 21:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135447">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / گزارش انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/135447" target="_blank">📅 21:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135446">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2fceb3f2.mp4?token=pCsjGe2qAlni2-2wuC8Y_CnBvUYO0A8pChelAD6fN4AH-ijyO0HdDJtbDnVKPJNkf7XAIAJn6z19jYRhLCeeI0aVS0LpJte2NKHjIOSZxdePvnxutGoGACQgHPEijwTBLQFFUcJyFqB5lNbIy-AyVEAmqUXwRHc6FkdMjEBtvu04734W-LgMsSxqBaRN6xQ6Wbc5wh9pNb0BQIjUPqzY57LxKV2XU7BSSTwbVypZFSy6rqJ-B_ZxC6UsWK-bZbTxD8RdAIln7WYgkYTuRqTFyK83FjHwig3YKEcfH_0s1wqi-hK7wi0g090NYoyUefUWxD946IGboYOZ-oC_RW-jjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2fceb3f2.mp4?token=pCsjGe2qAlni2-2wuC8Y_CnBvUYO0A8pChelAD6fN4AH-ijyO0HdDJtbDnVKPJNkf7XAIAJn6z19jYRhLCeeI0aVS0LpJte2NKHjIOSZxdePvnxutGoGACQgHPEijwTBLQFFUcJyFqB5lNbIy-AyVEAmqUXwRHc6FkdMjEBtvu04734W-LgMsSxqBaRN6xQ6Wbc5wh9pNb0BQIjUPqzY57LxKV2XU7BSSTwbVypZFSy6rqJ-B_ZxC6UsWK-bZbTxD8RdAIln7WYgkYTuRqTFyK83FjHwig3YKEcfH_0s1wqi-hK7wi0g090NYoyUefUWxD946IGboYOZ-oC_RW-jjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر اختصاصی که میزان تخریب گسترده در کشور بحرین را نشان می‌دهد، در پی حملات موشکی ایران به یک مجموعه استخر مورد استفاده سربازان آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135446" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سنتکام اعلام کرد ۲ نفر از ۱۳ نفری که به صورت سطحی زخمی شده بودند، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135444" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
گزارش تأییدنشده از درخواست تخلیه برخی کارکنان و خانواده‌های آنان از جزیره خارگ یک رسانه به نقل از یکی از مخاطبان خود مدعی شده برخی کارکنان جزیره برای خروج تا روز شنبه تماس دریافت کرده‌اند. تاکنون هیچ مقام رسمی، دستور تخلیه عمومی ساکنان بومی جزیره را تأیید نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135443" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135442">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmA2v7UTPvoRSPI8PBqktnQyPIcqlBi6oUS6FkacP0VeVrsnu5vXx6YhTUHjb6em2OGbTdQRffztUsJ1C30SKWZaeoFNWtwmikQNYiL5AtILhAxPilnK0A8LnAFgGoXyJbvKjVJ9goZ6SRPvqPqgqjEccMLoNRQc9XgAESVVzYZXtOTrbS475TDVCKevDyIQvR9_UZnDtyXJqhyqXJ9g8fXOoSPi6GvjmkutujNQGc5OIp0WsNd3ahExeiVYCuOTHechaHzuUGL48-qKfH-V9nDTGQe6xqONX2WvPv2gHk2Vbd1DHYxGPSbSLK3jaHIipsOHGlvlhem65ARu_HDJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پهپادی روسیه به قطار مسافربری در زاپوریژیا؛ تلفات جانی گزارش نشد
🔴
رسانه United24 اعلام کرد در پی حمله پهپادی روسیه به یک قطار مسافربری در منطقه زاپوریژیا، لوکوموتیو و چند واگن این قطار آسیب دیدند.
🔴
با این حال، به‌دلیل تخلیه به‌موقع مسافران و خدمه پس از اعلام هشدار حمله هوایی، این حادثه هیچ‌گونه تلفات جانی بر جای نگذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/135442" target="_blank">📅 21:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135441">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
تعدادِ سرباز‌های کُشته‌ آمریکا؛ از اول جنگ، توسط ایران، به عدد ۱۶ رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135441" target="_blank">📅 21:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135440">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / رویترز‌ : خبر کشته های امریکا به کاخ سفید رسیده است و ترامپ بسیار عصبانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/135440" target="_blank">📅 21:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135439">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
حمله شدید دقایقی پیش آمریکا به زاهدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135439" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135438">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
استانداری هرمزگان: فعالیت ادارات در روز یکشنبه با حضور ۵۰درصدی کارکنان و براساس تشخیص مدیران دستگاه‌ها خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135438" target="_blank">📅 21:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135437">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1e5dd4bfc.mp4?token=TKN8tOOAsl8ZnOzXAEecv7DkvFjxQfhGeQZrFWN38I_RxB7x7VBC2povLiJKK2xRvfpJJGznWXz3FGzu6T5Ax3a_XwqusRHhVV8gBktsnb2k5NmzNPNAk3CdIxShm66aiFovrvMeV75OHrVkCNa-mNcL0oOc9ctdq5DvmGPoMmVQFH_DVlEnVHrwN-GaBFXTD9bZjSz0K2SnQBApM96qBH3S8mHuh1IaQ7Vx9wQbf74QJ7qJcDySS-P1zI-E3Q-GnexX92zWSrychK6IHU7SrgwrX_KAznbWDtjAo_GN5J5wECP3o433vJot9yRPfBcrfIzrSnCDF3YGau66kkNjMLdmdE5u_m6_z75Cn0vP9GTA4cK1KIXCJr_9WZLzxFE2xqa-_B8eiIlNUG8mRY9mi0EsPw_uvH40RTRFyVOtU9O0H0-N_FdGdUxrL4WVO6tsQw64bmDKymELFAah_QnZXXnvEBWVphf7Km_RWBuatvZ-GyBBQsePEscG4__DBxgl0nnvzup1yHLQ5ZuFBo8ahH4CRkOzPGflXfTOOoTAK-p4skpkFzFqOJxBr9D2OQTTvn--YIZXVhbTSc6F44fD3d66B4_QT5fjy8ko2lmNGJtFmet5Vz8ALt5MXkMuVNhJLGqSCxN4DumeRE9MHS_90YdMTnDmZyTsgpSTocCX_0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1e5dd4bfc.mp4?token=TKN8tOOAsl8ZnOzXAEecv7DkvFjxQfhGeQZrFWN38I_RxB7x7VBC2povLiJKK2xRvfpJJGznWXz3FGzu6T5Ax3a_XwqusRHhVV8gBktsnb2k5NmzNPNAk3CdIxShm66aiFovrvMeV75OHrVkCNa-mNcL0oOc9ctdq5DvmGPoMmVQFH_DVlEnVHrwN-GaBFXTD9bZjSz0K2SnQBApM96qBH3S8mHuh1IaQ7Vx9wQbf74QJ7qJcDySS-P1zI-E3Q-GnexX92zWSrychK6IHU7SrgwrX_KAznbWDtjAo_GN5J5wECP3o433vJot9yRPfBcrfIzrSnCDF3YGau66kkNjMLdmdE5u_m6_z75Cn0vP9GTA4cK1KIXCJr_9WZLzxFE2xqa-_B8eiIlNUG8mRY9mi0EsPw_uvH40RTRFyVOtU9O0H0-N_FdGdUxrL4WVO6tsQw64bmDKymELFAah_QnZXXnvEBWVphf7Km_RWBuatvZ-GyBBQsePEscG4__DBxgl0nnvzup1yHLQ5ZuFBo8ahH4CRkOzPGflXfTOOoTAK-p4skpkFzFqOJxBr9D2OQTTvn--YIZXVhbTSc6F44fD3d66B4_QT5fjy8ko2lmNGJtFmet5Vz8ALt5MXkMuVNhJLGqSCxN4DumeRE9MHS_90YdMTnDmZyTsgpSTocCX_0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله شدید دقایقی پیش آمریکا به زاهدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/135437" target="_blank">📅 21:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135436">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d7cab844.mp4?token=sDHuMsePnyh2eA_l1ZvARBHrHV65mHs5mYXzreEnV-z0WDOA07lBMkA82fRwNJLCf1QLWpJ8TYljk-ysQOvPdrfnVBRQAZUC-WpA5ZO-CTYTZkXccW-WIMEqBSitel3UAET9tWbHV9vEpXDmOXOZ5hKXfHjXAKA1wo8hmsQNLSL6q-26p_pz3gqYimoK6ZFa30CQ11YKZnXK6K23Nrla9JONXtwFAG50bPVEr0V4vQlgDfTbkTCxs4w4HyJB7YMmFhMRqIBPvDYQXqZadzq5l8j5ME6qDgF7dPfCokSArStkG-UbP068vezv1IfaNFiJFwzDDXyMxxVrfNyB3NliUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d7cab844.mp4?token=sDHuMsePnyh2eA_l1ZvARBHrHV65mHs5mYXzreEnV-z0WDOA07lBMkA82fRwNJLCf1QLWpJ8TYljk-ysQOvPdrfnVBRQAZUC-WpA5ZO-CTYTZkXccW-WIMEqBSitel3UAET9tWbHV9vEpXDmOXOZ5hKXfHjXAKA1wo8hmsQNLSL6q-26p_pz3gqYimoK6ZFa30CQ11YKZnXK6K23Nrla9JONXtwFAG50bPVEr0V4vQlgDfTbkTCxs4w4HyJB7YMmFhMRqIBPvDYQXqZadzq5l8j5ME6qDgF7dPfCokSArStkG-UbP068vezv1IfaNFiJFwzDDXyMxxVrfNyB3NliUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از تجمع مردان عنکبوتی تو تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135436" target="_blank">📅 20:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135435">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سنتکام اعلام کرد ۲ نفر از ۱۳ نفری که به صورت سطحی زخمی شده بودند، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135435" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135434">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا: یک کشتی تجاری در خلیج عدن ربوده شد
🔴
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک کشتی تجاری در فاصله ۶۵ مایل دریایی جنوب المکلا در یمن، هنگام حرکت به‌سمت شرق در خلیج عدن، توسط افراد غیرمجاز تصرف شده است.
🔴
بر اساس به‌روزرسانی UKMTO، کشتی پس از تصرف به آب‌های سرزمینی سومالی منتقل شده و این رویداد رسماً در طبقه‌بندی «کشتی‌ربایی» قرار گرفته است.
🔴
تحقیقات درباره جزئیات حادثه ادامه دارد و به کشتی‌های عبوری توصیه شده با احتیاط حرکت کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135434" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135433">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5IZsXetjzfHuF5_enEVYzDtlgbb1q2vQu2noQgqs0WUt1jtCuyWy6nAMNNTpRQiEYu2B_kD7zXG2H5m4Kaw8hoQoH43kYTyt1PeL84JMjrfBhY-3moRAqV9T77TZw-aAEdUipB0L2_vBAKpKckxh2y8zwoJR7P8X6hC_h7lDFH1pxtxZFOtg7XH_4mqTMOpB83fjmJyXaX3ny23Qb_xFL_C3KK-A3rs3p0pvPJheCzWS0zQ5rqtk1DRfMztExhzKHds_1UACB819Cw3wOzcbgw-8h2e-xkv6z0SW4gEjpq3jsWrx9ch0wlqSPRz_-L5MVTfV-vJvNeRMFQpJv5y0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام اعلام کرد ۲ نفر از ۱۳ نفری که به صورت سطحی زخمی شده بودند، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135433" target="_blank">📅 20:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135432">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری /ادعای کانال ۱۳ اسرائیل: در اسرائیل می‌گویند آمریکا برای گسترش عملیات نظامی در ایران آماده می‌شود:
هفته‌ای سرنوشت‌ساز در پیش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135432" target="_blank">📅 20:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135431">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QM4lOny5TgZZkOSz6K9z45EkH3UI60FaqNy1zGrP_GQrE-MzBsTJJpByZmacjFk6lxtTjT438S5-x-xu_X0EkTAJyRACtcLR5eTmJJCXDdi5ReNZxnRtn3kgsiF1EM3Sc8psz-wVtZnXHYeX9FR2w__CxdoPjpsvAXCjjA9N8GORmKwXzjO0a9q_WArKWlGM2746qoJeZhTrV5KqXi6XMRQDe-IBvUq6ONRs5ssj_-LsRlWmAerWDlusCiVbz0mtHvlgHncQbxIxC32Co_sQHuktThkXcsUn5wHb7fUkJGl2GX4y_D3EcallF907JpCHK9j5R5FbpPE4yx3NoVcHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلار در آستانه 200,000 تومان...
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/135431" target="_blank">📅 20:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135430">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری/ گزارشات از حمله به یک کشتی دیگر در سواحل عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/135430" target="_blank">📅 20:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135429">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری/ گزارشات از حمله به یک کشتی دیگر در سواحل عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135429" target="_blank">📅 20:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135428">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0IKfupj5ui9nScmO0_YbQVAO8zDqZEClM5pUV0s92jCs8ZKgs4z24KG2iFtkzrL14uj91qsM8Ip1sF74x8odR5I8tJq5abXq9hVeWiS8dX_cBeLWGwUxtXJRAmqTyjiwAy2nVn4ZStTzTlD5apNe7OvpcEnCCjO0M2N2UM8PbD5WVPrsGUOAeaTWGkA0dDLUU75FGoRzdt1goRNjnFuh7xVF_tJU2St7-uoiT1E9o2I6xQVrTbZmYGxWEY-u6bqR7szTcQ1w5sekVwz-nu9tLgKfZMH16qlxa7NSu9-XYvJ83yn-R0BZ3fWe4JhdUe4qePKckFQ9kdMRKGe7Qu-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بخش مهم بیانیه امشب مجتبی خامنه‌ای: با توجه به نقض آتش بس و حملات شدید آمریکا، یه درس فراموش نشدنی بهشون خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/135428" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135427">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3243f8579.mp4?token=Cl0actOyISjKId23n-YuR2XF3gsqQusQGPR3yi15VLxo_0kEJBiEzobYK2n-TvOBl3salL2qrzZf-Zca3twQMdh5R5jajlqY_YmkikGdZMDNyL0Wb0HYh4kp3TtyA_q1yCGe--df4Byk6vr-qJnC06fReZjcRsFgmH3UXTZAotGMVSEc6hkavOmFBNgfRhjX8I4LCRn5BMtnQCPCVH5DexYgvgUhCKqxBlSff8Mr8TqRU_6R_6zV4mC6f76MrzwI8crE4BAYnJYXW8DpLsz-TrCB4s5Hx82Er5nK4pKB-iWQskGCbENLLYKdozFmV22fZydAWbejam77DMFxelgyVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3243f8579.mp4?token=Cl0actOyISjKId23n-YuR2XF3gsqQusQGPR3yi15VLxo_0kEJBiEzobYK2n-TvOBl3salL2qrzZf-Zca3twQMdh5R5jajlqY_YmkikGdZMDNyL0Wb0HYh4kp3TtyA_q1yCGe--df4Byk6vr-qJnC06fReZjcRsFgmH3UXTZAotGMVSEc6hkavOmFBNgfRhjX8I4LCRn5BMtnQCPCVH5DexYgvgUhCKqxBlSff8Mr8TqRU_6R_6zV4mC6f76MrzwI8crE4BAYnJYXW8DpLsz-TrCB4s5Hx82Er5nK4pKB-iWQskGCbENLLYKdozFmV22fZydAWbejam77DMFxelgyVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک شهروند اردنی، یک ویدیو منتشر کرد که در آن موشک‌های ایرانی را نشان می‌دهد که به سمت پایگاه‌های نظامی آمریکایی در اردن در حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135427" target="_blank">📅 20:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135426">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCr1H-kv45GTBscjw0FNBXiP_C0rz8cOERzsfAqfL_pGs0kFUynisLr975IPSsE-WZ45-Hc5MoE0GG_fHRM7SOQXZeEWQWqnftE4wdaxCCvJ8YMCdWdG2lBi2AlLHdhrQ5DevO-k2Yb66uLTf7ORnWqqFYyvvxzqqW6tyu_lWE5SAYaBwtC9AaBdurMyfnlFrirPyJFmoQA1oELoCEPXFZM7w6DAg2zMnJuA1om4YbSgt0KKYrj2xU6MGYfAgTKViiVotwZBZ7n2X8i65n6hcQVo5iHGulyelnTO0Oow2m45xrMGWIGZyGBJBLx9EXFtwOyrS-otk6-FmvWIMwavFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز، تعدادی هواپیمای جنگنده دیگر در پایگاه‌های نظامی آمریکایی در خاورمیانه مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135426" target="_blank">📅 20:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135425">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5_TkDQHWj1x1RDUZR2Uh534BiiivVidsgKoBqPubK0YRsqghnISlpBw31wuN8CVnWCIHTnWuIZz-0m8Q6N-0UuqUNZEJE0zqChsWJPL7uCcSfJYdWYnsyu37nbg8y-MizBgq2dg0PJ8uXJRQ5caFl71oLyou5RGyl0NM2dgup-AfA9UqqpoOSXcP-otibKVJFhLUn8EccngCdeHDG5MFzFat3W08NV-rPQcLaDAyaFq5UyGwMBN43_JkhxaAIEDgL3SSFQkwTUpWDVNdgiZ1d_DoKuPT1iyJkFintEeSWVpRf6Wi_qkPyigyl3NmkHFXyA9rDcJpRBJHTxVedR8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر از ۱۹۵۰۰۰ تومن هم عبور کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135425" target="_blank">📅 20:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135424">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
استانداری هرمزگان ‌از شهروندان خواست تا اطلاع ثانوی از تردد غیر‌ضروری در جاده‌ ها و محورهای مواصلاتی خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135424" target="_blank">📅 19:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135423">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
حملات اسرائیل به نزدیکی تپه علی الطاهر در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135423" target="_blank">📅 19:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135422">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مقامات آلمان هشدار امنیتی صادر کردند
🔴
وزیر کشور آلمان با هشدار درباره افزایش سطح تهدیدهای امنیتی اعلام کرد: این کشور وارد وضعیت «تهدید بالا» شده است.
🔴
بر اساس اطلاعات دستگاه‌های اطلاعاتی داخلی و متحدان برلین، احتمال وقوع حملات در خاک آلمان در هر زمان وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/135422" target="_blank">📅 19:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135421">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دلار در بازار آزاد تهران از مرز ۱۹۴ هزار تومان عبور کرد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135421" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135420">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: «ما بار دیگر تأکید می‌کنیم که هدف قرار دادن تأسیسات تولید برق و آب شیرین‌کن در کویت، از تمام خطوط قرمز عبور می‌کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/135420" target="_blank">📅 19:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
عربستان حمله به اردن را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/135419" target="_blank">📅 19:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Od0zTfF57CvNQiUDY_An4RAO2MJ04iwbCTL92c5qCTTV6692YS_9vtPp1-xKcs09KwemF4VRfYiTi-DLSyPl7nvMPimioZZxrMu023y7AbveDAvEYXkIusBI_11dHfGGS38QaP6Rq4OpFqOJgSQKAJwQmldVFFP5mL9LszXdMr5Q1b_uR7-4yHGoHsw3W7tZR_wK4HSIrZQgQCayrilXJT1Q2tonvRJ0clzkCMzBmkwzlqwyeQrrBVszlUEJX9-D9bkwHtTw2GreFs-TXKLfxSFezCZA2HdY_UkGWeUnRx_cskTio91z6YK3zAmlOpc68AtiatVTJmrvCCWFlx-XoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت خبرنگار بی بی سی
🔴
گوگل مپ داره تمام نقاطی رو در کشورهای منطقه که هدف حملات ایران قرار گرفتند کدر می‌کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/135418" target="_blank">📅 19:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اسماعیل بقائی، سخنگوی وزارت خارجه :
قرار بود ۱۲ میلیارد دلار پول بلوکهِ شده آزاد بشه، اما نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135417" target="_blank">📅 19:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135416">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مقام آمریکایی: ترامپ عجله‌ای برای ضربه نهایی ندارد و چند روزی‌ست عملیات دوگانه‌ای را آغاز کرده که شامل محاصره دریایی و حمله به مواضع ایران در نزدیکی تنگه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135416" target="_blank">📅 19:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نیویورک پست : رسانه دولتی رسمی ایران روز شنبه به مردم هشدار داد که «از پایگاه‌های نظامی آمریکا فاصله بگیرند»؛ این هشدار در حالی صادر شد که تهران حملات خود در منطقه خلیج فارس را تشدید کرده و رسماً تعهد خود به تفاهم‌نامه دوجانبه با آمریکا را که از همان ابتدا آن را نقض کرده بود، به حالت تعلیق درآورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135415" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
چند سرباز اوکراینی : قبل از اینکه پهپاد انتحاری روسیه به خودروشون بخوره، از ماشین پیاده شدن و فرار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135414" target="_blank">📅 19:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135413">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
العربیه به نقل از برخی منابع آمریکایی مدعی شد دولت دونالد ترامپ در کنار حفظ فشارهای نظامی، به دنبال وادار کردن ایران به مذاکره یا پذیرش مطالبات واشینگتن است. بر اساس این گزارش، آمریکا از چند روز گذشته حملات به مواضع ایران در نزدیکی تنگه هرمز را افزایش داده و هم‌زمان محاصره دریایی علیه کشتی‌ها را بار دیگر اعمال کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135413" target="_blank">📅 19:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
استانداری هرمزگان: در ساعت 12:30، 16:30، 16:40 نقاطی در حوالی سیریک هدف حمله نظامی آمریکا قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135412" target="_blank">📅 18:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135411">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep_TmedS_zWEAfB58rJ3qYWp6zE4YhCFaXjNzimPHsy-jJ2zobFwL8w628YnXHXsRIyuJkpcbCW0Jfdz-4obAs0Xm6s4kKapGOxxS4H2_muvFseIcAAjF_0TQPu_73LnKLrPn3_XeD5Sjzh68CuyUR3yI5z2Mx0EYQpOW6DKBUdyl6msnsJpYQrxNS3RGPcoAYpgLy1oWQGvMlGM00H7W2R9xmCWXYLyJb2MdOTzJWyaKP2Uc71z9XHvl90d_OhheKWSqtzkX0FNqh-YBESDJgd8fpdVDbzR_3bgofUC2f94RQr8Ju2UGBXUsuLnXQ7gAZuABdhsuCgeNhQff5_Dqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی: اگر ترامپ به هدف قرار دادن غیرنظامیان ادامه دهد، امارات متحده عربی هدف بعدی خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135411" target="_blank">📅 18:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135410">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v9w2b1ZxsYW8lgCPF70aZOCLvx6G1q1UcnMnZSQh7CijcDLoyIYm0Zu2cQs2wVfQmMaFLhnzf9AliStBJRxgEWJOc3v_QsNI0KcrbdBzrzKixr706a-pTJnD33KMfle_F0sCvymtMmQYlKwZznGe1Ih7RwcjyYGgiShZL-54-tixdvl4MK1Il5BPasIVthnQ-OIGjy4SF_cn4nqmDPoA0urUT4zP17NRmDC9hOKDuSM-cnHVF9tJsTNowlB8NJtMlIct2vQascI9efpANqOcm5zPIDPLRnEKV8bSiXBxu8MVRbql9jSPMikWXNJ_LsP1X6p29wTuMumYjs06NzqRcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ کلی هزینه کرد که پل تو جنوب رو بزنه، اما بخاطر اینکه رودخونه‌ی کنار پل خشک شده بود، مردم یه جاده خاکی از همونجا درست کردن و تردد میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/135410" target="_blank">📅 18:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135409">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: توافق‌نامه تفاهم باید محترم شمرده شود و از هرگونه تشدید بیشتر تنش‌ها جلوگیری گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135409" target="_blank">📅 18:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135408">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
امام‌جمعه قزوین:
بازماندن اینترنت بین‌الملل در شرایط فعلی به‌صلاح کشور نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135408" target="_blank">📅 18:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135407">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipyNjRnxfNapU1tgMmtqPtnL120805k_hy2zfSABcU9qyvVl4G06DmpNtQP4A8BEbbdat6K9U2vpiSKA6wBOJK6JSktq2dq591UtjnPo0hmVZ0HUvh8LvbUk0jd43rNK27XQbTjdCExM1WQqMdaRL0M_zZASdoOqtLOyIwWc411l1Gj5w6gvQrwgTvPWZ6uE5xwdDi0340Ig1Hlwo8EGcdebOdvCiLx4wnixwLFgojDYLLvBNk44BfRP7F0d4OLOMIeQBePghWmKzlRsepZCfHBTJTwdRYuM_F_ti77B6XVFJinl5a0qTBAOYPsMfU5QlLkr5J_azCJmriSCSP--XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از صبح امروز تا همین لحظه، ستون‌های دود از کویت به چشم می‌خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135407" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135406">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
به دستور قوه قضاییه پس از پایان جام جهانی اینترنت قطع خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/135406" target="_blank">📅 18:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135404">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
به دستور قوه قضاییه پس از پایان جام جهانی اینترنت قطع خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/135404" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135403">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
انتشار ویدئوی بمب‌افکن B-2 در حساب ایکس دن اسکاوینو، گمانه‌زنی‌ها درباره ایران را افزایش داد
🔴
دن اسکاوینو، معاون رئیس دفتر کاخ سفید، در حساب کاربری خود در شبکه اجتماعی ایکس ویدئویی از پرواز یک بمب‌افکن رادارگریز B-2 نیروی هوایی آمریکا منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135403" target="_blank">📅 18:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135402">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO8LkJ5rMieXXkUd9lzPXmDKCniD-R2mVoTuJOJw6W6Mk31T7Jr3M6WaQpt5FsoXb0G-Hq_zQ-1-c8ebmT1ArfQYTUvEu_hsBzuYHjnx3mW9Y1Cz_XidFJ2i4KqovsBuMG6BcWwv1lBWkB-dOkPcFeQknVrrGuMDe_BIndVIWytkOzRu8JNAjGz5Jphzs9B-F2DJR6iwxLYvE43z3kw-Tw-GRujMiUJ3j9e-Up5EuuSWWGO1-gc3yfmx5E9MDEELL2zb0Roeg3JLFycI8_S08EVMwv5d1y19rqRw0GQ5pSv0Fqx0HS6FzVJtuEeYAiDNHdbOBZHKIPPyzNPGLlk3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدهی ملی آمریکا به‌طور رسمی به رکورد تاریخی ۳۹.۵ تریلیون دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135402" target="_blank">📅 18:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135401">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فاکس نیوز به نقل از مقامات آمریکایی: دست‌کم ۱۳ نظامی آمریکایی از دوشنبه زخمی شده‌اند.
🔴
بر اساس این گزارش، حداقل سه پرواز تخلیه پزشکی در روزهای اخیر، نیروهای مجروح را از منطقه خارج کرده است.
🔴
به گزارش آسوشیتدپرس، از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران، ۱۴ نظامی آمریکایی کشته و ۴۲۷ نفر زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135401" target="_blank">📅 18:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135400">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTuqGLC4qwofgPVJkW_uTADGO8acOuyYaseWvflXnQgIFQqV0YLsCb0fapdxkOfbc1X99zcgQsg6vxI3eSmh4JqtrmMzRQmjt0sGTB7WDE_bLhNzet7KWfWx5lGw5Bqb5jgSV6Q0mOMcOOBjM0OWiVbzdFo7INQ7CguIlaLss0dl05HT0ql3PyCwXTHI7fM_Ry-SLo52bNF5dNCRxvxjqCY_8B9owfYr1nxX2BeUmL0b7v-Vst1lYlnSYaQw9iqGBOSUbelbsUP2MkaDZaf8yjKsARRTL1JMEFb4cgQwhuYLN595fbLdyHIVdIDTxPep5TOQHaB8Zr-AkXSsFhRusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر هوایی نشان می‌دهد، نیروگاه شمال شعیبه کویت که یکی از مهم‌ترین تأسیسات تولید برق و آب شیرین‌کن در این کشور به شمار می‌رفت، بامداد امروز هدف قرار گرفت و به طور کامل منهدم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135400" target="_blank">📅 18:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJJ9M1oBNfApS1Q7EPodHstnIdtHaZN7XwybFqZJXkZ6GO2heaMOQ_9LXa6JcPocGG6BvhZzv59RG0k4wD_uXijyucTRSLmQO4eD1LJQG7yD1jg-wZ9C4s4PzUi68xgUTt6HKqMfFl1IyHaPL3gz8fDjsmG3IwB_9sixDOnLNCRAegAYcBLRSi9Y4FBc0hGKlliH7abGpveJBvE1s1JzhCfau1EMWh3Yfw1Pkhg5o0qBeF89zce6W0PEMRUF1KM1a_zZcNiUIq4Ra7TuNLFV0zSwUxMZnHuzGG0ioFg5dHimn5iNWbA1vQn7IE5Gt7BUsoEulqoHwRy66V6odu2vqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله‌ی نیروهای هوایی و فضایی آمریکا:
پنتاگون درحال ارسال جنگنده‌های
F-35
و
F-16
بیشتری به خاورمیانه‌ست، اقدامی که نشون دهنده‌ی آمادگی آمریکا برای گسترش عملیات هواییه.
‎‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135399" target="_blank">📅 18:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135398">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4ca0c082.mp4?token=vBxTaXH7Gi5IsyL56SUqbBpfe2qMhji81JBJb-CW-ZoLVBCA6n_i_n5rGRJrMJsa5o10ssFerkFLEJwyjo_mFrc-ofwIJtF7QnumQUUmHVo5tfBuvA7tS-MErJ2J3t-Mx7i0H9PpaSl0wJtuLe2TU_Ls-cghVQcL7NQhoLE_JOzx-1Wm2raM_xwPb-ACMenvG9HGdN7Zo98r5MQ92eMU4RKHiSnY_lbGj7vKmPBIKkmqaKs9A7MNDnm44feWizCEyHpHakXp8upFzL7nmzP2E0TtRfmNnuXocXpenwYmewqw8Y2cdj_My6_2ad8v9suVb_nWXgCzMbCQOcXPPYaz6gIIocDgTFa7pwJDzFIOCl3pVxp4jo4_dmLSN4xHDR-A3U_CC727gNm2utJXmir4vpXN9FpkJHLqpDZCxpuNcthV8Ik1fmn9i9fRfxl2PunUxsB3gjzxzmhzlHMw7YEbJH4sf-2eHyvtFQ73u5pEfbGfZLa4D4GsY2CI5NhWS8di1JxvlLQW5E-ZPDSTMUw89eLiUqidyUYrl-o8egrCNB3-HLEDkcV2AfLlKWD_KRzTF6IbyJaDqKgHs5BryFm5Yr9jTublMhBE6ADRBI5I1Pe8Twqj7zhTBTQwYKH7z5pSmhJ6-qbWSSl6tPYviGxN19NR-ETHi_hqI8QFOzNL0KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4ca0c082.mp4?token=vBxTaXH7Gi5IsyL56SUqbBpfe2qMhji81JBJb-CW-ZoLVBCA6n_i_n5rGRJrMJsa5o10ssFerkFLEJwyjo_mFrc-ofwIJtF7QnumQUUmHVo5tfBuvA7tS-MErJ2J3t-Mx7i0H9PpaSl0wJtuLe2TU_Ls-cghVQcL7NQhoLE_JOzx-1Wm2raM_xwPb-ACMenvG9HGdN7Zo98r5MQ92eMU4RKHiSnY_lbGj7vKmPBIKkmqaKs9A7MNDnm44feWizCEyHpHakXp8upFzL7nmzP2E0TtRfmNnuXocXpenwYmewqw8Y2cdj_My6_2ad8v9suVb_nWXgCzMbCQOcXPPYaz6gIIocDgTFa7pwJDzFIOCl3pVxp4jo4_dmLSN4xHDR-A3U_CC727gNm2utJXmir4vpXN9FpkJHLqpDZCxpuNcthV8Ik1fmn9i9fRfxl2PunUxsB3gjzxzmhzlHMw7YEbJH4sf-2eHyvtFQ73u5pEfbGfZLa4D4GsY2CI5NhWS8di1JxvlLQW5E-ZPDSTMUw89eLiUqidyUYrl-o8egrCNB3-HLEDkcV2AfLlKWD_KRzTF6IbyJaDqKgHs5BryFm5Yr9jTublMhBE6ADRBI5I1Pe8Twqj7zhTBTQwYKH7z5pSmhJ6-qbWSSl6tPYviGxN19NR-ETHi_hqI8QFOzNL0KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش بینی های نوید کلهرودی در سال ۱۴۰۳ که دقیقا داره به وقوع میپیونده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135398" target="_blank">📅 17:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135397">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
فارس : اگر آمریکا امشب نیز به ایران حمله کند، فرودگاه های دبی و ابوظبی در امارات را موشک باران خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135397" target="_blank">📅 17:56 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

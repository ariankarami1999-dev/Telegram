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
<img src="https://cdn4.telesco.pe/file/izuuVisBsGFXo6XY0xCPAbtD0fMR4K535O32G_mpOSMHi6reHAqmzMoJhhtUh70-ID6CWxQP2ogM8_5gEZJdns4DqVU5f8izhneo1YKmNJYugG3fvUbqjW6txMPAjKNU2vazUleCFME-unKULn6-dao1XfScN5Is72UyPQLbQiAVY9RZPFiJmuapwIcu6azy5_8-WEHNwDztDcMa8HagU9qwxs6A5OhE9Ybp3U3kqJMQFcEHW2GS5ega0DEp58DzeIkF_aBBLjnBBz_FztuFAJUb9BtGgEiR7znX5ltck-ovPy65klED8nkM7ccVgf1w69eBCIi6kJzLJRdbYU_ARw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 07:15:18</div>
<hr>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است، اما تا این لحظه اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند.      اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت. @WarRoom</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/withyashar/20452" target="_blank">📅 06:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صدایی مهیب در پایتخت یمن، صنعا، شنیده شد، و هنوز علت آن مشخص نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/withyashar/20451" target="_blank">📅 06:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تلگرام از اپ‌استور اپل ناپدید شده است
، اما تا این لحظه
اپل یا تلگرام دلیل رسمی و حذف اعلام نکرده‌اند
.
اپل قبلاً در سال ۲۰۱۸ هم تلگرام را موقتاً از App Store حذف کرده بود و دلیل اعلامی آن «محتوای نامناسب» بود؛ بعد از رفع مشکل، برنامه برگشت.
@WarRoom</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/withyashar/20450" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk1eWSf4B7w4hWwdMVruEGTesHbYE1ialvTOc8ppVKi41CkD_Qn4ExwsSXH6E6x4oAwjqjAWPcHh_0_QRs7WolLwYcpjGdfAMCyxNGBlIRwHarrPRk8bxUwGIFeW3LmzDzcg3_TRMOORG5U4XDBeuRSaGr9bJAeN5mq7tduEctZfVOB66Asjg1rBVpeDtzWktB8GS8BuYHMTegj5VyHP0yF-EBAcw4z3BXKlYHVWvnfwfoXgAQvqUTlrs7oOwrfI-9rVl4dBMwOG4W7jLTjVH0JQ6y0U29yl6cd8AiU2gMLs2HPP1AN4qWT44yZwNhnGIqxKaEVwaVAnrj04niUS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مذاکرات دقیقه نودی به درخواست عربستان سعودی
@WarRoom
😁</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/20449" target="_blank">📅 04:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDGoNCW8vP_SV76Nn0hEe5pypWWmP8Vs2y7rqlPzcrwk6nlzedyUnYb9X2_fZMeUndcFC0iKcfECxX2yeAQmWssxMdTwmLJb0mTIO85fEqQHaCG_zCPi9HJrf5UafjGPcNENZUwWsu37m2WKymIWYitqbiPtcutb54l0FjLIWd8e6j4gsnRxlM85mTV6h52FvZ9lA8jUikBvG3cNaR08Vzfi1LmxtBXpUSjdqeF8WqEOWe9YX-PqSBMYughy9AK87zrLvZGs4m-O0S7T9Gecr0fj48aRxxij__xCsKqDVPRbvLBIPDmur0fGHOaUNHUYzCN9rLytUoRo076Sj2qVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا : گزارشی از حادثه‌ای در ۲۰ مایل دریایی شمال شرقی الخصب، عمان دریافت کرده است.
یک کشتی باری در VHF 16 اعلام کرد که مورد اصابت یک موشک/پهپاد قرار گرفته است.
مقامات در حال بررسی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/20448" target="_blank">📅 03:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZYaGTfM-iYRR-2csdQyOMTqQMMtMxprqrUzaR7A-9YUvcvxiw6iZfIrc0nHNN1XSeUrEHNaXRswLFJu-8ojUiRCbBMjLrVp_HBC7e5o1rt6ODen3kirG1IRiVmNfi3s3Dib0ZvuJdBkgiiMb9nSk9G2fBoDw1XLS1EkfKk3i-Wu_Wgss86LDiz_ZINXROiXh_lD4Wf9b8AGxb_qfkP6nelQnwIRUKUnwtdeFaJvZzW5XxlWwVKs2Vyeu5No9L3Mx4YyaWh2N0Vu_cJc5W2qz2LbKmy1OIZtqpz3OTkCqANRILmZnBVBMvGWRowDgohAppHx4-DyUce6Pbn_EgeD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت هواپیمای ترابری نظامی C-17 گلوبمستر هم اکنون در مسیر آمدن به منطقه هستند!!!
@WarRoom</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/20447" target="_blank">📅 03:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کانال ۱۴ :مسیرهای دیپلماتیک ایران عملاً از کار افتاده‌اند.
به گفته درور بالازاده، تحلیلگر کانال ۱۴، مجتبی خامنه‌ای،  رسماً اعتماد خود را از تیم‌های مذاکره‌کننده ایرانی و آمریکایی سلب کرده است. دکترین تندروانه و بدون امتیاز احمد وحیدی، فرمانده سپاه، اکنون سیاست رسمی آنها است.
@WarRoom</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/20446" target="_blank">📅 03:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20445">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">لاکهید U2؛ شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید لباس مخصوص فشار بالا شبیه لباس فضانوردان بپوشد تا در صورت افت…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/20445" target="_blank">📅 02:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTa6thrm3yCSE4VephY-oQ54fnTomeMBndNSqbtpPHnWa38Ef7J58W_bq3PBbBcNLX6V0P_oPtTeYXqC2WD5VDAdsENLs0Z6nBMFztZQlAbrmMLyTCAW3LzyN2AVfGQbXQQj4_DpvTH7dqgWAkBAkE1Gp6rRJDAbvsFWAKox2y8_y-FJkziFsDaQ09omoQ6MeqUDMNbimeK3BKGjAmGbkEGjb3YSdLiHWivWlyufw_PItMK8Gi82WG4Qt0wc5Ctxo5jDzrkbsZqbjEKWBlq4RglUk17l8gv53hsH9VwAXTlj_fl9z-9eZ2536xROr7pt0r7sdgt-VRArPMXLnlbPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاکهید U2؛
شبح خاموش آسمان‌ها به پرواز در آمد
🚨
🚨
🚨
🚨
هواپیمایی افسانه‌ای که در ارتفاعی پرواز می‌کند که بیشتر جنگنده‌ها حتی به آن نزدیک هم نمی‌شوند. خلبان آن به‌دلیل پرواز در ارتفاع بسیار بالا، باید
لباس مخصوص فشار بالا شبیه لباس فضانوردان
بپوشد تا در صورت افت فشار کابین، جانش حفظ شود.
با دوربین‌ها و سامانه‌های شناسایی فوق‌پیشرفته، از صدها کیلومتر دورتر کوچک‌ترین تحرکات را زیر نظر می‌گیرد و ثبت می‌کند. با وجود گذشت بیش از هفت دهه از نخستین پروازش، یو-۲ هنوز هم یکی از ارزشمندترین چشم‌های اطلاعاتی آمریکا در مأموریت‌های فوق‌محرمانه به شمار می‌رود
@WarRoom</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/20444" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20443">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری های رژیم : شنیده شدن صدای انفجار در کویت و صدای آن از بصره عراق هم شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/20443" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش پرتاب موشک از ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/20442" target="_blank">📅 02:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMI6zUPMcC-jqomKA0Mj46mpp1-MLz1QQJxIGObJMbbn7eUeq9Nf6YvoePQpy7LiHUrtw1SQ_Te81gapKrpHz3_kiU9Ij5MCi41bSU6SWDnh-7JywD1_FAKeEUTaUhTk_VfhlEUclEgoRNhs_30EyDP3E50Jpr7BWFkuEYakMaZT4yC-yMabYCRx-KQ1Iw2dUIbKrh0mr1JICoKlzu-MdShCYjw1PDaKcPjSSsGj0lEoheHtROklLJTdUehMD5wgUsjvQ9yVcwr-EzREUMJ_lbyCQ34DgLqx8Mpb-zZTXKDNDhzUquV_azH3MZ5M75W-1xvnfOiximjkUYagRnrgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت یه کاربر خارجی : اگه نقشه ایران رو برعکس کنید؛ چهره ترامپ رو میبینید!
@WarRoom</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/20441" target="_blank">📅 02:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پاکستان ادعای ترامپ درباره آغاز مذاکرات با جمهوری اسلامی را رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/20440" target="_blank">📅 01:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV3Ow4QfiIsyzCegHg9Xb-T9dA411QVfz5s9gnPJycQJ9m5mhVPnHqLiIBzlBcMDecpf6zYD1lwkWLMTsGwdOE4v4h0FjHiO8QS_Mq1qSB-hrBnXhBv3PrxSudCBWY7Y5X8OSg3TvalqYUhB_WMaXNtaEaEsLGF78pjzmahZG7sLZMQk3eDcPmqU1B1jyyMs9vfUJlDUUqyyReszXLVcrz8hc2y4Ff7YV0sVz3w72zU4H-pKPxx3f5qshaE166RLpH8MSrwIvImG85c9nYllS7w7gnpoCTi9mww_qioT8MG5ZGTePWCBw4XxRoM8bOWCbrJEAygImVPP9r8U_N9gEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اسرائیلی (یدیعوت آحارونوت) : «تو ما را دیوانه کردی.»
‏ ترامپ: «من حمله خواهم کرد.» من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@WarRoom</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/20439" target="_blank">📅 01:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGT4NV0wy1ZLt4sYainLNST556nWJemHxhj_kseAukCqmbpUtvivf8rWzfPVpvHasEjwMUtG8Qx_CiKrRW78Xg0tlP1XLtF4SkTj6L7vhAvHBzMS9hvZJD-02VBQlNPe3gYCQDA_vrAJ6xsJwDanzVa7aOji1yFXj66-YAJ7mafd3BNxvPc5jgy5yXRzf4cfTPqYe2IUbNdT2N-nFemPloBvdFSkhMo3IVzn5m2Rs9gjID66OgYIdIfp6E0wotQKMxFNYS4ZHg7uGWMPqmzgkZDCb3xk1nseFxiogkT6KzhnCh8tB8-vsYUNJgKxqvZ_uKRNevESlpJKDwyQHd3KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون
یک پهپاد سپا، مقر یک گروه کرد را در منطقه خبات، واقع در استان اربیل غربی عراق، مورد حمله قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/20438" target="_blank">📅 01:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩ https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/20437" target="_blank">📅 01:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIP1QllaazSp2pBAElFvHCZpr7KujK30QDlpjWG8kG3EEtTex6ppRhEHv0CejMOqv3G9wXO2Suv8pOlQpPJN8WglT0_r_gej3fUoSM1Jf-oGS6LcRknAyKTOXVu8-gtCqhRmi_TJhnaOsAyukSHRV6avlVxrhuix9UKLXeOhU6cQz1aZtFBSf_X6zDuNWD8rCctDcn3XnpgYn_VKPWyzcNfkNUvJgM72NzQTtufo-yPAT22e10ff8wepxWgug14VFvyPZ4Q3o2ZQds6rpp0bnqttI-V1IOQb6kF1JlSxaY9_f6HKinqsOIgVqtTnIPfGzFkdIvOODG2kVFYSM8nfCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : دلایل به تعویق افتادن حمله از طرف ترامپ
اگه شما مورد دیگه ای‌میدونید بنویسید ، حتما تا آخر ببینید و کامنت لیک ریشیر فراموش نشه ( کارهای اداری )⁩
https://www.instagram.com/reel/Dbl_dAtIsre/?igsh=andsNWUxa2tqaHZs</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/20436" target="_blank">📅 01:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/20434" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20433" target="_blank">📅 00:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=rPIjN83ge3S3eKhAwg04gSeHOjTw2XMMK299YUX3NKmSU5jiVDbfAIXqoE8Bo8tAvoiqyVO3q8aePPaOsPJzDSmH4gW6_84FqS-6B6DBpQXMC5Y9d2by4Py_GJuYx1QPBmypMOPm9uu0Jpd_VQ91sXgtLVk5m1g3cbllcKAR87RzVKd1sz9co0k915LBgeGyDd_ftWewBtl2GJ0dMdMMepP8i41eCxncV7L14jMIbIsuL73ojikXimM9dZWBO1i6T52PH6zmco3c3ZocY6YsQ1GfQ9YLKWqBlYnsyH6bTnWGij7u3OYOGypUiZHmJkEQK7Yeiq5NBgUjRXm-SadosA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a075dbac8e.mp4?token=rPIjN83ge3S3eKhAwg04gSeHOjTw2XMMK299YUX3NKmSU5jiVDbfAIXqoE8Bo8tAvoiqyVO3q8aePPaOsPJzDSmH4gW6_84FqS-6B6DBpQXMC5Y9d2by4Py_GJuYx1QPBmypMOPm9uu0Jpd_VQ91sXgtLVk5m1g3cbllcKAR87RzVKd1sz9co0k915LBgeGyDd_ftWewBtl2GJ0dMdMMepP8i41eCxncV7L14jMIbIsuL73ojikXimM9dZWBO1i6T52PH6zmco3c3ZocY6YsQ1GfQ9YLKWqBlYnsyH6bTnWGij7u3OYOGypUiZHmJkEQK7Yeiq5NBgUjRXm-SadosA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ‏عراقچی در عراق
😂
(مراسم اربعین)
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20432" target="_blank">📅 23:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20431">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانال ۱۲ اسراییل : بانک اطلاعات اسراییل برای حذف سران نظام در حال تکمیل شدن است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20431" target="_blank">📅 22:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20430">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دونالد ترامپ با «فاسد» خواندن کسانی که دست به افشای ابعاد بزرگ طرح او برای حمله به ایران زده‌اند، تأکید کرد این افراد باید زندانی شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20430" target="_blank">📅 22:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20429">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارشگر شبکه 12 اسرائیل:
پس از 30 ساعت سکوت در نوار غزه: یک پهپاد متعلق به ارتش اسرائیل به یک خودرو در خیابان الرشید در شهر غزه حمله هدفمند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20429" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20428">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">محسن رضایی: اجازه نخواهیم داد هیچ مسیری غیر از مسیر ایران در تنگه هرمز باز شود. حتی اگر آمریکا یک ناو هواپیمابر را به مسیر غیرقانونی تنگه هرمز بیاورد، آن را هدف قرار خواهیم داد.
آماده بودیم اوکراین رو در سه نقطه بزنیم اما بعدش عذرخواهی کردن و پشیمون شدیم
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20428" target="_blank">📅 22:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20427">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ: ایران از طریق افشاگری‌ها از حمله مطلع شد.اما اگر این روند ادامه پیدا می‌کرد، بسیاری از افراد در ایران باقی نمی‌ماندند.
می‌خواهم به ایران یک فرصت آخر بدهم قبل از اینکه "اقدام قاطع" را اجرا کنیم. امیدوارم آن‌ها با عقلانیت عمل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20427" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20426">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ:فردا آخرین فرصت برای ایران خواهد بود.
گزارشگر: آیا ایران حاضر است به آزادی کامل تردد در این تنگه بازگردد؟
ترامپ: من اجازه نخواهم داد که آنها هزینه دریافت کنند. اگر کسی قرار است هزینه دریافت کند، ما این کار را خواهیم کرد. ما کنترل کامل را در دست داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20426" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20425">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=S4l14wlvJQEl2Mq7RArJT-4EYM3G_j83IE0bLzmv7Y0fE7JHK6lwfZAw_e-2QyT-Dn9BQyLSSX2H_7hUajRVyLAglXwE5TufrHGvlQL2dVOmYXA_kaV_wboB2l07WfQ3c9-rDBX2zYgKcaB6QP-gfSMcG5SEwLdH6V7s3CbJUYDwAosk6hLQbcixsNEwv_QLcHZsxqxJB37AeGHgiCxEu3KwsqUXqmsAfmPHbTjFYf6MBok-1SyYp14AqSyYv7H4KiQFTVmLS3xW2m2e_-Sl8Td6pF9JH6JR54SW-cKlnXjkFS8AJPUkEwlWYjK-eBRPif463BoHpIzbJXFpkVMeLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d709d0023.mp4?token=S4l14wlvJQEl2Mq7RArJT-4EYM3G_j83IE0bLzmv7Y0fE7JHK6lwfZAw_e-2QyT-Dn9BQyLSSX2H_7hUajRVyLAglXwE5TufrHGvlQL2dVOmYXA_kaV_wboB2l07WfQ3c9-rDBX2zYgKcaB6QP-gfSMcG5SEwLdH6V7s3CbJUYDwAosk6hLQbcixsNEwv_QLcHZsxqxJB37AeGHgiCxEu3KwsqUXqmsAfmPHbTjFYf6MBok-1SyYp14AqSyYv7H4KiQFTVmLS3xW2m2e_-Sl8Td6pF9JH6JR54SW-cKlnXjkFS8AJPUkEwlWYjK-eBRPif463BoHpIzbJXFpkVMeLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: مذاکرات به سرعت، به یک شکل یا دیگری، پیش خواهند رفت. موضوع خیلی پیچیده نیست.
ما قرار است فردا، به طور کامل، تنگه هرمز را باز کنیم.
سپس، درباره توانمندی‌های هسته‌ای ایران صحبت خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20425" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20424">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ درباره ایران:
"این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است."
ما دیروز قرار بود آن‌ها را به شدت مورد ضرب و شتم قرار دهیم… با قدرت بسیار زیاد… قوی‌تر از هر حمله‌ای از زمان جنگ جهانی دوم.
اما ما اکنون در حال گفتگو هستیم، این گفتگو بنا به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و سایر کشورها انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20424" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20423">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f308e1bdbb.mp4?token=LmPPpGM1K9LEPR289xSowll6wVcUVuKVZT9K_MRwB2HLNK-8umocvABKiqhAIan2wD7Ak5LvRF7NDYO8MpJrbTumL56921ybKTud3Wegi9F1SXMTn83v4LxhyoJ6etVoGpKOHU1HVJ-xfYdoHI4He1d0KMJ5m0zl7g9WB6rvDmCb5DH6SvoswVKCxajnbQ5IUJVGYDWhU_k3ikXg-5uV_NFSIFM3sn3sgCqQlgvLBwqK7wT-4hW1lT_TFVDthW6prNnUppDXiVOB0m-8YHKF43Gm6nMD8v7CUH3peFLpG704wCGBV2w_deXZQunMAqfcsBZTfpp3uCxsSnLI41JTkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f308e1bdbb.mp4?token=LmPPpGM1K9LEPR289xSowll6wVcUVuKVZT9K_MRwB2HLNK-8umocvABKiqhAIan2wD7Ak5LvRF7NDYO8MpJrbTumL56921ybKTud3Wegi9F1SXMTn83v4LxhyoJ6etVoGpKOHU1HVJ-xfYdoHI4He1d0KMJ5m0zl7g9WB6rvDmCb5DH6SvoswVKCxajnbQ5IUJVGYDWhU_k3ikXg-5uV_NFSIFM3sn3sgCqQlgvLBwqK7wT-4hW1lT_TFVDthW6prNnUppDXiVOB0m-8YHKF43Gm6nMD8v7CUH3peFLpG704wCGBV2w_deXZQunMAqfcsBZTfpp3uCxsSnLI41JTkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «از همه شما به خاطر حضورتان در اینجا متشکرم، چرا که ما گام جدید و بزرگی را برای حمایت از خانواده‌های فوق‌العاده نظامی های خود برمی‌داریم... امروز، من یک فرمان اجرایی برای ایجاد اولین کمیسیون همسران نظامی ها امضا می‌کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20423" target="_blank">📅 21:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20422">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=H4iyMA8fgw9lI2J_iSTygM4tDVWHHjkj1a2ydSbZ9AUQCpoukt0kt8Q6cOVwh5HhhIfyQpnL7f5_VJFJ1TRdJGnAsyqNgr9DYw1pbRV9RzuQr8OjuaZ4UtdGtH3eIMTwICt6WdgiYhHkm-ZJt2tpqISX6LsfoehKOyZd41vOcPh9uEwzQgFbu6dAxZddaB2T5W9aU4rVnK5OCs7JH_IgEyoElrWdpvFL7_Vp_RJrvFuzroEYuvBt9XGk1ACzyuBsiqZFoyikzWyPkMwuOcqD3SRUKu77a1EPyIZwF5EoNwPz1rOxyorqhNBkb795ibGRuZiHvgQ1IlZkAPnz0Oygyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb6721586.mp4?token=H4iyMA8fgw9lI2J_iSTygM4tDVWHHjkj1a2ydSbZ9AUQCpoukt0kt8Q6cOVwh5HhhIfyQpnL7f5_VJFJ1TRdJGnAsyqNgr9DYw1pbRV9RzuQr8OjuaZ4UtdGtH3eIMTwICt6WdgiYhHkm-ZJt2tpqISX6LsfoehKOyZd41vOcPh9uEwzQgFbu6dAxZddaB2T5W9aU4rVnK5OCs7JH_IgEyoElrWdpvFL7_Vp_RJrvFuzroEYuvBt9XGk1ACzyuBsiqZFoyikzWyPkMwuOcqD3SRUKu77a1EPyIZwF5EoNwPz1rOxyorqhNBkb795ibGRuZiHvgQ1IlZkAPnz0Oygyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما اختلافاتی با ونزوئلا داشته‌ایم، و این مسائل به شکل بسیار خوبی به پایان رسیده‌اند.
و ما اختلافاتی با ایران داریم، و این اختلافات نیز به شکل بسیار خوبی، بسیار خوبی پیش می‌روند.
@WarRoom
یاشار : مثال قشنگی‌زد
🤣</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20422" target="_blank">📅 21:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20421">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=rq7hVVRpbPFwjHebPt4O_9QJToCBZkdD5zcU6J8gMolAlxvm5KWSh00ZeFUG-yuOgVN9PDPOKTsdg6maIrIxYEz8q2Oi598S_cJNj51g--zmtwHttpp_hM037IeesrmgVrCQS-1mzTLA9DZUHbSf6p2jVrLX0rKXZcC48hi4B5Z8MWBItAwqbym7O8EEyg2HjxY7QvqHaJwH19bQFS1fbGB-Hyb6ZnkRKlMSQrEMR0ptMkvclwKlKIXHqGA40UGFT6kXnYVgKp5taRuERL9BWvCAcljElnEMZ5WCXG66V-NEOBwy7tPn-6sG4BiOqbBd_CkpopCIJksakHAEhNIMHhqcLfNq6TxWH5czf5F02c-YKqStVPaIDI7kTFWbTNPuAC1ATR2JkhCKzCngOo0Ly9HfQKBSgOmxjUC4UVRndjBWgpnRp7EIBUteOZrYLlj5PiycueGnet3jZZxiczD4LsvCbghE4BPz9VEa0_h-4xCXuCzecfVgi2ZXpVU-gVcvAbfR4IVHys5xhP9yRX3r9hCCi11r9WBrTz2Th2MOFq9bL0UbRrwqIbTjkhhze37r_VZ1J3mdmzfVrZj4xjVtlbRzhmIkd-j7BFS4XPp6W_onofY26Rv6mKa-Arpbt1jOYPwQo1QTirkGetTphyktCWbM8-L73pd--JNm-fHFWtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9742ced6.mp4?token=rq7hVVRpbPFwjHebPt4O_9QJToCBZkdD5zcU6J8gMolAlxvm5KWSh00ZeFUG-yuOgVN9PDPOKTsdg6maIrIxYEz8q2Oi598S_cJNj51g--zmtwHttpp_hM037IeesrmgVrCQS-1mzTLA9DZUHbSf6p2jVrLX0rKXZcC48hi4B5Z8MWBItAwqbym7O8EEyg2HjxY7QvqHaJwH19bQFS1fbGB-Hyb6ZnkRKlMSQrEMR0ptMkvclwKlKIXHqGA40UGFT6kXnYVgKp5taRuERL9BWvCAcljElnEMZ5WCXG66V-NEOBwy7tPn-6sG4BiOqbBd_CkpopCIJksakHAEhNIMHhqcLfNq6TxWH5czf5F02c-YKqStVPaIDI7kTFWbTNPuAC1ATR2JkhCKzCngOo0Ly9HfQKBSgOmxjUC4UVRndjBWgpnRp7EIBUteOZrYLlj5PiycueGnet3jZZxiczD4LsvCbghE4BPz9VEa0_h-4xCXuCzecfVgi2ZXpVU-gVcvAbfR4IVHys5xhP9yRX3r9hCCi11r9WBrTz2Th2MOFq9bL0UbRrwqIbTjkhhze37r_VZ1J3mdmzfVrZj4xjVtlbRzhmIkd-j7BFS4XPp6W_onofY26Rv6mKa-Arpbt1jOYPwQo1QTirkGetTphyktCWbM8-L73pd--JNm-fHFWtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : خاورمیانه دیگه اون خاورمیانه‌ی قدیم نیست، ایران هم تاحدودی هنوز قویه و ما دیدیم که تو درگیری‌های خلیج فارس چطور میجنگه.
ولی بنظرت چرا اونا تو یک ماه گذشته به ما حمله نکردن؟ چون میدونن که ما قوی‌تر جوابشونو میدیم.
الان یه محور شیعه‌ی تندرو هست و یه محور تندروی سُنی هم داره شکل میگیره، ولی ما با کشورهای مسلمانی متحد میشیم که اینارو قبول ندارن.
درحال حاضر اکثر ایرانی‌ها، به اسرائیل احترام میذارن.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20421" target="_blank">📅 20:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20420">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کانال ۱۲ اسرائیل: نتانیاهو در حال برگزاری یک جلسه امنیتی با حضور وزیر جنگ و رئیس ستاد مشترک نیروهای مسلح است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20420" target="_blank">📅 20:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20419">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c66da50c.mp4?token=WHXzWBx7T5WTSsKVrMe54Jb7AcDRp3UulZ8Yt4Y_AUlkcXLGBns2m6KiFI1XSaTz-phWu8Xhq426ZYtgVC83jlNAqCnYoxLhZ5Zy1gxddC89S6TkvYqawtpA8UMifRNgzJmpsiSoTBNQViqwRtOAmi89YXMibHc8NjqbcPMe19kZYY3pnNym8D9IlO-f3AU3J4cqi2-BOj7ivQ9042oC8x30vOGVacQdJpuMoxROpFql0uU80vkFcpse5PFh4Mw4TnNuys6qfC3jfzSKIYial6pmZOKfEIkluljKMAYjNTk0x8V8CMR5_uR52Y3DhQ9ykgm_OzS5bWcJwb8uqMzoNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c66da50c.mp4?token=WHXzWBx7T5WTSsKVrMe54Jb7AcDRp3UulZ8Yt4Y_AUlkcXLGBns2m6KiFI1XSaTz-phWu8Xhq426ZYtgVC83jlNAqCnYoxLhZ5Zy1gxddC89S6TkvYqawtpA8UMifRNgzJmpsiSoTBNQViqwRtOAmi89YXMibHc8NjqbcPMe19kZYY3pnNym8D9IlO-f3AU3J4cqi2-BOj7ivQ9042oC8x30vOGVacQdJpuMoxROpFql0uU80vkFcpse5PFh4Mw4TnNuys6qfC3jfzSKIYial6pmZOKfEIkluljKMAYjNTk0x8V8CMR5_uR52Y3DhQ9ykgm_OzS5bWcJwb8uqMzoNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی همچنان به اجرای دقیق محاصره اقتصادی ایران ادامه می‌دهند. تا تاریخ ۳ آگوست، سنتکام ۴۴ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی را توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20419" target="_blank">📅 20:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20418">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ux9btNUkzuMs3QKEYoBqtkrMvAYZbsJLfBcozJilPu5L1PySyGk7qgQEJa5PmWSCGKygM_SsKWNn2sLX1eX4fg_PAbHyilZFdmM9wp2nvs8S4roKXWdzVs17HqWm7Q80lnUzWkoEEomBvigivTXn2N4AhYe_OxrTxW9wkfPBXpdKq29UopOYYGMJzKa_6FVnBXXFYwj4KajTJ7h_Y_RQJtZw_Cl3_hj-J4Zsw05GvOT8hNXijk7rzInq_txl29rYQ237Exo29BMTnvpivBs83aKYs_3TKAU95pZOxTcn2Vt-kCXOFc04oSOUuXalQ-8iVyDvIPwZKAr2EeYO6_ONzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک چترباز ارتش ایالات متحده در حین اعزام به خاورمیانه، آموزش سلاح‌های سبک را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20418" target="_blank">📅 20:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20417">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مارک لوین :
من از اسرائیل حمایت می‌کنم
من از اوکراین حمایت می‌کنم
من از تایوان حمایت می‌کنم
من از مردم ایران حمایت می‌کنم
@WarRolm</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20417" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20416">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرگزاری سی بی ای : مقامی آمریکایی اعلام کرد علی رغم ادعاهای ترامپ هیچگونه برنامه ریزی برای مذاکره با مقامات ایرانی وجود نداره
تماس ها صرفا از طریق واسطه ها جریان داره
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20416" target="_blank">📅 20:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20415">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20415" target="_blank">📅 20:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20414">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=MgvocG10zhpjIK0I2VUFHMohzgo_sS6ukJJrX9CNZjmMGEgwxcuucc5I-DEc9cK7L61O_1YjLBX4PkUckOCbB-FYzmpLVX0bytbfb4ht6NB9-ZuErRK5VtVlt8q2z_CaPtXcgClzfJ3l3IWf-OoeOJs4KkXvXoNpJomXRuug3WGfwzNb5QTWN5FP2I-W8NFGpPhzUIa13WEA5knv8qfRJd2aNkzCW6SrtC9r26-tRc0LoDuyfZ2XXO7Xim-aXYp3NK7inBSzyDCcy28d1heIRQUfbjQjamP30dhnsgH-Mifzmcb4BQwOv3RFNHCl2LdmjQX5gQjydE5NPKd1VDvxPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=MgvocG10zhpjIK0I2VUFHMohzgo_sS6ukJJrX9CNZjmMGEgwxcuucc5I-DEc9cK7L61O_1YjLBX4PkUckOCbB-FYzmpLVX0bytbfb4ht6NB9-ZuErRK5VtVlt8q2z_CaPtXcgClzfJ3l3IWf-OoeOJs4KkXvXoNpJomXRuug3WGfwzNb5QTWN5FP2I-W8NFGpPhzUIa13WEA5knv8qfRJd2aNkzCW6SrtC9r26-tRc0LoDuyfZ2XXO7Xim-aXYp3NK7inBSzyDCcy28d1heIRQUfbjQjamP30dhnsgH-Mifzmcb4BQwOv3RFNHCl2LdmjQX5gQjydE5NPKd1VDvxPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20414" target="_blank">📅 20:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20413">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WugiyP8IoEdIcOaz3jn6e85qYpvbMGsQApOu-crlDh-Vu-w4j9MKWBvHn32pvNG2yiZ-sZfnfHaIOllSO58eUZF68Z6qVvObhoePvuip-aqYLyvJWhWv6bovIxNbv7N54lX08Ql_Ivaij1D-_pRedX_r3wRAxhpCadLEOH1Sa8-iwqbndSx6K2exa8x9XDBtFoA322rnjiR0kThYsVmymm2-NtUNSKHW3Vs8WMUiC9FLZxB3xAeV7D1Kv-2jqZLMK5OtxClvhNwGPw3KFLsaKT8Jaee5o44dNklchDXCgU7ERzW-iWPwHSJ0wYxYZgmLtmEQuARnEvs7z7hkrp0ATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
رهبری ایران به شکلی باورنکردنی دورو و فریبکار است!
آن‌ها درخواست برگزاری جلسه می‌کنند؛ بعضی‌ها حتی می‌گویند «التماس» می‌کنند. گفت‌وگوها آغاز می‌شود و قرار است در آیندهٔ بسیار نزدیک جلسات بیشتری هم برگزار شود، اما هم‌زمان آشکارا و با افتخار ادعا می‌کنند که هیچ مذاکره‌ای در جریان نیست، هیچ موضوعی در حال بررسی نیست و فقط با «عمان» در ارتباط هستند.
@WarRoom
بعد هم طبق معمول شروع به رجزخوانی می‌کنند و می‌گویند تنگه هرمز را با قدرت در اختیار و مدیریت خود دارند؛ در حالی که این تنگه هم‌اکنون به‌طور کامل تحت کنترل نیروی دریایی ایالات متحده و «محاصره دریایی» ما قرار دارد؛ چیزی که برخی از آن با عنوان
«دیوار فولادین ایالات متحده»
یاد می‌کنند.
هیچ چیز بدون اینکه ما بخواهیم وارد ایران نمی‌شود و هیچ چیز هم وارد نخواهد شد، مگر اینکه یا
توافقی
حاصل شود یا
تسلیم کامل
صورت بگیرد.
چه ایران بخواهد این واقعیت را بپذیرد یا نه، ما در حال مذاکره برای یافتن راه‌حلی برای مشکلی هستیم که خود این کشور طی دهه‌ها به وجود آورده است.
موضوع بسیار ساده است:
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20413" target="_blank">📅 20:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20412">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یک منبع ایرانی گفت که تهران پیشنهاد اخیر ایالات متحده را رد کرد و تأکید کرد که تنگه هرمز تا پایان جنگ به طور کامل بازگشایی نخواهد شد.
این منبع همچنین ادعا کرد که واشنگتن بسته شدن مسیر کشتیرانی جنوبی را پذیرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20412" target="_blank">📅 16:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20411">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20411" target="_blank">📅 16:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20410">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">لحظه نشستنش رو استورررری کردم
instagram.com/yashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20410" target="_blank">📅 16:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20409">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c929d388fd.mp4?token=N3v52uMbP6LFIzP08MOC2CskUcAkh2hOgR1SFY6EhZSm6gjOvZxMJTTxvdkB8-rs4alXk5Irz3VI-_gCXtAl57Phhp2Elrch2YSm2EMtztq1lY2ILTOz0jmMFLmKEXSj8o0YbmrfzVSO4XoUDiPJBUvksUD_E8w8fWnEKvbC4UhfP7Dl5WlAQ3RJXcKUkvtddf_aX4TcbhQrH6vQkRONlLsi6MY-CZm2wtsdC30ftOROG6gR0lMTrrkNBl1303rLJS9d6J3T_ohIsa38hg_mxWPW72DNzSZZaPL62tdz9NBbpxar4XwYqij-VjyiULVUXYcpEn19VwgVRMK9lchBPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c929d388fd.mp4?token=N3v52uMbP6LFIzP08MOC2CskUcAkh2hOgR1SFY6EhZSm6gjOvZxMJTTxvdkB8-rs4alXk5Irz3VI-_gCXtAl57Phhp2Elrch2YSm2EMtztq1lY2ILTOz0jmMFLmKEXSj8o0YbmrfzVSO4XoUDiPJBUvksUD_E8w8fWnEKvbC4UhfP7Dl5WlAQ3RJXcKUkvtddf_aX4TcbhQrH6vQkRONlLsi6MY-CZm2wtsdC30ftOROG6gR0lMTrrkNBl1303rLJS9d6J3T_ohIsa38hg_mxWPW72DNzSZZaPL62tdz9NBbpxar4XwYqij-VjyiULVUXYcpEn19VwgVRMK9lchBPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20409" target="_blank">📅 16:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20408">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اتاق جنگ بایاشار ، رو سفید تاریخ : ویدئوی اتاق جنگ مربوط به ۴ روز قبل از شروع جنگ ۴۰ روزه(۵اسفند)، هواپیمای ریوت جوینت از همین مبدایی که امروز پرید، یعنی میلدنهال انگلستان، و به همین مبدأ که امروز میرود یعنی جزیره خانیا در یونان، پرواز کرده بود و من به شما گفته بودم
🙌🏾
@WarRoom
I TOLD YOU
🫵</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20408" target="_blank">📅 16:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صدای ری اکشن هاااااا نمیادددددد</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20407" target="_blank">📅 16:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20406">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیج اینستاگرام رو باز پروندن ! و بازم برگردوندم !
😂
پیج دوم رو داشته باشید حتما
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20406" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20404">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1c503433.mp4?token=Eqd9aHWliLzWNwysDcQGVdMmpBkWpoUX_GNo8YQLSSLoHEjBUH-bbMpNO28KXj7_mMuQWgPEIe_mczUTVtnnlR7abnlUT8uR-1jfN3VAu7GiQIwIW7rdEiIGz6oxM06YCnT3RH4qfsRGrN_wZrBhCdWVAC8fWkTUYP4ORJoJhPKgbgMXb17mYjTBOc-Da7gOGyneWYVIMIRv-BzevoojKA6MgDrrB7IbdiEGC-9K7YcaMiu9jAotD8BOHoNpUFdHM_0keZBeThmBy-rlBhKXR0d9yih4GKWjKW7bNpRF7BSnKDHB_vEFhq8P9RlTJMwKk8kPLnbfxWV25Ekf0saunRDE6lnl9GdeSU5SihG_807nMGjNvpb6uGn600WN2LcCTjEN5BDoDoelST1E5HQynYi2xcGd9EFNY2iSds2YYjOGuCGNUe9mps_fXDTRHZp6j1j62J6jUtrbGqH5QyxkuMDvGQvC3ZRYX8PVIFLJK1hhDhIYB094Bl1RYvLZpbG0eRcnA74BhObfuqattf7Rb4Q39XXIoXWFWx9cFMtFrVB3VdP_2tytkaYCJ1-rByOpUI3Nb58pFbNnPYZUDmpcxSm-99be0yIwrBJjfUgJ8seL9QCezGohyvztX9VWVCqXZUEByBrv5Gg4phjdg0ZQgfqEa1YuFUQ5Xpp1nxYhbUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1c503433.mp4?token=Eqd9aHWliLzWNwysDcQGVdMmpBkWpoUX_GNo8YQLSSLoHEjBUH-bbMpNO28KXj7_mMuQWgPEIe_mczUTVtnnlR7abnlUT8uR-1jfN3VAu7GiQIwIW7rdEiIGz6oxM06YCnT3RH4qfsRGrN_wZrBhCdWVAC8fWkTUYP4ORJoJhPKgbgMXb17mYjTBOc-Da7gOGyneWYVIMIRv-BzevoojKA6MgDrrB7IbdiEGC-9K7YcaMiu9jAotD8BOHoNpUFdHM_0keZBeThmBy-rlBhKXR0d9yih4GKWjKW7bNpRF7BSnKDHB_vEFhq8P9RlTJMwKk8kPLnbfxWV25Ekf0saunRDE6lnl9GdeSU5SihG_807nMGjNvpb6uGn600WN2LcCTjEN5BDoDoelST1E5HQynYi2xcGd9EFNY2iSds2YYjOGuCGNUe9mps_fXDTRHZp6j1j62J6jUtrbGqH5QyxkuMDvGQvC3ZRYX8PVIFLJK1hhDhIYB094Bl1RYvLZpbG0eRcnA74BhObfuqattf7Rb4Q39XXIoXWFWx9cFMtFrVB3VdP_2tytkaYCJ1-rByOpUI3Nb58pFbNnPYZUDmpcxSm-99be0yIwrBJjfUgJ8seL9QCezGohyvztX9VWVCqXZUEByBrv5Gg4phjdg0ZQgfqEa1YuFUQ5Xpp1nxYhbUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خودش بمبی نمیندازه ولی همه بمب ها پشت سرش می آیند !
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20404" target="_blank">📅 14:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20403">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اتاق جنگ با یاشار:جیمز باند.
قدرتمندترین هواپیمای جاسوسی تاریخ، ریوت جوینت، در حال ورود به منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20403" target="_blank">📅 14:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20402">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20402" target="_blank">📅 14:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20401">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e4766f60.mp4?token=EWFAVGsSSdIcbkLgGj63gOS4XyzW8jJQxtLPFUnEP29c-2Kgdx47bGMWQ1xmZP8AmrQWpMG6xBhWXln1YYCsy1NC_1rwtwYNT_5bpqFJzzUV_ISd5G6-0gg3PZOLpNIEZm_9X-GYFKKr9Qny5SoLsIb3K-rN0ZW01u1eI18t_IdDVCPZFM1z6KRvQZv2neSgbdyaqbwqbMM2M0foligX3IvRcGuz_s0ZXu09e8Ih48k_yGvZ03mEU_PVxTK25L91gcl-rfhVKXWTEKqJbcIG3KD9q3WwqHuxF29xWujvYYnmSNaXv-5u0hBxZbY2q3141aUUh1TVdeE5iD2M61BSFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e4766f60.mp4?token=EWFAVGsSSdIcbkLgGj63gOS4XyzW8jJQxtLPFUnEP29c-2Kgdx47bGMWQ1xmZP8AmrQWpMG6xBhWXln1YYCsy1NC_1rwtwYNT_5bpqFJzzUV_ISd5G6-0gg3PZOLpNIEZm_9X-GYFKKr9Qny5SoLsIb3K-rN0ZW01u1eI18t_IdDVCPZFM1z6KRvQZv2neSgbdyaqbwqbMM2M0foligX3IvRcGuz_s0ZXu09e8Ih48k_yGvZ03mEU_PVxTK25L91gcl-rfhVKXWTEKqJbcIG3KD9q3WwqHuxF29xWujvYYnmSNaXv-5u0hBxZbY2q3141aUUh1TVdeE5iD2M61BSFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهده دود بزرگ و غلیظ از سمت ساوه دید از قم
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20401" target="_blank">📅 13:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20400">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رسانه های رژیم : یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه بر فراز آسمان تنگه هرمز رهگیری و مورد اصابت قرار گرفت.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20400" target="_blank">📅 12:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20399">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بقایی: ‌در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد @WarRoom عراقچی هم امروز به کربلا میره و مملکت تعطیله</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20399" target="_blank">📅 11:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20398">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بقایی: ‌در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد
@WarRoom
عراقچی هم امروز به کربلا میره و مملکت تعطیله</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20398" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20397">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aaf651e2d.mp4?token=fH3HiCH3UU5PlL9quMjk2qbKwqu_8JHUgWTMlnxMXc6WVjkaS7ghrasP4EVjwhP3Lz4HxNBDvScnG21nojBah0vwCaJApNQ5L6AScPQLYeW5lNxyj6ZuYNkHumF-MmLZMdwhMcU5Cjs6kWPpIUnxbyuhvRsUQYoWX5mBunOXYVKJMnUysW5V2tjyWnnE5YpbDZDbc19qZ1YKF-V25gUaByJ-ioXDUsc9BvYN9NFypD6sbeTKiBVxlWJMdDrHq5eZsx8eFrSgQYrgtf1HEfbHsYQYfS_JiYh_NLuEBkjqZmW8O2L2xMvT2iU3Hdj4tDDm9Q8esMlvsCswQTaefe0nemszG1hkqyI5ZtYiNdYRj_uJLCOozh5xAAn_SS6sDbGhKJjwULwJl008P8_qS44Y1lSAeU84ZpInGg5MqkUWEoTcXs57yYkeL77d3bhgLr4O5SYD4E0qBjBgwjJHLgER9iOa5GyHf54e1_McyuDues6MzbVeTbEpWrgGYTpgVibZKf-d_M63xXwyjEkfokBu9H5nmce_Jgm5xeCO057tBOpDyS8BbVrWXi9yODFyVYTCbbWLXYjUdw_txVBxPGbuvYOp9fNKGzXiH-L3B4rS2nPHEwir9es_L119fbuoe6All7NmADMSXrXhRl6_kwhSYuJ5nW_vz3kOb043PmcBfts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aaf651e2d.mp4?token=fH3HiCH3UU5PlL9quMjk2qbKwqu_8JHUgWTMlnxMXc6WVjkaS7ghrasP4EVjwhP3Lz4HxNBDvScnG21nojBah0vwCaJApNQ5L6AScPQLYeW5lNxyj6ZuYNkHumF-MmLZMdwhMcU5Cjs6kWPpIUnxbyuhvRsUQYoWX5mBunOXYVKJMnUysW5V2tjyWnnE5YpbDZDbc19qZ1YKF-V25gUaByJ-ioXDUsc9BvYN9NFypD6sbeTKiBVxlWJMdDrHq5eZsx8eFrSgQYrgtf1HEfbHsYQYfS_JiYh_NLuEBkjqZmW8O2L2xMvT2iU3Hdj4tDDm9Q8esMlvsCswQTaefe0nemszG1hkqyI5ZtYiNdYRj_uJLCOozh5xAAn_SS6sDbGhKJjwULwJl008P8_qS44Y1lSAeU84ZpInGg5MqkUWEoTcXs57yYkeL77d3bhgLr4O5SYD4E0qBjBgwjJHLgER9iOa5GyHf54e1_McyuDues6MzbVeTbEpWrgGYTpgVibZKf-d_M63xXwyjEkfokBu9H5nmce_Jgm5xeCO057tBOpDyS8BbVrWXi9yODFyVYTCbbWLXYjUdw_txVBxPGbuvYOp9fNKGzXiH-L3B4rS2nPHEwir9es_L119fbuoe6All7NmADMSXrXhRl6_kwhSYuJ5nW_vz3kOb043PmcBfts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سناتور ریک اسکات: بعید می‌دانم مذاکرات با رژیم جمهوری اسلامی به نتیجه برسد
‏ریک اسکات، سناتور جمهوری‌خواه آمریکا، در گفت‌وگو با فاکس نیوز اظهار داشت که تصور نمی‌کند دور جدید مذاکرات با رژیم تروریستی جمهوری اسلامی به نتیجه برسد و معتقد است ایالات متحده در نهایت بار دیگر به حملات علیه این رژیم بازخواهد گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20397" target="_blank">📅 10:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20396">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی : ‏نیویورک پست با دو تن از رهبران میدانی انقلاب ملی شیر و‌ خورشید در داخل ایران گفت‌وگو کرده است، افرادی که با به خطر انداختن جان خود، تنها یک پیام برای جهان دارند:
‏«ما در حال آماده شدن هستیم. از خیزش دی‌ماه درس گرفتیم و مصمم‌ هستیم کاری را که آغاز کرده‌ایم، به پایان برسانیم.»
‏«ما به‌خوبی می‌دانیم با چه خطرهایی روبه‌رو هستیم، یا این رژیم می‌رود، یا ما.»
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20396" target="_blank">📅 10:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20395">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری میزان اعلام کرد که صبح امروز حکم امید بهزاد و پوریا صفوت، زندانی‌های سیاسی اجرا شد
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20395" target="_blank">📅 10:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20394">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مقام ارشد آمریکایی : هنوز به توافقی با حاکمان ایران دست نیافته‌ایم، اما تلاش‌های میانجی‌گری همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20394" target="_blank">📅 10:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20393">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">بوست کم شده داریم لول میایم پایین یه کمک کنیدد بریم بالا استیکر شاه برگرده به دوستاتون که پرکیوم دارن هم بگین
https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20393" target="_blank">📅 04:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20392">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6507572.mp4?token=FQ5OFNCNubHaESiZyiJoFgHCcab3eiEuwxNXg40ugVWrZ9Uu0s68qBtSQcGUFZmGNYbOq3bvXQsfv8WrEQWJy5MxBi3G1ygl70wR4SX2iSK4SPEqXUUCK3xD8KWMxDlNclFHfuz9pcGDUSTMPCtM_gR3u5npsWEI6bmXPXeFzXitHXo0l0J6xTL_XuCTkTDV6MGavm-mkVWgmLbiVtYMQaxToSEJyCA6n-67ZQ91KDTpBD8IakTmBFko5Z9vGgiewE28KHR5JMWo_a8C6YCVVH8VFUqxAt4r-QQKUpqTdCokLvF9LW9VxwvJIwI_JTnnBOhEQ3MpJlMKrADBYOBmzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6507572.mp4?token=FQ5OFNCNubHaESiZyiJoFgHCcab3eiEuwxNXg40ugVWrZ9Uu0s68qBtSQcGUFZmGNYbOq3bvXQsfv8WrEQWJy5MxBi3G1ygl70wR4SX2iSK4SPEqXUUCK3xD8KWMxDlNclFHfuz9pcGDUSTMPCtM_gR3u5npsWEI6bmXPXeFzXitHXo0l0J6xTL_XuCTkTDV6MGavm-mkVWgmLbiVtYMQaxToSEJyCA6n-67ZQ91KDTpBD8IakTmBFko5Z9vGgiewE28KHR5JMWo_a8C6YCVVH8VFUqxAt4r-QQKUpqTdCokLvF9LW9VxwvJIwI_JTnnBOhEQ3MpJlMKrADBYOBmzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو مارک لوین به ترامپ برای حمله به ایران پیشنهاد میده:
۱. تداوم توقیف دارایی‌های متعلق به ایران
۲. ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
۳. هدف‌گیری مستمر فرماندهان نظامی
۴. حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
۵. هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
۶. حمله به بانک‌ها و مراکز مالی
۷. دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20392" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20391">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عمویم پیت هگست
:
وزارت دفاع آمریکا آماده اجرای عملیات بود و همچنان نیز آماده است؛ در سطحی از آمادگی که از زمان جنگ جهانی دوم تاکنون نظیر آن را ندیده‌ایم. ما کاملاً آماده‌ایم و هر زمان لازم باشد، عملیات را آغاز خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20391" target="_blank">📅 03:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20390">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رویترز: زمین لرزه‌ای به بزرگی ۵.۴ ریشتر قاهره پایتخت مصر را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20390" target="_blank">📅 03:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20389">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20389" target="_blank">📅 03:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20388">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPQiruD7OFK3G2rXLYJmR6VyU61hAXTjINQoUkUl3tBVpi30ceIgHqT9oazJIWJb8wwgy7nyL5g7I7oUEaFcoXJhwr1enhAlpuIzEW245SatdOEcrPU3kMRAHjNN9MbhJ8fsQYDNSmElr8FiS0iftrAgUjA2g_D5qvPCNTyMe1aR3_Ei8qTVjb5OjLo1zBZMi3-SIHupzYPFzrtd06fv4IMPGrRNzokYlFaMJUiG-ZlJidFSQlQ61Ljw2pCUS4mVi3sJ14fBEhz107Gk4FRJ24oxKssPWge-twnsubXc2sDU-cp9rHsleWe0xk1HhDANMKEoy-TemxWYRiQs-AoG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۸۴$
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20388" target="_blank">📅 02:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20387">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ دم توالت: در حال صحبت با ایرانیم و قراره از فردا بعدازظهر گفت‌وگوهای اصلی شروع بشه. امیدواریم این مذاکرات بتونه جلوی کشته شدن آدم‌های بیشتری رو بگیره @WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20387" target="_blank">📅 02:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20386">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فعالیت‌های نظامی قابل توجهی از سوی آمریکا در عربستان سعودی و خلیج فارس مشاهده می‌شود، به طوری که یک پهپاد شیلد ای آی V-BAT در حال پرواز بر فراز تنگه هرمز و یک هواپیمای E-3G Sentry بر فراز عربستان سعودی است. @WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20386" target="_blank">📅 02:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20385">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXNeFBhtfRZyZ8auQDE_CulfcNP5HZHq8UHeHfhXWoIyAm2GMNRcUPBXiBJSP_AU2IQ7KMLv3xQGMVHzk8OpBWw6tqgFt9cS6tgyzQ8f2fKdObgru61i_4TZ1tG2rGmFgBdyGBYmcj8NWni5uCTvABldrNSVJ_O6eedpkJPl9oeOYhbPiAb5L8ullEWYvOPBdcmJI0Zu2c9pYV9ax30D3Ll__WYhsl9eY_L0pYpCAW3XZ4wUwdh6kgf_6hpuIOorGs0HNHhNKbNfUOQJjNpsCrWDdr-RpxMjsaMxIzW-W-NGU24zXc-YKZ2P5VzQ6f-McANWNd6oj_ezVHL6vPnOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ستاره شناس  https://www.instagram.com/reel/DbjVq_yxDKO/?igsh=MXgybDB5dGZ1cGVqZA==  کارای اداری و اد استوری رو انجام بدید کامنت کنید کی میزنه</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20385" target="_blank">📅 02:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20384">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پس از آنکه ترامپ تنش‌ها با ایران را کاهش داد و احتمال توافق پدیدار شد، قیمت نفت بیش از ۶ درصد کاهش یافت همکنون به
۸۶$ رسید
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20384" target="_blank">📅 02:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20383">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28b4a7f0f.mp4?token=dJprDJoN_6N5UlgJwM7To2blJDq-vu5nQUstFdvDGe6kMV5mAYfryls4-orxYAWsBthcvDGRtAeNGA3IrFpiOLEDWW_FmIHORazBDlc0UH7GnreLj9NrqqzbtgiISJBg8v5pMS8u5cvkegOmJpjsxp_xoCtu5SWOpkeNkKes3aK7EFOFSMsk92dKF43WKON1xOSSmpA_4f5xrAp0zBpQyDs-au39Dlc1VJG30xKekfxQSovOSJ0jqHvQbzcYyFo_oWiFT_Zug--kKwuYkL0hgM-MZCkJSjyWcsks47tc-kE_6vFBhfRvmwqSRR0WysSswfVQEJUqwYKZuPw3Uc94gytaN5-ku6GWlAokbRqaJnBn8uehJLuf1WaN-dQ5oO4i3LuK4puEHZYsOqTPSaqZXIyNhIEWXuomICkiBGbZCPxoIyZCl8QsCpW68pl-IRvEYXtR0fHdLX_g1_UVdLAauSLGxZrWLPpd_F_RSH7q0VufHrseJZY4XERfEPaTgYjK8OVxqYeWnSsOiiYKQd5MlS-_u8d82jeN86MaEFB6IlC419QwfZoAvxiiH9xtZ739eDbbELISmv6BP51uVFjk6pbBTNZ7IGbtKYonFrRy_9z9Tpi8HRTR3kse1mjeL1UNEKfsbHHf1aGXNOBiHWbbaTuFt0Q41qCB59Z29nHaSgY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28b4a7f0f.mp4?token=dJprDJoN_6N5UlgJwM7To2blJDq-vu5nQUstFdvDGe6kMV5mAYfryls4-orxYAWsBthcvDGRtAeNGA3IrFpiOLEDWW_FmIHORazBDlc0UH7GnreLj9NrqqzbtgiISJBg8v5pMS8u5cvkegOmJpjsxp_xoCtu5SWOpkeNkKes3aK7EFOFSMsk92dKF43WKON1xOSSmpA_4f5xrAp0zBpQyDs-au39Dlc1VJG30xKekfxQSovOSJ0jqHvQbzcYyFo_oWiFT_Zug--kKwuYkL0hgM-MZCkJSjyWcsks47tc-kE_6vFBhfRvmwqSRR0WysSswfVQEJUqwYKZuPw3Uc94gytaN5-ku6GWlAokbRqaJnBn8uehJLuf1WaN-dQ5oO4i3LuK4puEHZYsOqTPSaqZXIyNhIEWXuomICkiBGbZCPxoIyZCl8QsCpW68pl-IRvEYXtR0fHdLX_g1_UVdLAauSLGxZrWLPpd_F_RSH7q0VufHrseJZY4XERfEPaTgYjK8OVxqYeWnSsOiiYKQd5MlS-_u8d82jeN86MaEFB6IlC419QwfZoAvxiiH9xtZ739eDbbELISmv6BP51uVFjk6pbBTNZ7IGbtKYonFrRy_9z9Tpi8HRTR3kse1mjeL1UNEKfsbHHf1aGXNOBiHWbbaTuFt0Q41qCB59Z29nHaSgY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من واقعاً دوست دارم این مسیر نتیجه بدهد؛ چون جان افراد زیادی را نجات می‌دهد و از ویرانی و نابودی گسترده جلوگیری می‌کند. صادقانه بگویم، اگر آن اتفاق می‌افتاد، سال‌های بسیار طولانی طول می‌کشید تا بتوانند خسارت‌ها را جبران کنند؛ اگر اصلاً امکان بازسازی وجود داشته باشد. حتی فکر نمی‌کنم بتوانند دوباره آن را بسازند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20383" target="_blank">📅 02:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20382">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">صدای انفجار جدید همین الان در تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20382" target="_blank">📅 01:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20381">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ-fcxD14m9FvtUo7oWpSm8yJTuI361ZC6c51dHii-Y-1vF32gQMXeiBqVxM1pasvsQI05fW9c6rdYd3ls6sLm1IUnTg7G_m6nuVHeyVbj5KyGH6JG5afFo2fuK1mU03JlzLoCxLDHgj6jtxNweOlboKWwi0I8ITUePswXkWOozU8Dmi8hEqg9OcevANb9zYvItZt8B-JfSCnIIxfUEdHfxU71Tg1pYSzx5wp3nEZKvK4O_ziGk11PymnHS6-A_2PMk-lnjO29SsdwgzPhnKj5tUWVglseZy0rZQfAlNBs-c8-3wq9I-9BaDqwRc2jEz6i_Z9z8wWru90kYonD0Wsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا: گزارشی دریافت کردیم مبنی بر وقوع حادثه‌ای دریایی در فاصله 20 مایلی شمال شرقی شهر خصب در عمان. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20381" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20380">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سازمان دریایی بریتانیا: گزارشی دریافت کردیم مبنی بر وقوع حادثه‌ای دریایی در فاصله 20 مایلی شمال شرقی شهر خصب در عمان.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20380" target="_blank">📅 01:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20379">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ درباره ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست. آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20379" target="_blank">📅 01:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20378">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرنگار : شما نمی‌دانید این حملات به کجا منتهی می‌شود. منظورم این است که آیا همسایگان ایران با سیل جمعیتی که به کشورهایشان سرازیر می‌شوند، مواجه خواهند شد؟
ترامپ : یک فاجعه. اتفاقات بد زیادی ممکن است رخ دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20378" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20377">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ در مورد ایران دم توالت:
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20377" target="_blank">📅 01:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20376">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: ببینیم که آیا می‌توانیم به توافقی برای خلع سلاح هسته‌ای ایران برسیم یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20376" target="_blank">📅 01:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20375">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ دم توالت:
در حال صحبت با ایرانیم و قراره از فردا بعدازظهر گفت‌وگوهای اصلی شروع بشه.
امیدواریم این مذاکرات بتونه جلوی کشته شدن آدم‌های بیشتری رو بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20375" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20374">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایگان آنها هم همین را گفتند. ما فقط فعلا می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20374" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20373">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرنگار: گزارشی وجود دارد که نشان می‌دهد شما در حال عقب‌نشینی نیروهای آمریکایی از کویت و بحرین هستید.
ترامپ: تمایلی به اظهار نظر در این مورد ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20373" target="_blank">📅 01:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20372">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرنگار: آیا ایران برای رسیدن به توافق، ضرب‌الاجلی تعیین کرده است؟
ترامپ: خواهیم دید. من قصد ندارم به کسی آسیب برسانم.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20372" target="_blank">📅 01:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20371">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ درباره ایران دم توالت هواپیما:
گروهی از افراد هستند که امیدوارند من این کار را انجام دهم - به عبارت دیگر، بمباران کنم - و گروه دیگری از افراد هستند که نمی‌خواهند من این کار را انجام دهم.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20371" target="_blank">📅 01:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتاق جنگ با یاشار : ستاره شناس  https://www.instagram.com/reel/DbjVq_yxDKO/?igsh=MXgybDB5dGZ1cGVqZA==  کارای اداری و اد استوری رو انجام بدید کامنت کنید کی میزنه</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20369" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20368">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaIUSTUa1zkq23qlzf_oWvhg9-cTznjGmewrtqqEHaf-4uXAf4DNZVgtuC52Kqlz8E85AM3fEKSf1MOxRPPgt-Z9HCp3EsKDqOmY5BcqmevmaxOPXNpsR19Jbub5WHAnJodJ5ePqOJFlIk_Icdt_4uA4PJu8ltZ6K7Z9_JtDJJY-QBav4oSJhHnJmYFvC-XunDiwwONdiL6TWW7xWzqkchk16yQskeiwOQsW7K1enDSqUkFdEA_zq_FiTRSfcuvffVOB0OoQEctkPo305PFA8cmj9uFQB4UsMLxUZPVMDjHk6QwV8buMjbdKi5-wChTMoeXxjKfyCSI32V1oQ6MppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ستاره شناس
https://www.instagram.com/reel/DbjVq_yxDKO/?igsh=MXgybDB5dGZ1cGVqZA==
کارای اداری و اد استوری رو انجام بدید
کامنت کنید کی میزنه</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20368" target="_blank">📅 00:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تنگه صدا میاد
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20367" target="_blank">📅 23:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">استوری ۱۸ بهمن ۱۴۰۴ اتاق جنگ با یاشار
۲۱ روز قبل از جنگ ۴۰ روزه !!!
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20366" target="_blank">📅 23:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کانال ۱۲ عبری : مقامات اسرائیلی تخمین می‌زنند که ترامپ دوباره موضع خود در قبال ایران را تغییر می دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20365" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منابع اسرائیلی به i24NEWS گفتند: «حمله نظامی آمریکا به ایران هنوز روی میز است و لغو نشده»
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20364" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مقام آمریکایی به تایمز اسرائیل: قرار بود اسرائیل بخشی از حمله به ایران باشد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20363" target="_blank">📅 22:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20362">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تیپ ۳۲۸ مریوان : ساعت ۳ بامداد امروز، گروه کورد پژاک با دو فروند ریزپرنده انتحاری و شلیک راکت آرپی‌جی به یکی از مقرهای ارتش در مرز حمله کرد
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20362" target="_blank">📅 22:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20361">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانال ۱۴ : انفجاری در اردوگاه تایجی نیروهای آمریکایی-ناتو در نزدیکی بغداد رخ داده است. این انفجار احتمالاً ناشی از افزایش سریع دمای تابستان و انفجار مهمات ذخیره شده بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20361" target="_blank">📅 21:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20360">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانال ۱۲ عبری از قول منابعی در دستگاه امنیتی درباره لغو حمله آمریکا به ایران: "ما برای چند ساعت در یک وضعیت واقعی از عدم قطعیت قرار داشتیم. رئیس‌جمهور ترامپ ما را در ابهام نگه داشت. حس ما این بود که ما را نادیده گرفته‌اند."
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20360" target="_blank">📅 21:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20359">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کان، شبکه خبری عبری:
مقامات اسرائیلی از نارضایتی خود ابراز کردند، چرا که دونالد ترامپ، رئیس‌جمهور آمریکا، برای بار دوم در یک هفته، یک عملیات نظامی برنامه‌ریزی‌شده علیه ایران را لغو کرد. آن‌ها اشاره کردند که این عقب‌نشینی‌های ناگهانی، برنامه‌ریزی‌های نظامی را تضعیف می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20359" target="_blank">📅 21:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20358">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU4P5lQoPADW7_7vNKYF0p5f7O3gLSMW7sG_RGwidS5P2_Yhh_fWsc4m8ysFB5pHk5vUdQIZvMbfgVGy7HTz2S6FS9qB_LIRjz-NOlYtnyFqa3OPkoeLINN-87CAi1nHh37zbggfvQb2rgxrTaY5jQQb2SBR1Rq1MBAK2WL2nAE5GlLODa5fVZv5bUm9W7FqSOGS_bEmhi8OT48-6v53y2DlRt1gV5RWTPh3-KXamP1ySpsZ-MGZhQuZVdhq08mG9CbbNi1EvXnagzuXUQjB0tX8jzBdoOSuGkTpZzU14QNA7VA397v5QNaBbXZg2hV1LYHa8l8fLWNFHJ7UFqI3eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره Sentinel-2 نشان میدهد ناو هواپیمابر آمریکای لینکلن یا بوش به 200 کیلومتری چابهار رسیده و این فاصله همچنان در حال کم شدن است....
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20358" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20357">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZADZsj7jfSbUdshV_EGr5ie7LfFuifUdLr4RcF673MZ9jtjhemwyt6sRvkfPNeZSlcCNzTGJWrTUJiWWraizNc7c5pR3WZ4UyGsKF-b8q9KgR5Xsy9hhenCIfZvULD3Oz63bkd6WLwk14x4zD4Mfhqu-sqBbW-o6hjXUJgum8JECQaAF3ExyhQ85QYReuj47BGXy65BHUxe3NNvEA-aqJGwmFenXz2gPaoiiW9lqYRHFrYwPw-VjEtubJUec1oZUyNIRJ9CkBypV4TlDZWemlMrR2SOBvuTAWrmlxU8iMmWXHktNaX9MjUnFe4OA4HmpIDonBZDHXwjpx6iKsoRykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش در تنگه هرمز مورد اصابت موشک قرار گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20357" target="_blank">📅 20:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20356">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش پرتاب موشک از باغین کرمان @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20356" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKNrAONOx2TnDSld2ZNs6ewSpG1P-Upt6cdwuZZ0v6ypdHzabdLQz_oTznvo2-Tg8NRjSj5q9oJP-TG-wWr16SAjPxJ0QV4EL9Z4vDGbIdlps5_3NsNCMwY2q28GFtK6xwlGLOpoAF7YcmZf4ig0bS5KkS8_j8mIdjAhd7wnpPxPjSoe2vVvE8T42JB9fVt4vLedmxaFYqzVHJBvs4z90G9h4BEMapAJJ87wJMNqBZc_NWZD7Y1MtXQrEHP2jgN3jGEZ4YRuiw4YaUtd32c-DjcCtUEHrIeXKPq7nzPvrj7EehF4Z53Bj8hPV-ALExbPunzc4FqdXpO3jkFFiP_MLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CopKJAuGYUh01mgCz0vaE16Y0oFL5YcFBE5MHj0fJEqWVc67KHUPg8_nAyDw_1pPu5PY4i-gwVZR2k4iAYcxjPn2mYaR9drguRJxdeLpHbWIQuDqx-D08xmUGDwrcwv4Z-ZDA8AElDll6rbOm_vtxsGz9k9-yQ4idc1rBrt0I5tuuTbGv2C5CepTmyvWcAk_Sed710SwfGMt54vx-ZVGIo_2TzJ7N70xMSvbmX3V7Je6wLXdcnTZ5cYB3pWBeuQcCeQBECkL3oK3cCEZw7tFMhF_hwJx3CelTwD1-aOeJHui5LSxip6GVNEViUZscUe4JvePfXvfuvqoyTWOnCVcXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جابجایی راکت انداز گراد در حوالی اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20354" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وال استریت ژورنال: ترامپ اگر فورا پیشرفتی در مذاکرات و توافق نبینه، میتونه هر لحظه عملیات علیه ایران رو آغاز کنه!
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20353" target="_blank">📅 19:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش پرتاب موشک از باغین کرمان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20352" target="_blank">📅 19:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20351">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92517c853f.mp4?token=GXVOnvEgV1fDngLLKFR2UisfZgBT0z9_s1Dl93pkpnki-JjJVUey1PQlqwCPgmLRj85vESRjpO9rUfM2eH8JeoIrZIgDhWSiI9i3P-b3HyJTi9cAJwVWes8DT37N9n7asC8r263fcIXJRgC1lqMbSy8dHclQB2aDGlXIvw4cCcKVMauoKfvDi3qLePazyuI6jdkkf7cnG-VFcN1MB5ZSkrIekAU8Y7kNN81z0v4h5g88g61rxw4TuL7-1qpUTHTFi_8MPli65mssS9bBmc2KaKLXQoYf35G1cPvli33m3Z2YJfb-Y3HBgW3lVaMvox4bGdH4eoqLB5MfD2g8GM0d6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92517c853f.mp4?token=GXVOnvEgV1fDngLLKFR2UisfZgBT0z9_s1Dl93pkpnki-JjJVUey1PQlqwCPgmLRj85vESRjpO9rUfM2eH8JeoIrZIgDhWSiI9i3P-b3HyJTi9cAJwVWes8DT37N9n7asC8r263fcIXJRgC1lqMbSy8dHclQB2aDGlXIvw4cCcKVMauoKfvDi3qLePazyuI6jdkkf7cnG-VFcN1MB5ZSkrIekAU8Y7kNN81z0v4h5g88g61rxw4TuL7-1qpUTHTFi_8MPli65mssS9bBmc2KaKLXQoYf35G1cPvli33m3Z2YJfb-Y3HBgW3lVaMvox4bGdH4eoqLB5MfD2g8GM0d6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : یک جت جنگنده رادارگریز F-35C متعلق به نیروی دریایی ایالات متحده، از ناو هواپیمابر آبراهام لینکلن (CVN 72) در حالی که این ناو هواپیمابر از دریای عرب عبور می‌کند و از محاصره ایالات متحده علیه ایران پشتیبانی می‌کند، به پرواز درآمد. تا تاریخ ۲ آگوست، سنتکام ۳۵ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی دیگر را توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20351" target="_blank">📅 18:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20350">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏وال استریت جورنال: یک مقام ارشد خلیج فارس گفت که برخی از کشورهایمان بر ترامپ فشار وارد می‌کنند تا اقدامات بیشتری علیه ایران انجام دهد. این مقام افزود که ایران تا زمانی که ایالات متحده اقدامات تهاجمی انجام ندهد، مانند کنترل تنگه هرمز و بررسی عملیات زمینی، کوتاه نخواهد آمد.‏
کشورهای خلیج فارس از فقدان یک استراتژی مشخص از سوی ایالات متحده ابراز نارضایتی کرده‌اند. به همین دلیل، متحدان خلیجی خواستار موشک‌های پدافندی بیشتر و تضمین‌هایی از سوی ایالات متحده برای محافظت از کشورهای خلیج فارس در صورت ادامه درگیری‌ها شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20350" target="_blank">📅 18:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20349">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۲ : مقامات اسرائیل خودشونم از پست تروث سوشال پرزیدنت ترامپ متوجه لغو عملیات شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20349" target="_blank">📅 18:41 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

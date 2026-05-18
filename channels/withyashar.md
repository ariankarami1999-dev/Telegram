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
<img src="https://cdn4.telesco.pe/file/b1otcCp1sULTBo2-csJQRVs_GMm3wWBWqbddtmCZsf9fKA3byITnSqeNaqSt_dVSqe3dw4_d3uEVueh1EJVI_dlDySM_hLuFxnT7V-HCpF6gvYKIDcO_3en9w2Sr1fcuLHAk07NcaoEEMfBFfQX5B-XovXrBDx-19V3SeMUYQGf0uD3ZXVzYo8Hpk1nRIXRluUiiA2Jlf_UTFsLj24qdsGfQtDZZTGFD_6QFAPkN9yzkEAuoT77K5cciUupzqFdC81Wqub7s_rcM-Ym_i2wn1hz9TLDWmmP_agEVIbk7RubWB5kmLurv8pWxMoFeqN_TdBucgczYnzMgtxYWHpD-EA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 263K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 20:13:28</div>
<hr>

<div class="tg-post" id="msg-11559">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">منابع «العربیه»:
وزیر کشور پاکستان بعد از آخرین تلاش‌هایش، تهران را ترک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/withyashar/11559" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11558">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تری یینگست، خبرنگار فاکس نیوز‌ :  ما تو آستانه بازگشت به عملیات‌های رزمی تمام‌عیار هستیم
@withyashar</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/withyashar/11558" target="_blank">📅 20:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11557">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه های عبری:
ترامپ‌ امشب دستور بمباران را صادر میکند
@withyashar</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/withyashar/11557" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11556">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
رویترز:
آمریکا پیشنهاد جدید ایران را رد کرد
@withyashar</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/11556" target="_blank">📅 18:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11555">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0kzSmTMnshZ71IoZqu6mawaZfLXPcLitDeGjvt3vddfktofvO0WlzCBRSj73bPF3iy3zx5lvLWk65ZMtH7oAQaPHKLmFjL6ET_E9-LswoDwOqZPDbvGp0nE83dnc_E2G57yqEB0mhoU-dYyZI6mmGIw55Rv2UalWftLpiTN3rqv-BIExsaPDVMyjH99BY2iv2uGWEBo9qIcrYVfWX9LTebaztBVuIJeycxiACEAD2a92SPev-EOdnG4MDNiE-24tiWmhPjz7UyLJb_Dz0nPvYu8iArIwnqlL0K_sj8V5tUB81eoFIbroM3swelNnFH23287PyyxPl_2kiORlKuORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی‌ آقا عشقه ، چقدر راحت و خاکی‌ کانکت شدیم…  بد یه عده … چی بگم… درست میشه اونم … در آخر هر چیزی فقط‌ مردمن که مهم هستند
🙌🏾
❤️‍🩹
@withyashar</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/withyashar/11555" target="_blank">📅 18:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11554">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کمی‌پیش ستون عظیم دود از جنوب تهران، دوربین به سمت : بزرگراه یادگار عمام، جنوب @withyashar</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/withyashar/11554" target="_blank">📅 18:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11553">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxD3v9iX_jip-ad_i4Y5Vc1HjrY4lais2ph_qLfRjeNFwIoXTyVJlbHoLw7-kCsrD4qDR_bFYf7mw1ZDz3s4gyrvImTWVlwmyaOzo3r3_rZhpVYEYdnx6c6b_CiR776pJMpBnPP9t5wD2oJ39cEEFr4x--Cs3RE-qWdhZTQvPvWZuK2JMEDukqhQjC5m-_QBGB-Ag42lVqUe55u0y6Uno8KDTOkU7aoO32qhHpRHQBB3chO22OFfE1V4mYzg3zLrZ6t9x9NUAuriyUJJeymRazw-1j9f6OPiuXMBN64xrOgoaHIrxe-moL6v9ftLVpVdmECxOFxVTFjB7C6328DC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی‌پیش ستون عظیم دود از جنوب تهران، دوربین به سمت : بزرگراه یادگار عمام، جنوب
@withyashar</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/withyashar/11553" target="_blank">📅 18:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11552">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تسنیم به نقل از منبعی نزدیک به تیم مذاکره‌کننده ایران:
ایران بر لزوم پرداخت غرامت از سوی آمریکا به دلیل جنگ، اصرار جدی دارد.
واشنگتن باید درک کند که پایان دادن به جنگ، در ازای تعهدات هسته‌ای نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/11552" target="_blank">📅 18:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11551">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V460bf58qg3TgZR8VylV-YBD3J0acX_yyPYDGmSJV9p4vwD9F2lk7XjNtHqs3mWN9rD0sQT3zlVw6oHwGFt8NeUETSXW9PPCKC1QHNKtGmFfQ2gEb1sdrmyoO83VmzW7JGTtgGYUfALacRTQW9_6wGLqOTOn0VuHknyDmgfYVI3Es9YZqg4q-OL9T2h_1piE7IdeY5dEq8Qb6bXtOXaQxzrk3NziGpLWG4jQgc6J7bqUvQxN2DAHIPfv6Pk0_6pE-3FnYtvYiaCmxJhNARax4JHbmqHLLgwi8reAoMsXlds1UtebrHLxVtc5XkBHZKw2dxh64zaIjZJtsOJxcw8TjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : اگر ایران تسلیم شود، بپذیرد که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده است، و نیروی هوایی‌اش دیگر همراه ما نیست، و اگر تمام ارتش آن از تهران خارج شود در حالی که سلاح‌ها را زمین گذاشته و دست‌ها را بالا برده‌اند و هر کدام فریاد می‌زنند «تسلیم می‌شوم، تسلیم می‌شوم» و با شتاب پرچم سفید را تکان می‌دهند، و اگر تمام رهبری باقی‌مانده آن همه اسناد لازمِ تسلیم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده آمریکا بپذیرند، آنگاه نیویورک تایمزِ شکست‌خورده، وال‌استریت ژورنال چین (وال‌استریت ژورنال!)، سی‌ان‌ان فاسد و اکنون بی‌اعتبار، و همه اعضای دیگر رسانه‌های جعلی، تیتر خواهند زد که ایران پیروزی‌ای استادانه و درخشان بر ایالات متحده آمریکا به دست آورده است؛ در حالی که اصلاً رقابت نزدیک هم نبوده است.
دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها کاملاً دیوانه شده‌اند!!!
@withyashar</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/withyashar/11551" target="_blank">📅 18:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11550">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کانال ۱۳ تلویزیون اسرائیل: نتانیاهو برای دومین بار در ۲۴ ساعت گذشته با کابینه امنیتی تشکیل جلسه داد
@withyashar</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/11550" target="_blank">📅 18:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11549">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رئیس‌جمهور کوبا: هر حمله نظامی به کوبا به حمام خون و عواقب غیرقابل پیش‌بینی منجر می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/withyashar/11549" target="_blank">📅 18:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11548">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کی‌یر استارمر : من قصد ندارم کنار بکشم، باید به مردمی که به من رای دادند خدمت کنم!
@withyashar</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/11548" target="_blank">📅 17:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11547">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبر بد برای گیمرها
رضا احمدی، معاون نظارت بنیاد ملی بازی‌های رایانه‌ای:
طرحی برای سایتهای دانلود بازیهای کامپیوتری به تصویب رسیده که طبق اون، یک گیم سنتر مرکزی تشکیل میشه تا سایتهای دانلود بازی قبل اینکه لینک دانلود رو آپلود کنن باید اون لینکا رو به اون گیم سنتر ارسال کنن تا یه کمیته محتواش رو بررسی کنه و اگه تایید شد، اون سایت تازه اجازه داره لینکای دانلود رو برای گیمرها آپلود کنه!
@withyashar</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/11547" target="_blank">📅 15:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11546">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آمریکا در متن جدید خود اسقاط تحریم‌های نفتی ایران را پذیرفته است
تسنیم : یک منبع نزدیک به تیم مذاکره‌کننده گفت که آمریکایی‌ها برخلاف متون پیشین خود، در متن جدید پذیرفته‌اند که در طول دوره مذاکره، تحریم‌های نفتی ایران را Wave کنند.
ایران تاکید دارد که لغو همه‌ی تحریم‌های ایران باید جزو تعهدات آمریکا باشد. آمریکا اما اسقاطی(OFAC) را تا زمان تفاهم نهایی مطرح کرده است.
اسقاط تحریم‌ها WAVE یعنی تحریم‌ها موقتاً یا عملاً اجرا نشوند اما به معنی حذف دائمی نیست
او‌فک (OFAC)مخفف:
Office of Foreign Assets Control
این یک نهاد در وزارت خزانه‌داری آمریکا است. کارش اجرای تحریم‌ها علیه کشورها، شرکت‌ها و افراد هست، به عبارتی کنترل اینکه چه کسی می‌تواند با چه کسی تجارت کند
@withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/11546" target="_blank">📅 15:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11545">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5887773253.mp4?token=mjbvzSj7QvjIaWPKVKpKD1dSBMEAHkbr3UaV04mRmma2vEJUU93rx7TYcg17PmW44ZuIyAPFHHuTjq094mw6JJyVMsUb2b3pVCP5y6cEaLh2DbxtoepO_luHKGBAFOLxkIOaMgYsbVanLd05gJiTc5PcukkS8_aOb_z2luwBFk7ir8LDnTigS_lcOr3C1x9rd_cm4KFxTTQiCz4gP_iaQkLRRN7lBuH7ws2c9aLNPNu0j_m5M_Q2K0PAuhnLx8uaMxL0FA8ptEfGWzG5crWNmmMZIZeH9wb3rFcvU_d93qYgDlURVIPcR8M9-qcNCaUAIgRs2Lj5YW6gUmZTGt4jYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5887773253.mp4?token=mjbvzSj7QvjIaWPKVKpKD1dSBMEAHkbr3UaV04mRmma2vEJUU93rx7TYcg17PmW44ZuIyAPFHHuTjq094mw6JJyVMsUb2b3pVCP5y6cEaLh2DbxtoepO_luHKGBAFOLxkIOaMgYsbVanLd05gJiTc5PcukkS8_aOb_z2luwBFk7ir8LDnTigS_lcOr3C1x9rd_cm4KFxTTQiCz4gP_iaQkLRRN7lBuH7ws2c9aLNPNu0j_m5M_Q2K0PAuhnLx8uaMxL0FA8ptEfGWzG5crWNmmMZIZeH9wb3rFcvU_d93qYgDlURVIPcR8M9-qcNCaUAIgRs2Lj5YW6gUmZTGt4jYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: آیا ارزش از دست دادن انتخابات میان دوره‌ای را دارد اگر نتیجه یک ایران غیر هسته‌ای باشد؟
سناتور گراهام: ارزش از دست دادن شغلم رو هم داره؛ اگر مجبور بودم کارم رو رها کنم تا مطمئن شم ایران هرگز سلاح هسته‌ای نخواهد داشت، این کار رو می‌کردم.‌‌
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/11545" target="_blank">📅 14:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11544">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتاق جنگ با یاشار : تا آغاز جام جهانی ۲۰۲۶ در تاریخ ۲۱ خرداد ۱۴۰۵، حدود ۲۴ روز مانده است. و تا فینال جام جهانی در تاریخ ۲۸ تیر ۱۴۰۵، دقیق ۲ ماه مانده است
عید قربان امسال در بیشتر کشورهای منطقه، روز چهارشنبه ۶ خرداد ۱۴۰۵ (۲۷ مه ۲۰۲۶) اعلام شده است.
بازارهای مالی (بورس‌ها) در ایام عید قربان روز تعطیل می‌شوند (حدود ۵ روز)
حدود ۹ روز تا عید قربان مانده است ، حساب دستتون باشه
@withyashar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/11544" target="_blank">📅 14:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11543">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPawLu3TZKCPt2Q2jmXjTQYUj7hEQ0144OszkSs5LYcS7AF2mDgc75MzLeXStvhsMhyU9HeQdxfUxJQXylE7kSBjkJydJcfKRdEEyDMNd98Ok0MZwjQ-eRA9fgLW3hD1GEQVNiPiqxPTj-BOEIxRcB9DVV5PyRLluBMxPbX5nqNKU10TA-SLLt4ZrVNCBLZUxY0B2b99BFT6JlGfcCKt92ZFNk4H0NNWKzZeGxxs8Q14iW2XlEHEV0v0FwiZlmX3QttEA3N4ZKZMrXHYkIH1JY758yl99MObz5Te3JkH7Gazuk8Y3BcCJM7AbJ3BkCGiaqRyeMenEmOeEbp4vioryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش هندی‌مکس PEGASUS (9276028) که با پرچم روسیه و تحت تحریم ایالات متحده حرکت می‌کند، صرفاً از روی لجاجت، مدام به محدوده محاصره ایالات متحده رفت و آمد می‌کند. ما چندین تصویر ماهواره‌ای داریم که تأیید می‌کند این یک جعل سیستم اطلاعات ناوبری (AIS) نیست.
فردا ولادمیر پوتین برای دیدار با شی جین پینگ در‌یک سفر از پیش برنامه ریزی نشده به چین سفر میکند…
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/11543" target="_blank">📅 13:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11542">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31cff4050.mp4?token=jnEGmcMglsELF-PThZMmh1_7w4sq-M_SqXqwJYpcacivI04xpXlL87G4NNUx0pGzCHYmh9mcRECd3OuA58_XNL48cHbt--UyHlHMVQyBFg-e-gAog7XLq65uFGnOT8thu_O_q_3_B7bWBWGw7Qw6Cp-2yDITAo8eTY1haIL8TAvpatUi3D8H-mCsy_rS6p7yAIn-MI3VdKIAyEzaf5zdpv3MqxEFpWoq7TInYL_x1fTro6C2y1zJDQGWjZeVu1R89HbwefSUbNI1nVyHR_pKsLtcDDpoCvEx5PdruD8PamhqWicwXyMGXBOkC9lBRE0OOiYFeDx30QpHRXYzDetsuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31cff4050.mp4?token=jnEGmcMglsELF-PThZMmh1_7w4sq-M_SqXqwJYpcacivI04xpXlL87G4NNUx0pGzCHYmh9mcRECd3OuA58_XNL48cHbt--UyHlHMVQyBFg-e-gAog7XLq65uFGnOT8thu_O_q_3_B7bWBWGw7Qw6Cp-2yDITAo8eTY1haIL8TAvpatUi3D8H-mCsy_rS6p7yAIn-MI3VdKIAyEzaf5zdpv3MqxEFpWoq7TInYL_x1fTro6C2y1zJDQGWjZeVu1R89HbwefSUbNI1nVyHR_pKsLtcDDpoCvEx5PdruD8PamhqWicwXyMGXBOkC9lBRE0OOiYFeDx30QpHRXYzDetsuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای ویژه دریایی شایتت ۱۳ اسرائیل سوار بر یک کشتی حامل فعالان حامی حماس، در آب‌های بین‌المللی مشاهده شدند. این تصاویر در حالی منتشر شده که اسرائیل همزمان با حرکت یک ناوگان دریایی به نام «Global Sumud Flotilla» از ترکیه به سمت غزه که طرفداران فلستین هستند، سطح آمادگی نیروی دریایی خود را افزایش داد.
@withyashar</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11542" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">زرشکیان :  نباید به دروغ ادعا کنیم که هیچ مشکلی نداریم و دشمن در حال نابودی است! ما با چالش‌های جدی مواجهیم!
مسئولان ادعا نکنند ما در شکوفایی مطلق هستیم و دشمن در حال نابودی است!
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11541" target="_blank">📅 13:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11540">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LX03DJCD8SfEKZ17mVksCOZ4B06wMi_fCWTGdXjBZKPcMrFJzFNlTq21ofGVq1rLv-kgMaXjTLFYa6PXsRLgVAyz99GuOQy1s-oY6P6UND4e3wbZIIGl97xMSEQn6IvGMVgqitCOF2ifBSfwlRZm4B0VE2bGqFCrpb11d5W-M_9wqBUsZIUAlaIbYM1yGsCAb1IQyIZYBfYPTp1BizJzy7rm5G3yNrZUeaw1EOHo_o36gv67UcbVBtVB7-kOJ114zryLvK_BF2BhFTozaMbzzFFg59OWT8bJIAPJV9JShezqsTtZBsZIySoCEGZ8RArsREpNKvwBE9CaKJNgkc72Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره ای بلومبرگ:
حدود 23 نفتکش در نزدیکی جزیره خارک مشاهده شدند که بزرگترین تجمع از زمان آغاز محاصره آمریکاست
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11540" target="_blank">📅 13:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11539">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سی‌ان‌ان:
پنتاگون فهرستی از اهداف برای حمله به ایران در صورت صدور دستور ترامپ آماده کرده است
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11539" target="_blank">📅 13:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11538">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گسترش آلودگی نفتی ایران به سواحل کویت؛ زنگ خطر فاجعه در خلیج فارس؛بر اساس تصاویر منتشر شده در شبکه‌های اجتماعی، تداوم نشت نفت از زیرساخت‌های ایران، اکنون با عبور از مرزهای آبی، به سواحل کویت رسیده
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/11538" target="_blank">📅 13:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11537">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: اونا یه برگه می‌فرستن که هیچ ربطی به چیزی که توافق کرده بودیم نداره  منم می‌گم، شماها دیوونه‌اید یا چی؟ @withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/11537" target="_blank">📅 12:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11536">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ:
اونا یه برگه می‌فرستن که هیچ ربطی به چیزی که توافق کرده بودیم نداره
منم می‌گم، شماها دیوونه‌اید یا چی؟
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/11536" target="_blank">📅 12:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11535">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وای نت عبری از قول منبع پاکستانی: «ما پیشنهاد اصلاح‌شده ایران را به آمریکا ارسال کرده‌ایم، وقت زیادی نداریم»
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/11535" target="_blank">📅 12:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11534">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجار سنگین در بیت شمش اسرائیل و دیده شدن ابر قارچی گزارش شده که در کارخانه شرکت تومر رخ داد. این شرکت موتورهای موشک سنگین و سبک، از جمله موتورهای پیشران موشک‌های ارو ۲ و ارو ۳، موتور موشک هدف سیلور انکر، موتورهای ماهواره هورایزن و موتورهای موشک باراک ۸ و…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/11534" target="_blank">📅 12:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11533">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی وزارت خارجه:
هفته گذشته علی‌رغم اینکه طرف‌های آمریکایی به‌طور علنی اعلام کردند طرح ایران مردود است،
ما از طرف میانجی پاکستانی مجموعه‌ای از نکات و ملاحظات اصلاحی را دریافت کردیم.
بنابراین از روز بعد از ارسال نقطه‌نظرات ما به طرف آمریکایی، از طرف پاکستان مجموعه‌ای از پیشنهادات را دریافت کردیم
که در این چند روز بررسی شد و
هم‌چنان که دیروز اعلام شد، متقابلا نقطه‌نظرات ما به طرف آمریکایی منعکس شده است.
روند مذاکرات از طریق میانجی پاکستانی ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11533" target="_blank">📅 11:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11532">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سخنگوی سنتکام به شبکه العربیة
:ما به اهداف نظامی که برای خود در ایران تعیین کرده بودیم، دست یافته‌ایم
ما تا حد زیادی توانایی‌های نظامی ایران را نابود کرده‌ایم.
ما ظرفیت تولید نظامی ایران را نابود کرده‌ایم.
با متحدان خود برای پشتیبانی از پدافند هوایی همکاری کردیم.
توانایی ایران برای تهدید دیگر مانند گذشته نیست.
عملیات علیه ایران بسیار مؤثر بود.
ما به دلیل استفاده از تنگه هرمز به عنوان سلاحی برای تهدید آزادی دریانوردی، ایران را محاصره می‌کنیم.
برای هرگونه طرح احتمالی که ممکن است از ما درخواست شود، آماده‌ایم.
در طول آتش‌بس با ایران، تجدید تسلیحات و استقرار مجدد نیرو داشته‌ایم.
تهدیدات ایران مانع عبور کشتی‌ها از تنگه هرمز می‌شود.
تحریم ایران بسیار مؤثر است و ما به اجرای آن ادامه می‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/11532" target="_blank">📅 10:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11531">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شب گذشته راننده یک خودروی شوتی با هدف فرار از دست نیروهای پلیس اقدام به ریختن میخ‌های چندپر در مسیر اتوبان تهران–کرج کرد که موجب آسیب‌دیدگی لاستیک‌های ۲۴ دستگاه خودرو و مسدود شدن آزادراه تا صبح امروز شد
پلیس اعلام کرده که با استفاده از دوربین های جاده ای خودروی شوتی شناسایی شده و راننده آن تحت تعقیب است
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/11531" target="_blank">📅 10:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11530">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">طبق روال هر روز اسرائیل جنوب لبنان را شخم میزند.
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/11530" target="_blank">📅 10:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11529">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یک کارشناس صدا و سیما تهدید کرد:
با یک انفجار در فضا می‌توان خدمات اینترنت ماهواره‌ای استارلینک را از کار انداخت
@withyashar</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/11529" target="_blank">📅 10:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11528">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏شاهزاده رضا پهلوی: «برای انجام نقش خودم به بهترین نحو، باید کاملا موضع فراجناحی و بی‌طرف داشته باشم. نه به نفع پادشاهی و نه به نفع جمهوری؛ به نفع دموکراسی!»
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/11528" target="_blank">📅 07:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11527">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پست جدید ترامپ در تروث مبنی بر فشار یا حمله همه جانبه به ایران @withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/11527" target="_blank">📅 06:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11526">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حسین دهباشی سازنده کلیپ تبلیغاتی حسن روحانی سال ۱۳۹۶ در پست عجیبی نوشت : حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/11526" target="_blank">📅 06:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11525">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سی‌ان‌ان به نقل از منابع آگاه:
ترامپ به‌طور فزاینده‌ای از روند مذاکرات با جمهوری اسلامی و ادامه بسته بودن تنگه هرمز ناراضی و کلافه شده.
ترامپ احتمالا اوایل این هفته دوباره با تیم امنیت ملی خود درباره جنگ دیدار خواهد کرد.
پنتاگون در صورت تصمیم نهایی ترامپ، مجموعه‌ای از اهداف و سناریوهای نظامی برای حملات بیشتر آماده کرده.
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/11525" target="_blank">📅 06:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11524">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGyWUlaZYDe6-Ik3ng0zdeZipl7VSBkTKO6m3VpTW4AymbRuv-kzSMJBBMJoXeVaMK0DEH0XTdjyFfyODAIKhACgeE28g_4D0tAMM9KNhOweqAg2qa6H4bDbAGAmZAx-3Y74PFEsgK1X71JNDxXXOP8J8sdYdNhvd_i0pRrCfGuUyMl4Mui8GYMl37Ac9ySx_YO9R8KC4AN-FSulT3ru8P75q3zUnapZUTZmmtEwSV06WquQvgt4Vpa2klc9ntJSd7j7IGd4O1iJFR6FhYBoIylDWMwwf9vleLahi6u1L-9ahBMnNbu7WVp98NqwiOBBx9xLYDwBtDtYRs2L_foi7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث مبنی بر فشار یا حمله همه جانبه به ایران
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/11524" target="_blank">📅 01:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11523">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کان نیوز :هرگونه حمله آینده علیه ایران که به تأیید ترامپ برسد، به‌صورت مشترک توسط نیروهای آمریکا و اسرائیل انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/11523" target="_blank">📅 00:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11522">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سنتکام : ما تو زمان آتش‌بس با ایران دوباره مسلح شدیم و نیروهامون رو جابه‌جا و مستقر کردیم
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/11522" target="_blank">📅 00:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11521">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ به کانال ۱۳ اسرائیل:
فکر می‌کنم ایرانی‌ها باید از اون اتفاقی که الان در حال رخ دادنه بترسن.
@withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/11521" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11520">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هم اکنون گزارش CNN:
ترامپ تیم امنیت ملی ارشد خود را برای بحث در مورد ایران فراخواند
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/11520" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11519">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پست ترامپ از تیر اندازی  به پرچم در تلویزیون ایران فیک است !( این کار  انجام شده ولی ترامپ چنین پستی منتشر نکرده ! اکانت فیک ترامپ در X منشع این خبر است</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/11519" target="_blank">📅 00:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11518">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339423bcdd.mp4?token=MNqvyYaIjuw7diJR1HGGr0ZNek85InQ1pXxqj5GTya_P9YLSCGtyJ9PZ7oy-zk6QCNJAQ_ZnS1gQ3hSUD8ibKRfHDnw9OWlitkVQFsLW11S5-CrbQ5irQU9qHZxKDPZQ6Rf3xZLaBqZ4W_VIxlm0pZU2_rbpjd-FTrd2MbpYGF_JiwDBhM0BeZ7yLYI2_RkpPH3XpqwAo5VGd1ra73q_bK8_SFkaIFCotM5iW6fLHbUaE3rggv4z9OvtvDIMumD57DAwmdp-RQ45BESCIutOM-5IrcQPDJaQ1sB_ktHT6w4KxQwYMXyabOaBcN-UthkNytuRuzK_rfdSiSY6d-xtzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339423bcdd.mp4?token=MNqvyYaIjuw7diJR1HGGr0ZNek85InQ1pXxqj5GTya_P9YLSCGtyJ9PZ7oy-zk6QCNJAQ_ZnS1gQ3hSUD8ibKRfHDnw9OWlitkVQFsLW11S5-CrbQ5irQU9qHZxKDPZQ6Rf3xZLaBqZ4W_VIxlm0pZU2_rbpjd-FTrd2MbpYGF_JiwDBhM0BeZ7yLYI2_RkpPH3XpqwAo5VGd1ra73q_bK8_SFkaIFCotM5iW6fLHbUaE3rggv4z9OvtvDIMumD57DAwmdp-RQ45BESCIutOM-5IrcQPDJaQ1sB_ktHT6w4KxQwYMXyabOaBcN-UthkNytuRuzK_rfdSiSY6d-xtzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
دلیل توقف پروژه آزادی به درخواست پاکستان بود. پاکستانی‌ها گفتند: «اگر شما پروژه آزادی را متوقف کنید، فکر می‌کنیم می‌توانیم به توافق برسیم.»
ما پیش رفتیم و موافقت کردیم که آن را متوقف کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/11518" target="_blank">📅 00:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11517">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ادعای فارس
: ترامپ با آزادسازی دارایی‌های بلوکه شده مخالفت کرد!
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/11517" target="_blank">📅 23:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11516">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صدای پدافند در اهواز
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/11516" target="_blank">📅 23:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11515">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کاخ سفید: ترامپ و رئیس جمهور چین به توافق رسیدند که ایران نباید به سلاح هسته‌ای دست یابد و توافق کردند هیچ کشوری نباید برای تنگه هرمز عوارض دریافت کند
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/11515" target="_blank">📅 23:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11514">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اکانت رسمی اسرائیل به فارسی: شایدم اصلا چیزی ( جنازه خامنه ای) برای دفن کردن باقی نمونده...
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/11514" target="_blank">📅 22:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11513">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f212f792.mp4?token=CuHbveCkVA_sd5TGkLvLiKAXWgnWd4EHK3lwkU4abSo97AeiqbnngEIJ6pRQdHnh8FlQqgyPhEmktTwhs-NCpKqz06UqeqBUPwRwogNry1NIRIyYk8-jUweLCSeteqJHnenZhXlY9mf7gDm6TDUAG-SKuxQQHeG7iD1rXewkHLWijYCmuvYtIVu9kV6Ba_ZP6HboQ0vRpqOjyb4LKnVBJ_feRCMesNDuIObkvhCBY2e7mqDdY8HC4qNLBnNmh_ViVH0UdphQfAQWWoG9A6d_KpygJiofz7ch4U_HekCREF9eH0Ul4lcSasBkYtwUD5dyI77SfZK6Q16t7TMVd70A1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f212f792.mp4?token=CuHbveCkVA_sd5TGkLvLiKAXWgnWd4EHK3lwkU4abSo97AeiqbnngEIJ6pRQdHnh8FlQqgyPhEmktTwhs-NCpKqz06UqeqBUPwRwogNry1NIRIyYk8-jUweLCSeteqJHnenZhXlY9mf7gDm6TDUAG-SKuxQQHeG7iD1rXewkHLWijYCmuvYtIVu9kV6Ba_ZP6HboQ0vRpqOjyb4LKnVBJ_feRCMesNDuIObkvhCBY2e7mqDdY8HC4qNLBnNmh_ViVH0UdphQfAQWWoG9A6d_KpygJiofz7ch4U_HekCREF9eH0Ul4lcSasBkYtwUD5dyI77SfZK6Q16t7TMVd70A1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/11513" target="_blank">📅 21:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11511">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: ما می‌خواهیم توافق کنیم. آن‌ها جایی که ما می‌خواهیم نیستند؛ باید به آن نقطه برسند، وگرنه ضربه سختی خواهند خورد، و آنها این را نمی‌خواهند
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/11511" target="_blank">📅 21:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11510">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/11510" target="_blank">📅 21:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11509">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یاشار فک میکنم عرزشی ها هم منبع معتبر خبریشون تویی
😂
با این حجم ری اکشن هاشون</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/11509" target="_blank">📅 21:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11508">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoo</strong></div>
<div class="tg-text">یاشار فک میکنم عرزشی ها هم منبع معتبر خبریشون تویی
😂
با این حجم ری اکشن هاشون</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/11508" target="_blank">📅 21:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11507">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رسانه‌های اسرائیلی به نقل از منابعی گزارش دادند حملات به ایران پس از چراغ سبز ترامپ به‌صورت مشترک با آمریکا انجام خواهد شد و بانک اهداف در ایران شامل زیرساخت‌های انرژی است.
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/11507" target="_blank">📅 21:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11506">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آکسیوس به نقل از دو مقام آمریکایی:
انتظار میره ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت با تیم ارشد امنیت ملی خود برگزار کنه تا گزینه‌های اقدام نظامی علیه ایران رو بررسی کنه.
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/11506" target="_blank">📅 21:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11505">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ:  زمان برای ایران در حال اتمام است   بهتر است خیلی سریع اقدام کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. وقت بسیار حیاتی است!  @withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/11505" target="_blank">📅 21:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11503">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8925f5731b.mp4?token=NASsUydNFNiT8MUGZMP5K0oB07-XTrX-7ORiqLczMeiBPqj_QjgMP_yp0in0bvgTzr8ef0AdEM9sHq-qIKWHqQs0YMPXmyTTwA6Kdu-A_sAa1hRNbJTdm7fj9AYuUq3LcuMS7NG5_DUUrFVHCA6vEajNasJ_CNTeG7DJtxPi39GNjOQACi5mUsiX2-h0bVkIFXjV13ucUDv5N442aVr9w1QOuFCEk5tlfGR_ttrnqtOKlbUM2ByVtILoI0UWlVjr0XtdhTXgVIdWomWEtBlbjtz6KuSZd6T-d8-BmhdSHHdJcBQsHQoAI0z3PKWa3XrM55fDc15MBSAb2EN5qAieeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8925f5731b.mp4?token=NASsUydNFNiT8MUGZMP5K0oB07-XTrX-7ORiqLczMeiBPqj_QjgMP_yp0in0bvgTzr8ef0AdEM9sHq-qIKWHqQs0YMPXmyTTwA6Kdu-A_sAa1hRNbJTdm7fj9AYuUq3LcuMS7NG5_DUUrFVHCA6vEajNasJ_CNTeG7DJtxPi39GNjOQACi5mUsiX2-h0bVkIFXjV13ucUDv5N442aVr9w1QOuFCEk5tlfGR_ttrnqtOKlbUM2ByVtILoI0UWlVjr0XtdhTXgVIdWomWEtBlbjtz6KuSZd6T-d8-BmhdSHHdJcBQsHQoAI0z3PKWa3XrM55fDc15MBSAb2EN5qAieeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعر امشب
😬
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/11503" target="_blank">📅 20:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11502">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مقامات آمریکایی به اکسیوس گفتند:
مذاکرات با ایران به بن‌بست رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/11502" target="_blank">📅 20:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11501">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل:
ما منتظر یه پیشنهاد دیگه از طرف ایران هستیم؛ اگه این کار رو نکنن، با شدتی بی‌سابقه هدف حمله قرار میگیرن.
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/11501" target="_blank">📅 20:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11500">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/11500" target="_blank">📅 20:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11499">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گوگوش در پیامی در اینستاگرام اعلام کرد مدال افتخار سال 2026 «جزیره الیس» را دریافت کرده و این جایزه را با «عشق و احترام» به مردم ایران تقدیم می‌کند. @withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/11499" target="_blank">📅 20:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11498">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گوگوش در پیامی در اینستاگرام اعلام کرد مدال افتخار سال 2026 «جزیره الیس» را دریافت کرده و این جایزه را با «عشق و احترام» به مردم ایران تقدیم می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/11498" target="_blank">📅 20:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11497">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:  زمان برای ایران در حال اتمام است   بهتر است خیلی سریع اقدام کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. وقت بسیار حیاتی است!  @withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/11497" target="_blank">📅 20:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11496">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da3Fq2fb6m7277ZprGDriGFr_cu_hA93EkYW8-uea3yAXnnArimnfmK4xT5AAJVOjWZOQpq4uVO302Nz-jQ80O5PGbPvKqU1FsEGIUoL1FTzR-f4JaTJtBGwEz1Evpegst04E4b2DIPQGViPIEuHEciRT-tOWsiaKdoqmNgUXxOqQwklL1p3s5Qr_Q1PBTMGAd3CjNFPYTIIDSWlYB10sarGWGNw3EUG4e4aZgiQWeU6RJo4X29sgLi8rBxV-e7lA9Q6FomR-6aT64Fy9DUO175bqXz_vH1R5WgwkbZ_y1ueAG3lcUP9TZqndhS1SNatKqAAAblK3xPQmnyRfZgsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:  زمان برای ایران در حال اتمام است
بهتر است خیلی سریع اقدام کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند.
وقت بسیار حیاتی است!
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/11496" target="_blank">📅 20:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11495">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c29a07582.webm?token=oKBDiQdI58huQMob9PHaAmv5SPMsnO5r1-DVQLphbUE8_kOLz88K-xxfAePWqWZBemMkV5Y8C-DXfOSKE-qvVaHdBSqj1UIxi_lMzS3-q53Oy16wWHuEjAYgfPMtePMuOXtxTqQKrxliZ9heEq3MzjqHEcgX5_I_FfbXGHyIyQPJzhO5aUooybLNCnxYcee6__7LB101CFteaYGnUups8D85pXCdrlytRMONhjyogTfp3e4EqPNEqDeqstx0aYJ1suEqw9CMst8_by8rbmPbwwMlsnxdzAiGDwj5T_Buzl1Zr-07GOk4VUQrxhEpooytyyDko03EzJW3o_Elnm6oxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c29a07582.webm?token=oKBDiQdI58huQMob9PHaAmv5SPMsnO5r1-DVQLphbUE8_kOLz88K-xxfAePWqWZBemMkV5Y8C-DXfOSKE-qvVaHdBSqj1UIxi_lMzS3-q53Oy16wWHuEjAYgfPMtePMuOXtxTqQKrxliZ9heEq3MzjqHEcgX5_I_FfbXGHyIyQPJzhO5aUooybLNCnxYcee6__7LB101CFteaYGnUups8D85pXCdrlytRMONhjyogTfp3e4EqPNEqDeqstx0aYJ1suEqw9CMst8_by8rbmPbwwMlsnxdzAiGDwj5T_Buzl1Zr-07GOk4VUQrxhEpooytyyDko03EzJW3o_Elnm6oxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/11495" target="_blank">📅 20:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11494">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اتحاد باید شکل بگیره ! حتی بچه هیئتی ! تغییر رژیم شکل میگیره ولی تغییر عقیده کار یک شبه نیست و باید هر دو سمت شل کنند ! من خودم کافرم ولی تیم باید تکمیل باشه ! آس پیک شخص شاهزاده رضا پهلوی تنها هستش ! ترامپم مارو میره قاهره شک نکنید !</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/11494" target="_blank">📅 20:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11493">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">محمد پروین دوست خوبمه امیدوارم با تغییر جهت به سمت مردم برگردند</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/11493" target="_blank">📅 20:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11492">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72df07c21c.webm?token=ry17GHyCWM4LzaJ6oLa0vKwVO9tvn4AkDWcB19DUu92dHaEt-ZeLU2MEd-bKA5Ix8gcBVcau85SOjznSSpDpDNf-Y-VLUpZzJrUMO_7InyHbMpMFU7DyYPT1-CR0N-SBLIh7RuYawBnQTnchNCIhwlSu8ZSrb5vfWmtv7aDDSbJOZTyLg1DVWCjjT7ogYia2PV3ZEW1DZtk4rZrl2uJkdt1NYMISmJe9Xz5k2VGiZcEGgGqmtgvx9rMgFxt0GzMZWYOSMALDRTbLfXl8v30iUcxjTwYPJqgiRxwVAurXQhq6-UqQcHUXy2VPFoTeXYxyO-F2p4nSpe3gGsKoQI3SyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72df07c21c.webm?token=ry17GHyCWM4LzaJ6oLa0vKwVO9tvn4AkDWcB19DUu92dHaEt-ZeLU2MEd-bKA5Ix8gcBVcau85SOjznSSpDpDNf-Y-VLUpZzJrUMO_7InyHbMpMFU7DyYPT1-CR0N-SBLIh7RuYawBnQTnchNCIhwlSu8ZSrb5vfWmtv7aDDSbJOZTyLg1DVWCjjT7ogYia2PV3ZEW1DZtk4rZrl2uJkdt1NYMISmJe9Xz5k2VGiZcEGgGqmtgvx9rMgFxt0GzMZWYOSMALDRTbLfXl8v30iUcxjTwYPJqgiRxwVAurXQhq6-UqQcHUXy2VPFoTeXYxyO-F2p4nSpe3gGsKoQI3SyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی پروین در بیمارستان بستری شد  علی پروین پیشکسوت باشگاه پرسپولیس برای دومین بار در ماه اخیر در بیمارستان بستری شد.  پروین به دلیل چکاپ پیگیری برخی از موارد پزشکی مرتبط با خود در بیمارستان بستری شده و نزدیکان او معتقد هستند که احتمالاً تا یکی دو روز آینده…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/11492" target="_blank">📅 20:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11491">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">علی پروین در بیمارستان بستری شد
علی پروین پیشکسوت باشگاه پرسپولیس برای دومین بار در ماه اخیر در بیمارستان بستری شد.
پروین به دلیل چکاپ پیگیری برخی از موارد پزشکی مرتبط با خود در بیمارستان بستری شده و نزدیکان او معتقد هستند که احتمالاً تا یکی دو روز آینده از بیمارستان مرخص می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/11491" target="_blank">📅 20:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11490">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شبکه عبری کان: نتانیاهو و ترامپ، بیش از نیم ساعت با یکدیگر تلفنی گفت‌وگو کردند و در مورد امکان از سرگیری درگیری‌ها در ایران و همچنین سفر ترامپ به چین بحث و تبادل نظر نمودند
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/11490" target="_blank">📅 19:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11489">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝕭.𝕽</strong></div>
<div class="tg-text">کلاه شیر و خورشیدمو الان باد برد تو آب های خلیج فارس…
🥹
❤️‍🩹</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/11489" target="_blank">📅 19:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11488">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo5XVvBhYk1TF2Vy_pULfLD-dsDsjIN2TPIklwRQEnxQg7Ea-eeywLpy6c7by2iTX7ktDV8XA5lDf-vQQWrfN5EuzdvEfQUxziYQ1vt_OQuVhrML_f0MMKFGK1sFVmBvChMVBQRloi1chb3E0r13BOcy9u7SyTUzLvb1_L1c_x6VcrQUScpbABqXwf7stLoocO0yEwMx7VUHyP-SFuk_gZH2JgQHnZlkyNbvDOpS9OHG0vhJap5-X6BfO1e5mD3ysov6v_rSQ_vUAFOzeM7fTXY7qWc6DpdxFNNfPO_-QwAcLzLxQBXBQfxjq883UQpKCUfvS9l5gHDLSFEFcakcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاه شیر و خورشیدمو الان باد برد تو آب های خلیج فارس…
🥹
❤️‍🩹</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/11488" target="_blank">📅 19:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11487">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">زیرنویس شبکه العربیه:
قرارگاه خاتم الانبیا به یگان های موشکی اعلام آماده باش فوق العاده صادر کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/11487" target="_blank">📅 19:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11486">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">زیرنویس
شبکه خبر: هشدار درباره عملیات غیرموجه علیه کشورهای منطقه و انتساب آن به ایران
یک مقام آگاه نظامی: ایران همه کشورهای منطقه را از افتادن در این دام رژیم صهیونیستی برحذر می‌دارد.
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/11486" target="_blank">📅 18:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11485">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سناتور لیندسی گراهام در مورد ایران:
طبق تحلیل من، هیچ نشانه‌ای وجود ندارد که افراد مسئول فعلی با گذشته تفاوتی داشته باشند - آنها هنوز می‌خواهند جهان را به وحشت بیندازند، اسرائیل را نابود کنند و به دنبال ما بیایند.
بنابراین شما آنها را بیشتر تضعیف می‌کنید. کاری که رئیس جمهور ترامپ انجام داده از نظر نظامی شگفت‌انگیز بوده است. زیرساخت‌های انرژی، نقطه ضعف آنهاست. برگردیم به بحث جنگ، من انرژی را در صدر فهرست قرار می‌دهم.
من خواستار آسیب رساندن به این رژیم هستم. بیشتر به آنها آسیب بزنید، شاید آنها به توافق برسند. اما در حال حاضر فکر می‌کنم آنها سعی می‌کنند منتظر بمانند و بازی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/11485" target="_blank">📅 18:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11484">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کیهان لندن : آماده باشید که احتمالا آمریکا و اسرائیل به زودی حمله می‌کنن
@withyashat</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/11484" target="_blank">📅 18:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11483">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حریق در یک ساختمان تجاری در خیابان جمهوری تهران
سخنگوی سازمان آتش‌نشان:
ساعت ۱۷:۱۴ دقیقه یک مورد حادثه آتش سوزی در یک ساختمان تجاری به آدرس خیابان جمهوری بعد از خیابان شیخ هادی به سامانه ۱۲۵ اعلام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/11483" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11482">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mehmooni (iG @yashar)</div>
  <div class="tg-doc-extra">Amir Tataloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/11482" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/11482" target="_blank">📅 18:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11481">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd18535cb9.mp4?token=ZmNulJ0sgq4eW5det00nJ8gDQyc109VOZjODLaQB5xsgLSBZFcQVYUABSTfuytvdGPqHy2MYObojZhT7v9fdaAfuNjvhN9AXbQtpgiceCTe3RtfxcZf9wfa-p5zQzWbJW81qfZUFbCa8EAIArUD5J09I7hyAHjL7e2s9g4KI1QQg-bbzwbbIAgSf1cbTSuSZwlmaxywJ4YCVpsuVLgdM_N5t1Fw2uayryrB7Me9h_S2tIm5SYYa1bKL_3-VfL8UG6h8LH-JoqF39BLRXVR-bWKGL7iGkX1eIR4nLkzFzQaB4dgIogNP1PMpG15JR8ByapETNqIKXMR7GIUBmcNN99Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd18535cb9.mp4?token=ZmNulJ0sgq4eW5det00nJ8gDQyc109VOZjODLaQB5xsgLSBZFcQVYUABSTfuytvdGPqHy2MYObojZhT7v9fdaAfuNjvhN9AXbQtpgiceCTe3RtfxcZf9wfa-p5zQzWbJW81qfZUFbCa8EAIArUD5J09I7hyAHjL7e2s9g4KI1QQg-bbzwbbIAgSf1cbTSuSZwlmaxywJ4YCVpsuVLgdM_N5t1Fw2uayryrB7Me9h_S2tIm5SYYa1bKL_3-VfL8UG6h8LH-JoqF39BLRXVR-bWKGL7iGkX1eIR4nLkzFzQaB4dgIogNP1PMpG15JR8ByapETNqIKXMR7GIUBmcNN99Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/11481" target="_blank">📅 18:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11480">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نمیدونم چطوری اطلاعات بدردبخور رو‌انتقال بدم  نمیدونم اجازه میدی به وقتش واسه خودت بفرستم و تو یه کاری بکنی؟</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/11480" target="_blank">📅 17:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11479">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA i</strong></div>
<div class="tg-text">نمیدونم چطوری اطلاعات بدردبخور رو‌انتقال بدم
نمیدونم اجازه میدی به وقتش واسه خودت بفرستم و تو یه کاری بکنی؟</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/11479" target="_blank">📅 17:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11478">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شاهزاده رضا پهلوی : جمهوری اسلامی را نمی‌توان تغییر داد همانگونه که یک گرگ را نمیتوان تبدیل به میش کرد
@withyashar</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/11478" target="_blank">📅 15:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11477">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e1343f7.mp4?token=g3xa1X8qm51VzzZtavlVYLMtYzc995TWJ287ZsKxZUI9ZtuYB1paCPugxMQleBxZ4WyG0Mcsw9o_HV_7gQmEuZMGUcnOVHkjH4ZdMf_8OZuClm2YlOx80m8Ms-Bwi09YvjQp1soRGqIpSyhIXNT0CjPZioJFGYCBMs0aYY0rPRZc1ED8EkfWUja4ZAIbCTYlm8NDJNuFxatmCyAl61roO2vpfils0KVwD3vCCrFLCvBhAqoWv3pEK4Rpwpi9lJy1Hj3VcDSnb2MFAhDC7hMRdUqwmKBekFKpS0TTJ-ylI6eVVUHO3Nbc46BH18wQJs8_hEe776Lo23TCU1WMIItBUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e1343f7.mp4?token=g3xa1X8qm51VzzZtavlVYLMtYzc995TWJ287ZsKxZUI9ZtuYB1paCPugxMQleBxZ4WyG0Mcsw9o_HV_7gQmEuZMGUcnOVHkjH4ZdMf_8OZuClm2YlOx80m8Ms-Bwi09YvjQp1soRGqIpSyhIXNT0CjPZioJFGYCBMs0aYY0rPRZc1ED8EkfWUja4ZAIbCTYlm8NDJNuFxatmCyAl61roO2vpfils0KVwD3vCCrFLCvBhAqoWv3pEK4Rpwpi9lJy1Hj3VcDSnb2MFAhDC7hMRdUqwmKBekFKpS0TTJ-ylI6eVVUHO3Nbc46BH18wQJs8_hEe776Lo23TCU1WMIItBUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما:   با اعلام مدیر کل آموزش و پرورش تهران؛ دانش آموزان پایه های هفتم تا دهم دیگه امتحان خرداد ندارن و با توجه به عملکرد علمی یکساله سنجیده میشن.
@withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/11477" target="_blank">📅 15:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11476">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیویورک‌تایمز:  آمریکا به عراق دستور داده بود که طی دو عملیات داخل ایران، سیستم‌های راداری خود را خاموش کند و عراق این کار را انجام داد
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/11476" target="_blank">📅 15:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11475">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو: امروز با رئیس‌جمهور ترامپ حرف میزنم،چشممون روی ایران بازه، برای هر موقعیتی آماده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/11475" target="_blank">📅 15:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11474">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzdihb1zILiz0uc1w5vIXaAD3AOGCwPBAQja7canzpSy-1Nt3dAS3kMEUuSycSo-8THZwPci0Up2WYTL_5WzarmzaFdNSLDiIPxRZmEXMK1UY2704ViDW-yNtpiYFmFjEFUv_8N4nxnaxNkEN3wunh4nWB_KaqKFZbXSrV0-bZd5RfVgX9w47tl5aIWaPQg4-X1NzfPtGyV7U6AXI8u7guxIxOesJx-02TyRGmzX5SekgOtWFWwVf2Z7dDrUPwgFFaTZsUZ5FXp_jz6tl_rARaZGuc2M0q2Bb2oIJcsqxxQ6mgxfPmg8PhHmzWPNQTezVAsyDG5G8PQiAwwKksHVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: یه کشتی اسرائیلی تو خلیج فارس توقیف کردیم که خدمه‌ش عکس علی خامنه‌ای و مجتبی خامنه‌ای رو روی دیواراش نصب کرده بودن.
@withyashar</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/11474" target="_blank">📅 15:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11473">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو: ما در غزه اکنون چیزی را در اختیار داریم، دیگر ۵۰٪ نیست... اکنون ۶۰٪ است. این وضعیت امروز است.
ماموریت ما یکی است: اطمینان حاصل کنیم که غزه دیگر تهدیدی برای اسرائیل نخواهد بود.
ما محدودیت بودجه نداریم. هر چقدر هزینه داشته باشد مهم نیست، شک ندارم که اسرائیل اولین کشوری خواهد بود که راه‌حلی کامل برای حملات پهپادی ارائه می‌دهد
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/11473" target="_blank">📅 14:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11472">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتانیاهو با ترامپ تلفنی گفتگو می‌کند
رسانه‌های عبری: نتانیاهو امروز با توجه به تحولات و تنش‌های منطقه با ترامپ صحبت خواهد کرد.
@withyashar
امروز همچنین اسرائیل جلسه امنیتی برگزار میکند</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/11472" target="_blank">📅 14:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11471">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تایمز:  انگلیس برای جنگ آماده می‌شود
این رسانه انگلیسی از افزایش بودجه دفاعی انگلیس خبر داد و هدف از آن را آماده شدن برای جنگ های آینده اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/11471" target="_blank">📅 14:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11470">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مشاور سابق پنتاگون:تحرکات سطح بالای نیروی هوایی آمریکا در خاورمیانه شدت گرفته آماده باشید
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/11470" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11469">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دارم میرم یات تولد ، شاید دایرکت ها رو درست نبینم کم اختلال داریم ولی من هستم
😬
🙌🏾</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/11469" target="_blank">📅 12:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11468">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سی‌ان‌ان: ایران به کابل‌های اینترنتی تنگه هرمز چشم دوخته
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/11468" target="_blank">📅 12:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11467">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/11467" target="_blank">📅 12:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11466">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlejandro Sosa</strong></div>
<div class="tg-text">داداش شما رئیس سواک میشی شک نکن</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/11466" target="_blank">📅 12:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11465">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فک کنم ساواک روزی که برگرده باید اول به من بگه دادچ آرشیوتو بیار
🤣</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/11465" target="_blank">📅 12:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11464">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1faf363e.mp4?token=I4TaiILPw7ou-w_7-mTb0kBcFhAIyWSOeuGrDzuQbfaXwpKmhnFlejfoBaFjqRe7jd_Aq4GHWZZZILDVatjxPN7ljSlBzEAkR5g0B5qTMusnLinzZaOuksFhVQysncLXt9k2T89xR-YKsITYDh0c9i34mfCszsF_32f-lvkd_ZRb4ZbxqF6kByFdqJ7N46uovA_yO3JE0btYGbVbLyBgVAlY8-B9hmnGVERsDrCSCNNCBz-PCwSISSjEU-WNIJ-81LzRpm7x7EwUa1MJzKSo--NLZmYzXd3jvWTrTG2CdnvcfzFhVd99hbO34zygZMqCYZdYYSqS4DBzzFOISwf2rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1faf363e.mp4?token=I4TaiILPw7ou-w_7-mTb0kBcFhAIyWSOeuGrDzuQbfaXwpKmhnFlejfoBaFjqRe7jd_Aq4GHWZZZILDVatjxPN7ljSlBzEAkR5g0B5qTMusnLinzZaOuksFhVQysncLXt9k2T89xR-YKsITYDh0c9i34mfCszsF_32f-lvkd_ZRb4ZbxqF6kByFdqJ7N46uovA_yO3JE0btYGbVbLyBgVAlY8-B9hmnGVERsDrCSCNNCBz-PCwSISSjEU-WNIJ-81LzRpm7x7EwUa1MJzKSo--NLZmYzXd3jvWTrTG2CdnvcfzFhVd99hbO34zygZMqCYZdYYSqS4DBzzFOISwf2rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان بحث داغه دیدن این ویدیو شاهین نجفی هم که در اوایل شروع ‌به کارش برام فرستاد خالی از‌ لطف نیست ، من امید وارم همه با هم متحد باشن و مشکلات تموم بشه
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/11464" target="_blank">📅 12:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11463">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ac4f62eb.mp4?token=q2lfIBYDVevb8COWKIjj78JWxC_z42B5Lfq5dL-FIbqZvbGjjUm2flhmNO8KVNZ9yU6Jvz2iGhCQ92TYlD7ubTLBSiI-BiYuKayXFU4BeRx5kMcd3vbm5i-xXfN-XAgE7ctMiRUBOL9kTJCDYFAJVBnL_TuLUItMQ5J-RSZdjUZwT_K6Kf88kO8f6l16hezZcjE8lEeWjFGnog9Sude_DXgrKYYnfP6sG-WZhjlpqKwCGitlwuAX4Nd0giHKuMxR7Eo46_YAykDvMrjnqe_az7lhnazAgEplidEkgNIYCBOQmoLQ-vD-Bv1ZYQlsCWeF8vD-C3XdNn7qvakIqPch4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ac4f62eb.mp4?token=q2lfIBYDVevb8COWKIjj78JWxC_z42B5Lfq5dL-FIbqZvbGjjUm2flhmNO8KVNZ9yU6Jvz2iGhCQ92TYlD7ubTLBSiI-BiYuKayXFU4BeRx5kMcd3vbm5i-xXfN-XAgE7ctMiRUBOL9kTJCDYFAJVBnL_TuLUItMQ5J-RSZdjUZwT_K6Kf88kO8f6l16hezZcjE8lEeWjFGnog9Sude_DXgrKYYnfP6sG-WZhjlpqKwCGitlwuAX4Nd0giHKuMxR7Eo46_YAykDvMrjnqe_az7lhnazAgEplidEkgNIYCBOQmoLQ-vD-Bv1ZYQlsCWeF8vD-C3XdNn7qvakIqPch4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا همش به تاریخ پیوست…
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/11463" target="_blank">📅 11:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11462">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تو اين مدت هر وقت كه ولنجك رد ميشم ياد شما ميافتم، هميشه و هميشه و هميشه اين ويديو رو براى شما گرفتم و صميم قلبم آرزو كردم به زودى خود شمارو تو ايران ببينيم
🌸</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/11462" target="_blank">📅 11:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عباس عراقچی، اعلام کرد که کتاب «قدرت مذاکره» او به چاپ پنجم رسیده و در چاپ جدید این کتاب، بخش جدیدی با عنوان «دیپلماسی زیر آتش» درباره روند «مذاکرات غیرمستقیم با آمریکا در جنگ ۱۲ روزه» به آن افزوده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/11461" target="_blank">📅 11:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تو اين مدت هر وقت كه ولنجك رد ميشم ياد شما ميافتم، هميشه و هميشه و هميشه اين ويديو رو براى شما گرفتم و صميم قلبم آرزو كردم به زودى خود شمارو تو ايران ببينيم
🌸</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/11460" target="_blank">📅 11:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM.A</strong></div>
<div class="tg-text">تو اين مدت هر وقت كه ولنجك رد ميشم ياد شما ميافتم، هميشه و هميشه و هميشه
اين ويديو رو براى شما گرفتم و صميم قلبم آرزو كردم به زودى خود شمارو تو ايران ببينيم
🌸</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/11459" target="_blank">📅 11:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11458">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/11458" target="_blank">📅 11:01 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

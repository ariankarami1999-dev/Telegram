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
<img src="https://cdn5.telesco.pe/file/lKncEe7zBz7hl2UtJeuPpgnKfuCPXOwvPTzoD0p5IjFq_XCbCXF3ItbfU-zhpyNq1VYevMMacTHrKPV-IBEasGUU9c7oPmmEN5c8vlECoEuB6Xi59ViWFUrTMnXAb7RdruTqKGleeFoMlIHUSOyjv4MO_ffBvFJtxmsUq_yZXD9SoTs3kqLxi9mYM1VK15cd3GMddzAx0yG_B35h0QgFOd0zcucmXMJlfBF81guHVdob8vnnbZL-mGNV6HTpXe2LkXo0zdp-MbJpkc3SkCcCJ8mdu-hKTAob4OZGjS_OfiL4IEiVZNx3lpPJvl1azLkBEWAaSG2pefYKXa6n3EP-aQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 523K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌هاط ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7ooaVI_DvXbplMBM_mWIcSUaU5gp70ZrlGnwfejtpS3aK7AXhdlkoqIjZA5G6EpWHLT87iTRchVuHWurSY5KS-zAHwkynxPDzQsTT50lxCFUhzciut0Lu5135VCbMqFtNnDjX7h87VKefvmutT325_oJAeKgOUJd0UQImuNLZN_emiLSuYRVq1zc5bTt1VsiizA4ITp7lPzJB068tvnKqzmdOic4hZL1BaMvFSqfBP1_9jV0JKvzM_mfLu4uEINk6WYofq0L3lMIGvT-Z0Ust71L8k55HdCBU7MF9Hj5k1YNbKJdOSgzVyD_vgdxXdg9bPvjG6-ZH4g2SLrCsVjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru09_HfwE2SPkORjfDJSIa6ce_MJooCx5CijpBlTU0ZHmOCjLcYmEYnOkI_kZZQHvUdI7SFWTDoJCQo3VE08ae-UU8t0ADsHcYp3K_G2aO44KECshjiJSgTFm396yIukUVv1o2KDqRUu-iSGt1paqiri-Z_sUm5-ockCsHsEABPRXh04GtsdiJV85LNcJ2JdezcTaj2T-QbvKwvVYcd1CHM3tgh8DMLaFaKjaiFLJdt6POkNPGDO15SQShh6EJAEj_SfIzwAg1KDrG8emK9N2l4_J0nCa5vRAx5DWCsNFIe-q0b1gyfPFlfx296hza_hlmlk1t1TsuqbfvxWSmO3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-kaq3X8DHKyHrA40cN3pXJsY5ko5nSUGUi9gCNpWgOSY-VL6A5nKjPCm9jcO_f6hq14bgKIUAt8PdZ1nsKUranF5Hr720D-8dg8GtBogKM0mqtWhX9oqAEsTOM3hqhU3ObtaxoI69wDapLLlJcRtmE6zaw6Qdvdcbqen43ysxkw-q-XvARaLSA7jKMSYpCb2A2X0lGxXUT8uSh6yIKOeGsTanaKlC8sP7mR_H8J-MRZKi6yVLlIGsqPm_Ad-9V9PBdv4I-7tagLf1GsW_cdeaNb0IWUh_z025yLsKJQp-wVi4N5U3FHkTlTUb3S9QVMPqte-M2luEeg03DD8cN9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی اسپورت
:
یک قانون جدید در فوتبال انگلیس در مورد مصدومیت‌های دروازه‌بان‌ها اعمال خواهد شد.
اگر داور اجازه دهد که کادر پزشکی وارد زمین بازی شود تا به دروازه‌بان مصدوم رسیدگی کند، مربی تیم 10 ثانیه فرصت خواهد داشت تا یک بازیکن از بازیکنان حاضر در زمین را انتخاب کند تا به مدت یک دقیقه از زمین خارج شود.
در صورتی که هیچ بازیکنی در طول 10 ثانیه انتخاب نشود، به طور خودکار کاپیتان تیم به مدت یک دقیقه (خروج موقت از زمین) انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLE5THPEjNFzyS6MBdKuXMoI0IFxLaDkEBYUnVobhk0DaUKXD_OPLlUUnYHEII95mMPEuZG7ulQP9rks7s3oQCs8QJpyEb9_jHEF72_z8-eirWjHDPJ5UGKYRqFBIwEiKDAlpSrAUPHAfQ0g0izkt6tbAGqZwHY_PdIZAN29QtZ-B1OWOFQh1dLFnRJmkJCgj_Z5VPdoTI7JdsgYXKGckvAYUtLgl0paYSg3JjU4QNJpJfq4VEmne9J1g5c2YZ_rPPxdymQs6cEceE4G-v1px-0-i_Q8LCN7804MusPbsBdlT_Nf8Ib3hgLBLwQDnbTyKOlLX0DLJ8mKN3M4Sbhnaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو:
‼️
بارسلونا با افراد نزدیک به کروپی وارد مذاکره شده.
⚠️
بارسلونا با بورنموث تماس گرفته تا درباره امکان جذب کروپی پرس‌وجو کنه. بارسا یه سری اطلاعات درباره شرایط بازیکن جمع کرده و چند تماس هم داشته تا وضعیتش رو بهتر بررسی کنه. کروپی بازیکنیه که داخل باشگاه بارسلونا خیلی مورد توجه قرار گرفته.
❌
البته این انتقال خیلی پیچیده‌ست؛ چون بورنموث نمی‌خواد تابستون امسال بازیکن رو بفروشه و منچسترسیتی هم بهش علاقه نشون داده. بنابراین، این معامله اصلا آسون نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7hT0ZAEGd1c_n6nEFg8KbNNdbX8FQOX6mEO3aMRH9PnZ0qybs1GOk15C3s5-BHW9FO_5evC8hAoyVtkamftKJkK6tXdJs-O-Uev_FVsRHo_DPZVVWZVYI7GxxMSkanf5Vw8uTQcSBcIYopvQF1nB-BJU7gv1mqLIbms3ZTC49mHKJkc3OSZ9sTHIyHtyNP943FnL3VbXzNFtg9osSclqNN_UH0WqM0tFBQA2cgjWrJo73pjc5_wLlgHyyu0noXoldD99NItxI_31XwVlvuXctpiUhJpbs-GWL_DYJk4N3lmNyuPWdacFgGBo32LlG3d7Sq88CccluDBGyAZDn1zLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فرانس فوتبال اعلام کرده که بردن توپ طلا حتی بدون کسب یک جام بزرگ تیمی هم امکان‌پذیره.
📊
این اتفاق برای این بازیکنان افتاده:
🔺
جورج وه‌آ در سال ۱۹۹۵
🔥
🔺
لوئیس فیگو در سال ۲۰۰۰
🔥
🔺
کریستیانو رونالدو در سال ۲۰۱۳
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czCXJ5f93YtMacoNjSm-GhMLzXLbzFewc8I0jdf4mkFTQxxgFycrXrj6KoqnqRYBE7SPsOQAECgY5-wEI39DY4iwMIhYCWPqrCK8TNqbx5QtJnvdZ1tCH6jF95p2xEwn6W17-PM8S-z7ZZd6RbUaMJepjdLqodPx8pygbz-WHhGTpttLNZaffrc-OvsMtY6VuZSLL_U53CGJ6VAYpapbkdWXDKlw9cZkL549WEjz7tOcZeOcmP0BzE6cG8khjnVTrI_T0PdOu4sCoJWN98j5zPJWWexiB5a3gBf5QR0ZDe1Ph9aN9by37kvRqZg_dgzWXCm3JeCmUXWDm9VTMK6moA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm6Igoe33qI_V3q03ogwEOWM5hwbKN6mSFLe4pvbYhYf4aiCEuJ9GzB6sAHojQ3U-QHy0ZuVfiGjLY-C1izF6AUuui6DIFjkNtjODxHZO0R9RC-eyR6m2alrUJ26mON6pRYdc8ytsJ4kK_jQd5wvAP17CcExk_MaW434dsWEMxAmPG_HxkJjlVqnKr90UlyL_A_7NBZZ86v-HR9SxJuSEyfKiXxvPDNxnf-KRPvK4niviJBGM85Hg6ZqgvSHdxifUiPQqD_lOYw-oAIql0P18_dbRu0RogJKW81Hf4-o1FRa0GPhH6ODAKyVuSiL3u3DKhUM-7LwzGSH3mlCqtqR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdANBG0UT5YHhq_refDmi7hg_DbiNfRTqZPssIOELD5rlsSlJPFdoIw4gSvmgWsRnopNEAWNrpgJQ8T3eLkfN9ys6OsfWWNemJTd2GPUkCRbPqxZcPO3xFMtyc10xVSxv-8hxdLwa5h27j4yq417K4oVlF8tLk9wJ6IZ8LJwVUm6pJafufmA5TGevCA4-MPEg5j2wJuFRJhuCsHBjK3VjAquHQiayRiBtM7rAwIbf8BhNKDSpGq_eX13oxPUELAgo-bs8VbhaEzhO9HHWyhpdZpaPCibeWhacC-hzso3qnGQ3P6iP2RNKLsExK0XHJ07zgkVmiIpWsPtDjgdoDAExQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102071">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy2JL5U7tDdGJ429KDWQN6otYVponUOQsSSt4YFQDa3WMOjQesB6O3QFKo75Pl81T2Vy4stjr6wtQLcCqmMfsibqIRNQiL2e41glUtvyL4y4VbYP58weK_Mbtp0oITBmBrnjqPcBzfNKeCmTWoP-l1xxDPuY8Gnhz11Obti-CFeznb2eBylt5RHERAeINU8C5tegaouWMCIi0uUGzPsl78DkfZefC5SVfF2WmAn1E8pqqA2a8dSz-aqUCsY_f-TIrxHLOVLqzBaEJByk8NoyEz0oShxeSkySE4vqR-L7RH__WNgnjj2D5aFF6f8DGSQAPaakwicVMoFxr3BkheWGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور دیومانده در تمرینات لایپزیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102071" target="_blank">📅 16:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102070">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=uJAshLxpo0CB0Lqi8t-WZjdtnrpuymJ7VkejC-ADSXTK2A-r3A-K_Ba33itwbzku1XfU42XsAljq6cCdeHt4dT2WBzqJgyvncRtHPQuTDyIaAQWEKudix1o9mCOs2pdQsSgvylb8VyO7_Yw8DZLbcVRfAt7OFdR77U5j5ZZRCMSmRlggaoTGLSz96Ld2FMccEazcJaK0Oq52A8NcWw0H8U3sGQpN8Jdpt54gAjtP7xsiYlpXhkBZolPf7zFNl_D_Lu0X-B3IjJb-XQXOPuUXNBCGNKclaEGyvXQ_Chj15DPjfLbmpHExaZ7Rtd-hNXbfA5hfNM6GBozOatCYnYBwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=uJAshLxpo0CB0Lqi8t-WZjdtnrpuymJ7VkejC-ADSXTK2A-r3A-K_Ba33itwbzku1XfU42XsAljq6cCdeHt4dT2WBzqJgyvncRtHPQuTDyIaAQWEKudix1o9mCOs2pdQsSgvylb8VyO7_Yw8DZLbcVRfAt7OFdR77U5j5ZZRCMSmRlggaoTGLSz96Ld2FMccEazcJaK0Oq52A8NcWw0H8U3sGQpN8Jdpt54gAjtP7xsiYlpXhkBZolPf7zFNl_D_Lu0X-B3IjJb-XQXOPuUXNBCGNKclaEGyvXQ_Chj15DPjfLbmpHExaZ7Rtd-hNXbfA5hfNM6GBozOatCYnYBwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
عاشقانه‌های رونالدو و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102070" target="_blank">📅 16:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orUoyUrhagI10YDYWkyYeyQMy0kGQj3JrY7QTNQcyFVnEdRXezLAoe-Qlxr3KNqhjG4OBO9U5jl80Q0arc3_7CB06Eswpr0FZqeGRnjdcw_avDn1p_a1TEQoio0yq0yVeed068kW4oZYmJKj7Um4U2Oq0hBmMSmTWjkAgckyCsLpvm0RLZ8zXY5GgkmSjPkywXSnQ3QlcdZEihnYq0H_tDuwaSmnAA7-F5Ry1rprmFu0Ro6IHkQLz7lM0_p-Dxo1q0qVHPkwtYUxpLbtK1DFMspu44SSZNvL1eNS_Cm3xQBBZ124VLWsyHYWILx9qTmUB2SXrSys3X0i_pDiV2QsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hz0DKsiVEbL-yb0JqYu3W4rWGK5xEjTRd5cyhUGbvHDXivqXiaFYxgZ3BXDKE_WKWZd_44ugE-aHwK3kpt9IlI2JuvexxCpnBFhz9NpQsFFci__hn1pSLcHtbvLqndhS_tWumEigkJM785xzz7eZni0uFB36vihBTPs8Mjq8p_NPN8M2q-_5lLy1ttjeZ2LJ1AOJRccTrQi0TrY90Uq5XhLFIi1QK00Z0vTxAyCq3aWlgLn_hLHhqbp3lg42_CHA6V3AgkQw7JD0L95qOMgiJR2QMa3bErIW_DgTBNts4vQqORYVFVBfd36deefieQkf6cUgCtVyl33fyw6XScEyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4D4XFOCDkFaGoVzJOqYAKtBUsi4pFNlCASqCmqlUqtZvFOngq5M33H7ZWE-Uu6wGnBtJB8aevnQYIcbYPzYKXDTghTMccZkEEuo9SZBKoaEazaVvEwE1pt-5afNaLGwIRdQnytryqka0WJFidRF21qZQrGYgp6_-JJjOR6YMyj18e-1uFBCo4sbKrbmuIetiG9s4TFpPDdv_eYJrBYb5JTesIheLMmv41cZEAgICGrxJes6OI9dDpKmPk_tfeRhKXmLSVG5qNj88kcVpKi5eUa2w8j7IOvuqyxmtU3aavJjHQRen5Kav049cV_E5n4Y7Kh5irTiPNVzJL5IIOYIRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32263398.mp4?token=H2_Q_-EuvdZbJwsLT8pf8Ag-5pgq3jNQs3stmOK0Bb9iYsJ8x6gRzyukvbOrakh3fyYll7SDZGpUwqVYPX_S6nJDPM-CSDiEAmu6XT_8HDhLC86AOcLeLGk_ZB1evlFoYFTbFWEINsMw6fOpaoBsfm0KIRBJHl59mbidcMLjLCxx5lIgJ0JEEAj4Lceqki1NT-qdrdOeu6OojUp9vVsg1Mu4C5iKMJGGgToSl84dGBNBgmKl-hCPqHlI12SMUyGzgFqWizYzJ6e6DdeRvu1or1L6DT3Y4tgCr4Ya9Y9qHltE7ahhNf4Lx8v2xHh6NMM3qZfg6khB2NymEKkZiIbFJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32263398.mp4?token=H2_Q_-EuvdZbJwsLT8pf8Ag-5pgq3jNQs3stmOK0Bb9iYsJ8x6gRzyukvbOrakh3fyYll7SDZGpUwqVYPX_S6nJDPM-CSDiEAmu6XT_8HDhLC86AOcLeLGk_ZB1evlFoYFTbFWEINsMw6fOpaoBsfm0KIRBJHl59mbidcMLjLCxx5lIgJ0JEEAj4Lceqki1NT-qdrdOeu6OojUp9vVsg1Mu4C5iKMJGGgToSl84dGBNBgmKl-hCPqHlI12SMUyGzgFqWizYzJ6e6DdeRvu1or1L6DT3Y4tgCr4Ya9Y9qHltE7ahhNf4Lx8v2xHh6NMM3qZfg6khB2NymEKkZiIbFJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزاله اکرمی بازیگر: رضا عنایتی کراش دوران نوجوانی‌ام بود
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lwl5GwU2_WPSyeLM1apW0RGYIAmjIzoaG4Y9cZECh5E8YhcZu2p_QJAwTHIefPEpGo93op2Y7ttC3Hjm7PJvTlo8PTEFT6fa7XkTXkBYkROryu5e7EHHSnrHA2G0XykKfv5iqQv-5_5s9rZ56B-aU7xvHiTWfU1vUte6m3ODBacuijZlYY1raeMXkU_Xy3kUcJ5GjEimO7KwJXH0Yzfh3Xqm62odUxpbX1GAhniR385L6ngj6a_KZpqEfOzthSCSzjoh5PvtUpzxoLM2FFt4vWL1l8nUA67zsgjgST0XmoCq3liUepDph3WatTu6QqW5qYxmPEqAmhHaBXioEP0i-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQUrjA11MZubmEyqcAn4iqMlwLNQvajPRbX9M_V7uKDvWYXrwECak709F4RRs0vntqirshjMv3V2OcMjQa2cvJGxJeKipBYXEdNA6dJSkmy0RP6-iIYJXmV2uCzrNEKCB189WM7_-FcS5w0NeUeo9tQ8zQebRmlq90c4KcvkdzVCnT5CgiGp15Uryn3uhGJMhbs76AJA4tw4FvJwCicuZCzjiwyEYO3H7aF034MWpsT8vdfdNR7UAuhSLXl2qutA96yT5SgUe_lXxo9ZOW2KzgglrDMrtZ_TmMw9VtdZCe9_MQsn1VDQQR5Ougj6OrBi-S55pM4nQYcmEjruynG2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sChJWF5oIqWhzwWNzfmoEAPh0zNCaca8H2dbM9QBESmABJVxkZlWLKFD-FtaWuTvmUeoNUG4zRx4oOlVMmUpX49nhFcTk3DqAR0SvAnJxmdZUCWb20-rhQTf-V8oft7SFWCL2_AZjGjqLp-_XZAkEQj6iGdg7A8v_-mmyCoIJsbKM2_IjZSTBRQm_yNpRMus1qnrlIjCX6FfdYatryUaWDSWwyxvMV9rIfftolJKGtke87OvNdR7CE54OlPNmizb76Pz5SnSK9G5A1SCyNqnPOSeGEhVX29zcZM5UMXXr39km8oSvZ0IPIbVjEaZfCSXoqByPKu19NKUdBV1qaxpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=Ppuw877SF89XUEkTsp5yrY81aPaMBifrt8rHcuxvTZp3r0UXwvxpiMfSZ6GMHhKGbM-95C1ekuse2FkHvBSbLe-NmQg8zV15Q1dgPtzIMvDDETN1zKhRPSBoWu9MePSRSbA8LmP2ciIe_H8BWEPql_PHNcj9jrc5tolXgHoeoDCmdY6st-TDGaOabJ8CcbSk-ubkecZhkLbBKCKMn0IRCdwmL8R8QXSFSWuyQyW2n8go1wu4IX6nV2Ux2oJZ8QMQKG0jsh5tD5ODYKvqaSInrELeEUdzKYYSCZTAuhX4PLuTyigECPVRsY5kSA0yBzR9LCuloNgDotolULFo3_RIzr1iVg1LCexEeKwlQx75jeezp0PgLPyVJDchwNJpR1sxYPmBe1_ZXTMZL9MRx9UH2D_AyLD4zYYrBDZTkNH2-b2MO6hJmngRZfMBL-9NIMHmqJ9mk08VaUoO0Opr5JkJE0fBxrnWYfgw-_NRTQqxC_gDHxV4a2-Afzlo6RAOjAyP0vKa21rdQRtZVmhk1O7ZvT7kf6DZqNGVbUQf6kta0nBlIUzlCN7luIX1ZB0I0aS-3T_dvHaTfGhxDtWLz56MpMhg65_77SOayEK8tYK7kBnRT0FWpary8MBBqjv1XdI5hIffOZXdnmSTUNRQQ0BL-_M11XHMkEttMYyqPsfMEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=Ppuw877SF89XUEkTsp5yrY81aPaMBifrt8rHcuxvTZp3r0UXwvxpiMfSZ6GMHhKGbM-95C1ekuse2FkHvBSbLe-NmQg8zV15Q1dgPtzIMvDDETN1zKhRPSBoWu9MePSRSbA8LmP2ciIe_H8BWEPql_PHNcj9jrc5tolXgHoeoDCmdY6st-TDGaOabJ8CcbSk-ubkecZhkLbBKCKMn0IRCdwmL8R8QXSFSWuyQyW2n8go1wu4IX6nV2Ux2oJZ8QMQKG0jsh5tD5ODYKvqaSInrELeEUdzKYYSCZTAuhX4PLuTyigECPVRsY5kSA0yBzR9LCuloNgDotolULFo3_RIzr1iVg1LCexEeKwlQx75jeezp0PgLPyVJDchwNJpR1sxYPmBe1_ZXTMZL9MRx9UH2D_AyLD4zYYrBDZTkNH2-b2MO6hJmngRZfMBL-9NIMHmqJ9mk08VaUoO0Opr5JkJE0fBxrnWYfgw-_NRTQqxC_gDHxV4a2-Afzlo6RAOjAyP0vKa21rdQRtZVmhk1O7ZvT7kf6DZqNGVbUQf6kta0nBlIUzlCN7luIX1ZB0I0aS-3T_dvHaTfGhxDtWLz56MpMhg65_77SOayEK8tYK7kBnRT0FWpary8MBBqjv1XdI5hIffOZXdnmSTUNRQQ0BL-_M11XHMkEttMYyqPsfMEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
درخشش‌های فصل‌گذشته لامین‌یامال در بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap50rvTiVleX_PK6zusjXmdq49VexkkU5OWO2dnuv22MO0cBJ3Ka8ylrKSOytsrgmyxFTAIp12qZmQZMB9An6q5Ul9Dh2TV6F151hmdgHOIhTZuqR-EvcJ6SxiT4LKPDv3iPFwhz5GV9LZIBpcXrmTXwXAviJN6At4KBmv0hZocs9zHZg6kr68JislmNj_j8hsk545cLGuCu8bnUwvJILihN5oDddnW57UkThFIs1BCLsdVMwlzGPAY-01i2dz8wwPWa5MMVJo08mAmWgwlbtmKAUy5zhF8Ybel3gtYFoolnRG7WFJLQzF8AGSm1KTN-f7nZth_fw5TsS5Is4SJyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102058">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLipo37XpQRJjMrnscnAYXoqEfri71pujDL5k7G6bl76kaqnvqlgACOqEYvfRbwBVHteqZirmXB053r1AaW2MPROLO9F60BSBzP677rU1X2kdbqyfqswCMFSSjDmLTjE3ONt4kQQIe_fWsBqNZ7XIoBLe9pqV2ld_i9ULo12ECr7lOGT3WgmY66ntFrxJ5glanmx3z1tebaAK4srROS9HRc060ropQRHNUQm2nPkseHBq5cWIA5T_P6kNCTrbewPlrwZ3fBrhXw30H4H9TccqgNyZnxW5DBrZRfrK04AYCnaXYy45pp01qDYwCSH-HhQ6EubzqrGhtWa3CwUgzcu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olfgU8RdiVcLsHfeiGMsAO7ClXoANC8-2Xranav4Wgk18KM5UfNlFBHX7Habs8zabT2ETZpab2eQIwVWKO2W1YOwl9-LJslyRgpp3PCUB5wINz0S4WirdASasMNUWnxBr-BmQ4raXwgxlerM_mrUsnFC2ZaKcJhYWBMgqBgG6RGtnxeHnwMCfIzYI_xxmkTlAkoaPLwLLLz8CksXCGEgfWEnnjTXnVyLN8tt_V8EueOCJxdbFt5xj6wMzbKs6f2at1jcUszFw1cfB9053c1LXatw3tz4kEslnAIxyPzxhptFQ9BnwPtfw9HBC_CxOWUcMGRK4ocYZ6EcTITxlavl9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
نیمار:
وقتی در پاری‌سن‌ژرمن بودیم، از مسی خواستم پنالتی‌ها را بزند، اما او گفت: "نه، من برای این کار اینجا نیستم. یا خودت بزن یا بده به امباپه." او حتی برای هیچ‌چیز هم بحث و جدل نمی‌کند. آدمی فوق‌العاده آرام و صلح‌طلب است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102058" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102057">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772e430691.mp4?token=oMz0AeB5Iq5BtLiMfpuZ20Lf4WlKK3QxdsYL2PNQ0tbSpT_eqwibMuq43uySvg9LZHLCfwtFmpWYSzZVrge-e39OhKdEy0Xj3eczbe6AcW1mPTZoeFiMrxeIc0NnpRH6rJ0_GBHJ8L9cJTduzNJWLXuIB-t28yR9dtHFaGfcX3RRTZ7I1eGAEm0geZrBl11MVNa1sc-wQPOxQuwN8NAfZYWitvoNDBV53BWsS1EECr0KdA7fM69kx7EVCTip1D0rU6izSI4dTw6K513qODtlKcOQ2QfzKTjzs--oE9-zkNEk_MBIjRAI2KM9dpkqR4y5ghRKWDet54sfUFmckOXu-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772e430691.mp4?token=oMz0AeB5Iq5BtLiMfpuZ20Lf4WlKK3QxdsYL2PNQ0tbSpT_eqwibMuq43uySvg9LZHLCfwtFmpWYSzZVrge-e39OhKdEy0Xj3eczbe6AcW1mPTZoeFiMrxeIc0NnpRH6rJ0_GBHJ8L9cJTduzNJWLXuIB-t28yR9dtHFaGfcX3RRTZ7I1eGAEm0geZrBl11MVNa1sc-wQPOxQuwN8NAfZYWitvoNDBV53BWsS1EECr0KdA7fM69kx7EVCTip1D0rU6izSI4dTw6K513qODtlKcOQ2QfzKTjzs--oE9-zkNEk_MBIjRAI2KM9dpkqR4y5ghRKWDet54sfUFmckOXu-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جامی که داری میرینی توش آرزوی خیلیاس پسر جان نکن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102057" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102056">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwtbYgdT2wmo10EvZmvSzTFc5VYiGOa-4uS6QONHfn8upRb8smCIJRVWXFQJdcB1XfaF16rUOTKsF4zm994BxmKveuORph0AjRGikt2nJOI87Q63k4S3axcSX_LeOFcoAWUHpAKvbfinCA9ENUwhqXafkYTrARVGfhYu8qbfSgzOeamoXnZcZN4nuTLNyva3uhOqHNe2NvPxlsZRJZ0Me7YGInLvWqThKMsuERAEk0XUktx5tdP6SC_Du1dzmSHKKxKlyvCDXH1Ju9mgW9SnISlnCZe5jFe51Sgl2EXTLX2fottxBtRnocnIdlDeDDk5p0n7F4yIoKJkQMf1J3vI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
بنر هوادارای بوکاجونیورز برای تیم ملی آرژانتین:
ممنون بابت تمام این شادی‌ ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102056" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102055">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.  HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102055" target="_blank">📅 12:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebffP0JjbQ747RbG-W2N4qx4aM0NvdWinoQ9a73MUpQrrkYp-F26pbxoL4SDUJcm0zY69_-qjm4dlhodKuADiW5M99KatHxU_Nl6Ags-bj1_UE3YFosDU8ytZcOk_rzj2OLeGjRZMPktl-xYnvWSvk0FTfh6DZAtPYVx66D3dBDu6ZA5vbCQ4QxBd50stJB3EhNH2xVLy9QUXjPbKBL-5LpjnE1gM6kOUgK7i39hdohPdCibVCM1N2gvgnQ47rNv5Z6X3N4SlZIzcF2QsmC6C_k-JrCElmU1dF_52x6Cpzq3u03u5F7nn0gtScnkFwXSOZy5U1WC00oNCO_5b9q5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChWiwSNlUgBsASpCasJpnNAivaqFAflA6zuiz-x7oZGxmXGn8Hf3mzDtZH5B8qZMnN_ysCGgPWD-IMdpLYIcIrWt9YCA8VeiW6TMGR4pmN7Bki_QPeEGp1wD99WfoeUB4784yl2cvm4wTp0JPe4Y9E4RgR0OHIu4JAUkd-Q95GhoCxlNWa1-fpXFtDV_HLKKkmOHCSUa0NC_DhrNaEEAtwzg2ewNO97BCjUf99d6jrBHSfGk1IO_iHbU5ZCOwBhGbhkHwjGf2Y8YVUUW6ET9MuRS9pG6C6q_cT_7MjmhWHsZ7zvVivSg4Kd4WG_ydzLaC02lP_tANHKeu2TNr59X9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCE4XnxmTAfNmJ5hRr6W3ajuo-_PnjnLMuEFzwhnqAE7HlLSdxcLYYAh2kQDHRLhTwO5NglIBF6_irEhvU4zzxFmyIbWt9L6MCB9S985e2Di5VTLUhgtxQLPQHXvhnNcWRA78RVWNb-VayM0GKQt9p5eCfJwtElfLfsjFErWa512ticBcJvaVhZTzVV2eQM678eJ-O-CsxWw_TAsRWkXMJRSMW_A-ftVPKSMgoQjO1oV9ns-5ndHXKKQu1kAWEZoKJxNm0vwF7Rh5TLFsnh8ZLl3FSjU-DgLLUwy2sNi1k540PhWGGfJXaTidFWmJp3VXiyOvtq_S8ioTo9WD7Tadw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=VouvFJkG23N0HP8tXpaFKUxovjucc050dS3Ddoy7Xri8O4Og9PduEjRwzRrmRIQOQWtF2tuNXkm0km5Qfpu5gJfcayO2jOzsHjp899Sy_jYxLgUyrdLcUfjMEIInQFEKWIf6GKKy6f-IQ5YN2Lk5qknaaQBTSsFndN5HN7fMassbxDdf2X2IeBmnCyiQNnZP0tBziDaPiiltG4rSCzQBoYtVpdn-7d2C5x-WLdyBuU5gvgUWUVBNWA9hGWkT7wq-zX-HQ29toHb3xEJu-id9UaIvjkjaNss9sH21Lfh0uBw1gUWobFM8upBbbXpB_RyALX9D_44zRLgOP7MRPjwipQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=VouvFJkG23N0HP8tXpaFKUxovjucc050dS3Ddoy7Xri8O4Og9PduEjRwzRrmRIQOQWtF2tuNXkm0km5Qfpu5gJfcayO2jOzsHjp899Sy_jYxLgUyrdLcUfjMEIInQFEKWIf6GKKy6f-IQ5YN2Lk5qknaaQBTSsFndN5HN7fMassbxDdf2X2IeBmnCyiQNnZP0tBziDaPiiltG4rSCzQBoYtVpdn-7d2C5x-WLdyBuU5gvgUWUVBNWA9hGWkT7wq-zX-HQ29toHb3xEJu-id9UaIvjkjaNss9sH21Lfh0uBw1gUWobFM8upBbbXpB_RyALX9D_44zRLgOP7MRPjwipQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
🇧🇷
۱۵ سال از روزی که نیمار این گلو زد و پوشکاش گرفت گذشت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfPw_DakiWIuYvgkhOksj-Eu4GrKo0CO1SaCccJc-PMsWUeRcnYHBKlL7vCWJRycWgTBj_HENipSrXXBVd143vflM0Lsqbfr6k1h12TJJ9jE-B2CvzEwgqbfdmvp_CkPjSYVzvMAIJBkUulkQ7OqbSE52s4TBDM8ou4TzhUGUNgatP8PdyzFLl_GD3tclTPzZJpsE1gO65O_D3qiNgq4wqzQLdvBWGq4Z0kB2nrpnkKIQ3YlGotOzYq7aC0QHFDWgc783ez7MKMxq-7CObBVeKGz28J0fr0F-ITSaGUpuRZMyMQr9SXkYSUwIlXjZ2K_RcFPd8zgEOHbXN1OjLwOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ie5Uc4jlmGlSqTlO8QPQ2aCpq9qzLSDENCQjm57D5-B1FjT8hxiNl6LRNPoOxMRDOrxMm0gjynQ1ySGYioupVhXhLFohmD8H-OkYGwphfWGUPmtIzai5Sa9XizlIrhplULpAUsn-PqFKB9luL9eMtWGOpkmbZWkbRmG8JFmyJ3lCISIeYFB8wTtqH7b7kcfd9gZ1y9dnCAUaNmobLJIc_hX1kJT0Bcip7YZhIeNM2UohRsFTol4ECRJ12kxELcP9uMblqOx2MnqB0nllEUYC9fJX0eYzi54pI5qwQP8KHMNBx7vesL1Qhc4CNKbyJhtLisZodzXXlBThReafjmNk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5K9UsvBOEJm_xOFDpseRXn35KjlBbJYm0xq3a9dDPyFr3xmIqjzHbIwiHnWFbVA5hEANki65U1E28ywVRVju9VytZGhKnuVpzQxLiov9niHwoOaborVfVhSadf-iwCSWXUc1FLVki5xTRWnQsb9Hthn3s9AuuQJf5vwjE6KGw4nDgWwyuDtWGRbjlwfF3_D8kDo_IcB_sfxsS0FwLn67YeU6vURPjLmQsFy-xZdqgou7ORDtrFm-Alngk70d_K8LZ_TNZHKMJLSeJiKAM5maDuIo84oTKK9dX1kcR2ydzgn_DXTcmKv_YkB2L4ThQtEoExavQpkl-bza6lIYuDLuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZq4GPifQ83R8SDEnhmqHe7hV3WNVwnqn286fZ1rZoEUOmqEckNJWZ3zPSSDCc_RoJdM7HdoNZmYV3pluFZazIlGAWXQqcwxsg1s0RQC5PeQG66yGHqpm9NejS9hAsHO_8kHd_FwO_xhF5C1dHEq7cr3AQLNo19UVardKnqkPfOFf3XLcOQvhwOmdPwj1Mgcak9G71AT0cYEDQqHPSTs2815IQW8Qt_oYIQJr79SxPJjEB2VBWUHkBe-N-BsfDJjq-aawJPjecWl70WIOBk-_kLQ4h8fFfEIhRYxX1A7J-KK0k-ptoVE1bxsqECIzWHrh2Osex95sl6ELnMW_QgMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MV50iwe06tVwV_Y3wtKxEd9oSEqCh21VediSr16G8WLyXw4XERdh2f-bow2e5b7uwMD20g-pe7g4BWPXmoq2xshYGJuJG0_FMdlAO30STRz3-5cBwYTagu6muo8x6rG8qMVnWFXBwxfLFTgd9WVXxqDr7fnp0MgkA3vgHM0uApE2R4QHwXML3kUMycH48HNbbBVbKwvx3jg66_96XQQbjmoP-M8ojRLmNEF7DTxI2LXyf5DyNMgqvH457f19LNxtNGbgwCzTF9BWdKNMMZ8cKEyiN8K04oa7C-Fj1udGlpLF63YQ59-pOx5NDrJYesriyZS8shPo0hGfd6Tz5AapAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ19ttLEK6pG9hIvCKqn4agJrRNORHih7x0Rvc6f8Mcg7PGSl3uO8NjBdZTzeoc_Hdddg-7JuEO23zWJj0IiEvL6e3nv9o3sfWPaWYs-lYk1crfh8Stg3xI1EmXE95eJz0ZKu_DCkZ2w09W8DI7si_I80FANAQgfkUa5vRdaM8S9Hg4IRXbNcsQo85bwAcKgIfaweQPaLr8-CrMcE6ed73sAnkxY3lazFWP_MjesO02WU4tXCdOJYyc-e0FKIvmern4QzZQy_ZUFQgjtDTQuhh2e9TMLylA19X-4a8mPRcboKjeKfmI_X68tnp3hGLth3SfShoXBID6zncUlDrx4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو: پاریسن ژرمن تلاش میکنه بین رودری و رئال مادرید مشکل به وجود بیاره
‼️
🔺
🔻
پاریس از هایجک شدن دیومانده بسیار عصبانیه برا همین با رودری تماس گرفته تا اوضاع رو برای رئال مادرید سخت تر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo71YSJ0eRLykuaF_PA7fsLFVFbcydYQYghizCJbqyYSG5JnvMoYsdceGLnCKnJZM2EXfNownDXwDa5dzx_DvHe5mZBBTmagG9kTuz9VTZeQniRP9pKgeDti0pbg9hSqHAYKN23KdfjgX_SGdKX463MdwuazC0n2J-RR6Ih5VU4kOPmixGtDtcvt9G__sMPckEDHTjjnZOJqommmCgjPVfYLhXyCeN5rC4Je-8Z9LBnwoXj8wa-8vGWz04U4JhamF7TmEO7Y2fBMATtVekdD0SqOeEUgZVfIMAY5P1AY5M95uv0PqGFm-IH7uLVTf3yraIaer14_ljDW35tQRgdQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3eF6WFMF5xi0w_zhtXcUp5TZLps2j76hX_Ab8Mw-HI5llfFe3WE7qr5Nck6OSQ3ltqlcsQk2_qwsDpSsRpq7RUI3pyi_sas24BoW2zFVBEEuTOXxLJBtt0Tf2oYKhg4rBIUJnRGKcwjvis2bgmWWd-TWnAgxP1Tkxnt6HoJ4OaN5zmWK1epZNyA65GO0TMcwII2vS00aizyvEd892nOwTtHb7Qn59pq3dmxx-tRhDQJ3BfQTvl-vJRB1kHLZ_b6k3XfYXN4q308JSKa8-5OfknDoRHavrxJqRfTCeC4jhEyOeXJxNmbjGOk1rnVIC7IDoyTr90CCUYv7qGxOuzLKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTt9dokoU-A02FqQrxqvVgDT9QXIggcdmC4zGnXQ9v6BvTjbG9AD4ZokiPz7MFHsKtczKYDHnb0fGv7SXXHX-9nTXtQRMw914RBbwv4yGXBKBprxY9-t1qoq10S7-G01BI5zmVmtXk0q2E3aW9vAzPF0tyeJHcKTW-3p_QJkCL8DhUU_fhr-D1vF6eyKLfOviSmp6wUgoaGeKbTLY1M1J-nfBSXRH6mrQ4-FQBNmpsz3S0Wj5Wm-rz2JQ1oihU0gPzFh4mEtumQpqcS_B9ATRFD1Y7US3VKIhY1Iyj0Cw8hBWcdKnZ7RGaRPR4r5CpirXT0nSRCgSJKQZXfo3npz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWgI6838P4f6mKZen73HzrvaS2x2vlkXfTjc_OHuA_VL1Eo4_eK_kT4IzyOt_-r2jlzid3GBf_IesQtggV_6wNxmFSyGGej-wVihsGEaONk9VKA5c72Ig9t8Wa8XpYvW9V3Y1nAvFYTr66LQBijO-QjgFa87ep6_Yn0GYrUMj8hiFryEFbLtDLbIR939KBkoZyL1GIdj15wVtK4xJ2AJslJTir-MZigrT67HRh58ramzBwPn7B63c23H1eo4bGZ4o0A7Gk02UbUIxBlAL8L9tpyKozcBPrCcDNWtiHlP8u8LsGVuJpwD2IdqQ2cTeuibKQqUH3Sy48UcY1fKNEhYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_rim_tIw7z1kYxLoiS_qn_rW94bK0XBuMMDpNcRigaatQZpHzC3vth5ojZnH_gDRzfO0fZtG2pRepMRfxjaP52h-JTc7iMb4LVz2rKpnN9UVGRAeqzuRvnS9L6bGqCyu8GKsP67sr0ipeE-hlIwJ08zO8-b3V1hVvIEJlKubbrYe_TAvtL_bNbYGPOQisSfNQSwViIekgM_WqC7WDa7iKE6nSLEkGjgctXuQcq5A8AwJaU1CeCypKR_QQxBJe-A-osOKoV4P53XF-Qbx4AfkrFSbnocSc3Wpc18O1QBDpOFmil6arkHpZb7inEnzKhTkoQVuJAZ3hf3h8mihU0S7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyTThOG9AwDcsmyGYI8cbp3HOj7S_f2Ica6cCQWgEKoKg-klmCACPfVus6Eu8qACVZDDKoMApbU5dGGkyFyLCyzuwR3_ZAjZYkGM694hDFHKffAkQpU06LJIh2MeJJmPfiarH_XjIEkNFDTHw0gwAa62ks-aBqw8wxmwgW7JrEe0hNhYz-TFkUG4Yspbse8fMVzxli2nVHmzbXNDmZbafr8X1UzBbc_vTF8MPQ7i59OGk0FriQFZguj7mt2VlbgSafTuOUC9-JyYbctn3enrG89ztpiD-c0rVh3z9f13XUtdDKbrsjUfBbp0iLQ3MACyKYAjxohxjyXKguCG6gYpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWrrbqIYE468t1YJSj3UJjIkHjAGt6cc4J-wcAZqLBCpI6FiTXHn0-nh2_PTRlCpvzAUNSi_B5bBYR85zXKeK-EctyWcrcevL5g_5UV5bm-Ki1F8Vx1cCuM-EKUEo4hjdvsB_MgTrpwNevQ6AQ9B1uJN-i-d1MOw_evAHPNwtPJu4JPHDQf6ypVN1h3CHCCo56syXvBXH8fkaFlBv541rTp-F_yzfFnql9z72--mS2deWDrw9VVv8FtJz2B0mFMqIJi3fo1XhSccQWqoHy3Zsv4dIpsYHVM5Cw5RkWhzcuGCeDiRU0Qa7Ukl4WWIdmq1NkbJWfI3o6xOsqbcyhjXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHSE_uSbXQJUmobBU3rS5zgiXprMdXlMlbGGln-i13oZls9utDWbc6i4GICoCc3nfuTwDbr14dc-61TYyWNKpQD25_XtO0Lr_VEqyYe_Q5uQqw5AUKCp5tZPwsKVWo_D28P1qlvq2QSCuTf3nPj22VVmERGuu6q8clyQ5xlxBNIT8Bdf6xTorBZBxwiLFm9G69eRc8dAd89Powz1RluWx8qTYOLgXgBHkEDvWPTonBz7qEcJB_wU-sbf7oFHFAfbGiC7WOr6HxRqqe8F59rXbjLmV6YKb89Xr7t-0mSQ0VUXgTor4OXmeYhArISuoPCagkHU-2Y_52PjfnZPbFNLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BHGS0dIk0Tt3jkiGkavzl-oADm2Zua7i9p1pdLmmHfEgVdnlfcHyp20uPJoTesdyJ2-27xaaYjPtGhynG22T__9zRAsVvNFVSm0O-I_9YE1TOhtim-HLv24YKi5HVTvzuXLK_gtnfHL-nxmwA7DpzaVh3Z49plZmgQ9a68yd11s4p-GXTtBjzkhLi82Ugh5Ke3gl81uO0WJmrAAR5auNzETkdkLWGnQ1IyrrA0At2aM6Jbx21kekVnMc_6Amhl_hy4d0PyS5BRpakhusdE87iAlBhA9n0B7Ek2rhRp8mpCpAcDpP0LAyZqgp6AW0NqmbqYQg2Sy2qLsNESVZgFHtDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Huz5GJJLSV8Ax8Hzqo-0NWAEdYPo3x0A0ecxDZUVqMDLqQyhhkQ1vtOHFukXkikf1CkeHmD2eaMQKJzyoenjrduOMFePFwQW97ccrpAWtHVRjZuD9jxRHq2lhDndvPxh6YiCmaaDs3pA38Hq95kT4iMVZoVrd1f16cODH6s5IdDjUZGEqo53n4Dy_had-8Q1fKRGaa8DnpuLzJLjUrCVW4X4fbfcjoA_Uo6uw6_bc4updS9bYVw-7a8vyDcAgUMAnThIZqsHPQKAuzpXusvuHCbNosavJ37tEC1EHUADrqh7w0U20Sbfg4f94sBUQ9YphLRlwiYnQMKgVveG5SpT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa8UvnkUF_f01vHrldLAh4E4VdD3JzARKGXGz3RFKzsPpcM1eX2eUfoKVH8VljRLfWZ4tSQbj1YIJiEH4F__W9PC-gKkJz7qWc7rPP2EFV-iZyk9ihqLHvI8AsJtS5GUKpDCg8yMRHxgAwPHtyoJcn8O-WtdbzdMpLA9_TK4MTkQMX7kcne9Xma0iL8cetXtNFyiXqHbjX5y1y5oDfqSXn3J0rVcVw17afAQetE2rlK3W_Dbh1eJARXGuuV3QtS_nXCTHFuripIW-qmwDz5dKcO0b8zoELd09PlpYZnAZo23J1Hm7FH9UjvUwcySP-fBDdNf7OUlR9d5AACi6ekJ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=EtXiPOLft1nrldRd2vwmqejQ7dGMuSUShujyNG1y2cOH6sQFxtht0Q8OAnnruVwTAUDk9GhdmH87iSgo1aZNzAqgqIxadZ5-_9yt4b6vdqywh2LdO4k8Snhgmc7lycWYoODZGGCbSmPzM74nY6iv4VSgGtbqd3Eyj_trNh87xjZpApkiiqTEJpftT1g-djtUJKyLje2ta2RnXHkoAq7NBRvasAc3FyUaw2C23AEqP2WcPBa0y6OWZQ3PxezKiv5nlNl5vLx7x8gz-F3DQzFQuk5yvEUhUJayZmlCk2HwmjE8GJ0yhn27znOJcffl9me_-QljtJ0E88sj3JR8_XHFRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=EtXiPOLft1nrldRd2vwmqejQ7dGMuSUShujyNG1y2cOH6sQFxtht0Q8OAnnruVwTAUDk9GhdmH87iSgo1aZNzAqgqIxadZ5-_9yt4b6vdqywh2LdO4k8Snhgmc7lycWYoODZGGCbSmPzM74nY6iv4VSgGtbqd3Eyj_trNh87xjZpApkiiqTEJpftT1g-djtUJKyLje2ta2RnXHkoAq7NBRvasAc3FyUaw2C23AEqP2WcPBa0y6OWZQ3PxezKiv5nlNl5vLx7x8gz-F3DQzFQuk5yvEUhUJayZmlCk2HwmjE8GJ0yhn27znOJcffl9me_-QljtJ0E88sj3JR8_XHFRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsxSCbDGDoskxmMlPAA0qbm6GCmsP9l9pbPe6AskIGOgNdB0ZQZzFZ2ZlcKeg9sxg95QeDZC49RKcoUDKF26FqsWfEwT8j35-4VrZuxBt5Xdg2sYvFxQcKOpMu_8V8XgR9ka9Cxiuh4PLCT0vTLhbq-MzQ3p_cDSrUJ21K-ZrCgF6zfGQRZuPmViOm48flAN7FLFfdy3v7ZuPolt8KVFa_ljlyC0bN3q-o9KKAgBl_90kzNB0mW315qI1SIT-rl01CT89qKmJddERHwUxoo3Z3TjeLI5FDXMfq3_XAI0Z-nL0gfuVpOHgrUCb90kulTSmK7Sj9dX98wBtt3cZqiWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg6834j19-onTZyksz_TLGfUfB3KwP4Qe1TahPuOJcGEH2PmNQGgw4IivhCxLodImPkpzXS9US0CueVpsQpemcT9ig4iN0onPdURtxbxWz6nyKDKLGD2vA10xp4qdY23A2WtqrGE1G1Ly2wSWkAKpDeb_PnOdqrl8G9MtvHc9Kqo_09m26C1rU6H_vaMJ069Rp9L6uFbjlOtQ8zvsvu5f-AeBMeva4tLFM8715B6NEOyL7QTTaEeckNt5QST0o7jr8k2GEL7gfYjfw7FoCmar2PIqLhUAk0XjVNaXewBB-gR1vwVOMbF7xsVW72qbANiCsCCA4ZOLdA-fOhztU5CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=dEMdWHUTzPVrAitDx5eMqMu_DsZFbn6YzvlwSg6PYBD2yQj7gyCFziTQOlkSYThPn51NCnIx_FxmPDUsGk1BLQ3EgALDUqGntTE6sWu14xkYhwlUqpAL8aev6NXGSjXFY7d3lylypGSROgqGTaodfvz8v3f_h6tlc6GVgAGLJvM5TIsQBIhT5rn5xuKJ9qn2dXJbXidqY1iH8YQI4eQcA-ru2gJQSG0-TBMV9R_4arOaIygGqmF3RRcbospymVavh8KdlOaUad2OjG-uH5AkPa7VsoFpMurj9r6cxTu8MZCt0iKneoEzfNPOKx-UESPeCFuNocxicIcsZJVnGPoKMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=dEMdWHUTzPVrAitDx5eMqMu_DsZFbn6YzvlwSg6PYBD2yQj7gyCFziTQOlkSYThPn51NCnIx_FxmPDUsGk1BLQ3EgALDUqGntTE6sWu14xkYhwlUqpAL8aev6NXGSjXFY7d3lylypGSROgqGTaodfvz8v3f_h6tlc6GVgAGLJvM5TIsQBIhT5rn5xuKJ9qn2dXJbXidqY1iH8YQI4eQcA-ru2gJQSG0-TBMV9R_4arOaIygGqmF3RRcbospymVavh8KdlOaUad2OjG-uH5AkPa7VsoFpMurj9r6cxTu8MZCt0iKneoEzfNPOKx-UESPeCFuNocxicIcsZJVnGPoKMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-Jf-JDFYT5hmzFjQoKs4JmLlmoPVu4ar7P8xJCR4KckGrpHNOWgX_G_SzdWzabmwMBGHLBDFvjmlTf_9rLStKBzL86wLdDH9bH3bbIAcH2O9lNMO3iZ9JGYoPTvSfxEeKMynx6rjPkOYpnhhb-K9i9hf8ykdwLEZorzGLvgbWz3yewPdGjfYlI5jLxixaKNZKRYD4X72Ru2fKNgYvtreJTAzaQTIruILOXCnhoWR39XllTCLE7FJx745MlvsbK_agBM0eQPeFCaV8NstUc4viHOirwnlVvuFQ2-d5CoAl5B6nXip13iCf7qHRL-NHjY-fSY3N3bP5eVXkTPXrM5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7akM1nsPOQPdQq40UThZrzimtRHiV5G2c2jjLfuaMUYR68CktDIGCI7bSdYWCBydryz-PhCemq2c04aXuumGL5xY6otk_0Her-HiaE7nicGREDEHUKmgxsjcR3LqMJoSQi1wPxRA9HcgC2jvlJgJc_DFtSyoJFyg4i8BnZXggH-JZGne0VvmLtwgfflSlRS0JQ7I996kdeV9XHbz-SdA73GkxxCxNB7LdzAtH0X8_57Op5wrUnJYNaxDJtMEnmKxYdO4Nu6kMlVP_rk9FMvM8gTmnvMgXwosEaCYjyr8b1jlgiWEx72EXFNXGiQT6pajE1-ICqPzEW3uWsNhaxFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3FoT2IcQaQfdDpg0riZpW-BtKr8o4ToHw14lClyoKbswHRD1ciyDrmfdJJoEIgeu4W_m80aQ8q8vYJMS45t6fG9NsjnvYlRvs7z30bFR4ukIt7HvZusRh0pg3lMFfvGGVX-_gTx9fDZJNBd36b068uevnBOUk3utMor-xNIpI__sTxDoiqpr4ZfQgIPnsvP1qjRQRU3m_e5NS_aWAylNeEvtH0ugmmx5tdParQa16x2fF1nG5z1JKt2NkBQ7_sa6B4XyB_uvs09PoVzKX3c8feP25iByIk1UtpoEtBcB0b3Fuq0VdNBWTnUNmNVUdEeIanYYnAZx8V18f_g1xiSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsoxNlju29xs5yhDxU3V7X_k0Ye9pVSVP2Bg0MxQ1eBmRD9TOq_cfFskYMQ7sZ6rQwqvzxd7tsng57mpYfIbytTe_6krCyIs2aPqkJCTi62PI4MLZzE5623Y7DWAN-nI0yv-85uUxdfo3TX3Dthu3TBLZheaB4ZHY49cqrcCm4h-_vq9YC_DINDLTEHjUaKScLA9ZrNUCdiQimr80Oxmq7iOlVx63oo4I-SbzW_29NYs4mwgeiM6Lzm-QSmRVi586Tu8UZ8kC2Pj-cMjNRy7sscp3qvcS9NRkY6HT7qu34VD5ik51OsA1FrubFTPMZ25D9dqpLjrIZdlamPo3367ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی
از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست.
𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNtM0RqHP3dW_GfaYJ2r_0Prw2B80aAR16G66xL-glT3ZVN6DOV1L1SoT196vFCGGkUP1-Grof_1kDSQEyOYnCZEjqV_wKEehM8zyWyr514u3FTMgvDMDPuAQOsYID7LPkWwQkVnuwaR5mqUgLvhXRO81t6UzZy8uy95pNP5epkp1iDS-BocQhxcSnwxoUoLfS79HmOZR5YZfj4fp8SpXLCb0LgoaueXBwuO6KeRJrJDkXI9bTrQh7ZMheR-sB1o28BISzKItJkt3g6JcTK7LIxe09uRtRH4rIGdGSoUb8wjQYn136OcCquwd_GAl-rXwAsqbZduuRzgo2uWMAYqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=XIEWabVqC07DbUYaEQxPZC0bxF-k_CTlKac6aYNzvddNe430gVjjuoZqewmx63DwVERv5QhbI_Nj13hwo2KWPJrvOHUzZniaSWSz2OMqSNB3uODdIIla7p3SHJeUhmE-ptxWvpgQECuNnHwSzQCLrL8RlLlDhJcxhc74-2wcOnSdBudCnSyWcs9EowzjVU_wMTHt3JuIYK-Er69ciZdWOQRshAp6udMc6hZkvj6y-JbH_8ICHogSIjysDx014702h9RTBb4HdWUF77A3wzztluy09dZr0FjzrnJPnzNMAnLS_-p-kkvMN3UQ4CtJhfhdWv4bLxiASKk7159S6EoEJqnT6WqRpq2isM687MEscGWRzbs3F-mbPLxtmfeFIsuC_Os_hXiuE_kUGJo2kyvre9otmSUPj_Ibv_XWOnoAydldJBOkczTdOINYX1U9n4wMGv8hJKNrJbPdWNnvSkl8WbQs1uMw72dFtyuXSiurZZp0BMxIlj4BAjwutmyw9ntZ-mGS3_EwhqyfIjkLbQoz6NUivDq1G7tbk5-wfVEd60LntZH36ft-PTsBa9KOH8j5eXatWyC80G7FeffNT0jXqn60W0VYmKXkqa5TpvFCSreJjBQHxyJzYuevP81C7T63-EvE9tLRMJim3CZqWwCfJ7Ekksp093wvrJAc7BwRkg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=XIEWabVqC07DbUYaEQxPZC0bxF-k_CTlKac6aYNzvddNe430gVjjuoZqewmx63DwVERv5QhbI_Nj13hwo2KWPJrvOHUzZniaSWSz2OMqSNB3uODdIIla7p3SHJeUhmE-ptxWvpgQECuNnHwSzQCLrL8RlLlDhJcxhc74-2wcOnSdBudCnSyWcs9EowzjVU_wMTHt3JuIYK-Er69ciZdWOQRshAp6udMc6hZkvj6y-JbH_8ICHogSIjysDx014702h9RTBb4HdWUF77A3wzztluy09dZr0FjzrnJPnzNMAnLS_-p-kkvMN3UQ4CtJhfhdWv4bLxiASKk7159S6EoEJqnT6WqRpq2isM687MEscGWRzbs3F-mbPLxtmfeFIsuC_Os_hXiuE_kUGJo2kyvre9otmSUPj_Ibv_XWOnoAydldJBOkczTdOINYX1U9n4wMGv8hJKNrJbPdWNnvSkl8WbQs1uMw72dFtyuXSiurZZp0BMxIlj4BAjwutmyw9ntZ-mGS3_EwhqyfIjkLbQoz6NUivDq1G7tbk5-wfVEd60LntZH36ft-PTsBa9KOH8j5eXatWyC80G7FeffNT0jXqn60W0VYmKXkqa5TpvFCSreJjBQHxyJzYuevP81C7T63-EvE9tLRMJim3CZqWwCfJ7Ekksp093wvrJAc7BwRkg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt_ROmmhbo_7jnQgP9o2S3GRJ73SPHeZCuuGx6cp1HNbVdklaOaLNoVWL_ULhW6QK_LWmk8XNjTWjM9B8X4iKBLyPJQNZlV4_tCY9sadAjYDQRwRE6Rhv81WPlHRWPmirSo0bsa758so_yS2f3ef0o-Xejdmg1ULI2tI2A61wg7Nt58DT-YHQt93pZPiyq7N0bZiB-otYLocSBkownaEeJFRnjnqGxPYrSywAhYEGONOq9bPYdrMTPT7ykIhhsrmOmhAWvwTakM4pga8hrlfmzzywxpll9ICHg5oLBqQUtxF14uwYHXLdEGTi_4rvOiwLdWlxUh4x70i4wAHHx2Rzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5zzliCY3XhrOr2MesfXcMSwTkDEmBEKk7hTR25U_BJZOilYk9IZZQfv2hQZEIPOBznr1i_IvAi7po9C_X4D9pwMmV-D6DO83LQLOjISwP7TaR9j2LDeT6xOwRckW1EKHAkhaIAv3xAYPRcHt0laCvZzZ2SADfkt6RIA1zmeZ6IVDV4VplJYY-gGnbtJ_l4RUaCLIsxhAz3NhFaKc1d0C85LdtDMYDlTWA__ZUMyUeUrfqESPjA2v-DDMuzUbpEEgmb-ddfh64-r_7Z8ax-FhQzNZe-GFg7cK2a8L5urkZej3VKNBjYoWX605c76umlnGy0NfelYf5-J_m6qEcsc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHbzxP3PyEfw00dGaBnWBUvb5V3hBIKx0pDKMZuBwUwbNeKBiJNBFqQ9jUsn6yMpiYlFvsFR-2SpczG8UVyLRs_MlHCzP4ULVN9lGFp0juFhDzhI3wsymepoqA0ilkiYKKGJ0kEiw0rZWNQ7n32JVm_AE6Ay8fAx7MNqEw7ZY9_c7ZLR4qeMQvn50UUDVY63yC-4SldaXy6d-1I2F_L2v0Aot-FYmYfdQY_5PkbiSxLODsJIutqx-Z4M4Ibj2hzTeB88tM3ruzncdpttulVODbm-kVcTr0y9Srqsnq_9oqPnYc15FZRJncTmqDbzdeT71xu1I6cy13wRQNx6OglCYRu1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHbzxP3PyEfw00dGaBnWBUvb5V3hBIKx0pDKMZuBwUwbNeKBiJNBFqQ9jUsn6yMpiYlFvsFR-2SpczG8UVyLRs_MlHCzP4ULVN9lGFp0juFhDzhI3wsymepoqA0ilkiYKKGJ0kEiw0rZWNQ7n32JVm_AE6Ay8fAx7MNqEw7ZY9_c7ZLR4qeMQvn50UUDVY63yC-4SldaXy6d-1I2F_L2v0Aot-FYmYfdQY_5PkbiSxLODsJIutqx-Z4M4Ibj2hzTeB88tM3ruzncdpttulVODbm-kVcTr0y9Srqsnq_9oqPnYc15FZRJncTmqDbzdeT71xu1I6cy13wRQNx6OglCYRu1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1Z5RJYqU0itqrAylG3Pn7gwGkwJ13vjs4CzPCCq3W7SUJ1WH9XwDcdwAVkdWbMzrctbz0IFFLkp5aVdzrN02P4ISI3ff7B4vWs5r6shyXlRIlASuK4jGbAt0PfuIsp2VeM56MM7n9nOuOdk-JAX45HU8Kj_XLza_1NJ0y3eanc9b9PIOGI2stbRtsf76EcOYv2x_-ioikDWz44Q2S0rOOZKelCQcQtAKfaJ9EuafwKI8IIcpTlL3Idd4V_DGQ3F7dFzkqbybboxBwtM4A8RFRWxcsAdLVi2EVmbniCjrk0HFKB1Q3cBDFBKG6tHUHIZFIX_BqxyT4QRMzdSNEtghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCT9zj2eo7fvKACWgr1Xi6kCzJZFm1H5cOtOBOZ4cgxsn2jMhYO7Ckf009Q0ccStHnla49EpQzMODLI4pdE8rtqw0Bi9JN6V_8nx1fstKwO22b9EhWxpd8Q5NB9VeLRtTe4KhYbhhwihGCUAg2sGo5cW8np1c_c-XTas-z6VbUdmB8LeCOoWdTzMxqkxXzN4eTG1DqiWNVU0_DJsb69iUjx11Nxc04u2KJD_fO3pInNb9F9hH75f3tICaM2UnmDkNtiAscr3Oo4kZmttGHCpF5Xem5JUt5gNt4QvYoyB8TYpg14zaJZ7_yOKHxvFzwrVgMah7bRqFRM2H9SsLQG2Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8Jm6Ge_NIQ5p-uWg226N0wg9FggzLjdFB0ruWc74JvvjwKiFtO5oWQZBLkPmYtPuIkApsVQ5iOVzBsFps6yFTQpcOR3XZDzfDbTmKEHmE7Jn87uVf2wot1uTIyJ0fz0BcdWdmOo-GOqqPZjsEeuUCE2w9quktv0ZIJ_wU4fzNKrLs7Cs5VdXYzRfjDiUkxW23QctZCjC001ZT-JKfQqyctdV6VBM_Zb1kghvy1AVnkqcY0QvYLnG3QhQefueVa5HbADF34CrZ3h91gY-k2MSriDVLFBb2oTrL-dRBEH2TWSeyQYuaRxRkAkKImVSLtWTqVVef4VXI1y6SPajYrlKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
گران‌ترین انتقال‌های تاریخ فوتبال با در نظر گرفتن تورم:
🥇
رونالدو: ۸۰ میلیون پوند → ۲۹۲ میلیون پوند
🥈
ادن هازارد: ۱۵۰ میلیون پوند → ۲۴۵ میلیون پوند
🥉
آلن شیرر: ۱۵ میلیون پوند → ۲۳۸ میلیون پوند
نیکولا آنلکا: ۲۳.۵ میلیون پوند → ۲۲۶ میلیون پوند
فیلیپه کوتینیو: ۱۴۲ میلیون پوند → ۲۱۷ میلیون پوند
پل گاسکوئین: ۵.۵ میلیون پوند → ۱۹۷ میلیون پوند
مارک اوورمارس: ۲۵ میلیون پوند → ۱۹۶ میلیون پوند
گرت بیل: ۸۶ میلیون پوند → ۱۹۲ میلیون پوند
استن کولیمور: ۸.۵ میلیون پوند → ۱۷۹ میلیون پوند
ریو فردیناند: ۳۰ میلیون پوند → ۱۷۵ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=ZBKsKw_eH4znZITljUejA1M_sqzGnJyySM5aGAZGeBtjvqh8vc4Xh_hueYTUXrba1mnxbfar2Svwmduin-5wdixv5ET6cpjo0j_bv4liGyShHEbSVvGt1kx8nT8GZlzOJCqUgjbLefp-C7bAagHnfGr7YUDfV1LAmFhU-rb_JyWAUrsXaI9_-tQ6p6gzyI7MXkTPx1ndf3NEiroBKsUjyfjRYTqjYwlIDuKjf2TJpNgnWjc3PeiaYWqX1Sw5EeqOl2PDxcbo1TFIXYRkJxLAziCC5RjhyEILV--qa4PcELK0l-LwzNpEMb9y1C-KCDDNlmQhfx0Uscdp0-mWABbQGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=ZBKsKw_eH4znZITljUejA1M_sqzGnJyySM5aGAZGeBtjvqh8vc4Xh_hueYTUXrba1mnxbfar2Svwmduin-5wdixv5ET6cpjo0j_bv4liGyShHEbSVvGt1kx8nT8GZlzOJCqUgjbLefp-C7bAagHnfGr7YUDfV1LAmFhU-rb_JyWAUrsXaI9_-tQ6p6gzyI7MXkTPx1ndf3NEiroBKsUjyfjRYTqjYwlIDuKjf2TJpNgnWjc3PeiaYWqX1Sw5EeqOl2PDxcbo1TFIXYRkJxLAziCC5RjhyEILV--qa4PcELK0l-LwzNpEMb9y1C-KCDDNlmQhfx0Uscdp0-mWABbQGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=v3xwvfRAl-1cxgZM-Nv3Onl13Lq7QmqDSHy4KTaIivU_SqAG-w0E-WJyXBX2-G5NDaIhYOVj-CzdKo9d8YuC860CzHYTvXzWqxK9vcXFFPOQBVG58fxfVUyWPGhNZ0keiaL56TuH3srsEwKk2CIbN-G3UjczG4U_zgfoONGrpV-HomRHwzHhwcOIfU8T2IjzwWWxa4tBrYLalvAo2DufjxDqZw_OEBAAE6shc49zTtZ-cpGh-nMYpCPp7WXehCgT3Za4UYw7dvLbWdxUFZVw9OQ4WlnfP4n9SZp2xgAhXFytY0nPWnf-erb8KH18LVzt1Cn5lvDOUkQG2JhddelYFSgk7xszYmwWooADv7kToikWhn7HyAUnQrZjw9KMnEFVScWEXyHWufUcAqejSmZXm-E9ZAk1uurnHvBI8UQ8fdnjOdCaTqZ-nHRxXV6qUXAZEwhlH6Q4elDPQ7548MrCykKDMFrmOuBuRcjBxdyvPQcgBelhot1bJFzt1ewh0TJ6uIuQaAC28oNpbgiG5wnqc3jnJVv370jUdawYYYm_QF2cCZVueAb7I9IDuFfDSHAVlE8aPzFXm64u1eXS_3RNmLzBhuEwPaQugFaJkuKxKfDUaS_fT2VpX4fLVX5510Vh69uGmNdNCWLWWPS8ylK3OTq0mIX1M3vrA2Su1Xdx16A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=v3xwvfRAl-1cxgZM-Nv3Onl13Lq7QmqDSHy4KTaIivU_SqAG-w0E-WJyXBX2-G5NDaIhYOVj-CzdKo9d8YuC860CzHYTvXzWqxK9vcXFFPOQBVG58fxfVUyWPGhNZ0keiaL56TuH3srsEwKk2CIbN-G3UjczG4U_zgfoONGrpV-HomRHwzHhwcOIfU8T2IjzwWWxa4tBrYLalvAo2DufjxDqZw_OEBAAE6shc49zTtZ-cpGh-nMYpCPp7WXehCgT3Za4UYw7dvLbWdxUFZVw9OQ4WlnfP4n9SZp2xgAhXFytY0nPWnf-erb8KH18LVzt1Cn5lvDOUkQG2JhddelYFSgk7xszYmwWooADv7kToikWhn7HyAUnQrZjw9KMnEFVScWEXyHWufUcAqejSmZXm-E9ZAk1uurnHvBI8UQ8fdnjOdCaTqZ-nHRxXV6qUXAZEwhlH6Q4elDPQ7548MrCykKDMFrmOuBuRcjBxdyvPQcgBelhot1bJFzt1ewh0TJ6uIuQaAC28oNpbgiG5wnqc3jnJVv370jUdawYYYm_QF2cCZVueAb7I9IDuFfDSHAVlE8aPzFXm64u1eXS_3RNmLzBhuEwPaQugFaJkuKxKfDUaS_fT2VpX4fLVX5510Vh69uGmNdNCWLWWPS8ylK3OTq0mIX1M3vrA2Su1Xdx16A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBFUJna6LTTORDP3LrvTgjHKMS3WLYTBtbZS6_hwXWEld61hAYC2QZvv3Kh2qCgzqWEHsKNZOwTjJuuOKlHsYSeBsaB3ICXCrARJN95isLdtiCVrQnvHPUre_E5xAH3TUXHPK8RiWcrkGmiWr3UKlCw-e940dUIUkdXfHtveFvUNmHu4BPx4ye744gjOUmquY27lOCDnO58gTHCEqm2UEdCEK5813ofwSmBAhY_6xrl8PR9tOuknRevBVclBlcJTML7HBPLAiD6WXjqCC3m8j2J6b8Ma9jlK0qafLaOpW7UhzEfDJ9AtmQjsiVB0umUBkD1J19F45hJugAfXRG1R4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=hicMlUajdhXOc099BABeh66TgBfItQ68avC-T5MqDPkw7x3M2a8Tt4-15nn1BIxhSbESIyYZkNWWTGKwnu3xWKpGLkVvB2N_YpW0X9OAmOIJbWOJee1CVQ7hJj95cuLkmd9ejv8J6-toVIyK5hItCUcIwd47M-8saBD_NaS52F13lKlfmxuhokGxXqF40N4P7WBWJ9DyoR1cfBdeZAkzCtHpnJA_deQIc5NiHqQoV4QL-1kMoEDIWXUPRYcBXnpWl29qajTHgD9Z7MvRey2UGfgdk6L6NVaP9FwHMXjswmlTIcqprPfOSKK063iPznW_R1KyBPN9N4QYTM6Ej_fUIad_i49Rw5_Z4nfu5G_JRz_cX8pFG_iG9HVQRE0nw3GHH_N37lnH56tf31ejf_Uy-_7bMwBpXq2gdwSlKNCsdFXLaGPaHjhw6HwAupWREaOEze0MnaPgeaUAIFcvv0MiJNNaG6SyVYKyYN0tDse6kriRXNRdXyjlzsDEKZ2CKv7NmgM6fsA-epvnF6aRXFF492A2yA31OXKvPC8Utfgrfs6QACanxHdk_y5xMPH5m-TbrKu80QjW_Kit89v7xRw4ulHNWGxiWyk5HaiLok_nNKzi8jm7Nv6LMRDOtRS_KdTXgFpvao-QSXjjEGFzVLth1bYRMY_qod0jNlvr8_K28v0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=hicMlUajdhXOc099BABeh66TgBfItQ68avC-T5MqDPkw7x3M2a8Tt4-15nn1BIxhSbESIyYZkNWWTGKwnu3xWKpGLkVvB2N_YpW0X9OAmOIJbWOJee1CVQ7hJj95cuLkmd9ejv8J6-toVIyK5hItCUcIwd47M-8saBD_NaS52F13lKlfmxuhokGxXqF40N4P7WBWJ9DyoR1cfBdeZAkzCtHpnJA_deQIc5NiHqQoV4QL-1kMoEDIWXUPRYcBXnpWl29qajTHgD9Z7MvRey2UGfgdk6L6NVaP9FwHMXjswmlTIcqprPfOSKK063iPznW_R1KyBPN9N4QYTM6Ej_fUIad_i49Rw5_Z4nfu5G_JRz_cX8pFG_iG9HVQRE0nw3GHH_N37lnH56tf31ejf_Uy-_7bMwBpXq2gdwSlKNCsdFXLaGPaHjhw6HwAupWREaOEze0MnaPgeaUAIFcvv0MiJNNaG6SyVYKyYN0tDse6kriRXNRdXyjlzsDEKZ2CKv7NmgM6fsA-epvnF6aRXFF492A2yA31OXKvPC8Utfgrfs6QACanxHdk_y5xMPH5m-TbrKu80QjW_Kit89v7xRw4ulHNWGxiWyk5HaiLok_nNKzi8jm7Nv6LMRDOtRS_KdTXgFpvao-QSXjjEGFzVLth1bYRMY_qod0jNlvr8_K28v0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOOrbECUARsFgTU2gVe7znrmPkCNIuDYdjriwxCzvyQqOjR2amU1wPSWzKW6biB2K5TW6VGbfJCysv60Swfm3p3RRH6sH6pW3MktBml5hgq_NhtDeW04wUxHxwUnyTNWcIjeAc18ZznNTkMBrua5bvGlIq9up85b1JxLwLhrYz1cBLBwH_4Tr3-qTaPEDe66xcCphDReiq5aJVyTX7YzOvX572PoBDAHKjPnDJZSvUmU5yFrD5S9L5g4ViF7Ipij3VEaM2vLlTnj6Pkdl8tr4vCbCaNq3zTKVP-7lRdXwrao2LwW2cRoWqWu-1qmwrIgci3r2pTYmsik1aziJehf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3ZpsQhqaCft9kUJdWEsT6zUHtOg-L3euOT4QR9HBAro8x5v7oP96rNwT0WNv61SIFjbdLBS-P4lmv-UbWykQgG2G_QPZcuGtDexQZkRl5zT_dk-SYAyo657-1ALlQAglQgVnKb-RRlVZXxx84ZkAd3la9r4Ke0fdA3RmGpfRZNGM9NHVKMaJYs_BhQVz0kyqDfNCQzYEXCHUr8mTSvWdxJh7JfOUl_22z3uhmLT3M9F2b_fMwzFg_rJWCgeE1L5JtLY5XfuAJ62zo-HM0XV72puMegM2wt0CGUC6B31vrKZ31WXYQdx_L9zl70r8ukcqo32eoSpV2wV0iO9X_F1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oR3vzR3vGlXQTND2uCI83H2Tp2sH6FFkXsl-dlNhwJkHoiFcm7YWBkNOvRS5LHJY65gsXhjWeEqzWsuCwGF9Qacrvn0NT3PGxLfZH9qGg-83yIkgFp-crpjkR79mj5XLgOc9St2NMosnysXjpsKOZDS_yjkE3hRgivi428EjqVcsCWeEtfOu-iSY_iWuiq2vgE3EtleDD0_pSrGfS5S6WmRMLsgL_CPDVdrhzRR6cBIatulWi_Rw9ESVd_FkQGuD2kKgc-gyaDPRjxIa-dfLEHcIpdNMlHTRDag87jWIR52sD042nvo7jcVmr8MuPFPt2wcMwg3Bxab5odeorJGEoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های وینیسیوس جونیور:
• 2021 —
🇧🇷
ماریا جولیا مازالی
• 2022 —
🇪🇸
اِستر اکسپوزیتو
• 2023 —
🇧🇷
لورنا ماریا
• 2024 —
🇧🇷
جولیا رودریگز
• 2025 —
🇧🇷
ویرجینیا فونسکا
• 2026 —
🇧🇷
ویرجینیا فونسکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=KwHVwjV7WBQY35_0eLDxPD8c8xMIAkdoPDFC7GkLv7j-5cvbRSs1-vUYvSIqXc74FdsbxIqlf9mAE3y6vne7np8SsFjISrfSLUa0krbjaKHq1zG-DTww_F2aUN31dZSTQrfA1q1blQ6-KQPSMr09jM8rFu8_2Tf8NMtZFC0qWrpCC2dVmH-D50Azl0g6_h6x_fVIcPALs27FzFsf2TcGD4_cl090Ti78dy53JcIQiIWA_tuGaVDBIY9ZVtLk93bzrw86vCLyn1eLgMo3ylVoNBP3EHmULzZLi9ekHp9sRbnfru2bZdnAB1m8Xw4m0KpKEoUvlEY2DWJTBI4Di_Up_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=KwHVwjV7WBQY35_0eLDxPD8c8xMIAkdoPDFC7GkLv7j-5cvbRSs1-vUYvSIqXc74FdsbxIqlf9mAE3y6vne7np8SsFjISrfSLUa0krbjaKHq1zG-DTww_F2aUN31dZSTQrfA1q1blQ6-KQPSMr09jM8rFu8_2Tf8NMtZFC0qWrpCC2dVmH-D50Azl0g6_h6x_fVIcPALs27FzFsf2TcGD4_cl090Ti78dy53JcIQiIWA_tuGaVDBIY9ZVtLk93bzrw86vCLyn1eLgMo3ylVoNBP3EHmULzZLi9ekHp9sRbnfru2bZdnAB1m8Xw4m0KpKEoUvlEY2DWJTBI4Di_Up_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfSRfCh0qOIY1YpEY04GUD2i9bAAqqVhD7gB817iT_ymc7p-68fZ8yXknydses5hudXA9LoPiOO5ZI7pkKOUXkJ0iNbe2xNRYRm7w3w1SSCtM7RLkCfwhIT29vzDFeM4kMdFLBvhQhiZdDx5havkjTFoQBTT5j10wA-boFVTjonjWokiFm1llrzdY1I_Ti46CKYEB3YBOG-Y7817VKW72m6-lDQiOTaB5XbrhumjJq7s1PToCCp7YSKB3zfIEw47AM2uYUbbFqyLL2GocwQEwIthTL4CGZ6_g1ZJY3KGGgYzzWHnmJXKttu5mZFR8JWOF9hCwa889uW7AKN-SZRWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇪🇸
رقبای احتمالی رئال‌مادرید در سید یک UCL که با دو تیم از این تیم‌های در تصویر بازی میکنه
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3SkABz1zvwNgQsRKn1oUzkzNvfuC4oD4-poGb_evRJckm56Nl4l5Bpp4koHj-z4lSFGCG_VhPmv6fK4uY-4TyN2rUxf0GkUcmCGNiyDuzrmD7igeFZBx1Kx7lGJUiCYUbe4fvIhnuqwkWKu81szhuaV7qQZh6p9cSdPb9ynTgw9r7jBv932598A2F4beNhRvHptA39XlJYwCBVJC9RUprmwAKvc_Ysd4-MZwepug0txIvDiOPg4OzzyObf7fby_aZge9U8dndDl1tiu-dBYBhb0OZQbkm-mvhYX2ZB1ffy2qC7iDYiqwzvmHG5mgMhqADBB0nPHQRzkZJged14HAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeKKw52ACbUOisQNc4c5CfxVtG9sucxE9eBY1-2qVNGNEjbOkWMT6EUaJCX1d8ut8UpOqpsTCDXHwP1DFNG03EeRrJ3e-yzy4m82Y0udBNENDZ2pm7Bbl4xkzZ9-ke2l-1_-C7JqYvY7lf-fTuF0YLkW4i5bxoZpnbv-RuzMLxPucArb97FWXxmxODd7iE2e0036Oq_Oz6Ofmaa2577R2qasbqzK7Ynb0zSwDNaskb3960fR45WKPwr8GjXfpSaWWTaMQYjGJzVIQtfwAK_BtySwGgAD1MgqK15u-O1NfMwLrZKAE_VMBjnF9Y9IxtzO6gcfhsJE7AcuIpwXVhS-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=RhEJsYvvfeZ5ZkW8X7gz1gqbTCEI-L0ATyey44eqk626lwsnTCTjarHw8qSY_d0xwtRin-Ef_VBLkb9J5I_u9QuxdpIY1tTFDemad0aArMZWCWB7DCj4TBItZnfJ0LSGvq0ow5cJwqfxyhHS6_dpNInnAeYu3LZNjtBBbg2-vJ299rNqCw0dI3u6W_Pn7-hGhZDVDNe3KAAEkjVaX3gqMaoVjorGQ_JAGkGLzHSdL32JR8N6SfVZDZ03kUlPJ3a4J3G6ZGeq7G4hoKsgDbiGrtps4WuXj5QRoHN_rMklgOMXKhLISClif6wSSKAaHiJGDO5geZnHzrU6-_-LOjAPKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=RhEJsYvvfeZ5ZkW8X7gz1gqbTCEI-L0ATyey44eqk626lwsnTCTjarHw8qSY_d0xwtRin-Ef_VBLkb9J5I_u9QuxdpIY1tTFDemad0aArMZWCWB7DCj4TBItZnfJ0LSGvq0ow5cJwqfxyhHS6_dpNInnAeYu3LZNjtBBbg2-vJ299rNqCw0dI3u6W_Pn7-hGhZDVDNe3KAAEkjVaX3gqMaoVjorGQ_JAGkGLzHSdL32JR8N6SfVZDZ03kUlPJ3a4J3G6ZGeq7G4hoKsgDbiGrtps4WuXj5QRoHN_rMklgOMXKhLISClif6wSSKAaHiJGDO5geZnHzrU6-_-LOjAPKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=QDYgWtf_PK6bmx0LqkOevufKtvj7soVTe2o44XESDsWH8OmpaYE_nTwVIzw6Q4_Hs984pq4YwKYypUoAxiB77ahj09OH6zJ7N3foNSQf4WSSJGHrhRxhHmwv68KRL_Yc_pgJtQtdDhQ0_D-JCv527clSmEeWvhTfyc89G57qZ_v42LMJ2Kwjk_qiCF__mz77LZSZZ-Q4lZHyI9kvF_pq7Oj6wa9Na7Ke7rZncdWvgDLQ6D3XWKg0IDctgh_irwwTkxJLCSMQHs5ddborksp0YByRMj0aYGJVHT8Mt3MIuJn_Zm5ewksFLSgGM9dlvxQmADB6FasnD1p02YewEnzxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=QDYgWtf_PK6bmx0LqkOevufKtvj7soVTe2o44XESDsWH8OmpaYE_nTwVIzw6Q4_Hs984pq4YwKYypUoAxiB77ahj09OH6zJ7N3foNSQf4WSSJGHrhRxhHmwv68KRL_Yc_pgJtQtdDhQ0_D-JCv527clSmEeWvhTfyc89G57qZ_v42LMJ2Kwjk_qiCF__mz77LZSZZ-Q4lZHyI9kvF_pq7Oj6wa9Na7Ke7rZncdWvgDLQ6D3XWKg0IDctgh_irwwTkxJLCSMQHs5ddborksp0YByRMj0aYGJVHT8Mt3MIuJn_Zm5ewksFLSgGM9dlvxQmADB6FasnD1p02YewEnzxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=D0i28wOK8nVI6Q9Rbpov9vYxxuW9Ds5IPxQKpQPw-1lAf4alFr1E7PoJGds9-wInrEbbG5SFbYjnXsfyIfvPJrSJp7jDQrWGHaUGpuF4Qwj9mXFKvYJ6qFE7jALDGJxsh8G5EOW8QQEiqtODb6rjMPgj8hWdbpsvrovwiHLoiIe3oj2cLKMZ5df31rfKmJrM90yQYQLngHIi4SBhU3WLr4VKhxwRCtoKsmhq7Z3rqH6jvZvhUdCUNIKgLfVdY3LOkRYKicZ0D458_UAA0-Wy61zVje3JiT-OHc_ZXb_6YEm3cA7x1E1XwK09X6T4tYA44-Uh1BCsKye9KcAQZpx5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=D0i28wOK8nVI6Q9Rbpov9vYxxuW9Ds5IPxQKpQPw-1lAf4alFr1E7PoJGds9-wInrEbbG5SFbYjnXsfyIfvPJrSJp7jDQrWGHaUGpuF4Qwj9mXFKvYJ6qFE7jALDGJxsh8G5EOW8QQEiqtODb6rjMPgj8hWdbpsvrovwiHLoiIe3oj2cLKMZ5df31rfKmJrM90yQYQLngHIi4SBhU3WLr4VKhxwRCtoKsmhq7Z3rqH6jvZvhUdCUNIKgLfVdY3LOkRYKicZ0D458_UAA0-Wy61zVje3JiT-OHc_ZXb_6YEm3cA7x1E1XwK09X6T4tYA44-Uh1BCsKye9KcAQZpx5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJOnrEofa6QGkoO_rnIIT8_mXHtb5AyrJoGlITK3-Fs-nL_V2TrazXVWHbf5F53ICYMvECKDP-rBYxC9_dg_H12XGew_xp6JFB2aEZW9GangO3Ksi2QE4vGQ2zGXnzXaGrvYLhOnU7Tu1YPrusKP4hQorx60BPIlR_uf9N7QRXVWHpF-UAikCb-k4JTH9AC-e1E_GAJs0htDnDuqSOkbTXY15sBVAT3w-vp-bAmH8roevgxB9ShdXKD9ctjYajp1-DPRkti-vdDgV-nTPIzIHOAw011pi7jqbqd8d5yxQPsO4oU41xsOTFEQBFMARFo_CWkfohFuRDTPP3-9AalYiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنانی که با همسر یا پارتنر هم‌تیمی‌هاشون وارد رابطه شدن:
🇦🇷
مائورو ایکاردی و همسر مکسی لوپز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری و دوست‌دختر وین بریج
🇩🇪
مسوت اوزیل و دوست‌دختر کریستیان لِل
😀
تیبو کورتوا و دوست‌دختر کوین دی‌بروینه
👀
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=YGiTt8gx49If07W4mh1Le3siv9epY6Dv7jq4WoQEnxR-h24vmABt7grryA0dEksU8Xsw-rWs2k7QJPifiiiqBle7rsLuhDdqP9su8sY5S0qbmz_B8fvXuQBvYqZ7WiDoigK1V_rdzs1JTeyNAuo7xj5Or58fZuRHGbE_j80qASL3pVnHCJzNqz3nubBFTqIi5G24IjNVzLCzJyr8u3_H5GWF7OV56aFzREuU3w8-I6Wy6VEJl_GFnqFSl9v1iBb28TjHe1waUiPuWn3RIsV5EqxoR1DSXb3Pj9sK9ePINXqw8MQ-Rql5x4EUj45VMcV5-SgTwRd9JQoYJ9OvgltnRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=YGiTt8gx49If07W4mh1Le3siv9epY6Dv7jq4WoQEnxR-h24vmABt7grryA0dEksU8Xsw-rWs2k7QJPifiiiqBle7rsLuhDdqP9su8sY5S0qbmz_B8fvXuQBvYqZ7WiDoigK1V_rdzs1JTeyNAuo7xj5Or58fZuRHGbE_j80qASL3pVnHCJzNqz3nubBFTqIi5G24IjNVzLCzJyr8u3_H5GWF7OV56aFzREuU3w8-I6Wy6VEJl_GFnqFSl9v1iBb28TjHe1waUiPuWn3RIsV5EqxoR1DSXb3Pj9sK9ePINXqw8MQ-Rql5x4EUj45VMcV5-SgTwRd9JQoYJ9OvgltnRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3is0GXF75vAOnN_44vZzbfnGqd8RocU7TbtOrtqGhNR7ov4iFPVjcOP00cSdrfsekluSs_ce6_rKKgSopTukn-mcXrLZSQ8wAZiQ-GOKuzxmK0Bvlq56V26IWxfF3PEpM5V2r8eQrYNhMxKE0u6Yy_Ys0BYCIvgDbFpPCUD0IcsKCLRs_vdC7_HOvZcBBc15umUncejH0YKuLjzpgzAkCuvMM9R_Svii36sVGbjfQu4J0--phiRKwou40iom550jMeuX9wHuKbj0-LbO8m9Pe5VO-hkI089cS4XnG1to6tQQuRXxSQF-cH4XN1_KtBIetRhu3ym80Ku-BMviBXsqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📉
می‌دونستید؟ فقط چند هفته قبل از جام جهانی، اینس گارسیا، دوست‌دختر لامین یامال، حدود
۲۵ هزار
فالوور در اینستاگرام داشت. از زمانی که با لامین وارد رابطه شده، تعداد دنبال‌کننده‌هایش به
۴ میلیون نفر
رسیده است. فقط در روز فینال جام جهانی هم حدود
۱.۵ میلیون
فالوور به دست آورد. همین رشد انفجاری باعث شده چندین برند بزرگ برای همکاری تبلیغاتی سراغش بروند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkKfqkNoAWMBkluOp8sgoQBZnHe8tBecj9lhhHOHzop26wihs76zzSt6mTynh8MaiY3oThmomM-HJr49pdDONYp2sb9g8Vu5AWUO3RXP2KmDWGq4DVAg-ceqh7AinMs_9MZZCnkQW1UoCdKT2Bd4Npl5x092Supzxz16031gcx1zejDgHkyk6DfLBpUnPvkv8hp_6o7E3FcpReB7IjLQFAyKxR8FXTMfKZx-kPfRD3aXC2SNerOy01PgjlC0Ve9SEbcayBYZ4WTQ3dWTFMohz4bOOzewZRy9V7INOLs2hHlElBj2pWzfEBFNhDDV6jTZPhrbPZu5myoX-xQF2cYEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=L5PLs7NABqkTsq06iHOjK3T_AxnXiLVCk5ID1h6v0g482WSuGEvQSNNor5zk339RjyMye1Qg0p4AJH_OulL97tlifaVmWSZOXWCJHnxlJn4NoIQgW4Cf2FBqHDuCHHYg7EJIzDtcsS9r_Q6J_wukRlpIGw5p-GvGEicbban-x6lCHQH_QQ-EQRwhLwbHVoxQ7wv26Jv2QocOwjlbLbbh09TjL42JNPG3CojbGI2c1F38bbJU6QcwuEZ2zKttrxPO7K-XYFWE2SnJlFm0fDDCj00prgTn-QU0RF-gCiJm0-XSHdlGw9dThaH_5kIhAyEvLgC2CP7WwcpwMSooR18lgB4iM5zrJKGcKquCvM4j_586ulUuOf9rp75ofnTiCVDSXe2KMYCNUK7u5cegjrNSte9L07NSB2vISN1UvGxtJw3K5E1MxlJrZLC82vZI4-BW4RY-_cdUL7jS_XMKMEHhkffkS7_9g2HnA2BdtdJA24g2Mbd9gno8PvKTxNzyl93ieHDSKcZ_VMnfR2XICkfzgEJiORGN_Wn7f2vXKQMrpM3o8WgxTyLMHW95pJv3tIofeAjtfbj60GbKfKsjo9XgTqTDf4uGUJSbh_FvSHUGmYY3dWebFl_AHYkzDwH3xQwhoqAum8YnNKBVxhe7Yy8vJls5hhSYA8a1fxbznPzoxlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=L5PLs7NABqkTsq06iHOjK3T_AxnXiLVCk5ID1h6v0g482WSuGEvQSNNor5zk339RjyMye1Qg0p4AJH_OulL97tlifaVmWSZOXWCJHnxlJn4NoIQgW4Cf2FBqHDuCHHYg7EJIzDtcsS9r_Q6J_wukRlpIGw5p-GvGEicbban-x6lCHQH_QQ-EQRwhLwbHVoxQ7wv26Jv2QocOwjlbLbbh09TjL42JNPG3CojbGI2c1F38bbJU6QcwuEZ2zKttrxPO7K-XYFWE2SnJlFm0fDDCj00prgTn-QU0RF-gCiJm0-XSHdlGw9dThaH_5kIhAyEvLgC2CP7WwcpwMSooR18lgB4iM5zrJKGcKquCvM4j_586ulUuOf9rp75ofnTiCVDSXe2KMYCNUK7u5cegjrNSte9L07NSB2vISN1UvGxtJw3K5E1MxlJrZLC82vZI4-BW4RY-_cdUL7jS_XMKMEHhkffkS7_9g2HnA2BdtdJA24g2Mbd9gno8PvKTxNzyl93ieHDSKcZ_VMnfR2XICkfzgEJiORGN_Wn7f2vXKQMrpM3o8WgxTyLMHW95pJv3tIofeAjtfbj60GbKfKsjo9XgTqTDf4uGUJSbh_FvSHUGmYY3dWebFl_AHYkzDwH3xQwhoqAum8YnNKBVxhe7Yy8vJls5hhSYA8a1fxbznPzoxlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=Pw3LbSyUH7adZYZMT4VCE8Gi50-5sMWTYx_AJplt4kW4RaylIXXkQYzoNf_aHuvbNaUYRdzt0VKN4OxiG9qZt25AkvYLi70nDA_C0RxL4tNbUCOg1J7BQGg9I1vmKDU09qCy0tbC3Qc5ppwiu2AJFOAcfI6_PqoSeT_0hFhCwMLfW5dm9aKEcqQLWMvP_uffEKEH0NfgeKLB2zmpuUzZTQB-IQZqfyRFlVTUTRFqcRLc8821pjrxdrOfHzpSlDpw2WldruOzHuaCzWkXv8uCzoll1xljj5_J3H4KZIwlaHOFk2zSJS19PqyenOBPZ6Lqe57rIuvKm_cRh7gI_NsXPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=Pw3LbSyUH7adZYZMT4VCE8Gi50-5sMWTYx_AJplt4kW4RaylIXXkQYzoNf_aHuvbNaUYRdzt0VKN4OxiG9qZt25AkvYLi70nDA_C0RxL4tNbUCOg1J7BQGg9I1vmKDU09qCy0tbC3Qc5ppwiu2AJFOAcfI6_PqoSeT_0hFhCwMLfW5dm9aKEcqQLWMvP_uffEKEH0NfgeKLB2zmpuUzZTQB-IQZqfyRFlVTUTRFqcRLc8821pjrxdrOfHzpSlDpw2WldruOzHuaCzWkXv8uCzoll1xljj5_J3H4KZIwlaHOFk2zSJS19PqyenOBPZ6Lqe57rIuvKm_cRh7gI_NsXPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJoAfumttjDB1ZppmqFLGtp9xLgoL_hDipIuuErv1QlWgioVFuBsCceqg7TbiIh6N4FK9cpwmAP6PuiEuyOYhcxYauMt1wOD0I5R7tBiUwtOOBLg6za2EJy75hGqSvtDsbwrX52c3HtQInjd64wfYHYKe1ZvhWjqkjwaVWiINL0P-8UoqHQczsLpU4WjemCmB9Egs5c1uKMpiDsK43zjc1AL-0aPRCek5ehjzQ4_b9bw4hxVz8XZv0Atty07QZdLq61OJG7t7Oyz86nm7-mnAkGAMK5NhXF83sujDaAe7iajaBlaqJCwmFF1YkZWZhK7ItFiEIsJL6TCKxBLXmLArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_a_h9cI7K2U4hwpBVklhv4yAACoeOA7J1kMCYkHnyTIohdl4-UQfySsFdgy56VNca-Tl97ULtRMfJP12MuMpkCLwT1NXHmqh4oqtMwAdCaTu412B451HjibnIHyO6xrzJ6iKWZxbFBZVPlq51_7kBxKPyzMdQyWcLenHBrH-M9LjWYaC8imELnlVKvDs_ISf_yGgMxNhcHBUHzhHBYvGzyBKlTTmTVo1qDDaFN0wTxFyqvaLAhEY8Cyg3gVeTYRJsczg3gwBL-fJ-0nOw7n-9IwOLqH5qsIOY-V5MUwftNsDWqu5SCwnpI8sziwaFrKdLm4yMc5t3q0iweruTIJsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=s5-ONk4jTwrGuSQtMCHMk3BsQTPBByqeK27o3f-UAMJSNH2zm8XH8HatwusHWURiLajmWRD2apH30i6ySXgfX7cEyADH_A4eUXTQ01l0RScrEctkLLF3ZtEd75N3iOfOjsYum7e_uHPwfmwp44gIg5dr9d5QUO646xA_bnJaIkqCl4YtQaaPO84q1upI9y8ygYvbo9N3v2CnUaodCcNTE7ng4wGH1UBSRNdI2fEP14eJXGcAOBzjeEcN9sWe5Taa-xSaxoFcWiUR3A9i6qjm4rj6I47Gm4_u7kaNA-rORwDvIFdT3FxY52XdGQ8LI_kunxBYcgkSnek5Pxm6ZUyY_n7koSsidHDSD3867Sq2ls2Q9bqCymYjErMf2SvOi04za5JfWx4oBF_HH4CkXKC2qDDbdoPzH1HcmGXMnWBnqWwXBVAk9YgTs_UPpemuZFs0EmJEQZWHWgo72Eo6G911qM4hKp87BqOJevSWsnk-P9HyePSZIukdOwSWjCBWGwOUO1OyetuyrnXBF8XSoI9PI4YMJNBcWXkxktLAmM048vENUkTRykGl0RFdEnsKGNdVk620Ktmj4kZGlq2MrLU9WE2CWUnxazTsVAtH-uK-f4UDsw7i1xKBQqzmg3gQlziZTyD3_zhY8ArNG_Fmhri4KJwCB2HEsr98EVKyYmlrrSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=s5-ONk4jTwrGuSQtMCHMk3BsQTPBByqeK27o3f-UAMJSNH2zm8XH8HatwusHWURiLajmWRD2apH30i6ySXgfX7cEyADH_A4eUXTQ01l0RScrEctkLLF3ZtEd75N3iOfOjsYum7e_uHPwfmwp44gIg5dr9d5QUO646xA_bnJaIkqCl4YtQaaPO84q1upI9y8ygYvbo9N3v2CnUaodCcNTE7ng4wGH1UBSRNdI2fEP14eJXGcAOBzjeEcN9sWe5Taa-xSaxoFcWiUR3A9i6qjm4rj6I47Gm4_u7kaNA-rORwDvIFdT3FxY52XdGQ8LI_kunxBYcgkSnek5Pxm6ZUyY_n7koSsidHDSD3867Sq2ls2Q9bqCymYjErMf2SvOi04za5JfWx4oBF_HH4CkXKC2qDDbdoPzH1HcmGXMnWBnqWwXBVAk9YgTs_UPpemuZFs0EmJEQZWHWgo72Eo6G911qM4hKp87BqOJevSWsnk-P9HyePSZIukdOwSWjCBWGwOUO1OyetuyrnXBF8XSoI9PI4YMJNBcWXkxktLAmM048vENUkTRykGl0RFdEnsKGNdVk620Ktmj4kZGlq2MrLU9WE2CWUnxazTsVAtH-uK-f4UDsw7i1xKBQqzmg3gQlziZTyD3_zhY8ArNG_Fmhri4KJwCB2HEsr98EVKyYmlrrSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMG4eTM_j5iHd_iY3yUU1ujdb7Bndk-IAPxyeGpwVTHyKr13BUynSIwS4yJFRnPcAZLP4vG61Pt46QpuJmiIUGJhWQnxXW5CrqQuboAaITVxNkTybc-GlElugDmo9om6CncEQKdEsByji_9Qz-tsHHkEHEs2eYvLsiOY5LiOpXdxq_oICMTMwrZB-WTnzC6lONZFA_J50_o1R-_3JhEvjnN0IjC2kT1siHdKxb_ugbN0kugxe6j7DEHBWix0NO2quSrMfcVbFir2tkNcdLP_-dQwGqc1M_C_n5tPbiXHnbHZ14aMrJr9PzRC14Tn-FS3nZVK93oWMwiABdbxi2acOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYsx1yH56SveXb-suc2BQilbw14wvchWlz3bawtXjQkaLUywzjlIs98qjHkyCt6RlnZ5dgnpE3ewFtMEXUxGU365wsyXKaRRX1v-7vbRbrbtC4L0fckDdUvr5KWZCU7yR1gisGKQv8-BBz7vdSDAAVhucOP8K9Qf3-KqbOrfePsGdgcQ1XnQ3vanJWPUnNreArGmwjobqViySXkMoYpeuQBPwGvuYmiHFakvVD-C6cFMxbm0V2s_lwTZQwpPkSJsTn-Z_v-dpz0bItVFUAzTvJ370vnmxUf0F1-GLfDSIkA5wYVHgDG2E-wHxVENzpQ9tZX2PGttltPd8Gg-lzRW4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های لامین یامال:
• 2022 — سینگل
• 2023 — آلیسا
🇷🇺
• 2024 — الکس پادیلا
🇪🇸
• 2025 — فاطی واسکز
🇪🇸
• 2025 — کلاودیا باول
🇪🇸
• 2025 — نیکی نیکول
🇦🇷
• 2026 — اینس گارسیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKL3RDy_GpgzcLChPx3te6RtyMywz7DF10Hluq8zuPvOYjoZAouUAc-uMFfCbsOw4JKN3zQSeuBk96XVNndiDKCwuBxzlrNQ0KU1gkG-3v1PAER9veYhjlAZEOTRr4Folch-OeJc9D_eC3NSDkYdGeqGy0Dtb1e6kyRxgOGQeIjL-p7beVvQRk6emp99LJeFoxawGHnP9XzPfDJcqNkaIqyMeZ33n7VzC2VOcsZQgzEwyE1Ov6rYdrBDKbjOSFL57Eo5667pcg93jBGpJpnxAjeJ-1PwHRMevT4s3dKDBNTgEfFYAmrs7Hk0KC20aHLEsYRUcvJ2GZsOjaz83tXHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Al4zMus46TJumGcFxMvLty3mUph9KtQGSaqTofD7X3hvFVecJfh1Chvh0n-2PqC4mnXEHCv63A1ZEBpFPl4a8-lEQ81gR6dU40pBOpxAAsxB59eJP6L8pLt_t--ZlizudpkV17On-MLrmmw-CjsB0YhPNY6RQQNuGefXZAXNUonJKFSi1oZl8ExVSdIYTzBLvg-wj0uaCPG6QfDOU2qOrNkhrhT0EpOuMuRQO2kA7ib1eL4wYhmxhbZOf1-21gW1krZnb2lchGGztSGp-3pn3hK0mEeNX3jloS5wMGjUk-VEiXnWiE0rUtktIcvR4eIkFG5G4Pmt9GGmj95t0xrdrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-tlutafctjVqDh7MnS6lEUII7NeuGjn7cryvBQcC0ZTELBbFroMcb_LNcHnXfXy00FvylDFMMHH_OBjM2R6JHbVYN-QqwJCpAIi0PAbp5Q05ZWbJjb2qA1rol-d0PLzbNUjZSmvZPQ7W9DyBHo45JhKJii3oaCPR3F5lxG89s2jORizxMFDzHaliebjgYDA1-YUmowrcFdpqJmA7_drj7ImkW2VSPSwcosYVkhS49_rq_5WFy602ZPnMLo7g8yLY_4e9PwzetF_YFBC5nk8rUs1CJZpT1doX_2hTs1BuvL2dZ03V3PlCqjjYXWYD1NMJQxSjM9DnPLkrnaDh5qD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQoWFqRlPj4py5EZzHJpqEFQsr52sdKKO-b_fVyIX4Qn0LAIPIYtnYlE1fAYXlRp0bEQbk-kRhaB2nxZWIQOI0LcV71q4I5kCsEZaDUqBcWtN93RDYFtr8hk5WOyYsC2a4BNT1slo0RA4LaMGU1TAl8P9UIH5LrdXo9hXF2UKRrxtcNs6ZEJhEjNLlkNPXqFWJ7ObuNxpFGCIo4kI6EMzgF4utiRUP55MOamPdouW9ZdO6V1vtw9EEdEWyUdoz45W7FkspQ1S8kotmzeZ7Vg4MbZDE2Ao9ffZyonS-OnV0iGD6VXNhCKb6ko3maajburUxG8K5UfTCl-9AuQbMJo9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHl9jcibgeFHmAGhIc3zJugNVYYu4b_TnSFb24QlHdUQCZbJv3Ib1ZiDkI1GgP5lTYXbPs4RSNzi0MjvWrwH6JN43ZRfMbyzvL2M2elHPWoSUaJdeR_eebV74_f0dpaZriYLGoeitbM2AXF_BK8_CS7ROlZXPaaljcYkJqCGrd0Psu0r7RfBnkfG6Ux7OVBMXX8uCNvUiGjQ6UlmKoxKimn1_AKVeBg9SrbAzzed7ErgKmrufAwrQ0al-0s1k0dX9-zKkEFrozCFZbiLww2oOzh02XaD_SjOivvUqqIt6fxT3Q588gErFCe8qsGJmKtEPyD_xneNr_mU-KxzpYeyeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📅
🔵
17 سال پیش توی همچین روزی بارسلونا 46 میلیون یورو + اتوئو رو به اینتر داد تا زلاتان رو از اینتر جذب کنه.
🔵
🔺
فصل بعد اینتر تونست با حضور اتوئو یکی از موفق ترین فصلای فوتبالی تاریخشو رقم بزنه:
🏆
سری‌آ
🏆
لیگ قهرمانان اروپا
🏆
کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4NAXiSaWnVeBjtk4L9kvpb51W0EQxkUZbVd8ZTLOfQ_NIt6VO1UEZ7wfYCEGNm7vrw388I2Q3bGR2Jca_GNpNzXS6JtDi9OaEz9IFc3YlSFU8XgQCGUnJlbo_iynCC8nBIY5fN0LdOQcc0KyRaMn-kRa7mwirsSQk8sgi6spL9aCpGxoviZCXXP-NMlTvKhhb9zseh-dR2rvWHFcrPczYc3cxpaYUhgJCp-tDaHucKBt9LGlR-7ZnlkpxAdwhTfmwSGgU_fwdgacIGT9ONJtFcLy21Ls7l4pY--O8R2J_-eqjW7hxBwSBYPomPZ_0PfbdJVuXjxjEYmfb3mrec0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxsDZI8u8owQM3aNDimMQjKF7Jm_DASzYyvfpy6T8VAoAT57mP4H6iY6I8SC8j6wEP0DP33QCznfUup9LW20pu8r-EwMXRMUmasDAU6R7FkhS9iFzsbALIB2DRG1erVm5PsDcsxp1IpsZrBb-loef4m_7jziK1LrqmU6ghaQ2unsVUwIr4_8SVhCw1V5vN7nx7P-1gNNFWRdqJ0ihaRPWB6zXd9CRhwyECyEaaQnG1gPoZYSXd1VgkVSYe9nkGCXBLOfSB4uqUKVb4Kp4XjVKJMep99rgmueCDD-pKcgU5v3gO3zXZTXOF6EPbjUY02cz5dekbGBPlAxob6dt8U11A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8iEh4APMueJD0yHsNljLhbSckRuHSr5LNJnGsrH2HGMSlLzoyFlGE0fy9EAy1VFMd1mhxwB7AlcwRsVpgeyLDMGPCsXzGsd0w_L2nupXCDlRryIVWhsASy-FD3Wp6oFoQNkksLUf31rljRd9blSauEn6zO9SQXVxsQWlUEgqTivMBB-DSbIHivYlxgmPVZOVyh8GD0sWvyJPIm1e56ht4b-v1x_oRvNVdEdjjbPm2h-5n5LIFJRRWHmHim4ZcrJ-O0DXCjqJAD4QUysoc0XLttOM4Wejm_ipBeRgRj3IZNAIacACKaMQMbQzQ2AvsXpj8ilMBFb1AQqsXNgIteg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v84WRSuYkeAj-PI6O20SRJNk_p9xBvXhWQg35V5gsjBLHF3aCbkaxYNBfjIWDf14Y-nCcVsc9BJxeA1AwOq_kuJAujW4GTOPsO18A7lRubyZxjkxr-CXFULLT10yOHUeqHER9INFXNBNuX_bUJcSz70q14pjlgdEoS7IGrZ-tVJZ4jb-pE6gyzwyj4agGzMVcA8oeTJLMM11WOIQMKVquILi7XELJtlNyFWSbN_8q8Km6zeHZbXhAztS11ahSRpkRsbxv2o6gtmaiRGNIIgLhj5ZM2gmMB2aw52mlFOdHJVXlAMtbdQZA1jYDpF43RIn3khYFsn1ydNi8fhVunk1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=oydpr5t5OB7O5Krz-GO5-sC9gDsgfFqAyCF0pqwdflTavSxdh2NeM4VOCch_j-AF5GzzQPTnFqkXblzyJBFD-Ifpv97rRc5pAKppcusyx-kppOusIjJlMgY-tKoPmgVOLLCW23mCaLGQTK8-KsnTYqE34vlFAA-XYtwEwV9X3xzWPK_L_6FK3UfZb248Z4Uet4YslERJAj7OFQ2ZOKiG2f_9sUtC-bJ9U-_YnwctIPYHfXq1R7chHYaeJztDDE6Pc-Y7rlnRoM38YtQ55HNS5s4iiIxrI6NnEg-kTg2q5Y01-g9FedObAb63oHrbJFwmXJdH_fibONFjYasj-zpHnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=oydpr5t5OB7O5Krz-GO5-sC9gDsgfFqAyCF0pqwdflTavSxdh2NeM4VOCch_j-AF5GzzQPTnFqkXblzyJBFD-Ifpv97rRc5pAKppcusyx-kppOusIjJlMgY-tKoPmgVOLLCW23mCaLGQTK8-KsnTYqE34vlFAA-XYtwEwV9X3xzWPK_L_6FK3UfZb248Z4Uet4YslERJAj7OFQ2ZOKiG2f_9sUtC-bJ9U-_YnwctIPYHfXq1R7chHYaeJztDDE6Pc-Y7rlnRoM38YtQ55HNS5s4iiIxrI6NnEg-kTg2q5Y01-g9FedObAb63oHrbJFwmXJdH_fibONFjYasj-zpHnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idmyqXQJUmceMp-0JHW6IoD6KEeojaQJlKAFJi_REbZ1Pl87H9Lj07tpDEMmNaUvB0KIZfAIwep0JvbqhaRf-7Z9lScrohEHbMjnRQMPsq1XQqx3ZgqCPPRnmtuNYMjhaxi0sQzZkV6mRYtiU5wmm8l-IfHeBBIsrTK7CUMq3Zs07TNh_XJK0d7troCD-V7r4ghx2PzviKOiicw808hALr0mAokqIgAy8lmNqkqoaVakPn1gvbNfpSvSWF_B0VFjFVTTzp0tqkqlP5B8jJa94mJPOfjAGhv8kpHvyZeifvvsMFBzv_sGXNbfNxEakfNkskFMCj3kiAfzxikIon_T4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Std4vRb1hzH-liCFRs4zBOCIRwhpYb7dcMyVwGuLfHiMtXn5N4PMPEvlOpgDa6EOLvdHgF6efwkPRIYEAfz0PK8vsV6UPYb3Y7FcixZALg0ih8Ur3khD4BNkgcmxkrCDgVa7FLc_vno1ruKrjtujDcTs8BMaq7HlCLnXZHc4ME-vtYWmkOZx7Kq4EQPmmV9evqcVwxq39IkbUnyhOBrpjYc8Bms-Tm5QMhbiBbVFsn7SaXG3p5Qf2Kl3q1rUPvPrcV3ca-HEhgFHBw3_y1qC-SfOpnsT9lXVYmyzAHKL9kYBvNZ4HsEoUWTdHMlbJfgxjnK9bA7aL50ipx3Zk6faRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
مانوئل نویر:
🔺
هرگز آن لحظه را فراموش نمی‌کنم. مسی بواتنگ رو رد کرد و درست جلوی من گل زد.
🔺
بعد از مسابقه، بواتنگ شوکه شده بود و گواردیولا به او گفت: «احساس گناه نکن، این کاری است که مسی با همه می‌کند.» سپس به ما گفت: «حتی اگر صد سال هم مربیگری کنم، دیگر هرگز مربی بازیکنی مثل او نخواهم شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=Z3ifjfBE9f9yr2r_ATCvULvzDF71vJp87ccLWzhQ-Ock96yBLdJpEL5GiW3TqWrUms7IMwTLWDAhqt9QCz9duvRRgPmdJrNIA1EXRWyP0mDJevKPDx1YmIbBFXluc-doC8sRWhLJMfdWOKEcPO8SlHq-oRgPgJ61S6bu3CAIUX-cH4fNhdYPCrtnH1ZvIjWleIHXabniUky2y_3oHWWY2qUUXXcpUX5e9kJfohD3un1NGmShv7lXqkWk0TI08tyhzPfAQeBYRv8_iMpMRovnv1qMMH3V6dogoleEjDsI0-2LvLpVewb0GruzdOT_GfVyIB0QHQd4OmaiBL94_tTuQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=Z3ifjfBE9f9yr2r_ATCvULvzDF71vJp87ccLWzhQ-Ock96yBLdJpEL5GiW3TqWrUms7IMwTLWDAhqt9QCz9duvRRgPmdJrNIA1EXRWyP0mDJevKPDx1YmIbBFXluc-doC8sRWhLJMfdWOKEcPO8SlHq-oRgPgJ61S6bu3CAIUX-cH4fNhdYPCrtnH1ZvIjWleIHXabniUky2y_3oHWWY2qUUXXcpUX5e9kJfohD3un1NGmShv7lXqkWk0TI08tyhzPfAQeBYRv8_iMpMRovnv1qMMH3V6dogoleEjDsI0-2LvLpVewb0GruzdOT_GfVyIB0QHQd4OmaiBL94_tTuQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKesEtu_32zaps4bqzR18ldePDztfRWMgCQDxgkh55lRzVMl3DS7oK1kwJiX4QYfDnk1e8c-Ig__p5uW67nxyGIZWQpgAxwQhW8XTSaOT37E61mp3MK7x-e52dSypBbwT7FTCZMGfdsnFxSnjY-BpK1Bp1lXJQ75kzNAZatOzHxYLLlaNNrtNtKBe1wJYK_93ieH1TNJGS_rVp5sQ2lcX9px-vwQswJk9Sw7p5fjE-kJlbRAuXMdPUaZqLLzbMvus-KUKVzISgKLh8MICCWw21bKAn6FCAR05m6DMMIRzMcg-shhlE1chAREcunTQtFz7iIcyVr13c1ihzkatNULew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRxJOpdepMB0P8U2LO8GyMcm5YSFSLPDAjcqB9mlm4qISgaZQlNBrMdjJfv5CkZOzVvE9Gl3iAr3FTbg4rPRHVhJSxxluP8xipNVMAlsAV0dfehf4RK01Z4F3il6r64VCT6ZIqIluUGl5NLybtm11SYVBn8xwzDkgCeiz_olnjPc6YAAFNwm5qaw-jdeXLcZtMy07--zl1zN66ZISg1J-eGSAil_yjXKVi0h4EIBgg1qqic45O3yhTir0o1ozaJKXyQmjcNjjA7CsCiN3uMIzrIzoFwnqfEhSOm4CRvncGCAl1NgmryR0XD6rx2hXxYA7n2OkrXadafuRUMhgH-24Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPuGXSCTyLoYroE0jJmV9lKx4bbXkyqPOHnBnp2f0-p2elRjyhXHbDm8YeM_ip82HJvv7WUjqJ9aPDpk6ykrvWT4DeDCq_xjtCH-Fsx0nA0gAvD8nQAmiyof9A7tj0EWCjiGzvCcaei1gN3vW2HVe9yPu4xkNMMR2L8KVZDXyyPEdVQyuYwzzdma92Cax8c2MBkY0IVZ8F1hHpSUk1N7GkkOs4z9OaL3ZSVrAy8lAJEvVq5Ru92YFZ_ZECkAkYSYqEIiTiioFNuLtU4GA5YSDVmBdZzTq5472Nj2ZsViRoDtQ0IOqQqiyJRHZIaijEDzzGXQLRjo1UZdQ9h3WPq8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8IKR9VBqY9cKNMnuHPzvwkxd7SdgfQ_GNp2WBxeuds0E42_gcOifWxcO2DIFgc7NcmEMGl1eApqbU_wTZ4XvcDJ058nmqjTdIdeZ5kKzs8agEfhM3yb1OHVe80zXj4IVJ6k-l9RjOB0Lt-Z-QkqRvE_16jbPvua7h_8aUQS_InDtCYrVHNjWsHWv0pwWVvutrJ8Xn6eqINg0aMpLUPnD4Rx_uV9o2cb-ppKJkclMUDJxr-F_gAoJP8MdgPv1x8DfjbmjNNXIB4RzE9H1_FvLdRhugM4HoQMAS3kh6vieBtRzOlnDNJJ3TNTgv-x3dpK5W_x4sdDItHPrtN_8fi3tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KneMM62_D8qRrtexF9KqCXiZAsPQb0MkwIC6Sy8T_QxhwLYAWr9QG2twC7SjHfqzNs-lnxjo2nbuLBB5s1UZ297Oh5mr7y4cT299r7dw28rYZ2vHc6Y13fHZHHomeOpmR3hJT5o58OVPR1o1AKUP-Amr4p9rc8Gf0RzHTF-TmUpJDAO2ovAi13XLSY7atZn7D8bp4lZixQRv1oR6AbZ4RRTKH9eWgQ4GuyIhs9MudV0u8IpkIIfn7gatVbG8zpwX70Gv3xyZDlLfUB2xSIwai8XIDt3Jm0lERupvxKYhE-efjvQ39zDYSWnGE8vy3dz5IQWki2Uq9jQ_e3xtqq-K_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s66WS2vEVLVJtU1I_P-joyzZrvtKJjA75iQ9sitf3MmK_-HfVfXZmpeEbi1Nln5ry0q9g5fPlvbK5hfTsH_YDNuRUT02GbCzMOtg_88lci-s1e4MiCJqN_l3hwk8wN33RYYb07SI41Ax4xisVTU0-W87pL-Rv9-8C8IXB7Y5KTXykwms_T7OE1L1OYx6NL6BocsYDWDvd6HXdlJwOx7X4pvXYffcHabUxAACg-3ycJUiPZN1anSv_JIQRk8-OrUl_Sr4NofzGATw6MEbvCf7ImaP7xQb8ulBzfMi4cX4kwdQ60xpsIIdqNLA5L5AZT96KlpfcGBpdELrZ_wc1PwfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
–
فابریزو رومانو:
⚪️
در ساعات آینده، باشگاه رئال مادرید یک پیشنهاد جدید به باشگاه لایپزیگ برای جذب دیومانده ارسال خواهد کرد.
🔻
این پیشنهاد از 100 میلیون یورو بیشتر خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWAiS645f8kUP-rJzQTSeW3YJk5HubNf9z2w2-FNatXLKde-c2ioHYelBC-85aECUovaaEAgtPOURWnm3tGvsx9tjRXg1v9getgbkCYyLfiBuD1AmBSsBKDXAouUqEiTI4CqteXU-vxfUfYG7fGinLKol5oWdhGp3i9wqY1lzwhxEgemdVUUwj3jzHPy891w1RrbqMmq59JjhImucb5AJX0o_QxI1q74UZyKC_MzuKQkT2XTDqsuxJQN9zJMeoF672EmY2xJUn4jv6-A676vO2IMi94QVbhzq7_U1L3axIrvZV3EMBafmO--dfEbp5eZ34D7JsM_xfAsFRqeQ-umPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joljFntLHp32PRm9-S9k1JIc6CBcHfSrt8YoQCDavxK18xecs9bQaN7_5XqKwHF0jBGTMZ_PnNBeAMeNwex_ou7kFrtpeTkudjSU19MlmixpqcAHSb0LlYnNUElPdedTrN2abEVlSVDN3bbnfzLBbE4wZY1a2yzct50hW4gB1tH_t8gMgip3UuG7sUWzcFu4C3fV8Y_ld5-eRPl_a2sMj2sJrnajZ60a_2GWs3SRvdpUpoWzYnmGFjz3WTIcrCNGV92ipuAiQ0UDROTYECWoBASOr3lXFxv8YaPyb_z9ZY8tUvYV6JGVTJ7etOTlbocz_qllq7Hzu2n43pnBg406_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

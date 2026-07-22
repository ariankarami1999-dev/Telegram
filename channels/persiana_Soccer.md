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
<img src="https://cdn4.telesco.pe/file/t9QXv6BYYmt70VnVtIEQ32Bnz_lxVUiQmJZfUjEj26KTCNhCiJ-6UTUS3r7FLrS8C5blGXkETOPgBlc3GavOQaBwC2hsVbOPjQqyxEjRXPVET1P5PX5zRkb6BsVhrq91DMH05zDQQSZ9at4ffa6NhW36ZgZnLqwFVRWc4tsPE_i-DV8OSQ4yW-0rUdVkhYfBluo-OpTXX2AbfOnSZh7Kf6pkaE8eB9tTXFXlshoUfbbibGK4GisGAgT1tjXQ5c8Mo3G86WkbR3e6E_iftWO9SQsy6X-GRBTCJzA1dhhAlTZy4RHdlsHH_Qz9ZyExbWapaE8iJOkAA3rzCPxAhELNXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 536K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 05:20:15</div>
<hr>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuSVMnzg5V_MCgdRLhno_LdN3F1nTZMnTHbT1G2I6p1WzboKEuhwBsUyUJ63T-Lss5446o5zNq1mBL8b5JJOla9AKjETSxoF80o5SMN197cio2sEkwAa890O-seQ-E2-1S3vBXKxmO7SwsSqVpNiTZSAERwsoESFATqafeU7nZPpM9D8zj-HzSvyNPMXpxmkiA1LVrgJUM5uOT8xjA2keXuwMWDXVwbvmRKnqnj329wI-AbeOZjSvJnSUGDyvpaQyaKmZdFA6r0ZfGsFUO6u30sV5QtfHCZ4hW_kNorFjTOFlJHc5R-wQgjmfO_HJVNB90eTDKRrUjkjYONWkz1Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIrgJDezyXVDd6ps9UghDn2U8rEwOCzXZdsEcyVofccc_f583zVtLxM-AlATVbJFD1jRZ1ZL21EQHbF2fWOsIafShISiwK4jRId2RjAhh1-E_gJBCe6rRHXKKzvTj2BkdTNNK2Rs-yxKscjjmC2GhSBeG2Q_-C_INFZLqjWVsxdlgUazN9WAxtgHbUd5suUdEI0u_Iq8it9S1C0_DPiZ4EB9nEF8uno8At7HlOVfiOKVNJQKDvcG8Bs6mGxiwuVQIEzBOfYdyVeARkQZmjzaK8QiK_QIKSohlTMUghB0AOhjQHZoOz6WOB6zP-8nDo6FTHDv4RkEH-lgiapcACJ57A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBCEUwBpelyJiO7UjmALKc-_-v522PeUCWqPtqIOiHJbNXbOPVbH5mGI2GSsZpWaa_4gZMeqUC7K-8stgqfDW6-UtCumBapvJnsGMit2Nnfeah66oox_PTSUmGs5n3tPKnRPYvk1X63IGK3l_GQI2gZU2gB1ocYe40h_Md0xLLfHChf1eJFr7oHhrnPJEhrwoeknwiIKF5lsOH6D3Oo-TqFSOPyKhFGfD3OyP59ZF7lpdkMa2t3GoQOPoB_P-AkfwJ7sKONfaWPadp6PLalrPeJvCkAGt81s_2K__h-aw30lbx7_3Xc0e1R6SQ_UlnRMzkFdxFu0Izn-DOe6_4EzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=O8zMfgOwgjtqf_VeTnKlJhTswLRXBja8QmsUdfwwy20FUfaYYv_e6bMPSZeLSlMxBBiaVJ_jK-t59zGkSQkaC7g_v3NvuiPXpHPicTInrK3J-MMVhDJk4jvpsQ_PoqDrgAS1g5yiUVLIOfqWf28SNVOGvQqBWfO5Uzb55E4Lta13cNob6ZNcW23IKCPrV0qGymjwuxU7xqpLFuHSSdXhfdCrD_-xhNmlxLNQ1aTWWl1-vWUVkHtNkSFxqnU2aRtRMLmVwAHXokiFnmyO76Tu3PYejjLicipXLP8am4swn5iT3OnCsJeCZY7hf2D3Tfa2wv3jFBoGYYxUPWSk9w0wLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=O8zMfgOwgjtqf_VeTnKlJhTswLRXBja8QmsUdfwwy20FUfaYYv_e6bMPSZeLSlMxBBiaVJ_jK-t59zGkSQkaC7g_v3NvuiPXpHPicTInrK3J-MMVhDJk4jvpsQ_PoqDrgAS1g5yiUVLIOfqWf28SNVOGvQqBWfO5Uzb55E4Lta13cNob6ZNcW23IKCPrV0qGymjwuxU7xqpLFuHSSdXhfdCrD_-xhNmlxLNQ1aTWWl1-vWUVkHtNkSFxqnU2aRtRMLmVwAHXokiFnmyO76Tu3PYejjLicipXLP8am4swn5iT3OnCsJeCZY7hf2D3Tfa2wv3jFBoGYYxUPWSk9w0wLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=lQuKf8ZV-Z-gNb67V5RC44vQo_YYXRlS3f1DPhE8U87QXOmepJ-e2txDTS6ZeSeJlXKVtrQuvL698Lm6ZVqJk6vsiY3SJ_B0jG_ZLyP0HumgwvDfMlaQFQwbffKMYrzRf7L6PUnlxHKYIGrEk1CoUB_g39VVB2m_SC4TwHrfXh3GWTbGWoXXp-_9NzF5_ehDai5XUs0_NnFGnoLlkludImKS_oBldxuJ9XzfJ2AkCebR_iOB3AFCn8kxJsgWqZEUH-CPZdSRMYumXD6eLhPiq-lQcm8Dq5uB-GnBt3nAymsdOH9It4YNkVpYvK9FraHuj9cWhZPlioy_96vomuTIQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=lQuKf8ZV-Z-gNb67V5RC44vQo_YYXRlS3f1DPhE8U87QXOmepJ-e2txDTS6ZeSeJlXKVtrQuvL698Lm6ZVqJk6vsiY3SJ_B0jG_ZLyP0HumgwvDfMlaQFQwbffKMYrzRf7L6PUnlxHKYIGrEk1CoUB_g39VVB2m_SC4TwHrfXh3GWTbGWoXXp-_9NzF5_ehDai5XUs0_NnFGnoLlkludImKS_oBldxuJ9XzfJ2AkCebR_iOB3AFCn8kxJsgWqZEUH-CPZdSRMYumXD6eLhPiq-lQcm8Dq5uB-GnBt3nAymsdOH9It4YNkVpYvK9FraHuj9cWhZPlioy_96vomuTIQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26261">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN5lOhA3vrMda1pohCw6DFTEk4fctURSdRXZM2mFaH-npIxN9rnu5K0T192c9A2V3VLUe0RaP98dUYs8XshcDHnW4QzVpGbFHTkShcSVtlXqSGVvdSiqB3DAvnzLCkm-GSY1bxlHBfu5UBSEMZbVuUWq1Vi7cK-ovCevBuGLsAuahwJtthuV1ZJ8KwRxyd4Sc0cGaof9191wMEgo0AVHLPUQuWiZLfVpgYvnhWf1MoCyitwm2x9T5KNe2PfogsSvHw4_43RtFqSEEpyEaOoYFAZwBlD2N3ySlhmPQmJbK174bznmP0JZ_lQiHIi2fcu3GSR_uIxzaWLDdsfeeBEdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/26261" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bulvij45AcTGXTZ1FnkEMOuMIF7ma_P8m55cLBBxqRKU2mnMiO8qQ5CXJLuqKrXRQxUpa8djzCFmJbPwcOUEjLHn-7FX1Guout6fzxCHaK_ylCYtqVFXdE07LyFRy5WXThv87Z1X0G3tqlPbIt8oyLE0T2IqjxXD6nQB1Fu-ekQJDLuxjlGt1w0fOWiCev48fwDyvYUqt3KvS-XtcocXN_Vp1QMHhDWQ3f2x-Z_C2vWaFybtC8okrzpi3VlaZ7ZBBUXRuJTq1SesswQmLvToYpkEnFY--sUk80SW7nxajL32G_A4iQ5kuB6pGrRH78XmdpAzAmUdphk5wnPyEOtybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mb9HFdSAm0Lyc244Jy-34BFoqExiqzJMRYefV8zCAxH5O49SjXapdp2FUnzivuql1XfIM73C2_6mWsr1RFc7i1L6sOjVEUbqep3e47WTFzzkxaL9BYQgEHwf0RJW23-IQGJfOv5DyXr8db9GNe-9WXJemHLaNHYnxW5DLQK_g36hKiPMnz8N7Dg9Rfug1k21iWCcGxJwD6FQ7tcBoOhZ99m0wjdHLjwJFUt7DEhqWfEirbGiMcglVyWEUuZkV2xz-aTWiRPbUyGSNFgxpea88Yl_4jHiwD9283T1IgvuxT7Kw_QguVVSQJAkj01EVGvTR5x9FWsWYMITZP2Vkq9ZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey56noqRzdOHPf0rGC-n3KPaCuuCJ0ju6VWu52kjDvtW4w3fjxYLJTukvF-mxxNZf7abWh2sDnFWnMDBLopxGBwNXIWiupUAdE7R_3Oy0OjQmVu9PIeP7ONVJqd65rd1EgDl9zWNe82CtZcRGu0NsPpOjVEGchAUz1CbR7vE5PaKYkXEwKysszqjRQd9Ab6t2r_G4TLaxMDa1lsmrt9OMgiUKNrfsShf_5rhc6Pfb8Q6y8fYTLaFEVhuKiH7nQgPW2B4iQmfiKzMJARbrqwRXTEXx_Tu-TGRrjWnSXZY52XUZvVsePlnUPHWiDY4m2Xf_qwF1qKqs3ADioky2pr20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCaCdgzPrPTckBLiGH4ogIocAO4xKzddaNiwWTpTT46VyZmOkgLrLg5DbyVswGH4W0J8Od_vy8eXHNZNZLbiBHb-RryVSnPiDODoXiC_x-X4HsFonVBvVGsZpfFm6-HX_EvRplDlWYgCwVOf-ylR-yW9DXCx7MqogsVF6pEUCbIl_iyzdlIi_y8aBhIBpvZlX8g8z6reZDsY1ppbhBKuUzRxhs44oCW9S7vbA0IDB_92b7Rm5BOQSeTP55WDAEiq4BUpWytiRMgMAM0bpj0lipxRxGkRz3m2iMgxVL1GFyN63VynltZ2NCzFmiSEJEHsON6wO2tmkX_Au-5VBUEeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewi-UxTLZ-rI0IOPHEENlRRqCG7bUmHi7gQvRdM2lEEdrNLkevJ5BvaY7aCWrvqbKX2_pXhmTdFzK8PO8-X82BEztrVIV5XpyRAFxHbAdDp-xuq_786uyhJ7Frr3cls0fGE_HadtNn-cSTzxaWxJHc3KqctLAoftIO1jAPdo9SqSc1P-eoGDBTGh7qaLaexiISR41is1uwohn6XBL4TwDp4a9sDDLRF3JkMB_83fl9aMvabebVZV2FpSvdLOprgp1M_HFVcQBe8poqfQKsTO6O5Apddat4MvW9ZSgkYvl-2Vo8XfZLJ25VmZTvU1NNL-ipyku_JmN-Eu0aaavVnRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5RYf0SkAqdghInfnCo6ZxiiMTn0kE-GfsWS3nbTKuNCQTIc83cTn8_NfqF9so727gRZZm9hQ61Ljr5_G8tt6V5p-MiVPikl1Oj93REYahZF5LwXZUsHb9J_7Fk629vMzBIfMfIkbKRnx_bY5CqVmbtCB18HeB2JrJWY-svOkB2hKOSipEslfYXhu3lycdtND5aEcOTvj84P9iSw7L-jXIXHY4sMT3tuR4AGrZaJ-11Quf5fMt_AeXyi-4D483dA6bcgl5GH4ix8YcHHSHzJg9gcwehl2jIP5hHXNxTGbrdsdhza8nJG4H0m6mQMp9f_uMhDlEHdzc_clq3uIbs3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=lvtLBCY0ojrko-_KUSZXZ_dwjZ_YR_UMedZk408bGX0v0E3kOM3pltQi6YOZd6gS3dVvxwHL3aOmsKzxyO8FP8WHlZNRyJz-oalJulKdTxNs1oKPwruTJDr8NEORcHLDbN13Peix8TcI3Todx8TeCemTtRLHPmtgr84A01ff_bf_hThAqTNVS9cfB_cqcgCSedVWjl1YuSdnCULcGAwQ3gXODvYpXHkiNHZZoj9VnXXiAenjwuyVPLyAvawG58NNqc7DqcLzrl5bVnZNF5yDj7IDjQMAVjSYZRmKScRF3LY36FRBEx-TuyPMlqkmCxmA03n5FRgQ3aZiCiwZriVgog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=lvtLBCY0ojrko-_KUSZXZ_dwjZ_YR_UMedZk408bGX0v0E3kOM3pltQi6YOZd6gS3dVvxwHL3aOmsKzxyO8FP8WHlZNRyJz-oalJulKdTxNs1oKPwruTJDr8NEORcHLDbN13Peix8TcI3Todx8TeCemTtRLHPmtgr84A01ff_bf_hThAqTNVS9cfB_cqcgCSedVWjl1YuSdnCULcGAwQ3gXODvYpXHkiNHZZoj9VnXXiAenjwuyVPLyAvawG58NNqc7DqcLzrl5bVnZNF5yDj7IDjQMAVjSYZRmKScRF3LY36FRBEx-TuyPMlqkmCxmA03n5FRgQ3aZiCiwZriVgog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=Ht8_473Avt1ltqvPUu97ygmbLRgSyEKKD6tA4kZTtmuVjOOGYr8ByYCAP6ppmjvuS-jQuaKDtVyBe1dm-ImOtbwGc9o2z-8NyvGTTNrvmd_Avy0oZtOnIyvhpWLucsJ6s6zGDlIU-BJ4mHdxLiOtnraqMN6S_ZJwXRZjtGE7xPB8lPR8E3RS-GDcpWMJ52i23VgN_ON8az-4gNvChW1SxhSDUawAu5n8bIyS128qWWhZHpjymYG7ItzyRSYspi6eaWNbbDcjssbl6runYMjekAp7wDwKI5c3K675q96FYeGvjOwpY27obIsPKWUuK3su0W-hM75mObkTLidOJS0iZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=Ht8_473Avt1ltqvPUu97ygmbLRgSyEKKD6tA4kZTtmuVjOOGYr8ByYCAP6ppmjvuS-jQuaKDtVyBe1dm-ImOtbwGc9o2z-8NyvGTTNrvmd_Avy0oZtOnIyvhpWLucsJ6s6zGDlIU-BJ4mHdxLiOtnraqMN6S_ZJwXRZjtGE7xPB8lPR8E3RS-GDcpWMJ52i23VgN_ON8az-4gNvChW1SxhSDUawAu5n8bIyS128qWWhZHpjymYG7ItzyRSYspi6eaWNbbDcjssbl6runYMjekAp7wDwKI5c3K675q96FYeGvjOwpY27obIsPKWUuK3su0W-hM75mObkTLidOJS0iZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emeq0MEA3ChK1f7LAdnrn7vkVYwGrnkDvX8y-6GRmmGXXEQz2EEIhZ0HASwYxo8-66x0PgtbYBvBegYjp2g3A0Ner15xl_ktpE4f4YeQ09aOPb8-qC5iSdZqKcflGvviIQ9CFLdXqWEISxdDt0WCJBO3p3IaRwEq40BIwTzSylOQELXFBhAeKFYLx_TkOchFKQjImY82JM1Rl0iEabFmx_KggykD1KV1hwMmvVcnYNPAo-OZVgctdX4dqrIqbCgc6W1UOSJfMtr-bsztvM2_q8VrQcN-kcE169NV8ygMJTwRlG5gbkc1wdpXp-owAPkP_UfRFXDmq4HUvk27iTDr0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=vj--5Nyvtw_Du_7uqZ0V-hOFp7bJHjuBp1ZwJKDTOvJyzFlTEclvmlwR8Yw1V5ILS7gyQKLJJcOj8LtFJUzsAkjX3rCXc9gKPxu6Y52L3XfxVowbpoxeX5Ial_eJo0nRQ1zUgI1c8vYYefHwOO2GUNtt7o-2Ggc3RjLvMQX-ED-t6cnFZnvwoFuN412UElg01LWRt_X6JOW2gTTvYV6gZ0FY_ILSloQvGG5nSHP36c4BFeQBalyQ4dmDaVEqalm1bqFgEw0GV0XJ1r_whHrpKfOrSB8LITLkCMw7IYPdXKzDFVagsibTdz7nDaDQpxmTIKiq26vZjt9cy-9o35emJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=vj--5Nyvtw_Du_7uqZ0V-hOFp7bJHjuBp1ZwJKDTOvJyzFlTEclvmlwR8Yw1V5ILS7gyQKLJJcOj8LtFJUzsAkjX3rCXc9gKPxu6Y52L3XfxVowbpoxeX5Ial_eJo0nRQ1zUgI1c8vYYefHwOO2GUNtt7o-2Ggc3RjLvMQX-ED-t6cnFZnvwoFuN412UElg01LWRt_X6JOW2gTTvYV6gZ0FY_ILSloQvGG5nSHP36c4BFeQBalyQ4dmDaVEqalm1bqFgEw0GV0XJ1r_whHrpKfOrSB8LITLkCMw7IYPdXKzDFVagsibTdz7nDaDQpxmTIKiq26vZjt9cy-9o35emJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=MCa_eMqxvizbrdBk1ju7nGQgIFn19uMTtUM-fuNovqNVvYrYXM_-NOcAI7irTQ5OEh6dYT2pI00q6kO0dfiaMldBYSat0TyBOOC_o7jK2Ohp7vsU_vegZ7f9SeNnKN96OKDxHDrne3Y_VLUWVVoo7nGl825MYFmMKBDg8bg1t5LzI_SoZ_83Tx7wLels4GQQtNqMkAKnZEq0A71Q1fqcY_n1TiTL7lPE-dZOg_j0iRwBK53-WSi4RHi8_FPjxzyUQYKT9rfZc7gCcYLMrRR1ZlGj90cTyrKoSHJIzkFV8bIcFK7uRxIK4FuRGbyRyigtpt_5LGObtaD0c8hanbJKTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=MCa_eMqxvizbrdBk1ju7nGQgIFn19uMTtUM-fuNovqNVvYrYXM_-NOcAI7irTQ5OEh6dYT2pI00q6kO0dfiaMldBYSat0TyBOOC_o7jK2Ohp7vsU_vegZ7f9SeNnKN96OKDxHDrne3Y_VLUWVVoo7nGl825MYFmMKBDg8bg1t5LzI_SoZ_83Tx7wLels4GQQtNqMkAKnZEq0A71Q1fqcY_n1TiTL7lPE-dZOg_j0iRwBK53-WSi4RHi8_FPjxzyUQYKT9rfZc7gCcYLMrRR1ZlGj90cTyrKoSHJIzkFV8bIcFK7uRxIK4FuRGbyRyigtpt_5LGObtaD0c8hanbJKTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oilq_DuEZemsLUN_eTs5fiMfr86yaHi-2gH10rhB50bV16swDePSZjsHrmzVdEC5o_yxnQvJK2RK5BoMzEwNjFAuAONusyypl047yKw3KOUymInItOeDKqCc9I0RutsDw8hnQjJTYVSYxSms3oJTYtXb-xJTIhmocW_HuLy-t5kNkvVKKaNlvMknrKBRdwS39wB2TN95L7TsaIXlp8LV0dOTGq21ZO_OBV-15bWqyY_Da9uZjawxK3fiWq0_qCDKdqA8L7kTHnJDk5IS3ibblMrnU5toCD1CEDGCGOCc6-9C2tGv7TaXb5XtJhK8HW78WOVn0bSfepx2_a94lSsZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te6CKRAET_vMMOPC4JwyTIEA15YUevjD1XFiCJcpH6XnI5ZmTLmUjjw5tfqF8_2knAJAX6wMKFK8Mn42F9YQIZIVVuG0RRNAzRVAMLR4GLRrgWVnSkaFMWSr26hVAszJ441Ptpq4xedaQdyhuyZ7YFp80B-zOKtaOgwdJRHVAODBA9trVJrtOSnSco1-HWAbv9cCffXXMdbbRJ1FzukvwZLS2G6zJEFM_SJcNaIE4-i7hc6gSGVpE1tTjSWmgC2KfvUwp3VV6XZHLiPjfUJl4jRdz55C9PWql7j7a-cwW4WvYDZRx1l_OY12Cx-tGSRHUN22vt869wpkEzbooNo7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7mKsBkuQWcXH8h1mGbDhiknWPOGUoILKFdldNBNWWebfHho7tnG6RJIZZ7k3tO4TNOM_ouhK2nE-a3m4kfpsppO7-zmk9Im788JBdQGgJNgZJofI25AOgulrGwhtEWraHrxzXQ3bquCm-iPWae47Pjf_7GvGulWPq6KP49WElcNLYYk1A0OFAyNw8dco1LIMeISffuvVvncfP2ohHs75mrl_3Ygin5xUitiuvSAkxrfXOBBFRiXx0Hgn-z6XubMsnG7OsFG-uT7qaDvoXNydP2UUplAGBOZPSGmynKKJ2y1Tf5TSdZL4iyRjj9kSC-Bn1Jkh0rE0-L8nXZFGjnjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=oImEN_PO7JlHi2drVPeIoGcSQjNuH_aIEHpVwANQAIu9O8JMBoeY5ug6-nZIf6J-Rh45mKD7ZUUXCI8tF__gJnMbrRfuolrnaKEDg8qalnpuZ1O-jLaxJpq9A9cE6PgFsyTtod8upw_C7H5p8B9tIPvKTpSlGtjOfRkPJi0Dq9q9cxun1bqXCx4VPjNad4FtiyH-8hpodTrqEpQ56MebDGCjwvtJqsWnJVHgIp5cr865dIMCZDT7wHibHH9jo1for1kr00vBOxfNYEe59Fk5pXx7yO-BxKUCCuk-Zqooh_2c9EJ7nwv7024uQ1v32XopnRNpO_4ZGGiAGTQfTO7sszsXqxBCGbrWDH7vT0xSlifYyY4Ls4Brj24qJViS-bgsQpgF8v5yFbWPksLoVgFCUSYzDMkYg0s6u8IkoyWX53F80p_NKcQMWxgP_206VhlclFmTF_fcusp79tT08EpCz2Kk94Ua_L2Okd_S7FRUsu0KeDgSmAdcpyMJjHdvpK8u9R9OYFGkpXIyvs0t__j2_d8tO4GgOAQTrZu67O5jerh0cvcjO9EM88fuk4H61n70KE-7TBxejxZ8QyzYGL1B3Qqtm1UXL8dLYy9swcUxeEq6avvGBvRCABGyqWJxjFU6c52SKVpgrUB2hfVYTVTFUCgUxf12WsdlxoSpUFGE6-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=oImEN_PO7JlHi2drVPeIoGcSQjNuH_aIEHpVwANQAIu9O8JMBoeY5ug6-nZIf6J-Rh45mKD7ZUUXCI8tF__gJnMbrRfuolrnaKEDg8qalnpuZ1O-jLaxJpq9A9cE6PgFsyTtod8upw_C7H5p8B9tIPvKTpSlGtjOfRkPJi0Dq9q9cxun1bqXCx4VPjNad4FtiyH-8hpodTrqEpQ56MebDGCjwvtJqsWnJVHgIp5cr865dIMCZDT7wHibHH9jo1for1kr00vBOxfNYEe59Fk5pXx7yO-BxKUCCuk-Zqooh_2c9EJ7nwv7024uQ1v32XopnRNpO_4ZGGiAGTQfTO7sszsXqxBCGbrWDH7vT0xSlifYyY4Ls4Brj24qJViS-bgsQpgF8v5yFbWPksLoVgFCUSYzDMkYg0s6u8IkoyWX53F80p_NKcQMWxgP_206VhlclFmTF_fcusp79tT08EpCz2Kk94Ua_L2Okd_S7FRUsu0KeDgSmAdcpyMJjHdvpK8u9R9OYFGkpXIyvs0t__j2_d8tO4GgOAQTrZu67O5jerh0cvcjO9EM88fuk4H61n70KE-7TBxejxZ8QyzYGL1B3Qqtm1UXL8dLYy9swcUxeEq6avvGBvRCABGyqWJxjFU6c52SKVpgrUB2hfVYTVTFUCgUxf12WsdlxoSpUFGE6-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-8xRJclFWl-wKv_7MUchXEDpik8TOkcL2zlbzGibPyDrS-JbldX_9u7S_SLMdtefLcPjQG48ItihYcUB1ravfAlQjWIFIYRCO397KQh6Tc0qn2bGAOuPC-gHYTOL8UvRXpDH2jzTZ8Y89s8J2CJJmTP8giUWiYGCBybnmJTYae9UCKU8KG-UdFFdXi3yOv2sEzXnHtKQ7EWUC2T6NPtHZeD3Gsa2PpeXW6FPcS5nDZR7MXiqeknJuiB3IT7ioX7x4IUvsk7gaoxhAbftuflwGMpf3HVbCuCep4CRjJxYi7VjkgXOosOE_-UhPGqlH-ETYZhypXN1vxiu1ALqD6ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBaNRoi_aSkdk4kGTcX926Di2RRhftfU-u7nqXxhnHiaiomMAE4JMwPxUhWJz79l_-A7eFRBwFZrXSeiFhHTiqqff_C0rnQEk9dVHZfCYt-f29FtZkHBNTOl2yigl1fuwhdUB5xGvoa-ZLWGe4D-CfSaNkON_fPz7Dmo4KwULAvVgAbTqD96Pnx2QCShcWkt4s7EPvXJ8GHr8i723KYoAA19FZ7w7UNSn5UliTB_gZ4Ay75Efwrq-bvY0fGt4sRce9vqWcIcGs1m4BJazP1d4o62ra4nQpzOfM_S401cZ4hNVFkfF4OJi4V1SKx-nbrfWG7-QnzfRiRzYwz6KTbQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYGDCrG6AljhxbCh_HMfoOeoaBouU7lhGIv8fAYk0u2dSyAHTdg3mr4guK45vnceEwKNBoI6p5i80muubGb_JnMRx2hRxk1yQaQA51sbSZZ3F9DCyX-lIHg3oUpjOlW1KpEEh0KUsj7OJCj5P_FBpUuzgILFGgyV416nCKrOIPlnQJiwE2Psi42vSRgWikh6EAYJSN6gINgwHKESoo6saIkVgf0F179lmF7vDlVF9lLzWu2o4hSiLFSYfV_5d3xKHKBa-R8PfNzEJzV-aHHxn25LcR8tqrdIkUN3fBWtDuh6dTeVkaspc4x7Wwhx-REpMEmstjZXyVcjUIpP4wFi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRAmecfDKlXPuYVlDIoU8MbdFLenMJyOr5AK1FQtCDHFtD9JxhSFOCUV71rsCbmQhQv25xv0z_X3odP7qmrG6LAa-bUEQe4-SBNlmI3ZxCbl7F29trIhyPNb5QHzYx-Cg0rKFseBJGh5W_pd13EQ0Olyboarj2tU5GB2Qkd_I4TCrb64ydmK8pJiStfgB8bbt-aLeOcJ3fKoXmSZZqME77lBx8b1urqv-SJwFCFxjwckIYj0Bf0rkeAzr4gmIvcqr3ebRYS1TUqfcNXDTD9wd0R51TGAH4oUgBDz3fzaEkx6K6evGnBi5J9bT8MXBPETibLCsMQA0XRbyp16i5zuYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yfa8C4ekVwGpgRLbqoE2z9XuNwn9hai3QNwSlzugT5E7lLb6BTWBHdlvDLq2iU7t-xoWmUg7trV2sNs5P239Q4b5l98aEPi1wq9hTGK2ADOpGa1KaKhcu5zF2ahvQgy7-uPu8Mfzva_see99eBQ48OvnoHYdaqIEber9gJRezP93Ag-lH9z8wJd04UqAA9bZXdBOJdCl6Dam_WS4rl0bNrkLjBAQQUCA2EtVrj5GMrlCKWjH1_-R13Y0E9fIhCtTC0EnfyoFXM-ZsUeQLvZAKs_xNnC0DU8YlNv2LHaSeSK7Yoo5UVv148XZF1ClzFb0uMmLna1cOjRsUE4ANuMaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=l5PumpUKU0DylDMWNFIiisj6iWCZfl1Nj3skaBkAncLVMj4RzYp2F71Gg2Dhn40XGK5JICir7nIb6NRzH94bQSwE1ZfYYdEbwgrcy17MHCvyrmJ4RGtQzNYQ8GB5QGSNdBZ1xiIpYrpNorbEoxR3oxmbksE-sNCY9J5Elo1NainGLCqdqGcYYHNyl3FBy2UwIZl9gcSZdeupiSiLUQN9TaUwrUgy_3W2lb2R-kv1LRbIwvcc3i8yUnqUBdQr_uWC0q1QpBfTmW2NnOorAKl5G59O1kjEIsyNFal5qGyCYIHNMCCky_PIoy_Ymqg_UHk_a3ownrXWccF2CpNNPPAM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=l5PumpUKU0DylDMWNFIiisj6iWCZfl1Nj3skaBkAncLVMj4RzYp2F71Gg2Dhn40XGK5JICir7nIb6NRzH94bQSwE1ZfYYdEbwgrcy17MHCvyrmJ4RGtQzNYQ8GB5QGSNdBZ1xiIpYrpNorbEoxR3oxmbksE-sNCY9J5Elo1NainGLCqdqGcYYHNyl3FBy2UwIZl9gcSZdeupiSiLUQN9TaUwrUgy_3W2lb2R-kv1LRbIwvcc3i8yUnqUBdQr_uWC0q1QpBfTmW2NnOorAKl5G59O1kjEIsyNFal5qGyCYIHNMCCky_PIoy_Ymqg_UHk_a3ownrXWccF2CpNNPPAM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip6eQHWHApF68Roh7AkoHgplyBJYIWaqGSonTjik--AjJD9wigrs_cvRqZsiRbUc7VS4jlx_iDaPikkZ_GSfxEWia9V5OXmK6S1qRGOBV03-K-jYVRCUfDNh_JlujjZ0m2Tg5NVHDTOu3KpG-_ZACwyFFb2DCrOaN1qIk9CZmaYD67_UoXk2ewfA1TCzYZI_6jd15BIyBpDc6q-wlGLnUSPSmkhk6-oEWGH5Tw67tU2xlYrOrpL5qgVaJCpQ1p5p2w1pZ0QgunzPADjBOnxdC8tqRAESN2dwuEOASzYxAg3C_Gwvo069pqwTFbUeklNkDJH7j1dN_6JOO9_nS-_J-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfPLzcoTbVk2O5Lvep4sRpeLRKmFh2mf_ie-CiPq25W-CmwLtv_aBw0WiXQXIpYMTHglTXalUGg4v-U4lxNXXWRtETo6_lOEa8WSkfJIKZExm43p96MfVMrKY4t-G_yrvy3gmcxbbDWEtLyRVKN72QlADLyAxn8L8RoW1JVWuQdOJF88cyvo2-HEiR5BW0A-o2Z1-qYjsEMGDDScr-ivIXbwqUWf8A7L227-o_4KgHQxVLiVl5AhxljWhMTblxI_Baj99V58gQf_Nu5lWYYdpn50cnuytE1wPl7K8aklvBBUBUvWjcZdkY20uzQ-0j0GoZwESJkW_gjwBwkmR8BBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIJnh1lGly2nQMFfaOoZkqCOG5OSLVmK5pgp8hvUr72ji4jO8RVS7wnnnHaAt5LQZ_FgcPja1FIlj24a8TW3u38hD6j6DarR9TFXOGypoGKFI1rWFuc4sDrG9HZKwmRhmAN_S2P5CsnnPVjA1mfyy1mo55084LY1uv4G3gDuswXTdzJTOs4kdhyz1kMakGSLi4RpayGHxcuBnSQdEJ0KTV7hra3ASZxcVK1jl378GNfgK_fJejOjFm16z_Jc5mAcARv9Bj8E67eTrK80bMNNLWMKAAiXp-Pu_1T4F6wlLUIACiJyXX6Xu4CTBuY8TNtwNT7izz0KHrsqidnRj6xYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=kijEBuHNudk34zpjHafUFJ21aJI9n5M2DSEBvfgyrmOF1pMd2BZYrAxXbNFNuLAJ2XqOhgyXdF9p1WDqWoe26yi91Jb7T1UsFtpIAZSjSzLUvm_i9fDXwzbp8xYNxHrN9CIdGyDe-8Y0JL4e-71NZYIbcMP8DBtnO_kr8EffUsKhNwKv5KUcI7_R3gfZFnmJRYjAjHgRE2af2GCUiG7Us-70dDkYm3XNiabIDNpLnv5DOhHI0YlM3RVuxZ_TQK9kiyGPnsY_4aEezwh_UgjnNogpuvy8pMRHoD8gu77C7dDNjh1fHu5vntYb9iNhjhDuCh-laDs17eokWD5tqFPEcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=kijEBuHNudk34zpjHafUFJ21aJI9n5M2DSEBvfgyrmOF1pMd2BZYrAxXbNFNuLAJ2XqOhgyXdF9p1WDqWoe26yi91Jb7T1UsFtpIAZSjSzLUvm_i9fDXwzbp8xYNxHrN9CIdGyDe-8Y0JL4e-71NZYIbcMP8DBtnO_kr8EffUsKhNwKv5KUcI7_R3gfZFnmJRYjAjHgRE2af2GCUiG7Us-70dDkYm3XNiabIDNpLnv5DOhHI0YlM3RVuxZ_TQK9kiyGPnsY_4aEezwh_UgjnNogpuvy8pMRHoD8gu77C7dDNjh1fHu5vntYb9iNhjhDuCh-laDs17eokWD5tqFPEcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haYJuQGzFUGCjn-7v8tSzDv4ah6EOn_xGs7iCaot8Kgm8oXyn27s3vYKmCC_WICDgJko_dt0KY9Rb8wl1J3gLCUpbHR-X_UJUYS7GcR3TTKQwMhMbSIeGDxiumm0Qp-kEFB5_bJSg8hhJsH_frQ3zwwC_HnEDWAinqYt0kYZVc9RMiptrR8RHHMfLxCahhDU8UcYRz-DGHZCgKW-5DR2D4cG2fddLDa-9Io_45L1V6K3Mv8yedS60Qlqi7AV20cWfTCe2C-J0W0jAdg4GJ0MzxNpTL2KW1LT9AFvlGsU96Bgukvs_QH_KumynI13SisHTBYaU4b_nVcXyTxpBj3QJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mcx-SrEfdcONkub2sZRI0vhuH57_oiHI4wV6JXi8qxKU66HjYjU2wKx2JLZCEh-9CWbyASUxWlPFcX7uj5RZucObs6BAQfd1Vd0BUicj0bZmAzt_HM_ETdiBzKCcdD7LM1jlJjc2lI1NSgW1bw3g1bmIPg7zOILf0IeubxQL6k_eKq1syf8w18a_RbesD-927aZrIY8glQs7N4ONki3kcDh-1M6QrLv7Vl1GLruh7NzXYxolZjSKQ6XFK0Pzmcaostr5qu1gU9HrPIsfejmrIwc7mTfiMIFoAH7PHXV5Miuhu1XvPMw2erBokH68zihwE3OAp5QbeAvFbAS-xfcsxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxFdImJ6BHSvbMqfEMuhtepnbHYRR9aYsA-sx1sWYOTOwuP0o8jWk9RMfk8zMaPnRm3KgCVy97oXZ2QJXcl30NVcSYClHCoLg_nAmTS7R-iPPMbhsmZtFqA-jpPzprmI94-Z2dbI9LTB1kDTTBCBzOaR8KAo8ZsqUTvXFNUbnV08t3qzL5ZZSYJ8O2aV5REkIYMD4-urnnKeDFJ7D8pVm3BEFHrts6Y_6CcERTa7_nwkHkLPkXM4X6NY0VGdXgaPchBWFywzYamQlX9ma9m68BvSurh2n19dgL89jnJFAqWuePyO0YV90agpm5fmsA582qsB86fD-4dkYEsBeiKK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keaqzuBCRk3rm51hC_ZkvZpYbrZvbQtSrCiI5K7phSvpKOKzgiBOPNdr2vnkP1BVeVo2ZhlLEg5jq877HRMVM6DVQO5IPzZMx9N9AoclI6pj5OlQlkMNTN8a3-x5cxkRF9iAn8yGUEWv0kIJFBDj7vTFjsZc6w4do_2u9Xj8S1Xk1_ArQd-vxe2FA0pay6FUIzB5OWkFagAPc8d8MmuABgfcHvmK-XKZjWwx_3E2gFf_qixenuRhqN7UgsAP3xyGDh8p5O16mt-9cVtQyKsjSt5-0gASqKWGvy1WLIGKT11Q5fW1UEhsFJ4niCOvJS0RNQcQ6aOYDnR-3StaoBPo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV8tnVDWoHBR9qW8VAENrC08hNM1RVcRripU6rpb7mVZ9GBNjADX1fR8un11hKi9-nC-4z3To3CYhEQjLbl_1a6TbC8cot8ah-B1O1F5YjJvlosJ-MTU0CtwKNPDSBuZUlcDn6HWvEtLj6HJCLcXJntcVkUzwZrr03qzJf0PeaI-7LfKEbR53Gc0PahKwPNWF74rA73mQKVErUfucUlkZubp36gHgAeOzMM7tbpUKal1I5B4nfnTv5f-CeP1tUzxYbp_6_kFSZFD1P3NXlBxtb1QrSiYjM17L8JVDECO6rFsDH3T0XqC4X6pt0EIb6ulX-qPz0WW_XxAlqBWTMeslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=gqe0bIzUePT0JkCEtDj2Dgub3FpmqP9WeS4pC-dqyPp16n3ki_pUwC0drl-5dokzY7u5HmC96wHT3XdgZvcdhfLPs-qOLSMwE1AsORDyh8EDZJIdIbTNwebJpJTDFekLsULvzEJT6NHjEfG4b3cwIOlWLHg8_p5ocAKrVvlB3dxzMVehWE60p7a4hjhvOOU6jYDDQMzu87VCxZ-xY7yD5EBLVrpVqSnXy7YK6lVxCfPv7ommgp9ltXK5_B8Bq0JEjyVN9aUcNKKlRE6KTL_zKhcdKdd2BVmlXeINoVS9SUzbRi0R6fynLDjBKKHet91YPGwVMoU7vTK66cCx5X-LPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=gqe0bIzUePT0JkCEtDj2Dgub3FpmqP9WeS4pC-dqyPp16n3ki_pUwC0drl-5dokzY7u5HmC96wHT3XdgZvcdhfLPs-qOLSMwE1AsORDyh8EDZJIdIbTNwebJpJTDFekLsULvzEJT6NHjEfG4b3cwIOlWLHg8_p5ocAKrVvlB3dxzMVehWE60p7a4hjhvOOU6jYDDQMzu87VCxZ-xY7yD5EBLVrpVqSnXy7YK6lVxCfPv7ommgp9ltXK5_B8Bq0JEjyVN9aUcNKKlRE6KTL_zKhcdKdd2BVmlXeINoVS9SUzbRi0R6fynLDjBKKHet91YPGwVMoU7vTK66cCx5X-LPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=d8z8IdSsPjZ_bV9X83-7L0UvIi0U9Tmrt0_axbqZvqoEnIdrLPqbpTKbH8Z8jHdypK4oiuENh7hpNEpPgPby4M8hvGdZGuuRUNPn0bccjELYWC7OjBAVHvRXq3SJra690ZJLFsPCvf_J_R9iojTWg_-9AygnNY8iX8BhaTB9jCf1WctQnAsNkmT8M9bbrCCa7oSW85E_O3EtXnsq_ZZFrq0ifAhQyt9E9aSiq4fhrlXTtpP9yQwz64wb06If7u8w0_5fxqQ2rXhYJJ-SgZvC4KUqjZD6MN8OM3E7BMAQPkpNgkISQA2WUT72RB5JnwhRsg8ebajiDLN44io0WwzfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=d8z8IdSsPjZ_bV9X83-7L0UvIi0U9Tmrt0_axbqZvqoEnIdrLPqbpTKbH8Z8jHdypK4oiuENh7hpNEpPgPby4M8hvGdZGuuRUNPn0bccjELYWC7OjBAVHvRXq3SJra690ZJLFsPCvf_J_R9iojTWg_-9AygnNY8iX8BhaTB9jCf1WctQnAsNkmT8M9bbrCCa7oSW85E_O3EtXnsq_ZZFrq0ifAhQyt9E9aSiq4fhrlXTtpP9yQwz64wb06If7u8w0_5fxqQ2rXhYJJ-SgZvC4KUqjZD6MN8OM3E7BMAQPkpNgkISQA2WUT72RB5JnwhRsg8ebajiDLN44io0WwzfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26226">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqA5-_1a2UUXEAqsbUKLdSDLOkvyiseDzqk_dXW6XA4eTfauHKVIY5Hqp5wEVqnvi9fT_9n3eu_Ail_d_rNKkLDGXCoPUPFawODGLWKaJZ1b9mIwul34Si3jDmGqPTJjLtHm7i6JZRhT86wQFCOeIY_WIS694v0nGf7CGpoBQXJnR4uZkNAoyJEYtGnT1RtCTS3VEE6HEQz2IMTC8PBF-fHcYOlA7BnzSXjt5Nr4nkrZDvgeBvL8w19dBz_zFQCcgl7lYUbX5nZ5hhEsgeSw3zmJHwx7616Fi_oKhjKYu7KgnJyGF-UslDCJXMH8yHh2Ar7rk7hhHLnpq7V6svh3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26226" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=ZI0Wxj3hkBYpPmb5OcN-w10mt5k5jit0JrNNiggcN3MC_4ukxV34PRQuFmjIkdqBWmsj2sUYSA7N7V1bXT67OEz1byYp-TYUp7UYPQbK5z2EL9wsifb_VCJvYh2jzW2UkNkil5E2c1wBsaJL-Ef6dwOhX-6Nv383zK39cuHh59mfX2gNN8sFZrjifIPvZxZ49DR2_Qk49o98E73ecID2qPIu-IH5KOAYI7RsMMcUk6lFSoPwHY2xbv_V5T1PanmxkQtAfd5GEc8e6sd1ZA4J8HvU06MHVjZSWMwkHy-KINDBB37LVPrwtddUpPbdlBboAICgBmyXL1O_hRmCq8TO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=ZI0Wxj3hkBYpPmb5OcN-w10mt5k5jit0JrNNiggcN3MC_4ukxV34PRQuFmjIkdqBWmsj2sUYSA7N7V1bXT67OEz1byYp-TYUp7UYPQbK5z2EL9wsifb_VCJvYh2jzW2UkNkil5E2c1wBsaJL-Ef6dwOhX-6Nv383zK39cuHh59mfX2gNN8sFZrjifIPvZxZ49DR2_Qk49o98E73ecID2qPIu-IH5KOAYI7RsMMcUk6lFSoPwHY2xbv_V5T1PanmxkQtAfd5GEc8e6sd1ZA4J8HvU06MHVjZSWMwkHy-KINDBB37LVPrwtddUpPbdlBboAICgBmyXL1O_hRmCq8TO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2GsjeDhht6sr6utzT2g1Cyru74HSF6wx1DqfuxbYSuBQrzeUyPHPQcaV222KwyUdoIpeiwFiMDrulbQm1B8TB1yKhjgEPjV11R0vIrjp61OsAt2cQQ6rI8PY0F8Fzj9FYgArFPrU1L1AXA0-URSt0k3haLBK6OmJM4FnsKhwK2oneBQvjxOBx1cVtcv4g5I1hwmkGcDoH9xPmp2nUO_v_Iw3jcAKcX8A_1brfJxasWuyaaa46_x8p7WUrrvPAiPALkHadxb-JXzmxoBVERx3mTwUoNw-5H5pL2-JyynadRDLy8_nPO8sclLzygaRc4v6Lf9bAQ-ZwlnudOgNgh4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6Eerm4-BOZlhrUvDhEMXBp5De-FHtxjzsASfgxFb9t2Q42vZyES46yB71M2mnk6a6KEsdbiNs_yONekXTBFensFY3K-mPsRtUIqtkN236Pwh-uS5XEaNguGwhfD6IW-_lMaT_owUjbvhLFeWndZ5S97yAOM7j_1Fy7l34ltpPoZXl62ajfOI1EY9X2UZYmqM_3EJu8j4AEUsZLL2KIWo4yPWBajF1N_PRsxiNERM7T_oZNGTXxY8bQWQR27zPX-AVaKad8XLmuQTUQ5Bh8gWbofDbjw8jOGd7WGL9qZEB44Dg_44UJ8FuqzJl-_CTsR51JnnXPHIX1Up7fUakLEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKWgVoxtnznYBb-00w_lANopy802UDZ5JwJr8bzl-IT7CvYTLfYdFe9btlab3CcABgdtUw6hfRjHVKzPAKSPB8u9wJDPpsAvKaynm5rhDTk2rKRys8_-00x0QxwMZW1MYMDZhojV_-LxRw6I3q7TWze8c_1kDqb_pzw6R_8e-aAOCvV1oy0yGLWBdG_WcJmNIUvL4eHjs0ZrgxVUwAWtIE2cZqqTsGYFmAfdLfstzQdqvLw3NCGxulS61wt8y5_pxnRXgJ7f5_hb6pUofZrkYO1-gK1wQfH0VdxRFtTyl0p7lHguR4_R-KZZFpz9G0su8ZuEHYaDUKIa_QqXfEh_Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-2menXbcRO8dShACa-n0jcgL0j3YiNYAJt82H58dFN2RxSb097YbL351b80K7TGN4JkTP7h4raGxw_lQ-rDViX2Pmj_bKi38Acxz760hzKx_aC3zsILIj1T50WaMmaMSpSa-ZORHYwiUDcwkXmDYs_HpIR24XesxLYD2ltlam93Gf15SOmuku0SpRvZVu0nDWnMqcp-H6pq5jsmaam2rUlbB4nSLH_H4L5MYNOCyvpT_9WpQ_RFa2SDDiu-xYfkjAQ3mQN971ZXx3RAzjvD3QdfHbwCanQ09p_w4JoXC9bBO9rTZm2jjJ-jYkdW3dr5Il2K-TeoeS1Lgf4XnsvVUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSjjuahqYhIfIx2TEKk9ZDZxouHUFYBERDfRSeEtfBmV6a-MjHzEC_gE2aXVUx5cFPXGAk2Zb2LTTCGko60xyy4e0uJ_PdYagUzE95kofW-ZPUX5yfwVqnObOVgbGWGRuDFnMcCweysYcE0mEeZ1M1_EcmbKEcqGSA4-IdHBArabEusLqyKz5pHgMKqPVG83LNRKBzvF6EcnUSicBRgiK8GTsFY9KM_E3MmkdhkOACxE_wB_esxmGdiXrzqtCiMTX5z7q4eJEViNckeUsLxhbt4lb-1w6OXlkqCo5sdYH8B-Md7vP32b1p-I_bdZ0f0UfpqSkI8_MuZyDFThIuomtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD-NyN4n3Y2SEtCESlAdBav1G_mxRr1INnDB1cvTIVTRxLPZPGf_Yu7mWkSyiaoem2sSLAHZ2dQxAv01IsuDfi4__qkP5nXDlDzo4sbKzv0k0bHbpYQcDRa70a4dVeekYspdgLehTXNaKs2lfaSsFXhBYMTsAYujPOUUXG9jRGn4err01HN0KOYCsUQcsNodqDkDhyejbKbh4llLBmoGY_O2CNFhm3hmm-xom3FL9g4KXF7KiVa4r4m6cXHxpGdns9rF77zSlXtfkrTRydOYc3sC3OGlzpGePZbVhABwP6TQ9kmPhtOWEOtT5-EvQobywGzOw25wy4l_VYZPog0rIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbh-0AGZtMRfxMVWY2MIgjhN4WE9Y_vRmNdNzsHo-XJMjVxnUFP6JVmjcZGenVqr9nJqEohZhszBjNe9Bz8eJf8KOxY3VEGHK0vC4Ai8tol2WZv6wlU3J8DLG6E6qEXnAkCmSZFQD1hw_W91w5AZvNRVTA2MVgzJsOnnOGWlB-GDYf1EZDQoTfhVHf2xqfBxRNNrTDJMxGAaiJg1amKdkT14YygIsR-XvISv7N-Fh5st319cV1wRymGC8BSwo7SnNPP5lxga7pVaRJRhg-j60kBgdA4OMKh_wmOTw1uTHb30NNXRupfoER4vn63e_ELMl8qBMBaFwaGrAXeSv0ZiPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl_qHm8er-RFt2jwz0sf65Vnsre0KEvSkhd9MISSkfizP-PNVNLJ8xsGbnZRsJKuLBEROFkfh9dcALTxiPsZ61mzTAkfaoo3L_nAGRtvvJxNyGHuqdfLKgNuB9TesZqHc67oHph-RVnS9hWz_0t8M6WkawvGeZpoSJ65rFcnMwphcV1Op1ukcs42tIyrZuSDiP0BZHIq9DEJBh4iJDAKWhGdU8Ns8M-TBiS-XzrnA99dqUAl9ArO-fCA2lEyKBT_Jelm8NPa5IGphpQlyWac8F83ACwA0_1dULfCay6xMkoE66VK7d8IY1MxQWMG3sOVtKS4J_ND_RkHO38gXYNMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfK8_Ogwsylrysi9gnNwcniUR9HYMFMntCsHpKiTV1zDyR8y5skP1PPCGCmA0IAe6c1LGyEyERGa4nDAOMyTjB1DVZMFymz2dX0vWqqoNl0NjJCG6vWvgx1Nbvl1PuHobsPpHXNKntIoDiI3Q2uiw7CmKvjOvx6L2Kj0r4-nWB33ieMXSoD7b7Jdhv_nbPUbiME8O1zCCiiPYEcQGD2wyYPwUd9QEmwZr7rJ-wtn5vLntsBHd0SbSm3QFROuNE4V7lMv7G8l0p_Fg22qignJobm4olmQ919B_zox7e0Hc_n4hx-3a3uis-6erXMjaeV5knh5Rf2Ojb4lyF8y6XwQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbrkH1VgTZrO_Xa-cWJKXzkuMklCGp1LadUg0L90R7MeWZLx4B8OpkKTmU6jO7aJEVCTpdgp5o2BXwE5_XkHdiIwEkCa5_e2aNhV79KagmVwXXi-Mgqm0r2XzAFowjOLgqT0cvtYi68Mhr113jGU8S3THwmlSS7Tf2VzLKUdHZinuaAS2369Fx0MBWuEXDcqBOCX3KPLAb2F_KNdltt7umozBJURC76xxZVX7Q1xVJuR7V0EiYyn5RgC4-Sfswfrm8pingL2mVFMt80nrX44IlBVrPYWG33PLTBdjd4ZBlljEJ0hZiX3Wa72F0yo1UWAuTi-4AbtiVgnhw83mgoGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBovW2GcfXmsTvQjweLHHpwEkIcO6abLqYUXs3UlUxYF-sBZh6dn2s6p7S51Z_CZuPPEdK3_nMbovCSReTEZaueO2sYiMMV7cVR_Gxxs2p8t_X6lsffq_05mih2uvUDzcVb4k8mIx6VbZLl_wbR2wcf8poiGrDLj8e2o9xvV_3RA2BV6Mu5Uxm4Uvt6E6UuquweKYj9OELNu2cKPXzSKnxtA9sTIUcO59PtIRr3OlhwOqRP0qIpOckxMGk_HHW_ZDiGR7TgWqhpYNBuKDKQ1WvNDSW0zLrMonuK3-AAjaiuA33TTO0s-vnOwWmXthtxz9ebXBQmwp9wJVg-Hx3-6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVpW_yCaLQ1L0IifAPFDkjbdIWpT3wLsKpdWGpV4BKMN7T2nRW-k5UAaiaWlMUCc8rjNbbUHW650UMPyY0tYi34WQr0Mp9_sBBQrkb7I9_NcsV-HLtolPKgX8DeHMgXA9n7EjDpHFG6CledNrjjuBJDy3XQUhLvbXbUFd-rfNKb7Bk_kaUwmR9LfRd06tzwXhANT2ALGGoNWaFJdxFWzGr7Zi1mjErdnztYCxaB-7hxG5tr0lOipLOIw_QR30GWeP0ojA_JtlDYppJYm1n7zD_QP_0Grpi7lMdHDJ9g6nFDUlT0-sN7aAWdGkmEj7Mw9G7P5wFcULraWsYLqyi2Lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hD4xEwOFnvxe84rL5-9JWa0BZg82BVdCBXRHxju8jhoTcvXEaOpYNWKxMM7dn9xBVdGexj-cHrD0ubU3CQNOoicyzZudtWBtxz3PrlA_wu5BUU5UldXWfmP7X9NCgcsu1Q0YymDta2DwRCxaGqLz8GzcJ9Wrbs2dZf0hFYW_3y3qjPSdPTfwI5SVWg_VW6Bt8vsmbdee5_0q4Ulai9MWMNtJW9z0Qe64vnsKzsb5hqc6loAut-3as87vxhZYYpujquHF1dHY-uSOEIjyaxFMWdmWh6TevAPuO02J7FbBqdFp8MA-feFXjqfognJsrvrzvAJUlMyX1drb27LqcKmtOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJCdgnAvmv71M89troUfZK8qfO9qcbrc-IutRU_lKDDF2iQ3T7yBfH_lk5KUzjRTonFnIU9zLDrGF-exX3s6nEcfQV_fsisZy_SFBym-6f2FNgLrT8D6IHzfIDASQdF987tTZHb7j9a0X9P55U1dGvTf-6e161OPSyYNQXxJWfc6hbi-oxD0rXIk4V7W-E_aK_sNAqNgXLK4-5QBgAAFQkefGD9WlKBbsTgZiWeYOWWYV3Z--jfGGpQJmQRJU8W5B19FZQH_bF0RLqeBm0UVu7gfKjaaxb1x_fGc5B-_fH2GqHZCPwD77S2EzXDkI56vTnlA--8dRW7pwd44OhEQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsxrfEsBQyu16abdpHFISJAv6sjT9cUZ5no07XEnwHAsGuq3eqNHo4meYsvXU22CsL-Xu8RmoCumLJvV6VZrb2ZUfPijkNO1-hZb_OJf11JmcWNtxaHpDRmUraohGI2CtDkvvYAsqii249NSpr8BW45_DED7EoQR9rsLgvorgg6M4eJRV5T8UyQGWFZSvzqjgFYW7zvbir5tOj2U60KNbha4TjYAMMp4Iz2uJm0ysZfHNTvpKoTC75ci6mfWRm-oj7yxTwaZt8IbjpLswX-WKrhe6Pm-gtA-sfVpkDxFa1ohT3WKUp-oVJS9WivEpvryHpJ7JmKxKrlj2gxGofDqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZzlTbMTZA2M10pK8f3BthNO1QnP07TaCK3qsgp0sVbKTbRqxL1odWvgPbWoL6t7qCj99grzgRvUWj4c45ipqsnpa29GVpTKq_rBHWmP0fmZjdwzBmFiHk1xZOT_JXGO_zBZV2Fypk1eMeHJcK3Aq_SIzvbZXdPCNGbOfaNiRcEgQxYGjSRWEtxul-MzYk2-gcObPmvRN1UWpTL7PxTjnrvk2SPT8Vx5fXq08B9Hrf8HsybAsOa7dITYzA8zHU3_zK3AlyQCB9AeaInWwtYlpxPYz2ghkSqjCutNiKcmv8LaHTqYjb8np-_ehMhFao7ZqdE-tRo1B43qkCO4ZO-itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHAY4JiMCGpSx0VBHLiaqw-Kxs0MQ0SHPQec24i2f6GMNycd1iHhZ4FQcqpIaAPOGZxn9nNewgZYMlM4eGxcmFiUAcGZBbXs364UR3vJ-8V-SKqU_S2AyHg88t9RWK9JsRBkutEJRZ95FILq2Ueqs3P7LVjGxumgMF-u66VezsdMvlr9Ab0LW0pSk6zY-gjWaIhjHgyl1QUwAROE9TRA5qyZNrpAkxUyNR8zzgwFWwlOonyyCRj_ErYU4fZMthdSB0H-iY1WShu5d3i0fZkkIldU1Hk0nqtQifhHKvSoHx-8qxJj2oVZ6k_0dCvSvmzmQWYy8IjN7Ws8BU7t7SqTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiZU8_MsMvg2hckePMyDVbFIn5jQwqpiKJTGeSuuHkxAjy_JBPkKOr5ONtviM2oWjm439wh7qCn2uAv46u5Jsmf-9WA-P7yOjwZzcX8JIJqPcZPzcBz8eOacQwyp5Z4UUyVebmO12FJ026QiwerOfDyi-PMj6mLUwaAg27uEXe5EdLAi-04NzD-htv4C3Ni5kH2nK04Mprh36hEGzD8ytyx-_gb1t3clLajlvLYPZeFto9YdBFnXTRsKvMIOOSc5zhDIVPetjBB3B3wLKxBv8GPLVCneNs55eOa98-UuihJNPvY3a-EGxOO2Jn_IUCSkQ-z1390REB6IdmV4uEXYVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=TY3D7p_Lkip7yPGnZndkkP-vxa6R2QO84djzC9NrNEbFoe46dgoHOfoxg1r9D5CWfqL0W-9wtNzr-GPIlpAads1C7tMY_Ftmezs8PetsB5HF6teqSzj_NTKeR8erhkPRU0JFAyGhf9c9Jj5RtHHkSosENRbDfv_UPz7rX3v0xx54J3J05d5xHTHlP0lrfFNzDlnoBT99WUG8pJgpze6nGY6-FejDm9fVE4-0K_t-BlpoBXz8CCXuKOBwZosuV0C3_d8BR6N5znUW_YLuqzqhL5ZhsXzx8Y0igFndtUh9y4-vbS4NCpTEhXLxMxTMeFSN-xgyIMXa6S3JXuFu8sbt5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=TY3D7p_Lkip7yPGnZndkkP-vxa6R2QO84djzC9NrNEbFoe46dgoHOfoxg1r9D5CWfqL0W-9wtNzr-GPIlpAads1C7tMY_Ftmezs8PetsB5HF6teqSzj_NTKeR8erhkPRU0JFAyGhf9c9Jj5RtHHkSosENRbDfv_UPz7rX3v0xx54J3J05d5xHTHlP0lrfFNzDlnoBT99WUG8pJgpze6nGY6-FejDm9fVE4-0K_t-BlpoBXz8CCXuKOBwZosuV0C3_d8BR6N5znUW_YLuqzqhL5ZhsXzx8Y0igFndtUh9y4-vbS4NCpTEhXLxMxTMeFSN-xgyIMXa6S3JXuFu8sbt5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ficXvdt7MJAjwgZMTp7EjCt7s0Awa2HPIyQgryrWKfsEHNU2QgVYJcSvq64rgmbuyY6A0rmVGThBln2hkPx3h3s4pPa8IcwJnJ1w3wprBRDH6hQw0KVIZK5VObTrc8KgPGSEXNgEfjsZtCooUHPtPMSQ4dgYZR7ynIO-LPGvKAKwesCkQq3Y3KloNDncFl0xNe2ngrVohqALfwEF7L3lorPnWLq2fAWE3l5Xa3E9cvhaCgy_lU7_OaIn7h2nnY2EuR9qJvpzIENywUJk8MF0gMORQOo2e75P5Kqmft_JRS3H2Qe7OKkOVgydZn6ZtSgqp25tJjiA6piUV4GaOciAzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJTW2345PTxk2eGgr1jMfTRS3WVcSCL_Csr7zOfmPOlcW0CtnkSFs94gIKIakhcFAPZ4gP0eNo4JoL_whxXooQbwwDYhY8yJvU0GWKeYZHLKvZy5x5xUsPsOOE4RVoFTrN8fqLEZknNQMS5mHW0Hna6acVX_eygoCWLA2RNF7zgz7VfF6v_CRUxgc8mDk2Bu7JB-u2YFvL-ZOOuBrMZVJ_VdAOgIeCvjWDPQEjd5tOWpQyp8eeQq-C3f7AaDNYvLaB5dlpsq1klYqtxU3m8SWSgcVYtoksL4mKsRakIpmfLcpNxJlQ3a3q9_KmWyUB0zLNX2ADKwXWBeRuzFj-U9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kjk4TYcPOjTFiHGx8zNV1sg26w8Jhf4c5B4WuRt6J198pE2gtsk4_M4H0Bs_wBCbeyKg5aArxuQ-XNRvnlW18_T1WYV5jpXEehRJJn9VcSfTrXnO-NhPgLjOyp9avBnWSChFNyvs0Q2ajC8w254-f-i1k9YnughV38wSh3SuK3gAefXbw88i7GF3XU_yVQ0Aa3EjarBaEKyb5Lf0N1WqLMOjPNdzBVZ7GFwY0ecn1mR3GWWoGpIxGGAE5cLlbMbMLmEwkid61r_xNWSvWmVj8JGwLCuJJo0orunYNVktB3WXEZn3VDVQi0xKqtMTBnrvsK7p6WmWGsTJZ6M4hOrH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=BoalYiH23FmEYTjTTLMuPltd74RSaKwo1G2C2JZvZdti7nx1wjkuLUooFb-YKWVH5HoL00Hzbo9RwY81jUfMDFFi_jA0aoxVrv27ulqEC6-X_2qxwe65mjUq7Sql0CnoB0KQFvAb5e0KtjCfKX4wUsM8dU_wBn9F1ygEPFVcUzyfDuYEnbfmixmP5VlcsW8W0ibCpgtC8bD1961znKpfEbxpk8SgJilgADQjsfekBAyZ7SsA0DSBqCJ_k1aZ6XjQV-GIUWKB6MFNbAe26oFqu4FApeTr9_-OAiJcLaYuUiNEvxPcV4cLJLuYy9Tb9cZTlzNqez7Kl_VNkfW7Zv0c8iSoFHOctHkunVJXmX5MHMcPiuao5DtHM0pnefSyICxRthtVXsHGIPS9t6HHWzSPmrFZoQM_JVD84zgitFPSRO80GMqDv2kOtsT_fDAuoePX6DL1kSH3s8bpTQMMFGWhZnYn8aCBeZVOwRFFukccsApSdSgI7zq5d6E4FncVG642nwYaL_X8wetH3xLJRmSnzi8T9OnKfjRlexbkDbTSwfod8zx0UiDP3w84GBjOa2qLRprhNzkvK4HCnZV4N8hu9XR7iYfgYjJ9xe002AIV-47vVGnipKxFuT-nG2CPC_8KnruG7HEegkZM5hMftfLBmrMzvCQMZxROk_LgHC8smsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=BoalYiH23FmEYTjTTLMuPltd74RSaKwo1G2C2JZvZdti7nx1wjkuLUooFb-YKWVH5HoL00Hzbo9RwY81jUfMDFFi_jA0aoxVrv27ulqEC6-X_2qxwe65mjUq7Sql0CnoB0KQFvAb5e0KtjCfKX4wUsM8dU_wBn9F1ygEPFVcUzyfDuYEnbfmixmP5VlcsW8W0ibCpgtC8bD1961znKpfEbxpk8SgJilgADQjsfekBAyZ7SsA0DSBqCJ_k1aZ6XjQV-GIUWKB6MFNbAe26oFqu4FApeTr9_-OAiJcLaYuUiNEvxPcV4cLJLuYy9Tb9cZTlzNqez7Kl_VNkfW7Zv0c8iSoFHOctHkunVJXmX5MHMcPiuao5DtHM0pnefSyICxRthtVXsHGIPS9t6HHWzSPmrFZoQM_JVD84zgitFPSRO80GMqDv2kOtsT_fDAuoePX6DL1kSH3s8bpTQMMFGWhZnYn8aCBeZVOwRFFukccsApSdSgI7zq5d6E4FncVG642nwYaL_X8wetH3xLJRmSnzi8T9OnKfjRlexbkDbTSwfod8zx0UiDP3w84GBjOa2qLRprhNzkvK4HCnZV4N8hu9XR7iYfgYjJ9xe002AIV-47vVGnipKxFuT-nG2CPC_8KnruG7HEegkZM5hMftfLBmrMzvCQMZxROk_LgHC8smsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMTSPY3czYCkyMUuY5s0uBRTHHgEkKOQ3OdvOO25v9PTRcQMi59B2DgzaVRTDbt-nhqHyxYkcE-Gxpwj0ILFd1l5BpaQrlDIQQzHKGpXuChBCwkN8maqYSn6jkRh5rqVlcH5Tiz-v0MdOT71rrlp9IJFQnqmCQ2NaZ0TDdd-HyLVQTcE2l5S3uhDofd4egdpa0w9VgpnV_yhhZFeBvdHTz6_d_G9fvxU2iJGUdXTUIESeDoD44qOKtiWT-8Rl18vJZmy6xLm7deLUjx42Rm4xOQdZ595Uw1k9PkzMKP7gRt_cu1np30vu8GEx4q0UQa2TK7N5i7ndGXr0rq8KPCeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnl9ymVkSXNfGTYR5mOVOLFT3oK4Iw7Pm8Pz_pa23Sh05bq7wNkne3VEcltpp4JakYGm-dsJDGeW5x-8CBHrLANEPpnvH7yL0FfEkoJsW8_tGe0MRBlpK7GOoL3nmXeRUrewWEhuY30bHk1hhVCN9vssc0oqJsxxTfi1koP601ccQYHeZWFLx6YSTneRW1YA_GumKT8kyZAXFPddePoo05BJeUtBgcASdyLVUUIHvhyDwZAOD0CQCMjrRnxSNRKGGMNaPwGjnCklAh0HVKoJazoK5fzvXcz54pG4EL6KFaUCBS6vEr_6smB64353qQN8kapjSvWyG9WLw7mQGGkuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=EwForFAe0WjsJlCDu-47tl3MtO4fjDxg0tRsumf-ADggGLtlfiAqIF46g9CXoUeRJP8k_AP-Je8v2cAbOt2UKEsdYVRzlexfAFOJXdghSorsDhdstsOVazWJdFbtXgzJY184ebMvgeR3ipiexaIMM6Dpo-7_GNIpjyyxtshH83c5-1yw34U9gAq7OGcBPnyYJD-bpxj_21YJWSoZFBOJ_haS4eJMskGmu3PvuuyX4ngZ4g_PUPSNVCQwhfZ8W2wsUY_VTXx91qle2kH41LZKyU7nFj5w99NzPnYTbLxaqftNSn2hHjlZgA75KlQw9sMiAlpYbHE272Q_aY87OqKsMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=EwForFAe0WjsJlCDu-47tl3MtO4fjDxg0tRsumf-ADggGLtlfiAqIF46g9CXoUeRJP8k_AP-Je8v2cAbOt2UKEsdYVRzlexfAFOJXdghSorsDhdstsOVazWJdFbtXgzJY184ebMvgeR3ipiexaIMM6Dpo-7_GNIpjyyxtshH83c5-1yw34U9gAq7OGcBPnyYJD-bpxj_21YJWSoZFBOJ_haS4eJMskGmu3PvuuyX4ngZ4g_PUPSNVCQwhfZ8W2wsUY_VTXx91qle2kH41LZKyU7nFj5w99NzPnYTbLxaqftNSn2hHjlZgA75KlQw9sMiAlpYbHE272Q_aY87OqKsMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=feNpQpU3lP9I8m-yqjicwNNUC5A_zgIQ7K7_CmWk3dnT3xoOH0FrUmWx0fWOOqGLkHgxR5Ehho_NKy-eLnyK9uiuv4B6utH7_E_BlcY2hJF2oNgcsZqBo2Cg-rZmkSRfIf6t2JOMePRIpvBwlm8-5eXvSULFMFPu0FkeUnYvmFhhwD5zLBSDEVefWbKUNzdajzgXxg6pzHa8U2xq1Wx7zRQvJuZ711YSOtpxN7sbmEL85ukER7T0KHLi2PrNBNNEkpyQDHcfxAbJZfWhUR6-H1F6dwaR2Ut__1XKJOF8cnoLK3Z5rf1bCyRBZ2w2Wp6xLv1PHqXBiaX6A3hXPlTlTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=feNpQpU3lP9I8m-yqjicwNNUC5A_zgIQ7K7_CmWk3dnT3xoOH0FrUmWx0fWOOqGLkHgxR5Ehho_NKy-eLnyK9uiuv4B6utH7_E_BlcY2hJF2oNgcsZqBo2Cg-rZmkSRfIf6t2JOMePRIpvBwlm8-5eXvSULFMFPu0FkeUnYvmFhhwD5zLBSDEVefWbKUNzdajzgXxg6pzHa8U2xq1Wx7zRQvJuZ711YSOtpxN7sbmEL85ukER7T0KHLi2PrNBNNEkpyQDHcfxAbJZfWhUR6-H1F6dwaR2Ut__1XKJOF8cnoLK3Z5rf1bCyRBZ2w2Wp6xLv1PHqXBiaX6A3hXPlTlTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=KGV6cyG_cVBhxT4yr4zascPIO-jRMzgGDAp8i_nhF2T_SO94hWwJ4aY9V3nahDTQZiNQDlxTL1h3-LjAoLCtAXA6-CV2Xhe40E9DfCA1wfgRB4R2wg8CCKStFNKXz53-u0ZGPGCpkLZHasI5Fzl3pJj3eMDzq2Bl423Ssxhg3vDD5Bi2FwVcE1iqAvtKAVf-i2Eeyub3osIN7ZHp6bmEWVasv6kE1Qhz2cp0qZIGp0AjEAvE_Rzx8xSLFjxamUkFCrXky4wa6lodq_OSMczKrp67lhxMhvjjXcNAoYDR-kP2XGjMddUPIJqf6mcJ1D5540oKRECFUwlPYi2-yS4dlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=KGV6cyG_cVBhxT4yr4zascPIO-jRMzgGDAp8i_nhF2T_SO94hWwJ4aY9V3nahDTQZiNQDlxTL1h3-LjAoLCtAXA6-CV2Xhe40E9DfCA1wfgRB4R2wg8CCKStFNKXz53-u0ZGPGCpkLZHasI5Fzl3pJj3eMDzq2Bl423Ssxhg3vDD5Bi2FwVcE1iqAvtKAVf-i2Eeyub3osIN7ZHp6bmEWVasv6kE1Qhz2cp0qZIGp0AjEAvE_Rzx8xSLFjxamUkFCrXky4wa6lodq_OSMczKrp67lhxMhvjjXcNAoYDR-kP2XGjMddUPIJqf6mcJ1D5540oKRECFUwlPYi2-yS4dlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba7QhKogaCo4S5364_tS4UG7XNO_MS6YqHAiUgI2tFZhrrZutN6Je4BF6hW6GDYZ_11iQsR1PrgrzgeAOMYVLmu4ctroJzZF519IqtIyUk8vdekpJhVlHZqfF4vjv2lLnNUNUJSA2oGjjhYVbvDiKEDPlSmCCJwFZoXZjoJKVsBG27qNXAdf5uQglsfsSfOfvak8stEO2OksofAcKYtB93Nb2mnIG2HSOKLbm2OtgMkF20o3z-9K_iKUwy46IIzxRsLT2N8Ww66e4tNkz65HeAeg_20kM05qfmv5_wP3cG5Pl7_z12GMlUkf7nIHdmjPZWmp3f7x5GTcAvQq_LgWlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6gCFFg6J-QHEUpbdnC7eKubSoYfLKNdzWkHlCMZsluHr43W_FwAMUPoFMWm5M_neGh_v0zRaMKRUdGJYLXZdyBmxIKC-b_aSKs0VXbJt4C4gTjhA9UV2CnyDTAtOKa8yxrCI3CyBNPGL_8DKX7_gfF4DqqXW5ro7OmBXfCKAUHGt8NOFyrzwWKPwzDH2XdGiOLgOfHt4BCwVxgEGlxdYJ-VM9OOffgPGjACIN0P0vg5yAeeVh0gGIe_nKrW226_40Nt3Mhio_qv8dpx_uMR1BIN0SKVGUpWqJssxCJYcLYGjT365iWkt3DeTVCuftnTY1dY_rdP_kse5zVrUNJyZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=Ug3RlgdVtFnkfi3cNdPxGUw_TFM4io0DFTiMAveJIbSBMPg55tDzLTPStb7q0k7ADbYrwZ-QPkbDXCVJXbheXMkLqj9R2apugfIZRXasjMDyXXrwPayzkTo71E8YSYfAphgxvIVxovySTAFZ5OyRfNPeFJBLse5aXDz5kNZZImunacGR2ME5MXDL9rdIKRB39MLDsXYiDFZCGX7EUCoAvLysK6IxRowsC3NtBp70jTNT611Dx9D0OpZ-kyeMUnPQNDSwvv_6ytHx5fIhuV6hn_PRFU1OFq7WiNUsWbt94UXoBLEzUliB4vS5vLjQQ8OWAyv199j5m14g1ATJJrcjxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=Ug3RlgdVtFnkfi3cNdPxGUw_TFM4io0DFTiMAveJIbSBMPg55tDzLTPStb7q0k7ADbYrwZ-QPkbDXCVJXbheXMkLqj9R2apugfIZRXasjMDyXXrwPayzkTo71E8YSYfAphgxvIVxovySTAFZ5OyRfNPeFJBLse5aXDz5kNZZImunacGR2ME5MXDL9rdIKRB39MLDsXYiDFZCGX7EUCoAvLysK6IxRowsC3NtBp70jTNT611Dx9D0OpZ-kyeMUnPQNDSwvv_6ytHx5fIhuV6hn_PRFU1OFq7WiNUsWbt94UXoBLEzUliB4vS5vLjQQ8OWAyv199j5m14g1ATJJrcjxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=liGtVucxCKKYTkXw_IOFOJHQROqJyEgQm2OP0VhRkxmBveqzKeco4B7R7vAXotHFRtenp3c02PDvznvvSgbpSF1QPUVviVg8fLrMN_HHKPYllMLWlq9G97-DKuAei3fM1ZjyBZpC1mTb79YWt92H2ezlCult_Njg4koPFOXHYp_JOHMZpUE2YZpPGtfJ3dbjLTfek-pMC34CnBAiNVCDY-KfdYUjmaxmw5ZULXeq3-fBa0xWOi6gOXY_bhHuGgvqc_bYRo-WapY1eTqRblYyXt-88zwq0QsR9g6GlptVukDFGSnIYP7BmcM_VVQY6_O5tqBsVo9AmlwS-VmXaqDjlGZ0mjeUROpXmzrYzO0qQUBdikEWpCqVLgsqsVio_NsFNCj9h162jiRCnFSzxgFJeDXCHSHu-CEyE7_90PpzYTPidK6yZJH7dPe7A14VbSLqBnWF39D_YUmdQ9U9-u-_zl54YihsUHuHLEjdePSFoEj25XKQz1fAiVk6ZcHFFcWt4kqWJaUf0Uxltj5G5tPhj2-8tqjT4wvZHZg3cZDR6GgQLZL99VZFjTo07DjdRTNK-YDV32Av1w9C2SXKmEiGU1T7pYHmdhZvu9sie0wMZw4lsJhYg1d13K9Bb3j1OAt9QYCtauhoDqhxgcHz2bU1fHXuvhwwaFL9hg53iHKB2I8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=liGtVucxCKKYTkXw_IOFOJHQROqJyEgQm2OP0VhRkxmBveqzKeco4B7R7vAXotHFRtenp3c02PDvznvvSgbpSF1QPUVviVg8fLrMN_HHKPYllMLWlq9G97-DKuAei3fM1ZjyBZpC1mTb79YWt92H2ezlCult_Njg4koPFOXHYp_JOHMZpUE2YZpPGtfJ3dbjLTfek-pMC34CnBAiNVCDY-KfdYUjmaxmw5ZULXeq3-fBa0xWOi6gOXY_bhHuGgvqc_bYRo-WapY1eTqRblYyXt-88zwq0QsR9g6GlptVukDFGSnIYP7BmcM_VVQY6_O5tqBsVo9AmlwS-VmXaqDjlGZ0mjeUROpXmzrYzO0qQUBdikEWpCqVLgsqsVio_NsFNCj9h162jiRCnFSzxgFJeDXCHSHu-CEyE7_90PpzYTPidK6yZJH7dPe7A14VbSLqBnWF39D_YUmdQ9U9-u-_zl54YihsUHuHLEjdePSFoEj25XKQz1fAiVk6ZcHFFcWt4kqWJaUf0Uxltj5G5tPhj2-8tqjT4wvZHZg3cZDR6GgQLZL99VZFjTo07DjdRTNK-YDV32Av1w9C2SXKmEiGU1T7pYHmdhZvu9sie0wMZw4lsJhYg1d13K9Bb3j1OAt9QYCtauhoDqhxgcHz2bU1fHXuvhwwaFL9hg53iHKB2I8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqNTnMzrGtGMSRodDk3x9owzpTmKQdtnQ_sPRPEbFBOfyQsleDevqwkZCOHgv7j-HDgAWOOalQCqMnedurh9L6B-1hAnrwet6HyQoqBwW4Zsi50kyEgap4zw1SwGsY-Lh63MH7e1E2SqfyU49Y53tnETe36tNRWZFaSJvi9wszzTp4bU1KeKSwe4N-k0jHnYYzCsgQjgcNsEr6SJpItMx7r23i3bTBzEzpEtDuFoOoStVhhnm-h5dFg2EXxw8I0ixxZgBeJPhgH9VyN2EVHeyxAsz1jJ3oOQYzBRIbt3wkAHVPYCymiiYsqRffKQYjLjVjZNcaedZHt5E4LZH5M5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=dt2IEfP5o5lnO7UisXTTSir2upXyUdJA5nBCY32B4j8CEeMpVeqmxpQLbmXRCdBl0jVSMXCCZUvh0c8ecLdLX_qxjzeGn_1w_-OVsFe1Ntv5sKQZmZuVVVLVogVNPY3BS5KHbCmi0eOI6b7FdpcRoH-Y1KRAs3iG6LFkbrerka5MNi7aV5Bj-wYVkKlgt95xW2RCIiNYYMUz14u7-QCANaJOlXJG8PGLJJ9h-nyOMguoM3rcgCNxEkrsYDq9dqSMFuXGNsv_C5xtgQgd3nSjJTlrKJGG48qCURFl4Isqr8zNN9zyRKPVkG_eA1tqz8jD_5z9ImMitmMFR0ckrbpxhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=dt2IEfP5o5lnO7UisXTTSir2upXyUdJA5nBCY32B4j8CEeMpVeqmxpQLbmXRCdBl0jVSMXCCZUvh0c8ecLdLX_qxjzeGn_1w_-OVsFe1Ntv5sKQZmZuVVVLVogVNPY3BS5KHbCmi0eOI6b7FdpcRoH-Y1KRAs3iG6LFkbrerka5MNi7aV5Bj-wYVkKlgt95xW2RCIiNYYMUz14u7-QCANaJOlXJG8PGLJJ9h-nyOMguoM3rcgCNxEkrsYDq9dqSMFuXGNsv_C5xtgQgd3nSjJTlrKJGG48qCURFl4Isqr8zNN9zyRKPVkG_eA1tqz8jD_5z9ImMitmMFR0ckrbpxhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=kslGbcQbJz3IL8yzHU7XvXjByjBE69xO5J__r7vhGZAg_6UfgYe7ueDfZrBvYN0lmz7PGrOY3POYiziXNOW8iuAMCQ_-CwbOkY6H4FwKIK6ClRH7IKdJhqw4VSrzs_yDO33iVjDaSD-cKgdJmf4S4DdmscGF2AvD79sKKf09hKL1pWtNTjU57FhdU41GbAU6OJbGbJXMUkr8K1mZN2PMovoVdPuPra2nqgsnFOfj89PjrzO4sVvabPbEWVNSQnIbA6Fs7wNVpSx1v6NChdaVI3gvGW7IJESbwk1iZjG1XUCox4_v9GOk8oKaVdGfRNuwrmun9hXPAKaDun0tPg5LAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=kslGbcQbJz3IL8yzHU7XvXjByjBE69xO5J__r7vhGZAg_6UfgYe7ueDfZrBvYN0lmz7PGrOY3POYiziXNOW8iuAMCQ_-CwbOkY6H4FwKIK6ClRH7IKdJhqw4VSrzs_yDO33iVjDaSD-cKgdJmf4S4DdmscGF2AvD79sKKf09hKL1pWtNTjU57FhdU41GbAU6OJbGbJXMUkr8K1mZN2PMovoVdPuPra2nqgsnFOfj89PjrzO4sVvabPbEWVNSQnIbA6Fs7wNVpSx1v6NChdaVI3gvGW7IJESbwk1iZjG1XUCox4_v9GOk8oKaVdGfRNuwrmun9hXPAKaDun0tPg5LAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4Ndn5F3CzUpqK71iYRyAQYOzcFBacD81GhacrtWQHGPffJa9HseHfwb5YFzyqGr_gwH7FAlfX4Mn_oIzavK0gXTBl2jyGt_LLv_A0-hhwWIOF4jAHMdb4OO8uNtI0XZAafdPED-xHkU3MuKE7V7Moad9yaYk0sgdMAt2mNCHCNUqVXFERPxnmH7G5yfbkQGhqL8xMBo31b8Hk2zOkZyF3CySsEq2Fk8yzcp2bvvWOV4f0tGUXg3mVzm4SQlD2-QWaCUJ5sXHIJeWDNmk3xLkX_GqorJ0KcjugWVMqq2XPWOhpVO49JdZHq1MEXBSXJMtVUCM2EU6PkmnvBhTP6WLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIPjFi4RoyiRWIsG19mHuy0nhA_8V46sKW1w1CZeaS2e3nX3TVeyux3uh8t9Fd1V7JH7gtD6b7LAXibdWlzFn3C5fuKabIfUYvLL8WxioCHEWGYHpy6ECG77ojPSUi4BGKTMOwyLXEOgpRMiMxrJ3eSm3kWfAGdU23HHgUgAEc9fs5jxTpYbrOSrJ-4DGygcIOev8RL5gw3MMhw5zWeXAiI6-kO_BguVUvpYsFJ-olj9Xo9vc3b61dIXOUVRyFoaZ_DvdeQD43ob5MvV5AzXYwaUpmDJ5AoZNI1w6BkfNm66UMU-YA5WxATWJBV86Dl-KIgonU0n3TSbZAg8bRNu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=HKGrjYhdzSmn5M2X1vD4Xm-HaEixb8hV6ovNpaGbU6gahsy5eLwwlbx-ZKJMtyXiHHHOWdBI4r8R4WyF0GZSzVcRctQ4_JZLQ8qay7h2JE2w2Hqr0aonozImbmn16uPZEs92Q7umDmeG15dmSnodhAzkP_TO-pw_Ha6w-VSGG3N1oI1WXeMhd8FlUIpUqkea9gm-O8EV3xlixo0vVdrZKBhaHdEcePtEkeEI9XMzv-xKdYGWZPsW93UmwGQpj5A9GiB9BE4-Mh7P1vluRNey6Z8XWe6oYYLcR3I6fkXGmDEj8fmb4Xf8fgxRHK1HD3ZV81JM19Rqb1y4qcqH3Gj00A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=HKGrjYhdzSmn5M2X1vD4Xm-HaEixb8hV6ovNpaGbU6gahsy5eLwwlbx-ZKJMtyXiHHHOWdBI4r8R4WyF0GZSzVcRctQ4_JZLQ8qay7h2JE2w2Hqr0aonozImbmn16uPZEs92Q7umDmeG15dmSnodhAzkP_TO-pw_Ha6w-VSGG3N1oI1WXeMhd8FlUIpUqkea9gm-O8EV3xlixo0vVdrZKBhaHdEcePtEkeEI9XMzv-xKdYGWZPsW93UmwGQpj5A9GiB9BE4-Mh7P1vluRNey6Z8XWe6oYYLcR3I6fkXGmDEj8fmb4Xf8fgxRHK1HD3ZV81JM19Rqb1y4qcqH3Gj00A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=rTagifEGYz5Ty2P1sxqEa8hK8USqVn1S1zIiWDjtOH6HzoyxJFMAEMiNuCDa-PCuLWXkdHPzNOkU3WVGofbuGBkgqq-tyXW_SF5cGU128-PQK_ejYqVMUjKRV-0-etwuq0otLIExV_wLnjo5tD7nZyBKGONb5pOnmhBav9R4gCUHx9sY9O_LAMpbrhrnfleJOoh-lkdsSJvLExGqHuGVRYwCfNm_DZltAdvbuZ4mLIwHl7OWa7csXzwt68QGOe2YvyAkz-bvBtjpPbQedOGuIQJpg-0cHhNhwcrGLHq1YnOUAV1h0cDmbJDCxr6UXtf1yDruAdM94kV3_Qs0Bs3u-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=rTagifEGYz5Ty2P1sxqEa8hK8USqVn1S1zIiWDjtOH6HzoyxJFMAEMiNuCDa-PCuLWXkdHPzNOkU3WVGofbuGBkgqq-tyXW_SF5cGU128-PQK_ejYqVMUjKRV-0-etwuq0otLIExV_wLnjo5tD7nZyBKGONb5pOnmhBav9R4gCUHx9sY9O_LAMpbrhrnfleJOoh-lkdsSJvLExGqHuGVRYwCfNm_DZltAdvbuZ4mLIwHl7OWa7csXzwt68QGOe2YvyAkz-bvBtjpPbQedOGuIQJpg-0cHhNhwcrGLHq1YnOUAV1h0cDmbJDCxr6UXtf1yDruAdM94kV3_Qs0Bs3u-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1AYc-xl065gCCFUVe_UAFhmEGvh9lrOBDG5IMeTaOnjTfLMwzsPN0OLDVMG_B4RW7HBD8INn5ZjQUSSRjUcZuAigy7XzU-lPOxXL_iI8zzwxCpcS1IXhOpSTQMp19SYtGAoBzZZ5Yo-E5LFB5Uyjr4oaIDnsD2i9ktm4G8cD2qjP0Cw97Jxx9nDSZC23diSuKhR9ZkyS5jJ6nHb55ZUtTofppxM2XZoLBhlVTpg37YTRXFctuztLsAo6zSzd5B9avdafwyYiLfYTs1plSAprCjYizp7uFDJsFNbBtUWc9Tk_Zlh6dwaqkcuxLgSZew7R44MQQ1cOjkEwX7JpGCt3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUREMI3t8ga95wO4h3AmfzOBdmB7b3_QCix-Xtkn5t9KPjgqORxLws2HzNW-PuubcCtq8_w6Kc5iLF4dgE5wHnZX6QTBbl0JA576vLwA5U7KheiOOvGSQjYxb_7dtaf8AzgQlzBLJX9asivD0PNIXzKfeSqyX2khsxZfz50ROJR8gznKHTyU4oHLn3-w5JSff4sLmhMsnFgDf51PO_QepCrdRYy2bCE0ObBGd0Kx0pTfJc8nBNoNWQ8qA8sy5LHYYyiAmjmM4dzJjZoLDcBYjnwqdkADjTZi_mTzUgApdf4nMPAqmKcG80T-TNnSHW9QnTnOLMfTLTgMHNRO5VnP6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO_PsfdW6uSnX_0SIH3tz-762YiyHic6EPKswli_9QLR5IBrQrS1HozsP1JHKxKrYo2KIgbYovPKYCc7sXmEhXC8rmSQyf8rJwJ1njzWluQJg3O8L8RhQdtZsD8jKEVFYoCGwPV1WTs9_oRgV7kIgERRiumb78kCViauwq0u1Tia_kIjjMdtGeO0O1mncbNjkETm__fWBiSohHHKbHyeDpici6ENnJLq2DkM1mFMmgk0pKAhafUD9zxahKMejMmZEN25XJACK8UqRHNT9XhfVs5BpVmNNPI1zk7NYY2T_I2TXE3u6KQAWZRgjjIUz8SmWcu49asNlU4i0w12z2BgDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boiKJfKYDZpYsbv7zr_c-rbQ6ukJEgCMq8QZrJ0Gabet4MuiGMHS_lfxV2Iz3IXrg16mAJVQe_vpjHeoHBMBrOWLkeMkhTn-TMD22L_QbKexwpXHY2s0eDAMW49DN3yJEWLU0aN-1Z0ML4aeTehjX8mpLrwM5sIux3Tis7egdOsFjvg2joESn_EPHipqnBXWqp-HDFJr25lhdYYtr5ghn9AqnOvGRN8SiMEhucRXh-L9sbh1M-SK4JKVYCjUDcP9HzDWIVHMSvWoslgaKcKjE4Wx9oIQoU6PuX6iOBp1y7W2oySo-8WU61gqtlJkovZHFaWnYcxcXPDgegRwIGmINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=RFwKYWhdgXT84DdUqx0sFb7macKY_eiWeerahigeS54e98_rxzMgYgRUF01uYzE9Dhn5xpQ2awqLqvOAZxnXFp-xM48-N-D5c7jao7BnOvpBxdwJdYb8FNDcenGYlk8q9wmo8-v9wHOrvvAqEjOqlA9sIHDuHJGfSU5ZyZeq8-k10hYR5WqeBbrfY7-N8fBAAFS3BB_INP1Fuw3kT6L3TrRReWUKJPl4WYyKhANdYO6v0vi1SfjR7AW06J3HP8o0gdXOSYMoDd30ZSw_F4P6q0OfX2WXy6CSf8Tep1fxypYM_reNwlEIp-hO59ClQDiJ86sczTNkXLotkQOA0tRwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=RFwKYWhdgXT84DdUqx0sFb7macKY_eiWeerahigeS54e98_rxzMgYgRUF01uYzE9Dhn5xpQ2awqLqvOAZxnXFp-xM48-N-D5c7jao7BnOvpBxdwJdYb8FNDcenGYlk8q9wmo8-v9wHOrvvAqEjOqlA9sIHDuHJGfSU5ZyZeq8-k10hYR5WqeBbrfY7-N8fBAAFS3BB_INP1Fuw3kT6L3TrRReWUKJPl4WYyKhANdYO6v0vi1SfjR7AW06J3HP8o0gdXOSYMoDd30ZSw_F4P6q0OfX2WXy6CSf8Tep1fxypYM_reNwlEIp-hO59ClQDiJ86sczTNkXLotkQOA0tRwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=EjXlWtt81m5gscGzbDg9i56EEwcw5Riz-zCcltnfUz3QNY8b-MEWhl6uhO0nWYQijkUXD9kAsFi36S1xQI0u7dgOee7-6C5CJ6Dn_ixeZVPeKa5R8VkrReDOMQGwwW9TaNJgtF5HZrjZvDLPhk0979FYNNF4EMsuvbQ_p0NAMc1EZNxCnJkN1wXBdR0XeLw0R6Kh0v_f64idTWN04oSEK_igWwWvDPFquQ6IvizeWvGuceIxJ82UYZFR2WP02CfJSvHV9ulU906EWRts969i21yPE1H9OyPPiio47Ih74n5tKP46Fn1syXrj2unGBEQOW88n7tpSrykykNhy7Vl10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=EjXlWtt81m5gscGzbDg9i56EEwcw5Riz-zCcltnfUz3QNY8b-MEWhl6uhO0nWYQijkUXD9kAsFi36S1xQI0u7dgOee7-6C5CJ6Dn_ixeZVPeKa5R8VkrReDOMQGwwW9TaNJgtF5HZrjZvDLPhk0979FYNNF4EMsuvbQ_p0NAMc1EZNxCnJkN1wXBdR0XeLw0R6Kh0v_f64idTWN04oSEK_igWwWvDPFquQ6IvizeWvGuceIxJ82UYZFR2WP02CfJSvHV9ulU906EWRts969i21yPE1H9OyPPiio47Ih74n5tKP46Fn1syXrj2unGBEQOW88n7tpSrykykNhy7Vl10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=ffe7I83BU2ZCVDxSo2EyXUcPFUWHzkARaMwVgLCpcti8N-De-pBNEV9umsv7sxtPoCLfYi0xIz1Mb6JQJNCpqwUyxaNFaKQwyeGPKOXwgQM1TKna45vDfGpwYvtusVTaXwvXcsCILG25yJi2d6wBUP6dLqd136fOWz8S7b_22TUe8GSd_DnAILDNY2lMD-Gi1LQzmTp3XeXksndTocYJR-i-ckOH5bSFWlBvVANCQMJ0B3MIZ6zONS9YCFxVYRM6Vopu27UJsSlpGwwCRJAEkjeyABBr0VImY67c-qdgH00YVllxKx38VNiVvp4DlN81hM8Z6c3aXFOEqCPbE7upIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=ffe7I83BU2ZCVDxSo2EyXUcPFUWHzkARaMwVgLCpcti8N-De-pBNEV9umsv7sxtPoCLfYi0xIz1Mb6JQJNCpqwUyxaNFaKQwyeGPKOXwgQM1TKna45vDfGpwYvtusVTaXwvXcsCILG25yJi2d6wBUP6dLqd136fOWz8S7b_22TUe8GSd_DnAILDNY2lMD-Gi1LQzmTp3XeXksndTocYJR-i-ckOH5bSFWlBvVANCQMJ0B3MIZ6zONS9YCFxVYRM6Vopu27UJsSlpGwwCRJAEkjeyABBr0VImY67c-qdgH00YVllxKx38VNiVvp4DlN81hM8Z6c3aXFOEqCPbE7upIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=RyJqkspF4TMQw2y0XkZuzKZAzMtQ9d9ozZTXjKgRfzriwUd6qNHou7vk6vXLLGUp35py4NWw9AYK5sq2LoOqjQqJPVElQPY3lRsZ8Uqb0N8SoMSRC4vbGPWsKdL7Fh8b0JME-z83anb3Ca70O0fp8kgohD2X4riq4njrc_0DB9i_9eXHgULxhkDBp3cTLGXDj5ucHVTrviawlGpC_vmB6QnGMKDE4udSfcMaD-5WkyYf3j-TFf9keJSQE5J_Z17gIPoPjRkxAp-JU4ZjnDjW-U_SdfryMdqym9UHc1ztGSsX2C38CmclVyL9UCtvPO3jZhWIzo7k4_wK_muHdUZeuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=RyJqkspF4TMQw2y0XkZuzKZAzMtQ9d9ozZTXjKgRfzriwUd6qNHou7vk6vXLLGUp35py4NWw9AYK5sq2LoOqjQqJPVElQPY3lRsZ8Uqb0N8SoMSRC4vbGPWsKdL7Fh8b0JME-z83anb3Ca70O0fp8kgohD2X4riq4njrc_0DB9i_9eXHgULxhkDBp3cTLGXDj5ucHVTrviawlGpC_vmB6QnGMKDE4udSfcMaD-5WkyYf3j-TFf9keJSQE5J_Z17gIPoPjRkxAp-JU4ZjnDjW-U_SdfryMdqym9UHc1ztGSsX2C38CmclVyL9UCtvPO3jZhWIzo7k4_wK_muHdUZeuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4u0jkfxBj1HbVcEoV0A5p4tRvKwnI8weOVCkRmEJKmtuh8YrUz8ggvx9p7wDuwOn0kN-Fxy-U5EaNc-f0HyHKWMcGuCuD8Yht6ltv7op1qygfVDmK78aFZnFkjvPzvk6N22NeXJzU6beA4Kr7WKHIT1h5ZobddYFhPqJpUn2xKdNGt5DFy9EKmTSrsFqPzePWxFftZ69X0N4FSgwysGBUJFlPzaSq-kM46Q_ICQi0lOXCH4aTeuwQWDHUtHoQlLtwIZCt7BqcyhHs6HleKKQXf78bZqvCNHEQJFroi6VCY1gox64cRuH0zzajr4kxE4tb1x2upeIcJvqy3ghnjFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=Ov8dXh5zJgKI2M2d-BNowf1VBYx2jFowbvy1p-o6ECtcsc1Os4CFZQl5SfYmx88zUZkbby43v4B6L-af_dzoAN0h_BYGcN-PRLrO1MSqp77g5dIDswCRkrA8NimyitOzuwJr7wn9_ApHN27dpejQ0OIF6dQ-AgaVmYDBGfsQ1cCoXv5n2L3Vry2wHh9rEWAk_eCgKNbou6j4gkKvnmLBxD2yDe7fmHVJRxTTHlfy-UK8NJF8vb-Qxe6Tryf2YvrlIIH94G408vQvE1d8gIvVrqy_f0wh1JhBWCMiD920xHwTB7udt2Z4kWW1jYEmN1eYY5KYCOa2LKR3sGOcVmJZajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=Ov8dXh5zJgKI2M2d-BNowf1VBYx2jFowbvy1p-o6ECtcsc1Os4CFZQl5SfYmx88zUZkbby43v4B6L-af_dzoAN0h_BYGcN-PRLrO1MSqp77g5dIDswCRkrA8NimyitOzuwJr7wn9_ApHN27dpejQ0OIF6dQ-AgaVmYDBGfsQ1cCoXv5n2L3Vry2wHh9rEWAk_eCgKNbou6j4gkKvnmLBxD2yDe7fmHVJRxTTHlfy-UK8NJF8vb-Qxe6Tryf2YvrlIIH94G408vQvE1d8gIvVrqy_f0wh1JhBWCMiD920xHwTB7udt2Z4kWW1jYEmN1eYY5KYCOa2LKR3sGOcVmJZajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGMDAMUniqfa73tdb_-9bVp1K_sV0FHrE1uAyjQFNWr8KW4USQihTL1RgESJDgQjjF4SaPKjiTgAcBg1RrgKwB9tKA6BCFa_z6JHvoAyMssZIZsvpl-0j8RpR1QwfzD7ip-idjeTvhJq1H6RcRbovLIFjarBxbtBH8MmOxhoQSOC_8XWff7TmNIV7sBZrfyOFf5gLCxcSG0EmgGjB5pq6e2VkWnpEC6jU2-lJ4fHKT_-QanafxG4FJMdN0vcoUdS0eb8nTiIbSKpXWmDEDg1YdW53cVyGQ-EHQtus1wziO4E8eOIVD1YhZooNlvTucCG2qMHw9YB-1duV382BYZRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY6tYDUfClL0rS-29J8OBA4vrUfQTTwjORs0NxL-fiR3DDBQksNcwMqGdHwPkaoG_PdPuTaiIkErHDzOwi5B37yHnM7knvD2283mLujREBIbaXrhqYOUJMIeMh9GN8NddBjzIZloDRdJNc_yjW0QOIXMDcMN8OR4_nhmu3rzrY4wURak_w99LMJY-B8APiqbbqD2RYbkWcdtDg0jYOa833rGwM7psNj5UlEf2-mg7AGWT9Ore8dniboBOl_Zw47Ar4AtE-xiIUsAsi0TwdSxmoDBbkkwFPEuvm72x3wwqzTZu8EIRL9h-b2hMnxaTXZp7t-CMtf7ko0l8UhdLl0hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWpJaqRXDLh_yY1M6_fNjs4-6zM5tg7T4zqmDbfNCOi_khdFCJ0IBZrDte-EUutupwTF-corRXStIP_koZEcAeZR3xAy5uMFptI5ixp03Cv1Eh4AlELVUd3jypqhA9Z-oLjm-7LmFwTWeJNnRTk7RPfFJRgNGZ1y6cS1t39TrFfocxXs2NbuKuHLV-FcTKxxjb3MiSa0aL476k4AgLjgPOAPxeKnqWrwhzFHgXfm2zYxZrcdiSntgIzziLQVwNmm0_ezhnseXjH_e0i5iU3Be90cCd6qAU6e4K6whAvqjUAigUt3jUig8QCe5_HIYT6kNhEtTkEihermxuv9ZXEByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rA6nLdaq3UMguOQLNbBMSziVFskhy0C2iJFGWCfM4Z--BDiYIg6ESe7k7dK821qawEiInr6Pt7-1Mjvor7PqkBZ_GElzGExSo-RLGILLMnj6OQzUVl5NgF5iMRpoUj6MY1fZgKSF3p5Zl74LcuHKUuSyVU2_4wpYE-HRbthtAic3XoGm3OA1h1Z00KSRLm5Y6TIdQlJEapfPgaSMaMgreuEWtxGkSWpQZCrDaw3DjDW6Slvqh6Mmb7F7O8pRfJt0HycmAFpbq6F0f3ZqbDY0I3GINAINnUI14G6GXqqbzMXy4e02RElKdOgTfMKbiC8JGd5Fx_ZDJBnx2p0EtuNCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=civaa6NMoJ6PyoUfOzoi-gn7QXPDN35ms1Y_m-yyffQDuu_XLmKDOft6wDiH9JbV12FXPd1jdgerCE76lC1ZeApJCeZVbbD6D3oG9BOwnTcTfN-P9LZmlHN44WDCQf1JLXrENZxUhFas-87r6OZEukkeXLhaaApT73vvzu_HX2B-JREmiancq0hK8eK5k5TmVFFOdqgSv692iOOah-bOZ31-Pc6vLYAiHYlN6M1hj3bwpNVM-BVd-oBeKSnIOjzTeqGedCvjCPWpMVIyO3YJ5nyMfbDcXDvUpeOML6gxdQR_xHbsEyP7PxjNIwMJfqtbjWJYl9PC_imlLVyBwTBq1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=civaa6NMoJ6PyoUfOzoi-gn7QXPDN35ms1Y_m-yyffQDuu_XLmKDOft6wDiH9JbV12FXPd1jdgerCE76lC1ZeApJCeZVbbD6D3oG9BOwnTcTfN-P9LZmlHN44WDCQf1JLXrENZxUhFas-87r6OZEukkeXLhaaApT73vvzu_HX2B-JREmiancq0hK8eK5k5TmVFFOdqgSv692iOOah-bOZ31-Pc6vLYAiHYlN6M1hj3bwpNVM-BVd-oBeKSnIOjzTeqGedCvjCPWpMVIyO3YJ5nyMfbDcXDvUpeOML6gxdQR_xHbsEyP7PxjNIwMJfqtbjWJYl9PC_imlLVyBwTBq1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbnfFIu-3tjWQSktqXQgFUmmOU-yWphTMaeagFQh235USy57HzV6FC_F-PntgqXCRXUDReo_bUsmyOVPwf0ds5Bs6_Z3mcCiqjjDsGzRxbgx0ih7pL59Q70aa50073d3DG8HLwTBeX4ds-XA8SGb1SqnjOXsK_AcfqH24Z7irD3xpL-BxMg4qTEwxFDGX7WopFdst02tsBdIllcErwWjsGe8fGXI_oNKHpXQPXf1w41NAsGkfpWuwMQEyv35OdF53FkKHnzpkeHoeB9NE4MiDgp8sGSUGM7PvrzcLSEreFV4HUf2KCNDh5DNkSSGMOvn-BoLdXc71v2sQnP1M_bkUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=X-sWsgQ5iugZ8TmAurwzf0XistLarNP49B6DKTr1l4Bwb0uU3rMJZSOEjVt8JbIvwqusrByI3w3rZ8txppahZ0tUEGgF-q5wC4p5lYTtJCXSzby7vRBSLUb_4ujRg8D7t79i6xy930P0JNa-UDYdp0Qkmz424ziFD1n9LkwgriPEu634CSSq7Pu25xhNKOJXfACaCUvmADVUbY_ARRfKUTTZ44UENueA06nzmLO_JxHiOSvCuhV2Jwh0pFjZjB8eVmuv4dx0Q53X-o3jr0ujUNHZrinpHq3la7TPUXNf1Hy6YJApLlhr-U2wZnUalfwTsxyyaxkQuDk52ef30sVh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=X-sWsgQ5iugZ8TmAurwzf0XistLarNP49B6DKTr1l4Bwb0uU3rMJZSOEjVt8JbIvwqusrByI3w3rZ8txppahZ0tUEGgF-q5wC4p5lYTtJCXSzby7vRBSLUb_4ujRg8D7t79i6xy930P0JNa-UDYdp0Qkmz424ziFD1n9LkwgriPEu634CSSq7Pu25xhNKOJXfACaCUvmADVUbY_ARRfKUTTZ44UENueA06nzmLO_JxHiOSvCuhV2Jwh0pFjZjB8eVmuv4dx0Q53X-o3jr0ujUNHZrinpHq3la7TPUXNf1Hy6YJApLlhr-U2wZnUalfwTsxyyaxkQuDk52ef30sVh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=lsZZ_eIWZWYaS_NyfZbUJ6YHoavnsphmhE-mXsUWSBjjQwaYfBUwND39ZAEjNT7iJ1Im5deFZ_oBEQ7AnwJNLfPIwAXeondrM54eGwNEFaB2ZCopFpc1boYC7gCfe1ecX1MBKA8pPmrwAw1qeny_t9HkADkoVE54VOaAlBSuI-NZ6ZfREDbeD6Qt3U34X-lNGIDMJwmtFAs5RIShpQ_mntP6PANAQ18ArY8wNZbOFzvIM1uVVKsOVMZCVa_rtwNXbHP-yLfzAj_5N6jEAyXw_XgzoY_3VuJKAP_zXnVcTARuYUbgG34Q-TK6-Y9J68XOav0LhhqQjJA4_PSA_ouj-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=lsZZ_eIWZWYaS_NyfZbUJ6YHoavnsphmhE-mXsUWSBjjQwaYfBUwND39ZAEjNT7iJ1Im5deFZ_oBEQ7AnwJNLfPIwAXeondrM54eGwNEFaB2ZCopFpc1boYC7gCfe1ecX1MBKA8pPmrwAw1qeny_t9HkADkoVE54VOaAlBSuI-NZ6ZfREDbeD6Qt3U34X-lNGIDMJwmtFAs5RIShpQ_mntP6PANAQ18ArY8wNZbOFzvIM1uVVKsOVMZCVa_rtwNXbHP-yLfzAj_5N6jEAyXw_XgzoY_3VuJKAP_zXnVcTARuYUbgG34Q-TK6-Y9J68XOav0LhhqQjJA4_PSA_ouj-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=sEV1RMPbehGUdsnVl5GhIsJHKD07BJzH4hNiTozt1PcXVLuC7DD3kBChefwFEpznhfLyHp6xOiV_mKgRf5og-BpsqqzOhwM5m5PsgvIPykz8L_MqLU8Yz-x_QM55wR_Hz7j_Amwwh6kJd6CZ9SzWJi65-o05naQKdu4lo4oeitPCOPPbmxew_KANzvsuw3YFo_iB06zXD8rAwUJ69bsyCclZSu5jJ5_Bvs04i5qpCMwsCvP9IEXZHtXUPyMZCJG1Mf1jMZvOt8nI3Hfk_huhCc8Z1s3dZC11uUG4aHYSjJ59MswirN9oHYa-ESlbcJkiHoB36iS63y1aaSrJMQOxvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=sEV1RMPbehGUdsnVl5GhIsJHKD07BJzH4hNiTozt1PcXVLuC7DD3kBChefwFEpznhfLyHp6xOiV_mKgRf5og-BpsqqzOhwM5m5PsgvIPykz8L_MqLU8Yz-x_QM55wR_Hz7j_Amwwh6kJd6CZ9SzWJi65-o05naQKdu4lo4oeitPCOPPbmxew_KANzvsuw3YFo_iB06zXD8rAwUJ69bsyCclZSu5jJ5_Bvs04i5qpCMwsCvP9IEXZHtXUPyMZCJG1Mf1jMZvOt8nI3Hfk_huhCc8Z1s3dZC11uUG4aHYSjJ59MswirN9oHYa-ESlbcJkiHoB36iS63y1aaSrJMQOxvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6fkOaVdT7ha1d8NaAQELP8zOfkJ695UNO41m-lBDwsFo1X6NCfFivJPHHgNotxVfn-FfGyhEE0KqsVuzblu4JjbETsue8AkRfb2U9CBskLRQ6x3_bkUvuAuvLzLfwS78OQenFL8iRhIdTvjztrNfz9RRIXno-cYpjzkvExbK6JM9JW2-4IPHndsGJlmjQ526Ll1eY1OkmK1sC5Jxpi41byu77eB8qT_id6VGkwe8gTszp6yaFRzzQQ10pr1X_3FRt32N0ZNVL_ELIeDGNg8fUSxYUAOL5IGZdu6YamkUjiM6YGO8F0lTTNRrlNuSjebHvP1894cfetkhRVblZ7ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2fcDsPy2iuHFb48eKWT5-cAPjmbH3va3yvkI_WwViESgcvvU8FQp3vJVjVH5PNY3xiYWI3cG1BoJnCww7PdE5Cpm-TZnX9On-GMHkWvRx1oDAZBibujSCuMTiO8Zv6u2im4fXIFKDfw17BBDJhMke372pSBfoDPix50q1YMBj0U5syWa14gSNjSyN1SutO2Ri6n1IuibYrVPgnL5QJlb6hLicWOfLEEfp0TO3jROszcV0TF_oyMw5gPKYOp-iv1reWPodXWOK4WBwIb_CQTphJirUYPN6yr5zUH4PTYf9dgMycRD6CQqhMjw_dKMTzXDKhyM_mTisg7ILe_qQESuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=d36nMMbKK9e18lgk7Zgsxqj2q95ugpybCHB9TFM09P8WZ4hQ_sh1dWf5YhCX2tYOwyCWDvL2xJ9XPinQs42WYcm091E_WElEciAH0Xd5RGfdQDrnlHvlaGllV5F4vvAHT8NeW0l7h3ZKiCAQvxudpvmCGNtrFM3btP7lXMqpH8tVvuuJswJ0Vmkjw1Uj0kLCoJGZ7zIoQgEuyRiMsFzaG1e8lZpdcp3sTSehW-P2EzapeXFh-SvgkxxdgRm0dnIyGqHRkdxOIduiZOOGg-KXK42l0a5dBYQx4seupJAKT2J2tZ-nPlSyDcnWYz6FU9_-pyx07xQCuCcL3McqEpJJlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=d36nMMbKK9e18lgk7Zgsxqj2q95ugpybCHB9TFM09P8WZ4hQ_sh1dWf5YhCX2tYOwyCWDvL2xJ9XPinQs42WYcm091E_WElEciAH0Xd5RGfdQDrnlHvlaGllV5F4vvAHT8NeW0l7h3ZKiCAQvxudpvmCGNtrFM3btP7lXMqpH8tVvuuJswJ0Vmkjw1Uj0kLCoJGZ7zIoQgEuyRiMsFzaG1e8lZpdcp3sTSehW-P2EzapeXFh-SvgkxxdgRm0dnIyGqHRkdxOIduiZOOGg-KXK42l0a5dBYQx4seupJAKT2J2tZ-nPlSyDcnWYz6FU9_-pyx07xQCuCcL3McqEpJJlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

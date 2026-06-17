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
<img src="https://cdn4.telesco.pe/file/l2F25VWpSXTZAfmFUCSH5fyE2H9lvUDXTki1qNafgRmMwv7SYpN7V6kpB-eJr4J0enl-j4OPLYJxtPeFAGoiSnVE1ohbNBrfO2_7hqq7KIveY_g_MOmfb_Vl7e0FDdvIzG_ir3emmeAhGQnm3ZrtHA6PlgKDQ6eI_6YVSweJidtiMPePwHFlrtRIfd0XMDIJgZAQN3lzuv2pzRAynsz-kQV-aFwRvj4FOgfmgKlS7zN30jVw2QkKg-iPwalNNStOhJ2mnM9pjpuDo5S_MRuZNdDJs6vjUS_gOzwRs-vLhjdbfqoWOzOTob8IjJqqODac0g07xl_SwH2FmYvWNb4N9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 306K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 20:57:42</div>
<hr>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDprcrPkt13CcdzsfOEcctL-dAkFVGleVqWsxQc7IbxJ7IyierK6LWgLe6J0EaNrgUFcDoQyFHlpL9w_nA7yxMIRI3OaxTB1Mb9LDaMkB1vhE83twCo-ge6vURj7h3RlOtTcgucGpwJWZQNDc9Nfh5Qf5iX90oAFINE1c7AhhvmpbCUuudeUaegVyNozDjBnzterj3vlRx-i3oiytk_BUAZYxIl-lTYo7FEuUw3B4qZ72skKerJtXf05PRd_uANa2aFUVX4J9Zj3166a99CLGAOEGoefyP2ZYy41OzF4mBMuVKPcassKAik0_dkybEx3eXuMKvuYbedMr_ic9Qjg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/23704" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwSXe4L7NIVwcyb4x4-oof2ct5T2cglbSE4BIm0U2rZ8zbMsMrotd_JjdgaN2Jec5PDqE_Dsd5-f-LGBJiEAtGSfgj1outZOjhgW19akhcJBw1LVXGBifm9QGvvx1Dt0CxLOkONhkAGXlx5yHw3mqtdMs9AWcik2f3X9IstSFdZXQFDjWRCsH71DKKp1KLRJD4-6gFHzADVXulXlgkRECOVwhJxNaRH8WLj93aHJMbWz1D2-1ojC--jWjzJKrB5ujaIB3zKgq2DmU145R9Q3hYeCGA9IlbRlNZk-zcJTPkACoj9obiZ3pngNb26FehTppnoIBWYKRTeUP3O94QBzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/persiana_Soccer/23703" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_G0dJt6PHz3pNmsOY6mHQyKjsEGIF_i9in__j3PpJ0WiZfNb3m0NrgZ7JVXv4eCi1hr_VjqufHyhOAgVlFALi1DCmirS0k_q2j9Kq_XpHwttH2Bq76Frs6Rh65dI4U6yrYC7mn57029rTbLduZ1R05AGVT_M1YjhOgiV6JwFY4Ma-r_ceL1bHV0zoMhUG9UzdPnwCfXpLdIdIHQ0GBDky4ZMWWJq7DHqCA9eNWlhdWgwlrwCTkd1WJr2lDEsn1Fs9CPITxpi5NpSBf-h3OVac4uGtrVtYm1WJs9pW6_lOk1WV_6GfgHVE2IpUVvLmIxe-81PHzITbnkERxrSpmzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/23702" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyO7Y98tLjDP48s_qGd61MTty7eCF5rFhi5hQo0aTVh2CmV1q0BwvaMibkiQ7flyn2UWHl6zKCa9WjBsYQdbNlH8CaWypts2WMtXGwAJykOXJ_UHq4tZvT8-bH5da-VWv9vIOsRcIAxODXX-lEO2yWqP92ycHoJpmZyv5AxB8XWebg9rDyqgrCtGCGllPGlGckEFOtAdpM3XYIO-OBI3XRdEN8XkGHGgZwGixEAGHVyaXCVrHOLlKSiU2t-1qGql2vozdUyb9G2pmQxfH5hYBYASaiL36d9hi5EHeg8t_TyVrh90YitlDMJA6hTMqyhXDeVwa0IcE8Q6PAB6dMBtyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/23701" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKUlg2jk1xuvWkBe_GzdXjd0YVfhSkOVf9Mg4QFwQHMscTO7222z11KMu_3LuOC_my-dV-Cy42C8yw6D3maTCk0k0Pt-7wFG_rMer39xDeXx5b-_uEFtX1aWfItMkRbq9NJZO2rQqq6MArihDGySN1sLYcN9nj3yCuPurhF1TCR4GtU1RyCUswmNd_wa9tZfji4sLOR1TVHNuE94KWfOd1Y6azKMPxrlrIYJ6jZDrSUgXwbUvQYLZbHQJ1x2VP4JXjoAG4qu95b3SfQVUzJ22mhJRVLLtaaawK5zH33xRXAUVQLQl3NcfAkVFUIGgNUpHEwImBef1PIF3ktEm9OXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/23700" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23699">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlLtgN1mWu1E17iFKdT3Hp60T_g7g1FPwPRRA7jDivHkowAMr2SJBAFiSpuWNsFcq8lG0dYbuP_Bn_L8NOvsAdRbvHlKIJS680JsenpOcKlAXBFVhu3o2i0m9VHGPEwSzIfKZa5vzXGYxpGc-uSeoonB0bWT6YSyhLwQyQn7__HIOSS0z9rFYA6GYBZBV92HOx2pBAh2Tzj2aTHDwUA_Xsxs-OANlCFlUEb0wgdsG2iSKuNCsul2IGmNhX0x8x8csPJWyr1kFSzst9BzMisWcN0YC8GBzyKwfIg85OfLWOKIY0kAxpQZeM2SwiLQeYojDJmuvqeMtWALp99xFF1-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/23699" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gc7_O53pU1HNlwKDlmhdLQYZhQkQl6mBiuq8GYIwUGi1uyD0MIGykEhIMlKgVdtASrN8gS9z2-M_wjU0Evq31Cgq6r6w1Igj3FjpocmkK_IZFJS3dE-cqM7FplCWkkCaNlHor-DSoNdv6tC7ZDuyZ5iwvlE2gYwOjsqtfHRqielvUU3dUTf55Jkpe1hiWJOyr6Ebtu5adp3uHChEJj_qt5epbxIQteo-7VQ3h0qIwKcfXS2ZPtebGJbjy_uO0gGtkqMNeXFm-juzvl-_RfT6kcQewZPA5K9TG1CT4v-FLITRARxrktEHAswKZoiBmSLbAGOV4AbRiw-EdZO6mW9D5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiRga2NFLR3n3s4jwgASyUUrXYMDNtb5pD8NYcH7TVFINmPiqbVOQcSZNAgWjF1L888HYnN7_nNvkrCSuaZ0PRUMisUxUH3dcPUXYsj3RCHa2ezPzXHKLr526T2zjVx3M296S2dAg777KC056ygBHP0ccDY6DSeAEjf8aXFYu1Um85y-nO7LpXa_PX1uG7ooll_LhXQoLzYB28Y6FsAMbQ24-YpTcQeZOwqkyN90uRLnKef25jSXR6AG-lVStSB43hWwcRTICWNGGhh7GIFuZBMCBMaeVHHwUdYLzY_Xjsj6tz3EmbVBW9AgAPDKVpASp9UXSIAsOJSIDhSqgyuH5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/23697" target="_blank">📅 19:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7cgx146aSqW5CGX8K2yFfIh7ljXVX5WVd72hwAB_Z_hGVCZVMc4zdR7qdcbS5VkPTeFpODVgZKYtmKPfscpMM1gmQLUOmNtPOIbaKV_o9p0ixFtNHu-nLhy8UI8-LgxWZvk1wqcMkxlw7-1YUZowWLQztjYNa_nAb3c9JKHcnMDeJHMfZP7wJ-UYy4x2xtx0ii7Us46UMvpBmV7PSAd_ascPogzNQFpMb2PCEXNzw8K4cKk83D3k867w3AMmg4ITqlCOuPX-orRc_FKyWjrthSTxRSBD_txP3-FJcRhCV8wJfnn7Ss3XKuHVc85XHU7VB3PPiBaZziDIZw0_YHFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو سرمربی رئال مادرید از فلورنتینو پرز خواسته از بین ماتئوس فرناندز و انزو فرناندز دوستاره‌پرتغال و آرژانتین یکی‌رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/23696" target="_blank">📅 18:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kikyCmlcmApVOiizq0S9jn8kOS6Zo9mo4YKQcLIr-Qf0aPkkwnAhycMYl7-5Zt8_p4em-fRFhfWGJnhihKKT-Jrc0R8qGoFwbtMyeSoqu5kcvNnXMFNgLf3BDo_PZGGZacEh5qcEuKQUMzQZyYtV29BMHljgaJySMyDwD4ZtI2Bed4MhCY0clHNyZ6roJ3FNzs3oOMUs9dMYmTOfnwmFVa2FNDS45IG1bqij6wJ0MSYehL5028jl1prRhzo7SDKJMjcB5y8cK1rZiMS8SvU2cGPifr2OGtkOY5O0nryHvYxLuSyI8rNICCgdD_36uslmX2Dj_pgrbjUWTSoPi3oUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/23695" target="_blank">📅 18:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJBvwqKKs3ydMKaGxeP92e3jKcSia59xXiHQ9XGTWgcZEwCaln2wnrIWyxOcsBzOxRm9g_A5ZbqSaAw5XqXU0wOa6roddvFYiDfGW_GmSvi1RIaQw58yOSowNVBdFBq-40vmllO5_0DhcL_NdshyGJFN-TF5g93aTPd57ZveLGIxJmdkqWpDZHvgO6IBgkro5-bG52pvxcqrrmmQVojF1sKsJx_N77LXU_pEN0hQd6RGyc2DvyHqtBXLDq0jC3WwVuudqbMbFJrqDF-x7i9dfKom8g4qP-jN8oit60cMirdnenj1ZBHH8KZen9Hlm_J2L2Xl_LknfPUSm1P-JJ9WlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام ژابی الونسو؛ دنی سبایوس در رئال موندنی‌شد و او این‌پنجره‌کهکشانی‌هارو ترک نخواهد کرد. همچنین رودریگو پس‌از کش‌وقوس‌های فراوان به این نتیجه رسید که در باشگاه رئال مادرید بموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/23694" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7iYPKChN3ufJxcnseHY6vwkg-LGHyhGJX1XF0yMZcfckHvonpyG27MoSJRmOi-OTkHs4ehqCPkHnDVtdZRczXN16DSfax7-yS--hKYyH7Ir8J5mpu3RTXbPS10I-hIuVNSdJDtR5dCMvyGn74-kKensE1oYjtkvrisZqmCjUq_6CrBIu3fyJN1THRmpdhfRrALYmMq0qsbacuozc2fOIAOUwEZsyathKdCmpNPJoN3ItF3IzrdRBwzy3PpZSbjhktT_R2GmbLmQPeL8Gmlu0YTNIqZoJXgTKJhL5sNepbId4fkan5uPE_X2lE5bzCjjM5N7k8YvNxA8zOOEd_u8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام باشگاه خیبر خرم آباد؛ سید مهدی رحمتی سرمربی موفق‌فصل‌گذشته این‌باشگاه رسما از جمع لر تباران خرم آباد جدا شد. به احتمال فراوان فراز کمالوند سرمربی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/23693" target="_blank">📅 18:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=J60lzj3R4kAH9rBXIEjtCP5A0IeyuOF17ynsbEgSou4yutukDh6tvtzrMQU-oRjL4GgKltuNGd32oZNp2pFt1iDdlqj6MLm1gpRmx5NLpuNbjT57KKJDc_E0AZW40Mo5dSJQ26fNgxQMP_XuvBxM_S_VMgWmMLslb9UwSP628hbIl0M8z56AK-2jwXjNLTffvBbhc6MJ15CgPflWbsbwE6MzkDS86JUgsbEU4yvRpn_q2Fv4Gd5va_0_4ewWGXxF44NQ8-bEPi3AUPEYu8E2VL3TgOf_zbyVxr3hkVZ5afpInG8IPHwcOv4_LuXiOYZBbD_NUEC-l_D7lPm6WiBzGrQuaBaRMyGviSVG7Sek-ZtvYx4AUi78KKGKfV3cTWyk-oYjFHHanJg5k6MY9kIT31pIplHI-HinkZBi3ng66RzK8IuLrOQ6W8bZ1i0oUlk4n0lmEbxpT6u7wCEoOD1TG4qb45kdcEnke-VE_XZYDVDyh7-cnaDxCKTcFqENgd51mgBxdmaYr-d1qeCb2qNjszxqHUBl3Rd1FVMIJIExh4WLtuIaIwxsacegZfsA3pdoCtPLOqLR80x6W_aFKjSfH-sdSHmoNC_a0mFy4r0g0XQljPIa1-x1RZtLaKUTqRDkGnMtZ1X85Gsydw6yOBWG2mJ9cIVs2kCxDGBhORCk4ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=J60lzj3R4kAH9rBXIEjtCP5A0IeyuOF17ynsbEgSou4yutukDh6tvtzrMQU-oRjL4GgKltuNGd32oZNp2pFt1iDdlqj6MLm1gpRmx5NLpuNbjT57KKJDc_E0AZW40Mo5dSJQ26fNgxQMP_XuvBxM_S_VMgWmMLslb9UwSP628hbIl0M8z56AK-2jwXjNLTffvBbhc6MJ15CgPflWbsbwE6MzkDS86JUgsbEU4yvRpn_q2Fv4Gd5va_0_4ewWGXxF44NQ8-bEPi3AUPEYu8E2VL3TgOf_zbyVxr3hkVZ5afpInG8IPHwcOv4_LuXiOYZBbD_NUEC-l_D7lPm6WiBzGrQuaBaRMyGviSVG7Sek-ZtvYx4AUi78KKGKfV3cTWyk-oYjFHHanJg5k6MY9kIT31pIplHI-HinkZBi3ng66RzK8IuLrOQ6W8bZ1i0oUlk4n0lmEbxpT6u7wCEoOD1TG4qb45kdcEnke-VE_XZYDVDyh7-cnaDxCKTcFqENgd51mgBxdmaYr-d1qeCb2qNjszxqHUBl3Rd1FVMIJIExh4WLtuIaIwxsacegZfsA3pdoCtPLOqLR80x6W_aFKjSfH-sdSHmoNC_a0mFy4r0g0XQljPIa1-x1RZtLaKUTqRDkGnMtZ1X85Gsydw6yOBWG2mJ9cIVs2kCxDGBhORCk4ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌سنگین‌پیروزقربانی به کادر فنی ایران:
من‌ نیوزیلند رو راحت با فجر سپاسی می‌بردم. نیوزیلند اگه درلیگ 16 تیمی ما بود جزو چهارتای آخر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23692" target="_blank">📅 17:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjN_z5YN1FY3-VyF_OVkDy_NkPNfZcbVZjHSDBHAl8MZT-P9UW-zxtrJiajwX61Xxm97Wc12ta9igdztG4kQ9kMLcGx_LZE1eISe_cwkLUQC3rDPZiKYhYPWnSW1H1yk2xZoQmYe4oHuWzvjSLcrAxvXFIk6ISuiWIVB_EAaUFMNn0Un-ZAJawbLScajB96me50_VQUX_PjwtfK5TrvdmJkckEiT_S6TQaY24KKbQAJe_zLSXZ2D5DP0JUJswHK7lZF5netNQhde0Ef5seANZFrW5xGqqaYcIjIgIlCU7BDVD_HX_lZ2zGpy0WOJmD5hfVKk15RG2qKAQtwXisZssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQVZlcehdgcioJDEa0vv6jf5kBOomTJpKnPxdBWQBkhckvhKAR7Jkoahmk4Bp1R-5MaKLAE4O-psiGuslHMCJCqQqZwX77is1bPs6ezszi69aW6Kvm0JjHLmjG9w32CM8DfuwsrOHm8E-dyEW-QIcH7Bwa-v2NUvZxnV6JITtpAV7JBHlPOYmG9hZflIFrWefMePRZEYWZUClw3rHjRVHt4ySOpCrnkE8XZ4XIOaxd3TW0O_IOTdcMhWGp1Yt_74vtILytrBn6idjQq-YBbU9lg0ssyGBImVLVeuHK0oLJ_kVlzqaCv-yLN6PlK_plhAzn9f8ZrEHEUaKQw8tedj1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23690" target="_blank">📅 17:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkDVtjo9C8-Nfvo1XyNaa-lLqUMBHoO1v7Df_dTDPjKZJtJtugwmDd5gDsL9p79vt6XsqrK9LhXFm4A84kvpUm9e1e1etO_JzuTpQ-ILmNHDgpq8KlLm0ALlB3Yn3RHThV1HQn4dX7vSXF-9dplIznpSsBQZRn4FZnzY6OdFxUgHpXKigU_HEu8lg7CMSwzTgl2Yd1h5BuU5LmrhuwhKvs0aVHUKZ0byGao9MNCReHIAa8JtuwpBNoT6UN28RrxgdAtE8VinIB5EfOaJ71AI5ocm1JoQ1a4kUqxzhTXFYLNnhR05XiTb7l0xYGJ8wLmH-kPCoR9emPOF2WSNmelzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23687" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012fc50185.mp4?token=Lu8DGiAi_n-dGXBcM8Vhz3rlhTCZKudJEX9HRCX5RHP1lH7OVGj1eSetcMF1a1J7QpyoxVkhol0FoMfmv6CSU8ljpMhT67N9xCawAfzhEp-7KyZ8jDDF3wgujPRbt4LFVK1R4BUEjUufLf0Dc3YEkGOX6CUbd6XKyW8bm6Y6ziGAi3UzOrZ6HG4l5AkyjvqQznlLL6dr1zNezxPtAgiVZBIxRYQvI1ooicqpwRM29FxkO1tBoR1-PDpCS69rMIvJmUjopq_iDmOx8Iq2a046CIMODK889IVgicVp5lvhhrHdcRd9yIyvJhiNL67l8_OsBbrVRcTXFPhiBV68QJ6heQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012fc50185.mp4?token=Lu8DGiAi_n-dGXBcM8Vhz3rlhTCZKudJEX9HRCX5RHP1lH7OVGj1eSetcMF1a1J7QpyoxVkhol0FoMfmv6CSU8ljpMhT67N9xCawAfzhEp-7KyZ8jDDF3wgujPRbt4LFVK1R4BUEjUufLf0Dc3YEkGOX6CUbd6XKyW8bm6Y6ziGAi3UzOrZ6HG4l5AkyjvqQznlLL6dr1zNezxPtAgiVZBIxRYQvI1ooicqpwRM29FxkO1tBoR1-PDpCS69rMIvJmUjopq_iDmOx8Iq2a046CIMODK889IVgicVp5lvhhrHdcRd9yIyvJhiNL67l8_OsBbrVRcTXFPhiBV68QJ6heQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خداداد عزیزی سرپرست‌جدید تیم پرسپولیس:
من اینجا روزی چندین‌بار از حرف های جواد خیابانی هنگ میکنم. بعضا وقتا اصلا نمیفهمم چی میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23686" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHb5t-6VV4WcGaCLuUx5GO_N977Q3fjlIgkg3gK2PNYlTaiEfVdMnF4wNuPk0A_GJc6y_EVxL4Xn7_fyckAYyju5ayoQApr5om8nB1Oj5F_SHdXvFh-LigGla2XWBybo9SUTSWvAylKEPtozjVnRrFcwJ62rwyOSTCjZj4XZAxqvzcSKgAeLpK6HhWL2vrqJmqCMoP41_mZQcyHjjQxUuLL1E_3SATJ_U6RHxEDPPsTnSQWBowUcxWeFicvjxGzag9XsfabDbEJCkXx4pDVnkVNpScBV0QRwi4Rzc9V5ymspdpaP0rmqruic4ryApJfETw7ztb2B9Xz79uznt-yUnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23685" target="_blank">📅 16:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=rhCf8RtOT6XzGvxpE2i4fGaOahgxwYCTh0EdM9Yh_JbloCSwJwczDIDHjt33Gijj6KqLZblOsOvVwghU8WB6lc_RTjX7sPw5crbpTc6e6ni8pT89wIQSMz8vHl1WwgzVUHzFrz8WIEIvBw_YGxlL13YUiahux7drKfzUsP2EiymqjYU8gdoBjZOZ7B8fR66gmkCao1s3ugjYfUHa0GuMQF888hBnJd7jVHVklOa3bzjh3Gi6NVfeIjaCHef0I7MbaZPBv-8uWEvJ7N2aB1XyMp7dMZ_BkrtuUGqz5U8xhbg4cVAYr321BXVG2dAVXX_7B9-Ef9eAFCl2_FgJlFKWvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=rhCf8RtOT6XzGvxpE2i4fGaOahgxwYCTh0EdM9Yh_JbloCSwJwczDIDHjt33Gijj6KqLZblOsOvVwghU8WB6lc_RTjX7sPw5crbpTc6e6ni8pT89wIQSMz8vHl1WwgzVUHzFrz8WIEIvBw_YGxlL13YUiahux7drKfzUsP2EiymqjYU8gdoBjZOZ7B8fR66gmkCao1s3ugjYfUHa0GuMQF888hBnJd7jVHVklOa3bzjh3Gi6NVfeIjaCHef0I7MbaZPBv-8uWEvJ7N2aB1XyMp7dMZ_BkrtuUGqz5U8xhbg4cVAYr321BXVG2dAVXX_7B9-Ef9eAFCl2_FgJlFKWvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇶
#تکمیلی؛ آیمن حسین مهاجم تیم ملی عراق پس از ورود به‌آمریکا توسط‌پلیس دستگیر شد و بعدِ حدود هشت ساعت بازجویی آزاد شد. اتهاماتی مانند همکاری با حشدالشعبی باعث دستگیری او شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/23684" target="_blank">📅 16:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34750719a.mp4?token=fGewFTEih3xe2lm83X5wfQgR6tND1YiJ78eiqK0brADKp_RNcE-tcBlNhbAouClol0lCt3Bwwldm9BnLr87_61Vvc3H4N2cqtuu3ysbAGIqPQtsj4qYEJYqpTN8t1OmcoR8mdFbJAeWSWHzTNN9_WAd19p1zWYx9tZo0DFQoGNZPikdT8Oulon2rN3OUzB5dp-PNQMzFRKze35YtcbNjmT6IeU1pp6ujboyqvwHylwkO4yj6P9X-eehXFB9pjPkoKBGs1rNx9UDJcdGnXWXUkr3ZLsFuQwT-VHNdyBPftpzGl7Mf_6wCQKv7qKufnmZjLk0-IMIeHRXDXZEz7YudEYCzagf-Vdx5L9FJ2N6PuEISEWgHD1bgdgphDZa2Ej-gngZPpnw6-TiE651T6mfJHZWa09VWNhgu4Kgg6IgBF3tT0-l9j-mc7KwSzdkqSLHWrsz1ZljOpMCtk4SwZey9EpuKrkOe_Dv3FJcwQiXeBtQeZ98zcJWICwPWP83PdX1qm6NDGvfxHH_dvaOmEtdVp9-_kJQb3gxi5w3f6aBzrb8vjL3BrdKuSCz_omj0Bi3f_wdphzwYyG5i3xP4H3Xy4UJxt3aeVisFz_eCGood0VA9H24neq9nnAufkEURzXW2Wx8iNreX5Ax49tX9dlsh0Gr4-33GRN1uDQH_yj2Djjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34750719a.mp4?token=fGewFTEih3xe2lm83X5wfQgR6tND1YiJ78eiqK0brADKp_RNcE-tcBlNhbAouClol0lCt3Bwwldm9BnLr87_61Vvc3H4N2cqtuu3ysbAGIqPQtsj4qYEJYqpTN8t1OmcoR8mdFbJAeWSWHzTNN9_WAd19p1zWYx9tZo0DFQoGNZPikdT8Oulon2rN3OUzB5dp-PNQMzFRKze35YtcbNjmT6IeU1pp6ujboyqvwHylwkO4yj6P9X-eehXFB9pjPkoKBGs1rNx9UDJcdGnXWXUkr3ZLsFuQwT-VHNdyBPftpzGl7Mf_6wCQKv7qKufnmZjLk0-IMIeHRXDXZEz7YudEYCzagf-Vdx5L9FJ2N6PuEISEWgHD1bgdgphDZa2Ej-gngZPpnw6-TiE651T6mfJHZWa09VWNhgu4Kgg6IgBF3tT0-l9j-mc7KwSzdkqSLHWrsz1ZljOpMCtk4SwZey9EpuKrkOe_Dv3FJcwQiXeBtQeZ98zcJWICwPWP83PdX1qm6NDGvfxHH_dvaOmEtdVp9-_kJQb3gxi5w3f6aBzrb8vjL3BrdKuSCz_omj0Bi3f_wdphzwYyG5i3xP4H3Xy4UJxt3aeVisFz_eCGood0VA9H24neq9nnAufkEURzXW2Wx8iNreX5Ax49tX9dlsh0Gr4-33GRN1uDQH_yj2Djjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:
که اول نظرش رو تغییرنداد و پنالتی‌نگرفت. دوم اینکه آوانتاژ داد و باعث شد کیلیان امباپه اون سوپرگل دیدنی رو بزنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23683" target="_blank">📅 15:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=vQvSn5b758J3-H5O077WT1Cz4gEZovSeqSIKIKr5w8UQrvRJAiXZUmQVgmA3twVxiMNB90C2wk0U8xZ-5fYBptSdNarmVhs1mvKsWlGiE2DULz4-SF1aUjWe01ykH5Vg-U0Yp9x2HQ9BhB2EzlJ9ANUmBfaGIAlNL-ygr6H69ObRm8yn3mNwIVP7S141_zIQRNgUTSiQU0D_WU61MKmeCl3vkpNAZSd7VZ7_M3st8PXdh7IVx3ul1KIDhd9raztS96iZOBEQN4xHEewLt7dh9jb5cmbYBSFfMFp9vWCAmPMzYs_sn1EsdhSUsRlZUjc_Px-J3ycJfpj1nCGojox9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=vQvSn5b758J3-H5O077WT1Cz4gEZovSeqSIKIKr5w8UQrvRJAiXZUmQVgmA3twVxiMNB90C2wk0U8xZ-5fYBptSdNarmVhs1mvKsWlGiE2DULz4-SF1aUjWe01ykH5Vg-U0Yp9x2HQ9BhB2EzlJ9ANUmBfaGIAlNL-ygr6H69ObRm8yn3mNwIVP7S141_zIQRNgUTSiQU0D_WU61MKmeCl3vkpNAZSd7VZ7_M3st8PXdh7IVx3ul1KIDhd9raztS96iZOBEQN4xHEewLt7dh9jb5cmbYBSFfMFp9vWCAmPMzYs_sn1EsdhSUsRlZUjc_Px-J3ycJfpj1nCGojox9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
#فکت
؛ تعدادگل‌‌های دو شخص حاضر در این تصویر درتاریخ رقابت‌های جام جهانی رسما برابر شد و حتی ممکنه سمت‌چپیه از سمت راستیه جلو بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/23682" target="_blank">📅 15:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx-yHtzyU0118UlELMNjPu4BdHndZULQWcwSwLfq_LKfWlfJ33HTozyG_DHFzvOT4LhkuYj8RRTef0zdHJg8FoPCTFqSF1xwxjOBa5i8CW_SWQt_5wzN812vKh70TfQZV0Elzv3qd9Fjc63UgS5ZdqEUzJcSojAa4MNiUJNh34BEA65B5CPhr1nu8atMuwYgwYr9lA9PGud0xD6v1u8vWX7bG2FbOUY05kEVy1ZBN0LBWzGH-3UDW8Vhu-0_zDrsdUr70X_vgDkm-M1KhFBjknF4XgSJvJ53CCIlM0b08Gl21g6ppp-iiom3Y-qQ19CK4K6jZMuu0df9BCAmhC5WCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام 120 گل لئو مسی باپیراهن‌آرزانتین در بازی‌ های ملی مقابل تیم‌های ملی چه کشورهایی بوده؟
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23681" target="_blank">📅 15:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqv1izsHNzgvRbTSWR_sTuHYsMnQYNfJEFMRr6fYPUS_r-FfPD3sVOdaBCor1ItShdxF2M18D16zvYggKcdSZ7vDCZE4sl9cEV_U6Gb6xpBs8wyhqWG7uZzYPzB9WgtkqQ0NFYXTToKFPXqy_6TRqvnq7_I2K8Md5gO2XXVARdXBvvI91XVkOcnVh6syvTJRV6WVU1PS_arNdu4hiDEJ5dd3vavfA8T51SpVfykgNA5sP7_Ih0umpXx40BTL8Kv4nGhGMvjVT712vD7dQhk4ejdqWHIuURBlLMI8fVm2Abmk--GQb7x5PUeQ-FnIsZ8baopVPhv1cDuoawj6ItZsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل پین قرارداد یک‌سالش با سپاهان به پایان رسید و رسما مربی آزاد شد. مدیریت استقلال او رو به سهراب‌بختیاری‌زاده‌پیشنهاد داده‌اند تا درصورتیکه سرمربی آبی‌هاپاسخ مثبت بدهد با او قرارداد ببندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23680" target="_blank">📅 15:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmD4Ob2h-J4nBlCa3OtSXUG3pQOi9NCsGzlr24S-XwVxrhTiGStJp_TxZNaxFbAPI8vBG5RvHXeR1fxSTrbzZ12Qw6xxQ8pKguZPsrlOpsMT1M2gVKXtTOc5aHVtV4-Rn0JEmXjtCXN2Gs_Xsdr3lW_XTbezc4grC4JDXwtWcJVONO6LqlJb2N2blJBE1hWNh8phFQvWvVyenG6HgM9ZI-CPCDWEPOW5whyhOXeV8Y_kMOZvwkPLzWUaF0FaoyToagB3XjExxOxsQwRIMhhuto_lVN04PB5qn4BJTifwJ5z6K5PnE14JiRArT1scafTeT3c3E1UlCHRMaiGDWpkuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23679" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23678">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-JpyHRxjBd_unikAcuWk3STnXH5Ut8OOEC9eL6KedhPXpjN_94ucji67yQqiccS1g3F1BPRrNgrnhnZLCOUw62kYczFrUyvGhydzbE4Vk5HaPlvhpH1jNjbkxEuglzktxB6kPb2R4PNyK0PSiW444sUPeqnm6sAxTduYQwtjT2_gEIQRmkUD8Se1vuY_sfmx_MG2bZbm2J_g-qirpFAWw28gaMa65__3oLdC52cBnJ5gxJC1YTW3yaZo7kSdZHBKrBnoMINpNr2wDJJ-ps86NhxJxLeZZGuwophRjAe1cNR5RqkrdGVi00VfTMB7Ghcdcm_YRjHEa1eSIZIKw9RQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23678" target="_blank">📅 14:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23677">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwzyWl2QCGMGEf-db_Fd_JDSoYdMQW25hBFmCsExsCYJFGKGicleKnqMi9nTQwGdAPwWNdh1gCkppMcbbzTguqRMsldtEqJb91-6nRwDBFMFXNg1e_-oLjpvLPuofLnfgpIQ-ANWFys5R8QEphhG71BtWzBdEa0hO1ugj5AWJbVBDvE4ik6ADZyxGwY-lSuJGigEIS-EX7h9-1hrxowUnKmDqYw0HNa00Yp3Mf1DwC6EMHKX1OhFgDIR5kNJLJY0rseKpJAELSj2KjxGEZcOaZJ1RZcczQxO4BYtaxszwZ3aAqW9kWCrRMJftznL620tkCJrkomPX9yjtDAJvoxwMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23677" target="_blank">📅 14:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23676">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK6am3OX09ylRbqnt_7V3mE146s_nhUC7fvu00IsCS0G5l52KUTKEJsw5XOPzC6b_eq_jW5eqm33Mp8upp9mpxFs84jrt7LI1F0-U8Vhb02omTZJgQ_qx228Sm16Gt2fdUGANW8hpH4eENn5d3AHj0psLqPX3CgplNrXt6g_SANMt4-1Ed7fvmm54N0RumgLxxIlKflKxhe-VpoV6jiEw0pVuz9efBrpJPxnqHZnIACPNLTSLnpgxM7NHcb-4-TnuHZTwDpCPM3tGVptTx6xPM_W5fx-LTG4AhK_65oJt5ygw9qmdiCguy2EZ544Dq7gmo8uYURJ0bCF5iYo4H3NIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23676" target="_blank">📅 13:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=gFBijo2WN7EoIAgF5iEVYXoCSwmsACVft0EX3eBaHQUVN4xMUPnjAbWSodY3KnrIaGIlPY9LojpC6vW4a1SNBhqVnzX8Sjx48_izeFbYx1buNPTVkeEeG13tco7tyM_hB81NzbyNgabd_NlOtJMHZMR60aPuRCOmENOR6T6WRnxPk-tFYzI6Z-T9UqHRmDq0VBhqxkJ2A_4E48qAy-3LkM6ofn_ZcLx7xfiZ6LimX74hNV46Xo1nDj6ym_uHRgpYZsz4jh11x7az25FeH__6i3s9XJl0aHGBN7xGG5nsNkynDswZ3jlhe0OPGudmNmsjR9gMMaIeWFd-PlAPfcKyuy5R11GhdJn7vrv9RusipE4NgQ-6OUs2MH9hgXkWhC4TV9f2jZOoBGmNmNxc4mQqrtDtnzgIRu04y487rRpKzp0zUh1BbdLftn6d09XeCOey5-ohlMu1iS4KeVjFBb8bYK6N2_u6CNi5LnRJ05NXwHA4tdEFfqj5QawsCpHvNUtfSecg_58I0negoGB8U8MIPv29nc2CyRZHJXrKxDjUif9-rLuGYztQI2CiCj-uVxQcJ_cOLNKBMT6wo4q36_Z5bQ8gWuJOloomCvvnSf_lwnZfbSABV6wL124BVFJ8oEBxm3XeREoTX8uey9EE4tLs-1P6pAEbj72aaFaS2M3hd2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=gFBijo2WN7EoIAgF5iEVYXoCSwmsACVft0EX3eBaHQUVN4xMUPnjAbWSodY3KnrIaGIlPY9LojpC6vW4a1SNBhqVnzX8Sjx48_izeFbYx1buNPTVkeEeG13tco7tyM_hB81NzbyNgabd_NlOtJMHZMR60aPuRCOmENOR6T6WRnxPk-tFYzI6Z-T9UqHRmDq0VBhqxkJ2A_4E48qAy-3LkM6ofn_ZcLx7xfiZ6LimX74hNV46Xo1nDj6ym_uHRgpYZsz4jh11x7az25FeH__6i3s9XJl0aHGBN7xGG5nsNkynDswZ3jlhe0OPGudmNmsjR9gMMaIeWFd-PlAPfcKyuy5R11GhdJn7vrv9RusipE4NgQ-6OUs2MH9hgXkWhC4TV9f2jZOoBGmNmNxc4mQqrtDtnzgIRu04y487rRpKzp0zUh1BbdLftn6d09XeCOey5-ohlMu1iS4KeVjFBb8bYK6N2_u6CNi5LnRJ05NXwHA4tdEFfqj5QawsCpHvNUtfSecg_58I0negoGB8U8MIPv29nc2CyRZHJXrKxDjUif9-rLuGYztQI2CiCj-uVxQcJ_cOLNKBMT6wo4q36_Z5bQ8gWuJOloomCvvnSf_lwnZfbSABV6wL124BVFJ8oEBxm3XeREoTX8uey9EE4tLs-1P6pAEbj72aaFaS2M3hd2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
عملکرد فوق‌العاده و سیو‌های محمد العویس گلر تیم ملی عربستان در بازی مقابل تیم ملی اروگوئه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23675" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYKlNfqUUuxKv9xuFaB8vI3efXx9RI4BwJnn7F-P1_2JG3E8qqWeZi0MBFyBkseNxub1qZv-OYnW_lla5jz6qmrM8jFVWx6hj3wPqorvwPCU7Dpc9tCvRTTiBVqbnCrNSSzDTTMVyMyp5N3bQVy02fOF0PGh8xnGsiJySUYrJ2CMTmQbAXTB7mcoTTzWbmfVbe1mPmjH1x7lq_MVXk7-ebN7npFvwmCHYFhyGeyCBoNeWwg91NMMik8rtYYozQmU3TExU6CMZiUD1pKRJG1XjPmZlZOPVw9TxpemPvT4wzf1zEQKXdIcp5YfMccAoIW3ABA-5_2KSkajjVGgw-xqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23674" target="_blank">📅 13:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek1G7hWM2G2fdRcKypnou5GfIbs3tw8aUgitxSFXPbrg1rMonU1rDgP2fNXlMCPcQFCTf__0WEIHzyXTh9YajL2ppS0_WKS96y1-WMFThzKfJYv_HLJTYz_wC4e0t0CviwRP-nnMlOcjWd3mieKbFSm_x4TS3dtXJG6I9L4L8r0oXKGdHjlNqR5somgxxYTWNlVDKYw3fEiDuQFzqJi0iRCRg6xkfj_hb6Uk1i2Zzt2JSTvtREOz1Hnttwt8cazbbrczrazwTn8ijFfIrNWt7F1SNb9IKLsfnGYhtURcrx6FWY8wnXe9g2lwBzziGV28tXp7DCgHL8sTGhBZq_CPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
خوزه‌فلیکس‌دیاز:فلورنتینو پرز میدونه برای جذب مایکل اولیسه بایدرقمی بیشتر از 150 میلیون یورو به بایرن مونیخ بدهد تا راضی به فروش این بازیکن شوند و قصد داره همین کار رو نیز بکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23673" target="_blank">📅 12:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF1HQLepWZ6Ph-xJmNNJBCOGzbOWvcrfSHnqAmjGWyINUTktu11BJVlMdex9PDW6fKCkQ5IxLXxGtDJWnlV8JpNxg6wNqDfm0P6MXojtBspSNK3Dxw7iJXrmI65LGAOL6ePjksfehabMsE9FzKnbbh3TtK-WmdmwsBv4FLakjmx1SSXjlUsyf5K50Vvyrl5ExQXKP51XbvgFcri5zzTSd9xBfPeKb6bjneFp7JzYZ-8GaqOOLwjVlX7ZCOlG2aiLQwT2w3ptanIxtTK5JlVniUJQrS1I-Yzyvt7vc2Zz5CF6x1TxHfFarkqy3ZuaeTGv8zPpaqZrL6dg_ekLi7lGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده و باشگاه بزودی پوسترجذبش رومنتشر میکنه. قرارداد ستاره پرتغال با رئال مادرید 2+1 ساله به ثبت رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23672" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23671">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7YxBHB04A1WrMsS6j9swXE82mWl8WoxG4pRc-FtF8bIKt2sO7KQkzqVacN7lPawtsFog7_V2gluRkLpd1fEAkRxSmaCJNVs1rC4LVt7MZ54VSFT7qqVQC5gIPsfXVep37i5nXUWpbrxVqQnFSl3_UxnE6vAR8u3HBPFS1-qfTneHzKEJcsCfL5J4zRwHSQTGCdAY3Je75a_nLBdXUe0PxgBYORy8_9wVpi31mMAajR35TxqWDUKQ7doHrWZnsNDJbBO31HkKHm4l_vDvw3Y5JZozUNIfEczP7k7M3ERYac4u3mxu7UhH8qfgv9d7VN_5PJ0ZZnj92vUwPxHc6h4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌ پیگیری‌‌ های‌ پرشیانا؛ پرسپولیس پیگیر برگردوندن یکی از ستاره های سابق خود شده. امشب اخبار جذابی رو در کانال خواهیم گفت. ساعت 23
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23671" target="_blank">📅 12:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23670">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGScfyUpwmbkfG9LGdrX8jGTvFAicdIveCABOBT4yvAYE7HRLoj3QRqcNDMfM2SyrnpfgoloHqKq8VM8FzPgChKSmUTlG6LSdXNcYGA8YoWYbvOh3ypHp122TavMRbY6tO0sbhLyc4PbcKkSmweDZjaSRBSsVR8fXwU_tpvSza9OrJFvDJWrzgckKyuVJcSe4L8twGElseNqNeMadvtr6BYzTPe2WpetdvrhFuTQEsEt1lCNN3VsgfXnBDxA4LGSRwLSo2BL2My_FzOiDa6Hy3fY7rkeO0OqpbePhvkNWjbh0X2NbcBsJsOlGNNV3QjOyrzMEuPXijnzNe_HlzHx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23670" target="_blank">📅 12:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23669">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgUKKC9-pZ4v1iuATwllLPq9HTARp7uA_qce8VXVLOFhAdUIA9cPxzrZN_tufstnfMbU3luw8AXWV6vKMR6pdeWos1HxZXKLwt3dbjIzwnMEza1hns7sXLXA8jM7HHQxE9xtJHujjt5vGTT-s1S8Q48IXbPdGGkRKbmtNXFGruaNv8FQVUvwS1wOP2c9vluGNtIMemS7ngrNLunUL1wnee4mdGGUZHyMlWP2f7Hch1568sd1eBV2ypZOHjet0lWtceiM_iksO63Q_RQ1dCZqxs4XBbk1LQr2-8yuAxIXQiZ6SIfsiyaUwh8h3tpiz4PRFHon-D8q4njYMn9eIcTyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد محبی و مهدی طارمی در پایان بازی صبح مقابل نیوزلندپیراهنشون‌رو به هوادارایی دادن که باپرچم شیر و خورشید در استادیوم بودند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23669" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23668">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB2k025FaqBemiVR4pOQ94j3uWRpxY7Q2DJ6yKmQsb5bJ1f7gzRz-63qVEbTySuB2clSoJCU-SJp2SGdr4-29JjgA9it-4pZDOZTU7be0qOyIuS_1CcKRXksxZtxvmx7MaORT0hTZOh-hEZO-8SDnYgW3pS_YR9UWvWHwjRN00rfWYfUdie8Nio2nOCQqVuA2HEcHzhV8VWU9ldW5--kPyv23Xj1TaGruZ4BKlsdQ7eNYI_hdWfNyjkaLt6KG1LqfRvnIn1jFVNlFFEa9XgEOdVGF_ZHnHgnLP1Vb7lo-SIODFYSwRJXXKmlHdoFbm0Kl2M_W6mFCPrCwz2qMGiINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23668" target="_blank">📅 11:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23667">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chW8tq7PKKs94h2Q31PU2csLksSoi6ApgeuKRN0zOE6xgfpA8LawnDau54FX95YIeuR04iN9tyLqLwMJ21nh6ksktcL0RtYMRhVmtxTPBKftR1uZMcPDQxgijTKOBmaw55ZjupcVp1pbr9GZoLS9L6MUdWxXT1YugaED377JujBiGh8246WnrGvoA6yavR4inUyqRqYCOn1vngQsc01if6Gb1gvrrWrgEEHThW4iWoqmolnzC558psealyVwbjjpUu7JCr930vdWZOC5puizCYUJ-nee9l7FNabrET2jHb9T3G1l2MNJ20xVvWNc3_UcrzMvTPLTNqJbk-mCPfKXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23667" target="_blank">📅 11:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23666">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3G6feuvvkRkd-HVEeAPjAR3ae2zNVn5nkkbQLjE9_prdRrztKMalipi2WNYVveY5UxNx4TYFeQ6N3lmtukYO5kUUiNz_3ZXy28JBF39x-svZPYrX5ZhKODQQqR74TkWgY4FTW_47fSeV8VgxKK62v60T0aFKcjJ6htfMvDBHMyGB2ag-74Va6M-tH2WnqYxIErNByrHS4ltk7Pk4_3jjM1BPsBNIWsBoBki3ze1AA4da6dp0Vnj6g_s2MOByL53zg4JQQede3VLgIAHp4S3Nd4VzYtBoKrQHyfjTAMVjsYp1CSap-iMcwX4RVVG-xRYt7zdMuRznQ_NKz2wv_5A6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری‌عاشقانه از زوجای‌ایرانی در حاشیه دیدار ایران
🆚
نیوزیلند در جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23666" target="_blank">📅 11:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23665">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXmNtX8FQJC_j1ETUcREr6yhH5P0fkq13xQyY9UWz-3AbZmGdx7qv2DvETluidSVUAc8YTJzFqRQI5AWROVtEezno0SnPeQ52sX2Ernl24j3wtOkMPAK6EgqUvZAsg_fV1kbfCMffLfz1ATm5xhD62PZkQs-q1h94XraynsrGsQ0SjgwvvE_xgKhz0kQ1TtQ_9NL2uL3qGNmmqATzADCzoU2fQ9BMmMphbb8hEHQeC4a4yCb04sZAwV3Bg92g04jyd65J1t84tfy4Wk-jhsDUxw4zZ64BWMyWt5EdLFcERd41IhvwHEpEs_zYB_ta4ohdTj6Ikj6d04ju7Tgb64iZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنتونلا و پسراش دراستادیوم بازی با الجزایر؛ آنتونلا در پایان بازی اعلام کرد که بزودی همسرش رو سورپرایز خواهد کرد؛ بچه چهارم تو راهه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23665" target="_blank">📅 11:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23664">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlKSFoOtESUeGw-kNLsBXI7jXGDZ7avLdCt220B0vUZJ2ejzep6GJxlzin5RNl_W7E0Mw7e3CP4b2r3v_Mr7oP9XV-7g8S6r1SwB7J8UfPO8SG-NXstOGReMsGuVSmXB1BO_rOtfXjTYVgtINqWNd4MciZ4s8Uswgd6q2vN6EBa0oI-nloTR4lu8a2CHTiKaABCeJR-UeH87Tv5XYIVeo2l_gc3uSIjGf3z0eW_HOgnxkcidl2gE-wW3os5Vph_InebbLDrbFLH1QZZ_GiPoIjke4mQjrveoAWOvDFpMusBCJ-ol04Uslv2a__wZKHQ4147xo84wjd1_E4zs5maajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23664" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23663">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHPSWaz7hg9FrVHjX1U8PBHqAergeMX_7H6UmxydC8n1T6-r6YtjojC0YHUok8efANsHz9T_Hr1xA6Ejw4_t6epoUow8iX5ZRwQ-n-pjlSfrICRmvGQm5ABlIWQWzJWXQbNodaQUUwswoAVKpF6eJLKy0lkbX7N7LNdR4zI54xIxB1AnHOmS42wk0UCuabeOpFpSEXxxuPUdz9GgGAC4pcWAx5VAL1vSPMi5qJSzSwLInBQckYocLqlpGM0kAunmG7Q8I3o4taYMhWQ54HFIyGCCWRY_foHprMU7HU71NyL24pAAewPv650IQIY1CHULPkL2UB6W7qYsBv3f7Rm4zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ لئو مسی با ۳۸ سال و ۳۵۷ روز مسن‌ ترین بازیکنی شد که در جام جهانی هت‌ تریک کرده. عبور از کریستیانو رونالدو با ۳۳ سال و ۱۳۰ روز.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23663" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XkCswcJMWPK_2dy7LPYpHYSRQ5e7jtlvAwYmFZwgkmxN8CUXZ1dEwIPbVLTLyJAjss1gyXkvqILjkHy_tmRdPrYCfAvZdQ9ge8Ri0xZ-QLYP5S46sD56VznJMga1hNUdsqTrfMDOpqhB1DQhYxYSRn1gARI5g6-aqWyhG8tDaL5yN3phVyOHx_z0pLatRK3CxIbRQXU-x5PRdQ8sLpz8aBXmS5P75fHxDcAboMU9T_lX4hPGTVRa5ib8slSokdfjwtHP2rXOmGRG8jwwmRy8MpO7zOEi6EzvrmfCrHeuuo73OFYLjRPGOXxX1TyDtx2TSc2tHzUoZHDDjs67vm6Tfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nnVqSpnRm9Uwh5JbWZMii1jNRqFDHAWy0JhiOriJvNTKLFJ82jD9z312hIK0eZCTwB1o3rfcx1AAisy5--46gqlXjuhNXDnprM47opO1qEOzwcaytDXNiseTjNRfpy4bYbZWUD4EshR5OysdmoWSJ7DN9ISDe_BcA-7Iy-rbtfCrkke3VvpwqqpUL5iwbr_JWPjhMxg7JFAX50_qlkNycnrBF-TtVMtQETeBiTNQD3QIbQ9wg2IYkRqpe1ez4D11Y9LWPqQvZJmPzpRMRPL_fDejPsaRPqx90gKSbpUWdalwjZ66PVnsYtYp15g339F2rKmH1Zh0Rit1C8sj2km41g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23661" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=BNKyEvnzOPPgWcX6YlX-Lszeg9HM1FrQwE4l7xtBohMlIdaD_IyLW0MOQzmeMR7grZQ_kJzXFBcTT1NRntmcLOgGrbRkB55x1xXoEaTlvpm7sh-5vuJG-riJaBgL5PwaGKM5UaLfKnHtkLfCEwSB5NpgRHWZoDZ-eXMm7TiYS1RB8rLbM4Exxq5Nb7b8wpdOrgO0faJVr_8nCxZunQ4Vps5eOPSDMs0sJQ1ufYS-7JSlEOHLnGVmUGYXIFzotyvmcOzhSTHGVam2CT3PNlh3JIuO-Bhw8s3x6yppt5vYWw8CF1yPMekatJdcPcTqaEYuTl5jVZ3i6SpFMyRG88pBZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=BNKyEvnzOPPgWcX6YlX-Lszeg9HM1FrQwE4l7xtBohMlIdaD_IyLW0MOQzmeMR7grZQ_kJzXFBcTT1NRntmcLOgGrbRkB55x1xXoEaTlvpm7sh-5vuJG-riJaBgL5PwaGKM5UaLfKnHtkLfCEwSB5NpgRHWZoDZ-eXMm7TiYS1RB8rLbM4Exxq5Nb7b8wpdOrgO0faJVr_8nCxZunQ4Vps5eOPSDMs0sJQ1ufYS-7JSlEOHLnGVmUGYXIFzotyvmcOzhSTHGVam2CT3PNlh3JIuO-Bhw8s3x6yppt5vYWw8CF1yPMekatJdcPcTqaEYuTl5jVZ3i6SpFMyRG88pBZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
«ووزینیا»ژوزه‌مارو اوورا دیاس؛سنگربان۴۰ ساله تیم ملی کیپ‌ورد نمونه‌ای الهام‌بخش از درخشش در سنین بالا است که پس از سال‌ها تلاش در سکوت در جام جهانی ۲۰۲۶ به ستاره‌ای جهانی تبدیل شد. او که کودکی سختی را در غیاب والدین و نزد پدر بزرگ و مادربزرگش گذرانده لقب‌خود را از واژه‌ای پرتغالی به معنای «مادربزرگ» گرفته؛ نامی که ریشه در شوخی‌ های دوران کودکی‌اش دارد چراکه در بازیای خیابانی هر زمان بمشکل میخورد به مادربزرگش پناه می‌برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23660" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23659">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23659" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gl-gBGub9oj1_roK9B0wGwElNcJwaKQIck6LjE0lPlA3JiU3qKpTskQP6a0ImxcjA5SrCx-5KWhKi1tXOV6JShnmVeIzmWoIgFocWILyQy5hJaCBhycrNkEWa_Ki-Jhl8lDf3FCRZW9K28PCMoj78kRRCIVFH0UkHD0e26Cg5rnLX0sHWhQSDhS0mjh4-EeiyrAsEXfgCEcwhFDgY7GRzv7rbhk09uYvTG44Dq5m36oSsnbSSx-7-BQwpmoo8j2UBzwgndpJj0Jhtcwo0c3TokNNrmLcFh9g9e4RqO9v8y0EhY0UdWSWQb97UzSMDUT5NsAwlbqq9zyvM0jqpsejfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه گل‌گهر سیرجان پیشنهاد تمدید قرارداد دو ساله به ارزش‌سالانه 20 میلیارد تومان به مهدی تارتار داده و منتظر پاسخ نهایی این سرمربی کهنه کاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23658" target="_blank">📅 10:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf2oygBHnPDFtA0A5oCVXZLqd-JtbaHjk7q5mSABRRYF-tFcRUfYYnsvL7xGfmXVeT_KArn2QbFmMURoMTuEEnN2fUXSkiEyizxeAJyKowfiIQqddI6kfnshZ0kDSsKq71w7rjnQzNvuIPX0JxbPyLUx9F9n7UDR1_ZOBMr5Jldy366Yb9QW5WBtidGZuNdGoKkNaC2wFV3gUTSndlJemAbYKK6JLO0-3ng_bnEds-zGD25mRWKkIoAwHOruTKyzP2DY3xp34sJ1h7b95codftlSMPYq3S7ppxrPoYdFOdQkPHIcty4IY6OXOHYHnvGE3qjRcfN5KuOV4_u8BbiBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23657" target="_blank">📅 10:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK7W68xatU9Io7z5qOtgDhZZBDUEMcO5fv0vF-rOhGUAFFmiFFOh0Tzq9pJCKqS1dvVDAdrTM1Etb6BDEz81Dt8G2N7d2RMCF9T8GhEuG2RweSD1vovXS9Pfh72o-43A_vwA6FcVZ8BXbk_HA0FHQdVBcbUg920r9XE7YGmilvi2lLNDkhA4AHOxB-z0gMGqqDU1ypaA7GFSjkDjsDXiMVg6zf_XuHNJgFgN56KZDbMxNvbLWdFjYfnGkCjUPP0Mpm8nA7aVqtpAHWDt0XmRrvRO8n1eTorX-Wqi5k7y4jGcarz1_o2GikRNc3nd1Lreg6yjEbko-cJzMBKERp5X_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23656" target="_blank">📅 09:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23655">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚽️
خلاصه دیدار دیدنی‌وجذاب بامداد امروز دو تیم آرژانتین
🆚
الجزایر درهفته‌اول‌رقاب‌های جام جهانی برای دوستان‌گلی که این‌بازی فوفق‌العاده رو ندیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23655" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23654">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=mNsYO3xnj9yDvtkaznrNj1_QuBxyUeA6fmPk2Z-cja7PumZ_ku-YZGfVk4Y5xkImQb_M9UCaX5n01csWrn5gzcuviqBgqYGyhj9ksngkOtKOXdEMVJmk7pExaEu0VXmAnBFNJhucADdpYdnu5vip_z5-yEV2ZcrC0c5vSQXz_TxGboLTLCpBY-xlwa7vwk9PDuQXVBMI1tDNED7XpZA4tRFW_-ZjgO5_TK3UKYek3uQIL_apMXJPRe90YaP4Cko8VseHCaOO0cAd9YdBylmJTeAMJFJrauf5j10lQm91gJIrtaLGKH_XWogBUG6mCXP3P0GUEZW9rY7BOcs2JZA9rCmY9h5D-HIixNhpyYFudABpY4fXrpTskkCiltlhJNnrEjWO0liDe8euheMwFhf9iYXy9W5KKwCNj6l0nWZEU3zZKUr5AZliVu94mvYSM8tAkWKxMGwsOEvrmnaxygT5Y_JHFOttb-JJ97OYJvo9QybSO9Gf92sGz10uesmzxWhLS0IASYc8Ce8Fu5453UHCSRjr3SGQwqP6mQciVlHEh0TeYfVNn6ZiAr1BoUYsptwcY-KgnB8S9w4ggHo-8qlfnFuv_ZZc3t8I_48bTojFlD7HIu5Y51PXkGCJZDIKjxhZ6WkkzYLOpxFEQ1M4en3q2svk7QEbHCTMbJj376OQtCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=mNsYO3xnj9yDvtkaznrNj1_QuBxyUeA6fmPk2Z-cja7PumZ_ku-YZGfVk4Y5xkImQb_M9UCaX5n01csWrn5gzcuviqBgqYGyhj9ksngkOtKOXdEMVJmk7pExaEu0VXmAnBFNJhucADdpYdnu5vip_z5-yEV2ZcrC0c5vSQXz_TxGboLTLCpBY-xlwa7vwk9PDuQXVBMI1tDNED7XpZA4tRFW_-ZjgO5_TK3UKYek3uQIL_apMXJPRe90YaP4Cko8VseHCaOO0cAd9YdBylmJTeAMJFJrauf5j10lQm91gJIrtaLGKH_XWogBUG6mCXP3P0GUEZW9rY7BOcs2JZA9rCmY9h5D-HIixNhpyYFudABpY4fXrpTskkCiltlhJNnrEjWO0liDe8euheMwFhf9iYXy9W5KKwCNj6l0nWZEU3zZKUr5AZliVu94mvYSM8tAkWKxMGwsOEvrmnaxygT5Y_JHFOttb-JJ97OYJvo9QybSO9Gf92sGz10uesmzxWhLS0IASYc8Ce8Fu5453UHCSRjr3SGQwqP6mQciVlHEh0TeYfVNn6ZiAr1BoUYsptwcY-KgnB8S9w4ggHo-8qlfnFuv_ZZc3t8I_48bTojFlD7HIu5Y51PXkGCJZDIKjxhZ6WkkzYLOpxFEQ1M4en3q2svk7QEbHCTMbJj376OQtCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل فردوسی پور حین گزارش دو تیم فرانسه
🆚
سنگال‌درباره‌قضاوت علیرضا فغانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23654" target="_blank">📅 09:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">▶️
قسمت‌‌‌ششم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23653" target="_blank">📅 09:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23652">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23652" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23651">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23651" target="_blank">📅 09:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23649">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-FhbLH5IOMiSbH0pid5sWzA-0ohiTTK-jq8OctxV8NVHNb-N0fli86HvwnNuZBrvodUhlpGbr0OmWI2dBNwV5sp4yaz2pWHMfSjnHh5-EnNZ4CRKM3-NiS2w6dfXfWynff6IfxBtPwAp-2NKidAhYcRdIQB_VOlwoBA_ab5bAKi8GVUeH1uAgETCMRPg0FGIMqDz9TggLiMxqkf64lHb3dKtkzjKzBqUuFQnmCnqZbbKvZTFtdWed8bHRENGkfZbRD3Xz1dSQE_BzgFzLBiumUuQJKRKdQM8vlWFld7lSQwdNb1mxW8RgicBb-dttKlRUbItg8Ab1DIwerACLkfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FvTYJhBoJZQhDq7kB7F0CaG3vA5-miVLBvQ8W0FPlrD-7O7Ew2f1Ao-M1SRKovE_rcm9RApMesyVbDbrhmSzNatPsJjbNFgiTBn7F3G2Sqkt5PxKa29D_p372WfrLEHfbL2nfuIPhq58E2eGaUc3-mGR3QZdlBP50bnbDKA-8Tj3_tJOuqq-iixaUMtsGSLF92uP2yZ5U09N8EvmMfssd3bnoIVQx0n4e9swqfvAaV3WNCFIxLCTMPeMtwphLPo1KPJDtpXFjFKR0rFyu0n4Svrrzvezr8GBlLP5oIxkvrf4zREyriFA6cPWSujy1a1tdN7O3PJXRvy_vZSI9-Zv3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23649" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23648">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeHVyS1FjSkKkk_lyrYRpN31TBZXxVFXN5kEpYZ5hImQPM_LLBMivfxYPcETNpHHS3YyxEms-H3Rw3zUV_C3-KdU0dPdspfOaYJAQltyl4ttsR17-ALtzmIYZ_YY0OFFuFP_7e92Ccy00j28AnwRHMwIL0oUgU3IcR3m4w24t3GzPgPpCvy07ARNe0awMkUzXYjSgPSYJRysUUcf2QCnlqFSGLe6WHlKSy-12IbpJ64QkZ287bdOuBESKZ6uQV8rZPSPC6QxauUp-CO1k77mJJD5LH13hu9TbSzcrvjyhc6WWkK7jg0gRzC3I3Xw_YQATx0BzSgkS_noGgj0HitW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23648" target="_blank">📅 08:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23647">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23647" target="_blank">📅 08:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23645">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvZm0P43_sV571YCirS8q3srEUCdVHeqCHQnujoL5nL7MheHd0yl1_416gHnidel-YMf0VZCijJHxdgp-fxF7QD-vG8OrttYv3ARbpJjcNT5o-KaEoZwL_Rjy9mX6-ATmfEvbgSBoUCXvdaUjMFKjaTelrbr0DiZxT8pghL7NlP3PLi7juO-PIG56ozQzlP0FkO_osm6I4Nexsge9j7hxAApdpXF7Ob034G7urQaOP9kfEExd44lMs_IL0q39pBg3F9LzVez3wcGlpyHl4cmeHNzatmWZ7npHXM31lGNtSTMYbEMmN2yNFsyhC-FhmECLY63pYBiw4JhCkB1KFDC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LbxiZBJlKb3xJPNP6ul7A05_k0QIWHiH9RJyFuL6ilJcyFYgKlqEcRUUDX-g_x1Rcac-N-UXcFr4X1libZoKwi_N7BDQPic9HSSAl165EbhTOtGcrRZSwTCjTiFCJqVcI_Z2oORMAmYFGs-dyJ-4SboMLAMoZwkRhIK3WRcBVdnwSKPEgCJoKCzYFua0vrgnbBT6s7juhKBJZLzyERlYlGfgjv1rLXgyq-bnxd50V06Q01VsAFnAUbaUa68zCTB2VaJb3ZE2qQdurXLUllzsbc50yiz2CADF5ZwUPp7kege14OoU7ZgELpokbveswNOYB462ySZ00E4sd_4YEapc8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23645" target="_blank">📅 08:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23644">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f480511b29.mp4?token=fulu2ZMBeulpPKMSFDkcg-jjJgZnax0jc0mD3WYkUOk1XHeRyJAMJxn69dqnlf9Ly8B2RJmhVOwoSfcBoed8iv_4aqYI_177Rs6xqPwzwu9GdZXPx6pwo8LYJPqItwLk4o0wbpkV2DWhBpuT5tr-WZvjTdPjvnSvQ_3LgTQ_WzHyeeRsVzxCV4fS2hz680hlr2qHkOlWL_JE_QQxC1t0oPJ5vjss8gCi7q1N9bn_gVoV8GqjUXX8AjBpChgdBt0q-Um1G2choK_BzP9aA41Jb8RDk0IRWmBB9jK8vuyKoFwXhJHKoeSV4HJb6ERdHJeSSO0pYsOxuuoLI0UCORUMBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f480511b29.mp4?token=fulu2ZMBeulpPKMSFDkcg-jjJgZnax0jc0mD3WYkUOk1XHeRyJAMJxn69dqnlf9Ly8B2RJmhVOwoSfcBoed8iv_4aqYI_177Rs6xqPwzwu9GdZXPx6pwo8LYJPqItwLk4o0wbpkV2DWhBpuT5tr-WZvjTdPjvnSvQ_3LgTQ_WzHyeeRsVzxCV4fS2hz680hlr2qHkOlWL_JE_QQxC1t0oPJ5vjss8gCi7q1N9bn_gVoV8GqjUXX8AjBpChgdBt0q-Um1G2choK_BzP9aA41Jb8RDk0IRWmBB9jK8vuyKoFwXhJHKoeSV4HJb6ERdHJeSSO0pYsOxuuoLI0UCORUMBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23644" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbPz_NzAmGL2rwIEFuo2yaKlUzHig_AKeDoFBTV2FH_Y3YwQnQ5iEEkgVuxnPNFJzjjy-_za2huclldVKtKLd_q79zGsAGfAIt1Peynr7SB739ciX1s3NRKilicBSh1QwbyysJCS3908FXb2XZ6R3b3ETgV6jfrSIKI5RtmQEUGhKbTXR-Q1zHhJBcV8nKYO4OJrvJxMscji9LfbWk5Sr7d0munMWhUg5TbiGZQd4txGgRMfR5unJW6_gLIvFlghs0WvVnerjOpJHNOkfqy97jPAaYzkqksrUE9vlD9oZTOqX6LVYTGXkcVX6bv3DMqtU1dzt4hVKR4U8KblfuTEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
#تکمیلی؛ درخصوص بازیکنان تمدید هم لازمه باردیگربگیم‌که‌باشگاه‌استقلال باایجنت علیرضا کوشکی و محمدحسین‌اسلامی برای‌تمدیدقرارداد این دو وینگر جوان‌ آبی‌ها به‌مدت 3 فصل به توافق کامل رسیده است. به احتمال فراوان در بین بقیه بازیکنان قرارداد روزبه چشمی نیز تمدید…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23643" target="_blank">📅 01:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf4McjZ49kD8nnyUJIu2nBsUa5w8cjMIJdKG9tffPkPT1Jj4fq16i-a2w5R4P3O2fHX2bUSPlpYAUdWkunZ-LHjejD5swL3vVzTx7vQffd7EOF0Q47lLFYxIMNxfs6BOh2mlLzVwRPVcUVaKs0nxs4oZQuxE1WDkqYF-teUbhs8Rn9YtN1gfK9KzT-snu85XE9Yb1Zeqk5LfCfKyy3j4kBo_651uSOGPqk8ozDeDPBGxXRZTBaLzWIubkqZ_42UOHkqIhLXi76nCX2B2sUycE0SsYdaeYwWVeX4aGdn4gpQHWk2fWec7lhEKGk4OAGIaXh3wNY-Owdzv9rJUnOohcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23641" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23640">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USlH62WKum-AjA5stGP5v5BAMNgWINbYNOrjvG4aGVKQiQWt3bnTdIn0dkE9ElngG6--2EV1SIVT3i_Wujh06hagX7LPnOcXlKdVzk20dOTJ2jatgjAocOQRvrXpsaqhsG2PrhBhgYbb8uucx35kw5Qo0DD6X0wVdV3K6yD3jBag41fBYjZyl0oupzR7bg-42syWfyOyK1w4itwjiZp-0UWSNcJgG84xA7Z_ET1r1ip8qaUnSdHlWQFH4M9-QtO6TARey3PUBw9AO1pEo6IFdpisEDCpgUpB8R5IqGU1sOLDJ2jBQ5mp28YAVwrF5qeYkTQxqY3bM-U_zJ4q98T8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
استارت قدرتمند شاگردان دشان در جام جهانی با درخشش امباپه و اولیسه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23640" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23638">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSB2SO_hbtqwoBqDhlWSDIKTkQscOJC7LJBrNT6awM1ItPYBrh52Os68ncrguYKou04J-FI8SE8XOeJ_k4Erz2A2yrMrHKalWPUxDQxukCqnoi0TGhURQS7oHxsMkNo1p-vEL_w3VTfoVPZN09vorl53Ax4ukM-pv3DzaPh2FXuG_r1ausQfD0pJE4CZK_fVxxpYbFJxByYclq8Uxjy4cySqwG8dahDUyYRnK-snp-PfNCXao6kshq8zAuHdhSMP_bYSyKkZvKEFADTrrsR646HFRyyg8Al2x2pHqcxS-DS2oi0eHXhls6Ei_85ZV8BZiVicHEzVUT3ZuSJRjuYOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#تکمیلی؛ جدول‌ بهترین‌ گلزنان تاریخ رقابت‌های جام‌جهانی؛ لئومسی و کیلیان‌امباپه برکورد تاریخی میروسلاو کلوزه اسطوره آلمانی ها میرسند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23638" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23637">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی شیرین و ارزش‌مند خروس ها با رکورد شکنی کیلیان امباپه و در شب قضاوت درخشان و بی نقص علیرضا فغانی.
🇫🇷
فرانسه
3️⃣
-
1️⃣
سنگال
🇸🇳
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23637" target="_blank">📅 00:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23636">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRXCCDzexgFjx3BXOl7RtCo6OXdCufFxuyO4KLFCZDOG5zmFFsSqDatIYNMcPpk1As13hpbXoBikJG6_sNySIYQCxSNOo95IStUW4ZEGlpctvSQviggtbINEOI2kbtDu4wUOp_382pa6l1XrCfNJqqhRotu3b7CM4xIQ74sr3IEgFHAmGvATdG-hA35MaBsewaBPo9IVkWQEXTe-jJONgfg2OTWlek7MSZ5OBXEmr3cjmKD2n83TBiKxS-8KT8fwMFHJ5aJJmd-kMPYd0q_rpGJlsKD-XCuoWNInPvvGyW-dZFOdiBNOnNBhZytrxDYk-1G8rnjSURXeUTmcPj6h-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دو تیم فرانسه
🆚
سنگال؛ساعت22:30از آپارات‌اسپرت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23636" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkkdBEoOukaPHK4Z6_3FkAwXiLrdz37SHUeBUuUBz0CfzmR9z-m9CQk5LuL_xxpcx2r-XocpXspIquj9uZ2BIeGuecgUnhps6mCkHf4xanSBj-PAukHBJ3J8DX-WxLd0-k7Kwrpb16JL32h3Op2j87hHP115B0633bkeuHq4x3rpyHdPMGr-FfiUPEd1BCzRz8Bd3IsmMqWsC35vDCUYw4EGgPAwrN04Qg8u0KPgz9n8d7dxL_WVX61w4d666Zae7NS4u9p2bsaE5SFohRxwh4bbn1afDyvohjTld-8q_gySRDkC4H8RgFuMasWq_kcXIQEAIVadw9eKJj0jvO-njA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzWhfvbTrwqiVy7iGgUHZutMCuU8xOCfVXJqvuOYPaYgiz6fMZRF8eG3LyQwDVOq2Kc8Wd2USuO5zuSIwmXm4q4L2pzgRbTc3SyxOGm5wALBEqEewLL68TRzXUfKzdYfKcbV2_XzFhMHmw7y2XmzdKVfI-DXP-IVvFUW9mKakKK7gYV2r-0ctDXkufBN5U1zCyOZiDfpN-_FDG70DPzPwhAuwL789kt4eV0BKjvA7mEgyFRsDYeji0rre86TyiwbabzCnaM57518PuLHxaFpgg0yuMlifFE4YaKw_dkVOQ4fkN6vU0FCVbd5tqTc5hVkkpychVBBAbm7sYDSwDe_SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم نروژ
🆚
عراق؛ ساعت 01:30 از شبکه پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23634" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF07_4mFONaAF5DZUqbN1PROj3-c_VCbuaatrqraxc2aENk6wsja_84uabxlo8FrS8V5fXz5JVap-h_xPfiuZ9ChUnbxc4p_dGTG6zyAAGXlpR0QQ2RThnj6aNYflOmvMpHf19W6HyoV8hl-VadoS6ML-r0VqFCc_yE65TKT4GVbxBUSixFTLQujI1RYFfZA99TbcaO7dTU99QyIXRJ8QOWUSSvO7fqH5-YfUYFklgdavTNwN0LAwN5-KrR7epdmWNqu0PNyXpmJaYaKkQbXLWvjcsm4ussAFE20qnUoqyAJQHRsrggQZdrwxjnDscb7wsgp57bOm2NfPi-bmQpFNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23633" target="_blank">📅 00:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6WI_gLVZ1d5lCOcWEex9ychoeBAi0GJeXsETa9A3t3pKyT92adgO6_nj-xuvG6TEu-ydlw6kh5YSLZSGr7PR52tGbj0BZzOBAq-r3bSPjci32olbrR_d0k1Nq6HsZ-b6Gk-PrEFkvnMWr7tB50nZcgKUyRZleDwBqWm2fMADo-OCxcs1ePhWOwq31NGpjhvfCLFdYly5--VUcsiET28W4Iorvz2YngIN5KNyYkQPv7F0J85dBuzkORrOH7wzmj26ca1bEvKUogz4QMOPG4kOK14_RIFGZfZq5Nw62UEoxf2kNcWb0BHiqKNpT4bWhvKNABcJsCQyC0QgtYCke2vMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23632" target="_blank">📅 00:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23631">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp8QCkesAhcpE5zL7efrHW6Hn8eIiYKbG5TmygRprlSeQbLpob4zbDRB8OxRMhdz2-x5e4T3taermoa46IzrPYkLvgCZlhy_W9W5H6hxVtzn9hTWB5--wDOo6-G8Q3MfrVoYh21Tvr_yaQHgEAvop3I5QTYB8noMQexILiAz2-uz0Qel9w9eUEbRQP0fY9LBR4-qAU-G1fmdWe5uZaLToJrr7tWit7FkOdpcVFPc9IF0h99Wy5hP7JcGBrPmERv8f9fj600anWrO1BK7hnuzwBLshaqZiH1qdeQd-iT0P4nkvMcFWsh1GaesW4TFx42P0rI_XdYJ5jXYmqf2urLujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ به‌احتمال‌فراوان بزودی شاهد هیر وی‌ گو رومانو برای خولیان الوارز و بارسا نیز باشیم. اکثر رسانه ها و خبرنگاران میگن که نماینده آلوارز با خود بارسلونا به‌توافق‌رسیده و فقط توافق با اتلتیکو باقی مونده که با توجه به فشار آلوارز به مدیران تیم اتلتیکو…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23631" target="_blank">📅 23:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23630">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7Iuwyq_oywfgTAhACgxOWYys51CSs32mMYmgogA2_SDD7MfH-fLkJTvyg6NTUHixzgQdPbB28yyhAwN4viW92kGJ6Xw75c6U_DNroINQupMekMFdbRQ5SKINKp4796pl1rGmfE97xOZ_wf-fKH0OXjmJahLex-i8CnmCeG1IQPLgtlt_Ag794TMSFpJIPVGxTw6FYfT_eFTxUfGdJSM56NW27ZXlNouQx3qW2mgMBxavJYwEjmwZIjq0nyad-D_yxI7dBHX3r0ttBChVhb8DwJdZTixvgVHHUEbus05watane-bdVfG_DNN-ofCQvMdHe6zbVGR_vw299wuaSy9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23630" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23629">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=H97yvtf7_jwRSajOO9Ddui40bjqJC1K4yk4uMKltPUZRq9065SD-xS7HF0dh2-k0tE2jdVbuvNzOvyU5VVfEA-Jn8KMg_QZQ37ffk1FfllH-Jyw9I3ddpLexlyALB45dElcY9mOtixtqS_5rEKY4FZsFM32fEpFtJE4wmrzGKF8qMxLcqQRZPq_RUFGzNTbVdYFRuCSH1lkp7TBa_hdtbsneLsfO_w8x15Cj7FHhpMwO9rLXXGuwbtR14682FcXxGXeTAbjt5tQX96wQyQqx4Z8QzF3_P_zfnafIdCorvkI2cHBrycw49p0NCqNJ2TjBqPRJLghXvzlAcBP0-BneiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=H97yvtf7_jwRSajOO9Ddui40bjqJC1K4yk4uMKltPUZRq9065SD-xS7HF0dh2-k0tE2jdVbuvNzOvyU5VVfEA-Jn8KMg_QZQ37ffk1FfllH-Jyw9I3ddpLexlyALB45dElcY9mOtixtqS_5rEKY4FZsFM32fEpFtJE4wmrzGKF8qMxLcqQRZPq_RUFGzNTbVdYFRuCSH1lkp7TBa_hdtbsneLsfO_w8x15Cj7FHhpMwO9rLXXGuwbtR14682FcXxGXeTAbjt5tQX96wQyQqx4Z8QzF3_P_zfnafIdCorvkI2cHBrycw49p0NCqNJ2TjBqPRJLghXvzlAcBP0-BneiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
تیکه‌های سنگین عادل به کارشناس سیاسی صداوسیما:
هرچی‌میگی برعکس میشه. بسه دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23629" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23628">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FubPaBpieFcyd-DjpRBUsh0L-fSmzL98ZkYKSICjUVyhN6isAkEIVcvL3r8LKWMbuVpOClpiVbk6IWWoJuJ50Euj0TEbqxSNsitdVz4xbOfJon_5SQzP13vBpUhm8EjS0VPMOnaPQdQf9UzMQyPVP-2btoL6uOdygbAujEWBgYg-nu0fsP4YlGJpqPg2R8HFvwhZIJEx6xb0IWr5i8-wkrC8WEyVloaJq-XBJtjc-nWTYF70IDZVNv2HI00FlI3QSmEJNiKLcp8i45RW7p8Hjqn8NRmEt37XyZDCm5TVsO_ON0i98T6D7EXUXIRfqSHdWFSumCwTouVVRu7YqRyt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23628" target="_blank">📅 22:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23627">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQj9RmHu9DhNepNxIxcs9VV0c6cROrS69gNa71I2vzR8cuMkXzGY-SL4qwNV8YxTmVWfhwkuA1L2UetLi2SL5v1GA34Cj73h8SARD244Yt_iWvgMeaK2OFwHBKsXOrHcSpJp8dGaS6JzRW2Fc7i8qkuJzd-iHan3yPiw0Rzc9unAahBcDkIWJ-ynHAC4Z-16n7zDkpAnzmJXsVDdUSvBp4F41O5zDL4tlMecBokNVnPoXL9hu1hFv03eAX5vnnHoUTOmD3sKEaND0_Co7InwrHrs_6XcAdx61xgX4qHXukbtT7djUqba1b4oU5UqLhrw9-7iF7Vrn8H_hYn6J3flBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23627" target="_blank">📅 22:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1uz-ftm1PRn2C47xZZJODkWjA-e56MpCOyIs9FcqxaRnMY0Z2WYdP3oShkhwsHX2LbJVoO9HPv6vxXpcco5P0VLxjHFkGe7Gq-sEhpJj75ryzKocZjNzK82yH6_smcQ9PQ4dVjD5mwlWyZmHWNuhIp7cjZlS4r0d8dIu7y7WrFhnBu1Tm_TLfzaLf_X5WapJD1tXWEswzJNgQRFnq6b9hJG6iDc4_U2ZmCV6p3Jr5AcwvCF2K2JZ2ktuPQquGhuDPIQrg7yNmv_l_ZVPRpT0kN5hd8dAs8A-fTcs0WrLL0Fkdflddy9LisRU3NKhA4dKOeqwBgopq9O_VPxeLylZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23626" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpSOIkX7DeFiD5Lxesy6ctdgZsj4cjJ5VAne4gR0Q31IHMbLj5kRAJtYrPltuPy4v1sno8gdGo3bRqfh_-nZmc4S0gPtFT6JpdlCm7IFZG87ohuF2IcCe9Dw8zK2qb3YZvGL5uiKCVjHBzecsO_9aUtdwDavYbOM9kMoUznTbzMp5w_OU4lJKgFhXfDMx6hDpfQw8PlHzyvbDDGKWN0u9JiGlSCt5vibyaVajNF3ieEC-DNCb3gLIEms-jjLZe5ns4gr8H5ngqVSAjP6JUI2Uao-NotSIhxnc-7NTMrJth6nN7B9jgpE7hUHZaQtqOvfcjLUg4u6jZjj_wXsVDCVUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23625" target="_blank">📅 21:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23623">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHrDsikfoIycr_WQHa2Vit77vrEgauRvEOqISrj3YWqBGtZa1LBW3hYJHoR5e0W7kMShg7PYzpAW-prWhc_l5xDAa5Z_GOriFgG2lO3Sqlx53G0dpbTsjTL5LC5Coe39hwlsSl8aasMWy8PzVDnsdbHLHbSzO6OKMXXcEhqsHwBi9sVZyVHfLIk9YYlkR5ICD79s4TRPQajoBbWpukUm2_ggI1JddURQqctHRp40926D2YVRuYeQYNdWAWh8muYLKYkunyoTjddWHD3yMHbQCahb9HCc_ngYsRaBKgk02CYduSS3K0ap4qUIhMABhLnygEGb_WXoj1f-RUB-FNXqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chBA44eU-_sQzgN_XKyc-gvqOYWH8wCQykIiYIRw7pfi_5jfxmr-bmA1rzlvq1jMVeql09rDcs2NkHPkDQK03PQXLlC6fOMMH-M1548ei0LOI9Bj1H22Z6VIEB89ZLLWJuraeyQnyw2k68FYSRe3vNvPWU_ZqMfbYkmFx0B2lc6BRIwTsIVbSdxSeWQfJUFUNXxyfgsDh8lUCNMgTOjk-WeHe93v4nPRtvwXVlBKMwHAvLaB_X0iK84OPeX6caY_2hD9t_2VftpG5Wy8R5qAwpVabw82mhSGzZn_pWagiF-iMRri62jSv51FkMLOSXpbhA5L8FacXgp9PYLHJHPKEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازی جذاب امشب دو تیم فرانسه
🆚
سنگال رو عادل فردوسی پور در آپارات اسپرت گزارش میکنه. روی پست ریپلای شده اپلیکیشن آپارات اسپرت رو گذاشتیم اگه ندارین دانلودکنین کیفیت پخش عالیه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23623" target="_blank">📅 21:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23620">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJxr74Ary_gX9ci_y76HqRb-kzRM0KWMuXfjkuasaUbg3iKa-hvgmmsmAT8ho4qLcB9u5J8ol3kCjukbwkFvs2tXpCnr0da9DSiUMAlxe5EzILMG0QiJUnCay3C_6PwCfhbN0XAWvgMJSK9283txOapCnsiUuVg2xKI_P1-PEneYAji8MA_atXjiJpK4rJnwwnr36X2lOjROPDSwYL8gzm0VVwrRSR0zz_g7UOwDdORZqg3KKVgeX4Z0apZ97CFkuhwppFHY0_L0xf_-4VZtx99yehiyGCjlDrA4wXPpfET_NNx8JrewsqcWSp97ZWNUF-V-HxmZevzN680vRzXOmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23620" target="_blank">📅 21:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23619">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nppxUnRcI87q2TBKOTK7iDKIGDBNjHzM17H--4X-THdeJFoB3ayC9V9OoBhFYDi2Q_F43H73zBPccRNpyKu69jzzW-xYvF0hXddARKp-bMAza1eYXgjoTnajvYkaqgmOjtHnnuo__1kvYfZR7MkNGTsKVRoCowsRkV9Kms581QmxfGyqfiqcUoMrI9xegZAwC3BQyTLu8M8C1NmLpWg0HY5gldkUwfGoo9SXida2almMTu2dNf-ARcXKi3ZKWZEZWBbcJURdfsaxsUzbhXGohMAacX7INIzN9Q8203Si5kpjkjYSV4DejRo5eiC0AH_KG40DeJr1O7xUK_H4YkCx4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بامخالفت تارتار سرمربی گل گهر؛ انتقال مهدی تیکدری به سپاهان در پنجره نیم فصل منتفی شد و این بازیکن تا پایان فصل در سیرجان خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23619" target="_blank">📅 20:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23618">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335ba40687.mp4?token=f6JhPiu6WXf3-Hi8G1ZgR40_yeCITJirGrE6FeuXNuuU91Rp3EQDYo9mIrnrmDcJQ-JP1OyOgeHZ9MPxinEw4XqVtKlRUPdDdPjEhFvQ3M4cv5EzgHilOA5_qp3lH1Bx0_n56Dwx0zylN8vZYOF2IhQrREucqwUtpVIw05-mxiaCMP2Pqb_OfQfkB3IL9HsknHAu32ESUCfDY3sv_QMTkbscjHw5nMwSVcQ0nq6KOU9ArgGGvKFObxHfk6Jk2_E01vOTnFFIgSe9xvJgCoQqPegH-8iwx6jFLVD-8f79cbyfgd2jEGFiFppGf67AzN_KcYvcd6_4S0iJIUBbIcnWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335ba40687.mp4?token=f6JhPiu6WXf3-Hi8G1ZgR40_yeCITJirGrE6FeuXNuuU91Rp3EQDYo9mIrnrmDcJQ-JP1OyOgeHZ9MPxinEw4XqVtKlRUPdDdPjEhFvQ3M4cv5EzgHilOA5_qp3lH1Bx0_n56Dwx0zylN8vZYOF2IhQrREucqwUtpVIw05-mxiaCMP2Pqb_OfQfkB3IL9HsknHAu32ESUCfDY3sv_QMTkbscjHw5nMwSVcQ0nq6KOU9ArgGGvKFObxHfk6Jk2_E01vOTnFFIgSe9xvJgCoQqPegH-8iwx6jFLVD-8f79cbyfgd2jEGFiFppGf67AzN_KcYvcd6_4S0iJIUBbIcnWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
#تقویم
؛ 20 سال‌پیش‌درچنین‌روزی؛
لیونل مسی اولین بازی خود را با پیراهن تیم ملی آرژانتین درجام‌جهانی‌انجام‌داد. مسی 18 ساله در اولین بازی اش یک‌گل و یک‌پاس‌برای آلبی سلسته به‌ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23618" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23617">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb1evUfI0WufRvOmc4Qye7z1a4z-k8zbM_7l6swIvCzeII_AhSXhSPJBfxh4Ie4UPR9qZG4J-DCCWfSHHetHWJgpvQwednmxADS4H07Gv5RKui4NdCxQ_i36IC0Y7NY746G00uHWjz2sImWjJtEf2q6KKNlh8KGZyIRyN6I2N4yh19XJkZA0k_2UnYvW7Me9emvlRgb3iz7c_4qsQmoHICGlRCUaREG01J9msajEjoPLo3nu5mW9rPf4N-M3t3w28qeto7YZHYx9AgC7FKvEO-AgAyTMUweYEvPC9wsfjbi93UatxIOAOUfGX3EZuke9mUCHXlnc8GD6SOsyzoRZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:  2014: تنها یک بردمقابل استرالیا و حذف در گروهی. 2018: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی. 2022: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی. 2026: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23617" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23616">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZy8nRhY7_X_eJsK77VBgBX2CWi7ynugKNVJUD443fH-Thq7B7-4HNzCcOqlbxLeGqxEEuh5sfab465vuxmGaJFMhLrro-GcQpUFa-MMdV5EA22ca64qy4Snix40qfLQI72yN8V9VXsFByQjlGvnWFnuST-kCV0E2BLu2RShVT08zgo03mHANsWq66oRMvCdhmo2msNtmUnI7azMnOkZ2ws9u2obOJW5zaPwYcbdzl5c3_BANz8MgAn6vvN7ryvXdvbJS-tWk_LWUG7aPyky5Wb3cUEjC6W2QuL0rb0OHG4DHssRw-uIFY-PXAMuKzFeahgUeGPM7biTMk8wu8j0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23616" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg_zWeJa8gwD4KxK7FivhlJEvbhMjqXB1qhEanKRAiYldr-Tbrl2V7Liputm-B7guRr9p4MTnvRqp23IAlh6Rck7o0N7l42cJKrSiDUObYTz6Q9FzG2gWWgEqaE_VEjrxQOqThXHvbGGMriWrmxGF82B-FExJqUqaY7y2-HiLYm5_CD3NG-6UWJ628puL_-A4SYZ96XM7CdOahgUi4dMx_maRHavXz93NMl2AJylU8Y5wIZfRGyp9JZKQrrPIcQYiJOPigeoM7qd1Tusla2YN31lgfSXfMi8sdOMZl3gbnsK4_eSrVto0grB6OvMSg6s68Xex9ecTIV07lCVc6M1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23614" target="_blank">📅 19:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nopWSyymPfys43kC8Sahs99LCuqZCLeC1bW4qWNShvLlAOUo2w_MNQEx5lTcyHvWHA71K01wjnfFfOM0Cb_Ljg6YFSrHNCj8UeIczEv1CbWEBc5EsBcg_O9xrFaQLLUylLEZjUuB11cdYuk88kYXj_35JaW3YZy4yoUBJRgtlHhacMCq0BumEegfC18qNtFEUJd6KpeMU5EoiOYlx7VeGJgo3KlsGCiWO__RsDjf39hHMdbcjq-Lnua_VXBAsXRnVfqfjkTxaE6WegDefv4uNY1kG_oMOn6wGVAvnyiKYlw6Fp2vob5Vz8pWFsC2DPj87LPK0SdTw0hyGjoQFS5wwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو: روبن آموریم باعقد قراردادی سه ساله رسما بعنوان سرمربی آث میلان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23613" target="_blank">📅 19:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVeXQ8gu5C4qm96b0lIZz-kD05EiJ9LUMAOg3TtkUKCFnWCAjgECSh1xJab7O9eULreLGSug3aesNgXGtLBpmDeLi4i5J3hDCt19wUjkSDsxgiQHFFtWlQXRDAiHI0B6CbuyWL81f-KosOBzgNm45aKmQkFwlZ4tdaP6MnOekaMVBEAyPGfOgwdZemOJrGGCpQLySxORTMXTBvopyePExr9VZ-9rxJ1BZGRTUL3OzZk12ktYABfS3k70OpzRYNH3pYToGP0TEpWL__Ioo7qk3Bir7G4JdXpoi-C9xUNFdKpOCDql74-rOqWkJ7UH3Vtf5I0WheKOSY_8NZ6iMM5bKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
⚪️
طبق شنیده‌های رسانه پرشیانا؛
عارف علامی و آرمین سهرابیان دو مدافع میانی استقلال از فجر سپاسی و ملوان پیشنهاد دریافت کرده اند و به احتمال فراوان از جمع آبی پوشان جدا خواهند شد. سهرابیان از ابتدای مهر ماه سرباز خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23612" target="_blank">📅 19:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328fe52870.mp4?token=U50gwnfJGGuAGIUwNr8DSSQhUY61hVIx6kpFt20HQtZc83qt3dN27SKQVwCDhjQUE6QehrxZW_toBD5ETqxV3qmuYUJp9JZFNfTqTphLosDH7zWUGcNYTSWQDqoUy-sV8PlFaMSmZMUz-MxtCEPLVcaZg07mUCIRbIVISzv0E5S4LCn3q3qRKVLrQKyka5epbGxTK00eqGx5ruhW-LkJa9i7TJaPtWlp_GkjuBTKE2A2OylUddatcYWb5n4dm27GW0RKc7TP8NYF9hH88g4kMow4_Iv6q6ZrYf6BTVHXZa9sjoA2Y50XqaC1h1boxDGtjQspSF6j-ZpM24i0fyGgeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328fe52870.mp4?token=U50gwnfJGGuAGIUwNr8DSSQhUY61hVIx6kpFt20HQtZc83qt3dN27SKQVwCDhjQUE6QehrxZW_toBD5ETqxV3qmuYUJp9JZFNfTqTphLosDH7zWUGcNYTSWQDqoUy-sV8PlFaMSmZMUz-MxtCEPLVcaZg07mUCIRbIVISzv0E5S4LCn3q3qRKVLrQKyka5epbGxTK00eqGx5ruhW-LkJa9i7TJaPtWlp_GkjuBTKE2A2OylUddatcYWb5n4dm27GW0RKc7TP8NYF9hH88g4kMow4_Iv6q6ZrYf6BTVHXZa9sjoA2Y50XqaC1h1boxDGtjQspSF6j-ZpM24i0fyGgeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
وقتی لیونل اسکالونی سرمربی تیم ملی آرژانتین رفیق سابقش رو در کنفرانس مطبوعاتی میبینه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23611" target="_blank">📅 18:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23610">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isNKT2a6CGzpQy4M-h95io6TkxU2-Wg2exi_GHB3PmACdKJoH5K22kL0hUDj7SlEnRxuBxTengFa8iyBQIVn-VYhVKF6EurATGjDufjogKUWZhkgkt-6cIJlZHVYTkpEPRoZZoSxAAnYzw5ejqs9tq0ZbQ_6aRWS6GTRmloaUbedV0MIJN721qEcd6SCvdoFZA7DF03gNiAEiSm8g6w4u_MkCEHoJBZpEexnKHjMvX6fPxznQitJB2dh8E9DJ_-4d74Pw3veT-fyxQZkNVC3Ak2joCxRZ56SaX9Zle_rkZthgO7YGNDvnYhGh0aTjrWwHRyIHMsGhDTQLzjQfyYV5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آریا یوسفی در اردوی تیم ملی: فصل بعد یا لژیونر خواهم شد یا در پرسپولیس بازی خواهم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23610" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23609">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqafY5HGRrn_hlA5B3kfk3HeBcf5hE3cXrxE3hTwJgGCst5pqDQI5M02V0L-apowqr4_XH6u95uuLAxpLK-ST--Xpm2tAPIjcF54YCRQ_KuL_IPDFSc5qvVHdjvkaHevtFcfDbWymprecJhLMyUZPC79fLTiV6BI-EhJJkPVUB91jKlyK0YUIs8erMuuriikdWa5j9uH9D-h86Gx1vGPlpjZkFN-jg4BPdisYmm3RWuaNgPp23bBaMQyadSNKySkcuaBrdQivlDW4jeKQmuk3I_NiCroj4VF3zLXknN7rXtvGJ0u7KZz2v0HmnDiaykwqLrOneewGv-MMKswLLHDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
مدیر ورزشی باشگاه بورسیا دورتموند: چه رئال مادرید چه هرباشگاه دیگه‌ای نیکو اشلوتربک رو میخواهد باید 60 میلیون یورو به ما پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23609" target="_blank">📅 18:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23608">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk02wtp3Ds4InH-5PdtZFw5BCFcupCJZwlDl2d0DWx8yAKgA7gWb8mPUP-T2QUS7iRxkXQVQ1AgJlQyIqQ5CcIDZtWEmUeAzAOsdLzxFjpYFoRqwfkcDCdVECMv3ylrx4olG4OkWVxDc5FViaKWJ3wp17DBbuzYDReQI8F_9Vv-rmdyDJRDFt0vL4KPmUGIvFWNJiM8O8ynIAsoOZPH9mXmnct7vf0sFz3X6dSrE9QMjdTsdK6C5gpz0OjjZE-nPmDIQNPDP0Ke2uiBbyyueEVFC7D9p9H5A6iFvFrodKy74zA1h6s_66Yz7VFK89cjC14KJQZykPkZxGr_jOZziH_Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk02wtp3Ds4InH-5PdtZFw5BCFcupCJZwlDl2d0DWx8yAKgA7gWb8mPUP-T2QUS7iRxkXQVQ1AgJlQyIqQ5CcIDZtWEmUeAzAOsdLzxFjpYFoRqwfkcDCdVECMv3ylrx4olG4OkWVxDc5FViaKWJ3wp17DBbuzYDReQI8F_9Vv-rmdyDJRDFt0vL4KPmUGIvFWNJiM8O8ynIAsoOZPH9mXmnct7vf0sFz3X6dSrE9QMjdTsdK6C5gpz0OjjZE-nPmDIQNPDP0Ke2uiBbyyueEVFC7D9p9H5A6iFvFrodKy74zA1h6s_66Yz7VFK89cjC14KJQZykPkZxGr_jOZziH_Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید.…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23608" target="_blank">📅 18:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23607">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=KArDRdz2Y3B7iRq9oAnXCsn9xIXVm-Vm4d9BH7NMZWYVcPWv16Y9oVMaCrkrGzuPCaFshF6FvjaLiGTxq2FY-vNN5YnN5RhQk2Q7X6B7peRek8wbT7qhGD8fKJdUH6aBH4YI0_zk8NhHeVm1HQHrCGarKPtkMz3fY5lCd6b8nfqRRcTLxJh75DiP5CgEeXbKHb1w2J_EQGVXB9D5rGgg4_AExnN034Mx3bdUFIB4ty6N18gLoHQkNx_jnSlZfpSsWnbVSXMlPyzWsaT4WqqKg9CxMi5rsclFM5Kf1ASJJWaxuTkBNeGesUztifLjrRsNuuSWR7-ksatQ2M0ENbY5zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=KArDRdz2Y3B7iRq9oAnXCsn9xIXVm-Vm4d9BH7NMZWYVcPWv16Y9oVMaCrkrGzuPCaFshF6FvjaLiGTxq2FY-vNN5YnN5RhQk2Q7X6B7peRek8wbT7qhGD8fKJdUH6aBH4YI0_zk8NhHeVm1HQHrCGarKPtkMz3fY5lCd6b8nfqRRcTLxJh75DiP5CgEeXbKHb1w2J_EQGVXB9D5rGgg4_AExnN034Mx3bdUFIB4ty6N18gLoHQkNx_jnSlZfpSsWnbVSXMlPyzWsaT4WqqKg9CxMi5rsclFM5Kf1ASJJWaxuTkBNeGesUztifLjrRsNuuSWR7-ksatQ2M0ENbY5zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره‌خنده‌دار هاشم بیک زاده از حج؛ میگه بری حج نمیتونی با زنت... دست بزنی بغلش کنی
😂
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23607" target="_blank">📅 17:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23606">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXF6KYhid8lPhRnf9pDiFeKlENkpi8PSB5EBBNq5A2ZMm1gS_h2G5GfG62bUtt2qCg--PmFY59HW5s6K3TVW3zYeNFZtBVSwk-PozoOKsYQXmXafWImSy1Bp9Ntpvmp4NkSb1FtIBPie84oAogXLLixofDjPm_z4nZ25ZKwcqpV3QMpaouGm76y3rI_OZh3ov-Wrt09JkngYssFe3GRDqtQ_HeqnO6w-P2Le9gM_IA4d1LUdzT0k8HiWcWouMDQZKRPDwfW4YEbEUnCOZWz2kQ_tbu9RiUvRAhvw-58KaMvPoEkCbUlb7FZ-fAVpcBPh2SaCDkW7aWw80wHMuKHHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید. 15 برابر جمعیت کشورش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23606" target="_blank">📅 17:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTEVXf2HrQNYGZKmpTZoNgxtr9Jv5rKivIueE7MZH8cphrZlR7N_harq7HAw3s397ic3z2ccH3K32otTn-XamqQkk6kQK-I8j6qywqSU6OQoq9K-aopBFXp1VAWuOMMx8qmWIxmZ2WrA7vidDN_qxlgycHLP-3sqpGr4Pjz5coxSQlXFTkXxFSeZlrLX5fc16tY64n4pzaiM7_Chiq8CFMPO0FthkeD4wJyllOp5Lza7oOmyPE9115St9EjijQxvT3_-ADo2st19rCIh822xL3AQbJO93RYvDL3xLgEA4g88D90qQ_wDRd9f-E9asgZ09v9ME1DzBLvfbXhBsLGXJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPDn3LegheOItwGcvK_mIiYJdDxUg7Hz9nJjJEHtNoYBa7N7YzK_XnyVnyEoUmk37tOFlsQQlRZQQULnf9BgUYN-DEfIXnPKkX6-SpB20e4qDIK8DrWYzHEfobeOh_pl8elXNUSNfYfDHK2OuG-ZH8dVJQxB5EnO5dobvGmI8YPScedYs_p5f6MrV0j9KBxzMyMmcPJykx0hQdvHVM7YUVnR9B1l0SpSjlJFnLTzUMXj-zwz7dbqUf87u6Hi76q5beM7b1enA7auhj-Y_DVRPJnsTs_0-vVJ9lMSzjK8ymVOYw2Ru8d3NQVPUIWElLzFXWdYPQDJlomUvz-eaN7WIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23604" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UseF_k_kkSvV8jpQGmqWUN4SWc0HoMmkt8Dr9Z4bQ_kSitX4jsmHSaJm5SXV2DiwOwn1Ske_5pPvCrea3c63fbA-1MfeOHGWIgpu9gfdSBdj6JygieN-hyc30qNsasHXBVK-Jb2FqTSs42kR9G5UfZFDpFNdYpLIVJGU63ACHYUIlxG4sjfzneqbdo1rj-YaQHH6M-YOefbMozOzKH7csbNLaNStJqKYe5JwqszLkHrCrhpJcanhWjDB52RnIInztBa2g7sz9HzzTZF0os0MbgZPioLnsA48tSyut2sz_iES7yT_iLxMO2OSRGdM92oLuGn-Pqt2Xla-hXhRKOUkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23603" target="_blank">📅 16:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCF8xBum2oGw2taiMf-P9XPKPp9Ne2Bvgua7XVBnzb4CpLxK4dzVzI2qVJhJmgjL_HYX054T7EAJSRkiCdH3nj6WigaSDx1RK97lDKU8lMZL-LM_yDO400Z--Z-yH1a-o2WpQQaw0xQflDqEsWDqV8pGg_NAKXVSgyRg34afs9J5Deah2ivq07NvyLn04eXBYB5m8l_e5UsjzsVgnZPkCbxZxoZrBTm-EAGZltnlAzlgqDK2VNfYWmr4gpNweXmb9D7KvbDMQ9bT2ckCXgJdEXaT88R47H6dqVf32332GB4b7BqHY6NUtcq8w4riZjpIF4rxKGxZEYxJiX-tJdxVtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23602" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=EOWMrVG9j1zEVpNa2OGwXAfmc8a3bzdzwT6Mn_RP0h9Au1WK2R0AXW9dt-UNQXQ2Bs25QPweQNmEv_H1TKa3RRYP8bbktJwY6CK3IMmeZmqvj5nRMfmVEEZhaCyr9htsAzs9H5NGo5_bdMEp_pI7AuDANZm1KLRB-H_5RiJIRVpuGF_dzXZbcS_NS59pd1T9HTnTHgSAwP8L-CtV6X2c667cbSopKCvALqJtO4Vcr0_AWKopQTzq3Ay2jtHUX5lBQ3uKVtINMx_zULEXypn-KjVEN3uAIFLqDzuN9bQjJa-mMRSQn4XF9wIaTGCsfLtn2p8BP_P5Uxr7z6mtqMcLLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=EOWMrVG9j1zEVpNa2OGwXAfmc8a3bzdzwT6Mn_RP0h9Au1WK2R0AXW9dt-UNQXQ2Bs25QPweQNmEv_H1TKa3RRYP8bbktJwY6CK3IMmeZmqvj5nRMfmVEEZhaCyr9htsAzs9H5NGo5_bdMEp_pI7AuDANZm1KLRB-H_5RiJIRVpuGF_dzXZbcS_NS59pd1T9HTnTHgSAwP8L-CtV6X2c667cbSopKCvALqJtO4Vcr0_AWKopQTzq3Ay2jtHUX5lBQ3uKVtINMx_zULEXypn-KjVEN3uAIFLqDzuN9bQjJa-mMRSQn4XF9wIaTGCsfLtn2p8BP_P5Uxr7z6mtqMcLLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جز‌ ترجمه‌های‌ماندگارتاریخ‌ ایران
؛ پیاتزا میگه به خلاقیت‌توحملات‌احتیاج داریم؛ حالا مترجم: سرویس خوب میزنیم تو دفاع باید عملکردمونو بهتر کنیم:)
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23601" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
#فوری؛ کسری‌طاهری امروز بین‌دوستانش گفته مذاکرات خیلی خوبی با باشگاه پرسپولیس داشته و بلافاصله بعدِ اینکه مدیریت این‌باشگاه‌رضایت‌نامه او رو از روبین کازان بگیره راهی این تیم خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23600" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBI82K232RtpWnROBQ3WBHKuaDzrnNUu-Za7NT5f9ZhKPUys49q0cIyS1Ufi7i-Zblt6iTLRYmV7PDhZCWClAFmfP8tUvQRq8mWBXJzhfHmSlpAGBsj-YmHz9_95b1v4cPR8QeKjWyjp3-Nsmv3lrOXu2adRaZOD0_bcYxP0a4MG0RWjP54erP6JERSAjZ-BJz1oyvo7ITpWAfptR--S0fe8ZmDPziUiu5-LPScd8qkSz138Kyws1z4azjb_jgdlRnVAx91n6AgjJg_C7rOtfMbqRcNkd__aPk4yzTWstTruTXcqBtK-S2H6QwISGRPZjvKknBuwL2sdNdTeS08-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
تیم منتخب روز ششم جام جهانی با حضور رامین رضاییان و محمد محبی از نگاه سوفااسکور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23599" target="_blank">📅 15:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23598">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPU-B2XJXbMt4hb0qimFivDOFs8I_GptlovYjt-lypLzNMDH6KK4ch_cBRe55dblG4aR2HSBdRJRc0IWCMx4_rqtU7sD9OrV2hp0F7HZTAvNCTV11B7ao_u5mX_V7u3qhWSe90x5G3j7oefzYlOR322aDHx-CjXZ2RIYHEVNUc5thaA381QsZs9id2RiP9AAJklDZouI4fW3P4exHpS6gUDjZj3ABWwO1cRaU2hr-3pk_EZU8D7OFodQX7kHypsYrh9N-xA5c7g2n8WDzvY9f7tH0i29HC5LSx7XpisySMzOf1gosV1Oq0SL0zi-6lBdaYa-qGi0mvNBDRC25h6iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
روبن‌دیاز پس‌از ۱۸ ماه رابطه و زندگی در عمارتی مجلل از مایا جاما مجری‌معروف بریتانیایی جدا شد؛ بلافاصله پس از این جدایی، با حضور دانیلا ملچیور بازیگرپرتغالی فیلم‌های‌هالیوودی مثل‌جوخه انتحار و نگهبانان کهکشان ۳ درجایگاه‌ویژه‌بازی‌پرتغال و شیلی و تعاملات این دو در فضای مجازی، شایعات رابطه جدید دیاز دررسانه‌های‌بریتانیا و پرتغال بالا گرفته تا او علاوه بر فشار مسابقات، با حواشی سنگین زندگی شخصی‌اش هم دست‌وپنجه نرم کند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23598" target="_blank">📅 15:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23597">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=EUKlkCzWiIRr28nO0NBQltPxVb-gBbw8xL925EQIAcEkKqwfoDHz0Jc4ZS2FMmY275eM4mLZmZqQk6Ilq_oWsoJz_tw0f6Pf37svnmT-VH9zbRFX8Lder7FVIOyvBjUYfBZ-7qKR05hlo5MFbNZ0bmVwIlRqRm3zLSMeoCg_rd3AE2s3zky1n4RsoH7bgfvLbTRKmar6X6gg5LUuqZ0iHSxzgBMeGV1XexiCyg9Gwcdk_-VQ3vU7ceqCCHR-huiHmViJwcFghqgrOvwrhHNx-L7biWyhMZAI57pJRqwYe2i7BwbYY3d5Y2Gfoj_VYvr7XvkNhvs_B6L9kmyaEdIrqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=EUKlkCzWiIRr28nO0NBQltPxVb-gBbw8xL925EQIAcEkKqwfoDHz0Jc4ZS2FMmY275eM4mLZmZqQk6Ilq_oWsoJz_tw0f6Pf37svnmT-VH9zbRFX8Lder7FVIOyvBjUYfBZ-7qKR05hlo5MFbNZ0bmVwIlRqRm3zLSMeoCg_rd3AE2s3zky1n4RsoH7bgfvLbTRKmar6X6gg5LUuqZ0iHSxzgBMeGV1XexiCyg9Gwcdk_-VQ3vU7ceqCCHR-huiHmViJwcFghqgrOvwrhHNx-L7biWyhMZAI57pJRqwYe2i7BwbYY3d5Y2Gfoj_VYvr7XvkNhvs_B6L9kmyaEdIrqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
یه عینک بزنم تو برنامه زنده جذاب‌ تر بشم کسی زیاد توجه‌نمیکنه‌بهم؛ همون‌لحظه عادل فردوسی‌پور:
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23597" target="_blank">📅 15:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23596">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fs_dmXQJPqn70BB2GySFQFF5wPomiTEyBMMS9fDJkhc2_SYY7g3glBJlBIVJHhcUWtR5h1cfNvNu0Ba2YLrFIoStZvfsgIhDhGzoQcfG1CO9yhLFTRgRAAzJDg1-ybTgBtTfxL25s4O1ksPxvhO_I3I5G329FbbhRNUSqYHHVqWfx_a_3ntp4jq-tb_PKpEfNphQ5BENtY2K5_Lp1s59iDU9xGWa5o3ZrgWrwVO_JBoaYrjROalfs8gTG8CVEQAjhujPy52MQZYIgp4EM25GG0q9DWqWkm56j3XIJZ2igELHUj-3a5ZpcGLgoCNubjwwNoz2lQxLwDtnEzN5zZBFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌نشریه‌فرانسوی لکیپ:
دولت آمریکا ویزای مهدی طارمی و مهدی ترابی دوبازیکن ایران رو باطل کرد و نمیتونن تو بازی با بلژیک تیم رو همراهی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23596" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23595">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyXRDNlRt9nz0LPMQz3f-wH5cIhzzG_J1IHL9VZr3g7ZTLA1haDrbhEtpmFva_EUI1msA8usxZtW40rMTUN49qhZm2YPa1ad8LUGfLiDvdgMS67R9qyVAlLwYbjNJ2bEy1kNvxpM2Hz2r1sVPC_NPf8CzsgriKtzghxCgRRMWlxfTDeWM2NUstVg1_DwTkPnATlHL356qFfOkGq_eEd0MQu0URnUt8PjqRkl4EHBzmrM5XKGgQ0HeqM-EiGddF3kUXu1khh_hTnEEkvLPFAWwY1aB0fRoAcUj59omuPgU6qHdDVG0m6envpEkuWtSOeNAr0I0w5B8Q1TgJ_HCFEFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بااعلام‌استقلال؛ سهراب بختیاری‌زاده بعنوان سرمربی جدید آبی پوشان در فصل بعد انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23595" target="_blank">📅 14:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23594">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0ymD8ecMLC-VWkmxMUOuE2k29HI4d6-KRH3FoeQ1MYIPzQSyUkqft72H2K1wD5tRPPIeowmWoYMIIdb9SEUZDe528CsmyUV5MME4rkJEQLnywoSUVIheAEv0KPguy3FlGU-AyRtvhR8sOcE0ZxpL7TbmexurCUzisR8EvTOzTotigMiD-Oj255lzxQS-eH9oVr_7SWJbMWas37D77mwSK2vcCePSZ6Rib-UMtQece97MudHpInOWtHQBOjcErA0Z7jizv3ALyhHE12QjSV9ToSyN1ta-QdFpof0asxGHYBoygRBL9ZB9uNud3_KsVyIPfWVZei80YWqpCNUz-VE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇳🇿
بازی که مساوی شد با اینکه نیوزیلند ضعیف‌ ترین تیم‌جام‌جهانیه؛ ولی کاش تو خارج از مستطیل سبز هم همه چیمون با نیوزیلند مساوی میبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23594" target="_blank">📅 14:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23593">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDsVgmRgHXlC8ykILExp9Pkob2vlri8nXgIPBnmndtpY0dzanCcJXVnqpO8lGopig57sGSWghWb_muvPad-O9Q4q3r7qCCfrxf6tfNMnwXK01oEgaKMMQVA2cGrQN0ZtzOZ3RUJeU7bNzjku5DYgdwlINwuoMQHGFwilsFrfQqqTOo24DdEUxbAaeVf2_38NCUDXH0pD79bZ0qBZ6Q4yvs0AzJpJDYCD0YbaV_OHpteeMWqdJdT7mquloJE4cNzKPniFXgBBhoXWM_c94S3r7Hk_f9c_sMuTQYkDYlJQRrU2s8xy9YHx4eOagc-YiY4xUFKSIvscx_9OIYunlCfeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23593" target="_blank">📅 14:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23592">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuWCEbvwHI9ESwKy8Kj0x7amLsQUntK2TrDXQJP5fFd4te418qrVIlE5f0Kw7vDVZublRg0tQjzRNRldz0IlXpfpSBGMKtgzjNaxb6O31xtwP1Nn-NMwobMYZDsPggXuNlm_9mVJtUTlDDqWgSo_loUytpD2cj843nQSE1Bezwo6FUkzf2c7XHxua2Brlh8t06LIwQeWIOnzHEiTpsaGPiCwpj2DdxFsNpn6eWtMuTavtPgf4umzh7tXoPoTxjNDeBfpipl_oFaYCFgJDlwUh-Aa2UZNl0NcccTwZ9DY0whIMeHgHzoGgOWlgfqTAJAn6apfCyR1TIA4_86jYGGVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23592" target="_blank">📅 14:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23591">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3yVBBN2RLpT835afJrrM2ZbijiNRVzBUlqfMM6PlN8qsbLRW-L2Dn2fMipJB3qOjZyfQCoglKzhVeoxTFzB-KTtHXug3QR_3SfPqExkBZOqHTzcS5Bzz2CvhZMGG_hDKIQlg8GSjypvIJLC_S5a6JuXUbSDXA6zma2pEilqOPSnZyQP4q6RYI4yirHnyHxxAM0CkgJ_v1AR2sFoiahy16yziVwfd_S5VhTW-wlnU4k3MAPPZVng5OXtfRQl-EEDeTHnU7aojStBHH5bSUuoklPBg--x8aznmTAajDXxK6x8sUhna9k6XQ3ddX8m3myaFvcXc6lfygQAcyxHUd2yjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23591" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23590">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=benvlc7o0i3-xVvsYBWC31Yejd4GDIaB1Y4kn8vO8uQaXAD2ZoM3psfqd8KOm7qYU9J_i_7bpLKRnoZW9dqrnG0kC567ljVDhC4x00j9PZQxxoPLrGNUfH_6HnZW2rlYN-D5ELHyPyUYlcUx0gRc4ANCmcMk5svdgcHWpOT8NTrIr6n0nd9jN_kHYqYXNGkyw_sXWJSM79lhNIIV-JwJPQaHLGbXMAj_g1LNTrW5CBdRhMRaYwH6AFIzIbbS6po5hNC4DSxidiTY__95X4MRzcSB6AJVg8D77RSqKuE5Z6DFozICahv4iu2hnyHWuCrSlLqacmEIHS_fiTV61ySP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=benvlc7o0i3-xVvsYBWC31Yejd4GDIaB1Y4kn8vO8uQaXAD2ZoM3psfqd8KOm7qYU9J_i_7bpLKRnoZW9dqrnG0kC567ljVDhC4x00j9PZQxxoPLrGNUfH_6HnZW2rlYN-D5ELHyPyUYlcUx0gRc4ANCmcMk5svdgcHWpOT8NTrIr6n0nd9jN_kHYqYXNGkyw_sXWJSM79lhNIIV-JwJPQaHLGbXMAj_g1LNTrW5CBdRhMRaYwH6AFIzIbbS6po5hNC4DSxidiTY__95X4MRzcSB6AJVg8D77RSqKuE5Z6DFozICahv4iu2hnyHWuCrSlLqacmEIHS_fiTV61ySP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23590" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

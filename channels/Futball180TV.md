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
<img src="https://cdn4.telesco.pe/file/VMgGQxL6bhKehABhUIU8wDVruIKyQWqiGnqdqqRGGVG3kzH_lpok2_axE78H8lGXxf9elbnY3bdzSBWVIGi7tdmxJ4VXyT8HB-JdERodLGxpZBhS2hClsec_hTrX8vr_q75VACr8K27kWXKRMVHbt3JN7wokYvxL8MvXyn-eiYuMTZLhBp4yyYFXRuIgxwKBJx1ghayHbcUUCayKBEJP3Ie0PscF9iOB3geGmDOs6Hn-t1x2KGNcP2_XSkDM2tEdZUff2b3a2ggcPPOZp5QRcGDCuaBhBzNQepyXeZLEu5f-eHkD6CLRuNKqqEXjrqd5xGejLsimrSZWV0cHp_LKLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 135K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 04:50:21</div>
<hr>

<div class="tg-post" id="msg-89961">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CGFwp5-OHHr_BVe9xdvENccIedjoaYGHHpjohB_ii5ioFoGCFuSdVJVmqSMBJlRfdets3lvTAqnn_Bodv2-igjZnzyFwYUD2dXDTW_2FNl81H5T3dWGpmzwAoqzmgrQWk9nEMwCBjjvPTUC-LpEyN4DBlnmBYmc7VX2tBPQx_FQKulHKGlbMG9NU5Gp0_oR4hLFW2eoeY5bOvLrYUfPsGwmn8Cbr5Wa5YQKZzYXAuIEjlUr6_OXyrzxD_bGWslpJWvSkFLvT-g2dy2pZc6Vb47JzDCelJ-HKBeGuJDl599exEozqrTqSPyu6mTjUmXWNFp1nIf-j1PqWjCM63ZbSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 297 · <a href="https://t.me/Futball180TV/89961" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89960">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/Futball180TV/89960" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89959">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OUcI7dYsVnN1p_kO4OCAnvYDDHPTfph3OM8JRUpO1TdKLYJJ3h5kCxMvdl0T2XY4RXCOGRL_k_sKwQd3tu994k9FgdYqHoJ9sTxk_u_16fDXGFO9jf6K_1PHoFvvJDq-RQ4RB59v-DqV4G49HAUAdS8p04cO7-k1QLZyaBPg7wPbPqyijiTOv3UJ34Yk6h6SW7rRreYbcv_QpMRds-KU0S_OT2jRWGWTSPJbo7OCfb1QVw3gChVfK3rTrVDQKoyOGXr__NroC4J6jxncAv-4Vh26mDFMAlW2YAIeQHnOVxtc-jOE0phxtCXFyJ_QWDqqOEWN63ue0n027QqVWXWa3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/Futball180TV/89959" target="_blank">📅 01:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89958">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇨🇺
دولت‌کوبا با هشدار تمام شدن مخازن سوختی خود اعلام کرد که برق در سراسر این کشور تا مدتی نامشخص قطع خواهد بود و مردم این کشور در آستانه شورش قرار دارند
+کوبا کشوری‌ست که اخیرا ترامپ اعلام کرده بود سقوط سیستم حاکمیت‌ش بزودی رخ خواهد داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/89958" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89957">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=T72W5XcSaqFORrJtj1sh1uMQzDLjJiT80xVmP8EIb0e-_9aCuHfM2soh6Krx5eA16drLYL0CUvfF9v60kI0D0kBYAwps6NC40J9z7nk8LrImWhiinDldydp_bNToPiuTIwzizujNI07JMpfzMZGq-Q02BFd_pCsQoipvfj86v5y3W_eFFeYWgxhz83bWSGZn1MqrWYM3Ed8sFXlTIXziFjqKwNg79pdlw0QkiOoSV_SXgrmjavLhnoaKUCI7Sqcf_fIYcWuiB3js3d83ceXZAt1HNfi-1B3RlPK9kY5dESJmDqjKYTNCjmFxcGDznQllXu4Tlc0FLPy86D-HiE0i4pyd0PddFQM50DiDCfVAhAtjG7ymHx0cFBbz3fxfNwmO-u5yB66sJ9LoeXmnilBv4ZZ48IWHtLzyoGA_avpTERBCCLXCOSR1CR2ED4MXSq0FpVw1A90nBHgHEHEsSyYbBSMXROL16JJXWxUSwBDIrweCC9MJw9a4Lc_UWIU1XfS0i5J-aCFCTnsT19sbKA8NrY8AFnj4vVg8yZQ376pvelFM7BsSE3PhJ2o3yb6fCMGEL6Cw2CsM9SuCdTcY0YZMg2RLJ_6gwTbcz4RrTKnSz0oRG9Gs0rpvNCOxAvIZHvW8O7EBBdihmm8wPUodN3xkss6ekNPTVHpWJAG6jXT-9mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=T72W5XcSaqFORrJtj1sh1uMQzDLjJiT80xVmP8EIb0e-_9aCuHfM2soh6Krx5eA16drLYL0CUvfF9v60kI0D0kBYAwps6NC40J9z7nk8LrImWhiinDldydp_bNToPiuTIwzizujNI07JMpfzMZGq-Q02BFd_pCsQoipvfj86v5y3W_eFFeYWgxhz83bWSGZn1MqrWYM3Ed8sFXlTIXziFjqKwNg79pdlw0QkiOoSV_SXgrmjavLhnoaKUCI7Sqcf_fIYcWuiB3js3d83ceXZAt1HNfi-1B3RlPK9kY5dESJmDqjKYTNCjmFxcGDznQllXu4Tlc0FLPy86D-HiE0i4pyd0PddFQM50DiDCfVAhAtjG7ymHx0cFBbz3fxfNwmO-u5yB66sJ9LoeXmnilBv4ZZ48IWHtLzyoGA_avpTERBCCLXCOSR1CR2ED4MXSq0FpVw1A90nBHgHEHEsSyYbBSMXROL16JJXWxUSwBDIrweCC9MJw9a4Lc_UWIU1XfS0i5J-aCFCTnsT19sbKA8NrY8AFnj4vVg8yZQ376pvelFM7BsSE3PhJ2o3yb6fCMGEL6Cw2CsM9SuCdTcY0YZMg2RLJ_6gwTbcz4RrTKnSz0oRG9Gs0rpvNCOxAvIZHvW8O7EBBdihmm8wPUodN3xkss6ekNPTVHpWJAG6jXT-9mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت تلخ یک تولیدکننده در نشست ستاد تسهیل منطقه کاشان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/Futball180TV/89957" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89956">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRkED5l39QGv1D2viVo5_GFdfY16x-6vEPKD7I6oGGZ6eC2wvNfyKb9GjP4So-KAZTRvsCbpJikrCLPXGM7Sak_7Ew4YGvcCxLQIpPWT7DUDrP3TmP3uQbTZAYTYXW1D4UNxgKAoqscTMBXRghYmd6i6bliLu2fuGS8DD8BZGA3pvxASdaimI6k6zcSGg2WgB_li2o7-j6WlbwbUv2Gxd0oc8QTWJ4C5HmMYZ38pcBh_UQcgs8F7In--YYo9oo8CiJ2G0oQyAJVVvQFb9yttjXcWOxz_rgMfOiRxtet9wGLipMGwG4G7tp0KgeXzeTL60r_SGfHHAnGAJOEMFqSN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇪
فهرست تیم‌ملی سوئد برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/Futball180TV/89956" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89955">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKGwNxRcFg8flq7TDfeyu5JqCUIR3Bg8fHNMoADJkE4u19hfrRyo4KOYPEoM-urTP6Qya97J3liEpSvVZEybvgUx12qWUQPiEngh1udqX95AHluZZBq0DRc6fCs6yI79GApWLKsb2dPL9cr-A1u-vWlNKStdkip4vckPgp3aRxqyU29dIGCQ7oiYantENOGFj1IUZVuzMOHSq7mF1WkBSHCBcF_KYGh-PlOQlTF6XxohLykXNcrSV9sA14eUcgm7h2m4RbO7a4JUHEb5rF4jD0M_bYFG5xygtzI-pwrOGzPtWsaFVeI4nmf_nPThBieTpx_G-dsDM5Z5qf_0E8QiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست فرانسه برای جام جهانی بدون حضور کاماوینگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/Futball180TV/89955" target="_blank">📅 23:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=YwjwGmN4344XqPONy0enM32InlYEaD9aHnpcF5qlX-jHKVGxfSnON7Hbahwy7fCoOd7xXmO1ZTel7KybMy1cGXELAXGEKuj6HGqn05gNYfnJ1N_2qd9eNpAC7cd_wlR7E4Yd3Enm6efoYGeXFK463nhW1RKh590pGk8gEtPOQRvc6JESJOowIsOKpVwH5G2Ko5suQtr1wnwummdHdy_YzCPFr9pfEtjGyeLGvnn9679g_0StHNP-uKcFfcBvuiqBAJeCRGJ-5OhEV2yTKBTLxe-3_2ikRou2z9kdZ-7ZJudnIk0PMBlSAnp1rBD7XuFF2HoeeuEDxffyxNnS44CDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=YwjwGmN4344XqPONy0enM32InlYEaD9aHnpcF5qlX-jHKVGxfSnON7Hbahwy7fCoOd7xXmO1ZTel7KybMy1cGXELAXGEKuj6HGqn05gNYfnJ1N_2qd9eNpAC7cd_wlR7E4Yd3Enm6efoYGeXFK463nhW1RKh590pGk8gEtPOQRvc6JESJOowIsOKpVwH5G2Ko5suQtr1wnwummdHdy_YzCPFr9pfEtjGyeLGvnn9679g_0StHNP-uKcFfcBvuiqBAJeCRGJ-5OhEV2yTKBTLxe-3_2ikRou2z9kdZ-7ZJudnIk0PMBlSAnp1rBD7XuFF2HoeeuEDxffyxNnS44CDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاتس وزیر دفاع اسرائیل  :
ماموریت ما کامل نشده است.
ما برای احتمال اینکه ممکن است مجبور به اقدام دوباره شویم - شاید حتی به زودی - آماده‌ایم.
اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/Futball180TV/89954" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89953">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89953" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/Futball180TV/89953" target="_blank">📅 22:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89952">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koksjDYrRF7qd6yhqelZ7NohPffa7MG2enF7qJbxMB1S8XPY9p7YoOzIsMJ-M4s_6RTLB1AcStUJ9ia6ZA63CjDW03H2-ZaXp8kNo_-jZCar0kewJtCzMDppdzO7QJlEz53ZpdcQjybCqjkV_hYZ3k9-l8GQpQhTpyTj7V39KJcuHtJLKSbAMRplDLyJJnOXAazyhxnA0MLmHJpLBpcnVcvEodagiq5irsNo0IegI7on8ye_zCWI4AJk1aaZtXgryU7tjxn1objT7R6yntLiVIcaHOunpffMOwlMWQoIHqlAExYSkx5WwofU0b2hoAp8CTyBD4Fjf4Pxe8sHmg80Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی بدون ریسک بر مبارزه
Verhoeven
🥊
Usyk
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/Futball180TV/89952" target="_blank">📅 22:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7iNDEZHl02Bxdjas8JwI7nLWdvF2D6g4YQLrEsocGNTspU8gFmbqyKxxIf-OnFZMFDDPW6B-HOnvNvzxOCJCzbMLyms9RLQRUPR3tM6SRMlx0Q8YOlurVzh2pyZqXYTmhBA8G1m-2U37n0l-OHUEAon4EZJh7kPtoDTKYq3rb76puJxnYvESDpNUs3TRhQmgrAtiAFtVByguuG8iqCKZNMzYhf4DYXfud4Q90CRVnVs2Tuw_Vkh5j0S6hoowrS8VCTEM9YmyyV5jtcJlSWS0fcsArsYnjZ6kkmxiSuC6YqvZj_JAgtlvUBXdQ_3BFECi_WkhSNZBi0fqhAffMt2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
قرارداد آنجلوتی با برزیل تا 2030 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/89951" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5OsKhxtyWYIoH-AYFnP1saohpso6WvrJHzb5fEZnCWzNNX3fZEIIgpm_UBjg9MyZ-T6EPg5nfdKOKHbnxWKdz1z6epgUJnggJZIlF6mlbAvGup8-zyQsuLJwIQdr7NEF73id0wY33N7qSql0ptlCMYnr9ltxS2ZIWusz_QVg-XQSAYGMtbYxiY92aOSWXrGMKLN9K4SfgdFWY0HfT0NgbQ7Xgf6nN-X-i6de2kEenwOTBNIxfdto1_E6n9PHcDfaMFzNbOVXJZ0F4yOYiZ5lUvr-Hfpq_k03XgL1kxfTYsCL5TYTsDPt3m7HMXkILUBHAq7RwgZ1I5U73Cw5hEPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
فهرست‌ابتدایی کلمبیا برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/89950" target="_blank">📅 19:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🔵
یاسر‌آسانی در گفتگو با مدیران استقلال اعلام کرده که بلافاصله پس از پایان جنگ به ایران برمی‌گردد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/Futball180TV/89949" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMbBAjw1LQjAAQoz2o8WjOSoctmleMwLtRamQHZ9IKYeqdCxUi-aVaxnN45SHdyqMBQCf7538LELWstg1JDPjDYibmCzTPI13z23JC4QjeZYQq0fVQt3NYI3EMEUvq-fSbLDxPOI30gxbk2tqKetuWQXbmCJABf1FSeZWXmOS7MpJCElFRb8pjXvEk1oIV_8qe0UJSW8iqnPM-jJ5mFZW7J1Ow28kAaXh01J2V01st-I5DBH24kZYKrELIrfGatOVqtQB6X17hTBhyImKKV6JRlXzkbbIc7CPMq6gdROduI4ohHSvSMyOveRJCZp3QN3uGhDZOH0qUlda0SqqR-5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژائو پدرو ستاره تیم فوتبال چلسی هدف‌بعدی نقل‌وانتقالات بارسلونا در صورت عدم جذب آلوارز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/Futball180TV/89948" target="_blank">📅 19:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=hXJW-Zpx-K_K_eZo2x8YfQU4iIRKRhFzzB7l-nXVQ7ppvW53e-fWBHeNKaorfG9qUsm69Sf_-5YXsq6OfbZ--aRqCgkvYV4CVW_i_RTRJ-NltQywrdCL2olUiSZlbL_93DTBlbHexShf3h6I6U_5ycP5DqxJvU_bIofIyZxs1siujvMF5_o723mj3FzFFRyfkAd7Bft9q0HHWxKB1jRsaE_sHy7EmFOleNRnmRkfTkleuXlPRVyyagIu_3VxaDOJn0j4a_aRJPI-bVMCKN8h_e6QPwEfsjchFVZNHGc17NOyiYitIHGwFUwPSIBGeTDoBynHk2TccxvM0UvSFyd1ooO9fLp0x4C_JKOcCYiBEC8alCx2zGPF2dCaFeYVgh3IxdC4WIc-iS50dEY0edAYnAkLfK6uEbrupOjkRQs_16qyBH4kgGGsAd3uYT55vRPmRy4GB3sSGPDqusvjQZNGVj_IzhzQGAH3maYmdYoq5up__NPqHpQM5vslZ1mXOjw-dnsVShEhrXgc0BBkEjA65rcdtdpkVgzbpXbJyjKvPyYqT7TcWzop3peq2kayh-GydmPuiliKubdf2Jl-IVLq8RTyEhvhKzzxWEyorL9BapZCuQICPFgRa8DE0PaDqILcjeLbD1XcrjwmiTZf4IpFSfzzgvWPGpThRRoZMVbP-GY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=hXJW-Zpx-K_K_eZo2x8YfQU4iIRKRhFzzB7l-nXVQ7ppvW53e-fWBHeNKaorfG9qUsm69Sf_-5YXsq6OfbZ--aRqCgkvYV4CVW_i_RTRJ-NltQywrdCL2olUiSZlbL_93DTBlbHexShf3h6I6U_5ycP5DqxJvU_bIofIyZxs1siujvMF5_o723mj3FzFFRyfkAd7Bft9q0HHWxKB1jRsaE_sHy7EmFOleNRnmRkfTkleuXlPRVyyagIu_3VxaDOJn0j4a_aRJPI-bVMCKN8h_e6QPwEfsjchFVZNHGc17NOyiYitIHGwFUwPSIBGeTDoBynHk2TccxvM0UvSFyd1ooO9fLp0x4C_JKOcCYiBEC8alCx2zGPF2dCaFeYVgh3IxdC4WIc-iS50dEY0edAYnAkLfK6uEbrupOjkRQs_16qyBH4kgGGsAd3uYT55vRPmRy4GB3sSGPDqusvjQZNGVj_IzhzQGAH3maYmdYoq5up__NPqHpQM5vslZ1mXOjw-dnsVShEhrXgc0BBkEjA65rcdtdpkVgzbpXbJyjKvPyYqT7TcWzop3peq2kayh-GydmPuiliKubdf2Jl-IVLq8RTyEhvhKzzxWEyorL9BapZCuQICPFgRa8DE0PaDqILcjeLbD1XcrjwmiTZf4IpFSfzzgvWPGpThRRoZMVbP-GY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ستاره روی لوگو فقط برای قهرمانی آسیاست؛
تاجرنیا: لیگ برگزار نشود، قهرمانی حق استقلال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/89947" target="_blank">📅 17:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQJqQRR2IL7TRFILrPSqok27xWNAzeYQb2oT1MvC8CgaW3c7GyNaQSEas6lziQgrIt1y52TuZN_Kc_TGD0TYTHUvmNmvUvxkhId4lG4Gxc-D0Tl7XyZ8lT-qCKC7-qfWAsrPshZrrTOeAQW_180FqtOegFvHs25cA_CNmLPWfBHw1pPANdMO3xJolFpMhYOvuYomcems0cgXIeJzB3JD5QBvjPZBI4mKquLqoYc1PNl-hoMNC_qmwQcZYN_Rqn18fOm5wCkSNa3Vp6Q4Hn8-FX9-f_Nbf1Xunz7diri81gGzf-LetPsORY-2cI2TtesIkPKo0vwdWyFgW2XM-kQFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای کسب‌عنوان بهترین بازیکن فصل لیگ‌برتر انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89946" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89945">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89945" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/89945" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izKnaI8-pQeeu_dx82AY_78hVOXBsqjVxKx9-jX7jL7R_10TtNE9uIfPq1-48y6CyLzTzqqm-N2PELORFDIPSR56xhcRZCfveKe1FbkJttrLBjSufWZGiEPCXwncLMe4zlXgpbPnexp_TK17TRyBFOQNmng-Amv_PzArePZ5-yl3idYr5oYgR4xmd5QE-4iPrJMbVQBCsupM-cYYEWkvmCmhGekLvnCoHfTiFiBTEKROdAVb8lLBLrA0FDEZ8AoxnMzMbomFHZvhN_d175eVc6YkMAYkfw06k4V_h-1DvcJE6CKj2KYzM3JbJHZ3fIlEF9sSv0Bz1byigre8m1t7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتیجه بازی جذاب
🔵
منچستر سیتی  - برنتفورد
🔴
را در 1XBET پیش‌بینی کنید.
🌐
بالاترین ضریب ها را در 1XBET پیش‌بینی کنید.
💎
گستره ی وسیع از گزینه های قابل پیش بینی (قبل از شروع بازی و هم زمان با پخش زنده مسابقات)
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/89944" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=H6UIYBI5HD_BmVZrTpFVzfmWfaMulK1ywYTZN4FKb0fRMz30kCqa9-EUXdycoDTFOXXHx8E01E2HPVc9_r3X_kXED-B1cAyWy_nyqAxoJGIoBhRikD4wGlrREsv6ntRQsA4eLRtNMtd2pupUYn6t6Qcnt6LpHR-PmuUnS8oxBmkV85wh1TTqWqcemac3mrapQez_wW8sY7jLCRcdGAgxsdRzMFcyUK0H_u6euaiTzDH0SqRwQMBBAtir16VEEaZuooQJjZF4ktYo2GFoQRQGmhmuDSLGHpr07sNwBhbhwXmqLIub9l2RCdVIatQh_NtVWaSqrzPBxHSFuC5VIxluHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=H6UIYBI5HD_BmVZrTpFVzfmWfaMulK1ywYTZN4FKb0fRMz30kCqa9-EUXdycoDTFOXXHx8E01E2HPVc9_r3X_kXED-B1cAyWy_nyqAxoJGIoBhRikD4wGlrREsv6ntRQsA4eLRtNMtd2pupUYn6t6Qcnt6LpHR-PmuUnS8oxBmkV85wh1TTqWqcemac3mrapQez_wW8sY7jLCRcdGAgxsdRzMFcyUK0H_u6euaiTzDH0SqRwQMBBAtir16VEEaZuooQJjZF4ktYo2GFoQRQGmhmuDSLGHpr07sNwBhbhwXmqLIub9l2RCdVIatQh_NtVWaSqrzPBxHSFuC5VIxluHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/Futball180TV/89943" target="_blank">📅 12:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF1G3YxvcmPNpL6GRRRMS4IooRjuQIAbTzxkGZYHfuO0KG480YNp7imY0LmHBwTFaq-zIWtWx3EmNKaY894QEcpWYOrx4079yTb76iHXxsQ-M3DRkv10Fv6yIdU8F85Pa5N7iw7D1OAMtckoe05IewnRlILZwp8p8t199_t-izTdGgqLuaTrZ-VMO4DBQZG2jQi7b5WTeeENwJwWlT55V1WtpRmTQo8v4fVlvzowtgiH18KHV55RbQBXj6rh1Kn9c-5aZ7H0uXNmnojRsmw_y1mezQQtf4EJhvp8Dkjnqam5REYTwvuAk6_mrVAtsJPRzsPe6bXT8pQDiK_r2ariBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژابی‌آلونسو به چلسی
🔜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89942" target="_blank">📅 12:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fru36ND6T1Cs3efdRRJ-NY9L4MkL19wmgMD1DVsBEhRdVP_MZHJYyEuoOdrW9bu_c0_IJGIwkBcceH5voRhOct6DRk7gI78C-2mcL8KCjMFs0gW26WbPJtoLgqErmcw6-ZlKDiSQ07TJZM5CBamaDnbVe80zdBBqcbX78ejerzQKQ0tjdIwNj0OhlsudGl5OII4DEeyFvJXfhy2k9ocOokni1MZk_h7yu7urSm9hePJrllGnE_SXvc6GnnmrUq4IBD0KcmNx-E6LPGzXbotv0PE8Uj8iBJdqqMiBr63b1Ucj_n2ITlCIVMaJlAKGzWcVU5FN_1PEfQLbAB-oLqWaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی از کیت اول فصل‌آینده منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/Futball180TV/89941" target="_blank">📅 12:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvujH9Jq61qOUcbaN0h3YzFe4uP3hsNaHEwAh-l5bTUBt9Gqs2CtgOVxcWhVLtmMJN1AZeDBVyVkpsK6WpZaRVov8-DbvkWXAssy2TpN5XaVIKivPX4rmSNx8zxg4R1_371qu5uynoRnfUxkeU-jW-YcQAhEoD0kuCES4B0Yanq8dwIavEtZzioe0xFS-1tKf1mwZeXrBAj7VstYv_zq_nERs9tE5rwzlm9d9TBU4iOhxqm60No6wtYsYuyx5sqgBORRbfkEkNyM01JZOugA4Yk8uASbme08KrtTSjqkPnDYyvdbQHp3Azoo939G8uSvKbpRUI8EN9RcNCaseWcD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام فیفا، در بین نیمه بازی فینال جام‌جهانی، شکیرا، مادونا و گروه BTS اجرا خواهند کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/89940" target="_blank">📅 11:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZuP4t1r4QcxVYuPf2lbo0-_7US3Qsw-Elj5yVyn-icyIijrx6vzdt5Vw9u407SAyZyXDZMj7mcs5CT5hSgXwjlOsHPKHqhWt1gIzPqgRI_zg-YT49WGND0agvCufiJJQXfwBih1gXzURoh5hmCCWPSA5QgGSHx3osWdivaDV0h5VHtIMwRWJ__e3DWKCL3ovd7yZc9iOsadb3ETN9ATiPYZ0UOLUpOkjD7cwDVa5i9GZkhFSEYBVcOLzUpNvRS6hEWiL94G0Js1Bjkra5-npDgg25iDekEcDqCmdrMM3iDEjo30d2Z7gOmrgN3Hx183BwqzoCE3iiiV1SWuAYHf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام لیست نهایی بازیکنان تیم ملی نیوزیلند، یکی از رقبای ایران برای جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/Futball180TV/89939" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf-rbjOePQ5XCaZCpRo_NvGbcfZEvslFyzOhbi3wmZ0dHi0Dba-a7zBOMh8jAMDktm2VeEZ3Jx976Lnrc8VMmbtIP2JVroxoc9na3Bos5udiYxbcXilxXI1Mryy2LUXIIwOs0vdA0-M54hN9L-XGCq-0uSwqUIQnPujP4TXmDDiMy4E6p-CFpiiSTJU-17Un51OR4wjx26i4u8qt0T9wJu5m6gD3Gnf9_5QpZ_SggvnvjVcFXDN3WQiGzke9WMmfsAz2OCc94nLpXTv-V_0Y2aLffk0QK1Q_QnVelExvP4AlH1y5xQXGrjjjs3cqdm2aFlKj1tyxg9kmiLjoeIBcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نصرالله معین خبر خواندن سرود برای تیم جمهوری اسلامی را تکذیب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/89938" target="_blank">📅 08:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89937">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/89937" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89936">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHoI0ENRYsc-zh20r0h7FuWIeRcGJUjAZDW0UBXNFoEgQC0kUhr497BKMpv5MDijTEGADbMcgJul9Oa6xU8a7r5CuC-C3kyigx5IH4BRa_sMPG_RGCcbNgV3gZ3qXrA7YI94koeAxK886OZQd47X0cEGjVaRGN8oRnnfomG5p9nYz04FtuZRpJLYqLIzqYDi2vmagJAl4k5ZS_IpbKGFamgtn0IudqiyihjwqUW24HDRk5N6Zzg1PbxucX_TlhkDRYr0SrGxOcYXyL7qXhw3iB_IumdVbVsmK8Ed-WIzGyROvNxVte_YwOOkDrzslJsHkQXnMpZdPFKhPQp7ylenIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/89936" target="_blank">📅 00:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYnV_v19oz8VD32QP6Rn1nZ9uZ_HlU9XK-gJmxlSw7eMZWfDrLLjkFscqRuK3gVH-cgbfx2zDO1b-w-RU1l4XatupcNqDnGDJhyVMXDIzaIVVDD9q5eRQnsOd9EXv-TOmR-WCZpNo6DmpRPLFkA8xlmT9ytXkL9qUmLP8Id2JNleXLJUvjxDnwvAoMBiwddc37pa70amzCCCjNIYOkAwES_3PJ1sIoa9NaH_CWGHCEtF0bTddr4-lm6zIoG3XyuxYDktPHdufb9bMf974S9F8wEbghx3lcQp4Tixvf3_szfflxUffQOz96UiLDSi2ckUVsJRHWTN5Ai8qbpoPMCcQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇫🇷
پاری‌سن‌ژرمن قهرمان لیگ‌فرانسه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89935" target="_blank">📅 00:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A94Z5grfOg1TTDo7KLvoqqsB0xCTptOaKi-6MRV1G144K3ulJK2TtlP9mnNRS62wpp7BVJrbge8SeFc8jlCCxyBlx2f0utenxIr7McJcf81DNVyv7-Az_TCHhwpnddpPtaal-ShrGwHfT-LFEbIka0xcjJXNO9cgdTBJaGyMDZQ1WyqGhRNizMVblMJm_nVHcGgiNx6VO_lt34ZHUO_rziXWCRTWA05OVvkhzekp002RC_gNKoa1Y8OBYs3IH57PBvCC22Kx1e2B4w_T6y8c4z4UxhI0I6Sx8nNU33PI0PIuYjBNNx0WeH-k-d8XeeiNiGA1SyaKb37c4yZbW63LEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
اینتر با برتری دو بر صفر مقابل لاتزیو قهرمان کوپا ایتالیا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/Futball180TV/89934" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgavsypA8hjXDwIw3we2j8W3EDI-R2tfLL8JHp0kS_-pDjmGbtRQcFqfR73vi6lJvIU6ky2hTwgqORxAM2rpTBFHuUAcwkHNdRtCB3FO874ZVbqFGO_WNIV9Hua4YgubsA0CoV5HaLN4qz51jcw_jKwHX1ZJDOBs6rvd17znle8Wau9kZB7G_ib2HZUbuh-bTJvoyL_xbD03J7Y5wx40udE2qb7KfExNzNYH8BXrB1MM1IjiT3WMdGl3Px0Tf9GufXz0F9y1lKW_izFoWeZ5K0_nkUBIku-sCHKH8JiRZpykZmjy0sT_Mbzknk6dEMIz0ldb-DBdBeIBq5SRM-yt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مایکل اولیسه به نخستین بازیکن بوندسلیگا از زمان جیدون سانچو تبدیل شد که در یک فصل بیش از ۱۵ گل و پاس گل به ثبت رسانده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/89933" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoh6rsJIEZ3zOI8H9H56dKDIKU13y1eQmX2lV3hTghRevvwInqcLmhS8jylokl8fzgq18q0qs-uw6rg7gU2F0YpKkbNtbyI9aHEgIItef_T8R3PwU3meJW0F594g22mc2FkMGcRzePXcAhLjTjzfFLKekB9uWnLVUNlILekHIEBj6D9iM10jDyyG2a-W2-pUj4bi4dRSihtSQIx6QRVLEEepZqSXwJDs1cANxOpL22YOcTsx2cb72RGIPwInz3ZUDkwJ-Ka8FYHQ3ekY563DCzEU3sU6J_CLicC6_AMVoRg-1EOf2xCF1qoy8ViN6jh44R4xdtSk9sWAjifg5hjM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار و عملکرد مارکوس رشفورد در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/Futball180TV/89932" target="_blank">📅 20:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89931">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/89931" target="_blank">📅 20:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89930">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY-_PaQu7pyq6oKLsrjyxkE1CvrqNZjzMGiDlC_RCQ1r7RWLYbGjBSeqE753lngq3E9YLdd1gSY7RA6xMaomakB50S_fgaZHA7loWuInpZWGdwi92m4vssl19NWG0NTarX2phy4o5eQRaYQE9b9MOBoz1-p7INWu615yBcLNKRDNrVkQNs3aUVQx5FDd583ObutwCX-5dOxsLpBHoTPmJgYvYNSjtbEXiY1fFuJ7A5ChpjHHXUHAVenwzPV-f-WtpsS4L4m_SzeV7HSRj5Kg8DAwD5kgpZXZ1dcnLHaKGZ5TqKN-Xzz5ZT1Z845K2vZRiVhV_w6OQVSMLUewvkQ8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی بدون ریسک بر مبارزه
Verhoeven
🥊
Usyk
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/Futball180TV/89930" target="_blank">📅 20:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
باشگاه سلانگور قهرمان فوتبال مالزی با ارائه پیشنهادی خواستار جذب یاسر‌آسانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/89929" target="_blank">📅 17:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxZE5nlAX0kZq-ngOGczpMvZBQFagaUqfuGSvMEVBHk3pKUcrGJWX8fz2f3ElwimnUhh7OTqji0HiaVq_U_uO_Q7QRcXVaR8mGRls_61W8YGtQLiK3jqKP8jQMhQuecI35NLiUGuiq3koWKC6cRI68urX7B5QtFkrZKC3fSU_MokEahEmqrGcfnsvgAmYCGyKUjP9xFC-vCFbH5ovUrNOkeDxiGfbACwZzkGPfvv4BLMXethtI9EAxRRDrAOvhLePKeLbFqW-3tM62SZd4Lb6ARtsX0-dVN3_vR3k1xGgS9LK134_v41jKoQ9NlobeajZ1GTCXGFntHeAACU5cSzlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
اتلتیکومادرید پیشنهاد تمدید قرارداد با افزایش دستمزد به آلوارز ارائه داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89928" target="_blank">📅 15:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOOo3Uw_DUZJwIpSpOy4KABuuH7UWP2qAffzVkF4VDokLEEBsoRE5cT3laxUhZ_uZaZf7j9qG_dRHvRv04vFkictwPVIBx6L9upUcIEHBPK7eP52uMpzYq4l89BPWvFKOCPjeSdGqTdS4CC-2lojIAN2EzbKb-GRLkjkk_PAakzoZNAjx58hStU7Vp-pFS5Z0OQ72YLbigL81XovNLvFTPTMHf5kUCLnlM4X1l3MxsS_ezoaklNd8Z_Vt9C5GD_eMSg9Yjz5Lxv2P1u2nmrfwzdwAm_46WXiKDYClO1KvGti1k-TYGMXMlkli4Gl9QuVri0-Ks-HZyfIJhaZCZBZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
باشگاه بایرن‌مونیخ درحال تکمیل قرارداد با آنتونی گوردون ستاره نیوکاسل برای فصل بعد است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/89927" target="_blank">📅 13:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=sEwH6fx8jIYr0MjT66Pth_RO08H7pAF_6VcabKR8Q_RKSKyor_tlmt_yVMQx-jNhyBfQaaT1Jj6hg5TLMY727tT6SefJo_K_Z7IcPGuVXrqKByYcRlsL5bomVclQeFT9-zHy50lhklQ72iwRwZOTOI78VKls9pcK-anD1hjYp-mWTb_MNmcPFp2fOwSt-to6p3EdlQVSQhxYfh0cDJ-JKuGRhB1AK0ui5tzeQvPyEwkXL12j4BqdoXdbKyPQXSiu_MXHlWPFgezEUKuzaqPdKrNcGmrZfvlppTRtCHlAX0kvCqyxPsyCXdwUjCBgzCHKEET_AG2IlJieWc9j6YFsSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=sEwH6fx8jIYr0MjT66Pth_RO08H7pAF_6VcabKR8Q_RKSKyor_tlmt_yVMQx-jNhyBfQaaT1Jj6hg5TLMY727tT6SefJo_K_Z7IcPGuVXrqKByYcRlsL5bomVclQeFT9-zHy50lhklQ72iwRwZOTOI78VKls9pcK-anD1hjYp-mWTb_MNmcPFp2fOwSt-to6p3EdlQVSQhxYfh0cDJ-JKuGRhB1AK0ui5tzeQvPyEwkXL12j4BqdoXdbKyPQXSiu_MXHlWPFgezEUKuzaqPdKrNcGmrZfvlppTRtCHlAX0kvCqyxPsyCXdwUjCBgzCHKEET_AG2IlJieWc9j6YFsSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در ایام‌آتش‌بس درحال بازی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89926" target="_blank">📅 13:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfkGL1s_MXDJY9c3444LaF1d072vrGrWr1gKUTGO6KKpEz6bfq_3qHxV_ww4VVjxkRWBvA7eF7ITS3NbOsHzy3IbHH-LwoVreWMgmJNZ9vwdWW5EuKRCd-121NcenS0Rsf68QZUksaiieY9oEl4dzboovnPCp0-bfBoembJKK-B2Y5yOBWVLK1fXyEDrEDvDxjjWqE3Q8IAQp3zkx3V00gwAvuBjW5_0jqghekrNil6Rahtey4sGetBcTxYcXSGrxDR1NiQmZ3xo1naOLe9Gcz8k_usjFDPBYcVo7bduUF2deEI6wUvu5yvbIhhSDfp1zg8drCond8YIoVQSrNvAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
برخلاف اخبار منتشر شده، رئال تا این لحظه اقدامی برای جذب رودری نداشته و این بازیکن بزودی قراردادش با منچسترسیتی تمدید می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/89925" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeyD67d9b6MjB6jRSqNOtlvYn5WB2uvoN6fdjLWkKduTocCvIt1-1KD0BlKEHjJ1mGmNszHj0kpr_5UKSSozDs4lhxdMJDoPfvq0KFcoBnFkP-g6ahmuM3BF5aX9M_L3_mLUexIqP0HmiF_6hAXkCeh-qbqkA89GOFR1vNM_fAVFnwq53WKqasEbCN8DhI7Nh7ecYZsbw2n0Lva4z5U1VMW6gJIXmtg6zhWynt9-x5gFWypqZttyg6Fx7Fq6F7Umuzk5G5KHhNmDv6ZE-lStSP855JrLCYbGy3-zS_n1KUjheCUfnDtn0P7kxZ4Z1EfRvGsC3EzaHsp0Z1I55NS8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
یک خبرنگار مطرح لهستانی در خبری فوری اعلام کرد رابرت لواندوفسکی پایان فصل از بارسا رفتنی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/89924" target="_blank">📅 12:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzRp5WlPaGvK52VAzFOMfm8ZgEgM5yqkyfBecyf1cQfV8QsADgjUmmZbQXwFqjmgd0Y6Ylb21f9Zqq7qZ8AjBQE5Vwg2VreIildkf64EWmMToSO5JoWOBt0btpN6RNPoIwQz1gY9MqegC8Yo7EbFzoc6vE_r0WFnBauLoq1F6HHblTW7X-qepnyFtU40MiDm2FPM7NKChyqNMJ1mqcubBjOIdg3aaolnT7_uj25avNRyN0ef5mW1BmZVWK9VpuPOMbyiHb_jTi6jSByDnn6VlHpqAcQ0Cr_NkbUAxMjC41nRKxafuPJt1XRv8CyCmNmLo0C8Zw8uUBBDyQX7YWaoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: قرارداد مانوئل نویر با بایرن‌مونیخ تا ژوئن سال 2027 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/89923" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggHhLijzrEQu3kEWNg0P1jBckDpybQnxag-YgKft4rtkoeppIXqGUFWVRHSSjuDZ-3KDOdtVDdvHW4y-CDuNzMu2RCV93ZPpJolvmI6870QcOwcgzpbEszStiwEZ470gvG-BTFcG5u2KnsQEz5pbu1N-oWOKP66VQ5AfZx0DqTJ5hTr8k6ZfKGDI2iAaSUir3tajplaJ369znAORCA1F7D-r2Mg-gMUNTwrhMSJZv7xOM24dgWROsLiKwxy1uLTPIHHFKolOlH-SjtDDI5SpCv1HNwkh9IYY_DZJSzYOM2hhKohOREGjAL-a08PKF-1uxO2d_hCt7aBD2bBD0A4zjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قصد دارد برای جذب فده والورده از رئال‌مادرید اقدام کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/89922" target="_blank">📅 12:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uELcb6__gYZPvmZGYxSQbeLfX5DPmuxV5PaFp5YKjvBhtZL9ewZd5coCF-y5gAH1zBYWE_R4Wuk6J-fVGuBFNSjCVfYT_3RMg2tmATtglSaWr9wizpKRQIKCWFvAvcmF1PfeRcvYZJ5UCBvKLSoEvOic1chtMH5tZzZbYp97Ei_pQy7hwtdTdAtjhGfSNXkJmnSXcfRk5eTfnO_APk-399qp0qGWa7olhJOW0Afd1n_fgy8ov360NeY78_0lrqv34a6R8g_QGaaKJul6DiTe2k5FnuKL1gaJ4aFpG26N10QaMCPczk5PrPLB8tejgV4qu4Fzm4Otlgz3uk4Yo5C3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
فهرست اولیه تیم ملی بلژیک برای جام جهانی ٢٠٢۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89921" target="_blank">📅 12:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axZx4c1RNsv98CNeHjbzQgx0pPxzJSWJ7a1grp8eC0LD7Um1Ozp_ZTY_O0VOqJ4zNJEY9QE6qYpTwX5sONeoPF2LvJpQMe5LS3BKCoO_oxqw6ukaJt4itRzdUUbuVJsr9pENBbBkVj1MyyVlTL7BDAnpNDU9ZMI-oR0PzQ6I970ThM6dwN9J3pUbihCSXshH2x5EabfXMntujdRC6HQ859tFskGBdrNfZXrGIZY3OIwM703ev7eieLPz0fJQM3MYZ1oOlgw2HkDKzwmU9tJk7kmjXUd8-fnQyarPxWmB7KfzLKH28_QwwzIFOORsdEHfhTJuxl5-7t5lX-XWKpBEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پی اس جی مذاکره با اتلتیکو برای جذب آلوارز رو شروع کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/Futball180TV/89920" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89919" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/Futball180TV/89919" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erMa6UIqQ6_K-AcY7yBvJ3iw3l4_ilUiKMF3mkVuYVuSgloD3rVzPBbPx-aJXkywXeIncYUvP_DBp2J_KPdBOXEtqJ-dBbhOtg_8s4alIZ-8dbw2AR1Z8B8Dyic5F77ZkXBTKwNqrfbKSP2mpFVyXBR31hTsCRa_Z91SbfUCJlXgMGwN8s-cl4qbxvp2demnQVbPuQmJn2BGDEJMHf-LLgAO42_UyfTUp52C2Z-eNQNCN6FuoMD004m43EZ5-2-M5hqT0ZVwCfKnwFFUosdTqrzs4H7fkj4v1_N2LEAKFvYg6dHXivSoZKBb3yDtSRgf7pS0mleH-IEA4gaO_B3DWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/Futball180TV/89918" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
آمریکا برای جام جهانی به پنج بازیکن تیم ملی عراق ویزا نداده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/89917" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89916">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=KlfNkK8-8KEITIs0Vt_EJRXSjexvMRlriRzW-x3Ci2RX6UTAExzmkaStRu_jWUt1Lp8MtKcX5dBIxGCP8tarT66lD9Hdv_E_5o8foJMvs5o_i55Snl9QJIVS-DSOVR9AVB7l0YVynVckfxdaftgW-NFYEeX8vJ8O0OIEPM_bIGh5nI1RcOX2qYL78-bCFfNiFSlbSUxXgW4tde5MWUUqvK6jxtIBtCAKrSicdShb-KPa-1c2SxG4y1_MSlNtRZhQtj77A4d675dQEV6obPThU2ufTzvmZLXJA_0vLvksfzNiBNQO_zML_5uDTe11-PANPAl2Icf8ejIlEUGD3rQ6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=KlfNkK8-8KEITIs0Vt_EJRXSjexvMRlriRzW-x3Ci2RX6UTAExzmkaStRu_jWUt1Lp8MtKcX5dBIxGCP8tarT66lD9Hdv_E_5o8foJMvs5o_i55Snl9QJIVS-DSOVR9AVB7l0YVynVckfxdaftgW-NFYEeX8vJ8O0OIEPM_bIGh5nI1RcOX2qYL78-bCFfNiFSlbSUxXgW4tde5MWUUqvK6jxtIBtCAKrSicdShb-KPa-1c2SxG4y1_MSlNtRZhQtj77A4d675dQEV6obPThU2ufTzvmZLXJA_0vLvksfzNiBNQO_zML_5uDTe11-PANPAl2Icf8ejIlEUGD3rQ6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درگیری هواداران الهلال روی سکوها در دیدار شب گذشته الهلال مقابل النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/Futball180TV/89916" target="_blank">📅 11:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89915">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJzwCFTdhiZNg8BQv2STimQ2jrWVefQbUDTY3cphLnngDbtqwhN7Pezd59AzL1Si3aYlYkeZddcBUGzN5ACOzfwwJ2xwbcmx5INv-kWv8Zuimy8gP2mAzhfDUKd3fbBMuQv3scUKdd794T4pvpeZzKdO-u8PhyXaVHpdOELllbElm4MIIU7J1g61qGEH8UQNagMyOuLrLswZ3htUc1k5H7kpC5jS5hZVxV2dpXxcyzbyzIlZ6ht6BDchdYVRqrfTRNIbmwzH_snKKS_DH3zOjrPA_Sew704OBsQGR_yR7tISrOlTVC9EFg0FHQf2_pMd38zE1AnDBBA7LaVTLw3elw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با برد ۲-۱ مقابل الچه، رئال بتیس موفق شد بعد از حدود ۲۰ سال غیبت، جواز حضور در لیگ قهرمانان اروپا فصل بعد را بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89915" target="_blank">📅 09:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89912">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حمله پرز به بارسا:
پرونده نیگررا بدترین رسوایی در تاریخ فوتبال است. باورم نمی‌شود که هنوز حل نشده است. داوران همان دوره نیگررا هنوز قضاوت می‌کنند. آنها هنوز بازی‌ها را مدیریت می‌کنند. این غیرقابل باور است. بارسلونا برای خدمات نیگررا به مدت دو دهه پول پرداخت کرده است و این داوران هنوز در دهه سوم قضاوت می‌کنند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/89912" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
پرز: رئال‌مادرید مشهورترین باشگاه دنیا است و سایر مسائل خنده داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/89911" target="_blank">📅 19:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89910">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
پرز: با هیئت‌مدیره فعلی در انتخابات شرکت میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/89910" target="_blank">📅 19:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89909">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
پرز: دوران ریاست من بجز امسال با کسب ۷۶ جام همراه بوده. هرگز فراموش نکنید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/89909" target="_blank">📅 19:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
پرز: مثل سگ صبح تا شب کار میکنم(جدی)
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/89908" target="_blank">📅 19:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
پرز درخواست برگزاری انتخابات رئال مادريد رو سه سال زودتر اعلام کرد
دوره فعلی حضور پرز تا ۲۰۲۹ هست ولی او برای نشون دادن اقتدار خودش امسال انتخابات برگزار میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/89907" target="_blank">📅 19:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
پرز: متاسفانه استعفا نخواهم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/89906" target="_blank">📅 19:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89905">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/89905" target="_blank">📅 19:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89904">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNKRX6gG8l_tQjDqT753yXYve1yW4O-s6vHRzxCiX1qhREh2cKv9T_HN-d5TaTOZsW_g2GLuhfaX5D6Uur3GkXo67aY4VgPmJfteT-_F7OPnfz8A5QjxwfJ4aPeAiMRwmg7X-1CXpF1Hy8HG0dgn_rUhgT71u24IN3qdQiRhPyOq7USj0VDGA9lmJaLt0o8hDd88FlANmKxAzYdXR3PxSZtAtHodh7BibAODjalrYelDud91R74ze7MhHZPxjQi-I5O83cMNlTMEtBg4-L_SXvde3EWjSZt_3FzKCBPG1w24NrcJLST3ile_rxm-mViBxB26_u7q0rv9bVq1uX52CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/89904" target="_blank">📅 19:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89903">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPwrBV_bP_JHfxASCtqFLlfXJZOm5R7HQ6Axw4Rhrxt4iyXdxBXxElXoHFKpi5hvontbo_qBkFrUo4C4cPTmV93_X73mbh_aINr6euX8O1wjO34VdfErSPHgwjJkfPwGu9rlr1o4UNrBjlNWOPh8IfUQ_ufC_zoVydQuZcdqLcDsqo2ZKJcomF6RkJlbTS1v9Bx_n5CtVRR4qLz5eDzFsxnxZ1pwKZHavk_R_eJzomce31UOwQeTkXzsgJ5lZtTLPK8e_2SLtFOcHKV_Y1ZnJAB_1B1UMFSpU72obeVjhu60YKJZHHn3sPVOzKsz7cl4lvkJFCbSiQgl-LN8ryklMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو راموس باشگاه سویا را خرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/89903" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89902">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB2cGkX3S2WhVa7fW6YxIbhjOhr5JTfWLH78hujSmeRTJklI39vt3m5xP0p3zxYlnsxEzfa1xoCRztSLc5k3mKInv38kuaZtP9qa9xUfmI5EtTCUBFdceTnV_oK8LpdUGLNeFiIfukG6EI_PVFSlFbciBNhcJvMAXc61xy0dxlnjwKasgrbtjPqaAudoQ9ossfPVbmqyUz8fACd9q9NXtfw29pQTTjDAmjhCDzRPY89b5_8Az1tG-r6B2MgAHy4sV2YdA6TYbpUkWtWIKVzrIUK8a5WmjW8IS4RGYF_tkQ3f6tWNAUNX39Vw823mojhuyu1V9OqiMj9WdRc2BV2tew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
لیست اولیه قطر برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/89902" target="_blank">📅 13:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89901">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqTiebO8rYdwq34IWGVjFZJo7RQbzL9BbmcOZT725mj2d9x0zKlAvjjV3f0NWe87wzdDRAqhGXzhsnMVjeL2txuQdR7iwKcHgKwsSY82fYZGXTCgXtH_sZ7fMIJpvWIVkuHt_RUuGDIRj9qyYD7eEcJSPTcwKiPcV55qyqdp37bj79BVMfNhggODuISgqU_q--2QafID3DY4vyZJFAYlL_o_TEvagPDWC2nVTH5lztVxxOSopJrF9Mivnasj-35KtdxNK77o6xsYeB7IF-HjnV5510S9rFVI1IqB0BMP8Mc2oPOgtW8vqxoSfQEVd2RlF_PVzFdhSzZma7BVdbb9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
پیراهن اول یوونتوس در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/89901" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89900">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf4tzJXbHemhF05ygAYF6_eOBmnTbUCwh2NFwcB01yuQKyt9q3KVfolIPQBN1P8F8JnT1RR6MygWmXM4AcOzDBrn_4QSm8CBVYZvj4n8cQkBKKPihYTLfkfTH7HOXPVQWd-srjBeSXRI80HItUvBHBJQ-1pKRUsZWt-mRvGdj6-tahSKVP7zKCWlisy3Gyx5kgBGDQjxSYXN4Ezwgx0so-7W9K6TCkGydjguZ6gHW8KDKpEokhtbryI-UYqA_Ur_UkX8yZKhHoorWxZf6TOUaUDRJXJHNfMz7brfCy60scXNiqL48EMfBL9tvAM3-0MafkS8-mIAgQae_54_MDF4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89900" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89897">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd2Gy3MzBt-63ZTODY1qdr5VDW0fSsOxJvqhF-8Q4nVcmZ4CIllmzhnpavbcyFoi_9YS3c9TnmURbc1XVA-ZBTXMacdOXrK3Emk0uVIzzp3aslWT2t0RbBUOwFBVHRsu2o2yU7Y8Orx6NWtXScnSXzz9hRUVn2KfOV_4lQHkO4akQLALdM2qtztR7nKegwB3R7L_wS66G1T8S_yQVKR-u_FcCAiyFOSDZO-jx349sUDxXNcnjfPCTg382llc6dV1wsDOzWIBBsltWZ-GGv4wn6I8j_ErIDSz80TY9xpLrrbb5kyCS1ywhApDq952wTASNJxA1me1pMke1PCL5ipnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/89897" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqeqa5GqiMdRzKu3BlXlOOc5yBDmBB0hhMVzxUJMIWG23WSMvJSDrLZrwhaY73oe_JmM9mG9zU8Zg19ZKC9aPWCYBKaJPcuIY2QvKSjudLn-oyPFxeP8j4LTrpsk_14VpxxXNLlaOGj5vzzWoiM48GWUJlYm2iwhtk7m9REZvex7V67rpyMbVkS_EiO0zN-wcp2XXwrlyUJuijzrtp8KmiNMT_lj-uIk1_cwcqrqIwuPqrl0DueCa8g71wQUZskN6Awfh10cHehpMrMJRdyunu_fNXOrSdyaiTLcXe705omKRNN-MibbESaQ4tNjgLzUCQhnzQ0fNjSOkG_SgU60yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسانه‌های اسپانیا: امباپه خواستار فروش والورده توسط رئال‌مادرید شده است هرچند وینیسیوس و بلینگهام شدیدا مخالفت کرده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89896" target="_blank">📅 11:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89895">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0SgB1N-S4Eqg8OOcrV_GftGvQZQz5Dth8CIEwo8Y14Aq1PmpfpYTUTXf-qeo0WgbZUd0XqPsg36_yzMlczDY8OY0WB4u98Lzp9BM4O7QknuGQtIzs8zXeIEK82sj3vKop60QBf0HJs-9CJoKZ_To95IBElrABqIFC3UrTqT2ceemh9rkaWaHKjbQwmzxzii0dD4vbeYqKXeSPpqpxmOOk5XhwXDUSQJG9KQukNL_mZL-uWkLclr5TpzNr0HVdcrcn0eF9NA9rR6mFzYHGkMiG5JwF71VHhuCH-FDnFOZe3I1q1ab8vYuM7Q3v6BE9IeIQqyakGH7A4FuX0xmV5oug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نبرد حساس قهرمانی لیگ‌عربستان
🔵
الهلال - النصر
🟡
🔥
امشب ساعت ۲۱:۳۰
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89895" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89894">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=JfNoERHE7edBQ-W1RuGERMhPZbKOSmJaI2MI50mL9xPH3SpMd4vOsepPCJJmG_EGCxDTk2HVNpiwYu0-_hLJdqgxeYTZBJs6dHO8xTAVkCucsfy5f3rtYD2rQgg1W80TazDDSc7_VZDvrfn8C_vJGtlpd92seOfsRt4MT2V7RHoPNMQ5e6gujJDCrJUPCpXJee-RSpdbBWu3PFLb05t-6IoIEe9VXKW-GoOi_FQdAks93JBIgIeOE-KgfAcsencF6TpVMGDzGYDIjMeIZXUDqpOL6zy8tE-2EBTp4qgDpYzGKegsjAk34zYkUZhOMFGEv0DRYA1YeO_DsFkW3ZDipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=JfNoERHE7edBQ-W1RuGERMhPZbKOSmJaI2MI50mL9xPH3SpMd4vOsepPCJJmG_EGCxDTk2HVNpiwYu0-_hLJdqgxeYTZBJs6dHO8xTAVkCucsfy5f3rtYD2rQgg1W80TazDDSc7_VZDvrfn8C_vJGtlpd92seOfsRt4MT2V7RHoPNMQ5e6gujJDCrJUPCpXJee-RSpdbBWu3PFLb05t-6IoIEe9VXKW-GoOi_FQdAks93JBIgIeOE-KgfAcsencF6TpVMGDzGYDIjMeIZXUDqpOL6zy8tE-2EBTp4qgDpYzGKegsjAk34zYkUZhOMFGEv0DRYA1YeO_DsFkW3ZDipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی محمد قربانی برای الوحده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/89894" target="_blank">📅 09:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89890">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=v4_z7RYxB8hQJ4_VONri2rOVF1TlLp5RV8HKFWjys71i0AfPNcl6mHr0PYW7ZZGnii04aJ97Rd0jEHtRRk_Rhg1nYdOdIIpHn0nwe_jEe8-2ph19I3nPAiLjS2PIheBWVh6TcrkwCZrx_k2xywaYznT3UuRqYT0wmvShNep52g_xR5GUFIAcZpDiE8F6rjvS-MRItKrYsPExRa6OmvwWxBM4K5Z6G8U6SNbo5R2knOz9MwbY2zzSmJgdgq3P1VgHa9m2xrI89QiGLW3cg6w1a9vbdF6mIw2B7Mf6dU8JCotqmVSOfQmbSDlDcIivHLxiOqPxamcunjEXnOOqcXHP3X7GEfS30Tj3WlUQ-ZOp-qgsADx7Uwg5lzLvVDX8eIiwhWy1fnF8mbTnpyOrn2A3bX9NXp3rXQf00CrcK4euTRgdw-Fv-xG_gfQP9K2lFK8MXkDC-t-ghGVGeHnDaPfNjKr2tItINdBUzgDHJsZPt0WXtcAe7rtiYTbKLoj_ROqfgb3Pa5bY375QirT05alTAdRfRiGFsaohduZQb3BEDPIjU3MI2bIqD3fbV9jH31plJlBl5XhcMvjFPniG_y1atxoL2LxwWsgzIzQr20Y1hMRP1dXPXhVg8saKHWRqEZ9ydgWJibmHwCQa7EHmR9DxMQ5bOD_hIuC1md12GXp4aMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=v4_z7RYxB8hQJ4_VONri2rOVF1TlLp5RV8HKFWjys71i0AfPNcl6mHr0PYW7ZZGnii04aJ97Rd0jEHtRRk_Rhg1nYdOdIIpHn0nwe_jEe8-2ph19I3nPAiLjS2PIheBWVh6TcrkwCZrx_k2xywaYznT3UuRqYT0wmvShNep52g_xR5GUFIAcZpDiE8F6rjvS-MRItKrYsPExRa6OmvwWxBM4K5Z6G8U6SNbo5R2knOz9MwbY2zzSmJgdgq3P1VgHa9m2xrI89QiGLW3cg6w1a9vbdF6mIw2B7Mf6dU8JCotqmVSOfQmbSDlDcIivHLxiOqPxamcunjEXnOOqcXHP3X7GEfS30Tj3WlUQ-ZOp-qgsADx7Uwg5lzLvVDX8eIiwhWy1fnF8mbTnpyOrn2A3bX9NXp3rXQf00CrcK4euTRgdw-Fv-xG_gfQP9K2lFK8MXkDC-t-ghGVGeHnDaPfNjKr2tItINdBUzgDHJsZPt0WXtcAe7rtiYTbKLoj_ROqfgb3Pa5bY375QirT05alTAdRfRiGFsaohduZQb3BEDPIjU3MI2bIqD3fbV9jH31plJlBl5XhcMvjFPniG_y1atxoL2LxwWsgzIzQr20Y1hMRP1dXPXhVg8saKHWRqEZ9ydgWJibmHwCQa7EHmR9DxMQ5bOD_hIuC1md12GXp4aMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درخواست صالح حردانی از مسئولان برای معافیت خدمت سربازی ملی پوشان فوتبال ایران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89890" target="_blank">📅 00:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89889">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=tUX-9r_BC1Q5YpYequtyIgHSk88he6VK7Wf54atsZPXfq_wzMerkzNQLEcAxz7VlkC5pgCW1rBaVyvoVtgy5fJsptnenIn_RQrzgdMUMTL7q5q6tbLBkGMJ-xMrzEPWNgGghWAKf_M5dNWHlTNeFZ3bOnEMopmwCzaOu3EA0iMgVNTXN5Pg5fwbOljtx2an6aVjzon1I9JnIoEILaK-7wRv4G1sl6aEKhus4YdXKRhEQbUT1bl4cDo4YQ8ikNVre1d4nyTwTpRJkoA1pvPlykvR1ogHW5ZfUFXlUcTWYiNJRfPQeu2Qtl7ZOEGbolhAn7E5n-jL2DRbsKtjMVvbsbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=tUX-9r_BC1Q5YpYequtyIgHSk88he6VK7Wf54atsZPXfq_wzMerkzNQLEcAxz7VlkC5pgCW1rBaVyvoVtgy5fJsptnenIn_RQrzgdMUMTL7q5q6tbLBkGMJ-xMrzEPWNgGghWAKf_M5dNWHlTNeFZ3bOnEMopmwCzaOu3EA0iMgVNTXN5Pg5fwbOljtx2an6aVjzon1I9JnIoEILaK-7wRv4G1sl6aEKhus4YdXKRhEQbUT1bl4cDo4YQ8ikNVre1d4nyTwTpRJkoA1pvPlykvR1ogHW5ZfUFXlUcTWYiNJRfPQeu2Qtl7ZOEGbolhAn7E5n-jL2DRbsKtjMVvbsbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین یامال در جریان جشن قهرمانی بارسا در لالیگای اسپانیا، با در دست داشتن پرچم فلسطین حضور یافت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/Futball180TV/89889" target="_blank">📅 22:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89887">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksL68BMTcRTN78MAeoWY7Tah1razQ3dxz5poq-Od4041c2EpPU-voE3-cWSOHZr9ijtlqYO8_XOuWQ_Xyqqouf92tYiu95i-JULDtTR_P7Dgb31CQkitgdoUwKcql3WiyFz0Ad0iwYK0Rpw3qJgtktNCv6oRpmBssCn0ep6GypHVTtLwPN3bV8BIyRSTOGpJ0-8odnEJ4zjO5jg4IRoI3F_GZrOZsHh6F3Ii_cfyVb3A_5EfnDVN6QjvIdgd4k2ficbQRxBukfwg3d55jTDbQFf4uu5QbA8XfoEan5zUKMK81RwQEY0uq9jB19q0jdtt_ceDJSyn4Uugrw2-hIqDMRmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=voQH13wdZEb_DnXrSvLvheO8wcTgHTq2k0xmM_NeAMiPfNvDYmJ2W23bYRQphlWbQ3eaYzELbBd1FCqus7qlcLsQyOYPBszgEO956LQIaqiTDv6_dT9s93OBF-vwgFSwiCC_y69x0PP4oYoOU_8e3ZpfcnbaT6X42Fglnfbl5u5fdrCKM6xvhArCLeBLd2_Yy20F67WGvQwvElonOcB8ENFo5b4FJ1ZNqZk2zwLn_Zmd6s5SVd19NuOZVERe929T15dEPQ2Qdibo3A-0F7DXW7CcZ6ONn5BmCUBzrzs3OjbjH9ni1EwzqltDuSte1H4XBZZhMgj2gzigmwC7aU_ksL68BMTcRTN78MAeoWY7Tah1razQ3dxz5poq-Od4041c2EpPU-voE3-cWSOHZr9ijtlqYO8_XOuWQ_Xyqqouf92tYiu95i-JULDtTR_P7Dgb31CQkitgdoUwKcql3WiyFz0Ad0iwYK0Rpw3qJgtktNCv6oRpmBssCn0ep6GypHVTtLwPN3bV8BIyRSTOGpJ0-8odnEJ4zjO5jg4IRoI3F_GZrOZsHh6F3Ii_cfyVb3A_5EfnDVN6QjvIdgd4k2ficbQRxBukfwg3d55jTDbQFf4uu5QbA8XfoEan5zUKMK81RwQEY0uq9jB19q0jdtt_ceDJSyn4Uugrw2-hIqDMRmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: من از کردهایی که به آنها سلاح دادیم تا آن را در داخل ایران تحویل دهند اما آن را نگه داشتند، بسیار ناامید شده‌ام.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/89887" target="_blank">📅 19:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89886">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=izATqa9uyEaDu48wNIWvtZsjHIqFpLou_TQRgp4B93Ac4q5RRBMRXjqxlgYWe98aSJJsQCWpJTa3DpWHDWCsNa6lITTqGSaU3bLoIIvMvWHk4o5oedsVX2sGl1_zJby6biqfT7L40IjMusQoSEcL7ZIbOB8WzvzD3W2zB7Oz-_Q2eQt9Koel08PuwYjSpYnW-KGhqvy1eVFtImY_fRXfj89ukN97rLn3zBbO-ESSd_YkBwvBezOh3B1Z0X_5HJEztYBlsfvXqSPxMB8B5Gwhj0doxqiQKW_tdqZS2_HP_2QoKlO0vTTpZV0ysGGQeSD-T5jFjQ_9LdyooqoCFjSnMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=izATqa9uyEaDu48wNIWvtZsjHIqFpLou_TQRgp4B93Ac4q5RRBMRXjqxlgYWe98aSJJsQCWpJTa3DpWHDWCsNa6lITTqGSaU3bLoIIvMvWHk4o5oedsVX2sGl1_zJby6biqfT7L40IjMusQoSEcL7ZIbOB8WzvzD3W2zB7Oz-_Q2eQt9Koel08PuwYjSpYnW-KGhqvy1eVFtImY_fRXfj89ukN97rLn3zBbO-ESSd_YkBwvBezOh3B1Z0X_5HJEztYBlsfvXqSPxMB8B5Gwhj0doxqiQKW_tdqZS2_HP_2QoKlO0vTTpZV0ysGGQeSD-T5jFjQ_9LdyooqoCFjSnMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😄
🚬
شزنی‌همین الان وسط جشن قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/89886" target="_blank">📅 19:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89885">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYOadZ9qVOGMTjIHW0BxV7D3HtGd9-VzuhBy1YmFbCPlXFawQhrEOWr6de2kw0QGntJ74Z3U48IQ6lGTODS-baLznEsa35xywDup80UurT8cFNQCR3sgPGHtaGEvmWALz2TB71k-SCqUIFxy2N1kUVh_Q9qsIqQdbo48xgRS3yqLnLjzhbTauudY_jCFgUewwiRbmjgOmdQfiL0ZH0TuAFLNpo753XHTARtlCdg26qkkpYkcpO3VhHzjYKN5MqsS0CzfPICjtMiijEVeeM3Z9qu8jXvvJIOMpF8qQH_tXrTE4Sl62s2eVsnhVd5KzBUvDhL9n7deCRmIsFgb4pQrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ایدول‌خبرنگار مطرح آرژانتینی: لوئیز انریکه سرمربی پاری‌سن‌ژرمن خواستار جذب آلوارز ستاره اتلتیکومادرید شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/Futball180TV/89885" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89884">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeTfZvLoQaKKiZB4Y2gcT0ALS9Qc-z3g7Rj74Lw2uX7jw0E7UZxRrR82iSmap9Zbip3wnKY_dVLIPBsRbiQQfXKfos2ozPi04XrOEOKJYSo-1WGniYEYoM3tlfLN2odtbMfj02Wq6uwcKinfGSUJLKXMwG5W4Y9FINLVuJwRQwb4Nwbcb_nE5p7f3WeRNDd_FNS-nO6Fddrg0jSinti36JZ_WvpTYbnrzq8CQEtzFXCFcStOtBga2izECKoNgUanseHaYHaifiWXlhqJAbN7iudF2VWLn379dodhv9ewBjxuIdE70EmEurDPUmwQKLKHvQ9wnkyKNFjNwYG0BSrA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇧🇷
لیست‌ابتدایی تیم‌ملی برزیل برای جام‌جهانی با حضور نیمار ستاره این‌کشور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89884" target="_blank">📅 17:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89883">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS7sLKjz9hS0sRifo5y5_R_q35iNRsLO_XwVoVlNxwSHsKKNjYH-WZWBT4G3GYlBCCri4U9G09fHOhc2Io_d78uaxih6WU2WoXMWr77rq9Gh87Q8JXze5gjc61xLAA3oy0YgMCV3SOAMv9TmG89CI_uLHeNWHwJTRDG3-KXFHHBSiaZAM97i1ltRx5YaDDJRapcPsotJYngbXsvOy3RFr8Tm25wrH17TM6dGQo6fdKlxyWzcoXg-RnwgXMMbtBU83EqdniSGZip1KQiXj6i5HVUMJcoR3TUYy4vsIq6o1Mz0w8D7T-9bZWWXId4vGqBj61sgolrbuK2M1xVRyVmwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
انریکه سرمربی پاریس: باید بگویم که به احتمال 99,99%  قهرمان اروپا خواهیم شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/89883" target="_blank">📅 17:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89882">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAVdK4lrCdkSVdV9tTS28pMUnEKjIlLd81phpQHjA74Hn5pMqh2Z2hasV6f0pshhDJV53HvI59KW6U76ztWv1DFHuqSfrJxfDuFzP3L_cO3EvfYnsThmmari5BRCQSHay-cHz3b1NrxOZ4QjGp3hiMC4tFrMe4c5hGHgfXaB7vFvPGli-bwfONRfHQeDNlzZw5wJGDd_h3utDeTVry4SlC9JfNQiaxJtUCu5VhceZbmHmR6nrhWtZ8HEe2X42Rc_dFLp5GpOXPgvWNFqESrMkhNcHIMaic83xl2YNKjnHJfsNZVlWo8EEvWgOdQRqInSE9i7q1qLqHcXDj1FoqJVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
خامس‌رودریگز اعلام کرد که پس از جام‌جهانی از میادین فوتبال خداحافظی خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/Futball180TV/89882" target="_blank">📅 16:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89881">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaN0BgCZK6PmvGmSSzODp6LbKeVB_0xSFxfnRJTPd2DynW--h5PP1sNqqtDFobSN9wyRE18QOkJok3MkcsIM2qtVoo_GsmOsv_foSUtFajoNlRRM9F0zYpVXSJQkwTrevMs7uf730FzHc5TmZAxNiKRvZ8LOMEs--2vK6NU-TD_ctT5sEbF1HJI3a0hloeyQM_xNfAh2sNa5jE8gpvskyFoe1KlyVZeDYdLesizo5KZNzpSWvT6gJ7F-514JkfNK2rezBF1qM90tmd2rImAe3-8-vco-vbZ-RNFBoB-VaQ0y7xe7Ytw78ZC0GDB1tcXMBhQHP18-XCmqT0D-Q36bQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
دنیل‌زیبرت آلمانی داور فینال UCL شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/89881" target="_blank">📅 16:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89880">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAb8nze9SHV3UJn4S7oFKU7_vHIxDpvgnGjaQlxyNl7t1_h7h9bZUmozTrSpsj3Ej6_pgB0hR9I9eGR-H4IhJf47jLhwKMCmsj5hp0I0BAK397f190mPlndTgPGcy2w1pVmohFTbKBZuO_V7KNVk-9lepoIhD3bhzpjcM6T6ZTrY0bQ65razFcevgkDVZBagaVpzZJKCFSvAMOQLfrq30c9T_jTalKlNFiG_QPvUDOEKunJ0Kw5Bmh-GU_otBwgAT0EOJVpv2gV3d4fblb7cIdvAZ8KC7fpwn4XK6GHzVWokF_ZYITQ_zTOkqqixahgc4VGGUBYkeVfOT81ZRqMEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فهرست ابتدایی آرژانتین برای جام‌جهانی، دیبالا رسما از لیست خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/89880" target="_blank">📅 16:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89879">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6bFw9iW_GlZj7YWYBrLkyrRRrM0UE6XxQtWgVR4o5AuRZtlCHXKkIV6duiXtZ0BvrADvnh9jnkjIAqE62nqAP8j6QsY7vpSXXmUaXFXosAKX6O0rU4xzQ5Y-oWiVhCVu1NV9KM0ICw76T8mHz8O6RijnXYKAX0SsmsaaGrgiUkfkifyzzgVfrb-IZj25fOs82sv4etYSPTV_ojG2zAyYoITorfmgZeOxybTtojWH7Mm8elizuApzx9HM5zbQfeAz5VBgw9d2kfXstqeeA3BRUxaBOARMnvV5Y0YZ4XftwCNJCOIP82LVWF189hMxv26yzEPWQG4oeUJO-JKJ58XtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💼
یک ماه تا شروع جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/89879" target="_blank">📅 13:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89878">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
⚽️
در آستانه جام‌جهانی، یک شهروند آمریکایی به ویروس هانتا مبتلا شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/Futball180TV/89878" target="_blank">📅 13:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89877">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
کنفدراسیون فوتبال آسیا درخواست ایران برای تعویق در اعلام نمایندگان آسیایی را رد کرد و بدین‌ترتیب احتمال بسیار زیاد سه تیم استقلال، تراکتور و سپاهان نمایندگان ایران در فصل بعدی رقابت‌های آسیایی خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/89877" target="_blank">📅 13:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89876">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jyq39f8nfzP7eMuw9_UOUVXnkaXkNb4iSEHY1A4jmCKTY0M8regtvfT_FBisI6uyK6JhMTc2HsVFY-DzgNaCfmYLen_wqjjwxCVXJW1ZDvfxnsjoRXLLOyQYx2AIKVTbuPo3Ik76NSC2U15ceN_6r0TIxkce5Une0uRxeCILN_L5eOiRo1IHgmz_gLnMY9zYosiSvQ7kdM2320pFrITI_Edv-f7THOX7rsj5B9GzVOlSgUBgP8VuJsR67Lll3kn8EiCQoG6KGRzCNDkdo9G7IEjtGFsuVJsk35VTR-xxciDeKSkq-VI6QxnlDBHZqH2DPHbLymq-PZKlwG_198I0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/89876" target="_blank">📅 12:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89875">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7fq0TzG3aKgmLnhsaerlpiQB66KdPN8pTsh6Aqd8IZdOT-VmEykKhE2pYUEqGE147Dc8tBD2eA3NSbaazBaTpjnhZcmXkO5A9SIKSW9I-x7hLNV6q4RecHE3QbOQZrj4RGVD1oMcWr0scy1N8yBW-ml3F0Xr4kS4Eym03km1VtWvPHI_caaP7ZeuVb13ufENmrQUzmVWjLj9pQKfQi0xfxN54N5zjWtCgJKduRjZcAIwc6UsFNLAAqzU7dr2mIXbB8ZdH3_gsSB2_nrw-ORC4djVG_Ze7rlIxAlfiW1qZNRmvSRglg_zJscravraD_C4rxrJeTC9o5x7k862gkerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
نیمه‌نهایی سوپرکاپ اسپانیا ۲۰۲۶/۲۷
🇪🇸
بارسلونا X اتلتیکومادرید
🇪🇸
🇪🇸
رئال‌مادرید X رئال‌ سوسیه‌داد
🇪🇸
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/89875" target="_blank">📅 09:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89874">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSwBFs80DOqDdBK4763mAakayPqH941EzD_9AKt_H7UBJgCM5Ouknn8kuqvTwIbgOxvnVbPRXdKbsEV519I4FtnT-B53TNaiheP0hF_CEhNB20gSk_s_ceqXO7FLNujup2TuSzu_cX3FhAA67JF9-ddTGS9_w2Cawm2N0kXqKOiLpSXbuW4jZw8zthdZ7oem3rfs4Q2bNqgLlFWT6EPnQb3fbfSd44w1a_8EqBtuAThHYq96DsO9MUn9N1FVC47j1CZ7-geN9GcyX7_WsgYgVs8jcn10zZqZW5W-qCDAt2Z-KidALVYpOqpLTQb_msbnbqlAZu5p06WSx7KG_BVnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمار در ۱۷ بازی اخیر سانتوس: ۱۱ گل و ۴ پاس‌گل‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/89874" target="_blank">📅 09:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89872">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=aBJxjZCO5zlelG606uf5a0YXzlqBHITu83tgJ1ruvZu5mmg9kcAjGhK-k3ofbpbAglEDFbIJwYCFqHv4Hsobsf4CA2zU--_gTCmOof-31VyYYEiFp0q6HZX4knJOMXQlGjiMrlwoUW8AV1liasrHbr54skfFCD0cWBueCoFtaLRB3JPIdggZE7_gTb5rVj230EqbrkA0JDKsayQXqM7BBQ2gPr_AW53lrhcooSVtLgbh0EbdeLH8iQCAv3cpl4U04BKuAYIwdnDMneHxx66emoM-yjWJcljBjFwbvZtB5M78kXK6-CwyokZgsgT7-4luasaBDd-Ahzhs7Nc4s3L2jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=aBJxjZCO5zlelG606uf5a0YXzlqBHITu83tgJ1ruvZu5mmg9kcAjGhK-k3ofbpbAglEDFbIJwYCFqHv4Hsobsf4CA2zU--_gTCmOof-31VyYYEiFp0q6HZX4knJOMXQlGjiMrlwoUW8AV1liasrHbr54skfFCD0cWBueCoFtaLRB3JPIdggZE7_gTb5rVj230EqbrkA0JDKsayQXqM7BBQ2gPr_AW53lrhcooSVtLgbh0EbdeLH8iQCAv3cpl4U04BKuAYIwdnDMneHxx66emoM-yjWJcljBjFwbvZtB5M78kXK6-CwyokZgsgT7-4luasaBDd-Ahzhs7Nc4s3L2jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
جام‌قهرمانی لالیگا رسما و شرعا تقدیم بارسا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/89872" target="_blank">📅 00:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89871">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHI0SXig7iyf8RaI7pCwN2F-_CKkRNoH8tU4MEV5MZUlJ8ZErnAulNAMQAonnhX0i2wrLltJOX-RA84g96OfDhUjmiPc8rpdKMVtSEWHuA9xgh50ymhCNBWrV15zsZcXcJrbxuAmrgJeDijNP-vZ1hLPOPL17HpTNfIWRgay_v_vvRyK4BvN819jZ1rcwwLKb8wLXWllzBA5NmUCloLh4Sg3ESjQAVNxg2QKwtGYI0o1aq8CiV457bCSV2QYaWrCHRMMO6550rdSnwSFt8a3P-mb2K3PJCY925MxZdw0bRExp-hw807L9auhNIGnmY80Luf_8QW7sSgGgB98fngQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
لواندوفسکی برای سیزدهمین بار قهرمان لیگ داخلی از میان پنج‌لیگ معتبر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/89871" target="_blank">📅 00:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89870">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVv1sQ9Gb6Rof5YQHEtEawtefARD6CKIhImNHrs_074yIjeLCfnqQhEOypeX-DgOVWvPLMcdfJLXjkCRTLEzPlWmP7mgMup4KRtZ_bgy5n3JbvHG0M64M2nLeqsCvXnr9jwERyoETOc2dQgmwpWHm-sUKrsP66F-NGzdgqGxvr0pfssfQbSObz96wsWl61zn24rnAGyHdMTJ4m-gOk06MGq_M9x27SMwejYbAV33ecTQv5NhavmlcuOyq5cBhOW1sKPgLVjPJlQ0q-_dIEagxWVhyKIc5kxIlgT77IR6j31HCJe_aDt6uJPZO4B9FfXc0W46gMuiWZkPBd7twRb8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرافتخارترین باشگاه‌های اسپانیا در عناوین داخلی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/89870" target="_blank">📅 00:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89869">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2Mkt_iAFKCZTodMJDQeCCl3B8qkuPrYdrltanEfZDi_7QxVi5ya5dvBTFXGMgiqY1lI5oAmWAShPrtH_Xr8B7y40MOwhnUXZH5P1V-vKJeG93Cimhg2OOofZkaJZBFI8sMWJV6a-HbKss4oGMdjIL4wXx7P4NYQVRhsHriz_nQrRfSrgGUqh5vvZgMS0maxVlkxT5UU8uAPl6i5jNNbPzmRi1ttiHvZRefmtLSdGl6Yk4lBC4yIRWBimMYPV-tW8ESotmboIX8UYOOR3QK61BxHA6Pwkg0b-xHOs1uUWR_O49IcT9ROABzvxlIxAMbtH40MtIuZx1L7XSXtG2Pz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️‍🩹
استوری لیونل‌مسی و تبریک‌قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/89869" target="_blank">📅 00:40 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89868">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
😂
آربلوا: پنالتی واضح ما گرفته نشددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/Futball180TV/89868" target="_blank">📅 00:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89867">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqGODy4dyOYCreT0xdWgePLfWKzSzrl0lS4DImVDB47YODgH-ssy2kmX-AhjTrRDgoKu-xpE5Lz7ZoJFXWzBZ0EjemSAVqwC1Y0KqrKcQpQwKPTEFQU_cINiuyOrTpcfWe6beUnE0qRNYpCDYsutKU_5KFO1ThynkRA2mAgTOmBikyBdU1fAzndEYrXOkVjNWaiRC6SzBF-3GuJMlGXi2FLlbf4mQOJaxZ4QSTccosUjfHQp55kRsxQCd_h-WglsMVDzbFGJax-P1z0jTVk7Ap-DJVwpOSJqdMo_VxTBJNaP5TLeLsCqMnivkPu0TII9GWXmSchJqPrj1XirOB0_OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
باشگاه بارسلونا با قهرمانی امشب، به رکورد ۹۹ قهرمانی در تاریخ خود رسید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/89867" target="_blank">📅 00:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89866">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmvVUo9ty7otYRfu9fymA6SUiigm-tLLxLllKPSkVz0dYe9GZXwkNKVbBwpl9YBKprwuWlV0MarrGL0bWS5UCnxadsf6ScontgWB-OJzxkD_6ciHyKQntxqVOwesO2DQ9Ay_HQvlpImHPf2E8nMkxneW28YdFCoFdLNcFqAO0go_T4mx512bGLkpvv-Jcn3hdRfFRz7h6lmhYW1AHYhMLR24Z4Ew3YN-yC3mB84ie1CQaIW7ktH3OTxBADy3DyMcUa_X5c7PgJUTwMQ91lKdgAokW_nRvrmAj8weARsKt2WiJUBNCW0wY-uHXTpYN-eBqPw791R5KcNjjbXKsMpTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک رئال‌مادرید به بارسلونا
🇪🇸
🇪🇸
🤝
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/89866" target="_blank">📅 00:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89865">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sur7KzAFD-JetDdrwDHp_ti1T9ZjPiNyLV0RpWQf9ZF7A8MutyTo0SRPvByUHFb1c9eijjJU5xHRT5zFi0kbla31Yqc9wm2FqifOkP1_VCig2gVbSopHjnz5iuA9qh7UkkR4c1aEZlUGgZUhOS6Dl7qo20qaWKL21TOdkOoy5CwAp0drBkyWGzKmzcYi2kmaXY0Y9QecichyoIMypqrrXQ8pEA_WVMDqQ0Rkjr_sD8Qsldd1vadt1DjbwfnwEs-qg-MS6o1ER_mkXWBjKBZhUEUJGwZ_tctKJ9gQuhxoYQfZuW2EwIebeZtVXoleRP97TBva6HbL5-PW41VSY0Cc-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
یه آمار جالب و بی‌اهمیت
📊
لامین‌یامال ۳ قهرمانی لالیگا
⚠️
کریس‌رونالدو ۲ قهرمانی لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/89865" target="_blank">📅 00:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89864">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDj8TvQ0uH8_VdGZe2gOIXX-UgcLUAtZyxpmPusac0mLl9rhj4gQvGvxYRv8nNoJ1tQiOMPMPS5nalqTTo-D1d91sg4gmmXhkPSgLaBqa1_HlpcFz0r_6xJ5tvSDFcykAabsbIjBUEs3z3d48iUYvD7hDvEhNY9YU2mW355Wl4tcJdN0o9bhOG-zhbUKZPSO07WpieAIyO_3vNUzpr0Zqan-cRSgNWGgMeUNKBtRllFFDrrEQAgpnVso_1Hf2M7Qc8GyPHO4IMuWw3mIR9mJ5cjkCOI3RY8vL1xkBt9W0LjQYxZDpdFFOmNDnn3bhJSyHaRVP5p2czCdzJtcNiW-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوان‌گارسیا بهترین دروازه‌بان فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/89864" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89863">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0DmGjM42iTtApqD6SD2CjFlr3hJOlZwSC_-6KJ8-14Dqy7zjMVglFNtgKXnykGt67o38Ot5EKU8uOL4QmLj73s5m8OEJ6Hm-oh4QzVNjblgA6Gn4iTm_tghYiTmJCTa03hItsrJdZZ_pFFEU4XMI6lZR39ghFRaQxSAStnXzGhFTi6_0tf45LgGpUYoRHWR395MtQqYb91s40z-TTdz2vTJ3BRgHri4Rw_Z9BfGBN4p2C0uCaKYBR_ioHSlBXJrncn02U4M5pmEdOUSJLN_5gVaylqk8luoFKP-bUF8WX7auUZ1my5oSS5HG0Pt4H6k2nNqxij5JSLlJKn5VS0SQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
دومین‌فصل و کسب‌پنجمین جام فلیک در بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/Futball180TV/89863" target="_blank">📅 00:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89862">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtgFJBD5viLQzVAICILmTH8caqHGJjoMCuNZUy1FnP2QKWmTDesOr1POs0xs9FvMzhV0TGZGD-TSSboPle9YjVhbseYUyJ0_GhUDUyo3w2AwZDouWVX5pCFPJh1LxgocHif8wpxklhxtghU6EmItCMx6IpUgbTD_TasSvECqjE6jvl3bBYDtoS4qf1QQl3C2AyyyPPrtxMEHR8MtS_BcPfurAucxGE_YXUF3OlUaWkllUHPq7ltzGF9pm8B2HEEbOdma0JI3ZiCYnBJ5bTF47nFux3zHfDXZDh2R9GONhAmbGjEUA0eiaHDnOz4fo7uHbwWWrhSdTh_LHdIA4ntf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
بارسلونا قهرمان لالیگا شددددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/Futball180TV/89862" target="_blank">📅 00:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89861">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رئال یکی زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/Futball180TV/89861" target="_blank">📅 23:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89860">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECY3239aAn8IKpkfcGp6vfGR_41N1nPs-8aHnXY2RVqSY0YKi8wkq1bC_Gd7geeodFz497RiDxqwfRKK2a0oLxXiFAs9mHyrYcGtEY-cmKe2JF201iXZwsQfdfWVjWI4m_ZV6Qht9Ukf-5VTqJ3_egsk2pX-nd_o-kQnIciQFyKobf8YD0HUjn0sB_QUMff_C-ahtTEKllD0FySIGWj_vAp2UxdZY_K6PwQscxL1809mGhIVDrrYRw3xg3Vhrq0QfQ1sDelS7iLM5XCM3YEu1QJQjxMSqAgug3nD8gBdlGdJ8t34hKxPC9vcNptguLzxa72fj4fN3FC5MaAAwVe45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ ترامپ: از پاسخ ایران راضی نیستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/89860" target="_blank">📅 23:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89859">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-fdCENl4vFruj-uNZazC9NKOpZT0fD-0shZwIs7bABI6U4HiprS25NANo4N0ATtjhItNxGzEkqVYs4CaP6SMXAiO7zg8seOj3Qy1fa1f2DV26zm02Z35nhj57NW_F5ChgNIzaZ2WMNHhrN9ZsVar8tAZarY0_Hm9NfFMjFpnxW0u7jj2zsxUL7je7U1Hqlejg8C4VIygqTWlcAnQqxhftwi5ejyVfj3HMQQT9UKp60oPopNCDGahZrYkynskuW87jSx1rlBsPQUMSL3p4ggxtWPy46hQUj9WVmDojE6Ybm6zfLDdT7XynPX5YuwHzi2sW_p6weFpVrP_9m7l8CZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری امباپه وسط بازی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89859" target="_blank">📅 23:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89858">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4cd35b145.mp4?token=TN-lsGb549nkLpTymvr9tU2kdKwzFmkVtMenHlnDLEaFbrHur3V6hsenxkmE0vOec-JS8Cfi1KiAw-b-MANK3ipYDm9h0wjro4t2x4ikdjktJGshOJgy9gFx-SJoxmAR9HmTqLuc47eNGBHvg8ZatfmX-jzq8untoT_AKxlmN-xh_tDetg0AKILNHn-HOuxazpmSrsaPiLyJOGCdN4DrJwaD8VlVy8HyfF5yVoU51jHPRp3OA5OzOkhCzRSad-B92oW6udsaf8O0b99zTbhqI8wVcXDji0VP8cAl7RA-DeE3vVXFzTYhrH7vAgjstyfHaaTrHLQGYnZDKmArG4CQ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4cd35b145.mp4?token=TN-lsGb549nkLpTymvr9tU2kdKwzFmkVtMenHlnDLEaFbrHur3V6hsenxkmE0vOec-JS8Cfi1KiAw-b-MANK3ipYDm9h0wjro4t2x4ikdjktJGshOJgy9gFx-SJoxmAR9HmTqLuc47eNGBHvg8ZatfmX-jzq8untoT_AKxlmN-xh_tDetg0AKILNHn-HOuxazpmSrsaPiLyJOGCdN4DrJwaD8VlVy8HyfF5yVoU51jHPRp3OA5OzOkhCzRSad-B92oW6udsaf8O0b99zTbhqI8wVcXDji0VP8cAl7RA-DeE3vVXFzTYhrH7vAgjstyfHaaTrHLQGYnZDKmArG4CQ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوممممم بارساااااا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/Futball180TV/89858" target="_blank">📅 22:56 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89857">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
فرررررراااااان</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89857" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89856">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بارساااااااا ۲۲۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/89856" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89855">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گگگگگگگگگگلگلگگلگل</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/89855" target="_blank">📅 22:52 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89854">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e39aabd36.mp4?token=pKXCN3igekxl85zPY_vnWoyeG3mQvqd2hZRvDUUcKIxFuzhOFwaRSd_kg5hZneQsuZG3W-bO-qblZvSuaUigNz1VGSi5ASoM8SyQL00yOCbhsxjSFzLQ-iJo0zKBm5wTLs2uIkTflYgTAY6xb2fXs2GfAY4wDT5IKH-C0N5PgtamAwe5tCZhrKAsZnr3kD1jPHchEWI6vTpAkw9W03qO0ZE4XNoK7UQclmAxzRFFMV5_U0QdnCnXcvhf8IQ-WNvwhSU2ZYookBijHZeNuy0mDtPu9T7GIF_8qHI2eiV1nEpvDqMxrbn9S_oBxPjv3WvNhrGibD57JIH9ZOZO4ZRqCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e39aabd36.mp4?token=pKXCN3igekxl85zPY_vnWoyeG3mQvqd2hZRvDUUcKIxFuzhOFwaRSd_kg5hZneQsuZG3W-bO-qblZvSuaUigNz1VGSi5ASoM8SyQL00yOCbhsxjSFzLQ-iJo0zKBm5wTLs2uIkTflYgTAY6xb2fXs2GfAY4wDT5IKH-C0N5PgtamAwe5tCZhrKAsZnr3kD1jPHchEWI6vTpAkw9W03qO0ZE4XNoK7UQclmAxzRFFMV5_U0QdnCnXcvhf8IQ-WNvwhSU2ZYookBijHZeNuy0mDtPu9T7GIF_8qHI2eiV1nEpvDqMxrbn9S_oBxPjv3WvNhrGibD57JIH9ZOZO4ZRqCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
گل اول بارسلونا توسط رشفورد در دقیقه
9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/89854" target="_blank">📅 22:49 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89853">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNqdGgSDhVM7zby2Ue4aMikqVZRrJsLfjEUkZhIwcC7i5397HH4ILZp-JDLm2_we_uEu9w_qP1wFk5Okj27qd4fcW7RHtwccyTwn79pAlgQFam-XyGnG5uxIhX7t4hHfA888Vswr53gtXUAWQxmY8y48zn7yZ1Ffzu2VK8a4CisJpwUXyq6M7Ne0nnsgR3wUR20ZN84dDCIlvr8a3x8vfLp9oBIq0Mwn9gN-8uPpIahm8-Mhe441TEL8m_ePHPRzBwVJzLL4JMmOQ_axHqa-4AsyUQx-Xm8U-rDuJjJUQhpUufjEFLXN7eF80uBP_CVQdO9CnRmAb2RYevgsSNbIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزيدنت ترامپ
: ایران ۴۷ ساله داره با آمریکا و بقیه دنیا بازی درمیاره و هی وقت‌کشی می‌کنه!
تا اینکه اوباما اومد. او فقط با ایران خوب نبود، خیلی هم بهشون حال داد، متحدای ما مثل اسرائیل رو ول کرد و به ایران یه فرصت بزرگ داد.
اون ۱.۷ میلیارد دلار پول نقد هم با هواپیما فرستادن براشون، کلی پول هم در کل بهشون رسید
انقدر پول بود که خودشون هم موندن باهاش چیکار کنن! ایرانی‌ها قبلاً همچین چیزی ندیده بودن.
اون موقع عملاً احمق‌ترین معامله تاریخ رو انجام دادن، چون یه رئیس‌جمهور ضعیف و بی‌عرضه داشتیم. بعدش هم اوضاع از اونم بدتر شد با بایدن خواب‌آلود!
۴۷ ساله ایران داره ما رو اذیت می‌کنه، آدم‌هامونو می‌کشه، اعتراضات رو خراب می‌کنه و تو منطقه مشکل درست می‌کنه، ولی دیگه اون دوران تموم شده. دیگه نمی‌خندن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/89853" target="_blank">📅 21:31 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

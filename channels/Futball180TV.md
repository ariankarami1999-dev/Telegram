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
<img src="https://cdn5.telesco.pe/file/eweV_Z2jjHsC5rSKawF16m150WJl9x66cOShk79XSUttpKOtgwAutl1ZP_IaHKFvOpIyYCcod0xSeuBGpVWtZeLdQNfD29WfMIVWMF5EHTvbeXQ_t5CowmmJK7GzYcxAdM8AT2MLUHxVnbjYumPkkInto33zw3IqBSzR9Uxjd_sHPOFywqWjTwBL1MBoHBsGFwgIIs01VEqczDD8ZepMI9YUjtJmtZLHrgpjONr5GJsAgajdZy5_AaltA-JTFiCQq33MEMCYMRE9izVN01IkQjksztq-Z0-c1hAwyLcay1pm-vD8x6H_xLrOta6dncYswGfUYhZnchKYKz2PRiwQ_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 438K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-105000">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e4faa301.mp4?token=AnP0r_Ty4UwxrLmWt71Hido_btCaLzNxIPsTEjcuYugx-KB3vOkeFKhrlnhKMGjWiGc6My4Hy2xXtL7Af2axlF9eLfbICurvjgsINQVIINVqV65viKjA8JD6wwGjguPAYw_4ufAKNFERI9V9QMGADpFLRQE8oEyM0NqaO1InqeMQF4Q2FAIl2-i29D876Gn3VninseFkoqVKd8thx5ZoX4D3M-7eFsvpoQKY_Yd_vYyWJiWbUaqCcSxM_bvj5F2JGoIS5dvfoT6stRL64Cmr01KIoJ3Ay_994pdk-xq5OiqYdKhJjtz0rGt6TGLMhScIqc12aQxzowhwHJunmg1WTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e4faa301.mp4?token=AnP0r_Ty4UwxrLmWt71Hido_btCaLzNxIPsTEjcuYugx-KB3vOkeFKhrlnhKMGjWiGc6My4Hy2xXtL7Af2axlF9eLfbICurvjgsINQVIINVqV65viKjA8JD6wwGjguPAYw_4ufAKNFERI9V9QMGADpFLRQE8oEyM0NqaO1InqeMQF4Q2FAIl2-i29D876Gn3VninseFkoqVKd8thx5ZoX4D3M-7eFsvpoQKY_Yd_vYyWJiWbUaqCcSxM_bvj5F2JGoIS5dvfoT6stRL64Cmr01KIoJ3Ay_994pdk-xq5OiqYdKhJjtz0rGt6TGLMhScIqc12aQxzowhwHJunmg1WTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
یه‌سوپرگل در محلات برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/Futball180TV/105000" target="_blank">📅 14:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104999">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcHc7-d5qkFcukGflfSPaF52eYSd4HgiAM8jjB0ZU15yETxew_U67TmU18tJecDjR6dnAg3BaySW4FbkO7pHXvPZs9k2ITv_e_zcf38UxE13MSP9dn9FbUpsZZ8zsfnrSkCVxT9DQPhOVyxhrfPLajKXN8KPfQ8knhgyXacm4W9N6Bo-Vh2QAMGly9gt5dJrrV8xw7yVCQSO9H9SWRHOkw6SsgkXUSvmal7IPjmMGbPLaY-usTY6s5Sg-geRoJmeCnnYCfGh9dDNY-E2xX5gV1JOE6dP6eUu42tlIEWJqpoP2JjM3Y5XKlfhuXrHT3thF7KM9gkPie0TZ1-BgziZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
پردرآمدترین بازیکنان لالیگا در فصل 2026/27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/104999" target="_blank">📅 14:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104998">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3cUxEWbLrM6lgUejQU6UH3wA3UNOi_TVUWKXE4ldfwk5iWWK1OsALw1uAfcMYE3TYRbvMd5oB0X9XvJMX7DUzTXT7VEn0v0OSzBe312OajiD3ZAhEC3TPUZLEc-6m93RLsfFwkU10G_79r0_SXRW8zv7m0Ls-DI9AbMFB0r8R2BLYn8DFnQZldHzzDNB6_DjGHHteSoMzRNBhqcmj8yEJ3aA0_NnNJEr9E5HB_OqtcpNEvLDIz2ii4AtTGTaL5qxEeroJ_ne887Xcq6T6rcRkOx5WhJa2SZGZuYd3FhwR0upvZPZYMP04hEmipCLURadxEUwrsUqdY1zscgomZGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب لیورپول مقابل ناتینگهام؛ ساعت ۱۵ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/104998" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104997">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgFg8V4TQZ-3SNfinZKCNtG12CwrTtG5En5s4_xmeqEsxCvAtNFkuwF7PEmy2kJjnMu9LRy_WKJbrbsRKjOJPHbxOoY_TQa8qLzIMfSb6rE5vCbZiULwZu9hFhUQxpVR_qufJls6OGr8f0kE9UfxlcEtO1-ZoKCdUxWJyIyefNLxsZbXZx8KzmQA58SxK3Fh_An4iMf7cRCjjmbTTrbnboZg8-0xQc6Q5p06Nji6EEFzgNHzh60_DvPtGLhkxOyNgsh5mq4vuNDq1c3A1Gep8oeehG8Sf8rPNvutow8gXNlp72jXtwkw8m3jD67W3JWzYOTKvudg5_H20H5iVb4YUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
رشد قدی لامین‌یامال طی ۳ سال در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/Futball180TV/104997" target="_blank">📅 13:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104996">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g83L3ohmpRGIR0xItIr9KJKtLwdUIeqhsQGTQphzH0_Z2GVbR9JpPZE5JRFbxGnkibT7Iv7vv7B40Hfnu9U3hyFCZ-izHnanN0haCEQK4Y4pG2edePArZ1yvHyTyLkWlDn_r1C93-6YNaL3FSla7WSAqJPRVmKWcboN1OGUV_HLZpBOnjixrLdkvAJDuIM_RtoNsiuiA0A7vuA-YI_Z6HNM4O6KT3bEtb6pf8xvygEbl72up7ZH9BcN9y-qGuUQRSdZ8aJMRPqdlK_r_rgZO900Vk_Asag1fQTtY6q0ocxpjYmH1_sqFa2pb8FzXE-68WJlj8B7tB4lKWNHio6YUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ابوالفضل رزاق‌پور مدافع چپ‌فولاد:
🔻
پرسپولیس میخواست برای جذب من رقم ۱۲۰ میلیارد به فولاد پرداخت کنه اما در نهایت این اتفاق رخ نداد و خوشحالم که در اهواز موندگار شدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/104996" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104995">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d94427ed.mp4?token=TBmBhQ1WwKGtBLXQLcRbKUIC9uz-KHfxRZb08691Jpq9ELnnw5KnxVgm2TUOeuzrfnUVQkbYXif77YtJIcn6sQq-dnM1dAjTZq77Pz_yaH1F1d9ulRTJOa0QTueX07LeOTLRSh0Or6zAEmU9qwyNrdek9OoYJyp2hO6OB3QibQsSQAfHw3ck14lGaTZCSVT3MxVnGrzdl-qD0dduiukk-3iMKtLSZkVCQBufJNxkjzSOYl3IRCNnUXgmwSXxzAKRT5Fki7JijZu4Ix8yB4gGkBBOcHbnXAr24bSBQ_BRKr3hcvSy9-xQPk3R0EkIlinFnTDNUJUtP-J4KrHE67ZnMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d94427ed.mp4?token=TBmBhQ1WwKGtBLXQLcRbKUIC9uz-KHfxRZb08691Jpq9ELnnw5KnxVgm2TUOeuzrfnUVQkbYXif77YtJIcn6sQq-dnM1dAjTZq77Pz_yaH1F1d9ulRTJOa0QTueX07LeOTLRSh0Or6zAEmU9qwyNrdek9OoYJyp2hO6OB3QibQsSQAfHw3ck14lGaTZCSVT3MxVnGrzdl-qD0dduiukk-3iMKtLSZkVCQBufJNxkjzSOYl3IRCNnUXgmwSXxzAKRT5Fki7JijZu4Ix8yB4gGkBBOcHbnXAr24bSBQ_BRKr3hcvSy9-xQPk3R0EkIlinFnTDNUJUtP-J4KrHE67ZnMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار آلوارو موراتا در مراسم معارفه به عنوان بازیکن جدید تیم‌فوتبال لگانس
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/104995" target="_blank">📅 12:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104994">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2hjdtF_YIMIlK9YQ6S85RQoRYvyMozDoqts7OGWRrjX-mAjs4_NulC2avSjtQUv6cOPYJ6RUGVFQN3ACvLxh3ws9mQoe8PiLeOHh4E0UGNzQvpB97uekws1sSoQbFhN8pu9oMJ9r6l2qMUt6H5c1AQKd9XHoyVi_mv6AJcg5fwwfG6GOxMiQ37hzd5PU0G7chXtMLbhh3-VkauDl2MfsV7WMk5HMu7gioIj41dOXEZhoykD7kx-MxoNlG7WG9dZj7NR8MSdb7elYj0Hdo2h3wP7uHf7LvGJ81uXPAMrLhysxaP43ou8kzSXgs_X1WL5VT8cR3iLOSib1m2nYVZUqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇪🇸
🇪🇸
خولیان آلوارز از لیست اتلتیکومادرید برای بازی امشب مقابل سویا خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/Futball180TV/104994" target="_blank">📅 12:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104993">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/694fb72f97.mp4?token=VL6u0qsJbmGgTpzqwqnTsQt8LY3IDorY8kcg7sK1CoGhT-p4-esgzaH1wlIZn1Mrzu-P0lr8yIiqp0OCqnB83jlY8hbV_29h7XB5qMRFvXM97U7fIXmsARTVL_Ev9USOq19Vbth_oePg-HOsF_tOwRIBWoJcCLIENEM62PRkeRGq5smXRlhdZjWOeGYR573RDFSdLl7UkvdYKRrRlxn6GQBPzpLPYAutrb4G5UJqFdYF_N1o8cqilZVqTfglrnZNOfIN9y2Y7cK284Lkd0pquflt0alMDT9M5wzbmFBRDD66XEUXzeURMg9k8X6T1JEKS4WnJqqjpR77XQ3pWMq0OnnBFs8jzSKEK9s_hNer4WhM0HplE_l1Ci_0x1kDn4jZhC5U4BPJGC6jFvw3PVRrt-dXyKL6-D2GulHNrtIGLVFI2Iv9hdBVOClHakPvSHBWer_W_hiHO-sFGRjY-Vz61Nv8jTPKg1J7Np_O-tqiC2EMdMCQq0QPOaIommBSxcHwHMulqpaqTS74XZ7twYc52NTO89fnhQtTKIylJIJfvq3Rm4Drd7v0nnq72FNqxt67kl73CtVxTGq6Bpa7P1hgLyvtfQleeqkw5RRidiVoiYqIAOMAcBrt36TFxAin5x7cT6isXsPcBwSMOVG5-J_jPLfIDSi2p-_IJ4KVsoRZnbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/694fb72f97.mp4?token=VL6u0qsJbmGgTpzqwqnTsQt8LY3IDorY8kcg7sK1CoGhT-p4-esgzaH1wlIZn1Mrzu-P0lr8yIiqp0OCqnB83jlY8hbV_29h7XB5qMRFvXM97U7fIXmsARTVL_Ev9USOq19Vbth_oePg-HOsF_tOwRIBWoJcCLIENEM62PRkeRGq5smXRlhdZjWOeGYR573RDFSdLl7UkvdYKRrRlxn6GQBPzpLPYAutrb4G5UJqFdYF_N1o8cqilZVqTfglrnZNOfIN9y2Y7cK284Lkd0pquflt0alMDT9M5wzbmFBRDD66XEUXzeURMg9k8X6T1JEKS4WnJqqjpR77XQ3pWMq0OnnBFs8jzSKEK9s_hNer4WhM0HplE_l1Ci_0x1kDn4jZhC5U4BPJGC6jFvw3PVRrt-dXyKL6-D2GulHNrtIGLVFI2Iv9hdBVOClHakPvSHBWer_W_hiHO-sFGRjY-Vz61Nv8jTPKg1J7Np_O-tqiC2EMdMCQq0QPOaIommBSxcHwHMulqpaqTS74XZ7twYc52NTO89fnhQtTKIylJIJfvq3Rm4Drd7v0nnq72FNqxt67kl73CtVxTGq6Bpa7P1hgLyvtfQleeqkw5RRidiVoiYqIAOMAcBrt36TFxAin5x7cT6isXsPcBwSMOVG5-J_jPLfIDSi2p-_IJ4KVsoRZnbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین‌رضاییان دیشب قصدی برای خوش‌وبش با نیمکت‌استقلال نداشت اما با توصیه ساسان‌انصاری به سمت نیمکت‌آبی‌ها رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/104993" target="_blank">📅 12:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104990">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHvFXNJP6do5y3-Eb6xjW7x-09JQfO201mArO9781Tly1Oh-sA8Of6jdXtktRz4-z50mCllnTqLJKMF9kgj9G5rdkqx03Yz_r4MQDMUqNI0yCcDastl-2sIL4DlYCl7XXdkb7IGxoVA3MCOabJ2ylsctJb1edVJcWBLaDb_xhPLo5GZ9ygZPH2ADSJSfGxI7VXzfYKwbgz57fSorDzg8yIWQDGC3QwE9dzK8ztlaCGTXLo7_HSXp651cfzjfvEx4K7bUcHhXcm3LIwbEVosbU7oqBTSe3GJKFkS3YDHBrlafP4OA2CwjvwL9QF22zOHcK5W7qgDZDPpRkEO632L5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wco_HfPqpCUyLl3tVLjhutkyaKj0mwG9UE1Yd0kjkOdb9HuaCF0wOEGMj26LJoLQrPk20QfRyCG0-5FllbPKCPwIhAyZCF0QSpNx4sVpXh6lQwaZB64RmsZXmDxDc7H02vxIbmcIjXFUP4SGAN5RruwYaQ7yVL7zLFQXsegXEIF-KGcKqyEsYtZECd4p_1apUw9kLcXJb2Kz5cdQhaZ6MkQnDL-7pw-CLS1xBYkvugtZMk4n9EpOW-AEPFbge8zQEXjj0O2mVAAez9n-uPHLxS-wKnI7JyAx7tv-6qW5oxmApvvK9-o7MCIltrOoy6Bqz907otzg2FXX7Sal1Bdg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOY9Ohr-bmuaO6xf86Vv8uofBPjEZWLeq0csZyN0OuyPsPmUOmvzsHu8BSu6skAoU_w5q9xClLgLlWqaf2KLAYQXlSFLo2b2iUbJGVv7C8PUDjlYwF2G-OXaFA34ExOOYGRrCEOCGNUkfCTggliM6WpWXAHOdzOk75Z7NbmKB8pv__J3lU8w7S6I8nrvrVxTNy84tHANLRfJvigOf3QrzQVrkmNdvw_1POiZ75HJKev12UKJh08nwpXOZHi6TeHkCSqpalChC42mHK6UB6fH3Qhm5CPEpsCVPGpFkSl3pGf16GRFXfbblp34vpio3gcHbARa4sfJYoAePqidLAKJAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
گابریل آرتتا، پسر بزرگ میکل آرتتا، دارای یک ویژگی نادر به نام "هتروکرومیا" است، به این معنی که چشمان او دو رنگ متفاوت دارند.
❤️
💎
🤯
فقط حدود 0.1 تا 0.2 درصد از جمعیت جهان این عارضه نادر را دارند. یک گوهره‌ی واقعاً کمیاب!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/104990" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104989">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104989" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/104989" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104988">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6zXQHN8cS37EEzi5bwBSYLmle7xqTsPo2EWJgslgr-2bdl5Gr575202Ec42TxYEPcCJD_JtQ6pRXrLwsQY_aqqiCIqJgx2FgjjbekIqlZPBz-L-wmfa2_Rw97OzJF4FXt-MI06Dm3yx8wZfxfh9NE7leDM0SWwaLMsqwHlcX68opQngJS667jg46HbAcw2ee0FfSEJ1CmSVudPX-TlGjZqtDYvS2xRG1KP9BUt54TfNRa3GTFeAJZS3uSQCpZYFvbUbdXaKeWc_ur5hKFkgz0NsVfyvl2uFZrlNFCazKxqazWCtQHTvIOv8in7Vdtzfx3vxIVZavw1FByQo4ipqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
پرسپولیس
🆚
ملوان
را در سایت بین المللی
TrexBet
پیش‌بینی کنید.
🦖
دوشنبه ساعت ۱۹:۱۵
🦖
استادیوم شهر قدس
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر:
ملوان: ۱ برد، ۲ تساوی، ۲ شکست در ۵ بازی
پرسپولیس: ۲ برد، ۳ شکست در ۵ بازی
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/104988" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104984">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4df35536.mp4?token=asJUN6KF22MyGo9ARNiHrKtL_dtNiX1HGiR9poZTr65-BB8oWJsr_TkeQYG0IJcUogjc5znRsW4B5BY7e6KJ82KbO1xB4eb0wtRfrHmIUTCjul_A6TU0GBgvYPOeR-vNGZYSQk3cm03ttUA_RLth0GeF6R4yWcwIv6Eh1osuBiHz7IH3n-Je8DnXtnyk9BBOgaxHUoQeulLq6B7ZXGfiXK4od1frDo-X6oEctmJ2sfr4AZltujF59uQUegvSpZJrMq_Vq2_F_TROJtKxsmV2sIStN1a1rqAQJuoiUsWzZUVK0uu-y8kjW5b4EAi80j-01Qu0sa-9lbt3D8_JEqGuVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4df35536.mp4?token=asJUN6KF22MyGo9ARNiHrKtL_dtNiX1HGiR9poZTr65-BB8oWJsr_TkeQYG0IJcUogjc5znRsW4B5BY7e6KJ82KbO1xB4eb0wtRfrHmIUTCjul_A6TU0GBgvYPOeR-vNGZYSQk3cm03ttUA_RLth0GeF6R4yWcwIv6Eh1osuBiHz7IH3n-Je8DnXtnyk9BBOgaxHUoQeulLq6B7ZXGfiXK4od1frDo-X6oEctmJ2sfr4AZltujF59uQUegvSpZJrMq_Vq2_F_TROJtKxsmV2sIStN1a1rqAQJuoiUsWzZUVK0uu-y8kjW5b4EAi80j-01Qu0sa-9lbt3D8_JEqGuVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تعریف و تمجید حمید مطهری سرمربی فولاد: بازی هجومی استقلال باعث شد تیمم مجبور به دفاع کردن بشه چون تیمشون در حمله خیلی فعاله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/104984" target="_blank">📅 11:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104983">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📹
✔️
⏸
تحلیل داوری سه بازی مهم هفته چهارم لیگ‌برتر فوتبال با مارک کلاتنبرگ
🔸
چادرملو - تراکتور
🔸
(امیرحسین حسین‌زاده باید با کارت قرمز اخراج میشد. همچنین یک بازیکن دیگر گل‌گهر هم در ابتدای بازی باید کارت قرمز میگرفت)
🔸
سپاهان - گل‌گهر
🔸
🔸
فولاد - استقلال
🔸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/104983" target="_blank">📅 11:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104982">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0aBx_EIFgiJlZZXU6h-qLMGmm5BFQ-I_Ky14uuEh_CghvdRPCJHBCqP8mXG7TPI14WQm16ykURQDSo7nHiOPtWkPuTddtDpuBbiz3MvyGkX5mLZ40qtpysQdHdPESOe_uwpTQXswh5XrNp-z109BNWfk0k3tqemJBhAxxi2qB-9BxJyua1j7LeXLVd18WN-ZDbpcYqc0gTI6Hi3s5K8adDEwZmPbSKxdJ7uTKrkx8nDXTbY-bmRKfnJGeu6oxFya2VAY_fRpXCpp4R-hg5xwNvrTxMmBhEUubTWxvYYd3cO4T34kavhpKmcOdDHRc-aPpJgSoh8MXMjFb4yw_8xfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
صالح‌حردانی و رستم آشورماتوف مشکلی برای همراهی استقلال برای دربی ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104982" target="_blank">📅 11:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104981">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f929791585.mp4?token=M7zHG-y4k2YKa8nnPrSaKlHE9qlUtHw59vo8oAnR6Fl6BsbkYhrT-1E1zNijGWOsyBl1ukvGD1gqvUOneyz4Aql-DoA7m74kzADbXclJUSnvb57-L4V_itUjNZzYXtOZhErmTz9jw9MzfCZAcZjqdWa-4WKPB7s1C0pvJTgfcQp7rXDVyO4LUcxOLcUD47-KP1JrpT0VaVeZJXZv1aqp_TeJj4RbkNnUoI-4RjcfjO6mFav8XDGUuFwlWz0OfFlj3meN7aty8o4sPtUoZGaQ8QpDAfYkRKDqkYwrUNqFMj0jHaG2Wt7F6qijzRBJmHhbY7TaODHFhwGE7BAWF_O2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f929791585.mp4?token=M7zHG-y4k2YKa8nnPrSaKlHE9qlUtHw59vo8oAnR6Fl6BsbkYhrT-1E1zNijGWOsyBl1ukvGD1gqvUOneyz4Aql-DoA7m74kzADbXclJUSnvb57-L4V_itUjNZzYXtOZhErmTz9jw9MzfCZAcZjqdWa-4WKPB7s1C0pvJTgfcQp7rXDVyO4LUcxOLcUD47-KP1JrpT0VaVeZJXZv1aqp_TeJj4RbkNnUoI-4RjcfjO6mFav8XDGUuFwlWz0OfFlj3meN7aty8o4sPtUoZGaQ8QpDAfYkRKDqkYwrUNqFMj0jHaG2Wt7F6qijzRBJmHhbY7TaODHFhwGE7BAWF_O2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شاید تمیزترین و بی‌نقص‌ترین اجرای کل مسابقات جهانی ربات‌های انسان‌نمای چین در بخش هنرهای رزمی باشه، آنها آمده اند که بمانند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104981" target="_blank">📅 11:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104980">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8294617ce.mp4?token=gGfKcoY4SLjoSfnXkaqrN5OY-5HaaLro0d1MkjIAVRqM6UJ-mAhpE3q2Wa1A0QO_DFQunQck-S8Wl-56dZeXANs927zMB9NP3sOW262qVK8dkCp77OK95WiJKbSUHZesxUFOYBI6lxydr4s5fkvqq4bG4R_GfXWL_siklWF-0R6ilAGtnNUWPCyugiLxmTz7YDeqLP2Fe3YB3aFZMpqVN_fqFLUAsaQB_Qo2Q9HbllMy7ZQ3kCf24wNgyFL6ZO1JAzUm0GazBFRXXnoQpKbFvK_LiDbUFVEvZSv0b4t6GFbOVl9uvmJ8bLbrGiYBezHY8hq2KDHxqZfiarmJLZSt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8294617ce.mp4?token=gGfKcoY4SLjoSfnXkaqrN5OY-5HaaLro0d1MkjIAVRqM6UJ-mAhpE3q2Wa1A0QO_DFQunQck-S8Wl-56dZeXANs927zMB9NP3sOW262qVK8dkCp77OK95WiJKbSUHZesxUFOYBI6lxydr4s5fkvqq4bG4R_GfXWL_siklWF-0R6ilAGtnNUWPCyugiLxmTz7YDeqLP2Fe3YB3aFZMpqVN_fqFLUAsaQB_Qo2Q9HbllMy7ZQ3kCf24wNgyFL6ZO1JAzUm0GazBFRXXnoQpKbFvK_LiDbUFVEvZSv0b4t6GFbOVl9uvmJ8bLbrGiYBezHY8hq2KDHxqZfiarmJLZSt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
چرا در آلمان از کلمه قیصر برای پادشاهان‌شان استفاده می‌کنند و به فرانتس بکن‌بائر می‌گویند قیصر فوتبال آلمان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/104980" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104979">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c7fdcd83.mp4?token=FEfyphmbT932BRXFqO-mtVMu_amJseKgrIodmK4002SesnuY_j3d2CR94v4JNMN2dEjv1HlbZ-C3d8SOjmZ_bp9xXHyNM9NiKmw6FUnbPj1MziQJcjJRZOXJEmq3JU-0D-XdvA3jh7pDL1cW-w20PtiiwUnuu5P7Spysd-oEl1b8jwRwMZZ3zqtbEEl5xM64j0O-5l6GDLkrrvBQbj1GG6tTBYemtPYvpX-7qc21E0xB854Oaw7LA-gcXelqsCV1O0c_-apE7p3PtL2GeOJ8y8WFvXL-cttij3rgxAMoFOLKmWYgH9DRMP_w7IhiKIN5VqFpWw6Muz2vQr_nsqORAZc4e8YIOnCWK1uXhlJKDVDjiqGuzQ_gjzl0hJG3WGDmiD94yiisjJK42Bb8fOS3fZYk9j8y2lEj-xiL3DANpVC0uuBrQieoOLSxouHvntrTXnGP37rh2O0PRWO28T4WQjs9wsUgFYvlrQ6GIWmQ8Rcx8eKTmJ3QsdSuXGpzwP_xNYG-lN-3eZJAgfT5C7w4HInE4x5o_ABG78ZE4ovY9ryfRm1eiVeSCILtcP6xctTrlBJ_FIcHmCRBLctUCxzRQSyc85TPcGc0YT_k3oXl-DBUXhEqogrJFfmktze67DfytNz2UgJf7vsQT7PkZjI2RtO1Y4BczoVSaoko_fO848U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c7fdcd83.mp4?token=FEfyphmbT932BRXFqO-mtVMu_amJseKgrIodmK4002SesnuY_j3d2CR94v4JNMN2dEjv1HlbZ-C3d8SOjmZ_bp9xXHyNM9NiKmw6FUnbPj1MziQJcjJRZOXJEmq3JU-0D-XdvA3jh7pDL1cW-w20PtiiwUnuu5P7Spysd-oEl1b8jwRwMZZ3zqtbEEl5xM64j0O-5l6GDLkrrvBQbj1GG6tTBYemtPYvpX-7qc21E0xB854Oaw7LA-gcXelqsCV1O0c_-apE7p3PtL2GeOJ8y8WFvXL-cttij3rgxAMoFOLKmWYgH9DRMP_w7IhiKIN5VqFpWw6Muz2vQr_nsqORAZc4e8YIOnCWK1uXhlJKDVDjiqGuzQ_gjzl0hJG3WGDmiD94yiisjJK42Bb8fOS3fZYk9j8y2lEj-xiL3DANpVC0uuBrQieoOLSxouHvntrTXnGP37rh2O0PRWO28T4WQjs9wsUgFYvlrQ6GIWmQ8Rcx8eKTmJ3QsdSuXGpzwP_xNYG-lN-3eZJAgfT5C7w4HInE4x5o_ABG78ZE4ovY9ryfRm1eiVeSCILtcP6xctTrlBJ_FIcHmCRBLctUCxzRQSyc85TPcGc0YT_k3oXl-DBUXhEqogrJFfmktze67DfytNz2UgJf7vsQT7PkZjI2RtO1Y4BczoVSaoko_fO848U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا پرز بعد از هر قهرمانی رئال در اروپا به مورینیو زنگ می‌زد؟
چرا رئال دوباره مورینیو رو برگردوند؟
و چرا پرز فکر میکنه مربی شر ضروریه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/104979" target="_blank">📅 10:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104978">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/181464f819.mp4?token=uPVqtin4IgTil75rNtDX5y3h0YlXiQReybco_48pypFT_VUTmy2fy30-PvcvBzabM-yYgIY6UcWfQvoGbHepudDkg5TfdszPueQCEnueTjioYHsjCo43EM7NSHLbQXhN6B8BcIQMrQV7IhXtkkj0746gWsB2A-l4FmU_mzwYwB1y4k50ZhZIIJlJT7FjgGZFEssValWy6lA98EvKULAxMw6m2GP0oAdMqw8Xh96t_H-DKDSLgdsH5o3aiO_N3ePyTEN2fRLOUUni1Kyz2nMblk_UL0mN1vXw3Fh0JTWUhNQyApBaLZFig3XgE3vQszrE120CMGBpTZ40WU6WKKkoVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/181464f819.mp4?token=uPVqtin4IgTil75rNtDX5y3h0YlXiQReybco_48pypFT_VUTmy2fy30-PvcvBzabM-yYgIY6UcWfQvoGbHepudDkg5TfdszPueQCEnueTjioYHsjCo43EM7NSHLbQXhN6B8BcIQMrQV7IhXtkkj0746gWsB2A-l4FmU_mzwYwB1y4k50ZhZIIJlJT7FjgGZFEssValWy6lA98EvKULAxMw6m2GP0oAdMqw8Xh96t_H-DKDSLgdsH5o3aiO_N3ePyTEN2fRLOUUni1Kyz2nMblk_UL0mN1vXw3Fh0JTWUhNQyApBaLZFig3XgE3vQszrE120CMGBpTZ40WU6WKKkoVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
درخواست ۳۰میلیارد تومانی مربی لیگ برتر برای حضور در تلویزیون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104978" target="_blank">📅 09:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104977">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e6b721d.mp4?token=GWvFsC6niVkGQYbEeXJP_pgx-Ol46TAbqWPEKVfSfDcMZ-8zaIkkdaBhF8u7CoSL9ldTAjRjk9t30PEdCgUq9y8T5fDdYYqT7rkZv7HyCnVksmymRD0tPqoHllR4hEvAwJblHxQz-igQ6H3tCnqSU3ZfTEA1o3ScHB3huU84gZcQ3IDyDcVfTccvLffHzy48-kx7orZjesLGEzCEGu1U9-xA6q-4KydxA7C2U2jQEpvmMcDT8fhOKfmSFvkceWZrVmGyeM_z4O6C3QpTJwWKx29dhdLULZ0HV4ZJKT8fF_3ccBAbvgIghmTaq4GrDIUzqkJDHv2HiYInZePpfMCdEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e6b721d.mp4?token=GWvFsC6niVkGQYbEeXJP_pgx-Ol46TAbqWPEKVfSfDcMZ-8zaIkkdaBhF8u7CoSL9ldTAjRjk9t30PEdCgUq9y8T5fDdYYqT7rkZv7HyCnVksmymRD0tPqoHllR4hEvAwJblHxQz-igQ6H3tCnqSU3ZfTEA1o3ScHB3huU84gZcQ3IDyDcVfTccvLffHzy48-kx7orZjesLGEzCEGu1U9-xA6q-4KydxA7C2U2jQEpvmMcDT8fhOKfmSFvkceWZrVmGyeM_z4O6C3QpTJwWKx29dhdLULZ0HV4ZJKT8fF_3ccBAbvgIghmTaq4GrDIUzqkJDHv2HiYInZePpfMCdEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
سنگ‌بازی دیشب هوادارای استقلال و فولاد حین خروج از ورزشگاه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104977" target="_blank">📅 09:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104976">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75514852e3.mp4?token=n7Mrf6lzHf44BTO8lddZmB9zbVyfONzkCpuqL1lKHmjRpH0ThiH3E4R104k8IvKQiriehHv8IcZV3QyMUj3vEHYsc2tbfTmGdGXHPjguyLLlF6ld4BB1e27GvH1sH_kZBytP78NYC1t4cm8OJ6htmQVj9BHyZNFLM0KsERTNXDyNkbSWaYPOaumyiM6jKK-T-J8M8m4DKOmSJr6YhElmlIYoKHqMrixKVxR-LMI5NtG7YSHrbAgWVR5k3-B5ozvfg8O4r6ZN_YveCnMtDFRb7704vZAtl2G9JxU1-OUTJc3ebCu_OlbSeWJYC7iXzgWLncBj4CIWgnApDjg1hApRCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75514852e3.mp4?token=n7Mrf6lzHf44BTO8lddZmB9zbVyfONzkCpuqL1lKHmjRpH0ThiH3E4R104k8IvKQiriehHv8IcZV3QyMUj3vEHYsc2tbfTmGdGXHPjguyLLlF6ld4BB1e27GvH1sH_kZBytP78NYC1t4cm8OJ6htmQVj9BHyZNFLM0KsERTNXDyNkbSWaYPOaumyiM6jKK-T-J8M8m4DKOmSJr6YhElmlIYoKHqMrixKVxR-LMI5NtG7YSHrbAgWVR5k3-B5ozvfg8O4r6ZN_YveCnMtDFRb7704vZAtl2G9JxU1-OUTJc3ebCu_OlbSeWJYC7iXzgWLncBj4CIWgnApDjg1hApRCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
🇮🇷
تشویق دیشب اسطوره علی‌دایی در یزد توسط تماشاگران چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104976" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104975">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
سوتی فوق‌سمی یاسین‌بونو و کولیبالی در بازی امشب الهلال که منجر به پنالتی برای حریف شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104975" target="_blank">📅 02:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104974">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aac6582ca.mp4?token=R7J6cwfpg16Zn0vVazuPxjl5kglClGWl7b3KvjxLQXXNH5idK8f5DwIIvbBEoj0pTPJg0Dlwc_AH5fqHuYjy8MlAhrss0GVPiSVJ8sWbikNc9weB7HBO4vRYxmKtVbqZhmWmkre6XLE7NZVfqEqXMnLcxoOPn2m64Xrwa6nejV7Doyqcs-MM9uo-kBoWkOkR2mmtoh7BgB50FH03kgSL-N1HlLYpp4RhwaHW-K_vwt9GMsBPEEiurI7ylYstjI_Y1H84WIzf_FiS-_pOu4yhEtQSXnRCJTQg9q_-WHXdOmd7jiZlyUtV53m-9dF8GCGxcnZqRxyOTmw37XnP8fDgLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aac6582ca.mp4?token=R7J6cwfpg16Zn0vVazuPxjl5kglClGWl7b3KvjxLQXXNH5idK8f5DwIIvbBEoj0pTPJg0Dlwc_AH5fqHuYjy8MlAhrss0GVPiSVJ8sWbikNc9weB7HBO4vRYxmKtVbqZhmWmkre6XLE7NZVfqEqXMnLcxoOPn2m64Xrwa6nejV7Doyqcs-MM9uo-kBoWkOkR2mmtoh7BgB50FH03kgSL-N1HlLYpp4RhwaHW-K_vwt9GMsBPEEiurI7ylYstjI_Y1H84WIzf_FiS-_pOu4yhEtQSXnRCJTQg9q_-WHXdOmd7jiZlyUtV53m-9dF8GCGxcnZqRxyOTmw37XnP8fDgLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
🇮🇷
مصاحبه با خواهر صالح‌حردانی ستاره استقلال بعد بازی
: کل خاندانمون استقلالی هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104974" target="_blank">📅 01:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104973">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQB7JuSl4nVQUpAYBMNYRjgRp1a14W11AD1IJZ20JzVjDBEopNzKW9FPaT02vic1r9_Z98LEijPzcuQ9dtwv-0IJMbF_IEfwVz7Yxgn8DiYsjJwdHlSdljvwTo2Iec_sEaa9mnXaFpWs5iMwnE45tqNhDqzdEmg-Jon9aZ3Di28drKFr4YOwpyjDCRiTWkKB7Kl9e6fkEp-8YfKWvB_BUsJKkd4k8lxu94KeEnv6a1S_1AbgakD0sQ-Wv4kYCU13EkcVQyZHHHQArcQYWMw1qVjvRDTy3zl_UVMRUAo3zeYWuWVaR6c3dzNdrlcPWU4bOJpQFKmvBRjPgNkw3mWmygns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQB7JuSl4nVQUpAYBMNYRjgRp1a14W11AD1IJZ20JzVjDBEopNzKW9FPaT02vic1r9_Z98LEijPzcuQ9dtwv-0IJMbF_IEfwVz7Yxgn8DiYsjJwdHlSdljvwTo2Iec_sEaa9mnXaFpWs5iMwnE45tqNhDqzdEmg-Jon9aZ3Di28drKFr4YOwpyjDCRiTWkKB7Kl9e6fkEp-8YfKWvB_BUsJKkd4k8lxu94KeEnv6a1S_1AbgakD0sQ-Wv4kYCU13EkcVQyZHHHQArcQYWMw1qVjvRDTy3zl_UVMRUAo3zeYWuWVaR6c3dzNdrlcPWU4bOJpQFKmvBRjPgNkw3mWmygns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فراز فاطمی سرپرست چادرملو:
🔺
آقای پیام حیدری فکر کرده ما خریم. قشنگ بگید میخواید یه تیم ببازه دیگه اینجور قضاوت کردن بخاطر چیه. امیرحسین حسین‌زاده با تکلی که زد دوبار باید اخراج میشد ولی حتی صحنه به وار نرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104973" target="_blank">📅 01:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104972">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa1d6121e.mp4?token=Xn8lgU6rc5a24O0CTnGaf1nouT_dXQB0eaDJYZ_mmWC2jPNrUthZF6LYPEyk45_RR4Lm8DYxc0jN7qAEg-zyJSmjzuEZIl_CprCeEuk6gkFkCOsIThRLri__iHbpewFrcbcS1RPAOBpe6jIL2QVPmYWoFwslKtdjnyEhXV7DtW1yYnFSavnciZLJ3CQNsn1Dp_HgPnLJVYVD0Llp-Vn7sah2UD7LdObi752ISs-m3baXoANpRMcYUoGwF9vND-Hv2oHZ6yiUWM2Qjf64JupbY9A-xRFgtJeoZCOHFez5atVveibuW8bIGpohJrLgfkiZN0u6FVk_0YR5DQ0g8oDx9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa1d6121e.mp4?token=Xn8lgU6rc5a24O0CTnGaf1nouT_dXQB0eaDJYZ_mmWC2jPNrUthZF6LYPEyk45_RR4Lm8DYxc0jN7qAEg-zyJSmjzuEZIl_CprCeEuk6gkFkCOsIThRLri__iHbpewFrcbcS1RPAOBpe6jIL2QVPmYWoFwslKtdjnyEhXV7DtW1yYnFSavnciZLJ3CQNsn1Dp_HgPnLJVYVD0Llp-Vn7sah2UD7LdObi752ISs-m3baXoANpRMcYUoGwF9vND-Hv2oHZ6yiUWM2Qjf64JupbY9A-xRFgtJeoZCOHFez5atVveibuW8bIGpohJrLgfkiZN0u6FVk_0YR5DQ0g8oDx9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🚨
معاون اجرایی پزشکیان: شخصا اگر میدونستم آمریکا قراره رهبر نظام رو ترور کنه، دست از ایدئولوژی‌های خطرناک برمی‌داشتم و غنی‌سازی رو حذف میکردم چون عقلانیت حکم می‌کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104972" target="_blank">📅 00:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104971">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujP37uQHlUQ0R_LgJ28kwkMcgMjtJcchzRVbDG0Phf8SwRqS9o-XgW6adNTFmVffSPqiVv9f_EMMkk8SNmKEyXPLs022eLkzi6CtEDZBZkFbcB4pgTIc8EKYDkHp_iEvZifGv442BkLeGFDrfzbZdNf-VC2soD3lmPDqrxSxoazKcBopGYtPR2Ah9efwM6Bxh04hc_7zceWXtX_YChTZq-VbsJROcnPBT71I7DsLp7jjCw7CtIDradG3fm-rG3BIrsPnsvj3hCWfmVWsDG0B98b3ZYJffZQR71XDe9yLG28VMCWI6zHdCa2l0sCi9anpk0sFgu_2Aeh05aJfrfbKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
هفته‌دوم لوشامپیونه؛ انریکه همچنان در حسرت برد؛ لیل موفق به کسب امتیاز از قهرمان اروپا شد!
🇫🇷
پاری‌سن‌ژرمن
😀
-
😀
لیل
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104971" target="_blank">📅 00:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104970">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzminsONL_Xj5y-5xiXwnkZroiSlGxMbiINqN3w53867U3LnLvwN0vmbIxfDc4x7TlxSld2mWDOotrZXX_WQ2oZRfrIiR6BTpMfWa9etLPwhBOrPQuzAYSiUxk7-jxPHAA9UivEIsyBMFdJ4UjP2WFR6omIZZaZzWXtJa-eVuS7t4J4_hApp66hF8ak1QgH0uSuTosjPvDzIwh_Okb3j83YlQ_bG2Wt44r2_d2GtIXuLhrheCh7DGFgqbkMxEvnbfJOoH4eOS-1ZAdVb0FlD4GGUjmugtot9BzFGvKb5x9SXOx0J6hO4idNJPyPD0212jHmcww3KP5MZt-y8nycJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ پیروزی پرگل در خارج از خانه؛ موتور گلزنی هالند به موقع روشن شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
😀
-
😃
کریستال‌پالاس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104970" target="_blank">📅 00:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104969">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA-wip4WFJ5P8_Nqt7ADrD3hIhTN5s77gXa2dem9Uhm4BR03PtEhAEILfaG4nN9eB_EaoPpSsoz2bRELBgcHzebbn9OcgpLyJVJM4k0Zq7GntAAjxnWClbjdJZpbEuNQYoRajJGTmzA1onbM3kj5FqFk4hbMOO2CT6uB9eYOcobXJzv1nGvRnFAislHhtbJwWgLUodF3TVtFz_0mnoJiWEqHhA_XgUyCKx4P_eCeZYZza2_VzwoMiz6eaN56NIwFjIsErzg1bO9pa0Z3gR8EVO9SR1Clp0x3Th9kIbUJfuUdx0RDF8ILOkGj5JRnW2Vy3681CMNeq1bnwgjrZ-ASjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
هفته‌دوم سری‌آ؛ پیروزی راحت در خانه؛ روسونری با مهاجم جدیدش دلبری می‌کند
🇮🇹
میلان
😀
-
😏
ونتزیا
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104969" target="_blank">📅 00:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104968">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=aN4q7m30gUYdERjYvY1qTZ1MKw04J6te_31aNQhesLeBpMaE2nDknFLJARfdme2LmpHoyCtxErbrcGMBveRQCDP88aFNAuKCZpebevAWbt_WpPlbigU3b8dAITDyi8g4RneQca6TjQfWW-B-sXVWFQwnTeI6YXYojBm5Ta0FJ_pvRm9LWaddHV1Akh6wauhv9MhBALp5WsM9RCBQB6LuvweBZ-8Kms3Naml4rm07LRiNYDhRoK__b2qtvVmZJQmJF_bkEzrebusrD26lfWftIuVZidrtG01OKdq1Vph__vKvpVids9Blkm3s6yFs-A1CuJZtnDmA-vbIUBwvJIERHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=aN4q7m30gUYdERjYvY1qTZ1MKw04J6te_31aNQhesLeBpMaE2nDknFLJARfdme2LmpHoyCtxErbrcGMBveRQCDP88aFNAuKCZpebevAWbt_WpPlbigU3b8dAITDyi8g4RneQca6TjQfWW-B-sXVWFQwnTeI6YXYojBm5Ta0FJ_pvRm9LWaddHV1Akh6wauhv9MhBALp5WsM9RCBQB6LuvweBZ-8Kms3Naml4rm07LRiNYDhRoK__b2qtvVmZJQmJF_bkEzrebusrD26lfWftIuVZidrtG01OKdq1Vph__vKvpVids9Blkm3s6yFs-A1CuJZtnDmA-vbIUBwvJIERHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104968" target="_blank">📅 00:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104967">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzOQbSvHEu93Aw3V-qmxbBMrEM5l_eIWFY92YZ6zouKyUVOlxNCAzr2H7Xinj4tQ-ClhOfcRPGms8kjeJmXJ_iNDqesc6lDt9BuNOwpvORMJvfjMDkhyMGmKm9irt8XwfSt2zZCtTLl-wbG97qEH_lVXI3x81VYxzQNLWNglpeReUJ_Jy2U9SczzDFKfaoZmduSRlWvbI2NjOgANMr0RF0wUVirU71krTrtbDmOu6L2Wbvft0rNss93BRsbrjiTZPixr_rZu4qw9mNbwlWT3jVNvehKawfi3ymACZgkDzxjk76IIfJzZtShzZzI0FCs4x4APRgs9p36wqvA-9RXSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇩🇪
هفته‌اول بوندسلیگا؛ موتور گلزنی خشن تیم‌کمپانی با قدرت لیگ‌را آغاز کرد!
🇩🇪
بایرن‌مونیخ
😄
-
😃
اشتوتگارت
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104967" target="_blank">📅 23:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104966">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e92dec0fb.mp4?token=d1GiOyR-_vuFFtI0h3P3TG3AtUa-1fJ_tTamOhNHU8oovRxYP1VLRioo_3qrunoTAHUPgUHVGJj8eaQjt7HIsVxDArYB5h7gBOK0dzrGhRpDOmxWsXi1LNw8CAV0ZGFgea9K1bnaSkALUN-K2nq9RLi1SmYbf-viuqvWoBAHTJ3jdiLAIIr99ifbbeOT5I6ZQSTZFnAhCcjDVGyumnYoqHAjFt8HV6UEwRIta-LWiCUmpgQTnhhdzDu4dfArZ3AQ47WLlS6VOb07vg-Z3B3gY_ntH_hQr7iFs2BaJ5w18pnRUKq-pTuZy1c5Vwj0SpowCX11nXFVewsYpFlRqzzBFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e92dec0fb.mp4?token=d1GiOyR-_vuFFtI0h3P3TG3AtUa-1fJ_tTamOhNHU8oovRxYP1VLRioo_3qrunoTAHUPgUHVGJj8eaQjt7HIsVxDArYB5h7gBOK0dzrGhRpDOmxWsXi1LNw8CAV0ZGFgea9K1bnaSkALUN-K2nq9RLi1SmYbf-viuqvWoBAHTJ3jdiLAIIr99ifbbeOT5I6ZQSTZFnAhCcjDVGyumnYoqHAjFt8HV6UEwRIta-LWiCUmpgQTnhhdzDu4dfArZ3AQ47WLlS6VOb07vg-Z3B3gY_ntH_hQr7iFs2BaJ5w18pnRUKq-pTuZy1c5Vwj0SpowCX11nXFVewsYpFlRqzzBFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
🇮🇷
🇮🇷
محمد تقوی، ایران‌اینترنشنال در برنامه هت‌تریک درباره تساوی استقلال برابر فولاد گفت:
«غیبت آشورماتوف در ترکیب استقلال باعث شد تا عارف آقاسی کمی با مشکل روبرو شود و نزدیک بود با اخراجش شرایط استقلال را در بازی عوض کند. همچنین بازیکنان دو تیم در ضربات آخر بی‌دقت بودند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104966" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104965">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104965" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104965" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104964">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spa9MByUMNf_dr9OIEqJIrgBxA4rOEmXRPSVdA0zzhJNIbbXqeW3bBm7Ruv5y9ZAIcppdYBGXDOZ50kAq5tCpLk83rIDPgy7QMqfbRbTIjLmSUrUKLYQwnqbg3rB-SDmOgX9cx3lvIE0HYXZv3lXkV85SHK04607F80vOztIHZIkcSKQ8OIojxZ7xk-hc-VrrBmvrNv7p2WgDSLzDsfxm5DE1YoUptNZ1m9QFXCMSLvyBvCCr4Fk82-GpOzYSbcsgKs7hV292leoVegr9yHa_Q2Cs5sNLN3vA0MRAUZo8mIz-egjhSPLOD3X-7ErsImKi4wgTtEvx2fj7wkrKEybow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104964" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104963">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c196e7e0a8.mp4?token=PrHEVkPmNZsLqekTya7Gl-E3gRE0r2tFwHxzvN98RHW3NKvEpR0B4UfPJhk5lTUL5UNJ7CkKXMeYj1Ue7-41FncfxnZqPvCrH7x5HinICdMrVyVXhnynDyu2nJw5VgI-NneY0dVZsDXglN8ExqHp64UAjLyi8_b1IBlkF16r_aEHn0LEgAsTsqgcrWa5KohEhB-u2vp65ECkiAe6-4ZpKctGJchBVV4kowmS2TtSSm0vI2M6cQVD85tyw-iCvvcRwrKDIUJp_s_lj8LJL1g-jtRBTPZimPJu9pc2uq5pouBfXifs1qRwlFOla_wo_wURh-tXVFQr1BK_BGSw9byfng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c196e7e0a8.mp4?token=PrHEVkPmNZsLqekTya7Gl-E3gRE0r2tFwHxzvN98RHW3NKvEpR0B4UfPJhk5lTUL5UNJ7CkKXMeYj1Ue7-41FncfxnZqPvCrH7x5HinICdMrVyVXhnynDyu2nJw5VgI-NneY0dVZsDXglN8ExqHp64UAjLyi8_b1IBlkF16r_aEHn0LEgAsTsqgcrWa5KohEhB-u2vp65ECkiAe6-4ZpKctGJchBVV4kowmS2TtSSm0vI2M6cQVD85tyw-iCvvcRwrKDIUJp_s_lj8LJL1g-jtRBTPZimPJu9pc2uq5pouBfXifs1qRwlFOla_wo_wURh-tXVFQr1BK_BGSw9byfng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مسعود پزشکیان خطاب به کسایی که میگن تحریم مهم نیست و آمریکا هیچ غلطی نمیتونه بکنه: نمیدونم چی بهشون بگم. فقط میتونم بگم عقل هم خوب چیزیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104963" target="_blank">📅 23:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104962">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc25ebba85.mp4?token=GJnOYYKSR8NEUFvAvjbpnuuy7mb36t1gN56_ooiDEWPAd-PrBUuWmfzY1AgNq6acQPTVOZT0otoGY3hJI_cziG3SKgMGiimCqJlqDqLrjX_t9XOI7oTw2NCAW3BgG8eaF3japqkayDx0x4XnxrhiJ59MijwM43GA5oDLf0lvLBRyAagrKuH_bFsioGMMND49gMBo8lBxgyLsS8DzGL-WoLm4jx6XySEjBfosXzKuypiRcvZ5yB6nJOQkPU0VLIqIM1KS2EXA6gmH16SB_cuuP4i9GlQde3bsQKPeC4vbj94uYEiZfLga8fKznBpp1-t5yE7gwPsvZdtfQMP4dOzo-Bu9VUXOumDyoT_dJ8rxL_SIXZyCgyWnCKqaY6XYnzQxWtDitYZfzMTFl6KAyOZKwrMrvH_qQdNZWQRtgRFqm1shR58uEdhRz1UyEkH4l9HDcrzx_j75Oz_gsZ2nyyk3BB_-EkRhso540Buoenn8Qz7MK6ZPjSmXqiugBnw4ItZlHzEldU9FypIS1XTuwJ2VgV4yvmizfFVd15iI9nQlx-SUMyE3goZLEp0SZ4TULAheOVxZHGr-PekLDDNtMVCIqUzt2pP08mhKeQ6qGvFfU_1vCj1kYeC3205curOFcF6mZjl3UWQl0lqDA23oNyedX7rdUhEDke_N7bh1bPZvWuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc25ebba85.mp4?token=GJnOYYKSR8NEUFvAvjbpnuuy7mb36t1gN56_ooiDEWPAd-PrBUuWmfzY1AgNq6acQPTVOZT0otoGY3hJI_cziG3SKgMGiimCqJlqDqLrjX_t9XOI7oTw2NCAW3BgG8eaF3japqkayDx0x4XnxrhiJ59MijwM43GA5oDLf0lvLBRyAagrKuH_bFsioGMMND49gMBo8lBxgyLsS8DzGL-WoLm4jx6XySEjBfosXzKuypiRcvZ5yB6nJOQkPU0VLIqIM1KS2EXA6gmH16SB_cuuP4i9GlQde3bsQKPeC4vbj94uYEiZfLga8fKznBpp1-t5yE7gwPsvZdtfQMP4dOzo-Bu9VUXOumDyoT_dJ8rxL_SIXZyCgyWnCKqaY6XYnzQxWtDitYZfzMTFl6KAyOZKwrMrvH_qQdNZWQRtgRFqm1shR58uEdhRz1UyEkH4l9HDcrzx_j75Oz_gsZ2nyyk3BB_-EkRhso540Buoenn8Qz7MK6ZPjSmXqiugBnw4ItZlHzEldU9FypIS1XTuwJ2VgV4yvmizfFVd15iI9nQlx-SUMyE3goZLEp0SZ4TULAheOVxZHGr-PekLDDNtMVCIqUzt2pP08mhKeQ6qGvFfU_1vCj1kYeC3205curOFcF6mZjl3UWQl0lqDA23oNyedX7rdUhEDke_N7bh1bPZvWuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
درگیری شدید خداداد عزیزی با خبرنگاران یزدی پس از بازی با چادرملو اردکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104962" target="_blank">📅 23:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104961">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssz1Nc5_JkCTLHBsZ-8XCwuGtzDuvHCsVq9yErH6aqzsX7ztOCjkquiv9MPzhy7oriWCazBSWzmTlcocRDeNbF6Yf6ZoP2F--YEdlSlV1J1GAHCiURKmzHPklfg0GMo1PoOV67rV0hv3lfLIzV0WJ5_RhmKtR2p9Un63aAGhEi_SP5TjXAodE865CjuARLrgfQRpENXrDo3_-i0fAIzewXHiyl-FY0RpbNJoqCNkXOqXhLRhbn9wMsRLfP7ZanfDqPfaYjD2nXq_Rygz2P8eF34tP0Y1I-6IwgFXwI1ZqyWXRgerzmAabxBEsGkQXgS1hWdc0ztIFH9bemFRZNE5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
هفته‌چهارم لیگ‌برتر فوتبال؛ پایان نوار برد آبی‌ها؛ شاگردان سهراب بختیاری‌زاده با تساوی به استقبال دربی رفتند
🇮🇷
استقلال
😏
-
😏
فولاد خوزستان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/104961" target="_blank">📅 23:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104960">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwB9Z3VmDwQB_6TTOTIE-KiFmLkuvdxtPUO7Cf2fjd7H1jqTQmgGzWXQYkIWcRDVR-96RRiBgvUq5_2ZyR-PhLfp8Sugaqz071xhi1NOZ_MHVYmZZE-Hj5qy4f2UsSXTZWC5ZFex0En7r7quUd18hnoXKAM1F7TDKn4uBYkAOJv8eR8e2z8Tzpbj0j-6wG_vEs-u1frwi7smfGT9Hmpl3aaKA1xXU_pztA01rgo8rWTXXFLZDPxyWTCjSE8kLz9-F_bhsneSFX265EI_9rzcr_BHt-VnoVc7yslPEYMGMfTK17WSZ-B5kLDMTu3LtAtFFU1HHuAJmFitovuH59inFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
هفته‌چهارم لیگ‌برتر فوتبال؛ پایان نوار برد آبی‌ها؛ شاگردان سهراب بختیاری‌زاده با تساوی به استقبال دربی رفتند
🇮🇷
استقلال
😏
-
😏
فولاد خوزستان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104960" target="_blank">📅 22:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104959">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇮🇷
🚑
صالح‌حردانی در آستانه دربی بدلیل مصدومیت از زمین مسابقه خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104959" target="_blank">📅 22:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104956">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed2d489407.mp4?token=fTC7QN4IJZWcrvBCn1Ij6PgWhxLbtr7NffqMkpD2m1dJWtQeKBUjFmkk4NObpdX90jhm_KVa2BRjTBEyv68a5XGYnQ8sC-2MzXRgb3sjg1fKOiSAIofqiJ7H65FgprMGD0p2fNJTWh3NsC5ZtM_JpvSCAB2PFewJlLFkXLx57T5CEt4H-y65gd7FV1W_GpxsKFDxUPT59YWy-ueSUVzkhvXHNzoZwjZmz7hQUHdpnxcGo9Eby-cvA3WnZcCE5EXMgqL7JA7d2opvhTythWMo4bPNjzwFajgKnFLXGQ3i__TBKZamingcjew7mZ65WPre9YCAsAq1UsTIdRyl_CFzyWi_xmsHWfBap-YJ_CLPkX_RgJ97iNTS_LRm5n83s1V_3z2J_Qz1LB0UmrEw6WcPIbrC1twiSCuwm53795TZHYd0g46Y7Vrefvsoubqw72KgbCMREPzcrDKuSIRlt43ZCXndLkBRKMgb4wSAaApwobKgmYZAIKf033LpR7eDl5DlJHjA-axE9MvHEIiR1HzzzBJXiyU27uQfOCyaFyW_5YcDO4hSZ5RYQ-OC_gK7DDV03mZSoID8l0qohWWhVB2QLgRhU8puDOWcioLsRf65tnnG4DCi-TiWgr-BgnDEK1-NJtslkAA-vzdqzjRnfqFRrOOaALlIezDaIGqw-JwtuFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed2d489407.mp4?token=fTC7QN4IJZWcrvBCn1Ij6PgWhxLbtr7NffqMkpD2m1dJWtQeKBUjFmkk4NObpdX90jhm_KVa2BRjTBEyv68a5XGYnQ8sC-2MzXRgb3sjg1fKOiSAIofqiJ7H65FgprMGD0p2fNJTWh3NsC5ZtM_JpvSCAB2PFewJlLFkXLx57T5CEt4H-y65gd7FV1W_GpxsKFDxUPT59YWy-ueSUVzkhvXHNzoZwjZmz7hQUHdpnxcGo9Eby-cvA3WnZcCE5EXMgqL7JA7d2opvhTythWMo4bPNjzwFajgKnFLXGQ3i__TBKZamingcjew7mZ65WPre9YCAsAq1UsTIdRyl_CFzyWi_xmsHWfBap-YJ_CLPkX_RgJ97iNTS_LRm5n83s1V_3z2J_Qz1LB0UmrEw6WcPIbrC1twiSCuwm53795TZHYd0g46Y7Vrefvsoubqw72KgbCMREPzcrDKuSIRlt43ZCXndLkBRKMgb4wSAaApwobKgmYZAIKf033LpR7eDl5DlJHjA-axE9MvHEIiR1HzzzBJXiyU27uQfOCyaFyW_5YcDO4hSZ5RYQ-OC_gK7DDV03mZSoID8l0qohWWhVB2QLgRhU8puDOWcioLsRf65tnnG4DCi-TiWgr-BgnDEK1-NJtslkAA-vzdqzjRnfqFRrOOaALlIezDaIGqw-JwtuFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گلزنی رونالدوووووووووو برای النصر
گل شماره 978
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104956" target="_blank">📅 22:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104955">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccdc8cb72.mp4?token=WBpTTNiDScxdAzvi-kqkcJWzA4PkfHAM74-PXOah-rXhAOJdq4nYDT14zfeYZgCgwk3QAdMHOStRfIAE66IXwVDgKD8nFBLM4g0WS7d5tBad38M40jTjIQqflBFGzOg2nEtpPKotqEqIWdBUWkPm4ve9jSc65ql0XM5y5TEDxGgrBDrxA5opz0gn1w19APL6U1aXrYIkVNPPtOmNE8gXkBAy0dSEMzY3_4IAhlatAIMTaCh_pRcvYtjBR3luGHG83wdKXhc1t613gmtPSptfHHoYZsXmHG4cuo2053d1Z8UBtdRkVM7KWQsf5ZPmSAryo13T-bmOzYcfp31OMPw6tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccdc8cb72.mp4?token=WBpTTNiDScxdAzvi-kqkcJWzA4PkfHAM74-PXOah-rXhAOJdq4nYDT14zfeYZgCgwk3QAdMHOStRfIAE66IXwVDgKD8nFBLM4g0WS7d5tBad38M40jTjIQqflBFGzOg2nEtpPKotqEqIWdBUWkPm4ve9jSc65ql0XM5y5TEDxGgrBDrxA5opz0gn1w19APL6U1aXrYIkVNPPtOmNE8gXkBAy0dSEMzY3_4IAhlatAIMTaCh_pRcvYtjBR3luGHG83wdKXhc1t613gmtPSptfHHoYZsXmHG4cuo2053d1Z8UBtdRkVM7KWQsf5ZPmSAryo13T-bmOzYcfp31OMPw6tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
💙
لک بازهم مانع از گلزنی یاسر آسانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104955" target="_blank">📅 22:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104954">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ed0196bb.mp4?token=Gg_yYtNmGPCF5hbdiBrqQ8tv5KFL5gdUHs3e48weZvNWNBppJIB2DrHDgA-CmQRMWVctewEJOTyZvFNsOe-qS1P4IqrTSvmBqby9A_rmkR5qXU3emahDD-Qs55aTo7HYgecXTJZx3jdfDnEKmGqof7xNYjVJlvYfSaFy0rRScYtN1k9k1JJxH9tl3RaDGCcTBoF1GETZ3eHuPmc7p7SWv53MznkYgcNg_heecTZOA9X6oZxmoZvwP9qNDMO6sgKi6VggTSmk0LfJ6Ug1eozSiOKdja8aA1F2rebMNRfOib5j4TPFzdTXwNY5WM359cpX4060gisJegag-mOZP6CeaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ed0196bb.mp4?token=Gg_yYtNmGPCF5hbdiBrqQ8tv5KFL5gdUHs3e48weZvNWNBppJIB2DrHDgA-CmQRMWVctewEJOTyZvFNsOe-qS1P4IqrTSvmBqby9A_rmkR5qXU3emahDD-Qs55aTo7HYgecXTJZx3jdfDnEKmGqof7xNYjVJlvYfSaFy0rRScYtN1k9k1JJxH9tl3RaDGCcTBoF1GETZ3eHuPmc7p7SWv53MznkYgcNg_heecTZOA9X6oZxmoZvwP9qNDMO6sgKi6VggTSmk0LfJ6Ug1eozSiOKdja8aA1F2rebMNRfOib5j4TPFzdTXwNY5WM359cpX4060gisJegag-mOZP6CeaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ با اعلام پزشکیان نرخ سوم بنزین از ۵ هزار به ۱۰ هزار تومان افزایش پیدا خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104954" target="_blank">📅 22:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104952">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7PDmPMmz2_xqk18Bzn4yek6rAKSKoJ3Pt8crZ9kR7afpss2dmixarVP60Oz81VHRrRPZbQ9FXxh0NNZwsKGetAAkyC1CO-95h9Ux8jkMHPYjBpN7xNag3US7pDNVu-HvIVPQMXcqkXxFo4QynAYNalmsAb-ZP_hiFEfmbDSHH2bCHf7yel7454d6t4ddIF8xXBlWJmAId6Kqy3lsegfXu7G3fFSykFJZn2-iojqiQlB5NA2IIic7F-4iRdRDgCXsnXs_32kv5LxBTraAVB4-8dlRV7xkcBEQIjO2gNSfZsPrj3v2uTd4zHzRkUftkx-0PLDa6sOgpQy8rjPJZ4trQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🚨
🚨
🚨
🚨
مارکا:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طی چند ساعت گذشته، منچستر سیتی نیز به کورس رقابت برای جذب خولیان آلوارز پیوسته. آنها در تلاشن با یک قرارداد قرضی او را به بازگشت به منچسترسیتی راضی کنن
❌
🇪🇸
آلوارز هیچ تمایلی برای برگشتن به انگلیس نداره و همچنان روی خواسته خودش ( بارسلونا ) پافشاری میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104952" target="_blank">📅 22:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104951">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
❌
🇮🇷
اتاق VAR اعلام به آفساید ساسان انصاری کرد و اخراج عارف آقاسی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104951" target="_blank">📅 21:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104950">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
عارف‌آقاسی مدافع استقلال بدلیل دریافت کارت قرمز از دربی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104950" target="_blank">📅 21:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104949">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
عارف‌آقاسی مدافع استقلال بدلیل دریافت کارت قرمز از دربی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104949" target="_blank">📅 21:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104948">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9QJhWhbAED8pgHdaqZ_6SwDV2C9KQoCun9LJ2Ir2zHF_-g9PQkLHq9RssP7f1mHnsj0WM_h6plxnub1HNzVRnUtLxLKTMXigUzNwiTltRuTwmlGU-ZH98FfbTAn0boVPVsLxhtV7RJctewVNaG8_76rrDY7vBwBbI5GQMj7IV0xpO__TE6Uf_qu-s2ODE3xPCC4tulQiQFfRh0Ym_s2DxO3FFg9SeX0FM7fhmGfL26vpBXHD75CQCd5QCUMBIMMploRT6IGOuCrnxyecPnnnpLiA-Bb7L_ieNJpF3HrNewvm2jz1dk7NBLJQ0aMi3peyzD1Dlrd8eIzN6GN27EL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ نیکولاس جکسون با عقد قراردادی تا سال ۲۰۲۹ به ارزش ۶۵ میلیون پوند از چلسی به استون‌ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104948" target="_blank">📅 21:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104947">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6W2Lfyoa11Bz0Tj5nDdre8Mnr1qbebVkyHFaD7jZLxySt706c5qlv4CET8FpyVPgzlljhlIiUX919Y32pR9vvZwvE_DvaB1Rw2h1zR1RoJRZHmiA-MYuPfKAl5JmQqYMyCThXCya7zBwiyyUB_8zTOtL8lLSFSBy1iLEf1V1REKDlm7fpycRn5mnx9hIu9p4JI9B7yfjKMtIAMBLV16bJn5n3DnI7A9r65TN9hgV-MwMFKhy3M_OFpkUy6YRcWaaa7i1V3ONzAhtMxgai0nKFKQwJUQVxSppZvFIiS1EKN3Sh1b5NZtaTvWJgDTxQOzMEty-sncEadkq3F5xc5DzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم لیگ‌برتر انگلیس؛ ترکیب منچسترسیتی مقابل کریستال‌پالاس؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104947" target="_blank">📅 21:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104946">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1abe2b073.mp4?token=e_ldZYDan998xJpSiQomU7kRrzHQp-ozTlQIPnZB7aYELsWGWjnA_KP5VOhEuun-bTIZh-DULgsuD3GamfT5x5Z8fgR1y-JakaV0LblWIGcMLhd8cC7sx8Nh_zC2XQK1IgWkMihGinleQHutsM5fiNmOuLsLp_nJYUX5Q4kxMJKuHEUWrh7QjHW65kLqzVp5ff482rCS8RukI5n1YTF3M63CL9Dn0LsRuxGsss1C8ZVMVn4KsW6VjK9gJwnNtFi0J2d6lDFER4pnBrLAEgTnBn5s6Er-xB9v9-f4OGdD3he2hQ3VM-6hx1AlE7Xiiie_Ao-eT6EUCMQZVv1ewVF-XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1abe2b073.mp4?token=e_ldZYDan998xJpSiQomU7kRrzHQp-ozTlQIPnZB7aYELsWGWjnA_KP5VOhEuun-bTIZh-DULgsuD3GamfT5x5Z8fgR1y-JakaV0LblWIGcMLhd8cC7sx8Nh_zC2XQK1IgWkMihGinleQHutsM5fiNmOuLsLp_nJYUX5Q4kxMJKuHEUWrh7QjHW65kLqzVp5ff482rCS8RukI5n1YTF3M63CL9Dn0LsRuxGsss1C8ZVMVn4KsW6VjK9gJwnNtFi0J2d6lDFER4pnBrLAEgTnBn5s6Er-xB9v9-f4OGdD3he2hQ3VM-6hx1AlE7Xiiie_Ao-eT6EUCMQZVv1ewVF-XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل دوم تراکتور به چادرملو توسط اشتراکالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104946" target="_blank">📅 21:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104945">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrhEvD6CI7AQ0OP8AiZ-MOspjeY6WLppyGDzNfhDRmZkrPcd3eJlb_wsZrgwbP6iflnDCJPFwEOtNZDx1f7fnR3vHG5Lm9lAQwtXayn07DYWHUZuuW-CKwY-vCvB08PKtQhrJ8pomWqu3dyKZ2dMzZnOVvCso8p8YsN2qsr5qLV04NQx8qxOhS-RrRZUJW0q3Iy-r00CELUHPhbSi8ynjYcBFBUp8fc-vmexF4kIm6jaj22kpPMVzmMEcIOa8JD4DlM44Y_s5SjWNLhmalInSisebB2BD5TZPt-LtU-ldbq2B1vwqQ99sKlbmeFll8Bg6VLeRo3qYGFg9YRIzVzNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇩🇪
افتتاحیه بوندسلیگا؛ ترکیب تیم فوتبال بایرن‌مونیخ مقابل اشتوتگارت؛ ساعت ۲۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104945" target="_blank">📅 20:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104944">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2abb732ba.mp4?token=frZHf29uRGswvlMW73dH8syyD6Ha5wfTQLmUAdNxoqjHW-ECAcnD5kYuEiCNGWuUMGJUdpyNKt2L2_X_vpDLxAxmixn2veau2InBmd9sDdEw7wXK0-yoigSn_IBl0Lq-xXsb3wSq1ya_ZxR3iBKKrnEUk7ZQVe2pGd2cFjaI7Fn0YXnJsH1EC2cH2I1BTdTHALjzZSR3SpNHmFC61b1WmyTfV-ZEkhrBaefe6q98peZiKtpNCgPEeUhb0Ztcg8EXNfPa6FpCOrqkJdKKxcZ7xqFtSlmI_4cBPpFrXIRgChBRi_oYprdaID3ZwbfgoS66hzkq1bsyYAa1_XlFoR-xjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2abb732ba.mp4?token=frZHf29uRGswvlMW73dH8syyD6Ha5wfTQLmUAdNxoqjHW-ECAcnD5kYuEiCNGWuUMGJUdpyNKt2L2_X_vpDLxAxmixn2veau2InBmd9sDdEw7wXK0-yoigSn_IBl0Lq-xXsb3wSq1ya_ZxR3iBKKrnEUk7ZQVe2pGd2cFjaI7Fn0YXnJsH1EC2cH2I1BTdTHALjzZSR3SpNHmFC61b1WmyTfV-ZEkhrBaefe6q98peZiKtpNCgPEeUhb0Ztcg8EXNfPa6FpCOrqkJdKKxcZ7xqFtSlmI_4cBPpFrXIRgChBRi_oYprdaID3ZwbfgoS66hzkq1bsyYAa1_XlFoR-xjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
پرتاب بطری به سمت پیام حیدری و بازیکنان تراکتور از سوی هواداران چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104944" target="_blank">📅 20:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104943">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b801553.mp4?token=SMLwyLrXRKUaPxX5CIWxvLR9FCTRwUDNlYrb6CROE_-VBfaEbgbkku7k72afpAyKRYdQ-JPNcKZ-LXWY6Gp4KG3kNMptoU1coKqdpBWayUk8KUEbW92R-KuMY4PnsE_g8eBg7W_KJSTeYjtSaapXFxQ-PvzvdkXPH_s8zVMz1P4kcpqKgE6AP5GEEd_aehKvACvt7wW0HlDf0oPRxKh8ZTc9Bov8gqzTfWmRxyJcpiwzyDtujX1MG-fK9u36X1V47BtA0FWLCJQHfPXIPPcV2iLY4RNAVbysQLUk76TXaKtOsYy-t7-RnoyqWXfubJvBdn_d5c1jbyCEFLGonMHnCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b801553.mp4?token=SMLwyLrXRKUaPxX5CIWxvLR9FCTRwUDNlYrb6CROE_-VBfaEbgbkku7k72afpAyKRYdQ-JPNcKZ-LXWY6Gp4KG3kNMptoU1coKqdpBWayUk8KUEbW92R-KuMY4PnsE_g8eBg7W_KJSTeYjtSaapXFxQ-PvzvdkXPH_s8zVMz1P4kcpqKgE6AP5GEEd_aehKvACvt7wW0HlDf0oPRxKh8ZTc9Bov8gqzTfWmRxyJcpiwzyDtujX1MG-fK9u36X1V47BtA0FWLCJQHfPXIPPcV2iLY4RNAVbysQLUk76TXaKtOsYy-t7-RnoyqWXfubJvBdn_d5c1jbyCEFLGonMHnCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
62' اخراج کلباسی بازیکن چادرملو به دلیل خطای خشن
روی بازیکن تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104943" target="_blank">📅 20:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104942">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a01cc820b.mp4?token=YB4O6MZIM0aUQRHmofp14rocl-q3s6n16NTm_PkbXFT8bDDWqiH20TbrmUMWBFKQHReRctY4aq48hmUCstW_t7s-DJuhFJ87ssqSBQFYGpI5fgBO3Bg4mdiAXIdnsab0k3bEct5RSZJy6MCUdbr-kcfKDCERu6Vb1VSnpyj-8ALlOHLuWqV-AQdNbn40xoizbLo5A4O05tMjsgZPZgV9rVyRsu8ULRfkWy8H-jFag-adE7XxQyMXzkqmqqI96kQHWCDEKIaPN7-8hGrhADdcnfrvlPrhYGB4nAvE13N2cgoVwEvjNmWvhc_IEyBWvnibiFDwUos2FzsL21ULTmYNf3YzQp5z73eg6PcVZ6j5dRQDmPzz_UhuRZSwTIvs0VBfKcQpa64-aSVj84F58v88b8jj9v_1s1nKDP6OxGKTB483t_66KkUkW09LI5lfiMSWX3Jaw628pgG5neljrECkYqqzemKmL_gNAD56xPtEszXHqz97FYSgn5e2AShHaQzi_gwc6-otrPvWipl30-NK5woinfhPWWlvGC2vr4IjYExkIXgq3EfdAeJV4AoJ-x9kBMIoa3J6Lqav1RjvmHoQPr2hzJbXZJd8L8JHFHzKLCGQWQhWIxfY9SWzksx5k0Ig4AWSzWjd-l2CNeq5-vjtS05t3HLQ-wn_FiAGdFxWgIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a01cc820b.mp4?token=YB4O6MZIM0aUQRHmofp14rocl-q3s6n16NTm_PkbXFT8bDDWqiH20TbrmUMWBFKQHReRctY4aq48hmUCstW_t7s-DJuhFJ87ssqSBQFYGpI5fgBO3Bg4mdiAXIdnsab0k3bEct5RSZJy6MCUdbr-kcfKDCERu6Vb1VSnpyj-8ALlOHLuWqV-AQdNbn40xoizbLo5A4O05tMjsgZPZgV9rVyRsu8ULRfkWy8H-jFag-adE7XxQyMXzkqmqqI96kQHWCDEKIaPN7-8hGrhADdcnfrvlPrhYGB4nAvE13N2cgoVwEvjNmWvhc_IEyBWvnibiFDwUos2FzsL21ULTmYNf3YzQp5z73eg6PcVZ6j5dRQDmPzz_UhuRZSwTIvs0VBfKcQpa64-aSVj84F58v88b8jj9v_1s1nKDP6OxGKTB483t_66KkUkW09LI5lfiMSWX3Jaw628pgG5neljrECkYqqzemKmL_gNAD56xPtEszXHqz97FYSgn5e2AShHaQzi_gwc6-otrPvWipl30-NK5woinfhPWWlvGC2vr4IjYExkIXgq3EfdAeJV4AoJ-x9kBMIoa3J6Lqav1RjvmHoQPr2hzJbXZJd8L8JHFHzKLCGQWQhWIxfY9SWzksx5k0Ig4AWSzWjd-l2CNeq5-vjtS05t3HLQ-wn_FiAGdFxWgIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
صحبت‌های هواداران استقلال در ورزشگاه
❌
ما رامین را نمی‌شناسیم. این جام را به ما بدهید. پرسپولیس با تیم‌های ششم امارات و قطر مسابقه بدهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104942" target="_blank">📅 20:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104941">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a93dbbe2f.mp4?token=LnS4E4mMmMVkr8ceEJAYfn0iBfXL4dKE388ryDy1Ig5-g03bLoN3l4AmijJGrO1l5zIcRQI_xK3qtu7LpgtcGz7Qz95lnUBsYEjdBTF50Q771WKhXXDGAiLAKaKTE4__jMOJZ-KAISHDN_VauTXITRwZpe773rKZAsvS0oAMyCQX4mxfBDyKX_dB0xqjREdn9phWFQFUYsjXjcZl5J6VZfqHcB53L2oLnJVBdJD05r45XziAiBN4REUJE6D12tk7Eyh1kfM9UeSxpynYKN048f0zx_an9Qo61by44w6u9jmZYukNELU2t7Qmtahl8Gd2iizWWphGBSR9lKGDv0Qw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a93dbbe2f.mp4?token=LnS4E4mMmMVkr8ceEJAYfn0iBfXL4dKE388ryDy1Ig5-g03bLoN3l4AmijJGrO1l5zIcRQI_xK3qtu7LpgtcGz7Qz95lnUBsYEjdBTF50Q771WKhXXDGAiLAKaKTE4__jMOJZ-KAISHDN_VauTXITRwZpe773rKZAsvS0oAMyCQX4mxfBDyKX_dB0xqjREdn9phWFQFUYsjXjcZl5J6VZfqHcB53L2oLnJVBdJD05r45XziAiBN4REUJE6D12tk7Eyh1kfM9UeSxpynYKN048f0zx_an9Qo61by44w6u9jmZYukNELU2t7Qmtahl8Gd2iizWWphGBSR9lKGDv0Qw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول تراکتور به چادرملو توسط حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104941" target="_blank">📅 20:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104940">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz6muRenhdzT_dXDqtVSEckHIhMyebkPvlIDbpy6l-cKV2KnekH9nqRF3D-B0kVrRE3IUsmvf2KsL303DzqrpcsRNjoBOLZhJ5EjU2zd0riKAs1xYY_wyh0cP7qU_NAYqR9zYD7YdBay6Gx4C0O6dmC46uCvuSsPBaLuRB9t1VWRyqdCTvjCz6BZtJxn32i64MCN5Ro0dMIEg0S7fPQG_CgPUNNLXHHX4dFZ6drfUfEWBXr9eMAP6CI80j5Renm0biNd7hzY8T4AtJjPFaFifAtt524qC7kSaCNvQN_LmrZ356op5U1Y8Y2Lx4aEMv76GPMoldyZKJl7MaERy3b1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو در ترکیب فیکس‌النصر مقابل التعاون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104940" target="_blank">📅 20:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104939">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2cdd650bf.mp4?token=l8eaX8hn0nUjfSee3JzHw_0uuNPmO4olDTcH--YCF0IOILHOrcdLqvweyTgaJW5Q_1Um1Nehrq6q_C_lmBtYFU-X6jZaWAZLpns1L4Bcf7P6pOhC7ruETL9QJJHmEVTfL9o1JzMSi7lr9O026dvTlkjX8-kxSokLCX_y-ZbDiwMTFdwhSKcsBOBP3ZTQpldTi_5DhdTv1IJTsa4m72ty8mwIRIBC7vruM-buSiNR1o4W7bq5tkeNACj9Cj1mmjVCCh4HNDNsVlxqWxy2Kz2mnbnbVVXrwhY3G61wGclWfwQQoVDyEVbs8fazptNRc2Plbg4ZpAXAwzheTdtsM-MGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2cdd650bf.mp4?token=l8eaX8hn0nUjfSee3JzHw_0uuNPmO4olDTcH--YCF0IOILHOrcdLqvweyTgaJW5Q_1Um1Nehrq6q_C_lmBtYFU-X6jZaWAZLpns1L4Bcf7P6pOhC7ruETL9QJJHmEVTfL9o1JzMSi7lr9O026dvTlkjX8-kxSokLCX_y-ZbDiwMTFdwhSKcsBOBP3ZTQpldTi_5DhdTv1IJTsa4m72ty8mwIRIBC7vruM-buSiNR1o4W7bq5tkeNACj9Cj1mmjVCCh4HNDNsVlxqWxy2Kz2mnbnbVVXrwhY3G61wGclWfwQQoVDyEVbs8fazptNRc2Plbg4ZpAXAwzheTdtsM-MGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
دبل‌کسری طاهری در بازی امشب سپاهان
سپاهان ۲ - ۰ گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104939" target="_blank">📅 20:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104938">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ca3971a9.mp4?token=NydOVbR2iHEGkHlbflFVZD8wJrlLWZktkmmzkkwnJu9hE9qkal1XMqsfw8heaqYufy-r5cWt5Fu82wOJx0fBhMYA1rT4jBb5J1OIH5iJoH-F4aKs_o338udvTppxqCimsM5QzyhfEcnOAc-zG8VXmXSGgKnruT8HHgchIXf09MrVMOO80sHCgeOuHZthWEM41drEg6lLfJYH8d70aqZ1IcNw81Lg4Up3BSUq-3qsN-vgC-w6-LQ53bNJspAv6TJwMWIE_wYuFS1pKbPwbRiR7WlhpifAIIEeNQ4MXnyaGzpV7CCz2uJYCfN3Rl8d6TE1SZqW1H7ojLlsK49ZYDuRcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ca3971a9.mp4?token=NydOVbR2iHEGkHlbflFVZD8wJrlLWZktkmmzkkwnJu9hE9qkal1XMqsfw8heaqYufy-r5cWt5Fu82wOJx0fBhMYA1rT4jBb5J1OIH5iJoH-F4aKs_o338udvTppxqCimsM5QzyhfEcnOAc-zG8VXmXSGgKnruT8HHgchIXf09MrVMOO80sHCgeOuHZthWEM41drEg6lLfJYH8d70aqZ1IcNw81Lg4Up3BSUq-3qsN-vgC-w6-LQ53bNJspAv6TJwMWIE_wYuFS1pKbPwbRiR7WlhpifAIIEeNQ4MXnyaGzpV7CCz2uJYCfN3Rl8d6TE1SZqW1H7ojLlsK49ZYDuRcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
هم‌اکنون نمایی از استادیوم فولاد آره‌نا اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104938" target="_blank">📅 20:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104937">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD0dX8vlZYvqvx7rPrh6XnR0a-rdlqlLUoz9vwvuOy7DRB6iStCVr8xFv3Tf7144qdjUK4wI7EACVi1UKn_htdJmtqJTX7XZebVq0GXV-W7Jf1db2J3Lie-hsl3LQaElScm-isEKh38D9zXmquljGa6PK-IyKc_sQG9y8x7j41kDRSnBVPtQ8O0eosun5qEQkWWSQigDZnonNHtgXcx2j3BMWu_5FScIbOx1EAYzjT0_X7tVypEZ-ejowWiMM9_kqP2g-7RZ56gBRRhPob4gUQUsxXqeUtte6_sZ_kwD2fB7LAXl7CP9xtFCOOWulcV8qFMdF40yuTLSsYN1A2lRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل فولاد؛ رستم آشورماتوف نیمکت‌نشین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104937" target="_blank">📅 20:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104936">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmJk5jY9WsC2jjOIOwDl0QqXUVo2-DXlCFbOltDgFaX01ZWiZS9xmC6khROEeMWZhhjmG2E29Mhuy6QXXmvCpwavW2XpHYKXd4JBN8-O-Z7MEPBgaddHpV5OAI9D2-2D3e0gEU0eaceXQ6L6ksW2LL4GRurgQUVvn93St1uvb7FTkqlyl6VcDBD1A63wgkyJcT8euPn0b-zF57d5dgiqcLmMco13QOi_H47rZ9wIg7Et8ogxUhp50dLy-4b4qsRYMC8XxGWF49hkznoir4WfM1vqthR4Jlnl4G0RZpBPnHMZeh6aogq8wZTeoi--J_pv0ESO0tMMR5e2IiDTPUdQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل فولاد؛ رستم آشورماتوف نیمکت‌نشین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104936" target="_blank">📅 20:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104935">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2f021f29.mp4?token=X2FbfwnjpVlphFxVGm8uB4myH2vbWzqKdMRUvMpSRwZcocKasL72qbliK0LAYQyf-Vx6UtV_CUWAqMdDb_7_TKz0AqDGyXM3vqJ0DA0RF1TH5wc8gl8u-CfSOkVppxLRz7rjfJ5EoeiwfVc1MUGrPrKFA3w-DqHqlIPiN5Xqom5cDRUM7f_kEMQWUZ9Qh74v2PegcGkCjir4FvE3n6jBIhpAzsHrwhzyKWO9S7wu_cI0dtMRtHTlwjeJc5R78lT9LvhD5Oom-oy10jIGliNd9uMXjqwDZMjA4wWJzp6P3QgfcfozSF3nOb22kANKEdFxS1qw7LoxU4trc7jN84Wi3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2f021f29.mp4?token=X2FbfwnjpVlphFxVGm8uB4myH2vbWzqKdMRUvMpSRwZcocKasL72qbliK0LAYQyf-Vx6UtV_CUWAqMdDb_7_TKz0AqDGyXM3vqJ0DA0RF1TH5wc8gl8u-CfSOkVppxLRz7rjfJ5EoeiwfVc1MUGrPrKFA3w-DqHqlIPiN5Xqom5cDRUM7f_kEMQWUZ9Qh74v2PegcGkCjir4FvE3n6jBIhpAzsHrwhzyKWO9S7wu_cI0dtMRtHTlwjeJc5R78lT9LvhD5Oom-oy10jIGliNd9uMXjqwDZMjA4wWJzp6P3QgfcfozSF3nOb22kANKEdFxS1qw7LoxU4trc7jN84Wi3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
✅
👍
تیم ملی والیبال زنان ایران با پیروزی ۳ بر یک مقابل اندونزی برای نخستین‌بار در تاریخ به جمع ۴ تیم برتر آسیا و مرحله نیمه‌نهایی قهرمانی آسیا ۲۰۲۶ صعود کرد.
تبریک میگیم به دخترای عزیز کشورمون
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104935" target="_blank">📅 19:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104934">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg6x2MYJJDeNTHF99tOvFv3dxRhMMVMdv2jpZtb_lSIkm9A-tO10l1OGqnp9mVI4QNrP8BgQq3ro9w1RD3Ryi50inbbPtzoAGWUrQqZGukBG03vZ9kOR1sJBgD3PFU4GyMCHSn_AKIpvpxVPSgGIlLJ8bruHi6X2sp46AfeLx7lPiZv6E5-_2A4OL5X0TGsRWNfm4Xhh-aDiayLyiCHgJ5kU41wUYiCf8xXCAzbs0qzRmRs3FFxTLuP5LD4Bmsi2e5Joc4JJ4MKKWDT7e1u5tt7X9usleEFQcygUFXQDZA2ORGo9OkY1z2ldFO5U3RXMJR8qYq5nm7Lpuo2CChwWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب فولاد خوزستان مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104934" target="_blank">📅 19:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104933">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded8751287.mp4?token=HwueMZjP5VrLZdWQ9F5zkPmY7MaCN-RZjhGu1nVlOsiR9rbtH7Dtmv3YL7yas9WXEcG_j3ccArztKWuDCmtaDcXsbRcKTHzzkBZdQ5nXpmGvDpqBJVMKDsHROBctQ5RTDSviZw-VLSHntJdUCm-jkN5i350RzoHdIFBXv3ZkcAqUQfShzpLYGVw5FWof9nE9HdlkoH_8kc2y7iIcFLt1LVQs1bS5Kbqame4Y7gBMN97aAne4BYe5D0B-6usSlDu3c0Ga-h_oNCgXWxqmBrdXoZ7CshZOdb7a4zNG1aBUlNNzwhqSrWAq6duKFarzQ37zDDqUELcZwYYStKCITWSPRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded8751287.mp4?token=HwueMZjP5VrLZdWQ9F5zkPmY7MaCN-RZjhGu1nVlOsiR9rbtH7Dtmv3YL7yas9WXEcG_j3ccArztKWuDCmtaDcXsbRcKTHzzkBZdQ5nXpmGvDpqBJVMKDsHROBctQ5RTDSviZw-VLSHntJdUCm-jkN5i350RzoHdIFBXv3ZkcAqUQfShzpLYGVw5FWof9nE9HdlkoH_8kc2y7iIcFLt1LVQs1bS5Kbqame4Y7gBMN97aAne4BYe5D0B-6usSlDu3c0Ga-h_oNCgXWxqmBrdXoZ7CshZOdb7a4zNG1aBUlNNzwhqSrWAq6duKFarzQ37zDDqUELcZwYYStKCITWSPRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌تماشایی خیبر خرم‌آباد مقابل آلومینیوم اراک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104933" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104932">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fddb9c4e6.mp4?token=fhY8vhgXdwllPlle5BZF_8xFIEfaLDUAe5lV6vywmTV6CUXXaYWh4m4_ld8KdKYPfLxF8tLq7EYsTYeCufYa7-1VoCneZ1m76oU9P2vK6XekDIeCUXHHNKMqWOd1IT7M9_Il_6wqTbCpTopuPno2GcGmgTOXE31NBkwA6sz9m602EnWyU30FlDFB_fXrP3EEvz1RcL6O5gvDACawNQkGoluHO4FsKzIe7R2LXHozFGk_QILnYexD4LGyCIKSctVLZYrxofzmSjpvGTZrQTu8TMEmNtOH-OkmyVXVFmosXew4EilDOrqy-dsSUXSiV2G-W2b7t27wujI_kNBmyyCTaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fddb9c4e6.mp4?token=fhY8vhgXdwllPlle5BZF_8xFIEfaLDUAe5lV6vywmTV6CUXXaYWh4m4_ld8KdKYPfLxF8tLq7EYsTYeCufYa7-1VoCneZ1m76oU9P2vK6XekDIeCUXHHNKMqWOd1IT7M9_Il_6wqTbCpTopuPno2GcGmgTOXE31NBkwA6sz9m602EnWyU30FlDFB_fXrP3EEvz1RcL6O5gvDACawNQkGoluHO4FsKzIe7R2LXHozFGk_QILnYexD4LGyCIKSctVLZYrxofzmSjpvGTZrQTu8TMEmNtOH-OkmyVXVFmosXew4EilDOrqy-dsSUXSiV2G-W2b7t27wujI_kNBmyyCTaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول سپاهان به گل‌گهر توسط کسری‌طاهری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104932" target="_blank">📅 19:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104931">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b835e745.mp4?token=CCUGVKPRAkoKpXvr6fFWHB9ZdM7YqmR4CAIdaSoar70mK1sL0gOC6NV3sHzXGlWMPlB2YCGv6lFsu4v6ryw5-rSOhRfidGhmvXvkS4mEB-CO_hJ8dBnQkGztGyxyylraK7hjhzBDoKwbVNgZnx89dGLjP1aTUuwmIptIeT3De8g-GOAFz4F41_nfsMWJHka-lDA-J7DUqRXLJhM5UeqlMHbIktDJhZhFk35-Y74SEhJOUFkcEDNwpgtsNmk7IQa8XbIr9VDjGnPxx4hst6wrJgIYSprmw2M1087p8apbbaDc_fuoWoQ9DkG4zeZB7XjA7EbJu-xGAdArxmW_26BhjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b835e745.mp4?token=CCUGVKPRAkoKpXvr6fFWHB9ZdM7YqmR4CAIdaSoar70mK1sL0gOC6NV3sHzXGlWMPlB2YCGv6lFsu4v6ryw5-rSOhRfidGhmvXvkS4mEB-CO_hJ8dBnQkGztGyxyylraK7hjhzBDoKwbVNgZnx89dGLjP1aTUuwmIptIeT3De8g-GOAFz4F41_nfsMWJHka-lDA-J7DUqRXLJhM5UeqlMHbIktDJhZhFk35-Y74SEhJOUFkcEDNwpgtsNmk7IQa8XbIr9VDjGnPxx4hst6wrJgIYSprmw2M1087p8apbbaDc_fuoWoQ9DkG4zeZB7XjA7EbJu-xGAdArxmW_26BhjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
دریافت جالب و دیدنی پارسا مقصودی لیبرو تیم ملی والیبال زیر 17 سال ایران در دیدار نیمه نهایی مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104931" target="_blank">📅 19:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104930">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b2bd316d.mp4?token=FoRtvWdWHCkjCGvRfx9iKZEif0u-xxLK4u3SQxxhqhvZgPWAXdLSSxg8hyLj1sGmSQPDrY20oeGBl_VmIs69_rZKEemeloYZG0gBBfVH3tSnGMtoqP_WpFlQTBL28hMfX3evIs_Cnx2Lmbcedh6bO9F7wSjghDBymeH0RpSHZjnLDmxo4RiCHg8N-8HLhr9EGNX_XOnlFsGTUyxs7G0T6nc14-kifCrAniD3TsobzftUuiSz8Jw-nfImhY6yckrnZNtkETanBxIDYhIJaNT-4XYn151wWqJzGRl0-vUwuurGMF5TTFAZVhj67W1tCtT29hPrKX_Lk12KmFsWNg4oGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b2bd316d.mp4?token=FoRtvWdWHCkjCGvRfx9iKZEif0u-xxLK4u3SQxxhqhvZgPWAXdLSSxg8hyLj1sGmSQPDrY20oeGBl_VmIs69_rZKEemeloYZG0gBBfVH3tSnGMtoqP_WpFlQTBL28hMfX3evIs_Cnx2Lmbcedh6bO9F7wSjghDBymeH0RpSHZjnLDmxo4RiCHg8N-8HLhr9EGNX_XOnlFsGTUyxs7G0T6nc14-kifCrAniD3TsobzftUuiSz8Jw-nfImhY6yckrnZNtkETanBxIDYhIJaNT-4XYn151wWqJzGRl0-vUwuurGMF5TTFAZVhj67W1tCtT29hPrKX_Lk12KmFsWNg4oGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سکوهای استقلال در اهواز تقریبا پر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104930" target="_blank">📅 19:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104929">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b980e101bd.mp4?token=eyGT5ENkXEYf90sWdWBMBipiYJCxugQU-7nWZhP-IBXOZbGM7xadikskrx4XVZOJg4eouHYQ8LxjAvpct8vUKqpeBHfRC8DgdqN6QTVLS1-TOrh8079hO7np9hqg7ee5mj0esjeDnyTfsxK1aCRCGiZ1XBO8bdcX5TG5geMLVEGeuMR0xFsJJn7_hfjOqNpqahTyGcOOR7GczhfeC8ZtSKKKoOCzDL2VJjejYGJqcKnQz00kkqZ5gdFYCd6p7xU0SpRtpLffVtMvBmJK8ZrLhMG81T2WFJjyVvGsc-kofwmAKsyRjlnboO9Nw_poWYLs8g3zr-cC8GVBQlMXhKJcjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b980e101bd.mp4?token=eyGT5ENkXEYf90sWdWBMBipiYJCxugQU-7nWZhP-IBXOZbGM7xadikskrx4XVZOJg4eouHYQ8LxjAvpct8vUKqpeBHfRC8DgdqN6QTVLS1-TOrh8079hO7np9hqg7ee5mj0esjeDnyTfsxK1aCRCGiZ1XBO8bdcX5TG5geMLVEGeuMR0xFsJJn7_hfjOqNpqahTyGcOOR7GczhfeC8ZtSKKKoOCzDL2VJjejYGJqcKnQz00kkqZ5gdFYCd6p7xU0SpRtpLffVtMvBmJK8ZrLhMG81T2WFJjyVvGsc-kofwmAKsyRjlnboO9Nw_poWYLs8g3zr-cC8GVBQlMXhKJcjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
آغاز درگیری‌ها روی سکوهای فولاد آره‌نا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104929" target="_blank">📅 19:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104928">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f2a045c7.mp4?token=uLB1PzDHuukfNSyUUbPKcWp7Xlq5qTyxRE0tniN_s0IWgN_Gnglga68Hqsdj-9K-TliFfvgWvkoxrFfX4B37t5rjNBKPHpfOP5EeIgsVsBQY0IzzabvuT5DU_YlVa8uip592VHw7VVJxOZe4vNVJYBSP0epCRKKsg5Qmu9NamaHn8vaNnz7d4zpgAGpy9FchaigWrniOGXKe_0dyFee37xQqnxIFI7XkpDKD6vrKj0JeRvzybbjFgw78ZuqQxbVO7nXhQlDEkrLiowhPccDUJV7WKCeU94PJ8EXkHltUaPzNUQntlQQ2k2DEoQMz_xBy5K-XLQquTMbiNBHNMu03lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f2a045c7.mp4?token=uLB1PzDHuukfNSyUUbPKcWp7Xlq5qTyxRE0tniN_s0IWgN_Gnglga68Hqsdj-9K-TliFfvgWvkoxrFfX4B37t5rjNBKPHpfOP5EeIgsVsBQY0IzzabvuT5DU_YlVa8uip592VHw7VVJxOZe4vNVJYBSP0epCRKKsg5Qmu9NamaHn8vaNnz7d4zpgAGpy9FchaigWrniOGXKe_0dyFee37xQqnxIFI7XkpDKD6vrKj0JeRvzybbjFgw78ZuqQxbVO7nXhQlDEkrLiowhPccDUJV7WKCeU94PJ8EXkHltUaPzNUQntlQQ2k2DEoQMz_xBy5K-XLQquTMbiNBHNMu03lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
شعار هواداران اهوازیِ استقلال: فولاد به شهر ما خوش آمدی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104928" target="_blank">📅 19:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104927">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj4VN5WVGjMNhC0f9ZxKd5Hu7wcJAc_WH5mK1_r_Aa-VQJbv3aUUOZS56ov98FtzgeazsprEmzZtp5zWX2xbq5qngPeYWRXLM_b5TIA1B_SVQwPmbwewMAnTXl-1mHtox5fWb4IfyKurItMPxVJKz1arkjvbGnhBeOXzcyfq7hiZKdwDgSfvM68fddoE5Ga_cN7SIWx8CY1RgDG0hW_8Wxzcx4pXcNh65Mxs56_FUJp4VroqmPyj-sL7WVRobpIIzZwTZKqsnghmNlWt4Nwb6u5fC9ouSzbvLr62C0IGPcZijcNKEjdh91iOQoX0CGRxwlLeAhFyEwnCqeDK8OCmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری
از رومانو: رافائل لیائو با مبلغ ۴۵ میلیون یورو از میلان به گالاتاسرای
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104927" target="_blank">📅 18:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104926">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04a994664d.mp4?token=bWdu9Wi_WpqU0ymUVAiWO2csi7H9WEASYp84PT0o7aKNRyHHfFSoJ_Ifznw2awos52-PWzFqo4d1Jeo8xtpJcLoz7RfEJebrPhNnfVLNgBCH4nw8Hadtejnhvaxalhp6V45a8lSB7eC1-3_0K8PGPoV5SBfPEyNmlbtaQpTvwQa2AK6thj-Gk5igzZk8ge4BcQnO2bcMC6PnKlFB8ISohCteBZSyQZarl1lJz3MamwbJB29DlCpxV-ARQ_N_2GV8_2DR1m9r4Bpq_icy8Z3Nt0zScYj7vkqmeQIt6wBnfnoSZ8gEiyZKh1ZAOCeYyuJBmERwpyLG9tE6enRGIHeXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04a994664d.mp4?token=bWdu9Wi_WpqU0ymUVAiWO2csi7H9WEASYp84PT0o7aKNRyHHfFSoJ_Ifznw2awos52-PWzFqo4d1Jeo8xtpJcLoz7RfEJebrPhNnfVLNgBCH4nw8Hadtejnhvaxalhp6V45a8lSB7eC1-3_0K8PGPoV5SBfPEyNmlbtaQpTvwQa2AK6thj-Gk5igzZk8ge4BcQnO2bcMC6PnKlFB8ISohCteBZSyQZarl1lJz3MamwbJB29DlCpxV-ARQ_N_2GV8_2DR1m9r4Bpq_icy8Z3Nt0zScYj7vkqmeQIt6wBnfnoSZ8gEiyZKh1ZAOCeYyuJBmERwpyLG9tE6enRGIHeXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
شعار هواداران اهوازیِ استقلال: فولاد به شهر ما خوش آمدی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104926" target="_blank">📅 18:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104925">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf1KmLVbmT490wmQLKwYXsCXqclvhZBo2zALN3EFILx6IamLHBksctY5UzVWvzbvtvcXOW8MdCADzKsRDf-X_gbJPHUDIJ6CURkN0QXpufWNgg9BVrrk34me7amGfbozQZudzqhVPUWAyjQREnro_Ztxevh_fYrnmDyddtM14N2s4EZtN-pACijiOnVMIiPBBQSHCRk4YrazTOr9HtwRYxMOzH2_4OicrnbvdX9RJKInFtTw8Ltv9dn0i5_UTRCNMyvyRIXpL5yBHf-xNy4hN9NkCF_ZVKvzOA7TYqX4j3OJHBcyGYtIIbz_ffev9GRktGDzwNfWs8G34lGekElOUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ابراهیم امبایه از پاری‌سن‌ژرمن به استون‌ویلا پیوست. مبلغ ۵۵ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104925" target="_blank">📅 18:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104924">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31b21a19d.mp4?token=GhLzdtoCDtOiqEpn2fFhRl8gQWeDcOj0LJfM3A1zig4_cuiI2Kn99jptNTIFEzn9eelLl1U7OpprXZzoiCckuM0tPcfE_Lr3eQRziNp5jXNMLECwjHQ4c6xut2KY1Ejt2FR94itZVT3xrAFV6UL6rQsB1qHNDWdUzwIrX2trgTaEpzWSIVbvI_xXGXvhDhHWvO-7728_F9cmOvxZCAmQ2GaIFy7G0ndKRd9-1tSndWV0_SqglgZ2obgjKhTxmtRJLNEp_Mr1JEswydXrwq3u4VppNgxxjo_Cnpx12FQPd0bP2ibso8O_wM1n4aMIaINB5qweMbEDjjO7hFfwKma1cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31b21a19d.mp4?token=GhLzdtoCDtOiqEpn2fFhRl8gQWeDcOj0LJfM3A1zig4_cuiI2Kn99jptNTIFEzn9eelLl1U7OpprXZzoiCckuM0tPcfE_Lr3eQRziNp5jXNMLECwjHQ4c6xut2KY1Ejt2FR94itZVT3xrAFV6UL6rQsB1qHNDWdUzwIrX2trgTaEpzWSIVbvI_xXGXvhDhHWvO-7728_F9cmOvxZCAmQ2GaIFy7G0ndKRd9-1tSndWV0_SqglgZ2obgjKhTxmtRJLNEp_Mr1JEswydXrwq3u4VppNgxxjo_Cnpx12FQPd0bP2ibso8O_wM1n4aMIaINB5qweMbEDjjO7hFfwKma1cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
امان از دست هوش‌مصنوعی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104924" target="_blank">📅 18:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104923">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a984f5caff.mp4?token=urWibvwUi8v4AytM0TaP55YFSloNR50lWzLkUUT3vsy00N9lds_jwQICop0pfMYTVuxy--7prj8MTCqTaaVwM8e92aQvYY0qCQ_xgAo6ikM_685I90alFXMToug_5c-b74sX3otEPDbi79vCcfUJkOK_Dk9DAG7BQcXNLhqJD4h6USqo1KN-4hYblWpe0frzzs0rOZRxm1rrjtRQ81_bH-mzuJrjPvu3C9F7mH2exOX9Ggd9IK3ACDmsQjrOYFqOhsDsrfaH5f_T6Z7ASyjx8SNAR9f1doM8R1EVWUUa5E0sEuKCTCe2osmzwvicZZx93uW_BbA-3I6kLx2xvIzm8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a984f5caff.mp4?token=urWibvwUi8v4AytM0TaP55YFSloNR50lWzLkUUT3vsy00N9lds_jwQICop0pfMYTVuxy--7prj8MTCqTaaVwM8e92aQvYY0qCQ_xgAo6ikM_685I90alFXMToug_5c-b74sX3otEPDbi79vCcfUJkOK_Dk9DAG7BQcXNLhqJD4h6USqo1KN-4hYblWpe0frzzs0rOZRxm1rrjtRQ81_bH-mzuJrjPvu3C9F7mH2exOX9Ggd9IK3ACDmsQjrOYFqOhsDsrfaH5f_T6Z7ASyjx8SNAR9f1doM8R1EVWUUa5E0sEuKCTCe2osmzwvicZZx93uW_BbA-3I6kLx2xvIzm8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
امیرحسین صادقی: مطالبه هواداران و پیشکسوتان استقلال، اهدای جام است
🔺
یک تورنمنت شاهکار را به فشار باشگاه پرسپولیس برای سهمیه آسیایی برگزار کردند ولی وقتی به استقلال می‌رسند همه تغییر می‌کنند/ هواداران از من خواستند پیگیری جام قهرمانی باشم/ احکام وقتی درباره استقلال باشد زیر و رو می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104923" target="_blank">📅 18:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104922">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/877443a39e.mp4?token=dYc8oKbl_EJjZtnWc9WhAFtpfJnJ_Me9bKvkQuOBlNCJ1BH2rI_vJjSvBWjxILvNre0sH8VHyB1a8ZE-1L_derkJclAmmC91TjD7pIcBYwUWoFGjgcMo80csYWyyEw34y1t_WbGZRQGXD4CH35k6p0-OcWrFpe1uxlohknG-QTwBUOf3QqAk4iPn5WSmelxzLWdE6fyHxtbhgsMrCAIKsK1ieMJwPFZTbTskyfXAczNrBvzpjydIyMaZw5PI37IUDSGw21q71p0QAo7GlvyFFYpT0qLxZ9AWwC7GVunpxF2t4cjsixHYEu4JJGQhwCe2e86wTxzbsC-UdA1wjj_Bxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/877443a39e.mp4?token=dYc8oKbl_EJjZtnWc9WhAFtpfJnJ_Me9bKvkQuOBlNCJ1BH2rI_vJjSvBWjxILvNre0sH8VHyB1a8ZE-1L_derkJclAmmC91TjD7pIcBYwUWoFGjgcMo80csYWyyEw34y1t_WbGZRQGXD4CH35k6p0-OcWrFpe1uxlohknG-QTwBUOf3QqAk4iPn5WSmelxzLWdE6fyHxtbhgsMrCAIKsK1ieMJwPFZTbTskyfXAczNrBvzpjydIyMaZw5PI37IUDSGw21q71p0QAo7GlvyFFYpT0qLxZ9AWwC7GVunpxF2t4cjsixHYEu4JJGQhwCe2e86wTxzbsC-UdA1wjj_Bxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خریدهای جدید بارسا دارن از حضور در این باشگاه کیف می کنن.
😍
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104922" target="_blank">📅 18:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104921">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104921" target="_blank">📅 18:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104920">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJTGZHjaidG64O9f3TCaX7Ql59InYJVYQLQ_QXmKjkBnRpJqy8z-fN6re6J9fqAyJvIo_8taYngK-oNrJ2q7ukUjJJncTQY3S2ywSd6dxf6bAgeuD6r4kbKW-JpRx3kxW5XwNA1HmjFTZ6yXBQ7JNrxvcRC5PEe_wldHNIuotV_lYm19HrZd_sRo_bzfbs99V8R3m4WhPaxBBLrzjE9fGxt8-yjLf_Wc501yaN16cIiFA5O3zIoJEI8NsQn1mRHGNCgd6sRwwuIkjkw7KyoDgABayLIfm7jz0O9Vd0hFk-RYZnDrL9VCQ9wAMlt441JfvJh12QIlXLAxQZJzIWMt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
منچسترسیتی
🆚
کریستال پالاس
ویارئال
🆚
آلاوز
ونیز
🆚
میلان
اشتوتگارت
🆚
بایرن‌مونیخ
پاریسن‌ژرمن
🆚
لیل
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104920" target="_blank">📅 18:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104919">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hzqwg0FqNOHKX6MFkcXAZxBMv9Y5nMZAC5Oriuwr6vUr1eyDyJW_HOGDIsADPpZVngvSVwW70g9F4UcemYzXZPBSJRnCe1Ay2vS1ZHd3VvdU7Z4JXOv9DHhgLn74p666vf9sgz31yOmk4XE5eepns6ndfzwCewXDxKeEoq_xsJ7KS8Fg0F6RtyydXcHkZy8X9tGDxU_V5DDfnPZ1yZAQ82rhyM-sDfIbhGfXQvALqPlWBuyqHCP4gmhxGCdJChPMigWjfNWMKXvU0IOTjTHaVUV7FFEPa-bQoxhmDvNBiMbboOvwh4m95WTyzxxlTP0wJATtphMiyIqSchUksHd9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور مقابل چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104919" target="_blank">📅 17:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104918">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146c8ac859.mp4?token=MS2ngcE-fzYc8gP0x3W73WzWmrFX0v6YhRanItd1BKTjj1rkKoz2OW_Bq30u90BlLzRamb7w_afyfIBHZ_wx7qW_28p1tdKEaGKj8I5_0-DduO1vL4W7Pu5CMyhb-4xk0rWpZ_3hkcx_N3Twh_ZlO23ABTkAL-B6bs2dGchgS_8GD0Np9O6GWQrNfrLdsUmQzO-bKBGYg-IkhsZjO85dQ_LKOnWQeFZeguQ_Dt_GxG0ub8O5cPf7NfuGxHR94pgxF_UvzxOCnfrvLT1TSlF9Urti2nRA5is9YYE6vpBSNHDDzjP1EJ8F0fUB6PLqVIHV_q0Zfs3IBFdLZFdIQEV23g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146c8ac859.mp4?token=MS2ngcE-fzYc8gP0x3W73WzWmrFX0v6YhRanItd1BKTjj1rkKoz2OW_Bq30u90BlLzRamb7w_afyfIBHZ_wx7qW_28p1tdKEaGKj8I5_0-DduO1vL4W7Pu5CMyhb-4xk0rWpZ_3hkcx_N3Twh_ZlO23ABTkAL-B6bs2dGchgS_8GD0Np9O6GWQrNfrLdsUmQzO-bKBGYg-IkhsZjO85dQ_LKOnWQeFZeguQ_Dt_GxG0ub8O5cPf7NfuGxHR94pgxF_UvzxOCnfrvLT1TSlF9Urti2nRA5is9YYE6vpBSNHDDzjP1EJ8F0fUB6PLqVIHV_q0Zfs3IBFdLZFdIQEV23g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇺
لیگ قهرمانان 26/27 قرعه کشی شد و تیما رقباشون رو شناختن.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104918" target="_blank">📅 17:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104917">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f229668d9.mp4?token=eVXa12AzwjFnmXJ35RW1L9dK7OBHFYnykZZyhAEibjZUadLxldaiSDTfBhe1BurcIcItYrhMJKnDY1mYrJGVtR9fM4bJxCTVjskk6BLFvKxeuGIw3HhKQy6ZynD7W_a9CpjlLMwfDxJeyXHZGf82gMiNwJA5rPm6QLg48-XK2WOAwnE3C6Q5SwYG4zEIcDG8QZB3DKhrZOsLEDhCBtpf2699jbwLOY5xFf_pEa5tjkze_9myQGDeD5ap5CfcWLJIBTDQ8NzAQBfT83CQolOyS2yYV4lnHJzR1-UTOj4kDIy4T3iXU73mO11sDIfoW9xOfWhoipiOPayi9RYQjg167g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f229668d9.mp4?token=eVXa12AzwjFnmXJ35RW1L9dK7OBHFYnykZZyhAEibjZUadLxldaiSDTfBhe1BurcIcItYrhMJKnDY1mYrJGVtR9fM4bJxCTVjskk6BLFvKxeuGIw3HhKQy6ZynD7W_a9CpjlLMwfDxJeyXHZGf82gMiNwJA5rPm6QLg48-XK2WOAwnE3C6Q5SwYG4zEIcDG8QZB3DKhrZOsLEDhCBtpf2699jbwLOY5xFf_pEa5tjkze_9myQGDeD5ap5CfcWLJIBTDQ8NzAQBfT83CQolOyS2yYV4lnHJzR1-UTOj4kDIy4T3iXU73mO11sDIfoW9xOfWhoipiOPayi9RYQjg167g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
🇮🇷
صالح‌حردانی کاپیتان خوزستانی استقلال از هواداران تیمش خواست که امشب در بازی مقابل فولاد حتما در ورزشگاه حاضر بشن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104917" target="_blank">📅 17:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104916">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCyiOdyWPVIoW1ox-nEI7qEHgRcqmHu_QpHvEPECsYNA_xkdWE0rSxkThX-FP1ybCJ8gzF5nH-CpP6UUxGkybXwawDJ_TkZXP_sbMUM6qP-Axh5Y77bGwJ_Cq-d3NM3IekCHJ87gNmNcG3w2LkJnD326iTJ3GCsHyNW3037pJlO_-DHcShCTVLfdFTY_lUsxB8QGcBzq-NrMbYURnvLICCg1ily4lJO_ISKTMYGz9sCzi_4EbAFa_igLqOzJqBq3pOEkoKxm45_C4CpfglXVlL3Ic0RHZM1qLXvyJ3RNtY6ROTDX0YTtXCmELt96-dqlDe7SrJeWaj-QpMv5KqhZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
‼️
کادناسر: خولیان تصمیم خودش را گرفت. حتی اگه اجازه خروج نداشته باشه، هرگز به کمپ تمرینی اتلتیکو مادرید برای تمرین کردن برنمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104916" target="_blank">📅 17:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104915">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef920f58a.mp4?token=GjK7acvvu9TIhoPrgbpDFF3WzCl1hWa7WxDSM5JnBXVJTnzPEtUh2GsOmRKtNOfTikZytZVKzf7QHzhQeTsEagI0u7HhMLNBZYERnCjDpzEdLioOG7bTsPr6Q926lXQkA3KqSpujGAtvMOAZIVUoN7Wb1Ufeu298y-CZdxYBO1h4mwJPyuxtfIZ3F4i_i7Vl0iCAPwTGUIPYPUP1WoRk9sU6hiioNPEVpXDITjbgpfAF739defVAHYX6_AsL0oiKR-H0a3CwEY34dNHJJqyvc124XR-baT3_rOXKFSQTIlvNI-CU-zXONto-xGxiw00cjDFlmhy4_nimjna1wtyddQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef920f58a.mp4?token=GjK7acvvu9TIhoPrgbpDFF3WzCl1hWa7WxDSM5JnBXVJTnzPEtUh2GsOmRKtNOfTikZytZVKzf7QHzhQeTsEagI0u7HhMLNBZYERnCjDpzEdLioOG7bTsPr6Q926lXQkA3KqSpujGAtvMOAZIVUoN7Wb1Ufeu298y-CZdxYBO1h4mwJPyuxtfIZ3F4i_i7Vl0iCAPwTGUIPYPUP1WoRk9sU6hiioNPEVpXDITjbgpfAF739defVAHYX6_AsL0oiKR-H0a3CwEY34dNHJJqyvc124XR-baT3_rOXKFSQTIlvNI-CU-zXONto-xGxiw00cjDFlmhy4_nimjna1wtyddQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری شبکه ورزش : دوست دارم عادل برگرده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104915" target="_blank">📅 16:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104914">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddYAcpLxoxVUeQYd-W8bdySa1VCL0XEDOavo6CV5CEzKqCyYmQu9aSVESbdCS_LTxIy6av23EVG3SNAPleHXuECSKXEpU-POiVibnGYxkWOd-z5CcoFiMQUil0w6saHQMhSmYBdRwcEcBswj01KxQsVT6eM0u4IlrClcpo4rvQkrireMJW89FS37r8NEuqX1MVtVI8K7wrA55ZWmmehur9pAI3oyuV5c2BUEWt32QD5W4x1yCdVRor2E59tXt8N4t1yHGCyWr-CtPy-Ad0tlRDM31dyw7l1vEkyQjJy0oKp-TvcwihZRFu4mFBAaBtCKo9U6I73vGlMUc7Ou4W4_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
پیام هوادارای اتلتیکو در ورزشگاه متروپولیتانو:
«هر جا می‌خواهی برو، اما همین حالا برو.»
«اتلتیکو از غرور تو بزرگ‌تره، خبل مارین.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104914" target="_blank">📅 16:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104913">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04262aed7d.mp4?token=MLo4l0WS9VY6CQGHgpsFSrzNwyI3ChwzYEDp9CtmXPFokNbfOIgpZYMtGJ1B5_gFtnovZsUxuQ924pCXAoaO61sG6XLfbbFCwqtUX1NC6a7QrhACBDEiF6egIH8RM4bxYveWIy7RiZs4ikmg3hEbWmLnq92D9pG93wpgh2PcbxGs9gQvinVuttU3IyzvnwCdr84-EL_Mw-hE-xfMKxnsilLFajQy4Fdmd0-yzYL61AuCu3CYeq6EoRzM_KlaYRBFt9UPC8gTMt67cByQxFFQPOsJQkPzUPPV3ffrTkKSMTWgOCuAKP7vu7EAHC0kZwmAKHxDWXR10-PNUXgxMGJBkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04262aed7d.mp4?token=MLo4l0WS9VY6CQGHgpsFSrzNwyI3ChwzYEDp9CtmXPFokNbfOIgpZYMtGJ1B5_gFtnovZsUxuQ924pCXAoaO61sG6XLfbbFCwqtUX1NC6a7QrhACBDEiF6egIH8RM4bxYveWIy7RiZs4ikmg3hEbWmLnq92D9pG93wpgh2PcbxGs9gQvinVuttU3IyzvnwCdr84-EL_Mw-hE-xfMKxnsilLFajQy4Fdmd0-yzYL61AuCu3CYeq6EoRzM_KlaYRBFt9UPC8gTMt67cByQxFFQPOsJQkPzUPPV3ffrTkKSMTWgOCuAKP7vu7EAHC0kZwmAKHxDWXR10-PNUXgxMGJBkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
#تکمیلی؛ تراکتور تبریز هم اعلام کرده که امیرحسین حسین‌زاده را به هیچ عنوان به اردوی تیم‌ملی امید نخواهد فرستاد.
‼️
🇮🇷
از طرفی تارتار هم چند روز پیش مخالفت خودشو با حضور سه بازیکن پرسپولیس در اردوی تیم‌امید اعلام کرده.
❌
حالا مشخص نیست که زور و تهدید فدراسیون…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104913" target="_blank">📅 16:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104912">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=e-Glb0fYEqmXWE4EpKqPDWj-wDouqjiVPPwe9WIQo_gqeKNT7SG0OhJOsCosG2jZUMguWCSEq-r81F1w3r3DKXhXSbSqro0CWTF2538j6VWouQxgXJEphnEey67W6Su_XZPY4W2iIdoFc6vwCEQ64njiF_TOjjJt_bA2W0hfv2h1CEvMVnon3J37n38kwyVEIXBVcZ6sx9SfpkTA14MLigHrk4VYoHJDIjCrbglsrq1TntGe2PcU0KFgYqYg7cQP_9W0OkwmHuUWIeQedeWpVS7IDqd1zAdLWvW-u_TMtqkGsAksaKF3PpIVYPU-qarKp4JcnNZmPgiGp3O66VPWpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=e-Glb0fYEqmXWE4EpKqPDWj-wDouqjiVPPwe9WIQo_gqeKNT7SG0OhJOsCosG2jZUMguWCSEq-r81F1w3r3DKXhXSbSqro0CWTF2538j6VWouQxgXJEphnEey67W6Su_XZPY4W2iIdoFc6vwCEQ64njiF_TOjjJt_bA2W0hfv2h1CEvMVnon3J37n38kwyVEIXBVcZ6sx9SfpkTA14MLigHrk4VYoHJDIjCrbglsrq1TntGe2PcU0KFgYqYg7cQP_9W0OkwmHuUWIeQedeWpVS7IDqd1zAdLWvW-u_TMtqkGsAksaKF3PpIVYPU-qarKp4JcnNZmPgiGp3O66VPWpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تارتار: زمین چمن یادگار امام تبریز واقعا استاندارد نبود و کار را سخت کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104912" target="_blank">📅 16:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5141cf449f.mp4?token=hBR9a6WC99j8QZP7YHQTGZoI91bFWxMHgLyuHcW2CYxO2UmaGixGwGC1xw5_FEmLoBvhCkRLw734QGW-mZezugjKMRtpnSjXeWaBownlpdiIEYuVHhnPVOwl0vSirFsw1GjvcdGnDrOURJAPjlYNFc8yrTmV0Q72bdTLoYCLR7MGREgMF11zWqL1hNftZmNl9XeDVXsXV8iIQWPLrayd51XtGlM_5vIFV6TvGh-ssKIrCynlqssIIpVJ1nj8v87Q_ygWL6FxQ6ZKJnrrdpxUx7qzUXo3qUDtEzoF1YPZX_9ty9AmFTN5FD_KUZLxcFgjA6rSiLCb9ggIt6wJwOStt6A90IxGhpya2g61j712ZmjA_ThZhFye8i7ELGqJBxV7pPLgQjBmIPka14PkO4BizD3xfbB3UdJpSoYHoY_uoX2GV99fsMRAWES6CmGEWXUNqrVjElAPGScQrsE1bhXFJyadPG3ROlia8KJVMg_J8u4B5UwoCxGlX4Ne0d5QsnVsIWNcVOzkAsdLZ2S1KRtluCilSmYhOCGeJ0VQnRppxAfCheEVxJ_8z-z7_VOSnzM-XJZ0PXDb7uBLPBEG9KVhrVEPatPGPy3SP_byDjY6zH4g8ZnnSJUtnaTvutk8UTYgwKte0IJpgLztAz5_PP5D90Kttp0DngtB-JmCMFy-xp8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5141cf449f.mp4?token=hBR9a6WC99j8QZP7YHQTGZoI91bFWxMHgLyuHcW2CYxO2UmaGixGwGC1xw5_FEmLoBvhCkRLw734QGW-mZezugjKMRtpnSjXeWaBownlpdiIEYuVHhnPVOwl0vSirFsw1GjvcdGnDrOURJAPjlYNFc8yrTmV0Q72bdTLoYCLR7MGREgMF11zWqL1hNftZmNl9XeDVXsXV8iIQWPLrayd51XtGlM_5vIFV6TvGh-ssKIrCynlqssIIpVJ1nj8v87Q_ygWL6FxQ6ZKJnrrdpxUx7qzUXo3qUDtEzoF1YPZX_9ty9AmFTN5FD_KUZLxcFgjA6rSiLCb9ggIt6wJwOStt6A90IxGhpya2g61j712ZmjA_ThZhFye8i7ELGqJBxV7pPLgQjBmIPka14PkO4BizD3xfbB3UdJpSoYHoY_uoX2GV99fsMRAWES6CmGEWXUNqrVjElAPGScQrsE1bhXFJyadPG3ROlia8KJVMg_J8u4B5UwoCxGlX4Ne0d5QsnVsIWNcVOzkAsdLZ2S1KRtluCilSmYhOCGeJ0VQnRppxAfCheEVxJ_8z-z7_VOSnzM-XJZ0PXDb7uBLPBEG9KVhrVEPatPGPy3SP_byDjY6zH4g8ZnnSJUtnaTvutk8UTYgwKte0IJpgLztAz5_PP5D90Kttp0DngtB-JmCMFy-xp8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
تارتار سرمربی پرسپولیس: ارونوف یکی از بازیکنان خوب تیم ماست اما دیر به تمرینات اضافه شده است
.
بحث مصدومیت ارونوف جدی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104911" target="_blank">📅 16:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a61739d98.mp4?token=X9gGQHafBEv9Nn5RX-nSlu_RiZyvVArj05jnJxeP0JqeX76tdGKuP6bM5zdzcoZQHcGzlWCmTrDpOYS1MNHCA_nIqKToXrwqyic3RVJ5CAgrIw8Pb8TDMtgNa6b5JVl-MI0YwZ7DWTUDlHWnXvqJxsnbZTNjG27_W9xEnlIlFfB0QaULACF_OjoWzXJCLlMtdti-Jxd9ZzSGrZo-jXYnathc-l0HIojse3TOp3uNxeINwn7v7mDO-LrL9xD4fmLlXarzPIIJFJNVi76EOI771e3o3SWWA_xJu5C2lYN5MzdLd1kaWTfkOevsgyVrhZpE6p3pC_yg9ZoC6i5huwa9pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a61739d98.mp4?token=X9gGQHafBEv9Nn5RX-nSlu_RiZyvVArj05jnJxeP0JqeX76tdGKuP6bM5zdzcoZQHcGzlWCmTrDpOYS1MNHCA_nIqKToXrwqyic3RVJ5CAgrIw8Pb8TDMtgNa6b5JVl-MI0YwZ7DWTUDlHWnXvqJxsnbZTNjG27_W9xEnlIlFfB0QaULACF_OjoWzXJCLlMtdti-Jxd9ZzSGrZo-jXYnathc-l0HIojse3TOp3uNxeINwn7v7mDO-LrL9xD4fmLlXarzPIIJFJNVi76EOI771e3o3SWWA_xJu5C2lYN5MzdLd1kaWTfkOevsgyVrhZpE6p3pC_yg9ZoC6i5huwa9pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⁉️
داستان پارسال ماتتا امسال هم برای آلوارز تکرار می‌شود؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104910" target="_blank">📅 16:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104909">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🙂
🎙
از سری نکات شنیدنی امیرمحمد زند :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104909" target="_blank">📅 15:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104908">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0c43226f.mp4?token=Wtr-T_6S_oUOPikq-n3M2eQdAQAh5cr4DKCW8GpIOgGHeCTt9e3llZRi-RimkpnmX1AyAWaesqS1tTJYUUyz6HkDmuRnAFpkwbi9lV-DqoQNDAzWGgWY776pYc32B_ijsjtZ3NOjDhOFOZgQhdw2yQIkarMOYBUqYFWWKfP6gptvxFoEpnDjWZtGO09_eZK82o-nZw5bbuBtz1EeOaQelglkL-0hNSFEGIptpmHmxmZHEGu-3nw4n0rA4pnjcRfyZFh-N_-fWuzLNrFvOSIQKewbQhafyLwepPQTkftcMWaQGunQBm3iFpgt8Ge9WwFZy3Jk0Y_9ZJukH3ZP8E9wmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0c43226f.mp4?token=Wtr-T_6S_oUOPikq-n3M2eQdAQAh5cr4DKCW8GpIOgGHeCTt9e3llZRi-RimkpnmX1AyAWaesqS1tTJYUUyz6HkDmuRnAFpkwbi9lV-DqoQNDAzWGgWY776pYc32B_ijsjtZ3NOjDhOFOZgQhdw2yQIkarMOYBUqYFWWKfP6gptvxFoEpnDjWZtGO09_eZK82o-nZw5bbuBtz1EeOaQelglkL-0hNSFEGIptpmHmxmZHEGu-3nw4n0rA4pnjcRfyZFh-N_-fWuzLNrFvOSIQKewbQhafyLwepPQTkftcMWaQGunQBm3iFpgt8Ge9WwFZy3Jk0Y_9ZJukH3ZP8E9wmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
👀
هنر زیبا در ورزش جذاب هندبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104908" target="_blank">📅 15:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104907">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎙
🇮🇷
صحبت‌های شنیدنی نوید استادرحیمی درباره سهراب بختیاری‌زاده و‌ وضعیت‌استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104907" target="_blank">📅 14:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104906">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc259d7726.mp4?token=TcdD85TwMrThVazTXEmgXKASYoFfQDXyQzvvD3t-TTBik4KOfPxZ7Hqyb3YnDTEjnGe3WxTOekTIi7VFTv0NLaeheDqXvimt0mqgD5rk4nT1p4z2WQf0k8dqg7suUBWOktEd3QFAJ25PXX32OZAJhem3v6TTwaJMtYtr5i9g4Uihr0cHR1JWz4_Pt6QkB3gpHkBtcmtfksu8x3_C91IwhWVmL-gs6hBXBLOlDyJCQHoUkn1DjgeLgU0gVTeVqfKjzQ3yVCbBNbyvPmaUNu5h-WA2AZpgVXpnqDn3D7qlHSY7SJFUwPHD0H6p0fIpCq4B68es4D7k75Xv8ykSblQe5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc259d7726.mp4?token=TcdD85TwMrThVazTXEmgXKASYoFfQDXyQzvvD3t-TTBik4KOfPxZ7Hqyb3YnDTEjnGe3WxTOekTIi7VFTv0NLaeheDqXvimt0mqgD5rk4nT1p4z2WQf0k8dqg7suUBWOktEd3QFAJ25PXX32OZAJhem3v6TTwaJMtYtr5i9g4Uihr0cHR1JWz4_Pt6QkB3gpHkBtcmtfksu8x3_C91IwhWVmL-gs6hBXBLOlDyJCQHoUkn1DjgeLgU0gVTeVqfKjzQ3yVCbBNbyvPmaUNu5h-WA2AZpgVXpnqDn3D7qlHSY7SJFUwPHD0H6p0fIpCq4B68es4D7k75Xv8ykSblQe5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما فقط این هوادار کوچولو رو ببین
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104906" target="_blank">📅 14:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104905">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104905" target="_blank">📅 14:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104904">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUnp2-Z-uwUy-aafX1yazNRGau4WuPewAao7-QJwdnONB5WDDpgWVof7bgMjvCPQgw8Yfb0ANFUP0RRQsl3s3VgErxbq-WvA5xhPMhW3ryC4gtQLdIrANAX2DBeoBuoG9TLmj7dJOw3nxumvVMjerMVHJpy3RmDSyo-RHyQMZYfw1XdE3Xj7PSk-omLHeGV8_V7wVoY2tFQBGSuyGtBwdZJ40IKjS9bB_O5nzoRTMTQW5K-aVVVnJDflntahzEu5jlcBAdVmSQEkVdEt9Y9bDv2TJR7yTJfkx-jFWXVgNaYtwrIYhg4WasDNbV7uJzOVUkC9qzyGn9Axs9TZSDegaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد جذاب فوتبال ایران را در
TrexBet
پیش بینی کنید!
🦖
استقلال
Vs
فولاد
🦖
جمعه | ساعت ۲۱:۰۰
🦖
ورزشگاه شهدای فولاد خوزستان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104904" target="_blank">📅 14:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104901">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/676a532a06.mp4?token=a7T4F18cQIiY5zmEnPPiHIAAkT3pvuMTkY4O76bVI2_d3BUSQBrNuvUO7V0kWYG1pl-lzVEJJ2-V7zlBgHvNeMedFWUuTfZbYabHf7GCjqA56Ba2vGrItwRmNrj3bg9vOUYfx0hvOICDuLO-LcVG0va71-rMd3ZXr7EUloCUW5yY7Azm8co4m_Y2ilzueu7QO24SA-9YwIMGSMArTGedePcCLeVZosaTnWQxoI3xxrqKJ0nasw_pfzp2D36IAwbjtIfOcdDD_QaS4iiBQhpMsKUwS4CY8Dvj0-PzGApljBx4iHHIe5-rxEcMn2xoQIt8cEEv3W76EUARZwnsVs6-Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/676a532a06.mp4?token=a7T4F18cQIiY5zmEnPPiHIAAkT3pvuMTkY4O76bVI2_d3BUSQBrNuvUO7V0kWYG1pl-lzVEJJ2-V7zlBgHvNeMedFWUuTfZbYabHf7GCjqA56Ba2vGrItwRmNrj3bg9vOUYfx0hvOICDuLO-LcVG0va71-rMd3ZXr7EUloCUW5yY7Azm8co4m_Y2ilzueu7QO24SA-9YwIMGSMArTGedePcCLeVZosaTnWQxoI3xxrqKJ0nasw_pfzp2D36IAwbjtIfOcdDD_QaS4iiBQhpMsKUwS4CY8Dvj0-PzGApljBx4iHHIe5-rxEcMn2xoQIt8cEEv3W76EUARZwnsVs6-Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
پرورش نسل بعدی بانوان ملوانی
🤩
‌‌‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104901" target="_blank">📅 14:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104900">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f9954ef8.mp4?token=B1EqoG6w8R-f3Qq9IU4Id4Bha8LR7aBF-ScOj-1ARhcscNQH2nlRMmkQIeV_8D0nqedDt94wcy4U5XGd1oAo0mdbfXDOd2v_zbT18EkY1APJeR61E7R-I9omURPO5Z4O5pd2OkVxECbywXuNRXkoMcU_Zv_8xPYqgbSFDWDGrWiCGNTL7KlXNvmGwecTJkQbUl6ENRhhv2eh2PDKdDB1DoItFP04ykD3G6RFBmG-loeAkfvvk49GIXxoDY4jdTquL2gq-jxso7u53nba37Xad7tp5vtvh7RH2g4AS3Z3vXa9fEyEcztplH1fKjXH8A2rmphcNjMt8uCXXl6D1MAXNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f9954ef8.mp4?token=B1EqoG6w8R-f3Qq9IU4Id4Bha8LR7aBF-ScOj-1ARhcscNQH2nlRMmkQIeV_8D0nqedDt94wcy4U5XGd1oAo0mdbfXDOd2v_zbT18EkY1APJeR61E7R-I9omURPO5Z4O5pd2OkVxECbywXuNRXkoMcU_Zv_8xPYqgbSFDWDGrWiCGNTL7KlXNvmGwecTJkQbUl6ENRhhv2eh2PDKdDB1DoItFP04ykD3G6RFBmG-loeAkfvvk49GIXxoDY4jdTquL2gq-jxso7u53nba37Xad7tp5vtvh7RH2g4AS3Z3vXa9fEyEcztplH1fKjXH8A2rmphcNjMt8uCXXl6D1MAXNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
تحلیل جیمی کرگر و گری نویل در مورد شیوه مربیگری ژابی آلونسو و نحوه اخراجش از رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104900" target="_blank">📅 13:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104899">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TADfOGm3xlDlFluSaf-YI7azUVSVesEhm9Uj9OYRhsYLmY2jrkwdfKieEQedn1ysDZv1Xt09_AeVB4q_qQfI15QrpJFMa0mjsvKG06Gadw_1R77JmGX1acxuJNnOUmlwYpaAT2rfUzWjE67yS9Q2vLfuQIVtd9oagH8oCVPwfncyBkfGJsgxZYa4xd76IG8bdNHIJwpTJdaFKbkUnYYOCF8N4k_cJXYqwaWe3R3ujZNMT_p6twR1jZNKUNbgbyctGPfuK8bRXntlxjNh5eF7MR4QZaTx01dNrPSiXxbMrvUhezJgLiRuZp6Sdo7HjdMoXWqO-LthCxVnYvFCoiuong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
لیست پاری‌سن‌ژرمن برای دیدار هفته دوم لیگ‌فرانسه با خط خوردن دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104899" target="_blank">📅 13:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104898">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
🇪🇸
🗞
رومانو: آخرین پیام و شعار آلوارز به خیل‌مارین: یا بارسلونا یا هیچکس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104898" target="_blank">📅 13:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104897">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuzTgufHCBExKzInG0mmsQ66elso2kvWbMFz3MnyxaDYOIRiexVfZsd-fIGiaA1lPdD5grm34OkYyMyJ4M9xXBlEj0ulFVCJ6ve8TY4mJnDB5SYTKf1QdY4eQBa_U9by_3PzXuz-NPqYe3jJlVRRXEyImT-YtUzcfRdt15zsIR3g81_NrPIb7OlVzoCL-XtGDQB2-P4JBKDoMe7Lzj-aEH3ZKXTvVC7tv3NnclYoWTyITkkUxHOnV3Gu7AJA9_P-31-_d6zRnbb0R34nppcFuuT9uQMz6TS35x7Y6W0KOSpqEq21uPb0uSKhJbeivXR5xXZvAyvpe_meWHZJzbwGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
✅
رومانو: موراتا به لگانس HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104897" target="_blank">📅 13:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104896">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b74cb03b6.mp4?token=TrNbZ1qb105iICVORnjd6g5XB38_KmyYNjzvjJQLr2k7gPfLDIjpcS3dNrf-rX1-FyaA2GHnciRx8vHwEJPe7az-0_ydKYUPDyQVYRHhWJ2zl39EheqvkveVHjrLRluxwc2jnQyfZ_7CWQBqJogTn235_otqZc5LFkBuVuuIvOJcEQ3Zru9hI4Kf9htjoGVogum0pYrCu_9qoDzHjx2Pb6AilNL6EsZeeQl72MEnnIaZwnUGW_fHrB9ry_M_Pk6EOZIs6Beckh7q4lVw2_BGwb9jIzovOn3F4sXJFPJ4S2FHVpK5K742zYzViSYPQH3lJeN3ax7MNEflwKL_1Yo4ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b74cb03b6.mp4?token=TrNbZ1qb105iICVORnjd6g5XB38_KmyYNjzvjJQLr2k7gPfLDIjpcS3dNrf-rX1-FyaA2GHnciRx8vHwEJPe7az-0_ydKYUPDyQVYRHhWJ2zl39EheqvkveVHjrLRluxwc2jnQyfZ_7CWQBqJogTn235_otqZc5LFkBuVuuIvOJcEQ3Zru9hI4Kf9htjoGVogum0pYrCu_9qoDzHjx2Pb6AilNL6EsZeeQl72MEnnIaZwnUGW_fHrB9ry_M_Pk6EOZIs6Beckh7q4lVw2_BGwb9jIzovOn3F4sXJFPJ4S2FHVpK5K742zYzViSYPQH3lJeN3ax7MNEflwKL_1Yo4ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
🇪🇸
ادین ترزیچ سرمربی بیلبائو:
🗣️
باید مراقب انتقادامون از لامین‌یامال باشیم. با بازیکنی طرف هستیم که سه هفته پیش کل بازی‌های جام‌جهانی رو تقریبا فیکس بازی کرد. پس توقع نداشته باشیم بعد گذشت این مدت کم بتونه هر بازی چنتا گل بزنه. باید به این بازیکن برای ریکاوری بیشتر فرصت داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104896" target="_blank">📅 13:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104895">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHCBIupB-s3EWVUie3zadzWWYXd607HPn_gSjyXiRdl8lq_vAJL59YSKpO2MjwV8StnDfxXcUwsjingYOLLWtlnUlJH5-tW8xWPBo420WpuZNbTCkLfdB2Zijy-Ygtv74ThlWRTNGiWBvG3HAcRmiRuJJ_BYFQIhdNZ3eIup2cWnxiIJbpdO5BZ1T1eulj7gQC2_Kl5cDkIdJTfse-jjZD4zmfOH-azS2CqCkmz3zmDBxf31uqpq-Un050OtZ1GnQb0ngQb2wuc2KnXykGECVLdrGTRhBiR23A0ewp4HvfsE2zCvts72wqHt3tjx0MVPFKFEIsdIYK7BK7XIMMrinQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚬
🇪🇸
روزنامه COPE: آلوارز پرونده پزشکی با ذکر دلیل افسردگی به اتلتیکو ارائه کرده و تا هروقت که دلش بخواد میتونه سر تمرین حاضر نشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104895" target="_blank">📅 13:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104894">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnBwdnd7bUfWCg7k3Ha-k_zqhGxKOLzj_pNuZaNO72o9rAzQPkaDSjxU5WeL2Vr5qgUMHlqFkXh1tjSZwuPw6kA6tXnvFU1b3fYLvHMmMTGOI7L6wwByG7BavzVDJRKOFMiRKmzVeHDvKdtXtnRCtpkT3kHAPNEGZKRbsK4K7q4Y-zgseJM6UqRq9oxTjC1cbWSNeUp40EYquT4r1D6-9-6fANTxL0Itvtm17mf4YCmVbKhaBzOXMV8U7R-eQv9wn-_-8vEA40_kgHXT_YdAEVtkvIpDrVazbaLrAaat-CDac_NdDMQVP_hPi365BN74UJ1M0FTPb1MSOJ7JVDNQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
❌
خولیان‌آلوارز برای سومین‌روز متوالی در تمرینات اتلتیکومادرید حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104894" target="_blank">📅 12:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104893">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d697485bc.mp4?token=nF4HGV8Pw-qtDzXCgrHgfpHrp2DImOl5kTEoB2VoKBb2Kl9h7oE18FPkkRocBJWutqnPexHVaWw9RiCszaBhVDjIKl0r2FRf0Q-UCdE1LFwT46taEyFC0gCIRb0xYu4jcczChCGFKDh93ap87tBr1o2FjBIJA_OdEiLz9Y6x5DAZaSULfW9QEYQx-bjJswuvVdJCJaQ8VkCFC81eTrepxKVsCbtIxPgLxWNtdk3WPVEK0MSDEebJTiHhmdLsjIDt2JcUGt1ZhWCgyoZ9pLJxi6XxbuETTK9LWl2vdFpodNlgtNT8-wUY9Y3dQ7c4-SRMXxv5InKEWyLsird515Simw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d697485bc.mp4?token=nF4HGV8Pw-qtDzXCgrHgfpHrp2DImOl5kTEoB2VoKBb2Kl9h7oE18FPkkRocBJWutqnPexHVaWw9RiCszaBhVDjIKl0r2FRf0Q-UCdE1LFwT46taEyFC0gCIRb0xYu4jcczChCGFKDh93ap87tBr1o2FjBIJA_OdEiLz9Y6x5DAZaSULfW9QEYQx-bjJswuvVdJCJaQ8VkCFC81eTrepxKVsCbtIxPgLxWNtdk3WPVEK0MSDEebJTiHhmdLsjIDt2JcUGt1ZhWCgyoZ9pLJxi6XxbuETTK9LWl2vdFpodNlgtNT8-wUY9Y3dQ7c4-SRMXxv5InKEWyLsird515Simw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
یه ویدیو کاربردی ببینیم؛ با این روش حافظه پنهان و لاگ های قدیمی گوشی سامسونگ پاک و سرعت گوشی بهتر میشه، حتما بعد این کار گوشی رو ریستارت کنید. نام گزینه :
Delete dumpstate/logcat
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104893" target="_blank">📅 12:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104892">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cca0ed089.mp4?token=aQ_h2xqz4_9gPodSykGDuNyJiZVHoOFPDxvtvH4hSUbTKna-iltfnvY61nYsd1SYpM1la74gDP51joiKXePBEofGF_dBe6CMWoLRXdmJgILoF8oleKzyDsAzgz-R6Wm9wFrRNGKSmw9ApVA_YGLvZtS3wh2uOICJA5XGYCPG-cNcSqRvqRvK25DXYCiS266wbAkPCwL6s5Fwt8Foe0Z36iuYlezOstVCtsn64zVGckW0cKJMs5YdpZYuDQiMlXB2d-kQopC5DSiYgZ5RGwvlOWMgJKCzH5DIG5eIeLkj39Jtmap2HMs80uYTrffvFyy37dHPpITFtXIau9fP7jaHmV3tda-lUHmVY059i3KJz2_182WssVVsGDm37CFoH78cdIrPwbyHtLj-apX2IFAkT8EARbDjQ-4g8Sn0IpX5eOhlI7GP8pfG8iOomQRCZVMi5gT5Nw7DO6JVeHFfUsUeODb-Spv6N6oqyz-aIwtgWLB0UY_uT94PGN2Db6IXFAGOrLH6q4FVpZn0euWdvElocXmCpb-pg8o89aQB0BD8fkSwf7jLcu5MJZ0HHGrodJC4rA9yNwEOaRtiHuq19s3Sln7LlibzjljsH_-ap9_jU2yN1zFKoIjqOmgRTi2b_FxzFX08Fqlevm1Um4dXhkNgeEhbFnpJACjDS9zLy0DNXNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cca0ed089.mp4?token=aQ_h2xqz4_9gPodSykGDuNyJiZVHoOFPDxvtvH4hSUbTKna-iltfnvY61nYsd1SYpM1la74gDP51joiKXePBEofGF_dBe6CMWoLRXdmJgILoF8oleKzyDsAzgz-R6Wm9wFrRNGKSmw9ApVA_YGLvZtS3wh2uOICJA5XGYCPG-cNcSqRvqRvK25DXYCiS266wbAkPCwL6s5Fwt8Foe0Z36iuYlezOstVCtsn64zVGckW0cKJMs5YdpZYuDQiMlXB2d-kQopC5DSiYgZ5RGwvlOWMgJKCzH5DIG5eIeLkj39Jtmap2HMs80uYTrffvFyy37dHPpITFtXIau9fP7jaHmV3tda-lUHmVY059i3KJz2_182WssVVsGDm37CFoH78cdIrPwbyHtLj-apX2IFAkT8EARbDjQ-4g8Sn0IpX5eOhlI7GP8pfG8iOomQRCZVMi5gT5Nw7DO6JVeHFfUsUeODb-Spv6N6oqyz-aIwtgWLB0UY_uT94PGN2Db6IXFAGOrLH6q4FVpZn0euWdvElocXmCpb-pg8o89aQB0BD8fkSwf7jLcu5MJZ0HHGrodJC4rA9yNwEOaRtiHuq19s3Sln7LlibzjljsH_-ap9_jU2yN1zFKoIjqOmgRTi2b_FxzFX08Fqlevm1Um4dXhkNgeEhbFnpJACjDS9zLy0DNXNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⏸
آنالیز فوتبال استقلالِ سهراب بختیاری‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104892" target="_blank">📅 12:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104891">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCWOmgTa63Aznj0C52EyymWsDAUQ7nUNDE61A5cjwfsPGCpfZQQxy9larj7fSmCKRnVMEdnnZYuiqMjQHTqWwJnLVfh183WXNbiugw-Kw-iHZp0mRP_LiJkW3zlI0sGEp8A5YTakzVG2jCQEpvPbwbLJQqOEP99lKq6loTok341Jnm0CrheNDE9dTmWjRK2xmRhVojWQhH5o8IDgAwf521vjlxywx3DoMBRXU5rZCf_WDcuE6b21gS2GMgN4DvJx4ftUdL8l6Mx9N0ulpldsdvKYkZ5BisNAuVQfy94AmhYregpZtZJxmSjHdOHexuRQBOFs1XUR2qIsJjjzome3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🏆
بزرگترین بازی‌های دور گروهی مسابقات این‌فصل لیگ‌قهرمانان؛ سیوش کن بدردت میخوره
❤️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🆚
رئال‌مادرید
🇪🇸
🇪🇸
بارسلونا
🆚
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🆚
پاری‌سن‌ژرمن
🇫🇷
🇮🇹
اینتر
🆚
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
بارسلونا
🆚
پاری‌سن‌ژرمن
🇫🇷
🇩🇪
بایرن‌مونیخ
🆚
آرسنال
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
بایرن‌مونیخ
🆚
منچستریونایتد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🆚
بوروسیا دورتمند
🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد
🆚
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104891" target="_blank">📅 11:52 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

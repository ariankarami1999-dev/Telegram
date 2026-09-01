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
<img src="https://cdn5.telesco.pe/file/fIG_5VExzUQQAmoxnmEfo8a0FUp6HI_KBf7L3h6-IpMBO_EynZip0hItmUlUcSmUsLtPicqcxg1ZYcgfpu42bs-Sh50OGPnrA8gY46AoCpdetsw2dtULYun7D8BQzh1CtQ022xcn3FyzP66BuaJDtkE2IyXNgo0_ahKOxh8NHJvKdTs1nT21xDnoV1hx-CxprK9T-tA_sce86jwN46MKO-uvhqoqGz87DXYGWXe5jBEP3Yxg5ZHlgr3HgjbVJG9WFnbc0B3ezCwPuiawcCkPI79c4oMRT9G8rS6PmXMrHL6Wiaw9iTgUZBJPZ_md-QKUKC7s4ASB2msdi33YhQYYfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 432K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-105298">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=frZ5gOD8rFSi2J5YMgrh7zoxPDjwyHvtWqICIVH0lAHoEqnSbtvJHll9S_4wIA-8dcfkoEq6oaArSpnTXq-TNgGD61H_FUo4A-u2hPKn7yLgkKwdRlrah5z5AdKjrfIFpsKJ9QHAsZOnh-rMby1bLbsRyzXjTm5k84u5ATSV6x0Wcc3gIH0Cj2a9VmqTd-vFESKEmU72XJyuCJSWUmVNju7eToCQNTi42YCgGYeDk8nteRFYrOOz-AhJWZTkfDTKgxEcMNKEaCEs57Nb-b9D34B7D4kYygLFKLL6pnjZ0xbRy-ycpzNcncB1-_pwy21K9oAiFlHVh1jFc2M-HFtU6izFRmKNztIolc52bXUFxDoyxZ7kMECvZAJl5341UPWlK9YMkCgl63VX61kyslSqB433fXz2KrOO08UJ4Ux6EqDUhHlk0MsI_kyhP_jvMTSp7FbZjvleQ_DLSZDXxXANa6uzZpgGxag3GqftSKTf0z8eKW-xWCEXnyAerfwoGn11AC1eS_hOw4RmfnDYtiMeM9-tPmjJX3NP57QlGpZwo9tF_2fV23pEb9FRjF-9f-1-gWJQ_UrqcvIM6hFQibpLdyXqo3t7TtG7Fk2OXL6UMwAlouL9smwP-EOnw1Cz-5lthjhkduB1BgnsQnPxxsi03st6I8n4J4WRYnwwO9Y8A0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=frZ5gOD8rFSi2J5YMgrh7zoxPDjwyHvtWqICIVH0lAHoEqnSbtvJHll9S_4wIA-8dcfkoEq6oaArSpnTXq-TNgGD61H_FUo4A-u2hPKn7yLgkKwdRlrah5z5AdKjrfIFpsKJ9QHAsZOnh-rMby1bLbsRyzXjTm5k84u5ATSV6x0Wcc3gIH0Cj2a9VmqTd-vFESKEmU72XJyuCJSWUmVNju7eToCQNTi42YCgGYeDk8nteRFYrOOz-AhJWZTkfDTKgxEcMNKEaCEs57Nb-b9D34B7D4kYygLFKLL6pnjZ0xbRy-ycpzNcncB1-_pwy21K9oAiFlHVh1jFc2M-HFtU6izFRmKNztIolc52bXUFxDoyxZ7kMECvZAJl5341UPWlK9YMkCgl63VX61kyslSqB433fXz2KrOO08UJ4Ux6EqDUhHlk0MsI_kyhP_jvMTSp7FbZjvleQ_DLSZDXxXANa6uzZpgGxag3GqftSKTf0z8eKW-xWCEXnyAerfwoGn11AC1eS_hOw4RmfnDYtiMeM9-tPmjJX3NP57QlGpZwo9tF_2fV23pEb9FRjF-9f-1-gWJQ_UrqcvIM6hFQibpLdyXqo3t7TtG7Fk2OXL6UMwAlouL9smwP-EOnw1Cz-5lthjhkduB1BgnsQnPxxsi03st6I8n4J4WRYnwwO9Y8A0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
حمله شدید اللحن شجاع خلیل زاده به عادل فردوسی پور: همه می دانند فردوسی پور با تراکتور مشکل دارد!
💬
شجاع خلیل زاده: من دو سال است که فحش می‌خورم اما خم به ابرو نیاوردم/ فشارهای زیادی روی من است و خدا را شاهد می‌گیرم که در مقطعی می‌خواستم از فوتبال خداحافظی کنم اما این کار را انجام ندادم/ دو سال فحاشی به من شد. تمامی این فحش‌ها تقدیم به عادل فردوسی‌پور/ همه مردم تبریز می‌دانند عادل فردوسی‌پور با تراکتور مشکل دارد/ از زمان برنامه 90 همین بود، الان هم همین است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/105298" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105297">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1acbc66f12.mp4?token=nVr9qQPitRX_pH1LS1d3_7t8e6oxRP36GGNMyZLoqlVyedIxkhVK5QNRp1LqOVJ-mJ4Lj0WDdCclBskZ-uxn4EksoGmowSr9ObubZ6YeOSVImoSgB_1O5e9suOU68t2pYkQC0leqwfyuA9zobT70OfvpSkethFmMh9uID-2kO69IPRdS0gPjw7xuOTMSqtFvvqSTxGuS2-lSfjl-vh0-LEcodlpgxEdHmdtbnITB4V4X7S2dOFglESRL-2nLm6VgAYX1N26w_hiPq-OsHvtB--7sW9wkPXJBuzpbj2ZKbz61QX4cLJOcvNnR9LAlc11LCq91hFNjqoiw8nubKqCrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1acbc66f12.mp4?token=nVr9qQPitRX_pH1LS1d3_7t8e6oxRP36GGNMyZLoqlVyedIxkhVK5QNRp1LqOVJ-mJ4Lj0WDdCclBskZ-uxn4EksoGmowSr9ObubZ6YeOSVImoSgB_1O5e9suOU68t2pYkQC0leqwfyuA9zobT70OfvpSkethFmMh9uID-2kO69IPRdS0gPjw7xuOTMSqtFvvqSTxGuS2-lSfjl-vh0-LEcodlpgxEdHmdtbnITB4V4X7S2dOFglESRL-2nLm6VgAYX1N26w_hiPq-OsHvtB--7sW9wkPXJBuzpbj2ZKbz61QX4cLJOcvNnR9LAlc11LCq91hFNjqoiw8nubKqCrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
تناقض عجیب در صحبت‌های پیام‌صادقیان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/Futball180TV/105297" target="_blank">📅 22:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105296">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
آغاز حملات موشکی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/105296" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105295">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2a82a31c.mp4?token=dgxLNUANp-z0UHo4KHxGPlKK92U_C1B11fqj3alCXrcHqI4GbJPI1w4_USwuEdShGrQKHlXBv3bXfL9G5oKyV26yQ20SsZI3w6nskuqgaad28hnulUC0ovBFl1mJFHEw2gK1gXXnMwCcXb2dBkvPPtj5MXvevUp2SoOLll1EuVWK8d0k7PH2uLFOANN3JxokdGEU2yV9tG4khY4fmwpdNmbIZnhIM3I69feyHSWNbtm7Wk5aN_rgt8NL3rOGaCIbyB1WvvbUnQLOnEc006ushDQwC3XAQq1jiiMYfvIZ-LQJTrMKTGu8O_JFLLaCmPTOzlxbpXGnb_BIPMN-E3c7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2a82a31c.mp4?token=dgxLNUANp-z0UHo4KHxGPlKK92U_C1B11fqj3alCXrcHqI4GbJPI1w4_USwuEdShGrQKHlXBv3bXfL9G5oKyV26yQ20SsZI3w6nskuqgaad28hnulUC0ovBFl1mJFHEw2gK1gXXnMwCcXb2dBkvPPtj5MXvevUp2SoOLll1EuVWK8d0k7PH2uLFOANN3JxokdGEU2yV9tG4khY4fmwpdNmbIZnhIM3I69feyHSWNbtm7Wk5aN_rgt8NL3rOGaCIbyB1WvvbUnQLOnEc006ushDQwC3XAQq1jiiMYfvIZ-LQJTrMKTGu8O_JFLLaCmPTOzlxbpXGnb_BIPMN-E3c7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری فرشید باقری بازیکن اسبق استقلال: پاتوسی سر پنالتی چیپ دربی با فرشید اسماعیلی درگیر شد و ما جداشون کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105295" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105294">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8d66f699.mp4?token=AR72EBba5VRLdhMsy015AcZhjDFTUd_Pl2f_6MBR2-OJPWm7ktRPZEfPkcUhVqcfnB5nbk224FEXqNIibabyzf0F3bJtdI7F09rLE0i00DgkReEnyuSBAEt9JnlY4DF3gVY2D9EMgZqP-ma-bGAR5Fk9ExWefF1oBgU46a-2DuuU1FU70rSqsx3KU55NXnxDgNDE7SgfoVhF_f09jzhHAltGk5HEyAH1bpko9u6kPZWwas-wkSPnNnEV9LvENr-CQJbtKK-Q0nfUCifLSbTGY6BDV4SBgrhPOdnSa4k8DPOlT7wRKcaM3Wj-Tri2_NNFgMpM7OpziXP_cO9CGiDDQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8d66f699.mp4?token=AR72EBba5VRLdhMsy015AcZhjDFTUd_Pl2f_6MBR2-OJPWm7ktRPZEfPkcUhVqcfnB5nbk224FEXqNIibabyzf0F3bJtdI7F09rLE0i00DgkReEnyuSBAEt9JnlY4DF3gVY2D9EMgZqP-ma-bGAR5Fk9ExWefF1oBgU46a-2DuuU1FU70rSqsx3KU55NXnxDgNDE7SgfoVhF_f09jzhHAltGk5HEyAH1bpko9u6kPZWwas-wkSPnNnEV9LvENr-CQJbtKK-Q0nfUCifLSbTGY6BDV4SBgrhPOdnSa4k8DPOlT7wRKcaM3Wj-Tri2_NNFgMpM7OpziXP_cO9CGiDDQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
💥
خانم‌مریم‌یکتایی هستن مجری تلویزیون جم‌اسپورت و گلر جدید تیم‌بانوان باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105294" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105293">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFdSsDuEIWUGDFAE7bwjbAqvtiGACCNCiJQP2aZ7sK62VwGnFm9mQEQBFUEaTFG4vdZ8fnhvvNyyT1lz3sQmKPY_pL2rN3HH0X2FkSfxRVHCPLLIi9V1_SXWCDo1Wkq-8MzjloisE5DZOHCettJU1r2lJ7RlAC8YuKnonE9eXC6OsP-Tc7i8z6P8fM1c4TH_cV0vJsOrFiRNCFC3rGA0TFvP7MecPAdSab81feb4qJETO78Kq34eDcShWfUi_LMyQDzGI-mJCubiedDrOjaqcIT7guG7Doku_NTmsbTWTgY8t634BU9Efn67se8BdVeO3YITobEm0z9VxTmMjLLT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
#فوووووری
از ترامپ:
🔻
‏"در حال حاضر، ایالات متحده حملات هوایی را علیه اهداف ایرانی در نزدیکی تنگه هرمز انجام می‌دهد. این حملات گسترده و قدرتمند هستند و در پاسخ به تلاش ناموفق ایران برای کارگذاری مین‌های دریایی در این تنگه (که در حال حاضر عاری از مین است، زیرا مین‌ها یا به طور کامل جمع‌آوری شده‌اند یا منفجر شده‌اند) و همچنین شلیک هشت موشک توسط ایران به پایگاه نظامی ما در اردن انجام شده است.
🔻
اگر ایران به این حمله توجیه‌پذیر پاسخ دهد، مجدداً و با قدرت بیشتری و در سطحی بالاتر مورد حمله قرار خواهد گرفت، اما این بزرگترین حمله نخواهد بود. بزرگترین حمله هنوز در انتظار ایران است و وقتی به پایان برسد، از جمهوری اسلامی ایران تقریباً هیچ چیز باقی نخواهد ماند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105293" target="_blank">📅 21:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105292">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649b5fb52a.mp4?token=H4D2xUKcD4B7Aq0DAKMGE0wB9-C0VZd_dVYEOfkESQU8nYUZDpI3p4jn1PVnIuSzKrHPxt2KrKeeRbg-QCXIjPH2XlL36o3XCerY5o3y0_Upxxaac6uzLRh-akfmOkWpZ0Ge4RVELdhtLm0rKJoHrcEz0xpWMI5JTGDFWTkWe0JqwJyQi5n0EFZ_qeeAngFdX-8sZWPvSJ2_v2j2bOCaE2ZcEcoxXhZbsKdd9S0yIP4G80L1xMJgPshIel2moyQZUcUzH1DyTsp9lkQCdMzDriIO_CDjvIq6MuwOCd602THj9F_aMXAWza1BL-CDi5OnkthRXtLybmzhu23ypvwOBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649b5fb52a.mp4?token=H4D2xUKcD4B7Aq0DAKMGE0wB9-C0VZd_dVYEOfkESQU8nYUZDpI3p4jn1PVnIuSzKrHPxt2KrKeeRbg-QCXIjPH2XlL36o3XCerY5o3y0_Upxxaac6uzLRh-akfmOkWpZ0Ge4RVELdhtLm0rKJoHrcEz0xpWMI5JTGDFWTkWe0JqwJyQi5n0EFZ_qeeAngFdX-8sZWPvSJ2_v2j2bOCaE2ZcEcoxXhZbsKdd9S0yIP4G80L1xMJgPshIel2moyQZUcUzH1DyTsp9lkQCdMzDriIO_CDjvIq6MuwOCd602THj9F_aMXAWza1BL-CDi5OnkthRXtLybmzhu23ypvwOBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🍷
تلاش خداداد عزیزی‌ برای یاد دادن اصطلاحات پیک زدن در زبان فارسی به اشترکالی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105292" target="_blank">📅 20:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105291">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0375b01ecb.mp4?token=XhwvXTfGUNpXhb_xNHGsVMdxzyXebdDtay7sgZNlzgZIS-q2ja_k0x212g7fWUYftgyrw1CVYHLK0yczczlskQeeHBywrBq1O4u_3B-dJkaHa8H21THNDc-5cNHXurl_9IBcKj6ZEa8uJxf9PI_Jn-OkrXrpDZtOAgZfcnbHeGkDCn3WDA-6wMUV2zoHAVpwc89QlxxEHdyLd5Adhs4G1IzOgK9Kd8ESzdnOigAJuM61a5osmYpmL5SySQjbbpH8nra0itVfRI80dR7tlFRAdcHfrEQLkx0EqKLs0Az7tbxordwJokG5CujjVSacGgRA5SKDnV7MVKCC-zAp1gzv-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0375b01ecb.mp4?token=XhwvXTfGUNpXhb_xNHGsVMdxzyXebdDtay7sgZNlzgZIS-q2ja_k0x212g7fWUYftgyrw1CVYHLK0yczczlskQeeHBywrBq1O4u_3B-dJkaHa8H21THNDc-5cNHXurl_9IBcKj6ZEa8uJxf9PI_Jn-OkrXrpDZtOAgZfcnbHeGkDCn3WDA-6wMUV2zoHAVpwc89QlxxEHdyLd5Adhs4G1IzOgK9Kd8ESzdnOigAJuM61a5osmYpmL5SySQjbbpH8nra0itVfRI80dR7tlFRAdcHfrEQLkx0EqKLs0Az7tbxordwJokG5CujjVSacGgRA5SKDnV7MVKCC-zAp1gzv-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به جمع بزرگان تاریخ منچستریونایتد خوش اومدی، برونو فرناندز
👏🏻
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105291" target="_blank">📅 20:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105290">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdSEgtueWn2EwJddYIU16zOUf-49iHem1o45ybygg36RB5bvp9JnC25FArqeBsMWEIVrxYmKWQMQH4-db3aQKtbzFxd-2LcZLp2KDUHATEp8A8i29cTAL4BP0d7vN_0TVpS92JvJSuvEP3dVsRtuibnPIlrPR2uyp6gWJQ5l1oax_7zvJwTCx_RVa9B8rZnKAKl4QERBsCI6SZ7_2UlOqGbfska1zVn3kA-fRpf2OFh9Cghzcgqb6gHsM-DOJ6jYN6AQHzwRHq-c-gr7MLBmanGt5yZ1m89F7duCuL4OYIl5-Kar029ztNSK7wPRD1ckBpyhnNy8lrHUJNUIM7dVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
ترکیب الهلال برای دیدار با الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105290" target="_blank">📅 20:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105289">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
موج جدید حملات ارتش آمریکا به مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105289" target="_blank">📅 20:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105288">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUsgIgh-CY9Z2Mnctrs4uVnj0ZED_4Wr2SN_Ux0IimWONRED6cn1vSMt5jlhU3LK4h6zit3lGGR7Yd8wzUZCn4dKh6Cg0Tq5S2f3dRL4gYTDbeKOOzQbAWuR8Qi813PJLJfYJBjNtn_I4jEv8qLko-Z_B7dHk5K8g0HcaH-CySV1ZRN80w43U7Z0PyKjnal1aEeXygxH62SWRx9E4MOLXnoIT8BaZlygrryc8nU4u4l3a3fZxKSoRkmbWooEtvUMRgHLVmjMoDLqx2cYmJ8knKCl2gpVo3WkbrPP631qv066k6X-XSPtmAkQUX5jx-pXq26n4WxGOgkhicaGfGTPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
ترکیب
الهلال برای دیدار با الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105288" target="_blank">📅 19:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105287">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
موج جدید حملات ارتش آمریکا به مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105287" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105286">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
آغاز حملات آمریکا به نواحی جنوبی ایران از جمله میناب، کنارک، چابهار، قشم و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105286" target="_blank">📅 19:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105285">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
متئو مورتو: مارک کاسادو با قراردادی قرضی به لاکرونیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105285" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105284">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo05yuHkrGNbR1wB66QGWcYzNssWbLI-M3NDw0OC3VftNhljH2yaPn8OWVJNf7GYpzkNm7cyqImpxWW8oiDhgIcxJwpguBGucEdFSFZiX2eQq_Q6x32cW23rIqE35I1KkoJNfgjk9Xzy5XbDQ3I1boOBsYLFErbBqA9kIpZcxRMAGqFpFQrs3hW5GXIsriEeUgJuZHQudkgo0FPNduwE1eVo-ckZpitlqzSCVNdh-FqAS79npfnxDA8gF0bSt0KKPn3_64jP_8Yd_r7CyThT336ypDd413fCF3UsT_AKsXlhyrXEjBiW-IoT4ww2Y2RoWf_kfnlu3iIdw0PYnWoA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
متئو مورتو: مارک کاسادو با قراردادی قرضی به لاکرونیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105284" target="_blank">📅 19:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105283">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
آغاز حملات آمریکا به نواحی جنوبی ایران از جمله میناب، کنارک، چابهار، قشم و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105283" target="_blank">📅 19:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105282">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🎙
🇮🇷
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری پیش از دربی:
🔵
دربی همیشه خاطره‌انگیز است و بازی‌ای است که در تاریخ برای بازیکنان ثبت می‌شود. ما شاید موقعیت‌های بیشتر و بهتری نسبت به فولاد داشتیم ولی استفاده نکردیم ولی از بازیکنانم با توجه به شرایط هوایی اهواز راضی هستم. امیدوارم بی دقتی هفته قبل را فردا جبران کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105282" target="_blank">📅 19:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105281">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep68WtputvOLQKNgMleraEHooJ0GVEL7DBD6VHhGv1zD0ympnnadbmcvQRoVhRPCV0rfwvVl2c8gCds-zzyTIBKHMQMoee74nVC3ftQUBxMeRaSWHmkF4okbE9jNLAHjrtMzol0MqpfE4ZMUfKi_7cfpoNTqglEmmSHE3JS-lQtpCG7xCQ5OCXrLy0ZTm6lG70Z_0CCM3279WGHxLL1XMMtyvrAp1Qyh9VObJLpWgOw2aDGpG3baqxpSkdHiBnfKjSAkRirvAZPE7voW6UCGgCQuM3xLMOJnZximrpyLNlCbenTO6yWo5hhTFvhheiDGj-ku-x8p9wY215XqbgoFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105281" target="_blank">📅 19:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105280">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=Ck_lC1AnkTeegvyYrlbhAxL4nJNa9ywGunk66NRGIwUKHUW1v1sxnpjsrQ4gvoV4V-YYx2V7hbAHWA3REXHUwYSVigR2zGGNJwiA7GVdB5fbl1JrHZiyN1QlKCpueYQce9MHsX4TnigmnIlRxbUZkbIHYGm1ztnbCXxVkSLoyK3EadNvndrLVTzphoyXEzYK6cDE6eFuuhXz4OfH2nudajBMfP_CR254WlP3eMbbaV6Vl0IV_A-DS_rDL2DTKbLq6FBDdZ5yYY4SJ61AiP4FMQNQ14PwfOgz9idw0hGPJq0v5lGJvX1qmet52wp7CxExegHRN3YHnjRmr-MYSJmcOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=Ck_lC1AnkTeegvyYrlbhAxL4nJNa9ywGunk66NRGIwUKHUW1v1sxnpjsrQ4gvoV4V-YYx2V7hbAHWA3REXHUwYSVigR2zGGNJwiA7GVdB5fbl1JrHZiyN1QlKCpueYQce9MHsX4TnigmnIlRxbUZkbIHYGm1ztnbCXxVkSLoyK3EadNvndrLVTzphoyXEzYK6cDE6eFuuhXz4OfH2nudajBMfP_CR254WlP3eMbbaV6Vl0IV_A-DS_rDL2DTKbLq6FBDdZ5yYY4SJ61AiP4FMQNQ14PwfOgz9idw0hGPJq0v5lGJvX1qmet52wp7CxExegHRN3YHnjRmr-MYSJmcOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
🇮🇷
هوادار پرسپولیس در آستانه دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105280" target="_blank">📅 19:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105279">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei-co9DRurwACPPZLvz5I4JIdJdmp-Aoc2TlSt69tB_YIu45aojRjplEkiVkRT3S8_UcUcCKb1M13EID286qWUhdiNERKlCwpE0Ex65ExDKjgdOPJLe2dbgxr_XY8j8Cvac8C053gMmkfMK6kCWHA2t32heE3tc1pNXB5PkjRIWUgLFs_ZrNh4WC4kB6COi65rBNJ19AcxHJS4zyv2q0mXPWoZNn-OFy0rKOriM0gSDtGwJLyKT8kzAuVUnS9PL58S-jN2Zuy4425gl0THkbjwqUDwyykviVq8drS3mbVKMbFyEyWY6m7twTWgao2-kfTBaaz4CWFfkCJdieRAW61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105279" target="_blank">📅 18:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105278">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cf132574.mp4?token=G3bpoDAPE7nbUJYmWfsqPjvrrZsnGRY0z1jTbelG3AWmPzShmxkDBWkG28FBmhxr6ghjbEc-Iqwm7P0d5u0oH1kfL04BMZwh7A2nlzddeZGLV5qBavmIvuMIzvM9WlpJ8Z-m9lwxcaCw2Y0MmzMmi__qtY9ibR0x3QNJ6XI5djkeGq84dxPIVt0_dVeNcHyeL9p88-FR6asJaByN0dfCiv8dkssPfrbN9mlGxO_rr6kC0W3qAmHYb8fwJ3Nh0QPapOiHLc7RGsBIi9jMkpo3EMlwfxO69yZEcWp7oXfywtD6FgULdBYoWKu9_6eHRtJx89S3UB_V-HX6sYJDCsBo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cf132574.mp4?token=G3bpoDAPE7nbUJYmWfsqPjvrrZsnGRY0z1jTbelG3AWmPzShmxkDBWkG28FBmhxr6ghjbEc-Iqwm7P0d5u0oH1kfL04BMZwh7A2nlzddeZGLV5qBavmIvuMIzvM9WlpJ8Z-m9lwxcaCw2Y0MmzMmi__qtY9ibR0x3QNJ6XI5djkeGq84dxPIVt0_dVeNcHyeL9p88-FR6asJaByN0dfCiv8dkssPfrbN9mlGxO_rr6kC0W3qAmHYb8fwJ3Nh0QPapOiHLc7RGsBIi9jMkpo3EMlwfxO69yZEcWp7oXfywtD6FgULdBYoWKu9_6eHRtJx89S3UB_V-HX6sYJDCsBo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
⚽️
تحلیل‌گر شبکه‌‌ورزش کشور عراق: یحیی‌گل‌محمدی تمرکزی روی تیمش دهوک نداره و معتقدم میخواد به لیگ‌ایران و سپاهان اصفهان بره!
📊
یحیی در چهار بازی ابتدایی فصل لیگ‌عراق موفق به کسب برد نشده و هر ۴ بازی رو مساوی گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105278" target="_blank">📅 18:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105277">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guPZup19PF0Zwh8ryaUIQ9984gYgjsWIorWCFtunM335sUmAR5CbGJ3Hjf7_apsGGIg7xvtVbi-iQjZT7Zcaf_40a6vGxG6MlyvTuxnpv-rHZ911DpiuGmKJo0oO0xXmpj5zk5ss-lMEnQEy4jz_RgNKNB2ywZnc2bXuVdHuBVWcSHjQTHXDzfPK3B3OimO3wFLph6lthuaPOeo3yXgcGo2Ptq9syXl4jQaxOgSh6ZrOTpmI6_JHjIBJCsOR7wNwSs2OkILIzuApvgT65pvTiFDQPfN-R1Orbp9F-YosFLP2gJxuvLRMLTPhU3fqRNw0oH2VMVMC8ugRFp01cmLAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور تبریز مقابل شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105277" target="_blank">📅 18:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105276">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=XHk3_408Imdbun2KdhuF68dShHRoG5bZs7TRBVdwy0AIuBU-Kz9zBxyxHfyr2A9QLrPrQ-IxX6QkpQVsdIfbBS3r-AvMCOLKVv_8_9XcCc3IjudWp9YLfHt-7BM2EBlqYSlKalKreLbkizLtvzI9o6-XI8udRG49rs89SqsA1mW9bqbi3njoQDwkcT00UMssR_wApI7COnRRqI4bTY8NlgILIP8Ss4hom-L6FmZrrL2OXMM9SonvxpQo2skdUw-GfrwjypRrMXuHCK_5ipSMwkfAavuuAOy8cKGSPzS1zaDRV3Kd92P8_ExHb3m7cvIuKEAiTL9Ay1W8_VpvNqxKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=XHk3_408Imdbun2KdhuF68dShHRoG5bZs7TRBVdwy0AIuBU-Kz9zBxyxHfyr2A9QLrPrQ-IxX6QkpQVsdIfbBS3r-AvMCOLKVv_8_9XcCc3IjudWp9YLfHt-7BM2EBlqYSlKalKreLbkizLtvzI9o6-XI8udRG49rs89SqsA1mW9bqbi3njoQDwkcT00UMssR_wApI7COnRRqI4bTY8NlgILIP8Ss4hom-L6FmZrrL2OXMM9SonvxpQo2skdUw-GfrwjypRrMXuHCK_5ipSMwkfAavuuAOy8cKGSPzS1zaDRV3Kd92P8_ExHb3m7cvIuKEAiTL9Ay1W8_VpvNqxKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان‌چالش ترند این‌روزهای فضای‌مجازی
😂
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105276" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105275">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105275" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105274">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRp58W9o8CtofwGTSMvAnhu1boa8YoNKl06f3hWODBw-l6k_96JQY2hAyzSD2U2o3apSaReKTy0vlFk2FcUpBxbn9PAMeSeiYrQFpm512X_GwPp3qnDX5xPfGvpRGApl2TcI3KoYDB-aFYSBy4qu789T6E3wF7jJc8nwKd11vq3tLZBMjDAVMllNkOnpCXJyvswDHgVAeCfWxiOCUTo3xFUCJNQqJlJCvZv96tkNOiJluj_ay7pP8ivI7t50SwHzHJGBFHbMRUIArr8gWNbOr1u00JPuwMOmuHo93v6EV-9E0M7GVVQIHtMiPL12o8c51fiGPZQejOc6k7Wl-wfCtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105274" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105273">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=oaf4q2WeIRRf96mvCabdZKyE5bAcAdh3ydrzIU_RciNxYFp0rBgYlEseGVy4YLVC9jrrTxcOOQnkuT5pKntbYgRhhfp3IqSC4yPfLYg7wyucJQTd_zxR1CPyotvUxPAwZ8h4SCpO726QOcyNw3zJ6eChhmVfGo8CEP39KXO-jF4e76_9effm3KMBXz2o_q9zOJ1furEMQ569vDOUp1-ogSYE8ikntkCxMl7aG4-KcgG8jEECIZhyAWipq7kiYknddEU_VmX49ASNRYBwX_V5KOAH9zWDf546JWtBQdI6M4942H5oFRT_qYYdqDgpxhbfbb8o1npMF3BJPPSMX8Xp9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=oaf4q2WeIRRf96mvCabdZKyE5bAcAdh3ydrzIU_RciNxYFp0rBgYlEseGVy4YLVC9jrrTxcOOQnkuT5pKntbYgRhhfp3IqSC4yPfLYg7wyucJQTd_zxR1CPyotvUxPAwZ8h4SCpO726QOcyNw3zJ6eChhmVfGo8CEP39KXO-jF4e76_9effm3KMBXz2o_q9zOJ1furEMQ569vDOUp1-ogSYE8ikntkCxMl7aG4-KcgG8jEECIZhyAWipq7kiYknddEU_VmX49ASNRYBwX_V5KOAH9zWDf546JWtBQdI6M4942H5oFRT_qYYdqDgpxhbfbb8o1npMF3BJPPSMX8Xp9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پلیس‌فتا در واکنش به صحبت‌های دیشب: به پرونده پیام صادقیان قطعا رسیدگی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105273" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105272">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=QBohqEPMlhZxn3LXsrH7-zfr1OpY6rO_cF0F_qNQwUdRco-m4F0zN3PTvI9ZxtTlq4sRvkdUguCuXvAgZCT3DX96Iq25W9Vyo4igCnDHLXQOHIqdIkFDLAMDnineNCB90jGs-45BjrjZs8dtbF7efmNA4r_jk5lcsqyHw0Fj4Vm2HvzjU0JM02c4A2iBj9ChYbtpq5e1U_46xEYaGEWCuM0MdDjlrp-2vNi554ffdqoB0dbAExfT7kK4UMqR0qM72mJC_fVzo7mE1avNTBbwouVhpbc87hOQlDP5YnsndlXrsVCO2aeT1RWf-uD5niQEDS3twFdXXEVRyrWpNfo-Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=QBohqEPMlhZxn3LXsrH7-zfr1OpY6rO_cF0F_qNQwUdRco-m4F0zN3PTvI9ZxtTlq4sRvkdUguCuXvAgZCT3DX96Iq25W9Vyo4igCnDHLXQOHIqdIkFDLAMDnineNCB90jGs-45BjrjZs8dtbF7efmNA4r_jk5lcsqyHw0Fj4Vm2HvzjU0JM02c4A2iBj9ChYbtpq5e1U_46xEYaGEWCuM0MdDjlrp-2vNi554ffdqoB0dbAExfT7kK4UMqR0qM72mJC_fVzo7mE1avNTBbwouVhpbc87hOQlDP5YnsndlXrsVCO2aeT1RWf-uD5niQEDS3twFdXXEVRyrWpNfo-Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
تیم‌نروژ با قرار گرفتن در رده ۱۲ فیفا، بهترین رتبه سالیان اخیر خودشو کسب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105272" target="_blank">📅 17:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105271">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=hqEeACaU2M2pwoUb51T-UjA0_8rk2Kf08RS10cfTp9m_X6i4ostCTUTQnHB7-p5MeG5aXrgCfsUkesVNbJD_1pOxf8VrP7KDVfUhTkXWPdk0HbLAHTQOeeoubeKO_kkiGiV0Gemrz96TFjuCgDjJ3D7dG3mp-H-Tbaov5xmnOUl2HB3jTRUelfJ4xkQ2u9LEOflEfmBdZg6J3flIXJklBoe8vowx4AcnECL0pT7T8KsxKOPgxBX10mPdrw8UJvB9joJ4ZYzFjXaCkoJaAWkoM4h8YvgLaPE8igvePOd_l53T9cmHV_ZHi2xbD7xZETGc-xDPps_nnf6OST6tul4kXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=hqEeACaU2M2pwoUb51T-UjA0_8rk2Kf08RS10cfTp9m_X6i4ostCTUTQnHB7-p5MeG5aXrgCfsUkesVNbJD_1pOxf8VrP7KDVfUhTkXWPdk0HbLAHTQOeeoubeKO_kkiGiV0Gemrz96TFjuCgDjJ3D7dG3mp-H-Tbaov5xmnOUl2HB3jTRUelfJ4xkQ2u9LEOflEfmBdZg6J3flIXJklBoe8vowx4AcnECL0pT7T8KsxKOPgxBX10mPdrw8UJvB9joJ4ZYzFjXaCkoJaAWkoM4h8YvgLaPE8igvePOd_l53T9cmHV_ZHi2xbD7xZETGc-xDPps_nnf6OST6tul4kXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های هوادار تراکتور پیش از بازی با شمس‌آذر: ممنون از نیازمند و ایری برای گل و پاس‌گل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105271" target="_blank">📅 17:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105270">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOV8ROzXCdoV9w6reBmLFv_BHyE8T51Wd44GN8RPtsf1IwisMSN5JXpy8uocECHPSOihP_QpoJ1d_Tm6c1qjOEbwBgjOKs5voTSOGdlxP_JvJQJQLTidCfB3ogKIMOyZ60qcMbkMJbzJXxQ5GBF_XtqFrU9qY9s4ZetyNh24zSJCXt9LbbamHNh7qWwfRQxv-Dc2vXsVCD91fP378oO4VUEhcjRyIMnp9eiCjraWtoyCAGuPGFgd1oxSfys7niV9f9A6Ru_Xkn4q2Nr3kW4cCoPWioY9dnQGeabohuwfG0J1qUiH6V0ssxGvcOt-TvLr4XuY9QELEgkpLFQkwuCnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تاریخ اولین ال‌کلاسیکو فصل مشخص شد:
‏
📆
• یکشنبه 3 آبان‌ماه
‏
⏰
• ساعت 23:30 به وقت تهران.
‏
⚽️
• ورزشگاه اسپاتیفای نیوکمپ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105270" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105269">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6DTASKio92OEZ6Txd4w6o_7Gtxjg3rgVwvnkog01f36F1LBktBn84BuTrcy9Ruxm5U5V9EeIJS3BKyCCPUHuqQXIiViE_KfAt7RHtQJsTRPlB_eocUE7dR7368Xi5t5WNsGERdUqy0az5U6SbeNI2J6SMhGgTKF5Z828jf66XgqYNiDiZ4t2keKF6cK3Zwumc0E8kQyBe2ursF71IzFuqaY03CDZHozO5X1re_J6NFCzGL-MU0v1cWRAIjr_pHxi8-EZRNM4dP6evNreBeHWNyNhcPsB3S_AG8woRNE5PP78oZDlgWhIVQn3dHZRX1Bzr5swG2DPw0EU2Dsk1v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
🇪🇸
مقایسه عملکرد هانسی‌فلیک و مورینیو در تاریخ الکلاسیکو فوتبال اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105269" target="_blank">📅 16:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105268">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHZlpwwXx7EXlnRmN92erbuxTgExf4gr-CjOoLBhQKr3VS82EVGNa9N8YWQKvlYIxLZOFchZkx_FFIM8nuXAKokj45gqju5gt1r_2_k3YQ0xcmHgH2VHbuYI3VWR9Gbuvvh-jlShfGE8pLxc7Ac7yGcizdo_uwsfzz12wFNK_j0PokSoujlHdli9Gk50znXV9sWXV7yqQIdep3eI4xYd3cb8_eKhaBcjzYjnyvounaBd_sjYsrlAhm055dv1x-0O3ZjqaRpmxi6e4uUBwMN20EtT4_V-B1xGNIFnnPDAQAJUFvdeMtgAaSiwr5auDMy5sUyw1vttgAOpgKRR5JuOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
💥
در آخرین ماه از تابستون یه نگاهی بندازیم به بهترین فیلم‌ها از سال 2000 تا به الان که اگر فرصت دارید در این اوضاع شخمی مملکت نگاه کنید. سیو کنید بدردتون میخوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105268" target="_blank">📅 16:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105267">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=n1eKTd0KqE47ZGFHhKm-trM7N0j8BqPJNqdR6qnmBs8hcppojdGO8wDgAjtmN_lm7RHOqZ0ZA5Gi0cyg2uyVtUalpBvMgccRwAyWbhrBYjknIokYqpMd0ECsbzMAcKhpXLN0S1YPJehxKRSGEm8vfOZ9DsvYdIeyNTZmERQr7oRZ8eiaaGYhwWvWJidVDO8ikqdJP5eivLOQ4JgQp_bxKD2S-xVSgTmNExVQ6Vn5vj8GgGtT2XvNGBRuy0Utd-gK8pWkEyPtJrjobA2vtkwl0AkTlfPTCjCPlDYmeXPCHKOpShP12AeT40z2Fq8ANhNQOxJ38PaWjYiH1JJ4lRK6cRtdDNkCiaHP2UcPdnRLCv5rNBq9VKNuawFsLwndXD7-ZRy9d97nsRALwxpUrqmn6eYbCrbrp-D3w87caqJ22xOnlziMxSRqSklGkoeYDXXa2kRlzJH6wbsJtiZqEmHxwWTMPmn7ltLQANSQv_OZAG1NPLMHn0f1nPON83IGEG7rNkDSiYNvTXC5N_j1Z6opiZGYpz6NzNWoQAE_rspnxpQp0gxMOc7uinK6U_dMWfHkpURBsLGws8_vC2tcrH_xY-heqEAk-Q1TaTlKBxtoljyUmviZmCxWPz2E5bbXrjnhV7PDinBEDUP8_eglli7DVZYz0sLyjW1ly4SJ9EhlXb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=n1eKTd0KqE47ZGFHhKm-trM7N0j8BqPJNqdR6qnmBs8hcppojdGO8wDgAjtmN_lm7RHOqZ0ZA5Gi0cyg2uyVtUalpBvMgccRwAyWbhrBYjknIokYqpMd0ECsbzMAcKhpXLN0S1YPJehxKRSGEm8vfOZ9DsvYdIeyNTZmERQr7oRZ8eiaaGYhwWvWJidVDO8ikqdJP5eivLOQ4JgQp_bxKD2S-xVSgTmNExVQ6Vn5vj8GgGtT2XvNGBRuy0Utd-gK8pWkEyPtJrjobA2vtkwl0AkTlfPTCjCPlDYmeXPCHKOpShP12AeT40z2Fq8ANhNQOxJ38PaWjYiH1JJ4lRK6cRtdDNkCiaHP2UcPdnRLCv5rNBq9VKNuawFsLwndXD7-ZRy9d97nsRALwxpUrqmn6eYbCrbrp-D3w87caqJ22xOnlziMxSRqSklGkoeYDXXa2kRlzJH6wbsJtiZqEmHxwWTMPmn7ltLQANSQv_OZAG1NPLMHn0f1nPON83IGEG7rNkDSiYNvTXC5N_j1Z6opiZGYpz6NzNWoQAE_rspnxpQp0gxMOc7uinK6U_dMWfHkpURBsLGws8_vC2tcrH_xY-heqEAk-Q1TaTlKBxtoljyUmviZmCxWPz2E5bbXrjnhV7PDinBEDUP8_eglli7DVZYz0sLyjW1ly4SJ9EhlXb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ربات وزنه‌بردار چینی وسط مسابقات جهانی وزنه‌ خودشو رو میز داور ول داد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105267" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105266">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=fBS8SMeBWcDCE6THSpMUeBpJkDRqlTkiKoOvBKyTY0cQ-kTy490n6mpHk8vBSCj1kGXRQMwD6PCTFB8gUJM32IyWttMh5H18XiwOJurydO3DzjvUsR83hRmpcf3LvsNxd-LkR_TlIj-51TV5y1czHKDhKSGBLIbI6hAqHa0x2ANw5rP4JCl-5vQSbDVoiBt_K3cPoWaOm4FXJeWVmSqmwcwDW2zWs2iCYAQ1oGybBvQvJih_V-9ggxtpgotQHWh63MTJJjJx3XKd08w7I2tx30LBPzYysFv8zLHkFGfDFt4oFrUwoWTxgdGrv2vQEhsS5MLK4ZnUguAcK7pt98EG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=fBS8SMeBWcDCE6THSpMUeBpJkDRqlTkiKoOvBKyTY0cQ-kTy490n6mpHk8vBSCj1kGXRQMwD6PCTFB8gUJM32IyWttMh5H18XiwOJurydO3DzjvUsR83hRmpcf3LvsNxd-LkR_TlIj-51TV5y1czHKDhKSGBLIbI6hAqHa0x2ANw5rP4JCl-5vQSbDVoiBt_K3cPoWaOm4FXJeWVmSqmwcwDW2zWs2iCYAQ1oGybBvQvJih_V-9ggxtpgotQHWh63MTJJjJx3XKd08w7I2tx30LBPzYysFv8zLHkFGfDFt4oFrUwoWTxgdGrv2vQEhsS5MLK4ZnUguAcK7pt98EG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
پیتر کراوچ در سال ۲۰۰۵ فکر می‌کرد بالاخره مخ یک دختر اسپانیایی زیبا در هتل را زده؛ اما جیمی کاراگر خیلی زود فهمید این «دختر اسپانیایی» کیست!
🗣️
کاراگر همه‌چیز را جلوی هم‌تیمی‌ها تعریف کرد و کراوچ تازه فهمید دختری که به او علاقه‌مند شده، همسر ژابی آلونسو بوده!
🙂
کراوچ سال‌ها بعد در پادکست گری نویل این ماجرا را تأیید کرد: «فکر می‌کردم به خاطر جذابیتم از من خوشش اومده!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105266" target="_blank">📅 15:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105264">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=Zt8xZbLC6TrlgdYgBKIIwYG5ZERQl3BbU0OMlYuNeLmzua-H26z1Jz17eb3x2431vxuruIjLMD4DbN1GSvWJ-KfcCVRqD0a_UTbOHJ6TK20YVzO17HU9nwbNFLLauqamhKGJ71GMWEWwvdq7V58o-y3WfgT73tY5C6BnOIhY7rLefYGWds8nP4ilKKMZlYOcs1MRQNV0cDPWkE-9K4VtN1dQ7ebx5LDAvnTyvG9FTTmWMVhbjGeFI4pT-PSQc6YSy3-ZEZsEDdEwYgqOTnL5yhSPX_s7UMxHbf7M-rsfLipoJMFS86aUMs1cOeIOzQCjB7T0WRgVIfjdF90mUunfRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=Zt8xZbLC6TrlgdYgBKIIwYG5ZERQl3BbU0OMlYuNeLmzua-H26z1Jz17eb3x2431vxuruIjLMD4DbN1GSvWJ-KfcCVRqD0a_UTbOHJ6TK20YVzO17HU9nwbNFLLauqamhKGJ71GMWEWwvdq7V58o-y3WfgT73tY5C6BnOIhY7rLefYGWds8nP4ilKKMZlYOcs1MRQNV0cDPWkE-9K4VtN1dQ7ebx5LDAvnTyvG9FTTmWMVhbjGeFI4pT-PSQc6YSy3-ZEZsEDdEwYgqOTnL5yhSPX_s7UMxHbf7M-rsfLipoJMFS86aUMs1cOeIOzQCjB7T0WRgVIfjdF90mUunfRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
⚠️
واکنش عادل‌فردوسی‌پور به حرکات منشوری شجاع خلیل‌زاده و عارف حاجی‌عیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105264" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=cFo54OXtBSx4xZuVo_XzfJEBdcWQiYTmGc4UycDhwPVxoX2F_gAZV1DkuQNmxoTSmzXF2j6KXN_tNin4XJ1yCMuo9pzDjmk2X55ux_tZjTqzg6SxfXA_2S78jktF7YrT91WW-e4pDRv-EyFodx21TeJlO4YbdRF40iZm0ly4Ndf7dc6TW9univBgLRP5lQsxj4UDM_K_7YLg1T-cMkKNd-SfZ0x7SBWeoRBkUjj69OTeFbXadx7YswhvFPk_yHhGz_IbLLUYc0aHbN0VT0IGCpT4hqfr8lXJJz3ZN7YPjlpOkiBkRGpqJWxvEfJ__RrxGrWrCHC-zNT10QPBbEdrlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=cFo54OXtBSx4xZuVo_XzfJEBdcWQiYTmGc4UycDhwPVxoX2F_gAZV1DkuQNmxoTSmzXF2j6KXN_tNin4XJ1yCMuo9pzDjmk2X55ux_tZjTqzg6SxfXA_2S78jktF7YrT91WW-e4pDRv-EyFodx21TeJlO4YbdRF40iZm0ly4Ndf7dc6TW9univBgLRP5lQsxj4UDM_K_7YLg1T-cMkKNd-SfZ0x7SBWeoRBkUjj69OTeFbXadx7YswhvFPk_yHhGz_IbLLUYc0aHbN0VT0IGCpT4hqfr8lXJJz3ZN7YPjlpOkiBkRGpqJWxvEfJ__RrxGrWrCHC-zNT10QPBbEdrlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دخترای جنوبِ ایران
🫶🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105263" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7EF8RGYBG539V4ZDMhcofGPxUeRoKK0A3cEXqctF989f-xxt2XXNqusb69o_HYLUjkXQIIt7t2cd5_GNvjbFYXYNjG5vbfUTuOy1rjf-B_4vZSOswH9GnZejMfnrDGdVJigOv-MbzRsHP4B7nEXTnvgmOMFOExkha9Obb2dzvMkA8b901py-cwIOlW2qtXykEbw6YinTcFmzGpqW0Brf-NhjPmpAN2WtEWPZ4TfAyy55meCizxgDv4xyC5jyPrngV9RPWjEAQQ2J7WK7ubrRmypbEvIjU8EH-TnPYGOGbmSiQGO-cTSuZUO-74NdcCtvzASayJbdf2bKEAGL8MfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
هوادار بانوی تیم‌فوتبال تراکتور تبریز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105262" target="_blank">📅 14:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93b254714.mp4?token=qlRrRulvqfLTwHw6xorT4XFvQDlYrco4SO_jCjBL7fsyrZAYzT2YRfvhSDKrYLZyCEXc9J5h8pnESAYcQvWToOtDjtxkxalruV7-8_qOjJ7-W7g9LvF30VYHITNLLcm-ESqc6qWaEhgU1vZB9jjz8ZEAXGwYPDhQmrKNhh7Mm3OOqQzdvTX9rHp0-cCtsxAjWh17C-chJSfrU_OX7uR3PfSizDhjzQt59GItqjmNYwiUfE7UrVhws1FmQsSOfIictZzBR276reMeSlqPpOP1IfUnscdgNoNXj1Tbe_fQDB5S8nJBiriTRcAWL7l8RxSszGNifGqI1qydHuvGCGuTNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93b254714.mp4?token=qlRrRulvqfLTwHw6xorT4XFvQDlYrco4SO_jCjBL7fsyrZAYzT2YRfvhSDKrYLZyCEXc9J5h8pnESAYcQvWToOtDjtxkxalruV7-8_qOjJ7-W7g9LvF30VYHITNLLcm-ESqc6qWaEhgU1vZB9jjz8ZEAXGwYPDhQmrKNhh7Mm3OOqQzdvTX9rHp0-cCtsxAjWh17C-chJSfrU_OX7uR3PfSizDhjzQt59GItqjmNYwiUfE7UrVhws1FmQsSOfIictZzBR276reMeSlqPpOP1IfUnscdgNoNXj1Tbe_fQDB5S8nJBiriTRcAWL7l8RxSszGNifGqI1qydHuvGCGuTNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
بدون‌شرح‌ترین‌ویدیو امروز...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105261" target="_blank">📅 14:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=NQFFdVXcQqZDeeYUYKS0Pel4fZUuL2pUpynQ9ERhY0GgHciQNMxAz0clePKCOKFdYXnJ7Cg_vuSRJFFJQLNHw_ru3sC7JWPqkPxv1cxx1ZVIVIXQoD1Tkp0tZp1oYQ3XNpqddztMl57-KmpA12bXXGNKmoJ6GOiu_mEqy45W8LS5BZ6JE3wcRkzMxitHSe6SKcYDYm_G4o6DphNWuJQD-IYF-YHCZnyBNyQMhTC8uTbPW8nVxlCr9Piiq-EllexwERqyYJ1mEz-4gMEILDmZV-V5Jj38H5z4Jq10z0CHyEn16C2Y8zj8f41SjOlB8Do7LXhp4gyOh68Rr0yY95_cvbgJt0VSH9ZQTjhE41ZDkM7YkDYTefjOYB0C33EuJCPcPHqyeGsSV7l4hgodVIbUKJWO442RaCJO7cSiFWp-tBOJ5eg0_CzqBjzK1wAek1recfMuiJz2uvcSmtIXXX5EFQwRx972wbq5LELNL0_I69Yt4ZJ45vRoN7Xi7ru-pG0yMjFYSzBIWoyRe414C-dWodqgSzd71S3REboZfyrkh2XK6FBcLkReykQ3MEj-53c9Z_kg3AZs9gEtIJ7mY_w0rlgTptlvwPynccbx5bOH7wvJb49WhRvcFB1lSrt43AXx8q29-ZJNVJhka4kfW6zlK6QiWI10qW44CEHncYUj_v8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=NQFFdVXcQqZDeeYUYKS0Pel4fZUuL2pUpynQ9ERhY0GgHciQNMxAz0clePKCOKFdYXnJ7Cg_vuSRJFFJQLNHw_ru3sC7JWPqkPxv1cxx1ZVIVIXQoD1Tkp0tZp1oYQ3XNpqddztMl57-KmpA12bXXGNKmoJ6GOiu_mEqy45W8LS5BZ6JE3wcRkzMxitHSe6SKcYDYm_G4o6DphNWuJQD-IYF-YHCZnyBNyQMhTC8uTbPW8nVxlCr9Piiq-EllexwERqyYJ1mEz-4gMEILDmZV-V5Jj38H5z4Jq10z0CHyEn16C2Y8zj8f41SjOlB8Do7LXhp4gyOh68Rr0yY95_cvbgJt0VSH9ZQTjhE41ZDkM7YkDYTefjOYB0C33EuJCPcPHqyeGsSV7l4hgodVIbUKJWO442RaCJO7cSiFWp-tBOJ5eg0_CzqBjzK1wAek1recfMuiJz2uvcSmtIXXX5EFQwRx972wbq5LELNL0_I69Yt4ZJ45vRoN7Xi7ru-pG0yMjFYSzBIWoyRe414C-dWodqgSzd71S3REboZfyrkh2XK6FBcLkReykQ3MEj-53c9Z_kg3AZs9gEtIJ7mY_w0rlgTptlvwPynccbx5bOH7wvJb49WhRvcFB1lSrt43AXx8q29-ZJNVJhka4kfW6zlK6QiWI10qW44CEHncYUj_v8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
دیشب‌کریم‌آدیمی بنده‌خدا فکر کرد چون ۱۰ دقیقه تو زمین بازی کرده دیگه بعد بازی نباید تمرین کنه که دستیار فلیک این‌شکلی کاسه‌کوزشو میشکنه و دور تا دور نیوکمپ کنار نفرات ذخیره تمرینش میده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105260" target="_blank">📅 14:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=lTzcNW0RLaL7KGyy31c0cQ-YskdQ14X4Nu-GG7lMtvYJdHvN-6OV0aTpf6CyD0FlruH0S7atxdfQ9pto1gzzGKNI-DHPokvhVvcWT8QvMxuCFyK8oNjg7j-hfTNR89WNlf2-vQ1QzlsYVfnIp7x33z-YaEZ9V3cIWD62kgOXP-96-W3YnV0-WDMBBO9xbArwNz155yG5lVlfIVFeodgFF1Yaqeo_xI8THNesjqNVLlH0es-kjgy8P0YOhRaDMIq_InmmXxDgHzp-60cnwNyMPHV_y6dTZgDulGHcKoWRuT55MIRQZDCsTVImJx0-7ENW6T_Npji8YQK0UPlH5O31SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=lTzcNW0RLaL7KGyy31c0cQ-YskdQ14X4Nu-GG7lMtvYJdHvN-6OV0aTpf6CyD0FlruH0S7atxdfQ9pto1gzzGKNI-DHPokvhVvcWT8QvMxuCFyK8oNjg7j-hfTNR89WNlf2-vQ1QzlsYVfnIp7x33z-YaEZ9V3cIWD62kgOXP-96-W3YnV0-WDMBBO9xbArwNz155yG5lVlfIVFeodgFF1Yaqeo_xI8THNesjqNVLlH0es-kjgy8P0YOhRaDMIq_InmmXxDgHzp-60cnwNyMPHV_y6dTZgDulGHcKoWRuT55MIRQZDCsTVImJx0-7ENW6T_Npji8YQK0UPlH5O31SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
عملکرد پشم‌ریزون دیشب لامین‌یامال برای بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105259" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=BcyMTYFotNJc5B8KInKakHPahpEZv7azpNKip1JCI4m5c92mF4NC0yJ_SxJ3-KYNYU_XcWPWLkBoXTKrKEyNgbkl7D14IblYTG7zVEr-gLNxj5euBVEXEisZOnOJt67jnSIFVpy7NkSQTqYum_dWjVdjs0f5U0l0kfiquttE8A0L_oLpLbktWUlB3Y6vzBz7NrmCiByfP8cmslD_M0MCx0vjEIioLiumDDVoLXR1FvpQO1iP5MT2NDgBuW8Yd5Zxk4ut5ygz92fV8rn0atbCooOEjV0Aq4ieVMKsUcfVLK67cF8_ZZaS5TvgMAX5pPPbCunhC-lxcnCRMlAflVczIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=BcyMTYFotNJc5B8KInKakHPahpEZv7azpNKip1JCI4m5c92mF4NC0yJ_SxJ3-KYNYU_XcWPWLkBoXTKrKEyNgbkl7D14IblYTG7zVEr-gLNxj5euBVEXEisZOnOJt67jnSIFVpy7NkSQTqYum_dWjVdjs0f5U0l0kfiquttE8A0L_oLpLbktWUlB3Y6vzBz7NrmCiByfP8cmslD_M0MCx0vjEIioLiumDDVoLXR1FvpQO1iP5MT2NDgBuW8Yd5Zxk4ut5ygz92fV8rn0atbCooOEjV0Aq4ieVMKsUcfVLK67cF8_ZZaS5TvgMAX5pPPbCunhC-lxcnCRMlAflVczIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
محسن نامجو مرتیکه دلقک در کنسرت نیویورک، شانزده شهریور سال ۱۳۹۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105258" target="_blank">📅 12:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105257" target="_blank">📅 12:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=Ud7fBZuPkbwvfiqQ3Cfw4XbHiV4icC9GsKua8_lH1CY8M_BjcSqQP7in2JFdhwaRQYmukYHmYnBm-U0mDT0rE7hrSKIl9lO0NZyZ1b_xNVIvlnEbjTdnMjHGu6eABTW0NjN18Xw6EJj4ppOL7vrTCR5yyz356l8UY5ra4VGv2_R0Z9TLlrr1ZPHD9pJSK5HjzanbHraUTqBLc-ZYZ-VE215lkAnzMHNbgYYnVHDqge49b_P_6NVG-rUymWgazIxTTYcMDZSNtTWFUwgKog_3L2wEP7MfmUwBnHESPrCt9ZA4iswcFXUyybb2fWLbxhmuVYpfqGqJTpFNq3v6AJm1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=Ud7fBZuPkbwvfiqQ3Cfw4XbHiV4icC9GsKua8_lH1CY8M_BjcSqQP7in2JFdhwaRQYmukYHmYnBm-U0mDT0rE7hrSKIl9lO0NZyZ1b_xNVIvlnEbjTdnMjHGu6eABTW0NjN18Xw6EJj4ppOL7vrTCR5yyz356l8UY5ra4VGv2_R0Z9TLlrr1ZPHD9pJSK5HjzanbHraUTqBLc-ZYZ-VE215lkAnzMHNbgYYnVHDqge49b_P_6NVG-rUymWgazIxTTYcMDZSNtTWFUwgKog_3L2wEP7MfmUwBnHESPrCt9ZA4iswcFXUyybb2fWLbxhmuVYpfqGqJTpFNq3v6AJm1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مجتبی‌پوربخش: تا جایی که اطلاع دارم، وضعیت جسمی علی‌کریمی خوب است، فشاری بر او وجود ندارد و صفحه شخصی‌اش نیز در اختیار خودش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105256" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO5lvoocKsaOWTMW4BlPVzaQp--lfW3AUEAsz4zrT_jkXyPtQl--Uv-EKAqMCJtVl7ONivow1ppLo8XOoAHOmtkIyUKdfcbnspWeMqDgm761Riuz_bc4_IGvI00VkBbw5pOwiYqc_JaVbYiGUSm90fNa3mDBGs6bTQyjXnYFQCeEPmc1I7D27gH3ecR-ftlGMx9fQVETtZw0E_UFInirGATuTaCLOlWOvAQvYQVJ6RaNMagmrx1VxYTTbvneLXVbj0kvv-8emQi4JobQ56lkY1GQGEzdtPf-0JFaNgdFaXm6OKj2Mf5XRuaZdXFTt8OVnn8tvBBVnCsu0RC4AfB1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
نتایج سه‌بازی ابتدایی بارسا و رئال در لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105255" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=QLhNuwLz0A1woN9A5zGDjm8jG7o8GbQAUYz0yyZVBdEemi6GKZlurhYpQEUe4lxbXF5iH9NNpxJVPXW81zQVp-1LZqvhoeo584vA8Pu9sgacBo9JxvomPOJaGXSHfFW5STbT6AS03dIrzSzSOp7hEEgZVYgxZtJGoMOS8r-wU8NRti6SlfLIxtAeCkYLPo0UGQfJRpJIxVOcjpVYsI-GX93xgTC28mgBw_CbO0BTozfVOifQRpGvvgHqNs5tmygvpVESReuRbN5Ta-msILi3NcSVFvcd4NBAdV-3gO3194mqfX0hSL6GNo2vqGoxqCpIJUg2AqE6fodCMipxzCy-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=QLhNuwLz0A1woN9A5zGDjm8jG7o8GbQAUYz0yyZVBdEemi6GKZlurhYpQEUe4lxbXF5iH9NNpxJVPXW81zQVp-1LZqvhoeo584vA8Pu9sgacBo9JxvomPOJaGXSHfFW5STbT6AS03dIrzSzSOp7hEEgZVYgxZtJGoMOS8r-wU8NRti6SlfLIxtAeCkYLPo0UGQfJRpJIxVOcjpVYsI-GX93xgTC28mgBw_CbO0BTozfVOifQRpGvvgHqNs5tmygvpVESReuRbN5Ta-msILi3NcSVFvcd4NBAdV-3gO3194mqfX0hSL6GNo2vqGoxqCpIJUg2AqE6fodCMipxzCy-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
ویدیو زیبای و دیدنی حمید سحری پس از اعلام خبر خداحافظی اسطوره لیونل‌مسی از تیم‌ آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105254" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105253" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105253" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZoNFvq5wXE-R_RkDW0PRqu8N7mxN8Kpcz9j1FEPl89HLH9HoMhXOPfbWCCJ0RoaJQPKlxP00jV74FW0187iaa8IjYg0rL59ngJcDcurrkQAEYe3EtgY2m6kBHh8K6ftWHzhj43-cKIWXsXcdqxN92eNFaLjxrdqRmkkdsS5QTZ67yfuQ2DHJWWY65NbzxmQd7zY5-kPfInBJcHHz9QUaKcQEVWVw2JjEhzVPFJSuFz2L23ol14bkORlSVioxigVkJsG5IEBdTJVYP5vu3xR1xaFMN7HJgN_bNSrTgRslYnoA6IYYFJH-af9Vq23mmwS8MkAO9U5KrhGPtmrUseZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105252" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=HNy59gccwZha4SUfqA5ssQWnp8Z24rDPHCdwW9Ze6oyMyw_U7TZu7ij2BKaXstb3PRFYmxLD_lzWp8gKo0qkp00-8ORCPa2ux9SC9GhA0GRIBR-M-jSl5jboF27tMVtsawqJXq370CMQ8ACRFK19M_CihqXREfiVa37Jap-zJkltzyCaJ8QiCLMZcjIts2fMyG7WdF64KoSST_pTsyVOdTof9jwGvrdu-5mjaSfM0cXOIAnzy1ktx9ot6FRdC4HSTVt2hyZa8ocgfwqSklzolrGjppukHdUq-F1nQjUe_XvG7QDxLVQ66VJ3TKJmbjOfUXIqYOfPjPHAfl1G9wIRJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=HNy59gccwZha4SUfqA5ssQWnp8Z24rDPHCdwW9Ze6oyMyw_U7TZu7ij2BKaXstb3PRFYmxLD_lzWp8gKo0qkp00-8ORCPa2ux9SC9GhA0GRIBR-M-jSl5jboF27tMVtsawqJXq370CMQ8ACRFK19M_CihqXREfiVa37Jap-zJkltzyCaJ8QiCLMZcjIts2fMyG7WdF64KoSST_pTsyVOdTof9jwGvrdu-5mjaSfM0cXOIAnzy1ktx9ot6FRdC4HSTVt2hyZa8ocgfwqSklzolrGjppukHdUq-F1nQjUe_XvG7QDxLVQ66VJ3TKJmbjOfUXIqYOfPjPHAfl1G9wIRJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
🇮🇷
فرشید باقری: خداروشکر به پرسپولیس نرفتم؛ آبم با آنها تو یک جوی نمی‌رود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105251" target="_blank">📅 11:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105250">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=CqzXUg2dkZxyU0VUI5ojIzngJeZFoFCxcJ_ggOSuDs6B9cTpuQoNoLrcYTOWPFMaG-00RJJJlR2V8oTIZl89xCgac0hA_qjStAGP5grJM8E8lF1UXAu63bbih7qgtZCwqi5zdaxwZkrpxLbILwfAec7DAqEM4JZ1Jpv43OX1snk617eNI56bAAYWuyiEBUI3uef8bAdKGZA4ofnJvkWwcwHleqJboJVVsQtWe7c9h-D1XDjxdTeGatid6ECGRRtVUv3gSLsDS0VdKT4IxfoLtOhuTerNzo54nX21PUl9VGz-nXa1vxUFNbSqLpsJIgi1-xzxRwkoyPsM02xW5JJ4Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=CqzXUg2dkZxyU0VUI5ojIzngJeZFoFCxcJ_ggOSuDs6B9cTpuQoNoLrcYTOWPFMaG-00RJJJlR2V8oTIZl89xCgac0hA_qjStAGP5grJM8E8lF1UXAu63bbih7qgtZCwqi5zdaxwZkrpxLbILwfAec7DAqEM4JZ1Jpv43OX1snk617eNI56bAAYWuyiEBUI3uef8bAdKGZA4ofnJvkWwcwHleqJboJVVsQtWe7c9h-D1XDjxdTeGatid6ECGRRtVUv3gSLsDS0VdKT4IxfoLtOhuTerNzo54nX21PUl9VGz-nXa1vxUFNbSqLpsJIgi1-xzxRwkoyPsM02xW5JJ4Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وضعیت سخت‌افزاری ورزشگاه اولدترافورد که وسط بازی از سقف ورزشگاه آب میچکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105250" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKGhcVvjtmtbYVLtKKRFoI9G1lTfudXIO8H1ZSrcpg1H-qsaJwUKcjHbhLdTK-17eOSdmmaO8-i0P5dX45jF0d4oO3tokX9uYpxN7qF7qIApUyrTlTF-f7yRSe1NZkMGdmYgXJdPevVVXENXOEotOOEzAiDPne80odr7rPIngFK5bTi502UR5X7ro7EYyBqFMXIrZhhd4Mh6e369ohPCIvJ5UndaADLPyw3H2vcfFvFykgjYp5pHo5E1BwXzP7vuw5kHvrvqo1VBxnOa-JYpMGB0efKy6nksjei-s2TVPj6X9MNFE5UbsL_HXyHCJpkIz5lJsdgdqw_76e1ujitWYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105249" target="_blank">📅 10:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105248">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=sw6shZIHXImlcF3ud4Ku_dKgUYQwk1P66TjHRSjkBsjq8PY8JF7RGwt2VtCBU-XjYNHktzT87RmuL0lu5cgA1HGHTikBntSJap_0HXbmA71bk98b3jZeZ8qMi3tF2CFnJt7R8CxQPDNJzvsj572x9GpI0nrnwsAvzO-qJloZb22Uw_iid674cymsQTtEm9x-e1YItHroKMC3oRttDo-WeB2b5LTNuo0mBoDy6aok7kXpKlN-AQ4_CwyH65w1vrw_IRW2BV_qnp_gq7JsZdutYSlvpy7DHmEDstmkeHX1XgPdybrFXH-u24iHuGeBVs194vGarl3O3GS3O4SJdYk54Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=sw6shZIHXImlcF3ud4Ku_dKgUYQwk1P66TjHRSjkBsjq8PY8JF7RGwt2VtCBU-XjYNHktzT87RmuL0lu5cgA1HGHTikBntSJap_0HXbmA71bk98b3jZeZ8qMi3tF2CFnJt7R8CxQPDNJzvsj572x9GpI0nrnwsAvzO-qJloZb22Uw_iid674cymsQTtEm9x-e1YItHroKMC3oRttDo-WeB2b5LTNuo0mBoDy6aok7kXpKlN-AQ4_CwyH65w1vrw_IRW2BV_qnp_gq7JsZdutYSlvpy7DHmEDstmkeHX1XgPdybrFXH-u24iHuGeBVs194vGarl3O3GS3O4SJdYk54Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری شب‌گذشته داشعلی‌منصوریان از فساد شدید در ساختار فوتبال عراق
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105248" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105247">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if5O_kI19ijKQHKXPUm7tOp8pKjL99APKc0iDoNpPZE9lQN1D9Y3BKjp5fYevBapr1VzxLb03rSHYQT-w5lwf48mUjk4uwuaV5vyrPgDXG6BiN6KI3gpEYzc-Mgd2uxFsZeN6vea5amd5acA0PeZ29tEX_LFfKvuWHUvSvSkxBH10fqvvzCgqTgplrlzpGAQBjPxI5e_QdHwvUykkjcYoAHxiA0neSeCkDTkrz-ZDk4CaXkYqIHcttd69SW_WHg5KoazZqlq-rHpHgqckMsxgPVEhvHSDiiTOrDnkRKxA-X-ko76VA-euauMnyqv4hBTg7gH_VTS3sZtOxm5JMsaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
با حکم کمیته انضباطی، شکایت دو تیم سپاهان و مس‌شهربابک از استقلال بابت بازی غیرقانونی یاسر‌آسانی مردود شد و این بازیکن مشکلی برای همراهی استقلال ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105247" target="_blank">📅 10:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105246">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=oBLaRAGYtY93ZIFgFmJOj9yA7HVlP1LADdIF3XC3Ts8ogjd-BcPjkrwzrwyRl_o7CXEu0hDgbwVzkvmZ-naQ9rtpEzQZZeqpcSaYtt5Q65iFNFXZrX3GUNogfCU2VIjNmsa5t3gp3Cvahdqm5YI9FZwCP2BuCIOdkYxfctIP7ypUlEcJDyCVvYHRvext0AxS6Pz3TZqrrNtnlTTd3BOCatmJZO8F3yNJWw_MlUB6nPYP5fb96jkIRcVxv3b2Wcjvyd8a5CMf__UMLHHn-oOJqGTKqyb3qB6M4-mXEu76gLxdxOFkajBpVtV_fVTfQiftZYo5f8ZM_YMzJCxIVdvObQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=oBLaRAGYtY93ZIFgFmJOj9yA7HVlP1LADdIF3XC3Ts8ogjd-BcPjkrwzrwyRl_o7CXEu0hDgbwVzkvmZ-naQ9rtpEzQZZeqpcSaYtt5Q65iFNFXZrX3GUNogfCU2VIjNmsa5t3gp3Cvahdqm5YI9FZwCP2BuCIOdkYxfctIP7ypUlEcJDyCVvYHRvext0AxS6Pz3TZqrrNtnlTTd3BOCatmJZO8F3yNJWw_MlUB6nPYP5fb96jkIRcVxv3b2Wcjvyd8a5CMf__UMLHHn-oOJqGTKqyb3qB6M4-mXEu76gLxdxOFkajBpVtV_fVTfQiftZYo5f8ZM_YMzJCxIVdvObQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
‼️
عمو رشید دهن سرویس درکی از دیدن برنامه با خانواده نداره
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105246" target="_blank">📅 09:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105245">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=Tz2TKShco5ZZSmOQRIl_RCaMvPUyf6Am00JZxvT3uFdgLWCL4xXA6yu7PsVoBq4XWz4JU0GetKdNZ0yZoZuliDtrl2RKVuewAANP_V1bOOIDwqNBQ6Vdg5xYdyTpHiu0Rj-_qu8clax1aBNa7F-5auDnEhgJGkQTJPvOGkv6Lflu2a1IPPWwyZz7HpkmP3gZseMsJ8H-Ib08Fc9-IPcK8mSP6-g5-xM1CznPCdg-vYfS36OMdNpLE1swiJK7-k1BPW8YRKeuXrd7rgJJOTTBkPiMKMCtY1ndp-OIF0mFJd_Z10BtWKpl7pZq7STJ56GkXROz5mp_T9iDnCoBC5dsCQoJrDXaM1Y0Gjl1n80n9vOd-Dze_yG1eByrCD81VsLfkYKT8Y0TAhGmkEv1TTUKs69np8VuZ62FWoFgQ6HN_zVSfF-LSLRNank2VuE4t1QCQ0JC6JflshYz2si6FYYzzEuIfMo8_h7ADbAphb71lZjx6_WAYyUolueF8cZIX4t1kOuyTs6cTdFNuv3CEhpiV_PJ5D9rntn3asJU5kx69jZe52WVaIKHoGdQl2u7BlBeXGtYKwpFtyoac-EALTFqYIAg5hJFFP7pBdGBKuF3IMSYggGbHIGpdrSEKU5CWj6isMzpVaBS73HJxQKIjFShsYm71jCBWnq1rXz-Ri8TSfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=Tz2TKShco5ZZSmOQRIl_RCaMvPUyf6Am00JZxvT3uFdgLWCL4xXA6yu7PsVoBq4XWz4JU0GetKdNZ0yZoZuliDtrl2RKVuewAANP_V1bOOIDwqNBQ6Vdg5xYdyTpHiu0Rj-_qu8clax1aBNa7F-5auDnEhgJGkQTJPvOGkv6Lflu2a1IPPWwyZz7HpkmP3gZseMsJ8H-Ib08Fc9-IPcK8mSP6-g5-xM1CznPCdg-vYfS36OMdNpLE1swiJK7-k1BPW8YRKeuXrd7rgJJOTTBkPiMKMCtY1ndp-OIF0mFJd_Z10BtWKpl7pZq7STJ56GkXROz5mp_T9iDnCoBC5dsCQoJrDXaM1Y0Gjl1n80n9vOd-Dze_yG1eByrCD81VsLfkYKT8Y0TAhGmkEv1TTUKs69np8VuZ62FWoFgQ6HN_zVSfF-LSLRNank2VuE4t1QCQ0JC6JflshYz2si6FYYzzEuIfMo8_h7ADbAphb71lZjx6_WAYyUolueF8cZIX4t1kOuyTs6cTdFNuv3CEhpiV_PJ5D9rntn3asJU5kx69jZe52WVaIKHoGdQl2u7BlBeXGtYKwpFtyoac-EALTFqYIAg5hJFFP7pBdGBKuF3IMSYggGbHIGpdrSEKU5CWj6isMzpVaBS73HJxQKIjFShsYm71jCBWnq1rXz-Ri8TSfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
افشاگری پشم‌ریزون عادل فردوسی‌پور از ریخت و پاش چند صد هزار یورویی مسئولان تیم‌ملی جوانان و امید در اردوی ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105245" target="_blank">📅 09:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105244">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=BI4u-RUijah9CSPmVrsZiMd4dBGa2zlI5Cu2twPsgiAf6_ldHZvXJUWA8tRZSX7_4-cuUcXLiJP7TS9oPfhvh5WXzMKViIxDIUMpuG4fniX8xSabri8RFwf1z6e_gu51ZTObChwt5Fd4SXg5d-SJNaadurZn9tOfv72VQAV0XbjPbnqpKowgGONkgChhf35vu5RT9M4FN9CWXM_CeYvYA8AUiog0jjQpYd3bMya1RaPzgepsckD83XtzCy4TDeIKxwed-CI--4zKM2qi-5mNwcz59VQx3ugmXZQXmTaPdA4E8VGoun9tCA2QdnDG2jBBxp-oJ4Iwtkps1nYuQl7Uyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=BI4u-RUijah9CSPmVrsZiMd4dBGa2zlI5Cu2twPsgiAf6_ldHZvXJUWA8tRZSX7_4-cuUcXLiJP7TS9oPfhvh5WXzMKViIxDIUMpuG4fniX8xSabri8RFwf1z6e_gu51ZTObChwt5Fd4SXg5d-SJNaadurZn9tOfv72VQAV0XbjPbnqpKowgGONkgChhf35vu5RT9M4FN9CWXM_CeYvYA8AUiog0jjQpYd3bMya1RaPzgepsckD83XtzCy4TDeIKxwed-CI--4zKM2qi-5mNwcz59VQx3ugmXZQXmTaPdA4E8VGoun9tCA2QdnDG2jBBxp-oJ4Iwtkps1nYuQl7Uyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو خواهر پژمان‌جمشیدی از برادرش در بدو ورود به کشور کانادا پس از رفع مشکل ممنوع‌الخروج بودنش بابت پرونده اتهام به تجاوز !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105244" target="_blank">📅 09:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=LvATsXm5j07sIGjkEy2im5KLYZbXW6lmbTVSnV0oG8JzdjlVlPJ465H-L2u0OEXhvIzkEvkt6CbEpLZdUka0FrTO-jfzkW7dGdALik6RuuctuZ7wA_HDZ8j9GEGG-2B_PLgcwbD5F6U-v0IFYgIYc3TH0xW6lEGKEmPUOsyGfIxKcEltxuu7c7GW1I6Lxv6srbOIWpY80G9UbwmKBxEYFmsQT9dsWXcYevYhyix91Pej_9B1wW3YKxnINgRxtqAr42L42WSaAVkRE-1X9fhpQoMQl9TAsvN6_8flUAzZKGTqyxFbE94AUkZsa1HGiYPfEeGn2JCMGcItcUYvoh-9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=LvATsXm5j07sIGjkEy2im5KLYZbXW6lmbTVSnV0oG8JzdjlVlPJ465H-L2u0OEXhvIzkEvkt6CbEpLZdUka0FrTO-jfzkW7dGdALik6RuuctuZ7wA_HDZ8j9GEGG-2B_PLgcwbD5F6U-v0IFYgIYc3TH0xW6lEGKEmPUOsyGfIxKcEltxuu7c7GW1I6Lxv6srbOIWpY80G9UbwmKBxEYFmsQT9dsWXcYevYhyix91Pej_9B1wW3YKxnINgRxtqAr42L42WSaAVkRE-1X9fhpQoMQl9TAsvN6_8flUAzZKGTqyxFbE94AUkZsa1HGiYPfEeGn2JCMGcItcUYvoh-9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های عادل فردوسی‌پور در اولین برنامه فصل‌جدیدش پس از حواشی فیلتر شدن سایتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105242" target="_blank">📅 08:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETmvRcAGmdpRxIyEHjj8FNlLaWjIsNzAUCslaewXaOKrZNKpiwiPv6_FfMBj5wAC1yWepuDvm3v90whv3merqAB81NIX4AuMR5YUmqZJi4yRZI0kukJliWaDBT8jvs3zsRBvilgVjhIl4gX5F8DGNTuKub9thUfXLmLOVMxssgZLQyKkqIVi9xrZ3CjOic-SSIF7tGW2UcjXTeSeh2M_GGWvmWMGbdllsHfftDLvTnB8C90ST6_j-qxrQfdkAUz5Y2oIN78Nyef82pYTzXCoYl8O0-lMhI8N2Z2IANrA5AdZYbwg_VLXY8SZ9MDzSMVAR2ZJE7rKCqecdpyaKuTlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیك: 91 پیروزی در 120 مسابقه با بارسا.
🥶
ژاوی: 91 پیروزی در 143 مسابقه
با بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105238" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105237">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve25a6538fDlMK2LyUp9DMGeehY-2xRNqWwsyBan0fO6PRzmMDHXN8BoMZgQ1YbpvzalymjIPUSrbhzPPDLghUK-zsMLG2Th2HNina2F1qEvHZhfA_n1gcVlylhzc74W7zvel6pb2NprV6Hos0klBMAWI0Q8Tepry4L7YbTDqFyC-gc9nee7RqYUmKxMHiNAcQMEHAP3gJwJlp03aFA_IDb5q2XpUWLEZ3RPSJRht3QtSiUtc-Wvy3jcStIDD-W9kZZM8-6RZ7Y7YCiKXC0qG9abqfOy4knTMncEORmo1UDPYbDONor52ozUB6h_lfdeMEdC7D557RtSunsQSMtR-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: مودریک از چلسی به تاتنهام با قراردادی قرضی HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105237" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105236">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fadkLLTw3aQrfn5T_l1Z2jnfaUgjGRdDbe-4rzjC3ZIn30jKee1EzdhtLPy1cC62J7kYzzmz-QuK-xxB3vs_CbyUneDhGbhsCP_INDmpJCS3L7Susv6nRpop--_N7dNImyGvUBH38PrIQyu1zr85ThlAaj2foXwY-pGqE9qmfe2EFBVAs-1gXNE2eCUVsfx8W0rnQY4MfalcutCTqa0-2SyKHWzwzvSgREDPUgjoQEBnL0YoRCHnQhH4i3FKsEMBKYESgu0hcE2gXMvI581RMunD7Oty6sL8oEW11wghgkqVp-Ocf1lba4k1NwNe9Wlp5f2j4kvSLACgkBCKewcKrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌سوم لالیگا؛ بلوگرانا روی نوار برد؛ پیروزی پرگل در شب بریس رافینیا و‌ یامال
🇪🇸
بارسلونا
😄
-
😀
رایووایکانو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105236" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105235">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لامین‌یامال دبل کرددددد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105235" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105234">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بارسا پنجمییییی</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105234" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105233">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گگگگگگگگگل</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105233" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105232">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105232" target="_blank">📅 00:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105231">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی استون ویلا 0-1 آرسنال با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105231" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلگگلگلگل چهارم بارسلونا با دبل رافینیا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105229" target="_blank">📅 00:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🎙
توضیحات پیام صادقیان درباره جنجال سایت شرطبندی؛ من اصلا نمی دانستم این سایت چیست و فقط تبلیغ می کردم، تا الان یک بار هم وارد این سایت‌ها نشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105228" target="_blank">📅 00:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105225">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگلگلگلگلگل دوم رایووایکانو</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105225" target="_blank">📅 00:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105224">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105224" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105223">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105223" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105222">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=A3EueqBlnKpPbC2oFKpqn6n7sE9x7lxnE8QGtKQZkVBmBmz6aZ4sIgdcisJEFYGtf7CJDfS3ppAK7-FawQrNQjToWlFwvaEe-k3HQLaSqmt8zXdRjJm9grdYZMJesXVpP28PdN1fR3XuoLiwdr8PgALvAr3LUr-wKI4Lx6o_5__np_uwAoNuD95xQ6ljvzuGfiOYY45jMjVbp7E_G3Y25Ytx7QCLNrehA6jxQAtDQDherl0nDZvbNsbtqjcMFHsTDaOXHzm1i_xlClbO4tgKo_6O_0iUyd7_ZeZ7RiBBOXuSu5WpKH0zvUGi7zLzrqfSyZ53J5rhk46GJlPLobKKsxJH2ZEkpD2uqsiOsdF5HKkP4FqQczr4f2MZl_ko-OO8D9DbiwTSfLu6Ru-i2rZ2QX3TC3ekdSYCs5QJeLJTZpKdIC3_Edm8D7KwyBl1GhH4vux7G0p0Xbwq72nezg9LS3SDYLlEcWfHOYfKcYZCsFw4lU4cf6H0DFDzxSwsxmW0zKfKU_HArLgYjnV90Yz0GdqCnSwdbtqGz5YJVaKhZCBYon-nQJinAtbwpnCNtiZQB_LNf0HUq_CjDxC6WsSSHZTsxYl21wUoRxrbBK_27Egg4yuTNmWJEpotcFbS7G_3MD0AQabRkOWnEp7ANJwaVZG724Ps_zkxgN-HaYt9hEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=A3EueqBlnKpPbC2oFKpqn6n7sE9x7lxnE8QGtKQZkVBmBmz6aZ4sIgdcisJEFYGtf7CJDfS3ppAK7-FawQrNQjToWlFwvaEe-k3HQLaSqmt8zXdRjJm9grdYZMJesXVpP28PdN1fR3XuoLiwdr8PgALvAr3LUr-wKI4Lx6o_5__np_uwAoNuD95xQ6ljvzuGfiOYY45jMjVbp7E_G3Y25Ytx7QCLNrehA6jxQAtDQDherl0nDZvbNsbtqjcMFHsTDaOXHzm1i_xlClbO4tgKo_6O_0iUyd7_ZeZ7RiBBOXuSu5WpKH0zvUGi7zLzrqfSyZ53J5rhk46GJlPLobKKsxJH2ZEkpD2uqsiOsdF5HKkP4FqQczr4f2MZl_ko-OO8D9DbiwTSfLu6Ru-i2rZ2QX3TC3ekdSYCs5QJeLJTZpKdIC3_Edm8D7KwyBl1GhH4vux7G0p0Xbwq72nezg9LS3SDYLlEcWfHOYfKcYZCsFw4lU4cf6H0DFDzxSwsxmW0zKfKU_HArLgYjnV90Yz0GdqCnSwdbtqGz5YJVaKhZCBYon-nQJinAtbwpnCNtiZQB_LNf0HUq_CjDxC6WsSSHZTsxYl21wUoRxrbBK_27Egg4yuTNmWJEpotcFbS7G_3MD0AQabRkOWnEp7ANJwaVZG724Ps_zkxgN-HaYt9hEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
ادعای بابایی مدیرعامل چادرملو: سه‌جانبه را برگزار کردند تا پرسپولیس آسیایی شود
❌
صحبت‌های علیرضا بابایی، مدیرعامل چادرملو، درباره پرونده جنجالی معرفی نماینده به آسیا/ رانت اطلاعاتی، دلیل گله از گل‌گهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105222" target="_blank">📅 00:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105221">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSM65YvhwGVMQ07eJzdwsDSAb8HgJKVLPFDsXL0pFIa_LafUsy-IfGBfXpQMWiEpBdnleEmRUVzjapZ2pAZtGu5vXi8b53MnDF7yE3-NSkscH5EMbp3db81o8N0VQ2pdno7C_FgTVLL1XJzcznP4a_2OB2MpxwueTy-aeevV8UjeAAzfhimAT3rBmL-gXAnmE4ieTsuaibSjX7IfYmfKrwdactiNMMkSqGvM5ZAP6DKWIuvf_KWxdBrG5pQi_Qr8TcwXu5LP05gaIINlVtprhKlMROSve-gb0ZEUJ6uY6Nr2RDNJyDdhinp2Te0xu13uiQbCiciAZsXwfCSY_fFO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105221" target="_blank">📅 23:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105218">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلگگلگلگل دوم بارسلونا لامین‌یامال</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105218" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105217">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگلگگلگلگلگلگ تساوی بارسلونا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105217" target="_blank">📅 23:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل اول رایووایکانو
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105215" target="_blank">📅 23:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=coWyj9i1Uv9uUgOEpVZBOlmtptHWa7WL872PbYax3bo3mOSRRBJ1vUeiZCh3i9fs74wRdoWJdBDS6CizZptF8pbxAhsgRMJqIbR-cZ5P_N5mYQCH4h-Rc9bWRpgRrpeBT_adHibhQvsS_3TPd2tmv8jlwiBVIvlmbR_jSkoe-Fws2q1cfsoSrGS9i4AxKG5qE4N-w26j4nQ4v8lRKHDTAYWGTEICULopx32teCtMI-Svr7-YZ6UPiVKs9urExMY75LXM3SCdziYPdNetFVOiQy8RxfYWOpZX66qXhJXuvtFHfWGFZ3Gt0rL8UJ-d6eWVjwihu8oGzOxjnHIL2YMakA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=coWyj9i1Uv9uUgOEpVZBOlmtptHWa7WL872PbYax3bo3mOSRRBJ1vUeiZCh3i9fs74wRdoWJdBDS6CizZptF8pbxAhsgRMJqIbR-cZ5P_N5mYQCH4h-Rc9bWRpgRrpeBT_adHibhQvsS_3TPd2tmv8jlwiBVIvlmbR_jSkoe-Fws2q1cfsoSrGS9i4AxKG5qE4N-w26j4nQ4v8lRKHDTAYWGTEICULopx32teCtMI-Svr7-YZ6UPiVKs9urExMY75LXM3SCdziYPdNetFVOiQy8RxfYWOpZX66qXhJXuvtFHfWGFZ3Gt0rL8UJ-d6eWVjwihu8oGzOxjnHIL2YMakA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
در اولین معاینات پزشکی از مهدی ترابی مشخص شده که این بازیکن دچار پارگی رباط صلیبی شده است! معاینات تکمیلی قرار است امروز انجام شود و نتایج آن اعلام‌خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105214" target="_blank">📅 22:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
مصاحبه‌های منتخب هفته چهارم لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105213" target="_blank">📅 22:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=PpsdLgFjX0YPlCZAKQXcaWWhH1nlf_B8FUpJGXJnSx1feOoyPLgIJfbG6GED7TyQRfDtnsiT1ABWVdxdsLyaZvTSfOQifbuMdBtAoke9yiE8T0omBU5ofLFfkvz8xn5uHdGW1WSZNy6efOvtbZAB5nhSUM-vnCz4Ujgv6oFQ1_w3c_734g2qJnV7rcaDk1xQyLLZESl6zOk64RMdfIalPVKwT81PvllMBzeCumuZtb_TfSDtmSrZ5T7I626ox4wjFsJrE2ZFNdDapWxdkUauUugXyi-_IN8Bdj48vvHzvzv-GSuEm6XZajqxDR8ioaV9nVhHRHOOvQAqocf_hfoJaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=PpsdLgFjX0YPlCZAKQXcaWWhH1nlf_B8FUpJGXJnSx1feOoyPLgIJfbG6GED7TyQRfDtnsiT1ABWVdxdsLyaZvTSfOQifbuMdBtAoke9yiE8T0omBU5ofLFfkvz8xn5uHdGW1WSZNy6efOvtbZAB5nhSUM-vnCz4Ujgv6oFQ1_w3c_734g2qJnV7rcaDk1xQyLLZESl6zOk64RMdfIalPVKwT81PvllMBzeCumuZtb_TfSDtmSrZ5T7I626ox4wjFsJrE2ZFNdDapWxdkUauUugXyi-_IN8Bdj48vvHzvzv-GSuEm6XZajqxDR8ioaV9nVhHRHOOvQAqocf_hfoJaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی با گابریل‌ژسوس خرید جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105212" target="_blank">📅 22:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCco_JU9EwPzbVsLF56NTziWBrs04XFC6vZ1uDx2XgoUFhMZxIr1sf3F_g6c-hFwSfH7q-IdxlYFi_HlgHd7MXUXxaynKmmVTeW_nfWg80XBcrJyLWi1vol8s2ALVjHRBopomfhkV9k_ZxpL7WAShkqiaKsDduuxKWMEcXNzZu3ASBcdcrnaGjH-scJ34DefJnaYPquFxPKZjITjifH2V40fIw100609_M2iFYFWzh_vxEGlElLoQsvdm-4yEpYOkZOVtmv0tHDzgmqbHYI1i-PzHvr_QntwA9Yi1lWpb07v_RJhc5eovWwdM3CW_r1dGt5S73R3_G5qJU3HFT8IeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ایلمان اندیایه از اورتون به منچسترسیتی؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105211" target="_blank">📅 21:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105210">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXWQp686KnzLgpAt_0Yk3DLh3bNln3_vlr4D9v9wpjVIFeZaBfW8x1J1wUXoNUNckdj7JHpWGvAk-bORxIcuW-Tzt6FAspwmgiha_V3ykyv889XqDR8PamPABmmefV_esriBFh61EZEFsiKZuqMpNaXp1BTeagflVQxU8T9WKjevlVLzYBdDreG9sHIhp5dlYjLACR4EFCIwyp2rQynvZywvPloK2qOuN2GKfAbMDoTWSyt_ecS0N5ulPbASsHZK6e32xzZSC-meXMfL00B-UFzoByYcKMR1BiocsvjC-baSQ6GGGVuofvMsMF1rivMaE7T530dk0A90uXdxREbTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌سوم لالیگا؛ شماتیک ترکیب بارسلونا مقابل رایووایکانو؛ ساعت 23
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105210" target="_blank">📅 21:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJFmw1jvb1oKoCmeldQd0DdNrRozTVvzXDL52ir1mk69nBVV6Ev7ahHZi82MIU4GGH9s-lNwduBHxCf5amf5PcCxZ0dEGuvv2w0rcAA1kGE83ooncHZiRagSvoL496SGpo0oF8DE5g4wK08KrwgD44U-lYLhmdG_FRvz0Tai7ypnfZLTTvr1ZT3Dv4_zu8uJ6YDXQuU10hPjAbIPhij35Ia488a9pOwxSGmb56UN5h--0f5scb7vaSgORQ6W0sxr-Jwkr15S-OHB0zU5B2u5qTLSXTqP8v4-zEzeyUgq9_L4CDZHK-Jyqs4NfmyBX9MZkW9tt7qXGS53lLVsKp1GEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105209" target="_blank">📅 21:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105208">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6mxgLphM3OxOPIKSmVVDOlStzlBzx3EGPpqHngfZQm3slc0JbDoKUH1VihpL-yFUnGAUN6vJiLOp_aq7qXSJcYmbujve6c4WopBZu84QTZQEmsCjjy1I5E9-IgKbICRr3Ov78RFHx30fmK1BN4QMnLpulhT3jtrd5BFUaFJgpUGz7x1XT27LOPkJ65-y1fvxmo-TUmjZH9k4MD5EKMBwZ-f0UH7CUPwmvZ-K4_BO9PLIztfg86rgXFlYwqx0xdAL3OmCAk55UBP167iVHjy9v0oY7xmbZ_ji9ikHPZ1DYzKg0qco9vxwv0b_dSkH9Qxlso2OojGilB2TCqUy_-Ayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: اولین پیشنهاد تیم منچسترسیتی برای جذب انزو فرناندز به دست‌ چلسی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105208" target="_blank">📅 21:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105207">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMiciS6Ivo5n5EXJDepw5gCcZOw_Um47ScQvrHLr-cXdJOKyiPqhjXhW-QzoNN7ypUnMT11n8Jlw78X617nDBcDmgjTa2OX9pXhFsRUtVckto4KU82hV_pF0JAJBEhwt3qySe8Bxe9FbBBQS-TYv74j2Zd515OOjELEakNG4V7OJZVzEBTxLzDFdYOL3A-6E56tqFLSS3XkUOMYI1Ak92ARjWLDpyZXoeHQ8x6cmwDggSiev_gArZ3Ln_6gkRQpiDzXEJjs7cgk1A3umGWD33xcv3lqGDukLlkIPPAwKw4JY2KbMH--xy3ejLZqrZLwo6AVDYIZTmucDApkX1P7UyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب آرسنال برای بازی امشب مقابل استون‌ویلا؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105207" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105206">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOcPTO2r5Z2nbvNAtsAU8bMVj9oEb3tkc0YCbpMYiEmSav3ctPRMwT_WlJtHP5vuv-LkAOxLVYJGoCrAKZXLBhG-oQFUxMvtVXvkWTdCOswjY7cvCyRAYeDfxu1FY1wlupjnAEFJ3jLw2ZvpVZznoMEMbnmY01_0lDtBJ30flanDNxo5-x8XUSNu1k0GjuNRmdBalru_POnB_LmVo5J5jKq-ZA8Nc6O9kgUoBrwn62G_O5WWNdfYNlvGicyqu0qInadJvrQByZBs81nKgw3R-Dq2LaVPWI1eTizqRRkaeF8GZ8t_Q_W5jfhpoDAGnxoSYdQDS9YToTQUa4BbP53LTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: آینتراخت فرانکفورت درحال بررسی جذب خوسلو در ساعات آینده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105206" target="_blank">📅 21:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105205">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amO7Lx9XWLzk8W7vAmusMPynmRuKKA25gsVpc06jbLWn-P-TLCzJhEPCX3mbxI41TQvdgDGKw0XauKG8Bc3sBBaZXVK-ndwYJYYSdiztN78EmB9FIWyhe9-_vJmV-CmLDnyYP5bHUOM5lwyDJgyKWo4xa9HVdTMsAN5k_x9VQRyt6zYJRHIi0XdITrWsopoG6DHsv-d9nXqXgGRmzQjbXYufvcnnL_UTyrbaEfdV9XQYw-226fOvhQzEOwULvP6l3-S5IiyP3j4HL-6GJT5akPWmzPyUZQqHiNl1tQcTbhvDHtdzAqOKy8xP89YdfPm0dlEi0-d0nk-A3gG9jW4Kqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105205" target="_blank">📅 20:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105204">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq7BW3C-MQeYuFtwVW3G3CZQdM8jLrsu2TD3hPEs07RmH0vNwzKjmGysxitYo0g5MG4ZKjzsY5Wz5ARC-zVPQ_caqwgy33YVra0EBGBx2BAhxLPFZijjeS6xmbYdaBvk868dxRzwRfn-abUUvG68GhpBDs_0eTNbDIbGWA74TGaPGqdkuvcb3Zv9ATLJL79pN0w7fPaXbzZ2IC2p-W5mFKFcqD1hIeEgcf5X3PtYhBYTNm7fwPfYGKiqubcceyOjzvaf-3sYofm1AnHKqdE3CvsCLDWbmD7mxPemTk7zu55wRGxsPVOVkbX7A5EzfGRphAS2vCBdxpG0yvbUzNI-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت بلیت‌فروشی دربی طبق معمول ریده به خودش  زیر ساخت در ایران 0 گنده‌گوزی 1000</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105204" target="_blank">📅 20:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105203">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
⭕️
#فوووووری؛ بلیت‌فروشی دربی آغاز شد. برای خرید بلیت از لینک زیر اقدام کنید  https://ticket.sepahansc.com
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105203" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105202">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
اعلام جزئیات بلیت‌فروشی دربی ۱۰۷
🇮🇷
🇮🇷
بلیت‌فروشی دربی از امشب آغاز می‌شود و سهمیه هواداران استقلال و پرسپولیس ۵۰-۵۰ خواهد بود.
🎟️
ظرفیت در نظر گرفته‌شده برای هواداران: ۳۵ هزار نفر. سامانه بلیت‌فروشی که فروش از شب شروع میشه:   https://ticket.sepahansc.com…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105202" target="_blank">📅 20:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105201">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWJybuokJyQjdyKWbe-u4bSGAlXkUVbIf4xeEY8eGpwG1FlhrcxeG3SXfazpiYnrnr58R09jat4wypeESzUwNkiSNXiyiX7LafoMt8VaZqg7i2bBtjYweuepvWU6BL0ekYXFmp5nNGUADzpNAU4ylNDWhIXhJw5vxPihYlQrdISdCT2iyyiGXuem9B4bYVqQrPabOK9aA9vKEavZQ1Cl-2HqYY36EZDSjMEqHAUeeF5t4S3cFCHFqj6rsYMkhNP4sOlU8cUoRejsw5JyCp7MYlu5--IU6Xt2Qe4vkn1uhSM_nz1p7R5mBvqvgNfVRbC56bO_olW2d_MjpXfCvR_yeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105201" target="_blank">📅 20:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105200">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UG8Q2mNs73SiGsBHJ8j0PdokJFB9C3dKC51FYVayFBkTRdo4ZUSMcAiN-cjcp4CMujmawCgXm_Jm7qzvaaMgvweS_suD4Fq6Z2Z21qvloNoMsttLIZgEpa29BX80wPoDBg4iItiepuRH5Z_z7lxpuEl7U_gpYdFfyvDtoxUwp3pmfJPfBFyaO_aBOYseuWEfItBCKygWW_O3FUvucpxVac3cpfr8rfX1ddgBa_BP0XhPguShVA_FNbLM8Z1U-QAMvoKj0o_DFv2ZaEWmKQqzglQPTXdXMCJ3onzdkBfTESpRz9wir8fEiyJR-7du42EHOaRZpOPKlfQRR0HYszNLwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
قدرت دوس‌دختر در بازی دیشب رئال‌مادرید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105200" target="_blank">📅 20:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cb7444c7.mp4?token=GEYHIJDxUpz77KA_5DCLwQdu_bNMNmstI4Bing71vxevWQPc6pliZq4YMM60ub5n8Zwn5RAxfwPs9RKv_LD74Gx_cXyHSIZM8F7Q9MAqcp5OD3xQXkSKz4N6HmtpCMMirApMjZiUPbQE4gqL3Q75rihzA1Av2jm0vvKDqklE9lsaQYp4lIAPqH7CPpyzPLDNcgdrsSwbAcJgqYcJA2z669kqppQSZWU0r3F0lTZa7LIJHzKvkfgGZMpbjN6z6LSuj44sRsVyxp-7lkBAwlM8UEmruEbLFWRYyjnDUGeael7dYXMljTnw6ngnZLj_ZXSHhcVwcs4mmjlAPThWaAq9CnVW_ETvk8sZMLHvhjrZ-HqlfmJhqzk1G7a3AzkSXnPfan2zXFgdyU7G2NgTPLoOdMhdQq6caZLF4KAPEJIaREC-NxfKIgcqJN_FkbXKij_Zj2QU627OO4ZJZWwoGO8_t9B_-STHkGvRpOBcKaGRsqInjo8QOZTpGaNLqC4B5HluqFQLkiFItO1kc1Oti7H-JXAAoz5zkj3jEQHJV0RXMIseujcU6KySGPw3jvzk5Ss1aKD8kMUgDotQgn2rPU7etkVObIGRb9BSNyQHhVD1fJdW9AqXQcUbI3mFlkIJ011mIRedQ1_9miy1MKR-TVKJMgRNRhzkLTCLH-tt3D3xz1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cb7444c7.mp4?token=GEYHIJDxUpz77KA_5DCLwQdu_bNMNmstI4Bing71vxevWQPc6pliZq4YMM60ub5n8Zwn5RAxfwPs9RKv_LD74Gx_cXyHSIZM8F7Q9MAqcp5OD3xQXkSKz4N6HmtpCMMirApMjZiUPbQE4gqL3Q75rihzA1Av2jm0vvKDqklE9lsaQYp4lIAPqH7CPpyzPLDNcgdrsSwbAcJgqYcJA2z669kqppQSZWU0r3F0lTZa7LIJHzKvkfgGZMpbjN6z6LSuj44sRsVyxp-7lkBAwlM8UEmruEbLFWRYyjnDUGeael7dYXMljTnw6ngnZLj_ZXSHhcVwcs4mmjlAPThWaAq9CnVW_ETvk8sZMLHvhjrZ-HqlfmJhqzk1G7a3AzkSXnPfan2zXFgdyU7G2NgTPLoOdMhdQq6caZLF4KAPEJIaREC-NxfKIgcqJN_FkbXKij_Zj2QU627OO4ZJZWwoGO8_t9B_-STHkGvRpOBcKaGRsqInjo8QOZTpGaNLqC4B5HluqFQLkiFItO1kc1Oti7H-JXAAoz5zkj3jEQHJV0RXMIseujcU6KySGPw3jvzk5Ss1aKD8kMUgDotQgn2rPU7etkVObIGRb9BSNyQHhVD1fJdW9AqXQcUbI3mFlkIJ011mIRedQ1_9miy1MKR-TVKJMgRNRhzkLTCLH-tt3D3xz1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخرین وضعیت زنده‌یاد ورزشگاه آزادی تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105199" target="_blank">📅 20:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105198">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqkMOWOAc0XsezX7WJKpnJeuweW_7Pzz9ZqWK_UQdo7HULKeA_9tHoL8E0NOcWJ7SkOrmsGg-fSYbmOgoV854q3miSX66NpyuXSFvq0XbD8BufkwXjkuLF2JkGQs46DLW-760E1tXSeIzuPd42mk63wO6W98bmJF0bD314S09nJGrKyxdvP77lRm96D058DrQUb8QalGZ2QLxCXPA8dnADgWgN365o9n_OmoLkNX5hMF7hkcV7Rri4cEEnfEQRUEdbZE6jIYvDvBK8StJFKhYmVxMc35A9I8_T22csNHHCP8zkydEeOb25pljAiSlf-58BQRxyqEseKFjw2EMVv1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
آنتونیو آدان: به باشگاه استقلال گفتم که نه پول فصل قبلمو میخوام و نه دیگه حاضرم به کشور جنگی ایران برگردم. قرار نیست به استقلال برگردم بخاطر همین طلبمو بخشیدم چون وضعیت ایران خوب نبود و مشکلات این کشور رو درک کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105198" target="_blank">📅 19:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKKmrhEqKwuBx-LNas578kdYoFS2jr-HTVPSrYimvnaBiywBrnN3mlaYZX7s_43ckMlsjXqo9fOAlH_vPklNAAxM2Ytj8IIPX9iHEpgBvNYKryICTxB5KKlEPKiu9DsJ-S7NTYOPp2kTXrXV3zbaUhtXNn7NplDoE9x-RoFHiioHie8wkaluv5DFW62iQZLlUzFW-OSvEYzyUNL0hMTegRCKyuSVUNFBAMf0o1IEqY6RAmUQZ5XvilJzlEz_joBy_XwMRX9fCKOoZoAZyCFlgLRXlTifYaS1LLJT6gf9V6CS1oEMdV9H_pRECe57UH6hjs-9wXtgWFt8sZ1QJirNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نامزدهای نهایی جایزه توپ‌طلا روز ۸ سپتامبر رسما معرفی خواهند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105197" target="_blank">📅 19:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq-ipoVLsj0_dqGoiwmlXrDPD52ZUeEHir-pVcSf1Z8MGXdxZnqajp3Nq3VzOnoFVjJ_JJc6g8k6H41TignUj5FZ_3xGOgnX6DoRX9fZgdaN0L36-Knv7Uc6I5CwQZgYW8-u-LmhfkKT61nFEEjl6dch9NYRQvEmsV9fPcDZsKvxvM_-yvmoRDjdbLDM09XLWiJEWXd7GzX4D5VcSF1_0euU5ZYlAqhpxN7WZxaTqKdSAMWrrUKiwVeu8TJDuGYK5i0IfQAjXzZH22Gj_0A8ZmBLfjMeXktqrGt7oMsrdWjPrQs4Hy9droioii60aCDRun_PSGTMRL9wdJK-rriyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
🇮🇷
🇮🇷
دربی با نصف ظرفیت نقش جهان؛ این اسمش مدیریت کردن فوتبال و مردم نیست
❌
ظرفیت ورزشگاه نقش‌جهان برای دربی از ۷۰ هزار نفر به ۳۵ هزار نفر کاهش پیدا کرده؛ یعنی عملاً نیمی از سکوها خالی می‌ماند.
✔️
در دنیا برای حضور بیشتر هواداران راهکار می‌سازند؛ اینجا اما یا تماشاگر حذف می‌شود یا بخشی از ورزشگاه را خالی نگه می‌دارند و اسمش را «مدیریت» می‌گذارند.
❗️
مدیریت واقعی یعنی فراهم‌کردن حضور بیشتر و ایمن‌تر هواداران، نه ساده‌ترین راه یعنی بستن سکوها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105196" target="_blank">📅 19:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0D8bzLAKMB3TkhAE4edakUF_KO_wIYj81Ic8EnQrlUelSEHwE-R8mTwbLKGkhJV4n227BYZcbqG90FURVdfON-yfIAvuvHaTBizMaBQduTdKgKj2qn_-1YIfdGkw1mhBt3zcIG1kAPR402jP35OwRzytr6X_S0sjMJMoGjjaYHMaGCjyqMwRRbX6uos3dRG7aWNnVBnMpD7gkpMjvimQGEn2A68ZSZVOC_P7ovFDQoclYh3127ZMhn2NwJuje-NHSu5cPZX9eBpwVO09BY9ZH7cdcm6aHIB3em6xDBYQdNLxPBf5CD6mmwsFkrTdaiQV4VAHSHVsvOUNdMnyI1sfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اورنشتین و رومانو: لیورپول پیشنهاد ۷۵ میلیون پوندی سیتی برای جذب گاکپو رو رد کرد و این بازیکن در آنفیلد موندگار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105195" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105193">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddcd857187.mp4?token=sk4RFDtsBZzHMw1zL2qt9td794wBpehGGHrzODfcRnSDpzK_MrtadxxOUXLIKqMZauYRU9q1V6w2AGRLyGnAARttA6GsFt_vZ4lYzlweSxYvs9_HbIzbfx0T5V2O9H7jWZfR4YqivpU5Sk6JLq4YUCWwm_AgwUIhEH-2dlqrAuH76JK_OWyZH9sqaShxWDxZw7hlXVyIEntaQ2hIDuZk_gVh7VaPrHHGDbawJY9ywwEgZsH0PSjPJTpPaqf67iiPBqDYqtvPURoUYcq2RFOtXeKTE34JKml6xNLMHOfhuV4_OJw1RQhKxVfA9m6VnFIhP3NPNaeQELqx1DYEFi6gtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddcd857187.mp4?token=sk4RFDtsBZzHMw1zL2qt9td794wBpehGGHrzODfcRnSDpzK_MrtadxxOUXLIKqMZauYRU9q1V6w2AGRLyGnAARttA6GsFt_vZ4lYzlweSxYvs9_HbIzbfx0T5V2O9H7jWZfR4YqivpU5Sk6JLq4YUCWwm_AgwUIhEH-2dlqrAuH76JK_OWyZH9sqaShxWDxZw7hlXVyIEntaQ2hIDuZk_gVh7VaPrHHGDbawJY9ywwEgZsH0PSjPJTpPaqf67iiPBqDYqtvPURoUYcq2RFOtXeKTE34JKml6xNLMHOfhuV4_OJw1RQhKxVfA9m6VnFIhP3NPNaeQELqx1DYEFi6gtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105193" target="_blank">📅 19:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
▶️
🇦🇷
ویدیو جدید اسطوره لیونل‌مسی از دوران حضور درخشانش در تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105192" target="_blank">📅 18:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ3pj2_7eFLZ6lbPQJjErt-DVt2dAUSgMJ1HWjDHKgXqWQKWLj1OfJvJXf0NhOK17e0DBxyBwp2343qNugdMdMY_EMrn3Aq-c7IYJdDOOuCJjot7zrHpU6EQsWOpRyr_ONH-qteCDGJbHlJ4QJGNkBq-GNg9Zl2HYjDlBD09g8gpFewYKbblJCSMaebK5UINXOU9yhTjrQcfMrbWADXQwZxHxqdyA-P_Vodlh6gypBw7aWLqtUwvhG-j8boei218vJJJwLgEhbFZN9SNK77ulkK-sUsiuZpCbcmKDorrniohFQ_0k-5CjbHs7BtDPcqBxU-GurVnMuz8sIB-BLgZiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🐐
عملکرد اسطوره لیونل‌مسی بهترین بازیکن تاریخ در تیم‌ملی آرژانتین:
🏆
1 قهرمانی جام جهانی
🏆
2 قهرمانی کوپا آمریکا
🏆
1 قهرمانی فینالیسیما
🏆
1 مدال طلا المپیک
🏆
1 قهرمانی جام جهانی زیر 20 سال
❤️‍🩹
207 مسابقه؛ 125 گل؛ 68 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105191" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGxTOUw0mbkeNRujrzDs1TVOQMPPn9sz0IA10tIxIo5BKMdKX0AWDsiW4hh2N4JnCkbGoJQS5oNBRwTnfRrM-raWbEq1zE1Io1Ek7kIIXq6zQRMDykUe4rCfJwUCyHI7Xq00PE_ntXVjUxI0fC4XWr5tH2RdLw0MiGF4Fqr7CLajkg5gACVZk3JzDn9NYAjHQWAUgPXjIMQRsLYQZNRVZuIf6yoIT88R1J3B_DYuyiiPpsPKaxtV40S9ryBvv1bURK5v7eCuOhDmYMXrGmq3enAYJn36qcKie3ixWszVdIos0mAJZezj1NV5G5MYfSovayO1eS0O6M96QGFT-lCUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐐
📱
پست اینستاگرامی اسطوره لیونل‌مسی و اعلام خداحافظی از مسابقات‌ملی:
🔻
دوست دارم، و دوست خواهم داشت، و همیشه عاشق این هستم که بخشی از تیم ملی باشم. تمام تلاشم را کردم و دیگر چیزی برای ارائه ندارم.
🔻
همچنین، بازیکنان جوان فوق‌العاده‌ای هستند که در حال ظهور…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105190" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105189">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpTcVTR1mV0vKAnpXjb7iQqDy2w6jjgu70yurq18N_Aa98qhy2u_NvYcaV0MMfRIPcT1u5VQm-fhWRhE1GRm1gnc1Oxn3F5nCMPcKzbaKjhl-MyTPKi4b8epzDkux6M3GVUCrP_Kp0xrjq9Md-6yaKAemDpop5xlk-s2J2EarXayEBBwd8MT4cO4UgPwkeyAAHvi2mmgiaZnbCudlgEbT0nc9btSvnEDn30QSLboujDxaBSUUGJw0_vrtNW6dZY3JDHkk31gk2OAuFDfD8oith_SYOC6mrH744wd0goZIJSiJC2CavaDV3VnGVVNJ6ZMh-HA-QyRdebpTTZpaV5-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
❌
#فوووووری #رسمیییییی؛ لیونل‌مسی از تیم‌ملی آرژانتین خداحافظی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105189" target="_blank">📅 18:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOk1QlaLZtmzh-dmUHANPaZgJrc5Xe2rxyT2lfH-mMxBUaKR15aFLuB6HAd3xch01DaSbTfpBv9MO50GEYgmCJD3fPYWFEq3ZYrB1YF-oM3VC3yhsxdo1dhJEnVDuPFwvXyyeK-TcROdeSXXTmpgsFYN3CT_5wkpH_y9aDqUn2yGfeiSEdJFiI_JiAp1oBylNWjC8jL7iG95bgQsZTc0DNICYKuAuUVH0RC-dypLmh459Jtv4J8TSsumLod8WfkHgMl-UL9lLlpUrkFmvYdwWW5YWwUySaD2R0SZwwKwElJ8QFD8vG3lYb49mQXzFABStNAQ97D63OZiDnxjFn_TGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
❌
#فوووووری
#رسمیییییی
؛ لیونل‌مسی از تیم‌ملی آرژانتین خداحافظی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105188" target="_blank">📅 18:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105187">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afynCwk6yX-zvC0vn7r8r_2U6bsGG2R5L7LRS-2Je_JfWIwtHRqrehbPoFOgT-OFA4GfigxlXsnraptEp2uOtMkMSziXPO5imMM5dild3euSQrdaMXZV7e4iQo4fCxxMeFjAhtuiQo2kqhOYyW4Gmb96UgSWiUVTC4iOan3TYPdVF1LLdEsC89LECJLmp0wxs9VJTy2IK5KE805s_BmTyMHKnF81SoZeY9E4SbLnrxHVq5wmm4faZIar8fuM4UqRQD_VsuFYxXCwbPrQe-Pk4o8GskhRHWmQGV1Cfm9-3N3s7tbESXPrtQuFMR1x5vLx4K9lEMWoGAzis_9bC8Aorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
مقایسه عملکرد مسی و رونالدو در میامی و النصر؛ کدومشون بهتر بودن با ریکشن بگید
لیونل‌مسی
🔥
کریس‌رونالدو
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105187" target="_blank">📅 18:32 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

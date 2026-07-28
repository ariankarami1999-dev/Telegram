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
<img src="https://cdn4.telesco.pe/file/EUTkv9_pExAVTzFRvVPwypqc9r5yOzF8Ov72Gd-vinh0CNWdaFAw7Q-0enw-ZMGxeK1EaiMAbE3PdLs3At1u8MEpBOK74y_Cufu6f9f4kjsG6rA-QAq4SMbNocB447Kfyz7aDXoq9Ywn_h1gkb3KYJ1jh3DRke3r0a7tm74cyFU_jhgUS7Q41nKyeAbCBpQytQ5q38OPbMFZZY8VZ231LzbSKb9fQUPJpjgHBfASUIv8Hf34oixz2O6n0HjktzuVsZXgWknt5bhd0ptQfsTSxZ4jWAOdRHo-BMWtNwJUgYjxViiWuwQ9p1Eu4QSTTP8jlO7EmyJhx93vyCwtqndt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 611K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 21:37:21</div>
<hr>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6hrNUQD3F14akj1AxT3ljvqQPmtqb65o_CjPChGYV4_CcRsdQ-uOlyiqZyX-fqSGMY_aZSyVvhaJzCAuTDjJ1cfoIFB3yzpgF1E25eocdwB0zLLG-eVuSD8W46E-_6xvxuKxt69pSL2-AQwt7YDp-bdpYouQvevByUjHSuEexD_6VfAGnseirZ61lezqjRhUpZjCN3V1EF6rn0CoaKugkyBCzRv0sN7R5iRQdJvN_ZQxtu5qTZ8g3vNceO6pCnwdNx26qVhmw4lOp1eWwfJUIdqtUjMVKIXWaLeDv3HPRmgxa2vVJtnjyWsIJ-QYzOsys6PRoTEx7uj1_l1RCbGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOWuF1uw2b1K4hA62KWZ_1sZHILUNPxdpjLjpSeuOwGBm54GkQfYTwzxHpiv2ywdVE-scmFAsdWPI2iBZn-qy0zovWhb2w4izOzEIj5ZwJTBwUcltZlp3fV0DC65LiuAey-5StqnHY7WRejRTimYY2lxWtitmNujQ1-ClKz3agfURN-x2RUQWybcGoNbI5zMVAO-o4MgbQX0GRyvKD5pmLboegHMhqeCk9WiGliBhHfnGQyQOSM69WtDgyXGiZiAdLYQp4nEjPcmNAJLiIA0B3prMdQ_O25q9aiRrxAHSYAVrcdyCxF885qELSZr7AdrBiMSGxwG_FE5dzG4b4E3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=FMhhTBW-GUB3w-6mYv617S34H65sxmQiM_hh6qwVfsqH_aM5QXdQh2oSr7I8OBFeDjep1B8H4AzRZ3NzV9wV-yebS-cXHQlHNlGYmts1MqQo9kx3M-_PICytHZgXfPSRsIjVhWQwWvj4h6b6G3Ym52IkI4eMv-o9OtYFi1CSsCbdbhsibYPf0F1i3N_Lm8fmfpG6j4aJow_Hr8FjNHAG1gqPcUPWGkPcu4cIoK2NUYaSQaIoSI0QADskNC77yM9cB5InKKVlhDUKkEi2kd_cJRf66qSzyB4WmQN3rvowmJWzI3lTK3Oh9eICVvVTJJCEAeDX1sc_jCBYki7O0MS-8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=FMhhTBW-GUB3w-6mYv617S34H65sxmQiM_hh6qwVfsqH_aM5QXdQh2oSr7I8OBFeDjep1B8H4AzRZ3NzV9wV-yebS-cXHQlHNlGYmts1MqQo9kx3M-_PICytHZgXfPSRsIjVhWQwWvj4h6b6G3Ym52IkI4eMv-o9OtYFi1CSsCbdbhsibYPf0F1i3N_Lm8fmfpG6j4aJow_Hr8FjNHAG1gqPcUPWGkPcu4cIoK2NUYaSQaIoSI0QADskNC77yM9cB5InKKVlhDUKkEi2kd_cJRf66qSzyB4WmQN3rvowmJWzI3lTK3Oh9eICVvVTJJCEAeDX1sc_jCBYki7O0MS-8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=hHOm4SZZVcilAQ-iqEAgKLPkfUzYkbIQV9plcNZn-ZdCo-DnUO-VJ4F_w3DktCDJPXL1Du2D_cH9B-wa72b9pHneFBnArlU4DDfSp2OVqrFo29bAfkmegU6gLL5CIXtTfTAV46CXLYoNlcWehHz_g29qIGNjj1Y8BUJy9R5kaf5kLBwLKw5PuW7MFJ0KlC8BcVxpcjk9_Jk86FKJO-7Hxu2tkkMTzkbcfRwNVm08Bwg9KqWtbxqgNjtDBrZvMi8CJjLv60V_5rgXR3BvCIF0aaz0OMZ686pnitGd_B0t7wd6kR0t2sFLVryBL_wJ3v2JUY_EEmTMd9Y0kucSuNSdwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=hHOm4SZZVcilAQ-iqEAgKLPkfUzYkbIQV9plcNZn-ZdCo-DnUO-VJ4F_w3DktCDJPXL1Du2D_cH9B-wa72b9pHneFBnArlU4DDfSp2OVqrFo29bAfkmegU6gLL5CIXtTfTAV46CXLYoNlcWehHz_g29qIGNjj1Y8BUJy9R5kaf5kLBwLKw5PuW7MFJ0KlC8BcVxpcjk9_Jk86FKJO-7Hxu2tkkMTzkbcfRwNVm08Bwg9KqWtbxqgNjtDBrZvMi8CJjLv60V_5rgXR3BvCIF0aaz0OMZ686pnitGd_B0t7wd6kR0t2sFLVryBL_wJ3v2JUY_EEmTMd9Y0kucSuNSdwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpN5XpOsT_QRHp32AJMNql0ke3yHJ5N1iPMr4YjPt4aydff-yLbCwYQ3GMxgDQq2c8J72hiAed1TJDOT1pFsfXXui83yRrT_xBq5tuxh4AcIdNV-mwWSYEZ6d7ToassfhZ_NfqBOkb1BRy7Ekor7EZQZtNm9eYGY-37X8wsRby8qwjkZVLk8bIoCGy5HJwoJdXr0exEswLk2gQVDSKdTs4Edj27aXJzyjwxZTCJdSBdDh81W3MKXptP0dHye1MMZVEoxvtG32mFaAtUm7iaUFSoLNDHaRBE_i2QnSMbkfv_y4dctlwa0pGdFmQHTWP1SYu3pT1SM22peSw6M0W36qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHhqOy9m6ob3fr5ijjyMRhFttD3fx1MmQwc9LGmrFwFvBNNY_zpf-9_140WEuo_NlPxNS0Ya3e3VH3eqdr7qSXg1wFiLGgA1lS0IdLszLNDIJByI7T2aEfOGTV9wgAF_5T-L4NPaxubL48_2lV9UsV4_4c7qN8oXTVGgT1tc13dflEaM9-Sm5fL4186yaivTsYJLIQRkUdYMEc5XQGmnzrC-eIifIvAlKTto5z2T0KLbAqaJdQg46A7zcxYDP3OK6shUaZbCrc8Qi2LAOUCZL5ZVrO8X2Y30mEN9JepgLbPW_IE62QAhod8BmAkxGt5BjKxhJhWEl4GB6SWui1IbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=a8ot1x2Gr0ESD90FJB0UFJswsBTQRXaVDIQnybC1A2QXJ7ARGiztKbwz2_nC3ycnWDy5rl9WP6gdpy971eJHZJKi85A0g9AusrPd3cEU-iZgvzffc_QEQDponLV6jaVZMrkYX9VsJGIvLiE-klLwQwEyTTh0CRzpyi8FY2nM1EsV6Bst8IbeZ1hUAJ0v9dcvqD6JxH5HIX4rmfElZ1PmUvPhaBIfhAC_924QNiFSdzMv8rOt_mquu93qmfaujn202_dQ_DAdJPWnAnxJWUhGISqxRzxLt6AHHjkxfhCaXCe9-G8Sn0QZBLQhvb8lUGXJCCwPB7KwWh9IH221JLAsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=a8ot1x2Gr0ESD90FJB0UFJswsBTQRXaVDIQnybC1A2QXJ7ARGiztKbwz2_nC3ycnWDy5rl9WP6gdpy971eJHZJKi85A0g9AusrPd3cEU-iZgvzffc_QEQDponLV6jaVZMrkYX9VsJGIvLiE-klLwQwEyTTh0CRzpyi8FY2nM1EsV6Bst8IbeZ1hUAJ0v9dcvqD6JxH5HIX4rmfElZ1PmUvPhaBIfhAC_924QNiFSdzMv8rOt_mquu93qmfaujn202_dQ_DAdJPWnAnxJWUhGISqxRzxLt6AHHjkxfhCaXCe9-G8Sn0QZBLQhvb8lUGXJCCwPB7KwWh9IH221JLAsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTP0WWgiooWfTUGgsXCY6kvm2z4l1G8duRWdokHr6OkeEOJK6qh1ILcC8POeDZ5h3GqAw3sw4Np-SFUQ4uXOkbArObU1bgrzNQA0H0VZrvM4O2-kkdAhO1s9VQUOawlKi0Pf3YVSUsp6K18atbH4pF4_kNNDdPQ3QB_N6Awuf8IcaZLpXPLng94QcqSnNh38GSjSNBAopE6H5HPR7zF9jUeSV9oNaWHaCEpH4vQv47MAAm74OZ5PuTsESi0f1BK7toqP0w7u7yHoCpwfQbkFdSL1ik3jZe1ylposmZ3cPdB5hI1hh7ZEJx16wydoWxXV_T41xCctmZLp6E-BmbD9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0dDJHf8ElTQlfIU9SP3DR4EzoubMjJA41uACr9yQLxs8aa0hqd0wMQmDPkmEE1t9S3MppFFHSi71QH2ascjnEXRsSdSHsrCu2TQWaC81yAVcJHQP2lBrnQouVogmVbGr5VGjy1wrR_fXzmtV09tRsM5OOzP0BJxcSB_p-W9xDixvaZegZLNHkkqKSc5SOE1siGL7rvPU3paiemFo9rWzSeRzbpd_zt_C1lzLF0_SGIMepyY5kyrX8-B4gGB-o88LLvsNtAQUw14l6zuZjXoiYAp6NHFdzIjozSXb0sjUyRNBr5ZomOD-bIaTLd3TZgkPH_i4iZtdT7Cs-Rnxp_krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgYaaYBnWFtM6wUjaRHzFLtGO8oS9gzx5wIj9YN3rVKepHmnMoWGop6Itud43n6EMAwDmo5OTId9yXkhc09NKVxyOwSwebSoitRULv9XiuHVCb2Cvv3jGe3wp3Q_ch7jq_QLEvUSeF5tJ24yJa7NG3IWQN10jLqdaYuMLNYhl75iYa9woNlJr4OFYldAKTmcslLNkE5l8nEGKjzbUOnDHZuS0rWuHI2Ojszh7N2qxFDRpa0rBYhD-yIgP7IkrwXIhUCLZLSVh6yx4-v4NHADs8iccWIonX7OXkkhLzKQ8DdXk6OfisNT4_LLXl3LD1ClJffc6gI8LSg8FoaaikFDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn49UxswJzr7A7rqTl6yltt3t5umAlizphzabhHrXaeonfndMNbILVdOD2FCnnw8ufrjybW8TIeANSPq-AeEOOhz4Wm3KFgpiBlQcWC9u9tsJgMuCjed9nA68xQrWm_TSvGh4ABaLaCViggb6ZNdUlyXDkRKq0Kr0n2IKODTNb0p_ikecOpfHs9AK8FCc3XIOT_jRyvrvqUZuoTYDUG_64wmZCNmlfym88IRgEdHkq94KPqTrtwIjYtuE3nkwdsZ-D8uqx3ojPC2fAaY_PMdaidWcYZivPwWVSoWu7MXAsdGrjoz0SgpVz_tOv1YnK___qFbBK1lY3lYV2W4SLZp6hws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn49UxswJzr7A7rqTl6yltt3t5umAlizphzabhHrXaeonfndMNbILVdOD2FCnnw8ufrjybW8TIeANSPq-AeEOOhz4Wm3KFgpiBlQcWC9u9tsJgMuCjed9nA68xQrWm_TSvGh4ABaLaCViggb6ZNdUlyXDkRKq0Kr0n2IKODTNb0p_ikecOpfHs9AK8FCc3XIOT_jRyvrvqUZuoTYDUG_64wmZCNmlfym88IRgEdHkq94KPqTrtwIjYtuE3nkwdsZ-D8uqx3ojPC2fAaY_PMdaidWcYZivPwWVSoWu7MXAsdGrjoz0SgpVz_tOv1YnK___qFbBK1lY3lYV2W4SLZp6hws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2TygFC0OghHbh1DZGDKMU-7YuKSvBObKUg2QPeEOCUz5DrEbdQwCH_LEibbJNoxVQS-fNM7ontFLiVpK8nHTp7y8QMl6Mh6AtbDswEao5tzCRe5NQxjDElqxMRoKtCO6dt6VgZO4QlHq6wZ9-7Bu6PUmdauXfjUrN4AqzJf1qSW9sCGQ5eXPr9aAN_hw5ZLKM7fpADrHI6UDKw4hXKKR-SXErXVYRCtgSRCK3MBdPau_elwot2O9jVLBBA0B3ICjG-M-Y28zL3J3h4CNLpStGHaOFqQYyrAprO9xcMEnIyRWcYuRN_PWnhMZ674uC1jlnh2PbMcecRAWoDNwstR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMcHg-jxHzgFYIIZF1vt-mo05SEU605OoB2GIqYVxMXEjI2ZBFnUugydd5tS41-1rqun25317wvUMnQhNMJhrB5YmkbwMxOyxUGYUJVY64ktP3oXwh48jH4bGFbNS9p9hHVitCGryNihZHytDsECEWFFIClqTmPKO-wn5Dk_-W6lmEmA-Srgos7xZYXfBUNk8nCeyQUusySGF4M_7GydBznsvC6SzOtD_s_k2piMq3F5-g7vIeGWDC9obt9AqfsHlbCPZk-t5So_aBYyvD97y-YIpRb9GfptvzaOZkgC0e_-ZpEmHFwcCieU3G1rWpDpCzvaaYCiA8DMvBjM69r5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26700">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QclHNdLBiBVTEbLtWC-zNWhLhbIf1x0bggpXPW8Qz2oYnBQniz9bF40qz3JWJvr1V-j3nCYhuclUISJwSrt9I9urfZr6-7hoqGEEti-KTDhqyhRhnXZPb3Zsr703ZLEWw9qjQ6-DbPZ32R-gjU-b3Doj3tvoqXDLQt30oHgZz3IKis81GJSMd_8LLbQH8GjVc0vRMcZoo06ZfDM4rmnE_UInkUuxJZtY_0Mmw1FNFxHJg-2ztXAFYILFw30OOXaIZwNlW70mUZcmXxXs6N7O3EMlrhBDFI0XPfym2gtinVNzKgGtlHxt5Uo8F_IDdHQ6goxlPF2ahIUbQhrW7AemgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/26700" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZgrqZ830FfA4cDC7KmXrsJv9aPRLpR5dmlRIb7VVuAkABhV0iuH5R4ODfMo3m5odAwvI_9Rqb2DW3BDXO3wDTqfohgVddOXjVTxTd0OmW4T3HEfEn9Mw-K_d-fPBZUX6MShIODUkDVuK7BOgzSFISNim6VzG4r-mi_OMo17mhbcefvownxltGlbmkWoYmxRHd5_ky9AD0IVqzyrQmtaTnhrFdnahuFz_LjaNb9lZrtSeO2QhSi8EjedmItwLuX8q0d2uhBAR-k6Ssd5EFU2Fb025sawt4MXulu3479_U2246wX4h3DNAviiRk9g8D1n2R2s7-twgr8beiYZIt6M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B357tKHCB4INedvy_8hxa-KwJZRMvDhJhZ_eEAFuPjwoDvN7MnPDhOO9SRGLMhvm7DBh-FEUwEt9fDI_1-pPh6nex6-Nq4h_fzrI34i0XYNEZLhmoJFvXZmSwwEV4OarV6WOSLVeT-zwnTYWicQtUTSEfKTSdnYQWpRdf1NlPgczikzDA6pThLrrZkG-RNvDWSiq4RKAKVjRhe-qX2Cxn81PSKYDXG_HCuk9YRxVrmRodW6A-wuGhDCawt8MCz1Zc7WD_-JArB4xpchleRvXpCZdO-FKoeyO_gf5F-DlSLzHbiSfC4-vrbMZR68ethYEiyvrps00eF1EHFmo1jjYug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOM7tl8D_8ZMYk3uvCSXnGA4r_VG-1_VHqagYpNzgjQ9Pvoqh8XIZe1nyz5jSzXMyJuHs1hzela7LIHfH1fbJKXzXa7pTpu3gk0y8b3aQ6BaTPhkThjPiag8PvuKYld7kMDHC4iFpyas_C7W303Cuj4O8Q4UzqAkjCpy3kwz2CxqsURKhvD2qxdbbJh8WbWrwkeN3cRuDQCd_yu0S7u8Vf1ihBJOz1VGB_MAKtpQVLCXelmXCBMjpjQDCGAoJ938piwicj0CC673UQFYHb9g3eTTCD-PJTFl0h905M1jzhqwMWMWjB9WA_CsuUgWGsXi0Cvb2XImqH6qcO-gwN8iuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrEZDrSpZi__Cz_PkyGd3Kijqvrla5kmi7hZXTQz13KeQJfgMYP5NCLki0C-5pDEnTse1k1YZ0f3c3n65xz6sMqz4_hzteJV_pS1_SO54WefeC7DE_cybdhNU7-lO4jhKImUzmx5OGSItMFa3uDiLK4lV0WUGnasnp6o7FTr4JLps5y5C6T8lgQE80-2CMH_keFwgD52wqq4obrxMJU06XANnIg79nAnVkGsFeEd4iCuFqeSSY8HMAZoMgfd8YtzECNir1PM7U1YktEF4uObproxvfyr8GZmonZgPThaBho2v8zpt__XPw2QBwToR9DZLuMsYbYB1p-PmoOB6kC1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izdm8cA1pw2W5z-7tJUn-biYbsCzEbXtcC0RPtd5tEZl8odOmq-zfQDVvDdBw_RiOHM4TbQ8bookna-04QIVkgcuoyf2aIU5ga8t2xsI5mK_Ous3_r23exOJ-lv3vAlrJVyQdB9nZvbV9DHxQLijUiBrQSLdLG98sFBTo9W32y08eCRHRMy9wQan_8wgIYTDh1O50y0bOcgfaiJUYHbmx29MqYyxd_tghyFilUV_xGu2QbVMvuPhLO1elVfrGbflM_erkG8qV1EqQPyvYFpdNxlUhOZv5LM36v1W9EC0u0Na5dRmeEkujmiaYQ6Jy__Aa-VPdJHUyk2r_Qi24zMTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=nmoUds6rczoHpOShT1EKN3FJZZc7axDf-ZXKIVZO1bhAOqWvAhXHMaM8YtwpF9GYix_Znvc99Eq9ZQrsPmTczuu6joYnxZExAppk3Dk7VzaeFm9M1rc3g0tttUVkJwOHL9prgG8B8BAJfzqnEptbu1UhdLGE9ESA12THy7rfouxT9g2Ygc5a_3uEYJXR63DcO8jcfV6nzIftafajW_RmiCR5TNlREi_z3ybP-rhNhB9ncf8ASh_0b9lCENjsciOgdX8mGGryId8DCfDHbUGxT-Py1uyTdN4HWCqOQzmdYGBIeRisu00Mxo_3m6QmmHSE1iKGRi4QwSpnlhIUvFs3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=nmoUds6rczoHpOShT1EKN3FJZZc7axDf-ZXKIVZO1bhAOqWvAhXHMaM8YtwpF9GYix_Znvc99Eq9ZQrsPmTczuu6joYnxZExAppk3Dk7VzaeFm9M1rc3g0tttUVkJwOHL9prgG8B8BAJfzqnEptbu1UhdLGE9ESA12THy7rfouxT9g2Ygc5a_3uEYJXR63DcO8jcfV6nzIftafajW_RmiCR5TNlREi_z3ybP-rhNhB9ncf8ASh_0b9lCENjsciOgdX8mGGryId8DCfDHbUGxT-Py1uyTdN4HWCqOQzmdYGBIeRisu00Mxo_3m6QmmHSE1iKGRi4QwSpnlhIUvFs3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0yPY4D-v7YPaAXxBH0v82ESKkI0qH3bU-OmLZQkZYDfFtUvYzptSkGOvtYZ9bgKsRdMxS5TEzB43A4eJqI_eih-W7wLsJkUbAVhMuh5nqnuS4vmnwMDoWa02AVQYCFElDAjQ6b4pc6qzQ7fWSBs9ZHNyPeuBf-J6VnhnENa7yduQy_SzMTnkteaGt3BS3N7sQNMPb4xTk36-xSQ_tslGKfiDN_K0zmSvBLlTDcVTu3XQKOB_4qPA55dmPU8c-wZTanTY9jlbOvbN2w5fsM_98D_jDgQsXGpv_M_5yVdT2344a1ywqCkzYOfeSabS4_UX1m9IL-kcTiYh-DXwhkOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYqoUW_4JOCrDIdea6eVgBK3UuqYLILK5keZk7AYm-nmBQDS0qarZg5fI5u_NaYUECP6OGdxTF8bfCOeBleDR1CnIkbg6gudYWO3xIHyQ0xIttcry6amx6dS0qMMJl5CQysJoT_ekVZigY7hp8kzabOtnICqozbuzHdIlwK1xx10mjn6gXtbcu_TDAZ3GJPBerb8A44q0n7DRdaEfUqjbv3vlHz7A9btJVG8dA7ouZlEAsnGqC-apNEVLru-Q3lQVgrrnuTPhD17nGyinoV34FO1APOx4gN55fUanV57wZRwJ7d-pG4tSmFCNOpNMHuZHKzTTNM8pagkov1pqUjg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8LKrM4_iBx-NhmGtl9Bfs8dQJxstM32T0gc87kciglmArUaiLEdMpO8NldGjxHtXojfFFva0sJF7LukedNGj8iR7EEgNTYlJY9k5VJ0s4HULPSXx95xf9lucET_iq0zMIKwYLyTpAsaqIlJOS-xyqjC6XnlKDz2XoAb28j90yJokEMZ8rHo-OadKs_jzgFZa1bPqETLE-wZnLBDiR7G0l3u0LAe1G0C2dW-OAMP7611fcNQOKdDYc2QW3wtVc_nGh3A2F6gScjE8uJLjY5oyCk9oQz8iacKn9vD3IOsUKpLNaA-tEFC4hRkTghkGnNHTHosQD01RS8wYzdUpiP71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=QfUeCg4wTGC_13B_u9XDcGFlNhJXBKcr7sgeewJbvz89m5Lwp1Nmv5gDAMimq8RnSzpMpN5NRjWTHelv-FvnhchhTjO68WD3YKGIQpc1EeQx3NoATE_FCCtVWLJDgyEwvnP4DnWIRd0Y-yqZmI0lD0mGbEM4kSz9is-g0jzboo0fxRDHiIQyB4Et_TEqXI4MpYFYd16maEtw535PlFtEwr0tCgnVHByWqNk2nLiRTFUgHzSAGK80ttKTjgGu01m8iRRMKMCCFZLlYyS2nubGlRQbcLkPO7cUvCvTsCg7VJ0nciW88dVfAi2UvIfO4U5aBWf_RAnanrNXFucQKxIjrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=QfUeCg4wTGC_13B_u9XDcGFlNhJXBKcr7sgeewJbvz89m5Lwp1Nmv5gDAMimq8RnSzpMpN5NRjWTHelv-FvnhchhTjO68WD3YKGIQpc1EeQx3NoATE_FCCtVWLJDgyEwvnP4DnWIRd0Y-yqZmI0lD0mGbEM4kSz9is-g0jzboo0fxRDHiIQyB4Et_TEqXI4MpYFYd16maEtw535PlFtEwr0tCgnVHByWqNk2nLiRTFUgHzSAGK80ttKTjgGu01m8iRRMKMCCFZLlYyS2nubGlRQbcLkPO7cUvCvTsCg7VJ0nciW88dVfAi2UvIfO4U5aBWf_RAnanrNXFucQKxIjrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF5cA7nBu9SQkW_EKptWcUeDHG7YB4a2Nd61Fulvm8AJW0dXKBl2JoMvqU8u3ugiw2kDq8bj5eZ58jkVsWvaXfBp-qVOdIRfRFfe37_MpeIwYTz4htyZrWjYj5HGQwPltgqNtE2ZN9WaNmp7IAa6PUQipzpX4XGug9XHobKFbahBrVCzBicTsid3kp0PkrRo3WVnzwNI9TF8SGBoF5s5ljc-IRbeCX93kUjldPRcaHByZ5L9oXSq31WVYiI_kw5yV9DPgw6n5jfpoey66ou0GxUbNa4duK3aH1ELmkCUmTWh6F9NENR_vVft4I0Hg_ErdneOrK44EY2NHhgHSQRFUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF-Ly61OOcBDpzEUylFUTxVgzQXoTQyinZbSzseCAEuhdjav2UlUWd-CrOA2udEMO4KrF3fcMZXdNjpF9ji2CBeELDkRhYPlZEqKgr4-q6gPNzHXzP-LnzWTIS5uyvOlla9gqJu_x_9P2OfwxsEKU2uuYTaYFI89WB-5LUPZfXOxxpZue5JJ1Y6cv-0jV_aoeMarHiNcxr2ULkUq4WlvqPnNKs24he0ehtHdJ-DHmIc5LP9nzCMjhoxp89jP45T6PXMwxlBr43di1Yh1t8UM1-yMrL_ymCMhFcp88h-mFRMZ8XBeWV8MbVP1V5qjyVrKAE8_NeJRmdlWMVC-wFdgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm1meXqHBi-D74lLmSEI495Tx_aNs4ns-mZL-DeM6Fv9JnH1sXooDV-Fbd8P0FOcUGI7RgTvRZ6KGmW8xb9tiWvjcmgK_I8470SXFbEjcKBh08e53vB2TiGXSaSLCRjKN_VOaIjjW4_o6NbFMa8BUa_gszeb1Aw5XWqh0dTu6Q735O4jKf95ue77R7Ou5mwHRr_2LnJfP1tg5qHOY6BEX1QqMTspY3Yxhu5oDZf6TsvskYBqexqNQExaPzek0RjGUXRdAwH5Mwa5nwQ3AYzr_BWefXNg7jZGtwPvE6cpgNnwure3CCq7HSrLoQfNwwgZXP7wPHoZopDUYCG5pZhrhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heqIfoiVgxrSPVqLBXlMBOLMOLHcnPSQ-YZqhUjhub2lP2SPZyFixWSeDyjLKWxXFhuA54weyhyEt3mYArhGdfIE8wt64TWwOyLowJoR4TXZwf7sRiXJw6e27rAFQVZirz8fKZa5uikImpGx8TlalSGZYmwgQ6zPZadQVGabZAzly7SAw9BOH3nxzGG9KzK4rkrSVXtkV2u1qfl-sNf1URB6v2KIkJC4S2UPSd0qaihqRroGI7ah6C_m72MHwr9gzC0tit5vtS4ya5zWcbBkcqnPcYuHvhzZW3TxePVw5MdUWV93r45uFFBiQt_EZ5jg8RODm6cvEjLViSGjr2VjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilf7rqX2hI1t3BPZCIPn7sm0_K5T0Tkbno5EcVLLRDi3r6gAjkOmocTrrHnkOmzpJEPYUChUYOZEwXvxE8irOC7gpwwiTJQaZhh5-9sFCSsFxSmmF0pVGcwMfGFvXRb8pTnFSxASIOn_YqbhiPvV8O7o3mYebgnnwQMUbIGFISDs1zuy-0Of8bfGPGFQQ-yB9y4mj1Y7xQVH6OSmtEvi1bgKM5JCUWypCMMHLNnGfkzncOZm_leBHYE35k4nvxA0Sf5T_LnHmcY4OE19yH9dDDt7AdWS4IHTTJq-EDKt-SKQS8zFX0ZQD_ZAmSm_gNEv7BLDNu8AX-Lfm_Dp4nhj4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fknwoWABY91d9VazxO_Ej8XsSynDaURyfWqvnoUsfEafbcHwkV0yKQ-2klhtxozBkRJKVxEqmh322z-dCm6LmZI_9KFx5KccHwjWrkuxWYd70_EWUGO7wwS-kDD-XgnfrEns5ugWdnDu2ZhGu99fyTZ1OkOQSC7WjWh5TQZgitI3FW2nb-so3wiyGxzRo-bJ3_xct38nweI7Vn2y-sIj5qbpGj5NtT5AISrzHnc9qbZFSR0KLcwN1Dfkaxhd24DVQjHvBiOHHYla6xgs6wZHDwzv8xufy-fSxCJ-JR4Dxmm-Km70cC_zhsTfr8FeODpQEn3VuRsFhE6I61F3LXTt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAzU2iGo-2cHSItWIaeWYPsldxxzKrUBg65cjgNWZ9kYld-n7VRBNLRE2k_aKxfMMMTZxXCSbSADJid1wNoearh_ODFtndmP0Nta3K8p-IFknFG65FdlfDlI2BV9CHDyOd9RBs5UntwKmoLZQPkZOzyxL0mvR_LmjjAeigNf3-fBzOJJiLbfhq9WN0NWdRohoHLcRflUUX4-mcbmda0GtdER_5cMXWK8UeeVGwmp6lyFbM0LmqexWv2EHs1IvrqEFhmAyj6Y01QElvlo9pDukB9SDGx_fpTbWOOOyG-_KXBhA2tqoTi3XHGSGhrelZTCoufqczSvceQY7EJmqqQV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEgFnZK-GuZ-VNehqriBqO2YsVBBpu1AMyqIeTY9n7WlgST-Wj1BoKtMeYRYIkhvo-MGA9Ie3ynIsfogfDFuWOVM1ucy76xsV3jdGn_FRawatXrqHpb-hC-LQEoAbOMrH0RX1R2YYOJqNPdVVjUA6K1bhnIMfO1myB5Hp4AzKXR_7-nq43dOdOTtFFloMQwF7V7Zkt_rmNetGb8P7ad616VeOF8wVPynmOUkZg2p169CMS97GcNEfNGpj1m-F5tJgCZxjKVHeLGk6Kxt80UmBrkW0OTxhpgvcgqjWzgKSr4ap7G5iPGVc86S2nxrYRCC_iUVEp-5Zju7O1RdMUkRCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7EPcFjaZrcKIg54MAy5vWaQaDjz_fpgQIHw7OIIbi-rcOiBhd5dkJgthV3oaiOMJJh5m4zkWz5yXlQR7xTZ3FJeRBzBrRabTv7r_3QY0Icm2AcS980su48vMovfU3bie8A9gNhodUACE92E_NNKgzwHzs1Crz5PJZRCUwSumocA0XkqIq3fgTv5lqrYbTORzJ638Djg3jXEs6FmJcDp98FZInokiOyxPOE9I30TQOI9oEJLDrHkbjyWmX2IcMVyXM8O7adLxwsrURglPZhmF68nZ7LqqoTn43gGlUqLdsIaukMLJrabHdOzFpYFTFbIKB_s_4XQ9X1iY0N9dBifZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3emZzOgueKrHGHlgJhRwt38C4s0CiTPA9u2m5U-fTiLy9kCD7Npp9CZp8vmFuAPxxl_bgm5ZpaaNTveOCtRPmv7ngfr877Cta16w7TXMuG0AvOOLLgc6aCjxImXQsTBAIHIKj0RODi5onwtbf1ZuJiIT9gyeV-q1mFTW_bnWj_xUMAAa7CT-7LZ5T-RbPOyjDoNXQ1mqGj_IvX3f23i5FDUywO-qJPCfxaRBkrGusBkM5tp6HNJVCenjoHwVeQji_rpXSTQ3Y3DHDHeUQFdWxoA1x3i-WRjjbykTBF6CgIETSrX7cECn6RIVRWa-e375wgmVYCjuFMaRQC29WneMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY_5gEApdcwrJVNdsaaJGrvVmas6b2xWZrtwnf9PHU5yuoQy_H0RnG6bJnXnqnwTy45XG6JNFeplEVObDNXIyXazbVczLXP7YuT3Sf7PDZ38-DKmrSKN4fNKP0VpPDwDDaHexvcFchMphA3Z58Mwh6i2h78e5qVXUXI6gcBx93lJdKD7UxYv9e8WkGsQyufvhMQ_Z8-pZqmkUzjdpNBaho1X_Wyp499W7-83yeQ4Q5lnaVy3XEk9LiDNXzPafSSyvGhcjHSQ8yfyx14g3NxD_wd9lw40m_rnFeeHIY3rJxrqqKX8hss12vcY4FO0M8N9fDdN3zyMqRowBOCw3BHASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYP3LQDHABIaJkOWoezJLByqOEu1PdHzUdlhQEaN2TcseLPWq0NmN-29zAKMavpfvKpyQMIxU-gAK7rUQaXUropdbEiJm3XID-uJRfhG87T3NbQ-Bp0lDsrpOE-iQHyFPRJj6nKc1nSp4w0-b91jBwgdJdXFGBj5d_WBIjvOlmz7D_2_cI-CT9z51wXmJU3em3sM-YZek8Csvfu4R5zJRrYahHK_nki_VdCG7yMwqcK-7-cf-mJXJzdncVIMMFrCI75o_VSRyXFjmN73XFZs-Ae3jte7CnEeYhqzl-BHa6cmfi5vdeg3fK29lxxtRdjnS6-B3P0H45rRYUnHUNl3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrJhSX8iMbfe78YWntOCn6fhs3_euVJd889NAjOpeYJ5A9QDt4gU6x-hzfS40NeXRiFUfL4goAjWT2fUNHjK-f1jUfOeZ6wjWA7_j-jatw3OhP5TSKUExuFJCF4aPNTWwlgXxAmS-FqnhFOHTGxDbDEkVULtOy8zJF-Zg1v4G04CeFmVPNBBG1Y4fFqH6cV0k2pfM74AIKBA36j6o174NQES-6JdDz2R37M3iEp54-3Pd6VwR2SmFvxEA2rykDo6QWVXpF9V5aiN3uhOSJAgVbPuku0L-aBmzZNSB5eePowAMEBXm09ErG3kfPToD_yTDMbzqpoF8eOzOzokoTxsyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI6yKMNSqq-Y6N8LKuA6TrBaSrN3UPveSi0y1nQvQQRECyxwWIA1jn9cB_zzaaTH0aFcr2QFmIjO9Cui4OQYKrFIdVtIw_0-ygMA-Sh8NB4Z9mbA5ZTJiUNElKkKZBsKAdAhlU6efTfg6nmpOdxNIUMdNX8tNKT3XFbOAYSnflwBtP-alCsQj6cQ_JA33XoIon6rrfnfxRe6Uud4mVyTfMOdC66PlSPcgzRdx92r0tZkit1iRvcJPxREVvKoxt5enogQ1lTS4h-gK0DYr_iME0PNVtWJ-OMCjfLY5FDmcq2ZU-j-NpUvs4ki055-5N7mlJBgHYSljOC-7oITyl73HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mmmbwp801QYgocPcejv1g5vURpUn__XXMdvyUzEHGotcBCcB7F6ir27tIcS7aYEdKFxAfuvbHeqL6jTdeHLKwP_hG5VwVvH-r-ZecvdomroiCsTKsQEmX4EtLXS1yuPNktEZUBGIK_OZ0IQ06IqTDaK5qu_UGRd8Rm_Peg2ARWM6rPw_oegqkxlH78BAwPw5PEBeb_afH_OGucaJf6M-n9l85RZJfRpaKfhsood7KAANcPzoxtWjcgz5ChdTwLB2LtqwH0-mb6wqGVFwUc0Upc1RNLf1qFegwrfY2wTqjohgB2VH0DZdX5Y33hpLuAwCuV5mXwhRBXIdR2XKe9wn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsZF0gRfkgO7By0tZkS4Z_LQ6IXftR5XEnUejU9aIuSmxeBhof73r_bYs40HysdJT6iuWT5vg2p-Ir7CMA29ad4FhIFB9B3fclVkTFDuWcgcNTTdUXfkSYqOPQNYGWwyfHyo0z_SRBb1SaltEx3za3IbUF_Lv4ueEVwcUoMuk8EQSG0ZQk4iDKyy4qMzLOnuPg5Q2oYEMlo01u9UKs0TUDoSSZanSQ2uDoPKOKGNtDSEku9lQcjaeCKGJeBF7Y2huZKeDZlDEYVPZZNzXoUf5gSX83Px_45NkJOmc_10LGlHUU0Q9jnhE5z34B3bSmEbTTD3a2wdMJBQC-aofWE5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imCYgVFfILfNb1v7OsUFKwXxxo2pwJ_EUgkEXm2lQWQdfHTy44tEvm853kBIvE257HBn_W6PjJAKJrPflhxcWKv4jwGY8Z5Zl-D6A2GKlYMRQ9aFzpZOuycLQFILy8R--T7QMaDS2WF6fBmGdzLF7xG9NckkjcVVTpKycbAYcSBdFHfOzeOSsfpITHwYsbP1ZJVcCu3Ze-CHvhn9unS_MRFa3aroBVyv0u6K3tdYl2fxcTvldaHaZ5na8Aetff78ODUb8zGxvyKZA2W8ClJLRoqREAujoPz7p3yo0amU_m5l9fb0rhkHwmfx0BNZpy0b8wkz3RxawnzjYcBXAK_4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=qPbkSVCcvk_Wcd94sr0Tfu2JsUGPHSsbcnh4Q5b_xPrTA5Z7omiLP9EXM2QH0rP51LhccXsGTl-1B-6CTJLXS9BHGIRMWm101kb5S4HLki9qTHctV9mrXB4Is4gDm7c6iYsUc8JjVYQHqo8-canPHdXyTdpNXW9DNe4QmmCtAypimmEuF4vHPgjYDaOItq9FgjRLW3xXPGSlaAas7mPdpUYnGirgvEv-Vk7mqYku55U6YEQH0df0aRdMVYv0VGSneAvpGKXAFPGFad78Cjj3xFo3ecg7qCplLQRVeqanCAhxLuBiiLJybLx5hTLm_Kd8Xv5t0bZAk7W7DiGO235mSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=qPbkSVCcvk_Wcd94sr0Tfu2JsUGPHSsbcnh4Q5b_xPrTA5Z7omiLP9EXM2QH0rP51LhccXsGTl-1B-6CTJLXS9BHGIRMWm101kb5S4HLki9qTHctV9mrXB4Is4gDm7c6iYsUc8JjVYQHqo8-canPHdXyTdpNXW9DNe4QmmCtAypimmEuF4vHPgjYDaOItq9FgjRLW3xXPGSlaAas7mPdpUYnGirgvEv-Vk7mqYku55U6YEQH0df0aRdMVYv0VGSneAvpGKXAFPGFad78Cjj3xFo3ecg7qCplLQRVeqanCAhxLuBiiLJybLx5hTLm_Kd8Xv5t0bZAk7W7DiGO235mSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای بت هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26670" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO4BLJM7XB3BEWjQfSRWh68mJ2JfA7qTYAg42nbJyTa-hCeD0rA6O6KMvyBt1EWh27-CNG0HEhNFeCFgrCvy16ztWw17MYzpcGmDDErbSDxsYgrjFN5sqBc_lWeKJ7pq0X8syJMN8w11IxVWv5LeImO5kXLqwEJIq01FNRNsbzz0GtXUzTPwTukUYubGhXUGDVRQADZsLA_duaovd3sQBSeRJZv2qumrPjrY3QZca_tTxqDKNI6VoupyRiUj-VRfnKba441DQHZIObV5MCXCY3RsS4UqBNrPWC-NxWcsby5JfKCESVgthrd4Gelwh0cA_4n52xlMp86dBA_MXxCUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OB5rtSPCno3zfkY1-pQtpR-_AJiK4c6XFVsYS2bEvp-y_Nr4I7jmF_LrtjYkJ6gF6aDzdz9lKN58r4N3H7vHDdBF2j5cZSYsHzADjAVUWsAQOyzdWyaztbJarW_Z5Gek1lekfcGyoXCoS-JIwopeonwBbyyu1SY_6o3ReqsEHdig8zc6tiYI4ttPDNi9A_3TRy5UMM7jo4WNdDbfVlRyHIxogidoS_h-_zu7kDOZeYEir8ZalD1jB4QRovYT7B3AykWStbaH3SjEqZy1yfA82BvCZzRgd-3pu0TD4m7gZHompTTEyI_qTT6A_AMGJMkKR0omPObN-sBlJPCaKfmOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2aXxrQTNoKYmnDjuC946kON13BNbLzOkkTRz0rUyDxEI7uu_eJRsumeGu6GZICRtG7yTcIMo5Edlxu7WIVs2E-YAsgRq8LOysfapr_sxM4AE-Av-5uRwtbVXajXBqF6pqZsc-9I0LCnAfZBxBr6SrBFtvldA-0soQoQB2DYv9tkTU-pld3ZDpZVhVgxfaJvEzN1vXivDsHiMscs4kwnL_CklnrD1Ss8-cIOigmyFwz2HOGFkADkzcbb2jTS17a0UVdpo3tcwmu7-SflmAlisY9BcWIZngkd7wq7xuxf_LxqReAjSzrGTAlIatjdMCLkJkhUl7FC__xu2HCmfuJk8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIaIn8J-wy1fBnuQX9vlDfAEhG2wIsW34NIUmgTDf5cTkDZTs8TBUINYUJQpxfy8nxKuK9KmhxLaFIFOiJ0vtTh052C_xKAVs6Gsq7r0wG61MqZlCoPhvIRtZv2wywleoSG6OC74-EtMvhAfZCHj7akDuFoug9dOkHojDFFejh_rUGSLmavkmycZ4voGer1xJS47RpN5b5NSi5nXNBuYv-2Y5dA_usqnhqjbxXDDJk2VZZjpTeimmKfRT34NiYqYK4zgm-WoZQrA-BBqkcuSAGAe9MXM000aTuSVlOo1Q6c14N4mMloQC6eiDzZMsitmXV72iGnXlqe5mn3q5pz-MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3f5gyfGxlqqunEE0ZnQ4pYUZvZXm6-OQCLJwac1fLGKgm7sycZNpQsi9IqhVQx6z-pRMFGOFIz3p1F_5Ve8pX90aOTue7OgGI-3ZnbrtuUu7vjWFR_MjhSe9ffkcoyMdI0BXXbfJkXGYXgcKv6OHvieU9lgSht9PtFM8txp3Hb_sFrbYMIJgzfJMgjCbyTLeO_gcAsS2N_ApKVJZtRRJU8F-V66XoI4GgIX5YhK0RkDBddqbR-wEPgm5InHPPwg38P5SV2KuK3G3VyoeSMOgsQa9fnbKOeot6tfR07P_fQKkpBqW1S2idfsNjswq3s4bGS2WvxhB76tXx6R1t7GCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxfgmySK1ihH3w07X8OVIUc1nhA9vMS3UZ5-ry_1Ce_LsU5AMTX6OtEyToMLNG0fbvBsRz8JTW61DRY6vI9gTIvYEIBRsULsSkJEcyAWgrC5bqzKRKLl_4TYB246uj5UNqVhBBL49zI4LZh-jmwyatoleCxHbxGOkoySXngu09ws6YmJbILF79ehtHYuCZtX1zUL08RSPagXscJzx928VblBSnEFCecwHzQbp7ni3v_SPLWRHyPJ-VaHDH8xnw_dO0s6b7pnWt_6QlnXv1uK77gYWLf_LuxfJp5UiNLhy2n968bQWmewjihyKTvfxRtpYl6uRn07AXYrAxPZPHjq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT0inP7G5bKW6vN-4acM1NRddZ8posw1GKQuY3ZhW1ON5MqRU0jxxWP7_TabHcw4C3E7Xa3rhgaYgP2t1ahxV12LvVemTgbOd3vm3_fl3U5pSvdj_OPCfqx2gewpGCem1-0n93fd-dQZCy61WNyEirrGwKqblTQ-nfG0-dHux9TkuNXWbgeEFx7nDP5_By5XJACAreBYhX93jX5y8SfGsrO3JBK_ojTGFoMsWaAY-KeN2v3qu4OTr47rwnJlTetyOc_ZRSlX4F1i79vUw4_vgce2Hng-LTsSYJwzWTgyjvT5i9lr7jT2k7fRwvl3_ml5icKeCpWIh_kqYy-8jpsjUrLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT0inP7G5bKW6vN-4acM1NRddZ8posw1GKQuY3ZhW1ON5MqRU0jxxWP7_TabHcw4C3E7Xa3rhgaYgP2t1ahxV12LvVemTgbOd3vm3_fl3U5pSvdj_OPCfqx2gewpGCem1-0n93fd-dQZCy61WNyEirrGwKqblTQ-nfG0-dHux9TkuNXWbgeEFx7nDP5_By5XJACAreBYhX93jX5y8SfGsrO3JBK_ojTGFoMsWaAY-KeN2v3qu4OTr47rwnJlTetyOc_ZRSlX4F1i79vUw4_vgce2Hng-LTsSYJwzWTgyjvT5i9lr7jT2k7fRwvl3_ml5icKeCpWIh_kqYy-8jpsjUrLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyBw4I420WEwovbp6Fo5ZHMhesSHtm6__IrQrBhIPeTNeWXNonf-AfbyRhhdnzvbnd-nM3GkiLaq4BuYczrExJmL4e4yQ_ESGW63MX_cwGMgPBZ75Y3JBpZb_wJTEhd33kMkJEpmhqUsCIthHOQNvZAcekNcJpc8gU-lNG0-drJmYW9DvTDuepank1ovYWzrQvcUEc7CLKsgEB_4ao50caJtAKVlSAYTNkiuUo19Fp2B-0ZC72oUBEyhImIaKnpgLRLITxymUdbVoSZsL699Jv00hWg_jE7fAV-_tKDdXhS08h9vRS3YsmulpNN1TU04lZwZekbRW-oWDrYuNxP17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WK9AV18yyc4mVvNfLPMRa4gwLM4ZNBo4YCtU5f8A0UTQk_Pegj5hQevT4wYbzTFPA-pnBICOfUedv8Tbp6C-SOn69mTljvG5i5dW8QJSlEdxtYK1BdZW3DMHFKUkjD7vk8pidLzQ7zbE6juFPOGMH6V_39n8MrBlnSgDxsbGzQKs4nCErrJxrRml7QX_LhZFRFPBvu_DOwdyzZKJPcsRHWwb_uTi_cCbFJFY-yhk8LB-GEUd3okwrvzCUCebiOn5X229Oh3mJkLgUmKLOHVV5SKlkrglmN3D4mzlpCyYUR1fNL5BpyUJewPdO_XU-C_l-k0MlkanZKpwS4ZUGIUKyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHKMJTMX1ZUKJRfF948Z2pnAQpag4mJPJ8R6z9Qpujz1IYFRTHqqba1rAfauX5SJ3n0TJQyDd5NJRCOjTGioftvxCoTd9PdxlDkFDoE36hc3G-lis8qehBpZBPtyGRA4rwwn-reLHqziKm9fsNaziQNkMXYFWbZRRmA3evnFDcsuKVb1a5XCrSz3yM5HLJ1G-P6BvtTkZRY2RqFz2zumFO2idhhI6XX4TNsLpZ-c_2cj86pQTcHjJ_CIgScZ0zl24fJ_oEoangvep-kksDxeH5UF1bIG-GxalozTnaInlIi_j1Ifefd5h_f1BXQ4PI99uZJF3IKvnfznc3T2TG5PKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=l58L00SPQP5VTIT4qdZ9GoRwCUQ4WMmz9TetYo2kgYT03Gv1Og-3scvJmO_luzRepclpP0BHXxm_aCF0H-cdOLllMywASmRrzLVN4IfC0yFfxRcmm1wOsoUaxS4u5BRldktopcxeCTP7JS5Cq9JsAqQ5fv7461lbIbwBUMKniC6hKE920t_qw0CdHhdjOqkcWr3Sl9yPqeiEEBTVP37wz6zBuAeoE6Bm2zJTZkRLWBZSoI31L_lfu0urhTTO6zcHQgAnMdzbIBdisWz76x1hUlX4kM3wCGYKQnCNwBDZnEcOx8ZXsuwmomyemZZw8gs4az_QD29W9uz5aLdUnNtYPT8W7I-wk8hcYC_dxJ_1uK4SkoUkOou6xIOC0wEqzkozg2ONLA4aQyuZez1cRtOPqd1wxjDL3IwHIit0lRSwdbexNKPZFqw4ujIYNaksfgd9mywzpY8K9HEFy-OP-Uvv0MZZ1QXfB2rojECywjHHh1AwutxbbYL3Zs3OfjHl6MfnL1ow5YLSJymfj_WYLyOYBgD7WkR8SxzH9DW0Uu0EXbPbrn5h1JiPPKiKAz3D-ecQ2ElqK-tjaSlbM7YWR5HrqdsjZVhXYG1X0dZlu5CN67OmBy_LcnDPUHHVIIl0dIDwfw7m7CmiQhqfY5m7wRfLEy9BsgNLzPGvSaxM0qFIF5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=l58L00SPQP5VTIT4qdZ9GoRwCUQ4WMmz9TetYo2kgYT03Gv1Og-3scvJmO_luzRepclpP0BHXxm_aCF0H-cdOLllMywASmRrzLVN4IfC0yFfxRcmm1wOsoUaxS4u5BRldktopcxeCTP7JS5Cq9JsAqQ5fv7461lbIbwBUMKniC6hKE920t_qw0CdHhdjOqkcWr3Sl9yPqeiEEBTVP37wz6zBuAeoE6Bm2zJTZkRLWBZSoI31L_lfu0urhTTO6zcHQgAnMdzbIBdisWz76x1hUlX4kM3wCGYKQnCNwBDZnEcOx8ZXsuwmomyemZZw8gs4az_QD29W9uz5aLdUnNtYPT8W7I-wk8hcYC_dxJ_1uK4SkoUkOou6xIOC0wEqzkozg2ONLA4aQyuZez1cRtOPqd1wxjDL3IwHIit0lRSwdbexNKPZFqw4ujIYNaksfgd9mywzpY8K9HEFy-OP-Uvv0MZZ1QXfB2rojECywjHHh1AwutxbbYL3Zs3OfjHl6MfnL1ow5YLSJymfj_WYLyOYBgD7WkR8SxzH9DW0Uu0EXbPbrn5h1JiPPKiKAz3D-ecQ2ElqK-tjaSlbM7YWR5HrqdsjZVhXYG1X0dZlu5CN67OmBy_LcnDPUHHVIIl0dIDwfw7m7CmiQhqfY5m7wRfLEy9BsgNLzPGvSaxM0qFIF5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO7jGZ0nuK1WzwdzdXy_Cw6waT0F7F5m22xybZwvendDKbWyORJRp7d1uKhn9m3UWCqn9_TotyQEfX2fO3QwIuNdV8hkKRC442o6gvkTzAp7A4B7hsxv7_Pj_qr6_X0zi29cIiO4fTGEHypeIwA586i0bgcZW__FJL5XrxlJ6qDBxufK2m6VnLqQXdKGcyFBdXDE_xtbGGY3DLZZZYh3JZr-pbRmq6qytVlTD9Y9pSPdx_iWNTyCEb-gG9JRn0II26a6-7FnkZgfNjTSz3wPhvPUWiCFYAJznkws-67t6PhdKqaj36C791LjOSdJyRIioK234Wk8QnP9ah3ZUT1dWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twc0gJmEMlPs1WNreV0gZeEI1KllAXIP4JUJEFgp1mqMa8aFogj4FUDm3clv_Var7g0bsrri7uKo8Rr8tMSmQj0IqaHboKu88e8fNXn_2O9Rp1mahmYQvL9H6g80FaIpLXjwXYMuQbCachcPt5H-kuewEPDpL7Xw4XOFvSj0B67zlTetw54XgqO3PEVKs0YASKXxM7i1xWEodFIQwmPIHQN_9E1AKUQS4NEuNih8D-5QtuLQLV3g4PeFLSlJ2H9MUfkZhD73GHs-PXdpUoZS3TUmDQe1_be0RzdsKluUw3WKLLRltX4lKFduKiDx3TG3lA_ukTPiQVsJY16FrN2hJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=U13OQjHKQAyLgw49IK4WcR9tIVfnXBXd7mhMq0S2Gc5cIjcdbCXKJhDLBdajFcmUIZHV9YF_36AbuYh8M_0ZpE-usK3FQLOkmjX2zyKgr6TUfsqJmkrvEdMVeydqFziqCCT3zhmsvy-iL9-Js_zs-3YsLb_8Akm5ZyGBTyRCi32_c5fD2W1bSSv7R9a8JG2RB-Xg50AS9sk6LXiuFbhPpr41KQnCL3X0okx8aCV-BaAaXuUEVzG5j8mXSb3wbDwmGzyB8FmLLdLqUB9QhpH8ad4mGo5-oawVuAfQY2UP43NrgMP2-HFe2Ub5sv2hdpQEGq4HxEwwVAMymZPmaNsKNLIjlYMsRj4Wg7s1BydU3Qp79hyT_1ikiDr2UvuBF86kQPajvcASjGCiQc4_z9kEPYu4uD6aD10ASl5C3-nLfE1WBGF6DyjzJsn0cupEh4V5MQ8zjdit9c-aB3DB_YvUNHXYuxCs9zlAh5izkDOfL_VC9TkJmBDG2-JQ9UL_PKoHpItZnQa2xaklGwV8MjWIxKxinrLyktP7FGgO2ZEWXRXjb8zb-E8QNa9tJcieI4eYJ79sVkIubtTjkrTOjRdHy5Ye6ZP_6o2BihBipF_iImFLHM8A2Iv5rWD1yaw0RtUkNRIziLwZpwSkCVQAnBbk5CvS6i-7mIAY_ur9B78e2Yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=U13OQjHKQAyLgw49IK4WcR9tIVfnXBXd7mhMq0S2Gc5cIjcdbCXKJhDLBdajFcmUIZHV9YF_36AbuYh8M_0ZpE-usK3FQLOkmjX2zyKgr6TUfsqJmkrvEdMVeydqFziqCCT3zhmsvy-iL9-Js_zs-3YsLb_8Akm5ZyGBTyRCi32_c5fD2W1bSSv7R9a8JG2RB-Xg50AS9sk6LXiuFbhPpr41KQnCL3X0okx8aCV-BaAaXuUEVzG5j8mXSb3wbDwmGzyB8FmLLdLqUB9QhpH8ad4mGo5-oawVuAfQY2UP43NrgMP2-HFe2Ub5sv2hdpQEGq4HxEwwVAMymZPmaNsKNLIjlYMsRj4Wg7s1BydU3Qp79hyT_1ikiDr2UvuBF86kQPajvcASjGCiQc4_z9kEPYu4uD6aD10ASl5C3-nLfE1WBGF6DyjzJsn0cupEh4V5MQ8zjdit9c-aB3DB_YvUNHXYuxCs9zlAh5izkDOfL_VC9TkJmBDG2-JQ9UL_PKoHpItZnQa2xaklGwV8MjWIxKxinrLyktP7FGgO2ZEWXRXjb8zb-E8QNa9tJcieI4eYJ79sVkIubtTjkrTOjRdHy5Ye6ZP_6o2BihBipF_iImFLHM8A2Iv5rWD1yaw0RtUkNRIziLwZpwSkCVQAnBbk5CvS6i-7mIAY_ur9B78e2Yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZve0SIFOwGxdzzlBaaqvnnv6koy2oXitz3qnv_53sdhE1zjoLPujBS6k2bqZjXzpdqiiSLbeXI8-Wi4KbjKWL_XRaU44W9OauCf43tJZEpN_MBMJbP1pF8lGCAJovps11YFSweZe-RDWgPjck-CeOvegQ644FlVktUajLSUWUVsU_CESqBE-3lUO1XebRjgfOWORa9i5L47cQ8Dg9Rbtqx115t1hIiHNnLkY5rrb9TIRyVdpi5D-6u0yeavnEVG8jiYfgBLwDJydeal4G_55aB4DvqPAJ6LHh6Qv3dXoByXxmyil-PUDMEihwnDbORn54BJhJEJgOKPGWP9vh1-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBx0-Q_D6wxfqPUyVyNlFhjo-8tvaibYpY_be7FJ02bQOyxWk_C9vKRoRO-0cpG5_J65PWOoqI8UZQEzTomvHzpra60wVRbPezXlwntMkoTyK9f4NC9UyGpUNaMA1s1vBi-I1enL9dHRMMgkMsCWUHEy1ck_8wAh17p2cpZMN9gVA6Q1UrxV4jcFZH0kmprAqpJmMI0BWNxy7Lp_yvzsmyr2ij1yVaa-EpbXIQZTarfEFHi9_l3qLgnl7D4nV0EgyY5RCXDLI7HYYKsGntoF6jCjKk9PK4XMddzNfr5LE7Lax_1T3etDyU29qt4bzfZETyi71KwC2E9dyjDnPOSkgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW70tAP9A0_0O8pfUryhs8obk7jbx1eP7-Hacx517_jHCfnMq6DxLHhjW1MCtyV5SEWVDQwbbLINR7z3WrSfLvyJNxXlcodYnl1GxKH5s5hgFOIA3RtuBJZf9hWKpYa6ZIMpjb6EHida0_UqtLG2tW9Hl8YqDsHalifNOXDCvu8yL6wdUPDTGBtnNNY6Ahnq1dyfZeteK0exx_TPsOB-Mf_R1yUqvgpzqI-7_uRdEqzs70wqjxdn82924z8M8YbYvvNIiR7Ae4Iuc0hCCSyy1jiYUzwf-nbZ_PV1bYjcRUNAU4AvOjy1wnrzB9Cf3zJd-2A0O9ol74q5G9oIj3obwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=Ve_HkUrcEvk3wvVj92cdoswjEo5mNQrBJ1aQ1WPtFPkomY5HbYKewFW3NtTur1i-KpcUAc3EG74CI2On-FZexVZCLfyZjVUI_9ORMuyC_JbBE69kPZW0GHl1f2meppwuQqK2V2ic_7yYH8bVeON6oxEpCaMgdhD-u6SdObQIXwzlp7WMgxWqb5VnjRhwBPTNFnf-R9KVQvrL2YNXm33PZr3wcVCbLKQTE6xDr3VsbXbA3Vv1czF7adzr8vrbAdo4sR6RdtDtVZ3KQA5oknaz9sD0X5q_HAakqf2_i4LB07iDaVyJbh0H1bWAn-fhi1ZAHZpvWcm7XWqjQBuykxNQUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=Ve_HkUrcEvk3wvVj92cdoswjEo5mNQrBJ1aQ1WPtFPkomY5HbYKewFW3NtTur1i-KpcUAc3EG74CI2On-FZexVZCLfyZjVUI_9ORMuyC_JbBE69kPZW0GHl1f2meppwuQqK2V2ic_7yYH8bVeON6oxEpCaMgdhD-u6SdObQIXwzlp7WMgxWqb5VnjRhwBPTNFnf-R9KVQvrL2YNXm33PZr3wcVCbLKQTE6xDr3VsbXbA3Vv1czF7adzr8vrbAdo4sR6RdtDtVZ3KQA5oknaz9sD0X5q_HAakqf2_i4LB07iDaVyJbh0H1bWAn-fhi1ZAHZpvWcm7XWqjQBuykxNQUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjhQaDEbUeyFZdPDa_Z-aNZ6Xo2abBjqNiatAYY_mnPacJUpQ4K--7C7IOkmWBKJQSMkTFl38snG9sP6EL9QB9Y5zClu07oUhTF9r7-qFpF3yX6I00gmoN06DK3ZDNZU4znnxFcA-7ftfqjVK73e-m60JBKwL6iZlvoPclDE09lF9u0JnUClpq2uamXR0lRXJkQWzrMTZrkdNKTZzvtiaNBdIXWmkRZ_1b3iDUeGYsMetb54F20xdwCnLJ2U3g4ZJ7Mbpp10A1kHyvq71rfcWaPyZw95hFz4RT_AobCxGgPYoGuoUbB9-ZsMHvpOEb0BxOEySBXfXDAxbOzlQ-A9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9DRJI-nDL0QR_qu8w3UEGCcyXs25Wx74VlbCPGvmw-K9JdelBcv1wzTnPeJm34Nrcpha6FcNoE9877c-OTT85ibI9Y-ltIyHXmtnXJoF5VG0L_ipDzg8XFlGPw7IkI7-kwtPGAzl4CF1k8kWEo-V_-jrGyDs9rGG_y5yiaaAp1TNEjGPdXHj_6YQNcWzlskkUysct5EmN7HrsIsZ-dyZ3r-ngTZd2bshLwfTWgpFKtjH2a2YoZRI6CBWNTGbA7rNCVOy_vWbRnAgutjIakeWkqw4xoY2NvAYDhDojBdm23d2VOFLwe4qBVvz9inKbJNPk6N3UKVMf_neCRoREq9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZwH_O1t3TdhTNYeXUbB8ihVtTF7JxFf-TM0Gs2HG6QgPI8Mg8hAORArbv1-5sgvDv8KwocPAyIqEymppluGC2iz3Wm15TOLjs80v2E6fv_vqzJbU30udaNV95wcD5E1L61coYEFiSukM_b31JAEorb_yOOL_RPsZv2jQUD5pPQLi95eexOMJIXVqovPs9z7mOBZTdhXEwwPQ4PcCE8cu2all_GWmfAZKZeLc8eaERtH_F6eDL3Sd9KpOdCk14X43OtDbRcT3YV5DCT8saaHSID97ptN13loekogCGX6leGQNToiLQ7wkP3VRhow0LpZC8NRY7EXp_jUYbkIELqf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=VWH4LGItvkknsjg6Agg9teYH_txHKcSyR-URWP96691_5pxHN47tUT4IsW4o_oyANgGfdmW7GPqePOig5UNPREpEdI4Nu-tKC4DGPyMKnGpt5AlC73MB0GP0a6pzWv8bAc90mpyKGH2RBL8LkOQqveIPbSsrPRXE7Vcq6wkxVmJ4GYe609a2yuWVNtXCW0ZUh8gazdrBXbP_Iwl8CFEKJ6H6o2YENoWSRQ19jwZ2muYcf4Cn9ebL5VKo-4Dv__LZcSVumd1BMtGY76koToqMRFOy6vIvhMWFD-4YBZQTpOxz5_58ouEnLUTHdUisCToVcmywwEEhhwJ0SIMcQRUDXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=VWH4LGItvkknsjg6Agg9teYH_txHKcSyR-URWP96691_5pxHN47tUT4IsW4o_oyANgGfdmW7GPqePOig5UNPREpEdI4Nu-tKC4DGPyMKnGpt5AlC73MB0GP0a6pzWv8bAc90mpyKGH2RBL8LkOQqveIPbSsrPRXE7Vcq6wkxVmJ4GYe609a2yuWVNtXCW0ZUh8gazdrBXbP_Iwl8CFEKJ6H6o2YENoWSRQ19jwZ2muYcf4Cn9ebL5VKo-4Dv__LZcSVumd1BMtGY76koToqMRFOy6vIvhMWFD-4YBZQTpOxz5_58ouEnLUTHdUisCToVcmywwEEhhwJ0SIMcQRUDXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRYL4oXQctRJnc2vCmIFYpubt5yRKui131C-Ct6qgwKEmA4_9eQXNYhX1t_z8oyIAsJKcUAFaWDEjj-p272-ooeRToRIlBB-qwd24kQ1_d78S-UL8PB8HHdiegsBGSIFIm7oeJuVFa9qSwmVVdtESERi0mQ3C8HWeQE049IIsH4r6DWnWdV9gcoX9upRPvlwzgh-Vm_rHH1Fl8SEESAAlbaLAc3rHjGMuM2Ml7_KtvVrHon_tB06HA1uL8i61lh1lcEysCc1ty3d1Ya-6I1_8DrvizdBMtbCpj6ewHd3WOk80w2jWV5j2D09riub_Rs0_c-hEPON-T81Io4F92mBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f06nnlFpohI4Us8hWGMCaa3ea6ojxBTAdQ0HJMEtt6Jd2aehXD6cIxoq9kMW3igfjb29aLelHroTr6-wYxym-ZMu23ZWcdnBTD9_l9SsIi77q2wdjiLSzvkVm3xQH2kf1r0xIdRfaYDL-VJWbTRrW6H1x9RqMf8-N8lMP8NVQSOXpZpqaSMEPeqidwN7pDB7tNnS_tpEwM4ID9L5MmBHSuXHy6bKtGebItv33wdBJsDfiAlYxuc7Y1mu0UGLo4jfCdvfiujLE57K769dhECQJNmyFB-acaTvu-2TG5HPWs8L4Wk8kE2tHhKWepgERxzDrtRAI-jwAlCouQrQ1hB8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFTNnbXQRUQsu2lvdjmVpnDxqQIglu3bOWljVDANKU_16COsqT8IT1LCk7XfI62f55w_KBiLMQgrdnwECh9NKA1yNij3fw-rWQFziUXDpenKiDxXHiHNd6l4qpRMmEZq2-dk9p1urq3gNhkDFwS-PxM4MDepK341ilVpM9QKjI8f6tgg7TI_j0kro0RmBUlo7JFpzJOHYcMRuJlmQskDQ5v7H1QdNH7-zaH-nM8yz2zse61UUHCNhKTZtDgkjLAwfrvx2Tc_kzZJU4at4XFGSjtA_NxQ9QLuRhpO0-2O13RVdlwC0RFztd1_V8HRovXmJ8JnYl-f4aWcLzwPrsWJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJGYp9m69wVgOTtkSiMZJozrUUL8UcIQBPp3tqEBzBrqlwd7idfeXJZs9Lo2KOw4MpL4CxzoTtOTJPGnjit7mY0FEXfoo6Pl5rPO_eXnHJvPCV5FE4rLKF3BZUCtQrMMcxFu38IivmdBTyqLmcwGhtU0ES1dFQWK7ge7BMrKvBHrZB8N2yrKqnajWbnkhz3WftoUflWXo7BzR85n7XunVoCygcGw9VLgwICvYRNDxEFRhshqW7eht_b3mvWMndHIHhlIHU9IpBzF2SyovEhW3lffrRMvsxZg5IZwe1ALd6Jbww_XRYMJg95cQDofJrtTNcYf1daYOs-s1r47_q-Iyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blGoizL5XImMt888-ZsGww91ZO0vmyHQqae_b_OI3896phBw-uWWt5XOqkPI2EJDyslJclfbqO4-xXAoeWFU02SfEqvpZLa1CR0z92F-s4v4xkICXmjN0PJl6OchLLRPFSz1a4CljF2I0hW-UAalk_dJ5B-kJaZSOdDJDC3z5NPRFF7rs2fI0d3nvUH7zBn2WVOYwlmKaqFmJCnG0BiP0gkHA1dhyxJ1fbm8ZcaNu1m2TCu0JzJbw1HsKqHK3T404beseYcwYlRTY3EPY8YVEBx5vqxGikZN_L0C5nG4R8mPlByyjDcmMuJbCzfbcGmAB7MAmH4Kj4bAUR2xDdZ5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srXCCt27PW7CQ84kI0ayBjc7X3XAu3wVYmwip12NnnCA9HkiDhDMyo4JCzQeLKwRAqCJgX9JJe9z2A4Yume7fwf3Vc5e7hEedZk53-HVosy2luCkiL7LnjJh9jnZlp9e7yvwD-8K3rENk3c1YkxEGIg4Bua1J4dj6d0CjGiVkqtlCMTNXjCsiHxDTJNwCOUEzYuqRvMMed6bUkfZPTt4Y-Q-1DBjHhDknwh0ccrs2p-w0h9E21vm2fuGH-T3WOJus5BggfHJfxL1x3V_cwdpfbwN9-VCtxBUV7JhStQoNxIzNEuxuTflNZflvRyku1Cn2iiGiwZIe_DqIdILzHOOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRgZk3PZRb5AjY-19ilEw2QsDybl1REUXnVyip1TgFVqp0GCDk-n6vDhe_mFlV5phQpnDm9TQCdSKSnqWpi1hH2744Xqs8gdkWTMpkY9K0oZBhaHoXNy2AicaDy7StuqSqBPE3_jcdbfv1um73baKH1AO26pFVO--bKGFm7viZOf8hUrPVcNA5bni39ciTfTorfxPZ5HFebxeeA6LK8xKoaYsZnNzbm_SU2447z3ssEboYMvQwhagQQvYthCjiEN7E3wcBZ0N7SOCImr14fruBI_zJVIBPcefNqF30yaIrFgicKdGu8uEtSJVdOxdWnpQAxVjQ7h7wI0MhXU_sB2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xjxxy7Bog5WmZ9Ujqa-DlKQ1TMKaLqFfI9gCeNM0lvRpw9qF-N4XBJx9yKwfjj94E4GL3HuP4cGRx2QCs1R9Fh20Yc5XqDVPjbeKA8ARQy26Ofa-8ZRqNITEuUcskJyt-HREZzefyV4eiLR6lL1lTTtNLnpkWm_p6lz-VaB3_7PSIN-LdcsXWqhpZSehfXbMtzIpvvX2CvRQnyseO4w3n34T7K3B20wsruFLbueKX66-73eiIEkxoS7_BGvtDdQyiYusy7PKx7JVC9C_84BX20eCdrsMtuqelRbFzZj3fQrZOfLmg91THYQabIC6A-fsDHAMHj-OnCKjqNwjvZiUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv4OTuWTeak8F4dcgwvQB2upulnQ4dm_7aFW8OxoOUoI33bUy_Mjiq9vXlhQ4wIWFYotaPVIHP7XThg8D2vgY83TJZcBRS6fgQktlHTZ5KQW2VGyV3LXYedNJoAMsbWrjPKr-vFlAqvL3BtO0Mz30MShALoj7tji3qBv57e9UneigVQzwc_tPxV_i3PZbtKrU8LPKSnl5tssiZBnijMsxangvwUk4eLHgt5fqh_X80SPeqJUK77612ryETA6_N3tWlVYX--mn48urkazQ-GAHnIdm_UN-x61mdFq-1XHeORB2lQNcy2NNPVMbGwP8GY8Ur15xyCObTLxO5C5kVCSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwQrpC20i98FCJSCvs_-RVULEQyBh6qCF0cWtqCkZvFCa5FdWfp3mwFCofOZobi1r7Wx4c0ayaAF7qaiPOdtv1fz0_0qYYD89_YUzP2Qe36jH5sa3P5H71-9j6OKwEskj_7Y1s66ZoW8pv391hHJFVyfPhxFl0pMqIn_cnJIqduMmUdvNrde4xTrQdstantoPLp-i9Muli8-gFkMuuCnKGDBgkoMgf4iBxrFWNAfEbHGDNVU_nkoNQvTIBqV6WJAVKv5149swvRljr_0-XZRm4HDPZl1wRhoFep5fbgvB1Jb9y_SEdDl3_LhM_G6oj9bhfzCFWJmF_ndx6hW89dsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0GKCdRONRwdBGVm_RCphU3Grqvzm11pEDA6KTKHg7Vh8nlwapqSd2kIJk-klaVsQkVwWIEasLMu9SuVxpLBYGsTh3D5CYKFQQ3EM0JUiaVazSve7yPMymY-6ElJ_oy2sdfgsmi_0-6HucdmFSnnN2slLsBtDDa-bwvfJ43aBPLARvlstpDVN-ChxpCOY9vjs_Iljql_lWBq3FalK_nQntYjG3SCeItoAwuWi7SzRG3GcmoCjzMX4X1UIUb-kArpN2Cf8RKSRc63QPFT4oWuzU5QFGH_BJ6RSJADZwn93LHoZpR6JLWMpmxROOq-pn04NuHKcZvmCi0HQxGrAAtNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljgAE-UZupZxke6z3SmDs06zxKDizM2BDJVsTpF3F8ckxuet6U7-aHtaJNrG1GRVqvoiIQm7mIZy5QWkSn74gXoUEIGtEvKAqxh80JeIBnoYUTXtdMchOVFEOnRALloBno-b2AFOYmr4FBC7HWF8dm_RYy8jlt-yFMv1sO0UslgyO_OBpSSNaE_1N27848EgEOBENyFYPVY8VPjHJy-AnOOS1Dr4GoNAN7nDE8y4Ch98wAVfDfRBPlIJHS8RRxDA1e0mkwzvXxefDOjbrLLUNbLEqRxGEeimRXo9ImyJhgWYf0iWZpZBoLAL7ZBjUiZPGIfpH2Qdy4dWc8--91p51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL5GDngtSOhjg-DCdAdubxdn9MXn7nN8UuUX3CPSs2GEF0SXuborne3aPF0f1sWjpZwYUicGy3P5xohW-upOjUGbLKgCuLxuPiCqongypZCuZEhkIS5Y5-j5G95La4rjpsaoUPxeSTRD4V9vCUAjnITnvS8QzpKFQO-TOAr9BWtUoFar1ZRKv6B9aWZDbHFbN0RpN2-Vd6z4r0z-y9npY6PahyC8_0eUwTrf1SShhUzjgpRFs-hfJ_Gd35XH3lCFqZDdKB_5JZ01QJfj-TS5YSolAI3yq5f9N-0C_AUmE9Ug52BJj4yeLz7ZBSmVpcq_ynr44kTTD_jxbq3OyCjz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6VQPgry3D6Le3jCcJ50yInACoA8VuhwZtWbr4h8m4Uk13hTVIarv32BhHDgUckY1BQh396dm_169fjWS0BZGRwrfPi1_7UcHyJXnOO9PoO-19OLjGnJody03uVx9j8k0EpCG1iWuJnNHUfKvctSRfNOfzhyvMRToYVpHXnBXQc7hp-MTc6J-Srm39nViPiu3mZY2pD05RyzrlCCAJmyXDdcBOdIffiYN7Z5wcax6KowVx6anXpJJSWKXABsKYZY8anQAag3smayslAzaJGyvtg0vcdDnO3P1PJFd3noCFSh8IpNW5jPWwy4ZSJCtYSvOzEelw30CeNiBYLQ0AX54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9nd9PBiTXbhhpb8t2Jsmo7GviToKMorN6x3i3qVziesYHLEy8s_PRnYc7JwwRZqxefyMPpczvjel8negWodD8WoIDlsRSjx_oc3tu3Tx_J-Ycg9qqrjb7ZwXQiDLpSH0JDzASPf6k7xRyDyDLy3__EvkCTu9iH90Ng-VA8b8_cOPhFezuiERCK0ujuyZQmipKV1XBlhw30rHt-Cb8T1EZtMqZmjQaQxWUqEZKnA8IKXr2Zz6yzv9gwQMc_Ao444IbYtdJZkf-PhD4c4-hAVoEw2Lm3ZRXmwqbdOR4JW9MDq_3amDMd3q6gu_SLRTQ4MLnMSOb-L7kvaFlyxn9xjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdRYIWp5LKB1n0H9pOV4FPfhx8fu7NEfqMIkgEXskGhtMCnHPFSzA8rn-VRG85lPlu7R2ofiRqeQu7dZN5hQCgpzJEa6nHL6IfPenEwwT0px8BAojxExm20ZleyONAFRbm3xjaHeR1tC-SR2MN6UovSBc1Xnw7Ha14ldjBRdjpsAdMbd1T5evtAZURG0ofDwjl7Lf_woNsVd-ZsFYexq24TUFogo07JuQQvTl78Tn2Rg6-HLRamgPYdq02ETd8Nfyiq0c8c1mloOjxnuEm6Jf6b6epNa90nrXGY4Ov_DqpKgDMDqEjvcDuXxMfWc7fxH7F6YTYzjiUzrBq7FL4uGaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bj_FVjQbbOinGoI_1Khl1R8BDP-JZsRA67WvgzQOf0GHbvzz1u4QHaIJ4YLjhv8q_sPkL5K4gXjsnZVMSHD94EyrAw825YE-uUJ5Lk8RShFl2_5TrFVyt8YhN-zzo1Pov7ny4-DY1xO35VbzDChwQTAflkN1sAH13VX-1wiqXCs4e1eGt7gyX8EEde3eMFA_OMVCWqxBHOR_Ntledd_IIkngOjOmBsgIhMA720u59_gQj4F8iqSxHg4EnltcI5cQccV1H8IHOCdrIncnu8Bo1_19D9NmVK3dXZU56HAspDMdtpJlWI23J422K6Hw4SW9DtBppEkDshBg7Sq_nIplGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=GCunQpsVRSGsBm6HicGUOgNUsiCte6pKI_MT45e-_--X-MQl6mkEu0_1RJmKfjbMYF1UKkHxzp1ubrbpKUg_i_j0KLc4k1RMf9VHS19LKt3nEqVBrZVFL9f_Tqx-nA0t8PXL-pZbEdts4657-XgEueI-sezF1qmfbRGmwhMs6VkOra_rZwWDsSr87l5G2-W7mL0S7p3xGpkWJRhLNG78i7ge1J16tSHK0WvskPFvcxkvetiEmWII41CYu7jHCGgTLyNptUT1_SDkFf5KiOcuNDHpF62arWXsbcqFkixN8WCtxDS0JMOGmm_-QEFNhLQsvIIi-iI6hcRt_sLlqD6owA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=GCunQpsVRSGsBm6HicGUOgNUsiCte6pKI_MT45e-_--X-MQl6mkEu0_1RJmKfjbMYF1UKkHxzp1ubrbpKUg_i_j0KLc4k1RMf9VHS19LKt3nEqVBrZVFL9f_Tqx-nA0t8PXL-pZbEdts4657-XgEueI-sezF1qmfbRGmwhMs6VkOra_rZwWDsSr87l5G2-W7mL0S7p3xGpkWJRhLNG78i7ge1J16tSHK0WvskPFvcxkvetiEmWII41CYu7jHCGgTLyNptUT1_SDkFf5KiOcuNDHpF62arWXsbcqFkixN8WCtxDS0JMOGmm_-QEFNhLQsvIIi-iI6hcRt_sLlqD6owA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=eOHUAANEJg98SE48ud5amN0ET-_BMy4Lx5khAChrrCfrZXS6RlY3n96Y0QJ4wmGJ_ezTtSBqtz0O72kHfC1s1HXv2tkDYkwXdBu67Iqjf4BJA2X7fEGvr1Vu8dDAYnDMXsHY1QubqKqHcu_ytUlmE7W_b_tiC_Dw5BrHhKepuQapa5HF1rlZHN6gsvV6MS6f9Ue6nHWmKaUZeTe3YaJR8zwcrdAzVqivMSGPEchUiXF-JUiGfkfGQeYuzmvcx_VWQ7ZtCmaYhqqJysMKy4ZgSwBo1__Lc_K522cU4chTryFnf_MKStFpNPXE4LF-MC0ZiFJCD_5TBF_e6qKiHEZqrxOVP2zjpF4ozOQEVMlTGCk7gP3aRtNmy46VmKJ6bHoUNTxw-bWLG1YTOck4DADj5pBnPIG6JUIQoDXaSf7kW15QQEab60LqUNdj3TsLW0w6SMN6M7qrH3h-qePUYG5JdeMYy8rvSZ_2jRpkCQk4bGBAdsARwSZ8jMTgMFOFWqhLWoFvv-HAPz8QrCelSjjk_oNDXn6TZcfwNbkDonIEttdyO7k7M4XGm31P1QTGPyow9_BYBdf_m5z4ZWuzgb0CIISUiZmgZECVt2rBOt1WsUBKCYcEvP9Ca4TNw96rpWTyzTDgK60f83S84c-3iYR-2cDdZVrfQRtIXg5dsQuMIVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=eOHUAANEJg98SE48ud5amN0ET-_BMy4Lx5khAChrrCfrZXS6RlY3n96Y0QJ4wmGJ_ezTtSBqtz0O72kHfC1s1HXv2tkDYkwXdBu67Iqjf4BJA2X7fEGvr1Vu8dDAYnDMXsHY1QubqKqHcu_ytUlmE7W_b_tiC_Dw5BrHhKepuQapa5HF1rlZHN6gsvV6MS6f9Ue6nHWmKaUZeTe3YaJR8zwcrdAzVqivMSGPEchUiXF-JUiGfkfGQeYuzmvcx_VWQ7ZtCmaYhqqJysMKy4ZgSwBo1__Lc_K522cU4chTryFnf_MKStFpNPXE4LF-MC0ZiFJCD_5TBF_e6qKiHEZqrxOVP2zjpF4ozOQEVMlTGCk7gP3aRtNmy46VmKJ6bHoUNTxw-bWLG1YTOck4DADj5pBnPIG6JUIQoDXaSf7kW15QQEab60LqUNdj3TsLW0w6SMN6M7qrH3h-qePUYG5JdeMYy8rvSZ_2jRpkCQk4bGBAdsARwSZ8jMTgMFOFWqhLWoFvv-HAPz8QrCelSjjk_oNDXn6TZcfwNbkDonIEttdyO7k7M4XGm31P1QTGPyow9_BYBdf_m5z4ZWuzgb0CIISUiZmgZECVt2rBOt1WsUBKCYcEvP9Ca4TNw96rpWTyzTDgK60f83S84c-3iYR-2cDdZVrfQRtIXg5dsQuMIVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGF4ARe-nV91rNhInHVyQ7RE4lPM2jvO-6MA9vTXON-hQ1d_LuivlHZyJGeeXhQPOI5Btfmm4meSLkNaFt5KI9VHlCm2N8fmRZ46sBr6EXa-bj8UyishrI7UX4CuejTDktub1fIEsWtWZg5QWoh1BomCpB65GaEslyl7fbHxEmpOwYhoXRDrYPkUk95o-IiWudsve5PiIF5HLoZuKM_MLjL1zS8N1oxnWFqINul2vG-MK7J5JPJsVr9RRPIKaArQnDpVd-UuplxcYlkqhRuaLPg0F_VZzc0B1LVvaB-avUI2qDdye7qqPIkDq4-avmxedegGONMtOf5MFyV0DMPB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE7haZaFX45d_FD8ZPFRDdZpVgNtgvCCFwlBqxVqSeH470sXKKm-eG9fdSKhljBQ2hHPARUYlvtcEreKqujoSMtNMZHVk2eyOBJboTfKM2PhdZXMP_6LIxpm4ybSUUCjtOHeTUNRguStanrez4jb271-vxGOEKfb7SpD9ozvxvgVlEK1kNf57y1hRvxPJ4MW5Ap_bXJ7fXIY1UdvoYAhLpS8oe_6_3BR-ASS0g7LsDUCo34krgh1_DMCV6DoQbHUX9a3j4BqKvyP_nkV7aRA7ffLM2hRq5MoGNvU8JVfT09Cz9DGlU-IHEA-EPe6h7oBdSXfzYQ92IzgS0HNHcNtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE6b38sZPpTcfc-3HFHgXM6u7FVTwcu5hAt7574KBV9NSFGZcTrNmoNHEYRbaD0MMpOpsNniyx8YytIA8e5p8Geh1G9OGqyqa6oU_FWhgRe5mkaB5L5VYQB2cRsqPtjbxBoQtWiJL0y_ZrWycmImRXP4c7CBPfnwkoQG2b0DdOHIp49gmaB7E-eagto4z8vrMmASBx2yM1fozYi9Hq1HhcalyAym-pbX8Z3Baf6_XTfaBd_hIQCxz5pjB8Nb1jRvJ2iu3vETaaKWu7z2rXzt86Zqzp_FjOhIwjhS97gpHgDwAuGDsL4ogHBpqi4GInm-uaUnouVy71pO4Esm5CQMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuqYu7qdFDsCurdfZxG6e0PxuulPUX0aQaYLClKjbcMG7xLHuaKZiU-1XSsKmQOruuU8TDqHoF1_Cr1hryLS1kf02axRNBVDGQdNuuWdMLRM-lPsT2j3X6WvEYa7te5QJ_ymSF2qawt5jQfoBBeFnlrw8hDWmFTfpVlLZond7QPCvpv4BFm_x_PEjXg7g4eoU0xDpi5aj_6aDulBcWBOCsBjRA1uvV5VgeOsyi6I_L2Gr3yrgfp_kM0uY3SKDm-fYwMnMcn_d2VUlX3Sy0T_dAtNuqnyuSvw-XDkSXU8GpaolWc5bdnLFJzagV2SjZEaYEZofdVrgApD4H3Wfj4LRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=GpgJ1MvySHKGEABR1UFyeI514UGe92tUSCWOFL9XYbgFjYUQGr5FhHCYoUt3z82-qj_sSjebtOfsQoVna8y7SUhGOmzJhH4ymlyaxDa52-MPV9IpHEvsX789DaznuiMw9XQ_7QenNhWX2VCD06PjcRYzJc9lSA80EoksiPlMj4Wpt9gdTSLnEqTPN-4VH9ab9xIHKTHLoEsw-ctBt41pvsN45E62Rwet0rETBT4pv0711Wjp3QjDVHFUrFDEfoVID_N8dDbppmC3A9N5KNj-V0UIAycpOuIZ5_wTdDVz35dTowIDjiT-gOlM5GQuVMMLo7ltMW2id0xto9XZ444xUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=GpgJ1MvySHKGEABR1UFyeI514UGe92tUSCWOFL9XYbgFjYUQGr5FhHCYoUt3z82-qj_sSjebtOfsQoVna8y7SUhGOmzJhH4ymlyaxDa52-MPV9IpHEvsX789DaznuiMw9XQ_7QenNhWX2VCD06PjcRYzJc9lSA80EoksiPlMj4Wpt9gdTSLnEqTPN-4VH9ab9xIHKTHLoEsw-ctBt41pvsN45E62Rwet0rETBT4pv0711Wjp3QjDVHFUrFDEfoVID_N8dDbppmC3A9N5KNj-V0UIAycpOuIZ5_wTdDVz35dTowIDjiT-gOlM5GQuVMMLo7ltMW2id0xto9XZ444xUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtnsUOUbGxqlhmP2vCzjq8tMevWzL_qlVVRWHroRxLs4yhZr9c-78jEyUy-SI9SQwfof6-H9DOz6KZZfq6XJAKvpOSatUI58Ey8YgU51wKD7UXJUQ6jsLkdbg2F_bpVrcUbXqMN-oMjFCGucaOv_CMNZ3PGkcjMKyl7rqhlD_2sCC1CDSLVi5NzhKtOKeCr6Ch35S4uA3O3GFEAiyYNNQm23VVyk29D2-YIa_uo5H0SGAW3xVpGX4N7oJ8FpKrywETbAtKaKYWvy6Gv5YhuapZSZWRzsk5lrf0OUt0qU1TQxuJaBNucdOafYAOmbilemrMTduaOx7--qg7y3W4iTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9XnYY6nY4gFKKNG_P4yblEjxG0a2wwSC3ri4kfl4q9yP1N8vBG-jrZ1My2jK-s2QYz8S3GdgYsCAvnf4WU2IA7ez87KhrqejDcqMm5dUH56feNkm9Pzl6VDQJTTf37XYzOFoskeaEATD8R1uEZJzd3pcufL8nLyCAeFQp8YMx7bQ74TyJdz4Lm5tQ_3GdnTCByA4o4fRf4yRYwViyWk3kh4nr_kbf8ft9GC4zuyPfNua8oYTRriTGtv4YRnD086AHou2eDKWeB_3xkGpQDDe3-gYEDn0rWICTn_o1z68cmI_alToS9QlR8yL60uX5Qo7D8TL-b-af9ADN3kyKrrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjcVGFzyVuw08DU2FCKioxAur577THLY-mf5-rjYlS01Ee4m7mWaaKwoNSq5bPu0BuolIdJ7IkqOJ06qKcpUtrAxBFZ_w7xJtEe4AyWgtvzyayPAIyU8BXTYri_CqFfpx5vOwS1Wz21t5jUnhHOqu6HHIi0Mg9ApnOdCjxVSbkFAeCfa6FUD-szWyhvXgY_Djd6NI6yFpKT1cA9oRUE1QJtzoaP5pAEavAMHC3iLJ6SfnpcVMRMnkW5wYnw7tiZY91-i7fBA2BTxh39uaf5w90EshFG3EixgTxtGYtMp72WUhd1TqzRiSg-boVgMwKwBVmLVT09RMdRm2AUsuzD9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt2-pQErL6RT5mXjz0LtI_j4knOWcbmzJ5J2GRDZ8O4bQ51P6M9-IeV4ggEZBaXs2WIqpON_ayNx8z61A75slfUOQ7IUFp0h3S991eSSjetZNXMtS_XB5mJEgqycxQWrQ-SMdYIynKI27dwq0x0hkbbSoBx9LX-J8zqSauNZIOU0-jaGEI-AVH_Fg-X689GX31P0JTFluj_VJsPNzQfmzWCVuwYfCZs37s-_dWx6nk7iJRStJOQZ60MULx4oAMDovCpRo4d43YqgaMG7S5qak9n0hC189VTeVKPXY78bYfHca5Syq_NhilmLyceeFFUMzAw7FyrEIb62AA9sHXOqXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN_XIAbTdNr9US8UT3ylmChEQn6o8uQ2guibsqYqff_s1uOqcEsEYiKT30H7SB3-YnwW6EfZE2q1Op4p5Qg-YK9pqZl5XA6hDDV0jDQQ_iYHQYvNqcClTqAnp_BZtoGHyeKJKTCT3LodvRZASAIwO885o8NhaV2nGT498hGbd_ONoUfBwLS2r6e8HSDbPWhNTV6gOi94Nehj7NS50am_dVLEqjZIU9JQFr4_nJH5gubirzOywwcGnmZ3-XG3uREA2fvEK2h7-3QCK581XStzBHEQQ3BFtz8Mu-fJDvQaZGhrQJhh7_YSqVvfhJcTuz4p4lnyYZQu8DPA-WOf0TK5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWA__xWFfsudb61yfzv4Fcrm4XCiur5cYV2Z6lvnZU9RBPPwHumsgNmGsb_XfFoit-YkVi08b3oi8MkZrryMbmNUEOIuHsnELmgAJyJ_yO8Pe5HGqXrp-pFbYnIkzmOJ9Dm2fiuVZSeW8qjJv-hOJfjV2PwCFiWQGn5Xv58LaRHB5ZDQBZS7kltPAvcy9AGtqZA1ktZW5jM_wq0TFMGnAOyu9gFovxomgoBIFTog_iBu1Mk-wDVc1eKf7tzyUwmkRJMMXlhd1ijWQzAhRcBBAX87Q_UHJRKsMNK_DF5o0muRArKDPK8IW8aBvl4_HlL11nz1dQQCYAtdFCUPB0105Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-raHfQagX3wbqAd0hS2GShdy-dfxbB0f6OArossdOYLMBHM49mM_GJleLDzgukNUZFpeCYULeLYwNe4YvOmH6Dbgfv2z_u5u-GiDsD8Lw6_GuIp40bAH2Xqx2EOOtCFMBKqV1tiC5XqPMUR44hiTSNFCDq5NTUw-LknVMjRAnfVew2rsHEJqS_pCLrCnrRvOgrcMr4E7_DdLpIFgQ5OM3ytcrsoto2o_Q6Md4GZplVOflmUlHUYlparoSSHa5evP0Qfmlsz7wbWTBPSnHgLNX3X_r231bAbA_Z66a7XxW8Ev5oKIstjYYhDuEorGVyShg5sjhn6m7BwywEQxvdeTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InyVn3T435rtsjHX4weOlZJYrxcW510C9KADVz7L5n1xA6zbxq8JB3Ps0gwvKamianEGwhSvjcdBGtPKWYc1-eguGiWTgP4kr9IyE5Onviu0JREQKhx0i87hyPdcRU1p2aSD7mPNIlFB02Fm7dZ91NsS04pqHptpEz8hdaQSkC7cPqR8Tx-JByfBOkLdXWancFF0jqkDCMLnCvnpHMaslgv4c6DPIktwYHsMWo56GABo0rW0j8MpPKbMngmqs98UCJHhfCWg049DYxeb-RY_k1JRHCQfThWPPRJxEwb8QBHlorz65Eff7txBqDG130qZIw_cw0ILY32cY2a5NdQCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrCAqJh0drG8kLdlSIaC2Vji7c0bwjl1rn2b3z-RQORgQwC5LajKzDl7W3Mz99-9ako_6pjqJ4XMyS9CBC2yId_Z6JaOmCrEQ9tGLdFWYRHPFYBD5kqF_VKwQx2vucEbMwN9TGE8fApPmKTfobbd46r-MSayS__a84SpHm-3KKPoPeoNTjY5oaEOHPNntRVx3EqpRmKweY2VCpSr8oKWGr2CEn5i8-T3KRmRhvkPAlHXT8MAYwf4HBmNggsaNfQcDEfM-5IuJvgCPsXE-cB8nh2dDfaVcbUljpJFZF8aNYcMACSrZ8s_1NQ0mpndw3wX429r-s50XZSQyh68eer9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=KmlibMzDhmzDkzaZXddOnX7fgW3V0jzraaOT8HkygG2zUEHdh2lV51GeIIOdJu1PLeGFbnTEVuFxIQoSR8FFyMX-e7DcjwldFk8UI51JIvDREFPX3iKIyHXevRncdZdzuJ-XSurQXvfJ1PzeZ6_MZ86P_bOuhlDER12eNwapMrZWXqnCKYT6M_---NVLnOOhdp4rCa4FiSNOMGun5ddaV0b5vfBin-9WibPSoyblcSKd1ADJA_fdQTY6VPXKpdp4zFE74Mu6xTwLOmglEDlqlm067cf6VhTMjJJRS-wtT5HKe2ZMSzyK7JAFMeUDFDP9ZJS7jYcvvFPt-IVhOL2Idw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=KmlibMzDhmzDkzaZXddOnX7fgW3V0jzraaOT8HkygG2zUEHdh2lV51GeIIOdJu1PLeGFbnTEVuFxIQoSR8FFyMX-e7DcjwldFk8UI51JIvDREFPX3iKIyHXevRncdZdzuJ-XSurQXvfJ1PzeZ6_MZ86P_bOuhlDER12eNwapMrZWXqnCKYT6M_---NVLnOOhdp4rCa4FiSNOMGun5ddaV0b5vfBin-9WibPSoyblcSKd1ADJA_fdQTY6VPXKpdp4zFE74Mu6xTwLOmglEDlqlm067cf6VhTMjJJRS-wtT5HKe2ZMSzyK7JAFMeUDFDP9ZJS7jYcvvFPt-IVhOL2Idw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLOwYsOz4dRWFR2vAP2JBvMwOptf-6FnKjsfBIjdM6KSTMP1NaWGdKUri4aVcrhSG-vk1hc5l1tqmNSyG8aKS27IdHOyAbbNAcfVJGPNuFVeH37BhLL7peWaZFcUY5P2uypOGiJUqxNqMiZugPTqsFfRBDG7SuiwsVuAxKv5lTxkVI5ZHvXAFguPNJVlXy0OKwhYgUKi_n2stqkEBl5jGVz8X-a6SmWpeCl0JbKGMS-fOAHFxxp0wohRtUprIeVmcAPy1e3ObV99H5X5VK7uvxltwDbP__Cd_zwujj64tjan_VhKZzuyYNID0zN3heuMU-WJUb6Hidx5Px8YJLdm5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

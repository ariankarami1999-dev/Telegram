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
<img src="https://cdn5.telesco.pe/file/ZEzTZQGvM9NxmsM2Qm5055YaR0sFNFYwMoiiUsJvzvmx5b_EBeMtBCyLRd9pd7a7QlhG-y3DWv5avILRclvKBuXpkYlfaHt_YIdDX_2hed_qDe_nOQqq9zjc8MmKn4fza_7sRwhgiBP-Oou3vHFvmK6QDjxn8349LS0k4bV38JQEei1uV1qGe2zWEv5_Cjbra9isfC7AgyXv_stE_O0gCjlZbqSMrt9dB-LR02Yl87mx3dGwP1WF_XA8sLB5Rc5zctH8JjI5p0t3Y8pH5jnYcO85Hantv_s4c34q6aRKYNNQSvxZazOU8b-WfxYFJxGSXZBnpajlgrKaCi4ATdwqQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 479K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 20:52:02</div>
<hr>

<div class="tg-post" id="msg-103279">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAsZYZttSNGYa8MyAkJwf_PXS60pCqCQqnFPgrvnZHsjfuhXB7lkMMXZ4lF9LEEp7gVLNvW5JcNrVUlezWo0Pol3oMZJ0HeuTCNf6wgfrBK7bQfL_tFSNRdz5yWTmhjKKmUx1s216E51XbXAb5gkllwX0Z-P8oA5_W3Sf6w_w0t8QU4FV5XJCCpjKtF6QHaOsu_p2Kj3hUMrwpku5RTYpNGNzY5hCrd4wpYieuX4AyKcrZbiaibVdWjE6fnvAbUsDa7WpCb2KmqCnlYNQqPU0kNxmN3NmmkrbcwAKZi4wJQPH61NjG7VjJ9QkItfTRolQ6iMTaublCPy4zwftGed0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پائول هیرست
:
⚽️
منچسترسیتی برای فروش رودری ۷۰ میلیون یورو می‌خواهد. بارسا اماده است ۶۴ + ۶ بپردازد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/Futball180TV/103279" target="_blank">📅 20:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103278">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcHD9nk5nfW8ZGhJY3hqkXXg5KZk6lsUzOfMOh5WtBdGfYLcAZTQrnL4pmUGldnJQQ428rZw7RtSShi-f9rGJpBZJSeKFWo30UgZI8d0NXmG03hJoFli7A6Ny-nIG5zMQ4UlL1FO-RafLt9kL2-cD26GmWNGo4lCR9lWPq2kiN4hjGRd9L4eiwIeNwtKn3-I1KSFU1WCDYJ1A2l5LTTkES7UmAOF4bKH87BTjhCh5XYOr2K7lbsqGFbFII0CLBu044hLacgdFkaq1By-XPqsHLbdF3_n1FobrEprIyzXdMSdapWAWbjM2_UOLGULtbM9mEZWv5qridIqnrUoPHXJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
ترامپ:
ایران خواستار غرامت خسارات درگیری نظامی ۵ ماهه است و من هم از آنها غرامت می‌خواهم
چون سربازان امریکایی را کشته اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/Futball180TV/103278" target="_blank">📅 20:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103277">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfyvTqOR3rS5ofhycTWhWbdQ4mcFb9E4wvOYujAcYjxxcRWSGZoo7NZv92ghbVobuSTPTu44toW0LF2zBj-A-1nkRSOXN9KkiH4LX1meBfGY-k2G6W0aRmnzuIkkdO3uSaPkOQJlovPFgFAXRacoMS033pOll1G0QQ1djk61H9wyvukTJnUhYOUStHnOOa3rlpIhVgLgbJ2nNaA9MxSOsw7z0AaEfM_jxesleebajrp2QnlkNxE5ACC0AngS1-UWAKxNrOjZncnXVHmtQ_SRRGm3z61_TJbS67To_krQ99RvrDcxYwCw5VHuZVHaF9TKKaOQHU8da5gnr1Q26DwknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از داوید ایبانز:
🔺
🔻
لاوتارو مارتینز پلن B  بارسلونا در صورت شکست انتقال خولیان آلوارز است. هانسی فلیک و دکو از او خوششان می‌آید و این مهاجم آرژانتینی را زیر نظر دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/103277" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103276">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSvCLk13EK-Nq8x9R5fINvjlGp0Op_nN6BG7vad1mj5i8wsfovPkXcIw-ET44R-1T9kt2t934KyvHy-6uTW8YKHduQWDMKM0s5cMCrT3H8W64j4cP9jcrzI_Px70Tp60jVxWGY8pS0xoGk1Wxumg4kxP5nRXh7lj4RL-Nrw-CQIwKDOfj8fCV2ubj6b59UQdxk_j6dk9Hx_mYy0N3XHyZTz89gt_hLFwyMBOfDdhzob1bVMD5RClvuYpwSCzvSYdLbRnDojeBTm00jQqlrlsC-XsmEfmJrSQACDckIM-xRLzBuOA9QgMg8z7UCNqC5hdVDii-fyjD6TFo5QPNfhKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پریمیرلیگ در این تابستان بیشتر از مجموع چهار لیگ اصلی دیگر اروپا هزینه کرده است!
🇬🇧
پریمیرلیگ:
۲.۰۵ میلیارد یورو هزینه شده است.
🇫🇷
🇪🇸
🇮🇹
🇩🇪
لیگ 1 + لالیگا + سری آ + بوندسلیگا 2.047 میلیارد یورو خرج شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/103276" target="_blank">📅 19:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103275">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbdb454k3Y6hRxw9qfdOYK5x1-dGB6dhplrKsjLwigmao3r8AKGsdEM07eg34WjM_XbVZCutE4AwvjWrIxw9vwjMhwmQKfpZJ0KZv_MT8j5sPwBmii6oxw-18f6PV39r0iCR7RwYVfL2xQ7QihPYUNkOka7dT8aqbUV-72F6Zl0bx_YCng9rrpLpwawdV3UVPXSmkKgh6IKoHL2iB_eru7iMhyOcv1FL6vX6jUhcSx0pff9caH1rUmJWSeyDF61S4Bg9VmdQUiF7KMOfJO-jdX4OlX6NBKXH7TAD3pFs-7BfxajWFscPepwgdIpaphsS7wOI_fl_TySFBeW8Bnw-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین بازیش برای PSG تو فینال سوپرجام اروپا مقابل تیم سابقش استون ویلا خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/103275" target="_blank">📅 19:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103274">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8023c35480.mp4?token=Gb6-NBjbcW5sxHZ0wH4WFAOjpMQyylrjQOqsROm1o3xsmHW18NLaS2Rve2pSlCvcwviQvVERyuva7xofwgoWbBQHFcFNgvjyJMhftJrKC7dl_U2c_zB0O84HcZolgA_JXuLwRt8HuZAa8hyjeM8dtmF-bVtciLlSVzLp1QPjbKDdZbpHwARqKPfsFChY3xcmBqcUKFjMqHi8SWjTfjxERgPo4gvkPOB6HjynHcLt0Q4gmrQ4CPC8Vfds4oDmdheX7w4gDgLYbrKOjgpxj5OFybXolUrGnwkj_Rjy1H4cvrgsh0ulRNNvLgVJqBqWNUVDtY_qg6wyChS2gxTSnrnC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8023c35480.mp4?token=Gb6-NBjbcW5sxHZ0wH4WFAOjpMQyylrjQOqsROm1o3xsmHW18NLaS2Rve2pSlCvcwviQvVERyuva7xofwgoWbBQHFcFNgvjyJMhftJrKC7dl_U2c_zB0O84HcZolgA_JXuLwRt8HuZAa8hyjeM8dtmF-bVtciLlSVzLp1QPjbKDdZbpHwARqKPfsFChY3xcmBqcUKFjMqHi8SWjTfjxERgPo4gvkPOB6HjynHcLt0Q4gmrQ4CPC8Vfds4oDmdheX7w4gDgLYbrKOjgpxj5OFybXolUrGnwkj_Rjy1H4cvrgsh0ulRNNvLgVJqBqWNUVDtY_qg6wyChS2gxTSnrnC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار دوست پسر استر اکسپوزیتو تو اولین تمرینش با مورینیو
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/103274" target="_blank">📅 19:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103273">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5629191c63.mp4?token=Hskl6n4Asfk5cjAc2ygqzY5dD_Cv42sj-R95Lsr0_uU4aEeG3Injg-zX8N_e53_6whOSRO4NH_e3iyCvWjhTWSmi5_wI1sKF3SMUHTIndFwTh00ldV4GzAVoPOyVvUK48En-d1BYxQ_qLaJVB2FCjuX9_vJzQBuht0EuNL2jIw7hskDwJ5I-HiOwY1X68XttCg88QFewBuJySgDvzO7xK7s0nOf5i6aT_1InZDQhOdxLuyliXI2TapJIUqXmKgbbYSgldmx3TPmWGhkFAjYpd-8tXGs3wUtXuJPuPu3FBebfITN9_Tiojd1hXcMMiTRWel_Z4gAM3vUoorbaduXb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5629191c63.mp4?token=Hskl6n4Asfk5cjAc2ygqzY5dD_Cv42sj-R95Lsr0_uU4aEeG3Injg-zX8N_e53_6whOSRO4NH_e3iyCvWjhTWSmi5_wI1sKF3SMUHTIndFwTh00ldV4GzAVoPOyVvUK48En-d1BYxQ_qLaJVB2FCjuX9_vJzQBuht0EuNL2jIw7hskDwJ5I-HiOwY1X68XttCg88QFewBuJySgDvzO7xK7s0nOf5i6aT_1InZDQhOdxLuyliXI2TapJIUqXmKgbbYSgldmx3TPmWGhkFAjYpd-8tXGs3wUtXuJPuPu3FBebfITN9_Tiojd1hXcMMiTRWel_Z4gAM3vUoorbaduXb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی قصد داره از تمام خبرگزاری های آرژانتین به دلیل رعایت نکردن حریم خصوصی (تصاویر از مراسم پدرش) شکایت کنهو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/103273" target="_blank">📅 19:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103272">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ps_zI2c8kTDfObPE_jSlvNNbC1_IPDz9pRu_KF6f67SVFgWxNEjb7u_fo3htf_EnyczGDRwZygiFMyaRaXqPL2MA3ARnlrWsaxurRRu7WEMgCR_2uuf2CxU02AzkmCWluDpJ9OYL5lNS8TJ_YjK9Tyt-zhdBO8TqVN6myReJ4NiacnEFlhkgQRh53NeOVea9YVc6wvmEfSX82nbrYLyPP0sMW1r-88HegZE56sQBux07Kc10sS9ymQ28Ulh2d55slkEIwqlVF5RAZbC1F6pIx3aNEov0WXbfnGSRx9KuWOjfXpfb8xtjwyrLa30KyfqZLO_L0tEVoBX2mDiug5Fn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
علیرضا جهانبخش با عقد قراردادی به اکسلسیور هلند پیوست. باشگاه اکسلسیور فصل گذشته در رتبه سیزدهم لیگ هلند قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/103272" target="_blank">📅 19:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103271">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29f11cd214.mp4?token=WXIvnCArD9tz5Wc_jy7w4-V4owwfzwVlL2UH7Nw2Yit8ClZ4cmwLpiO0Twz6FAvNhvSrc-oUY2cVxJ4rabicXEqTjXfMRTT4cftJ48LLc2sT1UJIijTKK8OXSdCKj0fMyj1FwoF0K9mfzyGvptmkqVrP8KcZbhN1AmboluFcGg6-ibAZoL_Lr-OYYGvdJMoc2C3GFKpyCsKBRjFjstD-J5y6XK_POwLDfX2Ub4ejRFTmeXm2Ljpcz1v170Ev5qnPOnp_Eod1Xcjq-pD_7xsPJiEC6hbpLpoljblkHVAptD8LEwhHG9Xrr0M7pnOnS2hjkIVrYbtTv9lz6mcN9k8ckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29f11cd214.mp4?token=WXIvnCArD9tz5Wc_jy7w4-V4owwfzwVlL2UH7Nw2Yit8ClZ4cmwLpiO0Twz6FAvNhvSrc-oUY2cVxJ4rabicXEqTjXfMRTT4cftJ48LLc2sT1UJIijTKK8OXSdCKj0fMyj1FwoF0K9mfzyGvptmkqVrP8KcZbhN1AmboluFcGg6-ibAZoL_Lr-OYYGvdJMoc2C3GFKpyCsKBRjFjstD-J5y6XK_POwLDfX2Ub4ejRFTmeXm2Ljpcz1v170Ev5qnPOnp_Eod1Xcjq-pD_7xsPJiEC6hbpLpoljblkHVAptD8LEwhHG9Xrr0M7pnOnS2hjkIVrYbtTv9lz6mcN9k8ckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
یجوری پنالتی زد که فقط اینجوری میتونست جمعش کنه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/103271" target="_blank">📅 19:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103270">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c6dda8f2.mp4?token=RNPBvLvJqeUY4CY1U715j1wOsZ48sOvpJlQkv3MOrNRJnMQi-nY1u68V6yMjOigXlx1haJRewT-ujp9nrUr6bOX9CxkA_ER7fAJPaA1yuukZhL7Lap41-B3xPRs0g2qTUfZ1VFsi9IlFOzzW1w4-M5a5ZCWBShcOsFwoHgJv2qtkuHAqFQjDRBHBwIjihxoMaAkkZJPIybSx94B5VrfMver-ejzZQFjqpmTq1EEDPJFCCK_S9v2VJe_5F-VTICncF4Dx9kF_a7eVbQo_P8o8OKrk_kSitwDm-LAeDJ531M_tcPIIOS25t_0XRToeyjUpzJm428KUOC6TaPgZHkJCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c6dda8f2.mp4?token=RNPBvLvJqeUY4CY1U715j1wOsZ48sOvpJlQkv3MOrNRJnMQi-nY1u68V6yMjOigXlx1haJRewT-ujp9nrUr6bOX9CxkA_ER7fAJPaA1yuukZhL7Lap41-B3xPRs0g2qTUfZ1VFsi9IlFOzzW1w4-M5a5ZCWBShcOsFwoHgJv2qtkuHAqFQjDRBHBwIjihxoMaAkkZJPIybSx94B5VrfMver-ejzZQFjqpmTq1EEDPJFCCK_S9v2VJe_5F-VTICncF4Dx9kF_a7eVbQo_P8o8OKrk_kSitwDm-LAeDJ531M_tcPIIOS25t_0XRToeyjUpzJm428KUOC6TaPgZHkJCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کی باورش میشه رئال در 9 سال گذشته 300+ میلیون یورو هزینه کرده تا برای ایشون جانشین پیدا کنه ولی هنوز موفق نشده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/103270" target="_blank">📅 18:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMMSeY31QiV70_kah95PnX7v9BCO1nJWLPPVicdCuKMG2cdXH269Bn7QHD5Z_u432ICW7waPU2r9ZVRi5D4ww6iROr0qXBCfeI55E0VAoqGJ7__WiXPaxjFI96Tx196M3py9v4mCDWUVqbVT-GtzNyCnZl45cLWTg2Ieu5C2-YMUCDj9LuixTEgv1trJtfzughGos9GfOXvwpDSOGnSweOk3kTkMj7IjrE6MuyBOycu8gISThwTlkKSnWBw-ZMQ5xvEneyGZtxpXGNJRcZX3Rk8pr7goX5W14DUHbeTF5XTjgG1SSlw3EhAi0ymwqjrO3pH0ilvw_e-NW9-7BNdhJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
باشگاه‌های پریمیر لیگ که بیشترین حقوق رو به سرمربیان خودشون میدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/103269" target="_blank">📅 18:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103268">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qi3y7zv9TfXYcp_femcIhCvrWoSMeIKTMv4lWrDKdSBYk0TMIRU2vi3bS6vnrvleT5Zu4g0GSnluxCnshM-BpaDno6NTdYF-euvfaJp15zJzrFAJimadUUYF5qdJyz8471SWfKMugilZu_ToWl2mdLRkyceexuO8QfcTynLerLrbHHrLO6e-E_D9XOgLi0gwP75Xs1dURTGQ8HO4E5tYsiyV-WlvCc2-NxNgxO0TPJNgJTXOEki-pHhSUsyP4okvqCphHTa44Yym_ys5Q8pXVKsQLCTT_oSQe1UWUvH3oq8M5Lj26pEL-tSbQKyt_G-Bc9IXFfqJKkcIBimjm715tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
فقط یه فوتبالیِ واقعی میتونه هویت هر 6 تا کله کچل رو حدس بزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/103268" target="_blank">📅 18:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103267">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb1ladMD6vx3FvBocIDRt-xYkpCQuGV_5wc8rYZajA3hLFWZOkivtVpGBzIIdVG5Id-eASiqjI6HAre5OjR45dGD8L-R-EfJIZ_alLkY2T4KFN3Akg8cptjgRw3J3F4t_gOIIHUE3FQJKZ8q242SeMb9d_UoPMrMsxHJPRIrbPMGJom_f5HK1vjPcHwsRuTwF4R0knV8HXCHomrah_LL2UwlcIt5RK-sfqdCezpYFgUrIeZP3g87jBe_eoVqs1OL3wAoV5rv62laH2CZdhDjbMQF-ndDpELmRvkPEG2P4-YXT0Cb-i4T31yAxnvT8y0o90db7wWvxrMtJxR7GEQFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس کلی پول خرج کرده روی صورتش که نهایتا شبیه کینگ اومتیتی بشه :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/103267" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103266">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad5bakeJRG0vdgeFld3ePhCtBpGgZ5kCO-8PycamtwGmGY_3DIO6blz0UpqErnGvTvTSpgENEwZdJjHmhBraBJfR63EK6VYrZSLzm1SGP6yMcg08xVOz96ReOEzLYW_6nrYwffODTNRTfZmt1-_ARtRsHgrURQ_nInes7Udhu7jpAvyWIenI1RDUg_zZMFL8xR6W395CxrVBL4cYwfACN03f4RMMsb3DDzJdZNDcjmbJoAgFo1sZS1Lq6RfYQJVI47egiAJaDKgd6Pei5OkgKNpdcfDYDtMowo8SRjv_d6EUiJd6s94Uf8aLsbDfPS19yAUy9m3Jbdk4CYDVxRa2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
علیرضا جهانبخش با عقد قراردادی به اکسلسیور هلند پیوست. باشگاه اکسلسیور فصل گذشته در رتبه سیزدهم لیگ هلند قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/103266" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103265">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103265" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/Futball180TV/103265" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103264">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4A095Rrg12Trlge16LWGypGodoBVQk6bLSwlgyG5SHv1SXG4SbEEuGQ0pBdPb6Ymctulhq7IP1VEAnXM_MyGkiJL5I83cyUyzBeL4bY_AoVliWUBkp1bPyLAqi3m3LGqQr29AN6m9dEBzdUo9jdcAPu24Z-IOqO7UYUpVnj3IdGMkQcriARy_e1zBplnz1ahBUaLaYXRIPU7NsZpugIn5IPKzIVI4sBo_oEt4iNQ0-5i7GNPWYnaVqlFm6zvtTYffIoXd6fVXHcfII-ietuuCFJ60jTijViAeHFP0WXgX_4nrjo1IPT-ez04WGOsFImXstwApXTT5SydqMDju12WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/103264" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103262">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dikhEfWGcNBQKK15Ljy8mOBuFtf_PWTtL0HabWdZF0yp2jiVrZIJh-vVYvgR393_XqKtUl2KKYJuy67AldW7YzYu2aUqqTfT0CpMKgrQX9RNBTA7uMF46ayZdsK6jGBV-035dMOXuFcN86aZCEtOZx5un2FZCzn0hPEGOGIJcK08KQjbSLhPQjKje517gvcFXwmLcszGICRIwYDFB2mzTZF77gsSiA1TJah6c--vOKDzHjUBOsVhhbCt_4Sm1fxiaPNS5MyK9Hkl-giOj5UWvQR1PiwXX2YA_xoHV9vdbOSi5zQk0PVWFNnJTVEVpFyK6qkqYN07jWq1zbNyvVN4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/naF0kF_3kt7bLmkP4I1npCBTGCMnixGV-yRKrVqESbAqcDZFxbRM40JSDyL_YnPdKEOaQlwYH2IoDaV-j-mVY4PYkWGBbohts_QcmN3Ezooxv2X3q_SueoLiUgrpfuFRgs2Zvp3md1yL6XZ_LRrClZ-XwAa1KDvugs2SAfmxG7kNLCQI-Imex0NeMkCwN19rRHqWzUSbaLZeQWGVA3M0Jn-z-5JJ10dsDaBOQE6MYJcjdMb90zyE5IWYRa6iTNS79yN5bwHNrngJY-2UZXaccxt0JZQ_oOhDNF4zj7eCC9wW82OxzaOm-qeJNXEN8zono6PcsNO4HAzbh--w5SlqOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚪️
رونالدو تو آخرین قرارداد خودش با رئال مادرید، سالانه ۲۲ میلیون یورو خالص درآمد داشت. رونالدو ۳۰ میلیون یورو درخواست کرد، اما فلورنتینو پرز از ۲۵ میلیون یورو فراتر نرفت و رونالدو در نهایت جدا شد. وینیسیوس جونیور ۲۵ میلیون یورو درآمد داشت و پس از تهدید به ترک باشگاه، قراردادی ۳۱ میلیون یورویی امضا کرد. پرز بزرگترین بازیکن تاریخ رئال مادرید رو رد کرد، اما برای وینی جونیور استثنا قائل شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/103262" target="_blank">📅 17:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103259">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p94hdlgbH3wN7TMs6LjuaOfDjwp9cJguloqvSa9ZqQuzkWHJ8xzsSTVU6c3zOqR2geMeC8LrCE0ic0Q5hn4qJ09kOQxt0Ru_ixD14rTAvO7gMe9ZNTj2o5WjTLLpKei1udM_5T6lDHBtfrxZF_RQAjZZ-lvTn_bZ65zrQWBmhHBORUAVJBCH7Pwh-gNOYk9kxWGJ298n3XVyeJCkXIbL-YczwD6JA57DLQxoKKwzmvFd9Ewi-xllUfrCrN9zjN5J1LNh-fYCNuBN4inlKWvsWlB1_HMXXsEofsAEDp9KncfReJGtXRjcJwpYGzHIdLQi-l4y6WR2rrF-5ZJ0m-a_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTa8CNS1zIPI9QJ8vIEMhNYhrqB6EHigLRyCmIZsOJ5Nft8Uxc98oLEAGPyBeIakwCmHG3bzGIqQGN4icn29SOUboDy_EYlBAFV903BrdrqphBS5orz92gn-qEHFwZV1RDeO2G8xslfMWScgYfGE5QlcvUrbsn_bNAtslyfBDt-cFAazQCiM75Zq7ULezSE4-8JtlqBZqSCE_osgMEEjmh31HeGnj_uDJTS1ibcjma1d4Aw4mey6Iq4pCA4ZzbwiK9LY-uznONzkq-2OOituA_VSTZRHB6l10b-eEfdvQxTyvYxA5ecOPnb2Y1s-MvHg9A8hV2VEaMx3osY7UJKVaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c6e02cf3.mp4?token=GBaoLPg-M6YKakj3L9Bom5Sva1JY5WDO6hy4L9ObZaWRUJVID2uQIGnLiw3JcfhnZ6vHRt8XGya6BVkArwm3RHXjH7acw3l_jy5r7OH_EXWrfO6U8jvirWPIu5Hp23VJpOhLESrmN-3u4LE9YA963R5as6t-7p1rx1EWkb9AwIKzhosKgwWUaSPB_16a39P3XY5Yh55lpkqAlcYyDM31B1IBF3k3Y3IZCAz4abm2sobuwrrC2EsACgTR9l4quEwhpUU0TpF4JeXhS2yGPqjfkwkSkC4MQbXK-YS-54RJbdpEXXsbBJy6V1Ea02WqX2zMNMkswQ2x4gdvGhl_7AJigg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c6e02cf3.mp4?token=GBaoLPg-M6YKakj3L9Bom5Sva1JY5WDO6hy4L9ObZaWRUJVID2uQIGnLiw3JcfhnZ6vHRt8XGya6BVkArwm3RHXjH7acw3l_jy5r7OH_EXWrfO6U8jvirWPIu5Hp23VJpOhLESrmN-3u4LE9YA963R5as6t-7p1rx1EWkb9AwIKzhosKgwWUaSPB_16a39P3XY5Yh55lpkqAlcYyDM31B1IBF3k3Y3IZCAz4abm2sobuwrrC2EsACgTR9l4quEwhpUU0TpF4JeXhS2yGPqjfkwkSkC4MQbXK-YS-54RJbdpEXXsbBJy6V1Ea02WqX2zMNMkswQ2x4gdvGhl_7AJigg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید بانو جورجینا
🍑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/103259" target="_blank">📅 17:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103258">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZv37qQHlO6BJ0QWTyAKeuMGobjyZnCGn_r9MmGTfAuVgbW3ZPYPCLpzv9qbGM59HsDPK5ooJaL9jbGdYmDp5T_XNvRQ82fOnLBbCYEKjgSSD69p2uah9cOfX-fjJxb93H9OHDl2oH6xBuPqUIeZlEISKPl6qBl3sxc8LzfEHVemtQ3-GVYNw9GheO6-ZfSLNl56TPMWhPqtl61SobbeWaG2nU1yJ_fkqR7drZQj2Ztu1Mx88GVSNCVCQceYSpRkoTG2vK5ICvvZ9iXPn1LvMw1RbyrqndtKFcTg6T_GheJXWaJCSjkVA4YVRvcwdkY5wBQ6Jv7UExBI5Azmlwyl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
🇪🇸
رونی‌بردغجی بازیکن بارسلونا در تمرینات امروز دچار پارگی رباط صلیبی شده و فصل‌جدید را به طور کامل از دست می‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103258" target="_blank">📅 17:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103257">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9099fd2879.mp4?token=QrB7-6hK6jZ8i5IkmrUxnOSYNQhma6hbZVL8nfGbmUHELs-rHPnn8UQRhcPHv4CbvYlbDi8NtIqX2uxLiPVRLlb3NYoOxF87bH8zQfhImZkeUJnziBKB14cOPfB1_DQik-z0GOHeh3K75E971z-n_nd3gej1jTSHP5bIhGW1jV3vkTly6iQrb_xDjEL_9u27bxuzNAzrO6-7ZfSAaetvWqdckd-JZN-m6A88pQNG6pSuAvxVog5caKLVRhvb7p45kmLZFYjAg4aon_EhQ9PK9O3HCSfc_1yew_r1ZdRtDbnPnnOAV9_88ivghNrOktba8iFhqnh0VmXEEj0sk-8RFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9099fd2879.mp4?token=QrB7-6hK6jZ8i5IkmrUxnOSYNQhma6hbZVL8nfGbmUHELs-rHPnn8UQRhcPHv4CbvYlbDi8NtIqX2uxLiPVRLlb3NYoOxF87bH8zQfhImZkeUJnziBKB14cOPfB1_DQik-z0GOHeh3K75E971z-n_nd3gej1jTSHP5bIhGW1jV3vkTly6iQrb_xDjEL_9u27bxuzNAzrO6-7ZfSAaetvWqdckd-JZN-m6A88pQNG6pSuAvxVog5caKLVRhvb7p45kmLZFYjAg4aon_EhQ9PK9O3HCSfc_1yew_r1ZdRtDbnPnnOAV9_88ivghNrOktba8iFhqnh0VmXEEj0sk-8RFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
واکنش خبرنگار صداوسیما اژدهایی به کنایه‌های اخیری که عادل فردوسی‌پور به‌وی زده بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103257" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103256">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujd4YgIQ49WvHsIDgmwN6jKkqW_O4J8Na6hjF3jbOLYRdYy1PZmd2JKS1hHkY7oHCMDQHjbGCzqt7k5AVSNy9cRzwjsNMX3ANs96DzilqwzXtqtj47Tf0veqUonFj0uN77eByza9y92GtTMvAMFbenDpYcTsjBi0OBu0Uf50KTbUP1PLI6G9lazaUyhcqwT0PbUQXMoG4Us17z_zoMgaNUYxQvQzPqhBmIZd4IdUFUahyUZw13G8eFgEP35N44nzxDT1DJ583liYKn2ouD_BfotuxgpFXRJ1U9FD90dQzq7EHK_aq0I1M4nsSwo9GeShtds3DQNkaELa7cpdAYTtqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای نیوز:
جف بزوس در آستانه خریدبخش زیادی از سهام لیورپول قرار داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/103256" target="_blank">📅 16:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103255">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e349ee52.mp4?token=MDJqdGibwnP1jC8eMDUowMXpagneGa_C4qFTnnTvtYQGsK2P7g8BdbN371-EO07dmk4o9jUi8aVCV-TFnmHJ-EVwFxpVl0paooUcunUH8XkvIPVxgN_8c4iBuaEeYiBKu7Ii9Ic7g5IGgx8LVVXhRDOVTeR2hdfU5bW_7NhGSEPs4-Xld9e6F-XdSao77OBdfuF-Hkl5aSw8g_0bZ0MxcpRQ3U_S7tErvb7-8zmvne75im3wgcQC3LsEkR192sr7X9pSEugnpWaagEm-eWVK2IvJZPK14hdbflQgHZlhqLtk-ZTeOG6OqJVfz_nmnxtwJ1zPkgBkDWscA0nsl8-9uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e349ee52.mp4?token=MDJqdGibwnP1jC8eMDUowMXpagneGa_C4qFTnnTvtYQGsK2P7g8BdbN371-EO07dmk4o9jUi8aVCV-TFnmHJ-EVwFxpVl0paooUcunUH8XkvIPVxgN_8c4iBuaEeYiBKu7Ii9Ic7g5IGgx8LVVXhRDOVTeR2hdfU5bW_7NhGSEPs4-Xld9e6F-XdSao77OBdfuF-Hkl5aSw8g_0bZ0MxcpRQ3U_S7tErvb7-8zmvne75im3wgcQC3LsEkR192sr7X9pSEugnpWaagEm-eWVK2IvJZPK14hdbflQgHZlhqLtk-ZTeOG6OqJVfz_nmnxtwJ1zPkgBkDWscA0nsl8-9uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار به نکونام: زیاد تعریف نمی‌کنم شاید فردا مجبور باشم بکوبمت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103255" target="_blank">📅 16:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103254">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇪🇸
Xavi and Iniesta
🆚
Italy
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103254" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103253">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a709379c25.mp4?token=V3Fe51frv7DMPoCqc5Lsbi8waB6N8RLe7GRewYuGaIbIxSq9azlaNIUDaLvfpkXF-4Rh7FCLvotPpTEOavwOWK4Shsr94PfRHWq70s2LroOgAuCkpdr2VyRamt-Eq27Uaqw9sYYxLQ1o0Vhv5STb03KJDZxd8AXdi9SS3uAix7qJovyd-4eVhq77ALiJjIRkUZb0H8JbCM7D2i-5dfYcATRICoXdqrqwaKMnfbqv0PJtpmQYWrQgnOTm9MiMHatKcWjbgSoiJ6PhKU7vYrcZRI2MLNYgI35n8UwAs9pFDQxgl-C30XefignLltXdiQ6fFZHGByOANvOlWytVZbXG6EvjWJ5u6MPIYDAbhFfMTLKImgH950mJsEpnBIue1tCjwEqcaimdllE3691or8YC25hPHV2ypkNKtYhd7giMkWCeBZxnGJ8dpg2azQMtTkYWMaND7UuGz8QHH7DYUHdwVZ4EEQOXFZrw4QSDCfv42YtuSlTYDR1j4SL-1PAbtqQes4AiU0ZalXkmSolSexzh2FH-1L9muRyvOKltiIZg75jg1TtbK0YzbF7kKiZlEiSqbKIbIGMKpBRP8W_kz4I6h5ucUIHyoUbZO7NmfjzF4_pwTkM-ZzRXH-Hf-MaD_zGNxeqEaXV1UkXCmm6qSRurOKZjDeGaj5zsy0UMuD85614" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a709379c25.mp4?token=V3Fe51frv7DMPoCqc5Lsbi8waB6N8RLe7GRewYuGaIbIxSq9azlaNIUDaLvfpkXF-4Rh7FCLvotPpTEOavwOWK4Shsr94PfRHWq70s2LroOgAuCkpdr2VyRamt-Eq27Uaqw9sYYxLQ1o0Vhv5STb03KJDZxd8AXdi9SS3uAix7qJovyd-4eVhq77ALiJjIRkUZb0H8JbCM7D2i-5dfYcATRICoXdqrqwaKMnfbqv0PJtpmQYWrQgnOTm9MiMHatKcWjbgSoiJ6PhKU7vYrcZRI2MLNYgI35n8UwAs9pFDQxgl-C30XefignLltXdiQ6fFZHGByOANvOlWytVZbXG6EvjWJ5u6MPIYDAbhFfMTLKImgH950mJsEpnBIue1tCjwEqcaimdllE3691or8YC25hPHV2ypkNKtYhd7giMkWCeBZxnGJ8dpg2azQMtTkYWMaND7UuGz8QHH7DYUHdwVZ4EEQOXFZrw4QSDCfv42YtuSlTYDR1j4SL-1PAbtqQes4AiU0ZalXkmSolSexzh2FH-1L9muRyvOKltiIZg75jg1TtbK0YzbF7kKiZlEiSqbKIbIGMKpBRP8W_kz4I6h5ucUIHyoUbZO7NmfjzF4_pwTkM-ZzRXH-Hf-MaD_zGNxeqEaXV1UkXCmm6qSRurOKZjDeGaj5zsy0UMuD85614" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیمه‌نهایی UCL2012 و بازی جذاب بارسا - چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103253" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103252">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fbe5b387a.mp4?token=jgoWL3GUAHU-Bs9E0F4O-KOBEAsv2UD3uEmx4McvCG_bai0BAL8erdTPJGt1XChn8f-lxsFcebONqs8i1zfulqB6hySNMBGnWS8vk2ZCymoHz_mSX-8gjlYk1LExx4ksUQ9b3cyFSQegUBCnpMwO88HONOJfcpcopu3e-uku9cZ6NcsOfNVWk6bFFbWkNAvjdXkgwObPn_OxA0KOQh7Bir77_xvpZskgnswIJXEfLaKvt2pV14HOUa1uIvSbJh5QjdYlUTL4lnsT4MkOPd-JVZviasGmg1jdJVKdummoyCuTxRohecmsNXGQ74yckJSoJtP4cKew7ES2H92I3C4FEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fbe5b387a.mp4?token=jgoWL3GUAHU-Bs9E0F4O-KOBEAsv2UD3uEmx4McvCG_bai0BAL8erdTPJGt1XChn8f-lxsFcebONqs8i1zfulqB6hySNMBGnWS8vk2ZCymoHz_mSX-8gjlYk1LExx4ksUQ9b3cyFSQegUBCnpMwO88HONOJfcpcopu3e-uku9cZ6NcsOfNVWk6bFFbWkNAvjdXkgwObPn_OxA0KOQh7Bir77_xvpZskgnswIJXEfLaKvt2pV14HOUa1uIvSbJh5QjdYlUTL4lnsT4MkOPd-JVZviasGmg1jdJVKdummoyCuTxRohecmsNXGQ74yckJSoJtP4cKew7ES2H92I3C4FEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ادعای خنده‌دار وزیر ارتباطات: به اپراتورها هشدار دادم که هیچگونه ضریبی روی بسته‌های اینترنت قرار ندن و باهاشون برخورد میشه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103252" target="_blank">📅 15:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103251">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8870e38c3.mp4?token=DMxdd2iNKehJAlRfIrfQ5VtClWvcCwsb9WNo5jIDwnWC0-80YuSDQru6f2KvugCFgFpdSxplNU3px5BiAo9R_KcOZl6QIOsRyrIcXe5Lq9XOuEa1-RAEm8DhmEMhg6xX1c7qjeI18KRgV36uLgbUtZ9JHRrZWyKzgwkaHCSmLogTvAootPOKZFkIJH7eRUmSi8JTiJr9It-qbHQiB8uEsWAOZZAB1cBM8_227EpQcgXUMQmYRIQ_tHKcE_tsNCaBk-tnMVSYajlIFh8rAyksc5kkXZPdGvi2nJ48YL3MRL-_cZTkYe2h6ZbyQF1XQm83DbrRnz1aeM9YJR_q41w20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8870e38c3.mp4?token=DMxdd2iNKehJAlRfIrfQ5VtClWvcCwsb9WNo5jIDwnWC0-80YuSDQru6f2KvugCFgFpdSxplNU3px5BiAo9R_KcOZl6QIOsRyrIcXe5Lq9XOuEa1-RAEm8DhmEMhg6xX1c7qjeI18KRgV36uLgbUtZ9JHRrZWyKzgwkaHCSmLogTvAootPOKZFkIJH7eRUmSi8JTiJr9It-qbHQiB8uEsWAOZZAB1cBM8_227EpQcgXUMQmYRIQ_tHKcE_tsNCaBk-tnMVSYajlIFh8rAyksc5kkXZPdGvi2nJ48YL3MRL-_cZTkYe2h6ZbyQF1XQm83DbrRnz1aeM9YJR_q41w20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
امباپه، گولر، مورینیو! این مثلث رو قبلا جایی ندیده بودیم؟
👀
🤔
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103251" target="_blank">📅 14:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103250">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsDMaGuhulaJpVe8x3c-Ehm0DDaJbJAPpD7wuTBKYfoJJNUj25-rr0QmW-MaW2on0TRwLmGjr4FYatqP8JZgzJhsNYYPD2Dz0JYE3eBkpRqMfDZZEZe0IKrMG7ttDs5Z3bkRTngBr0drd9dd_3dRiSY4HRAGwj7B8WgqNk3A5oA19JZU3ugKSKwZgS9g02V-pbBroJeZFeknkd2FUsC69YwNTYrdQOeYAl-oYCqKaD7JKu7UpNJlGpxUNmLjFElmX7ECYrby-fGjovNaW46scz5_44TQEXfYetjo72QTFUh3Q3LkaFsXlqlpKSmvXHfJKN0b4uNkOcIutrBpGTNWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
پس از تشکیل تیم ماهیگیری باشگاه استقلال، تیم دوچرخه‌سواری استقلال نیز افتتاح شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103250" target="_blank">📅 14:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103249">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hrzau2RriuNtXxUEB_tsPFt9hn8uN_mXJM1GTJ99iJ6xKksn_h07ImIKrv-GQgyz1qtyBu5rO_asEj08cnJKt0Ozy6NfZaOP1tVzL9deLOIj5gIzzqVVjxOx_PIaZ2unlUULNXDEDlOR0tUILuuw8RUhuZHw_4-PssJOSNOZjbKCGD3MKGFRyhvEwChHZ6_fhyHqD6vTnJhYnAz-Dis_qUhr4pjL5xzhtZmGtzagfpNOrScJZ3Ynoz2tZkvV6qvSXDJ4cJtvKLhhyy7my8J3M8E4QQNuu-K9Vyi1FlW6YVgm8ENBVAj9OtNiBBwoj6PY4N7GjZ4F3s0ZiWbOP3UmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇫🇷
#فوووووری
از متئو مورتو: بارسا و پاریس برای فران‌تورس بر سر مبلغ ۵۰ میلیون یورو به توافق رسیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103249" target="_blank">📅 14:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103248">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103248" target="_blank">📅 14:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103247">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b442857f8c.mp4?token=FoEQtjiIsZQFXCj4kdj9E-D0kG1ZLg4AH8KLI1SuNn7ZHOL4UOklk0mAPJ3jEXFJhKnt5zWvOokWilbSRPHY2lSWqXUpcZ5RPsvltRGiInHHnETpbwac-HZ5r3e8fmyeg1RmgrI75HjSeLMU6-u5I23UaYktGqK7JdaCkEFAcsZYVIKsMiZCeMAfyOh5JSa2EF4LMDloQ2ORjvTMUfowFfQNhScLOUThPQOvrxA64ifh5xxpravkq9sNbKp5Tps9UMiBgfpaMC_YocTPW54ohgh8pJ-I-M_By5zowZpxzsnd-Qin8k-SlzQrkjhQv0vIb6bL2CcQLbvSaYFl4u7fnHBVVO96jhuOvVroM7T08Yp_le4TU35hBj2D9pEmaHQXss2_d0EMfRr0pGjUGD9Il4ZY9lRrb9HSkAtHaxUC2Y_oWrE1bz6xm6B8NyaJbdW3KoSF1wJSY2aibRhY3J60lA0lIsLjsoayV51o0NOkbQF64YJAF8JoMRy-674FaOe04nBzJIkJmsaFn2DfrUpWc5nj3lE3LocFrpI2HorPdtcmI6Ie2iDImqR_ZTaMuE_en5W_PjmzyKxQFq8hPL3wKuMfvjzfR0mSBrEblnGXhwcJrBsgSEeimHgtSIoAZlbnceBfenuC86ieszCc_1-6gkllRjOL_SE54Jbw3vETLao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b442857f8c.mp4?token=FoEQtjiIsZQFXCj4kdj9E-D0kG1ZLg4AH8KLI1SuNn7ZHOL4UOklk0mAPJ3jEXFJhKnt5zWvOokWilbSRPHY2lSWqXUpcZ5RPsvltRGiInHHnETpbwac-HZ5r3e8fmyeg1RmgrI75HjSeLMU6-u5I23UaYktGqK7JdaCkEFAcsZYVIKsMiZCeMAfyOh5JSa2EF4LMDloQ2ORjvTMUfowFfQNhScLOUThPQOvrxA64ifh5xxpravkq9sNbKp5Tps9UMiBgfpaMC_YocTPW54ohgh8pJ-I-M_By5zowZpxzsnd-Qin8k-SlzQrkjhQv0vIb6bL2CcQLbvSaYFl4u7fnHBVVO96jhuOvVroM7T08Yp_le4TU35hBj2D9pEmaHQXss2_d0EMfRr0pGjUGD9Il4ZY9lRrb9HSkAtHaxUC2Y_oWrE1bz6xm6B8NyaJbdW3KoSF1wJSY2aibRhY3J60lA0lIsLjsoayV51o0NOkbQF64YJAF8JoMRy-674FaOe04nBzJIkJmsaFn2DfrUpWc5nj3lE3LocFrpI2HorPdtcmI6Ie2iDImqR_ZTaMuE_en5W_PjmzyKxQFq8hPL3wKuMfvjzfR0mSBrEblnGXhwcJrBsgSEeimHgtSIoAZlbnceBfenuC86ieszCc_1-6gkllRjOL_SE54Jbw3vETLao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🐐
برخی از گل‌های کاشته تماشایی لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103247" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103245">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMUsRe6Ic5A_7YdWA5ukDllkeHokK2qZMrWcmvv-KjuncbJvQsxFvJT3XFeuxoOZ7S0lxvpkPQDRmx4K_UqDFplZPLb3fbU4-hMLrSUP69_axvnFhjRmpL_wohMkbtJ7VqgiYT7jJ0vSBifN7Kxof97_cmUzEAZFWBgWXIymo7YPPKjOY7o6XyStQoZ3XrRPefgxHJU9uDmM8v8ESMR9vS_HIVq65OV9Fi-3ZUgrv04s_6RbwjDC7JzkSNdXNqXmjNyPEtFebdYiSfDvMrWGL4MhX0RbgyMVWEZcR8GD-T-pUjDZ8lxlTNA_Zp1j3xD8kHUWRiL1XVXILP5qz9pExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkoK-Y6cWbpHwDwtCAnw5lkcvvxpzksRhtfiVoJl5h1obAFkRU55pm6KP0wgGcutswl5EWM791g-CtaXru2U-q3sov3blAAnmsFTrVOQbq5uokf-kDu2At-LZU-jQrd9dTwfesGL3LC-rb97OekonavzarFAkztNlgaDlGnfr4ld-ZTVjOjr0XJT5GLSIIA4_aSDY56fc9z2PIhaKyWIXtdO0uIzwLNI-6c4ZcmC8wGn5Q6ZV8CajLga_w5o_SGCEkvcfLrtm2E2Q6w4Yo9_ndhbTI7YYyP7SQdnhGmhKkbVDElDBjMQndqQ0qSirw9Ee7XbT8JxM-hihu7kDCQ-4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⚪️
تمرینات امروز رئال مادرید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103245" target="_blank">📅 13:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103244">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e730d0e84.mp4?token=KRhk3QuRth3dhVTrDrinJ06y34GAyNL3HqAXXDPXrTMZZw2Why7cVmDTp7CQjgLzw2PJ5za9x7AdIVlnZRgvk9ENH9Op37muUCwWaD9xK_Gb7py60NfPIw1JUrW5aeL-Oay4f2ooErXfI5w-2Nl-msoxh9J3nZvP132lBa3evYZkPQcMjED63-yga7l9uuzAQJwjMx3lhhT4nBDeq7-ASZ49S53Gnz6sdBbEa6YQOGP5lflJAbFJNX4Xgj3LhKHLSiDGpjFr9zBCkOg0Dsw3VRZ2mi8j1yad-dqwjRmuwzgK3YhYYGN81qS-ELouTg2hcs1yrS9hAUDolxAXrcRdrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e730d0e84.mp4?token=KRhk3QuRth3dhVTrDrinJ06y34GAyNL3HqAXXDPXrTMZZw2Why7cVmDTp7CQjgLzw2PJ5za9x7AdIVlnZRgvk9ENH9Op37muUCwWaD9xK_Gb7py60NfPIw1JUrW5aeL-Oay4f2ooErXfI5w-2Nl-msoxh9J3nZvP132lBa3evYZkPQcMjED63-yga7l9uuzAQJwjMx3lhhT4nBDeq7-ASZ49S53Gnz6sdBbEa6YQOGP5lflJAbFJNX4Xgj3LhKHLSiDGpjFr9zBCkOg0Dsw3VRZ2mi8j1yad-dqwjRmuwzgK3YhYYGN81qS-ELouTg2hcs1yrS9hAUDolxAXrcRdrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
با موسیالا هر غیرممکنی به راحتی ممکن میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103244" target="_blank">📅 13:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f008e3e11.mp4?token=k9AHxA4EiwqeIaN0q1kUbnpSNI1FkGeiXMKytEpzWxQUu2rnVbimKqbyKhpKw33FQ6bdErreJ3sUjKZSWfDW5EUw2Xonxk0oiC8XYkGumWAWsQjudF2JALxRsI1lHRkkTKVG39L8nisNSHGlR2G5VyikpZKC05oO6j-j-WNZv0uvPbdT6r8euePBpREKD4Nlh8GTvg8S2ca5WF8Q7c3AtssLb_74nkvyuiNavqdGePus0UWU6l-8WzOSD2sgU2cMdwQBxtocfWQhJS3dINqp-WOBbRFY0ulLJJ2cVEeaO4fqMy3OXLERlRl7LAZ42dc3ToavTp0RjV3TSy9tSVn9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f008e3e11.mp4?token=k9AHxA4EiwqeIaN0q1kUbnpSNI1FkGeiXMKytEpzWxQUu2rnVbimKqbyKhpKw33FQ6bdErreJ3sUjKZSWfDW5EUw2Xonxk0oiC8XYkGumWAWsQjudF2JALxRsI1lHRkkTKVG39L8nisNSHGlR2G5VyikpZKC05oO6j-j-WNZv0uvPbdT6r8euePBpREKD4Nlh8GTvg8S2ca5WF8Q7c3AtssLb_74nkvyuiNavqdGePus0UWU6l-8WzOSD2sgU2cMdwQBxtocfWQhJS3dINqp-WOBbRFY0ulLJJ2cVEeaO4fqMy3OXLERlRl7LAZ42dc3ToavTp0RjV3TSy9tSVn9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🤯
وقتی گواردیولا به جای بازی پاریس-بایرن، دسته سوم انگلیس رو نگاه کرد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103243" target="_blank">📅 13:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa14f9fec.mp4?token=VOWbcLBpUBW3wfD-3uFPapkO3g2qAWr1N248pfjnAzqRnuWRToNxWLLOmAXkYqPL0ILRaeEfeVkUHp-dTOEXUgZthIZ92M2sFGkbxu3ZUincPg6V9RVSp7ZNgX_2oQohh5TVVJY1cwxndTc0BtUW5DCbLJ1fc1ZWjIAXRQlMOXnvkNZ5gWkiAG0-InvltQz_hz-XZpAUdihCzpXOeuHzUch85euMs5yGKTqiCOlLRp3mdEDoMyB_MP4b8X5NB4lC6DS2f8ZHvjFculyWq1tc3okT_ahQj_KsBDHH7uhDOQSdd615NdtTLIekHG5F7bkUqnDaM6KCqNGrfpT0df_TClFr-WYBGIenV73DIrrZZNq8tRvHcFPpUOUxYjpf7RUxBTNKIEOm8m8TvHWTiB5KsnrWqzgMud17rRZHTrl1wRnI7jk8iiYkSVA3TVScG9xcJJ5o-dU576yesM6MTamrJ-S0yRqcP3o7q0zQbLh6WWgnp3KLwjID5N2BYeZd8hutPd-q3AiqvUYguTT04BMHwL7wiSrrvvSW0RnQ35dsE1Ogh9brYvb-HchXPR50jviaeuS8BhAjrn9ioKF2fHcU8qc4FguZdrq4kyCW_QaNJxgFGAancEUZf5m52Sm-7-JsVcW7wUNt-XS4L-sGUN3lVXgt8zwmKacJ3IpYYd20Jwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa14f9fec.mp4?token=VOWbcLBpUBW3wfD-3uFPapkO3g2qAWr1N248pfjnAzqRnuWRToNxWLLOmAXkYqPL0ILRaeEfeVkUHp-dTOEXUgZthIZ92M2sFGkbxu3ZUincPg6V9RVSp7ZNgX_2oQohh5TVVJY1cwxndTc0BtUW5DCbLJ1fc1ZWjIAXRQlMOXnvkNZ5gWkiAG0-InvltQz_hz-XZpAUdihCzpXOeuHzUch85euMs5yGKTqiCOlLRp3mdEDoMyB_MP4b8X5NB4lC6DS2f8ZHvjFculyWq1tc3okT_ahQj_KsBDHH7uhDOQSdd615NdtTLIekHG5F7bkUqnDaM6KCqNGrfpT0df_TClFr-WYBGIenV73DIrrZZNq8tRvHcFPpUOUxYjpf7RUxBTNKIEOm8m8TvHWTiB5KsnrWqzgMud17rRZHTrl1wRnI7jk8iiYkSVA3TVScG9xcJJ5o-dU576yesM6MTamrJ-S0yRqcP3o7q0zQbLh6WWgnp3KLwjID5N2BYeZd8hutPd-q3AiqvUYguTT04BMHwL7wiSrrvvSW0RnQ35dsE1Ogh9brYvb-HchXPR50jviaeuS8BhAjrn9ioKF2fHcU8qc4FguZdrq4kyCW_QaNJxgFGAancEUZf5m52Sm-7-JsVcW7wUNt-XS4L-sGUN3lVXgt8zwmKacJ3IpYYd20Jwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
برخی از سریع ترین گل های تاریخ فوتبال
⚽
🙌🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103242" target="_blank">📅 12:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103239">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ullyv4QXWUyfFa3N2kI0QHz5bqEXDc5yn-hNNplb_Xg2X1Q92gGY8NU0QMkyoNoaahj2wQEbgMvbjzvr_g-w3MlScGreHffFcwYEwkG4dgoR-ovElpym1j3X2wkwk761FWeyBCCMvu-ivrmjX08Sdy2kI3afKKJI-pIBkm15Zk97vq_M6yx7I0kCjQYoYhhLXWCi8RQZcjPxlvNX5IftYA67eX8QofZ7CYYAai170rI_vjyzoDGm-cPnzJo_cv5_KuZmB4DvWqVzqVBDjEuvpD_Hz4sreRd3j_9jXBVpaIw42IQQdBCiG9WBil1zLqmPZezCf-PiBqCTrQAksYGu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THhX7w6C0IjrubHycIgtdJYZ7q788K5-FKVV4NIrWxdRaPT0zLKtm9nMDqftareYjXpB7wRtFNdNF9AL99lFhiPoa2dFY1WlXkUjWfPACUSCRcocyk70GWQaG-D14xQ4rSAxJ0bKtqWuNq_s9D9B1PnG9GyglPxfZtkSu0NPDFUk3ppAIWXrDXfgwk2RNUKsYHq9XJvp266rp-EVCbQnli3f1bAPeklfNWfT3gOwC3ceQIYO8j1IIClNnMH7KqcFq7xpxSQNfZ3tQ1BehHoCmy1b7FXfsuJZia_FotDBP8mPwrTNCrUgQLHrEkNP453yQ_mEsJcjKCr5R6gOqrU3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAZk6WEXLpVMlO6vb-FRP-kPmNkm6HW16GDFOMybvRtu8NXXyUKhKpf33mdzR56KvABg_7EWL0z4USp2y7aMixxRpm7fOOLyiEzwnf1sfUtN5edwzEwxbTLgbtNoea1aToGS-olQnv-6CRMawtjXgL6HZ2QrhKUqyEL6k9IEVK7aOybOHtZ-b-WTPn2fMBl2O_zOhlJ3emGZrFFRAWwq1dzJ64GgwvuDv_zwhQHFP4AWKTRk3RZT9s5Bt6zIo5EutIHwTEPL7wKa2vl9y3HIwFkNjLs6M9rSxoyu7HjWe6oukGbsPOJJCuA2QHe9SAKitA1yH2hszzgwgIWM-orXMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امباپه ، کوناته و کوکوریا بعد از پشت سر گذاشتن تعطیلات تو تست پزشکی رئال شرکت کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103239" target="_blank">📅 12:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103238">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4861e800.mp4?token=M7bIZFWV6Z6zSkBEWjQkzlTrl4M3K5s-d9Hm6NFw14-rH2GaWNgqvtjzenEWj4U75ra2qlCCjV-liAToDRCtTuWqOf2YBd4UHAXTt5bEMwMkjPH80wOZxAPvKanHCpfwuWFrdOrrUSic0MNNpfaUeZQbOSeYTkuFnzc3eC8BeVSLpJIpsmVUt0oOH5cIa60mjiO9KIpolsNjOWAwmrhqnW6XS8PLVY66aA-nMS-gywj690Jl4lbpzr2U8Y3PpTQXG9iWvuLuoEK19mA6gsS-HoxQaQD_FQKJa-EmZhqawOcP4vtjpW4YNLwn-h53oyKoPKMOlnebx6tUtoAxeKB-Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4861e800.mp4?token=M7bIZFWV6Z6zSkBEWjQkzlTrl4M3K5s-d9Hm6NFw14-rH2GaWNgqvtjzenEWj4U75ra2qlCCjV-liAToDRCtTuWqOf2YBd4UHAXTt5bEMwMkjPH80wOZxAPvKanHCpfwuWFrdOrrUSic0MNNpfaUeZQbOSeYTkuFnzc3eC8BeVSLpJIpsmVUt0oOH5cIa60mjiO9KIpolsNjOWAwmrhqnW6XS8PLVY66aA-nMS-gywj690Jl4lbpzr2U8Y3PpTQXG9iWvuLuoEK19mA6gsS-HoxQaQD_FQKJa-EmZhqawOcP4vtjpW4YNLwn-h53oyKoPKMOlnebx6tUtoAxeKB-Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
علی‌فتح‌الله‌زاده: مسی بهم گفته منیرالحدادی بهترین بازیکنی است که با او همبازی بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103238" target="_blank">📅 12:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103237">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccEVuyVkBw2sqUZRLUOTifU7EAlLE6CWmALI07_nKwRRvxyIIG-GACsSxbY6UCNP5cQSq_TfEvT9YqtFJ4tBWLWRRRnUGYGX0L5RiMcCggW3bPQo_tT6Jm424j0khk6yVWdw4JeDIL_AE99AaLhFvWqoyeu4zwEs-gQnn0V930W0ATYenViI009G3mtrwUikWeQmWSGmSs4zdiuZwOkFGU5zha2whNBLPQgxG1cusTK399VE5cEdpNNAK1fDFbqJF48IjbCwvF_lmnwBycoJN4CBTmg5ZoTUtJi18oIH9Q8Jwd1TBBz0jhaUi6Rq04c85yY1vdL2BmNgcnnyTITWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
بن جیکوبز | یوفا، کونکاکاف و ای‌اف‌سی نامه‌ای مشترک به فیفا ارسال کردن و خواستار یک بازبینی مستقل دربارهٔ FIFA Forward Enterprise یا همون برنامه اینفانتینو برای فروش سهام جام جهانی شدن.
نامه که توسط چفرین، شیخ سلمان و مونتاگلیانی امضا شده تاکید میکنه که اعتماد به‌واسطهٔ فریب از بین رفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103237" target="_blank">📅 11:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103236">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82a19a1124.mp4?token=H7y7dmJuKNpMwTxe3PqJy22BqL5RIVOwsExTBA0H0N4N3HRxecm1czrmJ2ss02stxLKWK1BEn83hkitIa_nx2tC_qrYLDun5wDJ0sx2LLf6mW3siK7MKG_uSxroGj53wTyMIMeshRhDfcLrU-H2n1dNZ1NXtCmuNB94sp-KKSPNggic8EDKDSx0BwIHNBjR5Sao71YgAnBqbQfzXmWmQnt5elkcxaX-CTVHBSK0UvfMAxAVoGHOYSP9ORdb_aszPMwW22UJ6U32kvAdvm79DjNWkhSM3OwW-E3E4RgxvttRiOPcbH-knr1pBb-bOcmnbdtbO7g1FxGUzAYnTxrAI_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82a19a1124.mp4?token=H7y7dmJuKNpMwTxe3PqJy22BqL5RIVOwsExTBA0H0N4N3HRxecm1czrmJ2ss02stxLKWK1BEn83hkitIa_nx2tC_qrYLDun5wDJ0sx2LLf6mW3siK7MKG_uSxroGj53wTyMIMeshRhDfcLrU-H2n1dNZ1NXtCmuNB94sp-KKSPNggic8EDKDSx0BwIHNBjR5Sao71YgAnBqbQfzXmWmQnt5elkcxaX-CTVHBSK0UvfMAxAVoGHOYSP9ORdb_aszPMwW22UJ6U32kvAdvm79DjNWkhSM3OwW-E3E4RgxvttRiOPcbH-knr1pBb-bOcmnbdtbO7g1FxGUzAYnTxrAI_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
محبوبیت‌ دیدنی لئاندرو پاردس در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103236" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103235">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e57eb2f58.mp4?token=Q4Dgs0uH7P-4q6tYyaH0zzyBMJH9gWl3k5x4oy2zROMrQufRxB8EHIsQNNkk2deyXla1PfDsF8zIbjGihlwIR6vTPWCs_fc3lwga9-6rUKYXjsWbZ0mpIUWTwfPoRrkTyFHKtqipQzWrduoLt-rZ9OwVCnOWYsFmMD-jti_LpKPm3C-13ImY-ad8TeXao61j_CaWj9DJMWIsUBAkbAZNrjkqm6TchZn-C6Zafu1AI1IXgyvcZUhs9_QymiFOvFj992pNE5uR2Z9AGr_iFRGEzcJuegONzGGokOT-3zEmBGFzTZHBQAS_4U5UVUHcAwqeedcoMZqpKIP4guXCWqy2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e57eb2f58.mp4?token=Q4Dgs0uH7P-4q6tYyaH0zzyBMJH9gWl3k5x4oy2zROMrQufRxB8EHIsQNNkk2deyXla1PfDsF8zIbjGihlwIR6vTPWCs_fc3lwga9-6rUKYXjsWbZ0mpIUWTwfPoRrkTyFHKtqipQzWrduoLt-rZ9OwVCnOWYsFmMD-jti_LpKPm3C-13ImY-ad8TeXao61j_CaWj9DJMWIsUBAkbAZNrjkqm6TchZn-C6Zafu1AI1IXgyvcZUhs9_QymiFOvFj992pNE5uR2Z9AGr_iFRGEzcJuegONzGGokOT-3zEmBGFzTZHBQAS_4U5UVUHcAwqeedcoMZqpKIP4guXCWqy2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
🎙
داریوش: شجاعیان: شفر قبل دربی گفت اگر پنالتی شد فرشید بزند. رحمتی به منشا گفت بیرانوند تو را می‌شناسد و نذاشت پنالتی بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103235" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103234">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7df2b7b9.mp4?token=lxJOR1wCjuypSQDzeYzWlQD4BEhpIbInpwx4vCPoNM_ZDjghl0VjORLyuAu2DNX-29EBIswNp9030xf9UxqEIICgNo6wP8YbfxVOjm73GuCMB6a6RRUz2OJHV9yiwgTWbWRzqbFWKFvp_I0JPRntNRoraTFf71w8XK2hZUxqnSt-dbHgzKF1ztRGIfuYVGrdc4oFTo5GP2uSEjkZUiTAgDM8o4x6hJ9dZbLJ2_CDngl-w59u5Yi2L2Kv0NoeUAS65HPcU-qSomRVgTmrtJd4mlSE8q3v31hiIEv_PFKXAnaEq-rctwRbo2jsn_HxTUWvCLPd_ekkulLwIdUpoEClYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7df2b7b9.mp4?token=lxJOR1wCjuypSQDzeYzWlQD4BEhpIbInpwx4vCPoNM_ZDjghl0VjORLyuAu2DNX-29EBIswNp9030xf9UxqEIICgNo6wP8YbfxVOjm73GuCMB6a6RRUz2OJHV9yiwgTWbWRzqbFWKFvp_I0JPRntNRoraTFf71w8XK2hZUxqnSt-dbHgzKF1ztRGIfuYVGrdc4oFTo5GP2uSEjkZUiTAgDM8o4x6hJ9dZbLJ2_CDngl-w59u5Yi2L2Kv0NoeUAS65HPcU-qSomRVgTmrtJd4mlSE8q3v31hiIEv_PFKXAnaEq-rctwRbo2jsn_HxTUWvCLPd_ekkulLwIdUpoEClYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین‌بازی ضعیف دومفریس در‌ رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103234" target="_blank">📅 11:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103233">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7ItAT4X3scIY0vtTL5143FlnKR3muQrco1-1csXic5lbXbmERU9crH0x2H88538DeTHWbJa5JrObu65cCGePHqkanjK03F3T0Yg4vHw1Q3HK_bHlYBBzsa9uc4eCj9iBZ4ui6xc_Susaj72lOcECuQ5eD-bcuC657aaAW7GtJoomHlSGtqv9PbwhmNHxhH-JUk4plenCfIS_g-eg40RCZ6f6CLnRot7iPcWD1R9GAknEwbRNJWKWXjbh0qjgvu75OAQT5MaaB78xs-ftxijE_dJ8ELJwDta1maTDG0OqHQKvJLPmNsq3YaP0Q6_PDMWVaslv32H3bk8JR91VUkI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
5 سال پیش در چنین روزی؛ لیونل مسی اسطوره فوتبال در انتقالی پشم ریزون به PSG پیوست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103233" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103232">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuSQIds7s9NDbJQ9bcUpyRikGuHyGd7CsiwD_SFbF2zUcitDLXj9pXW7EFnvUu9nXml3bxddmRMygU2DR0pSPOvhZACjGkS4ISxEIzGroG6vzi4NDQZ82ZCe52RfeXnFDO1ewM7viOrY3DVfN-60_Ovxreo6zBjlewc6Ujy2J6NHMr08Cbnqg74Ig1i7RYNtiIy7QvgAylVNLBlJrErN4EHaEoIg6enmPNic7TL0v8avS11x5IP19MBgiz14G8o0hKjg5LBdJ7wk6LQ4eIzHv97tGkuDZK1rxDZUxIzDFdrdXE_XpeCfXWI1IhUJ0_CKMvMjsbXswy3WgU8mDAuKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
😳
جرارد رومرو خبرنگار بارسایی امروز کسخل شده سر صبح داره دوربین‌های سطح شهر مادرید رو بررسی میکنه تا ببینه آلوارز کی رد میشه و کجا قراره بره
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103232" target="_blank">📅 10:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103231">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtY0n_BXsEm3MvxevMgJ3mp8-suYPSXzUGTpyfCds3aVZPb0IPSjw4KCScUUN5whgibriOiTI9qbWNBa8g870IuaQvWBpG0M2o0TuBLw08y-X9IfIak5YX5YyMtJlRBO8TVYMWhJzhXr2jLnQ4PyPHqry6fGhijEBl4bTM9gRARC-sAxCO9zqpP5BkhnN-p3zGZ5l8Gq9uzVXXl049xz1SdPsPimLZwQqZUKXbIDGpd0rXVQKd-Ub_CbpCXvA32HZDzbzt4NAA2a8zIPc1syFMAeG1_p4qKympiMxZg7OKvHQuH-yJyPBnAWsIDl9I9IUZQk3ux1ZFVQ8h5cOwziVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: ایوب‌بوعدی ستاره تیم‌ملی مراکش با منچسترسیتی به توافق شخصی رسیده و مذاکرات با باشگاه لیل‌ در جریانه. بوعدی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103231" target="_blank">📅 10:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103230">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8c797d10.mp4?token=iBa6U1S9oWFnMhW3r5iCH8c32MlUcM1Kujj2kIR-hEv4lNYBPtwUj4Rcwo20wM_pUP0hQ7mPXwYGSk9axp7t3bdeza5Ub4n9B1KwX85tz4F_WPl5ShAWSM1MLjsZiRGm1ofe0NZt5pTx4JcgflK6MClvBjoS-IKhqQfo1jSwxv2IKgD49pHuuFitgKnwYXS93UnZ5feoapqiCQkCZCxXkgqu3KZiBLSxKwgyIpKnAImas9lfjQF2UXRKE-QSR3DD7bl3KAWVZ23JWnrJd3ARyB62Afsl_Fy0wLYVDrDHTnIP4v6EIeAi_N-ME3domRJFAYpcnvFRuG09a4_JSS4yebs5W9Q04WcyrsC9_3m9oyzzkc7bStLvJQaj9n07BYEekgIjsESSI4kXw00tahaf5sh1p_24rxnzvdNNAkqb0A-QWlMz-Lnf1qCeV1b_roR8rvbuihmiX3X9CCoKM1s_jdFdQN2uTOvzjNpF7WfuIHSAoXuoe2CaBmosBhNQAPXDrMXiPv8fbJx2_Cc_yaMyZcRLV0Oq1ugh-LRrF6orHnF8EpaTHYmtiwhcX71xtSsihZqC6Dv57iqiYtw-vU1cimDI1cEQhoOjqNFLgwIn1Bv4FVabtdxmgPcrgxcC1xRafyC8qjrORsyTGtu2TudAvDPwgywtXafcMcoycZbLPL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8c797d10.mp4?token=iBa6U1S9oWFnMhW3r5iCH8c32MlUcM1Kujj2kIR-hEv4lNYBPtwUj4Rcwo20wM_pUP0hQ7mPXwYGSk9axp7t3bdeza5Ub4n9B1KwX85tz4F_WPl5ShAWSM1MLjsZiRGm1ofe0NZt5pTx4JcgflK6MClvBjoS-IKhqQfo1jSwxv2IKgD49pHuuFitgKnwYXS93UnZ5feoapqiCQkCZCxXkgqu3KZiBLSxKwgyIpKnAImas9lfjQF2UXRKE-QSR3DD7bl3KAWVZ23JWnrJd3ARyB62Afsl_Fy0wLYVDrDHTnIP4v6EIeAi_N-ME3domRJFAYpcnvFRuG09a4_JSS4yebs5W9Q04WcyrsC9_3m9oyzzkc7bStLvJQaj9n07BYEekgIjsESSI4kXw00tahaf5sh1p_24rxnzvdNNAkqb0A-QWlMz-Lnf1qCeV1b_roR8rvbuihmiX3X9CCoKM1s_jdFdQN2uTOvzjNpF7WfuIHSAoXuoe2CaBmosBhNQAPXDrMXiPv8fbJx2_Cc_yaMyZcRLV0Oq1ugh-LRrF6orHnF8EpaTHYmtiwhcX71xtSsihZqC6Dv57iqiYtw-vU1cimDI1cEQhoOjqNFLgwIn1Bv4FVabtdxmgPcrgxcC1xRafyC8qjrORsyTGtu2TudAvDPwgywtXafcMcoycZbLPL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🏟️
آخرین وضعیت استادیوم آزادی تهران
✅
قرار است به‌جای دروازه‌هایی که به‌ صورت ثابت در دل چمن نصب می‌شدند، از تیر دروازه‌های سوکتی استفاده شود تا در مواقع لازم ؛ امکان نصب، تعویض سریع یا جمع‌آوری آن‌ها فراهم باشد. عمق محل نصب سوکت‌ها، بسته به مدل ، معمولاً حدود ۴۰ تا ۵۰ سانتی‌متر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103230" target="_blank">📅 10:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103229">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3E7Fx3MB35Ubim0LOVN2qzQ657VJORaiq2NL28S2mSZcB6xO_2-2eMTm33teP7iCcFtMwud5Qk_TMhRutXuU0ss0k60s_GrYFxEFrkdzhPcWPY7mQjjpV9tiytgySthTAUXFEA770FICvmihWhZVlaUhVDxLWH-z33214o-Giz20-LOcjSjCtxbYu79eWXkzstj-UidYaGiCjMPZQEpXn2DLElEhZiH2vTdy_ZfJ0K9rBzzBlaxiGRDzGbnwcp5fDtgInxEs3yWNd1zsyjpTGidhdgkuSyUS6CVChIIIBBI8AaT2UTaZRwix_APCneIM8gi33_2O-g3Uu5pVB7MFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
آرسنال برای فروش زوبیمندی خواستار دریافت رقم ۹۰ میلیون یورو شده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103229" target="_blank">📅 10:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103228">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=vhpzo2ugisCaitgO0mNS26O0p5KZprfFF0eFfClZilsHTAmJWeUjiGxg0j8Oed5-wjx08j4wZv66su__bISUC4OrLgEliPszL2LjSIhHxs-jofGcoCEMAVOn-dppm9dWTj1LDJs18wP_ITQnmAPinG4Kdt1rXJUwctjdkx9u0eztLm8lZOGByO-xFdBS187fRJXojG2PcmdfdTeB112NVe564HfRssZFtPNQPnQn_P6iRXWZYAZ1u2-s_mS_A-k9cXH8Hx24ybIOv5yWX8UPphJKWkHg52ti5S_ihjihrb_KVXAE272iDcp4OigIitx6Yxvve4XKSD6z4ZkuyBLHCWVzPuJg2UpWsO_ehGdfRnQJMXqD1Zwoo3IojMSNTZocS2MrSA7exO204xFr016bnSzRtwZM_XK3C8JOsrS7K2neku1fyDT3xpHRxzkb2WZH0WLupVdpl26Ky-pHEJ-_YgeGpYtFBX00KCeAIDdaSj_BvxRER6bpnsHkMtc1JCnJk9uRLa24loX8xUzGUTaDwFuwfUZNuKNOkmXmSLVKjTnDnxlARc6Le6uzvCR3gQ9CtkBo6kDQnEvZyICGE3mYSgPJFuOo-mOqpfuGV-RhJ0t8dQfXf43V1e4W0GLfd8wnKkIZdb_jEGensYqIB6PlFnK9X0G-K0rdi-fYhRk1Wso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=vhpzo2ugisCaitgO0mNS26O0p5KZprfFF0eFfClZilsHTAmJWeUjiGxg0j8Oed5-wjx08j4wZv66su__bISUC4OrLgEliPszL2LjSIhHxs-jofGcoCEMAVOn-dppm9dWTj1LDJs18wP_ITQnmAPinG4Kdt1rXJUwctjdkx9u0eztLm8lZOGByO-xFdBS187fRJXojG2PcmdfdTeB112NVe564HfRssZFtPNQPnQn_P6iRXWZYAZ1u2-s_mS_A-k9cXH8Hx24ybIOv5yWX8UPphJKWkHg52ti5S_ihjihrb_KVXAE272iDcp4OigIitx6Yxvve4XKSD6z4ZkuyBLHCWVzPuJg2UpWsO_ehGdfRnQJMXqD1Zwoo3IojMSNTZocS2MrSA7exO204xFr016bnSzRtwZM_XK3C8JOsrS7K2neku1fyDT3xpHRxzkb2WZH0WLupVdpl26Ky-pHEJ-_YgeGpYtFBX00KCeAIDdaSj_BvxRER6bpnsHkMtc1JCnJk9uRLa24loX8xUzGUTaDwFuwfUZNuKNOkmXmSLVKjTnDnxlARc6Le6uzvCR3gQ9CtkBo6kDQnEvZyICGE3mYSgPJFuOo-mOqpfuGV-RhJ0t8dQfXf43V1e4W0GLfd8wnKkIZdb_jEGensYqIB6PlFnK9X0G-K0rdi-fYhRk1Wso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
شلیک‌های سهمگین سوبوسلای ستاره لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103228" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103227">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103227" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103227" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103226">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=TEsoMX3TDRfib-PIhcpq58pgX30KPLKeuNeMv1BObFm-FNpulD3wFZiAIrUPkjY_YT0W4V-dHmyOpkp4ny086GZBXrdvFU6kwyTlvlvgDg97dskg_efNUYXKbSVcT84WoGoBfIWnmlt16ddihPL8KpiERlEnX6LEynZHLAMCP190YgpYGNQncrgR_RpsD_DYcw3Vb0rMuc0VqDceO5TfT-0jLFw_iDgwB-a2MsMQlYw8fGNPHzXnkVn7rNpf7uxy0o763UcTBCREmMWzRl39gK5n6LAsd1DVyR1HXUDvqouvPyeQvpI1bSD1wlofNumoci8tmqgsta8Yar6rbEANUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=TEsoMX3TDRfib-PIhcpq58pgX30KPLKeuNeMv1BObFm-FNpulD3wFZiAIrUPkjY_YT0W4V-dHmyOpkp4ny086GZBXrdvFU6kwyTlvlvgDg97dskg_efNUYXKbSVcT84WoGoBfIWnmlt16ddihPL8KpiERlEnX6LEynZHLAMCP190YgpYGNQncrgR_RpsD_DYcw3Vb0rMuc0VqDceO5TfT-0jLFw_iDgwB-a2MsMQlYw8fGNPHzXnkVn7rNpf7uxy0o763UcTBCREmMWzRl39gK5n6LAsd1DVyR1HXUDvqouvPyeQvpI1bSD1wlofNumoci8tmqgsta8Yar6rbEANUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103226" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103225">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFB7tePvSF6qybrm7kN3g3d9m6Ibv_fMI4SHK9RkWyHLIXVMIyBA_tjCHYVS1-RGJHUZLQO6reYvAikHfAAcO__A9pGvo_QydvUvGbnZO_gAEmMa-P1gtBSuGIFsd_a8DJhL__jJ1oSCa1BFZ7kEZBPEvXm3cvEmPwr_JgC7uoz7lQQC0H4BA3jXpjBYKPqSCBIxD2ydx-gK04jGwhgA1Hq9tNGAsmQSsrt6VuuUjUldcsEopL1ZAmuyMzWwFIXsrORvpIMAa8MNUSgtGJzd4OQfzSn3F4HjXeh860cfRCaGgFm7jaB3rYpmdpl9DpAm3NjU6X2JV1jAFL23xHMEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
مقایسه آمار فرنکی‌دی‌یونگ و رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103225" target="_blank">📅 09:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103224">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJIHAdALsxGa0XN7yYoyXOgN4gf3482RX4drsrHk0V36suknCXaF0sHRdldegRCfeBGaRJGVHBCyU4EbnlUK352L5fA4A0FDbF-iBOzV6j-G5gz7Qstju9AxOvLWz6Em-_PjhZwsUIlcdpkrEzLlkd8DPjuq9r7WEuOgYFD_qg6EzmCPSJn1m0Qh1slx9ogeVTxzguVLYDjxRxDI_pk_kb4LGM2NMkdezw9ebh4lVikRiDXuxrYtWzB4bZ4zIPSv0m1W0c8R4XXWgBEWlfRRJQPG-ERYh5GAnCrVLt_sxdgJ8XDH4oyimNczfxS0CM0C6Kr5rO3D6HRtJ5EDW_aEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط هجومی فصل‌آینده الکلاسیکو
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103224" target="_blank">📅 09:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103223">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👀
🔥
برخی از گل‌های چیپ تاریخی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103223" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103222">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsRerGv4jJNIx6hPFSKOQn1LjXqWqTJWHA40fFFJn3bSI--rdlNFkNlXVRaLtG5A8I99ZOOsTNR3riLpNoBzPxyEPQmI0ZHGKaFKBJ9sLGA7WYlmbm4-vBSX_BCSE_JgAAy_SLZc9oxt8aR7Hi29dBqpaXyi3dPbp0K3s17CwxWd6jxGT0uLmfosqhvFtBT3r_uS4Wgbtm8sT_GLWMmZwk_JaF6UMvjWC6h3-LwHg8H9s-xOjzpsrkocTHkNA7N6x-x7529_p1gcn6q0chdj0V7VWr-JAeePgpTUrtIa5DYOZ9xW8JiJERqd4P383qUtWaWMB2Rx-4ER11-JS48bPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇩🇪
نشریه‌تایمز انگلیس: هری‌کین بزودی قرارداد خود را با بایرن‌مونیخ تا ۲۰۲۹ تمدید میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103222" target="_blank">📅 08:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103221">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-DufT3vobUjBpoPYXv--BtLkR111_4s6l_7sYjqHZHb2xFBQZTnxaRt1LBwKSVS4vc8UudAp1oP_pNaVMKCC-H-SZG6D56m-fpGN00YDaIW3Dp7JvCevRGKemlGf-ON_xnySu1vuolfW_Xvs6qLyF3tnXx4hCX2a0fGRHPnLOfWfGA1vHuwIwH675Q28acRlxZPVkkxkL3OogGNgcFSgwYbVCCP1Z7gvncY4gbd_8E_b9zI2mp-Tx9Tm-EhRq_qOmdYtbR9pnTekHvp5SjJwIGxKYMX4XJBtFLaZT4z0OSStbcR2TUHDG8oD2Hlm82qAV65Te6Bei96iIDljGO1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
#فوووووری
از رومانو: اندریک خواهان موندن در رئال‌مادرید شده. از طرفی استون‌ویلا و رم برای جذب این بازیکن اقدام کردن و مشخص نیست که رئال راضی به قرض دادن مجدد این بازیکن میشه یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/103221" target="_blank">📅 01:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103220">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ5e6mY3QeFnU8bn75Vz1AOPXETzA0W4REzzX_NVRtiXnztIVE34zJW34hWQyBA551GY57B_ANfHACi2Q3EtzH7NfGtCTyeFsRpPRuDKxMIM5ZRyuZ_swns9VqRB1GBjeM5wMatoqslXTLTM4-i1t8jN2AO6ZKfKQzrv1QGezWuuZdCzKeiAJEzJQRcAaBwybFsfeJT5G5k1ljbRy-yFUp8lhpzI1-o_D3Tjx3sp_llT9UC195DVYcnZ-nGZK2LU4pGXGCXwJGu_9s_zQnXEesph8y_5vMbbKYudQZuVEAGJ2_sEXeJQ_4wt41Vc6t7tqH3kt89Se9OtNq13KWci-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: کونده مدافع تیم‌ملی فرانسه و بارسلونا از یک تیم در لیگ‌برتر انگلیس پیشنهاد خوبی دریافت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/103220" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103219">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
👀
⚠️
حمله تُند و بی سابقه محمود فکری به عادل فردوسی پور: زورت برسه همه رو لِه می کنی! نرسه هم دستشون رو می بوسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/103219" target="_blank">📅 01:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103218">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🎙
‼️
📰
علیرضا دبیر: شبکه به‌دردنخور، آدم‌کش، جاسوس و کثافتِ اینترنشنال! من محکم تا تهش هستم؛ مسئولین هم نترسن، بزنن، بترکوننشون، به مردم بشناسونن این کثافت‌ها رو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/103218" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103217">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRGFoCv33K6U8k0BUOXyNF8TSZwcHXRFoe01aLuMczWjS2tu1viAa1oQ7HfduyUyq1pckVhcus7_kJB90kEkrYUA8wKwNhmHtl-u_JxUPi-oLCN5-ePVpixaUgfwSXPZiX27Iuar4KAvsdwMdQLyIDuKnaJGAC2MSiAXE2OG9BS6zRcvXH1XPn9jlZ15CFvoi1kzTLMxuJ_BAAymI7yS5QH1g9mqG-M6KQQYCiGlkksCDhvFkea4FWW1b603bCZ05AWyO27ZKk-aBpo6SHhkz16AG04G7t5Buy5X-3fH6ewwDeplNClFDJGaoPOGYl7fkXD1ILKQOSlIAy9S7y_W3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇹
برنامه فصل‌آینده مسابقات کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/103217" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103213">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
⭕️
🇮🇷
سپاه پاسداران یک کشتی در تنگه هرمز را با موشک هدف قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/103213" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103212">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQWLkqz7EV_AuSkxfE7KA07srHfLPzUrIZNrTWAyof2pLxGvGN5-4DI1Dlf5YKcZZ4FcNiyyASY3KfGuQe_xHYXZpCnqpKrO20on_UeFwVnEQUkQkqdM68le5wvYSogTnaxzgEHK8J1nC6HmRi-TexdQCoVYNg0f1AZ2mQbuAwXM_FaR8MSawoFAHtNGFhbP441Hk3XhsN8oHF0pze5XEoPVPFAd2ubcxCBh2yVws39Pg6ZWo2QTRIW3N0kyyd3op1y9nBb0MRmFfUOhgxCOLQBVnQkMrHlAWAT6wWHZFP_yOog-VdwyM3mu0ogRC1U6f8P5uSpD-i7kqXHHmQu6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از گستون‌ایدول: کریستین رومرو مدافع آرژانتین به اتلتیکومادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/103212" target="_blank">📅 00:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103211">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
گستون‌ایدول:
🔻
بارسلونا به خولیان قول داده بعد از صحبت او با مدیران تمام تلاششو می‌کنه و پیشنهاد مالی چشمگیری به اتلتیکو میدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/103211" target="_blank">📅 00:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103210">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJfbmyBQL1VEDvB0RDB6_TzG_NNPjtiwc2z2tfO7I_n2pWC18_QTGLWBtlJBarDBxopMeIKtrcSZkk7bkjVfmA0Mut1FLdGKZ2iwWuH7T5VSH6mv6m_YrVUIN24FmWmPYoC6L2HPwUPPg0p0rPLstNRAdMhrha1YvlZlxTl9NqmMFJ38pMc_0RcGDfdV9nxFfl1xTvW3VUSWf22jDdTO_IkzNmdKBYuSG0A9eiLEqOs6RjqWlGPBu8sf4qizijGu2g1HG3Xu02clsHe_syyPffs2Z-G0DIF29c-LAcUYZEFm5vHYsrh6WCDvISuLwFrhxCA_o5sSPzHm1bbzLR4jsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
و
#رسمیییییی
: داروین نونیز با عقد قراردادی به ترابوزان‌اسپور پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/103210" target="_blank">📅 00:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103209">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/103209" target="_blank">📅 23:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103208">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103208" target="_blank">📅 23:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103207">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/103207" target="_blank">📅 23:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103206">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffgL7QWJrRks1NcfbKoC6mHDzJn93kCAubPCIEBbttNT5q83w01mYct1WSbJwZhABsUG-4_60wraS7AEy3_JuiBAqgXRT8YciBuKOo0r6SprX5cwbtV2LgxnutcIaHfTWsqxFky2R6_IzQDKxrEAFDtYdUftXau2pLQLDr-FQTHXVxR67HjyamgWBdzX8A9FP5tI16TuAQWtLGWm4PVHT1IvMN4nvvfYYt-hXt3RP2ONRqKTBVZaibeiJFKiXLcIA1eOYa3_-CwDQnPFn-3dUq36nHq7RcgohdfnCb1HUkSdU4Lrgo-jyu_nxVrLGkM3eGxuM06-BK3BbFUFXDnf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری
از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/103206" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103205">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IzLrI6t4VA5eh6FpQmpCIybmwlS-1VB4MYB8GX248pTirVrfQc7FH_7rIGoNZ5QeJxrAne3t0ItjLSrrkUihN7O11FC2a4G3Df2hTWNhlYxqz3TMplynIGjH_Wqhhjtno6HTs77cSqGPLtFC_2ONz_-4qWQkDxeVuAMWgmPbNh36heSGq7gpujX8Z6AAAqWaNvjmz3-FmyOYfBrl3GH7SifC_if8L9yFSNyiEv6rtV1J9r8A2_5DNkv70YjVeKl2YXmGFdFf7FuxWwjjdV__wCJmfUcxBg2Dm_jGjHlLWrz2KkTnpmKq5cycT6XqMS730qWkiPQSJMJ9Lr6qkLCxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
باشگاه بارسلونا در اقدامی‌جالب نام رابرت لواندوفسکی رو‌ در لیست اساطیر تاریخ کاتالان‌ها قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103205" target="_blank">📅 23:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103204">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mABBr1vIea-hg318ogCBL0_BC-tWMjblBYjYKT_bfdBN4_DwaWwNCHERfz7vWtCKHCNU9AcdnAi3S6-kE5P0G6XT7nqVH1qdPuHot0vRDt38SEp6PNCq1tHNXMeXvPK77XtC-AEqW2GIZxU-FyrRSGGcDdaAjG56kB_muGBigIK24k6mjO2JpAGA3eCfDhpEwcb_mHcJ05QHvc2s057zhu4G24cIXk7BlR8sfr8KRRTVbZjErwl4HWyb0jYFdlpu6poV56Sa-HUlgvfGiLTmjTnd7-0aiXuqskLLgG-csHMkPjiZcbOo-U12CntuJqsDWvp06d-yMLXgOskdFu7NlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دفاع وسطای لیورپول در فصل 2026/27:
🇳🇱
ویرجیل فن دایک — قد 195 سانتی‌متر
🇫🇷
جرمی ژاکه — قد 188 سانتی‌متر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جو گومز — قد 188 سانتی‌متر
🇮🇹
جیوانی لئونی — قد 196 سانتی‌متر
🇺🇾
رونالد آرائوخو — قد 191 سانتی‌متر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103204" target="_blank">📅 23:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103203">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0zI79B5nl5xozx4cnbeDh2xzBsF0mX0ARyJBoaeg5o1J0OXoTvFztdeCVcPTEFqYFAcCd3dPDDojBrMTzaXYR_hetCuL3C2wSWw-Pv91ycOS4WKU-XlFabtUAXYxQ_ST_xX_4-rMQ5KWQ_flyaGtdjv73WPfBoJJdHzx6ssXUlypUgs02GzP9l8Hrlp1YNa6IQH-BvI1Jgmv4Hc7Wp3eCHn0bUOhkf0jhTS_dbxOKng5ikSKePZjeJQMS9LQg071jDM_cLrcU4HhgwF9AlLfM1-QwqplV08pBs-C154taqs0b6ma04k-2qwQ7GRULMrb4ErKA6UsjhnSxsN2L0ubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
پیشبینی هوش مصنوعی از جدول فصل بعد پرمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103203" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103202">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7WN7_mzi3bb56SdbxVk1AhKhFepbCLtKHN6K0XlvUoMxelygf6ueM9s1po0heUau1JeOch4WS6owqiaWpaCrx72YK7BU9FdZb-yiZ4cftrwKqsF8UosNI3m3iJMd-Bca_rI6mSQMR3f4ld_3m4YUK3cZ3H3W5n-JGpy9_VVoiBiRBsrMISAn3v1YjVTsCvbo_muATr9s7ltQafPziJQkuoBxoCd7owwQnN7FlKMQ2XGSLWglPxgr0ssBBURFu4JzvSvEaKa0vGu16RuEprll1Ihp7CjnPG012BtlvfEqn9I1C3D7cJ_5CPmf_amEdtGG7i6L-dqcy99gJdDKixlKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103202" target="_blank">📅 22:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103201">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_y6FbsRXxjyLpz-rHLoOD1PdWglJJnS1Ktbjw0ygdgSdNR1en6lvyT3q3Lwv08uzD_DiRbwzk3GnQ1sVmyKJuEIqs5JAkrLBSZdzxslqwjqVWR97eOAeuSIDpnwj9jMigMo0R3fzE-xw3PN95p2sl-tLJh99u2LTJ5f1rmc5FjZFH6E3QuwncxcmBp25HnS2H2ppKV5l_CxszqrfwFpexdrmPZd-AjUpmrb0DFhUoUozcU31Si7TLMzpFeJA6K_Io6UD4aLlXqSk2t3vgqqeYqxrYoJ8CdJyUJ_l3kBaDJ59RGQFHanG0F6xNxk1CFruFxwywaccMM7QxYaIcTfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103201" target="_blank">📅 22:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103200">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=jkqsHvtRzVpv4zUuxDhIyafaeE6tZFjKLrM98zE2xsRK9_1xhK3t0abaXjQGlifXzRe_5VmgT6eZKnVy7QLMmaIhp6a9jNyczgAWj9DuruV_ZHFr7jJcgAkyt5imxGSKohLUKew1FgdfQCqqxOWyqPj7sDQd5BPLsBQpv3FAlrgISFuCouGvE0HdqpQ6jT0gaDdcTXbw_BTJi1VjtnnxYbS8V71yTQdmsjHZfVJlkxb0WCuIKppiAI1cJdftwylZ3J3JMepdZhufPOQXzQLBD7dj7s4KoCrKdosg1mBWSe_F0o0N8Jbk8R0Qlf5JLX6BjowzwMtRZ1tJSozDwLNtwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=jkqsHvtRzVpv4zUuxDhIyafaeE6tZFjKLrM98zE2xsRK9_1xhK3t0abaXjQGlifXzRe_5VmgT6eZKnVy7QLMmaIhp6a9jNyczgAWj9DuruV_ZHFr7jJcgAkyt5imxGSKohLUKew1FgdfQCqqxOWyqPj7sDQd5BPLsBQpv3FAlrgISFuCouGvE0HdqpQ6jT0gaDdcTXbw_BTJi1VjtnnxYbS8V71yTQdmsjHZfVJlkxb0WCuIKppiAI1cJdftwylZ3J3JMepdZhufPOQXzQLBD7dj7s4KoCrKdosg1mBWSe_F0o0N8Jbk8R0Qlf5JLX6BjowzwMtRZ1tJSozDwLNtwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😳
😳
😂
😂
کوروش اژدهاکش بازیکن جوان پرسپولیس: می گویند اجداد ما اژدهاکش بوده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103200" target="_blank">📅 22:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103199">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psrqAVLuV0XCwiHieNBU0Xur_WZkuLUTCWyW7tTpgnr0Jmj10iSLaz_Eb98Xsu8sW97HVstymXLIhAyZDPF63FSONKq3ZOMgkKj9SuW06ehgVkj0weXxAO02J3AkttUDbb4YPP5lJcJebrYziJvSnEvVXW_p_LHod4PS2euGOxCZJpUhHjD4GIJwsHJ7mWGoaC_Euj_lh38hAINSFt_sBZWU_WcVcUeH9wqXtcIMPEzG2cH4sskgK2a5hrS8cH7GqBR0uitPBmgeS9CXZjzh7jmrb4Lc8-ZX3kPEq3ht3lvprq35VU7aQOidahfiTcWUomeg0RhD_E5ZXBgYjLIe1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
‼️
درصد شانس قهرمانی در چمپیونزلیگ فصل بعد تو سایت های شرط بندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103199" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103196">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnIlFkT1MDWXVx2Cz72Y2CZox_Nw2kcrE2MKN3A05tEbespGhS-xf9iVXYX6QKvo0iU-IytCMoe7Ary3uaBNCBdV7zTZmZcoMCqo9c3vJWNJjG9OAB8rWmjbnjWKhlrj_csOEmcpn081DowiREHMmwUsp_OK_l_KliD5cTKGNIu_NVyXoHvasrrxhLiPde4-RWiCb8zrmXjLtZ4d2552GHZ8Vknwtpg177OD_G0_7k13L_O0FvwX8RDhiSoqBAYxL1eZ6jv8xoINxJ0jdJgsdubVlLoXLKuj18PXII1Dhol9mcCIemW0o6jnqMohg9cjshrCCrLp4kXaPYd9XLSqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NjO2O0HA5esH-bRzwVze1aFVeduzhP6FbGBRaXq3YzmWa6SPUuStfSqJ68lgK8Z99CeSrf5F7J__Bc4BCF14BT_a7Vwwk-pYAp0wiBOy9OrKcvvQ9v1jHPVjzLiPekElMAETwI_iqIUtsa2zIS8nM8ZEsBxCiTyFcHtF02qNAIH1sRcJdMb1DZAF4aqX3IeKB2firaRxNyeZhe_Jpt7hli5JJVOHxSABBjlwN5r2SM22qwwU2WCCkkU2DwjOy61Le3B4jF5imZWsBf_FN9fewHnTVnTw3HL05p1SXq8s6_j51kpbPgmZ_Derm6RLrq9lyrp92YDvJvm_sHv_NVITeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=DxVjL0-gxkMDUBGO1g-pOyETwuF32at5AQUojB49CBEYJukWxC1rC8MEbzMG6W-pUbDlhyPyxzMflqcOudzuyhkmu9-_4KiEuy0slzvLj8HHNVCZ0we4xZzpTH2qrw4Oz_STsIYYnnaOYwAblXWxLo1JKap9GKb-R27FKhJg1mYpCXhKQndNMsiI_zxl_ggm_78yIqilxNQLtTnT8OUa7YFMeZ0r5TnJM-0xMGZAmisz-5qgaTaJUXUA0cOjOy2GpuGoz8UeCz7xbKNHvzBDqx7ury7pQk99k6r_2SsVkux5NimSkL0P_87tosAieDohABpA4-Daq_Ee0GIK6rWj7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=DxVjL0-gxkMDUBGO1g-pOyETwuF32at5AQUojB49CBEYJukWxC1rC8MEbzMG6W-pUbDlhyPyxzMflqcOudzuyhkmu9-_4KiEuy0slzvLj8HHNVCZ0we4xZzpTH2qrw4Oz_STsIYYnnaOYwAblXWxLo1JKap9GKb-R27FKhJg1mYpCXhKQndNMsiI_zxl_ggm_78yIqilxNQLtTnT8OUa7YFMeZ0r5TnJM-0xMGZAmisz-5qgaTaJUXUA0cOjOy2GpuGoz8UeCz7xbKNHvzBDqx7ury7pQk99k6r_2SsVkux5NimSkL0P_87tosAieDohABpA4-Daq_Ee0GIK6rWj7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان پیشنهاد میکنم حتما از ست‌های برند mimoa استفاده کنید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103196" target="_blank">📅 21:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103195">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQzF97dTN3TWqGw97IeZDN0Ir37PNpj7IeVpkeVuQkcvDm18ljZQXv-nGf_7578QhHOkGfKUzUdSv7W5OaUvpUKjSaw1QP_lINXIl588DmnjI-heArvMADAm8c1-5kMZAcAvH6iaKDPSTIXp2OBlp0lPzN7RcGNP5nmBp7_7hg1dImZgYR15TlJOjIl7BBwGm-SEWaodkL5IcFcsQ0vXzWAVb7ADbSkpbXSUnWZHmLskw90e0IMEypraxSoI-OwJpMsOx5qmxM5zpPt5Dg0ldfSEJ0mvwcYqp2-LfmiaCj61APJdKIMJOutZFgY082ye1Z6zyBv72nZJUeQ-FIhT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
🇹🇷
#فوووووری
از گری‌جیکوب: دو باشگاه گالاتاسرای و فنرباغچه ترکیه بدنبال جذب گابریل مارتینلی ستاره آرسنال هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103195" target="_blank">📅 21:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103194">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH16QA7KW-mt6GJo15IH44hxqXm2Q8Lb1PkM3fi9Gsl7MQjsoVgA8I2Hfx9FpzZgNX6nCIu_XT1HtfrDwtMEVciTP_pUUXhmuv9VpDzXdyJZWxCcuOsxNJsUGk7UxbGF7ARMntB3cpgiJSu93u0Jh3CdWg1H-gBmvR1e9-WXkJRVrranKf7-RAs-o0LrqFa0lAc7K3V_1mD7JopES3OKlSHFHBvS6oyZMoypt3oYiMQYgZkdYwOBWiLBZzAMHMkFCmSxp_TRE4MAX5uA-ZxqxMjk_IvFIlX5o3wQWOaWFWzBM5RYY9r0LJTSX0VgCy9TLxX0o9CzvV9J1TsGdJNplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
باشگاه فولام‌انگلیس بدنبال ارائه پیشنهاد برای جذب هکتور فورت بازیکن بارسلونا است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103194" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103193">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5qWMOIgfUpIRYjl9mZt39kKZR03cxbNpInQaLsPx2fD2ERJmEooJyb4d-z4XS5bvyZHSfc6Fv7ShVX5eX3PiBrDvucAuLAsKQYEBkutDp9jeliefsQmldIYlbPH7t899wOKNFaeqOJhKexNdDja3fEfxpUgfKzw2999T9czbOOnvZBlIIBWonEPBGi0s2dxNUIJl4NA92RP2IRvSeSHcMRreFu_HPLUmuXGtS-UcUywuoEwQIjT0RVN5gLA12zuFnyB2SRAJHEx9ezWnWsIRBu9ztrrQC4z_f6mfISUHZKTeY4n3a39bdDetrl_xZUZHPgF37U_SAJD2la-oei-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🇫🇷
🇪🇸
لپاریسین: مذاکرات بین پاری‌سن‌ژرمن و بارسلونا هنوز آغاز نشده، اما ارزش انتقال او کمتر از ۵۰ میلیون یورو برآورد میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103193" target="_blank">📅 20:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103192">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeLjiDGsCL5C6VE_XeWSM3-Xk50vkrtN_IYXl-TyBiDEwWCuV6taPjHlMMViPs6UqW47PoIZFWmlmvH43QU96p5Z-J9QazUwmbmnYD9MAjS_bCSHwWZ_Xq5weXFVnonOLVCS1Bo8QTtp8cB5QnkG1DBF7U7nGnUpuRQddygG72rCQjuhKsIWycASpLAQhr7wxKQmkme-IZMhg8EPiNYF1psqylXpQLw5KSaxn4livXYoW0t4olWDFyGSoGnhMGirxWtsm3DVmcxPDlX5fHctOaIEtqEOhR8fTIDVMvi4Dmjt7PtltBXVk3x-LkyKYExJIxEgR-31fopOe4SDJSuqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103192" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103191">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWOHlabsjMS8lGk8MyRXqEe13I6ZUV3AeRNxyN0nYEdDjBH-pSgZJIoebFsnirVkxitURMFx7CYYjwWsuxzoHeRk6EA0C93KFMuMhVrWgFEyjfSvLHV1sOW4m6qKX_Ox4vKSE37_jRY3VPExQCrVrjoXlkL5KW-ijRsnR-HNCOJ529vTf4tTlW38JFHYbaZFby_owMDnGg8lFznceP27mcXkiVD4yIS0qYpKvrUIPChe8zkZVMbfb5TUzI_lmve5cye3QrRvznaR1EV6ifM2HlCdvB_BZCVFw0zipB2V0swNwcZjML3QEW1YqXpITrV1GxBI8qnaCZFftuC1eQ53Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
✅
رونمایی‌رسمی پاری‌سن‌ژرمن از لوکاس‌دینیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103191" target="_blank">📅 20:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103190">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA9wNYXrrgFOiTLW2dOkqCG2nGSEY8J1bkriNKdOn4pq4kNidVwzvQuVYlRGJceaDWXj_Mf0JAqXSE_bqXmB26Kh5gkyhC8hNdQvduBKf5r15wKJNdkODLv3vMm4hrk2EmbB03Gw5nx1Ck07JkFg8CBkM6iFGOFeeIz88sB8RVB8Dk48w0W4UyWWqD7xPZq3SlJWQFBUBpMW_1YGiDeNEGFBkhi2x8Kfp6VFYb8lMvmQyQ5nyDX9RBTNCglHj1_wHXVCzwuk9beXLy7dPnjppT6VV__ExiXXn4XvUVNP3SF3ZsXn-l9jasrJ5vawroSQqFlQHJfMqs6EZAd2JFVBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره لیونل‌مسی در مراسم خاکسپاری پدرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103190" target="_blank">📅 19:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103189">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=eAGcDiZKhfKfdvutJkILS7L8vS-8AuLziR86j2AgsqvT2TxPkQSw7AhGHxaIHeJU3GSeQ0S5yAqnhlhITDfwdN0L8bTl3212zYIh1AwPizXshs8BCmFG2fEcmkQkQkVyIntMRnPIbj0UYrHjv0mKTBzn4cpsOTIsp8DUUwnClhrteTPNmB-Yr2NzsbfpoE-FqkKJD6OnVit96E_zwyB8HQr6uYNVcqfK73eNkH9a7Ks9SkujjBKzQeXathTFVFLDjkjqN6TReMthpiGKkOvdOrknUVmizM1HnW59in5zfuv7l1d4Y-i1Sw9SApjrr9x6OubXGvcQvbla1pZ-MmXA4JHTZI2tnV4miFphSWppfxJ7sAUpa8JYsPU5k3FNE31VyVOVJEXMTAKwQqy1o898svuNz7P2t6UmNnz7Oqu7e13KKtzRcBpwfieE59UdDnTqoIdiHn9ynM3llbDhyHNcdKOaxvdoQpjDKKbFEoGVtwvWy7KkNNnNnXoF-wtF0NJDflm2J8daJcnOY8dGWLAQHzkMXYh_iwpCwux4i1EUiz-V0BWinnm8mU8mo6JSk5xYx9HlpTM-pmpqbh-PLnZfmcMXhjCF5NmeD_LsIyhkXO08Z-34fxV1GWdrGZU55mipSk38IC4BIU6omi3kqKI-xB48JfydeGQKOU20IwbfoHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=eAGcDiZKhfKfdvutJkILS7L8vS-8AuLziR86j2AgsqvT2TxPkQSw7AhGHxaIHeJU3GSeQ0S5yAqnhlhITDfwdN0L8bTl3212zYIh1AwPizXshs8BCmFG2fEcmkQkQkVyIntMRnPIbj0UYrHjv0mKTBzn4cpsOTIsp8DUUwnClhrteTPNmB-Yr2NzsbfpoE-FqkKJD6OnVit96E_zwyB8HQr6uYNVcqfK73eNkH9a7Ks9SkujjBKzQeXathTFVFLDjkjqN6TReMthpiGKkOvdOrknUVmizM1HnW59in5zfuv7l1d4Y-i1Sw9SApjrr9x6OubXGvcQvbla1pZ-MmXA4JHTZI2tnV4miFphSWppfxJ7sAUpa8JYsPU5k3FNE31VyVOVJEXMTAKwQqy1o898svuNz7P2t6UmNnz7Oqu7e13KKtzRcBpwfieE59UdDnTqoIdiHn9ynM3llbDhyHNcdKOaxvdoQpjDKKbFEoGVtwvWy7KkNNnNnXoF-wtF0NJDflm2J8daJcnOY8dGWLAQHzkMXYh_iwpCwux4i1EUiz-V0BWinnm8mU8mo6JSk5xYx9HlpTM-pmpqbh-PLnZfmcMXhjCF5NmeD_LsIyhkXO08Z-34fxV1GWdrGZU55mipSk38IC4BIU6omi3kqKI-xB48JfydeGQKOU20IwbfoHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
حمله‌بیشرمانه مجری صداوسیما به علی‌دایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/103189" target="_blank">📅 19:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103188">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqHpxe_CWA5yzhbn0ZV2zIvWrFvjEaUY4biQ-Fxfm70A0DTunVXao-7U8nldnc4p18jqjNVXOeRVa_QuHTFJ9N4Rrk8VXXAkFniJFc89_a-NXk_SrXK7VIT2zXikU9Yrxr-66EIxY0tcfP9PlgGzk7XCNFNvcpttHoCceqh322Hic8GUnRjB0p4NC43dCEOhhW3VRr1Dss3zwkAi5zpo4Y7HQeZoWYcFjaqT60FndVF6rn_C6DN-8vTLsCGHnp8NCoeJD1SluyD7s9-YA1j0875QxsjVnYV4x6fePZOiE-jdvUxwm3Qa4jKkX85rV2y4kpD3t6KrZDsFdDY6deNnmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
پرسپولیس در دیداری تدارکاتی، منتخب کرج را با نتیجه پرگل ۱۱ بر صفر شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103188" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103187">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toMJA9cmsstVV3XVJ9ArA68HWllOw1a5yqVrlCqbjPx_PLvARxLCzdN-dqlkRxHnyd1MK1_gjH29784k10O7NGoGzWkShsZGrjZgCi1Mtz9ECPLAGm2DcH40dHjWiJpc77psSaz--ZplM49e197WatMsiyC0NlhKQpOWyBJIbSurX5696jmyzPsCtJEg4cKku-Cehhrfx5ugQb7ZhXF3g3YtXBHO6Vr4WbJdzX8aCXwut3-J4h8bfz2fxJD3GMAGO67DptgtC98HLvvcpAWzASOxwPTMRUEr8Y5OjCFu6mSc-rSfkEhGde4kxl3x_wDbWTqth38PEWMkcNTtYVkn2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🎙
انزو مارسکا: رودری؟ فعلاً او روز چهارشنبه در منچستر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103187" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103184">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=NRl0_S5SniwnaxKAITDTgUhemfLT0XgCv7Jefuk7uSleaUZp8BSEqr-M5r6WsG4PeYjShTJm-Zr4Dhn6nncIZcx-L2uFccuXHfziiYyNLY01c0IWbiJt7rb7NeCUo6zOye4m-2SOK4K6m2Jvvv4CDSOej179K6lbLxKxZnprrlARWUqT6jkeQ3M6ngMel57puhvBWMPtdoGy303ANjHCJ2o47LIPHbW180g8tUzTzWS8aoyJzLcYlxwTokmjPxtZjeHSXMPaHrKE7FwJ3OBTRzV3NBy40lhUuZDUoJgeYerQn0mUb8FxRgpRrnXfKkHX6fWXAPvc9iu6OEmyIOBQyycE8vJnnfWC7HB11okmDUgKl8TAUgNJkmMI3VqD_fcBqzWVXFFnBGvBGUyuD2n-5ClyNFWiCx1bvEitPnTjh1ZuFqQicva4buHxEulrTE5fKf6nBn9WRTJihcowyNsT8R_LxC3U5pRLHKEsBKislKsiLC14PxVMoUlHVt2aVRHDz3LxWuItVWK1XMyuSw224aayK9aU68I8pOrWx7xKevaFUKKbRnNQVvVzPXV6Ji7ttilKa0NK2rGRfZKZVuWG9YAThaAjzNDdzYkg5YzB4ItL6bc0yBOvKgYEVhrgJokN0s9i2kIyDrfcWb3dr-xa3gncfCtWKvt__I8uuTh5hik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=NRl0_S5SniwnaxKAITDTgUhemfLT0XgCv7Jefuk7uSleaUZp8BSEqr-M5r6WsG4PeYjShTJm-Zr4Dhn6nncIZcx-L2uFccuXHfziiYyNLY01c0IWbiJt7rb7NeCUo6zOye4m-2SOK4K6m2Jvvv4CDSOej179K6lbLxKxZnprrlARWUqT6jkeQ3M6ngMel57puhvBWMPtdoGy303ANjHCJ2o47LIPHbW180g8tUzTzWS8aoyJzLcYlxwTokmjPxtZjeHSXMPaHrKE7FwJ3OBTRzV3NBy40lhUuZDUoJgeYerQn0mUb8FxRgpRrnXfKkHX6fWXAPvc9iu6OEmyIOBQyycE8vJnnfWC7HB11okmDUgKl8TAUgNJkmMI3VqD_fcBqzWVXFFnBGvBGUyuD2n-5ClyNFWiCx1bvEitPnTjh1ZuFqQicva4buHxEulrTE5fKf6nBn9WRTJihcowyNsT8R_LxC3U5pRLHKEsBKislKsiLC14PxVMoUlHVt2aVRHDz3LxWuItVWK1XMyuSw224aayK9aU68I8pOrWx7xKevaFUKKbRnNQVvVzPXV6Ji7ttilKa0NK2rGRfZKZVuWG9YAThaAjzNDdzYkg5YzB4ItL6bc0yBOvKgYEVhrgJokN0s9i2kIyDrfcWb3dr-xa3gncfCtWKvt__I8uuTh5hik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
مراسم ترحیم پدر مسی اگه تو ایران بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103184" target="_blank">📅 19:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103183">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=OlaFVQ-tW1hjVgyXzxDgAULpgXW8mwBz8i4b3wyLqD4cbX5EtRRZLUFWnt2ZJzI6FdUwsQBZXjn_StRqyYY5w2cYeVt0wqX1UobMYAbwP8c78TDmtUBN7cXnsrpbJ5yF3LWX0GiplJOd4lCi-zcLzB3z5ryKFhX55xhgG-C8U3LLUMpLoaVsghhxTxRiyugH20vSoEGlJ59UOTz5r0Gqym1s9O3ULRO1MyXD8X1FgW7dVg06jTZj6oAs2Lh38mjqcIzmYoWWSkWeAmtR2LqTdodV5G95mRg-p2T4VZOob4q7UIe1I4aAPK7mwn95l_iYvvDyykXzC3sd_eQaXiQHyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=OlaFVQ-tW1hjVgyXzxDgAULpgXW8mwBz8i4b3wyLqD4cbX5EtRRZLUFWnt2ZJzI6FdUwsQBZXjn_StRqyYY5w2cYeVt0wqX1UobMYAbwP8c78TDmtUBN7cXnsrpbJ5yF3LWX0GiplJOd4lCi-zcLzB3z5ryKFhX55xhgG-C8U3LLUMpLoaVsghhxTxRiyugH20vSoEGlJ59UOTz5r0Gqym1s9O3ULRO1MyXD8X1FgW7dVg06jTZj6oAs2Lh38mjqcIzmYoWWSkWeAmtR2LqTdodV5G95mRg-p2T4VZOob4q7UIe1I4aAPK7mwn95l_iYvvDyykXzC3sd_eQaXiQHyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کارا چیه مرد حسابی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103183" target="_blank">📅 18:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103182">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
هایلایت بازی آرسنال 2-3 دورتمند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103182" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103181">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=PTuZAMlM6nTlBWwAvRL5uZqlfPd5kNoGTXehRcnm5Hmzx8Z_gIb0ZwoxLHIrb4ZjrgJcDxaB8J_1tV3LF4TqtZ5nZxT0pvuYsdI1ZTFJG8xjU8Wz5hv7-TyZhwdxTwNdnZ-33Qwm6wiskHBMNRbjin8uOHbAwpmKdTSNo6H7ztVp4swna_QN_OkCKtTG2arlCxowMj3kb4_7AOY9BPMzoXUbFtLcJGFSNnj-awQHMmqX9GX3nC0vGI5xjrdb7Lw89jj4EAkjsaZr9vctNrxEZvPnl1n6KBi8nxMi7RkjyH5ObQEHXZlvH37h4p_3CC3B7-OkGJkz_t9YEif8cZJwGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=PTuZAMlM6nTlBWwAvRL5uZqlfPd5kNoGTXehRcnm5Hmzx8Z_gIb0ZwoxLHIrb4ZjrgJcDxaB8J_1tV3LF4TqtZ5nZxT0pvuYsdI1ZTFJG8xjU8Wz5hv7-TyZhwdxTwNdnZ-33Qwm6wiskHBMNRbjin8uOHbAwpmKdTSNo6H7ztVp4swna_QN_OkCKtTG2arlCxowMj3kb4_7AOY9BPMzoXUbFtLcJGFSNnj-awQHMmqX9GX3nC0vGI5xjrdb7Lw89jj4EAkjsaZr9vctNrxEZvPnl1n6KBi8nxMi7RkjyH5ObQEHXZlvH37h4p_3CC3B7-OkGJkz_t9YEif8cZJwGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلبم گرفت حقیقتا
💘
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103181" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103180">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5IhkKdwk1BKXuAVMtlcMLQ_hCwwvhyeH68OkBQlxrB6memf8flFvCJiV65xoCQRQwZrlQmz6WsTtx24xYfhJrhLToVHO_5rqbP48LlgZca9lSvm4569HjwKpEYzMVqXsnBDzSqaFW5k0UbEPPmQwLwkSC7YDHeZVd6xn-xfTYbBcY1Rh9O5WQJUFoNkewfphqi0DDYEOWT_atojdgbrEpOG2uu_CupmN1SV2qyQtUnB2jx9XV9YyVlO-wDRJOl_hlzI9pXSloqowbibYgSqJLJ0cCulo4H7F_dcND3_XSDzqYYKiajQyOvjqnW1w6BClIm3xmNK7Eb0Bju2_2aRVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🇪🇸
فابریزیو رومانو: پاری سن ژرمن زنگ زده بارسا و گفته با بازیکن تون به توافق رسیدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103180" target="_blank">📅 18:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103179">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=oQxCHCNrf6BKR2o-uGRHjm328Dt9HpxBSGbCZvYdQarFs0_zH3jr5ZqkoTAdvdlqpA_F5k9n6ykMdUpXDt_cOrn6W1cruFHQyANkLfqET4MWVS7s7UNfhgL-yadb8_N_NbsYq6Px-XUmad2_TaP-q7HPBj3TUcxtcSok0Vne6isFSw8x0VUlTa-Qoxo2LwpA_po_jRGktlt94NGeF9DdthEEo6lGINeDqm6m8A4JFFm2e3sF-uzG6KG_AdqgApoejUngiTxCjyS1wGrcQgWaYMBsKpZfpvIXE2j5W2X1HPv3uYzr-tonVrBdUpF9cOvr2v9WiEHkJZi6-Z32rFIvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=oQxCHCNrf6BKR2o-uGRHjm328Dt9HpxBSGbCZvYdQarFs0_zH3jr5ZqkoTAdvdlqpA_F5k9n6ykMdUpXDt_cOrn6W1cruFHQyANkLfqET4MWVS7s7UNfhgL-yadb8_N_NbsYq6Px-XUmad2_TaP-q7HPBj3TUcxtcSok0Vne6isFSw8x0VUlTa-Qoxo2LwpA_po_jRGktlt94NGeF9DdthEEo6lGINeDqm6m8A4JFFm2e3sF-uzG6KG_AdqgApoejUngiTxCjyS1wGrcQgWaYMBsKpZfpvIXE2j5W2X1HPv3uYzr-tonVrBdUpF9cOvr2v9WiEHkJZi6-Z32rFIvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ساندرو تونالی هنوز فصل شروع نشده حواشی خودشو آغاز کرده و تو بازی دیروز تاتنهام وسط بازی با بازیکن حریف به شکل عجیبی درگیر شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103179" target="_blank">📅 18:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103177">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGjVitBUF8VPioOO1t88x8ec6T-jxgNyYx5TE9pWm9NHhGjJHozSSji9r94_SYsG-7cK23wiFpvsdYVnU3S_HZ4iCvFKpiN3sKBumph01mYIhs9RFnP9cb8RTzzFV4uTZ8mZAgLHV3T8ovv0XERT9-ECXV3YeT7j21bS6T900gZgGekbeUl_jcAPJaNDcQ5BBi1PTcuigHBxHny0Y0GZdJp1cmjWFu_z7ZA1m-TC8ptxbtDRa-H3me1_GGGcyk1R_qqwZAjvCQyV4NDafQO_pvSkBAXYfI1Jok5MDMI2LzEzUngurD8Q2zm-rIu-LSMzmvGVeWqhDVQ3RHq2Py_40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQyRVtBjNvqTs9h9K0p4nnVI77A0mQdfXyQnXmwbxno_BxSXe0_REtqErtH-hR0ZtE2qILWBT3OIAJAweSk8umhRK4GvZrLl17-vrHVA_hTfBmlBMNgz4WCGX1KUyYe-DAbEaZ2pee8BNB7NOI9yAvHupwmTaDhSj__Duc1WEIF9JbZY9M_pooAU7bwwGYNc7bkYH6bc3tVfvPgFPI_M81f4Fgy5o6BY_WqSNoQfrDkm5A-Nww_5Vp8twW7cDo3Ns74m9utLrBKNIfiHyuHay83jFQkyRtyTR7Pqd2u4rmx28e6O-kDkf6jQ5LCAzaEIwRaBB88mWKdC64VTxwwRZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔴
رونمایی از برونو گیمارش پیش از بازی آرسنال و دورتموند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103177" target="_blank">📅 17:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103176">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFC1C17_r4OwQ7dHENJwGqiV0s4X8OXONaizwy7bwgqxrHNR08xmhFjZKcWZJwzphwrcmE-cbKLThi9PG6aDvpscN4hx3abYg087CHXfNWayugYWPMACSNENh8V4nBYtBmWonGyO5GzUBdm_mY1uzXVbuY1WZt4cfQJA0GRrNqXsWY9eucZMifKWhbz44-q10jYik9iCExwG0UCeykh39n9Uo1HF-T9eFYEAo2HP3Xw4yxMC3J9ZY2EapyKJ2-8nl84FLazzSG3LewOaqnZlhUymSHTHlgCS1Oz8rl-YGrM-YFhRy9OqkgOlwd9a38gbFIQBBJ6RsmjzEjgOgnUbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
چلسی مقابل دارالتعظیم با پنالتی مساوی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103176" target="_blank">📅 17:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103175">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba95cb0cd.mp4?token=ZTipCSXw7uvytT58DkaoMetoyzeE_uEyuJQoUT-giuOMLEftjYmfc-8GDaMEvv3U6JAhlFC-IQ_GScACytpYmE14q9KpDentDlodFpXH8bFzL4ijdg2PQlYJdqOhklg71y4QXBvMCixLdGSSs7q6FrhRwF0DcBNeEMzAhzCSqeU7wuAjWEfo2x7FAvtv3fKCVfkwCkC-3TmrEPwwzAuHzGF1EknPzA9WRsSUDBjaIFCEljt-b4pI23aMwoFbofz3s2SfVtGTqfvCEopzyI--KIe6rviFN0LAjIqrn2fxFv4ocfudLLNpYllEp8l3fJkXFJ_Z-C8P3y0Tw5yHrzZYwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba95cb0cd.mp4?token=ZTipCSXw7uvytT58DkaoMetoyzeE_uEyuJQoUT-giuOMLEftjYmfc-8GDaMEvv3U6JAhlFC-IQ_GScACytpYmE14q9KpDentDlodFpXH8bFzL4ijdg2PQlYJdqOhklg71y4QXBvMCixLdGSSs7q6FrhRwF0DcBNeEMzAhzCSqeU7wuAjWEfo2x7FAvtv3fKCVfkwCkC-3TmrEPwwzAuHzGF1EknPzA9WRsSUDBjaIFCEljt-b4pI23aMwoFbofz3s2SfVtGTqfvCEopzyI--KIe6rviFN0LAjIqrn2fxFv4ocfudLLNpYllEp8l3fJkXFJ_Z-C8P3y0Tw5yHrzZYwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
😢
وسط مراسم معارفه نکونام برق تبریز رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103175" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103173">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsrFvTakim1rJyCYqHc-iPX6UwcH91JXZimhB9TAWZh2ChrxvH_KMFHimIFFBUSaXET074xvZXnN_mJXWB_msbObKVsJyboPcVHFfsBrK4FHYEIQd-atsOpDr11gVVhf3wZdri7g6lHg__MkeuNAdKJjy9iTUtCSD638llziyJlCXdtWI4Re2vc6TwQsNTuNlSzILyx3cqdFaFFLWuz-glgOtSCPpHz97bznTeV8IlUkYbEPny7ykHDh3gp0Va8UZ_D6mzNEHJ64nTW_wRl4YtpxXyl8pIHTMqBIydMd4hemSfAc7ntxa9-n_Kb0MW6LYm2N751szJ9dANRbropw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه دومینگوئز بازیکن 16 ساله اتلتیکو تو بازی دوستانه به سیتی گل زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103173" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103172">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=YBvobkb74o7txFs4HkB4ldxNF84qkbiSMW1NdaCfXkwVCGDoF3Abr3zIsXsBaguN25qrsXv_FnmLIcHFKIp86eiz8BmvB6dcF_oTQqGHNntwA8ox4mHcnHAXs6Enxpuu2nZYRuQNXLBj752tjLKT4Sp5jwzhy8l0IajTPBoURGdK8uXd31JyoJO07tOcQWpUv1lVS6Rwu8B47-k-94mDLlqXKkK9pkGykxdAF-mB1svl_emctNjPZH7T8yfKE5Fk5SWgP6rH42alspjrtJkcKYyPaIGhqYc78OewXb_opB4btK0X7WrYjZNl0yAWjl7_Sw_WnjQJa364F3GQ5_uxAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=YBvobkb74o7txFs4HkB4ldxNF84qkbiSMW1NdaCfXkwVCGDoF3Abr3zIsXsBaguN25qrsXv_FnmLIcHFKIp86eiz8BmvB6dcF_oTQqGHNntwA8ox4mHcnHAXs6Enxpuu2nZYRuQNXLBj752tjLKT4Sp5jwzhy8l0IajTPBoURGdK8uXd31JyoJO07tOcQWpUv1lVS6Rwu8B47-k-94mDLlqXKkK9pkGykxdAF-mB1svl_emctNjPZH7T8yfKE5Fk5SWgP6rH42alspjrtJkcKYyPaIGhqYc78OewXb_opB4btK0X7WrYjZNl0yAWjl7_Sw_WnjQJa364F3GQ5_uxAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#نوستالژی
؛چالش‌دیدنی‌پسرمارسلو مدافع سابق رئال مادرید در رختکن کهکشانی‌ها و ادامه داستان...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103172" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103171">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg9YYHhOpqhG3BXs89CggCh2gG_fMqd57x0jGeEg95jsCL44ATsQ1VwQ5wdHA3rFv9-ALPcMl8X6-7di8ZGoxcZAMFZr6P0vh360zXxTtTm8bVCimk_xcAFl4a1mHldDk7YQ3vOhAeLIT99HHct6oxzSp3_TRz9e2aoTT7NSF9xLCawqFMgfo-MgfjxYtnfNI4etBz65FGIZq-WScqllcaMHbgBG2IZDzvcj35HsMq5Xibo288rf15u3JNcpOuHw4YHOKMhEoxz7XzkPZvcdGsRy_P3ggZIoQPZQmtkrX3El7uMXui3FombPTUgna9C6XhesaD12s2PemUVvS1DUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
8 سال پیش در چنین روزی، تیبو کورتوا با قراردادی 6 ساله به مبلغ 40 میلیون یورو به رئال مادرید پیوست.
🎙
تیبو کورتوا: تا هرموقع رئال مادرید منو بخواد میمونم و قراردادمو تمدید میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103171" target="_blank">📅 16:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103170">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=Ht5DP1MVLOe5ozgS-lfI3uN8kquAjhl8yCQaVe0p8kC1sOKbCDFUJ414MX0ClRTOTTSoXIabOZuplvx9Efdf6grn_TlUEjOUEynVYJYMcF8jsh8it94Qcf06J90COKr7TSddJZ_wicqKfMgqQZGknbgUx79egWkWHdU9OSEOQXBbnNHRI15Ip4xb9ULtNKtUaQpV8SFg5GqX9p0VJzBk-8XsLA4l3r6fCZBiH3mV4Z1h6G8amPz2ZBTvuprFquH3jhRKTYlnPVnnEUpsFoKyuqae5sO69xB5OyNVhse3R7KgNzI8xTl3oxhsHBXjjENBjl-Ewg8WwXGVyJnimXr_eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=Ht5DP1MVLOe5ozgS-lfI3uN8kquAjhl8yCQaVe0p8kC1sOKbCDFUJ414MX0ClRTOTTSoXIabOZuplvx9Efdf6grn_TlUEjOUEynVYJYMcF8jsh8it94Qcf06J90COKr7TSddJZ_wicqKfMgqQZGknbgUx79egWkWHdU9OSEOQXBbnNHRI15Ip4xb9ULtNKtUaQpV8SFg5GqX9p0VJzBk-8XsLA4l3r6fCZBiH3mV4Z1h6G8amPz2ZBTvuprFquH3jhRKTYlnPVnnEUpsFoKyuqae5sO69xB5OyNVhse3R7KgNzI8xTl3oxhsHBXjjENBjl-Ewg8WwXGVyJnimXr_eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلای تاریخی کیانوش رستمی در المپیک ریو
❤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103170" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103168">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dla2hDVcl8VsBeOOiLgesRPTAgYJnMJ4A4a9aBOjVzhi24gDmp9UJRbkyAXRxdO2OqyPNgSIFRH0hEFj3bLXOVXDbBuj4BZO26Td9RBZ5trFiBB3gMqR0ewuLMaAj6YvWvasn1ZSH8UQKShf6CisdtVlQUi83NdwDPaIazlpMJjzzVoJOmJ5dlP__xCvY78eU5iMrIOEhBekZPNaoHDhc83eKqAuhcz_f59MLWu45tDR97o65zNJ4EI0zrqt9pHfd9N3p-HVVqBtfitIIh3DwUQvcQx5mrO3B0GZKi94I8AawcbpGrWosoGVRXR1UfzmotSmaG_nEvNuHXpvrdkr-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mT0vj2I0otOfDrx2wpUcSFlCsL647cMPm6-195PqrxVry8BnxIZAp1M4AqUz4d6q_gY5XLlE3PARO7TATtzAna6O_tyF9c8RAkAHuJwz2d6tBB6UpRJIgf1gHRI7S-Ix0XKMFelV3OjWmlUVq9rJbVOHTt2cQQPO8E2UGQznSv4tteUiPdPGvVXR42ODi4_HSeOjqZl43c_5qZBgJbGTZLRkEvhj7rj6JirwPGgP0P5Jq4GM4ePybfpyqlZ72MVD2VO8T_ilo08KfVZt4lrbVqf_-l43-45wil4BR4G8b6_vNwLHs-6wDavIj2rJf3nwtuICX9O93SkDNmYzqsZ23Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103168" target="_blank">📅 16:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103167">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=lyJw2x8G1iJSUFkGtLvo7KDVi4A8SUlNvC49lfNduxS5vMxL5lN3pbV-jixOhzcVTB0LenKw3wX8Dj_nEpVmAg0YmUyIQHPNQFuIfqIvIlc_5fUfSBBtxTF4KylLQFtocbvrJYabNNcX7CcatVpW5sBn3nWjRdCuAvkvLmUu0GJh7u8KEuWpmh5JnyF5RUl15hi-kUzUv1jF28B-ozVl9OV5DMjxi0wbx9CqcR5TLEzmBSm-mxH7upX8tgBPTi8OTcpCmxOhAYYS6J1muFIcyUPolUlGmtFEd1VRCMo0Fks7wtV-yA7g9lovpbzeYuaU4qEIB6dn6smCBOQnzT75tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=lyJw2x8G1iJSUFkGtLvo7KDVi4A8SUlNvC49lfNduxS5vMxL5lN3pbV-jixOhzcVTB0LenKw3wX8Dj_nEpVmAg0YmUyIQHPNQFuIfqIvIlc_5fUfSBBtxTF4KylLQFtocbvrJYabNNcX7CcatVpW5sBn3nWjRdCuAvkvLmUu0GJh7u8KEuWpmh5JnyF5RUl15hi-kUzUv1jF28B-ozVl9OV5DMjxi0wbx9CqcR5TLEzmBSm-mxH7upX8tgBPTi8OTcpCmxOhAYYS6J1muFIcyUPolUlGmtFEd1VRCMo0Fks7wtV-yA7g9lovpbzeYuaU4qEIB6dn6smCBOQnzT75tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روی کین اسطوره یونایتد: اینکه‌دنبال بازیکنی بدوی تا بخوای پیرهنت رو باهاش عوض کنی کار خوبی نیست. تا حالا نه دنبال کسی رفتم که باهاش پیرهن عوض کنم و نه از کسی درخواست عکس داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103167" target="_blank">📅 16:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103166">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ojf-b20ZmqMcYL6QGeKYd2px_5OmDVg7CjS3M-Z1a_nw2Lcs87xiBGHhnRm7YIksfIE8tv5_VsE6K1SGORBN13hIgeQzDRAgtBq7BSbhUTg7I_5W72HcP1Gp6NKgzUdnqfZjg4QXAOcScTeuFZ7wB5MJGe5aHsBXtGfXgzcJMEjR9_cPbUKFYz1r9qWR5aFqJKbUciaV6qlN0OT9JFHaLEs3wMfp1dRnMCfh2LCNmO9fZuzwt6Lwj82p9-5ZDnrS2rj2qqEcc34Fg8UEuDUYdokbM2oRB7p4lXsC27NtZK4eq9lcPLQCNydR5zmceHN6O0JTqgTmOjbcIEDCu-un1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چلسی از دارالتعظیم مالزی گل خورده.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103166" target="_blank">📅 16:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103165">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-our3arjusxBSjWgdW3lSqbf7nZ0pyC-7n-cOVFK4vmwFvIxbGL0sYk46FnPpX8Sa8IGvAb5gg7JOqCpfADJ2GCN5eZDdVN_oriYirCca45SVdOxbF5woNZXIzquItRneuBIBGrcyYrLL06Chf9OHCVwz-w-I-w00dU54hEa0a11VJl88hajQXbt7EGiIcTRAu6OqD4FWi5nrP0WOZTOUbb47IrLjK_QKno1X45BxPcl_UqQ1XKf_DjE4vExwxYlHqho_OaLyC-bKX0hxvnFY4Aow4FbJgm3bLtCU0BdeV17dIC8fgauxTTUlyuJk7DbxoMztNIaxTlSennwAErLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عمق‌اسکواد تیم‌آرسنال در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103165" target="_blank">📅 15:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103164">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=QJEN_XK9vkXCQF2YcnffGihVBZiLtz7JBBX0YIKAcrQuY81_Iwl6fFOSRbJyf4KGxexXjn3-Qwp8e9JLm-ETbOhH9ZVE4kvT_aw1vpNdWUNp13ttu8SWAJ-V3_a2-ZlS0U_faljWb8dXDgLppulqgQrvbYjtBCkMBNV52L0oQxc97c3ni-lCJ_wO96PcryQL3acBEkkRtDYo4oIbsNTCDVpA_d2Sbgkj2q56tl-TFIDfB6UQFjdSUm7WcCcj008PJDXuJtXn9oje9j1M3ClRdeWMxYoD04dQfoMcRfT6w2P82VdCX39ztqa7Aw2MNzv5hfi36ImfjulIttDOjPr_Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=QJEN_XK9vkXCQF2YcnffGihVBZiLtz7JBBX0YIKAcrQuY81_Iwl6fFOSRbJyf4KGxexXjn3-Qwp8e9JLm-ETbOhH9ZVE4kvT_aw1vpNdWUNp13ttu8SWAJ-V3_a2-ZlS0U_faljWb8dXDgLppulqgQrvbYjtBCkMBNV52L0oQxc97c3ni-lCJ_wO96PcryQL3acBEkkRtDYo4oIbsNTCDVpA_d2Sbgkj2q56tl-TFIDfB6UQFjdSUm7WcCcj008PJDXuJtXn9oje9j1M3ClRdeWMxYoD04dQfoMcRfT6w2P82VdCX39ztqa7Aw2MNzv5hfi36ImfjulIttDOjPr_Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
کابوس شب و روز بارساییا در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103164" target="_blank">📅 15:15 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

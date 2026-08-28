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
<img src="https://cdn4.telesco.pe/file/c53FGN8spbQYSpqXwfXgo75BoDWEX_pV_XC3w-c9WMPL4Ubn_sCzj07VLDPNmsl-N_KHrA2x6ees08ZmAFI2wlB5_17cRJ45EMfjuXMWTzqHPSSMQp6FHoqkDNdeGnbRbCvsnnyG2gr5wSedpU2EMZjh8EU7fTqSxS7wL4Xhlt4B1Vns-M11piZpIislSePNDgwAAuhJptXjot2xObkoLG-MAhohsLIYEjv3LezF19BXtZytvUkjtcxopoB1FN6ay3uzWHn-aPFLT_zAPoM4nzwxCDm_K4yn-QzV9_WbTq4uSHfLkarIIxrIvIwB6ExCywp5bl_0wPnodjDDeJe4Xw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-82685">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1PGVswspDwr08eNSPNKesqw_iFqeJ9g_Tyer-IXe5Zx_ooKbywF8Kdnky1tX6mINIZBD7fdO_MNUZUa5ej6DkwK_8j4hf55En2oTshxqQTELVWzp7_dc4r_N7n4T71gpLQcU5Ksg9ohSwllvkJr5Cytoikab0Ium_lvDhzsMEleSHfqEgjcKwlRb6j6qO5wtxk-x-pPZSf95s6Fd6v9rg48VW1YfDYhxuDn2FajFdtE2DoJtpWjtrvQK6GDXYI_UbZ0QUjA_ZSC81DZ2DZ6dT613AjF2SQZN4L4GoASdIhXjenn63t2WR2dZcypDWCx1kuwL67laOXX72OPzIWapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیم ساعت کسشر خالص بود</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/funhiphop/82685" target="_blank">📅 16:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82684">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پوتک آلبوم داد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/funhiphop/82684" target="_blank">📅 16:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82683">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پوتک آلبوم داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/82683" target="_blank">📅 16:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82682">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نتیجه نهایی اومد برید و کارنامه طلاییتون رو این زیر بفرستید ببینیم چه کردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/funhiphop/82682" target="_blank">📅 14:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82681">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03afa533d5.mp4?token=duOPZDDJx5V4hAhCSEUcBLbmP9ScqoA24mC4dblHp79E3ALAcdcssncjwUYGwqlZaEU8A1NlhWkdJKBhSssfGlrmAG3J1qWGPWxuqv_s6DhjepoV577KEOxFxp9NFkyOS4ZWXy7yxW32--buOGp7NOFRqWWxDAdftLj2-Hf1HZ8eBsC2gB0IYVH0kHyE-MoiEw1fIMdRJ1r3s0Nc3p_6DSM2rXqZDtyTR5fTL9hF8XZv-quiz9SYcTDXQHiifXbTldhHHrOG-m1UpJDeuUs3N8q2xQAestcb2oqM_fRyMofOfk5UH9ePQC8PRYzWRCigmEdQSmBE-TjKpt8grrSOgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03afa533d5.mp4?token=duOPZDDJx5V4hAhCSEUcBLbmP9ScqoA24mC4dblHp79E3ALAcdcssncjwUYGwqlZaEU8A1NlhWkdJKBhSssfGlrmAG3J1qWGPWxuqv_s6DhjepoV577KEOxFxp9NFkyOS4ZWXy7yxW32--buOGp7NOFRqWWxDAdftLj2-Hf1HZ8eBsC2gB0IYVH0kHyE-MoiEw1fIMdRJ1r3s0Nc3p_6DSM2rXqZDtyTR5fTL9hF8XZv-quiz9SYcTDXQHiifXbTldhHHrOG-m1UpJDeuUs3N8q2xQAestcb2oqM_fRyMofOfk5UH9ePQC8PRYzWRCigmEdQSmBE-TjKpt8grrSOgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرش عمید، معلم هندسه و گسسته‌ موسسه ی مدرسه آلفا وقتی یکی از دانش آموزاش گفت ما برای کلاست هزینه کردیم به جای صحبتای بی ربط، بیشتر روی آموزشت تمرکز کن هر گونه توهین و بی احترامی که دوست داشت به دانش آموزاش کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/funhiphop/82681" target="_blank">📅 13:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82680">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeMaabiuTt9wchI7mOgMNYU-PwJoDD6bE2K_pO7VT71SBSTh6ofIMe43p6lxclgY6XQyBk2huv3atKySVQ-y6xzuRSHuPk8t4_kID69tQ7CiKTh4TOMB5BQfu-F6-qjMYeD6n-z-tNTdn_eV9JUVNrCVaXUcUXyD7dYP02xFNBT_07_fxdChZsnT_3nFMgwXk7ofpNLsSciw5XurhXo9XUGVFP03EqR3GyLqhbNF4ag54mBYklez0_nQ5aQMxqCNiuKptzobfmZDy0adNP-givW7d86JquV66oA8o_o_00RSHe8-T343y2GaLgSIhu4JRMuC3aZmR8ZoJ11tI_E9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی سری آ ایتالیا ویژه هفته دوم
💯
⚽️
با ثبت حداقل ۶ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته دوم سری آ ایتالیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SEA2
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/funhiphop/82680" target="_blank">📅 13:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82679">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTPnrs8V_3lrMkCHokigziQTWXB8ipekceuExjGaxNcazd7WmRH8UqPBZdL5Bx68w5MD2LRTtmG1J0BjFTZMqW0K2B8Dy0Ns6BH2O2shAF3KSsNxpwfrBYRTJi5yXAnmwf6-7U1PNkpUGA7Vz8iIlLK_O3HM9jXoDIFRN-uMVmoSISot1_4SfzKJtOOwdMiUx0mXh3n4FfFZ5Mk6OibwAhD5k87wcUVX1lw-ViAbpTctWjEwcNUbawMppbN77UghND-qgrp_kWMHs7DULa4FGFMABbQXeqYx_t7O9KkWiRu7PGpjhYLow1u0FXugh9Ct-ZRyOAXLP7OCx_k8BYpCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون دکتر عراقچی جوکاش قابل‌تحمل‌تر به نظر می‌رسن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/funhiphop/82679" target="_blank">📅 13:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82678">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrVSqvn-MkNCYySwPiSTJL_gai2S694gdEPDyHRti6mJdKe0Ndi4eazYN_RrkEaMg5KyVDeNAsqx9RvlIUe8la_hxNijxBQy2rtP97T1mqO93_PhYPBwONUWoLv9skSSbtn7Dncaeg3mMjR2y8ATV9EwUdhHterwacAKUTHmBQbkKFQH9mWCMHUTQD2GmiG0muhduPabfV1UjGzG2iSG2IbIkrdA0O3G8b0JRXl-ACRriUlJDg6d0V-EgvHRSVr2hggf3ESG54hx5JYAvrOPOfLguZANB8NevXGZvsKJOjXmlut25PAWpbcrPb0HlPTRzKxdSQfxbCCDC7O2tWVlfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم از همین الان پس‌انداز و لحظه شماری می‌کنم برا کنسرت استاد نامجو تو برج میلاد. واقعا حیف این همه نبوغ و استعداد که این همه سال از وطن دور مونده بود. ممنون آقای پزشکیان
💘
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/82678" target="_blank">📅 12:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82677">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcfb73b16.mp4?token=X373UV8gXABiyvaq1inn7BnKnROPzatyDxl_cB1hposGQMNnHerCLTZ1Q_Bze-XVu5FK_B6_HBXrZtybvc8-fk0HNmzkVY77DM7lSY6kEDrfAUhCSJnVq2gpEoykgly8EwN9oKZ7TE71gJcWrmTIJPEQ1BKqCUpGbHR0K8YefenNCTYhIjqehukqk1WoFCx91ty5HUq4WaIfbLaofVKcf4UyM0O-z83Ix8CUqcS3qw0leOq6LBzwCWRcq6OVo7rKpqdF5ZzU1ZpiUpthgzAQWO5P5K6S9eCMZwt_aJ6QtcVhCP_MlPuF2tQfzD63QC8td4cYREOsJdWy1WWMWMMCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcfb73b16.mp4?token=X373UV8gXABiyvaq1inn7BnKnROPzatyDxl_cB1hposGQMNnHerCLTZ1Q_Bze-XVu5FK_B6_HBXrZtybvc8-fk0HNmzkVY77DM7lSY6kEDrfAUhCSJnVq2gpEoykgly8EwN9oKZ7TE71gJcWrmTIJPEQ1BKqCUpGbHR0K8YefenNCTYhIjqehukqk1WoFCx91ty5HUq4WaIfbLaofVKcf4UyM0O-z83Ix8CUqcS3qw0leOq6LBzwCWRcq6OVo7rKpqdF5ZzU1ZpiUpthgzAQWO5P5K6S9eCMZwt_aJ6QtcVhCP_MlPuF2tQfzD63QC8td4cYREOsJdWy1WWMWMMCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/funhiphop/82677" target="_blank">📅 12:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82675">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GAH-aDfHNUN38oLTgMovRdV2_ZQsopamKm6I6Ng2V-k5V5Gh9hsiTMMZyU2jYIbHrcuITCAOiIofTUsm5mVO7rYMEhkyEtP6o3KOua-LtKn5yL8yRApS2vyOW4_b2_yS5o0ippPkG5hG6eY6gpax7j5_h-b92nIXAI-n_bEpCkyMebIeF3kK9aXmsGFcT5E_kaA4zud3qhBJpoOL_hoT3zWJdu82Iwru5z-z-R0ouVC7uowHdlNpKX5wOecPYd5_zHavpPo2I4H7lFQfMf5EYY_6kSZwEJ0ySEfrZ0xG9X6eUmrGT2h13cGenGuT2mP4kAykL926Y6fTkKbbxIA30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNlHATKBvzEjEKICpSQgkPRnwPnxtrGGmUDX0c_Qr01GKmAVXgC43GVbyHoVSSjSqQ7LjqrlfaRhpzuhH0GT-Q_BQKOqDDjJmxPXUn-bdiM1EtG_pmuQ-9WKk0BkeJPtm6GOwar2J4Rc4fjnmJuIMUf3gAepbytlNFj7ZdyLz3F3UGXT3pqhFPbMgTWJ7YPbUHGVfPPNYNZ-jPsRiU6Lr-5KJph6hjNAhXq2BGijyxFElfdMG8FI4HH7mfpB42lTHmzgjHHvRt7bA19ayoPysGRTBXslldtPSXWgCIJ7QXHXY77inHNExW9tKR289e62VMyxOxJoCqAU1ySaJXXwHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارسلان دیگرد (یه رپر زیرزمینی که احتمالا نمیشناسیدش)، چند وقت پیش تو یزد یه اجرای خصوصی و محدود می‌ذاره و تو اون اجرا یه ترکی رو اجرا می‌کنه که یه لاین سیاسی خیلی تند داشته؛ برای همینم براش پرونده تشکیل میشه و به جرم تولید و انتشار و اجرای موسیقی غیرمجاز، ۳۷ ضربه شلاق می‌خوره و ۸۰ میلیون تومان هم جریمه‌ی نقدی میشه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82675" target="_blank">📅 01:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82674">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgl_iEXGKaKQflV5LKnDpI41oXjQ6AvrpCV_7ZShcWg-Dy7tKN51whRTxJ5KX0uDYt2QuuwGpRb0QEiWf3FErYB_CufUBbWwlJQzKmBah_h9gFnLPDDyuNnhszKnWnpbJApteP4l6_-PV9Ypf4YBdgwRVkWh61Aw3i_Jk1LCwPCsHOsubbx_JwaNGZd4n8Kw9RomMaK9X-eItQRjlCZVI0GZGwK0DNfk9Lh1m3C54xVcnpgI6wpWQWRbVBjyxy-oB2MZHssGmUMxZwkhpIldv5Ams9rMxM6PBB570kfmU7qV5-XBfwnInCur0LdRrJbajBfGiEMkQpGVkIGbGgx33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نا امیدی ممنوع
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82674" target="_blank">📅 00:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82672">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پدری شاهکار ترین هافبک تاریخه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82672" target="_blank">📅 00:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82671">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از تهدید کردن فک و فامیل ترامپ با زبون فارسی تو صداو‌سیما منظور خاصی دارید عزیزان؟ زبونم لال دیگه اینجوریم نیستید که مثلا انتظار داشته باشید پسر ترامپ میان برنامه‌های ضلال احکام شبکه قرآن رو با دقت نگاه کنه و بترسه مگه نه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82671" target="_blank">📅 00:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82670">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نیم ساعت کسشر خالص بود</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82670" target="_blank">📅 23:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82669">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده. اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82669" target="_blank">📅 22:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82668">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده. اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82668" target="_blank">📅 22:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82667">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کمتر از ده دقیقه تا نمایش رسمی گیم‌پلی کامل و همه‌چیز GTA6 توسط راکستار مونده.
اگه نمایش خوب باشه بازی و رو PS5 پیش خرید می‌کنید یا Xbox؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82667" target="_blank">📅 22:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82666">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینکه هنوز ترامپ نیومده بگه برای آه کودکان مظلوم ایران و گریه‌های سحرگاه عاصم منیر همه‌ی تحریما رو لغو می‌کنم و بهشون ۵۸۴۳۲۳۹ روز فرصت مذاکره می‌دم کم‌کم داره نگرانم می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82666" target="_blank">📅 22:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82665">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ بعد از تغییر رسمی اسم خلیج مکزیک به خلیج آمریکا و دریاچه مرزی کانادا به دریاچه آمریکا: ببینید، ما الان یه خلیج و دریاچه به اسم آمریکا داریم، شاید وقتش رسیده که سراغ اقیانوس اطلس یا آرام بریم، اقیانوس آمریکا تنها چیزیه که کم داریم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82665" target="_blank">📅 21:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82664">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=Mz7GDv3_7phUzkxp_LEbK9Wr5IGJPM6S-cS0p2IVw6foa7xi7AertQGX6LPiqV4E7As2DAEaDmi1FVpYHQoGVKHpRa2fpK0_onLYqkxVgvLgM-8KoX1Ly7ijPRJN4sQeCGTm8dlQAPTMFqItm172GMmiL2Vh9F5XsBvDc82a1sTUYw7gXDMYr7tRLELUl1-ezLfQK-Ex3saC5oWCZCKj5A_HBxSDhr2erxj-bNzOwZXgjzLoTKYDbEOHzvI1XB1tt2Pr_hbyBrad0Ny0qSeetKp7v_FjWr8xWYQA5M44hSFgpw1M178OyOCUbcC-7CrUoauAS1CnBG1XJ-eoj67xkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=Mz7GDv3_7phUzkxp_LEbK9Wr5IGJPM6S-cS0p2IVw6foa7xi7AertQGX6LPiqV4E7As2DAEaDmi1FVpYHQoGVKHpRa2fpK0_onLYqkxVgvLgM-8KoX1Ly7ijPRJN4sQeCGTm8dlQAPTMFqItm172GMmiL2Vh9F5XsBvDc82a1sTUYw7gXDMYr7tRLELUl1-ezLfQK-Ex3saC5oWCZCKj5A_HBxSDhr2erxj-bNzOwZXgjzLoTKYDbEOHzvI1XB1tt2Pr_hbyBrad0Ny0qSeetKp7v_FjWr8xWYQA5M44hSFgpw1M178OyOCUbcC-7CrUoauAS1CnBG1XJ-eoj67xkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از تغییر رسمی اسم خلیج مکزیک به خلیج آمریکا و دریاچه مرزی کانادا به دریاچه آمریکا:
ببینید، ما الان یه خلیج و دریاچه به اسم آمریکا داریم، شاید وقتش رسیده که سراغ اقیانوس اطلس یا آرام بریم، اقیانوس آمریکا تنها چیزیه که کم داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82664" target="_blank">📅 21:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLhp6pEujs1gOnQe462Diu34r9dk4gsYc9XV5lTxeTH6PxFTkgT_GMiClRycv1NpxiBrL-oH8z5yNGwOc8udbwJKgSAtSkplEcHFm3cSalKiNL4fe7R6OMo1fTwbBWj76ZZrmCBguq49bbEbnzFfxO9djEOt-9VqMnH1l88k2_zSWpXQl39CjPV_h8-KQQAakssBLVJ9TlpINqIXakMzDpav4JKLrYbO3eQpv2IDI6ZLNv-6j2ul6v9m4FWHQEa95MzjxpujbKbxsiJimxox8B5W7SDNCyLaJSrBCKvr6eCaHjXA5-AZDhg_FCPtNYQkNl2DGU0CkW9IvN7jzu5sJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافه‌ی اسطوره‌ی نون حلال و ایلان ماسک نابغه‌ی ایرانی به خاطر حجاب پلمپ شد.
💔
این بچه تازه با کلی زحمت و امید و آرزو بالاخره تونسته بود یه ذره پول جمع کنه تا به آرزوش نزدیک بشه.
اینه جای تشکر و حمایتتون از یه کارآفرین مستقل؟
لعنت به قوانین سختگیرانه‌تون.
😔
آقای پزشکیان و مسئولین با غیرت لطفا هرچه سریعتر رسیدگی کنید.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82663" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCp03JbfJ5ikO1MlpAkkqT4Fly6i7r67_nbbGCYx0Q065GPlqNrhkYnAcFZHMHJxNV8-8ArL6JpKx-uA1ybxY5JjG2thFlUY_dKSLEazzrlbGcWngZzlrsyLpYa9XIJtu3Wk9V-g3UKpJbpIuc4cw4dnmqybbQGBpXGgHKROmjUZbM_HFT32lWrz066_Pb5iKU38Ijhcc7PxFCjyeQ-HfvwFqYHBf0TKhF5NmBjW4OPp2BjJ0SqE75A-yx-28ci-F8Y4VAet2rO5G_LkBSNR_Dzzw1dZHwssVfKobMrICte1opSDP9JwjGdelG477DwyERq7eDurmT-dV1KgThY85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه این دوستمون اون اسرائیل رو اون وسط نمی‌نوشت، خیلی جالب می‌شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82662" target="_blank">📅 21:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShirazVPN | شیراز وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI7LzHaa45stZQJ9KwYgCx8ypUepk-fCqsYW3p9aPzm2Z1kbiA9F1AnpcD_PMKH_71s9csAkDgZB5FJeXEFpksrEvQDyv3UoqqejnZzY-A2vLYeYpaqG7INFPTeleWr1nmySW1kqYBbzVTBU-AsNfPbuADkzBEJCnZbCIaEkjUbxJAVuxIGr8bzbmBr7zXIyn7BHli4xpigpFE0hbhPea7AL-Is6doqXMHqpyojtjuO18MypfmUXAJIp_dqOUVHks8h4jZ3H264koqN_qTpoMqCisHk7wskEH1VwjAp8ubJuxQWtinMFVnXsDSjheaMnSkbrWHCGJ-W0vLkeZaxRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پلن نامحدود فقط 180 هزار تومان | خرید از
🤖
@ShirazVPNN_bot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82661" target="_blank">📅 20:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82660">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojmTvrDISY9La8vs2Xw6bXrP6UY331USeNgMPHvuL5qX8cyfupvfDsJdyZ2QA2jt4NqZVBGLLDZ8gpTSLt4sIf7DKs7WA3xk-rXJdnxYMButNja7tu0h2SvpZluIa5lJSlshaZ-NRwMTIutD95v0UE3khk4XHtRswJD8SdVXwYaBSP3OSgOsRKr-xX9NRmzzIPHpaOAVX2R7UeqIvqRYt5n2tDZ0HdJkYykx7FkC5rpqe8tcrTlhndqaNO8MUeJpTDtucWjCUw5_e-BjmDD6CDu9iTeO_JA0lgwCTNl5Dky_pyyk0kGf7JVp_SDXtP2nkZz7Vp6iQIbndITtNa1PqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسا خورد به سیتی و پاریس</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/82660" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82659">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بارسا خورد به سیتی و پاریس</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/82659" target="_blank">📅 20:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82658">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlsiCDEGeuQE__mknWIzAE0_YQN3IuJxKaTmZeeWrjLHg-3-SZ6ViLDmIKJtGyUCjTdZ2zuNozOLCfL32pl_tOor6sdHFVX7Krf7snMsjeByP0z6sIHNbE_iFhetTAwjyZU2Z68CCUgtkHSa1DIgYvZN013T6rP8gtWnFmqOUVgRgL4swNgmvatGrgZd9wHVpkBEbtddaC3AFQt8yzB74Duh68K1DPXp0j54X-S_bA-xj2TaWiEFEVXM_rJchN-2gyKjo7SbNr6ION_zokDOgHKgrJkkmRCIzKv6o9P78YCybWqjpsNTMLhz60mSFu5XPfmZleUQ3oDmNMke2ZU8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه رئال تو سی ال چقد سخته</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82658" target="_blank">📅 20:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82657">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بارسا بخوره بایرن بریم برا انتقام</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/82657" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82656">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-gunRMoXQQ76bGhNikUcrs8NfkG8zCIuNosZrjKU3Z9yO62-I7cqV_y1gHohMpWxVWfc1qsAGWYkHyg6yvHeGRLbyv39Rsmgnp4HRSzmyjWiMVKupF4EkQDjwzj4lcl7p-Qs3e0uo5xDzrOWuPBSA7ypw-CSrdJFVup4V899rqcqZmsxIq3lcCdL30E3puiT1uAJ1pzyRJvE4ESYmT9wR4i72gMBXeTz2fNSIHdUgOjhghEDZKiMKu4Sx_0rnjfe2z1-gHXOEwus74R25kTRUyog07apJec5kmF9l1-BGeh9xpIigFbJhTYSJ5G-Ez9mCHCuGmwzIwV8yFwDLnjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82656" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82655">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17918269ee.mp4?token=mODrqNxHJy8FZHiOvI-GjpKT42Z7HoOawOXWAuECEr-DQaYvz7AguL_HBrXHU4IllxiDfeHV6Pn6w_Y0tXn0_BsaiblFEaRnrRaYV5M1ITkNr7yrro01KOud09prcT_CTwK4nld0eQhcnIo33t_AvWzQD_5Km9UFe4IUtirRmF63g_Lzr__HTPrY3nPU5B7VgMVLkT0oyg8WdntRHN1BywwMaLxzYqkhcZfkLSx_w7UdhMlLiP-fhTVhuU-ZNGXWmYTxgdklc1kJrsT6J482VAzZzrh7HWLK7efJUf-HzqInKP0VIlH4_pP_yd3CW6Y9CTRW2toGaG6nzAJAbB7uAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17918269ee.mp4?token=mODrqNxHJy8FZHiOvI-GjpKT42Z7HoOawOXWAuECEr-DQaYvz7AguL_HBrXHU4IllxiDfeHV6Pn6w_Y0tXn0_BsaiblFEaRnrRaYV5M1ITkNr7yrro01KOud09prcT_CTwK4nld0eQhcnIo33t_AvWzQD_5Km9UFe4IUtirRmF63g_Lzr__HTPrY3nPU5B7VgMVLkT0oyg8WdntRHN1BywwMaLxzYqkhcZfkLSx_w7UdhMlLiP-fhTVhuU-ZNGXWmYTxgdklc1kJrsT6J482VAzZzrh7HWLK7efJUf-HzqInKP0VIlH4_pP_yd3CW6Y9CTRW2toGaG6nzAJAbB7uAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داش علی تو لیگ عراقم داره شاهکار خلق میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82655" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82654">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4APL6aRUcmDP6gVbj_acDiKKTJC2oVboswsczW3FlJTxbsAHtH_yNBNlDUG34DQMosRXJOgmQx1hyaaR-g___0nnZcihI8GcURxnshnU8np7r4JrR-P79tBUrlne7VUNONgc7AXR0ErMJJWLRV_HfzF9K65UGi3tE4H_UrZyVp6LsZpH5MUiXccDRLTMlNLmjdUySQEOvcqeSoZkbROzxph5C6kE4RscnFcdyHjrAzq4xxnMkKa6SIcx5ZYiZXXCxgtBzwCrOHIhaJ3bSwXSsVZ8P_8q_ta1yE1CytF8y9HvUDPDOFHQqt7Ett6fKNGrUKwfVjC9KhhbeGkQU5p8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بارسلونا
🇪🇸
-
🇪🇸
اتلتیک بیلبائو
🏆
لالیگا اسپانیا
🇪🇸
🕔
پنج‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوکمپ
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
بارسلونا
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
اتلتیک بیلبائو
:
۵ برد، ۱ تساوی و ۴ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر بارسلونا: ۳.۵ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر اتلتیک بیلبائو: ۳.۹ گل در هر بازی.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g5
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82654" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKd3pl3U49TwPI6KP-J6Otpt58Le9Le-6S_MGvbn-RSK072ZI6imvua-lrqvdCLNAUm2r4PcyHLc6qXXlMSkYzT_DSkb0CsBq99-zKWC8afTc_udmYvzdUg2f2-dik4W5dczNhlV3ybIxuGYc-WJ6A0HFMH-vFeYgMBzmUZ8nebgyfoLxA8MmG6sOC8P5eKXT54WFPS70rYphoKJtyjIPq7Ob9c2O30EkYtN4KQwJwkUqNUj6bYtsRfrUxALA9XFCeKmAAAt2h9VytVZdNdJHs73C9pIEJ26xe20w-deeoEok74VgZmvfJNanOQCYDaX4qmRlexPvEXiErgjg5ZTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این خیلی جوکه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/82651" target="_blank">📅 19:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82650">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">listen to demo</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/82650" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82649">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lNm-n6TiIXi7kBE0H5xINPSwDGS_ZZ_ztRkgJ_UekHp6E1wgjBzqesOxKdo4GRvI5r9gDK2B6Xoxua8yfABdaIrqsr8T6EYvjWqO8ObYyMDa1nNxNOSYhTYJwwTf2zltcqm6ATV02svR-pXpOLj0bun2Dj9uw5lk_yPefVJUqOkVYPQX6gQRHsl77Lj-wCT4PKolM7IgtYzAxXZAyk1vgFXHxoXzN7iutu9VKE42lGM34rD3PKZvehvFdHhvk__nORXr7QpaeESLvlMmpN9hO38UOQcSM7OvmxeRWDNTiU1L1dFpuKsTnR4jcPWZSw6KVXxvF2TmXAmVICnYUNgIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید زبر به نام ثاگ لایف با همکاری سعید دهقان و سیامند منتشر شد.
SoundCloud
🔸
Download
حمایت
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/82649" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82648">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6cb16ab0b.mp4?token=da1nY0Y_IBXxdUgYVI8BZb0cZOQlNRHhbWGtqosJv9HZFeEoO0POnoLhgPeXRzbIFcoUvgc2oHxwfRc5SKPeLE62Qk4hCKAGdd1azHix1rkLj7hfyOxkcSmmK-iDx11W3DV-sPLukzbHY2YGUQq5UC3q_bxxzDq7KA8KTa4DnZBRNZU9iJlx8TMCP5-j5T1I1hnUwVkFDiMKudfrQDPFySpSQRb2JByrqZ_6R1CCm_ueywYcNXobgGE4ZnBxw9vouYM_8s-wZmO1hvjx6OujN2pQS9cRVpICoTTqSx1PI-ymKJa0Ka9-4sfYGR_2qxCd13eTi7PHDjG1Itc3PD8tUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6cb16ab0b.mp4?token=da1nY0Y_IBXxdUgYVI8BZb0cZOQlNRHhbWGtqosJv9HZFeEoO0POnoLhgPeXRzbIFcoUvgc2oHxwfRc5SKPeLE62Qk4hCKAGdd1azHix1rkLj7hfyOxkcSmmK-iDx11W3DV-sPLukzbHY2YGUQq5UC3q_bxxzDq7KA8KTa4DnZBRNZU9iJlx8TMCP5-j5T1I1hnUwVkFDiMKudfrQDPFySpSQRb2JByrqZ_6R1CCm_ueywYcNXobgGE4ZnBxw9vouYM_8s-wZmO1hvjx6OujN2pQS9cRVpICoTTqSx1PI-ymKJa0Ka9-4sfYGR_2qxCd13eTi7PHDjG1Itc3PD8tUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82648" target="_blank">📅 17:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82647">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82647" target="_blank">📅 16:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82646">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82646" target="_blank">📅 16:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82645">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b53927e2.mp4?token=PJCLGtl2nDW3-DnwYd3V4PoryWTSzqVrzGQ8U4nIiJbkdYZeZ0p0qvNgWNke-I4DVe1yGig75GKJwCIir0tggfaAWbKRPWOgYIixX4sjlfsAlmomqAo_L1xch7lqJc--J5dm2azmbM9F9NPDyBTU2jyJLSJStc3Je_UAxPKIILs4vUrEsXq2ZRSq-eYNs4k9Lt6tzE4S9cqn3OLf-jr5AKkEh0pjfwUgwnSm_cN5LE0nYQWJRYr4sIdGurByQpxRnbpq7wKxYj-PWEYoER5hiyxlrfHT7PHqg-HXrkg3nikGqJX26VBnmm-aHT1mR78esFLotqvAasWDiDI7CkTDag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b53927e2.mp4?token=PJCLGtl2nDW3-DnwYd3V4PoryWTSzqVrzGQ8U4nIiJbkdYZeZ0p0qvNgWNke-I4DVe1yGig75GKJwCIir0tggfaAWbKRPWOgYIixX4sjlfsAlmomqAo_L1xch7lqJc--J5dm2azmbM9F9NPDyBTU2jyJLSJStc3Je_UAxPKIILs4vUrEsXq2ZRSq-eYNs4k9Lt6tzE4S9cqn3OLf-jr5AKkEh0pjfwUgwnSm_cN5LE0nYQWJRYr4sIdGurByQpxRnbpq7wKxYj-PWEYoER5hiyxlrfHT7PHqg-HXrkg3nikGqJX26VBnmm-aHT1mR78esFLotqvAasWDiDI7CkTDag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو برگشت ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82645" target="_blank">📅 16:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82644">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82644" target="_blank">📅 15:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82642">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSSzw5faMxt7hBDpCidnkoxCwHv6mccWzxWo5tzhqhTlLEMTppRsW9WNaVT8nNW1uPimz7P78xpEZbLDsWwzUH96fYioSSFCqz0hWE7pV82i_-zMafeX6B3LG67Xp875AswyQiIeeY_qkWY-OPXJo73_XMsS40Jp60ntf2tRZfy5vzhsQPjRjzEupg277jupguYF8qghqFYHN2j_jPcQu-dOLJFnaJta0kYmcV9eOZycVndXYPr6-1rO28hArmSL7tpkmTGmvwhdsjA8X72f7cWpp8JVORhf6aZo33LAku_RLHPOSNpCOFhrY5IO7l72_pn5MheghqVpRY6sq3152w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZvMiOlDOtkz_2zu32LlozbIp8NZXIStitWng5uHEGV8swLros6CgoKmtrPLtRCypsY2bPShaMAtEyc5jrcXCaiE4bPeHFSClkPnYGIw4fa2YDlqNMzDcMyOBEfSjmq9sFXDJU1N32As4Jw2MG8khbV9VaII81-mvrFlIvz0ASMJAAfGmQlq0QEPhM1k5b8j2eoj-TSFNFjaj3eWUmFSTq6fW-YoFtkbCS21qdKBlukV570v4nRMW22It7UkttQnbE9Rn-tNt5_TXWabXGOlMFs5Lff_2fKuly0VgVfF7-tARuzVMzDJLsAPQtkCQhBg3kXJfEUOPxTbV8PbExVdmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82642" target="_blank">📅 15:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82641">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d8214fc7.mp4?token=AbAGTDS2MtJNbGnqN7TThOBMHrvDjoh6pGzJB-2pUzQywDzQ8HwYqAjALfiRY9l8M6tpxLtEWNaHrcXdKGbcdgqBgB8cfvUYtighXTPyKIFqEH8yI-hkadc2zE5f7iRJFmQYz6swXuu2cVs5cwvBG2l79OOC75CUvpQcfUrvgvYCabui5JyLTIqnOzNVpoHlYHG4d8QqMEtboOVbrpOMq85TsppKAcoxyPhovvvKEVrJfeiHIrdiBp3o9CzKIuvCq0bghj5VoUsM3rzYXQW_t02w0pk2xRclZy9rAIvsR3Fq_-4SycJekh-8-WXasPwxLIT9p1aQFWyP_ZekCH8lkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d8214fc7.mp4?token=AbAGTDS2MtJNbGnqN7TThOBMHrvDjoh6pGzJB-2pUzQywDzQ8HwYqAjALfiRY9l8M6tpxLtEWNaHrcXdKGbcdgqBgB8cfvUYtighXTPyKIFqEH8yI-hkadc2zE5f7iRJFmQYz6swXuu2cVs5cwvBG2l79OOC75CUvpQcfUrvgvYCabui5JyLTIqnOzNVpoHlYHG4d8QqMEtboOVbrpOMq85TsppKAcoxyPhovvvKEVrJfeiHIrdiBp3o9CzKIuvCq0bghj5VoUsM3rzYXQW_t02w0pk2xRclZy9rAIvsR3Fq_-4SycJekh-8-WXasPwxLIT9p1aQFWyP_ZekCH8lkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82641" target="_blank">📅 13:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82640">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONJIybF0RkXFCp5aODlIq0Ac2kzZ1jDthQjXlqTHcKEz1GGwbLt7UEbBC5m_bvGUeQXUosCu4t2xBvZx_9BgeaN7LllsU0Bgj0aUlJ2Nky_BFP4q4ftAxkdEnNHXZ6OER7gqwiYU0F7zw4XP5FBjCOBaDxxAwHnkbzUcSJlVs8RlUL2FbltmlSHvJjPT093nPbcCzZdoKHt4Z-9lcNcjDEYQJUFbtgRLw17_qvxqWJZxzFyvYKOXAiaiZJtaoAm5tn33YlMTZWtkSU6ZwRf1dFMe0npjldprH9luie4ejx-P7GLNXhmx1EpVHEZwYp39cGrOcEDjsfXU9H7DXcsqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی این که چیزی نیست، پوری سه ساله قراره پک فیزیکی فیل رو بفرسته برا خریدارا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82640" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82639">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgrCBYphSZA88MsbLD3d1xX7vMK_Aq4AwWHd3z_aUVNEG_qReZJJhI1b-n8IWsPAZWD2FJhtW2jb4AX-W59FPi7yqekjwWeW5OjYStwEdb0OopcGnJN-HE8furqjPouLGuBmsbaxTGVJiqiphVjmREe-hfQKN9IQtRZX7GldsNuEmvEm6c5ZlRfb-92JVb-oYKp4vb-wfqmyOOGjPj8JLwnXZuOSmEYnJAVxpiGcl-FLy84yFRORheLtP-ivC-ZdIbz_jolGJwuqwi4rbOw72nnD0qJKgXg9yLt-XhVBGcLjgFi66ha6jiBEUe-8LjYxfSy69VJ74Of4QZXLZPV5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا میدونستید راب استارک تورک بوده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82639" target="_blank">📅 13:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82638">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سبک جنگ اوکراین خداست، اینطوریه که ما که چیزی برا از دست دادن نداریم همچیمونو زدن هرچی دم دسته تو روسیه رو میزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82638" target="_blank">📅 13:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82637">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آلبوم جدید ویناک به نام "Concert Type" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82637" target="_blank">📅 13:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82636">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGBy6oPCt6RjApUwYe5NOcVKr4bDcj6bzwVaihByA3TeI5QwwmN6rID5UvviyjWJPE3FqZZusmRCg41JwZR7PzY2wp8kGmLRKqjsDJh53kS1bzASJzc59aXtxWR2GwkQGBMF6abayNjRehN11W5e0hCcEFv0Zq4VK5jMsQNbEIdQPrhuVNZmPmP1f2A839ERF4LT-dA1KEt659D1YouPzEJwwzMUKgcf3926zC67IeBNvOOojSxSltnYcIvHC5uYKmpMaYBMajEgVgadXKEOXlQmMmB4fTR4Rxj3gNKSjvlYEjtGgOd7Fs-VPlxL5JG6_ueFO0JkxlaJ8JE2kMsnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ویناک به نام "Concert Type" ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82636" target="_blank">📅 13:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82635">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خدا برا ماهایی که تتلو ۹۸ رو ندیدیم محمود ویناک رو فرستاد
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82635" target="_blank">📅 13:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82634">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d048ddd9f1.mp4?token=EpIblSsy-m4U8lddWa6mx0kZB0-_USymWzzmttjm0p3qgTEjT3dHd6h29vIFhUxOcz_pT4tdFdHQdE88IbzZLVoNWsdnnehCZErGy4ghbo2hA01lxlG4mc3oEnGQRbtrYBFEsB93SypP-eP8NF9-j7Qm1tvzpJJdFSmE9ofdPz3XfO3H_f061T0d1irIjM2di2L9QOzaw-gQmbbJ758lzr_DQg-0PtoY6dO74dnWX1cLoFG1i2n_mrigtE1j4L-GaxsQRzmfV1SmBJB6N300ql2dLrii7FPxQ4kBg4zce6gEkbBNY5hDpycBNmy6D_420BtmUnQIhHQbl2IVbIMTEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d048ddd9f1.mp4?token=EpIblSsy-m4U8lddWa6mx0kZB0-_USymWzzmttjm0p3qgTEjT3dHd6h29vIFhUxOcz_pT4tdFdHQdE88IbzZLVoNWsdnnehCZErGy4ghbo2hA01lxlG4mc3oEnGQRbtrYBFEsB93SypP-eP8NF9-j7Qm1tvzpJJdFSmE9ofdPz3XfO3H_f061T0d1irIjM2di2L9QOzaw-gQmbbJ758lzr_DQg-0PtoY6dO74dnWX1cLoFG1i2n_mrigtE1j4L-GaxsQRzmfV1SmBJB6N300ql2dLrii7FPxQ4kBg4zce6gEkbBNY5hDpycBNmy6D_420BtmUnQIhHQbl2IVbIMTEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82634" target="_blank">📅 13:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82633">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عجب چیزیه پشمام</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82633" target="_blank">📅 12:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82632">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ویناک دیروز اومد گفت این پنجشنبه ترک نداریم
شاید فک کنید خب ترک نمیده بالاخره یه هفته، سخت در اشتباهید چون آلبوم داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82632" target="_blank">📅 12:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82631">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ماشینا شمام تو تک استارت روشن نمیشه و بخاطر بنزین بگا رفته؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82631" target="_blank">📅 12:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82630">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اگه پولتون زیادی کرده بیایید چنل بتم باهم بگاش بدیم:  https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82630" target="_blank">📅 12:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82629">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه پولتون زیادی کرده بیایید چنل بتم باهم بگاش بدیم:
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82629" target="_blank">📅 12:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82628">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبر خوب هفته علی گرامی و سجاد شاهی آشتی کردن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82628" target="_blank">📅 12:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82627">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ff60b305.mp4?token=BT3T4lb-ayzINHpKjZGRhjU0uUty1mL11ieDcQVBDnwSU5iAnPOlkETt7KPY7uSMXXOmpbtxKfoaZKz5Dg5JxHr8aW-219v3fHO5iBede1zET5cwndNcKN2NF04SK4Hd3s7hIqMUdRoNGyQy8iCR0iwAvOxK49ozfuzhwN9OIHuysNwwNbLCcAUcmlYfRP4gO8eHP2XOQYGbXwJlQeN1TaEz69Ioxai71s47lRmEDWeLJr0W5JHVNzePgQstlddvZ9iZCAUxRSplcZtkkjQWzLcNu9a7O3iHtOepLHsbC7dx6x7vWrj_s4rHOOTMPkUPhhwV_1i7WGfHdStRsA7n1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ff60b305.mp4?token=BT3T4lb-ayzINHpKjZGRhjU0uUty1mL11ieDcQVBDnwSU5iAnPOlkETt7KPY7uSMXXOmpbtxKfoaZKz5Dg5JxHr8aW-219v3fHO5iBede1zET5cwndNcKN2NF04SK4Hd3s7hIqMUdRoNGyQy8iCR0iwAvOxK49ozfuzhwN9OIHuysNwwNbLCcAUcmlYfRP4gO8eHP2XOQYGbXwJlQeN1TaEz69Ioxai71s47lRmEDWeLJr0W5JHVNzePgQstlddvZ9iZCAUxRSplcZtkkjQWzLcNu9a7O3iHtOepLHsbC7dx6x7vWrj_s4rHOOTMPkUPhhwV_1i7WGfHdStRsA7n1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوب هفته
علی گرامی و سجاد شاهی آشتی کردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82627" target="_blank">📅 12:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82623">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjvT03Emur6wEIGxzvNxFGaCNVUdpauDBTGUnauSMQ7Pazji2DmUwedMoQIERawB721S4jtvVu7YzH-hcxeswY8JzBeRxW678t4DZD_92EGFJqRQocC52ZembXQrEPgz6cmQqy57zWf_7mWVI7jkcCBzhbuTUbJ_MMaiqL6wbkz483pbpGcJPVlfB8kThTWeFgav4JPwZvkQH83auucKxSl70K1Vp7_WXj08e5c4CtlXZaZQVDSny0W1HuoPh8wuBQ2f04hW4HujVRHh7IXuLlY1Yu7ootfh673uQs6pBj9_3lxN30NLH7tWlEqoCyvs0lCMyD119yRvBSUqhuqe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmA4qkinAJSU1XnVUH097bfx1XL64FH6JUgLSxNRJJUbWtqY4Xg0azSYmggQLjkN8CKeia5Gat476LIZnls_5B-tUrZNJV7-ZrT_LEcrKYF3uYFuOD22-U7y0NYtIyJ_oSr-BcWZN8r8O3MlmYQ77EVWc6KRN90r1OXOCXJKUmRJXof2hT5YHJ3veib9evVH1nwP4SeCm6Qg0VSmbJCYKnhojW5HmcNSN6Cys9HkROLSX4KDiXw_fdfaUnFOc0p7Zp58o_DcM5PLvdq6k5KHv4QIvBINzp9iSEeYzKo-lBwIlZzdvzU37irCRL4gAVtCRoJjNLhNJGzqYCoaUsuOLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GM966592SlyU_BWDDSpFbhq7EB-p80A8oovPKLWDLX4eoy4C89l-WsuvYGwNcl14GjNmCqah4P0AHtDlCfFWqE2d1CfWpFwtk7AJ8ptQXllM6MAcOW5E8mYaQ422AsJUlR0eQKWvOYgE11OzNXKYSkF8lrpvTBRle0-i_iTd84yPuq5anYXLd0Xei2iGCtbOoDEJZB32elCPQzzCUF0lr5e9WYz1Bt9Kb1fYXUYb11uFD1gSDyXhZ-F7STdgBnrPM02Tv7faTIa2-A0RZWDJP0AmP-1PVTGV6ggyrdXv4ubD6D2ZurUbySezszMsM3wEoC6rsbUrttNVLUcLKEdHGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUS03ccx0xDJoWsC8FgM3_LbKrd7hkFIPG2W3f0i3C2y1RGSn_bSS3A8Bc7Ljr-PvbtrCPygAEXso3jZYjQB7ekv3O7Iop36FX0u-ygavtqwemEH4ocYPP5zWfRsdARZP4HUW0Qdkd9Dqu8meW6AgO0Z5AoRVhgq44djp0ppJwFfAYkQXUIiBtcZqq6eipLmToXtPmLj5XX4d7XNyJqtjnmho0x0ewmZo563VbBJXkVKFuzr1QgnKqPVEm7-dzirarbtIEvA3HseJ-lNMYF0iDGiwNdkI4m_4pY5CyzjJKCxrZW5BiDXx1dD_MdKZtVyn9MjP9C4EoI9mj33tfLlsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماجرای ناپدید شدن دختران نوجوان در تهران و کرج
در هفته های اخیر تعداد زیادی از دختر های ۱۲ تا ۱۸ ساله در مناطق مختلف تهران و کرج در حال ناپدید شدن هستن!!
همچنان از هیچ کدوم هیچ سرنخی وجود نداره و طبق گفته منابع خبری احتمالا بهم دیگه مربوط هستن و ممکنه حتی یک نفر پشت همه این ها باشه!!
زهرا متقی ۱۲ ساله چهار باغ البرز
ندیمه اکبری ۱۵ ساله پرند تهران
هلیا عین الهی ۱۴ ساله پرند تهران
زینب سون قوریی۱۷ ساله پرند تهران
آنیتا شفیعی ۱۵ ساله اسلام شهر تهران
پرنیان ۱۸ ساله فردیس کرج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82623" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82622">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ddigia8IQUI_kg-OfCx4k2LST23YEZdqYMVHlaQnkSRlvmhTSD0eu8FlFCo7rSxe8I3VY4zyJW7AQ2G6M2K_SmaCCh_5tdltZdeNkPhqwiKfTAkV2mKxVCG3AMf05QtpcbLjJAHfJSm7RoLfmHt8N3jEz5YzB6ZtDYqVd4AmrRyPWHabZu_tLVQnDhCJRqMMy4lYdsmbVR7Do_CIOk9EblrKjskPkn0hyLoMqNrnJHd27weFeKTpzv4UlX-bezmbTjHAq-o3BejRJozejl3L0-9LGQToB5xFWaOxhP68lJt2Bgk_BQhIzcTjI9_HMEMEPI9WU5EbHvIt_xSJ5ep6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بارسلونا
🇪🇸
-
🇪🇸
اتلتیک بیلبائو
🏆
لالیگا اسپانیا
🇪🇸
🕔
پنج‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوکمپ
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
بارسلونا
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
اتلتیک بیلبائو
:
۵ برد، ۱ تساوی و ۴ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر بارسلونا: ۳.۵ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر اتلتیک بیلبائو: ۳.۹ گل در هر بازی.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82622" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82621">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAacXX0KLYY3sIL7Y4v5qy3LD1YCujf-ClKI59wmEYJFIg6QEbzMvBxZY5QrdfINq7DG_wljKaBMzyi0PYxmjvEJlF2104ZA_QCoYbrAP2XKCobOUL3mbvqjgIR92ap71dF3oN6Hec66-z-C4cnn6BVt2xHnqHUenCbnLmk1ShiGLNqUIjq5DblmvKGucPnUxvI_w8hY3HfJ4_H7-nu_WWkOPEzci63YiI44LrPdBXqzlX7kP-6Hog9ER5hNXCJ7Q9NK6IiVvtafbF53T1uXbirPDjw3MPEyufSsov3QQfEmwAFzP2X4GDvKXXQTK2ROrAlE1DS1Z6hZ1fnQqe6z6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام صبح زیباتون بخیر. 8
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82621" target="_blank">📅 10:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82620">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82620" target="_blank">📅 01:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82619">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امروز 4 شهریور زادروز کوروش کبیر بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82619" target="_blank">📅 00:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82617">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">رئال جذاب مورینیو</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/funhiphop/82617" target="_blank">📅 00:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82616">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORlWT9lv7N7-F6Dhg7ypHwaNUpWiopSX37bSt-rRclaewnCg8eP4nOm2JVbmRNIYkFIQyPhLxArOlTvbb2qp3fDayq0yX4AIRtG77J7Pc0wn8j9GOcunsIA-gbegdvZF17paFzB8BosbWqpGovcrpn7bmgHkPqz7qIBWvgmNBEylJGqDeXT6qz_9pGInVCp0pn_GLuOEXodyo3fimX0FOlICXjLUR2m0oVgH_2BEf6Pj4kkWUpr_kV_dgYSKRS75S5cdm0-WqyW2F3dqhItf02IN_kW9Ji05sABzI7bz3AzRZ5hXXIKoGj4TO98l7wB-jkdGFCT1asxp34zxgqaalA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه خدا لعنتت کنه با این جوک بامزه و سکسیت، حضرت آقا شاهده که ترکوندی شیر.
فقط دفعه آخرت باشه لطفا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82616" target="_blank">📅 23:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82615">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNTzb2MeKNDDwsQjYKmxcyNkl3aLewQl5HHA_aZST7_LOI2i71VrSBfXFSVihgWj_dLGzCLw19mBdUK7UU_C3kzHMxi8Mw92xx-lluFiAX4H1LYcjMoSvnqQTjtVHTra6iHBwkOCgKLbVK-RFoPxRBHXtVk7W0Fpm59gEWwJ620qZPUyEL8XwxXMCzRPprvOYBM-A6r4vJTUyyNm6DvuJIpxUqlusSmn7zcHNlpQVKSmBUIlaXDHZK_ZdzN0VHBtDxK9wSsV3mUEPQ9ciN75946kyx7g9ZP6s_PUI0MtnzJjp2euSPal9O82bKSBuZIpaSBOyoHjOpsIGlOhVhFInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناراحتی دیامونده از بازی نکردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82615" target="_blank">📅 23:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82614">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رئال جذاب مورینیو</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82614" target="_blank">📅 23:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82612">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS8TE5Z1kTXBr3xNh1k0YjNpvSUISAoOp40HkjW_KlhY3NTQf9YUHIqbltCpXkei6Aw7hPUVaZwGi8qeUPi0bwiVOwMjH-PAtAlAPOc0odMPundvL52fPhL30NK02Bzq_dVUFkCx_lwQAZwvXRUCqdKD8rE_Zu3IaEx-NmhanRyrSt3TlFJRK64OZDREhfcKov_ohPwFbl1oqHkzoqPQxyJT74gIxSM18wMvMldHlZcDyMALrZ_l_sdfzuns3piXJlrylAACFGjeMen_uP4oE_ifNO9FWFsF-1QLN8QEonJ6NGCf7QEyk8IZtArRHqQBQmhW3igtNPW1HGYcwWhRRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه فان هیپ هاپی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82612" target="_blank">📅 23:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82611">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEGEFek0svVpD8mVzQsPfLcgIe-AzV8ZIs3Wq4R5skvdgQ_546pBXBxvRPCfRHJzfOZVGcYyEPWC-_yXCtq-IEFK5Uy0ISyN-5kwtoYabAQV_k_jGtWVSJhNBAhIFzyBGKEE5l-DGzES3J2gPNPwEZgyHGDEveMok7BgUfA4FOuER6KkesPR-KLTlkKA3hwA9mLS_XD-FTf6C_g7aqBJar0-tS1BfZA5juyUMiVtTbNv2z2pKjNpwL70Vm8D5OBWplNTv40aAg37cvncIYQXYHNNPRlxGlhF2F86WkOD8YMSh4ftrNl1GjHjeDtDNOHXD1OWU_sjG3PiiQPaOJ8K1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الهلال از وقتی یادمه داره سالی سه تا نوک میخره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82611" target="_blank">📅 22:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82610">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2pqBmKIVo0h3yWOXZ9cjhg87PDUf5quqaq2w9hmx9H0djTB6cQQMprNeYlZKwogC74ZwT1bVcWugH0Xn1yeY9aj098mVjyGYOw_Aw9uTCA9-V18ShmaoUmldidIAlcHXVA5mhs5N-iPvirdTf-m12Zg5n8bN2UkOzMGAkoWEDbhDZQpoyb1Y6kmvnpOIC4a15vtgZIy6jzu5ONeZ4GhqkYJwGwwqf_pXASWmBdVYkpFGtbiUECMI2cCGBvzH6CUVcHsQ6-8Hc_dc0NunftGzKQbEJ7er7aZ_XcDsklUnSOAUlQ1_TxvEHKKp5PRWq6OslrNTapJKbHiCwLWjxkQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82610" target="_blank">📅 21:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82609">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsOcfFPqRUqD4zzyFAVM3WPtaEjaBBdY9H4f_WNY9y2eUh4W3OmiXK0UizY3GSqzI1qrlRbWvSB6WSNYdfBPNxqpyyFGruN66zD9jjBQxnRFxzMKUG5NxALVf5HUHRcE2Kgt6PU3WhcRHUJDUu2v8fk6JkRLNlVkKr-WzH8qYXCbjav1uOpOknp_9gIE_R5JJnX9peLkddYnjI45MzG7Pk643TWWeGOTDX8hXScWN4m0LsYu5Oc1PyAjCGaZL4vg8qKRLGuCr7Qmwqjy9E478DCZ5gxVN8wl0ey_Ueyr0tMZEfz-OzL4dzaAKTbxT_xddccsIGRzpW9ItB-7yZ90NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس یاس چی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82609" target="_blank">📅 19:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82608">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a262ee6c0f.mp4?token=P6mB03VLSGPLkRYnuvs0IqMrT5ScIdoi82OtWp5gTyxu-CR1bHucRaJZSlzSwqOlmHo10xVE8XtKS2K-zIpLmMbeu4Fb8SR9jgGbG6nXAJaZje-AqLEpvoIcRVizObFFHfgmjboDE6wao-W12apQOjgKsDIGpivjmHl1w4EBF6MmXIsWCCjxkVfJbcUvN1qPRokkuO8Cf7qJTsZhZpbPaA638GFkFx_F7wQglyNPPPZfavKUsdZeBbZtdbaKdoc14HdBfSvxhYDlFQgzdJBp4Ru8uRMLP1QRwVW9KSvK9E6a_SnDYjT6USjcYZhUxkLjJux1OHewpHdUvBamTDkdbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a262ee6c0f.mp4?token=P6mB03VLSGPLkRYnuvs0IqMrT5ScIdoi82OtWp5gTyxu-CR1bHucRaJZSlzSwqOlmHo10xVE8XtKS2K-zIpLmMbeu4Fb8SR9jgGbG6nXAJaZje-AqLEpvoIcRVizObFFHfgmjboDE6wao-W12apQOjgKsDIGpivjmHl1w4EBF6MmXIsWCCjxkVfJbcUvN1qPRokkuO8Cf7qJTsZhZpbPaA638GFkFx_F7wQglyNPPPZfavKUsdZeBbZtdbaKdoc14HdBfSvxhYDlFQgzdJBp4Ru8uRMLP1QRwVW9KSvK9E6a_SnDYjT6USjcYZhUxkLjJux1OHewpHdUvBamTDkdbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوش، نیما تکیدو آزاد شد
❤️
💘
💔
🥵
😱
💋
🔥
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82608" target="_blank">📅 19:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82603">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZxQ7mFQZMjo1wXpLlZ6TtFQAd7XxNmwPp1gpv15EoXyDaEoCJvpcifya7tIGOl6zEAcauaHsb8tKXTpAJkuizUGYtlaXuk08EiH99mscsaY_w-C7qL0gHbDZA6eVBemj8tuWkiCce9ug52POTiQzK5W_5CF6k3WEaVgRvSny42zWYZHXrW0kaMAl5u4odGI0YQLhbTOKu38LdYQSst8Mtg5ZZfyI6EqgRe3wgm4SoBJM5z90gupsBhH_Fk6MFXU4X1eoVDCGsXtvd7xSMOxHz0RHAtRfx062fwCSHABwcaoVmxXsGrjpXs4XYAAdNlBApf6xMQqmDswvVZoP761pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/omlsPJfJt9i5fN71rZv_pb-Yp6X4eLeUxFsgUP730rWYqB_LduMGAoA3YGlSDhmANIitnDrXA65USVWaAXWPVZMBjBoPssISL67KTQJ2wpDYXnCJMgBywGGNSMjdgqSLbfbNHMZg-H0XTVlyiTIhiqc4xd8MwqJvARechYLE6oS4L6MHWLQieDuxuGxqbk_Wey6lLSN7d59XKS_wuLfMA7ZPRmomqZWZJX3E2gjwxidRTwVponyWAWQtL1Z8MIL8NseaCvXC59i949FYWC_WZYCYQjCdgOZGiPSyQ5RSb8hDX_JkLceRzS5grwnzDO-IJAxEY3nld_vEUzY8U3TLfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnmZ37fTTNCGL63lUIIdYNONsLBliKZErmNrNEe4xYWJWQ7z-vGFx0jb5_e_shFCs04Hoo9EYeGP2ac0QSLRxt-NgdyMfU6Od7VVZ8bK4zIr2XQsmiIo7cdg7jyLp_xBcVR7MvETF_P5rpt_aBZmL70GWR7Rq0Ufo84ADbgUfinMzVOsKU4kGXC_fpnYYcq360Yju_tGyFO1idMG9tICh9APEAMcLz8bQlREfQRm700cHuECSrjyBWJMowoHPepedGkfN7PWJv_wZ8USbdr-1lhY6_7imdUu-o5JVUw3mTptK8F_xNXBf_MTSyxhyzob38SY_FDWUWaYmlKC_HI0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsGmDdcgmTlBz48EqqX_MbSjpvK6HXb4hfgkq4ElvENjMwqgxQsrXPzbcAaLhO9MVhzKePKI2KyCHWmxmEX3G_SOAPL8nASWvLcIb-49dj97M41hnxLVHabJql8iwzRCS27o58gjn04wumgSWOpzvKqSyfBXXXGKaGnRTZd_5qeaemgNS1eg1w_yM9w15J0U1SlfuFUV7C6h5DoL4Qm9vJ0Jq3InoFlLiY7linUQjZXhsSMo81xDsReaxCI5cZbRpG5JTbu-3u2UMCpr2inNx9SvjMRpla6BS_UZa47ylLlYuGIXhN2sDzXPivEWa-ZyMxQGcJKkTW3EzYHA3BFbVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d5151d06.mp4?token=tzzpAYAMY4yQFEOAEVZeXbpDjBlJo3nwXoEDhicmkNHQFGUbLlSwm9M1tDO13flOjjDZ1Kadqaon1Jd5BYOpQzZaWSFaQcUzF02x6B-RlsFJ8-yiBeKXX74HnXHq9nGMXBQRvHlrijjkWc0VkLvlu3Tiwi1KHtJXwMfwDP3bDJOxEUQIS-p8Hkylv2qbil7VHVMZMNRJTqpzMHqQ5BeM8VTtkt2c_Sr0_oiE5xhHe-rbTPiXvDuxwRv5nn5rVR4kjZUgtrO9M1FQuad-Vcx6jTx-G8it8o4hc1ZhrcX53joeT-KEG46gfp3Usjkvp3k_Dya2lFNgkmelhmliZTQEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d5151d06.mp4?token=tzzpAYAMY4yQFEOAEVZeXbpDjBlJo3nwXoEDhicmkNHQFGUbLlSwm9M1tDO13flOjjDZ1Kadqaon1Jd5BYOpQzZaWSFaQcUzF02x6B-RlsFJ8-yiBeKXX74HnXHq9nGMXBQRvHlrijjkWc0VkLvlu3Tiwi1KHtJXwMfwDP3bDJOxEUQIS-p8Hkylv2qbil7VHVMZMNRJTqpzMHqQ5BeM8VTtkt2c_Sr0_oiE5xhHe-rbTPiXvDuxwRv5nn5rVR4kjZUgtrO9M1FQuad-Vcx6jTx-G8it8o4hc1ZhrcX53joeT-KEG46gfp3Usjkvp3k_Dya2lFNgkmelhmliZTQEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوش
،
نیما تکیدو آزاد شد
❤️
💘
💔
🥵
😱
💋
🔥
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82603" target="_blank">📅 19:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82601">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e5d7bb63.mp4?token=dcrdKW3CiGUoH8LhVoT0imMZqP9CfbehDEb3ms2a6TKBKj6werp8wxjjM40GzSDTjMFtvVMp-Pyhpxevkf70uXXgBJjz1xzG8vdPGtE8b2qn-OCMe5Oe9TWkGrFH4X9_yipS6SGUaArnhMG406wXjz0XNeF3h1qsWgTJMqBUdEb5a7YNkDJNCDniX8pLXBBuyAVsapsVHzS0UVe4a5HcHED4m-Nk2BMmHGksq3yyUweGYe4Qoyyap3KTpxQ9W4LL_MxypX1bTzGTuhDIKHJSLhi6GApctSvZoNEIF1bNF7jgjofHiezqSMbImU_jOy44WeeDA6vZUPwmcWbAemY_6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e5d7bb63.mp4?token=dcrdKW3CiGUoH8LhVoT0imMZqP9CfbehDEb3ms2a6TKBKj6werp8wxjjM40GzSDTjMFtvVMp-Pyhpxevkf70uXXgBJjz1xzG8vdPGtE8b2qn-OCMe5Oe9TWkGrFH4X9_yipS6SGUaArnhMG406wXjz0XNeF3h1qsWgTJMqBUdEb5a7YNkDJNCDniX8pLXBBuyAVsapsVHzS0UVe4a5HcHED4m-Nk2BMmHGksq3yyUweGYe4Qoyyap3KTpxQ9W4LL_MxypX1bTzGTuhDIKHJSLhi6GApctSvZoNEIF1bNF7jgjofHiezqSMbImU_jOy44WeeDA6vZUPwmcWbAemY_6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از یه ایست بازرسی بدنی تو یمن امروز وایرال شده و مردم جهان که زیاد با ساز و کار خاورمیانه آشنایی ندارن پشماشون ریخته و براشون خیلی سوالا ایجاد شده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82601" target="_blank">📅 18:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82599">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY-0r7YtxaLADRqAmqyAh-aBgGqCXAsL6qzplEARhRbnwWcxV2HTX7wJE_wk_jJspfLyZQqzxoC2pGmXxPB2wPQfjLtALxa2rHwCE8rMw6NLzaEHSA2gdcMdQlKOGLDDBpkFd4L78OU3u2TdmWdGRJT-3caA1-vRYybOm7y6MGxSmyId1pFliIpsQsBT9VZ5pMjrf2kDNQFx-0r6Qi-M1DbmouTJPA1flulk-Co685mYqVVdGqUuRJtvD4rCPdXFEmhKDoYfaktB_uv8zWBQOz8duMmbw5pQb4QMMqdrXd_PA_6ysgTTP34s2-XRaGH_DFF6EK8N0kEw-a6SWiqOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bE8b-8XHzfZHNq18uRuzqy4ji0BKWRhZtpIXfFDk4Td6vhxpHP3iyHT87EnyQ30bCElvnh97dnSGNfTGEOpG4ywmVjt8xzq899CSld4PzHq2BMy0RwwymCrMNw8w21pQVAHVIN2Pf7oDdZgcgJtOjuX1VtMhwn1RtGNwF3dTTczuz6dyzuKK_lXGgj_tdWWKajVRSyhH4vww5RUgMt9RYUpgXrZgqcVnyBxipoSCMv-ROi5t330RiRWxfBQbOeULu2hA89e73Um3so4Eb3Mk8X-qovc1LSgGuPCWekobSED-CAxBkAvz0c-BZ1LE1dA5AhD38s1NIwKzrGNe8R36WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هالند با یه مو کوتاه کردن از غول کصکش سفید تبدیل شد به کراش نصف دنیا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82599" target="_blank">📅 17:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82598">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قالیباف: مذاکره با قاتلان رهبر برام افتخار نیست و برعکس برام خیلی سخت و امتحانی سنگینه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82598" target="_blank">📅 17:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82597">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ریدم   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82597" target="_blank">📅 15:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82595">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تو کافه بابک زنجانی اسپرسو ۷۰.۳۰ سفارش بدی ۶۰.۲۵ میارن برات
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82595" target="_blank">📅 14:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82594">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efhKz5jv7pD1AJTgeGlMvnKpz0FNxDByKzed3X-Sea-ryPFcl3DP8VTirJPXzDZYeAW7MZABGEZIOPfzlns-xB6Tm8k2S1wE0fNR-T3ZQgv71BUbDuAiIh8ZsbF-D4JfTu8pW8Y80u0G7mSuLR8ZvgEXjE9pBHr1VGdsmEEls0co_4glu1dG3kSwxhTnORTPLPQRlh9hQ96IoICLFrQctqCOKEe3l143aUTt3G8wkVxOxKxJ-DaT06T-PDvrMBzKmAsaM9RBWJ5ivu-6sU20fMgZyx9GBEvM8IiyIMeqp2pxLqehfON9EKb_1OeSiM4l-ExnnCUUiX4Q4ICY-UyWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین و آخرین کنسرتی که تو زندگیم قراره برم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82594" target="_blank">📅 14:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82593">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این پیرمردایی که میگن روزگار خوبیه، ما قبلا نون نداشتیم بخوریم ولی الان همچی گیر میاد هم دنیای جالبی دارن حاجی</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82593" target="_blank">📅 14:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82592">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4y7zdo0L0XHQkySX6oEo8Mc_OY-DkxvcBZH52Uqsk65K2COdDZ0NlfYfC-aC8g3fvposyteo2n1n62UZQ3V08Rpmtm3_UNRmduajOIpA1pVtC0wNp4Xve8VCPOiiFFQtF2drF0KlZng3FHxePlV6cvR6NIEaePXHrkH0NZLBZwisyma4fqq41MNsLy4MYCPweYi1iahF7_LS8UBRWwf00PsRNQU2FAKrbDmbBD-y85YWo85cLRiqzWTZ1XpmZCcU6b_bOmqfMS6EsjnDDjifhpzyeXjfPXDPgCjAjI37s2zGPxjrcLGVNsY4ihmMjxl_oAPB0A1i6uYlTS09cVO0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها بین این همه خبر بد و ناامیدکننده بالاخره یه خبر خوب آوردم براتون:
قرارداد سفیر برند رولکس با تیم ملی فوتبال تا آخر امسال تمدید شددددددد
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82592" target="_blank">📅 14:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82591">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slooChB2tg1ciOrHCw3ol1k5Uhw6ZW-QC1sfwmU__SgmgoT-uhE3dpWqN9TPBG-RNStupziSHB4OEuvxMj7qdRep7inVIfLh4YkDgCteOuMTikHJ90pqGVIIzQCHSUjsMILzf-SqM_J_mVfs5hCF9aR_Vc55n9x7U-GRa2_Ri5ntfiTNnaZ254KqBEGuKLchEUJt49zwuxn5w7YVKrmtCJ_QE92ENvI2LwLvrT52wLd7QfIlNisXu59Lthsc3EuCjwPpcidJutnI1bvpOaX3iNNxCSlFt9ObAL96BAFKXYrn1fLD7__XVRoHZTI4ob-gJs0bgICk_o-1XCxOXPyT8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82591" target="_blank">📅 13:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82590">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ2y_ilkejANuDWOgMz1BVSk9wGW_pvnhIopVsBG7aL6xfOvPjFWhO7wKB3yhu3rBeuJYJB_cSb6P8z9Dg5WNoEiit9fey9AE6-5fXXEroo5nmPchviZCsQgN5zQqYEVY2lwnD2aMtwgxn43K9uAGr0mv3svUqLnTuUDyPG2jJxuox0Gk8STwSebohR6oeNj0m4KnYG--g2XK3nujQ_830YMNB4_5ps-LKho4Q8W_KM4M1fXn5R3PjHvOeuFNHtCvXEBj7JbPacXqASi94h-DPFuK44lQ4KzN-8ijpDtZe-X9s1c4e-0ArEOGlM_B_FRbD5E8aK9S9Q4w4NAbQJejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه تاریخی داداش سریع بیا پیوی همین الانشم کلی عقبیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82590" target="_blank">📅 13:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82589">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ckhvp9hLKSDu2hkCiPQmPmZxF-yHGTWlWT3R3ONHCVsEqETo8oGEGkasdAY91wPqgpeCyaNetH2GqfouFdDy9PY9DPccKUqpcF1oge7geBz7NetevTz3vXaIGBA0i3PQzwD62pEZwFCr4FeNcdgGC7duNxBMwE-3vTgjUttS-cHNMd960fKgrNIzHqBcI1rdDpaCcqKdPkNZpIuEC_Be523KY6lmV_pWBb9beoq-yeaNyMjBoUZB8US_FF5dPB4mmM_b5ib3KWld_A4f5lpr0Ea4lxNVweOaFhAvghYt6hEu3RXIR3IBsMmhcRmRbCaC00YbWmFsH8kS531JrtanYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82589" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82588">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQGOmTNpOLzpmshnas1UfCtJsD_wypGnnQaXedq63rpnOBXzwWcNzoWPmKEQTJR7yF2L3I2WifXZQrqAz63FKPd7vYyavDVlbBdvyHClVnx7EoQldNv3J44D4Wj3p-gcJR82lAaSKjUp5ZNDNKwNN9INE2-felMmOGelY30XYJvrlUFbgZEhBzfJZ6RxQ40K8MGOev0SF0pvnqapP2fuPMualQiIDjctv-_NeaZPYN6x9f2KA-WdPwGizGYcV7zYBC7-f1Mw2gXBjB1r-ZKwggGaKEQOTgMLFwAaAf9gWn-V9kxI8gnBsn8SLqGLiHXsozl9MpBIElh1A6ieGtTxxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82588" target="_blank">📅 12:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82586">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef19c3dd8.mp4?token=EdGCbkx3btq4WYBRoZZgo_mph5lehjF3GKE6_ldtZ9BnjEEanoM6J92Nsax0Y3G46EEo1UiFWw1QrJBNbnaikb0B60speSBdEIJkjbYQLT8yMFUW-XREKp7X2ixgPZUCZL6ErkIZD4864pEqkSfFiaT3I2QnWygq1DHsm0cKrKTjcl_gIXPbt3eY32be5C8FVLMIQgxahc0Jy-RQK5iYU2Ys5n3kWfqS2zRCGDjt06o77P7HuwgspXPdDN7g2_j1ri4Y80KydTvvOYicyK1iW6n9Ehg2l83y3EC5gVNmalW2JmwbvMZJzUB5NJj2JjuI-thFcJoyknhlk-ngsi8CDFJC0uoizT02V-FqD1hryegBfo2f0ewjuu7J4LhGaKmD74IDCmxwf8w7A8GNqcQLcxixsW0dxtaSf2vn6iyy7j5aeAczm6e8Mg530ReVQxjateUfIuZxWJWqUwEBk7psDhXHXOxq_BMz8P_aw8sAz7SBqJ0GFnKZyd3FeZt436Bw4JGJFQFzeLYdoamUMANfAxGapJN4Hkk8zaQa3_06qmEAa5T5o08q41MEQPooVRVf76EsPxNB_M7bJ8Vl9fWX6ZMTfnB3p3q_oNp268xWe1JB9osMDQoAqIX6bob1BLtcdGdF3-69ZzuX8U3E_27KSwW3iOqfHXTA0fBaxtULGm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef19c3dd8.mp4?token=EdGCbkx3btq4WYBRoZZgo_mph5lehjF3GKE6_ldtZ9BnjEEanoM6J92Nsax0Y3G46EEo1UiFWw1QrJBNbnaikb0B60speSBdEIJkjbYQLT8yMFUW-XREKp7X2ixgPZUCZL6ErkIZD4864pEqkSfFiaT3I2QnWygq1DHsm0cKrKTjcl_gIXPbt3eY32be5C8FVLMIQgxahc0Jy-RQK5iYU2Ys5n3kWfqS2zRCGDjt06o77P7HuwgspXPdDN7g2_j1ri4Y80KydTvvOYicyK1iW6n9Ehg2l83y3EC5gVNmalW2JmwbvMZJzUB5NJj2JjuI-thFcJoyknhlk-ngsi8CDFJC0uoizT02V-FqD1hryegBfo2f0ewjuu7J4LhGaKmD74IDCmxwf8w7A8GNqcQLcxixsW0dxtaSf2vn6iyy7j5aeAczm6e8Mg530ReVQxjateUfIuZxWJWqUwEBk7psDhXHXOxq_BMz8P_aw8sAz7SBqJ0GFnKZyd3FeZt436Bw4JGJFQFzeLYdoamUMANfAxGapJN4Hkk8zaQa3_06qmEAa5T5o08q41MEQPooVRVf76EsPxNB_M7bJ8Vl9fWX6ZMTfnB3p3q_oNp268xWe1JB9osMDQoAqIX6bob1BLtcdGdF3-69ZzuX8U3E_27KSwW3iOqfHXTA0fBaxtULGm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک حرکت شاهکار مهندسی پارک لاله نوشهر با ظرفیت 10 نفر افتتاح شد، مساحت 307 متر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82586" target="_blank">📅 12:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/090cf184a9.mp4?token=e9tQkVKcQLehh6B2PO7cGlxRah27p_0ZMDpin-zngbBM6lDdAOD7UX-9S1k50F5BRXfl8rL1oY7yDa6dyLgYnyhijHGIrBB6qFzcRJc8I33ZMRLKwy9aXy0WoEPCR-f2GTcNYArn6SAuLEfo-FB0rTmGgIWj3ygyBNJcQt5JcQBsYVZTAEV-HFBI0W8jjDKVa9q72NYTyy-uf0liOza3G1H-YrE-O30kjXPjxgNAWhd69dKkagSl3cIUD6St8PCCVxDpwFzhWMAdNAdBvKWPbSIMd9z0tPoewT01L-6Ah9mZxNSRHOXPvCzLBimbDt1ZAcdvHQSJ9zvrrJiMLYoOlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/090cf184a9.mp4?token=e9tQkVKcQLehh6B2PO7cGlxRah27p_0ZMDpin-zngbBM6lDdAOD7UX-9S1k50F5BRXfl8rL1oY7yDa6dyLgYnyhijHGIrBB6qFzcRJc8I33ZMRLKwy9aXy0WoEPCR-f2GTcNYArn6SAuLEfo-FB0rTmGgIWj3ygyBNJcQt5JcQBsYVZTAEV-HFBI0W8jjDKVa9q72NYTyy-uf0liOza3G1H-YrE-O30kjXPjxgNAWhd69dKkagSl3cIUD6St8PCCVxDpwFzhWMAdNAdBvKWPbSIMd9z0tPoewT01L-6Ah9mZxNSRHOXPvCzLBimbDt1ZAcdvHQSJ9zvrrJiMLYoOlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو تروخدا
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82585" target="_blank">📅 11:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82583">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmVOHcAYP7jXhsu8HMsDGydC0bj6uQjNqGNRitrPu5YwtmyLT6TpiNQ-vce2VIBHeGovwLzyJDy_x0u0O4hyNfuJIt-l84Ld_mNNdnTheeOI_X9iACaTbEsNif0q851r-ZnpFamMDXisNOkEFUitgeRw-dFi04ToVmwQI2vNcU4kp-TPL3MuaLXJMjuzsgPVF-hljPyYNwpwPLYxAHH27eAbdWqQM_pUFWhaW1KrPbQudK9_bGbrETOnNKL-xBLawQ4Ac8n_Z3ePWlviXJ3JIQM5H-EItLsEFpH38pRzrMHa_4QOy28HF_928XPWBDCZB4YgYOpNoNxseXY61_Iemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد خیلی بیشرفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82583" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82580">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuXBeMICOqzJJ30_KdySGvlw6-pZdkqtryB7yWAy37sqaz-6GcYua7_hvQhOjxZNrutayEqwMDsv3YWnv0wP_sqZXo-9mjbxqs1opXpKO3nl7IwoCq1ZTK-ZDdDN50hgf4FX5p8BObnUq-GuALlk6scFQJBByDj--dPyxrwtT-UpRaXWMtMxt5b4Dr8tGEMDH6F_JrDCWfeUCoIg_DyM7fh3gfHzMlwLhHHurfo2XclWAbaa4SnCfCpNYdMT-asI948Qw6M6iuEV9L1FVzsRZmx4_yTiY86PC7xPMGrjM6PGc_JX66BBCgptchZC6E0J1LtVAIMGMgKQqs4C5WYzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMMgnbZfxB-4aR7CzbUTeurwdDSGeLPGTWHDPYQ6uREhhKxijLwNePkTIqYafSaU4S0kwxyg8s7UxJzcW1o67pNBvzzPke4e9A6a-saTD0eiWJ-z_B84IAS3qOE7nvgx1GenkRafYTXBGXHKvLLmNxTF7g7Izd_rPWN_VJSRFjPw0UztxNc0QZRfZcDOfbnfQyqHUoLPPveYkpbno0dWi7fmOYV2FJzE-73FAYmGc-r-iMIbG9prz7rk_lN-SLeGIW-X6eQsxfM078nCjQ0DmlE18VRCBU90mBcfXDL9SR8EtEpqQwqZY65IgwPCoH6ryY-5Owzwzyp-qylYG2d1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rr27QLj2anW_B08PpT6snbP71cag8f8VDjMWetAkCATxukG16PmqBrbyqsXWeuFk0IY2gRpYHYgsC1CD71vSOtkDI5vLQR2jknsQKleVVfPovuAxeWn7xtMU3gYPO0sxJAUOXQz0uhjXVgiF-C1LdME9RLGOcnqtU8eyoVqX16aoQgrjhvVjhYWWPrBs_FpRNlf_JN0QZWs83OUpNozt_Ynwm6woILqiatpSzlYlEf_Yfu6MiulgAylr8HOIhgKoT5R18Df-Ysy9wbGQKElXLvVPoN_kFep5o0v-Qdtq7rNXBC4FhoVDYx0ZdvspO2RwbBxdzR1Y5lHSEtRoYhTCow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تو عشق ابدی ورژن آمریکایی یه دختر ایرانی به نام پارمیدا شرکت کرده و اون ته مونده های آبرومون هم برده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82580" target="_blank">📅 10:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82579">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbIMJvuGvG9B0tRdH8f41CQZekd6fStangfntyZQnmi4gzF7MXhNPt5023puE-VoGY8EvR5cCe9z9C6ZVLT2bZ80L7RPyUIisF__KyUwdsfIOsXo0M9xe2BHlIjkNLh4qELIjei5CLpgcDCnZ-1MBipQcGC8HAMRO_6kFor4Gb4K8dpgTHMbEb2fYsbTJHfuFTLYlhA1x88k9Xbsdv0nsJf-C8MssGHsj1kh2kzA6S4ONXADDPv625X0u7Usc51Ob0QTOgve6XcDs8dL-nd3i7FUJ1p3kdEdqHNR_wFnc3kbWPxKQZxYA2hfbwPX9XaRNQ1qLnF4Y7RWEQdUxSQo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو وقتی تو دی ماه ۱۳۹۸ گفت هر کی ناراحته جمع کنه از ایران بره دلار ۱۳ هزار تومن و طلا ۴۰۰ هزار تومن بود
خودش سال ۲۰۲۰(۱۳۹۹) از ایران مهاجرت کرد و الان آمریکا زندگی میکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82579" target="_blank">📅 10:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82575">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnO1U6UdonobWDrUOs5Hysa2CE2XOJu-qCKQkyZGgTDOvB_KZAnTIpLKuZ9jRyDbLqjPNIk_pdN2RcoMqQc9wLu13zMDsjZbOtj344V4oe_jdTqLgJp6z74rTmWOL4rsunaHLasTqG7d4uL19-s75WxltM3OC1CL520YNUFTzMSy3yZteswsknpxMaXLni_dJ-fIcqK5X6hULSl2OG0jCyhXdOq5Nbni7PxyFCi3UKI3vcYJhX6-GXkosR-PPcqBGHePBIGZOrg4-ZhrQl_Eh4PEp8K9h1mE0gjzhbzPfWs5aDOaKiabfxkbRjRgp9ZHtGT5ovQMCjAbe0JkTUA1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو میخواستم ۲ ساعت پیش پست کنم منتهی برقا رفت نتم قطع شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82575" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82574">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpKPz_BAEitCzPKONfuu1ytSMtO9ZloPN2Uvhcy5sNJY2wQkOv57YKQf_2YYu0szckcEj_3DdgPDyeIg0yB-DGzZiTSMVnpWGnWk5yC4ukrFIvvzv5NR2YiLZRHjVBGA59_o7by-fvXFy6QWgT-aTRrLdnu_IdKHxOViOGiG8OyevTXH1VrIH0LCfp7DpDqQ4V2kMH4iqdDstQuCtTP3iDBqpdNF4kkiEJSSprh-oUR-60EEqPnM6w6U6youfZh2rl8bQZsXOtHjijxKGo62CbVWBzTQDRVgzRIwKIfu0f6o80qrDayLSno7YOFwUfyQuysJCps5rE1hnn4P0x34EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریر تلخون تا اینجا کلا دوتا نقطه عطف داشته:
یکی اونجا که فان هیپ هاپ تصمیم گرفت مسخره‌ش کنه.
یکی هم الان که خودش تصمیم گرفته از تیمارستان امین‌آباد تهران دوست دختر بدزده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82574" target="_blank">📅 23:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82573">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MINZQ8ZVP7nnkkk9xOsnPWAeQXyXt4ol6Syocjzv_lxYeKxkzix8HIUfX1XQc_eMG6TGPapFqpjMLjTCv1eNODgGg_zMKORmQgVi4-4tx7x_Wfef3PLDn0RADw6zp2qygAr-eQVrjr2lV2iED75wxsSQm9J4x5MEZfKSKU0OyKlCQXBrw5n2yLgtPEII-I00p9QQbjFMt5XhjqONUllodOFotCQQO4CuNQPe4R-cLD7ruFG5p4K96Cu_EHuHLPCq5gzjDzcqieunpvgcooI4OVooWNOsb-KWteV0fMaFNdSL4U5cWaQM7j_7YE7MYOB8Ohhuz2UFhAehF6QjMzzK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهره هوشی اگه عکس بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82573" target="_blank">📅 22:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82572">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d715zL8hPsabhPWVn3QSF5rA-q0wZBkf1N3IPWN3z8gJ2rQfHynPUUOQYFvAxp0FgerlH9gFRHw4BpK3XyepY2wQ9kL5LC0OkKKtS68GiPBqMRB4Kq6HswLLHjxd36bc3AjVXFd6om-tJXOsLHz4weFbcdqBdZX-Ps2HD-Y2TjTYrwqBGkC5fJ145P6lnu5skotiEsGHCs4zqNqGMAXhcHVGrvL_kCN-XoWhOL7aZbYaVB6H3IUGV0s0ZcoPUEoxDd6oybbGOBwkxgdyx441z2e78DqLfBbt6_KsINoNyC3zSviUfMiLHASHLubB9vwYsB31W6yqvuEr7egjlaTJOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82572" target="_blank">📅 22:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82571">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترک جدید داریوش تبهکار و بیگ شگی به نام "Vice City" منتشر شد.   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82571" target="_blank">📅 21:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82570">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOnZ87ItoY4ulZiSqAB0EqucmC09PjWpQ2ZutNYORq6FMX7mofqj30_XQJkO0e8Slbj4dZjNITUd-YyFBEzWTnGlh4BJVFtCcT4eS92OXV-yIDEWUEgaoquEZCN54r31WAe5uk72Ryfimbje5g1KpkNS3xO_gPtgfC1pzalUfFEppPhYFqZbaN1wnAgQfY77ybenqMi0ZtNZ0obKD024wJM5bTdA8fYi5pTFNTCRI4d1gVrUTKiNJvINgo3MBVuM7Fw5Cf1pUc3-k3AldenakheaXPpPCmxFsaxj-WRjQatG4FgWnoI31cUw-iWNL7TBdk_8W1RHhSgMYUDkEfBm9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید داریوش تبهکار و بیگ شگی به نام "Vice City" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82570" target="_blank">📅 21:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82567">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49661a4016.mp4?token=TVOd_Vy4pg7LMCPo4E6F1IamCRlfLuJ5Zb9MMfBBmR-abXfMndABShvLIQ4VeCjRKGToP-JbiVk1_1yDnuNdDAi6vRKlzpqD7Y-96pmMF74wjuUT6LekKW9ykX-ZcHZYGEO6jIOaDLC_rRoA9Fx7oLT5BuWGhYFRp2NkVyAK_VOIBZdyBcxq89BpEwRWvaDRqfKyffy2hEaT51c0TTTJqZBjrZn4DwZ2uXHn7WEGeuAvLUG9TGP0Bw5lQdABIvfVswwu3UFyptzBsMSh-yREw-XPGtdQd4ZMJMKoO9UU5PbwhV5MNtaoJUWcnh04kuMbDu1-XW0mkEprYo-0bvLeIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49661a4016.mp4?token=TVOd_Vy4pg7LMCPo4E6F1IamCRlfLuJ5Zb9MMfBBmR-abXfMndABShvLIQ4VeCjRKGToP-JbiVk1_1yDnuNdDAi6vRKlzpqD7Y-96pmMF74wjuUT6LekKW9ykX-ZcHZYGEO6jIOaDLC_rRoA9Fx7oLT5BuWGhYFRp2NkVyAK_VOIBZdyBcxq89BpEwRWvaDRqfKyffy2hEaT51c0TTTJqZBjrZn4DwZ2uXHn7WEGeuAvLUG9TGP0Bw5lQdABIvfVswwu3UFyptzBsMSh-yREw-XPGtdQd4ZMJMKoO9UU5PbwhV5MNtaoJUWcnh04kuMbDu1-XW0mkEprYo-0bvLeIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Mews
🗞️
“ NITROUS “ Don Toliver’s New Album
Coming Soon
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82567" target="_blank">📅 21:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82566">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024532bfe.mp4?token=JW8TWir-XO5unMzBRdc2bp2NATxrNaMDAuryP5EnvSkEyPgs0lVCGiH0dyF2hOBgaL2NXgJjjUJlV8BTC_TXGfssA5b1jrWGTuWwW4jU7wr-fff0OoUpyUUaUpL2vxEFVpKAuiL2LolESyfNfy1gf6Ejx3iaohios_PNZO8yoUAW2d2lG7ttCT6o6qDYcCpcxx7L3J0-ZLMcBGzVIKkthVfX80YeG5LlsaclrLn1TvJumRqEHq9puD1XUl9wx24WVPCvILIrNDdot1HAabKFhhdEMk-V8U2v4o6rO0o0PqKXF35JzbjS0Flid7JY6pfXRUeWiX0BLbDsbPyxH7hPsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024532bfe.mp4?token=JW8TWir-XO5unMzBRdc2bp2NATxrNaMDAuryP5EnvSkEyPgs0lVCGiH0dyF2hOBgaL2NXgJjjUJlV8BTC_TXGfssA5b1jrWGTuWwW4jU7wr-fff0OoUpyUUaUpL2vxEFVpKAuiL2LolESyfNfy1gf6Ejx3iaohios_PNZO8yoUAW2d2lG7ttCT6o6qDYcCpcxx7L3J0-ZLMcBGzVIKkthVfX80YeG5LlsaclrLn1TvJumRqEHq9puD1XUl9wx24WVPCvILIrNDdot1HAabKFhhdEMk-V8U2v4o6rO0o0PqKXF35JzbjS0Flid7JY6pfXRUeWiX0BLbDsbPyxH7hPsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی حاجی پشمام از نسل جدید ناموسا اینجا ایرانه؟
😜
ناموسا تهران کِی انقلاب شد ما خبر نداریم؟
😅
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82566" target="_blank">📅 21:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82565">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb65d06f1.mp4?token=Xyvwef9_C2CTVoq7vGhAYvy1z0avIaE1j17xMGlaVkMcACbFFy-Fl-0Rs1Yre4tA1FnNWW01XgNe1ivX6xMEO_zoSCzApUanusfkC3ns__oU9ijjTSYcMPkc996fQd-SGOOrq_GPm5rsh0Zn6oDpOnB70XuDt6y-SModwg95y0K8fTnpL9yoYS_fKVXPK4loTpbfwT0mcOOddDf1GIsD8B12jO79r0q7fMCjBhvYU16SdbJAAD8rCdPKXWmLoouQzH0CeIyNqAEvBZgEiKohja9qb00jIMyC80-ja0jYdxKyLXmFijWsvyaf3ZUq40inHYV9WgAgKMe9GNwHeEj7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb65d06f1.mp4?token=Xyvwef9_C2CTVoq7vGhAYvy1z0avIaE1j17xMGlaVkMcACbFFy-Fl-0Rs1Yre4tA1FnNWW01XgNe1ivX6xMEO_zoSCzApUanusfkC3ns__oU9ijjTSYcMPkc996fQd-SGOOrq_GPm5rsh0Zn6oDpOnB70XuDt6y-SModwg95y0K8fTnpL9yoYS_fKVXPK4loTpbfwT0mcOOddDf1GIsD8B12jO79r0q7fMCjBhvYU16SdbJAAD8rCdPKXWmLoouQzH0CeIyNqAEvBZgEiKohja9qb00jIMyC80-ja0jYdxKyLXmFijWsvyaf3ZUq40inHYV9WgAgKMe9GNwHeEj7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرات حسینی تو ۵۰ سالگی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82565" target="_blank">📅 20:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82564">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSB4t1haJobShZkCSvP8xIEXTYwF4f3cZ3S2UMPLR_ymPk2Psn2JMjrdktZMcH4lIy-lxYjuUGLy8aGX-_vxZGItWCJ-lCatnwnSY5rwJzmRcxoD4rK7YmsVMVzyC1HIKI8RYOKMXEy3f_vsXnDv4Y5XBnABgRtKAGvXPhKpdUGI4R9if1QWwG7bI51TekPP9XCLG3vkbXcUbs9C4mF1exky_BpRutzciHYwoYA5KAxfjZsOmiSxOvsotpu1hGABz1zCcODWu-nKRkCoX5mGFQsqdnAORPf5gQQfyW-dgoj56UEsXDkgkrmk0JGwKN8-O158sk5n9TYjoUeVF9JIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل ما از خارج و تحریم ها نیستند مشکل ما مسئولین فاسد داخل هستند
اقایون مسئول خجالت خجالت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82564" target="_blank">📅 20:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82563">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانال 14 اسرائیل:
ترامپ به تهران دستور داد فوراً کشتار مردم خود را متوقف کند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82563" target="_blank">📅 20:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82562">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">از زیر این توییت واقعا گیف های شاهکاری پیدا کردم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82562" target="_blank">📅 19:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82561">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-i3To1m2GbQ90PWXroSvPHM1U2WR2bovmhCymP_UCvf9Flp7_j6rVWkg8WQnkMhmFQd3zWrwlfuUE1SNFNBl9alk0Rav_kr8avyW4JbZ1lXCUZb4zx2EyOLZtuPc6MIpWlIzbckArefQU6JaSjN1XsthZsHD-WEftEt_8ZYe1VYryOVky8Txy_xs5gkKtCX1GJIRJ7n-IyI1ynirdxeFXmbx7ix1OVdXOKu15Br768OCFXnSISYRiiuZ6e3HW1DfTWSPF4k4pZjBQkgrNsVJw-onyjynSClco0aDqkbUsSi6FbcEKGJzpGLSXjUlrmIh6kY3udjbyJX25zXo1zLfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زیر این توییت واقعا گیف های شاهکاری پیدا کردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82561" target="_blank">📅 19:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82560">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe-nUJAtJHgLxwirJRXGDQX9Ra4I5EwmQ4s515NcX_J98PsZW86GlC75yqVMTvlgeACg1pb8H2VbIXFo1RrtroCi1BiUI_e5iu57RIaXbd3Hr3lTrkFBmZwEaVW7NEz5eVW-LPDtlv5TVlnOIU-CdGhBTRlOcAFOuRwEffee4r0H0kQtL2lQPjuh72ixt55sms6HNlENhF-yfndc3-XPveSy8qN1PcrddFwV3uAXkWUYs5IS1lHigGtJ8Zo2ixLWOtXL5DKK5SykM5wnbmCC8qzjBpgBQ4ukZQWHsl3W9kf5YylDJQUoqRgsR8rPUN5w29zHKBB91fxPST13cOoT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرادر آزمون دیس ویناک به پوری رو پست کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82560" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

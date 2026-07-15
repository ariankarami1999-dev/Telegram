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
<img src="https://cdn4.telesco.pe/file/t__wUD5960hfXh1yJzC1VboECe33bVVc130ScU6CzuLMnVPSJ1z8_IElWBps-Ya-jwkz3N-gF55iFyySrQSHJFl4XnWK8TUP-4TV9B1FXWUozqNLN0UW1BiXlXh5PvDY5i5FzPrCUgGUkInFiGcjmwSpJAMMfu5mkyOl3ixhfmbnYSOQxh77fdbFeexTdvgRUGl-n94PUl_BwykOCNRB1jqTfl7Po8aY7OU6oXwjej0mMqQdliB4KoojOuPbKyuq9gSEQM0kJd76mINUPOWVbehrU3VzpVl3nqFsi43_t1IPketbQsb3eea_J0a-UjZT_avp9lx1MddaDI4GNRWb-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 470K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 23:34:48</div>
<hr>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsO6lWmlYZx4vdwgs8XOQVhfchS6Wiic4AgtgsZ6NWvuCRKcdOy0S6koCXrb42IRQB1H82WjrZBtmLIis9QMXUr-aZ6vYKpjJ9SbFijK8nCLfkkF3tG3n5GQQz6Xzxbul7nrGdopeWQK950XqSGghN8sXnB_L_uuSLqEdb-Q1_d4b-BM-5x8b22evPSwGbzEGQB45pp2_MjWnNeDEksXUve5ei6BPTVMb3POFfDUii8C1XzJKp8lIdxsdFsuS9gTlLWgUQ368MrIvwJMXBW5Ekpgl6muz0_4_CfznRXi_FwnIRCsHoI7lteWG5f5-VkFBDE0xrk40QsQycJ0j1jEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8axSPAWzmwnKQsPI8bjgwlz7mRCIBI8h1AahwzB4TgQqMFA0J7X0HPlefynVvM0MO7Dp4AG1S24QZnNT1chsIwk0zmm4OKGOZWWINraGp7lO22A32TjO9qfIOoNGr3tckeaS3uG__bBYw_hYpn_SIqzI9TL2zS6BPc1S27pCMKLYIKeVw2sRme9zyu5Qib8ICh9F-DPVjobFAo3vA-zNxf04aQqSajM_DaJVrtD6E3B-3T1Or08t1mDILhAkX2ZC36i79OTz5wT2b3OVEfaNoNSAgYjEj-3SSqTgzseQPffPCr0uh8a-k_mcS1z0BPoeJ5fMolOQqJfs8OoYZOmOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=uXY9WxJ8pgG93CTLJ8KturRkXM2ciqaRwYIcIuFeYb2BCIM1XKirXL4xT56-ij2GOH49jB0bhKXzIHLgI5r-uhp2cdSVjoJNXeP-WS1boWZT_lXgmIb6DyuSArQh3SBuyEa0abQdnUUeenm-1zMQln-IWexMXWQdZ8X5l4IjqgnmXz_g8jZ5knKA6X20kFkTy-V3PAL9ZWqo7M6B89UcrHiqbleGsR3GHN_1Ul2RnWqP2NniDtsRureg9dRV3cMR354_0XkYIaqHLK_e945p4LZGbxJfU0AdDO94MwGU6UVP--dULRsWzCl6jeF7ewY5aEHy_F-Jt3B6FIgadYo15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=uXY9WxJ8pgG93CTLJ8KturRkXM2ciqaRwYIcIuFeYb2BCIM1XKirXL4xT56-ij2GOH49jB0bhKXzIHLgI5r-uhp2cdSVjoJNXeP-WS1boWZT_lXgmIb6DyuSArQh3SBuyEa0abQdnUUeenm-1zMQln-IWexMXWQdZ8X5l4IjqgnmXz_g8jZ5knKA6X20kFkTy-V3PAL9ZWqo7M6B89UcrHiqbleGsR3GHN_1Ul2RnWqP2NniDtsRureg9dRV3cMR354_0XkYIaqHLK_e945p4LZGbxJfU0AdDO94MwGU6UVP--dULRsWzCl6jeF7ewY5aEHy_F-Jt3B6FIgadYo15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25798">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_yKkza6KYFUfJ1rYTlitJQbmASfdIkQo509TR7drT48e45x-DjibM38TsbW1nX989xXOwLMEhOFWJ2yy5g8bfoqCIKtiN2-MqteOquVC_-FHkNfj8Bnj4oGjp_7fEoDXuO4jrUfxPBLg2WiU0sjjnYes75ejmRhkHt8RjhrXjs_l7zlBzyBPrpBSnQlVRzItiRVtaJSAWgM2fqbMqiGDFrzchJjh3myGTzwlUouTJBjJKi7b1GqHUP9uqgOJc5yfIQWM5q1oSAzL-KOGc8S8g2vLq492ZFKhWfeXF0ZG7rCyTXcetmJSrYZC19xLFGk-6HVSKvSsxB2wGPtEMkQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معرفی زیبای عادل خان فردوسی پور از مهمون‌های ویژه‌ برنامه‌ امشب؛ علی دایی: تیم ملی ما وقتی‌حذف‌شد که سردار رو خط زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/25798" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25797">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436909609.mp4?token=eG_B0Avi9111S5aQo-sHxtYdxgcr9t1m52FwqRhMwh_m8q0UpuEyZzKKQU4G0Dtwjn3fiLkmZXFSLRNSZLxxXw5atnEkeK5rCN7QdQ_n7jonKZEs7qN7LqDkGoYMdx_3Bx8gZcqxdvvCjun9J6i5rv9XxLf1E-4-eswdsdwg8ptNhnM2RYPtBHCNvEBNmssgcs3NUeC2axg2Z5NsKQ1-O1FOr-8jU53OH8Bej75buzchBekstHDbnTtIMS4jeGQqHbjr2qt5iDK4Z2j2BQYQbdD2rM3s72XRQk9rPwGghHcbcGs8XA359oUNuBx6S-JeOvPt0ATJhwscJ0JAZ16vMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436909609.mp4?token=eG_B0Avi9111S5aQo-sHxtYdxgcr9t1m52FwqRhMwh_m8q0UpuEyZzKKQU4G0Dtwjn3fiLkmZXFSLRNSZLxxXw5atnEkeK5rCN7QdQ_n7jonKZEs7qN7LqDkGoYMdx_3Bx8gZcqxdvvCjun9J6i5rv9XxLf1E-4-eswdsdwg8ptNhnM2RYPtBHCNvEBNmssgcs3NUeC2axg2Z5NsKQ1-O1FOr-8jU53OH8Bej75buzchBekstHDbnTtIMS4jeGQqHbjr2qt5iDK4Z2j2BQYQbdD2rM3s72XRQk9rPwGghHcbcGs8XA359oUNuBx6S-JeOvPt0ATJhwscJ0JAZ16vMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق دستور علیرضا بیرانوند مجسمه امیر قلعه نویی درمیدون‌ازادی‌ساخته‌شد. بیرو دیشب گفت هر مربی دیگه‌ای بجزقلعه‌نویی این نتایج درخشان "سه مساوی در ضعیف‌ترین گروه ممکن" رو گرفته بود تا حالا مجسمه اش در میدون آزادی زده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/25797" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx2MTsnyryxDtBHHMBRTM_DAOTwiUTDL92YSPvXoQxb61rQFArBD43j6BB6aoPyZF1SyScSREXCzMTQw_fo_hzd1OYYUriwG-KMCACyUm90wkXZLAsvZp2p0BQXhy5taNbTxyU2DMJ4IpXnmUE1lOiGxg3xo4ku6zLDWlqEXjV7mVnNC1hWHiEVdlZcowFmksA3IqRbrgrNgv0oRkE6qkfLya91RTd76rr5VD3Zf2ZXT1Nf2ALPVY86Bk9zq5XF4jXKN04m3lKeZR-eNv-Zc9s6Go_QOsgKXwrJtuLVxGArKgESgRw_6h0ysXKsPD_E_6xWqkH1s5gT9_N3jqjsf2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=IPxthAn9epxc_wXkbgSZMBKA48LXyS9fat0I9j7bFYE0pcc20o1VceKaEpFaNdRsT3xkvnhjx6Yt1khg32cVqMT4hXs7fKbNYonamAK1TNjvISd9HygOJOF39MuOatXOcVxOsYoNhxPdNlnNC_D8Wkn-lb6Bm6qUw1qcQ_616ay3FvpGAKZigaVdmr1V5dMEPbdRtwCFlz_AcSYpD1dGE5MZ-DuPNORjR2YE_bcqdvAGoF96ZITGbXcUrcc814ybijHhnTXmxpzARQcq4elHD4KjdHDr4Y4t6YbkB907syMPpMMn3lx4g8A9fGiLu4uQ4RCOR82sanm6GSuMQI-CdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=IPxthAn9epxc_wXkbgSZMBKA48LXyS9fat0I9j7bFYE0pcc20o1VceKaEpFaNdRsT3xkvnhjx6Yt1khg32cVqMT4hXs7fKbNYonamAK1TNjvISd9HygOJOF39MuOatXOcVxOsYoNhxPdNlnNC_D8Wkn-lb6Bm6qUw1qcQ_616ay3FvpGAKZigaVdmr1V5dMEPbdRtwCFlz_AcSYpD1dGE5MZ-DuPNORjR2YE_bcqdvAGoF96ZITGbXcUrcc814ybijHhnTXmxpzARQcq4elHD4KjdHDr4Y4t6YbkB907syMPpMMn3lx4g8A9fGiLu4uQ4RCOR82sanm6GSuMQI-CdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=ISyZOCKv0RWZr0VNa2Dayxus6rEyDz4eVwTW3YzCMyMwLuMckOoXPNEYbC8SAzEwv9hYr1ypWGLOyly28G6s3StH-UuXVNk4e9BXT75WoU4dxjmogYKXp6CbAnr1pRhLASLJZjjYB6Fnzvk03TDplkicn-_SGlnu3U2-F3VJP5o_tHSKQOKZHUPZlk6vPAbAmeNzyseQrjqqZARfxZ0C4T37PNOehVEJ3hqEiGpVYAyebINljnuu4VqQm3rEBz0iDeQwIGk7aF6UnRfa8IQyZNGK7piBj0KD70sPG-qnga68orjheE95sEPt19ldeBeYFoPfRG2zCmRwpV48hfAGmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=ISyZOCKv0RWZr0VNa2Dayxus6rEyDz4eVwTW3YzCMyMwLuMckOoXPNEYbC8SAzEwv9hYr1ypWGLOyly28G6s3StH-UuXVNk4e9BXT75WoU4dxjmogYKXp6CbAnr1pRhLASLJZjjYB6Fnzvk03TDplkicn-_SGlnu3U2-F3VJP5o_tHSKQOKZHUPZlk6vPAbAmeNzyseQrjqqZARfxZ0C4T37PNOehVEJ3hqEiGpVYAyebINljnuu4VqQm3rEBz0iDeQwIGk7aF6UnRfa8IQyZNGK7piBj0KD70sPG-qnga68orjheE95sEPt19ldeBeYFoPfRG2zCmRwpV48hfAGmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNFO3j7cliQT8lVASY8LkjeLi6isZRsakB_ogDe5NvqD46zhwteD3mzvp7WL8lY_HNmmlHCmDaHWXzyhxlGJUB3fuKcREnl5Woi8o_lQ7siU4_gpfgsMz18ZynDmIciqi--AB2b1Orhb8KpREQm0KC4wGrEbuoKKdj0QXunVQolRNmHyxrQ50ElanFloN3gD-qNZnmpL3tllOlvL9ufZe0heiMNNKL9yAuu_bLzaaoEEQt-KV4BCohn02yJsoXArbKHDoKt69lJxSsClu-MUVrWe8abeE1ajZtokEhQWADWEhbzWLWm9mVlfu_3NIxtXo9QnuvKAR8a4xTRXoCoG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GX99Y_HuA4cO-xdaIKvjb9H26NnT54BJtfCd5AMwNrPTp1SlEqNlFUDU77UNJNd14hj5wC6-roCA-UZUONlr9lh4UmRuqxHR2vHtUek3EtT4UXefOk7iex-egi-dNU4o3SEu07WSE1UGXzHdw3M6c-Oy_XyKMgNfNAIfKaZ-riuUu9R0B_DeAzS58Gq-lpzjp15doMb2QguBHbqZq70c2FduWKBPP9reWV6wLDsWMTelVpfepYGBtlsg_ledm-HKG1uiOLusVL3SOgS3Ps3NdbiBM7_nVvUvvpH7wdc0Zl7inK5d9P3eZPEMpYCUwexV6pnla1r5Be-LOoVUjBfBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UciGm-K7cCiVReEYyecFcTGG3G0neNxpOihPJUw8bnfMULB9aN5H5Uf7OYWwNYiRtZtdst0SFhiRqfJO4HZGllzInUhetO23iizYW7xQhZNH-Lvn2_wOjxNlqER4lcgZ3dT5pt2yOG8hzgMhfNcudBFihfRq03lHNSQqpkcgU-_nx1Srb_locf3ZjgQm77VHyeTpAqTAw_ejSMZ-B9k1oLk-r0xxav_G3oslgKybmnJn3O0qFepo4ZgBUdNKs1Hj5sDuzM5HAsrBKVlIe6iCWtwPN2uZaA9h6_nibYlk6YjLc0kqrCmiAVtRrHW74G3AibSWPyBNo_H1t550Irb8lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB-F3OfstbJwU9bsLg5qqqGRXX5FDUxj8zOci0e2wPtT35yTFv3NWev5jxIGxxfJyYM1A_d8QJUyrowp0ZCKQ4b5Buta7qhzPNWMAmef8bie2KaEjClD47h1-eqfzi4nEIBHe5Vhg2WI0UqSFX7jKbKoTtVxeLBnIDujEIYqGRy64jvqSA5tICw4kFxAgxc5wZeqo_14oI4EAm1ml7AzubcS8zZfXdK-d8dYaBIcKAjs2yJu8Lg0pIJkx21U_r1UWJNrxgS9ACvhNGUQAfnfAqfUvkmeTqfen09uj7n9ispQ2jo9BtEUZNXBX93tv_LXx96UU3MRi-vdWmVnPfs1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSJVe8IUBdBNdawenDOcRf0Heh9krbxA2Kacs0jtV9VSZ0iOFMgUmKZHXG5I0gnNvAB7WgAcDo0tckKFDE2nUp1-2_t3SfJZ3VY-3QWb3VA8fRt67EaST1ZFsoFc9ii431D6lwk1WjaV75elybDlwnZpSE_Wn1XghQ63i4W5rOWN29sUWTJUn-7xguQCGNd9nAtFVEovCNAJMQJRxp83mXKXJHkH9PUTWPK5yDfScEE4HyTemRQaXtxlAMnXYnDT_z9lw_sy5ZHQBuRe4eQqzXnbRzfLWnQ5slTlBluRy5hpPaq-yOMpb6J061mFozMYPOSCGZ9qIAsGyodJh7HdsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=gRFpzwIzZM4RxPRl4UdhMG-Y5SnPPgd5zJJguyx7cIFG8duIemGdPoVsxpbutHw7UATqag4He-gOvRDsNt5XyqTabaJUKnc4FHUOO0rtQkHPE_kTTpYJYpTg8a_fEu0TWueujmx4D6AnH7B8nhJv3d1Al4n8s0_g7yKmpFYwB9G5GhPHA9_ZhfXHLeANufZj-T1WAazWjp--vwJWJHG-3X0rXjrt1azhC5QU7R8xOME-R5UG1HRBvUfitumdPIrTgDP9Z9tfKutOK2aIGhdKR2KIDsN4-Gk2AvNy0QsabcP_OQrck-x8MLdjUm1nGZAtYf47ipZOJiNnYapvzTo2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=gRFpzwIzZM4RxPRl4UdhMG-Y5SnPPgd5zJJguyx7cIFG8duIemGdPoVsxpbutHw7UATqag4He-gOvRDsNt5XyqTabaJUKnc4FHUOO0rtQkHPE_kTTpYJYpTg8a_fEu0TWueujmx4D6AnH7B8nhJv3d1Al4n8s0_g7yKmpFYwB9G5GhPHA9_ZhfXHLeANufZj-T1WAazWjp--vwJWJHG-3X0rXjrt1azhC5QU7R8xOME-R5UG1HRBvUfitumdPIrTgDP9Z9tfKutOK2aIGhdKR2KIDsN4-Gk2AvNy0QsabcP_OQrck-x8MLdjUm1nGZAtYf47ipZOJiNnYapvzTo2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUNo-ttyVjLvGfVYFn1e0camMucDES_qLgOndyUqAfMCKJgl4aQEM2F68YjT0GAUoBqcqWRAj3ntkwK4lrV4UfUiDVn9wgWn9KR02DSydRXrujdgLmIIepC7Mqqgu4Zrh2AG4QPxSFQlL3OA94Si8feEHXXKYhCWaCni4NI4jktYxTDl2Jdqmn32tMLCmCp6UvRX1NKx0iYaXgzBMMJtX_pgJ6WT5sl6zAGd3zwiXb-mJxcYYYelE-XGd03gEF8RyfDNL2dXos0EkbcoCAA4TyBfB3lq_v8g_-inUymMCwEimyAd5lq_UjCCVZVpARDnxxlwoJ6tj_b2d6gQ-oOX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgzhJJ8U6P0klz_QtszAjNu_IF_p2I4q4UeZBj57u4gHRAGkSpywXgGKDBFmAOVpDVLO2zo5UpTC7SOzQksp4uJTj3WfQueAvStDSnXm_O7PmXcjrxE5mvlLEEhWixO9JLgFl50DNtx8bXRPKRTLPfn_qDTKq445r4uL4SfW1zeteJNVDsL0ErqS3Lc8DI-boxPQL6wkGPKk0dMYSjdw84vh5gbTXgH-xJzCRguaJY-IjeosPRaUn8FGU3h0sd-AnQ6Mop0tZaq7cKzCwDURjjfQyYJw7yy2zODrsN-_fFj0elWzA-Ln1QgU-rboWab-KQ8hEmFc7X5VAfLj4csTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz1VgjnzTYZlBd9ZVrWgWVShn7_w4gkTlXrpdCO-jYOhlvcGwRXLS9iIwLB2zP11jyihWbPINdATn7SX2PZ3cVRlMm7Cxmi2ABrTRUHmwAwi6yH0uCa2NAXkLgWQ9vVB7GJ_wkFd0SR0sfZox6R2AK4zW5V_WTizSV-5lt6mmyZm4QHCJXv4m30zOaKMPq2v0nFLRK9TRGpTsQT2tnZHBPfqxN4zpPHeg06og7QxGE7q9_hpdQt71yj7LXe-smMnTUNe50z85LhfLQ78IfANTXc3eN7LUpUZcPC6Vm7cHzBrIjvRnaYyExpxu2uU54ZyY5ldPOdDHFl9Czf4_tbBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_YEOQW4R6G8zz00w1FNI_ErnKY38hTodgz-Yji5g-ep3eIa6oerSlUSS4MYpa0PydOPrrlRTnrmoK8iqhVHo-P8aCStnf5d4kRXzzIFU_nLu3kryWFBRF97-URaGBcXUSR2bCaa6UgkU_wQ7Kso9m-L4Xp6BOWLKBxaCnt45o-BoMPEp4kyiasChPTJ2-DSaLM6b3GnEM5rSz-pT8k50VCKLhApt-tZIMamgzcMNjMhU8dZyeL7yrAHy7mG4PhEHGXiLweKyvSjD2akyrLSed0fHqYwKyMGy_Ys46uoupEmFwypyxhuxM0sv0xoWL33TnH8mOxBVVstHU3KHAKN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25782">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=rZ8c5QieMUm0HBt-DK0VwPDh_WhDkuxP_VaQjHD3U0PF7L7GIFnJfkXUTr_bS4zcSWqkQS3K0A8X3BBQJrL9p6jiAAeXn_ua5MJwNu96BKqH4Pdnr6nDnqzfJ6aMV6WpFNMPfIM11Zne61dhlebPfS-45_W_SX52nQAdIU1M9DNNKxnChInLGZWGz83RiIvzg_TjfgqB6PutziWUOl94IU-CSegj-Pha6k-0Imx-IcxIiSW8I8UcMvHBpXhNYWu94Ee8z8K6ymVv9javgtg9Dn12FQRq5lC2NMGjtmqT4j2QGOoI0CsjnVTN7D4uwABTDqLRlQIpCvRwGZ--yMIV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=rZ8c5QieMUm0HBt-DK0VwPDh_WhDkuxP_VaQjHD3U0PF7L7GIFnJfkXUTr_bS4zcSWqkQS3K0A8X3BBQJrL9p6jiAAeXn_ua5MJwNu96BKqH4Pdnr6nDnqzfJ6aMV6WpFNMPfIM11Zne61dhlebPfS-45_W_SX52nQAdIU1M9DNNKxnChInLGZWGz83RiIvzg_TjfgqB6PutziWUOl94IU-CSegj-Pha6k-0Imx-IcxIiSW8I8UcMvHBpXhNYWu94Ee8z8K6ymVv9javgtg9Dn12FQRq5lC2NMGjtmqT4j2QGOoI0CsjnVTN7D4uwABTDqLRlQIpCvRwGZ--yMIV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه بازی‌های تیم‌ملی‌والیبال+جدول رده بندی لیگ ملت‌های والیبال قبل از شروع هفته سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25782" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=nxePHNwwlJQXYsVuU8HWp3klrMFIhQh18b1cZtu8eYAYkEjbfipHhBp--bSz0eA2GjQPw-wdeBDTGfFu5HXJcvj1FjR6PA46m-JehS9dFKq0iArYZvWqxiSZOKYKGOh9d-XJG0k1WrNL2ab7AFglATbOPBRtAvH6YDZhfCY07JPkOlVPxTvmZdSRWoIgoV94UMyZF7jR3LSKypzch9tg5Hh2C5s5lTFGAvwEpCVIbl53aHRTnfvB1ZqD6Ca4RVr5mQG6GgLMdnqWWhw54kxBkX31cnfQ2h1HJ0ki67CpqFKyWKaXolOEoJVifd6t7Jg6AeJKilUba8BwjuwsfwfCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=cLlk2bKYJdQs8jbw8q-LHWviHmxe_n-D1m2uO6c2klyGBUk1bpPP9tyyNqMfDlmihFmd4UFYa9GVNxo6ra7Qhckl9SmQYsZvAP9J4lCbajfA5snn8PWYcIAtXh-HjK-y_5KSG9oa4ChzYE49HTT0GLzMXHsrbs9pIcWMUQEhBDoK6aEEi3UZxzxseJTUYs9wnc1LuXor9xZTFU5mWYE-9iSafy4C-ogVX-I2HIb9FVeRb2M3ojynmLPwYehhWzjsEISIrq0qrRJvUgWg5w4Nd-82yP_HowVld1ZgYt_89WM66lLB-nG2vdS5fWmGQjaGSNDyYWPioFN7TU-xHMMQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoX4Jh0IkGo6VKuVOI3FHFMtPLR-gjH7MvU5o-Ts9ekHY0uDEH1GBWwP-ctxCxDUu8bJ2_MCSj2xqEe5lCLmgp9zw9dbNLBrYNn661sl-JzPzYgHN9Ufr-NxxB6jVTkaplvVOeLzOd2Q-T7OZnytri1g4zdIa6ptr7HAB1s8t-RayMlA4UlwOMvRoHWsWRkxZ-fqJVb6F0aTLrsRKstwyEZldRz0mINQTCxkdy9l_u__P17752-xazBGJsa94QHZaPXgGHM_sieAtyMbtIrBAFHxQUYtWkt7LGVI3CvP56aYp400HcA1tQCokzZIWe407u4j9MvRoKeq53Dvwyt78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-f8BESUnPFVEorN_FGGR_JzEtM9jIrVF75IQ8ewrlxnT5en8zo4Y_Xl0WSWxapDVNy_fNQ_kQdkUgPnk54fjygMCor9Q6ExDlC-sGuuLV84km7-EkVGDBdcokbCk-UES9Xe6oycdO3UHPVxNJ6yWGU53a0vEl3n7_S_3trsaBx7-HOVKmPkCtlB-aXsxrfymH6H2DAn9ODQ2srBl25topB0PHw4PjRNtdnYYWJpwdi3O3GJ-AtrYXSbf4nCBAJ9_U_J6jxC8_Cwgl3g1xljDFmiFAzKdcbwYcWXF9XDMAuiSy_Lj0wlDrJ9YdwOl-HLqpRz4IKy3OYLfLDagQ3c-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS5-wcs8Lib8dOEBIp4ggO4swlfMcWtMqQe8-pZA0xtTxFb-6-T7ykJQFoulY-_i9s9ARXy3xY728aNqfCAFDzOps8NQrs-3UvALDq9zaXCLL7K2hg6WdXZv_KSmPapDhWLJv7acXHEtYjsr73RNFEMyN7U1GsDe93MDzP7xdOYq5JmmV_Ph77Oit_a1gJ3xWJ4P1T4cb8GdHcqbNwvKIv7RoBIt4bRAD9LPl0dLQXyg2-DLUCCq42wajmILawZypvWvwJ4dEicIQwkPmA4ChhpnTKcC5g9fypDr7u-mJYKp6EwqLQFZdxKRUruJ4jCm62shr43jr8Vd54bTxCznSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsRkYQjdCm0RQsQjDb5vBBAYixARnoeQSfThGdseyDddwwWoyRPsd6bumQpRXb0aU4ZR-ldTClOI3qI8Ba68Ni_xU5oSayEpHfFhS2h6IvHYRvOllOL0sXJYC6fedhR8-OfFXhfzgwoFZ1PRiej65G8kkxJLIuqXYL6cfYT9VeaiA6PDKqPaz3A_CRlatA6DT_TqQ7i3JAfYP1iaK2f7mdoUNiEcG2xj6Fk7SVQLppXI1nM1960OD13S5OAAwZE4LlTPDMNQ_-EYR0ZdfZ2uScJ2mNmk-UjPzlttXzWmcZ5tl5wjcsmh6wBBRYP576nfqFqCH-kjud-3gEUe8N4G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isACpuYeNbFIh0kK1qIA9gvDWehlCkP-WZjE0XgRZEzDyDW4s_WtVjHgoAm9hq-a_5v347hIbnKSIjbkLsJhgCp20UTORSpWfMQU9b-N_rUeuKgTxvZY74SOrMStg2Z48OGlAO_pMH5taMLguN-Qb4ZaKqvPwarSoYaFTwxjvWY2I8v_xmK2IbJOJqrqBYfE2jxYU1KzPnJmCM44I5blTnjjIdAU507WTLdyGBxo-LxTvwl0ydcZQ2vNQmTyhxkw5WkABHf2HKgVlx480EzG74IaibfEXJgdSCK_2D8lBVAvLQx-ovO2kJYoKY4Blxok97kc6yvUOHd6vDjem7oo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urlZd5TZMgYSGIGTUmd_VCqwha8rxEf58HMVc0PXcMp0DlRLQMTCk2hB2E-sAoFVt9WdAn1-Io07Q-qyiQ23hW_gOWeCHWljft-Dn4ArVvt2rxYRqnLATHbZFYRjvFEh7LjmyiMwKO6_w2ZRT9k-yj7zOvOczoxsQ_15wgSKfIcjptI-bdZgYr0ZbfL4qWvaAHf8zDiLllmGqCsSR7tnmnp_xZyv6aLwxpNycEAh4LMxLxpaHFb8KLQGc4Pm-GmqofWG5_XMNAKWoF1RwVfaZnauwg7OkiCOa3WIrU60abYCjY59rF5RC4RyVnCs-cXDpXYTaXPAIDnGKt27r9wzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25773">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvIlWO5eB03H3KzkqBZCS5fEaZLaJPcSYSguABjoz_gMPPsWSpmgbA0T-U0oHFPzOR2RRRBfm6r6C5vplxHIyWUhMa5xCSO4g5rlNYluEix84oefenBk0rhxXkQjWWQzWFUtcv_RT6AoBf5ipDF1Ex-4taWrRMqaiBMV1yx7AWSDrgTf0YazFOdb0Z8uA-qunfK2twYqPJYbBtZnzotfSUDRz90gbR0__4hDgXIlJHXX_21VpOzTjtNwd3g9KHQ49JvKTfdwX9cV6Xre6H0Jb6Dmr4sdCQ3SbHl8p0AIsYQfPYxmRWuy5C-zcCTlCYp_nYx-Rk_qssg5v0cKTXDqmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود بسایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25773" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvZsLVeSkpxrnPe4168BmNhxlIFksHreVTxvTWdRTWXOI_nEehNYZu07GDKGlTQIYOeY01NRMLCE70A3Kd6LWN8qeG8x91-OHkViM9k31VL7b_jxnvlebGbnq52v_AZNxfmOQvNzZUv0qNygbpRcB6gdfED-2P2E0P-miUtTeaygUMlLNSU7w_3oP1Ga7rZTiODJDWpHXBjTM-FytBjL2EbCQ8z-5DFui1W0iIA1XvtcMCRNrSc-vArZiwdYHJTUihrKCdoafq6uSZvlrIXYyUok94XcimmZsdngzVzdRDzUgHSUlVMy5KrupVu3BJwprJttF4pVgS1Vxx1jOpgHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ayabq7mACFTNWoXuw-ia_Rv7QgIA_bbOBf3iRRy3n65EvnDC2OPdt46LBpqwu_gLjjVbdW9jv9qHN9gvuQ3HBb_Xh2gXKtEm1vVfJ4OkqwUYLUCx5re3b2wdabV696-nKyPSg4wYvtpOj8S8d5HlieJbPkbT6F84PSLYo4agX-IDyfafSgHw8SYhqAExe0GlZXCkaQSMwuG47iFL4qRbZbpNOT0UfXto5t-8n_WXNgRLn69tuaSKVnSk-c9ph55HniKggQtzSL976IiWU7GsAzNbzJgEhsjzF2RhdhKzkawOMAZLc_QryJEKfdZ9_r8BOW-5PtwhbbUiWSPfmWDDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qM9YqYLXkaElqMTmpsqVh_cka2oGjO9Snwew6Pl8y5HVpyfYcR7L82J01YryHVKQvBmffjYacXgXpA_VJXb3UZH8Nn6O9Zc5V3rUQ4_SVRN-Uxzn6uSnIrd1dcy76cJQOhNL3jlFrP7FYlgDiQDNK7cjpkFUEBUOE52TDloNNKSkjV2_B01P343ffOFsLdNLN4rZzKnXm_xkiCcWmAAw9R5KwiQDE7kqiFhuFCirbKoToZBzEXirX02d6Yu6US9UrrKxMtvLCZXkn8GmKMfMUemEFlf_u3usdzHD_4PsLE1-ThqMch53zvDxGPSgbYFEBnhFFxgHHNJxzwqipa4TKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtVxvLonZIV1GrpWAetpdY59LI8F_hV7Zg3NQl_ALolPTggS2R-S_kQSOmJFi_6VuN2Gi2Z_jmx6zM4hWyksR3BFfF72L7qitRl1y5lysj-fFXL77autWfiavHlqk2oLTs4Vk2byeK_P_CYiQucVnYRwoY29WI0lWXFMyYucO8YHt14MAYmU2MiQfyxjp3kVvZmPqTm8jHqQAp7RsHnnMZSi9jWtlfYt8uKdgPmL71y3WSmxe-9aiizWB7KXB3WGHnnKGDCM3p8TCXQJoILmf3vCxlIxnksHiPRKRv-UGYYH2XQa7d2aIfHGT3E8XexZPmmYXCFfPc77MV36B2F28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEK6Zkbd32dcADu4f2S3R0POHpIcgTu2aHiv0O02Sc9jFtFfG8kSRKNMy7OxxHeRBQJ4uT3-qmf_I9eVZ6oreESiWJB5ahmYeE-uoQ4QY04QbWwxPM2vVuFYVk1cDsSuydvUA2U485XFWqanXGdvER83G4cq8jzTOvzN4XB_JX-EbRyhlQs-5Dfyn9M3RrbH1vMiS4wgnqkj29Bb1QA3Cp7hWLLpgTEvPNsFrjrOQsGGvSs2X9gmQ6BZiV2_IM9ECkGwdCcjI9khGm1bp7q8-vRRVdWZ11v3B1KWYfuEbTgociaUXKbP-4-H2rrLYhIQiE3njl7f5rIdLph59QpfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dq_Ta0GdY-X7eXcci6-kFo7h88w_eAXREQnjODnp9P-3POIcCHQj1yd3qRme5y9oOy9h48GgQb3MSnrtkBf6LMHRuO5vjuuyBjs9yS9-lYMUCXLRQOzGtg-nvRI7jiH3PbeO2_EB5kheppA1dLc_fHmQxTbvI9LVQtlOdy47Li_UwGVywn_Avwj4anyHeUS2Cy23FjGWEmrjWuAAz0mKKIsgH-c3VbfSws80RbZ2VqbrFgaN5djvnk_HrC_ACYiWYr_pXK-1Eq5sdxE6dS7PCFEXTgrC2yfrQUUCNnlmpyyfTNzCiCfIhU0YUYC5SrxudccgCUz4zeCHBvbaw_xyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=U87LHwnNizeuU5hNCWaP9GyTi5Qme0xVb3mmeDMVei2YtGSfRY1HUaMbFwtSOcveBJEzqHBPBCcMg8RL_hGcE37tYAiTy2uDCUeNXBmqHCLEcfKZ-IKsL9L6xl9m3CGO7E7llDMJMLhR5p5RupsaLMa6-DnJsuwcLxma3y295B-FHBNIEP9a5TbtTZNR4MT2v1I5ecao-mxdzdr1JQCk67MZXc6MM9DwzUrwSlkGek6_Y3lShQFpqO8vaxOckCRqmiSvO9llRKyH76M-ssmFVBK6Ujg-vynwYUCmOAqTFaIdcGERddUKEJIV_KqBkGMnpXhNqSIXUxG3sxhAbvEFAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=U87LHwnNizeuU5hNCWaP9GyTi5Qme0xVb3mmeDMVei2YtGSfRY1HUaMbFwtSOcveBJEzqHBPBCcMg8RL_hGcE37tYAiTy2uDCUeNXBmqHCLEcfKZ-IKsL9L6xl9m3CGO7E7llDMJMLhR5p5RupsaLMa6-DnJsuwcLxma3y295B-FHBNIEP9a5TbtTZNR4MT2v1I5ecao-mxdzdr1JQCk67MZXc6MM9DwzUrwSlkGek6_Y3lShQFpqO8vaxOckCRqmiSvO9llRKyH76M-ssmFVBK6Ujg-vynwYUCmOAqTFaIdcGERddUKEJIV_KqBkGMnpXhNqSIXUxG3sxhAbvEFAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K51F02mwc8Z_xeej-_UgelMRlRZqDQSDGjsNE_lrYoLEW_wa1asZ_INk_HgGtUE7ucN78hvWyTpgugfZrOOkNF4artP338Eaveiu-fqbTkp9YR81T8a6njjN1RjrjEQkQcVDxJE1-Rvz-bh0Lc0uAzhudD7UPKOuJTJf9h07RRGy88vwBsKFWiB-YXOd5NSRh_vGJ2Bsu_F9Ik-X_7K9PYsht8KSVSDkmCgYqmympGV6SsSfJsuk9HCe8JArU2soAXAiIobPvA_o-u2e6QipiiT4KhFc2cU4xKdnqKVG-UbQFARB2jcA5tNK-ChXZirw9E7yFzf-K7iruq1NuRYIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU57pACMKpoGNoBP6pAufRqCeSiI1b3s9Pj9YNJ-apaVhzUb5uTyU6M8PnL7OkFWcCIrrqB676-RsVB-cEYiLzs60V1ZGSgpEvoJlGNYKtPxIvE8mNkrxoCJULl412_aYhJu_neS2hLr8zEwnbdVFyw2fPMRQulqw8qgRZuQG5NPV5aq2C8ys9gPyocUCI0vtD_e7F8F_H2jv87V7xrmyfmVyNd-q0aq5AF9RH8UHQgn2WmH3QcPVAZbaN01tQ2PWFEu7dpEgnCRJaBbTJG5yvlPKY_8aMuyUs93f0eIgkHWD1_4Dbfk9hbSQLWDbCdZ12_fhs3eV3dpXjFtCpNV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgnsgfoWcxU1x7QITyTLl20T4rRAF9Hp-PRlWIt9Bw3-tgJpyf77drBQvoTod_9tT-ohTJZKbmbM5KRoZwMPEetJCzIonslXO4rYHhmkS2jvJIgm7RpX0UXhkilQsHkYFcimv39c3sBXJtvHp92iAE-k9XTl8BPv74bXdwuZtTAd8JRVMW8SBItvUMn8x1ZoT6zPiYe888OWIgAdbfLQEn-2dOm2PwX-UQhA2lc91AYx53a9CbZRR2096gTtNwbZhl991Kc3soZj1D52wAPZprnSKe4SrGJP7IDx5uT29QyKu2rC5WtDha7UdY732PVKxbSSa6VHRu9NkYqq7-xGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=qC6M1S5EXV98JNhuK878Rx9t1OBkY0kp4Tovfm4fCkDkNs4bB4LHYa0rPzmaP26anEyFt-fMYcIvJsCmSNKZCMUAvbTMWj4ELeS6OnTQdp02SB-och_5XVYK2-6ZkEHPiDyJy8LBD8z-cj-fPb7ZiSaGKFCvarTmLNHyr1ZW89jgCJlpnQMhgtOL8d1oDGZLT_e-_VT59Ded2Yxbc49FofPzEc_XCtPtM93CJkDWTRWA-0-wS0-dNknRspjs19JDp8j8JyQcW2clBwzVjiu5gkOIyrsPZMLrHJp58BQsJ4sbyaByabXiT4YQ2c1iNSVqgHtPNFwRfS86Y0UlmkzxLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=qC6M1S5EXV98JNhuK878Rx9t1OBkY0kp4Tovfm4fCkDkNs4bB4LHYa0rPzmaP26anEyFt-fMYcIvJsCmSNKZCMUAvbTMWj4ELeS6OnTQdp02SB-och_5XVYK2-6ZkEHPiDyJy8LBD8z-cj-fPb7ZiSaGKFCvarTmLNHyr1ZW89jgCJlpnQMhgtOL8d1oDGZLT_e-_VT59Ded2Yxbc49FofPzEc_XCtPtM93CJkDWTRWA-0-wS0-dNknRspjs19JDp8j8JyQcW2clBwzVjiu5gkOIyrsPZMLrHJp58BQsJ4sbyaByabXiT4YQ2c1iNSVqgHtPNFwRfS86Y0UlmkzxLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMmek5x1ahWyLjnmHYz6zYDGlz_h1eCw8Sh59NWBqeXqXxf1O1ouYY8IkroLHHqMNbraJ4aDhaBNSQ2ObscDiGdtTsW7xP4i9I4Ge7Qrcp0SwM1J0SrMg_rMhSg3aXcfcVKDRfpLmIO7C4lz1UVm2XgH5vgHMCZJEJHk-yViZdm4Mml2Y3gAKyhhzZUZnKFWiXCWtWTDkfraLXjFhW0g_RzYm77CZmS8kvr-izY37EQceSrqz3Mes8V3Lz-a7HhhrSAGlPyS0HRdJRS8Y4PI0VsmFsZZH1Qpk-huKhFj0f-NzSd8GP_UGQIlsLPhSP8YWStaS1Aue8f2a5JO7-xyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSISFbQpxyYkarBuhJ9k_gK0Y9xA-trOgdhAQMROS3x5_lzxiAWPPHuzGgbv_aAvookmmDUvlWhchdpIzTl8OKPaLi-zNf670EhjfqNwuNUWJr-A9HWogu76Zfm2G98UzWj7X7D3_2tLhNPW7TTkYgAS_WFInsXUmFF1qL6J5e7i8sH5cb97FcQrzmTa1Q4YIxn_6AyRMevaePR7Fs9AD_HS-IBKy0G4fKjc5BhiFYve7Fwt_rhIj6sI56uzENEDHNzC0uJPuPVNyJ3l8UEMcK7Uejo8Fk-0pLGSlGnu9w0QtfwyqqCHtMu6370Dv6fTT6G9Xcgg9BijF32d0u0KPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfRuLGO0JeZnLBQxkHU2DBhHn7U4HM5CjctDenbT-HQJ_4t3NaUle7OHYoYY14QEGsHPg8lKKTzbje9g9RtaK1TnhJLIyWwnn4WktU3uVLo49hUoy_8Bf5eKv873uqPQQ3Xdu8sHLhJvDIJY_xT3aOR9wUMyH5MxrKu6qZCRUQvjdSbIxvMDi5HQfRCbmdp7ytQCiKvhwciap1qXhPeCrlDtiZfq4fR3uUeuQg36cPz7zo3gjIxZRo7lTvsa8wMBpYuA_9WGPYqMZwiLI24kN9wqKqt9v5iMZoO7UzFaEDIx-dAb0FFVtRrKV17j9oHJVKSgEzSUT0PSj_XQmqUn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYCCDeCYFyYFSdXBIuZJJq6iNjHNI6c_SPU0uBITIVIJmAv4wyngsrHsP_bJcJAlwI5DomkqYORiOc2W6SawKeCJvvOdcoqO_wTsR--bKfYOiSJf1_pEgggzBqeR_SnpGUu9KeI9RiG21bXt2ljw3dPDJ6I1t9O78c3N6ZxrmuPxydUxQfUXd1X2v3y7KCF-X2U7TWvtq9PPfAL0sixy4FMfIRQRwW1p4MlI2z90AytTXhWHQykdvTPwP12EWqrq0vZW_sWn4ZpSlMlfG20OogO5MJMMt9lX_m8tfn6e5n3AvJnyOXE8Q_WsU_alXTbi-7jtS2HOXIrD2vzFOs-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QebI9MWA_hCAdH2KuJaSm-HNGwafsSM_gjnAxN3nsE19jR67XlJItMi1skvQQ7wLAzDNgtB7enxSqq8OxMB1_Qb72Oj4Tg-Z4yHf8fK5Dsmwd-bff21XxFQayfYPDkZa-OyKvpI4kXoNAy409AdbcxugsjjTB7vrF13FP9oB_gw5_NSgk2gcqZDcqpsglbiCU1Pg6TBQzehRrLP3gEKC64a0Cyx1IhHFY-ablNsiMKxXF3UQik2evl5p5htgzHhu_wW5Z8WhUCrKGR4419S79Vh7FHz8aolJKpKfpK1yjkKGA-II2TRbSxAgPCw8nnN-J7tennRo91GzF8-l4wrBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOqFy1edCgLykBW3voRn9QXrLSqr2Ul7HhS7zaBZIb2k8QRdgmd6m8sYcJVtpIWu99uXEhI3Ccjawvl7dBt4JKSJD19oiaFxX-Bev7JqTgsYi8cA3SXf97M1klxoQF2_kXNxvhXHGFpSWRH2nEZxMW7BIdm1_XRj1QhVLsmhv9VKh_HQoyyne7a33DPuTm-bQF7a7VKeTTmIF4Vv5zkUut-B7BoTfmde5lzpvAohYxcpZH9k6dOmV3ytu_bFF2X1GuvHZKpWb4wgMIOKZsJwXrAtPv3sypty4ZLLCat-fssOu8IklE2tL7CY1G0kkrzp7cSgsdDY0N5ZMv_DZ6wXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMRRTpK_8xM10cWNZdcPSasKxN-L8kieWISv_5exXXcORRJ4QM_oj-ixnp7KVKC0rZeH8pDmZvKVnHgrnS8a9n6AV25fukS7KcZhF37C3Me-t91nY9_PedP6PdcOq68_eOpikDLlyG6LiM2X7Lk5W371mEqGTefgQyw4zZRaolFqVnrSPfinExDf3xnTXITOHsqg6zsVRjSe35WTTWwm9uxbGl2lTmWObrCPEJRryV7vg2xNu5yU_H5PHuarTEcOOkPJFw9TmkgcUp28hUpopIlfcALBMdggANoWROKgGh-c8wtTxiV6e4_7a7KU3mAdHKztYS_4k5b7F2FJ-uyONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgfEoj_R7JpJ9_3s-kVmZI2ewJRZ4u6t2rj-pG6CScoUXVzpGtb08Ii1WqOrPvj7D44EcmtUwSwifl71Ei8PRNS_XgRvzRYae3k1qm-JmOnzZHpJlbM_rOKtVLBMwNB90Tc2VSMQMwo5zaYwVpIy7JVubqpF3TfqTaPYuLLlyhnUFI9raovmc7OVKwDVQ0TMJjmkMKfwrWvCgoufb26IfUmJstgorPhK00aNQTMvD2b7qNRfSzn9YgmBVBgXu-_a3DvqAo9zoROA_M5nhHBiVIoEHpcB0U4jrTet0RbcoKeSPG2-sLV8egTVjmtEjRXAh6nKwlHHTNPXc2t9zL5W6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K064-hpG3XgZ1IUNnfcfh-t6U4UGpHfOOf9Llpm003OalciA8tWkxaw1MyhAQ9U_zJrsrPAl3b_7F-BfcFSYS32GCr_jP2EqRMVOv8ahk7a6jdVKSh_A5vf7hd8TEuH5vueIG3HgLpuMAeuynvDZVuj_CBBmywWHQ1tFiVoxF0sJXVmI0Dr3Gd8Mr3ay4eYoULCUCYHl6fgfBCs_-otrB4h3D0a7swhhhknI3bjq-Je41XVxmOm2vNd2RYH6NkyLx4heBrKxtUap0q27ta4WsXkD5aH_D1Z_10OfSCRB1pzv5pQoLfJeu9JBQD568Ps3vmW2Q8Hs_7FlWjMBvlB0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=MDO19MFwpmEWE0oa4LcEF6-p8O8hJm3qWlbZq6CQsYI-ouc4Gspi61uUyjk58QKAwEsSaNYX5jqTlh-OI2T5meZuPXDt-HHMoX8hRpnxEpxYVIBam1Abz8bBsOjTUq0Le5m0EPAaG4eYl8Zmx4FhHA79emg0ZzbghzBhFAhZ3IJtzUA3V68U-miJ8cM9RO2f62zwT4Kbx5sHGnW1bwsnadnQesdOlC2320WSu1yV1ZJgb0tg8J3CFtmeadsw4kj-nyq5nyXVSbisPqDj3IQ0pe48-cGnXbnI5y0sK9HoZUnZXWceY8QW0dpnf7gegWcl7vqKeYRXhaBBLEouHmacpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=MDO19MFwpmEWE0oa4LcEF6-p8O8hJm3qWlbZq6CQsYI-ouc4Gspi61uUyjk58QKAwEsSaNYX5jqTlh-OI2T5meZuPXDt-HHMoX8hRpnxEpxYVIBam1Abz8bBsOjTUq0Le5m0EPAaG4eYl8Zmx4FhHA79emg0ZzbghzBhFAhZ3IJtzUA3V68U-miJ8cM9RO2f62zwT4Kbx5sHGnW1bwsnadnQesdOlC2320WSu1yV1ZJgb0tg8J3CFtmeadsw4kj-nyq5nyXVSbisPqDj3IQ0pe48-cGnXbnI5y0sK9HoZUnZXWceY8QW0dpnf7gegWcl7vqKeYRXhaBBLEouHmacpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlwqncwfG1UJrky0_WFoJN96cGTTCWbedZMoii9XNpsXUwLqymwItGvnMf4kUInBTWiC767FufJBTEdnDv8cV6vchS1qjpcNajtyb_XrkTbcIWrU0AOzLRqIiEcwW4Dpsb74k-jggZtNu6k8maKUTxhS9DXbaGKKFDBS2N9S-ZEu9PpeykXsIp3tteYhS2qLFhVLaw4X7TzefKFNMIPOstXsFqQXO0wNkcoLf_y3IDCLPHVnYkr-Vu9kYTAdSVdFYK1U4LBKCVLZn7A42f1K7WAhYygfS5HH2fmSPdiK-THz_NfQ0ONvwfY3dBVRfS-JsXAB8CxKm3Ngre_FLL5Yzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/funk4VwP_hP7b53Yodu9s7kLpPQgZano6BBRbO4N0AedgtQUBLehpBB2ug9j1T0uokXNGrMNJxSY5L63UIkZehaJB-th6mq1kMNmYIRS5AsC0a3dHwHZSdCbcFIzoFuvaGN0_1SVxH3zKS6VwvQb5-pZEkIyi69pVGA5n-nldhLI8BE_TniPxiOrWVa_4KrxHSRAIaVi0UUNREg3X4R9PvuqGHJesEkNDkOstMqKguc_N5PWmETty4wcsPIGF-yqwHDeKIuNFNw2F45Hic-nrapFbaRcL9hB7m7TJxIR-YN1w68EkQWFCa_5zHIYjgiupfotOZoD5iCghRY1ZwR_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtMuiqbPndku9qTspn71lBv3KYFuLBDwCc72XCg0t-njDFL7Wksgne74hsgVrhmNOboL8876NbUF9OeyOhmH49WKdrgBuRorBjX1pr6nuds9xjf7WTJcuh3Lppsug7WlExt_jErBDFWV-2zWl3Fz69Ed9O0tTf6z7eWNOh2Q88gFPek_cpCiAGLS5YBQCqNuv0nbf_5x9tZLfESykb7rzDj2qWd09dlz4H8HEwprJWCm9BlM28RcNqb0fJvMFBv8flL0cpQz3AtreyocMLUNKTNzr2sHeLKnhUcqO-293tAF7jFY1MjIIstdYnb5aqFu9m6Ct3Ryjp16bSnc9zTyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3HwIHiBM6_4BhtbpSRxrmuc3_XiCQJHo9c1XeXEhjiJsrK44-HD0ILqOu6UksXrJpX2kEEIQYeEFBKk0wrA-vru1YjMPwMeUiYsFwsh5Gxb3LHU_ekSZxU_tDzMGd6twDE-Xj5nlwRPDfdYEqRIccIEsxlywJjajFGFUn-pG9TB84UBdhdG84QvhsRUHrXLn85Xdf4tbKaL6LMbhI4BC81xZvvqASwzrU2x3GKbPb0ObmfdZ6Bme78ZJksyaDLxgFadOIPJY46wPtZylNM3-rIaVJ2V69WwXesti3aUTs8tyx5UwzH5BVmLoAdvRraniY9N-DmUBLpr6omoINFZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEmMch2U0Dy_8V6BYYbCVFSBu7M3V3IIjbKncSxkEeSYeEb7_Qq0mEFgdE5h-XI5piuDBlUTMPGQwG5YfxhNX4EY8Xt_8-DfWci1znis20Sr97xOTQKX5rlzHy5j_wJoqUqNoBldtgFl1i1odagcZf2RCApa1uMzrGWZ07zf_w0rdQ1rvI-WNPwiOjdN9c_csskhZgQpr9BuFT4Bl_SY7mWa-uj4Mjd9BBuAGsGe82jmXPpBVyBcQDP3kOwQWa7TwPbWLKRak-RH7qm-pkBhINlYaUycic4RknxszR5UjwCI1iE7xC2VqPp4rcwi3cWSCBpeSXHMkEb1MaGfnr690w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=rR4aSzWwls031XVUyRZCtMzW-Y5j5wuoIUDkKqNyAy9BsSOcUJruP8G8uSz24ini55Ilho2D-_Z8uI4fu5MHDDfCNJlKgJACyVcwRhJThiy2LBTs3FCegeRNcI64oOKH_giTUQpPjhK5xAXDK3Y5qnQwYorLhC2CX2kYDIV2L6tFyNeJL-WQJIQ9HcUO_dLLf3Coi46lfHI7t1rgyhwoMUTyEo_Lm19_DaCaoSvGfXEM1IFvvuXY5_Ve2bKsic91karI4LpGYprDnEoVYmGuqwMrHTHaGXWk3ugOfG8xBLvnjnLDeVqcAxl0YWeCUZnudSO5ZuMwBqFl8wA79JUcRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=rR4aSzWwls031XVUyRZCtMzW-Y5j5wuoIUDkKqNyAy9BsSOcUJruP8G8uSz24ini55Ilho2D-_Z8uI4fu5MHDDfCNJlKgJACyVcwRhJThiy2LBTs3FCegeRNcI64oOKH_giTUQpPjhK5xAXDK3Y5qnQwYorLhC2CX2kYDIV2L6tFyNeJL-WQJIQ9HcUO_dLLf3Coi46lfHI7t1rgyhwoMUTyEo_Lm19_DaCaoSvGfXEM1IFvvuXY5_Ve2bKsic91karI4LpGYprDnEoVYmGuqwMrHTHaGXWk3ugOfG8xBLvnjnLDeVqcAxl0YWeCUZnudSO5ZuMwBqFl8wA79JUcRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOVFkgSDIv3iYhZfsNp96Fe9_D1VRKekBN3J_ukMCeOKqZfF4q3dZJr0Q1Ig-Gc33yTra01-aliSSEWN2B-ztiE_-kUhoGt4KJ5F5EOiVw4o2ObHim1JdSLtxar70IwCISuCqA54hZ9vA0Zns_aaF4wbkqDhEQ9QQa7CRv3SJKPTpGftbZk3hCDX2wANyBGvrKibFlxUvaG8e2lUtiUwsSYECyJUCEAyYgtMfxQCjtyu6FutPBHhaGb855uvEzaoxawkveVxkQL67Bpl_Grmx2qX9ndBNC7zfhJAg63QUQySo3itBkycF3XCT8rEOQelePrGydYspMMaRm61LDpFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQEhscP1gzjjCJyC1eV3PaM2KgmnoEUdKHuBGgV5cBv_PmAvpYQegnFOIc8xpAyJRGOmFGE_9-35mbO6ooB5F5sXVEWjwL9SkllrZ5Be-zVMRl5Pj3dG6WOv8ZlxK4SK3abbyE9t5OKVKD7pmDVqGyx_j4d-5QAIabiDbe2ZYoVCMHHmx4ZFApiC_2i-6J49dvJ6a1U_piHalE8W9hxPRRJMXM6gqq1VVqaUZirJyztsIlijrmftRSltKqZDd54xUYdYS0RvogbQySCj_B-RoAzzouTGK1ZadRn1JvM1OUu1YJHd0O4iytZt-A9q4iSKEGClwEhQT6leSDuQd0altA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=a1ZnAooe0hJURS_NmS9375AUfXBtuOLWmBYoP4kIAAgEXAiGJHfwc6jw1_l-A3mnxvqGcikEunLRXTU2F3cgSmKmjgTgj6ryhumiW0qfKpFCEtCOY4hJCKHaZ3rQNKex9SN7rM1wBzr6VouZRYAnv3lMSGrwLqMITnD6W5T5Z5YUiHNdkAdUlB3SO9KXYti1HK0poFVG1bt3ZBzOld-RBB8-VXwzlVghHdgmjV74A7rXDap80GXCpEb_mO9SKklGmYX4f_obwAa7QkXsPUH5KaMselE73QdaDJOEvtQAir5wboOXYxYj2HwAi2Ie37md4INQGxlVD3-USS-HEBAVVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=a1ZnAooe0hJURS_NmS9375AUfXBtuOLWmBYoP4kIAAgEXAiGJHfwc6jw1_l-A3mnxvqGcikEunLRXTU2F3cgSmKmjgTgj6ryhumiW0qfKpFCEtCOY4hJCKHaZ3rQNKex9SN7rM1wBzr6VouZRYAnv3lMSGrwLqMITnD6W5T5Z5YUiHNdkAdUlB3SO9KXYti1HK0poFVG1bt3ZBzOld-RBB8-VXwzlVghHdgmjV74A7rXDap80GXCpEb_mO9SKklGmYX4f_obwAa7QkXsPUH5KaMselE73QdaDJOEvtQAir5wboOXYxYj2HwAi2Ie37md4INQGxlVD3-USS-HEBAVVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vd8_uP7hc65AEkZye3XFmxdi79U2DiN4Ka8FYsPMY7L4n1e81u3-JkjkCx6I19S4Qerp05wGLb8vx0WvHv0YNn5JjtY_I-Z8-Tl_Nx2HyDDc1TZ-alyj23mls1H0OLkYfLdSL6GKJj8ucqXpg4TsHh0_E6uBlVcp0B3sQ2ndasAs7dJ01At4dvlt81Yf0MBgT6rjE1tgC1-ggCXEcR5kHSOaJ_I9C0w1-TZUKB4UkcgvvYO6JHb1VZURDy3nBFX1hu4BbCJW2Qcd5sDhvWrzKLu4d5hS_AEnBXfPyrlDtD8zPup3QK9ihGtonm-duOXoMJkUmWpJh2MBENPY07c3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=VYgH9_-BHGUnfLXJ50YWj8TWOn_ilfKNoWHHFUOrAWwZ7M0V7pZzfXJOtIcK-sRAv93AULZbCLxMcFD10bEnV0pvKKSv0HiYsRu9dEOxSg9SAAKJilkqdbsEJzDqcV-lq47m2OKUyarkQzHwH901lfBiEHRrCLqeMb3Y9aoHwWOVmsMKVjFpqMosqb-mvf1W3bK883SsoJpYNdoJ6rN9PWst-CZpK_07YKb7IT9CHLmXQ9H1T0pq5x8yTMvJGRWI6f9fcuC9PiuB9zKBVrDR5JOD9vul-BLmQ8wjm-KZtuklNYTOY-NrABVMlFKPOkmVb8Mm7vvmCV8_KrZ3Lvo0PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=VYgH9_-BHGUnfLXJ50YWj8TWOn_ilfKNoWHHFUOrAWwZ7M0V7pZzfXJOtIcK-sRAv93AULZbCLxMcFD10bEnV0pvKKSv0HiYsRu9dEOxSg9SAAKJilkqdbsEJzDqcV-lq47m2OKUyarkQzHwH901lfBiEHRrCLqeMb3Y9aoHwWOVmsMKVjFpqMosqb-mvf1W3bK883SsoJpYNdoJ6rN9PWst-CZpK_07YKb7IT9CHLmXQ9H1T0pq5x8yTMvJGRWI6f9fcuC9PiuB9zKBVrDR5JOD9vul-BLmQ8wjm-KZtuklNYTOY-NrABVMlFKPOkmVb8Mm7vvmCV8_KrZ3Lvo0PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssJ5yD4EsyIrMLTAGHHMaWiwQlgSpWKlSjs8q8WQTju4YOLe0beu1qi-3xM65F1wNYuvElKUBae5O6GCptaXGrB-huJ6ublRPQ23-9qyy99PkAG9UjBkv_y6B6zqDU-VxgrCemoA7XIYHVAPF0o3hiYu0d167WFyt4wfl0J2qZWc9QN4WlViiXdDK_FK9In1ToUP-hXAz4Xhr60dt7scFQpa5Uwb2GZ-3560M9B1csh9eDOXJW5ASQPC4OqDtkMgmVzUtLeyz6DNRklwhIEGvrM4iIpc8vccpBlJMnpK1AbutLJXB4G1ZySFG9HpSnpeYs_-caikX_RynkhT9WIRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WayspfynuLh87iwD6u31_xHDXUQCmhlw_cSwj2TJOxhNnzMVfQutRpzbIufe4cy3FrgD2eORqq6n4tREcdi8GIX8voG28rAfrVW4MTFy2SFQG2I5v2V0FICdQvWRxAxbOQpfLAVKQB_KuTMBFzvA-Y5vEmi0YUyMaP_eyCDMuvoParPg07I-_qLJESmCEhGFvOTsa8SuV-1gb5ClBSdH9sg1ABuVibT6JiKfMt4pVpcMKp5OSW4DSKm2rYy0K3PQ2ZF51h3Kpvr-CzSvLOhSEQmBrP200GfmhmgHL1MjNfACkWXCc5mRAqO4-EO2jdWRKak0tcAsFaEEAkInfUI5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=dkb66rgo7wFPf1Ezo1xM9b0ut9mbWBwnIxfzOL4U1YfFXKxLitqzefrR11Mb6RPDRlwQkSmkHUV9lIg2ecKhivX1BlohyTgBzg7Es-3wLxzowQf3q3AC2E6RxK-CBCbgJcdqgfrZkHptcHd92Ety-kzXli9o0yaSdeQL15kAJWmFGnhIQ7h-eMxmEZrcUFkeXwnYCMxGt3vcMx-F5vLkrO3FN_aBfRWsxR2Yz5jWLq9ccSqBIXZ7hQJ6agbG6hIx3GZjJDd6zgBDFoln5tq-HRgWEJ3obKPcd7RFnkju9ZQSUaN5_6bCxckSa6pDe73qU4abc6HHAwQxHzEhnzArg70cg7AIL2ElS20wNxXilamKEXySey7v1tAEHr6l60ns5xAnqE_IMyQbl8e9qOkC1OGoJPkSaUg46oefgQ_5stTUN8gtQYuXZybLBPkta7xgP2uuRAi8_W3QpyRgatx9Zy8_ZRcKeNMNcnyzL6wCWB45D_BQxZ712rGNqlM1AExB-orvTTPaKZUAu54cJZOfvwQImdg53TKM43PvR_Ow0xRtuED3Ke8KA1EYOakkcsy-SfSIpS47LEtk2EJ3XhJoJS9LZvZraPzjgTw4AYS3Krs6fCGpXpEanqJ3YR5HMVVMZt3LrqavcbPsuvXmxhci89276ZBJ4tpY9kjvLBdgc_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=dkb66rgo7wFPf1Ezo1xM9b0ut9mbWBwnIxfzOL4U1YfFXKxLitqzefrR11Mb6RPDRlwQkSmkHUV9lIg2ecKhivX1BlohyTgBzg7Es-3wLxzowQf3q3AC2E6RxK-CBCbgJcdqgfrZkHptcHd92Ety-kzXli9o0yaSdeQL15kAJWmFGnhIQ7h-eMxmEZrcUFkeXwnYCMxGt3vcMx-F5vLkrO3FN_aBfRWsxR2Yz5jWLq9ccSqBIXZ7hQJ6agbG6hIx3GZjJDd6zgBDFoln5tq-HRgWEJ3obKPcd7RFnkju9ZQSUaN5_6bCxckSa6pDe73qU4abc6HHAwQxHzEhnzArg70cg7AIL2ElS20wNxXilamKEXySey7v1tAEHr6l60ns5xAnqE_IMyQbl8e9qOkC1OGoJPkSaUg46oefgQ_5stTUN8gtQYuXZybLBPkta7xgP2uuRAi8_W3QpyRgatx9Zy8_ZRcKeNMNcnyzL6wCWB45D_BQxZ712rGNqlM1AExB-orvTTPaKZUAu54cJZOfvwQImdg53TKM43PvR_Ow0xRtuED3Ke8KA1EYOakkcsy-SfSIpS47LEtk2EJ3XhJoJS9LZvZraPzjgTw4AYS3Krs6fCGpXpEanqJ3YR5HMVVMZt3LrqavcbPsuvXmxhci89276ZBJ4tpY9kjvLBdgc_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7KP0Aotsw6ket_as82IKTekzg3h-ofnYNDfBRrM_tiZj21YaSA_AzKhsc6iFWRtrqHYXmWiuCk0aHxSMqe5wVYRrRW3VrfEDPsGgVxLXNqaVnxg0XJafr3gsZENsUw_fGpQtL82ayG8k2QyJmn6T8HrIBjIT9WVeS6mQxMkBCKhopeIENPWuGvWGXAp0oGccZfQh6qwLukJE9P-rfRuUijA5sdDmImDZfvgmHnWxtbKSVBM9q1HBoRPIEpvR0zD4ND7uPhVigCeso2VfZrwUETBfOGcIjgqPiLd7moB3f8FslNLLSxDZ7BTgCTwkkedQ-btup0GMQX4rL1WN-0DWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzki4gE-Op3wjjCfapM2wgmR35Rjmahzq9Oz9UtHIf7a4OSNM4tMBbqUNK8nJ2_vFcGBrDWfW0d6aOXHOXvyS3hK-SocKFwgHgRdbYEZx57iSGf8IeTW_tYbdtCyYGX-Z6OvL5qz6wuWDr2Yyo-SxYU7B8XX3S-pRTRGPARje7584i1kHPzsVSIyP79_jyWBH_LloBW0ScORlNeJF02HtXaT7Sgupfh0e1ivTXHIzhw3owOlxe0BjBPEwiiWpmqlq3ivFyjZfnboiUCy_CJsgG8y04twyqPBSREzcxATrquCcH8sd3T4VhtOVI1SGBfUrO8oKkWz8PQG8xroLFpoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Faqxun6vfBx1DpqDcjOgjeq0KPfV-eDPNh3qGteSYDCODMB-DkwNYb244RKtNBRR1yXtKjPTqIdqQtKkn9BwyTlAIsDsQ-E4-N9yAI0c60MEPkVuYv2yL9VkEmzFPu4QTsML-VRn3IFHd4jYvRUepjYsQ7aVYjFqmHWY648k60R0p3as726o18mpaOfRo5Uu2-fmYCGeLNg1PZGkxnEdzh-dswQC3luCyIh3Z48aQH2Tv6LhKqglgLy_veGezTSawrAAt9R7eOJCeNYFUkd6EvNEd9AdW2sl1rwm_xx5oAFBEEJdogJ6chqjwUKoHDgeenMw_fj-dKsIKlhkXzJKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei7jAzobmHJLPLpJLXe-JhhwG3V6sjiReBdvIO0-9dVmH64aoJZqazEX7JDRO7vbeuSXIylaNqu5THcQOZLOqCmHoggegITFFsNAWgUg3ecuLmSPvUcw-PZROhQkPq-9NDB4OFY2SibXrKKWem_yxmIIubgdOblSTksoA5lLmzcX6poYrP7hgfzIWMVzjyGWqWC-Ym6RcY_D1c3-MZ_aq1HXAs22-1xkZ9LT1uQzgwWijRhvK6YczjIJm-dbc_Bt-dilFsdtj3TgUVjkeV0FaHA8RKsIVFejb4tkM-MaOdsZ3F-dcDm8wHS2Z4fJI2-3LAhVdBx0WgCCChkjDTt-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=oGNDXQhUAV78IObrcWrxWhuHAiPYknQ9QD5t90bOnEXInYyOSkeBkFuoT0fwMUInlg7IXSOEWQ-hzu7kaD4o7FKMMIEkQZK55akoNng_iCFALEVz3SZicROHq7IZILjIO4ZAMR2oELPJVfoDJ8Hqjsnbyixm6Y2LA85UdRuMdENozW_kJ25MAg-1xYTGM088TmyvkXvWqjTSN2Ydc_CE72u8tNwUpvewEqwHSyiXIC4thrZ8ersxCRCoVh9zJPU6FvoGegC2RpLGP31z-bhWXXH2NCrCXY28F37HrrqixnaFn8GWBl2misgu519HQgcHRYGPQFOg4QZSudowk7V_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=oGNDXQhUAV78IObrcWrxWhuHAiPYknQ9QD5t90bOnEXInYyOSkeBkFuoT0fwMUInlg7IXSOEWQ-hzu7kaD4o7FKMMIEkQZK55akoNng_iCFALEVz3SZicROHq7IZILjIO4ZAMR2oELPJVfoDJ8Hqjsnbyixm6Y2LA85UdRuMdENozW_kJ25MAg-1xYTGM088TmyvkXvWqjTSN2Ydc_CE72u8tNwUpvewEqwHSyiXIC4thrZ8ersxCRCoVh9zJPU6FvoGegC2RpLGP31z-bhWXXH2NCrCXY28F37HrrqixnaFn8GWBl2misgu519HQgcHRYGPQFOg4QZSudowk7V_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5tfBjv8OLR19ENjxck-m-nPE7XwwNNnql4wr3UoBD3cvuwyVvDJ4nUSpaEIZVrq8Mz44UhsUqv08fVNhyL1D0_uFseDdIudZoTa6vl6y81eEmm5P1HjaWVVQwPw3nfqvXANUwm58EMvUbicLPhZ_VSa-a3ZNh38FTt1CV7a6VPukeyIqaj2N2UTgO44hLBVeSxCCmX3PoaVMGng74wOqobifEwuZQ_1mNzE1ZNyuleIVgtPTpaynXR_MoRLLXVaY2kSERW153nSRo5NBl3njByAvBm47AZhurHD_MEUk57lbeBp4zjmdwQn1cPpD7ycDVlVz3kGHOTTmU1SL4urFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwhIWUcTxn4g-MjuDE_VvmUk3OhvgnBEg8yb5rUfLo41XHw2iAC5OvuNFZHsag4uSozH70Icg5SCsHaQ_oYut8FDMHIRG7BBD0UfTFRxlqQkeo82UW8-mvD306QLxIid9w2SbdWNmC-alPxqJX3HfLWCcOFzalKAlFQI0PWAEYXw8Olrq0CwTBYTbDjue8woW4_fliRuuEJo1G57bDW7mjOeCgtrMBb23eTT1Xzv_Ass9pf7SEHXJQ5xixi15lDIHlyjZ8hpW9KFG2BOBWdiSKSxBZzcOAVN3JxuIBweExUHR3dGAUtQDCM7FJTkk-8fVut1r1hdZPIXaZQUZ9nH6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6OcTXWmLT3Xo8_i9qL-DK8DagYEfosrRqABSQ3E4GvUq15bpDtt0ZI7MnkIzIFtHlcy5P3r7vtf13RtaTpSUMOFKCItP7FMQTGTS579Q1YEzfoJUHahVT78_Gyjz0qIjYAyD9SKfPADxz1TA8jtjSt3q4OeaJ83KzAaACUHwCvC4nCbk1fiS_0TocQKXk3hoEVSFsNefT6rV_qgY3rMV87j8JtqG4BhlyVcaxL_rPKTxRYaVV0X28f00ksXbKT-4A_wQsPqMyWPg0yPySehiN1P1go1wu0q7a8lJ6VYek3-tHYuvdj4JVBBwXTU_wvNmJD2ibGOftqFiuLfDZRLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHjYfsqDLfdUn8aWN4SS_uWVyWOFvP92Wwaym8dBaOSyBfWH4oCevwVFHi9VEBCn4ocTufr23HbNQhboN4Bs_s7yvzQMYfPSwloYO8yiBwtBxnP5hRTYjoNPVCflCgp0IpEbRA69ZY2aRDgMeO6jMpQTz6tvytMh7YMOA5rBLdsrWfvd7gsj6lhKchPiqgYq5NUb3giKoyS8DbwhyFcZjeACHJzycAvKdGdg-f7RQigIV6eIDeg9805uFD8cQyHLp9FA0HiWudMyzW452OaX96URuvXVxHRo1Xn2XnhEGrlIFdMR2-g3-jdrPqdgO9IqxpvvA8sjDHeoF-xekrUhaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dy9OMHIdbqhg04x09ga63RteXozplVrb6-1Tc8H6qpLVhJNf-ggqjq2GdUpBCoinsc1VeLC8Qk2_MKArv3EZh8RqIoe0Uzk4lJq-5pZmPBKVBbFRTeLtetFjgtWai5YgECtUAdPl8YfQf-4e_h86m5QdUALfTJch6ek2jBEr5ud5J9a3PgKAHnnfl6yXAPUxLWBvbb8ov3JYYFFYR1A3Vz5NH6lsUfUN_M7RgVd_43eBejYN2-WsLIqAYr9NTLPH19E_3Gq7ZaxioT6Zfj814BmM5w-E8bziTNz3ATZPfIBIa0kLvUGj6rHMM8BlySo2aRfL12h7D51-4VpRHnzK7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaPYb8iqg36l7Z8M1gOFB_O7iApIFkPxOIhjVZN0_y74ozmn5kCukkZR2a__kRByc8f04al07d7G1IGp5csmOLPYUvB56W1dYrzlDtpmAa2P-QXyEA8kkanj4mZkdHyzDXt8-8OBlrN1kEqgoft44Y-Fuzvq2a9R1-fStJDqP72m6f1HnJ3QjDtv6hw1gEA0TTcRPObY0Dr1rjscs46XOq63-l1iiJC-sihRLu2dC2NIMhO7w9us4XriAGnKIVRaTXCjMhCM-N4AOUCv0o1abswB15NHApGHei786-t8oyH9e4zp8oYudmOHX6fmSMnVcEoYjXBfjTfOSVs_zjGVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlJc_K_C-lBjiECi_O9ygf09FEW9bzvyrzW1mq-bpYyk0JQKNTYbMltL1oTJgHCNypLhpyelto8sKfQpwUvMQzcNG4UIVpFaM20ZFPL55FCWtQScVNGdI2xp9T_ihUeLdLugv7eLwH2ssdpyrD1XdgpH8t0qHcCKYD3p5BUFRwU3QpvSpamgx7hth0kkmzqE2aylyXKq0aYIBuiXRtL5znNXLnhsaPISqDLVw03Oc1jOa6Ttq9OMy5s05JrPR_j1kPPhjJ2_SiHO_D-7Cco82m4RrxDlyPumPg-uPDO7n4inEE6b_YiLikMsOyf12Y0QQxyxPNU82SFv_Qeqy-BwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-43UKe1kMzXOjPaxypuRvnGARt2O5eO2Sk9MhPOXhJvR1TSV56htzOr2lKQmCM6uZV6GNcRu3HZnJwvfbTdYcdBkMVi0xSRWGVPBXFvJwzeDahqMTA1P2SUO0ES60r5-fyQgjG52tqk1DmkKWOTryHgL-GetzA8HhH4DRhpQ9oslpP-iO_juTePo7vJX_hIM9laEPVOBLwIbl0RapwO-mMwGWf6qVV6QJvoVcrYFtXt5ylI_iE9NhzQiAiVyyUOTHDp7SbaRwmDM6a6u1G-TRSlpw8BQw7E35w9gxKAEUQBQvLqM5RFdgFL-21r1IQnOidvftorQxBcoM-eyWuuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZT3-f7tpBdSAzv6_1OFzxSvDcd8pWAUFAJ0lOA2U6rXUJmX6EyV2LoESQYSUOeamBw_ibGJtj799qWv-mscP6LPO1s0TMXC7qw5mJnuC5Anw1zCAeIt-K04s_btH61MGCD1Jy--Tzlgc6VbpuXDig96s5HgRj4P1ynVgXN0P0Oe2xqO0ruolh7-8xDCUclsToiVJkSLIYVIFQqfuOh4BXilMn22AqL5Yz-usYmP-FvXp22S7oJCK0mjq-kdyicbyqNUHLT5hK9nbMfYuvqvFaYuutMirGOIGjbgFXnKxM_rWS8zveuVctKvxLesntjqS4-oHMaTBq6sxGK6ALmgPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzj1rtUm7hAZ25-HVlA0dZBVQN7W9SOqxhkkdJ5CpmLnBoJFZ7-jvYAnnX7YUcheN6b7FewEqNiBcTbAw_rD9dyf5GtZGQIZH_GZexLaxe5qwpwQIbVKtmIMWSOXzA41AfhU3rNnKsMgTNrpBSpzf7qdYmum1HgebilZ--po3xKKyI1x63BEYT26z8Xnc3Ce5Xcnw8IgPPPMQgdkCU1ygX7NpEnsy6NwJjCQDnvfjdaVYjNdFUju5xebI2x1v4koSKr-RPVUaWz6zqZoX2eVHRw4CUDxZUIs6jz6aWTG__PU62iRlv6Zn5p-pYNSA1QRGnXgRjkUxCJBT6H2LClp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDq-7Cj7D_GHQClMgs1wZBJqkUijnhkJt5JghspHIzf4lR9xz7ZQStkR-GALz6F7kpjIsKdzZpndUDqWGlwNLsqSM9Ya-VXY_xd3C_PwdrXmF4oGoLYoJN2RkUPTgM1J4Yid2rmrH_aGilbstuWjJ0BNe57tdl5LAueXUX5kYkpNDuTLHTHEuMNiZ7r1oT9Y-f-eFDBp6NaIc1Si8uTOsJSjXoASo-jLfJniQI3I05R2HpONFFBZM4T9uCxpd0HyAETvpzB63RdtvrfjYvo8l3BBy2aYnO9k0y3leKxdzHTahb6yDozU7XzunU4Hykeh0vzd2Cel5nLMBPKsyW52wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNo1NsgDE6-fS2r3hNl_NPiFMzomKcmBPltU_D-u_mzmxRSs4nE5fW7OdmKJ_129ejquyutTWN8GyJfkD1VLT6tcX2rjdZLiML_ALjE5QqpgjD6rKAmapDc3TfctMUhzAOQOYjvFDvmWZE9AobbH-cjT8OBgLZ_MSXeLSE0QTKVV8tMjtzv1U9jDO2RmrQSYExSsANRzB7ALbrSiJPpnlbl7A423rjkrN6KOFKD7ZWFBwPkd5G-253o2-y4uEu3bs6ar1UpXzigeVbmmEu238_GggG7vkFRlL2pC4Ijof3rg8egc2UGOr1Jz_tPFiIYVfSx0Hf7xAKEjHERHsOZRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPSXe6Pm3-uIsVHakwfsa8hdgFKvNrPaFY6qyNIGXudf__3pa4pFVVlKKGMkV453a-V3Ldsy35uyW0KKRD4kzZDvBIFy85VUkb9u4wuwaZoPJms5zGEMB355oqd35uH9PAUWZGGiOlM_Lhk9Z6Arfmyd6bwrOa34N9_Qoj3pDYLT0iFhG5DT0e26qSdZNCGmzy-zM_Rrryn50m2B6ozVT-ugJUnAstWIHjPjyHvezGyOBZsSEwdf0mavT6GrEmfaZNGyfSl__w55HfSuvxfkoE2iNoVps9mA8j2zQzANNcf8jFVdd500Q8xTkMdulbE3k8LpUrQLySg31nBIeFumEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhUHN6CBEuor2VzAPQZAhkVzuqVQv7PDE-soiBEDzs7eBR0G9F-KxD5jxqb1o885ruosUapeEOm34C7is11LbtmJeNSGAGX3quF3NAS9-3Xxt9J2IIlCGwGkTTxyqpuOj33NTc-FS43fyOnE04fCIZgxlf1duS2y_JvwVQPyqM68dxs_RVHwbnbbIC3x6TAydvaMndE_9o6OF1Iw-3vzc2e-UTe8MHzM787z1VN5ZSx6C0pjUU95os1vOroT1g8TwBjAbb4tB5EZDkShHn2zLtipdWmoOF4Y4L2zgL5pDYPV9_lfcGtqNSU3_deizc5MJsWc7EuVz5ZpW_mxPQKh8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFFRm1lqvPgkSo6BjwWlL2SBCbSFCScWUvTjVRMPPNvwUzNkt_M3EVh8IVoLJOCsaqnl9fEd0KnkDG7krjh3NTBdJTh1jpofo5LsiAm5pwmveU55t411_nMJny4Qf4GbbpILrH-ZhuxuqKb_H4kadMFgR5Q89yKIdialJnQlWEcIs5Wt2-Gzo5wHJ0fktcKJmdHWZ_eF0NxFmVcjhJe9eXPrPkTfGuMeY1SDt7i5_QFyfOuXzVhoaCXvN3zix-3XgPU2nt5oqHNPUo08eisfz7edYmBErpmI_22XlB3plrxk8sBB_8Dx58wab9dNu065oSzYP978wAUGNP8kYpjOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHJL_y7y4J0D7BoTFZ6nPz6QrC_eccCbxlV3kZ7uR_hQgmfzqBpMZV8pupPfUW2G5vHYrpcCXseYzPDIUecyfFE0A9ZGncgFgh8SxMYVUxLOZRw6b5KluCZ3JktiFsTcap3lN9GJcwUUp8vf5jSrht-ACx9MZjr0IjgRzJxsQScqCRNIi0mqyRYTRnXb6PxLsaupacyAUr9gLlQkYamoC4lnPIG28vdLYIqKtaUsOZdisglWyvStke-Z4u1BWxALmvXyGideRPcjmGW7BAiUxbsRTnV8tc414xYNnxjjvVjRMRR7upgpmWgm_yS9UTLvIMcHPBdmRTkn1CMrbpT3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AL43B0SIDyeTrMAFIZiwRECgrODx5ZTGv1Hc6NU980etIr6i9ArE-OBT5TyIjiveNTtw6GA_083fkRIGbicvRY8ttUJNiLo6L9Y1PT9Vm3gZXsaj2AQp1ZwfhNj9FAGSA8zjFDUawSzNoqeOzV9j_VgOtG7WntlKwGtXsRvRW2gJvaLFS0QpBhZIZyzWBdCoVtY8-_7-41w1tETg_fh56cvj_V2AGXbZTDEWQgT3FeyVnJ9HMcDJPmSB-N56flUND0RXWG8ibQYEWLM7IyWZlN2hWW2IX-W8WxCggzENIH76ZA82xyj96yPLO2HOD4pmnlAR-hVv2TV8E5x8Cj3myaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=M3vrlandLTnbBZ2g6iAFAXFyAHKPY1BNvC3bqcH3WOi6CnhvPs9O_yQjHPJTUcP1_kVxWfjNq4LOBQks0MrUl_qeZskU0J0xlWEfjmnu4dU273a-TqWdckZ7Px04Ixvzze3uPxn6f40sKfXCLuNlMU56HG8SNtFq4UrlYswC9GoKWOzCfDKBQ7200IcmiOtDKK0VHsli-hFNxrTcVxTvZm0tuWGEj52xTql0apzW6KVRMa9uXVIVwgoFxphc6D5f9_WgUtOUjKf436fY5nt_70q9SQQBUantJeoximv1Pt6T6irdgogyL_FrsJgEHwrC6rRj15b_sHTYsGQNEO25AL43B0SIDyeTrMAFIZiwRECgrODx5ZTGv1Hc6NU980etIr6i9ArE-OBT5TyIjiveNTtw6GA_083fkRIGbicvRY8ttUJNiLo6L9Y1PT9Vm3gZXsaj2AQp1ZwfhNj9FAGSA8zjFDUawSzNoqeOzV9j_VgOtG7WntlKwGtXsRvRW2gJvaLFS0QpBhZIZyzWBdCoVtY8-_7-41w1tETg_fh56cvj_V2AGXbZTDEWQgT3FeyVnJ9HMcDJPmSB-N56flUND0RXWG8ibQYEWLM7IyWZlN2hWW2IX-W8WxCggzENIH76ZA82xyj96yPLO2HOD4pmnlAR-hVv2TV8E5x8Cj3myaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=QVYUlZL3KIPoNJuKbFNAtdlPuUoNrHdJfjrqqp5BgnmODUDPawtORvYd-_H-K9jas22RLXXtYjg__PrxU1L5YGzWZlm0e-pEhm8IGk-7HJF-TLGcb9e4TJtxSbLhiiMsunvLXUb4zEddA0e31nJE-HMJ25Ii1oxMRvWEbCKPgoMP_sw7DOnYT9EnfMbqgZBzvbkxBDo5-n6euxPT9KEaYGZ3uwcHtXd9fKprLefKkXVW-8jIBd-YrHz9YZkdpnsrqYiewEQJJinXEt-7ZD-spLltd4HTuqbhbo6laPJPbB84KKTQ2WReU_f8ujb2InrtRgPaywr7KmbBvUDGhxqc9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=QVYUlZL3KIPoNJuKbFNAtdlPuUoNrHdJfjrqqp5BgnmODUDPawtORvYd-_H-K9jas22RLXXtYjg__PrxU1L5YGzWZlm0e-pEhm8IGk-7HJF-TLGcb9e4TJtxSbLhiiMsunvLXUb4zEddA0e31nJE-HMJ25Ii1oxMRvWEbCKPgoMP_sw7DOnYT9EnfMbqgZBzvbkxBDo5-n6euxPT9KEaYGZ3uwcHtXd9fKprLefKkXVW-8jIBd-YrHz9YZkdpnsrqYiewEQJJinXEt-7ZD-spLltd4HTuqbhbo6laPJPbB84KKTQ2WReU_f8ujb2InrtRgPaywr7KmbBvUDGhxqc9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIa1WM6LDhTPKHks0LiyWQhYzpxqYAO9itzqOZS4pFvXBHl35To26SyRLGIS8_Ff_EISrtLJ_cvty_uTRQMt93-93d6zbzkazebN1xSJBiZtBrEsz5h0pWlqz6UFBKyerfVZz8wpx6JbzvPVT6AG-6h_RwMvqyCQOem3wZg8STgA7_edW5LVl8DmMJTaSSm_CxQHRyipQGMgtCJrd6UeydOVT8nx2x2t9lzD0_LDuEQipUfwMC3v025TJ3J0hxNgI2mDVapjJLcG9gX6ywf4pQGda0T6IoZU26u-6wj9EAV2nkQ0PFDUQQhtlyhNdMDIluinNFsjjkcf5POEbWpx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEJvln3raRmPXH_BPnHI5gdYJ8ENShvt2klyj412xLhQIWXUr-P8IItUf15qD6O6jTtb4DbrC6cIMhjcmvvDhpKqOt7AQlN-tLU_SxjZZW2A4bymkA62T97EZGHnstMLvTnx5wNYkB-IcuQo-bn4CuyjXLQgtMq2BiFb1nx2DETnuMlNFay19m-7e1TPp9_ihBYCAvfrRLhqmiZTvixMXI4v1VBbApO5eTErCtmn46aj649BPHKmvoR2l9Kx0ieDygsMHp7wHJDb6FwD_aAXeQ3ijd8Ea4Wued0aht_6sQ9XidJCRfQpWo_LwGOeX_pS_WaLkWAb-IPrmh79TXZpUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eB_yyeqe7HCFOkBzp1nH2_3W6LJ598VzTVyQu_LJer73Hs6luLkaP_sq9RMOcgMx-10kMgXnnmEOvFa_mydclz5kGAVm3-rC6ClrKbokgVop75i-wJVFQfyqLMsr7mueWtQ4HWaXdoY47itPNo8DOsxDocrolvrYsePi2iMX-BxGdhjBvK5U_qNZQEcaeyXhYU-H5oPFAC_DYtSXOSICTKrNw_BRU8X8U8a6ZTVC4TPE1SyfdgT8TuiqNTJ5pa01tL2TuVHpQVKXcT7cT7o7Gy2UNRvCJWgzni3K-cT6-RxLyN3oVG2hA9TYq-IA-7rgXr2HPfHF9iBOxD_i2Ira0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEMRKcdUxhIoIyxDwqgSbbDyPRaeB64f5Z6AID59Oij3PVAc8NiBgXfAscr228esHosyN2wY0Sj5FGFttjA3Vd78JnfxdoEOUhy_bMmyOgaD7yoVfbllqRTpqUZExnhPFINcjRaEoy78vb5vqDyrkNzvonEO3BE57c3Y5tQ_pYeF0H7jfUI33B31TozBspgfVwuseNGWQ0WpBizjc3lQcMKJd0rJ3UYDKWY1L-PEYJk0mZmIwLF3N9naIrSHkEff0hxBY9jfwyxnbMWX4H8uSFQfH4EFLiq-ylPbUe63N0DbKmxaofUMcoAq6vU8jqzn05grCRyFq_LJVs6qAXYtiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdBnh_lx5C5N_QonVTapsj27nBddZ_Ay8eB95wM_XrTht11eh7el8845P7W2cUZHdNytvLzI9qbQOSnGBicpaq8ujy-sbAV72cRLYlGqkTM-vYcu6GHfWz_pv394BuUUG22wduupaAcX88_cpDU7IhuUFG7KJ-HxlB8NFGJgiTfrVol2gjw_5m_-CJcJtg5CTq3lzg_x9Qt3ukIdaoYUF3-x_fUglGRAFQdGVBEOqXNOJ8xPHTs2MZbDzk3MEG20Qcg6vBXwwlInK8g-gv45LNDy8crexDU45AdERlP_tWHKwdxkLZD1KsPxIMha3vlP_8SJrnqemmw5kK4lcJyIHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPBaEZKZqXsuo-QwWHO7KjEdzDlHG3Ywoc5CH39XO4snyMd8atWwU2Nhu6UHLfmQBgMZkJ-8CA2Xobqv7QhLWSi2sHK4Ool7ILAHW4zubvYruO5oX8zYB3F3D6KDZWhMcGptz-XUd5OeyB3Bpf_fIuP8J7XtvM__qtl7wqlwqlnKsk5NE0q7-HVAZJFF6yRXu6lZBhBH5FhaO1kHTuyd60rN9mhCllQCc9Qk7scFy8c_ZPedRN4gz51eCpi9b1-m7DwHp0MIitgawXW3sllYyXMNpMtoJcBY25sA4ueYoJse0gfJoktuHmAgRILKbmFSjIoZyEX753WwYCHeG17nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRJWVJudXI0t91nReRksZwD6HCOn3jsq4oS1spfH9KZ9WG2d8ZZcT3h8UjkcCprcLIrAvKcD2npr11_bz1Sd2Xb5mPYq4Ht0FLVsLssWzpIqKi_5tDxH6n3v3Mq0JN7yKx067YdMrSpvGGG3aXl3tcAI78QmCLf0SGMcQfEnznjLttuBSqLsR8qUz7oRrkDEGjsEPa3_8YJJ4aRgWSYgp25nyDIt12NgzgoVqCANzRbER9T1YBI6-KlUSU1_0y4TGdsNB-pfaI9J6icx7ydKobs-flBw1GT-5hbAAdlIUm9wcRRmfQcutDI4elp9Y-Vs8EU9dMy0Anyd1oTE1HK3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irSRQYr2P4sDhu7rvyssYw2DxJYSnQfWj92hbe-MmTTdNI9D6TYn3FrpB1t3QdYuTpIuTPRz2LN5rLJa41aLoSbEx7LzQzLUGEEmajTb37LkNDZoU15EujbUv4rykPccp1TSo0wklOSbeoVz5Y0KKhLkyfOJ_FRR9btDaocCzupIYY7Ibj4POrxklq-RxcCfwznzPjYsDZopY3RFBXSJPCCKeSNr40yJWmVqWuXnAKMcUCmPoCeXwiTIuPpYUD2zlNfEdgyo2cUYPjceBwA9IezmM3LawebCJhJVVUVV3E_zD_XIpRMLLaZxfz2DxACgzIcaR5M6F-BuW0SjrsUPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lL5Kav1f8-WwMMCk5LV-PLjGKjIcAGn48qRMnSh8TX2jnP4iPnL2ayiREJvd1fKRCiLUPSaxjTZbKM6NQphINKoDvkqOifM_QxpRi_X_W4dwJn63DNmuRvj4vjaX-HgCaevVxPMZ_13Zr-NBjflBRMlnH-_Bb8ydI4jkGvIMzlW18aD_u5PHljjJaV2fmJbMLHtqrzhZ8i0TCaCUuBQOz-myXUgkA4BqYd7ROu9IoqWUxLIvO3jv3h515RQL6xiyYPH39b-n2yvKKUyvPt_oTyCmjZwFCQtR28bt-LtZVz-ZTg6UxH6GxUG_dTD7ALZPsoZNCbnP3kT7kd03d3ED6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU0aH_vwJ-hdWpgxES2redlU8J2-bdfMytvWDM609AEZXhAi6OIatUyEyECGeKz5VcTTHrAfHXN05MDvLdrcQF3r0DozM6bYrB4qUeqcp5kFc8qHjzfar63nzez9OO-_6RXu3m1ES7qcqCnfJifYUv3TlOcqhQxiRfST919Jq0oKyHSQQoKBaDHwaXOAzTqidod3jE86o6FpA651nopL2El216xi2pLfAiTCNfJ-qLjC-D6s7YjEuWGxoZl1IB_PvRBlrN412KroWySYwZPPwstsVjtTs2ALtfpj9mb9OtAd7ZNipsr1S6kJ-1LcfIxLIS33ZbFMsPid9xikZLFZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=ZzQ0YN39cTljPczJzopj9xVKGZb1UmXMY0IbyGMtMraLilgXYmZoTQG1ks7158tVIyIazo04phBKSVZwrA6tSra996gQNkGMkYC45BnSSoKfWZEDvYFnHRJ-i_h8b_zxpk5TUos0w3OUdGgmkrw46eYlPCUKdkSBemYo1TFLGWo28L0COA2PBEw3mJWSOhuVeDLf_a3aO10DHJER-gtFwJVTvZOB0rOt48W_lJuq3NKvm2q4yYwOsu7KFkC6-Z3Pc6COKIrtRe5CgoXezk6e47uhSfQ5XfTeMT46c8RsArIDy_4GCTBHGuM0OiPo5hg09D4Tf37ljT0tWFMRGSpllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=ZzQ0YN39cTljPczJzopj9xVKGZb1UmXMY0IbyGMtMraLilgXYmZoTQG1ks7158tVIyIazo04phBKSVZwrA6tSra996gQNkGMkYC45BnSSoKfWZEDvYFnHRJ-i_h8b_zxpk5TUos0w3OUdGgmkrw46eYlPCUKdkSBemYo1TFLGWo28L0COA2PBEw3mJWSOhuVeDLf_a3aO10DHJER-gtFwJVTvZOB0rOt48W_lJuq3NKvm2q4yYwOsu7KFkC6-Z3Pc6COKIrtRe5CgoXezk6e47uhSfQ5XfTeMT46c8RsArIDy_4GCTBHGuM0OiPo5hg09D4Tf37ljT0tWFMRGSpllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx77QE1odTs1icuBcXKRM9u7fsl0i5FOy8LvLVUMwbPCSkq1qeIBNPzJ_GQa6c7yvJbhFg3_2a1_ZF49qzwjZbls7GksLkQ-jn2OqFtrbXkzgIoDIEC3puxBOxd5mO-V7y9Q1j-qkMptATdYsSO4uz7Fdau9FyaSx7hdouWQx2uqWGHJj3IvKX2ZUJMZavz7XTibVZ_YvMFKkSMuRd6EVEJbFBOwEyMir2lCkOZctdqbVDnQrzQbcuiU4D-vKmj1QdIXWVbY6sKuhzq9X9iJ2Q6SbbC1Q4ip0yZb-dU88Ii161Q5WTACaxNOJ48kqrq5x1I1ttoh1-UWuM3yQZHdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JO7m9qhFdmRKRDeQg8Z4Vb53MiGC4lF-umxS7Q9QROFKN5hcUElMlDNGa37o_4YkcYR4K3MnWiOi5PR6M2xY3Yd0UQGwFkcmN9XLXET-X0YnkMv2mBBAbR5VjfRDcEa-ympkuy3ANaMkaUGO91TwoF9SNGEcWL7n52UbnWR735euRsv0cJ99lrcC_jYOyOGQ3xnUnrxmiFRAmPJOoHoxzYe9k-Z_kSiIAIThQSqU5Gx-sIlkEyZ2fbggtWCHTXGCufkPIbZIrxTespyQkHXcz7JwwmBVe-Gtub5C7albFykKMZCim8_MUVD-CDsRADNS8fLd1GULpAczZwaGA0WGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7Oyj3lpGSVEY7bu1hSkjpBLA3a3WZBob4zXi-A8n9jZV66UmWqr3K_E0A5QF7MsPGfGw4HCNQmaj5lKrQ3JAiCrtphy1uadv7rCqk4lPqyelK_mrFZ8dnuemiQ2wBB93GF573LdTkAP-FadNPdvoFV50TtvxfV_LEdWDH4txtTTmLRGpwltE-BPAeDEFfM_AxSoa-AfjtcyQFChqMhx6i8s_n5poEpvR42nf_bBr5ErvkWqIKDQzq5Xu4JyiqgdDKeephlBD3xjd0WR5_H6FRxC12xZ24YuiTAaJRKASEwHFNENpwjsV7C8zZmBYV72FaBP1gUzpaomr5cZbuQRDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFTeHHeFsCyWuF_iG6d0kS2ii3nKrF9kJdWbxkoT2CbofoGo1EsF0ZzTayd611ZTnpwg7FyyDgmN_PBBFLXbzOkEwROkWIhS52AoFg0VmDP4oZMliT-nvGCVHcJbW4J_NRr2wOlC-LBlY5gVNzX39mpiggtiDqWJgXyZ3zXCx72fX4F4sGyzUqLiFSmiSoX2ZprF9eergY-skn-eOLXRDDFEw3MteFwYhGzYhkT9PX1uXEc8GgR0IP601eLk91aByeIqxeRwUNVbAkgnU6l2C96I93Zbv38a4zajLK6Ui3okH0BLO80NuagoVB3cKejHSQrzY9FgnLdn6sI4J42_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ts0pHQHGjFy13pO-jAoANszxjTwrwDNJG4VQ-YGyAbPSl8OYbMX5KqCQwKq8coA6Tmmz4yzlBDhufkgXnnjfPGjyY725o3OHERRg__XxAZ3S-J6_RCcfErqzfSsJnZp5tQ3RprKSod-5p3HHyS_JkY-sEDextElNFvXscVsXFwFkc9Fl67XnQ9Y-cCBIJby3ryYOvTA_TuYQHsNgN9vpSmunAw-twtv8DEzIJNjnYE4d0que0VDI5UBAzO_ajmXYjDAJEMdqmCoj6i1G4qd3ZIUzY0Zv6ohO484JKdhbepeBECHczkjst805rgfRyCsfOMiGNIrX39mP9DclK2DdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI4IJs7FMMv-096mZZmYfaE1E1JcIzKs0a6T766Vmk_epLOt_LLxmz8VQl-XH1GoDWU_BLWGZKO4Y2TZqV84QpkmZwUfykhE0F5htBh6PyyAEhFBu3osndRSYm09UIiDluB1KsFQ84rsVOZBU6s6xDkBJ9wEWoUdNXQnP3UnkTZjlY2JetTHr6RcjeGfBS97VP6yCHuTF3a7yWyJepcKM7Zu1BA97EKjGjg-b6Y8UahQ9ZPOajbVTDxJYqGNyy1A76jNeBj1maedRlP6w1NapJITxgl-Ha1UVQympnQ6S3xhv3rGVVWrrmFAlN8jLCP0zmBA0j6p72tJsPXNuryGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxnCqN9dcJ9vp7lcuPkksgps1r-9zjbAYOywJZhP3qRPEbwToXRXojuV2HQFx63BGdO0twZ1ELJbw45gbe13nPYIHnmG4rbhN5s9DhxzM8OwQxs9rl0aq5P4v8-uqVUfQ2rKit7-JZqIsag42UTGiCN6Q_qNzcNCG0HmgNhneqyIgU-fh71aBQYR0NxcWJdA0n9zY7SxkY6xcWt9xeVjPlwa_BwNz2J_X5Oq-3sFqDFfUzEuH8OwudH6xi0R0ua_BlWfBF3pp7cUbGPzfQ4WqWJ2Bvur_PcgzXte6XZMywv9ekFhpeT9Y6nNJZP-2eRMfWcIIzjeQlx4uhHWuer5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

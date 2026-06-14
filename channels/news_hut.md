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
<img src="https://cdn4.telesco.pe/file/iv3EvOwhabNKqQNzrE-bZyuzblLB216nD98c8-EDgDyXtL2-9e40AlTv1sNT4WBhO4yVP14BAUcm2ycMxrlM2_CXDcmM78befFUl-u2kqLZa7zFrHBfVUeqE1h0LSx4Y-cp5jWgBIWsgp8HAPcDfUx1b_z6E3OltQ1xWLCm_Ig0RNinTtFKs5U5VbSID5Xznj9OGl8h3_0JMpZWcJ3PpB7sVMnHAub7C7wdgXJAjsn8YRkdHbdus4loXnBwCMLIndPXo15qVRt7Goizq6GWM0CQGnZyFTb15uSt6j95RoRQZewfikxPc9M3eCMBLAXtmUH6o806DXE-0EoKC9UPoUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 15:50:01</div>
<hr>

<div class="tg-post" id="msg-66070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=XufJCEUxH12hbA6lpnk0Ll7dAeCxEuAbmDzILRpBSJaxn3WT93oH7Efz5oLgkLbR56-ol2rOCwXloKK91PBZy77ezRfcCA7xitQz7RpLnc-zgAzb3DxxBte3s1BHcQ5-ebGVhGqTus9nWhtuwKN_pIvSolQYJdPMycn2uwKeskSPuhtAq6r4fHapV9UnfdOqYW0ds-ZzL43ine7JgV6DqPFCM-27c0Sb2S1B7C6IuLBaUhxdD6lNUVPlfp35gqKjYkl8kiHnS4XmdmZhLDVDrN6Z0q4EwXr_n4bo76emJFr2yAmVcLR-ED727hb4BGw0-WwCAwOf3EQl4wxjT-fr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=XufJCEUxH12hbA6lpnk0Ll7dAeCxEuAbmDzILRpBSJaxn3WT93oH7Efz5oLgkLbR56-ol2rOCwXloKK91PBZy77ezRfcCA7xitQz7RpLnc-zgAzb3DxxBte3s1BHcQ5-ebGVhGqTus9nWhtuwKN_pIvSolQYJdPMycn2uwKeskSPuhtAq6r4fHapV9UnfdOqYW0ds-ZzL43ine7JgV6DqPFCM-27c0Sb2S1B7C6IuLBaUhxdD6lNUVPlfp35gqKjYkl8kiHnS4XmdmZhLDVDrN6Z0q4EwXr_n4bo76emJFr2yAmVcLR-ED727hb4BGw0-WwCAwOf3EQl4wxjT-fr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم اکنون واکنش نتانیاهو به توافق
😂
@News_Hut</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/news_hut/66070" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">طبق گزارشات رسانه های لبنانی حداقل یک نفر کشته و چهار نفر در طی حمله هوایی اسرائیل به ضاحیه بیروت زخمی شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/news_hut/66069" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/news_hut/66068" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66067">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=U0SQg6Fy6-fv6T6Phkj2R87V6x9MTaI7f6JrIiPB2KMJLsMxLZl3s-TDSmnhJgfWAyl96-0CPoiSfTrJxACj_ph6cLSUbQRj-My3qBtsetcD1Yii_t41E710pF5eF5FzoHnCc6bjcAUXVQuyQtshpCr2GSqD-XKiHVblpv6dwikIvwRoneZ2upLWUSd_JBroLsEKlbrZfjjritCRd-AuAdgx0iCZGNXLtJ4lSVZQ06USHqTa1G6V5Xf4hX1WOtK_ElRnkDRDUXNxoHXzgeW1X5MBFBd5O7kN23hgQNHFSr9uEv90ERhnL-bI-AXtkDHryF7Eq7sIoN3JnAPbem6_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=U0SQg6Fy6-fv6T6Phkj2R87V6x9MTaI7f6JrIiPB2KMJLsMxLZl3s-TDSmnhJgfWAyl96-0CPoiSfTrJxACj_ph6cLSUbQRj-My3qBtsetcD1Yii_t41E710pF5eF5FzoHnCc6bjcAUXVQuyQtshpCr2GSqD-XKiHVblpv6dwikIvwRoneZ2upLWUSd_JBroLsEKlbrZfjjritCRd-AuAdgx0iCZGNXLtJ4lSVZQ06USHqTa1G6V5Xf4hX1WOtK_ElRnkDRDUXNxoHXzgeW1X5MBFBd5O7kN23hgQNHFSr9uEv90ERhnL-bI-AXtkDHryF7Eq7sIoN3JnAPbem6_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: رسول خدا و همراهانش در جنگ لت و پار شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/news_hut/66067" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66064">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=nVtNhlJateqBmbPj7dPxDiCL2Htao0HVB7vEPRZtfCARnnCZsYANPabYhzSo4AoziEvYs91NwZlIJaNr7oL9A_xMrgTTOj8Yc2VFL_4-TDvBQpeSSN8oz5Ce-5hr5r7InBwTtEwxHFiukOEUvPQJAOBPpi8IJdgq68gSjf7JfStsc-KhOHB4TrzSqyElwQI_pxObQySYrf3h3YJpOqGqN2oHCZRkuoQpwTNaZq3Qo46eshVemTCUJ2o1gIHpiz-z_Hj5uItiQynVMyT_fZUNDj9GeVB8w_7P07kZkmwF4yifYGXbbIzJgzkWD4WAaVWE9zoRRxJEnRMbbEysEeTy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=nVtNhlJateqBmbPj7dPxDiCL2Htao0HVB7vEPRZtfCARnnCZsYANPabYhzSo4AoziEvYs91NwZlIJaNr7oL9A_xMrgTTOj8Yc2VFL_4-TDvBQpeSSN8oz5Ce-5hr5r7InBwTtEwxHFiukOEUvPQJAOBPpi8IJdgq68gSjf7JfStsc-KhOHB4TrzSqyElwQI_pxObQySYrf3h3YJpOqGqN2oHCZRkuoQpwTNaZq3Qo46eshVemTCUJ2o1gIHpiz-z_Hj5uItiQynVMyT_fZUNDj9GeVB8w_7P07kZkmwF4yifYGXbbIzJgzkWD4WAaVWE9zoRRxJEnRMbbEysEeTy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که ارتش اسرائیل از حمله به ساختمان حزب‌الله در ضاحیه بیروت منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/66064" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66063">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
کانال 12 اسرائیل به نقل از یک مقام امنیتی:
این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد.
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66063" target="_blank">📅 14:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66062">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
کانال ۱۲ اسرائیل:
هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/66062" target="_blank">📅 14:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66061">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دیشب تو بازی قطر سوئیس، یکی از هواداران(خانوم) شرتشو در اورده بود انداخته بود وسط زمین
⚽️
@fotbal_xc</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/66061" target="_blank">📅 14:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66060">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=UQHk3uNCUvUgRvDOWxHvyFmnakkJ9lXHWQkHtfRFQYjNMrZmqgRy2rRXtkvMheJTTMO4BQ9yxOG3oJ_sANwNqPFqbuvccxNyhZt-91EhtSbMp1mgerzYiU2vtZvwItF1c2vkvwJXA08L5E2bEnJw3CsjOOCoOSZQ7NHHa-7d-mbcvuRlb38kPoJRjLlWn8sNHes5n_CyjFOGMrNFRruzqolCIfvn6Bv9BdES_ZKyDdwfAoIjgXbweorZRgRIvXP7tGGhDBo6JtVVWEd_Ub_uckUvvN7LSaQrTw07T-A0VJMP3HzNrYu2X74F4jYQQgaKUNqt7krfE3dHzJdU9q6zkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=UQHk3uNCUvUgRvDOWxHvyFmnakkJ9lXHWQkHtfRFQYjNMrZmqgRy2rRXtkvMheJTTMO4BQ9yxOG3oJ_sANwNqPFqbuvccxNyhZt-91EhtSbMp1mgerzYiU2vtZvwItF1c2vkvwJXA08L5E2bEnJw3CsjOOCoOSZQ7NHHa-7d-mbcvuRlb38kPoJRjLlWn8sNHes5n_CyjFOGMrNFRruzqolCIfvn6Bv9BdES_ZKyDdwfAoIjgXbweorZRgRIvXP7tGGhDBo6JtVVWEd_Ub_uckUvvN7LSaQrTw07T-A0VJMP3HzNrYu2X74F4jYQQgaKUNqt7krfE3dHzJdU9q6zkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چندساعت قبل، اصابت پهباد حزب‌الله به منطقه ای در شمال اسرائیل.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/66060" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66059">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/66059" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66058">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=jL0BwH4Ddwim3R9DTk2re9reBe0EyvSLJsBB7dLcgSsYD3szu8xmjQFa5prfIKmGxFLdXJwYU80xQPVRDfQpfUyFLGTOPyjfhDOGeGh7oa0L27k1e8_QN9nWWxbFT1GxBqo_TBPv6fY2AvTQdTZ_FcQ41daU7VnIWodtZzEzlk576vcALjgFVOuVoH1M0xMd0rFYr6rlyv7h2rDFZP_mY59ioFyaHk5PJi3ysgrdr8tOpSY7argLQwM60CoG7obieQGfF5-3A9rVBsPlWXyR1CFxdj-EiNZmnL0r_flbAvw-hTIrygGB72fKFX-_19wWI1Ko8jQfbq_cnfyBCeeaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=jL0BwH4Ddwim3R9DTk2re9reBe0EyvSLJsBB7dLcgSsYD3szu8xmjQFa5prfIKmGxFLdXJwYU80xQPVRDfQpfUyFLGTOPyjfhDOGeGh7oa0L27k1e8_QN9nWWxbFT1GxBqo_TBPv6fY2AvTQdTZ_FcQ41daU7VnIWodtZzEzlk576vcALjgFVOuVoH1M0xMd0rFYr6rlyv7h2rDFZP_mY59ioFyaHk5PJi3ysgrdr8tOpSY7argLQwM60CoG7obieQGfF5-3A9rVBsPlWXyR1CFxdj-EiNZmnL0r_flbAvw-hTIrygGB72fKFX-_19wWI1Ko8jQfbq_cnfyBCeeaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66058" target="_blank">📅 14:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66057">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل:
حزب‌الله با نقض آتش‌بس، سه موشک به سمت شهرهای شمالی اسرائیل شلیک کرد و ما در پاسخ به بیروت حمله کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/66057" target="_blank">📅 14:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66056">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByvB7J-leWaci0SuRs49SrrYIqH627pZjuixEuLY_-KTduQFOzscwSQZlmsUXgtGpKnrvO6a9Xw0FFRoYvxPk2WwWcUBMF0Z8zwIs44Z94r4YtLqYdltVcbHrJb3V4jVajqmjQKJSniWeP2uN9Llx_tmfUWc7hDgDkbVbqK2lPLlkazMk9HxjLGq0-m82K3zVCNp48dBDWxEyN2b2ej9IKLn4MJUUqxTAExgpBXj2Vs89i_cC2DWOdL68AUnC79XOPWeYCUtkhv_0Qb3bdQotjQUGYCLdMwKgThUchfu69w90pc7jtA7d6j9rlOIRZKIq9ZmcRvfEQc0zG_v1J-_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه نتانیاهو و کاتس:
ارتش اسرائیل اهدافی متعلق به سازمان تروریستی حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66056" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66054">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3UGAzIxB5VH57Ca91n2LMOen03ZxRhAfgt4TtrIdD8bHOMudYEsHp94789XHQ9jNoFCkOyR7xIkLjU8Wy5L8FPgo30JZadD70emoVmFdUyjiyplK0sfKD65KKBQyGIoU_EZ_oUQ-vCDZVfQRR42h_0TPDB_sZQmQr9jOQEjHd7RoSay0b1OpDLXIdnBGYzDR_7ZmNe8vTPl4TbNLVXg9cHlZ7q414HUSh06e902doOleXf_m7fYWJQUsBi4vnffdjmXk033TrDjui_Xda_hl4MhhJW998lPVC64M2qm64_Novt-NY-BK_ahu8hIRtiSz_CixPKA4HysF9ZtaDcUDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها ازحملات اسرائیل به ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66054" target="_blank">📅 14:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=g9Xgy10Jt85Yb-_tCOYcuRw7Doqm3Flf_PHdqG3JSe9QsMb6B7DkrXT7NzzqGKd0kVaRowG-pB3A9pLqo2l0CLuW0C8vjZ8fRXQ2uvZcqG4oJGLculJut34Z0HnTwr9cJv_pO86qSAw5e4CDUjFOxPMyoT79hkt1V5P4hkZTmscPzZqs02laxflTHmefnYKbfB6iHk2TmSi16F6Nx_t2F-f35vMVQyZ-CaILzGOG5pXEnmYis3kk8ItNx9R7Vb9HdDtEu4BoTMRf-JWPJOJWzZQJ-5anSHaWJmH7SLFVKlRBE0o_u_AMpds8xty2qwlFXrxQIGeRfnbOr12NFUUGnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=g9Xgy10Jt85Yb-_tCOYcuRw7Doqm3Flf_PHdqG3JSe9QsMb6B7DkrXT7NzzqGKd0kVaRowG-pB3A9pLqo2l0CLuW0C8vjZ8fRXQ2uvZcqG4oJGLculJut34Z0HnTwr9cJv_pO86qSAw5e4CDUjFOxPMyoT79hkt1V5P4hkZTmscPzZqs02laxflTHmefnYKbfB6iHk2TmSi16F6Nx_t2F-f35vMVQyZ-CaILzGOG5pXEnmYis3kk8ItNx9R7Vb9HdDtEu4BoTMRf-JWPJOJWzZQJ-5anSHaWJmH7SLFVKlRBE0o_u_AMpds8xty2qwlFXrxQIGeRfnbOr12NFUUGnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
تصاویری ترسناک از لحظه بمباران یک نمایندگی خودرو در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66053" target="_blank">📅 13:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=U-El8PetEGQvAWlfh3iopUTKWjEujDC8WNcDHgHmiBAOvrdLi5-bHLZxtv7oP3VK72yE_2Mm2f_zxsc004Hu15lL6ZgWdKZuN0lQtTOC2jsEW8O_UUDLPfz5HFA07S59oWN4fVEYYIkwveiEZ-IRzqGT8Lmlf6nUS8BI7AyG4K6qy9GIhhisssC1dRAOt3kbkoWVN8S0S6dr5hvLhDy_kwEHgIdxd5CSxAzYimkso2FaKlsOoqUxcExXep5onWMn6yEIsdjyzW2-NYz32BwGKI79sVqvqKv321L7OvWhyMqzA4Ag1yK0PYw4rk7GHBAep_CM0Y4L-Y9g7DYRtJ_DHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=U-El8PetEGQvAWlfh3iopUTKWjEujDC8WNcDHgHmiBAOvrdLi5-bHLZxtv7oP3VK72yE_2Mm2f_zxsc004Hu15lL6ZgWdKZuN0lQtTOC2jsEW8O_UUDLPfz5HFA07S59oWN4fVEYYIkwveiEZ-IRzqGT8Lmlf6nUS8BI7AyG4K6qy9GIhhisssC1dRAOt3kbkoWVN8S0S6dr5hvLhDy_kwEHgIdxd5CSxAzYimkso2FaKlsOoqUxcExXep5onWMn6yEIsdjyzW2-NYz32BwGKI79sVqvqKv321L7OvWhyMqzA4Ag1yK0PYw4rk7GHBAep_CM0Y4L-Y9g7DYRtJ_DHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو برزیل یه دختر 21 ساله رفته بانجی جامپینگ یادشون رفته براش طناب ببندن و انداختنش دختره هم فوت شده
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66052" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66051" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66051" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYyo34rU4AcuRhcaJP3utppgrrgznqiPhbPziQ5s5SG5BDs1Me1gWR5krvYVh30Ork_MmU5w32KjqyyEo0Y3q-F7oBFZv_B-WjBGJJTTWmk6mXJghkQaHcXUMDCTgPofhp_MBjbF-j2U7mL6SIThFwIX-2VUxxmmnB2_vkqATIv6oBocLQUinTuPgThDqyhDgnLobroV6P5TiU6tLKlQc2qPVJWOjGGF0GqtCRZQQJnGYHvb0ficHwMs3hwSkgGt8uwUnWgQoW6srJhN5lUXvSPxwm_O0iany8SMhFDX2CB_N1sBmePt19USGy_3EwtHWhcm-XHf9v5d5JylNfoUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66050" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66049">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db36249809.mp4?token=M9JVHgCQ7j5NX20jwY8V-oOhBFNYf2sZhZeEgiW8CAMfDtgn-3GiiQPaCWaakF2jKj95vLtKsnDPtbi6z0W_Z1OnP9O2EpXBfX3-BmtdpxuL4Uy_liHVp9x9mTFAQ2MFYU1HFTs3Bjzol2kjYeIb0Gpm02oWqmzV32vSurMOTewKw9S2eBLtEN6Fs__IJJplJ_xSVLc0jjtaP65sIbdAw6BRRISuq6mGvlJS1lHAVqy44fS1J6xmaWClipyxHcTZnAwOC6OdwKsxFTsC0DRxFm4faiqaUhVTHkmQUx8t-3cPV0KuJtXc6GqEXsHsX8oiXDiOyx1YhWoJveiiwdHtjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db36249809.mp4?token=M9JVHgCQ7j5NX20jwY8V-oOhBFNYf2sZhZeEgiW8CAMfDtgn-3GiiQPaCWaakF2jKj95vLtKsnDPtbi6z0W_Z1OnP9O2EpXBfX3-BmtdpxuL4Uy_liHVp9x9mTFAQ2MFYU1HFTs3Bjzol2kjYeIb0Gpm02oWqmzV32vSurMOTewKw9S2eBLtEN6Fs__IJJplJ_xSVLc0jjtaP65sIbdAw6BRRISuq6mGvlJS1lHAVqy44fS1J6xmaWClipyxHcTZnAwOC6OdwKsxFTsC0DRxFm4faiqaUhVTHkmQUx8t-3cPV0KuJtXc6GqEXsHsX8oiXDiOyx1YhWoJveiiwdHtjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۱۵ سال پیش زنده‌یاد مانوک خدابخشیان جنگ میان جمهوری اسلامی و آمریکا رو اینجوری پیش بینی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66049" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66048">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
امتحانات نهایی پایه‌های یازدهم و دوازدهم به دلیل مراسم تشییع علی خامنه ای، یک هفته به تعویق افتاد.
پایه یازدهم: شروع از ۲۰ تیر ۱۴۰۵
پایه دوازدهم: شروع از ۲۱ تیر ۱۴۰۵
جدول زمان‌بندی دقیق به‌زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66048" target="_blank">📅 12:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66047">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28745391f.mp4?token=YwxXNRiKPzqKhmiT6JOT2PmKK3yPyZOXsRoMpI7mW4j7mWgqOg41TVtUog1IGykAfRq77THMiBaEq2_sbx4PyAgJe6fDbN6PBFfNj721nRYvvoY4Oa3utC972Z98RvI8FdTveRJ1OnzHiTTrwSZfT3I1lYnNxShuS1RCs3v4sH82yaVI7F6g1SPHtbNNAXN3onKEgaqyYsHlhyEm4R11IjPkotcsXnScpoCV5r76nVyJckUx07YbuNQst2-bnAVclzDvLiAJgJf7l8Wyw2HOz9nZUy_4A82P_dsCCorTTXZwdsqAnGvtjI5ASh19ErT4eTy-sr1IRNeu_1ABqt725Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28745391f.mp4?token=YwxXNRiKPzqKhmiT6JOT2PmKK3yPyZOXsRoMpI7mW4j7mWgqOg41TVtUog1IGykAfRq77THMiBaEq2_sbx4PyAgJe6fDbN6PBFfNj721nRYvvoY4Oa3utC972Z98RvI8FdTveRJ1OnzHiTTrwSZfT3I1lYnNxShuS1RCs3v4sH82yaVI7F6g1SPHtbNNAXN3onKEgaqyYsHlhyEm4R11IjPkotcsXnScpoCV5r76nVyJckUx07YbuNQst2-bnAVclzDvLiAJgJf7l8Wyw2HOz9nZUy_4A82P_dsCCorTTXZwdsqAnGvtjI5ASh19ErT4eTy-sr1IRNeu_1ABqt725Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
صحبت‌های حمید رسایی علیه مذاکرات نمایندگان جمهوری اسلامی با آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66047" target="_blank">📅 11:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66046">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
ثابتی دیشب تو تجمعات بسیجیا: عراقچی خائنه و من طرح استیضاح رو به مجلس ارائه میدم
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66046" target="_blank">📅 11:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66045">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeNp1UCi-EiqDfG6LhxyBt4gTC4JJkR9y6izCoNeEm-lCwHDBuKu1FyCa4YLS7hqyz8FXie8oxdOUUmc_ymiiyjl5Pvw3G2jlP8Q6BrAWX4SBxjEYA8ytSR4RIPUlZITWe1qlcz9qnnneP0krsNDvN4S0YECyDATwd3S5E9BVLEWqn4wfvHJHV7hC9weX41l-oNZx9OTbNSFKFchHIy6RRzcrrXhOT6czyJnc8dcueKHHKAWmjWtxgo5zQyLwikAP2LZ9qBjE6kXlKeLnWaavw16IqEn_8e_csqeAJXKvyK6GvFXNyQz0hPxo2enBWViSDJ_HBp5lEjsqKju3kGILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی والا مام خوبیم
بابامو کشتن
زنمو کشتن
بچمو کشتن
«ولی رفتم باهاشون توافق کردم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66045" target="_blank">📅 10:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375671acc0.mp4?token=AGLFWNGNgcZRx1Z27TwiV9J7Z_Ls74TOUxy3dsfK2Dh_DwMVzZRyyOI-zQDC6QXnQqK3fvcqz39HuEeSSwr3c2qGwdttE1-htmnN6AjpPvBD83AX-Xwgq0HyFaMhw9zuSBWgStvXVufg2jwmbSZNQzM8jikwlyD-EamaMbELh92ysYrbl9WadbzSMV7zG2O7cA-9UBxYnuaz61QJopGuUMWBvcDUZ371X_-q2XwXIg2-K1Hl7mJlB3jYeVUuF1aRbV7syDEiK9Q-FZv2TtxnhWeTARAWLtPWY4fUu8yewaY7dvbgkkvCU7vCwWCn_hk0xuB0_39cCngGQCqlWW2lPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375671acc0.mp4?token=AGLFWNGNgcZRx1Z27TwiV9J7Z_Ls74TOUxy3dsfK2Dh_DwMVzZRyyOI-zQDC6QXnQqK3fvcqz39HuEeSSwr3c2qGwdttE1-htmnN6AjpPvBD83AX-Xwgq0HyFaMhw9zuSBWgStvXVufg2jwmbSZNQzM8jikwlyD-EamaMbELh92ysYrbl9WadbzSMV7zG2O7cA-9UBxYnuaz61QJopGuUMWBvcDUZ371X_-q2XwXIg2-K1Hl7mJlB3jYeVUuF1aRbV7syDEiK9Q-FZv2TtxnhWeTARAWLtPWY4fUu8yewaY7dvbgkkvCU7vCwWCn_hk0xuB0_39cCngGQCqlWW2lPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ١ دقیقه رو گوش بدید
زنده یاد مانوک خدابخشیان میگه :
رژیم اگر توافق رو بپذیره به جاکشی می افته !
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66044" target="_blank">📅 10:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3ukPOx_zi_9TS0RTeh9RYoKYaZpua9UkAjxC-XNAmgbeo29bAisfZoaO5KTQEoQ89tWruvv27t4g_I1oQ5_f5evAh8e0ZeRw9VFu5RuIWcM8NVcgKBfb6K3wMcujqhX4C7A4YNwGbAoMAco3Lzo69poHQzFCEQnbc1cbB8d-w6cDQwFO6Sy2gzPkWQnzBPEUUgqOQKHMrSgKKCt4sOGHn18g59FojbQ7EpmRZE_XfE689LGdZT5P6lboxdzl0D1uGZI7WpDMNX0J3FcdXD8ljOXYo9C4FPcGYm_9Fh6VFvQX8xAslggdRSISkrSy9zh5QOQYckJndmw2wpKmnfH3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط عباس میتونه جوری توافق کنه که:
جمهوری اسلامی ناراضی باشه
مخالف جمهوری اسلامی ناراضی باشه
اسرائیلی‌ها ناراضی باشن
آمریکایی‌ها ناراضی باشن
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66043" target="_blank">📅 09:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518512af42.mp4?token=VDDJpPWgwdM9dKvixMTrDCdwM19ok235SnIq60U2mQnFcJ0j3ByZEYRXrClSb2E_wTszY_tBeaQN3IvzGqHseRhCLJ8TMpfIqofDaEXqzRC0Se0qNux8-dXiv7kJdM550TXRmJ17-0syA4MI2ho3wKDqstNUbPGIKltjyZLi5yzSKc3_vYpQfimY2GXfh_soiVMhc3zAC7y1U1pyM_tuCRzfQDKxwrWaqgxTZ5Z24vR936fDGYx4shBYVL6YvpvCarMePLJqsMFyWMfnG1YaVmE815qAT_k-BjXcMypJMs6i54vx9cDpCgNIuVgThFVbnpkpj_OJlWnL6anutoiQsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518512af42.mp4?token=VDDJpPWgwdM9dKvixMTrDCdwM19ok235SnIq60U2mQnFcJ0j3ByZEYRXrClSb2E_wTszY_tBeaQN3IvzGqHseRhCLJ8TMpfIqofDaEXqzRC0Se0qNux8-dXiv7kJdM550TXRmJ17-0syA4MI2ho3wKDqstNUbPGIKltjyZLi5yzSKc3_vYpQfimY2GXfh_soiVMhc3zAC7y1U1pyM_tuCRzfQDKxwrWaqgxTZ5Z24vR936fDGYx4shBYVL6YvpvCarMePLJqsMFyWMfnG1YaVmE815qAT_k-BjXcMypJMs6i54vx9cDpCgNIuVgThFVbnpkpj_OJlWnL6anutoiQsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه آخوند آوردن صداوسیما داره میگه به پیر به پیغمبر اماما همشون با دشمناشون صلح کردن شما هم شل کنید دیگه.
«
واقعا بی شرف تر از آخوند هیچ جای دنیا پیدا نمیشه»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66042" target="_blank">📅 09:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66041">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66041" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UuEQlWNq-SXNBecLCO6GBTS2ZPNtuHdo4l1B8PoJf_MuWvxtBYxBsYySBrnv2uVJkRyJihAfkTziUuupCidzf-6fAoJ0aS20dWgoZC9CR6C0zJkFu4FIvnxowUImwOSqw2bPNyjtPA9GJYzdrdoMMa6TE5_3_s9kI2Gxswfys7iUy0E-vsZkeJqpE1q1c8sZ-v2MFo5mmO_ZJI4R1d5zv2nOpZ_Xdtkzwda4v4G7-yu4MPRBE8-UUzAdB8tE55NyPLZR0G8QlDoXMTv1NFwxY-85ygzw9quvLdHpfLOYG_HEiCvj7mW-NGIgBK0W7QA6t2x9PL774ZKmVbDyxwEtDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66040" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPTTbh8ZUiayVw3I6T8TVTLNH44pqR2C_PHVesKDGkJpOzwQCQuiwA2jSy98Ozzylz4DWqHlJhoNxsblP_Fsn810qLurZWMNSBPEunFop7VtrLkBaojvm2zS5C1uhoF_k-qQQ9rjiyN-7dJ9HkHSUD2-7NU7TXHUuFHvv_xTss3TYXaSGGMfLnZaBnX6F9FVVKLNB-1OJ0l8o0PUlvFcmjuCOnKjqgDnu65EcFWDT364p2OqDgfsUmsr8fO3KuGU3sYeGP1j9uUGtRJCUcuLocWLUSBY1h52tHIBJGiJFxMoeVoUHfeBmQaaT-J1N6Sm51L6JERBTAtq_mFgJwihfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66039" target="_blank">📅 01:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=UKynp_fqx8FsXAUz5h0568nJ5k3Z9vdpjYfxyOaMgA5yC0fmimIYWNXJ0xfYTLyCl8s1Wqr0y28VBY39Dn_ovVb3US8BPlaoDlWLScLlvOT1loplq0khOxwbEmdmSbMC64Bgh-k4wmekzp5yqfZGMkPsnif9HAMFRt_uMSH9RF1zMCG3Y6Uv1ZCaSpu9YXIi9AjLHXkwMkj01jsj9TzX9342SUv8kKNfQB58mL2APvGVzm_bW_-d9qcYfYAHYU9QV7D9Lh2KRSfOV6V4IaHr8PVRw-DFXvHLUvZ4bIG1GY6wKzBIjLpYncDyv9HgpG2GniLt7Laqbz4celzlYtrvzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=UKynp_fqx8FsXAUz5h0568nJ5k3Z9vdpjYfxyOaMgA5yC0fmimIYWNXJ0xfYTLyCl8s1Wqr0y28VBY39Dn_ovVb3US8BPlaoDlWLScLlvOT1loplq0khOxwbEmdmSbMC64Bgh-k4wmekzp5yqfZGMkPsnif9HAMFRt_uMSH9RF1zMCG3Y6Uv1ZCaSpu9YXIi9AjLHXkwMkj01jsj9TzX9342SUv8kKNfQB58mL2APvGVzm_bW_-d9qcYfYAHYU9QV7D9Lh2KRSfOV6V4IaHr8PVRw-DFXvHLUvZ4bIG1GY6wKzBIjLpYncDyv9HgpG2GniLt7Laqbz4celzlYtrvzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
شعارهای معترضین به مذاکرات با آمریکا
اگر چیزی امضا شه، مسعود باید کشته شه
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66038" target="_blank">📅 00:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66037">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
⭕️
شعارهایی که در تجمعات امشب حامیان حکومت سر داده شد:
۱_ تا باقر کفن نشود، این وطن وطن نشود.
۲_ مرگ بر سه لاشی، قالی مسعود عراقچی.
۳_ این توافق خونیه، باقر خودش کونیه.
۴_ خایه بخور با سینی، عباس بچه قینی.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66037" target="_blank">📅 00:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66036">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9VL81V7YCsYSzLkq_q9hPhaH2DL7gz1xgO4wI8QxVgXzEXOYS_QRGAg9xztD8QqYsRwNaHmMsRupWdmpKjrHsOSwK-XbEmgVwSPl4oDwUOYyD3vV0QXtuyoFomSzDrqkI-dIFyRmdiJ_gT8o9Myp7M7ntjo_4KCX1l5xdcvlAvnNZSzIcz2KWaqqJNwdVsafnVf9kCj3dFKaADYhbDVnF5McP9IQe8ryUUzQgPS_CzreLZFUeZBuhjsRcCth4t388mK7t3u4pkwI6DdcBJE6D7kvYNvcRuM98u0q9ZgtmKcH2HR0AGpc3FXHtqBrZbLK1r3t1Mcn_DpJN3bIM_COw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ و پیت هگست در موکب هیئت محبان امام صادق (ع) کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66036" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66035">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQLLHhZUQlPtI0cgMlfJPGx33FKi1b9LYZ9Ao36kYVsVQlpMAqqNx_51DvmbFu4N4qC0IHPlSdAunV0VbKlHtp3eU7DsztRYlXexx6_Fz92ky2nUq8lgOpw9-YqNe9qFPR-fkdbcNuhmM1l0H_wkWd4rkmEVdUFowjraBbVLdR2LOJwNZuTuVJOEohnkBYO9r2F9D3r4FaFsWVdeITgkBcq1emsUvbUvmLwemOq4uDaUv4mNW-PX1k1fWYYZKnyLfN-Opn62LJbmNxoWiuPqgbMSoEAivGQzif3jrqpgaZ7abkfrFtE5BqT8LS6YGxQB5VDR4STzOJ9tT9wCFDIA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
توهین و کنایه بسیجی‌ها به آقا مژتبی
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/66035" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66034">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
نبویان :
امریکا اومده به اینا گفته 300 میلیارد دلار بودجه بازسازی مملکت رو از عربستان و امارات میگیریم تامین میکنیم که خب مشخصه نمیده
اگه آمریکا بعداً بگه ما از عربستان خواستیم پول بده ولی نداد، شما می‌خواید چیکار کنید؟
«وقتی توی متن نوشته شده هزینه‌ها باید با توافق دو طرف انجام بشه، یعنی آمریکا هم باید درباره محل خرج شدن پول نظر بده. حالا اگه آمریکا بگه این پول نباید فلان جا خرج بشه چون ممکنه به دست سپاه برسه، اون وقت می‌خواید چیکار کنید؟
من بهتون قول میدم نه پولی واقعاً وارد کشور میشه و نه اختیار کامل دارید که خودتون تصمیم بگیرید این پول‌ها کجا خرج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66034" target="_blank">📅 23:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66033">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCzz7r_whU4ujb28RiltULvDw-vMOKS6GsSt7OMo0MA6QHXUXp-co5aASNtwGJBK8HL6-1eJnsY93_G0Px8TB-dfgxI62DvFhmtgG-WojQYrVCXnX3YI39B10-EwG4dfxIivSdZLEQ1S_83UVr3Ty7ZhynYOA4rKhDZW9fXEM-yuM2wxSITc3ICbPXJyUuefuc3OzL1EJG2KzJdv-J4Vy8YaTR4YQ2ivTktkqRz199YWKd-JsWnKwtXUqTz_kVBFtjpRFf69QMsz9s_POrRbtWNZaIreDW_0UbO9I8ZQ53kBllkhEoKOMPAxfKsa1a7dMneOZ6MC3I80tM4gTA8IJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز دفنت نکردن فردا هم قراره با قاتلانت توافق نامه رو امضا کنن
😂
...
«چقد تو مظلومی»
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/66033" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66032">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:  طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است. نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66032" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66031">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077634d539.mp4?token=VnpMfGqSiaPMQvu12-tfrUhaS2fv6fakxNlp2aWDVN8HhoPzSlZm93zGaHAtW0PqHC-aXzD7xT4sJX8hJd3HIi04bkJtRj912phwUbZACCcim_NX3Sx8hWMRiL_M8ubJuRqCQ9tH49ZJm6ZJGFii-SDin4_zAbv3ey6jUnI8dlWq2PwhpeDG4NXyTntQAKQMRCCPRaCcINVlBzmZNw0vpOMFLs3SMa56GJHY60HQR77NUvbVhWOCN0z5FLHAr7gd01FLyVwJdDPdaFRV1OgA4MMDe7wlOtw4_NucFrSQlycoJm7yGQblOSkNHyrV9Cwly8dP4_uHLWvgFr17w7TJcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077634d539.mp4?token=VnpMfGqSiaPMQvu12-tfrUhaS2fv6fakxNlp2aWDVN8HhoPzSlZm93zGaHAtW0PqHC-aXzD7xT4sJX8hJd3HIi04bkJtRj912phwUbZACCcim_NX3Sx8hWMRiL_M8ubJuRqCQ9tH49ZJm6ZJGFii-SDin4_zAbv3ey6jUnI8dlWq2PwhpeDG4NXyTntQAKQMRCCPRaCcINVlBzmZNw0vpOMFLs3SMa56GJHY60HQR77NUvbVhWOCN0z5FLHAr7gd01FLyVwJdDPdaFRV1OgA4MMDe7wlOtw4_NucFrSQlycoJm7yGQblOSkNHyrV9Cwly8dP4_uHLWvgFr17w7TJcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرفداران رژیم دارن شعار مرگ بر سازشگر رو سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66031" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66030">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9383ea7d9.mp4?token=QdOjKngEYuOIUUeM_fspHg03G3RF2KicYvbh9ZUnzcs5WiILwTCztPyHgKaxb36fgH_WYqZygUrbBmlpBSt9VTs9CnhPHhi0XBhy3WYYE6YFI5kg7jmaqYh6bonXVrbwIU2g09w2jLISpjamo-hgYgOc_TLC_-ke7eXsYr515INX_flz14eSgiusJ5WfPTCI12RJ-8CTS9t1Pi5UykEUqvSmshO7d0QL1xIV4gpjN5lBojKBcPl37_tOAkmysY-iJ9FVbFvcZayQANMag9Kfg4CWBrKFfi8qJRXdwGigZgrSXTyebwV_2ZzvbPKubopg9KVOPVNJj2pNHMHu2MHS-5ECt_XawhjQ7DwCwdJ5heR3MBoWyxH87L32SU7DNkKtTsgTxGsfj3erGQN4BQwKbDm1dwzitkoxpLxysm9gQXrSIWUFjQwjRu58vk6WJVc-rBRsrancCuNazYlBkAb-6yll70ivRDl-kr2q0ffnQhCC6I_xWIQVuzhj-NMdE-fvUwabx-P9_hdByI6AtsFozOJhlPVqbiRYPZcJldPlC1p-oyCflUfDrBOM2AnoF7DVXTNr-tBBp0E9lvgI5F395GzKVe4rvFuIcXkCTvrkK9mWxWx5jYUXd9zpiNjwxfDS-QhCjwbnIEuQ89NtEyD6o0cm4Ixgpgh39UxndzwFaAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9383ea7d9.mp4?token=QdOjKngEYuOIUUeM_fspHg03G3RF2KicYvbh9ZUnzcs5WiILwTCztPyHgKaxb36fgH_WYqZygUrbBmlpBSt9VTs9CnhPHhi0XBhy3WYYE6YFI5kg7jmaqYh6bonXVrbwIU2g09w2jLISpjamo-hgYgOc_TLC_-ke7eXsYr515INX_flz14eSgiusJ5WfPTCI12RJ-8CTS9t1Pi5UykEUqvSmshO7d0QL1xIV4gpjN5lBojKBcPl37_tOAkmysY-iJ9FVbFvcZayQANMag9Kfg4CWBrKFfi8qJRXdwGigZgrSXTyebwV_2ZzvbPKubopg9KVOPVNJj2pNHMHu2MHS-5ECt_XawhjQ7DwCwdJ5heR3MBoWyxH87L32SU7DNkKtTsgTxGsfj3erGQN4BQwKbDm1dwzitkoxpLxysm9gQXrSIWUFjQwjRu58vk6WJVc-rBRsrancCuNazYlBkAb-6yll70ivRDl-kr2q0ffnQhCC6I_xWIQVuzhj-NMdE-fvUwabx-P9_hdByI6AtsFozOJhlPVqbiRYPZcJldPlC1p-oyCflUfDrBOM2AnoF7DVXTNr-tBBp0E9lvgI5F395GzKVe4rvFuIcXkCTvrkK9mWxWx5jYUXd9zpiNjwxfDS-QhCjwbnIEuQ89NtEyD6o0cm4Ixgpgh39UxndzwFaAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
نبویان: من خیلی ناراحتم این چیزی نبود که آقا گفت. پیش‌نویس توافق بازتاب خواسته‌های آمریکا است
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66030" target="_blank">📅 22:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66029">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=caDyXPZ1WD2Flc6Q_GxFXENq5M1Xn5_swK1CZjTLvyeK2J5okBdVDP6JCNWuCTmo9sIiNLUCY3e3bzMOjpech42j23n_Df02YrA_9kk4Cm8_1T3vue0m0G6uUGnPCY5lRpkzjgyZCsGEQoPbApjRmlyIHZ_x-oNkLYO9qC_5s4PsU9NnoIQrTDxXi30ea_EKTS7zoOW7GZqMf8pFiJSo_ffyjo7M6iM9EiVzo-S2XKSEhvm2GjvDzsIawC4zzEZlm_ZueOwws68XTzRlT1ACnRISyh114PvGIcUYWL8NcgheEUaJlphGkqHQHvmiN1GvBR6fm9yK1FGqrYxLmRa3MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=caDyXPZ1WD2Flc6Q_GxFXENq5M1Xn5_swK1CZjTLvyeK2J5okBdVDP6JCNWuCTmo9sIiNLUCY3e3bzMOjpech42j23n_Df02YrA_9kk4Cm8_1T3vue0m0G6uUGnPCY5lRpkzjgyZCsGEQoPbApjRmlyIHZ_x-oNkLYO9qC_5s4PsU9NnoIQrTDxXi30ea_EKTS7zoOW7GZqMf8pFiJSo_ffyjo7M6iM9EiVzo-S2XKSEhvm2GjvDzsIawC4zzEZlm_ZueOwws68XTzRlT1ACnRISyh114PvGIcUYWL8NcgheEUaJlphGkqHQHvmiN1GvBR6fm9yK1FGqrYxLmRa3MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشایی تنگه‌ی هرمز که قبل جنگ باز بود الان شده‌ی آرزوی ترامپ، آدم می‌مونه چی بگه، دهن تحلیلگری که بگه آخوند تسلیم شد رو باید گِل گرفت، می‌دونیم که این تفاهمه و توافق نیست و توافق اصلی در طی دو ماه آینده مورد بحث قرار می گیره ولی همین تفاهم هم فقط و فقط به بقای جمهوری اسلامی کمک می‌کنه نه تضعیفش دقیقا به مانند برجام.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66029" target="_blank">📅 22:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66028">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkUS0Cr8khqqvRkUFTsERoFhsg-p9IqokEpeaHWOsIJFixzturu-zHou4TRz7AQva9fcl7n3oD-EBTAP5La-3TthKwGJFu0AzJzOx9b1IOyfz7M0lltBjBsc2a2tppRZsFXQuMahS6ZHLkK69Fq_3Q2pAymoIutZa6M6ZsBoCJ5JmY-rOIMXrbkOCUXVCITxZz5ez_dxCjry2vhAX3oFzpHuXAywY_PdEOxp_eXB7hGggpIVEGhMDjEzndfFW4vStOWtVCzc1MI5lmdWuUjBdqlMipt_b4fENcAbSweaojNMT9DK90sG3AXnJxq3PZ-NXovvesdXOcvdO_bGf4IejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فراخوان اعتراضی نمایندگان مجلس علیه مذاکرات و توافق
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66028" target="_blank">📅 22:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66027">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
رادان: هر فردی که در تجمعات شبانه برعلیه تصمیمات حکومت حرفی بزند یا شعاری دهد به عنوان تفرقه افکن با او برخورد خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66027" target="_blank">📅 21:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66026">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3933369d.mp4?token=jK5y-XpTC16X237f7xctb5wpWavpweItjWNJBIMaePp3ahpPssoFw9lp1t4TjoCTqxcfJBHsDEQV8QJOqIhPx4PuoQLZLSTJdoinfszeCdffo7YJ8jYNdo2dqKgyN9PDc-PYjZ7sGz0pNEIGpVoNU8RSAnvlGhckqoonWeXnY2adULxtndLRtWfd3uObGDrAe0dVfCHedJVm1mb06etnZSC-6pB9E7P_iY4KNrkgM-7Sb5XB6lT4NKPPWXTjoySK9HYqFU0k52TD7uT246m_Pyspos7tGzIfoUBQ-E0dXEjIV61hGOuI22GA6ylk3Glgn5S_OdCAhp8ghXLVnJyfHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3933369d.mp4?token=jK5y-XpTC16X237f7xctb5wpWavpweItjWNJBIMaePp3ahpPssoFw9lp1t4TjoCTqxcfJBHsDEQV8QJOqIhPx4PuoQLZLSTJdoinfszeCdffo7YJ8jYNdo2dqKgyN9PDc-PYjZ7sGz0pNEIGpVoNU8RSAnvlGhckqoonWeXnY2adULxtndLRtWfd3uObGDrAe0dVfCHedJVm1mb06etnZSC-6pB9E7P_iY4KNrkgM-7Sb5XB6lT4NKPPWXTjoySK9HYqFU0k52TD7uT246m_Pyspos7tGzIfoUBQ-E0dXEjIV61hGOuI22GA6ylk3Glgn5S_OdCAhp8ghXLVnJyfHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
در تجمعات شبانه:
عراقچی حیا کن
امریکارو رها کن
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66026" target="_blank">📅 21:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66025">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
⭕️
🚬
🚬
فرهنگستان زبان فارسی: از این به بعد بجای کلمه هدفون باید بگید گوشینه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66025" target="_blank">📅 21:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66024">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5CarCioo1BoKpA_Ar2R6T9tUM9CWZAv66OxsuzU9TAK3Qm3PdlA4nWKnuqx5J7X2ZPZNKj0Tle3HKYtRsQQ0dK4d92KugUv9XHnl1DSfwdQUBNg7TSpocr1qjKn4qn5c2pUNO6S1aeyDCvCJRV0Vd7FskHeD7C2rz2js8THMlsLm5nOHhq0bmrvvE84jcuQxxd3RFwk8B9Yh6_5PiHzMF_Kre_oyMNv8X9QXCUtmHSmW3ZsRvWGjxFKWaIxQbBYYmTTlg3rsShGfmAhfjrS2mPQ4xgB2iq-P0P54Ui9bNWaiFlr1L01mCmaceP0mDyj_ymx1wkeaZTBE088LqVttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
⚠️
سردبیر مشرق: رهبری در کدام پیام ده شرط را اعلام کردند؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66024" target="_blank">📅 21:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66021">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71f300a74.mp4?token=lQeqykUvw3OjI2Nih5uBXqTYuybPTnHi_6PMzlGQ_PvtoOC3u4Dvd2GgBBgeqiL8XRObG0_vrkN2S4lDH8mOJipQ6mJqMrppB5ZUsRFTaczQ1mZOcYN_jwx1p-V-kciZ3N110qRp3yow1aXMBz9WZJlGLz-UdSp8Ah9WwK-27Ca0BKAlfyrgjo0hwRIdSyWkEt120ZXxFcyMGie1HL_8NiQ-1xNGWzLjJZWSUTcPGivQvCtwt8ie6p9XYdBfjCOrpj0KqiSTdurjNhsv8yhM7CGcp9tjrjUjAveIQhKwj2ayjce45BtPJBWSDkU2-iGXbBIwLqNu9BdLT2T0d87l4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71f300a74.mp4?token=lQeqykUvw3OjI2Nih5uBXqTYuybPTnHi_6PMzlGQ_PvtoOC3u4Dvd2GgBBgeqiL8XRObG0_vrkN2S4lDH8mOJipQ6mJqMrppB5ZUsRFTaczQ1mZOcYN_jwx1p-V-kciZ3N110qRp3yow1aXMBz9WZJlGLz-UdSp8Ah9WwK-27Ca0BKAlfyrgjo0hwRIdSyWkEt120ZXxFcyMGie1HL_8NiQ-1xNGWzLjJZWSUTcPGivQvCtwt8ie6p9XYdBfjCOrpj0KqiSTdurjNhsv8yhM7CGcp9tjrjUjAveIQhKwj2ayjce45BtPJBWSDkU2-iGXbBIwLqNu9BdLT2T0d87l4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربا با ماشینایی که تو ایران شده هرکدوم۱۵/۱۰میلیارد و شده حسرت برا مردم از این کارا میکنن واسه سرگرمی...
💔
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66021" target="_blank">📅 21:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66020">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66020" target="_blank">📅 20:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66019">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری؛ ترامپ: فردا توافق با ایران امضا می‌شود  توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد. توافق من با ایران دقیقاً برعکس…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66019" target="_blank">📅 20:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66018">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfhJnYkqV-kDdlnOdo38YC0SfPoeds-3oXq3ODM8DdBSoaiXaZrW0dIskih5V-zVUOYWLpnt8sGd5w2zHr58dckYhusG8aT5Lzg0A_oA2RDBVbHhUA2vckHacvbA0IkTlWFdRJp9ctvcY40WUExnaCTgQl-9wQSkg83lYMcOe4dQZEkmxzMiTjNsjvkoIV1EEGBtKFgvvBQJkECmSX7kAYiKiC5ZqTVVw1YAznskby2ioB79Eo5Pu6J8hlKorlKnU0tQ6MqIAUfOhqUQOccYCt5CNUwMzp6p-PqpSQLl4IqkaN6HM2APwQpKCSEqjIdGO3OcLoeysLXFLpGtvJEOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
؛ ترامپ: فردا توافق با ایران امضا می‌شود
توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد.
توافق من با ایران دقیقاً برعکس است، دیواری برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر سلاح هسته‌ای نمی‌خواهند و نخواهند داشت، چه از طریق خرید، توسعه یا هر نوع دیگری از تدارکات. قرار است این توافق فردا امضا شود و بلافاصله پس از امضای آن، تنگه هرمز به روی همه باز خواهد بود. رابطه ما با ایران بسیار متفاوت و بهتر از روابط دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداخت اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد. در زمان مناسب، وقتی همه چیز آرام است، ما به لطف بمب‌افکن‌های زیبای B-2 و خلبانان درخشان آنها، وارد عمل می‌شویم و گرد و غبار هسته‌ای را که در اعماق کوه‌های گرانیتی قدرتمند و غرق شده دفن شده است، جمع‌آوری و نابود می‌کنیم، چه در ایران و چه در ایالات متحده.  ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای طولانی هستیم. امیدواریم که این روند به سرعت، به راحتی و به راحتی پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مورد استفاده قرار نگیرد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66018" target="_blank">📅 20:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66017">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b00aed34f.mp4?token=H3mHVzhbCj8hOp6jgDgF-8JOLfYg97uhkhfRzLg7y5kY259aU1VWlhJhxn-zrPkfMAEH-4vnCBcWI3x1yQh2x0dCiF6uZl8zzhULIElVqUTXDeFUH_qnC56sg0k5XOuty9iTa7H5SltysCALjvLFGo4H3INcy3Y2YJarCs3U2VGcgYF_3AJITHWZ9CKsjSrsTkYYbT5CQnWfticWR8EdYGzSVOda3d7kOg8FB0yaL7a9SIjCy-sbCDAFUe_SUA45VQ9x-HmRRXMR6wxnU5dH3grh-Vtp7MHS-enV22GSK6-brvRVThLdFMaXWV8jm57pv-9CTtAA5WFKPtNHjWJapQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b00aed34f.mp4?token=H3mHVzhbCj8hOp6jgDgF-8JOLfYg97uhkhfRzLg7y5kY259aU1VWlhJhxn-zrPkfMAEH-4vnCBcWI3x1yQh2x0dCiF6uZl8zzhULIElVqUTXDeFUH_qnC56sg0k5XOuty9iTa7H5SltysCALjvLFGo4H3INcy3Y2YJarCs3U2VGcgYF_3AJITHWZ9CKsjSrsTkYYbT5CQnWfticWR8EdYGzSVOda3d7kOg8FB0yaL7a9SIjCy-sbCDAFUe_SUA45VQ9x-HmRRXMR6wxnU5dH3grh-Vtp7MHS-enV22GSK6-brvRVThLdFMaXWV8jm57pv-9CTtAA5WFKPtNHjWJapQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
تجمع هواداران جمهوری اسلامی مقابل وزارت امور خارجه: مرگ بر عراقچی بیشرف نفوذی!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66017" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66014">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4e2f8eb4.mp4?token=QmS-8niDIuIMHSsQVtYc0lbD5Vpwtw2RR9ualvpcrbmpL27C6vtQC9hq9R6uuzyRZFQVKrCvlrxxnJxftW3eF0ph7IQmY8YYAwXRNz02hgE0EFBij5d56FHSt5qJx2ZndZJDpil_kuK_6VRDPR5vDZDzm95UnakIrvfKlUB_rC2qa8tMwUjFlbcnXVum0MopzWdVrSKArb_5dKEnCIPKLfZvrLxeCkGXVpM9w8RQy6qEh6wMUWxUWG9_2k7AC_RslsL04_9GdqQjAxrKL6chBIvnIhGP6GnX8vcv2MbHCGrmGxECJ76O8_Uf7YIVflQIWgkSKD1Gsf4t_RDxO61xpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4e2f8eb4.mp4?token=QmS-8niDIuIMHSsQVtYc0lbD5Vpwtw2RR9ualvpcrbmpL27C6vtQC9hq9R6uuzyRZFQVKrCvlrxxnJxftW3eF0ph7IQmY8YYAwXRNz02hgE0EFBij5d56FHSt5qJx2ZndZJDpil_kuK_6VRDPR5vDZDzm95UnakIrvfKlUB_rC2qa8tMwUjFlbcnXVum0MopzWdVrSKArb_5dKEnCIPKLfZvrLxeCkGXVpM9w8RQy6qEh6wMUWxUWG9_2k7AC_RslsL04_9GdqQjAxrKL6chBIvnIhGP6GnX8vcv2MbHCGrmGxECJ76O8_Uf7YIVflQIWgkSKD1Gsf4t_RDxO61xpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی وایرال شده از کیوماسا، گوریل باغ‌وحش ژاپن بعد از دعوا با دوس‌دخترش
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66014" target="_blank">📅 19:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66013">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7No_SZBUbfzF6XMLZibxDPohoPBa6mpfOk-IX3ySxJD14hz_l_CeTlTwM_FrfzwUj9JxAkiOSd_gr3AfGfET9KpA9lZStT0porCxc_hgdFFTDPWLqdSR-47LxIt7M_ghAj3_VLeajoonLzN0qoiDtDPvNJ6fsdAtqnqyIVaoHJtn6rifwx9oEpJdJjh28G0UcwSGwnqz709tqAnKB9Vckfz0kcR1G9Bm3W7USNmND1fyCAf1TUaOa4Y71HSHomXJMMQ4rRBws3BfS3ZsDPA1oBrXZ2p7W5yvoQs86_oWsy1Wj9vcA0tC0VYhV3QwTYti7rKk2QN5fmzSyVDso2neg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید به نقل از یک مقام آمریکایی:
پرزیدنت ترامپ روز سه‌شنبه در حاشیه اجلاس گروه هفت، دیدارهای دوجانبه جداگانه‌ای با رهبران قطر، امارات و مصر خواهد داشت. نتانیاهو در این نشست شرکت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66013" target="_blank">📅 19:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66012">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4JL5EV18G_zRHE_S-BYqL8e_1M3IgWe0x6yYidQaX9_hbDF2J6pxr14p8ntd1sUh-HS1tr7ZrD1PYXNhxg8LwBrCzLtujWBKskDOOi_ifDK5B_amY8FNCW5s6fluFl3D6VYltZyUPxZEiv1_eUW2HyblZOpD1QfuFp0sCbKFJtIMqS3y_e4_NXn4nDHBk5uWDg6xLmNAwlsN6M5Ukxl_uj-nRL3aX9HQ45j1LIxTY7dwVgCQ9AKLJKTlC128hc249824_KwPdustwaLC2PR3ybTnEESQH2Ge5dK5MdLugDEblFm-o6LXpfXN8Q_nTWa30xg5lsOhbb2u1IkgF9CIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تجمع اعتراضی مردم تبریز به دلیل توافق با قاتل خامنه ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66012" target="_blank">📅 18:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66011">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
#فوری
؛پاکستان:
توافق آمریکا و ایران فردا بصورت الکترونیکی امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66011" target="_blank">📅 18:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66010">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpslYLbFarmTJJVvmCGqdA5Y5NnplQP8X1aCfwQeYW78r5GI6_DQOYhORZPEuKN-tZWcEk2Jgfe4gI3sgd2PuuApy90Zv5XOTESoJBS80Q7Js_1bnFMLsQDh7a_7nlJOsjRhLsqKY83zXfZ49ty51JtAoIhhOvVEbM24VacZrpjF58xvUntaM0F4ZHLYyM6pys8zYTFdBTviplN-6FSmANhNO18ww6pIV584sczb2bVnP7RDD0OeNQmbQz7xULfio69TPhWK9NCOp3mMlj2XBRdxbyUQFgSNueQopPXWo-HebQyUa1arR8QVi4T5waDzWFG17sbE3_otpjwuLLyxOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ توییت شهباز شریف نخست وزیر پاکستان درباره احتمال توافق تا ۲۴ ساعت آینده را در صفحه خود بازنشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66010" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66006">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hf0ft8Duci3DfpYiQlvd3u3Qj51Y5i1uhxB-kcrOG2okPNIBSjWKKkP-5oKo5jAG5gGIxIFnLjJHYSqzfC8I1uo34HQ7oA03f1rgjgD16Set9srhsjgOMf11AufHfhdEteSBvtgEwd6th5W5JFVyoULaRwe2jCg0_RAuYTPwnSBpdklJrY4t7zJ3yPYOiNRBlZN5BqKAJHJmbNC3dYKzxvANY8Ntctg22E2hEHda2q_tFGR6Pxty8F4EUim8k7IUifu_CignmersYfDMr67CXOrRrR_h4ks2izukZhe3HhOa6cB-dwS3tJom7SUsEubuBgYV0uIzE9rQgUSUlzt98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8vlkD0ooQgI7p8iwUQ8SE-yRq-ccXlYl70vg3O1PjmBtvqHf0Yfjxg0pqyQi0So6v5Thn0-zPpvDFu_WCbSrdVMMJv7vcESxBf8ttwOz9MMqE18i8Xt7zTZ_8r9MQwdTM9CNXqVfiAT5mi_P-eciuUcPHAN98vm2o5MPR5XJvBMNQbsW65kvqWnc1xaEuWdwDI391MSkQa01DcMbvxRlJG49rHAJCb-o4_iWqtVFoSFvL2QRx7qpDimB0LS1n7BpDLbDPV4zPnF6133AdukjIDyqRdQa3r6iX8aFY-zOisyMUfPMTf-6cxudCiPOD9c2WO0t1iwgwl-J9i3C2X2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEw5dUq-CeLSLO7hSFKfWcHY7I5RqUn_SE5p2mg-9TMQZ42MqQQgDKfV2v4nSwnIgNK3HUhTBeHW6QgXSOb-dcoStEgumxQc1PtoOgPb4B-HqIXJaZB4caN4ydJr8qnxJ-85HRz607RkCwgpQkBfLP-Ti4_UqVhO7FCbGt-10vzg0OcsvmDUWKOS_0gVlpUJlBrm97t8ax6kWjiwy6RdAIAR0WhUeFiVOl-YjFmXFdXsAybiFNfVL3A6KfM_mp7Mumb-kTZdtRGFLeBI1wU9XhNhpOgXbTPQ5hEeX2kPO0IsPBrkkBlqrews2ibeIG6-npkFw0V56EYtGjV37_DyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsCBfSK0cNn3GQPjKxgzo4c57lPh1YOR7zyPBpdkVNTcjwv716nseRAoj2joUpqyj-Wx5eL3COjZ3rEAiZXuMl-8uySnvKYGknIhUIPaqDvXAIdV7cX7dOj19nQaguvG9xMta9zMwVnur5_YWDLUCSjlBB10umc18v8Brp2JJGnP9PIrNNSry5nsBX1nvQy6kv4uPrIIHHFjLmgBPFMgLSNpM2g4FO7_R_kG5o4OJQaN_9vwgSk9N6ZAMR3W_AJNqYxSlRqhSFbkGAg6jKBiMYIoPihx7VDHlsb08n2vbb6iMF-cmn-mEBvoRFKBVHVY4ZEjtoP42dG2LNv_y1DrPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جت‌های جنگنده نیروی دریایی ایالات متحده و هواپیماهای فرماندهی و کنترل آماده می‌شوند تا همزمان با عبور ناو هواپیمابر آبراهام لینکلن (CVN 72) از دریای عرب، از روی آن بلند شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66006" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66003">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwOsxWDF_8w7WvPvryZDQBc9fL4pylI4Nxq84e7e3PvS_Uw96ADrN5Tq-toroRAJvUMR0GhQLfA-tDs2dYijaWGvk1ODAuf3AP9EDLli5fqSG8rzKzMSvwfkyFl5_nY4eLP0NPpyEBV66WUj8nKBJkcNxfP7as-A0lCTAQUeziZveYHv_Ji145SqkpXZzs2F20jbWW4bPdIt2H81lYVJe6AsR1w1XkEoshEhEWvOvsodr_580Z77OgoimABF3zwiyIpbTAp-gG4M3yVTTKyTIGJCgeeRLXTjvTvW7cToxvC5SzeNtfcw3ickdpM1u2FRDPmPsDKXN0YdMRQRvj17Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی از نمایندگان مجلس به همراه قشر تندرو امشب جلوی وزارت خارجه تجمع اعتراضی برگزار میکنن و به روند مذاکرات اعتراض میکنن‌
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66003" target="_blank">📅 17:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66002">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsLpQFLqqBN1j0dLaNGheXTC3e3d5FxfpHk8EmsepNPQQDexXfbRtrNiBMBhTk9Tjuh9oruutrkjH2ZO7Hbdbl-uwUVe6zoJuz8ADHRRNc52d6JKD2W4-DPJx5irgPllYeo1mfHsQoz0foImJv2cGfqHo-c0fC_HMw8MVAZ0h1KwsJQPYjjl0MtMIQJFFv1dEZX0ixWQwOcXKCWZGYrBDoHudQnqsbK_CP8yfUVEkxXpYqWdM9p3EGOaxFiIRzY5zTpFepuiYR_fPVSm9C-pTyDFQf-DILgKRbtmEnk76K-vRfkW3C1C90yxwlyVHX4d8jb0PO7JLpZyJGofRzpU3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اواخر بهمن ماه پارسال، ترامپ مصاحبه شمخانی که گفته بود «اگه آمریکایی ها سر حرفاشون باشن میتونیم رابطه خوبی داشته باشیم» رو بازنشر کرد ولی هفته بعد کشتش ، حالا دیشب هم صحبت های عراقچی که گفته به «توافق نزدیکیم» رو بازنشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66002" target="_blank">📅 16:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66001">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=r--ttlJ7Dwi1dOAgGAX1mACKHO975GgVjX9cKZ24ocvCUGnKhmw0e3u9AxbRPtUPdsZ83D80sVje1_Bn2Xke2-qrwhrGSFdTzNwSQWcQMIayLan6s-xK5-_tW_wy2SdjCro5OT5hA9-bJLCjOkMpRGfvraNjl_zH2mA-VNFgFBntWoolH1NqcxxwNAeDWL0HpGM61P4jCgK5SNuK2u4WiOgXHjM5ChZ0GYD5NZpy918UkVmKT5DIERRuguvX0v_tHZAt0NW7HuYxacejEqvKoV1-4sv5Fsraxc5jezwihZPO-nMrKfRFJ9KV5TM2B3gkHqa0cCqSEw637bHzuVR7UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=r--ttlJ7Dwi1dOAgGAX1mACKHO975GgVjX9cKZ24ocvCUGnKhmw0e3u9AxbRPtUPdsZ83D80sVje1_Bn2Xke2-qrwhrGSFdTzNwSQWcQMIayLan6s-xK5-_tW_wy2SdjCro5OT5hA9-bJLCjOkMpRGfvraNjl_zH2mA-VNFgFBntWoolH1NqcxxwNAeDWL0HpGM61P4jCgK5SNuK2u4WiOgXHjM5ChZ0GYD5NZpy918UkVmKT5DIERRuguvX0v_tHZAt0NW7HuYxacejEqvKoV1-4sv5Fsraxc5jezwihZPO-nMrKfRFJ9KV5TM2B3gkHqa0cCqSEw637bHzuVR7UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه هدف قرار گرفتن راکت انداز Tos-1A روسی توسط پرتابه FPV اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66001" target="_blank">📅 15:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66000">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7uhnOT4-5xCErTvttb1tuGjaOZjH0ls40QHzfRGq-gsPFitQh2Goaj4gEYyXRyBL-kZCiuBCgvXYYRZbVRgyTis7bV1D8lWQSw_qjwAHfN08_fb8z7Pz6VMBQgFCX12HEHSJ_8cZpScNQHM8PDxUBZn7FMKVHMW4mnIkmJipIWHMkpqnL4Jr6DBuAQDH1_AzmAIhAf6YM2PB1RaSDbgZJjPGYt-3s66GkVXMN0TwaGK0uXyD641CCejV1LmHmxHtrxIhHBGzaFHfmb3t7VB3qaJzL3ASgQV1Bmpyh0TldiVokYkggxcsnfossprpAuYmy4nwCbfA0E4_1TfFyHYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقایقی قبل سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۶ مایل دریایی شرق عمان دریافت کرده است.
گزارش شده است که یک نفتکش توسط یک پرتابه ناشناخته در دماغه بندر مورد اصابت قرار گرفته است.
خدمه در سلامت هستند و هیچ گونه آسیب زیست‌محیطی گزارش نشده است. نفتکش در حال حرکت به سمت بندر بعدی خود است.
@News_Hut
﻿</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66000" target="_blank">📅 14:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65999">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
من مطمئنم که توافق تاریخی بین واشنگتن و تهران، پایه و اساس صلح پایدار را بنا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65999" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65998">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
مذاکرات فنی هفته آینده پس از امضای الکترونیکی توافق آمریکا و ایران برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65998" target="_blank">📅 14:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65997">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
پاکستان در حال آماده شدن برای امضای الکترونیکی توافقنامه صلح آمریکا و ایران ظرف ۲۴ ساعت است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65997" target="_blank">📅 14:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65996">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر پاکستان:
ایالات متحده و ایران بر سر چارچوبی برای یک توافق صلح که به ماه‌ها درگیری در خاورمیانه پایان می‌دهد، به توافق رسیده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65996" target="_blank">📅 14:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65995">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
؛نخست وزیر پاکستان:
ما بیش از هر زمان دیگری به توافق صلح نزدیک شده‌ایم و احتمالاً ظرف ۲۴ ساعت آینده نهایی خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65995" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65994">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شهر عجیبیه! تریسام بروبچ دهه نودی  @sammfoott</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65994" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65993">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
⭕️
مراسم خاکسپاری علی‌خامنه‌ای روز ۱۸ تیرماه در مشهد برگزار خواهد شد. از روزهای ۱۳ تا ۱۷ تیر هم مراسم‌هایی برای رهبر دوم جمهوری اسلامی در تهران و قم برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65993" target="_blank">📅 14:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65992">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
از امروز صبح خدمات الکترونیکی برخی بانک های کشور از جمله ،تجارت،ملی،صادرات و توسعه صادرات با اختلال مواجه شده است.
خبرگزاری فارس اعلام کرد برخی منابع از احتمال وقوع حمله سایبری خبر داده اند اماهنوز منابع رسمی این موضوع را تایید یا رد نکرده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65992" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65989">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J22YH_xo2uS3gknUoOK397C5-HQvaCBKrNEQqPrvatrOzpn9gOQeaiZX6B7A-u3vnMsZVfM6ialSBMAs7jO0rCIrW6afE8n9uEoMZcp58lfBixGMS0utAB3IXQKeILeM9k-6lHgpFelEgrsjSM1rJmEutj2VMN6_LFMlXkzA7HJcu_7b-1aWFDTllyuYsk4yO7AGUyEpWUGkfoC1I3MahUFrdnrVaVkmxlvRE_jeCMyYFzPwQ0QtG1KL_shlDVziNYG3ykpkmF3rBAJbpWbmqzC-PFoP-k8BrBdCVe8t2VPKwBC-dZQWxTlpRTGU8ofKFhxvLno-xncGqNtpEuUy0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جنوب لبنان؛ارتش اسرائیل پرچم این کشور رو روی تپه العویدات و کنار سازه یا حسین نصب کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65989" target="_blank">📅 13:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65988">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dig_1w86OP8QB0lZVLV5zd1Qh1GAdCYiWPCwNA3oNj-baTJ9fstg4_046rCl18ar_aV24Wn-4NpnsqeKRMfhcs6PLxGTXkezboEeuHy6sgwA8XCWp4qpHKmCH_XgNJgWaQiflgTLMOqhzEt52JiAyFqPsDqdvWLFs8Qt6PbB3n7C_pBHqOMfllTLI9gdb-FHu6Do-efOZYCeo_btQqrXJiO7eMS7UN_B6jR-pEv62EkohDgt8lyMAizk_Ve48tROh68vdL6zcSafuFAb86s1E9JmQwLoYpcAJ83eJC6kJ65vMGEQgfv3jPSjPLD9vo0mWP4gjstffML2PAVhLRkNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایران تو هفته‌های اخیر حسابی دسترسی به انبارهای اورانیوم غنی‌شده رو سخت‌تر کرده
- طبق گفته چند منبع اطلاعاتی آمریکا؛
- ایران بعضی از تونل‌ها رو عمداً ریزش داده و ورودی‌هاشون رو با مواد منفجره مین‌گذاری کرده
به گفته این منابع؛
- الان رسیدن به این انبارها نسبت به یک ماه پیش خیلی سخت‌تر، خطرناک‌تر و زمان‌برتر شده -
CNN
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65988" target="_blank">📅 12:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65987">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=r5_c4ZKmHf_cARx6z3e7KbpPE6Dk6Zcb6fVYX89toRxORbFnFWDRDOvnKwIOnJX8UwkSrTbBdWPn5LLiMFbAvqVEacTLqVEZNWBhWdooWLhZ-GPi8B947OG1IbdfPjBONMNLtmZWYkU8iiKFdk7Tl3FZP2Eluc64saOGX91BA2vrABTbByNkgpxni93pGrYQpCxuQmG1UD4jI9CTmI7nQdSndui1AKvFx6mYGyruUMwo1Dfzhpl5QfFKueBAQ6yBzDiCJbCbZQncHGYDB91FlaBVfD2QW6qNk93EMAqT_aBlK0dKs3senbTFq_EOS3tAjawW3y_THHWPEY1nhBDyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=r5_c4ZKmHf_cARx6z3e7KbpPE6Dk6Zcb6fVYX89toRxORbFnFWDRDOvnKwIOnJX8UwkSrTbBdWPn5LLiMFbAvqVEacTLqVEZNWBhWdooWLhZ-GPi8B947OG1IbdfPjBONMNLtmZWYkU8iiKFdk7Tl3FZP2Eluc64saOGX91BA2vrABTbByNkgpxni93pGrYQpCxuQmG1UD4jI9CTmI7nQdSndui1AKvFx6mYGyruUMwo1Dfzhpl5QfFKueBAQ6yBzDiCJbCbZQncHGYDB91FlaBVfD2QW6qNk93EMAqT_aBlK0dKs3senbTFq_EOS3tAjawW3y_THHWPEY1nhBDyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انفجار شدید تانکر حامل سوخت در مکزیک
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65987" target="_blank">📅 12:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65986">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEnKwAXgW6igDQa3LTgyOwavWoQq3NsyZxfp_xtRLXqHILjTS8gP9P7HPQk-6z3rxRa3_t7KaMd0IZrOUJvSEfP2lwMEbL3ZbuL2OzWd3eWpgZnlVnKPhIPB08RdNbWRAjT48KOHv41709zlutuhW1EptJpDk8UbUJeq1uRiNsNkIFaeYyBvnSG1eadGkHWvjIUZsdlTDBsctblXE4Fdb3W43Zo78nMuP9eafkrzhggUr5QHnLu6EwnsoCVh4r92umC504diR1E5p2f72b85VD1SWRnM4xj-Oyv3luPqFzKdiVxhhTMhXZ9frX6tYWwxZgO8kHLfUaLWlX58i9-0I9N8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEnKwAXgW6igDQa3LTgyOwavWoQq3NsyZxfp_xtRLXqHILjTS8gP9P7HPQk-6z3rxRa3_t7KaMd0IZrOUJvSEfP2lwMEbL3ZbuL2OzWd3eWpgZnlVnKPhIPB08RdNbWRAjT48KOHv41709zlutuhW1EptJpDk8UbUJeq1uRiNsNkIFaeYyBvnSG1eadGkHWvjIUZsdlTDBsctblXE4Fdb3W43Zo78nMuP9eafkrzhggUr5QHnLu6EwnsoCVh4r92umC504diR1E5p2f72b85VD1SWRnM4xj-Oyv3luPqFzKdiVxhhTMhXZ9frX6tYWwxZgO8kHLfUaLWlX58i9-0I9N8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
خبرگزاری فرانسه:
روز جمعه، از کشف یک جسد در صندوق‌عقب خودرویی در مجاورت محل تمرینات تیم ملی فوتبال ایران در جریان مسابقات جام جهانی ۲۰۲۶ خبر داد. بر اساس این گزارش، بازرسان و کارشناسان پزشکی قانونی مکزیک در حال بررسی جسدی هستند که در یک خودروی متوقف‌شده در پارکینگ بیرونی استادیوم «کالینته» در شهر تیخوانا پیدا شده است؛ استادیومی که به عنوان اردوی تمرینی تیم ملی فوتبال ایران در این دوره از رقابت‌ها استفاده می‌شود. این حادثه تکان‌دهنده تنها یک روز پس از افتتاحیه و آغاز رسمی مسابقات جام جهانی ۲۰۲۶ رخ داده و پلیس محلی هنوز جزئیات بیشتری درباره هویت مقتول یا انگیزه احتمالی این جنایت منتشر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65986" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65985">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=PqLwcZX5jZWz0P_QXVXAkHA4QAVLpmHybQKeBaRx9cPTF4zb1YPtFvNI5-5prpLnrvI72o_mx43G-AAYjqMiGLG_HIkCIUUttzrcjEiidzRrg7464-muGBqoBbhwWucLMMkpbngk5aelAI8_CN8iYhW6jBtAAkXqS5BuSFxERAvb9Pwnfl0bNVV8ev9laUHqDu5EHx7uFNws8OiNZ3qU9TZNIuqfyKUhw8juZeUvwKay2YmSLs3_BrO1D8okZrk4190uBontGkbRRxPxNRLWQRLnQCF_9EmI6U-BTOboSIdEcBuC-raLrf3K6ewx1907ey0SZHT4Yuw6a9mZg7xObQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=PqLwcZX5jZWz0P_QXVXAkHA4QAVLpmHybQKeBaRx9cPTF4zb1YPtFvNI5-5prpLnrvI72o_mx43G-AAYjqMiGLG_HIkCIUUttzrcjEiidzRrg7464-muGBqoBbhwWucLMMkpbngk5aelAI8_CN8iYhW6jBtAAkXqS5BuSFxERAvb9Pwnfl0bNVV8ev9laUHqDu5EHx7uFNws8OiNZ3qU9TZNIuqfyKUhw8juZeUvwKay2YmSLs3_BrO1D8okZrk4190uBontGkbRRxPxNRLWQRLnQCF_9EmI6U-BTOboSIdEcBuC-raLrf3K6ewx1907ey0SZHT4Yuw6a9mZg7xObQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند تا پسر اهوازی وسط جنگ وقتی رفیقشون خواب بود این شاهکار رو خلق کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65985" target="_blank">📅 11:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65984">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=pow02GiB5F1XaATTSShR0ctNe0Kr8ZZweqhC4iCB18rOxYda0GwPRsyMAuIA1vLU4Y8SPsqzZE3gmLZQbG2tuh-H2KNtdfSjfFb6dto5Hwe0iB8cjuv1Zb61ytHopZVffR8X0aCwVvc8h2Dd9jWJno4uzLu4LycvIeLisyIKpqvAm7oo-FV9ZhwbXa8KhKrKyMCaAw6NBpeC8QCWZhQbifN6gaxLKm1vHu7MOyLvx5VufBCh1jkcKE4YcVTNskYl4OHeXBpNEcQc71cjjZR_LLyIv4zG9Ryo7xeCNFqIG_ozNPjMDDcXCV67Usfg968HkFJyGcW8WSLk5DkvDaTLhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=pow02GiB5F1XaATTSShR0ctNe0Kr8ZZweqhC4iCB18rOxYda0GwPRsyMAuIA1vLU4Y8SPsqzZE3gmLZQbG2tuh-H2KNtdfSjfFb6dto5Hwe0iB8cjuv1Zb61ytHopZVffR8X0aCwVvc8h2Dd9jWJno4uzLu4LycvIeLisyIKpqvAm7oo-FV9ZhwbXa8KhKrKyMCaAw6NBpeC8QCWZhQbifN6gaxLKm1vHu7MOyLvx5VufBCh1jkcKE4YcVTNskYl4OHeXBpNEcQc71cjjZR_LLyIv4zG9Ryo7xeCNFqIG_ozNPjMDDcXCV67Usfg968HkFJyGcW8WSLk5DkvDaTLhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ربات گدا در چین دیده شد
یک ربات انسان‌نما که از چندین روز بدون شارژ ماندن شکایت می‌کرد تا همدردی رهگذران را جلب کند، در شبکه‌های اجتماعی چین مشهور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65984" target="_blank">📅 10:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65983">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=AvgI8RTu5W-1UqRvQ-rHhmnDIvvoHzhohREOmWl2tB3zRGRMLBJLRmx2nsT2kvO_Ent3gDmL0itU4klexH0j9dL1aYevrDSP_6AszL1jopcWMBozdobYoWsdADox8V_qwtmZM7KfoauSG_o9DXIMvgPDWe4W3d9SNPp2L4kaT1yRtbuDWTiU7i4zYSYQ87WIKrlcPyFToZYgOVXxW-sFeOgw25Osc74K6JUcGgXO3vpBCUxpbx7WiH2rQxwNLBkK2tKjzTe4I08sICsopiC7ap7eUowSHBzceQt59oSodVnFrZq6ZGxuin3vDzdfWgKlO7Q4ZR_fqXd5MMxzSh-ViA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=AvgI8RTu5W-1UqRvQ-rHhmnDIvvoHzhohREOmWl2tB3zRGRMLBJLRmx2nsT2kvO_Ent3gDmL0itU4klexH0j9dL1aYevrDSP_6AszL1jopcWMBozdobYoWsdADox8V_qwtmZM7KfoauSG_o9DXIMvgPDWe4W3d9SNPp2L4kaT1yRtbuDWTiU7i4zYSYQ87WIKrlcPyFToZYgOVXxW-sFeOgw25Osc74K6JUcGgXO3vpBCUxpbx7WiH2rQxwNLBkK2tKjzTe4I08sICsopiC7ap7eUowSHBzceQt59oSodVnFrZq6ZGxuin3vDzdfWgKlO7Q4ZR_fqXd5MMxzSh-ViA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد دیدن این ویدیو از مسعود فهمید جز توافق راهی نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65983" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65982">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpieZW2_LCPmlp1OMxYpXWf8TRuzMECY4noRDM6j8fWa4tzGq2ammVlGFK137GtsJjlEBm1xUrBdBfXVh2CnTbVeEypB2zf_K9sP3RN32EzlROQH__zwgK1bAgd_RTGAhzqANN-0xoCI_0HQwWjxWtZxg9Z-zSu8tvRR3ZcteCGHC_26z6TBAhBwJ-nIRng6adDjegqLFcOYG5QQR8M1vj1amCigFe4HfFu4-54y-hPzzmAM1O3jalH2eEGxsKoPo2GfFiDAefnX1NCIpeYv-hOzjGsHaryutagK8SSyUMKRY4Zi46K1WkCl5scqIacxewx2RFa_msAUARFS75fmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ایران چندین پهپاد تهاجمی یک‌طرفه را در تلاش برای حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند، در حالی که جریان ترافیک از طریق تنگه بدون مانع ادامه دارد. این کریدور تجاری بین‌المللی همچنان برای ترانزیت باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65982" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65979">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJNaxr6Cm3xsRioVYTPwyIfkQ1Gnv-RWLVHyqQ3n29qVtZYTAmXYefBqUxQ68yofefsQBkf-CqM29hE1_NA79Hm4IpfxrWL246mW6cpbjd1cOp-HhJKEThFEEoWHDYuwMfRPaiEc3j6Yw3IdL37L8UWQ1ky8FTEX6gTlqFZGJfG7wUcqQD4gUCLirg8aHmuBMZE3lglnjjUKOz3SEulcbAhshoCHLYmvsPDECazg13r84GLLFMD-HzEfrHbi2F6cLVR4b_woRYCVB1uzfaLtRUoOhQv-5kHZhZ7C6W9BlJT18GZbw5inchNB1Py2eZh2dP5CixzAf9b2FvzmOKxN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روح الله خمینی:
اگر آمریکا و اسرائیل «لا اله الا الله»بگویند ما قبول نداریم چون که آنها میخواهند سر ما کلاه بگذارند
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65979" target="_blank">📅 09:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65978">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=VwCKyjOqzc_wIZW16ze-xlZuSs4970w1geXzBEf1iQ-1_tRofsfzx_fwuu5_xb932nYjunPGV-Ep5Q1mUo3xaS2GTc2C-6-perGbNNU3bsI6IgGiMc8AcRgL7SRqbYDNn8qdAlnH2f11xb6xQLkIG7-qH2sbqbCamUFv3NnZzA9HdUhBgo_tlu4TzdWm77otWbFxK0rAdLln-Reeun8YqlIX5RXbHRvoskph6_mWAHTFQXNqeZ6cxDhK3WkedCBvMTj-LCnLFVWHBc9lPqod1AA9uw9YbwA17-085_QHrzIIfUQu5DOZL8oOTY_U2EYZ-Qb2lZHaWmwE_DuBMNq9gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=VwCKyjOqzc_wIZW16ze-xlZuSs4970w1geXzBEf1iQ-1_tRofsfzx_fwuu5_xb932nYjunPGV-Ep5Q1mUo3xaS2GTc2C-6-perGbNNU3bsI6IgGiMc8AcRgL7SRqbYDNn8qdAlnH2f11xb6xQLkIG7-qH2sbqbCamUFv3NnZzA9HdUhBgo_tlu4TzdWm77otWbFxK0rAdLln-Reeun8YqlIX5RXbHRvoskph6_mWAHTFQXNqeZ6cxDhK3WkedCBvMTj-LCnLFVWHBc9lPqod1AA9uw9YbwA17-085_QHrzIIfUQu5DOZL8oOTY_U2EYZ-Qb2lZHaWmwE_DuBMNq9gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی خامنه ایش رو میکشن، مقاماتشو میکشن وتحقیرش میکنن بعد میزنن تو سرش میگن بیا بشین سر میز امضا کن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65978" target="_blank">📅 09:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65975">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8NXfycsd6vrQA8SutUGqZ-b2TvZBiyH15o4PasyllShLvxLm5AsxHhsrZ6OGrT74rIQJh6R0HDqP4JwrASDxqrgr0SIY-PMNECK7AycPEPdhMInUqpwJdJqHKGFr3DOy3znetuwbKndkGcuSVafGMBdtzeq0YZlLn144P6bFFTMlzXCxp10I8GWcuOBvwPcnqbUyMcRHWiOswnU-0jXDm17GfYfCwkwLrNf3zOeSR1Mfss9KByevrN2KKo-p5ExZFQDDJHmS07VdNYcdeAGUeN_jXL-HedbUdHFtdzPFETT3qDqqC9c_Hw6QJ6sgSa7zM_MkJTXqcqrgYMlxpZ0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تندروها گرفتن رو قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65975" target="_blank">📅 01:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65974">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
سپاه:
کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65974" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65972">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک  @News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65972" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65971">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65971" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65970">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=dptQyvKDLJumlYFvYq74PFcZe1cdvCdhQQQpqImS0pHisQn6Dbfq489bh-3jIUuXZQXVIs7ta2jcxAvmFuPfhR82xKn_buIKBJqI9RCeCEr2GODp8Bi-mW-2U1g7UKI8l0tj4brPzAMdGdBg2e9JuWj9CQFeTEwqlgIzOsYG3zKX8Y6VNgro0pYvrJADEot2JNnwFCbLitwBOClxeUONHXDktQbGU8N8UjfXnNVXwS34XmAGW_tBhrgO5TgUEdBAmNQBsriw-3147gq0cIkReD_GHZnWs-fwJTzVrsspSDY5evPR4UEUTIAbJJlvJxmZXJ8EKl7cO-DEL0qfGp1fCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=dptQyvKDLJumlYFvYq74PFcZe1cdvCdhQQQpqImS0pHisQn6Dbfq489bh-3jIUuXZQXVIs7ta2jcxAvmFuPfhR82xKn_buIKBJqI9RCeCEr2GODp8Bi-mW-2U1g7UKI8l0tj4brPzAMdGdBg2e9JuWj9CQFeTEwqlgIzOsYG3zKX8Y6VNgro0pYvrJADEot2JNnwFCbLitwBOClxeUONHXDktQbGU8N8UjfXnNVXwS34XmAGW_tBhrgO5TgUEdBAmNQBsriw-3147gq0cIkReD_GHZnWs-fwJTzVrsspSDY5evPR4UEUTIAbJJlvJxmZXJ8EKl7cO-DEL0qfGp1fCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدا سیما: هک تصویر انفجار اتمی در تلویزیون، سیگنال آمریکا بود
!
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65970" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65969">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060800d75a.mp4?token=qEiTuR5l9oVx3gUR-K3f_qui2GDUsOBpSMaAEm1NKo2nSeiLcuyLZ1WEH7fwffiowOCpxpIgbAhUvawoS_0MK03lwmQKcQIzShQ4kW9sb8gqRQ19Bl7_AmnrpQF5k6npOU-BQX9kdDKtrrPK2dnqd-8aKV1w05eiXBkP_7AXMOaAMBWaH4_HTBauo7i8ZU2Zrg0ygBWd1Q-ai5NOUIboCSuG-A8dLsbAMcj79R2nFQKA6pyrZoA9jQe85sju9K-krDMxVuNObUQtRAJYVSyMAPrO-PIs4ukDOr6BErW2OcfpK1-xoxhKwVknZnsM6XhQ03IUAJTBXADEuJrvbXmxSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060800d75a.mp4?token=qEiTuR5l9oVx3gUR-K3f_qui2GDUsOBpSMaAEm1NKo2nSeiLcuyLZ1WEH7fwffiowOCpxpIgbAhUvawoS_0MK03lwmQKcQIzShQ4kW9sb8gqRQ19Bl7_AmnrpQF5k6npOU-BQX9kdDKtrrPK2dnqd-8aKV1w05eiXBkP_7AXMOaAMBWaH4_HTBauo7i8ZU2Zrg0ygBWd1Q-ai5NOUIboCSuG-A8dLsbAMcj79R2nFQKA6pyrZoA9jQe85sju9K-krDMxVuNObUQtRAJYVSyMAPrO-PIs4ukDOr6BErW2OcfpK1-xoxhKwVknZnsM6XhQ03IUAJTBXADEuJrvbXmxSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گفتگوی عراقچی هم اکنون شروع شد.  @News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65969" target="_blank">📅 23:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65968">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود
دارایی‌های مسدود شده طبق یادداشت تفاهم اگر امضا شود، آزاد خواهد شد
هیچ‌یک از دارایی‌های ما نمی‌تواند مجددا مسدود بماند
برای جبران خسارت ایران طرح بازسازی در نظر گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65968" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65967">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
عراقچی:
به زودی ایران و عمان بیانیه ای مشترک در رابطه با تنگه هرمز منتشر خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65967" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65966">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
عراقچی:
به طور قطع تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65966" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65965">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
عراقچی:
پایان جنگ در توافق همچنین به معنای خروج اسرائیل از مناطق اشغالی در جنوب لبنان است و ما این موضوع را صراحتاً به طرف مقابل اعلام کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65965" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65964">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkjVm3h4zlG-iyBgUYJiNUrr40e1395l_G-xrQFqT4VKlmatPqh96jP4Kdt3ymKp8zMULwSsaeI0-ybeIo0WXdBH6ANDcpq4b87hZOf-7zv5kgvR1_MKEBPBPmHuVv4DXQwCP2nw7kTbdv6axbLX_i-hR4s6Hqw1tQhp8t84hV96AceiYkYtzV8w9JglKYVpnjbmS9MYkaSBIk7NcPVy6oGZsd71G6hPrccBnMu9w4aMGjiU9rxShXqJTJLa72zD06l5FmaRlV2vnc2S_R9i3WJNaitUdmdixVb8bCQCg77xLu6tWPhv7Scxt3TKKEqljXttSM7xunMaZSiUSz74og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
هر چه بکاری، همان را درو می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65964" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65963">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65963" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65962">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما پیروز میدان هستیم؛ مقامات خارجی به من می‌گویند که ایران را این‌گونه نشناخته بودند و ایرانی‌ها شگفتی آفریدند و با قدرت بیشتری از جنگ بیرون آمدند
من می‌توانم اسم ببرم که کدام مقامات این حرف‌ها را زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65962" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65961">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
هیچ دوگانگی بین میدان و دیپلماسی وجود ندارد و هردو در یک‌راستا حرکت می‌کنند
به این ۲ رکن، رسانه و خیابان‌ هم این‌بار اضافه شد و ۴ رکن باهم در یک‌سو حرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65961" target="_blank">📅 22:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65960">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
همهٔ ما مدیون تک‌تک نیروهای مسلح هستیم.
همین‌طور ما مدیون مردمی هستیم که ما را تنها نگذاشتند و هرشب در خیابان‌ها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65960" target="_blank">📅 22:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65959">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
عراقچی:
دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65959" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65958">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
#فوری: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65958" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65957">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
خبرگزاری تسنیم وابسته به سپاه؛
حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است
«حسین الحاج حسن» نماینده فراکسیون حزب‌الله:
بر اساس آنچه از سوی مقامات ایرانی به روشنی به ما ابلاغ شده، لبنان نیز شامل آتش بس است.
بر اساس آنچه مقامات ایرانی به ما ابلاغ کرده اند، اسرائیل از خاک لبنان بر اساس این توافق عقب نشینی خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65957" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65954">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
کانال 12 اسرائیل :
توافق قطعی است و این به نتانیاهو اعلام شده.
ترامپ از ایران خواسته به صورت علنی درباره توافق شفاف سازی کنه و هشدار داده انجام ندادن این کار پیامد هایی رو به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65954" target="_blank">📅 22:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65953">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
رویترز: امارات ۳ میلیارد دلار از دارایی های ایران را آزاد و به آنها تحویل داده، این اقدام تضمینی بوده در ازای اینکه دیگر به این کشور حمله نشود
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65953" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65952">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOB9Pr_Wpu0GnxuQKczfgQaDyK0m4ZOeGWVYU3BIfN6sNEAhiu_0iM6i5VRunkUenGperINEYo7pAx7t8LeN3Jcbj2AAxdHmkaeaRcZJDDe0DazA07wSctl3rlKYlf87MLAL5JvzSghA999rE8ReIurkiOkkRcWuS4-EmZbenbxFbWoLZuEKyZ1rv1EEAWWWbYkmmVoEz0G_erEp6Pv6TbMZuTuaOvHMuJ6_EEwMSqxDoCqHvS8IgCIYKbupwEG-chm_7RTYozVG2Lul6QkR5w_CmH83sRohqhzn8EiKAcICN0J2E_jaae4a7Zz3hHZE7Nyi2mF0epAbY8-KVKiVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوری
: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65952" target="_blank">📅 22:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65951">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDk5xhMNMPYF57h1vy5PWYr_2LblfQZzvDMHnTtfTJZQTMQomw3pwZ33dE4d9of9AQdGWBpFYDhigdvdPft4mmjFrPg66fkXwWBF6dZJpdMWA5hL5WVrWmNiSCkUnQ0VQuzoLZM2DA1MEZknmgedSWoyk9L0F3tBelCey5OBKTDCdrU0E5pzr_6dxaskGfp8BIM26X-CLuB_uGDwB9PkKxeJpA0B5w-WqvV_fZtRuwvGHKdDMUE8gi9AtXtbXHu69kVrWVb9MxzSvCqshxKPJEcmCFBHsk4k8fTLzvxtyRvYpinBdi2nKaAkii579geRr0LirSOE754PgJg0v0nOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا به شیرمردان سپاه اسلام و حضرت آیت‌الله العظمی سید شیرمردان حاج آقا مجتبی حسینی خامنه‌ای، خوب دارین کیر می‌کنید ترامپ زن کصه‌رو #hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65951" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65950">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5cAa5KQ_ti41CgQdrvt37ZARZ8jsPs7NrwayTL_y1tjImURHbnkbAu4wkFzQkQorT1207XE_lryWrlMWA4_7FWD8gBQDCJBNCEU2PHhEFw8kQo-iVjnE3SHgoLoKMqVP0CHfDmpUJVUPCZPZ5vG_11wyyWwbqcEBLQYbmX72RSqOqlHkNGWsur7vvkJueOEyu_PV4VaXKabE182c8byXg9mErxalF5hBnWubzy_raEoyY5pLzgXVvTtf1aY7JCzvBeDQWb0Q3UQnYq1bR6hmrUcJdWG86pswFon6R06ce2_K5TCCmS0j7NP2g8tk4vTwBySzdF_mz1vKU0_dWI0SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است.
نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65950" target="_blank">📅 21:25 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

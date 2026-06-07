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
<img src="https://cdn4.telesco.pe/file/ocVDeNuEXmKXrvs81S0SGTH5H5z3hTpsPbe_l8ABthcUER6a0N4eW4b2C9KxKSvXTXHVqdMGKBp1V7e1DFTBibWv-Y_oDh2tV-TbDncxW3vcShMCdKuiZHHb_IiaL3CmQ84YLCoSsbMyB8J-39gwEM9SckanTj8XOoy9bUCyOZDosSIzjhHYhTKmSFeTHezUk1BGiG4n5pOCtjq_0-MpTpnep7VpGGEYQglsrUmbo5i_H-AacVVfFGppkT4xGlzoSYmCxup5v7vX0TrhtJCuVGOp3L9q2TSKyRYg1OlukP9WM17Kk8zc7V1dSDUhOEuAy_IeVH_p8UuV_msetfnbCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 291K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 14:32:08</div>
<hr>

<div class="tg-post" id="msg-13672">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیویورک تایمز: در گزارش تازه‌ای آمده است که اسرائیل در ماه‌های اخیر جاسوسی از مقام‌های آمریکایی را، به‌ویژه آن‌هایی که درگیر پرونده ایران بوده‌اند، افزایش داده و پنتاگون سطح تهدید ضدجاسوسی را به بالاترین سطح رسانده است. طبق این گزارش، نگرانی اصلی آمریکا این است که تل‌آویو توانسته باشد گفت‌وگوهای محرمانه واشنگتن با ایران را شنود کند و از مواضع داخلی دولت ترامپ درباره مذاکرات و سیاست خاورمیانه‌ای او آگاه شود.در این گزارش نام چند مقام آمریکایی هم آمده است؛ از جمله استیو ویتکاف، فرستاده ویژه ترامپ، البریج کولبی، مقام ارشد سیاست‌گذاری پنتاگون، و مایکل دیمینو، معاون او. نیویورک تایمز می‌گوید افزایش این نوع شنود و ردیابی باعث شده پنتاگون محدودیت‌های سخت‌گیرانه‌تری برای اشتراک اطلاعات با طرف‌های اسرائیلی در نظر بگیرد
@withyashar</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/withyashar/13672" target="_blank">📅 13:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13671">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وکیل تتلو: امیر تتلو واسه ماه محرم درخواست مرخصی کرده تا بیاد مداحی کنه. @withyashar</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/withyashar/13671" target="_blank">📅 12:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13670">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3vi0LHIxQ34trtIw816yL8hU3xhS0wVBk9HzXAdbooikcUhhAlGZ6iDv5jLwin3IxLpJv83A7A4EeEp79Prv45DRYN5zXjMKSD7slzNaw3HexClRVCDQqVWx39uOTU2CUmNUk8j5lz80t1eOZaTqWTiuvAHWSG-bnucKLkeQKSGJOXypDTlSwh3rQ9_qtsk9qIXu69rIgOnUYyBkHOLoiegtSyXUapjKXZ-L5EE8TlzlcnbCEzAsH9WYSfiMyL2zbAEMJTSGfb1CWSYQyLXCGgJDyPnENBu3WEygjIycziPSI0faf_Onf4wRNZG8PTcW325_re3JL-hndsv2b-saA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل تتلو: امیر تتلو واسه ماه محرم درخواست مرخصی کرده تا بیاد مداحی کنه.
@withyashar</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/withyashar/13670" target="_blank">📅 12:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13669">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myrGlsU3_y4Dafja16taUJRouLwyUFpXqq06X4UFU8Rkks2b9P4biEZQpT3YLCPR30_u14pwojIIl8T1e_A1Csdq3fZ9Y3b6FwvPcrNPtEeQ8wTmusJw_377UgLvFDqlQKCAiGl1AEnUKdLXKMQSDxE6sID7-HhBqvSDPXi_0sHE0TBNWMqpJsMSSfD85Zc_m8JcXHPb9kYUVkIUdDtng_zoPDxo6UDMmEvNigQDync5jK7Wlnb9KTsnM2qOSqL_BldEazW4ClgKdl9jkoH-Z1fn4ZRetMx3YMl1ehiQv_Xi7qFZrVZPlrTrRMuZxTbZpZxWyzXRVu-LZapGsUOFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ پاکستان اعتراضات شده و دولتِ پاکستان اینترنت رو تقریباً کامل قطع کرده. بعد اینا شدن عباس پیگیر واسه ما فاز شخصیت و حقوق بشر گرفتنو از طرفین می‌خوان خویشتن‌داری کنن!
🧴
🚿
🧼
🧽
@withyashar</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/withyashar/13669" target="_blank">📅 12:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13668">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تلگراف : آمریکا در حال پرواز هلیکوپترها از سواحل عمان برای هدایت نفتکش ها به خارج از خلیج فارس از طریق تنگه هرمز است
شناورها سواحل عمان را در آغوش می گیرند و تا حد امکان از سواحل ایران و آب های بالقوه مین گذاری شده با اتکا به راهنمایی نیروهای آمریکا دور می مانند
@withyashar</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/13668" target="_blank">📅 12:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13667">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر کشور پاکستان(سناتور سید محسن رضا نقوی)امروز به تهران می‌آید تا تلاش کند در مسئله دارایی‌های ایرانی مسدود شده، پیشرفتی حاصل شود @withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/13667" target="_blank">📅 12:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13666">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کانال 12 اسرائیل :طرح موساد هنوز می‌تواند به سقوط رژیم ایران منجر شود
@withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/13666" target="_blank">📅 11:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13665">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">العربیه:مذاکرات متوقف شده بین ایالات متحده و ایران... و یک "پیام بسیار مهم" از پاکستان.
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/13665" target="_blank">📅 10:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13664">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTqSKrNQnPBC_JKPKjK9WFjEPJZN4HobbXsOC-vi63jHzNf9oAvPSVzP2S9XAMDxq2mNRjzqE303A3n1u0uiE3Kaw_vCHEeVHu6Bmi-8w1yWnVnNi-2qFf3phsfxk4bpYA6OCfHI23vkIYYdX0PZJrbi8oTEfaKfvfqmmMmQBw0WvqkZjtoJVr3JxfVGdYlscPvdAcMeZoEweoTPDoEctGjyUmnZ1qBKM2qHsldUO4c1mMCIqg4q23Jd5xUsRXNZonXspjpKHKSAJ-5j8nfKjA4Rm-6ELNff_8e41dv1ZQM1vI7gT0-HW0v2LKAzJj3ariGS4zVIBEyKQquEWPE-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : خدای‌دریا  @withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13664" target="_blank">📅 05:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13663">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13663" target="_blank">📅 03:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13662">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5NYmXqupScv__fvqNl5NjqfCa3kAgbWHLlMX7qvL1ge-65Z_nnAfQQW08Dwt8gIh6W0YPbEIHKUjdQtRV9zdbbIrasfqJz9GAMF9II3UZI6rh4Td4qzD_o57-6mXT2dOq4ySRCZQpczXjlmEQ6aS0Qc8Jvo-1W0JWdb5ZdO3h96lX5DdVzfcnX5-6-8QF4KUbLNHBsS-Cuizz3Y_yJN3TuZwFSI1P2-SMGXC4OvzXOawGlJv8mo6mDn2W5ZQ6PvIuN9en4TwnKAn6sAfb20M4suhg75h-u9mtZOeb0lku1UqHJUta_dtdOdJcTPJN1hHoabgueNFZVddrrbivl28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تقریباً ۱۱۳ فروند قایق تندروی نیروی دریایی سپاه در مناطق مختلف تنگه هرمز درحال گشت زنی بوده اند
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/13662" target="_blank">📅 02:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13661">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/13661" target="_blank">📅 02:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13660">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/13660" target="_blank">📅 02:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13659">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرده @withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13659" target="_blank">📅 02:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13658">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff55958846.mp4?token=HJctt4DF1-AgpQ_jQfZbiKF_Iie6dw4pEyoERIdPrKbgszv7h7ALG_9Gb3CXa47r0ajjUt0oc3L5CfgI_Kp5llN2fIaM5-qf87G6osaFzxZitUWIwS_RXlf-XIJlvUdoiFyNpdhvTdWMvjSveEHSsK3Ks-gmS-DpbvPJiDpg4ee6hV-w8IlW5cFFR3BGc8WO73LQhB_msMJ5FI0m9Sn4YDzv9dHWRVKgL0m4a9sD0TkvRffOQZexXDBD2v0ZonbhoB1FgHfn6WHPJd5H6T39Ucra0se9VW7iaRIP3WztF4MF4lrRVFeWk7xofbfM17gFeB8B7UvFo5DRT2FjsV5q6ZiQ2vtPx83--725zrpmdR3uJY55VyKEbrOWEJCG9kDbeXnZ6PI1Gb8UIbsD3GjmvuQUZWkcjop8tLp_r1JG8xbJbUbYupaoo7cJuYOfn-R9t6lTxW8EnTbN4ohgZ8IIA3PmKy9_RgeYrNefFrjKaZd5WFcg_zJi_crPBbumbGieGuSAiShiKBiNR3im6xAT23g0ODmaKUhw2_KcQV4lc30hDTFb_3FT_1Kz9bJYzXvJRXN3zP_pf14FeMEoBf1No0mctZvH40ujA8uvbVfHRpi5RqSeRVzCV02rp6ttsOBPnxIsSgupDbFaw0tqenMPyUgddPtOONtIWFzYRDquObk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff55958846.mp4?token=HJctt4DF1-AgpQ_jQfZbiKF_Iie6dw4pEyoERIdPrKbgszv7h7ALG_9Gb3CXa47r0ajjUt0oc3L5CfgI_Kp5llN2fIaM5-qf87G6osaFzxZitUWIwS_RXlf-XIJlvUdoiFyNpdhvTdWMvjSveEHSsK3Ks-gmS-DpbvPJiDpg4ee6hV-w8IlW5cFFR3BGc8WO73LQhB_msMJ5FI0m9Sn4YDzv9dHWRVKgL0m4a9sD0TkvRffOQZexXDBD2v0ZonbhoB1FgHfn6WHPJd5H6T39Ucra0se9VW7iaRIP3WztF4MF4lrRVFeWk7xofbfM17gFeB8B7UvFo5DRT2FjsV5q6ZiQ2vtPx83--725zrpmdR3uJY55VyKEbrOWEJCG9kDbeXnZ6PI1Gb8UIbsD3GjmvuQUZWkcjop8tLp_r1JG8xbJbUbYupaoo7cJuYOfn-R9t6lTxW8EnTbN4ohgZ8IIA3PmKy9_RgeYrNefFrjKaZd5WFcg_zJi_crPBbumbGieGuSAiShiKBiNR3im6xAT23g0ODmaKUhw2_KcQV4lc30hDTFb_3FT_1Kz9bJYzXvJRXN3zP_pf14FeMEoBf1No0mctZvH40ujA8uvbVfHRpi5RqSeRVzCV02rp6ttsOBPnxIsSgupDbFaw0tqenMPyUgddPtOONtIWFzYRDquObk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خدای‌دریا
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/13658" target="_blank">📅 01:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13657">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13657" target="_blank">📅 01:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13656">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش صدای انفجار در حوالی سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/13656" target="_blank">📅 01:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13655">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">از روی استوری تو اینستا وارد کامنت میشی کامنت دیده میشه ولی از پیج خود شاهزاده وارد میشی دیده نمیشه تقریبا هم ۶ هزارتا لایک خورده. من فکر کنم همه به ادمین پیج باید اعتراض کنن چون من خودم زیر یک پست دیگه اعتراض کردم اونم هیدن شد الان دوباره کامنت گذاشتم که…</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/13655" target="_blank">📅 00:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13654">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoheil</strong></div>
<div class="tg-text">از روی استوری تو اینستا وارد کامنت میشی کامنت دیده میشه ولی از پیج خود شاهزاده وارد میشی دیده نمیشه تقریبا هم ۶ هزارتا لایک خورده.
من فکر کنم همه به ادمین پیج باید اعتراض کنن چون من خودم زیر یک پست دیگه اعتراض کردم اونم هیدن شد
الان دوباره کامنت گذاشتم که این جور ادمین بودن خودش دیکتاتوریه</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/13654" target="_blank">📅 00:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13653">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رویترز: ایالات متحده در حال بررسی راه‌هایی است تا دارایی‌های ایرانی را در اختیار متحدان خلیج فارس قرار دهد تا به تأمین مالی بازسازی و تعمیرات ناشی از حملات ایران کمک کند
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/13653" target="_blank">📅 00:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13652">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkvBCIv8r0qa5rX55VMwo3dMXtzNNXfqOfai38t75jM_uQj6PkDrugDfVsKDua87T9goANorn7GpGd4nXNHE9xBKutu6v4EDiEClI--STvDOVjgWdSGmWt3KJatsny4zAg3kpAuDIoSWYE0AcPWbvG-YXoQ2wkMa0bvDqttyQKLSUgB7QfBTz-BmKXjxfTovtYbAeg5J_szRfoTCeeteCvRDIh_LLvFrPhFV81crYlKvUXz6R7y0wL-tLYylrb-6-tIzusDmdKQD-P8BVvtj_3fIlFUps2XbbcuLIBHvPolV7oB_43HpU-5s1Z08MUgMFVAZpN-OvHELDTAoCq-skw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث شبیه آخر ویدیوی هست که پست کردم شبه حمله
😃
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/13652" target="_blank">📅 00:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13651">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/13651" target="_blank">📅 23:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13650">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">https://www.instagram.com/reel/DZQKl3sRlmS/?comment_id=17866790943686477  پست جدید اینستاگرام ، کیا منتظر شب‌حمله هستن ؟!</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/13650" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13649">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مهم ‌محمدجواد لاریجانی: سایه ترورها وجود دارد، آن‌ها هم باید بدانند که حتما بهایش را می‌پردازند و ترور، ترور دارد
کارشناس ارشد مسائل بین‌الملل: اینکه فکر کنیم در صورت تحویل اورانیوم‌ها و حق غنی‌سازی جنگ تمام می‌شود، اشتباه محاسباتی است
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/13649" target="_blank">📅 23:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13648">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/13648" target="_blank">📅 23:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13647">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرگزاری ایرنا به نقل از وزیر کشور پاکستان: «پیامی که برای رهبر ایران می‌برم مهم است و امیدوارم اوضاع خوب پیش برود.»
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/13647" target="_blank">📅 23:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13646">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">https://www.instagram.com/reel/DZQKl3sRlmS/?comment_id=17866790943686477  پست جدید اینستاگرام ، کیا منتظر شب‌حمله هستن ؟!</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/13646" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مهر: صدای انفجار در خارگ مربوط به خنثی سازی مهمات است @withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/13645" target="_blank">📅 22:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">https://www.instagram.com/reel/DZQKl3sRlmS/?comment_id=17866790943686477
پست جدید اینستاگرام ، کیا منتظر شب‌حمله هستن ؟!</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/13644" target="_blank">📅 22:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نیویورک‌تایمز: اسرائیل مکالمات مربوط به مذاکرات آمریکا با جمهوری اسلامی رو شنود کرده.
اسرائیل تلاش‌های خود برای شنود مقام‌های ارشد آمریکایی از جمله ویتکاف و البریج کولبی، معاون وزیر جنگ آمریکا، رو افزایش داده.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/13643" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13642">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15cea3880.mp4?token=eZ32zuemNTIK0yrsN6PpUm9X7n72vHt4730sLRaJZEc80DflcAHthj0jpj3STh2BOTywhOcp2uW2Jf2elmKTBn5EDQMQmElxtRPib6GWT2elDNELX9owh6MuEwaO4zb4tlh2ZAK_pqh2Smdu7KcZErJ2yxZWWxvJPOtwueQsQpuYW-gyUJNCFhdYSac_4TVGLfmdxopSS77mk1cGnYPYm0vmptJFLVWUzOwDKGZaQWKY7xknIn-d3LsqTQGqoqVGOZfho4ecxWY8GviUQ2u7QDa7YRXBuY-SzAewsPrhiXwyS5G0aFJThhU1ymDb7YzYE_-afBmPD8Ex7EocSb7xFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15cea3880.mp4?token=eZ32zuemNTIK0yrsN6PpUm9X7n72vHt4730sLRaJZEc80DflcAHthj0jpj3STh2BOTywhOcp2uW2Jf2elmKTBn5EDQMQmElxtRPib6GWT2elDNELX9owh6MuEwaO4zb4tlh2ZAK_pqh2Smdu7KcZErJ2yxZWWxvJPOtwueQsQpuYW-gyUJNCFhdYSac_4TVGLfmdxopSS77mk1cGnYPYm0vmptJFLVWUzOwDKGZaQWKY7xknIn-d3LsqTQGqoqVGOZfho4ecxWY8GviUQ2u7QDa7YRXBuY-SzAewsPrhiXwyS5G0aFJThhU1ymDb7YzYE_-afBmPD8Ex7EocSb7xFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نورتروپ گرومن سامانه دفاعی
«AN/AAQ-24 LAIRCM»
را برای هواگردها توسعه داده است؛ سامانه‌ای که برای مقابله با موشک‌های حرارتی و دوش‌پرتاب طراحی شده و به‌صورت خودکار با استفاده از لیزر، جستجوگر موشک را منحرف می‌کند تا به هدف نرسد.
رسانه‌ها آن را به تهدیدهای منطقه‌ای علیه هواگردهای آمریکایی و اسرائیلی در خاورمیانه وصل می‌کنند. نورتروپ گرومن می‌گوید همکنون این فناوری روی بیش از ۱۵۰۰ هواگرد از ۸۵ نوع مختلف به کار رفته است.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/13642" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13641">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3cd7dfbe.mp4?token=IV5YMFFGusVjzq69Ds6miLLsJ2qzPzi535xdCoiqiBBIG7Liy18SJUmGWDwysFkgEC3XfRCauvK4U-djVZjdOPHFzTd-xHbjLQWwtjEj6-v-XkQM5cLV2YMeoMfXQuLMw7Q900ot2CjEMpNSHw-u1x5M40glKPRFqMXV9P98afjoJmPxpJsQP-FEJMP47a41jB_WkjD-PgHz74GutIIkjviY1YzDkpCuz8vCfKb-48s9uDuLxxArpx6TcnqQWDMULLkkGOtgTQQTzPP3Z4T5K1K-ieXV70gYNnE2ma_xnzfvQ_fWwaBXIE3JIwcbq7tZuZw6AbygITxuVRvTe9g3BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3cd7dfbe.mp4?token=IV5YMFFGusVjzq69Ds6miLLsJ2qzPzi535xdCoiqiBBIG7Liy18SJUmGWDwysFkgEC3XfRCauvK4U-djVZjdOPHFzTd-xHbjLQWwtjEj6-v-XkQM5cLV2YMeoMfXQuLMw7Q900ot2CjEMpNSHw-u1x5M40glKPRFqMXV9P98afjoJmPxpJsQP-FEJMP47a41jB_WkjD-PgHz74GutIIkjviY1YzDkpCuz8vCfKb-48s9uDuLxxArpx6TcnqQWDMULLkkGOtgTQQTzPP3Z4T5K1K-ieXV70gYNnE2ma_xnzfvQ_fWwaBXIE3JIwcbq7tZuZw6AbygITxuVRvTe9g3BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان بابل پهپاد شناسایی دیدن با کلاشینکف دارن میزنند
🥴
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/13641" target="_blank">📅 21:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13639">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مهر: صدای انفجار در خارگ مربوط به خنثی سازی مهمات است
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/13639" target="_blank">📅 21:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13638">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLgoEMJChIjogF-UOLubZ860R_5wl8HcVMc8z0l6zn0ENI4yNzxNbyBXqFoGX0p7EsnzkzvqxnnzKMUDVox83WRjHpjo6C8whkrMUh8TT-bU_8-B4u3yLrVoeD0X9b-LCwsymBkc_kYFTIHI_1bocuHZHrf8cXtkIVjrkyXK9fLO72m2au3pg4rDvnb9S2R7-WY5CUa25D07ede1KWS7WPrxymf0EF8mB66jN92R_zqzBcj8TL8sR5oP9WEppN4So-3PjwTUtQgBw0TuHw2kwlo4i9iLH1ZFhY_7NbrMRbC9Po0Vr9o2ulTKOUWTQbS5Qrs-Efb23n7LXjG9Wq9kJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار وزرای کشور ایران و پاکستان
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/13638" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13637">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کامنت رو رفتم زیر پست جدید پیج دوم شاهزاده   https://www.instagram.com/reel/DZQKl3sRlmS/?igsh=NzNsemFkNW9lcml0</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/13637" target="_blank">📅 21:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13636">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/13636" target="_blank">📅 21:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13635">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کامنت رو رفتم زیر پست جدید پیج دوم شاهزاده
https://www.instagram.com/reel/DZQKl3sRlmS/?igsh=NzNsemFkNW9lcml0</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/13635" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13634">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77683181b.mp4?token=Y4gY1Vad3aDJbnn4ISHt5_xugJMFx3fJ7v3ONc0ag_08bsgGbGu6Ppx5SGAu27g3KIqKTodMgWK0LyB777USSNnFt0PHmAs3GxLGqFsn_3ErKHmuj77bXMUQnQpxjNXPWhQmPN2GBeqhqLgKOi5OjIL-jjMkEDdEJzfWOtxzgNkB2057Pxgrq59M-sbXVnX0d0ZBvCPCZKRNg-r6C9n86N5KGGlCc3T9rK_WrNSYnJbyuFCknzt5S7FRh03fpHr4gmhHDdAjtcLMpqbAUwPK2xng-UBi7LvnUKaNuXmUMfqVS8dNdlq6gKhbxyJmny3J_0X48LPucggZEsW6fEf6zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77683181b.mp4?token=Y4gY1Vad3aDJbnn4ISHt5_xugJMFx3fJ7v3ONc0ag_08bsgGbGu6Ppx5SGAu27g3KIqKTodMgWK0LyB777USSNnFt0PHmAs3GxLGqFsn_3ErKHmuj77bXMUQnQpxjNXPWhQmPN2GBeqhqLgKOi5OjIL-jjMkEDdEJzfWOtxzgNkB2057Pxgrq59M-sbXVnX0d0ZBvCPCZKRNg-r6C9n86N5KGGlCc3T9rK_WrNSYnJbyuFCknzt5S7FRh03fpHr4gmhHDdAjtcLMpqbAUwPK2xng-UBi7LvnUKaNuXmUMfqVS8dNdlq6gKhbxyJmny3J_0X48LPucggZEsW6fEf6zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فعالیت جنگندهای ناشناس در آسمان بندرعباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/13634" target="_blank">📅 20:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13633">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/13633" target="_blank">📅 20:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13632">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6234155d.mp4?token=ctnipa6nO2pIanf4fa8OEytNZpeNGnnX1_WnoeJGX2jCteMAXhdJWX1pA4-wCcmCiUmvGiI3rUwrP46jpoGxY2YQ-o-FAubUoViyBzCm8qL1xgvYEpMmhIl0S0tsBDqX1aUoyhFzLfJKQnsswtxO7AKq9JPnWz0lBeXL5iR5rRsxuzKkx2L0Es0gQhHhPYtXh9Am_IO14Wl1ieFNX3SA0aHFh02U9vf6x845qsriiSSxFvYQQJpZQT_u0RTimJrAQFYLPCjiPWzhLrEiDhcRvsBSIiuaiB9l-2NVr6RXOlCFnJes00D7UmdfOEYJOYVE3FSOKy1FAsx7cyghVgnbGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6234155d.mp4?token=ctnipa6nO2pIanf4fa8OEytNZpeNGnnX1_WnoeJGX2jCteMAXhdJWX1pA4-wCcmCiUmvGiI3rUwrP46jpoGxY2YQ-o-FAubUoViyBzCm8qL1xgvYEpMmhIl0S0tsBDqX1aUoyhFzLfJKQnsswtxO7AKq9JPnWz0lBeXL5iR5rRsxuzKkx2L0Es0gQhHhPYtXh9Am_IO14Wl1ieFNX3SA0aHFh02U9vf6x845qsriiSSxFvYQQJpZQT_u0RTimJrAQFYLPCjiPWzhLrEiDhcRvsBSIiuaiB9l-2NVr6RXOlCFnJes00D7UmdfOEYJOYVE3FSOKy1FAsx7cyghVgnbGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/13632" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13631">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/13631" target="_blank">📅 20:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13630">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuD_xJuM2r-J0xTVNqVSMcUx7yzPbjlA7m1UgkB34EZokQ43gkx4R7v3jIHHiibP1mTedJzvdGGaPY6IUtwG0M1XjD5KU9a9ZvX3xEDUOo_oCTR2hjCdVRsnxCnPMbb4xmFOWje9tmQkuyDWisZ9OIhsYmHaVKzvy5uq05ixB4GTzlA0kiXVbBqZ3wkuAUc47jhZR8fd-da2z4kw07jF90RabQuqZr8gsPuZTpaVeWiCy5cgQu5CdVePD6Qbhv8X80MRMjO6_zQcO8nzC0hN0AZjdudjuZ5IGBvE7L7z1tmjRRTGHvUPrVIhn19pNWt57VoNtsVkP748SP5B1UvMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ایران و بستن تنگه هرمز، به صادرات تکنولوژی‌های پاک چین مانند باتری، خودروی برقی و ... منجر شده و به بیشتر از ماهی ۲۰ میلیارد دلار رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/13630" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13627">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">العربیه:
ترامپ به میانجی‌ها اطلاع داد که مذاکرات با ایران بیش از 60 روز ادامه نخواهد داشت که این مهلت در روز های آینده به پایان می‌رسد و ایران باید به‌سرعت پاسخ دهد.
« این خبر فیکه که پخش شده »
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/13627" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13626">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d35551fc6.mp4?token=tKR069eGWmnlCjzcgo66OkRchNYzLMmkgRwIf9f-PnmW0Ssj1aCryGqikk3JWlAXFuwnJsdIJUe3nMghKxjsu-bDpyoR5ziQ6Q8QmUgqm8OppKCGhiqZ61-6xZWWAZrS3TkPEftHl3Eh9Ee9KF3UWJhE0tZWjZEGw_gN7SSZhuL02Zu5lVlxJ9--kRjtbRHYAG31dgHPBVoPYPbjvmUMGHEiNLrXG89HeDo_nHfO-qJvfFKDkuOZ6YzfnuvwvyWaEzN5u_rDDYPlFftlsWdqWstYTljx3pwo4Hr1MJolsGYfKliOjDhIou3rjL0ngMipjz0kvg09WHyF7P3KVW-5CnGPt8S1DiYUKfJv-61q94EAA0EUD2qyqrmr1Gs3gz5slCUt54P1KDm_bjHeiQ4rmXOgzO_S01ujtj9nu0Ghhz4d-WVl8VSFWvtQ6S2qjtP_n0baDDUDgTClu02cYCKvUUUcmY371MiZzFzL2UD2V_SX34dqfKJJ86DzQncLZnRl-lp1WO3hKW9yAL0jn7bEZvWt5gfLLbgpw7M5Gz7q6UoTvlLYFNEk6J5oIaQkvqDLoqH4liy3fcaRapEQS5BdVu9L9QF83ec3DAAIU6YWA894rfcQLsAXjrtnh0hpKGkfC1qSIoVN4PXXoL7HwtV_SR94dW0uCZm8ylVYKSZYdVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d35551fc6.mp4?token=tKR069eGWmnlCjzcgo66OkRchNYzLMmkgRwIf9f-PnmW0Ssj1aCryGqikk3JWlAXFuwnJsdIJUe3nMghKxjsu-bDpyoR5ziQ6Q8QmUgqm8OppKCGhiqZ61-6xZWWAZrS3TkPEftHl3Eh9Ee9KF3UWJhE0tZWjZEGw_gN7SSZhuL02Zu5lVlxJ9--kRjtbRHYAG31dgHPBVoPYPbjvmUMGHEiNLrXG89HeDo_nHfO-qJvfFKDkuOZ6YzfnuvwvyWaEzN5u_rDDYPlFftlsWdqWstYTljx3pwo4Hr1MJolsGYfKliOjDhIou3rjL0ngMipjz0kvg09WHyF7P3KVW-5CnGPt8S1DiYUKfJv-61q94EAA0EUD2qyqrmr1Gs3gz5slCUt54P1KDm_bjHeiQ4rmXOgzO_S01ujtj9nu0Ghhz4d-WVl8VSFWvtQ6S2qjtP_n0baDDUDgTClu02cYCKvUUUcmY371MiZzFzL2UD2V_SX34dqfKJJ86DzQncLZnRl-lp1WO3hKW9yAL0jn7bEZvWt5gfLLbgpw7M5Gz7q6UoTvlLYFNEk6J5oIaQkvqDLoqH4liy3fcaRapEQS5BdVu9L9QF83ec3DAAIU6YWA894rfcQLsAXjrtnh0hpKGkfC1qSIoVN4PXXoL7HwtV_SR94dW0uCZm8ylVYKSZYdVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در تروث
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/13626" target="_blank">📅 16:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13625">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFehGAPDsJV5VQhPs14V0TCzB6RV2WMw5q18HLKSk8y0s0vF46HYlRb-ori8Fe1uaxkyV1uQiVfocagTDWRDVrXfVfNw1FIIDC5bC9TQUPG01419eIA86KqgPB8z7QOKb27VCqM9MaMAvCPIpAywJfyzYZ80QsF7-XgWgg39ylMDXV7hJteaDWxxhjKf41uJGzTJfQeSpNT86h0MJfzKT67_EXs06meNCB7sLw1_UJCL2V4s6BCWNJMXzqOa9NgiFJ1ls7-FZlAMiY0ByFrMtP-F0W1Zhq9bfG9_okF0YVaV5KsuZeAlmYz0bCSP_ZB-I-4vZjOWSqvdAr_y9Zxbtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل مخابراتی پایگاه شهید راهبر نیرو دریایی سپاه در بندر سیریک که شب گذشته، هدف پرتابه‌های آمریکایی قرار گرفت
پیش‌تر اسکله این پایگاه در طول جنگ هدف بمباران آمریکایی ها قرار گرفته بود.
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/13625" target="_blank">📅 15:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13624">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزرای کشور کشورهای عضو شورای همکاری خلیج فارس (GCC) جلسه اضطراری تشکیل می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/13624" target="_blank">📅 15:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13623">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مدیرعامل آسیاتک: اینترنت دیتاسنترها همچنان قطع است
مدیرعامل شرکت آسیاتک، با اشاره به تداوم مشکلات دسترسی به شبکه در بخش‌های تخصصی، اعلام کرد که برخلاف برخی اظهارنظرها مبنی بر بازگشت وضعیت اینترنت بین‌الملل به شرایط پیش از دی‌ماه سال گذشته، دسترسی مشتریان مراکز داده (دیتاسنترها) همچنان برقرار نشده و کسب‌وکارهای اینترنتی کماکان با چالش مواجه‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/13623" target="_blank">📅 15:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13622">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ به میانجی‌ها گفته ایران باید زود جواب بده
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/13622" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13621">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/13621" target="_blank">📅 13:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13620">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صدای انفجار قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13620" target="_blank">📅 13:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13619">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">(IG @yashar)‎⁨منتظریم کی شب حمله فرا می‌رسد⁩</div>
  <div class="tg-doc-extra">اتاق جنگ با یاشار (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13619" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/13619" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13617">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزیر کشور پاکستان(
سناتور سید محسن رضا نقوی
)امروز به تهران می‌آید تا تلاش کند در مسئله دارایی‌های ایرانی مسدود شده، پیشرفتی حاصل شود
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/13617" target="_blank">📅 12:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13616">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d357648b.mp4?token=ZcKo91uLKjZ9Eed5IqFQw_H3zYYNghywFMpY7D9kg8CNa2rEaHPs0zl1Jwk9sGUCE0ZEtK-obqOk7XDFsH-2IrY7oIhMAxp67hdYyTjpryiwQc0dMvNqv-_zdtXpJE4nMkF0d7CF14OPyZFj87gltR2mukwUBYF2K6iZV3iXx3w8cKcfCaEXzS9C69vjiefw_bcMVXgH7nt_Ywm5rtZBpkoa4z1LjDOQoKUzZfiVEuKYBRbwh0E5FH_vGNYG2tfxZMC_1GHULFdXUT8XAbwXgbua0Omk4bFOc2jlwZesqCYiTpRJT1owiUWLg3Z4pDC6bTrwtU0Qy1TQ0DwCF---QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d357648b.mp4?token=ZcKo91uLKjZ9Eed5IqFQw_H3zYYNghywFMpY7D9kg8CNa2rEaHPs0zl1Jwk9sGUCE0ZEtK-obqOk7XDFsH-2IrY7oIhMAxp67hdYyTjpryiwQc0dMvNqv-_zdtXpJE4nMkF0d7CF14OPyZFj87gltR2mukwUBYF2K6iZV3iXx3w8cKcfCaEXzS9C69vjiefw_bcMVXgH7nt_Ywm5rtZBpkoa4z1LjDOQoKUzZfiVEuKYBRbwh0E5FH_vGNYG2tfxZMC_1GHULFdXUT8XAbwXgbua0Omk4bFOc2jlwZesqCYiTpRJT1owiUWLg3Z4pDC6bTrwtU0Qy1TQ0DwCF---QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون پرواز هواپیمای اف-۵ ئی
تایگر ۲( تک نفره )متعلق به هوانیروز جمهوری اسلامی برفراز مشهد
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/13616" target="_blank">📅 12:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13615">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEGSM5z7WVyC3Yw9HUr7s_WWVTDXY_lDB8CxkUndszFpkhJg3rX0BQ30UDkvz4m7cUHN6NTcjDunSIvzfEelVmgmtg0r0DfZyRw6s9LjMHA1QUDoq-YKLerveiqmApnXpONX7_jJePIGmRjCeqPNtIKhJX_DbpbhGsa0T7yKjR_VatAXzpBO7Kma92NhlBZ7hHk57sesUWdzbqhfuKmG4pTUVZnIp1p3X7WnKGyg2PAW9lKEVgcQyqsMYgoGrgUHILQi-6x_1H8dy2DyTR5i97c9AwAxXAD85k6iI8L33jgmIauFHKtwhAk55oNFUdp4kBy9JmfQYvQBfbYfZ_mn9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس های جدید پایگاه هفتم شکاری شیراز بعد از جنگ
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/13615" target="_blank">📅 11:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13614">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ورزش سه :  آمریکا به 15 نفر‌ از اعضای تیم‌ ملی ویزا نداده و رفتن ایران به جام جهانی در هاله ای از ابهام‌ قرار‌گرفته.
رویترز : کسایی که ویزا نگرفتن برخی از مربیان و هیئت همراه هستن وگرنه تمام بازیکنا ویزا گرفتن.
آمریکا اعلام کرده اجازه نمیده افراد غیرورزشی به بهانه ورزش به آمریکا بیان
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/13614" target="_blank">📅 10:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13613">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سنتکام: ۷ موشک بالستیک ایران به سمت کویت و بحرین شلیک شد
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد ایران هفت موشک بالستیک به سمت کویت و بحرین شلیک کرده است.
بر اساس ادعای سنتکام، شش موشک توسط سامانه‌های دفاعی رهگیری و منهدم شده و موشک هفتم نیز به هدف مورد نظر خود نرسیده است. سنتکام همچنین اعلام کرد هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/13613" target="_blank">📅 10:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13612">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ba7b496b.mp4?token=nvggBSCSllMJTQu-XaDsW14LRuLfMsxTQUDNqODagHNvUojRwq9czgTNWqb2AoP3ILZmAjxPNF3XMZ5Tfowx3wpXySZdiMMroBw7vt-BB8SeFxvLVdbBfyfhd1pvt30PS2gxBe_wzffbHo3ugnQ_fJPWDZIU-4oEClpP8wNdqjGYWlDxSvp9Rr3yw9GsdCpvjzmEG72idvupqce7BWfSyEMDnN7LmVBdtrNdazLcET3FtrW195yc1HRWYL1rTGooteeQzL7uv3-0gIGH1bQXvuRwLa7Q0me3aveYMP5YlxpghKHL7ZjEkx4KfnV1htVPiE9Ygfwm8Y2lTSUgWrB1Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ba7b496b.mp4?token=nvggBSCSllMJTQu-XaDsW14LRuLfMsxTQUDNqODagHNvUojRwq9czgTNWqb2AoP3ILZmAjxPNF3XMZ5Tfowx3wpXySZdiMMroBw7vt-BB8SeFxvLVdbBfyfhd1pvt30PS2gxBe_wzffbHo3ugnQ_fJPWDZIU-4oEClpP8wNdqjGYWlDxSvp9Rr3yw9GsdCpvjzmEG72idvupqce7BWfSyEMDnN7LmVBdtrNdazLcET3FtrW195yc1HRWYL1rTGooteeQzL7uv3-0gIGH1bQXvuRwLa7Q0me3aveYMP5YlxpghKHL7ZjEkx4KfnV1htVPiE9Ygfwm8Y2lTSUgWrB1Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر کرد و
کفت
حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/13612" target="_blank">📅 10:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ارسالی : من بابامم تعریف میکرد که زمان جنگ عراق و کویت صدا های بمب هارو میشنیدن خرمشهر
@withyashar
گزارش های زیاد از شنیده شدن انفجار کویت از خرمشهر !</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13611" target="_blank">📅 04:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13610">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWRwKz3VdHdspvrPEs1yiIcsPQ6anxqedTm9HsF2HYKDRoP2vN_hpZ5obPKSaCreLncWi_wKcTcdIaDVXk9DBSGzQs-1FGQr09rewwvip0lauyXw8f9ObGal-HFMinno3Md23XNZxiMiviLZSAppAih-NtdLj2yLKmCzIsOg1ay9uHRT03WNpE3MQohgHQDWBe6OhizOFTe8yZra3k3f3IRPTGz7vAEI8GL8T2fUMlgb6byJf4txk0VQ20IaJd8IyDXSGnd6VigI7PHczzSDhlHLzBbF7vatocSFvP5KwSH2FYsBVDMzL8rjYNT16k5QnvFcu8E02MbzGbFxxhMMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : کویت آلارم اومد الان ، ۳پا موشک زده سمتش !
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13610" target="_blank">📅 04:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13609">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622170a597.mp4?token=lK1rd3_hjkValj9Tu4rXl2oDicbivyiWwUqe0Rv9IMY8SI07a6YtDJfQcind0HuCdMXmuzC7CLJADteIozqqvp4G2r95wNWXHO5KFKGGOduOzkfg0g3p3XRuNmTidU6ugikVfVtZBxQvh24j0dq27YFjbvb08gS_D9vO-yca_8tE0mxE0H2Zjh-5lDymSXFS8iIlycWtjyqbxA137yrFR6CpzVmZtdiJ_g4wqQef95A6aTVP8cMDQB8ql7vPT5OytKYnrzemKFZiHrjXjzSrJJVZxBMpueRRfHzWBmn9vnFTXZqZd8lj8IiBO_WR-2wY5KFwvdq6TTsv3o49EYp1Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622170a597.mp4?token=lK1rd3_hjkValj9Tu4rXl2oDicbivyiWwUqe0Rv9IMY8SI07a6YtDJfQcind0HuCdMXmuzC7CLJADteIozqqvp4G2r95wNWXHO5KFKGGOduOzkfg0g3p3XRuNmTidU6ugikVfVtZBxQvh24j0dq27YFjbvb08gS_D9vO-yca_8tE0mxE0H2Zjh-5lDymSXFS8iIlycWtjyqbxA137yrFR6CpzVmZtdiJ_g4wqQef95A6aTVP8cMDQB8ql7vPT5OytKYnrzemKFZiHrjXjzSrJJVZxBMpueRRfHzWBmn9vnFTXZqZd8lj8IiBO_WR-2wY5KFwvdq6TTsv3o49EYp1Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در‌تروث : نیروی دریایی ایران
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/13609" target="_blank">📅 03:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13608">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda12e11f6.mp4?token=u0iSFLRYjyCQDRaRZfToTCwN5LX_3eBNc0NkbDFgIYhNwdzBfXFCSvNgR35ZNwDf_vE7dp6P_XzUWhcNvOCplkpwhuPvo-ROksfPKIi9YERffc4ZJ-jtFjSi1g2tRGTCje9wdS0Okzl9r_Z1PxU1T9J6bp226vRsWyqHIc5i8u6FQ6rPoiHUCFc8yZSaoeIsBsTYMJ1jfMrR-g-j68VmN5uDP70zlSdgfcYKqR8kBGuVHIrA8EiwqwisZmXsSfDVXieqx-v2NRbnQIsKorTx3gMr0z41jCLVenzt15xthiNfFqqmd6LvUPL9gteLBQ7rjE5IHl3BnZkQm9LHSmOUsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda12e11f6.mp4?token=u0iSFLRYjyCQDRaRZfToTCwN5LX_3eBNc0NkbDFgIYhNwdzBfXFCSvNgR35ZNwDf_vE7dp6P_XzUWhcNvOCplkpwhuPvo-ROksfPKIi9YERffc4ZJ-jtFjSi1g2tRGTCje9wdS0Okzl9r_Z1PxU1T9J6bp226vRsWyqHIc5i8u6FQ6rPoiHUCFc8yZSaoeIsBsTYMJ1jfMrR-g-j68VmN5uDP70zlSdgfcYKqR8kBGuVHIrA8EiwqwisZmXsSfDVXieqx-v2NRbnQIsKorTx3gMr0z41jCLVenzt15xthiNfFqqmd6LvUPL9gteLBQ7rjE5IHl3BnZkQm9LHSmOUsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون
جت‌های جنگنده آمریکایی در حال پرواز بر فراز استان بصره عراق نزدیک مرز ایران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/13608" target="_blank">📅 03:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13607">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea974c1bb.mp4?token=B8FLs4HRYKL4RsNe6JQNZYtdW2SuWLoTh1OgIB6HqS6Rl1enbpqNQQWFyqhchM8EjZBzl5RyZ-mUvSbSCH21FiLWzdjtXZsgYwGYC0Ke6GPQl8Zs6lrf7ZyDHTG3NpAHNQ74W7n9zIbZ-hC_oAQ6sQgpVgaYM2Ct1QL6zAdrgi8AyXN8t5KYrJLWPP6CRcWMJfJbpQBnhUwZgKUeVYJwZht0jwG2c3OGzqLGlWANPeu4IsqZpW-eGnGNddSMZDbgtxIM2Tyei-dtQ3CLWn6E2g3ynSczepSztSlAfDS9O5JOX-Eiuu31Zpoo8gfiYiOSlpb84PcWxP8J6WzWhz9jXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea974c1bb.mp4?token=B8FLs4HRYKL4RsNe6JQNZYtdW2SuWLoTh1OgIB6HqS6Rl1enbpqNQQWFyqhchM8EjZBzl5RyZ-mUvSbSCH21FiLWzdjtXZsgYwGYC0Ke6GPQl8Zs6lrf7ZyDHTG3NpAHNQ74W7n9zIbZ-hC_oAQ6sQgpVgaYM2Ct1QL6zAdrgi8AyXN8t5KYrJLWPP6CRcWMJfJbpQBnhUwZgKUeVYJwZht0jwG2c3OGzqLGlWANPeu4IsqZpW-eGnGNddSMZDbgtxIM2Tyei-dtQ3CLWn6E2g3ynSczepSztSlAfDS9O5JOX-Eiuu31Zpoo8gfiYiOSlpb84PcWxP8J6WzWhz9jXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتک نیم وارو پهپاد های شناسایی اسمون بندر عباس همین الان
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/13607" target="_blank">📅 03:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/13606" target="_blank">📅 03:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13605">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/13605" target="_blank">📅 03:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13604">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb45455c0d.mp4?token=JG4KuFt2ckk5D7J5tv1_TCSZgQn_jZOaW-hCdQzVXUncngPIYYHJNAKBRhtqHCMAcDLZfJzih6sW9j37S_BhoT2iq0tUqMsrqRZ79DfD4P7qfsmrP-QNPOXexfjWu6f3xbSt2Gb_miKEcTtwxkj4fyVyRoPurAUiHHnOPCIL_R-X01vCJkq4_HAUVMion2vWDp3fjlbee7NVMtj6gHHFXni1nvgDaGZJWSsyxvSkYGdbwGSBPf4N3yo_WRBulbTAAdJSpkNdiA9ITOHo4k-S40tplekbwaVnJE9r7sydo-Nh8ILh2Wl8fxJkzW1N9St4XCGYrodSWGcrvujDcNNwLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb45455c0d.mp4?token=JG4KuFt2ckk5D7J5tv1_TCSZgQn_jZOaW-hCdQzVXUncngPIYYHJNAKBRhtqHCMAcDLZfJzih6sW9j37S_BhoT2iq0tUqMsrqRZ79DfD4P7qfsmrP-QNPOXexfjWu6f3xbSt2Gb_miKEcTtwxkj4fyVyRoPurAUiHHnOPCIL_R-X01vCJkq4_HAUVMion2vWDp3fjlbee7NVMtj6gHHFXni1nvgDaGZJWSsyxvSkYGdbwGSBPf4N3yo_WRBulbTAAdJSpkNdiA9ITOHo4k-S40tplekbwaVnJE9r7sydo-Nh8ILh2Wl8fxJkzW1N9St4XCGYrodSWGcrvujDcNNwLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
منتظر زارتان زورتان</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/13604" target="_blank">📅 03:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13603">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">۳پا باید یه جوابی بده چیزی‌ دیدن یا شنیدین بگین</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/13603" target="_blank">📅 02:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13602">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چندین انفجار در سيريك
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/13602" target="_blank">📅 02:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13601">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کانال ۱۴: همه امیدوار بودند که آتش بس برقرار شود، اما بازی به طور کامل در حال تغییر است. برای یک آخر هفته فوق العاده گرم در خاورمیانه آماده می شوند، زیرا ایران و آمریکا از اعتصابات تصادفی شبانه به رویارویی های روز روشن تغییر می کنند!
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/13601" target="_blank">📅 02:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13600">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سنتکام : چند لحظه پیش، نیروهای سنتکام چهار پهپاد تهاجمی یک‌طرفهٔ ایرانی را که به سمت تنگهٔ هرمز پرتاب شده بودند، سرنگون کردند. این پهپادهای تهاجمی تهدیدی فوری برای تردد دریایی منطقه ایجاد کرده بودند. در ادامه، نیروهای آمریکا برای دفاع در برابر حملات بیشتر، سایت‌های رادار مراقبت ساحلی ایران در گورک و جزیرهٔ قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ‌دادن به تجاوز بی‌دلیل ایران در چارچوب دفاع از خود، در حالت آماده‌باش قرار دارند.
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/13600" target="_blank">📅 02:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13599">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
سنتکام از حمله به سایت های راداری قشم خبر داد!
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/13599" target="_blank">📅 02:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13598">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چندین انفجار در سيريك
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/13598" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13597">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سی‌بی‌اس نیوز به نقل از یک مقام آمریکایی: نیروهای آمریکایی حداقل ۴ پهپاد را که توسط ایران به سمت تنگه هرمز پرتاب شده بود، سرنگون کرده‌اند.
🚨
@withyashar
بچه جنگ شده باز</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/13597" target="_blank">📅 02:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13596">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚠️
@withyashar
گول نخوری !</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/13596" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13595">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فقط در ۴ ماه ! بسوزید عرزشی ها</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/13595" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13594">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💥
290k عرزشی سوز ترین کانال تلگرام</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/13594" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13593">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش هایی از قطع شدن اینترنت
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/13593" target="_blank">📅 01:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13592">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سی ان ان : منابع می گوید ایران چندین پهپاد را به سمت تنگه هرمز پرتاب کرده است. نیروهای ایالات متحده حداقل 3 تا از آنها را رهگیری کردند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/13592" target="_blank">📅 01:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13591">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوتا صدای انفجار الان ومد همین الان قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/13591" target="_blank">📅 01:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13590">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مجری ان‌بی‌سی: رهبران جمهوری اسلامی معتقد نیستن که به‌طور کامل شکست خوردن.
ترامپ: ایران به دلیل تصور برخورداری از قدرت کافی، از امضای توافق خودداری کرده. ایران در نهایت گزینه‌ای جز توافق نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/13590" target="_blank">📅 01:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13589">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ به ان بی سی:
خیلی از مقاماتشون مغرورن، یه سری کارها هست که هیچوقت فکر نمی‌کردن مجبور بشن انجام بدن ولی الان مجبور شدن، راه دیگه‌ای ندارن و این قضیه زمان می‌بره.
داریم درباره 47 سال حرف میزنیم که هر کاری خواستن انجام دادن.
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13589" target="_blank">📅 01:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13588">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ به NBC : وضعیت برای اونا واقعاً سخته
یه جورایی استقلال زیادی هم دارن، ولی سال‌ها با یه رهبری ضعیف و بی‌اثر از طرف آمریکا و بعضی کشورهای دیگه طرف بودن؛
طوری که عملاً گذاشتن هر کاری دلشون خواست بکنن.
من فکر می‌کنم خودشون هم الان باورشون نمی‌شه به اینجا رسیدن؛ جایی که عملاً خیلی ضعیف شدن
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/13588" target="_blank">📅 01:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13587">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: رهبران ایران چاره ای جز رسیدن به توافق ندارند‌‌
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/13587" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13586">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌ @withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/13586" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13585">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13585" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13584">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به نظر می‌رسد جنگنده‌های اسرائیلی از عراق به سمت ایران می‌آیند
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/13584" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13583">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ارسالی : پدافند ۱۷ شهریور گنبد کاووس فعال شد @withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/13583" target="_blank">📅 01:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13582">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ارسالی : پدافند ۱۷ شهریور گنبد کاووس فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/13582" target="_blank">📅 01:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13581">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به خبرای هست ولی نمیتونم ثابت کنم</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/13581" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13580">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/13580" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13579">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارشهایی از صدای جنگنده و پدافند در شمال کشور
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/13579" target="_blank">📅 00:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13578">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: ما خیلی سریع از ایران خارج خواهیم شد و نتیجه آن، به هر شکل، بسیار قوی خواهد بود؛ چه از طریق یک تکه کاغذ (توافق) و چه از راهی بسیار سخت‌تر. شاید حتی راه بسیار سخت‌تر، آسان‌تر هم باشد.
اما ما از این مسئله عبور خواهیم کرد و قیمت کود شیمیایی شما به‌شدت کاهش خواهد یافت، درست همان‌طور که چهار ماه پیش بود. قیمت کود شیمیایی اکنون هم کاهش یافته است.
قیمت انرژی، نفت و گاز نیز همگی به‌طور قابل‌توجهی پایین خواهند آمد. و صادقانه بگویم، من تصور می‌کردم قیمت‌ها بسیار بیشتر از این افزایش پیدا کنند.
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/13578" target="_blank">📅 00:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13577">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش های تایید نشده : چندین جت جنگنده آمریکایی حمله‌ای را به بندرعباس و مناطق اطراف جزیره خارک آغاز کردند و چندین بندر از جمله فرودگاه بندرعباس را هدف قرار دادند. پدافند هوایی فعال شد و درگیر نبرد شدیدی با جت‌های جنگنده شد.
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/13577" target="_blank">📅 00:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13576">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش هایی از شلیک نیروهای ایرانی به سمت ناو های آمریکایی
🚨
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/13576" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13575">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره خارک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/13575" target="_blank">📅 00:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13574">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">@withyashar
only for pro members</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/13574" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13573">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">@withyashar
operation economic fury</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/13573" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13572">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/13572" target="_blank">📅 00:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13571">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجار ناشناس در نزدیکی کنسولگری ایران در استان سلیمانیه در شمال عراق.
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/13571" target="_blank">📅 23:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13570">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7Dt78CVFOAeNhNZksGxqadAXP1tybGxzt0m38w5-rwd5OvnJcCYrD3JY0YRy7qBW-pOPT9NY_aLJByxuKdR-4S-be7XpAWo8EhlzcIvAdC5_BOiPBA5OtlhecvqB3S_hgk80gQVddlfETvrjJgv2ZaAIHIzunED888hEJ3sGQK8-v9yqTrjLYEsdNLV5rQf8LWzOJBkkZgC8nS0IYWP0xR-VL0_0OpB0G3uhTMAj3Us1RHSaYO6M-JUmdOM1gFbo2aDDLgObVKoMNGyGVaeaVPjCTkeaa0VPz8vdiqPunMROxLtqmE4B-gZ9hVf-EZtN3fg98ExybDG359jIN12BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواستگاری جنجالی قیصر از الهام چرخنده در تجمعات حکومتی
قیصر در یکی از تجمعات حکومتی، به‌صورت علنی از الهام چرخنده، بازیگر سابق تلویزیون ایران، درخواست ازدواج کرد. این اتفاق غیرمنتظره خیلی زود در فضای مجازی و رسانه‌ای مورد توجه قرار گرفت و واکنش‌های زیادی را به دنبال داشت
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/13570" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13569">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شبکه ۱۲ اسرائیل به نقل از رئیس ستاد ارتش این رژیم: قصد نداریم از سرزمین‌هایی که در لبنان پیشروی کرده‌ایم، خارج شویم
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/13569" target="_blank">📅 22:34 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

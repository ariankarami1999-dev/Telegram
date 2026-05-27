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
<img src="https://cdn4.telesco.pe/file/itfe9HWladFvMsHjxkchCHzNiMUcZq58O9q7li4YO9LTYtfcXyeVz2S05KXF1lZYeLY15Qyvkr0F8JVON7um4K3Oy7J2t1oqKZwpUUSGaWEGYkErhLxL4PwGRnmQoM8WlyLiyWduUl-zshL693Z2pTL6QZBeKW_Xw49gpJZLW_DL3nnp9Lp_oZEkxg6wLxXOkPnCkm5vFWWaXMKn0Hf5ZnaoyaM92F5TwK6BSEIgSW500NSv3ufKQUEcer57qd-7E3ISWMgE2WInyCa7WctxHdM7BfWzVzB0uo8DYlQhEq6GIm6TXpK41i2xQf9IjCXA6j-VsXD-FE9cHCWJI4gtIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 135K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 09:41:48</div>
<hr>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac4qn0pELJ8gqbzrPKvfcYROVr_LQiVlXJYBdZri25Z2coHHQahz7Tus-SnHnfPtrQ-TKmVNZDzTi2ffPeQHEXuTjK6E-ECSw0dc8wGfHetJHolVDqFgGRWai2rHVqmZKsXj-C_TH51ymKzLNWOgoieGQZqqOejR12wXnMs5C02WmecFvbe_VWStSzpoYJfO_t6cuUmbSrl_wivVt6t1P0QwWiBYuN5J83pcVcn4Kib_Vx354qeDJR2KxinSVhy4Lab8RLYzYd7Xp8yKFnMqx2WR9tP-zGsh_yuBlTuqnzAughAGjH-9ogiSCJ8iG47yu7ouge37seVPAiBIk5aaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyUczIRYFleyZXcvCDsPz8azRDNiSHgG-TPa6YerZa4zo-SraB79N5zEtOgCtfzSx1D3aTVtrjyas4y1OUAxZs_ZjmDxE1DbI41V_Mn4tv00B4-FCqF4Mq2Yp7uW_fflbbQiBoH8yDZ_DK99ceiA0AhNhTXJF-Kode5L3R17iCQ9kK7p-MN8WV1GrHBnOJgZkqMcbtv9glVI-kfYEV-9xMZsqr3yGWqvv4I8u1RIs0Am6gckToPrP47pnFXqJ-igbRXkQNhh_vIxAISPiF1Uy83iULkn5lUNMJa5EUR5oluoMI7Zbd2m_1twT1xr_mb92hdOA7aY6SHucAFdWpEl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTrsRvfu0L9VJt5PijU_M-VTCQaOlNHp3_UVFXreWBy6uvR9nVZYq1_eqVsOg-6ICbzaP10ae7uXli8xM_ZyS7eB51kKYZpdPbk56tOAfwlx04TqUIuIh_sGbo6zIreTch5IttY9uzogRrOa8Ds7o1WhaVgBT3bO_1uABk0jtHM-Vu5GKq3qVC89d6BxXu3EWKHq1XOjJf4kvtEhSQfYHWui8Ccnrzka2LWdmj78Q-IrQnFYLICQAkCzuudrU8f4knTVqIuhaQXeXeJhCnADXeaQ2Rt1Mkk-CjeVNJXZ2iwyNmXPg_zGP6GHechBdArareCHnKwPepeojzSM7GNdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZCHVG0CUM80XnMsmzr62tYXmRBBmDcsZ_YCl5oukanKiHM2MBUQOIxTqD0Qv-3zTKTaBxzGuYu2F7L4xErhWtyCt-utYX4MySF6kTVIu2VQUEfPzYtCwDubOGzh3Lub0ph_X8vpw1ZzO0zWurSkKlelQoYHZIwCK22eVDodzpdsELo8jpDDBrGPrvm8QV0Yf-l2Gd_kfm-gqSNlINAK3z30vKbuoNb6dHwFUi1x8t3WONY003fWX0wZZNUylTvzQ5418SzHIXKyImrmt6odvhaWIVluQ5kXRg58RCQz4DCqRcTwMTUSvYJOYWpKqoUlx1L6c7XTLPCWjVBtR4Qhkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت خونگی.npvt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/news_hut/65089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کانفیگ‌ها و سرور هایی که بصورت منطقی براتون وصله
،
در صورت عدم اتصال می‌تونید گوشیتون رو بزارید رو حالت هواپیما و بعدا امتحان کنید
.
🌐
‌ ‌
لینک دانلود NPV با نت ملی
🛒
‌ ‌
لینک دانلود مستقیم برنامه از گوگلپلی
🛒
‌ ‌
لینک دانلود مستقیم برای آیفون - 𝐍𝐩𝐯 𝐓𝐮𝐧𝐧𝐞𝐥
🚨
🚨
🚨
تعدادی از کانفیگ های V2RAY متصل منطقه‌ای؛ یکبار کلیک کنید همه رو کپی کنید.
vless://392c0d0a-157f-4fe0-b528-11586477cbe0@185.213.165.81:38024?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.80.73:2096?path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%258%D8%B97%25B3%2540WangCai2%3D&security=tls&encryption=none&insecure=1&host=sni.jpmj.dev&type=ws&allowInsecure=1&sni=sni.jpmj.dev#%40HutNewsPlus%20VPN
vless://e0a98968-eb18-417a-87e7-c8933aac5f13@31.59.40.53:52729?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
🚨
🚨
🚨
پروکسی‌های متصل منطقه‌ای با نت مخابرات:
https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
@HutNewsPlus</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvCx02mt9QBEFMmtPk-GXb1okZgrPXIsGZ3_rRsCgAnIpzO3TCckafD8QPKu2A13gwewiWhHYDjpxQCR8jFGVbwAAuYCgCbjU-ZkmpY7lwoQgyfAONyV0jRNXecX84bol8hMGuA6-WsLc2zaw_SHGgCPmjo1n0QkP1azMktsJ-5bi1sJJkopauPf1ZOoe2R13FVWEDokg5huOzL_Z8VzpXX726fAG1XBJTzS720Vp7Byokt8wySq71vDF2RN7eADL8FnEGmjrWrnddP1BjCTl2xKp8m4PmaTr_qOD5UBK9FZDovX16dPOMD5DWzyjrnCAZE2B_vSbQtOkwsRNPncIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65087">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-text">Barko VPN_v2.0.apk</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65087" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65086">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.0.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
فیلترشکن :
🟣
Barko Vpn
🟣
v2.0
(20260108)
🔹
🔹
🔹
🔹
🔹
🔹
🔹
📝
مشخصات :
🟡
بدون قطعی 100% پرسرعت
🟡
برای تمامی اینترنت‌ها
🟡
مناسب شبکه‌های اجتماعی
🟡
اتصال خودکار
🔹
🔹
🔹
🔹
🔹
🔹
🔹
✅
تست شده و متصل !</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65086" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=DoQUlfhwXWfY2bQQFAhKytua0z5X5hGLS-PhQ3_R-ZAFc4bKag2gn-qqrV2XpdkzhziVuSse22CtTLIjUZyX-MvExpoL3ckV8ACGyjamPbu2DK2Y4MOsPVgKirsNRPAuZeyuJenas_qH2t1M5LTixlDqBsqDqeud1_UqY2R3PTGgzEf5hSad5L4ordsnYW_vJka1WXRWSvbRUvtD85Q2YSF9OJvYs2VrLqUHRqnPuSrn747UyhDcpPREI0mq8JgTf6QN1XQpVe4Vh2sCUpXNHMGNQ6o8edO0j9waFja3Jvn30BQNOEOd5eWLY95B2SyAtlEEC56d2p9CHai39eRp4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=DoQUlfhwXWfY2bQQFAhKytua0z5X5hGLS-PhQ3_R-ZAFc4bKag2gn-qqrV2XpdkzhziVuSse22CtTLIjUZyX-MvExpoL3ckV8ACGyjamPbu2DK2Y4MOsPVgKirsNRPAuZeyuJenas_qH2t1M5LTixlDqBsqDqeud1_UqY2R3PTGgzEf5hSad5L4ordsnYW_vJka1WXRWSvbRUvtD85Q2YSF9OJvYs2VrLqUHRqnPuSrn747UyhDcpPREI0mq8JgTf6QN1XQpVe4Vh2sCUpXNHMGNQ6o8edO0j9waFja3Jvn30BQNOEOd5eWLY95B2SyAtlEEC56d2p9CHai39eRp4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2xKq8LdWJD6VfiZC8bDP5ICKi1ltlsARYXFt9l7jEy3UyjLrWIYta_wrFoCeCNha2OkZndqEsmlf6piSP1aAGfFw5gJTBba9dzSxNi-R17If7Ht9l3odORe0Pbu_MVM19iHGxungfEyYOOiOFrZvdiQ4_Otb7ewgyCurx76tl2aE7aIhFRQc-dxkU-tCxee70BjtFhjthffKIPwnTVRKjcfHyRA0K_bSvKWBrq9zjouEn89VLvXW_nj6EYRgFyavXJ1NZf1Bctf9aFq-vobOQAdBdlEE479jNmAfngoFpRfS9TVauzNutOrGuLwQ6HOIFQ160VntWwlWyFoVSxFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65079">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJA1D0lntFVufhXIbBezFlX8_vWVcNkH_go4NXTDTXF3HyRYDB51z60p0vOAejV_UAmab2uLX8g8p_MKyw8aBxh9ba6AzsgJtnZu7e5f4pa5PfsGXk2oGv1n2qvfitIOzg4A-TuxmWExNtIZLsVb-twdsbZYcUo4cPqNVf4emvuHXQbrhzus1NdKUStrRINf6717fnBjySoA0HEKcEIn_JHNLSYvkUXNs5L834yk1uuCu7V2rIL8DwgZC6rI520qwIZYWjrgeXfDvYrf4s1kzwS8KiYAosWQWehp-HDfi9TuCoz8BMnkygb3WpgEgXdATHhiEHcfCKGn83PtqDVTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65076">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD3hElcU9sdQrwQdnI78NY_8ekQ6AogqtpNEK7fkZq6g6yNbC68sXr657yJ9OWrmhVfJi6hT4ejxLhud2Ouvecn2CJUQzPnyTwfumzdG1FjqemXOqnHOgokdBI8z-2hAcoLuPPWhYGK1JOCdHqEuixjFYJ2Q7WyYgz2lvpGp41CWtKf1rLCrMuatKCAq-yofQLewee7syc87Crn1S1SAVgNcee9rf_85C26sjOa7gVK0G2lOXA7CwE3ME5CmnN-x6agQ4vgjzTu0VIihEO4jxHjDVdnx6oqo_NsNb3NOzJHJjqh52Dh3OYWML92BH805TDbn8ukX7D5YRI72ADXJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.
این چهار حروم‌لقمه عبارتند از:
رضا تقی پور، نماینده مجلس
کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی
رسول جلیلی، برادر سعید جلیلی و عضو شورای عالی فضای مجازی
محمد حسن انتظاری، عضو شورای عالی فضای مجازی
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65076" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65075">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65075" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65074">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65074" target="_blank">📅 12:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65073">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=uAJOITESrnD8Y5AjFx44-z8opYvzcBmiBl9K3RIJ_pIlZJfq1q3UA9VXzvMwtq6kxJPSvmGgYikRdLqrVNBxhqlTjpexuyXf1llrsrLgXQV1XL4tvDjOaZPyUxXiudXdHVkQS_0wkRSp-IWPIPi86fCwBaloGqe7wR1sXsc3zsi3me1yiTdp_24d3_3h8AnP9ngw-1qIpRClakJfZeuHZDc8HxwrPeWaEqJW5j8MM_2ZOqxtO-M4l4R-KUZWRhMH_d69U5NKKcEak7S7f1opIBSrsec0hLdylZ7VDibXwfHx4jS0W3vzb2vLuuC1K5CTweS6u5a1RZww_N46Yfb5IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=uAJOITESrnD8Y5AjFx44-z8opYvzcBmiBl9K3RIJ_pIlZJfq1q3UA9VXzvMwtq6kxJPSvmGgYikRdLqrVNBxhqlTjpexuyXf1llrsrLgXQV1XL4tvDjOaZPyUxXiudXdHVkQS_0wkRSp-IWPIPi86fCwBaloGqe7wR1sXsc3zsi3me1yiTdp_24d3_3h8AnP9ngw-1qIpRClakJfZeuHZDc8HxwrPeWaEqJW5j8MM_2ZOqxtO-M4l4R-KUZWRhMH_d69U5NKKcEak7S7f1opIBSrsec0hLdylZ7VDibXwfHx4jS0W3vzb2vLuuC1K5CTweS6u5a1RZww_N46Yfb5IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65073" target="_blank">📅 11:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65072">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رهبر سوم جمهوری اسلامی: سه چارتا جنگ کردیم همه دشمنان‌مون رو تا ناموس شکست دادیم جوری که ویران و حیران شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65072" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65071">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
رهبر سوم جمهوری اسلامی: پدرم، علی خامنه‌ای خلف پیامبر بود و بعثت الهی یافته بود(از طرف خدا مبعوث شده)  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65071" target="_blank">📅 11:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65070">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65070" target="_blank">📅 11:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65069">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GG9_a3v0o1po2xoSZOrol-7H4PZkQf5Kn6i2zPzgTzoKOLrZJgDk1GnbxZNX3yakpedkQvm7nWAAlFhfHSwVgdkXaOtZsE4nHiOyoC0mjlLGk47wt35g4EByJ3V7sHLs51_g6KhxTp7ewupICYAUqmr8yNqWfeKeK4Woo8KkfZi4mhMYqDOyYouO-ly3Pq7cflsbLX_cgo7E_23xptaZOJazftrP-iiyj6fSXkb5D5N8vR0XF7_iHO81Ql0KW6XeLUKKuOWODajV43Ihm6Ew4zadjO-fPlf6dxE8EYCjwssMF0Kt3jIWUwFXlso1fdohialPcprY8Us5KIgV2HTCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65069" target="_blank">📅 10:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65068">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YsU-LwN6wbc7SGXe6dg3xjMmYWfG2UTBqN_mYxjshhhnHO0ky41GFabdbVtZ-ka1U-knY8YcSyZc9jZwhL0ZHpQ3YpjC1HcoNfMfu8cPauJdnECHhjAxi3Di1iHWQ6LE0rNvR1xSfsOKjSlfxjoVsEUeKeGmYeuS-tuMBqvSmENhfc0-GkdKIxfiPVQ60vAc5q-sfPoNrZFmTzA0sebcJ_QIRez92qR99B8I2PFdue5_g3ssYT88XRi-aAYK3953MNhmmDvGZeBlutTpHXpXz2c0wiWdEchsudx9tuQ1AJ42woxwmWuJuUZkB7T3_z5LVXMbO0QnZ36Y4dLNycvqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65068" target="_blank">📅 08:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65067">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErU7odRmiiQWRHAcnaxg-7j5I1dT46ZWRdoaoP7tblMeFlKcXObew6ZDOKKTLqHBSVc3LE_EKgfsbTV6WFAob9B8yDhDIlX1o25C3DqvYVV1aVxZjD6nEq3AuqCBNoAFKQV3w6lsdn4AOn-4U-954n_20p9S5_lJWqEbRz7rCmIeQwHNajp5vuc4HRBHD4SqsjmnjhO-WLrkZGyEkIAkc_accjNdUD9w1l50g7msRVF6Kxh1brA-ADEtGd0n7280GyED3T4pJqh3dx3SRc6SS3MUgrbW7QSvD5OWo9CJ5IrdALVNaO32xe5NHGbZVn4fKy1Nsqxp88nUlxASk3KCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65067" target="_blank">📅 01:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65066">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صابرین‌نیوز: امریکا دو قایق تندرو سپاه رو با جنگنده زده و ۴ نفر هم کشته شدن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65066" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65065">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkk-KXQHIH1t6LbdGCC9U5hJSfEBBLA6s7gfDiNrhUkoebzjXbRYOvANtH8nmfVIzm_SV1XPicLU_cNxZY8dxLEf36uQXQqeVp3XZkjk02T4Wrcr5lVotMnoUsLu-g4-o-LQxUISCiFOyjGAnpSO83f2qngJN57DkkkHCsvjRi_oD0XyM08NhxhszxuLIc5bbllxs6yXYdH6OqIJLRFrE2j-pVsd1OLoIGS325FH8zy23Qtz_RaHx_l6XVWMn2G1NkoxLEVUAdcMGB_u1ZrlsC1MQ4dWTCf_CO7qqcIWjiV5xku6suwMZ1Z_h1iGX5S3q6Ma6yjs6SGXNVc0mEwzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود.
یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل آن، این فرآیند و رویداد نابود شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65065" target="_blank">📅 01:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65064">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65064" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65063">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AviDCQL02RQRFQh3CS5idbsyBDCVMGtAQrPncfGJZhNML9W3W2dPJ_Xixu8gk7pbIYCs5lSN7Uz7xsAiTyxT_2TBzmewSFKTHGGK0X6iQjEcmHG_JKtPc9Eqh0EWUH2X5Xs530sDKpJIu6gZAxgv27wTO0CkgbZbFqZ8GdUMMl5V7FdPgz3CjiEJzy4WzgPUT94Alcr7uDy_z4j45xh_9b0dShlxk58EDjMT1QRFDf5d7DHzV7LzwTm-LtBDjUN5KWitPnpxaBao-f7E7vv3XVtotEAqf-q-wXnvkeEQ9ecuwqNSifRMbiXpqPa2ENyyewrlua5nsbi_ls53WVdNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری تایید نشده مربوط به انفجار لحظاتی پیش در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65063" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65062">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65062" target="_blank">📅 00:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65061">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
📰
آمیت سگال، خبرنگار شبکه 12 اسرائیل:  ایران در حال حاضر فقط حاضر شده به توسعه سلاح‌های هسته‌ای رو متوقف کنه، در حالی که ایالات متحده چندین گزینه برای ذخایر اورانیوم غنی‌شده ایران پیشنهاد می‌دهد، از جمله فروش آن به ایالات متحده، انتقال آن به یک کشور ثالث یا…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65061" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65060">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">به صورت قانونی، ما یه "شورای عالی امنیت ملی" داریم که به "شورای عالی فضای مجازی" دستور میده که به بقیه اپراتورها بگه که اینترنت رو ببندن. به صورت غیرقانونی هم سپاه رو داریم که زنگ میزنه میگه اینترنت رو ببندن. زورش میرسه، میکنه! حالا دولت رفته یه "ستاد راهبری…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65060" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65059">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ: من به صورت الزامی از کشورهای خاورمیانه درخواست کردم که پیمان ابراهیم را سریعا اما کنند تا «جمهوری اسلامی ایران» را در ازای بخشی از توافق پیمان ابراهیم داشته باشند  @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65059" target="_blank">📅 19:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65058">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
ترامپ: توافق با جمهوری اسلامی ایران!! به خوبی درحال پیشرفته این یا توافقی بزرگ برای همه هست یا بازگشت به جنگ بسیار بزرگتر.  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65058" target="_blank">📅 19:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65057">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇺🇸
تروث طولانی و مفصل ترامپ درباره توافق با ج‌ا و پیمان ابراهیم:  مذاکرات با جمهوری اسلامی ایران به خوبی در حال پیشرفت است! این موضوع تنها یک توافق بزرگ برای همه خواهد بود یا اصلا توافقی صورت نخواهد گرفت؛ بازگشت به میدان نبرد و شلیک، اما بزرگتر از قبل و هیچکس…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65057" target="_blank">📅 19:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65056">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65056" target="_blank">📅 19:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65055">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywpp0_7kKWdGTi9Fh3TmTeaHXSuagSoj2SvmUkQSpSd0XawEQcBs4kl1A6c0I2m2pDlQX-LWUffO18v7xzInzrLw7VV8744VN7ud-PF5_H62bYw1WUzbhGS-qpcHgkY8iuf53GHc_-UCM8ECeH-LXnE2TxtoSxjWQa4Y-FSg7dnawFWT21zgMdL25Jh_MH62bu82GqIKVG1fXO-rac9Ce4ysE2SLcIZcrodLwsKYURJ1EkwGlRwkYVc5U-2uHfohU2pOTg-Npyt1SGPCSkYgqePV6DkyUt-FPj8TzTDg_xTOyr-AeJJxU8_Gcf897eHnU36s2yi7R4dLpDErq0M_EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم  در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟! #hjAly  @News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65055" target="_blank">📅 18:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65054">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم
در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65054" target="_blank">📅 17:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65053">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چه افتخاری هم می‌کنند حیوون های حرومزاده...  سه ماهه حق طبیعی مردم رو ازشون گرفتین و الان از بازگردوندش، دستاور می‌سازین؟ باید رید به سر تا پای دولت حقیر پزشکیان و امثالهم #hjAly</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65053" target="_blank">📅 17:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65052">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65052" target="_blank">📅 15:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65051">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65051" target="_blank">📅 14:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65050">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbFesca4_AXFnqtx6H5R71VzlDsz1ddM1H5AV1spooikjDSeT_eDDt2I88J75x9jq0OjlSF4MXcw13sRzkMzpQ1R-FKpZ19amiWJDhxaKkGtEnbmFRKRtS3cQpKEPZXQtL6wGQ3iWVdHY0bpgv3lZXRETdRFZ4JDjDDFyXbREc8r_wHXIxPTwoOWgjj3XR2nZwob5L9bZr5X1Cpk3yjF6RAVcw9hMSxspbv7C2JfVGfK3zNr08klZeHYUn6FBWB16bDcQm49wLLg8gBs7vdFyn177wflHQd1YPakpjJWXgrsbsqkv_Lyd0Oq7ZooVi_tis_pADmDy6ZGtlfpbA1aig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65050" target="_blank">📅 14:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65049">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=RvM1r39Q55pAEfXmMrQ0asMVYMvNmS0R13a0flVpwtVEMjy_znAPfsmY2IEZsoHYkafX3Q9k7H9YzPx1w-YYa076kohbNJFMgAbHFXlAW4wFF7viVL7GbCJKTp9On-HMOXYty5Bi-hlYR11fe-0FEDkazxOwve3F9oLTAFFrCRdoRH9gbH0nBUNCQ6kVlJyx6iP2X9-8JdsL8VU7_wolC8GH7kqcLypzSAPqfP1bDb2rEeL9cWYQa0M7HhYkaJZDi51zpFHJhKYyNV6S3XXUCJP0PUgn5R-7JgQ9zcQVM4Ta5-hM53u7pkrC_LXVQ_L9YRKlli504T2uKIhUhRLzMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=RvM1r39Q55pAEfXmMrQ0asMVYMvNmS0R13a0flVpwtVEMjy_znAPfsmY2IEZsoHYkafX3Q9k7H9YzPx1w-YYa076kohbNJFMgAbHFXlAW4wFF7viVL7GbCJKTp9On-HMOXYty5Bi-hlYR11fe-0FEDkazxOwve3F9oLTAFFrCRdoRH9gbH0nBUNCQ6kVlJyx6iP2X9-8JdsL8VU7_wolC8GH7kqcLypzSAPqfP1bDb2rEeL9cWYQa0M7HhYkaJZDi51zpFHJhKYyNV6S3XXUCJP0PUgn5R-7JgQ9zcQVM4Ta5-hM53u7pkrC_LXVQ_L9YRKlli504T2uKIhUhRLzMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد نگینی‌پور، مستندساز حکومتی مستندی ۴ دقیقه‌ای از حضورش تو پزشکی قانونی کهریزک منتشر کرده از اعتراضات ۱۸ و ۱۹ دیماه‌،
تو خود مستند حکومتی که منتشر شده تعداد بالای کشته‌شده‌ها و کانتینتر های حمل جسد دیده میشه که جنایت خودشون رو به کار دشمن ربط میدن و ابعاد بزرگ این جنایت مشخصه!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65049" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65048">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65048" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65047">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=fl_xLwOH_nLSf9Hs0RYaAAwllG6SUd_RFngr8ERDJG6m0NrJzozGrhRXqV_QvpiUpVTUGhsCrQzRATO1tN833xwbAqP0LHDgl1A8VoYN1RtB0aUcLH1nBBBvsH51hxG-SpNJ7bI97N4CPLgux230N20Zel4VNYo4PNBIFhsdIgImwCIxjJf_44baaktOV2IN6NfXwzWLwFL8p46ZPQJkVYZioeK2_aBfaOmZX0QmmgQnRfT-72a-F5gYQKk6uLS1SAnxiHxmILO6GKhtbqKbqK0zAv6ePxIQSbsHfbn4wCE9XsymcRBivG0Vk-9_UZXDz3VuJjivXLsMmGBXpPCWxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=fl_xLwOH_nLSf9Hs0RYaAAwllG6SUd_RFngr8ERDJG6m0NrJzozGrhRXqV_QvpiUpVTUGhsCrQzRATO1tN833xwbAqP0LHDgl1A8VoYN1RtB0aUcLH1nBBBvsH51hxG-SpNJ7bI97N4CPLgux230N20Zel4VNYo4PNBIFhsdIgImwCIxjJf_44baaktOV2IN6NfXwzWLwFL8p46ZPQJkVYZioeK2_aBfaOmZX0QmmgQnRfT-72a-F5gYQKk6uLS1SAnxiHxmILO6GKhtbqKbqK0zAv6ePxIQSbsHfbn4wCE9XsymcRBivG0Vk-9_UZXDz3VuJjivXLsMmGBXpPCWxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ترامپ قرار نیست توافق بدی امضا کنه. هیچ‌کس به اندازه ترامپ تهدیدِ هسته‌ای شدن ایران رو جدی نگرفته
خیلی مطمئنم که یا به یه توافق خوب می‌رسیم یا مجبور می‌شیم یه جور دیگه باهاش برخورد کنیم.
ولی ترجیح ما توافق خوبه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65047" target="_blank">📅 13:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65046">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قالیباف دوباره به عنوان رئیس مجلس انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65046" target="_blank">📅 11:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65045">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKePD1kZfIxmvTFRES129N6F9bxNzJ9TZr5lWCKZcsXsgFtYT2W0vB-HDTTmMrjnhPCNLlzXueUFC5SlPuqt2ueX9FCZYPwPwYZKdGnvuSg9H7M-Fm2AuLGipQ0_GS-NNdXgnARpGBpxApT_X5D2mgRiLIXHnKTPZ0DZeE9Ud6z-3sndedapeYqPmbAPWshWTV8lYF17CIUe4j_dvGxLVYv1j9Tu_FrJA36UoA5u1PuxajKctQLnrSuTW9FcCjaf_Y4-9J3DFRenq6Pt2qpiODz7n8CmOSK6kw-WBDnmEoF_TVGWujpNQ3tSCSD42xluBL8KtmqHyGo64ajdJMNiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوج حقارت ارتش
ایران
به روایت تصویر:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65045" target="_blank">📅 10:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65044">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: توافقی برای پایان دادن به جنگ علیه جمهوری اسلامی ممکن است «امروز» حاصل شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65044" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65043">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام: اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.  پیوستن…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65043" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65042">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tcr6Dvj2pG9zNvFYYvkqbeffRhL72uyDXzr2zlP7i8ymVvyWgBMSJNAZmCUp6tT_-7L9sjZNvulbN5SK_8Zlv5AaxYy76tc2PX8diQy9zJVWESornvtOZDjFhet9aW9fxMrtSLmqBK2vi27KJV1f03M3Rc5VFZsWGkelUDhALINMcOq5MifFY3DVVAz1PebhcOxS9ikrJEEtCusUdyx2y_jGCGp4-szHmzjDzuwDt7uhl65ROwnfqGlajDhj4QSfa269lt_Y-AjcCYwiM9WsY_sCetiRR_jMV9z7wrVMpCPMJpXjffzd1xyuF0jJYeeAL7ONtuPD2pjU8BHDTFYm5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.
پیوستن عربستان سعودی، قطر و پاکستان به توافق‌نامه‌های ابراهیم فراتر از تحول‌آفرین برای منطقه و جهان خواهد بود. این یک حرکت درخشان از سوی رئیس‌جمهور ترامپ است.
به عربستان سعودی و دیگران: اکنون زمان جسارت برای آینده‌ای جدید در خاورمیانه است. من انتظار دارم، همان‌طور که رئیس‌جمهور ترامپ پیشنهاد کرده است، شما در واقع به توافق‌نامه‌های ابراهیم بپیوندید و به طور موثر درگیری عرب-اسرائیلی را پایان دهید. اگر از رفتن به این مسیر که توسط رئیس‌جمهور ترامپ پیشنهاد شده است خودداری کنید، این موضوع عواقب شدیدی برای روابط آینده ما خواهد داشت و این پیشنهاد صلح را غیرقابل قبول می‌کند. علاوه بر این، این موضوع توسط تاریخ به عنوان یک محاسبه‌گری بزرگ دیده خواهد شد.
رئیس‌جمهور ترامپ: در گرفتن یک معامله خوب با ایران بر موضع خود بایستید. به همان اندازه مهم است که بر موضع خود در اصرار بر پیوستن عربستان سعودی و دیگران به توافق‌نامه‌های ابراهیم به عنوان بخشی از این مذاکرات بایستید.
دوباره، این یک پیشنهاد درخشان از سوی رئیس‌جمهور ترامپ است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65042" target="_blank">📅 00:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65041">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آیا دونالد ترامپ، باراک حسین اوبامای دوم خواهد شد و دستور آزادسازی ۲۵میلیارد دلارِ جمهوری اسلامی را می‌دهد یا خیر؟!  بزودی خواهیم دید! @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65041" target="_blank">📅 22:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65040">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc9iLnLDeFBpz-tq3_539wXJh2E5Cnxw_9c4jZo7r4J--mQ2iMo-Zw_oM46VO1xm1yq3IpGTmtoRSN7loUkNKrUE9p0JRKccLuKFV1SklKqMeWinJpVNzXpftcpgQ10GSTB618NJKZlRVGRw9DTIeToTbY2W805s04e4jKynLA0rIx4wKZ8y70iianC19uZkgRFHI0QWV1MpECU8TEp9Rgdf8ZPG_2AZrGwMAUJIBeUtLAgx7H1QjEyh8UqYd2_7WBPRT32iy9yR2It-hhYPWxom_ioK82zI0AF3knCALB4xCV1V1QFiBB9gL89fAdkGnMpUpkPXkjkLyRUJH-LgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65040" target="_blank">📅 22:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65039">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llnfJnbaqD5259QIMsh637Df3iRGFU762QIlIkWvibXjx3EibY5Gl9GyC-HjP6SfOzqfMkhrZHDuUgmTj8qXGDlVdfG1AtUkQCQY212_Kt4LPjXVvypcKfzwVY80i2RyQXl0MtwyQ0FU8704LVTzCWxTjO199T2-K5D-lSya8Bm2NztA6Ims0sG34qz3NOP-zHdI5ndczHeZO6WQoOv7MGZ8rrBY95qhpfvtfHGfzFoQnz5LLoSccABYC4lryMkgLV9QABgRvcS_Nezy9SSx6g4VJRSGCqOHBWppC5sqqWvVCAeFG2JbSNiTaTa9074ovFngGTPMGLkmbbA74E-4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز حتی به طور کامل مذاکره نشده است.
بنابراین به بازندگان گوش ندهید که از چیزی که هیچ چیز در مورد آن نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بدی انجام نمی‌دهم
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65039" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65038">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو: توافق نهایی با ایران به معنای برچیدن تأسیسات غنی‌سازی هسته‌ای و حذف مواد هسته‌ای غنی‌شده است. من و رئیس جمهور ترامپ توافق کردیم که هرگونه توافق نهایی با ایران باید خطر هسته‌ای را از بین ببرد. این به معنای برچیدن سایت‌های غنی‌سازی هسته‌ای ایران…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65038" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65037">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: من معامله بد انجام نمی‌دهم؛ در مورد جزئیات توافق فعلا حرف نمی‌زنم، صحبت های خوبی در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65037" target="_blank">📅 17:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65036">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تنها چیزی که ترامپ تغییر داد رژیم غذایی مردم ایران بود
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65036" target="_blank">📅 15:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65035">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=X6meh0UEBwvCKqv7HFDHe-kIpvYLBxaf0sZAmzNdK4wdB0beRsoOwExWa8rNJwkrRV-N4GCgBEzxD9XPj0_xwGrFpPtcxF0hNSXRbDzmbykobcHGXIoaRd5Cmazs_hxc3mEfIGtpHJDFp2FPeYyx6xcQuldzLWjAYVMkf3lVZApIyrKFDV-nsUbCnTf3Ef-ntSC98iGY2N2FkwHPdHUSXvFlhXzQLL2ZaLpZjOYJtL-zWw3nbD6CEDfwVLevNC2tCayy4QPjHoJWYmY4c9IWhqLTK44uaP4il2EMw4Y287lFTWH9oJUg4qW_2m1xF2bBuGMCXMvgOWU1ObaM5DDM6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=X6meh0UEBwvCKqv7HFDHe-kIpvYLBxaf0sZAmzNdK4wdB0beRsoOwExWa8rNJwkrRV-N4GCgBEzxD9XPj0_xwGrFpPtcxF0hNSXRbDzmbykobcHGXIoaRd5Cmazs_hxc3mEfIGtpHJDFp2FPeYyx6xcQuldzLWjAYVMkf3lVZApIyrKFDV-nsUbCnTf3Ef-ntSC98iGY2N2FkwHPdHUSXvFlhXzQLL2ZaLpZjOYJtL-zWw3nbD6CEDfwVLevNC2tCayy4QPjHoJWYmY4c9IWhqLTK44uaP4il2EMw4Y287lFTWH9oJUg4qW_2m1xF2bBuGMCXMvgOWU1ObaM5DDM6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65035" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65034">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxAzalLT88lesOljj4tRTQ3qcVSqzHbfFnO10t9I7Spd0bqGPxI3tMZ6XDwzLC5e_YfJcoKntSLAojlPG4vxTn5CyH-lZYmY5p_-noWZdyUw8uPkW9zdJPAYTF2JQ8sT0GyXtkbgv9w_Vy37tf2Jt1xNQdC60qwtdbQPmu6pt-iTqtfbsRhslFVGHvb90KhpIa6CX_DlAVAL-k5uWFAblWxF3anEEuAjjvIPAaPx2_j-fpNljLfqBg9QC3o0VyslBoPa6qIwCae2XMBmd4AHsRSNnRDvpIREDs68tkXPbmNhbO4Gn8FBB6h1ldeU6LSpjkFDIS7SJUieIRyrolgKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجایند مردان بی‌ادعا؟
🗿
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65034" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65033">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مراد ویسی: سپاه می‌خواد روحانی، احمدی‌نژاد و پزشکیان رو ترور کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65033" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65032">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GrCg6w5XU5rCMkAHzcwILQs4x25Vw9vTGgm5ka0WwMSwnw5efiXN7vEYHkxEg_QUJn5zAYycCoD1Vz1eCtkdgUEcL0e_0XTrwwJunrVfuNYBs96sO_65PihrJOUfZaH6jgwdNlgFaWCzuEPfh53IgsWW5NihSocqFe8CluJpADAv3v2gXnn6_KLnfVMwJSD_dolUEZlFax0DMsnn-HK2n-MnPRKM_iwqAWbCo-J-XT9jECLtBvEbporB_sN8Thc1n-K3WB3f5MPXRtOXzAIin5m5nKAMbJGdfAO_th3oHVdEaR_Dv8bZH42MrwOFeW98-HZRt0n0_iKtoutYa7BkSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار تتر بعد از اخبار دیشب درمورد توافق تا زیر 170 هزارتومان ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65032" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65031">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
آکسیوس: توافق بین دو طرف امضا شد.
👎
این خبر فیکه و آکسیوس و خبرنگاراش همچین خبری نزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65031" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65030">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=aBUT1r0rO0hrXZnRA3MF46T7dO7rjvQUWIkq3BfJolDsXo5387aMND7V7hgDqgCNNnOaC53R7MLImZChcuGzmHMxv5yJz-tSugGuESfO8_kVgTL4_9Ne7oc7pKgztFS5pX6wLh2J63avCnLQnSLKOtyJmrxVZdqjwh5vKpXpOlchLyqBXZ226taCiJslZf7btm9ui0BPrRsamzwmmXzIxzY-JrN5KNGn9h-hiEVs41l12qGTnKwNoebd_FGV-2bR9gVPzX1ZHc2HwEhVcGafX2kusSUPsyELSQUbHKHFAzd13ewTP8n3wOVa8W7LlkYc6HVbypp8eCDqViJvfd9LYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=aBUT1r0rO0hrXZnRA3MF46T7dO7rjvQUWIkq3BfJolDsXo5387aMND7V7hgDqgCNNnOaC53R7MLImZChcuGzmHMxv5yJz-tSugGuESfO8_kVgTL4_9Ne7oc7pKgztFS5pX6wLh2J63avCnLQnSLKOtyJmrxVZdqjwh5vKpXpOlchLyqBXZ226taCiJslZf7btm9ui0BPrRsamzwmmXzIxzY-JrN5KNGn9h-hiEVs41l12qGTnKwNoebd_FGV-2bR9gVPzX1ZHc2HwEhVcGafX2kusSUPsyELSQUbHKHFAzd13ewTP8n3wOVa8W7LlkYc6HVbypp8eCDqViJvfd9LYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65030" target="_blank">📅 00:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65029">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=Nc8JuMHltSVOFn_GFg8VBKJYk7-4I0Ny-D6dFheYbyvZV0WYpLWvw2Z_OqNA9rROsx5rs29QowhhWIr-zLrnB80VtoB2VhjvQsObDPKs1uoAt3WbYoEx6FaIjvweb88IzUnYgnOYHvQWqaEG8PuscBnA22zEBillOU1XJzgIhVpZQUBOYceVlEbxB3I1LIjn0oKbQVigYHN1ig15UIAnz8i2Sv_JD-hRbLxirjY6J6hplfGoUvB2nkq4NfK9tP1s_vK82ty0qdJEdhjKoSSVCAq8FampC02sshkXHSO4wgMDEPZbjv1_QYBVyQNtH7Ndo7OkFD1ztBxfS8O5nD7gfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=Nc8JuMHltSVOFn_GFg8VBKJYk7-4I0Ny-D6dFheYbyvZV0WYpLWvw2Z_OqNA9rROsx5rs29QowhhWIr-zLrnB80VtoB2VhjvQsObDPKs1uoAt3WbYoEx6FaIjvweb88IzUnYgnOYHvQWqaEG8PuscBnA22zEBillOU1XJzgIhVpZQUBOYceVlEbxB3I1LIjn0oKbQVigYHN1ig15UIAnz8i2Sv_JD-hRbLxirjY6J6hplfGoUvB2nkq4NfK9tP1s_vK82ty0qdJEdhjKoSSVCAq8FampC02sshkXHSO4wgMDEPZbjv1_QYBVyQNtH7Ndo7OkFD1ztBxfS8O5nD7gfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65029" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65028">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65028" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65027">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W13huR393y7SUYnyyIrLLZKsufOQjwDJyp99jJu-fMAGY0qg-2pbF9rrurlSjLSnLaWWhBy2NCgr9gHdVAlmnhBu7rZCN2HSh_NLVJrizyhA1UV_X3OAmpkf1440b1ODLRM498zVK4q_Jhb4YT7SaR8xcJrEvrbAsakn7m1Sqz9nf5DySnhiaFePnjQyuArOx8hyhGx_dFwYCnGuT7zpUhdhaDpHpKKl9TYDFYXh6kXAB--nP6YHiIKuwuZjOh90Ic6jZmZkQgeDURnnl9TI8lbS0i8WL3o2v8QG992qn8RhE79A8ppl-6x9ASKX8cQ95BIyYjNGn1U6RAuCIQuq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ:
من در اتاق بیضی کاخ سفید هستم، جایی که همین حالا تماس بسیار خوبی با پادشاه محمد بن سلمان آل سعود، عربستان سعودی، محمد بن زاید آل نهیان، امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی، و وزیر علی الثعادی، قطر، مارشال فیلد سید عاصم منیر احمد شاه، پاکستان، رئیس‌جمهور رجب طیب اردوغان، ترکیه، رئیس‌جمهور عبدالفتاح السیسی، مصر، پادشاه عبدالله دوم، اردن، و پادشاه حمد بن عیسی آل خلیفه، بحرین، در مورد جمهوری اسلامی ایران و تمام موارد مرتبط با یک تفاهم‌نامه مربوط به صلح، برقرار شد. توافق‌نامه‌ای به طور کلی مذاکره شده است، مشروط به نهایی‌سازی بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همان‌طور که در بالا ذکر شد. جداگانه، من با نخست‌وزیر بیبنتانی، اسرائیل، تماسی داشتم که به همان ترتیب بسیار خوب پیش رفت. جنبه‌های نهایی و جزئیات توافق‌نامه در حال حاضر در حال بحث هستند و به زودی اعلام خواهند شد. علاوه بر بسیاری از عناصر دیگر توافق‌نامه، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65027" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65026">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">بله  مگه چیه ما با ۹۰ هزار ... گواهینامه مون گرفتیم</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65026" target="_blank">📅 23:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65025">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گواهینامه شده ۱۵ میلیون تومن!!!!
الان یکی میاد می‌گه حاجی ما با ۵۰ تومن گواهینامه گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65025" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65024">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بستن تنگه‌ی هرمز در جنگی که ۹ اسفند آغاز شد، تمامِ معادلات آمریکایی هارو بهم ریخت، اون‌ها حتی چند روز قبل مین‌روب های خودشون رو هم از منطقه خارج کرده بودند! دومین مسئله‌ی شوکه کننده برای اون‌ها حملات وحشیانه به کشور های عربی بود  هر زمان آمریکا_اسرائیل به…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65024" target="_blank">📅 22:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65023">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65023" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65022">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم می‌گیره، یا از خواسته هاش عقب نشینی می‌کنه و یا اینکه دوباره جنگی برای اعلام پیروزی شکل می‌گیره، تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65022" target="_blank">📅 22:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65021">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65021" target="_blank">📅 19:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65020">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65020" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65019">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
📰
ترامپ در گفت‌وگو با آکسیوس:  در حال حاضر احتمال کاملا 50 / 50 است که یا با ایران به توافق برسیم یا دوباره جنگ از سر گرفته شود. یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم + ترامپ شنبه با…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65019" target="_blank">📅 19:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65018">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
فایننشال تایمز: ایران و امریکا به یک توافق آتش‌بس ۶۰ روزه نزدیک شدند!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65018" target="_blank">📅 19:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65017">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
📰
#مهم؛ فایننشال تایمز: میانجی‌ها معتقدند که به توافقی برای تمدید آتش‌بس به مدت ۶۰ روز نزدیک شده‌اند.  این پیشنهاد شامل: بازگشایی تدریجی تنگه هرمز گفتگو درباره رقیق‌سازی یا انتقال ذخایر اورانیوم غنی‌شده بسیار ایران کاهش محاصره آمریکا بر بنادر ایران رفع تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65017" target="_blank">📅 19:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65016">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZovSd6iJzFLQ4K453xAavVokhJtO0eGoy1YzKlFKK686T77_lI5fWwAjtSXpG50dC8l1Gi630arpvdwD48bzMuIuIU3mKZtjIROiSSm-6pLF2FSQbpKzPMkBRzW6FRVhPJ2gUF5tS4Q9N7S3lfPFAapRrPcrcPsa0KlcOcOMCK26kOgxIWEVekeJgRj2eoeWl4_DyqFuDNi4HhlsxXZ2Eb2aNGYv4BFFq8JkWrHX_rARcAWFxPhFrWlVgoygoZRHzIuWelz7Zkyg4ozjcceRh4nbpKfXAge8g9Kj2YXpiWZ-bwG5Sm_TAVmmqv3ZF-eW4wXfy5jsEdZn76hrr4r5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ تو تروث‌سوشال: ایالات متحده خاورمیانه!! با پرچم امریکا روی نقشه ایران
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65016" target="_blank">📅 18:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ مارکو روبیو: ممکنه امریکا به زودی خبری در مورد ایران منتشر کنه شاید هم نکنه امیدوارم این اتفاق بیفته
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65015" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=TusfZciDBhh-VPlW5BQykKiFvB_UKz1Hi2h-ZgLKwu6b7xBBWbXiabxJTvufBr2jO0A3utz1vs-lR37SFp25ovxRtoXvD8vT8fzwzhDa2gE1ay3Nl0PNFWPI4A8cn2ZzF7fQsGuWwU0abbdM3RaVVah6oKiKM2Uq4XQYjdnsKJrfm9xU5vUm75nZtqEEXheJRfap6BlQho5jof0eP-FJ5xL1jSXBkIyKiraIW0o1iAa6ZBA0hQAklTdpYmagzBD4F9GfRxrLt5rJqYeRn1BUCgWpmzrDfQHmvnlgiq-p54OZdpuql-1Vd66cVPCvyvTZjMX2dRVsjKD3pfLuYvqYrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=TusfZciDBhh-VPlW5BQykKiFvB_UKz1Hi2h-ZgLKwu6b7xBBWbXiabxJTvufBr2jO0A3utz1vs-lR37SFp25ovxRtoXvD8vT8fzwzhDa2gE1ay3Nl0PNFWPI4A8cn2ZzF7fQsGuWwU0abbdM3RaVVah6oKiKM2Uq4XQYjdnsKJrfm9xU5vUm75nZtqEEXheJRfap6BlQho5jof0eP-FJ5xL1jSXBkIyKiraIW0o1iAa6ZBA0hQAklTdpYmagzBD4F9GfRxrLt5rJqYeRn1BUCgWpmzrDfQHmvnlgiq-p54OZdpuql-1Vd66cVPCvyvTZjMX2dRVsjKD3pfLuYvqYrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقائی، سخنگو وزارت خارجه:
ما هم بسیار دور و هم بسیار نزدیک به یک توافق هستیم.
دیدگاه‌ها به هم نزدیک‌تر شده‌اند، اما نه به حد یک توافق — بلکه به حدی که ممکن است بتوانیم به راه‌حلی برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65014" target="_blank">📅 17:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65013">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73653df566.mp4?token=CKRsS57yjBOmm8JepRIA-bf163CdFeatABGql2eLd5VbcFGn-GaaG1tn5nTWMRiSuXVq3dYd6KRHoVcwCZb-3pARRP_6pQMyuGoyUHxDWEiHZzjQuydykCXYrmamjSwIaYOU_u67Fo9W8W9rKoTcEt36z-zKGCx6096MaxXDVrQtQNOLuO2EDd6YWPGhaJxhgNTGU7iKAi2qew6ooRzCa_D9fouW6o5K1KqDgEUkxljGtdoBkXR6RMt_ZSvJ8WC7QJ47UyNkHQDR0XSMnuXvz8VlX2M7sXWDJe7z5kapNX-hHu8Oq4vgG22vju3Tp_ZAYGQQHalyQzYHCK9WduMZ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73653df566.mp4?token=CKRsS57yjBOmm8JepRIA-bf163CdFeatABGql2eLd5VbcFGn-GaaG1tn5nTWMRiSuXVq3dYd6KRHoVcwCZb-3pARRP_6pQMyuGoyUHxDWEiHZzjQuydykCXYrmamjSwIaYOU_u67Fo9W8W9rKoTcEt36z-zKGCx6096MaxXDVrQtQNOLuO2EDd6YWPGhaJxhgNTGU7iKAi2qew6ooRzCa_D9fouW6o5K1KqDgEUkxljGtdoBkXR6RMt_ZSvJ8WC7QJ47UyNkHQDR0XSMnuXvz8VlX2M7sXWDJe7z5kapNX-hHu8Oq4vgG22vju3Tp_ZAYGQQHalyQzYHCK9WduMZ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توئیتر اکانت ترامپ که با هوش مصنوعی به ویدئو درست کرده از مجری سی‌بی‌اس که مخالف خودشه و ترامپ میندازدش تو سطل زباله :/
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65013" target="_blank">📅 15:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65012">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PHbuI9JDYr3aL2oEUUcAbX0a8KdETtFYpOUc8AOVRHke4TIWbYqDcR0aSueslQmHAKgfxu4lCcKNaAVWY0xHtNB7g2joqN0PMUgt8rt4GnKoP3NrUjj3NLYWhslDOAVOcU0D5op9y8e3E9D3OWsBGBVBQB_HnT1i3AJij9fQ0f81ke8ZUf6ZdDRxeR_cVvm_uopbcGCQUtW3h5UAtwWtgnRPTHB0e7qDmLBKCy6ZHr-pIDjR91OvxJ2w8DSgAKdpZC2887S-_Kiul1VmxNCqEUvDgdtdyGmKujqSpsHKEEwZPVybAvBT7Ljw8Gk_ugHArhg5fHYQtXYxi0I_CVYTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عروسی پسرش بود نرفته، آخر هفته برنامه گلف داشت که کنسل کرده و تو کاخ سفید مونده حالا خبرگزاری‌ها شدن دو دسته یه دسته میگن توافق نزدیکه حتی متن توافق منتشر میکنن یه دسته متن توافق بقیه رو تکذیب می‌کنن و میگن کلا حتی نزدیک توافق هم نیستن دو طرف.  این وضعیت…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65012" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65010">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aIQjRmHnMqg-rbgaXU3bPN3VY74DynsDULN_1hT68OWfpLnybKzRxoIU3cuJPDvdbZYdNdFU-XaxgDFxfuWVcd2dskRJZU8UrgSMwWzZURVpOyLZ297SpLLyKM1szpCx2kyyXMGcaVh8Y_Gt-DKRTJhJ32LWnSSTuOGg__a1KNkFEKuuttkodX-ek9dGo3EFEwzvQ3AtC95XiI-WyHc6dK9-dw7dQEZ6zWylf673bImIDps-aPDiUy5PyrpcJEsXDFW7VOCniDgUNMyWen9EC3ZGzkFRSHogRJUKP7KvsNY34F9ao6IYqMmn3MwcWQ1xqvBfZNGrw8ZEjaPDAiqvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=ZFJtxpRGbkrqkgzuz3K_VdVEPdcBfiWucxmKif_LXnAkc652SZo0v0bA9feDg76u7HX0An6ifbSUyzTIlFQ7fO_rLa5pyXrPDTeaOgr6PIrLPC3paUcFe3AVN26H04FIP4dVYuadgWwrI3RsUSwriqvDCIJ_JR0DnNFCqsiebqQodzedVSFSAZUly2rkdIJ0ZHIXH8BS22tbuZaI1jXmVTAEacpM5SJi0DEOwbzO7HXIXg77x50AQY9nU_O6RnOAlU56eAlnuwoQh8_YFYlhbNXlAAFo-b0_-LUALtfzaWihTG2rzUfLKGsIR4ftUdy0z-3hOFLxk7_BurmoyPBD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=ZFJtxpRGbkrqkgzuz3K_VdVEPdcBfiWucxmKif_LXnAkc652SZo0v0bA9feDg76u7HX0An6ifbSUyzTIlFQ7fO_rLa5pyXrPDTeaOgr6PIrLPC3paUcFe3AVN26H04FIP4dVYuadgWwrI3RsUSwriqvDCIJ_JR0DnNFCqsiebqQodzedVSFSAZUly2rkdIJ0ZHIXH8BS22tbuZaI1jXmVTAEacpM5SJi0DEOwbzO7HXIXg77x50AQY9nU_O6RnOAlU56eAlnuwoQh8_YFYlhbNXlAAFo-b0_-LUALtfzaWihTG2rzUfLKGsIR4ftUdy0z-3hOFLxk7_BurmoyPBD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی از برنامه جدیدش به نام مای دات رو نمایی کرد و برای تبلیغات نوشت:
اینستاگرام پولی میشه ولی برنامه ما رایگانه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65010" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65009">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65009" target="_blank">📅 03:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65008">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65008" target="_blank">📅 01:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65007">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">واقعاً خوشبحال جمهوری اسلامی که با چنین اپوزیسیون احمقی طرفه، نه تنها پادشاهی خواهان با [به اصطلاح] دموکراسی خواهان دائما درگیر هستند، حالا خبر رسیده که علی کریمی و شاهین نجفی از داخل گروه پادشاهی‌خواهان هم باهم بشدت درگیر شدند
!
شما با این وضعین می‌خواین در مقابل آخوند بجنگید؟ جای تاسف داره واقعاً، حیف مردمی که گوش به پست و توییت های شما بودند و هستند!
#hjAly</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65007" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65006">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=UYmbpL5hR-9NYZmIGZex7kFGbhPsT73HZu5K22Md1ZeynY_bAPuMscSgCXpeMIeGOp-SU7jyCf6AfFUhCA8uhH-u5UMjhetIt-ZRw_Spf7-7IMGn6QnaToWezyHN7YAbVPjmYhZ_T3wY6fSh3HUiPszNaenUYN_sylqr1q7hxphk6Az_4T_pLJgQouxoAoiqzmFHKrX9gej00NFi0Q7qoLuXMxoM4I7Oy-RthFwOrAqy0EzXAHjqLZ3U7XbAOTbqZixuCdMej0i9Lz6bN7SB_ii0sk7-hv_CP6G7O51spT4GdGwrj2J6rQ-1QulvfnqpIOztW3uUY4E6erfLccZlFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=UYmbpL5hR-9NYZmIGZex7kFGbhPsT73HZu5K22Md1ZeynY_bAPuMscSgCXpeMIeGOp-SU7jyCf6AfFUhCA8uhH-u5UMjhetIt-ZRw_Spf7-7IMGn6QnaToWezyHN7YAbVPjmYhZ_T3wY6fSh3HUiPszNaenUYN_sylqr1q7hxphk6Az_4T_pLJgQouxoAoiqzmFHKrX9gej00NFi0Q7qoLuXMxoM4I7Oy-RthFwOrAqy0EzXAHjqLZ3U7XbAOTbqZixuCdMej0i9Lz6bN7SB_ii0sk7-hv_CP6G7O51spT4GdGwrj2J6rQ-1QulvfnqpIOztW3uUY4E6erfLccZlFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امتحانات نهایی پایه یازدهم و دوازدهم تو بازه ۱۵ تا ۲۰ تیر به‌صورت حضوری برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65006" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65005">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65005" target="_blank">📅 21:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65004">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
العربی‌الجدید: سفر عاصم منیر به تهران دلیلی بر توافق نیست و پیام جدیدی منتقل نکرده است، گزارش‌ها درمورد مفاد توافق گمانه‌زنی است و اختلاف بین طرفین هنوز زیاد است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65004" target="_blank">📅 21:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
📰
العربی‌الجدید به نقل از یک منبع نزدیک به مذاکرات:  سفر فرمانده ارتش پاکستان، عاصم منیر، به تهران به معنای این نیست که توافق در دسترس است. گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و صرفاً گمانه‌زنی‌های رسانه‌ای است. وزیر کشور پاکستان پیام جدیدی…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65003" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65002">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
📰
العربیه: طبق منابع العربیه، انتظار می‌رود پیش‌نویس نهایی یک توافق احتمالی میان ایالات متحده و ایران که توسط پاکستان میانجی‌گری شده است. که ممکن است ظرف چند ساعت اعلام شود.  شرایط کلیدی آن عبارتند از: آتش‌بس فوری، جامع و بدون قید و شرط در تمام جبهه‌ها، از…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65002" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65001">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرگزاری های حکومتی: عاصم منیر وارد تهران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65001" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65000">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=og0m3CG81ndmP5Q0ewnyKQwa-C6OhfcvAzIY6rVOy_JiGaxnNPFpMjIkH_EO3peLiFlhymxmsjHR2AsngIF0y4HtV919QgIL5uuIA9EGNbFZxHsFarftyjqGPZiopOQiGace_GGWCSHlGkBIxuHR7MQm8KLz582CP2WpgCUzkBL1mlMi_haaD4lv3uR4hNM6P9BfzKGNcb6NwAlo9oMhB33J40XdKb4Iperwi2JavOo4d_csYQ00pJhhcKKri11Q7WF4EoOLZ01bc5Uuz2Iyl8su1Jpl-n3WUpeB2W-o_Mogl5e0GUmh6Zhs3sNRhSFRjNxDNQYYIw29Dbt2Ie-bqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=og0m3CG81ndmP5Q0ewnyKQwa-C6OhfcvAzIY6rVOy_JiGaxnNPFpMjIkH_EO3peLiFlhymxmsjHR2AsngIF0y4HtV919QgIL5uuIA9EGNbFZxHsFarftyjqGPZiopOQiGace_GGWCSHlGkBIxuHR7MQm8KLz582CP2WpgCUzkBL1mlMi_haaD4lv3uR4hNM6P9BfzKGNcb6NwAlo9oMhB33J40XdKb4Iperwi2JavOo4d_csYQ00pJhhcKKri11Q7WF4EoOLZ01bc5Uuz2Iyl8su1Jpl-n3WUpeB2W-o_Mogl5e0GUmh6Zhs3sNRhSFRjNxDNQYYIw29Dbt2Ie-bqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ما باید شروع کنیم به فکر کردن درباره کاری که اگر چند هفته دیگر ایران تصمیم بگیرد، «ما اهمیتی نمی‌دهیم؛ ما تنگه‌ها را بسته نگه می‌داریم؛ هر کشتی که به ما گوش ندهد یا به ما پول ندهد را غرق می‌کنیم» چه باید بکنیم — آن وقت کسی باید کاری در این باره انجام دهد.
امروز این نکته را مطرح کردم؛ خیلی‌ها سر تکان دادند؛ خیلی‌ها بعد از آن نزد من آمدند و آن را تأیید کردند، اما امروز خبری برای شما نداریم که چیزی در حال وقوع باشد.
باید پلن B داشته باشیم برای اینکه اگر کسی شروع به تیراندازی کرد و چطور تنگه‌ها را باز کنیم، و من امروز این نکته را مطرح کردم. نمی‌دانم که آیا این لزوماً مأموریت ناتو خواهد بود، اما قطعاً کشورهایی از ناتو می‌توانند در آن مشارکت کنند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65000" target="_blank">📅 18:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64999">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/news_hut/64999" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64998">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQJXjvByXqgcXUKSC6e4kEAStlM7nKBDrDRPVuGfDy4oh3FgmMzJqr4YayS53XgcX_xZg7VpsKcr5aPqRF_kbiqOgOYIRIrOjemr9VI4IhoaGJYfmUaA5hRq1bxOBzfGnIxBPRnd3vd_Y4wY-UQUQZ_CyhzawdNAndg6jl9r-3UvjeVSN-cOk7XsjROyaVEvp_OkTBQtgV6gp03a27YdJHLjnO78JkRL7V4Gqj1qqx53isXV8e6fnv9okDZ4ez5BlyYldm-bHMqGEYlpMtBlCM-Eksn0r7K2N7XJc0Q2am8mfOptmvFlAuMgv72faXb9CU3NYtANUt3_yQU4MnbPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
لارنس نورمن، خبرنگار وال استریت ژورنال: یه منبع میگه هر چیزی درباره پیش‌نویس توافقی که داره می‌چرخه، دروغه و صحت نداره!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64998" target="_blank">📅 18:07 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

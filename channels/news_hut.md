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
<p>@news_hut • 👥 134K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac4qn0pELJ8gqbzrPKvfcYROVr_LQiVlXJYBdZri25Z2coHHQahz7Tus-SnHnfPtrQ-TKmVNZDzTi2ffPeQHEXuTjK6E-ECSw0dc8wGfHetJHolVDqFgGRWai2rHVqmZKsXj-C_TH51ymKzLNWOgoieGQZqqOejR12wXnMs5C02WmecFvbe_VWStSzpoYJfO_t6cuUmbSrl_wivVt6t1P0QwWiBYuN5J83pcVcn4Kib_Vx354qeDJR2KxinSVhy4Lab8RLYzYd7Xp8yKFnMqx2WR9tP-zGsh_yuBlTuqnzAughAGjH-9ogiSCJ8iG47yu7ouge37seVPAiBIk5aaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyUczIRYFleyZXcvCDsPz8azRDNiSHgG-TPa6YerZa4zo-SraB79N5zEtOgCtfzSx1D3aTVtrjyas4y1OUAxZs_ZjmDxE1DbI41V_Mn4tv00B4-FCqF4Mq2Yp7uW_fflbbQiBoH8yDZ_DK99ceiA0AhNhTXJF-Kode5L3R17iCQ9kK7p-MN8WV1GrHBnOJgZkqMcbtv9glVI-kfYEV-9xMZsqr3yGWqvv4I8u1RIs0Am6gckToPrP47pnFXqJ-igbRXkQNhh_vIxAISPiF1Uy83iULkn5lUNMJa5EUR5oluoMI7Zbd2m_1twT1xr_mb92hdOA7aY6SHucAFdWpEl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTrsRvfu0L9VJt5PijU_M-VTCQaOlNHp3_UVFXreWBy6uvR9nVZYq1_eqVsOg-6ICbzaP10ae7uXli8xM_ZyS7eB51kKYZpdPbk56tOAfwlx04TqUIuIh_sGbo6zIreTch5IttY9uzogRrOa8Ds7o1WhaVgBT3bO_1uABk0jtHM-Vu5GKq3qVC89d6BxXu3EWKHq1XOjJf4kvtEhSQfYHWui8Ccnrzka2LWdmj78Q-IrQnFYLICQAkCzuudrU8f4knTVqIuhaQXeXeJhCnADXeaQ2Rt1Mkk-CjeVNJXZ2iwyNmXPg_zGP6GHechBdArareCHnKwPepeojzSM7GNdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZCHVG0CUM80XnMsmzr62tYXmRBBmDcsZ_YCl5oukanKiHM2MBUQOIxTqD0Qv-3zTKTaBxzGuYu2F7L4xErhWtyCt-utYX4MySF6kTVIu2VQUEfPzYtCwDubOGzh3Lub0ph_X8vpw1ZzO0zWurSkKlelQoYHZIwCK22eVDodzpdsELo8jpDDBrGPrvm8QV0Yf-l2Gd_kfm-gqSNlINAK3z30vKbuoNb6dHwFUi1x8t3WONY003fWX0wZZNUylTvzQ5418SzHIXKyImrmt6odvhaWIVluQ5kXRg58RCQz4DCqRcTwMTUSvYJOYWpKqoUlx1L6c7XTLPCWjVBtR4Qhkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvCx02mt9QBEFMmtPk-GXb1okZgrPXIsGZ3_rRsCgAnIpzO3TCckafD8QPKu2A13gwewiWhHYDjpxQCR8jFGVbwAAuYCgCbjU-ZkmpY7lwoQgyfAONyV0jRNXecX84bol8hMGuA6-WsLc2zaw_SHGgCPmjo1n0QkP1azMktsJ-5bi1sJJkopauPf1ZOoe2R13FVWEDokg5huOzL_Z8VzpXX726fAG1XBJTzS720Vp7Byokt8wySq71vDF2RN7eADL8FnEGmjrWrnddP1BjCTl2xKp8m4PmaTr_qOD5UBK9FZDovX16dPOMD5DWzyjrnCAZE2B_vSbQtOkwsRNPncIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65087">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-text">Barko VPN_v2.0.apk</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65087" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65086">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65086" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=kiHdxOkzqkYwChHs--SOuNSGXFG_SGajGfsTNAIADbMUC_gomG92TMl2O1bKx7bXjMjg9rWwCdTFnx3fWZNCghZ6P3kY85c6vfqIuR32wMh9cMUL2qwpwAAXBpLDFT3cAZ5mdXqnVJVUlSZVxuqHROeuCq5usvLl8kR5X-_Hd1Pso8MBuWsQzPog6lYqUFzYZkB2KjexpgSqPuyiMdXDK4CKEX5k7vzcZQ0_8oRpUMvIdD5m5qLJ3UgHiAYK2eZc9gOAnju52MqvE3n6Xsqwc9cf4uu1ldJRrKmL_gyXLGEZLTLliLYJFNsi8pmlVl3uYFe4RBLxDabE52VV4jqqAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=kiHdxOkzqkYwChHs--SOuNSGXFG_SGajGfsTNAIADbMUC_gomG92TMl2O1bKx7bXjMjg9rWwCdTFnx3fWZNCghZ6P3kY85c6vfqIuR32wMh9cMUL2qwpwAAXBpLDFT3cAZ5mdXqnVJVUlSZVxuqHROeuCq5usvLl8kR5X-_Hd1Pso8MBuWsQzPog6lYqUFzYZkB2KjexpgSqPuyiMdXDK4CKEX5k7vzcZQ0_8oRpUMvIdD5m5qLJ3UgHiAYK2eZc9gOAnju52MqvE3n6Xsqwc9cf4uu1ldJRrKmL_gyXLGEZLTLliLYJFNsi8pmlVl3uYFe4RBLxDabE52VV4jqqAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJ1as71sCs1Di6eyzPLZ0oka00GkADz_b46tfIGmfJuctDuHaOEuN1GnN_0TuQhWCt7twN8O1WvjxEFAHGOv-FqxNTOqm4QXQObWo3vtMvJP9sTVPu1WCouFqwuvyk-Quyn1C7cyIET_aYhDwNi7rJTtqVNoyG51we3ropLBJ2oWi02EfO4oCoysvpsEa46Y0ZnN48LsgIURE7aMstxIkIKD3bfxvm_aT61ZX2vVBragbosxzSJOXoVfPauIU0Ihi-gbKlrMGAtwzMh4I9DbSL2JnjS1dzuDZI41MbeItgfjmTQz_9GfkJWqlc9UihfsGgVWOOMniQHKMfejaw6vtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65079">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7BckE9RXrVDJ6oJi6Xn-gfTBNlLTnuxvrc2MWIxmvtBMttAZQz7nDlPC0fblbyiHd4cf322QhidvbGXMcLd16mxugPn8IwbunguV7kfaCR50KVqK-Ju_R0jD_8dW1ua985zJ9xNjGZtA-KfFBnyMfNoke8LxhwU8O_axrhxGfyD9e2dq8syRfIGu4j6BtxGVu6g3UH48P2tCuVlDmARs4I-jdMge4HhdVrSLiQi4QC7B5gyaeGZZxWnylKBzX4K3v-6517VjBVCMtw4BUa8u3hI7pfq3W2MJPkBEjv-wmcVB_KskJkca8i-HJ7iJu8viroUuqGSta1U2FmFJ8dZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65076">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOEWw1Gs8EVaRd3ACoItPevE6e8fK_UOyqpSKRnx7aijexA3DFCzkpvGfKAnTDevkxa9V5ZylD4tlPe7NfFOTZcxQa9ffRBcqn3qRZcHm8Q_1kFniuW4DVgeZfXBlOqz52u1-no13x2cNTtoZ8uQlbExufufXpUwDDDcpIofRLUI75aS3c-zaad0IM5pJV5PGFvom2nEzFVBenLAnZO9aPP4WMwiOMMjhFuifcnTC1klqMYJBXZd4tnjgPE5lxyoJHtOGr0nnLw65EbIzFFEJxV1wKW0ivxKDulXiBDqcQXRntkAXGZ0Fwl1RHpijQSCV4rm3Kiao9Rgi2nIt0b2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.
این چهار حروم‌لقمه عبارتند از:
رضا تقی پور، نماینده مجلس
کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی
رسول جلیلی، برادر سعید جلیلی و عضو شورای عالی فضای مجازی
محمد حسن انتظاری، عضو شورای عالی فضای مجازی
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65076" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65075">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65075" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65074" target="_blank">📅 12:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=aHVLEYoqR-0g9ZWmrndgLjyuX1dRTafqHTxvMZg2Zf4r8hD678sqvqVPNo41AMarDiyv-jUcddh872Za68IsVSqwpd8KylzwgRNqqBrVnYF06ehLX_8aqgBXf6Iq7HPLv6jNt9nfg_PH4ruw7bBELE18Yi71bK9x0_5hhljSAAR91jkE7zk5V8c-Fd8OfR92Mob-J56LzBItzEMVzJXaX3v_wLLbg8Bh1sgA5rG_WLjUr0AGU65b80ESAuTrkxBmf-7EgpkbCSAWESQEzzlsnpaY-h2cQRs3jQ5-bzUSuFtXMlicNX_xu-MrOJaNNAVIsmhP7e1USQBiPl7H32i9QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=aHVLEYoqR-0g9ZWmrndgLjyuX1dRTafqHTxvMZg2Zf4r8hD678sqvqVPNo41AMarDiyv-jUcddh872Za68IsVSqwpd8KylzwgRNqqBrVnYF06ehLX_8aqgBXf6Iq7HPLv6jNt9nfg_PH4ruw7bBELE18Yi71bK9x0_5hhljSAAR91jkE7zk5V8c-Fd8OfR92Mob-J56LzBItzEMVzJXaX3v_wLLbg8Bh1sgA5rG_WLjUr0AGU65b80ESAuTrkxBmf-7EgpkbCSAWESQEzzlsnpaY-h2cQRs3jQ5-bzUSuFtXMlicNX_xu-MrOJaNNAVIsmhP7e1USQBiPl7H32i9QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65073" target="_blank">📅 11:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65072">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رهبر سوم جمهوری اسلامی: سه چارتا جنگ کردیم همه دشمنان‌مون رو تا ناموس شکست دادیم جوری که ویران و حیران شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65072" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65071">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
رهبر سوم جمهوری اسلامی: پدرم، علی خامنه‌ای خلف پیامبر بود و بعثت الهی یافته بود(از طرف خدا مبعوث شده)  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65071" target="_blank">📅 11:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65070" target="_blank">📅 11:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65069">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O4asf3QnU-dsW3XKW0GlKcwn_zpC0yN7aITXEIjlME8zFQlRtg6hK7hHiAkJGX8vRi71w6EdcvhwfteBWUac-15UCR7vPKqp7Biv8ZALp6TMAw3BLi9yB6_FkSYp9b4py5C4xLRkz0F5uN79Gp7RbtCQXbuR2gFsM0qZk9t7lyUlF-FBUr39UlZURLsIfDO83BoXyyqPWsRK3ON124miJ348nuKVJ7jyfT0T5vpDPwCWjxv6MxApcC-y-lAId-lSJCj1VTJmXmZWrJ3wg9HkEvb3ImCP2WzbjFC4FlBuAEYjPLeS38txNm25oXstSwG3SXfDh5z6NABEs3RPMZY4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65069" target="_blank">📅 10:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65068">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YsU-LwN6wbc7SGXe6dg3xjMmYWfG2UTBqN_mYxjshhhnHO0ky41GFabdbVtZ-ka1U-knY8YcSyZc9jZwhL0ZHpQ3YpjC1HcoNfMfu8cPauJdnECHhjAxi3Di1iHWQ6LE0rNvR1xSfsOKjSlfxjoVsEUeKeGmYeuS-tuMBqvSmENhfc0-GkdKIxfiPVQ60vAc5q-sfPoNrZFmTzA0sebcJ_QIRez92qR99B8I2PFdue5_g3ssYT88XRi-aAYK3953MNhmmDvGZeBlutTpHXpXz2c0wiWdEchsudx9tuQ1AJ42woxwmWuJuUZkB7T3_z5LVXMbO0QnZ36Y4dLNycvqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65068" target="_blank">📅 08:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErU7odRmiiQWRHAcnaxg-7j5I1dT46ZWRdoaoP7tblMeFlKcXObew6ZDOKKTLqHBSVc3LE_EKgfsbTV6WFAob9B8yDhDIlX1o25C3DqvYVV1aVxZjD6nEq3AuqCBNoAFKQV3w6lsdn4AOn-4U-954n_20p9S5_lJWqEbRz7rCmIeQwHNajp5vuc4HRBHD4SqsjmnjhO-WLrkZGyEkIAkc_accjNdUD9w1l50g7msRVF6Kxh1brA-ADEtGd0n7280GyED3T4pJqh3dx3SRc6SS3MUgrbW7QSvD5OWo9CJ5IrdALVNaO32xe5NHGbZVn4fKy1Nsqxp88nUlxASk3KCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65067" target="_blank">📅 01:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صابرین‌نیوز: امریکا دو قایق تندرو سپاه رو با جنگنده زده و ۴ نفر هم کشته شدن</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65066" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkk-KXQHIH1t6LbdGCC9U5hJSfEBBLA6s7gfDiNrhUkoebzjXbRYOvANtH8nmfVIzm_SV1XPicLU_cNxZY8dxLEf36uQXQqeVp3XZkjk02T4Wrcr5lVotMnoUsLu-g4-o-LQxUISCiFOyjGAnpSO83f2qngJN57DkkkHCsvjRi_oD0XyM08NhxhszxuLIc5bbllxs6yXYdH6OqIJLRFrE2j-pVsd1OLoIGS325FH8zy23Qtz_RaHx_l6XVWMn2G1NkoxLEVUAdcMGB_u1ZrlsC1MQ4dWTCf_CO7qqcIWjiV5xku6suwMZ1Z_h1iGX5S3q6Ma6yjs6SGXNVc0mEwzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود.
یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل آن، این فرآیند و رویداد نابود شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65065" target="_blank">📅 01:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65064" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo59FBCxeX27i4w6fwjXtdwZsujXk9QOOs82_5CMW_W9-rCuHp-mNKopE4En0vuY6j85zPbd4aEozJQzZ9_bBMYu5GIb4T9GT1S_HFHgaYy11HmFgDn2IV4Ndy0CePpE50VcaEcm8hA_KWejbF7qC4PQR1s_8Tw-mHZgEmh1mFhSWNfgrmn3mu5yHpGL8exlW6pI2UnAkW8SYaACQHO9YIqx47X1meulhcEprS9RJSqCwEHJrmiSHnIzBb49gzF5A5nnwCc3tpXiN5XTiHeikeZtgZRcIGlc3DAiNF-YbutH90SR1Htm-XLntbD4avqblFRZlOLOou2z1lW9-7fIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری تایید نشده مربوط به انفجار لحظاتی پیش در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65063" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65062">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65062" target="_blank">📅 00:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65061">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
📰
آمیت سگال، خبرنگار شبکه 12 اسرائیل:  ایران در حال حاضر فقط حاضر شده به توسعه سلاح‌های هسته‌ای رو متوقف کنه، در حالی که ایالات متحده چندین گزینه برای ذخایر اورانیوم غنی‌شده ایران پیشنهاد می‌دهد، از جمله فروش آن به ایالات متحده، انتقال آن به یک کشور ثالث یا…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65061" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65060">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به صورت قانونی، ما یه "شورای عالی امنیت ملی" داریم که به "شورای عالی فضای مجازی" دستور میده که به بقیه اپراتورها بگه که اینترنت رو ببندن. به صورت غیرقانونی هم سپاه رو داریم که زنگ میزنه میگه اینترنت رو ببندن. زورش میرسه، میکنه! حالا دولت رفته یه "ستاد راهبری…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65060" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65059">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
ترامپ: من به صورت الزامی از کشورهای خاورمیانه درخواست کردم که پیمان ابراهیم را سریعا اما کنند تا «جمهوری اسلامی ایران» را در ازای بخشی از توافق پیمان ابراهیم داشته باشند  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65059" target="_blank">📅 19:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65058">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
ترامپ: توافق با جمهوری اسلامی ایران!! به خوبی درحال پیشرفته این یا توافقی بزرگ برای همه هست یا بازگشت به جنگ بسیار بزرگتر.  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65058" target="_blank">📅 19:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65057">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇺🇸
تروث طولانی و مفصل ترامپ درباره توافق با ج‌ا و پیمان ابراهیم:  مذاکرات با جمهوری اسلامی ایران به خوبی در حال پیشرفت است! این موضوع تنها یک توافق بزرگ برای همه خواهد بود یا اصلا توافقی صورت نخواهد گرفت؛ بازگشت به میدان نبرد و شلیک، اما بزرگتر از قبل و هیچکس…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65057" target="_blank">📅 19:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65056">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65056" target="_blank">📅 19:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65055">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENOdE4xPhjw8E2DOuT5BJQxCFB3dLrtSY50Nk_qk5xlBCmJRhyWz6ukMLpMIpA0-_ukWBte5kOOVfHlk_QRRlPI-wdy6UXpJBMX1TYXzgJPwooho7eKmc702Al4wKhyxBLDSl-dIZnOPNDg7LtS8PRyVZFMd7bGUa7fxj-icF6aoxne4k6ac-4ObDsVgZQ0PJ352iND9WX15btPcELoLkTKy0M6WVOFSO6EYFxWCn6NMaGYixClU6NX4tVoENfbWUyd4xiIZjdxCUZzBsvPwjcMbvGJYRlF0A-IuvbglUmhEOZgoNZgfa21xo-EJ1ztVMBgpjbpgdxyjoJtpgEaGGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم  در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟! #hjAly  @News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65055" target="_blank">📅 18:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65054">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم
در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65054" target="_blank">📅 17:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65053">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چه افتخاری هم می‌کنند حیوون های حرومزاده...  سه ماهه حق طبیعی مردم رو ازشون گرفتین و الان از بازگردوندش، دستاور می‌سازین؟ باید رید به سر تا پای دولت حقیر پزشکیان و امثالهم #hjAly</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65053" target="_blank">📅 17:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65052" target="_blank">📅 15:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65051">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65051" target="_blank">📅 14:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65050">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0sg-s24HSVvu4LEAF5Rd08_t20UeAf_1fTlrUZeNmFARUbuLjVQsOKVEkM5MeycHEkoLDfj6T_NdBHuItK1edSRBZYpgVUDspKAB_a4JLNaCie6fEUECYI6z1SwHyKzq7iCLjHR9KW8VrPIg4R7xeSB-P452tWn2iHb77cQU84iCVw_9cQ5a8II8Qt-Ts50NWuaBi7lPLsjIBNLKBjNBy07xp5d7UfPU63LF8S6Eksns_MUPUO35Bar0FnyszQEBM6wdIjKoYd1_70k9YdeFYwa4RD30yrMeK_jFGxxLR_x18lDc2YHj4mYPSynXxIHRlDQ_H95c5etX0s-EcIynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65050" target="_blank">📅 14:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65049">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=osOh_h-wa9FWtcxltPg6ItouYdmUgKilb4uX40XY8z4Mbly_4hr_PZokenqho2RdCwLE9NrGRzGkzjwVVd5V9D_r7FRNYGsd4Km8ySHx13gT-ZOcwtXXTvkZpSqo-JA7dW9oIzmoyuH5XmmdfIDPKTif4b-a4btYprDIYKSBiCix54s1wm46Rr5KW4gaZdiPuEliJdlANyD8zCqkldvXICNjA7Uz7Q8uvMwCjAcsgRPcks6FarJtqA9JUouhjX0wh0vEW0LwcCjfyU8YGnpAFbHWuqjcLQREDYQbJyAo3ZKJfyde7CenjDVGyisRSeOrEVPeIKoJ8YM0rq7LqfS-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=osOh_h-wa9FWtcxltPg6ItouYdmUgKilb4uX40XY8z4Mbly_4hr_PZokenqho2RdCwLE9NrGRzGkzjwVVd5V9D_r7FRNYGsd4Km8ySHx13gT-ZOcwtXXTvkZpSqo-JA7dW9oIzmoyuH5XmmdfIDPKTif4b-a4btYprDIYKSBiCix54s1wm46Rr5KW4gaZdiPuEliJdlANyD8zCqkldvXICNjA7Uz7Q8uvMwCjAcsgRPcks6FarJtqA9JUouhjX0wh0vEW0LwcCjfyU8YGnpAFbHWuqjcLQREDYQbJyAo3ZKJfyde7CenjDVGyisRSeOrEVPeIKoJ8YM0rq7LqfS-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد نگینی‌پور، مستندساز حکومتی مستندی ۴ دقیقه‌ای از حضورش تو پزشکی قانونی کهریزک منتشر کرده از اعتراضات ۱۸ و ۱۹ دیماه‌،
تو خود مستند حکومتی که منتشر شده تعداد بالای کشته‌شده‌ها و کانتینتر های حمل جسد دیده میشه که جنایت خودشون رو به کار دشمن ربط میدن و ابعاد بزرگ این جنایت مشخصه!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65049" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65048">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65048" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65047">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=b7AqM51MUH3bAqSIA5C7s3NMQTCfYFScA13n-Ktq0yh34LEJecn-MaR3mxmf8ENHV6jtql32C-3YX3VdAqnysflb1taGP7ae6hWJv7G1PbWGUTGlbvTX7NVTKPOFEaOj2pgVCXLthVp60GKCNxi591O1wX5HaMvl4h3jknA9cNPwsfKDGqtFKaSsJJlGTG7G7iswHJ7Wj55-pROFtalecxnlzCE64vaCEVBTV9BSo6cDOUzMUj5oGeOEmWXdKy9o2Ugz9dLpLF1UvMSFeAo8ErQYP0bAdreLfWHXhu-UGPP6mdNDleMHJc3XwI7y-d3iy_CTv7Af4cIKgj0cLg--Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=b7AqM51MUH3bAqSIA5C7s3NMQTCfYFScA13n-Ktq0yh34LEJecn-MaR3mxmf8ENHV6jtql32C-3YX3VdAqnysflb1taGP7ae6hWJv7G1PbWGUTGlbvTX7NVTKPOFEaOj2pgVCXLthVp60GKCNxi591O1wX5HaMvl4h3jknA9cNPwsfKDGqtFKaSsJJlGTG7G7iswHJ7Wj55-pROFtalecxnlzCE64vaCEVBTV9BSo6cDOUzMUj5oGeOEmWXdKy9o2Ugz9dLpLF1UvMSFeAo8ErQYP0bAdreLfWHXhu-UGPP6mdNDleMHJc3XwI7y-d3iy_CTv7Af4cIKgj0cLg--Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ترامپ قرار نیست توافق بدی امضا کنه. هیچ‌کس به اندازه ترامپ تهدیدِ هسته‌ای شدن ایران رو جدی نگرفته
خیلی مطمئنم که یا به یه توافق خوب می‌رسیم یا مجبور می‌شیم یه جور دیگه باهاش برخورد کنیم.
ولی ترجیح ما توافق خوبه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65047" target="_blank">📅 13:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قالیباف دوباره به عنوان رئیس مجلس انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65046" target="_blank">📅 11:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65045">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVRyeIpxxJliiwwFLHZlwRV17AODTGc-fDQq5s7DiXlhKPT1PFZaIf0gPAJbTIGIUTYDdWMec0BDEaPVcpBrYVbviGKzwXFH93pDGta72sZWMqywMxl0ko4FNeh3xx4NbNxglWvz3TGcXSvLBylh6E2fNO0E4XtwBjOzD3GcOH0UYoWWPPeemk_Ol6kK8jkODDy07JyZ2Zu2aiD2_H9IfCAzDByCxIIeh-mK6dJWdD9XCyyW60i32Yxh5lDt3bot6IinRtTZG3stvoX5TAjJv3pkN86V0pHhrIYCbywYSmUvge8Or4u4BogFnEtQwaBftLf6V6-hWZkBP6CrvD_bHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوج حقارت ارتش
ایران
به روایت تصویر:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65045" target="_blank">📅 10:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65044">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: توافقی برای پایان دادن به جنگ علیه جمهوری اسلامی ممکن است «امروز» حاصل شود
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65044" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام: اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.  پیوستن…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65043" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhWwTh9s5Y9TDCjRmqFMwa530VdzaxvOTHzmUeDeAmXOos_aBGB1IHMTbJ10qRAoXHBqqxei7vLecnP6ESSFaKOJyf9ZwyZaCJn7KGCUiGaiel52MGvazO_9RcaNvswjIuI800DRtAbkvq_NE6kWHvPWYggiDA_RNW6FdDRjgNaLvSdH9i-ByeB_wica-0z2y0gbfa5k6_X0V7qYpIjGk3w_vTalcnEd3oQprBDCPSzZGuLOeScceDJ3m1zdeiZrYUzED1KIK2YJH3KYvVDb6IyKjJupOLghBvfqhf5tRf0I0LmXdfaIlGd0hpNqFnnwVB7cmD55hrPwwkWkZVqIrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.
پیوستن عربستان سعودی، قطر و پاکستان به توافق‌نامه‌های ابراهیم فراتر از تحول‌آفرین برای منطقه و جهان خواهد بود. این یک حرکت درخشان از سوی رئیس‌جمهور ترامپ است.
به عربستان سعودی و دیگران: اکنون زمان جسارت برای آینده‌ای جدید در خاورمیانه است. من انتظار دارم، همان‌طور که رئیس‌جمهور ترامپ پیشنهاد کرده است، شما در واقع به توافق‌نامه‌های ابراهیم بپیوندید و به طور موثر درگیری عرب-اسرائیلی را پایان دهید. اگر از رفتن به این مسیر که توسط رئیس‌جمهور ترامپ پیشنهاد شده است خودداری کنید، این موضوع عواقب شدیدی برای روابط آینده ما خواهد داشت و این پیشنهاد صلح را غیرقابل قبول می‌کند. علاوه بر این، این موضوع توسط تاریخ به عنوان یک محاسبه‌گری بزرگ دیده خواهد شد.
رئیس‌جمهور ترامپ: در گرفتن یک معامله خوب با ایران بر موضع خود بایستید. به همان اندازه مهم است که بر موضع خود در اصرار بر پیوستن عربستان سعودی و دیگران به توافق‌نامه‌های ابراهیم به عنوان بخشی از این مذاکرات بایستید.
دوباره، این یک پیشنهاد درخشان از سوی رئیس‌جمهور ترامپ است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65042" target="_blank">📅 00:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65041">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آیا دونالد ترامپ، باراک حسین اوبامای دوم خواهد شد و دستور آزادسازی ۲۵میلیارد دلارِ جمهوری اسلامی را می‌دهد یا خیر؟!  بزودی خواهیم دید! @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65041" target="_blank">📅 22:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65040">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgWY4c8Gi_rR8TjFrIO1289EVlFkI8HO2pAd3HtnI1l9H4CxcItWd8hALOADSV-8NwaMKGnUrKJES-_8QoBN2eI_s2wdGI7kepx0PGWw6YErgawh4N4j6ioJypwzhZmr-W7_GzFp-I41BGgJVbamOTxeY0ET5IChVBG1Q4rArlOYizdp-6cD_pqcEO6pyzthbBPezJIDCzI_4DAViXBVL573utUDTe1M7pEn9ichYacK5wsB1w5-aCsRvD1E-0brYWbs3419frWnloF7hp9aU8y_NYFkulf4MIRB-ZkLlzCiNmWZPVcZtcCpqeZ7UI3p06MwvR_YtdCoFkpxfppP0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65040" target="_blank">📅 22:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPAnDNwe9b_2RdGQaAaB8IEva0fTX_OgYJJX516nXjdJzSEwkIy4RJu1leCstdzi4M2Xkx_nTVZdUbd8wHpcoAvnvAlLx_mMVdyIojb7oTnMXtQYP15NOFZ99Ww68QW6fw88qe0gl0TTv5UmfSmXpA-tEuJ4OPRZgELGtBkoQpJLYwfHPjK5Y9u_fDPESOa_ZN_qy_3BlmGnRxEWybz0p87Ju32EDvNT-7ElVvjcaIWVnSPq5Q7c4jxYZV8q7UhaFMMop4BN8fCG0q6LAT8gciCPeAg1CgOznawRyiItcoA1O9Lbye79D31aw8-2AzfeftMyEYWaJp-PD_nxDBPeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز حتی به طور کامل مذاکره نشده است.
بنابراین به بازندگان گوش ندهید که از چیزی که هیچ چیز در مورد آن نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بدی انجام نمی‌دهم
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65039" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو: توافق نهایی با ایران به معنای برچیدن تأسیسات غنی‌سازی هسته‌ای و حذف مواد هسته‌ای غنی‌شده است. من و رئیس جمهور ترامپ توافق کردیم که هرگونه توافق نهایی با ایران باید خطر هسته‌ای را از بین ببرد. این به معنای برچیدن سایت‌های غنی‌سازی هسته‌ای ایران…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65038" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65037">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: من معامله بد انجام نمی‌دهم؛ در مورد جزئیات توافق فعلا حرف نمی‌زنم، صحبت های خوبی در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65037" target="_blank">📅 17:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65036">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تنها چیزی که ترامپ تغییر داد رژیم غذایی مردم ایران بود
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65036" target="_blank">📅 15:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65035">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=PYThme4D_FayUc-SJD1wtrdH7IjSQJ5lbFvzLwhy3Ka-2yCirbSCiKPLWCwqb8efH6eCqWNiPrIUdzIKNZiqR5zgJxqOe6CvKY-FnGAAyW_7Tjizs3Z3we9vgYX9gwbs2TA4T3UP2N5ylIPZg8_IknsM3NpQq9eDd7QGmdBvC7HE00AnGuYyu9-TED4m3ch_GfWJPuYP3rJtxwKGn1zH8KWJ2gLDTvu-MZQyCCVbwM1eremRLMmzp0RLj4dDbI3mReWBOv1zsFq6Ncw4OU-ic6kadt1_dthm-mihM1d1mPoP2x3uhjHMsjFzVaWt3HPSmv03yoWvTGWulxdeYKRzLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=PYThme4D_FayUc-SJD1wtrdH7IjSQJ5lbFvzLwhy3Ka-2yCirbSCiKPLWCwqb8efH6eCqWNiPrIUdzIKNZiqR5zgJxqOe6CvKY-FnGAAyW_7Tjizs3Z3we9vgYX9gwbs2TA4T3UP2N5ylIPZg8_IknsM3NpQq9eDd7QGmdBvC7HE00AnGuYyu9-TED4m3ch_GfWJPuYP3rJtxwKGn1zH8KWJ2gLDTvu-MZQyCCVbwM1eremRLMmzp0RLj4dDbI3mReWBOv1zsFq6Ncw4OU-ic6kadt1_dthm-mihM1d1mPoP2x3uhjHMsjFzVaWt3HPSmv03yoWvTGWulxdeYKRzLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65035" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65034">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lW9uiQ13QFsFyEmeyycln2emkZa0e4n0U1KQONXAlF3N3g8zsipbjWWjXr01FkJ-FXbpjOqs5TAAPzZZ1KV7ZB2e2DjmYobpwjdWH0kV5vuLqIzsl_8oVfTgqC3DhBJ6xPvGH_JIYO_dOPQqemoT_ocBRYXPyBoWle6OwHE97ZTVX2_wvXzEf1dwEmC5L4-Dhy_jrmiCf4oY3l7zoJtslxgUAt3JJhTWeawbx8Wfqq-P2Hlq0yXN7QRMZ_qEX53uOKOf2ilfEj7A6COzkWd6sYHn4H6jDCMJRS_CdnzcXVH5Uk2TNgk5S0_TfkWEJN5R-DwsvkyFaQHGo6h8mRDPaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجایند مردان بی‌ادعا؟
🗿
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65034" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65033">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مراد ویسی: سپاه می‌خواد روحانی، احمدی‌نژاد و پزشکیان رو ترور کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65033" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65032">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ectcHax9Ru3gT_x6lrVujuefmuEJjUFGkgAFn_DmUkFjyADvnn-eoqlgEy0RyFZBPUZarUUyTA6LKNhSKOevUrp5sP2i4awulK1c4sZLeyy_3tiImjO7yaXPHOiV26g-o9VVxH9QFee9CeY7c0rAfocyE1kXg9T0N5w9C7GMK1aZ2g6eiWDa9Jg9S_qKWie3bJojrQLzef92j6zBI7kRkmICHo3rHBPj9ujqMUkdVkpwkYltWdHFryVLKhvpzx-0ATA4TLSLG5n0Y5Y1GSI2BZ1w7RIrhRB3zaMUgULCIdY0q0m78fsI0rXL7BgnForVPLSEfvlClGyeTTa5RF_3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار تتر بعد از اخبار دیشب درمورد توافق تا زیر 170 هزارتومان ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65032" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65031">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
آکسیوس: توافق بین دو طرف امضا شد.
👎
این خبر فیکه و آکسیوس و خبرنگاراش همچین خبری نزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65031" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65030">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=nafafGiv-bbSu56binO5ERsg4Dfp72ug_tx2OcQLt066Dyf1rkff4UKgLa8NbDCTQBzIZIEhHtRuH-tg-z8z6biyCmnFYPr4_jx3C9A6-MYT6Q05aB7bsI2nC72rEl5q7Gc_702sg5IitVrvsUgoZclL9CSBbDTPO4_Ng-mGRhOOhi0mEjXuIH_62iSZobYbUj3L7fboPvzXL3RMZ3Ub4LQDd23h34EnLB554f1AzfMuu3ydFLxvBZYvU8Bqv-qqWwlpY1N3KDSQBA6KL8WsDFTexOcLubYAuFSEoul5qKuzYldiAlyc2m_02LUceSCVgwk70EdYJCJ22kkVNlUDzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=nafafGiv-bbSu56binO5ERsg4Dfp72ug_tx2OcQLt066Dyf1rkff4UKgLa8NbDCTQBzIZIEhHtRuH-tg-z8z6biyCmnFYPr4_jx3C9A6-MYT6Q05aB7bsI2nC72rEl5q7Gc_702sg5IitVrvsUgoZclL9CSBbDTPO4_Ng-mGRhOOhi0mEjXuIH_62iSZobYbUj3L7fboPvzXL3RMZ3Ub4LQDd23h34EnLB554f1AzfMuu3ydFLxvBZYvU8Bqv-qqWwlpY1N3KDSQBA6KL8WsDFTexOcLubYAuFSEoul5qKuzYldiAlyc2m_02LUceSCVgwk70EdYJCJ22kkVNlUDzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65030" target="_blank">📅 00:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65029">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=Tft8SzKu0lKzb5KjcbeZmS9oK4Iw7UohpXqWPGAmsM7n-T9-KBd90T__msqklZSWFzvI37_-c7oA9eivGT-o8yueKwaIzpYJQWTJiADz5T7_86fltgEAntKj3vnZlKsKUymROVCkCKCzPxJ07CbwYEevUULW06GnNoMfCaAsuxFyGOuI4aIhryiIHzjauXHrNSdSLaYk8PLlFPrmKh22B_jNB-T1HPle_BgI9C6kKMru2cnANKkDMMBvclZVSqpv96sWmnbvo0PL5ffZtGG0q3asUy29giIW9P9i3WJIo4HdYtW5F8u6ucvUMIPZyyB-ZFPYKWUGw54LJyhvRdb89Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=Tft8SzKu0lKzb5KjcbeZmS9oK4Iw7UohpXqWPGAmsM7n-T9-KBd90T__msqklZSWFzvI37_-c7oA9eivGT-o8yueKwaIzpYJQWTJiADz5T7_86fltgEAntKj3vnZlKsKUymROVCkCKCzPxJ07CbwYEevUULW06GnNoMfCaAsuxFyGOuI4aIhryiIHzjauXHrNSdSLaYk8PLlFPrmKh22B_jNB-T1HPle_BgI9C6kKMru2cnANKkDMMBvclZVSqpv96sWmnbvo0PL5ffZtGG0q3asUy29giIW9P9i3WJIo4HdYtW5F8u6ucvUMIPZyyB-ZFPYKWUGw54LJyhvRdb89Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65029" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65028">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65028" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65027">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cKm8Up5qFzQFrYk5P8SdIQZMUUFHvnyx109y8wIaZU12uQvG7j9K9dTDpAjGYfV1dOzD4_WMH-fUKrN-YL3qf7AIVy08J7F2GHTLZkoD_0z3od1RIeCiJIJH84adV8bBo4hjkNVqGxT8mo0j0pFIVzIiFUGfdteogcYMEpKzvMIizKRvoxtAVYO5nPViOXdbrjF5StBZmGNIwESjwO2SHwYmmhY_QoTLzW--cC451vpSptZfV0jneTVaIAI4HeZug_tJiZvdChL1ZzurV7c43T39dk3L4PxyEeYl69YhztepQo85NU1pmRYEm8RrrLg8I5qs5Z2Ss7F1ZxfSQVVbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ:
من در اتاق بیضی کاخ سفید هستم، جایی که همین حالا تماس بسیار خوبی با پادشاه محمد بن سلمان آل سعود، عربستان سعودی، محمد بن زاید آل نهیان، امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی، و وزیر علی الثعادی، قطر، مارشال فیلد سید عاصم منیر احمد شاه، پاکستان، رئیس‌جمهور رجب طیب اردوغان، ترکیه، رئیس‌جمهور عبدالفتاح السیسی، مصر، پادشاه عبدالله دوم، اردن، و پادشاه حمد بن عیسی آل خلیفه، بحرین، در مورد جمهوری اسلامی ایران و تمام موارد مرتبط با یک تفاهم‌نامه مربوط به صلح، برقرار شد. توافق‌نامه‌ای به طور کلی مذاکره شده است، مشروط به نهایی‌سازی بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همان‌طور که در بالا ذکر شد. جداگانه، من با نخست‌وزیر بیبنتانی، اسرائیل، تماسی داشتم که به همان ترتیب بسیار خوب پیش رفت. جنبه‌های نهایی و جزئیات توافق‌نامه در حال حاضر در حال بحث هستند و به زودی اعلام خواهند شد. علاوه بر بسیاری از عناصر دیگر توافق‌نامه، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65027" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65026">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">بله  مگه چیه ما با ۹۰ هزار ... گواهینامه مون گرفتیم</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65026" target="_blank">📅 23:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65025">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گواهینامه شده ۱۵ میلیون تومن!!!!
الان یکی میاد می‌گه حاجی ما با ۵۰ تومن گواهینامه گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65025" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65024">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بستن تنگه‌ی هرمز در جنگی که ۹ اسفند آغاز شد، تمامِ معادلات آمریکایی هارو بهم ریخت، اون‌ها حتی چند روز قبل مین‌روب های خودشون رو هم از منطقه خارج کرده بودند! دومین مسئله‌ی شوکه کننده برای اون‌ها حملات وحشیانه به کشور های عربی بود  هر زمان آمریکا_اسرائیل به…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65024" target="_blank">📅 22:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65023">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65023" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65022">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم می‌گیره، یا از خواسته هاش عقب نشینی می‌کنه و یا اینکه دوباره جنگی برای اعلام پیروزی شکل می‌گیره، تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65022" target="_blank">📅 22:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65021">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65021" target="_blank">📅 19:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65020">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65020" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65019">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
📰
ترامپ در گفت‌وگو با آکسیوس:  در حال حاضر احتمال کاملا 50 / 50 است که یا با ایران به توافق برسیم یا دوباره جنگ از سر گرفته شود. یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم + ترامپ شنبه با…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65019" target="_blank">📅 19:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65018">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فایننشال تایمز: ایران و امریکا به یک توافق آتش‌بس ۶۰ روزه نزدیک شدند!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65018" target="_blank">📅 19:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65017">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
📰
#مهم؛ فایننشال تایمز: میانجی‌ها معتقدند که به توافقی برای تمدید آتش‌بس به مدت ۶۰ روز نزدیک شده‌اند.  این پیشنهاد شامل: بازگشایی تدریجی تنگه هرمز گفتگو درباره رقیق‌سازی یا انتقال ذخایر اورانیوم غنی‌شده بسیار ایران کاهش محاصره آمریکا بر بنادر ایران رفع تحریم‌ها…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65017" target="_blank">📅 19:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65016">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asc1Ww0uhtmfnPjz5JAqIqq8hRUlceAcZB9hu1tur_5F0Ca13cC1bkZQ4DMLoQ5aIpImR2VoXPQnSJm1_4Wp3jWMPUksT60RME4X5Gtm_08KNKD_X82sq5_L48haqTa3dpgAV8p0anheIzA6HsQI50CTTImCrpOXnWHptGXDk1srENeVEPwk2McpaAYHjDOMT8ZCGAE8mJg19dcnj0DAUmIBMRlXN_ZDRGo9eQnYvA7HdpMgg3-TP8NmFp_QUdVCJR9hWQrYakDsc8Zmhg2V9NwkYR3UqE4PShW7CBNTBQThyZ61cxwt2Q-g520Gyn0Roh7kLWJGkswIM_FhRl3zng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ تو تروث‌سوشال: ایالات متحده خاورمیانه!! با پرچم امریکا روی نقشه ایران
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65016" target="_blank">📅 18:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65015">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ مارکو روبیو: ممکنه امریکا به زودی خبری در مورد ایران منتشر کنه شاید هم نکنه امیدوارم این اتفاق بیفته
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65015" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65014">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=aU-LVpwYhYKlLesUMZRBiqiGvzdcv7KkkHrbafi4STFOTwGsws1DbY1lAXwDo-ZN5m9Aho6ekf1k3arfws2fWF6PlMSIopiZ5McJm24IU2ARGwpup13JcTIDk3HZGoqIne40Gr3wRbAGjPYEApnK3vQDhHBR_fuJFw45gmIM8nlKxTgLD_Jy3Pm0NBU_qL1QDmOMKuKPX_EZPCliJr5a7F_Mhrj__3tf19lrnWahUupqFjoweZYzg6efUTkZEWpF4ZzFkbV4PF1sbWqU5cROSec1rRCXBMNw7VsnCqm9rMlG692YP5Y32mIW5sqHNYkR9MPcwqXrVlQe7nAUHDkQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=aU-LVpwYhYKlLesUMZRBiqiGvzdcv7KkkHrbafi4STFOTwGsws1DbY1lAXwDo-ZN5m9Aho6ekf1k3arfws2fWF6PlMSIopiZ5McJm24IU2ARGwpup13JcTIDk3HZGoqIne40Gr3wRbAGjPYEApnK3vQDhHBR_fuJFw45gmIM8nlKxTgLD_Jy3Pm0NBU_qL1QDmOMKuKPX_EZPCliJr5a7F_Mhrj__3tf19lrnWahUupqFjoweZYzg6efUTkZEWpF4ZzFkbV4PF1sbWqU5cROSec1rRCXBMNw7VsnCqm9rMlG692YP5Y32mIW5sqHNYkR9MPcwqXrVlQe7nAUHDkQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقائی، سخنگو وزارت خارجه:
ما هم بسیار دور و هم بسیار نزدیک به یک توافق هستیم.
دیدگاه‌ها به هم نزدیک‌تر شده‌اند، اما نه به حد یک توافق — بلکه به حدی که ممکن است بتوانیم به راه‌حلی برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65014" target="_blank">📅 17:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65013">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73653df566.mp4?token=PVQ1s60JaDg4mSPosl9WTX25QvnF_JqMqRUEgB1bvI_hcyabhw7N57l7s1z9Hj38HrgYE720d30TGDfkx8T9Y3R3Fqy9nsUIa1A4PyvDf_3OZlSx2bqY2bHxo9kwEinSqna0JjeFc5gfaS4EYlJ7NEj9ZfHnnSLaLATHoDGhtraB7fH5MCKP8XpgMeTXIMrViJV_aWZBt_kN8vtt4-wAIfie9SDEql-7TOIVARSk0Wo716JmpJUJWUnLptzwYxw4x9gpBBdeDwzoK8M0k80UahFnhbAGXVGDKLQW6i7QqgbZvPh2EzwGpgxkYaTKdkOeNhRpwqdhEm07CJmX32-qxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73653df566.mp4?token=PVQ1s60JaDg4mSPosl9WTX25QvnF_JqMqRUEgB1bvI_hcyabhw7N57l7s1z9Hj38HrgYE720d30TGDfkx8T9Y3R3Fqy9nsUIa1A4PyvDf_3OZlSx2bqY2bHxo9kwEinSqna0JjeFc5gfaS4EYlJ7NEj9ZfHnnSLaLATHoDGhtraB7fH5MCKP8XpgMeTXIMrViJV_aWZBt_kN8vtt4-wAIfie9SDEql-7TOIVARSk0Wo716JmpJUJWUnLptzwYxw4x9gpBBdeDwzoK8M0k80UahFnhbAGXVGDKLQW6i7QqgbZvPh2EzwGpgxkYaTKdkOeNhRpwqdhEm07CJmX32-qxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توئیتر اکانت ترامپ که با هوش مصنوعی به ویدئو درست کرده از مجری سی‌بی‌اس که مخالف خودشه و ترامپ میندازدش تو سطل زباله :/
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65013" target="_blank">📅 15:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65012">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RILp-xoc8M-NZGHsuBG6kjO7IFQML5qaPbepoyIuLnTQdDBLvrnJrtW8XjF2JbEyAUXc-VE3z-YabSht0oFbH3TfLD4q76R13wemyrUI0qzG8kR-dDETpYmj_qQ8bEOEyM9mqRYPQ1NXfwy98uCigEJQbZK8pxFs6e6bsAwPr257EheRNmKJvCD0Ql8ycEm0KtBIo-HSAsA-tIvMlErscM4fEd6QjJxY8FByJRHh0dG4Id19g5vXtGTliaQz0EFsFVZxDPPClaTOsuJDoUiab_1kmsqX4VAglEyg1bWPZzNhNeEbiyFeKtRZT7AbYu3HWaeuEXnHPbrdYs_ftWO3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عروسی پسرش بود نرفته، آخر هفته برنامه گلف داشت که کنسل کرده و تو کاخ سفید مونده حالا خبرگزاری‌ها شدن دو دسته یه دسته میگن توافق نزدیکه حتی متن توافق منتشر میکنن یه دسته متن توافق بقیه رو تکذیب می‌کنن و میگن کلا حتی نزدیک توافق هم نیستن دو طرف.  این وضعیت…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65012" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65010">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MvfjhmSKRkZLK9PW7mgzLo7sRNTWD9WRcshGfEH0WFH1k0Or4RXshsi5dgIFPBCv2atgAQByPcXu7c0ncmDKa9QSX3m5f-v4zGRnreHPy2Jm9H3vErttvVEOsQVSZGjajahBpwy2vS4DSoTOX_h0gWXMah9KbKzwhcWW2Cci8qxr-4onEN9Yry3IDiAeM1nx4IDe_zkNIINBZGj1Er804RUEd1p7NqwFKMSNXDF38RFVjjhn_QwcCzUsTYuJjwe22FuzqmRM3Aq1rPDDVMTsTDC9XEe2gYAhPuohUTy57pMkloIwD4zgVWWseS7MI1cuZEVam0RpRaXwjG0l7TGURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=HrSrvGcJRDCCG1K715-4MpnuRLzPnk4yW0uujhX2-6P5QtWlXAYAO4wOM9C1zKeHa2evmhDxYdxUynFI6uuB30S0NKshF63da-zlC0oLYr1W8T75YkLHAdIarJUNSHZbobmfP4XTxXn03FC3Ggj4gBYtepGVZT-fGNYx-XSzXuYdK8GuvvxxdUWqFj9M4olRhKi2NLyGxIlb3vcNLY-ibDJgoTuXvWqejBw9GhR0iQEdbCl6uCE7f9Nv6Uz0e99jA-FucXQXagaeEDCoFdlwFpjlX-jln3Yf0nUOxYnZnec7ewlITSpAsjo-o6oDtYiEBEtyWdcPWojFa5PxhJ0hiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=HrSrvGcJRDCCG1K715-4MpnuRLzPnk4yW0uujhX2-6P5QtWlXAYAO4wOM9C1zKeHa2evmhDxYdxUynFI6uuB30S0NKshF63da-zlC0oLYr1W8T75YkLHAdIarJUNSHZbobmfP4XTxXn03FC3Ggj4gBYtepGVZT-fGNYx-XSzXuYdK8GuvvxxdUWqFj9M4olRhKi2NLyGxIlb3vcNLY-ibDJgoTuXvWqejBw9GhR0iQEdbCl6uCE7f9Nv6Uz0e99jA-FucXQXagaeEDCoFdlwFpjlX-jln3Yf0nUOxYnZnec7ewlITSpAsjo-o6oDtYiEBEtyWdcPWojFa5PxhJ0hiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی از برنامه جدیدش به نام مای دات رو نمایی کرد و برای تبلیغات نوشت:
اینستاگرام پولی میشه ولی برنامه ما رایگانه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65010" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65009">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65009" target="_blank">📅 03:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65008">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65008" target="_blank">📅 01:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65007">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">واقعاً خوشبحال جمهوری اسلامی که با چنین اپوزیسیون احمقی طرفه، نه تنها پادشاهی خواهان با [به اصطلاح] دموکراسی خواهان دائما درگیر هستند، حالا خبر رسیده که علی کریمی و شاهین نجفی از داخل گروه پادشاهی‌خواهان هم باهم بشدت درگیر شدند
!
شما با این وضعین می‌خواین در مقابل آخوند بجنگید؟ جای تاسف داره واقعاً، حیف مردمی که گوش به پست و توییت های شما بودند و هستند!
#hjAly</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65007" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65006">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=qiAR0ZuKnTilj22hD8tPuJVoiDMf0oB353ZcnyZ7LKdJV6h0NSjUem4Q5cW7AeRtIKTVHWC2NFwNwbDBJMjKw8ESAflsvwHCq39D_TkTdRV3v5MzW-sek-8UPRn4DlWV6ZviCi_YSyl0sw5upRB02G6PJlZaEeCgds_F6oKgCH1gXKnTOa0U5KZY_pePqhQpx_AxxBJcRtn7eu2GrkqC1hgPin1BT1IiSiDg6bHMXHxb9CPbM2z8tBYBPyKdWdUSoEw12K124i6-7iqpUrpZKKGrDp5RIS-EDEs7LjERxUwgkNKnnIg7nOym3JjhZm4YNc2lrkEj42DGIYA03lkhqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=qiAR0ZuKnTilj22hD8tPuJVoiDMf0oB353ZcnyZ7LKdJV6h0NSjUem4Q5cW7AeRtIKTVHWC2NFwNwbDBJMjKw8ESAflsvwHCq39D_TkTdRV3v5MzW-sek-8UPRn4DlWV6ZviCi_YSyl0sw5upRB02G6PJlZaEeCgds_F6oKgCH1gXKnTOa0U5KZY_pePqhQpx_AxxBJcRtn7eu2GrkqC1hgPin1BT1IiSiDg6bHMXHxb9CPbM2z8tBYBPyKdWdUSoEw12K124i6-7iqpUrpZKKGrDp5RIS-EDEs7LjERxUwgkNKnnIg7nOym3JjhZm4YNc2lrkEj42DGIYA03lkhqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امتحانات نهایی پایه یازدهم و دوازدهم تو بازه ۱۵ تا ۲۰ تیر به‌صورت حضوری برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65006" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65005">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65005" target="_blank">📅 21:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65004">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
العربی‌الجدید: سفر عاصم منیر به تهران دلیلی بر توافق نیست و پیام جدیدی منتقل نکرده است، گزارش‌ها درمورد مفاد توافق گمانه‌زنی است و اختلاف بین طرفین هنوز زیاد است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65004" target="_blank">📅 21:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65003">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
📰
العربی‌الجدید به نقل از یک منبع نزدیک به مذاکرات:  سفر فرمانده ارتش پاکستان، عاصم منیر، به تهران به معنای این نیست که توافق در دسترس است. گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و صرفاً گمانه‌زنی‌های رسانه‌ای است. وزیر کشور پاکستان پیام جدیدی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65003" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65002">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
📰
العربیه: طبق منابع العربیه، انتظار می‌رود پیش‌نویس نهایی یک توافق احتمالی میان ایالات متحده و ایران که توسط پاکستان میانجی‌گری شده است. که ممکن است ظرف چند ساعت اعلام شود.  شرایط کلیدی آن عبارتند از: آتش‌بس فوری، جامع و بدون قید و شرط در تمام جبهه‌ها، از…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65002" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65001">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری های حکومتی: عاصم منیر وارد تهران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65001" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

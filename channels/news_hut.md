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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 21:09:14</div>
<hr>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac4qn0pELJ8gqbzrPKvfcYROVr_LQiVlXJYBdZri25Z2coHHQahz7Tus-SnHnfPtrQ-TKmVNZDzTi2ffPeQHEXuTjK6E-ECSw0dc8wGfHetJHolVDqFgGRWai2rHVqmZKsXj-C_TH51ymKzLNWOgoieGQZqqOejR12wXnMs5C02WmecFvbe_VWStSzpoYJfO_t6cuUmbSrl_wivVt6t1P0QwWiBYuN5J83pcVcn4Kib_Vx354qeDJR2KxinSVhy4Lab8RLYzYd7Xp8yKFnMqx2WR9tP-zGsh_yuBlTuqnzAughAGjH-9ogiSCJ8iG47yu7ouge37seVPAiBIk5aaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyUczIRYFleyZXcvCDsPz8azRDNiSHgG-TPa6YerZa4zo-SraB79N5zEtOgCtfzSx1D3aTVtrjyas4y1OUAxZs_ZjmDxE1DbI41V_Mn4tv00B4-FCqF4Mq2Yp7uW_fflbbQiBoH8yDZ_DK99ceiA0AhNhTXJF-Kode5L3R17iCQ9kK7p-MN8WV1GrHBnOJgZkqMcbtv9glVI-kfYEV-9xMZsqr3yGWqvv4I8u1RIs0Am6gckToPrP47pnFXqJ-igbRXkQNhh_vIxAISPiF1Uy83iULkn5lUNMJa5EUR5oluoMI7Zbd2m_1twT1xr_mb92hdOA7aY6SHucAFdWpEl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTrsRvfu0L9VJt5PijU_M-VTCQaOlNHp3_UVFXreWBy6uvR9nVZYq1_eqVsOg-6ICbzaP10ae7uXli8xM_ZyS7eB51kKYZpdPbk56tOAfwlx04TqUIuIh_sGbo6zIreTch5IttY9uzogRrOa8Ds7o1WhaVgBT3bO_1uABk0jtHM-Vu5GKq3qVC89d6BxXu3EWKHq1XOjJf4kvtEhSQfYHWui8Ccnrzka2LWdmj78Q-IrQnFYLICQAkCzuudrU8f4knTVqIuhaQXeXeJhCnADXeaQ2Rt1Mkk-CjeVNJXZ2iwyNmXPg_zGP6GHechBdArareCHnKwPepeojzSM7GNdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZCHVG0CUM80XnMsmzr62tYXmRBBmDcsZ_YCl5oukanKiHM2MBUQOIxTqD0Qv-3zTKTaBxzGuYu2F7L4xErhWtyCt-utYX4MySF6kTVIu2VQUEfPzYtCwDubOGzh3Lub0ph_X8vpw1ZzO0zWurSkKlelQoYHZIwCK22eVDodzpdsELo8jpDDBrGPrvm8QV0Yf-l2Gd_kfm-gqSNlINAK3z30vKbuoNb6dHwFUi1x8t3WONY003fWX0wZZNUylTvzQ5418SzHIXKyImrmt6odvhaWIVluQ5kXRg58RCQz4DCqRcTwMTUSvYJOYWpKqoUlx1L6c7XTLPCWjVBtR4Qhkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvCx02mt9QBEFMmtPk-GXb1okZgrPXIsGZ3_rRsCgAnIpzO3TCckafD8QPKu2A13gwewiWhHYDjpxQCR8jFGVbwAAuYCgCbjU-ZkmpY7lwoQgyfAONyV0jRNXecX84bol8hMGuA6-WsLc2zaw_SHGgCPmjo1n0QkP1azMktsJ-5bi1sJJkopauPf1ZOoe2R13FVWEDokg5huOzL_Z8VzpXX726fAG1XBJTzS720Vp7Byokt8wySq71vDF2RN7eADL8FnEGmjrWrnddP1BjCTl2xKp8m4PmaTr_qOD5UBK9FZDovX16dPOMD5DWzyjrnCAZE2B_vSbQtOkwsRNPncIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65087">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-text">Barko VPN_v2.0.apk</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65087" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65086">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65086" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=kiHdxOkzqkYwChHs--SOuNSGXFG_SGajGfsTNAIADbMUC_gomG92TMl2O1bKx7bXjMjg9rWwCdTFnx3fWZNCghZ6P3kY85c6vfqIuR32wMh9cMUL2qwpwAAXBpLDFT3cAZ5mdXqnVJVUlSZVxuqHROeuCq5usvLl8kR5X-_Hd1Pso8MBuWsQzPog6lYqUFzYZkB2KjexpgSqPuyiMdXDK4CKEX5k7vzcZQ0_8oRpUMvIdD5m5qLJ3UgHiAYK2eZc9gOAnju52MqvE3n6Xsqwc9cf4uu1ldJRrKmL_gyXLGEZLTLliLYJFNsi8pmlVl3uYFe4RBLxDabE52VV4jqqAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=kiHdxOkzqkYwChHs--SOuNSGXFG_SGajGfsTNAIADbMUC_gomG92TMl2O1bKx7bXjMjg9rWwCdTFnx3fWZNCghZ6P3kY85c6vfqIuR32wMh9cMUL2qwpwAAXBpLDFT3cAZ5mdXqnVJVUlSZVxuqHROeuCq5usvLl8kR5X-_Hd1Pso8MBuWsQzPog6lYqUFzYZkB2KjexpgSqPuyiMdXDK4CKEX5k7vzcZQ0_8oRpUMvIdD5m5qLJ3UgHiAYK2eZc9gOAnju52MqvE3n6Xsqwc9cf4uu1ldJRrKmL_gyXLGEZLTLliLYJFNsi8pmlVl3uYFe4RBLxDabE52VV4jqqAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJ1as71sCs1Di6eyzPLZ0oka00GkADz_b46tfIGmfJuctDuHaOEuN1GnN_0TuQhWCt7twN8O1WvjxEFAHGOv-FqxNTOqm4QXQObWo3vtMvJP9sTVPu1WCouFqwuvyk-Quyn1C7cyIET_aYhDwNi7rJTtqVNoyG51we3ropLBJ2oWi02EfO4oCoysvpsEa46Y0ZnN48LsgIURE7aMstxIkIKD3bfxvm_aT61ZX2vVBragbosxzSJOXoVfPauIU0Ihi-gbKlrMGAtwzMh4I9DbSL2JnjS1dzuDZI41MbeItgfjmTQz_9GfkJWqlc9UihfsGgVWOOMniQHKMfejaw6vtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65079">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtRrVfsZpJWMOtzVjnDmUrbpCKm4dhPbNbgLMqnzWMcCTEDs-LBhoYeI_HCxFj4mceM1r8OrVbc82tHNTxQ4R4_T-eI0TmATfrvc6xvEIB4FQBP5LdN9i4ZVt6EOMSqPOAOm1df7QBkDczRCsZBTBSkVXw4ZfUIMxZmOIciIxsbt3OfdD24TO6NfDvSP_SOjd78WCbm5JfqjMyVBD6GJNsS3i3DW63M68tqn6UubwNN9UrdwvOnge3UhGpG1h2X_ekm_w63RMi87Lkj1tlr86QoEZLyaKNEZlW66oTYpowSblGUM-GEUUG1WRnBkhBcKnfVMc6vtbGCbKre8rwfW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65076">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOEWw1Gs8EVaRd3ACoItPevE6e8fK_UOyqpSKRnx7aijexA3DFCzkpvGfKAnTDevkxa9V5ZylD4tlPe7NfFOTZcxQa9ffRBcqn3qRZcHm8Q_1kFniuW4DVgeZfXBlOqz52u1-no13x2cNTtoZ8uQlbExufufXpUwDDDcpIofRLUI75aS3c-zaad0IM5pJV5PGFvom2nEzFVBenLAnZO9aPP4WMwiOMMjhFuifcnTC1klqMYJBXZd4tnjgPE5lxyoJHtOGr0nnLw65EbIzFFEJxV1wKW0ivxKDulXiBDqcQXRntkAXGZ0Fwl1RHpijQSCV4rm3Kiao9Rgi2nIt0b2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.
این چهار حروم‌لقمه عبارتند از:
رضا تقی پور، نماینده مجلس
کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی
رسول جلیلی، برادر سعید جلیلی و عضو شورای عالی فضای مجازی
محمد حسن انتظاری، عضو شورای عالی فضای مجازی
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65076" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65075">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65075" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65074">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65074" target="_blank">📅 12:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65073">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=aHVLEYoqR-0g9ZWmrndgLjyuX1dRTafqHTxvMZg2Zf4r8hD678sqvqVPNo41AMarDiyv-jUcddh872Za68IsVSqwpd8KylzwgRNqqBrVnYF06ehLX_8aqgBXf6Iq7HPLv6jNt9nfg_PH4ruw7bBELE18Yi71bK9x0_5hhljSAAR91jkE7zk5V8c-Fd8OfR92Mob-J56LzBItzEMVzJXaX3v_wLLbg8Bh1sgA5rG_WLjUr0AGU65b80ESAuTrkxBmf-7EgpkbCSAWESQEzzlsnpaY-h2cQRs3jQ5-bzUSuFtXMlicNX_xu-MrOJaNNAVIsmhP7e1USQBiPl7H32i9QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=aHVLEYoqR-0g9ZWmrndgLjyuX1dRTafqHTxvMZg2Zf4r8hD678sqvqVPNo41AMarDiyv-jUcddh872Za68IsVSqwpd8KylzwgRNqqBrVnYF06ehLX_8aqgBXf6Iq7HPLv6jNt9nfg_PH4ruw7bBELE18Yi71bK9x0_5hhljSAAR91jkE7zk5V8c-Fd8OfR92Mob-J56LzBItzEMVzJXaX3v_wLLbg8Bh1sgA5rG_WLjUr0AGU65b80ESAuTrkxBmf-7EgpkbCSAWESQEzzlsnpaY-h2cQRs3jQ5-bzUSuFtXMlicNX_xu-MrOJaNNAVIsmhP7e1USQBiPl7H32i9QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65073" target="_blank">📅 11:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65072">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رهبر سوم جمهوری اسلامی: سه چارتا جنگ کردیم همه دشمنان‌مون رو تا ناموس شکست دادیم جوری که ویران و حیران شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65072" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65071">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
رهبر سوم جمهوری اسلامی: پدرم، علی خامنه‌ای خلف پیامبر بود و بعثت الهی یافته بود(از طرف خدا مبعوث شده)  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65071" target="_blank">📅 11:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65070">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65070" target="_blank">📅 11:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65069">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O4asf3QnU-dsW3XKW0GlKcwn_zpC0yN7aITXEIjlME8zFQlRtg6hK7hHiAkJGX8vRi71w6EdcvhwfteBWUac-15UCR7vPKqp7Biv8ZALp6TMAw3BLi9yB6_FkSYp9b4py5C4xLRkz0F5uN79Gp7RbtCQXbuR2gFsM0qZk9t7lyUlF-FBUr39UlZURLsIfDO83BoXyyqPWsRK3ON124miJ348nuKVJ7jyfT0T5vpDPwCWjxv6MxApcC-y-lAId-lSJCj1VTJmXmZWrJ3wg9HkEvb3ImCP2WzbjFC4FlBuAEYjPLeS38txNm25oXstSwG3SXfDh5z6NABEs3RPMZY4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65069" target="_blank">📅 10:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65068">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YsU-LwN6wbc7SGXe6dg3xjMmYWfG2UTBqN_mYxjshhhnHO0ky41GFabdbVtZ-ka1U-knY8YcSyZc9jZwhL0ZHpQ3YpjC1HcoNfMfu8cPauJdnECHhjAxi3Di1iHWQ6LE0rNvR1xSfsOKjSlfxjoVsEUeKeGmYeuS-tuMBqvSmENhfc0-GkdKIxfiPVQ60vAc5q-sfPoNrZFmTzA0sebcJ_QIRez92qR99B8I2PFdue5_g3ssYT88XRi-aAYK3953MNhmmDvGZeBlutTpHXpXz2c0wiWdEchsudx9tuQ1AJ42woxwmWuJuUZkB7T3_z5LVXMbO0QnZ36Y4dLNycvqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65068" target="_blank">📅 08:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65067">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErU7odRmiiQWRHAcnaxg-7j5I1dT46ZWRdoaoP7tblMeFlKcXObew6ZDOKKTLqHBSVc3LE_EKgfsbTV6WFAob9B8yDhDIlX1o25C3DqvYVV1aVxZjD6nEq3AuqCBNoAFKQV3w6lsdn4AOn-4U-954n_20p9S5_lJWqEbRz7rCmIeQwHNajp5vuc4HRBHD4SqsjmnjhO-WLrkZGyEkIAkc_accjNdUD9w1l50g7msRVF6Kxh1brA-ADEtGd0n7280GyED3T4pJqh3dx3SRc6SS3MUgrbW7QSvD5OWo9CJ5IrdALVNaO32xe5NHGbZVn4fKy1Nsqxp88nUlxASk3KCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65067" target="_blank">📅 01:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65066">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صابرین‌نیوز: امریکا دو قایق تندرو سپاه رو با جنگنده زده و ۴ نفر هم کشته شدن</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65066" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65065">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heAwN2s6Iit4D5SN7bqSHWYX_J89GjYWBTseupPLAwWX2sh4pb73_Uqp2ML6JqychNcxfQV3JolagRNrqoZyoE7KGuEm1ZnfA18lrLvlRmi5D4KemvvTiMMX3UzJpxxdmLTFl7na54CuYZQ8kxbDyDjIXRr7TxLbtAMWlTYeaJdw3uxna-q3q13KlIiL5y8AmhAWMEcXazWC8-ADdnHj126mhJjgpcy3XRUHfAEIo8QcDqocAEvISE_b6gWzTbrehHa_Gzdh_aiqP20PkFMjOjHNd_NsSHxqbqSw0r6JJLqtBbq0i3SmCWkZAGaMab4NPGe7IwVYzKcgp9fQxNb8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود.
یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل آن، این فرآیند و رویداد نابود شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65065" target="_blank">📅 01:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65064">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65064" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65063">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAeNNpUUjQ9ZBTtwTadpqVA39xcm3fIq0w_Qqh1cHubE2DotzOFJka7gU3Bbp6_UmkEvuCYjdyanX5KgGzS4JotRgU8mHHUQOAsRWfe5px0tTd8jAyU8WUQ2ROQZ7WNNM0DtXauBkdbyjYPcTjUrXerrs-vwM6zDlQ9m4vjoAzLs7lQGTzGvV3Krz_SpGryN7BDHP4Ln1seRNN7nYBVs2YiXgi2huXtg4lS37mbSXc-Yevlg_XtSkD95HUv-gA5yrQF9vl4aw2ed_peimHCEbCvqGAvfEmGU6CoCKtJbvU-C6j0AdXuQqgMm1vk4a6OD48yYaZ6TB1DUG2eioLDVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری تایید نشده مربوط به انفجار لحظاتی پیش در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65063" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65062">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65062" target="_blank">📅 00:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65061">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
📰
آمیت سگال، خبرنگار شبکه 12 اسرائیل:  ایران در حال حاضر فقط حاضر شده به توسعه سلاح‌های هسته‌ای رو متوقف کنه، در حالی که ایالات متحده چندین گزینه برای ذخایر اورانیوم غنی‌شده ایران پیشنهاد می‌دهد، از جمله فروش آن به ایالات متحده، انتقال آن به یک کشور ثالث یا…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65061" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65060">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به صورت قانونی، ما یه "شورای عالی امنیت ملی" داریم که به "شورای عالی فضای مجازی" دستور میده که به بقیه اپراتورها بگه که اینترنت رو ببندن. به صورت غیرقانونی هم سپاه رو داریم که زنگ میزنه میگه اینترنت رو ببندن. زورش میرسه، میکنه! حالا دولت رفته یه "ستاد راهبری…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65060" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65059">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
ترامپ: من به صورت الزامی از کشورهای خاورمیانه درخواست کردم که پیمان ابراهیم را سریعا اما کنند تا «جمهوری اسلامی ایران» را در ازای بخشی از توافق پیمان ابراهیم داشته باشند  @News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65059" target="_blank">📅 19:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65058">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
ترامپ: توافق با جمهوری اسلامی ایران!! به خوبی درحال پیشرفته این یا توافقی بزرگ برای همه هست یا بازگشت به جنگ بسیار بزرگتر.  @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65058" target="_blank">📅 19:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65057">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇺🇸
تروث طولانی و مفصل ترامپ درباره توافق با ج‌ا و پیمان ابراهیم:  مذاکرات با جمهوری اسلامی ایران به خوبی در حال پیشرفت است! این موضوع تنها یک توافق بزرگ برای همه خواهد بود یا اصلا توافقی صورت نخواهد گرفت؛ بازگشت به میدان نبرد و شلیک، اما بزرگتر از قبل و هیچکس…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65057" target="_blank">📅 19:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65056">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65056" target="_blank">📅 19:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65055">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhUunkXF0nudcxrTBK_T7FafjqeaCAmuzW0EkqZzCYRRwJPoAjUCuLGtCI50cyQZG9qEZ38qZxQDf8zKdpUbIIeCakw05xULnb7INTbdDxejleidRfk2L5s2aGTviQ40yOahVXEhS_-kUm5W9fOKqbAa94lWfOs-0u4NgyoHr0SYVl-DyhQ7XWbp4OjfWQXGHsxpkYGp8FC3x0HXz92DCB2UYzoFQ157X44geFgdSdcKV_HRaCL6TCHGemzq4Y6TpzaGA_oL6bIgQVXLIq5CCJwRCQh9ZOEVinG-LcTYZGtHS8yfXfg4oNz1X8uXghMbIEJRubcBRNdTuUe29Y3Asw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم  در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟! #hjAly  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65055" target="_blank">📅 18:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65054">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم
در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65054" target="_blank">📅 17:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65053">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چه افتخاری هم می‌کنند حیوون های حرومزاده...  سه ماهه حق طبیعی مردم رو ازشون گرفتین و الان از بازگردوندش، دستاور می‌سازین؟ باید رید به سر تا پای دولت حقیر پزشکیان و امثالهم #hjAly</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65053" target="_blank">📅 17:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65052">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65052" target="_blank">📅 15:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65051">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65051" target="_blank">📅 14:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65050">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgCjWDIs0gqvC72LHW_oUYOfCaUB3yGHSnLEJl-AKC8pPQKWEQWPV8Tr9ScRq5z7oBfNTSmddrmsQsLHT1jzBEMcZKMotrjF7GClAC0nFHvFTJkKM9tTq9Smue1KhoxnAcmx2aKuyqi-wnUePqUCQdgBaD9xbsB8PhABT5MTX3AruRwsxyfFAfTri0Dw7piMAKRP2LJLNwpkB4OmL79fjvRr2Lz0Na-vbF38zH8NGyXD4SEatd7yLRJqOx3YcHds3ogj4cMCx12gBlAgi7f8ghX8zqthfr_WV-to7_ZZmLy88wmleOPIxbLixRb-PVyCMN8DcvytSF38p3p4fvGEMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65050" target="_blank">📅 14:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65049">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=S38XWRSX5r1dX4vsLgmT1PzSNcUhz-T8518xg6GXnlJroWf5kaz3bAc3X5MRoalm_taUQ8cqUklncpr_xa-NN65zVDnlz7FiR1Gog5SHbw-bR-01GzB4LpeHkR0pYzd8M3xBO_22wMhOSRd7NjGoIGLHJKO1dh9lldwYFlVexIWVPmV4Ze8DV_X0BAAWlGLPfO6GGI55Jj9HhAqdf92OsQ2WjGZCCbBgiP6BvnaHl5imWyaBp44m3iJ7xhfzxMaXg3bdTWX2u6iZcmsEbyejAmz2n79ntsUh01V1z3TvS9XuiDqEiuFIRWwxHHiHAuRotuNLXLxp1AVWilUrw93C6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=S38XWRSX5r1dX4vsLgmT1PzSNcUhz-T8518xg6GXnlJroWf5kaz3bAc3X5MRoalm_taUQ8cqUklncpr_xa-NN65zVDnlz7FiR1Gog5SHbw-bR-01GzB4LpeHkR0pYzd8M3xBO_22wMhOSRd7NjGoIGLHJKO1dh9lldwYFlVexIWVPmV4Ze8DV_X0BAAWlGLPfO6GGI55Jj9HhAqdf92OsQ2WjGZCCbBgiP6BvnaHl5imWyaBp44m3iJ7xhfzxMaXg3bdTWX2u6iZcmsEbyejAmz2n79ntsUh01V1z3TvS9XuiDqEiuFIRWwxHHiHAuRotuNLXLxp1AVWilUrw93C6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد نگینی‌پور، مستندساز حکومتی مستندی ۴ دقیقه‌ای از حضورش تو پزشکی قانونی کهریزک منتشر کرده از اعتراضات ۱۸ و ۱۹ دیماه‌،
تو خود مستند حکومتی که منتشر شده تعداد بالای کشته‌شده‌ها و کانتینتر های حمل جسد دیده میشه که جنایت خودشون رو به کار دشمن ربط میدن و ابعاد بزرگ این جنایت مشخصه!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65049" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65048">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=aB9R1_RysVJ4ngMYHuEk0M7dbWVjdeNp1u84SeCcX_A28zrXzWrrbgEzQ8mXGB9Lxdpjq0POIYAeS3orjmKJF9BDfaHWFADxoZ50fV9nO830162Vt1NhtpHNugoChtsBaVtXVB2D8ADII66-RhewNWzCay2kd6UL1DLcgTKCGhFxeAaS8LQxeBBKMRLPMUYUMuI6XawQ3yPFKSzurQh5gIY8KZcShvD3Y40huRebRMMmxAKioanqIzyTFw8kBxufUy_M2FbkFRQ0veB_MOOhHvOmDSYG9giLmykqlVlsnRrKi0J8JvfH8gD1qfnZl1onK4lvxlXXitGEtYHLCUAEwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=aB9R1_RysVJ4ngMYHuEk0M7dbWVjdeNp1u84SeCcX_A28zrXzWrrbgEzQ8mXGB9Lxdpjq0POIYAeS3orjmKJF9BDfaHWFADxoZ50fV9nO830162Vt1NhtpHNugoChtsBaVtXVB2D8ADII66-RhewNWzCay2kd6UL1DLcgTKCGhFxeAaS8LQxeBBKMRLPMUYUMuI6XawQ3yPFKSzurQh5gIY8KZcShvD3Y40huRebRMMmxAKioanqIzyTFw8kBxufUy_M2FbkFRQ0veB_MOOhHvOmDSYG9giLmykqlVlsnRrKi0J8JvfH8gD1qfnZl1onK4lvxlXXitGEtYHLCUAEwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قالیباف دوباره به عنوان رئیس مجلس انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65046" target="_blank">📅 11:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65045">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai_u4_GSv5LcsVAUXJmNq9XBIDbhUZ6_0U3kfcxyKGDFWeQfIvgOJ2-P0u7R9zNSFr7PkIOKwUUGOkOCT1dDZKC5Q2fKq_JoDJS0gE_g88vNtVJk4Lyv7y50G24AyrDjGGjt_bYzPb-X1t1ouOvd6Xxe9yJVx8SGybn70M3LWrnwW0MESRJmTgRx_x3qTNq-XyDO1hKjzkfm0GbYJWsnrP-s2bbMvQQgBft0coA0VTeF5m_WQibPdAo2BIhJ3zIDmIb9TMDIl6PvbOCxkY7FS3nQYK-kBLsLmg7lyJztjeCLCaOtkPSXHpOrm3Cqtg3QsUOUmerxgZNib-rQP3mGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوج حقارت ارتش
ایران
به روایت تصویر:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65045" target="_blank">📅 10:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65044">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: توافقی برای پایان دادن به جنگ علیه جمهوری اسلامی ممکن است «امروز» حاصل شود
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65044" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65043">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام: اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.  پیوستن…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65043" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65042">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmAm3kJirOTAywztr8n7qO5X056xMeXO4YC2TNuVNMNOyg_b3FO-9kEkzenr-6S5nQPB29jUFT5hj0GTMxZuNo9pd1FSpPQMptj2rjRpOM8yArWvbX7fLpkmoF-yUWqmLuN6eCSwv4-8AuLKDOQP6iPj8nRTbyxWMAsvEbpS-13WEcDagy8mMWfR9KGgiu7hGZp6Z_vrczGC7UTKhwYc4tPrIECD90833xM5prhPLpQP2jxqNqRf8ywkbLL7MdA7Eiv2P10zFkxNcbAvnaJrdYpUT8b6f4F308_cxg22_mTBM69MW_QCk0Fo6bcRkF2kNz6427TDkscM9mkOV8pnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.
پیوستن عربستان سعودی، قطر و پاکستان به توافق‌نامه‌های ابراهیم فراتر از تحول‌آفرین برای منطقه و جهان خواهد بود. این یک حرکت درخشان از سوی رئیس‌جمهور ترامپ است.
به عربستان سعودی و دیگران: اکنون زمان جسارت برای آینده‌ای جدید در خاورمیانه است. من انتظار دارم، همان‌طور که رئیس‌جمهور ترامپ پیشنهاد کرده است، شما در واقع به توافق‌نامه‌های ابراهیم بپیوندید و به طور موثر درگیری عرب-اسرائیلی را پایان دهید. اگر از رفتن به این مسیر که توسط رئیس‌جمهور ترامپ پیشنهاد شده است خودداری کنید، این موضوع عواقب شدیدی برای روابط آینده ما خواهد داشت و این پیشنهاد صلح را غیرقابل قبول می‌کند. علاوه بر این، این موضوع توسط تاریخ به عنوان یک محاسبه‌گری بزرگ دیده خواهد شد.
رئیس‌جمهور ترامپ: در گرفتن یک معامله خوب با ایران بر موضع خود بایستید. به همان اندازه مهم است که بر موضع خود در اصرار بر پیوستن عربستان سعودی و دیگران به توافق‌نامه‌های ابراهیم به عنوان بخشی از این مذاکرات بایستید.
دوباره، این یک پیشنهاد درخشان از سوی رئیس‌جمهور ترامپ است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65042" target="_blank">📅 00:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65041">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آیا دونالد ترامپ، باراک حسین اوبامای دوم خواهد شد و دستور آزادسازی ۲۵میلیارد دلارِ جمهوری اسلامی را می‌دهد یا خیر؟!  بزودی خواهیم دید! @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65041" target="_blank">📅 22:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65040">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYlt67oXn5Jq9-puQiYKEzIDg3vFVhDTWuvXw4TGN6amdIKZaCa2IeSs_rLFa5ikR7tfYMOv2nWytqyxFPa0zk3vn9WxfdCLnLEZ7YdlP1cPJDlC0RSVfzmFbtPe4NcyyPS9Sn6Vxu3iXOsD1LegNG9vH-HALYXPyzHq6SoaAxNMCXilvqGrTR0W5O2ZJ5UVsNxz92LCTX5td6sj9sf4hNbcqPWlmlzO1OuEkeQmAk0GheD1ZAsbxj0IpLkOlDiOeRcfeFNHJXtlZxRX22JtC7SDSfMmZ3tNWPc-VBi02O3DAAtD5nvhvSIzD6_WxJ_7QnGF6pevZvzyMKG5Opji6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65040" target="_blank">📅 22:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65039">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zn_3kRmFGgOxxQ946mGS5YGa_bx7acg4A6932rINnVR9E0599AW5YyNJ9y_gLNWMc-BDbfr5vLpz75DXfKFV_A7nGgi4SswyGkz1fUFJqwf9McMiIXUFlwXIJEZsKojA3N2LdsmqBDjpBMb88zmnr7nU1qHpdbknJcSoqfV5kep9ZmGC8cqvTcj0a5m3aUn3Ne6y0BCAC27DbyIYIp5fEIL9LeVY5UzvdTLMfXVi9HEJCw3wMgWsf8QtbgEIwAOOLWS6lk2KUCrPdC5qXF0_CS2K_0x3EcdE9YdcOxBF0hOy9LlqaH6kG87VpVO7m8TnokqGtz9gEFpjrh2tfRk_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز حتی به طور کامل مذاکره نشده است.
بنابراین به بازندگان گوش ندهید که از چیزی که هیچ چیز در مورد آن نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بدی انجام نمی‌دهم
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65039" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65038">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو: توافق نهایی با ایران به معنای برچیدن تأسیسات غنی‌سازی هسته‌ای و حذف مواد هسته‌ای غنی‌شده است. من و رئیس جمهور ترامپ توافق کردیم که هرگونه توافق نهایی با ایران باید خطر هسته‌ای را از بین ببرد. این به معنای برچیدن سایت‌های غنی‌سازی هسته‌ای ایران…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65038" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65037">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: من معامله بد انجام نمی‌دهم؛ در مورد جزئیات توافق فعلا حرف نمی‌زنم، صحبت های خوبی در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65037" target="_blank">📅 17:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65036">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تنها چیزی که ترامپ تغییر داد رژیم غذایی مردم ایران بود
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65036" target="_blank">📅 15:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65035">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=YBH77t7LzLDcn-KY7cX-wcgpt7u7ShDnGbYEwTs0Zb6lPwbrciFS_OYAtX2seUds-3yiT4f8KHMvPsXwD1PVgvDty53FQz6cmC4mMhsjnSqZSDxvFjxVczKFJg5uhkAcODXJXs2809PTJ6FTv8w2kHLPA9Pzf30-HljupOGaERRzR-iKJN5N7EJnvjLf4s5iI-gadvGSfk35uJHiUs4x9von7_8uJScQuwVTPG_UL67wgSkXc6wBV988OcEKZahCXcHrdG8cA6OsYMkxpbvU6beQX4cz__fvOfYHqUqHFfqx29FBwUKVKQA-HmQL_cmWSNwO8kp-mDHhAzkaG-XRAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=YBH77t7LzLDcn-KY7cX-wcgpt7u7ShDnGbYEwTs0Zb6lPwbrciFS_OYAtX2seUds-3yiT4f8KHMvPsXwD1PVgvDty53FQz6cmC4mMhsjnSqZSDxvFjxVczKFJg5uhkAcODXJXs2809PTJ6FTv8w2kHLPA9Pzf30-HljupOGaERRzR-iKJN5N7EJnvjLf4s5iI-gadvGSfk35uJHiUs4x9von7_8uJScQuwVTPG_UL67wgSkXc6wBV988OcEKZahCXcHrdG8cA6OsYMkxpbvU6beQX4cz__fvOfYHqUqHFfqx29FBwUKVKQA-HmQL_cmWSNwO8kp-mDHhAzkaG-XRAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65035" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65034">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYZt8RgNqCyAQGsqfn5YM8a9WpZXnpcrQwi2kb7pZ8HrRaVNkHCIU-3NE4hKOth5Yn6RGn5M7L2jLD9aNxI8Ar1_2yv0dmxP7b3w2BVymzZhUE4WS4pJPv-MxQ1dbKLj6zMAjdR1jyjjsd65lss8S3F15NG_iw0lkk-aY5JW_Ac9PklNpdaFLZKKuIOKhv9VyHR2PStEhNmS2q29EZ1pAvvEXxZjlgNKpupxJun_H56sB1MhdqlOrfejuH2hFb-9LsY47igS-LI3t7Ja1qEH1lf7Bjvd8hAwV-vmKwRtdqQGZIOVI9Lcjhh6eSqs_n-nPtS_tbZR6BlgLXVZgaBcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجایند مردان بی‌ادعا؟
🗿
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65034" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65033">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مراد ویسی: سپاه می‌خواد روحانی، احمدی‌نژاد و پزشکیان رو ترور کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65033" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65032">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xb492P_Cj9sIRSRW2296zo0ey8rHCoNRESEEWhF63fAfgIXfLwlth-chO_KCyIhxuZ4sZuJxH90K5_Y_9hYmcbVBlb6vQAKNWSPE23maOTFPWMpVY70U46nBN5xwY6UmAcDM9ZGSeljDhIHnDa49hDcIa45OqnaaZyptqvEBVv7uifOPyqsIblNIyaBxByH9YisgsR3pB-rqa8tJ1hvEl3QJh6sQAtf05WgE1VH2hb4NvWF7KEuEnE2jv29xLqrO4k4dTWEMQ3pNwDuRNdlZp0RMg0SB3wQeH94k8qdXN82aeAbf4HFMiCjP4OkIyMC_wJmwpxhbuUM8kBupgG2rdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار تتر بعد از اخبار دیشب درمورد توافق تا زیر 170 هزارتومان ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65032" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65031">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
آکسیوس: توافق بین دو طرف امضا شد.
👎
این خبر فیکه و آکسیوس و خبرنگاراش همچین خبری نزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65031" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65030">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=foSrKaXIqh4hVKwOVhzeQNhoXW1SujiXhnhwGE5o9DIOPUny0aoo8VXNUU5PdaHIWp1CMGSvHE5C2zMqC-75Snj6sJsXCqncJSzQtjBhSZaMX_f34gAX5KE229BMEHQ-QbT-pHrda3C3EAmXGw1BlHRKqo2YdaU68i25qZ_1W2dyPm3HBmDKR8RR_yheq-1mKZQgco6gEvHE89Bg4XsjPU96D1h4gpE0_kJJO1nVQUCfeZQ50SL5qY5tNCLmoAix-kADyWwwhJ2SjMcljbGN8aVmExjgIBqM5lNh2liJARiHZb93GIE0q9XwCHcKZqs8DWnGEV1AMavvlxIMUrVdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=foSrKaXIqh4hVKwOVhzeQNhoXW1SujiXhnhwGE5o9DIOPUny0aoo8VXNUU5PdaHIWp1CMGSvHE5C2zMqC-75Snj6sJsXCqncJSzQtjBhSZaMX_f34gAX5KE229BMEHQ-QbT-pHrda3C3EAmXGw1BlHRKqo2YdaU68i25qZ_1W2dyPm3HBmDKR8RR_yheq-1mKZQgco6gEvHE89Bg4XsjPU96D1h4gpE0_kJJO1nVQUCfeZQ50SL5qY5tNCLmoAix-kADyWwwhJ2SjMcljbGN8aVmExjgIBqM5lNh2liJARiHZb93GIE0q9XwCHcKZqs8DWnGEV1AMavvlxIMUrVdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65030" target="_blank">📅 00:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65029">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=PM3MSrhox6xl_aBxQXwfFpw2Gv9SZmv_LkTfInmbVmQc73Xjb0KcFgnuAJrhHixWOwyDAv-GTjVwx6w10Bg11u1XF1Qc3g9AukQwD7hnH6JMnza73spWQLc2U-DZ7ZliqDdEo59RDfC6TCyf5-udyVHHEPNEtTD9DAYFRAI9Qr64goMhigB-ze5sA4qIOjEQWvqfWCGwjQ-x7NJl6or5yAlwITxuilzpBA2DHWLWylg7e9LBaLi7sk6HkIPcUGjjUhaARuEl0Z94acRLgPDjz8ktFUsbDkVSr2AmpT1Ja9jqWkYjoVmoQlGoRDgvTu7qn0xe37r97ZKHoXIuJtmz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=PM3MSrhox6xl_aBxQXwfFpw2Gv9SZmv_LkTfInmbVmQc73Xjb0KcFgnuAJrhHixWOwyDAv-GTjVwx6w10Bg11u1XF1Qc3g9AukQwD7hnH6JMnza73spWQLc2U-DZ7ZliqDdEo59RDfC6TCyf5-udyVHHEPNEtTD9DAYFRAI9Qr64goMhigB-ze5sA4qIOjEQWvqfWCGwjQ-x7NJl6or5yAlwITxuilzpBA2DHWLWylg7e9LBaLi7sk6HkIPcUGjjUhaARuEl0Z94acRLgPDjz8ktFUsbDkVSr2AmpT1Ja9jqWkYjoVmoQlGoRDgvTu7qn0xe37r97ZKHoXIuJtmz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65029" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65028">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65028" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65027">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CA2At_Z4QgJuIjdZEJdeSlKUq1Gr_FH3TyJkgCx3pjrVFOoYaFirh0isfUi-orJwIxQqPOCiXHaBQJUrbEGRpv__4BF3EUdom-DMFYFuBm8H85W83u8z0xv-z9P6TgvKAQBj9q-bOrqtbRjMr3HpUg7yAggqIlqhWVhZGpKXkz-bN-N88J4MyABf8kH2PMrJR_zzdMBUOiGjls7nrApyT24fgIilP5BB9lljKPrzwibwcvlYgerRTxBc6ZQpPouWEKo7kdaOR9IyGFgt0pEas7BByDIb0RqNM73lrq91yb9IpOFvYnJpvZU92XFxzlSbsp8E5yTiMJMrKlnOVTrhjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">بله  مگه چیه ما با ۹۰ هزار ... گواهینامه مون گرفتیم</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65026" target="_blank">📅 23:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65025">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گواهینامه شده ۱۵ میلیون تومن!!!!
الان یکی میاد می‌گه حاجی ما با ۵۰ تومن گواهینامه گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65025" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65024">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بستن تنگه‌ی هرمز در جنگی که ۹ اسفند آغاز شد، تمامِ معادلات آمریکایی هارو بهم ریخت، اون‌ها حتی چند روز قبل مین‌روب های خودشون رو هم از منطقه خارج کرده بودند! دومین مسئله‌ی شوکه کننده برای اون‌ها حملات وحشیانه به کشور های عربی بود  هر زمان آمریکا_اسرائیل به…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65024" target="_blank">📅 22:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65023">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65023" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65022">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم می‌گیره، یا از خواسته هاش عقب نشینی می‌کنه و یا اینکه دوباره جنگی برای اعلام پیروزی شکل می‌گیره، تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65022" target="_blank">📅 22:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65021">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65021" target="_blank">📅 19:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65020">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65020" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65019">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
📰
ترامپ در گفت‌وگو با آکسیوس:  در حال حاضر احتمال کاملا 50 / 50 است که یا با ایران به توافق برسیم یا دوباره جنگ از سر گرفته شود. یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم + ترامپ شنبه با…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65019" target="_blank">📅 19:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65018">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
فایننشال تایمز: ایران و امریکا به یک توافق آتش‌بس ۶۰ روزه نزدیک شدند!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65018" target="_blank">📅 19:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65017">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
📰
#مهم؛ فایننشال تایمز: میانجی‌ها معتقدند که به توافقی برای تمدید آتش‌بس به مدت ۶۰ روز نزدیک شده‌اند.  این پیشنهاد شامل: بازگشایی تدریجی تنگه هرمز گفتگو درباره رقیق‌سازی یا انتقال ذخایر اورانیوم غنی‌شده بسیار ایران کاهش محاصره آمریکا بر بنادر ایران رفع تحریم‌ها…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65017" target="_blank">📅 19:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65016">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_2vrR7EpFqHYgPxTI2k29WnPHz1hy3kM4n95RDEMDAcGELr1zWI65sl2YzoSGLIMrcxYP7MxqZcYWWSKQ0aoiy4pRZj1QNnwmcnReeOpEniJX408h4NOoFGBghAxSW3eTLJlQNkLQq8BQXbDWqFxc-tWtF-bM7rscaYFnZ4x9Iy6Ghdm9inYX1MWv7wfoZFdnZEh9YXASPdmoG0ZYz8e0b-W7WbR1irPhSVKXLtxySduNTQVtiiLHd6Lly9x_8mkDgFGCgUpiz8f13cKs2dJ4Oa66RO_bqma3XDYc309ITZR-HEQnzozv1qK_heM9S1ceplSlR3okbVukJ4QhWKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ تو تروث‌سوشال: ایالات متحده خاورمیانه!! با پرچم امریکا روی نقشه ایران
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65016" target="_blank">📅 18:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65015">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ مارکو روبیو: ممکنه امریکا به زودی خبری در مورد ایران منتشر کنه شاید هم نکنه امیدوارم این اتفاق بیفته
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65015" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65014">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=P-HWbJdVI2ELQ18SvJtRyh_aTpAluBowsQpIgfuPOIETqPVb0RKDV-Jiy0WahTUsL_AK3oRcC5waNjLHkIXNzDc8oOrsx4MIe6vbJ3Rkhsv5Jmqx7WfyAWr5Z3IRHSZ6yyG7k4SMkuaHA4WB2nhPCQKz1FZlvGBc68N8IyJI80QZAfcvYN9MBxjaqmnGaOyX21fn4_5b2Zq5MwOfPsFnEp40ohxyQDNtwKh8vFT8HmY5k3gm63pHRSgLFcj6gyj1RVCZJpr89uQt987uREHm6kXivPKzGj73SuXA1eiHjm30969PhaV0OO2Wp073kvI9mafzCrb2UlBnNwRsvl6ClA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=P-HWbJdVI2ELQ18SvJtRyh_aTpAluBowsQpIgfuPOIETqPVb0RKDV-Jiy0WahTUsL_AK3oRcC5waNjLHkIXNzDc8oOrsx4MIe6vbJ3Rkhsv5Jmqx7WfyAWr5Z3IRHSZ6yyG7k4SMkuaHA4WB2nhPCQKz1FZlvGBc68N8IyJI80QZAfcvYN9MBxjaqmnGaOyX21fn4_5b2Zq5MwOfPsFnEp40ohxyQDNtwKh8vFT8HmY5k3gm63pHRSgLFcj6gyj1RVCZJpr89uQt987uREHm6kXivPKzGj73SuXA1eiHjm30969PhaV0OO2Wp073kvI9mafzCrb2UlBnNwRsvl6ClA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقائی، سخنگو وزارت خارجه:
ما هم بسیار دور و هم بسیار نزدیک به یک توافق هستیم.
دیدگاه‌ها به هم نزدیک‌تر شده‌اند، اما نه به حد یک توافق — بلکه به حدی که ممکن است بتوانیم به راه‌حلی برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65014" target="_blank">📅 17:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65013">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73653df566.mp4?token=hC6tdSHVa2wEckXfZy_7t8DkwV7SsteVe_Fwi5zjNfpQdnGznwELMAQOKxkaVCj7cn0QnJ_K-63NF1lUgnMNjUDUHeHh6YpCHRF0L4edTzJNMzMlm2IEs1bCfFE--Vx40g_KzvrTNCtIuM2W_3Hzo4kqT7R_Wjl-duj2_NYAroppxCEkcxht_Ohk-n4sfBboQ99DfemLRUcLDIcHfytWaRwNEf6N_FRT6Aum23-LssnNnINoHsx9F5TjeBhESIBffJFaKsjtmU1yT20lvXBeBeiE7EN61InjZDZoPZTZia3az1D7u5loQYIZ2l16OsJRQBZD2KRz08RAlIAtAnICMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73653df566.mp4?token=hC6tdSHVa2wEckXfZy_7t8DkwV7SsteVe_Fwi5zjNfpQdnGznwELMAQOKxkaVCj7cn0QnJ_K-63NF1lUgnMNjUDUHeHh6YpCHRF0L4edTzJNMzMlm2IEs1bCfFE--Vx40g_KzvrTNCtIuM2W_3Hzo4kqT7R_Wjl-duj2_NYAroppxCEkcxht_Ohk-n4sfBboQ99DfemLRUcLDIcHfytWaRwNEf6N_FRT6Aum23-LssnNnINoHsx9F5TjeBhESIBffJFaKsjtmU1yT20lvXBeBeiE7EN61InjZDZoPZTZia3az1D7u5loQYIZ2l16OsJRQBZD2KRz08RAlIAtAnICMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توئیتر اکانت ترامپ که با هوش مصنوعی به ویدئو درست کرده از مجری سی‌بی‌اس که مخالف خودشه و ترامپ میندازدش تو سطل زباله :/
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65013" target="_blank">📅 15:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65012">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RvL2kCkRsLXWdI3PYLZpF_ndWLf4QrchvRoZVcFx57q72w4AA8dHuBk3eV80OGqck5mIT0iAHrF-8dnpH2lPVPlVJolmI6VD2bv4qop6_fR7o8b-p5WdMYvPxBlg5mIHBzHsC4qms0iOa0gMa1watABEWL9RKcDLU_UTjQnc7FZYuGUg3TXu-Ig9N6R1r92J5cEDsrrWaQxjp7TGfxwAERDi82WK23aqk4cUCQbXaBSjEdWD8T2JG6vDw_DSdlGkPzT53LfwkXTuNCSLWxjvg2uyzyEDM8bfdaf8FuBNHT5bFoWrVOVaIb59pocSN0_AzFoJfx5Iej-wpPVghAJ8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عروسی پسرش بود نرفته، آخر هفته برنامه گلف داشت که کنسل کرده و تو کاخ سفید مونده حالا خبرگزاری‌ها شدن دو دسته یه دسته میگن توافق نزدیکه حتی متن توافق منتشر میکنن یه دسته متن توافق بقیه رو تکذیب می‌کنن و میگن کلا حتی نزدیک توافق هم نیستن دو طرف.  این وضعیت…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65012" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65010">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jrQBUy_P2IHkQfAKpxeVnTjlYpPl2M8LiZzaY0VFgmuW6_7MXxucon7ePnRRia7ChaIKm0yOjxuJ0C7caW5G8aM7rRneDrP9LHBN6-mz8qjsPJyQ6BLZZ2Qg-yh-i2QK3mvtQMSG-_-gz2leVtJBBR7jzrBgj8dNqV8Ot-ipMkO_BQEA9YoETCg20hSJ1rRrVvOYCzMWjWJOqbQL4eq65lv32YAGREuwzZ8mZlYfKZCxwaY2bcBwqVNZLJMBaH-zt77_TjlWJ8o3iNKFrhqeAuGQfzZ7BaapJBKsqKk4_RhklNxAAKUHzh_2lBwaQCR05Mxvebs-1TaBkwDqH72kKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=oYW5BgeiJ-FMVQAg7KxnVU_MUOcb-wQsesk4Bwz0_CREP8ujUldyA_dG7VszQPQKe6Hd_yPE1Kf3808kZvX-7rA8xWihm-ZQYylM2s_DLeAYOHn4T7FJmAY-dpxVHbZXRCQEo1hUdfBoqSGCy2y2dqE73yJC0C-anx8ju-9xeiDEgogm1YRzdQo0oCtFXUNaNvWC2JBcTdWBNN4Kizl01WJn3U0kjDccnK6wRqHcJsAQZOaUV-1oVfmLA8i4syu9oJELzXjv8W6mplUcyJ5Rhc1clOljmy89E_OhunxDboNX7r-f0GLoLzonQbJhXOGtd8qMYx0lG4KlBromyByBFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=oYW5BgeiJ-FMVQAg7KxnVU_MUOcb-wQsesk4Bwz0_CREP8ujUldyA_dG7VszQPQKe6Hd_yPE1Kf3808kZvX-7rA8xWihm-ZQYylM2s_DLeAYOHn4T7FJmAY-dpxVHbZXRCQEo1hUdfBoqSGCy2y2dqE73yJC0C-anx8ju-9xeiDEgogm1YRzdQo0oCtFXUNaNvWC2JBcTdWBNN4Kizl01WJn3U0kjDccnK6wRqHcJsAQZOaUV-1oVfmLA8i4syu9oJELzXjv8W6mplUcyJ5Rhc1clOljmy89E_OhunxDboNX7r-f0GLoLzonQbJhXOGtd8qMYx0lG4KlBromyByBFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی از برنامه جدیدش به نام مای دات رو نمایی کرد و برای تبلیغات نوشت:
اینستاگرام پولی میشه ولی برنامه ما رایگانه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65010" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65009">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65009" target="_blank">📅 03:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65008">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65008" target="_blank">📅 01:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65007">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">واقعاً خوشبحال جمهوری اسلامی که با چنین اپوزیسیون احمقی طرفه، نه تنها پادشاهی خواهان با [به اصطلاح] دموکراسی خواهان دائما درگیر هستند، حالا خبر رسیده که علی کریمی و شاهین نجفی از داخل گروه پادشاهی‌خواهان هم باهم بشدت درگیر شدند
!
شما با این وضعین می‌خواین در مقابل آخوند بجنگید؟ جای تاسف داره واقعاً، حیف مردمی که گوش به پست و توییت های شما بودند و هستند!
#hjAly</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65007" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65006">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=F8muKAhw2GFVIdemuq55EF7E6cg_LpApB6uOcggOoA3zPVQA91bMoaC3bJT9aHmH5E7S-fwNqQQ1hfhqAp9KVp7cK3jKxSZqtPQGtjiRh8GdBndHjMuZGuXMjywM-ELrv8c-9-yGSxRJsdF_aMWq0SpX9XAaKK8WnHV7HbPVxhKXdbioyhP3pPjG5lutV-MWcUl6rwKwvTcEluCuJYxQYgDv6ukjj7gIuW6IiRmr1lUrrIMfkHH4oxaJPEDyBmfsOqyhe5TPas68wj1PJjQSyvqfkj4oeajM1qLP-RWi-pAnEV-lTQTaMPXIdQPAO9UOUrRvRzem-kYHX_Vtu2ZRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=F8muKAhw2GFVIdemuq55EF7E6cg_LpApB6uOcggOoA3zPVQA91bMoaC3bJT9aHmH5E7S-fwNqQQ1hfhqAp9KVp7cK3jKxSZqtPQGtjiRh8GdBndHjMuZGuXMjywM-ELrv8c-9-yGSxRJsdF_aMWq0SpX9XAaKK8WnHV7HbPVxhKXdbioyhP3pPjG5lutV-MWcUl6rwKwvTcEluCuJYxQYgDv6ukjj7gIuW6IiRmr1lUrrIMfkHH4oxaJPEDyBmfsOqyhe5TPas68wj1PJjQSyvqfkj4oeajM1qLP-RWi-pAnEV-lTQTaMPXIdQPAO9UOUrRvRzem-kYHX_Vtu2ZRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امتحانات نهایی پایه یازدهم و دوازدهم تو بازه ۱۵ تا ۲۰ تیر به‌صورت حضوری برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65006" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65005">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65005" target="_blank">📅 21:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65004">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
العربی‌الجدید: سفر عاصم منیر به تهران دلیلی بر توافق نیست و پیام جدیدی منتقل نکرده است، گزارش‌ها درمورد مفاد توافق گمانه‌زنی است و اختلاف بین طرفین هنوز زیاد است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65004" target="_blank">📅 21:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65003">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
📰
العربی‌الجدید به نقل از یک منبع نزدیک به مذاکرات:  سفر فرمانده ارتش پاکستان، عاصم منیر، به تهران به معنای این نیست که توافق در دسترس است. گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و صرفاً گمانه‌زنی‌های رسانه‌ای است. وزیر کشور پاکستان پیام جدیدی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65003" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65002">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
📰
العربیه: طبق منابع العربیه، انتظار می‌رود پیش‌نویس نهایی یک توافق احتمالی میان ایالات متحده و ایران که توسط پاکستان میانجی‌گری شده است. که ممکن است ظرف چند ساعت اعلام شود.  شرایط کلیدی آن عبارتند از: آتش‌بس فوری، جامع و بدون قید و شرط در تمام جبهه‌ها، از…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65002" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

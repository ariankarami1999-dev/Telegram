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
<img src="https://cdn4.telesco.pe/file/KDIB-OpKxWbzcQ73by63KZ5p0-gH_QO0gOl7ZGP6KyJ0uR_TBdImavC3tN2lYUGtA1XqZZQljv8B3U-AAOSlN1ZtJvI2UXsMIasv737eGp6tlLaWyvDTj5gP5wbkv5qsAdeD9dYIRH3gfIR52qqaz0Uf6mv9Jdo9zwfFVfSIGkcQJBJx3Ss_ivQrEGbEPyaVhzU_pEHwvdKwWKeklafrEAlW1vTUZpX56HKBTRDwxAa7rLTWtoS2geui-QGlos9a242z_0xKvK95e6bChi_CdWgJBmPRYUTWIxdtfo4OnrmkPYZ6OLSzMxvkf2N_svoZ---czDlwOVSC4UKXHp0Kbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 17:45:14</div>
<hr>

<div class="tg-post" id="msg-90318">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e86b9dc9.mp4?token=LL9oS5UmKv_tHzo01dalNKhqLs3T8b2Is5l5apw4d8WsL-TwVmVwmpT4X9QBhqByJGD-NV8TAWS8-Wbi0AqSAKRgK9IvqPa5pVgDIza1RyWuDEPZMYT1wNw8qElL82WVFeWGEVddbWmPM1QDzPkneZioK3atqos6xk1pL4JwrxXls3jK9p1JNXX2EFSiIERL7rgLXHFJ4--C_5j4K0TMuxyl0omI0lCQqv_VLgI6XZNuEO8jmlxTckmeio3PvY1hw0cs7y4hb0KCaoR8Wx1Y-Coq6_qO9ZfQAp6lRoBtBIMDStEjQzyEQWdgsd0RHELFD1fEYqBH99UnYiSnCsQ2zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e86b9dc9.mp4?token=LL9oS5UmKv_tHzo01dalNKhqLs3T8b2Is5l5apw4d8WsL-TwVmVwmpT4X9QBhqByJGD-NV8TAWS8-Wbi0AqSAKRgK9IvqPa5pVgDIza1RyWuDEPZMYT1wNw8qElL82WVFeWGEVddbWmPM1QDzPkneZioK3atqos6xk1pL4JwrxXls3jK9p1JNXX2EFSiIERL7rgLXHFJ4--C_5j4K0TMuxyl0omI0lCQqv_VLgI6XZNuEO8jmlxTckmeio3PvY1hw0cs7y4hb0KCaoR8Wx1Y-Coq6_qO9ZfQAp6lRoBtBIMDStEjQzyEQWdgsd0RHELFD1fEYqBH99UnYiSnCsQ2zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في تعز وتسيطر على مواقع استراتيجية بعد اشتباكات مع مرتزقة السعودية</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/naya_foriraq/90318" target="_blank">📅 17:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90317">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">القوات المسلحة اليمنية تعثر في باب المندب على احدى سفن العدو الامريكي والاسرائيلي التي دمرتها القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/naya_foriraq/90317" target="_blank">📅 17:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90316">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات سمعت بوضوح بالجانب الشرقي من السعودية</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/naya_foriraq/90316" target="_blank">📅 17:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/naya_foriraq/90315" target="_blank">📅 17:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90314">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354f2e2cdd.mp4?token=LccoP2RjHaKbA0SACbpVj0OPd4eYZWyhG3bCASpmYGnY-YUFE52l_i0x0cABmsg2nHjnkWsdzFAuCFgwzD_0-D9Rg86oFBaHceQPlm7JQqDmCS1odVir8x_v3ZOSFmS4pJfZ8HmzzfNe3B9O0nWghtbekBMEZcYwVM4c7l9RbglxA-Dg2GDSPCB5AEBL2-e09y40QIs-6YW6IW-zOv-TjoQ-Km4k5CBS-VEPvtdzy6-SViM_0f8fGZNQ_EaqQzVdGaR5zGe2SRRErfL1oztKf_HYHjF_4IbYlqfotFDObv8GeATxBltE27dGAMfoSbpJ5CNBp0gZKgskq2de0B-DgwnC8b274143NjzAFH2dw_MT9kZrRUjvr7l3pG-11s8pt0fkNx2nMXy1guWCtsBUS67xwhRyirlso8HGP5joQKy3ebwgmMg2vfIk-qlVgMxf7cUzOMz1__ZtIFj60-Uxkg2TQBmYWbJLChhV88HGqrWc_E9YeOR0sFX8bpgS17HAvGmEDcU647fEdVP2fvaNuN4VC6nHc6FXkw_tz85_uGRPl4aBHhq9OIiNA4i9s8bmES10FGBQ1KDTpwTZbS1RXY0-fGiPX1VyPhnMj0mJEPeVqCX7Q2Dw8UHvk-vN9El-1adIt4wZQZlJbw6oYFdLZy4oss-_KyXN2IbcrNqTxEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354f2e2cdd.mp4?token=LccoP2RjHaKbA0SACbpVj0OPd4eYZWyhG3bCASpmYGnY-YUFE52l_i0x0cABmsg2nHjnkWsdzFAuCFgwzD_0-D9Rg86oFBaHceQPlm7JQqDmCS1odVir8x_v3ZOSFmS4pJfZ8HmzzfNe3B9O0nWghtbekBMEZcYwVM4c7l9RbglxA-Dg2GDSPCB5AEBL2-e09y40QIs-6YW6IW-zOv-TjoQ-Km4k5CBS-VEPvtdzy6-SViM_0f8fGZNQ_EaqQzVdGaR5zGe2SRRErfL1oztKf_HYHjF_4IbYlqfotFDObv8GeATxBltE27dGAMfoSbpJ5CNBp0gZKgskq2de0B-DgwnC8b274143NjzAFH2dw_MT9kZrRUjvr7l3pG-11s8pt0fkNx2nMXy1guWCtsBUS67xwhRyirlso8HGP5joQKy3ebwgmMg2vfIk-qlVgMxf7cUzOMz1__ZtIFj60-Uxkg2TQBmYWbJLChhV88HGqrWc_E9YeOR0sFX8bpgS17HAvGmEDcU647fEdVP2fvaNuN4VC6nHc6FXkw_tz85_uGRPl4aBHhq9OIiNA4i9s8bmES10FGBQ1KDTpwTZbS1RXY0-fGiPX1VyPhnMj0mJEPeVqCX7Q2Dw8UHvk-vN9El-1adIt4wZQZlJbw6oYFdLZy4oss-_KyXN2IbcrNqTxEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النقطة الاهم في العالم - مضيق باب المندب</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/naya_foriraq/90314" target="_blank">📅 16:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkRdcCEu-_jdvWfLHG-Jmjeh5Wb-4qtdhHms7GFW-SI32XI8rULAITYzYj-tyqeEAah2bmnBS7aLY9_-LUDXExRU9qtgpbkn1n6WBEFqzXYca4EZemgYU2130kjroIYs4qI6QlQ41po3vhKA3mVxKB3dJy_G54uvqf8MtlO7cLUZ6iXgIXfNK3zYcK029qEe0Nhi6oauTlf6COQAiSa1zB7TUFTOecjcWRR5V2nZE-QmQXreZgB-Tu6ltWocjPQhIsFCalFyKF7Ytcky6CT1rjgacKOSe48ppQ4xoFhSDCA0DkHGmZiD6i0jyolGGspVcmYtlKlFL8ez77kDFRKr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZD1q5hPu7tPOD9mytmJ4ztZdlTNdgL4U9uWCT5JYp-gD9C0PJyqx4uX-zRWoX_Mt-FhuLNfbGIszfe40Hz33CfYZc3jx5YTE2Z2R5J0AriZ2UQXh1tlAlSQCFxQ_kqSf_rshK0sAAeR7lqIcF7ECB3ori-83NTFbktoWbCzSL1fXnMgRLebR8Dr_wWS1kw077NbRlSUzaBm_kl-s-047FiaHtdrl-Z8GbLe0ZE6owMcedsHWh5XCrS7qd7NY0KSaedXjglQJm8vB4GmeXyq1sPfxgPus0vDNeDAN20VNJ9zGohKEg4mO2ON9eMk7vkwpq3IxYz20OUbBJOMxNyNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUsYoLM-72KswNoia4xwrJOzo8S2JRRrKqWER57hUdDN97aXBt-zggLR5hRHOfRq1AWOcig4i1N9JUofJ02UoAfoeV9Wufa7cVXU_YzOnN-K2J6ymazqPHEnpu3ibLKsmnJ9-qfllE8uHoyMDVdDrAMcM0unm3YLbFEwAaNTXONfjxEf2RwAmqUuorVJimu9xrsNxVHfMsxXt_VF3FhsEz0QnJSoM9dRIx2WMj3T7xV8p5WMfGZWmYhjkncZDkXilC_yOXjCYeWBeK5d0r0qUHOflnrVH5oDNnQlrMnYuTIGHFKcVhkujiIN6NhQ4tAQW-rbEnnDn5a0HflbifDafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BObLPwF21YqYyU-khCaRtXno5ZZMYsKeKsQgaPvk6Oxi-NMVoTxbTJV4kHmReuhrHSfAuiUk49OU4vpOOp0OW-3mQRxS60xDAXVmA6k7QQWj7kGDhFj_kSzxyXZyXYT2pIchOC96-YoY2Cni0QiFdnw2tPiPUST_-xWPv8yU-lpj-u_Ee1HDahUphZnY2TgxZBneToFs7gF-k4hM4q4TCKSRX3DZ8pov-N9vzB5gb77o30qtfIzQnuPXOV7tBHzy2hq-lyvjzgnEDJWTzocy0G9FT494EZdPrIWQKexwzLmXIqUoCkzgEB21pyDY3g4Zeq-S6n0X559OFHiPgbsR8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد ادعاء المرتزقة يوم امس انها سقطت بيدهم.. محافظ البيضاء التابع لانصار الله يتفقد أحوال المرابطين في مديرية الزاهر.</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/90310" target="_blank">📅 16:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
🇮🇷
مكتب رئيس الوزراء العراقي:
الموافقة على طلب الجانب الإيراني لإجراء تحقيق مشترك بشأن العثور على منصات إطلاق طائرات مسيّرة قرب الشريط الحدودي العراقي الإيراني.</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/naya_foriraq/90309" target="_blank">📅 16:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">المدن اليمنية تواصل استقبال الاسرى المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/90308" target="_blank">📅 16:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: خطط لعقد اجتماع إقليمي يضم العراق ودول الخليج الفارسي.</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/90307" target="_blank">📅 16:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">استقبال يمني رسمي وشعبي للاسرى المجاهدين المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/90306" target="_blank">📅 16:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90305">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
🇾🇪
نائب وزير الخارجية اليمني:
النظام السعودي يسعى لتخويف المجتمع الدولي وتضليله، ونؤكد التزام صنعاء بالحفاظ على سلامة الملاحة الدولية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/90305" target="_blank">📅 15:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90304">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇷🇺
السفير الروسي لدى اليمن:
نؤكد دعم بلادنا للجهود الرامية لخفض التصعيد وتحقيق السلام في اليمن والتخفيف من المعاناة الإنسانية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/90304" target="_blank">📅 15:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90303">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">التلفزيون العراقي يقول ان لجنة أمنية رفيعة المستوى وصلت إلى منفذ الشلامجة للمباشرة بـ"التحقيقات في الخروقات".</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/90303" target="_blank">📅 15:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90302">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">استقبال يمني رسمي وشعبي للاسرى المجاهدين المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90302" target="_blank">📅 15:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90301">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv-kuoiPT4GY5VqXPoUFb_TBkFOMDdWpRtNi5ZEv5Og9_qcRA5yuVSw6mehSBuuXvaLNsQHvMKkOKLxFdfm3Cblgh66p33hrru1EU8HNO5iMHSw5gOMDzd8g8S1iawdPbQ0NGxmnDdM56d24mMpRf4Y18OWfVykIfEBtZYFII8icf-vBSPDl1EuiWGCx-_HwHKUmRwMKA4Gl0k9iQU1mMgMLIBMfGzJaBZwy2soJnjiFtp44bAA2Ku_6xZAbTZaGVKcv599-IVUHBP0BcoCjwGdC05VywsVy7uVbG-gLKRHXq6T6iKJUUFpKrITLhA7D3UCZbZnSnK0EkK62APeq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90301" target="_blank">📅 14:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا مشاهد من عملية "والله أشد بأساً وأشد تنكيلا" العسكرية النوعية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90300" target="_blank">📅 14:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اعفاء قائد شرطة ميسان من منصبه</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90299" target="_blank">📅 13:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اعفاء قائد شرطة ميسان من منصبه</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90298" target="_blank">📅 13:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رئيس الوزراء العراقي يوجه بالسماح بدخول العالقين من المسافرين في الجانبين بمنفذي الشيب والشلامجة الحدوديين</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90297" target="_blank">📅 13:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90296" target="_blank">📅 13:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12c317f4b.mp4?token=FiWFqMdsas9ZMMTbgPD6h2MNfeRcnVoj06hkzNyCFW11-o1EmfVLxlfso4-ArODtPXUOzIO1z1iySJXVTU5ioW4W3_m-ovsx1qKdvS4Xw_Y2o98xCPw8LJZ57ckaYznTh9_PQY-7bG9MqO2ScxSdEk-_0IU_0Fu3_G4anh3jvspXnw7fWYTZvoU7D7WM95qON-EQfwd6mnSQ5_CKb0rVsteTzqvo2Za1-Mg9Fxy6QqoD8JFiEP1MFg-RiFTWwje3hKOy8SOaBXIB6UCIHSx19Zj6MV4ur07H7c2GEM9E15R0SZcQHHRoX8SnA2TY671hIeM6Chi_76KuFIrERLOslBthkE-teyWrnG_tohjWzG_kyccC7XMQ1E7zgOqGplekNzaTewZhGnQzH1-Yv13ZMHNvJJqMtQ5YbLNCeJ5y0bVTaG8kDdAma3ycdrDAjRrJu7y-EQqgKPid4wVP3xUMhMuMU6F1X-EkxtBqxuvemR5-Ub-xcUDb9h_XnnSmBfPXigByAgW_dUiSX3RKInCK0JrLPVWbpIbziDeRnKIY_FwAUdNyV7Waqf9fQrC1vEM4SoTJB0Zy2BuYVwzA2h2n1k9akybVAu3LJVc5nsFZ-uoHiXyEx0xPxU2-T_JBFCrFgz1wFCjkE6xt_1gLq-Y6-9B8w-m9gwy0ryGdCb1e7U4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12c317f4b.mp4?token=FiWFqMdsas9ZMMTbgPD6h2MNfeRcnVoj06hkzNyCFW11-o1EmfVLxlfso4-ArODtPXUOzIO1z1iySJXVTU5ioW4W3_m-ovsx1qKdvS4Xw_Y2o98xCPw8LJZ57ckaYznTh9_PQY-7bG9MqO2ScxSdEk-_0IU_0Fu3_G4anh3jvspXnw7fWYTZvoU7D7WM95qON-EQfwd6mnSQ5_CKb0rVsteTzqvo2Za1-Mg9Fxy6QqoD8JFiEP1MFg-RiFTWwje3hKOy8SOaBXIB6UCIHSx19Zj6MV4ur07H7c2GEM9E15R0SZcQHHRoX8SnA2TY671hIeM6Chi_76KuFIrERLOslBthkE-teyWrnG_tohjWzG_kyccC7XMQ1E7zgOqGplekNzaTewZhGnQzH1-Yv13ZMHNvJJqMtQ5YbLNCeJ5y0bVTaG8kDdAma3ycdrDAjRrJu7y-EQqgKPid4wVP3xUMhMuMU6F1X-EkxtBqxuvemR5-Ub-xcUDb9h_XnnSmBfPXigByAgW_dUiSX3RKInCK0JrLPVWbpIbziDeRnKIY_FwAUdNyV7Waqf9fQrC1vEM4SoTJB0Zy2BuYVwzA2h2n1k9akybVAu3LJVc5nsFZ-uoHiXyEx0xPxU2-T_JBFCrFgz1wFCjkE6xt_1gLq-Y6-9B8w-m9gwy0ryGdCb1e7U4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90295" target="_blank">📅 13:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlPIee51qYe7KoHMBT4itfUImadT3i-u4pjXKcKonrvO4QxLaqz82dsd3ItVJuT8oRiXs7X4cX7yX0UcBXn2KBYV0fI7xTWuP9FKybp4TqBVRs-KBnwY-WZS96Z7b5qutE-NLPDS-CidQe3IhqIU0Yt7JDeoAKxwsxMJJ5PZiRXNVMGXkqLNdHoFEHdspNoLVF8u_Br5jOsG7zwiW6Tv2abs6wZrbO8LYl8jZgsxOi6iuE3YFxtAWCmb7PJ-HXcou3JuiY72-RZyHvg_Xdw8XnkDaW66DNodrneh1GxcIadyYj4VY_CpmsfZKWV2Ztaod3pUcQ0hDyvcp8Vf-dNJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
رئيس المجلس السياسي لحركة النجباء مغردا:
نشعر بالفخر والاعتزاز ونحن نرى هامات اليمنيين مرفوعة بانتصاراتهم المؤزرة.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90294" target="_blank">📅 13:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38811a403c.mp4?token=eukRn69TQ2osOHJDXV3dz2IAGzaxcltHeSvYPRwOc8nfc3_6N2jXFLD-OsPeOaUgjgnOznoJXorG_yBCbolY2CBWv38pbLB9z0ilwe_irndmkkKxIxJfZA49nQ1bJMZPhBPfUyojJD2MJcwvuHQj6UOCCVtt3u2cSE0n1wPhyKghykCbJOQJdMa1qYt3GApvxeoqndxBZiWlphuVIGVx9dbRVNNwluJpP-Z7DOdJvMChyRK4agSUkk8Rg4wkjNhEcIbDXcpTClRJjjqp77k807iBiIW_lzF76cnYo7xVIwYSwlk66ujUAlRnPwPtETFIk5p4Fq5o0NBpM0IaGx9L4rKJtLZMQ2rqGPUZzbdc0jt5FyeXy1iOYy8ryTC_Lhd6dCo1qqgermHJrbnC6i-_M0OiUbWzR9VMrTl3HvcZ_pTd2NNf4bGUc_fhP7CmXTvPWdSHLvEw6NMNagQGbvAH_oLroejTGtAes50eovqugk8BOAyaG1xI_fJHBgpOgJAMg5PqwqIjidbDSKxixpc6Xnkugh0O7CL2IwNzJTn9vCFPBXahN0cpneBBT6hTOeSK2_tu_wTA2FCZDt68ghEC1Ld10irqroPyxYvzwNv7swuYr8jdwvf-05HQEv4YDig_0c9aoe_BzJPsOqHh_Btq0tIgD3G6hcJv_Yi_n0mq17U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38811a403c.mp4?token=eukRn69TQ2osOHJDXV3dz2IAGzaxcltHeSvYPRwOc8nfc3_6N2jXFLD-OsPeOaUgjgnOznoJXorG_yBCbolY2CBWv38pbLB9z0ilwe_irndmkkKxIxJfZA49nQ1bJMZPhBPfUyojJD2MJcwvuHQj6UOCCVtt3u2cSE0n1wPhyKghykCbJOQJdMa1qYt3GApvxeoqndxBZiWlphuVIGVx9dbRVNNwluJpP-Z7DOdJvMChyRK4agSUkk8Rg4wkjNhEcIbDXcpTClRJjjqp77k807iBiIW_lzF76cnYo7xVIwYSwlk66ujUAlRnPwPtETFIk5p4Fq5o0NBpM0IaGx9L4rKJtLZMQ2rqGPUZzbdc0jt5FyeXy1iOYy8ryTC_Lhd6dCo1qqgermHJrbnC6i-_M0OiUbWzR9VMrTl3HvcZ_pTd2NNf4bGUc_fhP7CmXTvPWdSHLvEw6NMNagQGbvAH_oLroejTGtAes50eovqugk8BOAyaG1xI_fJHBgpOgJAMg5PqwqIjidbDSKxixpc6Xnkugh0O7CL2IwNzJTn9vCFPBXahN0cpneBBT6hTOeSK2_tu_wTA2FCZDt68ghEC1Ld10irqroPyxYvzwNv7swuYr8jdwvf-05HQEv4YDig_0c9aoe_BzJPsOqHh_Btq0tIgD3G6hcJv_Yi_n0mq17U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لغنائم القوات المسلحة اليمنية من مرتزقة السعودية بعد فرارهم</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90293" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8TEKzsZ4j92gC73CsahLtydwFWN7qWYiXwb28vYigM_8JJOOrJcqJxZ_duY5Fx_Sy_B2UOBwMhIgU9LNNmwnBsqPVgNYIPC7u28tXHkGYwoca6vQy5nfgoTjbzn6FVXqOGXe1tMeaV1sw4Hvc0fE6W7ch2unAlpl3iokzyRIVd4VrnJBCsZ4MhOQSxk7eTTNwyeuHm91vs1GPq9loWw5QZzRUh3TL4Qc68YeFa-UUrmY1dlfd2-VI86myDdbI0hG3Y3_T725PIvBqn9f8r_U_bj_0eHMVjuwXoQ_N4DITq-nmpeBtBUDOjzomf2Dp1OcSl5CPUGHUzgl2iaQwxi9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
​في الوقت الذي نبارك فيه للشعب اليمني الأبي انتصاراته الميدانية المتواصلة ضد القوات السعودية ومرتزقتها، نؤكد: أن الاتهامات الموجهة للمقاومة العراقية بشأن استهداف المنشآت الحيوية السعودية يوم الجمعة الماضي هي (شرفٌ لا ندّعيه)؛ ونُعرب في الوقت ذاته عن استغرابنا من تسرّع الحكومة العراقية في تبنّي هذه المزاعم دون الاستناد إلى أدلة موثوقة أو تحقيقات ملموسة.
​إن تكرار سياسة إلقاء التهم وصرف الأنظار لا يعدو كونه محاولة فاشلة للتغطية على الهزائم المتلاحقة التي تتكبدها القوات السعودية وأدواتها على أيدي أبناء اليمن الأباة.
​وإذ نجدّد تأكيدنا على الموقف الثابت للمقاومة العراقية في مساندة الشعب اليمني المظلوم والمحاصر من قبل النظام السعودي منذ أكثر من عقد، فإننا نحذّر من الانجرار خلف المخططات الصهيو-أمريكية الخبيثة التي تسعى لزجّ العراق في أزمات لا تخدم إلا أعداءه.
​وختاما، نُعلن استعدادنا  للمشاركة في أي لجنة تحقيق حكومية بقصد  الوقوف على الحقيقة، بدلاً من الانسياق وراء الروايات المشبوهة.
المقاومة الإسلامية في العراق
12 أيلول2026</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/90292" target="_blank">📅 12:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae1f3afd.mp4?token=jDmQOKgno-koiuFugfuK8UiIJfOUReUp0WmU4KLZWHpXuC5wbOG2CecjsYNUp7Bx7617OdT3Xij3or9gK4V--SeAlVbzUxl3khsowYpn8FEIV4fhyE2zU4w6rETGg0wtTwbDlRcId8Lttw6T_pGK7L_EQf4L23HbMl9UhAgDxLNDpuScFDoTKUi6ZQaPcfD7U55whyF15jJqFUD46c93vc9c1SJM-6XutuzKwpJ023XBWz3RPGSCHL0U411hSCy7bYUEdwfFrRQ-YTvw9sj_jHdBvReC1kevo5H5BaaDBsoqk60ncYnfIJhE-Fhd8gkjSHV0nCwTrulORF2LfkZGdEVYYtjZWoh_j7wUb9eWx3OOowm-emGOmdc01-vheeK03TdKqhWYGUhoeQIQ_CyijXtkq-0YmkXCiwwe20_FO8FBZulWzUncg0hZOiGxVBGVN-3VBcxmlOY08OGkPxQ53Z87fsmEuzF80FHIYXIjhuZdbV1m637jQv1Gg056mXDXdsQNjrWjJEuBRYSgv-hjlVfE2vUEd5r2zwO8r-P_Vih9qjIndzjZRa1tzXm0C-3qbw5C4AqH7Iwznw_S9BwbwvYvzGQXY6132tqcr2_StFbQrNOE4ejWFvHg7h4jdxuBfmMdqiea7CeJ9Jqnd3kP86_1BokyqAC1TLWQnIiko7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae1f3afd.mp4?token=jDmQOKgno-koiuFugfuK8UiIJfOUReUp0WmU4KLZWHpXuC5wbOG2CecjsYNUp7Bx7617OdT3Xij3or9gK4V--SeAlVbzUxl3khsowYpn8FEIV4fhyE2zU4w6rETGg0wtTwbDlRcId8Lttw6T_pGK7L_EQf4L23HbMl9UhAgDxLNDpuScFDoTKUi6ZQaPcfD7U55whyF15jJqFUD46c93vc9c1SJM-6XutuzKwpJ023XBWz3RPGSCHL0U411hSCy7bYUEdwfFrRQ-YTvw9sj_jHdBvReC1kevo5H5BaaDBsoqk60ncYnfIJhE-Fhd8gkjSHV0nCwTrulORF2LfkZGdEVYYtjZWoh_j7wUb9eWx3OOowm-emGOmdc01-vheeK03TdKqhWYGUhoeQIQ_CyijXtkq-0YmkXCiwwe20_FO8FBZulWzUncg0hZOiGxVBGVN-3VBcxmlOY08OGkPxQ53Z87fsmEuzF80FHIYXIjhuZdbV1m637jQv1Gg056mXDXdsQNjrWjJEuBRYSgv-hjlVfE2vUEd5r2zwO8r-P_Vih9qjIndzjZRa1tzXm0C-3qbw5C4AqH7Iwznw_S9BwbwvYvzGQXY6132tqcr2_StFbQrNOE4ejWFvHg7h4jdxuBfmMdqiea7CeJ9Jqnd3kP86_1BokyqAC1TLWQnIiko7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من محافظة الانبار..
ازمة الوقود مستمرة في مختلف المحافظات العراقية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90291" target="_blank">📅 12:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇨🇳
🇺🇸
ترامب بشأن الرئيس الصيني: «يقول البعض إنه يتجسس علينا، لكننا نتجسس عليه أيضًا، ونحن جيدون في ذلك كذلك. نحن على علاقة جيدة. حقيقة أننا ننسجم معًا أمر جيد. نحن نتعامل بشكل جيد مع الصين الآن.»</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90290" target="_blank">📅 12:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9397297397.mp4?token=oHiS7oe3n00gd3lf61Qdjytm7SDvxMy1jD0IJ_GiNlUt9FyahBAnsGCh37WCy37K0N_cI27Y1D8zlIzInZus5Y-rub349aFWQuS9F0aKgpFyqshfqZ73AMRk2m9dgrknQD4l0O4Slamjt7FuoHFYTgZUWzYJf6qmL_-WNN7ltxZHlSzRRSYwYQA6g8UsZSxr0rQ55U5qDc26eT4Q1boPM4BloNLs1nVW2TzCxfEnfdarYitHvU9jq1GMseveK8D8xj0a86pVf-3LWqPNuiQc5kldmHiq-iiEbXCqGedMuYqSMuvuVP-it06ZahpB91XdjAAimD4TDIj6quk93ULcqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9397297397.mp4?token=oHiS7oe3n00gd3lf61Qdjytm7SDvxMy1jD0IJ_GiNlUt9FyahBAnsGCh37WCy37K0N_cI27Y1D8zlIzInZus5Y-rub349aFWQuS9F0aKgpFyqshfqZ73AMRk2m9dgrknQD4l0O4Slamjt7FuoHFYTgZUWzYJf6qmL_-WNN7ltxZHlSzRRSYwYQA6g8UsZSxr0rQ55U5qDc26eT4Q1boPM4BloNLs1nVW2TzCxfEnfdarYitHvU9jq1GMseveK8D8xj0a86pVf-3LWqPNuiQc5kldmHiq-iiEbXCqGedMuYqSMuvuVP-it06ZahpB91XdjAAimD4TDIj6quk93ULcqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇺🇸
ترامب بشأن الرئيس الصيني:
«يقول البعض إنه يتجسس علينا، لكننا نتجسس عليه أيضًا، ونحن جيدون في ذلك كذلك. نحن على علاقة جيدة.
حقيقة أننا ننسجم معًا أمر جيد. نحن نتعامل بشكل جيد مع الصين الآن.»</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90289" target="_blank">📅 12:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
مديرية شؤون المخدرات العراقية تعلن ضبط 150 كغم من المواد المخدرة وضبط 3 متهمين بينهم أجنبي بعملية أمنية في مياه الخليج الفارسي.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90288" target="_blank">📅 12:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
رئيس وزراء العراق يعفي قائد عمليات ميسان من منصبه، على خلفية ثبوت انطلاق الاعتداءات التي طالت المملكة العربية السعودية من أحد المواقع داخل المحافظة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90287" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvCdISbTUmfGdcx6OXocSU4fqPT7CYNL2twyx4IZE3ulpCRWqI_kbi6mxuopCLf54FdPJiNqsSUvoHdhmJkITqGK0LSoiCKgVc9h_Snq-IUGq-8ERvCAyadAzsD1UCmrZnGndITPPvbdmgh3UVA37SlXyR-HOxQSvY7HeHovdo185WCESXQNUSqrHiK-kjZ5WJhAC4B60qw9sH7U0AdpTG45fFhxN-vat88qCjQGmkQPv1wlfkqdhmMEN9PeYdJXKaHc0KeNiPMGJ9fTrrNJHHt0LuptzX0z2a4FIuW_MBH8NhBNGTGY4zJQeHXLmYSKP0ncrEHet8SSl1Wc5KQZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
طائرات النقل العسكري الاميركية تتوالى في الهبوط بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90286" target="_blank">📅 11:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
مصدر ايراني...
انفجار مسيطر عليه في محافظة اصفهان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90285" target="_blank">📅 11:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKd2MNWRdpqCc9IX9G340O5O3bWcsz-qo0M1IUXhzKj004GJQhDxrD04-T1rzOHdDH48SVAvMrc5_4fU1FZ3g2hX6K_GtznGFYpuAzlz7OlLl9emcPUfhuF3F1NO-E_eFLH2v-9xH8Oye-Ivd0KEJJpTssLb0lXmFMijEas6Gq9BEI6NReu8SKt1ArpZUq2H8FH4YHWi9D40FgksYHlGvwfzRrJjBzZ34xX607Qyu51QJeRtFDtgEjE9k2zQkYFiRKcbuC0wnauJfJKw3EdVFMowUydw84W_wScOhmso5bd3X9CyU466rLNSxkj89ZJPvSoHRrn2JNbDDEPkdxgN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpFULMh73AFxsE6y3DB-JbAcrXzFnV10wKCZkyaf55PgFX2XOgQ7B-Y0MWqZIbAPA87QCTpZ79uUgUSSXnOb1nZ6QQrWAA80jGZohj73tS8iRfYkXEsHcCcOuqkhBBbhYBvjc_-2ErGIJ93ECW21giSDZ7IrhN373YtYrHO7G5mWPHx48C8b9BKWlO_uS5wsS6VScjTfDk0_kRjMbpUyhWintlu-koIO2YKfrNIw3e-flGFIuMzTZfn2y7er21rUe1z9bcz-UTmApTRtSaPv89o217mty7M8ahNka1OvTCzaG996qvus0ZR9teGCFbrlR2txeQyubKKbFQhK_dF-Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
لليوم الثالث على التوالي...
استمرار اندلاع الحرائق في حقل خريص النفطي التابع لارامكو في السعودية بعد استهدافه من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90283" target="_blank">📅 11:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeOA8v5z5PJItNv3Ugrn_X7MRFVBzjc2YZlaL3tG30O2crqUCA9bvty-oppgLOxRlURLu-bX0o6nQQy_IjTQW4lLjvW7PJ3Kvvxu3VRzcO_l1BJphau5WwBjuPF31Q_Ei_NFR-ZKL_Z7VnnycDb5xrvzO7JJa5pbEXajRNQCWbBudArXBXP4mReLKJbJqr5ImLZA7HX9fexq0J3DqbYHCyZyx8L_Gb_H7c4t3nkPM9LsS2ogZEIVuf3bq5Vw13ciOUAIOsdNbWWSZgFsAvScCL31_0gPX8xFyn3YIzI5fRb_X1JO_0W0ZmUgHyMy916Kv9zAPNPY3FifgAMn-JR9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر:
بسمه تعالى
لا يستفزنكم القوم
فهم يريدون تغطية سوءتهم بفتنتكم
فلا تكونوا عوناً للفاسدين ولمن يريد النيل من سلامة العراق العظيم
وحافظوا على وحدتكم وعلى وطنكم.. واتركوهم في غيهم يعمهون.
نحن وانتم فوق ما يقولون والله فوقنا يحكم بالعدل والإحسان.. وهو يحكم بيننا وبينهم بالحق في الدين والدنيا والآخرة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90282" target="_blank">📅 11:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYYqVmmsCyo845_FK3CwEgSEkKqqmNcJ3OcG4RrQJ7X-hiFsEZTyeAzFciP8VjJOyAskLsIs5AYuHgtb-DjOwnuKhZo9Lck3SKGXbOnMexHs8dNZTIBKPu9hx0hFLgtRxvyiS104oFdxV9EtjqEj1KuOT4P1I2zmRomNh8t5zXHxWRMwfL5HgTey5TzOoRAGpKmkFTg2qTgrl8okzlF53qlHSs8e_VJLJ-LpGfRb7RREt4dE-dnxmJT5ceyhS4D9hNTQ7aM-t1UPJc_bpXEEuQ_-WBO6UAW2c3XOUuayPDNBFHt9v-HCwQW4X2rKz5Kz6Y96pvYZmNoCwKyXeJnO3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأردن يدين استهداف الفصائل العراقية حسب ادعائهم للسعودية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/90281" target="_blank">📅 11:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">طيران مسير أمريكي مكثف في بادية السماوة جنوبي العراق</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90280" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
اتخاذ سلسلة من الإجراءات القانونية اللازمة وتكثيف العمل الاستخباري والتحقيق والتدقيق لمعرفة ملابسات الخروقات والمخالفات التي حصلت في هذه المنافذ ووضع الحلول والمعالجات المناسبة لها.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90279" target="_blank">📅 10:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇷🇺
بوتين
: نشر قوات أوروبية في أوكرانيا سيعني دخول هذه الدول في حرب مع روسيا.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90278" target="_blank">📅 10:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c984e675ec.mp4?token=hUuR5fYfdyAXBjLBZP0ve8vrxGJoq8CdiAeE4mfjIgkBRPez2R6sgmw0eqb9B1eMhot8vhQlMy810FpjP6PdI08CV5V_aGRi19LYBortlg5U3cWf9nA-egJrAk9nmSHJv9FAPhfoMolEPtiLVyplxa5d8NNBnDnc2l7PuYOrfmLkastYDAcaLchjWrSwKrvqmnPliarVzc_fHofLivqZYmZo2h4bWGyQA9CDGewUhaGvoB1VApXV63i2fnqEFiF5xijWghPz_XrMStN8q_Uf-Dw82l2m3hYamGrCoWQBx8D4PtHp9tecFPeiqZF9WUIkTykbmBcSzXUrwfjmNvTuLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c984e675ec.mp4?token=hUuR5fYfdyAXBjLBZP0ve8vrxGJoq8CdiAeE4mfjIgkBRPez2R6sgmw0eqb9B1eMhot8vhQlMy810FpjP6PdI08CV5V_aGRi19LYBortlg5U3cWf9nA-egJrAk9nmSHJv9FAPhfoMolEPtiLVyplxa5d8NNBnDnc2l7PuYOrfmLkastYDAcaLchjWrSwKrvqmnPliarVzc_fHofLivqZYmZo2h4bWGyQA9CDGewUhaGvoB1VApXV63i2fnqEFiF5xijWghPz_XrMStN8q_Uf-Dw82l2m3hYamGrCoWQBx8D4PtHp9tecFPeiqZF9WUIkTykbmBcSzXUrwfjmNvTuLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
استمرار إستهداف العناصر الإرهابية التي تكمن في إحدى مناطق مدينة سراوان من قبل القوات الأمنية الإيرانية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90277" target="_blank">📅 09:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
حاكم مدينة مهران الإيرانية:
معبر مهران مفتوح، والأنشطة المتعلقة بالسفر والجمارك مستمرة فيه، ولا يوجد أي إغلاق أو توقف في عمل المعبر مع العراق.
خلال الـ 24 ساعة الماضية، عبر هذا المنفذ 17 ألف شخص، مما يدل على استمرار عمل قسم السفر في منفذ مهران.
الجمارك في مهران تعمل كالمعتاد، ولا توجد أي مشاكل في عملية تصدير البضائع.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90276" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb9c722a5.mp4?token=LSnOsEVmCvZhgRBoKG73LrXGpTGZfzBloe1OYRVkwM7KbHTFPStQM6tWWIh8yjnZrOBE3YJ8XLa9iYULJkLL0g5iI2JLYMuRTHlCQZMK8KHItk3fK4SkKCqljNg5To_FPBAbaEZLj28HNympj7bzneqX299iwEbE5y57shZXnSl6JKrJXcfKU4Cx1jamlG2XaIaaXPEDQ1sBnNVIsYqh-xzvRO6j9EtpwG34DRXTuD-oMkNxDmiqofBCEuUB2X-n7Yx2CPfvBVJpTSO-VzRhwVUK-Rva4INYCStd2-zAwsKruB1bfZQnUXHeSleeJsA3nW0iTviN48UMfBs5QwI7qoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb9c722a5.mp4?token=LSnOsEVmCvZhgRBoKG73LrXGpTGZfzBloe1OYRVkwM7KbHTFPStQM6tWWIh8yjnZrOBE3YJ8XLa9iYULJkLL0g5iI2JLYMuRTHlCQZMK8KHItk3fK4SkKCqljNg5To_FPBAbaEZLj28HNympj7bzneqX299iwEbE5y57shZXnSl6JKrJXcfKU4Cx1jamlG2XaIaaXPEDQ1sBnNVIsYqh-xzvRO6j9EtpwG34DRXTuD-oMkNxDmiqofBCEuUB2X-n7Yx2CPfvBVJpTSO-VzRhwVUK-Rva4INYCStd2-zAwsKruB1bfZQnUXHeSleeJsA3nW0iTviN48UMfBs5QwI7qoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
نائب محافظ خوزستان الإيرانية: وفقًا لإعلان السلطات العراقية، تم إغلاق حدود الشلامچة والشيب في محافظة خوزستان اعتبارًا من صباح اليوم وحتى إشعار آخر، ولا يتم حاليًا أي حركة بضائع أو مسافرين عبر هذه الحدود.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90275" target="_blank">📅 08:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUNaUG-SjwhZFLafxEHAx_RrYHJW_cGayYRlte0hpF7Yl3ZV1fsJW3kyRBQdQaeLfK9bOugGAn-EPErd7D1ANtQStsc9-H8oErOrt7CVoPLUaJbyxHkEDmlESp0EFh3H0Vn-yNGQMFe_2_ECjSB10saMCFdVC4bGG3zH4LJecj1e3XCWbQa-7GeEx29prrZgNL22uKFFv7hxdHOKsXHrTGOgMD4xE0coSXr2jVBYoGY1pFpk0GepRIWWH-9ctmrumkRUiI00Lk5bITqMDxnmhesxLihvcvkpQ0D4icR_oN-q_9DRjh96b64fClK6emlIb2K3537KP3-l5cIwyY_FxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a79629eb3.mp4?token=QYdZ4apMs-I_K6VqCS-86RNLaMMfOiW08D9J2sRSrjppiPlN15sKlKje3NsaBELZCtQaAnTlMajiSxJRmxyotp9flFO35y2_bGxRv-ky0EnuPYwfv3P5Hal9cSNN1Yli84Yq4M_XsQ20hN5-JFbCmchZnoenz1_D4N0c_2t0mztMV_NqggTjh2gPmxe6tACnczUhiGoihC-HapPSzNUIZHALqzl27sc6CIRWQx9YvlGz0H0Rqu1PSC0UURAiDRpe_Sl9EKJZ7rwk49sfu3pDNN8PCEojTH380WHL3myaMvimSMptVtPZIc8j4WMgyFXXkRgL9CB5Pmvpxru9NS9U9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a79629eb3.mp4?token=QYdZ4apMs-I_K6VqCS-86RNLaMMfOiW08D9J2sRSrjppiPlN15sKlKje3NsaBELZCtQaAnTlMajiSxJRmxyotp9flFO35y2_bGxRv-ky0EnuPYwfv3P5Hal9cSNN1Yli84Yq4M_XsQ20hN5-JFbCmchZnoenz1_D4N0c_2t0mztMV_NqggTjh2gPmxe6tACnczUhiGoihC-HapPSzNUIZHALqzl27sc6CIRWQx9YvlGz0H0Rqu1PSC0UURAiDRpe_Sl9EKJZ7rwk49sfu3pDNN8PCEojTH380WHL3myaMvimSMptVtPZIc8j4WMgyFXXkRgL9CB5Pmvpxru9NS9U9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
منفذ مهران الحدودي مازال مفتوحا أمام الجميع وحركة دخول وخروج المسافرين تسير بشكل طبيعي.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90273" target="_blank">📅 08:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfc5f64ec.mp4?token=QQ4TuCXNEcJto7eKet7ahzaumhgXcTr8qh3vVgAwoMlOshUFkXn9dwOLKofhr6RAOI5DUnsJ88rAO807brMBQJLMneLzawW93_WCI4YEeDluc-I2I8Pc44RKn5W60D4rkcZrRvIwKeLPT31aoI__SkGLrGDNLcgX540zW5RqoQ2tt8pdTNxSh9iDCsx7DIOjnDExWtNG6SPd80VAhXdHzufdTM9u1E0arnX1i0EvWJW7WXVHsvP9hbmyXH0XWCCj542bUX3ajkcHRwR3ihdhhvUxlo49St3OKV2vxLxiKE7_YCXqYnYyJ0AbvOvoXbm6Zh_HeWwg1BvGza4rTis5Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfc5f64ec.mp4?token=QQ4TuCXNEcJto7eKet7ahzaumhgXcTr8qh3vVgAwoMlOshUFkXn9dwOLKofhr6RAOI5DUnsJ88rAO807brMBQJLMneLzawW93_WCI4YEeDluc-I2I8Pc44RKn5W60D4rkcZrRvIwKeLPT31aoI__SkGLrGDNLcgX540zW5RqoQ2tt8pdTNxSh9iDCsx7DIOjnDExWtNG6SPd80VAhXdHzufdTM9u1E0arnX1i0EvWJW7WXVHsvP9hbmyXH0XWCCj542bUX3ajkcHRwR3ihdhhvUxlo49St3OKV2vxLxiKE7_YCXqYnYyJ0AbvOvoXbm6Zh_HeWwg1BvGza4rTis5Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
نائب محافظ بلوشستان: إن المجموعات المعادية لنظام الجمهورية الإسلامية الإيرانية، والتي كانت تسعى إلى زعزعة الأمن العام وتنفيذ أعمال تخريبية وإرهابية، قد تجمعت في منطقة من مدينة سراوان، حيث تمكنت القوات الأمنية، بفضل المعلومات الاستخباراتية والدقة، من مفاجأتهم…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90272" target="_blank">📅 08:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90271">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
نائب محافظ بلوشستان:
إن المجموعات المعادية لنظام الجمهورية الإسلامية الإيرانية، والتي كانت تسعى إلى زعزعة الأمن العام وتنفيذ أعمال تخريبية وإرهابية، قد تجمعت في منطقة من مدينة سراوان، حيث تمكنت القوات الأمنية، بفضل المعلومات الاستخباراتية والدقة، من مفاجأتهم وإلحاق ضربة قوية بهم.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90271" target="_blank">📅 07:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90270">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
مصدر لنايا: توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90270" target="_blank">📅 07:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa850a0397.mp4?token=iByXmQXpqh5N2E8MrXpJmj2Qm8RNOp7UcqDmA0BxN8tEB0a_el2JULx0jWncatqWisJnwFKdeuC7snxXolPszP71eb0mUs6mFu9Aain_669Ws_UWSJarIxvEZ8x6Y6fO6AgoEm9hXUmGGfwdGqcIU_bZ7Sws6MFefcfNcfCcUIvjLi0o-wfrnHL11qHGNjvducdxss2U8R5Hx2oJujuKXvQTSXJ_tv6wArnTwN4_T_6wIJLm_oAxEJ9lPbNmW0_eIwQdv8sbUyiVlHU8jE1QBl6O7-wb-hyML1vocKHcjMIrsUVzfiDZoK_3OQgf0q80jlxi9wG7P2-Cx64g0ktQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa850a0397.mp4?token=iByXmQXpqh5N2E8MrXpJmj2Qm8RNOp7UcqDmA0BxN8tEB0a_el2JULx0jWncatqWisJnwFKdeuC7snxXolPszP71eb0mUs6mFu9Aain_669Ws_UWSJarIxvEZ8x6Y6fO6AgoEm9hXUmGGfwdGqcIU_bZ7Sws6MFefcfNcfCcUIvjLi0o-wfrnHL11qHGNjvducdxss2U8R5Hx2oJujuKXvQTSXJ_tv6wArnTwN4_T_6wIJLm_oAxEJ9lPbNmW0_eIwQdv8sbUyiVlHU8jE1QBl6O7-wb-hyML1vocKHcjMIrsUVzfiDZoK_3OQgf0q80jlxi9wG7P2-Cx64g0ktQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
استمرار الإشتباكات بين الأمن الإيراني ومجاميع إرهابية في سراوان بمحافظة بلوشستان.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90267" target="_blank">📅 07:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e64b1fb2b.mp4?token=WVumNFvuzF15zghGdqcWTEfuVGnMMXJGUTfyuWwsA2Dhpw0Fj2hT1u76JbBBhrgyTu8ELgqkOVuVhMGumLppJARt5eQecKfaIw-NoatzRhJv20nbfJtxEW4cxxmwN9vA3iSVLo9McOSMjpCxTnvQ-5kLxEYANmfE-xdFivn4bLBBtoyfnX9A0KanPgZbUraXrvs6yBdWx_-Zs7WVofR2uDSvK1ihMmGy_-DwstqNr-eGpoIOgvWfnA4rnpbG2ZyVbE_e3I7XV5ONsUJz3AcmfAG9aYFINfM0UH9iYNiR9AoJNdXMt6DzO6qX6DsqHdAZ4CWv6Aj6dkjUN6IVaoDToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e64b1fb2b.mp4?token=WVumNFvuzF15zghGdqcWTEfuVGnMMXJGUTfyuWwsA2Dhpw0Fj2hT1u76JbBBhrgyTu8ELgqkOVuVhMGumLppJARt5eQecKfaIw-NoatzRhJv20nbfJtxEW4cxxmwN9vA3iSVLo9McOSMjpCxTnvQ-5kLxEYANmfE-xdFivn4bLBBtoyfnX9A0KanPgZbUraXrvs6yBdWx_-Zs7WVofR2uDSvK1ihMmGy_-DwstqNr-eGpoIOgvWfnA4rnpbG2ZyVbE_e3I7XV5ONsUJz3AcmfAG9aYFINfM0UH9iYNiR9AoJNdXMt6DzO6qX6DsqHdAZ4CWv6Aj6dkjUN6IVaoDToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعزيزات إضافية للقوات الأمنية الإيرانية تصل إلى مكان الإشتباكات في سراوان جنوب شرق البلاد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90265" target="_blank">📅 06:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85ebf565a.mp4?token=VnKmmJJQeA8eK_hw0bgYnMaW4uK_q89ZFO3dV8sFXmkRhSUHEOJLDbMgrWi70u2-SkMweUX_QWiyVmD4fzE5IDZDpXVecnVssJnCP_P8GC-pcOaHw1EHKN8O271Xok-FaV_aRAF06LUPZ3HSIIXJs7MzBM1b_UzUkIEqmnSI6qxDGO4q2x-36CHEST1kW3iRMYPopK541QbDv3M3bycxug7YnuITr8_dsUA-pJZnf4pdfNPGMmz9EELP5B4MUQSl-DRb1ZlEuULN8FctpHSv1nUlZt6xROZbtFzfqKT-OemfLaldN-H1l-EoDTMRQJ48V9bcPiBfOY0GHN4CXZANxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85ebf565a.mp4?token=VnKmmJJQeA8eK_hw0bgYnMaW4uK_q89ZFO3dV8sFXmkRhSUHEOJLDbMgrWi70u2-SkMweUX_QWiyVmD4fzE5IDZDpXVecnVssJnCP_P8GC-pcOaHw1EHKN8O271Xok-FaV_aRAF06LUPZ3HSIIXJs7MzBM1b_UzUkIEqmnSI6qxDGO4q2x-36CHEST1kW3iRMYPopK541QbDv3M3bycxug7YnuITr8_dsUA-pJZnf4pdfNPGMmz9EELP5B4MUQSl-DRb1ZlEuULN8FctpHSv1nUlZt6xROZbtFzfqKT-OemfLaldN-H1l-EoDTMRQJ48V9bcPiBfOY0GHN4CXZANxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعزيزات إضافية للقوات الأمنية الإيرانية تصل إلى مكان الإشتباكات في سراوان جنوب شرق البلاد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90264" target="_blank">📅 06:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/839ea30161.mp4?token=jDpj9TL6rsiqxxpbmRU1TUjX0wT-8gJtz27l5KDPQzIJ-z8aiYHMdBO0jm9OdYhJGEaPKHyWXA50ZySxVOOt7EMER-f8TDN6E_2ICQtAoFeBEbTZHDWelRAS5wPg_0yENCacy_AoZYo8XZlGFGtT2mKzHfCkD2iDkqedSyNoE-Q-yfpIGdyC7iXPuOD-u2nhtozkzPWV_w92qgW1cu4tBvK0fMMVGqEFJ37o8DrAlTLmHkQ6tIS6zndcWyht3wM_nJbXfO_B4QhV8SbOObLGGRH--YGNcbXzrMVujXdGqBJPO0u4KbBdVlLbhVDuME5z_lkOxWs44Q-aJu25DGA27A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/839ea30161.mp4?token=jDpj9TL6rsiqxxpbmRU1TUjX0wT-8gJtz27l5KDPQzIJ-z8aiYHMdBO0jm9OdYhJGEaPKHyWXA50ZySxVOOt7EMER-f8TDN6E_2ICQtAoFeBEbTZHDWelRAS5wPg_0yENCacy_AoZYo8XZlGFGtT2mKzHfCkD2iDkqedSyNoE-Q-yfpIGdyC7iXPuOD-u2nhtozkzPWV_w92qgW1cu4tBvK0fMMVGqEFJ37o8DrAlTLmHkQ6tIS6zndcWyht3wM_nJbXfO_B4QhV8SbOObLGGRH--YGNcbXzrMVujXdGqBJPO0u4KbBdVlLbhVDuME5z_lkOxWs44Q-aJu25DGA27A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد أخرى من الإشتباكات العنيفة التي تدور بين القوات الأمنية ومجاميع إرهابية في مدينة سراوان بمحافظة بلوشستان الإيرانية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90260" target="_blank">📅 06:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bb12d1d5.mp4?token=C4Oyc7zjjbXwiwA9NjkTko8mAxRXwbp14iVXFBYTRQtBCHcyvhg9eklRDjj6mv1g5X5YlJk6uZ7jNAiolsA-sW6VjAGzSNkpCqAKgcVtzwNcOQvWJh4Ol_ACIh9RYvWI--hb3PnwvcwlpWtqYpSlGq3O1PtzdVR3n-M5Wyw4cMM9Gd-7jDG3lPaRY_f_rTI1J82bf2DQbHxdCBpizE7CjMw8vBXmukslYfir3a0xZN4rRBYexqzxYlKdPEhBcAJf5SrqT5KWLw5GKU1wl8cHsdCz64Wzw0mlb7DTFLflAr1szZPVS0RWGi8-RB9HbNkasPZCR85KG11v_96ZjaFfHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bb12d1d5.mp4?token=C4Oyc7zjjbXwiwA9NjkTko8mAxRXwbp14iVXFBYTRQtBCHcyvhg9eklRDjj6mv1g5X5YlJk6uZ7jNAiolsA-sW6VjAGzSNkpCqAKgcVtzwNcOQvWJh4Ol_ACIh9RYvWI--hb3PnwvcwlpWtqYpSlGq3O1PtzdVR3n-M5Wyw4cMM9Gd-7jDG3lPaRY_f_rTI1J82bf2DQbHxdCBpizE7CjMw8vBXmukslYfir3a0xZN4rRBYexqzxYlKdPEhBcAJf5SrqT5KWLw5GKU1wl8cHsdCz64Wzw0mlb7DTFLflAr1szZPVS0RWGi8-RB9HbNkasPZCR85KG11v_96ZjaFfHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اندلاع اشتباكات مسلحة بين القوات الأمنية الإيرانية وعناصر إرهابية في مدينة سراوان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90257" target="_blank">📅 06:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90256">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
مسؤولين أميركيين:
إيران حصلت على صور أقمار صناعية من جهات صينية قبل قصفها قاعدة بالأردن في يوليو، حيث أسفر ذلك عن مقتل 3 جنود أميركيين.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90256" target="_blank">📅 05:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇸🇦
انفجارات عنيفة تهز محافظة شرورة جنوبي السعودية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/90255" target="_blank">📅 04:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af37c0446.mp4?token=NJoGID6xiqyqtpfa_gYefXn1AJR0EOBgMcx4rrpf3Sn02ekONHSpXBxvkyhsGGdie1KB9P7QFXBYisU9g5_j_C7iyhK9jLpOJ_Z0tGkUQwX_VoC_PY9pkgsUgmgY5G1Gt6aDajVFjwFgzQQhx6xnlmXttLkjMZMu_h3amc2JI5QGeVSih9YYxySnI1r6x1nyVHMJxnLFtcImrRIJT1dKNCXw6kaa-RbkpTVZw9FGdrelxXXV381dK56ErLqs8Trwm6gLbKFbWz6h2QL1Ca68gqngRWpPq1M3Ocz66CPBGQcoT-Fc2llurrf8gL-BGqoxsAgH8a_TkpwNawoJho6elndWQ490Yth29x0ixZMfP2M_AWbMcvq10Mdte3PzE2Nj8Wi8WQAqM1acSGwy8UTb__G7l23JPHn2ARpD6NXWAYRGZFVQuKqgyXD16swf0W-_VsBPhJoKbcZ1JtTmSIWCMMKNWG-VskG7bFqtYryhL_SLyoGv-hsbX-4g_AmCMomTwfRQ14dP1wsr6YuO6ejAIg5476Rp9bsfUPCYD0sM-lWGusUQmwAZMsb9txx0WpO6Sv7rJhMwZMACT2jJQz2PYZsiw1rqlV_4MaNO5XYSyfjw2AXB1jZS3luaPB73OAHb21O7C9VxOApC-NSXo7hVZqIGjnVLA6hIFFaaWzauDYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af37c0446.mp4?token=NJoGID6xiqyqtpfa_gYefXn1AJR0EOBgMcx4rrpf3Sn02ekONHSpXBxvkyhsGGdie1KB9P7QFXBYisU9g5_j_C7iyhK9jLpOJ_Z0tGkUQwX_VoC_PY9pkgsUgmgY5G1Gt6aDajVFjwFgzQQhx6xnlmXttLkjMZMu_h3amc2JI5QGeVSih9YYxySnI1r6x1nyVHMJxnLFtcImrRIJT1dKNCXw6kaa-RbkpTVZw9FGdrelxXXV381dK56ErLqs8Trwm6gLbKFbWz6h2QL1Ca68gqngRWpPq1M3Ocz66CPBGQcoT-Fc2llurrf8gL-BGqoxsAgH8a_TkpwNawoJho6elndWQ490Yth29x0ixZMfP2M_AWbMcvq10Mdte3PzE2Nj8Wi8WQAqM1acSGwy8UTb__G7l23JPHn2ARpD6NXWAYRGZFVQuKqgyXD16swf0W-_VsBPhJoKbcZ1JtTmSIWCMMKNWG-VskG7bFqtYryhL_SLyoGv-hsbX-4g_AmCMomTwfRQ14dP1wsr6YuO6ejAIg5476Rp9bsfUPCYD0sM-lWGusUQmwAZMsb9txx0WpO6Sv7rJhMwZMACT2jJQz2PYZsiw1rqlV_4MaNO5XYSyfjw2AXB1jZS3luaPB73OAHb21O7C9VxOApC-NSXo7hVZqIGjnVLA6hIFFaaWzauDYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
مشاهد إضافية من إغلاق منفذ الشيب الحدودي مع الجمهورية الإسلامية الإيرانية من قبل الحكومة العراقية.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/90254" target="_blank">📅 03:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367a0b2c6c.mp4?token=cmoHwd01aXzDOEUPDFBeG_c1HMcb8B_ULiyRVqB4UJAWmw8FHZIHDPKzG-W45MuBswl2miTceAEDkLpEcoJdEOKYW3xVxazashEL2x2pnodIZko4OSvBJ5bVhWZc8uGz4KvtLYBp5Nqu8B3DqaMBjmYxjt9XhRedQiWSAyDqKkZ4kBy2HUEIiWZEuFYHpmOO24Tp0OnTMajblMVnl9fNmkChduXXsK-cAMULaEazio2lnlnAwM78pt7kH4lssasHZgt9TegJAVk1Nj-UrR5wNgs4hiJJ5CZaYdAxODq0DeFTdcy8iXVObqumzNaldQ3pUKm5AyVpkBys15OI1DyDpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367a0b2c6c.mp4?token=cmoHwd01aXzDOEUPDFBeG_c1HMcb8B_ULiyRVqB4UJAWmw8FHZIHDPKzG-W45MuBswl2miTceAEDkLpEcoJdEOKYW3xVxazashEL2x2pnodIZko4OSvBJ5bVhWZc8uGz4KvtLYBp5Nqu8B3DqaMBjmYxjt9XhRedQiWSAyDqKkZ4kBy2HUEIiWZEuFYHpmOO24Tp0OnTMajblMVnl9fNmkChduXXsK-cAMULaEazio2lnlnAwM78pt7kH4lssasHZgt9TegJAVk1Nj-UrR5wNgs4hiJJ5CZaYdAxODq0DeFTdcy8iXVObqumzNaldQ3pUKm5AyVpkBys15OI1DyDpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عوائل عراقية تقف خلف أبواب منفذ الشيب بعد إغلاقه من قبل الحكومة العراقية.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/90253" target="_blank">📅 03:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91429e7bf4.mp4?token=cf3KOcn42FIF2hRl9_ku5kH8BNeibONR-5dO3eO55dZ6qZu0lrDy1jLg0n9gYcOtlz5zD8WOp1SBZBdx-iKA03SQm6ekc0rsVTPDwjUPliLomdvkD7dgwinUwCfBeDhz31DPJi_Ue1X-EGWtF5Fq4L9uCuhxTvPilLz66a6Lq6eQe6IcaXy87w9MGaRHJp04X3hgljTJcbTObFxU4OLuLhof_1kKMK7gVXOYAeCiZ733WqrT-BgRwXlPWwPHZbkvpJLkEGpXk6EfoQlyOIHb3mhsqtlxPlDtcIC5_NW6nAERICpv7QCBaOyFgu2ulGs2Au8o5MQ8YHXTlHWS9HpB9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91429e7bf4.mp4?token=cf3KOcn42FIF2hRl9_ku5kH8BNeibONR-5dO3eO55dZ6qZu0lrDy1jLg0n9gYcOtlz5zD8WOp1SBZBdx-iKA03SQm6ekc0rsVTPDwjUPliLomdvkD7dgwinUwCfBeDhz31DPJi_Ue1X-EGWtF5Fq4L9uCuhxTvPilLz66a6Lq6eQe6IcaXy87w9MGaRHJp04X3hgljTJcbTObFxU4OLuLhof_1kKMK7gVXOYAeCiZ733WqrT-BgRwXlPWwPHZbkvpJLkEGpXk6EfoQlyOIHb3mhsqtlxPlDtcIC5_NW6nAERICpv7QCBaOyFgu2ulGs2Au8o5MQ8YHXTlHWS9HpB9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مصدر لنايا: توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/90252" target="_blank">📅 03:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q46vqLFRRcjhDFSCttbgp0yiVv8-PwBWvoU3Btdl3cbG3ZlwMz3Z2hfIi80tnkMoDPMLrqOwLsOhKWDzUAT0vURdJfefl4pDT7c4c56uIP8zmfGFrxfik-PmCUJ6lgaVip_xzOmaTZMEnH7i1YX5IS9DJw7MTM_v9V_baRD0lTkV9mYAzxTmkUcTloEOTZFJU06tpG5i1zQDhaEzGpP--bV09MKSXKsuobuENO3u02WLlrh-ZZmrBPMiuZ1MPISv3hGXSbsZ7NDrZqgcNVugy8LOtjYcecG1gYsafXepqAq-pBYBFae39aAbT5EZ499ezWa60JdrvUQ6HSDW0Bt-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مصدر أمني: إغلاق المنافذ الحدودية مع إيران شمل الشلامجة في البصرة والشيب في ميسان بشكل تام وقطعي، ومنع دخول وخروج الأفراد والبضائع من الليلة وحتى إشعار آخر، فيما لا يزال منفذا زرباطية في واسط والمنذرية في ديالى يعملان بشكل طبيعي.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/90251" target="_blank">📅 03:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
مصدر لنايا: توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/90250" target="_blank">📅 03:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">إنفجارات تهز الطائف</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/90249" target="_blank">📅 02:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/90248" target="_blank">📅 02:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">إنفجارات تهز الطائف</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/90247" target="_blank">📅 02:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات تهز خميس مشيط في السعودية</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/90246" target="_blank">📅 02:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارات تهز خميس مشيط في السعودية</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/90245" target="_blank">📅 02:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
مصدر لنايا:
توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/90244" target="_blank">📅 02:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7o9rptkLYC_aK2gnmBwb8FTptK9itc4YUX_vXR26H5-fCXMv6mvIvTGwpG-ACNxXCfWDvpXJsvRi98Oyjg01fsfieO7v5lcuS4Fb58e72s3l2-LXERcrOqDLcm7Dx61Z54Tem3ez-iHUfMGXRxf7wDsxaOaybKItl-7MgG3Nn6ExpfalgsBDGruhIN3Ny6ajAAo2M4b-VUtZQiJwmgFF7fqWjz7gPxs0H3hZr7vUgKcZoIwmm1kSApZG3_v4kO18QCMJ4NsAdtzTHycpVJYZCtAPQMX2WhT_Z2XrOCvLwKk1bNx3FBbI7JN12hyyMNXfCOTc3hNLPsII6YJYWLh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
حريق كبير في مدينة ابها بالسعودية بعد استهداف عنيف من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/90243" target="_blank">📅 02:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
القوات اليمنية تسيطر على جبل جرداد الإستراتيجي في محافظة تعز.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/90242" target="_blank">📅 01:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce0bc6b13.mp4?token=LbYJ4AEI-JITxhnQcxZ8FWtpaPYyUR3lVYZ-Jf9gUESychxW89k6t5wuLJ433mTk4ZHa_y6T_7Wki33Rc0CqJwpbXcXQVY7lrT6SKtyWCl6NOMD-LAqmg9UY8L-SfCKoMPVIFH5yseLecB9hy4nbCpG6BY6ClRAuxpXtQcSdJY5V2l2YP_lZnFjIfpzT7kN-BrsBLYK3heVLGQ7NUuXHYfHGRZ1r4TbdYwEdlAf0a9RWIxfWiEZS1gbh7_zh96pOd1nuAkTzzCyAOIyPsA0MR93uxzhYPBPDqCadUSRpL2BajvFeOGBkV0yjx4P4Qb46MscVbWhPm3Zp-LtMVGF5YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce0bc6b13.mp4?token=LbYJ4AEI-JITxhnQcxZ8FWtpaPYyUR3lVYZ-Jf9gUESychxW89k6t5wuLJ433mTk4ZHa_y6T_7Wki33Rc0CqJwpbXcXQVY7lrT6SKtyWCl6NOMD-LAqmg9UY8L-SfCKoMPVIFH5yseLecB9hy4nbCpG6BY6ClRAuxpXtQcSdJY5V2l2YP_lZnFjIfpzT7kN-BrsBLYK3heVLGQ7NUuXHYfHGRZ1r4TbdYwEdlAf0a9RWIxfWiEZS1gbh7_zh96pOd1nuAkTzzCyAOIyPsA0MR93uxzhYPBPDqCadUSRpL2BajvFeOGBkV0yjx4P4Qb46MscVbWhPm3Zp-LtMVGF5YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
سماع دوي انفجار مجهول في العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/90241" target="_blank">📅 01:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e27ef9604.mp4?token=cYkDOX6RJEyBsNHi8bMr_SNXHjKtOL2Vv-ZZOy5hMlARA1p8OTmTxshkf3WxT8T5qyF9uEd3vfHxR51M8odyJuJUhVxMwnu5qOjv6ogwhk1ecAW6_H_i9WEaz2h2b4qCrXp29xN3Zneab0SE6Y2lt44nXcKmt3LG2NWQlqtMqCUBH3U8QEknOZAcA0aEUiTL8Alr3zpvxvA2jI-hny5Ghp6hspvQQOK5hIb26EgAXqPuU5h_WcivxWL_iedZeOmj6Mc3ZfECJhbqc3rtw-sDUu-MOTiRgtfssKu8H__bAnlRFmggM5TApFhcEP_Bqd6mQ-O63vHC-xC6Pbp5lLKYlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e27ef9604.mp4?token=cYkDOX6RJEyBsNHi8bMr_SNXHjKtOL2Vv-ZZOy5hMlARA1p8OTmTxshkf3WxT8T5qyF9uEd3vfHxR51M8odyJuJUhVxMwnu5qOjv6ogwhk1ecAW6_H_i9WEaz2h2b4qCrXp29xN3Zneab0SE6Y2lt44nXcKmt3LG2NWQlqtMqCUBH3U8QEknOZAcA0aEUiTL8Alr3zpvxvA2jI-hny5Ghp6hspvQQOK5hIb26EgAXqPuU5h_WcivxWL_iedZeOmj6Mc3ZfECJhbqc3rtw-sDUu-MOTiRgtfssKu8H__bAnlRFmggM5TApFhcEP_Bqd6mQ-O63vHC-xC6Pbp5lLKYlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
سماع دوي انفجار مجهول في العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/90240" target="_blank">📅 01:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏اول موقف رسمي عراقي   تدين الحكومة العراقية الهجمات التي استهدفت المملكة العربية السعودية الشقيقة، وتؤكد رفضها لأي اعتداء يمس أمن المملكة واستقرارها، أو يسيء إلى العلاقات الأخوية الراسخة بين البلدين.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/90239" target="_blank">📅 01:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq4vl4hMitQsAp0ybfbLEdBjPLiqKl67SKvEsLNUN8T9lCW-8bzEJCrxeZkl0bBLweSQpnOGm-ZI5tNn1INBz9wOCeMnHh6w7aYg1dxynalTTqmd3URudBkMF_RQwGralC6b8JfYEOtwovd3I82N5MiWpxjS7J4u6tlWyTrdsj7shvaUyyllKskG_qy_5MINhDyyvwiJxNh5LohrBG1qp0v_gf4Z2yWkjqFARS9cy0vTvOD4JV8I__FbWxnZrr38i0jyl3ao25uu4I1nD2_KNOps7t8ilQcczO5XPmEl_nZGrbdj5GhsstvkLFCV8oUyC3tWe_W92W3ELKe57x7XHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
حريق كبير في مدينة ابها بالسعودية بعد استهداف عنيف من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/90238" target="_blank">📅 01:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الخارجية الأمريكية:
نتواصل بشكل منتظم مع حلفائنا وشركائنا في المنطقة بشأن التطورات اليمن.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/90237" target="_blank">📅 01:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/90236" target="_blank">📅 00:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/90235" target="_blank">📅 00:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/90234" target="_blank">📅 00:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmSH1OzhGbPvZcju5Q_ZP_y6s7hZLQoSHNdl9PASsNXwyzNTrSDBzU7Xs924YrS67qQ1QO7W-zHkykS04n7fnvyMt_O9n__bsIPdy4Ni2zDEE2OvYA8j8cIBJHZUqnFlSBxXiP78SR3bcQWXFUwbfo2l1SvSpXv4plShcEPh8Af0cXXp9PVp5zUpJHrXY29ctF2hOlavfvGZw4sc16sVBkvVglqnjEOKhFUtTiX6nLRnXsWhhrn00laAFFZUEIUhxvvUDzm5ceFRhBbONgLtPmT280LYe5tOBOuUtoLosmfwbGhmSu4nGmnZUYwz14rguhILED7JXQz6-KkXAgSi7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇶
🇮🇷
🇺🇸
🇸🇦
بريت اركسون : إن تعرض خط أنابيب الشرق والغرب لهجوم من قبل الميليشيات العراقية يجب أن يعطي الجميع استنتاجاً واضحاً للغاية: إذا استطاعوا ضرب جوهرة التاج السعودي... فلا شك على الإطلاق في أن إيران قادرة على ضرب أي بنية تحتية تريدها في أي لحظة.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/90233" target="_blank">📅 00:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb3a9e2c1.mp4?token=gkLgL-secOM0Z_2iRjsE1az7v1a9-8ppd1PHtrMtUHe6bPUwfuNEqL64EAGAIPpLx_MU8dQ74IJ6rsjmW4nzgX64616wiVP6LY2u0w_fzvkGtymfOpWG8kP1dN5js-JQNXptsLS5Jj5ByvLC4z5gxG6tlP9XgDTGFsE4izM0RttccKp5AUyKIoURwyBd4QA_jOhUlC5Ebb-tTZikgFmIOcDmopVfR3KMdBpdrvrIftONyAx8AVXU-QAkNtgFy_6rIGgZnh2UfiEnbN_wSKsEwB2Ekr_FjnSoJdBFFfXFkGab-FGOWWQkqPtixMdotAhBCWwCQIkylnQ25higeUS19A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb3a9e2c1.mp4?token=gkLgL-secOM0Z_2iRjsE1az7v1a9-8ppd1PHtrMtUHe6bPUwfuNEqL64EAGAIPpLx_MU8dQ74IJ6rsjmW4nzgX64616wiVP6LY2u0w_fzvkGtymfOpWG8kP1dN5js-JQNXptsLS5Jj5ByvLC4z5gxG6tlP9XgDTGFsE4izM0RttccKp5AUyKIoURwyBd4QA_jOhUlC5Ebb-tTZikgFmIOcDmopVfR3KMdBpdrvrIftONyAx8AVXU-QAkNtgFy_6rIGgZnh2UfiEnbN_wSKsEwB2Ekr_FjnSoJdBFFfXFkGab-FGOWWQkqPtixMdotAhBCWwCQIkylnQ25higeUS19A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الاميركي: نحن ما زلنا نرسل الإرهابيين إلى مكانهم المناسب - إلى الجحيم - والسفن النفطية إلى قاع المحيط، حيث يجب أن تكون.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90232" target="_blank">📅 00:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524aca328c.mp4?token=na7QMeEZ9e-grew-d8T0IIte4_x4sW8XZB6CssKBFY6FMiypDOq43qt5iuoYiIDdIaDwKo2k1HZYS40vCdNcb-p0sio81v3l21saTjtUIDe_tNzW1mdEWQ4PLtG7oS0nU0Y0DVvi0Atl77pMzrf6yrsJo_P7UtwVQY29b9abrz3KFZoeQEhDWKdTHiNDYnZMRWnpvMh4W-c7cjukxv1Y3CdPSXPTCqjpZOPFEL7l9f4CkhM1D1RUl9btiC8H174PXHdvadWCZwNI8fpr1lIddcx3GPtn7lHdVTIzIOYJZjkQLtr2WB94hG5Eof61KtrsUudlDGyoY_-OR59K0PfpQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524aca328c.mp4?token=na7QMeEZ9e-grew-d8T0IIte4_x4sW8XZB6CssKBFY6FMiypDOq43qt5iuoYiIDdIaDwKo2k1HZYS40vCdNcb-p0sio81v3l21saTjtUIDe_tNzW1mdEWQ4PLtG7oS0nU0Y0DVvi0Atl77pMzrf6yrsJo_P7UtwVQY29b9abrz3KFZoeQEhDWKdTHiNDYnZMRWnpvMh4W-c7cjukxv1Y3CdPSXPTCqjpZOPFEL7l9f4CkhM1D1RUl9btiC8H174PXHdvadWCZwNI8fpr1lIddcx3GPtn7lHdVTIzIOYJZjkQLtr2WB94hG5Eof61KtrsUudlDGyoY_-OR59K0PfpQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الاميركي:
نحن ما زلنا نرسل الإرهابيين إلى مكانهم المناسب - إلى الجحيم - والسفن النفطية إلى قاع المحيط، حيث يجب أن تكون.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90231" target="_blank">📅 00:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🏴
قطعاً بینی سعودی‌ها به خاک مالیده خواهد شد.
@Naya_Press</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/90229" target="_blank">📅 00:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6MvwFrT9CMcVD91ZFjw_Njrvm4KxUHjVB_qq8fKaLDyXq-j3HLePTl0diIPRnzxH2LfHJEW5GLDqLfO7kGgSAkHMmF4nnYsjBDLIq2PZj47_bpP3mJeTOqD52OlKhbmaVUShLMvES1PtOb4IL2Lypb2V1YJpVhAym31Xt4IHkBd5GbkjcTDYqf7PlV0uY9TXkMgreU47wBfmWX4fjQMr328rLbuxLB7c_bGSHbiRZOPOnmkXDhYEebKcegvqplEkl3JDZDytgsOahayz_TAqVoZ2dMbq-4y49NlUa9Ir3cVXNco3ic-SesJL232YG7XFi0r6DGyGnPPY4jvewy9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇸🇦
السعودية رسميا تدعي تعرضها لهجوم بطائرات مسيرة اطلقت من العراق.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/90228" target="_blank">📅 00:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇰🇵
أطلقت جمهورية كوريا الشعبية صاروخًا باليستيًا لجهة مجهولة.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/90227" target="_blank">📅 00:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/107c7847b1.mp4?token=dTiJU4oHrKcQGeteglrlj-LSGW206dzBaJCVNbS3ImLhfpax_BeZE_3vQUaAGRRaMi_FjPxSxT_T8C6iM3QDfa2jOB41yM0Y88DrVaj_8RHqudG2a60qhFxo0WKRkmfTEnLazH-mN7Hf8nAAOtoatJ28HntV1UeEguSHct3y_9znO222TGVqQmwGIfRLKOZYaX5CcGULSeiIuLOWl6J7O3nyWp0qOtB2ZQ421pHjY0USfSfDl0I6_73aCe9YSW_AcCj4aX1r1zCmaoNf755g9yOI7deECD96Q9_RXf4-80xxlelTl6yWTyOlQXUyM8QfvmwbxJE0ywSnN2NKJqd-UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/107c7847b1.mp4?token=dTiJU4oHrKcQGeteglrlj-LSGW206dzBaJCVNbS3ImLhfpax_BeZE_3vQUaAGRRaMi_FjPxSxT_T8C6iM3QDfa2jOB41yM0Y88DrVaj_8RHqudG2a60qhFxo0WKRkmfTEnLazH-mN7Hf8nAAOtoatJ28HntV1UeEguSHct3y_9znO222TGVqQmwGIfRLKOZYaX5CcGULSeiIuLOWl6J7O3nyWp0qOtB2ZQ421pHjY0USfSfDl0I6_73aCe9YSW_AcCj4aX1r1zCmaoNf755g9yOI7deECD96Q9_RXf4-80xxlelTl6yWTyOlQXUyM8QfvmwbxJE0ywSnN2NKJqd-UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
هروب عناصر المليشيات الموالية للسعودية من ثكناتهم العسكرية وترك خلفهم كبسة بالدجاج من دون ان يأكلوها
😫</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/90226" target="_blank">📅 00:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الاعلام الاجنبي: اصيبت شبكة خطوط أنابيب النفط السعودية بوابل من المقذوفات، مما أدى إلى اندلاع حرائق، مسؤول يقول إن الهجوم من طائرات مسيرة انطلقت من العراق.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/90225" target="_blank">📅 23:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jip1hB-3r3jyC1vEwTcUP6o0F4CPmABha6vk1sYppMzPcNAMe3PCgpVporpu4KnQCnsEehNOwojx09aCEwrfOZWUHEzH0jZLRmoYZOWbOVhikHy6nN1XgOb97Cu4PIJ9tcq3JKKFSovNTsf4SBhJOGRHL6Hl0vAFXE15BOVteHfPtWmCONiV-MynbbuSfv12PAfnLtlA2a_ucJoM-ztRbPwUYKUXYMyRwj7yQm-WVPTtpOAGl3l4uVWOCcEalL8DexFKK_UJ5KC7xLuFXdNAw6m-kQeJx2lG2ND33s0kngQPi7LLGc0OJFe4L7C7uSvmVmdWPU9qO2Rr-K3b1neR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إن الهجوم من طائرات مسيرة انطلقت من العراق.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/90224" target="_blank">📅 23:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇷🇺
بوتين
: أوروبا تدفع دولها نحو الحرب مع روسيا. روسيا لا تشكل تهديدًا، وليس لديها أي نية لتهديد الدول الأوروبية.تم حل كل شيء بناءً على نتائج الحرب العالمية الثانية.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/90223" target="_blank">📅 23:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇾🇪
سماع دوي انفجار قوي في تعز</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/90220" target="_blank">📅 23:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-text">🔻
It seems that the US and its allies in the region are very upset about showing the losses through photos and videos. Therefore, our channel’s name will no longer appear when searched for on Telegram.
🔻
Please share our channel link as widely as possible.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/90219" target="_blank">📅 22:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اطلاق عدة صواريخ من سيريك</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/90218" target="_blank">📅 22:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
🇸🇦
حرائق لا تتوقف في خط انابيب السعودية بعد الاستهدافات اليمنية الاخيرة.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/90217" target="_blank">📅 21:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇱
محاولة دهس لمجموعة من جنود الاسرائيليين في فلسطين المحتلة.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/90216" target="_blank">📅 21:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
تعرضت حاملة الطائرات جورج واشنطن، التي تحمل حوالي 5000 بحار ، لهجوم صاروخي باليستي إيراني في نهاية الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/90215" target="_blank">📅 21:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqZeLCdaCdo3Ec4IvHs8KNM1lzSNPkoSu2ORUnrZj9DWh6ZFQfWKqFrOhGDkpiQOiVfFoMxkHcCNXiNX1TDsQWSdZ4HnqIVc1E2aaAZ2xZhsQYfk6hyLcCd0nnk4S-pTy-FxyH4dmsuKRhFxaP00CL_bCcit3EOm6zHc-CT1NueHrHNTuuyDh0HErWCZKvlQOSPx1N7fqTau3BZ2wOKqp4DTyvaPWUve8IHL0RD3HbPM8qeeL-OAOBNfSOxjcQK8BnHoCTgQ6wbyF3oOMLq0e58QgRxovzGceLV0ZvsMKCSgtFLDbqeqIIJIyDkViIkmjy_NkXuOaMBLeSnSJXaCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسريب ضخم يطال وزارة التعليم السعودية
🇸🇦
أحد المخترقين يعرض على منتدى إلكتروني قاعدة بيانات تضم نحو 600 ألف سجل، مقابل 300 دولار فقط.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/90214" target="_blank">📅 21:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POSqMi3y-lQfnm43y0l_7FCl3vTDLn16oelEJkV0edtlDXl8c8_joZI4-InWKvrrlfQ2jC_sWeaMDkFP5AWp3_ksVeDTNDS7VmS22_ZKG1fh5pgBocmh1TguY_l3x3KhtKDpge5zRahSAhs8Xh6Ppx58GGp9tCKsNZiAz2tJ4kbFdAB8fYK_2Vbpds7ceHMsFcE7Cfy-BqU48H6qju4FC1GBQj8zsJ92jCPWWQo3hVKwrUMWWhfFeZ2bYs4K-d8IdwJDeA2SnVBdQzG_xJrDlvr3EifNJlfNkZW9TBFKnFQoeXhEBDWFF_J2I-vTdPZv8Wb1v6hq2TEIqBiT10Jslw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ همام حمودي في ندوة حوارية بمعرض الكتاب الدولي: الحكم في العراق ليس شيعي والنظام باقٍ، باقٍ، باقٍ
- نجحنا بشهادة دول العالم بإقامة نظام ديمقراطي تعددي، فيه حريات وتداول سلمي للسلطة، وحضور شعبي، لكننا اخفقنا في بناء دولة مؤسسات.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/90213" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ
سستى مكنيد و اندوهگين مباشيد، زيرا اگر ايمان آورده باشيد شما برترى خواهيد جست
So do not weaken and do not grieve, and you will be superior if you are [true] believers.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90212" target="_blank">📅 21:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇾🇪
الشعب اليمني يجتمع في ميدان السبعين،
شكرًا لله على الانتصارات التي حققها الجيش اليمني ضد المليشيات الموالية للسعودية.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90211" target="_blank">📅 21:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90210" target="_blank">📅 21:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
رئاسة الوزراء العراقية:
فصائل مقاومة سنجار ستباشر تسليم سلاحها إلى الدولة.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90209" target="_blank">📅 21:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
رويترز
:
يدرس البيت الأبيض استخدام "قانون الإنتاج الدفاعي" لتوسيع قدرات تكرير النفط في الولايات المتحدة، وذلك في ظل ارتفاع أسعار الوقود المدفوع بالتوترات المتعلقة بإيران.
ويناقش المسؤولون تقديم دعم فيدرالي لتوسيع أو تحسين المصافي القائمة بدلاً من إنشاء مصافٍ جديدة، وهي عملية قد تستغرق سنوات وتتطلب تكاليف أعلى بكثير.
يُذكر أن مصافي التكرير الأمريكية تعمل حالياً عند مستويات تقارب طاقتها القصوى، حيث تبلغ نسبة التشغيل 98%.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90208" target="_blank">📅 21:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGELyE-wI89b7cE9TxxEv1Hr0cNdWMJ44h-H4PhvvHUpnJfjiWhAU9ktmAWF1ZZ-Fm6UhNduYzSTAXPSa-u0y34VErwcHUP_7U8tfKIg76gqCtx7jS6cVik2MflfOAwQIdeYzrsxFKVX21Lpd9WjY4dMK4HxKVen0hNYj_8J-zNs8ntm7qp3BnAOKHQlb6uuL65U5l3hTmVEXYTsaGbftgBcMttZ7YMaZ_WFYQL7vuK7M8ekrQGq2F26KQuvNCh05jKYB4ufqawxPqnGSmaX7gcbIVocavp_5f3XmSTmqv7BwhiJucs71zPMoMcA2Tra93wulSItZtKa0RPaJtcgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇷
🇺🇸
ول ستريت جورنال : استخدم إيران نماذج الذكاء الاصطناعي التي طورتها الولايات المتحدة لمحاولة استهداف سفن البحرية الأمريكية في الشرق الأوسط، وفقًا لتقرير أنثروبيك الذي يحذر من مخاطر الأمن القومي الناشئة.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/90207" target="_blank">📅 20:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اطلاق عدة صواريخ من سيريك</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90206" target="_blank">📅 20:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmUgL6TIVFlWPAZWbiBuPh0oCiTIg61OilUg0r9J3KHBpw7l6EY8kg3QcyYmgQT04ZrtxqOAZsCwQm3MUR0ChGku9KfycsNBhJhWG1NFhnBvwP0Nbr4GNNVc-VRYMRkDBbDQLkpM4C7gVzyt2rqYM_qzm2hKIBdPBAdh-S0sUcCncFzQGvKOmZKjlkMcd5p3JutfZn7YpXAXf38OCJq25Ew0i8YL3_CQWmPYRxIm9ii4Y4CQziKQ3l0gwU2aaGnWHTA8wLghFs3Ti_rOIuSDKrSrUrR-4opt42MB1K68c7t5R9Am_FEH7AEiMcvLeUagZsrYr9MOwoGZ2q0axsoL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
عملية "والله أشدُّ بأساً وأشدُّ تنكيلاً" في الساحل الغربي.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90205" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jglGmyIB_LVebKSqi13lIaCACSLUnOviuk-nw5TTUAWEYIoYLqZZmlhxeVI-gquf16OByORnagk-EKSIP19Ej0R2V1h4oyg8CKZkI5_blVXpJZGBju_BtoPb4siXyuafqZbJrRv1RxRtuR8qXPXngHPMVmiOhcQjxLb0UI6DRqwcRG1oPTEX4PWwq_kRnbc-faC5mJvoJlzYBKFhionIu2vGjCGmRqwPkc7XDafDzpOe5-07McxDyOSx3jIsU938dFUcWnwc4pR3U2DWtwdj0R80Xhnoju4qdnv1ultfcErK7r_4l2YOunEyOcHX8CvCPnvdF2aNUkq_Alxm0yvWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام الاجنبي: اصيبت شبكة خطوط أنابيب النفط السعودية بوابل من المقذوفات، مما أدى إلى اندلاع حرائق، مسؤول يقول إن الهجوم من طائرات مسيرة انطلقت من العراق.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90204" target="_blank">📅 20:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47bceab31.mp4?token=F9zcYPlH94f9F3mIHQSnkjZI82yP1vigG1Vy4qcrGZAgDERkM0bSm9Z2ZXkpqCVKaJnoAFwNpwKfdOUG6K-5K2KUvt9ybPpBLmtzFdTycbdXrQ42sU7kR4FMa4SnjO9gRul5N-kjSIZLW80XoYY-ryqw_LKhXXGagLmoXOtDCVQIdSAujQ_M7wT4-n-5U4VAmtCeTmKAHDY1dHrYKAcYkjg1rO-hReiQrP1iY-y8Vp-kJ-8FpAanLJu_eOrx2mPCLaQW6RRTips6Iw4Wk1jB0rEsXZ4okv-9FLgS6YkezaUkVXWJkGNWDYiPXzVAljhnfF84lQEfQRPL9YxuYEeuxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47bceab31.mp4?token=F9zcYPlH94f9F3mIHQSnkjZI82yP1vigG1Vy4qcrGZAgDERkM0bSm9Z2ZXkpqCVKaJnoAFwNpwKfdOUG6K-5K2KUvt9ybPpBLmtzFdTycbdXrQ42sU7kR4FMa4SnjO9gRul5N-kjSIZLW80XoYY-ryqw_LKhXXGagLmoXOtDCVQIdSAujQ_M7wT4-n-5U4VAmtCeTmKAHDY1dHrYKAcYkjg1rO-hReiQrP1iY-y8Vp-kJ-8FpAanLJu_eOrx2mPCLaQW6RRTips6Iw4Wk1jB0rEsXZ4okv-9FLgS6YkezaUkVXWJkGNWDYiPXzVAljhnfF84lQEfQRPL9YxuYEeuxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم اعداد كبيرة من العتاد العسكري في مدينة المخا</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/90203" target="_blank">📅 20:06 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

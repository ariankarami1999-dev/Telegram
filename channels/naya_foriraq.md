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
<img src="https://cdn4.telesco.pe/file/C-1Yd3f7YCI70nFMCb8CrNyNgR_Kqjo4pQwP2Rv-5DcuIGy7M0d7aOtoiVGk4JYHUAJlj5N2pATuIQRTOmpfPWCM1-WX4UYTYJuGMXEYIw3yWU7NtVtXkJXMV92Tz1QI6o2uhahxKlMmfdrYqhvgC8YwOc3JrIRmieeVMfvLGTJCIH4FzghrgGCIbxwRJTCuedT7TPSoDBMJN-aCKXGXXfIaQVp-KIqB-fdGR6pqpEN6fD-PV0ly0t6wCXDS4b_vlQhAhAHSX-Czu7XLAZ2i1mWMlPplFDLQgPqAhNLg_ghftyVbjMY-c3BWhhbWtCHbugdwgud16iLL9D3LuMgfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-81649">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">العلاقات العامة للجيش الإيراني:
في أعقاب الهجوم العدواني الذي شنته القوات الأمريكية ضد المناطق العسكرية والمدنية في جنوب البلاد، وانتهاك بنود الاتفاق المكون من 14 بندًا، قامت الطائرات المسيرة الهجومية التابعة للجيش الإيراني، منذ فجر اليوم، بشن هجوم على مراكز تجمع القوات المتخاصمة الأمريكية المتمركزة في "معسكر الشيخ عيسى" في البحرين.
🔺
إن عواقب انتهاك الاتفاق بشكل صارخ ومتكرر مع أمريكا المجرمة، ستكون استهداف جميع المعسكرات الأمريكية في المنطقة من قبل طائرات الجيش.</div>
<div class="tg-footer">👁️ 181 · <a href="https://t.me/naya_foriraq/81649" target="_blank">📅 08:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81648">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">Mavic 3 DJI over Alnajif street</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/naya_foriraq/81648" target="_blank">📅 08:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81647">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسالة السيد القائد الخامنئي لكم يا شعب العراق العظيم</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/naya_foriraq/81647" target="_blank">📅 08:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81646">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12ac0a9f4.mp4?token=dh0PK5FY-R00G9SniBJOUb46AOT3jcHNsooOFhRd3RuYF51cSmu9DwrTM0mazLessVJUOqKYaKruPDYDGAx9Biv_WD4VkFI7JEW1ubQgKoXZOVTemXnUX2hnyI2dk9NE4SF2ernISOaZJeBwsuHYrgAe7bSFrrVVl0BJL_kEzkQu1Kc5AXk8FOewrLir6LuQlCP0s7hyyhAZJ6kB2WFIREncDHCKCtiV2Y8sMAfkiXzQlK9JDeR7eSmrKOVEMDSJR934WPGdwikLOj0olhBZYYV8K5sFEqhalE45jXgK07rBUu7qFJwOnTAgxkjvWB0tnNSB5bUf5oEaI259_gc-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12ac0a9f4.mp4?token=dh0PK5FY-R00G9SniBJOUb46AOT3jcHNsooOFhRd3RuYF51cSmu9DwrTM0mazLessVJUOqKYaKruPDYDGAx9Biv_WD4VkFI7JEW1ubQgKoXZOVTemXnUX2hnyI2dk9NE4SF2ernISOaZJeBwsuHYrgAe7bSFrrVVl0BJL_kEzkQu1Kc5AXk8FOewrLir6LuQlCP0s7hyyhAZJ6kB2WFIREncDHCKCtiV2Y8sMAfkiXzQlK9JDeR7eSmrKOVEMDSJR934WPGdwikLOj0olhBZYYV8K5sFEqhalE45jXgK07rBUu7qFJwOnTAgxkjvWB0tnNSB5bUf5oEaI259_gc-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس خلية الإعلام الأمني: متابعة دقيقة لمراسم التشييع الشعبي للسيد علي الخامنئي في النجف الأشرف</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/naya_foriraq/81646" target="_blank">📅 08:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81645">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4e6207d4.mp4?token=PrEBuq6PlXbapyEPkNnpLp6DhyRZe1GorjF7w1mjFUqQPdL9zCCrw64Ux8gVeV30gOIiuNXNH2_7S3FsTa-YabK3UTrue4U7QJ4X8eeLbXWNBcwKRYKG4yFCLaRiGQYAUEN_9BXhTssI6CbAwItDZefAEoFLmTIqgxcmZTki-hRf72ceWjYkAEzkRJTAr5MePW22KIdAX-4Mz9W-xRUnpdZuN79t-PhIh5_7uDUhQMPk4kR6jH95PCyp2hU5AqCqJjI4LvdlTGWmFCfnZ7x18g9VbTEUzoXcL96bk2mh87BPCPnk1qpfACmhPz8l-WS0Rq0mhqLO2ct9Sfu37YPHmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4e6207d4.mp4?token=PrEBuq6PlXbapyEPkNnpLp6DhyRZe1GorjF7w1mjFUqQPdL9zCCrw64Ux8gVeV30gOIiuNXNH2_7S3FsTa-YabK3UTrue4U7QJ4X8eeLbXWNBcwKRYKG4yFCLaRiGQYAUEN_9BXhTssI6CbAwItDZefAEoFLmTIqgxcmZTki-hRf72ceWjYkAEzkRJTAr5MePW22KIdAX-4Mz9W-xRUnpdZuN79t-PhIh5_7uDUhQMPk4kR6jH95PCyp2hU5AqCqJjI4LvdlTGWmFCfnZ7x18g9VbTEUzoXcL96bk2mh87BPCPnk1qpfACmhPz8l-WS0Rq0mhqLO2ct9Sfu37YPHmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر لنايا : تشير التقارير الأولية إلى أن عدد المشاركين في تشييع النجف الأشرف قد تجاوز مليونين وثلاثمئة ألف شخص حتى الآن.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/naya_foriraq/81645" target="_blank">📅 08:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81644">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/naya_foriraq/81644" target="_blank">📅 08:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81643">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0144dd6d2d.mp4?token=sVAa5hPz7-La5o5TD3GMzO2lEPDgE5mjo-RgQKlmT3dK5C7VOM8Gj8TJ7tCB9mKOOVPKdKlIUDb_ce4-iDfP3mN5RqJ5Qsfp81-4BKbVSX0-tDkLS9dyCOm_46gbnOGF68unt7uUhiBNXfBz7ZZ_IcrO7xI76ijmlCz4jN8_iYxKMnuRTdZnuUD-fTHf0ZrZkwbaX5aOqe8TBdqSBtKyQTJP1ep_YN5ZwmnnzKgzSmG0OTrFvyU1RnSU61KDc8vnD3lAkY294k9PhcoRI9gxOwMVb4rQdgEgk3grT2E2YVTh4Q-l5Qd5KsGyIt99VwNBd_ExPEhP7AzLNDzvdUql_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0144dd6d2d.mp4?token=sVAa5hPz7-La5o5TD3GMzO2lEPDgE5mjo-RgQKlmT3dK5C7VOM8Gj8TJ7tCB9mKOOVPKdKlIUDb_ce4-iDfP3mN5RqJ5Qsfp81-4BKbVSX0-tDkLS9dyCOm_46gbnOGF68unt7uUhiBNXfBz7ZZ_IcrO7xI76ijmlCz4jN8_iYxKMnuRTdZnuUD-fTHf0ZrZkwbaX5aOqe8TBdqSBtKyQTJP1ep_YN5ZwmnnzKgzSmG0OTrFvyU1RnSU61KDc8vnD3lAkY294k9PhcoRI9gxOwMVb4rQdgEgk3grT2E2YVTh4Q-l5Qd5KsGyIt99VwNBd_ExPEhP7AzLNDzvdUql_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاركة السيد مقتدى الصدر بتشيع السيد القائد الخامنئي</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/naya_foriraq/81643" target="_blank">📅 08:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81642">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b91606094.mp4?token=vEWGfVT4eouz6mUa5bBoIQdLkRR3nsGP17Bl0qIlmniPQ1W3oSiqQiBLMeK0B55H5ClsKiNxi6_CBtnkmwqZTxOg3PiHXQH0Jk98SIhMBcCcAGMVrTqxx4FiDIqCltjmvYZJ7lb9pP_DyQRdonrq4hBH0OvXAr2HICA9WplZLvvTk1usjOIJKYR-fLyTfyHpIt41Q1XHVxQUvEbX6AOF2KEwlyfuU0I7kshGMfBCi0dnwzEU-dc80bYdYoUl2R-qyvt5L_N4x8D83Zt8JWIyHTfs8TubxxO8h8OOBi2HnT_X9ploM1IblXRb6MFN3wFeOH6U9Wcuv-60fqSHWbGItb0YKCOm142lu1QTg2VAJTbzheJyGTtE4x0ax_xZdUV1CdrwTYbpap1y3j_bb37PPr0JPQyQuK5lO7oEl3QrrTW4UpLDPuQQ34Dst3ZKXhcYb6pE2Kt3zB8zJkUGVmioAGtn6ecm3aGtVd_gQ95LiZnmxs3Dae5W4a3dbbGR-vuvWZwZyACGpDGAadIdQW3o2mkfKl4ynefU9PSkCPH2p-n9j2M36XuxPQiDCzRaa0bW1Qy417Dygpo1q0sraTgz_WSHiPoRd2vA4rektJHbSqPRDKFGetL6cgLY9w3aH9U-4Wk5xRFjZIzFrExETjlbBLQNCNIn9iOnPOqEY6WATo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b91606094.mp4?token=vEWGfVT4eouz6mUa5bBoIQdLkRR3nsGP17Bl0qIlmniPQ1W3oSiqQiBLMeK0B55H5ClsKiNxi6_CBtnkmwqZTxOg3PiHXQH0Jk98SIhMBcCcAGMVrTqxx4FiDIqCltjmvYZJ7lb9pP_DyQRdonrq4hBH0OvXAr2HICA9WplZLvvTk1usjOIJKYR-fLyTfyHpIt41Q1XHVxQUvEbX6AOF2KEwlyfuU0I7kshGMfBCi0dnwzEU-dc80bYdYoUl2R-qyvt5L_N4x8D83Zt8JWIyHTfs8TubxxO8h8OOBi2HnT_X9ploM1IblXRb6MFN3wFeOH6U9Wcuv-60fqSHWbGItb0YKCOm142lu1QTg2VAJTbzheJyGTtE4x0ax_xZdUV1CdrwTYbpap1y3j_bb37PPr0JPQyQuK5lO7oEl3QrrTW4UpLDPuQQ34Dst3ZKXhcYb6pE2Kt3zB8zJkUGVmioAGtn6ecm3aGtVd_gQ95LiZnmxs3Dae5W4a3dbbGR-vuvWZwZyACGpDGAadIdQW3o2mkfKl4ynefU9PSkCPH2p-n9j2M36XuxPQiDCzRaa0bW1Qy417Dygpo1q0sraTgz_WSHiPoRd2vA4rektJHbSqPRDKFGetL6cgLY9w3aH9U-4Wk5xRFjZIzFrExETjlbBLQNCNIn9iOnPOqEY6WATo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل جمعیت عراقی‌ها غيور در تشییع پیکر مطهر آقای شهید، در نجف اشرف.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/naya_foriraq/81642" target="_blank">📅 08:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81641">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba481ca1d.mp4?token=qRdRNLSdGFppNsBUM5s1z6_PQjS8j7x-KY3-1NsRqOH_0tUFNdAl7EtYpA6PhnBwUzUAb0DbTpue0zVpwWbqYp95rzzFQi7r3owSQ_ai3xMpgtarAtrN6YlZCojAw7K0W4GWZOs10joqwdEUWYcrsIJSTPI4iXNaRbDU_IT6m1vSSqT-Ak2UQToCqThe3DLxgAgV_4b3-nl94wUxnYxTs9ORAmrt5bZHxojfn_PJJ_lMKC6W6WQ2oPcezmfDUdS1fgCH4kLPcrlsXFkMBWIDwelKFZQeNFQB2aHFYUGV2MCisgGcm4mqoZmtuC414buHS-fztZy-hMCohty_eRzqhlXQ6NaiNgWMg7hX6--Fwj_NhRCQk_E5f2Zlg3S8NoZJWgcwdrDMcO-1sRMUQRDsUy0vfCVLdh_A2OrS9cKEGj9ZKJwj6uHRsN_SxcSmjCNL2Z6n2hQ3xpLkmuLkWC0WYdS9eZuBaPyKAaXZAoQmOUbZ5exshyOEIwAk1sX6LuKlT6GREOcTxUgtLB_XPs7NkhMyLjC8m5zps9W80-ZJm4ZbkdgUvY5xEGEK2NnvUzv16xwTnKbts9i4F5_GRRkp1k0xWknOYVihzBVHC3RJ-TccdrL296YE7aN7hjDk2YwRw-Z9B71MhmODlA9gnrVANoXqZTK90JgPvfj4CIo71u4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba481ca1d.mp4?token=qRdRNLSdGFppNsBUM5s1z6_PQjS8j7x-KY3-1NsRqOH_0tUFNdAl7EtYpA6PhnBwUzUAb0DbTpue0zVpwWbqYp95rzzFQi7r3owSQ_ai3xMpgtarAtrN6YlZCojAw7K0W4GWZOs10joqwdEUWYcrsIJSTPI4iXNaRbDU_IT6m1vSSqT-Ak2UQToCqThe3DLxgAgV_4b3-nl94wUxnYxTs9ORAmrt5bZHxojfn_PJJ_lMKC6W6WQ2oPcezmfDUdS1fgCH4kLPcrlsXFkMBWIDwelKFZQeNFQB2aHFYUGV2MCisgGcm4mqoZmtuC414buHS-fztZy-hMCohty_eRzqhlXQ6NaiNgWMg7hX6--Fwj_NhRCQk_E5f2Zlg3S8NoZJWgcwdrDMcO-1sRMUQRDsUy0vfCVLdh_A2OrS9cKEGj9ZKJwj6uHRsN_SxcSmjCNL2Z6n2hQ3xpLkmuLkWC0WYdS9eZuBaPyKAaXZAoQmOUbZ5exshyOEIwAk1sX6LuKlT6GREOcTxUgtLB_XPs7NkhMyLjC8m5zps9W80-ZJm4ZbkdgUvY5xEGEK2NnvUzv16xwTnKbts9i4F5_GRRkp1k0xWknOYVihzBVHC3RJ-TccdrL296YE7aN7hjDk2YwRw-Z9B71MhmODlA9gnrVANoXqZTK90JgPvfj4CIo71u4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه رسیدن پیکرهای مطهر خانواده آقای شهید به حرم حضرت اباعبدالله الحسین عليه السلام در کربلای معلی.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/naya_foriraq/81641" target="_blank">📅 08:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81640">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
🇮🇷
فریاد "لبیک سید مجتبی" عراقی‌ها در نجف اشرف.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/naya_foriraq/81640" target="_blank">📅 07:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81639">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFTps_9oS8nU3PhKfSWpj7N7vjBXSzRjDuZW4NCwkz9-ri-bwLN23SkLbx3m0_LBlvudovHEi2givn13ccSFzkO_Pow0I7rC1tipCVfG1tynaIyZWz5TStlElkcwiFg5sXA4UgqB9g2OvKyzPfD9hHn2Q0siHTP5BFv9KQjCQw5hp9JQZ7zlo4rXEik9C3hWdz8Yjs4xhjREUeMFt4yoVasE2ckm4AIFfepz0HUc-NzV86d40t3H92AjYVfkq3YoZPY0knbwzW-Ww5_7YMk_6DvEeGjkrKRL9thHBKihCk7eRHr5tUbaoat_zNo1dQHpO_qO1V22yCv14ZfYA3KRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زعيم تيار الحكمة السيد عمار الحكيم يشارك مع الجماهير تشيع السيد القائد الخامنئي</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/naya_foriraq/81639" target="_blank">📅 07:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81638">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b86baa7e.mp4?token=G0W3IXih_Jr0aeY9mwCFeT6W1EG74a0dvVop3hsC8GmUxpesyXRc2AA1tzUfNNXsdcQrux0LBR83po56W_94j6AQxg40EkojxkK0m_NvSDDyIZN6ysBHACSRskfdFvezK68wqTRdJpU_IY1wBJlChwuZ_jXB-TJFs3-CLSUQoAkByiJlrJJCZIwaApw5oCIApjG0rDJJB-oPk7zC6d7cFc8pqPOFRoNHPKvSWzFdl5x_8LmN82oeQflPCobkYTpZVeUxommyHvpw82jCbjzkX-wLU74XiZx5xF-js6P7hbh2cVR3Z2letPMsU9T_hOvupjQblybOKr10C3V5cj4GJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b86baa7e.mp4?token=G0W3IXih_Jr0aeY9mwCFeT6W1EG74a0dvVop3hsC8GmUxpesyXRc2AA1tzUfNNXsdcQrux0LBR83po56W_94j6AQxg40EkojxkK0m_NvSDDyIZN6ysBHACSRskfdFvezK68wqTRdJpU_IY1wBJlChwuZ_jXB-TJFs3-CLSUQoAkByiJlrJJCZIwaApw5oCIApjG0rDJJB-oPk7zC6d7cFc8pqPOFRoNHPKvSWzFdl5x_8LmN82oeQflPCobkYTpZVeUxommyHvpw82jCbjzkX-wLU74XiZx5xF-js6P7hbh2cVR3Z2letPMsU9T_hOvupjQblybOKr10C3V5cj4GJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
فریاد "لبیک سید مجتبی" عراقی‌ها در نجف اشرف
.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/naya_foriraq/81638" target="_blank">📅 07:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81636">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d48fd446.mp4?token=XwdbMCT3WJ-euH3inp6EAPAp3wai3HZin1OpvjrGHcpezcOR6sswbwpYZ-t1PiH_z7nWPABbpm0lhphkSHysVFnXmUUy8hQA-jA7S31ty9r--Knl35p9tzzXEBzZ6zdsw5LGuqpqNZ082jrAaP-4IbaQiVDUSkzOflu9txnU_04M8ohDMCbSOv4q6vZTK--bWI6yJI9j07PCodiB3moay4ZFYHnNdHu9rdiev_ekF62fq_pnnfC3baHdBqlCO16yGDK1EGrK_rQKtDTQAan0GxOcFEvH4mmGDVxzty_KELQbUlzgoT4Vj-SEBuLCzlZKQe3bEetgM1VqIgsc2eIXtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d48fd446.mp4?token=XwdbMCT3WJ-euH3inp6EAPAp3wai3HZin1OpvjrGHcpezcOR6sswbwpYZ-t1PiH_z7nWPABbpm0lhphkSHysVFnXmUUy8hQA-jA7S31ty9r--Knl35p9tzzXEBzZ6zdsw5LGuqpqNZ082jrAaP-4IbaQiVDUSkzOflu9txnU_04M8ohDMCbSOv4q6vZTK--bWI6yJI9j07PCodiB3moay4ZFYHnNdHu9rdiev_ekF62fq_pnnfC3baHdBqlCO16yGDK1EGrK_rQKtDTQAan0GxOcFEvH4mmGDVxzty_KELQbUlzgoT4Vj-SEBuLCzlZKQe3bEetgM1VqIgsc2eIXtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنا النجف الأشرف حيث يُشيَّع الجثمان الطاهر لشهيد الأمة وقائدها الإمام الخامنئي على أيدي أبناء العراق العظيم.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/naya_foriraq/81636" target="_blank">📅 07:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81635">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">المتحدث باسم جيش العدو الإسرائيلي:
وقع اشتباك يوم أمس بين عنصر من حزب الله وعناصر الجيش الإسرائيلي داخل المبنى الذي وقع فيه الاشتباك يوم الخميس الماضي في منطقة بنت جبيل.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/naya_foriraq/81635" target="_blank">📅 07:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81634">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d414d1b2.mp4?token=MKhW6w_iVuRurx-kNd0PvDNRwWXImxnkvq4lk-VJkRcDsE3PzfQ5RCPfrnVPYN4mHW0ngXUDT8LX0Q9YUUGNapnimxOsFg0D_Fp7mREQolgrkVaPayn07PKGHbQGNuKKG69E7fwcjRIMVBM69RjjJvIoVSwjimJtCwEXwq0E9qpOyc_x5iXfuPUjxQAG7hdHDIudgOsj4dv-Y42H9yEyxJPtTN3HP1otcpdk6YbDAuU8LIkXEYUqXG4kJs3V8vetwvYlRtbSHKKoFdYmq9ZmriLydazmfA1bTfTnKMncZw9-Cb_Z9IEAB1Sx4lysn1_oiEIDxRbGLRvTycsFF4cWraID5VkCVK3pkqAPgryfOhlWA5_7x04-LHpBmss1sLjQJDdJJnwMojIjVjj_6PB0psNAR5pSA9Vkc37lLMmjRbfuuqlDPuex3y_DdMzlaYQLZKsAN_uIw56zN_SDcn9Z8p24EiyRsgxM6A1g8xIhQbZl7cHhoAZSzvc5Xdznctq9mRKtBx0FfSJjZRPTl5kr_lIsEynN31WO3iklWOmNZoRC-Qjj-QsMe7PMaDUC_Dzdg0RouuLfy5kCVrXg-lYn2t46hZtMNmTmh_4fjFbdiDqXMa8L28-KNcvtpLdj9RWm9_BhsFg7zpqjfzVxxmwYXeVj5-rACqI6L7e3uZeeWRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d414d1b2.mp4?token=MKhW6w_iVuRurx-kNd0PvDNRwWXImxnkvq4lk-VJkRcDsE3PzfQ5RCPfrnVPYN4mHW0ngXUDT8LX0Q9YUUGNapnimxOsFg0D_Fp7mREQolgrkVaPayn07PKGHbQGNuKKG69E7fwcjRIMVBM69RjjJvIoVSwjimJtCwEXwq0E9qpOyc_x5iXfuPUjxQAG7hdHDIudgOsj4dv-Y42H9yEyxJPtTN3HP1otcpdk6YbDAuU8LIkXEYUqXG4kJs3V8vetwvYlRtbSHKKoFdYmq9ZmriLydazmfA1bTfTnKMncZw9-Cb_Z9IEAB1Sx4lysn1_oiEIDxRbGLRvTycsFF4cWraID5VkCVK3pkqAPgryfOhlWA5_7x04-LHpBmss1sLjQJDdJJnwMojIjVjj_6PB0psNAR5pSA9Vkc37lLMmjRbfuuqlDPuex3y_DdMzlaYQLZKsAN_uIw56zN_SDcn9Z8p24EiyRsgxM6A1g8xIhQbZl7cHhoAZSzvc5Xdznctq9mRKtBx0FfSJjZRPTl5kr_lIsEynN31WO3iklWOmNZoRC-Qjj-QsMe7PMaDUC_Dzdg0RouuLfy5kCVrXg-lYn2t46hZtMNmTmh_4fjFbdiDqXMa8L28-KNcvtpLdj9RWm9_BhsFg7zpqjfzVxxmwYXeVj5-rACqI6L7e3uZeeWRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العلم العراقي ورايات المقاومة الإسلامية تحيط بجثمان الإمام الشهيد السيد علي الخامنئي خلال التشييع في النجف الأشرف.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/naya_foriraq/81634" target="_blank">📅 07:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81633">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c202b369.mp4?token=Cqf4C_kaQSlsJfxM6EXqY99nQRL4dAB2TbIS3TYtdopMp7nzhtTde7jsXgUVl1tUvSLLobFmGJMLlh9lUFcNnNDGMi54M3ikayn3XZCWSs8zAIaza_a2FcAsRGN2Bn4NBuvFw76bQZdtZM2oPpHNFy_OHtGrI4URDJipKfO3O3tvp73Kh2ZxLvn6jqUtIrVHEe4bpb-GzCZrUsLQM-AhrIJ6ryoz8iyia9A2c9cUiUxcNRjI4FP0H_rso0Fhbw6GcKR6DndnlriWJWpo-aYhDufRx938xqMAY3v46BGDgn5Bg8yjEHp6T9ru0n8PazRKA_rnnlZHYjjprADWG_FuYxEqzRTneH6f5fvWxMd2PD3AFzK5uUVtL5u5IlJCWpTkUGYIkKQwuaGlIPe-uWb2l5oajPMHEGSNUC9mtKempX_7by_2GpGpD8Khus04dz6PjVVSkkLHGjDe8tzOLUPJTjBVd1PCj7iL9ag6zetFE6_kis7535y-IFfV61sx-isdwztFKVuHeyYzqVR4MVOSS7Kt3ns2LsljgcYLBa9xAWXUQ793SKGacHAkXyvE_Ki4WyMDf8pMb99zaRb7vfKxqwWuO9TWEhEUYfcj2m2SJDQGDYGFFxPwFgQV45JSwKn6zfTiGR0WZKu4_yEFBa4lUHHF61__TnhYcnkLvcvfoC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c202b369.mp4?token=Cqf4C_kaQSlsJfxM6EXqY99nQRL4dAB2TbIS3TYtdopMp7nzhtTde7jsXgUVl1tUvSLLobFmGJMLlh9lUFcNnNDGMi54M3ikayn3XZCWSs8zAIaza_a2FcAsRGN2Bn4NBuvFw76bQZdtZM2oPpHNFy_OHtGrI4URDJipKfO3O3tvp73Kh2ZxLvn6jqUtIrVHEe4bpb-GzCZrUsLQM-AhrIJ6ryoz8iyia9A2c9cUiUxcNRjI4FP0H_rso0Fhbw6GcKR6DndnlriWJWpo-aYhDufRx938xqMAY3v46BGDgn5Bg8yjEHp6T9ru0n8PazRKA_rnnlZHYjjprADWG_FuYxEqzRTneH6f5fvWxMd2PD3AFzK5uUVtL5u5IlJCWpTkUGYIkKQwuaGlIPe-uWb2l5oajPMHEGSNUC9mtKempX_7by_2GpGpD8Khus04dz6PjVVSkkLHGjDe8tzOLUPJTjBVd1PCj7iL9ag6zetFE6_kis7535y-IFfV61sx-isdwztFKVuHeyYzqVR4MVOSS7Kt3ns2LsljgcYLBa9xAWXUQ793SKGacHAkXyvE_Ki4WyMDf8pMb99zaRb7vfKxqwWuO9TWEhEUYfcj2m2SJDQGDYGFFxPwFgQV45JSwKn6zfTiGR0WZKu4_yEFBa4lUHHF61__TnhYcnkLvcvfoC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاصل نايا  قبيل انطلاق التشيع ازقة النجف تخرج عن بكرة ابيها لاستقبال الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/naya_foriraq/81633" target="_blank">📅 07:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81632">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d9a8cb9f.mp4?token=lt0KVm8GON2ZX4RjDG4SgT5GdS65cekCW_TpSE1cgu9PRIREbFAkZT5k2foK-O1L-SGR2GmMk4KvpPCylIkf0kVGDemBJ3DE0ecyLVzVLksD5aN1T6v2Fo3boxnRSj7ZvpoNWYjGPjOIYFw9HKFmjGm5kUpFgc7mZde2lf_t4qBLxL1F82ePY29t6hAZRtE0fjFSaES9ayMSD8wsrusjM-BBQj95PlCthGrr7tBSdsqX-OhRoev0wyEF-Lw8kyIsHYqNRp0MYvko5ClCwFWHY9nvNQsj6U4C9ryPhNnw3yR57kZyfgE87qBQYOHBdMzYdd3zdCodZw7LOLLg55a62Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d9a8cb9f.mp4?token=lt0KVm8GON2ZX4RjDG4SgT5GdS65cekCW_TpSE1cgu9PRIREbFAkZT5k2foK-O1L-SGR2GmMk4KvpPCylIkf0kVGDemBJ3DE0ecyLVzVLksD5aN1T6v2Fo3boxnRSj7ZvpoNWYjGPjOIYFw9HKFmjGm5kUpFgc7mZde2lf_t4qBLxL1F82ePY29t6hAZRtE0fjFSaES9ayMSD8wsrusjM-BBQj95PlCthGrr7tBSdsqX-OhRoev0wyEF-Lw8kyIsHYqNRp0MYvko5ClCwFWHY9nvNQsj6U4C9ryPhNnw3yR57kZyfgE87qBQYOHBdMzYdd3zdCodZw7LOLLg55a62Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاركة السيد مقتدى الصدر بتشيع السيد القائد الخامنئي</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/naya_foriraq/81632" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81631">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فاصل نايا
قبيل انطلاق التشيع ازقة النجف تخرج عن بكرة ابيها لاستقبال الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/naya_foriraq/81631" target="_blank">📅 07:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81630">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تشييع مهيب للإمام الخامنئي الشهيد في النجف الأشرف.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/81630" target="_blank">📅 07:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81629">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حضور مليوني عظيم في النجف الأشرف لتشييع قائد الثورة الإسلامية الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/naya_foriraq/81629" target="_blank">📅 07:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81627">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6726247e.mp4?token=QHgegov5EPF9jF8kJQfxPg2XbBU6ioB57HlhQtLX5RCFw3Dm7jTV0afx6ofm5phj6LzL9Zc01HluZEdxMaj0Wj0qfLop_h9x_mOBr-B3gpTFhngQtYAsEiKl8KqT-Lc4PFgvCh4ty7l3NUSk9i3dLsQ65l9xSwx2MF747Whu10pTpDTMMtcSAs4Z-ko_Kew70EKu17Nyafc6lp7tEY4nXa30QvDy7ZpvT2f2S9Fd8uPvhxaTjWQZmZDgbrokbSmCcWJ1CNfLkKSJRaZ3pNUNpU05YeEeKXFnyWqYTqXZr0amjMJyL1m41WxxZvXgKBniBenmGjzHEGWo--h2_DxpGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6726247e.mp4?token=QHgegov5EPF9jF8kJQfxPg2XbBU6ioB57HlhQtLX5RCFw3Dm7jTV0afx6ofm5phj6LzL9Zc01HluZEdxMaj0Wj0qfLop_h9x_mOBr-B3gpTFhngQtYAsEiKl8KqT-Lc4PFgvCh4ty7l3NUSk9i3dLsQ65l9xSwx2MF747Whu10pTpDTMMtcSAs4Z-ko_Kew70EKu17Nyafc6lp7tEY4nXa30QvDy7ZpvT2f2S9Fd8uPvhxaTjWQZmZDgbrokbSmCcWJ1CNfLkKSJRaZ3pNUNpU05YeEeKXFnyWqYTqXZr0amjMJyL1m41WxxZvXgKBniBenmGjzHEGWo--h2_DxpGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سيل بشري في النجف الأشرف يشارك بتشييع الإمام الشهيد وعائلته الشهداء.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/naya_foriraq/81627" target="_blank">📅 07:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81625">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c734f5ee1.mp4?token=QjqlJkyaaA269_1Sp5A_wQki1Ork74Slf7y4Jb3HI1P6NedUKCxJT0tyPNB-N4PoX1MxnLkZWFrEk4R_0v6m5orut2VRqROzge_0rvAR-hI2OtYXzwKV2NWGT3lX8NJA5upFjiQbs83m3PcFdqwwN_w1hbm7LfWgEMZZ7cjfVYHXJAHdoNPSArXhpQwl5ryxRp2dPtymmFFkm2x1SQ97tFRz3C7cgTUC67vKlS0sUc7w5hkqIsqTUrhqkKJsZqZ-X8179HtztU_hKeuoNdM-YYuyacJUp2rPhSih8shhDJpIZMSBaSZi3hy4elOQ4rMFRHXbetAsEedIB0jYQ6HWnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c734f5ee1.mp4?token=QjqlJkyaaA269_1Sp5A_wQki1Ork74Slf7y4Jb3HI1P6NedUKCxJT0tyPNB-N4PoX1MxnLkZWFrEk4R_0v6m5orut2VRqROzge_0rvAR-hI2OtYXzwKV2NWGT3lX8NJA5upFjiQbs83m3PcFdqwwN_w1hbm7LfWgEMZZ7cjfVYHXJAHdoNPSArXhpQwl5ryxRp2dPtymmFFkm2x1SQ97tFRz3C7cgTUC67vKlS0sUc7w5hkqIsqTUrhqkKJsZqZ-X8179HtztU_hKeuoNdM-YYuyacJUp2rPhSih8shhDJpIZMSBaSZi3hy4elOQ4rMFRHXbetAsEedIB0jYQ6HWnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس اللجنة الإعلامية لتشيع السيد القائد الفريق سعد معن يعلن انطلاق عملية التشيع الشعبي منذ أكثر من ساعة في محافظة النجف الأشرف</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/naya_foriraq/81625" target="_blank">📅 07:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81624">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9eb9d8e47.mp4?token=oS6Jg4OGYBIGf00UCJjC6j8kHIZ0Sf43y7tPzIietIUHY6FOgxzvlj64XtTgPCS9pROLo1NRMo1T17Fg967zyZ_rvy185QY_csj6qbODZ9XrBJojzlXk17jwOQVXDopJN-nyBIxuXaDsCe6ge5ZIDil3wqYnJK627X7ylj_cpMHNDS_ug-xeDOcGWDpGmUHjZCBfLE238gJ8y8onehIULSv59g6IiM4dUaQCyZ_1OU1h1dzork7AJ1qSdFEGmINpzLaTFRvi6bp4M5wot0q2S4ES0Yq0oRxaxENU8KXFdVUNcpUSQWQv7_vsKEy00J81COGvUtZGLnXRUJUc5wXEnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9eb9d8e47.mp4?token=oS6Jg4OGYBIGf00UCJjC6j8kHIZ0Sf43y7tPzIietIUHY6FOgxzvlj64XtTgPCS9pROLo1NRMo1T17Fg967zyZ_rvy185QY_csj6qbODZ9XrBJojzlXk17jwOQVXDopJN-nyBIxuXaDsCe6ge5ZIDil3wqYnJK627X7ylj_cpMHNDS_ug-xeDOcGWDpGmUHjZCBfLE238gJ8y8onehIULSv59g6IiM4dUaQCyZ_1OU1h1dzork7AJ1qSdFEGmINpzLaTFRvi6bp4M5wot0q2S4ES0Yq0oRxaxENU8KXFdVUNcpUSQWQv7_vsKEy00J81COGvUtZGLnXRUJUc5wXEnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملايين من المشيعين يحيطون بالجثامين الطاهرة بالنجف الأشرف</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/naya_foriraq/81624" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81622">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b515fb2d.mp4?token=GCmjBPOqcEkcAbYM6lvvfIBHCvZ1D3u05d1Zl9naJxru5hdB6WaQpZB-oXVEMYLrDZ6VQdSKB2ueUXdoS-sLQMhZG6Kc0ktRj4H_ydJyHz05QaT0a5yToPbYdNYZpV1-hKGYJj6lILn8_9RJi8ebnSus-DClIZvegBbEdJdLYtsTPj7JHSS18Xk1PbpagQVmWpIdUTjEBlo-05oDpW2qEct_ST28f94iEig9H71CzNDK-mXpc-Noeuxiskg6EVKIxjBRx6TqmIiv6VzbDW7wv3WhR4tHZzTafh-alGytrtpLcFgB1Vn-Vy4UbSVwrcknRpS8FUvy1y7X2zbOS3KX-Lg9AstiTqATPHPmcFz4GCUnjI65uTfi-Wr13zjP2pv14FjkmYOifvMv0L0mCVYmlHRgqx1ExCIbONlCt6KURQuDV88xXSFP1Z_8Wy3Hap_hJuk8to44PU_NM5sETv4AL58B4pryQvFBUrkFyRjg4IfXubXn88jJCqhGbJRxRn7m2qxZ6ortIQ4WF_FJPKoGMjHJvkKY7AZrvYrJNnN8A7R5nQIOn0gjCdvqYmUID5RoL9IC7Pa5tVG9T7sjMssFnx8vJHs9D-fthDqeXEA9D9v7Rd_rvm5zjkwUF5Tpa9vZYvzIQdh3U7IdKYniisqdDAKMF5iESvLjYXapnppY0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b515fb2d.mp4?token=GCmjBPOqcEkcAbYM6lvvfIBHCvZ1D3u05d1Zl9naJxru5hdB6WaQpZB-oXVEMYLrDZ6VQdSKB2ueUXdoS-sLQMhZG6Kc0ktRj4H_ydJyHz05QaT0a5yToPbYdNYZpV1-hKGYJj6lILn8_9RJi8ebnSus-DClIZvegBbEdJdLYtsTPj7JHSS18Xk1PbpagQVmWpIdUTjEBlo-05oDpW2qEct_ST28f94iEig9H71CzNDK-mXpc-Noeuxiskg6EVKIxjBRx6TqmIiv6VzbDW7wv3WhR4tHZzTafh-alGytrtpLcFgB1Vn-Vy4UbSVwrcknRpS8FUvy1y7X2zbOS3KX-Lg9AstiTqATPHPmcFz4GCUnjI65uTfi-Wr13zjP2pv14FjkmYOifvMv0L0mCVYmlHRgqx1ExCIbONlCt6KURQuDV88xXSFP1Z_8Wy3Hap_hJuk8to44PU_NM5sETv4AL58B4pryQvFBUrkFyRjg4IfXubXn88jJCqhGbJRxRn7m2qxZ6ortIQ4WF_FJPKoGMjHJvkKY7AZrvYrJNnN8A7R5nQIOn0gjCdvqYmUID5RoL9IC7Pa5tVG9T7sjMssFnx8vJHs9D-fthDqeXEA9D9v7Rd_rvm5zjkwUF5Tpa9vZYvzIQdh3U7IdKYniisqdDAKMF5iESvLjYXapnppY0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملايين من المشيعين يحيطون بالجثامين الطاهرة بالنجف الأشرف</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/naya_foriraq/81622" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81621">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الحرس الثوري، : استهدفنا ٨٥ نقطة عسكرية أمريكية ردا على الاعتداء على إيران</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/naya_foriraq/81621" target="_blank">📅 07:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81620">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGJir8uhZdTV7oc0eM-Lh3cITtLOc5AeDDRgEzdfhHOGFWsdfHA6DnwuuTJFnodNxt2OXi_y_HFL1Zlg5w4_w2QFIL54InxVR6NuPOZkT6ovxVy8ifAx4eEm3dyJZCky7dvyWcNiyBRCtXbqQSMP_ZwGSmaOVveCkkpMm2t3nSgBkx7c-3E4Qgm_KXS9-kKqwNIJBuFKTczEB4Oi3Lq2U4aPaURN2pspMtLsRkXmqoZfZQBjFYElkdUZEuX3w5ocflPIX9tRvpRLI21WAIC2nsZFKCVUYdVAWoMtBd4h-I3gEoufzH_WREL7qx9IxD7DFhbdGHQNzcG8eoFDMlqUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أعلام الثأر الحمراء تتوسط الجموع المشيعة في محافظة النجف الأشرف العراقية</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/naya_foriraq/81620" target="_blank">📅 07:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81619">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مرور نعش السيد القائد بين المعزين في محافظة النجف الأشرف</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/naya_foriraq/81619" target="_blank">📅 07:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81618">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a1f2f805.mp4?token=BO5ZPeVCd81ghK1giER-JH6qwKm3sl3KJ-lbJKImC6Ios4VSIQMWzviYBLX5VwLZfpZNnZ8e8bGQtkfGQi-8Mz2_Xuw2FKdfLLshuazMF8KsK20idlBBUpYFmp85mCbqegEa2wwdcIlYYc8EPgdub-1u2m-8ahQknmG0_HMToGn4-VhTUkcmrq53ADBNCGv8JN56GBe47z26_nSVVv_fd8yuNZapaQvESgF4Ze-z1UBdnVpXAGLQLrtbOApmywiKhckag9shxbxS6dPTOAMc1a8ymOYN-33cNFv79HG4Al8AJIXNLtIEXDkCgdD1AFZt47z2nQslWXk1EL1i8_OG2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a1f2f805.mp4?token=BO5ZPeVCd81ghK1giER-JH6qwKm3sl3KJ-lbJKImC6Ios4VSIQMWzviYBLX5VwLZfpZNnZ8e8bGQtkfGQi-8Mz2_Xuw2FKdfLLshuazMF8KsK20idlBBUpYFmp85mCbqegEa2wwdcIlYYc8EPgdub-1u2m-8ahQknmG0_HMToGn4-VhTUkcmrq53ADBNCGv8JN56GBe47z26_nSVVv_fd8yuNZapaQvESgF4Ze-z1UBdnVpXAGLQLrtbOApmywiKhckag9shxbxS6dPTOAMc1a8ymOYN-33cNFv79HG4Al8AJIXNLtIEXDkCgdD1AFZt47z2nQslWXk1EL1i8_OG2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أعلام الثأر الحمراء تتوسط الجموع المشيعة في محافظة النجف الأشرف العراقية</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/naya_foriraq/81618" target="_blank">📅 07:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDJpB0eKo9RyBRbaiKRCb50snGTbhGH4-l_7x2Kw59y_OdiM7r9ivm7b6ZqGkBWbtlwg877fpAz3TjA0dpAsB_glg5uRA6I-V7uG1oGXhfjWc8bDgMiLIE15AHtAlUrIk0p1S09yNIFJD1gqRihGeXb0Jm4UhyJPFOMOsptDk_spl7-_22iYRw7o8JOhWg0RHlSuxrxRMXVGfqkJMmzOedF9YmO6yK450ENhuFC6mXZEikyDcMWr_6jeh8mkbLcd9I62ewI3Jd3ohenFIn4QFFdi7GyGK__NCdJbTGBVDEkhde2tngogT6IypZAAiN2s9D2f-fwDyYSDmW4GAc0iXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0zUBMrN8S54W_avH8pry4Oqg8ARYLYmgIr_ktS8r3Vdfhmsru7l1BQl1loi3kRYV5SqlVdzbKs6XqyWBWt8XSux9XjqJgruxFMGHV3ArFXm22P7cCVjj3SMBzCXlHNaUPjsdwDTqyBjniM82J6IcVoHbRYrp2YUavIYsU9lej2-as2sw-nhcq1i3r4BjqA_qR9nl_pA_hI9tl3stoGrGu2X2D2UTSwzqgxNK3zFNwEDxd-Xh5rPjkT_hqRV0OZeMtKnIs5cneHz5t2ZIIgWifVSfRlP6AvjmUYYzMJxg3I3dlskDr-YONUKzTrjk4Sl1yGm25NGOR78bsNgt3D4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmWv9zdMZsR2NlZHmJRPdv_MV4SDC8BdqgcCKkd6Zn6O821YPaQJLdtUcNa66q7kH1OC5frupMpAngrKtlH_y7NsFud6ssym2vudgnm7NXN285l214rVHK3Mo3wLCN8NceAoYSaY6xWC60bojcuBXImi0C3bzFwtCdza6jpzDFEv7S-N2kuEwDfTu5Ko8qNaFBss6MzxsnR4T5FfuVbU4hj1GoVCPQOiIq-4gou7VUkhHmwO3x1uh8Oi2L-3rOiS0uQwZHXMu_9VamG2ll_bP9jxsbewIer1YFChGIytHVvI1_dBM1LxOQSldO9SvXewr6c84fGnLfBiMu8j0axLLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0I7qFR2tnUECMFgrIRSUqEqt_YFHY-KhJnaxDRirVG1482S7KUntAgoaxjv6r2d4oKxqaU9k16qjnZ8v9Y-rr5WMYpc876nSMgKe0OoootGu3rUaR_RVsgfO3CBEbdfOUsTkFijUFyVrBsiopuD8ZoF5nM4iDHrWQaFezeWwnnlaq1Y1lb0CNdsFnlI_3OsbvQgu5uevAbTix3bsoq4meQsrTcYLQtzb3lnsEEV5Ix9AVUiUG2jKUN8H1XT5UGEZhEImreLlGOKp2CPk91ZR3z763jOHmG8PIjMQK0cb5fkW6I2NFqE0cQ1ML_6GI-IwRaaBET7XpEbbowpfLXR0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جموع مليونية جاءت إلى تشييع وتوديع إماك الشهيد في النجف الأشرف</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/naya_foriraq/81614" target="_blank">📅 06:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81611">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94a03fac0.mp4?token=rYdzmiV6kisxft72d9pvGj-crN7z9HiM7avBTWHyiOdNXHBAE5B-i8w83cmcuYjlxu-0nybuhR-Q0AbDA3HFmVOih7nnPh8lwywm1nAgDP-lbnO-AoJbNZdQd0wFLqXBx-pTWu8EMLPBwXFs9dWLbMb8eiDc4HOsi_lO8rlU6QlCIJlxm8RcoZt8bAymB7_QcfY668siN1NiCyyHxUGxhlIbmiECZJCxM84z5SfxnYWLC6StzdPeOblYtClcw37UIS4njFNYY8LbgJ-Y82PA5cTn1oV7MwzklgsyPOYsyLcoV0UQBx7rJnJXEJGLzjGxskcTD6DZn6fm8EenVXoXzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94a03fac0.mp4?token=rYdzmiV6kisxft72d9pvGj-crN7z9HiM7avBTWHyiOdNXHBAE5B-i8w83cmcuYjlxu-0nybuhR-Q0AbDA3HFmVOih7nnPh8lwywm1nAgDP-lbnO-AoJbNZdQd0wFLqXBx-pTWu8EMLPBwXFs9dWLbMb8eiDc4HOsi_lO8rlU6QlCIJlxm8RcoZt8bAymB7_QcfY668siN1NiCyyHxUGxhlIbmiECZJCxM84z5SfxnYWLC6StzdPeOblYtClcw37UIS4njFNYY8LbgJ-Y82PA5cTn1oV7MwzklgsyPOYsyLcoV0UQBx7rJnJXEJGLzjGxskcTD6DZn6fm8EenVXoXzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای خراسان در میان مردم غیور عراق در نجف اشرف</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/naya_foriraq/81611" target="_blank">📅 06:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81610">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a264bb9b9.mp4?token=Bsd6MkCunUcJtSrlzfQ9A0-xLG5GMBg13xq1aQG7daOKWfhunuEWwyWo_nkz31vJviDHKHhWs0bzRf8TZ4JNhW3Gk-Hm3Frx5YIDtKClVV08JpKn8zQTJXu-G65bhmRdbEJJdEINK20xshRUf0WBEn84NKplrvgk0JOGNkRRS1J1cTuhG58FDq_I7C6qaSs5BJsJLtAqMGvYATSPVAZ0d5xwH0laN2uakALiFBxXF1IG3Fe1iOybbEzO8dGysOvh_tpQijDuhy_T8W_1VFAV-eqluEdV8aJjoDxg0OUSV_PEA-yFbXuDcK84-ii3JraWVSVU2-Aydz3e8AgHcfgwnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a264bb9b9.mp4?token=Bsd6MkCunUcJtSrlzfQ9A0-xLG5GMBg13xq1aQG7daOKWfhunuEWwyWo_nkz31vJviDHKHhWs0bzRf8TZ4JNhW3Gk-Hm3Frx5YIDtKClVV08JpKn8zQTJXu-G65bhmRdbEJJdEINK20xshRUf0WBEn84NKplrvgk0JOGNkRRS1J1cTuhG58FDq_I7C6qaSs5BJsJLtAqMGvYATSPVAZ0d5xwH0laN2uakALiFBxXF1IG3Fe1iOybbEzO8dGysOvh_tpQijDuhy_T8W_1VFAV-eqluEdV8aJjoDxg0OUSV_PEA-yFbXuDcK84-ii3JraWVSVU2-Aydz3e8AgHcfgwnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلا حقوق °°°  لحظة تشيع الجثامين الطاهرة في حضرة أمير المؤمنين لعائلة الشهيد الخامنئي القائد</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/naya_foriraq/81610" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81609">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الانفجارات في البحرين لاتتوقف</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/naya_foriraq/81609" target="_blank">📅 06:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81608">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b412db963.mp4?token=G5UykuhY7JGvYcQSCqQnHMNjmtiV7WWQ-E1l3bXghYOAb4mAqryi1QFoS9-5xS8YLBCT5s2FFy6QYvnulJUjoKu7HyinBGXj1S-q5PohXbM1dM-GTLqLqUvw0M7ard33LZWO_avToPvp54gg8zVmolf02XTs57sckd9qwOO1K1zHejinpAP2oyOcxIKDHNi5MFH-tDG27f1_kMj8FfWz8SXDz0NNivi1rIDyTQt9pPrQTfoZp5DCG8tKkjkpPvsCQpuFOeQMxahIqqo4cHeE7DArluCmYQz4M-PZBZEzZwmivotRiv9Ef69nRiFpLGi6hEQH4xZv4TF5lEY-ZktN8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b412db963.mp4?token=G5UykuhY7JGvYcQSCqQnHMNjmtiV7WWQ-E1l3bXghYOAb4mAqryi1QFoS9-5xS8YLBCT5s2FFy6QYvnulJUjoKu7HyinBGXj1S-q5PohXbM1dM-GTLqLqUvw0M7ard33LZWO_avToPvp54gg8zVmolf02XTs57sckd9qwOO1K1zHejinpAP2oyOcxIKDHNi5MFH-tDG27f1_kMj8FfWz8SXDz0NNivi1rIDyTQt9pPrQTfoZp5DCG8tKkjkpPvsCQpuFOeQMxahIqqo4cHeE7DArluCmYQz4M-PZBZEzZwmivotRiv9Ef69nRiFpLGi6hEQH4xZv4TF5lEY-ZktN8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلا حقوق °°°
لحظة تشيع الجثامين الطاهرة في حضرة أمير المؤمنين لعائلة الشهيد الخامنئي القائد</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/naya_foriraq/81608" target="_blank">📅 06:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81607">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/benc1oPWwQF1x5Pzd9L5_UGwBhHEE5aa5TzkdPQnc4Mc7mHpQMNTx1V1wUvtQz_qVJ1gBEvok0SjQwooqV5OuMqVs7QDXCjjhRkNBZnfGH8A_7FzR-ryZVFE6YHGDjQOHa8xL3W2I_TGkH-Dst3qTeBywNMGWcbicbGpXLjLfqd-ntO9XCe5SJh4z9UEHzgyg13VEf2W8gZMqDzj16JsNeL5MTvHUhOYO7QS_U4zbfQxCJ0687riPIGgebTwLDiordBx-ag7fVF0DOFc-wSHz_lGBQCW2hMLCpK0m3RmXDYPVYZUXt9OQ_WT9cGhLnABtVMkvmy864xowIhuxGW8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة تهز قاعدة على السالم الأمريكية بدويلة الكويت</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/naya_foriraq/81607" target="_blank">📅 06:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81606">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سماء البحرين</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/naya_foriraq/81606" target="_blank">📅 06:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81605">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بتشيعة طكينة أمريكا</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/naya_foriraq/81605" target="_blank">📅 06:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81604">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIOAJGVtahJ6zf7nAdQPda1_aremqVOIHD3mcrS1-KDZx_0Zqd_iSNmS_DOPIrqrqasiEOj8S2j3bRiSf3kj3j7felY_JXDezpQUfJYZ8I_3gZhzwHeWkTTjtgo_8Gpsvqoxta7imLVTifVeMQO5cFItuhIb4Dc0jUDBDB50d_ONQHvI5JDz9REeexClJuH_eKyuAYMq5Z9asRDepZXVoN7eyOK5Zr4jfBsc15Oqscp47QBs-M-SXkGT2pOhlOV5od_rUZMBM37YJ0Yjno0q3GgK34dv1Vh6BTwAOKc7KeLCQGA-dUlPkOEX1xh9twVivJ7k4wX9P6gE3OIRLYB97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في سماء البحرين عقب الهجوم الصاروخي الإيراني</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/naya_foriraq/81604" target="_blank">📅 06:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81603">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8493c96c3.mp4?token=D6xTC6KdHNlkk8vnIG7AQ4G8aDbdEViYG8v3m_x9L-19aseO6qvGy63ROSje7wOke7TqsMD19u-aCild8sC-RfcJEevP7ig6w7vDG0ajOiFv9Z3L65rIgK37g1SxQSoCV02621xN8dhlZotllRYgoi_sErdJkLrRTo1olMSdr-yskeqLmlqjBz7ys4rwIOymAKLzBOdj2IRYTmOiEF46X6bL7zYJnZot_s1q_kK_Z-OAU8EORNEfyn-TulJqOntMPPfu1UGmOVfzKUCyctTrcG0AIULHPSjjb7S95zIoX7O2GYtTZcDh2f0ndeL_8MhL0ZCCSoffV28Tp4HPEYCdcCgN-2sfZVUEv1yP-xYvpf_mfy0XOnOHBgl_kIcc8I1viIaeSATOEnx6lDjp1VWw8kqSzXuTihETp8JD_05SAbq-ycG7yl06nO74-wApc8NuscdKfS6dM1noYlLEnHVy9-0MIPNNHGvmsInU5LJ4_bF8ryRTcmzGy0zf0IU3sGg6nNKuUnH_FTUXopoBjRc6ofJf-8IHjLP8amy65Ud7Nz0ro_APsL3_uCDJ_ypdfCFn0iOhcBEuVckmpiaQYP388BLfuKUWW87lPLSwZxyoBFamJ1Uzdi8CFvKM7QJTCmS4Qei5gFXRVsswQI05GWn5kAw7Pp_oT1PsoH0ti1Sdx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8493c96c3.mp4?token=D6xTC6KdHNlkk8vnIG7AQ4G8aDbdEViYG8v3m_x9L-19aseO6qvGy63ROSje7wOke7TqsMD19u-aCild8sC-RfcJEevP7ig6w7vDG0ajOiFv9Z3L65rIgK37g1SxQSoCV02621xN8dhlZotllRYgoi_sErdJkLrRTo1olMSdr-yskeqLmlqjBz7ys4rwIOymAKLzBOdj2IRYTmOiEF46X6bL7zYJnZot_s1q_kK_Z-OAU8EORNEfyn-TulJqOntMPPfu1UGmOVfzKUCyctTrcG0AIULHPSjjb7S95zIoX7O2GYtTZcDh2f0ndeL_8MhL0ZCCSoffV28Tp4HPEYCdcCgN-2sfZVUEv1yP-xYvpf_mfy0XOnOHBgl_kIcc8I1viIaeSATOEnx6lDjp1VWw8kqSzXuTihETp8JD_05SAbq-ycG7yl06nO74-wApc8NuscdKfS6dM1noYlLEnHVy9-0MIPNNHGvmsInU5LJ4_bF8ryRTcmzGy0zf0IU3sGg6nNKuUnH_FTUXopoBjRc6ofJf-8IHjLP8amy65Ud7Nz0ro_APsL3_uCDJ_ypdfCFn0iOhcBEuVckmpiaQYP388BLfuKUWW87lPLSwZxyoBFamJ1Uzdi8CFvKM7QJTCmS4Qei5gFXRVsswQI05GWn5kAw7Pp_oT1PsoH0ti1Sdx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة جديدة نحو البحرين</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/naya_foriraq/81603" target="_blank">📅 06:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81602">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بتشيعة طكينة أمريكا</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/81602" target="_blank">📅 06:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81601">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/naya_foriraq/81601" target="_blank">📅 06:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81600">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/naya_foriraq/81600" target="_blank">📅 06:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81599">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/81599" target="_blank">📅 06:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81598">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/naya_foriraq/81598" target="_blank">📅 06:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81597">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b25147f9.mp4?token=aUWdcZP9u4k-G_v7OJhSTJVNf8AccY9I1qVYM9kuvUtM-osZcjzZYXsh8uNwpzq6S_bmnftzDQf9u4CqDdNOFDq-danNzGx8nlpeLjr7i78FmW-LBbz7KDQ47YujSYnWc9aMc3yQ1yfB4yrvPVHWeImRvDi-7GfwS6-lqooH12p4P678iGIzYNMi2gbdL28mOFv3XCvXskPJLPOwcOIVP9zYvAvb7L4Wnk89ETFtpuMMj-t04VgQXm4aYLzCzHfwae-VM7npk2xI9UaOp78ul-7LWpxDth0xelIvhmhu87JPBAN2Qg_DXqvOmxft6e8DKAQriT2d-U0kHXeszhf_zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b25147f9.mp4?token=aUWdcZP9u4k-G_v7OJhSTJVNf8AccY9I1qVYM9kuvUtM-osZcjzZYXsh8uNwpzq6S_bmnftzDQf9u4CqDdNOFDq-danNzGx8nlpeLjr7i78FmW-LBbz7KDQ47YujSYnWc9aMc3yQ1yfB4yrvPVHWeImRvDi-7GfwS6-lqooH12p4P678iGIzYNMi2gbdL28mOFv3XCvXskPJLPOwcOIVP9zYvAvb7L4Wnk89ETFtpuMMj-t04VgQXm4aYLzCzHfwae-VM7npk2xI9UaOp78ul-7LWpxDth0xelIvhmhu87JPBAN2Qg_DXqvOmxft6e8DKAQriT2d-U0kHXeszhf_zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لقطات مباشرة من مجسر الكوفة.
عدسة نايا</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/naya_foriraq/81597" target="_blank">📅 06:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81596">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الصواريخ الإيرانية تنطلق نحو الكويت</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/naya_foriraq/81596" target="_blank">📅 06:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81594">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eW7-SnJsUV8xtPta4o-vqF_tIJDcC-B6X4Nmp9UFkvAbqao_BDkdqAmN3LVOXUr5THc1rc8qD8XcZ9EnN8jwf7lq8OJ7v2SoQKUQiY426C4HYd1uB1thFbvyYJTT31Nah4-xp4cWXGlGY-oI-kI4KviWhGsDrOL8A1g4f4DDssEwxw3fSVGJir5vw4BSIJS80-0tlr_prpILCQKKXHHfoztsanJEWiPKcqVJRFWS1cy-dTtba0IWEA_1DJqVHY6qPIvmDo5CaH3tKyGZXdL1p9logPPZXMn4vS5ljiWAAU-leTuru87PwFVnK926BjQN6iHS9gkZP7d6pJuhe_yUVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ الإيرانية تنطلق</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/naya_foriraq/81594" target="_blank">📅 06:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81593">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/naya_foriraq/81593" target="_blank">📅 06:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81592">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/naya_foriraq/81592" target="_blank">📅 06:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81591">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/naya_foriraq/81591" target="_blank">📅 06:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81590">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/81590" target="_blank">📅 06:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81589">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c1bdc161.mp4?token=mg4CAY8zIvpFQ4S3hB_2sMD3mJc8UDQInH9yWCqp_GNCce6FFv7m2DXRT8BXojXaqkW1ZnQYIemIsSMSPrmK2lpMAS5UtoyJ3AGotZ4knMFwBAr1W88qWUilrD0bZx5-9NLDDyhgnihO2TJSpVLOZQXSkNPMxWMbUL-F2gmbB0VVVvV97IHmuRltY1bQUf1C0v4C7Xl-f_JO7OUs2DNLFRUlsoNM5mO9h249JqbnYZtQGSnbBlMYtsJFYEUk_p1Vp4MVdsDdLhsmttU8HidI0TIgOI0gfJ3ubOCuhK_ABaK6ds91rmrAZXoztR8O7ZzTy8kDCqAIawNJ8q2Wus4B6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c1bdc161.mp4?token=mg4CAY8zIvpFQ4S3hB_2sMD3mJc8UDQInH9yWCqp_GNCce6FFv7m2DXRT8BXojXaqkW1ZnQYIemIsSMSPrmK2lpMAS5UtoyJ3AGotZ4knMFwBAr1W88qWUilrD0bZx5-9NLDDyhgnihO2TJSpVLOZQXSkNPMxWMbUL-F2gmbB0VVVvV97IHmuRltY1bQUf1C0v4C7Xl-f_JO7OUs2DNLFRUlsoNM5mO9h249JqbnYZtQGSnbBlMYtsJFYEUk_p1Vp4MVdsDdLhsmttU8HidI0TIgOI0gfJ3ubOCuhK_ABaK6ds91rmrAZXoztR8O7ZzTy8kDCqAIawNJ8q2Wus4B6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يوم القيامة.. النجف تخرج بتجمع بشري هو الأكبر بالتاريخ</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/81589" target="_blank">📅 06:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d95cbb7e.mp4?token=ixZds6TfeV8QM9lhryrZFWe0INQTfHbU9g3bCnSoD0NfrhAQWAQyVDdslJ72ET-_t2G5yIx12Ne4FO9Fl78k9hulZ4RVD3gnqDg35KLMkHDRqT8qKFufzKQGlAQD51X9GLAAfJN_sFjrZ4ewf5rfm0TYaOAN1l0WSBcjieIUh7gu26yJQcBejU_rq-5wkM36IKLqBNvyfFLED9KQsLX2I_Z2TegYUZaVqn48xCaeGWtI_P1FUkcn-2g6ohFc4HrTd9PVdPpsK6vWhzVbozf6F3L1WujVO7Wqfa_J2BRNykRAeoPcdxkvEl-9lZ-F1rt9w8nfXEPbigFSNp2ZNAL65g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d95cbb7e.mp4?token=ixZds6TfeV8QM9lhryrZFWe0INQTfHbU9g3bCnSoD0NfrhAQWAQyVDdslJ72ET-_t2G5yIx12Ne4FO9Fl78k9hulZ4RVD3gnqDg35KLMkHDRqT8qKFufzKQGlAQD51X9GLAAfJN_sFjrZ4ewf5rfm0TYaOAN1l0WSBcjieIUh7gu26yJQcBejU_rq-5wkM36IKLqBNvyfFLED9KQsLX2I_Z2TegYUZaVqn48xCaeGWtI_P1FUkcn-2g6ohFc4HrTd9PVdPpsK6vWhzVbozf6F3L1WujVO7Wqfa_J2BRNykRAeoPcdxkvEl-9lZ-F1rt9w8nfXEPbigFSNp2ZNAL65g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الملايين من المشيعين يتجوهون الان على مجسر الكوفة بالنجف الأشرف</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/naya_foriraq/81587" target="_blank">📅 06:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81585">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الملايين من المشيعين يتجوهون الان على مجسر الكوفة بالنجف الأشرف</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/naya_foriraq/81585" target="_blank">📅 06:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81584">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMeaBdrkLIb57wUz29XqaKeFy12UwMAraQraHPnxcfQkhnjxVAxIet-kH_8tiDy2299SXKNyOF7u_vgEC6FVqbVWSWdR4P83YlRqEmWenvmL3O7hSigHd4LDgYi9dsmCn8vGZ4T-QSOfJpaj6op6RjX7NGVGniCLGR2fq1YvHM0cIWUiT3Gl0ATrRsYe59Vcz5fC8sWyAL3fYSziW7jkeqxU8bX6ViqGlRHwpYkRNe71mcth-5OcLZF6Bir2Ko8dwCJIOV5utRfZA8D4V0OakxWMUkPNdo3hocQzSfm3NtWnOYIkftG_ZXXXEt-b_NWRtvL9gnNVlxnmBSVhYS_CvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار الزحف المليوني نحو مجسرات ثورة العشرين</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/naya_foriraq/81584" target="_blank">📅 06:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81583">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1065c221ce.mp4?token=AaIzwSn3ENAF2Yu6VyEy9Bq9imbV0TNNmb1uk-zuEE_p02Rvh5lJIF81S7sA8vQNeTnOv8FX09ptu0PXLvdQF5fuSQTfiDAGLO9Oq1iohyb4ZY1a1mn9-B64pGG0awKcR97LNjqd9kFB1XwWArqtjZ0bfINQeyyG64TGLFRTUpfSHMLYGhTJxi0Aj8fc2JOdc8EXbVx06KzNsmS7bLALB27qRQ1W0ZJtS81XQ4libfdhqi42cHFSBArWGc-TPlZSdqE-j4al3qeqMWnv3Uc6ybs5BoMFZ60rugQ88c0t7IclPHeS0sC-mYW5GCtXG9mi4aoBhuq7cQ7IoFYtEUbdSDQKkyf4mz0yrGvj1l1oWK_F4P-xYqVgnDvViRdWRwWznvAlJwSZFLTFoAIRJUyEiAJLIc1G_Jd0r7uzi8J-Szy2WFHWB3jI4kdDTkV34dNKiEEXudHtbhuQ8oFte5zeRZFUxGGYThU9QmZsmn22RCuNvjtfD9Fx1sTmEdu94DfAi4OsSqtPre7Lc9aZZqTAgBD7n0Wc0e-kYsdzelhMATK2kSRUEj_LnHT-VMUFX4DBip7FCzVf538v2bQnpQp59Gs9iSZUCw3U9TJFSgxNFiecpHjwbjbAoCacuQpxdImdwqoLyR3u3xvsmOj6hJCJXoWAOmU_xOdXQ12-GDIhb0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1065c221ce.mp4?token=AaIzwSn3ENAF2Yu6VyEy9Bq9imbV0TNNmb1uk-zuEE_p02Rvh5lJIF81S7sA8vQNeTnOv8FX09ptu0PXLvdQF5fuSQTfiDAGLO9Oq1iohyb4ZY1a1mn9-B64pGG0awKcR97LNjqd9kFB1XwWArqtjZ0bfINQeyyG64TGLFRTUpfSHMLYGhTJxi0Aj8fc2JOdc8EXbVx06KzNsmS7bLALB27qRQ1W0ZJtS81XQ4libfdhqi42cHFSBArWGc-TPlZSdqE-j4al3qeqMWnv3Uc6ybs5BoMFZ60rugQ88c0t7IclPHeS0sC-mYW5GCtXG9mi4aoBhuq7cQ7IoFYtEUbdSDQKkyf4mz0yrGvj1l1oWK_F4P-xYqVgnDvViRdWRwWznvAlJwSZFLTFoAIRJUyEiAJLIc1G_Jd0r7uzi8J-Szy2WFHWB3jI4kdDTkV34dNKiEEXudHtbhuQ8oFte5zeRZFUxGGYThU9QmZsmn22RCuNvjtfD9Fx1sTmEdu94DfAi4OsSqtPre7Lc9aZZqTAgBD7n0Wc0e-kYsdzelhMATK2kSRUEj_LnHT-VMUFX4DBip7FCzVf538v2bQnpQp59Gs9iSZUCw3U9TJFSgxNFiecpHjwbjbAoCacuQpxdImdwqoLyR3u3xvsmOj6hJCJXoWAOmU_xOdXQ12-GDIhb0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات الامن الأمريكية تطلق النار تجاه مواطنين مكسيكيين في مدينة هيوستن وتقتل وتصيب عدد منهم.</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/naya_foriraq/81583" target="_blank">📅 06:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81578">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2f0869ac3.mp4?token=ra-Op44BYYw0bBmL4CeZMPlbyH0zQu3l-Ncfi_1cpl9ELzrT4d-7z-iVZRf9oy4nD_3pBvJAxgLj9i-1BGlllAXdv3gmOC-YFdz_tPCl_vWfTrzLew8XTMusMx3QRP_mjPwsE_iIG74KyRZ6cNTkfK-RNk1jYoPY-5iLkK_0UyrGiO8tr720I7ajWlKkViIz7PpU3UB1GVeFd-yl5X1MNZgsVkFKQWjfvkykCghnQ0QVQUHf6hpXPI5mGWAtyPRdvnMXlOckzWu3576iOEgatvSG_5cCC697bQ-R9zwkx-QeufINc9esGafFfeITB_5pMwo-j5ZiQHzKyvLDAsPDbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2f0869ac3.mp4?token=ra-Op44BYYw0bBmL4CeZMPlbyH0zQu3l-Ncfi_1cpl9ELzrT4d-7z-iVZRf9oy4nD_3pBvJAxgLj9i-1BGlllAXdv3gmOC-YFdz_tPCl_vWfTrzLew8XTMusMx3QRP_mjPwsE_iIG74KyRZ6cNTkfK-RNk1jYoPY-5iLkK_0UyrGiO8tr720I7ajWlKkViIz7PpU3UB1GVeFd-yl5X1MNZgsVkFKQWjfvkykCghnQ0QVQUHf6hpXPI5mGWAtyPRdvnMXlOckzWu3576iOEgatvSG_5cCC697bQ-R9zwkx-QeufINc9esGafFfeITB_5pMwo-j5ZiQHzKyvLDAsPDbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران إرضاع جوي أمريكي يحلق في سماء مدينة الرمادي بمحافظة الأنبار غربي العراق.</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/naya_foriraq/81578" target="_blank">📅 06:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81576">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ea001678.mp4?token=nBXIuVhQLC0akBPbRR4KHLUKqlQCMVQ_yBa_0kb_KwGEG7PXbDjUsf-MGaHfH2T0kCcZfbirlyk9sz8OFSx2pdRgu0CiH2e2uthzIG1xPdnuhO-xfZURU1Fkt-Fb4CxcC9zybEVaP-rYSFF1b7jgiV4aWAOQGiXHrsBTH3yLR61CQUUIkAOiZmzqgxv64wqurciZycluMBqq5S_eCHa93gNSDQtc4sOusxK5EIfqn7seXme8fHVVRWMWXSjkpv67Nin-T__mBZeTeaX4ZjVg2VJmBwjcbQk7OUFRTGa9WdxzmAN_j78wzvHxWnLGPOnqAQC-cEL4mVzBglSRpAcNFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ea001678.mp4?token=nBXIuVhQLC0akBPbRR4KHLUKqlQCMVQ_yBa_0kb_KwGEG7PXbDjUsf-MGaHfH2T0kCcZfbirlyk9sz8OFSx2pdRgu0CiH2e2uthzIG1xPdnuhO-xfZURU1Fkt-Fb4CxcC9zybEVaP-rYSFF1b7jgiV4aWAOQGiXHrsBTH3yLR61CQUUIkAOiZmzqgxv64wqurciZycluMBqq5S_eCHa93gNSDQtc4sOusxK5EIfqn7seXme8fHVVRWMWXSjkpv67Nin-T__mBZeTeaX4ZjVg2VJmBwjcbQk7OUFRTGa9WdxzmAN_j78wzvHxWnLGPOnqAQC-cEL4mVzBglSRpAcNFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجهيز العجلة التي ستحمل الجثامين الطاهرة في النجف الأشرف</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/naya_foriraq/81576" target="_blank">📅 06:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81575">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42531eddcc.mp4?token=v5smEHiMuDLeCtnclc9E3Mp1vTp6Boy3VVKBGr7-J117pg-saZTMhqc5FMq1q5ZH0sc6tE8JebbWvwvRSK7z4Rj_ILni0h95yIsEvyOXOQSaw0NeSC-OH4WQg8ilwXLGGCBR2FKhRz7BrMOcdQVyJPtEx0CXGioQGTsXwrqcMiW9peZBz_C1cGN3509KYUJat6AruKXHpHVYBq3FccXkjzc7SToA3APaCrdED8qWZG72LFA0p4ubH_2Cn9VcfgmfnNLo-D3YJca30gUc-9bIREH0oAGqcmICISkbqXrFJdlz8OKkAvYdXag_SxNO0qpbHJ_X31pzOWKnimJNL5w-DD7QxEtbsbP_SPdwySmfStIfx-7nZMKVvRXUhB5UycZbeOOd5_Cl8t5GYMpUpefkHX8TNANZ54xLMa1nYSsKTn7xgfzY_TEgyKfbMQgrBdNDxVLGS-rHgH-5O4hJQVNtD4eG9kI1MZiPEB5yZvijxCs95lBxaQTUaIg4q6B_RQeBTy7gf_agoxYkfOEHiQtqMR8dOZ-yJIOxvgmrhZqwFIjeYT7N1jxqo7kBB-hZjwIXF1p6dzan_TVKWfEtFAhsf_F_4CmyIWNSqH5oqnQJpU0Jz2Tua9JbHDiZ_4vm7MDt_8KEUmNCjbyazemxNoJdn8E2Eggh7uqq2NlEMdDfnIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42531eddcc.mp4?token=v5smEHiMuDLeCtnclc9E3Mp1vTp6Boy3VVKBGr7-J117pg-saZTMhqc5FMq1q5ZH0sc6tE8JebbWvwvRSK7z4Rj_ILni0h95yIsEvyOXOQSaw0NeSC-OH4WQg8ilwXLGGCBR2FKhRz7BrMOcdQVyJPtEx0CXGioQGTsXwrqcMiW9peZBz_C1cGN3509KYUJat6AruKXHpHVYBq3FccXkjzc7SToA3APaCrdED8qWZG72LFA0p4ubH_2Cn9VcfgmfnNLo-D3YJca30gUc-9bIREH0oAGqcmICISkbqXrFJdlz8OKkAvYdXag_SxNO0qpbHJ_X31pzOWKnimJNL5w-DD7QxEtbsbP_SPdwySmfStIfx-7nZMKVvRXUhB5UycZbeOOd5_Cl8t5GYMpUpefkHX8TNANZ54xLMa1nYSsKTn7xgfzY_TEgyKfbMQgrBdNDxVLGS-rHgH-5O4hJQVNtD4eG9kI1MZiPEB5yZvijxCs95lBxaQTUaIg4q6B_RQeBTy7gf_agoxYkfOEHiQtqMR8dOZ-yJIOxvgmrhZqwFIjeYT7N1jxqo7kBB-hZjwIXF1p6dzan_TVKWfEtFAhsf_F_4CmyIWNSqH5oqnQJpU0Jz2Tua9JbHDiZ_4vm7MDt_8KEUmNCjbyazemxNoJdn8E2Eggh7uqq2NlEMdDfnIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنويه  ينطلق التشييع المبارك الساعة ٦ صباحا</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/naya_foriraq/81575" target="_blank">📅 06:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات تهز المنامة</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/81573" target="_blank">📅 05:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81572">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات تهز المنامة</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/naya_foriraq/81572" target="_blank">📅 05:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmaznffBGtrTHdxg8UMSC-vHymfXER9HE25DY7qa6QIHPVVOyTTTn32BEZP7G6EesJv7RCz8Tm0XY6nGPNv__r9QVTD1l5Drd_7qIlJv4SOO2yxtk2bdo3SJn27qJh8rs3iACyU73lzQ_DAFGHfNTwfr1IxV_3so6Z071Brnh41_XzT2M43eI5cpPjuORIWMkkqXqk5vvluKTkt01ATQIT1ctEuQM_VIzZH4XUgj_DqiFDqP_qe80feW0vDQg1t3KZRuHEReuYntd7u5jn-_wVuiRY0-Y0HFePQKF4syYdj0rN_i5e2hIZaoXrN8y6VuCqBTZ1ncLvlAZuwIK8j3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنويه
ينطلق التشييع المبارك الساعة ٦ صباحا</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/naya_foriraq/81571" target="_blank">📅 05:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81570">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxlUZhqwWGZKhhoztTj1WeWjad9w-e_fyf9zmDBfZgKBWqDH-MumqrOeMQRUmzSsXvWeuR5cTYjIbVLg06Qcp5KcBofsh05wXGThDV1s1eUQQYXv4LEXZ-VpQzt5dPTm81O8bTv7IcknH4VNBREtqA-a1Scskuu2YkCpszD2z3ROBzNbtDk2Q4pXY6elIU7I95bPKCGC-S4Z9-_M3W1XDi2JvTAZnAYRNXC1jqUJ_LjzbkQ0jH92RNQBytIid_ZWIJU8yAOIHsF1ESVAVaNGNgitybK5qukCFX0ZGu97ls8naJN0ynKvg-CgQzHpxX3iNDASu40Sc8SgyqKkJrcjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف:
انتهاكات رئيسية لمذكرة التفاهم من جانب الولايات المتحدة:
انتهاك التعديلات الإيرانية في المضيق
تهديدات مستمرة بشن المزيد من الضربات
إعادة فرض عقوبات النفط
هجمات على جنوب إيران
استمرار العدوان الصهيوني على
لقد انتهى عهد الترهيب والابتزاز. إنه لا يؤدي إلى أي مكان. لن نستسلم.</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/naya_foriraq/81570" target="_blank">📅 05:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81569">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c103b91b94.mp4?token=JssjB-OYBIctW75q9UU6GOlRbZPN3z5hKszC_UvxbAKhBH2QCKWrBKkUmLrmJ9qomu2BiFiqgZum49YAxoUB5TjiW9yryyFoPdUyW7gIAegBixfeRT4dotV7knkLNY-T7Z_74uvEC8rWXMJjoz85shUig2cB04Fkn3AXMiPWuEW6FlO2vbcidrZjudGlq5pItZpa4EQ1-hthOXEEO3quo2EP4gvnQ2tYPAYvkoDQ5j51KZYbgghTwJb9imlwqFCqZU6rEUTs0KBZ99PDg4yWVvpOniHD6DOf1rmrUmoPLOxASRmpRRQCCnOMa_DrK_-T0Yv7OSn29xQHigDFHcKNSKsE-e6G4gqOYNIiM4o9pSllEHC5fWx-_8J9CbjBKcfogBsSFnqb37s-hMNtww8p_akroFDVtoRhKPoG8vHEEt0spCUs4aPPn0PX0XWhUjPmUK70scOH1q0-ierfJv8jmtjSh1qjg-D2_8O7prm9kcicFmZFdjmHC0L4NE3vqmgqKu9P3p_dcj28uFp1_46_DeAKApPYYevheJk8MRE-Uy-QBFhZY6D7o8Y3cGxXYaILuflCdha-ODWej_-Ecd80X1gz8VhuyYNi2NHTrrr71EUSD9TJfcvMVT83e2pn8QzzLWN8laRaaPqe4BLIC43PwdZvc4_1EdT54wxvtKYhyds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c103b91b94.mp4?token=JssjB-OYBIctW75q9UU6GOlRbZPN3z5hKszC_UvxbAKhBH2QCKWrBKkUmLrmJ9qomu2BiFiqgZum49YAxoUB5TjiW9yryyFoPdUyW7gIAegBixfeRT4dotV7knkLNY-T7Z_74uvEC8rWXMJjoz85shUig2cB04Fkn3AXMiPWuEW6FlO2vbcidrZjudGlq5pItZpa4EQ1-hthOXEEO3quo2EP4gvnQ2tYPAYvkoDQ5j51KZYbgghTwJb9imlwqFCqZU6rEUTs0KBZ99PDg4yWVvpOniHD6DOf1rmrUmoPLOxASRmpRRQCCnOMa_DrK_-T0Yv7OSn29xQHigDFHcKNSKsE-e6G4gqOYNIiM4o9pSllEHC5fWx-_8J9CbjBKcfogBsSFnqb37s-hMNtww8p_akroFDVtoRhKPoG8vHEEt0spCUs4aPPn0PX0XWhUjPmUK70scOH1q0-ierfJv8jmtjSh1qjg-D2_8O7prm9kcicFmZFdjmHC0L4NE3vqmgqKu9P3p_dcj28uFp1_46_DeAKApPYYevheJk8MRE-Uy-QBFhZY6D7o8Y3cGxXYaILuflCdha-ODWej_-Ecd80X1gz8VhuyYNi2NHTrrr71EUSD9TJfcvMVT83e2pn8QzzLWN8laRaaPqe4BLIC43PwdZvc4_1EdT54wxvtKYhyds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الملايين من أبناء العراق يتجمهرون عند نقطة إنطلاق تشييع إمام الأمة الشهيد في محافظة النجف الأشرف.</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/naya_foriraq/81569" target="_blank">📅 05:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81568">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مشاهد من مليونية تشييع الإمام الشهيد في النجف الأشرف</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/naya_foriraq/81568" target="_blank">📅 05:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81567">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27818687f1.mp4?token=ezJaAv0avUnDLQvgq5k_5BUPPSM8KSvSVE3EsS36S-t4J5QUQoM0CxJLK-lOZWRpUHfg9feRavqib_PXQX4i_5HKyhA7Yd1U8WHOFYPYY6LaYs-E6Evp3eBZyi7MR7UWt7eQYHveZcfPZLYKfVPxj1MPd8KoknQbz1HBR3UJnobeWoHPaA0yRwQcuvQ8sWPyKRS10dh-g1HyITtZJozRW86Yjtln3W3e6piKIp5N0F6sd-gZtBxaOhIpGYscikLvRa0NBHTS_zSO-dvIEZM4IZNJ6LgRha0cfoT_BZzzfx1EXm8Nirb-g7nTaFGoPcyRhkNFwwD3_0_ruaN1d3PD6D_XIgH6iur3nNIBvpFTLC8yPlWydT_O0Yu4kZ8YPfIjSF7uxyjDrTzVV2mJ9i6JEubR7DxleckoT5BHSN8oBbgjGLqmlX2dic_rV7dq6E602XUvAq_YQNoO3kzP2MBvB9oFHgG2cfWPO7dSOIVpXasLy-GSzLpn8mlOzfBKBWS8iCeFi8ZU5qxZVJPJBZP-Gsq_lUpTMN_VGScTLsMzOi7VUbWIrAdKrr1bZCCAy9rvDFxKY_3BC7rd6zYsKPZey6mpz4xeHa00SaGmKDEx78b5OmowWq7lJh5uNeYJ517opXrup5v0CeeyUxRTeW7HDJfiU7MrBFZF5k65wclbikE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27818687f1.mp4?token=ezJaAv0avUnDLQvgq5k_5BUPPSM8KSvSVE3EsS36S-t4J5QUQoM0CxJLK-lOZWRpUHfg9feRavqib_PXQX4i_5HKyhA7Yd1U8WHOFYPYY6LaYs-E6Evp3eBZyi7MR7UWt7eQYHveZcfPZLYKfVPxj1MPd8KoknQbz1HBR3UJnobeWoHPaA0yRwQcuvQ8sWPyKRS10dh-g1HyITtZJozRW86Yjtln3W3e6piKIp5N0F6sd-gZtBxaOhIpGYscikLvRa0NBHTS_zSO-dvIEZM4IZNJ6LgRha0cfoT_BZzzfx1EXm8Nirb-g7nTaFGoPcyRhkNFwwD3_0_ruaN1d3PD6D_XIgH6iur3nNIBvpFTLC8yPlWydT_O0Yu4kZ8YPfIjSF7uxyjDrTzVV2mJ9i6JEubR7DxleckoT5BHSN8oBbgjGLqmlX2dic_rV7dq6E602XUvAq_YQNoO3kzP2MBvB9oFHgG2cfWPO7dSOIVpXasLy-GSzLpn8mlOzfBKBWS8iCeFi8ZU5qxZVJPJBZP-Gsq_lUpTMN_VGScTLsMzOi7VUbWIrAdKrr1bZCCAy9rvDFxKY_3BC7rd6zYsKPZey6mpz4xeHa00SaGmKDEx78b5OmowWq7lJh5uNeYJ517opXrup5v0CeeyUxRTeW7HDJfiU7MrBFZF5k65wclbikE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الملايين من المشيعين يواصلون التوجه نحو نقطة إنطلاق التشييع في النجف الأشرف</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/naya_foriraq/81567" target="_blank">📅 05:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2739a5f4.mp4?token=ZAiQFeS-ixT4cBn50y80XwIZO2Tsiuv5KRoDzuFJKdcQLUEuaRyi_--crf0Py92fPhc5GQIXJLhiylx2q4CKXw1ucYGGJZBUESjTDnGrk7kkY5RPqf7iqhxLQdo3WlfYBKjwbbzd1ONPxI02V21Uvzx3OrRT9SpbzeM8mI3Zt3TqnB_vgToT44fG6xerevXnQ4IF30HEdD7d-2iKW0JQxjvuVfiJbTtB8RDb3zI5kpKgY8-5K-BxxXGlkJKtcpa4pdODeSkbzvYzll6IhrlH-v3M7hzsvlIx1GERpD7zMq5mu_1AA7RluGEZ6RM07RFVb7cG-TVTPKuplZ-YpIDBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2739a5f4.mp4?token=ZAiQFeS-ixT4cBn50y80XwIZO2Tsiuv5KRoDzuFJKdcQLUEuaRyi_--crf0Py92fPhc5GQIXJLhiylx2q4CKXw1ucYGGJZBUESjTDnGrk7kkY5RPqf7iqhxLQdo3WlfYBKjwbbzd1ONPxI02V21Uvzx3OrRT9SpbzeM8mI3Zt3TqnB_vgToT44fG6xerevXnQ4IF30HEdD7d-2iKW0JQxjvuVfiJbTtB8RDb3zI5kpKgY8-5K-BxxXGlkJKtcpa4pdODeSkbzvYzll6IhrlH-v3M7hzsvlIx1GERpD7zMq5mu_1AA7RluGEZ6RM07RFVb7cG-TVTPKuplZ-YpIDBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الملايين تتجمع الان قرب نقطة الشروع لتشيع الجثمان الطاهر بمحافظة النجف الأشرف</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/naya_foriraq/81566" target="_blank">📅 05:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDNaRUnvURVD7Y6jUYqJLIYSHem4gZ-TZV-Aj-Bb_23_v7HfXgL_YamkuKdNKadzs6ozEqpHVmAkwxefqM0lg91NcCwWBXnHOXL6i2iDLsgGa4StFVIj7z0CnzRIEboO34mfp7ZLVqgqKE_TT_RRQSoZm9cchIEyGc0Wiuf3ysBzUWGeDXrG3qQbaHdC0qFGW_xn6zC_vwKVqJT6u5iy352COGlDkG_GZKW16PXgjFKiMwJyRxEpSXWW7iCmNKURt6emPbEXig11rQdwi8lO8QEnHBOoCYipCZsadD8H7LUXJ94kKVFz4s_1N2yLPVk-yo21ha_MXaQDcRs0vk35ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد محافظ النجف يشرف على بدء التشييع بالقرب من جسر مستشفى الصدر</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/naya_foriraq/81565" target="_blank">📅 05:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90153b99f.mp4?token=a3Vk8vXXwM7jZASQZIXfzC0Gr8Rei3_ix83-cfztKx2-pMEPZ_zxTeLEhahnonRlIwfEx_9GrWDAD0ly_FI7wDfL7UAdcOY1EWezDLYtFjnQBt59QeZi0Fz1Fkr4qJkm7CSXb1r2CCk5Fi1C6o78Ewf6ze-WYtdzeN1495DREJXrOnYVstQ--wPn7Oj4TVVRkDOi9roxnoM2YbnYGM5gwhUTGXNVtD78kZh3cdM9yuav49_vii8_wV7ufpzepqWTCdR2d-I75fdmh2uIcMV-OkPGq79nbGA2eflUHI0Z9DiTf8uxnOTK78UlhsCSvhFWnV-L1hGjsMTDk9iP_NXwOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90153b99f.mp4?token=a3Vk8vXXwM7jZASQZIXfzC0Gr8Rei3_ix83-cfztKx2-pMEPZ_zxTeLEhahnonRlIwfEx_9GrWDAD0ly_FI7wDfL7UAdcOY1EWezDLYtFjnQBt59QeZi0Fz1Fkr4qJkm7CSXb1r2CCk5Fi1C6o78Ewf6ze-WYtdzeN1495DREJXrOnYVstQ--wPn7Oj4TVVRkDOi9roxnoM2YbnYGM5gwhUTGXNVtD78kZh3cdM9yuav49_vii8_wV7ufpzepqWTCdR2d-I75fdmh2uIcMV-OkPGq79nbGA2eflUHI0Z9DiTf8uxnOTK78UlhsCSvhFWnV-L1hGjsMTDk9iP_NXwOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع الجماهير المشيعة للجثمان الطاهر في نقطة انطلاق  بالنجف الاشرف</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/naya_foriraq/81564" target="_blank">📅 05:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3067466f9.mp4?token=kutwdE-_xLoY1fCY48--5ch9Mjfl8NNa6T6d4aaODFdwO3P3AxW6YsuCvxrUXx-FvL1kYcPmV_4iATtN8vYNijLYRslWJrRTkcHRjN3A1y4caFbeLrMeQDfW7UA1BvonT1JA5YhWDzHLp0CMrVNXDwT4scvoH9P1YYIgNnKkjYLOtz0_zgHgmlRkb52Wf_1xt_NzMkA1g0gv4NCz9HV22wbhl70UvK8C4QC6klc-J5tOR1uWSOR14RV0CV-1jxo83fSJM7KnF-axOhy4YOaKpqBZBvoBuoO4e14QQ30uAGtwwDcH5Xzf1nMLfGf30J7CztdGWPQyL6mbxOTo5_mYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3067466f9.mp4?token=kutwdE-_xLoY1fCY48--5ch9Mjfl8NNa6T6d4aaODFdwO3P3AxW6YsuCvxrUXx-FvL1kYcPmV_4iATtN8vYNijLYRslWJrRTkcHRjN3A1y4caFbeLrMeQDfW7UA1BvonT1JA5YhWDzHLp0CMrVNXDwT4scvoH9P1YYIgNnKkjYLOtz0_zgHgmlRkb52Wf_1xt_NzMkA1g0gv4NCz9HV22wbhl70UvK8C4QC6klc-J5tOR1uWSOR14RV0CV-1jxo83fSJM7KnF-axOhy4YOaKpqBZBvoBuoO4e14QQ30uAGtwwDcH5Xzf1nMLfGf30J7CztdGWPQyL6mbxOTo5_mYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع الجماهير المشيعة للجثمان الطاهر في نقطة انطلاق  بالنجف الاشرف</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/81563" target="_blank">📅 05:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c28e8f14d.mp4?token=EfcMqCq4f-VOVJR_H9EBpQnUCVmVBo9Ysc6eVL9MZwbOkP6u13kGSV5YF2oKFzBwls1KwWWaMCwnvCcwfNMszrNa5y-ND-3Qth4mHNHh8hBBd1n1uHpJQL2bFlJTnPILRQmd4RIaqaUfuAhcD0SriHFyl0ZNqEVrgFMnPkAkiC_ogupd-LpnI_tLnSndeAdxXMdOuPYbFtWoNndzX_kkXu6Jbf0GTe3xNC-mD4v0SnadeLLZ6-qAoHajq2IbHv9W9kOTva_EbgVQsaOK9z8IDxXPh-4PUBIrqM8CuboflhspAiYVHiyeX3h8pREqOxEFoNYHGtD2kUCjgL_bNSGbTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c28e8f14d.mp4?token=EfcMqCq4f-VOVJR_H9EBpQnUCVmVBo9Ysc6eVL9MZwbOkP6u13kGSV5YF2oKFzBwls1KwWWaMCwnvCcwfNMszrNa5y-ND-3Qth4mHNHh8hBBd1n1uHpJQL2bFlJTnPILRQmd4RIaqaUfuAhcD0SriHFyl0ZNqEVrgFMnPkAkiC_ogupd-LpnI_tLnSndeAdxXMdOuPYbFtWoNndzX_kkXu6Jbf0GTe3xNC-mD4v0SnadeLLZ6-qAoHajq2IbHv9W9kOTva_EbgVQsaOK9z8IDxXPh-4PUBIrqM8CuboflhspAiYVHiyeX3h8pREqOxEFoNYHGtD2kUCjgL_bNSGbTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
ما تسمى القيادة المركزية الاميركية تنشر مشاهد لاستهداف مناطق وسفن تجارية مدنية في جمهورية ايران الاسلامية.</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/81562" target="_blank">📅 05:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تنويه هام
🇮🇶
🇮🇷
هيئة الحشد الشعبي:
تؤكد اللجنة المنظمة لمراسم التشييع أن التشييع الشعبي في محافظة النجف الأشرف سيبدأ عند الساعة السادسة صباحاً، انطلاقاً من مجسّر مستشفى الصدر باتجاه ساحة الصدرين.
وعليه، فإن ما يُتداول حالياً عبر مواقع التواصل الاجتماعي بشأن انتهاء مراسم التشييع أو اختتامها لا أساس له من الصحة، إذ إن التشييع لم يبدأ بعد، وسيُقام وفق التوقيت والمسار المعلنين.
وندعو جميع المواطنين ووسائل الإعلام إلى اعتماد المعلومات الصادرة عن الجهات الرسمية، وعدم تداول الأخبار غير الموثقة .</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/naya_foriraq/81561" target="_blank">📅 05:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/510cefa993.mp4?token=h5EotdR3gEm6uAvZ1SnU49Yturv-FAGr3QpFixUZ9mzWgB3jGPLRjCSthfmmr9q5tXiNHyH88yp0PGXb0I2iPMH7bjEVlkbF_TyyRFFO2l1GdnqP0Fya7Y6IaJmk9B7kC7fneFLsTunq_hJ0vxXp6ndTvYSgHUNsGxLPMTCWXNFt6c3kUA8RNdd7vNc3pZ879k83CBtl3ljp4YTfJDi5K3kbn61Lm2Dz8ZWqWTkOz8uLmvsBPRxUqA75NUKwZVJ-Yo1Uo93JzJ23TzwN3FD5vX15wKjKwQL_-L7RRUZwW9O6_oE--95Y3ioPcrDxjz8XzT8qcIHD7SxlvmbKHKIhNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/510cefa993.mp4?token=h5EotdR3gEm6uAvZ1SnU49Yturv-FAGr3QpFixUZ9mzWgB3jGPLRjCSthfmmr9q5tXiNHyH88yp0PGXb0I2iPMH7bjEVlkbF_TyyRFFO2l1GdnqP0Fya7Y6IaJmk9B7kC7fneFLsTunq_hJ0vxXp6ndTvYSgHUNsGxLPMTCWXNFt6c3kUA8RNdd7vNc3pZ879k83CBtl3ljp4YTfJDi5K3kbn61Lm2Dz8ZWqWTkOz8uLmvsBPRxUqA75NUKwZVJ-Yo1Uo93JzJ23TzwN3FD5vX15wKjKwQL_-L7RRUZwW9O6_oE--95Y3ioPcrDxjz8XzT8qcIHD7SxlvmbKHKIhNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
من بين الحرمين الشريفين في محافظة كربلاء المقدسة حشود مليونية تنتضر قدوم نعش السيد القائد.</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/naya_foriraq/81560" target="_blank">📅 05:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81559">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9162ec4eb.mp4?token=gssbhwWzXnseoDlqZ0lwhNxAFo0ECvTVzMTxUr9gvNvaTCA4Yp2DteH92yDM3k_qRIVr0UYdWyNGlFjLw_I6XekV76omwILXCuy4GrH2toIzAEf_mMKrlrBVz7E0t-4Yb-2VNNJ286rtz4BTvOVXr3UWeF3E7CQqdw8zt9CLwwHgI_hkXHimhbrdKHKJ4ZIZd7Rjr3kX5L3Ld1eU8jFQR_AqVnRShcPIkPgMrfpHjKyhzR85vV9d-GVYcZNAzUJXYbXqe5Mgfp0Q6WN7kU8M4s5ptMXjyUUovqXP0X8pXJ0zxCRfYdjRmTMoLCwhwvdIEjo-e-ni7WUsL8wP-t6HEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9162ec4eb.mp4?token=gssbhwWzXnseoDlqZ0lwhNxAFo0ECvTVzMTxUr9gvNvaTCA4Yp2DteH92yDM3k_qRIVr0UYdWyNGlFjLw_I6XekV76omwILXCuy4GrH2toIzAEf_mMKrlrBVz7E0t-4Yb-2VNNJ286rtz4BTvOVXr3UWeF3E7CQqdw8zt9CLwwHgI_hkXHimhbrdKHKJ4ZIZd7Rjr3kX5L3Ld1eU8jFQR_AqVnRShcPIkPgMrfpHjKyhzR85vV9d-GVYcZNAzUJXYbXqe5Mgfp0Q6WN7kU8M4s5ptMXjyUUovqXP0X8pXJ0zxCRfYdjRmTMoLCwhwvdIEjo-e-ni7WUsL8wP-t6HEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
الحشود المليونية تنتضر اكمال زيارة النعوش الطاهرة لحرم جدهم الامام علي (ع).</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/naya_foriraq/81559" target="_blank">📅 05:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81558">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f35c31313b.mp4?token=bMt7sXBictZPawcosfORnTG9nIq3GLuPC9KVwkjUaRld69vE25k-9tJG-zTNJ_-4QkXe-9vHW1MvmZQOBluR7BG2r6gvt52f3fXQu4A_bQdJRf2Z-4jSC-BLnn1lNSvnZCIPnhskuelcDylCvvls01y8XjH7HExqfolLdTehviGN0T7VB16jPsSxTiToxPT22RCfUank8zbgvNN7mmh1jqC1OpVACWXmDNDxIPAlXnYMusacCewUleBReZXfn84txkeGmY3iQcGBLn-rvL6HDtx6ATo39Bz93Q2RYw1XRbgapPCK2lnkGUlhVwORwmtLNlkOzQRN8QM-aMFXsovlRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f35c31313b.mp4?token=bMt7sXBictZPawcosfORnTG9nIq3GLuPC9KVwkjUaRld69vE25k-9tJG-zTNJ_-4QkXe-9vHW1MvmZQOBluR7BG2r6gvt52f3fXQu4A_bQdJRf2Z-4jSC-BLnn1lNSvnZCIPnhskuelcDylCvvls01y8XjH7HExqfolLdTehviGN0T7VB16jPsSxTiToxPT22RCfUank8zbgvNN7mmh1jqC1OpVACWXmDNDxIPAlXnYMusacCewUleBReZXfn84txkeGmY3iQcGBLn-rvL6HDtx6ATo39Bz93Q2RYw1XRbgapPCK2lnkGUlhVwORwmtLNlkOzQRN8QM-aMFXsovlRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
بدأ زيارة النعوش الطاهرة لحرم الامام علي (ع).</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/naya_foriraq/81558" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81557">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7d25feb6.mp4?token=toyQrNw41w3V71FZuPYvLxzcv06UhZksnF_T4NnYqFUMIcfrHMFuA3hRgyj8xMERxzeloRovfQkYwjsqrs-ki5nP_qDFvzoWlVQ9gjHPCnJ9kV3ACI6anFMNRyBNISvR5NIrCxrAykI8agHZqHqL1T7I8LREFLoXfTHUDfHC-vWp2Iy3AACTI4POwGXplAhWSTkiUefZvVTvocyh7_2mlvvHO9RzwT2boSPAjEt2G2JYSL8AO9lavix-P1KWaSh0heSVoYfXNr0ZentibCLq1Nbebi-e5KpcDHdDyCv_1LWRmFw045ylVfJrY85Z-5u8yOPbQA0d6ZF--YuI2YrT7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7d25feb6.mp4?token=toyQrNw41w3V71FZuPYvLxzcv06UhZksnF_T4NnYqFUMIcfrHMFuA3hRgyj8xMERxzeloRovfQkYwjsqrs-ki5nP_qDFvzoWlVQ9gjHPCnJ9kV3ACI6anFMNRyBNISvR5NIrCxrAykI8agHZqHqL1T7I8LREFLoXfTHUDfHC-vWp2Iy3AACTI4POwGXplAhWSTkiUefZvVTvocyh7_2mlvvHO9RzwT2boSPAjEt2G2JYSL8AO9lavix-P1KWaSh0heSVoYfXNr0ZentibCLq1Nbebi-e5KpcDHdDyCv_1LWRmFw045ylVfJrY85Z-5u8yOPbQA0d6ZF--YuI2YrT7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
بدأ زيارة النعوش الطاهرة لحرم الامام علي (ع).</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/naya_foriraq/81557" target="_blank">📅 04:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81556">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/510de80780.mp4?token=vrM0V1aT77KR9Y4o2I8jfNajIyjt8f-zB9yhqf3511TxMSm8LzsJpKj44QiT4qt1GhXi28SWCAxW2EL6M6dkd32DZUvTAOXXNXmLH-LkjfK5DDmacBhQR1Pge716XIp7aYnCauPrZDsGqrS6K_ZNmaaUpeEGKb4QJ_dq4JwYeYD-L7wIixK_BgDxV98D1s11BuRRaISYj_UhQDlTVN5Gk2E1GN1i-aLDsFqZqoYKqveP8r4dYx_MPkYySIrL47-F0HGUEwLHriad49nHKoMpHzO6HDTxpunXVkgBxQD205_6OoSEL3ufOUm6DV0ECKUqQ03kftqxgQSiFF5HOnfHvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/510de80780.mp4?token=vrM0V1aT77KR9Y4o2I8jfNajIyjt8f-zB9yhqf3511TxMSm8LzsJpKj44QiT4qt1GhXi28SWCAxW2EL6M6dkd32DZUvTAOXXNXmLH-LkjfK5DDmacBhQR1Pge716XIp7aYnCauPrZDsGqrS6K_ZNmaaUpeEGKb4QJ_dq4JwYeYD-L7wIixK_BgDxV98D1s11BuRRaISYj_UhQDlTVN5Gk2E1GN1i-aLDsFqZqoYKqveP8r4dYx_MPkYySIrL47-F0HGUEwLHriad49nHKoMpHzO6HDTxpunXVkgBxQD205_6OoSEL3ufOUm6DV0ECKUqQ03kftqxgQSiFF5HOnfHvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
أرض العراق تفتح ذراعيها لاستقبالك... والقلوب سبقت خُطا المشيعين.</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/naya_foriraq/81556" target="_blank">📅 04:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81555">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb34f17673.mp4?token=hBcjFBpIGoXw95xuIIqnHx1XzKCyBuu9tUuCqOZBf1mii4CmG863KATKXTDN6CUQ2OnurMOoudskJWGjwrvvLWNFZagonV8d8VmLYT-DPTqNRLOg3cdxkgn-Obq1z-kl-CVxLR7EGldd2hxkjfE62nAU7Zy3kvM0Br7GTFHnEhbi5gyhX4IxVKTpmprU4MZs2_AG5rWtAPG675PsDLny-0B6XbV4Gpvhm1nDPbZ0GDTFD4XhOdwsQPW67ktrtxxkiUjwWMHn8PEO3JN3WNKPUkqdBaaI4JwiolCk_qvw4buuBLlmsvDbP5XjaTrQQd22wMlCn4_1HF9dHaiVsQHdSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb34f17673.mp4?token=hBcjFBpIGoXw95xuIIqnHx1XzKCyBuu9tUuCqOZBf1mii4CmG863KATKXTDN6CUQ2OnurMOoudskJWGjwrvvLWNFZagonV8d8VmLYT-DPTqNRLOg3cdxkgn-Obq1z-kl-CVxLR7EGldd2hxkjfE62nAU7Zy3kvM0Br7GTFHnEhbi5gyhX4IxVKTpmprU4MZs2_AG5rWtAPG675PsDLny-0B6XbV4Gpvhm1nDPbZ0GDTFD4XhOdwsQPW67ktrtxxkiUjwWMHn8PEO3JN3WNKPUkqdBaaI4JwiolCk_qvw4buuBLlmsvDbP5XjaTrQQd22wMlCn4_1HF9dHaiVsQHdSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
أرض العراق تفتح ذراعيها لاستقبالك... والقلوب سبقت خُطا المشيعين.</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/naya_foriraq/81555" target="_blank">📅 04:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81554">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766b183c64.mp4?token=WZJ6iqjLM07Ly3h3g_JEnaAd8Goojf7jkF7Mcp99EPENbJh4m_qTJc6m6ugtmKz3rFDVJdEpRkIm1K72lnKZpBtM9IncoJIq9Iy0M7tenqzffr6Kb5EAOU5yUOYQ4VIWlVWK90jAvO8SPjPwf0_5z5IEGMUwixGxdxwitRVDwaz_eJTKUdNueLYyuNlYU0W34fSVHTVgIqiY_VmqTfh4iXMP3USY3dtzaFjYE4ikYkSLOED88lXwdqos-uD3rLkK1BM8SkbswGyF-AEL4BJxGwu4ShidInFvrMLOFFo7f_90a5OLHU6OxPzEqsEVN0YMkU01VTbncOVnybV5BYivhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766b183c64.mp4?token=WZJ6iqjLM07Ly3h3g_JEnaAd8Goojf7jkF7Mcp99EPENbJh4m_qTJc6m6ugtmKz3rFDVJdEpRkIm1K72lnKZpBtM9IncoJIq9Iy0M7tenqzffr6Kb5EAOU5yUOYQ4VIWlVWK90jAvO8SPjPwf0_5z5IEGMUwixGxdxwitRVDwaz_eJTKUdNueLYyuNlYU0W34fSVHTVgIqiY_VmqTfh4iXMP3USY3dtzaFjYE4ikYkSLOED88lXwdqos-uD3rLkK1BM8SkbswGyF-AEL4BJxGwu4ShidInFvrMLOFFo7f_90a5OLHU6OxPzEqsEVN0YMkU01VTbncOVnybV5BYivhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
يا سيدي حملناك على الأكتاف كما يليق بمقامك فمرحبا بك في أرض أجدادك.</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/81554" target="_blank">📅 04:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81553">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5c946de0.mp4?token=G2MTT94VzWdmLBSPhl0kMoS5argjpvJv0c_rlY0TqzkHVhIAInPCyo-uOMfRXdSLOGy-rTa5nneCQ46xwSsneyJJJs9tzOlcVmOW54CN0Z8e4WWDTCO-UHbVy8rStFb6G7bqCDqVz_fKL4epXr19iGQUSY8NJZ813y_Kk5FW0iSOPk_j-6rvY6TpmfMYXfOPiL_pu9U8_1qxWzwVBvPPbkUBeSakm5EnrsH3EqOKO3rVuiP4RIVEb_lY-0gxZFlmtYzeLClmoiHAom0ZeZb0BzrZ6oBtTavIinrU7FbA3Zh5vTmmuPYwfcy98nGSdcXzK1Z8VKPkFkI_Dq5v3la0bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5c946de0.mp4?token=G2MTT94VzWdmLBSPhl0kMoS5argjpvJv0c_rlY0TqzkHVhIAInPCyo-uOMfRXdSLOGy-rTa5nneCQ46xwSsneyJJJs9tzOlcVmOW54CN0Z8e4WWDTCO-UHbVy8rStFb6G7bqCDqVz_fKL4epXr19iGQUSY8NJZ813y_Kk5FW0iSOPk_j-6rvY6TpmfMYXfOPiL_pu9U8_1qxWzwVBvPPbkUBeSakm5EnrsH3EqOKO3rVuiP4RIVEb_lY-0gxZFlmtYzeLClmoiHAom0ZeZb0BzrZ6oBtTavIinrU7FbA3Zh5vTmmuPYwfcy98nGSdcXzK1Z8VKPkFkI_Dq5v3la0bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
حمل نعش حفيدة السيد القائد علي الخامنئي.</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/81553" target="_blank">📅 04:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81552">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b8c2207f7.mp4?token=RwfrwlX2WVoqkWygVuHmXN3-mC2vs6m_m_QB3I0aek5gvr1YpDbbyiLfIq8LvJSrGh5iQrcNSTDthKLvpRQnwbTrCcFBCu2xxNR5ac5mcStRffp3p3_vQUG16QvWyDHNOPvE2r3XPKSmCPwQU7R-EKctMh8TiesH9ukZSR_Wd5qJVT2q-n15K-7qQelnslUZ2Zxe9GBCWf95h5Sk_K3hu1ft7UcOfsfDlzMpOtJGJ1cIPJIK02-tCaGeZnFVsSYJyc2zeTX7DTBxQD0-wL-LSIOum4rWa6-2zVAJ2W9v0B97kdr2fKpZfNRNbZ7MPt61_f2H0-qzpH7FdAo0KpLsPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b8c2207f7.mp4?token=RwfrwlX2WVoqkWygVuHmXN3-mC2vs6m_m_QB3I0aek5gvr1YpDbbyiLfIq8LvJSrGh5iQrcNSTDthKLvpRQnwbTrCcFBCu2xxNR5ac5mcStRffp3p3_vQUG16QvWyDHNOPvE2r3XPKSmCPwQU7R-EKctMh8TiesH9ukZSR_Wd5qJVT2q-n15K-7qQelnslUZ2Zxe9GBCWf95h5Sk_K3hu1ft7UcOfsfDlzMpOtJGJ1cIPJIK02-tCaGeZnFVsSYJyc2zeTX7DTBxQD0-wL-LSIOum4rWa6-2zVAJ2W9v0B97kdr2fKpZfNRNbZ7MPt61_f2H0-qzpH7FdAo0KpLsPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
حرم أمير المؤمنين (عليه السلام) يحتضن الصلاة على الجثامين الطاهرة للإمام الشهيد علي الخامنئي وعائلته.</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/naya_foriraq/81552" target="_blank">📅 04:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55db15f31d.mp4?token=LOjl7sp_fFtH-XPwr-wh3m031uP8XMBL_OrSpelmtUBjW-z237N9bXO2Ebx3e9FDUXlSc0udIXMCpS7DxXDiRBQYfsAZlV4kRtmDK51LYNzPrY-ikKAkqn2GyNkP19XLQvYSBh97ykbnEuk_pzeIo2hYxvNFlbNdpMoxb9T-aBcKC3tyaQ8Bihh-aW1R8Zp0mGcH-NA4_t-YHc3skISndF_fu8b6z3Pit70y6Gqy6TeSHFVNvsq9umd_eowdJStxfkhduBEHuzdaMnovcY1weRmPjheBKLNG82_sbam_9AKvLQsc3jXGMiuTgTz00WFGS49SZ2uhxaiWqFxJrcDd3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55db15f31d.mp4?token=LOjl7sp_fFtH-XPwr-wh3m031uP8XMBL_OrSpelmtUBjW-z237N9bXO2Ebx3e9FDUXlSc0udIXMCpS7DxXDiRBQYfsAZlV4kRtmDK51LYNzPrY-ikKAkqn2GyNkP19XLQvYSBh97ykbnEuk_pzeIo2hYxvNFlbNdpMoxb9T-aBcKC3tyaQ8Bihh-aW1R8Zp0mGcH-NA4_t-YHc3skISndF_fu8b6z3Pit70y6Gqy6TeSHFVNvsq9umd_eowdJStxfkhduBEHuzdaMnovcY1weRmPjheBKLNG82_sbam_9AKvLQsc3jXGMiuTgTz00WFGS49SZ2uhxaiWqFxJrcDd3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
حشود مليونية تنتضر قدوم النعش الطاهر للسيد الولي في محافظة النجف الاشرف.</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/81551" target="_blank">📅 04:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0234d7ef6.mp4?token=Z5YsNxi8faR6NQtF370IGrQaICmefKpe73-Oama7vUaGozKjmlKXy4Q02-Fa3sIk74hHR4PeRT7uOgFoDd27XPd1FOfoPZit2mePDjK1_Lo0wrVnzYgPAqeT6L7rwO9e5qT60wp0Z-kMOCN-qSyQxYvode_Hsxu8Ywc7Ht7gmdL98KhS0bsxIH_DAPpKx5tqutmXWT0BswH1NhTX6GkfETd3v7RFRmzzA-ss3OK0IHCUvAWoVTLZjeIZ7n3lAbwPZvceoEVjvZgxqFtnl3xPx-6wROMJldjwQw6exA5K1IGI37tV4sCzYNph969OTeNqmLpbeZHEP-_e3QHdxZYZ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0234d7ef6.mp4?token=Z5YsNxi8faR6NQtF370IGrQaICmefKpe73-Oama7vUaGozKjmlKXy4Q02-Fa3sIk74hHR4PeRT7uOgFoDd27XPd1FOfoPZit2mePDjK1_Lo0wrVnzYgPAqeT6L7rwO9e5qT60wp0Z-kMOCN-qSyQxYvode_Hsxu8Ywc7Ht7gmdL98KhS0bsxIH_DAPpKx5tqutmXWT0BswH1NhTX6GkfETd3v7RFRmzzA-ss3OK0IHCUvAWoVTLZjeIZ7n3lAbwPZvceoEVjvZgxqFtnl3xPx-6wROMJldjwQw6exA5K1IGI37tV4sCzYNph969OTeNqmLpbeZHEP-_e3QHdxZYZ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
حشود مليونية تنتضر قدوم النعش الطاهر للسيد الولي في محافظة النجف الاشرف.</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/81550" target="_blank">📅 04:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c046fea80.mp4?token=jDQoNRETZ3Qae6d6D3LhH_bVUpu52vRRmUsNpJR8qegUBT2e3kB-1lHU3boXyW4e9B7PdZv1ep5UpZwskYQhOimEOcOtXDFo-1WfNI7AeGV-k_hGByjggBBF_y6gDSmPJ53j1aJZuURC-r6oMxyO1N2Alp4VBUYt_576AWZ8S3Uykl70aiMM5wEwaDrzO_2b9fV2ZSy7D6wSfbLzE_a465Mq-jIzRGBr6MgNaCCug3brKODW-GcU8QXBK3Jep_WN7F89QYagoj0bSK5S8Sh7PhurOKUYhQwTD-zvEegsCi0typf6cybVyuqP2egfQq4EmyvYUE_AMU5XCv3Wc_tNPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c046fea80.mp4?token=jDQoNRETZ3Qae6d6D3LhH_bVUpu52vRRmUsNpJR8qegUBT2e3kB-1lHU3boXyW4e9B7PdZv1ep5UpZwskYQhOimEOcOtXDFo-1WfNI7AeGV-k_hGByjggBBF_y6gDSmPJ53j1aJZuURC-r6oMxyO1N2Alp4VBUYt_576AWZ8S3Uykl70aiMM5wEwaDrzO_2b9fV2ZSy7D6wSfbLzE_a465Mq-jIzRGBr6MgNaCCug3brKODW-GcU8QXBK3Jep_WN7F89QYagoj0bSK5S8Sh7PhurOKUYhQwTD-zvEegsCi0typf6cybVyuqP2egfQq4EmyvYUE_AMU5XCv3Wc_tNPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
حرم أمير المؤمنين (عليه السلام) يحتضن الصلاة على الجثامين الطاهرة للإمام الشهيد علي الخامنئي وعائلته.</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/naya_foriraq/81549" target="_blank">📅 04:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ecdec096.mp4?token=ZOmxv4j_AhFlWboFJI4HvIyR4QiY3NAgfZdyYEnPehTCoUMiysm6E44sEXL3qVxlhVrRN4gxFdHWxxyYdQVk4ollpzRT7r-sMnZdCqrvCE_-48g1krrQCXzXNuRxjiMsFzHs-bGTlXTpUK-9dzglNqWtqdCroRVENoB3ZLgOQ5z1BhMsfgZ8XZ9bsbPXVdaARQLQmeET3gY5QdYyC6PUEnvSpMYyEldgpvp7zKn_7pIP2Byv8WdclWXHMLuxTLj4Ga3oUu3gzWFp71hfVHH6z55UeRXJ6OD0AspKl-Cs-QjnLRZLp7gSCmfHO0MQ70_3mLnLorJDkMnlEGa4fHik_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ecdec096.mp4?token=ZOmxv4j_AhFlWboFJI4HvIyR4QiY3NAgfZdyYEnPehTCoUMiysm6E44sEXL3qVxlhVrRN4gxFdHWxxyYdQVk4ollpzRT7r-sMnZdCqrvCE_-48g1krrQCXzXNuRxjiMsFzHs-bGTlXTpUK-9dzglNqWtqdCroRVENoB3ZLgOQ5z1BhMsfgZ8XZ9bsbPXVdaARQLQmeET3gY5QdYyC6PUEnvSpMYyEldgpvp7zKn_7pIP2Byv8WdclWXHMLuxTLj4Ga3oUu3gzWFp71hfVHH6z55UeRXJ6OD0AspKl-Cs-QjnLRZLp7gSCmfHO0MQ70_3mLnLorJDkMnlEGa4fHik_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
العجلة التي تقل جثمان السيد القائد علي الخامنئي وهي تتجه الى الصحن العلوي الشريف لبدأ مراسيم التشييع الرسمي في محافظة النجف الاشرف.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81548" target="_blank">📅 04:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e22e40a6a.mp4?token=cTOD2gakEX4I-IzL1Ln1riIfhPZAJZL-PSAhWQjh6Z9qY_zzOsOYsMxvIiHKrJEc-hYyeLPPulH4ogWfzmr7tic3WBXN8p15RfjuiX6HKZCYOrWqJiecEXDDW-9js3Eoou6cLMLUn3Vsb9J7y3BXB_1I57x2RqwBmNfcaDGciOYcaRZFqwBezn5SAe-wYHMjL0k5ZC08TywgzC_mHyk6wQrQe6tT0xRPLmbsMYRMzcKOTXd4DNnPUL90rHh7pi37Lf5ZcFJNCME2mto1yptO2Yg0h5arM2JxggKZCUOE-yPJEvNWWT0kn1sHAqw2dMi4Tda55EUwlq4Szv05y4IwtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e22e40a6a.mp4?token=cTOD2gakEX4I-IzL1Ln1riIfhPZAJZL-PSAhWQjh6Z9qY_zzOsOYsMxvIiHKrJEc-hYyeLPPulH4ogWfzmr7tic3WBXN8p15RfjuiX6HKZCYOrWqJiecEXDDW-9js3Eoou6cLMLUn3Vsb9J7y3BXB_1I57x2RqwBmNfcaDGciOYcaRZFqwBezn5SAe-wYHMjL0k5ZC08TywgzC_mHyk6wQrQe6tT0xRPLmbsMYRMzcKOTXd4DNnPUL90rHh7pi37Lf5ZcFJNCME2mto1yptO2Yg0h5arM2JxggKZCUOE-yPJEvNWWT0kn1sHAqw2dMi4Tda55EUwlq4Szv05y4IwtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
جموع غفيرة في صحن العلوي الشريف تنتضر قدوم السيد القائد علي الخامنئي(رضوان الله عليه).</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81547" target="_blank">📅 04:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcc2bbee.mp4?token=Iq6qy8oTitaVdiA7ALvx4ilXLmiyCcRvYLBWWuOztfSLXyC6us_wYwYJ1YaDr8KrnRn6QoGevqttB4oLOkenwjKk7orOsmyN5CwYvOIADdHRhE_BjywZcScOxeKW13aOoZfWaG5GSLYBMPsyQa4bzhrpmGm4WAvD9ob64NrQ0RS6gGnbBIZmm5L6oAZwb2ITePYo9Qxp9MTcgC7Onc_NIa4CKWgNniwDO6wBolfntrGZh78zgy9WjfliLB2Gp0iPmMRKHW1QgU9cSQoMEzUhDdAIqpvX_5XTUm0C6USCPoNfPLp4WWN6JTrkFK5sk4oZXP_s8nfftDxhMLz7N_kfRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcc2bbee.mp4?token=Iq6qy8oTitaVdiA7ALvx4ilXLmiyCcRvYLBWWuOztfSLXyC6us_wYwYJ1YaDr8KrnRn6QoGevqttB4oLOkenwjKk7orOsmyN5CwYvOIADdHRhE_BjywZcScOxeKW13aOoZfWaG5GSLYBMPsyQa4bzhrpmGm4WAvD9ob64NrQ0RS6gGnbBIZmm5L6oAZwb2ITePYo9Qxp9MTcgC7Onc_NIa4CKWgNniwDO6wBolfntrGZh78zgy9WjfliLB2Gp0iPmMRKHW1QgU9cSQoMEzUhDdAIqpvX_5XTUm0C6USCPoNfPLp4WWN6JTrkFK5sk4oZXP_s8nfftDxhMLz7N_kfRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الصحن العلوي الشريف</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81546" target="_blank">📅 03:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جمهور كتائب حزب الله في العراق يستمر بالتوافد نحو محافظات العزاء</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81545" target="_blank">📅 03:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81544">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e56111a2.mp4?token=gBGav3I_beC6PcoUvjCEbYHEhQDA0Ef0csv6Ac8pkt_uOSCYhOEZTd2Evm0wRLBaIcS6Y3XXuOcQdmBiaXKeU1-kfDQhBDi2jLKWKLoE0WD1bEdez9iiMWuP5_xvt1Hvg21mJG9byyD_uDHdzLJPLzzPy4wvDRrOTcLwznjy_TSBj-kW4S-JoTN9tk6TjhmbwqqmVrHcHdVTQOr55cx3UCsv5TbjILLnrppUxvhNmnmckwi7iMGPvYUwc2UJPGYHI8wvQUbHllQKEKbIug03_L1v692W9vqAVpxZDVUunq1c76uaUI-TGOkzvmfPmpw0_71t4LDhSGMgpWqlIwGqTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e56111a2.mp4?token=gBGav3I_beC6PcoUvjCEbYHEhQDA0Ef0csv6Ac8pkt_uOSCYhOEZTd2Evm0wRLBaIcS6Y3XXuOcQdmBiaXKeU1-kfDQhBDi2jLKWKLoE0WD1bEdez9iiMWuP5_xvt1Hvg21mJG9byyD_uDHdzLJPLzzPy4wvDRrOTcLwznjy_TSBj-kW4S-JoTN9tk6TjhmbwqqmVrHcHdVTQOr55cx3UCsv5TbjILLnrppUxvhNmnmckwi7iMGPvYUwc2UJPGYHI8wvQUbHllQKEKbIug03_L1v692W9vqAVpxZDVUunq1c76uaUI-TGOkzvmfPmpw0_71t4LDhSGMgpWqlIwGqTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
جميع اطياف المجتمع العراقي يشارك في تشييع السيد الولي الفقيه بمحافظة النجف الاشرف.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81544" target="_blank">📅 03:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Td5e-sYChRgKUmU9g25m6kDRJbNtFckdc8HzFiNzzz__mTDBARbS2UDuvlvtXJeUb07eGDMe-ietludtm-q9ptHxWRM599RnoQgJZC1M5FsVw2RNunsY2vUQuvdimt310h4vxSSBbld_TFyfXoxVv5qmAeWB-q-WiVfweTqilZYUYGoU6T-7X0eTLOaxgws-GRzzJZSILZdGcQOkYdC5_jogOBUzd7eLXeiKnkXK5tFfkCMCebMoR1QTnhf08M4oH_FAGK5gmDfB0aPvAP6pPfGCKxq4tJbgWC-0G5OJcrxzZ2-wBcUs9rCrWrtpQs8NQ7EYBNxDp3y23HbmYJ21Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYdbjimawa7BIzg4TYAAqV_gzPV2hdGZK3QpcjnDiFkqg26bESWi5p22rjGFx4b3X-6ZuxQcD3AAx5wHezUXFJARfq4Msl38gfK-EiFDKyeE4Syig-Hf26R9pxIC3CKAam5O-MulscEpnKwI_E_RcymC0RCnoqcSuE-pvcf4ByGI9jWNl8FvE6rxZpFqRuuj0RJdmfyrKgb9EDLQ0YNlnKg1Ck1kL9Gi-1jp226Pw2ibIFuQA9WT0kysA-E1HD6lE9hDapJ4UF8Y1I40B3RdkFitZCsfcQGSCF8UU1pM_cQBPkvqh_aXH-_0sYXgoZI22GFmswCIl42D7_drtejtDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYbM2KJgh3WvWbzOaFarNoJGuP_eRWTZVUp1OCiVEkh4zq2Gwj-O8kaAAic5Cy1uUG5e1X1WiCidU0ecYLBopE3wDLnSXNhPLCP59IAP6Oah7WGvumMbwJVY-XH5U33aNg7D25__WZ3SsWZUcsEwCy7-13liGga2YS_hDbASqh7tMD76e9PpDiETgvDc43kYyxh5AmnFHDQmIhp55zsS08TFznFOLYr3tgxoKNIhmjXEGo1z-ZzqRAsPMOXbcvqhgyGZzWk_Q-2APETU0eFY7aTs9LKF4oZJTSfnihoDT9R0UAI-5zcOATGZsoKC13252EE2JhZcg590CGBN4GkEiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇷
أهكذا يصنع العشق بأهله؟ مواطنون عراقيون يفترشون طرقات محافظة النجف الأشرف انتظارًا لموكب تشييع السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81541" target="_blank">📅 03:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
🌟
عقب العدوان الأمريكي على إيران.. الرئيس الإيراني مسعود بزشكيان يغادر العراق متوجهًا إلى إيران.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81540" target="_blank">📅 03:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d8bbcecc.mp4?token=P6TFbEg7cFQDhG7_ChmXSp_SmxuEw-NfFlgs6QT7kZN23eabvwujwZ85US1RtOfX3558d-roVNZ27AZXlWa7PkECFAj6kvfSGf3v8WflOUuk7WDPPXJ-rwvSdkgY0cmeVv5Wdr2Ei8Qo9aK9PckqVvqFu2XMghb3DD3jAmm2Ji_b8F4WxgKu4u-5Puv0pcy6IUE-AoJkoU7bU407kZgcQmkmA0Bi6b4Fy1QDMgFZQo4opSjsWgWBB43YXBszfWFlN3VwpIO46Z7MeHNMc2L5s5KunCEsl5Bz_cp15Q7LL0EH6rTKz6IgLEdA5auzJrrfRN_avt_zFesfHnPIu2aTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d8bbcecc.mp4?token=P6TFbEg7cFQDhG7_ChmXSp_SmxuEw-NfFlgs6QT7kZN23eabvwujwZ85US1RtOfX3558d-roVNZ27AZXlWa7PkECFAj6kvfSGf3v8WflOUuk7WDPPXJ-rwvSdkgY0cmeVv5Wdr2Ei8Qo9aK9PckqVvqFu2XMghb3DD3jAmm2Ji_b8F4WxgKu4u-5Puv0pcy6IUE-AoJkoU7bU407kZgcQmkmA0Bi6b4Fy1QDMgFZQo4opSjsWgWBB43YXBszfWFlN3VwpIO46Z7MeHNMc2L5s5KunCEsl5Bz_cp15Q7LL0EH6rTKz6IgLEdA5auzJrrfRN_avt_zFesfHnPIu2aTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
جميع اطياف المجتمع العراقي يشارك في تشييع السيد الولي الفقيه بمحافظة النجف الاشرف.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81539" target="_blank">📅 03:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81538">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6850587fe.mp4?token=jZU3eljyJ_PW6kzZijyGBVM5q_1L1NwtUTD0JdcGlC-JEfYB-lrKGUhpKAVZuyV_rHc_JQb3aHOlYGEdf9Taez3Whe5PUCwLIcm0O9G2IZDtj8IaTuT97Vxx7afrZRA0zwoTKq_z1gWgrjc-dbqFRMCXdahUD7lBdS6CaewpfM5KSvMVSAuQkHjnzhT4jCkHmQDoN5VUZesem6zJiW8Xcu0nPHoZTVsajEJ3GfirowHNVrejlk4Idvao__AxzKKyj-rfAdvlK7wSfFM4A9DXDcW45B727epIN-kparA8Mm-AGypTQ9wZy41rh1QeL1oTpHap16bv27ZN6RVHxIRXVYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6850587fe.mp4?token=jZU3eljyJ_PW6kzZijyGBVM5q_1L1NwtUTD0JdcGlC-JEfYB-lrKGUhpKAVZuyV_rHc_JQb3aHOlYGEdf9Taez3Whe5PUCwLIcm0O9G2IZDtj8IaTuT97Vxx7afrZRA0zwoTKq_z1gWgrjc-dbqFRMCXdahUD7lBdS6CaewpfM5KSvMVSAuQkHjnzhT4jCkHmQDoN5VUZesem6zJiW8Xcu0nPHoZTVsajEJ3GfirowHNVrejlk4Idvao__AxzKKyj-rfAdvlK7wSfFM4A9DXDcW45B727epIN-kparA8Mm-AGypTQ9wZy41rh1QeL1oTpHap16bv27ZN6RVHxIRXVYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كاميرا نايا
تجري لقاءات صحفية مع المواطنين في محافظة النجف الأشرف التي تحولت لأكبر تجمع بشري للتشيع جثمان السيد القائد</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81538" target="_blank">📅 03:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ae3e981d.mp4?token=T1fVGHcv7es1moGODP8VqoFXWJ4a_jOYtflQanlqRXKQqu2z4pyw7qinSpa2gwGODlqOX_rudz4xpO2lmNvtEO4xtq_oFRKC-JHKK60v_aYDweac57UZ-5NveCdnu-rpz_izh6L9BhORR4AcFy5UbfZUTW_CUsmIwPLut_GUjcr04UNFMpTHNk00oFcC7hNZj9gDISQR4gVNVqEggmFxbU_lV4i5HWEIgtnTINiSCyVdlbRFIQg1J2hOzdvm5lUepF4aArtww_mLLQMJBDYIU8g3YtQJ_djrsPNmPjGpK4sdGEaMtwsI3Pqcruj-LX3V5-GimZ9RrcTLeCpHrjZ3mDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ae3e981d.mp4?token=T1fVGHcv7es1moGODP8VqoFXWJ4a_jOYtflQanlqRXKQqu2z4pyw7qinSpa2gwGODlqOX_rudz4xpO2lmNvtEO4xtq_oFRKC-JHKK60v_aYDweac57UZ-5NveCdnu-rpz_izh6L9BhORR4AcFy5UbfZUTW_CUsmIwPLut_GUjcr04UNFMpTHNk00oFcC7hNZj9gDISQR4gVNVqEggmFxbU_lV4i5HWEIgtnTINiSCyVdlbRFIQg1J2hOzdvm5lUepF4aArtww_mLLQMJBDYIU8g3YtQJ_djrsPNmPjGpK4sdGEaMtwsI3Pqcruj-LX3V5-GimZ9RrcTLeCpHrjZ3mDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوموا لله يا شعب العراق العظيم.. السلام على رجال الحشد الشعبي وفصائل المقاومة العراقية البطلة</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81537" target="_blank">📅 03:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c197ab9d7d.mp4?token=k5bZekLMlLIo5MG5cSTzCZAFEGImSsogZx7nauF7efx8o8Xj0nnPsw-grBIyymrf75hQOtE1EarEZgmoYPWe48lsWyXTVLDrWKvZbC2H8blpwYVAnUKLwMveo2ysGKIlPD9bJuQRiIGWVs8N_B4Jbgs-BZ1RHl5ZVPVg3rXMZsR5kAYv18pvic8wVSwQswVDfcErZjqathvKptLBNxF2W4joLCOybftIjwyAKs2xZJ-AkUXSJUA3STJsmQg_qgVa8wUC_v7yNSft5563kSzO6zt8TYWEs0FCypZRt_WIYW4OdeooS6KTwvDSIdhcKaL5Yr4liBFK0EQaAycDA9jMPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c197ab9d7d.mp4?token=k5bZekLMlLIo5MG5cSTzCZAFEGImSsogZx7nauF7efx8o8Xj0nnPsw-grBIyymrf75hQOtE1EarEZgmoYPWe48lsWyXTVLDrWKvZbC2H8blpwYVAnUKLwMveo2ysGKIlPD9bJuQRiIGWVs8N_B4Jbgs-BZ1RHl5ZVPVg3rXMZsR5kAYv18pvic8wVSwQswVDfcErZjqathvKptLBNxF2W4joLCOybftIjwyAKs2xZJ-AkUXSJUA3STJsmQg_qgVa8wUC_v7yNSft5563kSzO6zt8TYWEs0FCypZRt_WIYW4OdeooS6KTwvDSIdhcKaL5Yr4liBFK0EQaAycDA9jMPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
جميع اطياف المجتمع العراقي يشارك في تشييع السيد الولي الفقيه بمحافظة النجف الاشرف.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81536" target="_blank">📅 03:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8913959e9.mp4?token=G5p_d-OQvbXVxjyKcr3-S6TQW6G1f5wicQaTRzFKlnCS9A7uLIER76K6623NIIoHlyo_nj-s_iHAAlv9J0mKoAw0wxhJ5Tqv4A8HbN6PPEtvyARWRgqlIX6vRWwQe0pB4NldPe06X1DDccEmoQvfxUr3ERNIBNESw9KRfqJfkDrdfHq_EzudvnU_lPyHX5gGLxmogSienFQnajF19eNtOH1_HWtsd6dN07tbWdmbGjx3EepJo12KZBaZbYREfnKxM_qWkW_VZ0V662xSQtkOHLuKA7IhDDUmTcxcbS4V48D5gAojhzZIJqcfL1eEQmQHe3sWFZsgamZtkmT8MmAn5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8913959e9.mp4?token=G5p_d-OQvbXVxjyKcr3-S6TQW6G1f5wicQaTRzFKlnCS9A7uLIER76K6623NIIoHlyo_nj-s_iHAAlv9J0mKoAw0wxhJ5Tqv4A8HbN6PPEtvyARWRgqlIX6vRWwQe0pB4NldPe06X1DDccEmoQvfxUr3ERNIBNESw9KRfqJfkDrdfHq_EzudvnU_lPyHX5gGLxmogSienFQnajF19eNtOH1_HWtsd6dN07tbWdmbGjx3EepJo12KZBaZbYREfnKxM_qWkW_VZ0V662xSQtkOHLuKA7IhDDUmTcxcbS4V48D5gAojhzZIJqcfL1eEQmQHe3sWFZsgamZtkmT8MmAn5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
تتردد الأهازيج الجنوبية العراقية بين العتبتين المقدستين رثاءً للسيد الولي وسط جموع المعزّين.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81535" target="_blank">📅 03:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb19c1f2e.mp4?token=YT8uWrNt1wRrm8gwBUFIwi78ZqaCoBxwjJZiTyOnEe5W7coGhbjyGw2Xuh_F1koKJEF2kGrF275axzoe2L6t-Ne70EciCMUfZL_Y9c3_VPhLKf1U_ejYVruJu50u2LAR-84QomchrZ3L8BzwtJzv2QXzk2KI_qCFrlqBrboGKvHUiQ7pe6xel8z2MVgVAYYrZGqEsUimb-d4BH5kmfai0jPCgCKHbEv-2dVL5-YodYAbul50o_CiEKIWOd4NLH84xsR5akBPkn2dcIYIwy5XxVy9NVTGDBWJ91T3C2tIFfzvivva1wiB6qcqYDtpgRp316r-VnSzcu3ptHbZDS1Keg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb19c1f2e.mp4?token=YT8uWrNt1wRrm8gwBUFIwi78ZqaCoBxwjJZiTyOnEe5W7coGhbjyGw2Xuh_F1koKJEF2kGrF275axzoe2L6t-Ne70EciCMUfZL_Y9c3_VPhLKf1U_ejYVruJu50u2LAR-84QomchrZ3L8BzwtJzv2QXzk2KI_qCFrlqBrboGKvHUiQ7pe6xel8z2MVgVAYYrZGqEsUimb-d4BH5kmfai0jPCgCKHbEv-2dVL5-YodYAbul50o_CiEKIWOd4NLH84xsR5akBPkn2dcIYIwy5XxVy9NVTGDBWJ91T3C2tIFfzvivva1wiB6qcqYDtpgRp316r-VnSzcu3ptHbZDS1Keg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
أهكذا يصنع العشق بأهله؟ مواطنون عراقيون يفترشون طرقات محافظة النجف الأشرف انتظارًا لموكب تشييع السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81533" target="_blank">📅 03:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJvh6vm0yQDYIfRpmZGc1TthH7kzpiLv2o5UEPTzYcTXmGBCxs-QFeFoOdLTL80RsazUtBiqGFAZMIOHcKMn2-Bl3O5I4S4dO1KHTt38CKP2KDekXbvdxLVHZ7Albo7ZbUWci2BxreqYn8HSq6-HVx1ALPRdTmu88ezVlupMU9GeQjg-RZVpmXxZOm38pFC0SrdBWd6UX1xlPp5D8uWveNcD7cQ_E7dVZPUHUXjq2yTmy4ZndVT2ZhvzYr0WSkjxE_jfVXQIU6nwNxl8ORXLthF_RMsBdljH-t0p_vTPgAqQlq42jod030JR0R8g67EXsfuSxTinqHtehkyNB3ZMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
لافتة "اقتلوا ترامب" ترفع في حرم أميرالمؤمنين عليه السلام بالنجف الأشرف.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81532" target="_blank">📅 03:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2547fabe80.mp4?token=HEJK8Oo5GUs94PZm22TY6rC8CaC891R5S5JwLStHIntBFwMXjehqgjKDRXMRclLR6QUPXf-rAsrq-jOW_6ZBtoiTsDST2ApOGvxbmd02g6zQ7v5U3NrmmJPFlm2bwjLJxxUr4zrklFk79YP8-Gymz5XCuIdujazunFoOQAx4KuPWJY1Hj58XwoZy4nxJntAYzHwuI0McrAfESkqhoenVZrCiqtEU2ATNdwZS8bA902MNOD1r3sjQaAv3RcxzCACYd_F4SpbccecIjw2Lv-YFQr-nhXz_28h7a_kOA71hMQ4gkgzduqUSDDMOwohHyIBo2isEpf2buvqDODROkGjtgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2547fabe80.mp4?token=HEJK8Oo5GUs94PZm22TY6rC8CaC891R5S5JwLStHIntBFwMXjehqgjKDRXMRclLR6QUPXf-rAsrq-jOW_6ZBtoiTsDST2ApOGvxbmd02g6zQ7v5U3NrmmJPFlm2bwjLJxxUr4zrklFk79YP8-Gymz5XCuIdujazunFoOQAx4KuPWJY1Hj58XwoZy4nxJntAYzHwuI0McrAfESkqhoenVZrCiqtEU2ATNdwZS8bA902MNOD1r3sjQaAv3RcxzCACYd_F4SpbccecIjw2Lv-YFQr-nhXz_28h7a_kOA71hMQ4gkgzduqUSDDMOwohHyIBo2isEpf2buvqDODROkGjtgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
لافتة "اقتلوا ترامب" ترفع في حرم أميرالمؤمنين عليه السلام بالنجف الأشرف.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/81531" target="_blank">📅 02:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c55b9859.mp4?token=okiMYKVLyxPgPWGww9LDei5IcrFxpgEUkhYVFS3ARgdm3FmgOZNJwUHkX59hzCEIAN6AWAvphpfayKo7uzaV0FOMIBDxY2C-Hc7EP30s_zvAZgOHCU1SXC2CJosozIPBwb_kVO-upLeKxU7Gtfe3TN9tMMMAWTYnyXy51P3yOVe2u9-y2C1sTGzriwGzPdpnNL1RiSXFcLQm95larR1X1WQFvaMO_F-dSOP5PvvZjgvvegOCXofsD-g-vNubW83zOykBlCJBmTOBoownVrqS858jzWM9BxFLVCu9IdpVD5DUyJ7ecOyjH1pFkSfeESO9yBr3VDfaQyP35tGvH-GLUYAd-wbKBWzlEhDcprW934u_XUzgNCGA0b56Q8ytciaxMy0dXTh1fiXUwmcNv9E-1g4vqYfeKVqtXoxoyU1T-UfoP3CKCOZOjT-xqgV0dXLHPHHJsboeMl1myXgblsGM_7hXNMcHkox7T5YB-wZdPpe-7qc1BKg8JPLVSAje92sm2J3CMq0CFhFCTzd_X6zxgrwTy2xfpkIruXKZ7rrwE4Pzfp6OkU6zLX3w9G9jlUV1y4i0W4RfzunJpJxzghy9VUDFObFj3kyTQyYFqyyMn0jKjhZZUv0zogpnScYcoIFcUV77XuEJKp-0vE_-ecRWJ3vei15etqd_MdYK5XHRIFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c55b9859.mp4?token=okiMYKVLyxPgPWGww9LDei5IcrFxpgEUkhYVFS3ARgdm3FmgOZNJwUHkX59hzCEIAN6AWAvphpfayKo7uzaV0FOMIBDxY2C-Hc7EP30s_zvAZgOHCU1SXC2CJosozIPBwb_kVO-upLeKxU7Gtfe3TN9tMMMAWTYnyXy51P3yOVe2u9-y2C1sTGzriwGzPdpnNL1RiSXFcLQm95larR1X1WQFvaMO_F-dSOP5PvvZjgvvegOCXofsD-g-vNubW83zOykBlCJBmTOBoownVrqS858jzWM9BxFLVCu9IdpVD5DUyJ7ecOyjH1pFkSfeESO9yBr3VDfaQyP35tGvH-GLUYAd-wbKBWzlEhDcprW934u_XUzgNCGA0b56Q8ytciaxMy0dXTh1fiXUwmcNv9E-1g4vqYfeKVqtXoxoyU1T-UfoP3CKCOZOjT-xqgV0dXLHPHHJsboeMl1myXgblsGM_7hXNMcHkox7T5YB-wZdPpe-7qc1BKg8JPLVSAje92sm2J3CMq0CFhFCTzd_X6zxgrwTy2xfpkIruXKZ7rrwE4Pzfp6OkU6zLX3w9G9jlUV1y4i0W4RfzunJpJxzghy9VUDFObFj3kyTQyYFqyyMn0jKjhZZUv0zogpnScYcoIFcUV77XuEJKp-0vE_-ecRWJ3vei15etqd_MdYK5XHRIFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
أهازيجُ جنوبيةٌ عراقيةٌ تصدح في منطقة بين الحرمين رثاءً للسيد الولي.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81528" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f53e1a044b.mp4?token=PsvKC_hAoyuKbHU2_YL_JiicCQP16RgUptPgIcEbzH9IZzDRohx_VK0byrq17zt-dkf59d9sRh4by-Lx1JHXCDJ4xYiS1et8u5014bSx8ABhDr7xvh0zkF7V9QAC7jMyrM_pOHHI5gpOt6Kn03VxiUjJstkWi8iOJYoR6DiLm8PeFBHWU6HlLV8hrzefonaA6TLbexyQVBUHOehvIXwP4_HKcZAtc_PnwRuAAIaINHDP7Wytl354er8ElEtUhukMdOwtB0RDZn5-ADWnH5zhg3hnye_1PRbC1hDqjIeyf_vHGjAU-ydZKMvEk7_KUgYo3j8GInASLQ8r6p8BLs6KoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f53e1a044b.mp4?token=PsvKC_hAoyuKbHU2_YL_JiicCQP16RgUptPgIcEbzH9IZzDRohx_VK0byrq17zt-dkf59d9sRh4by-Lx1JHXCDJ4xYiS1et8u5014bSx8ABhDr7xvh0zkF7V9QAC7jMyrM_pOHHI5gpOt6Kn03VxiUjJstkWi8iOJYoR6DiLm8PeFBHWU6HlLV8hrzefonaA6TLbexyQVBUHOehvIXwP4_HKcZAtc_PnwRuAAIaINHDP7Wytl354er8ElEtUhukMdOwtB0RDZn5-ADWnH5zhg3hnye_1PRbC1hDqjIeyf_vHGjAU-ydZKMvEk7_KUgYo3j8GInASLQ8r6p8BLs6KoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
دخول نعش السيد الولي علي الخامنئي في ازقة محافظة النجف الاشرف.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/81527" target="_blank">📅 02:40 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/hHN-KtnS6JNJw2NUUrZ-gGJkC4e1i0Lmz9pRJ2gFWdOLek1_ZHF0fb2dBgzcs0tbm0pynx0KA8eua1W_7LmRQFSN1NIHwWzCqkdaCh2f16ryn-3BoNfbuS9gxK6B74zY9-yPDjTh4YWARBm0VqE8bkGiJvLjO3mPmz0a4Cg63Ys8gA-FdZP5KHi01Uk2q08J4kR4gOSKa7OTB4TZ9Eq3ZyQUNK-3OZpsOs9BfZDtx1Wk-70hU9pQoYVRvuoZdTcWYmoW7z9_HAJulV49y0HiRzzSjv36EDf84S2fQP8NG_xF0u3pUraZwG4k96RpLGjz3lC9ReFI2HhbmioUCc_WXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 14:49:00</div>
<hr>

<div class="tg-post" id="msg-84400">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN9stcygTg9MQqGSEuNAuRfq7FU9T9ThfWXztQ3p6kC6APUNEoCYiT70W85yHybI2J76HrcnT5fDEbWpyWDCIrStqiEzrgvjY_qfGNFxAorz8iVqxivSuSfabWDbNgiD-DkZXYIGEE-M9Z2s9BiGwdABUwDeH-geGHqC8lNDf-a9L21DTyCnyuamSNFzGRrx_fyjLGUrLw0YPDtkTR2nvSmsICWaclw9rGctVUixQIvvutvCj2K6c-A1JOv3mWOhsRMVkdZ1hsB_kKltPFKs94mco5LRbPeka3-ZI5pbZsWVL12vDFMWzjyIK0SgM-YWq5wmjcWFZ_cU94SvUbKZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
‏يُواصل الأمريكيون جلب معدات عسكرية جديدة إلى المنطقة، ويدّعون رغبتهم في وقف الحرب. لقد اعتمدوا على معلوماتنا الاستخباراتية، التي لا تتجاوز مستوى ذكائهم المتواضع. ‏لقد وصلنا إلى مرحلة التخطيط لهذه الألعاب الأمريكية، وقد استعددنا وفقًا لذلك. يجب أن تؤكد الأفعال هذه الادعاءات، لا أن تناقضها.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/naya_foriraq/84400" target="_blank">📅 14:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84399">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOglC_wtJVeMXuxxGvxlgGP4k8eNhVkknqOOyOXPrWgC6veVu1rQLG2K7ijCkf24tjcatdcKFkqoOkaKEUD-9HV-Sd8FLZUK15rELwyXMxocaiBeke1Rr_zcAI6L0keW6Pp15eD5UKt1oLn4Mns7hDmtxGvRV8h4nG6vo6mkD1xbHpMPydwbPl2-2JRn4yoDhuuS5X3V3mBUgf_sZgl0-sLByoSAMrPElTOUQvSFLONhX2sR3TBuaNqUuvsGSDGNcogDj8CZpBM1pZMxDioKsBnY6dfRfPp8lI0r_n6U71lfeE5ffBObCPzot3g8nW4L3Dj4nj4p8r5FEg70gCt42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بيان:
‏تعلن حركة المقاومة الإسلامية حماس عن انتخاب الأخ المجاهد خليل الحية رئيساً للمكتب السياسي للحركة خلفاً للقائد الشهيد يحيى السنوار.</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/naya_foriraq/84399" target="_blank">📅 14:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84398">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏الطيران المدني البحريني: عدوان إيران استهدف أجهزة الملاحة الجوية المدنية للبلاد بمسيرات</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/naya_foriraq/84398" target="_blank">📅 14:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84397">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سقوط طائرة مسيرة امريكية من طراز لوكاس بالقرب من رأس البيشة في منطقة الفاو الجنوبي في محافظة البصرة جنوبي العراق من دون ان تنفجر</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/naya_foriraq/84397" target="_blank">📅 14:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84396">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">باكستان وقطر يقدمان مقترح مشترك لحث الولايات المتحدة وإيران على العودة إلى موقف ما قبل 9 يوليو/تموز "كخطوة أولى" لاستئناف المحادثات</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/naya_foriraq/84396" target="_blank">📅 14:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84395">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huSg0qr-5YJTRaSqhzC653tD6RHSmvFN4vFRGXA0I_avxUV797vcECXw2ekJs3mwlgAxhfzj562uCWJDXDvj6yPBC-8SvSacxlDJyAIgQNsFRpLHariS7n6dHRDpFk_hr5ElTfWC6Xdh0lupsfi-bhdw7EtCZVZ92bWszyiNeBLQHEmfkuvMtDiXq_qfKCp16QWlJmMaruClb-1sJepRqNvc7L8YVUrEQp9fATL4J2USlcGnwDJav8dnQSRpaYnnkd7NO6NmEH0hj340T5tC-8YtyR9LT9rKCjzAnrExa8azZ9dbxUaS0FCI7dFIRNLG35-_NZyEwZmEl95Z6o3flA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
جيش العدو الامريكي يكشف عن هوية اثنين من قتلاه خلال الهجوم الايراني على قاعدة موفق السلطي الجوية في الأردن:
- الملازم أول تايلر جيمس فيهان
- الجندية إيزابيلا غونزاليس</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/naya_foriraq/84395" target="_blank">📅 14:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84394">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇨🇳
وزارة الخارجية الصينية:
اليابان تحاول إحياء قوتها العسكرية والسعي للحصول على أسلحة نووية، إذا سعت اليابان إلى تعديل "المبادئ الثلاثة غير النووية" فإن ذلك سيقوض النظام الدولي الذي تأسس بعد الحرب العالمية، وينتهك التزامها بالسلام، وسوف تدفع في النهاية ثمنًا باهظًا.</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/naya_foriraq/84394" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84393">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇰🇼
الجزيرة القطرية:
الكويت تدرس خفض نسبة الدوام الحضوري في مقار العمل؛ لتخفيف الضغط على شبكة الكهرباء والتعامل مع التحديات المرتبطة باستهداف محطات توليد الطاقة</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/84393" target="_blank">📅 13:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84392">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
🇾🇪
إسماعيل بقائي، المتحدث باسم وزارة الخارجية الايرانية:
في رأينا لا وجود لما يُسمى "حظر جوي" على اليمن ونعتبر ان مبدأ فرض العقوبات على أي دولة مبدأً قاسياً.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/84392" target="_blank">📅 13:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84391">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
مصدر أردني لنايا: وقوع عدة إصابات في صفوف القوات الأمريكية نتيجة الهجوم الصاروخي الإيراني الذي طال قاعدة موفق السلطي بالأردن.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84391" target="_blank">📅 12:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84390">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📰
نيويورك تايمز:
البنتاغون يخفي عشرات الإصابات بين أفراد الجيش الأمريكي في الحرب الإيرانية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/84390" target="_blank">📅 12:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84389">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f9ad4d954.mp4?token=quNPZA3g4cEbwI64pbvvbRz5V13eRB6UG6YNNtqkY8U-FbxioSl_31uaoPd6cOYroXwCAX0W587xnBUlZA7B4Ye5pNQk6UayytM1QuEjSSDqAMbgw0Qsa9JWITWKp9cFz6Fh9Nls0Y0Ncpn7Uhcb0bICfv5Si-5wa8I3qVHrxPDowLm4AGWlS9Vlqqo0GqveRHny-D5GhtZX2Z1-Cj6jN5lBYiHb4GQYRBSE3bKtp0MLcYbXnu2Q-vsb8mOasy515Saab8WoT_Wrgiq1jh7vwGDiN0D7UnMXEBTqt_fDVKjnhcwt1NeNZyurzEeDaPKeYBrZDIhpsOvfvA3jMyDxhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f9ad4d954.mp4?token=quNPZA3g4cEbwI64pbvvbRz5V13eRB6UG6YNNtqkY8U-FbxioSl_31uaoPd6cOYroXwCAX0W587xnBUlZA7B4Ye5pNQk6UayytM1QuEjSSDqAMbgw0Qsa9JWITWKp9cFz6Fh9Nls0Y0Ncpn7Uhcb0bICfv5Si-5wa8I3qVHrxPDowLm4AGWlS9Vlqqo0GqveRHny-D5GhtZX2Z1-Cj6jN5lBYiHb4GQYRBSE3bKtp0MLcYbXnu2Q-vsb8mOasy515Saab8WoT_Wrgiq1jh7vwGDiN0D7UnMXEBTqt_fDVKjnhcwt1NeNZyurzEeDaPKeYBrZDIhpsOvfvA3jMyDxhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب يتحدث عن بيدرو سانشيز: ‏تحدثت مع إسبانيا وهنأتهم على امتلاكهم فريقاً رائعاً. ‏لا توجد بيني وبينه أي توترات.
ولا توجد بيني وبين أي شخص أي توترات.
😄</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84389" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84388">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2bscMp8Dqr4I0L4IkK_RZNC3XRc52JPAI64ZRE0Cr2uGqS179qqyOv66zpMBpZY2lqzAm103s7QVYDNrqv0dH-zPd21Fkyxsr9daAdgBwF9PPE7yWdqve_60evXHiCvJCK2pgNcJOlQYTxLlUGKhqB1vTLUaualWIQZ23p8ZbnnthGgLGLcNupSbh3yyRURd3f8hNbDRa-nIvaVX68E9VjgqJU80gHMUeXdcpQt59dHNCImtUjXmN-4YbsOwCIFO0hDeNa1eQ80hAy-zKtjLDpxXC1G5rYmEna2M0JhB2bvO6NIBafsOqqJtucP90loi0h0oyfUU--J-J7q8xPtnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوارع طهران حاليا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84388" target="_blank">📅 11:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84387">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">#ترفيهي
القيادة العامة لقوة دفاع البحرين: إيران تواصل نهجها العدائي الممنهج عبر اعتداءاتها الآثمة التي تستهدف المدنيين في مملكة البحرين.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84387" target="_blank">📅 11:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84386">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🇵🇰
وزير الداخلية الإيراني يصل باكستان اليوم حاملا رسالة خاصة من بزشكيان تتعلق بملف المفاوضات</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84386" target="_blank">📅 11:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84385">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79a89642f.mp4?token=Kif_UDOTHDz1yaDMuldSrIJAivL1oBp9hI0Tt_cVjQxw0RIblnUuS1iWnW3qn0H8UoXB2ave7FARyNoFHXZkrBhHfseXztSgZ6aBEWt6nephgOzmvHoiFWOmlQpjfZWuG2fMJxT7PY39c735ziEfFU1OqlTXtcgtxek0nRJlNbokkT6HMTx7Fs4IJ3nAYLj0Ugrk9g38eXYhAcwmMFy9bxh_xl-cnvpHwJ6qTlyi4v6KbXhkf6MZu2nQmpVEr0yZgmCd4DGZkApDbKgsqYAd7FExuQgivcR54mKjvXdKociG3Nt4o3kR8s6xDxlGstmBmCG5XxVHuSZZeo1wkMRDGylNEOsjSrwSFRUsMctkO5f3HqFmdMNQ0KQJBWr0a7EuU9a-V39o1j9UdXiTeOi-Imeh7lttKbrovx8PR7-r20iiYwMc-uMUw8RYFgwkbgs-54XvcLO7J6bdSNzVR8L1Ttl4bp1u0P-3Rl946P7FZOR1FIJbQFenoE0T8YSeJ22dRrP_W2aqtiKVSJSVL-MJji2J8eEOMugEr1_l-LEIljfshiYTqSrc23HrM17ApuY1rasVbZLBg3oKpTPniNoU9Nuf2jS2BzhbC1j5dPTqRcgDvulCKRekac5p93p9nbPEeHpHoj4piEvFAIC6YuQm6vpTdlIr9ML9HbBOBv3ckBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79a89642f.mp4?token=Kif_UDOTHDz1yaDMuldSrIJAivL1oBp9hI0Tt_cVjQxw0RIblnUuS1iWnW3qn0H8UoXB2ave7FARyNoFHXZkrBhHfseXztSgZ6aBEWt6nephgOzmvHoiFWOmlQpjfZWuG2fMJxT7PY39c735ziEfFU1OqlTXtcgtxek0nRJlNbokkT6HMTx7Fs4IJ3nAYLj0Ugrk9g38eXYhAcwmMFy9bxh_xl-cnvpHwJ6qTlyi4v6KbXhkf6MZu2nQmpVEr0yZgmCd4DGZkApDbKgsqYAd7FExuQgivcR54mKjvXdKociG3Nt4o3kR8s6xDxlGstmBmCG5XxVHuSZZeo1wkMRDGylNEOsjSrwSFRUsMctkO5f3HqFmdMNQ0KQJBWr0a7EuU9a-V39o1j9UdXiTeOi-Imeh7lttKbrovx8PR7-r20iiYwMc-uMUw8RYFgwkbgs-54XvcLO7J6bdSNzVR8L1Ttl4bp1u0P-3Rl946P7FZOR1FIJbQFenoE0T8YSeJ22dRrP_W2aqtiKVSJSVL-MJji2J8eEOMugEr1_l-LEIljfshiYTqSrc23HrM17ApuY1rasVbZLBg3oKpTPniNoU9Nuf2jS2BzhbC1j5dPTqRcgDvulCKRekac5p93p9nbPEeHpHoj4piEvFAIC6YuQm6vpTdlIr9ML9HbBOBv3ckBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد لاحتراق منطقة واسعة في معسكر للمعارضة الإرهابية حيث تم تدمير مبنى بشكل كامل في السليمانية شمال العراق</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84385" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84384">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇷
نائب قائد القوات البرية في الحرس الثوري: سنقضي على أي توغل بري أمريكي في أراضينا فور وقوعه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84384" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84383">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sb3lK8sY64ZZQ2roE6PHlDrSfcTZj0E8siy3q3CFwBfCVlva-6ThR6weGJgtqFiZaAFHkdi90jk2azAD8yX4fzilPknDY13TzHvqqMfs3aY8qquxXvCaEyahGMi8lLYA4wjDuqQs2ThiHIIF0-YSfn1TEogRa7JkekYJICTxyHToCbYmUcbs9sCxT882X5-9eI_NXqKzuLrEvcmhL3LI9iMDI5QQ2EwUf3A2Hr35ZkqJjvvKFlBBeH1sWKZLG9A2fa19WcyvY_6PKHuN2qJlNZlZcz-8kyfFJYck8XbtY1jF7x0R3GWFtC7-Kgcrk5KP4QpHT5pwyif9Y8hWlXbAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
طيران الجيش العراقي يقصف (6) مضافات لإرهابي داعـSh في منطقة (وادي زغيتون) ضمن قاطع قيادة عمليات كركوك.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84383" target="_blank">📅 10:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84382">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔻
حدث بحري في عمان</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84382" target="_blank">📅 10:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84381">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
حدث بحري في عمان</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84381" target="_blank">📅 10:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84380">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تجدد الانفجارات العنيفة في البحرين</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84380" target="_blank">📅 09:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84379">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">على مايبدو البحرين تعيش اصعب لحظات حياتها</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84379" target="_blank">📅 09:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84378">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">على مايبدو البحرين تعيش اصعب لحظات حياتها</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84378" target="_blank">📅 09:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84377">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84377" target="_blank">📅 09:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84376">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
إعلام إيراني: سماع دوي انفجار في مدينة أصفهان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84376" target="_blank">📅 09:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84375">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
🇧🇭
المشاهد الآن من البحرين
🔻
تُظهر صور أقمار صناعية أضرار على محطة فرعية للكهرباء في البحرين حيث يُستخدم الموقع كمركز قيادة وسيطرة (C2) عسكري أمريكي ومركز بيانات للذكاء الاصطناعي إثر الهجوم الإيراني.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84375" target="_blank">📅 09:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84374">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84374" target="_blank">📅 09:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84373">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/84373" target="_blank">📅 09:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84372">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇱
🇺🇸
مسؤولين صهاينة: التقديرات في إسرائيل أن واشنطن قد تطلب إدخال عشرات الطائرات الإضافية للتزود بالوقود إلى إسرائيل</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84372" target="_blank">📅 09:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84371">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc91471066.mp4?token=VsbIRbswG0piI27IorFm4K6kMB2pmH1CrKlEKvRD6GNQbfLcaaxqe2i1LbHdMt0ldDfgeT6VUHc_0VzYVhXiaiz3XiPWT9m2r_6FalLAIUsoWtDmsvWoFO_x0X18iWD5bcMcoDccVaKGIKRHoTfBYb509rWXDgNX07pIZwA5ZXGln15uJWXMglWmc5n4HMobs7ItWFINirwyMNJk40qaUpCWbNfjqTlKvDLWGhZ8eRbZRB5OvKbaof5VJRJr1tey8en5y_uvR3yJ8zS5I1q5k0Eu5R5cn6E1p6WEXUhG9S93euv-bO1KpMjpln3aCcYTzihfA-lnTm89m6-cr3x9WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc91471066.mp4?token=VsbIRbswG0piI27IorFm4K6kMB2pmH1CrKlEKvRD6GNQbfLcaaxqe2i1LbHdMt0ldDfgeT6VUHc_0VzYVhXiaiz3XiPWT9m2r_6FalLAIUsoWtDmsvWoFO_x0X18iWD5bcMcoDccVaKGIKRHoTfBYb509rWXDgNX07pIZwA5ZXGln15uJWXMglWmc5n4HMobs7ItWFINirwyMNJk40qaUpCWbNfjqTlKvDLWGhZ8eRbZRB5OvKbaof5VJRJr1tey8en5y_uvR3yJ8zS5I1q5k0Eu5R5cn6E1p6WEXUhG9S93euv-bO1KpMjpln3aCcYTzihfA-lnTm89m6-cr3x9WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"
اخ عليج يالكويت تعورت يالكويت "
مواطنة كويتية تتحدث عن ألم و حزن في قلب كل كويتي بسبب القصف الإيراني القققاشم … مراقبون اكدوا ان لو لا وفاة المرحومة الفنانة ذات الأصول العراقية حياة الفهد لكان شاهدنا مسلسل رمضاني يتحدث عن كيف هرب جاسم بالوانيت نتيجة القصف القاشم !</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84371" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84370">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOiqhDQjIUKqRT2ZK6AHq5H-ckU8y0RYTHEnvu0T2IwkIhgAU1hyjh8mmwv0rb4tg9EQ0HpNfh1H_wN3Od7d_oVh2Txmzf0-u2ww0XaJrXcuCeQxXySI5ebHuEpCQMAy3Evi60v-yfcSePvvMLvLsVxHOQlxawtXTzxD2-q5-TFxnTsjdT8B4JCTS4PgAUra0CC5MlZ-Q85yCxk0DI3uSDJg-muFNzcHpknxIgIUuyniijeYpDmm014ItHiQcOQyIshaQIyAB7jMj6em33hIBJVniFJiawW13DmD1fWYCpyCpnobzng4VBL8FKlQBvYgj7xOCi-Ec7eXITErwWZewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط مباشر في المنامة وتصاعد أعمدة الدخان من مكان الاستهداف</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/84370" target="_blank">📅 09:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84369">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات متتالية تهز البحرين</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84369" target="_blank">📅 09:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84368">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">البحرين تحت الصواريخ الإيرانية من جديد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/84368" target="_blank">📅 09:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84367">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/84367" target="_blank">📅 09:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84366">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84366" target="_blank">📅 09:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84365">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجارات تهز البحرين مجددا</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/84365" target="_blank">📅 09:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84364">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/84364" target="_blank">📅 08:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84363">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50429d07bd.mp4?token=mC3eu0jdojq9P3Ye7RKCHqLTVwj3w1vE2Xy1Je6SCrBWIQTIN70HgbewyuPmbu2Dv_3Q575rdH3iNKRdXm07RauwnO8obsWIax6AhQ2U1Q-d8DEROi-CXfgk1uR0NN2fzoOIO4gL-R9DG9NW9v5REmSstAF33ndksdePoAr-mlTdbx2fnkWGPn4Br6il_S82NaeXLRtYoAEkInWs_ukW2J3OqRjExy3ku5fO0jo7GN8uKTGHOkyPss0UdApSPiXYsQRah-5BE8ak-z6ObdEZTng8VSaU4SPSLWDtvlOejM-YWYDMcZ6DSLKBIUEpB69mw1Q7Wm9-DJ_Ux5E8gAemTIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50429d07bd.mp4?token=mC3eu0jdojq9P3Ye7RKCHqLTVwj3w1vE2Xy1Je6SCrBWIQTIN70HgbewyuPmbu2Dv_3Q575rdH3iNKRdXm07RauwnO8obsWIax6AhQ2U1Q-d8DEROi-CXfgk1uR0NN2fzoOIO4gL-R9DG9NW9v5REmSstAF33ndksdePoAr-mlTdbx2fnkWGPn4Br6il_S82NaeXLRtYoAEkInWs_ukW2J3OqRjExy3ku5fO0jo7GN8uKTGHOkyPss0UdApSPiXYsQRah-5BE8ak-z6ObdEZTng8VSaU4SPSLWDtvlOejM-YWYDMcZ6DSLKBIUEpB69mw1Q7Wm9-DJ_Ux5E8gAemTIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
لقطات من الأقمار الصناعية تظهر ضربة مباشرة على مبنى في قاعدة موفق السلطي الجوية بالأردن حيث وقد دُمر المبنى إضافة إلى تضرر عدة مركبات مجاورة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/84363" target="_blank">📅 08:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84362">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇷🇺
🇺🇦
انفجارات ضخمة جداً تهز جنوبي أوكرانيا جراء قصف روسي مكثف.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84362" target="_blank">📅 08:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84361">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارات عنيفة تهز المنامة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84361" target="_blank">📅 08:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84360">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0727eab181.mp4?token=TBvlc8mXpeyNcPLNuMAUdv4LPOrR6IxHaDLdyMxUBmBXmaLbXX5WLWIM2yI_1s_kfbZ_pb4UsWelQkGG8IXPZ053iRlmA0ugS41TzAEMx6-VK1FZqSkFCMgmY_6fn4KQtmPEmrWGWo1yKZKMj-oN96mvxoHKkKi4x2o3du4kXZkzzj6wUiblFgllUWh0qyixY6NpiRnYC5_97WWgkaF9pf56Cuz12fNZfX6jfuGrhmLmC1TVO28GWB-ZB1MNmrcoXlPHjkBR9P0q75qauLirPnHNP__j3_2NptZUNOfhKbNuk5jFA0b_rEsAejgtbMFGK2W-hTv_61NABtHGhGEnrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0727eab181.mp4?token=TBvlc8mXpeyNcPLNuMAUdv4LPOrR6IxHaDLdyMxUBmBXmaLbXX5WLWIM2yI_1s_kfbZ_pb4UsWelQkGG8IXPZ053iRlmA0ugS41TzAEMx6-VK1FZqSkFCMgmY_6fn4KQtmPEmrWGWo1yKZKMj-oN96mvxoHKkKi4x2o3du4kXZkzzj6wUiblFgllUWh0qyixY6NpiRnYC5_97WWgkaF9pf56Cuz12fNZfX6jfuGrhmLmC1TVO28GWB-ZB1MNmrcoXlPHjkBR9P0q75qauLirPnHNP__j3_2NptZUNOfhKbNuk5jFA0b_rEsAejgtbMFGK2W-hTv_61NABtHGhGEnrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇰🇼
لاول مرة
الكويت بدأت باستخدام المولدات الكهربائية المتنقلة للمناطق السكنية بسبب العجز التام لمنظومة الكهرباء على خلفية القصف الإيراني المستمر .</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84360" target="_blank">📅 08:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84359">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">منظومة الباتريوت تفشل بالتصدي للصواريخ الإيرانية في سماء المنامة عاصمة البحرين</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84359" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84358">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/84358" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84357">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84357" target="_blank">📅 08:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84356">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">إصابة مباشرة في مقر دعم البحرين</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/84356" target="_blank">📅 08:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84355">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات قرب مقر دعم البحرية في البحرين.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84355" target="_blank">📅 08:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84354">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84354" target="_blank">📅 08:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84353">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/84353" target="_blank">📅 08:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84352">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84352" target="_blank">📅 08:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84351">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a0ec0dd3.mp4?token=azQGlNhDo6QxYCoPZZE0s-amOMatZKtlI0Ea1d25m9sswCLbY5MaZAVLEAC_KD8u67KFK9m0cLFx12hB9oWPnhQ0DXbymrKsh10ndQE5W0twQfd8fxsRyj1epxN_hJ-Hj2Hea2CVlxaGafU6UHLmNcIJ4bnyawSUtQZdujRakXsi3B6bzpowku9SZe-8lgZ7HgYgzNVtaswy0dc8dYaJWIIeigl0TegFhV8fjT0ocPHnr7eTC4kxvpydH5vFnvW78kZr9rklgPq0A_4tbIPF0Cz9pJOXUdjABramzd4PH99k49fa1ySVGolf0uHHNo7jY9JnGzxwZHjM9QqJUOJHFWSVCLa77BAmVOft7_9lsaWO5kzfHt2TFaB_3ogKm9_pqoaE4gPqK7enqix6LWNd_gDdTStLGipZz0aW5T8eyIQPx6wzi2Ep3LJ1ZE-Fhtk5aqCsI3cRzxdrDiYSxVQsyLYQ96V3DSCo1gArl8hw1XOn7krO6IMZstRadq87oBAcx_nsqGkJN8Kky1p1t45-MdgzXVJMOzyjCVpw88ByUE3B0GBZEhSFlnhnSOMHZUB-NPW11eRSrMywJTemLVJiQmlbcDrDHhHbkRqIAPMFLXlz2egmZ3BltEw4M-CymbkIcyPlV56p92iVGiE1QYdp9S0arPLXBfoxpWLK_oiAke4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a0ec0dd3.mp4?token=azQGlNhDo6QxYCoPZZE0s-amOMatZKtlI0Ea1d25m9sswCLbY5MaZAVLEAC_KD8u67KFK9m0cLFx12hB9oWPnhQ0DXbymrKsh10ndQE5W0twQfd8fxsRyj1epxN_hJ-Hj2Hea2CVlxaGafU6UHLmNcIJ4bnyawSUtQZdujRakXsi3B6bzpowku9SZe-8lgZ7HgYgzNVtaswy0dc8dYaJWIIeigl0TegFhV8fjT0ocPHnr7eTC4kxvpydH5vFnvW78kZr9rklgPq0A_4tbIPF0Cz9pJOXUdjABramzd4PH99k49fa1ySVGolf0uHHNo7jY9JnGzxwZHjM9QqJUOJHFWSVCLa77BAmVOft7_9lsaWO5kzfHt2TFaB_3ogKm9_pqoaE4gPqK7enqix6LWNd_gDdTStLGipZz0aW5T8eyIQPx6wzi2Ep3LJ1ZE-Fhtk5aqCsI3cRzxdrDiYSxVQsyLYQ96V3DSCo1gArl8hw1XOn7krO6IMZstRadq87oBAcx_nsqGkJN8Kky1p1t45-MdgzXVJMOzyjCVpw88ByUE3B0GBZEhSFlnhnSOMHZUB-NPW11eRSrMywJTemLVJiQmlbcDrDHhHbkRqIAPMFLXlz2egmZ3BltEw4M-CymbkIcyPlV56p92iVGiE1QYdp9S0arPLXBfoxpWLK_oiAke4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇨🇳
قادة أمريكيون:
سلاح فرط الصوتي بعيد المدى "دارك إيجل" انطلاقًا من غوام قادر على تهديد أهداف بالغة الأهمية في البر الرئيسي للصين.
ربما يكون الجيش الأمريكي نشر هذا السلاح خلال مناورات "فاليانت شيلد" خلال تدريبات على استخدام "دارك إيجل". حيث لم يكشف عن الموقع أثناء هذه المناورات، لكن الصور وتحركات الأدميرال صموئيل بابارو في يونيو ومنطقة التدريب تشير بقوة إلى غوام.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/84351" target="_blank">📅 07:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84350">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
مركز رصد الزلازل الأورومتوسطي: زلزال بقوة 5.5 درجة يهز غرب إيران</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84350" target="_blank">📅 07:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84349">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
مركز رصد الزلازل الأورومتوسطي: زلزال بقوة 5.5 درجة يهز غرب إيران</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/84349" target="_blank">📅 07:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84348">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
هزة أرضية قوية شعر بها معظم سكان العاصمة العراقية بغداد في هذه الأثناء.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/84348" target="_blank">📅 07:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84347">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هجوم جوي جديد على البحرين</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/84347" target="_blank">📅 07:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84346">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eadd25eee.mp4?token=rufIShhm1P4j28vwfaPd9OEy6YgcPUssGeqlTfMuXPVyIryA32wcPRH_0AN7wcLYwRl9f3ISAQ0WsrGpPsiL_2_dUdCiPeYpc2yIbkk47bsSdVir_CB8G5vWW4qERZVc-CJXC2SZbRJwB91JUWSQf_Hz2iZ_dQy7DTLkrUq8H-HA0XzKBMvFLRj9b0YVD3IgICwQbIrx6_BpTiSnLIj82qkNUM9BWd6M-rXGvJ-X4lauzC9lCZmg-40yn_d32F5wjZyMzD0SwR2E1-mV_lGfCL_pZ-8GmDqh-3-mJgVN8HJhcHzJ8YI7MJwSe1RngrQdIaJFCJ38dQbU5HI-LSLGKJ0OZQudGyua-gVjZqOmcKpMy0uC7aMWCh4wagTtRbW3MlaWhbTTji2U2TEFWlUtJHd1RIsr2w-M69HXibcOb6gcCUucdOS3y9SKQkgqD9GcVWl9oSGbv8wNcsFd3I1Dlirm55cg6hzIxIdVgBZW98RKWR-9fQ_iO7A40beFyCqHrOo8bzPYn0J5mJ06eTsiSC0kuhkJmIpkZZ8j2F3v46G14foxK0Zkjnrw0N_EMQ54OcnqHYrsLTjdLBep_bl1ADHrYbToFOdZYF7UQ7ooLIhuQANiocO_yfZJHBcCTyqWBQ3sgJe9uhvhNpu3C4uNWn619iIb_SPyBa49cU5ly1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eadd25eee.mp4?token=rufIShhm1P4j28vwfaPd9OEy6YgcPUssGeqlTfMuXPVyIryA32wcPRH_0AN7wcLYwRl9f3ISAQ0WsrGpPsiL_2_dUdCiPeYpc2yIbkk47bsSdVir_CB8G5vWW4qERZVc-CJXC2SZbRJwB91JUWSQf_Hz2iZ_dQy7DTLkrUq8H-HA0XzKBMvFLRj9b0YVD3IgICwQbIrx6_BpTiSnLIj82qkNUM9BWd6M-rXGvJ-X4lauzC9lCZmg-40yn_d32F5wjZyMzD0SwR2E1-mV_lGfCL_pZ-8GmDqh-3-mJgVN8HJhcHzJ8YI7MJwSe1RngrQdIaJFCJ38dQbU5HI-LSLGKJ0OZQudGyua-gVjZqOmcKpMy0uC7aMWCh4wagTtRbW3MlaWhbTTji2U2TEFWlUtJHd1RIsr2w-M69HXibcOb6gcCUucdOS3y9SKQkgqD9GcVWl9oSGbv8wNcsFd3I1Dlirm55cg6hzIxIdVgBZW98RKWR-9fQ_iO7A40beFyCqHrOo8bzPYn0J5mJ06eTsiSC0kuhkJmIpkZZ8j2F3v46G14foxK0Zkjnrw0N_EMQ54OcnqHYrsLTjdLBep_bl1ADHrYbToFOdZYF7UQ7ooLIhuQANiocO_yfZJHBcCTyqWBQ3sgJe9uhvhNpu3C4uNWn619iIb_SPyBa49cU5ly1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
لقطات من الأقمار الصناعية تظهر ضربة مباشرة على مبنى في قاعدة موفق السلطي الجوية بالأردن حيث وقد دُمر المبنى إضافة إلى تضرر عدة مركبات مجاورة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84346" target="_blank">📅 07:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84345">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84345" target="_blank">📅 06:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84344">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/84344" target="_blank">📅 06:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84343">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/84343" target="_blank">📅 06:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84342">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني: استُهدفت منظومة رادار الإنذار المبكر الأمريكية، ومبنى لتجهيزات وقطع غيار جوية، ومنصة لطائرات مسيرة من طراز MQ9 أمريكية.
أهل الكويت الكرام؛ منذ سنوات، تشغل قوات عسكرية كافرة أمريكية أجزاء من أرضكم الإسلامية، وتستخدمها كقاعدة لقتل المسلمين في إيران والعراق وأفغانستان وفلسطين.
قبل 140 يومًا، بدأت جيوش الأطفال الأمريكية، مستخدمة هذه القواعد، حربًا ضدنا، بدأت بقتل 168 طفلًا في مدرسة ميناب، واستشهاد العلامة الدينية البارز في العصر الحاضر، الإمام الخامنئي (رحمه الله).
يجب ألا تكون أرض الكويت مكانًا آمنًا للجيش الإرهابي الذي هاجم على الأقل عشر دول إسلامية خلال العقود الأخيرة، وقتل ملايين المسلمين. هذا الجيش، بحكم فتاوى علماء جميع المذاهب والفرق الإسلامية، متجاوز لحدود المسلمين، ودمه مباح، وواجب على كل مسلم أن يبيده بكل الوسائل الممكنة، وأن يطهر أراضي المسلمين من وجوده. نتوقع منكم أن تنهضوا بواجبكم الديني، وأن تعيدوا العزة لأراضي المسلمين.
قواتنا الشجاعة في الموج الثاني والعشرين من عملية "نصر 2"، تحت شعار "يارقية (عليها السلام)"، ردًا على التعديات المتكررة الأمريكية على أرض إيران، قامت بهجوم بطائرة مسيرة، ودمرت بالكامل منظومة رادار الإنذار المبكر الأمريكية. كما في هجوم آخر، استهدفت مبنى لتجهيزات وقطع غيار جوية، ومنصة لطائرات مسيرة من طراز MQ9 أمريكية في قاعدة "علي السالم"، وأشعلت فيها عدة طائرات مسيرة.
نتوقع منكم، يا أهل الكويت الكرام والأصيلين، أن تنهضوا بواجبكم الإلهي، وأن لا تسمحوا بأن تكون أرض الكويت منطلقًا للشر والقتل للمسلمين.
"إن تنصروا الله ينصركم ويثبت أقدامكم</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84342" target="_blank">📅 06:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84341">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الخارجية الأمريكي: الولايات المتحدة لا تزال منفتحة على الحل الدبلوماسي في إيران.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84341" target="_blank">📅 06:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84340">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عدوان أمريكي غاشم على مدينة تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84340" target="_blank">📅 05:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84339">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd21cb7cb7.mp4?token=g2ah1606z1nVm6tXdDQTP9SLQ7NnWB9fEBYH4X3a6Y3JO53QMOFQcNA3c-w7WBdLjijsi42Myf2ubbIWFQk9ECc3VIrzuvbxQq-0HBuW2QfrbYT9VnQELcC3wDAc-UNP_NVjA4NCl9Q5Iq-Uufr9zytzjhtYapPgjd3tGd69KyE6Hxln3MkLi39gQ4GRxS4In89St6gXGvnH2W85N7cUZ_BonUrOS0NxfVebbicD0uvKptft8YraAn-_ALxSHGmiLSgTMjvMw-nwfueVAhNa_w_E0R2xt2af0gmd0_WRaHT1ZUe31BEv9CM4SDncqWWGSlkjAP1XgDTBDR2RwJR58g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd21cb7cb7.mp4?token=g2ah1606z1nVm6tXdDQTP9SLQ7NnWB9fEBYH4X3a6Y3JO53QMOFQcNA3c-w7WBdLjijsi42Myf2ubbIWFQk9ECc3VIrzuvbxQq-0HBuW2QfrbYT9VnQELcC3wDAc-UNP_NVjA4NCl9Q5Iq-Uufr9zytzjhtYapPgjd3tGd69KyE6Hxln3MkLi39gQ4GRxS4In89St6gXGvnH2W85N7cUZ_BonUrOS0NxfVebbicD0uvKptft8YraAn-_ALxSHGmiLSgTMjvMw-nwfueVAhNa_w_E0R2xt2af0gmd0_WRaHT1ZUe31BEv9CM4SDncqWWGSlkjAP1XgDTBDR2RwJR58g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي:
تامبا، فلوريدا - أنهت القيادة المركزية الأمريكية (سنتكوم) بنجاح، مساء التاسع عشر من يوليو/تموز، الساعة العاشرة مساءً بتوقيت شرق الولايات المتحدة، الضربات الجوية التاسعة على التوالي ضد إيران.
استهدفت أصول سنتكوم مراكز القيادة العسكرية الإيرانية، ومواقع الدفاع الجوي والمراقبة الساحلية، والقدرات البحرية، ومواقع إطلاق الصواريخ والطائرات المسيّرة، وشبكات الاتصالات، وذلك بهدف تقويض قدرة إيران على مهاجمة السفن التجارية والبحارة المدنيين العابرين لمضيق هرمز.
يُحاسب الجيش الأمريكي إيران بتوجيهات من القائد الأعلى للقوات المسلحة. وتبقى قوات سنتكوم في حالة تأهب قصوى، ومركزة، وقادرة على القتال، وجاهزة للعمليات.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84339" target="_blank">📅 05:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84338">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الخارجية الأمريكي:
الولايات المتحدة لا تزال منفتحة على الحل الدبلوماسي في إيران.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84338" target="_blank">📅 05:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84337">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
الحرس الثوري:
أيها الشعب الأردني الكريم والجنود الأردنيون المخلصون،
نشكركم على تعاونكم الصادق والمعلومات الدقيقة التي ساهمت في استهداف مقاتلي الإسلام وتدمير 20 مبنى تستخدم كمواقع لتمركز قوات الجيش الأمريكي "قاتل الأطفال"، وأدت إلى مقتل العشرات من عناصر الإرهابيين الأمريكيين في منطقة الأزرق.
🔹
مقاتلو قوة الجوفضاء التابعة للحرس الثوري، في الموجة الثانية والعشرين من عملية "النصر 2"، تحت شعار مبارك "يا رقية (س)"، وإهداءً لفتيات الشهيدات في حرب الدفاع عن الوطن الثالثة، وبمساعدتكم، استهدفوا طائرات النقل العسكرية الكبيرة من طراز C17 وطائرات القيادة والتحكم من طراز P8 التابعة للجيش الأمريكي المعتدي في مطار العقبة، وألحقوا أضرارًا جسيمة بعدد منها.
🔹
الجنود الأمريكيون المعتدون، الذين هاجموا أكثر من عشر دول إسلامية على مدى العقود الأخيرة، وقتلوا ملايين المسلمين، وهم الداعم الرئيسي للنظام الصهيوني الدموي في قتل جماعي لشعب غزة وتدمير الضفة الغربية، يعتبرون شرعًا دمًا، وكل مسلم، أينما أمكنه، يجب أن يقتل هؤلاء القتلة الوحشية.
🔹
نشكركم مرة أخرى على جهودكم وتعاونكم الذي يمهد الطريق لتحرير القدس الشريف من خلال أداء واجبكم الشرعي.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84337" target="_blank">📅 05:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84336">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله أكبر
الدفاعات الجوية الإيرانية تتمكن من إستهداف واسقاط مسيرة MQ9 أمريكية في سماء مدينة "إسلام آباد غرب" بمحافظة كرمانشاه الإيرانية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84336" target="_blank">📅 05:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
الحرس الثوري:
في وقت متأخر من الليلة الماضية، انفجرت سفينتان نفطيتان مخالفتا تعليمات، كانتا تحت تأثير وتحريض من قبل الجيش الأمريكي، وكانتا تنويان الدخول والخروج من ممر غير آمن وخطير في جنوب مضيق هرمز. وقد أدت الانفجارات إلى توقفهما عن الحركة.
على الجيش الأمريكي الاستعداد لعمليتنا العقابية بسبب أعماله غير القانونية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84335" target="_blank">📅 04:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عدوان أمريكي جديد على ميناء تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84334" target="_blank">📅 03:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3ed7e945.mp4?token=BTL4rCQ43PPzDdFZGaO_SMjYN-bjC4BAYJGuvTiiKL0uJAVO22DuCxRyd4iN4nvx-bEA9g6jZ6fTHCN6a_cxXv4I55ybJCWSBZ6G6pnKhqOgT5KFdlY01Df0SC_sXHKIA7eIfSkoh598zbcT6F7hVDt25H9rdaS7Vd47HE50aJqc30LvN3tFSo3QmqDkJMm4KMzEthnCIHYfjlaA9Ue-0RvRoCx9u168GYbWEr8dDrgfgbwfTSUOyq1ZJbFiK3yIoZ33VOwl5X9pE-7mzfXIFpPKLhbvPMAq7pM_d5X7o2lk0Xhqo2Zom030qr2YSX9V7SqEeWxKIGxXtHOH1DSewYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3ed7e945.mp4?token=BTL4rCQ43PPzDdFZGaO_SMjYN-bjC4BAYJGuvTiiKL0uJAVO22DuCxRyd4iN4nvx-bEA9g6jZ6fTHCN6a_cxXv4I55ybJCWSBZ6G6pnKhqOgT5KFdlY01Df0SC_sXHKIA7eIfSkoh598zbcT6F7hVDt25H9rdaS7Vd47HE50aJqc30LvN3tFSo3QmqDkJMm4KMzEthnCIHYfjlaA9Ue-0RvRoCx9u168GYbWEr8dDrgfgbwfTSUOyq1ZJbFiK3yIoZ33VOwl5X9pE-7mzfXIFpPKLhbvPMAq7pM_d5X7o2lk0Xhqo2Zom030qr2YSX9V7SqEeWxKIGxXtHOH1DSewYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب:
سنضرب إيران بقوة هذه الليلة.
إيران ربما لديها بعض الصوايخ والطائرات المسيرة لكنها ليست كثيرة.
لم نعد نكتفي بمنع الإيرانيين من حيازة قدرات معينة بل نقوم الآن بإنهاء هذا الأمر تماما.
نوجه الضربات لإيران وسنرى ما سيحدث.
كنا نعتقد أن شخصين [من القوات العسكرية الأمريكية] قُتلا في الهجمات الإيرانية، لكن كان هناك ثلاثة أشخاص.
نُسيطر على مضيق هرمز وإيران لا تسيطر على أي شيء.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/84333" target="_blank">📅 03:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84332">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d18382358.mp4?token=c05jYzlzsEICa5Se0ySQh8atTruxCbFc0xmn23E18dnbO2oqtVSIbTc6-w03e_v10Yl5cUKfFr1IbCLTqAYblAP8SP7A3s9hC2PtOlLKByNZehotQAYhg3j6i-_lEiirrqdKfIcxJstZIJQnvqnwuSjCe9WFmvZt6wVQPSwuxC5Z7rHWujsoNEMIyj6S1yf-dG3VAoCQjcJMszXJx4tZjF-PQ9DzidAIeJeyCmUFIzzHks9rMGUxOQTOoSH2dzTMsKrn9Wh0oXFpxssHs5Vdq1bIvCdOmquUkRP4tNJuFbQvMn3RlWMOjEkpOt5SI4Se6pZmfnklwOa-atw8ccV9xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d18382358.mp4?token=c05jYzlzsEICa5Se0ySQh8atTruxCbFc0xmn23E18dnbO2oqtVSIbTc6-w03e_v10Yl5cUKfFr1IbCLTqAYblAP8SP7A3s9hC2PtOlLKByNZehotQAYhg3j6i-_lEiirrqdKfIcxJstZIJQnvqnwuSjCe9WFmvZt6wVQPSwuxC5Z7rHWujsoNEMIyj6S1yf-dG3VAoCQjcJMszXJx4tZjF-PQ9DzidAIeJeyCmUFIzzHks9rMGUxOQTOoSH2dzTMsKrn9Wh0oXFpxssHs5Vdq1bIvCdOmquUkRP4tNJuFbQvMn3RlWMOjEkpOt5SI4Se6pZmfnklwOa-atw8ccV9xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي على مدينة ماهشهر</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84332" target="_blank">📅 03:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84331">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الله أكبر
🇬🇧
الجيش البريطاني:
اندلاع حريق على متن سفينة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84331" target="_blank">📅 03:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84330">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عدوان على مدينة خورموج وميناء سيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84330" target="_blank">📅 03:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84329">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇱
دوي صافرات الانذار في مستوطنات غلاف غزة والعدو يزعم أنها بسبب تشخيص خاطئ.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84329" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84328">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1682925309.mp4?token=tO3S1SONWcQYYP11Yw5ReoiDnEVkmTTzJUyn-dp5q6luWyXP3oYlip7KfbuCP_0V4y5sSzWnFSiv75JK-8wrBw1gdx6_1daf58yb_sfxAQdowbczIkg5OPjIpeoHkM2wYSFsWXlNk41ErtIJZ6nAHS9kEFy3J6a8z8fU5__CLaJqzNsh_SZpSeZssXXd5BCjn49OCzq2khf4YH2fee4kSdDV727rSuBFmzTWlcYkQ6Q8vb6ObtP5YwaCkdVZKiVMBNarHpxMAuOalzNUL_cIa2pE-2aQToL4_AYs8YObo1VyI40b_U6t7_meirrFwisxnmnHYEq0CDIGWCJd2Wzinw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1682925309.mp4?token=tO3S1SONWcQYYP11Yw5ReoiDnEVkmTTzJUyn-dp5q6luWyXP3oYlip7KfbuCP_0V4y5sSzWnFSiv75JK-8wrBw1gdx6_1daf58yb_sfxAQdowbczIkg5OPjIpeoHkM2wYSFsWXlNk41ErtIJZ6nAHS9kEFy3J6a8z8fU5__CLaJqzNsh_SZpSeZssXXd5BCjn49OCzq2khf4YH2fee4kSdDV727rSuBFmzTWlcYkQ6Q8vb6ObtP5YwaCkdVZKiVMBNarHpxMAuOalzNUL_cIa2pE-2aQToL4_AYs8YObo1VyI40b_U6t7_meirrFwisxnmnHYEq0CDIGWCJd2Wzinw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في غرب وجنوب شرق إيران.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/84328" target="_blank">📅 03:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84327">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عدوان على مدينة خورموج وميناء سيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84327" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84326">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84326" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84325">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/84325" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84324">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0ckfWy4W7PALiRJfqMeINdgSA8RfiijImXJdQoxYvtYxqskGVfqv0rULO2N3eQU0oGZWih8tKlyuClUg7j23_8SA3rVkNqHgrZYLQYRUYUQwd7d5Ra3A3aXA30IFkGAl5f7YS88hSQcheKfmgaybgUmIihFAHibXebMarrR7Gb7C6fnkQqBkr_Y3se6GcJdUnDWoQoSYJPf87nscuDEBg1IPfN-JTZ-eVpoKNxwYbQIuFoYjpq0q4QGGgdHl2V-Oo3NooialADBBaPcgQpEyPi321LdctFb4vFCfTnRcjm-8_op8rKZG6YZHzgOXSj7ue5JwvJTA_p01KqC7UX0Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث أمني قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/84324" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84323">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حدث أمني قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84323" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84322">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETX8uGJS6np3pHoMgSlTTk2IBndIq4iLkhuZ3tI36nBO8oze05eKH4Jq9PiS84fdN4SzwM5kTZ0TCFrd9_phDzKo-cBDTpQQWY0fO_JlJF9V-uVVLWivIGUkkEztEOsosiI051SdXHESKUxMH0hkoscYg18v1Dpn6Y2hUTsKQQIMIPiQEHyrYDZBVgwelsbQuR8Cs1tYyqk1eFoWEvra3waSnBIT9JRvW2wsCNcjhQ8-vfnjh1MAvvxEtAaLn2ykOilmsb_OuIvqJKgOQ-OESC0D5ayTg-JCu83JuP7TQ-w1k3fLV1ifbkEcVJHXXrhxwr5_wFVZikTAmPaK1faaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من العدوان الأمريكي الغاشم على مدينتي ماهشهر وسربندر (ميناء الإمام خميني) جنوبي إيران.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84322" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84321">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
🇧🇭
‏
السفارة الأمريكية في المنامة بالبحرين:
لدى السفارة معلومات تشير إلى أن إيران قد تسعى لاستهداف مواقع غير محددة في وسط المنامة.
نحث جميع الأمريكيين على توخي الحذر، واتباع تعليمات السلطات المحلية، ومراجعة أحدث التوجيهات.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84321" target="_blank">📅 03:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84320">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله أكبر
إنفجارات عنيفة في رأس الخيمة الإماراتية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84320" target="_blank">📅 03:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84318">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5b8b6ad4.mp4?token=bl27hH9l7fPRczPCgC7znm29neKM7XC2XVDoNzBpYgAwijHmVNEAb8kXYIJhRrdDVoMBR-Vxjz46a71vzKyACQS6yF_AfKvwS56Hx9yBpbjtHB_CGg5ClCKPafiOr8KyJ6E0ei6BkthQYxLIPrPbmO8hRrnl1oCrQV45SWz1Ou7r6B7NZnJPWI0n_DI5Yh48BR6bxsClYJD6GORcjzWFaOAyCERcxXEhHKhz1XrQqe5LJL-7k5yvJ1lXv9-lrdjenMzHx0UXpFgod93R_OEs9hAGT17YbSWKtHHylXmJdjdVUZKm3olwW4Mty_RLpUT4jeo98xS1lyHkBI4ZF8_Xow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5b8b6ad4.mp4?token=bl27hH9l7fPRczPCgC7znm29neKM7XC2XVDoNzBpYgAwijHmVNEAb8kXYIJhRrdDVoMBR-Vxjz46a71vzKyACQS6yF_AfKvwS56Hx9yBpbjtHB_CGg5ClCKPafiOr8KyJ6E0ei6BkthQYxLIPrPbmO8hRrnl1oCrQV45SWz1Ou7r6B7NZnJPWI0n_DI5Yh48BR6bxsClYJD6GORcjzWFaOAyCERcxXEhHKhz1XrQqe5LJL-7k5yvJ1lXv9-lrdjenMzHx0UXpFgod93R_OEs9hAGT17YbSWKtHHylXmJdjdVUZKm3olwW4Mty_RLpUT4jeo98xS1lyHkBI4ZF8_Xow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي جديد على مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84318" target="_blank">📅 03:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84317">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">عدوان أمريكي جديد على مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84317" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84316">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4322d49914.mp4?token=PM5T7SGQuz0rZnoBKHobbRcA5HZOQQh1Vzkw5sWZsdJ28j9P4ujuqC9_uSzL21UGlKPRScgfu1-eslxnWbAvVnlZoQR6XaRn0eDl6AAg3snKcrhVMJYLWcS4WrTkSbMQPRzaRiG38ir67Gaifl0D7IYw_1dV3XKGyiwyel_H3pYA7q0Fm3fCfrXwRcSuDaVQcOlmQFp2bTmLoyyU1FrbIBSeMCgsJwW14PeQe4dJY3YaqP1YY2CnjTAKZ9SgUllNgA2LDnVb2BihoukX3vJG1Lx-tK1aocceVQSEw1kwvhf7zfYZCQP959JT5QeY-V-ryT6Rjzb7qkV693cM9NuTPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4322d49914.mp4?token=PM5T7SGQuz0rZnoBKHobbRcA5HZOQQh1Vzkw5sWZsdJ28j9P4ujuqC9_uSzL21UGlKPRScgfu1-eslxnWbAvVnlZoQR6XaRn0eDl6AAg3snKcrhVMJYLWcS4WrTkSbMQPRzaRiG38ir67Gaifl0D7IYw_1dV3XKGyiwyel_H3pYA7q0Fm3fCfrXwRcSuDaVQcOlmQFp2bTmLoyyU1FrbIBSeMCgsJwW14PeQe4dJY3YaqP1YY2CnjTAKZ9SgUllNgA2LDnVb2BihoukX3vJG1Lx-tK1aocceVQSEw1kwvhf7zfYZCQP959JT5QeY-V-ryT6Rjzb7qkV693cM9NuTPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي على تبريز شمال غرب إيران.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84316" target="_blank">📅 03:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84315">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=n0wJAhcyqA_ehB_yr4A1KyiL0__CwznByECrfQWYvVL1fZfEsgNAl5US2xG-vnT-y23Bn8nIr9cHyMuG9n0vXIqiPbuULIBkaqUhQZQsk5_q1hqegZw94GngXCwOr-ifHWMC9_H30pu0xBxBI0dNS_P9YyleNnFuNTW90jkg4x5dJA2sVDvy08q3RtdGb2ipI1drsxEgJ07kJGUxSdgrxLiOJvH-yxCtgLHwOW9fdwbbf97Ns7QvVDEn1XHoFXx9pIWZseeS32SEqk0cTFmFL1dmce51JpY2ah85qfCCgybnRDu85KBG67q8EyxF9B8Bm-ECgbDg1qNgA6ekr8h6lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=n0wJAhcyqA_ehB_yr4A1KyiL0__CwznByECrfQWYvVL1fZfEsgNAl5US2xG-vnT-y23Bn8nIr9cHyMuG9n0vXIqiPbuULIBkaqUhQZQsk5_q1hqegZw94GngXCwOr-ifHWMC9_H30pu0xBxBI0dNS_P9YyleNnFuNTW90jkg4x5dJA2sVDvy08q3RtdGb2ipI1drsxEgJ07kJGUxSdgrxLiOJvH-yxCtgLHwOW9fdwbbf97Ns7QvVDEn1XHoFXx9pIWZseeS32SEqk0cTFmFL1dmce51JpY2ah85qfCCgybnRDu85KBG67q8EyxF9B8Bm-ECgbDg1qNgA6ekr8h6lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من الكويت تجاه إيران الإسلامية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84315" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84314">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله أكبر
🇮🇷
الدفاعات الجوية الإيرانية تتمكن من إستهداف وإسقاط مسيرة أمريكية جنوبي إيران.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84314" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84313">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9cfa9c17.mp4?token=bad6KLFIWH3Mt_oiv97X7MvoHeSGLqHYKaKH0j0uQccLvuWqYUATR0eDdSya9qjPbgr5M_Sbz9snzI2AvS6GsjewA-X5h5OfbmsysKh7Rg6DY-aw13XJlogfV3IaIji4ERAvrb5j5JsEPnxDK509fXcCwm6tWsKRxmfw7dv7xLRbjqZ2fsxp0QVdPnFJ9QFh8VtzQdzd2h3_0QYs_UldtbEZ7W3oJLSieLIHklVQwS8L6nN-Ge3hPaBzDAiRQ-X7ELCjMcGhNaM20ISC-unGCgGLqYpwMMP-pBHd7bLWNk4TaXYGAfXnJtT49ElGQhnZ94_dk5DkOzzSY-FLNbNYAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9cfa9c17.mp4?token=bad6KLFIWH3Mt_oiv97X7MvoHeSGLqHYKaKH0j0uQccLvuWqYUATR0eDdSya9qjPbgr5M_Sbz9snzI2AvS6GsjewA-X5h5OfbmsysKh7Rg6DY-aw13XJlogfV3IaIji4ERAvrb5j5JsEPnxDK509fXcCwm6tWsKRxmfw7dv7xLRbjqZ2fsxp0QVdPnFJ9QFh8VtzQdzd2h3_0QYs_UldtbEZ7W3oJLSieLIHklVQwS8L6nN-Ge3hPaBzDAiRQ-X7ELCjMcGhNaM20ISC-unGCgGLqYpwMMP-pBHd7bLWNk4TaXYGAfXnJtT49ElGQhnZ94_dk5DkOzzSY-FLNbNYAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجار في مدينة تبريز الإيرانية</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/84313" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84312">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e07ac69b1.mp4?token=X2QaI7n5A9E28ykOG61r1v5o59iClB1azO8aj01nTLaGBXa1vYplON2aoO4bX0WdagknVjIjYhUl8Cea-TsqP3Pvac5Gm-SP4x-u0_5P7ajMu8suVM12-BmIWjF_5QAYYyPjZ8hZZeMK_ivC4Lt-NfCqokWeI2FuojsjKhosEsgDc3u4x56tE2tf1a1Oc78uLU3FgZspGnQydib3PnKfcC7-cZcIu82QT4qihyk_SJfWW3NIE0dn5NqDDAOH2IND1LSC6c9c-ILy7bnicAWyHHyiu0H4kW-lbWybGOFQQsYMC7cnOJz3_mwiWNiOXy6df3m15BlgPVe3soC_Mz6q7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e07ac69b1.mp4?token=X2QaI7n5A9E28ykOG61r1v5o59iClB1azO8aj01nTLaGBXa1vYplON2aoO4bX0WdagknVjIjYhUl8Cea-TsqP3Pvac5Gm-SP4x-u0_5P7ajMu8suVM12-BmIWjF_5QAYYyPjZ8hZZeMK_ivC4Lt-NfCqokWeI2FuojsjKhosEsgDc3u4x56tE2tf1a1Oc78uLU3FgZspGnQydib3PnKfcC7-cZcIu82QT4qihyk_SJfWW3NIE0dn5NqDDAOH2IND1LSC6c9c-ILy7bnicAWyHHyiu0H4kW-lbWybGOFQQsYMC7cnOJz3_mwiWNiOXy6df3m15BlgPVe3soC_Mz6q7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف يدك مقرات المعارضة الكردية الإرهابية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/84312" target="_blank">📅 02:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84311">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارات في غرب وجنوب شرق إيران.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84311" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84310">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارات تهز الكويت مجددا</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84310" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84309">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات في غرب وجنوب شرق إيران.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84309" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84308">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الجيش الأمريكي: ‏
بدأت القيادة المركزية الأمريكية (سنتكوم) اليوم، في تمام الساعة السابعة مساءً بتوقيت شرق الولايات المتحدة، موجة جديدة من الضربات الجوية ضد إيران، وذلك لليلة التاسعة على التوالي. وستواصل هذه الضربات تقويض القدرات العسكرية الإيرانية التي تستخدمها إيران لمهاجمة السفن التجارية والبحارة المدنيين العابرين لمضيق هرمز.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/84308" target="_blank">📅 02:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84307">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عدوان أمريكي على مدينتي ماهشهر وميناء إمام خميني جنوبي إيران</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/84307" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b4cafb2c.mp4?token=Ca0FECqLPLuCKvfMRM3Yny8npgebTwXHk7KVCNqr2DpFqDArNgxdQXVDVEQxJNM9ZxhII3_esX5mRiEjkpBgqoq7nrVi_Il8fYqqFVyaas5Jf240W3zBqn2HFKSllJKGo0y5doeJ8W2_f9EbQxpxqS5QLmBDtebEpbusLeTwV_1uFNMUzaKmDdRInZhDABEOPgqHKFkLVMu47r513_oYXUkk3EYJUKKpiYW-yf6b5NOshx3kZs9kYrDJfp9SioAICuunqi7UPRs9okn1mW1PxqwbxEh1TasEHx8FHS29rVoHGUeyBKuBungsAbj4_TrMn17rOlzjeK-IDtRVfqm0fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b4cafb2c.mp4?token=Ca0FECqLPLuCKvfMRM3Yny8npgebTwXHk7KVCNqr2DpFqDArNgxdQXVDVEQxJNM9ZxhII3_esX5mRiEjkpBgqoq7nrVi_Il8fYqqFVyaas5Jf240W3zBqn2HFKSllJKGo0y5doeJ8W2_f9EbQxpxqS5QLmBDtebEpbusLeTwV_1uFNMUzaKmDdRInZhDABEOPgqHKFkLVMu47r513_oYXUkk3EYJUKKpiYW-yf6b5NOshx3kZs9kYrDJfp9SioAICuunqi7UPRs9okn1mW1PxqwbxEh1TasEHx8FHS29rVoHGUeyBKuBungsAbj4_TrMn17rOlzjeK-IDtRVfqm0fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف يدك مقرات المعارضة الكردية الإرهابية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/84306" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07d9dc9b9.mp4?token=cMwyKcVEtM_-RorQXi1anniFNpBMNL87r00kAbi92ay-aLmPF3UqfAK8BLbDZFaMy2a2N1iT7xaJmhe0kiHWSOJb3Uv1pWVmDZ9bx_iEP5S5QFcF-iyIGoRhwsz-yXBrh09-a201arWIsILCfArpYSQEKbOFoLFORa4h3xdFzDevzKxJQkU3bsfboeP0CU9GBnXvj4mnmMoRic1Aj1dkRDxFidMs4lGATx7CYmzJeGWB3AjTcdKj8F79dTMTLj_1eX2o3wpW2f1arn-TMfgSdzX_CLewMETfYAA6LDC05ZyvzLI-2oSaCxhGtH1QvQJL1mugDW9UyMhCJWnOxuUZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07d9dc9b9.mp4?token=cMwyKcVEtM_-RorQXi1anniFNpBMNL87r00kAbi92ay-aLmPF3UqfAK8BLbDZFaMy2a2N1iT7xaJmhe0kiHWSOJb3Uv1pWVmDZ9bx_iEP5S5QFcF-iyIGoRhwsz-yXBrh09-a201arWIsILCfArpYSQEKbOFoLFORa4h3xdFzDevzKxJQkU3bsfboeP0CU9GBnXvj4mnmMoRic1Aj1dkRDxFidMs4lGATx7CYmzJeGWB3AjTcdKj8F79dTMTLj_1eX2o3wpW2f1arn-TMfgSdzX_CLewMETfYAA6LDC05ZyvzLI-2oSaCxhGtH1QvQJL1mugDW9UyMhCJWnOxuUZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجار في مدينة تبريز الإيرانية</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84305" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84304">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4Su2avF8Lio5AcFBeofBe2DcMGvSyu6ErVCJeT2giUWF-QBi-EA3_QwUTA1ox06D5WPXeuZaPDVtHmKFLx8xjCjmJUCS0BBLDs7nG57GTvM7wwzNwMCKgON5eun5xsKvqIhx0sO611H1NMzBUPE0m4uB9Emrjd8gt5nRFGhppw6g82xtgo8T3ch_9Nh9YQScxJ9cGWys09V1jSWUTcf79TqGXL2wpZpIWE7ZUprNAVX7IS7UrQ7so5W_a1CiegRBzL8G0-AO3IbVACL6sKimsT0orehnFas5eobm92pxDIYeYlBVdodpC-kJ2j-i_9GVHc9bGcD-XOuDrwPLlSAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا عزاء لنتنياهو و ترامب... إسبانيا تتغلب على الأرجنتين</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/84304" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/84303" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84302">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دوي انفجارات قوية في الكويت</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/84302" target="_blank">📅 01:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوي انفجارات قوية في الكويت</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/84301" target="_blank">📅 01:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc48fae07a.mp4?token=ggKR5jz6562Kvr3mCX2FRgqOPQsVJOtgIn34plK9NDu8HIOE3UgROk7bhNyYO1tW4mc7HKxVg8Wnc4l4U8VGdS4_-68qVQYXY963aMeYDAZAxkk_XIv2vOxJhDVhkwXstvXRxIRr3t7kQeZeX8kXxOvk5bHKmTJeg6WIiihA54BnVmmbPokZGIxQiDj7BEsyhMSJkBMgVazDGjul0WhN45xLtc2bRw7dFc6tSt5TbGLkR1tMwQt9q5vnjEFSAMhYQXD5fZHd7FSmclpaFSJ1uHa4OgQzmdDGAsrdD2Do6CxmSDzZ-F8OMvn4ml4VhoyzlqBnGnxkt49XtkOsY8MQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc48fae07a.mp4?token=ggKR5jz6562Kvr3mCX2FRgqOPQsVJOtgIn34plK9NDu8HIOE3UgROk7bhNyYO1tW4mc7HKxVg8Wnc4l4U8VGdS4_-68qVQYXY963aMeYDAZAxkk_XIv2vOxJhDVhkwXstvXRxIRr3t7kQeZeX8kXxOvk5bHKmTJeg6WIiihA54BnVmmbPokZGIxQiDj7BEsyhMSJkBMgVazDGjul0WhN45xLtc2bRw7dFc6tSt5TbGLkR1tMwQt9q5vnjEFSAMhYQXD5fZHd7FSmclpaFSJ1uHa4OgQzmdDGAsrdD2Do6CxmSDzZ-F8OMvn4ml4VhoyzlqBnGnxkt49XtkOsY8MQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لا عزاء لنتنياهو و ترامب... إسبانيا تتغلب على الأرجنتين</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/84300" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

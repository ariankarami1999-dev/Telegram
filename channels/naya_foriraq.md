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
<img src="https://cdn4.telesco.pe/file/FKHlvjEDVU9q_fLGcjHvfUGNv90uwNr6RfMxM3Q46hT6ZoQq3ofAdA_kX23C_fGzPnIaxR57Ov-Kw-vaZnNQxtr5bd92n2QNUvx6E3kG6bkPhx1mMnlXLj1zUoXJiK9fPUjr_hdqVP4WYAGI7hUokHnDZzvQGzY2lai8gijiJlwIgsXIJBu7o0kMr3jaZh1XAj4TWrgBeOy8CBAGKnXpQKxRx0N850HO5YEcjktrpkwZ9yrZh4lWRDzj1L1nFE8xR3F2f9ZHQUjwplRMlS3PZV1hn-TfeHc2FzsKJBcDc4aVou2a26ct-y5iH0PE2fzyXlER9v5vnuEahbUdgPsvZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 09:43:41</div>
<hr>

<div class="tg-post" id="msg-83582">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/naya_foriraq/83582" target="_blank">📅 09:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بكين وباكستان تدعوان إلى وقف إطلاق النار واستئناف المحادثات بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/naya_foriraq/83581" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">استهداف رادار أمريكي في سلطنة عمان</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/naya_foriraq/83580" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/naya_foriraq/83579" target="_blank">📅 09:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URWjItrk5Ks5n7xyvrB7n-f5GooEkqlpQ0BzlLHGkGozY7Qk-0VBfJDz8mhXxJKnFl_ERW-KfVW_ahTKgqAm9pAt2yzXefnRB9tCwmtutxIOoSAyCmI4BnCgd9et0qtjgn4rJ7efd43xxcQD9hCG-TYjmR8ZJeRDNboXcu0opsb2RXZvPdfHjX1QVpnHn8op_s80f1qDnxE2b2d1pNKpF-WrCrAPkcSDaThqgO3PxwUDD6zWVsgOtI-x4A373Vm2n2vRX2t-l03ti5HN4ZAYGtdpD_PGrh5Piy32vRa35HZYFcjSz5o2hICirpEUF0tnHsFMjx0NNMS3WiBOIvOQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
🇦🇪
بالتزامن مع تبادل الضربات
الإمارات ليست برئية ، حيث أظهرت بيانات تتبع الطيران تحليق طائرة تزويد بالوقود جواً من طراز Boeing KC-135R Stratotanker تابعة للقوات الجوية الأمريكية فوق منطقة الخليج الفارسي ، بالقرب من سواحل الإمارات .</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/naya_foriraq/83578" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83576">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a186bf2799.mp4?token=nE_9O7G8Hg-rQM21npF3DPbz10PXEU4hANRcV1pD9OXHWJrCzqCiWqiTqPDdUI7L9I7i68KLamvw4enHVJZ3PtH0NfotOL4iwZLP2lbpRD5Q3u8UVT42VKU4rHHFz7Awv0THJ6-bc4bkrTPtP7Fr-K-fm_f37YeowD_u6fDFoO4jjMAL_s9GaioI_3Y8JX0RLPI6g_cQSdzA1LcuoRegTkis8TK5Lo5vxeDWKBlQ52nATIQc5Z5HddrqIr9al4oQ7-_Lo9buZ1XdTBrAToT_fSqhLjYsGm91M-VdautkT3uX-DdlqVZdwbkLVkG9I5JFQJMYuQRz5XiyBKMsT7dsvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a186bf2799.mp4?token=nE_9O7G8Hg-rQM21npF3DPbz10PXEU4hANRcV1pD9OXHWJrCzqCiWqiTqPDdUI7L9I7i68KLamvw4enHVJZ3PtH0NfotOL4iwZLP2lbpRD5Q3u8UVT42VKU4rHHFz7Awv0THJ6-bc4bkrTPtP7Fr-K-fm_f37YeowD_u6fDFoO4jjMAL_s9GaioI_3Y8JX0RLPI6g_cQSdzA1LcuoRegTkis8TK5Lo5vxeDWKBlQ52nATIQc5Z5HddrqIr9al4oQ7-_Lo9buZ1XdTBrAToT_fSqhLjYsGm91M-VdautkT3uX-DdlqVZdwbkLVkG9I5JFQJMYuQRz5XiyBKMsT7dsvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/83576" target="_blank">📅 08:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83575">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUN_7ALzk8ppSYc0004XmHXeM4SUru26FDBM8JlbI_AaiAnAsBFItu5gSFEvn80ZPdYRiTZb7BNG36sm9smvUm0_ckW0vPeu_gXdQA8xN4EnUoORk4Sxv7FBaH6iZt8-pzsO6ov08qxgkFDdMIBjOKiptkIbI4u22u7MZ26S6jdrZmvysksjWz_MuigESZ8mS_WTUyM5VXsuHRAiXCJdBIscutZnycHBUHKhhkiiXWBsZ-a6OG0n75J-SZtNQn8MPKK4e3_kHngFY1hkSnTrnNqz8scvHZbtMmzapP30wzlSUdvgDgvc3v4admgKKPW7jnybthabVRJFca1K3tNzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خون ریختن
خون بریزید
خون در برابر خون
پل در برابر پل
برق دربرابر برق
برج در برابر برج</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/83575" target="_blank">📅 07:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83574">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  ردًا على جرائم جيش الأطفال الأمريكي، قام مقاتلو القوة الجوية والفضائية التابعة لحرس الثورة الإسلامية، في الموجة الحادية عشرة من عملية "النصر 2"، تحت شعار مبارك "يا أبا عبد الحسين (ع)"، وإهداءً لشهداء مدينة بمبور في إيرانشهر، بهجوم مفاجئ على…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/83574" target="_blank">📅 07:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83573">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/naya_foriraq/83573" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83572">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/naya_foriraq/83572" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
ردًا على جرائم جيش الأطفال الأمريكي، قام مقاتلو القوة الجوية والفضائية التابعة لحرس الثورة الإسلامية، في الموجة الحادية عشرة من عملية "النصر 2"، تحت شعار مبارك "يا أبا عبد الحسين (ع)"، وإهداءً لشهداء مدينة بمبور في إيرانشهر، بهجوم مفاجئ على مركز قيادة العمليات الخاصة للعدو في منطقة التنف السورية. بالإضافة إلى تدمير نظام راداري، تم تدمير عدة طائرات هليكوبتر خاصة تستخدم في العمليات الخاصة، وفي انتقام لدم الشهداء الذين سقطوا الليلة الماضية في إيرانشهر، تم القضاء على عدد كبير من القوات الأمريكية المجرمة.
لا يزال السيطرة الكاملة على مضيق هرمز في قبضة مقاتلينا الشجعان، ولن يتم تصدير قطرة واحدة من النفط أو الغاز من هذه المنطقة طالما استمرت جرائم أمريكا.</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/83571" target="_blank">📅 07:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veRXBs0YWIxcPhAYJUOa8p95ClvMlB4ht8gt_uXD0mvMLKSXzn3mzTe__Sn3la8S_sTSDKeNk9qH-M1sdTkVcKym1Y4U7uubI8YoOQiPpxwCUsKj-7pyuf0zNUvKg36F1V7XnApQB3AiVlXf3xPiSZV15SvLUAA9Ny3nIhBuJFFtQQuBvRpbyRQzFBK2PkE2VRokND3BDXxsmMWxxJ8fYmc9BrvmUqw1PvFOKiW05YtMDRfHa8mvMOgxkZZifwk4K3MJfAjLwa34Xeet5MhM435oVmyyKw9SYX3Mtz_yEgZSY_Nz7n1sByXeIg2rM4xpY8QSMnH9hb6rOK8TdpFHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشر وزير الدفاع الأميركي لقطة لاستهداف برج مراقبة في تشاهبار</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/83570" target="_blank">📅 07:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات عنيفة تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83569" target="_blank">📅 06:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات البحرين مجددا</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83568" target="_blank">📅 06:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هجوم جديد على قطر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/83567" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/83566" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/83565" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سماع دوي انفجار مجهول في العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/83564" target="_blank">📅 06:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-LMUysa1TjaTm3vZ4OtBvP-HmZhtkvhnNRPdu6KrvtAuwZa1gwVWqqrCOvOtx-efE8GLbDZ9HXlF6mRDwRvCuU3g67bdvhY2MpYDno_2yyOrZg5_OZc6kIVOe4n2pnPVfm5-c4axBD3PK-5mNBDbVks4jHefbcBQK-Rb2QjdB6hG21Gp6PbRtKyAKFWChUEV84ElpNYf6BC3dB6cRENPCqAXZ7orwAhL2Oj4mf6FwMLOEITQ0ODLE65zWVgtKj2kYL5uhJzwp2O5qtRYuKZCruBCcUnFvu-L54c9qP2pcwOghj8j6Mc9NdCG4hOK8H-XsXUYim9o35huePsFQnqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مروحي أمريكي  من نوع اباتشي يجوب سماء البحرين في محاولة لإعتراض الطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/83563" target="_blank">📅 06:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc0nE1nbGnJBk_P2ideO0rvgjsOR_2TX8rzMtQqH5ieqc3uLIyBID7976-_lxdC0Xs86OCNXsNSh0Uo0cXHdgD1TloW0-eK-O1tMhSUa8U11ojGD9VVr0tVI0MJe_zfUl45lsTLRPvDYbO4rBLZCneJsCS3xUaIlEgixjEnBGAwSzhg4trKKCJAJnwqJ7B04xFFbmm0UZCFDju9F2fAc3K9cf3ZlKjxPzw06Xj9vA2xnduhjztDOSPjmAuI7B9vhmB2d8ws2JM7rko36huFhnRn-IA-YxE3PcZ7pU2TkBjyxcqYoyjXCVtueN9g0cJ7GGGpDbtWffKfrZCaV2x1LIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مروحي أمريكي  من نوع اباتشي يجوب سماء البحرين في محاولة لإعتراض الطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/83562" target="_blank">📅 06:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTDYh6qaGynJ8mq8i5KCrqXsAZpRRKhQ9BkNq35dTmL2SH2kBkcc6iQUGL4pRT985nuLtBLyuijyutVh6aPeQxqy-Qw2tpoMiuN6wMnBb_vY8FQOsWjM-lA9_1tGtp1v7cVvVP4OynksHYbne6h8FOzUXSoWO3VzM2tk7UrliqEpCyp6wwe60x31z-b27CNIxL0wWizR6ZdOkXRimSzT3TAzHjo5Qiue_48Keq1Z5wOoCGZCmhPFhHVJ3-0o_WpL-QjyEGME04O6Bo_lj_1-7NWPt0tM8PmYGzZ38fSXJUD7z4zcXHxzjmPZcVX5L3C3uLLIlIEPPvZMDtci0DdP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات البحرين</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/83561" target="_blank">📅 06:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8733970ed8.mp4?token=mqZlYwWj53FQbpzRkItCq04ds-90K3EIqeuLf57R5aAHu8XnW0RwiRkwoo-9OcmZR10iaiGi1FMQVSl0OmQsY1yI8QYLUHXHmNEAkTktEest-L_MiJ6L9g37pqe20Hs0BDkU3Joj1wWwUwA9zR5GFH7tZM4L_R2BeTROCyDUdQhQUmuyAlNE1NkWFkyy7gOBonx3YZs8y6qNQX0qsewdnfAo7xaY4cRlKsd6kqKQHLaLltznEJ3M0ExD5rp8Dfxr39aklrwEqdI3XX7Fnnh510GSyS6JrZlpPCqHIhZgqLj0KqLoLodffzRtqXRH5KgBKnBaN1IiwU7dJRlUzLWa9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8733970ed8.mp4?token=mqZlYwWj53FQbpzRkItCq04ds-90K3EIqeuLf57R5aAHu8XnW0RwiRkwoo-9OcmZR10iaiGi1FMQVSl0OmQsY1yI8QYLUHXHmNEAkTktEest-L_MiJ6L9g37pqe20Hs0BDkU3Joj1wWwUwA9zR5GFH7tZM4L_R2BeTROCyDUdQhQUmuyAlNE1NkWFkyy7gOBonx3YZs8y6qNQX0qsewdnfAo7xaY4cRlKsd6kqKQHLaLltznEJ3M0ExD5rp8Dfxr39aklrwEqdI3XX7Fnnh510GSyS6JrZlpPCqHIhZgqLj0KqLoLodffzRtqXRH5KgBKnBaN1IiwU7dJRlUzLWa9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مروحي أمريكي  من نوع اباتشي يجوب سماء البحرين في محاولة لإعتراض الطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/83560" target="_blank">📅 06:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353f3a3410.mp4?token=hYdOjS20GKBC2ZIYbYNZPnp-6NLMBYfA4-HJ0vfN26bcruUPmPXCA2e-nWNX0YkYW0s1hnO3cTWJC5ASDpipjP4mepEqDVvrfiEMb-r08vWV_jDhEDGTXkGhoziTCTm7ySMPyGbGoXSlSyF5WxSOnE24vn7BCyX-otk3MsCRVZB8DV9mo116h-jIpUPmGGLpljhYO-lKUIiFz4le7BMXz8jQo9SQOSl97wJpwJFMv7wfPUPCtUfBQHseqbDMFEzeYF46K8a3IthsLhgt_XCxva2WuTjbcXZzaJ3zsqHwPEtz_gpkSlMHpRfFmZ0VaOUGKvzh3YenmEnrrGGo_CTXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353f3a3410.mp4?token=hYdOjS20GKBC2ZIYbYNZPnp-6NLMBYfA4-HJ0vfN26bcruUPmPXCA2e-nWNX0YkYW0s1hnO3cTWJC5ASDpipjP4mepEqDVvrfiEMb-r08vWV_jDhEDGTXkGhoziTCTm7ySMPyGbGoXSlSyF5WxSOnE24vn7BCyX-otk3MsCRVZB8DV9mo116h-jIpUPmGGLpljhYO-lKUIiFz4le7BMXz8jQo9SQOSl97wJpwJFMv7wfPUPCtUfBQHseqbDMFEzeYF46K8a3IthsLhgt_XCxva2WuTjbcXZzaJ3zsqHwPEtz_gpkSlMHpRfFmZ0VaOUGKvzh3YenmEnrrGGo_CTXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
هجمات بطائرات مسيرة تابعة للجيش على مراكز دعم الجيش الأمريكي الإجرامي في الكويت.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/83559" target="_blank">📅 06:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83558">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a39b1f78.mp4?token=qB7ieZ9JoWNNJ7KJh80Jp-OmAkA4LZCKRwIF4Un8Z8NcIfpkQhmmfRA7uSff39AAGEfm10HcudSHH1NNjC7BxD3APPu-Mh22DQOZpb5km8XnNQWfLfe-drkLoRwjSMJB1AzAJ3zriI-eHPOmPt6yrdpW0W_T7m5NIEC3io0qtK-3KBg7lF11eZLqaz-IfQUPRcpn7Cks0M8dWfswx-73mLhtdcSalHfW9Gtg6BnlP_XI0YGDBG-3qQ3v_qGPfro5yPePq8oz-jTmbfPpieqvwxzjCUYoBFDLiYm0w22TBp_XNkXDGhH-4qk0n46JkpFeyT4q7cCape0a-926F78PDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a39b1f78.mp4?token=qB7ieZ9JoWNNJ7KJh80Jp-OmAkA4LZCKRwIF4Un8Z8NcIfpkQhmmfRA7uSff39AAGEfm10HcudSHH1NNjC7BxD3APPu-Mh22DQOZpb5km8XnNQWfLfe-drkLoRwjSMJB1AzAJ3zriI-eHPOmPt6yrdpW0W_T7m5NIEC3io0qtK-3KBg7lF11eZLqaz-IfQUPRcpn7Cks0M8dWfswx-73mLhtdcSalHfW9Gtg6BnlP_XI0YGDBG-3qQ3v_qGPfro5yPePq8oz-jTmbfPpieqvwxzjCUYoBFDLiYm0w22TBp_XNkXDGhH-4qk0n46JkpFeyT4q7cCape0a-926F78PDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع اعمدة الدخان من القاعدة الأمريكية في أربيل بعد استهدافها بعدد من الطائرات المسيرة الإنتحارية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/83558" target="_blank">📅 06:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات في الدوحة</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/83557" target="_blank">📅 06:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83556">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات البحرين</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83556" target="_blank">📅 06:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83555">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b0f5c801.mp4?token=mP2sWOthOn7xB_WZeZgFs5A05Srx0UsCBNhSDIJ2Vnbad8GDp8frC5jZ_EMctvN3A5vX4XKGJjzkJvY6J9MAkYm19KZqt84yVyn2BbO_s-QGBA-k_50PbJIgEvo6pIDpmDbkKk4np2jMM1B0iDvoHrBIn2iXATGwphSnyBiU9UwvtH8jCQV5TraMfEPClwu9fkvLWvL4IfKbKet4d1r9uTmKSa4CGooFgaQFSgKOjHBVE2EWQlNMslRf5n9tHyC9xli18_Y_3CsKikrpwr6h9PRZyLZ6O44a8s7wDct27xy3fFXVNI9KYQNBdv9K-7Eenh4XOy_Zpk84aw8OgMqVKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b0f5c801.mp4?token=mP2sWOthOn7xB_WZeZgFs5A05Srx0UsCBNhSDIJ2Vnbad8GDp8frC5jZ_EMctvN3A5vX4XKGJjzkJvY6J9MAkYm19KZqt84yVyn2BbO_s-QGBA-k_50PbJIgEvo6pIDpmDbkKk4np2jMM1B0iDvoHrBIn2iXATGwphSnyBiU9UwvtH8jCQV5TraMfEPClwu9fkvLWvL4IfKbKet4d1r9uTmKSa4CGooFgaQFSgKOjHBVE2EWQlNMslRf5n9tHyC9xli18_Y_3CsKikrpwr6h9PRZyLZ6O44a8s7wDct27xy3fFXVNI9KYQNBdv9K-7Eenh4XOy_Zpk84aw8OgMqVKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/83555" target="_blank">📅 06:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83554">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6d2c418d6.mp4?token=mRDICXiYBqpiDDUP-7hTX7-aY7x6VN31qnOeXvcK8W2U6kgliMC4l93iLOYggaAH7I8rJp0kBLo-3mbv_txN0r-bqAG5j5VR8V99D-JWgNZ8if-oRJNMIC1M6J-9CHRtO1E9Oo7pGgdKNAU2JQTDstk8RbG5YfhQPCtCHodqAXE7wQFG234BbC1TRlcDH8xKXIkgp9XEaUeiKBCdoMkCOWII4rgHPkSC2rMeIaETSPXRE9aMd8BodzFVDvzvkpi-M06Yha1ZX6-oVTVGOKBAXbXSF-hrYGcJ-jGszwaHLTV80414OO1nsAEYVGBJ1PXaI7Vygf8iWmm-YKuir1xRgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6d2c418d6.mp4?token=mRDICXiYBqpiDDUP-7hTX7-aY7x6VN31qnOeXvcK8W2U6kgliMC4l93iLOYggaAH7I8rJp0kBLo-3mbv_txN0r-bqAG5j5VR8V99D-JWgNZ8if-oRJNMIC1M6J-9CHRtO1E9Oo7pGgdKNAU2JQTDstk8RbG5YfhQPCtCHodqAXE7wQFG234BbC1TRlcDH8xKXIkgp9XEaUeiKBCdoMkCOWII4rgHPkSC2rMeIaETSPXRE9aMd8BodzFVDvzvkpi-M06Yha1ZX6-oVTVGOKBAXbXSF-hrYGcJ-jGszwaHLTV80414OO1nsAEYVGBJ1PXaI7Vygf8iWmm-YKuir1xRgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منظومة الباتريوت تحاول الصد وسط انفجارات عنيفة وتساقط شظاياها على منازل المواطنين في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/83554" target="_blank">📅 06:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83553">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98243b5322.mp4?token=hoCIXF6BQnOVvAt74dtYC88UUuCZlNFJF44V_hxFG-Bayppg6b6ZXr3NkaXccx17FxmwbGy1-Paf7RX2_hz8lHYKH5qwz4sdKsPkbn8rXVIr0LO9eCVNdlUshM2YnQ8ONqpvFHAosVhS2c99UF9V-jyIIVKFZESPdQn3z2ielTRk8nA8fqR17SS9C1B-KOYueky6xDIdCxG_XeybCw9MjWYFU2lSvHYVlXZx99cLrV8VxZ8hwGGnlEill0L0YB3m7G4a-LMe8jT5pTrcNF3tBUulVhRmWr1To6vmA3ukd0GFEjpfoJEZa20njiQm2xGQM2tkPcSIKaL5pqhMZJujyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98243b5322.mp4?token=hoCIXF6BQnOVvAt74dtYC88UUuCZlNFJF44V_hxFG-Bayppg6b6ZXr3NkaXccx17FxmwbGy1-Paf7RX2_hz8lHYKH5qwz4sdKsPkbn8rXVIr0LO9eCVNdlUshM2YnQ8ONqpvFHAosVhS2c99UF9V-jyIIVKFZESPdQn3z2ielTRk8nA8fqR17SS9C1B-KOYueky6xDIdCxG_XeybCw9MjWYFU2lSvHYVlXZx99cLrV8VxZ8hwGGnlEill0L0YB3m7G4a-LMe8jT5pTrcNF3tBUulVhRmWr1To6vmA3ukd0GFEjpfoJEZa20njiQm2xGQM2tkPcSIKaL5pqhMZJujyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عنيفة في أربيل بعد هجوم بأسراب من الطائرات المسيرة الإنتحارية</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/83553" target="_blank">📅 06:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83552">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpWquTerW2y0SQUFnOM7ICTwwwXir3RcJPPwPwI32h0xnVGbSMszhn_QvtLX4f4G5ZviscuQfGvUaI3yLmK2aYuLGxa-WPLDFOjw6ulqmp2UMjOfnzKKIXuh_rmpJwPnxJ_YyOP4NzoVAH9ZmZ-rd8aMW2EqEVW2D67UHe0_Q02CGw_e2ZVl1Iv_AytwQItPvPhKqnsT53Z0ZuohMBtPzAzUJO8sc2iMVMj8qaqBp7SVrzYjOaAwObw1jW8YgJbnH3IPRHB-FT4vIKGwbrfrLBXEoJKMLWHf0jf11yLc8iblw1KGzQAt3JcwVq0ju4aKvaCnRgdrWXoxnm8lRZbb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجدد الانفجارات في أربيل الان</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/83552" target="_blank">📅 06:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83551">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تجدد الانفجارات في أربيل الان</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/83551" target="_blank">📅 06:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43539170aa.mp4?token=VwisUm3oPuNyPNkHE6iAvzovZ7wFuiJ82l9Y_dCjj9b314MDnB3CFS5BsT-uNvERwK5fDamamwbUnnNXqBzPDJ81CDhV3zzaP5jwDt6i_VM08YrM4OKBfPpsBT9mQb4AaMBWbd950Kb1nUB5IFZsUweGCBwlkFzN8ZLdMjUedQ1bQKjJjHBVqIN570sBXC0aZAhPYi7Ora-yVG2d7R5tGPIGhnaJI2vKaH_9WQmrlzozdBSwVViO9whvLxAmenHxhkcdCYMMHe6akNZV6XKGqBorKB514tgkO1HGAJhVRCqCE5IG7fHQv4S6UPnDCbGd1wQKuLAFOoe-Y0GQTk38Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43539170aa.mp4?token=VwisUm3oPuNyPNkHE6iAvzovZ7wFuiJ82l9Y_dCjj9b314MDnB3CFS5BsT-uNvERwK5fDamamwbUnnNXqBzPDJ81CDhV3zzaP5jwDt6i_VM08YrM4OKBfPpsBT9mQb4AaMBWbd950Kb1nUB5IFZsUweGCBwlkFzN8ZLdMjUedQ1bQKjJjHBVqIN570sBXC0aZAhPYi7Ora-yVG2d7R5tGPIGhnaJI2vKaH_9WQmrlzozdBSwVViO9whvLxAmenHxhkcdCYMMHe6akNZV6XKGqBorKB514tgkO1HGAJhVRCqCE5IG7fHQv4S6UPnDCbGd1wQKuLAFOoe-Y0GQTk38Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/83549" target="_blank">📅 06:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d537f28b30.mp4?token=p736gsnK4zcfd43PO66eX2EtNbGb7g77vuwKdT5UMdlpNX0fGqK_TUpgnJk1JfWPR8q3pxXu1AP5mZ-P061vPpRVcIrc-vsfzqF2XrG_P2HfUA49hYzKu4ue4i3oPPh8Xh34BguroEcPQ03uo5RejIWNUBJ0YFo3nGAJqtwvweqp2iVPtc_N0dQtpnCFFRic-YAw0eqitj9WpZo31dGZjhjiJ2vjn4LHFZd7HNwBU1XVo75xGGhS7857BQ4s5uyLNZwV_IHA-YhF94u1p5F3f3Sx0pJvBbxBaghx3zw4XPZNk-sNk8Da9ZsZSAamNoYXYrk8ZC_W4VfWgKUth0njdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d537f28b30.mp4?token=p736gsnK4zcfd43PO66eX2EtNbGb7g77vuwKdT5UMdlpNX0fGqK_TUpgnJk1JfWPR8q3pxXu1AP5mZ-P061vPpRVcIrc-vsfzqF2XrG_P2HfUA49hYzKu4ue4i3oPPh8Xh34BguroEcPQ03uo5RejIWNUBJ0YFo3nGAJqtwvweqp2iVPtc_N0dQtpnCFFRic-YAw0eqitj9WpZo31dGZjhjiJ2vjn4LHFZd7HNwBU1XVo75xGGhS7857BQ4s5uyLNZwV_IHA-YhF94u1p5F3f3Sx0pJvBbxBaghx3zw4XPZNk-sNk8Da9ZsZSAamNoYXYrk8ZC_W4VfWgKUth0njdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة الباترويت في سماء أربيل</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/83548" target="_blank">📅 06:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9b8186b6.mp4?token=oJqglUWSCRPQ9TILSK_TWamUGuKjp_SGt5hqR75qu7bPzAsxf2BTk1HyeQdkr2O3EzFHiA8wyczUP-QBQWw2sYShggQmlMTq8ZOJg02m8lrlD8Gk4MeXbvGhVjW4-wEsKZu04Z8DJUcMEk1Ax90ZmvD6Vdmz4VDbgSuSnoWvTGTgSUvhretZiZLuEM0WbY0BgkM-pQYubF8YUqkLL7lGO7CIJ2cGgmMQ7jFZxazKPCjA-Khy_5m7Sg7OY10RndnCEDMxrkcbbCk-RVK9keL-icuFiKctMD_LY29mpd1aS9INCV2icZPeAtvWFPDWbEQu7Oq5eELzP05lZwbS6Mv-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9b8186b6.mp4?token=oJqglUWSCRPQ9TILSK_TWamUGuKjp_SGt5hqR75qu7bPzAsxf2BTk1HyeQdkr2O3EzFHiA8wyczUP-QBQWw2sYShggQmlMTq8ZOJg02m8lrlD8Gk4MeXbvGhVjW4-wEsKZu04Z8DJUcMEk1Ax90ZmvD6Vdmz4VDbgSuSnoWvTGTgSUvhretZiZLuEM0WbY0BgkM-pQYubF8YUqkLL7lGO7CIJ2cGgmMQ7jFZxazKPCjA-Khy_5m7Sg7OY10RndnCEDMxrkcbbCk-RVK9keL-icuFiKctMD_LY29mpd1aS9INCV2icZPeAtvWFPDWbEQu7Oq5eELzP05lZwbS6Mv-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة أفينجر الأمريكية في سماء أربيل</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/83547" target="_blank">📅 05:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995536560e.mp4?token=ldJth9rWF-2o6hvznZ_UxeuKNU4f00dzEPz0Qc5jSwFxXI-vyBzT1TUMARC9iIMOqFcuhta4uMbr22gwSy-HojmU8hcjr0vpsU-Ob-rDeI7C3gJm-Oo7uKolJO3CYClZPtxh2FyZItIhPb0WRpWpb4fem3va5ZZWmD7z-I-jcjMCq2IW-eC1Nc0bon9KADGpq3nd2gimsdaJaKUt6xoGnq8sEyrn1DHZaZ8yBnRzUWcwnSQ0g4VpnSIlZSxsjTFPSick_N3PuAXlaeEOR8NiN5Yj7_fUPc9CerVn1cma7CYZVjh_lcu8j1jnnKHRpcmEEzapTSru4gSQRAfxquCdJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995536560e.mp4?token=ldJth9rWF-2o6hvznZ_UxeuKNU4f00dzEPz0Qc5jSwFxXI-vyBzT1TUMARC9iIMOqFcuhta4uMbr22gwSy-HojmU8hcjr0vpsU-Ob-rDeI7C3gJm-Oo7uKolJO3CYClZPtxh2FyZItIhPb0WRpWpb4fem3va5ZZWmD7z-I-jcjMCq2IW-eC1Nc0bon9KADGpq3nd2gimsdaJaKUt6xoGnq8sEyrn1DHZaZ8yBnRzUWcwnSQ0g4VpnSIlZSxsjTFPSick_N3PuAXlaeEOR8NiN5Yj7_fUPc9CerVn1cma7CYZVjh_lcu8j1jnnKHRpcmEEzapTSru4gSQRAfxquCdJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة أفينجر الأمريكية في سماء أربيل</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/naya_foriraq/83546" target="_blank">📅 05:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇷🇺
هجوم روسي واسع على ميناء أوديسا الاوكراني .</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/naya_foriraq/83545" target="_blank">📅 05:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83542">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f41868f4.mp4?token=KJByZXbS2zl-RH-eTl9D8DchR8k5hRVT2CGMOPIOKKtrMJqJrp1DdDiHCcJXREzSUMslw6hPX83I2FuRPIUbpZg3Rbdsg2URek2bpEKR_aGUalAkKTJ3aPTMvzfoPkKLBaCQ3dVJBipDC3ntzHf0RUbv5ChqaaWjrR5CSUSHqq3s9UEPMjDENy7I02tqh0AU1L96N8KPkEw38x7ABu88F_qVHFORMeUrqAEwxCGAuDcCn2aW0yrchi98rNJP-q0KTiMNcpHd53wUCk2HH3R7iHfgevQlNx-jhw4DgMG49C89nHkOsx1Jo6L7jk1zTkTDiHU-VLmFKa7Sh0xLnPfANg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f41868f4.mp4?token=KJByZXbS2zl-RH-eTl9D8DchR8k5hRVT2CGMOPIOKKtrMJqJrp1DdDiHCcJXREzSUMslw6hPX83I2FuRPIUbpZg3Rbdsg2URek2bpEKR_aGUalAkKTJ3aPTMvzfoPkKLBaCQ3dVJBipDC3ntzHf0RUbv5ChqaaWjrR5CSUSHqq3s9UEPMjDENy7I02tqh0AU1L96N8KPkEw38x7ABu88F_qVHFORMeUrqAEwxCGAuDcCn2aW0yrchi98rNJP-q0KTiMNcpHd53wUCk2HH3R7iHfgevQlNx-jhw4DgMG49C89nHkOsx1Jo6L7jk1zTkTDiHU-VLmFKa7Sh0xLnPfANg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Parking Us cars in time square New York City cost 10 $   But park your ATCAM near Persian Gulf cost more</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83542" target="_blank">📅 05:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83541">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قطر تعلن اصابة مواطن نتيجة الصواريخ الاعتراضية الأمريكية</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/83541" target="_blank">📅 05:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83540">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6598f4c01a.mp4?token=pH0EDEYBzdoo_bclV6bNCsWNcAi3rCEn6y4wB6jwH8hZthfpkEHJh1ukgmjQOhJcCroHCNuvPivyoHVrf4QLgrBkfujVkFOeMpkEXKR-_h42c-HaHMkXHCY6ucQbWBtEnCt3IQ1dVqQGxXiwMv0kTBIBape2I7MQbIhIEaTdxnpcER3kLourFMmHZtoNh_FSqBf1ngWlGKkII5pDJnfnsDh0s7RD80uZqw29hGghybjfcEddGKC5qUdc15Mh2BuimweQXMKJ6DPom04g1UT5CDYw3kNwxsYMzyVeoxwCvNVpSuVpIPztretO6YCzahnS7GBBwmzU-IcmkYO4rawD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6598f4c01a.mp4?token=pH0EDEYBzdoo_bclV6bNCsWNcAi3rCEn6y4wB6jwH8hZthfpkEHJh1ukgmjQOhJcCroHCNuvPivyoHVrf4QLgrBkfujVkFOeMpkEXKR-_h42c-HaHMkXHCY6ucQbWBtEnCt3IQ1dVqQGxXiwMv0kTBIBape2I7MQbIhIEaTdxnpcER3kLourFMmHZtoNh_FSqBf1ngWlGKkII5pDJnfnsDh0s7RD80uZqw29hGghybjfcEddGKC5qUdc15Mh2BuimweQXMKJ6DPom04g1UT5CDYw3kNwxsYMzyVeoxwCvNVpSuVpIPztretO6YCzahnS7GBBwmzU-IcmkYO4rawD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
الدفاعات الجوية الكويتية حاليا</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/83540" target="_blank">📅 05:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83539">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91f0d257d.mp4?token=LDNJUHGMiI9vkifqeV10hxEsIksWRsjBkF-iE49vpc68be8Kfgrbdy0NVRJnIRw0dV9n8l7OfOD0U364u8yBUa6GICVSegAAOgp19ykdnZFoRpSr6ktp-dk-GA2s3qzoWT-d6y2sA9OgddQ0K8eXDo0h02mlRbiQlLqIrxP5XR5cRNlsYG7aq3VlK8SnYI_xwh3AiaFk6D0qSG5I1HlJhJIIEcb5fzMUntFFXiUrEpFBcxSmsfTwHA_sWoU9ulIQQ88XdXSz6uH-aJHXeiW30LdVQ5aVWJxq8qa-3O_pytrMFdfIvDAJQFJVBptPkzbOuLvdyAqWAHFaHI56NKgjbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91f0d257d.mp4?token=LDNJUHGMiI9vkifqeV10hxEsIksWRsjBkF-iE49vpc68be8Kfgrbdy0NVRJnIRw0dV9n8l7OfOD0U364u8yBUa6GICVSegAAOgp19ykdnZFoRpSr6ktp-dk-GA2s3qzoWT-d6y2sA9OgddQ0K8eXDo0h02mlRbiQlLqIrxP5XR5cRNlsYG7aq3VlK8SnYI_xwh3AiaFk6D0qSG5I1HlJhJIIEcb5fzMUntFFXiUrEpFBcxSmsfTwHA_sWoU9ulIQQ88XdXSz6uH-aJHXeiW30LdVQ5aVWJxq8qa-3O_pytrMFdfIvDAJQFJVBptPkzbOuLvdyAqWAHFaHI56NKgjbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من القصف الصاروخي الإيراني الذي طال القواعد الأمريكية في البحرين.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/83539" target="_blank">📅 05:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256d6464ef.mp4?token=TJf9-xzuuZQYZknfEIDAxZl9i8EEO8ktyzheypTuHQi-HI2A2jJF7TE1cB4BgG16_YMM9PTqo0FD9KmWAxS14VwgxZwJB1OGEQ_X1vxu9g6Q3l8RlYvqHmobaRUI41u2uG14rrXYiChQ2BAIJa9RUW5ESR2At2rf-N5yeDPNzqENYWY1HPeW8FlCSeqR5m3QOLPEQX44L1y2uoefCn9c3UMp3NB78wrmj95xgGqecApjYx1t1tTB0hzgJHkuVy8pOtfRS8HhCjTuJM5nLWb9LV2TZ1ZrnF6ZDKgQE0PvJ1T-47OtWac__xeylM5kBbOLJ_3DK5lUaGHwiWtI6C7Kpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256d6464ef.mp4?token=TJf9-xzuuZQYZknfEIDAxZl9i8EEO8ktyzheypTuHQi-HI2A2jJF7TE1cB4BgG16_YMM9PTqo0FD9KmWAxS14VwgxZwJB1OGEQ_X1vxu9g6Q3l8RlYvqHmobaRUI41u2uG14rrXYiChQ2BAIJa9RUW5ESR2At2rf-N5yeDPNzqENYWY1HPeW8FlCSeqR5m3QOLPEQX44L1y2uoefCn9c3UMp3NB78wrmj95xgGqecApjYx1t1tTB0hzgJHkuVy8pOtfRS8HhCjTuJM5nLWb9LV2TZ1ZrnF6ZDKgQE0PvJ1T-47OtWac__xeylM5kBbOLJ_3DK5lUaGHwiWtI6C7Kpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الأمريكي:
اليوم، في الساعة 9:40 مساءً بتوقيت الساحل الشرقي للولايات المتحدة (ET)، أنهت القيادة المركزية الأمريكية (CENTCOM) أحدث موجة كبيرة من الضربات ضد إيران.
شنت القوات الأمريكية، بما في ذلك الطائرات المقاتلة والطائرات المسيّرة والسفن الحربية، ضربات دقيقة استهدفت عشرات الأهداف العسكرية الإيرانية، مثل مواقع المراقبة الساحلية والدفاع الجوي، والبنية التحتية اللوجستية العسكرية، والقدرات البحرية.
وتمثل هذه الليلة السادسة على التوالي من الضربات الأمريكية ضد إيران.
وبناءً على توجيهات القائد الأعلى للقوات المسلحة، تواصل القيادة المركزية الأمريكية إضعاف القدرات العسكرية الإيرانية ومحاسبة إيران على الهجمات الأخيرة التي استهدفت السفن التجارية.
وينتشر أكثر من 50 ألف عسكري أمريكي في أنحاء الشرق الأوسط، وهم في حالة يقظة وجاهزية قتالية كاملة</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/83538" target="_blank">📅 05:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpMMeC2OlDi562QyXt_7JUfYs9ru2t5dL71Mkl68TAGBM3ytZklSLYQSM885RUehGkzh-x1ifYh7u2QSEXFXRzw6EVMbXskyrYhCRdAsmWzcQqCm0rmrqXjvFSsXMKUSMovP0THrG4GgN55PtFJebp_YcNywwiCNOcwuuB5Z4gX2kCSvgDzXKBXMws4nDVIS3iqiEGhNXora74eCNV6fvPTtF7SW8nR9klIM9h4b8if02fOxFYhXlAvf6mOJAtLvZc96wONQVhdveUTkK2E8c2NcoS8OXJ3N1ADwd-OWSYdb9FyDxYAbZG2Ci5jnL_Cgq6rx30JG8ZTFIkp4HJK79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر لقطات مرعبة من المنامة، عاصمة البحرين، فشل بطاريات الدفاع الجوي باتريوت باك 3 التابعة للجيش الأمريكي، والمُخصصة لحماية البلاد، في اعتراض وإسقاط صاروخ باليستي إيراني قادم أطلقته القوات الجوية التابعة للحرس الثوري الإيراني. وكما يظهر في اللقطات، أُطلقت…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83537" target="_blank">📅 05:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83536">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تُظهر لقطات مرعبة من المنامة، عاصمة البحرين، فشل بطاريات الدفاع الجوي باتريوت باك 3 التابعة للجيش الأمريكي، والمُخصصة لحماية البلاد، في اعتراض وإسقاط صاروخ باليستي إيراني قادم أطلقته القوات الجوية التابعة للحرس الثوري الإيراني. وكما يظهر في اللقطات، أُطلقت ثلاثة صواريخ أرض-جو من طراز MIM-104F باتجاه الصاروخ الباليستي، لكنها فشلت جميعها في اعتراضه. يُذكر أن البحرين لا تمتلك منظومة ثاد المضادة للصواريخ الباليستية، مما يجعلها عُرضة لمزيد من هجمات الصواريخ الباليستية التي يشنها الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/83536" target="_blank">📅 05:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83535">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVz5Je8F8SgYpr0vDROJw6JzJ9ngN48IfJPcBDO32FCxuRO5HkGz5xNG3mJEY9v5rsTbroK-XDI7rXebPSqXVXBCpcIJEG-2vBbopxqpAW43qw8FVS4k6ACKN7ngA1f9JK8kXCEw3FI9PTwKiPJfJfLGpjGm_I61kQ74fV0WCxgEKSgfAWeHnajJ7UAYljn-k0IALpoABGcF8PwbghT6Hu9gwkgrLL6jGzvNns9PHeGqNTUNfpAVG8U6M5HahGBP5RKWbeJoaFD4Mwx1gFvapPUjFeoILO1MwDzURzxYgStAbPK49IbGO5BmdC-aEaHn9Exz0Gv13m5i42ION_GqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Parking Us cars in time square New York City cost 10 $
But park your ATCAM near
Persian Gulf
cost more</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/83535" target="_blank">📅 05:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83534">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏
😆
ترامب: يجب سحب تراخيص القنوات التلفزيونية التي لا تغطي الخطابات</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83534" target="_blank">📅 04:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83533">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/83533" target="_blank">📅 04:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83532">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇷🇺
🇮🇷
🇨🇳
🇰🇵
🇺🇸
ترامب: يمتلك خصوم الولايات المتحدة، بمن فيهم روسيا والصين وإيران وكوريا الشمالية، القدرة على اختراق البنية التحتية للانتخابات الأمريكية.   لدينا نظام انتخابي منهار تماما ولا يمكن لأي شخص الدفاع عن سلامته.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83532" target="_blank">📅 04:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83531">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏ترامب: الصين حرضت صحفيين على كتابة تقارير ضدي.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/83531" target="_blank">📅 04:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83528">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYVMooN57Pq4fgLT8iIHIrjvNJoLP99FwmEJ18bhTKl_Ybfgy6N4qTSmAwAob70-FnriyCCJvMtdOiAqA9a1iPD1n8xZx4SwD6gqyKayjYlBjIMu8BSZBnEsw-2T-nuBWv5d0XkSZ3fzcs9qMG-cmz1YjF-0TiRF9xvBfMUwp_tBszvhCXknr9TA4BJzNO4nGG7WXOAYEQedVUR0MwYcBBPPiDyBlM3XE0MVj_ktvCwNZcsVfs1yVgjGLdOC9Ji08qNHeKQPHApjXJgg10Z1hO6Idbk30omyhq1w9lnkQwtcKkJlJZTNfTgcvivgh-tTr7DJqreX3tS62RF1-o7q8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2e4c52cf.mp4?token=AJuzui23cGaq_gQEI-4SizvvbayIoY-NWCjCqLSiylzripeg-FVhDvwqWjx308QmKDsxXTusxt2fJa1TjDfIsjtOA21f3qVtO4YYycKUTmvVFBN3Bz847RMUDIwco0kQ6C5RPhwncJU53mlEwCFGev5seduUfoZOskfVWG6N8-a-kJMmjW83jHRNUgzgvAmOcexM27QMooUKYiS7ethYRPmsQ6dKyo-vKKRdU69cfnH2u48yzKnEvXWDKFwqnUgTVmxFE49_zNJfs-3cfLkabGfac7gO2H2MeoHUhrMrBxHsv_xwlwsbVvzTc4kF4c_TYFnZkeLnsQvFkZQf7397sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2e4c52cf.mp4?token=AJuzui23cGaq_gQEI-4SizvvbayIoY-NWCjCqLSiylzripeg-FVhDvwqWjx308QmKDsxXTusxt2fJa1TjDfIsjtOA21f3qVtO4YYycKUTmvVFBN3Bz847RMUDIwco0kQ6C5RPhwncJU53mlEwCFGev5seduUfoZOskfVWG6N8-a-kJMmjW83jHRNUgzgvAmOcexM27QMooUKYiS7ethYRPmsQ6dKyo-vKKRdU69cfnH2u48yzKnEvXWDKFwqnUgTVmxFE49_zNJfs-3cfLkabGfac7gO2H2MeoHUhrMrBxHsv_xwlwsbVvzTc4kF4c_TYFnZkeLnsQvFkZQf7397sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في ميناء تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83528" target="_blank">📅 04:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83527">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6f327901.mp4?token=u1tSrWfbfkOLXgc4P7JNiOVGugOcweufNqvCi__Uvb_1Dsb1-YF6t-6PYj4rsvYOGUYOy6Nez0M8mdht02dANOpH38WL2JMuy1OwvEXURZI4E879TqotMzIElS-PaCBqq6I7wKZVTP2co8QQfkKxJN6J97dCCr-epw0we50uDgz-gnS33SZ_zok_myzLWHOkJQgSkfoyAA503EuAxpnGC4ME8vGE3abErDAfZqxWcFBjt4kBEv_uIEwI1tl2AYehCcmBsRIfGaGpjQtUul6upQZe-Et0IqXDgut8m3l0MLKofctFXXMe8lSacN2EMGAJZ1oLOnDbubRnEF68wmXhRWB2sMa4aMCZPQVxLzBGvWXEvHY7NPZnKix_K92KT76JDbdNSJwnW2RqZtLatDWUvxaFnqWqRsUS2Qb0Gr1woLAiIIZpCw0iZ-izLp9ejmxg-JLHNZeZU8XqrFInrn-DPPhIrt6sb_hqE9hNVcn29eCpsWOzp6SRLizLlT-_kZDJcGatAWIZWBPE-Od5tgO3waT88YY5CcwNOsZ501Sq9TLY3rLl6rtKehQRgTf8omwTbidQENRXSh4tHGdgFvw_0jN3MQcZ0SkK-qE8glf-FlWz6WuG4HsyVvSRNXqBvPheYpOO5k3WVfct1RvFQaELqODpPDlINqhXNgwLYXi8-t4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6f327901.mp4?token=u1tSrWfbfkOLXgc4P7JNiOVGugOcweufNqvCi__Uvb_1Dsb1-YF6t-6PYj4rsvYOGUYOy6Nez0M8mdht02dANOpH38WL2JMuy1OwvEXURZI4E879TqotMzIElS-PaCBqq6I7wKZVTP2co8QQfkKxJN6J97dCCr-epw0we50uDgz-gnS33SZ_zok_myzLWHOkJQgSkfoyAA503EuAxpnGC4ME8vGE3abErDAfZqxWcFBjt4kBEv_uIEwI1tl2AYehCcmBsRIfGaGpjQtUul6upQZe-Et0IqXDgut8m3l0MLKofctFXXMe8lSacN2EMGAJZ1oLOnDbubRnEF68wmXhRWB2sMa4aMCZPQVxLzBGvWXEvHY7NPZnKix_K92KT76JDbdNSJwnW2RqZtLatDWUvxaFnqWqRsUS2Qb0Gr1woLAiIIZpCw0iZ-izLp9ejmxg-JLHNZeZU8XqrFInrn-DPPhIrt6sb_hqE9hNVcn29eCpsWOzp6SRLizLlT-_kZDJcGatAWIZWBPE-Od5tgO3waT88YY5CcwNOsZ501Sq9TLY3rLl6rtKehQRgTf8omwTbidQENRXSh4tHGdgFvw_0jN3MQcZ0SkK-qE8glf-FlWz6WuG4HsyVvSRNXqBvPheYpOO5k3WVfct1RvFQaELqODpPDlINqhXNgwLYXi8-t4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/83527" target="_blank">📅 04:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83526">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تدمير منطومة باترويت في قاعدة أمريكية بالقرب من مطار أربيل الدولي</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/83526" target="_blank">📅 04:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تدمير منطومة باترويت في قاعدة أمريكية بالقرب من مطار أربيل الدولي</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/83525" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83524">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/83524" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83523" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83522">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/83522" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامب بشأن التدخل الصيني المزعوم في عام 2019: "لقد ركزوا على تقويض الثقة في الرئيس الأمريكي. أرادوا فقط أن يظهروا وكأن رئيسكم لم يكن على قدر كبير من الكفاءة، بينما في الواقع قام رئيسكم بعمل رائع."</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/83521" target="_blank">📅 04:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097e67d111.mp4?token=VIIWKrAKD9acZ1w8ji5MOo5sgnfrHZCzx6MBacGMjhmh9C0ZN60goTLTFSbhg8yMdQAe0-68_1YWHAMS0e1IFA0FimuAZLW5iODsEyMEEd2mwMU8dOYmhNJAj_Gh1DBYVlu6NzbcCuPgiOD3jG9yz9WlJkpvgjfs6QIgpbue7-HOL_1PPzeeM8l7_K-YC2w9Fm4LNjXVPCeFG6HOHozMxaENOQ1Y4MFU-fBaEVrUmnpsiDKrsuCln5wKrQri1MsLoWLNwjcYngNYtnAXYc3gALUDICf2PXr8c6lQ2jz-V7hjAdkISK5pSW56LSeM8KnkSsBM8AhlI0pvTYgXiSDxyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097e67d111.mp4?token=VIIWKrAKD9acZ1w8ji5MOo5sgnfrHZCzx6MBacGMjhmh9C0ZN60goTLTFSbhg8yMdQAe0-68_1YWHAMS0e1IFA0FimuAZLW5iODsEyMEEd2mwMU8dOYmhNJAj_Gh1DBYVlu6NzbcCuPgiOD3jG9yz9WlJkpvgjfs6QIgpbue7-HOL_1PPzeeM8l7_K-YC2w9Fm4LNjXVPCeFG6HOHozMxaENOQ1Y4MFU-fBaEVrUmnpsiDKrsuCln5wKrQri1MsLoWLNwjcYngNYtnAXYc3gALUDICf2PXr8c6lQ2jz-V7hjAdkISK5pSW56LSeM8KnkSsBM8AhlI0pvTYgXiSDxyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏تم شراء بيانات عشرات الملايين من الناخبين في 18 ولاية أو سرقتها أو اختراقها من قبل الصين.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/83520" target="_blank">📅 04:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامب: ‏يا إلهي، من كان الرئيس عندما خدعتنا الصين بهذه الطريقة</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/83519" target="_blank">📅 04:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13acd514fa.mp4?token=eQudq3p5ZstHfQD_fjgJOkezBy8VriwbM0FV0q4FgufuAuadcBJWZNoubiXTjQhq9ElStlMu7Qr3tjl1L4zgDrzkU2eN6v_0o0birT8hmkt4ekMfe4R1-r7l-PpVHrO3hg--lIfvKShEOUa1qbTDZY3cY6SiU6AeHYdKrlcMSXYwXoXX_DZ7Dtk5Ko589-nb-mTlVWRY4V9Bbk76KDtstZO9MiQJXgCNlaAXYm9M5XYD_wiYMGYZ3tbjae5B6tUo7sPehrTXSaIF8kA_KoMRONAUnytMvK180M4fMC_Vcg5rjgxR03_MRIgZCsLt2YSg4HZSvTd99IgHi_p1sv8b-zaOLvR3-EHo-VfLbbtEBCgrM6sFeoJaH8yYrO49NtiY5X_nvY5SKznE28Kg1T0I-b29xvOW-lTjiqbkgnO8Z1vRMQWW1ht1Q_dBHUrlIY7Sq38SrxngtqVgtX8UQE3SN6V0Hs7SJku5XeIo3-RX3CX90OZcVIhzTibBpf8cDyR41hB8kXcLVrTGuMswryo5oe33cIT27TrVAU446w6uoJakHeYekM5cfUFANllhTQcu7agoex7S-36mWa2s_8Y4KuSKJ64Gjr7qXB_E7XEEh4_9lF6OY5692yNf4C2hjc-pl0xXd7biu2gxiPUB2Zydi5ahFpfsO-Al9LljobQ5PjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13acd514fa.mp4?token=eQudq3p5ZstHfQD_fjgJOkezBy8VriwbM0FV0q4FgufuAuadcBJWZNoubiXTjQhq9ElStlMu7Qr3tjl1L4zgDrzkU2eN6v_0o0birT8hmkt4ekMfe4R1-r7l-PpVHrO3hg--lIfvKShEOUa1qbTDZY3cY6SiU6AeHYdKrlcMSXYwXoXX_DZ7Dtk5Ko589-nb-mTlVWRY4V9Bbk76KDtstZO9MiQJXgCNlaAXYm9M5XYD_wiYMGYZ3tbjae5B6tUo7sPehrTXSaIF8kA_KoMRONAUnytMvK180M4fMC_Vcg5rjgxR03_MRIgZCsLt2YSg4HZSvTd99IgHi_p1sv8b-zaOLvR3-EHo-VfLbbtEBCgrM6sFeoJaH8yYrO49NtiY5X_nvY5SKznE28Kg1T0I-b29xvOW-lTjiqbkgnO8Z1vRMQWW1ht1Q_dBHUrlIY7Sq38SrxngtqVgtX8UQE3SN6V0Hs7SJku5XeIo3-RX3CX90OZcVIhzTibBpf8cDyR41hB8kXcLVrTGuMswryo5oe33cIT27TrVAU446w6uoJakHeYekM5cfUFANllhTQcu7agoex7S-36mWa2s_8Y4KuSKJ64Gjr7qXB_E7XEEh4_9lF6OY5692yNf4C2hjc-pl0xXd7biu2gxiPUB2Zydi5ahFpfsO-Al9LljobQ5PjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: سينشر تقييمات أمريكية سرية تُظهر أن أنظمة فرز الأصوات عرضة للاختراق من قبل الصين وروسيا.  ‏الصين نفذت أكبر اختراق معروف لبيانات الانتخابات بدءاً من دورة عام 2020.  ‏الصين حصلت على 220 مليون سجل للناخبين الأمريكيين.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/83518" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Emox0ol_3qH9Je79N_NVbuvziKyKw_eismLDsBhvkK0rv8GD-yf2T9SdDOU6_3Lb88UntjJbrBqgXkia_Rpqk8prWqRQu6eV9JGfOJ-WqiwqgVtiOZE1NlXeQAmmAMf9AuKxMrVRGMxvUY-0bGc160nSvUl871WD7ZemckiT5k6KfSc27lNB5EpL3Ful8q99KBXF5FtFaDVTAc93CiFdetK_fY0zXbjCnXHodWGPGGoAKfFwRpUcQDp4W9UFPbmL0XdY65wY_d6JcouepYmb2jJuDzEr5fS1GgkVa7XMGdv_15qbZc2Ra3DHzpX604Q4mGjVuYYwLqyReuuJ_nY3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البيت الأبيض ينشر : الأخبار الكاذبة، سي إن إن عدو الشعب!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/83517" target="_blank">📅 04:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb28Mh39OKRCv61wMwFZ8fL8Ejk9mE-lJyzeMAF4ZI8if2G8Cgy3W5j3YgcVAR1zGNrY1Et_c6xAY_i2lfuTYz4ZYeM8PkvYxKuNyzLlvx8PFFvN8F3zvQ9htjSET-PHJMu-5KIHgc6g8_BXDbX1wztcRuvefGvm0qhXqmNAJZE0iTxnfb6Pes85eqMdjXM_HL0FaMWBHEzueH5LDdMc_7TrqyK7ZPCTVKdPuRHYgKvzm1rLZmxZAvSfjZvreUgaaHbeXtvbXJuveFvhn79uYmM_fnfpnLIPAAzdhcvb-YBTicaEvCYXVwU3_kM6n832NrgQPx_BEIjoZhN9WAzHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صور الاقمار الصناعية تظهر تعرض مستودعات أخرى لهجوم إيراني جديد في الكويت.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83516" target="_blank">📅 04:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انفجارات في ميناء تشابهار جنوب شرق إيران</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83515" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5a8b9b061.mp4?token=kgzKQ0ASudsCdjJxTymkHJYQbTR1b2VkTAqJdUX3-C7o54bITzv14oPOpHWNlIhtcgw6XZegg3nJ1cun52wOtS3vDjTkhzlU05WC0qTyJ7PeNetOXMoghE6Q5JeBuT9l1fW3oE6XZOL7NPCLhXaWAi_s-HlpKw8wKSlNsPs-DfA7Ru9EfAmxPdSmFCe8LIcbRSvSYNQgL6Ywjs5s6tXpbZuv0wqVo1aIE_hfh20K5DfDLl1Ep0jHv8HKDMpe285LLJ83AET16B6DRCYCVcn2ez2P6BDiwptJE7UYtIigFtMdt7WQpi9wslpAbgpPKhvkxVENz4mHVV6t51OGVO9D7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5a8b9b061.mp4?token=kgzKQ0ASudsCdjJxTymkHJYQbTR1b2VkTAqJdUX3-C7o54bITzv14oPOpHWNlIhtcgw6XZegg3nJ1cun52wOtS3vDjTkhzlU05WC0qTyJ7PeNetOXMoghE6Q5JeBuT9l1fW3oE6XZOL7NPCLhXaWAi_s-HlpKw8wKSlNsPs-DfA7Ru9EfAmxPdSmFCe8LIcbRSvSYNQgL6Ywjs5s6tXpbZuv0wqVo1aIE_hfh20K5DfDLl1Ep0jHv8HKDMpe285LLJ83AET16B6DRCYCVcn2ez2P6BDiwptJE7UYtIigFtMdt7WQpi9wslpAbgpPKhvkxVENz4mHVV6t51OGVO9D7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب، بصوت أجش، يكافح لقراءة جهاز التلقين.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/83512" target="_blank">📅 04:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامب، بصوت أجش، يكافح لقراءة جهاز التلقين.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83511" target="_blank">📅 04:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98986b4537.mp4?token=Px7dGM_k0vUjTMwWnV--r5_zZkbSEZTWglU-XoBpFvY_j1UpxfltzSo5A-ix1Qh9FP3mnctsL5Vcux-SkditwEC9eoG4cqf7VF-pY14W5qakfY84taM8dsB13GHC12FlcOYc-jwWmDDGkWC81MsmRCwFMeHl2pALfIiEDcZ_GFDEqeHJ48DzpgfhzIZ9dhEI-sFYTkHdg472_KnPh74eGZILaks5D3nXc6u1BIx_b2vxMEkYPsdOoTpUWIva-rAruchGwl9lQG_YhZ06nDioi5tbjvERhzt6vbsJV9If-mIPd_3-EzLNeW_977E1etdO7F7t2FUNGLCtHCqKobrIRnY3Ie9_Z_-hkv6V6X2FPvo87EZwz4_rn3ehT0FkNQemUAIAOpGYeWpXbNNThKrsjYFpaRk1dNrj8c9ILMYqD5ZprExq_yyIlfx0O0hSQs_bFnEetPEi6VAoEs88W2Z5CdrK_zCvScy-a9TSpkHBBOOs8o7VULbngQwp9fkLlDFySxPU-_1MaXKY9VqSIuoB8QNSLQvz_lyv3x7FdqhUm6Gl3d2rrH0ijyply5Ylp3VNEPvyESPISsuUSJce8UtmMW5Ipu_rVK-b6hkvzM7Yr-FO_YGY-8haeTHmK0J8YraJ4L6wHXVAkWFfTGn8hWkRj-q7XjLSDGzRdpy3a0NoKbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98986b4537.mp4?token=Px7dGM_k0vUjTMwWnV--r5_zZkbSEZTWglU-XoBpFvY_j1UpxfltzSo5A-ix1Qh9FP3mnctsL5Vcux-SkditwEC9eoG4cqf7VF-pY14W5qakfY84taM8dsB13GHC12FlcOYc-jwWmDDGkWC81MsmRCwFMeHl2pALfIiEDcZ_GFDEqeHJ48DzpgfhzIZ9dhEI-sFYTkHdg472_KnPh74eGZILaks5D3nXc6u1BIx_b2vxMEkYPsdOoTpUWIva-rAruchGwl9lQG_YhZ06nDioi5tbjvERhzt6vbsJV9If-mIPd_3-EzLNeW_977E1etdO7F7t2FUNGLCtHCqKobrIRnY3Ie9_Z_-hkv6V6X2FPvo87EZwz4_rn3ehT0FkNQemUAIAOpGYeWpXbNNThKrsjYFpaRk1dNrj8c9ILMYqD5ZprExq_yyIlfx0O0hSQs_bFnEetPEi6VAoEs88W2Z5CdrK_zCvScy-a9TSpkHBBOOs8o7VULbngQwp9fkLlDFySxPU-_1MaXKY9VqSIuoB8QNSLQvz_lyv3x7FdqhUm6Gl3d2rrH0ijyply5Ylp3VNEPvyESPISsuUSJce8UtmMW5Ipu_rVK-b6hkvzM7Yr-FO_YGY-8haeTHmK0J8YraJ4L6wHXVAkWFfTGn8hWkRj-q7XjLSDGzRdpy3a0NoKbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يتحدث عن حالة البلاد قبل عامين: "كان لدينا متحولون جنسياً للجميع"</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/83510" target="_blank">📅 04:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c351174ca.mp4?token=NH2AC01rStFFLBD8apU4XW5CTQSPiUtbllmhF3cToE1yintLFNPqCoqPyg3U95Ty5eJ8PLa0Zi1wVb8WRWY0iY0aaY58ZEahmQq2oqAUBfEXrN8FKayXb99P_bW8AaqGWB-bYXr5Xvi8sIGb_Tx3XKaQjY62bu2IqJmsB0uN8oDnK0uT5SNkLVMpYyeQmsz8Hwh8wDxOGzebwsEBQW28pzELTCKNXgc9VOn1fWZkq2eLKRGeIyClWb8TMfvHH-N75VP6kgwmV3khIX3d09J7Bv_IwayH8892q2MdY2kcCA3NI652lOTVtV6QALDY2_s4oJgvqsB-3YRiaHSGO6DfAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c351174ca.mp4?token=NH2AC01rStFFLBD8apU4XW5CTQSPiUtbllmhF3cToE1yintLFNPqCoqPyg3U95Ty5eJ8PLa0Zi1wVb8WRWY0iY0aaY58ZEahmQq2oqAUBfEXrN8FKayXb99P_bW8AaqGWB-bYXr5Xvi8sIGb_Tx3XKaQjY62bu2IqJmsB0uN8oDnK0uT5SNkLVMpYyeQmsz8Hwh8wDxOGzebwsEBQW28pzELTCKNXgc9VOn1fWZkq2eLKRGeIyClWb8TMfvHH-N75VP6kgwmV3khIX3d09J7Bv_IwayH8892q2MdY2kcCA3NI652lOTVtV6QALDY2_s4oJgvqsB-3YRiaHSGO6DfAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يتحدث عن حالة البلاد قبل عامين: "كان لدينا متحولون جنسياً للجميع"</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/83509" target="_blank">📅 04:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏ترامب: الولايات المتحدة الآن الدولة الأكثر جذبا بالعالم
‌‏كان العالم بأسره يسخر منا كأمة، ولكن ليس بعد الآن.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/83508" target="_blank">📅 04:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83507">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
🇹🇷
🇮🇷
أكسيوس:
خلال زيارة ترامب إلى أنقرة، حذرت أجهزة الاستخبارات الإسرائيلية الولايات المتحدة من أن مسؤولًا إيرانيًا قد ناقش محاولة لاغتيال الرئيس أثناء وجوده في تركيا.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/83507" target="_blank">📅 04:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83506">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/83506" target="_blank">📅 04:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/948f6e6b08.mp4?token=mjKXLw0Fr5cDxuUrEvJtbXfQLdjClG9YZ3p0pEczQACmsXTudsAQ7if-thq0h1LRd4pfpawlU9IgTBoDa0I_OHsXnHxBWBQTDSlwH_iyGyeZapSJ0BNLtJD09CZraxHftlQVVb1DYdPFRGpPUnkWuuu7KdTX3IqridrbJgF8eDjw1l0-UaY46H1pcQzz56XgJAA12uNLsgSaJLpueTiIpTeEOc6VBGSByYHNbFAqAe9M-3Bvp_i1Y-uL0yuwxC_7VO4yxyGjMlXP0RJl3Ur8xF8s2RbGZHZPrCfCnRo4FA1z0ybuLsTYwSRoA64cbIXF_w73tMRUdr9_1_2nmpuOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/948f6e6b08.mp4?token=mjKXLw0Fr5cDxuUrEvJtbXfQLdjClG9YZ3p0pEczQACmsXTudsAQ7if-thq0h1LRd4pfpawlU9IgTBoDa0I_OHsXnHxBWBQTDSlwH_iyGyeZapSJ0BNLtJD09CZraxHftlQVVb1DYdPFRGpPUnkWuuu7KdTX3IqridrbJgF8eDjw1l0-UaY46H1pcQzz56XgJAA12uNLsgSaJLpueTiIpTeEOc6VBGSByYHNbFAqAe9M-3Bvp_i1Y-uL0yuwxC_7VO4yxyGjMlXP0RJl3Ur8xF8s2RbGZHZPrCfCnRo4FA1z0ybuLsTYwSRoA64cbIXF_w73tMRUdr9_1_2nmpuOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83505" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83504">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECu0FcFuqwreFyhjrO32oa-RYL_WRC2tQD__zDu3hUHS4YFQL9Fi_mTT8RydILo4rH9VJW6GnDkgTLedAdwWjZojz8vG3U7u5xDx64577cvY97ubLPZMMvXH36V9iH-agyIMzKccyf_1aWBjje45iI7eUjPdel85q8ZYuXPomEbmZsuKsIEF0Yjwo9cs6REEbIE9LI8GuQvsvMa193m9DtXGM_Ue-WGPsSYoVmOL7UiqAlm1ZZ0LVaESoFjTxgwfrkaA3agbmgnXpvk6JWwurJhaQrJTIH3XxqzN8sYk8F9Y9IR7LyrQwOuNsdr6Z4eYyRFJ5zLqX8Ycz3h8kOdIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أبناء مدينة أم قصر يرصدون النيران المشتعلة في المعدات العسكرية ومنصات الصواريخ المتنقلة الأمريكية على الأراضي الكويتية بعد دكها بالصواريخ والمسيرات الإيرانية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83504" target="_blank">📅 04:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83503">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzZkGJmCQ3JljCAQpUTaYLziJ14UMY6NKUOQ0XdSJ1LY9inypkYgtPgZaSDClN4nU-Q-JVhqDpQ6HK20RQZwYdR52tojCL_9xRAU7b3iUyWxDu2vrdaVD-9JD9MDZ2hNFCPB8KcA84jULbE3WyHG1nRLn9PwVdNc7dltOoVXNktC21C8SS_bM8_6WLp7EAX8izOmUAilYn77j-zi8ecVK1IBAeBY2cdpSDY8gTyBua1qDS5Z_C5VvQsR1EBi08O0fQD_FKDzutBBKY3EStf79BFa-IMSYnJ6rodUClYlYN9hbVv36ewWXxVh1XsiaU9oHRQ7WXNuymzyJOwy-0-dng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83503" target="_blank">📅 04:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83502">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">إستشهاد 2 وإصابة 4 مدنيين جراء العدوان على أحد الجسور في بندرعباس كحصيلة أولية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83502" target="_blank">📅 04:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83501">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83501" target="_blank">📅 04:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83500">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83500" target="_blank">📅 04:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83499" target="_blank">📅 04:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83498">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83498" target="_blank">📅 03:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvrZUsp-FX_XANbd36lNjvmTU5YzY_OMzAYhoFj92fuZeTe7Q0aIHXAqb8IrUCm2Wrq8BBp7eus0V0rD3ezx_7wewHf-9DdAatpbXDeJkyr1Bk5faZLHoS_mIc4zGAoD_tDegnU6P99KXlO5t6coN4Ia1AcyMf6a-15tycq-un7lEVQdZR20oKWXcJuNNGOzMWND4vx9mkug6SHu0l8dfHAtTQkXqGXGOxxwjDCFaRM5hdj44aTtp0i2ll_PFuR9UhGqwYU6mGKQGOAGdDaX8DHEjjKIelkIXIgPDd-kqhAV20MTHq6V8KZb8qFeFo8xc8Yfhv72FPXla9VzAGDH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد متداولة من المعارك الصاروخية بين الصورايخ الإيرانية ومنظومة الباتريوت الأمريكية في سماء البحرين.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/83497" target="_blank">📅 03:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8105b22245.mp4?token=tfJVW9AtPW8In2nQRS_FOj3OyDzOVzem7aSkdyDyo3W65AzEwF3krqitWJnZg2KF-39DNnUaN6kufVeu8K2hEw3DZjf24uVVOPBOxwtjmU6LbQUy2qN3_gE8KYGfUVWD3qH_fNFRYkwAIUm_pJQXtAHt0x1Sssv0oIim7yVdwCCnPw1PgFIjhvZCvEwF-6-zf50S76ioclsHSBp8shrwmk2-S60Ovs2qxgmZuy2-H2TJxXbKEzAaeMAyADHMx7a0k4S8dehJjLiqmbD25h7Z3QRktUiDjvkO8huU3YbtzIwet-9gl66eTStwAOTj4QQ6B2PY0H-0Zhssj1brhxor2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8105b22245.mp4?token=tfJVW9AtPW8In2nQRS_FOj3OyDzOVzem7aSkdyDyo3W65AzEwF3krqitWJnZg2KF-39DNnUaN6kufVeu8K2hEw3DZjf24uVVOPBOxwtjmU6LbQUy2qN3_gE8KYGfUVWD3qH_fNFRYkwAIUm_pJQXtAHt0x1Sssv0oIim7yVdwCCnPw1PgFIjhvZCvEwF-6-zf50S76ioclsHSBp8shrwmk2-S60Ovs2qxgmZuy2-H2TJxXbKEzAaeMAyADHMx7a0k4S8dehJjLiqmbD25h7Z3QRktUiDjvkO8huU3YbtzIwet-9gl66eTStwAOTj4QQ6B2PY0H-0Zhssj1brhxor2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/83496" target="_blank">📅 03:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مشاهد متداولة من المعارك الصاروخية بين الصورايخ الإيرانية ومنظومة الباتريوت الأمريكية في سماء البحرين.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83495" target="_blank">📅 03:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9786e5193e.mp4?token=V-azAZ250_zJf74iIcSdc3PXw7KrJ6uvT6-ekHdrBUhBh6JNxva7SbFSuchZkkxV3a0MHnCX1WHZ92K16RO51XhtUNS82TeroDspN4H9Jooe0LB5WWZ1ybZVjqEDrJ1hU50Zsp4160uQ9DLxGwOjJQUZOgY_HZE6VTu4hjPrR5i6Qjcngze4dUuNMItEn9JiX-Y9nMbJyxKqGB0dNjOfyHpcqEFymatEfgaxmqWRGE_6pXdO6bfQBCgpcskofHMLvLGjFPksm_fTRdmqxOPntXpJU2U2AGXiB9hdhxV4XUWJslQOJWUdBRdx-COTevyGaY5qfvF7Z0j85ecVZkSozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9786e5193e.mp4?token=V-azAZ250_zJf74iIcSdc3PXw7KrJ6uvT6-ekHdrBUhBh6JNxva7SbFSuchZkkxV3a0MHnCX1WHZ92K16RO51XhtUNS82TeroDspN4H9Jooe0LB5WWZ1ybZVjqEDrJ1hU50Zsp4160uQ9DLxGwOjJQUZOgY_HZE6VTu4hjPrR5i6Qjcngze4dUuNMItEn9JiX-Y9nMbJyxKqGB0dNjOfyHpcqEFymatEfgaxmqWRGE_6pXdO6bfQBCgpcskofHMLvLGjFPksm_fTRdmqxOPntXpJU2U2AGXiB9hdhxV4XUWJslQOJWUdBRdx-COTevyGaY5qfvF7Z0j85ecVZkSozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ أخرى تنطلق من إيران صوب القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83494" target="_blank">📅 03:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d6c9dca2e.mp4?token=ozPTQGnCfgTbPgTIeZhbl1FpnV7tnfz6XIhoVLf3CTyPAaAGrmlMUHfl6b18oQYNf_HmIQxRqgGN0STf5b18YThyd1-Jgu3ViPoihtbPzkWYj7qmVPmx4M0ENsCUMrHv2slTldwPzFREnqBAWG-F5WC41eARaa9R0tRzHdJx_j3F2D5wTAih6PG2x9GRYE2ni28w8xZ4ayEn_ApE_ujPFe9yw7j9XNzOrKpdmLt9WOqBL2j2Og3D5COj21sMqxTT_oL0VSrlhXgjA1W7FhHGWKU9cmWP4s0XJlUmpmcR60XPdr-bYzMpZqAEAQ8jNUudqSvA0f8QPPi0mmUOsapPeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d6c9dca2e.mp4?token=ozPTQGnCfgTbPgTIeZhbl1FpnV7tnfz6XIhoVLf3CTyPAaAGrmlMUHfl6b18oQYNf_HmIQxRqgGN0STf5b18YThyd1-Jgu3ViPoihtbPzkWYj7qmVPmx4M0ENsCUMrHv2slTldwPzFREnqBAWG-F5WC41eARaa9R0tRzHdJx_j3F2D5wTAih6PG2x9GRYE2ni28w8xZ4ayEn_ApE_ujPFe9yw7j9XNzOrKpdmLt9WOqBL2j2Og3D5COj21sMqxTT_oL0VSrlhXgjA1W7FhHGWKU9cmWP4s0XJlUmpmcR60XPdr-bYzMpZqAEAQ8jNUudqSvA0f8QPPi0mmUOsapPeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83493" target="_blank">📅 03:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de24f0dac0.mp4?token=d6D6JCbbbBn0oUS9WPwjPTwDnE6Gd1Xr0OyDVfmuNl3mQ30uObNhytaFGRj4MrTqx7gW-e_qe7i6ItdWt9jJHX3GX6o5HMjpMAtfZnnkc3fvUGf0F7ncIbnL4bpRQB8YOKcjd3pCGt8odA-hb7cYLNdQ7JLg3BiV8uBsq_QGI3_2iWO5G3JJCEnSkcC8LX2CFET4P8F2daGrCjqmqhgVIG7GBy8d6DKpJMXbAzVFvWT0e_mJv9FqCKay3h_byAwo5qodNXhfZM_kAreu_9REu_Xy1Rvyz_EHrqbK503HcA7t5MzQKsVdxKzOW_8XOepQRVA27u_bjYd85hyH49XMqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de24f0dac0.mp4?token=d6D6JCbbbBn0oUS9WPwjPTwDnE6Gd1Xr0OyDVfmuNl3mQ30uObNhytaFGRj4MrTqx7gW-e_qe7i6ItdWt9jJHX3GX6o5HMjpMAtfZnnkc3fvUGf0F7ncIbnL4bpRQB8YOKcjd3pCGt8odA-hb7cYLNdQ7JLg3BiV8uBsq_QGI3_2iWO5G3JJCEnSkcC8LX2CFET4P8F2daGrCjqmqhgVIG7GBy8d6DKpJMXbAzVFvWT0e_mJv9FqCKay3h_byAwo5qodNXhfZM_kAreu_9REu_Xy1Rvyz_EHrqbK503HcA7t5MzQKsVdxKzOW_8XOepQRVA27u_bjYd85hyH49XMqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة بمنطقة الجهراء في الكويت</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/83492" target="_blank">📅 03:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c20eb661.mp4?token=pR0H4pHdFl7t_AbcEFJ2yGOciyRJTp4-slenfMjl18KW5CjxfWhb3BLpNtae7NqC4tUa4OB4plrX1U_1SbRqQxCXOUaSmzS3kJYXpweZ-JcIJgRrveJKIgXIO_sxrN_S_Z1pHYXJ1dQePLaQvtuJKG1TD0wkNPhCcbZslhUM5CsNgkdlK2637WyaNtekkJVj9FoCYq3nwAvTmdLzdda-s6RMwOqTAsdyJlhpTrYB7r7AFibXyE6P7vQ8fK2VDK2sdv7Ml7yLULmILm8BI6Ky_AbcoEmcUcSYI0MxlNp4c8Iho1mjfL886K8sJl3nDYtqV9Pm2QzridqjqnX0rbs0Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c20eb661.mp4?token=pR0H4pHdFl7t_AbcEFJ2yGOciyRJTp4-slenfMjl18KW5CjxfWhb3BLpNtae7NqC4tUa4OB4plrX1U_1SbRqQxCXOUaSmzS3kJYXpweZ-JcIJgRrveJKIgXIO_sxrN_S_Z1pHYXJ1dQePLaQvtuJKG1TD0wkNPhCcbZslhUM5CsNgkdlK2637WyaNtekkJVj9FoCYq3nwAvTmdLzdda-s6RMwOqTAsdyJlhpTrYB7r7AFibXyE6P7vQ8fK2VDK2sdv7Ml7yLULmILm8BI6Ky_AbcoEmcUcSYI0MxlNp4c8Iho1mjfL886K8sJl3nDYtqV9Pm2QzridqjqnX0rbs0Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تحويل مسار الرحلات الجوية إلى البحرين</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83491" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5423809ebf.mp4?token=b0OIVO_6o0OVdr7VCz7ATVn6pRAZ11KNwpCnC3RzlTOwEvr8T3HShCWAvVXZr3Sz9Yt83aWqkT0wXwpWm_DDmZgm2Kf_bqK4jgxGqdxpieq_nN3Rw6SHnAAFzYoSKx6z3XUzPz0859pPCEpWEUQWzcUfxCpKKgj9JQHwnEhuXuVtF0AS4oUoCQb91pp1tyHDNstuU1I983sMhxcggP2tzdWo1TMimKpoewn8Eey187EXJEasnT1qbreoIhN4iniEA2kxZ02zuDZBmqqh_pFx_HzyjcfYXD7ZXqQaErMG8oBRIfHR6G_wYP3GzavgDbQ1s_VcC9W60tum913s9vthhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5423809ebf.mp4?token=b0OIVO_6o0OVdr7VCz7ATVn6pRAZ11KNwpCnC3RzlTOwEvr8T3HShCWAvVXZr3Sz9Yt83aWqkT0wXwpWm_DDmZgm2Kf_bqK4jgxGqdxpieq_nN3Rw6SHnAAFzYoSKx6z3XUzPz0859pPCEpWEUQWzcUfxCpKKgj9JQHwnEhuXuVtF0AS4oUoCQb91pp1tyHDNstuU1I983sMhxcggP2tzdWo1TMimKpoewn8Eey187EXJEasnT1qbreoIhN4iniEA2kxZ02zuDZBmqqh_pFx_HzyjcfYXD7ZXqQaErMG8oBRIfHR6G_wYP3GzavgDbQ1s_VcC9W60tum913s9vthhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تحويل مسار الرحلات الجوية إلى البحرين</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83490" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منظومة الباتريوت الأمريكية تحاول الاعتراض في سماء الكويت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83489" target="_blank">📅 03:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e21f06d5.mp4?token=bWLm9pN5LbscK8wdiFem-X-mxtiUCF7KNoJypV8GHlVczkU4D3Cv946o80Z2ySkaKVoCxoxS6KOecM5Qgj9U0y7cjhLHJcW3JGHMGj-d2h7n8sNgQZ16YaZisZI56a60WO4ItJ7OSskBNZAo-UwZQPC1goyROrb4qPNmVAIT-WC8iQWqmutWQtHverZKIV4b0ePZ7YMTuvwMFlmuiKsYbdOHgk25HUmZ2263Wm1V7SxyKIA5NwZfK3B1OpkXo-RI4aDFR47xRDdFlUZhVS5i2_sOTj43ACE6fl0429Iq44AJ9miHEhn8JwD1wFFp9rb7HukD9BbAatEFrRqLiziK7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e21f06d5.mp4?token=bWLm9pN5LbscK8wdiFem-X-mxtiUCF7KNoJypV8GHlVczkU4D3Cv946o80Z2ySkaKVoCxoxS6KOecM5Qgj9U0y7cjhLHJcW3JGHMGj-d2h7n8sNgQZ16YaZisZI56a60WO4ItJ7OSskBNZAo-UwZQPC1goyROrb4qPNmVAIT-WC8iQWqmutWQtHverZKIV4b0ePZ7YMTuvwMFlmuiKsYbdOHgk25HUmZ2263Wm1V7SxyKIA5NwZfK3B1OpkXo-RI4aDFR47xRDdFlUZhVS5i2_sOTj43ACE6fl0429Iq44AJ9miHEhn8JwD1wFFp9rb7HukD9BbAatEFrRqLiziK7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في الكويت</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83488" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏تحويل مسار الرحلات الجوية إلى البحرين</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83487" target="_blank">📅 03:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/333b8f7dc7.mp4?token=Zi9JdAQUQP6rlMepKuZ9UernTPHia4vxnt31PIPB-5xX4Z7ff8XlP1JDNkXCZnI3-S4WVnqYo36lImYNLBIlijpHnT4-y4IJq6uvtsg1ernXOD-DN8P_V82_AMv9aT-wuAsRX_kveOSZLpz9dRtH-o8NBH2G8mSUobiRKiTu3FDZoZoLeYAl4-XSyrxyCspCIjchQpHRMhaL28A7Zth_cZfOJ97KATkWD5mdhiWpxS6U7FuCEED6--C6HAwEeGW9suHkL7sUwTYcjvwA_FFBZGlAOXFAoEaATfqNy2kcOyfQRyltA1SMiZARxkHZxU7CkGxC9pIoI5d8Wqe36vNz6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/333b8f7dc7.mp4?token=Zi9JdAQUQP6rlMepKuZ9UernTPHia4vxnt31PIPB-5xX4Z7ff8XlP1JDNkXCZnI3-S4WVnqYo36lImYNLBIlijpHnT4-y4IJq6uvtsg1ernXOD-DN8P_V82_AMv9aT-wuAsRX_kveOSZLpz9dRtH-o8NBH2G8mSUobiRKiTu3FDZoZoLeYAl4-XSyrxyCspCIjchQpHRMhaL28A7Zth_cZfOJ97KATkWD5mdhiWpxS6U7FuCEED6--C6HAwEeGW9suHkL7sUwTYcjvwA_FFBZGlAOXFAoEaATfqNy2kcOyfQRyltA1SMiZARxkHZxU7CkGxC9pIoI5d8Wqe36vNz6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة إطلاق الصواريخ من إيران نحو الكويت</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83486" target="_blank">📅 03:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/83485" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83484" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/931e975fb0.mp4?token=aLlOSIuXltshCTFVLXgxx8bXYlfCXcD-CSjg6vQZ4LRw4gdfX483nkHq551DSgXuJcchg75MuoPNsv5QVqv7YSdxZrl20glWEbAcRggANO2NZyh6SGTpP6WrTRakvlEKj5IhQNIXzb8or8e1G-eRzENA8DmRNQgJ_yBTUtMCrHMRv1KK0-vmyiwLxf1XISoVxkj9aW8YH8MmhweAoWL_rdWTL0H772C2XrBNQTb9-t_aT-TaIhbeem-Jb0EZ3pMmzjR6UH5v7Ie-WQKnyrqJHef56cQokdfJprcGRUlx2bRs9W0yjrgyRlb0cGSxHsPEj1xEPFMLd9ad0ppX4l1oyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/931e975fb0.mp4?token=aLlOSIuXltshCTFVLXgxx8bXYlfCXcD-CSjg6vQZ4LRw4gdfX483nkHq551DSgXuJcchg75MuoPNsv5QVqv7YSdxZrl20glWEbAcRggANO2NZyh6SGTpP6WrTRakvlEKj5IhQNIXzb8or8e1G-eRzENA8DmRNQgJ_yBTUtMCrHMRv1KK0-vmyiwLxf1XISoVxkj9aW8YH8MmhweAoWL_rdWTL0H772C2XrBNQTb9-t_aT-TaIhbeem-Jb0EZ3pMmzjR6UH5v7Ie-WQKnyrqJHef56cQokdfJprcGRUlx2bRs9W0yjrgyRlb0cGSxHsPEj1xEPFMLd9ad0ppX4l1oyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  رشقة صاروخية تنطلق من إيران</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83483" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الصواريخ وصلت وانفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83482" target="_blank">📅 02:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83481" target="_blank">📅 02:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الله أكبر  رشقة صاروخية تنطلق من إيران</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83480" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله أكبر
رشقة صاروخية تنطلق من إيران</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83479" target="_blank">📅 02:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83478">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">إصابة مباشرة في قاعدة الجفير مقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83478" target="_blank">📅 02:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83477">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83477" target="_blank">📅 02:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات في البحرين</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83476" target="_blank">📅 02:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
مسؤول أمريكي:
الضربات الأمريكية استهدفت عدة جسور في إيران يوم الخميس.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83475" target="_blank">📅 02:43 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

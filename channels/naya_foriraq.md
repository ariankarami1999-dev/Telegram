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
<img src="https://cdn4.telesco.pe/file/TqI87NaW7jnZsESUqDsR7eKyGCOYPOgXmq8uoY-VlsQZHRsE2cpdEJj6qNiiDGyO9nUDchbsS-Q5BaUAdKHxyXFYGaYYLE4Jitna0xGLjrieCQxDPzFSdCXIqyrx1JRFzA_cWOnft8J_-O4I0S8shjIgIE0tTJNHfRFzztzHRAEhVV3P_rZmMmfXh_zeglAzb3hbIenkeUz-WXB5H5TST2UFmEsEAQBhKpYSNwMe_D6sL8rzNFmSCeOB9KAS7UldBn94xJqa8x3MRbczXEBI1SsYL-M_Y1j6pDRwhhd71sbAIvpUQFDkle_DRrlDJDIdsWnZ83fqk3I5ETsUa7dDJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 16:29:12</div>
<hr>

<div class="tg-post" id="msg-86630">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb6f4d28c.mp4?token=I-jO02b8EIaoCFkBHjNqnuL3Xfselfj3epMINc3InWRkGaW0Xhb-g9LVA_Qta1wfWFKTMkrTndCuaPGnL2ez7PcrpDYBgitqGAFpsQIpKEHBfgUv3Ic7ta6JfLJH51w51dMJHPQvGmURj_g4CIKpqeCLXzTp0aMhCPu9KIkawMkTDkfwfd1KabEiqW6tJ9Q2ngMU2awpSkH0fKe5E2IPq6CF4bbm72L_6kTGLg1Dl6t4Qp4HybvCXb5SkUWa9DvrUQ-N8zc8cjqEkls4twQksR_7eozZ7sQ3DYlpqt9AtJ35yhlig4IFZ1uqYL3TUBDGcBx9rrTX3sJ0vKBqjhgeXgaw9dtPehZCKqLBOB5hElBxI6nKUq0kHE3s4y7qAlXGnH1_GMXWyrlLTQUaOWxcmvJm10OC39i7bIeh6_EJQe0wqz4yc_8AdO7097zx5VlWuF5JI4R7kioX6hN7PaCOUfBO0l3Ps5GzTZxIv9yqJDoBWOyzfVR9u1UCRQFsRRaNzmH4SS9pFafyiDFdM61WK5OiG6whNqPeuK4_vMT4TrkOkS8tbeQIlBsbatbS8ft3Xi2ITjivd_gfZY56aW30JmmA6jbtM9Q3mxXOK2afsQOVM7C9kwS8mtsCdWEH95cm0YqqoLGbw9bQhuJ8ZUgps_wDhFPFOTs9KMpneCHTeHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb6f4d28c.mp4?token=I-jO02b8EIaoCFkBHjNqnuL3Xfselfj3epMINc3InWRkGaW0Xhb-g9LVA_Qta1wfWFKTMkrTndCuaPGnL2ez7PcrpDYBgitqGAFpsQIpKEHBfgUv3Ic7ta6JfLJH51w51dMJHPQvGmURj_g4CIKpqeCLXzTp0aMhCPu9KIkawMkTDkfwfd1KabEiqW6tJ9Q2ngMU2awpSkH0fKe5E2IPq6CF4bbm72L_6kTGLg1Dl6t4Qp4HybvCXb5SkUWa9DvrUQ-N8zc8cjqEkls4twQksR_7eozZ7sQ3DYlpqt9AtJ35yhlig4IFZ1uqYL3TUBDGcBx9rrTX3sJ0vKBqjhgeXgaw9dtPehZCKqLBOB5hElBxI6nKUq0kHE3s4y7qAlXGnH1_GMXWyrlLTQUaOWxcmvJm10OC39i7bIeh6_EJQe0wqz4yc_8AdO7097zx5VlWuF5JI4R7kioX6hN7PaCOUfBO0l3Ps5GzTZxIv9yqJDoBWOyzfVR9u1UCRQFsRRaNzmH4SS9pFafyiDFdM61WK5OiG6whNqPeuK4_vMT4TrkOkS8tbeQIlBsbatbS8ft3Xi2ITjivd_gfZY56aW30JmmA6jbtM9Q3mxXOK2afsQOVM7C9kwS8mtsCdWEH95cm0YqqoLGbw9bQhuJ8ZUgps_wDhFPFOTs9KMpneCHTeHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طائرات حربية مجهولة تحلق في أجواء مناطق سهل نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/naya_foriraq/86630" target="_blank">📅 16:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86629">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
طائرات حربية مجهولة تحلق في أجواء مناطق سهل نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/naya_foriraq/86629" target="_blank">📅 16:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86628">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
🇮🇷
مسؤول أميركي:
الجهود الدبلوماسية تتقدم ببطء واستئناف المفاوضات المباشرة مع إيران لا يبدو وشيكا.</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/naya_foriraq/86628" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86627">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiwYWFEaMJM65osGE7IJEh8CWOBonjBbxIhSDkguvAdvKN_zvzgaQu7ZZkJeitte9AayXqSWOEg3WITjsRiQ94V5N098Q2qWbCqSPOPYzzV6THE7CKRC6_JP8cyyJDlwOqgGlRaLZkm9MSH5QL2M8n-RroA_qcJr8QkCnoKyQ8YU-wDCc5Zx82kdPLXd-fGSq5S-ruQZgO-X86P_DOHb67AJj-tU3kd_6Xat8mwnYuF1S51we09yP8wD4sbg6HVLwEC80dN9uBiDPDwWdmQRHGfPYd3N8WmufaSk1UPvN5yifeYr1wQivlHhFwv1alOb4uLiKQiw6EDuV3Umtx_1Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
واشنطن بوست:
الجنرال أليكسوس غرينكويتش القائد الأعلى للقوات الأمريكية في أوروبا يحذر البنتاغون من عدم كفاية عدد المدمرات البحرية لحماية إسرائيل من الهجمات الصاروخية الباليستية الإيرانية مع تلبية احتياجات الدفاع الأمريكية في الوقت نفسه.</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/naya_foriraq/86627" target="_blank">📅 15:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86626">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية: اتفاقية ثلاثية لاستئناف التصدير عبر جيهان بطاقة 750 الف برميل يوميا.</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/86626" target="_blank">📅 15:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86625">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzeAxX91LYGkjxGlQ_q8eFsXbdGYfLBHXr1tLztjDYL4OCO5oGFTwZBy-UUaMA3_aWlorXWcg_oSHfPxZZ7UHgTUFVEOkZM4Uc4Rx0JvpvG7tMsAIAnEH8va-YgJYdGoIxU7TBIhdpx3N00PneVQRa4tNvWPuoiZLadn3R86pLYOQbQ7SVIqrr6AdMXFouxf_tI5Jr4ilQysIRQR1VJXKHVh8RFN6k7WvcOVrvTHx5NavkUL59r2A25_-1RLu9dXi0ytCECKC3rSaL0MvXuleDlo34iW_petREpwG3maVoeZV45p5vtwk8DbHHDazm1d39kk9XYk5bfB8yMh2yLePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
في ابهى صور الديمقراطية..
ترامب يهدد السلطات التشريعية باستهداف جو بايدن واوباما سياسيا في حال لم يتم تعيين تود بلانش بمنصب المدعي العام للولايات المتحدة مؤكدا انه سيبقي تود بلانش مدعيا بالوكالة.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/86625" target="_blank">📅 15:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86624">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrtHcQahG0knrfBZ1Xe_hnlLZQho9fLR96b5TOkocmyg3QP56DiBYSvb-pUuyPiMfXCgzA9Prj2B-AWtxwaaA7h7TEFuX0KhXH1v5WJTNqICrnULN4CqQpdOshorv9VPTcDlLPAMUbJhhk9YfNIwpvaSXaPK5j8CqX6m3WkspZY5GM5CSZzxvehbtDdZ8BobcQU6LJ0amVdSy9XxUCmUN0cXk5qd3kOpZ7BBBjug_yi-W_1ppsVTZZPXA7dUCGnwq70nUTuFe7AR8x-9kmbtvW3t0gzqKoIp_eY5Lzu36HeGixP9Qv9PGz-3kndvrLLolIrp13cd6CLA9JF1MYLLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارات الامريكية في بغداد وعمان والقدس المحتلة والقاهرة وبلدان اخرى تنشر:
يجب على الأمريكيين الموجودين حاليًا في الشرق الأوسط توخي الحذر واليقظة الشديدة، والاستعداد لإلغاء الرحلات الجوية، والإغلاقات الدورية للمجال الجوي، والاضطرابات المحتملة في السفر. وقد أجلت بعض شركات الطيران في المنطقة استئناف جداول الرحلات السابقة؛ بينما ألغت شركات أخرى بعض الخطوط</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/86624" target="_blank">📅 15:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86623">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇱
جيش العدو:
خلال الليلة الماضية أصيب ضابط في الجيش الإسرائيلي إصابة متوسطة خلال عملية عسكرية في جنوب لبنان. تم نقل الجندي إلى المستشفى لتلقي العلاج، وتم إبلاغ عائلته</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/86623" target="_blank">📅 14:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86622">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuv4sNFBIRZNgSNsE1FL80PkHPYfwnO-nbizPx9aIaIGtTX9aPnN-_nBL57FouNuoLJ2rdVMFFuE_GGbX9z7_1qBvVlusGmrK4TmEtMNGdKpYU0-E9L-i9DBsL7uTKIdGT_b8Bk1AZaMfw51UNHzEpbGDfaObYUKUu0C9wlv0D5wgzYlqDF536sBnn7b7UZzdEfCqcYgF8jVBHB0wx0zNCuWkaTktrZuMGb0Z7Hf9J9QmBJpkx4bedRtZ_d8Q3djuXd01wMCipefjzvDLk16aTJuZyy2l5l-nkwIFSvk-FhWwwK9FKMb7Ch1hAEKOiQetQ1SWQKWfK8B7LiOGDC6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظام ال سعود يعلن فتح باب التطوع الى الجيش بسبب النقص في صفوفه لكثرة الانشقاقات ولصعوبة تجنيد مرتزقة بسبب شحة الموارد على خلفية اغلاق مضيق هرمز والحصار في البحر الاحمر.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/86622" target="_blank">📅 14:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86621">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
🇮🇷
السفير الايراني في العراق:
موسم الزيارة الأربعينية لهذا العام يسير بأقل قدر من التحديات، هذا العام، بدلًا من الحديث عن المشاكل نتحدث عن الإنجازات التي حققها موسم الأربعين. الزائرين الايرانيين يتمتعون بصحة جيدة وفي ظروف مثالية لأداء الزيارة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/86621" target="_blank">📅 14:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86620">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية:
اتفاقية ثلاثية لاستئناف التصدير عبر جيهان بطاقة 750 الف برميل يوميا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86620" target="_blank">📅 14:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86619">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">من الحريق في اربيل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/86619" target="_blank">📅 13:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86618">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34d9c123.mp4?token=aMTJq9f3UjmLU05nGSx2pJOkSSaPTYm2jBSCvoMZ95GXfHTiGufI0rhbExZuUiGA6aLZoT_qRhKpuvkoRs6in314qWduuU_4EQvoHx-V8Hs6aYc9jT4QF4WPtpcIk7pfY_jMO0ACA5tLUtEXFPVAUozHlgOs3pvFetnfNx3MQjHaw0yBCSwWhxbm7nBARWvsx5IIdxo9hKs5-ItOZ1nsoljGuK_4XCgpfSD2gOYa419dxyX0b5oNNoa7lbBFXKveb83_eWHaFfCnwo6A6-8wkSA8AfmEPIVEYURuKTUdQ7WKGqXrl7gAs6vRTBciyc4WsjRTzAP95Zzk1n_uC--gQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34d9c123.mp4?token=aMTJq9f3UjmLU05nGSx2pJOkSSaPTYm2jBSCvoMZ95GXfHTiGufI0rhbExZuUiGA6aLZoT_qRhKpuvkoRs6in314qWduuU_4EQvoHx-V8Hs6aYc9jT4QF4WPtpcIk7pfY_jMO0ACA5tLUtEXFPVAUozHlgOs3pvFetnfNx3MQjHaw0yBCSwWhxbm7nBARWvsx5IIdxo9hKs5-ItOZ1nsoljGuK_4XCgpfSD2gOYa419dxyX0b5oNNoa7lbBFXKveb83_eWHaFfCnwo6A6-8wkSA8AfmEPIVEYURuKTUdQ7WKGqXrl7gAs6vRTBciyc4WsjRTzAP95Zzk1n_uC--gQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيقات اضافية من الحريق الذي التهم احدى مصافي محافظة اربيل</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86618" target="_blank">📅 13:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86617">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇪🇸
وزارة ‏الداخلية الإسبانية:
وفاة ما لايقل عن 67 مهاجرا خلال عبورهم جيب سبتة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86617" target="_blank">📅 12:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86616">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e37647a01.mp4?token=NX5YvJe2GMRc8upKjoG3p3I83d2I_ZVkH3NvjgomdWrb89MobOTopIlpL4KomOikZT2vcJFQIj-002DYNGX_LtcOYjtZDEzO1_pS8K2taRcr8q-wrui4Uw0UijDPBluOomfWbOBdWTiBvrVZELcJ98Id4y_dJC02qyMUp4THjj3sjVjxZmVZSIJ9hjotIHSu_RGc2GnvyvWEszShhYC46XIykGMxrrB3wCJHkWuA4gt7UbNuaelfRfV1QRxGClUT9WUZs0MeiXq1dGKNSGYNzzSDWh3SbWO3bBbiKVjMdOF1vvBfxA816yeMJ5LjQuNPjpffbiBEr-BfLGoKt6bhkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e37647a01.mp4?token=NX5YvJe2GMRc8upKjoG3p3I83d2I_ZVkH3NvjgomdWrb89MobOTopIlpL4KomOikZT2vcJFQIj-002DYNGX_LtcOYjtZDEzO1_pS8K2taRcr8q-wrui4Uw0UijDPBluOomfWbOBdWTiBvrVZELcJ98Id4y_dJC02qyMUp4THjj3sjVjxZmVZSIJ9hjotIHSu_RGc2GnvyvWEszShhYC46XIykGMxrrB3wCJHkWuA4gt7UbNuaelfRfV1QRxGClUT9WUZs0MeiXq1dGKNSGYNzzSDWh3SbWO3bBbiKVjMdOF1vvBfxA816yeMJ5LjQuNPjpffbiBEr-BfLGoKt6bhkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الحريق في مصفاة للنفط بناحية شمامك بمحافظة أربيل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/86616" target="_blank">📅 12:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86615">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feed9248e1.mp4?token=pO0rExJ_kSUd-PYsdMG0NIP4O8EPKEl59DGrYbF6PJTkQXOJAQHjo2tAUCpr4CExsmJ8Kr7yBjgu82RMft0bzaYzXxcfDqrSbu-EzHIRiu3-BKPLBsP4vN9BR_NgplNOuNRi3-GXJtKOLBZN_6nUBK8MaqiUwxlg5GoDaNNs5Pcf362cMTCn31wGLVQpaykLYv1NJVmzgmOrJKrNSj09ItaNxzusGyFKeeiLOY-Ytntv4x7ilKZXFXoesO9F7xuhk5rWe7EG-EF3FCBfwgQQiSGazwprMUIoTT7HXnO-ViQcqXV2gQVvd5f_iHd2oTcOCwXi00f_0uuqxf7aK2eVS60DBozHJ7IsfAS_ndM2qRXwctKZKmZD0GUXnZdn-7FZEA60OmLtN-5Zd-f35aAvbevCsJTkpi6pLq0cxpxvh7z2QnTHZEGnHtvg2XbYnpVGB0TQUFNyCF5UkifGZF4ft2vGf7DrMUPyHrpQ6s73ZUTdjRNlotKcgC5RFEc9x-sgq2Sr1WfjyGI_Quj-WGU7beKQKz839RheI7jBUHzXTuF5LYQIkV8JpuLaaK-Umz9jMtxECWxHVR3eaKeh9GJMY96H9hpx9904LMcmS2gYm378pKLdGpmhsrHIsCtlQZ7t88C_JKog6SbDAeOfqBso_QjZkSCcM1aixHaXtvSfwOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feed9248e1.mp4?token=pO0rExJ_kSUd-PYsdMG0NIP4O8EPKEl59DGrYbF6PJTkQXOJAQHjo2tAUCpr4CExsmJ8Kr7yBjgu82RMft0bzaYzXxcfDqrSbu-EzHIRiu3-BKPLBsP4vN9BR_NgplNOuNRi3-GXJtKOLBZN_6nUBK8MaqiUwxlg5GoDaNNs5Pcf362cMTCn31wGLVQpaykLYv1NJVmzgmOrJKrNSj09ItaNxzusGyFKeeiLOY-Ytntv4x7ilKZXFXoesO9F7xuhk5rWe7EG-EF3FCBfwgQQiSGazwprMUIoTT7HXnO-ViQcqXV2gQVvd5f_iHd2oTcOCwXi00f_0uuqxf7aK2eVS60DBozHJ7IsfAS_ndM2qRXwctKZKmZD0GUXnZdn-7FZEA60OmLtN-5Zd-f35aAvbevCsJTkpi6pLq0cxpxvh7z2QnTHZEGnHtvg2XbYnpVGB0TQUFNyCF5UkifGZF4ft2vGf7DrMUPyHrpQ6s73ZUTdjRNlotKcgC5RFEc9x-sgq2Sr1WfjyGI_Quj-WGU7beKQKz839RheI7jBUHzXTuF5LYQIkV8JpuLaaK-Umz9jMtxECWxHVR3eaKeh9GJMY96H9hpx9904LMcmS2gYm378pKLdGpmhsrHIsCtlQZ7t88C_JKog6SbDAeOfqBso_QjZkSCcM1aixHaXtvSfwOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كبير في احدى مصافي محافظة اربيل في اقليم كردستان شمالي العراق</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/86615" target="_blank">📅 12:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86614">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4b26c5b8.mp4?token=Up3xRWGHSU7zH0FeGM_03HhylJ2vPlaDljS0D1RK7XO24UxRh3Rbo_LRY6M_AB_6ulp8VKKYmPEd4OVzGgu3r4gpCyJLXZLbJXSsq98-s9rHsz7Nn7k2llgWzPWo91RO5RxPqr3nPi2hoIC8Nh-GXd3wnNM1pdYASONhxecOwtMayX26TfB981mFooRBpFTmq9uogolkAUW-kk3X9BHkoT95VLN2VKNJDJ1bWkzb2zlWhTuc4F-_X-vgTS0p38XQt67sXvqFaSUCIKZFgbeSZEWxL2SfUrPc3oBylbjQ8h0qNuK59znc49MPhQXgk5-S-dX4j_eys9wYGC5y60NIjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4b26c5b8.mp4?token=Up3xRWGHSU7zH0FeGM_03HhylJ2vPlaDljS0D1RK7XO24UxRh3Rbo_LRY6M_AB_6ulp8VKKYmPEd4OVzGgu3r4gpCyJLXZLbJXSsq98-s9rHsz7Nn7k2llgWzPWo91RO5RxPqr3nPi2hoIC8Nh-GXd3wnNM1pdYASONhxecOwtMayX26TfB981mFooRBpFTmq9uogolkAUW-kk3X9BHkoT95VLN2VKNJDJ1bWkzb2zlWhTuc4F-_X-vgTS0p38XQt67sXvqFaSUCIKZFgbeSZEWxL2SfUrPc3oBylbjQ8h0qNuK59znc49MPhQXgk5-S-dX4j_eys9wYGC5y60NIjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كبير في احدى مصافي محافظة اربيل في اقليم كردستان شمالي العراق</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/86614" target="_blank">📅 12:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86613">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
🇯🇴
🇮🇶
السفارات الأمريكية في العراق والأردن يتنافسن بالدعوة للمغادرة..
سفارة أمريكا في الأردن تدعو مواطنيها إلى التفكير في مغادرة منطقة الشرق الأوسط وتجنب القواعد العسكرية، وتحذر من أن النظام الإيراني غير متوقع، وأن هناك احتمالًا لتصعيد مفاجئ واضطرابات في الرحلات الجوية والمجال الجوي</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/86613" target="_blank">📅 11:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86612">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇱
🇺🇸
منصات المستوطنين في الكيان تتحدث عن غضب في الولايات المتحدة .. نتنياهو يريد حرب دون نهاية وقد يقدم على عملية عسكرية قبل الانتخابات</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/86612" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86611">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هجوم مسير إيراني يغزو الكويت</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86611" target="_blank">📅 11:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86610">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هجوم مسير إيراني يغزو الكويت</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/86610" target="_blank">📅 11:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86609">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86609" target="_blank">📅 11:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86608">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
قائد مقر خاتم الأنبياء المركزي:
تسعى الولايات المتحدة الأمريكية، بوتيرة متسارعة، إلى إشعال فتيل حرب شاملة في المنطقة.
هذا النهج هو نتاج استراتيجية خطيرة تهدف إلى التوسع والهيمنة غير المشروعة في جميع أنحاء المنطقة.
لقد أثبتت الولايات المتحدة الأمريكية، في الحرب الأخيرة ضد إيران الإسلامية، أنها لا تتردد في ارتكاب أي جريمة أو تدمير ضد مصالح وموارد المسلمين، وذلك في سبيل تحقيق أهدافها وأهدافها الشيطانية.
يجب أن تدرك الدول الإسلامية في المنطقة أن الولايات المتحدة تستغل مواردها وثرواتها وبنيتها التحتية الحيوية ومواردها الاستراتيجية كدرع دفاعي لجيشها المتهالك، وفي الوقت نفسه، لتعزيز آلة الحرب والأمن للنظام الإسرائيلي الإرهابي الذي يقتل الأطفال.
لقد أثبتت الجمهورية الإسلامية الإيرانية وأبناؤها الشجعان والأبطال في القوات المسلحة وجبهة المقاومة أن ميزان القوى في المنطقة لم يعد يتبع المعايير السابقة، وأن عجز الولايات المتحدة عن تحقيق استراتيجياتها العدوانية وغير المشروعة ضد إيران الإسلامية قد دفع الجيش الأمريكي المتدهور والنظام الإسرائيلي المزيف إلى شن الحرب وإراقة الدماء والشر من وراء تحصينات الدول الإسلامية، وإلصاق تكاليف الحرب على حكومات المنطقة.
يُعلن بوضوح: يجب على الدول الإسلامية أن تراقب عن كثب جرائم الولايات المتحدة وأن تعيد النظر في تعاونها معها؛ وإلا، فإن أي دولة تعتبر نفسها درعًا دفاعيًا للولايات المتحدة الأمريكية الإجرامية والمتجاوزة، ستشتعل في نار الحرب.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86608" target="_blank">📅 11:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86607">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
🇺🇸
إعلام العدو عن مسؤول أميركي: بعد الهجوم الصاروخي المفاجئ على قاعدة أميركية في الأردن الأربعاء نفذ الإيرانيون هجمات إضافية
الإيرانيون هاجموا سفناً في مضيق هرمز رغم تهديد ترامب بأن أي هجوم إضافي سيقابل بضربات أميركية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86607" target="_blank">📅 11:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86606">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇵🇰
إعلام باكستاني: العثور على جثث 8 من بين 10 متسلقين انقطع اتصالهم بعد انهيار جليدي على جبل "برود بيك" في باكستان</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/86606" target="_blank">📅 11:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86605">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
إعلام أمريكي : ‏دار نقاش حول محاولة إنهاء [الضربات الموسعة] بحلول موعد افتتاح الأسواق المالية يوم الاثنين، وذلك بسبب المخاوف بشأن تأثير التفجيرات على الاقتصاد الأمريكي والعالمي، لكن لم يتم تحديد موعد نهائي</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86605" target="_blank">📅 10:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86604">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇷🇺
🇺🇦
قصف صاروخي روسي كبير على العاصمة الأوكرانية كييف والنيران تشعل السماء وسط انقطاع واسع للكهرباء.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86604" target="_blank">📅 10:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86603">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
إعلام أمريكي :
‏دار نقاش حول محاولة إنهاء [الضربات الموسعة] بحلول موعد افتتاح الأسواق المالية يوم الاثنين، وذلك بسبب المخاوف بشأن تأثير التفجيرات على الاقتصاد الأمريكي والعالمي، لكن لم يتم تحديد موعد نهائي</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/86603" target="_blank">📅 10:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86602">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هجوم بالمسيرات والصواريخ الإيرانية استهدف القواعد الأمريكية في الكويت</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86602" target="_blank">📅 09:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86601">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86601" target="_blank">📅 09:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86600">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC_CCvPlPYo44Vn2gl1IRGLR_a7hHllKGL7c74S60hntSO3sBin3WKV-VojvyBqUuGpLGzXxqgSPmwpS4fF2_cqZ39PcWq6-scw1vljo9OGvwxzKkArlnsGbp-TYkqJwrAaWqVmlDFveiO-fnAjD4bGgpA1bXPTG6tGfSSmRX2zCCNGKpNt_zYWD494pUhDnQDxZa-z61Cnv0KGGbfdtWsbwAL0ftMFYAOiGLVuJU0TvZ89jdgBIad5SXqW_nUxB2suPhUxtjuJglZntWLX6i4LDkL2w1mQxvL1fUHVbxByCxnOKr3P-hc_WDqGXIXXvkYRCN5XywPtILqfhejnxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري قبالة عمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86600" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86599">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حدث بحري قبالة عمان</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86599" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86598">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86598" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86597">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
إعلام يمني: أنباء عن سماع دوي انفجارات شمال شرق تعز في اليمن.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86597" target="_blank">📅 09:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86596">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaaDn6pUq2ICZ1nVYOjmYuWEwvFsGK2Sm0doGKBE6gI_40ZnUJTxHm0mSwkcx1RH82_HXkmjjLASLc9CAND6GhaGax_Q3sm0X-TyuMRevnemiQjMWdzDWo_3ugv_CUyWVzG4lYnC8eS8yOTZcNKyVcRhPOeypwg1pb3Fl4ZoSMvypsYwfFGD_UlT0jLD7e5IPWm_o0yaizzQS6oUpttagSkeo5R1Lq_rw7TLTEsNXXXSzuGXB45xsiBckiFcgyLLPWbmOlEh06PMBe335NTXrF2BX9hc9lFDTxCohofjNx1WPagFyhbPq4oX2AWYCKvzjQw4nK0vpuZBzNgjlIbzQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
الهيئة البحرية البريطانية
: ‏شنت القوات الإيرانية هجوماً على ناقلة نفط أخرى في مضيق هرمز ليلاً أثناء عبورها الممر الذي تحرسه الولايات المتحدة. ‏أصيبت السفينة بقذيفة في غرفة محركاتها ولم تعد تحت القيادة.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/86596" target="_blank">📅 06:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86595">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044c3ed5b4.mp4?token=Fyc1AVs35X__i6RuoZPlLwCGKFX2m1FZ6c7ykL6mk3ika9Oz58FNHZhKje3qrLV7saAlOn0MxI4K9-8QBlvdZ9rZvj0ro7v-0mNoeM07DbxWPLWFLJcpmjShmJj9J9Pxbg5IgTOfXr189FpSeXz8moJQuf4Yk3K8Oz_y9P23RQfTTD7BDEH-MKRtmMrkWKLfoxRouJ99wPbzDEsMo46pF70aupTKPj89UMRA1fsykqsl3za5ljqDeAZN38unl28ep2ncXmcdZcmPY9COKFvPw6aKR1gvzb3JU6B8OCdd-6H3e6xAkKrsFA9je8RN1PIs6ypsnAm6oYSw3pRLKZz6D05xs0TSJzbcQMTzWwk1JdfZXKW63LkQZ0ZOGLj9oaoaCmgVBkJFoaBeRRQYqiRqzDAirMOm6M26rtCk_qNhrU0HGhaVRaqIjsBoISd3-E4KgEPQddpIwmZgEh_SNfm_Z7WF9aEhozpIjUHOx4OF9JcZkUqQVU2-aQMsCp73TWaxxzbqArXg222GH3wNucbtJDsN-IVsPBlF15gdYOgj8rA78WQ2hzG0sirYvyxVXt4evuuHQqugszYxrwD5Ck5en-P9IXa_5__hMX3LGPGuaLFSEI2S2Dwg-VOfT4UvzHwAM9TjtZhBoR59jnSNtuFLKPrWVttv6chKXRpvmjNCobM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044c3ed5b4.mp4?token=Fyc1AVs35X__i6RuoZPlLwCGKFX2m1FZ6c7ykL6mk3ika9Oz58FNHZhKje3qrLV7saAlOn0MxI4K9-8QBlvdZ9rZvj0ro7v-0mNoeM07DbxWPLWFLJcpmjShmJj9J9Pxbg5IgTOfXr189FpSeXz8moJQuf4Yk3K8Oz_y9P23RQfTTD7BDEH-MKRtmMrkWKLfoxRouJ99wPbzDEsMo46pF70aupTKPj89UMRA1fsykqsl3za5ljqDeAZN38unl28ep2ncXmcdZcmPY9COKFvPw6aKR1gvzb3JU6B8OCdd-6H3e6xAkKrsFA9je8RN1PIs6ypsnAm6oYSw3pRLKZz6D05xs0TSJzbcQMTzWwk1JdfZXKW63LkQZ0ZOGLj9oaoaCmgVBkJFoaBeRRQYqiRqzDAirMOm6M26rtCk_qNhrU0HGhaVRaqIjsBoISd3-E4KgEPQddpIwmZgEh_SNfm_Z7WF9aEhozpIjUHOx4OF9JcZkUqQVU2-aQMsCp73TWaxxzbqArXg222GH3wNucbtJDsN-IVsPBlF15gdYOgj8rA78WQ2hzG0sirYvyxVXt4evuuHQqugszYxrwD5Ck5en-P9IXa_5__hMX3LGPGuaLFSEI2S2Dwg-VOfT4UvzHwAM9TjtZhBoR59jnSNtuFLKPrWVttv6chKXRpvmjNCobM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كلا كلا آل سعود..
تشييع الجثامين الطاهرة لشهداء اللواء 30 الذين ارتقوا نتيجة العدوان السعودي الأمريكي الغادر الغاشم في محافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/86595" target="_blank">📅 04:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86594">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇱
إعلام العدو:
حدث أمني في الجيش الإسرائيلي والتفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/86594" target="_blank">📅 03:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86593">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cffc20c83.mp4?token=pzmL1UOyJfIi6irRdf2m4WyxoZ0QZqN3u71d4PwUplkYTq8Qfm3DiVwE-O7XdGIMYv3b8wdfZ5OO0C3Hf0JUaoAQ6sPPo7H7noro2NfwYyeLnqDBdSVpKCxYQJk0TK9DmLC7sbxMGCG_7t1L_YWtsoPfZDkk_7WELtRtzaCxLxwr1B9CN-glxlu6_IzCMnvt3Lp2aS_1bUdgBuvPFmQPWPKnY-HACtzkfu7Cxns9ImDJWJVGwqEgv5jPOkx5sF2umS-zfFU8ke3ZVXC5qk8MTAaDnweBiDpE2yikd4kcDq0FguWchnYa8-HX8JkGZues8pa-Vz-29O50sRkgE2emUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cffc20c83.mp4?token=pzmL1UOyJfIi6irRdf2m4WyxoZ0QZqN3u71d4PwUplkYTq8Qfm3DiVwE-O7XdGIMYv3b8wdfZ5OO0C3Hf0JUaoAQ6sPPo7H7noro2NfwYyeLnqDBdSVpKCxYQJk0TK9DmLC7sbxMGCG_7t1L_YWtsoPfZDkk_7WELtRtzaCxLxwr1B9CN-glxlu6_IzCMnvt3Lp2aS_1bUdgBuvPFmQPWPKnY-HACtzkfu7Cxns9ImDJWJVGwqEgv5jPOkx5sF2umS-zfFU8ke3ZVXC5qk8MTAaDnweBiDpE2yikd4kcDq0FguWchnYa8-HX8JkGZues8pa-Vz-29O50sRkgE2emUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
إقلاع مستمر للطيران الأمريكي في قاعدة موفق السلطي الجوية بالأردن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/naya_foriraq/86593" target="_blank">📅 03:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86592">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
إغلاق جزئي في مطار دنفر الدولي بالولايات المتحدة الأمريكية بسبب تهديد أمني محتمل.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/86592" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86591">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7OE8neXgogf8ckM9FlB_Y8Ex1BQ3rmT1K8UMhs88C4JwRRo9EbMhCTFzCup0KjO3uMc5KbbTEd939OskFHjo1QafGkrfEwfBXIoWdpSQMqxlkgHqPWDJ64woBDzTIce0dPr081112rx8klnEO_MpgtCWK5KtsC4fQJEnJ_Lnbs9t1nTwKdvSP1H9dEwlqhU_eIY3sCGm8kTjcG5G_wDG00E-8V5Rys1X5LCOjB_yXxISV5Xh0rRw3XWy9nFREsvwN96WAtcl-05wrDN8mKyjE82j6xRS4Ll2BVBuG4h2BrlvNw4nCE80GgAtLwp-EgII3iLIm8lavQ5vHwD1PvyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇺🇦
قصف صاروخي روسي كبير على العاصمة الأوكرانية كييف والنيران تشعل السماء وسط انقطاع واسع للكهرباء.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/86591" target="_blank">📅 02:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86590">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
🇮🇷
‏مسؤول أمريكي: ترامب أمر بجولة جديدة من الضربات ضد إيران ستستمر لعدة أيام</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/naya_foriraq/86590" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86589">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
البيت الأبيض:
طهران أخلت بمذكرة التفاهم وأطلقت النار على السفن و
قتلت جنودا أمريكيين
.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/naya_foriraq/86589" target="_blank">📅 01:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86588">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu9fGDNEs-NbzdVh_tb4hQ2k7ucgQ25sRmixv4e7ZNm_qOzZ2I0fqPLYcQnupDaUD2CoglJ_C8Ltsdj588hNGx8mJET0AXMZJiTnO-awkBmT8AhIFtpf4Nm9qFI_vASklua9ntPCvBf26ey9BJxOFReNLHAamgAPw_MqZxYOtbmy-GF3QS0bpBOx9TB9Z4lEsAFpGfryQtnWYLKH0ojNIniKfrJIfK6-fN3qHnr5rjkfd_SosX8O8QlQqMLgTvUIS3iMW4qPnFNEs_lYieO6ZlDkArASb_kq_fRpXR3rdiPUGEOmW5LrGsl5VM19uoxnuFm_9ZIC5rRN445_oYpf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الأمين العام للمجلس الأعلى للأمن القومي الإيراني:
إن استمرار الحصار البحري وإشعال الحروب الذي يمارسه النظام الأمريكي سيؤدي إلى تشديد الحصار على مضيق هرمز وإغلاق المضائق والاختناقات الأخرى. وسيدفع الاقتصاد العالمي وسوق الطاقة والناخبون الأمريكيون الثمن.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/naya_foriraq/86588" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86587">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔹
مسؤولين أمريكيين وأوروبيين:
روسيا تزود إيران بمراقبة الأقمار الصناعية والاستخبارات الإلكترونية التي قد تساعد طهران في تحديد مواقع القوات الأمريكية، وتحسين دفاعاتها الجوية، وتشويش الأسلحة الأمريكية الصنع.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/86587" target="_blank">📅 00:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86586">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔻
تسجيل لمحادثة تحذيرية من قبل القوة البحرية التابعة لحرس الثورة الإيرانية، وعودة سفن النفط من مسار غير قانوني وغير مصرح به.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86586" target="_blank">📅 00:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86585">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
مسؤول أمريكي:
ترامب أمر بجولة جديدة من الضربات ضد إيران ستستمر لعدة أيام</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/86585" target="_blank">📅 00:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86584">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
🇮🇶
وسائل إعلام خليجية:
القوات الأميركية تبدأ الانسحاب التدريجي من إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/86584" target="_blank">📅 00:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86583">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الاعلام الغربي:
‏تستعد الولايات المتحدة وإسرائيل لقصف أهداف متعلقة بالطاقة في إيران في أقرب وقت ممكن نهاية هذا الأسبوع.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/86583" target="_blank">📅 00:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86582">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇾🇪
العميد يحيى سريع:
في إطار تثبيت معادلة "الحصار بالحصار" ونتيجة لإحكام قواتنا المسلحة للحظر البحرى على سفن العدو السعودي النفطية تم إجبار ثمان سفن نفطية سعودية على تغيير مسارها باتجاه الرجاء الصالح.
تؤكد القوات المسلحة أنها مستمرة في عملية الحصار للعدو السعودي وأن يد القوات المسلحة ستطال سفنه بإذن الله حيث ما تمكنت من ذلك.
تحيي القوات المسلحة بإعزاز وتقدير شعبنا اليمني العظيم المؤمن المجاهد على خروجه المليوني في الساحات والميادين رغم غزارة الأمطار ونؤكد له أننا لن نألو جهدا في إنهاء الحصار عنه واسترداد كل حقوقه بإذن الله وقوته.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/86582" target="_blank">📅 23:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86581">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
ترامب: لو لم يكن لي، لما كانت إسرائيل موجودة اليوم. لمَا كانت موجودة، وكانت إيران على بعد أسبوعين فقط من امتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/86581" target="_blank">📅 23:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86580">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇧🇭
إدارة مطار البحرين الدولي تُصدر تنبيهات احترازية للمسافرين والعاملين في المطار.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86580" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86579">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
ترامب: أنا أقوم بعمل أكبر بكثير مما كنت قد أعلنت أنني سأفعله. كنت سأتدخل وأدمر قواتهم العسكرية، وأدخل، وأخرج.  ثم أدركت أنه إذا فعلنا ذلك، فعلينا أن نحافظ على هذا الوضع بطريقة ما. وإلا، فسوف يعيدون بناء ما دمرناه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86579" target="_blank">📅 23:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86578">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
🇺🇸
‏ترامب: ‏مع إيران، وبحسب التعريفات، فقدنا ما بين 16 و18 شخصاً، و‏نفس الأشخاص الذين أبقونا في فيتنام لمدة 21 عاماً يشتكون الآن من إيران.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86578" target="_blank">📅 23:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86577">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
ترامب: "هل تريدون أن تنتهي الأمور بسرعة؟ أعطوا الأشخاص المضطربين أسلحة نووية. ستنتهي الأمور بسرعة كبيرة."</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86577" target="_blank">📅 23:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86576">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90150a3aec.mp4?token=IU1fx1jfLsn27_i0DhsxwvcGyv4OYuKAEni55SnXdq3qgP3s9NeRA03MdM4BYBzKfqLZt9SI7ItriDNPCh3kFRdaFt7kB1qvc_jteDCTrmm74bNsLOyAO10k6UCDEn6EpycvIIux2LbycqRv2sVAa9Y7_T680BoLLlBdqGSvoxX2ruOKEzhWWPX3jdyyTv2NPC-f0vXQNG7YvWVsI3dMAUDFw6bquheOXFo4Kxbjl0vrU_hoDkdvPsjE8N8HyqneYU2qCjWsDCb647DMpadUzaPIb_r4-CeConQKTogcKkq07L8p6Kgax2qcUN7Mws9mON_DM0rBzkUQhSD8l1uo8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90150a3aec.mp4?token=IU1fx1jfLsn27_i0DhsxwvcGyv4OYuKAEni55SnXdq3qgP3s9NeRA03MdM4BYBzKfqLZt9SI7ItriDNPCh3kFRdaFt7kB1qvc_jteDCTrmm74bNsLOyAO10k6UCDEn6EpycvIIux2LbycqRv2sVAa9Y7_T680BoLLlBdqGSvoxX2ruOKEzhWWPX3jdyyTv2NPC-f0vXQNG7YvWVsI3dMAUDFw6bquheOXFo4Kxbjl0vrU_hoDkdvPsjE8N8HyqneYU2qCjWsDCb647DMpadUzaPIb_r4-CeConQKTogcKkq07L8p6Kgax2qcUN7Mws9mON_DM0rBzkUQhSD8l1uo8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار عسكري كبير في حي جميلة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86576" target="_blank">📅 23:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86575">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ce236252.mp4?token=nbpjqwVinx-e-iQNxmREUrl1RDOLDxZ6h6wKJMG0Jsx4r-PMU_bZrLAEf4Kd0SNKUqFpv93YZSWbO7QcZ53hxmewQHgIYfJz797OtNBpTplXrqFV0aOecseO2o1EmC7-ZtrLG9j2VT1xOYyOfU5M81c4c3edL9QKhF1W3caueLoBKm3tkz8-mvgm5wNe_sJ1xQxrkfGFroqj20VMjumoAPHJzt9gXAOJbziwqM21rhW-o3cZ5eE9vivVEXzHbXW9v6N0MTHN-4a6uzX4f9wh0Dwi_oJsXPH0zJP1uJifw2B4FtDEKdr_D9hDnXjit6Vp9gmwlmAx8210RzqKl5TGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ce236252.mp4?token=nbpjqwVinx-e-iQNxmREUrl1RDOLDxZ6h6wKJMG0Jsx4r-PMU_bZrLAEf4Kd0SNKUqFpv93YZSWbO7QcZ53hxmewQHgIYfJz797OtNBpTplXrqFV0aOecseO2o1EmC7-ZtrLG9j2VT1xOYyOfU5M81c4c3edL9QKhF1W3caueLoBKm3tkz8-mvgm5wNe_sJ1xQxrkfGFroqj20VMjumoAPHJzt9gXAOJbziwqM21rhW-o3cZ5eE9vivVEXzHbXW9v6N0MTHN-4a6uzX4f9wh0Dwi_oJsXPH0zJP1uJifw2B4FtDEKdr_D9hDnXjit6Vp9gmwlmAx8210RzqKl5TGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب
: "هل تريدون أن تنتهي الأمور بسرعة؟ أعطوا الأشخاص المضطربين أسلحة نووية. ستنتهي الأمور بسرعة كبيرة."</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86575" target="_blank">📅 23:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86574">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اندلاع حريق حريق مجهول قرب القاعدة العسكرية في مطار بغداد " مطار دبلن "</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86574" target="_blank">📅 23:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86572">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
استنفار بين البعثية للبحث عن الشخص الذي ظهر في مقطع الفيديو بعد مطالبته بمكافأة قدرها 33 مليون دولار زاعمًا أنه أبلغ عن مكان اختباء صدام حسين(
الحفرة
).
كفمي كفمي شوكلاطة
😆</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86572" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86571">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
‏تعرضت 67 سفينة على الأقل للهجوم أو الاقتحام، وقُتل 17 بحاراً، منذ بداية الحرب مع إيران.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86571" target="_blank">📅 22:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86570">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5605707ff5.mp4?token=TLMQ_ZnBd--qsBkJtOoz8bDKsLduy4rJxa9xYCSqz1WCvU-6vTrzbqV6fsxBVDHMyrUqtQRYBGnKu6rgP85yo6xKN_HBb4UZklAs3TOS7baS-NgKX-jox8rIHtZfL4Y4XKl3j4sd50eWSno-ahiBMEgB-4CNvV03xBiDKd0zIA2mM3Gjrlsibm6f5J0x1G4RadwIsViX9c2vNANM8LYzkbSiCamQROWP0V2lUk74xZ96va77vZxIsAn9eBIeWafo0OSsrBYXDYgW8_73Ejif6Vy3MkZphp6bewGRgJQfjXbBxbAbRui7WjlM2uobswHdB04XlmOscp6uG1iEu5taDZNJ2-teutl50TRveo6ceUv7MKpYfNKHJUFwzTHHBEkHw5yIMHkcAgC7xYnP-shqQ3dQqh8eKNnmEx9qO4oLrd_CnqnFT5dAFw4-zdyn9C2MQ47ZbrzG8o3cxViFn3NDIUd7BIuVCkb7ErBy_DTJCyR91uq-pDfd7_x3SOdzjdPw_05oEBR9VIGzHiNZVP2H2sfTp_kQCIPUpvudQz8UZJq0lagHCtyIDkLH4gy6pANun1VVMdWqHk15v61GfjuLJt0JS2eQct25XUjqp0KsloSsUqlBhxu12qIOrgmrszu3t-NimUO5kNvK3XyYiUT-AYqycuKjjgFb7cqo0SuQcNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5605707ff5.mp4?token=TLMQ_ZnBd--qsBkJtOoz8bDKsLduy4rJxa9xYCSqz1WCvU-6vTrzbqV6fsxBVDHMyrUqtQRYBGnKu6rgP85yo6xKN_HBb4UZklAs3TOS7baS-NgKX-jox8rIHtZfL4Y4XKl3j4sd50eWSno-ahiBMEgB-4CNvV03xBiDKd0zIA2mM3Gjrlsibm6f5J0x1G4RadwIsViX9c2vNANM8LYzkbSiCamQROWP0V2lUk74xZ96va77vZxIsAn9eBIeWafo0OSsrBYXDYgW8_73Ejif6Vy3MkZphp6bewGRgJQfjXbBxbAbRui7WjlM2uobswHdB04XlmOscp6uG1iEu5taDZNJ2-teutl50TRveo6ceUv7MKpYfNKHJUFwzTHHBEkHw5yIMHkcAgC7xYnP-shqQ3dQqh8eKNnmEx9qO4oLrd_CnqnFT5dAFw4-zdyn9C2MQ47ZbrzG8o3cxViFn3NDIUd7BIuVCkb7ErBy_DTJCyR91uq-pDfd7_x3SOdzjdPw_05oEBR9VIGzHiNZVP2H2sfTp_kQCIPUpvudQz8UZJq0lagHCtyIDkLH4gy6pANun1VVMdWqHk15v61GfjuLJt0JS2eQct25XUjqp0KsloSsUqlBhxu12qIOrgmrszu3t-NimUO5kNvK3XyYiUT-AYqycuKjjgFb7cqo0SuQcNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستمرين بالمواجهة لن نخضع ولا نركع إلا الله .. والسلاح هو ملك وخزينة للدفاع عن الشعب العراقي والمستضعفين
المقاومة الإسلامية كتائب سيد الشهداء</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86570" target="_blank">📅 22:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86569">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
يواجه البنتاغون حقيقة متنامية بعد أشهر من القتال في إيران.
يتقلص مخزون أمريكا من صواريخ الاعتراض الدفاعية لدرجة أن المخططين العسكريين يدرسون ما إذا كان بإمكانهم مواصلة الدورة الحالية من الضربات الانتقامية المحدودة.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86569" target="_blank">📅 22:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86568">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
العقود الآجلة للخام الأمريكي ترتفع 1.29% لتبلغ عند التسوية 84.67 دولار للبرميل.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86568" target="_blank">📅 22:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86565">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fG43g8zOAmay9RtgbzqdtGYiXmdAcaf6RZGPUG_wrxfj39xHI0kVit1LpFK1iRzyK9j-RDUPIuOL934LV8qhIXiMI0eUeqn_z7W_rQR0kHov4oddn1U0NtF-h37hcujzjq46l-xC48lj8pnUrw44HXOXd3vV45pIE0Kg6Rw_qVUEhmddsY1eE2P_zhlAr3adT0QtLqBuMm_Fhr3EoT5sPgZykezUwbGSxaOF36d2zNsEK6Xro0AR_yQQ4nqIPport6NT1Y3e9dAUknz5daj1EheWOCpww28-5opJzshNkStr-NkjhpwtBtR18vB8EFVG3m600c6FXfnRBwD540JkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLCh3DDhdycR1JGxvy151wyGqLgDExisK1QSUeXJu8tN9to_ZTFRnCrLpTrtOd_BN57kYQb_8uyK62XwVG8IphoMNgs-WZwNZ_NqJ-qY95vjut0s-x8BI7qgrTUDK9PZNMfDnBW1oOcZcSWEZ8QyEGxbEEkh4gLWBxRcciBDlniFg-NK0R0eiiSQOzr7Q8tyO5ACtpsaYoR2fZ0RFMR4vr-ieAguDlN7bNmO0I8Wxcf5ZrhuWdkFYTx10UlAZ_Kr746efqZj4u82RE79G3E-VFGhu0PhQAAQMgF_ue3mMVVdcytcz9xJoNwtvB1wwe1gqevwTMyS9dNArDdRB9DVyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXZY6OzITKJZVnssCg5wFL6oypOa2qgKgUBJEc21goSeD0mFv3UT3uomkGrjh13kaN6Ds1M0xgRrsSQXDilwzZ-9diANxNRN3i7wopI_oRrYJRq03N9ErRic6nsgMVVk5hHHb8jgmv8sRYVqVUqXl8FByXpgqhKAXzSu8rpGljJXGjsmuZNT3PkAILctF__SZYz3zm0yqjz54rWSDmPJNxODbA5SF9EiMJjPjoRvyiujqsdGh5rf4Y0qSPA87G8ldS7fXKZZDmUTCaBx_rOmhyKbbOzCM1fcaflXxtPmjSQDufbRQpPqObMhfvtPqPl26HiELVoBDB6qzgJ-KnGoBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤡
🏴‍☠️
🇮🇶
خلايا اوكرانية تنفذ هجمات في العراق وتُنسب للفصائل.. مستشار الأمني القومي يكشف سراً "لم يسمعه العراقيون" من قبل</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86565" target="_blank">📅 21:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86564">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e0d6ec59a.mp4?token=ePzGWfHt4Rj6W0NH2UcPniOcnB0LFcjmrJVFu9lcMh-1Uyes7hST-7H3a71jb6pNQQyj0htXaOA-y-YoIDuWEfPTfTzOCdlQlpMmCtxNgQAb1TutB1PQ_rw2RHWibgWM9FE1pKIbSNsAL9x7NsbkLFolz25AZd__D6WEjy6hf-JUfFoom3oJ2sUY2X0qCfkAgV2kBw29yfBmQiFM1IB8v2x3bOWlSKulYF8fuwZ79UrI507NH9dUmc7PjFYynj5Vx2eJlal7ZTl91VaG9QPzBIWSVP_k_vlgwyCP6oyxwviUzIPRLt9a6uND8AS2UtWD4IBk4T0NbuJcAVGhuU0h8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e0d6ec59a.mp4?token=ePzGWfHt4Rj6W0NH2UcPniOcnB0LFcjmrJVFu9lcMh-1Uyes7hST-7H3a71jb6pNQQyj0htXaOA-y-YoIDuWEfPTfTzOCdlQlpMmCtxNgQAb1TutB1PQ_rw2RHWibgWM9FE1pKIbSNsAL9x7NsbkLFolz25AZd__D6WEjy6hf-JUfFoom3oJ2sUY2X0qCfkAgV2kBw29yfBmQiFM1IB8v2x3bOWlSKulYF8fuwZ79UrI507NH9dUmc7PjFYynj5Vx2eJlal7ZTl91VaG9QPzBIWSVP_k_vlgwyCP6oyxwviUzIPRLt9a6uND8AS2UtWD4IBk4T0NbuJcAVGhuU0h8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ارتفاع اعمدة الدخان من وسط القاعدة الاميركية في ولاية كاليفورنيا. وتدمير طائرة F35</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86564" target="_blank">📅 21:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86563">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67da2ed6f7.mp4?token=evRh-32yGc328owZK_eOHlB2NeNlGoEiy084JoKU4GLh09-JyCjsReeMuMsOXFy3CQ70L6QnAsCU9Bv6cnoZvo0-F2OgddIvqQQ6hNrornqo3pADYHZRdUBE3SJyu7FQbwi0TDJIVWHzce1EYZFOOqOP81347i5Rgj7jdT7cq_wunoa1115Ia5ggInVa0hqElbPqNMYbQ7qTEUSmtdgGkomcMhGAXVEiW-U2y-hh6La5vthC3E8K9pRSff9fg9pPP_VTJSRsfsiMfHpUVgSeOlQ53YVR6LIbvXAeX7cETFidteuebWW80nGG4UgKcbaPS5EzSXbpyxd9PinvckP26g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67da2ed6f7.mp4?token=evRh-32yGc328owZK_eOHlB2NeNlGoEiy084JoKU4GLh09-JyCjsReeMuMsOXFy3CQ70L6QnAsCU9Bv6cnoZvo0-F2OgddIvqQQ6hNrornqo3pADYHZRdUBE3SJyu7FQbwi0TDJIVWHzce1EYZFOOqOP81347i5Rgj7jdT7cq_wunoa1115Ia5ggInVa0hqElbPqNMYbQ7qTEUSmtdgGkomcMhGAXVEiW-U2y-hh6La5vthC3E8K9pRSff9fg9pPP_VTJSRsfsiMfHpUVgSeOlQ53YVR6LIbvXAeX7cETFidteuebWW80nGG4UgKcbaPS5EzSXbpyxd9PinvckP26g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات داخل قاعدة عسكرية أمريكية في كاليفورنيا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86563" target="_blank">📅 21:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86562">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات داخل قاعدة عسكرية أمريكية في كاليفورنيا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86562" target="_blank">📅 21:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86560">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlnFTEHyag_86UGniRf_SdiaJW5lzuqMkofFi3RtbAsAcxkngRjf_lBriTmgiiPT_n0s2Gx-wugv56sl8LZPaCMpDuzoPSnNYLbA7LMJ3iHUUK4uSsqr4GoARl4VLIPTn4nkmn25tN2n90dcxiuHyu9kI3oSyTUHFTsWff2ZD52fDa0L4PO0cMMk36zqXBwCOUmIMWm2HNXoEbxKM-Xm393fn938CZwiGCv7Xhm47i5hTFJDtl_WwbeIe4DKxsOfUPWE0BdXacIfdlTEr3y08xhxIFUc7h811dwa7lJ2FAE45Aeq1sC_bpWBluqN5Vk9yX4ah6gCqdYaC9ZalgqQeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصرنا
😆</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86560" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86559">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4999db8b.mp4?token=dftjh-MNby1ecaPWecaT8yRxToOUGRAk7KjI2LnlcmxHGFD6807VJ-e8l704oj9dw13WP581GFrrPhJMxWcslyRf5DbWzPEk3Pz813TMnQOBmyCfwyfIijIdeQsvS1JuM4sxKrTYBFETq4Vof2Xu4plFLf7fMKCqffp9RNH8SO1d3puBqJ8XWEWOxpVhvcm4Lh-3xd4qe2YiUZkYxPGpEYP7DhN-Rp7PZydvwlQm7pY3ipC8MB4zAcWw2kffQ3FvJKh1OArZaVyJzT6m4FpggnZ3AHWETHFuE06XmFjjhDmpo31gVE9aBb69JX5rnrms5a6oAC_Xv9YfIsL4PSJEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4999db8b.mp4?token=dftjh-MNby1ecaPWecaT8yRxToOUGRAk7KjI2LnlcmxHGFD6807VJ-e8l704oj9dw13WP581GFrrPhJMxWcslyRf5DbWzPEk3Pz813TMnQOBmyCfwyfIijIdeQsvS1JuM4sxKrTYBFETq4Vof2Xu4plFLf7fMKCqffp9RNH8SO1d3puBqJ8XWEWOxpVhvcm4Lh-3xd4qe2YiUZkYxPGpEYP7DhN-Rp7PZydvwlQm7pY3ipC8MB4zAcWw2kffQ3FvJKh1OArZaVyJzT6m4FpggnZ3AHWETHFuE06XmFjjhDmpo31gVE9aBb69JX5rnrms5a6oAC_Xv9YfIsL4PSJEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إنهم يتحدثون عن البرنامج النووي لمدة سبع ساعات. وأقول: "لماذا سبع ساعات؟ يمكنكم إنجاز الأمر في خمس إلى عشر دقائق."</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86559" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86558">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
ترامب: إنهم يتحدثون عن البرنامج النووي لمدة سبع ساعات. وأقول: "لماذا سبع ساعات؟ يمكنكم إنجاز الأمر في خمس إلى عشر دقائق."</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86558" target="_blank">📅 20:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86557">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7828268882.mp4?token=PiueIPBB4x9fMvglSjl9XNR5LGp53gkIVBdEf0ilqwwUYq9upZDLrfb7HXyTWSKZJuXrEHKHB3DU8I3hTqOGNXpg5VGGeL7F9NUartK4q0JHfuo0m_Wh2rmS5VYGBVCdlA5RPKvMqf7tdqdE96AXaaKwJshUHd8OjOw_rpMDfpEs12RnqOGnnlxBmk_MS9oK7Y7rCH0ulNfRA1Iibhb2YR66lm90rKb5RMXcuYNMcAEPuM9ZtBEZ8cRZa8thOfQxKFVIed5tr5ghquXHql_dkIXawbtw_toBTQqtRdaC4FsG3VHt5zhFYbw770cPs1lddxSQsXOL3CgqsRnneyATUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7828268882.mp4?token=PiueIPBB4x9fMvglSjl9XNR5LGp53gkIVBdEf0ilqwwUYq9upZDLrfb7HXyTWSKZJuXrEHKHB3DU8I3hTqOGNXpg5VGGeL7F9NUartK4q0JHfuo0m_Wh2rmS5VYGBVCdlA5RPKvMqf7tdqdE96AXaaKwJshUHd8OjOw_rpMDfpEs12RnqOGnnlxBmk_MS9oK7Y7rCH0ulNfRA1Iibhb2YR66lm90rKb5RMXcuYNMcAEPuM9ZtBEZ8cRZa8thOfQxKFVIed5tr5ghquXHql_dkIXawbtw_toBTQqtRdaC4FsG3VHt5zhFYbw770cPs1lddxSQsXOL3CgqsRnneyATUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: الدبابات الروسية كانت متجهة إلى كييف، لكنها علقت في الوحل، قرر أحد الجنرالات السير في الوحل بدلاً من السير على الطريق السريع، حيث كانوا يتقدمون بسرعة.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86557" target="_blank">📅 20:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86556">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf2738436a.mp4?token=N7-Own6IxIYzlpx0xmO_INPUzyziO4u36YeBvF4KwOsxcLCBEWkktTWhJmf5NusZZTby8EXG5aSldAIvxFIKrc52fCcjPv059PEk2iQRqfAGGtXAIeovRq6HxzyVLm7yTII87Y88m2pX51RWbk63YsuO99S6sRapQN4-qJxgsOmhIQghJk_ENoUrmpgPJQqZC7Iz40c9y8XgKFKOFynfeNSgFxgTdSi1PWg5OFyYsK_PAC-dqCJm73wQQQv10igctHtGoXNRg9_xtOkmbj9QuSb1yaL0Fvz2kx5g5dm-K4HNYNfgIracgx7DMvIoLBvOh-Ai3ffl7J1EOzgPKdCw1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf2738436a.mp4?token=N7-Own6IxIYzlpx0xmO_INPUzyziO4u36YeBvF4KwOsxcLCBEWkktTWhJmf5NusZZTby8EXG5aSldAIvxFIKrc52fCcjPv059PEk2iQRqfAGGtXAIeovRq6HxzyVLm7yTII87Y88m2pX51RWbk63YsuO99S6sRapQN4-qJxgsOmhIQghJk_ENoUrmpgPJQqZC7Iz40c9y8XgKFKOFynfeNSgFxgTdSi1PWg5OFyYsK_PAC-dqCJm73wQQQv10igctHtGoXNRg9_xtOkmbj9QuSb1yaL0Fvz2kx5g5dm-K4HNYNfgIracgx7DMvIoLBvOh-Ai3ffl7J1EOzgPKdCw1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
المراسل: ذكرت أن إيران لا تزال لديها بعض القدرات. هل يجب على الأمريكيين الاستعداد لمواصلة هذه الهجمات المتبادلة حتى تصبح إيران غير قادرة ببساطة على الرد؟ ترامب: ستزداد قوتهم قليلًا، ربما الآن، ولكنهم سيصبحون أضعف. نعم، بالطبع. يجب دائمًا أن تكون حذرًا.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86556" target="_blank">📅 20:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86555">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb7c06f17.mp4?token=ctxmor6Bctwiw1SGkDeAeRHWLgOm-cnd8ofunSY_Gval5HyWZDow7R_fX5-BdJoL5vNn49gc0cvLZnh_eJ1vdnsoCbW_MiIPe3QPiYKROFBLX3hl64gPlgtjX3AcUPs_uPd-p6HhzZ2hfvKU8OAKGyeeEtuVl05SofVVeg0IOXY4dDxqiFqQYHI-wkObfAha003SYDQSEmiPMk-0cKqX-RBIA4VR5tDBMkFHnHToXq1j_ziSSZoLhyPM6gLjVcs_4F_MLzWPX-_OYlbA5sjk1eNcmMpgogcYLCGM-2MsBy7xQ5z3nEpwkpIp02dVmkNjUR36jOhwSDto_YkuJNLNMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb7c06f17.mp4?token=ctxmor6Bctwiw1SGkDeAeRHWLgOm-cnd8ofunSY_Gval5HyWZDow7R_fX5-BdJoL5vNn49gc0cvLZnh_eJ1vdnsoCbW_MiIPe3QPiYKROFBLX3hl64gPlgtjX3AcUPs_uPd-p6HhzZ2hfvKU8OAKGyeeEtuVl05SofVVeg0IOXY4dDxqiFqQYHI-wkObfAha003SYDQSEmiPMk-0cKqX-RBIA4VR5tDBMkFHnHToXq1j_ziSSZoLhyPM6gLjVcs_4F_MLzWPX-_OYlbA5sjk1eNcmMpgogcYLCGM-2MsBy7xQ5z3nEpwkpIp02dVmkNjUR36jOhwSDto_YkuJNLNMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترمب: إيران تريد دائما التفاوض وتريد التوصل إلى اتفاق معنا، ويمكن التوصل لاتفاق مع إيران،ويتكوف وكوشنر وفانس وروبيو يشاركون في محادثات متعلقة بإيران.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86555" target="_blank">📅 20:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86554">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a25f78e699.mp4?token=dp6mUpZK9U2DmNRKAxzgXHmeKEgOtgfrSy7oub5In8AiLiFz5XCJnpDXh1qoK69QpnjE2RjwVkH4LBE9bA9FONqeef5eCQz7ccgkYv0oZW9wSPjToc-eYkRyTBPyP99ZKj0exQIwsGnmf-WgvxBgZ9JLTuZUfLHduf0wNaYV-2i3MxpWaGdIJDJZzQo_0VjWGdsmhDS7hIlmB-DWDBY5L_n9pdXx3SFNVhd9ASCPEL8kbwYG90dQVRahIdhlUIJSbb91RLtlM9xfN339I94YXZagWBYZeQdmg_PUi81V9qKCjdJsd_sFjMaNmmYV8obMd6ptHRsRtwOZSPQ8E2DNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a25f78e699.mp4?token=dp6mUpZK9U2DmNRKAxzgXHmeKEgOtgfrSy7oub5In8AiLiFz5XCJnpDXh1qoK69QpnjE2RjwVkH4LBE9bA9FONqeef5eCQz7ccgkYv0oZW9wSPjToc-eYkRyTBPyP99ZKj0exQIwsGnmf-WgvxBgZ9JLTuZUfLHduf0wNaYV-2i3MxpWaGdIJDJZzQo_0VjWGdsmhDS7hIlmB-DWDBY5L_n9pdXx3SFNVhd9ASCPEL8kbwYG90dQVRahIdhlUIJSbb91RLtlM9xfN339I94YXZagWBYZeQdmg_PUi81V9qKCjdJsd_sFjMaNmmYV8obMd6ptHRsRtwOZSPQ8E2DNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب بينغ بينغ بينغ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86554" target="_blank">📅 19:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86553">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
ترامب : "إيران كانت تمتلك أسلحة دفاع جوي متطورة جدًا، ولكنها لم تكن فعالة."</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86553" target="_blank">📅 19:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86552">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377310bac7.mp4?token=aqZGWag7WLUfEtkbanj8g6CIUf9qwJYVGoDUZHKLOpztcwd2Zmcl928fQwJ7ipL3k_MRUV-iEa6RxAhzedg69vWXC9eytHXmtQ0ALGge5qUBF6LAuvXFhXynn0AAVXlp5AR6eAqkaiWshYnWc0aq0q5F1mreA1yAuu0FzY685c2YevXOaSEY59zoLqZxfrioZJFoipjaG4S_brRwM2nXjB4VmoZtV4MJozZD68R2-6wZpaDvnPv-BCf6UA91jiHXdK-YQpdm4pf7DWkc7dN1fVHVfO_18Ee9gxRpQ_g_NMIgJGmUJbwNZq_Tza68h7bILWHX0cgXyD4cvQLw2FsWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377310bac7.mp4?token=aqZGWag7WLUfEtkbanj8g6CIUf9qwJYVGoDUZHKLOpztcwd2Zmcl928fQwJ7ipL3k_MRUV-iEa6RxAhzedg69vWXC9eytHXmtQ0ALGge5qUBF6LAuvXFhXynn0AAVXlp5AR6eAqkaiWshYnWc0aq0q5F1mreA1yAuu0FzY685c2YevXOaSEY59zoLqZxfrioZJFoipjaG4S_brRwM2nXjB4VmoZtV4MJozZD68R2-6wZpaDvnPv-BCf6UA91jiHXdK-YQpdm4pf7DWkc7dN1fVHVfO_18Ee9gxRpQ_g_NMIgJGmUJbwNZq_Tza68h7bILWHX0cgXyD4cvQLw2FsWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول إيران: "نحن نريد فقط الفوز.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86552" target="_blank">📅 19:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86551">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=dZ0mTUz4j_DINnOx8cyaT2wVL7dgfzDr7tR_O-G9XVkRhfaQPcRzjP_akBjT6dIBMmq-Hd235QYTjmxymssx2MpTshZmkWkcAUKyhTIc8H5h9CPpLHmm017aP0l4we3UedHCbeXK0jm5xX9q3HO0Z4h4_dO3iYogUo4XESUiowUzSSZzWdtyifdAMonYviz3NVY6dMMA0rqNdxK9p-cnfaLenVf0jrJbE-KNgdmZ12DgU7bNwd_p0HYEQESPWoH9OQorT6yJuX5mS43aV5MfKShgkH7C-3jyU7So4MfPPZJswqaXzvAmh-nZg1Eikkq-lkQ9f6P-TkCu7Klrl8JmAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=dZ0mTUz4j_DINnOx8cyaT2wVL7dgfzDr7tR_O-G9XVkRhfaQPcRzjP_akBjT6dIBMmq-Hd235QYTjmxymssx2MpTshZmkWkcAUKyhTIc8H5h9CPpLHmm017aP0l4we3UedHCbeXK0jm5xX9q3HO0Z4h4_dO3iYogUo4XESUiowUzSSZzWdtyifdAMonYviz3NVY6dMMA0rqNdxK9p-cnfaLenVf0jrJbE-KNgdmZ12DgU7bNwd_p0HYEQESPWoH9OQorT6yJuX5mS43aV5MfKShgkH7C-3jyU7So4MfPPZJswqaXzvAmh-nZg1Eikkq-lkQ9f6P-TkCu7Klrl8JmAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول إيران: "نحن نريد فقط الفوز.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86551" target="_blank">📅 19:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86550">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1facef9bcc.mp4?token=Mn4zSdNvF3BmZE60QAxAhCNCnZn_39_2Iu-wOY0Q0LbBUcVn1OsHhWFo96bgmvf2iM1OhG3GgJvNJi5FkEM8N2pBLnrYyxkdbt-8ylqOHlip5NHXnVMgUwIoJrgEqwXrtqkljx0qGK-RvCnAjfiwA1vtCdQQkbqcbEyCFhJ898LofGgstge3p2J23-FMR44GwilRF_bqltwLZlkb8seuK_sbfWjDt8VmNrMuNDsKF-q-gg1QzyUWQ7KuwyamZSGRFfWrQBwwkUZc6xV_OVHklkAHKuEtdGK1j8ZaFQnZZtjZK0EmbGS_JxQygkaMbsmHL1HEjcYOgEMfYO-9sI9hJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1facef9bcc.mp4?token=Mn4zSdNvF3BmZE60QAxAhCNCnZn_39_2Iu-wOY0Q0LbBUcVn1OsHhWFo96bgmvf2iM1OhG3GgJvNJi5FkEM8N2pBLnrYyxkdbt-8ylqOHlip5NHXnVMgUwIoJrgEqwXrtqkljx0qGK-RvCnAjfiwA1vtCdQQkbqcbEyCFhJ898LofGgstge3p2J23-FMR44GwilRF_bqltwLZlkb8seuK_sbfWjDt8VmNrMuNDsKF-q-gg1QzyUWQ7KuwyamZSGRFfWrQBwwkUZc6xV_OVHklkAHKuEtdGK1j8ZaFQnZZtjZK0EmbGS_JxQygkaMbsmHL1HEjcYOgEMfYO-9sI9hJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
اقلاعات متتالية من قاعدة الاحتلال الاميركي موفق السلطي في الاردن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86550" target="_blank">📅 19:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86549">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
وزير الحرب الاميركي بيت هيغسيث: هل تتساءلون عن سبب عدم مشاركة الحوثيين في هذا الصراع، على الرغم من أنهم عملاء لإيران؟ ذلك لأنهم شعروا بوزن القوة الأمريكية لمدة 45 يومًا.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86549" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86548">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
القائد العام وجه برفع مستوى الإنذار والجاهزية في جميع المعسكرات والقواعد
القائد العام وجه بالخطط الاستخبارية الوقائية لإحباط أي استهدافات أو محاولات اختراق
توجه لتسريع خطة التجهيز والتسليح الخاصة بمنظومات الرادار والكشف المبكر والدفاع الجوي
حماية الأمن الداخلي مسؤولية حصرية لمؤسسات الدولة العسكرية والأمنية
بعض الأطراف الخارجية تحاول إقحام الأراضي والأجواء العراقية في حسابات الصراع
منظوماتنا العسكرية والأمنية تتصرف بأعلى درجات الانضباط والجاهزية</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86548" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86547">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488504489f.mp4?token=bAyVldTjki_0m4UbbcXzerHeojwIm5YgrkuaP8cxf3pKOMcvKxvILmZRteGcBT5bx-QGOTQivKksn-vtaIwjrD4AuHnLmVCjKeQXb-5Pgr1Ad1sicozbF1x1zpasCIOTT8tjlz1zX_r9xxfJEZ6mp4OiscnzZBJE6TEQ3C99k19gKyz4eT7aA_rxvVyTHuDq8P_Yd0HrOucKXppryyDY4u6aB-2o--6R6jNXh3unpLJEW0vARjJOS5n43pdnBL_0FgqHqs9XcFlT2cFj59DT05zI0KLGU5JScWozefD2yio8iwV0lb9Xf2Dl6NiF_8NrJ7W0h5zSod9A8DMox9XQQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488504489f.mp4?token=bAyVldTjki_0m4UbbcXzerHeojwIm5YgrkuaP8cxf3pKOMcvKxvILmZRteGcBT5bx-QGOTQivKksn-vtaIwjrD4AuHnLmVCjKeQXb-5Pgr1Ad1sicozbF1x1zpasCIOTT8tjlz1zX_r9xxfJEZ6mp4OiscnzZBJE6TEQ3C99k19gKyz4eT7aA_rxvVyTHuDq8P_Yd0HrOucKXppryyDY4u6aB-2o--6R6jNXh3unpLJEW0vARjJOS5n43pdnBL_0FgqHqs9XcFlT2cFj59DT05zI0KLGU5JScWozefD2yio8iwV0lb9Xf2Dl6NiF_8NrJ7W0h5zSod9A8DMox9XQQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب :لديهم بعض الصواريخ المتبقية، ولكن لديهم عدد أقل بكثير مما كان لديهم قبل أربعة أو خمسة أشهر، قدرتهم الإنتاجية قد تضاءلت إلى حد كبير. قدراتهم في مجال الطائرات بدون طيار قد تضاءلت إلى حد كبير، ولكن لا يزال لديهم بعض القدرات.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86547" target="_blank">📅 19:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86546">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/728d2b7bc8.mp4?token=oKu_hSPbMJ4KknsqoPmsPyV8y3Yzp2Lpa0wPEcQYVf3Fcui2vKmD-NI6GUodOCdU4mbIlMlkTuTeB4AFAw0PtebZvlnjz7oA4Nk_sCHLJpYfNIBAG3Tt7D3DYOUnCZ3ZO3rVQOBHOHXBhEayu4VmhRMTHvW2bUKBlUprjrr6rIS2eRDAJ_9Yx5Bjd8l0eiry6EW7rdMtiIteSF5-52MTC2-liI5CEJ5TsDBhSs3Z-DDaEIq3W1H9g_EgS4Cd5BfVqraD9cUtxBSYitmrllS5NxWw-_UvnRNNk0KsfpM3I7MMPrVqgRRM9hhGBx12Llf_5aym1b-wRtA3SmrfGo_ZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/728d2b7bc8.mp4?token=oKu_hSPbMJ4KknsqoPmsPyV8y3Yzp2Lpa0wPEcQYVf3Fcui2vKmD-NI6GUodOCdU4mbIlMlkTuTeB4AFAw0PtebZvlnjz7oA4Nk_sCHLJpYfNIBAG3Tt7D3DYOUnCZ3ZO3rVQOBHOHXBhEayu4VmhRMTHvW2bUKBlUprjrr6rIS2eRDAJ_9Yx5Bjd8l0eiry6EW7rdMtiIteSF5-52MTC2-liI5CEJ5TsDBhSs3Z-DDaEIq3W1H9g_EgS4Cd5BfVqraD9cUtxBSYitmrllS5NxWw-_UvnRNNk0KsfpM3I7MMPrVqgRRM9hhGBx12Llf_5aym1b-wRtA3SmrfGo_ZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب عن إيران: "نحن موجودون هناك منذ 5 أشهر، وإذا نظرتم إلى فيتنام، ستجدون أنهم كانوا هناك لمدة 20 عاماً، ما نقوم به ضد إيران عملية عسكرية لا حربا.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86546" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86545">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ca7dfea1f.mp4?token=CIjgrbdTGzGIhp1HX9LlRZdcvmu-bc6p2OlU6zMrEtnCk5MVPlM1opSuAL5AE1SpeUZSi-2wwdpHpdZWevReRhFpplArk-FDBoHvw1i2TTf8Mzi9RyqRuzzKKdGxfBiHsx0KudvYDWT8ACi4MGrSN5LREct8Jqh6teE0jXea4itk0W3bx2vfsLfIi7noCp5eHH3QScAmfAu-o5W3c7u2K68Ldew1dmXmKU7HaLNLjuBq2i9CAGxmVUfrzP8xAJ4g_CgWM-YwcKZcfsphDseBTBioxCDEw9yusaHfBsg6HFci5e5y1xM67EJ4N42Re93KV02a2KycKjs93VABDIVN-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ca7dfea1f.mp4?token=CIjgrbdTGzGIhp1HX9LlRZdcvmu-bc6p2OlU6zMrEtnCk5MVPlM1opSuAL5AE1SpeUZSi-2wwdpHpdZWevReRhFpplArk-FDBoHvw1i2TTf8Mzi9RyqRuzzKKdGxfBiHsx0KudvYDWT8ACi4MGrSN5LREct8Jqh6teE0jXea4itk0W3bx2vfsLfIi7noCp5eHH3QScAmfAu-o5W3c7u2K68Ldew1dmXmKU7HaLNLjuBq2i9CAGxmVUfrzP8xAJ4g_CgWM-YwcKZcfsphDseBTBioxCDEw9yusaHfBsg6HFci5e5y1xM67EJ4N42Re93KV02a2KycKjs93VABDIVN-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب عن إيران: "نحن موجودون هناك منذ 5 أشهر، وإذا نظرتم إلى فيتنام، ستجدون أنهم كانوا هناك لمدة 20 عاماً، ما نقوم به ضد إيران عملية عسكرية لا حربا.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86545" target="_blank">📅 19:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86544">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الله أكبر  مسؤولين أمريكيين: استخباراتنا ترجح أن إيران تقف وراء هجوم سيبراني على نظام المياه في مينيسوتا.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86544" target="_blank">📅 19:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86543">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇱
السفير الصهيوني لدى الأمم المتحدة:
خيار إقامة دولة فلسطينية ليس مطروحا بعد 7 أكتوبر.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86543" target="_blank">📅 18:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86542">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86542" target="_blank">📅 18:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86541">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86541" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86540">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86540" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86539">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a759ef21a.mp4?token=l-y8oOHTv6ca3Ol65tBAteg5NdoxZNwd9Pp844e4UuBxot_J-FQau8JCjgBVfF4cPelkERSiqu9GFzG_NJi0rDV3pgLSENetKLbWS7M74C6XSo_fk5T83dLV6dTaGYSQV_b2AnQFb5YgqmnzETdPp3bT1VSEs3yCoK0xDnqQhH4OyieUwFqCR4eD62OsFmsZzBEezjwRp2G8cI3GtdSRe6claGCsWhI-vv5vLUBRJMAj6jkrJK-nHOk5E7KQR7AAQ9aPqbngDFv8w2rMktm2tru9YxzpxuGYMGXPbBsZurqpMlVBb5CNa3fShRd3-hPEJfWwPpepmQDynYZ6Ylpsnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a759ef21a.mp4?token=l-y8oOHTv6ca3Ol65tBAteg5NdoxZNwd9Pp844e4UuBxot_J-FQau8JCjgBVfF4cPelkERSiqu9GFzG_NJi0rDV3pgLSENetKLbWS7M74C6XSo_fk5T83dLV6dTaGYSQV_b2AnQFb5YgqmnzETdPp3bT1VSEs3yCoK0xDnqQhH4OyieUwFqCR4eD62OsFmsZzBEezjwRp2G8cI3GtdSRe6claGCsWhI-vv5vLUBRJMAj6jkrJK-nHOk5E7KQR7AAQ9aPqbngDFv8w2rMktm2tru9YxzpxuGYMGXPbBsZurqpMlVBb5CNa3fShRd3-hPEJfWwPpepmQDynYZ6Ylpsnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
من بوت نايا
:
"هذا والدي مدمن على اخباركم".
شهادة نعتز بها، ونسأل الله أن يديم عليه الصحة والعافية، شكرًا لثقتكم ومتابعتكم الدائمة.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/86539" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86538">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktGKSLx0WC6teniYdVqivDumOodEzMZQm4ZkaKcsYjjBkUZah3lQ3vyq-xYqRtjaOAIJuJFF9_WyMUaGW6YB6Dj_gweNIlQ47U239Pvrl_4IPs1ci_SvYjNofRYePpF5rIIvQL6zbUjrmyiHt42Pf-aza-049dsp79r_38uU1VZvM4TKNnRuS-HaVPcnD0wKwarK0H0ocKdIx2-c0MIGwoTa4e4t7kbWSXQVsgITNp3pbzu_yRtJgp4qATWfbnMcKDtKaCaYzh7iPdqJBBbOMHTBUGH1qhIt7U4aj5ubYTVz45Or5LTZschUOOu_vkcfsB4A2xpA3jjWGxhzb0008w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لن نشكر العامري لان زار جرحى الحشد
نتيجة مجزرة ال سعود فهذا واجبه
نحن نشكر موقفه باجتماع الإطار التنسيقي قبل ثلاثة أيام ؛ ستجدني اول واحد يحمل السلاح بوجهكم إذا تم المساس بالعناوين الأربعة ..</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86538" target="_blank">📅 17:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86537">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترمب: شيء ما سيحدث بشأن إيران</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86537" target="_blank">📅 17:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86536">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇱
بن غفير:
مسودة الاتفاق التي نشرها "مجلس السلام" غير مقبولة لدى إسرائيل. بعد السابع من أكتوبر، فإن دم كل عنصر في حماس مهدور، ولذلك فإن التعهد بوقف عمليات اغتيال عناصر المنظمة القتلة يعادل الموافقة على أن تعيد حماس تنظيم نفسها استعدادا للمجزرة المقبلة. يجب أن تستمر عمليات الاغتيال في غزة، ويجب تشجيع الهجرة، وعلى إسرائيل أن تنتصر.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86536" target="_blank">📅 17:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86535">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تعترض الصهاريج العراقية وتمنعها من المرور في مدينة في ريف دير الزور الشرقي.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86535" target="_blank">📅 17:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86534">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffae7e8ee.mp4?token=LovPnkyfmr5ajxNl4-zhfMZ4A6946HjVHDISD-9MHunGHf8a_bQWilnDNQZ2UI9Yygi261ewVEpq_8WJ1hBmTuh_4ESJaJOT1e82Lka6uG7TXxyCltJsXLTffxsxZ9FP4zVrGZvu64p2CccoPnjhjtovWPqt5jHKMbQKa4fCChEb7Npg2wqzatjKAJovwuRrVNZZCmURbYyoYtQMgYFHYsWjgqiY5F7Ya9tSNMKRF6h-zFvG7x7sUT2sWDP8OqL-5GeTw4Qs_ugPdCOUcqpAJB6qIw8cMaWKDCbCQ2FyCfTOzLrrylDW5cwCL-llEKTJHWkAuaH0_ZVgjjPMmHszt7-Y3FWzwyD0_kk0SoMdEwgbUzAjD5M3IQXjpeGoP997Hjus4AxDjGjKhMTg1QLZTRfZMwLkvny9ttE62zPPeXi4tnMuPJjdQu7hycg3HOtk4qGci_phoOXwj3onED7dtyDvGhIoUS8u589m4d8w1ZumJIsz5Ri6R_fGNBKX7yo0SKF0ez0SKZsKaUwids8tuVapQ1u5rIYuAyfxLNFrjpsbV8IYgY2DvCtwAA8jinZ--tP2XuRCSXjsJmTtZsUfrbkqRqI-tZCvSIC5Kaiq3eu7hwy0ES52PBvGC8nYHJGuXKRgv6qDmbs-d4JJ9SxW4boU0UVUhIoAmb69LUp_DKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffae7e8ee.mp4?token=LovPnkyfmr5ajxNl4-zhfMZ4A6946HjVHDISD-9MHunGHf8a_bQWilnDNQZ2UI9Yygi261ewVEpq_8WJ1hBmTuh_4ESJaJOT1e82Lka6uG7TXxyCltJsXLTffxsxZ9FP4zVrGZvu64p2CccoPnjhjtovWPqt5jHKMbQKa4fCChEb7Npg2wqzatjKAJovwuRrVNZZCmURbYyoYtQMgYFHYsWjgqiY5F7Ya9tSNMKRF6h-zFvG7x7sUT2sWDP8OqL-5GeTw4Qs_ugPdCOUcqpAJB6qIw8cMaWKDCbCQ2FyCfTOzLrrylDW5cwCL-llEKTJHWkAuaH0_ZVgjjPMmHszt7-Y3FWzwyD0_kk0SoMdEwgbUzAjD5M3IQXjpeGoP997Hjus4AxDjGjKhMTg1QLZTRfZMwLkvny9ttE62zPPeXi4tnMuPJjdQu7hycg3HOtk4qGci_phoOXwj3onED7dtyDvGhIoUS8u589m4d8w1ZumJIsz5Ri6R_fGNBKX7yo0SKF0ez0SKZsKaUwids8tuVapQ1u5rIYuAyfxLNFrjpsbV8IYgY2DvCtwAA8jinZ--tP2XuRCSXjsJmTtZsUfrbkqRqI-tZCvSIC5Kaiq3eu7hwy0ES52PBvGC8nYHJGuXKRgv6qDmbs-d4JJ9SxW4boU0UVUhIoAmb69LUp_DKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلحين مجهولين يقتلون الشاب "ريگر خيلاني" أثناء فتحه بث مباشر على التيك توك في حي باداوا وسط محافظة أربيل باقليم كردستان العراق ضمن الانهيار الامني الذي يشهده الاقليم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86534" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86533">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
ترامب: الحرب مع إيران تسير على ما يرام</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86533" target="_blank">📅 16:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86532">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇱
اعلام العدو عن مسؤول كبير:
لن نتراجع بأي شكل من الأشكال عن الخط الأصفر الحالي الذي يفصلنا عن قطاع غزة ما لم يتم تفكيك حركة حماس بشكل كامل من أسلحتها.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86532" target="_blank">📅 16:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86531">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
ترامب:
الحرب مع إيران تسير على ما يرام</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86531" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86530">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAaKp8Qh_se3cdDZcbHbbiMVUiOmb-PQetue6hYQQiU1phg5XwgcDU_z5lpeir-oB5JlMjhYiUNFCM89RF3p5RpAL_mB9fDeXoLbeloMUxioGKizWirqHpBlwF7wnDdLJ4L3Wop48wuuHTKj7Unhl62NKrX_NU0eKy1U0Sv_RDFvx-m9PyoWwdjOWz-StNM5V3A2Dp6ZuKy2LXtuu6ENs3eTPmnlzEcFIvc9wUYHwkEGEgLuTjcV5MBGmwAZulu8Lad4doxMYoyfTbaAAlCBrQPxRIXGDIvunpwiqY90lsFMP2KVoUyG2Ytv-r7AqXiEbH4f6iPSVVJOQkzWfKe2ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇮🇶
بيان مسيرات صنعاء:
ندين العدوان السعودي الأمريكي الإجرامي على الشعب العراقي الشقيق ومؤسسته الأمنية ومجاهديه الأعزاء.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86530" target="_blank">📅 16:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86527">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSdkfyOpcEIopdIx8wbXNf3b_9xDp4EO2kIdWkxhDnp8xJiDNnSjJGzCj6ETfKnZFBUvxGG3J0uWu82xXxbDMMMoTL1S4F8sSR2weYDs-FHsw3gLp2ja7eSiYqPiAXgSsiNeiEGd6cGfVOS6NmjevA53-gK1fbD7GLXfN2He9M7vTHqyMmUZS1MWBhhAwvKZ-0lqTSJ9p_2pyj1kpIZ3MIUv46Ub0RHjXzFjH49zNCqUuvPsHNqcTTNGCnMR_MmzZ3xA0HF6_yDdh7g7jzqmOqHQcTT8LRmC0pZXwHG0VxIv_IFZElwWV8LWzUPMS61TP9T-RRG9SfI0TgCnl5rLuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLrXNrTb3mpfERt1gUOBvBPa5JyMQJUZfcyIIPFllYU0pNoGEHtMiXlC-bpPTc89-tjrujw6qqDgKbpKWl0r7EIrKZ-baG-aLbq6PBgFXUj7tgcbq2sFRhn_OYrWc7hcDJpkmys2oOff-j8nupYz9DazPrS5E4Nktd5HtvGNC4mpfnlAmxhcYp-Dma15jZ5v4P12N6dxotHaVzs9g_TSDJmyvlBpPrETMUikgA-QLRT0DvL04H-14AafhILQ9dGqhXMIu4-DY42rHIScG8ct8F3j5JlcyeDkZtA-NLiLHwoc0T9mgBVoVw74uSiIcAUB4utfKTfTr_W8eIeVn0D_rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oF-ysk-NM9BaufwkUv91iF-lxSFlfhv40vDy03cw0va6rr89JKPwYylHc6ilkQwdNVD066CtzfF2ChIpOA6Gm6Q8U97dXed_lYApEkTmguei1zJqqyqD6R06Yffexf4yqAqFb2wlME2e5EM-cK-R8x3C0wm3ldpAsZdyqB9C6Jm1wEea1tJRNyoJ9HDEC-TNMenL-ElezR3TX6uLI3O_Cg623LfOiaZJ8sQ-HGa9-PXKCegObA9YCbGRN0V_wwXD089Nn868QtPoTRHl4OEHsCqyfRrPQNvSthQQNWs4aBMU_6rUGIcZrEl5T1jCEJVizbAw30ZbxsYiis8a8MFa-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇾🇪
مشاهد من العاصمة اليمنية صنعاء..
العلم العراقي حاضرا في مشهد يجسد عمق التضامن ويؤكد وحدة المواقف بين الشعبين.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86527" target="_blank">📅 16:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86526">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
🔻
بيان صادر عن حزب الله حول العدوان الأميركي على العراق:
يدين حزب الله العدوان الأميركي الغاشم على العراق الشقيق وشعبه الأبي، والذي أدى إلى ارتقاء عدد من الشهداء الأبرار وإصابة عدد من الجرحى، في انتهاك صارخ وفاضح للقانون الدولي ولسيادة العراق واستقلاله.
إن هذا العدوان السافر والخطير على جهة رسمية عراقية، وبمشاركة دولة عربية، يفتح الباب أمام تداعيات بالغة الخطورة على المنطقة بأسرها، ولا يصب إلا في مصلحة المشروع الأميركي - الإسرائيلي الرامي إلى زعزعة استقرار المنطقة، وتفتيت الأمة، وإدخالها في دوامة من التوترات والخلافات والاقتتال.
ووفق مقتضيات حسن الجوار والعلاقة الأخوية والتاريخية التي تجمع السعودية بالعراق وشعبه، كان الأجدر بالسعودية أن تلجأ إلى الحوار وفتح قنوات التواصل الدبلوماسية مع الحكومة العراقية لمعالجة أي توتر أو أزمة، بدلًا أن تنجر وراء سياسات العدو الأميركي والإسرائيلي والغرق في وحول مشاريعهما لزعزعة استقرار المنطقة وتفتيت وحدتها.
إن إيغال العدو الأميركي في سفك الدم العراقي يكشف مجددًا عن نواياه العدوانية تجاه العراق وشعبه، وسعيه الدائم إلى منع استقراره وتعافيه وإضعاف دوره الوطني والإقليمي في هذه المرحلة الدقيقة التي تمر بها المنطقة، ويؤكد استمرار أطماعه في خيراته وثرواته.
يعلن حزب الله وقوفه إلى جانب العراق وشعبه العزيز، ويؤكد أن هذا العدوان يستوجب موقفًا عربيًا وإسلاميًا ودوليًا عاجلًا وحازمًا ومسؤولًا لوضع حدّ للسياسات الأميركية العدوانية، وصون سيادة الدول واحترام القانون الدولي، ويؤكد أن الصمت إزاء هذه الاعتداءات، والاستمرار في التغاضي عن هذا النهج الخطير والمدمر، لن يؤديا إلا إلى جر المنطقة إلى عواقب خطيرة لا تحمد عقباها.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86526" target="_blank">📅 16:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86525">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
حركة حماس:
الموافقة على إدراج ملف السلاح الثقيل في إطار الاتفاق قد رُبطت واشترطت بوقف جميع أشكال العدوان، والانسحاب من قطاع غزة، وتحقيق التعافي المبكر، ودخول اللجنة الإدارية، وانتشار قوات الحماية الدولية، وحل العصابات المسلحة والميليشيات التي شكّلها الاحتلال، وإعادة الإعمار، وضمان حق تقرير المصير، وإقامة الدولة الفلسطينية المستقلة، وحماية حقوق المواطنين.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86525" target="_blank">📅 15:42 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

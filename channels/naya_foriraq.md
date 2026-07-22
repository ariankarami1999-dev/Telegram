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
<img src="https://cdn4.telesco.pe/file/RWfWfb1S_AxWny7SMXdS8xIzVhAdvqceyAnEkfmKSY_B4lRr16z7cBpoAGWaZL6FMk98EiDsWZaLKs33w7NSNEZKwOruzvmRgU-g3Lkefd3jz6SLYVE0N7tUaNL6JTXfeAmsY9PZAFvQ5vxkTqPj5g6XSx3l0Ev49k-Emk94Jayd_XUBKAtyMRbv3_INgVJ0CQt7AaroT3XYRIWZixdXxDyJ6ZUqE4VHX6zmRerIK80dUdDVXZxar7J2eNex4tedoHVlq_g06wl2tmzjwhG8oeZnvCugfomFxChUWfzr1PTUn_XQnVvnY-rIZQPRBzd1usBsYGYLBCVYXEaBNSLN_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 03:25:22</div>
<hr>

<div class="tg-post" id="msg-84965">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiZsnDMoDFtWIQE9p5iRGLT-f6tOhpBkQUrN7sjLJG3ePS8cO4CKKJ12vVHI1wuJpqPgguT0E--kQ9N8_248NaSS2MFu6NXr9jbf4FBg7Ro35LfPgeqDv35K_ba9Ow7kQPipnJGUvNrV3rpMROPid9zolovVK7Z7efVs2zpfnOh32Yxb7cplv_ztXHvTdluY2KniVC8RKBFRK6Fs69xQZx0EL4eqeKiCqpm3SsXIlj3G8_5oj3AjDtJN08QovYINh7lzD8ud7pecIRCC1GzGx2_-gpuff8bFtqsQlQqHk_LXmaCfPqeQLKmZ9rGhclJLZV_YzbVMGzpEjN65V6xKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXjoAw9fY9tQYI8Bp4oyfk3evgXLAjVpo5fkRZim6kmtdjgi2cyaD3rk0Go8lNjBm--zMS301YvXNgeKnNzZMzF6fOxgXWCtgZrBBJC5wYE5x92OGyAZBHGxNZkXuK_X6lmr5a12nZ2UYePcrzpZlJ9VydAzKoCHiZDR2oKcbKhlCiiEOvALaNH0IdO0ykEx-4Z0vFljaCYiSfWDPqrJ3FvxOxvqeVM9sFXjp7XevQant44EHe97eJ8zNGWbrGH-NfpiRuOwn3QyBARDJD1WsGtq9TKzEEgvDpOA20wuuJRT7C7KklWNj3zg7nJAIs27QMpR9Jo12gR_PoG33ZgyQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من منفذ الشلامجة الحدودي</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/naya_foriraq/84965" target="_blank">📅 03:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84964">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377fb136c5.mp4?token=iNt2R_ysmy2a-GSyBE0xh0StTg1DABibc4FkqyAm3xmwJ8a4ME7cAvLpOQjaUwY5o_b9dRQRpbU86k5XOcb6KQBtiOJWeqMzbehpuZe661kH4N5qenCaHRg-oraBsblg-lLmDiD1pvbpD2Gdo_QZWHuBzDu4PJNG2OAMRTkjLUj5Q9NkBaBYq2c-6LYovV__Z3SEsnki8NigffZLmmKwu2I5YY4VXUezr6G_2eP5NFS7ivka2iFbOfj8FbPkDfE6fHIbhuFXSUdjxwgeh5muVDSbfyPExwvpz0o3QWCnlRwE_QbYMeqa38y-J8s_jZK03Al--QLHITYwMbOjKNVmog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377fb136c5.mp4?token=iNt2R_ysmy2a-GSyBE0xh0StTg1DABibc4FkqyAm3xmwJ8a4ME7cAvLpOQjaUwY5o_b9dRQRpbU86k5XOcb6KQBtiOJWeqMzbehpuZe661kH4N5qenCaHRg-oraBsblg-lLmDiD1pvbpD2Gdo_QZWHuBzDu4PJNG2OAMRTkjLUj5Q9NkBaBYq2c-6LYovV__Z3SEsnki8NigffZLmmKwu2I5YY4VXUezr6G_2eP5NFS7ivka2iFbOfj8FbPkDfE6fHIbhuFXSUdjxwgeh5muVDSbfyPExwvpz0o3QWCnlRwE_QbYMeqa38y-J8s_jZK03Al--QLHITYwMbOjKNVmog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من منفذ الشلامجة الحدودي</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/naya_foriraq/84964" target="_blank">📅 03:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الله أكبر
🔻
الحرس الثوري:
واحدة من ثلاث سفن متورطة كانت تنوي عبور مسار غير آمن في مضيق هرمز اشتعلت فيها النيران، بينما عادت السفينتان الأخريان بسرعة إلى الخلف.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/naya_foriraq/84963" target="_blank">📅 03:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84961">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca89d96130.mp4?token=gjOqxtUpnp-MH_63r9RTAiTd84gkl2sgBq--qMAhHDserYoQn9KfgZwaBW3ZDX1GAvDSiZkePKurryS06oXwJ_VT8D7d0Svu63uO4dacUtk9TRmqlFcrFJRtgOFx-ugnqaMRMMnWKBWtD1pVglhLCNzdBwRcbPntFl0u_x_LIkNEtZgrzpWKtpnikK5HUBgXR84y7J5MEwSZeAmPYAOWujPmvLYyr8G9cRcTWlUdp-TR0EATtDTVOsE-AQby-lhszrJ_GZ60414SKMrpRYh8EbDQayciGAr57vHFEQ9faUIreSjalsPwKkrxlCWAQs9s3iAvWgHkZ2ydyRbIgeEETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca89d96130.mp4?token=gjOqxtUpnp-MH_63r9RTAiTd84gkl2sgBq--qMAhHDserYoQn9KfgZwaBW3ZDX1GAvDSiZkePKurryS06oXwJ_VT8D7d0Svu63uO4dacUtk9TRmqlFcrFJRtgOFx-ugnqaMRMMnWKBWtD1pVglhLCNzdBwRcbPntFl0u_x_LIkNEtZgrzpWKtpnikK5HUBgXR84y7J5MEwSZeAmPYAOWujPmvLYyr8G9cRcTWlUdp-TR0EATtDTVOsE-AQby-lhszrJ_GZ60414SKMrpRYh8EbDQayciGAr57vHFEQ9faUIreSjalsPwKkrxlCWAQs9s3iAvWgHkZ2ydyRbIgeEETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اندلاع حريق مجهول بالجانب الإيراني من منفذ الشلامجة الحدودي.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/naya_foriraq/84961" target="_blank">📅 03:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84960">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
🇮🇱
🇺🇸
سي إن إن:
مدير الموساد الإسرائيلي شارك الأميركيين معلومات تفيد بأن منشأة "جبل الفأس" الإيرانية موقع محصن تحت الأرض وتم ربطها بالبرنامج النووي.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/84960" target="_blank">📅 02:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84959">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي:
ما يحدث الآن واضح السفن تحاول العبور عبر مضيق هرمز ويتم تفجيرها من قبل الإيرانيين.
الاتفاقات مبنية على الامتثال وقد أبرمنا  اتفاقا مع ايران ثم انتهكته ولم يعد ساري المفعول.
نبقى منفتحين على الدبلوماسية والحل التفاوضي لكن يبدو أنهم غير جادين في ذلك حاليا.
في اليوم الذي كان يفترض أن تصدر فيه إيران البيان استهدفوا سفينة وضربوها.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/84959" target="_blank">📅 02:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84958">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnJT2lKRZiHaf9GoabIYoMTE-KkGnmrWL_YskOhogI33JYtQ5g1gA6O7lB4Nuwz_JtfOHgALgjFByTFmx0lL6Zt1ftPHhLjUY21yZP6dY2Z5qhqWdcaHhme7RpvMNFJMZzgN7xDCILv8DzesJmkt_9Lz0DqIIdKp-kVIz-X6PeUIeU_kOnT2Q2GKieVALkaUIZnSOLMxQ2EZ4snxiADAUGbsavDMa2PmTiH_MOjyMeZGA874dSLohYQZhnYHl3XRW6v-3A1GxbLdBnyX6RcUJgNCkM1UWlWAnAwehpsmXhp_nFl2Mc8Xvlo7mXGjSfCT6tvv_SVkI-bRmmzrdH73ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الطيران المسير الإنتحاري يستهدف القواعد الامريكية في الكويت</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/84958" target="_blank">📅 02:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84957">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سماع دوي انفجار جديد في بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/84957" target="_blank">📅 01:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84956">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
الجيش الامريكي: ‏
في الساعة 5:30 مساءً بتوقيت الشرق الأمريكي اليوم، بدأت القوات الأمريكية في إطلاق المزيد من الضربات ضد أهداف عسكرية إيرانية بتوجيه من القائد الأعلى. ستستمر المهمة لتدهور قدرة إيران الإضافي على تهديد البحارة المدنيين والسفن التجارية العابرة للمياه الإقليمية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/84956" target="_blank">📅 01:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84955">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/84955" target="_blank">📅 01:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84954">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/84954" target="_blank">📅 01:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84953">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/84953" target="_blank">📅 01:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84952">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohkkwYTLB_0-bm9pX3gfPdvGdSddOgsN_yJ3G8Ee4nrzyYXsSavLGEjD99AGW22SH6Wxd-JLd1BMa3W9jMQKH32yDPIuGKV_PahwJcniRMM_NbBpvnc4vjt1AzpJ8TYIWMfCxEgc9mT918_9zyAkolovMBvJqRclBx4JMeuEmO6JsUfWFDfThsS5S8BgjR11Oo41StheyDocCKCX1INTSO3cLnbmQj-3HH8xgCg7nBIMIy5ZZYh2Ft8TTHKKzRLzeF4XL8uXcXlsM5cs0ijema6XQH6Tz1fsN8BHpWuHTKKfeqHexiEboe1Jjji9DSAzPmhwWdECvOYwzx5CdTh2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد ان كانت تعتقد انه ُ قتل في الموصل ؛ استراليا تعلن عن العثور على ارهابي من داعش في سجون العراق</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84952" target="_blank">📅 01:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ-lMqHFjjlMJPSmk64UIK7RaUtEo9h7igw2JT3TEYlDDomEJXisMvfgr9PxfO-VvRq3_KX0i2v7SmrXIlWRyleIvC2URLODIhV_Ammr7zZH0aWkb3uHiOFGCEtq8Z_dnBWzZYQOwqmLoPoGG2WkWayg0WVxyKnKpJGyJ828a0AtWC0rroADQ3Bv1hQg-a9a79jfVDFur5S_qYTJfcqn3yYHAh6qbO-1zGtDWEJXi3LMGlwJ5OW2K8VJq1zKxttPMCIRiPXzbKVbAT3Irl8R2jO2492AD7vDWoIAoJk_o8xywkhPjlQ4v8JZy-zEi79qJ_KYMaw2qdk0iBd0Fj6eeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: ​ نفذتِ القواتُ المسلحةُ اليمنيةُ عمليةً عسكريةً نوعيةً استهدفتْ سفينتينِ نفطيتينِ سعوديتينِ خالفتْ قرارَ الحظرِ الصادرَ عنِ القواتِ المسلحةِ في البحرِ الأحمرِ إحداهما تحملُ اسمَ "ENCELIA" والأخرى "LAYLA" وذلكَ بعددٍ من الصواريخِ…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84951" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84950">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: ​
نفذتِ القواتُ المسلحةُ اليمنيةُ عمليةً عسكريةً نوعيةً استهدفتْ سفينتينِ نفطيتينِ سعوديتينِ خالفتْ قرارَ الحظرِ الصادرَ عنِ القواتِ المسلحةِ في البحرِ الأحمرِ إحداهما تحملُ اسمَ "ENCELIA" والأخرى "LAYLA" وذلكَ بعددٍ من الصواريخِ البالستيةِ والمجنحةِ والطائراتِ المسيرةِ وكانتِ الإصابةُ دقيقةً بفضلِ اللهِ وعونهِ وتسببتْ في نشوبِ حريقٍ كبيرٍ فيهما بفضلِ اللهِ.
وفي نفس السياق فقد أجبرت القوات المسلحة اليمنية ما يقارب عشر سفن على التراجع والعودة.
​إنَّ القواتِ المسلحةَ ستواصلُ عملياتِها البحريةَ ضدَّ العدوِّ السعوديِّ وإنها مستمرةٌ في فرضِ معادلةِ "الحصارُ بالحصارِ" .
وتؤكدُ للعدوِّ السعوديِّ أنَّ أيَّ حماقةٍ أو عدوانٍ يستهدفُ به بلدنا فسيقابلُ بعملياتٍ كبيرةٍ في عمقِ أراضيهِ وستكونُ عواقبها عليهِ وخيمةً بإذنِ اللهِ وقوتهِ.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/84950" target="_blank">📅 01:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84949">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارات جديدة في ميناء سيريك جنوب إيران</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84949" target="_blank">📅 00:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات في درعا السورية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84948" target="_blank">📅 00:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84947">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوي انفجار في مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84947" target="_blank">📅 00:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84946">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVTvFF2wEWN724DkeHG7va6-gCmL6C95sGYvYRdQ5aZD-CIkWk7zV9tgdPOqSOqs9zlP0rHitMN_xBbsFGxtTUrelmYWTqfm1y9XE3zfNTaLYEcje4Ga2IjqTUiCMj9GrkbBYnm-7sCIH9AniRD4vBbeZhevbL7Ezpp10dQmYnVTea5ZNdQH-obPPTDmsOTHHw6KPZgeDdoK-V_vSI7-fbdh-n0jz67M5-5VH0f4cXpzdzvWgaAOzXK2Ftim_qz5omCNMoxjsu0DC2yGhK_IjvXSChgbRHdCWJxX_dW1tdHe_F-P3JkUfLsmJdu9XhVavp9UcKd8iJmOKK9-MqtICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة قبالة السعودية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84946" target="_blank">📅 00:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84945">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجارات في مدينة بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84945" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84944">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">استهداف سفينة قبالة السعودية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84944" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84943">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/84943" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84942">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
اسوتشيد:
‏مجلس النواب يتبنى مقترح ميزانية بقيمة 95 مليار دولار لتمويل الحرب على إيران وأولويات أخرى للبيت الأبيض.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84942" target="_blank">📅 00:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84941">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في سيريك</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84941" target="_blank">📅 00:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84940">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في الاهواز.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84940" target="_blank">📅 00:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84939">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
انفجارات في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84939" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84938">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزارة الطاقة الأميركية: أميركا والسعودية تتوصلان إلى اتفاقية للتعاون النووي</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84938" target="_blank">📅 00:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84937">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/84937" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84937" target="_blank">📅 00:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84936">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية نوعية.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84936" target="_blank">📅 00:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84935">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">أنباء عن حدث امني اولي قيد التحقيق داخل الكيان</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84935" target="_blank">📅 23:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84934">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">أنباء عن حدث امني اولي قيد التحقيق داخل الكيان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/84934" target="_blank">📅 23:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84933">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/84933" target="_blank">📅 23:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84932">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇪🇺
🔻
تقوم القوات البولندية والألمانية بتعزيز الجناح الشرقي لحلف الناتو بشكل مشترك من خلال تركيب حواجز مضادة للدبابات بالقرب من الحدود الروسية.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/84932" target="_blank">📅 23:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84931">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc6512039.mp4?token=UDJ4KxML48nGMlZc2d7Ps4iwXGD3oLDncDWh1Jd7MGYoNA6Ul76V7pByowTdghd-Vxm48mtPbEjRkI0eUA92B0hH-RDsp6VnDM0301LTVzEYvWVJ347S-N79jT0nCt9xvb8ioEBRWELzl9Kvl8aptjbCdDtRAU7hymKmhQkwcH6Ujuya0tpYBqPCZv8G1mh9E7_EhaWT0lKgoHj0YqjD16i83P1V9TW3glNh4iz60JMmemgy3Rh22WPLWGOGV7rniHAEOn4AK6YGcm9beWGMOGuvT-Xtx5rl6Ehk3JCKJVeUCPtXglJ7ssmQQwoTDgMuBYmx0wfRfXEceAmP_uSudiOQq2EEYbeWyVqZ0qUBjUoY4EmKAPedOq9Pwq_eYSj22meLBfcmf9K1hjaIL6yalHK09jsHc0J-UzqR2q-me6E7dIUrCXuiIYj92UTm5fJeMw1ySxo2tqwLHJqRUA_jUy-o5dXJ4x3PfAg4COK4oG41Ld5-JC1NdXC0KGs_5iWbOI7qCgEd1J1Sut7qkZshsa5s0uDezuwNQrYGH9JzvTkvWaeLU8UhX_skO6Y9OBJHt5qjX841CZsGF2DhZFMGxHB1dG7hF7UBmmQ8GzqaKX1Ocs4mNTq9YDBmU0KnfAYPYht_lTB62ZCQ0TKqzl_A6O6KAYA6fOISjPWoJwIw5Mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc6512039.mp4?token=UDJ4KxML48nGMlZc2d7Ps4iwXGD3oLDncDWh1Jd7MGYoNA6Ul76V7pByowTdghd-Vxm48mtPbEjRkI0eUA92B0hH-RDsp6VnDM0301LTVzEYvWVJ347S-N79jT0nCt9xvb8ioEBRWELzl9Kvl8aptjbCdDtRAU7hymKmhQkwcH6Ujuya0tpYBqPCZv8G1mh9E7_EhaWT0lKgoHj0YqjD16i83P1V9TW3glNh4iz60JMmemgy3Rh22WPLWGOGV7rniHAEOn4AK6YGcm9beWGMOGuvT-Xtx5rl6Ehk3JCKJVeUCPtXglJ7ssmQQwoTDgMuBYmx0wfRfXEceAmP_uSudiOQq2EEYbeWyVqZ0qUBjUoY4EmKAPedOq9Pwq_eYSj22meLBfcmf9K1hjaIL6yalHK09jsHc0J-UzqR2q-me6E7dIUrCXuiIYj92UTm5fJeMw1ySxo2tqwLHJqRUA_jUy-o5dXJ4x3PfAg4COK4oG41Ld5-JC1NdXC0KGs_5iWbOI7qCgEd1J1Sut7qkZshsa5s0uDezuwNQrYGH9JzvTkvWaeLU8UhX_skO6Y9OBJHt5qjX841CZsGF2DhZFMGxHB1dG7hF7UBmmQ8GzqaKX1Ocs4mNTq9YDBmU0KnfAYPYht_lTB62ZCQ0TKqzl_A6O6KAYA6fOISjPWoJwIw5Mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: "هذه المناوشة الدائرة بيننا. أسميها مناوشة مع الجمهورية الإسلامية الإيرانية. إنهم يتعرضون لضربات قوية. ويريدون عقد صفقة. لكنني أقول إنهم ليسوا مستعدين لعقد صفقة. سيكونون مستعدين قريباً جداً."</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/84931" target="_blank">📅 23:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84930">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b79d0b62b.mp4?token=HG8xjT57kBlrXE0HmB2FODDgZwRzGiC_X_MX52T1J7j8gck138Ssqou5uOjCa6u2dcxBLRbTuvrC7wrbpSktRC0ycby6V_97G2e-gjyUkvW63IHFeunkY5UzqhUy8ETroS8u_sIFvmaziLDfkL4j4aNybEP2G5feoankMg2b-7cFwDBjBsXvzSJg4HoI4lCjvp1VHGLyua5D3bXtZ3jCAwvA8TNYdSbY7PawzSidnFQpTp8RSXbBL1g1Ae5Oh1V5zdJtw2r1oJXOTialoENQnodroh0-EsQ8p907SamJjCENty6jcd96WAUAe77Im-8wAHA1_DtqYHetcnNE2YcdiFJdBB_93jORPo6rQaqYwhR4rvNkyz5_JiD6Sm0GGb5sjKoysYB4-jebDFK2eCr3kHz2_NaurtVM5XwlrWb-M7SEKuNflMNeV46Myhi880Vn7bJJ0Dr-_tIkmNTa-bZEDNYWONIvLhLMO10saSKqLGzc-pTUa-XJH2BCkQ2aipDqnl5zo5CSuOfrTLOz1JmaSfmwO2KM-i4nXzol5YdIWDR5ZPj2ZtBBiiawdCoeImbNdbiSg6wg_t8Dbngpp-R9Cn3bqt_on0Ce1BzP6kEWxxtD8zqSzR7b1TPZQJAaLlW2nVGqzf3mu77JG8Q2TQicjnP8haO8lm1teKwDqvMIas8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b79d0b62b.mp4?token=HG8xjT57kBlrXE0HmB2FODDgZwRzGiC_X_MX52T1J7j8gck138Ssqou5uOjCa6u2dcxBLRbTuvrC7wrbpSktRC0ycby6V_97G2e-gjyUkvW63IHFeunkY5UzqhUy8ETroS8u_sIFvmaziLDfkL4j4aNybEP2G5feoankMg2b-7cFwDBjBsXvzSJg4HoI4lCjvp1VHGLyua5D3bXtZ3jCAwvA8TNYdSbY7PawzSidnFQpTp8RSXbBL1g1Ae5Oh1V5zdJtw2r1oJXOTialoENQnodroh0-EsQ8p907SamJjCENty6jcd96WAUAe77Im-8wAHA1_DtqYHetcnNE2YcdiFJdBB_93jORPo6rQaqYwhR4rvNkyz5_JiD6Sm0GGb5sjKoysYB4-jebDFK2eCr3kHz2_NaurtVM5XwlrWb-M7SEKuNflMNeV46Myhi880Vn7bJJ0Dr-_tIkmNTa-bZEDNYWONIvLhLMO10saSKqLGzc-pTUa-XJH2BCkQ2aipDqnl5zo5CSuOfrTLOz1JmaSfmwO2KM-i4nXzol5YdIWDR5ZPj2ZtBBiiawdCoeImbNdbiSg6wg_t8Dbngpp-R9Cn3bqt_on0Ce1BzP6kEWxxtD8zqSzR7b1TPZQJAaLlW2nVGqzf3mu77JG8Q2TQicjnP8haO8lm1teKwDqvMIas8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يحيي ترامب والدي أحد الجنود الذين سقطوا مؤخراً والذين كانوا ضمن الحشد، ثم ينتقل فجأة إلى موضوع آخر: "معاً نجعل بلدنا أكثر أماناً وقوة ونجاحاً مما كان عليه من قبل. لهذا السبب أسميه العصر الذهبي".</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84930" target="_blank">📅 23:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84926">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqgG9nxNxl-rzt1kFGo0FOcu5TH5H3TLdyfuBVz40SOqbF7SQV0KtcwSaFLEzoechGhWy2KJNeNcfC8i0GszoqMEKXodHgLB0o_lqXOrDY2nswpCk_aHDIz_y22UqvHS7CiIEMx_WAmn_vrHUjmtIDap1VnxXj8xVkXdIzJiAEW-rlhrfQuuyfpeDV-YidNmy5AHC_uHenWetPtU8usdyiBnQ0KMWLkwAFCrHNjzwEWdx1HO3iL9n1uzuD3kU4URgtgHsbOkPd4hSQIzDcI6BBwuyaRwq2p4LLlo-8WqHmWq81npJK-FswKicxsv2bDNj1T3ilxxnZVeerddrq5MXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qu6Aj5jdGzUfETDYuh_l7BIf5RI0nwUE6TsiwSkPUrbsIZl0Cqyv6a9dUuWAm2dHCEfwEZPoeHLd8adG36w1IcDrpwlUuoPCLa2N9joe5d85jK1m9gnlakRSWVjFDF6DISNm4XRiwXFlLMd2bkhWGBKypg4WtCMeeByVkC-ZAeG181EUYHX3mPy2dZpgNwNz0EPDBv0MM1Mk_fpQGaELKzkAflMB9fOa3P5bRn5qScNkfi0-qMmrrJSCvDSxpwTM-KnxyNvc26hi9Sqy1A-xXmddtg8qI6Yt6o27U2oLo2Z4wM8Oa2SaRiRklDqdWIZN1CQx_TFz7TWAp2IrgnHb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCbVaeph1BUSbzTphe5jVolxkYo7JXHW55aAnH3T1X4_bsPE_vGKncx4nuUNIa5bEqNWgPe_lxUY0y1O0VdsMLL00yiMH1H_60up8ohePW7h0PW8WkxG8Ne6OyGeOEnjaVr7ilYQ_oM9MwueasXAvdYk4TGSrNPSd4rzuwFx0CMqPz6x4KyAF8i8RDYMUw27sbZ7t_pGh4pNjVHWBjZbqd703uzSfgNKSegwHizVv9WD7ScBtmNZJQ2jJAQkVL1D2cd_EglnEF_FBGqZJFccTKbstmOaw-3bPNIjr5axZfiCa__H3FUZIFKS4MXZC75i-LtfCokoGGiSNoicWdRshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2AiEM0DmOsOIJJ-9wozQzh10vbAD3Yc9eqVc53rjthTyE_AfMPgj12JosZh3_k_O78iHfQ1WcYJ8QA_6bzE0P9vZn9HbnpR8niCbZ5LNytF05hwItAmY64QKRnySj_6ieOxX-9ZntwW76I6t1mt5xiSNc1MhnOW_FaRym2UkU_ZQKDwmZm0epjfRwkLX9T3xoZ8vS4BxFD7y9s_FZg82zhaASfUkehKiARQM7AEocU30CL_dYv94XHIkvqpqP4zPCtw53vCcNsPzJAyjE31usmwXGLjhrJAuX0KxuCANkJA-uPdD14cjNaEaEugRA_Oj0iZ3AMOP0hhyvQh-gBThQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
بيانات التتبع:
الحصار البحري للحوثيين على المملكة العربية السعودية في البحر الأحمر له الآن تأثير واضح على الشحن التجاري. لقد عكست العديد من الناقلات مسارها بالفعل أو قامت بدورات عكسية قبل الوصول إلى مضيق باب المندب لتجنب خطر هجمات الحوثيين.
- MICA (IMO: 9399935)
المغادرة: 20 يوليو 2026، من جازان
الوجهة: صحار، عمان
— LIA (IMO: 9417751)
المغادرة: رابغ، المملكة العربية السعودية
المغادرة: 27 يونيو 2026
الوجهة: ميناء سنغافورة
- بطل جديد (IMO: 9799147)
المغادرة: مرسى ملقا
الوجهة الأصلية: ينبع، المملكة العربية السعودية
الوجهة الجديدة: قناة السويس، مصر
— رودوس (المنظمة البحرية الدولية: 1024948)
المغادرة: ينبع، المملكة العربية السعودية
الوجهة الأصلية: مانجالور، الهند
الوجهة الجديدة: ميناء السويس، مصر
— أمازون (IMO: 9476654)
المغادرة: ينبع، المملكة العربية السعودية
الوجهة الأصلية: الهند
الوجهة الجديدة: ميناء السويس، مصر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84926" target="_blank">📅 23:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9ef37de5e.mp4?token=mLQ6NoYNaYFxPTXi7xgu0eWwqjzJUz-SLDTcN5fni7ipJ4fjWioX4anIxNan_3rqQbvPJwl6Hka4o-faQX1vQqDf_Yyq9xM9yYK1waRvsZhv5W1FUzJ6QLMue3eyPm3JTU2dNzqVlXHBdHByKvD07e19zOVcpy5QmyZ2L-dWe5qTOeo0kumZCw7gYGL-eeS3wwnn_wwDenNY_bqO-vMUbcgDCeiHUjsPl0FNrvqaRs1E3ms29iqXmUnNKp6WcFkEckPSE1qmVPtuFIAtH22cwbdEQ_nm5z3WHkzz-cu6mM_B7WxBwymbYybwpPGZhTS8NlfRN-G3KezcjY9cHF3e4RsmM_tuQ2YKjAcJg5xANB10QkXZh3MiBsUnMZWnP9xdi0N10HfB8S4ONOsFcFSZn1Vk7Di-EgzjlLODsgynAL3XlIZLd4tnU6cdGZyS9N81GsmwUHajByhN8Zysgj06qgvtZzn_mDtRqsEJzX2fKU888IIipGnpLk3VH4-a3ntcnssKzp2hAKg_XAEIVhdguST62E1J2ek2lPqD61ir2eht_VIccv5ONqqUarMmSoA4G8S5AjWvchtL_UcU47eebSs1v47_5yxrMNqwBR03O32UGIjgfmQhBTYyseQPVxwKOwK2lG4dIl72s-yab6-7GoUU3aHxMgLwjNEQhDYgrVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9ef37de5e.mp4?token=mLQ6NoYNaYFxPTXi7xgu0eWwqjzJUz-SLDTcN5fni7ipJ4fjWioX4anIxNan_3rqQbvPJwl6Hka4o-faQX1vQqDf_Yyq9xM9yYK1waRvsZhv5W1FUzJ6QLMue3eyPm3JTU2dNzqVlXHBdHByKvD07e19zOVcpy5QmyZ2L-dWe5qTOeo0kumZCw7gYGL-eeS3wwnn_wwDenNY_bqO-vMUbcgDCeiHUjsPl0FNrvqaRs1E3ms29iqXmUnNKp6WcFkEckPSE1qmVPtuFIAtH22cwbdEQ_nm5z3WHkzz-cu6mM_B7WxBwymbYybwpPGZhTS8NlfRN-G3KezcjY9cHF3e4RsmM_tuQ2YKjAcJg5xANB10QkXZh3MiBsUnMZWnP9xdi0N10HfB8S4ONOsFcFSZn1Vk7Di-EgzjlLODsgynAL3XlIZLd4tnU6cdGZyS9N81GsmwUHajByhN8Zysgj06qgvtZzn_mDtRqsEJzX2fKU888IIipGnpLk3VH4-a3ntcnssKzp2hAKg_XAEIVhdguST62E1J2ek2lPqD61ir2eht_VIccv5ONqqUarMmSoA4G8S5AjWvchtL_UcU47eebSs1v47_5yxrMNqwBR03O32UGIjgfmQhBTYyseQPVxwKOwK2lG4dIl72s-yab6-7GoUU3aHxMgLwjNEQhDYgrVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لسنا بحاجة إلى مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84925" target="_blank">📅 23:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0EaxOvU6K60IW7bH6FSlPQBlB3MgXaoL6BHLtVUnIxiRZLhznCorRuXmB-7g65Y5KTzPIVVKR5JqmrVNBExoyuoPEioyNvRRCh8OEN-GkmC0g8G1LBpPkD5YqxdplHYML-zOQlqMseiVc69xwDnU1uMY1OoCyillfdXZhHNA1ZYb8ovgFF8gN4LrSR4E1hn2cu3piJSqLF-CrrEf43h7tkKBaieFbXjMojpSQe_fCmf5qEg9NavxlFc_Wr0IkxTFVJPKT9sn5Uyc1w2KcDOQgQR876yaAMQOGjS0Y3cOoqL94gfB-HhnNGSJKQM3GZhrYguXyJ9NvNeZ4dyH58SKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: لسنا بحاجة إلى مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84924" target="_blank">📅 23:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee8aaa461.mp4?token=AnTCu-K4MxexdJJZoHQCXeH0w5o86zXa35-s-tOXSi4e7Io7qdSIew7PBevSvxWdF15qAqZcrN-D6NaJbeQ7mTmWMq_zFcSU9d3ikRXrS5taNnWRGpYjzE9Zpv8Ux4CiOHI3zGZPlikYWgbAs1h70zVSuFAFc7JkqIKKjO6kyaeDS1Xod3a7jtIoiwSU46DqBx0uxMqjGabhrtJBD8Vi-U7dX1LpYbI6ay_ftvwvrDlsmzH2ZzZSnDzHpMIW0PXnrXYYGOXshHeqbkrE7f0IWCP-bxnxjyD589I55E3CCCvpy91ogwbSZUAaEVngOKxQZogqgzTk3c3gIZIB4FojNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee8aaa461.mp4?token=AnTCu-K4MxexdJJZoHQCXeH0w5o86zXa35-s-tOXSi4e7Io7qdSIew7PBevSvxWdF15qAqZcrN-D6NaJbeQ7mTmWMq_zFcSU9d3ikRXrS5taNnWRGpYjzE9Zpv8Ux4CiOHI3zGZPlikYWgbAs1h70zVSuFAFc7JkqIKKjO6kyaeDS1Xod3a7jtIoiwSU46DqBx0uxMqjGabhrtJBD8Vi-U7dX1LpYbI6ay_ftvwvrDlsmzH2ZzZSnDzHpMIW0PXnrXYYGOXshHeqbkrE7f0IWCP-bxnxjyD589I55E3CCCvpy91ogwbSZUAaEVngOKxQZogqgzTk3c3gIZIB4FojNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لسنا بحاجة إلى مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84923" target="_blank">📅 23:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سفراء باكستان والسعودية والصين لدى إيران يجتمعون في سفارة باكستان في طهران.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/84922" target="_blank">📅 23:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات عنيفة في سماء الأردن</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84921" target="_blank">📅 23:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1Cg3EPE1kYF_wlRDmNnZlnOysqN8qYNjDBvnEYEe5fRY4nAfELxZl2pvA0Rw7Cq44JcWGh_G4KDP4qwDaLjz908ZfwWUZTi56s14bAIUvqZBpUi46RW4mXp9t4smtfEdgW3DqMzJqOqkGPaquLDkTt50nYzeWcn-dNxoNwEoQ72_N2dUKAA3kmtOKBBhIGT5p0cGg9JpV_piaECpZ6AOKhiwVhEXRTvGYBefhF_8cwS_v-5i6dOGuwF97ZozPib-7l1-OrALPZ8hpqGU8ZhBP035W4pD_3u2FGHBzv0EbMn1CAuhj9Hoy8S2Yx2KZQCL-1AW_-NRKlq2ZkxsNajQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشاط لطيران بريطاني في قاعدة اكتوريا في قبرص</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/84920" target="_blank">📅 23:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84919">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجارات عنيفة في سماء الأردن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84919" target="_blank">📅 22:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84918" target="_blank">📅 22:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84916">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7e7b6617.mp4?token=o2N1KJokS4LNJnDDm0Ko3t0oT33xBvh6QX6yAdZcI0qgM-Axo0MNdJ3aQW7bIGuuqyq8bQwQnUNfQwoz4tZ1on9-tDRuv5XMvufGWpuMUz0bDdRWb8Scz8K6eMOdlBkwcn8HO3ciRAZixySDIjbonAJUhY4X7F0S-wTyXAVKdg-tA9nniQlg9IYyTnnqF-Z6TMlnq9IbY31wx6r5MGJjRpvO_ShALOeJKayf5fj5jKgVBKG7YDyullE_XJkmu8RWx_A2yT7aew9wUjljLKEQXJX_I0Sng37ofdbytsISdR5gC546uMh9LLhFhyZeqNKKqTaQGQV-fXBEW3BITpB7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7e7b6617.mp4?token=o2N1KJokS4LNJnDDm0Ko3t0oT33xBvh6QX6yAdZcI0qgM-Axo0MNdJ3aQW7bIGuuqyq8bQwQnUNfQwoz4tZ1on9-tDRuv5XMvufGWpuMUz0bDdRWb8Scz8K6eMOdlBkwcn8HO3ciRAZixySDIjbonAJUhY4X7F0S-wTyXAVKdg-tA9nniQlg9IYyTnnqF-Z6TMlnq9IbY31wx6r5MGJjRpvO_ShALOeJKayf5fj5jKgVBKG7YDyullE_XJkmu8RWx_A2yT7aew9wUjljLKEQXJX_I0Sng37ofdbytsISdR5gC546uMh9LLhFhyZeqNKKqTaQGQV-fXBEW3BITpB7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار تفعيل منظومات الدفاع الجوي في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84916" target="_blank">📅 22:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84915">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCOHFsJimlgO8oiWw7aRWQyUMMcsqdJ4CCcVvS1VRODFqMIFc0rsJL0ld_irMHjHLem7Y94Mpul3eCqYCpsu881J6zeVMOkkc9MnZ4PUzARYrfMCLGFSTdqc5X6ThoGjM2Y-k2km0u_rblJZDHHFVTbYUYHSfs1d4chJ2uly2e4mLqUazoP6Xs6LfNgz5AkLpgw-tsN7T8ukroQE-IKjRC1j_d4TBSoFl9z4VXBTaMu2AR02W7nGS3o1nZsaiIEM24aPPYH6CKumuSzhT1Xi93J3w1M5slV54_ZCuP0DCXrPmVkj9x7x2UDsM9UBrpg-4wVXj3heRzDOkrnV-6uXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇧🇭
🇰🇼
استاذ جامعي في قطر :
يجب أخذ احتلال ايران لبحرين والكويت على محمل الجد
😱</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84915" target="_blank">📅 22:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84913">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21af8b296c.mp4?token=nia9hcgVFUG0oKSKD_Q_suIeDdIoQxvJ_w0rSS2iLNt4F6ZyaD-UP39yqxzIYDrCOv8WoGYA1qD1Trd5S91Ldw5NfIrBYXJcVrCJKGK6HfO-wWssdjM-tvvzIYFnMFGL-m0CH8KgByUoyEPV8HMXh7FB5rq0g2-01uICqj4SLELZlSJ5gFUAUGOfX0ZSqG1R6-bYEYZBUZmUngYEkHJeGMNwrEjLmy6eGOzOqYGK1XBF48otlDizPMOiqD5Z6rFwJyzZ_bTLhA6-5JG9riPwvLtr8VSz-uza-nqQHF34lCKFQInczukhePn1S7LOT4yXTUzdlIsCEP0t06GBQXYXYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21af8b296c.mp4?token=nia9hcgVFUG0oKSKD_Q_suIeDdIoQxvJ_w0rSS2iLNt4F6ZyaD-UP39yqxzIYDrCOv8WoGYA1qD1Trd5S91Ldw5NfIrBYXJcVrCJKGK6HfO-wWssdjM-tvvzIYFnMFGL-m0CH8KgByUoyEPV8HMXh7FB5rq0g2-01uICqj4SLELZlSJ5gFUAUGOfX0ZSqG1R6-bYEYZBUZmUngYEkHJeGMNwrEjLmy6eGOzOqYGK1XBF48otlDizPMOiqD5Z6rFwJyzZ_bTLhA6-5JG9riPwvLtr8VSz-uza-nqQHF34lCKFQInczukhePn1S7LOT4yXTUzdlIsCEP0t06GBQXYXYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من تفعيل السيرام في سفارة الاحتلال الاميركي في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/84913" target="_blank">📅 22:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84912">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad072cc600.mp4?token=L536dQ5zMXkPVI9_-TQK5NV_6GyznY6mnwWfO7N_ABo_9ignbJABn4-MZ8uoUAzeb6pYB6lRf2kEQ93YyyRF2vtowwd-mxWZKz-Bz4HMyvygbVfmEDAV_kML1R7ecXMwIOyM5QKSUHDxmqaf4Z1TKoES-tHz2cgy_0fUc-BkwyjVay99qfSoqhOu65s_zWvROUxLlSzFBQb-T-TrgE43RBrKjERSBjv-dZciWKbFJhDzFo7E7hcX4lpHNX7r9JANJldvKW1twcAYNl8kX9tFCSfTTeqbVCsczxBCXxmFyMTiguMz-UGz7tTz_MuKFOq152BinAhkhxL9yBrwDOZsLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad072cc600.mp4?token=L536dQ5zMXkPVI9_-TQK5NV_6GyznY6mnwWfO7N_ABo_9ignbJABn4-MZ8uoUAzeb6pYB6lRf2kEQ93YyyRF2vtowwd-mxWZKz-Bz4HMyvygbVfmEDAV_kML1R7ecXMwIOyM5QKSUHDxmqaf4Z1TKoES-tHz2cgy_0fUc-BkwyjVay99qfSoqhOu65s_zWvROUxLlSzFBQb-T-TrgE43RBrKjERSBjv-dZciWKbFJhDzFo7E7hcX4lpHNX7r9JANJldvKW1twcAYNl8kX9tFCSfTTeqbVCsczxBCXxmFyMTiguMz-UGz7tTz_MuKFOq152BinAhkhxL9yBrwDOZsLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل دفاعات الجوية في قنصلية الاحتلال الاميركي بمحافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84912" target="_blank">📅 22:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
انفجارات مستمرة تستهدف قاعدة الاحتلال الاميركي في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/84911" target="_blank">📅 22:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84910">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ثلاث انفجارات في محافظات اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84910" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84909">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKI8LT4mpMMiorh46l8SdVCGEgwvSSmcB7pmMa7W4f0Bc947DRbh6v92DframNwP-5Wk0iILK9QxOnDm7468CP4Ukegm4f288DqxguIA6bBDCnkMS9IES4zmwmkdP-7TNtlggNztIGBglHc6hIHRRcA4OfuLBrh64JA307sYIOtGyGWVUhe1FOXcFfm-SE86r-7IOTid80bDfEoxXUJUbv_HFu0rWnJdm0Mvy9I53MUf0Rw99Vv5A3W8p0Ukii7dky3zlTbxnvXea5_tSlKEotXz3p24nCHWvKfYeKANAjPZSRB4p29A-38mYt8SsZUpI-Gp_OsyblGMd7vTLG4-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
🇮🇷
صحفي كويتي متخوف من هجوم بري إيراني على الكويت ويقول اسألوا العراقيين ؟!
أيها العراقيون اتركوا له تعليق جميل
https://x.com/hamadalbaijan/status/2079819169067933854?s=46</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84909" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ثلاث انفجارات في محافظات اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84908" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb00f0f15b.mp4?token=i00yz_ETaJ8dHc6EzgbcVHuJX1ycHSsdfOOWcaRlKGNlQI14CGHpCblI3aYTq4LYVBLNF0dZPnCiCy15oBVNrPA48UhPyS6_858QVYL03QeoGt0S4Nqyb3dNLNtMV7Cs3IQSOEM1h1OxfApa8gxvIybJEw3owXNp9SIwRonclbnjNX7iqZWGNnZop_y2cmQB06Ze_oeOghD6OjTLLDHWpJBrkHahdlzUJikpGHR3km7EyfK2GSU6I1fNomx7AztembPyho8suilcRvSu1rc0ss0Tje4W01plh7ShIZO2e6w4hTyhr7Y2lP4M2NuwZ4YEYqyfsx7eRVReQcwfDcoXXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb00f0f15b.mp4?token=i00yz_ETaJ8dHc6EzgbcVHuJX1ycHSsdfOOWcaRlKGNlQI14CGHpCblI3aYTq4LYVBLNF0dZPnCiCy15oBVNrPA48UhPyS6_858QVYL03QeoGt0S4Nqyb3dNLNtMV7Cs3IQSOEM1h1OxfApa8gxvIybJEw3owXNp9SIwRonclbnjNX7iqZWGNnZop_y2cmQB06Ze_oeOghD6OjTLLDHWpJBrkHahdlzUJikpGHR3km7EyfK2GSU6I1fNomx7AztembPyho8suilcRvSu1rc0ss0Tje4W01plh7ShIZO2e6w4hTyhr7Y2lP4M2NuwZ4YEYqyfsx7eRVReQcwfDcoXXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇷🇺
رويترز: يقوم محللو الاستخبارات الأمريكية بالتحقيق في ما إذا كانت روسيا قد ساعدت إيران في استهداف منشآت وكالة المخابرات المركزية (CIA) في الهجمات الأخيرة بالطائرات بدون طيار في منطقة الخليج، على الرغم من عدم التوصل إلى أي استنتاجات حتى الآن.  ويقوم المسؤولون…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84907" target="_blank">📅 22:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
قيادة خاتم الأنبياء المركزية:  الرئيس الأمريكي المارق والجريمة، القاتل للأطفال، يهدد إيران مرة أخرى باستهداف البنية التحتية للبلاد.   استنادًا إلى التحذير الذي تم إصداره الليلة الماضية، يظل مضيق هرمز مغلقًا، وإذا كان من الممكن أن تعبر أي سفينة هذا المضيق،…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84906" target="_blank">📅 22:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84905">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
قيادة خاتم الأنبياء المركزية:
الرئيس الأمريكي المارق والجريمة، القاتل للأطفال، يهدد إيران مرة أخرى باستهداف البنية التحتية للبلاد.
استنادًا إلى التحذير الذي تم إصداره الليلة الماضية، يظل مضيق هرمز مغلقًا، وإذا كان من الممكن أن تعبر أي سفينة هذا المضيق، فيجب أن تفعل ذلك فقط عبر المسار المحدد ووفقًا للإجراءات المعلنة مسبقًا.
في حال تحول تهديدات الولايات المتحدة إلى واقع، فلن تسمح القوات المسلحة الإيرانية بتصدير قطرة نفط واحدة، وستكون البنية التحتية للنفط والغاز والكهرباء والاقتصاد في المنطقة هدفًا.
التهديدات المتكررة من الولايات المتحدة الجريمة وجيشها الإرهابي في هذا البلد الشرير لن تؤدي إلا إلى توسيع نطاق الحرب في المنطقة وحتى ما وراءها.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84905" target="_blank">📅 22:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84904">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPkD7012SlNjtXgUjgL1tzIsKXt6vLOZ2v0o4pkcZ9Enk0yHAVbnHW-CXKX5bM5UiAezKtSeRmzaPfng224xVhD3JvTtyx84_n8sWVt8B2KSeUT5C0XXIhHmSImWgJ4E4U7sUD6PVWDrUrx0b6PHTxQqosodyTTnszSzCODDR0UOMI6hLZgpVQa4yUBa3iASkj_2PvbieEPsKznuNiCW6JgZ4G4Y0rNFH9y4tsWEYMWDWrphiRBM4C84nWoYLBIH59Eq8JBYrK9cYwjR9_fO_nRkqhd8hYRW4P0KLyy6DfSqGtEbMnMxi_pxUGVD6jwYStzdTcji7K3PyLlPkPKsFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇷🇺
رويترز:
يقوم محللو الاستخبارات الأمريكية بالتحقيق في ما إذا كانت روسيا قد ساعدت إيران في استهداف منشآت وكالة المخابرات المركزية (CIA) في الهجمات الأخيرة بالطائرات بدون طيار في منطقة الخليج، على الرغم من عدم التوصل إلى أي استنتاجات حتى الآن.
ويقوم المسؤولون بفحص ما إذا كانت موسكو قد قدمت معلومات استخباراتية حول الأهداف أو حسّنت تكنولوجيا الطائرات بدون طيار.
ويأتي هذا التحقيق في أعقاب الهجمات الإيرانية التي استهدفت مواقع متعددة لوكالة المخابرات المركزية، بما في ذلك مكتب وكالة المخابرات المركزية في السفارة الأمريكية في الرياض ومنشأة أخرى في شرق العراق.
يعتقد بعض المسؤولين أن روسيا قد تكون قامت بترقية طائرات "شاهد" الإيرانية، مما حسن دقتها وقدراتها في الملاحة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84904" target="_blank">📅 22:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84903">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0XEvYLzMC2wtE3veLoY2Q-Jji2ZfylnYmp9Va6adPme9s7T7R7qQNYZ5ljQt56XFEg4FhsrV-thvDSFQY2WmQmtlMMt_0fhg7f89ucX8Fd-zUs1FpJhomszoPDQ7OjDTY8bo8cyMhqy5G8X4r2WWbkN8LhyMTUICzGcX1AOPdFiG-4rvYo4BBnZ55Kyc9NdLZnnRHzKBtLv5l2RL3WVKGnUlpva11_EOAiaKe8WMH9YD41l2ar9q4WAS31kW1VTcTVXru77xEAdUnFhEA0kM9HaspQcKLZKwGQGCp55rRCnzinr5lgc3rVcllQKuuJUph2sOCvmzK2hC8A56cv_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
Significant</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84903" target="_blank">📅 22:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84902">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e223e42f10.mp4?token=i_b4fG1AznD04KBeyO0_y-Zdpa3IqzXpCWt1ux9zg71bnt2ItXwf4IDKJJzttyLS0mprnP7I90ZJyekz3Dh2a5EFnd09Wpao2z23Cu8rPk5zzwWMxiD5hW-z4B5fjIyQIrYwlQkKmbpdUwmL22yGzOCY_Ws-mYNddgk7BJEg-RC2lmQswy0wLZLCcNcWmpUVmlYciUgGG-7AcKWfUSgOwFDZobF41i3F6rvilf02e_fxIHmcxThNEAjGAR5xQ6UUOYb34J60yn6QCjtXFsjJ60NMTxeN4aXLgC63wSpqUdCoVuT3WVw8YsE6oDFUYa2fp54Czp7X73Jl5Fass-9yjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e223e42f10.mp4?token=i_b4fG1AznD04KBeyO0_y-Zdpa3IqzXpCWt1ux9zg71bnt2ItXwf4IDKJJzttyLS0mprnP7I90ZJyekz3Dh2a5EFnd09Wpao2z23Cu8rPk5zzwWMxiD5hW-z4B5fjIyQIrYwlQkKmbpdUwmL22yGzOCY_Ws-mYNddgk7BJEg-RC2lmQswy0wLZLCcNcWmpUVmlYciUgGG-7AcKWfUSgOwFDZobF41i3F6rvilf02e_fxIHmcxThNEAjGAR5xQ6UUOYb34J60yn6QCjtXFsjJ60NMTxeN4aXLgC63wSpqUdCoVuT3WVw8YsE6oDFUYa2fp54Czp7X73Jl5Fass-9yjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وستنهار قواتكم ودباباتكم وطائراتكم وتحملون نعوشكم تحت اقدام غفاري</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84902" target="_blank">📅 22:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84901">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCeH8iz21yDyxGpsQpLY0VyRK6jcriaLLG78w4jXMHytB_06D5LVLfvcZnnCXwW7mtMMiTK0Yw6CkIeC307Qx1WevBUn1mjJ99F51Wzy-WwkKuEVxDhHtWhJ9qTciuiU8JZRURe5MnBzkngY7kHG40XiSTJ-YUZOt4edWM8Z3d3Brr-ohCVgQPlaqWLCxxPVoXXS_YMXGM-wDd_hgs7niR997-Czt4rkxE8gzazdVeKwPSunZjt4EM4uSi6jmGsa2mc2btBrnGZSx06Ld9L71NXJT1PwaMSsYdJCa_ugfq4RXbBHFI6ozbU1NeuFAeGu_O6Wmb7M33siXvKqs1sytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقجي:
عقيدتنا الدفاعية واضحة العين بالعين.
أي عدوان على إيران، بما في ذلك بنيتنا التحتية، سيجبرنا على رد قوي و حاسم
أولئك الذين يساهمون في مثل هذا العدوان، أياً كان نوع الدعم سيتم اعتبارهم أيضاً أهدافاً مشروعة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84901" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84900">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRXzhOS11t41pyZlhzeXXlL-2YHcSeyQWmnmusveZvCizVUjPogZGGq9SmGR29oxQklM4IKbeGlbUc0VzhDTEJ_gQF3Yjh5ttphQMz8Eux_jBZ7BJzws5Dc-JC78xz7ePyarEevF4r8d1OBo5K58c9G4MotvWSW1gz5pgpRKFbhKUQT2oIw69SlBAGvx1wB_wNZk25NI3EUXbqq9P0p5WJY6d8pyTAfBNxaN4U3J-dH0cgouu_MknNTNSbGsTUn9D9LRqqsRKYaSmYZuAbCad67px6BgUQQ3iBJDxhAYKA_tK8zTmULZKvV-hM67ZDtlyDFOsrwCkXKmUhRuWiiGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
وستنهار قواتكم ودباباتكم وطائراتكم وتحملون نعوشكم تحت اقدام غفاري</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84900" target="_blank">📅 21:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84899">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCWsMZhf6K1RP1iMLfwehYgRyUCGFC0COFs2kWNUARjU8uqV6X7BXd5aIfSAVNVRxzMMtSIC7Q-IT8BIVIgoPdtCtyPqjHqn9S1MGxqV0splbuqbmPZgUWvboJnfycns2kT7E0H1_F6Qea8x7JPHJrBL-cx2PhQHhG8lonQxdKrgQ1W0UB_COhXRIclHsnLbfuST4EsBT0KTKWCvglLArtfPr5swDdojU2IrO47nWqIz5-YGg-SXY_TN7qu3QnmMv1Le73Ni5ni1ddVp04QvQn0AEcugGmCr-UGkGvF4KSBJdvno4oI4tBwDL2W8NkIMauHFAXwPILOzxIWaM9GDSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بحرية الحرس الثوري:
مدخل ومخرج مضيق هرمز تحت سيطرتنا الكاملة والطرق البديلة غير آمنة ونحذر من استخدامها.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84899" target="_blank">📅 21:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84898">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:‏ من المتوقع توقيع الاتفاقية الأمريكية السعودية في الساعة 20:30، والتي ستسمح للشركات الأمريكية بتشغيل محطات الطاقة النووية في المملكة العربية السعودية، وليس فقط توريدها.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84898" target="_blank">📅 21:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84897">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
انفجار في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84897" target="_blank">📅 21:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84896">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVQiBvOSSnscZX68UBgK04FMW24Zqs370CLcEfzpvlMklCpfJ_FtN6rdWJxE8jBzykSSO5PvRMXeuCz0ghd2iMCzg4La4T1gCt3bjgaqk6qE58oFTDukGg_7zdanguka1vzwWhxEIKe-DSJynIlggN1I7e6XvSO0iORExTT1pRtHo7bmVLoIz00ff7XEpo8XvmLmivIb47QBOmYBKieDjgBc0RG3eMaL027tIlaTGyKMDtGdo7uL74tUiVQZIt6NxsT_VovMkgifaq4xWKEMU7NGjkoWTAkk-sDDa70d-U9D0paTu5n84smLlbemtOSrsjegH2rl5dwAJAKDsBbQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يا قائم الـ محمد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/84896" target="_blank">📅 21:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84895">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة ارضية عند الحدود العراقية الايرانية من جهة الشمال بدرجة ٢،٨.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/84895" target="_blank">📅 21:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84894">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9adb07c10.mp4?token=jqtRUk-Miv3JFUwt7XOFurtuPqWiMEiGkqaEO7YPbrpVEVHhPj2x3rsa0h6gwS9ID8yltd4rQFBrBftjgrR7OwagDrFRcBvlzD1h9ndjwXKRcM2XfX_5pnhe2Vu07aML89CV5qjU7KIDHUOjT1G6dPuPlbBl4pHhw4-tOFEcjn_oZdTo2qrfWZd0sTSSPveynXMXF4AQC5oVFRoNBDTqOpW5w_KoITpnAwh10sn4eNNHjOOOc02FKvd6hqmNBobOIMdzXKd5mZ2t0kNNxe1AV3pN-p2DhkRaCIqdgcdm_aRmKwJyQUFltANptV9p_v4mCBsUFDfr4zH8n57A5IdIbEz99mpa3IgttpJL1fzYbSH0S_kv59VzI_HEUFe9QXAf9f-j-F5lJNjlCWO-jI6W1GKznYbxt3go5wK1Ubw4HpLY4xfqEE_OvRG1MSmXIYMizRPz0_e7p9ZMnPOd4m9V983fzJhhVy5YdBTvn2lL0Gvqb1OhjcJ_3YNRJVOigk2ZqjyprrTPZeqrPYiNl3AN-C5J8CLFCrWS7rhJB7yta3fxLkjfPTKe9ydMxYhhU_TBRB21zk9YbfqITWswW0uTqOo2jmWiO6scPc_H9caVYbz-5Bt16H96hwwdIM3ipehfkK8hGhg8Jf5Rg8WB7ntjVaGc1YtvvQw9NPA7CIQj1xo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9adb07c10.mp4?token=jqtRUk-Miv3JFUwt7XOFurtuPqWiMEiGkqaEO7YPbrpVEVHhPj2x3rsa0h6gwS9ID8yltd4rQFBrBftjgrR7OwagDrFRcBvlzD1h9ndjwXKRcM2XfX_5pnhe2Vu07aML89CV5qjU7KIDHUOjT1G6dPuPlbBl4pHhw4-tOFEcjn_oZdTo2qrfWZd0sTSSPveynXMXF4AQC5oVFRoNBDTqOpW5w_KoITpnAwh10sn4eNNHjOOOc02FKvd6hqmNBobOIMdzXKd5mZ2t0kNNxe1AV3pN-p2DhkRaCIqdgcdm_aRmKwJyQUFltANptV9p_v4mCBsUFDfr4zH8n57A5IdIbEz99mpa3IgttpJL1fzYbSH0S_kv59VzI_HEUFe9QXAf9f-j-F5lJNjlCWO-jI6W1GKznYbxt3go5wK1Ubw4HpLY4xfqEE_OvRG1MSmXIYMizRPz0_e7p9ZMnPOd4m9V983fzJhhVy5YdBTvn2lL0Gvqb1OhjcJ_3YNRJVOigk2ZqjyprrTPZeqrPYiNl3AN-C5J8CLFCrWS7rhJB7yta3fxLkjfPTKe9ydMxYhhU_TBRB21zk9YbfqITWswW0uTqOo2jmWiO6scPc_H9caVYbz-5Bt16H96hwwdIM3ipehfkK8hGhg8Jf5Rg8WB7ntjVaGc1YtvvQw9NPA7CIQj1xo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وَلَا تَهِنُوا۟ وَلَا تَحْزَنُوا۟ وَأَنتُمُ ٱلْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ
@Naya_Press</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/84894" target="_blank">📅 20:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84893">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انباء متداولة عن عمليات اطلاق صواريخ ايرانية نحو الاردن</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/84893" target="_blank">📅 20:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84892">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇱
‏
الاعلام العبري:
التصعيد الأميركي ضد إيران سيؤدي لتدخل إسرائيل إما بطلب من ترمب أو كرد على هجوم إيراني.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/84892" target="_blank">📅 20:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84891">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">واشنطن بوست
تدرس إدارة ترامب خيارات عسكرية في مالي ضد الجماعات الإسلامية المسلحة،</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/84891" target="_blank">📅 20:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84889">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ليلة ساخنة جدا</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/84889" target="_blank">📅 20:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84888">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تم إصدار إشعار للملاحين الجويين لمنطقة معلومات الطيران في بغداد لإنشاء مسارات مؤقتة جديدة للوصول والمغادرة من وإلى منطقة معلومات الطيران في طهران، اعتبارًا من 23 يوليو.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/84888" target="_blank">📅 20:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84887">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c060d1357.mp4?token=XZVnGqFrONhaHd4n3w--m_fqukv-FLN1aSuR3u2CbR5UeEz0p3YyKo1F3SmJ6MmkJ9DDAhva3wIQYzRGHOBZV7CYlVsdTA3pZn0W4hyx3Y95mRtHFnMK7sJT4XBOC3o4M5hFxmd84jaU0b9gNWcYVwuzfjEo-xi0dx2Ibnt6Fqd8wx5BZuypih1bZEqQohBycAO75fkjgqqv4gfonBti7ilv2EjQga5OvhtmLdvAgA0njMDW-ezdnXOuyLeEh4mnYTN0C0d0D61GA7cnNCDmbM1Wf9bEB8ahN8Ta5jbX1VnLHQpmIFRnw2Vv7cgzMNfjXjtWOTRe85CUg19LCPBiuFg3rg8h7Wo3NDHtSWSpyZYmym_r4ReewpAfoGSDR5F2iDZ7BNgZTIYFqAxKwwfb5ralL6O4BvPAaRpurFzvNbASD1BPIEhZ8dRSvgrtvmWfDvbU-tl2RnBSxk8Aa2J3LozM4P6pGJ3b_5r60CJm6pB0WbNX0ONS2UPKXVHRySbN4GPGvAdLolRVOxwHD4KF7JR8wAgf4S3nBnsWX0XfyP8nU0aqj44qpWfk6WLLD6NtqeIwriihpLZiRkgez-WCNee7o8oXVLooq2gX3XALTA92arPyfI86Mz_7-7nYhu2Q3kqaSJMqNHlZhQXsnBizl-T76wmpDaW2ckt1XW55KzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c060d1357.mp4?token=XZVnGqFrONhaHd4n3w--m_fqukv-FLN1aSuR3u2CbR5UeEz0p3YyKo1F3SmJ6MmkJ9DDAhva3wIQYzRGHOBZV7CYlVsdTA3pZn0W4hyx3Y95mRtHFnMK7sJT4XBOC3o4M5hFxmd84jaU0b9gNWcYVwuzfjEo-xi0dx2Ibnt6Fqd8wx5BZuypih1bZEqQohBycAO75fkjgqqv4gfonBti7ilv2EjQga5OvhtmLdvAgA0njMDW-ezdnXOuyLeEh4mnYTN0C0d0D61GA7cnNCDmbM1Wf9bEB8ahN8Ta5jbX1VnLHQpmIFRnw2Vv7cgzMNfjXjtWOTRe85CUg19LCPBiuFg3rg8h7Wo3NDHtSWSpyZYmym_r4ReewpAfoGSDR5F2iDZ7BNgZTIYFqAxKwwfb5ralL6O4BvPAaRpurFzvNbASD1BPIEhZ8dRSvgrtvmWfDvbU-tl2RnBSxk8Aa2J3LozM4P6pGJ3b_5r60CJm6pB0WbNX0ONS2UPKXVHRySbN4GPGvAdLolRVOxwHD4KF7JR8wAgf4S3nBnsWX0XfyP8nU0aqj44qpWfk6WLLD6NtqeIwriihpLZiRkgez-WCNee7o8oXVLooq2gX3XALTA92arPyfI86Mz_7-7nYhu2Q3kqaSJMqNHlZhQXsnBizl-T76wmpDaW2ckt1XW55KzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترمب يشارك في استقبال جثث جنود أمريكيين الذين قتلوا في الأردن والعراق.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/84887" target="_blank">📅 20:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84886">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/84886" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84885">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
ترمب يشارك في استقبال جثث جنود أمريكيين الذين قتلوا في الأردن والعراق.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/84885" target="_blank">📅 19:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84884">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
انفجار في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/84884" target="_blank">📅 19:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84883">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:‏
من المتوقع توقيع الاتفاقية الأمريكية السعودية في الساعة 20:30، والتي ستسمح للشركات الأمريكية بتشغيل محطات الطاقة النووية في المملكة العربية السعودية، وليس فقط توريدها.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/84883" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84882">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
انفجار في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/84882" target="_blank">📅 19:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84881">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
مصادر ايرانية توضح الاصوات المسموعة في طهران من ليلة امس سببها الدفاعات الجوية .</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/84881" target="_blank">📅 19:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84880">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f6e0d88c.mp4?token=P1BPn85hRWoo9Rodo01m0uho78B9XcECfXDhU6-UmDIpD_5Sf7rHIGhGY1SAVn12zJZ8CeG6RruWOEY2FVyDpK113qEdLnx1c2lFpMY-_fCGO7PKVecM-0pEbrnrvEQd4rmDfQuPX99BDPbfFEp1wVYYGdXZh5RXFtAVqKksDLAe4jStLlh0BlcdkvilbMpGpGgMyznMIeS6TnKfv49yqZhJ82wyfD_LhQ1eUC9tnwgnT2_Da07Ob29RLpuYqhF5FEIuf9cWWgOo0Ir3VbLvU7oUdeqT4DZy0IiMhgXxbG6SBsKwIcMQGhqHeg_inNmad-Pco39Ar9Qg9v6aS4Jx8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f6e0d88c.mp4?token=P1BPn85hRWoo9Rodo01m0uho78B9XcECfXDhU6-UmDIpD_5Sf7rHIGhGY1SAVn12zJZ8CeG6RruWOEY2FVyDpK113qEdLnx1c2lFpMY-_fCGO7PKVecM-0pEbrnrvEQd4rmDfQuPX99BDPbfFEp1wVYYGdXZh5RXFtAVqKksDLAe4jStLlh0BlcdkvilbMpGpGgMyznMIeS6TnKfv49yqZhJ82wyfD_LhQ1eUC9tnwgnT2_Da07Ob29RLpuYqhF5FEIuf9cWWgOo0Ir3VbLvU7oUdeqT4DZy0IiMhgXxbG6SBsKwIcMQGhqHeg_inNmad-Pco39Ar9Qg9v6aS4Jx8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
النائب ليو ينتقد مايك والتز بشدة
: "أنت لا تعلم حتى عدد الجنود الأمريكيين الذين أصيبوا في حرب إيران هذه! عار عليك! أنت سفير الولايات المتحدة ولا تعلم حتى عدد الجنود الأمريكيين المصابين! يجب أن تخجل من نفسك! يجب أن تستقيل!"</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/84880" target="_blank">📅 19:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84879">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
‏مادورو رئيس فنزويلا الشرعي المختطف في اميركا يصل إلى محكمة نيويورك لحضور جلسة استماع.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84879" target="_blank">📅 19:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84878">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">▫️
‏
غرفة الشحن الدولية:
الحوثيون في اليمن يوجهون تحذيراً لاسلكياً للسفن.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84878" target="_blank">📅 19:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjl9dMGqPWUQDbQe8IIKxGZ-88pHEHJQ8nK_VGc0KTZTTWowL4jnEBNCEpqFXoqGStAkkaw_lGH3pByo2RSzC3r3rF48dhm2_gp-TFucXjpU7msBErDXwC7Jy9f5aLHRGOKaVsmi6OeqRb2PTRunI4fUymFImrjMxrfIw9M2qUrPwG_N-L4zalGA9K_y71VA_Z7mNgAfxzguw0B4y0mwdSjF8rdB68OTJt4vk1FpbfHYsjZ2q7nE7_V8Hj0uW3UaoTi1TYA17sxMoOO-lBSiFUOell8EDqdfbR74cDruYmVvyat6fvYRqzLWLUGuTRjC-OpWbGnucLUNjyKIrl0O_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
أسعار الغاز الطبيعي الأوروبية تواصل ارتفاعها، لتصل إلى أعلى مستوياتها منذ بدء الحرب.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/84877" target="_blank">📅 19:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
مصادر ايرانية تؤكد انه لم يحدث انفجار في بوشهر وما شوهد في الاقمار الصناعية هو لشعلة نارية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/84876" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84875">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
🇮🇷
مصدر عسكري للتلفزيون الايراني يرد على تهديد ترامب:  - إيران مصممة على ممارسة سيادتها على مضيق هرمز، ولن تسمح بتحويل المضيق مرة أخرى إلى مصدر تهديد ضد إيران."  - إن عبور السفن عبر هذا المضيق سيكون آمنًا إذا تم ذلك بالتنسيق مع إيران ووفقًا للترتيبات الإيرانية.…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/84875" target="_blank">📅 18:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84874">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
🇮🇷
مصدر عسكري للتلفزيون الايراني يرد على تهديد ترامب:
- إيران مصممة على ممارسة سيادتها على مضيق هرمز، ولن تسمح بتحويل المضيق مرة أخرى إلى مصدر تهديد ضد إيران."
- إن عبور السفن عبر هذا المضيق سيكون آمنًا إذا تم ذلك بالتنسيق مع إيران ووفقًا للترتيبات الإيرانية. وإلا، فإن إيران لن تتخلى عن إرادتها الحاسمة في السيطرة على هذا المضيق، وتعتبر ذلك جزءًا من ضمان السلامة على المدى الطويل للمضيق
- إذا استهدفت الولايات المتحدة أي جسر أو محطة توليد كهرباء في إيران، فإن إيران سترد باستهداف البنى التحتية والجسور في المنطقة، بما في ذلك مرافق الطاقة التي لها فيها الولايات المتحدة مصالح
- الولايات المتحدة يجب أن تكون قد تأكدت تمامًا خلال الأيام العشرة الماضية من أن إيران ستستهدف أي هدف تختاره. لذلك، فإن مقامرة ترامب المحتملة ستؤدي مرة أخرى إلى فضيحته</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/84874" target="_blank">📅 17:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84873">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📰
أكسيوس:
ترمب يدرس استئناف العمليات القتالية الكبرى في إيران والتي من المرجح أن تشمل حملة مشتركة مع إسرائيل.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/84873" target="_blank">📅 17:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84872">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9424056a04.mp4?token=NKBKzJM8U8tHFfjmmiF2fHoG2bBJr9X40gyU8c3NLGK4y5Maj2Ou6CHixeZHLlCT5rP9NiyKoVlTUlxESqCMA8Jyg8jWz5e7tnti2RHIg1I-iHaJtS7a2mx2wPr4pKsv8dtPVVk9QnTbdAcbpTK7ycY-03UTj7smaKfuVS1FfpT-_hYgYGPCcAJCpsJIP6oiU7ASVD4q24g1Ghh2GyIt-0Npo11wuNm5g7BoK8IWB_RryizctygFxys1oO0hVP_-DrJGvn8gP86x8YVkMhY0eoLLDONer-TLl7oEMix531-XqqiMtLfmmwYngY2-X2DeJYc0A1z55b6KYt9nrDxcAoVni_acF0uKS9hQjyKOKhpMphad4Lf0oeA0xOvu1J2YD4tWqdW6PSbG5dv1fF4A-P_hbu_w2D6UYJOqihKSCTyw-68x055nfAjPhWkzV3zNNxvruF8xuudNxKNutHhWkFrq7onkD4METrO_0g-_LtV4fjMqqBIZXSB_qWf2VFmVCr7N8yG5Ep3aL6LtEW_Pmpp6kxjbRTlnbiX1QiFTHFBVQbxF_nm75WZ5HGs7mcRm7NyMTKStSDwjtKZAHHU34WHDAtvzhWUCfcOom1FBaIzz4UGw4WvOIJ3nQ1J0eoo8HSYB3mc45uutKTRBDAGRaCtoi-h7Ocgq1vjFFetJ660" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9424056a04.mp4?token=NKBKzJM8U8tHFfjmmiF2fHoG2bBJr9X40gyU8c3NLGK4y5Maj2Ou6CHixeZHLlCT5rP9NiyKoVlTUlxESqCMA8Jyg8jWz5e7tnti2RHIg1I-iHaJtS7a2mx2wPr4pKsv8dtPVVk9QnTbdAcbpTK7ycY-03UTj7smaKfuVS1FfpT-_hYgYGPCcAJCpsJIP6oiU7ASVD4q24g1Ghh2GyIt-0Npo11wuNm5g7BoK8IWB_RryizctygFxys1oO0hVP_-DrJGvn8gP86x8YVkMhY0eoLLDONer-TLl7oEMix531-XqqiMtLfmmwYngY2-X2DeJYc0A1z55b6KYt9nrDxcAoVni_acF0uKS9hQjyKOKhpMphad4Lf0oeA0xOvu1J2YD4tWqdW6PSbG5dv1fF4A-P_hbu_w2D6UYJOqihKSCTyw-68x055nfAjPhWkzV3zNNxvruF8xuudNxKNutHhWkFrq7onkD4METrO_0g-_LtV4fjMqqBIZXSB_qWf2VFmVCr7N8yG5Ep3aL6LtEW_Pmpp6kxjbRTlnbiX1QiFTHFBVQbxF_nm75WZ5HGs7mcRm7NyMTKStSDwjtKZAHHU34WHDAtvzhWUCfcOom1FBaIzz4UGw4WvOIJ3nQ1J0eoo8HSYB3mc45uutKTRBDAGRaCtoi-h7Ocgq1vjFFetJ660" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يتجه الى قاعدة دوفر الجوية لاستقبال قتلى الهجمات الايرانية</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/84872" target="_blank">📅 17:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84871">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
بيان بعض الدول المتجاهلة للحصار الذي يفرضه النظام السعودي على الشعب اليمني صيغت بصيغة موحدة، هل تقبل دول بإغلاق مطاراتها من السعودي وإغلاق موانيها وعدم السماح بدخول أي بضائع إلا بإذن سعودي؟</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84871" target="_blank">📅 17:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84870">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رئيس المكتب السياسي لحركة حماس خليل الحية: سنسير على ذات الدرب والخطى</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84870" target="_blank">📅 17:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84869">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
استياء واسع يسود الشارع العراقي بعد انقطاع التيار الكهربائي عن عدة مدن ولساعات طويلة بالتزامن مع موجة حر شديدة وارتفاع درجات الحرارة إلى مستويات قياسية ما فاقم معاناة المواطنين وأثار موجة من الغضب والاستياء بسبب تردي خدمات الطاقة في ذروة فصل الصيف.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/84869" target="_blank">📅 16:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84868">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامب: في أي وقت تطلق فيه إيران على سفينة في هرمز سنقوم بقصف وتدمير جسر أو محطة طاقة</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/84868" target="_blank">📅 16:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84867">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامب: في أي وقت تطلق فيه إيران على سفينة في هرمز سنقوم بقصف وتدمير جسر أو محطة طاقة</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/84867" target="_blank">📅 16:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84866">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoyMd6Q1mWy1DQ9UEA3YL-ml0uVkB4saTOFt6zVXqf6Y1lRbmj4kYUVGSK6UCaBbBp6o8ipv3gb8_f40fGdaWnUCrOAhgb-p0zC7Buz1TOHd6SQYYBOKhOLhhFwVElp2vIBx3vzcoRQLAJWYVNBlmnQq5YxlOcw83DxeCUVP1hse2sNeu_21uofCLItoYFkE-l2KcMMMS1dN1jh9XuUeH_KMPdRDBsgSUu_8o4vlx6e2BVMDfLu4fSyJEBAJpIXwlagTuZCq_I4Fy6YRpzUaWMmPRSHlF3xFX4vlZIXZK5vcJTYl_F52KF0mybDOyRsdXd1A-aURwd1IFauVV_barA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يوجه تهديداً
بشأن عمل عسكري محتمل ضد البنية التحتية الإيرانية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/84866" target="_blank">📅 16:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84865">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8Ygn_1TxphU7l0niGqiW34POiD5r48ZWdnzZU47ZcOW3ngOywhndyc2zrCIDCZV9_hrDPg_KglHAXdRltDwAkeYn3yzKE1C9YDyolQvNstcO2A2tt6goky7syrjJ_Y4_Qe-LcXaZNw5Kw0MqZip41y5I_ZFmYj3Ss8EmGHA9IPOvUP_AsHiAjXoJTsxOgKMMzcMh5VZXxgNKvE-0J5y2AnAQb6T5Tb9K86QUCmLHcazTUzr1lPseJjF2b6J4wmYPQRdme9C3qDlq_8mzDzNpNED5W5gBJgxh1EG1XQLFQvNOa_GuwhaK5pBiI-ZnssGVotZN-njvbQj8myGGivvDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يتجه الى قاعدة دوفر الجوية لاستقبال قتلى الهجمات الايرانية</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84865" target="_blank">📅 16:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84864">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9234603b1.mp4?token=MM1KDfkqoafIqMefFgU1HF3WnG0JoGsTRGx2BYEQgl8g0ALoPeD281o7pUa8YKk-QGUWeaUtve1R5Fw0okB0Wqb47i6eoRezFi4kP6WzQ70Nxi7P0-H4dWx3suArmo3YnfRmTEEsBOdHaDlOn041LO-Gq4xiCawp8TMWH5h6LhbqAniVIcjx_NmgBqc5tzqAyOv1jBjPOseVsd9yZtJyA6StROZQ97Mn9fCV2m_xcVWvk94mSY2wJRzIEG4-EOBkF0JweYfbzeG3eakLhN-Q6NIVzDGKPEEVJzpo98zJpl-CyAmmMK7axMi3DyzWMfQiGIc30E_5W9GCeydJlw45og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9234603b1.mp4?token=MM1KDfkqoafIqMefFgU1HF3WnG0JoGsTRGx2BYEQgl8g0ALoPeD281o7pUa8YKk-QGUWeaUtve1R5Fw0okB0Wqb47i6eoRezFi4kP6WzQ70Nxi7P0-H4dWx3suArmo3YnfRmTEEsBOdHaDlOn041LO-Gq4xiCawp8TMWH5h6LhbqAniVIcjx_NmgBqc5tzqAyOv1jBjPOseVsd9yZtJyA6StROZQ97Mn9fCV2m_xcVWvk94mSY2wJRzIEG4-EOBkF0JweYfbzeG3eakLhN-Q6NIVzDGKPEEVJzpo98zJpl-CyAmmMK7axMi3DyzWMfQiGIc30E_5W9GCeydJlw45og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
تصاعد أعمدة الدخان بعد سقوط مباشر لصاروخ إيراني قرب إيلات</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/84864" target="_blank">📅 16:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84863">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEcH8Oqef0SaKHNkjF2NtZ3_iYM3bd8AChIdSZ7X67APeOJo_d0b_KtOsRLeNRcepXta50axQ6Gh60oSrLEWT7a3cLYgpW0zEqG_8M_RTTPx5hEInpQp1NA88OQFYrA5zHY8plYKLdIyimRd9X1wg0ycnzAocZ7aH5Z-OcVDiVkRQcDGXXFa8G-cxsFIOSdQ96j_8t_QuaWpQtI4cSM_5FgiOLRadn_PZ9fP9LThw8cxAZHy854tH6n4lZLVySsiwY1_7kczMx2voc551pYqmjI3FZEqyKQlnNOYaTT9fHeNeGl7P7pkNEPneBsv7d3bWYMpXj62pydqc9LdySZXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇮🇷
مواطنة كويتية تعاني من قيام طائر الببغاء بتقليد صوت صافرات الإنذار نتيجة كثرت الهجمات الإيرانية على الكويت
واسوهم بالتعليقات واتركوا تعليق جميل على الرابط ادناه " يا كويت لا تخافين "
https://x.com/albfatmah/status/2079838707947905163?s=46</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84863" target="_blank">📅 15:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84862">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txA24Q_jZKbiWj1aMej0pYHda_A7QXpCuNxATtpMjuVXikY4UEGSFpKU_8CAt4ZH-sEXSzjaB2WVv5i0Kh_1lsSnaZxCQPxmuZPpU9DGZEfROQ8nkQItd3s5R5Mo7RVf--fyUAXVVmXaAXBdMsMX57mo8fSgbBVQR_t5fKSTIxlEJTdpVXXWfjYQVnxffP_hzR0Mav2kueA_47zHBsWWZ3--Xv8o3JLWw_Du3Kbo3-Hs54eiXuso2dwXy2NNeuJIC8RgZeRhZQxwdnx7Bda8gnMgz2shwMuwWU0q2I05fDddGtHxmDtsi1nKSD8LK5lxDqPN85xZN8NOoAvjWmNCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشاط جوي مكثف لطيران البحرية الأمريكية في سماء الإمارات</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/84862" target="_blank">📅 15:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84861">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a4614820.mp4?token=cDF64zEBC5KwrCNLYAaD7x9h821E1JlPNY0BaDRaFFdYjYRnAHAoXbgVL2FjLNRX0TamBSFsMp58xlj7tGLghqPbPlNtrIVBB1lzz-IYfqKjDdsz0zxzP6nqp1hMVE5GlFFkCJgICvARtjgwQ2TBIAgZm23fKv-uqsBAH5Xs9x-An57vNuPAnNOhva1d9WUBaGshJnwent7IkU2iPwqgs5SDoarTrTyQlMmj74G7eOsegI0Uh4jMzPxi1OOLIv8hZgfJIz4n0ZRM5WqUtUf6u0tAR4BBAoQWRdBKXBuLGkyWudQ-idH2LN7Y8qKr_tVw0hBScKbjTVBnN0F6P3KNebmug6jTcc69g__Syd-8XImrLLC1lZGGe9yzTjWgk6ybsI2vMyqoj7-e9FZilEmXtuTqczIGpMMq7dYmCSk8mT4Q5KWLQgmM760LEzoHkerOZwy33ZoX6wuU7QLsO0M21H0jsYOiwwBsQsUy5D1AdabeP4mxvXEbbftVOnsPaQnGChvA_2KB7pYCPCPK1vJrZH8_lpYC7l-x82HAUqzZX_BP72h9RMjMN54Eo-GTIyi-CZ07m-QMKb6Jf4ZSu4CO_Pp2zdC6HxPEyp5CA1ppAH9jmktFtZuPExAEe91OQXJMIRtz5HKsdvaAoM3YcuOjLD3JID4oCLuVMLMhM5_M7ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a4614820.mp4?token=cDF64zEBC5KwrCNLYAaD7x9h821E1JlPNY0BaDRaFFdYjYRnAHAoXbgVL2FjLNRX0TamBSFsMp58xlj7tGLghqPbPlNtrIVBB1lzz-IYfqKjDdsz0zxzP6nqp1hMVE5GlFFkCJgICvARtjgwQ2TBIAgZm23fKv-uqsBAH5Xs9x-An57vNuPAnNOhva1d9WUBaGshJnwent7IkU2iPwqgs5SDoarTrTyQlMmj74G7eOsegI0Uh4jMzPxi1OOLIv8hZgfJIz4n0ZRM5WqUtUf6u0tAR4BBAoQWRdBKXBuLGkyWudQ-idH2LN7Y8qKr_tVw0hBScKbjTVBnN0F6P3KNebmug6jTcc69g__Syd-8XImrLLC1lZGGe9yzTjWgk6ybsI2vMyqoj7-e9FZilEmXtuTqczIGpMMq7dYmCSk8mT4Q5KWLQgmM760LEzoHkerOZwy33ZoX6wuU7QLsO0M21H0jsYOiwwBsQsUy5D1AdabeP4mxvXEbbftVOnsPaQnGChvA_2KB7pYCPCPK1vJrZH8_lpYC7l-x82HAUqzZX_BP72h9RMjMN54Eo-GTIyi-CZ07m-QMKb6Jf4ZSu4CO_Pp2zdC6HxPEyp5CA1ppAH9jmktFtZuPExAEe91OQXJMIRtz5HKsdvaAoM3YcuOjLD3JID4oCLuVMLMhM5_M7ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المتحدث باسم القوات المسلحة الإيرانية العميد شكارجي: تم تدمير مركز بيانات ضخم للعدو في الإمارات في الحرب المفروضة الثالثة. هذا المركز أُنشئ في الإمارات على مدى 20 عامًا، بمساعدة واستثمارات الأوروبيين، والكيان الصهيوني، والولايات المتحدة، من أجل السيطرة على المنطقة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84861" target="_blank">📅 15:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84860">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
مصدر بالحرس الثوري لنايا
أوامر من من السلطات العليا بالحرس الثوري بتوسيع دائرة الصراع في غرب اسيا وان الضربات سوف تصل لمناطق غير متوقعة بالساعات القادمة ..</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84860" target="_blank">📅 15:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84859">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/84859" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84859" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

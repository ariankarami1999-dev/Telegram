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
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 15:38:44</div>
<hr>

<div class="tg-post" id="msg-85074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فرنسا تخلي فريق سفارتها في طهران</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/naya_foriraq/85074" target="_blank">📅 15:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85073">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXWq_eK_tcMz2yU6wlmZsc0xY1DHk-Hri2LZCHDS33Z_V9pi8HHD8yIBhkiz4LDhuYzeiBHG247wSF89MYakwuM_o9Ua6JXPgrX7eawTcI13RUTUJM-BCowVhTkI-ehxwG8xwiVyBB-DolL-I6-LGfD3GkpxwDudOW_9BBAmsZKPpR3fFvmhdSEUbyVX79bfp02W0kfKFTupCxGOT6KlS_oI4Y3zARY3hx9EOlOzZ_F1zerrlNmAZu1_N1mgp0p7_Mtc_kKXHqXtmJqtPwqxxQiVetkhotG5oKhv-n_UknT1bhpF6X4W4aW4QrE3v_-uw6Qv_5y4zDDWwPj6gi-Rww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسالة مهمة بعد قليل نسترعي الانتباه</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/naya_foriraq/85073" target="_blank">📅 15:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85072">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسالة مهمة بعد قليل نسترعي الانتباه</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/naya_foriraq/85072" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
عراقياً
فراس مجيسر عضواً في مجلس النواب بديلاً عن حسن الخفاجي الذي حكم قبل قليل سنتين من قبل القضاء العراقي</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/naya_foriraq/85071" target="_blank">📅 15:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85070">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMVP2kfufZDmjgSBO2pXdZyAYmeQ4uCQahBDzUTGhZ9agfUwJVqn2S_lr9NiOXfngcPf2w82zGnAK4OROD9o_RSzzVCQQwPHtjTzdlehBu1qM9jGd7_Nl0OU9mgVEtyl6mt4OKd1Xzk5Lz1oZc4aPX7UL0Ak4FHzybdpk1Cj0ahUGLqCKQgc3pcyeH-446LDzqGGIeM6WCbK6qeZ6D7YEt5X0wEZWPU3Y1e5LtFEgHkaqkjhKl_OSCqJvlKg--9YDt3dMT-iP3wgK0cljj0r51KeSP-WBdNHnMdEp5rQ-P65CgZtrfoza44IH1aP-GL3TXy4vr08Us4-xKT5I9mf5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب: الولايات سيتم الموافقة على الاتفاقية النووية المدنية بين وزارة الطاقة الأمريكية والمملكة العربية السعودية، والتي تتعلق فقط بالاستخدامات غير العسكرية (لن يكون هناك تخصيب للوقود!)، ولكن بشرط مشاركة المملكة العربية السعودية بشكل كامل في اتفاقيات أبراهام…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/naya_foriraq/85070" target="_blank">📅 15:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85069">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏ترامب: الولايات سيتم الموافقة على الاتفاقية النووية المدنية بين وزارة الطاقة الأمريكية والمملكة العربية السعودية، والتي تتعلق فقط بالاستخدامات غير العسكرية (لن يكون هناك تخصيب للوقود!)، ولكن بشرط مشاركة المملكة العربية السعودية بشكل كامل في اتفاقيات أبراهام الموقرة والناجحة. الولايات المتحدة ليست ضد المنشآت النووية المدنية (غير المخصبة).</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/naya_foriraq/85069" target="_blank">📅 15:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏الجيش الكويتي: منفذ العبدلي مع العراق تعرض لهجوم بمسيرات معادية</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/naya_foriraq/85068" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85067">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
الاعلام الرسمي العراقي يؤكد ما انفردت به نايا: الجانب العراقي تلقى إشعاراً من الجانب الكويتي بإغلاق منفذ العبدلي الحدودي بشكل مؤقت بعد تعرضه لقصف بطائرة مسيّرة.</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/naya_foriraq/85067" target="_blank">📅 15:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85066">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوي صافرة الإنذار داخل قاعدة التوحيد الثالثة في السفارة الأمريكية بالعاصمة بغداد</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/85066" target="_blank">📅 15:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690c07aa39.mp4?token=v8x7jNQR4EzNm-TRRqmPUx75C-VoehBXW9tu6IE0So2gJd0fCGyjnSGKpEiSdC1X9Rjr1U1hlMunailF3irfE4mScVE6e5ETSRVmDqHfDGiXU_lzcFKyIKruBrMpXNB1TMnoSy6rfHL_aT3-sAySEof6XXy3PruLVlktsvs_YQPwKuafieIwN7f2EEgKHhrXvdiO-F-m4vj62LXBnSl8cuhIAvQUI_KwsvsJ6yQTtrxmsVMkwbjqtCvnm0P0kryeKpMz6J1vQwC-GCU3pC8SvIXtkk8b22fAz3dxxdQUPlgOh18CPpUNv30DuGzcq1iTIRlrRZWf0L-lEgEs6q6FZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690c07aa39.mp4?token=v8x7jNQR4EzNm-TRRqmPUx75C-VoehBXW9tu6IE0So2gJd0fCGyjnSGKpEiSdC1X9Rjr1U1hlMunailF3irfE4mScVE6e5ETSRVmDqHfDGiXU_lzcFKyIKruBrMpXNB1TMnoSy6rfHL_aT3-sAySEof6XXy3PruLVlktsvs_YQPwKuafieIwN7f2EEgKHhrXvdiO-F-m4vj62LXBnSl8cuhIAvQUI_KwsvsJ6yQTtrxmsVMkwbjqtCvnm0P0kryeKpMz6J1vQwC-GCU3pC8SvIXtkk8b22fAz3dxxdQUPlgOh18CPpUNv30DuGzcq1iTIRlrRZWf0L-lEgEs6q6FZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇰🇼
صور الأقمار الصناعية الجديدة تؤكد وقوع أضرار جديدة جراء الضربات الجوية في قاعدة علي السالم الجوية في الكويت بعد الهجمات الإيرانية اليوم. ‏دُمرت عدة مبانٍ، يُرجح أنها كانت ثكنات للجنود، ولا تزال أعمدة الدخان تتصاعد من الموقع.</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/naya_foriraq/85065" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">يوم القيامة في الجانب الكويتي   إغلاق منفذ العبدلي وخروجه عن العمل</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/85064" target="_blank">📅 14:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
🇮🇷
وزير الخارجية الايراني عباس عراقجي: خلال المشاورات مع المسؤولين العراقيين، سيتم بحث ومناقشة موضوعات مثل اتفاقية التعاون الأمني بين إيران والعراق، ومسألة زيارة الأربعين الحسينية، والقضايا الإقليمية.</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/85063" target="_blank">📅 14:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85062">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
🇮🇷
وزير الخارجية الايراني عباس
عراقجي:
خلال المشاورات مع المسؤولين العراقيين، سيتم بحث ومناقشة موضوعات مثل اتفاقية التعاون الأمني بين إيران والعراق، ومسألة زيارة الأربعين الحسينية، والقضايا الإقليمية.</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/85062" target="_blank">📅 14:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85061">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fa914cc2.mp4?token=jlWeIbjCgQWseuB7CKkzohFH6dUrJBGMBCz3aXB_xGzw7KIzfLbF2w1No_Px_1Uv84o29Aupgl_dEB5RGbzva0odhe4v1a4c3CdumESSNbWgf71fgm65nU9cZOszM675LK3gn1JwK63k9ETT2abg24Yp2oez3nRgx0Xl6K64_r6pKywQEdwynq1R1dTt3Wwm2Ym6--KIowB2yXL-CowwIWXvfkKdI2V4kZPlUys6NmBpLjciIrlPHRB6suchok7CzTasERr3dabED4Dksw2XhjdDWA8iuCNDYSRhJ0lchowmeNL1voogmfN5TOIQumxDtcVJSsNeVzawDw2c_hyfBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fa914cc2.mp4?token=jlWeIbjCgQWseuB7CKkzohFH6dUrJBGMBCz3aXB_xGzw7KIzfLbF2w1No_Px_1Uv84o29Aupgl_dEB5RGbzva0odhe4v1a4c3CdumESSNbWgf71fgm65nU9cZOszM675LK3gn1JwK63k9ETT2abg24Yp2oez3nRgx0Xl6K64_r6pKywQEdwynq1R1dTt3Wwm2Ym6--KIowB2yXL-CowwIWXvfkKdI2V4kZPlUys6NmBpLjciIrlPHRB6suchok7CzTasERr3dabED4Dksw2XhjdDWA8iuCNDYSRhJ0lchowmeNL1voogmfN5TOIQumxDtcVJSsNeVzawDw2c_hyfBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
لحظة إطلاق الصواريخ الباليستية "حاج قاسم"، "قدر"، "فتاح"، والصواريخ المجنحة "باوه"، والطائرات المسيرة "شاهد" ضد القواعد الأمريكية.</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/naya_foriraq/85061" target="_blank">📅 14:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85060">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
محكمة جنايات مكافحة الفساد المركزية العراقية تصدر حكماً على النائب حسنين الخفاجي بالحبس الشديد لمدة سنتين عن جريمة الابتزاز بمبلغ قدره (500,000) دولار فضلاً عن تسجيل نسبة (40%) من مشروع حوراء بغداد السكني لمصلحته باسم أحد العاملين في مكتبه.</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/naya_foriraq/85060" target="_blank">📅 14:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85059">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اغلاق منفذ سفوان من الجانب العراقي بعد تدمير المنفذ الكويتي المقابل له</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/naya_foriraq/85059" target="_blank">📅 14:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85058">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇨🇿
تحطم مروحية تابعة للجيش التشيكي ومقتل عدد من طاقمها.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/85058" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85054">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآية الله السيد مجتبى الخامنئي</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgXIGIxfRuV5ZIVpgN7WUd6Mheg_5V_aiTX_6kE9toTwH3o_QQ1B686NSU1GtxNjLfpMAb8QF1KKJVzXZ-GYp5LC3mkj-sxZ2doDCrsRQNgGJxhBHIY0vJAYB0Bxm-9E8XmmFoDzWWybzV1qW9EjrRRaf30k5jC5Uh7GlcPMMYdoVMLdiezIdU8w1moIlc-g5bmKTAvIXYnH0l9oZTbmuM6c-2cEyCf4zXfWUP6FNJM5FHzFZ5T5FfsQiHwHoyJ27TdeNiTPOsSeaoQyq48wtdadYK_QNSKSkjC9q7b1bRz0jQ39PHC2PfeKuU_XETPG45L9Q3wEIDemplkTAOyI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiaNgptFXUOBAJzM60t7lAusvqeB2V8tUFFQDOLghLy0GrO-gWkuo_rtS0D0CgLKmq35dSovGxWUHjQCItkyynCTgXUD58WTAY_r9L5OQ6B-14U-gMIgMzYe3UWvtKmZ12GMd5SZpL9H0YsbNHtysSwrbGNUNlWwROLSQ5rdeJPRnXdTUzYM6ornvlsfogTJiqNwP4LuQM-CJz4vh_DH6usER5TUfdNYcwaCxyD39G3_Tz54LI2L7iRQScT2URotEsqIHshuJA2WmhiOHCblwGOetEskKw_IC0w3tOp3BmNOMwB9HxkVx-QEG6ajMlmzjqGPUuV21sfBfpUX_VJRPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyRc-zXpOB2X-9XUYf119dLhCipJgkKP0vBRCgdERS-YKuPhFC7lc0qgDQYbLLntO18zHQGTj8XUAq942NXtbshJk2-puYa5RbwPctwZEsn2Nyc7mbKevdzkwzxKkWlymbOp9fUwtTUuUYrGtJcZKHWmuUO-j2QuieDp6_DQqewbjSz-YZow_oCT4F4_LwQGkmuX413vOCDhi6H7-KOKsmEPwtPQUJapOqWuk-OrdUfk7N30Cir3dniMR5NqakHW0_U1mUINqNu0hdXRbpcjkXrm5KzsDfyFg5U_9DWX8csLi0voxBtL09dFceW_BkF7D7Ol86DBrnLrY2MzfxdBSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xf27GW2NX-bH86i51Bv3JEnUieE0BuVDPBBHADSJFTvf-s3FX700AUSMOkVHSWJO8fugWbIWxK3RlYuScPxQViJrH9VgP7qCrJ5dP2oizLnFNa6bTw7InDlOJ6RiTFvxn-9V13sa5-PvPKICSDsXTBz2hn4o2oYFT4YDzF-RZjDPt6BXsiD4aIqWKXRad7c1qMdZ9DMMmJjXOAGSt-nHiD5VUpm7qdGAl6l5fMy2xaMGSaskko1AnVm43nSe6U8Fh1sAokLNHUL8LPQ9sb5GHezub13xyz1OvxlCwjlmTG8h3_K2g8Xo7qNPGUKEUdNex3X7Hn5FLQ2A22ESE82KLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
لا ريْب في أن قادة الاستكبار قد ارتعدت قلوبهم هلعًا..ورأوا كيف ذهبت تلك الأموال الطائلة التي استثمروها لتخريب العلاقة بين الشعبين [العراقي والإيراني] أدراج الرياح.
🛑
مقتطف من رسالة شُكر آية الله السيد مجتبى الخامنئي إلى شعب العراق بشأن تشييع إمام المستضعفين | 17/07/2026
📍
بغداد - ساحة التحرير
🏴
#قوموا_لله
#تشييع_إمام_المستضعفين
📲
t.me/mkhamenei_ar</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/85054" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85053">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اعلام العدو: فتح الملاجئ في الجليل الاعلى</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/85053" target="_blank">📅 14:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85052">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">يوم القيامة في الجانب الكويتي   إغلاق منفذ العبدلي وخروجه عن العمل</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85052" target="_blank">📅 14:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85051">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
شهود عيان لنايا:
طيران حربي يجوب اجواء البحرين.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/85051" target="_blank">📅 14:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85050">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bbe27969.mp4?token=ra1rmb9Xxnd_4L6S57LWwiTPo7Zd2aTZZ4rA6tmQyMmCMkgyfm2AsVQrVP_0XzflbBaPG5yTzNHPqs0XKo_si4fjW2EWLoG1TbLFTnaNjPhOR2XyocP5tfUz2WTdY1j5ve3dLwkphCeWOoJF8U_Sjk-4dPiywkvJKsCf_pvMybHTTNBTw-r4081GjWIcyN9wUPPdzm_fiK2TGfiDhJq0lTkFs6q1U7vhlYrXe33QsfkPo1XJND1TQLB_tZSCZ4Xb8Ch90AwUwMIz2Fa0QYFznpqxwVWFrLX4bPpkNKgnk6NdGqluVCMenFzp0Meof-SShOOm9I92ycr3njE1aHh33A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bbe27969.mp4?token=ra1rmb9Xxnd_4L6S57LWwiTPo7Zd2aTZZ4rA6tmQyMmCMkgyfm2AsVQrVP_0XzflbBaPG5yTzNHPqs0XKo_si4fjW2EWLoG1TbLFTnaNjPhOR2XyocP5tfUz2WTdY1j5ve3dLwkphCeWOoJF8U_Sjk-4dPiywkvJKsCf_pvMybHTTNBTw-r4081GjWIcyN9wUPPdzm_fiK2TGfiDhJq0lTkFs6q1U7vhlYrXe33QsfkPo1XJND1TQLB_tZSCZ4Xb8Ch90AwUwMIz2Fa0QYFznpqxwVWFrLX4bPpkNKgnk6NdGqluVCMenFzp0Meof-SShOOm9I92ycr3njE1aHh33A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يوم القيامة في الجانب الكويتي
إغلاق منفذ العبدلي وخروجه عن العمل</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85050" target="_blank">📅 14:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85049">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اعلام العدو: فتح الملاجئ في الجليل الاعلى</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/85049" target="_blank">📅 14:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85048">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c6c7a1b6b.mp4?token=Tvy2riEGKXvRHAe_lJJFz6HvLbZg12XLt-JfWyAJtHmwVvxiPu3zDQ1HkVnPKyCDQndE-TTN2C6P3cChjrTqdkDX4gjBv_nYnlrOqB0LhqJ4G2Wb14v37MOar0jc8geJJxTfTPKdJdvq_JK85m49YDh6ZEbOJfLSITGqgl-yiMQ7NfRTbrPYU_K1Z15JQvsFkuW4n6b5u3ekI-okh_dvvB42G89f_JKjXxA_j69fzMqOX6z8Z3Dn4mdxDmWVlZ00WNcF4sM7jQd9_-ACOUIwv1mSUdl6uIn-O0K1zlJ_he1cv21B3LvmYMkvOhe55p7gIOctYhaabo-YY1sU1NZmFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c6c7a1b6b.mp4?token=Tvy2riEGKXvRHAe_lJJFz6HvLbZg12XLt-JfWyAJtHmwVvxiPu3zDQ1HkVnPKyCDQndE-TTN2C6P3cChjrTqdkDX4gjBv_nYnlrOqB0LhqJ4G2Wb14v37MOar0jc8geJJxTfTPKdJdvq_JK85m49YDh6ZEbOJfLSITGqgl-yiMQ7NfRTbrPYU_K1Z15JQvsFkuW4n6b5u3ekI-okh_dvvB42G89f_JKjXxA_j69fzMqOX6z8Z3Dn4mdxDmWVlZ00WNcF4sM7jQd9_-ACOUIwv1mSUdl6uIn-O0K1zlJ_he1cv21B3LvmYMkvOhe55p7gIOctYhaabo-YY1sU1NZmFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العراق يعلن استئناف العمل بمنفذ الشلامجة بعد توقف مؤقت بسبب القصف على الجانب الإيراني</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85048" target="_blank">📅 14:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85047">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfFZ4tdB6LQCJ50XlwyC2PDfmmB5FNmtYPx1ObMWcUrVZvsbx5yUQMSFiZjsdKdOBb1JhCDCkRd6LNLQt_Tkv6SAkndnInjmwAUGg1RDAV3u2qI7l6RqKu5JX4gmMTyl4JVQbHt4xD6oeH4v-uW5WeTL22DoPBNtOxpD_kshnCX2Mecswdo2_KSB36bUo77co70hg1iLv8lPwaKkqkyvJTyQQmGNUQgbX5uL66bx3Bs9g9svhwN6NrUibmOXjA0FiJHvwUbSybi3xrSJDvdYdz2Gh31XBPxh7zK8eqO_MX1Pu0RtyCsvrI3EK5paqti8ACQyeT5tNa9NGgJdezjQow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الانفجارات في منفذ العبدلي</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85047" target="_blank">📅 14:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85046">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18e775f6a.mp4?token=MmxQlI2Hie88CoNHlQAtSKN7_k6kuT4dY-KSIAbcKmR6R7sczt0ZH5e4X5w1Dv-ILhSm9m1CFL8N_-nCwrqZwxzn0Kk7qO11SXvWRTrCrDQZW7HJIP2RNQ2kKXlMw_G6oTJ0bq_lPbv99mvdAykPbwa9jjSBrRlS-4CziEv-_cs50bDLMNLTgJ2OzC7LN2gbOqu-26qSb2Xb_ihMuo2oXOw6g8yxhAdRCk2qLisDhpVQEI1nz9BThvQGQsdwEjl9t8s8H5bu9_FWRMX-2zBYWtNEZ2VFnbE_gBXprwMXh8AIh8Lq1YbuAuX-TEn7RaK2E5oI8HnndLi0tXt5ZFdnww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18e775f6a.mp4?token=MmxQlI2Hie88CoNHlQAtSKN7_k6kuT4dY-KSIAbcKmR6R7sczt0ZH5e4X5w1Dv-ILhSm9m1CFL8N_-nCwrqZwxzn0Kk7qO11SXvWRTrCrDQZW7HJIP2RNQ2kKXlMw_G6oTJ0bq_lPbv99mvdAykPbwa9jjSBrRlS-4CziEv-_cs50bDLMNLTgJ2OzC7LN2gbOqu-26qSb2Xb_ihMuo2oXOw6g8yxhAdRCk2qLisDhpVQEI1nz9BThvQGQsdwEjl9t8s8H5bu9_FWRMX-2zBYWtNEZ2VFnbE_gBXprwMXh8AIh8Lq1YbuAuX-TEn7RaK2E5oI8HnndLi0tXt5ZFdnww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الانفجارات في منفذ العبدلي</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85046" target="_blank">📅 14:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85045">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50af4d9d9d.mp4?token=n9s9ugq56I5pxGXUxF9aHFqh6ut0zODoeLzvXj8faxL3_xl_I8vITBMjoRT7tVkOTL9wBRllyHUMuhvbR19fttIp1IzsiVsdfQ0gz75d8UWeXXIzLOKdo91zzegirmjWCSdvXolWwNnunv2pZ0o_yl9Z57DzaG6sEbJ3ps_fFT3pYCKlPI_NY-8qtjpegZvrcnLzYslWK9TCrWb301hVgOFKfl5vtbUwrv2fhVSqZarAxhC4PcKiu2ohTIdNl0OIJwifeTfoiSc60ZYR6BlT25Wxnldo-u-eSsFLTGP792yq1ZQVNacX0cQYHLD9MfmycUV9xNUe5bC4c4wY3BWrIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50af4d9d9d.mp4?token=n9s9ugq56I5pxGXUxF9aHFqh6ut0zODoeLzvXj8faxL3_xl_I8vITBMjoRT7tVkOTL9wBRllyHUMuhvbR19fttIp1IzsiVsdfQ0gz75d8UWeXXIzLOKdo91zzegirmjWCSdvXolWwNnunv2pZ0o_yl9Z57DzaG6sEbJ3ps_fFT3pYCKlPI_NY-8qtjpegZvrcnLzYslWK9TCrWb301hVgOFKfl5vtbUwrv2fhVSqZarAxhC4PcKiu2ohTIdNl0OIJwifeTfoiSc60ZYR6BlT25Wxnldo-u-eSsFLTGP792yq1ZQVNacX0cQYHLD9MfmycUV9xNUe5bC4c4wY3BWrIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر
منفذ العبدلي الكويتي يحترق بنيران حرس الثورة</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85045" target="_blank">📅 14:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85044">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الشلامجة مقابل العبدلي
والعين باربعة عيون
بيت ابو يمعة صبرا</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/85044" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85043">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmiafOTik4wY-IkkwA4K2Evuj-Xt69zcyR8HsXAVdSuMzx_2xa6xsd2ju4iK3AYzaiH0ykcv1JKG2uc29XCOxIoV3CsbmtyZDoynjS1GrTS0TGXxhqUrMLnpTKunNWpzsMrg0JQPTX4khQRDenpMXzbyM92P-GfuaV7kb2unwpEZcQZ5hyROjahCMUHoGmbG7YOguBr3FJSPfxYwgQ4jr4i4HIpUDuZhIgI9HFs18hjtTkFQKeijGVdX01zYQ3kHZmuE1ZEAr3QXSoZlyRH9sx0OrHYRi-C6qtMinNBUP32jDrOxR9zXR1DXBXIQWZ-BEIQeHLalyVXAiAL-eMFd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعمدة الدخان تتصاعد من المنفذ الكويتي</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85043" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85042">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3517028276.mp4?token=Bv7OT-p2pfqy3RFVYQ-kAm8PYPa3NxxORSN26Ph59ZOrCYkMF0kA5piSGNnNDFniVvFOiCQwftm7DCHQk11OHrREJO9y1ZD2Qh8EuXH54qz0AKYy6h0K7db-bji__71jJz7ib-3dPt_oLLFeHY67UjYT2rdkvE19dDmXIqaO3Q3PyxeOSwkn34QMqQKt42MoEzgKyGR3DsQCPl4tc4wsVJfAe8uRWEv-wTkonCYqiXINQkLlDDlgEWVWK8AUJZ8AINa7vJUIyf6SJ4psqwzzvnlCZQkgPKCv00EPOKqXBCrt70A-D9G_oOch2h1GPrUPHtlBZ2H6R7Ji0OMsDSG8ujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3517028276.mp4?token=Bv7OT-p2pfqy3RFVYQ-kAm8PYPa3NxxORSN26Ph59ZOrCYkMF0kA5piSGNnNDFniVvFOiCQwftm7DCHQk11OHrREJO9y1ZD2Qh8EuXH54qz0AKYy6h0K7db-bji__71jJz7ib-3dPt_oLLFeHY67UjYT2rdkvE19dDmXIqaO3Q3PyxeOSwkn34QMqQKt42MoEzgKyGR3DsQCPl4tc4wsVJfAe8uRWEv-wTkonCYqiXINQkLlDDlgEWVWK8AUJZ8AINa7vJUIyf6SJ4psqwzzvnlCZQkgPKCv00EPOKqXBCrt70A-D9G_oOch2h1GPrUPHtlBZ2H6R7Ji0OMsDSG8ujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من منفذ العبدلي الكويتي</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/85042" target="_blank">📅 13:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85041">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات في منفذ العبدلي الحدودي</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85041" target="_blank">📅 13:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85040">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85040" target="_blank">📅 13:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85039">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa0db633e.mp4?token=qLX64Qo7HZ4A1jsu8wpWGTmOMQoYSB8oVCsSy_wl9FgPgPtG53EYdlqIPYNM-Gw02lWyr1Y8O_RwBwzRNQsN2as0OuEQDLTy_KbY-0yyjkJKCY4fa6yhImdOEBCao3b28gN8mqaOpl_dw2O0S5xdN0vNzh1Jc-L-9cTaekkTn7lolKjNTaFZBRo65CgMoQuEIyRSJlFbPhy3SgWVfCP7-Sljjzh3SafNTtpfN63qsDD2EDaiUKJcLpw7xYJoyKTFlZn7iA-pQQ77M0UmX2439DxxkhgtP6ZGhPKJdmV7IFqGvvj3eBPmApqFbE2f1txQ3xyicwiF0d0IAtl_-HoGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa0db633e.mp4?token=qLX64Qo7HZ4A1jsu8wpWGTmOMQoYSB8oVCsSy_wl9FgPgPtG53EYdlqIPYNM-Gw02lWyr1Y8O_RwBwzRNQsN2as0OuEQDLTy_KbY-0yyjkJKCY4fa6yhImdOEBCao3b28gN8mqaOpl_dw2O0S5xdN0vNzh1Jc-L-9cTaekkTn7lolKjNTaFZBRo65CgMoQuEIyRSJlFbPhy3SgWVfCP7-Sljjzh3SafNTtpfN63qsDD2EDaiUKJcLpw7xYJoyKTFlZn7iA-pQQ77M0UmX2439DxxkhgtP6ZGhPKJdmV7IFqGvvj3eBPmApqFbE2f1txQ3xyicwiF0d0IAtl_-HoGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
الرئيس الايراني مسعود بزشكيان يستقبل رئيس الوزراء العراقي في طهران.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85039" target="_blank">📅 13:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85038">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇱
اعلام العدو:
تم الإعلان عن حالة طوارئ في مزرعة "ديرخ أفراهام" بسبب الاشتباه في وقوع عملية طعن. هناك مصاب خطير في منطقة الصدر.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/85038" target="_blank">📅 12:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85037">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تصاعد اعمدة الدخان من قطر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85037" target="_blank">📅 12:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85036">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تصاعد اعمدة الدخان من قطر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85036" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85035">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85035" target="_blank">📅 12:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85034">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85034" target="_blank">📅 12:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85033">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
حرس الثورة يوجه رسالة الى الشعب الكويتي
أيها الشعب الكويتي الكريم والنبيل،
إن إخوانكم في الحرس الثوري الإيراني، في سياق معاقبة القوات الأمريكية التي تقتل الأطفال بسبب تدخلاتها في مضيق هرمز، نفذوا هجومًا بطائرة مسيرة ضد مستودع كبير للمعدات العسكرية، ونظام دفاع جوي "باتريوت"، ومخزن للطائرات بدون طيار الأمريكية من طراز MQ-9 في قاعدة علي السالم الجوية، مما أدى إلى تدميرها.
كما هاجم إخوانكم أيضًا أماكن إقامة القوات الأمريكية ومخزنين للمروحيات في معسكر العودة. قُتل أو أصيب عدد من القوات الغازية، وتضررت عدة مروحيات وطائرات بدون طيار بشكل كبير.
كما استهدف المقاتلون برج اتصالات ردًا على الهجمات الأمريكية على أبراج الاتصالات في إيران.
في بعض الأحيان، يُزعم أن إيران، من خلال هجماتها، انتهكت استقلال وسلامة أراضي وسيادة دول أخرى. هذا الحكم خاطئ تمامًا. من وجهة نظرنا، فإن استقلال وسلامة أراضي وسيادة حكومتكم تحظى بتقدير كامل.
ما هو بالضبط القاعدة الأمريكية داخل دولة أخرى؟ إنها مكان يمكن للأمريكيين - وأي شخص يختارونه - الدخول والخروج منه دون الخضوع لرقابة حدودكم. في بعض الأحيان، يتم نقل أسرى من دول أخرى إلى وإلى هذه القواعد. يتم فرض الانضباط هناك من قبل الشرطة العسكرية الأمريكية، وليس من قبل الشرطة العسكرية لقواتكم المسلحة. القاضي الأمريكي هو الذي يحكم على الجرائم التي ترتكب هناك، وليس قضاةكم. القانون الأمريكي هو السائد هناك، وليس قانونكم. ليس فقط أفراد الجيش الكويتي، بل حتى وزير الدفاع الخاص بكم ليس لديه الحق في الدخول دون إذن من الشرطة العسكرية الأمريكية.
لذلك، فإن الولايات المتحدة هي التي انتهكت سلامة أراضيكم وسيادتكم، وليس نحن. نحن نهاجم الأراضي التي تحتلها القوات الأمريكية - وهي قوة لا تعرف سوى ارتكاب الجرائم.
أمس، أقام شعب ميناب الحزين مراسم دفن لبقية أجزاء أطفالهم الذين قُتلوا، والتي تم العثور عليها أثناء عمليات البحث تحت الأنقاض، ودفنوها بجوار بقية رفاتهم. كانوا 168 طفلاً قتلوا في اليوم الأول من هذه الحرب في هجوم من قبل القوات الأمريكية التي تقتل الأطفال. هذه الجرائم مستمرة، ويتم تنفيذ بعضها من خلال استخدام القواعد الأمريكية على الأراضي الكويتية. من حقنا الشرعي والديني والمنطقي استهداف المعتدي على بلدنا وقاتل أطفالنا، أينما كانت هذه الهجمات تنطلق.
نشكركم على تعاونكم.
"والنصر من الله وحده، سبحانه وتعالى، الحكيم</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85033" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85032">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسرائيل تفتح الملاجئ في الكيان المحتل</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85032" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85031">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85031" target="_blank">📅 12:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85030">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYXWrZkVU8U5DnEfwRG05tZ0H1UdqGdqcvISRSzV6KUKDSmydWqHQEgoMttuS8UdGD24sSZ6Chh30PrzmJ0utcXHPpHyKjnaF9sp93e615ZCXMdBWH_NoaZOzNLtPu8XNNPa8sCm2F0VZuhkTL-TB5VSeITudT7OcFrEtpggQw13-725tT7z9BjD7Wp2vawNdd77vmDQxnMO57PssEXKu0MhmrdLvhKvk8KcQs_GrwNZXyUDASWdZ4lY57xAIwapGrFLIr0jITkpJ1JGvlpjPv-30CZdVFGug9QAqh8RyXOlGOwv_CTJwXOHNm7WZr6Ac4lOaB_xBb-gZPzWPyV4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
النفط يتجاوز عتبة 98 دولار للبرميل الواحد ويقترب من 99 دولار وذلك في ظل تصاعد الصراعات في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85030" target="_blank">📅 12:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85029">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔻
مصدر امني خاص لنايا
القوات الأمريكية والشخصيات الدبلوماسية المهمة غادرت بغداد قبل قليل . دون اي توضيح عن الأسباب</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85029" target="_blank">📅 12:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85028">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5C75nfNsCy4xyy3AkObH44eTy48G3jw3C0j3NDbQmKyjwbRMLVW5cuMAdr0nemN4sR-hh5vidfowHHPyQBBUp4pV2PONbNtjvMsgOvP95B2_Jl237zzeTaq2P45Nqc80pKd0Zxnhqz89N1wKTFNGR9yIJXgpIz18Hq_jfFa2yW3sUWP7_h5ntlLCHRL_WUTEMCpXqCVRz-VGhvrqddp26bYtx9XzJN-WQXb2uKsTDggfVyP1JujR_z2j69NKxQZDnsYDGSYa49Rnbta0EpydMVLs-qKHTc6wakmQl2j--YFoWiIGPcRkyZgA3eN2KeYQ1pYrh25mh9AgDHE9nrPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق صواريخ إيرانية باتجاه قواعد الاحتلال الأمريكي في المنطقة</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85028" target="_blank">📅 12:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85027">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
🇺🇸
اظهر مقطع فيديو صوّره سائق شاحنة مدني في سيريك، جنوب إيران، بالقرب من مضيق هرمز، آثار إحدى الضربات العسكرية الأمريكية الأخيرة. ووفقًا لتعليق الفيديو، فقد استهدفت الضربة عدة براميل قديمة متروكة في منطقة نائية. وأعرب سائق الشاحنة عن دهشته من أن ما يبدو أنها براميل قطران مهجورة منذ زمن طويل قد أصيبت بما وصفه بذخيرة موجهة بدقة عالية، باهظة الثمن،هذا مثال واحد من أمثلة عديدة على استهداف مواقع ذات قيمة منخفضة في جنوب إيران , كما يصفون هذه الضربات بأنها دليل على يأس إدارة ترامب في سعيها لإنهاء الصراع.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85027" target="_blank">📅 11:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85026">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سلسلة من الانفجارات المتتالية تهز الأردن وسط فشل منظومات الدفاع بالتصدي للصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85026" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85025">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس مجلس الوزراء العراقي يغادر العاصمة بغداد متوجهاً إلى طهران في زيارة رسمية إلى الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85025" target="_blank">📅 11:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي‏روبيو: يبدو وكأن الحوثيين ينخرطون بالنزاع</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/85024" target="_blank">📅 11:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
إعلام إيراني: سماع أصوات عدة انفجارات بالقرب من كنارك.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85023" target="_blank">📅 11:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/85022" target="_blank">📅 11:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي‏روبيو: يبدو وكأن الحوثيين ينخرطون بالنزاع</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85021" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85020">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سلسلة من الانفجارات المتتالية تهز الأردن وسط فشل منظومات الدفاع بالتصدي للصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85020" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85019">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85019" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85018">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85018" target="_blank">📅 11:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85017">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تفعيل منظومة الباتريوت في قاعدة العديد الأمريكية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85017" target="_blank">📅 11:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85016">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجارات تهز قطر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85016" target="_blank">📅 11:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85015">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85015" target="_blank">📅 11:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85014">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8009f4f178.mp4?token=ebKRXqP6lTQqFoBxMu1VPcxQJjJg6Rppcg_AWoOZ-pIyWu9h6qGjbE1M-9ZG8H8wjHXLQx-RKivnveeGzwsPDTqLhCFkN6uCxZ1ed9m84GoT0E2nsfJcPFq6MMMf2IJIGGILagruw-OMX6YkRt_nzfuSr08Wb_8mFuzFJP7duDyL7c24QdeJij9E3Tv3XNx35E1E8TEC-c5caDnqBNjJK4Id4X5LmebH37Za5fLc2pJJZMwMQ64qZqm9T9TrwYG9vvjpTYl3Es43njh4I7woi-Yy0U20vg87tN2HGekAlYIfjZtO-Dz321w0pHyPbRwYhOvzUOzAfotL_BkPLP1qCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8009f4f178.mp4?token=ebKRXqP6lTQqFoBxMu1VPcxQJjJg6Rppcg_AWoOZ-pIyWu9h6qGjbE1M-9ZG8H8wjHXLQx-RKivnveeGzwsPDTqLhCFkN6uCxZ1ed9m84GoT0E2nsfJcPFq6MMMf2IJIGGILagruw-OMX6YkRt_nzfuSr08Wb_8mFuzFJP7duDyL7c24QdeJij9E3Tv3XNx35E1E8TEC-c5caDnqBNjJK4Id4X5LmebH37Za5fLc2pJJZMwMQ64qZqm9T9TrwYG9vvjpTYl3Es43njh4I7woi-Yy0U20vg87tN2HGekAlYIfjZtO-Dz321w0pHyPbRwYhOvzUOzAfotL_BkPLP1qCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صاروخي مجدداً من إيران نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85014" target="_blank">📅 11:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85013">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfq015XJsvvh1iAjvq0WomtJLuzZUMIFz1Fma2VKnRe49qMUYThLtbjhnne_XKKym2IKeOzPrYk0eQr-TBbMxUuO_ZL1bA-85uXulTD1kTIrACCZ0c72y_1SqAZewwGWT4xb5z7O8XxOz48kzDixo1Ect3zbXAYId2yp2wnr8IR4Lg_zCCMTJvQsoH44VMDho6KYpz5GVMU9MLDFhea9_8Ag-rgLNwHdMnCICHAnTmj53qpUUovz_j4mJF9GgToE-CV0CESC7r7JyTYHvtcNP-JuytzCcLKXMUQcMoDajIlbBE3u_3nQABM0Ie-K2AS60H99zWudTSQkxAw0IUFvXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق صاروخي مجدداً من إيران نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85013" target="_blank">📅 10:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85012">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الاتحاد الأوروبي: استثناء لنقل الغاز الطبيعي المسال الروسي إلى دول ثالثة لمدة عام واحد مع التجديد التلقائي.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85012" target="_blank">📅 10:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85011">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس مجلس الوزراء العراقي يغادر العاصمة بغداد متوجهاً إلى طهران في زيارة رسمية إلى الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85011" target="_blank">📅 10:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85010">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVzXJbN1cF4ABZxvPhMh7b_N0Se1L2vKMhybt9LMZqWP1H6p0S9eWbC_XnlZlYqp94s10cYzEMcNzVQW9m9dX4-27YNhBmozI6camQnRXaZzCB1qxchkAd185zq63X4PNXdAjCqr80S7nhIuXRfHL9XaA909Y5gCy9pAXW5PNnfOwAHJOD8k7yi9VazF6tisft7cEcxKb_c8uIVPh4KEnfNNtoi4WWkADsrsH5IOaJK7B-Lb0xBaqSVOAxQkdXchq7IclJeLjJB5nPOtp5wAwp60thOIB1KXLAyRw3LBZMqmmdZBnnPQ4Im7F1dmD_p9SUi9WfwjgbUis4BJ6exMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد لتحليق الصواريخ الإيرانية قبل وصولها نحو أهدافها</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85010" target="_blank">📅 10:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85009">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzKeBz6mWC1LKC0oEwvx8IeEybYwSM1d2L1Ig8nSN_I5pHetv691DRkxXKgxvVQgKSo_0kr9Tz0aij8UfQ2LNrslmYBYO4cBBjL90sssDM9H2HYqzgOhVkbxXBU9SO35XWCAvtN167o45iDGjaMz-9UTx7QaeVwUvVk5vrW31m2guVjWtSh7EnYv3sR9GxUM6t2PyuPzE6QvuFt6OCJaAEXAEZczjm2bxS3IgKMcJibLFnATcA8V42GaboHg8VeWNdHIq9psjeWD8Ckqt-TTOE5F1PwkRVYLN3sfq2IsU1Kn3oNyxJRuKiq-GoqRcHwu5i23oPyaY2VRUpde0ohn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاق صواريخ من إيران</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85009" target="_blank">📅 10:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85008">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0J0RXzsGaopyeCGds_4d16G9WJAITu4rBNtEREyE4ARGmRJRcIBnzvpamhJU8XfeUAJDidb0AP-w3pMDPw-2Du27812SD1YGCjcRsKsvYp66ffFU9AzWkWckieo01hRAppX9DK_UvFhqXJOLtuGCj_QqXGkGSR7K6YAkliGfRJsCtB2qlGh8V241Gul6x1ILdXnXDC5vdRP_CR-BQOFsScunSs-4itFIMLhtkiCmmQj6iiW2aYp1agDVellwzGbvJhRqeIJUQ6LcKNRUtWKMVqj9FDk82MpJQ5lvofaxVlaImtowYbOAmTBIfLuhgZeVQYnqnNxgZD6y2yK9Y6bXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاق صواريخ من إيران</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85008" target="_blank">📅 10:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85007">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85007" target="_blank">📅 10:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85006">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac3f27363.mp4?token=pLJDRs5XTFWNa2v8ead2QzX0THOkBBoet5-azSQDeHtST-fRZBTx94Td0eBL3edUQBhrMNajATJ3AX8bUfeAhNzyE2D2QKt7L9R2q1pPwFyMrZEAMduLl1mHYJPN6HEW3xWYpg35nI8_SSMAKcVXgVTXMP7BLY9T9sqPAAm6MFv6-aVNDzTNZgBSiOYyuZMDv2G2kaI3L_7Z_7GsSHKfDvmfuKkRN9l-yFU0SWeF2FV2Stl4g8b-oWa6sRhPUX_bnHXl4ZPZDI9WKyQOBmq-wez30P6MjfUdxdBTxJcSofDIPW5IVkoIxA5OpFBDmKQLUHu2Qk3e4x9BvoQUY9IOjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac3f27363.mp4?token=pLJDRs5XTFWNa2v8ead2QzX0THOkBBoet5-azSQDeHtST-fRZBTx94Td0eBL3edUQBhrMNajATJ3AX8bUfeAhNzyE2D2QKt7L9R2q1pPwFyMrZEAMduLl1mHYJPN6HEW3xWYpg35nI8_SSMAKcVXgVTXMP7BLY9T9sqPAAm6MFv6-aVNDzTNZgBSiOYyuZMDv2G2kaI3L_7Z_7GsSHKfDvmfuKkRN9l-yFU0SWeF2FV2Stl4g8b-oWa6sRhPUX_bnHXl4ZPZDI9WKyQOBmq-wez30P6MjfUdxdBTxJcSofDIPW5IVkoIxA5OpFBDmKQLUHu2Qk3e4x9BvoQUY9IOjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇰🇼
مشاهد من قاعدة علي السالم في الكويت حيث لا تزال النيران مشتعلة في القاعدة بعد دكها بالصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/85006" target="_blank">📅 10:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85005">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📰
رويترز عن بيانات ملاحية: 3 ناقلات محملة بالنفط متجهة إلى الصين والهند عادت أدراجها من باب المندب يوم الثلاثاء</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/85005" target="_blank">📅 09:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85004">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">📰
رويترز عن بيانات ملاحية: 3 ناقلات محملة بالنفط متجهة إلى الصين والهند عادت أدراجها من باب المندب يوم الثلاثاء</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85004" target="_blank">📅 09:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85003">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
مصدر امني لنايا
مبنى امني كويتي تعرض البارحة لهجوم بمسيرة مفخخة انطلقت من داخل الكويت ؛ المبنى تعرض لمسيرة كواد كابتر على ما يبدو من الخلايا النائمة من الداخل ..</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/85003" target="_blank">📅 09:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85002">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/85002" target="_blank">📅 08:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85001">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d4cf273.mp4?token=nK0YiQgpMQzmGBeKINttSziwOFnKrHjdlCVpQBu-6oxK53GHXqBXGXpcrnc3RliyNS4wTK_Dsi97RclkAK7wAIi8nWMUk6x7bRa7FcH041aN4v3N_eAUNYOXPh2EYQPvmtlOU4hW8ApKRCR68-6gjUVN99sOsYhB-Jkd9KqztntV8Jlj683wCIZKX1EQs7_JTELc2afbbY1KW0d6DwSM7wvNWhyyq_kY867NQz1OULsidIZEkf72323riGa0KPHj17DKBytqMqXDjMKrJfXHJ_Of7cwc_VJr3nhsZC7h-ytMNGlx0fJQKodeoEfd08sNjd2MuZF0GpBoIm8KON46zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d4cf273.mp4?token=nK0YiQgpMQzmGBeKINttSziwOFnKrHjdlCVpQBu-6oxK53GHXqBXGXpcrnc3RliyNS4wTK_Dsi97RclkAK7wAIi8nWMUk6x7bRa7FcH041aN4v3N_eAUNYOXPh2EYQPvmtlOU4hW8ApKRCR68-6gjUVN99sOsYhB-Jkd9KqztntV8Jlj683wCIZKX1EQs7_JTELc2afbbY1KW0d6DwSM7wvNWhyyq_kY867NQz1OULsidIZEkf72323riGa0KPHj17DKBytqMqXDjMKrJfXHJ_Of7cwc_VJr3nhsZC7h-ytMNGlx0fJQKodeoEfd08sNjd2MuZF0GpBoIm8KON46zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
ردًا على استمرار الاستفزازات والانتهاكات التي يرتكبها العدو اللئيم ضد بلدنا، نفذ الجيش الإيراني، في المرحلة الثالثة والعشرين من عملية "صاعقة"، قبل ساعات، هجمات مكثفة بالمسيرات الانتحارية على مواقع انتشار مستودعات الذخيرة والمعدات اللوجستية للجيش الأمريكي "الذي يقتل الأطفال" في قاعدة الدوحة، ومخازن الوقود في قاعدة علي السالم، ومستودع الذخيرة في معسكر عريفجان في الكويت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/85001" target="_blank">📅 08:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85000">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-pwauMQ-BC-rTAL-lQuS45FvGkJ1JoPjq5zEsLXIta9IssfbY7LG6UrVDmHLTqRUC_QWyCinVVLmkMkPIhva8pWTdAtYf7E6WTyR6lglDxIjfNVboT1wjyAb4jPbrPqHnrHV-7_S7uNs_Z3cuGu5faZoHc3PmkUO0gT5QezomwSzb5TwTXvnzdYeLP0XHHOoF8uziprdC4aVBIKDn01_MVs-Vmqr7vWbMNwKjhvQCc8D4F2T0RlZoYU7khao3e28ZGkVGEcT_h4ic4_uxCpZTI9Ei97seq7Vai7Zou2l77yjO7DT9zH2BjwOBWuwHHYG2y6JEX7XjxzUcgbEB03hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
استمرار ارتفاع أسعار النفط إثر تزايد حدة الصراع في الشرق الأوسط حيث وصل سعر برميل النفط الواحد إلى مايقارب 97 دولار</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/85000" target="_blank">📅 07:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84999">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
تقرير عن صحيفة أمريكية:
في هجماتها على القواعد الأمريكية في الشرق الأوسط، استهدفت إيران أماكن الطائرات المسيّرة، وأنظمة الرادار، ومساكن الجنود، وغيرها من المنشآت، وفقًا لتحليل مرئي للمواقع التي تعرضت للقصف. وتشير هذه الهجمات، التي وقعت خلال الأسبوعين الماضيين واستهدفت تسعة مواقع أمريكية في أنحاء الشرق الأوسط، إلى أن إيران لا تزال قادرة على إلحاق أضرار بأهداف محددة بدقة. ويأتي هذا على الرغم من ادعاءات البيت الأبيض المتكررة بأن القدرات العسكرية الإيرانية قد تضررت بشكل كبير أو دُمرت.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84999" target="_blank">📅 07:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84998">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b60f00f7.mp4?token=a6x1Du2gwu-yS22Upfh3gPhNj5EjTbBoVD6GlLwievDtpvyxjBhtmvyaNfUfm5euWWDT9jpx9MAx-TJpsY9lwDwm8lSs9YIcmNFrikLcGyBsPmgodEJJURiwCgnsCw0L2ATk-Rr4a3keC21NhdmOnz7fWvmnyS93FdP_d_NiefpYSSNHEHBwn2mkYNYOou38Z2di2wveNmMCv0m0BYCw9QxWdlOn4ykQge2QC4kAJ31ymOn1AypuTMISRy01UvzYPDkebiz4DGtNbtNUIfpZbr-fQM4hIE9YnqXfoFnN4CzcvWURG__qwXPSW4Sp31KLemCJDZ07nuSixbFvWUbMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b60f00f7.mp4?token=a6x1Du2gwu-yS22Upfh3gPhNj5EjTbBoVD6GlLwievDtpvyxjBhtmvyaNfUfm5euWWDT9jpx9MAx-TJpsY9lwDwm8lSs9YIcmNFrikLcGyBsPmgodEJJURiwCgnsCw0L2ATk-Rr4a3keC21NhdmOnz7fWvmnyS93FdP_d_NiefpYSSNHEHBwn2mkYNYOou38Z2di2wveNmMCv0m0BYCw9QxWdlOn4ykQge2QC4kAJ31ymOn1AypuTMISRy01UvzYPDkebiz4DGtNbtNUIfpZbr-fQM4hIE9YnqXfoFnN4CzcvWURG__qwXPSW4Sp31KLemCJDZ07nuSixbFvWUbMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الجيش الامريكي:
في تمام الساعة 10:30 مساءً بتوقيت شرق الولايات المتحدة يوم 22 يوليو، أكملت قوات القيادة المركزية الأمريكية (سنتكوم) جولة جديدة من الضربات على إيران لليلة الثانية عشرة على التوالي.
استهدفت القوات الأمريكية مواقع عسكرية إيرانية، شملت قدرات بحرية، ومواقع تخزين صواريخ وطائرات مسيرة، ومواقع مراقبة ساحلية، وأنظمة دفاع جوي. وتُضعف هذه الضربات قدرة إيران على مهاجمة البحارة المدنيين والسفن التجارية.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/84998" target="_blank">📅 06:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84997">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86300c639c.mp4?token=nPMGFaB9MK45oZ5SoAvQem5Fn6iIJtuibiGT1oPiSbRIilnhbMn1QMIq0GsULFDEZzzllMeDoLSiLaUbl18bixAvCoXVF8QRxuXlzBK0ur5GKVZLBHND5rgiA08-EJAVch2Gcmsr7sZKk-a5z8uxCB6q-udLPYAwYCtfKvtpt_yOwDE4cdEaLrb7wfdvIJIph4VaZbJ0IF9IMCUxcyjfebqFYhNB6aunn0rdWAgwrzsYHjllYMjmKlB0drfCK-YPPOoPVuCITJvfgTBZELte3RtYPW9ksifi6HjwXww4HG_ahsFFX7ixdLBN1kAY3Xv5sU93J-RLLOM68WqmBzHTkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86300c639c.mp4?token=nPMGFaB9MK45oZ5SoAvQem5Fn6iIJtuibiGT1oPiSbRIilnhbMn1QMIq0GsULFDEZzzllMeDoLSiLaUbl18bixAvCoXVF8QRxuXlzBK0ur5GKVZLBHND5rgiA08-EJAVch2Gcmsr7sZKk-a5z8uxCB6q-udLPYAwYCtfKvtpt_yOwDE4cdEaLrb7wfdvIJIph4VaZbJ0IF9IMCUxcyjfebqFYhNB6aunn0rdWAgwrzsYHjllYMjmKlB0drfCK-YPPOoPVuCITJvfgTBZELte3RtYPW9ksifi6HjwXww4HG_ahsFFX7ixdLBN1kAY3Xv5sU93J-RLLOM68WqmBzHTkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في ميناء جاسك جنوبي إيران</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/84997" target="_blank">📅 05:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84996">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات في ميناء جاسك جنوبي إيران</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84996" target="_blank">📅 05:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84995">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">استهداف سفينة قبالة السعودية</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/84995" target="_blank">📅 05:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84994">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇺🇸
الخارجية الأمريكية مجدداً: ‏
تحذير عالمي: نظراً لتصاعد التوترات في الشرق الأوسط، لا تزال البيئة الأمنية معقدة مع احتمال حدوث تصعيد غير متوقع.
ينبغي على الأمريكيين الموجودين حاليًا في الشرق الأوسط توخي الحذر واليقظة التامة، والاستعداد لإلغاء الرحلات الجوية، وإغلاق المجال الجوي بشكل دوري، واحتمال حدوث اضطرابات في السفر. وقد أرجأت بعض شركات الطيران في المنطقة استئناف رحلاتها المجدولة سابقًا، بينما ألغت شركات أخرى بعض خطوطها.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/84994" target="_blank">📅 05:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84993">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
نائب محافظ خوزستان: شهيدين و11 جريح حتى الان جراء العدوان الأمريكي الغادر على منفذ الشلامجة</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/84993" target="_blank">📅 04:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84992">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBl4gGxs0bBbxbvZfdGjsQvUj0-NZcAmTwDuNEuni1Iqko7KBlgUXhTj_7SVyXjs5rmtR5zN71ltwkdnSvIJR9RfyJmRj4to82kzlaky6HVm1JIh2NKiD_KeZW3DWGSM14frrY-i-z-wRH03dTT7waPLqmCm-GBjWb8Lqxi1mSwFHoyYWmZnAeqg3KPF0S1U4NYMh_Km_kS0EjM07oQUnFN5utW5pbbURP-hOtORHT8edtPe4Cbb-kXdWZT4fNiZPKfPX_eLkE4Vm8mtLjeNw-ZiMgB_kjP7pfIpnpjIRIR2olMHYJiugmGhV0AGcRPitMUR4NR8zbVYub7Fk1eACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏تقوم طائرة الإنذار المبكر والتحكم المحمول جواً من طراز E-3G Sentry AWACS التابعة لسلاح الجو الأمريكي الآن بإصدار إشارة 7700، معلنة حالة طوارئ بعد قضاء ساعات في العمل فوق السعودية.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/84992" target="_blank">📅 04:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84991">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">توثيق يظهر وجود مدنيين في مكان القصف الأمريكي الغادر على منفذ الشلامجة ماأدى إلى إستشهاد عدد منهم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/84991" target="_blank">📅 04:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84990">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b305e0fb5c.mp4?token=VG4cOnPxsQq61nopAMuB1iwpceWe70CNcOkYiKppI5qESYnBP0-9uLhArvOlW4XNHavw01B9OiDHvvdd66y7FChEU7SUYHgLOYe7mvV0NVm8MjJ_5NxsMy24mr4ddp5QSDjO5aZK0XZVFh7R9lWEBVckYHepWlKPbz-k3fjxN0yXEPskIgEuf-1LiuSqF3UcXDWsWVxP2rNLHURkG1QTci4fuS-bUWS3QMoeeIBuzvKeZWHxGQFnRJYi9O3ZpTdDKXsJigzVpG9JO5fP4Xg9a67laXmDTqWmGqJu3FARWIQsRtzxtQcR2uU36-4QFS3pXK7bIjRryZtToCDW_YX91g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b305e0fb5c.mp4?token=VG4cOnPxsQq61nopAMuB1iwpceWe70CNcOkYiKppI5qESYnBP0-9uLhArvOlW4XNHavw01B9OiDHvvdd66y7FChEU7SUYHgLOYe7mvV0NVm8MjJ_5NxsMy24mr4ddp5QSDjO5aZK0XZVFh7R9lWEBVckYHepWlKPbz-k3fjxN0yXEPskIgEuf-1LiuSqF3UcXDWsWVxP2rNLHURkG1QTci4fuS-bUWS3QMoeeIBuzvKeZWHxGQFnRJYi9O3ZpTdDKXsJigzVpG9JO5fP4Xg9a67laXmDTqWmGqJu3FARWIQsRtzxtQcR2uU36-4QFS3pXK7bIjRryZtToCDW_YX91g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
استمرار توافد زوار أبي عبدالله الحسين عليه السلام من الجانب الإيراني إلى العراق عبر منفذ الشلامجة عقب العدوان الأمريكي الغاشم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84990" target="_blank">📅 04:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84989">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49dc03cc40.mp4?token=soYOBBZsP-e56mgepUE5lcxFKcm4O1ESGGIf4lcPML_Y90K_z5Iux7ZBP8b4lBbKZd4fCh6mgSiRXIRNXcPpxyCXvuAsq-soAeMIb9-bk1qy9IrAMMYW5VYChJiw5AOqHDV6YszaYaD0FNYF0B310mMrj7KvGuJUTC_4rvcPrYeC10lYjC7C-6lppsKRQANNXFSEWT8PKEkQhVxpKJfWLW9-ALIeHEM7hnMwz2API15tnq66OUaaP-OTcHUdrU_Xc_sYeQXVMC4xpsNscmd9StvwbAFcWDzrEnJXSAPCsYHXCexXH627ato_-ke7QjNuF4pf69QPC3L3bmbhZZXdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49dc03cc40.mp4?token=soYOBBZsP-e56mgepUE5lcxFKcm4O1ESGGIf4lcPML_Y90K_z5Iux7ZBP8b4lBbKZd4fCh6mgSiRXIRNXcPpxyCXvuAsq-soAeMIb9-bk1qy9IrAMMYW5VYChJiw5AOqHDV6YszaYaD0FNYF0B310mMrj7KvGuJUTC_4rvcPrYeC10lYjC7C-6lppsKRQANNXFSEWT8PKEkQhVxpKJfWLW9-ALIeHEM7hnMwz2API15tnq66OUaaP-OTcHUdrU_Xc_sYeQXVMC4xpsNscmd9StvwbAFcWDzrEnJXSAPCsYHXCexXH627ato_-ke7QjNuF4pf69QPC3L3bmbhZZXdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
على الرغم من العدوان الأمريكي الغاشم.. مصدر إيراني لنايا: حركة مرور زوار الإمام الحسين عليه السلام في منفذ شلامجة الحدودي مستمرة.  "لو قطعوا أرجلنا و اليدين...نأتيكَ زحفاً سيدي يا حسين"</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/84989" target="_blank">📅 04:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84988">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccdaf35a1f.mp4?token=TnVc64yxOgijYKsakOCLwnP1ny2545VZBi76iFeinrEwiHhYBg3sSE6_g7gGKmLIDPO4rucTvR-Ji0sZRMriXhzrjm0nctMtEXKtE_iFjHVX1qZ-Otn3VBLCNSwwpn3NDj5Ng2Kn1-9-BrtKncA0vsRNRB6iRRzwuMHVlAU2nfvK82pNVzdpi92ikcZ7cdhiyTMOm8jB2fhGFyyVQn-6zOIhHHVJ4urcnGSGDuBLh2Nji-rMzA65TaAa6VDMg3xgZIeLVvvADg5SU_rIwo_Qbl3ZpyXe2fCyKOTmwBy3heBPqU-YiSnSt-cH0gNd3AQ0fOZ_VxOifLG68hSoU6aQLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccdaf35a1f.mp4?token=TnVc64yxOgijYKsakOCLwnP1ny2545VZBi76iFeinrEwiHhYBg3sSE6_g7gGKmLIDPO4rucTvR-Ji0sZRMriXhzrjm0nctMtEXKtE_iFjHVX1qZ-Otn3VBLCNSwwpn3NDj5Ng2Kn1-9-BrtKncA0vsRNRB6iRRzwuMHVlAU2nfvK82pNVzdpi92ikcZ7cdhiyTMOm8jB2fhGFyyVQn-6zOIhHHVJ4urcnGSGDuBLh2Nji-rMzA65TaAa6VDMg3xgZIeLVvvADg5SU_rIwo_Qbl3ZpyXe2fCyKOTmwBy3heBPqU-YiSnSt-cH0gNd3AQ0fOZ_VxOifLG68hSoU6aQLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حصرية  لحظة تنفيذ العدوان الأمريكي الغادر على زوار الإمام الحسين عليه السلام في منفذ  الشلامجة الحدودي.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84988" target="_blank">📅 04:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84987">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3d5fe3494.mp4?token=KmvlcduRwj8By3qjIa507r6dmRXSgmzJtpxDZyaLoAi4_MO4O_0OMbnDPzj2Qsd1WTOmwspMLv2XbqBIT-wgsEIhDNgDR8eDUNMJWsoRvY7iPuPeD41efvx9nYVSJ4gbjmTBkfUjF7At38XGuOwGLHeMBdy1jiNiUlLuFiXuFB-qglq0wUnHS8xZEm9mfPHgAaHj0Fc1BkHsnYETA6iltPf7C3zf45klh_kOQYe3jEkEHkucX0KJNoBLlIvHpg5h6ZJCO55c8Ro7HxwFWscbSGxtFE2IoxJy5bA1dOB2Q85yOE2oWM81bwa0lyNHTHknRfAyXBaPHmjYd9Lz67j6OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3d5fe3494.mp4?token=KmvlcduRwj8By3qjIa507r6dmRXSgmzJtpxDZyaLoAi4_MO4O_0OMbnDPzj2Qsd1WTOmwspMLv2XbqBIT-wgsEIhDNgDR8eDUNMJWsoRvY7iPuPeD41efvx9nYVSJ4gbjmTBkfUjF7At38XGuOwGLHeMBdy1jiNiUlLuFiXuFB-qglq0wUnHS8xZEm9mfPHgAaHj0Fc1BkHsnYETA6iltPf7C3zf45klh_kOQYe3jEkEHkucX0KJNoBLlIvHpg5h6ZJCO55c8Ro7HxwFWscbSGxtFE2IoxJy5bA1dOB2Q85yOE2oWM81bwa0lyNHTHknRfAyXBaPHmjYd9Lz67j6OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجلات الإسعاف تجري عملية إنتشال الشهداء والجرحى من مكان العدوان الأمريكي على منفذ الشلامجة الحدودي</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/84987" target="_blank">📅 04:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84986">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e0fb0bb1.mp4?token=DeEQKpNEbjrcgc8XmYp4e-nup9TweLLn_LUKpH_VLTxORMnWQ2_JVAQ0CasIGwpxUQGthzbeW0MJ9BwMZ3GSS89GSpNogBii82xZljPtLoSXq_01X93S7me2vQWubV0vTDehVjhFFNwhI7JF13Bvob8AThzBHXDlGR9RBNW7cxh9k6axbYu93po6yWXAWDdrW0Chakkg8nLduXnNc-f-ZRGI779pZQK9NzZZ9CjdHfABNkzr6ORxAZcPtcldhRz4IMLsGP2_bQfxxyUEHYBmDn0DARHG8IxkXNQwRWaO_UdpeV1VdJXLt4UAdWHi5SZtRPfKE2faASu4uK0z-5e6JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e0fb0bb1.mp4?token=DeEQKpNEbjrcgc8XmYp4e-nup9TweLLn_LUKpH_VLTxORMnWQ2_JVAQ0CasIGwpxUQGthzbeW0MJ9BwMZ3GSS89GSpNogBii82xZljPtLoSXq_01X93S7me2vQWubV0vTDehVjhFFNwhI7JF13Bvob8AThzBHXDlGR9RBNW7cxh9k6axbYu93po6yWXAWDdrW0Chakkg8nLduXnNc-f-ZRGI779pZQK9NzZZ9CjdHfABNkzr6ORxAZcPtcldhRz4IMLsGP2_bQfxxyUEHYBmDn0DARHG8IxkXNQwRWaO_UdpeV1VdJXLt4UAdWHi5SZtRPfKE2faASu4uK0z-5e6JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
على الرغم من العدوان الأمريكي الغاشم.. مصدر إيراني لنايا: حركة مرور زوار الإمام الحسين عليه السلام في منفذ شلامجة الحدودي مستمرة.  "لو قطعوا أرجلنا و اليدين...نأتيكَ زحفاً سيدي يا حسين"</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84986" target="_blank">📅 04:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84985">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">من العدوان الأمريكي الغاشم على منفذ الشلامجة الحدودي بين إيران والعراق</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84985" target="_blank">📅 04:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84984">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">2 شهداء كحصيلة أولية جراء العدوان الأمريكي الغاشم على منفذ الشلامجة</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/84984" target="_blank">📅 04:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a666f918cb.mp4?token=ReZ6mp_0Jqyn1pqQMNPZbMXkf3Z87JanTxPUuu6f1NwS2kNMzN47TqKXfNTsL6clEAovHnuffmKmIWLKkEXefZa7CzO7zdKW-WRDVHyf0RCYXopDpX-C4mCJ7OfqDEO9oQtWJ0itF__ocu7hC-wQX6laIHc4SmeZHbFOG5W5W7aJmekssQSptXtMA8sD0K2hbA1R-F995TaYSgcMK9T0MCOKl-y25ufJuMKSb2BT8Wr46ft9oVhl0lAsI7-NEWcOITKfzACkT460TnkF9GFtKBz3B-GJzPE0g6REyfNymD1ipyWVZ7WfmHDI4eYTWRDkHi9rxW1BbRQhvvibYO_8ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a666f918cb.mp4?token=ReZ6mp_0Jqyn1pqQMNPZbMXkf3Z87JanTxPUuu6f1NwS2kNMzN47TqKXfNTsL6clEAovHnuffmKmIWLKkEXefZa7CzO7zdKW-WRDVHyf0RCYXopDpX-C4mCJ7OfqDEO9oQtWJ0itF__ocu7hC-wQX6laIHc4SmeZHbFOG5W5W7aJmekssQSptXtMA8sD0K2hbA1R-F995TaYSgcMK9T0MCOKl-y25ufJuMKSb2BT8Wr46ft9oVhl0lAsI7-NEWcOITKfzACkT460TnkF9GFtKBz3B-GJzPE0g6REyfNymD1ipyWVZ7WfmHDI4eYTWRDkHi9rxW1BbRQhvvibYO_8ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي الغادر الذي طال منفذ الشلامجة الحدودي أثناء مرور وعبور زوار الإمام الحسين عليه السلام من إيران إلى العراق.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/84983" target="_blank">📅 04:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84982">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/653394b365.mp4?token=WivgHCzhRZDVhKtyY8nFEVXSx6IdQc7dFaXDolvBG3jamt5t_3Q8VatI8v_X0yui-bFrv8bzMHHWzaqU_8_P9b5E-brngKPWNyvOkFDyxwr4G9Njp0ACDRcZ5fGcZ1mQ1RZtfBrLz_4gRgn4AU2jXMpPH1soMCZ00Poo72SMRE81RWKvOBs-DwRPiaRFeYGkSiNCMVX0LCMc4WGSasAS2Z_RB1I5x-Lbwnz4-Osrhwf2YLcDqdSUTzE8JzBWuxntTEdKvijHwoYq4YpLiMmEUlqlKREj34KcpIAYHL6YAcOfS1ZsMTfEDMV-lnZFOQz92ocJRt3c6oAV4e5P8OfyGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/653394b365.mp4?token=WivgHCzhRZDVhKtyY8nFEVXSx6IdQc7dFaXDolvBG3jamt5t_3Q8VatI8v_X0yui-bFrv8bzMHHWzaqU_8_P9b5E-brngKPWNyvOkFDyxwr4G9Njp0ACDRcZ5fGcZ1mQ1RZtfBrLz_4gRgn4AU2jXMpPH1soMCZ00Poo72SMRE81RWKvOBs-DwRPiaRFeYGkSiNCMVX0LCMc4WGSasAS2Z_RB1I5x-Lbwnz4-Osrhwf2YLcDqdSUTzE8JzBWuxntTEdKvijHwoYq4YpLiMmEUlqlKREj34KcpIAYHL6YAcOfS1ZsMTfEDMV-lnZFOQz92ocJRt3c6oAV4e5P8OfyGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أمريكا تستهدف زوار الإمام الحسين.. تصاعد أعمدة الدخان عقب عدوان أمريكي غادر وغاشم على منفذ الشلامجة الحدودي بين إيران والعراق.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84982" target="_blank">📅 04:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مجدداً.. عدوان أمريكي على مدينة بوشهر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84981" target="_blank">📅 04:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84980">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29c1cb506.mp4?token=QbvI05Le15kmE_CXQQhz8KrWs8e_sVyBCqvhOT3KWI8QJ_pvGoVG2XGbW91lzCDEc6whE6ZW1SnTDeajdzxAwfN8FKw_WFuoN1yYqOGXhd83H0cITcEzsZZ_V86B0x92pNESxCSC4CeOFA2Llxygpkr2KJeJykVwpT7OTdt_o7jMLhkZDPnuYl9aDQqB6mr0go3mKhPUBdctkj_7XUHk4Vcfml3lfv2PkQL8g_amI4AN8x3QUrTo5dktRPf8PiK3puJ1jNPWhtTx7cn7enTMKJvGX6L2QJJ3vYcdXitU9gi7Z2OXEHhid_cxz5k7kD_bSWfcdGK2vSAFzXtj6LTX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29c1cb506.mp4?token=QbvI05Le15kmE_CXQQhz8KrWs8e_sVyBCqvhOT3KWI8QJ_pvGoVG2XGbW91lzCDEc6whE6ZW1SnTDeajdzxAwfN8FKw_WFuoN1yYqOGXhd83H0cITcEzsZZ_V86B0x92pNESxCSC4CeOFA2Llxygpkr2KJeJykVwpT7OTdt_o7jMLhkZDPnuYl9aDQqB6mr0go3mKhPUBdctkj_7XUHk4Vcfml3lfv2PkQL8g_amI4AN8x3QUrTo5dktRPf8PiK3puJ1jNPWhtTx7cn7enTMKJvGX6L2QJJ3vYcdXitU9gi7Z2OXEHhid_cxz5k7kD_bSWfcdGK2vSAFzXtj6LTX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي على منفذ الشلامجة الحدود</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/84980" target="_blank">📅 03:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84979">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxgf2b1iucseryZsWTKUaYpcAzPO7vmoWJ7aPknhU_lC1b6-Yraso6AqxCVIVO-x1BAbDQnlZhzoDejoZ11S5pGS_jhzf6frgJQr0lonfU_dYFe8q_vCgAEtoh8f4Ytl-39n5LrBzqgkxjec6mclJ46neLYo-6k_dbidzwevSBJdAnJwZ9JzFLhuFCqcUkMT4D4onBtZ2FpnehrKUv3-b_rFLnOlb_QrflizNJYrx9Ea2v8J4eNIy3hbRvNWaqhPjpMyKeiRUNwKG7opmo682OLkxXg94nTFR8HDRpCJ_v-hXma9S4E6Dh1de36iEIOJn5Ur075n0vRVnRevK-RYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من العدوان الأمريكي على مدينة "اسلام آباد غرب" في كرمانشاه الإيرانية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/84979" target="_blank">📅 03:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84978">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b220c708f.mp4?token=MbKAGuDo6No3g3ZGuifWt3u1aL7H-4PzcmbRz3qmil3LtgzktE6d3jipNpfMmORXsiF4uLc4M-n1e0vwK2bv8mkT9oXezqIvlcLmjhZPwB2Pe_Jn8Vh-56h0bFxuoC5K5-eJfA7FH7Ynbq2RpmWAbEQGEojRe74mNI5wtZMPmwMdknmE_q3gqpB4gQ8uUK8kuDT2MbOJZEsbz0DCD3qhXcqWNwTQRwRzRebRClW_jPNioFPk5BIPaOKH5lSZwX59QiE6XtE7BRkFPa_R_KrP1cOEgIGjckH0IUXhOqPejy4njUQ6Gi4Xn9UYXNKaKHIhe0KBimqDfwP9YOdgCr1h2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b220c708f.mp4?token=MbKAGuDo6No3g3ZGuifWt3u1aL7H-4PzcmbRz3qmil3LtgzktE6d3jipNpfMmORXsiF4uLc4M-n1e0vwK2bv8mkT9oXezqIvlcLmjhZPwB2Pe_Jn8Vh-56h0bFxuoC5K5-eJfA7FH7Ynbq2RpmWAbEQGEojRe74mNI5wtZMPmwMdknmE_q3gqpB4gQ8uUK8kuDT2MbOJZEsbz0DCD3qhXcqWNwTQRwRzRebRClW_jPNioFPk5BIPaOKH5lSZwX59QiE6XtE7BRkFPa_R_KrP1cOEgIGjckH0IUXhOqPejy4njUQ6Gi4Xn9UYXNKaKHIhe0KBimqDfwP9YOdgCr1h2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في محافظة كرمانشاه</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84978" target="_blank">📅 03:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84977">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/criDKsNFabFvHoSXTA0ZNvfvjGZSCUwKxvegFTSbw0bDQ8UaE78XPq1jHSi9GoOeoN99vRZN97f-hoik48MWFIB73xPCk0hdrDr8cnOxqozzeqAqAXymPIQ5wpUU3CaVvRtAVGOwbudmnLaNS0XQxxYAZA_PYIT5GHQsry8imeBPbGH9J_lYAmFH0eNCwUJ1qZD3Ipj4Pk71SDqSl0FrXhmjVdjzpnGzzfrDiDNicxFz5mFp6Q-tfWB8j0V6olEok_iMwtTxMPGEOuuG6lC01Ic0m1mh6zY29V5BbuhLneePfraRAXIk5Bk78aVUHPt-pn-ZpF6gU2gH6nRJo0PrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مسير يحلق في اجواء منفذ الشلامجة أثناء تنفيذ العدوان الأمريكي</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84977" target="_blank">📅 03:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات في محافظة كرمانشاه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84976" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3402cb9cd2.mp4?token=v_ciKfYz8u1TPZ3PCKLOWubD-c_A15h-9HvddZGoUOhRxOIdMNlJBukAeByAdd9AeyNdVk9aw7pR3tMrpaC2N949ADhJH2r78vq2xT9RNU519Z-GJjO-9uxmnpQkL-NXweDeSqrDobia0FZc-e9qW_AhhLdTA5aGbG4JkN3us-8uHOE2zw5Quf7opVeL-wQvScL5iK9N6nJwfsUxCNoZwzcF-lsQZOvmd680-bSQ97xLysNiPENP5cEREYMmFSZ7X2NgT22SCGXs0Pn2Ovrn49NY9r0-N-Noj3pzF8fj5oNlhcke-TIMcqeyzfsfq03P1Et6JEaLEJaDeaDQlXifJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3402cb9cd2.mp4?token=v_ciKfYz8u1TPZ3PCKLOWubD-c_A15h-9HvddZGoUOhRxOIdMNlJBukAeByAdd9AeyNdVk9aw7pR3tMrpaC2N949ADhJH2r78vq2xT9RNU519Z-GJjO-9uxmnpQkL-NXweDeSqrDobia0FZc-e9qW_AhhLdTA5aGbG4JkN3us-8uHOE2zw5Quf7opVeL-wQvScL5iK9N6nJwfsUxCNoZwzcF-lsQZOvmd680-bSQ97xLysNiPENP5cEREYMmFSZ7X2NgT22SCGXs0Pn2Ovrn49NY9r0-N-Noj3pzF8fj5oNlhcke-TIMcqeyzfsfq03P1Et6JEaLEJaDeaDQlXifJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أولى لحظات العدوان الأمريكي على منفذ الشلامجة</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84975" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عدوان أمريكي على مدينة انديمشك</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84974" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34216a257c.mp4?token=LSeKA_pVC9q51xIeMis0D1bRpdfNh4RqaIQoNg4XMIPXxQ7o--UMl-QEuJXDR0SxPbX6zOfZHksplLMj3dR3sKvlzRQxPa19G20vwoxq7VuMaGcgFKz7x3UpoPY7riuXav5plK7krvWXXFDSbkFx8F0QyePYXqQNkJI_86AFSGvVVbjUjrBE6mynrkozxL88JISgxkba4YTP2GEBPZOGWdmssJet9IyCz_vaW7NzjD5n9IrqosdXj4RhsfFIGsZpFeIfBRx7Ih8y4dmCcIhbFA3Ksk9ut9YkuekQlBCU0sZ60oojwNoQsnq6DcG1MszxXjq3ZHu01oP-9mfqw6E0_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34216a257c.mp4?token=LSeKA_pVC9q51xIeMis0D1bRpdfNh4RqaIQoNg4XMIPXxQ7o--UMl-QEuJXDR0SxPbX6zOfZHksplLMj3dR3sKvlzRQxPa19G20vwoxq7VuMaGcgFKz7x3UpoPY7riuXav5plK7krvWXXFDSbkFx8F0QyePYXqQNkJI_86AFSGvVVbjUjrBE6mynrkozxL88JISgxkba4YTP2GEBPZOGWdmssJet9IyCz_vaW7NzjD5n9IrqosdXj4RhsfFIGsZpFeIfBRx7Ih8y4dmCcIhbFA3Ksk9ut9YkuekQlBCU0sZ60oojwNoQsnq6DcG1MszxXjq3ZHu01oP-9mfqw6E0_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أمريكا ترتكب جريمة حرب جديدة بعد إستهداف منفذ الشلامجة المكتظ بالمدنيين.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84973" target="_blank">📅 03:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-84972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e89fd739.mp4?token=QEPeKAnuMkRj9bbV0tHdTKwAih71xMIE5fV0HK0M6XS33xWHv5EL8IQdn-2EsGJ8o3_WY-N5cz-yd5YTG-wZAtqmL_vrY-PRlC2P8Z0e2xFxxcWtbKNrzoPZTk7uv27ONMC559kn0k0If9L9DVqFgxrtpx1oZMw4l5kJuO4iWxxgYBMYqhPRMHXuo9SUyTQwV1pVYbRuwzHihqja0kC_ZTDz7DSpt-iSMF2skxfDsaKvfzUIlHFhRD4vrNfAKJvHJBxj4ZnJhVyIKVv9GFYHFB_qUKND7Tfy8qIderXCYOmX7Coexl01aEfHSFEhWRGYqqJg_vDKg50gkayY5WxmHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e89fd739.mp4?token=QEPeKAnuMkRj9bbV0tHdTKwAih71xMIE5fV0HK0M6XS33xWHv5EL8IQdn-2EsGJ8o3_WY-N5cz-yd5YTG-wZAtqmL_vrY-PRlC2P8Z0e2xFxxcWtbKNrzoPZTk7uv27ONMC559kn0k0If9L9DVqFgxrtpx1oZMw4l5kJuO4iWxxgYBMYqhPRMHXuo9SUyTQwV1pVYbRuwzHihqja0kC_ZTDz7DSpt-iSMF2skxfDsaKvfzUIlHFhRD4vrNfAKJvHJBxj4ZnJhVyIKVv9GFYHFB_qUKND7Tfy8qIderXCYOmX7Coexl01aEfHSFEhWRGYqqJg_vDKg50gkayY5WxmHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">2 شهداء كحصيلة أولية جراء العدوان الأمريكي الغاشم على منفذ الشلامجة</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84972" target="_blank">📅 03:43 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/ILFfzXvlLing9qpJA7wweanoimpDbZivp2PtaP2P0Nry5n_hsRXOEYJ-mbdNiBKSAhn6POjno9GZwE64HlDLhDY2q6MZ2T05G8ZKFitH2Xp9hSZsefFuH7lbAJJixiLgtvT-AGZGGfC0sE-clfpAZbVrGlYfT9wrZ4B-VffFKi8_zoQ2bwXnfmpNUpdxN3L8w6hTUefXGWy058WxVM8z1c_ITnoT5lJwsgzhg1hp8bqXoJ7oxKeIV4zRoenun1OMsLymAGY02Th10yQH2Hd8zT1Ga5WwO2xpQhZdZ4dvoCkT5BDU-bH0GXXcUig3mrvoNZuD51qdOoQGmD4ja-rWaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 17:23:16</div>
<hr>

<div class="tg-post" id="msg-79304">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">طيران مسير يخترق أجواء مستوطنة زرعيت في شمال فلسطين المحتلة.</div>
<div class="tg-footer">👁️ 538 · <a href="https://t.me/naya_foriraq/79304" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79303">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
🇷🇺
إيران:
المتخصصون الروس سيعودون قريباً لاستكمال بناء محطة بوشهر.</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/naya_foriraq/79303" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79302">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏مسؤول أميركي كبير: نتنياهو وافق بنسبة 100% على وقف النار في لبنان</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/naya_foriraq/79302" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79301">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇱🇧
🏴‍☠️
حزب الله ينشر:
لا مناطق آمنة لـ "إسرائيل"... وسَتَرحَل</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/naya_foriraq/79301" target="_blank">📅 17:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79300">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏴‍☠️
جيش العدو: سنهاجم بقدر ما يلزم، تعليمات رئيس الأركان لم تتغير ولا توجد قيود على القوات في الميدان.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/naya_foriraq/79300" target="_blank">📅 16:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏴‍☠️
جيش العدو:
سنهاجم بقدر ما يلزم، تعليمات رئيس الأركان لم تتغير ولا توجد قيود على القوات في الميدان.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/naya_foriraq/79299" target="_blank">📅 16:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e0661b1f.mp4?token=bkRJKIMKFN0g-YKSJT3Bs0ikV7p2krb4uKBU3pJwDp6G44S1WAoEcaQrs1FaQxjlEcPy_jOt6ycWoBiNcIj2fFkViC7vRE92320UVaKi4wFBf01Y97XEytC-rMxA4MB6n90KluzWx6HUmmSCEFcamVCrnAipi1hZxg2sg7CuMTtWqcCvVTE9X2eh2EzKflDGAZexWzhkKyE3PqoukQ7gfM2f6NbdkK7g2W7AcKYpJh0ObX7G7PXqGCUf30rXKkskpXVTfNR7H6sHGLuf4kSqx2beIwFin-FAkU1lQuGI-ESeVJIUfbxl5ns9ecP0GrBeF_sYXPfAvjPLE9JfMKfOUZkv5jOsVRAScghlkyTa5w8opKyQyV6pOrEj2rEXtM5qh0aiU_rU5PVy_sQ9d0jnZBNZq16T80u6nBwuLY5Ok1L9RqdGn1xMyNPcnwseNse3Fht4fWJhqOtRF40M0OVwZxeZMaC2QFtUa6d3qI4s_qAj4-5yMWsoJHDdpMC62g5K0LF-rsBbSDTJKukSWE2m4m9x9b-Op57qYAr5GLvlHOAeB9IciE02AXolr3noi2UBlYN-cJCfmlNwCveAUMstgpXnjug_GGZmR_GpL7FFyxJkUjnEYS_53UgcjmyGkPpu9D9lhYLct_8pljGCV6c9zJyq_aKFOS6yC6EGNJdQfEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e0661b1f.mp4?token=bkRJKIMKFN0g-YKSJT3Bs0ikV7p2krb4uKBU3pJwDp6G44S1WAoEcaQrs1FaQxjlEcPy_jOt6ycWoBiNcIj2fFkViC7vRE92320UVaKi4wFBf01Y97XEytC-rMxA4MB6n90KluzWx6HUmmSCEFcamVCrnAipi1hZxg2sg7CuMTtWqcCvVTE9X2eh2EzKflDGAZexWzhkKyE3PqoukQ7gfM2f6NbdkK7g2W7AcKYpJh0ObX7G7PXqGCUf30rXKkskpXVTfNR7H6sHGLuf4kSqx2beIwFin-FAkU1lQuGI-ESeVJIUfbxl5ns9ecP0GrBeF_sYXPfAvjPLE9JfMKfOUZkv5jOsVRAScghlkyTa5w8opKyQyV6pOrEj2rEXtM5qh0aiU_rU5PVy_sQ9d0jnZBNZq16T80u6nBwuLY5Ok1L9RqdGn1xMyNPcnwseNse3Fht4fWJhqOtRF40M0OVwZxeZMaC2QFtUa6d3qI4s_qAj4-5yMWsoJHDdpMC62g5K0LF-rsBbSDTJKukSWE2m4m9x9b-Op57qYAr5GLvlHOAeB9IciE02AXolr3noi2UBlYN-cJCfmlNwCveAUMstgpXnjug_GGZmR_GpL7FFyxJkUjnEYS_53UgcjmyGkPpu9D9lhYLct_8pljGCV6c9zJyq_aKFOS6yC6EGNJdQfEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انا وايطاليا لا نتوسل ابدا"..
رئيسة الوزراء الايطالية تنشر فيديو غاضب من ترامب بعد تصريحه ان ميلوني توسلت له من اجل ألتقط صورة معها!
جورجيا ميلوني:
يجب أن يتذكر شيئًا واحدًا: إيطاليا وأنا لا نتوسل أبدًا. تصريحات دونالد ترامب ملفقة تمامًا. أشعر بالصدمة بصراحة. لا أعرف لماذا يتصرف رئيس الولايات المتحدة بهذه الطريقة تجاه حلفائه! بعد كل شيء، هذه ليست المرة الأولى التي يحدث فيها ذلك. كل ما يمكنني قوله هو أنني آسفة لأنه لا يبدي نفس الحزم والصلابة تجاه أعداء الغرب، وأعداء الولايات المتحدة، ومع تلك القيادات التي يظهر تجاهها، على النقيض من ذلك، قدراً كبيراً من التساهل والمداهنة.</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/naya_foriraq/79298" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWTl3QTeTdJHM1BTUeZFUihecewD5LMKaArmU9zJT4l4vmeWRr2_V-hCNtXYK2A_pliFQz97eJt3q8XMijwXd-JPwasbgTKq-PZermWa_IPBXyU45mWbD_Wonno_ihs12H3VEOqOxcCjKGk2uTjHUu7KWrUvG8Zl6NPeTQZAS0hpVh6eDjT1PSY4U_lVzvzuuKOOAH4Jc4QwHWISStGBYJzgZlR3ySKzlamYVtS_S2WTApXkKG_JA2cLzpBHzNNyfnmwUpntpeeKSCNGzVsL_T2vF3fYzn5C7r1WmCL0DphA39s-wyhhhYqw3PFCzmds30sRce6hbMlMH1DEL70t6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن مسؤول إسرائيلي: نحن الآن في وقف لإطلاق النار وإذا لم يهاجمنا حزب الله فإنه ليس وقت حرب من جهتنا.</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/naya_foriraq/79297" target="_blank">📅 16:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">العدو الصهيوني يشن غارات على جنوب لبنان في اول خرق لاتفاق وقف اطلاق النار المزعوم</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/naya_foriraq/79296" target="_blank">📅 16:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وقف اطلاق النار المزعوم من قبل المسؤول الامريكي يدخل حيز التنفيذ</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/naya_foriraq/79295" target="_blank">📅 16:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏴‍☠️
وزير خارجية النظام الصهيوني جدعون ساعر يناشد الاعلام الغربي بعد العزلة التي يواجهها الكيان الصهيوني:
تصور الكثير من وسائل الإعلام الغربية إسرائيل كنوع من المشروع الاستعماري، كما لو أننا لسنا السكان الأصليين في هذه الأرض - شعب كان هنا منذ أكثر من 3000 عام وحافظ على وجود مستمر هنا عبر التاريخ.
تصورنا دعاية الجانب الآخر كشكل جديد من أشكال الاستعمار.</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/naya_foriraq/79294" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مسؤول أميركي: اتفاق وقف النار يدخل حيز التنفيذ عند الساعة الـ4 بتوقيت بيروت.</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/naya_foriraq/79293" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏رويترز عن مسؤول أميركي: إسرائيل وحزب الله اتفقا على وقف لإطلاق النار اليوم.</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/naya_foriraq/79292" target="_blank">📅 16:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏
رويترز عن مسؤول أميركي:
إسرائيل وحزب الله اتفقا على وقف لإطلاق النار اليوم.</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/naya_foriraq/79291" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
‏ترامب: لن تحصل إيران على أي أموال ولا حتى 10 سنتات.  والـ300 مليار دولار الي وقعت عليها
😄</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/naya_foriraq/79290" target="_blank">📅 16:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2xCYrfNv-QY2z7es4AMdqqh5tVeXiPUg_GAoG_ZGHnnEuX7jNXqyAOwjOsyouTnbfEgRfD37er7uQtM4qCFC6U9RpmFazrNQa61nuQ96_x37PsAkIIvb1Cdq-2e8f7ZlljcfGiPM6527h1pskZ4hX8O0F4P04bWzamDuVidgljLckmJknllDecdOl5YZkP_LihhxDbnX7iU-mBqrBQOEkwj7zYW1Qf83_8F6ChzxklGKzXH9JIMR4zfb22ZlKMvMy0Zah6qGc81DmDNf9EZQyPzKTy40px52xVoqXiBcD3VAnlGNd2tGmoYFgncBXl0fhfJGs4lwV4hJvbCD6tjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
لن تحصل إيران على أي أموال ولا حتى 10 سنتات.
والـ300 مليار دولار
الي وقعت عليها
😄</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/79289" target="_blank">📅 16:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن مسؤول صهيوني:
إيران تقف وراء الهجوم الليلي لحزب الله الذي قُتل خلاله الليلة أربعة من مقاتلي المدرعات. والهدف هو دفع إسرائيل للهجوم في الضاحية وبذلك تعميق الخلاف مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/79288" target="_blank">📅 15:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpXiSGXaN7kHKQE5pW3z15nTnkqgcyGca7DI6e1rvpZgrkFcMedUNpSXU98cA2_lZUV97jQLyxlTafnlnmvf1ucKD5_K1exOoTrd3R9QS3iF9fuqkAb-5SvDZHo0KfkhrDl_rTHp1_nIsNydd3YD-S41S-pBXqV4yyWcAVS-hqGLk3Xgb3WvZ1ztvo1poiIuZNV6yQoHjM4L4TgGXioaVF74kuXoJ3znNgPEA6Shc8WO7ipYK9tHLHWNHmULs84gy7L6KWgmTs0ikjpYaKy1_CbY1QDsieQKRUjYRx2amMZr2puJ_KKapoo7PY7CQrY9igva_2q1fEfwehKuGwEGiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🏴‍☠️
وزير الخارجية الايراني عباس عراقجي يشارك تغريدة بن غفير:
هذا ليس هذياناً صادراً عن مجنون إبادة عشوائي. إنه منشور رسمي علني لوزير الأمن القومي في الكيان الإسرائيلي.
منظومة القتل الإبادية المتمركزة في تل أبيب، تشكّل تهديداً للإنسانية جمعاء. إنها تهدد كل البشر. وليس لها من هدف سوى الحرب الدائمة.</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/79287" target="_blank">📅 15:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏴‍☠️
اعلام العدو عن
مسؤول رفيع في الكابينت
: لا يجب الانجرار إلى سياسة رد فعل. يجب فرض ثمن باهظ على دولة لبنان لكي تمارس ضغطًا على حزب الله.</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/79286" target="_blank">📅 15:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق هرمز الإيرانية: لن يتم فرض أي رسوم على السفن التي ترغب بعبور المضيق خلال فترة الـ60 يوما، سيتم السماح بمرور السفن التي تتقدم بطلبات العبور وتلتزم بالمتطلبات.</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/79285" target="_blank">📅 15:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق هرمز الإيرانية:
لن يتم فرض أي رسوم على السفن التي ترغب بعبور المضيق خلال فترة الـ60 يوما، سيتم السماح بمرور السفن التي تتقدم بطلبات العبور وتلتزم بالمتطلبات.</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/79284" target="_blank">📅 15:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇱🇧
حزب الله ينشر:
אם כבר נסוגים, אז למה שתהייה ההרוג האחרון؟</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/79283" target="_blank">📅 15:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79282">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
وكالة فارس:
اغلاق مضيق هرمز قرار يمكن طرحه في إطار قرار المجلس الأعلى للأمن القومي كحل رادع لإجبار أمريكا على كبح إسرائيل. وإلا، فإن انتهاك اتفاقية الاستمرار سيستمر وستتحمل الطرف المقابل تكاليفه.</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/79282" target="_blank">📅 15:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79281">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📰
‏
سي إن إن:
الولايات المتحدة أبلغت إيران أن إسرائيل "وافقت على ترك الأمر عند هذا الحد" عقب الضربات في لبنان.</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/naya_foriraq/79281" target="_blank">📅 15:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79280">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اعلام العدو: الحدث قرب مرتفعات علي الطاهر</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/79280" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79279">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
🇱🇧
أبو عبيدة:
نحيّي سواعد مجاهدي حزب الله الذين كبّدوا العدو الصهيوني خسائر فادحة ولا يزالون، في إطار التصدي البطولي للعدوان على لبنان وشعبه وسيادته، وهو حقٌ وواجبٌ كفلته كلّ الشرائع</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/naya_foriraq/79279" target="_blank">📅 15:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79278">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
رسو ناقلتين في ميناء البصرة النفطي حمولتهما تتجاوز مليوني برميل
رسو الناقلة Lucia على الرصيف رقم (1) في ميناء البصرة النفطي لتحميل شحنة تبلغ مليون برميل من النفط الخام كما تم إرساء الناقلة Romania على العوامة الثالثة لتحميل شحنة تبلغ مليوناً و300 ألف برميل من النفط الخام.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79278" target="_blank">📅 15:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79277">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اعلام العدو: حدث امني جديد في جنوب لبنان.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79277" target="_blank">📅 14:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79276">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اعلام العدو:
حدث امني جديد في جنوب لبنان.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79276" target="_blank">📅 14:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79275">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvdEFr_uJbn6EVU0HVP3X9oMKONx8P9WI2ieBMHLQYYKcSjNy3ZHNNqKnnKe_hhPztUiFmzNJ5Q98ojXzrhujAtR8hl8Gxmj-NU-YKgqpQ4BgQ0tHy1UztQB88u__uWW0zF4upFg7R-l-Rzccbmn7GzdMW1OO0oyVAhZIx6exCN4hLh4vg3wLcVZAVyhINe5tDpnY7CoJOlGhbA-1T5fxdZuxZFqpzRvo7Fn_PvScQfA1r4bHMcMXuHcY8gL8DM92v_l-ah9gKlm3NZjE4l-pqJ5Ya5PMcrVaalnOBl-HNwMCtlrCkGz6vxII4C4R8zx-b9gyCe6TMjAjNro76tOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوة عامّة  يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.  التاريخ: يوم الجمعة 2026/6/19 الوقت: الساعة الخامسة مساءً المكان: بغداد الصالحية -…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79275" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79274">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇱🇧
بيان صادر عن غرفة عمليّات المقاومة الإسلاميّة في لبنان - حزب الله:
بِسْمِ اللَّـهِ الرحمن الرَّحِيم
﴿أُذِنَ لِلَّذِينَ يُقَاتَلُونَ بِأَنَّهُمْ ظُلِمُوا وَإِنَّ اللَّهَ عَلَىٰ نَصْرِهِمْ لَقَدِيرٌ﴾‏
صَدَقَ اللهُ العَلِيّ العَظِيم
دحضًا لادّعاءات العدوّ الإسرائيليّ بانتهاك حزب الله لوقف إطلاق النار، تؤكّد المقاومة الإسلاميّة أنّ العدوّ لم يلتزم يومًا بأيّ اتّفاق لوقف إطلاق النار منذ 27-11-2024 مرورًا بـ 16-04-2026 وصولاً إلى مخرجات التفاهم الإيرانيّ الأميريكيّ الأخير الذي أكّد في بنده الأوّل على إنهاء الحرب في جميع الجبهات بما يشمل لبنان.
بل إنّ العدوّ الإسرائيليّ أمعن في خروقاته المتمادية لوقف إطلاق النار مرتكبًا المجازر ومدمّرًا الأبنية السكنيّة والبنى التحتيّة المدنيّة
، واستمر في ممارسة الاعتداءات البرّيّة من خلال محاولات التوغّل والسيطرة على قرى ومناطق لم يتمكّن من الوصول إليها قبل الاتفاق. وبلغ الاستخفاف الإسرائيليّ بوقف إطلاق النار حدًّا صرّح معه رئيس أركان جيش العدوّ، المجرم أيال زامير، قبل أسبوعين بأنّه "لا يوجد وقف إطلاق نار في لبنان"، قبل أن يعاود الناطق باسم جيشه أمس التأكيد على مواصلة نشاط قوّات الاحتلال في جنوب لبنان.
وعلى جري عادته، يلجأ العدوّ، تعويضًا عن عجزه في مواجهة مجاهدي المقاومة، وللتغطية على فشله وخسائره في ميدان القتال، إلى ارتكاب المجازر ضد المدنيّين واستهداف القرى الآمنة، مثلما حصل اليوم في أعقاب تصدّي المجاهدي الباسل لمحاولة تقدّمه باتّجاه تلّة علي الطاهر ليل أمس.
ستبقى المقاومة الإسلاميّة بالمرصاد لأيّ اعتداء، يدافع مجاهدوها بكلّ شجاعة وبروح كربلائيّة حسينيّة عن أرضهم وشعبهم، ويذيقون جيش العدوّ بأسهم، موقعين بين ضبّاطه وجنوده القتلى والجرحى بالعشرات، وفي آليّاته إصابات مدمّرة، وبيننا وبينه الأيّام والليالي والميدان.
﴿وَمَا النَّصْرُ إِلاَّ مِنْ عِندِ اللّهِ الْعَزِيزِ الْحَكِيم﴾‏
الجمعة
19-06-2026
‏
04 محرّم 1448 هـ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79274" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79273">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
سنجعل حزب الله يدفع ثمنا باهظا للغاية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79273" target="_blank">📅 14:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79272">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني:
لن نسمح بإيذاء جنودنا ومواطنينا وأي خرق لوقف إطلاق النار من جانب حزب الله سيقابل برد قوي للغاية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79272" target="_blank">📅 13:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79271">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامب: لولا تدخلي لكانت إسرائيل قد سحقت</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79271" target="_blank">📅 13:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79270">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامب: علاقتي بنتنياهو جيدة ولكن يتعين علينا إبقاؤه متعقلا بعض الشيء</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79270" target="_blank">📅 13:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79269">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامب: علاقتي بنتنياهو جيدة ولكن يتعين علينا إبقاؤه متعقلا بعض الشيء</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79269" target="_blank">📅 13:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79268">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGRebmd8DWOSZquAFfh40wvM3djnJhh4qKJH5R_rSzCXMpMij6rd1caedD8-MT1rjWddLEVfUu9sjnKSrq-Oug00O7QKSzunnQSVrsK7SLzHhJ9jA6qez5r_BR1aKf7kcxeoB0Yr7VSA6hrz6Opn6nF5Ac0XujKVaZOZQvqh0rvHjCK-9Psq3bLOftdsxGCemQ1tqttHt3OycOI5oToFr_bn-yrz3X1dsVIOYZmW7-UNhQ-0Vz0GlvhfpxUa4DuUO6G0WP4BSYd0ual1ffq_1epO32dnk5JppnOcZuDEXCvwVO-zNpFIbmW1Afn4IlK2Y1X-Zb1kve1u8EGyrhxJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو يوجه انتقادات لاذعة للرئيس الامريكي دونالد ترامب متهمةً اياه بـ"خداع الإسرائيليين" و"الإضرار بالمصالح الأمريكية والغربية" و"التسبب في إذلال أمريكا" مؤكدة انه كان بإمكانه أن يكون أعظم رئيس على الإطلاق" لكنه "فشل" بدلاً من ذلك.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79268" target="_blank">📅 13:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79267">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌟
وزارة النقل العراقية:
العراق يتسلم إشعاراً من الاتحاد الدولي للنقل يؤكد تحقيقه تقدماً كبيراً في تطبيق نظام التير
النظام تم تشغيله بشكل كامل وافتتحت 7 مسارات دولية جديدة عبر الأراضي العراقية خلال ثمانية أشهر وشهدت تنفيذ أكثر من (1000) عملية نقل دولي
الإشعار يؤكد أيضاً استمرار اعتماد نظام التير لحركة البضائع العابرة براً عبر الأراضي العراقية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79267" target="_blank">📅 13:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79266">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌟
🇮🇷
رئيس وزراء باكستان:
الرئيس الإيراني سيزور باكستان</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79266" target="_blank">📅 13:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79265">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmGbJymaXjmzhIVvPv9-9Xh51so6n-1pYL0cTBFsfw9R0SYDPaElEjbCkCR8j19OQJmYvLxR-Al4eoZEWr5C7uIf5sSsW1ruTdq3Aa9g14Jtpu7CL5CUgPOTIG2Jsfe_pI8BZgWQIGv4ibBSlGEnPUIKOJnfmkR37yYUnfa3ZXLiPeV6pXS8DTUuI5tUS5JP_Quvtegp1SbPsPjjihm3maVdhUPgKWlhk0rh4PnvIQK21CZuOYD-8Yu62Be3PHfZ-7noV_RZQsEvZl1d4WjGOOrOf9ZDq8dnorFP0Un779vflFFX364wPFzE4SE8pvpSYUJgUj4k3eAF1txLYaFtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الغارة الصهيونية على تولين جنوبي لبنان حيث تسببت بشهيدان وعدة جرحى</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79265" target="_blank">📅 13:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79264">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزير الخارجية الباكستاني:
السبب وراء عدم بدء مفاوضات سويسرا  مرتبط بانشغال مسؤولين إيرانيين بطقوس شهر محرم.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79264" target="_blank">📅 13:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79263">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42fd214d2.mp4?token=jFGOYIP9QnZ6WabQElDQCcNyM_zCzzy3VYins1MW6lcehmWM4LSWBH6CwpiT6A6a-4teH5M8KyNMKZYc1GCy8yEYln3pYwI97BW54n8ETAS88eEUNy-_hM6CbEm7QdF3368B31oM6bNePQ7SdPfIKUiFFq7BR6A_Rg2CVlw4GEACEJCFiie8VGZabHWrb52ikxDWt8on8BMvJl--MFRws5JTcqOMR6oSnF5BmW0J-0aHrEEJlDbj48KmbZBeZGTcOL6jjkjWsEXJVVDbgoeOPJU_A4nnApWOTYKTZAl_Ea3DRKQs9pqUe8GKsQJTWMOcEQdJg2OxMIfVbjyH1jdu_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42fd214d2.mp4?token=jFGOYIP9QnZ6WabQElDQCcNyM_zCzzy3VYins1MW6lcehmWM4LSWBH6CwpiT6A6a-4teH5M8KyNMKZYc1GCy8yEYln3pYwI97BW54n8ETAS88eEUNy-_hM6CbEm7QdF3368B31oM6bNePQ7SdPfIKUiFFq7BR6A_Rg2CVlw4GEACEJCFiie8VGZabHWrb52ikxDWt8on8BMvJl--MFRws5JTcqOMR6oSnF5BmW0J-0aHrEEJlDbj48KmbZBeZGTcOL6jjkjWsEXJVVDbgoeOPJU_A4nnApWOTYKTZAl_Ea3DRKQs9pqUe8GKsQJTWMOcEQdJg2OxMIfVbjyH1jdu_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مشاهد من الدمار جراء الاستهداف الصهيوني في عين بورضاي بقضاء بعلبك شمال شرقي لبنان</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79263" target="_blank">📅 12:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79262">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9MbGxXE1sXtF9UBTxwjsZU6Q4t0_1KVBkF75zBPnldhhWNmRtGa4jq5GMJsTzlcZiCod7PhGfqTA7pHuUB0ey9d-OqXwOUhFZrkqh13puNDAVmwyAX_aTyPqbkdT-ac-vLG5l8n81W9kD6jrfimDHXJch7DOSwAi_FaUwnDRn_Uk8BvW4o-CBol9LLi_GqaQU4xFPXomZohtEwJ812qyHwPO-kYwIhjlxyQECxmhpFG3danCKlpV7JnKwdixQkQKtbM57oVSul4LcW2rfsa7kmAOR5hGbDRUv9uq2ZEQE5lkPalY6CYJ9l1xXwK0DLe58je2TbnMnGLz-k0nhRHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فايننشال تايمز:
تم تأجيل المحادثات بين إيران والولايات المتحدة في سويسرا بعد أن رفضت طهران إرسال وفد، مشيرة إلى الضربات الجوية الإسرائيلية المستمرة في جنوب لبنان.
وقال ثلاثة أشخاص مطلعين على الأمر إن إيران قررت عدم المشاركة في المحادثات النووية المخطط لها بسبب الهجمات الإسرائيلية المستمرة، مما أدى إلى إلغاء الاجتماع.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79262" target="_blank">📅 12:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79261">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0386d17edd.mp4?token=sbs4Xjz-F4j8p01GYHBSnmM5zQDk6ATKuKAZqOmBrO5NhA0SPSGOleXPpYEvDYOxfgjnr6-FzMdNkB1LpvXh_9qdOHgSAmNhnON94xM19_zVAh7-Y6kbWZ72OG6PnVvZjnG9oXYxkiO2V3lGd2khAW5iTHEK5nUlTDOmjsuMjNvAuNpCRnBGi9_p3WL8Kd_S0BczLyxPCM7LtM_n7JxC1y2pE-SQ2DaQI_dlug03PY0hPMlOa2TsLP6m18oTFxkdMHhzxOEbyWKwdNcFrJHF-yyT3Hu9ujIBRpuYWKRdixN0VkxucRn2NH9ol8GpppCNQiN93z0mZWZ5BWkNgSKhQEE1IzPePIbpD0wnK-UyjNMkbNcJ0jNQJITfojvCOTqQNI-FTm-MX7q7cs7yRcq_sGI9eNwDTKXsUx53Qee_pIaXa9QWwWIZzFy2fZk4XUAZ3g0N7oBYYIQjDOWmJomSy1nzLw-FFiU0mwquI8MjWDQ1DRXTJNL3ZrqaxqcNsuAIIrmp8vhIIKIxPvAuIRmaGj1irat-CdOqf8kVd3wTTaQ9ISFtMhpM-yGb0tcVgUAgjb_dT62H90rFiXE6pd4A5jjhYP9_BgrW7CAZ_PlAruAJ4_2v_WCdse1nuD2K4_xEJ95TM44mUiBb-gZtKqk3LvUq2IbCHOfI-AgVGpoI0U0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0386d17edd.mp4?token=sbs4Xjz-F4j8p01GYHBSnmM5zQDk6ATKuKAZqOmBrO5NhA0SPSGOleXPpYEvDYOxfgjnr6-FzMdNkB1LpvXh_9qdOHgSAmNhnON94xM19_zVAh7-Y6kbWZ72OG6PnVvZjnG9oXYxkiO2V3lGd2khAW5iTHEK5nUlTDOmjsuMjNvAuNpCRnBGi9_p3WL8Kd_S0BczLyxPCM7LtM_n7JxC1y2pE-SQ2DaQI_dlug03PY0hPMlOa2TsLP6m18oTFxkdMHhzxOEbyWKwdNcFrJHF-yyT3Hu9ujIBRpuYWKRdixN0VkxucRn2NH9ol8GpppCNQiN93z0mZWZ5BWkNgSKhQEE1IzPePIbpD0wnK-UyjNMkbNcJ0jNQJITfojvCOTqQNI-FTm-MX7q7cs7yRcq_sGI9eNwDTKXsUx53Qee_pIaXa9QWwWIZzFy2fZk4XUAZ3g0N7oBYYIQjDOWmJomSy1nzLw-FFiU0mwquI8MjWDQ1DRXTJNL3ZrqaxqcNsuAIIrmp8vhIIKIxPvAuIRmaGj1irat-CdOqf8kVd3wTTaQ9ISFtMhpM-yGb0tcVgUAgjb_dT62H90rFiXE6pd4A5jjhYP9_BgrW7CAZ_PlAruAJ4_2v_WCdse1nuD2K4_xEJ95TM44mUiBb-gZtKqk3LvUq2IbCHOfI-AgVGpoI0U0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
سلسلة غارات صهيونية تستهدف بلدة حبوش جنوب لبنان</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79261" target="_blank">📅 12:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79260">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">إعلام أمريكي: طلبت إيران ضمانات بأن الأعمال العدائية في لبنان ستنتهي، وفقًا للاتفاق القائم، قبل استئناف المحادثات مع الولايات المتحدة في سويسرا.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79260" target="_blank">📅 12:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79259">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmA2TKg-CafHgTWEQM8qt0FUfnnDnvTo3XrbxgMK-IXSvuIR-8x0cFtBVXgUkeyDNcJK57O97qwBn5OO_yKc4lvpUcnMJXT5I7SUc2Cro_ckF1WeYk4zTyCoe2-ArN7qiDDcizLY7_woZGBTdVsrLZpvG1J_IXqLCaaO_M3M8M4fmGT27_IXJGFteEtvTXp_b4d9F_j2wyQ8VFW7Ol3TKDo1uTjQembUI0_-wj7puxrD1-3OAzdJDbpolvw_GQeufxQ5E6dkOCtobWPwbNMSNaFKQFFQtUR-Y4x5qOUYNe_mEJSuWVdEFN6yepjRmDSr74fDuexR9145nPIg5MU1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش الاحتلال الإسرائيلي يواصل اعتداءاته على المدنيين في الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79259" target="_blank">📅 12:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79258">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4865c13f.mp4?token=n8jYkDA0XHHatWTzqxi9NqRJ4g09hfwgvPGU4hGp2zXRljUQA0BW1EJYswnONn30M7lf3fkZgH-8aEqS1pgqb7b3709vb8xM0V6HiRAQRG-a57KTnMa6F84AUDH_-47WBCRvuPHtpD5f_rbmQ19aDxzmeAHflNVYtb7Qfxh7aaafScSP_q92hX-rgKSVbpAdPBQXCrVu0gQdTv7QxcC7sSnnXRNH4vhu2t_1PZ-GRpuDCmiQGuoCdM0RyWJjrfyi4SKHsNA_ItECnSwfJebAIbWH-_YLy4IZZK3jWdr0F4X48wsgNHCMpXl1uRrhFIBbf4Y234V12II4nDNpZlkmvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4865c13f.mp4?token=n8jYkDA0XHHatWTzqxi9NqRJ4g09hfwgvPGU4hGp2zXRljUQA0BW1EJYswnONn30M7lf3fkZgH-8aEqS1pgqb7b3709vb8xM0V6HiRAQRG-a57KTnMa6F84AUDH_-47WBCRvuPHtpD5f_rbmQ19aDxzmeAHflNVYtb7Qfxh7aaafScSP_q92hX-rgKSVbpAdPBQXCrVu0gQdTv7QxcC7sSnnXRNH4vhu2t_1PZ-GRpuDCmiQGuoCdM0RyWJjrfyi4SKHsNA_ItECnSwfJebAIbWH-_YLy4IZZK3jWdr0F4X48wsgNHCMpXl1uRrhFIBbf4Y234V12II4nDNpZlkmvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇸🇾
وزير الدفاع الإسرائيلي إسرائيل كاتز حول قتال سوريا لحزب الله: نحن نقاتل هناك. لا نحتاج إلى الجولاني. الجولاني، الإرهابي في البدلة، ليس عليه أن يأتي ويساعدنا.  لقد رأينا أساليبه ضد العلويين وما حاول أن يفعله للدروز  نحن نعرف سوريا جيدًا. لن يساعدنا في لبنان.…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79258" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79257">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f858111dd2.mp4?token=s-oMBgGq4nwlkc1vq8Am59H4LLQseHhCet0xjHLy1NI4jRVOfyPmsOjQ2D92duJ3ZLPSaj8h2RPWghrxdiVjauE9ItLRdlno8LyreSMeWAqq7Ss4G8bZ-fqgYmbJGAI0Fe_bE6I2EpkuHRGg9ApHgJ5EkfLm-eTmrWex2D2g53w4h8u711jHV4kSRWeMUzrYu-Sfn7CP6BFBLjaay7RA5oy96jkg5sAKJg7xalKZsHo_yUUOs9fFyFpHd8WBJaICsudsQn6X2eiEDTIjOdk7O0NsKpMvWYAH4X_O_I4OPLVcUv3GfUoGapaCJr1KHh_Z4-n0L5anToovjcsUzWse2rGRf-b-o-YjInLtt4FTjWtZSI_Z3eiITdde__HsV67RDdsXf-IRJfqXM5fzka6Dhzz1AsJlub-x0bfEx6rmlX619EsHHDU7LnE1jT7n1qILKJ6vVlMa0U5bfBQTXRTE5gVEqYk_j7NAmgDVJOGgY52y0GiqWrSlgL2U5h54mlXsq1iLhFS7z7WSdVyjk9EpIuu36ZkbAw2NJI73FaludEnDeQlU3OOYSneWLRJYZAsKza9yRzDrvE-kQdomW8vX7ea18uoKJB1k9bLiynWup2yZUFzs0TpXcO3W_x81GBYVC0mB0mBJIxgp2KPJWVEgHktYw_ATkOWaL7oRRbSp4Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f858111dd2.mp4?token=s-oMBgGq4nwlkc1vq8Am59H4LLQseHhCet0xjHLy1NI4jRVOfyPmsOjQ2D92duJ3ZLPSaj8h2RPWghrxdiVjauE9ItLRdlno8LyreSMeWAqq7Ss4G8bZ-fqgYmbJGAI0Fe_bE6I2EpkuHRGg9ApHgJ5EkfLm-eTmrWex2D2g53w4h8u711jHV4kSRWeMUzrYu-Sfn7CP6BFBLjaay7RA5oy96jkg5sAKJg7xalKZsHo_yUUOs9fFyFpHd8WBJaICsudsQn6X2eiEDTIjOdk7O0NsKpMvWYAH4X_O_I4OPLVcUv3GfUoGapaCJr1KHh_Z4-n0L5anToovjcsUzWse2rGRf-b-o-YjInLtt4FTjWtZSI_Z3eiITdde__HsV67RDdsXf-IRJfqXM5fzka6Dhzz1AsJlub-x0bfEx6rmlX619EsHHDU7LnE1jT7n1qILKJ6vVlMa0U5bfBQTXRTE5gVEqYk_j7NAmgDVJOGgY52y0GiqWrSlgL2U5h54mlXsq1iLhFS7z7WSdVyjk9EpIuu36ZkbAw2NJI73FaludEnDeQlU3OOYSneWLRJYZAsKza9yRzDrvE-kQdomW8vX7ea18uoKJB1k9bLiynWup2yZUFzs0TpXcO3W_x81GBYVC0mB0mBJIxgp2KPJWVEgHktYw_ATkOWaL7oRRbSp4Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇸🇾
وزير الدفاع الإسرائيلي إسرائيل كاتز حول قتال سوريا لحزب الله: نحن نقاتل هناك. لا نحتاج إلى الجولاني. الجولاني، الإرهابي في البدلة، ليس عليه أن يأتي ويساعدنا.
لقد رأينا أساليبه ضد العلويين وما حاول أن يفعله للدروز
نحن نعرف سوريا جيدًا. لن يساعدنا في لبنان. يجب أن يبقى في سوريا، وألا يتدخل معنا، وألا يجعلنا نتدخل معه.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79257" target="_blank">📅 11:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79256">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7094431a4b.mp4?token=Y2uyCB-eeaZeLyemNV_7ZXhaCMypiNswbUTIjoGZv9-Arxdo4LrTNa63jHpZcjebCSaJeTT7Bj_iK3nJbiBvxXKWON-RnfMNk8NIrLGE0UEse8rh_pv3jo2-TI19m9WEPeEHeC2QCeWDYw3b8Tb58oUVG-GfNrqOqZqM6Sfpymb98iDIQUjbbnLK21SH3MBtnXZVQQcOh-K9fZO_u-9lVC-vLxe5oPMtDOk4fyZtZRIFjt_O7-ZLFUyeLBWXW1Fd9nnTM-JVVEyXeO6S66gxilRUD4n5ZBqX-TPeNPW_8JSETsgJqIZzvoYSbSIEWmFU-qux8gcrJSKUERoQ_5ppgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7094431a4b.mp4?token=Y2uyCB-eeaZeLyemNV_7ZXhaCMypiNswbUTIjoGZv9-Arxdo4LrTNa63jHpZcjebCSaJeTT7Bj_iK3nJbiBvxXKWON-RnfMNk8NIrLGE0UEse8rh_pv3jo2-TI19m9WEPeEHeC2QCeWDYw3b8Tb58oUVG-GfNrqOqZqM6Sfpymb98iDIQUjbbnLK21SH3MBtnXZVQQcOh-K9fZO_u-9lVC-vLxe5oPMtDOk4fyZtZRIFjt_O7-ZLFUyeLBWXW1Fd9nnTM-JVVEyXeO6S66gxilRUD4n5ZBqX-TPeNPW_8JSETsgJqIZzvoYSbSIEWmFU-qux8gcrJSKUERoQ_5ppgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جيش الاحتلال الإسرائيلي يواصل اعتداءاته على المدنيين في الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79256" target="_blank">📅 11:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79255">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8z7A3TTA4qQd3kEWhbVhmPG49_Y8WWfStlibibj5C3kjU4CaSbt9xV3wUWYWEGadV_tCqqzi_Fv_FwiEZRQcyK5ZaLm7SfeiCp0NX1Bd6XBWVhPR3cj4w5aRtKuKaQkFpXvDc1pofx4IcpoQJP45tIBQ92KVXoxpimS-EXf7_GNc0SxbLepFK5Hmad7Jk6CoGd0U20Sbw_H4F9iWD389M4kJH3P5AZwb1UWWNHwQyiOYJXu-cIDP3qwzT04BBz3LCieFEr9C4D-z4hZnLNtcQR7QbPVI_cEl0hLFuzgOfW8EtLD0oRB2rHL_t4tDWnA4n-2OG9CnfIqRcLtxgkmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق صواريخ اعتراضية شمال الكيان المحتل جراء رشقة صاروخية من جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79255" target="_blank">📅 11:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79254">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5222d6d7.mp4?token=ZYSCTn8MfNROfBEZOYr-tT9UckIX39cGHma6hkV5P-Wl29Jl1Bv0GG63eZrhw9U_EzZZsJ9hUHiQE98fhw8ERpwAV-pV9K2_2vEKd7z0L_byjswWZfxQpsjPRrOV9G20O2sS8D7apkn5gGAk9AStSx9wMvdMd_PibUz3Q7Cp5V9DCTwuWY7Xsc1FlUmxz6tEb7pX04cJigFpoAq41M2uX3UGWZr481qfQe9c0-mR9BNrDRj-qnz7FTZ0f3ZOxkcZFgElp3Kv4v7BFknnGLLbGtTiNk4x0EncAYavws0KQIjntdQSmug31Nof_kanWNS4Ey0YgGtBnOZVqtFtN77q9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5222d6d7.mp4?token=ZYSCTn8MfNROfBEZOYr-tT9UckIX39cGHma6hkV5P-Wl29Jl1Bv0GG63eZrhw9U_EzZZsJ9hUHiQE98fhw8ERpwAV-pV9K2_2vEKd7z0L_byjswWZfxQpsjPRrOV9G20O2sS8D7apkn5gGAk9AStSx9wMvdMd_PibUz3Q7Cp5V9DCTwuWY7Xsc1FlUmxz6tEb7pX04cJigFpoAq41M2uX3UGWZr481qfQe9c0-mR9BNrDRj-qnz7FTZ0f3ZOxkcZFgElp3Kv4v7BFknnGLLbGtTiNk4x0EncAYavws0KQIjntdQSmug31Nof_kanWNS4Ey0YgGtBnOZVqtFtN77q9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇱🇧
جيش الاحتلال يكرر محاولاته للسيطرة على علي الطاهر.. اشتباكات تسمع بوضوح من مسافة صفر بين جنود الاحتلال ومقاومي حزب الله في منطقة علي الطاهر جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79254" target="_blank">📅 10:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79253">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1zbjSXSFkBGDc1rS9Vkdf5boBvdhQK4MAjIyN6_8lwunlSIU4JhplPlY8cu7BRlAGIicG1E0uQxtVVIS5N7ReUbgeINiY22aM7sNbNosIUpNFFumvsXe6O_o7bb5KEPt2YC-kMDwwdlVJNQgNCdxepw3Zn617j7fn_Cm1hAjIxgQMLiKGpdREG_A3uNyJ7k5y3ijfbP75XmHnAfh_2q244hR8dbb8vp8BhjxHou-nCn-GctD6RXkKzO0XPXo4erjf2TjdrJgC1FHyEyS_JyHXPyuBEhldq-DlCuJszgQO8LMLZNwvokUiVFAUVNGmds6ziwcy3e-3TroCZ12zIBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بن غفير يتحدى ترامب ويطالب بحرق لبنان رداً على فشلهم باحتلال مرتفعات علي الطاهر والمجازر الحاصلة بجنود الاحتلال:
مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية. يجب أن يحترق لبنان كله!
‏مع كامل الاحترام للأمريكيين، يجب على إسرائيل أن توضح للعالم أجمع أن دماء أبنائنا وأمن مواطنينا لن تذهب سدى. يجب أن تحترق لبنان بأكملها. واجبنا الأسمى هو حماية مواطني إسرائيل وجنود جيش الدفاع الإسرائيلي، وهذا الواجب يتقدم على أي اعتبار آخر.
‏قلت لرئيس الوزراء، حتى في اجتماعاتنا: مقابل كل دمعة تذرفها أم إسرائيلية، يجب أن تذرف ألف أم لبنانية دمعة.
‏كفى من هذا التكتيك. في الشرق الأوسط، لا يُحقق النصر بالردود المدروسة والاحتواء، بل يتطلب الأمر حسماً جذرياً. يجب القضاء على الإرهاب.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79253" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79252">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6V3Y80QN9tN5MNNwL_UPve4vqlFXWSYPXdJ6kEm-QMDYvhvFHE88nHey3PoyJUimemaTLBM-EZ735LjvtEYpr8vfrsbj-eu5JXArc6ACruapTeTAYRsoN2KpWGKVR9WfE62esIxK2YJhR10K-1qhphLtVqAHht1zyVaR9tsMlDuJwx3coBWOjc_a8vPlb0jm_rAdZE2TL101FM92h0meEzTNLJ8mpadcCQHw6MuejWSA_8jYB795l4JLyzdDUY-Bm-qSCCKWmIvT80Qr42xY952aFEjlKS62kRbBfgokAm4sZkLM4wiFQFVhj55PbkIpwIcH_KO6BYsy7PzvWTh0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بعد فشلهم باحتلال علي الطاهر ؛ رئيس حزب إسرائيل بيتنا يحرض ضد الضاحية الجنوبية لبيروت:
إذا بقيت الضاحية شامخةً بعد الحادثة المأساوية التي سقط فيها أربعة مقاتلين ودُمّرت عائلات، فهذا يُعدّ فشلاً ذريعاً لرئيس الوزراء ووزير الدفاع. جنود الجيش الإسرائيلي ليسوا أهدافاً سهلة في ميدان الرماية. لكلّ أذى يُصيب جنودنا ثمن باهظ لا ينساه الطرف الآخر.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79252" target="_blank">📅 10:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79251">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏴‍☠️
🇱🇧
جيش الاحتلال يكرر محاولاته للسيطرة على علي الطاهر.. اشتباكات تسمع بوضوح من مسافة صفر بين جنود الاحتلال ومقاومي حزب الله في منطقة علي الطاهر جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79251" target="_blank">📅 10:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79250">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c53888f74.mp4?token=D5D59QkVzBdYLEeogNff0Yap8ns8wHoxSGK6q02nQVd_s-D1Di0sEbY-rIcKNjdfit_Z8XLbfxVVIrrvR8aBaCmOiX1ayr6kkX1KNacCmEjHo8_9iaf1NH1seip3Zo6GiC5QFjo8YPfOQlrydE0YrUqgsePxjTjbt6l00k5gNDWhhHXu474bGXkWl-rEjorrWd6xTxZ53zIOLTGEW7ycMA10kpN6oWgJyQcJYleyhb00NjgcwVPer_mqslcsiwqn4hIKjcwNXaSd5hPHRWu_AVB85CktT4dlfDrzvBjOt2gRqbCsQCwePNblXUPIiAkhLl_9xQ5nM-PCseCogriV2A2vb9rRq3gHEHlixJVenm79GJAY2bVbJIGFH3cT8zYmPS945sK_eAHK2Dff550DWQPjQ6HXQkbtyHGKJPtCjS8kaQnAnoWsSxLLr6w0qy4N5_qVYyNWvH1IChuc0Q6wlIGWWYUdbQOY-w415PDUdGflBMXIT3ovNBzRTkyc8Nx80Q0V0m6L60QRviPhd8uMqcjdBR8bawABwwZI2w-swNefXVGepacX0QD-h_6O9fa3RzMFepFiUEgxrLkEHX5H9flwV0D58CIn4eEiUwM4q46l6NcVX2K_IfunY-r8uZbQlHvvBVjgJYCVndmnn52r8ivyzvEBjPaiSIeRlGjEWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c53888f74.mp4?token=D5D59QkVzBdYLEeogNff0Yap8ns8wHoxSGK6q02nQVd_s-D1Di0sEbY-rIcKNjdfit_Z8XLbfxVVIrrvR8aBaCmOiX1ayr6kkX1KNacCmEjHo8_9iaf1NH1seip3Zo6GiC5QFjo8YPfOQlrydE0YrUqgsePxjTjbt6l00k5gNDWhhHXu474bGXkWl-rEjorrWd6xTxZ53zIOLTGEW7ycMA10kpN6oWgJyQcJYleyhb00NjgcwVPer_mqslcsiwqn4hIKjcwNXaSd5hPHRWu_AVB85CktT4dlfDrzvBjOt2gRqbCsQCwePNblXUPIiAkhLl_9xQ5nM-PCseCogriV2A2vb9rRq3gHEHlixJVenm79GJAY2bVbJIGFH3cT8zYmPS945sK_eAHK2Dff550DWQPjQ6HXQkbtyHGKJPtCjS8kaQnAnoWsSxLLr6w0qy4N5_qVYyNWvH1IChuc0Q6wlIGWWYUdbQOY-w415PDUdGflBMXIT3ovNBzRTkyc8Nx80Q0V0m6L60QRviPhd8uMqcjdBR8bawABwwZI2w-swNefXVGepacX0QD-h_6O9fa3RzMFepFiUEgxrLkEHX5H9flwV0D58CIn4eEiUwM4q46l6NcVX2K_IfunY-r8uZbQlHvvBVjgJYCVndmnn52r8ivyzvEBjPaiSIeRlGjEWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
عدوان صهيوني متواصل منذ ساعات الصباح الأولى يستهدف جنوب لبنان حيث استشهد أكثر من 23 شهيد غالبيتهم من الأطفال والنساء.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79250" target="_blank">📅 10:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79249">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXFqWGNBTp2VJ2tsUFWuAf0LmeZ68P_x5xcqIJkh7yt4IhqnFAxN9GbfX-u4iydwV52QXOjxiV0bKIeAP4RudhQfyjNr8aLbhJbCvErmNPecz-FtOnDB8Iu17Wt6fNg-vnKDVTmP3b9BG6GW1slaJi-44hlnXzuQNv1Sf9n13DuYEAuAdnwDulv0DgAinChf4pbQ2AMa0lD8am80Bs6SNple5XWlm5bKJ66981tCkGWFz6VdkCpU3QwundMqRXLI1ebe17emN6hfsVGxbxoLUTZbcW5Ij3B58eIDdKCEKsN429iJPPYwtCa_gUuhtb0D2FWUfnzmvMnlJpcqUf2i-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
الجنوب اللبناني يفتك بجيش الاحتلال ويكبدهم خسائر فادحة خلال ساعات قليلة  جيش العدو سمح بالنشر: إصابة 17 ضابط و جندي إسرائيليين بعضهم قطع أطرافه و2 من الإصابات بجراح ميؤوس منها (موت سريري) بالإضافة لمقتل 5 جنود بينهم قائد كتيبة جراء إصابتهم بصاروخ مضاد…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79249" target="_blank">📅 10:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79248">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">📰
نقلاً عن وكالة ‏رويترز : الحرس الثوري شكل خلايا سرية بالعراق لمهاجمة دول الخليج الفارسي
‏رويترز: خلايا الحرس الثوري بالعراق شنت ما لا يقل عن 7 هجمات بالمسيّرات ضد دول المنطقة
خلايا الحرس الثوري العراقية نفذت هجمات في أبريل الماضي ضد ضد الكويت والسعودية والإمارات وأنطلقت من مدينتي البصرة والسماوة</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79248" target="_blank">📅 10:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79247">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏴‍☠️
الجنوب اللبناني يفتك بجيش الاحتلال ويكبدهم خسائر فادحة خلال ساعات قليلة
جيش العدو سمح بالنشر: إصابة 17 ضابط و جندي إسرائيليين بعضهم قطع أطرافه و2 من الإصابات بجراح ميؤوس منها (موت سريري) بالإضافة لمقتل 5 جنود بينهم قائد كتيبة جراء إصابتهم بصاروخ مضاد للدروع</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79247" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79246">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a5863fe5.mp4?token=Us4xk8F5jqc_FuYeduJaxKiecQuLLUSf1Qsm0-7sQ7Rj8Y2d1f4VtMsB9W01EGNvVzEy2YE5xJjAss29bZ8_0UzmUHjqJCSkilx3S3Yoo53iz54ZwbPOcH8T-VAmTZqoUjnJZHSTOweeKcrFOdGQThKksJdUiCy4f4QadSJIIS6x_gaMlBoQ1GqsTf7fu0kFy35QrRIKckFdlLHfiWdzLhbahamp7vIYxilAcizA75GE_dGlbZIqVrQp1b5WZkmdkNAkTvv3HvtJGyfZ6jrV3cfFZjF1raGNTMY6NGIRXS1_Flzwbes7ita0nnCoVuoLVuGTSWcJjiwApN5Fb_BmOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a5863fe5.mp4?token=Us4xk8F5jqc_FuYeduJaxKiecQuLLUSf1Qsm0-7sQ7Rj8Y2d1f4VtMsB9W01EGNvVzEy2YE5xJjAss29bZ8_0UzmUHjqJCSkilx3S3Yoo53iz54ZwbPOcH8T-VAmTZqoUjnJZHSTOweeKcrFOdGQThKksJdUiCy4f4QadSJIIS6x_gaMlBoQ1GqsTf7fu0kFy35QrRIKckFdlLHfiWdzLhbahamp7vIYxilAcizA75GE_dGlbZIqVrQp1b5WZkmdkNAkTvv3HvtJGyfZ6jrV3cfFZjF1raGNTMY6NGIRXS1_Flzwbes7ita0nnCoVuoLVuGTSWcJjiwApN5Fb_BmOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
عدوان صهيوني متواصل منذ ساعات الصباح الأولى يستهدف جنوب لبنان حيث استشهد أكثر من 23 شهيد غالبيتهم من الأطفال والنساء.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79246" target="_blank">📅 09:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79244">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YsOK8fe41MBT9EpXh-YAN3BRLvWllm0z29gvEwapeVL2YCg0VrAQTzxKKm62TQAtSxI8Jd6aNLKIveIunIqu72Ego5RfCproHtkhEGArSr4R7D0jxrfG2OU0fE3OR_zmBLCou0jld0LFXKJm2phLMGx7MlWEY2NHM-TzBrA1rEMyTBA7kzbdUEYATocVceTO_pgmXQ2SsvHawdH0Pk4_nDpq7a-QV4GkxhXnssNaaWJVVjBAEN01MnCh-GNuI0gNolgv23Mw-2ulzY1ukEx-WjMQvyYrTqMFULqOTpJqr4cH4oaiq_ZKQsjx_cwGPTctH_5rjvgnH7LgoolfcL0OZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTyT50ZnyX-lfPzEpM7OGm7EcGaj6TCJvdpoCmVRQaFtmnbxySoDuUT2gKGKzEJZjvYP8T_pG6ADAfHmsB8z8DfBcOPB3WGFNelccwyYdftEHbRY37FBaxxh8ie8z2uhE3Rz9XpSttLSjwNAMFtNQ9WklQJZM3Eu7SwM9baIX0zuB6ufqLSsUXh3LYQV6sjZR62c0YbPZIV5yXZa9PCP5YPd0_0OnA72awetLoCh1BSBnwe2rwoy9icyskMdx6BVPSoe8jifGWIvDcdgbTcqdv2DOpmDpr_YUsC0P7NfVU5GqylKba7FQIQcd4w370rTmvA8grMCFN77a3583L4AmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
غارات للطيران الحربي الصهيوني تطال عدة مناطق وبلدات في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79244" target="_blank">📅 06:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79243">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB8647k4JQ8H7HpM46gI9y_FTYpb-SRCIz7DPTGrzxTRlBYhHsTMImrvPbu33XF_Eq2L2G7RiAMeWy99GlaNcLdG6yCquQ0G1DmiB9RVLik2Yv5fG_4kiJ-S3fGohsqS6Dxofh9F2FmMCWGctqaxTPShOgUE5inMKdn-f1MaWdYGU7AoeQ4teAgcSb6SlXaqHkDeEZpi4KmH5Vdq2cdkmo6fzWlTIBE8ThtJvay7hqQmLZS8tsd1d9riPTJiszOjmuLLHScTuJGwZeZd6FZIT9sz_yGtXKr-3itlo2zyrVEIY6RP8daF_zuR3O5ezjdULVlPmzcxvTMjeb6w4GQhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسالة_قائد_الثورة_الإسلاميّة_الموجّهة_إلى_الشعب_الإيراني_بشأن_مذكّرة.pdf</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79243" target="_blank">📅 05:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79242">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🌟
وزارة النفط العراقية:
- الحقول النفطية جاهزة لاستئناف عمليات الاستخراج
- العودة إلى الوضع الطبيعي ستتم بشكل متزايد حتى بلوغ معدلات الإنتاج السابقة
(سومو) تواصلت مع جميع الزبائن لترشيح الناقلات المؤجرة والمملوكة من قبلهم لتحميل الكميات التعاقدية  من النفط الخام العراقي عبر الموانىء الجنوبية
- ستكون عودة الصادرات بشكل تدريجي استناداً إلى انسيابية مرورها عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/79242" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79241">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0819644274.mp4?token=IVkUZMfJUJP6am4UvnZ8fep5ksMwI9A2tGIIPQfu82XN2XgqMVgnphEfpN2u8APFbd_60JGxcJ7AoRyx-pCCBiEKLn40FV0sY0_3sZA1QIOs3PIU1nB3kXBoUJ-R8FLmy50Zh_1aS8-ukTFFGuSCdQc94-ZHoVOVcqmh6j35jZBuHLFmBeJyaTq_EPEyWnoszNJAb6O-vu1rBzPgQY3MxqUMPu6Wh4j_VRJvvcNb6tGuazEaD2oPzNbX5KpiJm8NBASTh0Fl-xYiHS3gDIti2T3jjVB9SaF_mcD_1OCnholyUJcQVu_SDC0uSOIK50Ap32dKJDOvEUKRQ-jYcHgewA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0819644274.mp4?token=IVkUZMfJUJP6am4UvnZ8fep5ksMwI9A2tGIIPQfu82XN2XgqMVgnphEfpN2u8APFbd_60JGxcJ7AoRyx-pCCBiEKLn40FV0sY0_3sZA1QIOs3PIU1nB3kXBoUJ-R8FLmy50Zh_1aS8-ukTFFGuSCdQc94-ZHoVOVcqmh6j35jZBuHLFmBeJyaTq_EPEyWnoszNJAb6O-vu1rBzPgQY3MxqUMPu6Wh4j_VRJvvcNb6tGuazEaD2oPzNbX5KpiJm8NBASTh0Fl-xYiHS3gDIti2T3jjVB9SaF_mcD_1OCnholyUJcQVu_SDC0uSOIK50Ap32dKJDOvEUKRQ-jYcHgewA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب
:كنت أرغب في منح نفسي وسام الشرف من الكونغرس، لكن قيل لي إن ذلك غير ممكن
😫</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/79241" target="_blank">📅 00:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79240">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154f345198.mp4?token=RsD0oHAQmCAnqVCqkvaO1-oawEZ7Cxmx02WOWLgViuiQmcplOSD76G2tYV7n2MVss_xaFOD7q56t_8da1eLnmr92mDrgyxQhNpRoPCFL7UDEnvZgIXEg87xsJ5gfFeobe2k6C7Z_tGF8w05xGc0PlIVRuMSJgDyvbO22MfA73HRjYq2J1qeJKdKv26lDuKZsuPMZ2ivS-xxVN9bh9iorCEaszd_WUoS_CTaK6d-jKOgUhi1q59T3MafGxKHcfLedAz24Xfh3Lqvk79HqTQfE3plSWYtd8plhFY761yGs4dhbKLZUDFBvYESUBEZK5oZKdsKuX9kVk0_shQsl8eeLLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154f345198.mp4?token=RsD0oHAQmCAnqVCqkvaO1-oawEZ7Cxmx02WOWLgViuiQmcplOSD76G2tYV7n2MVss_xaFOD7q56t_8da1eLnmr92mDrgyxQhNpRoPCFL7UDEnvZgIXEg87xsJ5gfFeobe2k6C7Z_tGF8w05xGc0PlIVRuMSJgDyvbO22MfA73HRjYq2J1qeJKdKv26lDuKZsuPMZ2ivS-xxVN9bh9iorCEaszd_WUoS_CTaK6d-jKOgUhi1q59T3MafGxKHcfLedAz24Xfh3Lqvk79HqTQfE3plSWYtd8plhFY761yGs4dhbKLZUDFBvYESUBEZK5oZKdsKuX9kVk0_shQsl8eeLLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
استنفار أمني واسع في نيويورك لاحتواء الموقف وطمأنة السياح القادمين من مختلف دول العالم.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/79240" target="_blank">📅 00:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79239">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGPIa6FJFpaflg5Yg-zo7H-04Zi6fAQG0itVwxnnoC9SuER-fkTK7u4OttP_kLC2Zp1Nkyi0z4w3BQNe2AEaPKHOSxSXlektmWqBehmLJEqQW8eiYAOcRVU-XUZTodvfPGYQQSatiTAUuFBGRUELgGYe9eE5JdEeHdrNGzGS_eG79WkspUP-XhLhDAWWl4OdWSLZFeN_zh04ylSad3bUTfvPG7Kk-tT_G9sJcd0_QPEVdJpYyfpDtLoHMS3znN94VA_y0q0emYZ0Qad2N0PE5O3C2pNJLK4oVhH2WW-VUJHjkphD9d32uZY_QgL_AkhO21f728DecQj1CMm3n7Scow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
مشاهد أخرى لفرّ وهروب المدنيين في الشوارع إثر اشتباكات مسلحة عنيفة أثارت حالة من الهلع والخوف بين السكان والزوار</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79239" target="_blank">📅 00:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79238">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8df92df5.mp4?token=TP3W7UqsmmU3xhS46CqAlUBiU67Oo6AyBQULxdWoUbg4VnNSE9jWu84O6IhQVV3_NHs5WROyfK2ykAjrua2NDjqgIijhIY57IIGJ_ChlPdi6W3BgNzMf20C9PSBJzGWpqDhXoKWq2lisdVzStl1qiTuy8d7eOmSD4v_AYUD8G_TNE4CNmtF53upR5g0Ux4yQsFqWFdnoex_eT6ciLeAwNljeTaXVl7I5PIE0MXbYwCMuT9itluneAX7GZ2-06jVQSDMnN5lEfGu1aoNrfWcU_VgLgQt8UMa1eu-YbU1o4rQun0zDvrIkWMM7A-tALdsmKRSJJ9c9Pt2BQZtrHKEiww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8df92df5.mp4?token=TP3W7UqsmmU3xhS46CqAlUBiU67Oo6AyBQULxdWoUbg4VnNSE9jWu84O6IhQVV3_NHs5WROyfK2ykAjrua2NDjqgIijhIY57IIGJ_ChlPdi6W3BgNzMf20C9PSBJzGWpqDhXoKWq2lisdVzStl1qiTuy8d7eOmSD4v_AYUD8G_TNE4CNmtF53upR5g0Ux4yQsFqWFdnoex_eT6ciLeAwNljeTaXVl7I5PIE0MXbYwCMuT9itluneAX7GZ2-06jVQSDMnN5lEfGu1aoNrfWcU_VgLgQt8UMa1eu-YbU1o4rQun0zDvrIkWMM7A-tALdsmKRSJJ9c9Pt2BQZtrHKEiww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حالة من الذعر بين السياح القادمين إلى الولايات المتحدة لمتابعة مباريات كأس العالم، عقب اندلاع اشتباكات عنيفة أسفرت عن وقوع عدد من الإصابات والوفيات.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79238" target="_blank">📅 00:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79237">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45fd29f.mp4?token=kc6ub-iq27FwuyvuEJNt_DZkwqFgvNUKBPsc6O6NcXN7he7Af6UupaZ6OWEVQI7BRt3_C6k-556sdv1IIR8y0csoP7XGWSVBo0X0TqjL4p8G8iTJlhrPL_keeNNyGklKVxJdk8eVryzXy_Mrd4iIJ3eEMnXoXBOpLJc7Vx7F6MSl3KwRCR-drUBDwWIoJ3_aiSaagJZjiyIRSYxZvvc-5fNOwb79-ocwDbvX6_X64KxTBlK1gMMG2CzDLi_fxETDCVQw8ulI_Fw0ISGieCy3EgIpAEdcjlyf6fz3HZ0jvBTOGgpKyx7zM4ijCZrGCO6NmJyvwpWrMuuUtGxiQOo9pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45fd29f.mp4?token=kc6ub-iq27FwuyvuEJNt_DZkwqFgvNUKBPsc6O6NcXN7he7Af6UupaZ6OWEVQI7BRt3_C6k-556sdv1IIR8y0csoP7XGWSVBo0X0TqjL4p8G8iTJlhrPL_keeNNyGklKVxJdk8eVryzXy_Mrd4iIJ3eEMnXoXBOpLJc7Vx7F6MSl3KwRCR-drUBDwWIoJ3_aiSaagJZjiyIRSYxZvvc-5fNOwb79-ocwDbvX6_X64KxTBlK1gMMG2CzDLi_fxETDCVQw8ulI_Fw0ISGieCy3EgIpAEdcjlyf6fz3HZ0jvBTOGgpKyx7zM4ijCZrGCO6NmJyvwpWrMuuUtGxiQOo9pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إشتباكات مسلحة في منطقة تايمز سكوير بمدينة نيويورك، وسط انتشار أمني واسع في محيط الحادث.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79237" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79236">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌟
إشتباكات مسلحة في منطقة تايمز سكوير بمدينة نيويورك، وسط انتشار أمني واسع في محيط الحادث.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79236" target="_blank">📅 00:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79234">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081d58322.mp4?token=QWM8I55DZ1O3WkYYVuQUMO0pOzZ2AVGRuQiAedzW-p-mO4OKkqtYCt2e1qaIvGij98CcthjXlGDXWuopt9VtLH9bNjYeD3EYZbNvSFS0_obvnQWqHVXGcRbF0_Up4xe69c4QITAUVuclTeCDk4zxq0hVqD7pFhp21PSG2KE2W1DrSk9O0E8eb97-Eo4HU1Bjp_I-Ws-j9AgZELVKV843VMJ5d8rvdxq8ojya9vp6aVFAwQunqsRGJoNll4LCex3TQkIhhFz252G3rOneZnUgS9BLiARj1bllOhlWTzMvO3J_v9jt8ZsEuBisDuxeZ3vCMizEqjMdDhwV7gxmW37pig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081d58322.mp4?token=QWM8I55DZ1O3WkYYVuQUMO0pOzZ2AVGRuQiAedzW-p-mO4OKkqtYCt2e1qaIvGij98CcthjXlGDXWuopt9VtLH9bNjYeD3EYZbNvSFS0_obvnQWqHVXGcRbF0_Up4xe69c4QITAUVuclTeCDk4zxq0hVqD7pFhp21PSG2KE2W1DrSk9O0E8eb97-Eo4HU1Bjp_I-Ws-j9AgZELVKV843VMJ5d8rvdxq8ojya9vp6aVFAwQunqsRGJoNll4LCex3TQkIhhFz252G3rOneZnUgS9BLiARj1bllOhlWTzMvO3J_v9jt8ZsEuBisDuxeZ3vCMizEqjMdDhwV7gxmW37pig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
قصف صاروخي مجهول يستهدف مواقع لعصابات الجولاني في بلدة الهول بمحافظة الحسكة السورية الملاصقة للعراق</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/79234" target="_blank">📅 23:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79233">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇫🇷
إعلام الفرنسي:
تشكيلة منتخب فرنسا أمام العراق {فجر الثلاثاء} ستشهد بحد أقصى تغييرين أو ثلاثة في اللاعبين من أجل حسم التأهل للدور المقبل.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79233" target="_blank">📅 22:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79232">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سوالف الگهوة
لقاء بعد قليل بين العامري والمالكي لحسم منصب وزير الداخلية … وباقي المقاعد …</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79232" target="_blank">📅 22:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79231">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇫🇷
‏
ماكرون
: الكثير من علامات الاستفهام بشأن الاتفاق..  ولا أعتقد أن الحرب انتهت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/79231" target="_blank">📅 22:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79230">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6ZVRUkaUWklN4sxsk00fYRK5hIFW6JuRFq1-bI4xJpAS4MkwvOrRxcpQM1k5PtcVByRLofZwaIiw6sA-JxzVbIXqeZWJViZJh2BqlEwQHFgqQbinyIi77nHUAYt7dUadWv1k6rwz0SRHUnULLdtYDK9wy005KeUrD9jx_NecZKkRGiSGkQq2sLnKR8TOwmEo6wX8kMDFDLfExOHDTs4wvv5Fqi4x7o1nknxBIniAnX0mdNc8uTUulBD2B6wmMxfu34iKSkfNtNqu0vKzd-dG-AHksjBBnHwN42oRSvarsZfZujLoPs0ZuDmWW8w-oXH_-YfZ6j6b3-VF70YIT-A9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
تلتزم الولايات المتحدة بالسلام، ونشجع الجميع في منطقة الشرق الأوسط على الحفاظ على التزامهم بالسماح لمفاوضاتنا بالتطور بشكل جيد. الأسواق سعيدة بما يحدث مع انخفاض أسعار النفط بشكل كبير، وارتفاع الأسهم بشكل كبير. نتوقع وقفًا كاملاً لإطلاق النار على جميع الجبهات، بما في ذلك لبنان وحزب الله وإسرائيل. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/79230" target="_blank">📅 21:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79229">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19519b7ddd.mp4?token=rBKtPsEA6H06110ydGrL4gzWdrsDWTS2QhyiCANCkUd5eA5TuXxAkc07NQD4vjJfIzRrThZDPsMMupom6Rp1kcp9BeTvafSyu8JN6KTLBk_da_4hSLQakAyL3GWff8R03M_kNRMwuHX4O7bBquzHY0bbpzSagLrK9TkZKiJ4gyIn34OB_ygVQC22slfwAb8CO15TVgFf0xnkHCHDKGheg903iv1WyJisp998C6iLBf0ZBaq1Ug9B69iDGrb6pVo8Ujqe0XxjuzIu5XvusvBCi2sxTYqDhLp5Vg2R-iKzocq98yE4x0ZSVOsiRv34fsUY5C-UyHnJqwv0sR5TZSYmC3M9LfFKjwvQlPjElY3oLjDTBR-1EaG3kYIP__OXrNj95MopzR3CzvIaiLsojGBsAP_sqKqKpPGR_jsN_LI6Ut6zGKdpK9kIYePX7-fxBR5GbzMbjWFZLEP2d9kQcvo_shLb7Oc8Ix6ATxVBgFvcksLv9bmS9AMhSG9rrY-NHrls3rANhrX-_xaVf-xOPVBCbdgABtjv457B6cnINClySU95RhrPBHA5ConTlOyUJS9wFUtPBu4V7Nosujn1OW938QGeN7Jj6AVAr7iuJLY21hi4OWCyR8gGVMskFPLIW6_oDvDZPjDklapPN8W_s6Eefs2b1J_tAS4h7CtR97dqb1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19519b7ddd.mp4?token=rBKtPsEA6H06110ydGrL4gzWdrsDWTS2QhyiCANCkUd5eA5TuXxAkc07NQD4vjJfIzRrThZDPsMMupom6Rp1kcp9BeTvafSyu8JN6KTLBk_da_4hSLQakAyL3GWff8R03M_kNRMwuHX4O7bBquzHY0bbpzSagLrK9TkZKiJ4gyIn34OB_ygVQC22slfwAb8CO15TVgFf0xnkHCHDKGheg903iv1WyJisp998C6iLBf0ZBaq1Ug9B69iDGrb6pVo8Ujqe0XxjuzIu5XvusvBCi2sxTYqDhLp5Vg2R-iKzocq98yE4x0ZSVOsiRv34fsUY5C-UyHnJqwv0sR5TZSYmC3M9LfFKjwvQlPjElY3oLjDTBR-1EaG3kYIP__OXrNj95MopzR3CzvIaiLsojGBsAP_sqKqKpPGR_jsN_LI6Ut6zGKdpK9kIYePX7-fxBR5GbzMbjWFZLEP2d9kQcvo_shLb7Oc8Ix6ATxVBgFvcksLv9bmS9AMhSG9rrY-NHrls3rANhrX-_xaVf-xOPVBCbdgABtjv457B6cnINClySU95RhrPBHA5ConTlOyUJS9wFUtPBu4V7Nosujn1OW938QGeN7Jj6AVAr7iuJLY21hi4OWCyR8gGVMskFPLIW6_oDvDZPjDklapPN8W_s6Eefs2b1J_tAS4h7CtR97dqb1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 03-06-2026 ناقلة جند تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/79229" target="_blank">📅 21:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79228">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">رسالة_قائد_الثورة_الإسلاميّة_الموجّهة_إلى_الشعب_الإيراني_بشأن_مذكّرة.pdf</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/naya_foriraq/79228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رسالة قائد الثورة الإسلاميّة الموجّهة إلى الشعب الإيراني بشأن مذكّرة التفاهم بين رئيسي جمهورية إيران الإسلامية وأمريكا
بسم الله الرحمن الرحيم
أيّها الشعب الإيراني الغيور والوفي،
💬
كما علمتم، فقد جرى توقيع مذكّرة تفاهم بين رئيسي إيران وأمريكا. وفي مسار الوصول إلى هذه المرحلة، بذل المسؤولون المعنيون جهوداً حثيثة دافعُها الحرص وحسن النية، وإن كان الرئيس الأمريكي هو من لجأ إلى شتى أنواع أوراق الضغط، انطلاقاً من حالة العجز لإنجاز هذا الأمر.
💬
كان لي رأيٌ آخرُ بطبيعة الحال، غير أنني أصدرتُ الإذن بذلك من منطلق الالتزام الذي قطعه رئيس الجمهورية الموقّر بوصفه رئيساً للمجلس الأعلى للأمن القومي، نيابةً عن نفسه وسائر الأعضاء، بصون حقوق الشعب الإيراني وجبهة المقاومة، وإعلانه الصريح تحمُّل المسؤولية، حسبما صرّح جنابه، بأنهم لن يرضخوا للطرف الأمريكي إذا ما أراد فرض إملاءات توسُّعية أو المطالبة بالمزيد. ومن هذه اللحظة، سنكون نحن - أي أنتم، أيها الشعب الشامخ، وهذا الخادم الصغير - بانتظار تحقق الشروط المذكورة، بيد أنه من البديهي أن المفاوضات المباشرة التي ستنعقد في المستقبل، لن تعني بحالٍ من الأحوال الإذعان لرأي العدوّ. كلّنا أمل في أن تحفّ دعوات مولانا (عجّل الله تعالى فرجه الشريف) شعب إيران الأبيّ بشتى صنوف النصر والفتوحات.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79228" target="_blank">📅 21:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79227">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
المركزية الأمريكية: رفعت القوات الأمريكية اليوم الحصار المفروض على جميع الملاحة البحرية الداخلة إلى الموانئ والمناطق الساحلية الإيرانية والخارجة منه
🇺🇸
الخزانة الأمريكية: ‏عقوبات أميركية على 3 أفراد و5 كيانات مرتبطة بحزب الله من عدة جنسيات "سوريا عمان العراق لبنان" وأحد الشخصيات سليمان فرنجية ومحمود قماطي.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79227" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79226">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
‏الخارجية الإيرانية: تخفيف المواد المخصبة مطروح الآن كخيار لكي نغلق الطريق أمام الخيارات الأخرى نقل المواد النووية المخصبة إلى خارج البلاد خيار غير مقبول لنا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/79226" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79225">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📰
رويترز: البيت الأبيض قدم نص مذكرة التفاهم بين الولايات المتحدة وإيران للكونغرس</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79225" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79224">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مصادر إعلامية: معلومات عن وصول أعضاء من الوفد الاميركي الى مقر المفاوضات في منتجع بورغنشتوك بسويسرا</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79224" target="_blank">📅 19:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79223">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888b5dbc65.mp4?token=hJG4yH3mQV8mU4LSlltVQmGc2CnH9MR_7g80QkWJ6zEwo2uq_DUCFbZej7cC-O-Wm2ZM7ANzy1ISh1v0eWkkT4e6plAiSCh3a3Gyi7BK57sspHQNUBJcDcwyrc_6E-B46LtC81Le7Wa1EhUfIyyizBHBdmOHpDyMiCl2ezZ88PAO_sQ43WAAIz8hTK-gDFYuSBzbp1luQXDRAKyvvEZiJpKZUCXOmSiR-bnf8JC_Ot4Y04CYHuDrfYENdAVyn_VRXqAUSt3LCqedWgBcY4kV3G8CXRmeRxrhqHOxX3ud3GVlOmFXbqKtIlwqpksa8fNWhgLliAiVtXbjUvi9YDs5Kp-e3GI8kHTRl6Zqvt02UZgMzmFLL2_3PGq6IRZDmM2oZ4BjRzlifNYYnuAG6jMcsN5JAbj79bSxuUUmmcZ8ZI0nYNHCoIKCUoYogpc6wrWamgCtby7z3q4zjYmrfMZL_POig7zQjYr0uD3yUElyEAZwHXE4XfIBUtOZKbiJd4UGhO2RxeXQldd2SwnCx0D8trN8-lE8hwTiL87rYhwYRvbEC6K-Zx2KeJWsRSAPpNMn0N094MvIZ5wmSubi7e8g1u8jNenhgiZhZc5xz0Kh4QzcVlLi01-QUo2oDTsN47gW5n__ezGLYzjtW4j2LFV15VLUonkqGhuwe4Cp9garAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888b5dbc65.mp4?token=hJG4yH3mQV8mU4LSlltVQmGc2CnH9MR_7g80QkWJ6zEwo2uq_DUCFbZej7cC-O-Wm2ZM7ANzy1ISh1v0eWkkT4e6plAiSCh3a3Gyi7BK57sspHQNUBJcDcwyrc_6E-B46LtC81Le7Wa1EhUfIyyizBHBdmOHpDyMiCl2ezZ88PAO_sQ43WAAIz8hTK-gDFYuSBzbp1luQXDRAKyvvEZiJpKZUCXOmSiR-bnf8JC_Ot4Y04CYHuDrfYENdAVyn_VRXqAUSt3LCqedWgBcY4kV3G8CXRmeRxrhqHOxX3ud3GVlOmFXbqKtIlwqpksa8fNWhgLliAiVtXbjUvi9YDs5Kp-e3GI8kHTRl6Zqvt02UZgMzmFLL2_3PGq6IRZDmM2oZ4BjRzlifNYYnuAG6jMcsN5JAbj79bSxuUUmmcZ8ZI0nYNHCoIKCUoYogpc6wrWamgCtby7z3q4zjYmrfMZL_POig7zQjYr0uD3yUElyEAZwHXE4XfIBUtOZKbiJd4UGhO2RxeXQldd2SwnCx0D8trN8-lE8hwTiL87rYhwYRvbEC6K-Zx2KeJWsRSAPpNMn0N094MvIZ5wmSubi7e8g1u8jNenhgiZhZc5xz0Kh4QzcVlLi01-QUo2oDTsN47gW5n__ezGLYzjtW4j2LFV15VLUonkqGhuwe4Cp9garAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جي دي ‏فانس:  سمحت اتفاقية أوباما النووية بالتخصيب، أما اتفاقيتنا فلن تسمح بذلك. منحتهم اتفاقية أوباما مليار دولار من المال الأمريكي، بينما لا تمنحهم هذه الاتفاقية أي دولار من المال الأمريكي.  ‏لنفترض جدلاً - لنفترض بعد عامين أنهم فعلوا ما نحتاج إلى رؤيته…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79223" target="_blank">📅 19:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79222">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
محكمة جنايات الكرخ تصدر حكماً بالحبس لمدة سنة بحق مشعان الجبوري بناءً على شكوى تقدم بها محمد الحلبوسي بتهمة التهديد بالقتل</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79222" target="_blank">📅 19:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79221">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
جي دي فانس: نشعر بثقة تامة بأننا نستطيع رفع تلك العقوبات مؤقتاً دون اللجوء إلى الكونغرس وطلب موافقته.  لم تكن العقوبات هي العائق الرئيسي أمام النفط الإيراني. لم نعتبر ذلك تنازلاً كبيراً للإيرانيين.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79221" target="_blank">📅 19:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79220">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b349c3eaa.mp4?token=Szq3QtRwLA8kKTecE6HF0C-whdtM8LKzfiuZloaeKcpDWV7BTcuvf3FrHM4xv0sniVTZ76J9IqGohqnlONt4hZWIbCNaYvvUy_Q2r98GQrMMQaMO5yXQ7SvaXLj0jKTrJF5q8RfqmWeHmSnOC0MhX4s7yUqwK_KYvfeUOBxPwrBKySaPPwS2Wi6ffTWwi_hcdYHKQ-wu6deWLQan-8EjaUczJ5UMVz-zlXavRRfbVRxrY9uMItb_Q-So-sLVAnsftlfMob65-JHHkW70CxQwVVDHg3Blazu_auu9KgE6MMhCOp6QQutCxa7F4w2-KE-231Dl7nZ-uarz7FQIyv44yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b349c3eaa.mp4?token=Szq3QtRwLA8kKTecE6HF0C-whdtM8LKzfiuZloaeKcpDWV7BTcuvf3FrHM4xv0sniVTZ76J9IqGohqnlONt4hZWIbCNaYvvUy_Q2r98GQrMMQaMO5yXQ7SvaXLj0jKTrJF5q8RfqmWeHmSnOC0MhX4s7yUqwK_KYvfeUOBxPwrBKySaPPwS2Wi6ffTWwi_hcdYHKQ-wu6deWLQan-8EjaUczJ5UMVz-zlXavRRfbVRxrY9uMItb_Q-So-sLVAnsftlfMob65-JHHkW70CxQwVVDHg3Blazu_auu9KgE6MMhCOp6QQutCxa7F4w2-KE-231Dl7nZ-uarz7FQIyv44yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
تفعيل الدفاعات الجوية في سماء المطلة شمال الكيان المحتل جراء رشقة صاروخية من جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79220" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79219">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7e219b34.mp4?token=duN-k0pwxWA0zHs5uyj5W2eoa6DjLTZGE7RxPxHMkT_7lH2wXI4OePBplcnt9VFHyZR1RPyjGdfdPoCw0sSZLrtjfsexV9Xkso-OUv4fh_jaeAlLA1i4YWKh_Derg_p7XCNJraP3hg0akOJiOv49IdbHGMdZC558drtW75TEklTl2gc0-e6oSY7VApXXb7GY5J45k_x5s-IgZBgU7DRp0OCKTuNW5pRMYgVLZ9GFPUsEEVxsl1fol2Mq--3RlsJwhMDgvjjjArdD92vUPyHrleGed6ClzEwNrD91tG_0Qn6W-RnNxG1XINfo8h2u4MMbvSjH8VnJY0tVXu9PdChqjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7e219b34.mp4?token=duN-k0pwxWA0zHs5uyj5W2eoa6DjLTZGE7RxPxHMkT_7lH2wXI4OePBplcnt9VFHyZR1RPyjGdfdPoCw0sSZLrtjfsexV9Xkso-OUv4fh_jaeAlLA1i4YWKh_Derg_p7XCNJraP3hg0akOJiOv49IdbHGMdZC558drtW75TEklTl2gc0-e6oSY7VApXXb7GY5J45k_x5s-IgZBgU7DRp0OCKTuNW5pRMYgVLZ9GFPUsEEVxsl1fol2Mq--3RlsJwhMDgvjjjArdD92vUPyHrleGed6ClzEwNrD91tG_0Qn6W-RnNxG1XINfo8h2u4MMbvSjH8VnJY0tVXu9PdChqjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جي دي فانس ملوحاً عن برنامج إيران الصاروخي: لإيران حق في الدفاع عن النفس وحقها في امتلاك صواريخ باليستية، قائلاً: "إسرائيل لا تتخلى عن حقها في الدفاع عن النفس إذا أطلق حزب الله صواريخ أو طائرات مسيرة على إسرائيل. والإيرانيون لا يتخلون عن حقهم في الدفاع عن…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79219" target="_blank">📅 19:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79214">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeDfitnWp9GuEryhlA7d3oTfciHQl6rxjeAdIITNuTn6AEF5aB5LVJ4qBJP6-ueMeEwKc-UHo2LOTagHhUCUexysANqNUQ44ffNSjdOnJ1j_qEB5S4sH4mONLcRAvv8Ad1kTQ1KrVoAyskQcvoV40_iflATfnZN3Wml5p2cDPyvTjTJXNTCi-M7Wwtrv3WNgWXbF305kaTlHs0K_srGfSUMKQZhubQpvkBxNJtMupYll-qVLR5l-Y0h0xgheyXRXbli252Ho-mUxWu-AqJxc4zR9medCy-BZiIRepWc9UQXy6k-KHBzG9bOVciPsYtJelRFS_TwrinFVLN8fIJhAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBL4QfPdS_maKZ8P1mgHfacnRezzoYVKdolI3nMpWnNSLt_ImRdSi3lnwHZ1-uTKrxt5LnLwPWZHV7O0sbDaf0tS9kXfLp4p2CgG-1fYzJZwl-ignAocnV5vKchIlLlEe2Be6KCyRyJV4cwUF7OpQ35qs_blufo1HhK0k7WZadE1SeBngLBZU0PDEGeS2Er3ETREKnETogS2uYdyi4gPm96R0AQlQ0kgPXAvHpTIT6bou9nirBfoj7dGG0Au419_NZ-tyP-IRHqF1X0aqDLUktVzvmEDfmpVR3I_i-puhd5k1-_TTJShMAx8b5RGhF01YOwmcRZrPc2V5A5Oo0jl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGHc84lPTDvFAZ9gagavuuIJJz9pNm6-A7ox_WbdoVXJiPBOHiZ57Bzd2kDLiibiMIVuDUZyMTGH0VzsRmbPU4fmQQZr20gGERCO7lssjUbxnjD494Lsg1cEGOML4jFZfEL3Phoz8tQKHHvqRhk5-3_ShlOFRTGa3V4Fyz-JneOqG5i3nUWxsUoTRtBmlbm5fOoCHhi5I1uGW9GGv4sqv37n1assUNDQbndEc6xpA0JS5RfJuSbMqqE7_C_M4HjL0rqYYJaXoXDVLGo_cECZCarDhW_q8nNl7fdwDNKcDECAdSWXSx7s3kGFn1szQAG2CzvvF1EDPHzR0f28-nVuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3i5MKEcQC28ZtTBlXkBntCk2DP8iGRQBvrDFjR4kDn3JpR3ILLQqH7yCP2-ObGTJ8a8EZGpLH-CKARpzIIZRsPelrnue6Jsjrxz27y3tMuAIEqAkPiF1ytsdBem6G8dQQsRIsIrjLF-ShXk2VAwMRAJDBAdswil140RoaTS-lc1LedBkpZYq1CI1vzfCdfSvcvy5PbAbfMmlle5rLMKhEHnekZpZpjBf4fZesUijptT1s9SBZ_ccxq4rBrtpVqriEYhbDweSX-35GwFdncEdeIFHe7bo07KpmU82BX9ql83gQTCkp6P4rdqZ3vMES4YsEI7padcxPX3igObvZpkEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFrnigkQFDV4V7RePI_qFvzgHkwQ_KpQ3byXuYsswfxPpvL2SStTVlUtGz8jOvE0RLD2qOn_q-Ll2qo4yUZW3Dqvu28mvHarPKP-K0i5sr4J8jCCzfl2j8SJIr72JsHDmX1Ars2LVMVyAyHZVtGdjA-rgEzZ5qfXwIXdSOtffIZgwdsPkAXqwxSIZdnyK55LRYQT8Fvo4yo1Bw3vscoCcd5ojH3-mQva8ERWj2w5g1P27vXohCdks_OcvCWfi4Yauqk0rGQ2Pt1tPNk7ktmlBrHxWv6V1ukiXjWfwMI1P4r8r76oCLbtlE4rfZlXbPqvoabMv7tzwwL5zVifMIIozg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
صيادله العراق يعلنون الاضراب و اغلاق جميع الصيدليات في العراق احتجاجا على قرارات وزاره الصحة العراقية و الظلم و التهميش الذي يتعرض له صيادله العراق و الطلبه الخريجين حسب تعبيرهم</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79214" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79213">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
جي دي ‏فانس: بدأت فترة الستين يوماً اليوم، بتوقيت إيران ؛ ‏بدأ الاتفاق أمس، وسنبدأ اليوم احتساب فترة الستين يومًا  ‏نتوقع كجزء من الاتفاق النهائي ألا تمتلك إيران صواريخ تهدد العالم بأسره ؛ ‏تم تدمير برنامج الأسلحة النووية الإيراني، لقد انتهى أمره</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79213" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79212">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43227bc2ef.mp4?token=DYLyu0G7uwLAOB2KW_nDgKpBgn1P_tSgkbWenDW3PQpdxLWP5wKbL6-agHa3V3KRFWoeNrKjvIzGLKMBR_y_FTSWryrh7n_Jb7znf8OB9WtY61c_5ItBAWHRD877Rs79KJ3rCAdtq-WF2PKAO0dMde8YYW5Ypah4LAOA69VznO8kWDUBTFsbU8wrKYo6bLMoLDd-e6AuAiosjKDFp9pMLDNgBk_3grvqXog8uQ9r-kqmKnO4pukUxfLtvTi4B_jxix4QVHEuHJ96XBSwAWF4fvHntGCIgKOgzeo47Q__B8Kh0yOMsXpqeynKXgvc6BJnJpAPzdID5wIzpj9BFRPT4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43227bc2ef.mp4?token=DYLyu0G7uwLAOB2KW_nDgKpBgn1P_tSgkbWenDW3PQpdxLWP5wKbL6-agHa3V3KRFWoeNrKjvIzGLKMBR_y_FTSWryrh7n_Jb7znf8OB9WtY61c_5ItBAWHRD877Rs79KJ3rCAdtq-WF2PKAO0dMde8YYW5Ypah4LAOA69VznO8kWDUBTFsbU8wrKYo6bLMoLDd-e6AuAiosjKDFp9pMLDNgBk_3grvqXog8uQ9r-kqmKnO4pukUxfLtvTi4B_jxix4QVHEuHJ96XBSwAWF4fvHntGCIgKOgzeo47Q__B8Kh0yOMsXpqeynKXgvc6BJnJpAPzdID5wIzpj9BFRPT4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جي دي فانس: الليلة الماضية، مرت 12.5 مليون برميل من النفط عبر مضيق هرمز.   وهذا رقم مرتفع منذ بداية الصراع.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79212" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79211">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
جي دي فانس: الليلة الماضية، مرت 12.5 مليون برميل من النفط عبر مضيق هرمز.
وهذا رقم مرتفع منذ بداية الصراع.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79211" target="_blank">📅 18:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79210">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇧🇭
الدفاع المدني في البحرين: حريق كبير في منطقة الصالحية ، والجهات المختصة تباشر بالتحقيقات.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79210" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79209">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🦠
الكونغو الديمقراطية: 202 حالة وفاة مؤكدة بفيروس إيبولا</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79209" target="_blank">📅 18:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxmmSAL3XkRHS8uyGyMLnPqu2TroVxFv2CrMdfW8Y0PCJOZ2vUM_oxEJ_fK0DP5G74nrXKAtn2qz3_ZjodUPOyJ0anMOwSho-SlAWV9XNYP_zsXI74RSN7gRKu3dUMTXSTRxeoZT1YgYiB2aUNwNU_mt9A_LIorvcW-5770jyZlAaiz2uYBjTvT68lE2ZkK8XDUL0x4Lx1Pu9IRhnh09lWXYHI24LDCY1oaERPyGbANODIPxtCOhjlaFEgKOBapqgryYHPHMWJEUxaQeP7hrTFYlxdMlpRSPq2E6CzNraJ3XTARRGAPW6cZDx2HxHNlhAncIz8sO6R0VKfV24zTeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
احتراق دبابة صهيونية وعدد من آليات جيش الاحتلال إثر استهدافهم برشقة صاروخية من قبل حزب الله في الجنوب اللبناني وإعلام العدو يتحدث عن إصابات عدة في المكان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79208" target="_blank">📅 18:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇱🇧
بيان صادر عن غرفة عمليّات المقاومة الإسلاميّة حول التصدّي لمحاولات العدوّ الوصول إلى مرتفع علي الطاهر:‏
يحاول جيش العدوّ الإسرائيليّ، منذ 4 أيّام، التقدّم باتّجاه بلدة كفرتبنيت ومنطقة علي الطاهر عبر أكثر من مسار مدعومًا بقصف مدفعيّ عنيف يستهدف المنطقة وإطباق جوّيّ استخباريّ تنفّذه طائرات العدوّ الاستطلاعيّة. وقد تصدّى مجاهدو المقاومة الإسلاميّة لجميع هذه المحاولات عبر استهداف تحرّكات وتحشّدات العدوّ بالصواريخ والمسيّرات والمحلّقات الانقضاضيّة، ممّا كبّد العدوّ خسائر كبيرة بين ضبّاطه وجنوده وفي آليّاته، اضطرّ خلالها إلى التراجع وزجّ الطائرات المروحيّة تحت غطاء دخانيّ ومدفعيّ في الليل لسحب خسائره.
يوم أمس الأربعاء 17-06-2026، الساعة 8:00، وبعد رصد قوّة مشاة من جيش العدوّ الإسرائيليّ تتسلّل للتموضع في الأطراف الشماليّة الشرقيّة لبلدة كفرتبنيت، وبنداء يا أبا عبد الله، استهدفها مجاهدو المقاومة الإسلاميّة بسرب من المسيّرات ومحلّقات أبابيل الانقضاضيّة وأوقعوا أفرادها بين قتيل وجريح، ثمّ استكمل المجاهدون هجومهم بصليات صاروخية وقذائف مدفعية باتّجاه منطقة الهدف.
وعند الساعة 1:50 من فجر اليوم الخميس 18 - 06 – 2026، وأثناء محاولة العدوّ التحشيد مجدّدًا عند منطقة المعبر، استهدف المجاهدون دبّابة ميركافا بالأسلحة المناسبة وحقّقوا إصابة مؤكّدة ما أجبر القوّة المتحشّدة على الانسحاب من المنطقة.
تؤكّد المقاومة الإسلاميّة أنّ قوّات العدوّ لا تزال تتواجد عند الأطراف الجنوبيّة لبلدة كفرتبنيت لجهة أرنون، وأن منطقة كفرتبنيت - علي الطاهر ستبقى عصيّة على توغّل العدوّ، وسيسطّر المجاهدون فيها ملاحم كربلائيّة دفاعًا عن بلدهم وشعبهم.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79207" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇱
🇮🇱
إعلام صهيوني نقلاً عن ‏ترامب: من المحتمل جدًا أن أدعم نتنياهو في الانتخابات المقبلة لدينا علاقة جيدة لكن على نتنياهو أن يكون أكثر عقلانية.. وأنا مستعد للالتقاء معه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79206" target="_blank">📅 17:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79205">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79205" target="_blank">📅 17:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79204">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d83Kcm44MOTskghEBtCfTcxFcALSF8cFiwVAUyMXuq9iW6NwoMQ-cQG0WpIb0p4WuenKQwbqirOvI7a12aN-SBfFvyt1lXaP0a41IZGp6QX8EAYB0TujS4XX7ydCdExt6b9Fa4I8b4soe05gzWWfT3fmvuo8M4_f3DCmWR7_j4HlfnWZWAvhPXLrYAFKFa3jTVSRlY0MScfqK5V6jOfQrhz8KGC0BVwOykbFN2wg57lapA1LwdXiUdnWssT_ja8Yao9XRSG_uv33U1tT1x-AIpXSdrAkRHUDCyoYShJkHmgqNoOLVkS3GZhxt4e7833wtXjJdTsebQC3FwBN2nsmvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب من غمرة أحلامه يغرد: "النفط يتدفق، وإيران لن تمتلك سلاحًا نوويًا أبدًا (سيكون العالم آمنًا!)، وأسواق الأسهم مزدهرة، والوظائف في مستويات قياسية، والأسعار في انخفاض (القدرة على الشراء!). بلدنا قوي وآمن ويحظى بالاحترام أكثر من أي وقت مضى. على الرحب والسعة!"</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79203">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مدير عام وزارة الأمن الصهيونية: الحوثيون والميليشيات العراقية يملكون القدرة على التسلل بريا إلى إسرائيل</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/79203" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79202">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏴‍☠️
مدير عام وزارة الامن الصهيونية: الحوثيين في اليمن والميليشيات في العراق يشكلون تهديدا على اسرائيل ولو انهم بعيدون</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79202" target="_blank">📅 17:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79201">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
مدير عام وزارة الامن الصهيونية:
الحوثيين في اليمن والميليشيات في العراق يشكلون تهديدا على اسرائيل ولو انهم بعيدون</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79201" target="_blank">📅 17:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79200">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wp9eOQct4IX7mrlLA_e2RYKeqgq1jmGLTjheTyJbNoEoLCda6EghGyiC-3KUr-FHzvgACRgzIl9_Y2DXlYUaL83mhszK0m1BOI8EK5XGDGvd3P8Tf0CMx2vAA8uJfOLDrz6hjeF5LqtgtE00thc3G0AZtZcD8jw-Yq_gmdtSb3DFPfBmW9yNqOJjpHfELRFk4qUQb2m84nyNgUDiOt1piU_wzDBfOKHWtzz9ZeDbwY9v78p8SBlRh_GikNBmAFJHsonBwPEHf5XqZ7ob-henlJDq--KH8oderPdD_GdMXz7wOv2-74btumdwcMgRrhKqZFGO12tRU3jrtew7IuNSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوة عامّة
يسر المقاومة الإسلامية (كتائب سيد الشهداء) دعوتكم لحضور الحفل الجماهيري الذي يُقام احتفاءً بانتصار الجمهورية الإسلامية الإيرانية في حربها ضد الاستكبار العالمي.
التاريخ: يوم الجمعة 2026/6/19
الوقت: الساعة الخامسة مساءً
المكان: بغداد الصالحية - أمام السفارة الايرانية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79199">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
🏴‍☠️
اعلام العدو:
يعتقد مسؤولون إسرائيليون أن الرئيس ترامب قد يؤجل شحنات الأسلحة أو يفرض حظراً على توريد الأسلحة إلى إسرائيل في المستقبل إذا لم يسحب نتنياهو قواته من لبنان.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79199" target="_blank">📅 17:21 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

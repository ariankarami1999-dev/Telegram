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
<img src="https://cdn4.telesco.pe/file/pNPAGrXuuVjyTqeCLAUcwR7lTPXv4dOs-R-s6wv9X3PVT78NPKm0rxijlzqplJkEjoQV2L7tpjRAofsK_11n4ZuoUHiGO1hvD-RqaTslV2GqQTk1HusAIxDo09JKLG933xTLWBiF7c2v0JlnmVw4ZjfxEltAcydxY6k1p0VdRk7rFZHlqVwpqLR6guHxrorUnPOQzQ00XKHkZMiIygAlCjJDJAjlCUULV3gBuepZKtyOG1lUZFvEQE9ssvoYKibBO_WilD0F952dsZcVNONssYEsBARiZjZ7oUHY0fdV2nuaNrvC8qdiXvRrFIv8apRAJb44dvltdOtgKpNaYx9Vkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 22:59:24</div>
<hr>

<div class="tg-post" id="msg-88180">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الولايات المتحدة تجري عملية سرية لنقل النفط عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/naya_foriraq/88180" target="_blank">📅 22:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-poll">
<h4>📊 كمواطن عراقي ماذا يهمك اكثر ؟!🇮🇶</h4>
<ul>
<li>✓ نزع السلاح</li>
<li>✓ توفير بانزين وكاز في المحطات</li>
</ul>
</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/naya_foriraq/88178" target="_blank">📅 22:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88177">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvtkYWBDRvKlSnIpdMycuZ_xEaqdODLRrqHkKRzP2Ta8WS_rNjuKeN6c9WlFUBKKXDlkP4w2axhp4X2XbtjxFGLX6YbCeEc90wKOCau38_H14ij7PXuK13rx-Q4BvltqsofE-TytYcep8T5Yg78Ig6ftDOj3bgI8el-3MnGDecvHQVRSuamfb1XmR8V2rOUKQmgsZx6PQHLUdttiETswRPoU3uFyVb4kiSjG97i2BaEEIhdDZak3ongeXo14rEd2iwPmOW_AhcxbvicltYnMv8ZEs902wpAZOEmkLu2iKAFpF7U4RKLrNDPFDL0nGHN80wobLRPpbcw37LjFaEaLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية تقرر منع سجاد سالم من الظهور لمدة 90 يوم</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/naya_foriraq/88177" target="_blank">📅 21:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88176">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
🇺🇸
بسبب هزيمتهم النفسية من ايران
إعلام أمريكي : ‏تقدم وحدة تابعة للجيش الأمريكي في ولاية جورجيا لجنودها تصريحًا لمدة أربعة أيام للعب لعبة GTA 6 كحافز لإعادة التجنيد. وقد اختار عشرون جنديًا هذا الحافز بالفعل .</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/naya_foriraq/88176" target="_blank">📅 21:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88175">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇱
نتن ياهو:
لن نتسامح مع وجود عسكري تركي في سوريا يهدد إسرائيل. لقد أوضحنا الرسالة بشكل جليّ: لا تفعل. يبدو أنهم لم يسمعوا ذلك بوضوح كافٍ، لذلك تأكدنا من أنهم فهموه بشكل أفضل.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/88175" target="_blank">📅 20:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88174">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي في قضاء الشرقاط ضمن محافظة صلاح الدين شمالي البلاد يلقي القبض على شخص قام بوضع مادة سامة في خزان ماء الطبخ في احدى المطاعم الامر الذي تسبب بـ(250) حالة تسمم.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/88174" target="_blank">📅 20:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88173">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇱
🇸🇾
رويترز:
رئيس الموساد الإسرائيلي رومان جوفمان أجرى مكالمة هاتفية مع وزير الخارجية السوري أسعد الشيباني في 14 أغسطس وناقش الوجود التركي في سوريا</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/88173" target="_blank">📅 20:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88172">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية تصدر حزمة عقوبات بحق قناة الفلوجة:  - إيقاف بث برنامج حوار التاسعة لمدة (10) أيام تبدأ من تاريخ صدور قرارنا هذا المخالفته لائحة قواعد البث الإعلامي  - منع الظهور الإعلامي بحق مقدم البرنامج السيد (علي فرحان) لمدة (10) أيام…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88172" target="_blank">📅 19:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88171">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e275d7a197.mp4?token=fT1dn_FaQGe5_qofM5qfokuLv4Jbsdbhz96ZbyI0tfxLzpMcG15zTpLVr7XTNdssAUxHCYIt77bpi9bYYcEv0igQ72mfqkEQbDScReJufcu7bPeXDDl4thFPnc01E1yQD98RvW7o3h7nRbCSZCMK2HkknF2Z6q3a3ZIf3fYxgy0UZ3nOWMJcp-r0sONJG4UNTXSFIHzX2c6m1PghOHK4jPyrVQ-XyKwlRYYEPJb4sUeIjZw9dU30Qv94nTG-Y9w6Ri_-mUz6qNUL98uH5Xn7THQrn9vSPnkQ_cCE8DffPN1-Ojxamt-ydPyZrXPjKr4UQt4oqzxwsmdH2TB2-EUlKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e275d7a197.mp4?token=fT1dn_FaQGe5_qofM5qfokuLv4Jbsdbhz96ZbyI0tfxLzpMcG15zTpLVr7XTNdssAUxHCYIt77bpi9bYYcEv0igQ72mfqkEQbDScReJufcu7bPeXDDl4thFPnc01E1yQD98RvW7o3h7nRbCSZCMK2HkknF2Z6q3a3ZIf3fYxgy0UZ3nOWMJcp-r0sONJG4UNTXSFIHzX2c6m1PghOHK4jPyrVQ-XyKwlRYYEPJb4sUeIjZw9dU30Qv94nTG-Y9w6Ri_-mUz6qNUL98uH5Xn7THQrn9vSPnkQ_cCE8DffPN1-Ojxamt-ydPyZrXPjKr4UQt4oqzxwsmdH2TB2-EUlKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏يزعم ترامب أن الولايات المتحدة "تمتلك" مضيق هرمز</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88171" target="_blank">📅 19:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88170">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeefd4da47.mp4?token=i2gNnC27cROSbBkOIJO4Ouz2vF4TNgFtyAM8UZdqJvq2km2QOpp2OcxGlAAHsRHmImUKyUeWjq_KTxaiofQAUPxpUM_MJA9ndwf2KAIUs-LkPmUQJSeJX9r8JJJrQwro-m-Z4pke66WCyERjGKLHI9o1U4ff6Us5z2Zyi7QvxNw53aFBx0TW8ELgDhoEFrqtB_JDqTZGEV_j7raDEzoaZjqyoQpBWcfwkSlGvlPdg8aEwLYHuJwPwF9IwIiAzB7hRzS3jHOw4MofdHDWzucNau6tZsaDymqCaztc6YSW7NGkvZqR-bRHDEhL4fSdxlwOJ5-u0p-LeTs5jcOJZBScvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeefd4da47.mp4?token=i2gNnC27cROSbBkOIJO4Ouz2vF4TNgFtyAM8UZdqJvq2km2QOpp2OcxGlAAHsRHmImUKyUeWjq_KTxaiofQAUPxpUM_MJA9ndwf2KAIUs-LkPmUQJSeJX9r8JJJrQwro-m-Z4pke66WCyERjGKLHI9o1U4ff6Us5z2Zyi7QvxNw53aFBx0TW8ELgDhoEFrqtB_JDqTZGEV_j7raDEzoaZjqyoQpBWcfwkSlGvlPdg8aEwLYHuJwPwF9IwIiAzB7hRzS3jHOw4MofdHDWzucNau6tZsaDymqCaztc6YSW7NGkvZqR-bRHDEhL4fSdxlwOJ5-u0p-LeTs5jcOJZBScvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: هل تتبادلون الرسائل المكتوبة مع كيم جونغ أون؟  ‏ترامب: لا أستطيع أن أخبركم بذلك. لكن علاقتي به ممتازة. لديه 57 سلاحاً نووياً بالغ القوة. سيكون بخير.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/88170" target="_blank">📅 19:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88169">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0db0a5c6.mp4?token=uSbJ6LNccVsGK5umuFFZoZ8Wd0Vl98Xuyl1Sz-RSsoSryIpxl_roe5OFilk3ULkZq2QlT7uXHbz2ZKbhkNv7eZhAReIklcB39cl5noA4vp9T2R5UyX5oslXC5AhVaRpBUnaKiHMcBz-AHhZ1PLYpQpGW4EpnGkpGx3jSTUeQcaw6M6OZbMu9aZ_imT49ChSTuo2ukkrBEOV60MsdFSeN23BJ843ioBMVWNQhX8JSLLy2xdTEYMJy0eggzuwiLlg0sWa45NqbxY2-bvVtbJMm-0uUac1zJ-GuFwiOaer3viC6GGBFanA3bzA4JM3nf8MTy6kFP9njm5Eutnf2Lx-L5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0db0a5c6.mp4?token=uSbJ6LNccVsGK5umuFFZoZ8Wd0Vl98Xuyl1Sz-RSsoSryIpxl_roe5OFilk3ULkZq2QlT7uXHbz2ZKbhkNv7eZhAReIklcB39cl5noA4vp9T2R5UyX5oslXC5AhVaRpBUnaKiHMcBz-AHhZ1PLYpQpGW4EpnGkpGx3jSTUeQcaw6M6OZbMu9aZ_imT49ChSTuo2ukkrBEOV60MsdFSeN23BJ843ioBMVWNQhX8JSLLy2xdTEYMJy0eggzuwiLlg0sWa45NqbxY2-bvVtbJMm-0uUac1zJ-GuFwiOaer3viC6GGBFanA3bzA4JM3nf8MTy6kFP9njm5Eutnf2Lx-L5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: تدفق النفط عبر مضيق هرمز لن يكون مثاليا، والمفاوضات قد تبدأ في وقت ما.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/88169" target="_blank">📅 19:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88168">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
‏ترامب: لقد توصلنا إلى اتفاق مع كندا.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/88168" target="_blank">📅 19:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88167">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
ترامب عن قاعة الاحتفالات الخاصة به: "سيكون لها سقف مقاوم للطائرات المسيّرة. وسيكون فوق السقف العديد من الطائرات المسيّرة، والتي ستحمي واشنطن العاصمة والبيت الأبيض. أمر في غاية الأهمية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/88167" target="_blank">📅 18:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88166">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd7a4575d.mp4?token=bC98S-wZC4ES6lLrlu5-dMFNOgh5SAUM6txRzWJcDhXUzdbbKPGNLRbRuJjtqlP-T9hFCXWf7n0BKDeg_P1dPlm-Qd036Oni79R8eHPmcnTVwxmcaUBr8zyd0uxAvRCwa4f43p_-Bvze3D_wWuuDnsYQIw5f_aQBq5tE4QfcOQ7SOJpEo4pMGnlrGlM3NAjcsHvmAHQzEwlucJSgPilrUPGTTsgCLVMy9pLtKHVWlKNy7A3_lfd68W8RVxn7ZbteeSMOPQ4-qOA-s-kAz1w7vdvmRE8MIy7-1xcUPtc1FEQVX19ktxaE2_jL3h_u0J30hi1Xzodp48UThITjxwiDdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd7a4575d.mp4?token=bC98S-wZC4ES6lLrlu5-dMFNOgh5SAUM6txRzWJcDhXUzdbbKPGNLRbRuJjtqlP-T9hFCXWf7n0BKDeg_P1dPlm-Qd036Oni79R8eHPmcnTVwxmcaUBr8zyd0uxAvRCwa4f43p_-Bvze3D_wWuuDnsYQIw5f_aQBq5tE4QfcOQ7SOJpEo4pMGnlrGlM3NAjcsHvmAHQzEwlucJSgPilrUPGTTsgCLVMy9pLtKHVWlKNy7A3_lfd68W8RVxn7ZbteeSMOPQ4-qOA-s-kAz1w7vdvmRE8MIy7-1xcUPtc1FEQVX19ktxaE2_jL3h_u0J30hi1Xzodp48UThITjxwiDdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب عن قاعة الاحتفالات الخاصة به: "سيكون لها سقف مقاوم للطائرات المسيّرة. وسيكون فوق السقف العديد من الطائرات المسيّرة، والتي ستحمي واشنطن العاصمة والبيت الأبيض. أمر في غاية الأهمية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/88166" target="_blank">📅 18:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88165">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇪🇬
🇮🇷
وزير خارجية مصر:
هناك اتصالات مع إيران تتعلق بجهود خفض التصعيد.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/88165" target="_blank">📅 18:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88164">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
‏
ترامب
: بناء مهبط طائرات الهليكوبتر في البيت الأبيض تبرعت به شركة سيكورسكي.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/88164" target="_blank">📅 18:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88163">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a2e4d48d.mp4?token=GSRdq4wTZGu8hCxLUml8HtdAan8aavdbHWAfFF9bBe_7F-RbMhDKD1krDAKUrNVeCr7vHTKsDjuMmn2vCDCx947vOf9TJHPlHoFgFzms02HIdvGAA2Y474gCpR5mxcHFWDfgIrMtlBRGKNRWIrHAthbZpfSsmdQn-nRsmxjNj5f6OfczjExmmjtQTkPeOpFvpQr1xeuEWKUuDdmgm8QsPfg0ZcPw2iwk7NVbE8Dnw1LgfQCM28LoWkHGpBL69dRPyoRjvabfhWGDyq0dzV7nuP2kNTBVlCR1_m8STBOKIF5uiTvQ_6AM3DwrR52FCqgtIOyv60vBammFlOdCZik_7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a2e4d48d.mp4?token=GSRdq4wTZGu8hCxLUml8HtdAan8aavdbHWAfFF9bBe_7F-RbMhDKD1krDAKUrNVeCr7vHTKsDjuMmn2vCDCx947vOf9TJHPlHoFgFzms02HIdvGAA2Y474gCpR5mxcHFWDfgIrMtlBRGKNRWIrHAthbZpfSsmdQn-nRsmxjNj5f6OfczjExmmjtQTkPeOpFvpQr1xeuEWKUuDdmgm8QsPfg0ZcPw2iwk7NVbE8Dnw1LgfQCM28LoWkHGpBL69dRPyoRjvabfhWGDyq0dzV7nuP2kNTBVlCR1_m8STBOKIF5uiTvQ_6AM3DwrR52FCqgtIOyv60vBammFlOdCZik_7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مجهول يحلق في اجواء البوعيثة ضمن محافظة بغداد.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/88163" target="_blank">📅 18:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88162">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
طيران مجهول يحلق في اجواء البوعيثة ضمن محافظة بغداد.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88162" target="_blank">📅 18:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88161">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
محكمة قوى الأمن الداخلي في البصرة تصدر حكماً بالحبس وطرد منتسب من الخدمة بعد إدانته بالاتفاق على بيع 2 كغم من المخدرات مقابل 35 مليون دينار.
يجب حصر المنتسبين بيد الدولة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88161" target="_blank">📅 17:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88160">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇾🇪
المتحدث باسم القوات المسلحة اليمنية:
القوات المسلحة اليمنية أصبحت اليوم بهذه القوة تفرض المعادلات وتمكنت بعون الله من فرض ثلاث معادلات هي-
المعادلة الأولى هي الحصار بالحصار حيث فرضنا على العدو حصارا محكما لايستطيع أمامه تمرير سفينة واحدة.
المعادلة الثانية هي ضرب التحشيدات السعودية أينما كانت.
المعادلة الثالثة هي حماية سيادة اليمن والتصدي لأي اختراقات للعدو.
وتنفيذا لمعادلة الحصار بالحصار ومنذ إعلان قرار حظر الملاحة البحرية على العدو السعودي في ٢٠ يوليو وحتى يومنا هذا ١٩ أغسطس تمكنت القوات المسلحة اليمنية من استهداف ثماني سفن نفطية سعودية خمس منها في البحر الأحمر وثلاث في خليج عدن والبحر العربي.
كما تم منع ٤٨ سفينة نفطية سعودية من العبور وإجبارها على العودة منها ٣٤ سفينة تم منعها من العبور في البحر العربي والمحيط الهندي و١٤ سفينة تم منعها من العبور  في البحر الأحمر.
وفي إطار الرد على العدوان السعودي على مطار صنعاء وميناء الحديدة وتثبيتا لمعادلة حماية السيادة اليمنية من الاختراقات لأجواء بلدنا وخصوصا في محافظتي صعدة وحجة نفذت القوات المسلحة اليمنية تسع عمليات عسكرية توزعت على ينبع ونجران وجيزان وأبها وإمدادات النفط في المنطقة الشرقية.
وفي إطار تثبيت معادلة استهداف التحشيدات السعودية أينما كانت فقد نفذت القوات المسلحة أربعة عشر عملية عسكرية استهدفت التحشيدات التابعة للعدو السعودي في الرويك والعبر والوديعة ومأرب والمخا وسفن وزوارق نقل معدات وتحشيدات تابعة للعدو السعودي.
كان من نتائج العمليات مايلي:-
- مصرع وإصابة المئات من تحشيدات العدو السعودي بينهم قادة وضباط سعوديون
-  إحراق وتدمير عدد كبير من المخازن والمعدات التابعة لتحشيدات العدو السعودي.
- إغراق  وإحراق سفينتي إنزال عسكرية تنقل الأسلحة والتحشيدات السعودية في المخا.
- إحراق وإغراق أكثر من عشرة زوارق حربية تابعة لتحشيدات العدو السعودي كانت تقوم بأعمال قرصنة وتقطع ونهب في البحر الأحمر بتوجيهات سعودية.
نحذر النظام السعودي من خطورة الإقدام على أي تصعيد فأي تصعيد شامل سيواجه بتصعيد شامل.
ليس أمام النظام السعودي من خيار إلا رفع الحصار وتنفيذ ماتم الاتفاق عليه من رفع الحصار وإنهاء العدوان ودفع المرتبات ورحيل المحتلين وترك ثروات الشعب اليمني للشعب كله.
ننصح المغرر بهم من أبناء بلدنا بالعودة ومغادرة معسكرات العدو  لأنهم يمنيون ولانريد أن نستهدفهم ويكونوا ضحية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88160" target="_blank">📅 16:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88159">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
السيد عباس اليعقوبي:
سيباشر المشاور القانوني بإقامة دعوى قضائية ضد جهاز المخابرات، والقضاء العراقي هو الفيصل بيننا.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88159" target="_blank">📅 16:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88158">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇱
نفتالي بينيت:
سنحقق تطبيع العلاقات مع السعودية، وإندونيسيا، ومع دول أخرى وسنبني تحالفًا للقوى "المعتدلة" في المنطقة ضد القوى "الإسلامية" - ضد إيران، وضد قطر، وتركيا، وجميع القوى "الراديكالية".</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88158" target="_blank">📅 15:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88157">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4y9Va-CCiZ648pCAr22EEohTls4jxDSadlnzT4yRUaIS-uPljG--MqGaBLHuRtREkJs5ZtIK7Y5GgIcpCoQSFEhnLje7wxJ3xLATF4UUY5X86HR6VBnVGHZw2K9yi15iIiMuHFZaM5j4iSlgJAkvKmtFXEHuwEnrtoNIi8bd384n-HUW45B2PCuEl5HgrywjePMY5XaSJcaeGCQgS4mVfkK0nSO44Tnfuf3w7tF-lLZTiLVnJWoVOrSaIKmFUYI9Z6J6BVJE1mWOvlotufUvwu85XAJ7tntbmFvdxypSU3-j4dA9m2ZXXA3oV7TI4-cS0BsP9a65XOFjlTogiW2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
قاليباف
:
أبو مهدي والحاج قاسم العزيزان! ها هي ثمرة جهادكما ودمكما المبارك.
‏في النظام الإقليمي الجديد، أخذ تدخل القوى الأجنبية في المعادلات بين الدول ينحسر بشكل متسارع؛ فأمريكا تبحث عن مخرج مشرّفٍ لها من المنطقة وبات مشروع من النهر إلى البحر للكيان الصهيوني محضَ أضغاث أحلام. ‌
#أخوتنا_قوتنا
⁩</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88157" target="_blank">📅 14:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88156">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCwU92vaDfCzh7SDdPgzbDZ-_oqRDg_zBBu5O2mIQREcKaJSkdjIuXsaVIUCZsSZcZ6mcmrdZENER0fCYn_tuXFLDxLYlc8hn15iIQRFOx4CzqN_0M54OcY5CcLiJJc4Q610j7G1lYgh-0VcpxRwdhsh5b7aE5ZjXmnh-eXUPvp8EHRpWlczrzuWb-U4fmelXRM48iKBgxWJcNM541cT6VPIIY-Y9tHJX2Heq9nsMOpdpswoNSoKCkzfCUB-DZO2fIhmB6jVCHX2lb-nfIkQQ2ECzrJIGhccEfSkLS7-3iXga3xEwaPWnfRMxi7Y1b3abJPWO1rTqivia8FbIbuFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان العراقي يدعو قاليباف إلى أن يكون للعراق خصوصية فيما يتعلق بتصدير النفط عبر مضيق هرمز بما يحفظ مصالحه الاقتصادية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88156" target="_blank">📅 14:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88155">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">▫️
هجوم مسلح يطال مدير بنك سيد صادق في محافظة السليمانية ضمن اقليم كردستان العراق واصابته اصابة بليغة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/88155" target="_blank">📅 14:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88154">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
🇮🇷
التلفزيون الايراني:
بدء نقل النفط العراقي إلى تركيا وأفغانستان عبر السكك الحديدية من كرمانشاه. أول شحنة تزن 50 ألف طن.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88154" target="_blank">📅 13:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88153">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mlfaj8OEc5Kdx9loKX7562toNU7RUue4SuoBemtHsJeKoL5QpGWv6IaLzAvDXIr7mqLFeXf3vPbqVOL4SNSQfwMoYkiK7RerAXvyThUp4s8p0BBazDh5ZuCjBf6wTzSqRORs6nlCC4W82J64-3GbFf4rq9WMyQRRgH4q1nnI1IbjxsAg-jy7S4PhKAgZmJTw_isNRct7BZ2ci2Uc0LxHRgUjZps4TLSoTTkibq06hlT38FSeB1NCDaj0rkhr0DRRAJJ736laXAQ8kKyrsDS8Pi7vNrv0rKH_mpauIvnQcqXi9tPFUuWEGxJnD4a-3ITeOyC12xWODS8luRAjGh02JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
القضاء هو طوق النجاة الأخير للدولة العراقية
استنكار سياسي وجماهيري بعد تسريب خبر محاولة استهداف قاضي قضاة العراق وحصن العراق الأخير .</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88153" target="_blank">📅 12:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88152">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0c38ef88.mp4?token=hJ07fAN99KcSJu_qcUQegaHoPNZ3LlSdmrXc6fU6iolxF2gv_5b2xPcvdMB6LJhLKcvWltG4xkPoQ3do--cZjxEI_oVcnnj_ioWTrJLJKcFt10knD4GZW0HGr7k0T6_EEUMuPeuoF8VqnH9dcQ8zss_Q4h9zgjcI6yafn1m79bPMs5s4y7RKCGqLPpyOMnIXlMpEh5jmmbGsb3ASu-qSS_yBkG-BNVP5DIEEuqzsl8U2ntsgpEi12IxMEzgadt5ChUjtpDMcTMjPepqERaPS3a5z-e31roGCe6bW0UMi1RO2FlE9eeeBMdX-03WFgkfaylQm1igUod5ZK64gPz8btGI8j3SRqy9ZE1sRac0GADgxNaR4b3POPle_e7BKw12pYvmoiL7YbeHTYxAy2zKFiIxp-48POBlHGWlrXFzXfKD01Pq1tibPspxQdU1a1WPKoyDSTNlOXCLvxWtelZjJZSFetWERZKAMLeybAReB4MpbZ29H_nHw3xF9u6uYCwddnKr2plWBFuFBdmCSHTlqoNRuM3yZT0vvY7zBRBdgIuMNsbbVgRIaG_U5Bo0giolDLfFIuAm9IiVddA4zr6mMdLjs9Z60EJxTJnYJOZ8XmkknHBWHlfw2cZV_y3SOfNKwbY6C7irxaQUZHfWTQqTEDipzqQVj2bcN1ALCH6yDAhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0c38ef88.mp4?token=hJ07fAN99KcSJu_qcUQegaHoPNZ3LlSdmrXc6fU6iolxF2gv_5b2xPcvdMB6LJhLKcvWltG4xkPoQ3do--cZjxEI_oVcnnj_ioWTrJLJKcFt10knD4GZW0HGr7k0T6_EEUMuPeuoF8VqnH9dcQ8zss_Q4h9zgjcI6yafn1m79bPMs5s4y7RKCGqLPpyOMnIXlMpEh5jmmbGsb3ASu-qSS_yBkG-BNVP5DIEEuqzsl8U2ntsgpEi12IxMEzgadt5ChUjtpDMcTMjPepqERaPS3a5z-e31roGCe6bW0UMi1RO2FlE9eeeBMdX-03WFgkfaylQm1igUod5ZK64gPz8btGI8j3SRqy9ZE1sRac0GADgxNaR4b3POPle_e7BKw12pYvmoiL7YbeHTYxAy2zKFiIxp-48POBlHGWlrXFzXfKD01Pq1tibPspxQdU1a1WPKoyDSTNlOXCLvxWtelZjJZSFetWERZKAMLeybAReB4MpbZ29H_nHw3xF9u6uYCwddnKr2plWBFuFBdmCSHTlqoNRuM3yZT0vvY7zBRBdgIuMNsbbVgRIaG_U5Bo0giolDLfFIuAm9IiVddA4zr6mMdLjs9Z60EJxTJnYJOZ8XmkknHBWHlfw2cZV_y3SOfNKwbY6C7irxaQUZHfWTQqTEDipzqQVj2bcN1ALCH6yDAhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
عدسة نايا تستقبل رئيس البرلمان الإيراني   #اخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88152" target="_blank">📅 12:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88151">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇹🇷
🇮🇱
توم براك:
كنا أمس على بعد خطوة واحدة من مواجهة عسكرية مباشرة بين تركيا وإسرائيل.
قصف إسرائيل لمطار أبو الظهور ينذر بمواجهة عسكرية مباشرة بين إسرائيل وتركيا.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88151" target="_blank">📅 11:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88150">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0774535f.mp4?token=P5Aa8f-b8aWzsiQsBoaNPlFlfEHHrGLQ1vOS2ytuLi1Fs7uIK6HoEzW7vPwh8RcVmkkB9yluNtoBXpXbICJlgeSj0fQDyGdXqd1UooPdK1ldSBPtSK2Em9HI-UOhu5VAAoKf5tpBtMtRveD5ItMH98UTMCT0KGjIHmdS5DpQxWmwT9_mBV76s5_IbmHYGvFK3xTEsB-LdVTZqT-rPQRaEyza-4ctHFgycLL9uhvvV63aq38XUP1cOlStl3yFLFW8ZvgdjJLUwgrO6Kn18URiielbfdD3mkwuE-7URgwBTvnMr8M5mGbbpk6NUjcahTsAMSUIsOM81_o188JjaVQ9Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0774535f.mp4?token=P5Aa8f-b8aWzsiQsBoaNPlFlfEHHrGLQ1vOS2ytuLi1Fs7uIK6HoEzW7vPwh8RcVmkkB9yluNtoBXpXbICJlgeSj0fQDyGdXqd1UooPdK1ldSBPtSK2Em9HI-UOhu5VAAoKf5tpBtMtRveD5ItMH98UTMCT0KGjIHmdS5DpQxWmwT9_mBV76s5_IbmHYGvFK3xTEsB-LdVTZqT-rPQRaEyza-4ctHFgycLL9uhvvV63aq38XUP1cOlStl3yFLFW8ZvgdjJLUwgrO6Kn18URiielbfdD3mkwuE-7URgwBTvnMr8M5mGbbpk6NUjcahTsAMSUIsOM81_o188JjaVQ9Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
إستهداف مركز شرطة بواسطة طائرة مسيرة في ولاية طرابزون التركية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88150" target="_blank">📅 11:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88149">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
في أعقاب ادعاء البيت الأبيض بخصوص تعليق المفاوضات مع إيران إلى أجل غير مسمى، قال مصدر مطلع مقرب من فريق التفاوض:
"لم تكن هناك مفاوضات مباشرة بين إيران والولايات المتحدة أساسًا."
أجريت محادثات مع سلطنة عمان بشأن فرض سيادة على مضيق هرمز. بعد انتهاك الولايات المتحدة لاتفاقية إسلام آباد، تم تعليق المحادثات مع الجانب الأمريكي، والمحادثات الأخيرة لم تكن لها أي صلة بالولايات المتحدة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88149" target="_blank">📅 10:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88148">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
إستهداف سفينة في باب المندب قبالة ميناء المخا اليمنية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88148" target="_blank">📅 10:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88147">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88147" target="_blank">📅 10:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE80_bkfoHgol5fWwnbsbMHfIO0rXGtLXJ_ufJLPXemswIwxprvy8yInpwG9_EjYLgn_kCuWIRUVo1J6HZ_moxZgQQqzX8CJkan_mjtA8MkoG7essR4PkmdxD0lqWV_P4XmjcsJ3DJC0usXIqIaTSjpoiZT3lHvjrdsRKx0trsqjOpuFkwkkKPVgRIvjQoEmoy20u4djAwZ5ylbu_lB1CY5y4z31cHg4c72OC40tODoetKu0I3CvWzM-vNWAwYseIyH9zpJi6TmA53Uw9CoMcCsmJIbBL2Ozyn3GHckOsHNJhB53HkL1QxffzuMEsMF0ZCIX6yFm9uHeG9Aptj29hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تستمر في الإرتفاع وتلامس 92 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88146" target="_blank">📅 09:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88145">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نايا - NAYA
pinned «
رئيس البرلمان الإيراني   يستخدم مصطلح نايا الذي أطلقته امس ليلا ً  " اخوتنا قوتنا " ليطلقهُ رسميا اليوم من بغداد ..
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/88145" target="_blank">📅 09:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88144">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88144" target="_blank">📅 09:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88143">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65250e4c36.mp4?token=ecTxvsxmS_a5cDil7vmOHHPXM49rroM10L731kIQVB5WG2EmBQTF0JUrHxjT9xwnoZ5yQ9sVgVnLK1dMGVLJBsAOQyqpWSlGJUgGvlbx_EveI61eVxznx7L3pDNToHDgSYL9oWWzsWqTXF5roMPFvhLVOww0JzaEth-Ol4-KFtzPTyVhZMhZ8U6G7wi-YBAFvqZPJQ8j5M23krHCmUbW7iNrqR8zTSIu3xyWXu2M0fDORRjV9aA9YYggBCIFStqSha-1JE3xkSTN0RjAQOEz1I1jLGNFfF2gVjuS-AKMvNlEdEK7MZk-NoKNU1urE5FhoHAhAt5-GNxOwaMAZ44kcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65250e4c36.mp4?token=ecTxvsxmS_a5cDil7vmOHHPXM49rroM10L731kIQVB5WG2EmBQTF0JUrHxjT9xwnoZ5yQ9sVgVnLK1dMGVLJBsAOQyqpWSlGJUgGvlbx_EveI61eVxznx7L3pDNToHDgSYL9oWWzsWqTXF5roMPFvhLVOww0JzaEth-Ol4-KFtzPTyVhZMhZ8U6G7wi-YBAFvqZPJQ8j5M23krHCmUbW7iNrqR8zTSIu3xyWXu2M0fDORRjV9aA9YYggBCIFStqSha-1JE3xkSTN0RjAQOEz1I1jLGNFfF2gVjuS-AKMvNlEdEK7MZk-NoKNU1urE5FhoHAhAt5-GNxOwaMAZ44kcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
قاليباف:  في حرب رمضان، أدركوا قوة صمود إيران.  المقاومة في العراق هي إحدى الركائز المهمة ونقطة قوة لهذا البلد.  المقاومة تجاوزت حدود إيران والعراق والمنطقة، وأصبحت عالمية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88143" target="_blank">📅 09:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88142">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e6b038ce.mp4?token=ZOJNNuKExav3TvEw7pLSUmtaHISOwiQEzsXLz0IHR-8KlE86pORm4ULHrUhAqIDhbrqyaB3cHYWE97YPsePeIL7r-T9QDEcnjsBMq-x2N7wZIuXoognwumhmqinJrslRGZ14XTHuEa5PN_xG37iu-NvlAUlY9kFjOAOpceSB8XolGnXfWQVNdf4mKvHtwaTDjmxPJyR6lAQMlzqbX5q6OcFyaDPFxq7Ys9p_qdfWnXo2wqoBPJZBpa59LwHj36uvTzlKXKHYCT6lMxAmqU-8FEBod00-Hls3mIFS5SA81dEKrYyiasWObi5lgftgzgMaBonN8a2301n8V_xPrjJ_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e6b038ce.mp4?token=ZOJNNuKExav3TvEw7pLSUmtaHISOwiQEzsXLz0IHR-8KlE86pORm4ULHrUhAqIDhbrqyaB3cHYWE97YPsePeIL7r-T9QDEcnjsBMq-x2N7wZIuXoognwumhmqinJrslRGZ14XTHuEa5PN_xG37iu-NvlAUlY9kFjOAOpceSB8XolGnXfWQVNdf4mKvHtwaTDjmxPJyR6lAQMlzqbX5q6OcFyaDPFxq7Ys9p_qdfWnXo2wqoBPJZBpa59LwHj36uvTzlKXKHYCT6lMxAmqU-8FEBod00-Hls3mIFS5SA81dEKrYyiasWObi5lgftgzgMaBonN8a2301n8V_xPrjJ_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
قاليباف من موقع استشهاد الحاج قاسم سليماني وأبو مهدي المهندس: لقد كانوا أبطالًا أنقذوا العراق وإيران والمنطقة بأكملها من شر داعش.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/88142" target="_blank">📅 09:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88141">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7fe5e0325.mp4?token=VvaXprgzSfAJQxw-vy9HFh9YLKUf-l6MwlCjNqdOQCHxgDMqh67MPGxagVz1qIPexyYDZJlv_-ptA7oe9NINuLvTsvUSSdudrwqr1KpSIaBMwJ_eAgPmVIxQdPyp8dHIhR0u_xDGbOdFrmLdSF41_J11YbhIpH5vfh95612VDQyZPQzjUnlhwPcAKdLHI8frHwc0VrKG2Sc7u2P5dL4U33ySVCw6V3LmPJsqd0dLL3Rz1orzNY7QzxOHsNb8c8waYn3Z70z_V8nZ9_gWmfBKvtl1Rv8i5jTozBz6kOLqNooT6CGPtpOMdCkn0JP6m74CndPE74goXI78dXOtjuafeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7fe5e0325.mp4?token=VvaXprgzSfAJQxw-vy9HFh9YLKUf-l6MwlCjNqdOQCHxgDMqh67MPGxagVz1qIPexyYDZJlv_-ptA7oe9NINuLvTsvUSSdudrwqr1KpSIaBMwJ_eAgPmVIxQdPyp8dHIhR0u_xDGbOdFrmLdSF41_J11YbhIpH5vfh95612VDQyZPQzjUnlhwPcAKdLHI8frHwc0VrKG2Sc7u2P5dL4U33ySVCw6V3LmPJsqd0dLL3Rz1orzNY7QzxOHsNb8c8waYn3Z70z_V8nZ9_gWmfBKvtl1Rv8i5jTozBz6kOLqNooT6CGPtpOMdCkn0JP6m74CndPE74goXI78dXOtjuafeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
قاليباف مخاطباً قادة النصر:  أبو مهدي وقاسم الأعزاء. انظروا إلى ثمار جهودكم ودمائكم الطاهرة.   اعلموا أننا وجميع المؤمنين بمبادئكم في إيران والعراق، لن نتوقف عن العمل حتى نحقق أهدافكم، ونحن على استعداد للتضحية بأرواحنا وأموالنا وسمعتنا في هذا المسار المقدس.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88141" target="_blank">📅 09:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88140">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس مجلس الشورى الإيراني من موقع استشهاد قادة النصر:  العراق دولة مهمة في المنطقة.  الحكومة الأميركية اغتالت البطلين في محور المقاومة اللذين أنقذا المنطقة من "داعش".   في هذه الظروف الراهنة الكل رأى قوة مقاومة إيران في حرب رمضان.   اليوم الجميع أصبح يعرف…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88140" target="_blank">📅 09:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88139">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بدء المؤتمر الصحفي لرئيس البرلمان الإيراني عند موقع إستشهاد القادة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/88139" target="_blank">📅 09:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88138">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUACGcuSHBXpDkVGPCzibhys2vqZjzUeINNpxOZoL0sIwgBmXMSt-YV-vQGkUjznVvH8i7BU86zXFaRDPxnuzgYUcjXLwNFsOVYC3f_1HNEHbYAHVqFbmJ2dgdLncshlOM5blrNWDOquJH2EuSOstRB7X4fZVBxqnT4dwdDOZWsFgceyfG8xHCd-riJYKEunjhdYpMPAWyKGcqkkOSvvvnxWwReHkFNna1eUnL5ml0HAjoHtsGKSNMz8CpCYz8FCcETEueUh_kXHbHiCpeAQ1PlrYQJ110l9ywhUsySNrYO-3piJkYib9MKmAP7O6nZh8TntURYSK84UIrUYamaYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس أركان القوات المسلحة الإيرانية:
الدول الواقعة على ضفاف الخليج الفارسي الجنوبي، التي تصدر بيانات مختلفة تعلن فيها أنها لن تسمح للولايات المتحدة باستخدام أراضيها ضد إيران، يجب أن تعلم أن لا شيء يفلت من أعيننا.
من غير المرجح أن يتواجد هذا العدد من الطائرات العسكرية، وخاصة طائرات التزويد بالوقود، في القواعد الإقليمية دون علم الدول المضيفة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88138" target="_blank">📅 09:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88137">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cO-V7xgnymsSIB9f8N9MmnKbUP4hoM1Pk-Zq_Ua8YeenmYbJZo8lGExSmk2K2QgEJgjjLtx72efDceA22aVfNglQ4YCtv2rUqR0Rh9Eh0OrseuO8LbR5eFvw4DSg8momAfILy23xniLR07uIvvnN4UoESTFkoWuezH1WfYEbJ-I4X85JWbzP33YqC_NSxw6v1SmtBA9BlHJ2lhWfz5noKq7z3Za8SxD_DvOwrE--JE4lqJ8UITnq3ZoFN-gv-zjYA5SVB1-MmutNg1bfnCZbbVRUeuJ9deFWNzGmTdm7ygLlKzsepmDs6juj6NFnx_5c2iZCaAoIIRgGNU1nbYTkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وصول قالیباف إلى مكان استشهاد  الحاج قاسم سليماني والحاج أبومهدي المهندس بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/88137" target="_blank">📅 09:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88136">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd61bb885.mp4?token=Nysa8S523Iqq_M7yvzfroUb0hhVStV3_laE8uq6-g6Qpu27S1XVFP9ivNS3lCve-Jvp-nkjOX-qfbXQF0SVZkXSQtDYSzfZrWA_XblQb7iuRlnHntMMlwjqNrdAkBMlHUQExVJzgEp99Dc8hnHvu2WxXA6k0zD5bgu-oQud1gZ_KAtQRFF_vTFWGHvnzBq__SaUtEhByHOJQKmE9LEZEQmsUChL57Xnfa2KMuZDayPYrw4Ghl4DRcGb2xVTYeqILNB9vPrq8Bq52zEc522tuXazdL3KwqYVx7nNLd1wrWaCOi75I60mNdfIp_--uRyoAjPMqstVCRn7LnmEdRWO_AIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd61bb885.mp4?token=Nysa8S523Iqq_M7yvzfroUb0hhVStV3_laE8uq6-g6Qpu27S1XVFP9ivNS3lCve-Jvp-nkjOX-qfbXQF0SVZkXSQtDYSzfZrWA_XblQb7iuRlnHntMMlwjqNrdAkBMlHUQExVJzgEp99Dc8hnHvu2WxXA6k0zD5bgu-oQud1gZ_KAtQRFF_vTFWGHvnzBq__SaUtEhByHOJQKmE9LEZEQmsUChL57Xnfa2KMuZDayPYrw4Ghl4DRcGb2xVTYeqILNB9vPrq8Bq52zEc522tuXazdL3KwqYVx7nNLd1wrWaCOi75I60mNdfIp_--uRyoAjPMqstVCRn7LnmEdRWO_AIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
لحظة وصول رئيس البرلمان الإيراني محمدباقر قاليباف إلى مطار العاصمة بغداد وإستقباله من قبل المسؤولين العراقيين.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88136" target="_blank">📅 09:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88135">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
🇮🇶
رئيس البرلمان الإيراني محمدباقر قاليباف يصل إلى العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/88135" target="_blank">📅 08:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88134">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebabbf606.mp4?token=Pe0P1st5W0LnxqiyyvZ5Zq7pYlHTuI1JjARNkJGjly_nDJqJAna1wMo7B-feNFiTiDgcUtmDhnZqoMaeTLwZrxAeCm9TCOvxm2SwU3luLQknxuDjR6W5fZDHs4nF9JrTjqTdZvgX6JmiTFgB65Ov-r3iy3jSBMZ8KmzbvIrdeIFltW59FSgp1Dep47toYGiWfROAlAZ6z9rO-B7jC4nDADN0wDNzRNtpFNEVS_TzeLJpe88Vri7-J8p50PduVmGCM8o6oPX5tEYNE2CFmObaYW6ldxDOk2vntJiiHZlaTJEmiYthlxCdE3PUbr_J9KjQ9JMy4nZ9trALBqUg2TWARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebabbf606.mp4?token=Pe0P1st5W0LnxqiyyvZ5Zq7pYlHTuI1JjARNkJGjly_nDJqJAna1wMo7B-feNFiTiDgcUtmDhnZqoMaeTLwZrxAeCm9TCOvxm2SwU3luLQknxuDjR6W5fZDHs4nF9JrTjqTdZvgX6JmiTFgB65Ov-r3iy3jSBMZ8KmzbvIrdeIFltW59FSgp1Dep47toYGiWfROAlAZ6z9rO-B7jC4nDADN0wDNzRNtpFNEVS_TzeLJpe88Vri7-J8p50PduVmGCM8o6oPX5tEYNE2CFmObaYW6ldxDOk2vntJiiHZlaTJEmiYthlxCdE3PUbr_J9KjQ9JMy4nZ9trALBqUg2TWARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88134" target="_blank">📅 08:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88133">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا  مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88133" target="_blank">📅 08:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88132">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الديمقراطية تدين التدريبات العسكرية المشتركة بين الولايات المتحدة وكوريا الجنوبية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88132" target="_blank">📅 05:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88131">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇸🇾
دوي إنفجارات مجهولة في مدينة طرطوس السورية.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88131" target="_blank">📅 01:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88130">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/88130" target="_blank">📅 01:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88129">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kg8LFFSy1IPnels9e4MMAmxJctZIOWkzJUUdvtfExv8vVmTwpmsBqZYnBcokVcOWlgPZNAoUdu2SxRHpnf4uHcGDQVrWYG0Ub3ptnC0gNJyC10KQfezRKIIneTpfNdU30lPtn0yt3CF_e6nLvYDE06vHUBBC-_Xk2-3fzsJay1yV_D4WOUZDsy3f0qGnKn7uFmG3de4aeW1oIhu3VK4kvxGEw2sebBDgkwrMkg3I_ooK4JCNUH0rzXtoSrDH0wAXjoczF68pW4Lt2j4Fzx2Wt103ia-DyZ3sqPlnuApYf0FpJcZd1rncq5Sqe92_oxUWdT2qVG41SLWu817BM8XzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
أخوّتنا قوّتنا
مع الزيارة الأولى للدكتور محمد باقر قاليباف، رئيس مجلس الشورى الإسلامي الإيراني، إلى العراق، وبعد المساندة المخلصة والمضحّية التي قدّمتها المقاومة العراقية في الحرب ضدّ أمريكا وإسرائيل، وكذلك التشييع المهيب لقائد الثورة في العراق، ستُفتح صفحة جديدة من التعاون والتآزر بين البلدين الشقيقين.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/88129" target="_blank">📅 01:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88128">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d822181f0.mp4?token=nST6bdCDZBmGA3tggIkq6vTX7QadpBucmQ-7GBUTi_4XIw7Tdsh-cLBGD1qioswEYRZ78gt5w2iNWEav9P2-LKwgA0KuyisQ5zM2n16lSvRCmRR7cmzdQpIKDXAtTFl9vxsg05nkrSRihPQNmVrpwpB_e5J1EilmRYt88u0mSZinCcmIYeC5TB91IMQWaV22xPdx0GNJ9W5fHe5k_7-KD8C3KUpN8aY1URlp3gpttXJ5gpDFzQhUkz5wdwWNs9g36vog_7iJ2yLkGHV6GgCBI3-eVkP8qsdhQAnz12b2oGmvPBgcTcgWRR-OM0Q5jUaEKeuUhpGRqU9F7zKrvART8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d822181f0.mp4?token=nST6bdCDZBmGA3tggIkq6vTX7QadpBucmQ-7GBUTi_4XIw7Tdsh-cLBGD1qioswEYRZ78gt5w2iNWEav9P2-LKwgA0KuyisQ5zM2n16lSvRCmRR7cmzdQpIKDXAtTFl9vxsg05nkrSRihPQNmVrpwpB_e5J1EilmRYt88u0mSZinCcmIYeC5TB91IMQWaV22xPdx0GNJ9W5fHe5k_7-KD8C3KUpN8aY1URlp3gpttXJ5gpDFzQhUkz5wdwWNs9g36vog_7iJ2yLkGHV6GgCBI3-eVkP8qsdhQAnz12b2oGmvPBgcTcgWRR-OM0Q5jUaEKeuUhpGRqU9F7zKrvART8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇱🇧
غارات اسرائيلية على الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88128" target="_blank">📅 01:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88127">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي: ترمب طلب من كبار مبعوثيه وقف محادثاتهم مع إيران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88127" target="_blank">📅 01:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88126">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي:
ترمب طلب من كبار مبعوثيه وقف محادثاتهم مع إيران</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88126" target="_blank">📅 01:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88125">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmcowgkjslLqfSR1XkWfj8D8KCt9E9LkbBlqInoCZPX_ffMPGH8CEV_LlO6WlekYxOAAjQUPVOFNNwdUB3LphiDOFCFVxUXEC4HngeO7RNLuDvfI0nEHy4oJ7KC2RIBcuMZDS5B1fOHX3o1j_Xzty_7Z147kAfvKqegm8PoXNPSTH2MYFwrzqjK_rA-SSd888Kob8TiLc9Yx4CsxqnzIfqzyK_EvWfq0h_sdGTfR4gJpdq1Ck061K625FeTpaTeu5eMgr8BP3mAMnWDpabxOj_NDApvxDyKdqUAQEpdO5KgidLPQPrQ9sqilDx54s_XI5ZtBzoQLu1oyMZirkvXM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مالذي حدث في جلسة الإطار التنسيقي الأخيرة
اين الشيخ همام ابو إبراهيم في الصور ؟!
شكرا للمجلس الأعلى</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/88125" target="_blank">📅 01:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88124">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
🇫🇷
مواقع اوربية : فرنسا ستقوم بطرد دبلوماسيين اثنين ايرانيين ردا على اتهامات لايران بترهيب لدبلوماسيين فرنسيون في طهران
بیا بچه خوشگل</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88124" target="_blank">📅 00:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88123">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇰🇵
جمهورية كوريا الديمقراطية تدين التدريبات العسكرية المشتركة بين الولايات المتحدة وكوريا الجنوبية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88123" target="_blank">📅 00:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88122">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
نرفض الاتهامات بإطلاقنا صواريخ تجاه الإمارات.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88122" target="_blank">📅 00:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88121">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea4713aad.mp4?token=PZxeDN610PeigCTT-vOmrQC6Izh1_l1TxGHfz1ZN2_UiNdZTvC0HxORWOfbLTZD4hGNN821Isor2ez898oQRJpD32rfhWRChQVMKQ1O-mHcY4QBWfK-abP0SR3P4dtFnp7v-44qiVZVBa8U3ppTswG2tpffKysqIPxuliklCyAAbIfYBOWJHFhNI3iBZg9wQFG1MC2P8mcOY1_HDuniTKM6aIQTfYEORY82vtUWDrjN9Nx1YvPxlF9IgkMXZ620cW_uyX8Jx_rgm65vtDq6uxpb1XtSVyzP47LLQrPUJKQs4f3nqzzZeSXLLQjZ9kxKPrCchCxLB_mBKfzbCjfbKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea4713aad.mp4?token=PZxeDN610PeigCTT-vOmrQC6Izh1_l1TxGHfz1ZN2_UiNdZTvC0HxORWOfbLTZD4hGNN821Isor2ez898oQRJpD32rfhWRChQVMKQ1O-mHcY4QBWfK-abP0SR3P4dtFnp7v-44qiVZVBa8U3ppTswG2tpffKysqIPxuliklCyAAbIfYBOWJHFhNI3iBZg9wQFG1MC2P8mcOY1_HDuniTKM6aIQTfYEORY82vtUWDrjN9Nx1YvPxlF9IgkMXZ620cW_uyX8Jx_rgm65vtDq6uxpb1XtSVyzP47LLQrPUJKQs4f3nqzzZeSXLLQjZ9kxKPrCchCxLB_mBKfzbCjfbKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇮🇱
إذاعة جيش العدو   بمعنى آخر، لا علاقة للهجوم بـ"تعزيز القوات الجوية السورية" كما ورد في بعض وسائل الإعلام مؤخراً، بل نُفِّذَ لإيصال رسالة إلى نظام أردوغان مفادها أن إسرائيل لن تسمح بوجود عسكري تركي على الأراضي السورية. كان الهجوم يستهدف التهديد التركي…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88121" target="_blank">📅 00:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88120">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇱
مكتب نتنياهو: وافقت إسرائيل وسوريا على وضع قائم على "الوضع الراهن" في الأمور الأمنية، وهو الوضع الذي كانت سوريا على وشك انتهاكه بالسماح بنشر قوات تركية في قاعدة جوية بالقرب من حلب.  لقد حذرت إسرائيل سوريا مرارًا وتكرارًا من أن مثل هذا النشر يشكل تهديدًا…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88120" target="_blank">📅 00:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88119">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
توم باراك: تم رصد طائرات تتجه شمالا نحو أراضي ‌ تركيا⁩ وكان من الممكن أن تستعد للرد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88119" target="_blank">📅 23:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88118">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇦🇪
🇮🇷
‏
الخارجية الإماراتية:
وقف جميع الأنشطة التجارية والمعاملات المالية مع إيران حتى إشعار آخر.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88118" target="_blank">📅 23:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88116">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6ux7z5JKGV0tTtLTQN3pKqcwqZhGTYXp0rTXMMTCRkvWzzRPwbfftwSj-ewzJrdQv0YdYBxByW7XX4k0QHVDVGgn2h2UspMJIwLH9IJqIHjKfdK0SSdLtSzFDw7qPi-k-Xy9aLoTJCM5QgjzuLq45h7f9yUOj-huMn0_nohF-GyXHRm8Xfn0wJjcOfMkd4jttVI0KvG6fC704IadpkhLOUEk2OcKaoh90t7OT7fjlJBwkVu6McYz0674sV2Nh-uXkDe8NOZzwU-RDnx-5EltAOCYl-ca35Dh8nVFZXgiEPnPMUgefbW5V8Ozuz9cA8V0gPCHf04eYAcunsThj0Xiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في بلادي، يُباع النفط، لكن ليس من حق العراق التصرف بأمواله، لأن هناك احتلالًا أمريكيًا لأموال العراق!
وطائراتنا كلفتنا الكثير، لكنها لا تحلّق في سمائنا إلا بإذن أمريكا، فهي تحتل أجواء العراق!
ولا تقبل أمريكا أن نشتري الكهرباء من تركيا أو إيران، ولا أن نعقد اتفاقيات مع الصين، وليس من حقنا إبرام عقود مع «سيمنس» أو غيرها لإصلاح وتطوير المنظومة الكهربائية، ولا هي تصلحها؛ يعني: «لا أنطيك ولا أخلي رحمة الله تجيك»!
الشعب يريد السيادة الكاملة للعراق.
فأين السيادة يا سادة؟!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88116" target="_blank">📅 23:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88115">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
تسبب انقطاع التيار الكهربائي على متن مدمرة تابعة للبحرية الأمريكية تعمل في بحر الصين الجنوبي الشهر الماضي في حرمان طاقم السفينة من مياه الشرب والطعام الساخن والمراحيض العاملة وتكييف الهواء لمدة أربعة أيام.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88115" target="_blank">📅 23:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88114">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
توم باراك:
تم رصد طائرات تتجه شمالا نحو أراضي ‌ تركيا⁩ وكان من الممكن أن تستعد للرد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88114" target="_blank">📅 23:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88113">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الإمارات
: الصاروخان الإيرانيان اللذان تم رصدهما اليوم استهدفا حركة الملاحة البحرية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88113" target="_blank">📅 23:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88111">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hkjsu6Lb1igGpjurbTq1SrYk8_3RU5_ajcOdYNz2U4iCp68pNi94I8_vBa7gsUkkqqFhO9jKEZgvTk46Tu8xjv4kQuhyl97rqibpvn1tIkylrCFN-nLc9Kd3NXNuw6KIz6pHkLLSEE__ep--ORXM_oiv4ZS-eTYLyuTCVPfpdkCHbiu8ivW2ox5u-8GZKruyV6VXB6BiIrqE8THIz-233rCyS0ds3Z2BEu8OQMKMmZWqptPDFxQciDrnNNMsSjGOAXqlkrGWjdi3XufO3dlh7V3kF5Jw07inh5vEqV5jwutXe7ygj2PKLHdGKqD7F9dO9IsfY2Rsg251V4I5OVehzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف صاروخي لسفينة سعودية قبالة ميناء المخا اليمنية من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88111" target="_blank">📅 22:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88110">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
عن مسؤولَيْن إقليميَّيْن: إدارة ترامب أبلغت عُمان معارضتها لأجزاء من الاتفاق الذي لم يُعلن بعد ويشمل إدارة إيرانية عُمانية مشتركة لمسار الخروج من مضيق هرمز.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88110" target="_blank">📅 22:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88109">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8s1KCT2LgjXD9dW_EtQyppQtTYHxFufDQBfYit0x-mWKdTbCwfVVOCsPk_UmBsvrJ8wtxpfDObsIX2QrSN-Ji2iP4NEbHI9WS-Q37KNJm3Lp2ureC4JPQrGQDPysbrf5tLRHaHS8GqQvELAVkzlrJpDKNWL4xd2RRt2SmYJBj3cjl9vw9PGb77fmsqgMhHBCNzSc32pBL3TxOA2f4mQitN1W6uzxe0EUOWBi1L-MPVRcD_WB3l57Xv4HuvF0-Qdo-puKmlj8YTNIPhRWrhyBjVGKJ_i3H6nG_h_ZxxqWe3xvTLqveFN6muqIsLCtjzaWQEoDDaQgwmnq7KCHHNnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
ارتفاع العقود الآجلة لخام برنت إلى 91.02 دولارا للبرميل.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88109" target="_blank">📅 22:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88108">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية خلال الأيام الأخيرة قبل وقف إطلاق النار تجمعات لجنود وآليات جيش العدو الإسرائيلي عند الأطراف الجنوبية لبلدة زوطر الشرقيّة بسربٍ من المسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88108" target="_blank">📅 22:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88107">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇦
🇷🇺
تنبيه الغارات الجوية في كييف والعديد من المناطق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88107" target="_blank">📅 21:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88106">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
وزارة العدل الأمريكية:
توجيه اتهامات إلى 17 إيرانيا بتنفيذ حملة واسعة لسرقة البيانات عبر هجمات إلكترونية، المتهمون استهدفوا 144 جامعة أمريكية و178 جامعة أجنبية و42 شركة ووكالات حكومية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88106" target="_blank">📅 21:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88105">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔻
حزب الله: بالفيديو سِيري عَلَى اسمِ اللَّه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88105" target="_blank">📅 21:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88104">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqOC-wd1oo1VncrQBRT5Q0D9xPxgeDF8m0cNI5AkEygELVLa75hIRRp0aDIsTjkfJoVpmev3v_-h1A8SrsfD16w-OuMSD9W9aSJndbNvMwGTgXK6JdzhBImGhs93k7PXTO8i25Ut2aAoVXWgpcIKjNWZD3xx2fFfs2gG4AeqBjeH2QNm99keetCATLdnN0EI-UcHGnMapqNYqIye20fTQyEc0AOjrOyZlC59sSVXnKgbX3B7a1AXlmr5d9gvAZ9wENhMr_gV0YZxWJQhQSuaVDrsj0SfeyfCM6VC6fTbanwWFRSd6j2_Ypaa_TmGk31kc9qTVJiwXJT0fiRVqp3AQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية الفرنسي على خلفية طرد موظفين اثنين من سفارة الفرنسية في طهران:
سيتم طرد اثنين من الدبلوماسيين الإيرانيين خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88104" target="_blank">📅 21:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88103">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف صاروخي لسفينة سعودية قبالة ميناء المخا اليمنية من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88103" target="_blank">📅 20:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88102">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjcNEGAITfXkPrIlSH1LhbkruKYO3lYTWpoSbx80MOFc4fXm8uiGTu621Gl_mlSxaP0rKOzoEKTb4tfegsiG4eHmsYUhJzB3A1J6i0GnbpTGvtGaiNH60ziL9geoMFC2WMyhPqN6V1V_ni63xJKePU2MvJcxBDpph3K1YvYHToaEMo_JjJ-nQFGDz4O1oeaJoA_PAWUAqut3xYnfo4MnTYY-JP64CImuCc-f5g9TCm3e7cMKWBbMAz8DWfO7-huwE2FOh_eYZtiTACm4L8mOm5sqH1N7TCTkM-4y7WJ_pXhXP0Ryv9o3ItMMZ7BmoR_vYhzLU3ztI4TIEs42YvzswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الولايات المتحدة تفرض عقوبات على رئيسة "المحكمة الجنائية الدولية" توموكو أكاني.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88102" target="_blank">📅 20:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88101">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#متابعات
🇮🇶
ازدحامات تشهدها معظم محطات الوقود في العاصمة العراقية بغداد بالتزامن مع فقدان البنزين المحسّن من عدد من المحطات ما أدى إلى توافد أعداد كبيرة من المركبات واصطفافها في طوابير طويلة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88101" target="_blank">📅 20:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88100">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw1LBmtVu4zcC61AK_vuQZBP1SxMZ9QGccep8QTaHI4ZUbHuyGtGYreiQvXFbbCD99dLjRsWG0XkmlwDR2j3_L-b74gBEEXfBZjuSwAltzBhj5ZZkPiMyZKXUOAZb_nwEaek8nELLtTnwNrZaxaZUtOkM6FD2aJgKFxdM3_NHAnlE2RV5LCLK5m876fHbAxPQOGfscXY_Kr1KLABSa3cRqC1Owi7c4639PuMHPrnTL2pRRDIdT-VL48--7F8FhTF5BlOh9XMbln6SY7dsXZ3Dfn4PWxHv-9TTuBe5wPXvAALlfiRrxQwsrKvknPCgpJvQQe1mYSOHPbxo2jI68D8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالبياف
:
يعتقد الأمريكيون أن الضغط على إيران بشكل أكبر سيؤدي إلى انتزاع تنازلات لم تكن جزءاً من الاتفاق.
‏بيسنت وهيغسيث ليسا في مستواهم على الإطلاق. كفّوا عن انتظار هؤلاء المهرجين ليُخرجوا معجزة وينظفوا الفوضى التي أحدثتموها.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88100" target="_blank">📅 20:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88099">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a206509c.mp4?token=aRAIhDqodZ_cq_u_iuarTG1FOPgaU5hzvpWVUR01lbQ7xzsSPXJkI4l2fPKmbi_mPhBob0VuJDYedZPl9Xv37UUgHZIy1zgpsjMbYIoHB5DrMOQl1JYIkABXu_ITpbN0IfRb1AU-1SRMJqrEV8wNEBJt3pWCbb_aE5waf_31AcDzzMDqph6VY69Z93fwPG6sKAeNKLv7TcbCP5COH48wfib8rvvO6diisdjv5vd9UuKYu0lLhVFz-jhKpa-XxDf_tHvZfQ-9Iv-3L4ucerbR9d40EhTsQauRWgZm8sFzNGqnFza4NbOl1FLcIUULYMnUi7tf0MTWSbS8IPu57fvzCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a206509c.mp4?token=aRAIhDqodZ_cq_u_iuarTG1FOPgaU5hzvpWVUR01lbQ7xzsSPXJkI4l2fPKmbi_mPhBob0VuJDYedZPl9Xv37UUgHZIy1zgpsjMbYIoHB5DrMOQl1JYIkABXu_ITpbN0IfRb1AU-1SRMJqrEV8wNEBJt3pWCbb_aE5waf_31AcDzzMDqph6VY69Z93fwPG6sKAeNKLv7TcbCP5COH48wfib8rvvO6diisdjv5vd9UuKYu0lLhVFz-jhKpa-XxDf_tHvZfQ-9Iv-3L4ucerbR9d40EhTsQauRWgZm8sFzNGqnFza4NbOl1FLcIUULYMnUi7tf0MTWSbS8IPu57fvzCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏انفجار هائل في مصنع فنلندي قرب الحدود الروسية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88099" target="_blank">📅 20:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3Odmr1WCc2Xt-CVfsfGs7VTTMwoLc5yZt5mH-dwM6Vz9uvw_e1C2NwCgbiQuPk1OeI_gOYImAPxpC6uyM2lHrnLLbwSVfPBpKxFvQ-FrXrQqwn3-rul2i0o4O5FQl-BMYpQIUVHrVWeeT84KBuuu2XAphwF88uBwfEhwmBV29z_49sKnrpCOLZ1nNunKZRRm-raDZgJjDhJhzuRYy-9vHpD9sBAVd-XdkKo2W92xnuEAoBAykTdFw6x2-i8x4TXhuJW_JbSpXWH0OvPXwXQkQGNqnVjjXRI_R6JIh0gxE2NJiLA1S7OMBHwY3BIkCuE0Ndttbxw7HWWnJcKqKAeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unWbxDBJRm9h1mNb7vQNlFRkBDidIqesiQ9AA4x5lV9nnfoH-2dnUcKddfQiP59XK_KVxkECLCt6KGViebgO6hm5UfE1xXKGTEBd53-C7gwG_aEeTd9RUhjcm5SzRjyQoebROih4C7BppE03_bFb-n6Q9ZShN4VzzLxwoZIDi0gjMxqZ6QggGIm3CqHZgvNCzybRoVFJ9BgC_NMvtTNd1_sAwGPoVHkY5FfhKT168IxwY7eOiLGGS6elRiMoAmvYSCQv_POjy5Zz2YSWrpYz5SOHcVoh4bGWBIy9fzoriR8BSaBQIk8_xRSBt-LDIu5QDiYWxMG8t79sGD22Ek5gog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
تسريب النفط الخام يضهر بوضوح من امام خليج عمان بعد استهداف عدة حاملات النفط لمخالفتها قوانين عبور مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88097" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88096" target="_blank">📅 20:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88094">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897db561c3.mp4?token=Y7QVEiDxjPJDHgf4STWgO7_LIPao6QX0Mz4ywifin5B0LoLxWAEuoaLqjJL3PHJjeNiSnNdgG3kdxRmk9sihosSUBKkYdu8yHWuEKC-O6HOOj4O5GVc9QDJbRQ5D-vrWjlbZMWDgzFImi7gENAYjqzPpKysus1vNlk6DjNsQkqC_3WiTF7AFVlzYl5hcEIqeIkwQdt-FSEzvXVx4aIPVLO3ftt4ApVYWoIc29vAd1cfepMuN0GLGO1_0fGERESvZgH9pbpL7bbzQ7pboXxWHbmQ2bLaq4awJJWhkGLjRg4bBS7iu9MZlg9TCpC9qGEjp2n-7UsNWq4jPEs-c3eltqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897db561c3.mp4?token=Y7QVEiDxjPJDHgf4STWgO7_LIPao6QX0Mz4ywifin5B0LoLxWAEuoaLqjJL3PHJjeNiSnNdgG3kdxRmk9sihosSUBKkYdu8yHWuEKC-O6HOOj4O5GVc9QDJbRQ5D-vrWjlbZMWDgzFImi7gENAYjqzPpKysus1vNlk6DjNsQkqC_3WiTF7AFVlzYl5hcEIqeIkwQdt-FSEzvXVx4aIPVLO3ftt4ApVYWoIc29vAd1cfepMuN0GLGO1_0fGERESvZgH9pbpL7bbzQ7pboXxWHbmQ2bLaq4awJJWhkGLjRg4bBS7iu9MZlg9TCpC9qGEjp2n-7UsNWq4jPEs-c3eltqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مقتل ستة نساء كحصيلة اولية نتيجة حادث عنيف قرب مطار المثنى بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88094" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88093">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">إعلام أوربي يدعي :
تقوم روسيا بشحن المتفجرات ومكونات الطائرات بدون طيار والذخيرة إلى إيران عبر بحر قزوين لمساعدة طهران على إعادة بناء مخزوناتها التي تضررت في الضربات التي شنتها الولايات المتحدة وإسرائيل.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88093" target="_blank">📅 19:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88092">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
اكو نائب حليو صغيرون مجكنم ؛ البارحة المالكي غاسلة بالكاع غسل ولبس ؛ خطية يحاول يقلد ابو عمار مصطفى سند من جان مهاجم بالحادلة بس مجتي بيده ؛ عمو بعدك صغيرون بعد لا تعيدها …</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88092" target="_blank">📅 19:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88090">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b6184389.mp4?token=kMG99TFJNE0mJP-T-AhN0D3XRBhhVX-fO_nqTwSHJVfGQNww29SdOnaOGsuHx7KUfahZpWHiJ0iY7xirqzkorbal5f19ycFLldBGcC7xkFXU3-JA6iNrCO32deFoe23ijrAaSdWRWEOoqlqlTBbGx_RKEblRcDvHj7vdXMTrflGwTEhdB_IKiPbMbNZU7R5v7iw_C6hcgXqFZiHBSMtR1Gnwzmqhk36ekZY1aDWWfA6POdW7dh3L6zVJlvaBG6QuwExd4YeFnrxXArghRvhRwO26yO4DBvaRCEDWWwbPsbNoHh8Eyd2N3tWYLiI4PKy40opqbY08ZRHDpCNmqh0T6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b6184389.mp4?token=kMG99TFJNE0mJP-T-AhN0D3XRBhhVX-fO_nqTwSHJVfGQNww29SdOnaOGsuHx7KUfahZpWHiJ0iY7xirqzkorbal5f19ycFLldBGcC7xkFXU3-JA6iNrCO32deFoe23ijrAaSdWRWEOoqlqlTBbGx_RKEblRcDvHj7vdXMTrflGwTEhdB_IKiPbMbNZU7R5v7iw_C6hcgXqFZiHBSMtR1Gnwzmqhk36ekZY1aDWWfA6POdW7dh3L6zVJlvaBG6QuwExd4YeFnrxXArghRvhRwO26yO4DBvaRCEDWWwbPsbNoHh8Eyd2N3tWYLiI4PKy40opqbY08ZRHDpCNmqh0T6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تشاهد من مختلف انحاء السليمانية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88090" target="_blank">📅 19:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88089">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352e85edac.mp4?token=Cro__ZVlRF-DWrlJoIXSerkBn_sHQ9DHL1CxX0oxmUJIuU0Q1eVKPtvTLY4_My6XzvkUeXUoR78UR3q1r9dJI4QSbLxMkGGv8jcH0djkL-Rvdk4R-5v0Ptm4zqkE-6dZw5dcRtJY6PgpM7nxpMsvZ_D_b_SMQgd7R5Fk95Mir721iYNNx37Jdga_HBP2bZKZ7yxnTE5UGfF5Za8IfiMocDBa8eDdKtWC7C9zqcYvetNVOhttNTluxnCg5LGIqTIwEuwHZKD3pv3SLG973lzvs2RnDnyr0bJtg26S7TcJQpctz4926fOaOe8eCRPSsCmg5RUCmRUL2iRgsorA5YlcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352e85edac.mp4?token=Cro__ZVlRF-DWrlJoIXSerkBn_sHQ9DHL1CxX0oxmUJIuU0Q1eVKPtvTLY4_My6XzvkUeXUoR78UR3q1r9dJI4QSbLxMkGGv8jcH0djkL-Rvdk4R-5v0Ptm4zqkE-6dZw5dcRtJY6PgpM7nxpMsvZ_D_b_SMQgd7R5Fk95Mir721iYNNx37Jdga_HBP2bZKZ7yxnTE5UGfF5Za8IfiMocDBa8eDdKtWC7C9zqcYvetNVOhttNTluxnCg5LGIqTIwEuwHZKD3pv3SLG973lzvs2RnDnyr0bJtg26S7TcJQpctz4926fOaOe8eCRPSsCmg5RUCmRUL2iRgsorA5YlcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد كثيف لاعمدة الدخان من السليمانية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88089" target="_blank">📅 19:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88088">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b671c100.mp4?token=KGb3VlPnYr5ppCARU1rlEEIefPV2MD93GrVRMRS4LJgitX_xUZ1AuUvAk6N_J22n_q1pF6_4pOUwogimn176rF-cGXy3MwrRONtr6S73i9snO4fLfy6ztpalrVIo6w1LOqpAFMYpGfVdUo0o8f_ZJiECvRUXiX6W9hyPVfEix4KBjO47HuljfDusMup0EPWEXtGtv-KN-JuXizZkEoIXd4VdlxTlLSK3-PNL-OGzX-hSjJv7TPCiLgQ-xIskrS-_ndRBTMVHiTwz4D3OvKyC1ySSnfLyQD4RDL0NQgRpr2vo4Zf-_8OAY0XGwUAj8ol849fdbWlWwpz-_A17NJkxf0e5bFGIqzFPYvNY42sa6834T0z342ZfYMFdAiDKcOLUB4xy8_oupc_3Po6u9HQhvSapPZgNSZsIoZdA6uqUGgKMo-nVi3DveDjN-ibOcwzJLAOm4tVIJ5AL140daLkbtNqtyJmf1s3WwpcXUU8SdMdVRk1UbCxOcp_DBbsfLt8rbV6pJqCZLzflFVEjw1s91oXBX_mLbU7ffdjE13mfK9QhMNP8MY0j41Gua-q6uK64vEEq_M887pktN7di0Prv39LXW8HGNd6C_db67A5b4Q5pOj-cD5vABL3-PqWpHEmxqFz1yEg8eBFm4Aqc4TFyHg60YOMqY7YNE334TZw3GCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b671c100.mp4?token=KGb3VlPnYr5ppCARU1rlEEIefPV2MD93GrVRMRS4LJgitX_xUZ1AuUvAk6N_J22n_q1pF6_4pOUwogimn176rF-cGXy3MwrRONtr6S73i9snO4fLfy6ztpalrVIo6w1LOqpAFMYpGfVdUo0o8f_ZJiECvRUXiX6W9hyPVfEix4KBjO47HuljfDusMup0EPWEXtGtv-KN-JuXizZkEoIXd4VdlxTlLSK3-PNL-OGzX-hSjJv7TPCiLgQ-xIskrS-_ndRBTMVHiTwz4D3OvKyC1ySSnfLyQD4RDL0NQgRpr2vo4Zf-_8OAY0XGwUAj8ol849fdbWlWwpz-_A17NJkxf0e5bFGIqzFPYvNY42sa6834T0z342ZfYMFdAiDKcOLUB4xy8_oupc_3Po6u9HQhvSapPZgNSZsIoZdA6uqUGgKMo-nVi3DveDjN-ibOcwzJLAOm4tVIJ5AL140daLkbtNqtyJmf1s3WwpcXUU8SdMdVRk1UbCxOcp_DBbsfLt8rbV6pJqCZLzflFVEjw1s91oXBX_mLbU7ffdjE13mfK9QhMNP8MY0j41Gua-q6uK64vEEq_M887pktN7di0Prv39LXW8HGNd6C_db67A5b4Q5pOj-cD5vABL3-PqWpHEmxqFz1yEg8eBFm4Aqc4TFyHg60YOMqY7YNE334TZw3GCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من محافظة السليمانية بعد الانفجار المجهول</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88088" target="_blank">📅 19:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88087">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c491d94.mp4?token=D3iyORksrviU9lIIfZUN8-RGckk1SFFkgPSl25A5DNKeY0FElZEP3tu1Xj7zS9k88IXMRqGKrKch-JN4HlqstXdFO3xqQDsf-5Dm8Mb7M2wFrzaw5Ylv4i519NDPTCZJzcQf5anVEVuXIzclEiQBuc7d1ChXUoVZY7Cn3Uek8twdffDRJ26NsElc_7NtV2k9WCqg7RjItaGkDkQIPwlKzOyj5YCmj2uTJSTbn0EGEysKe9iuaexePhX1CUgPCHx3_g7h7uJD2E1GM1qFXwjHlJC-jTfYI1mi5zBeSHQLqm6wApWFEPbvhiFVxbF_VdMOfj845BfGOIV6h9i6kC6Hmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c491d94.mp4?token=D3iyORksrviU9lIIfZUN8-RGckk1SFFkgPSl25A5DNKeY0FElZEP3tu1Xj7zS9k88IXMRqGKrKch-JN4HlqstXdFO3xqQDsf-5Dm8Mb7M2wFrzaw5Ylv4i519NDPTCZJzcQf5anVEVuXIzclEiQBuc7d1ChXUoVZY7Cn3Uek8twdffDRJ26NsElc_7NtV2k9WCqg7RjItaGkDkQIPwlKzOyj5YCmj2uTJSTbn0EGEysKe9iuaexePhX1CUgPCHx3_g7h7uJD2E1GM1qFXwjHlJC-jTfYI1mi5zBeSHQLqm6wApWFEPbvhiFVxbF_VdMOfj845BfGOIV6h9i6kC6Hmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من محافظة السليمانية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88087" target="_blank">📅 19:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88086">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوي انفجار يهز محافظة السليمانية شمالي العراق تبعه حريق مجهول</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88086" target="_blank">📅 19:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88085">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوي انفجار يهز محافظة السليمانية شمالي العراق تبعه حريق مجهول</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88085" target="_blank">📅 19:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88084">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-3XSr2tvZ-YXYJWhulV-Srpy30bLPRijqSwKcT7zocwFRAsFuK2flFXf_FDyZFHN9eZueMmP0MFtBFWeb4RjRClUbuOmk_E8HrZg9S6mLJM9iHDmw5pIsj6-NNDY9Qh0tPyHCqQmb0YluApBV4zPcGq-A_TNl6u6_8nLHgqZXmpLrPdh_lP11IIiBAh_0OzTjrqySptinxmW4TbnjGPQ8uInotYMTiykzjj1IDXi8fn4pLX1xTYMwteLO7mlF8rOnd8XiTjZ-ijMKJxVCG9tkJQ2I6h8woijRW94i_7zqZ0rpWZZb_rFLtzjWioYvmJ3qZTsG6XNwWutMcrbCVpew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
منصات مقربة من حركة أنصار الله الأوفياء تدعو لوقفة احتجاجية في بغداد يوم غد ضد الفتنة والدعوات الخارجية التي يفرضها توم بارك حسب تعبيرهم .</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88084" target="_blank">📅 18:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88083">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">واشنطن بوست:
الولايات المتحدة تدرس تقليص وجودها العسكري في الخليج بمجرد انتهاء الحرب</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/88083" target="_blank">📅 18:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88082">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9cf316785.mp4?token=OOHysDt-Lp_cE_b1DVcGGVBF5ee9Z2mVsd88_80JGXvEQCJ1T_HYMMiJMrKcu7r6GNX61Qh_K23CThYZYU88SLAAZqcxUxvoG3iovhV7tbIjVn_RETuIoymj7WKxVeR7n_-GCSeI7Xi4BJI2xjzbOrON35WuF1-7v7sYbtD09jAqgW4AqBAjOsUyTGFYiaQRlyKwQiufqIVqdrV56fQbPrbLkz4fSsD4n-J9zwFj3KIVRl4vravYZW-bA2NPEwV3tyiyv5x2tYOT1Yqbvl0wVis6zsmklC8VLoQad1R-BjQHytCeU_DWPPX0m8r-nBW1uV0A2t2P0VTc1BUJWNhMQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9cf316785.mp4?token=OOHysDt-Lp_cE_b1DVcGGVBF5ee9Z2mVsd88_80JGXvEQCJ1T_HYMMiJMrKcu7r6GNX61Qh_K23CThYZYU88SLAAZqcxUxvoG3iovhV7tbIjVn_RETuIoymj7WKxVeR7n_-GCSeI7Xi4BJI2xjzbOrON35WuF1-7v7sYbtD09jAqgW4AqBAjOsUyTGFYiaQRlyKwQiufqIVqdrV56fQbPrbLkz4fSsD4n-J9zwFj3KIVRl4vravYZW-bA2NPEwV3tyiyv5x2tYOT1Yqbvl0wVis6zsmklC8VLoQad1R-BjQHytCeU_DWPPX0m8r-nBW1uV0A2t2P0VTc1BUJWNhMQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
قوات امنية كبيرة تدخل مدينة سامراء شمالي العراق لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88082" target="_blank">📅 18:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88081">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
خلية الاعلام الامني العراقي:
ما يتم تداوله من قبل البعض أو تضخيم الأجداث بخصوص 30 أيلول هو توصيف غير دقيق ولا يعكس حقيقة المسار الذي تتبناه الدولة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88081" target="_blank">📅 18:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88080">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات عنيفة تسمع بسماء منطقة بر دبي</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88080" target="_blank">📅 18:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88079" target="_blank">📅 18:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88078" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هجوم صاروخي على دبي</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88077" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyzkVAnRm_T0k_W9f7PTLKpr5iNOerNlegzDmgvbgfU4qaIPNx9r0BRdCOVaRlVlkmwWb8OkKwybTUdjoqRdGnaKlCho5W5pxBIneuKyoMwlg_nqvXb_1y3YRmfWMR0Excj2pkZVLRPTw5hwqg6FU3MvTeLxAGtp18tpj8LHTZgv6uj3496y5z8IvfpdMT-O20T2d_XkJIAdyBLETVpQ5vSbYcC8aeQs9_Vj6VFdpgt0RPzEMQkZRZhZYTEYxkqdxeSScPryTxCkPsU1g26GpRVzhXgwl-CgmanUKlT5REEm6_0p1JPJRVz2SRV8OJPKst47vYTwFa1cLks668tXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88076" target="_blank">📅 18:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88075" target="_blank">📅 18:23 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

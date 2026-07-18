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
<img src="https://cdn4.telesco.pe/file/QxZbwXXNeCBFvbuyWenAKyN9JyRxVk26L8PFhBRc-8LpVMUA57E9mORtsWLNoEvF9MRMVKH827V63AGFDexNKslURKAKGvLJoWYErF1NOIiq7-dKzPR6nwFbwzIVJMe1otcqwDPQr7gbUpml3R-g6wi2n4hkjvY1cO6lmdexow2hCeZI_de641Fq-hGck-5wByAA_MHenfzi_XqVyOHHIPTuMOxFZELLAIYu5Fn4kdus7MQ5xLKDWsmkfJFcVd3eEiuuvFi4HX8K0uSJVSuY1Us3NDqfjciUUpzsyG3b6KXIWN4yOu7Lley3PW_M2vPuxAujPIk2kANE53N-Jv_Q_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 00:22:32</div>
<hr>

<div class="tg-post" id="msg-84010">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وول ستريت جورنال عن مسؤولين أميركيين: إيران طوّرت أساليبها لتجاوز منظومات الدفاع الصاروخي الأميركية، وذلك عبر استخدام صواريخ تحلّق بسرعات فائقة للغاية وقادرة على المناورة خلال المرحلة النهائية من مسارها قبل الإصابة. هناك قلق من التحسن الملحوظ في دقة الضربات…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/naya_foriraq/84010" target="_blank">📅 00:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84009">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الله اكبر   إعلام أمريكي ٢٤ جندي أمريكي جريح نتيجة ضربة الأردن ٥ منهم حالتهم موت سريري</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/naya_foriraq/84009" target="_blank">📅 00:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84008">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رستوران آقاى مجيدي در اردن</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/84008" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84007">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQY-oFEv74i7b4bBiDihjfQpMqAP-IkkY2ljNG6Qmah6c8d0ejPr-VOfpGEJOXzfKi3LKhL3sYA2p5LRUJLgM51VvIeH_ht7SoJ2gVOuIT8goeO1OuqKzaY4bJUkI6kCgX4SQ94UbnYtYF6TMH3JID1-o0yvX9knGPq8tjDh4J8nBdXetsM19vifTBvOQo_s0M1r0kr_DoCBhcRhZ4xAf3eWVU-UR7fJql13of4BJ3xOb5ZbQU6YIu3tXC9NC5TU8ttY3z5AQdu4kb0ks64r8-Kz5uLAO2SdbD6XIe9F3DglwkFJAL5sBv1d5OUXE6WuEkZJcECXO5AhyUKFcI9HAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رستوران آقاى مجيدي در اردن</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/naya_foriraq/84007" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84006">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a872fc771.mp4?token=JlEaYmvERz9v-wCKkdfNojJWMyX-IRWU-hjBX8aKIBQoNwCfmrWb09bVIIbikpEhU2AXrIT-14osal1jFSPCljhfLemB8H0lTMjpatmztCmyw0BVejI3WzhhWdJFLX79VP792QCGPVL1hlfH2Rm8PIfE8o_ehrfVTfXZU6OoK1cOE7lZjYAFkWDBIPHNGMQIbB9SEUa97H-Sx_PhWNtAIxIdUNYMoD2REUom9aTyDrMR_dD3UqcSjJw48sfFCedNkQibNy-zfhA7DU7xMVXDdNLeP4a_SoJnV3m8sNyq22ONnp1JayWYcfWPUFyKDVV6iX0C4Wl4bKSE9EkZmpl2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a872fc771.mp4?token=JlEaYmvERz9v-wCKkdfNojJWMyX-IRWU-hjBX8aKIBQoNwCfmrWb09bVIIbikpEhU2AXrIT-14osal1jFSPCljhfLemB8H0lTMjpatmztCmyw0BVejI3WzhhWdJFLX79VP792QCGPVL1hlfH2Rm8PIfE8o_ehrfVTfXZU6OoK1cOE7lZjYAFkWDBIPHNGMQIbB9SEUa97H-Sx_PhWNtAIxIdUNYMoD2REUom9aTyDrMR_dD3UqcSjJw48sfFCedNkQibNy-zfhA7DU7xMVXDdNLeP4a_SoJnV3m8sNyq22ONnp1JayWYcfWPUFyKDVV6iX0C4Wl4bKSE9EkZmpl2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The peoples of the Persian Gulf today.</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/naya_foriraq/84006" target="_blank">📅 00:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84005">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0bf4fa41.mp4?token=amULmUt4cnz0DwCaRlGDkFE31PEQCaLQJpT4LMYEO_GjraGM3SnbbvzZkjKD3n6SQyMPDshedJXs3F9ScZbQoZe1NNjg2Poh9exptFZxgFQcwvCo0wUeho1IbppY1fhWG4cBG-wcM4Rlv4TDGYMpemvNpgd9zJGfdb_XUBH3EjC-uMhz0uV6S8opvdBkRuZaQsHpiHWp961xtznqpt15QLzzSB2Nq7SnzUUsiEY5VvG7eAaYkAvaINKBg_AcFoipls1s4O5SWzhW_4HqgVrlMSifZnYZPuoix4fiiR1M03QJrbJeJLgQcefljFTHvBHzxWXOzuDjil3yeQVfwcTPOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0bf4fa41.mp4?token=amULmUt4cnz0DwCaRlGDkFE31PEQCaLQJpT4LMYEO_GjraGM3SnbbvzZkjKD3n6SQyMPDshedJXs3F9ScZbQoZe1NNjg2Poh9exptFZxgFQcwvCo0wUeho1IbppY1fhWG4cBG-wcM4Rlv4TDGYMpemvNpgd9zJGfdb_XUBH3EjC-uMhz0uV6S8opvdBkRuZaQsHpiHWp961xtznqpt15QLzzSB2Nq7SnzUUsiEY5VvG7eAaYkAvaINKBg_AcFoipls1s4O5SWzhW_4HqgVrlMSifZnYZPuoix4fiiR1M03QJrbJeJLgQcefljFTHvBHzxWXOzuDjil3yeQVfwcTPOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇺🇸
مسؤول في شركة HKN النفطية الاميركية: الشركة قررت إيقاف جميع عملياتها في العراق وإقليم كوردستان، بسبب تصاعد الصراع بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/84005" target="_blank">📅 23:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84004">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
🇺🇸
مسؤول في شركة HKN النفطية الاميركية:
الشركة قررت إيقاف جميع عملياتها في العراق وإقليم كوردستان، بسبب تصاعد الصراع بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/84004" target="_blank">📅 23:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84003">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
‏الخارجية الأميركية تكرر "تحذيراتها الأمنية للأميركيين من اضطرابات في الشرق الأوسط"</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84003" target="_blank">📅 23:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84002">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وول ستريت جورنال عن مسؤولين أميركيين:
إيران طوّرت أساليبها لتجاوز منظومات الدفاع الصاروخي الأميركية، وذلك عبر استخدام صواريخ تحلّق بسرعات فائقة للغاية وقادرة على المناورة خلال المرحلة النهائية من مسارها قبل الإصابة. هناك قلق من التحسن الملحوظ في دقة الضربات الإيرانية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/84002" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84001">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbyAkdgagRQzACaugyGs2-ySwNwPLBt55UHaK9cvhn5r-wCZO_ofNARIpyb5Q2CDSsiFbmcMtb8sH2N8WmMhKi19TZ81lH_xCanMjwP-8kmaZ92AEjEaY_an_0xKzQ8BzUYUkyhMYbjRY8f5Odw1Gfmy_CcAYM4o5Eu5ZE2EoTk5-BmkJwQpXOoaoki1rQyOYfRmx9weilgGbLtIYAnXym0hjwNtrqExgiIEDtigs4Vde_JP0Zt0aPy-BpDUY5QNrZLvrYQ7TzBbGznV9yfhb3hVYIMWRIHztuY5lmhtL4OdyqqoVqkWfG7Re7VnIwE7gzidneYx3IFdHEGHTwGCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام أمريكي : وحدات السكن المُعبأة في حاويات (CHU)، المستخدمة كمساكن لأفراد الخدمة الأمريكية في عدد من القواعد العسكرية الخارجية، بما في ذلك جميع القواعد تقريبًا في الشرق الأوسط، لا توفر حماية تُذكر من الطائرات المُسيّرة، فضلًا عن الصواريخ الباليستية. يشير…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84001" target="_blank">📅 23:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84000">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
🇮🇷
في غضون دقائق قليلة، سيتم نشر رسالة شكر قائد الثورة الإسلامية للشعب العراقي بمناسبة الجنازة المهيبة للإمام المجاهد الشهيد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84000" target="_blank">📅 23:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83999">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
الاصوات المسموعة في بندر عباس ناتجة عن اطلاق الحرس الثوري قذائف تحذيرية للسفن المخالفة لقوانين عبور مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83999" target="_blank">📅 22:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83998">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
تستعد المؤسسات الأمنية الإسرائيلية لاحتمال اندلاع حرب واسعة النطاق وخطيرة في جميع أنحاء المنطقة بأكملها.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/83998" target="_blank">📅 22:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83997">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
🇮🇷
في غضون دقائق قليلة، سيتم نشر رسالة شكر قائد الثورة الإسلامية للشعب العراقي بمناسبة الجنازة المهيبة للإمام المجاهد الشهيد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83997" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83996">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عمليات إخلاء طبي لجرحى او قتلى من الجيش الإمريكي من الكويت باتجاه درمشتاين في المانيا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/83996" target="_blank">📅 22:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83995">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9oH2rchW5adQGS1Dm_inFqfwwjAUppTAIlXRvWV9rLDtwDG0PJHHCII-koPO0YVi986KIJeBZioYH5L0DmhtdrBLYMGg5nqWa5ZaD34CocCW7zlFXso8Oo8iVIvTdRjeJy_o1aPUPwa9J3Ce-3t0zkcj7TYtWNEeak_ZXxOsTZEJXEwtJM46DP9pO8tN7kg0H7oAYunLISC18F4fzvKnWoham0ouUutS51fGb9WKYXSygrZBCQW_JYAuG3gjcINoXsSsdtPIz6YzBRhr47CkCUVDmZdo9WPREqUPmiKp6kmpmmAoTM03bQ9nFJYS8o7Iet1QjggOWyQtxak_O-04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏القيادة المركزية الاميركية: قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.  ‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83995" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83994">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇷
مصادر إيرانية تنفي وقوع اي انفجار في سيريك</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/83994" target="_blank">📅 22:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83993">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الاعلام الاميركي:
16 عسكريا أمريكيا قتلوا وأصيب أكثر من 430 آخرين منذ اندلاع الحرب مع إيران في فبراير الماضي.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83993" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83992">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔻
اهلنا شعبنا المسلم في الكويت
حسب المعلومات المتوفرة لدينا في حال استخدام الجيش الامريكى أراضيكم مجددا لغرض الاعتداء على الجمهورية الإسلامية فان الحرس الثوري سوف يرد بموجات عنيفة لن تكون بها مصافي النفط و الماء بمأمن بمعنى آخر سوف يتعرض هذا البلد المسلم لدمار شامل ننصحكم بالتنقل فورا عبر الطرق البرية الآمنة بواسطة العجلات  " طريق الخفجي ، منفذ النويصيب ، حفر الباطن منفذ السالمي " لا تنسوا ان تحملوا معكم مواد غذائية جافة بطاريات سريعة الشحن ومياه نظيفة للشرب انفذوا بجلدكم .</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/83992" target="_blank">📅 22:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83991">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6808cb44.mp4?token=t4CL4UgrPOGNu4IIbYrxgi8wGOMw7kADZWIhh_YAuD1zrSQTwI5oqJIbKduZ1BNk14hKjprmcKfJZlDLvGw8Jpr4ZjUyiZce-vHaok4fBgSzD2UgVK2eX3Hwq7klHpKkqwsxUdwF5FlJ4O7rKgBFeC2DC5AnVGNj3CotzYyB1ePWmmmsXlBh5xan5UHx09zenZTuFfYCRps-miZ3Qz3Q1cbdtBHNXDMx_9_yi7zr8nQp6xqFSiWKPJHUbG-E2tstmK7KSjbdaQAFrQ-u-xen9rXkm96MayMewoNM6LzHRXB-Wfz4ENdmXbUxUY_QJ02iMF-iJBg1NIQqHJbyWrSVUAFcBu1Xf7CnwoaGar9J3Oj6UriqoAMDMXsqL-x4AWNAlIXR-1NUzQioYN00O8hBFy2DSnQzNIETrQ7YJjnk8ykhuv8vnJpfCfvAutYHBygoG2qmcd8FdV6qwPSabf6Qo0K_1cWzPYLBP3VPkNWup3mkSv9veu0NhrA5IkhBNoWPzsh_7bZLb_U8yxjCJPhR4UVk339tQLovyBYZfeE-G8zzUEZY1CS6Xo6H61cZe_s5UThxizhfyBhpV5s69TcOEOqqTD1VGRuDv3AkjVpTfIYlA3xwHktGeUW6OBBx5QAK8EuDzvxHljY6b4Q9IfdYieikD0uTjKWCyg2TsBPWbPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6808cb44.mp4?token=t4CL4UgrPOGNu4IIbYrxgi8wGOMw7kADZWIhh_YAuD1zrSQTwI5oqJIbKduZ1BNk14hKjprmcKfJZlDLvGw8Jpr4ZjUyiZce-vHaok4fBgSzD2UgVK2eX3Hwq7klHpKkqwsxUdwF5FlJ4O7rKgBFeC2DC5AnVGNj3CotzYyB1ePWmmmsXlBh5xan5UHx09zenZTuFfYCRps-miZ3Qz3Q1cbdtBHNXDMx_9_yi7zr8nQp6xqFSiWKPJHUbG-E2tstmK7KSjbdaQAFrQ-u-xen9rXkm96MayMewoNM6LzHRXB-Wfz4ENdmXbUxUY_QJ02iMF-iJBg1NIQqHJbyWrSVUAFcBu1Xf7CnwoaGar9J3Oj6UriqoAMDMXsqL-x4AWNAlIXR-1NUzQioYN00O8hBFy2DSnQzNIETrQ7YJjnk8ykhuv8vnJpfCfvAutYHBygoG2qmcd8FdV6qwPSabf6Qo0K_1cWzPYLBP3VPkNWup3mkSv9veu0NhrA5IkhBNoWPzsh_7bZLb_U8yxjCJPhR4UVk339tQLovyBYZfeE-G8zzUEZY1CS6Xo6H61cZe_s5UThxizhfyBhpV5s69TcOEOqqTD1VGRuDv3AkjVpTfIYlA3xwHktGeUW6OBBx5QAK8EuDzvxHljY6b4Q9IfdYieikD0uTjKWCyg2TsBPWbPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحمدالله كادر القناة يشجع رونالدو
😆
سييييييييييي</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/83991" target="_blank">📅 21:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83990">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e223e42f10.mp4?token=XFT0495-Q1gZyYiHioETHuMRKh_J6PkNpTPbXMyuLF72r8zYxqWCcyDQnVPd4lFRpJWWhro4PYh49EfDNTmhh0Lrxj4wJDhugbt43f8fPzhFyTZEsx0Ct6GhIXvSYLNmA7w3Vu2TygxiqwEfoAp7zLnAqM5ksMzEhHqSSnaNn-OcpTahzuPQMxF7ejf5T-BZzKRPEwP_Jbfcc1dFUQu0glBK0bbV5qgRYIzsYK5a-1e8k3cas1oY-zwPGUuZZfU8XAmIBbC592cvV-FBhrm8lfuEnfi6OlsriEA9gSME7ytXXwSYQ2dAY2UTpZ4KA7AOboblGu6ugr8VlybnDrl7iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e223e42f10.mp4?token=XFT0495-Q1gZyYiHioETHuMRKh_J6PkNpTPbXMyuLF72r8zYxqWCcyDQnVPd4lFRpJWWhro4PYh49EfDNTmhh0Lrxj4wJDhugbt43f8fPzhFyTZEsx0Ct6GhIXvSYLNmA7w3Vu2TygxiqwEfoAp7zLnAqM5ksMzEhHqSSnaNn-OcpTahzuPQMxF7ejf5T-BZzKRPEwP_Jbfcc1dFUQu0glBK0bbV5qgRYIzsYK5a-1e8k3cas1oY-zwPGUuZZfU8XAmIBbC592cvV-FBhrm8lfuEnfi6OlsriEA9gSME7ytXXwSYQ2dAY2UTpZ4KA7AOboblGu6ugr8VlybnDrl7iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يقول طيار سابق في سلاح الجو الأمريكي، مقرب من القيادة المركزية الأمريكية، إن ما لا يقل عن 3 إلى 5 جنود آخرين على متن طائرات الإخلاء الطبي "لن ينجوا على الأرجح". وهناك أيضاً 15 جندياً آخرين مصابين بجروح خطيرة تهدد حياتهم، ولا يزال مصيرهم مجهولاً.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/83990" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83989">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui-af23-DcR3h3IgxBB1AnPL_9hS7tTOtBXamP7GDqKnv4uuDsblWnU_Ycod2xUWGdSmFtTo9LVpdf5tFS7WxAfc_2l-_d2KvuLPGN9iWyntnH1NB-aO85GIEEl8q-oDUqSUAKiEVheRDWlvkdBXCEX336zBBW-BA3yuml6QeW6_IFSs0nOuyGuEziLh__Ye9lwIF-nGs3JEKz4VO-Z4F8NOyn7P_FKyCa33SUlOcmk46so6T047WP5vRJGin7RHRQ1ZWXZjdl6RewiNc68n2bT6eOTA6f8UZR3NQxaxYqeHY1TNP028WhKDuZfUOVJ6vK0cXgt_08W3Qsxvafi--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يقول طيار سابق في سلاح الجو الأمريكي، مقرب من القيادة المركزية الأمريكية، إن ما لا يقل عن 3 إلى 5 جنود آخرين على متن طائرات الإخلاء الطبي "لن ينجوا على الأرجح". وهناك أيضاً 15 جندياً آخرين مصابين بجروح خطيرة تهدد حياتهم، ولا يزال مصيرهم مجهولاً.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/83989" target="_blank">📅 21:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83988">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a333c8aa85.mp4?token=ozA_Oaf-gnqbhMaEQgj9j9t-ALBOIMics3Qs-1eMIeBL0nfhZpQEwfYzciUxtI8PQ26hU9HG4QAaHyyhVql3iUaIb5Awo9l7Ga_Gxgc4t-lffbPyz_SRlWHnVjCseyPQlbHqpPdY1oKtV6yQIB9fJpeHZjDVkdY5miTm9yFNA3GyKChdmioeVlZDSWP9nHHy1czvTCWF63uynvNSnWtueBTsadorAAQniZzDK1_Jvpy0FrkknX4ZeubQPJPFSWFsVDKF461Ukbeq5-cnWJw-Jm5XK6HvfdhZ8vnovkUJW2TvIWAlcId0F7CQVH-gBChBRQX1qsGUwfHvtVOils8UOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a333c8aa85.mp4?token=ozA_Oaf-gnqbhMaEQgj9j9t-ALBOIMics3Qs-1eMIeBL0nfhZpQEwfYzciUxtI8PQ26hU9HG4QAaHyyhVql3iUaIb5Awo9l7Ga_Gxgc4t-lffbPyz_SRlWHnVjCseyPQlbHqpPdY1oKtV6yQIB9fJpeHZjDVkdY5miTm9yFNA3GyKChdmioeVlZDSWP9nHHy1czvTCWF63uynvNSnWtueBTsadorAAQniZzDK1_Jvpy0FrkknX4ZeubQPJPFSWFsVDKF461Ukbeq5-cnWJw-Jm5XK6HvfdhZ8vnovkUJW2TvIWAlcId0F7CQVH-gBChBRQX1qsGUwfHvtVOils8UOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لقطات حصرية جيش الاحتلال الأميركي يطلق وابلاً من الصواريخ من الأراضي الكويتية باتجاه إيران خلال عملياته الاخيره.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83988" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83987">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYIrQZZoXAQnMALIF0CHxZvscpRCzu-mEeiBeyUO2AQiX3_6yctkvKh7Dcf_QQu8XT3FAgnVcFJNdrj9gG6qy1KPDmI_zT5LqluDyJ1t77FCK1MkbyxTRG40K4QUXr4fInmrHtY5BN9Ggd7HPA9njObV5poRpR_f9r9TG2uJvkeyaJsIqLHFXUxxdhqKvcfnodPaof2FkZ6uj85GGZpPtkZDWl9PKWKNvU4lWUCxOUhkTFosQM1yIHbrTMGWWxfJ0Hty5hKIZz47Fy7MDuUkNmPlkORWXeeDaqXOm7W4CPUeZ5N7UbLYk9vj1iBk3e4yOxmr01-x2NrPmk9CFgZJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام أمريكي :
وحدات السكن المُعبأة في حاويات (CHU)، المستخدمة كمساكن لأفراد الخدمة الأمريكية في عدد من القواعد العسكرية الخارجية، بما في ذلك جميع القواعد تقريبًا في الشرق الأوسط، لا توفر حماية تُذكر من الطائرات المُسيّرة، فضلًا عن الصواريخ الباليستية. يشير مقتل هؤلاء الجنود داخل وحداتهم السكنية المُعبأة في حاويات إلى عدم إطلاق الإنذار، أو عدم امتلاكهم الوقت الكافي للوصول إلى الملاجئ المُخصصة في قاعدة موراي البحرية الجوية (MSAB).</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/83987" target="_blank">📅 21:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83986">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc325e131.mp4?token=bj7Vipqhr_gaDia6UM7ZY__SZEYFfPEK7tcM-DbdeEuD64rHU4sAUIbM2wCLnthYyVIx7geyIWYV0JeDAcL4LbSnrIO16LoJ-6bxjCEcSsUNwH4EuXFDCIEghIDMOGGog0CetDaCV4vWeK2kBswosLHpnSu8Rxg-vSUqeFkT-d5dRYU0hoABPoIn24JeWpK9RVVnxDnN40_YVvMwDxIoq0Stqnlu7dgtljum6soL0RIxkGo0RKFDydWPu5hqM2ig1Pu7o5ZeWNqEu-JG_zKcBLvfZ0IHP4KiSrI3GCjdmLWhBDfSIU3YJjiM0N_7DenBRst-k2s5juoibzgpZCX2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc325e131.mp4?token=bj7Vipqhr_gaDia6UM7ZY__SZEYFfPEK7tcM-DbdeEuD64rHU4sAUIbM2wCLnthYyVIx7geyIWYV0JeDAcL4LbSnrIO16LoJ-6bxjCEcSsUNwH4EuXFDCIEghIDMOGGog0CetDaCV4vWeK2kBswosLHpnSu8Rxg-vSUqeFkT-d5dRYU0hoABPoIn24JeWpK9RVVnxDnN40_YVvMwDxIoq0Stqnlu7dgtljum6soL0RIxkGo0RKFDydWPu5hqM2ig1Pu7o5ZeWNqEu-JG_zKcBLvfZ0IHP4KiSrI3GCjdmLWhBDfSIU3YJjiM0N_7DenBRst-k2s5juoibzgpZCX2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏القيادة المركزية الاميركية: قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.  ‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83986" target="_blank">📅 21:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83985">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83985" target="_blank">📅 21:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83984">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2fceb3f2.mp4?token=b5dDPvdQ9Lzc-e_JMBUvCReT6KQQeatU63D4RyIy_aYk2XS5r8Lzb9ZzI_vJww2_6NTE3NXguMxsVpXoI7MC5UBCoGU7Av5d7qLkYNaRiHDlzVaDNU6M2zOrKT4Xv0Mxoz2qdPZWMsgI1Ys-fuSpVuXTqIuQhY8FPdmW0wQ_aJrNYVhYld5OLDrBwn_MuLdVhTQ1SbuDYA7F5NiwhIbzjBEIlSx-ddB5jF3bSaMYERMyHysv2c_wNU5wMEjSB0VaQIpyVpLqAvUbE2QFf6QpIqUdD41em8iRQIO6VgnmQuwnNRrufUmmTn2U0I92ekLX9TiVK-pvZgkiyD97X4cv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2fceb3f2.mp4?token=b5dDPvdQ9Lzc-e_JMBUvCReT6KQQeatU63D4RyIy_aYk2XS5r8Lzb9ZzI_vJww2_6NTE3NXguMxsVpXoI7MC5UBCoGU7Av5d7qLkYNaRiHDlzVaDNU6M2zOrKT4Xv0Mxoz2qdPZWMsgI1Ys-fuSpVuXTqIuQhY8FPdmW0wQ_aJrNYVhYld5OLDrBwn_MuLdVhTQ1SbuDYA7F5NiwhIbzjBEIlSx-ddB5jF3bSaMYERMyHysv2c_wNU5wMEjSB0VaQIpyVpLqAvUbE2QFf6QpIqUdD41em8iRQIO6VgnmQuwnNRrufUmmTn2U0I92ekLX9TiVK-pvZgkiyD97X4cv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لقطات تظهر حجم الدمار الشامل في دويلة البحرين نتيجة الهجمات الصاروخية الإيرانية على مجمع استجمام يرتاده الجنود الأمريكان في ضاحية السيف</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/83984" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83983">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYauBM5wLu6Fscj4sIIFCRTqHmAGynAxZ5AiANhrEU5GqGtGtVXcMqsadFQDWqBJCBGpmlG1hofTwfbDP99Lg85Auz6_CaspUhMBIDT6ReARNix46ozYwg-O5ia-p6GenM6OJGbrfeOQncTmSneMUMVSulMTPbg0mARQssBup8jYJJwmGSIn5CkVTLeSkGwROJi_xR-AuATpZJUyMsdgc9l5liC5YQP_qxFT9ZdLSM-9H3OysRvFNPCwJSzhlw7uRbeiB1og1BidsZ8BUm37T6Zp2fG_3MedZdWblNBOyUnHabRUfkgObReOZDnynWpwrg2MjMkTxVJarwJAvLIhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏القيادة المركزية الاميركية: قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.  ‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83983" target="_blank">📅 21:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83982">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الله أكبر  من الهجوم الصاروخي العنيف الذي دك القاعدة الأمريكية في الأردن وسط فشل تام لمنظومة الباتريوت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83982" target="_blank">📅 20:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83981">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/83981" target="_blank">📅 20:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83980">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/83980" target="_blank">📅 20:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83979">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
‏
القيادة المركزية الاميركية:
قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.
‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى مستشفيات أردنية، وقد غادروها لاحقاً. أما الأفراد الآخرون الذين خضعوا لفحوصات طبية لإصابات طفيفة فقد عادوا إلى الخدمة.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/83979" target="_blank">📅 20:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83978">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">البحرية البريطانية: تلقت بلاغا بتعرض سفينة تجارية وعسكرية في خليج عمان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/83978" target="_blank">📅 20:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83977">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">البحرية البريطانية:
تلقت بلاغا بتعرض سفينة تجارية وعسكرية في خليج عمان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/83977" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83976">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3243f8579.mp4?token=aHYSBlJ5eUu8IPdT5-lcGKQmDlT9gYa7kdi1brgDP8SJccpTj6pb5qOzdauxRj7DwtWzeBos5yOodcOJZHRE03LYIoQxVqGAEBpSK0i_ChNj0XEBT1TPB0QbrQRBoiNiqZGbu14urnBSAme1rW-vj-svYEqc5-I0y4Qsf3iIjNi3itfuDNq_K-tjaP6bbyeSgN1sMnnjm0TlJ1gkBOgj6mxTcAdba5NyLW0aaLQUj8BuAivHJh0ePYN2QE3CuOG_qrLmsjEPjP-gIkaVzY2VzERZ7HFynFJQtUbk3y4SCqUphejhgZf-rUS76-TK_OgURQvQYoIyiD5VUTfVvsy1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3243f8579.mp4?token=aHYSBlJ5eUu8IPdT5-lcGKQmDlT9gYa7kdi1brgDP8SJccpTj6pb5qOzdauxRj7DwtWzeBos5yOodcOJZHRE03LYIoQxVqGAEBpSK0i_ChNj0XEBT1TPB0QbrQRBoiNiqZGbu14urnBSAme1rW-vj-svYEqc5-I0y4Qsf3iIjNi3itfuDNq_K-tjaP6bbyeSgN1sMnnjm0TlJ1gkBOgj6mxTcAdba5NyLW0aaLQUj8BuAivHJh0ePYN2QE3CuOG_qrLmsjEPjP-gIkaVzY2VzERZ7HFynFJQtUbk3y4SCqUphejhgZf-rUS76-TK_OgURQvQYoIyiD5VUTfVvsy1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بث مواطن اردني مقطع فديو اظهر فيه الصواريخ الإيراني وهي تتوجه نحو القواعد العسكرية الأميركية في الأردن ..</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/83976" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83975">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
بيان مرتقب لقائد الثورة الإسلامية السيد مجتبى الخامنئي حول التطورات الأخيرة.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/83975" target="_blank">📅 20:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83974">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZrb5jp6cDcZKmzXF6q8SiX1YJ2GvO8J7y78a6YG4_nifDlSFsuh9pYtrUePmWGyD998PwwbXD0nfhTGUFJm7IUOQZIMhXicHGyjWpVcxFtliHK06tCAIt184ELM8HqqqgAxI7nqr16lhb90ICPxPU3ONkLd7v_JZtSLnHRO_LSD6DFVYHGRTZiUot3EcBsq9dB_pW_FoMsBfM8zq1IaIRaoNEUK4WlJ1GxexIV9x8RFRfxoivo0v_DWFFD1vJUnPUP7wPJHQ5OZOSE18nKibfMTKDiyrBNiPVfXl7vxgGcat_W3s7O_fAWcy5nD80_PfgPYUZ2UzsVhSoVCCFfb4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇮🇷
عقد القنصل العام لروسيا في البصرة أندريه كالينين لقاء مع نظيره الإيراني علي عابدي
وشهد اللقاء تبادلا معمقا لوجهات النظر حول عدد من القضايا ذات الاهتمام المشترك، حيث ناقش الجانبان الأوضاع في الخليج الفارسي وانعكاساتها على دول المنطقة، كما تطرقا إلى سبل تعزيز التعاون العملي بين البلدين وتوطيد العلاقات الروسية الإيرانية بشكل عام.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/83974" target="_blank">📅 19:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83973">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
🇺🇸
**نماذج من جرائم الحرب الأميركية في الهجمات الجوية على جنوب إيران خلال ١٠ أيام **
>> تمثل هذه القائمة جزءًا من جرائم الحرب التي ارتكبتها الولايات المتحدة منذ 17 تير في المحافظات الجنوبية من إيران، وتشمل:
>>
▫️
استهداف البنى التحتية للمياه والمنشآت الحيوية.
>>
▫️
استهداف البنى التحتية للنقل المدني (الجسور، وخطوط السكك الحديدية، والمطارات).
>>
▫️
استهداف البنى التحتية للموانئ، والمنشآت البحرية، وقطاع الثروة السمكية.
>>
▫️
استهداف منشآت حماية البيئة.
>>
▫️
الإضرار بمستشفى الأطفال في الأهواز.
>>
▫️
استهداف المدنيين.
>>
▫️
استهداف البنى التحتية للاتصالات والبث الإذاعي.
>>
▫️
استهداف المصانع والمنشآت الصناعية.
>>
▫️
استهداف البنى التحتية النفطية.
>>
▫️
استهداف البنى التحتية للأرصاد الجوية.
>>
▫️
استهداف المباني الإدارية المدنية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/83973" target="_blank">📅 19:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83972">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
ندعو الشعب المسلم في الكويت بالذهاب لمراكز التسوق وتخزين الطعام والمياه وشراء كميات كبيرة منها قبل فوات الأوان او الذهاب والسفر خارج الكويت قدر المستطاع ..
الليلة لن تكون سارة مطلقا لبلد تحول لقاعدة أمريكية يعتدى منه على دول الجوار ؛ قد تكون أقسى ليلة على الكويت ابتعدوا عن تواجد الأمريكان في بلدكم</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/83972" target="_blank">📅 19:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83971">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
بيان مرتقب لقائد الثورة الإسلامية السيد مجتبى الخامنئي حول التطورات الأخيرة.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83971" target="_blank">📅 19:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83970">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHh52vIVdIDUzuPOJdlaeSRdaSJdLlWBRI6C3TcrV5wq42lxbN5Sy93k71MXCrl-9WFvwLAV_uR3DRhstOVL1_whK-a7NUkOMJ9irTXkQGSnpxSTTUb9zTBRSbGgdbxWHTEyOWURKEbaPrVPPt2xS_I0vofl-VQ9kyed-80-bampzrogNMPc_wDdPDPe9p4DOZ5nMiSKI4xmob7cvimRoZuMI1WwMd4Ov9Zt3ocd25lF0XiJUZ50JGK7Et5XXJqGBo66BQiTJ5_nfs1vzqMTypIL-bST4U3rZOSHsasm3-5GWw5BJU9Vw3UFaaTDfKX00UA6btj09_z7beKv01QpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السعودية تدين العدوان ع الأردن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/83970" target="_blank">📅 19:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83969">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الكويت تعترف:
السيطرة على حريقين اندلعا بموقعين مختلفين بالبلاد بعد ضربهما بالصواريخ الايرانية</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/83969" target="_blank">📅 19:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83968">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مواطنون من الكويت يدعون لجعل الدوام الرسمي من المنزل بسبب الوضع الأمني المتأزم ..</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/83968" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83967">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ab3c3911.mp4?token=owTyh9S1-zXlDZKFBpz8JgrCHM0Qfm6l0FxclenYeBYo3gedVryfC5fpi8LHekSTzUQrfAQlMtowQ9FMLPzIiKtrHrhPc2_u7qVRwnpeLuotDmUhHcxjxRxjs24RxJhsTJGSNorGg7VlwENwdoG7FaRsl1Vq_DdnSDtzbYj9VVsdcnZbJigx70RnCaBFOFfnknAvCZVbR17jhrcCZxHx2Dg-KHHCBproxCFLv5Qemvg8PmZs7uzVIBeFRuQZ0fCw1iH2nt-3IAYsfMIBnclJCLzQHNjmbPgKQNuDMJ5p-6c1jFfNqD_yVkZk_fTtfxBEDrWc7LUpFjgLxBd2OXqTEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ab3c3911.mp4?token=owTyh9S1-zXlDZKFBpz8JgrCHM0Qfm6l0FxclenYeBYo3gedVryfC5fpi8LHekSTzUQrfAQlMtowQ9FMLPzIiKtrHrhPc2_u7qVRwnpeLuotDmUhHcxjxRxjs24RxJhsTJGSNorGg7VlwENwdoG7FaRsl1Vq_DdnSDtzbYj9VVsdcnZbJigx70RnCaBFOFfnknAvCZVbR17jhrcCZxHx2Dg-KHHCBproxCFLv5Qemvg8PmZs7uzVIBeFRuQZ0fCw1iH2nt-3IAYsfMIBnclJCLzQHNjmbPgKQNuDMJ5p-6c1jFfNqD_yVkZk_fTtfxBEDrWc7LUpFjgLxBd2OXqTEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد ان فشلت المنظومات الأمريكية في التصدي للصواريخ الإيرانية   الكويتين يطلقون حملة طف الضوء ..</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/83967" target="_blank">📅 18:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83966">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnztDoM9Ksluqp7RNrE5fJ3RwP4865T0EX842AcWyFPICG1EUFvA4boVTR3rkSKUk8hGBarg7czoFEwI7eUH6FTaSAz2gGq0NAkUUGi22YVC59RcVKKWWxf72Yd0G4XH8Zcnc5pKv94XfN_jQ4KRk_L8ZxNHWS4FRpbIreUPVE4PzVOX6-jBddI2JMgjzkUADhZlfemRBItMUHQ2xjzfiF7QaDjLhsxkSMQcxp5w2oBEVAYxv6SClLRkb2BQjoEp47jxAqAlSOUi30AL9F_LqFXnqkJvXRhqED40pZTT3X1OtiQT9EXOBayAFjnUJFNK91jGhNvXp-ECFgjSa8wAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد ان فشلت المنظومات الأمريكية في التصدي للصواريخ الإيرانية
الكويتين يطلقون حملة طف الضوء ..</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/83966" target="_blank">📅 18:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83965">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmGXKXN8PaRLAhvjMYd21YnblDNHQMBltoOhTS_pvOXRjvTjRC9PJBaf-3JvFguZYzptBg37_YIEizyKcWIGzderRSaBzx3HZjheocVR1wylWjdnwHMCCHY8d--0ixt1pQ9JNNkr6Yp31skcN73KlhxIPkuk2wIhox5Au1phLIHyLgk2EWg5TZgDGqehkqi-i4TfDRo7y3Bgp_uQrWnC3a6GEp-B3_SQDBwwmrT1PVJb3G9_jSk4vFvMuTiOGv4e87sQCpe9GnLpx8fZomM3ns0eht_8y62dEvBvYBgvoms4XDOU_0ljkXVAW1LUUNPFRcyIuTrigT_2BqZ7u31VOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
فدای یک تار مویت حاج رمضان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/83965" target="_blank">📅 18:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83964">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWHdwDMG7nHf7aToc3SF2AWr4kKWQOB7n4qUfgOCsIklV2aO7qIAvvBJIx0Nw0-flp7kLa6X6ZdX6g13SH3ZLUiU4Qr45nMPD3bafTRVKn3Rw9Wz47ETOJ3tCLLYQ4nCXSSTDHoe3gHu1SvWBL7inh5NUuFrCIZe1S2CHLovD72c6F9Rckitgyxu6nm3KfNW1DzR1ayifvLWa4O646Ly606EcwkwOzh5nNE3cTSmY53tvMR964ppId125J964wBRwi2vkNtCrDfb11IJNGvTVf0gV7Bn4Vbu4XHiBwYGj_iqtyTB6jlk57EodJfGza8Dw5eshNxJfHXexJDQBH8CQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مواطنون من الكويت يدعون لجعل الدوام الرسمي من المنزل بسبب الوضع الأمني المتأزم ..</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/83964" target="_blank">📅 18:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83963">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔻
مصدر لنايا:
3 اسعافات عسكرية تتجه الى قاعدة عيسى الجوية في البحرين.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/83963" target="_blank">📅 17:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83962">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
مسؤول رفيع المستوى في القوات المسلحة الايرانية:
إذا هاجمت الولايات المتحدة الليلة البنية التحتية المدنية في البلاد، يجب إخلاء مطارات دبي وأبوظبي، بالإضافة إلى موانئ الفجيرة وجبل علي على الفور.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/83962" target="_blank">📅 17:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83961">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اعلام سعودي:
الحوثيون متورطون باختطاف ناقلة المواد الكيميائية ASANA في خليج عدن عبر مسلحين صوماليين.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/naya_foriraq/83961" target="_blank">📅 16:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83960">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
🇺🇸
‏الجمهورية الاسلامية الايرانية تعلن تعليق العمل بكل التزامات مذكرة التفاهم مع الولايات المتحدة الامريكية.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/naya_foriraq/83960" target="_blank">📅 16:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83959">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6032498f26.mp4?token=SNUOt5pLYlasjUmXau9jR9s52KiLPbyjVdz7gxQQO-LOsVWSFMlInCLpHrTzHDD__BbsSYvbg2Z7VLK6E_v2SYL-zUNM03onSi15u-ioZyLUqLPBil7pjNBV0hzQ0DIK2_iDxFz45J66x9L-6ReJGVJfrAQkmXjSgNW1NWZx5DttOuUpu9JLUQ4AOwm01abzrvge7EHb_FNjp5a-QVXQbhVAyC74nl-ItrhKsBPu1vBkoA66Q6odcvtqMjLx91iShlODTevCo9f-is5_Xx-RqgX3vVzT_GdXYEQXfMJWTfCE7__ygrEP77fW6XU7qYPM5Y7XwFt17moPULsdhkaTVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6032498f26.mp4?token=SNUOt5pLYlasjUmXau9jR9s52KiLPbyjVdz7gxQQO-LOsVWSFMlInCLpHrTzHDD__BbsSYvbg2Z7VLK6E_v2SYL-zUNM03onSi15u-ioZyLUqLPBil7pjNBV0hzQ0DIK2_iDxFz45J66x9L-6ReJGVJfrAQkmXjSgNW1NWZx5DttOuUpu9JLUQ4AOwm01abzrvge7EHb_FNjp5a-QVXQbhVAyC74nl-ItrhKsBPu1vBkoA66Q6odcvtqMjLx91iShlODTevCo9f-is5_Xx-RqgX3vVzT_GdXYEQXfMJWTfCE7__ygrEP77fW6XU7qYPM5Y7XwFt17moPULsdhkaTVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات هروب جماعية وأزدحام غير مسبوق من مطار الكويت  بسبب القصف الإيراني ، المطار يعاني عملية تغير في الوقت بسبب صعوبة الطيران في الأجواء الكويتية..</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/83959" target="_blank">📅 16:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83958">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XANy9mv24ZMqlmRxqZkFRF4sZiOMx65bG2pPUE0XTH1ADWH6tnBvqhFUeoEm3Jv-dJoYoeNQ55owAL7kbSqujKyNA0NDXkpTEoATgYcOTf022ZhzazS_ckYJr6jeGu7Y0Jdtvm6oHhT1v0LCCx7vIyyHbUR4Te6VLaZ7LH2UIURto8ePm9WPEwU_UeZXyCcpgxAK0Hlgeti_sU291qjiGoJZYF8mlwNEflxwIOhRi78kX755KB8rypSFB6AbUOPtW47cXDaqrVtsC0raik9Ioa7pEdSXmZxGKppmNnIDGTLWTEDpyWsdyilbf_K2l8V3wlYof3yIjP0C4z0kriZFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد فشل اداء منظومة الباترويت الامريكية امام الصواريخ الإيرانية
الكويت تفعل منظومة لا تصور " فضحتونة "</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/83958" target="_blank">📅 16:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83956">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a56b067435.mp4?token=bCghd5IamV0krWNmrrRBlqs_U44owSWqxgBwQ5jTctG-3yTwPqEhK1YeH1leXmPPVa-jtvs55yPcXIIzNvYEU29UOfGC0sDBYOV07dhdb-6_GtD4P8gXQpSwxhUQUyw1erJRsEeNQlkMkUrPdGAGktZkp1qh-dYghnIQkY9ehpFgxvrteZkcXhBRlPipN6yhm6D8S89sPLP9z7pqU5X2wZeYDU6LIqL0PcieGs8UfYYUDZ4vDRkNNnwOF4O4h_aHdsfZsJgXB979oz4BGAH5Stipye5hDEyhKkbCp--Z1T4dFrXDHiB4zAgxzReMLavOPkycOTou5NB6eDk2ilJ0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a56b067435.mp4?token=bCghd5IamV0krWNmrrRBlqs_U44owSWqxgBwQ5jTctG-3yTwPqEhK1YeH1leXmPPVa-jtvs55yPcXIIzNvYEU29UOfGC0sDBYOV07dhdb-6_GtD4P8gXQpSwxhUQUyw1erJRsEeNQlkMkUrPdGAGktZkp1qh-dYghnIQkY9ehpFgxvrteZkcXhBRlPipN6yhm6D8S89sPLP9z7pqU5X2wZeYDU6LIqL0PcieGs8UfYYUDZ4vDRkNNnwOF4O4h_aHdsfZsJgXB979oz4BGAH5Stipye5hDEyhKkbCp--Z1T4dFrXDHiB4zAgxzReMLavOPkycOTou5NB6eDk2ilJ0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الهجوم الايراني الذي استهدف مواقع المعارضة الكردية الايرانية في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/83956" target="_blank">📅 16:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83955">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff89045e5.mp4?token=q8EH9mprdMMt-320ywZk80I3YmeqFFUoDh36nm1Z2tPloP43BfXbkwjlN8Xh3MaKEvPY6JRz5bmitrjZD12VBT0S26lhqo06SzR5KsCGYbqWKst8FTdBfJ3Am-fagkLxz9mvw64yKZK4aWup2VtCkR_6XIqfA-WrPpd1pMZJUnP2WB_7f7Cvqjz92FS6KtNdznsRETQYUqvql7PPz3bG_kEQCu9fbPFVZdGyvEGDFlwtJNHX3spdbCjyF_HlANhtO4IFi82iaZDCYJ0s76AZqmvRduVBrvz4DHZs3KCbq2BPbmIOztvK92E5CrhsYePWht_kCaBWvvrkJfXZnggm3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff89045e5.mp4?token=q8EH9mprdMMt-320ywZk80I3YmeqFFUoDh36nm1Z2tPloP43BfXbkwjlN8Xh3MaKEvPY6JRz5bmitrjZD12VBT0S26lhqo06SzR5KsCGYbqWKst8FTdBfJ3Am-fagkLxz9mvw64yKZK4aWup2VtCkR_6XIqfA-WrPpd1pMZJUnP2WB_7f7Cvqjz92FS6KtNdznsRETQYUqvql7PPz3bG_kEQCu9fbPFVZdGyvEGDFlwtJNHX3spdbCjyF_HlANhtO4IFi82iaZDCYJ0s76AZqmvRduVBrvz4DHZs3KCbq2BPbmIOztvK92E5CrhsYePWht_kCaBWvvrkJfXZnggm3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع أعمدة الدخان من مقرات المعارضة الإيرانية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/83955" target="_blank">📅 16:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83953">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcWUpMOBX8Kc7q7n9iIK78H1eyIHBGgxK2vchfhIujpZmTH8pdT4OZrLcM1rIE5YcrqmtKitsONC7Nz0Gjq28ND2ZlHDNRkrvCmmWkOskaOiaF-VQMf83NsyCNYHyAkYW5_QomlIkYSykGRL8Jm41T6CQLQElk7sYROq3KoqAhNSKopHX2MMxKfvyNflj8z459BS1GuBd5p29UoV_uWr0rNO31_DaotDbNUZ_aZxeekJ9SFP6_xtRzLOEP2l_N7c1tscXZmTFwfXF5bJKZVdp9Z5xSrf6Ln0kKCAgUf_aHMKuUrSwm5fsff1Hh3aZ9lFfor-KQgJVbjYWFp8YyTGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc714b302c.mp4?token=W6nO5F3Hpli7aBVHE-pWXwx4bHKFQcQgJtRlaHL2dQwR31WvmvQsH-Nvtlt50kuNppj6qVPmpfWT_eUbEOI33nbHimdeU6aoXb0fz31UTEXSBi9W04EFtfJMm7Sa2Jh3Duhdx7XkRWd8TE-CnP-mbrnBnXkhKR0tP3BI4R5K0otJ6t6dKBj21NfnKISRFnAzDMad2d23XXLF7E5-oDI_33Ux5Bh3w-U5e4ArjQ3gpqclRvwF9fe4WDYXv8AZonb9VP7PWSm-h6m_Cp92kPlgUTY5gzDprGNY7Cls6wP9f72NhnUM6jHJZgzi29IU0k-g8PRIBIfVjO6tK5JaWFv0Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc714b302c.mp4?token=W6nO5F3Hpli7aBVHE-pWXwx4bHKFQcQgJtRlaHL2dQwR31WvmvQsH-Nvtlt50kuNppj6qVPmpfWT_eUbEOI33nbHimdeU6aoXb0fz31UTEXSBi9W04EFtfJMm7Sa2Jh3Duhdx7XkRWd8TE-CnP-mbrnBnXkhKR0tP3BI4R5K0otJ6t6dKBj21NfnKISRFnAzDMad2d23XXLF7E5-oDI_33Ux5Bh3w-U5e4ArjQ3gpqclRvwF9fe4WDYXv8AZonb9VP7PWSm-h6m_Cp92kPlgUTY5gzDprGNY7Cls6wP9f72NhnUM6jHJZgzi29IU0k-g8PRIBIfVjO6tK5JaWFv0Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع اعمدة الدخان من محافظة السليمانية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/83953" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83952">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f2abaf633.mp4?token=JLQ4c_Ti66uYqd0HSdObj1jT9D2GRtrovMQ5ua6Yutnjwe4q8Z4kU3S1cIvV3nKognx2dwx4dq2ajFLKOccHQNgRyXdTORwA0RU38iR6GHHA3zh-iOBdxxqIA0Bno3uaAE1JTVatX7N2t2HuXKe0YUDyRhbQhsCoOtWirWa8zpP4OKcfQCBesTSwHhFWUkRTDyj8lC4KKr8_-V042YbRheXmMniv2rV-hvr9b7kuQ1Kc8ns1tAEOM_NQkVz4LuPioT9d0Ok1wU5gn57vOK__8BJcVaqWhpQZo9mijeFXKVOOppFGG0NueaCSt9lsQPfzAo1i4ZzKCgXR5q6EpUEvFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f2abaf633.mp4?token=JLQ4c_Ti66uYqd0HSdObj1jT9D2GRtrovMQ5ua6Yutnjwe4q8Z4kU3S1cIvV3nKognx2dwx4dq2ajFLKOccHQNgRyXdTORwA0RU38iR6GHHA3zh-iOBdxxqIA0Bno3uaAE1JTVatX7N2t2HuXKe0YUDyRhbQhsCoOtWirWa8zpP4OKcfQCBesTSwHhFWUkRTDyj8lC4KKr8_-V042YbRheXmMniv2rV-hvr9b7kuQ1Kc8ns1tAEOM_NQkVz4LuPioT9d0Ok1wU5gn57vOK__8BJcVaqWhpQZo9mijeFXKVOOppFGG0NueaCSt9lsQPfzAo1i4ZzKCgXR5q6EpUEvFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/83952" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83950">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e783804844.mp4?token=KArJsV5yOXhdVW7Z0_YRawBZX7PNsU95KiIqTHPfhepL_SdRMgfiDNy6lDQkpsAkFGe1Wej9cbnyjlrzAnaotUZ3dvFtObnYYJ22TLCE1crfkWY0lIG7rYtD5nfKZronMK4mIeErirtYs4MLAm3y_AN4iS7sEfP36EW-yYKP6wgsHnHLIxK9iEFrpP8MIDFHK6tup-2Vr-y56mKFg1-8v4ec-TIjOV0TLcyIG00FvRkSbuT1E7AqTD5nCUqUfl-cLxMlAxZmddD_GVrf8_jQ18eBZvr3Nwnzp3Ti29tFZOmvF6iydOWayujWFoC0vN2Q1_2dackr_jnVSEoiAA3jBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e783804844.mp4?token=KArJsV5yOXhdVW7Z0_YRawBZX7PNsU95KiIqTHPfhepL_SdRMgfiDNy6lDQkpsAkFGe1Wej9cbnyjlrzAnaotUZ3dvFtObnYYJ22TLCE1crfkWY0lIG7rYtD5nfKZronMK4mIeErirtYs4MLAm3y_AN4iS7sEfP36EW-yYKP6wgsHnHLIxK9iEFrpP8MIDFHK6tup-2Vr-y56mKFg1-8v4ec-TIjOV0TLcyIG00FvRkSbuT1E7AqTD5nCUqUfl-cLxMlAxZmddD_GVrf8_jQ18eBZvr3Nwnzp3Ti29tFZOmvF6iydOWayujWFoC0vN2Q1_2dackr_jnVSEoiAA3jBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من محافظة السليمانية بعد هجوم استهدف مواقع المعارضة الايرانية الكردية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83950" target="_blank">📅 16:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83948">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSovsQDGsElsNYgTcyoMBC2VJzSVz1E9_K7tBHJzjROzmvuphVxiBNN6NRXHypT5_Cyxd4n8PyO3I0ziV7gSBjYrNnVTPQ9-yf9tkux3ZCyPiOAaOBALVhWQFRojnYp-AgmGTzsylwkL2MoMf1rgkvDxwpxm6r0Z12078OjcaNkEqG9ub_FDtkfthKIhluuSjHL2zBiTAKPVoLpQ52Ri5OGqrIJLG_xusS5LeTbtnRwP6d7qyDO2xOLevgOtfdO4_GbOF1jNDnove94drOJijzzyvgTlDuV8bHAvF2Yb4OX3XUJFmhlhSX4UWGOi-TgxbacfEZyBARByvvrhFv8NrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0Ho5qqh6qDyrx2N-c07V4ihcA25XXSR8WqUP0Toc-9jFi4U8ntZX2ZbR52obWgBcf-y-u6gltr9fq8uvszyQ3owtPsvYBBtEEzSqxQMV4H7hoR-pWvVhkic-wyqGv1ZrTA-2dQFbhInxmsyRTlmNlGDbswiofm4-_JLu31P-JbucWxxT2Oys5jh6DIhEtKfTBJK35oKP6i915lSwUrI6808t3qiMqpAYEzSN9YbFrn8GpoWHLkew_VT40kEeefTFDZmrR34XMGm8_8VeDzKLxR4jA82PUrUBmNxilSaSflD_BXcT-VVh_Uq8RuUlJrLoxpZjTV0al4G7hR0FbOajQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارات تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83948" target="_blank">📅 16:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83947">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoKMPvZMRdHOc3kwtwL46Dyf6etg20Bt7jinT3H-ORiTmts_BPtVaWMl7Ol9CYbtXyet7jeRgkS7pR75XMsmEI9S1_KY7m3CWR7BFvgmrDlY47QrLc1oXIxOSnkQ0S5latV6oNBmLlC0cehQBudl7xYQbdLjunrmJwcOzvkS1DuN-AvRIRrEoP6lhhAre6iCdjPcoAN6xDVYqik_Is7By4hBy7qT53yNbL1UApfrKRjjRfBs3p1KU2JNAYUzWStMijdRR8G7F1bvwYY4GULkjhp0OlswOM69zJBqAPs4kyMrMSTjWAvnt52TIZTS-mU9N4KNShYxTBls1fpMA_kyOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد اعمدة الدخان من القاعدة الامريكية في الاردن بعد الهجوم الايراني</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83947" target="_blank">📅 16:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83946">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83946" target="_blank">📅 15:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83945">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83945" target="_blank">📅 15:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83944">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجارات تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/83944" target="_blank">📅 15:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83943">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce6a72292.mp4?token=RtW46wAj8CqSgJaarhgQNuwx_VjwfdCfPoXxXDi57ckNrjZdEP33HnOl9YVFjunxg7WOJhBk7pQTrcOPCdfmJi5oDcUxvr_CuVXZ-IYUKspAOMi6MwWtOrKkbeiAgzpepBqNoBlUZOX5uU1Dx8ktOz1PYK1CJxZwxen60uGPaSa1te1-5wm7h3teTwBFCU2jcW1v8ixzFsNCIh0xg5XziGRW7WSRCIXPpPYWCSTeyKxaJWFSUxfreIuoXhprELTHn0_o-6mQ7Mx0yqYHibk6pn5yvNUrFB-7PnOHhoyipqJtFJaupaon677jDV5KSozyC9cefe_bPFSvPLNlb5NXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce6a72292.mp4?token=RtW46wAj8CqSgJaarhgQNuwx_VjwfdCfPoXxXDi57ckNrjZdEP33HnOl9YVFjunxg7WOJhBk7pQTrcOPCdfmJi5oDcUxvr_CuVXZ-IYUKspAOMi6MwWtOrKkbeiAgzpepBqNoBlUZOX5uU1Dx8ktOz1PYK1CJxZwxen60uGPaSa1te1-5wm7h3teTwBFCU2jcW1v8ixzFsNCIh0xg5XziGRW7WSRCIXPpPYWCSTeyKxaJWFSUxfreIuoXhprELTHn0_o-6mQ7Mx0yqYHibk6pn5yvNUrFB-7PnOHhoyipqJtFJaupaon677jDV5KSozyC9cefe_bPFSvPLNlb5NXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حصرية بعد قليل من نايا من آثار القصف الإيراني على الكويت قبل قليل</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83943" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83942">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f86a8ce4.mp4?token=YA3N58exChzDzfZe-GKXustBvDtA5bESAhhPJtzNS5dbXTzMcPe96DZufX9AJKDi5MmPFJR1_D21T2q-fGpri6jw2DZcQKQ4AeZ1BAAbY92bPCfTmXR-l4vM2RmgX15qHnKa_jV-kB09k0qwvdeNETCvWEh26jRoSg-lhD7iNYF-XdceLdOt71XpuvPPsgXpX8EdyflpG-O1zgRJdJLnhxkuJKxVBnI1Ywo1s7PrWMDKAv5ygnIzthJ4I4-ztqsENmEtII7WCMQZ8vXtSz_UjNeQmSTZ2fj6ZUd388joYExFqjeEjIuqrsaPIVTnLkb0R3wNk91uagAxXwydJ_uVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f86a8ce4.mp4?token=YA3N58exChzDzfZe-GKXustBvDtA5bESAhhPJtzNS5dbXTzMcPe96DZufX9AJKDi5MmPFJR1_D21T2q-fGpri6jw2DZcQKQ4AeZ1BAAbY92bPCfTmXR-l4vM2RmgX15qHnKa_jV-kB09k0qwvdeNETCvWEh26jRoSg-lhD7iNYF-XdceLdOt71XpuvPPsgXpX8EdyflpG-O1zgRJdJLnhxkuJKxVBnI1Ywo1s7PrWMDKAv5ygnIzthJ4I4-ztqsENmEtII7WCMQZ8vXtSz_UjNeQmSTZ2fj6ZUd388joYExFqjeEjIuqrsaPIVTnLkb0R3wNk91uagAxXwydJ_uVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حصرية بعد قليل من نايا من آثار القصف الإيراني على الكويت قبل قليل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83942" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83940">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0ddcdc3f.mp4?token=HUex52jk5JCGqB5hSpprYqr31nOdNx_DBPnb1T5UeqxEjpPo0kk9utZ5o__kHWixP9JXYwbBMbWC8PzuUPzbJKTwc8uMCJhFyphBZTC0CSTtdHd1WplNfRFtj1UQwofiXtVBw4lI9VrwR4F5re2KC4ZZGhVVCtm76GSbuhu7cetU2kBQ5FDLnu09g7_sOD6ftMobv1GUiDX_zAhgV_yOlkpr9aJloEnV6xXsBmwMY8s8iP1AFaGBh2ByN70PN43B8tZnhko7N1wp8hrJDYK3ZRIy6tnEFv59z2EfLEAzB8hMui2HlM9M44Hf6p9eHr7_4Osp7MZnER6-pHUoqRmpYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0ddcdc3f.mp4?token=HUex52jk5JCGqB5hSpprYqr31nOdNx_DBPnb1T5UeqxEjpPo0kk9utZ5o__kHWixP9JXYwbBMbWC8PzuUPzbJKTwc8uMCJhFyphBZTC0CSTtdHd1WplNfRFtj1UQwofiXtVBw4lI9VrwR4F5re2KC4ZZGhVVCtm76GSbuhu7cetU2kBQ5FDLnu09g7_sOD6ftMobv1GUiDX_zAhgV_yOlkpr9aJloEnV6xXsBmwMY8s8iP1AFaGBh2ByN70PN43B8tZnhko7N1wp8hrJDYK3ZRIy6tnEFv59z2EfLEAzB8hMui2HlM9M44Hf6p9eHr7_4Osp7MZnER6-pHUoqRmpYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من أكاديمية سعد للعلوم الامنية في الكويت</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83940" target="_blank">📅 15:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83939">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83939" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/naya_foriraq/83939" target="_blank">📅 15:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83938">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مشاهد حصرية بعد قليل من نايا من آثار القصف الإيراني على الكويت قبل قليل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83938" target="_blank">📅 15:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83937">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83937" target="_blank">📅 15:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83936">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تصاعد اعمدة الدخان من أكاديمية سعد للعلوم الامنية في الكويت</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83936" target="_blank">📅 15:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83935">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ecdbf49a.mp4?token=EbmTEriNJoNHxSYcKwVkj5cUYkRXianLTuvvB2kR_7FytqXuahh6XSRbx5TFFUaq_ChVksZgOmc9BtjaH8Wx2S-8o9F6NkCq4w6CSIJ0Vyj7WRmOvuvqkm1mxcE4orwJMEzbB_4bbtmMHrCKHdEeMWrNm7JemBfzMFp63f-cj811FTRXQZyjHL7SAA4po5h13OM_eEQlyx25EnQ74sjXsBUKfoEDUsHxw2VVjn1PxFVtUrAVeL-5kcJDssXF2d9TECxPMi-L-kRSqAH5CCAsO0h3nkNx4HaAzBbKFBECMjqo-qOHnrH_Bil9-OfXA2Skvj4_fj4-P7-bZZ11owca9x6tMM4HNHCikB2d8tmfuJX6GD2EfCz8wKptqytW-otYMiNmb0QyDahAYLTtb4SFAQfi7Ru_d2LEuAyBhvVyJ1E42bM3HAJdVvaAYycQONAs1cXwmfRCB2AokVwhz_cBClBlV6gMRSGijd4edR5dzYXmhS4reADHXmCPS93UYNUc9ic0iPYPIItgu0pUmNhXkIm4qy1mpmNeiuzYyQw4jQiVfzSx2utEhHOxWy4eAHzmiDQXeMydK3-1OdSDMPTp6CBuddQMH1UxkrKXjl-85rxFfrojSAmR1FDMmh2Pq2pgqs176cJOTouQZdQAn3A1dJHi3tuJo2T_V_CvEzO7XhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ecdbf49a.mp4?token=EbmTEriNJoNHxSYcKwVkj5cUYkRXianLTuvvB2kR_7FytqXuahh6XSRbx5TFFUaq_ChVksZgOmc9BtjaH8Wx2S-8o9F6NkCq4w6CSIJ0Vyj7WRmOvuvqkm1mxcE4orwJMEzbB_4bbtmMHrCKHdEeMWrNm7JemBfzMFp63f-cj811FTRXQZyjHL7SAA4po5h13OM_eEQlyx25EnQ74sjXsBUKfoEDUsHxw2VVjn1PxFVtUrAVeL-5kcJDssXF2d9TECxPMi-L-kRSqAH5CCAsO0h3nkNx4HaAzBbKFBECMjqo-qOHnrH_Bil9-OfXA2Skvj4_fj4-P7-bZZ11owca9x6tMM4HNHCikB2d8tmfuJX6GD2EfCz8wKptqytW-otYMiNmb0QyDahAYLTtb4SFAQfi7Ru_d2LEuAyBhvVyJ1E42bM3HAJdVvaAYycQONAs1cXwmfRCB2AokVwhz_cBClBlV6gMRSGijd4edR5dzYXmhS4reADHXmCPS93UYNUc9ic0iPYPIItgu0pUmNhXkIm4qy1mpmNeiuzYyQw4jQiVfzSx2utEhHOxWy4eAHzmiDQXeMydK3-1OdSDMPTp6CBuddQMH1UxkrKXjl-85rxFfrojSAmR1FDMmh2Pq2pgqs176cJOTouQZdQAn3A1dJHi3tuJo2T_V_CvEzO7XhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القاعدة الامريكية في الاردن تحترق</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83935" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83934">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9043e8d.mp4?token=IE79oq-jFUdn5RgmzoqvYdcO451-QQyAuBSYLGj9ONMccUJE2NUrKn8mNFPeZ8s64jpljEMagJEXdqRCxC9aG-_G3es8tbN8csvujH9xFxY-_UGMAIgzNHJvSCMP3-epTgltrH37S_IBZ05WMG7avv3a8GhnJ020k7Qj3Y-jjnna6XUmDl3d_YopQHzevMF-AxdeaAbAgfJtLG5LQpWFwyw0aUqEVQc0jH4R1Kuh1YSJe7R7aBBIVxTqdgn1hJi4BWr9uo9YQur9R97d9Yy1V1POvHoqAARMehH26SgBLEW1hxBhvKwDFoJHr6J2M9lDfBYB53jBrvNdwWY5SOKGMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9043e8d.mp4?token=IE79oq-jFUdn5RgmzoqvYdcO451-QQyAuBSYLGj9ONMccUJE2NUrKn8mNFPeZ8s64jpljEMagJEXdqRCxC9aG-_G3es8tbN8csvujH9xFxY-_UGMAIgzNHJvSCMP3-epTgltrH37S_IBZ05WMG7avv3a8GhnJ020k7Qj3Y-jjnna6XUmDl3d_YopQHzevMF-AxdeaAbAgfJtLG5LQpWFwyw0aUqEVQc0jH4R1Kuh1YSJe7R7aBBIVxTqdgn1hJi4BWr9uo9YQur9R97d9Yy1V1POvHoqAARMehH26SgBLEW1hxBhvKwDFoJHr6J2M9lDfBYB53jBrvNdwWY5SOKGMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هكذا تبدو المشاهد صباحا من الكويت حيث صوت الغارات والقصف الإيراني لا يتوقف ..</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83934" target="_blank">📅 15:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83933">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوي انفجارات بمنطقة الميناء بالكويت</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83933" target="_blank">📅 15:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83932">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏴‍☠️
انفجارات عنيفة تهز مدينة أوديسا الاوكرانية ، أوديسا هي قدس روسيا وتتواجد بها اكبر قاعدة لحلف الناتو ..</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/83932" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83931">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/83931" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83930">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات تهز قاعدة الجفير في البحرين مقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/83930" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83929">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/83929" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83928">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebbb2b7015.mp4?token=lEAiq4rq_GoPf1ghg1cVCNwj3xvy7lp7n7aflbFUBL7K3arwImpdQG9DeurHk9Bi0p2L6R6u7jYbLQvyR2bH9qbl5kbvBbtyH85Z1GDcLNTweOWlrp4TZjFd5RJ0l1jivQQ0Vig3_SWWl4LOIwn3Mm9UDPX05GpyLuE3exKyFzyIYKGDuv1DlbIwOi55Jb2go-Aa4SonOUsaxm_8U0iF3-GNV6UbuDb6MN85HiNd9SA_MteMnup2H8qWk7fF1XO537GEA-u2LavK_xWk2tsqMn9scHED_u3RnnQbs4RtXC_Gzzj5W2E_SEEQTMgFJqXaXOCQJdKTBIlG_HAMnhMsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebbb2b7015.mp4?token=lEAiq4rq_GoPf1ghg1cVCNwj3xvy7lp7n7aflbFUBL7K3arwImpdQG9DeurHk9Bi0p2L6R6u7jYbLQvyR2bH9qbl5kbvBbtyH85Z1GDcLNTweOWlrp4TZjFd5RJ0l1jivQQ0Vig3_SWWl4LOIwn3Mm9UDPX05GpyLuE3exKyFzyIYKGDuv1DlbIwOi55Jb2go-Aa4SonOUsaxm_8U0iF3-GNV6UbuDb6MN85HiNd9SA_MteMnup2H8qWk7fF1XO537GEA-u2LavK_xWk2tsqMn9scHED_u3RnnQbs4RtXC_Gzzj5W2E_SEEQTMgFJqXaXOCQJdKTBIlG_HAMnhMsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇦🇪
وزير الدفاع الكويتي يزور جرحى مستشفيات الكويت التي تعج بالمصابين العسكريين الذين يعملون داخل القواعد الأمريكي ، وزير الدفاع الكويتي يؤكد ان لو لا جنود منظومات الباترويت هم غير موجودين بالكويت</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/83928" target="_blank">📅 15:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a628a424fb.mp4?token=bXl2vmbWxgRVSoijZU1HNkUyPPQdO4hFC02yk36J_CSVi7EvVoTBmKmsXcdnnAsH548J26FA8Zmk9_cVrYMUq8fysNd_GOFGV8-4oFjaY6Zbu4BIePOQ_6ZnJchsFdPY_R8yDXtX3CO5gQpOtIIr_S93TRXd9XCHlK5Cl_S2nphui1jQ2Bmlj2HYiF4cCtiC-LBFi981HGVoZhtpTtJGCeTBjM5xjeKwyotLlBIEJE_NklfqG5RFkIwuZWhpQr7Im6nmTrPf5ChHtkYL-kD63o_vq9hs2lKKVri7V1KuUrI3iNzbKdyrXYKZtKBSa0MZ1b84H4TQXdH2Qgrr6nIYtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a628a424fb.mp4?token=bXl2vmbWxgRVSoijZU1HNkUyPPQdO4hFC02yk36J_CSVi7EvVoTBmKmsXcdnnAsH548J26FA8Zmk9_cVrYMUq8fysNd_GOFGV8-4oFjaY6Zbu4BIePOQ_6ZnJchsFdPY_R8yDXtX3CO5gQpOtIIr_S93TRXd9XCHlK5Cl_S2nphui1jQ2Bmlj2HYiF4cCtiC-LBFi981HGVoZhtpTtJGCeTBjM5xjeKwyotLlBIEJE_NklfqG5RFkIwuZWhpQr7Im6nmTrPf5ChHtkYL-kD63o_vq9hs2lKKVri7V1KuUrI3iNzbKdyrXYKZtKBSa0MZ1b84H4TQXdH2Qgrr6nIYtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف عجلة واوكار للتنظيم الارهابي</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/83927" target="_blank">📅 14:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83926">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxBATl-bYcXZ7vSoLCERc0PRQdfzgQ8wlSq2f4TxEkI7C2lSzJ5xS57fmVir1T9Uo2PwMVV3mUWVF0HvUrtw1Q0QUaDE0rD9xNJWlMzfmNx4p7PvhCEa7uc2H-rB5tNHl7zrL_bNk4_X7jwHd0Pm3BvuvnLb-24OhXgIAh_YXEbrcaR3tY2v9FZdG3Yv_LkMqSODDR-S5fVkzBvUV16J9_jfLEbXZIxBj580G5jiFt8AYXEUUbMgheee1FUmKPged7xVmOeRl8WuJB5v_kCLC0vItn48cncdSHfP6_stOMGoi15BracjGOQHi8iTJoCAi6Al0rweOX2ygHEwsPgFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصابة مباشرة للقاعدة الامريكية في الاردن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83926" target="_blank">📅 14:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83925">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اصابة مباشرة لقاعدة أمريكية في الأردن وارتفاع أعمدة الدخان</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83925" target="_blank">📅 14:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83924">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008b089ae2.mp4?token=PoUfroZ0hh8If36k2UmN32e-hxokndTAHQg5ITxpiAXH26vKq2pVoiFSnFoTER9k7srY1d7oc_ZWVqzU740w3RNodBnYwYxEZCh5V4Ij7cck4oBYeE4VntyPhkRLOuo-J6O_zJoaBXWrA2X9AqDpwAeT05OGHIsY7SlxgORw0H54xw1QVfAkMP6jP0JB3HgbHm9BidfsoqiDeIfghmJap961UWgCgORqlavH7HLtJRC-NFHlcHr0DK_ziB1YZwybaku0D-NaVcr7t3JQKw9_SxAr42SWL1tFDa_hoqQIJqR8Z6rHjRHEim0lhq7gukTD2WNQ6FIsIbN-ko9nany69w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008b089ae2.mp4?token=PoUfroZ0hh8If36k2UmN32e-hxokndTAHQg5ITxpiAXH26vKq2pVoiFSnFoTER9k7srY1d7oc_ZWVqzU740w3RNodBnYwYxEZCh5V4Ij7cck4oBYeE4VntyPhkRLOuo-J6O_zJoaBXWrA2X9AqDpwAeT05OGHIsY7SlxgORw0H54xw1QVfAkMP6jP0JB3HgbHm9BidfsoqiDeIfghmJap961UWgCgORqlavH7HLtJRC-NFHlcHr0DK_ziB1YZwybaku0D-NaVcr7t3JQKw9_SxAr42SWL1tFDa_hoqQIJqR8Z6rHjRHEim0lhq7gukTD2WNQ6FIsIbN-ko9nany69w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من القاعدة الامريكية في الاردن</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/83924" target="_blank">📅 14:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83923">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">موجة صاروخية إيرانية باتجاه القواعد الأميركية باتجاه غرب اسيا الان</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83923" target="_blank">📅 14:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83922">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83922" target="_blank">📅 14:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83921">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b2110ca7e.mp4?token=p8uAADQYtTzUd56rQaKWzbzqfy51HNUy9W0Pxj_Mo8RsBpwDIGiMNyQOgiSDRLE60yoLbeC7MrPB3dn_49JCRQQFd1n-_duGwM8dn1Q4tyck9-E8nGZ0zr0OArx9Z4E9QcUYWlw8YnmPdzQwPM9Ln6Zp-tysnlCyU6Q3mSy5SAV-1BS8-JniKaFtN-EGvVXMOwFDUiSZusp34B1a19vf2A4hYZ8NcRC2hQ9GOCwxXsXbf-i_fCKRLTJSxj84AwBMgA-9IaPvyG-t4q3bQbdyebHWgTGmwhRyS79jYWIO1z0e5eF-asyAd8lNDPGqsNPwTTuwz_AGmEs2i45IkwJ8_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b2110ca7e.mp4?token=p8uAADQYtTzUd56rQaKWzbzqfy51HNUy9W0Pxj_Mo8RsBpwDIGiMNyQOgiSDRLE60yoLbeC7MrPB3dn_49JCRQQFd1n-_duGwM8dn1Q4tyck9-E8nGZ0zr0OArx9Z4E9QcUYWlw8YnmPdzQwPM9Ln6Zp-tysnlCyU6Q3mSy5SAV-1BS8-JniKaFtN-EGvVXMOwFDUiSZusp34B1a19vf2A4hYZ8NcRC2hQ9GOCwxXsXbf-i_fCKRLTJSxj84AwBMgA-9IaPvyG-t4q3bQbdyebHWgTGmwhRyS79jYWIO1z0e5eF-asyAd8lNDPGqsNPwTTuwz_AGmEs2i45IkwJ8_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الاردن تتزين بصواريخ الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83921" target="_blank">📅 14:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83920">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اصابة مباشرة لقاعدة أمريكية في الأردن وارتفاع أعمدة الدخان</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83920" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83919">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83919" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83918">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUuRsAEUhUcFaOlXt8a1kw_0Q91DeM0WbDrv4KKqE1VjH17QGF3x8ezYgLF_hSSkG9mMLrCFJPt3JbQLhiC4jdJaJikmUY70FgK_BxnWB47zSchCcGhewCd0yZ_wTV6kiWSfYrvHBMK1bhSuXcZAuVae1gKktrfujO4SefrwkmtLbBL3PdEXK_5nLuPGc0gK-6YuT8t9Y-sJ5othqf1wbL8hSsGu2aBOEbt9hm1tAZRoyC4cf8RGdi2ObhETEzsr2HrQg2qJypk6XvzGhhXJ4BQM920SCBiwIVCzfIK917a5cYiopWtFUGm3706oj_mEhezr0Bire-kqhFdNDHandw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الطائرات العراقية تشن غارات جوية على اوكار تنظيم داعش في قضاء راوة ضمن محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/83918" target="_blank">📅 14:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83917">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
الطائرات العراقية تشن غارات جوية على اوكار تنظيم داعش في قضاء راوة ضمن محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83917" target="_blank">📅 14:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83915">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الكويت: تعرضنا لهجمات إيرانية اليوم بلا توقف</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83915" target="_blank">📅 14:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83914">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ايران تطلق دفعات صاروخية جديدة باتجاه القواعد الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83914" target="_blank">📅 14:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83913">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مشاهد من مدينة الزرقاء الاردنية قبل قليل خلال الهجوم الايراني الصاروخي والمسير</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83913" target="_blank">📅 14:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83912">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNIOUlrpffwDaWuOa6PnzLZneqgoKt1P6rTZTaK3zjeO50dp0hvXQE1sD80pIt9kfd1V6oIQ2xPzgUL4kuo0LElnSJFHr1xwq8wxAAWXUlyGKzzA7d3V7dxfCC_OPIN_4qsVX1TAIV2iLTPLSEt9V8VH8H4url6ry9soLqFFbXPvR8Zu_WIwbNWfZ38YpqDq2pnO4zdku54JJ5avN9QZL5NQx-A-OW09k7otjXXyzfw7LTqFwUn6pOsSZ-DxJbqPuNc_OMF0wAqpNgALv17jhFXAqbTAjAY2Ciu52V5h99neIwW1GnVbU7QxRMF-D9qRJfbDPmi5HhPa2S9dt3JbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب سعود الساعدي يوجه سؤالاً نيابياً إلى وزير الكهرباء العراقي:
ما جدوى توقيع اتفاقية جديدة مع شركة جنرال إلكتريك (GE)، في وقت ما تزال فيه نتائج الاتفاقيات السابقة مع الشركة وغيرها من شركات الطاقة محل تساؤل، ما مصير العقود السابقة وما أسباب تكرار التعاقد مع الشركة؟!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83912" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83911">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50fe64417.mp4?token=PXjNv0TW3oq8Bkyy_nOD8KVB9hr-CRJDEvlzrLzzCK3YRUJnnzdefMQI_SU0Kzp1qaWqFe_srRPscGFP-zLutcBUEx7z2ZCIfYAuU79WK1UdBv9DDZj6mFKyzHe6LRTyGmFkIU6yJKvT4JKqoykpKAwDwdl1DVqzMrBxUpF9SUqgSJCvpJBVj4teQ8uwLL_gBfRsXkegYU7datk9Zn3MjXuC7QKnBB5btChpD8_rAxKqNhtQwOq0qEs0jnb-3c9pRaoSK6ojrM7LGN3VrCh9qVZIJRZAgkli8pZlY5l5dgN3muwF1xO1VzG976bLL5sMNc-fDHAkUa5ohf6VhxZKhXQu7xsXgTopsEK31O52LOmQpXPs1_ciUE8v6gWiLOZqmm-kSiAeVtccBJryKJN6CT6pqnrnouh4f50zW7jkLDLquEllFJfOlxNYTM9-sBSHe6VvaPyN1EXcdvwlGyxTDoIKiPatR7fx0BH3Ns4z55F1MYfk1E31K_9543Cgwd-w6CcwxT_6v_efR42tF4wI4ImIuXmegWNyuAfqdRBSSbrIh5LE_W3rkuPFfe944lnjbQWOB1MTcdaqXMEf20tAOT5nd-2jm3e_xQLzzo4HpJVdaPyVOBUQnyfFG_weZgAkTfDf3cypqn1dBNet-LHXzUDhCE6g_Y93z6dVWqFs884" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50fe64417.mp4?token=PXjNv0TW3oq8Bkyy_nOD8KVB9hr-CRJDEvlzrLzzCK3YRUJnnzdefMQI_SU0Kzp1qaWqFe_srRPscGFP-zLutcBUEx7z2ZCIfYAuU79WK1UdBv9DDZj6mFKyzHe6LRTyGmFkIU6yJKvT4JKqoykpKAwDwdl1DVqzMrBxUpF9SUqgSJCvpJBVj4teQ8uwLL_gBfRsXkegYU7datk9Zn3MjXuC7QKnBB5btChpD8_rAxKqNhtQwOq0qEs0jnb-3c9pRaoSK6ojrM7LGN3VrCh9qVZIJRZAgkli8pZlY5l5dgN3muwF1xO1VzG976bLL5sMNc-fDHAkUa5ohf6VhxZKhXQu7xsXgTopsEK31O52LOmQpXPs1_ciUE8v6gWiLOZqmm-kSiAeVtccBJryKJN6CT6pqnrnouh4f50zW7jkLDLquEllFJfOlxNYTM9-sBSHe6VvaPyN1EXcdvwlGyxTDoIKiPatR7fx0BH3Ns4z55F1MYfk1E31K_9543Cgwd-w6CcwxT_6v_efR42tF4wI4ImIuXmegWNyuAfqdRBSSbrIh5LE_W3rkuPFfe944lnjbQWOB1MTcdaqXMEf20tAOT5nd-2jm3e_xQLzzo4HpJVdaPyVOBUQnyfFG_weZgAkTfDf3cypqn1dBNet-LHXzUDhCE6g_Y93z6dVWqFs884" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الايرانية في سماء الاردن</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83911" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83910">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d41849e7.mp4?token=JwFBYJuleYmb0yyqqHPJJWoI-mjRSha2mGBzoljFQ9XR2PVw-C4P7v9AqsdfMbvuo0ACFTdqqOTmgTUFUVGv2akI37rVrV3F1bu22Rj1o9R8qTsHFYNWqh5hbCbrse2UPe9v5OUSMfq3ii8oEQWiH5HT3Ox2cQRewUfklbgslWpjW8UfU9u_hDo8j1rN5wR17mbHqBYf3Igr1Y4xW-VtIx3huLApktGZx7tHXx5h3ewkEMBUvB7WJpc4t81TtbKgPN_9bNw1pRomsWbdfsp7FjZoNRUNW-lYcR2ZlkY1Z-MgU5siT_JDSNPiuH27PwJFc5361GfMh26m1cJwLISYTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d41849e7.mp4?token=JwFBYJuleYmb0yyqqHPJJWoI-mjRSha2mGBzoljFQ9XR2PVw-C4P7v9AqsdfMbvuo0ACFTdqqOTmgTUFUVGv2akI37rVrV3F1bu22Rj1o9R8qTsHFYNWqh5hbCbrse2UPe9v5OUSMfq3ii8oEQWiH5HT3Ox2cQRewUfklbgslWpjW8UfU9u_hDo8j1rN5wR17mbHqBYf3Igr1Y4xW-VtIx3huLApktGZx7tHXx5h3ewkEMBUvB7WJpc4t81TtbKgPN_9bNw1pRomsWbdfsp7FjZoNRUNW-lYcR2ZlkY1Z-MgU5siT_JDSNPiuH27PwJFc5361GfMh26m1cJwLISYTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجارات في قاعدة موفق السلطي في الاردن</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83910" target="_blank">📅 14:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83909">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
حرس الثورة الاسلامية يبث مشاهد للحظة إطلاق صواريخ "خيبرشكن"، "ذوالفقار"، "فاتح 110"، "حاج قاسم"، والطائرات المسيرة "شاهد" في الموجات من 17 إلى 20 من عملية "نصر 2".</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83909" target="_blank">📅 14:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83908">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الجيش الاردني يزعم التصدي لعدد من المسيرات</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83908" target="_blank">📅 13:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83907">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏البترول الكويتية: موقع نفطي حيوي تعرض لاعتداء إيراني صباح اليوم</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/83907" target="_blank">📅 13:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83906">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏البترول الكويتية: موقع نفطي حيوي تعرض لاعتداء إيراني صباح اليوم</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/83906" target="_blank">📅 13:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83905">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هجوم بالمسيرات يستهدف القاعدة الامريكية</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/83905" target="_blank">📅 13:27 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

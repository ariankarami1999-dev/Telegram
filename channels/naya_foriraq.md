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
<img src="https://cdn4.telesco.pe/file/Nxc5PnsBH-3as0en9R9lWgoNNF4q3ygeTCzYcMOCZ3BDboQVCMVW61nn9gEqrzHj-DgNIyswWW2A4MAKRtYItMU8TmmNzC-UJggTC-vDTSHUBo4Bm1Y3pDjn8T0gSucoNDet4-Bgalvx2fAK3lcqCWeHbYEDVB06aRVP45HTFRw03tXJi_IHWKCFWOGQ3UlDda3aznGdbzsZAJ03J7GpwnP7JDNNf4lJ3d7wVIhyq5fmNeMYaPxwwv7x3XzJnDKlm8W6eNDK2_7AA2lFGQP05CBkl1PVUSEI9GifmL8xz_52eFYB-OnDQpi4cbnHEMZfHrPDCShj4oM9JAW41bjl-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-78880">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هجوم بقاذفة ار بي جي على سفينة نفط</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/78880" target="_blank">📅 18:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78879">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حدث امني قبالة سواحل اليمن</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/naya_foriraq/78879" target="_blank">📅 18:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78878">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حدث امني قبالة سواحل اليمن</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/naya_foriraq/78878" target="_blank">📅 18:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78877">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhs6mCWX9K1DY8ciajwbugEiYBqkibXpUZq72js8IDFOmWQsnws9_LyVqnwgiQYS9enUckGDxnxFfF9cbkNgtsic9uw1n98kFxPYZlwTzbO5L3e_NOq4OJZ7D90dgGK0JWKs89yyJ2f1QT2MKFssXcGNT_oSzK1Yew8wjmH6DOjpIJZwuU-DDG1-fY5_M8__tCI7VpNSC1CDWI1U7BXLYXAlDdNOYSKCe5Gz-GFpgehb5JtZWdWDKP9EJjTlu6tmlTTIbJTutjvcuEdE2pH-n7CFJUDRSPuT09vigqejw4UD6hv2fGtgx6FHRSTdrUgbjEV8bOn1gO4HbOMma4hg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
متابعة جوية |
أظهرت بيانات موقع Flightradar24 تحليق طائرة الاستطلاع الأمريكية MQ-4C Triton التابعة للبحرية الأمريكية (OVRLD02) في أجواء الخليج الفارسي ، وتُعد الطائرة من أبرز منصات الاستطلاع والمراقبة بعيدة المدى المستخدمة في جمع المعلومات ومراقبة التحركات البحرية والجوية علما ان الطائرة انطلقت من قاعدة موفق السلطي في مملكة البندورة المعروفة بالأردن …</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/naya_foriraq/78877" target="_blank">📅 18:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78876">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">لَن نَغِيب عَن المَيدان ...</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/naya_foriraq/78876" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78875">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
الجيش الأميركي:
حصار موانئ إيران ما زال ساريا في انتظار استكمال الاتفاق وعلى السفن المتضررة من الحصار عدم السعي للعبور.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/naya_foriraq/78875" target="_blank">📅 17:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78874">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو:
حتى هذه اللحظة، بالمناسبة، لم يكلف رئيس الوزراء نتنياهو نفسه عناء التعليق على الاتفاق أو التحدث إلى مواطني "إسرائيل" في يوم مهم كهذا. لم يصدر حتى بيانًا مكتوبًا قصيرًا. مرت 17 ساعة منذ إعلان ترامب عن التوصل إلى الاتفاق.</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/naya_foriraq/78874" target="_blank">📅 17:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78873">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇸🇾
إشتباكات مسلحة عقبها انفجار في منطقة الإنتفاضة بمحافظة الرقة السورية ؛ وأنباء عن تفجير انتحاري لعنصر من عصابات داعsh الإرهابية.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/78873" target="_blank">📅 17:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78872">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭐️
دوي إنفجار في منطقة شقلاوة بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/naya_foriraq/78872" target="_blank">📅 17:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78871">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭐️
دوي إنفجار في منطقة شقلاوة بمحافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/naya_foriraq/78871" target="_blank">📅 17:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78870">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7610c404c3.mp4?token=QJEMfFgVIj9FuzyFSidJ-L-_WUx2O7NGryb6tZh7I0cdFG2JyYE27sPgYFQPGFnyNRi-tZrb7YMr7wnMHYn4dct-zZmlE-tqJRIJMdyulNrQctt8WXFhPs53Stgrhl2BmbO9NX7uY2lsiP0d3F7TaYSdnTfgPsScNIx5Yv1I4RgVbSf-JboFZ16FSTGlhZzFtG_Ih7h6c1kUwyw6nfp9GL6rir3zK2OHr6C4TzGmSAGpTwgTL8lvXYJwOkOsEnMvzf0MxbHveGnIh8Oc40BpRHobc1A32viOCDp-g25kLRRnk_1oYwSSWLYhEpR6Aq7kTP1nWljWX1oaCs7PEaKSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7610c404c3.mp4?token=QJEMfFgVIj9FuzyFSidJ-L-_WUx2O7NGryb6tZh7I0cdFG2JyYE27sPgYFQPGFnyNRi-tZrb7YMr7wnMHYn4dct-zZmlE-tqJRIJMdyulNrQctt8WXFhPs53Stgrhl2BmbO9NX7uY2lsiP0d3F7TaYSdnTfgPsScNIx5Yv1I4RgVbSf-JboFZ16FSTGlhZzFtG_Ih7h6c1kUwyw6nfp9GL6rir3zK2OHr6C4TzGmSAGpTwgTL8lvXYJwOkOsEnMvzf0MxbHveGnIh8Oc40BpRHobc1A32viOCDp-g25kLRRnk_1oYwSSWLYhEpR6Aq7kTP1nWljWX1oaCs7PEaKSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
دوي انفجار يهز محافظة الرقة السورية.</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/78870" target="_blank">📅 17:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78869">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭐️
دوي انفجار يهز محافظة الرقة السورية.</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/naya_foriraq/78869" target="_blank">📅 17:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78868">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a6747efc.mp4?token=B3MTCc-DQVJM0Vo3oFFSGOZnr2PZIonL1OIGQXD2FkJLoiaYuuh0qRXYAihFb-cOFd0ZvJrUkhrRHtTSpFvPoQpfoU-dmE7XQClBo8lKkxuSe33mhTXFeaKODQ7byO_YdXkBzbLa9U7IvuJGJ2_0ZgJBEXRLrp2DvUtHMIZOd7xlz4D82BMCux16eUNSSu1IJYXmf6mU8KjUQttP1eb1tDy8MLCwFS5TMY9HimIX1DXagfZ4DE_jZMhpcZO0GR5Xx8Dd-vCfEawLWKbuCqYXkUb1aQ1uEeJogfs_xpebC2LEjl9ANzYSbxL9yeh_8xoCSFLki1ddgORUxmt1ZUYFOZ2VY_yaVe1kLd2wIOay2SMd-qNHl_ym-Oz0yDmvhTiQjW5KQW35roMI4uAh11wf1s4GvK4asebTqKRGAMwaa9hIeNMo0i-zXD1IBTURxo_wXralUpoSe2ilA7HXK6T5oSJvbVkkBk-zFXYQuINPLZxjZ_c0oh-9RrUkE6GoMmGx0EhbcNXS2VQjhmysvnqt1enyg3Th06Wg71VWaELrv6rLRmG66N5k0R0YXHJ6uWoULMmu55p5ykTQ-47u83XRMpdB5eTBbNn9MN4ti2xBn67xYLsFo1c9tOA9F47o8OIrUyPXAu1F-iVnwc8XeDOMyaSBVwE0sZ0Luk6zikqcOM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a6747efc.mp4?token=B3MTCc-DQVJM0Vo3oFFSGOZnr2PZIonL1OIGQXD2FkJLoiaYuuh0qRXYAihFb-cOFd0ZvJrUkhrRHtTSpFvPoQpfoU-dmE7XQClBo8lKkxuSe33mhTXFeaKODQ7byO_YdXkBzbLa9U7IvuJGJ2_0ZgJBEXRLrp2DvUtHMIZOd7xlz4D82BMCux16eUNSSu1IJYXmf6mU8KjUQttP1eb1tDy8MLCwFS5TMY9HimIX1DXagfZ4DE_jZMhpcZO0GR5Xx8Dd-vCfEawLWKbuCqYXkUb1aQ1uEeJogfs_xpebC2LEjl9ANzYSbxL9yeh_8xoCSFLki1ddgORUxmt1ZUYFOZ2VY_yaVe1kLd2wIOay2SMd-qNHl_ym-Oz0yDmvhTiQjW5KQW35roMI4uAh11wf1s4GvK4asebTqKRGAMwaa9hIeNMo0i-zXD1IBTURxo_wXralUpoSe2ilA7HXK6T5oSJvbVkkBk-zFXYQuINPLZxjZ_c0oh-9RrUkE6GoMmGx0EhbcNXS2VQjhmysvnqt1enyg3Th06Wg71VWaELrv6rLRmG66N5k0R0YXHJ6uWoULMmu55p5ykTQ-47u83XRMpdB5eTBbNn9MN4ti2xBn67xYLsFo1c9tOA9F47o8OIrUyPXAu1F-iVnwc8XeDOMyaSBVwE0sZ0Luk6zikqcOM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😚
إعلام روسي: تحطم قاذفة روسية استراتيجية من طراز "توبوليف 22" في منطقة "إيركوتسك" .</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/naya_foriraq/78868" target="_blank">📅 16:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78867">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7I9InM5BsWexT2KJL1hOl0F3qzQMeZ3IUhz4jruM4jUxPqG2vgtW454X_E5gZnTfr8wtqW8qN_yD-0S7FLa13elzH0WCrS06-4RkD_oWmmWnGqCN0W_dMBXmm7CgZPCWx90xAy9f4G4YuI9C3F_rorGL1qA5AH5ONhm1sy-s4KbYIS7uTYgemxrpBohuWRrSbvDQXfsOoFauv3DGwcth3m43Z1V2KUOt0fUe96os0eMahcQLkjOEvOAaUlU7SkZ1vq0h4i5SDGsUlKHRcsR6YemlUcoFzBzlIzkwv6__Si1Abv8tAMwryofOSfaBanmWgaU33Zwn61kEtspR_Nt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
«بدأت السفن بالتحرك، وكثير منها محمل بالنفط، خارج مضيق هرمز. وهي تسلك الطريق السريع الجنوبي، وهو آمن تماماً وخالٍ من العوائق. وهناك طرق سفر أخرى أيضاً!»</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/naya_foriraq/78867" target="_blank">📅 16:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78866">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لن يكون العراق امريكياً
و نستذكر هنا وحدة الساحات نستذكر بطولات مفارز ابو حسين الحميداوي والكعبي والولائي والغراوي و ال…. مجهول في الأرض والمعروف في السماء أبناء بني هاشم أستاذه عمايرجي ؛ هنيئا لمن وقف بمعسكر الحسين والتاريخ لن يرحم لمن خذل الحسين ووقف إما في معسكر عبيدالله او اختار الوقوف على التل والمشاهدة من بعيد ؛ والله لتغربلن والله لتمحصن ؛ رجعنا لجنوب لبنان خاوة ؛ وخسارتنا فقط دماء طاهرة على طريق الحسين مثل السيد القائد وعزيزنا تنكسيري ولاريجاني …
جميع حقوق النصر محفوظة</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/78866" target="_blank">📅 16:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78863">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
رداً على تصريحات الرئيس الأمريكي بشأن إزالة المواد النووية المخصبة، الخارجية الإيرانية: لقد جربوا ذلك مرة واحدة ورأوا النتائج، فهل يريدون تجربته مرة أخرى؟</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/78863" target="_blank">📅 16:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78862">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxGiMuUJZOM1wU3SbGOwlD4DnhSsRPuvmfPMK2AtLuX-9cg-AVNIBTFHRoGtBMsPEihJmxSXhFtQd0ZaDuDVmZJ9YpgaT2p8_Y3JGJyMySDoanjJF36OHnMQhrKUxM-2CQu35C1dVZ--LkzG3SpxMs2h-XAayJfO7DjS1_k7i0eKlZ40k-owrcCvxqTgkODdqhh8Dbw_vI_UqX6oFvQicxVfOoc_45qL5Lij5ukHAYNY0ZMi08o0cutww-RFsCwJElsSSd8rzHSlWMJwbuBqZJ6i-LNtUma0MYwAumKEgYgTDK6RbVxLr5jD7VLSTRjLnVut0fS8UpDf9Awe4fgOrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
عصابات آل خليفة في البحرين تحكم بالسجن 10 سنوات لاثني عشر مواطن لتأييدهم الجمهورية الإسلامية الإيرانية في مواجهة العدوان الصهيوأمريكي.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/78862" target="_blank">📅 16:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78861">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله:
بسم الله الرحمن الرحيم
"وَلَيَنصُرَنَّ اللَّهُ مَن يَنصُرُهُ ۗ إِنَّ اللَّهَ لَقَوِيٌّ عَزِيزٌ"
صدق الله العلي العظيم
يبارك حزب الله للجمهورية الإسلامية الإيرانية، قيادة وشعبًا، الإنجاز الكبير بالتوصل إلى مذكرة التفاهم بينها وبين الولايات المتحدة الأمريكية، والتي أفضت إلى وقف شامل لإطلاق النار على كل الجبهات ومن ضمنها لبنان. وإن هذا الإنجاز العظيم جاء ثمرةً للصمود الأسطوري والثبات الاستثنائي والتضحيات الجسام التي قدمها الشعب الإيراني العزيز وقيادته الحكيمة متمسكين بالخيارات الوطنية التي تحفظ كرامتهم وسيادتهم واستقلالهم.
وفي هذه المناسبة العظيمة، يتوجه حزب الله بالتحية والتقدير إلى سماحة قائد الثورة الإسلامية الإمام السيد مجتبى الخامنئي (دام ظله)، الذي قاد هذه المرحلة بحكمة وشجاعة وبصيرة قلّ نظيرها، وإلى رئيس الجمهورية والحكومة الإيرانية، وإلى القوات المسلحة الباسلة من حرس الثورة الإسلامية والجيش والشعب الإيراني الشقيق، معربًا عن بالغ الامتنان لمواقفهم الثابتة إلى جانب لبنان وشعبه ومقاومته، وإصرارهم على أن يكون لبنان حاضرًا في أي تفاهم يؤدي إلى وقف الحرب ويحفظ حقوقه، وتحملوا لأجل ذلك أعباء الحصار والعدوان، لتؤكد الجمهورية الإسلامية مرة جديدة أنها حقًا نِعمَ السند والحليف القوي والوفي.
كما يتوجه حزب الله بالتحية لكل الدول التي شاركت وساهمت وساعدت وواكبت جهود إزالة العقبات من أجل إنجاز هذا الاتفاق، مؤكدًا أن على لبنان أن يحسن الاستفادة من هذه المظلة الإقليمية والدولية لتحقيق سيادة لبنان وتحرير أرضه في إطار الوحدة الداخلية.
ونتوجه بالتحية الكبرى إلى أهل الشرف والعزة والإباء، إلى أهل المقاومة الأوفياء، واهلنا النازحين تحية لصبرهم وتحملهم وصمودهم، وتحية لتضحياتهم ولكل ما قدّموه في مواجهة هذا العدوان الهمجي، وقد أثبتوا بحق أنهم شعب أبي وأنهم أشرف الناس كما وصفهم سيد شهداء الأمة سماحة السيد حسن نصر الله.
والتحية إلى قيادة المقاومة ومجاهديها الأبطال البواسل، درع الوطن الحصين وسياجه المنيع، الذين بذلوا دماءهم الزكية ومهجهم الطاهرة في سبيل عزة وطنهم وكرامة أهلهم، وخاضوا ملاحم بطولية حيث رأى العدو الإسرائيلي بعض بأسهم، وأذاقوه مرّ الهزيمة.
إننا إذ نؤكد أن ما تحقّق هو مقدمة لاستكمال مسار التحرير الكامل لأرضنا، وعودة أسرانا إلى وطنهم وأهلهم، وعودة جميع الأهالي، لا سيما أهالي قرى المواجهة في الحافة الأمامية إلى قراهم وبيوتهم، وإعادة إعمار ما دمّره العدوان. ندعو أهلنا الصامدين إلى التريث، وانتظار توجيهات المعنيين بشأن العودة الآمنة إلى قراهم وبلداتهم، حرصًا على سلامتهم وتفاديّا لأي مخاطر قد تنجم عن خروقات العدو الإسرائيلي المحتملة.
إن على العدو الإسرائيلي أن يفهم أن لا عودة إلى ما قبل الثاني من آذار، وأن المقاومة التي كانت وما زالت العين الساهرة على حماية الوطن وشعبه، لن تقبل بأي عدوان يستبيح سيادة وطنها ودماء أهلها. وستبقى المقاومة متمسكة بحق لبنان المشروع والثابت في الدفاع عن أرضه وشعبه وسيادته حتى تحقيق الانسحاب الكامل وعودة الأسرى.
ومن هنا نؤكد أن هذه المرحلة تستوجب من السلطة وجميع القوى السياسية اللبنانية العودة إلى وحدة الموقف الوطني لتحقيق الأهداف التي يجمع عليها اللبنانيون والتي تكمن فيها مصلحة لبنان وحفظ سيادته وقوته ومنعته في مواجهة أطماع العدو الإسرائيلي. ومن الحكمة مراجعة كل الحسابات والمسارات التي سارت عليها السلطة، والاستفادة من هذه التجربة وما سبقها من تجارب مرّ بها وطننا لبنان، والابتعاد عن الأوهام والرهانات الخاسرة، والإقرار بأن الموقف اللبناني الموحد والاعتماد على الأصدقاء الحقيقيين هو السبيل الأمثل لصون المصالح الوطنية.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/78861" target="_blank">📅 15:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78860">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: إن مسألة الثأر لشهداء الشعب الإيراني مسألةٌ دائمة، ولا يمكن لأحد أن يتجاهل أو ينسى الجريمة الشنيعة التي ارتُكبت بحق هذا الشعب. لذلك، سيظل هذا مطلبًا دائمًا ومستمرًا.  لا شك أن الدبلوماسية والتوصل إلى تفاهم مع الطرف الآخر لإنهاء الحرب…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/78860" target="_blank">📅 15:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78859">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: إن مسألة الثأر لشهداء الشعب الإيراني مسألةٌ دائمة، ولا يمكن لأحد أن يتجاهل أو ينسى الجريمة الشنيعة التي ارتُكبت بحق هذا الشعب. لذلك، سيظل هذا مطلبًا دائمًا ومستمرًا.  لا شك أن الدبلوماسية والتوصل إلى تفاهم مع الطرف الآخر لإنهاء الحرب…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/78859" target="_blank">📅 15:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78858">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇩🇪
قائد سلاح الجو الألماني:
أن ألمانيا مستعدة "للقتال الليلة" ودفاعها عن "كل شبر" من أراضي حلف شمال الأطلسي (الناتو) إذا شنت روسيا هجومًا.
الناتو قد يضرب أهدافًا، بما في ذلك كالينينغراد وشبه جزيرة كولا والبحر الأسود، إذا اضطر للدفاع عن نفسه.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/78858" target="_blank">📅 15:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78857">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: إنهاء الحرب في لبنان جزء لا يتجزأ من مذكرة التفاهم.  احترام سيادة لبنان وسلامة أراضيه جزء من الاتفاق المؤقت مع أمريكا.  سنستخدم، حيثما اقتضت الضرورة، جميع الأدوات الاستراتيجية لضمان تنفيذ التزامات الأطراف المقابلة.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/78857" target="_blank">📅 15:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78856">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تجدد القصف مدفعي الإسرائيلي على النبطية الفوقا في جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/78856" target="_blank">📅 15:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78855">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
الحصار على موانئ إيران لن يرفع إلا بعد توقيع الاتفاق يوم الجمعة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/78855" target="_blank">📅 15:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78854">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
09-06-2026
آلية نميرا تابعة لجيش العدو الإسرائيلي في مدينة الخيام جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78854" target="_blank">📅 15:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78853">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⭐️
قصف مدفعي من قبل جيش الإحتلال الصهيوني على جبل علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78853" target="_blank">📅 14:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78852">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
🇮🇶
مستشار السفير الإيراني في بغداد:
من المتوقع حضور 600 ألف زائر عراقي للمشاركة في مراسيم تشييع جثمان القائد الشهيد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78852" target="_blank">📅 13:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78851">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
10-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78851" target="_blank">📅 13:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78850">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭐️
عصابات آل خليفة في البحرين تحكم بالسجن 10 سنوات لاثني عشر مواطن لتأييدهم الجمهورية الإسلامية الإيرانية في مواجهة العدوان الصهيوأمريكي.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78850" target="_blank">📅 13:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78849">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxNS-I-sGVoXSCs06VIZxfUkOwogJU8aMNHGiu4ja-KuZn28euT26XBDdQ4d7ikJcNvnwQizBu0j4-zbl6n-9wvwQNpMeg1hGtr-bBn9CcoNy18uTzrJzbQ3cIqvIZmdILPVndUOzjoUCaedK0yr8iNoI9Lku8MIULK0JmSG3nYYaIFSRSNQ7fyIwG4UHvzOXp_TCcVsmrEO-zUCLxQ3olq-VmXNBnOBua0S2pxdDLCoi7Mo5X0VNf_lsPU0pTjFTiDGZT5sMEZnWqVOaO1x6_kzZm7iy1LbNLnq7KuEK5Z0VhBDuSpJ08JGItgGaP1LeR4s8rj57czpfscmybYPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: مقاتلون من قوتين مختلفتين على الحدود الشمالية: توقفت كل الأنشطة، بما في ذلك دخول المنازل التي يُشتبه في كونها مخازن أسلحة، ويتم الدخول إليها بإطلاق النار. عاد الشيعة إلى القرى التي كانوا يتجنبون العودة إليها حتى الآن، وتم حظر العمل ضدهم.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/78849" target="_blank">📅 13:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78848">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
🌟
الأرض لأهلها.. البدء بفتح الطرقات في بلدة زبقين بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78848" target="_blank">📅 13:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78847">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4745391d5.mp4?token=Ai7KpHUwg_bnkPjQ0wKmkOy8T8KySaq00Hctcr6Z4CJoXn1CRe3hY5z42pfuQoPdb9R7Q4tf99-RNDbJheuiy4Gk6J_SRt0vPRtGfQ4eGaIHMdP_qoV8I2FK2yPXoeb7hMdPKYaGOBGW11NVs9ix9RGJwTPld05iDGUsomDtN8WWN60fccFTOJ6Da039Pi2dmdwmSr8eyGGsTO_7WZhHUphuNrG19XjEM_cKN4H_61V7mgJwJIwFWiB3kyiMTPGuvM5agSuetN3Bmun9zTbPA-8BGEOG5cSTwv583A68rx1ok4whT-pdtOUUW9sQUDRovDeHCmP9-ISARdQ_EboLig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4745391d5.mp4?token=Ai7KpHUwg_bnkPjQ0wKmkOy8T8KySaq00Hctcr6Z4CJoXn1CRe3hY5z42pfuQoPdb9R7Q4tf99-RNDbJheuiy4Gk6J_SRt0vPRtGfQ4eGaIHMdP_qoV8I2FK2yPXoeb7hMdPKYaGOBGW11NVs9ix9RGJwTPld05iDGUsomDtN8WWN60fccFTOJ6Da039Pi2dmdwmSr8eyGGsTO_7WZhHUphuNrG19XjEM_cKN4H_61V7mgJwJIwFWiB3kyiMTPGuvM5agSuetN3Bmun9zTbPA-8BGEOG5cSTwv583A68rx1ok4whT-pdtOUUW9sQUDRovDeHCmP9-ISARdQ_EboLig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش اللبناني يغلق الطرق المؤدية إلى النبطية وإلى قضاء مرجعيون ويمنع سكان المناطق من الدخول إليها بسبب تمركز الاحتلال الإسرائيلي.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/78847" target="_blank">📅 13:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78846">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6_fb_fMmzG6iakoouYDxEV7onXrnrS2QUI3AnDqEL7SLp7Qe2ZaGCU1PUQL29r4qeMGDa09OHhGKuIaRKfFzSE_II21_o-UWu8tU1FNWRHMt194_5f09UFteFg7z8beCl_A9d43g7L80ER1z8UWG6af7bYgeR8AMnDvUQ3vtuDqOujVa5tvMydLHdhZxso9toBTI3rTd_cqvs2J1AR_KGgQqkehr6db6MHsQ43WaW14hgwXwkBWDv9_M6UvxAbDW3Jgdq8C0slmNKsJ8vvDOiZc8qj4_FhO0ol9hig3cm7Yf306MfW6TcDKBzE0GkqnA7gbNRz-vml5_gwVCvcc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون حمايات ولا درع وعبر المطار المدني..
توم باراك يصل بغداد:
يسعدني ويشرفني العودة إلى بغداد، للقاء فريق السفارة الأمريكية المتميز بقيادة القائم بالأعمال جوشوا هاريس. سألتقي اليوم برئيس الوزراء الزيدي لأبلغه دعم الرئيس ترامب لحكومته، ولمناقشة شراكتنا في مسار جديد نحو علاقة أمريكية عراقية قوية ومثمرة للطرفين.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78846" target="_blank">📅 13:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78845">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZewQr_gY6zpmcF7onkq5L5QXu6tuQSJvcOsXI21wx5Q3iXPtWhco4pcvUYuKmYG1lxDiY1NKxujGwkd_zQxegcGHtHn10BzZppj0FO0K-Dk2bAFWvclkjwRl6kOkxoVUH9g1ItQFgjQl6eF560VWVl7rDAu5JvDQ5fxRGzmLeJeFjULy2BQ_rFcBb0-oiFwJqUqneYLzl36J5S20xpyI5MEWuni96UpL1u0LCYqDAtqdbcONI1rpiFBGOCj_mEL75HAgPSE68HyrV4SL2wMHur1YoJxmoKe7Vod1xbROodps283IZ1tgVPyt3NEPJJ6ProL-GBc9gfgM6yUc9niGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا يمكن المرور على موسى الدقدوق او نعيه كمقاتل او قيادي عادي او ذكر جيفارا او اي مقاتل اممي آخر دون تذكار فارس العبوات الارتجالية ومهندس المجاميع الخاصة و كاسر هيبة الجيش البريطاني بالبصرة وتلميذ عماد مغنية وفيلسوف نظام حرب الشوارع بأزقة شوارع الداخل والگيارة…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/78845" target="_blank">📅 13:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78844">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCODU0t9k1jBY0rxHMQ_Qo_Ef-KfUJQAPl5nrxfOcCuqsIIaURhcVD4sElB1S-fgjb5j1uB-WQMBfAb8Eifl21V5ARLyBdWpZrs53mb9DpTYZQYb51MVP8npCbvsEv5yM07PUF3FzDab2HbM8zGVFkItKlJ0dMJgLQ0kT5oBnwE49nRJGCcv0sSj4ZVM3L6foer1-d8WzhHtw50r30SNgxFfMIqr9Hc62b3S4fpOfOvqzsSO8PnvHugsp6pSji1Z0b7dpiFAFE_3Zg5_gspu8U6vaj0Dp-yJfEUuF4NJhTPvGdPu50bikRBuoAvkHx2jd1QLNOkxcSSNTEhgTP8cZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
قصف مدفعي من قبل جيش الإحتلال الصهيوني على جبل علي الطاهر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78844" target="_blank">📅 12:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78843">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8hhAiSDrOVOqSf7Qk8cwdiqppiy1vMwE-j47OyW_PWTkuraD62gx_5tfVKX0VJOF14DWMLSn7h-QX75VABv3ffLKUo2Z9G4bt_C96mhW0JpucDOA6GEPQw1NOMlzsv4AV4bDDyEJ4BFpRiFJJjEKcca9T_-JJLCxNhB1Dl5A9MLFPecN2KGByCfWJ1aWx3sfW_bK9gVdQyBwVFDtHfTggBGEXYzOJvRpeKh-A-hu7f290U6kgvZn9mDLIt3wyOEQicHqyTf3EYpkp7nuq2JNxYb4TDK1k8gIXQkkAMoaAK46yzzbsYWyI2uAJk6gAgvrRtaEAOtMBmNXyElilu_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
العراق لاول مرة
مبادرة تدخل حيز التنفيذ الان من وزارة الاتصالات العراقية برفع سرعة النت بمعدل ٢٠ بالمئة على ان تبقى نفسى الأسعار بالقيمة السوقية  …
برأيك هل سيحقق سند الوزير الإنجاز كما حققه كنائب سابق في البرلمان ؟!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/78843" target="_blank">📅 12:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78842">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKhi5lsnjIWhAQh0ZtS5ixYuRtKNsLGLPnkTrZhysN9RQzOmTuu1jdqBNcgj60MeSCZ2UFAX__JTtZIp12ov1k6gQ1wJT0UMNY7pIYIJoSvt7t7OEYrRS1HKg51nUuNilE-eYaTzySB9irEAEVvmjbsxBK_bpekEQ0yzU6z5FMajn04SM9OjdejUnE19ODShn7kcpXwjzM-xAxDOAIZUzCpM0E9me3eI6HagNUai2YcWCCG0Lpy_F08pv4AUdPmy5NEl-LbNdUMfpXAISbPDD9O1bPSlvhFh3nQodHn0FlL1TFz_sT0sDV_SOqR-Zl9JY_lMp4_EztYVKWa4DgcwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
المؤشرات الرئيسية في بورصة تل أبيب تهبط بحوالي 1.5%، على عكس الاتجاه العالمي.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/78842" target="_blank">📅 12:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78841">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1b94cb48.mp4?token=YdhIY-4HDRYPE9CVQbmLZWtMK1o3HkInvgIidSOvcvqM9ND4qYQtT-zZncikWC7KwpXTVbG61fcHTSJzKz2X_awiLyG1VLZGuGtqaJwBuKmDgxQX_2LVIRb-To7aQ8HOVdUlOw9g95FhahOzU_cygcWE3EFWdutkXtUWQgeY3deSqwD53b023uwZELCCexT-aSZDkHoERAjS8xLbW-CQDv_ZtfMtqufE5OaJbtnqA8Wyj5ysCfWc21qJrM0_MJNF2HqTDZoNRcuVZk4-_UdLvA8l2Y1MHf6FEQM5nfoocfYnsymQUzJ2gYo47GS-kAQuTH5-QkFQtE5gIMRs3A_xwAZ6_FbABDYIauCav2jpT144A2aX77KBacUJDjnDys9XO3jWJ2jWEsRov-HAWzNZJ7FN2czKUMimnoWC2sxJzBUB3gseOkoYKZnbsMxBfnnyLPud7uRDLm6cqNxXdjRXmYiafy09do2ofBH7XTaHldvBgU1dtySRlUCzOfX3BY37d0aTWfAcgBd5azXO7NNPt36MpiyZqIGMwS8Cd76vwPSy6uFBgsF6pUxhWD7w70kz-lrXRyT1-aLm_h-U7YrR5NlwaHZR6Kr_rh_NKkPgMhI9EBAXiuykfWBKQAg5skiFuapRgX1c9bfNcxBCIt052lF5_YDTEVhE0YatqJIdFwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1b94cb48.mp4?token=YdhIY-4HDRYPE9CVQbmLZWtMK1o3HkInvgIidSOvcvqM9ND4qYQtT-zZncikWC7KwpXTVbG61fcHTSJzKz2X_awiLyG1VLZGuGtqaJwBuKmDgxQX_2LVIRb-To7aQ8HOVdUlOw9g95FhahOzU_cygcWE3EFWdutkXtUWQgeY3deSqwD53b023uwZELCCexT-aSZDkHoERAjS8xLbW-CQDv_ZtfMtqufE5OaJbtnqA8Wyj5ysCfWc21qJrM0_MJNF2HqTDZoNRcuVZk4-_UdLvA8l2Y1MHf6FEQM5nfoocfYnsymQUzJ2gYo47GS-kAQuTH5-QkFQtE5gIMRs3A_xwAZ6_FbABDYIauCav2jpT144A2aX77KBacUJDjnDys9XO3jWJ2jWEsRov-HAWzNZJ7FN2czKUMimnoWC2sxJzBUB3gseOkoYKZnbsMxBfnnyLPud7uRDLm6cqNxXdjRXmYiafy09do2ofBH7XTaHldvBgU1dtySRlUCzOfX3BY37d0aTWfAcgBd5azXO7NNPt36MpiyZqIGMwS8Cd76vwPSy6uFBgsF6pUxhWD7w70kz-lrXRyT1-aLm_h-U7YrR5NlwaHZR6Kr_rh_NKkPgMhI9EBAXiuykfWBKQAg5skiFuapRgX1c9bfNcxBCIt052lF5_YDTEVhE0YatqJIdFwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية ناقلة جند تابعة لجيش العدو الإسرائيلي في بلدة عيناثا جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78841" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78840">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هجوم على سفينة قبالة اليمن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/78840" target="_blank">📅 12:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78839">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هجوم على سفينة قبالة اليمن</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/78839" target="_blank">📅 12:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78838">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📈
الذهب يستمر بالارتفاع منذ إعلان الاتفاق بين إيران وامريكا حيث ارتفاع 3% منذ ساعات الصباح الأولى ليسجل 4,343 دولارا للأونصة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78838" target="_blank">📅 12:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78837">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bd22030f1.mp4?token=oUjnn4pUZctHE42rX4EKmJ7JtJD19C__y2T0chNXjUBDOoYom0ZkWIzuEmRItgqLMnvoSSIXTwBRQ3A1MXDbJsi7H5EqRKfofr7UhY6AKKyQZNhvdFkcqHjys743lnt_mEAfg6WD5fFElR5lCddWrN6gGhnh7TWIcJ2-RH776WBViETwcwaOAJZUP6y_M_8cMnToRnfbovmwsPP3_-9u57ANoVOma1pbppRnGWo0DD8Wv0-ezbkNi49J6xPenn3ueS69MVfdLE7ln8NPs7h3eEKgFzK-OtsadTfzFmCPFSPgWqwCKXZieAWmCCzbOBR-F1_DnIrRwjj7roj718QU8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bd22030f1.mp4?token=oUjnn4pUZctHE42rX4EKmJ7JtJD19C__y2T0chNXjUBDOoYom0ZkWIzuEmRItgqLMnvoSSIXTwBRQ3A1MXDbJsi7H5EqRKfofr7UhY6AKKyQZNhvdFkcqHjys743lnt_mEAfg6WD5fFElR5lCddWrN6gGhnh7TWIcJ2-RH776WBViETwcwaOAJZUP6y_M_8cMnToRnfbovmwsPP3_-9u57ANoVOma1pbppRnGWo0DD8Wv0-ezbkNi49J6xPenn3ueS69MVfdLE7ln8NPs7h3eEKgFzK-OtsadTfzFmCPFSPgWqwCKXZieAWmCCzbOBR-F1_DnIrRwjj7roj718QU8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يتركون خلفهم دباباتهم وآلياتهم المدمرة على جانبي الطرقات قبل انسحابهم من الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/78837" target="_blank">📅 11:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78836">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHTrZYGoJ3rqooaAJhNvrw0bNrzk6L8brw8lL1tA6xI3DDdlSFOsJRmf-56PsbdPG2xTxUMxl5mAsEn01uPo12TGqy5knvcW26rUuq8mC1444OBAoiLHRaQWOt-T06Qi8aHZ7dxxeRiph5LuLDsHB3gMphbItbI-gdhYHUDErHeSTxVdn2yi9vMKIqelzywGb4YqutvkpjksRj2f0pjzJa9o0wdhQf0fjYBd86LXVO12EIt6624EKSNUdtzFuuR6JWSSSVSUoP5xsfkwClAQ64a5I-Ikhj__Hl8W4GR5TcW0uSMjP8D02muSpbuor72xNNmejGkfBtEaqj0_yDrH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بعد اتفاقية إيران وامريكا خام برنت يستمر بالهبوط حيث وصل سعر البرميل الواحد إلى مايقارب 82 دولار لأول مرة منذ أكثر من 3 أشهر.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78836" target="_blank">📅 11:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78835">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رئيس الوزراء البريطاني يعلن حظر استخدام وسائل التواصل الاجتماعي لمن هم دون سن السادسة عشرة</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/78835" target="_blank">📅 10:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78834">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7cc2b4e15.mp4?token=gENDs2jicVD7681NCuVrPzZgihTu0kM04yUQiyqMbgU2ph969J5Nya9rE00EYJRA1HbewXs6sj4qgoS1ZywjjXaMaaiI19h40xDLahRZ2AIWJSEk4_kceE32-JJd0nKpYXXFET-UrmwLHcCu7XUeqoEqOn13TN_w-mwC2q4elYKO-Aty662Hlh1tYkLrAGxno06mgRLPxoZhNNPxQunyNCvGQUavZaqHNHFLQgmRbEr8QwIJvfcxbPUYztwFjHTX6YjTY68cmvgFHh7RCJ91WelfbgFeMFEsCkNTwefrdptmDv_uRZ4mNqU0MVeXMhIRXS-7RI_pxrCkz9qC2AZuKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7cc2b4e15.mp4?token=gENDs2jicVD7681NCuVrPzZgihTu0kM04yUQiyqMbgU2ph969J5Nya9rE00EYJRA1HbewXs6sj4qgoS1ZywjjXaMaaiI19h40xDLahRZ2AIWJSEk4_kceE32-JJd0nKpYXXFET-UrmwLHcCu7XUeqoEqOn13TN_w-mwC2q4elYKO-Aty662Hlh1tYkLrAGxno06mgRLPxoZhNNPxQunyNCvGQUavZaqHNHFLQgmRbEr8QwIJvfcxbPUYztwFjHTX6YjTY68cmvgFHh7RCJ91WelfbgFeMFEsCkNTwefrdptmDv_uRZ4mNqU0MVeXMhIRXS-7RI_pxrCkz9qC2AZuKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚢
مشاهد من عبور أول ناقلة غاز ترفع علم مالطا من مضيق هرمز بعد الاتفاقية بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/78834" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78833">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇶
العراق يعطل الدوام الرسمي يوم غد الثلاثاء بمناسبة رأس السنة الهجرية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/78833" target="_blank">📅 10:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78832">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏴‍☠️
رغم جهود ترامب وتوسله لسريان الاتفاق مع إيران.. وزير الدفاع الصهيوني يعلن عدم انسحاب الكيان من المناطق المحتلة في لبنان وسوريا وغزة إلى أجل غير مسمى.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/78832" target="_blank">📅 10:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78831">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ba9c4c71.mp4?token=k_waQ6oV3MckeU2xGOCn74EbGPSZ4jRyNX87CCeXoA5NLcAL0xi5kTHXRT3MDukHEcZTqxsKJceJE-AmuudPGTBIbVRPR24MgOxRqj6nF4xKyyzQt_WrndS98yU7DMj6MpUqLg_8di9Oq_eZCOEfmFLh9usTCLOrmgbfqKq5T12clrutmszuOqhjp3v-eTk5CGrA10kS0wldsJvwRElJtVVawjHHsqe7Ux_qDRfXGgGZ5jVRQ_YhUiLNbf6lYkxMtrXuTD-AFYs3W0ROzDGoGQtx32Pv210Y_m0GUkJGcytD4UDJCdaKeNXCXKH0t3GuAL2ev8knEdVUh7H7M5g1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ba9c4c71.mp4?token=k_waQ6oV3MckeU2xGOCn74EbGPSZ4jRyNX87CCeXoA5NLcAL0xi5kTHXRT3MDukHEcZTqxsKJceJE-AmuudPGTBIbVRPR24MgOxRqj6nF4xKyyzQt_WrndS98yU7DMj6MpUqLg_8di9Oq_eZCOEfmFLh9usTCLOrmgbfqKq5T12clrutmszuOqhjp3v-eTk5CGrA10kS0wldsJvwRElJtVVawjHHsqe7Ux_qDRfXGgGZ5jVRQ_YhUiLNbf6lYkxMtrXuTD-AFYs3W0ROzDGoGQtx32Pv210Y_m0GUkJGcytD4UDJCdaKeNXCXKH0t3GuAL2ev8knEdVUh7H7M5g1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال يتركون خلفهم دباباتهم وآلياتهم المدمرة على جانبي الطرقات قبل انسحابهم من الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/78831" target="_blank">📅 07:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78830">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf0d0b85af.mp4?token=lemi9Y76SJb0Lau9UnPfloL7-DnH8nNHhhNodmCgNsNEU0xE3_vjwyE_ZYeD0XQT7-NqVUyrB9P4MF03ohy61BU91BvXLF2aaOMLFezBUqq_lmOJkAFfD_QwF_DgM_wEmPztUhomWbHsiNBSqE-pkp-swHZfB40vL6GqjCQ4k_NW6s9lbiZh6ciwxVY95luUkk1GeOviAOjGniL-RVn9fJXZJtLPQuCfI9FjmE7rWMloSe0W9D3DdbhmPdCLjHIEA5HujD4gHuf3YAUkGhO7hSWwjYaS9_Z1g3hyXXmXNRMmJYTHrLNv85-lndQxujK-rASyEdiLvqew09UPKSGOpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf0d0b85af.mp4?token=lemi9Y76SJb0Lau9UnPfloL7-DnH8nNHhhNodmCgNsNEU0xE3_vjwyE_ZYeD0XQT7-NqVUyrB9P4MF03ohy61BU91BvXLF2aaOMLFezBUqq_lmOJkAFfD_QwF_DgM_wEmPztUhomWbHsiNBSqE-pkp-swHZfB40vL6GqjCQ4k_NW6s9lbiZh6ciwxVY95luUkk1GeOviAOjGniL-RVn9fJXZJtLPQuCfI9FjmE7rWMloSe0W9D3DdbhmPdCLjHIEA5HujD4gHuf3YAUkGhO7hSWwjYaS9_Z1g3hyXXmXNRMmJYTHrLNv85-lndQxujK-rASyEdiLvqew09UPKSGOpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
على الرغم من وقف إطلاق النار.. جيش الاحتلال الصهيوني يستهدف بلدة كفرتبنيت جنوب لبنان.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78830" target="_blank">📅 07:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78829">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
الاعلام الاميركي:
قال ترامب إن الولايات المتحدة وإيران لا تزال تتفاوض على التفاصيل الرئيسية لاتفاق نووي نهائي، بما في ذلك ما إذا كانت طهران ستعلق تخصيب اليورانيوم لمدة 15 إلى 20 عامًا.
وقال إنه بموجب أي اتفاق نهائي، سيقتصر استخدام إيران لتخصيب اليورانيوم على المستوى المنخفض، "والذي لا يمكن أن يستخدمه أبدًا الجيش".</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/78829" target="_blank">📅 02:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78828">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M17agmZ-xygmmhxFYdN4HTNRTP7iytU23vNtUw_2C4f3ZaiSFafH20V9y-Ju4OJL96oWwEVXo-4gCcDYqXbtny92Y5_WH0LlZrh0kBM-a8fu7-m0YBtIs3DWxkYbYVmhF3eWo20WO3sx7tHfcZgIDD0PBBRgyhzKF00VSwsIbrVXCqZ31fJDuC77iTRrSGXrIc9xFlE_LESkJFAO3HGE5JC23otyKeLT39JDziSTXq5n4Ns_98sZbtAsl0DcL51dFt0J5BEkiwE3-l1Lv8j-hrWbnymCLMM8fopANBLxFSkDQ-ltgaUaQMMAYm1ahd6ybTfKMuKGgDUoja6yn6ffAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جميع الاطراف اعلنت وقف العمليات العسكرية، ننتضر الكويت
😆</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/78828" target="_blank">📅 02:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78827">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
بيان أمانة المجلس الأعلى للأمن القومي بشأن اتفاق إنهاء الحرب بين إيران والولايات المتحدة بسم الله الرحمن الرحيم  إلى الشعب الإيراني الكريم:   لقد استكملت الجمهورية الإسلامية الإيرانية، بقيادة قائدها الشهيد، تفوقها على العدو الصهيوني الأمريكي، وبتوجيهات المرشد…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/78827" target="_blank">📅 02:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78826">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b0380fc8.mp4?token=Sp330Of_56zeOmuAfaI2H7Za0K5J_3vW3_nAT_NwYDbvJYiykB2k1vwoExeylskGyUgfDTMJvj9lOYbHAg7MEA_NK7rqPecx4byKXtvzgG0enMQdD_lBiBaVQ6zeMj6C7Q1gbIj-SgSggEvchwbiHugEu36noneKfB4cgjlGEH_txbz3Cr679CdqYjpi9K8rLv4WogSqUZzvCPiy2ADLBoELWOcAXRusF-kicsk7LJ5vQn1QTeNqA51qdDNp5-3nRjufKGjn5YeWLq-4O4uVZFIse-sSkzWn0M75kM9w7hLxwU630roXsKGQCdOY_emS-H2mdmL3sVvlI4S7ODlBUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b0380fc8.mp4?token=Sp330Of_56zeOmuAfaI2H7Za0K5J_3vW3_nAT_NwYDbvJYiykB2k1vwoExeylskGyUgfDTMJvj9lOYbHAg7MEA_NK7rqPecx4byKXtvzgG0enMQdD_lBiBaVQ6zeMj6C7Q1gbIj-SgSggEvchwbiHugEu36noneKfB4cgjlGEH_txbz3Cr679CdqYjpi9K8rLv4WogSqUZzvCPiy2ADLBoELWOcAXRusF-kicsk7LJ5vQn1QTeNqA51qdDNp5-3nRjufKGjn5YeWLq-4O4uVZFIse-sSkzWn0M75kM9w7hLxwU630roXsKGQCdOY_emS-H2mdmL3sVvlI4S7ODlBUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
عمدة كييف: انفجارات في العاصمة. قوات الدفاع الجوي في حالة تأهب.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/78826" target="_blank">📅 02:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78825">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
بيان أمانة المجلس الأعلى للأمن القومي بشأن اتفاق إنهاء الحرب بين إيران والولايات المتحدة بسم الله الرحمن الرحيم  إلى الشعب الإيراني الكريم:   لقد استكملت الجمهورية الإسلامية الإيرانية، بقيادة قائدها الشهيد، تفوقها على العدو الصهيوني الأمريكي، وبتوجيهات المرشد…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78825" target="_blank">📅 02:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78824">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
"سيصدر البيان الرسمي لأمانة مجلس الامن القومي الايراني بشأن اتفاق وقف إطلاق النار قريباً". ‏  وفقًا لهذا التقرير، بعد الهجوم على منطقة الضاحية في بيروت، ألغت إيران مفاوضاتها وكانت تستعد لمهاجمة الكيان الصهيوني. إلا أنه في نهاية المطاف، وبفضل تنازلات قدمها…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/78824" target="_blank">📅 02:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78822">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22b6bfdd.mp4?token=anoHzXUNsrV67Vsh8_LKK3MjF0XtnR6mAvX5Mja-ZVZl2bxaUliiI2ku9Myf9ifOZdlTGlSiwC0YH4dCpnGHgvyeFYuC7T3OFE8VjdMzxnkLFAmFECHKdJLewmxZ75znpAZP19WiE0rwiHbU0PYW-sfQihHfgkfLlOnX_U4mfOl8YnZX2-C7j6uP80mxMdQ43XI2EdYjQICaBhtQjU9a58HQwDoPup_lcVBuDxOFHwlm0ywKUysAAVvQKBfB_b0W8MYr_05AmBLq_w6ayI0Eltkl5pNLK0MJBDix-enefRFIOM6Np1XjD9TpHn5cY0v6uYStZEB--LDaDdmrg-xU5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22b6bfdd.mp4?token=anoHzXUNsrV67Vsh8_LKK3MjF0XtnR6mAvX5Mja-ZVZl2bxaUliiI2ku9Myf9ifOZdlTGlSiwC0YH4dCpnGHgvyeFYuC7T3OFE8VjdMzxnkLFAmFECHKdJLewmxZ75znpAZP19WiE0rwiHbU0PYW-sfQihHfgkfLlOnX_U4mfOl8YnZX2-C7j6uP80mxMdQ43XI2EdYjQICaBhtQjU9a58HQwDoPup_lcVBuDxOFHwlm0ywKUysAAVvQKBfB_b0W8MYr_05AmBLq_w6ayI0Eltkl5pNLK0MJBDix-enefRFIOM6Np1XjD9TpHn5cY0v6uYStZEB--LDaDdmrg-xU5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
افراح تعم شوارع لبنان بعد انتصار ايران وحلفائها على الامبريالية الغربية.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/78822" target="_blank">📅 02:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78821">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏
تفاصيل جديدة لمسودة مذكرة التفاهم المكونة من 14 مادة بين إيران والولايات المتحدة الأمريكية"
تفاصيل هذا المشروع هي كالتالي:
‏1- وقف دائم وفوري للحرب على جميع الجبهات، بما في ذلك لبنان
‏2- التزام الولايات المتحدة بعدم التدخل في الشؤون الداخلية لإيران واحترام سيادة الجمهورية الإسلامية الإيرانية.
‏3- رفع الحصار البحري بالكامل في غضون 30 يوماً
‏4- التزام الولايات المتحدة بسحب قواتها من المناطق المحيطة بإيران
‏5- إعادة فتح مضيق هرمز خلال 30 يوماً وفقاً للترتيبات الإيرانية
‏6- تعليق العقوبات المفروضة على بيع النفط والمنتجات البتروكيماوية والمشتقات، ومنح إيران حق الوصول الكامل إلى مواردها المالية.
‏7- ضرورة قيام الولايات المتحدة وحلفائها بتقديم خطط لإعادة إعمار إيران بقيمة لا تقل عن 300 مليار دولار
‏8- 60 يوماً من المفاوضات للتوصل إلى اتفاق نهائي قائم على القضايا النووية والرفع الكامل للعقوبات الأمريكية الأولية والثانوية وقرارات مجلس الأمن التابع للأمم المتحدة ومجلس محافظي الوكالة الدولية للطاقة الذرية.
‏9- إعادة تأكيد التزام إيران بموجب معاهدة عدم انتشار الأسلحة النووية بعدم إنتاج أسلحة نووية
‏10- خلال فترة المفاوضات، التزمت الولايات المتحدة بعدم إضافة قوات في المنطقة وعدم فرض عقوبات جديدة.
‏11- الإفراج عن 24 مليار دولار من الأموال الإيرانية المجمدة خلال فترة المفاوضات النهائية التي تمتد 60 يوماً. ويجب توفير نصف هذا المبلغ لإيران قبل بدء المفاوضات.
‏12- تشكيل آلية إشرافية لتنفيذ الاتفاقية.
‏13- سيتم إقرار الاتفاق النهائي بقرار من مجلس الأمن التابع للأمم المتحدة.
‏14- لن تبدأ المفاوضات النهائية قبل الإفراج عن نصف الأموال الإيرانية المجمدة، وتعليق العقوبات النفطية المفروضة على إيران، ورفع الحصار البحري، وسيقتصر الاتفاق النهائي على مصير المواد المخصبة وتخصيبها، ورفع العقوبات، وخطة إعادة الإعمار الاقتصادي لإيران. وقد تم استبعاد المناقشات المتعلقة ببرنامج الصواريخ الإيراني ودعم جماعات المقاومة بشكل نهائي من جدول الأعمال.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78821" target="_blank">📅 02:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78819">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQWflgE8mXcGpdxjfBZ7QdmIfKxr4uraJm2W9T313jtZ3bjQautOJj4fNPldjsAa-tvxS08CLsSjI3WtnW4fdxTR_BCAYXcVlmVqMNfYXeBTEyVo5Qsol9xx9qhEFczADOoIayuTQ80r81Kf7c3dfm1a3j3uCxjwCZnRaVSHbC0r3B-3CSKL-P-m1CcVoR9z4UvVQQdEAQBvefagVqiy3zZwjqQSBg5hbMot_3-g5r5EyUt6i9qukYJu470ah0jT1pfGH5m3_R19Mvkll0zoaL7ZIKR-qYjt0m0MmJn-SuawX7xLKNOd7BWJN7cTCTo-Ui9eo3U83knZUNo-gOEvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب
:
"هذه الاتفاقية العظيمة ستجلب السلام والأمن للمنطقة بأسرها. لقد حاول العديد من الرؤساء إحلال السلام مع إيران، وفشلوا جميعًا قبلي. لقد وجد قادة المنطقة، ولأول مرة، رئيسًا قادرًا على مساعدتهم في تحقيق سلام حقيقي. مع فتح المضيق بتوقيع الاتفاقية يوم الجمعة، لأغراض إزالة الألغام، سيتدفق النفط من كلا الجانبين مجددًا إلى المنطقة والعالم! الرئيس دونالد جيه. ترامب"</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/78819" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78818">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">المقر المركزي لخاتم الأنبياء:
إن شعب إيران الصامد الفخور، وأبناء الوطن البواسل في القوات المسلحة القوية وجبهة المقاومة، بعون الله تعالى وتحت قيادة القائد الأعلى للقوات المسلحة، حفظهم الله، قد فرضوا إرادتهم الإلهية القوية على الأعداء الأمريكيين والصهاينة، مُثبتين أنه لا خيار أمامهم سوى قبول الهزيمة والاستسلام أمام شعب الله وجنوده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/78818" target="_blank">📅 01:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78817">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22771bd849.mp4?token=aJjojStJAikcLF1fBuna9n81v3aRA2m3gmBUEh5YPm2WFlfQGljiOuPh1_-cM_KTMM9Cmlg5EX5sxBhZsKNBz5JoGrG8dE2Qq-yPy9rCV09EJzT4iOYzK-rcQOHc1pMxclppAcX9DcwaMkOT2P-1JBbE_WHgT-qS8Fb7TybCWj16KINovJpUWYNhgPDb04uFHc-0b9V2NtHYuk-Azl_yiFmTdQYn8N-ma-4HsV8EqrrKotdz2t3TJZ9MSQfxJUzNhqOytOWXoREXTQeHnilGCxcBc70bwsm5ABxD5HRAqHVvvw0SNFIPCiA1l_8-bJsCrGhGOSlV9CHB3AiDUeRrlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22771bd849.mp4?token=aJjojStJAikcLF1fBuna9n81v3aRA2m3gmBUEh5YPm2WFlfQGljiOuPh1_-cM_KTMM9Cmlg5EX5sxBhZsKNBz5JoGrG8dE2Qq-yPy9rCV09EJzT4iOYzK-rcQOHc1pMxclppAcX9DcwaMkOT2P-1JBbE_WHgT-qS8Fb7TybCWj16KINovJpUWYNhgPDb04uFHc-0b9V2NtHYuk-Azl_yiFmTdQYn8N-ma-4HsV8EqrrKotdz2t3TJZ9MSQfxJUzNhqOytOWXoREXTQeHnilGCxcBc70bwsm5ABxD5HRAqHVvvw0SNFIPCiA1l_8-bJsCrGhGOSlV9CHB3AiDUeRrlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقف العمليات العسكرية بجميع الجبهات بما فيها لبنان</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/78817" target="_blank">📅 01:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78816">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وقف العمليات العسكرية بجميع الجبهات بما فيها لبنان</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/78816" target="_blank">📅 01:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78815">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏خام برنت يهبط إلى أدنى مستوى منذ مارس</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78815" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78814">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">أسعار النفط تتراجع بأكثر من 3% بعد إعلان التوصل إلى اتفاق بين الولايات المتحدة وإيران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/78814" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78813">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH9kFRpYHm9MslatpbZ2mhW7f5TZnjaLTgDEdBdQpvmBBJl-fB1lWY1jsu_O7kvwYxc_FNNVJG0hnMwFpT4jF1GcbOFbpgDpal_1h8gWFFJC7AABnzsyDyXXYY9cebUebrh0r5-KGbkYhxiMqOzPU50BBH8-oHfiUCrTB3ioxfhLR8mCg6YOxDROkmNbdI71rt6W4esyoX8NCTCqZyYDi16WvcAyZBimT-PJEsm7SLtJhpzT_WrS1f5WD3HWE3g-qi_4UpN8iJaBPiPeRWxn-4vXfViMRhS8FQZYRTJkz-Fefd332UYWLp20z2vsl979nCBm_4a4xwHuamByJYhi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار النفط تتراجع بأكثر من 3% بعد إعلان التوصل إلى اتفاق بين الولايات المتحدة وإيران</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/78813" target="_blank">📅 01:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78812">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇦
عمدة كييف:
انفجارات في العاصمة. قوات الدفاع الجوي في حالة تأهب.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/78812" target="_blank">📅 01:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78811">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني:
كانت تهديدات إيران الليلة فعّالة في دفع بعض بنود نص المفاوضات.
ساهمت بعض الإصلاحات المنصوص عليها في التفاهم، إلى جانب الأحداث التي جرت في لبنان وتصريحات القوات المسلحة، في تقدّم أعمال المفاوضات.
كانت القوات المسلحة على أهبة الاستعداد لردّ حاسم.
كما اتخذ ترامب مواقف وانتقد الكيان الصهيوني. وردّ حزب الله أيضاً بقوة وحزم على العمل الإرهابي الذي ارتكبه الكيان الصهيوني.
ساعدت السلطة العسكرية والتهديدات التي وُجّهت في إتمام صياغة النص ودفع بعض القضايا التي كانت تُعيق إتمامه.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78811" target="_blank">📅 01:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78810">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🌟
‏
فانس
: سأذهب إلى جنيف للمشاركة في التوقيع على الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78810" target="_blank">📅 01:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وقف العمليات العسكرية بجميع الجبهات بما فيها لبنان</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78806" target="_blank">📅 01:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
"
سيصدر البيان الرسمي لأمانة مجلس الامن القومي الايراني بشأن اتفاق وقف إطلاق النار قريباً".
‏
وفقًا لهذا التقرير، بعد الهجوم على منطقة الضاحية في بيروت، ألغت إيران مفاوضاتها وكانت تستعد لمهاجمة الكيان الصهيوني. إلا أنه في نهاية المطاف، وبفضل تنازلات قدمها الرئيس الأمريكي دونالد ترامب في اللحظات الأخيرة، بما في ذلك الحفاظ على وحدة الأراضي اللبنانية، وانسحاب إسرائيل من الحدود اللبنانية، والرفع الفوري للحصار، اقتنعت إيران بالعدول عن تنفيذ هجومها.
‏ كما تقرر أيضاً أن يتم تنظيم النظام القانوني للملاحة في الخليج الفارسي بالتعاون بين إيران وسلطنة عمان.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78805" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78804">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الله اكبر...طهران الحليف الذي لا يترك حليفه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78804" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78803">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
‏
تسنيم
: المسؤولون الإيرانيون سيتحدثون عن الاتفاق مع أميركا خلال دقائق.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78803" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78802">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8Ald28Am92ElBq3VbhIAF41z159U1tKk1LPGdp1D6xIYxgnYNoy1UOdvJu8vPNxow6GViOzKxB8ppHBzKs_a37ASv29vy8nyXEi81I6kEFJVo7inMpoOgT_-YUsAN3OtGwvAl30Tz3z4B8j2uJdv71Mvh7Q82PcTlISsrBGKFZTRi9L2bpIEDdRgcnmsnVssPWaZQGki084LAbks7p4rhShwb-wI8WXoAEumOmthfadwFaPdBlQ2ZnLUPmSHEa2iEtzJd6F7kJrAIXFcbM9yO3C8vnjHRQ7vea_-g9-CAfEeP_2Rsn0Ky_0uQK6ogCKzPrJEOBq5y2DqKOMiyuR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
: الاتفاق مع جمهورية إيران الإسلامية قد اكتمل الآن. تهانينا للجميع! أفوض بموجب هذا بشكل كامل فتح مضيق هرمز مجانًا، وفي الوقت نفسه، أفوض بإزالة الحصار البحري للولايات المتحدة على الفور. سفن العالم، أشعلوا محركاتكم. دع النفط يتدفق!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/78802" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78801">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نحن جنود الدين والعقيدة...لبنان لن نتركها وحيدة
#شاركها</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/78801" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78800">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
🌟
🌟
رئيس وزراء باكستان: ‏يعلن تم توصل الى اتفاق مع واشنطن وطهران بعد مفاوضات مكثفة، يسرنا أن نعلن عن التوصل إلى اتفاق سلام بين الولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية. وقد أعلن الجانبان الوقف الفوري والدائم للعمليات العسكرية على جميع الجبهات،…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/78800" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78799">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وقف العمليات العسكرية بجميع الجبهات بما فيها لبنان</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/78799" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78798">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
🌟
🌟
رئيس وزراء باكستان: ‏يعلن تم توصل الى اتفاق مع واشنطن وطهران بعد مفاوضات مكثفة، يسرنا أن نعلن عن التوصل إلى اتفاق سلام بين الولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية. وقد أعلن الجانبان الوقف الفوري والدائم للعمليات العسكرية على جميع الجبهات،…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/78798" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78797">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Peerx7D_hApUkkjjkEt2hWZqBQbXep0pMbsg-NbbgN7oeZhbSSALEA4ydeMrGZZyRR1z2UDlrYNJHYIAo39Eqtcc1zWymYN_zj_1bf8O67R1Oij83F1kflcljGzJ4lT8vm4KmUhSn26PyAzIlKUswXuk_ndGsOSxZW22My_1M32Lqsipl-ASwwVAUMYUqlZKOVpA_xJm4T61Cadt3MlW0ASCHYPLhg6tWNuwEuWmZ3Yi4HnSCNlunZ9tLDYvybLBWz1xbuJneNiVy-Id8RqR2j4LKZ2MXrSrXVKf8-np7lBwDPO1iLEx5_D3ZYvohxyU5xy4EnHxURhTWtMmQJvfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
🌟
رئيس وزراء باكستان: ‏يعلن تم توصل الى اتفاق مع واشنطن وطهران
بعد مفاوضات مكثفة، يسرنا أن نعلن عن التوصل إلى اتفاق سلام بين الولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية. وقد أعلن الجانبان الوقف الفوري والدائم للعمليات العسكرية على جميع الجبهات، بما في ذلك في لبنان.
‏سيقام حفل التوقيع الرسمي يوم الجمعة الموافق 19 يونيو في سويسرا.
‏نتقدم بالشكر الجزيل للولايات المتحدة الأمريكية والجمهورية الإسلامية الإيرانية على التزامهما بإيجاد حل دبلوماسي للنزاع. كما نتوجه بجزيل الشكر والتقدير لإخواننا في جهود الوساطة هذه، وللقيادة الرشيدة لدولة قطر، على دعمهم في التوصل إلى هذا الاتفاق. وأخص بالشكر القيادة الرشيدة للمملكة العربية السعودية وجمهورية تركيا على إسهاماتهما الجليلة في هذا الصدد.
‏بعد إبرام الاتفاقية، سيتولى الوسطاء تيسير سلسلة من الاجتماعات هذا الأسبوع. وستضع هذه المناقشات التمهيدية قبل التنفيذ الأساس للمحادثات الفنية وحفل التوقيع الرسمي.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/78797" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78796">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
ترمب يتنازل عن ابرز اهدافه</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78796" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78795">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏ترمب: سوف يتم رفع العقوبات عن إيران بموجب الاتفاق</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78795" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78794">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامب يشير إلى عدم استعجاله في إزالة المواد النووية من إيران، ويؤكد إمكانية حدوث ذلك لاحقاً</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/78794" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78793">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامب: الحصار البحري على إيران أكثر فاعلية من الضربات العسكرية</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/78793" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78792">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامب يشير إلى عدم استعجاله في إزالة المواد النووية من إيران، ويؤكد إمكانية حدوث ذلك لاحقاً</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/78792" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78791">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏ترمب بعد ما يأس
😆
: لست مهتما بتغيير النظام في إيران. -‏سأتحدث قريبا عن الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/78791" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78790">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
ترمب بعد ما يأس
😆
: لست مهتما بتغيير النظام في إيران.
-‏سأتحدث قريبا عن الاتفاق مع إيران</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/78790" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78789">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏴‍☠️
الإعلام العبري:
واشنطن تسعى لتوقيع اتفاق مع إيران يمنعها من الرد على هجوم الضاحية.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78789" target="_blank">📅 00:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78788">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇸🇾
‏
مستشار الجولاني:
أميركا اقترحت علينا التدخل في لبنان.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/78788" target="_blank">📅 00:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78787">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsJNA4gQbYcmpz6Tp4NXiZIu2VYrIaRGgN6Cq_9t65ZBW_Vi4EXVyqxoCwvyv0HT2WaKym-fRjw4bXLJBgvNlmkF7j_uR4IePohj8fRyhrzIn4164SowKZDpGCWymEsFVIeaKiLCrYtt7DM3j1-crP2KL4I3y1wvQzVh77dm3tFD4wUu0buYgFpxY7gL2X9hHFc0PZSoQg5rzOB1XAswHv2y94gFMGzQManJJ-jxR-LbarXs1VqZ_6-BujlEyEo-W8HrrRBCO6azKeB3jc0XX29Lz3e2eF_xUhI7Ri0dKqYLlKo7NfcK0C14rphk7fqp0_UIu5tNS2S-pTh4LfYa3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
لن تمتلك إيران أسلحة نووية أبدًا، وسيتم فتح مضيق هرمز للأعمال التجارية قريبًا جدًا!!!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/78787" target="_blank">📅 00:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78786">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be1f8c2a4.mp4?token=IbiGaM2kIw3Jy8ziO0Az1xLYWYaAe0jAOnWhIqpLs3N9KkKO0RPKCV3cB-3GBv2lCSE2NPO_TYZTTXaqdlW0bZUFJN4iPam899KgXNdmZvRvxMAryIPosb5imFD_5TbiRR7FEXc188zkZiGvO1lOzlz9xdEOTXAX4CCNDaBBF4uPiMN6D37v2G74qIm03boips0xGciucbUH5S-r0LtXui6S9YQCt5p_qe1jr5FKtCrNId1JG8CRgxeer7HTk8yZOTYbP0dZ5yX1As1NmmII6-Wn4yQl7YBYbYc4UM-NmgEro0IN-co0eysD9BFeCb8ubfLQjl6r_IRY7oHW-eeo91NcG5L9Vj1PRNnemR0AaH5vlmGARhKGcAB98C_tfATqX0rc2hEfDsGdOm8qDCuQS07U7h_in7i4AThISZ-AN7GgvqBGGsv5ed0cR60GzIWt61EmXzvfrdMousoBxuo49ABenfC1ftirCDTrP2QTOs33IWSdl2CJOBaprMBvKhihjMk3KcyYPbjnlfq9-uEpy-mald8ShtCC-r22mwVwPMBxoi-og3hVAu7VbNu__tDfQ4Zp0k1M9B9JP8ZGn6ENlwA2rXPPLfmIVpGhUvPFCyRnQTPXbYFCk-E0htC2BFZF0udTv358yGJJZILfcbyapM5cwKIKArMKt2tOCN4xVC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be1f8c2a4.mp4?token=IbiGaM2kIw3Jy8ziO0Az1xLYWYaAe0jAOnWhIqpLs3N9KkKO0RPKCV3cB-3GBv2lCSE2NPO_TYZTTXaqdlW0bZUFJN4iPam899KgXNdmZvRvxMAryIPosb5imFD_5TbiRR7FEXc188zkZiGvO1lOzlz9xdEOTXAX4CCNDaBBF4uPiMN6D37v2G74qIm03boips0xGciucbUH5S-r0LtXui6S9YQCt5p_qe1jr5FKtCrNId1JG8CRgxeer7HTk8yZOTYbP0dZ5yX1As1NmmII6-Wn4yQl7YBYbYc4UM-NmgEro0IN-co0eysD9BFeCb8ubfLQjl6r_IRY7oHW-eeo91NcG5L9Vj1PRNnemR0AaH5vlmGARhKGcAB98C_tfATqX0rc2hEfDsGdOm8qDCuQS07U7h_in7i4AThISZ-AN7GgvqBGGsv5ed0cR60GzIWt61EmXzvfrdMousoBxuo49ABenfC1ftirCDTrP2QTOs33IWSdl2CJOBaprMBvKhihjMk3KcyYPbjnlfq9-uEpy-mald8ShtCC-r22mwVwPMBxoi-og3hVAu7VbNu__tDfQ4Zp0k1M9B9JP8ZGn6ENlwA2rXPPLfmIVpGhUvPFCyRnQTPXbYFCk-E0htC2BFZF0udTv358yGJJZILfcbyapM5cwKIKArMKt2tOCN4xVC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عمليات قتل وتصفية لمواطنين سوريين على يد عصابات الجولاني الإرهابية تشهدها منطقة كفرتخاريم بريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78786" target="_blank">📅 23:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78785">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JctLIPF2E6DETri_3GTKjwjK3KlHeLF9oHZUtC2disQUDTa_4bxBFBATVmvnGQBEi2Fv_Pqx_xmJp36Nv9xIbRp10gVIP_E0uCivS3dlvBMZW1HgRjR-p8tIhdSvRGAQME08q9kH5Gdn-OcoLImqICmcPCGFnJ6_GPALPxCTajG6b4v97KFLDJgSQnu6JEK3SrPDU4ZXsfugiCqkZejSInIsIUucMRt7HMpCy5UGQqGyBW6qYdDuOED480WgTx7ioc0-zopv8YMKkiYeJD6VdgFp2UkbF4P6pibrRtQ9WPSCI04S_pss_hI0LjcTPylIr_2mGhDNgMPZWxR8aNVtJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
كذب السيناتور جاك ريد، الديمقراطي من رود آيلاند، عندما صرّح بأن الاتفاق الذي أبرمناه للتو ليس جيدًا مثل كارثة أوباما المعروفة باسم خطة العمل الشاملة المشتركة. ريد إما محتال صريح، أو غير كفؤ. كان اتفاق أوباما طريقًا لإيران لامتلاك سلاح نووي، بالمال وكل شيء، وهو أحد أسوأ وأغبى (ومن هنا الديمقراطيون!) الصفقات التي أبرمتها الولايات المتحدة على الإطلاق. اتفاقنا هو جدار ضد امتلاك إيران لسلاح نووي، وهو عكس اتفاق أوباما تمامًا. اعزلوا جاك ريد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78785" target="_blank">📅 23:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78784">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭐️
الإعلام العبري: تدرس طهران تأجيل ردها المخطط بإطلاق الصواريخ على إسرائيل لإعطاء جهود ترامب للتهدئة فرصة والتوصل إلى اتفاق إطاري محتمل الليلة.  تقوم قطر بوساطة المحادثات، حيث تفيد التقارير أن أحد المقترحات يتضمن إزالة الحصار البحري على إيران فوراً وإعادة…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/78784" target="_blank">📅 23:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78783">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
وزارة الاتصالات العراقية: موافقة الشركات المنفذة لمشاريع الـ(FTTH) على مقترح زيادة سرعة الانترنت للمشتركين بنسبة ‎%‎20 بنفس السعر  -الزيادة ستمكن شركات الـ(FTTH)  من تقديم خدمات ذات مستوى عالي الجودة مما يلبي إحتياجات كافة المواطنين.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/78783" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78782">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⭐️
الإعلام العبري:
تدرس طهران تأجيل ردها المخطط بإطلاق الصواريخ على إسرائيل لإعطاء جهود ترامب للتهدئة فرصة والتوصل إلى اتفاق إطاري محتمل الليلة.
تقوم قطر بوساطة المحادثات، حيث تفيد التقارير أن أحد المقترحات يتضمن إزالة الحصار البحري على إيران فوراً وإعادة فتح مضيق هرمز بدلاً من تخفيفه على مراحل.
وقالت مصادر إن إيران خططت لتنفيذ ضربة صاروخية في المساء، ربما توقيتها خلال البث التلفزيوني الرئيسي، لكنها أجلتها عدة مرات بعد تلقي رسائل مباشرة من ترامب.
حذر ترامب من أن أي هجوم يؤدي إلى دورة أوسع من التصعيد قد يعرض المفاوضات للخطر ويترك إيران مسؤولة عن انهيار الجهود الدبلوماسية.
يقال إن الرئيس الأمريكي يدرس تقديم تنازلات إضافية للحفاظ على المحادثات وتأمين اتفاق.
وقال مصدر أمني إسرائيلي إن رئيس الوزراء بنيامين نتنياهو توقع أن يؤدي هجوم بيروت إلى تصعيد وإخراج الدبلوماسية عن مسارها، لكن المفاوضات استمرت على الرغم من الحادث.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/78782" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78781">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAP-eIWM63KdJvV7YYcfJ8wzFqVLwplgvKlH3glYvYUvW5sufyX876Q7vt8pPWMlC1dgGFJvnX8wUg0heMwqrXHyUZLX1KWdUPH2fnHwwAYrZVbBPKssi-6td6Okwr7_i6fVkSCjVhRHyDosdSCp9YFnbGx_u4UTL75Ho5K4QSt7JAMOQUC-_scW5xE6H94bCfFKfBQqGeq6hdd98ES5hk84-yr6v8A0UfDn4ilAFfEeIMdQCjC3sedVtshjx76dGUFOUV6r6QvZHDPowI2C4JJCAW2asiz-BWWcutenK59IupduREHyD2j4TNWUssWv_9cexxHPJkuiC_4IrcZfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
أجسام مضيئة في سماء تل أبيب المحتلة.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/78781" target="_blank">📅 23:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78780">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
🏴‍☠️
أستهداف دبابتي ميركافا وآلية بوكلين ومستودع ذخائر دبابات لجيش الإحتلال الصهيوني في بلدة مجدل زون بجنوب لبنان.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/78780" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78779">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOMjArUJhTtJWriJk11Wz36P84veK0ZSSWHl143eDg0gLp_OITg-BZYwAdrblTHGdFodrYwkBEUmZWoH7wxttqc7nFrSR_xCcH9_ky3ZJTLZLLlam1f50uUfujnQ_t57f9vvJAt_fHcrCA8oQprRDbpdOgsfJ1s1f7QXVdZszXqJbPiip7BXUDuUrOWdU9NsqfKWK8ePSbJof_8S1lfrgDoMIKRBohMGZ6_e0ZWuU0qkN76wo-tDh7eru2oR4yg0mtAB2WjLm01AIjsFwK_teSXyFgUBcYdQHLcPVVdl5s70ZhPszLwWktcF4u2znJbOns6HiIvVbpBAGeALaGY4Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
وزارة الخارجية الإيرانية:
"بيان وزارة الخارجية بشأن استمرار جرائم الكيان الصهيوني في الهجوم على ضاحية بيروت".
‏تدين وزارة خارجية الجمهورية الإسلامية الإيرانية بشدة العمل الإرهابي الذي قام به الكيان الصهيوني بعد ظهر اليوم، الأحد 14 يونيو 2026، في العدوان العسكري على منطقة سكنية في ضاحية بيروت، والذي أسفر عن استشهاد وإصابة العديد من المواطنين اللبنانيين.
‏إن هذه الجريمة الإرهابية ليست مجرد انتهاك صارخ للسيادة الوطنية والسلامة الإقليمية للبنان فحسب، بل هي أيضاً انتهاك جسيم لاتفاق وقف إطلاق النار المؤرخ في 8 أبريل 2026 بين إيران والولايات المتحدة.
‏إن الجمهورية الإسلامية الإيرانية، في الوقت الذي تذكر فيه المسؤولية المباشرة لحكومة الولايات المتحدة عن الجرائم التي ارتكبها النظام الصهيوني والانتهاكات المتكررة لوقف إطلاق النار من قبل ذلك النظام ضد لبنان أو إيران، تؤكد عزمها على اتخاذ جميع التدابير اللازمة لممارسة الحق الأصيل في الدفاع المشروع عن النفس.
‏من الواضح أن مسؤولية العواقب الخطيرة التي يترتب عليها خرق النظام الصهيوني للسلام والأمن الإقليميين ستقع على عاتق الولايات المتحدة والنظام الصهيوني.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/78779" target="_blank">📅 23:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78778">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561b7e384e.mp4?token=t3JkWHXLblChfVoL5TmmQZLzbxNjIGCZtqN9N9pX75j5b8TvItXpNsfFbdQbvrxaw-vB1p-rHOIB-MX1NYexHQ6glOK4bIluBldU9s86_k_zLrLok1XaF1Dc_Qt7UUd8UJBM4vI4-SjMwIguxQZ-9PTiesHkiSCxLOKmGmhmzN1I3FFL9G8O_KaGRg8nihyC1F4E-B7FyQup7k00itHO4ckiZmGFeCLIrZ1P5IVCNy9FeqRtpLndmtLsqSsPUaKUT3RAwOx7_UwUe2vniCVcd00Tq254oKwxzdhK3tXAQfgUyqNDtlG42v_gPB5vHC13UkJ90v_t8T6PA_erebyPZzqwGYOS175h6cXO5wG2RjSqyf_2yAD95U0Yj_9CeZVUM5HZix3GsbNq358RrMfM2QV62p1lNdyUjCEvgqZgBRO0BjDLm2ZnFcc2eydj2hyi9wXLJGKxSEr_T-2SjYkDNUcv_i7i0aUShipVsLPPzLKezp7vaLX_Sa2-jeHs3OYpLhho6VuLawQGD6kthXs6Qi9b1hhTkj5e-iidoezJYpagm5gtOHCFX3LT2d5MApHHbBDe8ybvOOCYP7DOugCIOmQfU3b-cklXA88_C6jAAdIz_c6dPomnGsYVtns1QEeGl7EQ32oJcDc5lQLtnwtZh_1ZT1__MbOI3TQnjCD3dFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561b7e384e.mp4?token=t3JkWHXLblChfVoL5TmmQZLzbxNjIGCZtqN9N9pX75j5b8TvItXpNsfFbdQbvrxaw-vB1p-rHOIB-MX1NYexHQ6glOK4bIluBldU9s86_k_zLrLok1XaF1Dc_Qt7UUd8UJBM4vI4-SjMwIguxQZ-9PTiesHkiSCxLOKmGmhmzN1I3FFL9G8O_KaGRg8nihyC1F4E-B7FyQup7k00itHO4ckiZmGFeCLIrZ1P5IVCNy9FeqRtpLndmtLsqSsPUaKUT3RAwOx7_UwUe2vniCVcd00Tq254oKwxzdhK3tXAQfgUyqNDtlG42v_gPB5vHC13UkJ90v_t8T6PA_erebyPZzqwGYOS175h6cXO5wG2RjSqyf_2yAD95U0Yj_9CeZVUM5HZix3GsbNq358RrMfM2QV62p1lNdyUjCEvgqZgBRO0BjDLm2ZnFcc2eydj2hyi9wXLJGKxSEr_T-2SjYkDNUcv_i7i0aUShipVsLPPzLKezp7vaLX_Sa2-jeHs3OYpLhho6VuLawQGD6kthXs6Qi9b1hhTkj5e-iidoezJYpagm5gtOHCFX3LT2d5MApHHbBDe8ybvOOCYP7DOugCIOmQfU3b-cklXA88_C6jAAdIz_c6dPomnGsYVtns1QEeGl7EQ32oJcDc5lQLtnwtZh_1ZT1__MbOI3TQnjCD3dFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 01-06-2026 تموضع جنود جيش العدو الإسرائيلي على الأطراف الجنوبية لبلدة دبّين جنوبيّ لبنان بصاروخٍ نوعي.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/78778" target="_blank">📅 22:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78777">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt_aahaDKyawv-XGlHhnrwJ2FFhrjSkXlhkVbBbqsbG9ux6E_cqtWEIBtKcjIuqz6TDxdjcjLuldNy-ENITMPmhzWQzswuhUaTDKGMNe0oYJOlXGaWeTv8ZGpNNulMc7FjAWQP9NFj2sDPnjwiQQWKA8HkMJ5Edt6h-Wmnvb0tt4bj7JA3w_uFBGGxkQHcUlT8EmMA3_pubTxGX41_Lwya0uTbXhfW-GYcpsxswHhZYDEKtUSqX6-46fREnSblHAkc847m4sNah4Pek0Jzu0oXnMe-2rVKFfewb0s5-lOjNTO8fuFBWm86hLsQ7BNp3VpNnDvFMlBHGKi0OW7PKNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
ضمن سياسة بني أمية في اقصاء الشيعة واستهداف مقدساتهم..
عصابات الجولاني الإرهابية تهدم وتزيل جامع وحسينية في قرية الركة بريف محافظة حمص السورية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/78777" target="_blank">📅 22:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78776">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qh0LdaZTfB7Zjdr8voFHb2QKy3J2FTz7SRFs_O-qwra6qqYtTO7g9wnGSJi5Ibm-o58XQVIXluxoKZql-TV_q3F7C2M3JMtJ4wc1sIJtnZCn5Mxf89FB5SZ2kXdIL5MhkHNsjeZ8GtjUFR-OA0JZBLfNGJOddTbs5kYIlMoPRzAMuv628xURwKqOwgGj0i4z6YgxrF8-8rscrYe1D8QEP7hNe9dLMuCn2lzKDdCd19ElRiA0qte8-Va8e3zQJ1lsPRXx-PtcJJYMmIK-MXIIDzUaoW-EEMspN6BtqGULej-4YvjNIqbztG_tzDTt-NYWAXl4WfS--Se85u25zPAJGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف:
لن يتمكنوا أبدًا من السيطرة على أي جزء من قوات المقاومة بمفردهم؛ فجهود المقاتلين اللبنانيين الشجعان والدبلوماسية القوية للجمهورية الإسلامية الإيرانية ستضمن سيادة لبنان الحبيب ووحدة أراضيه، وستُحبط لعبة النظام الإسرائيلي المجنونة والمُثيرة للحرب.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/78776" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78775">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
الغاء جميع الرحلات في مطارات غرب إيران.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/78775" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78774">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
الغاء جميع الرحلات في مطارات غرب إيران.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/78774" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

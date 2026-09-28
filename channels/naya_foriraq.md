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
<img src="https://cdn4.telesco.pe/file/K70ru_ZiJhNEu9qoK98qlMCbUXoUbQ6sQCKaeTvqPBgTtF-ApxI35utNWooegNCYyvJiLk8hNXPb4vLHFCM0B_GL4bIFZ76qlqQKkXgHFHIY_jYvxoNWejuc3JEbFESgDbKyC9aFsuJT1RlsccCGnrgNEaC460NTM9-J9HsPvKj_XIn7z4w7NS6kwXdSGgbw4Z5YP-mia58GTGVijRAZNp2FfHyXtAqmokOAgcmMy7L_JSLrEN-AEdxcSBp1Lz4ZoF0EgLhgy6W0_nLicjlQ9vMuudq8gHXDdGtbDG4RGR9YqXbpRHI312GyEV81xY9ib234qItpiIVsC9xm6ygCzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 02:17:12</div>
<hr>

<div class="tg-post" id="msg-91927">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
مصدر امني عراقي لنايا
ممارسة امنية تجريها القوات المسلحة العراقية بالساعة الثانية فجرا بالتزامن مع الانسحاب المذل الأمريكي من العراق</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/naya_foriraq/91927" target="_blank">📅 01:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91926">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سطو مسلح على شقة مسؤول في منطقة المنصور " مجمع المنصور ستي " بالعاصمة بغداد .</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/naya_foriraq/91926" target="_blank">📅 01:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91925">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اندلاع اشتباكات مسلحة شمال بغداد بمنطقة سبع البور</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/naya_foriraq/91925" target="_blank">📅 01:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91924">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85b26a8e1.mp4?token=lBI0rDU_Kc3fH7LEXDEkipeJK9EhSgDUmcZv_w2n--dms9kSBlfytV3CLUxsVgviSjFLWbb58fvIKfVbfFdluFpPnrcEo7RbISjb1bt1HVPnAKBF6iq-_e9UDYBlbZsX2NYcaXqorW0CVrpCVxrZ1W0_uFPHueCXty4gWwgcnKf9ZU93OcFN6fkT9Qjd9EsFT5xR1k_sWVQzKSs9wJPh6RLTR44K4d4w8NJlX5cNHYaHeCzA-F75O2wYtHRiBCqeFJWnEl9hQkwy0RaCJEjyhQ67HiB0ZlR2t20er_JDe7Wm3wGGnb93OED9aUCrc6E6gKFlAcvUKh1dvmEnTp5TTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85b26a8e1.mp4?token=lBI0rDU_Kc3fH7LEXDEkipeJK9EhSgDUmcZv_w2n--dms9kSBlfytV3CLUxsVgviSjFLWbb58fvIKfVbfFdluFpPnrcEo7RbISjb1bt1HVPnAKBF6iq-_e9UDYBlbZsX2NYcaXqorW0CVrpCVxrZ1W0_uFPHueCXty4gWwgcnKf9ZU93OcFN6fkT9Qjd9EsFT5xR1k_sWVQzKSs9wJPh6RLTR44K4d4w8NJlX5cNHYaHeCzA-F75O2wYtHRiBCqeFJWnEl9hQkwy0RaCJEjyhQ67HiB0ZlR2t20er_JDe7Wm3wGGnb93OED9aUCrc6E6gKFlAcvUKh1dvmEnTp5TTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتحاري يفجر نفسه في محافظة حلب السورية</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/naya_foriraq/91924" target="_blank">📅 01:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91923">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
انفجار عنيف بخط الغاز في دير الزور السورية المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/naya_foriraq/91923" target="_blank">📅 01:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91922">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asmEKrwxekALS3yuOwrWdV51rM8DmwPCl4j3fZlpGtc4L22RXbWBe-WPk2dFU7qWyz_WG6sQlVhjOVwBo6yn5f7z0EKoPkuufUsbaTh1zwhago_1vPSWNetIuEcgdIc8_NE0BBRzlmZY_qn4YilY6yqu1GWXfS-xcKeLmjc2FYH1BmrvgoQpGnjtD0vUl4b0OcptdyMUvmHCvqFv4l48y5VTAUPUAunPvISh54stciR5JDLJG61fHXWfxfL4uv4UkziuMvUEXwOTesdc9W49asqxGGfJHhzPuf-fKhsNGscPJp9ImMck0wDyvxSvOpUPhojcgszgSBPJu9qecFe0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يختلف على صحيفة اكسوس اكبر الداعمين للجمهورين
‏ «نشر موقع أكسيوس للتوّ خبرًا مفاده أن "ترامب" عرض تخفيف العقوبات وإعادة الأموال المجمدة إلى إيران. هذا غير صحيح. لم أعرض عليهم شيئًا!» خبر أكسيوس، كغيره من الأخبار الكاذبة، مجرد خدعة، تُستخدم فقط لإشباع هوسهم بترامب. عليهم سحب هذا الخبر الملفق فورًا!</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/naya_foriraq/91922" target="_blank">📅 01:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ea1HYrJ76By3CwtOCKJhpen8Px8jFKXAJEv_0-cfFUTV_Ov-RDijvOdeOi3TuCx5mCsjCA3-6uV03UlWvRYbCoCp6wIphIr_5qk1isDa2rPm6m-r0o9IrVXXtbvvuSq5zY0sr2g1dABOa3-wrJglrsE3U88dxucRTlBhxIno-3m-lMFMYs6AEfHnKpm2Fkk_NQa4kT5UyyLCQr3hWWqpX60RlumI6XEZjoZms-VYdvh4yP6cHPsDAfoUYY_EhYoED9I4l0qNn2pxSa4RVMgMKgiwRosW40ULm8KWPEO56BVi_kY_05P9i1OTUfAbI9DxSX29h9ucQ6EmJRGYM-XnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqGtJxDCP4eSdXXnOXZ8j6_f92syo8F21QrviQxYeoEOkWBsRzr53gBVhRGAssYX9L-5ueH870waZueUhFWIY0b36Bi5itWy8OYVUTrwM7b4zk7qf7Xhqk1Je2OxRjcSVoJcgAVkYoSC6yTw2XMjjcWpXp05K-tcEsPXzrgIXlxYZFrk8_RQ89vnU8tfdhMKuxnXtMQf9KxqZAnTipTcSCyQUuCJhYiCykdf9WxUoZf0_AnQESxjltzkanFt4zgMYFd5sLFW4nGPEwwkcHUSXT6d1tXL-UgPNaD6cNpNPk03AmLcnZNA8z3xkMxYZJCvu4nDOEvwefRxpygHm_IFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5YAoWwH1gzSTD_JCXtAHbFTxMt55BySf9anXsiZ1ZOeLybHrAMUcSb2n6NXhDpbp_fIoXeWv2NMvDgSJKpaSMMKoj0Im_klJmArLUAvKeoOZzyztNY5bi-HVfnfgTkqApdxLE8zjachsj1wgM7toeRVUwdUxr43mAqva4Dfs08dHeweWlaovUQncv9lw2esTaJwLzqsdM_-0idXdDluNdJD1t6mGIIIE3dc4DJAKYV4sxS6-PP9a8Q9lCGngdnzfmxZruStj6GpCUv0C72lRVMU5HJhs-zpCxE8DI8JqRisuq8SQt5FsZAK-cRd78dc0wvb9Jxvojs3IvIE3hFpqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">البحرين: مسيرة لأهالي الهملة تُحيي الذكرى الثانية لاستشهاد سيّد شهداء الأمة وتضامنًا مع السادة العلماء وكافة  المغيبين ظلمًا في السجون.</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/91919" target="_blank">📅 01:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91918">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاناشيد المقاومة</strong></div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/naya_foriraq/91918" target="_blank">📅 01:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91917">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromأثر</strong></div>
<div class="tg-text">ضليت راسم صورتك انسان
ذري، غفاري ومن جبل عامل</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/91917" target="_blank">📅 23:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91916">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇱
🔻
وكالة أنباء الإمارات تعلن رسميا زيارة نتنياهو السرية: استقبل رئيس دولة الإمارات نتنياهو رئيس الوزراء الإسرائيلي يوم الأحد.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/91916" target="_blank">📅 23:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91914">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات في مضيق هرمز</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91914" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91913">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات في مضيق هرمز</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91913" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91912">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صافرات الانذار لا تتوقف في نجران</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/91912" target="_blank">📅 23:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91911">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات تهز سعودية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91911" target="_blank">📅 23:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91910">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات تهز سعودية</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/91910" target="_blank">📅 23:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91909">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
القوات الامنية تعتقل المدعو  علي الهذال بمنطقة الجادرية وسط العاصمة بغداد ؛ الأخير يمتلك مقر وهمي باسم حزب الله في العراق ؛ مذكرة الاعتقال تمت على المادة ٤٢١ المختصة بالاختطاف والأخير يمتلك مقر ابتزاز وخطف مدعوم خارجيا لتشويه سمعة المقاومة .</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/91909" target="_blank">📅 23:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91908">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">▫️
زلزال بقوة 4.9 درجة يضرب اليابان.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/91908" target="_blank">📅 23:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4-tkZZXbpkgKXiJvVgaYu6v2xtk_oQ40KEf4pP9xO4Xn6lTZ_mMEj27zqWqdDuAfSrxDAAltSFGVxbKQ7QkSVhIh_n2LHd5j9Do7NtZhbCZEisVk9Ods6x6So4zXsjl8QCRvMqdPiTKc-LjUoOWHbo3GmgAHJedYDDh5isIvOKJnvcCBUmxIOy5dPjvmtiGIESvBByEGhALRXVPQn1ath244SUmbXYsM2D9Q2y2HCJkm06Aohg7IEvibTfrM4ATvxxmHJQmD2ZpwMhKMlFlIBCsP2tHfyG_bRCj4097bggysleJkPpTXtteut11upmQXwqd5cjALYQRDhLw5mmEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مسئول امنیتی «ابومجاهد العساف»:
در صورت ادامه محاصره هوایی ایران پس از اول اکتبر، مقاومت اسلامی عراق پرواز متخاصم را در آسمان عراق سرنگون خواهد کرد
روز سی‌ام این ماه با جشنی مردمی برای بزرگداشت اخراج نیروهای اشغالگر آمریکایی و ناتو از عراق برگزار خواهد شد و خروج کامل این نیروها را گام نخست برای تحقق حاکمیت کامل عراق دانست. او همچنین دولت فعلی را حاصل توافق سه‌جانبه‌ای خواند که برخی پشت پرده تصمیم می‌گیرند و به نخست‌وزیر هشدار داد دولتی که در خدمت مردم نباشد، ساقط خواهد شد.
او اعلام کرد اگر محاصره هوایی علیه ایران پس از اول اکتبر ادامه یابد، مقاومت اسلامی عراق آسمان کشور را زیر نظر خواهد داشت و در صورت نقض آن توسط پروازهای متخاصم، ابتدا هشدار داده و سپس اقدام به سرنگونی خواهد کرد.
@Naya_Press</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/91906" target="_blank">📅 23:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91905">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">.
♦️
اين ما حلِتْ امريكا حل الخراب
🎙
وَدَّ الَّذِينَ كَفَرُوا لَوْ تَغْفُلُونَ عَنْ أَسْلِحَتِكُمْ وَأَمْتِعَتِكُمْ فَيَمِيلُونَ عَلَيْكُم مَّيْلَةً وَاحِدَةً</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/91905" target="_blank">📅 23:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91904">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
🇮🇶
الحاج ابو مجاهد العساف: ستراقب المقاومة الإسلامية الظافرة الأجواء العراقية للتأكد من عدم انتهاكها من الطيران المعادي، وسننذر أولاً، وسنعمل على إسقاطها ثانياً.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/91904" target="_blank">📅 23:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91903">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TV_mECnTZ_lJqWrHBsH8dAUPcPG0w2bDU4dWxzJRgwtzLiHBX6Av4PfB8FrS6axmi9mMzCrfSwtCdb3kQoJWJUC3OKY0wNSlzLrdb-pOyNSa989TBzaTkg5GCjkTgrFH9f2i9iqntcKJeoqTJ-5BB_RkBJF9X2kW9Qs644VHE42bXFDbmSpnTng17WvSaT-ARHUjw0LDEpPG-wer3UoWlB7dLloicwOhrcA3k1LjtLqz9Ujj8On7p3nvoiMYjyOaX85ISdXG0Cf4-Zf3FBNXCPwQQ4qIAbhvBSMr2TD8UU8wKIgQ9LjJNHTsfhWHKBobK2IiS8_Ce7DfPSyyC7m83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇮🇶
تنويه: سيصدر بعد قليل بيان هام للمسؤول الامني لكتائب حزب الله ابو مجاهد العساف.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91903" target="_blank">📅 22:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91902">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
🇮🇶
تنويه:
سيصدر بعد قليل بيان هام للمسؤول الامني لكتائب حزب الله ابو مجاهد العساف.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/91902" target="_blank">📅 22:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91901">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG1nAmbNXZpH5QI7ht4ZQEAG-2i44r-B9Nj3ezWfQTsquaHDSgQE3We-9YhHiLaP3bCxdzUvas_YFu-50sD-MJvuFi_TIkyWBBZa6i8vQIOEsMhNWFiMD-3rAxVCxLOY9pZBWcxdZIy0HFqCQXLTK81TvKvBeSkRmJKkOrB20qznBNQIhuE45SwGG_XYTZZ1PSdFYNWXfcVdYziu5YGulwKWh2EVTdmLa3Wk7RIeXxpZtKothDyyqccyZPY4KxJvwAVeH1VdZ73iGvQVBWLlRHSDfY-pPUOuZVg-D-ynEdIIq_oexQ45jYAtsbyvpAelsd8Togs652FWnvjgwRVfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🔻
‏خلال زيارة سرية إلى الإمارات طلب نتنياهو من محمد بن زايد نفي التحذيرات التي صدرت قبل 7 أكتوبر.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/91901" target="_blank">📅 22:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91900">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74652b403.mp4?token=o6Ia3ldq5xdMCi2AqyeBdaAOenpbCN0UEN7hGzZQRfjm2psQP8dhuoUHi99Z__45PpNYoQruQyL1CLCIpvtgatCoIo05egJmdIaxwPmv_eGUmpme_ffWWLVNWISujyz_6Md8gzF0VmEYPTuP4_hN9iBLONX-bi1WXB4dn-8YrrEN5uBHmLpUWekuz46S4FupeOPJo1pePq_xClvp5FyK5BSz-olRiHzATgX7EL57VQOXJKA7uSBeT9nBi9A_DY9RvwqCXZ-FZ2M6F3cWjjnyaKDyO9iAG4mZLOWhUfXA3kD4dyjWTOpgrvdh_YA9fQArB51XLSyfynR4hoAS2hHEPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74652b403.mp4?token=o6Ia3ldq5xdMCi2AqyeBdaAOenpbCN0UEN7hGzZQRfjm2psQP8dhuoUHi99Z__45PpNYoQruQyL1CLCIpvtgatCoIo05egJmdIaxwPmv_eGUmpme_ffWWLVNWISujyz_6Md8gzF0VmEYPTuP4_hN9iBLONX-bi1WXB4dn-8YrrEN5uBHmLpUWekuz46S4FupeOPJo1pePq_xClvp5FyK5BSz-olRiHzATgX7EL57VQOXJKA7uSBeT9nBi9A_DY9RvwqCXZ-FZ2M6F3cWjjnyaKDyO9iAG4mZLOWhUfXA3kD4dyjWTOpgrvdh_YA9fQArB51XLSyfynR4hoAS2hHEPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إذا أردتم أن تروا الفوضى، فدعواهم يستخدمون سلاحًا نوويًا لتدمير مدينة. أنا لا أتحدث فقط عن إسرائيل وأجزاء كبيرة من الشرق الأوسط. دعواهم يهاجموننا بسلاح نووي، من أجل كل هؤلاء الأشخاص الحمقى الذين يعتقدون أن هذا الأمر مقبول.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/91900" target="_blank">📅 22:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏المراسل: هل حادثة قاعدة سلاح الجو الملكي البريطاني في فيرفورد مرتبطة بإيران؟  ‏ترامب: ربما، لكنني أقول إنني متفاجئ من قيامهم بنشرها. لم أكن لأفعل ذلك.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/91899" target="_blank">📅 22:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
‏ترامب: سننتصر في الحرب على إيران قريباً جداً، وستنتهي قريباً.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/91898" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59404fbd6.mp4?token=uwI4ivKlzr_0DJU9u3xZ7VKWCpqHoMsd-cq5a_id7HRijGajgCzLJabFuMI7NBqHxS1JG8WMJpuZhiyJB8bgnM4WAbDWdvBJyBBIHNuyAyfMljfwTf0R6wNoJcSzAOLuGnKm_oH5xJRnW9kp_cGv51Osz1flnw6lbGOYTRYi_rMBzNAULope05K-nowhLHxC_3Ly0vZS9Vp4BazhWdCgVQ5eaUrpJ0uSdYreYsNnCJrcu0B0hiOMiEP7NzKHTzWNW-ZeixJ16xj6NrxfudxiT492szIIElCz-ayFn0ks3Y_KAiaeY0qOBBQHM8mTkPeLTdORBvO7LsZo7K-XE55zCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59404fbd6.mp4?token=uwI4ivKlzr_0DJU9u3xZ7VKWCpqHoMsd-cq5a_id7HRijGajgCzLJabFuMI7NBqHxS1JG8WMJpuZhiyJB8bgnM4WAbDWdvBJyBBIHNuyAyfMljfwTf0R6wNoJcSzAOLuGnKm_oH5xJRnW9kp_cGv51Osz1flnw6lbGOYTRYi_rMBzNAULope05K-nowhLHxC_3Ly0vZS9Vp4BazhWdCgVQ5eaUrpJ0uSdYreYsNnCJrcu0B0hiOMiEP7NzKHTzWNW-ZeixJ16xj6NrxfudxiT492szIIElCz-ayFn0ks3Y_KAiaeY0qOBBQHM8mTkPeLTdORBvO7LsZo7K-XE55zCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب
: سننتصر في الحرب على إيران قريباً جداً، وستنتهي قريباً.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91897" target="_blank">📅 22:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
محافظة البصرة:
بدأنا الاستعداد لاستضافة خليجي 28 على ملاعب البصرة وذي قار.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/91896" target="_blank">📅 22:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91895">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
🇮🇷
الخطوط الجوية العراقية تستأنف رحلاتها إلى المطارات الإيرانية عبر مطار النجف الدولي.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91895" target="_blank">📅 21:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3dc67a530.mp4?token=BA1rlUt4qszN1i7rGDajhC3W-x1_JNR2U9etFcwqztISkpW1fn9ZKVAMJqFgQzZENqtn9eqFYGEBxduh4nw5Un0PecPmVa9KoV1fXShk9Suw4SK5dBSxe0nCDWZ3HhWQrVHL8xjM7AtbaXKhYE96vwSbD-5V1-4SEWy77CgkQWrht8zwvtM9BTmLX4nr6UrkdLqspS6ijr-3xt3wfklptUlC6wiwJQeS6jfn_3g7kOwpEcnLNhRGEyTq9vL4ROsBeVm9StpRShfl1hS2C2H5ZnSR8AkasIpspiteEe9PBfWFPrlLCRHP44gpxFLuMsbQXb4040xYaShZkHYhZGn1Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3dc67a530.mp4?token=BA1rlUt4qszN1i7rGDajhC3W-x1_JNR2U9etFcwqztISkpW1fn9ZKVAMJqFgQzZENqtn9eqFYGEBxduh4nw5Un0PecPmVa9KoV1fXShk9Suw4SK5dBSxe0nCDWZ3HhWQrVHL8xjM7AtbaXKhYE96vwSbD-5V1-4SEWy77CgkQWrht8zwvtM9BTmLX4nr6UrkdLqspS6ijr-3xt3wfklptUlC6wiwJQeS6jfn_3g7kOwpEcnLNhRGEyTq9vL4ROsBeVm9StpRShfl1hS2C2H5ZnSR8AkasIpspiteEe9PBfWFPrlLCRHP44gpxFLuMsbQXb4040xYaShZkHYhZGn1Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجار عنيف بخط الغاز في دير الزور السورية المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91894" target="_blank">📅 21:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91893">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
الاعلام العبري: صواريخ اعتراضية في مطلة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91893" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91892">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSXJ_qSlPFXpDgbZtBQUAnyLxj5GwXWWHQ3c_y_kaWIbM4PCOrzYwtvnQ0dyKNRUzI5RzQ2H0_JF0NJQsbiLmuO5mVxaDyAq1D-W48rFDTQX6gEL7s063d5Exud4y_3jIITK49T8Ac-sHQ7VmSH1ssScsLBku-z6BN9lY8ur2uGvvt3Hng0nvNH-02sHzGSISJad3EDNgUOmFaeViBogZdd_uFCMlzagfD88CoHVIHilPNmhMsFQRTUt5KkHAAOO3WwHHA_ObrK7Vc4qFSAAvaQRBAKzzmGE9bjL2KR1mJcBcSCv4KurDlgTSXSKuCMJ7-jNbdQFzwoRCLxT4_jExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سيادتنا_لاتفرض_بالحظر</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91892" target="_blank">📅 21:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91891">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏الولايات المتحدة تدرس إمكانية التنازل عن العقوبات، ‏رحلات جوية بين إيران ومدينة النجف الأشرف في العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91891" target="_blank">📅 20:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91890">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
صواريخ اعتراضية في مطلة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91890" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91889">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
‏
مسؤول أميركي:
نجري محادثات إيجابية وبناءة مع إيران عبر الوسطاء.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91889" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91888">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 38 غارةً جويةً وصاروخاً من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وجيزان استهدف العدو بها محافظات تعز وصعدة وحجة وخلفت شهداء وجرحى من المدنيين بينهم نساء وأطفال.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1123 غارةً وصاروخاً.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91888" target="_blank">📅 20:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91887">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
الرئاسات تؤكد دعم مطلب الحكومة العراقية في استثناء مطار النجف الأشرف من إجراءات الخزانة الأمريكية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91887" target="_blank">📅 20:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
الرئاسات تؤكد دعم مطلب الحكومة العراقية في استثناء مطار النجف الأشرف من إجراءات الخزانة الأمريكية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91886" target="_blank">📅 20:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91885">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇸🇦
السعودية تستأنف تصدير النفط عبر خط الأنابيب الشرقي الغربي بعد إجراء الإصلاحات.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91885" target="_blank">📅 20:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
الرئاسات تؤكد دعم مطلب الحكومة العراقية في استثناء مطار النجف الأشرف من إجراءات الخزانة الأمريكية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91884" target="_blank">📅 20:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
ترامب منفتح على تخفيف العقوبات المفروضة على إيران مقابل "تقدم ملموس" في القضايا النووية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91883" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c474fe6c26.mp4?token=nUYAfpaDOhlGGUUIlno_k4UP52_cGps6bkU5AYq3buFxjnTlURSxX9KBsgsAifzTO1C-ioHV-tIeqXcO9LFGWUNt4D2QCf725Bv19hK7HMvF3a4H5s6BnKgR7HiArQhYp065BCWQg8BOKq7iBjSVya04rgtHJbjS9qFaATcAhQ3_66XjY3u3GoOp3W9NToQufnJ8HljRoj3JDMuWHunblHiVpxQ-fXh0KbHo1TTtuuoXqplO0JCq4fY1tCBOA8t3QpEPH4DsbXxkS3HPg45k6n8_aCGtBFC3Npr5blUsepHhFHjHA-_5Mr2767WGgfl4S1edMvOvOVjA7suQZo7Idg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c474fe6c26.mp4?token=nUYAfpaDOhlGGUUIlno_k4UP52_cGps6bkU5AYq3buFxjnTlURSxX9KBsgsAifzTO1C-ioHV-tIeqXcO9LFGWUNt4D2QCf725Bv19hK7HMvF3a4H5s6BnKgR7HiArQhYp065BCWQg8BOKq7iBjSVya04rgtHJbjS9qFaATcAhQ3_66XjY3u3GoOp3W9NToQufnJ8HljRoj3JDMuWHunblHiVpxQ-fXh0KbHo1TTtuuoXqplO0JCq4fY1tCBOA8t3QpEPH4DsbXxkS3HPg45k6n8_aCGtBFC3Npr5blUsepHhFHjHA-_5Mr2767WGgfl4S1edMvOvOVjA7suQZo7Idg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار عسكري في منطقة اليرموك بالعاصمة العراقية بغداد.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91882" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91881">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">العراق سيد نفسه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91881" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
انباء عن اطلاقات صاروخية من ايران.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91880" target="_blank">📅 19:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔻
مقر خاتم الأنبياء المركزي:
العدو الصهيوني الأمريكي ظن أنه بإقصاء "سيد المقاومة" جسديًا، ستنهار دعائم المقاومة، ولكن حسابات العدو، مرة أخرى، باءت بالفشل.
جبهة المقاومة لم تضعف فحسب، بل بلغت مستوى من التكامل الاستراتيجي الظاهر والخفي، ومسيرة الشهيد السيد نصر الله مستمرة بقوة في لبنان وفلسطين واليمن والعراق، وفي أقصى مناطق الجغرافيا التي تمثل المقاومة والسعي نحو الحق.
القوات المسلحة الإيرانية، إلى جانب مجاهدي ومقاتلي المقاومة الإسلامية، مستعدة تمامًا للرد بشكل قاطع ومدمر على أي تهديد يواجه الأمة الإسلامية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91879" target="_blank">📅 19:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91878">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPvk3a0jQna7B-BtrgVhWCL6JclaPqLLdKslo9DeBGrBu_i1FDoi5_r56HreERVCk5Oh2YFTgnNzxfbOYy8PQu-TfqGP7tX6XBfk1osymisBLn-EWso5v8W2fs6PyyNkcLctDklSpMXYSc_mAMbpgu6L7R0Jv7JESqaSWpLOSAO5B-o5NDZ11BT62X0zvFteIp33SZ7IHUd2ljJBkDL3E_wTMiT6-rMghge9w73dWz2cn50SfevOEm8Ay7gz7Y8iFyCkYXzlVOuR1YtAlP3dlVH1DEFeGh6KLX0_PRRVq42wNA0e-vCRc_4C_dlaZGhjvj2NzdVpKIkRjbq53beQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزارة الاتصالات العراقية تعلن إعادة حجب لعبة «روبلوكس» اعتبارًا من مساء السبت المقبل.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91878" target="_blank">📅 19:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91877">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/91877" target="_blank">📅 18:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
‏
ترامب
:
المشكلة الكبرى هي تفجير مصافي النفط في روسيا. هذه ليست مشكلة شرق أوسطية بالمعنى الحرفي، بل هي مشكلة روسية في المقام الأول، حيث تتصاعد حدة التوتر بين أوكرانيا وروسيا، وتقوم أوكرانيا بتفجير مصافي الديزل في روسيا. لقد تحدثت إلى الرئيس زيلينسكي وقلت له: "يجب أن تخفف من حدة قصف المصافي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91876" target="_blank">📅 18:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇱
الاعلام العبري: سافر نتنياهو اليوم إلى الإمارات العربية المتحدة للقاء الرئيس محمد بن زايد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91875" target="_blank">📅 18:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i691f1xvlPmw_yZ_J2D8dngtXD4er-LNk5lJhJ6tmZndIBRx18dlOio6ciKjNSKu2fbape_75xQD5BcJZ9ugFcNUQ-9nU3MLy5TuAkox8pAAoISqeP5SDKV2DSTFiVLOLfAUkqYWzBbfyX87oBYEO7-LiebccjUr-6BA6h2LviC2msWSiaf4CT_zWknpWukugHx-0sbWXGlxdqSQ6AHEFu6La2zy1TRfTsKlGOe4muZzU_HnjRRBHdleDLYl7GEk4DrRpQUWBIe72CFN3RvvYIiTtCQ_EOqWoprzB6PuDUVNMgmcSuGcsjADhF4MNhLFJCYUS_xLC4OCIcQW8CW24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العراق سيد نفسه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91874" target="_blank">📅 18:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇱
🔻
مجموعة من الشباب أثناء تجولهم في محافظة القنيطرة السورية تلاحقهم طائرة مسيّرة وفجأة أثناء تصويرهم تطلق المدافع الإسرائيلية في المحافظة قذائف باتجاه ريف دمشق.
جيش الاحتلال: كل هاد مشان صحتك يا غالي
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91873" target="_blank">📅 18:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833eba5bb5.mp4?token=NbzAwzHkf4vx6sj5ldvDjX7arhNFIQzc3xLwMtIfw57dEiLk0eLM_7ofWT_7qNEZxrqfXAmgo2hTtUKF8pJbFEDE8LQ-1bhD4e8X1oO9WKIC_oz_ykM1sZAaQPXylNVILrXMLmiIihUdGb9AL7HwN-1_da3qRV6qAKC_WDcJTNFt3sA2ZgcPwzbWUkcfxmVeWwCvAMI6Dmmo358GPNZ9vLFbUXIi691HXwo2ewaSXli8icEUXR1nkRLDVhx01Fvmx51UUaht5UeR6qrPfZTX0jN_bUyYhyCPY5MDZIUKzo3uOdESWhQKZWal3a-xTBlb1UKcs0KUlPRF_kWhb84ErA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833eba5bb5.mp4?token=NbzAwzHkf4vx6sj5ldvDjX7arhNFIQzc3xLwMtIfw57dEiLk0eLM_7ofWT_7qNEZxrqfXAmgo2hTtUKF8pJbFEDE8LQ-1bhD4e8X1oO9WKIC_oz_ykM1sZAaQPXylNVILrXMLmiIihUdGb9AL7HwN-1_da3qRV6qAKC_WDcJTNFt3sA2ZgcPwzbWUkcfxmVeWwCvAMI6Dmmo358GPNZ9vLFbUXIi691HXwo2ewaSXli8icEUXR1nkRLDVhx01Fvmx51UUaht5UeR6qrPfZTX0jN_bUyYhyCPY5MDZIUKzo3uOdESWhQKZWal3a-xTBlb1UKcs0KUlPRF_kWhb84ErA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تحذير جوي في محافظة لوبلين ببولندا خوفا من هجوم روسي محتمل.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/91872" target="_blank">📅 18:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixv3Bz3UspZ8KJgS_r_MbvXjexkJzvl12LQicycBYONa9jclqJvduz_3rUY0ZetcBJ7rtzVB2g9jIcaiMf00GurUQQ5858PYrWgpnqpjNquHr0Q7kN1BnlPjAxMA35sR4xoEN8ODwy6KloNHZTslI7p_0eExbV1ABEzt7TTMy2h85ZXPIZRbTZefiIvUYeh8TzBp-5ZmwN1wUE1WJspq2N5qwjVLMrO8X_daZIQ5Dx_tIuttXqGjxt2vVi2CJfJIRv1ICYLHUXNRe99MqmUXKOeqTgmSdrOjchfdvZm_SSwsI4vAiKnWmkz5aRkQ-EIRM3F3nsRUVbkvffKdJ05D_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سيادتنا_لاتفرض_بالحظر
🇮🇶
البصرة تنتفض ضد قرار الحضر الجوي.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/91871" target="_blank">📅 18:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e39cfc2c9.mp4?token=QMnnT0iWoHWsgOw9J_LkurT_RaCjSnCOat-pdFVL1T5nQPl2yO--kfalaFdquRQ6t34Z-4eEFh0cMs4XA5pCNw6JVvai4KRuHuEcWRmZ1OyIdbZr8VA39YC1a9pLRkWb8C9QTa7T-vemFt-iFYD9GNVAfbmzAs0u345NguExcpAg0cAokmNmD3YorKFhfmZ0XtjQYe-ghG4KXc_OSNyfNnAYbGKrx3B1JUIyUNKjYo_93yprcVjOaHP87z4KuCKpZUS0bmO2ebE7fuOTdKKmNhQFWjJPe-z9yqnyNH9rm6Aj8gL79fZyEG4fwKLlcTP95RZGELzhMauQO35xsJpRlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e39cfc2c9.mp4?token=QMnnT0iWoHWsgOw9J_LkurT_RaCjSnCOat-pdFVL1T5nQPl2yO--kfalaFdquRQ6t34Z-4eEFh0cMs4XA5pCNw6JVvai4KRuHuEcWRmZ1OyIdbZr8VA39YC1a9pLRkWb8C9QTa7T-vemFt-iFYD9GNVAfbmzAs0u345NguExcpAg0cAokmNmD3YorKFhfmZ0XtjQYe-ghG4KXc_OSNyfNnAYbGKrx3B1JUIyUNKjYo_93yprcVjOaHP87z4KuCKpZUS0bmO2ebE7fuOTdKKmNhQFWjJPe-z9yqnyNH9rm6Aj8gL79fZyEG4fwKLlcTP95RZGELzhMauQO35xsJpRlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقفة احتجاجية في محافظة ذي قار جنوبي العراق رفضا للمشاركة في حصار الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/91870" target="_blank">📅 18:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91869">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266c2f95a1.mp4?token=KZXPnVN7naKHE0p0A5W-FTTkFYadD3jQdJUk-Q3BJUDhDw-28WsHfOZ1yCN7ifKgxN26UaFuEU13w_2ERTKBKxvIx9pUpijcyXrFmRHbxiAVd1Z11mjYirUJDIEDJ1NZYapJWnP1D-lm-ixWPE_EjDjB8pfsHh_CI0kaPCsukLgEk1l09SuuxyKhUDfYCMSDUP6sjS2A4upGrOyyDpHLD4oyZNO0YA4C09Aw0ifAZJdu6R5OtTIKxEtCOIG0QrH6M74PoU5-hl6D8n_biXlUXFeZ5YLVF76-nzDl20m20yxELw3LIS6sPq5YzW7JAWCsZBRM3SkKQtDOlWVP8aywVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266c2f95a1.mp4?token=KZXPnVN7naKHE0p0A5W-FTTkFYadD3jQdJUk-Q3BJUDhDw-28WsHfOZ1yCN7ifKgxN26UaFuEU13w_2ERTKBKxvIx9pUpijcyXrFmRHbxiAVd1Z11mjYirUJDIEDJ1NZYapJWnP1D-lm-ixWPE_EjDjB8pfsHh_CI0kaPCsukLgEk1l09SuuxyKhUDfYCMSDUP6sjS2A4upGrOyyDpHLD4oyZNO0YA4C09Aw0ifAZJdu6R5OtTIKxEtCOIG0QrH6M74PoU5-hl6D8n_biXlUXFeZ5YLVF76-nzDl20m20yxELw3LIS6sPq5YzW7JAWCsZBRM3SkKQtDOlWVP8aywVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من امام بوابات مطار النجف الاشرف الدولي</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/91869" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91868">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2cfc66ea5.mp4?token=dMi0SVGUsFb3caSZOkqWDsZF9tjlSHdajRXKYOKuljpqyf7VCri-mk4q5sbQ7j-lBz2DyjXKWs-TJE1py0q82l1xeNG-23-MnbQ9l39f2CkKaWoH8q_-l0PYoq2nL3U4S96wtTw02IePvy1lMFv3kLo2xd4lEr5EyCMCR1lhn3OX-Oe1U1hz7QI7ai__uSnDiFepFJwPxkWnB2Fyw65nrHhgqHDsEUhm3BVDsp8qzimbMouFUVjhOBt_iQrSHRmfwMj5VHVrxrDCzahukUMa-XjCCtFYpxJSSd0nAdW9kE5yktk9TVkogk1_wROVG7XkR3WS7PEs8_iangTcQ3An4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2cfc66ea5.mp4?token=dMi0SVGUsFb3caSZOkqWDsZF9tjlSHdajRXKYOKuljpqyf7VCri-mk4q5sbQ7j-lBz2DyjXKWs-TJE1py0q82l1xeNG-23-MnbQ9l39f2CkKaWoH8q_-l0PYoq2nL3U4S96wtTw02IePvy1lMFv3kLo2xd4lEr5EyCMCR1lhn3OX-Oe1U1hz7QI7ai__uSnDiFepFJwPxkWnB2Fyw65nrHhgqHDsEUhm3BVDsp8qzimbMouFUVjhOBt_iQrSHRmfwMj5VHVrxrDCzahukUMa-XjCCtFYpxJSSd0nAdW9kE5yktk9TVkogk1_wROVG7XkR3WS7PEs8_iangTcQ3An4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقفة احتجاجية في محافظة ذي قار جنوبي العراق رفضا للمشاركة في حصار الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/91868" target="_blank">📅 18:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91867">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وقفة احتجاجية في محافظة الديوانية جنوبي العراق على خلفية حظر الطيران الايراني من الدخول الى العراق</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/91867" target="_blank">📅 18:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91866">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a3ae8d19.mp4?token=qMBlNu1NTx_m2in4yCIEu_Sa4cy0hsRJ9Cm8g7a6hknE0yYS6VmyS28jbavpva7J9KNX4LmWA53x-XA5UoZ4RCMUVUuAX05sPWibfTR5JpCkgQnzxMw8-zscdtNBvvPNp5Zp2xOHgE3b0Fb4ytsxF6gUx0iCv8Tf5TZaQwr-9NFZdD9mfBxQb0xLh3jF27-nEA8LhgknwKV-SZgBYbz7l_u9WXEmeeHLwJOLYA6S7Ha-1uU5B7U_LTUxxdDC2CVd-ZC_0BcrbWoeGfNdFMlCeeeOzST0nnHQ2jrH5gXe8DdALPaMG23uMfnH1QIYoSaJlbZINsBtqI3rvDkaK3IgeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a3ae8d19.mp4?token=qMBlNu1NTx_m2in4yCIEu_Sa4cy0hsRJ9Cm8g7a6hknE0yYS6VmyS28jbavpva7J9KNX4LmWA53x-XA5UoZ4RCMUVUuAX05sPWibfTR5JpCkgQnzxMw8-zscdtNBvvPNp5Zp2xOHgE3b0Fb4ytsxF6gUx0iCv8Tf5TZaQwr-9NFZdD9mfBxQb0xLh3jF27-nEA8LhgknwKV-SZgBYbz7l_u9WXEmeeHLwJOLYA6S7Ha-1uU5B7U_LTUxxdDC2CVd-ZC_0BcrbWoeGfNdFMlCeeeOzST0nnHQ2jrH5gXe8DdALPaMG23uMfnH1QIYoSaJlbZINsBtqI3rvDkaK3IgeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ الاعتصامات امام بوابات مطار النجف الاشرف الدولي</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/91866" target="_blank">📅 18:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91865">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
الشرطة البريطانية:  حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.  اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.  إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91865" target="_blank">📅 18:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91864">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf9268f87.mp4?token=hptuGB_qNJPKPR6XLx_3JSRcsxAsWqTdY20JfFjUxPZl0Ppo8hY_NRnfl137NjPOrGE9gS_87527ilcXMh9QPDgUx1qOxPGLuamnKnWfqNN6DjJ5Dj6WZ9BoldfimQDj8cYEqRJQLjF95PXNRs87Av3FczMPE_g-F5VKZlEzqa33Zf31O5KHOxxDJZ22SgAvoSwR1c1n1vFov0ylE61bfNpFrlKRPbVQ2Zas04Dc-tIZhGRykOH9JCz_VWolbbM_pWTfp4i3rVYqzWJMEpIMVwG7jCNp7M29WyAJvzN4NuLH1MGjaIi4dH3LZIjsmefmZVVnLK-fL6PNPfzCo6-074i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf9268f87.mp4?token=hptuGB_qNJPKPR6XLx_3JSRcsxAsWqTdY20JfFjUxPZl0Ppo8hY_NRnfl137NjPOrGE9gS_87527ilcXMh9QPDgUx1qOxPGLuamnKnWfqNN6DjJ5Dj6WZ9BoldfimQDj8cYEqRJQLjF95PXNRs87Av3FczMPE_g-F5VKZlEzqa33Zf31O5KHOxxDJZ22SgAvoSwR1c1n1vFov0ylE61bfNpFrlKRPbVQ2Zas04Dc-tIZhGRykOH9JCz_VWolbbM_pWTfp4i3rVYqzWJMEpIMVwG7jCNp7M29WyAJvzN4NuLH1MGjaIi4dH3LZIjsmefmZVVnLK-fL6PNPfzCo6-074i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ الاعتصامات امام بوابات مطار النجف الاشرف الدولي</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91864" target="_blank">📅 17:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3lPASVGD68UhGzAcUBS2Fq9LE4DIzGpDjw50ksTsDkMSU7l6Z-GUsOI3DaJAJyEa0RfHF-OQfLKzXFNRomkCkZsFc0Fg75HE3G1fyeTNr5TDV84INipe4KmDWingmt2GB6su3cWMIUvZrErVX8_B41O37FL-MHr92Os9YPksfJdpbkH4te98Fp-83L46yQk_u2qIOkYFupNf01_Hkb0NAORT7mvv-A6R33kPW70AzXveOtF5HjWAc-N0l5gPWvLiT1NWOeV8Th-EcCqLbXWJ5Q2CAw5Zu-sm2KmaS50YhLrmvRjVIHDhF-FhuojIapkBh-1zcH26y7y_AbUh0diYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAniWqCTRhe8ypFZWvscblrvwFmLxWQkMk8t-z0bhOXcG968TSD17N1hpXoZft2yE8u1E_uMowECv1JFoQpQKHAVqMl-LIzdRrwSD5cWNSevilN2HcCQ50Oe_SInC66dHxW8hA_67tpGXP3JV57-h37pb2oiRwvFEj0evaRQk047W7lABYMeZKXD93TjnWPcCXe6zhSYijuM7apCGYzYQ1hvI1QX08prnPD4Vf9NBsOgo3gD4RBRMsKXcZrLtIp2ecc3b8c2zKHPzqfafGkFeomyoPsn-uwG4YZMOL2qVYssCTVno8lsEFnijI_PDa4qt75FC44qwzUMhUQ52rX9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIoX7aOiGHJ8IQ2LlYcYnD09lHnMosw_ec5bBgUlRHn1C67pzf2PH3GdwQ7EATtS-0aYsyIXpAcZR4U3hYYMhsyfkx3y2I0snZSWNorkzUXq90p_XGuWnrmRueXLqtz5a4jTT426Qqbm8yagKIW4ULMVQydAI7-pYUfcyBGB_pHAB2ur1JyOOJ_qmc1fm1CTqABnL1b3PZlt9V6eTQP66DKC-a8Gf6n_VJkWkfck0ij2Kc026XXemOfEcpOpcl1raV8Sp3V333j9ESwfzA0UCvcHf-pf7NrwRBLO2EsHW7PacvYV13LsrucAySeJdt7KWk7pVH_or1xWfnoM0mxwQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من بوابات مطار النجف الاشرف الدولي</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/91861" target="_blank">📅 17:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469d9dfecc.mp4?token=qHcsAOwEF1g_BoU3gP_7LT1J-WlayafiX_NLs4U-AZ8Gb-RIcYJabc1R9HgeG9JOMEklynFm9ebF2Opnf3k1iMx2qiv8kpybk0bQxms2gqCQcVsGe3IaMJIv9Uj7XDbSL8LeOMzhpPeZlBOxwtqawkugwjOj--zFvoRnrSvt_yW0ZKk_26pC3EYHTwGyr7VYVCpemwch0S0Qq83ks2ZbDm5xQxOh5IJNbr6g5nxYHgWFcsF5C4m_lR578FCghqmUQDg3onsybjI__g-na-xa9aEMW5fU-OoEmdNuZXb_tzN3IEhgEAilW6R6wC1ZWKDgmaZKbb272CDne3LO5x_gxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469d9dfecc.mp4?token=qHcsAOwEF1g_BoU3gP_7LT1J-WlayafiX_NLs4U-AZ8Gb-RIcYJabc1R9HgeG9JOMEklynFm9ebF2Opnf3k1iMx2qiv8kpybk0bQxms2gqCQcVsGe3IaMJIv9Uj7XDbSL8LeOMzhpPeZlBOxwtqawkugwjOj--zFvoRnrSvt_yW0ZKk_26pC3EYHTwGyr7VYVCpemwch0S0Qq83ks2ZbDm5xQxOh5IJNbr6g5nxYHgWFcsF5C4m_lR578FCghqmUQDg3onsybjI__g-na-xa9aEMW5fU-OoEmdNuZXb_tzN3IEhgEAilW6R6wC1ZWKDgmaZKbb272CDne3LO5x_gxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انطلاق التجمعات قرب مجسرات ثورة العشرين في محافظة النجف الاشرف استعدادا للتوجه والاعتصام امام مطار النجف الدولي احتجاجا على غلق المطار امام الرحلات الايرانية  #سيادتنا_لاتفرض_بالحظر</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/91860" target="_blank">📅 17:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03935d9672.mp4?token=YOluFFPEMuZ5lAWJwsVo3nDmb9FqviSMhxuj0-fgOZyYMkQuUJTzCzobbVxgavE2VOKG3SQTWffErH7Sg9Y3V3LH0l2kMa0Se5O9iumxyJr68IHdxwX30jw-F42AMXXCyH08F_IFv9hsZF_GT47IL3bGYAMNx8Z84yRzeXFWMYh4g12NUjrgWeMgQm0xF3HU_Qe7blv1TDAV7crDALpDVplu2EsRZzxFTXqpcZ_lQBt3EZyQdF0TABsg1CbWvUYbLUKiszSrIRq1rHyuhVV9W6a_flBi4RUNBzUtRrj5ch27XSvWQi-SE2Tp8wi41sGgEhVKnrMEcQSK16WzbiV5iGtkpIMEQLzmBuq4ZoMAqCmsaFh0ZPHIsaDSJ0MN-g69EDpVlwLUPxUDvxFjuK1EK1bby4M4oetHrwsUQq30w4AmLwAfvvpsjUp206fz5xEwou5Q7M6koybnvO1yzaq7T2Nde9VIsxoyTCo73UrgUirDdjqt9KRI0jG_AwQls9RwHoOnTEFSr7eeP_2sUhXgbq_2VoAKVW3UsvAt06nmmUbjH1AfpyS_BF6WGdFiT2fDayr6uhrVN6Bp5KiyIVVDxD4nqQTvdn-R7eLPRA3cH0IQSwNoVuxTWKmkF5FUX2oUykAoxU3KF1LT5NBg6nanDxp63_p0-WtGtKNPB5-EewU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03935d9672.mp4?token=YOluFFPEMuZ5lAWJwsVo3nDmb9FqviSMhxuj0-fgOZyYMkQuUJTzCzobbVxgavE2VOKG3SQTWffErH7Sg9Y3V3LH0l2kMa0Se5O9iumxyJr68IHdxwX30jw-F42AMXXCyH08F_IFv9hsZF_GT47IL3bGYAMNx8Z84yRzeXFWMYh4g12NUjrgWeMgQm0xF3HU_Qe7blv1TDAV7crDALpDVplu2EsRZzxFTXqpcZ_lQBt3EZyQdF0TABsg1CbWvUYbLUKiszSrIRq1rHyuhVV9W6a_flBi4RUNBzUtRrj5ch27XSvWQi-SE2Tp8wi41sGgEhVKnrMEcQSK16WzbiV5iGtkpIMEQLzmBuq4ZoMAqCmsaFh0ZPHIsaDSJ0MN-g69EDpVlwLUPxUDvxFjuK1EK1bby4M4oetHrwsUQq30w4AmLwAfvvpsjUp206fz5xEwou5Q7M6koybnvO1yzaq7T2Nde9VIsxoyTCo73UrgUirDdjqt9KRI0jG_AwQls9RwHoOnTEFSr7eeP_2sUhXgbq_2VoAKVW3UsvAt06nmmUbjH1AfpyS_BF6WGdFiT2fDayr6uhrVN6Bp5KiyIVVDxD4nqQTvdn-R7eLPRA3cH0IQSwNoVuxTWKmkF5FUX2oUykAoxU3KF1LT5NBg6nanDxp63_p0-WtGtKNPB5-EewU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان : بدء الاعتصامات التي دعت اليها المقاومة الإسلاميّة حركة النجباء في بوابة مطار النجف الاشرف</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91858" target="_blank">📅 17:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGlVublbmy80Fd24FXe_Ep-htGXmDj9N4WmzqBi3a0jBi7fl0U7d7s9HmR9ShdNuemKRy2UXgtGbnC19zUV5Vvo3wJUVnIZcDuaBlXJRu8oomS4X0NA5U9SfvOqaQmP9K4FQJLELFSK3oO1PBS4Kx4hxGMyWzmu9hQm_oCcCId0zToebaq_vhbRPNF_nuT-hntQvp8a4B2hPbxIBxKAp5AbS1E6w40k04aZIVllH47hKqY4HVZ3q6p0rmfrSOob0p7s1ueJ8l8jS9Hz0wkHbDYLbl07J3JrtRj_PhgZsSzr1rdX8NZtOL5lVYARRxxIWuqVDmARRJ8_00YogEjGnog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان : بدء الاعتصامات التي دعت اليها المقاومة الإسلاميّة حركة النجباء في بوابة مطار النجف الاشرف</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91857" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91856">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
الاتحاد الخليجي يوافق على استضافة العراق لخليجي 28  لا تكطعون بينا ترة حيل حبيناكم</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91856" target="_blank">📅 16:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91855">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
انباء اولية عن اغلاق السلطات الاماراتية لمقرات قناة الشرقية العراقية في مدينة دبي وهي المقر الرئيسي للقناة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91855" target="_blank">📅 16:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91854">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">السفير العراقي في إيران: مطار النجف الأشرف سيفتح أبوابه أمام الرحلات الإيرانية خلال 24 ساعة</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91854" target="_blank">📅 16:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed462a036f.mp4?token=jlz9aG3yroQPX9RWPUhOfiC9toYlF1nPMyXMoZqM7cmUnZhvW9vQi4S2EUlJwKjXof1_sirHqvW-dMNBXNsOF-qzzyQhPDj8MeRH-IPAlPsnuIFtvAQG4S6RKJ7U4KfyPX6rvL8y5FzWH7txcCDgcMvNLYV7q9fbQiPPXRBL3o82X-aQujaQjaNP8wzx3baPSqNalhmPxEYc18OF1OScoIpmuZ886Ylkob3bymL-YaX7D61HUXl7NqyisKp0DGVORijatVG1XSk-PCtmRJEn21wzCN8SXshsg1T1BNpO_jNSmpuOI49uWfUMBAhh-F8HAqdDXjDZb1ynKuSP9jORKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed462a036f.mp4?token=jlz9aG3yroQPX9RWPUhOfiC9toYlF1nPMyXMoZqM7cmUnZhvW9vQi4S2EUlJwKjXof1_sirHqvW-dMNBXNsOF-qzzyQhPDj8MeRH-IPAlPsnuIFtvAQG4S6RKJ7U4KfyPX6rvL8y5FzWH7txcCDgcMvNLYV7q9fbQiPPXRBL3o82X-aQujaQjaNP8wzx3baPSqNalhmPxEYc18OF1OScoIpmuZ886Ylkob3bymL-YaX7D61HUXl7NqyisKp0DGVORijatVG1XSk-PCtmRJEn21wzCN8SXshsg1T1BNpO_jNSmpuOI49uWfUMBAhh-F8HAqdDXjDZb1ynKuSP9jORKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات مجهولة ترفع علم اقليم كردستان في محافظة كركوك شمالي العراق وتقطع الطرق لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91853" target="_blank">📅 15:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الاتحاد الاوروبي: تحركات الحوثيين ضاعفت المخاطر في طرق الملاحة الحيوية، مضيق هرمز وباب المندب والبحر الأسود نقاط اختناق حيوية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91852" target="_blank">📅 15:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91851">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وكالة رويترز: يجري حاليًا نقاش حول نسخة معدلة من المقترح الذي قدمته إيران خلال فترات راحة جلسات الجمعية العامة للأمم المتحدة، وذلك بهدف التركيز عليها.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91851" target="_blank">📅 15:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91850">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وكالة رويترز: يجري حاليًا نقاش حول نسخة معدلة من المقترح الذي قدمته إيران خلال فترات راحة جلسات الجمعية العامة للأمم المتحدة، وذلك بهدف التركيز عليها.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91850" target="_blank">📅 15:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rI1A1EEgGTN6Bl-142MHVmCMTrh-KLSYlCrkr5DLGp_dlRXoNH7CFV2E7-qX8JDm-_cqPnF0UAnnUrxZjzyYqD222-LFg6XVXzEhBRDyppNNjOnlBf-FWoVKVHI0H7GoQ_DSM70saJv9w4YimsNRdpWXyrMaM3HyplO-j5s-w3eaQV0n7BIQwMXyGmM3GY5cSAsLSwZf8Tz1LCNMnX7mwUjBLmSTOl_owIGj034JVxSV0WclOToRg_niq7kKsYC-LvBlTRDsjRLggUYbN8n4J-2UhniXQiymOksTUQwGUJbriasiLyA5-R7ToTv9FVwZeccRMxDJkJle6_fwTlrMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkiWMgEV7hOgT9VHWME8qljZUMpMMhLh8RKX8mU9WFXiTf5L1cr08zec5vMSpz9aYTHkNis7ZO1xB0MoAiHWqXxcCtVaTGeh_kA4Gh7gu-g0G_GKtTt86ghpGfHuN-g9K4hruQZtYh9pCzFv0IzpwXRkTgUJF9GHuA4Lb3wKZO6HptOyHurqd0ogXvVpirczBiH0J5Gk-L4b3HMH1anB0SPdc4alflAFhC21vtk5xqU7UtL0OQn5pLBrfS4ztHlMErV3qBQdiDla7GlDcH5vI1LbajJ6BmAePiK357JtXWsGT9_8WNOwtvSF459s1Jm3dZaOOxFkntMyNHQSUbnbDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اطلاقات جديدة في هذه الاثناء من الاراضي اليمنية تخرج لدك حصون ال سعود</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91848" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91847">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات في جازان</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91847" target="_blank">📅 14:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91846">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارات تهز الجنوب السعودي</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91846" target="_blank">📅 14:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91845">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات تهز نجران</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91845" target="_blank">📅 14:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91844">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات تهز نجران</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91844" target="_blank">📅 14:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91843">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حكومة إقليم كردستان العراق تعلن تعطيل الدوام الرسمي في جميع مؤسساتها ودوائرها يومي الأربعاء والخميس بمناسبة يوم السيادة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91843" target="_blank">📅 14:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91842">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">كميات كبيرة من مياه نهر الفرات تتجه للاراضي العراقية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91842" target="_blank">📅 14:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91841">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY1HMj81jvrDETrrd72zO-kVGs6o2K5nptwZm7z1ZXDkF1wxfm7HqVBTZ0ZzZ5Nx_3R4rZLHJtOHxyRt2FwMDLB0Z2-SDWRmrn6T3VkinP3VkM-QDMCybK8sU6FWqMKx-qfYgYP8KvxC2W4f_vIPVMf1Y49Ef8zsnB4d85LiAItTCdtKZZ5rskSZ3KrE94TYKa50WwbhGz2lVdSeb95tqZ48zlVLYXZkrN1eFVCfBaZK-jUdyW2l9d5thhsKqo4dAM8n4grXva6Q7HYU2jAs33-0YB7F8mGwRORrmSBMsXrC_Z0PUhCxRWERbj3zZBFuHaDSnrExiXlq9o65ROljfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رسالة من القائد الأعلى للثورة الاسلامية بمناسبة أسبوع الدفاع المقدس وذكرى استشهاد الشهيد السيد حسن نصر الله:  بسم الله الرحمن الرحيم  وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِآيَاتِنَا أَنْ أَخْرِجْ قَوْمَكَ مِنَ الظُّلُمَاتِ إِلَى النُّورِ وَذَكِّرْهُمْ بِأَيَّامِ…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91841" target="_blank">📅 14:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91840">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
في غضون ساعات، سيتم نشر رسالة من قبل قائد الثورة بمناسبة أسبوع الدفاع المقدس وذكرى استشهاد الشهيد السيد حسن نصر الله.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91840" target="_blank">📅 14:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91839">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
الاتحاد الخليجي يوافق على استضافة العراق لخليجي 28
لا تكطعون بينا ترة حيل حبيناكم</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91839" target="_blank">📅 13:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91838">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAqeYYVNf47TM-X5bCChyMkXrS375WRWnPNm3hIoI1sIBusseurjzVCfS-fEzUCc0uz8n5EFyBFzVqnl25l-sZFSldDV2Eg3Jr0dz7oVuuDe0RAws35wrsTTA3mC0LguaFx-DGPD31fECTwhTPkWNxfaZbEuB4KSWS5YblcvOkxSS4LiN8jmRtBUDR-wL4zllwzqa5WZBLOqVIxKaBbHBEhWP2iDHimHTGrajT1xh0hTZXz9hUajbkAOs5Eh0-_d1WYxmJH0GwNiZ5p4NkMFY7QtkGhIj02Q_3fKXI53rMd73NNEdM0-lGSPNweYoeGMs5LmPaaXe7IlHkEtiMdWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
‏خام برنت يرتفع 4% عند 109 دولارات للبرميل مع تعثر مفاوضات أميركا وإيران.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91838" target="_blank">📅 13:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91837">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔻
الخارجية البريطانية:
لن نستسلم أبدا لتهديد روسيا ولن نقف مكتوفي الأيدي ونتخلى عن شعب أوكرانيا.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91837" target="_blank">📅 13:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
في غضون ساعات، سيتم نشر رسالة من قبل قائد الثورة بمناسبة أسبوع الدفاع المقدس وذكرى استشهاد الشهيد السيد حسن نصر الله.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91836" target="_blank">📅 13:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91835">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmGK8Ckhy3xdR1FvVJp37qY0rLRK689YouP_DxogAUu7DXfDMeQNktB3PQlNAVjeOy726Bil_TuU0EawCK9owLAquhSamyzx_yO9STrK075alXd11z_u2liixf9k13GASXz3OXCtE2_i-f3kVQPBR_6Aqs-Zqq_qFP5I_xU1R2Ob3rMs-noe_25paU_ktFdx7yP4Lx1Yq2BFqmns4Q3FFOIzAQJ5CpZh0NtcsAONCV5tU62wQe66DT_Tma0u_uUpx7ycOoMVKxVLzwSyF-IN5eLIeNBzwsv6c4PJz6bi3nrXv-AOY5Hrwl0iHRVub1UkbfjXo14JccsrxLn-kShoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#لا
أُعطيكم بيدي إعطاءَ الذليل
ليست كلماتٍ عابرة، بل صوتٌ من الإباء والعزّة والثبات.
وفي الذكرى السنوية لاستشهاد سماحة السيد حسن نصر الله، تتصدّر العبارة جدارية الفردوس في بغداد، شاهدًا على ذاكرةٍ تحفظ معاني الكرامة والصمود، ونقشًا يتردّد صداه في الزمن.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91835" target="_blank">📅 13:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91834">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
🇮🇶
مطار الإمام الخميني:
لم نتلق أي إشعار باستئناف الرحلات الجوية من إيران إلى النجف.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91834" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ac3tGzoRs-7lzOdNFFISHwwkqtmGeHNWiEZQmUtzsLg8D-rYugyTT8pV8bgr_JZy6RSVOWHiMTbdRpxgpwJ6XwvTNQ0yLcZlHR43NTXGaHZj5gjw62NsZCEQlUMeCu9TFSRPdDO_uyW1Clwwo3VuFq4eDhAQXAUsrzAwKvwk7vUXIykcbfyxzGPZ7rZe1RJc0KsyAJ5Eu5R_PqLI1D-L3rbFICHLngX2YEEkPPTqpyjo8_AiQ306tG76UXaQ8kCQWmM0pR59iZjpMRxF-kAhBoIk0sq-HWqaEnQQT2sFlKz6A1zJJbCJv5dTECsm0WAieBBiooYqvcyYKbNQWhNLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuppjD9PNvIj9ZbzCVCjZVgJDcIApUg7IyvGVRdv9Ik6LU9fXRnz7J3HqwPXORUSJhoGs1uVvN1H9E5mZcU-qcV0sTzmk9ToEd9c4N2O0rWyRZix4XvKdm4dejs4xrIpWEQK94LP3JJPygztesKgjI-GeUiJZeO7XuPsq-ru6KYtpahMOUqWe4z4UXGkaq1Se14TLzeyf5ulLRh-gazGKB6nhteJDcUMSrQuJR3XLfbNejf8mQt43KzZfZwSffNpRgrwMRYecYcmEN2n_kKYpzBieLZFW46pC1dvF-ti7wGklDGbXG4y38Uplju4Xhyky8wYCmcH7OsJDrmtLQb9Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b678dfd80.mp4?token=u6920e6tHjYDiI-x3LgIPZjMJbPuzz-cpZE78Py2RZmymuRjaBYFTNmfzZXdW8A9rgWOlnWr0Am2r1e_YOCfv0c3o6CYYkVBHG6rXkOp1BolaJdNqIJm9K55yLodO2lPq_X-LcXeSwBZnEDPj_A6-BSOYqTvSRgRhx8FnXKmsqx2GieGlZhy-TS-Ra-nMSdBAn4ckD8uYVz5PDMnuHWy1w7-lDvvR8J1h_TJn3mUO0eIJox23NtUrtNnKBX5coTGS9DcExhl20hnvjx-DVfrNlV2z2SK1EEWmGmhnRGQ6xIDNUnPwYcNd0wHYuUQvjpraQBp4Tdi0bCti_RyV1Vd3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b678dfd80.mp4?token=u6920e6tHjYDiI-x3LgIPZjMJbPuzz-cpZE78Py2RZmymuRjaBYFTNmfzZXdW8A9rgWOlnWr0Am2r1e_YOCfv0c3o6CYYkVBHG6rXkOp1BolaJdNqIJm9K55yLodO2lPq_X-LcXeSwBZnEDPj_A6-BSOYqTvSRgRhx8FnXKmsqx2GieGlZhy-TS-Ra-nMSdBAn4ckD8uYVz5PDMnuHWy1w7-lDvvR8J1h_TJn3mUO0eIJox23NtUrtNnKBX5coTGS9DcExhl20hnvjx-DVfrNlV2z2SK1EEWmGmhnRGQ6xIDNUnPwYcNd0wHYuUQvjpraQBp4Tdi0bCti_RyV1Vd3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
بالتزامن مع الضربات الصاروخية الروسية على العاصمة الأوكرانية كييف.. الكرملين:
على أوكرانيا أن تدفع ثمن أفعالها خلال الأشهر الأخيرة وهذا ما يحدث الآن.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91831" target="_blank">📅 12:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4a81a27b.mp4?token=bvSjtpvuKYCF3hKJjepmHnmG6_L_FBWetkP4_fhkzjmSMvQEwvGfRPAlLXZp_df0t-_eqOxKnHab3AvzeKYlduhQ2gmK6hm8x3KJzNoc9ZlUUr9G_eLSYEAMwmcwUpuOHnT4dOLlAY7vYXqsDfzCOZN2AWbt1QwyvzyR3W91mzwxYwO-eccn0ErAvzdq0sIQu8xZ9P19PTzMKjtKtc0TSn29VCqqiqwQjwm1qcfH_Bx6bLT3dQenZtyq3SN96DBWgoy7d7uUzaS23F4366VujxQH0RqSbHgRpvYCAzbV_SsGwKcht4wStwCmgLj4aai0fYSXVhMR7WDZ5hfXoHS-PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4a81a27b.mp4?token=bvSjtpvuKYCF3hKJjepmHnmG6_L_FBWetkP4_fhkzjmSMvQEwvGfRPAlLXZp_df0t-_eqOxKnHab3AvzeKYlduhQ2gmK6hm8x3KJzNoc9ZlUUr9G_eLSYEAMwmcwUpuOHnT4dOLlAY7vYXqsDfzCOZN2AWbt1QwyvzyR3W91mzwxYwO-eccn0ErAvzdq0sIQu8xZ9P19PTzMKjtKtc0TSn29VCqqiqwQjwm1qcfH_Bx6bLT3dQenZtyq3SN96DBWgoy7d7uUzaS23F4366VujxQH0RqSbHgRpvYCAzbV_SsGwKcht4wStwCmgLj4aai0fYSXVhMR7WDZ5hfXoHS-PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد دحر مرتزقة السعودية..
القوات المسلحة اليمنية تسيطر على جبل البازلة والأغبرة بمحافظة لحج.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91830" target="_blank">📅 11:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
‏
خلية الإعلام الأمني:
تسلمنا المقر الرئيسي للقوات الأميركية في مطار بغداد.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91829" target="_blank">📅 11:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91828">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58edca218.mp4?token=IDkqCmNnZOzvUCVQS7gtP5219ujYLzIfYTscuSre2eMCIicOCII7BsCsc3qV8w1jC0MsOkybob9tVjemIGXi2ThOlEMmAO9Ku4UO74uqORas-ss8iR0SwZEyrTkMwczThLBPPU7CG87K0l3v44pbb31bMXmibafF-Dnph1STwwzbhwQmu7ZKzIbXKQEGTb1BhE5ughOrAnYCss-kTy5LM60Yf0faUlAJWUYbTRKGPIo-PVb4FFJHIvDF9utP_NpeL0slNVn3XUjfU6IbV2_sfaBkAhu-TI566kIk2IU98g7s8nigVPmFXha-XdC2pYttoaAgBIDfg_n3hGoaBIPB8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58edca218.mp4?token=IDkqCmNnZOzvUCVQS7gtP5219ujYLzIfYTscuSre2eMCIicOCII7BsCsc3qV8w1jC0MsOkybob9tVjemIGXi2ThOlEMmAO9Ku4UO74uqORas-ss8iR0SwZEyrTkMwczThLBPPU7CG87K0l3v44pbb31bMXmibafF-Dnph1STwwzbhwQmu7ZKzIbXKQEGTb1BhE5ughOrAnYCss-kTy5LM60Yf0faUlAJWUYbTRKGPIo-PVb4FFJHIvDF9utP_NpeL0slNVn3XUjfU6IbV2_sfaBkAhu-TI566kIk2IU98g7s8nigVPmFXha-XdC2pYttoaAgBIDfg_n3hGoaBIPB8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
وزير الأمن القومي الصهيوني إيتمار بن غفير يقتحم المسجد الأقصى.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91828" target="_blank">📅 11:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91827">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa304d8f3.mp4?token=rLqbVK7M5jTS77ByTkcfyWY7DTWv7IzkZEXUqPU4yoYBUWqLYvS3THcAcq5R0rbkMCjHaP68Y_xlgZH7tZ7sqtusYjWlrW-IwE8mWcZJ44Ot1lRpDGX52rG-DeJ8tfuxOxe30FkmkzSE5TV6x-Vjm6bDzw2MJnMJrLeIEEXf4m5P6CO1XAOcifP18UuSfjW4gvJtzH2DUNzgop3tVSPxCAkQdElDSS72o9cj0FxS4cltbiIbleIoFXr-pMK8sBdUm5nvogVU9DZCnACZcn9ArSgwZdrKtSTYE3bHiEzBsIhY0-Lop8FWxffMefzN0WLtqiEJ_RcqlmaUEh8TumcRmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa304d8f3.mp4?token=rLqbVK7M5jTS77ByTkcfyWY7DTWv7IzkZEXUqPU4yoYBUWqLYvS3THcAcq5R0rbkMCjHaP68Y_xlgZH7tZ7sqtusYjWlrW-IwE8mWcZJ44Ot1lRpDGX52rG-DeJ8tfuxOxe30FkmkzSE5TV6x-Vjm6bDzw2MJnMJrLeIEEXf4m5P6CO1XAOcifP18UuSfjW4gvJtzH2DUNzgop3tVSPxCAkQdElDSS72o9cj0FxS4cltbiIbleIoFXr-pMK8sBdUm5nvogVU9DZCnACZcn9ArSgwZdrKtSTYE3bHiEzBsIhY0-Lop8FWxffMefzN0WLtqiEJ_RcqlmaUEh8TumcRmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇨🇳
🇮🇷
سفير الولايات المتحدة في الصين:
لقد أوضح الرئيس ترامب بشكل قاطع أن أي مساعدة تقدمها الصين لإيران - سواء كانت معلومات استخباراتية أو قطع غيار أو معدات عسكرية مباشرة - ستكون غير مقبولة على الإطلاق.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91827" target="_blank">📅 11:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91826">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571119c9bf.mp4?token=XYkucn0e4JzPUUAW-Y0JlciAb3O068QhiJvINwtkFEoQXDwC9AOFOmBMeO7xYeGwTKPjf6zG6i3scgefS67ZAcxnhpn4QsOCkboCrGzCcLLU224FHku338a09kwhArIuZzIEkdS9oh2q9LxZ9P59cVqRf8fm4XL_SXuW5TOeBvWwD2QV0u48mp2MKA6a7KIAD0GfJCqWqT6bHM_g8z4L5LWDn_YSzYjanD3D0Vm3bnYT0NrJndZl0q4E1IV5vKPuSe_NiEj-Nyw59Zv-of4CmzMljpCrbHWGexPqWLcb936ogfnbOuLMukP60bKLELdSWXgvmetSX0_NuNMNhmQryCPacwVHflvgi3sJRtuAd_qn4i_K6Zx7ukKNS8E88quQhfNDvtuXDfP4kYSZiwiUkD7Xd1DZUQJzCcfOfT0CYZV3rXcK-jSWmTC-PUqBfq092n_6wUt7lsdZVGOX3RQ7YhjYyhPra3cq-FuDc_i3ctUxe4zF_BvQpZ00QGed7v-kvSy2XwOPlXjh0yU0QF7CxklWVgkOGI_vG-3WYADOrOFOkiev66nLmBvrllkr3A4TRPml3XF97tqZQwhpZYtBl2FFI0AzJPqHIj6vRQOq18Rq9fBoAxoTU_JokE7oDjxHnk1MuBFHbqVQ1s18Zk8wESVQ2aBvjZqwgdOvhexHt0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571119c9bf.mp4?token=XYkucn0e4JzPUUAW-Y0JlciAb3O068QhiJvINwtkFEoQXDwC9AOFOmBMeO7xYeGwTKPjf6zG6i3scgefS67ZAcxnhpn4QsOCkboCrGzCcLLU224FHku338a09kwhArIuZzIEkdS9oh2q9LxZ9P59cVqRf8fm4XL_SXuW5TOeBvWwD2QV0u48mp2MKA6a7KIAD0GfJCqWqT6bHM_g8z4L5LWDn_YSzYjanD3D0Vm3bnYT0NrJndZl0q4E1IV5vKPuSe_NiEj-Nyw59Zv-of4CmzMljpCrbHWGexPqWLcb936ogfnbOuLMukP60bKLELdSWXgvmetSX0_NuNMNhmQryCPacwVHflvgi3sJRtuAd_qn4i_K6Zx7ukKNS8E88quQhfNDvtuXDfP4kYSZiwiUkD7Xd1DZUQJzCcfOfT0CYZV3rXcK-jSWmTC-PUqBfq092n_6wUt7lsdZVGOX3RQ7YhjYyhPra3cq-FuDc_i3ctUxe4zF_BvQpZ00QGed7v-kvSy2XwOPlXjh0yU0QF7CxklWVgkOGI_vG-3WYADOrOFOkiev66nLmBvrllkr3A4TRPml3XF97tqZQwhpZYtBl2FFI0AzJPqHIj6vRQOq18Rq9fBoAxoTU_JokE7oDjxHnk1MuBFHbqVQ1s18Zk8wESVQ2aBvjZqwgdOvhexHt0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مسعود بارزاني: في حال انسحاب القوات الأميركية لن يكون هناك ضامن لمنع عودة تنظيم داعsh الإرهابي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91826" target="_blank">📅 10:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91825">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmNII-fGJEfI8LeLaY0-qcC7sNC_4xAgd103QPG0dK0s3AcLYzjWx0X9ixIQGhrxKpmhy068NJeiyQRCJSBaHOEqhbIjTmGCwRtfSfKDOBpRyzdEG-NjJt2w9R4-LKGAPKbJz-fOxzJxmHX1zyFx31moGp_eBbAqaKHwgChP63P3z1GsvWDo3w6M5PHtLZQLuakTtoNcbeOmWn8noHA-8HxyUWkhnDxmxBxj0gLAbOeLndTBZG3_s8wrrEH8TlARfY8rcySIgHqOspXJZF3rxNKhHCsJWEQgqpDBfGriYwLiyAj9OpgN8vHdQT3fRfyzo6WTpZ7_UKiGVzFGeoQLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تستمر في الإرتفاع لتلامس 108 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91825" target="_blank">📅 09:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91824">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اصابات مباشرة لمقرات الاحزاب المخربة في اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91824" target="_blank">📅 09:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91823">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇱
إعلام العدو:
التقدير هو أن حماس لا تزال تمتلك 30 ألف مقاتل، بالإضافة إلى ذلك، تستمر في إنتاج الصواريخ وصيانة الأنفاق داخل قطاع غزة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91823" target="_blank">📅 08:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91822">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله اكبر
🇺🇸
اصابة اكثر من ثمانية جنود من المارينز في مضيق هرمز اثر تعرض سفينة لهم بصاروخ كروز بحري اطلق من قبل بحرية الحرس الثوري التي اعلن ترامب انها دمرت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/91822" target="_blank">📅 04:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91821">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏ترمب: تم تدمير السلاح النووي في إيران ولا يجب ان نقلق بشأنه بعد الآن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/91821" target="_blank">📅 04:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91820">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سماع دوي انفجار مجهول في اربد شمال الاردن</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/91820" target="_blank">📅 04:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91819">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34e34e8eb.mp4?token=hf4F0MCDbvIBObT1_X1_5VmfKueTVEVJhcnkTTl6w5KFeBMeB1ZHLjL6Z_4jAP8UB9kpLRDhVvYdu9xu2OjI68EO1v8C-BvaGEETiAD8Tf7fePa0S_wSX27fovruTfzjqQcFsN-pmprhwupc6ax6rJ6DhVmc2T1F-PD4UZX0hVW1rnrcLATbwqIyubF_yCkY7VgKgOoA9m47vnalA4ahH3WFGjsxTu16I9FNgRTUZPOKhEunXwTNwe5H14x6Jug0LiDUCAvNc1nBiZ72Csq2xQYIdaWVtNm-elCTwumjENksFWbWIPXF0XBIMrFi46I28iyPKVlYYKmryzhcszjfRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34e34e8eb.mp4?token=hf4F0MCDbvIBObT1_X1_5VmfKueTVEVJhcnkTTl6w5KFeBMeB1ZHLjL6Z_4jAP8UB9kpLRDhVvYdu9xu2OjI68EO1v8C-BvaGEETiAD8Tf7fePa0S_wSX27fovruTfzjqQcFsN-pmprhwupc6ax6rJ6DhVmc2T1F-PD4UZX0hVW1rnrcLATbwqIyubF_yCkY7VgKgOoA9m47vnalA4ahH3WFGjsxTu16I9FNgRTUZPOKhEunXwTNwe5H14x6Jug0LiDUCAvNc1nBiZ72Csq2xQYIdaWVtNm-elCTwumjENksFWbWIPXF0XBIMrFi46I28iyPKVlYYKmryzhcszjfRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابات مباشرة لمقرات الاحزاب المخربة في اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/91819" target="_blank">📅 02:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91818">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886951be8e.mp4?token=u0PKopnEA7CzLfiH3s84QdXsiNi0dRqATG-kVNV7IKjmr2lj27nvFEn7Di1JfJzNl_ZzUN3iwPZo1srZnu4psBUwBG5XW3CcUox7cwQ4UNXaFTx1ML2fCFfRbYIfF7nLNVJ3znxvxnLyEYm5AXoT3M2xDdNTY7wRF4-NWzeVsU9frNMq_7gbVpfUg3DHbKQlyQxD3pMa5Y4i17wQMdV01Pq6xf8Jifqls5sngJLU5pwGe406Ar8tefEtBSaDKjSo-A51C2ZbJPchyOBhe9mUq8l8lOvR78inSZKOolGArqdG_PEMls0ZIK3cx3LlKymThCNVlA5pTqcFsuqRbpp1lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886951be8e.mp4?token=u0PKopnEA7CzLfiH3s84QdXsiNi0dRqATG-kVNV7IKjmr2lj27nvFEn7Di1JfJzNl_ZzUN3iwPZo1srZnu4psBUwBG5XW3CcUox7cwQ4UNXaFTx1ML2fCFfRbYIfF7nLNVJ3znxvxnLyEYm5AXoT3M2xDdNTY7wRF4-NWzeVsU9frNMq_7gbVpfUg3DHbKQlyQxD3pMa5Y4i17wQMdV01Pq6xf8Jifqls5sngJLU5pwGe406Ar8tefEtBSaDKjSo-A51C2ZbJPchyOBhe9mUq8l8lOvR78inSZKOolGArqdG_PEMls0ZIK3cx3LlKymThCNVlA5pTqcFsuqRbpp1lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المسيرات تتجه الى اهدافها لدك مقرات المعارضة المخربة في شمال العراق</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/91818" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

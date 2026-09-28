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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-91893">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇱
الاعلام العبري: صواريخ اعتراضية في مطلة.</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/naya_foriraq/91893" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91892">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSXJ_qSlPFXpDgbZtBQUAnyLxj5GwXWWHQ3c_y_kaWIbM4PCOrzYwtvnQ0dyKNRUzI5RzQ2H0_JF0NJQsbiLmuO5mVxaDyAq1D-W48rFDTQX6gEL7s063d5Exud4y_3jIITK49T8Ac-sHQ7VmSH1ssScsLBku-z6BN9lY8ur2uGvvt3Hng0nvNH-02sHzGSISJad3EDNgUOmFaeViBogZdd_uFCMlzagfD88CoHVIHilPNmhMsFQRTUt5KkHAAOO3WwHHA_ObrK7Vc4qFSAAvaQRBAKzzmGE9bjL2KR1mJcBcSCv4KurDlgTSXSKuCMJ7-jNbdQFzwoRCLxT4_jExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سيادتنا_لاتفرض_بالحظر</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/naya_foriraq/91892" target="_blank">📅 21:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91891">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏الولايات المتحدة تدرس إمكانية التنازل عن العقوبات، ‏رحلات جوية بين إيران ومدينة النجف الأشرف في العراق.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/naya_foriraq/91891" target="_blank">📅 20:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91890">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
صواريخ اعتراضية في مطلة.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/naya_foriraq/91890" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91889">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
‏
مسؤول أميركي:
نجري محادثات إيجابية وبناءة مع إيران عبر الوسطاء.</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/naya_foriraq/91889" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91888">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 38 غارةً جويةً وصاروخاً من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وجيزان استهدف العدو بها محافظات تعز وصعدة وحجة وخلفت شهداء وجرحى من المدنيين بينهم نساء وأطفال.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1123 غارةً وصاروخاً.</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/naya_foriraq/91888" target="_blank">📅 20:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91887">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
الرئاسات تؤكد دعم مطلب الحكومة العراقية في استثناء مطار النجف الأشرف من إجراءات الخزانة الأمريكية.</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/naya_foriraq/91887" target="_blank">📅 20:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91886">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
الرئاسات تؤكد دعم مطلب الحكومة العراقية في استثناء مطار النجف الأشرف من إجراءات الخزانة الأمريكية.</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/naya_foriraq/91886" target="_blank">📅 20:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91885">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇸🇦
السعودية تستأنف تصدير النفط عبر خط الأنابيب الشرقي الغربي بعد إجراء الإصلاحات.</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/naya_foriraq/91885" target="_blank">📅 20:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91884">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
الرئاسات تؤكد دعم مطلب الحكومة العراقية في استثناء مطار النجف الأشرف من إجراءات الخزانة الأمريكية.</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/naya_foriraq/91884" target="_blank">📅 20:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91883">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
ترامب منفتح على تخفيف العقوبات المفروضة على إيران مقابل "تقدم ملموس" في القضايا النووية.</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/naya_foriraq/91883" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91882">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/91882" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91881">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">العراق سيد نفسه</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/91881" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91880">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
انباء عن اطلاقات صاروخية من ايران.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/91880" target="_blank">📅 19:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91879">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔻
مقر خاتم الأنبياء المركزي:
العدو الصهيوني الأمريكي ظن أنه بإقصاء "سيد المقاومة" جسديًا، ستنهار دعائم المقاومة، ولكن حسابات العدو، مرة أخرى، باءت بالفشل.
جبهة المقاومة لم تضعف فحسب، بل بلغت مستوى من التكامل الاستراتيجي الظاهر والخفي، ومسيرة الشهيد السيد نصر الله مستمرة بقوة في لبنان وفلسطين واليمن والعراق، وفي أقصى مناطق الجغرافيا التي تمثل المقاومة والسعي نحو الحق.
القوات المسلحة الإيرانية، إلى جانب مجاهدي ومقاتلي المقاومة الإسلامية، مستعدة تمامًا للرد بشكل قاطع ومدمر على أي تهديد يواجه الأمة الإسلامية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/91879" target="_blank">📅 19:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91878">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPvk3a0jQna7B-BtrgVhWCL6JclaPqLLdKslo9DeBGrBu_i1FDoi5_r56HreERVCk5Oh2YFTgnNzxfbOYy8PQu-TfqGP7tX6XBfk1osymisBLn-EWso5v8W2fs6PyyNkcLctDklSpMXYSc_mAMbpgu6L7R0Jv7JESqaSWpLOSAO5B-o5NDZ11BT62X0zvFteIp33SZ7IHUd2ljJBkDL3E_wTMiT6-rMghge9w73dWz2cn50SfevOEm8Ay7gz7Y8iFyCkYXzlVOuR1YtAlP3dlVH1DEFeGh6KLX0_PRRVq42wNA0e-vCRc_4C_dlaZGhjvj2NzdVpKIkRjbq53beQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزارة الاتصالات العراقية تعلن إعادة حجب لعبة «روبلوكس» اعتبارًا من مساء السبت المقبل.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/91878" target="_blank">📅 19:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91877">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/91877" target="_blank">📅 18:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91876">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
‏
ترامب
:
المشكلة الكبرى هي تفجير مصافي النفط في روسيا. هذه ليست مشكلة شرق أوسطية بالمعنى الحرفي، بل هي مشكلة روسية في المقام الأول، حيث تتصاعد حدة التوتر بين أوكرانيا وروسيا، وتقوم أوكرانيا بتفجير مصافي الديزل في روسيا. لقد تحدثت إلى الرئيس زيلينسكي وقلت له: "يجب أن تخفف من حدة قصف المصافي.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/91876" target="_blank">📅 18:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91875">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇱
الاعلام العبري: سافر نتنياهو اليوم إلى الإمارات العربية المتحدة للقاء الرئيس محمد بن زايد.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/91875" target="_blank">📅 18:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91874">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i691f1xvlPmw_yZ_J2D8dngtXD4er-LNk5lJhJ6tmZndIBRx18dlOio6ciKjNSKu2fbape_75xQD5BcJZ9ugFcNUQ-9nU3MLy5TuAkox8pAAoISqeP5SDKV2DSTFiVLOLfAUkqYWzBbfyX87oBYEO7-LiebccjUr-6BA6h2LviC2msWSiaf4CT_zWknpWukugHx-0sbWXGlxdqSQ6AHEFu6La2zy1TRfTsKlGOe4muZzU_HnjRRBHdleDLYl7GEk4DrRpQUWBIe72CFN3RvvYIiTtCQ_EOqWoprzB6PuDUVNMgmcSuGcsjADhF4MNhLFJCYUS_xLC4OCIcQW8CW24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العراق سيد نفسه</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/91874" target="_blank">📅 18:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91873">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇱
🔻
مجموعة من الشباب أثناء تجولهم في محافظة القنيطرة السورية تلاحقهم طائرة مسيّرة وفجأة أثناء تصويرهم تطلق المدافع الإسرائيلية في المحافظة قذائف باتجاه ريف دمشق.
جيش الاحتلال: كل هاد مشان صحتك يا غالي
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/91873" target="_blank">📅 18:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91872">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833eba5bb5.mp4?token=NbzAwzHkf4vx6sj5ldvDjX7arhNFIQzc3xLwMtIfw57dEiLk0eLM_7ofWT_7qNEZxrqfXAmgo2hTtUKF8pJbFEDE8LQ-1bhD4e8X1oO9WKIC_oz_ykM1sZAaQPXylNVILrXMLmiIihUdGb9AL7HwN-1_da3qRV6qAKC_WDcJTNFt3sA2ZgcPwzbWUkcfxmVeWwCvAMI6Dmmo358GPNZ9vLFbUXIi691HXwo2ewaSXli8icEUXR1nkRLDVhx01Fvmx51UUaht5UeR6qrPfZTX0jN_bUyYhyCPY5MDZIUKzo3uOdESWhQKZWal3a-xTBlb1UKcs0KUlPRF_kWhb84ErA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833eba5bb5.mp4?token=NbzAwzHkf4vx6sj5ldvDjX7arhNFIQzc3xLwMtIfw57dEiLk0eLM_7ofWT_7qNEZxrqfXAmgo2hTtUKF8pJbFEDE8LQ-1bhD4e8X1oO9WKIC_oz_ykM1sZAaQPXylNVILrXMLmiIihUdGb9AL7HwN-1_da3qRV6qAKC_WDcJTNFt3sA2ZgcPwzbWUkcfxmVeWwCvAMI6Dmmo358GPNZ9vLFbUXIi691HXwo2ewaSXli8icEUXR1nkRLDVhx01Fvmx51UUaht5UeR6qrPfZTX0jN_bUyYhyCPY5MDZIUKzo3uOdESWhQKZWal3a-xTBlb1UKcs0KUlPRF_kWhb84ErA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تحذير جوي في محافظة لوبلين ببولندا خوفا من هجوم روسي محتمل.</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/naya_foriraq/91872" target="_blank">📅 18:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91871">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixv3Bz3UspZ8KJgS_r_MbvXjexkJzvl12LQicycBYONa9jclqJvduz_3rUY0ZetcBJ7rtzVB2g9jIcaiMf00GurUQQ5858PYrWgpnqpjNquHr0Q7kN1BnlPjAxMA35sR4xoEN8ODwy6KloNHZTslI7p_0eExbV1ABEzt7TTMy2h85ZXPIZRbTZefiIvUYeh8TzBp-5ZmwN1wUE1WJspq2N5qwjVLMrO8X_daZIQ5Dx_tIuttXqGjxt2vVi2CJfJIRv1ICYLHUXNRe99MqmUXKOeqTgmSdrOjchfdvZm_SSwsI4vAiKnWmkz5aRkQ-EIRM3F3nsRUVbkvffKdJ05D_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سيادتنا_لاتفرض_بالحظر
🇮🇶
البصرة تنتفض ضد قرار الحضر الجوي.</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/91871" target="_blank">📅 18:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91870">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e39cfc2c9.mp4?token=QMnnT0iWoHWsgOw9J_LkurT_RaCjSnCOat-pdFVL1T5nQPl2yO--kfalaFdquRQ6t34Z-4eEFh0cMs4XA5pCNw6JVvai4KRuHuEcWRmZ1OyIdbZr8VA39YC1a9pLRkWb8C9QTa7T-vemFt-iFYD9GNVAfbmzAs0u345NguExcpAg0cAokmNmD3YorKFhfmZ0XtjQYe-ghG4KXc_OSNyfNnAYbGKrx3B1JUIyUNKjYo_93yprcVjOaHP87z4KuCKpZUS0bmO2ebE7fuOTdKKmNhQFWjJPe-z9yqnyNH9rm6Aj8gL79fZyEG4fwKLlcTP95RZGELzhMauQO35xsJpRlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e39cfc2c9.mp4?token=QMnnT0iWoHWsgOw9J_LkurT_RaCjSnCOat-pdFVL1T5nQPl2yO--kfalaFdquRQ6t34Z-4eEFh0cMs4XA5pCNw6JVvai4KRuHuEcWRmZ1OyIdbZr8VA39YC1a9pLRkWb8C9QTa7T-vemFt-iFYD9GNVAfbmzAs0u345NguExcpAg0cAokmNmD3YorKFhfmZ0XtjQYe-ghG4KXc_OSNyfNnAYbGKrx3B1JUIyUNKjYo_93yprcVjOaHP87z4KuCKpZUS0bmO2ebE7fuOTdKKmNhQFWjJPe-z9yqnyNH9rm6Aj8gL79fZyEG4fwKLlcTP95RZGELzhMauQO35xsJpRlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقفة احتجاجية في محافظة ذي قار جنوبي العراق رفضا للمشاركة في حصار الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/91870" target="_blank">📅 18:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91869">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266c2f95a1.mp4?token=KZXPnVN7naKHE0p0A5W-FTTkFYadD3jQdJUk-Q3BJUDhDw-28WsHfOZ1yCN7ifKgxN26UaFuEU13w_2ERTKBKxvIx9pUpijcyXrFmRHbxiAVd1Z11mjYirUJDIEDJ1NZYapJWnP1D-lm-ixWPE_EjDjB8pfsHh_CI0kaPCsukLgEk1l09SuuxyKhUDfYCMSDUP6sjS2A4upGrOyyDpHLD4oyZNO0YA4C09Aw0ifAZJdu6R5OtTIKxEtCOIG0QrH6M74PoU5-hl6D8n_biXlUXFeZ5YLVF76-nzDl20m20yxELw3LIS6sPq5YzW7JAWCsZBRM3SkKQtDOlWVP8aywVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266c2f95a1.mp4?token=KZXPnVN7naKHE0p0A5W-FTTkFYadD3jQdJUk-Q3BJUDhDw-28WsHfOZ1yCN7ifKgxN26UaFuEU13w_2ERTKBKxvIx9pUpijcyXrFmRHbxiAVd1Z11mjYirUJDIEDJ1NZYapJWnP1D-lm-ixWPE_EjDjB8pfsHh_CI0kaPCsukLgEk1l09SuuxyKhUDfYCMSDUP6sjS2A4upGrOyyDpHLD4oyZNO0YA4C09Aw0ifAZJdu6R5OtTIKxEtCOIG0QrH6M74PoU5-hl6D8n_biXlUXFeZ5YLVF76-nzDl20m20yxELw3LIS6sPq5YzW7JAWCsZBRM3SkKQtDOlWVP8aywVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من امام بوابات مطار النجف الاشرف الدولي</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/91869" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91868">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2cfc66ea5.mp4?token=dMi0SVGUsFb3caSZOkqWDsZF9tjlSHdajRXKYOKuljpqyf7VCri-mk4q5sbQ7j-lBz2DyjXKWs-TJE1py0q82l1xeNG-23-MnbQ9l39f2CkKaWoH8q_-l0PYoq2nL3U4S96wtTw02IePvy1lMFv3kLo2xd4lEr5EyCMCR1lhn3OX-Oe1U1hz7QI7ai__uSnDiFepFJwPxkWnB2Fyw65nrHhgqHDsEUhm3BVDsp8qzimbMouFUVjhOBt_iQrSHRmfwMj5VHVrxrDCzahukUMa-XjCCtFYpxJSSd0nAdW9kE5yktk9TVkogk1_wROVG7XkR3WS7PEs8_iangTcQ3An4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2cfc66ea5.mp4?token=dMi0SVGUsFb3caSZOkqWDsZF9tjlSHdajRXKYOKuljpqyf7VCri-mk4q5sbQ7j-lBz2DyjXKWs-TJE1py0q82l1xeNG-23-MnbQ9l39f2CkKaWoH8q_-l0PYoq2nL3U4S96wtTw02IePvy1lMFv3kLo2xd4lEr5EyCMCR1lhn3OX-Oe1U1hz7QI7ai__uSnDiFepFJwPxkWnB2Fyw65nrHhgqHDsEUhm3BVDsp8qzimbMouFUVjhOBt_iQrSHRmfwMj5VHVrxrDCzahukUMa-XjCCtFYpxJSSd0nAdW9kE5yktk9TVkogk1_wROVG7XkR3WS7PEs8_iangTcQ3An4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقفة احتجاجية في محافظة ذي قار جنوبي العراق رفضا للمشاركة في حصار الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/91868" target="_blank">📅 18:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91867">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وقفة احتجاجية في محافظة الديوانية جنوبي العراق على خلفية حظر الطيران الايراني من الدخول الى العراق</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/naya_foriraq/91867" target="_blank">📅 18:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91866">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a3ae8d19.mp4?token=qMBlNu1NTx_m2in4yCIEu_Sa4cy0hsRJ9Cm8g7a6hknE0yYS6VmyS28jbavpva7J9KNX4LmWA53x-XA5UoZ4RCMUVUuAX05sPWibfTR5JpCkgQnzxMw8-zscdtNBvvPNp5Zp2xOHgE3b0Fb4ytsxF6gUx0iCv8Tf5TZaQwr-9NFZdD9mfBxQb0xLh3jF27-nEA8LhgknwKV-SZgBYbz7l_u9WXEmeeHLwJOLYA6S7Ha-1uU5B7U_LTUxxdDC2CVd-ZC_0BcrbWoeGfNdFMlCeeeOzST0nnHQ2jrH5gXe8DdALPaMG23uMfnH1QIYoSaJlbZINsBtqI3rvDkaK3IgeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a3ae8d19.mp4?token=qMBlNu1NTx_m2in4yCIEu_Sa4cy0hsRJ9Cm8g7a6hknE0yYS6VmyS28jbavpva7J9KNX4LmWA53x-XA5UoZ4RCMUVUuAX05sPWibfTR5JpCkgQnzxMw8-zscdtNBvvPNp5Zp2xOHgE3b0Fb4ytsxF6gUx0iCv8Tf5TZaQwr-9NFZdD9mfBxQb0xLh3jF27-nEA8LhgknwKV-SZgBYbz7l_u9WXEmeeHLwJOLYA6S7Ha-1uU5B7U_LTUxxdDC2CVd-ZC_0BcrbWoeGfNdFMlCeeeOzST0nnHQ2jrH5gXe8DdALPaMG23uMfnH1QIYoSaJlbZINsBtqI3rvDkaK3IgeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ الاعتصامات امام بوابات مطار النجف الاشرف الدولي</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/naya_foriraq/91866" target="_blank">📅 18:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91865">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
الشرطة البريطانية:  حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.  اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.  إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/naya_foriraq/91865" target="_blank">📅 18:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91864">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf9268f87.mp4?token=hptuGB_qNJPKPR6XLx_3JSRcsxAsWqTdY20JfFjUxPZl0Ppo8hY_NRnfl137NjPOrGE9gS_87527ilcXMh9QPDgUx1qOxPGLuamnKnWfqNN6DjJ5Dj6WZ9BoldfimQDj8cYEqRJQLjF95PXNRs87Av3FczMPE_g-F5VKZlEzqa33Zf31O5KHOxxDJZ22SgAvoSwR1c1n1vFov0ylE61bfNpFrlKRPbVQ2Zas04Dc-tIZhGRykOH9JCz_VWolbbM_pWTfp4i3rVYqzWJMEpIMVwG7jCNp7M29WyAJvzN4NuLH1MGjaIi4dH3LZIjsmefmZVVnLK-fL6PNPfzCo6-074i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf9268f87.mp4?token=hptuGB_qNJPKPR6XLx_3JSRcsxAsWqTdY20JfFjUxPZl0Ppo8hY_NRnfl137NjPOrGE9gS_87527ilcXMh9QPDgUx1qOxPGLuamnKnWfqNN6DjJ5Dj6WZ9BoldfimQDj8cYEqRJQLjF95PXNRs87Av3FczMPE_g-F5VKZlEzqa33Zf31O5KHOxxDJZ22SgAvoSwR1c1n1vFov0ylE61bfNpFrlKRPbVQ2Zas04Dc-tIZhGRykOH9JCz_VWolbbM_pWTfp4i3rVYqzWJMEpIMVwG7jCNp7M29WyAJvzN4NuLH1MGjaIi4dH3LZIjsmefmZVVnLK-fL6PNPfzCo6-074i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ الاعتصامات امام بوابات مطار النجف الاشرف الدولي</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/91864" target="_blank">📅 17:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91861">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3lPASVGD68UhGzAcUBS2Fq9LE4DIzGpDjw50ksTsDkMSU7l6Z-GUsOI3DaJAJyEa0RfHF-OQfLKzXFNRomkCkZsFc0Fg75HE3G1fyeTNr5TDV84INipe4KmDWingmt2GB6su3cWMIUvZrErVX8_B41O37FL-MHr92Os9YPksfJdpbkH4te98Fp-83L46yQk_u2qIOkYFupNf01_Hkb0NAORT7mvv-A6R33kPW70AzXveOtF5HjWAc-N0l5gPWvLiT1NWOeV8Th-EcCqLbXWJ5Q2CAw5Zu-sm2KmaS50YhLrmvRjVIHDhF-FhuojIapkBh-1zcH26y7y_AbUh0diYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAniWqCTRhe8ypFZWvscblrvwFmLxWQkMk8t-z0bhOXcG968TSD17N1hpXoZft2yE8u1E_uMowECv1JFoQpQKHAVqMl-LIzdRrwSD5cWNSevilN2HcCQ50Oe_SInC66dHxW8hA_67tpGXP3JV57-h37pb2oiRwvFEj0evaRQk047W7lABYMeZKXD93TjnWPcCXe6zhSYijuM7apCGYzYQ1hvI1QX08prnPD4Vf9NBsOgo3gD4RBRMsKXcZrLtIp2ecc3b8c2zKHPzqfafGkFeomyoPsn-uwG4YZMOL2qVYssCTVno8lsEFnijI_PDa4qt75FC44qwzUMhUQ52rX9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIoX7aOiGHJ8IQ2LlYcYnD09lHnMosw_ec5bBgUlRHn1C67pzf2PH3GdwQ7EATtS-0aYsyIXpAcZR4U3hYYMhsyfkx3y2I0snZSWNorkzUXq90p_XGuWnrmRueXLqtz5a4jTT426Qqbm8yagKIW4ULMVQydAI7-pYUfcyBGB_pHAB2ur1JyOOJ_qmc1fm1CTqABnL1b3PZlt9V6eTQP66DKC-a8Gf6n_VJkWkfck0ij2Kc026XXemOfEcpOpcl1raV8Sp3V333j9ESwfzA0UCvcHf-pf7NrwRBLO2EsHW7PacvYV13LsrucAySeJdt7KWk7pVH_or1xWfnoM0mxwQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من بوابات مطار النجف الاشرف الدولي</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/91861" target="_blank">📅 17:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469d9dfecc.mp4?token=qHcsAOwEF1g_BoU3gP_7LT1J-WlayafiX_NLs4U-AZ8Gb-RIcYJabc1R9HgeG9JOMEklynFm9ebF2Opnf3k1iMx2qiv8kpybk0bQxms2gqCQcVsGe3IaMJIv9Uj7XDbSL8LeOMzhpPeZlBOxwtqawkugwjOj--zFvoRnrSvt_yW0ZKk_26pC3EYHTwGyr7VYVCpemwch0S0Qq83ks2ZbDm5xQxOh5IJNbr6g5nxYHgWFcsF5C4m_lR578FCghqmUQDg3onsybjI__g-na-xa9aEMW5fU-OoEmdNuZXb_tzN3IEhgEAilW6R6wC1ZWKDgmaZKbb272CDne3LO5x_gxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469d9dfecc.mp4?token=qHcsAOwEF1g_BoU3gP_7LT1J-WlayafiX_NLs4U-AZ8Gb-RIcYJabc1R9HgeG9JOMEklynFm9ebF2Opnf3k1iMx2qiv8kpybk0bQxms2gqCQcVsGe3IaMJIv9Uj7XDbSL8LeOMzhpPeZlBOxwtqawkugwjOj--zFvoRnrSvt_yW0ZKk_26pC3EYHTwGyr7VYVCpemwch0S0Qq83ks2ZbDm5xQxOh5IJNbr6g5nxYHgWFcsF5C4m_lR578FCghqmUQDg3onsybjI__g-na-xa9aEMW5fU-OoEmdNuZXb_tzN3IEhgEAilW6R6wC1ZWKDgmaZKbb272CDne3LO5x_gxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انطلاق التجمعات قرب مجسرات ثورة العشرين في محافظة النجف الاشرف استعدادا للتوجه والاعتصام امام مطار النجف الدولي احتجاجا على غلق المطار امام الرحلات الايرانية  #سيادتنا_لاتفرض_بالحظر</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/91860" target="_blank">📅 17:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91858">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03935d9672.mp4?token=YOluFFPEMuZ5lAWJwsVo3nDmb9FqviSMhxuj0-fgOZyYMkQuUJTzCzobbVxgavE2VOKG3SQTWffErH7Sg9Y3V3LH0l2kMa0Se5O9iumxyJr68IHdxwX30jw-F42AMXXCyH08F_IFv9hsZF_GT47IL3bGYAMNx8Z84yRzeXFWMYh4g12NUjrgWeMgQm0xF3HU_Qe7blv1TDAV7crDALpDVplu2EsRZzxFTXqpcZ_lQBt3EZyQdF0TABsg1CbWvUYbLUKiszSrIRq1rHyuhVV9W6a_flBi4RUNBzUtRrj5ch27XSvWQi-SE2Tp8wi41sGgEhVKnrMEcQSK16WzbiV5iGtkpIMEQLzmBuq4ZoMAqCmsaFh0ZPHIsaDSJ0MN-g69EDpVlwLUPxUDvxFjuK1EK1bby4M4oetHrwsUQq30w4AmLwAfvvpsjUp206fz5xEwou5Q7M6koybnvO1yzaq7T2Nde9VIsxoyTCo73UrgUirDdjqt9KRI0jG_AwQls9RwHoOnTEFSr7eeP_2sUhXgbq_2VoAKVW3UsvAt06nmmUbjH1AfpyS_BF6WGdFiT2fDayr6uhrVN6Bp5KiyIVVDxD4nqQTvdn-R7eLPRA3cH0IQSwNoVuxTWKmkF5FUX2oUykAoxU3KF1LT5NBg6nanDxp63_p0-WtGtKNPB5-EewU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03935d9672.mp4?token=YOluFFPEMuZ5lAWJwsVo3nDmb9FqviSMhxuj0-fgOZyYMkQuUJTzCzobbVxgavE2VOKG3SQTWffErH7Sg9Y3V3LH0l2kMa0Se5O9iumxyJr68IHdxwX30jw-F42AMXXCyH08F_IFv9hsZF_GT47IL3bGYAMNx8Z84yRzeXFWMYh4g12NUjrgWeMgQm0xF3HU_Qe7blv1TDAV7crDALpDVplu2EsRZzxFTXqpcZ_lQBt3EZyQdF0TABsg1CbWvUYbLUKiszSrIRq1rHyuhVV9W6a_flBi4RUNBzUtRrj5ch27XSvWQi-SE2Tp8wi41sGgEhVKnrMEcQSK16WzbiV5iGtkpIMEQLzmBuq4ZoMAqCmsaFh0ZPHIsaDSJ0MN-g69EDpVlwLUPxUDvxFjuK1EK1bby4M4oetHrwsUQq30w4AmLwAfvvpsjUp206fz5xEwou5Q7M6koybnvO1yzaq7T2Nde9VIsxoyTCo73UrgUirDdjqt9KRI0jG_AwQls9RwHoOnTEFSr7eeP_2sUhXgbq_2VoAKVW3UsvAt06nmmUbjH1AfpyS_BF6WGdFiT2fDayr6uhrVN6Bp5KiyIVVDxD4nqQTvdn-R7eLPRA3cH0IQSwNoVuxTWKmkF5FUX2oUykAoxU3KF1LT5NBg6nanDxp63_p0-WtGtKNPB5-EewU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان : بدء الاعتصامات التي دعت اليها المقاومة الإسلاميّة حركة النجباء في بوابة مطار النجف الاشرف</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/91858" target="_blank">📅 17:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91857">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGlVublbmy80Fd24FXe_Ep-htGXmDj9N4WmzqBi3a0jBi7fl0U7d7s9HmR9ShdNuemKRy2UXgtGbnC19zUV5Vvo3wJUVnIZcDuaBlXJRu8oomS4X0NA5U9SfvOqaQmP9K4FQJLELFSK3oO1PBS4Kx4hxGMyWzmu9hQm_oCcCId0zToebaq_vhbRPNF_nuT-hntQvp8a4B2hPbxIBxKAp5AbS1E6w40k04aZIVllH47hKqY4HVZ3q6p0rmfrSOob0p7s1ueJ8l8jS9Hz0wkHbDYLbl07J3JrtRj_PhgZsSzr1rdX8NZtOL5lVYARRxxIWuqVDmARRJ8_00YogEjGnog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان : بدء الاعتصامات التي دعت اليها المقاومة الإسلاميّة حركة النجباء في بوابة مطار النجف الاشرف</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/91857" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91856">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
الاتحاد الخليجي يوافق على استضافة العراق لخليجي 28  لا تكطعون بينا ترة حيل حبيناكم</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/91856" target="_blank">📅 16:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91855">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
انباء اولية عن اغلاق السلطات الاماراتية لمقرات قناة الشرقية العراقية في مدينة دبي وهي المقر الرئيسي للقناة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91855" target="_blank">📅 16:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91854">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">السفير العراقي في إيران: مطار النجف الأشرف سيفتح أبوابه أمام الرحلات الإيرانية خلال 24 ساعة</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91854" target="_blank">📅 16:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91853">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed462a036f.mp4?token=jlz9aG3yroQPX9RWPUhOfiC9toYlF1nPMyXMoZqM7cmUnZhvW9vQi4S2EUlJwKjXof1_sirHqvW-dMNBXNsOF-qzzyQhPDj8MeRH-IPAlPsnuIFtvAQG4S6RKJ7U4KfyPX6rvL8y5FzWH7txcCDgcMvNLYV7q9fbQiPPXRBL3o82X-aQujaQjaNP8wzx3baPSqNalhmPxEYc18OF1OScoIpmuZ886Ylkob3bymL-YaX7D61HUXl7NqyisKp0DGVORijatVG1XSk-PCtmRJEn21wzCN8SXshsg1T1BNpO_jNSmpuOI49uWfUMBAhh-F8HAqdDXjDZb1ynKuSP9jORKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed462a036f.mp4?token=jlz9aG3yroQPX9RWPUhOfiC9toYlF1nPMyXMoZqM7cmUnZhvW9vQi4S2EUlJwKjXof1_sirHqvW-dMNBXNsOF-qzzyQhPDj8MeRH-IPAlPsnuIFtvAQG4S6RKJ7U4KfyPX6rvL8y5FzWH7txcCDgcMvNLYV7q9fbQiPPXRBL3o82X-aQujaQjaNP8wzx3baPSqNalhmPxEYc18OF1OScoIpmuZ886Ylkob3bymL-YaX7D61HUXl7NqyisKp0DGVORijatVG1XSk-PCtmRJEn21wzCN8SXshsg1T1BNpO_jNSmpuOI49uWfUMBAhh-F8HAqdDXjDZb1ynKuSP9jORKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات مجهولة ترفع علم اقليم كردستان في محافظة كركوك شمالي العراق وتقطع الطرق لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91853" target="_blank">📅 15:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91852">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الاتحاد الاوروبي: تحركات الحوثيين ضاعفت المخاطر في طرق الملاحة الحيوية، مضيق هرمز وباب المندب والبحر الأسود نقاط اختناق حيوية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/91852" target="_blank">📅 15:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91851">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وكالة رويترز: يجري حاليًا نقاش حول نسخة معدلة من المقترح الذي قدمته إيران خلال فترات راحة جلسات الجمعية العامة للأمم المتحدة، وذلك بهدف التركيز عليها.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91851" target="_blank">📅 15:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91850">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وكالة رويترز: يجري حاليًا نقاش حول نسخة معدلة من المقترح الذي قدمته إيران خلال فترات راحة جلسات الجمعية العامة للأمم المتحدة، وذلك بهدف التركيز عليها.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91850" target="_blank">📅 15:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rI1A1EEgGTN6Bl-142MHVmCMTrh-KLSYlCrkr5DLGp_dlRXoNH7CFV2E7-qX8JDm-_cqPnF0UAnnUrxZjzyYqD222-LFg6XVXzEhBRDyppNNjOnlBf-FWoVKVHI0H7GoQ_DSM70saJv9w4YimsNRdpWXyrMaM3HyplO-j5s-w3eaQV0n7BIQwMXyGmM3GY5cSAsLSwZf8Tz1LCNMnX7mwUjBLmSTOl_owIGj034JVxSV0WclOToRg_niq7kKsYC-LvBlTRDsjRLggUYbN8n4J-2UhniXQiymOksTUQwGUJbriasiLyA5-R7ToTv9FVwZeccRMxDJkJle6_fwTlrMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkiWMgEV7hOgT9VHWME8qljZUMpMMhLh8RKX8mU9WFXiTf5L1cr08zec5vMSpz9aYTHkNis7ZO1xB0MoAiHWqXxcCtVaTGeh_kA4Gh7gu-g0G_GKtTt86ghpGfHuN-g9K4hruQZtYh9pCzFv0IzpwXRkTgUJF9GHuA4Lb3wKZO6HptOyHurqd0ogXvVpirczBiH0J5Gk-L4b3HMH1anB0SPdc4alflAFhC21vtk5xqU7UtL0OQn5pLBrfS4ztHlMErV3qBQdiDla7GlDcH5vI1LbajJ6BmAePiK357JtXWsGT9_8WNOwtvSF459s1Jm3dZaOOxFkntMyNHQSUbnbDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اطلاقات جديدة في هذه الاثناء من الاراضي اليمنية تخرج لدك حصون ال سعود</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91848" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجارات في جازان</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91847" target="_blank">📅 14:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجارات تهز الجنوب السعودي</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91846" target="_blank">📅 14:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات تهز نجران</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91845" target="_blank">📅 14:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات تهز نجران</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91844" target="_blank">📅 14:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حكومة إقليم كردستان العراق تعلن تعطيل الدوام الرسمي في جميع مؤسساتها ودوائرها يومي الأربعاء والخميس بمناسبة يوم السيادة</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91843" target="_blank">📅 14:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">كميات كبيرة من مياه نهر الفرات تتجه للاراضي العراقية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91842" target="_blank">📅 14:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY1HMj81jvrDETrrd72zO-kVGs6o2K5nptwZm7z1ZXDkF1wxfm7HqVBTZ0ZzZ5Nx_3R4rZLHJtOHxyRt2FwMDLB0Z2-SDWRmrn6T3VkinP3VkM-QDMCybK8sU6FWqMKx-qfYgYP8KvxC2W4f_vIPVMf1Y49Ef8zsnB4d85LiAItTCdtKZZ5rskSZ3KrE94TYKa50WwbhGz2lVdSeb95tqZ48zlVLYXZkrN1eFVCfBaZK-jUdyW2l9d5thhsKqo4dAM8n4grXva6Q7HYU2jAs33-0YB7F8mGwRORrmSBMsXrC_Z0PUhCxRWERbj3zZBFuHaDSnrExiXlq9o65ROljfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رسالة من القائد الأعلى للثورة الاسلامية بمناسبة أسبوع الدفاع المقدس وذكرى استشهاد الشهيد السيد حسن نصر الله:  بسم الله الرحمن الرحيم  وَلَقَدْ أَرْسَلْنَا مُوسَىٰ بِآيَاتِنَا أَنْ أَخْرِجْ قَوْمَكَ مِنَ الظُّلُمَاتِ إِلَى النُّورِ وَذَكِّرْهُمْ بِأَيَّامِ…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91841" target="_blank">📅 14:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
في غضون ساعات، سيتم نشر رسالة من قبل قائد الثورة بمناسبة أسبوع الدفاع المقدس وذكرى استشهاد الشهيد السيد حسن نصر الله.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91840" target="_blank">📅 14:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91839">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
الاتحاد الخليجي يوافق على استضافة العراق لخليجي 28
لا تكطعون بينا ترة حيل حبيناكم</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91839" target="_blank">📅 13:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91838">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAqeYYVNf47TM-X5bCChyMkXrS375WRWnPNm3hIoI1sIBusseurjzVCfS-fEzUCc0uz8n5EFyBFzVqnl25l-sZFSldDV2Eg3Jr0dz7oVuuDe0RAws35wrsTTA3mC0LguaFx-DGPD31fECTwhTPkWNxfaZbEuB4KSWS5YblcvOkxSS4LiN8jmRtBUDR-wL4zllwzqa5WZBLOqVIxKaBbHBEhWP2iDHimHTGrajT1xh0hTZXz9hUajbkAOs5Eh0-_d1WYxmJH0GwNiZ5p4NkMFY7QtkGhIj02Q_3fKXI53rMd73NNEdM0-lGSPNweYoeGMs5LmPaaXe7IlHkEtiMdWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
‏خام برنت يرتفع 4% عند 109 دولارات للبرميل مع تعثر مفاوضات أميركا وإيران.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91838" target="_blank">📅 13:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91837">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔻
الخارجية البريطانية:
لن نستسلم أبدا لتهديد روسيا ولن نقف مكتوفي الأيدي ونتخلى عن شعب أوكرانيا.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/91837" target="_blank">📅 13:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91836">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
في غضون ساعات، سيتم نشر رسالة من قبل قائد الثورة بمناسبة أسبوع الدفاع المقدس وذكرى استشهاد الشهيد السيد حسن نصر الله.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91836" target="_blank">📅 13:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91835">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmGK8Ckhy3xdR1FvVJp37qY0rLRK689YouP_DxogAUu7DXfDMeQNktB3PQlNAVjeOy726Bil_TuU0EawCK9owLAquhSamyzx_yO9STrK075alXd11z_u2liixf9k13GASXz3OXCtE2_i-f3kVQPBR_6Aqs-Zqq_qFP5I_xU1R2Ob3rMs-noe_25paU_ktFdx7yP4Lx1Yq2BFqmns4Q3FFOIzAQJ5CpZh0NtcsAONCV5tU62wQe66DT_Tma0u_uUpx7ycOoMVKxVLzwSyF-IN5eLIeNBzwsv6c4PJz6bi3nrXv-AOY5Hrwl0iHRVub1UkbfjXo14JccsrxLn-kShoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#لا
أُعطيكم بيدي إعطاءَ الذليل
ليست كلماتٍ عابرة، بل صوتٌ من الإباء والعزّة والثبات.
وفي الذكرى السنوية لاستشهاد سماحة السيد حسن نصر الله، تتصدّر العبارة جدارية الفردوس في بغداد، شاهدًا على ذاكرةٍ تحفظ معاني الكرامة والصمود، ونقشًا يتردّد صداه في الزمن.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91835" target="_blank">📅 13:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91834">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
🇮🇶
مطار الإمام الخميني:
لم نتلق أي إشعار باستئناف الرحلات الجوية من إيران إلى النجف.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91834" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91831">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91831" target="_blank">📅 12:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91830">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91830" target="_blank">📅 11:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91829">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
‏
خلية الإعلام الأمني:
تسلمنا المقر الرئيسي للقوات الأميركية في مطار بغداد.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91829" target="_blank">📅 11:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91828">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58edca218.mp4?token=IDkqCmNnZOzvUCVQS7gtP5219ujYLzIfYTscuSre2eMCIicOCII7BsCsc3qV8w1jC0MsOkybob9tVjemIGXi2ThOlEMmAO9Ku4UO74uqORas-ss8iR0SwZEyrTkMwczThLBPPU7CG87K0l3v44pbb31bMXmibafF-Dnph1STwwzbhwQmu7ZKzIbXKQEGTb1BhE5ughOrAnYCss-kTy5LM60Yf0faUlAJWUYbTRKGPIo-PVb4FFJHIvDF9utP_NpeL0slNVn3XUjfU6IbV2_sfaBkAhu-TI566kIk2IU98g7s8nigVPmFXha-XdC2pYttoaAgBIDfg_n3hGoaBIPB8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58edca218.mp4?token=IDkqCmNnZOzvUCVQS7gtP5219ujYLzIfYTscuSre2eMCIicOCII7BsCsc3qV8w1jC0MsOkybob9tVjemIGXi2ThOlEMmAO9Ku4UO74uqORas-ss8iR0SwZEyrTkMwczThLBPPU7CG87K0l3v44pbb31bMXmibafF-Dnph1STwwzbhwQmu7ZKzIbXKQEGTb1BhE5ughOrAnYCss-kTy5LM60Yf0faUlAJWUYbTRKGPIo-PVb4FFJHIvDF9utP_NpeL0slNVn3XUjfU6IbV2_sfaBkAhu-TI566kIk2IU98g7s8nigVPmFXha-XdC2pYttoaAgBIDfg_n3hGoaBIPB8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
وزير الأمن القومي الصهيوني إيتمار بن غفير يقتحم المسجد الأقصى.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91828" target="_blank">📅 11:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91827">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91827" target="_blank">📅 11:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91826">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571119c9bf.mp4?token=XYkucn0e4JzPUUAW-Y0JlciAb3O068QhiJvINwtkFEoQXDwC9AOFOmBMeO7xYeGwTKPjf6zG6i3scgefS67ZAcxnhpn4QsOCkboCrGzCcLLU224FHku338a09kwhArIuZzIEkdS9oh2q9LxZ9P59cVqRf8fm4XL_SXuW5TOeBvWwD2QV0u48mp2MKA6a7KIAD0GfJCqWqT6bHM_g8z4L5LWDn_YSzYjanD3D0Vm3bnYT0NrJndZl0q4E1IV5vKPuSe_NiEj-Nyw59Zv-of4CmzMljpCrbHWGexPqWLcb936ogfnbOuLMukP60bKLELdSWXgvmetSX0_NuNMNhmQryCPacwVHflvgi3sJRtuAd_qn4i_K6Zx7ukKNS8E88quQhfNDvtuXDfP4kYSZiwiUkD7Xd1DZUQJzCcfOfT0CYZV3rXcK-jSWmTC-PUqBfq092n_6wUt7lsdZVGOX3RQ7YhjYyhPra3cq-FuDc_i3ctUxe4zF_BvQpZ00QGed7v-kvSy2XwOPlXjh0yU0QF7CxklWVgkOGI_vG-3WYADOrOFOkiev66nLmBvrllkr3A4TRPml3XF97tqZQwhpZYtBl2FFI0AzJPqHIj6vRQOq18Rq9fBoAxoTU_JokE7oDjxHnk1MuBFHbqVQ1s18Zk8wESVQ2aBvjZqwgdOvhexHt0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571119c9bf.mp4?token=XYkucn0e4JzPUUAW-Y0JlciAb3O068QhiJvINwtkFEoQXDwC9AOFOmBMeO7xYeGwTKPjf6zG6i3scgefS67ZAcxnhpn4QsOCkboCrGzCcLLU224FHku338a09kwhArIuZzIEkdS9oh2q9LxZ9P59cVqRf8fm4XL_SXuW5TOeBvWwD2QV0u48mp2MKA6a7KIAD0GfJCqWqT6bHM_g8z4L5LWDn_YSzYjanD3D0Vm3bnYT0NrJndZl0q4E1IV5vKPuSe_NiEj-Nyw59Zv-of4CmzMljpCrbHWGexPqWLcb936ogfnbOuLMukP60bKLELdSWXgvmetSX0_NuNMNhmQryCPacwVHflvgi3sJRtuAd_qn4i_K6Zx7ukKNS8E88quQhfNDvtuXDfP4kYSZiwiUkD7Xd1DZUQJzCcfOfT0CYZV3rXcK-jSWmTC-PUqBfq092n_6wUt7lsdZVGOX3RQ7YhjYyhPra3cq-FuDc_i3ctUxe4zF_BvQpZ00QGed7v-kvSy2XwOPlXjh0yU0QF7CxklWVgkOGI_vG-3WYADOrOFOkiev66nLmBvrllkr3A4TRPml3XF97tqZQwhpZYtBl2FFI0AzJPqHIj6vRQOq18Rq9fBoAxoTU_JokE7oDjxHnk1MuBFHbqVQ1s18Zk8wESVQ2aBvjZqwgdOvhexHt0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مسعود بارزاني: في حال انسحاب القوات الأميركية لن يكون هناك ضامن لمنع عودة تنظيم داعsh الإرهابي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91826" target="_blank">📅 10:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91825">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmNII-fGJEfI8LeLaY0-qcC7sNC_4xAgd103QPG0dK0s3AcLYzjWx0X9ixIQGhrxKpmhy068NJeiyQRCJSBaHOEqhbIjTmGCwRtfSfKDOBpRyzdEG-NjJt2w9R4-LKGAPKbJz-fOxzJxmHX1zyFx31moGp_eBbAqaKHwgChP63P3z1GsvWDo3w6M5PHtLZQLuakTtoNcbeOmWn8noHA-8HxyUWkhnDxmxBxj0gLAbOeLndTBZG3_s8wrrEH8TlARfY8rcySIgHqOspXJZF3rxNKhHCsJWEQgqpDBfGriYwLiyAj9OpgN8vHdQT3fRfyzo6WTpZ7_UKiGVzFGeoQLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية تستمر في الإرتفاع لتلامس 108 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91825" target="_blank">📅 09:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91824">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اصابات مباشرة لمقرات الاحزاب المخربة في اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91824" target="_blank">📅 09:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91823">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇱
إعلام العدو:
التقدير هو أن حماس لا تزال تمتلك 30 ألف مقاتل، بالإضافة إلى ذلك، تستمر في إنتاج الصواريخ وصيانة الأنفاق داخل قطاع غزة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91823" target="_blank">📅 08:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91822">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الله اكبر
🇺🇸
اصابة اكثر من ثمانية جنود من المارينز في مضيق هرمز اثر تعرض سفينة لهم بصاروخ كروز بحري اطلق من قبل بحرية الحرس الثوري التي اعلن ترامب انها دمرت.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/91822" target="_blank">📅 04:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91821">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏ترمب: تم تدمير السلاح النووي في إيران ولا يجب ان نقلق بشأنه بعد الآن</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91821" target="_blank">📅 04:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91820">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سماع دوي انفجار مجهول في اربد شمال الاردن</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/91820" target="_blank">📅 04:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91819">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34e34e8eb.mp4?token=PVTQN-eWUWOKBvV5Hfv4QqUQV4JEYQDGQ4eQH8W3e6ekwHih6xRNmziYTIxVtJw8J8b1itj3JYcF4zKsG0m3bON8L8P8HcYBSJw9QCn4F7F2k0Qf1gowNAzyt5O5nIGj6L5WQC82PDECJNJNKViM-qpLz87B23om_Hef2HBVgx9mWQ8SKHFkk-tudlmay0CAKWdysw9Dr8GaOL2qPQsc3ZqbGC0j7huGtTbNLw3AnTTZHA9v9nt4GD5SM2JgrR8cTvxhJsASawwfPF9mtSUAa22V929R5q2B2-_wKGrURf2l_hs4GMjaUORwNke9vqK5bVfjSqaQjCH0etvEWJ_ssA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34e34e8eb.mp4?token=PVTQN-eWUWOKBvV5Hfv4QqUQV4JEYQDGQ4eQH8W3e6ekwHih6xRNmziYTIxVtJw8J8b1itj3JYcF4zKsG0m3bON8L8P8HcYBSJw9QCn4F7F2k0Qf1gowNAzyt5O5nIGj6L5WQC82PDECJNJNKViM-qpLz87B23om_Hef2HBVgx9mWQ8SKHFkk-tudlmay0CAKWdysw9Dr8GaOL2qPQsc3ZqbGC0j7huGtTbNLw3AnTTZHA9v9nt4GD5SM2JgrR8cTvxhJsASawwfPF9mtSUAa22V929R5q2B2-_wKGrURf2l_hs4GMjaUORwNke9vqK5bVfjSqaQjCH0etvEWJ_ssA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابات مباشرة لمقرات الاحزاب المخربة في اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/91819" target="_blank">📅 02:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91818">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886951be8e.mp4?token=jFa2W6KSjNYOTWK994u1GncsOdnfjlTlVsFbXzApbj_KIilbRTKaZwQ1RDbpsTVR7StCrK8VkPwwU4HHYT3bfmTnfsKd_QSPw3MdASqEy8gc31Qtv8bysYSSheXbeoxsFBlCRHk56MbYpELkwqtLfFvi0WutGCg8-yV9Qfyo424qdpGnCarIfAVdpSJhYoxawSERxm9P8ehRMLplQnt-mxx_LYDV8ivQFLvAFMcilhPxo0WAHXlEHO-ZlkH6gdiUJ1cGEEp-05KTihtAu7z-AKtWASrU9RDAzdjXbqjsnaGOfkpM08t12inLYWb5OCMYJYZ24byFt_zLzUSmRvSnSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886951be8e.mp4?token=jFa2W6KSjNYOTWK994u1GncsOdnfjlTlVsFbXzApbj_KIilbRTKaZwQ1RDbpsTVR7StCrK8VkPwwU4HHYT3bfmTnfsKd_QSPw3MdASqEy8gc31Qtv8bysYSSheXbeoxsFBlCRHk56MbYpELkwqtLfFvi0WutGCg8-yV9Qfyo424qdpGnCarIfAVdpSJhYoxawSERxm9P8ehRMLplQnt-mxx_LYDV8ivQFLvAFMcilhPxo0WAHXlEHO-ZlkH6gdiUJ1cGEEp-05KTihtAu7z-AKtWASrU9RDAzdjXbqjsnaGOfkpM08t12inLYWb5OCMYJYZ24byFt_zLzUSmRvSnSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المسيرات تتجه الى اهدافها لدك مقرات المعارضة المخربة في شمال العراق</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/91818" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91817">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوي انفجار في اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/91817" target="_blank">📅 01:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91816">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd346d3b8.mp4?token=PmWlppmroNEP8SnorQmHtGbKSRk99aY3DN0CQY-A_xPgkGRRc0AeDew62kbfi1BHlsqBzNq3Bkj1TzKdmt0NMhRa3SnPYjlIA7Vm1su_iRnE7Cgp0P6rl9lq0dgxOoXQvhb5n3GMGZhkLTc9zCG0KdfOJBqNuP-LcRDMFQ1b26PtVqt87zkJKkxilUTP9Zyc22UkF1ZuSn0xKmXXycy2Ebz2KKTp9tbTepizLiyBocU4seshQi_-o56FH_S6djtOCG2j5tzPupbf3KKY2sqU2G7IWbjeBDxBONqEMNJ69939cZ7hzbXEqrY0kdeMtL615Ks3pcJ3flBlCVShsHYVnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd346d3b8.mp4?token=PmWlppmroNEP8SnorQmHtGbKSRk99aY3DN0CQY-A_xPgkGRRc0AeDew62kbfi1BHlsqBzNq3Bkj1TzKdmt0NMhRa3SnPYjlIA7Vm1su_iRnE7Cgp0P6rl9lq0dgxOoXQvhb5n3GMGZhkLTc9zCG0KdfOJBqNuP-LcRDMFQ1b26PtVqt87zkJKkxilUTP9Zyc22UkF1ZuSn0xKmXXycy2Ebz2KKTp9tbTepizLiyBocU4seshQi_-o56FH_S6djtOCG2j5tzPupbf3KKY2sqU2G7IWbjeBDxBONqEMNJ69939cZ7hzbXEqrY0kdeMtL615Ks3pcJ3flBlCVShsHYVnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصوات مسيرات  في سماء اربيل شمال العراق</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/91816" target="_blank">📅 01:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔹
زلزال قوي يضرب جمهورية الدومينكان .</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/91815" target="_blank">📅 01:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/91814" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات عنيفة تهز العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/91813" target="_blank">📅 01:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/91812" target="_blank">📅 01:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSGQOLFQI62VJFL_wYcj_7rfQZFmA_MDu6z5f-m0MXwZKA2r2YOe3Q8-OACdRgrJdQJadlwHkjnMDpVh1oRegHapFyPI4y-Y45G48kRjKpUkMLIAhA7bst8oRLYSzPJXGxLd4Kb7HtPjP2rUvm-qwZ6aNLI06paQnkjunHGwZ9us8oh8Sxq-f8WxYQUEcAPHepuPou_3azXrH_1LUP3aDNkWz3OQ-L373QcsXp8Wied03qYCZ_C3r9seGP-txZ2CeWw6WiLRZy0j-YSPq-XeD1ZFk9BsOMQrXh2MLkIoz7zn8AKAIHsoq3EyuWbVO0nAOfZpREN7GLlB7vzIFwTgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
This is the ugly world we live in a comprehensive crime, whose harm has affected children, women, and civilians, is being promoted and celebrated from the platform of the UN
May God have mercy on the late leader, Muammar Gaddafi, the martyr who tore up the United Nations Charter on television.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/91811" target="_blank">📅 00:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca41f5abb5.mp4?token=MA-qfsvkRTr6wjYRr1D-qBOK9xxPLpYhHn00Nb0secR8c3-exOVNphMGmzG_nl3P3y4AKf7PoCIiVSKXSNwdZqGjKCk-nZGM1y_vAw2I_3VKjMKs4wJ71udNcFO7_O1Z52qsZ2clAT1cFf19LppLKlXdmCct9VmuoCR-necH7-MmZlicdabK9piS8SQ2FxdgEfsQYuWWE7f5W_3NMgio854MDlp5hzhlpHpyiS_AnTSKm2Xu1iEOJXJlXMNTIDOXUH29Gz6qRPhasnoNM2KCOFxLxU41VIHK69q3V8yqbGHXUdLdoECU_-2PUiSgxcGYOWfvn4ATdlM7uIFLrT9ymw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca41f5abb5.mp4?token=MA-qfsvkRTr6wjYRr1D-qBOK9xxPLpYhHn00Nb0secR8c3-exOVNphMGmzG_nl3P3y4AKf7PoCIiVSKXSNwdZqGjKCk-nZGM1y_vAw2I_3VKjMKs4wJ71udNcFO7_O1Z52qsZ2clAT1cFf19LppLKlXdmCct9VmuoCR-necH7-MmZlicdabK9piS8SQ2FxdgEfsQYuWWE7f5W_3NMgio854MDlp5hzhlpHpyiS_AnTSKm2Xu1iEOJXJlXMNTIDOXUH29Gz6qRPhasnoNM2KCOFxLxU41VIHK69q3V8yqbGHXUdLdoECU_-2PUiSgxcGYOWfvn4ATdlM7uIFLrT9ymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوافل الاحتلال الاميركي تستمر في الانسحاب من محافظة اربيل الى خارج العراق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91810" target="_blank">📅 00:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91809">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eff26c4ef.mp4?token=tTxAPmhBvclrAofBZvI9aHy0X7FxqFrVOiDYWOwekx5-XirAIw3_yQFE-u_eyPW8dj_EvakvxVoxW7QV6NN1yUZC-HKdGcSh1uGwj4ZFaqA4OBEre9WC3GN_Ee5BjfGjnhI9Wnu_KYTTtWdlrjNXj83-iRzxJ0JuZlPvclgi2cGivnw0IvKxFr5B19uZVsthWAq-lV5_qEnB8CBX2hJwYvXubXn1UBCCQJM019FiLY0k_hdGi_WiM-lWKjvrypfn8fEf1Q-VObXlbfG9FU3tsYWcKGpdHRNe2BGrl7M791EsYK6dmomKHAtyo4cAuvSqwYErHUXZ9_WFQdiWSrlpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eff26c4ef.mp4?token=tTxAPmhBvclrAofBZvI9aHy0X7FxqFrVOiDYWOwekx5-XirAIw3_yQFE-u_eyPW8dj_EvakvxVoxW7QV6NN1yUZC-HKdGcSh1uGwj4ZFaqA4OBEre9WC3GN_Ee5BjfGjnhI9Wnu_KYTTtWdlrjNXj83-iRzxJ0JuZlPvclgi2cGivnw0IvKxFr5B19uZVsthWAq-lV5_qEnB8CBX2hJwYvXubXn1UBCCQJM019FiLY0k_hdGi_WiM-lWKjvrypfn8fEf1Q-VObXlbfG9FU3tsYWcKGpdHRNe2BGrl7M791EsYK6dmomKHAtyo4cAuvSqwYErHUXZ9_WFQdiWSrlpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مسعود بارزاني: في حال انسحاب القوات الأميركية لن يكون هناك ضامن لمنع عودة تنظيم داعsh الإرهابي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91809" target="_blank">📅 23:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91808">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">كوريا الجنوبية:
وافقت كوريا الجنوبية على إبقاء عملية نقل أسرى الحرب الكوريين الشماليين سرية بسبب مخاوف أمنية ودبلوماسية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91808" target="_blank">📅 23:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91807">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f241fbcd.mp4?token=RMvMeg-f9Co6F9aES_p4WNSmsuhHqYLjDxub_cCkDNCtDgtrNZRynQyvJPYqGVfyPs50l0ijSnYBHwlWaMU86a-ytXwVOBd9DVEY2pG12g6uJryZh9bT1eFy0PBnJLJEt1Ur2Zqd6GqNscdQN1S1LAtzU63bNomac5w23YDJcl6mCQftdh87wMHDB9pd6_MVTGQXxVaTWvazKNLOjLOmEn10bZuO0Be2crRCJZTysLaFbVUYAuPyZNg-PhaG0hu5FFPqJLdFIfnLXIbGod7dESoOUocp-xIM22kZ2XtZfGLE3eZGRmPRjdrJsue7WIq8Zv7f1nZ2JFUGcQdGIzBnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f241fbcd.mp4?token=RMvMeg-f9Co6F9aES_p4WNSmsuhHqYLjDxub_cCkDNCtDgtrNZRynQyvJPYqGVfyPs50l0ijSnYBHwlWaMU86a-ytXwVOBd9DVEY2pG12g6uJryZh9bT1eFy0PBnJLJEt1Ur2Zqd6GqNscdQN1S1LAtzU63bNomac5w23YDJcl6mCQftdh87wMHDB9pd6_MVTGQXxVaTWvazKNLOjLOmEn10bZuO0Be2crRCJZTysLaFbVUYAuPyZNg-PhaG0hu5FFPqJLdFIfnLXIbGod7dESoOUocp-xIM22kZ2XtZfGLE3eZGRmPRjdrJsue7WIq8Zv7f1nZ2JFUGcQdGIzBnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇾
العراق يستورد أول شحنة بنزين عبر المواني السورية باتجاه المعابر الحدودية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/91807" target="_blank">📅 23:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91806">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c7c2387b.mp4?token=PVkaE2psPzRduM2m31LyVM6C9VY-Nb43R9uuFpXSX_MuRIVdqhTbxlXlzMMKj04j27uyMNyg4oV1xkzERT4T7PZTFbv1BlvrmjbVUoxv0r6V1yj0iO7xVNthQ9KkHArJxmbH5MAp54DgtLCYp-iYmPZ1HmTHLgA4LFZiGzYXKlHNMSkHqNG5mD5npDzzwWlFwc3P1Z07_SuXhEWXBrLxRuDUeOujTD0GXJ0nzEnUty8ArdnZdMzJ1jP5CD39lukr7xO8qxAzdeWKA4O7cZALE3mY74pc-SAGXVmvGQLdURe0OIHxYfj-Se0mDbI4dW43UhPsjN15v17hYy9aHj5vLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c7c2387b.mp4?token=PVkaE2psPzRduM2m31LyVM6C9VY-Nb43R9uuFpXSX_MuRIVdqhTbxlXlzMMKj04j27uyMNyg4oV1xkzERT4T7PZTFbv1BlvrmjbVUoxv0r6V1yj0iO7xVNthQ9KkHArJxmbH5MAp54DgtLCYp-iYmPZ1HmTHLgA4LFZiGzYXKlHNMSkHqNG5mD5npDzzwWlFwc3P1Z07_SuXhEWXBrLxRuDUeOujTD0GXJ0nzEnUty8ArdnZdMzJ1jP5CD39lukr7xO8qxAzdeWKA4O7cZALE3mY74pc-SAGXVmvGQLdURe0OIHxYfj-Se0mDbI4dW43UhPsjN15v17hYy9aHj5vLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد تصريحات مسرور برزاني الاخيرة والاشتباكات التي حصلت بعد التصريحات بساعات.. استمرار وصول التعزيزات العسكرية إلى محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91806" target="_blank">📅 23:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91805">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91805" target="_blank">📅 23:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91804">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
اشتباكات مسلحة في محافظة دهوك شمالي العراق اصابة ١٥ شخص كحصيلة اولية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91804" target="_blank">📅 23:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91803">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
سافر نتنياهو اليوم إلى الإمارات العربية المتحدة للقاء الرئيس محمد بن زايد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91803" target="_blank">📅 22:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91802">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">إعلام بريطاني : الهجوم يقف خلفه عناصر من استخبارات الحرس الثوري الإيراني</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91802" target="_blank">📅 22:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91801">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
الخارجية العراقية:
القوات الأميركية أنهت انسحابها تماما من العراق، ويونيو المقبل سيكون موعدا نهائيا لإتمام عملية سحب سلاح الفصائل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/91801" target="_blank">📅 21:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91800">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a9584f77.mp4?token=tv-6zkSSoIXTWlTNqZA94SPsJqBQwAKBoU1SnIu2VxMnUre1Wml7grqIo3GRCcb-SU0I2qy8b1W8r4f3fPrPsi-FguP6rGjXbiQrekZubkRkoQDc9wTraEpbxuznyQRb_oByJYHDTFlnAZoQuT-5wrfBmMglYAGtH4twf062ayA8ROZIBo923O818n1vpalsCcIJlBYpmbAMeaTUOfCvEgtOu0FgCfVQjfmvm2l9sPXQsGLgv_iAV1MTDhgMyx9R4bBGgnFS7EOqQBgVDEatBUyDkMh8XjuoUUXdXHV3RxzzTjOFd9rO-gb18b39wD7kIBJkVM3FPcVgvNcuw2H9mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a9584f77.mp4?token=tv-6zkSSoIXTWlTNqZA94SPsJqBQwAKBoU1SnIu2VxMnUre1Wml7grqIo3GRCcb-SU0I2qy8b1W8r4f3fPrPsi-FguP6rGjXbiQrekZubkRkoQDc9wTraEpbxuznyQRb_oByJYHDTFlnAZoQuT-5wrfBmMglYAGtH4twf062ayA8ROZIBo923O818n1vpalsCcIJlBYpmbAMeaTUOfCvEgtOu0FgCfVQjfmvm2l9sPXQsGLgv_iAV1MTDhgMyx9R4bBGgnFS7EOqQBgVDEatBUyDkMh8XjuoUUXdXHV3RxzzTjOFd9rO-gb18b39wD7kIBJkVM3FPcVgvNcuw2H9mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
مشاهد أرشيفية من سجون النظام البحريني للحظة إعلان استشهاد سماحة السيد حسن نصر الله وردود فعل الأسرى عقب سماع الخبر.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91800" target="_blank">📅 21:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91799">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مشاهد ارشيفية للشهيد الاقدس السيد حسن نصر الله والشهيد الجنرال قاسم سليماني.  الشهيد الحاج قاسم سليماني قائلا: سأضحي بحياتي من أجل شخصين؛ أولاً، القائد الأعلى للثورة، وثانياً، السيد حسن نصرالله.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91799" target="_blank">📅 21:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91798">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91798" target="_blank">📅 21:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91797">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇱
وزارة خارجية الاحتلال الإسرائيلي:
ستنتهي حصانة دبلوماسية المبعوثين الهولنديين في رام الله في غضون سبعة أيام.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91797" target="_blank">📅 21:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91796">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537ca099d6.mp4?token=hlBD2nvirN3hyJXHe084enbTwmdXY3DFaryPk8J_-Hte8PWpFHaDsXa_CmCjsYHhIb9DQsgV8u5mQP3DyyIIqm-XNXcaa1kIqR6dIifOhPqiOZXEz5HRMQib9xVHlZuMuxuS4m8abfh2FaJvFWwEbR39pdkfF8ZQ6fDKuAD6ZtJi4_L_GZuHPqKCVtsMu3vulDCrmuQf-XHHEphJDo4rkxHnd2stKX5p0q1K3pMqu1Y_J1stjdkxSAOPemiJDrL8xmPs-wPB2IvHgf3NFjyxIZEWXGmOlpDJBkjB2UhL88QWiRAXhB-VH-pSqQGFuHsKFDDGKxErhsam8QDi45DiBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537ca099d6.mp4?token=hlBD2nvirN3hyJXHe084enbTwmdXY3DFaryPk8J_-Hte8PWpFHaDsXa_CmCjsYHhIb9DQsgV8u5mQP3DyyIIqm-XNXcaa1kIqR6dIifOhPqiOZXEz5HRMQib9xVHlZuMuxuS4m8abfh2FaJvFWwEbR39pdkfF8ZQ6fDKuAD6ZtJi4_L_GZuHPqKCVtsMu3vulDCrmuQf-XHHEphJDo4rkxHnd2stKX5p0q1K3pMqu1Y_J1stjdkxSAOPemiJDrL8xmPs-wPB2IvHgf3NFjyxIZEWXGmOlpDJBkjB2UhL88QWiRAXhB-VH-pSqQGFuHsKFDDGKxErhsam8QDi45DiBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ویدیو المنار از حضور شهید سید حسن نصرالله در حومه جنوبی بیروت ودر میان مردم لبنان.  @Naya_Press</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91796" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91795">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇾🇪
مشاهد حطام طائرة استطلاع مسلحة نوع "كاريال" تابعة للعدو السعودي أسقطتها الدفاعات الجوية في أجواء محافظة حجة - 27 سبتمبر 2026م
.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91795" target="_blank">📅 20:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91794">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامب: الاعتقالات في المملكة المتحدة تمثل تطورًا إيجابيًا. المشتبه بهم كانوا تحت المراقبة لفترة طويلة، وقد تم القبض عليهم.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91794" target="_blank">📅 20:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91793">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 26 غارة جوية من خلال طائرات "F15" أقلعت من قاعدة خميس مشيط واستهدفت محافظات تعز والجوف ومأرب وذمار وصعدة.
‏وخلفت عشرات الشهداء والجرحى من المدنيين
‏ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1085 غارة جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91793" target="_blank">📅 20:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91792">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeTYzxpUKC9qI2zFopVzCDSjgz_09X7PoATKKEXlZZb4FRN7qG4XmhYwLcjILYOCLIciKBpmQlzz2Zwj-eQlBpvrhaocOH3d0HY73NY20L46xnFoU1Zg5n7hu2RHGH9kieQCsTkulQeuzSwLbaGFDZPNOOhGvapV8WoAr6uhIZG2g2k5hctHQ2fGzXazqUcd34LxBj7UeHsEC32eZSaOnR3A3EUOuY-pXwAPyQVfvj_qbPaX6lMs0W3FwpqPY4FsiC1V9tK2ytFZwAC_m1GDfGYtOUUiPDuUfJXM9f8jvu9_oej9bi4DHr7b4UGt7NsxpEF6L4enMn3jM4VZ1ZQzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مشاهد جديدة من الاشتباكات التي حصلت في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91792" target="_blank">📅 19:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91791">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ec925cde.mp4?token=aZTeCDZ76tMajPTXelo2_Uvg7t5XEx_sOsnsCEK5MelqnHmaachy9AjaLCcUVaRy7iRwSeSeNegjMwklTvAO21vNgY9T4gwdkhtJQ1N1MwmHuDzuHS3ZTDDOgbYdr1ARUMmlYpwxEq2s6BK2RaiXWfDtrk1Ij1Kc8yn4ybYUTe2zYanHkVCKWYDqGPYkKQ8KHUujOTzgmXLCXakvvyJm8TM9ksP7lCpfpKBBoX8SpePOyYZzSlQXULBg-qnMsY7F3x9rg5sDp1DVB6UufJHnFR8ohLb4QNM2gv1MSEqxxUqzmH0yfvFtzDI0nRWmyS2-pSAl-JxbZMmCv8pG-D17bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ec925cde.mp4?token=aZTeCDZ76tMajPTXelo2_Uvg7t5XEx_sOsnsCEK5MelqnHmaachy9AjaLCcUVaRy7iRwSeSeNegjMwklTvAO21vNgY9T4gwdkhtJQ1N1MwmHuDzuHS3ZTDDOgbYdr1ARUMmlYpwxEq2s6BK2RaiXWfDtrk1Ij1Kc8yn4ybYUTe2zYanHkVCKWYDqGPYkKQ8KHUujOTzgmXLCXakvvyJm8TM9ksP7lCpfpKBBoX8SpePOyYZzSlQXULBg-qnMsY7F3x9rg5sDp1DVB6UufJHnFR8ohLb4QNM2gv1MSEqxxUqzmH0yfvFtzDI0nRWmyS2-pSAl-JxbZMmCv8pG-D17bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد تصريحات مسرور برزاني الاخيرة والاشتباكات التي حصلت بعد التصريحات بساعات.. استمرار وصول التعزيزات العسكرية إلى محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91791" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91790">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29138c0f8.mp4?token=vq3l_RVOYN1UTdhimINCS1Bt7pPRW3EFapgiuXFzCGMJT_4nP6L8DDPiG-VGO8iGetkrSe55wP2Ncja-1te6Uu7DVxPRtSaV6hdE4bbrc6wADLsWy0IgzwBIcC81Rqq3kLJvcpT_zE28Ymxk8Hsd8B5opKRqAYdOpySIYy4xR_OpgWJsxQ1y0jvd0oa42QqDL2Wx-ZW8oCFChfNr_u0ObMkwGk6z3szi2tkFSuApVdHbLQ6rt8OC9W81i3N3JXweFgnXyGWLyQNaGYhpPC4EDF5PC22XtA4Jee4ljNYJRwIX4-jCzRUMzfoi1Z-fNQHYXCa9VcjcjwEVfr3QLtIHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29138c0f8.mp4?token=vq3l_RVOYN1UTdhimINCS1Bt7pPRW3EFapgiuXFzCGMJT_4nP6L8DDPiG-VGO8iGetkrSe55wP2Ncja-1te6Uu7DVxPRtSaV6hdE4bbrc6wADLsWy0IgzwBIcC81Rqq3kLJvcpT_zE28Ymxk8Hsd8B5opKRqAYdOpySIYy4xR_OpgWJsxQ1y0jvd0oa42QqDL2Wx-ZW8oCFChfNr_u0ObMkwGk6z3szi2tkFSuApVdHbLQ6rt8OC9W81i3N3JXweFgnXyGWLyQNaGYhpPC4EDF5PC22XtA4Jee4ljNYJRwIX4-jCzRUMzfoi1Z-fNQHYXCa9VcjcjwEVfr3QLtIHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جثث عناصر داعش بعد اشتباكات الاخيرة التي دارت مع قواتنا الامنية في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91790" target="_blank">📅 19:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MO6g8EruE8tnQKWCStRcqTOUYBiv7fFqsiBq3WvVSAR9VvnZYTwFPSExZUGrhAdFb4Xy3UGwNzVhvUYdB0WgMJqew4_YjU6u_mCZDRWzPrVGIX_z_MegkNs-sgfgxQy9ebjc0a4RjcLsbXPddCVhbhIqYnLDzGdVvD3XcgNjwnPOtDnWEZkbPbrFly0UdiVp_cInhPe8jb8yWMCpNF5vkXSK3TYQCuTcdqnJoydIdNdNKZb23o2m-2ZZmjQ2PMFpYBHbhQDQa7DQ4Cj8koOnokCvU4rLoG0qaohjgYCb5lvKy7nsPwmVGc4HTB-X1YizMWvQvERuhbuB6x44WETu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfIZsIezi-pq7ITN-3G0BPKS8Bn6kylm89_jOQW-52PHwmuNOtMqhgePx-cQ5UyJlKtcZX_wUqpQIsxDmuUKcM5QJMCk6Wc5JcgdFYbjjV5TfEVO-0pl3y_kYfsQTWS2r1dgFAGCNXhjcmwNiJSCtM62zmDJ_-EstD6xi5ubbRZ4khsXoKHtOyYIYKk0n5FmVdfqoVDlaVixHqj3hZquyaPxs4KWpk6Y6sJkthgAOdXT41aJB1IVNMsL7WNnFs08J-jTZq3W3rBbsYDPOJVkDZcluUNoDYBJlcZy5LgsyutZE2Ej4jnjbXzG3rr2oKtrPLvDrORgdR6woFz3_ViBkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91788" target="_blank">📅 19:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf92de22fe.mp4?token=QHU9tuiMs12KeXVITon3QKRAMOJLaSpF6kRI7bLP6GRWqj4Ldn5LdB-gO-g0uu4nKReFLqJXWd-xgC5VR6G2cPoZ02c5jUUYrxP_yXKbatQIwWW7YdHMAugZgfzQmfBm6DF1Hx3ftgPfjvhz3u0Byh6a3EPgc2n-NHJgjGFSPWVTTdYtuibO-mTjuKLpdoHfkNrTKxHr0Vs0IMoF0G1mjbkuOH1CqydB6Clrj5fJIvIaXXHENEs1JhLyqvMVAz__HFlbWi8zpLDbjZHcwG9NI8a2cvSgBDrrlcTEqSlcgH0HhsFIe1GmVQc_99SPqzCgMs0n1PNI-YteWNSbjyBC3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf92de22fe.mp4?token=QHU9tuiMs12KeXVITon3QKRAMOJLaSpF6kRI7bLP6GRWqj4Ldn5LdB-gO-g0uu4nKReFLqJXWd-xgC5VR6G2cPoZ02c5jUUYrxP_yXKbatQIwWW7YdHMAugZgfzQmfBm6DF1Hx3ftgPfjvhz3u0Byh6a3EPgc2n-NHJgjGFSPWVTTdYtuibO-mTjuKLpdoHfkNrTKxHr0Vs0IMoF0G1mjbkuOH1CqydB6Clrj5fJIvIaXXHENEs1JhLyqvMVAz__HFlbWi8zpLDbjZHcwG9NI8a2cvSgBDrrlcTEqSlcgH0HhsFIe1GmVQc_99SPqzCgMs0n1PNI-YteWNSbjyBC3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ویدیو المنار از حضور شهید سید حسن نصرالله در حومه جنوبی بیروت ودر میان مردم لبنان.
@Naya_Press</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91787" target="_blank">📅 19:26 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/YDSQrhkW7Ac_0kBXqYp9PxGTa9OfB2IMRv6Kij84CyEVixS7m_enACKgSjt25z2umVtcl3G5mJzfN-vStlxTuqmazY1iVSTf3kP7SSvgoH5YKoTKjQWsglWaOrObnBB8u7HG9lOsQQoWLf-sPSeEAfuNKEPucfo6dAwi52kFBVQoTmBVUUy-jkr9RzsjJefA55Y57A79OhTXCJfjWPyW8d-UBN0XF6ZNQKN-Ykh8SlAvkfDr9ATrqU8iqCWth8xzTEPShk7J2ABQg9ugxeVafgPX73_VgQ-yD3QbaZ1Lg2bKC8vOlcmhRnDmOWAhvhxf-Le27gZfn91wnX2KMGAc8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-93421">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
‏رئيس إقليم كردستان العراق:
أبلغت حكومة إقليم كردستان أحزاب المعارضة للجمهورية الإسلامية الإيرانية أنها لن تسمح بأي هجمات مسلحة ضد إيران.</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/naya_foriraq/93421" target="_blank">📅 20:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93420">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
🇸🇦
السفارة الأميركية في الرياض: توقيف أميركيين في السعودية بسبب "التقاط صور لأحداث وقعت مؤخراً" شملت تعرض مطار الرياض لهجمات.</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/naya_foriraq/93420" target="_blank">📅 20:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93419">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
🇸🇦
السفارة الأميركية في الرياض:
توقيف أميركيين في السعودية بسبب "التقاط صور لأحداث وقعت مؤخراً" شملت تعرض مطار الرياض لهجمات.</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/naya_foriraq/93419" target="_blank">📅 20:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93418">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 119 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية في العاصمة صنعاء ومحافظات الجوف وتعز وصعدة ومأرب ولحج والبيضاء وإب من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وجيزان وخلفت شهداء وجرحى من المدنيين بينهم نساء وأطفال.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 2177 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/naya_foriraq/93418" target="_blank">📅 20:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93417">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
🇾🇪
عضو المكتب السياسي لـ"أنصار الله"البخيتي:
إذا تورطت أميركا في العدوان على اليمن ردنا سيستهدف مصالحها في المنطقة وأينما طالتها أيدينا.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/naya_foriraq/93417" target="_blank">📅 20:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93416">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇸🇦
🇾🇪
‏
مفتي السعودية:
‏نسأل الله تعالى أن يقطع دابر هؤلاء المجرمين، وأن يحفظ بلادنا وبلاد المسلمين.</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/naya_foriraq/93416" target="_blank">📅 20:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93415">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇬🇧
🇸🇦
‏
رئيس وزراء بريطانيا:
نؤكد إرسال أنظمة دفاع جوي وطائرة "فوياجر" للسعودية.</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/naya_foriraq/93415" target="_blank">📅 19:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93414">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQrCvYdTtkBfDwAwAvO_Ehapsf3cgD5tJGo_BcTDAvJRmDU0uWhFzVjThB2r0rtYd1qR2YBlSrp7lrsfpwVUNSmY7kTAadNHYKk0Fnuk-nMeeYmlt7-wzdSmrMcyTvV4hqqg-5zsjIWLyOq5hfqL6-e79ZoYba5cH7wHrBDR7dyTHgI9tz8O5DLcNftEuyC0SecyESvqocVUDXpu27T21lqfD-CUe7crz8FrZn4IGaTCKJtxPD3J8XQbT71c4JKyt2aTV3wpBd-AstM9d5MIrXCU1UkFwyfnLuldAofRRrkid27IND4WFjAjpBXCIsri2VDXxiENz5NjqKdCFWrjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
انفجار سفينة في مضيق هرمز واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/93414" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93413">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
شركات الطيران التابعة لمجموعة لوفتهانزا الألمانية:
إلغاء جميع الرحلات إلى الرياض حتى 16 أكتوبر.</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/93413" target="_blank">📅 19:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93412">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8565a278e.mp4?token=qF3u05u7-6XzNdNUuXcbkltMruD7tT8_T0-DjjTEFL1ZuqqEMLLNWtMCTNwkITGPPCZQJ6lZiHOnjYcQI5O4FYGWjq-D_UjYQxF8JqCDg6Ku3iqA8ez1zIMm34AaKu18bJjU_K7jBXbEw3MiosGA1oM_Cx8HqBNU2iqA7Ox7UhMF78DcJMsd8q8xeNWjgo5_GKzykKsquL0Oaa-KqNAES-uaAwg8vmZnK9hMMMUCmnNylxaQJ0NiOBA1SZK_mWTnXbQwj5VSDOr3KYfZhwdRrCAoMJyM5Zb4fpHlXGZCYuxCcEG-xq04JeuHV75GJ-LzEVIUPdIJIJolJlod46OtNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8565a278e.mp4?token=qF3u05u7-6XzNdNUuXcbkltMruD7tT8_T0-DjjTEFL1ZuqqEMLLNWtMCTNwkITGPPCZQJ6lZiHOnjYcQI5O4FYGWjq-D_UjYQxF8JqCDg6Ku3iqA8ez1zIMm34AaKu18bJjU_K7jBXbEw3MiosGA1oM_Cx8HqBNU2iqA7Ox7UhMF78DcJMsd8q8xeNWjgo5_GKzykKsquL0Oaa-KqNAES-uaAwg8vmZnK9hMMMUCmnNylxaQJ0NiOBA1SZK_mWTnXbQwj5VSDOr3KYfZhwdRrCAoMJyM5Zb4fpHlXGZCYuxCcEG-xq04JeuHV75GJ-LzEVIUPdIJIJolJlod46OtNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
زيلينسكي
: إذا كان ترامب يريد تغيير القائد في أوكرانيا، فعليه أن يعلم أن شعبنا فقط هو الذي يمكنه تغيير القائد.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/93412" target="_blank">📅 19:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93410">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇬🇧
🇮🇷
بريطانيا تستدعي السفير الايراني على خلفية محاولة الهجوم على قاعدة فيرفورد مؤكدة ان العملية كانت منسقة في إيران وبشكل مباشر من الحرس الثوري.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/93410" target="_blank">📅 18:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93409">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8qC1DUkIfmoZfj3vMp1bOqNky9ImOn75rE3mcl6yDAU0ZyPMo9XI57cFw4mnoki1hcMW5ohyQCp5FYqRh7fccvvunSayMPcRPi4LAXJmG_hUZyXuEmeZvDqANvhrMoxIBtXHMKdyJCCtXTqLJeOIYjXrJMy3moRZrkcZJWWnaF6-TkLgCeP6kIXF-XfNcEjTUOsAfjH4LSepOlE81t5OALwslaKHTLWHXdaid4FW4PVx3A_fKUeC2-37rjcJVPtR0SfQrmOfqylMu1kd7JspL9QmAJUEM_rEmtqEu8rF4WrUfNRjebx8eJwheOtY0d09upXnDmIG1mNVeSXViiKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران جيش العدو يستنفر لنقل اشلاء القتلى والجرحى</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93409" target="_blank">📅 18:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93408">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4XepYAkIHvsVFbFuWijK_9aUqIN5RFE_Gb5XJ4ENCNtfJsLFpmuS7lrSn-E4RqZ4k7ztkVRrwdubAYnVEcws42dIRWgLB9I7J7YSzhpHO0wKP3UWBT9mjVq3xLvRSSCx9gunil1PtphuJXQIdjeF7JseMXB-lIrbarmieBb8ee_kWaLffyziAPXkV6930SNNymdeOpQrR6C_DumB6bvLajiZYUoXU92eqQBzms6R3UvNNcE5TzlVor3QfO9wRb1tvPI0pnQCus55sM5cwQqbFzq_DwHxy7GsfdJhyw9A9knSxGO_GK8TPnrGlY0Ee3VgZvFwWTcVhABJbz_C1ALFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تسيطر على كامل جبل صبر وقرى الصراري وتتقدم نحو قمة جبل العروس الاستراتيجي المطل على مدينة تعز.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93408" target="_blank">📅 17:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93407">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhhif6HCCVd2l5HXHxJT-nEfu6UayOujCU404jmPWstdc9zgqZaDrr10cmhO7rrKt3kOGhE3hWgxJmw9SP5UZJ72tjAcY7lJ4Gescu9jPjaJAShNhgUcntvoarUNqSEyjgnMT3MCvE1fh2ss9iyC2ZrOa7-8XpPu3LQWM_VtkpkUEUBue1oyrKo3HIHJkPne5KXqkY-l5MsI44tSZIK8nTgdtii0kAxpY0jsmjej7x9NFNgbEqjmsDh-d8JR8KR90T6VAcoOVZ_ESUBLpiBgVhF8Z6Mm7ho-d-XPYHtQbAqrDXnrKFmgiC_bFi_6qlPxHrzRnfK388cdt6qRsXZVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تتجاوز حاجز الـ107 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/93407" target="_blank">📅 17:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93406">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خطوط دلتا الجوية الامريكية تلغي رحلاتها إلى الرياض حتى مارس 2027</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/93406" target="_blank">📅 17:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93405">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خطوط دلتا الجوية الامريكية تلغي رحلاتها إلى الرياض حتى مارس 2027</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/93405" target="_blank">📅 17:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93404">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تسيطر على كامل جبل صبر وقرى الصراري وتتقدم نحو قمة جبل العروس الاستراتيجي المطل على مدينة تعز.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/93404" target="_blank">📅 17:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93403">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
القوات البحرية لحرس الثورة الاسلامية:
صباح اليوم، تعرّضت ثالث ناقلة نفط مخالفة من فئة الناقلات العملاقة (سوبر تانكر) للإصابة في مضيق هرمز، ما أدى إلى اندلاع حريق فيها.
وكانت الناقلة قد أطفأت نظام الملاحة الخاص بها، وتجاهلت تحذيرات القوات البحرية للحرس الثوري، وحاولت، على غرار الناقلات المخالفة السابقة، مغادرة مضيق هرمز والإخلال بالنظام والأمن فيه، الأمر الذي أدى إلى استهدافها.
وتعلن القوات البحرية للحرس الثوري أن أي تعاون من جانب السفن التجارية وناقلات النفط مع الجيش الأمريكي، الذي وصفته في بيانها بـ«الإرهابي والمهرب والمعتدي والناهب»، في مضيق هرمز ومنطقة الخليج الفارسي، سيواجه برد حازم من جانبها»</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/93403" target="_blank">📅 17:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93402">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFDuepUwUX-msBACUSwTqlC6bcqz5Zrs698PYhhCMe0G0jTEZBVFnq1PslwcDAHImt9Qsp3Dff6AJYHX6PxTIfmsOmhu4R8D1nZnGC8Obj_9Ipt27huW4Yg38cTnAq8ShqmfMWpm_LT7XhdKEza7huiD70X3kFh8Qh6iOzh_tCAOGKhA8kEDOnhAuBmgSdaaIVHIwyMSxI4sUUgwfGT0kUsDqbq7ZdltoL7o9lMfLS0esyukd7Enakk0j8lfXCQwDJvSKBajdWqzKGI9KFEZ5OTM_eVL6M0ZOrglVSD3mMgLTNnAbucPzaEPzH1wk4hf1qfNlxM__1fbPEyUO7E_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناورات صاروخية ينفذها حرس الثورة في الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/93402" target="_blank">📅 17:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93400">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tw2JMfAEV7GTXJZdgKo5_JvOt6p0epLQcZy2HhIkWSW-cD5q27kApMW0_mEr-dnYdnU6UHLp87Gk8X-t6RpkdYdkFE4YDPXaofLOCpP4ZiysXvUIjrra1ChJLxkqjGOM7rUaxyH0UYqDAeocWFLfMWeW4gDuhv4iqcefvok9V3XTB5zah30xuzQuz5jS7GXORuC6shaeHcWtmaL-mQi0LFKvH_albzefEIlecCHGcXpaX9w6hX0Pqo1tKQWOLV5RpF155f3oAgZspfMODF2xza2HJUw5IISGGtxlli5HT4ic9MWjV8wfbh4st5o4SgFP965VfEHIVVQCeUosETEieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qAgbFAoBeW12VOFaN6sZ8I3y5U2y_K85l3r0gVztc7Kk0xl4ebZcWURWeRy7Fy2o9x4i1QEdEmQtLiTQ2pXCg1Wl-QeYD1Cjbu96-d8euRyp_79JJmQakqnCNYJNDLmMATbOHK8aVvxc-K66k8WWwwZhj9B5AxIoxHVatd-5-xPRp_PJpcFcAgIMsW2x4aqkph_v6nybFYpshoGVTid1Fku8bEETGxUSQWuGUHQnZgDK7k-G6A5hvM91pqlc0oCySUHIkn-YCAs4iyinS6StxJ0KlcPm5oguZJKzmJ8T2PxkBQZDz5oPpmHpvZ_CCpGEfjgWIK03tKiVUQd3mXg45g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حرس الثورة يبدأ باجراء تجارب صاروخية</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/93400" target="_blank">📅 17:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93399">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حرس الثورة يبدأ باجراء تجارب صاروخية</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/93399" target="_blank">📅 17:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93398">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020de12a7b.mp4?token=Kok64z2gzyNzT4z_uETiuH1g2jZ8fRPjbhYampvx4S-q-rVDDDlqP1I-KisMNmihjzeb83wHK7pDo7-SRgw8oPQmOlduECxlTvGIGZj02-9fbF8e4ocOZ1LsS8OjziD3sgFjr2h5jmjvdPWGnEAqLOt0ibRTkh6hSuOIReYp48bZwaSCCnXG-T4aJYQE2b31rcMsEjSxvA6kbO5No-O8YpiAmb7XBUja-08YmLUb0j44P8qKqu6eB6BKPyw_q4TXuzBwjWzJym7CqdNwpP5UulViypWN0tA0GhcrCh6HtI3kmdi9cl-xHT5KBtAUWO3mD2IKx_BW3i_iQhnYSDYxhgvaSWg8s8JeJAu3I10oY4C9niH_1d5d00Q62J8KD0xF44N1EQz3CwRpsT8UUHh8MU78SY83zF5OwR3X3C9i6zEo9M_pHmG2FvjPdOIV63O-jzRuGEN_PA7xSKCy9Zm1ZhRKfsf40pgA0gmcUC5z_H0vkKEQneoM7y8jEPF51Sde-9meoCE2uIuYGQApULex3zzJyTPXiSmCUblMyTeZvLoc-sBm7Wf5qKj31f4MpmuTlGYi80z10WQAj4x4LqJ7HZOyYT8CJ8-YDu7lWtTMAEDGwBzkA5CzqdcPLczQ0XaG2U7QpVm2YZkbHavSy0hwAH7iKdYivR5sbnCaGB58nCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020de12a7b.mp4?token=Kok64z2gzyNzT4z_uETiuH1g2jZ8fRPjbhYampvx4S-q-rVDDDlqP1I-KisMNmihjzeb83wHK7pDo7-SRgw8oPQmOlduECxlTvGIGZj02-9fbF8e4ocOZ1LsS8OjziD3sgFjr2h5jmjvdPWGnEAqLOt0ibRTkh6hSuOIReYp48bZwaSCCnXG-T4aJYQE2b31rcMsEjSxvA6kbO5No-O8YpiAmb7XBUja-08YmLUb0j44P8qKqu6eB6BKPyw_q4TXuzBwjWzJym7CqdNwpP5UulViypWN0tA0GhcrCh6HtI3kmdi9cl-xHT5KBtAUWO3mD2IKx_BW3i_iQhnYSDYxhgvaSWg8s8JeJAu3I10oY4C9niH_1d5d00Q62J8KD0xF44N1EQz3CwRpsT8UUHh8MU78SY83zF5OwR3X3C9i6zEo9M_pHmG2FvjPdOIV63O-jzRuGEN_PA7xSKCy9Zm1ZhRKfsf40pgA0gmcUC5z_H0vkKEQneoM7y8jEPF51Sde-9meoCE2uIuYGQApULex3zzJyTPXiSmCUblMyTeZvLoc-sBm7Wf5qKj31f4MpmuTlGYi80z10WQAj4x4LqJ7HZOyYT8CJ8-YDu7lWtTMAEDGwBzkA5CzqdcPLczQ0XaG2U7QpVm2YZkbHavSy0hwAH7iKdYivR5sbnCaGB58nCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جيش العدو: نحن بصدد التحقيق في الحادث. كان هناك انفجار ناتج عن سقوط قذيفة، ونحن نحاول فهم ما تسبب في ذلك - لا نعرف ما إذا كانت القذيفة قديمة أم حديثة. تم نقل جميع المصابين من موقع الحادث إلى المستشفيات</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/93398" target="_blank">📅 17:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93397">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اعلام العدو: أحد الطلاب عثر على الجسم المتفجر، وتجمهر طلاب آخرون حوله، ثم وقع الانفجار.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/93397" target="_blank">📅 16:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93396">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اعلام العدو: أحد الطلاب وضع الجسم المتفجر من مخلفات الحرب داخل حقيبته وانفجر</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/93396" target="_blank">📅 16:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93395">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اعلام العدو: تشير التحقيقات الأولية التي أجرتها جهات الأمن في الموقع إلى أن أحد الطلاب أدخل قطعة سلاح إلى حقيبته، والتي انفجرت لاحقًا عندما كان الطلاب متواجدين بالقرب من الطريق.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/93395" target="_blank">📅 16:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93394">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اعلام العدو: تشير التحقيقات الأولية التي أجرتها جهات الأمن في الموقع إلى أن أحد الطلاب أدخل قطعة سلاح إلى حقيبته، والتي انفجرت لاحقًا عندما كان الطلاب متواجدين بالقرب من الطريق.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/93394" target="_blank">📅 16:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93393">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الاعلان عن مصرع صهيوني ثاني</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/93393" target="_blank">📅 16:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93392">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اعلام العدو: لحظة ايقاف نتن ياهو البث المباشر بسبب الكارثة التي وقعت في الشمال.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/93392" target="_blank">📅 16:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93391">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4f25f760.mp4?token=HgImRWWJdJwWMeKjnpo-d3ccIlbQHLW70lyWP-CkVAhtVY6fbcfJizc3FKPxaEYSMxYJDN40WHQuZBFvNpkbon6Jf7CaOVIP91rFIpEHcgyzbBN-5ZQgq7_OY_4YDNOxQSd_3JnzKeCOQd_hvgeg8A1-ACVHz0eMyyvGeEvoodhj_QhhX_6g0M54tYwkuBlONlQDHuqy09GOSy8jw4FBARvr9a-Y4KlrvSHM2nRUk6fNq9SFpqj5d8fhMOEPiVMRzubj-Xr-DLovd_H0npFXpRZOBr_J_nphY742jAC4Xngnuilv-0byHa4cDnniAZ6YXWHoDeHdwWQ9G0mkuFBBAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4f25f760.mp4?token=HgImRWWJdJwWMeKjnpo-d3ccIlbQHLW70lyWP-CkVAhtVY6fbcfJizc3FKPxaEYSMxYJDN40WHQuZBFvNpkbon6Jf7CaOVIP91rFIpEHcgyzbBN-5ZQgq7_OY_4YDNOxQSd_3JnzKeCOQd_hvgeg8A1-ACVHz0eMyyvGeEvoodhj_QhhX_6g0M54tYwkuBlONlQDHuqy09GOSy8jw4FBARvr9a-Y4KlrvSHM2nRUk6fNq9SFpqj5d8fhMOEPiVMRzubj-Xr-DLovd_H0npFXpRZOBr_J_nphY742jAC4Xngnuilv-0byHa4cDnniAZ6YXWHoDeHdwWQ9G0mkuFBBAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضلت بس جنطهم</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/93391" target="_blank">📅 16:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93390">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد ضرب تحشيدات العدو السعودي وتدمير وإحراق آلياته في جبهة الفليحة جنوب محافظة مأرب</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/93390" target="_blank">📅 16:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93389">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اعلام العدو: الجيش الإسرائيلي يفحص احتمال أن يكون الانفجار ناجمًا عن صاروخ لحزب الله أُطلق خلال الحرب ولم يُكتشف حتى اليوم.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/93389" target="_blank">📅 16:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93388">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇸🇦
السعودية تعلن عن خط ساخن لتقديم استشارات نفسية للمواطنين بسبب الاحداث الجارية.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/93388" target="_blank">📅 16:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93387">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بلدية القدس تفتح ملاجئ في حي رومما.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/93387" target="_blank">📅 16:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93386">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بلدية القدس تفتح ملاجئ في حي رومما.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/93386" target="_blank">📅 16:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93385">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz0woaFUAJ6vw7kbyD8QT4Y41h0a05PqrUptgk7eCEmzx1-c6K9xMnjdoN78i9ZosB8PeExQ0tu7ZDtr1xl6e4fdVJoRfcUbUZcirXgzju1id2EWYQfDltCxEmdXKO0redlhU_6vQb-sCiBE3g_Rmlg3TxtkIBGTLDjxVm5OAKJ2fmZnX3pVmpzEAkPL2EN-tQX8KJ6PmhT77WSq4fUMqwrWv1RA7Cgjhl6TjfHKeZRhJh4d-W8VuDPEykoKrM6QVJkYxDH_fPrA33DfupFQ3G7NDet6gnWgVMi1_wI2E-QMgdudpOkn_exJXZSdIYCYmskZqlGHfMSNEgRU8cthUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام العدو يعلن عن مصرع أحد المصابين في الانفجار الذي وقع في سلسلة جبال راميم.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/93385" target="_blank">📅 16:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93384">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الاسعاف الصهيوني يستنفرا جوا وبرا لاجلاء القتلى واعداد كبيرة من الجرحى</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/93384" target="_blank">📅 16:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93383">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdfMYBMNME3Q67iv01q4G8M6Hb4dQ4jRo_a1f2FjCwp5iDo53978XIioGQ8QgCnzgC1MXakCknVIYgGlqEasPghm9D3IYVbF3imidn23ztXQVQfwPWKPdVmY8l_O3pndQdfprlMgHrbyd7Yk-hrlxeOdvhBCFFKa4j8M-u8kpPntir-Bw_y-88xZ7DBeT4EbjoTyNj2IUw_8WBe8piecEeuIHU9jY2R0O-V9J6Rp66aEw-8hW080J7_S8djkXniXctG2LJKGAxth-4pL6YfhNDmmuQeTLzXUn-3Gh8BWiWgIWvh8YD7MeDHIAcaqOYJ_dY7lVPXnX2fg-r5b-OXH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالة من الذعر في صفوف جيش العدو الصهيوني بموقع الحدث</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/93383" target="_blank">📅 16:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93382">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d9c431a9.mp4?token=cYA7BtAhDQ1pRhEpi-XbSIbSKo0W7D_6lOfkhPOpHcvJ2ttpA95YsVIiFG6SQnGA6l6AB__HsY9RW4jmxEK0vPnUb0bfmx6gE0Uams-0KGblsJ_HepwyCzBosTz1vfhK5C8Nx_cyy9a4aSasqXJpLbBF3kTEgWjxInwCOBlVxGs-FxEYdsUHyYfrNJEzve3HyTSxJGOPe_AvljfeBn4Rk8Yp2hkkfevUuEuYNyg6uZopnkoPB4D3BXK6KkDUw8QU-QTUnxYEQOTlUN3nXgoq1KR2pk3z0i7O9Ss3_PsFEFK7MqkBaJXcSMrhXPLit1dttfHIYAyJK-Yph3Pol1crjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d9c431a9.mp4?token=cYA7BtAhDQ1pRhEpi-XbSIbSKo0W7D_6lOfkhPOpHcvJ2ttpA95YsVIiFG6SQnGA6l6AB__HsY9RW4jmxEK0vPnUb0bfmx6gE0Uams-0KGblsJ_HepwyCzBosTz1vfhK5C8Nx_cyy9a4aSasqXJpLbBF3kTEgWjxInwCOBlVxGs-FxEYdsUHyYfrNJEzve3HyTSxJGOPe_AvljfeBn4Rk8Yp2hkkfevUuEuYNyg6uZopnkoPB4D3BXK6KkDUw8QU-QTUnxYEQOTlUN3nXgoq1KR2pk3z0i7O9Ss3_PsFEFK7MqkBaJXcSMrhXPLit1dttfHIYAyJK-Yph3Pol1crjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالة من الذعر في صفوف جيش العدو الصهيوني بموقع الحدث</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/93382" target="_blank">📅 16:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93380">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5Z3mxtn0218rqHzxOy_xSXB18nevOPmQtp7w_aS0Yeaivnb0naw_jwSBZsdWGUeemtI_sr7JpNrzV7gmzao7g6vgpz-0tgfO7Gh7uDNasLesRr_Pl2YKWOlDE3FUaJucXB_8SwYJI9sRuGtiHOI5VgFjBSHm-0qUi3D-3dF--p1v7F5_XMFbcC69i87PL3Hihj8FP47Gf9ACWZJUMuG2qqwBktQ2P0QggM9GuvjO_NZvXhSepL_Gq7pTZHTes-kXSeR-qWEQbKiBz-aL_MmdxlwFEg_5ktQmcca6XkMx3gdaY7e9pCeqFy6c0j9mlpS6K1OWw94Z5MLByTOWdDHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXSuYrvoNxt0bk6ej0eO0dKqNWjKZfTHtfKTVhqY0Xp2dK0zcWClrSAquNfdFoHtL7G74i5qd6oRnwahv02srPoFW4QtVUu_UkaYpFDecRQ-oTZUL7LKU2R7s0KCQkWCShbt2XTYEt_m321J3ZeTmErdyVODZvxCdKZ-Eztx3k1LYbIf8EYUMY0zq3S2Jy9YOyZxlY_S5Ym5sta07Dw4pjK5V697VYvi3wxWGAdxTVHyvS7DqOdff4ZwPOglWx-qY4YsBjKBIiEzzDzxiU11YRiRohlbl9GmQOhAsaMS40GXfkXiSpKmbczHyB31cT3V-OpLMFHyYdZQpvj3EdQuIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طيران جيش العدو يتجه لموقع الحدث</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/93380" target="_blank">📅 16:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93379">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90fc74ebc8.mp4?token=onlpmMEDkzB-uzgSZaknu8n47_T2qaoRRgdUYCNTHj-1ScEP-vkYiRH9OoBCGDzGlAl7SA1xK4bIK0N632HTvKrJ38dPSWmHm10J9kouAFO7yFTJS9dYDTfhV7bvJrGI50w1p-70T7Sb86V492RpWUERijZCbmtWKQF9RCPSLdvS0rZitc_5cIWH5rS4G74xDMc1FXmJytJ2vHSElUw55B9NTm089wQIvSQ1ljlpxVIAltM79drgFDe-mG3JNK-bt8CGePV0Bi9mi2deu8-upVVVA3v4JCdyuoOtrCnuGx5-Sij9pQRjSOhaAdkSGGoh5J2rKjaDLh9g75iNf-pRIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90fc74ebc8.mp4?token=onlpmMEDkzB-uzgSZaknu8n47_T2qaoRRgdUYCNTHj-1ScEP-vkYiRH9OoBCGDzGlAl7SA1xK4bIK0N632HTvKrJ38dPSWmHm10J9kouAFO7yFTJS9dYDTfhV7bvJrGI50w1p-70T7Sb86V492RpWUERijZCbmtWKQF9RCPSLdvS0rZitc_5cIWH5rS4G74xDMc1FXmJytJ2vHSElUw55B9NTm089wQIvSQ1ljlpxVIAltM79drgFDe-mG3JNK-bt8CGePV0Bi9mi2deu8-upVVVA3v4JCdyuoOtrCnuGx5-Sij9pQRjSOhaAdkSGGoh5J2rKjaDLh9g75iNf-pRIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاسعاف الصهيوني يستنفر</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/93379" target="_blank">📅 16:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93378">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6073e9d6.mp4?token=XKKISMWZEGlkGavxe_OzZKG3iejCNVZioaFVIMHHudVo7AkNBtUAWoU0i3Pq_uA2iIJUV18DQZtGYN60bZXlaZbBw3ZctnKBwPkjt5W_rDJelHBmqk8jCx-jCQ9rtonnfAGTe3Izig5jSW5hL9dimZuRpInMr3S92DDnA2zI7lk0mnJyyeEwbWavjWhVxnKYHPLIgdUxihaQsIMyaAhCEiKQjXdCpkId--93fM21oaBNrJAGkMYGaMe836UqCbaZeXYw4DK2HWB9jA9oxL5Vbd1RgsIVo9EVtnHBf_O-BOQ_TqcBmafHQHHFRXKyLxaN2zAp-lrHcVblWzCzgxGp1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6073e9d6.mp4?token=XKKISMWZEGlkGavxe_OzZKG3iejCNVZioaFVIMHHudVo7AkNBtUAWoU0i3Pq_uA2iIJUV18DQZtGYN60bZXlaZbBw3ZctnKBwPkjt5W_rDJelHBmqk8jCx-jCQ9rtonnfAGTe3Izig5jSW5hL9dimZuRpInMr3S92DDnA2zI7lk0mnJyyeEwbWavjWhVxnKYHPLIgdUxihaQsIMyaAhCEiKQjXdCpkId--93fM21oaBNrJAGkMYGaMe836UqCbaZeXYw4DK2HWB9jA9oxL5Vbd1RgsIVo9EVtnHBf_O-BOQ_TqcBmafHQHHFRXKyLxaN2zAp-lrHcVblWzCzgxGp1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاسعاف الصهيوني يواصل الاتجاه لموقع الانفجار لنقل القتلى والجرحى</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/93378" target="_blank">📅 16:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93377">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7431866df.mp4?token=R4NFyjbURqFV3e5Si7ZgEQOsmAB-xcBy-RW3dL5EfLTS_Kki_eXQh5EcNDpD4AaRenkeEcYi2H8L89iLR8aOfOxhmND0qQw_Stoez48jYOtYEoTWG0DOHI-RwyclSo7SUwX3u6UHAVz5s4IC-ha-ICMfAqhpeJed7vftWy629FiTJGZoARXs1TejmS8PEVTW6HlwzbPBDU9LvHT6XZDhLTr5LU95rEEnW_hgZWCMT_OOoKZucmC6pOh905eBRQgt5Iu7nJxVVtxamOWF9qQ0YFhUoWG9-KfxgNd17euLRCegGRUtkvi6Zlx-C_0Fxs-nNEdLIxdwR5JV-SxiAzbV-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7431866df.mp4?token=R4NFyjbURqFV3e5Si7ZgEQOsmAB-xcBy-RW3dL5EfLTS_Kki_eXQh5EcNDpD4AaRenkeEcYi2H8L89iLR8aOfOxhmND0qQw_Stoez48jYOtYEoTWG0DOHI-RwyclSo7SUwX3u6UHAVz5s4IC-ha-ICMfAqhpeJed7vftWy629FiTJGZoARXs1TejmS8PEVTW6HlwzbPBDU9LvHT6XZDhLTr5LU95rEEnW_hgZWCMT_OOoKZucmC6pOh905eBRQgt5Iu7nJxVVtxamOWF9qQ0YFhUoWG9-KfxgNd17euLRCegGRUtkvi6Zlx-C_0Fxs-nNEdLIxdwR5JV-SxiAzbV-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاسعاف الصهيوني يهرع لنقل القتلى والجرحى ومستشفى صفد يعلن حالة الطوارئ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/93377" target="_blank">📅 16:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93376">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHRauXxV4d_pmL2zqrrg_B_4I2u6r5Kr0r5RNF7ZqETkd7w8YlH3CHJN4eAjMAIymfJHBojwxVB1mm6JCUi5XxAeHOL-zFAtV0C5wsPhfH1vpkHqibBVRUDVi4YLOeZZ0rUSJ7Z5qs1Onn0JWnA1yc7TYT1KJM0txO_Ohl1I9QHaTCFit0WkHJWi_XcDB2n6v2FpDroV6s6pzwwwDEbmbEFDEdjZZfQfH1_11UH77S_qGh8K6JbLIY4RxDXXUJMR5ziKQMmVSrsJtBuia-269IJV3Y-bGrF1GvjdPRM-PjyVYZUDeNIextFZj_6CgFkR88e8Sm03V5O_dS82ABNMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاسعاف الصهيوني يستنفر بعد الانفجار</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/93376" target="_blank">📅 16:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93375">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riWzgXFXvp3uISTHYi5NOQukx_94UgJWGPvZ4oNtKfqQEeCtqyErO-RWEEs1eZW6dZ7EGkVKo2TJDmcExLJY8pRKHJQO_AddPByIIu6nIlozeimZJCWdooFj1InMM5thk0CrxaYAVs9X7Rci24bcDzWkZA17nl8lBWfA-3ZTeU44X1UR6vIvjeDhdUB0LM62duYTEzI7PVw9tDuh32KlmBnkqNXriMRA-xugwwj0Pzsv1maNxHF0Ccm54Bb-NCzMrgV66vDJ8RwNPrIQtVG5YUFQHiGo2tJ6vE9FU25jIo7eBXp3Jgn5vMzIc9e_dxUMC9mxpclZpER18GZMEDiwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارة التعليم الصهيونية: إنها حادثة مؤلمة للغاية، وقلوبنا مع الضحايا وعائلاتهم.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/93375" target="_blank">📅 16:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93374">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">طائرات العدو تستنفر لنقل القتلى والجرحى</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/93374" target="_blank">📅 16:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93373">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f94dbc6c3.mp4?token=u5aAwAs9gvs3TI4cY67u_hr8aa3qJO1Fu1JuASYlULEeFJvoC-vzDjQMcCy9cBCPKUhckIJDKMNT1_E-flw4x5ba9-cpiNt6FCZsa1jOvFRtAwM_7NV_lmwcEfB7wL3cdM_qbM7iyh2KYlBDb1q0NSQMWXhXUjaJMKwb_PsZCdLJJ4Znxjd2njr1Khwz4wQAYPoIi2c5cStHgdlvi0miG7MRCPs6KFJ7xn94L1E1p-yABLmVwIBaMhAvuIfRY5gYXTAPkDUZ4xroz06Uhozm5PS-kydb02kIVKk9A7dtFcHx_Af6WRrUxYOFn1qOpCEzsYPOcLufV8nhIV-1-EhmXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f94dbc6c3.mp4?token=u5aAwAs9gvs3TI4cY67u_hr8aa3qJO1Fu1JuASYlULEeFJvoC-vzDjQMcCy9cBCPKUhckIJDKMNT1_E-flw4x5ba9-cpiNt6FCZsa1jOvFRtAwM_7NV_lmwcEfB7wL3cdM_qbM7iyh2KYlBDb1q0NSQMWXhXUjaJMKwb_PsZCdLJJ4Znxjd2njr1Khwz4wQAYPoIi2c5cStHgdlvi0miG7MRCPs6KFJ7xn94L1E1p-yABLmVwIBaMhAvuIfRY5gYXTAPkDUZ4xroz06Uhozm5PS-kydb02kIVKk9A7dtFcHx_Af6WRrUxYOFn1qOpCEzsYPOcLufV8nhIV-1-EhmXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو يلغي نشاطاته المقرره الليلة بسبب الحدث في الشمال</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/93373" target="_blank">📅 16:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93372">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اعلام العدو: التحقيقات الأولية ترجح أن الانفجار القاتل في "راس راميم" ناتج عن دوس مجموعة من الطلاب والمعلمين خلال رحلة مدرسية على "مخلفات حرب أو قذيفة غير منفجرة" انفجرت بهم مباشرة.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/93372" target="_blank">📅 15:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93371">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الجيش الصهيوني يغلق منطقة الحدود التي حدث فيها الإنفجار.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/93371" target="_blank">📅 15:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93370">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ارتفاع الاصابات إلى نحو 20 مصاب</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/93370" target="_blank">📅 15:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93369">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اعلام العدو يؤكد: هناك قتلى.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/93369" target="_blank">📅 15:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93368">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اعلام العدو: الانفجار في سلسلة جبال راميم استهدف جولة لطلاب ومعلمين.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/93368" target="_blank">📅 15:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93367">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اعلام العدو: إرسال طائرات هليكوبتر إلى المنطقة لنقل المصابين</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/93367" target="_blank">📅 15:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93366">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اعلام العدو: مجموعة من المتنزهين أصيبت نتيجة انفجار، يُشتبه في وجود قتلى.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93366" target="_blank">📅 15:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93365">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الإسعاف الصهيونية: هناك 12 مصابًا في منطقة راميم منهم 2 في حالة خطيرة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93365" target="_blank">📅 15:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجار في منطقة راميم</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93364" target="_blank">📅 15:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93363">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حدث امني في منطقة "راميم" بالكيان</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93363" target="_blank">📅 15:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93362">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حدث امني في منطقة "راميم" بالكيان</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93362" target="_blank">📅 15:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93361">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crBElPAdoiyCfHsAaQAm5sYPJXggeGDE__MIGDRE1Up0T9Kv3lfDIa6ukmQVgEG3Nu8q6yUtHXCrx6Uqs806muzfZTGa1MUlKj11vqJ0DKgo2aI3r8zBIB-Y9npYjp0O8ETZobCerMNH57HA_SuAPE5uBfMU8BdJud2sWOtR8FKfVK9plXLO2ZBc_2QyFgKRNw7B_NdIo-U88JVgvOBztyu-JFuzW35itSTfo6Z8DY1k4ATei7I8NkMP4WIBt7dtIyWGqBjAMNoN3YYyB0uBaRWDcpphjGdP0EVMuCTWLPDTy8QEVEg5vqTtAYrxCprU7yxju62oo-sKKaUxyelnqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
السعودية تعلن عن خط ساخن لتقديم استشارات نفسية للمواطنين بسبب الاحداث الجارية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93361" target="_blank">📅 15:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
حزب العمال الكردستاني يخلي 4 معسكرات تابعة له شمالي العراق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93359" target="_blank">📅 14:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇷🇺
الكرملين:
مستعدون لتعليق الضربات في يوم انتخابات أوكرانيا.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93358" target="_blank">📅 14:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93357">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77814f224b.mp4?token=HZtM4VfKpvnOUtQNTdv9c6ndY9Y87ikHnQtLtG5aN714e_Go-RrtK222XYS9Wcxkxy4vQno6Vd7GFgSvjKV1W7c9aN7q6dVe3goRfS66qex2elElCwtOKGtREYn7CCKmQOwB4db25FrzAVFkxM9EXLmeN-0CGH0tCDg6aZj84YFJSRRU8_ofkRRNhmEPmOVStbJ9_FVvmcg-0vFQwNx8vniu_25zC3HSZa7pJi2PJJ4lL32UBJZsvewMVcy6V5Zu3HXw7LjrucE9lAg4Rh65qQVrYsKQq3yGctgNT8oG51N7SNu9qZLjy8S4tuAZyNheTfYWrtYBI3cLH7TQ5UO5F1kurKE7nMs3KqDTfo7_sZH0B8ktijutHy6sPw0-roy0avPMj9XyHPl-1_yu05fbbB0ypFPHtHY6PcmnFbnKZ8pPR-v2RF6fbPMfNAD8HIJIs6OliHGGDCX9PZODHsy_DYjWPRZJURq3Er_mCpPmNPdWiEyeE7dbuPS4q1HPs4FskdHZbVeWdEpevsrGbYjwHxj18nnbXXud1EjusG_dkEUqUBTLyvc1Oc8iRUWL8X0KYfiOgTXh71nEcX1G2jvu22X-FqjRSbiaSBNiuWmLeTK6tUxUSOFpV1BwplgQrZgcq5A-hV33fRt52KIiT5yYq0c3PFqgu3EAWfkjjYMehVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77814f224b.mp4?token=HZtM4VfKpvnOUtQNTdv9c6ndY9Y87ikHnQtLtG5aN714e_Go-RrtK222XYS9Wcxkxy4vQno6Vd7GFgSvjKV1W7c9aN7q6dVe3goRfS66qex2elElCwtOKGtREYn7CCKmQOwB4db25FrzAVFkxM9EXLmeN-0CGH0tCDg6aZj84YFJSRRU8_ofkRRNhmEPmOVStbJ9_FVvmcg-0vFQwNx8vniu_25zC3HSZa7pJi2PJJ4lL32UBJZsvewMVcy6V5Zu3HXw7LjrucE9lAg4Rh65qQVrYsKQq3yGctgNT8oG51N7SNu9qZLjy8S4tuAZyNheTfYWrtYBI3cLH7TQ5UO5F1kurKE7nMs3KqDTfo7_sZH0B8ktijutHy6sPw0-roy0avPMj9XyHPl-1_yu05fbbB0ypFPHtHY6PcmnFbnKZ8pPR-v2RF6fbPMfNAD8HIJIs6OliHGGDCX9PZODHsy_DYjWPRZJURq3Er_mCpPmNPdWiEyeE7dbuPS4q1HPs4FskdHZbVeWdEpevsrGbYjwHxj18nnbXXud1EjusG_dkEUqUBTLyvc1Oc8iRUWL8X0KYfiOgTXh71nEcX1G2jvu22X-FqjRSbiaSBNiuWmLeTK6tUxUSOFpV1BwplgQrZgcq5A-hV33fRt52KIiT5yYq0c3PFqgu3EAWfkjjYMehVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تحرر قرية الصراري بالكامل بمنطقة جبل صبر جنوب مدينة تعز.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93357" target="_blank">📅 14:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93356">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ab1f5742.mp4?token=APrdnEY63UNENtz3sUeodWPnSFLMw4eL83-AVXluBDxgZ-ZQpDhsPx3jejmdTpyicoY9wPGB5mx35NBCVQdFZK0oEiWGRmEq9IRY3Tg8RiKf0mi_64yZqsYylKrtoSblyzO1C3ha9Tk9iLu_cg8N45x6zdELpIBT2rzM5JBEantyQp1PnfG4cBF9xKM4FRL_EQH7Qk8yz4MFX1JK98ihX0udah7uNNsJR0k61s1vhaOnXDw-0vhkU3ksPv0e3xgvpDXgrLzZSQ4fxPMbvwiZgNXpOJCNUxlTiBSjMaROAvkUagaKrwowjV0LlBNJpwAc48q2ch1sPrEHSNplWttyOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ab1f5742.mp4?token=APrdnEY63UNENtz3sUeodWPnSFLMw4eL83-AVXluBDxgZ-ZQpDhsPx3jejmdTpyicoY9wPGB5mx35NBCVQdFZK0oEiWGRmEq9IRY3Tg8RiKf0mi_64yZqsYylKrtoSblyzO1C3ha9Tk9iLu_cg8N45x6zdELpIBT2rzM5JBEantyQp1PnfG4cBF9xKM4FRL_EQH7Qk8yz4MFX1JK98ihX0udah7uNNsJR0k61s1vhaOnXDw-0vhkU3ksPv0e3xgvpDXgrLzZSQ4fxPMbvwiZgNXpOJCNUxlTiBSjMaROAvkUagaKrwowjV0LlBNJpwAc48q2ch1sPrEHSNplWttyOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تصاعد اعمدة الدخان من الطريق السريع في محافظة الديوانية جنوبي العراق لاسباب غير معروفة وانباء تتحدث عن انفجار صهريج نفط.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93356" target="_blank">📅 13:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93355">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsrOCz7zsedRsWRTG-U_tMho828W_JmcJEHlRWyehBrRTotDwpz6FXs6lKVMGy1K8wFFf4b_8bkZy2ZcBNSERlW1VbxEMm0Yr9810sfth90_GfxtLiDKYv8OiVIPEA9i3Xhq_Xv7jfDmQsp6zIOjsaq86yd_jH0r5J20B4MF9KuAki_qpKdDWth9dnKwm82q60jOy4XPxeTZE8LJ-TR2NACUHk1P7cWMYijPvHvFNfkJiNlFvFMvcc2BpioOyuER1ELK5DcrVDFvgqL7h1i6C4VOO5zVxxQ6vvrexCM8YWUuaRzIfxfW1_Eay4RjFYgl4cdfJEuZxkCHmMH4dOGROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المتحدثة باسم جيش العدو الإسرائيلي تنشر مقالا في موقع "إيلاف" السعودي</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93355" target="_blank">📅 13:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93354">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">زيلينسكي: بعد فترة وجيزة من منشور الرئيس ترامب على منصة "تروث سوشيال"، أطلقت روسيا هجومًا استهدف محطة توليد كهرباء في خاركيف.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93354" target="_blank">📅 13:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93353">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇸🇦
نتيجة للهجمات اليمانية.. ‏الرئيس التنفيذي لشركة أرامكو السعودية: انخفضت المخزونات التجارية البرية الآن إلى أقل بكثير من ستة مليارات برميل، وهي آخر مخزون احتياطي متاح.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93353" target="_blank">📅 13:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFsdD3rsqRxhnfWu7qXSsoHi0Q1r1QLrBgPJe1gkmZyFwzYXOJRgW6zeJLTd1H6UWG37D96hnoeLK5ggU8MmxAi1EVlZwv0PifIM-L0ZgsIJYVflQRi2Um0FBxLPgDmBBA5NEB-Eod4Qp1On5699s0VjTiAbpnVuocUTkMyJ86aszwJQHMkl8oqYSgq0hTrMiRUTCbZLOqGD5k9j9UsKGUDfFcIpeFDcjK1gbohY00XF7QDcdb32Xzdq_foUc0NEchwnYF8xKZVvCxhGRySZbKx8Cq3l62OOHoTt87D8FQtDqi81f_D2xAgIn8m_XNErWakXfZvnE_emCJ0lGFKQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتفاع اسعار  النفط لتصل الى 105للبرميل الواحد.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93352" target="_blank">📅 13:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93351">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d08bdb21.mp4?token=KEMFelI8xGlirpbBjs8hK-ERGm1LZBD2la0jrcG-pQhQ19P0fSN12c8HbIF-FMLVcSsx5d6u7XkyF3xSOqmBv7ueFcxkOHKamLOWzKWlpcUjzGav2PKi5a2f3eQqBL_lVoto3wblvwhlebfozJsYxQCi5RO5cRb4SLXTY21-Ayde1rH1DirFQED1oAZd2aYVytLnD8hjxBcsQv4NiFIsIuWI3YHZwTPqEiRGmmyiWkqrTVmf1FE-uFzmJP8ClPNX31tku1m7sBn-lJvM8QMbcbJQD_gDgsSRFhpD0TNxmciiB7I2DaKD7q-KRroiNtsUaZdLstwEpIOCk-Rl2Tf-sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d08bdb21.mp4?token=KEMFelI8xGlirpbBjs8hK-ERGm1LZBD2la0jrcG-pQhQ19P0fSN12c8HbIF-FMLVcSsx5d6u7XkyF3xSOqmBv7ueFcxkOHKamLOWzKWlpcUjzGav2PKi5a2f3eQqBL_lVoto3wblvwhlebfozJsYxQCi5RO5cRb4SLXTY21-Ayde1rH1DirFQED1oAZd2aYVytLnD8hjxBcsQv4NiFIsIuWI3YHZwTPqEiRGmmyiWkqrTVmf1FE-uFzmJP8ClPNX31tku1m7sBn-lJvM8QMbcbJQD_gDgsSRFhpD0TNxmciiB7I2DaKD7q-KRroiNtsUaZdLstwEpIOCk-Rl2Tf-sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تشعل مقرات ومواقع المعارضة الكردية الإرهابية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93351" target="_blank">📅 13:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇸🇦
نتيجة للهجمات اليمانية..
‏
الرئيس التنفيذي لشركة أرامكو السعودية:
انخفضت المخزونات التجارية البرية الآن إلى أقل بكثير من ستة مليارات برميل، وهي آخر مخزون احتياطي متاح.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93350" target="_blank">📅 13:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93349">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
🔻
وزارة النفط العراقية:
أسباب فنية وراء توقف تصدير الخام العراقي إلى الأردن.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/93349" target="_blank">📅 13:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93348">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c90ac70ca.mp4?token=sWsR3Uf1LcYlJPJWRtKeYozm8GlE4Yaq5KDs5_g896sTXfR495Q8c3mF5lOkpjM1IsAUVhrwjnyRTw6VXHdb1enI05wppd3HEnldviZbmEARCJlw1z5eSdYTEnXrClWzcxXr2a2qhbM05ekpFgrZtloaNjdCTA3W38mm6-ho7wbTKJXZR16U0LYpAUPEbsCKEzPGNn-I3X66xE9H6XCAu-wHSoOE0nRrRK5HQzDzyyqRs5n-vLNYSzu8HDYZfluv34cWTDfIm1-IYK47ovvbe_p8VQxCSjJ4IZzTlaS8BgZgsYDjpoJCx4h77_IYyf4FwQBSZZnROB82riH1FsOu8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c90ac70ca.mp4?token=sWsR3Uf1LcYlJPJWRtKeYozm8GlE4Yaq5KDs5_g896sTXfR495Q8c3mF5lOkpjM1IsAUVhrwjnyRTw6VXHdb1enI05wppd3HEnldviZbmEARCJlw1z5eSdYTEnXrClWzcxXr2a2qhbM05ekpFgrZtloaNjdCTA3W38mm6-ho7wbTKJXZR16U0LYpAUPEbsCKEzPGNn-I3X66xE9H6XCAu-wHSoOE0nRrRK5HQzDzyyqRs5n-vLNYSzu8HDYZfluv34cWTDfIm1-IYK47ovvbe_p8VQxCSjJ4IZzTlaS8BgZgsYDjpoJCx4h77_IYyf4FwQBSZZnROB82riH1FsOu8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تصاعد أعمدة الدخان من مقرات إرهابيي المعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق عقب استهدافها بعدد من الطائرات المسيرة الإنتحارية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93348" target="_blank">📅 13:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93347">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc156d9ecd.mp4?token=LKZgBsHmqo7-Woiju9sA6UuxhnygALQV8dkB0fpUcAQXk6h80ZNFsTseT77zkK6MeKmBc8LSM1PyxdJIIeifXCtzpaX8_XCU2w_EuwEhFQOf5p71kkQE9uukx9u-Aq6wk_2OW9sWp9AI2p4TK6oY7Dhw6PGpXpwmSYQkXzoDRlYb0YD-efm9K5_3EMSPR_JyJuZm8A8LgFDGaIY0cfxWVlafnFPyqnIPaTduQtHGd3G8se0tUH1H34UX5uD81zFQmZRDuzBR-f1O6Q0Cdpbd6nQ0JzVYHHghbLCSDs5izewlezxBDMhVam4PUB797pxDu50zO6vKOvQD06S1ih3-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc156d9ecd.mp4?token=LKZgBsHmqo7-Woiju9sA6UuxhnygALQV8dkB0fpUcAQXk6h80ZNFsTseT77zkK6MeKmBc8LSM1PyxdJIIeifXCtzpaX8_XCU2w_EuwEhFQOf5p71kkQE9uukx9u-Aq6wk_2OW9sWp9AI2p4TK6oY7Dhw6PGpXpwmSYQkXzoDRlYb0YD-efm9K5_3EMSPR_JyJuZm8A8LgFDGaIY0cfxWVlafnFPyqnIPaTduQtHGd3G8se0tUH1H34UX5uD81zFQmZRDuzBR-f1O6Q0Cdpbd6nQ0JzVYHHghbLCSDs5izewlezxBDMhVam4PUB797pxDu50zO6vKOvQD06S1ih3-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات جديدة تهز مقرات المعارضة الكردية الإرهابية في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93347" target="_blank">📅 12:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93346">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇸🇦
السعودية تزعم أنها رصدت هجوم مركب جديد بالصواريخ والمسيرات الإنقضاضية في طريقه نحو مواقع في العمق السعودي.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/93346" target="_blank">📅 12:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93345">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مسيرات انتحارية إضافية تحلق نحو مقرات الأكراد الإنفصاليين في محافظة أربيل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/93345" target="_blank">📅 12:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93344">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7be00c77.mp4?token=PhrTHKJrkiBHUjMQLPFEZ0DVPPf3xyL3X1K4D2TQwha4R1oihJzCuausYlLzK1jNpdclRsxa3z3Uk2HSkK-RJpTr3jQp0c_MYTRgh_Uj-Hllik2T1IBOEKcb1-HAgCu_5hqhKN-aYXPr0cEgPXRgqZxChMzHJ_dcXURu5UjgPHTvJZcCtk97bxRS1XQYMaWAN2AcanCbuthfIAS14C5G7HoPrbRQzuSZLCU4EKVJ3ywuTedzEyLiiZ0Kf0EBbmyxTzWtsM9wMjL2HCVTbe8DT4N5m2lc3SHPoGsnlkqdM3qiAYtn59eTa9QnU7BWgIAH3CTrzHj2LJHDzs1Ep79AUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7be00c77.mp4?token=PhrTHKJrkiBHUjMQLPFEZ0DVPPf3xyL3X1K4D2TQwha4R1oihJzCuausYlLzK1jNpdclRsxa3z3Uk2HSkK-RJpTr3jQp0c_MYTRgh_Uj-Hllik2T1IBOEKcb1-HAgCu_5hqhKN-aYXPr0cEgPXRgqZxChMzHJ_dcXURu5UjgPHTvJZcCtk97bxRS1XQYMaWAN2AcanCbuthfIAS14C5G7HoPrbRQzuSZLCU4EKVJ3ywuTedzEyLiiZ0Kf0EBbmyxTzWtsM9wMjL2HCVTbe8DT4N5m2lc3SHPoGsnlkqdM3qiAYtn59eTa9QnU7BWgIAH3CTrzHj2LJHDzs1Ep79AUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات مسيرات انتحارية تهاجم معاقل الانفصاليين في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93344" target="_blank">📅 12:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93343">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوي انفجار في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/93343" target="_blank">📅 12:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93342">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇷🇺
🇺🇦
وزارة الدفاع الروسي تنشر مشاهد من إستهداف مواقع القوات الأوكرانية وتحرير منطقة نيكولسكي في مقاطعة زابوروجيا.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/93342" target="_blank">📅 12:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93341">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLsXQaWIppMVV_Rezf16ldI6y2z_APLo4HP7Y8mQUykFz8aMfi26_BLf6mTfHG-urydR5KIj86GnNZEY_yiUOWI7H0OzsXQnPDLdiJJ_y5IuZDeE3ENcT0FacdnIznWUV_z8ZHGj0CNbOF_0IeEYL-woWJKFNaF_OhMbCMKtmgQBe-7j0JCJXsF_UX_hXsn3BXwby7FcDEbDvgrbWZpdGsso4rv-ViG6pD4VSroOSMVlfAq5OqcFp0leYB1AzcWhTkJX0OsET5qFJSDVNf2r9rlYVpf6UOaoi-BrPRbRzrBZomz0NYvAFa5AlY0wGQxyUekF8RTWKAqNQMG5jMcihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوي انفجار في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93341" target="_blank">📅 12:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93340">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇸🇦
رويترز:
تم إزالة أسماء الرئيس التنفيذيين لشركات إكسون موبيل، وتوتال إنرجيز، وشل، وشيفрон، و بي بي من جدول أعمال مؤتمر الطاقة العالمي (WPC) الذي عقد في الرياض، وذلك في أعقاب الهجمات القاتلة التي نفذها الحوثيون على العاصمة السعودية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93340" target="_blank">📅 12:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93339">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زيلينسكي: بعد فترة وجيزة من منشور الرئيس ترامب على منصة "تروث سوشيال"، أطلقت روسيا هجومًا استهدف محطة توليد كهرباء في خاركيف.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93339" target="_blank">📅 12:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93338">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇸🇦
بعد الدك اليماني وإغلاق مضيق هرمز.. وزير الطاقة السعودية: لا يمكن أن يكون هناك مستقبل طاقة للجميع دون توافر أمن الطاقة وأمن لنقل الطاقة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93338" target="_blank">📅 11:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93337">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي يطال مناطق سكنية في محافظة الجوف اليمنية؛ إرتقاء عدد من المدنيين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93337" target="_blank">📅 11:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93336">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4f5f9886.mp4?token=Yws0KFHIngesblYyuvLEyXP4DDAHJxwI5Ng4SkBlSb_p4wUA5xM0gUbMyk7sIke8jSlyQ3XymppPPq5EOYYzW_peg5A9FqcMf_Q3dyyfwoortkqTp2j3go58mpYDdskvLOe73uCqiQa3x6NKrq5w3DkRsm-GbKZw2sWQesnPCNsOxG0ee5MxS4Js8gRIhyYynyxl8WP45aShdJBjwpQo6_Jn6kXTGxwkHBIO0npCjztGoRD2CfJPfoTZw9i-rqAr6mD_dA8kKaxkaOgL6kD9ZF_ZMjlzMp-wGCCRbcbUTMTsE3FqnuPdgVWh8HgvrZ7PPv1mF85djS043mvSwC-qzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4f5f9886.mp4?token=Yws0KFHIngesblYyuvLEyXP4DDAHJxwI5Ng4SkBlSb_p4wUA5xM0gUbMyk7sIke8jSlyQ3XymppPPq5EOYYzW_peg5A9FqcMf_Q3dyyfwoortkqTp2j3go58mpYDdskvLOe73uCqiQa3x6NKrq5w3DkRsm-GbKZw2sWQesnPCNsOxG0ee5MxS4Js8gRIhyYynyxl8WP45aShdJBjwpQo6_Jn6kXTGxwkHBIO0npCjztGoRD2CfJPfoTZw9i-rqAr6mD_dA8kKaxkaOgL6kD9ZF_ZMjlzMp-wGCCRbcbUTMTsE3FqnuPdgVWh8HgvrZ7PPv1mF85djS043mvSwC-qzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زيلينسكي: بعد فترة وجيزة من منشور الرئيس ترامب على منصة "تروث سوشيال"، أطلقت روسيا هجومًا استهدف محطة توليد كهرباء في خاركيف.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93336" target="_blank">📅 11:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93335">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c82e4489c1.mp4?token=KcFU9srlv3wm9hOPO6EBtAS5xmtah-1FpZzrTTnmZbL-7j9t6MXuJ7SmDNjFSVRkdFi_siamfatB3bFghqgAca7yUy6VpCPkj_gSAomx76rDNUGXEp7yi_JfQ_crgfp4BW6rRdg5dgMRjfd6mJ6rOSttZDnZvwf5_nXpaUhaeTNdN0JrEr2ETgbzLUGvO4-iAAK2Yd2M3_QwtHPb2qlGve5-ijAcyp3GPP60v3ySFZpekN6j1KFaMg9xuD3lrB33XA_hGR5DwQmo-6vohTdNfQqvWW1F1rcNi_RAdaCx-P725xY0U0IGg_thDEsgIlLICd-Z5lyvdhJbIGHl6H-MKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c82e4489c1.mp4?token=KcFU9srlv3wm9hOPO6EBtAS5xmtah-1FpZzrTTnmZbL-7j9t6MXuJ7SmDNjFSVRkdFi_siamfatB3bFghqgAca7yUy6VpCPkj_gSAomx76rDNUGXEp7yi_JfQ_crgfp4BW6rRdg5dgMRjfd6mJ6rOSttZDnZvwf5_nXpaUhaeTNdN0JrEr2ETgbzLUGvO4-iAAK2Yd2M3_QwtHPb2qlGve5-ijAcyp3GPP60v3ySFZpekN6j1KFaMg9xuD3lrB33XA_hGR5DwQmo-6vohTdNfQqvWW1F1rcNi_RAdaCx-P725xY0U0IGg_thDEsgIlLICd-Z5lyvdhJbIGHl6H-MKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زيلينسكي: بعد فترة وجيزة من منشور الرئيس ترامب على منصة "تروث سوشيال"، أطلقت روسيا هجومًا استهدف محطة توليد كهرباء في خاركيف.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93335" target="_blank">📅 11:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93334">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇸🇦
الطيران المدني السعودي:
تمديد تعليق العمليات التشغيلية في مطار الملك خالد الدولي بالرياض.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93334" target="_blank">📅 11:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93333">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزير الخارجية الإيراني يبلغ نظيره السعودي باستعداد طهران لتقديم المساعدة لتسهيل الحوار بين السعودية واليمن</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93333" target="_blank">📅 11:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93332">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
وزير الخارجية البولندي:
يجب أن يستعد الناتو لهجوم روسي مميت.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93332" target="_blank">📅 10:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93331">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd1ac355ac.mp4?token=ln3PmUbt3RnoCCwijAXwH8WshTALXTFdzYSZEi_-XUXAg-cUKK8EnfK9ph3hQKCYAvZzmg2M_0ESoT3Rq08JmMIcdqp7pBM5ap7jCxn2aRRg6PYyIzmSr403MpmcUfKt8rY81UkcLIJKhNTzuN_cZc1YGAZwNFiD9SDvY7MxmK0DPvq4DYzsswQEjDd63I4obYIhCaB9EKvuv5qOyNv2r_wH4ncoiiXu-k94ovOemuAAEVTkqlbeA4CWBLg0dtD865o2vY3HkT9tycSymtjvljVEqWp6qXUuvyQVoYx89H9f11NEgm4uYgszw_EI02ow5ydF5DF7-H2MJYqIlopliw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd1ac355ac.mp4?token=ln3PmUbt3RnoCCwijAXwH8WshTALXTFdzYSZEi_-XUXAg-cUKK8EnfK9ph3hQKCYAvZzmg2M_0ESoT3Rq08JmMIcdqp7pBM5ap7jCxn2aRRg6PYyIzmSr403MpmcUfKt8rY81UkcLIJKhNTzuN_cZc1YGAZwNFiD9SDvY7MxmK0DPvq4DYzsswQEjDd63I4obYIhCaB9EKvuv5qOyNv2r_wH4ncoiiXu-k94ovOemuAAEVTkqlbeA4CWBLg0dtD865o2vY3HkT9tycSymtjvljVEqWp6qXUuvyQVoYx89H9f11NEgm4uYgszw_EI02ow5ydF5DF7-H2MJYqIlopliw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇱🇧
جيش الإحتلال الإسرائيلي:
قبل فترة وجيزة، أُطلق صاروخ اعتراض نحو هدف جوي مشتبه به تم تحديده في منطقة يتواجد فيها قوات الجيش الإسرائيلي في جنوب لبنان. التفاصيل قيد التحقق.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93331" target="_blank">📅 10:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93330">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇸🇦
بعد الدك اليماني وإغلاق مضيق هرمز.. وزير الطاقة السعودية:
لا يمكن أن يكون هناك مستقبل طاقة للجميع دون توافر أمن الطاقة وأمن لنقل الطاقة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93330" target="_blank">📅 10:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93328">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
🇸🇦
جرّاء الحصار اليمني.. السفارة الأمريكية في الرياض تجدد نشر التحذير الأمني لمواطنيها:
تدرك بعثة الولايات المتحدة وجود هجمات إضافية على مطار الملك خالد الدولي في الرياض وهجوم مستهدف على مطار الملك فهد الدولي في الدمام في 11 أكتوبر.
يحتاج موظفو الحكومة الأمريكية العاملون في السعودية إلى تصريح خاص لاستخدام مطار الملك خالد الدولي في الرياض، بالإضافة إلى المطارات في جدة والدمام.  يرجى اتخاذ أقصى درجات الحذر عند استخدام جميع المطارات الرئيسية في السعودية.
يجب على مواطني الولايات المتحدة أن يكونوا على دراية بإمكانية إلغاء الرحلات الجوية، وإغلاق المجال الجوي، وتعطيل السفر. نوصي بالتحقق من حالة مغادرة رحلتك مباشرة مع شركة الطيران ومع المطار.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/93328" target="_blank">📅 10:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93327">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1712bbf34.mp4?token=jhGfrGoc1YgYqdbzc5PRNxlLQNloOzPa3DAxN86YVA3E08JvUY4u5YEaJHs4VZzWHxdfF7GqeC5jbt38Q3hbINT6JobvwowyszDEjWgQ_kZKmmU4iiPDRegNNReOsgmqu7oc-9DWCLQ-Of9UgaaavRWah4l8w3Tn7uLFdAAWbYLK1FZY6GW5KQyiwB21CXjEGlpB2kg85PngSq5RHoz_3K8mKLFmaucJifruJ2XgQecDRYF-qFzHkM_6QkxDC__4jslKkeaX7Mc2ps1P4YSgqJQTJcIQ-D8ydHtlbZaeQaCPrMjxYQ_-Gw8TM5m3VGxRS1h2Yp47B80iQwvcOkn7XBy8OoAsptejgQ6-zY5LRKgF5VVix-TiJKr4yeWD3D1qEh50JPghm4gckJDB_PU_knggYY2tq8lqHlCa6e_-8SbRfliFDdqF7_fqGoZI_vb4FJXv06J45PhWJzzKLSHz6HwBlF9mCRW7nWpMpgby64Gw9qkWLnXiYWSItb09IPtvNoCkw8Xil-Dhre9ukjx6Kqy6XXimV00RlX1ZI3BQ8PdH7jBI0dMABp1z_o12LnX7ckVbVD37czg_KkKV75A7JZxyoBXN18mXDxtUM9krybFhixzfu-7GEDG5Dkd-1k12huY-9l-4o9jKP6-SjW-CJZNFYdI52Xwv3awjkto2ZXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1712bbf34.mp4?token=jhGfrGoc1YgYqdbzc5PRNxlLQNloOzPa3DAxN86YVA3E08JvUY4u5YEaJHs4VZzWHxdfF7GqeC5jbt38Q3hbINT6JobvwowyszDEjWgQ_kZKmmU4iiPDRegNNReOsgmqu7oc-9DWCLQ-Of9UgaaavRWah4l8w3Tn7uLFdAAWbYLK1FZY6GW5KQyiwB21CXjEGlpB2kg85PngSq5RHoz_3K8mKLFmaucJifruJ2XgQecDRYF-qFzHkM_6QkxDC__4jslKkeaX7Mc2ps1P4YSgqJQTJcIQ-D8ydHtlbZaeQaCPrMjxYQ_-Gw8TM5m3VGxRS1h2Yp47B80iQwvcOkn7XBy8OoAsptejgQ6-zY5LRKgF5VVix-TiJKr4yeWD3D1qEh50JPghm4gckJDB_PU_knggYY2tq8lqHlCa6e_-8SbRfliFDdqF7_fqGoZI_vb4FJXv06J45PhWJzzKLSHz6HwBlF9mCRW7nWpMpgby64Gw9qkWLnXiYWSItb09IPtvNoCkw8Xil-Dhre9ukjx6Kqy6XXimV00RlX1ZI3BQ8PdH7jBI0dMABp1z_o12LnX7ckVbVD37czg_KkKV75A7JZxyoBXN18mXDxtUM9krybFhixzfu-7GEDG5Dkd-1k12huY-9l-4o9jKP6-SjW-CJZNFYdI52Xwv3awjkto2ZXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
بعد فشل الرادارات الجوية الأمريكية التابعة لحلف الناتو في السعودية..
حكومة الرياض تستخدم تطبيق لكشف الهجمات التي تتلقاها من اليمن وتدعو المواطنين للتبليغ على أي طائرة مسيرة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/93327" target="_blank">📅 09:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93326">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇸🇦
وول ستريت جورنال:
يتنقل ولي العهد السعودي، الأمير محمد بن سلمان، بحذر بين القصور المحصنة للغاية والمجهزة بملاجئ، ويرافقه حراس أمن تم اختيارهم بعناية، في ظل تصاعد هجمات الحوثيين.
أفاد مسؤولون سعوديون بأن المملكة تعاني من نقص في صواريخ الاعتراض، وتواجه صعوبات في حماية بنيتها التحتية للطاقة وقصورها الملكية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93326" target="_blank">📅 08:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93324">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93a97c9ce3.mp4?token=se3pSyWuv6F90Qc1TN4I0S9xEXfGQyFp5ezpyWxKJE2wfPGNL-NBKYFNRSDbSvyGtjVKPFdIKoOXVAbN012uvLCJkFs_BVOVpSYoz8EY_79qNeiY_wAJ1kgk7ltr0Y5dui2fvh_MeTPNnUiB4FsZlDAVtHqvenU5XV9IgLuv0cL6eHt3pOqT2G8-fmmcUWtxtLKHcAbY_VoFPZJK77GLoub5p1rTNAccX-3sJRKMftDoGzjZVIIo3o31ur-HxCtKx8UKRXXmYQRppr5rgZS58P6L0-54Cnh5yzSxnYp-Z9hasML230DSAx6FwznuJ9lOsXoaG309hb2R0zphoP8N7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93a97c9ce3.mp4?token=se3pSyWuv6F90Qc1TN4I0S9xEXfGQyFp5ezpyWxKJE2wfPGNL-NBKYFNRSDbSvyGtjVKPFdIKoOXVAbN012uvLCJkFs_BVOVpSYoz8EY_79qNeiY_wAJ1kgk7ltr0Y5dui2fvh_MeTPNnUiB4FsZlDAVtHqvenU5XV9IgLuv0cL6eHt3pOqT2G8-fmmcUWtxtLKHcAbY_VoFPZJK77GLoub5p1rTNAccX-3sJRKMftDoGzjZVIIo3o31ur-HxCtKx8UKRXXmYQRppr5rgZS58P6L0-54Cnh5yzSxnYp-Z9hasML230DSAx6FwznuJ9lOsXoaG309hb2R0zphoP8N7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🔻
🇾🇪
توثيقات جديدة تظهر اصابات وارتفاع أعمدة الدخان في مدينة أبها السعودية نتيجة ضربات القوات المسلحة اليمنية
بدري على الحوثي يلمس أراضيك</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/93324" target="_blank">📅 07:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93323">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fe51abd0.mp4?token=ZTk2jFHHRqwbYXFeics_Yun13wtJ4MFrWPJm_uhsmdxTpQPopfgcaXwBxy0tLIsGbpETEGaggRUJW5P4ke8M36G_L9APYPZv9aFYJZjPJWalpAdrJv7QHeEDwWyI3Ge5HdiJy4eW8e7rYYO7QKbp6zBMhwCTxjy1BIPLL6v7jie_sd-LlncW6qjZ5Ow6hQTLd0GCzxOXsDjTgkr9FWhc8r4NRKiQlRKOgnOHWb-7uhQvz7Y7iitHr1O8yVIUG2LYJInMv71icwqA6ubzuoQWIecBdzv5xC6_XXx_OdsCDYFUUz_HCPlNYuD9I6eUvSy57b92UNlYigIJLZmKoxKBzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fe51abd0.mp4?token=ZTk2jFHHRqwbYXFeics_Yun13wtJ4MFrWPJm_uhsmdxTpQPopfgcaXwBxy0tLIsGbpETEGaggRUJW5P4ke8M36G_L9APYPZv9aFYJZjPJWalpAdrJv7QHeEDwWyI3Ge5HdiJy4eW8e7rYYO7QKbp6zBMhwCTxjy1BIPLL6v7jie_sd-LlncW6qjZ5Ow6hQTLd0GCzxOXsDjTgkr9FWhc8r4NRKiQlRKOgnOHWb-7uhQvz7Y7iitHr1O8yVIUG2LYJInMv71icwqA6ubzuoQWIecBdzv5xC6_XXx_OdsCDYFUUz_HCPlNYuD9I6eUvSy57b92UNlYigIJLZmKoxKBzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لأستهداف القوات المسلحة اليمنية لمدينة ابها في السعودية وإصابة أهدافها بشكل مباشر</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/93323" target="_blank">📅 05:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93322">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">القوات اليمنية المسلحة تستهدف خميس مشيط بصاروخ بالستي جنوب غرب السعودية</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/93322" target="_blank">📅 03:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93321">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوي انفجارات في ابها  غرب السعودية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/93321" target="_blank">📅 03:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93320">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انباء عن دوي انفجار في محيط السليمانية شمال العراق</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/93320" target="_blank">📅 02:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93319">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
رويترز
:
11 أكتوبر تشرين طلبت إدارة الطيران الاتحادية ​الأمريكية اليوم الأحد من ‌شركات الطيران الأمريكية توخي الحذر عند الطيران إلى السعودية ​أو فوق أراضيها، ​مشيرة إلى تهديدات أمنية مرتبطة ⁠بالأنشطة العسكرية الجارية ​والتدخل في أنظمة الملاحة.
ويأتي ​الإشعار الذي أصدرته إدارة الطيران الاتحادية، والذي يستمر سريانه حتى ​10 ديسمبر كانون الأول، ​في أعقاب الهجمات التي استهدفت ‌مطار ⁠الرياض الدولي أمس السبت واليوم الأحد. وأسفر الهجوم الذي وقع يوم السبت ​عن مقتل ​13 ⁠شخصا وإصابة أكثر من 300 آخرين.
﻿</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/93319" target="_blank">📅 01:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93318">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇸🇦
الطيران المدني السعودي:
بشأن  استهداف مطار الملك خالد الدولي بالرياض عصر يوم الأحد الموافق 11 أكتوبر 2026م؛ أفادت الهيئة بأنه نتج عنه وفاة مقيم من الجنسية الباكستانية وإصابة 11 شخص أخرين؛ وقد تم بشكل فوري نقلهم إلى المستشفى لتلقي الرعاية الصحية اللازمة. كما أسفر الاعتداء عن أضرار مادية يجري حصرها.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/93318" target="_blank">📅 01:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93317">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
أسعار النفط تصل إلى 104 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/93317" target="_blank">📅 01:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93316">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
🇸🇦
السفارة الأمريكية في السعودية:
تُدرك البعثة الأمريكية وقوع هجمات إضافية على مطار الملك خالد الدولي في الرياض، وهجوم مُستهدف على مطار الملك فهد الدولي في الدمام بتاريخ 11 أكتوبر. يحتاج موظفو الحكومة الأمريكية العاملون في المملكة العربية السعودية إلى تصريح خاص لاستخدام مطار الملك خالد الدولي في الرياض، بالإضافة إلى مطاري جدة والدمام. يُرجى توخي الحذر الشديد عند استخدام جميع المطارات الرئيسية في المملكة العربية السعودية. يجب على المواطنين الأمريكيين الانتباه إلى احتمالية إلغاء الرحلات الجوية، وإغلاق المجال الجوي، واضطرابات السفر. نوصي بالتحقق من حالة مغادرة رحلتكم مباشرةً مع شركة الطيران والمطار. قد تُوفر خيارات السيارات الخاصة والقطارات والحافلات بدائل للسفر الجوي.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/93316" target="_blank">📅 01:26 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

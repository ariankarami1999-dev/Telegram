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
<img src="https://cdn4.telesco.pe/file/O3VZugERr3gM7CQiSTcVqj89hixXkwZw9cpdU05JpmpRGBg-Y-60U8JyZs-qratoAIxlg-qVUYkA4iAv8nOZBIeboT950jFN-J1fH-GzRmlK77o0KtipIBru0WjsK_0tGJ1vMLXlza_2F0QXWj0LaiiMAm5DJGeayzoZgXaq4Rul0fukZua2VBNh9TUHiOe0mx5pLRbzU4eUEmkTI_WBv7h8A__92AXbaRZ3EHiIONdZejXNh25DdPisBjcPkR9j6Nb3F-NaFkCI_I5K5IPmu14IGY9cs3o3PDr3nk2gKgXtA7zbUP8kBtcEukYQEXXfTBqMnvOHicqtARUPpWIRaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 02:28:56</div>
<hr>

<div class="tg-post" id="msg-76950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
🌟
🌟
البيان المشترك بين الولايات المتحدة ولبنان والكبان الصهيوني
:
عقدت الولايات المتحدة الاجتماع الثلاثي رفيع المستوى الرابع بين ممثلين إسرائيليين ولبنانيين يومي 2 و3 يونيو/حزيران 2026.
ونتيجةً للمفاوضات التي قادتها الولايات المتحدة، اتفقت إسرائيل ولبنان على تنفيذ وقف إطلاق النار. ويشترط وقف إطلاق النار وقفًا تامًا لإطلاق النار من قبل حزب الله وإجلاء جميع عناصر الحزب من قطاع الليطاني الجنوبي.
واتفق الجانبان، بتوجيه من الولايات المتحدة، على الإسراع في إنشاء مناطق تجريبية تسيطر فيها القوات المسلحة اللبنانية سيطرةً كاملةً على المنطقة، مانعةً بذلك دخول أي جهات فاعلة غير حكومية.
ستُمكّن هذه الخطوات من إحراز تقدم نحو اتفاق شامل للسلام والأمن.
وأكدت جميع الدول مجددًا أن مستقبل العلاقة بين إسرائيل ولبنان يجب أن يُقرر من قبل الحكومتين السياديتين. ورفضت أي محاولة، من أي دولة أو جهة فاعلة غير حكومية، لاحتجاز مستقبل لبنان رهينةً.  أكدت إسرائيل ولبنان مجددًا عدم وجود أي نية عدائية بينهما، والتزمتا بمواصلة المفاوضات المباشرة لبناء الثقة، وحل جميع القضايا العالقة، والعمل على التوصل إلى اتفاق شامل بين البلدين.
ناقش الوفدان إطارًا أمنيًا، استنادًا إلى المناقشات التي جرت في البنتاغون في 29 مايو/أيار، يهدف إلى ضمان سيادة لبنان وإسرائيل وأمنهما وسلامة أراضيهما بشكل مستدام. ويشمل ذلك تفكيك الجماعات المسلحة غير الحكومية، ومنع عودتها للظهور.
أدانت جميع الأطراف هجمات إيران على دول المنطقة، والأنشطة المستمرة التي تقوض الاستقرار في جميع أنحاء الشرق الأوسط، سواء من خلال دعم الوكلاء أو أي أعمال عدوانية أخرى.
جددت الولايات المتحدة دعمها المستمر للحكومتين لممارسة سيادتهما. وأكدت مجددًا أن أي اتفاق لوقف الأعمال العدائية يجب أن يتم التوصل إليه مباشرة بين الحكومتين، بوساطة أمريكية، وليس عبر أي مسار منفصل. وشددت الولايات المتحدة على عزمها دعم القوات المسلحة اللبنانية، بهدف تحسين قدراتها وتمكينها من ممارسة السيادة بشكل فعال في جميع أنحاء الأراضي اللبنانية.  أكدت إسرائيل على تصريح وزير الخارجية روبيو الصادر في 2 يونيو/حزيران، والذي أكد فيه أن حزب الله ليس عدوًا لإسرائيل وأمريكا فحسب، بل هو عدو للبنان أيضًا.
وأكدت إسرائيل مجددًا أن أمنها واحترام وحدة أراضيها لا يمكن تحقيقهما إلا من خلال نزع سلاح حزب الله وتفكيك بنيته التحتية في جميع أنحاء لبنان. وشددت على أهمية المفاوضات المباشرة بقيادة الولايات المتحدة لحل جميع القضايا العالقة وتحقيق سلام وأمن دائمين.
وأكد لبنان مجددًا على ضرورة الاحترام المتبادل للحدود المعترف بها دوليًا، والحاجة المُلحة إلى التنفيذ الكامل لوقف إطلاق النار، مع التأكيد على مبادئ وحدة الأراضي وسيادة الدولة الكاملة. والتزم لبنان، بدعم من الولايات المتحدة، بتعزيز قدرات القوات المسلحة اللبنانية لفرض سيطرة فعالة على جميع أنحاء البلاد.
واتفق الطرفان على استئناف المسارين السياسي والأمني ​​خلال الأسبوع الذي يبدأ في 22 يونيو/حزيران، بهدف التوصل إلى اتفاق شامل. ووافقت الولايات المتحدة على مواصلة تسهيل التواصل بين الطرفين خلال هذه الفترة.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/naya_foriraq/76950" target="_blank">📅 02:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c8f003d5.mp4?token=rDf2rZmF3zI2OCxR3ll_xtGHEpMGOqoc_lv__ePd18E7pyywt8PP6lqPrJoPeSo2712YW1Y7GVbTkghmSU4xR3RDGDtcQMzMMdA3h8ZzcH1YA4VuWTgXs5IJ6zjnivpVcPjTyojRdkKo1pzmF_-Y8npxxTfUngpkDCFkn0Pf89LbRrAxJ3vGtC7iB57jM62Qx3pJKMAYiutr1ZBgEWiRx_JQHxKj88_LT3ksvTxUUu2eusbY5oJcaGmIhlcKkQyQa_h-QbbdfdnhI_HN4RZ1RC2-a3s-hLRCxGMvayqtp9_wYLSBwBhSwb5aqIREI7t6MBu9nWX4JWJKJ_4fjrgueQ1emqfO-tkndj7vE1NAdxsVx58hxOWaBDEx_PB0UmvhZs2-jbpzNJuA7m9T6q7EWcaBa1kl693Xi8Kj8WAIV39vIOQRQHZrmpNo7vDW-qsPBKXGqKoJ4jpKeloYhIRzBwIrmHBgZmeO-n97vQj8bDNJyUoayOPD3pFW4mA40mS7v0NolfIKqA77Q9i9FGK4mxe5wl91dS-7Ufm3CdibHBuOKsoPQDxuSMcgbppaeRNN12O7H3WbHeJXO37rZX8xrlATYDFGn4SkVbrJmDEjRAtAom5dpjw-PvW5Ukd1D7jP1mumKRPOuRkVq8PXmv1hX7NZY03W8cx1NGdIBve53UI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c8f003d5.mp4?token=rDf2rZmF3zI2OCxR3ll_xtGHEpMGOqoc_lv__ePd18E7pyywt8PP6lqPrJoPeSo2712YW1Y7GVbTkghmSU4xR3RDGDtcQMzMMdA3h8ZzcH1YA4VuWTgXs5IJ6zjnivpVcPjTyojRdkKo1pzmF_-Y8npxxTfUngpkDCFkn0Pf89LbRrAxJ3vGtC7iB57jM62Qx3pJKMAYiutr1ZBgEWiRx_JQHxKj88_LT3ksvTxUUu2eusbY5oJcaGmIhlcKkQyQa_h-QbbdfdnhI_HN4RZ1RC2-a3s-hLRCxGMvayqtp9_wYLSBwBhSwb5aqIREI7t6MBu9nWX4JWJKJ_4fjrgueQ1emqfO-tkndj7vE1NAdxsVx58hxOWaBDEx_PB0UmvhZs2-jbpzNJuA7m9T6q7EWcaBa1kl693Xi8Kj8WAIV39vIOQRQHZrmpNo7vDW-qsPBKXGqKoJ4jpKeloYhIRzBwIrmHBgZmeO-n97vQj8bDNJyUoayOPD3pFW4mA40mS7v0NolfIKqA77Q9i9FGK4mxe5wl91dS-7Ufm3CdibHBuOKsoPQDxuSMcgbppaeRNN12O7H3WbHeJXO37rZX8xrlATYDFGn4SkVbrJmDEjRAtAom5dpjw-PvW5Ukd1D7jP1mumKRPOuRkVq8PXmv1hX7NZY03W8cx1NGdIBve53UI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الكويت تبث مشاهد للحظة القصف المركب الذي استهدف مطار الكويت واسفر عن اضرار جسيمة</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/naya_foriraq/76949" target="_blank">📅 01:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76948">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دولة الاخ المناضل كيم جونغ اون في كوريا الشمالية تعقد اجتماعًا هامًا لتعزيز ترسانتها النووية .</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76948" target="_blank">📅 00:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وكالة رويترز: الولايات المتحدة ستخفض قدراتها التي تساهم بها في القوات الدائمة لحلف الناتو، والتي تشمل الطائرات المقاتلة، وناقلات الوقود، والأصول البحرية، والطائرات المسيّرة. دول الناتو تلقت تحذيرات بأن التخفيضات قادمة لا محالة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76947" target="_blank">📅 00:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏ ترامب: إذا نجح الاتفاق مع إيران، فربما يستطيع الناس البدء في بناء الشقق والمباني المكتبية في إيران.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76946" target="_blank">📅 00:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1w2d57tE5IzwWp_CJkR5mFdgvcSDJr8to6rgMNbye2cnzL0jRqfOtZo7FJAl_NNgCPLaapwjvtaw4C6ezJ5HfAYyFd2aFsAkMIt5EMM9iDefEvP97WpK-V3NXHb9iYhOcwHlWTxzAKUFoPp_b0EJuqa_pE7GOdBGPEA6qzWlqZL8sthWfhh7mAOUqcdbPxJgVT53DVul2I_627wFM7Qf0U9WeVYbmbiK01h_fYDog8F0bxL9ZX5jg4m9yD-_U0zniaeh-2eSfEHSWrzssx1zFiz1uKOxcYrtAC5cIzeIvyF2mhoK38-cbSiI9B8fgZcMa1u53QWY6GyWCBsEeIXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
إعفاء المتحدث الرسمي باسم وزارة النفط العراقية صاحب بزون بعد تصريحات
مثيرة للجدل طفّي التبريد بالصيف”، التي أثارت موجة واسعة من الاستياء الشعبي والانتقادات الإعلامية، بعد تحميل المواطنين مسؤولية الازمة</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76945" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامب: فتح مضيق هرمز سيكون سريعاً عند توقيع مذكرة تفاهم.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76944" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامب: الحصار له تأثير أكبر من القصف.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76943" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76942">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامب: نسعى للفصل بين قضايا إيران ولبنان وفتح مضيق هرمز والاشتباكات في لبنان.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76942" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامب: أريد الحصول على اليورانيوم المخصب من إيران. سنستعيد اليورانيوم المخصب من إيران في المستقبل القريب.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/76941" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76940">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏ترامب يهاجم مراسلة السي ان ان كايتلان كولينز: مراسلة فاسدة تقف هنا، لا تبتسم أبدًا. شابة جميلة، لا تبتسم أبدًا. لم أرَ ابتسامة على وجهها قط. أراها واقفة وعيناها تفيضان بالكراهية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76940" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏ترامب: وقف إطلاق النار في لبنان مختلف عن وقف إطلاق النار في أماكن أخرى من العالم</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76939" target="_blank">📅 23:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76938">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامب: إيران قريبة من توقيع الاتفاق نظريًا.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76938" target="_blank">📅 23:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامب حول إيران: يمكننا الاستمرار لمدة أسبوعين إلى ثلاثة أسابيع إضافية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76937" target="_blank">📅 23:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76936">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامب: يفضل عدم القضاء على إيران.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/76936" target="_blank">📅 23:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامب يتخلى عن الكويت</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76935" target="_blank">📅 23:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامب: الهجمات بين إيران والكويت كانت رد فعل متبادل.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/76934" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامب: المفاوضات مع إيران تسير بشكل جيد، مفاوضات قد تُعقد في عطلة نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76933" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76932">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامب: المفاوضات مع إيران تسير بشكل جيد، مفاوضات قد تُعقد في عطلة نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76932" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76931">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hha3exk2NkGoiBK0cgaLOJ3cgXv6H6rPtAyCE2FFxlqMFm8L7-eAv2UK5hzcjX_ueTYU6eqVPvdvsOgFE8Skpj_m49VrN2CwpIzFPgCIenwGWRnfIvd0HlENIdi1RWHQOSaZQn0_SwYqVdYJu9P2yWP6LwKGPXonVvEHun7QJ6MCJ8uV0S8EvF0VQH-W_M6tsQzZZcBv-N_VhDKTpoune1uQ9FzpJKNhXoZ9wGPWhMr-fkB_VAzGpqRUKiyWdkNK4eIQjb8O2A_w4pJEvoEguJ_U65NTKO_DEBQMh0B2mnVxBWxCtpmv7y849STHfr6e_tRo2AUTvZO3oBxbCQiL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏توم باراك يشيد بالفصائل التي نزعت سلاحها:  نتقدم بأحر التهاني إلى رئيس الوزراء العراقي  على هذه الخطوة الهامة، التي تُمثل حجر الأساس لحكم ذاتي عراقي مُتجدد، قائم على استعادة السيادة، والاستقرار الدائم، ووعد النهضة الوطنية. كما نُشيد بالجماعات التي سيُسهم…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76931" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76930">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb7cd4d19.mp4?token=gA69FVewgL46abjCLxmZkbRH4A1Ee-HAvJbxB02KP5PghuAVoByP-RbHGD1mVxMxj2oLDkG6MNqhxF1QF-7kelXhibNfCiDlGYR7IxhgH93Qc4D4e6EKVyS9mvxavr5o3tiEsx1zEmHtR2uhDxyYfzkHmtIht54rgzcH-zCIQyJyqddRVOJBZdGiiFtBNWezTGwEkdDwcjfPsRDg9D_6g19MHIQvmtqtPcEu4DdozwEVSDbHGmifbvcEylI3RBxS3WXrCFosdWL7nlDJOTzSKyGbsTvUYcyjOg9TmxLXNvvGHndJ3M5-juGtJSD9X_fbiPVAAcC7Ow9rCLVfLDXAgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb7cd4d19.mp4?token=gA69FVewgL46abjCLxmZkbRH4A1Ee-HAvJbxB02KP5PghuAVoByP-RbHGD1mVxMxj2oLDkG6MNqhxF1QF-7kelXhibNfCiDlGYR7IxhgH93Qc4D4e6EKVyS9mvxavr5o3tiEsx1zEmHtR2uhDxyYfzkHmtIht54rgzcH-zCIQyJyqddRVOJBZdGiiFtBNWezTGwEkdDwcjfPsRDg9D_6g19MHIQvmtqtPcEu4DdozwEVSDbHGmifbvcEylI3RBxS3WXrCFosdWL7nlDJOTzSKyGbsTvUYcyjOg9TmxLXNvvGHndJ3M5-juGtJSD9X_fbiPVAAcC7Ow9rCLVfLDXAgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني: استهدفنا قبل ساعات "مركز القيادة والتحكم" المتمركز على متن مدمرة أميركية في بحر عمان</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76930" target="_blank">📅 22:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76929">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">استهداف سفينة عسكرية أمريكية بالقرب من المياه الإقليمية الإيرانية في خليج عمان.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76929" target="_blank">📅 22:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76928" target="_blank">📅 22:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">استهداف سفينة عسكرية أمريكية بالقرب من المياه الإقليمية الإيرانية في خليج عمان.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76927" target="_blank">📅 22:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
🔳
المتحدث باسم الحرس الثوري الإيراني:  أظهر تحقيقنا وبحثنا في حادثة استهداف مبنى الركاب بمطار الكويت أن القوات الجوية التابعة للحرس الثوري الإيراني لم تطلق النار على هذا الهدف، وأن تدمير مبنى الركاب كان نتيجة خطأ في أنظمة باتريوت الأمريكية، التي سقطت على…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76926" target="_blank">📅 22:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">💲
📈
العقود الآجلة لخام برنت ترتفع 1.81 دولار لتبلغ نحو 98 دولارا للبرميل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76925" target="_blank">📅 22:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76924">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
عراقجي:  نحن والأميركيون ندرس النصوص التي تم تبادلها ونعمل على صياغة نهائية.  العودة إلى المفاوضات ستكون مستندة إلى تأمين حقوق الشعب الإيراني ونهاية الحرب على إيران ولبنان وفي المنطقة.  أنقل لكم حقائق أن الأميركيين لمسوا قدرة إيران في هذه الحرب خلال الـ40…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76924" target="_blank">📅 22:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
احتفالات كبيرة في العاصمة اليمنية صنعاء بذكرى عيد الغدير الاغر.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76923" target="_blank">📅 22:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76922">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
إيران الإسلامية لاتتخلى عن حلفائها.. عراقجي: نحن نعتبر لبنان بلداً شقيقاً وصديقاً لنا ولم نسعَ أبداً إلى التدخل في الشؤون الداخلية اللبنانية.  كانت لدينا وجهات نظر وملاحظات بيّناها وحزب الله جزء مهم من البنية السياسية في لبنان.  لبنان جزء لا يتجزأ من الحرب…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76922" target="_blank">📅 21:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76921">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
إيران الإسلامية لاتتخلى عن حلفائها..
عراقجي:
نحن نعتبر لبنان بلداً شقيقاً وصديقاً لنا ولم نسعَ أبداً إلى التدخل في الشؤون الداخلية اللبنانية.
كانت لدينا وجهات نظر وملاحظات بيّناها وحزب الله جزء مهم من البنية السياسية في لبنان.
لبنان جزء لا يتجزأ من الحرب بين إيران وأميركا والكيان الصهيوني ويتعرض للعدوان.
نحن نعتبر أن مصير حرب إيران مع أميركا و"إسرائيل" ليس منفصلاً عن مصير الحرب في لبنان.
هناك ترابط كبير منذ اليوم الأول بين لبنان والحرب على إيران حيث طُرح ذلك في المفاوضات وموضوع نهاية الحرب.
مواقفنا واضحة جداً بأن نهاية الحرب ووقف إطلاق النار يجب أن يكون في إيران وجبهات المقاومة كافة ومن بينها لبنان.
عند وقف إطلاق النار طلبت من رئيس وزراء باكستان إدراج عبارة "لبنان خاصة" عند القول إن الحرب تتوقف في الجبهات كافة.
ما تم في النهاية هو إدراج لبنان في وقف إطلاق النار.
نحن اليوم في المفاوضات التي نجريها للوصول إلى مذكرة تفاهم مع الولايات المتحدة البند الأول فيها هو نهاية الحرب.
في الجملة الأولى من مذكرة التفاهم قلنا إن وقف الحرب يكون في محور المقاومة كافة وأولاً في لبنان.
لبنان دفع أثماناً في هذه الحرب التي فُرضت علينا من قبل أميركا و"إسرائيل".
أصدقاؤنا وأحباؤنا في لبنان تعرضوا لاستهداف من قبل "إسرائيل" وبكل تأكيد مصيرنا واحد حتى نهاية هذه الحرب.
المصير واحد ومرتبط بين إيران ولبنان في الحرب ونهايتها.
إما أن تتوقف الحرب في إيران ولبنان أو لا تتوقف لا في إيران ولا في لبنان.
من أوقف الحرب خلال اليومين الأخيرين هو قدرة المقاومة اللبنانية بالدرجة الأولى وقدرة القوات المسلحة في إيران.
عندما وصل الأمر إلى قوات الكيان الصهيوني بأن تهاجم الضاحية الجنوبية لبيروت اتخذنا موقفاً قاطعاً والقوات المسلحة استعدت للرد.
منذ أيام تنتهك "إسرائيل" وقف إطلاق النار بين إيران وأميركا وفي لبنان لكن هذا الانتهاك قوبل برد من حزب الله.
إن انتهاك وقف إطلاق النار في بيروت هو عدوان وقد أعلنا للأطراف كافة أنه إذا هاجموا بيروت فإننا لن نتحمل ذلك.
قلت لكل قائمة اتصالاتي بوضوح إن نتيجة العدوان على بيروت ستكون عودة الحرب ومن واجبنا التصدي للعدوان.
أتقدم بالشكر لجميع بلدان المنطقة الذين ساهموا بهذا واهتموا وأجروا اتصالات مع أميركا ومارسوا ضغطاً عليها.
في النهاية أميركا منعت الهجوم الإسرائيلي على بيروت بعد الموقف الإيراني والضغط عليها.
في أي لحظة قواتنا المسلحة مستعدة لإستئناف الحرب وضرب "إسرائيل".
قواتنا المسلحة مستعدة لضرب "إسرائيل" إذا اعتدت على بيروت.
المفاوضات تتأثر بالعوامل الخارجية وهذا أمر طبيعي.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76921" target="_blank">📅 21:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76920">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
🔳
المتحدث باسم الحرس الثوري الإيراني:
أظهر تحقيقنا وبحثنا في حادثة استهداف مبنى الركاب بمطار الكويت أن القوات الجوية التابعة للحرس الثوري الإيراني لم تطلق النار على هذا الهدف، وأن تدمير مبنى الركاب كان نتيجة خطأ في أنظمة باتريوت الأمريكية، التي سقطت على هذا المبنى بعد فشلها في اعتراض صواريخ إيرانية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76920" target="_blank">📅 21:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76919">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427e365e60.mp4?token=S6BBAMeCC0juTfHq7RoaqWIHWrCdCvtvIxiiHKdyUl4btbDt5Fn4EhV2DiCzarJGoc8ixDEljzRf0mbWulKUWavVDlrlMp52ba865pworVS-j5tmlUx8hDkoxbC6KddhnSRD4y5qJsU4qMxmJ94tUaaJIm0idxqbLB-F5OPDdS6a9RvfIRm6KZSrTiX1W7OHXN9k0PHnYluzzV8F7_NnJraiWZ3onJ5af4fO0fG6VdXvGBbpHOw7XlhDndC4NpZAHLqVxaDFiy-8n_r_Wykgg-JthM55E09JFmAkSjicgKxrnrpz_EMljccIxc2rUGDURZkOHq9oW0UUHmzDDipEnzef3OghyEJsCDz8xywzDOqr_VcpyJZuH1Y1SkXAJZ916sxKGGShi2I7wjpBO1EObrogneILP6BxirsWdL25wqztZqyjiZm04FI0dKAb3wkOcbVGCAO_RhED5KWtHd9Ne52olQIrhzUqR5mljtSQjU0d-qCnYLI1YBdy_VTKSCv65_wVhWGTw-3fbWErWY9XcEMwj_AleQSHzTGWWrnBoNNLnRj6yXU1s9KwzyvoWhDddJB9YtYm6SbomqHf0Yq2UMgTW2MK4WnbEkn2bM-KxQDXQSaKNIXSDHDL2jeg5tm9rDbhefK4ueD0Lzaa9xmBavI0OJLXRDZBDD9ZZDLIJdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427e365e60.mp4?token=S6BBAMeCC0juTfHq7RoaqWIHWrCdCvtvIxiiHKdyUl4btbDt5Fn4EhV2DiCzarJGoc8ixDEljzRf0mbWulKUWavVDlrlMp52ba865pworVS-j5tmlUx8hDkoxbC6KddhnSRD4y5qJsU4qMxmJ94tUaaJIm0idxqbLB-F5OPDdS6a9RvfIRm6KZSrTiX1W7OHXN9k0PHnYluzzV8F7_NnJraiWZ3onJ5af4fO0fG6VdXvGBbpHOw7XlhDndC4NpZAHLqVxaDFiy-8n_r_Wykgg-JthM55E09JFmAkSjicgKxrnrpz_EMljccIxc2rUGDURZkOHq9oW0UUHmzDDipEnzef3OghyEJsCDz8xywzDOqr_VcpyJZuH1Y1SkXAJZ916sxKGGShi2I7wjpBO1EObrogneILP6BxirsWdL25wqztZqyjiZm04FI0dKAb3wkOcbVGCAO_RhED5KWtHd9Ne52olQIrhzUqR5mljtSQjU0d-qCnYLI1YBdy_VTKSCv65_wVhWGTw-3fbWErWY9XcEMwj_AleQSHzTGWWrnBoNNLnRj6yXU1s9KwzyvoWhDddJB9YtYm6SbomqHf0Yq2UMgTW2MK4WnbEkn2bM-KxQDXQSaKNIXSDHDL2jeg5tm9rDbhefK4ueD0Lzaa9xmBavI0OJLXRDZBDD9ZZDLIJdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
30-05-2026
مستوطنة كريات شمونة شماليّ فلسطين المحتلة بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76919" target="_blank">📅 21:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
‏ترامب: علاقتي بنتنياهو ممتازة وهناك توافق بيننا في قضية لبنان.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76918" target="_blank">📅 21:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRpzpq6J9U1flut63vJTizYohP8VV6QHIXG4aoZcymjwe3DeOJm4lvvv9NJ110qAv8vdRfMVryVqqrDFucbnnzMrltB9-fvIFEV5hk0iOxaVAzhY3AsumyUcjap0YqFekC9V3zPg8J0i-3IGPUt7TwGwDf40ptFULPyWAayOaCf1DSQtfPum8dqOzD2umP-YxTmuOPwt4FpT3dakAAb5wwxDdJJr4AhkwEVRPKWtVZUI6LNE8ORv2UfagQXYNF_zRBddELiXidUaEOTtwUFsNddcoDvuehNh_uymT6TVfUnovpMMYq0qvfckRvRSOETFYqBK8IKZCKhnmf7xsGtK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما حدث البارحة هو سياسة وسلوك ايران الجديد ! لا مزيد من الصبر الاستراتيجي والتغاضي والمراعاة .. إذا فقعت لايران عين ستفقع ايران عينين للعدو .. والعدو هنا هو امريكا واسرائيل ومن يأويهم !!!
من أراد ان يفهم فهم ومن لم يفهم بعد سيفهم رغماً عنه ولكن بتكلفة اعلى .</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76917" target="_blank">📅 21:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصدر لنايا   اغلب الفصائل التي رفضت فكرة النزع بناء على تغريدة ابو مجاهد العساف و الكعبي و الجعفري هي الفصائل الوحيدة التي استخدمت السلاح منذ حادثة يوم المطار حتى الان وبصورة فعالية ميدانية ذات تاثير واضح " عدا فصيل الغراوي " الذي لم يظهر له موقف واضح حتى…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76916" target="_blank">📅 20:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76915">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴‍☠️
‏
مسؤولين إسرائيليين:
التقديرات بأن إسرائيل ستهاجم بيروت خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76915" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
‏
ترامب:
علاقتي بنتنياهو ممتازة وهناك توافق بيننا في قضية لبنان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76914" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله حول ادعاءات العدو الإسرائيلي الكاذبة بشأن مستشفى تبنين الحكومي:
يواصل العدو الإسرائيلي إطلاق الأكاذيب والافتراءات، مصوبًا سهام التحريض والتضليل نحو الشعب اللبناني تحت غطاء الحرص عليه وعلى أمنه ومستقبله، وآخرها المزاعم التي أطلقها بشأن مستشفى تبنين الحكومي، في محاولة مكشوفة لتوفير غطاء سياسي وإعلامي لاعتداءاته المتكررة على المستشفيات والطواقم الطبية والهيئات الصحية والمسعفين، والتي تشكل انتهاكًا فاضحًا للقوانين والأعراف الدولية والإنسانية وترقى إلى مستوى جرائم الحرب.
إن هذه الادعاءات المختلقة تُعدّ تهديدًا علنيًا للمستشفيات اللبنانية والمؤسسات الطبية، لا سيما بعد الاعتداء الأخير الذي طال محيط مستشفى جبل عامل، وأدى إلى إخراجه عن الخدمة وتعريض حياة العديد من المرضى والطواقم الطبية للخطر، بما يؤكد النوايا الحقيقية للعدو في توسيع دائرة استهدافه للبنى التحتية المدنية والصحية والحيوية، وتدمير كل ما ينبض بالحياة، وضرب مقومات الصمود، بهدف بث الخوف والضغط على أهلنا الصامدين وثنيهم عن التمسك بأرضهم.
إننا ندعو المجتمع الدولي والأمم المتحدة والمنظمات الدولية والإنسانية والصحية إلى التحرك العاجل وتحمل مسؤولياتها إزاء هذه التهديدات الإسرائيلية الخطيرة للقطاع الصحي في لبنان، وعدم السماح للعدو بتكرار جرائمه بحق المستشفيات والطواقم الطبية على غرار ما ارتكبه في قطاع غزة.
إن هذه الأكاذيب لن تغير من حقيقة أن العدو الإسرائيلي هو المعتدي على لبنان وشعبه، ولن يُفلح العدو في زرع الشقاق وبث الفتنة بين اللبنانيين. وإن المقاومة مستمرة بواجب الدفاع عن أرضها وشعبها، وتُلحق بالعدو الخسائر الفادحة، وتُجرّعه مرارة خياراته العدوانية الخاطئة، وثمن تدنيسه لأرض الجنوب وتدميره للمنازل والبيوت.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76913" target="_blank">📅 20:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بسم الله الرحمن الرحيم  اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.  ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76912" target="_blank">📅 20:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف:
علّم الإمام الخميني (رضوان الله عليه) الشعب الإيراني ألا يتراجع أمام البلطجة والهيمنة، واليوم، مستلهمًا من هذا النهج، أظهر الشعب الإيراني في معركته مع أمريكا والكيان الصهيوني أن عهد تهديد إيران دون تكلفة قد ولّى، وأن أي عدوان سيُقابل بردٍّ حاسم وقاسٍ ومتناسب.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76911" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بسم الله الرحمن الرحيم  اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.  ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76910" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا وآلية عسكرية تابعة لجيش الإحتلال الإسرائيلي بمسيرة انقضاضية في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76909" target="_blank">📅 19:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76908">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTex9_NlVXtDosRhUdOw5pIRHp41clxDz2LkiEEO111oisGKIEojlyWgxv9ihuNXGYxg65lL5asXOckjLh8W_oxjSRPkQq99jIeqYc-G7AMReqf5i6kt3nkhAbc6o2ykFsffgdG6Qn_3eRx9EvSBEypQKWtLsq302JycdYf6MoXmSHVXUTGT4FY3gAJbe2rBCoGj_-8WK11k-Q5w8faRgOI8Real3BRP8Q_bf2J9U_pUkUtZVP1gPl5LpvygGiGdfsajpOJZXfFJuQohPRjyEdMX0mEIGlwZPiLqpv-IsR2vQU7_sHVBIWD5Qd6Qi2YOFHj4cNu9P7jbNrdmz4a7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.
ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ واستقلالَ قرارِه، ومن أبرزِها:
1ـ إنهاءُ التبعيةِ الماليةِ والاقتصاديةِ التي تقيّدُ إرادةَ العراق.
2ـ وقفُ جميعِ أشكالِ التدخلِ الخارجيِّ في القرارِ السياسيِّ العراقي.
3ـ إنهاءُ أيِّ وجودٍ عسكريٍّ أجنبيٍّ على الأراضي العراقيةِ ومعالجةُ جميعِ التهديداتِ التي تمسُّ السيادةَ الوطنية.
4ـ تمكينُ العراقِ من امتلاكِ منظوماتِ دفاعٍ جويٍّ وراداراتٍ حديثةٍ لحمايةِ أجوائِه وسيادتِه.
5ـ تعزيزُ استقلالِ القرارِ الاقتصاديِّ وفتحُ المجالِ أمامَ شراكاتٍ متوازنةٍ تحفظُ المصالحَ الوطنية.
وعليه، فإنّنا في المقاومةِ الإسلاميةِ – سرايا أولياءِ الدم – نؤكدُ أنّنا سنكونُ من أوائلِ المستجيبينَ لأيِّ مشروعٍ وطنيٍّ حقيقيٍّ لحصرِ السلاحِ بيدِ الدولةِ متى ما اقترنَ ذلك بضماناتٍ فعليةٍ تحقّقُ السيادةَ الكاملةَ وتحفظُ استقلالَ العراق.
كما نؤكّدُ تمسّكَنا بالدفاعِ عن العراقِ وشعبِهِ وقرارِه الوطنيِّ، ورفضَنا لأيِّ وصايةٍ أو هيمنةٍ تمسُّ أمنَه أو سيادتَه أو مصالحَه العليا.
العراقُ أولًا
واللهُ وليُّ التوفيقِ
أبو مهدي الجعفري</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76908" target="_blank">📅 19:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1af8c7a50.mp4?token=Vn_OwYgIA0GOJGIhk5bouejvis52b-dfCtCaUg77xjHExSV-xrL8IwlVCqYOIC3aCknlPSnxpctGN8GIdOM1eCsGqlWEWGLsBkhxmt9vlb-p0WLP03goJ8eq_tzcLvIVdLPpv4ccT9gc3kCmBK7OfcekjsP9O9tcefjITnnCpexfklEf6D5OIuG9vJzanzJaQ8EYr6K8KaSycYEBuUuB6C01Vp8c0nia85LyqNcwKi1NPdPLQcJ1dh5YzR4vbs55ionJx2jYqZbpus3DNIgxnUBrGKb6DIW3TdwBstyqcN6FChoaHPVfGboGtzLUtLxMuIPRon0HYeE3gzQ6UFLKtZDEvBI2vD43N2Bi4nfx-bPbAhakzRFfnzXWygVA5o21KkOFw-T6tG9FGzNEFqlD2WHXXsauvMvzYd6ZddA7jMa4LEH1szF0ad2eBQxUVzEXobl5O8qOzU37r8oPEZG9NLiP4dHaMC0fHC9ECCRlMDY5Vk7-EdZptP2YSuqnfgCjox-BG-HsEdC7Md_VqLBufQl0eVQ_BBcU8QoGZPEyysXq2F726-mzo81kyAEhozAjeCrUnrSRgXUujb2vOLi-nb7wn9OS5-cqqpfEbqRluuW8brQ1qyFJed1gG5rKO2aOhoyT7OBXPeNYx_bq1rlHHWVmwPXqy-xLJy5nYI6ELjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1af8c7a50.mp4?token=Vn_OwYgIA0GOJGIhk5bouejvis52b-dfCtCaUg77xjHExSV-xrL8IwlVCqYOIC3aCknlPSnxpctGN8GIdOM1eCsGqlWEWGLsBkhxmt9vlb-p0WLP03goJ8eq_tzcLvIVdLPpv4ccT9gc3kCmBK7OfcekjsP9O9tcefjITnnCpexfklEf6D5OIuG9vJzanzJaQ8EYr6K8KaSycYEBuUuB6C01Vp8c0nia85LyqNcwKi1NPdPLQcJ1dh5YzR4vbs55ionJx2jYqZbpus3DNIgxnUBrGKb6DIW3TdwBstyqcN6FChoaHPVfGboGtzLUtLxMuIPRon0HYeE3gzQ6UFLKtZDEvBI2vD43N2Bi4nfx-bPbAhakzRFfnzXWygVA5o21KkOFw-T6tG9FGzNEFqlD2WHXXsauvMvzYd6ZddA7jMa4LEH1szF0ad2eBQxUVzEXobl5O8qOzU37r8oPEZG9NLiP4dHaMC0fHC9ECCRlMDY5Vk7-EdZptP2YSuqnfgCjox-BG-HsEdC7Md_VqLBufQl0eVQ_BBcU8QoGZPEyysXq2F726-mzo81kyAEhozAjeCrUnrSRgXUujb2vOLi-nb7wn9OS5-cqqpfEbqRluuW8brQ1qyFJed1gG5rKO2aOhoyT7OBXPeNYx_bq1rlHHWVmwPXqy-xLJy5nYI6ELjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
02-06-2026
آلية نميرا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76907" target="_blank">📅 19:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏴‍☠️
رئيس أركان جيش الإحتلال الإسرائيلي:
سلاح البحرية سيؤدي دورا حاسما في أي مواجهة عسكرية جديدة مع إيران.
قوات البحرية تنشط في ساحات قريبة وبعيدة وتشرف على عمليات لن نكشف عنها حاليا.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76906" target="_blank">📅 19:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAchq7l5395rCpmXF_Gl51QKzw79i3MIV5cu0L6HbkBBcYC5SMrlsLyLnw22fKbJ_rUoBOxo8486zCFp9QYcXVGoos5065I9vx6SJPBQCLQa4pzoS1U7wBz3inoV7OZglco3-ytfRJnBjU43aD62Ug6YJd2Qs4oqQt-Ul6KiFR2JoFWLt6xqb2MSa-f-vRWh26F3mbuNaPpgUE-AUHQ1w94bhPaNCLGL5hoDr6nLP5xqR04mXYhjuPfq0_h4KsFHkJ-q1hiMgCJSs1KQjASPjhN07SNaiSeTNfPjyDkQXD9jwglN_NiQd4LvoJnFqE0KjZbRlCQ-7DPNnL6c1P3LSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
ماركو روبيو: بعض حلفائنا في المنطقة كانوا متعاونين بشكل عدواني للغاية، مثل الإمارات العربية المتحدة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76905" target="_blank">📅 19:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa386b3d31.mp4?token=OSMCiARzQeI9XzBMeINzcRMD_S87fCwEUhO3draSFsmo5YizZwE2rUE0FCCgxA8lRx7jvYMEtOhjorQ0oXHgF88fHb71mDvENFZHAgFGZtPkdlL5hw4AyyskMA-aQlW9AF6a6p3zsauUmc2b3NY-TGiqnjuJv1QjF0H-0t4sdcOTH9wlWv4cGQyBI3xKfCJOipNRKeN7sP7_jkjRZoFlgAw3R1BJa7isl5_4NlPf-0In7RQlNKcFvEiYZ9qgx0-7YnGblCLRDZD1TTz8YnXQUyJI5jwAAO8vp6F9-VCTQ1CyNwto3whXYYmQGGEYlB3w_BbJ122gM9jp1UT7eoNtFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa386b3d31.mp4?token=OSMCiARzQeI9XzBMeINzcRMD_S87fCwEUhO3draSFsmo5YizZwE2rUE0FCCgxA8lRx7jvYMEtOhjorQ0oXHgF88fHb71mDvENFZHAgFGZtPkdlL5hw4AyyskMA-aQlW9AF6a6p3zsauUmc2b3NY-TGiqnjuJv1QjF0H-0t4sdcOTH9wlWv4cGQyBI3xKfCJOipNRKeN7sP7_jkjRZoFlgAw3R1BJa7isl5_4NlPf-0In7RQlNKcFvEiYZ9qgx0-7YnGblCLRDZD1TTz8YnXQUyJI5jwAAO8vp6F9-VCTQ1CyNwto3whXYYmQGGEYlB3w_BbJ122gM9jp1UT7eoNtFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔳
رئيس مجلس الوزراء الكويتي يطلع على حجم الدمار في مطار الكويت الدولي بعد دكه بالصواريخ والمسيرات الإيرانية.  "امبه سنتكوم ليش چذي"</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76904" target="_blank">📅 18:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
‏وزير الخارجية الأمريكي روبيو: إيران ترد على عبور مضيق هرمز بهجمات إقليمية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76903" target="_blank">📅 18:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
روبيو: منصات إطلاق الصواريخ الإيرانية تعرضت لضرر بالغ أدى إلى تدهور قدراتها بشكل كبير.  واضح واضح
😄</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76902" target="_blank">📅 18:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a404b9b4.mp4?token=R2d9dRN9zHIe0r9iE3-bComMg5gst0WmLL2TIUAMVeA8460LlkQ7rHttIQheUvOSzLJMGbV6fYoukt97L6xrKRXGSdiSb4kx3FtliJWLjGYfuz5oOajyqmOhXHGZtNi3An7aAWp_OnqdGbvyjMCXlGTjNWlIenLR9aEvcE3fuheZX6JivMdgF7VI3yn5ELMopSTC1gDXjBoMFOQbndYm29GQlk7PVhboQMt8qHLUG95cOAAzZ5-y2eHXGLavP5KAwuKvO9-aVPtH3x7mMqcmeP3CZpwz4iZKboX66F8X_cJT8Kra1EKMwYxQMLHc9Jf98TrpWRNvhKvDOoP8ux80pl1HWBiQuC7r9P33TELTISHNjRemN1OyxKSXPYAoveuJH8OOEDwrs-ABAJlPngxIqKMuWBCH6mm-Q1og1cz1YonzObq42N0lQVoeNVknW2qj7EafL2qP9q0hMiaz-pAKVAyog8nfOSh9ujqDGsKTZ6yrIkz0SPERiejXdzXmm1vgSscKlNe3vif43uIlb-Slzn1y8XdiWyM2N-p4c8ecR1zXtDvi-OtrjRrq48O8o6oZsS-xw36vuCjb88tn2fVwwscGdiCp4Ed8fjEBf-NR3DoU9oursY-ggHPl-jDvQ-IOQHGdFBi7NiDzkLj_qsQHPm1Qza3vYZF7beXiM9uqNdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a404b9b4.mp4?token=R2d9dRN9zHIe0r9iE3-bComMg5gst0WmLL2TIUAMVeA8460LlkQ7rHttIQheUvOSzLJMGbV6fYoukt97L6xrKRXGSdiSb4kx3FtliJWLjGYfuz5oOajyqmOhXHGZtNi3An7aAWp_OnqdGbvyjMCXlGTjNWlIenLR9aEvcE3fuheZX6JivMdgF7VI3yn5ELMopSTC1gDXjBoMFOQbndYm29GQlk7PVhboQMt8qHLUG95cOAAzZ5-y2eHXGLavP5KAwuKvO9-aVPtH3x7mMqcmeP3CZpwz4iZKboX66F8X_cJT8Kra1EKMwYxQMLHc9Jf98TrpWRNvhKvDOoP8ux80pl1HWBiQuC7r9P33TELTISHNjRemN1OyxKSXPYAoveuJH8OOEDwrs-ABAJlPngxIqKMuWBCH6mm-Q1og1cz1YonzObq42N0lQVoeNVknW2qj7EafL2qP9q0hMiaz-pAKVAyog8nfOSh9ujqDGsKTZ6yrIkz0SPERiejXdzXmm1vgSscKlNe3vif43uIlb-Slzn1y8XdiWyM2N-p4c8ecR1zXtDvi-OtrjRrq48O8o6oZsS-xw36vuCjb88tn2fVwwscGdiCp4Ed8fjEBf-NR3DoU9oursY-ggHPl-jDvQ-IOQHGdFBi7NiDzkLj_qsQHPm1Qza3vYZF7beXiM9uqNdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
02-06-2026
تجمّع لجنود جيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76901" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76900">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8quVXy-FQL5pWA7kWkpAgkeZftEoQfHFYUyn2uqe5Gy7f6XjvAmXA3BNmKiAWNgUMpNHyR5qI81rlRGIcX-2lAfLjCrSt6S7WMcitDGhDoWhMKxUog2Cw-byq64V0gjFkYrfbgcHl_ngJeVW-vyJfDRKQNTw_OJKt7wIzkdrlWLg9E2vN3IcI-nltLV_LcQiH6kDhGt6d5dSGWvPoi2FBld5dnUKV7ldTT_0oyvoOH1OdMZh7zU7c9wci3IMjoNDjKhavtEvDOxq_J2N59QHacS3JmyXKeFFu1r3lrkDuK0G2KIIHKg_RflQmT69HyIb_MheZIMI39QeHzOxIyY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
جيش الإحتلال الصهيوني يزعم إحباط محاولة إدخال أسلحة وذخيرة من الأردن الى الأراضي الفلسطينية المحتلة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76900" target="_blank">📅 18:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
الدفاع الكويتية : تعاملنا مع ١٣ بالستي و ١٧ مسيرة قادمة من ايران .</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76899" target="_blank">📅 18:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sa2Yt5RTN3spCRiz0tLNsTG0DRV9q2Ic8auTV6-8XOucAfF9nbwjVtIVSH7pv4ON-wmWg7E1ytH8Yp5XA6_UoH4rr3Lt5AFa_aBKLsiin1j8UJQRURu9z5qK3NyPEnLpcSQF0U6xPHKvnBPHerOsFRXzKsrA2xLZHL27x9-F-8gTHdNhr_Ks9N98cjE5TKSZoncQIuBYVytXpGQrG5IVvLqv-YQrqnY3d73aPc_Pysvlaizoe6Nz-oyLKKK1uUZbayKp_S8IeumerSkkjXQ9zmsY-ZZ7NHcJViiOczus5vOVuUEpNFpZf6LckyaOO2MXvcw62-sv7epySGrk2FLRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpbS7HIGU3QmwoQZt7pDvYWzfoOBHOgxQMwLsmTGt7NYXqJ4AaQpbSGBsc3rMoqMg0g0l4KCq34mojAT9F6RN-ndzlxQIOmKBoNLxWN7AhxpIne_MJjwTQBoGXYgVMJ47xrl5bLEXlw0ULBnarjVaFrf3j4AB2t4MDcwJlVI_64i_-U-gq3nw7h3t6gU9Z9_ajHWw7e3NMZOOJx6eUnT-6l7bOahy22zs0f8xdDu3060kAV5pGG-fAQOlLIG6XaMjVkPoDm-emjVUuprAnHNnpwsVWi2t2MBwIu8eO8aKBVo9gP0RVJF4haSNd7YcDPEddwM_QkVK_m8tp4bsnd4ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🔳
رئيس مجلس الوزراء الكويتي يطلع على حجم الدمار في مطار الكويت الدولي بعد دكه بالصواريخ والمسيرات الإيرانية.
"امبه سنتكوم ليش چذي"</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76897" target="_blank">📅 17:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21001cb12f.mp4?token=lviEqLuOlyu6XdxaL1CHhI_jFR8XgHU52OCVIWEnWSibHr-ufn7PyIQnu3AKeoiwEOgXy4-RIdTJfIJbEDAPuNamkAmkozCerYzgaDcfQPDTJzUIsCKLuaoVdZrPilJOrDbf2xXCuutTpaUEqMKPecc5Dxlh7dTm5tgoHXrEAkPR8lUij7w9KJb3CF9DcD4k4FQ20nqE5Og7C5I3dqls6Nc5r7gL6K9ohszfrvuJAtZdi4ZCvModp73uLalt9y9jKjlAnzMXfUB6v0cXurqK7gC9G0cGA59uCbEIV8aHXVQRx4qFEx9eKfr4pvvB9DN8e9Nwap1SaWkrlv5S3lM744E2m-2Eyu2BOJXoyQnaggxQwRGuOTsCcf2vpkrFxNf_lFaYRJH5fdKyBLcEqDzJXZYVCq67uUxvuSKPKghJc73_5cQo5kauyovX2mvAkNEt4_rHL-ikPUo8-5ZxaclSx5slhfKC12B-kHOKvFhwlmT22CgrKMk_h6obZLuEHrWsITEmSnxFtzXQKZomkvWyrBq39FlxPq3aD-AP-LLlIWZVrHGDCVEebd2z2K1PkecI0tb6_u39hI-mtU_RXwvx3ev5BjZbo909-cRidZrhew0omYd_GkjIjCSlexs0c7Fx2C8LY9dk8drw7_d9ZELw1A5Xq3V4Crmz011EGZOHGrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21001cb12f.mp4?token=lviEqLuOlyu6XdxaL1CHhI_jFR8XgHU52OCVIWEnWSibHr-ufn7PyIQnu3AKeoiwEOgXy4-RIdTJfIJbEDAPuNamkAmkozCerYzgaDcfQPDTJzUIsCKLuaoVdZrPilJOrDbf2xXCuutTpaUEqMKPecc5Dxlh7dTm5tgoHXrEAkPR8lUij7w9KJb3CF9DcD4k4FQ20nqE5Og7C5I3dqls6Nc5r7gL6K9ohszfrvuJAtZdi4ZCvModp73uLalt9y9jKjlAnzMXfUB6v0cXurqK7gC9G0cGA59uCbEIV8aHXVQRx4qFEx9eKfr4pvvB9DN8e9Nwap1SaWkrlv5S3lM744E2m-2Eyu2BOJXoyQnaggxQwRGuOTsCcf2vpkrFxNf_lFaYRJH5fdKyBLcEqDzJXZYVCq67uUxvuSKPKghJc73_5cQo5kauyovX2mvAkNEt4_rHL-ikPUo8-5ZxaclSx5slhfKC12B-kHOKvFhwlmT22CgrKMk_h6obZLuEHrWsITEmSnxFtzXQKZomkvWyrBq39FlxPq3aD-AP-LLlIWZVrHGDCVEebd2z2K1PkecI0tb6_u39hI-mtU_RXwvx3ev5BjZbo909-cRidZrhew0omYd_GkjIjCSlexs0c7Fx2C8LY9dk8drw7_d9ZELw1A5Xq3V4Crmz011EGZOHGrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب لصحيفة نيويورك بوست: قلت لنتنياهو إنه "مجنون بحق".ويؤكد الشتائم في حديثه مع نتنياهو: لم أكن غاضبًا، لم أكن راضيًا، قلت لبيبي إنه يجب أن يوقف ما يحدث في لبنان.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76896" target="_blank">📅 17:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴‍☠️
‏
نتنياهو:
أنا وترامب نتفق على أنه لا ينبغي لإيران أن تحصل على سلاح نووي.
‏إيران لم توافق بعد على إخراج المواد النووية لكن توجد ضغوط متزايدة.
‏نترك الأمر لترمب بشأن التصعيد العسكري.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76895" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePqvOp-o8dD-PWQL7t3piDK5w_qsSMcdCC_R2YHdSXcTwtymje0QkiW644vtHEXBjJj3fwilX_JQnBZsBGU2miwpAN_ZFcrunFwGuYybdTPdGKGlhZ2lLuqjtbCUgBGkul40OV1_avKI6VcEyhL4IAgOlnaq_IxfWyDgYuoCOtbz6PpiCQWAxRrNRUuo5xsA2_Xl-SBhSFgYxSD1okkOzrOu1_DGR1dlCHH3hwyvLWPlbcKKzJjfUNyChrNbNHUietTrAv6HiI7DrkjC6YHLZYdp4iHoo2i0m2zZ4Wkt4pvE3LUB9Ktd2zycnse6Jljx4-_uTMyEdQjWdfikKl_VTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إندلاع حريق وإرتفاع اعمدة الدخان من المنطقة الصناعية في نتانيا شمال تل أبيب المحتلة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76894" target="_blank">📅 17:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7jNd7nutbAakxdrJwkKeIruaW-E8E30-ZgoYCkbFpurBKjGgBUVcpsoxZ91hDpoFMus0JV7f-R7ifVYty3idECFPg8E2JQG8wglssJkW4yu9Kg2QWxyIKmEDnf8eytbNXHQMimJbJxc4F4ECbVqrlWSGHVhCzb0oW0D2RUDt6HD-jd2Me1nSmcCZLW3O4Lk4VPnJ_mRXBs3ppulxWaUjqUGndGEUpBo7FnP9Vr-xmyD9TvXx_Y_0IJKjiw1-FSRNuXD9SLLDOHz5F0bjD79PmTgsouQmxIWQjctWuuZ7X03cyb3hygERy05mrZ-Hfl_z7kmG_iRt6B6Qs9XperMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
غارة صهيونية تستهدف بلدة زبقين بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76893" target="_blank">📅 17:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 01-06-2026 تجمّع لجنود جيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76892" target="_blank">📅 17:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔳
وزارة الخارجية الكويتية:
استدعت الكويت القائم بالأعمال الإيراني، وأعلنت دبلوماسيين اثنين غير مرغوب فيهما بسبب "الاعتداءات المستمرة".</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76891" target="_blank">📅 16:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🌟
الجيش البريطاني: ‏
مقتل 3 أشخاص في تحطم مروحية تابعة للبحرية البريطانية جنوب غربي إنجلترا.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76890" target="_blank">📅 16:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRkV2Ka0iy-aunp9gHq7W_14nBy8SO3pO-h_ja5ER4u-yYDmDjFbVRQJEewn5Lstg0tZ3yZOttMzcoPrr1eON_l6N73H34FmZxa-e7N9aKJyxlijPYY8pnWkga8CElWmjSj4FbaHL_XYkdQTboeHix0CDzvB2J1m8FKT2nD5z_Ya6XaqQJavpemMCrSpVuYhC-lln4ErucZvIcP2J-ROAsWZl_hn5qWuJem7k63vPx3m6cKkYsg8lnj1X1nMNcVBY2EKHH8we9EVr3gV6TH3zzK6TPe--jET-5e-1suqqmL6iOUCPQ-fvj78fsNh9uYg6ihPHx7EUhkKUMkDBAwwzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الاعلام الكوردي يتداول ترشيح اللاعب الدولي هوار ملا محمد مستشار رياضي لرئيس الوزراء العراقي.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/76889" target="_blank">📅 16:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
الانفجار الذي سُمع دويه في جزيرة قشم الإيرانية ناتج عن تفجير ذخائر حربية غير منفجرة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76888" target="_blank">📅 16:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
حزب الله:
تحليق استطلاعي ليلي بالتصوير الحراري لمحلّقة أبابيل الانقضاضيّة فوق قلعة الشقيف التاريخيّة ومحيطها جنوبيّ لبنان</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76887" target="_blank">📅 16:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz3TMNWYPsDDERx1AoVTbIL8bSuaOZEiuZILarWBGPAECk0kC49KZRFHlUuR2CQbFIqCudtYObPK5jOoTQ2PjLJa_XGsY9yCDg0RzOQhQWTC0042go_iDBM48YuViLbHdBjrd3uWZXQzJDAcaO0JfUeRFUWLU0MhtX-CTh2gDUhkULLNgNhkvuqiQLcMrpPdkdbW3CB96JxHDDT3yUawdbC8Pkv3Wj4SVPrgHMuaXm5d_1s6yrx8ExIJKosKeKXvcSkY3w6PRLxzvf2ZqYF2EoeTo4BSzMk-iolYG6rjl934cs3uzAJUDrDxE4lVxA26Hsr1B0p3uLjHFQOIsYe_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
المقاومة الاسلامية
حركة النجباء:
نؤكد أن موقف المقاومة الإسلامية حركة النجباء ثابت ولم ولن يتغير بخصوص السلاح المقدس المنضبط الذي وجد للدفاع عن عراق المقدسات وشعبه.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/76886" target="_blank">📅 15:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌟
رئاسة الوزراء العراقية تقرر تشكيل لجنة مشتركة تتولى وضع الآليات المناسبة لتنفيذ إجراءات فكّ الارتباط بالحشد الشعبي وحصر السلاح بيد الدولة خلال اليومين المقبلين.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76885" target="_blank">📅 15:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تنويه…
🌟
سيصدر بعد قليل بيان المقاومة الاسلامية العراقية حركة النجباء
.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76884" target="_blank">📅 15:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
الدفاع الكويتية
: تعاملنا مع ١٣ بالستي و ١٧ مسيرة قادمة من ايران .</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76883" target="_blank">📅 15:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad5f20ed9.mp4?token=RaFHHTRbAk01Gc_RHLJS3KF-z0OV9WDCgwQYeESe-6_9aBaFmfq2Eryb6jDzKP9BzrPXhibBAJ0kGq4bM06yBMW6pvaTgPFalfr-qZ0825OFlyNCT4eIN_fTl-PwVjA2mzQCYqAnuHYA7Fp8nIH6XD7ZPbZGe8O39G6_n1hLmTPkN1vtAZnCjEYvsCnLH2BgLlTKU-gbFajPaiwhzNgZ_RUAtMP-MBF465wRkjWbA-whbcTnzBu_rNOKm2VMdKLNbbR-vOuCnJnLbLIF4xZsQfTCVYDmm1reAhMqFcl36n0A7nu5wymdrWViYp6K9ooOx3DWCy8chgUBUpqIB444nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad5f20ed9.mp4?token=RaFHHTRbAk01Gc_RHLJS3KF-z0OV9WDCgwQYeESe-6_9aBaFmfq2Eryb6jDzKP9BzrPXhibBAJ0kGq4bM06yBMW6pvaTgPFalfr-qZ0825OFlyNCT4eIN_fTl-PwVjA2mzQCYqAnuHYA7Fp8nIH6XD7ZPbZGe8O39G6_n1hLmTPkN1vtAZnCjEYvsCnLH2BgLlTKU-gbFajPaiwhzNgZ_RUAtMP-MBF465wRkjWbA-whbcTnzBu_rNOKm2VMdKLNbbR-vOuCnJnLbLIF4xZsQfTCVYDmm1reAhMqFcl36n0A7nu5wymdrWViYp6K9ooOx3DWCy8chgUBUpqIB444nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
سُمِع دوي انفجار عنيف في قضاء جومان بمحافظة أربيل شمالي العراق، أعقبه تصاعد أعمدة الدخان من موقع الانفجار.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76881" target="_blank">📅 15:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
🇮🇷
المجلس الأعلى الإسلامي العراقي يطالب بتشييع جثمان الإمام الخامنئي (قده) في العراق .</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/76880" target="_blank">📅 15:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3070c474.mp4?token=pUTntlF2arvm7bKFGTYSuFQWmdb8EG3EK6BuqhObFxQkdSZG6PhOTC-5AVULyB2p-aD2SXopAH5cAg_DrTJs8767nt0D2zReO41bfFBfhpIXW5-qcvXdc552wDrMo0xJGrDiLd6obkf-zcE9ZMAhE-J4TW9I9xoa6Iqn5H-o7FRz2f96R1PC-tol3c2LZoYZ4F6_ax6_6vv_3Km9kpi2vybzraLrQFfuTMyvLAQqeEW7Moz5s94v6OTYBMdg78-vDBk7Qox6hVcem9t1nMY198KGvEAXDSqT8_6AWgUkgqTecK159bLy-O7DHXQGYdUnNnDgorUHluAz9QdPCQlO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3070c474.mp4?token=pUTntlF2arvm7bKFGTYSuFQWmdb8EG3EK6BuqhObFxQkdSZG6PhOTC-5AVULyB2p-aD2SXopAH5cAg_DrTJs8767nt0D2zReO41bfFBfhpIXW5-qcvXdc552wDrMo0xJGrDiLd6obkf-zcE9ZMAhE-J4TW9I9xoa6Iqn5H-o7FRz2f96R1PC-tol3c2LZoYZ4F6_ax6_6vv_3Km9kpi2vybzraLrQFfuTMyvLAQqeEW7Moz5s94v6OTYBMdg78-vDBk7Qox6hVcem9t1nMY198KGvEAXDSqT8_6AWgUkgqTecK159bLy-O7DHXQGYdUnNnDgorUHluAz9QdPCQlO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
شرطة أربيل في شمال العراق تعتقل شخصاً بعد قيامه بنفخ بوق يُصدر صوتاً مشابهاً لصوت المسيّرات الإيرانية.
كاكا هاي صوت مسيرة من باب شرجي
😆</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76879" target="_blank">📅 14:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76878">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDSKs7tlhM-KjVnGsOIjD_rpkeSEbsv39d5ELj0fYVpKb6i1yGE5DCqDdlY3CbhWgG1SzEteBqJxMqD1qsp_mjEh8izhDl9HlArbdoDCLlqu7igw7TGkGFIL253G7dfN8IvetI8G2shpohUsArNHNOmdWNitffoT6jb_ZNgnSWBjtqj7yHz98ZjNEMohqFitni2fYCSwUHVfF54dtAaDeTTiy9iaDLrqjgEvdkwZLHZ4LSEQrhpHeJ9iFvGDw3CQvg5aN8J60xPas9r-j9IFMd90xlSiyFTIX-FCcGFEH8bKUBp1011Z5V3ny2UrFt38phDfSptz8jRxiY3a-8U7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
الجيش البريطاني يعلن عن مقتل أحد أفراده  في شمال العراق خلال حادث تدريبي (حسب وصفهم).</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76878" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
الصحة الكويتية:
إجراء 7 عمليات جراحية كبرى عاجلة بعد الهجوم الإيراني، واستقبلنا 63 مصابا.
لا لا
يابة سنتكوم تعترضهن كلهن
😫</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76877" target="_blank">📅 14:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
الانفجار الذي سُمع دويه في جزيرة قشم الإيرانية ناتج عن تفجير ذخائر حربية غير منفجرة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76875" target="_blank">📅 14:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1c8f3530.mp4?token=uOwrUvaekUYOcbciq7Ml13FNB1FvEb07rS-j7NFI23ys0ARPV9Gv5DkHtYPkwsMPpC_35Akva6_PD9YDgYnlh9u-QL6QEfrduB8sSiBIcQOpHzUxPz1FfK6x5FWt9szx2XuE_QB7-O92zukfoxI55NCIvsXtAeBw7rAZhXpkhVOGDgV0_XLFpL7pT7X2jyi-zfa-KA96eKUiMUp2VEx6J5b_5Uy7PxPktFV7IA4Eq7dY6OuDVInn7m1l7WMOXx5p22qwoaSuwiqNlC-Bvk7YmTdZU0k3xakXhmYkYPaHveaTo0IBX_7bAyZu6avmQSGR9VFSyju6Q4FHbH_lYWV_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1c8f3530.mp4?token=uOwrUvaekUYOcbciq7Ml13FNB1FvEb07rS-j7NFI23ys0ARPV9Gv5DkHtYPkwsMPpC_35Akva6_PD9YDgYnlh9u-QL6QEfrduB8sSiBIcQOpHzUxPz1FfK6x5FWt9szx2XuE_QB7-O92zukfoxI55NCIvsXtAeBw7rAZhXpkhVOGDgV0_XLFpL7pT7X2jyi-zfa-KA96eKUiMUp2VEx6J5b_5Uy7PxPktFV7IA4Eq7dY6OuDVInn7m1l7WMOXx5p22qwoaSuwiqNlC-Bvk7YmTdZU0k3xakXhmYkYPaHveaTo0IBX_7bAyZu6avmQSGR9VFSyju6Q4FHbH_lYWV_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
ترامب لنتنياهو في مكالمته الهاتفية:أنت مجنون تمامًا. كنت ستكون في السجن لولاي. أنا أنقذك من الكارثة. الجميع يكرهك الآن. الجميع يكره إسرائيل بسبب هذا.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/76874" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2702a18eac.mp4?token=AnrTSN5t5fPoEiV6GX9y3T-EOLQJ5E3pRu9FSoAlBYpUnHMRqcdgdNDLTuTc8VHHO54gcsGhYd4Zwc8OiZ-psOkgG6XtlCjhgv-ERjz9-oZ_nHhrVZmCclUvhGh7M8Nl6F5hW000JBbbl99ahtcYvNdLwiOECqM2rGoxptZbDUzRrCn4gUNF-RTrJGSyllJ9HYO0EfBg1ZlMNp-_zbRsS5FqCd1LDhoQ1LZ2GqyNCHzU-Htdkc9I-AhMb0AKcADQFg_AfOHJKBZGznmYd7wkNDlyZNp9fiet95IpKa5qIH9r_MeS2TT9ghnbsNkT4IeEDlhWmefKTFontsIOAGhUAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2702a18eac.mp4?token=AnrTSN5t5fPoEiV6GX9y3T-EOLQJ5E3pRu9FSoAlBYpUnHMRqcdgdNDLTuTc8VHHO54gcsGhYd4Zwc8OiZ-psOkgG6XtlCjhgv-ERjz9-oZ_nHhrVZmCclUvhGh7M8Nl6F5hW000JBbbl99ahtcYvNdLwiOECqM2rGoxptZbDUzRrCn4gUNF-RTrJGSyllJ9HYO0EfBg1ZlMNp-_zbRsS5FqCd1LDhoQ1LZ2GqyNCHzU-Htdkc9I-AhMb0AKcADQFg_AfOHJKBZGznmYd7wkNDlyZNp9fiet95IpKa5qIH9r_MeS2TT9ghnbsNkT4IeEDlhWmefKTFontsIOAGhUAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
ترمب
: مجتبى خامنئي منخرط بالمفاوضات معنا وقد ألتقيه في وقت ما، وإيران وافقت على عدم امتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/76873" target="_blank">📅 13:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ie5bUmQTBNrqO7jF163CznR4vi7wv0RRQtAABXh23ZBD2IvpsU5-XNV-Cx6_lRQjgPgMedtqQqx_xFdEU51wRPqf8guKiLLTI3SWSss7aSJL0za2upODStETpgswlepE35X--n5U8v5ZSbhlCALCZPLGVKfodnYMSqRQ3xq7pGk0SQBUf47hEzVbTexgzbIGj4ejaGHfDptRVkcq57S6cFQjOX6ARd-Cp8fl3RAo6DoXFg6HYiZl3uycbtZwx0KvnRRaMk3wP3m8iQxrQvz_TwqqL8A16DqYR_wITT8dz3PRjKaK6cB2zgUCX50H-p_uGi16ZBo6kIKyZh51tt5x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
نفى المكتب الإعلامي للحاج هادي العامري بشكل قاطع الأنباء المتداولة بشأن تشكيل لجنة برئاسته لمتابعة ملف نزع السلاح.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/76872" target="_blank">📅 13:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61caaee40f.mp4?token=GUtCBX1LCGxVwm0VkSh8ReVkaUfm4DRbK637K0u4c7u1k1RGtHdw4RjnvM42sHEWjudUbvZzsaxcxP2eneg7pxIh_b6K78TPt6mqgnf7cYVJ3Ft9FTAmiC2knUocrJ2Zyl1lfp24NtY62NWN--W02Ck1Tjnho2QzvLuIm26LuenmG0lJX70fnHc04c5LMaLGxDPRm-QAlibjswQv0ZMHBGQGM2i9TReyx2GXLIXAId-bUF0ME_eoqGUr-9BvrTZMVjuwjxxRtCY5TJHM7u7f9NTq-Hm3tCAQURlohC6IomjAy-8YhPq6b9Og3B5avyakUp-62Sdf08QSqQP-TpZ8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61caaee40f.mp4?token=GUtCBX1LCGxVwm0VkSh8ReVkaUfm4DRbK637K0u4c7u1k1RGtHdw4RjnvM42sHEWjudUbvZzsaxcxP2eneg7pxIh_b6K78TPt6mqgnf7cYVJ3Ft9FTAmiC2knUocrJ2Zyl1lfp24NtY62NWN--W02Ck1Tjnho2QzvLuIm26LuenmG0lJX70fnHc04c5LMaLGxDPRm-QAlibjswQv0ZMHBGQGM2i9TReyx2GXLIXAId-bUF0ME_eoqGUr-9BvrTZMVjuwjxxRtCY5TJHM7u7f9NTq-Hm3tCAQURlohC6IomjAy-8YhPq6b9Og3B5avyakUp-62Sdf08QSqQP-TpZ8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حالة من الهلع بين المستوطنين في كريات شمونة، عقب انقضاض مسيّرة تابعة لحزب الله على مواقع عسكرية قريبة من المنطقة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76871" target="_blank">📅 13:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951231e9f2.mp4?token=HBUacnbFBEVDYudBVqawVhcyVEDrincEcdpTu4cRlQNc1e15voGlkW3PyAO_YxpPrqjgQcFHxUQiohM9Yi9kCmxjeYc3_4dq4UugGf2NObxqM95-Rn7-4MeBo-y8d1BP4iFUcWib4TdDthXl70eu9NdzjVvjKAgvGit6j_RUJbJB5u_nRndDClwMAOuaHevLliJHNLu0-g8d-A3-E6R78Dr6PK63-AZo2I9Lu5f875peDjLG9FQR-2y-1aZg0udzx6wEsE7YNpJvwNLg3Uc3OUdPBpSHQ9OSO9KHfMmI00w7-_kbSpptMg1GVoCB0VKvuEB_XbbF6OUsFdcfaPQEDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951231e9f2.mp4?token=HBUacnbFBEVDYudBVqawVhcyVEDrincEcdpTu4cRlQNc1e15voGlkW3PyAO_YxpPrqjgQcFHxUQiohM9Yi9kCmxjeYc3_4dq4UugGf2NObxqM95-Rn7-4MeBo-y8d1BP4iFUcWib4TdDthXl70eu9NdzjVvjKAgvGit6j_RUJbJB5u_nRndDClwMAOuaHevLliJHNLu0-g8d-A3-E6R78Dr6PK63-AZo2I9Lu5f875peDjLG9FQR-2y-1aZg0udzx6wEsE7YNpJvwNLg3Uc3OUdPBpSHQ9OSO9KHfMmI00w7-_kbSpptMg1GVoCB0VKvuEB_XbbF6OUsFdcfaPQEDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجزت فرق الدفاع المدني من اطفاء الحرائق المندلعة في مطار الكويت بعد امطارهه بعدة مسيرات ايرانية ليلة البارحة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/76869" target="_blank">📅 13:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇯🇴
حكومة البندورة الأردنية تعلن تضامنها مع الكويت والبحرين وتدين اعتداءات إيران
😆</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76868" target="_blank">📅 12:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇰🇼
هيئة الطيران المدني بالكويت: استهداف مبنى ركاب بمطار الكويت بمسيرات وصواريخ إيرانية وتفعيل خطة الطوارئ  استهداف مطار الكويت أسفر عن إصابات وأضرار جسيمة في عدد من مرافقه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76867" target="_blank">📅 12:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 24-05-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بصلياتٍ صاروخية وقذائف المدفعية ومسيّراتٍ انقضاضيّة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76866" target="_blank">📅 12:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76864">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇰🇼
الخارجية الكويتية: مقتل شخص وإصابة آخرين في استهداف مطار الكويت
‏اعتداء إيران أسفر عن أضرار بالمنشآت الحيوية بما فيها بعثات دبلوماسية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76864" target="_blank">📅 12:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76863">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d40ecfec.mp4?token=oc-IeE05LIr5D18QEhCnOKKiW0VDbu13gUjWaqNlygb8V_2SqNYQOB-EPmyEt_xB5Asy79vq7KhmEjbVWRupWpLRv7fIyxwBVDqLMG_OGzfF7ruD-PVsqOT3xrn_k8sDqzLCHknLhks75Zs2M1EyhNlS1KrqTb-D5iX2eTsbwBasge8Tj14qav53FeeoG-JXAi9IVu9l9ZCKubPHCDAq-jJU7RSdoNku6n9EqQhsL8G2ZbolggFhudBaRUgEX52sgNVroce75a_kMlS8k5NqosBYrdvMoGHp1MKrUVW5fZkB5bsYKJANPAwmJtdX1sxi4kqFX_AkE1c-dG2gZgbPUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d40ecfec.mp4?token=oc-IeE05LIr5D18QEhCnOKKiW0VDbu13gUjWaqNlygb8V_2SqNYQOB-EPmyEt_xB5Asy79vq7KhmEjbVWRupWpLRv7fIyxwBVDqLMG_OGzfF7ruD-PVsqOT3xrn_k8sDqzLCHknLhks75Zs2M1EyhNlS1KrqTb-D5iX2eTsbwBasge8Tj14qav53FeeoG-JXAi9IVu9l9ZCKubPHCDAq-jJU7RSdoNku6n9EqQhsL8G2ZbolggFhudBaRUgEX52sgNVroce75a_kMlS8k5NqosBYrdvMoGHp1MKrUVW5fZkB5bsYKJANPAwmJtdX1sxi4kqFX_AkE1c-dG2gZgbPUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المتحدث باسم كتائب سيد الشهداء الشيخ كاظم الفرطوسي :
تسليم السلاح من اجل الحصول على وزارة هو خيانة .</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76863" target="_blank">📅 12:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0a748bed.mp4?token=nI8bBQamzpR0JlgF9EMxNvKM2DMbced9MzRst1zzg9ehsC0PyyxOt0hkQLXIezfKi9I8UagR46aIPvaWj9msUHltzZLd0HA1vmRwPRTd8vyWw8DRCclvahDSNMxzZoSzYqMyCFOR1bFjMyqsgRgpjxjNcm-EQgqQRq0c8WCOgWi68NYGgKC0Q-IhmiTY5XCxBBYHCMOdR-sYcK5T8NdqPb5tWLohd7XGfo0YvUENJMYg7wIhCmqBdKGHL02eed1UKzzkx20fQFaQJSzZ6Yxsus_uBSOIWfdawOoakw0P9iIMKQDSwZYzBNFODCcMp1OuV61srLgGqjMEQoGVUpk1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0a748bed.mp4?token=nI8bBQamzpR0JlgF9EMxNvKM2DMbced9MzRst1zzg9ehsC0PyyxOt0hkQLXIezfKi9I8UagR46aIPvaWj9msUHltzZLd0HA1vmRwPRTd8vyWw8DRCclvahDSNMxzZoSzYqMyCFOR1bFjMyqsgRgpjxjNcm-EQgqQRq0c8WCOgWi68NYGgKC0Q-IhmiTY5XCxBBYHCMOdR-sYcK5T8NdqPb5tWLohd7XGfo0YvUENJMYg7wIhCmqBdKGHL02eed1UKzzkx20fQFaQJSzZ6Yxsus_uBSOIWfdawOoakw0P9iIMKQDSwZYzBNFODCcMp1OuV61srLgGqjMEQoGVUpk1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد من انطلاق المستوطنين إلى الملاجئ بعد وصول مسيرات وصواريخ حزب الله إلى المطلة شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76862" target="_blank">📅 12:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76861">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن رئيس الأركان السابق: لقد أرسلوا جنودنا إلى لبنان كقطيع من البط إلى ميدان الرماية
😆</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/76861" target="_blank">📅 11:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a04a5b1d9b.mp4?token=WkpmxzYmHOv4HMhBCSDzyuCQPUtTSdSlV1aBZGwbsE6LR8xP1DypD4T1LPB9zzqIgvnXSQ53Bh7-YBcooEFrQyHPSfvMJCvcFrl1QGSI6hLJsFmg33ElfmyCfOD3zjX06nm4T6hwV-nTaSW9jAY2qqUBWq91cSh6QI3HgW4luxzi2U5zPFM-8wE3Ger4oRK6z3hOekY9MjbIIhpGc2R49z9TACk1PwezpMaW8uhByDtrtkqzLXBktAr82gZHNkVXVxw3Cce0uar-emKjZ5j9mjsEnsLRYYe28jMfY-xtfoIRCkehPKSC8vHplTcE05iiHFDwN2_jKT9IyusSVsKYUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a04a5b1d9b.mp4?token=WkpmxzYmHOv4HMhBCSDzyuCQPUtTSdSlV1aBZGwbsE6LR8xP1DypD4T1LPB9zzqIgvnXSQ53Bh7-YBcooEFrQyHPSfvMJCvcFrl1QGSI6hLJsFmg33ElfmyCfOD3zjX06nm4T6hwV-nTaSW9jAY2qqUBWq91cSh6QI3HgW4luxzi2U5zPFM-8wE3Ger4oRK6z3hOekY9MjbIIhpGc2R49z9TACk1PwezpMaW8uhByDtrtkqzLXBktAr82gZHNkVXVxw3Cce0uar-emKjZ5j9mjsEnsLRYYe28jMfY-xtfoIRCkehPKSC8vHplTcE05iiHFDwN2_jKT9IyusSVsKYUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
استهداف صهيوني على طريق صيدا بيروت</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76860" target="_blank">📅 11:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇰🇼
مشاهد متداولة لمطار الكويت الدولي بعد دكه بالصواريخ والمسيرات الإيرانية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76859" target="_blank">📅 11:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9C8ReosdG1IFiUdtOZwMPcmUkkHOtYAPzeONnbBYzGnS-7s0ynxKe_4wVGEcpQYbLhaS68ZkrnxoAdAZpqp1UwQKhWquvblfc6HdEeK5OU-TwVPfwve9Uvdlc5clQJ4qKCw2exonWUpfyQVATKn7NBxzy1INzRAP3wN5s-n8-F0Fm4cXcsqGDZgKMkbTqha6XCLAQRTgN8WdQmYlRHpsQb5gxqa_jqM2Dyg6DbIqMZ6lcbrA9ul4-6dT5l9ifo9-s9FPFl-SZxxHYbJ0ZCmFId5VJ0t5glsZ8HEfWEYf4qAkis9xu9XtkKWvy99Zs5SneiQKcw8VTK7D7eJynEpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
صورة تظهر الأضرار الكبيرة في مطار الكويت الدولي التي أُبلغ عنها بعد تعرضه لضربة من طائرات مسيرة إيرانية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76858" target="_blank">📅 10:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76855">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fu--B_8qOznzV0xwBCSyVkqFnwR3BOWcQOWD6lH8kvUZK-cjs_sSl3uamhNuaW2gjDayTMjx7FisOPoRA8U9ZBTqXpttJHOYJgKEqcbM3aA64d4gIVHPfYMXuUTqkI62u7nQWIl1res1xX0MVpLl2pMQeFKWOL9Y9PeBHrKgKRlt8UvAMMLH7FfpxNtkkZyXF1J4dWuyTUas8khEG9sxkLRZkbgw0VZfGRpeYt7s03ZmsyjlgdUVrq3Bq4KrVdV9fGFdq3L9LF4lgWySP5Sp4czBr--xzE4AQ9ae4HAT_7VIyupqjTMkfMLcKJN7z75JBXt6dto-XYSxLZWJL0rLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdEGF3YnFDHuksbL3mOIo_oI7NSfGAuc-jImAylCAjzHxQjbk9io2h0y-1pGwqu4c_94tlcXaApMDIaPPGJ9-PZKvF0jArNCqkHfttHRrwmDqvDn9K9alTwW1tr-fW5Cm6L4-n3fY6T73dpWtdS3m00JgHcVJUATyy69y-xt4QTEoOLNTT_XS95hfNNlMW_2sKsaZUCqxr4KfcRft-EM5Q3hOUWlJGSw2y8fMb3bHv3bey87ms9yKxusqK_fbn_RdGx5Ap36NwCP8L9Kynwp61bOIm7Svhla9osWXksF4ACv21EvPCHFejLJsSZXjAtQ2kC5XE6O3ifwraCh1BfaJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b244cd39.mp4?token=KtLIUs-Fq2rcmp0BcIPIm7gsvRSeroCNNupyzWp4lhjtZzgGEa1SyqC1PeeMlwoA47h_zDHSCFqONackRokSL-PGNJpJW66I5ifmMj5MuX2CncmDy8dlwtkdZ-Keh0n3yXE6ctpRSg5EXWMPxdcVAxS60whyS97wdl5FqWxlobm30cuzqkhsODwZxd88B04vr9RW_N_jzmkKp-mHgs8zpUnVnLsf3_vHCQcCUc4T61wFVpfrU72BQ_Ntaj6y4cbid5f4sRbAV3kQZ9m0yjw3bRbc2877lL5VsjgZHxn4HbXYhUoVb2iC23xMnoyk0bQpyrzoL_sQItG5RehaV3hdRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b244cd39.mp4?token=KtLIUs-Fq2rcmp0BcIPIm7gsvRSeroCNNupyzWp4lhjtZzgGEa1SyqC1PeeMlwoA47h_zDHSCFqONackRokSL-PGNJpJW66I5ifmMj5MuX2CncmDy8dlwtkdZ-Keh0n3yXE6ctpRSg5EXWMPxdcVAxS60whyS97wdl5FqWxlobm30cuzqkhsODwZxd88B04vr9RW_N_jzmkKp-mHgs8zpUnVnLsf3_vHCQcCUc4T61wFVpfrU72BQ_Ntaj6y4cbid5f4sRbAV3kQZ9m0yjw3bRbc2877lL5VsjgZHxn4HbXYhUoVb2iC23xMnoyk0bQpyrzoL_sQItG5RehaV3hdRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇼
هيئة الطيران المدني بالكويت: استهداف مبنى ركاب بمطار الكويت بمسيرات وصواريخ إيرانية وتفعيل خطة الطوارئ  استهداف مطار الكويت أسفر عن إصابات وأضرار جسيمة في عدد من مرافقه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/76855" target="_blank">📅 10:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76854">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇧🇭
قوة دفاع البحرين: استهدفنا ب 3 صواريخ وعدد من المسيرات الإيرانية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/76854" target="_blank">📅 10:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNvRpf-a96gxUFS-zof1Szo1QKHovLxgZQQnDccs80x9dgc0bJ27el6dOUOsp0bf3dt7wDYNlIQdVKl1P1VVm8MJa4U4G4L99YS2MIkdJ8QFRWDwpFucVRNz3_-EzFy-Z6ZUABooXszC0GU0VCI36oMwFjroCeoFFfn62EcJfk4_h_bhGdVheKXrvnW08pzLBU3ehdd4THHKx9irD2cbp5J8tCNfXtf032GbFKiiojuov2SVBjRyW-pTOifxs32dsve3tYa3GUwSYqhc3Sb3_96gZBBcxvEtmPYqLxAlUiGyQMR-feaFpQyu-RlJK-rGiY4YcEgVa_kTNN5ixGUarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السلطات البحرينية تعتقل عدد من الشخصيات الشيعية في البحرين وذلك رداً على الهجوم الإيراني على المصالح الأمريكية على أراضي البحرين.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/76853" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpH0lgx49nOXW2dDiKyrUS9A_7-alj0iSTMZxpnKr-9mzpZb0-PFzGB2PlXBSUjSyT84MTwJuJYebBpiUDncTyXWF14cWYo-1uvTQHIGM0g1I5e_6UJ_lpYKjy67iGF3W-Yc0BtjupI2yELs65xkMb4tsVp5jCq2Dt9_WpbmUSPEf4rdNf91hTyuBpswurAG3lda31XvJJdaRq6SoR9ihRnqdEkZqjDUB9ZBBZ9aeY5V9Rg16oj1pDaTkdIEO3uiXEhbTWACaDgyWjgCvvExwHI245IRP803v5uROsSoKDOcE29QJWPNpHo6PzOhb8PpOxAUpLMV8ye18J-LnaJ_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة أقلعت من تل أبيب تطلق نداء الاستغاثة وبدأت بالهبوط متجهةً نحو Belgrade.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76852" target="_blank">📅 09:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇰🇼
🇦🇪
الكويت والإمارات تغلق مجالها الجوي أمام حركة الطيران.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/76851" target="_blank">📅 09:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇰🇼
🇦🇪
الكويت والإمارات تغلق مجالها الجوي أمام حركة الطيران.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/76850" target="_blank">📅 08:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGGUhfKOLe4rAttD78K0oFbHg4ee7ABIEVZV8wQjPBGrK0hz9mlJQWp_U7tW_3Lwp_9flYg75nm1UQiBrX5DhoWK6hwiKQ0zHFnG9gMRei7Svqf0PzcJdLsAq7A_WG0tHGz0HZbfoOfCunUfy-kxqT333UPl24bQgx5JKk3k1Kdb0l3YPNnR1A-SywofT7mQiCXbNA2LIYmMGLd9-L__6nT6LAbj1Q9uQTrO8sc9x7qefN_qLbf_FCz0jitz7kBzepQz1xKmi41MWAhbBvIRYUqDhywLuFFFMVWU0A202CRkWaahme0_IfFjVcm-guREtd0LIT_Tb_KmehZW1Z5tDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🏴‍☠️
طائرة التزويد بالوقود الأمريكية أقلعت من تل أبيب وتحلق الآن فوق الخليج الفارسي.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76849" target="_blank">📅 08:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">إطلاق صفارات الإنذار في البحرين.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76848" target="_blank">📅 08:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">إطلاق صفارات الإنذار في البحرين.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/76847" target="_blank">📅 08:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76846">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b904ffec5.mp4?token=GC0OgVMNT2GKtrUR713tA9CQqIdhC4fp22MOGs2fLk66BNp7rHZpWYrd0bLCbSwa3zvMlGTN55IgZBgh9-skdyuh7Y-c3obVPe364xCV2X2mHZgmDPcNDBpr7EpOVnZ3eUaCNYwx50QOBRtvUTaffnp2FPPOX41aAY0xpRhkZ5R-boicK7dc9yfDBQaAO2-ZIkJuqr5nstYsLey7ucHL4SHCyUjZygauIDp0w6vpCQOhXkdKqlejHlo6MTyTBwkjoYvYrUx0WBgF-W-uznzYyPX1T8ejtssuVyIgdfHuQwAUr2Sn52QReCOoqKG8Iv9uc0y-SkOcnpqxeIcTc7wmOw0CPIKqNtcbmNAaFERUQq0s3sz06zWxoF2ciacseNRZcb6iTWnc2LHSNGq9StCwj_KeRCZNKbE_eTYiytViDRZ_U9lkFZSUA6cgHd721CiuLX1-nPVCdMOSlQuijWzvcC8KMi6dEVyWikncMq-238NZ-ipb7qh1v6NFBYVnuXGDa_4p9-Moi3ghkW8qAMSkNec18mkYkrNO2yeEDkCTBLdahL1Nri1NRhsZg1F9JtAa1RX7qE7NdE0I5XWG14hwgC6iXoMI2bSaQDuY-vf2mKrB-qvp_0cSG_Sdzbm-DNxIgwcphuVjkyBEvZVHDzT2i72ZrPDBmQYoaeJTfxwiGWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b904ffec5.mp4?token=GC0OgVMNT2GKtrUR713tA9CQqIdhC4fp22MOGs2fLk66BNp7rHZpWYrd0bLCbSwa3zvMlGTN55IgZBgh9-skdyuh7Y-c3obVPe364xCV2X2mHZgmDPcNDBpr7EpOVnZ3eUaCNYwx50QOBRtvUTaffnp2FPPOX41aAY0xpRhkZ5R-boicK7dc9yfDBQaAO2-ZIkJuqr5nstYsLey7ucHL4SHCyUjZygauIDp0w6vpCQOhXkdKqlejHlo6MTyTBwkjoYvYrUx0WBgF-W-uznzYyPX1T8ejtssuVyIgdfHuQwAUr2Sn52QReCOoqKG8Iv9uc0y-SkOcnpqxeIcTc7wmOw0CPIKqNtcbmNAaFERUQq0s3sz06zWxoF2ciacseNRZcb6iTWnc2LHSNGq9StCwj_KeRCZNKbE_eTYiytViDRZ_U9lkFZSUA6cgHd721CiuLX1-nPVCdMOSlQuijWzvcC8KMi6dEVyWikncMq-238NZ-ipb7qh1v6NFBYVnuXGDa_4p9-Moi3ghkW8qAMSkNec18mkYkrNO2yeEDkCTBLdahL1Nri1NRhsZg1F9JtAa1RX7qE7NdE0I5XWG14hwgC6iXoMI2bSaQDuY-vf2mKrB-qvp_0cSG_Sdzbm-DNxIgwcphuVjkyBEvZVHDzT2i72ZrPDBmQYoaeJTfxwiGWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
الإنفجار الذي سمع دويه في العاصمة الإيرانية طهران، ناتج عن انفجار "خزان غاز سيارة" بإحدى محطات الوقود ولايوجد هناك حادث أمني.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/76846" target="_blank">📅 07:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd089958f6.mp4?token=GEQOIUPLJjtJSzVFGnd5WUBGlU24gI1unXoPHw9FAdCgVconrx1inGuDdQSzUS5Mde3vczTMQH3_UPmgWMLeTE9UZUADQxM4fGl4BIIojrnAOZQCtLi2TdTk-8O7ljzif5PiCQnYjT_a0kHMMtsoDz_AO5Zi908mOBIcfnlyNnKGyL9urcXfjrggTtj3tDybxP_sz2QKfTz0CS2yxd_1sa9uJ00PKp7f9eu9QsoU7PJIn4Z6mjP4Yzy0NIl5-hOmlL3aOIixpr_2CMlowVt0OcKjnOU_ufqDN0PabWx5o-044Wnqp2YIT7f1hAc_rDehgiqmhSQgRvQVTNiI-Kpbzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd089958f6.mp4?token=GEQOIUPLJjtJSzVFGnd5WUBGlU24gI1unXoPHw9FAdCgVconrx1inGuDdQSzUS5Mde3vczTMQH3_UPmgWMLeTE9UZUADQxM4fGl4BIIojrnAOZQCtLi2TdTk-8O7ljzif5PiCQnYjT_a0kHMMtsoDz_AO5Zi908mOBIcfnlyNnKGyL9urcXfjrggTtj3tDybxP_sz2QKfTz0CS2yxd_1sa9uJ00PKp7f9eu9QsoU7PJIn4Z6mjP4Yzy0NIl5-hOmlL3aOIixpr_2CMlowVt0OcKjnOU_ufqDN0PabWx5o-044Wnqp2YIT7f1hAc_rDehgiqmhSQgRvQVTNiI-Kpbzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
هجوم أوكراني على مصافي النفط في مدينة سانت بطرسبرغ الروسية.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/76845" target="_blank">📅 07:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76844">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇯🇵
‏
اليابان
: ميزانية إضافية بقيمة 19 مليار دولار لمواجهة تداعيات حرب إيران.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/76844" target="_blank">📅 06:47 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

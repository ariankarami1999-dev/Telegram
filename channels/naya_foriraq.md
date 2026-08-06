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
<img src="https://cdn4.telesco.pe/file/bpdICK3Vn72c9XrO51ro5gZI_SDxzBcsvfIsb_aZsNM1pJkXoZa_Zuma_NzyfF_dfaGlQuLSQOJUY3EHR_RSECY43tjUM53j0Z5Tt6Y3A65AvIbLPgGuYenmJCj7HKW03B3rK_CqVLeCZcgu-JjDjxFE9JvZ8LgYrEdsjPwYzTsWVDWZvOlvste4zMe76-iDXGwB3G2S8BPKLVlhINi9O6e-9xdWzUqtwEVoOJOQXnZioYjilJfR4EovTphuIalVAs-lEjkwu-M98weAi_y_XodsRhGnbePNI7kCmKjIFzb98ZH85vT92rZbolRW-ait7B8SeHjr5PeWYR3Latix4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 08:27:30</div>
<hr>

<div class="tg-post" id="msg-87081">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏ترامب: نقوم ببناء أكبر عدد من مصانع الذخائر في تاريخ الولايات المتحدة
‏سنصدر أحكاما بالسجن بحق مسربي التصريحات "الخائنة"</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/naya_foriraq/87081" target="_blank">📅 08:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87080">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
حدث أمني في حي بارك تساميريت بتل أبيب</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/naya_foriraq/87080" target="_blank">📅 07:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87079">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇱
حدث أمني في حي بارك تساميريت بتل أبيب</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/naya_foriraq/87079" target="_blank">📅 07:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87078">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb71ce607.mp4?token=BHjOsO-FXy1M9FrkV9ArxDlnl4pVOr6057Ep9tud-ul3B5ZJJFOgfcMp40aY04S7iD-BFo7OoFi7Gh81VWizEO9pzobe6-WagEtouvuHxiQ7WrYW9b69M6TKAFQUXiIR6m-wBYuRUuwCqGQFh8J39VvwuCJ8Ukd0aHWqcZ8ai2g9A-qVo00Ounx80CQRLyj0QLVqJ7bQkcHQYTTeYw6G9vk99eWioOdWdajIjj5Wn9WIlbmXjDJDDdFOzQ8L_OGFwNyKaagkdpxDW-FYfjj3lommGycEUGw9LxK37UG9NSmNK4yXKzEXraDw-fn9slT8m1K4mEVxC5_qY2716KXX5rvky30fLgegrn09cLRfqI56_hZ-If_YIk3uVfzaV4RSFpppalTAbStgjUD1zC8EGThSUQcwHMQXEZa9QciYHIv2W4TIpCj_iiPcV0-iihc9Y4Nb8HYlYIZhrB66063FZ4WSOthHT_7STivQQATz9NzKVDHrhX3ppcFfiapPjaSdBCN6abwOmuZSCj82eU5S6Dn1UDqY4-tStPufP3DCwt_8mtJZ3o-zRT3hLnSiA1RpvPi7f7X3L_A4z6m5I86oDhpjEB19EnNOcOwJpgzh1zP3SuRTujhPo28axCu54T8luidWwtrkFIfp6A0bY6JrUnC6uV2I2uJclOi89ZOoS5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb71ce607.mp4?token=BHjOsO-FXy1M9FrkV9ArxDlnl4pVOr6057Ep9tud-ul3B5ZJJFOgfcMp40aY04S7iD-BFo7OoFi7Gh81VWizEO9pzobe6-WagEtouvuHxiQ7WrYW9b69M6TKAFQUXiIR6m-wBYuRUuwCqGQFh8J39VvwuCJ8Ukd0aHWqcZ8ai2g9A-qVo00Ounx80CQRLyj0QLVqJ7bQkcHQYTTeYw6G9vk99eWioOdWdajIjj5Wn9WIlbmXjDJDDdFOzQ8L_OGFwNyKaagkdpxDW-FYfjj3lommGycEUGw9LxK37UG9NSmNK4yXKzEXraDw-fn9slT8m1K4mEVxC5_qY2716KXX5rvky30fLgegrn09cLRfqI56_hZ-If_YIk3uVfzaV4RSFpppalTAbStgjUD1zC8EGThSUQcwHMQXEZa9QciYHIv2W4TIpCj_iiPcV0-iihc9Y4Nb8HYlYIZhrB66063FZ4WSOthHT_7STivQQATz9NzKVDHrhX3ppcFfiapPjaSdBCN6abwOmuZSCj82eU5S6Dn1UDqY4-tStPufP3DCwt_8mtJZ3o-zRT3hLnSiA1RpvPi7f7X3L_A4z6m5I86oDhpjEB19EnNOcOwJpgzh1zP3SuRTujhPo28axCu54T8luidWwtrkFIfp6A0bY6JrUnC6uV2I2uJclOi89ZOoS5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
رصدت الأقمار الصناعية آثار اسوداد وحريق واسع في منطقة جبل علي عقب انفجارات متتالية شهدتها دبي منذ يومين ؛ حيث أرجعت السلطات الرسمية الحادث لـ "حريق صناعي" وسط تكهنات مستمرة حول الأسباب الحقيقية.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/naya_foriraq/87078" target="_blank">📅 07:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87077">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d964adb32.mp4?token=pTtqWN2MMqD4u2BwN12JZfOg4Wn4ltQAzA1ow0a6Ua0HlrelPBgkC78KUwAUnphAWDuCImOB0VQDmAfuVg2d9J77GeidZkF4XW7mLZF7cNZFOxVXyRInWbxsarDOmjhOu2WFE9cNz6K1ViYogaXsFa-TPA342hBH3XsHbmcSAzi-FfTNVX21OSSirR800vWP3BXpB4LhuHggzQHmffgSXDS5opfpJEygWFwubOpQhfDWsPQAwn_nsShD9JqK8reND6JnFlblQI-lGCuH-67E_zfTJBrD4ODoh3hbmj269yqKuS2x6Wis8b7ankIzwEohsJb3sp1XpAaZl1wKOz35mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d964adb32.mp4?token=pTtqWN2MMqD4u2BwN12JZfOg4Wn4ltQAzA1ow0a6Ua0HlrelPBgkC78KUwAUnphAWDuCImOB0VQDmAfuVg2d9J77GeidZkF4XW7mLZF7cNZFOxVXyRInWbxsarDOmjhOu2WFE9cNz6K1ViYogaXsFa-TPA342hBH3XsHbmcSAzi-FfTNVX21OSSirR800vWP3BXpB4LhuHggzQHmffgSXDS5opfpJEygWFwubOpQhfDWsPQAwn_nsShD9JqK8reND6JnFlblQI-lGCuH-67E_zfTJBrD4ODoh3hbmj269yqKuS2x6Wis8b7ankIzwEohsJb3sp1XpAaZl1wKOz35mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: "سعر النفط هو 75 دولارًا. قد نضطر إلى رفعه مرة أخرى. أنتم تعرفون ما الذي يحدث عندما نرفع السعر."</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/87077" target="_blank">📅 04:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87076">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSJFhuwpAivUe6RIq0BWUUnAZQKBleZUqsKBEHhR8s_brSxdSzW5tBqcpAX3_ceC_Lidat67XoI-oi8LGJlyXfHH9gZJs0CebjIjNoBJ1-HHrZvUL_UUxbIgBGvC-f0LTyenoy7217h6ICzZoyBYXWQ7sOSTiVSYdGoIb0vad_mS9JDHdlmeHQAxTXPjKfaHWAKO2phBCY2_E69sNXikKXDpmisqAlxrsNBmp60CyFnIYTJ5tFBAr0eIok1oIyFSD0SbLQIWmzL1cJLM473RBKFp_C0F3hdA3Q2i6xuVoB3nCvRYP7rgLbVNQVHae0ZNJFm16OmyKrIzJYbER7pKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
صور الأقمار الصناعية تظهر اندلاع حريق داخل سفينة بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/87076" target="_blank">📅 04:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87075">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrKlVsxvdKY29gWgcSbOzcgy8qeIC3w1ZHvMcxsHC3x2q7G8ujLL0yqX8cENWPULusG6bZZxocHYMuskn0oOzmWPnoMk3AO7Ss5JkEhVuBrepn27I3IvYrOvV9Hds6tgWzyxsnoJvpu_ZkjFkag4icmPfn_GgSkh-8ikBhkDpZIQJSFmPDzyVqJPYohiwdPtl0FXow9tBfPpzq0ynPT49Kk6KgvTdNksLEIePzmIJxYerdKpi6Ti-y8PiN3z6JJVQB_fvizzcNJh0esY6KqGCe5ugHtFAy1BDt_7MMPaoK6buB3S73elNmlDcqWn7uEEdq69EatQrG087WkJMQvmxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
كان مايكل مور، "المحلل" السياسي الفاشل الذي يخسر أمامي منذ سنوات، يصرخ قائلاً: "لقد خسرنا في عام 2024، ولم نعد نطيق ذلك". كلا يا مايكل، فقط تعوّد على المزيد من الخسارة! لقد كنت خاسرًا طوال حياتك، ولن يتغير شيء
لن يتمكن عبدول، رفيقك الشيوعي الجديد، من إنقاذك. إنه يعلم أنك شخص فاشل وحقير، ويريد أن يكمل من حيث توقفت. على مدى آلاف السنين، لم ينجح مفهوم السياسات الشيوعية قط، ولن ينجح الآن، خاصة في ظل النجاح التحويلي الهائل الذي حققته إدارة ترامب، ليراه العالم أجمع ويتبعه: أفضل الأرقام الاقتصادية على الإطلاق، وأفضل أرقام التجارة، وأفضل أرقام الصادرات، وأكبر استثمار في بلدنا، والقائمة تطول. هذا هو العصر الذهبي لأمريكا، ولن تتمكن مجموعة صغيرة من المنبوذين، مثلك يا عبدول وغيرك، من تدميره وتغيير مجرى التاريخ. إنه أكبر من أن يُدمر، وأقوى من أن يُدمر، وأفضل من أن يُدمر. نراكم في ساحة المعركة السياسية. لنجعل أمريكا عظيمة مرة أخرى!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/87075" target="_blank">📅 04:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87074">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">استهداف سفينة قبالة عمان</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/87074" target="_blank">📅 03:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87073">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/87073" target="_blank">📅 03:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87072">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/87072" target="_blank">📅 03:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87071">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
استياء ترامب من وزير دفاعه تزايد لأن هيغسيث كان من أبرز المؤيدين للعمل العسكري ضد إيران.
هيغسيث أقنع ترامب بأن العمل العسكري ضد إيران سيكون بمثابة انتصار سريع وسهل نسبيا.
هيغسيث دافع عن نفسه أمام ترمب بشأن النقص الحاد في مخزون الأسلحة وألقى باللوم على نائبه.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/87071" target="_blank">📅 03:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87070">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
نائب الرئيس الأمريكي:
هناك أشخاص في النظام الإيراني يريدون إنهاء الحرب وهناك متطرفون يريدون استمرارها.
الإيرانيون عسيرو المراس والنظام متصدع ومهمتنا تحقيق أفضل النتائج الشعب الأمريكي.
سنستخدم كل الأدوات العسكرية والاقتصادية والدبلوماسية من أجل التوصل لحل مناسب مع إيران.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87070" target="_blank">📅 03:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87069">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇦
🇷🇺
الإعلام الأوكراني:
هجوم روسي بالصواريخ البالستية يستهدف العاصمة كييف.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87069" target="_blank">📅 02:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
جمال الحلبوسي:
‏
السعودية والكويت تقدمان مذكرة احتجاج جديدة لدى الامم المتحدة ضد خارطة المجالات البحرية العراقية وطالبوا بسحب الخارطة و قوائم الاحداثيات و تؤكد السعودية والكويت بان هذه الخارطة تسبب تداعيات جسيمة بالعلاقة مع العراق ، والسبب هو للاستحواذ على حقول النفط والغاز العراقية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87068" target="_blank">📅 02:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c964d83f.mp4?token=p2DORtvgw4lAbJmNYX6TpxKFk6sdwX1SvevHsgWT9G6cYjkuYvG-rtU-I0yX8u6_sarpcW7iDiL3OMsByeu3qS_uVWitFTzESOwfglP7k6Y4BVXgJjf3LBPtLZd4gKrLOjkTmqUTaF1BK3OpGlDDuD2f9ipYVN9KpspOQ2T5AV-GmxmixYw0reoRh39y9_1OPELuyblhekgp6FhJJkY9RI9aZILDDvBxzHDNH_-5V1EF75F1QrSLHBjqpV2AUHXr_UTSWRxflmbQuIFwkJltrbyA2jqg0Bp7VbCovQU_d-sKAZ1V4Ix67y99eSTUBDSsAKyDFADben17K4Ti8EaKOp4Bl0WlhBihFJJnXY4sg7KOrXC5llhkVE3VVI4WUwK9lPO-9Rdc-i6DvuP6QO0CTltP7eFl63t1eUvKOAj34xIgnutiwn3PmePTsLpvLKw5U0LFf4mxABNhVX3anAHGsSH4uYl4BF4B7gv9sMqSJveyLzppTRNl9jJwuGlvubaH4LL2sm0XdGlCyAL7Ao0ObrMWH_OQmyT-u-TysHb7LmUo4py0LvMc-ZEpqhOv0ZX-G1577gJH8V6aEHCJ-8UP5FSPiXOo4WMApr72zW7m4GP54wHkutyL0RXvRHukIJa7IXeVQ9QBrbtkEijIj6a6xCKMzSdpQ7cAma41WY19VLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c964d83f.mp4?token=p2DORtvgw4lAbJmNYX6TpxKFk6sdwX1SvevHsgWT9G6cYjkuYvG-rtU-I0yX8u6_sarpcW7iDiL3OMsByeu3qS_uVWitFTzESOwfglP7k6Y4BVXgJjf3LBPtLZd4gKrLOjkTmqUTaF1BK3OpGlDDuD2f9ipYVN9KpspOQ2T5AV-GmxmixYw0reoRh39y9_1OPELuyblhekgp6FhJJkY9RI9aZILDDvBxzHDNH_-5V1EF75F1QrSLHBjqpV2AUHXr_UTSWRxflmbQuIFwkJltrbyA2jqg0Bp7VbCovQU_d-sKAZ1V4Ix67y99eSTUBDSsAKyDFADben17K4Ti8EaKOp4Bl0WlhBihFJJnXY4sg7KOrXC5llhkVE3VVI4WUwK9lPO-9Rdc-i6DvuP6QO0CTltP7eFl63t1eUvKOAj34xIgnutiwn3PmePTsLpvLKw5U0LFf4mxABNhVX3anAHGsSH4uYl4BF4B7gv9sMqSJveyLzppTRNl9jJwuGlvubaH4LL2sm0XdGlCyAL7Ao0ObrMWH_OQmyT-u-TysHb7LmUo4py0LvMc-ZEpqhOv0ZX-G1577gJH8V6aEHCJ-8UP5FSPiXOo4WMApr72zW7m4GP54wHkutyL0RXvRHukIJa7IXeVQ9QBrbtkEijIj6a6xCKMzSdpQ7cAma41WY19VLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: قد أكون الشيوعي الأكبر في التاريخ.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87067" target="_blank">📅 01:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
إئتلاف إدارة الدولة:
المجتمعون أدانوا الاعتداءات التي تعرضت لها قطعات القوات المسلحة العراقية واستشهاد عدد من منتسبيها ودعوا الى الالتزام بتوقيتات خطوات حصر السلاح بعد 30 ايلول 2026 والتي سيتم التعامل بعدها بقانون مكافحة الارهاب مع اي سلوك مسلح خارج اطار الدولة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87066" target="_blank">📅 01:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87065">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a22e27b0.mp4?token=nFqBNHAxMVFRFne089ErliXNSWYCoiX8eGOOPfETkBBGzvcSzIhnjRX7ukgtI-6JSNzi-GGHfyomyXlCmti33TGQnhX8FG45cTxxZQVqLeV_SLQmeAa1thhSYXOEsiH6dNvQa80dm5HPLnULUAHqL7jQzabBykCzvchTc-OWd2eRHitkVScsmIsx-t5__ACh-78ey9PkVIk24bV-_vXF6WwYtKyG6L585WaLtoF_QTs1rq5zdWfc324lC5nuCWEkIoeFfpr-4LE8CFGZ9zUhaPlCAWtD7ron-T9Ypymi59-bSIVZU0pXTu4gJUAQz7xprRNOj7ow8ARFHZfp263C4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a22e27b0.mp4?token=nFqBNHAxMVFRFne089ErliXNSWYCoiX8eGOOPfETkBBGzvcSzIhnjRX7ukgtI-6JSNzi-GGHfyomyXlCmti33TGQnhX8FG45cTxxZQVqLeV_SLQmeAa1thhSYXOEsiH6dNvQa80dm5HPLnULUAHqL7jQzabBykCzvchTc-OWd2eRHitkVScsmIsx-t5__ACh-78ey9PkVIk24bV-_vXF6WwYtKyG6L585WaLtoF_QTs1rq5zdWfc324lC5nuCWEkIoeFfpr-4LE8CFGZ9zUhaPlCAWtD7ron-T9Ypymi59-bSIVZU0pXTu4gJUAQz7xprRNOj7ow8ARFHZfp263C4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: "نحن نستولي على كميات كبيرة من النفط من فنزويلا - مليارات البراميل من النفط. الغنيمة تعود للفائز."</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87065" target="_blank">📅 01:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87064">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f8a8d43d8.mp4?token=H2s9ujBbBCuWOM1cHvMRDgES2b753mZUPjtGK1pokdcnB2jZNxwng_z_kHOpIpN4hZddVJi00OWQgXOz720WYOMuuGdg3djf5y_EOExrel5wwHGXH-CNOKe0B9NxGa1pNtbwdvKmbTE508dxsIv7Yyqw3VJQKY6MyVnDwicoe4vLX_7-1yfD0IEA-GK4cbxEWGRAa0Heqdzww3nDo9iOoVfcUHdxXurYmzWl2H2t7bqxErqjOB5XKurLdVVlC09afdBAKQDzCq6SZgBx2ToykHy58ZpA9mIznu807EO89I3SfjODdxD53EZjSAmPI25c8RE51hCPJjhriaijDJ5aH4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f8a8d43d8.mp4?token=H2s9ujBbBCuWOM1cHvMRDgES2b753mZUPjtGK1pokdcnB2jZNxwng_z_kHOpIpN4hZddVJi00OWQgXOz720WYOMuuGdg3djf5y_EOExrel5wwHGXH-CNOKe0B9NxGa1pNtbwdvKmbTE508dxsIv7Yyqw3VJQKY6MyVnDwicoe4vLX_7-1yfD0IEA-GK4cbxEWGRAa0Heqdzww3nDo9iOoVfcUHdxXurYmzWl2H2t7bqxErqjOB5XKurLdVVlC09afdBAKQDzCq6SZgBx2ToykHy58ZpA9mIznu807EO89I3SfjODdxD53EZjSAmPI25c8RE51hCPJjhriaijDJ5aH4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
‏ترامب:  أفضل إبرام صفقة مع إيران. ‏نحن نتحدث مع إيران، فلنرَ ما سيحدث. ‏لا يمكن لإيران أن تمتلك سلاحاً نووياً.  كنا نستعد لشن أكبر هجوم منذ الحرب العالمية الثانية لكن الإيرانيين طلبوا مني إجراء المحادثات.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87064" target="_blank">📅 01:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87063">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
ترامب عن كندا: كندا دولة سيئة. إنهم أناس سيئون. أنا أحب الشعب الكندي، ولكن قيادتهم سيئة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87063" target="_blank">📅 01:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5cb415232.mp4?token=MSOBGnlKA6z1oaWpEFjjVe5BRi2HmXnQm6fMak6LnVGu44w9N3QDuFHt1dmarCCF0W9_2C-tSXjjnJUXQvXp8c2cXziylcr_Gm-Ip8Equ6pir5GoqG8SI62hX1dgHbn_3SZCX7zNm936eBuyWlE4XnlYQ4hTffsNItMfOy-YVJj35-vk4GjO4LA11Qevl6--9Mv_zN1FhAKH_uen1a31tWGqg-gpbnbBrYJSTtgiyIZ-lsloQ6BgmjyWtTG4ywk3Mha6DxJY6ZMhOCOqiYRdsYj-KNhMDHULh6aOd1ITcoF5gSymeP5on3nzIF7j7wtqKbo9gR4602WsmddKE8hE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5cb415232.mp4?token=MSOBGnlKA6z1oaWpEFjjVe5BRi2HmXnQm6fMak6LnVGu44w9N3QDuFHt1dmarCCF0W9_2C-tSXjjnJUXQvXp8c2cXziylcr_Gm-Ip8Equ6pir5GoqG8SI62hX1dgHbn_3SZCX7zNm936eBuyWlE4XnlYQ4hTffsNItMfOy-YVJj35-vk4GjO4LA11Qevl6--9Mv_zN1FhAKH_uen1a31tWGqg-gpbnbBrYJSTtgiyIZ-lsloQ6BgmjyWtTG4ywk3Mha6DxJY6ZMhOCOqiYRdsYj-KNhMDHULh6aOd1ITcoF5gSymeP5on3nzIF7j7wtqKbo9gR4602WsmddKE8hE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب عن كندا:
كندا دولة سيئة. إنهم أناس سيئون. أنا أحب الشعب الكندي، ولكن قيادتهم سيئة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87062" target="_blank">📅 00:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87060">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ozmga3yvkIFCzMwnpaDm2AP-68O_MLZltSjI56_CNx1C6xR6M30DEZiFwwOmWRIe-CIaVq9gbHwKbv_AfRBnERgm7Nms9irB6ST5_xJsQVJkVW5e0Rz04czPBDhuTrFr87hYTNDvLcC5PQAFKagcW8RJJMVxI-pz4fIit0VjB6Py_OLfqOejaticYZ50l9HuvkPdo6K_bSN9sjZiq0Lm90B4dmCvmPQ8SDISvvJQBpsxc88r78mejqitQn_i52pIWyhLWzlH0aWr3-NOqALRCgTBtQcM0RIXZ4tVDMknEOT3tea3valYVO0a1qb1AEEcaqc9iSamttMlK5NMP2-VTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
أمس، كانت احتمالات فوزي في الانتخابات بناءً على التوقعات هي 28 إلى 1، وكان العديد من هذه التوقعات بعيدة عن الواقع، ولكن إذا قرأتم "الأخبار الكاذبة"، فستظنون أنها عكس ذلك تمامًا، أي 1 إلى 28.
كل ما تحدثوا عنه هو هذا الاحتمال الواحد، ولهذا السبب يطلقون عليه "الأخبار الكاذبة".</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87060" target="_blank">📅 23:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87059">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojv0lkRqkaidHVkYZLRqVJnchMtq1qtC5QFuqh49EZuSiHPPZJerXOwGbMh-jx5NsKTneT2JYz-E85hYx2I1prIOZgaBvr5IzvrAUCDVLXKvM04VtDaBXxCwnEbz_bvjJCUBkobBFpBfMQdoDPwFRNMWrF5fneyOkVY0UGCFrs-_QEovgskV4_0itVyNTikrISymq-gUPG67_ZuhetnTSt3pkIHO_dNUryjjtUALkvbavG413tYPQqf_V2aftuvZy2j5iwE7zdLzTe1OZ3kXK8sdRRtpj_-3epWCFD5gHTY6QCVefRrbJy17uNlikW52WkfjxPvWdoxNjaYEWGoVUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هبوط طائرة في مستشفى "رمبام" بمرافقة ثلاث سيارات إسعاف بعد انفجار عبوة ناسفة بقوة إسرائيلية في بلدة مجدل زون جنوبي لبنان.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87059" target="_blank">📅 23:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87058">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61da47e607.mp4?token=CV13Ia4S_cRZ7HHN2cQY9SbgjEnx23exAkJEz564aDxFL7Ubblvx97eqXduj8JHToyb09pLbyATbjDBBmacSMeQSr1pGCfOklfyGqAlnbM5Hs9s6VA5Zup05EeckWtw_oo5zDGyhgqwC6XZ9t38lNwI5tKigJuTiEyEPUYqMRlTLbhIuc7TkMbeay9Y-AbpX954dk2NJrlWTwnaZr8FHaFOp1Dj2kJbBp2PCgPDQUPpBaWuktVJBcO39ZObeJuYmkM1Is88L_XNC4CUBXDdbCWeQOQDwJdhvJkHxC5WI392tQkSPljTqCJIAIEgJTXLwFE12vYI4zKfv8woxYLgppQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61da47e607.mp4?token=CV13Ia4S_cRZ7HHN2cQY9SbgjEnx23exAkJEz564aDxFL7Ubblvx97eqXduj8JHToyb09pLbyATbjDBBmacSMeQSr1pGCfOklfyGqAlnbM5Hs9s6VA5Zup05EeckWtw_oo5zDGyhgqwC6XZ9t38lNwI5tKigJuTiEyEPUYqMRlTLbhIuc7TkMbeay9Y-AbpX954dk2NJrlWTwnaZr8FHaFOp1Dj2kJbBp2PCgPDQUPpBaWuktVJBcO39ZObeJuYmkM1Is88L_XNC4CUBXDdbCWeQOQDwJdhvJkHxC5WI392tQkSPljTqCJIAIEgJTXLwFE12vYI4zKfv8woxYLgppQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
السياسي العراقي اراس حبيب يهدد بغزو السعودية: نحتلكم مشي على الاقدام.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87058" target="_blank">📅 23:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87057">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ece2d0da1.mp4?token=nxbUE_Np_ZglemKySPHYJX87WbPkAWHuCwXqkGZPeAU2E0XuMavizASHEPftEM0VXl1VxQ6J7P5a6hDJSn74bbpbU2DwV97ERUFDJImeKbs2H2i9UksiRJ7WjxowDx39oIHMe8PF-jMEE1E5SwyW4hqkiWtanKrl8nXSsYAl5y8KQUerL3EA2SGzYyO3EstVvvES_R4fml3xcW76oUcP9hDpfUqOqvjHgDyCNzpGVEAwNv3YZZfg6hho1iodbBvAo9g8f8a4D82qWBEXMxAYjLkPwFTY6VLbs6QZ4zlkof4cMrpDHGGSW275uqLmyvDfZPAbS82yu3UWf4gChd_TeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ece2d0da1.mp4?token=nxbUE_Np_ZglemKySPHYJX87WbPkAWHuCwXqkGZPeAU2E0XuMavizASHEPftEM0VXl1VxQ6J7P5a6hDJSn74bbpbU2DwV97ERUFDJImeKbs2H2i9UksiRJ7WjxowDx39oIHMe8PF-jMEE1E5SwyW4hqkiWtanKrl8nXSsYAl5y8KQUerL3EA2SGzYyO3EstVvvES_R4fml3xcW76oUcP9hDpfUqOqvjHgDyCNzpGVEAwNv3YZZfg6hho1iodbBvAo9g8f8a4D82qWBEXMxAYjLkPwFTY6VLbs6QZ4zlkof4cMrpDHGGSW275uqLmyvDfZPAbS82yu3UWf4gChd_TeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
السياسي العراقي اراس حبيب يهدد بغزو السعودية:
نحتلكم مشي على الاقدام.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87057" target="_blank">📅 23:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87056">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRVI7WtAB3GVrhtL0VHkWJQu4e2jS2abjYoBcOsu9mu7MgHtl8w8HZGz8ex5jSez-nMzagtZEGQm9RXtr5BjBzrCJyejiNbRdzZYb6X_8rhW1qUWO9L5r9XsIohJJ-pMVAI1yR3g7l9ADiK_u0f8U9eiRC_kQOEPcTfMzZEgSo7Xg7oobcDWRuPVkYiHNFUCT7xojrOY-i8tj5UrHNKCSQqL8AhVMBJ9i5W1-K3LFam1qXWrWp_wZEQI0aqDGCDDqQx22l9Tca84RG-5TWPucXk07Fs9i_Y8DaTphAdN1FMonwID0WqDypS9zlp7PJESQwB_AeKtbrgd9Y7BIXuxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
متحدث القوات المسلحة اليمنية العميد يحيى سريع: تمكنت القوات المسلحة اليمنية بفضل الله من استهداف سفينة "Daisy" النفطية السعودية في خليج عدن وذلك بصاروخ باليستي وقد حققت العملية هدفها بنجاح بفضل الله، وتم إصابة السفينة وإجبارها على العودة.  يأتي هذا الاستهداف…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/87056" target="_blank">📅 22:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87055">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
متحدث القوات المسلحة اليمنية العميد يحيى سريع:
تمكنت القوات المسلحة اليمنية بفضل الله من استهداف سفينة "Daisy" النفطية السعودية في خليج عدن وذلك بصاروخ باليستي وقد حققت العملية هدفها بنجاح بفضل الله، وتم إصابة السفينة وإجبارها على العودة.
يأتي هذا الاستهداف في إطار فرض قرار حظر الملاحة البحرية على العدو السعودي وفق معادلة "الحصار بالحصار".
تؤكد القوات المسلحة اليمنية أنها ترصد بدقة كل تحركات السفن السعودية النفطية ولن تسمح بمرور أي سفينة سواء من جنوب البحر الأحمر أو من شماله حتى تتم تلبية مطالب شعبنا المحقة ويرفع الحصار عنه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/87055" target="_blank">📅 21:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCxcR06TEeWPnB-5XBNGtRFthwDktQRQ7wkT3S_54f5_BqCuSOnsJT52zLpM-6AUxyzwhOKlR2Lez_GZ0LBUS_8PadkiVGUK48Tz0k-ofCIvTEZjOSNgnrxpI48DUG7UXOVtXU3HjWmwSqwgxjAy60NI7ZIVA4uKQ0fMofBnc26bJ3ViYNpeHKy3LWAjn-Okh5U7g_g2gv9eEcZxTTYjY7rL10KYwdZCQbJmwQLdM6m3PbEPNd54Cj7e52NMOtst-xS30GaQ0KmQ2aO3Zw8mVfbkGTjNnS14P4LejhKD8ypxOxJz8Lx7As2Rve8KiDzdBv-VJ8r4Gxuj5DyjtvmhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري في البحر الاحمر</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/87053" target="_blank">📅 19:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حدث بحري في البحر الاحمر</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/87052" target="_blank">📅 19:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87051">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇧🇭
بحسب المستشار الاعلامي لملك البحرين: البحرين تعرضت للقصف من قبل ايران قبل وقت قصير.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/87051" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87050">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇧🇭
بحسب المستشار الاعلامي لملك البحرين:
البحرين تعرضت للقصف من قبل ايران قبل وقت قصير.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/naya_foriraq/87050" target="_blank">📅 19:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87049">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzjeh3dml2QRWiCqdOx_OD8Uf7_x1BWLX04-5bnHD2bm4Xom7xS18mnFH3u_esbzo6hoxWkvXBF19_oeQOgJiE5Y_VKtG7x-yWDisryVeNLffMINjaSYkgO4Y5kG0ltIVfy4tHWtUyuKqYbCS269jDHPSns9IPgP4Mo4jX7wAbZc1ushQ0a1IdirKPR-UVM2_bg9uUUM37Svua6-Yt-FPY8FuPlds8e8BpeSN26SBTXbwV4NdJ6c_2SD3NACuU01A4j_uEcII9Vrticjp-rpYuT2kIYfVEWeNXphXUeJX4sTm0RheMZh8NKOMH-8hVfFx--JG589YGvA4XPFDiGOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
بعض أهالي سهل نينوى بمحافظة نينوى شمالي العراق تلقوا هذه الرسالة وهي تتعلق بالابتعاد عن الاحداثية التي تتضمن موقع الفوج نفسه الذي تعرّض سابقًا للاعتداء من قبل العدو السعودي ما أدى إلى استشهاد 10 من منتسبيه.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/87049" target="_blank">📅 19:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhSgy4RBwisWCpQumnFNIHXUUKoUVIP1vr2nucAxHSOBiVoDOz9JadlDXS_muDA4krp9keGXgOuspg7UwMbsFgfH0Yq8PUcYEKj3CqwshYXbIqYR5_vtCkOuLi0zsjerYuiiOdTADRsY21gqEOQ4lYh4d9eSHRetjWGGwE8ucztJkE8VKz5rO7EH9e0NkCCZitaR1u3K_LeIR6ZBXL1lGCa_owL_w2YiTH4m8EpcXd98QNpvTL_TrwFwfqFk02HFtNxx2OQ5JXKb0B_LMUQn5L4YnIqy7Zc8X6YEUNTvDydsIZYDgS6COmOw27Y9z32TmHqBEyKTfwzYAQ_kh12bBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
الاعلام العبري
اطلاق صاروخ اعتراضي في اشدود نتيجة تجربة للدفاعات الجوية.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/87048" target="_blank">📅 18:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
‏
الخارجية الإيرانية:
تم الاتفاق مع عُمان على الخصائص الجغرافية للمسار الملاحي في هرمز.
وهذا لا يعني ان المضيق آمناً لعبور السفن، لأن العوامل التي تجعل مضيق هرمز غير آمن من قبل الولايات المتحدة، ولا سيما الحصار البحري وغيره من الأعمال العدوانية والتهديدية ضد إيران ومصالحها، لا تزال قائمة.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/87047" target="_blank">📅 18:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اعلام العدو: قتيلين كحصيلة اولية في الحدث الامني جنوبي لبنان.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/87046" target="_blank">📅 18:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
الاتحاد العراقي لكرة القدم:
تجديد عقد غراهام أرنولد لـ7 أشهر لقيادة المنتخب العراقي في بطولتي الخليج وأمم آسيا.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/87045" target="_blank">📅 18:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇱
نتن ياهو:
ترامب صديق جيد جدًا لنا، ونحن نقدر الجهود المبذولة لمواجهة طموحات إيران ولكن وجود إسرائيل لا يمكن مناقشته.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/87044" target="_blank">📅 18:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي:
تنفي هيئة الحشد الشعبي ما تم تداوله عبر بعض منصات التواصل الاجتماعي بشأن وقوع اشتباكٍ مسلح بين قوات الحشد الشعبي وأي قوة أخرى في مدينة سامراء المقدسة، وتؤكد أن هذه الادعاءات عارية عن الصحة، ولا تستند إلى أي وقائع ميدانية.
وتدعو الهيئة إلى توخي الدقة في نقل المعلومات، واعتماد المصادر الرسمية، وعدم الانجرار وراء الشائعات والأخبار غير الموثقة.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/87043" target="_blank">📅 18:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87042">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الخزانة الامريكية ترفع العقوبات عن شركة فلاي بغداد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87042" target="_blank">📅 18:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارة الخزانة الأميركية تعلن إلغاء عقوبات مرتبطة بإيران</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87041" target="_blank">📅 17:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📰
وكالة رويترز:
صادرات النفط الخام السعودي من ينبع انخفضت إلى أقل من 3 ملايين برميل يومياً بعد هجمات الحوثيين، بانخفاض قدره 0.8 مليون برميل يومياً. وكان إجمالي صادرات النفط الخام السعودي يبلغ حوالي 4.5 مليون برميل يومياً لشهر يوليو/تموز قبل هجمات 26 يوليو/تموز.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87040" target="_blank">📅 17:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeUSwTtSqNtlb2SHXEQY7hCIF2q5gZd9OYMDvVeod-VwFsWFC5GgnBIhrBN8y3ovqamrmXkMVwJFN3wUJa0ga2iwg0mv7gZullC0_-nNaQ1s1pRFaBQ6EgYaRRVcdxutct-J54JnSAS_IvdW5RRPXBnSzgpdtLdFMzFxwJOxIfhpXCC1vvi80NZNX6hoGkkqgc5-hvPFPUP3bIX4pS3PIoP9udZLe7JwjXwk3TMOVMDLP9AuWSYnZsiV2l71NcF6jeq77gyIpvqaL5nCFI_PArm2fXC8PIjmfJfLXrEoX1LFDPG3TdOWPNDyIwYejSIF4H8xO3AhXZ3pE6JCycTl0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: خبر رائع للحزب الجمهوري. السيد، الخاسر الشيوعي الذي يكره اليهود وإسرائيل، هو الفائز المتوقع في سباقه مع الاشتراكية. وكالعادة، كانت استطلاعات الرأي خاطئة تمامًا في هذه الحالة. لم يكن متوقعًا أن تحقق أداءً جيدًا كما فعلت. الآن، ستزداد سياسات الديمقراطيين المجنونة سوءًا!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87039" target="_blank">📅 17:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزارة الخزانة الأميركية تعلن إلغاء عقوبات مرتبطة بإيران</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87038" target="_blank">📅 17:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87037">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f37d7808.mp4?token=D_-kaVx4U-Ek0Zm4bJsrzW17B8NVmDpwv-zgwiI7dQbwg2TiWx1hktIigeZFcw8sJJCi38ubn6gxKn4B0upFgNxM3nM4qYrJ85WgbsLxK_LI65zh7sQ5h7HPbKm9C5RVDLQcLYPXaqGAdfFNbL_XHKHylZlYRoABqMpxfzFrVZnXw3l1k9KJ9wgUKc4Yi1UWiUW4KzPlxEyRy2jIBHihYmI4fBtiAJXuP4J72FNG_PZntNQnUKPcSSWH5u9Fer4LZJWQjRWqglZRWHd1uP2zfmaMB0EWV13m2XIkuoGvFbj9nwlk25nyCR2AXfDti0gJjZ_Lgdk8e1Ro4QmJ9EP13w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f37d7808.mp4?token=D_-kaVx4U-Ek0Zm4bJsrzW17B8NVmDpwv-zgwiI7dQbwg2TiWx1hktIigeZFcw8sJJCi38ubn6gxKn4B0upFgNxM3nM4qYrJ85WgbsLxK_LI65zh7sQ5h7HPbKm9C5RVDLQcLYPXaqGAdfFNbL_XHKHylZlYRoABqMpxfzFrVZnXw3l1k9KJ9wgUKc4Yi1UWiUW4KzPlxEyRy2jIBHihYmI4fBtiAJXuP4J72FNG_PZntNQnUKPcSSWH5u9Fer4LZJWQjRWqglZRWHd1uP2zfmaMB0EWV13m2XIkuoGvFbj9nwlk25nyCR2AXfDti0gJjZ_Lgdk8e1Ro4QmJ9EP13w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترفيهي
🇦🇪
السلطات الاماراتية تقول ان ما حدث فجر اليوم في دبي هو حريق داخل ورشة.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87037" target="_blank">📅 16:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87036">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/836d56fab5.mp4?token=oNqvhVB71cCbyGADGq6Eoch1EWob-0cXFs157B57tak-sRZFLFgS61gxUXdQNktbTPZlf4_4ktFyGDkBX7vhPsReWKcBFvQSEgjU5Qu3CqC3JFMcyYPiZbD7vduAjt1vjBAFazHQcbPTWw9qR2IpnwXyUM2noyQkjMVgvx1vC4a5TIYdYTZcstP2BQZK1EWYzQY3NX52A6eg2tUIPJaJ_ir2L1J1KM604DAW4rm4gMaDZLCo7eyUmoNP2oXxjtRxCcGJdpza8ZfYsUdHglZU7pRPknuPUM2I163Y_vd7DaEvUYOd9D8Zhd2TRc3ScDcKhyzLEjdK9wwpJU8dVaXN8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/836d56fab5.mp4?token=oNqvhVB71cCbyGADGq6Eoch1EWob-0cXFs157B57tak-sRZFLFgS61gxUXdQNktbTPZlf4_4ktFyGDkBX7vhPsReWKcBFvQSEgjU5Qu3CqC3JFMcyYPiZbD7vduAjt1vjBAFazHQcbPTWw9qR2IpnwXyUM2noyQkjMVgvx1vC4a5TIYdYTZcstP2BQZK1EWYzQY3NX52A6eg2tUIPJaJ_ir2L1J1KM604DAW4rm4gMaDZLCo7eyUmoNP2oXxjtRxCcGJdpza8ZfYsUdHglZU7pRPknuPUM2I163Y_vd7DaEvUYOd9D8Zhd2TRc3ScDcKhyzLEjdK9wwpJU8dVaXN8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جيش الاحتلال: البدء بتنفيذ غارات في جنوب لبنان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87036" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87035">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جيش العدو يصدر انذارات في جنوب لبنان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87035" target="_blank">📅 16:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87034">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شركة يورو وينجز للطيران تعلق رحلاتها الى مطار اربيل الدولي</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87034" target="_blank">📅 16:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87033">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0b8FTmszqKdeeCuns-itL_-MXVRiJZJ8N24HxPAE0mTHT4WD9kQHWBgR-5DqfILuWG6Zq26l5DkQ1JTTaFTnAMOfcYNRp6809Hhily5YYPXZmsNzBNjayekL5EUwILgc8_d3t0JDH-qSPK8rlf8Dv-7afOyM6QBk_qFf7paSGOLtzh7wZMbRW3M3ackw8zspU4-RO_IxtioYgZIWzp6mKu4eC0w2RaeMOh5We8cbpQAbtksfl3_yjEsnh2vKCK-ghEXI9VgMhYYqQQHCevDej3F_J1PR5MX3Gkg5F6UDNtNJ8NN2yGzHdFXrcgraKI8RFTQk46jRccT03w6d9HHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش العدو يصدر انذارات في جنوب لبنان</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87033" target="_blank">📅 16:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxeMvMZE2lROscW2cK5Q3RdSn5Z1tLIwGNf25yepPRNa8f3n143_Oulp9-8vmC55HFPxBTziOqZCJ3V-fozKJPmB7EA14Awb0DTcb4eWratgvicDsg_Rm8DPx7jEnIkOWtoVmQwHkNeSzQDQN8ONGwNKVHCIH4MsRn0Q8c-E45IyXS41T1pQYh3EdeZRuPlh4ttoDrCfGaCrS0eGqYjpRg0adk5_D-3aLXwC-hCWJD5O86PvqroM1BpxDXYEC-r9KJ_QRoA-X1TwjkDkQiaPYUHt0otzWdYLqJJnuRLqFToOPEq_afRXGsxAtlXkoiyBTL_Avvp7JyVNolfxOV2iZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وزير الخارجية العراقي يلتقي نظيره السعودي في عمّان رغم عدم مرور ايام على العدوان على البلاد والذي اسفر عن 20 شهيد واكثر من 30 جريح</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87032" target="_blank">📅 15:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87031">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏وزير الخارجية العراقي يلتقي نظيره السعودي في عمّان رغم عدم مرور ايام على العدوان على البلاد والذي اسفر عن 20 شهيد واكثر من 30 جريح</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87031" target="_blank">📅 15:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f6ede8eb.mp4?token=l5H-MuROq6N-wpN_A5tY1MpWVsdq2xrbd5C8P4bYnnXFPRqdnzhRkSszE5c67dvsS5CqJagXdNaxpjBGRH_Kkcoc7e3VQvzp_NlBA8yEP400Y0xFtrAdMI3be8ELNOG-FF2GM-9EF0jQx5nk9nfIZjUugVeZmBDRi-rUGABkHaI2kdD3H00DNT2n7xa1d6xJRZhYD70_5-_lzuIbBS4cNP0ZS5FAVbLSfB9e8oHU6mtSZCd-_QnQnuviYn8podUwXr6qF6WFyI1p_ka73xPG7bP6RGsPCQYK0ILBzoptnqAkCC6nWU2Oa7tqw7H1uLVqCXw_xLOWp03nfJrAAFumGrfgYHMvClxjHlHFycB7HONiQ04xD2oIOFzLB2leKvxRE4Mp2ZgdHs9-O7h0RMKoCUm_QQM1f0DwGXPmzl0cXnPTy4IEpwENLMegq1-vd7hh5cnS9V5AysVLZpY-YG2LEerAoOlkRlVlRLPIAm4td0uWHlJb5k9igFUYF_bgKQLnEQvePX1O91BlWScoH_W7ISJ_KPpc_upYAG3gny53_EQzgSFreiAqF_gWwvwEsFreysq5sq8cDcmuLX1-l1mMatm5udgEPZnpLCXbtrMAYeRgKYCvYhw1J1tNjjxrNuTRk2Vrf3dBco-sxEmdCLv4VklFDOGBYyrx3IMUJ_MTMzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f6ede8eb.mp4?token=l5H-MuROq6N-wpN_A5tY1MpWVsdq2xrbd5C8P4bYnnXFPRqdnzhRkSszE5c67dvsS5CqJagXdNaxpjBGRH_Kkcoc7e3VQvzp_NlBA8yEP400Y0xFtrAdMI3be8ELNOG-FF2GM-9EF0jQx5nk9nfIZjUugVeZmBDRi-rUGABkHaI2kdD3H00DNT2n7xa1d6xJRZhYD70_5-_lzuIbBS4cNP0ZS5FAVbLSfB9e8oHU6mtSZCd-_QnQnuviYn8podUwXr6qF6WFyI1p_ka73xPG7bP6RGsPCQYK0ILBzoptnqAkCC6nWU2Oa7tqw7H1uLVqCXw_xLOWp03nfJrAAFumGrfgYHMvClxjHlHFycB7HONiQ04xD2oIOFzLB2leKvxRE4Mp2ZgdHs9-O7h0RMKoCUm_QQM1f0DwGXPmzl0cXnPTy4IEpwENLMegq1-vd7hh5cnS9V5AysVLZpY-YG2LEerAoOlkRlVlRLPIAm4td0uWHlJb5k9igFUYF_bgKQLnEQvePX1O91BlWScoH_W7ISJ_KPpc_upYAG3gny53_EQzgSFreiAqF_gWwvwEsFreysq5sq8cDcmuLX1-l1mMatm5udgEPZnpLCXbtrMAYeRgKYCvYhw1J1tNjjxrNuTRk2Vrf3dBco-sxEmdCLv4VklFDOGBYyrx3IMUJ_MTMzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران حربي مجهول يحلق في اجواء محافظة المثنى جنوبي العراق.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87030" target="_blank">📅 15:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Diq60D1m_m4QqLpbCWH8hlpMJx3RLVqgLdvlxVAwmUzdvm6iAGes4h4LKGrQCvvHnY7Gn1b7Z1UefU_pvjp8JXxJPVCeGhaTpH-WyFedQCwFRnx46QRy-dh_4Kx-p6IpDjHC33LaHEYvdUI7CnffnYOnvHbuwTuxrSncdmQtT-LwkC72o5Xusl-jBCQzT0kAEpb0V9oVP6hdmeePTesApemGmkf6FnM9lm1rWTiVRNYbjdrV5WN-idDVjb3qxb3boKplYmujnT-oILL0CmMCsuLJJYcjZbhlT0KlS11OFqXSDQ2mvIhSmB_vYQV1FFHPc8N1QdYNz90hZIQQroQIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
تيمّنًا بالسيد مجتبى الخامنئي..
مواطن عراقي يختار اسم "مجتبى علي" لمولوده الجديد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87029" target="_blank">📅 15:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">غرق سفينة امام السواحل اليمنية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87028" target="_blank">📅 15:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldBM0Mq7erprj_UDspt_CsNNu8LAr_WYN4uuIQFmqUZT-JCoJwxsuD6_i9q_BHWg0kdfijt0X8VYJCkXpOnUp_8irgIm88ZZtOI7ceq4pYp-QVF2JlKVK_5vHUofgk0AfxNKThK9g2J_fTnBGF8M8cj7kfGWalchfxDlmIkti-P3VZM5Qbpbtsjb6M5hPHYbQ7_ilZ3XKkIYNnXoBME5Nc37FB0eesDLQKyOZPJqifJLtqMt-uKB39NVr31_q_Zi_iQS_VgR-e8A1gmQ1FySg4kxoD-s_U3jzYCr3OZPtg4pbYPCq52l4jl0ZXKBb6-AcArc4HtKjhHESEd2N6nBvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني في البحر الاحمر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87027" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87026">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87026" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87025">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87025" target="_blank">📅 15:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87023">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVNbMaEtADqY-BX4qWc1Flp6Bg9Z1dT008qacmYz5wMUnWAHDItOJ30UTtXHi_apNtYVBMNGnWIMsNNLGNObp39T1hBEBJFFQ8zATqgF1LcLRL6Mi31m2nnkdy7qy7HzAMa6-l7ODLesX3bvDCXGI-RAjlZbF4IbQI0w88R_sZ0pY8heZ4Y08w2Xrifs3pwAss48zlgKashQ8KcyxU9noKBCfYsmM96u8syxZoMWze5CWz7rQuefwlUhMQZ5bO-7LwqC04_ZRRRxXKioUYmAMx30aANSen5IwCo5jKmrD4NxEP_Y-oJsAXA6eWgDF_GR47BdzrzMAlFoxtny68hqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cw7pp8RQR3rmfWC79kW8R0IRtTtHZtF683saztHOLy2HMsV2niuPyIc8n8WC7GehIJVHSYavBvT9cRBiEZtvlKXfZ936sTUO5gnBOhQ3PGl0p3Ac0syaCKT4FSX0sm0tqDRr4afta2udEHl8hiTd9dnQep6_rjHMf0WzwgkstAz69RbpB6UMmYLdxzCYVRqzdV2INTJK5KvwrwJ1VeodmaXn4iugdvSXMuyV9umFN-a72vs29CBhU-P9FDo2I8tjFnaqvwO-TOfd_X91z1w5XiaL7dVN4Ggwlf1ihIhUIGug7d6jMGSQjuCCr78S85xUuEIQoConYy67_T_TnkBFXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
شبكة الإعلام العراقي تفتح تحقيق مع الموظفة "مينا أمير جواد" على خلفية نشرها مقطع فيديو يسيء لزوار الأربعينية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87023" target="_blank">📅 15:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87022">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
🇺🇸
ترامب للامريكيين الغاضبين من ارتفاع اسعار الوقود:
وضعنا الاقتصادي ليس سيء.. سينخفض سعر البنزين إلى حوالي 2.50 دولارًا للجالون في حال التوصل إلى اتفاق مع جمهورية ايران الاسلامية</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87022" target="_blank">📅 15:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87021">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حرائق وأعمدة دخان واسعة تملأ سماء المدينة الصناعية في جبل علي الإماراتية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87021" target="_blank">📅 15:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87020">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزير الخارجية العراقي ونظيره المصري يبحثان أهمية مشروع مد أنبوب النفط إلى العقبة
احلب يا طويل العمر
راحت النفطات</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87020" target="_blank">📅 14:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87019">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrkAbnIDPCE_QNx9xFllPsxdeI063ZMZee94ke-AKYjDvNgZa8U4oDC9cPTnLL-vYOsvlz-dBrS0FhE5XhSxALQ7RalSvoY5f1jP1DpqPAGYY1nDzJrRRxixNyyhbPD9LPaL8Hi7_wxhKZPSpMcFWyUUHnQVp3zs6V2XbL7ui70CBrwCcf7zAbsN6yS-XsLsjdoMJBPrjTmRutDUDkhbW6oGgNPJ4nbH0NvNYPtzoqfGuhQLRuPgQQe4PTYkN-jBDNhyqQ7DJl_JO6RrVUb0qLORgMDoGSb3eTrZQkS1jwge7G6-rvsvjMl90xqMNJf4iW7_OH2_ICjTMycgCynLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
اصابة فلاديمير تكاتشوك رئيس الشركة الروسية المصنعة للطائرات المسيرة FPV بجروح خطيرة وادخاله العناية المركزة بعد محاولة اغتيال بالقرب من يكاترينبورغ حيث ‏انفجرت عبوة ناسفة مزروعة أسفل سيارته المرسيدس مما أدى إلى تدمير السيارة ومقتل سائقه.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87019" target="_blank">📅 14:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87018">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوي انفجارات في محافظة اللاذقية السورية</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87018" target="_blank">📅 14:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87017">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اعلام العدو: من المحتمل وجود قتلى بين الجنود.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87017" target="_blank">📅 14:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87016">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هبوط طائرة في مستشفى "رمبام" بمرافقة ثلاث سيارات إسعاف بعد انفجار عبوة ناسفة بقوة إسرائيلية في بلدة مجدل زون جنوبي لبنان.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87016" target="_blank">📅 13:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87015">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4638e6b712.mp4?token=RXEV156wqZxrNptGCB29VdVSTeGaJAQABZQRrsjh3zsxSldFh0BNLw3wQ4CuoVY6L-PcvWPU9ku_fDTu131HK4YcGdbHQWo5NPa-2yAmMhTt7knWKtfi-61S9Z0qFbf7QySEuSD4i48Cu8iiNee1-MxCAukwYR72gwj09FgEL2aA0wdp9vlcJvgIfh0n403nHlEP2_bg8NTyl4uz8_7vXhPb0YEQNYliXH56-AINghS8_aNwavkD8PFCcrbjyvAljpgM0iKF9RbeWAdHnTNdwU7IXt2S8bY3dp4CZn33dzpsUcJnplp-32CFP_yfsRxO8770sHB-a-5mQLbLbnLmfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4638e6b712.mp4?token=RXEV156wqZxrNptGCB29VdVSTeGaJAQABZQRrsjh3zsxSldFh0BNLw3wQ4CuoVY6L-PcvWPU9ku_fDTu131HK4YcGdbHQWo5NPa-2yAmMhTt7knWKtfi-61S9Z0qFbf7QySEuSD4i48Cu8iiNee1-MxCAukwYR72gwj09FgEL2aA0wdp9vlcJvgIfh0n403nHlEP2_bg8NTyl4uz8_7vXhPb0YEQNYliXH56-AINghS8_aNwavkD8PFCcrbjyvAljpgM0iKF9RbeWAdHnTNdwU7IXt2S8bY3dp4CZn33dzpsUcJnplp-32CFP_yfsRxO8770sHB-a-5mQLbLbnLmfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هبوط طائرة في مستشفى "رمبام" بمرافقة ثلاث سيارات إسعاف بعد انفجار عبوة ناسفة بقوة إسرائيلية في بلدة مجدل زون جنوبي لبنان.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87015" target="_blank">📅 13:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">إقليم كردستان يقرر احتساب كل سنة من خدمة عناصر ميليشيات البيشمركة بسنتين ويشمل هذا القرار جميع سنوات الخدمة الممتدة من عام 1960 حتى عام 2003</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87014" target="_blank">📅 13:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87012">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXy6HtUoHuQHYhc4LtJoGzhbWbokQ-xZyj_Kdp6a5hX3tLb2Z42HxXe_NzpDCFfxhEzkqC7vYDfKfCKjjZX8jsoU5di0CxdNRyw8M60RSTi2UPkE69VFbbEIWPnEFSp6D7f089HinxTmcPxXAXs4AKZMLAxt6elWSEBLsODcx-_OhMKVpKSYbdrfNc_NcoWRl3bDn2MWX-GJNBTUcx_hWa0iXMPhWtV4ht9OyPbM3p5HDzOt_6UchA66VmM1wa6ygxvqpqfbw8pExce6hu2k6h9K9hUvQFZRGi7Qrt85lqgHOeVSzK37PgWYewt51fg2Z1QtIUNnT3_Q7i-lnfHLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDkXtcWRRi_PypvACLMXd-1aO6hICfdTOiiyagYcLGhhB62YiQOW-RLjkU98rCeNUCz_FCG9rerTUTDq6hRvZMvoGqve2hxon2f1QqlGjXuAPcXMfGZ6c8O0hRpTsxWuh0NOTASa0CbdrASjvW7wxvnITG2a3HkIcvei6Im8cTpKstV3T-1woT9AEWL2R1eBmmQTBiMe22kEjUeotJ1vEA1Cob82KEv1w85l5XQ2eUQKRCj50G5osNK5q4W3-rjm93NR3E9d-yyPl4p1YDfybLmr_-wS-DkOo8PJyuGn6e219IfwdKIMPRtvAQZX25Ycg97f5OMIA6eJd9vZU23CpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
ألمانيا: اكتشاف طائرة مسيّرة مزودة بفتيل متفجر ليلة الأربعاء على أراضي مطار لايبزيغ/هاله، والذي واجه قيودا في عمله.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87012" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3nBLhSxQjM__GkwB56JTl7XOlWffl_rScMGOXnxvRbuxDh9bnpG76Ya3jsnhr2qR7kEfOxSGHqYWopn6fQ2auBNyV70IYdzm-DanQTefL_XNMo0JluDeEkEJTh8O6LzkDipnNTZKB9PEcC-42a8U-raNoWOKohZyNbqTHUc1qmCgE7XpSrRMJEQxrCPe9VX3d99qoNyCc8EtGBsopCFbsWTH-b8W6y1GVywUXaDSg6CGoLGcNh_vdNXtbgE8rMge9CR2ENVgRrqjRAbUK4Wq5AyKf0bJziJbmlhalvI1nxqX-2VAGljCDcDKAltea1dXYxaE9NAuntMinQcszQkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إنتحار المعارض الكردي الايراني (مصطفى قاسمي حسنون)د في ناحية بحركة ضمن محافظة أربيل أمام مبنى الأمم المتحدة اعتراضاً على عدم قبولة كمهاجر سياسي وعدم توطينة في دولة أخرى كلاجئ سياسي</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87008" target="_blank">📅 13:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlqW5fsifF6vJ3rWxkLX6ViDj3ZI7VpLSHImj9heQIggGpM05fYNc5OYK5xxxgtXpV28XNt-xtFJqeB9HkSglSvyIiY_D5Hxz1n4n8N2unXdZyLc4G0tWPvm6HFsoFm9EvxKnoyN7nCMGZMGL2NoXjyK2hIqppo7iZuFqpKsMKGEcj59cdgiXS6swPK7e7YXN1uEX9mksThySULnhTqw5Hze-c7YXzsnQOLqOUVLrBmEWWkIp11Q-xf8IZiYfbgSZSfUxb9wgyEaQU7YH5N9Hd4uX9js8O9hRA5yKMj0BJ--ceLgw17WMP1SlKE1wqtV2FHcvh6BX_gKsd3R2tL_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">More time , more 48 hours softie
😆</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87007" target="_blank">📅 12:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aslcOJ2fXNuNjZeKkaa5ReJLtLkc7l6r3iNyGcAq5KhbwFnusTjox6Za0TYfpO91lFlMDbi91cLpNJdlOuq_JugsFxqdc9aOeHRiv43w-gqUgnBffjudgquCWv6bonUERL32bFdB2z3G3eLnPEuFjo4Ed0PZRGiRQuhsCc0S68FnSI7oyNNk4eVFhNOPnCi9_7Ek9WI1mAMTVnEc17rmWmRiDu_azTRxG748xhEFt-0-LUBHUtY7AG55wSlaEM7Svv4DLBjcFYej7SjnmipBbRIbRXRBYdOuW7e4GnizKbWzfZ35S79w6_fx6uv_hyljSuaucnELBzfdtxfV6J-UaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
شكراً إيران  بموافقة الحرس الثوري ؛ عبور ناقلة تحمل النفط العراقي من مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87006" target="_blank">📅 11:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87004">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇩🇪
ألمانيا:
اكتشاف طائرة مسيّرة مزودة بفتيل متفجر ليلة الأربعاء على أراضي مطار لايبزيغ/هاله، والذي واجه قيودا في عمله.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87004" target="_blank">📅 11:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi_G2VMBArn87d_sETWFQxuAt8mr3hy2ItM3DmFTToKGlXRAY34kI7qLMqk1JZKSWMaT4ga6izwqoVformMkOZ-CLvbJEnmQYVf_ZRrFaURdV9Fx6L1w7_L94CRQLUdwotAzhPCr1mh6ZJ1wLBW0BsL519QRHLvzn2G-puR4WoGy6n2B_mAJ5frgTDB_ZWPCUChvPpWJX8BlGycftEJoEkjyNVg1wobjdR2m1FAug4CfAOgSHDt336TabvxiAXLHMK3EuGVtyZhUdrZyBk8mNwaqeXnVo0jSuAwwkV87HGtNb2DM1cn6v-pNNcsIMmab-WN7rDBAlIhl-g1OVKk9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
شكراً إيران
بموافقة الحرس الثوري ؛ عبور ناقلة تحمل النفط العراقي من مضيق هرمز.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87003" target="_blank">📅 11:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ:  في إطارِ تنفيذِ قرارِ القواتِ المسلحةِ اليمنيةِ بحظرِ الملاحةِ البحريةِ على العدوِّ السعوديِّ وتثبيتاً لمعادلةِ الحصارِ بالحصارِ تمكنتِ القواتُ المسلحةُ اليمنيةُ بفضلِ اللهِ منْ استهدافِ سفينةِ "وفاءَ" النفطيةِ…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87002" target="_blank">📅 11:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامب: مضيق هرمز قد يفتح اليوم أو غدا الخميس</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87001" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzDJoCPB9S25xPQeSY-TMt9_QL1mJnBdYxvUHc2LNHxkrU8kNF0Po0_D2ivi9BoJ5QdloYo3xJwsu23aNe-QOwJ96E6YusHMFA6JGe9Bm90MwtAUSNxM6oUEqBNr9OoB-JgW4OaV3IhJ2GPBsK5fw1dsNpmqFJxM0LKHyQ0Qy4tYOPJzPZOSku-GdY958Kxq6caImPV0yWAj8WfhIKEt2O21VexesmiiYblzAAD5fZGfgMX3f8Qk6fFjwtEdsyez57VXdzRq8lBbLXx2eLYt7MvY47EIXagp2Az3JFg5Lnh8xLlVxncbaJQrCjEt4T2TL1BYM4R1-4y66dnq6glttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
استمرار اندلاع الحريق في سفينة تجارية تعرضت لهجوم بسبب مخالفتها لقوانين حرس الثورة الإسلامي واشتعلت النيران فيها أثناء عبورها الممر المائي قبالة سواحل شبه جزيرة مسندم العُمانية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87000" target="_blank">📅 10:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/86999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/naya_foriraq/86999" target="_blank">📅 10:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ:  في إطارِ تنفيذِ قرارِ القواتِ المسلحةِ اليمنيةِ بحظرِ الملاحةِ البحريةِ على العدوِّ السعوديِّ وتثبيتاً لمعادلةِ الحصارِ بالحصارِ تمكنتِ القواتُ المسلحةُ اليمنيةُ بفضلِ اللهِ منْ استهدافِ سفينةِ "وفاءَ" النفطيةِ…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86998" target="_blank">📅 10:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ:
في إطارِ تنفيذِ قرارِ القواتِ المسلحةِ اليمنيةِ بحظرِ الملاحةِ البحريةِ على العدوِّ السعوديِّ وتثبيتاً لمعادلةِ الحصارِ بالحصارِ تمكنتِ القواتُ المسلحةُ اليمنيةُ بفضلِ اللهِ منْ استهدافِ سفينةِ "وفاءَ" النفطيةِ السعوديةِ شماليَّ البحرِ الأحمرِ أمامَ منطقةِ "ينبعَ" وذلكَ بعددٍ منْ الصواريخِ الباليستيةِ وكانَتِ الإصابةُ دقيقةً بفضلِ اللهِ.
وبهذا الاستهدافِ يكونُ إجماليُّ السفنِ التي استهدفتْها قواتُنا ثمانيَ سفنٍ نفطيةٍ سعوديةٍ منذُ بدءِ الحظرِ البحريِّ في 22 منْ يوليوَ الماضي.
فيما بلغَ إجماليُّ السفنِ التي تمَّ منعُها وإجبارُها على التراجعِ والعودةِ في البحرينِ الأحمرِ والعربيِّ 29 سفينةً نفطيةً سعوديةً.
ومعَ نجاحِ القواتِ المسلحةِ اليمنيةِ بفضلِ اللهِ في إحكامِ الحصارِ البحريِّ على العدوِّ السعوديِّ منْ بابِ المندبِ جنوبيَّ البحرِ الأحمرِ اتجهَ العدوُّ السعوديُّ لتحويلِ مسارِ سفنِهِ النفطيةِ باتجاهِ شمالِ البحرِ الأحمرِ ولهذا فإنَّ القواتِ المسلحةَ اليمنيةَ تؤكدُ على أنَّ عملياتِها ستستمرُّ وتتصاعدُ في استهدافِ السفنِ النفطيةِ السعوديةِ شماليَّ البحرِ الأحمرِ لإغلاقِ المنافذِ كافةً عليهِ ومنعِهِ منْ العبورِ لتثبيتِ معادلةِ الحصارِ بالحصارِ مهما كانَتِ النتائجُ والتداعياتُ متوكلينَ في ذلكَ على اللهِ ومعتمدينَ عليهِ.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86997" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇪🇸
وزارة ‏الداخلية الإسبانية: وفاة ما لايقل عن 67 مهاجرا خلال عبورهم جيب سبتة.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86996" target="_blank">📅 10:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0yhoy4prXRPbum3bRXIrW_3JGuVdd2y4FZgRjvVL2BKyON7xWnmaexMOVT7HPR1ugh0vo0LHRG6X3ENLdMf1UJJBe32TtpZKy6-8kgLvk2GWTEJKjcpjWi1iS04lzt07TfVC8SxzB8S4IgQS9qa88Va5RQ8TYOro4iu0u_itjaN2t8GQ42cjQznoBVQaki5QfSVQy6MoCh1z3Kjm4kMdTxWhmuNxM9Q2ZH428Cl2q0Rz5iggERlGO4I0yfea-1xbujqGvxipmIxSOWnz9Fti_yPaTi417yZjKZJJfXfYqBoX2f0t4N7yo8RDNicOwE34H3HJ7kEVh7QrzHXGKscLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
😃
خسارة كبيرة للوبي الصهيوني في مقاطعة ميشغان بامريكا
‏أنفقت لجنة الشؤون العامة الأمريكية الإسرائيلية (أيباك) أكثر من 36 مليون دولار لصالح منافسته، هايلي ستيفنز.
فيما يتوقع لعبد السيد في الانتخابات التمهيدية للحزب الديمقراطي في ولاية ميشيغان.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86995" target="_blank">📅 09:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏بيانات كبلر: 8 سفن فقط عبر مضيق هرمز يوم أمس</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86994" target="_blank">📅 07:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed420e5d2.mp4?token=TxMLey7bSiAoPqdSNSzlN0az7EvC8TCqZh7Hpxp6vPdsd8FZhDGsuyWtp9kn9FdGcIcpmKQJP_ezrd8eZ3tcvLPudGAwqmscvsITKBPmt8p6rRDL3jzkevRDdGKBMhhpqd3afPIwVxCclkWKZZsSjDzSl_X48kDuoR8MvGADqb5TwQGyygJj0c9pPgfJJivSDIC7I-k8SRPhyXr37iKZBk4Z35Mz8zz6ajkaaXs8agW8TzAc18g7fmaryvDNp1V0y_FYmw4ytAaL06qnLTrcLNbUsOP52aiKCpEKE13pwleGJlQMZdG3HPmwEcAvRdc6iBXqiAp8Cr8WlO4dWhsK6oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed420e5d2.mp4?token=TxMLey7bSiAoPqdSNSzlN0az7EvC8TCqZh7Hpxp6vPdsd8FZhDGsuyWtp9kn9FdGcIcpmKQJP_ezrd8eZ3tcvLPudGAwqmscvsITKBPmt8p6rRDL3jzkevRDdGKBMhhpqd3afPIwVxCclkWKZZsSjDzSl_X48kDuoR8MvGADqb5TwQGyygJj0c9pPgfJJivSDIC7I-k8SRPhyXr37iKZBk4Z35Mz8zz6ajkaaXs8agW8TzAc18g7fmaryvDNp1V0y_FYmw4ytAaL06qnLTrcLNbUsOP52aiKCpEKE13pwleGJlQMZdG3HPmwEcAvRdc6iBXqiAp8Cr8WlO4dWhsK6oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: نحن نخوض نقاشات جيدة جدًا. قد لا يرغبون في الاعتراف بذلك، ولكنكم تعلمون أن الأمر مقلق بعض الشيء.  أخبروا الناس أننا نخوض نقاشات رائعة، ثم يخرج شخص من إيران ويقول إننا لم نجتمع. هذا كذب. إنهم يريدون إبرام صفقة.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86992" target="_blank">📅 07:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a30c867.mp4?token=hG0PV_P3x_ZHvgwDoDDnHSxRumY-e138xNgNhSddm6_QTF4fyR7OMOfwTQweWqSOV0tec80qfL5s-3clRUpaozcsU-EYjcgNdHImlngXi0ORViUZ_QjZtngfZygyhAW0ff0U-QOFVkcH75mqSO-8H4_KdEY9bYcSIInWbpgb9UpxxRbFhh-5VoFF9MXdeBZ6Wp8RACNod3yVRyJyPGI8KVAH8x0bs3vhy7z4LiH6eddOs9j6DArvnCCkbj4TiozQoNktHhblFbkP6F_qSRN7cjPzAshWJyP9oSVVc5avutzHW0nIlt6m9nNq2vOc-OzEwKpPmJOReLKKvDiNkFf3Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a30c867.mp4?token=hG0PV_P3x_ZHvgwDoDDnHSxRumY-e138xNgNhSddm6_QTF4fyR7OMOfwTQweWqSOV0tec80qfL5s-3clRUpaozcsU-EYjcgNdHImlngXi0ORViUZ_QjZtngfZygyhAW0ff0U-QOFVkcH75mqSO-8H4_KdEY9bYcSIInWbpgb9UpxxRbFhh-5VoFF9MXdeBZ6Wp8RACNod3yVRyJyPGI8KVAH8x0bs3vhy7z4LiH6eddOs9j6DArvnCCkbj4TiozQoNktHhblFbkP6F_qSRN7cjPzAshWJyP9oSVVc5avutzHW0nIlt6m9nNq2vOc-OzEwKpPmJOReLKKvDiNkFf3Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: سيكون الوضع سيئا للغاية على إيران إذا لم نتوصل لاتفاق   لدينا متسع من الوقت للتوصل إلى اتفاق مع إيران</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86991" target="_blank">📅 07:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏المراسل: إذا تراجعت إيران مرة أخرى، فهل ينتهي الأمر؟  ‏ترامب: حسناً، إذا تراجعوا مرة أخرى، فسوف يتعرضون لضربة قوية للغاية</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86990" target="_blank">📅 06:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33ea57fb3.mp4?token=gDa_MkHDcRtbh97TI8cTfA2CeuzmFDscXu_Q6s0nCjqvuytKTMc4dDcI5L0j2rAhe7Pv_ITbFLooyELGoaxBReQMcW391OCuM6MY4pI77zSzJZz_fQ-VIDW5uowvMN2IyCeOqNQ1LbvmcHiWxVkyIlraDgzs6zHvw3MqHoG6sPr1GhKW4MLCOtaIpKrIPKED9LF8Gl2lXPLmGgwuSqz7G-b00t_aFhvFMWzsBuIsEl08JYBpA8TomP_DJFHyDR9AvfJimiMqJzxS1g0OTLdp45s2XPTtiHoiXBR663hvkEMQVqFGJi8QL8YB3GKdIH_6EpHM4QxwnUjvOkXBvzPnIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33ea57fb3.mp4?token=gDa_MkHDcRtbh97TI8cTfA2CeuzmFDscXu_Q6s0nCjqvuytKTMc4dDcI5L0j2rAhe7Pv_ITbFLooyELGoaxBReQMcW391OCuM6MY4pI77zSzJZz_fQ-VIDW5uowvMN2IyCeOqNQ1LbvmcHiWxVkyIlraDgzs6zHvw3MqHoG6sPr1GhKW4MLCOtaIpKrIPKED9LF8Gl2lXPLmGgwuSqz7G-b00t_aFhvFMWzsBuIsEl08JYBpA8TomP_DJFHyDR9AvfJimiMqJzxS1g0OTLdp45s2XPTtiHoiXBR663hvkEMQVqFGJi8QL8YB3GKdIH_6EpHM4QxwnUjvOkXBvzPnIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: نجري مناقشات جيدة جدا مع إيران  مضيق هرمز "سيُفتح قريباً جداً" أو ستتعرض إيران لضربة "قوية للغاية"</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86989" target="_blank">📅 06:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86988">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6627805129.mp4?token=ARRVKAaHBtwS3tKK4ZYMNjj4EXSECNJ0S3eyjCi8aTy_DP1RoAmiSoObLtSb2XyDf_iX1R5HBp-yWYwo97utNL6S7103OqqHou4kmurD9FGRDM5RFhayur2yIBxpAklNFDBt8FhLj25tJ-e9qkhmzeOJbjjHdDFGcabdzW1XPtVQse-sOXOxTd_lquxnTGRm0frTTS44xnczJTlh7r1s-MEgLWiJ6gFgJUgbY0FDtozxiR_NxwMksr2X17rbmMBLR36B6TCJGo_XW3FfHE7f4r_ACQNA4feAmj7DWfdFAS80svUypym0uGCRXFybz8beEtmUKN561Z0BuqoWv69UzBzUNw4SuKLmMql6jPr__FGijOJ8ld77k6_8k3jxZGWPkg74-33BLM1lTSSXvO9RBXiTbh4soXuj1el38UN814JLhzhioPTP6q8oRsnO2OsqThH8b0i4iSxHLH3oSxSLfWS0IgZbGTj4zsDJLiOLuy8ZBZWoimXPWpGttQWjiTFNdGcEIEbyOJEri8PewO9Q5joJT-5FP5HDv06GRzygrVpXsxCXx-DEwzu_DK93cPAuPm6No1n0EfZDuTeJQnyMzs2JLOcjS6_WGRIaxrJHU5wRpkQL0yEA55VfZnHLt-9B9luDvzPefMNi7yY3g2QV3f3WrQqJ8k3BeflizHuulrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6627805129.mp4?token=ARRVKAaHBtwS3tKK4ZYMNjj4EXSECNJ0S3eyjCi8aTy_DP1RoAmiSoObLtSb2XyDf_iX1R5HBp-yWYwo97utNL6S7103OqqHou4kmurD9FGRDM5RFhayur2yIBxpAklNFDBt8FhLj25tJ-e9qkhmzeOJbjjHdDFGcabdzW1XPtVQse-sOXOxTd_lquxnTGRm0frTTS44xnczJTlh7r1s-MEgLWiJ6gFgJUgbY0FDtozxiR_NxwMksr2X17rbmMBLR36B6TCJGo_XW3FfHE7f4r_ACQNA4feAmj7DWfdFAS80svUypym0uGCRXFybz8beEtmUKN561Z0BuqoWv69UzBzUNw4SuKLmMql6jPr__FGijOJ8ld77k6_8k3jxZGWPkg74-33BLM1lTSSXvO9RBXiTbh4soXuj1el38UN814JLhzhioPTP6q8oRsnO2OsqThH8b0i4iSxHLH3oSxSLfWS0IgZbGTj4zsDJLiOLuy8ZBZWoimXPWpGttQWjiTFNdGcEIEbyOJEri8PewO9Q5joJT-5FP5HDv06GRzygrVpXsxCXx-DEwzu_DK93cPAuPm6No1n0EfZDuTeJQnyMzs2JLOcjS6_WGRIaxrJHU5wRpkQL0yEA55VfZnHLt-9B9luDvzPefMNi7yY3g2QV3f3WrQqJ8k3BeflizHuulrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: نجري مناقشات جيدة جدا مع إيران
مضيق هرمز "سيُفتح قريباً جداً" أو ستتعرض إيران لضربة "قوية للغاية"</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86988" target="_blank">📅 06:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86987">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">استهداف سفينة في الخليج الفارسي بالقرب من مضيق هرمز والنيران تشتعل فيها</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86987" target="_blank">📅 05:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86986">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم روسي جديد على العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86986" target="_blank">📅 05:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86984">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Udi1LJFk5wnR51Cc4i9z1dSMN3nGrhwKHt0gJ7zzCJOaMUftEZ4Y_q3Ww6PptSelu0iw9QaTybBA78pahsm0vHlnzelClBKogHnAaI-ya_zVcb9LWakSGM0RtA6SAuklwXxRGx6yES6nh7IdPIVKBjVGp1mkBpkkyLtVHeyK13dMM4dHj-vCatMPztdU1sjGRAgoeTYy5-93vibg9wB9_rmVP4Yxp73-OVsVat8yZYVtFHEJxS9kc3UAVYRREikH8FvQz8zs3XVMI6y7GklKRSeeIeWDl_P_JOYuM9E1tD_P8XTOftDkdnHB7pzs1uc73Mr1N4e9wyhrCaDBriyTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3MScKthhRZwcsEAoKHDTfm154pafMRzWp9oVmDibVmpB08Dp5LqQgakTMaHhtPYT1GeBCvt-QAVcWRqxqO2O4jR05yHMo2o2TeGyCou_Ysf2_uLlvkoBUqbnDZdKx3FqllzYDUUztEoEPmwh0QjIEqeiFBdiQ32YPTFagrYFYNlnIKUmAf4hmlyoslwM13wLFt8bVP2IWNKVCS3YBSLT7pFhffdKKuD0oW-5a67W6aZIsMEapzBSnW8p--N54uw7l7FcjUyKUyz54mNYyZbGXTVlEtpeE8_oDjnJrW1zMILKxhqzNsednYGhuN0cLDahX8dTysJF1YwarkaqqqmIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حرائق وأعمدة دخان واسعة تملأ سماء المدينة الصناعية في جبل علي الإماراتية</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86984" target="_blank">📅 05:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
وول ستريت جورنال:
مسؤولو الطيران الفيدرالي يراجعون حادثة تتعلق بسلامة الحركة الجوية وقعت الثلاثاء وشملت مروحية كانت تقل الرئيس ترامب.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86983" target="_blank">📅 04:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86982">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e07ecWV4lHxejguKMnstItEFHVFeK_V9PMXlrCb7ntRk7abF-hEgMKvl5a-2-0FB_AawQyN0-dmtvmKp3CwgVOpHlUzMU2cPxRme7IAFvjVN-IQHL5OBFCvQ9ieBGivBADYu4uzZ59gPMiOtitBkGQqsc_OqBYIRhbXBfChvWzx2U_LsQ1eyVPVUhOb7SzgSTi_0Ia1gFVEb6vApMWvw36unBa1Gi9kmc6usbmdQj4wYnJpQX1YylkMh89BabI6_USK9fQN0MfUu4hJbJnDOuuYSu9KsK_LWo0sC_9RooQhaQZtkzAYPbrmuK1Kem3OgqMdGhniiehWOSoVRBMXvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشاط لطيران مسير فوق اجواء قطر والبحرين بعد الانفجارات المجهولة في دبي</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/86982" target="_blank">📅 03:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ارتفاع شاخص درخواست "کله پاچه" در خیابان فردوسی تهران.
فقط آمریکا نیست که از طریق میزان مصرف پیتزا، نشانه‌هایی از جنگ را تشخیص می‌دهد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86981" target="_blank">📅 03:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86980">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViIktsoEHFv6DqR8ZihDM9U1oOP_pAouWbtWZWlFLTZduZfiqlL7pF3gtjjgn5aN-V7p65S1qH02y7ZB94IFzHAA2Tjn6HgevKuF1oNgMptmpA_fhCf82ch-o31riD9c1xEnDRSCxGm-S5eT8ZeAOh9dqqIzUOI5b6UJyb8HD5FpN3YicG3fY48ttY2-KM1bxi6599dg7SWFu5io1J1hhSiASm0pngeWI5OKHzEupv2GE0gYPHlBIqWiI8I8SQe4K6quQOC-Ncs8K-Z1mUyXjHPWD5C81n1ejllhOMAhLpCk3-gVaBNxPsV8NY8nxQXDcF7GvcDLmzkYTJs__PM6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇪
Whatever happened in Dubai, and who was behind the attack, one thing is clear
the outcome suggests that no U.S. air defense systems nor NATO air defense systems were able to intercept the attack. It also appears that the United States is facing a significant shortage of AD missiles, as Reuters reported today.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86980" target="_blank">📅 03:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86979">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60051ef060.mp4?token=sXzjwozz_w3IbJ81UlIRL5TM7PMWEeOVq7mf26oItTZI8FWhzUz2s6nbjrbgn9clnSobo9QVTsbQDjbdGhK0n0ivpp1GwbV42SrAGeJPauIYQtujydfbKix-8Jl1d5FnMNmeA1wHKs1urCl2yM1L_cx1pCC9u-PABbNbvupywNE3e-d-p0AEdwthHZFLACNQOPE9TWTv5Mxo8uidp4QlrTurs9CpVo4F_VtKS2WXNjUgXyITPdB3-FkcvpnOeTFE3_mh0kl1x_jev6bI5CKQmBVwSDGhTmsn-5MKTDAuPTY_Mczc9tdPFJKQLaNqje-lYsn1_Y5HzBAU9ZnXlUO5Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60051ef060.mp4?token=sXzjwozz_w3IbJ81UlIRL5TM7PMWEeOVq7mf26oItTZI8FWhzUz2s6nbjrbgn9clnSobo9QVTsbQDjbdGhK0n0ivpp1GwbV42SrAGeJPauIYQtujydfbKix-8Jl1d5FnMNmeA1wHKs1urCl2yM1L_cx1pCC9u-PABbNbvupywNE3e-d-p0AEdwthHZFLACNQOPE9TWTv5Mxo8uidp4QlrTurs9CpVo4F_VtKS2WXNjUgXyITPdB3-FkcvpnOeTFE3_mh0kl1x_jev6bI5CKQmBVwSDGhTmsn-5MKTDAuPTY_Mczc9tdPFJKQLaNqje-lYsn1_Y5HzBAU9ZnXlUO5Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احباط محاولة اغتيال ترامب</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86979" target="_blank">📅 03:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86978">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4142b08e04.mp4?token=u8z3gILtLsp02mGZg-Lfp51bTukwgv3-1GNHPctznug97VwUlPGD9qla3qYwkGMxfB5dBphubPpCTELymDY6Et2UxmkueMPUZFkAEm_Wys8nxspzQNX1zplbyC4LBzFsqnEGM7yyPQhwpI5fSGSRiRfDYbg8yXX4YjMHPDogT-rOqh9x1inqnDd2NAMrRW8zkLzfQnfbx68RQhvzFQLKZ6zqpjIuz3Hv273anSeSHTTmRt_zFBMQZI2A3o8a2CV9a2T_5wG9Qt9u59iqf9liCt97G0OgovdW81qHvWrM7wBoo02a1ocv0CauhNI1P6QZjyuPGHSPx6JIcc9nfSgSvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4142b08e04.mp4?token=u8z3gILtLsp02mGZg-Lfp51bTukwgv3-1GNHPctznug97VwUlPGD9qla3qYwkGMxfB5dBphubPpCTELymDY6Et2UxmkueMPUZFkAEm_Wys8nxspzQNX1zplbyC4LBzFsqnEGM7yyPQhwpI5fSGSRiRfDYbg8yXX4YjMHPDogT-rOqh9x1inqnDd2NAMrRW8zkLzfQnfbx68RQhvzFQLKZ6zqpjIuz3Hv273anSeSHTTmRt_zFBMQZI2A3o8a2CV9a2T_5wG9Qt9u59iqf9liCt97G0OgovdW81qHvWrM7wBoo02a1ocv0CauhNI1P6QZjyuPGHSPx6JIcc9nfSgSvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار تصاعد أعمدة الدخان في المدينة الصناعية بجبل علي الإماراتية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86978" target="_blank">📅 03:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86977">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بعيدا عن حرائق كييف ودبي
اندلاع حريق قرب مقتربات المستشفى الإيطالي بمنطقة الجادرية بالعاصمة بغداد .</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86977" target="_blank">📅 03:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الصمت يعم الإعلام الإماراتي</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86976" target="_blank">📅 03:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_MmkWvPbe4c6Nnmi1y4T1vSt6-ahhOrWer2GRxG6iwkH8ZQzkq2u5ITOa5LjmcC9CIRz-n_c6U9qhq3bGlVGbBExkmYDHRV8F4ckRXzCCJ804jYfJwyiBF0EANbSKhbllcTviXf4IgeGubaiHU7442H4WHFHn5PeN4zpmH9g-YgpgszhzZXS2W2LTDrq39KtVIl0IXppHZiRXfamqmpgJVuMTwe5tM3s5AZIvAOAFdI6edMaB0RflZym748wCL2dXm-YTF2U0A_OIVdzT-HVgFWLR9jOAShhjJAnkE8ARDK-3BhAYT71BPgC3WMtREJsDw8j3k3Hcfr6kN810URdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناسا ترصد ارتفاع درجة الحرارة على ما يبدو حريق او مصدر اشتعال من محطة غازية عائمة قبالة جبل علي !</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86975" target="_blank">📅 03:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارات تهز سواحل الإمارات</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86974" target="_blank">📅 03:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86972">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNR2d24z0tcSyOiCJ05JA0fdFV0x0JGQyXtl9_LPb6GWVpAwwdIlblVldtZAGeXKRUoAwHO4dsAqYo5DGSSVc5YtbFodyFFsUWni7uKcR2BjBf0LOUQGiT48xP_NNVGLMeTt77Q8LcidhqkV6wvOHl60ABrCP5LxwZQw668J5KTFOO4QeN16JRuN3aB0b2x0XDok1ihrGUYsxL8c6Use77AflI7aUw2YCbE_mfPa9Svrlu0UCp3tLr3KzlJ7fhQWo7yBJ1SXJU7h5xdel5UBs5AmOmPhIizo9m6n4bAjKVxVbuu-Ra2nmQNm6wrMV3n-WNUgkCzcilW0a1MKPllbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمار شامل في المدينة الصناعية بجبل علي</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86972" target="_blank">📅 03:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86971">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86971" target="_blank">📅 03:21 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

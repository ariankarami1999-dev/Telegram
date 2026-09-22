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
<img src="https://cdn4.telesco.pe/file/JnnyQkrRsvSzmDSq3Yg4SZ2waZAhmPUCKbSB-GByg5_h1fM3AbpLE0W69bFXxwtC-qBcr3Yu7krB38k5q6u-BKxKaHkpfm6vp4y9miekcmSGlEojIf6pEm3vzYRDLw-n1axQ-r3LvgxEZ0hVJdTsLT2Dnl7E-V6vhBjh4PzTTpt4lP1Fd7UCWkM1VD67a3zW0IuvYByI1KVAXk8bECbsMUbvpER2NC3qoM7N5iVL_WDqh0JXmDYr45wB1pr8zeAg0zn41DSK3u4HKm-WPQlmMJVGjt4yiaQMaFl_lWWgOD-jTugRt90cJKkbjgIOo2f5Q_DaU2txLegRZ6UpC1lAPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-91267">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cdd28462e.mp4?token=f7-coSM_GOHTalqSWfg5uUYmyRMdGZYVL9LYBsD9QbiitT1s33fn2MLzUG4XpJ7pLXpu8a_K0fIcaNf3o9jBDLDbEhSaTXKdzsievGafajnGR7eh3n1WQZhamnb2iblMl2gkUcwsc0o7F_ucFhd4ri9zTVL4GiwWWfh2LLB_dLd2iWAcvVGMSa3sjjn_LFY0tgaXWRMpRfHHDohwMZrKqz-kJehOHleopDqNBgc3AqxtFxTU8drAgQi-miv_6jsDAceujkHqWM6IZmYJII8DofGSrxIqVRnr6rYlUmC-InvkEeFZQs6P7ofW4ut72eTFBSPGl-gAgoRwaPMG1bsiral4JwTwlm5-NLVA0FfPCFLoTwjFaMM11vlX78heyeFUFaFMfz4uT2YocHI_NMW-YwQ0yR6SDibZNBoWxkUOu9bwumAZ47a-QwLg0qgzUlUMyQxSeMwjm3rRoAtxfh8TCZhMbKq3xrVKjMvWfu0yZRapbuCdRFdwAntPwNL-ONEo9k_WFiGxMDXdJSW1_AQX77Kdld-x7OH27BWZNJovpwK1mFeswp56a-S4gPkQsZ_bTKrKHKVBujHqe2-XOktjCplQqVaHNRlHIDvpNtkzBi45XazOkyGyNE7l4d5jXBzgppdkchEN915NYNpAKlMiHEKiSLrR-T4wjYyNBgCYtic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cdd28462e.mp4?token=f7-coSM_GOHTalqSWfg5uUYmyRMdGZYVL9LYBsD9QbiitT1s33fn2MLzUG4XpJ7pLXpu8a_K0fIcaNf3o9jBDLDbEhSaTXKdzsievGafajnGR7eh3n1WQZhamnb2iblMl2gkUcwsc0o7F_ucFhd4ri9zTVL4GiwWWfh2LLB_dLd2iWAcvVGMSa3sjjn_LFY0tgaXWRMpRfHHDohwMZrKqz-kJehOHleopDqNBgc3AqxtFxTU8drAgQi-miv_6jsDAceujkHqWM6IZmYJII8DofGSrxIqVRnr6rYlUmC-InvkEeFZQs6P7ofW4ut72eTFBSPGl-gAgoRwaPMG1bsiral4JwTwlm5-NLVA0FfPCFLoTwjFaMM11vlX78heyeFUFaFMfz4uT2YocHI_NMW-YwQ0yR6SDibZNBoWxkUOu9bwumAZ47a-QwLg0qgzUlUMyQxSeMwjm3rRoAtxfh8TCZhMbKq3xrVKjMvWfu0yZRapbuCdRFdwAntPwNL-ONEo9k_WFiGxMDXdJSW1_AQX77Kdld-x7OH27BWZNJovpwK1mFeswp56a-S4gPkQsZ_bTKrKHKVBujHqe2-XOktjCplQqVaHNRlHIDvpNtkzBi45XazOkyGyNE7l4d5jXBzgppdkchEN915NYNpAKlMiHEKiSLrR-T4wjYyNBgCYtic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الكوبي يغادر قاعة الجمعية العامة للأمم المتحدة أثناء كلمة ترامب</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/naya_foriraq/91267" target="_blank">📅 18:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91266">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامب: كوبا ستسقط. الحرية قادمة إلى كوبا.</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/naya_foriraq/91266" target="_blank">📅 18:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91265">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامب: نحن نعمل بشكل وثيق جدًا مع قادة روسيا وأوكرانيا، وسنحقق ذلك. أعتقد أن هذا الأمر سيحدث بشكل أسرع مما يتفهمه الناس. لقد انتهى الأمر.</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/naya_foriraq/91265" target="_blank">📅 18:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91264">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الوفد الكوبي يغادر قاعة الجمعية العامة للأمم المتحدة أثناء كلمة ترامب</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/naya_foriraq/91264" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91263">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
🇺🇸
ترامب:  لدي قرار كبير يجب اتخاذه. هل سيتم التوصل إلى اتفاق مع إيران يسمح لها بإعادة البناء وخلق دولة أكبر بكثير مما كانت عليه من قبل، ربما واحدة من أعظم الدول في الشرق الأوسط أو حتى في العالم؟  أم هل سأدمر الجمهورية الإسلامية وأفعل ذلك بسرعة، دون إعطائهم…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/naya_foriraq/91263" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91262">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزارة الطاقة السعودية:
تعليقًا على ما ذكره معالي وزير النفط العراقي، باسم محمد خضير العبادي، ورئيس مجلس الإدارة والمدير العام لشركة تسويق النفط العراقية "سومو"، المهندس علي نزار الشطري، خلال جلسة مجلس النواب العراقي، بشأن قيام المملكة العربية السعودية بشراء 25 ناقلة نفطية وربط ذلك بارتفاع تكاليف نقل النفط العراقي، أوضحت الوزارة أن المملكة لم تقم بشراء الناقلات الـ25 المشار إليها، وأن هذه المعلومة غير صحيحة، مؤكدةً أن هذا التوضيح لا ينتقص بأي حال من حق المملكة الكامل في اتخاذ ما تراه مناسبًا من قرارات تجارية واستثمارية، وفقًا لاحتياجاتها ومصالحها
‏الارتفاع الحاد في تكاليف نقل النفط يعود إلى عوامل تختلف عما أشار إليه وزير النفط العراقي والمدير العام لشركة "سومو"، ومن بينها التصعيد العسكري في المنطقة، والهجمات الإيرانية المعلنة على السفن، والاضطرابات في حركة الملاحة عبر مضيق هرمز، وما ترتب على ذلك من ارتفاع حاد في مخاطر الشحن وتكاليف التأمين، وتراجع أعداد الناقلات المستعدة للعمل في المنطقة.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/naya_foriraq/91262" target="_blank">📅 18:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91261">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامب: سنحيي الذكرى الثالثة للهجوم الذي وقع في 7 أكتوبر في إسرائيل. لقد قام إرهابيون مولتهم إيران بتعذيب وتشويه وقتل 1200 مدني بريء، بمن فيهم العشرات من الأمريكيين. وقد احتفل المرشد الأعلى الإيراني بهذه المجزرة ووصفها بأنها "خدمة للإنسانية".</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/naya_foriraq/91261" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91260">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eed65c16.mp4?token=rkGsGtFznvOtr7Nh4K2U8onBhP7LMUCGeP5qSdFKh8qIskKqjYLcXK3CaIgG0yI-9sd9cfmro8_9dPeluv5GRJ9j7xXoMnm0cAP434J_yT9QkPuplxAKyzGEpx0Isyiow7I7S6qr5Adk6rpLA6uxEP5hO9aOrjbBeeu5bzcp-PwYt6iQ1ms0fX98iEsKNYroUuYAqqW0DptuYFeXc2mPYvkKhCc30AVVfIIv6EeODj36-_ne7NYkM1FxuiHyQs_Pg5_in-_BmrNyULGGNUcxF1q3wqRW7_AkB0Pat9AklZaLE51y-Zb0DILE2n1NJWFoaJZqglsK93QAGI3o0EpZS1lTOxej_NyWE6tqlBSOtVSTgPy3P7LfhT8HJBjH59ciRImYJaf5KL54hDEhrMLgOMWs46pPkTD4_DOHrJ9yMiPbQsMOfYrCWGwWQ9tIi0i5PQDQ4AS9b0m39DRT92SMKLc00qRjjBIcgJfeCizfff8rALba7zL-ZuYMOKU28BsR1SWkdN5CdJS4eM0At-ZLPR9fA2oHCJHzCpdZBsB0fnqB_C7ta_zBCJOK3Tqq5EfTo3e9GbqUYcQgSswBW_xyMw_mkJmo_bYNoxfDd9JGr0cgS7Q93ctSsIwx0GKPtWMcyT9GtbQRg-yrOmL45_LtNHyl_OBU_VfuXsyxEWKPEzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eed65c16.mp4?token=rkGsGtFznvOtr7Nh4K2U8onBhP7LMUCGeP5qSdFKh8qIskKqjYLcXK3CaIgG0yI-9sd9cfmro8_9dPeluv5GRJ9j7xXoMnm0cAP434J_yT9QkPuplxAKyzGEpx0Isyiow7I7S6qr5Adk6rpLA6uxEP5hO9aOrjbBeeu5bzcp-PwYt6iQ1ms0fX98iEsKNYroUuYAqqW0DptuYFeXc2mPYvkKhCc30AVVfIIv6EeODj36-_ne7NYkM1FxuiHyQs_Pg5_in-_BmrNyULGGNUcxF1q3wqRW7_AkB0Pat9AklZaLE51y-Zb0DILE2n1NJWFoaJZqglsK93QAGI3o0EpZS1lTOxej_NyWE6tqlBSOtVSTgPy3P7LfhT8HJBjH59ciRImYJaf5KL54hDEhrMLgOMWs46pPkTD4_DOHrJ9yMiPbQsMOfYrCWGwWQ9tIi0i5PQDQ4AS9b0m39DRT92SMKLc00qRjjBIcgJfeCizfff8rALba7zL-ZuYMOKU28BsR1SWkdN5CdJS4eM0At-ZLPR9fA2oHCJHzCpdZBsB0fnqB_C7ta_zBCJOK3Tqq5EfTo3e9GbqUYcQgSswBW_xyMw_mkJmo_bYNoxfDd9JGr0cgS7Q93ctSsIwx0GKPtWMcyT9GtbQRg-yrOmL45_LtNHyl_OBU_VfuXsyxEWKPEzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أعتقد أننا سنتوصل إلى اتفاق مع إيران بعد انتخابات التجديد النصفي.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/naya_foriraq/91260" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91259">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏ترامب: علي أن أتخذ قرارًا كبيرًا بشأن فيما إذا كنت أود إبادة إيران أو السماح لها بالاستمرار والازدهار</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/naya_foriraq/91259" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91258">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامب: لقد صنعوا صاروخاً قادراً على ضرب أوروبا، وكانوا فخورين جداً بذلك. آمل أن يدرك الأوروبيون ذلك. كان هدف إيران هو إكمال قنبلتها النووية خلف هذا الدرع الصاروخي الباليستي التقليدي.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/naya_foriraq/91258" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91257">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7587284f78.mp4?token=kRHX72Q4U3xSJjhYBu44CmSz4ip6Ahop00p5v96boewiUJGix-SnExRqbo3x1KIHCS-gN3a93cYDUtwWA25fc5AWsQH9idP-EnE0M-UaguwmXdZVMezjPfenwy-VCaOinmWsPBFx6U8YCz6YTFTbJrf75SmgDMiIB7lQZ5HHJJMsbNn8LNpzVpAEfr7QdGWAspI7kB5CR0sj9tJS2ehhNaS_6sOnoMNRqnQd85As7R18R1J8-EdrnFMir31_PeNG4P4XiZoVQNXvuV5H74O5Z8ZsK4PGqaBGSqsKLRb5qYc2_uNcSbAOYgeYeFYzojyQmshzdgpuyZZiiir_48kdfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7587284f78.mp4?token=kRHX72Q4U3xSJjhYBu44CmSz4ip6Ahop00p5v96boewiUJGix-SnExRqbo3x1KIHCS-gN3a93cYDUtwWA25fc5AWsQH9idP-EnE0M-UaguwmXdZVMezjPfenwy-VCaOinmWsPBFx6U8YCz6YTFTbJrf75SmgDMiIB7lQZ5HHJJMsbNn8LNpzVpAEfr7QdGWAspI7kB5CR0sj9tJS2ehhNaS_6sOnoMNRqnQd85As7R18R1J8-EdrnFMir31_PeNG4P4XiZoVQNXvuV5H74O5Z8ZsK4PGqaBGSqsKLRb5qYc2_uNcSbAOYgeYeFYzojyQmshzdgpuyZZiiir_48kdfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أدعو إيران إلى إبرام صفقة</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/naya_foriraq/91257" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91256">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامب يبدا باسطوانة دمرنا البحرية الايرانية وسلاح الجو والصواريخ والمسيرات</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/naya_foriraq/91256" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91255">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامب: هدف إيران كان استكمال السعي للحصول على قنبلة نووية ولو نجحوا لبثوا الذعر والموت إلى ما لانهاية</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/naya_foriraq/91255" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91254">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ترامب: دعونا إيران للتوقيع على اتفاق لكنها رفضت</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/naya_foriraq/91254" target="_blank">📅 18:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91253">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e8def986.mp4?token=l08toiWxN0sRKnuvXzmyty7eiD_sEN35ecrsGVc81CxzxkSxz70YfiOUhqFhNgaaggixYM88CaYLkIrFvogAV89bFsbJ8ooLPNZPbsYvBjlmWFRxd7S_LujbIz3uNCM0ruCcNQahBMg7h8vCeV74VlcG4ArjAjT2u1F-cRFpFiYZbVuKh1VO1FFI8mCQy0NtJ-6My7Fa3Skby0TX8SzkuXtxei2UiYnkt2hISztUGLYkq08dh1wVM8eiaBfD37_EzG7Dxceszn8VTSpxWtkPiwJ86PO53aUGEK_bUKZdjT2moo0vyL391LUAg-jgKv-FEnTUae9ogXhrIFXwf8z14A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e8def986.mp4?token=l08toiWxN0sRKnuvXzmyty7eiD_sEN35ecrsGVc81CxzxkSxz70YfiOUhqFhNgaaggixYM88CaYLkIrFvogAV89bFsbJ8ooLPNZPbsYvBjlmWFRxd7S_LujbIz3uNCM0ruCcNQahBMg7h8vCeV74VlcG4ArjAjT2u1F-cRFpFiYZbVuKh1VO1FFI8mCQy0NtJ-6My7Fa3Skby0TX8SzkuXtxei2UiYnkt2hISztUGLYkq08dh1wVM8eiaBfD37_EzG7Dxceszn8VTSpxWtkPiwJ86PO53aUGEK_bUKZdjT2moo0vyL391LUAg-jgKv-FEnTUae9ogXhrIFXwf8z14A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: تستمر إيران في تطوير أسلحة باليستية</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/naya_foriraq/91253" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91252">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏ترامب: إيران هي الراعي الأول للإرهاب في العالم</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/naya_foriraq/91252" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91251">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏ترامب: إيران هي الراعي الأول للإرهاب في العالم</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/naya_foriraq/91251" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91250">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تحطم طائرة مقاتلة امريكية من طراز F-16 في قاعدة سبانغدالم الالمانية</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/91250" target="_blank">📅 17:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91249">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اكسيوس:
عدة دول وسيطة تتواصل مع الولايات المتحدة وإيران لترتيب اجتماع رفيع المستوى.</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/naya_foriraq/91249" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91248">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇸
🌟
ترامب:
من الآن فصاعدًا، لن تسمح الولايات المتحدة بوجود أي تهديدات لأمريكا في أي مكان في نصف الكرة الغربي.</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/naya_foriraq/91248" target="_blank">📅 17:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91247">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الامين العام للامم المتحدة غوتيريش:
ما يسمى وقفا لإطلاق النار في الشرق الأوسط ليس أكثر من إطلاق نار لكن أقل حدة.</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/91247" target="_blank">📅 16:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91246">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد إضافية من عملية "والله أشد بأساً وأشد تنكيلا" العسكرية النوعية.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/91246" target="_blank">📅 16:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91245">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
مسؤول امريكي لـCNN:
أخبر ترامب مستشاريه بأنه يرغب في لقاء مسؤولين إيرانيين يحضرون الجمعية العامة للأمم المتحدة في نيويورك إذا كانت الظروف مناسبة.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/91245" target="_blank">📅 16:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91244">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجارات تهز مضيق هرمز بعد استهداف حرس الثورة لسفن مخالفة</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/91244" target="_blank">📅 16:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91243">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏
مصادر حكومية عراقية:
لا قرار الى الان بمنع الطائرات الإيرانية من استخدام المجال الجوي للبلاد او الهبوط بالمطارات العراقية.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/91243" target="_blank">📅 16:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91242">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6lwNHOBWy-2M5U9jdSx_-XVigyWwoGujuAVY3eT4lPcAIOi4hRLYsCbT1sMqkAUU6RoDQUMZGofV3yioglETLZn0-MG74pfBRbGp5QG18WzpHTAwivBPTZLu_gFVCXyqCFBlQ0um_p5_qUdBiM36WMoj8seFiEzh3KmoHlmKU15lji5H8JuwkAfrmhRDnDoAp34s8Fo2Y21NSI_gVLyCYrsO8Kx_C4HUl3fXozfs_6y1NyZ5bQ1lNEdyf2cm7XsWDDoLe-e3E4OAebjY4Vjmv4iGxLWsYC_nyNkYIOS8Q0QrFNKGfoFrWF-zg1_heqN7KhbIzQH_evSpYKGZoGplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توقف تقني لطائرة الرئيس الإيراني في الجزائر أثناء توجهها لنيويورك</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91242" target="_blank">📅 15:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91240">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
دول الخليج تخطط لإخبار ترامب بتجنب أي تصعيد مع إيران، من المتوقع أن يجتمع قادة الخليج مع ترامب في نيويورك يوم الثلاثاء.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/91240" target="_blank">📅 15:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91239">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icG_HRma9X0zumpp4HFQVturyZ-IJmLMxFmYwvHP6omf_rL7y9DSTGvne0-SAi2Y41lYHkkKEIs6kOXDeyd1zam3mUXzfICroPni3_sszoW2iO05n5FHRH7LLhP3mPq_uwWw9tKzDgyun6TJDfUIHM7b-tnPFoyS8SqF_BMupXF5ouyJebUuHwXTQPH-2GDfRC3bKd-s12qnaRvnrXPhT6n413wTY1QY6Y0bD5jmDmZBMf3uYQrc1SWmgzZKHgu7RTmiluA6pEJiY9oD2FXHB3SBAvXZdL1luslBmOfIS-ull2YUGwA_DmUmcbmUNBZcOZ7AoVagMUV1g8LUlbG3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
المعاون الجهادي للمقاومة الإسلامية حركة النجباء عبد القادر الكربلائي:
المقاومة باقية، والحشد باق رغم أنف ترامب المجرم وسمساره الصهيوني باراك، فلن ننثني ولن نتراجع، وسنبقى حماة الوطن والسيادة والمقدسات حتى النصر أو الشهادة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91239" target="_blank">📅 15:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91238">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCuqc8ldBvKMeAB3kH9kzJa0q3tRFl1brKVlaoozOQZ5QXap6MZ9DEiI10uE_9S__uxcdC8MjXDaE10TH8emBoCJxN74ouubJ3C7uPxk0nqByzL8dmECVhfJm2TtfUB-u5mcJvxlBPYGm00ohPtGO-FVlQ3ZRzdBIs4k1ha9VNwDV9YSE1Y0ztmFqOehD7g-yCMtFd-BrH6lo-Y3kyUWaEvV9L_kdnHtGTpDhH3P4N6hnnRNb5rXkcx45-HBq428SpPTBtCcdflgeQDHhhL6WUtaSuXUpIUpKnpJxvWPLNPzsqygvsowuqqmHU_pI44C93KNfHkWXy7w-jBN3C2IGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
ترامب:
الجبناء والخونة سيحبون أن يقولوا إن الولايات المتحدة تعاني من نقص في الذخائر. هذا ليس صحيحًا.
لدينا كمية من الذخائر تفوق ما يمكننا تصوره استخدامًا، ونحن نقوم الآن بزيادة هذه الكمية إلى مستويات لم نشهدها من قبل.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91238" target="_blank">📅 14:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91237">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed350d7bc2.mp4?token=CYljdw8BwOkt_rUFUO_QsdT89MnJ4FYJt3puGDAMrAlPRh_HqO_krkRt5_Sp_nmaL3jDsrTT8OM8iQXUoQ4fTy6niwkWkbk04uKJ3SvMBNnfaXD9z2UlPr4BAeuASPbECtv5IzapUMucfdXwBOBXWQM9xXZb8cbQea4cj1a-6jkmz7PWsE5w7X_hA_nr7op1Icv_8tnFTAarSPRc4ZPGNUmQTij6KlGylJnCYkTDt1FdfSDIwfuBDdZUI2EbWGlTut3v0fnoLogYu6bJ4eVZM8T2ZvJis3HXh308YZUb1vrYjqDBBOTbo8ubmr4B6fXyOCPd_BB_f7SO3h89cxGwzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed350d7bc2.mp4?token=CYljdw8BwOkt_rUFUO_QsdT89MnJ4FYJt3puGDAMrAlPRh_HqO_krkRt5_Sp_nmaL3jDsrTT8OM8iQXUoQ4fTy6niwkWkbk04uKJ3SvMBNnfaXD9z2UlPr4BAeuASPbECtv5IzapUMucfdXwBOBXWQM9xXZb8cbQea4cj1a-6jkmz7PWsE5w7X_hA_nr7op1Icv_8tnFTAarSPRc4ZPGNUmQTij6KlGylJnCYkTDt1FdfSDIwfuBDdZUI2EbWGlTut3v0fnoLogYu6bJ4eVZM8T2ZvJis3HXh308YZUb1vrYjqDBBOTbo8ubmr4B6fXyOCPd_BB_f7SO3h89cxGwzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتن ياهو يهاجم ممداني:
عارٌ عليكم، يا سيد مممداني. عارٌ عليكم لدعمكم لوحوش حماس الذين ذبحوا شعبنا. عارٌ عليكم لإثارة الفتن والاضطرابات ضد اليهود في نيويورك. سأتوجه إلى الأمم المتحدة. سأقول الحقيقة عن جنودنا الأبطال، وسأقول الحقيقة عنكم.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91237" target="_blank">📅 14:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91236">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي: لا أعتقد أن هناك أي ترتيبات حالية لاجتماع بين ترامب ورئيس إيران ولكن ترامب منفتح على الاجتماع مع أي شخص.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91236" target="_blank">📅 14:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91235">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
وزير الخارجية الامريكي:
لا أعتقد أن هناك أي ترتيبات حالية لاجتماع بين ترامب ورئيس إيران ولكن ترامب منفتح على الاجتماع مع أي شخص.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91235" target="_blank">📅 14:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91234">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة الرابعة عصرا مشاهد إضافية من عملية "والله أشد بأساً وأشد تنكيلا" العسكرية النوعية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91234" target="_blank">📅 14:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91233">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
🇵🇰
‏
مصدر دبلوماسي إيراني:
باكستان لم تحسم قرارها بشأن تعليق رحلات شركات الطيران الإيرانية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91233" target="_blank">📅 13:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91232">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">السعودية تعلن استئناف تشغيل خط أنابيب النفط الذي يربط بين شرق السعودية وغربها</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91232" target="_blank">📅 13:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91231">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
🇺🇸
مسؤول إيراني رفيع المستوى:
- طهران ترحب بعودة الدبلوماسية إذا اتخذت الولايات المتحدة خطوات ملموسة.
- وفد إيراني موجود في نيويورك بصلاحية كاملة لإحياء الدبلوماسية مع الولايات المتحدة
- تم تسليم مقترح إيران إلى الولايات المتحدة عبر وسطاء في السادس عشر من سبتمبر.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91231" target="_blank">📅 13:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91230">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇹🇷
🇮🇷
شركات الطيران التركية "طيران تركيا"، و"بيغاسوس"، و"إيه جت" تلغي جميع رحلاتها إلى إيران اعتبارًا من 21 سبتمبر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91230" target="_blank">📅 13:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91229">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
قائد القوات البرية العراقية:
القائد العام كلف رئيس أركان الجيش الفريق أول الركن عبد الأمير يار الله بإدارة ملف سنجار وفرض السيادة الأمنية الكاملة وأي مسلح غير عراقي يجب أن يغادر سنجار ولا يمكن قبول وجوده</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91229" target="_blank">📅 12:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91228">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اوكرانيا: استهدفنا مصفاتي نفط في أوفا وسمارا داخل روسيا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91228" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91227">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ول ستريت جورنال: ‏أنفقت السعودية أشهرًا في إعادة توجيه النفط للالتفاف حول مضيق هرمز. الآن، يضطر ملك النفط في العالم إلى العودة إلى الممر المائي الذي كان يحاول تجنبه.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91227" target="_blank">📅 12:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91226">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇾🇪
رئيس اللجنة الوطنية لشؤون الاسرى في اليمن:
قام النظام السعودى المجرم ليل أمس باستهداف سجن يضم أعداد من الأسرى في  مدينة الحزم بمحافظة الجوف مما أدى إلى مقتل 9 أسرى ممن تم أسرهم في الأحداث الأخيرة.
وسوف ننشر لاحقاً قائمة بأسمائهم.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/91226" target="_blank">📅 11:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91225">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
🇨🇳
🇮🇷
الصين تعلن معارضتها للعقوبات الأميركية على شركات الطيران الإيرانية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91225" target="_blank">📅 11:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91224">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j83WX-67jBfTFiS93-NRw7dPiRRIOf-XVJugsIJvojAkjKWan76Va7UQd8NI9gTTgryBLHK5bVtZugzCpxXFC1KJhfgtaXroE-w3X2lw8aoIdgk0QS3IIZ_qNRiPyr4bSmH6ACNX2ldeBLCY_94tNCJ0UjTXz15zX1zO_O_Vl0cv_7LsdPPaEuxLmynPmlN98XAhneEA4rgIvIeZOSmT6NJfwlFHMhGEkDRgdhQHsaJgyiRRjiNmoEXn3iePJADcvdxM_XIWZs8ki_IJoZ7kv1r6xsKUJyiT8xHaX7rLkWdkGBpNsqr1CjQAR43FaipR9sKAQdosxEPLblZFPEsf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
تفعيل الدفاعات الجوية في نجران  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91224" target="_blank">📅 10:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91223">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇸🇦
تفعيل الدفاعات الجوية في نجران
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91223" target="_blank">📅 10:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91221">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyfH0oUaVFw5vSpbBSA-D5jiBQtMBeBKfefzLworbuD4tiPbjRu7gExb7MXRCJKNPqoMCvvw3xBM1Yr4G7bP5YkDN-TdFMpXUOWdFFpf_Fau3i4nVJUV3mvExW2uWs3a0KE6coZA-74K37AC0yDTdTMt1K5hiA_bQCNbmKrRMMKcCTa2vU3LPKyWFpbt-Mpj-ciZ-mgJ_HSXmrGbLG4O-oduG4zXMB35ltXhmzkvVprch4KljdapgLFbsXHZZVj0UGWUy7S4uC5nfTtePoOzge3ECJPRXH0WDxjMX3s9EFEq1ZG0A0Iif9soSQDnKLBAEAWvDwv92rk38QhR5_bw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إرتفاع أسعار النفط العالمية حيث تجاوز سعر البرميل الواحد  102 دولار.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91221" target="_blank">📅 09:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91220">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي بعدد من الصواريخ يطال مديرية الظاهر والمناطق المجاورة ضمن محافظة صعدة اليمنية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91220" target="_blank">📅 08:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91219">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي لأنصارالله "حزام الأسد":
استطاعت الأجهزة الأمنية، بفضل الله تعالى وبتعاون المواطنين، إفشال عملية إرهابية حاول نظام العدو السعودي من خلالها تفجير دراجات نارية مفخخة، واستخدام انتحاريين لاستهداف بعض الأسواق والمساجد في العاصمة صنعاء.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91219" target="_blank">📅 08:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91216">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYU8ZZgoTOk9sWLoPWBRRPFJWXTLOK-G1o2xDJZsyFEr3R2qKi8nQ4_PLQlTjBmMtljbt39JiimA_zIIRMTar38ht38yjlp6JVJef7OiPRS4pPcBbTYRqX82kFa5TaH59RvNIEh3CzAz8cVDzAErqXOntOFU2PLVLiOxzbCIYBiy0nkvlYw23Fd3dJMBPcKfEEBmlOnzoWqk1R9rAL3hJNxr_6eajAqhpYhrq5rXfQ2saeqaSnadVg0uTiqnE8QSHzw_jN5wpzD3P0oZgEBbL53vpsePOK_-LU_EjK-rj10Qw1pG7l3pNcc-zoAUIizXLkcU8QZF79SlhMfzrzOsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e0df582f.mp4?token=qmscbAi0OQ6tTclcxrcax6MfEzW8PdcSvh13MAq0sj6PslpaRENS_vNJqA1C2JJsp9EYNw5WWAaZzdYIzMjA8CYr_QGBc7QptYAcIYZgrZn6KbO0mni1paAsk6nNm2iJAVN4JVtk-3oyN_WxbQdX1X835oW0uO0svC47JSbp4NoP5vyYJVj1bIbfggdwM2lIscz1jqJLLMjVRbmL_-6uF9_eWaEJspIMeEyaGJ7kkNDiGYq7aE2os2sv9KGDViYCcrF55I6fZjN4m2CFBavF7IvgRkcU2ATXxkYYkwHNnNOZCSLJAq7KYLGaSlD1ABjvRSvKCrZMusFP2m__cWmWtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e0df582f.mp4?token=qmscbAi0OQ6tTclcxrcax6MfEzW8PdcSvh13MAq0sj6PslpaRENS_vNJqA1C2JJsp9EYNw5WWAaZzdYIzMjA8CYr_QGBc7QptYAcIYZgrZn6KbO0mni1paAsk6nNm2iJAVN4JVtk-3oyN_WxbQdX1X835oW0uO0svC47JSbp4NoP5vyYJVj1bIbfggdwM2lIscz1jqJLLMjVRbmL_-6uF9_eWaEJspIMeEyaGJ7kkNDiGYq7aE2os2sv9KGDViYCcrF55I6fZjN4m2CFBavF7IvgRkcU2ATXxkYYkwHNnNOZCSLJAq7KYLGaSlD1ABjvRSvKCrZMusFP2m__cWmWtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي واسع يستهدف مدينة دنبرو، ثالث أكبر مدن أوكرانيا وأعمدة النيران والدخان تتصاعد منها.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/91216" target="_blank">📅 04:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91215">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇸🇦
🇾🇪
بنك الأهداف السعودي في العدوان على مدينة المخا اليمنية.. 6 شهداء و8 جرحى من المدنيين، بينهم أطفال ونساء.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/91215" target="_blank">📅 03:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StwTKjVGaPjYzanCXyxD_xwNtiBrXi8ZNZ25Thh752OiBD-M0ePIee_DcNhK0WsYD0Jkt-YbwGORF3dFs_oxzh9w3eK07z7yv5Kf4dS_QAY6z3gUjK8jivIwYJrepGsdhwNFYhMUqFL5FKgrXBr2t51l-8Z6FXI7za4ht0_rHt061fyCobNddefi_dul3ApHSGZ48rOoJaHfQPZbYjVUCAi0JfGNibr79_-PvdhWD-TA9JcEyxoL8tvk-iO2fmw-zkDa8r404wGQFblI7Dk_wDKK8FhMCKDPZQFexQObS6W10lq7FYYzK5sjfWZKbxrd90R5S_uTeM4M9tm_rs5Ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
طيران العدو السعودي يستهدف عدة مواقع في المخا.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/91214" target="_blank">📅 02:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇸🇦
🇾🇪
إندلاع إشتباكات مسلحة داخلية بين مرتزقة السعودية في منطقة زنجبار بمحافظة أبين اليمنية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/91213" target="_blank">📅 02:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91212">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZPoBh3Q5s5dDXzCdiOGVmAQvY5euEyr2rJippwX4VcKo13yjL_Hkh9ELUpVOelioV0uNS5NIAoHjuUuXmXk7THk-CmHYFk6KTTlTe0tGX3GWG5-Ban_0OuAKKG3JKgqiKay2dswnOdaT8GN8M5B6lbjddoYA5kn8J7s2bpsTl6XtrYFObd52jMMbEh1dziuc5Gf3qJSBAkPV9lp-GPvl23Pa1U3gqFe1ArLjDN8CcfDC60c6u97aM5vXchRG-uhK28ZE-B9UJeB7gP5538NKMh_bqTH62D2iwh64ghxYvDwDkV3Yl_C4ACQQNLXbQhb_J2VU--9ymDSUhTqd-E7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
رئاسة وزراء العراق: حصر السلاح سيبدأ بفترة ٩٠ يوما لا تهاجم فيها الفصائل أو تتعرض لهجمات أمريكية، سنعتبر الجماعات المسلحة خارجة على القانون إذا واصلت عملها بعد انتهاء المهلة، المجموعات ستبدأ تسليم أسلحتها على أن تنتهي العملية بحلول 30 يونيو 2027، خسرنا 60%…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/91212" target="_blank">📅 01:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي لأنصار الله "حزام الأسد":
تخوض قواتنا المسلحة، بعون الله تعالى، معركةً مصيريةً مع نظام العدو السعودي المجرم، واتساعُ رقعة المواجهة سيحتّم توسيعَ وتنويعَ الخيارات في اختيار الأهداف.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91211" target="_blank">📅 01:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91208">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsLMzd_S322Jz5dlIP27K6oCsyv3ARWfadaOlg8UHPxsNJeiz5V_ozcIo6VGvOFd00wzaxwCBNP4b3EaOscwYXdxvOdln-QVX8ffuQ6cV3rO5ff_TWmX2ogQidqzwTdE8mxG2y9GSsHcU941M1qEsgWAG-_crvcPmKDID1yvtc9d-Dx_zTmrjqxgaOmVuNz0Acf0BbmKFUnH-vNKrN12FngXaYShOdg9ye37ByBVypKVM7v-nlG8KlUY5x543r4fZyCt2V_xK4LApFFFqqMCbrvvnJeVy_Q8J-jPUwgqRLjROvzU9YK3RogLSOiV4vUwrUSl6V-qCe8Q87cGt3OGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5LHuA-8aYCVeLaXia5ALOD1y4A3KeBSFoR-pvEaiI2hXZFWfe-ulbWJzs_-6eOxM6vUxZwVJwZuo1R2UnsNQgnGYq-fnlc3xsJHzgdWyEdIFBaFuWEalaDtwkk0vOzyk9ke1_2AqhEwFN-NDR9WJsoF1oCP78opMx3WXkhYzknrrJuapEKLsMNUufk4YK8WJXxiuXEQmVQO26jqzCqEwUrDRiHhInKtfwiUAtW4PMcNGf_my6LEGZlYCslDcuivcMcnAeLQvD-xntuhsYqPhPuH91drMq65GeXSJvqca4jTxBKRV8-fRyKQOZUFUn1JJVB2VxNMmJTvchVfdf6XWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibeKVs1fn75m1Mbg5R60XoZ8sTyBvx_CFuWzHpHOLyXqfccUhPYnUcfw_TfjC7L5-JUmQip-BfD-ixB_fkpgzbdf6bifaigWjw3nE59lX8kXcRHTJpGsren2SOrCdu-snNaTmETxu7itVSX8urGB438muMxhW2NKQB8Be8PnW1yve31VGtkMU8KH8VLE-32fPFEbeKuF3Hh230dIwV_FAT7nSfUjrtjbUh--908o6GZZ_b2jRs4fFgPki3pksFo3c1Pnf335jvdi9tA654eXOz7__kJKojxBTsl7nesvfKP7HzyC7IEN572kaB9wGK-GrVLKJ5zPX7ySnmcXAvtr9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علماء اليمن يردّون على مزاعم استهداف مكة
بيان صادر عن علماء اليمن يرفض مزاعم استهداف مكة المكرمة، ويؤكد أن المقدسات الإسلامية يجب أن تبقى بعيدة عن التوظيف السياسي والإعلامي، داعياً إلى التثبت من الأخبار وعدم الانجرار وراء حملات التضليل.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91208" target="_blank">📅 01:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91207">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5c10fbadc.mp4?token=q74dZX_bxswCUjNPL_vht722MY4N_9eMZs7JlsG2w-qFbByezrQiM1e5ntkoFIZ41133DPsVcmSjzgq43sVHb9W1_zv2K3pX-tQ8Hb2tg5llU_sSoMbCjXr-HFfs4FD_jxdOdvJagHrASeaTSrTDgFVopxVduPEwmxfKdU7SBXo03lh_93aA1tDznccm9wy-W44zw8kKv9xuAMgbfvFPaDYIh0UHw_O7IlktS4HmhLqMHPR18-8x3JL8W9Dk2F16111xbaxoMkJTqi30xJ2ZD5kj8Nlt8yBe7piH02CI3hH-vxEEMG7tm5wht4ddLI2jAckW9Eh0d8eBlY9hEdlJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5c10fbadc.mp4?token=q74dZX_bxswCUjNPL_vht722MY4N_9eMZs7JlsG2w-qFbByezrQiM1e5ntkoFIZ41133DPsVcmSjzgq43sVHb9W1_zv2K3pX-tQ8Hb2tg5llU_sSoMbCjXr-HFfs4FD_jxdOdvJagHrASeaTSrTDgFVopxVduPEwmxfKdU7SBXo03lh_93aA1tDznccm9wy-W44zw8kKv9xuAMgbfvFPaDYIh0UHw_O7IlktS4HmhLqMHPR18-8x3JL8W9Dk2F16111xbaxoMkJTqi30xJ2ZD5kj8Nlt8yBe7piH02CI3hH-vxEEMG7tm5wht4ddLI2jAckW9Eh0d8eBlY9hEdlJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های بزرگ و رسمی آمریکا، از جمله CNN، Fox News و NBC، در اقدامی کم‌سابقه، پوشش مستقیم سخنان دونالد ترامپ را بایکوت کرده و حتی از اعزام خبرنگار برای پوشش مصاحبه‌ها و سخنرانی‌هایش خودداری کردند.
ابعاد این موضوع به حدی رسیده که امروز، هنگام سخنرانی ترامپ، نبود خبرنگاران رسانه‌ها برای پوشش مستقیم و دریافت صدای او، انتقال و انتشار دقیق اظهارات او را با مشکل مواجه کرد.
@Naya_Press</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/91207" target="_blank">📅 01:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91206">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇾🇪
🇸🇦
طيران العدو السعودي يستهدف عدة مواقع في المخا.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91206" target="_blank">📅 01:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91205">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇾🇪
🇸🇦
رئيس الوزراء البريطاني بورنهام: وافق على طلب المملكة العربية السعودية بتوفير خدمات تزويد الطائرات بالوقود جوًا جوًا بشكل مؤقت لأغراض دفاعية بهدف تحقيق الاستقرار في المنطقة.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/91205" target="_blank">📅 00:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91204">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0517e652d0.mp4?token=ngcJPL5ScJdmJ8oRGjcen6VnXJT87yUTmb4XGDo1-qpeOg1Jr5Skzp5cfQN5L4G_o1MQYFKsrzX15U-8Vxi8UapPYk7ismTAzHX-w_BG3ws_wM_NZjeTRXkAtexogcVyIv1nliVB5Dpr-EHIfkeYaEC4lSrwWYTeKNCXSK08QuBHmn2HuSf1IMk8ZADTq2e2poCB_GGLdMlOTAsYnnDpHeezLcqtQgPrYdFLb4yUK_LkegRQhbFaKgu21afL-ggrpFQIExEjKbbMUDTNomGVFJmv4kMp9eELfEZr7rzolgQdC6mbrIvLkVtaAYeq7K7sDKZwJrtlsFU0AlOJA7suYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0517e652d0.mp4?token=ngcJPL5ScJdmJ8oRGjcen6VnXJT87yUTmb4XGDo1-qpeOg1Jr5Skzp5cfQN5L4G_o1MQYFKsrzX15U-8Vxi8UapPYk7ismTAzHX-w_BG3ws_wM_NZjeTRXkAtexogcVyIv1nliVB5Dpr-EHIfkeYaEC4lSrwWYTeKNCXSK08QuBHmn2HuSf1IMk8ZADTq2e2poCB_GGLdMlOTAsYnnDpHeezLcqtQgPrYdFLb4yUK_LkegRQhbFaKgu21afL-ggrpFQIExEjKbbMUDTNomGVFJmv4kMp9eELfEZr7rzolgQdC6mbrIvLkVtaAYeq7K7sDKZwJrtlsFU0AlOJA7suYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب
: سأعقد اجتماعات اليوم بشأن إيران، والأمور لا تسير على ما يرام.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/91204" target="_blank">📅 00:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91203">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇾🇪
🇸🇦
الاعلام الايطالي:
إيطاليا نقلت خلال الساعات الماضية بعض طائراتها العسكرية من قاعدة الطائف السعودية بسرية تامة وبسرعة بسبب المخاوف الأمنية من الاستهداف اليمني لقواعد السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91203" target="_blank">📅 00:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91202">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
🇰🇵
كوريا الديمقراطية الشعبية العظمى تعلن عن اختبار نظام أسلحة قتالية جديد
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91202" target="_blank">📅 00:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91201">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
🇸🇦
بريطانيا على وشك الاتفاق على تقديم المساعدة للجيش السعودي لمواجهة الحوثيين.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/91201" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91200">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
استعدادات في إسرائيل لاحتمال التصعيد مع إيران.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/91200" target="_blank">📅 00:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91199">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
تدفع الولايات المتحدة أكثر من 30 مليون دولار يومياً مقابل حصارها البحري لمضيق هرمز، مما يُرهق ميزانية البحرية الأمريكية، ويُثقل كاهل البحارة، ويُضعف جاهزية القوات البحرية العالمية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/91199" target="_blank">📅 23:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91198">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
رئاسة وزراء العراق:
حصر السلاح سيبدأ بفترة ٩٠ يوما لا تهاجم فيها الفصائل أو تتعرض لهجمات أمريكية، سنعتبر الجماعات المسلحة خارجة على القانون إذا واصلت عملها بعد انتهاء المهلة، المجموعات ستبدأ تسليم أسلحتها على أن تنتهي العملية بحلول 30 يونيو 2027، خسرنا 60% من عائدات النفط الشهرية بسبب الحرب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/91198" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91197">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDsRIpiq1ecixa-Q3aBkX_ZZ7a39lYz1OI9_7S6A1YwOejBrqnGGdMiJ0Cle0ViIAcdG1mSRx54a3j6qH0Rys_jKtkwtuJjo5Djcq6F-zsO7h-edWOe67CKHW0HjUBruyAwKjTjQFAiZStjynKLRL-BBJf5w63vmh1zEcLCNa6cVrfwmvinoeCjPZt3KiwLWz-uWoHUTSRsoz3lziUM5FRuWLKOiwpSGErXWt3GhavQPiHEUfyEMnuY_CF-PYmoQcnTREzWiVdvFGPHxXNBMvxdmKpOnuBdntuP-rn4IE0_2pv6I0m3-PRFPSdCONMLxzh_xJbsokqHMmT7fnffCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الناطق الرسمي لكتلة بدر
النيابية:
تحذير للحكومة العراقية وسلطة الطيران المدني من الانصياع للإملاءات الأمريكية وفرض حظر جوي على الطيران المدني الإيراني ومنعه من استخدام الأجواء والمطارات العراقية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/91197" target="_blank">📅 23:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91196">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
‏
الجيش البولندي:
بدأ عمليات طيران عسكرية في المجال الجوي البولندي عقب الهجوم الجوي الروسي على أوكرانيا.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91196" target="_blank">📅 23:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91195">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
مصدر امني لنايا...
🇮🇶
🇸🇦
السعودية بدأت بنصب مناطيد تجسس قرب الحدود العراقية السعودية على خلفية تهديدات باقتحام بري لها ..  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/91195" target="_blank">📅 23:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91194">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
مصدر امني لنايا...
🇮🇶
🇸🇦
المنطاد التجسسي تم مشاهدته مقابل السرية الثالثة مخفر المصطفى الحدودي
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91194" target="_blank">📅 22:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91193">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4a81398ab.mp4?token=ktizWqptJZhsmiVF5DjRFXDGHXYQgFp3qzIBYh6PLYwJxF-ubq-wCnLJhE3et_fh3qoTEwRIs0xcLw3zYVuvKR9SoQp3Z2gOZa6X1EG63XmT4L3hbWAHJ8ravVEhFHCelo62Mweaz-W1WIgGB897UQchdLwysdzD9_cwSPLYT2pvsWMlgutNTlhQhoHajfDrAdJWk4M1egOLgdXpdf3f4-3jDSISZRbJ1vZciQoHZSkEtQ9vhY_dDLsRRWtnvN9XTqIzaY6n_R-Q33gvDpcbTReK66N1crc8k8hWPHtJyYfEdvUe25xfGqhzVlnSsosY8xZhDwQylcy4kw02ZGNlEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4a81398ab.mp4?token=ktizWqptJZhsmiVF5DjRFXDGHXYQgFp3qzIBYh6PLYwJxF-ubq-wCnLJhE3et_fh3qoTEwRIs0xcLw3zYVuvKR9SoQp3Z2gOZa6X1EG63XmT4L3hbWAHJ8ravVEhFHCelo62Mweaz-W1WIgGB897UQchdLwysdzD9_cwSPLYT2pvsWMlgutNTlhQhoHajfDrAdJWk4M1egOLgdXpdf3f4-3jDSISZRbJ1vZciQoHZSkEtQ9vhY_dDLsRRWtnvN9XTqIzaY6n_R-Q33gvDpcbTReK66N1crc8k8hWPHtJyYfEdvUe25xfGqhzVlnSsosY8xZhDwQylcy4kw02ZGNlEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر امني لنايا...
🇮🇶
🇸🇦
السعودية بدأت بنصب مناطيد تجسس قرب الحدود العراقية السعودية على خلفية تهديدات باقتحام بري لها ..  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/91193" target="_blank">📅 22:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91192">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
مصدر امني لنايا
...
🇮🇶
🇸🇦
السعودية بدأت بنصب مناطيد تجسس قرب الحدود العراقية السعودية على خلفية تهديدات باقتحام بري لها ..
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91192" target="_blank">📅 22:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91191">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
اقترحت إدارة ترامب تخصيص 5 مليارات دولار لإطلاق صندوق استثماري لإعادة بناء مواقع الطاقة في الخليج.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91191" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91190">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇾🇪
🇸🇦
السعودية تعلق الدراسة غداً الاثنين في كليات جامعة الملك خالد في أبها وخميس مشيط خوفا من رد فعل اليمن على الاعتدائات السعودية الاخيرة.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/91190" target="_blank">📅 22:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91189">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-text">🔻
سپاه پاسداران انقلاب اسلامی:
دشمن پس از ناکامی در عرصه نظامی، به جنگ‌های ترکیبی، شناختی، اقتصادی و رسانه‌ای روی آورده است؛ اما ملت ایران با اتکا به ظرفیت‌های درونی، اقتصاد مقاومتی و اتحاد مقدس ملی، هر توطئه‌ای را خنثی خواهد کرد
نیروهای مسلح به ویژه پاسداران رشید انقلاب اسلامی در این نبرد همه‌جانبه، دست بر ماشه، آماده پاسخ‌های قاطع و ویرانگر به هر تجاوزی هستند.
@Naya_Press</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/91189" target="_blank">📅 21:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91188">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يعاود قصف الاحياء المدنية في محافظة تعز اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/91188" target="_blank">📅 21:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91187">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇶🇦
الاعلام الاجنبي: ‏
رفضت قطر تقرير مجلة نيويوركر الذي زعم أنها مولت حماس، واصفة الوثائق بأنها "مفبركة". وقالت قطر إن المساعدات المقدمة لغزة تم تسليمها تحت إشراف إسرائيلي، وجادلت بأنه إذا وصلت الأموال إلى حماس، فإن المسؤولية تقع على عاتق إسرائيل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/91187" target="_blank">📅 21:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91186">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
It seems that the US and its allies in the region are very upset about showing the losses through photos and videos. Therefore, our channel’s name will no longer appear when searched for on Telegram.
🔻
Please share our channel link as widely as possible.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/91186" target="_blank">📅 21:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91185">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇾🇪
🇸🇦
بريطانيا على وشك الاتفاق على تقديم المساعدة للجيش السعودي لمواجهة الحوثيين.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/91185" target="_blank">📅 21:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91184">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يعاود قصف الاحياء المدنية في محافظة تعز اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91184" target="_blank">📅 21:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91182">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e294732f4.mp4?token=gss6A0urFSELQ03aSH155wJO2uB6agQdck5XtOZfGHIoqPr1Dgb-w_z778o1B7IjosOFMHQcMjESb8_3oy-05_t12vGhnz3sI05KdK16fEuSTXfDOmdcGkNgFvwFbqIbO4SJQeaa0seHQYnHuDKAgqfy32vmkof_rPLdQRdBXwXc8dwiDrGLygNsIKoohCbVIG9LKsX3etHEYYtnqMUUlCjQVLMtdEokYgvMtU__5_PMPsC3Zk7VYIePlOe7pt5qc_DCvm_5nBa4_k3cokNWgglZ4khDIY6tidSAY0GaJfsGmbPnVy-pRFn8Gid5Zz2fPjPlSa162nNBddJ7SRwJqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e294732f4.mp4?token=gss6A0urFSELQ03aSH155wJO2uB6agQdck5XtOZfGHIoqPr1Dgb-w_z778o1B7IjosOFMHQcMjESb8_3oy-05_t12vGhnz3sI05KdK16fEuSTXfDOmdcGkNgFvwFbqIbO4SJQeaa0seHQYnHuDKAgqfy32vmkof_rPLdQRdBXwXc8dwiDrGLygNsIKoohCbVIG9LKsX3etHEYYtnqMUUlCjQVLMtdEokYgvMtU__5_PMPsC3Zk7VYIePlOe7pt5qc_DCvm_5nBa4_k3cokNWgglZ4khDIY6tidSAY0GaJfsGmbPnVy-pRFn8Gid5Zz2fPjPlSa162nNBddJ7SRwJqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استمرار انسحاب قوات الاحتلال الأميركي من العراق باتجاه الأردن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/91182" target="_blank">📅 20:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91181">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
في تصعيد كبير استهدف العدو السعودي المجرم  محافظات الجوف وتعز وصعدة ومأرب بـ 157 غارةً جويةً وصاروخاً، من خلال طائراته الحربية نوع "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، والعدوان الصاروخي من نجران وجيزان.
ليبلغ إجمالي غارات العدوان منذ بدء التصعيد 917 غارةً وصاروخاً.
هذا العدوان الكبير لن يمر دون رد بإذن الله تعالى.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/91181" target="_blank">📅 20:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91180">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxRNzQQzTOb0ZclblEhnTrb0X0EaxMf9b7pXC9ahsDnbj4cMvozp8zwiEBJuRXPqAspCKFWWpt2YAriRXur-nrkYvBdhESLoubJiWhush3PESiBTUE6gZtQ7ssCIHYaJTsgxPmBEWRxjVlfk8fqvAJ6oe5u3FtWpyrMqPHxM2oy4PrUyVCByiNBRA6MLXOuWWgM5lwfm-5xhYLhbNwc9MBPUAxuF4YP13bkiuo9XCKDNoWm_iqfat0kgWLeu6LPnnIev0kjG2dnsCcDiNV_EqV-lfXdbd_bjCOgxPMsQ_m-FhViRwYhMP1WyQV-RXg9f9Qooknj2TpuI-LnNfRBZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بقائي
:
عندما تغلق إدارة ما أبوابها - حتى في وجه الصحفيين الأمريكيين الذين لا تحبهم - وتمنع المراسلين الأجانب، بمن فيهم الفريق الإعلامي للرئيس الإيراني، الذين تفضل إسكات أصواتهم، فإنها لا تدير الوصول؛ بل تحاول إخفاء الحقيقة وتعزيز حملة التضليل الإعلامي من خلال انتهاك الحق في الوصول إلى المعلومات.
‏أمة كانت تفتخر في يوم من الأيام بإسقاط الستار الحديدي، تجد نفسها الآن تقف خلف أحد أبنائها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/91180" target="_blank">📅 20:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91179">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اعلام فرنسي يزعم:
‏العراق سيعلق رحلات شركات الطيران الإيرانية الخاضعة للعقوبات الأمريكية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/91179" target="_blank">📅 19:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91178">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfTeWftsp9OG1h0a5cqP_2mD7GlKuZUhgiAdnNkXJ7wJGSWbzCB6XGsuFOU9A9-I2cMVjYAx6jUXA5mxtWazIjo7lg68kAV3S95OYrGB2x1wjR4k___m51uiJyR666GGsV2ViSiyEtQW_6l_xzih_mz6TepCXVPukNzGCO00u0fIAQi-axKgv5Pfeyf9kk2ieJ5AALn8etScVmAIufISUwE3RuoNVQT6lwBnAwFTgRKltNEU4uColJRMZSxbFsl7VYuk0tnqW1YFFPtCT1m2vZeKb0DKItLO0dzJ7R6w_GRiVpny7POGFKM6NX75X1pnREAHbTiFSQWCgtF5kUPo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط: 99$ للبرميل
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91178" target="_blank">📅 19:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91177">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrZOP1cqFgZWz10tHbT4tQSzP3WGKrB6-uM8bP7PezQ0Oh2vxpAE2M954kchse7ghtJTYyYBba3DAWu_qMXakrLeAuF1Lx053T_ZzZ9BTBXFgdYNr4RTxYIaDx8b61VwTIXi5u4k3AC7k9VbzqVXVZqNB44KsUkIi4zmf45-LgkP3oRCcyijEVrj20XSwyY0InvTJdOrYY7yRRI9rjWrBqlMm__IzTv7opeDN7oQSbf-NpI-sbkOxa0AaSXtLRLraXQl3s8Le4iKWhNYJMj4aanNZ2fZdXUPCRw-k_-0OnH9W6Qcmm1uNulGJISxr4PaqVjpdHdwXkP-NOuqGjh-Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇱
🇺🇸
وزير الخارجية الايراني عباس عراقجي يعلق على مقال في صحيفة "إسرائيل هيوم":
لم يعد اللوبي الإسرائيلي يتردد في إظهار دوره وتأثيره علناً فيما يتعلق بالسياسة الأمريكية تجاه إيران؛ إذ تصرح صحيفة مملوكة لميريام أديلسون -والتي تُعد بمثابة لسان حال هذا اللوبي- صراحةً بأن السياسة الأمريكية يجب أن تُصاغ بحيث تدفع الولايات المتحدة أيضاً ثمناً لأي عمل ينطوي على عدم احترام أو عدوان ضد إسرائيل! حان الوقت لتتحرر واشنطن من هذه القيود.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/91177" target="_blank">📅 18:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91176">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LltuIvCatbCgE2abjHCtam-SL2y-rMsUSlRQX9v8LlnqXGzrkosOV8H6tPY7eNRscGjmQFeDweTA1E2ngR8S5WOX7_Jd53U5lnWXCvQkRbD9470umahsGe0BYAxB8VqftzumyNNemxmwLgImbjuesiYGkNzM0cz8K6zX__HwQZj3MPAVqnViPgF_V19LoyoLZ90eIwVaVzfvd2LOQLgKa0uggb5y6nEwN_oFgfCU92Hc8cUDHzet0S09vfp7PNYIzu5wfiE5qBnaF_NPdqz6d3UOn3V9_EJFFBUAl49q8QKA1Wa8QdMyUp9J9rXGsFlQyRdEyS-sv4iSwmtErbr-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب على منصة "تروث سوشيال":
الولايات المتحدة تعمل على صفقة ضخمة تتعلق بشراء البوتاس من بيلاروسيا. ستكون الأسعار أقل بكثير مما ندفعه حاليًا لكندا، وهو خبر جيد جدًا لمزارعينا ورعاة الماشية. شكرًا لكم على اهتمامكم بهذا الأمر.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91176" target="_blank">📅 18:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91175">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
🇮🇷
شركة الخطوط الجوية الإسلامية الإيرانية:
رحلات شركة "هما" (اسم قديم لشركة إيران إير) من ثلاث محطات انطلاق: طهران، ومشهد، وإصفهان، إلى مطار النجف، تجري وفقًا للجدول الزمني المحدد.
رحلات شركة "إيران إير" في مسارات طهران - النجف، ومشهد - النجف، وإصفهان - النجف، وكذلك مسارات العودة من النجف إلى هذه المدن الثلاث، مستمرة، ويمكن للركاب الاستفادة من خدمات الشركة الجوية في هذه المسارات وفقًا للجدول الزمني.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91175" target="_blank">📅 18:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91174">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91174" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91173">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/91173" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91172">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">السيد الحوثي:  العدو السعودي عاد إلى التصعيد بقصف مطار صنعاء واتجه إلى التحشيد البري الكبير لإبادة شعبنا وحشد عشرات الآلاف إلى صحراء الجوف والمخا والساحل الغربي والبيضاء وتباهى عملاؤه بأنهم متجهون لاجتياح ما تبقى من بلدنا وأشرف على التحشيدات في كل الجبهات…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91172" target="_blank">📅 17:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91171">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">السيد الحوثي: هل يقبل التركي والباكستاني أن يتدخل السعودي في كل سياساته؟ وهل تقبل الدول الخليجية بذلك؟</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91171" target="_blank">📅 17:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91170">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">السيد الحوثي:  الكيانات المتعاطفة والمتباكية مع العدو السعودي على منشآته النفطية وردود قواتنا هل ستقبل بالقيود التي وُضِعت على الوارد التجاري لتبقى في دولة أخرى للفحص والتفتيش قطعة قطعة!! هل ستقبل الكيانات المتباكية مع العدو السعودي الإجراءات التي تضيّق الحركة…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91170" target="_blank">📅 17:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91169">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">السيد الحوثي: وفود من العدو السعودي والبريطاني كانوا يذهبون إلى جيبوتي لتشديد الإجراءات بما يزيد من معاناة شعبنا عبر التضييق الاقتصادي.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91169" target="_blank">📅 17:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91168">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77280b847c.mp4?token=tOSaymhvlmQUsgNLSDHXimZJidHrJUf8AUL--Q1_9AUZvy6FZiAh7gBnbjmQhavA79ZR7RpnxFuKLGJaz64hicHeO-7o2Tbtg_ENs02jUFfdaxA824-qZ35LFTkfXVhtzZlYa-rr08ymnr-DdqICUeOe29ITEzObxHcJ-MRkk2CsgsNxsxHMfmhC0vhQhBVedIyH-H4dV1c_-7DsB9eRyv5VylUBjD2opZWvQSDeCIayaAQxdju3F9mEY4de7r_p7-hkBiqguZBWP6bUHUckxJ5Haq6CDq64q1fBVQQ2I-8IJkY1EYyAt--cZDJU_l7YbAyRB0XrTvfRrK2MA2oBUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77280b847c.mp4?token=tOSaymhvlmQUsgNLSDHXimZJidHrJUf8AUL--Q1_9AUZvy6FZiAh7gBnbjmQhavA79ZR7RpnxFuKLGJaz64hicHeO-7o2Tbtg_ENs02jUFfdaxA824-qZ35LFTkfXVhtzZlYa-rr08ymnr-DdqICUeOe29ITEzObxHcJ-MRkk2CsgsNxsxHMfmhC0vhQhBVedIyH-H4dV1c_-7DsB9eRyv5VylUBjD2opZWvQSDeCIayaAQxdju3F9mEY4de7r_p7-hkBiqguZBWP6bUHUckxJ5Haq6CDq64q1fBVQQ2I-8IJkY1EYyAt--cZDJU_l7YbAyRB0XrTvfRrK2MA2oBUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو المكتب السياسي لحركة أنصار الله ضيف الله الشامي: الطائرات السعودية تستهدف سوقاً شعبياً في مديرية ذو باب في محافظة تعز.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91168" target="_blank">📅 17:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91167">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عضو المكتب السياسي لحركة أنصار الله ضيف الله الشامي: الطائرات السعودية تستهدف سوقاً شعبياً في مديرية ذو باب في محافظة تعز.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91167" target="_blank">📅 17:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91166">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">السيد الحوثي: كل الجرائم السعودية التي ارتُكِبت في اليمن قوبلت بالتفرج لغياب المبادئ في التوجهات والسياسات المعتمدة لدى معظم الأنظمة، لو انتظر شعبنا العزيز للأمم المتحدة أو لمجلس الأمن وغيرها من المؤسسات أمام كل تلك الجرائم لما فعلت له أي شيء</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91166" target="_blank">📅 17:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91165">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
🌟
اكسيوس:
ترامب فكر في شن ضربات على الحوثيين في اليمن خلال عطلة نهاية الأسبوع، قبل أن يقرر عدم القيام بذلك.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91165" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">السيد الحوثي: الموقف العربي والإسلامي من العدوان السعودي على اليمن كان متخاذلا عدا محور الجهاد والمقاومة وبعض أحرار العالم</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91164" target="_blank">📅 17:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91163">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
🇾🇪
كلمة للسيد القائد عبدالملك بدرالدين الحوثي عند الرابعة عصر اليوم.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91163" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
هجوم إرهابي في مدينة ايرانشهر جنوب شرق إيران؛ إستشهاد أحد عناصر الأمن كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91162" target="_blank">📅 17:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-91161">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📰
وكالة رويترز: مكالمة هاتفية جرت بين ترامب ورئيس المرتزقة في اليمن رشاد العليمي</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91161" target="_blank">📅 16:58 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

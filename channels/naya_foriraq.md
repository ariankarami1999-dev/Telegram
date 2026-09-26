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
<img src="https://cdn4.telesco.pe/file/UiJuPDp7w3uPxgtQWiVdh1sE_fKT5y-_9xb14_OOQPyZBD0qg89hp13VlkWA6zupSDGnCsoQ_gBg2Cqu1hN_5iXHbnol_N8EcJBhpds1vxpkfmOPfsdgZlj-ziWamm6eYbcmu9BSSfnjOJdR-ByDcF6aDO8r82LFdzSbDCJ8-7ulVtGtAfm_yOW2C1Y44aQiwx-Q7SIgwKC4THaNrwQ1kThzlFnKEhZNV8aVtkfOnXS2WFUf0yl2jaorx2Ws4q9OQ53TPhBMsyZsGuerU7QbUOMohj3m0Pfc6ldcFYd6edm-3po-Naa7BhE3uATK66dFUfeRqkVEn33TbLWlqxkxPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 20:48:23</div>
<hr>

<div class="tg-post" id="msg-91699">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية
: رئيس الوزراء  توصل إلى تفاهمات مع الولايات المتحدة لضمان استمرار إرسال شحنات الدولار النقدي إلى العراق، ومن المقرر وصول شحنة جديدة خلال الأيام القادمة.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/naya_foriraq/91699" target="_blank">📅 20:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91698">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3ykn_z7Ix3OKyqZeQcSWZRBQ5mGzaD8MCrGqOEiBWzVEEHpcfiAiRsB0uWxmPbIjrVc5_VDsZTllmMljAjclUDDlMge0KtcdyAC83KbYWssGng4hDrGJRQ3roxHyKLjHCJ9H2VAYb1jE7TdyPq_D56o60oNRon0-KyOyvYvLk78EM0ppXbA9gMcmuKmojj73h7QxEiNvyOFit4pzx9jX7W9PYP33GlQiZg4G4QodXSmq2kdhf4jb_OYkeeI2oRSlR4_jXalLnztcncG8_IFIBWDvdz0wMQ3_N-RBycb_8kFvo85_xWNwZyYUO4-nGudbqEgfjBaZ59WxLwsqXbgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
كتلة دعم الدولة النيابية:
القرار العراقي يجب أن يصدر من بغداد لا من أي عاصمة أخرى.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/naya_foriraq/91698" target="_blank">📅 20:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91697">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇸🇦
‏
وزير الخارجية السعودي:
ندين اعتداءات الحوثيين وتهديدهم للأمن، ندعم الحكومة العراقية في ملف حصر السلاح بيد الدولة، ندعم سيادة العراق وأمنه ونشدد على ألا تكون أراضيه منطلقا للاعتداء على الدول المجاورة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/naya_foriraq/91697" target="_blank">📅 20:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91696">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: ‏
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 27 غارة جوية من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، استهدفت الأعيان المدنية من جسور وطرقات وغيرها فى محافظات تعز ومأرب وصعدة وعمران وإب وحجة.
‏ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1059 غارةً وصاروخاً.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/naya_foriraq/91696" target="_blank">📅 19:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91695">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇷🇺
‏لافروف: روسيا مستعدة للمساهمة في تحقيق الاستقرار بمنطقة مضيق هرمز.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/91695" target="_blank">📅 19:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91694">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي: نؤكد على ضرورة أن ترفع الولايات المتحدة حصارها المفروض على كوبا، وأن ترفع جميع القيود المفروضة على التجارة مع كوبا.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/naya_foriraq/91694" target="_blank">📅 19:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91693">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b190934d58.mp4?token=PgRqGF9VMevHjazcJvIY0Cil3yVC2IqaMk8UnRqAZQls-psPo4Ezl22iXAQM7hTq1XB882Imu8eLPvGzeqqIT59KsP93kWQLCuK9cdMUneM8cP4W4eG83x6wQZeFhmcpRNsP5Tz2lBrPwjy69yfFL313xlEeJu3d92fxVs8BvTUvvzUo725QJx01vHEgtjZnWrbz-08dLo2OvVXaMgkfsTS1PYhjEfx_DpjpECFHAdALEqUS3h9_zYiubcckWM6MjceC84iRTJlEsoGzKm_3BMGFcJA8FVj6ogKBJLxbvNXoQ8vX13wkKgV50Chj5Du1hR8QRGB_sMsJPrv7yA1Z5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b190934d58.mp4?token=PgRqGF9VMevHjazcJvIY0Cil3yVC2IqaMk8UnRqAZQls-psPo4Ezl22iXAQM7hTq1XB882Imu8eLPvGzeqqIT59KsP93kWQLCuK9cdMUneM8cP4W4eG83x6wQZeFhmcpRNsP5Tz2lBrPwjy69yfFL313xlEeJu3d92fxVs8BvTUvvzUo725QJx01vHEgtjZnWrbz-08dLo2OvVXaMgkfsTS1PYhjEfx_DpjpECFHAdALEqUS3h9_zYiubcckWM6MjceC84iRTJlEsoGzKm_3BMGFcJA8FVj6ogKBJLxbvNXoQ8vX13wkKgV50Chj5Du1hR8QRGB_sMsJPrv7yA1Z5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: هل تخططون لعمل عسكري ضد كوبا؟ وردت تقارير تفيد بتفعيل قوات احتياطية، ربما لمواجهة كوبا.  ‏ترامب: أقول إننا وكوبا سنتوصل إلى اتفاق. لا أعتقد أننا سنحتاج إلى الجيش. فريق شيكاغو كابز يعاني من تراجع حاد. نريد مساعدة كوبا. نريد أن نفتح كوبا أمام شعبنا.  ht…</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/naya_foriraq/91693" target="_blank">📅 19:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91692">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d52808a7c.mp4?token=bPUweYiRa5WVWJd31vmho6MqTlnEeQUxhed9faculL-53JwsLGYrxJ_bBtFA98S8Hi0N9738qgFmx9xWc1zykR_KUluOUYh6ekvkSgz1p0ywQOOC5sP75rb9S4cwJCsTJCIdhL52QlSL_8EGqKexd2BBHLY77rqniIW2kQKo8L_gqvZhfWc386b1Hr84GsYnr7xb5sGJ-JGp2pL98RCpmWs9wQCsIjsJlDUs8VJMz6REK5GCiTwtrrPMK70y9giB_vH4sVhTWCA3Yg4iM9EKAqA6y_HkWbFF-EDyhDteRgXAXrM_7OCimfFiWL6np6n8CEtC6Rk5tN4vnZjfbThiMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d52808a7c.mp4?token=bPUweYiRa5WVWJd31vmho6MqTlnEeQUxhed9faculL-53JwsLGYrxJ_bBtFA98S8Hi0N9738qgFmx9xWc1zykR_KUluOUYh6ekvkSgz1p0ywQOOC5sP75rb9S4cwJCsTJCIdhL52QlSL_8EGqKexd2BBHLY77rqniIW2kQKo8L_gqvZhfWc386b1Hr84GsYnr7xb5sGJ-JGp2pL98RCpmWs9wQCsIjsJlDUs8VJMz6REK5GCiTwtrrPMK70y9giB_vH4sVhTWCA3Yg4iM9EKAqA6y_HkWbFF-EDyhDteRgXAXrM_7OCimfFiWL6np6n8CEtC6Rk5tN4vnZjfbThiMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي:
نؤكد على ضرورة إطلاق سراح مادورو وزوجته على الفور.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/naya_foriraq/91692" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91691">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
انطلاق مباراة منتخبنا الوطني أمام الكويت في بطولة كأس الخليج.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/naya_foriraq/91691" target="_blank">📅 19:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91690">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIM1-xJeJfnI7EoR3SxhcRvjFY7T_AH3MsUGpGep3hcTD7fMpJK95CDZ0x4HmZsp3XAUpuHBLEwvDn2PF4b5GLY8P096x8djABI7a70Dzf3oNBaO05k0rNpadlzymGtZz_9l3z0f6_Fj4UejiRuBsDvZ9SGcc7CK1qTevvKGdZeNax0SzgmbmLIll4AePb2CwDNgDGARSsO1RNlc2ETEXnvWoAECWhb02Je8KpZ4GnX_kFuR6CDJiRmCCH_UVOt6rsV-0tnUGQqVH8nSOu_s1N_VqojLVHZGLYMsP8A3xVU8blxNaVcfUOB3hBWlqvzpRw-BbNda6xBV5e2dUrLI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
محافظة البصرة تتحضر للنزول إلى الشوارع احتفالًا بخروج قوات الاحتلال من الأراضي العراقية في يوم 30\\9.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/naya_foriraq/91690" target="_blank">📅 19:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91689">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مشاهد من الوقفات الاحتجاجية في محافظة البصرة جنوبي العراق</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/naya_foriraq/91689" target="_blank">📅 19:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91688">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇷🇺
🔻
‏
وزير خارجية ألمانيا أثناء لقاء لافروف:
العودة لعلاقة بناءة مع روسيا ممكنة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/naya_foriraq/91688" target="_blank">📅 19:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91687">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
مؤسسة النفط الليبية: توقف وحدة في مصفاة الزاوية بسبب إغلاق مسلحين لصمام على خط "الشرارة".</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/91687" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91686">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد الضربات الموجعة ‏استعانت شركة أرامكو السعودية بشركة إيفركور لتقديم المشورة بشأن خطط إعادة الهيكلة التي يمكن أن تؤدي إلى إنشاء قسم غاز مستقل وتمهيد الطريق لطرح عام أولي محتمل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/naya_foriraq/91686" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91685">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de7c72618.mp4?token=eTDyFCanXg1F-g4-tRo9PLkjdmXK5FZ1wWLTNv9SccgVQDP-QUJZmE-0mHMK5SVWDAf758Y3ZLxvK4gSzLTEdrQabbbT6MWONEq9BN09RRPi0K5r45PWwdMQxkyFocd85Ny9koylm_flCPaZO8GTF5ZE5tl7tCMogD3PLelxRM6ihneMMe6ncEvYwUtiOu8KuitIgsIIr_uAjQXrIkNzi5kQhqnWwbX6a62W5X81okMd7mmar5THNZ2dWjRJ3EkQJeNZcbBQXz-a76DLBUsg6yNIa5BpVA8dbhwLf7WCPT6GEMqCeJKVR3GfqX5n02nrWWEi9atKdXf9SD7UFg_txA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de7c72618.mp4?token=eTDyFCanXg1F-g4-tRo9PLkjdmXK5FZ1wWLTNv9SccgVQDP-QUJZmE-0mHMK5SVWDAf758Y3ZLxvK4gSzLTEdrQabbbT6MWONEq9BN09RRPi0K5r45PWwdMQxkyFocd85Ny9koylm_flCPaZO8GTF5ZE5tl7tCMogD3PLelxRM6ihneMMe6ncEvYwUtiOu8KuitIgsIIr_uAjQXrIkNzi5kQhqnWwbX6a62W5X81okMd7mmar5THNZ2dWjRJ3EkQJeNZcbBQXz-a76DLBUsg6yNIa5BpVA8dbhwLf7WCPT6GEMqCeJKVR3GfqX5n02nrWWEi9atKdXf9SD7UFg_txA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: قوات الاحتياط بالجيش الأمريكي تضع الأسس لعمل عسكري محتمل حول كوبا.</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/91685" target="_blank">📅 18:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91684">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3552d477f.mp4?token=H4m6iLfUaPDz7ig69J31lKkaTmvULm6ZmGFlWaXOZtmhm8Lg2rEcL2tuyjSqtQxrWOSizSNgq26Liym24Y50hMAFMn816zCZ7NY-zisp4CevGwnaYCrEMLs_ZicZBm8v3XUQA2b2Y89sUBccdOK5CPblj1ByoROXKey6TS4xpoZ4ebTb-Sh3xIxZwItkNuGU3XrHIZ6JVIzKpP-ro6iDJ44bnMtEhH-87iD6hrOqfDQju2DjyV1IDOn7VrjHVdNSkqV4_3m4Kjw0fTqBOJcCNi7YyjtTZXO-lpW3McwRHijIATipnJarNSxi6dfu4a9INXy0hxDVoE1F_H31TgZGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3552d477f.mp4?token=H4m6iLfUaPDz7ig69J31lKkaTmvULm6ZmGFlWaXOZtmhm8Lg2rEcL2tuyjSqtQxrWOSizSNgq26Liym24Y50hMAFMn816zCZ7NY-zisp4CevGwnaYCrEMLs_ZicZBm8v3XUQA2b2Y89sUBccdOK5CPblj1ByoROXKey6TS4xpoZ4ebTb-Sh3xIxZwItkNuGU3XrHIZ6JVIzKpP-ro6iDJ44bnMtEhH-87iD6hrOqfDQju2DjyV1IDOn7VrjHVdNSkqV4_3m4Kjw0fTqBOJcCNi7YyjtTZXO-lpW3McwRHijIATipnJarNSxi6dfu4a9INXy0hxDVoE1F_H31TgZGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س:
قال باراك أوباما للتو "إذا وضعتم النساء في مناصب قيادية في كل حكومة لمدة عامين، فسيكون الوضع أفضل". هل تصدق ذلك؟
‏
ترامب
: هذا سخيف. أنا أحب النساء. أعتقد أنهن رائعات. لكن يا له من تصريح سخيف!
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/91684" target="_blank">📅 18:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91683">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الطيران الشراعي يرفع في سماء العاصمة العراقية بغداد صورة شهيدنا الاقدس سماحة السيد حسن نصرالله في ذكرى شهادته</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/91683" target="_blank">📅 18:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91682">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇷🇺
ماريا زاخاروفا أن الجانب الألماني طلب عقد اجتماع بين وزير الخارجية الألماني وسيرغي لافروف</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/naya_foriraq/91682" target="_blank">📅 18:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91681">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da57ede6e8.mp4?token=VQ68AX22NoMAudfn-GQ2lp2iH888xQQrEyYUGE8a7uA2wKeN7LwVqJYtwYfD8iWNgM7LCjdZCOxy5q-vVBrq36DUIoJUOIrEaksp6W3O1WHczfK-N96pi4fvb2-YoQYEwT-2M6z_Y4RBmNKIR7SmQHRocP5Yg-62Mq-yHcGn6ckygVjoQlSHupdzn4mJvqYWOCmQXAOn8DzxfkytTsYKnLLME0kqNzsBSV_15KlKbgXTxREgn1J1kJmPNLj8rKavZSlmrOhBvZd3zBOBnur3Roua6WdHjTvScA-Hu-GMDWAL0z3wBEtjtqxcfPBUxCXJXeTgjLkMOr0bJWN-RMIC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da57ede6e8.mp4?token=VQ68AX22NoMAudfn-GQ2lp2iH888xQQrEyYUGE8a7uA2wKeN7LwVqJYtwYfD8iWNgM7LCjdZCOxy5q-vVBrq36DUIoJUOIrEaksp6W3O1WHczfK-N96pi4fvb2-YoQYEwT-2M6z_Y4RBmNKIR7SmQHRocP5Yg-62Mq-yHcGn6ckygVjoQlSHupdzn4mJvqYWOCmQXAOn8DzxfkytTsYKnLLME0kqNzsBSV_15KlKbgXTxREgn1J1kJmPNLj8rKavZSlmrOhBvZd3zBOBnur3Roua6WdHjTvScA-Hu-GMDWAL0z3wBEtjtqxcfPBUxCXJXeTgjLkMOr0bJWN-RMIC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لقد كان لقائي بالزيدي رائعاً.. إنه رجل رائع وصديق جيد لي. لقد دعمته، أليس كذلك؟ أعني لقد دعمته، رئيس الوزراء العراقي.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/91681" target="_blank">📅 18:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91680">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامب:
لقد كان لقائي بالزيدي رائعاً.. إنه رجل رائع وصديق جيد لي. لقد دعمته، أليس كذلك؟ أعني لقد دعمته، رئيس الوزراء العراقي.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/91680" target="_blank">📅 17:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91679">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
🇮🇷
السفير الإيراني في بغداد محمد كاظم آل صادق:
من المحتمل إعلان قرار جديد قريباً بشأن الرحلات الجوية إلى العراق. نحن على تواصل مع المسؤولين العراقيين وقد قُدمت مقترحات في هذا الشأن.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91679" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91678">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامب: ارفض المقترح الايراني.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91678" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91677">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91677" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91677" target="_blank">📅 17:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMes6fHu4JUqNnBm_yNErWQ6mmaqWmmB8bFRHVkdfDt37XWs6wx3OS2ZUh0RYJaOQb1pBGWYwCZblXYUTaZZO6P1ulRBGCafQrtE4VExacRjnILozHcPFc-JDQhb2u90iShVIbcUM26L9Z54SMpQw3VdB-a3U6QyurVlbivqbii3invVt7dkd_KDYBBpTQ6WVXS5kDa1prRxKBuBGAltHalx63jmw1eAo25VJreGYxYftyuqK8yMy8c1c03GeUMxdSrMUWS_LpjmieDUFk5lovWnMe12Fots8a2F608cFjiMAb1GqsXVMKqWtbEdOq_ZeFm18X1zvIhpvufHUxc93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأمين العام لحركة أنصار الله الأوفياء الشيخ حيدر الغراوي: العراق ليس ولايةً أمريكية ومطاراته ليست ملكاً للخزانة الأمريكية وقراره لا يحتاج إلى استثناء من أحد.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/91676" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91675">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامب: ارفض المقترح الايراني.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/91675" target="_blank">📅 17:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dbf96a66.mp4?token=X6Bxp8ySqVss2bKHhMEKI73ld8DZ0wU3nG5D8pCWaO9orELx17bqu7g57fDpEkORItGs20wUo_Hei9RJFRWwzia_CUV5Qc9km8Fq6Krh7N8bJmivGFULp3EGe-o5X-480Hpfn_lVhy7hzfAslhn6e0RE--GUjL-Lw7SbL9Nn_anxl6ElCWUQ9AMpjEp1v2nFM_UH2Pryzde639gswl2uOYqGNNThXTYihgXPNLOgWquiniP4hldfH9hEDbZWj4839bvOeEXxTh0c-Rr8QAxsFe9C7gLU85E0WO4pugXtKjjtdrmTmOGyVeLskAnRZ69niir7Yycm2mudxHxLI0zSzDcK4N9faBfy3bxSVHhYNLBagyxduq1xZkqSeG5dREI9KqBAjnbtv4-VYj09ix8nekN3PnH3KSSJKEDl40QmIlB9lh7YEtIatnWcTlWDQtyg38L98JDpzwPS6EIO-4LF8lcDeoBwD0kNKSf8HkcGNdeCPF0YaY07aIDW4y0JVRxL14aMgrREEVALlGTBTANuoINGh83K1_-BnDGuVUfbuNhp6As54AFKPYJ-UQHIzwJeNfDvqGRFmdL9PlpTpgjDduv09b0X-R65VeubvKTV0TMXEIdMwx7dXVqS2ycq8am0cVNI0D3922j8xawp3ipu6qh3xJgwCJ6uF9ONRQ-ZNoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dbf96a66.mp4?token=X6Bxp8ySqVss2bKHhMEKI73ld8DZ0wU3nG5D8pCWaO9orELx17bqu7g57fDpEkORItGs20wUo_Hei9RJFRWwzia_CUV5Qc9km8Fq6Krh7N8bJmivGFULp3EGe-o5X-480Hpfn_lVhy7hzfAslhn6e0RE--GUjL-Lw7SbL9Nn_anxl6ElCWUQ9AMpjEp1v2nFM_UH2Pryzde639gswl2uOYqGNNThXTYihgXPNLOgWquiniP4hldfH9hEDbZWj4839bvOeEXxTh0c-Rr8QAxsFe9C7gLU85E0WO4pugXtKjjtdrmTmOGyVeLskAnRZ69niir7Yycm2mudxHxLI0zSzDcK4N9faBfy3bxSVHhYNLBagyxduq1xZkqSeG5dREI9KqBAjnbtv4-VYj09ix8nekN3PnH3KSSJKEDl40QmIlB9lh7YEtIatnWcTlWDQtyg38L98JDpzwPS6EIO-4LF8lcDeoBwD0kNKSf8HkcGNdeCPF0YaY07aIDW4y0JVRxL14aMgrREEVALlGTBTANuoINGh83K1_-BnDGuVUfbuNhp6As54AFKPYJ-UQHIzwJeNfDvqGRFmdL9PlpTpgjDduv09b0X-R65VeubvKTV0TMXEIdMwx7dXVqS2ycq8am0cVNI0D3922j8xawp3ipu6qh3xJgwCJ6uF9ONRQ-ZNoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غضب شعبي عراقي في محافظة البصرة بسبب حصار الحكومة العراقية للجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/91674" target="_blank">📅 17:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مشاهد من محافظة البصرة خلال الاحتجاجات ضد الحصار الجائر ضد الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/91673" target="_blank">📅 17:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91672">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c94d716d.mp4?token=l6jb5ToYQqayRQLyif2vbjb2m5ovz3_pHx9Z79fiDxXM4Thddd3EoU0SYEskBQOvyOGI4cbr_8Qh6pBzuUl_skbrJjBN5pYq-nqKueagNNtLTeLj7Jk-F20PLc4IXRy4afSF1w5e-epkQc__Qh5IolwwLQPWmxqcVm9QEo3Te-AnEpsxwBft7NLTY_Ko0hFsCr-_xPWv2VL7B1iY3r2s-_VetGaGjljPYSHwtOm45pNY9GOlLoxXdASjeu7SkJU7kjpNSz18XKKPJEzI1Fqf1NDfjgFgI7Ia2JUt0lO2C5UGS6x_0FRAhJ2thIet0Mc62keZ6gSMVHBlosZrYIF_NXCVcGxy24gKm6xF4dpD9JPrIZlZ-2_cdmuipFoBJp1qL66LNoOERxVlUvDRhmZrwz0UFboxZopiLyInWrD-Hi35wrOC7Goce9qNabIha9Si4iNrspEnyriJpY7Fya1X09Z4pfnW5vJ7Fvitt-nBZrlt1OQtMOmATZ7jTc37loOnqDogzRnKFiW7HU6V9lIubsdoRqdZXkcMV3pyogd8ED_WTCAWxrjcx3jZneK0sUxiAj00k8CjR2qHolRaSxjSWkBXUU4cIRQUjTofhL6zaNNVaTlzkWL2Yvvuz2vbE_4xln2qsSKEPKKlELvDQb4UZK2tf8pGXpZBq86XLyNBFF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c94d716d.mp4?token=l6jb5ToYQqayRQLyif2vbjb2m5ovz3_pHx9Z79fiDxXM4Thddd3EoU0SYEskBQOvyOGI4cbr_8Qh6pBzuUl_skbrJjBN5pYq-nqKueagNNtLTeLj7Jk-F20PLc4IXRy4afSF1w5e-epkQc__Qh5IolwwLQPWmxqcVm9QEo3Te-AnEpsxwBft7NLTY_Ko0hFsCr-_xPWv2VL7B1iY3r2s-_VetGaGjljPYSHwtOm45pNY9GOlLoxXdASjeu7SkJU7kjpNSz18XKKPJEzI1Fqf1NDfjgFgI7Ia2JUt0lO2C5UGS6x_0FRAhJ2thIet0Mc62keZ6gSMVHBlosZrYIF_NXCVcGxy24gKm6xF4dpD9JPrIZlZ-2_cdmuipFoBJp1qL66LNoOERxVlUvDRhmZrwz0UFboxZopiLyInWrD-Hi35wrOC7Goce9qNabIha9Si4iNrspEnyriJpY7Fya1X09Z4pfnW5vJ7Fvitt-nBZrlt1OQtMOmATZ7jTc37loOnqDogzRnKFiW7HU6V9lIubsdoRqdZXkcMV3pyogd8ED_WTCAWxrjcx3jZneK0sUxiAj00k8CjR2qHolRaSxjSWkBXUU4cIRQUjTofhL6zaNNVaTlzkWL2Yvvuz2vbE_4xln2qsSKEPKKlELvDQb4UZK2tf8pGXpZBq86XLyNBFF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بغداد تنتفض ضد الحصار على الجمهورية الاسلامية في ايران</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/91672" target="_blank">📅 17:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91671">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e8cf94bf.mp4?token=IWuvkbTPoW_IYqBG6GYNd6yc5aCWlFtoxlT-TpwHwho1HZjnuYCmIv_UqJ8a4s4vLkwUVClYhfhal4rT66T_MSUXKRyKubB2oWkv5ZVQgEn8xrelY1KzrP7XLyw8lmChHcrEePCfAJt5n013D857QK9vWjv9gtBBdtxbog6heAFtJztaLlmvvSPmYb7Mj_9ua3TJW0Vc3PpIcmJ1hE6v9qEDZALExeFSyFHJ6bOjy8K90SpQXOLqtt4UA3byfh48S6jEIijUgZLqMHmTvPEtEUUJ_XqZdNSjDgX9HDIra5e1jf46Wenu6n91uTV8dowdKOjaLvmqSlJWrDdTRNOLEkEHiR7JubaNzIS4vjwMpmp4uav_JNmaeKd-lbxoN13AQks84sx_PhJ1gkiRuhJSp-nWD2JzQa1wkUe2dO2XgoHhACjC6sNDQ2_ikI8-TgL1--_vRlJg1OWMcw7ulOJODTLBA1_Y9WpPFkqHvMTF0-wZ18SDldDtblPHOQf4dNvCR0wiuTsP-BUYMSGvmfoCUqSYR_FdOUzRPnsm1gSg5jDRE2GG3d6FPXlTgSNdFldh6mMovJmjJPnZGMUn6UJovikCJzOZxzNBCV2ctmVm9j-euwSy5V_LJEy_xNur683xIbPSFRy0ZYVcrnc71X2X9OT3sfVU5lD6VPtakLB65RM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e8cf94bf.mp4?token=IWuvkbTPoW_IYqBG6GYNd6yc5aCWlFtoxlT-TpwHwho1HZjnuYCmIv_UqJ8a4s4vLkwUVClYhfhal4rT66T_MSUXKRyKubB2oWkv5ZVQgEn8xrelY1KzrP7XLyw8lmChHcrEePCfAJt5n013D857QK9vWjv9gtBBdtxbog6heAFtJztaLlmvvSPmYb7Mj_9ua3TJW0Vc3PpIcmJ1hE6v9qEDZALExeFSyFHJ6bOjy8K90SpQXOLqtt4UA3byfh48S6jEIijUgZLqMHmTvPEtEUUJ_XqZdNSjDgX9HDIra5e1jf46Wenu6n91uTV8dowdKOjaLvmqSlJWrDdTRNOLEkEHiR7JubaNzIS4vjwMpmp4uav_JNmaeKd-lbxoN13AQks84sx_PhJ1gkiRuhJSp-nWD2JzQa1wkUe2dO2XgoHhACjC6sNDQ2_ikI8-TgL1--_vRlJg1OWMcw7ulOJODTLBA1_Y9WpPFkqHvMTF0-wZ18SDldDtblPHOQf4dNvCR0wiuTsP-BUYMSGvmfoCUqSYR_FdOUzRPnsm1gSg5jDRE2GG3d6FPXlTgSNdFldh6mMovJmjJPnZGMUn6UJovikCJzOZxzNBCV2ctmVm9j-euwSy5V_LJEy_xNur683xIbPSFRy0ZYVcrnc71X2X9OT3sfVU5lD6VPtakLB65RM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ التجمعات الشعبية في محافظة البصرة احتجاجا عن خضوع العراق للاملاءات الامريكية وحظر الطيران بين العراق وايران</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/91671" target="_blank">📅 17:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91670">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">البصرة ام الشهداء  تقول كلمتها عند الرابعة   بداية كورنيش جهة التعليمي   استعدووووا</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/91670" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91669">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1be51000.mp4?token=C38gMc6m-skkgR516bn9_hQqUtAPtvjzpgLjSAzkOpNo50fNBvNcjJ37BNDWpiLuur8pU8wZCMumL5m88uK1IUzv4qsSTvArf3Wh2UMF7lLF7vRN0xVH_DYjYApHD_uSdJqWW4inwf_jVhkGOlML09vTEjx_vIqNgZhDIsqnwly8XpslxzU-4lX2E74LRQEmMOEyHaD-iGWvsfAVAbvCvh4OzksGYbOESvdkqMKkw1x2Azm3CFD32CVPI9F58HmEc7Q8-OG95KQVYMDmxGqepbFbzMmz7rWXd4gcQ5MULQMa_6-XeQAVatEQQprADeLoSQ-MsGhCdRxLIamIjWdqjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1be51000.mp4?token=C38gMc6m-skkgR516bn9_hQqUtAPtvjzpgLjSAzkOpNo50fNBvNcjJ37BNDWpiLuur8pU8wZCMumL5m88uK1IUzv4qsSTvArf3Wh2UMF7lLF7vRN0xVH_DYjYApHD_uSdJqWW4inwf_jVhkGOlML09vTEjx_vIqNgZhDIsqnwly8XpslxzU-4lX2E74LRQEmMOEyHaD-iGWvsfAVAbvCvh4OzksGYbOESvdkqMKkw1x2Azm3CFD32CVPI9F58HmEc7Q8-OG95KQVYMDmxGqepbFbzMmz7rWXd4gcQ5MULQMa_6-XeQAVatEQQprADeLoSQ-MsGhCdRxLIamIjWdqjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">البصرة ام الشهداء  تقول كلمتها عند الرابعة   بداية كورنيش جهة التعليمي   استعدووووا</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/91669" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91668">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBrRoIWB_Xhi3J-ZdL9pQBcwEiuyl4ox9gEueo9vHZnbsfJ-YFBgI2Mthnt3ZsUDPckuqay0GiVD-5pzsTA-avzfmUibC3EHEjwwl2yE8pX_1xZTo29E5Inox0t-yiVYwKfgscqPm5nGfMWYoxg49ji0b5j38ZCT57OHZX5XUipCO0UXT5vKK4eyc8-2yfjuRxN4RSJK1DPLDXrdbBhNqa_Ux2V0oAKCWrSfAyV-FQCW6LFrM5wZVRq9NLcFrdnDlRiG-zQCO1p6th8oizSSfG6nRv_dMgFzDKrY_AzVUzVelMLUqTSYq0M6gDcu4NKD4ux8cl8_cc4_rw6LK39SXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشركة العراقية المتحدة لخدمات المطارات والمناولة الارضية المحدودة المختلطة:
لم نتسلم أي توجيه حكومي رسمي يتناول حماية مصالح الشركة وأموال مساهميها. وعليه، وما لم يردنا توجيه حكومي رسمي يوفر الضمانات والحماية الكافية من التبعات الناشئة عن إعلان وزارة الخزانة الأميركية مكتب مراقبة الأصول الأجنبية OFAC الصادر بتاريخ 8 أيلول 2026 وذلك قبل التاريخ المذكور، فإن الشركة تأسف لاضطرارها إلى تعليق تقديم خدماتها اعتباراً من 2026/9/23 لشركات الطيران الإيرانية المدرجة في ذلك الإعلان. وكما أوضحنا في كتابنا المرقم 1855 ، فإن أي تعليق من هذا القبيل إنما يرجع كلياً إلى موانع حوكمة قانونية ومصرفية دولية قاهرة وخارجة عن إرادتنا، وليس إلى أي قرار تجاري من جانبنا، ونؤكد التحفظ الوارد في ذلك الكتاب.
إن الغرض من التعليق هو حصراً حماية الشركة وأموال مساهميها، بما في ذلك المساهم الحكومي، من أي تبعات قانونية أو مالية أو رقابية أو تشغيلية محتملة، ويأتي ضمن مسؤوليات إدارة الشركة في صون مصالحها وضمان الامتثال لمتطلبات العقوبات ذات الصلة. كما أن التعليق يقتصر حصراً على الجهات المدرجة في إعلان 8 أيلول 2026، ولا يمس بأي حال من الأحوال خدماتنا المقدمة لبقية شركات الطيران، ولا سلامة وانسيابية حركة الطيران المدني في مطار بغداد الدولي.</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/naya_foriraq/91668" target="_blank">📅 16:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91667">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">العامري: نهيب بالحكومة لعدم الاستجابة بهذا القرار الظالم</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/91667" target="_blank">📅 16:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91666">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بدأ كلمة العامري في ساحة التحرير</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/91666" target="_blank">📅 16:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91665">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بدأ كلمة العامري في ساحة التحرير</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/91665" target="_blank">📅 16:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91664">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2695180475.mp4?token=jX6F4fHj0bH3cTJTzhxnDzB8L8bqT2ZK-LtTw8oixIDaAxugJnkH2rJrMGe-o8OKoMNsSzowFFuL4TLJVeRn9otMVjWhyLikraQeJkzItwei9NlL0CuYN6092CuqXQb08_9AKS1MQijPmzwRP9Zj6f_NoKU85jDVIRxVODqDR7WzUu6WNQ4vZIGMJ184a9_ZDCjWZ0n3mgXdTgg1mz7QcJvJnDzBpa37KYOMmQzj87tyeUr3MONuLYhz9Ir3FuQEeTExLk7ZXESejdsqAoc7JcVMTHAmcr34p8a4L9AgAmyVQ2dRglT4SWsBEgxN34S3k0w6m0bJnB8is1TgWRsFXDVt_5Sy9IgrgLTUxB5a-qqimqhVR0B2bnneXnJFfJcJOT943rE0Uc2T6YzXdgYP_1EaNKm4GiWxG1RZc-p7pYKBVM3OSjK0VGiHKvZODgV-wlxqJT7IFFMG7HuelMhJHCIdmR2LiiMTCacxBSjHw4-MxVEx4E1iTO7BHzFhO6JU8okJvaJtJjguHzwu1c2tTQTrZHgeP1FQMINNN1bCOOwE5ZBBRCfRMNkDY1aU_v7IEOM5RX3TvUjRxmd0O8SEWNN0lKFJQmXjBuZFzc3-Jx72slBMhnbzHDliiN_T8P7RvFSk0TignjkIy-DVg5KX8RVUY6K6Keo1aN-LffE-8jk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2695180475.mp4?token=jX6F4fHj0bH3cTJTzhxnDzB8L8bqT2ZK-LtTw8oixIDaAxugJnkH2rJrMGe-o8OKoMNsSzowFFuL4TLJVeRn9otMVjWhyLikraQeJkzItwei9NlL0CuYN6092CuqXQb08_9AKS1MQijPmzwRP9Zj6f_NoKU85jDVIRxVODqDR7WzUu6WNQ4vZIGMJ184a9_ZDCjWZ0n3mgXdTgg1mz7QcJvJnDzBpa37KYOMmQzj87tyeUr3MONuLYhz9Ir3FuQEeTExLk7ZXESejdsqAoc7JcVMTHAmcr34p8a4L9AgAmyVQ2dRglT4SWsBEgxN34S3k0w6m0bJnB8is1TgWRsFXDVt_5Sy9IgrgLTUxB5a-qqimqhVR0B2bnneXnJFfJcJOT943rE0Uc2T6YzXdgYP_1EaNKm4GiWxG1RZc-p7pYKBVM3OSjK0VGiHKvZODgV-wlxqJT7IFFMG7HuelMhJHCIdmR2LiiMTCacxBSjHw4-MxVEx4E1iTO7BHzFhO6JU8okJvaJtJjguHzwu1c2tTQTrZHgeP1FQMINNN1bCOOwE5ZBBRCfRMNkDY1aU_v7IEOM5RX3TvUjRxmd0O8SEWNN0lKFJQmXjBuZFzc3-Jx72slBMhnbzHDliiN_T8P7RvFSk0TignjkIy-DVg5KX8RVUY6K6Keo1aN-LffE-8jk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعدوا   العامري سيغسل عار الإطار بعد قليل</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/91664" target="_blank">📅 16:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91663">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد جديدة لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرات رجوم في عدة جبهات.</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/91663" target="_blank">📅 16:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91662">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmSAuqPPVwrszH6tKSquf-J3bLQf4C9KWUdhk_iNx8Lz_iZWgEWpNwMSELdOs5luCNwg-H8wGH2nGOlltCxP5mFzWHd8drjZ4bggsSUI3Yo8RFnedGfbXQx9VQYzyEGVpLjj_r_7fgfOmeyKRcq2Hmrs_BQgIobmk8x8WV7H4VxnLfKMJzX49D13sV0pl8oMB00bD4D86QX8aikWydwb4w_PMERuKO2EwmwGful9h_eY6bdiiaQPfKen597X3P-UVTXWRTdrIWW6EBmgjf7-lWPECTBjwkkkKETrGIZj4CZugQuC_sgvqCxPb_v1gKeeXqyg4SxWZftrj7ArMjUA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمانة المجلس الأعلى للأمن القومي الإيراني:
إن نشر بعض التفسيرات والاقتباسات غير الصحيحة من تصريحات أمين المجلس الأعلى للأمن القومي بشأن موضوع النقل الجوي، أدى إلى طرح تساؤلات وحالات من الغموض، وعليه نوضح ما يلي:
1- تُنفى الادعاءات التي تفيد بأن إيران ستلجأ إلى رد عسكري بالمثل رداً على القيود الجوية الأخيرة.
2- تجري المفاوضات بين إيران والدول المعنية بجدية لرفع بعض القيود الجوية غير القانونية المفروضة، وتجري متابعتها بشكل مستمر.
3- هناك عدة خيارات غير عسكرية للرد بالمثل، وفي حال الضرورة سيتم تطبيقها على بعض المطارات، مع التأكيد أننا نأمل ألا يصل الأمر إلى هذه المرحلة.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/91662" target="_blank">📅 16:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91655">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cT8VV7lxUPZDDxC-4H1AbNS8cLvFqDh4G3FtYmuzXWAsyP43paSO2ezVMP_e38jywqHxb6ca73Y7j0LTu_C2wbEzJqdqq6KMjnOmj6Yden7B7ZmVp1wovXwaw47_HtKyI1Wl1ZXTNPzNbkaTc_SyM1y-zru8HGizqu5sgRg_1P3pLjtiGry9l7Q8roET89-0VmoKGN1dKRsO00xq6p9aYr8xrbEeGO5-Yefcv5PO1gV4B9_w9rrIlNXH4T6M5QHJxrhPJbMo_0fGZmQAMvkOZumRSqSleNKeW_JDdTKGgUE_3BT0P4t7It3cyLjMUT8xN9M7tmkb6MuYTf6ZdIcUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnQ381OpRjWGuRlF8yl0BGUKs8FeuvxC8KXIEAT4XD7ATbyPcHsaNL0ieE6LXM1ovEKvAoGhQMWVdLYl8_vr1Jowh0pWOpkxFcEtSlS0695UkM2MAxWRHOdqEbqCxuOTpc6Kds0IaJM12xbkdg6GZEDP6Cty7R6onQrv9s9Q0qlrfbZMqMVUwsv6J9yJFRrRG4ntIz0wZ5O-HTYNq63AB6VoyxJ7shRtShjqdfTpGUHsBjh0PmHFHMgt5HHb9ob5wJR9jIhZZQRBPZbKrnPmmCBGxkEAsIx30jYT_l4ZcDYqsw7ZyNZjO82OmyFTd3SIWHUUvptBjjkZvpzaU89_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JALDIcZDNst5q7wByRBKWUbSXcGWRclTUI-is5oPr8WCqDNb1JMBkjiwXhLWhgtcW3re7_Hxwtjoya9p_as4Zo2V23q90q0i1vqIE1vBuqZWFHXXYpwT8VJ4_n6OL1al8Rqi1LPSOQLqlQThzKc6G-lfr34vm9klt2NdWuyZJNJoofd5zkk7U9wAvOLs_YXlCWS9Z7jeBKuMQ8bPVTtK4gL-V02ZJ6M3tzw0nidVA8ZalT8IlYBqimVXM0rCuaqeUM66EXjx6049nRxOntiTYbx2Tsw7h2lYYjdQPQFx-3H1DkaVZsbnoDUuO2I2YeoRenu7FmXdpSCf4r8obliSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/im7WVvduIqk3XiELxexxWTRVaNv3qsvQ00hdgG5wpL07VFpSitQAwR4lUKu8sWuyup0w4gNHyj9bLFTWu3TwmlbudNMHM9CgVCFyiWkH-nmyDvU8AuCsndJF7mOgCQbEaFcV1meLzlkqm29Z46-Js5hvx3j-YSkwuoq8pEenVbKpNooqTyNChDEIselLhO7F_jy6HcmO5atRbkMj2vRQ9HgNOVBPxf4R9dYrSWfVkxWZKBLhyuz-x_I3028bMjdkePmQXVaRSspHQmiNP595Vw2Jtwo6nUaPOv0HSCwhdEQAUU0pmtsyK0j6GNeXMf3YS1USSpeTi2LoGf94XutO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAzC3BwvA7f3A1Y42ipxwU6fKxhBMa8_Yh6q9WDrIykfiQio3jm12uq6xuA-WQD43Il0pRAyA5OSpe3gBdye9WrhDPjUej7Nt251oC_8aalxI5qASwvcJJ4bXexcJyYTEhfuOVZlbBOt66T0SQpQwwLx-ta59aP0oJdrZxPiSnahH_93t6vXaEBXFEy43IXrhfGV9QrA9BiG5qAXr0JwnGBM_yqSQYD2KM8S8ri-j-y0RcMtGkGKwCd0X-GA7nD0xTT--KF9yRF2voExwTrq-wEOZ93VU02h3yyHVRR2feXmLzUqWWn9U30WsQw8t-ga4uTX3KlxZwiiWRvxJwyazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gz70HSsI5ev5u26De9CHdvaulTHVOoxV1Bur8c_RNYIR0m38YC8drlujOUC7gtzUJd98Wl0O1GH_j1-ObO5re-fY0ZU-T2yCW7wlm5s6VyBebseVxj9G34mcfXJ1nT2hJFwaMROqTSjL_ppsXDbrHoSnUhkFNAyMFiISAC9nNJ04iSD4TrVXozOk2d9PdjDyj7Uu2kpX8co2X22HAfCflJdDjcVMu1frNIdCFyCV54-rPkO6llU5Sxf00Uc1UbZApEHEsC6gRF3T7o9kAFOxK8uJLrEpirzLmPN1SUhR1mqApRl2UU0oR__3X_9kiWL9DPFrwMNZhhNgICFn9S8gng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7rbs7it1DyHq7NeoDz0aQnKwtu3lJKPWRTwceaucz5XdaRy5YRe5RvJ15rT2htlqmdJYKlG-ZbmTeeIQnPkbi7l4mAiJlm0MiCYY3W0R4weTb4s_dCfVHzRzRb9CRlJsKtX6yGKW_KpN93sbne5EvwGA5XigP1cVocNKhQ4bqJ2wOhM1lMBNgF1hyTNdJ-mp1ssLOdCTDwuusDBYfRUwM73D_ueK858fvorQrsNlxRToNhM3Gu5Rj4yNbqbo82a3sCcI243NfrAHAWhavIUclBVCC4xPFsuUHVYT5D3L7lFf1HCv0QSzbc1YDYxDPloFCR10XJ5bN7n4dBO7WP4Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من ساحة التحرير.. انطلاق فعاليات إحياء الذكرى السنوية الثانية لاستشهاد السيد حسن نصر الله والسيد هاشم صفي الدين رضوان الله تعالى عليهم في العاصمة بغداد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/91655" target="_blank">📅 16:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91654">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL6JTqYGAFTjXm0SLNZUv1XA0WOFoSTPpE6-PX703od0oly8hCWwj_xIHckNJ6vM9HtOpNILyQJAhKBHm1zEoi7ivd3cQs31wIVSofeO5XR94Zzy4ZISzyL6bvnSWVf-_msfFfk3fTCgf-0zJe8oDKTbXL4MWpy-FHDFe-fEIz50fQixwecepptFlPS66xHOnUoBrunf5ROWrFBGk8pDmhQZHC8LdIxsuKgVgYJRuFjMTZ2ulRxjsBdj7rge48KBfgxsHz2jSTP2wljO1qe1tuI2BWgEeMotuUo0zeA-UqoC8bYxpfAds_23qw3jT_2iAUtjFT4nSXH3mXHSwtLPWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
سوالف الگهوة   سوف يعتلي صهوة الجياد اليوم ببغداد فارس من بني عامر …</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/91654" target="_blank">📅 16:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91652">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">البصرة ام الشهداء  تقول كلمتها عند الرابعة
بداية كورنيش جهة التعليمي
استعدووووا</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91652" target="_blank">📅 16:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91651">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الشعب العراقي سيقول كلمته
ساحة التحرير - العاصمة بغداد
بعد قليل
تسقط الوصاية الامريكية على العراق</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91651" target="_blank">📅 15:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91650">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
🇮🇶
المرجع الديني المدرسي يحذّر من الاستجابة لإملاءات الأعداء والتضييق على حركة الزائرين .</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91650" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91649">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_eGoiAeemtcV4YELK-Z-V8zJBDEkQNnYsnP-7jrTTcpIANM6UMflt7RNU1O4MpdWOm2cjXyYOzpgRFEmnyZItJRv8KuD7HpCSsLpJw3ePko9UlsEAT76kXOoZ6IortDhIik3srjcZprek3BV_bzZmqE-c0UL9YGUg_ysS33nHNV00nUAPejboRorP6YdyPfqfkE7e3gxTr0BQIw-faqwqqVwkMNRFapmua-xM7yojPjyQiLGhenZZmOOfU1cCzwQTglEOlMhDH2Sg_BI7N7oNzH0rGAeZXDUgPCt83hpjQM5ysxXQyq4QQyGlkNSeye4E1Cs51S5SStNgEbaw02RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
كتلة إشراقة كانون تؤكد رفضها لإجراءات الحكومة بشأن إغلاق المجال الجوي مع إيران.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91649" target="_blank">📅 15:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91648">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة 4 عصرا مشاهد جديدة لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرات رجوم في عدة جبهات.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/91648" target="_blank">📅 15:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91647">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb71pclX2cle8Bbh09GuDRwEkDjagtde43ny6WK9Y2TdyGa4I8yY9vqCLSr8lC7ABsX7wWA5JXf09nYeY9bIiQrVIT676erQ8XiKy1yWvhYIXHE06G8eR1PpPyXAjLyB4jX7xbqunXAxpF9BIMAsm2HfaxI5dnyA3zKow7DaBHWaeuQy10a5uVQVIZtf_NYZB1h0AEWqIQ9btxk3Y7GCJvBUs7Dfkv-hj6bRkRLp_dPQk0sbOob1nk7YK9gLdXs_55HBoNZVp8AqE0HbCWWeg4UJzifz5p2LB1nFxLApI3KfFPWbzDVIq1raQ3Wdu5Qk-_ikSkJw2W_0H6Fp4QjWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
العراقيون الشرفاء سيكسرون الحصار الأمريكي على ايران
ما ملت امام حسينيم</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/91647" target="_blank">📅 15:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91646">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAbyOr8ss-6cgqQL_5E2FJvZRSVBITebA6wlkoz7X84Wy2nYbWv4wh_HPLqabkZK1Ij6_wbMEmQy1R_CQb0WEAkB4c8BgN3crGHhOe0q82MntHfwHVKyQMnE3QYxyv2kDgBRK3JNRz0jyxUveRbAXuBbExDoAxPlzBz5G2X_2TuK1AlLivnTplg44tagMM80E95dD7IQ56Zphuh5hPl2XyHYGfZ-PHChkW7QanO-4EnQt3gbu0rknLxJfma2knoAZlviHmTwZPzA-FlKE8Ue9sJ9h0qm83f7zO4WqydPwYaAvWKyQyt8yOuajmKxXXuVupyeANE5bNLiJbkQZXKp6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇱🇧
تنشر لأول مرة
نفتقدك يا أبا هادي " درة لبنان الساطعة مع سماحة الشيخ همام حمودي "</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/91646" target="_blank">📅 15:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91645">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎬
*افتقدناك يا أبا هادي*
🔻
الشيخ أكرم الكعبي: أنت ممن يستحق أن تبيض من أجله العيون، وأن يبكى بدل الدموع دمًا..
🇮🇷
انتاج: مکتب حرکة النجباء في الجمهورية الإسلامية في ايران</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/91645" target="_blank">📅 15:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91644">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
🇮🇶
النائب الاول لرئيس البرلمان العراقي عدنان فيحان:
بيان حولَ الموقف الدستوريِّ والقانونيِّ بشأنِ قرارِ تطبيقِ إجراءاتِ حظرِ الطيرانِ المدني الإيراني في المطاراتِ العراقية.
تَجمعُ العراق وإيران روابطُ جغرافيةٌ ودينيةٌ واجتماعيةٌ ومواقفُ وتحدياتٌ مشتركة.
هذه المشتركاتُ تُحتمُ علينا، دولةَ العراقِ وشعبَها، أن نقفَ بجانبِ الجارةِ المسلمةِ وشعبِها، بل هو واجبٌ شرعيٌّ.
﴿مُحَمَّدٌ رَسُولُ اللَّهِ وَالَّذِينَ مَعَهُ أَشِدَّاءُ عَلَى الْكُفَّارِ رُحَمَاءُ بَيْنَهُمْ﴾
﴿وَالْمُؤْمِنُونَ وَالْمُؤْمِنَاتُ بَعْضُهُمْ أَوْلِيَاءُ بَعْضٍ﴾
وواجبٌ أخلاقيٌّ.
فإيرانُ أولُ دولةٍ فَتَحت مخازنَ سلاحِها، وأرسلتْ قادتَها ومستشاريها للعراقِ أيامَ مواجهةِ عصاباتِ داعشَ التكفيريةِ، بينما وقفتْ دولٌ أخرى تتفرجُ، بل بعضُها يدعمُ داعش بالمالِ والسلاحِ، وهي الدولةُ التي تجهزُ العراقَ بالغازِ الطبيعيِّ رغمَ حاجتِها الداخليةِ إليه، ورغمَ عدمِ تسديدِ العراقِ المبالغَ المستحقةَ بذمتِه، والتي بلغتْ ملياراتِ الدولاراتِ منذُ سنوات.
إنَّ هذا القرارَ المُستعجلَ وغيرَ المدروسِ لا يتماشى مع مبدأِ الدعوةِ إلى النأيِ بالنفسِ، وأن نكونَ مُحايدين، ومُخالفٌ للدستورِ، فقد نصتِ المادةُ (8) من الدستورِ أنَّ العراقَ (يرعى مبدأَ حسنِ الجوارِ، ويلتزمُ عدمَ التدخلِ في الشؤونِ الداخليةِ للدولِ الأخرى، ويسعى لحلِّ النزاعاتِ بالوسائلِ السلميةِ، ويقيمُ علاقاتَه على أساسِ المصالحِ المشتركةِ والتعاملِ بالمثلِ، ويحترمُ التزاماتِه الدولية).
فالعقوباتُ الأمريكيةُ الأحاديةُ ليستْ (التزاماً دوليّاً) على العراقِ لمجردِ أنها أصدرتْها، لذلك لا يكفي دستوريًّا أن تقولَ: (أمريكا فرضتْ عقوباتٍ، ولذلك نحنُ ملزمونَ بها)، بل ينبغي أن يكونَ هناك سندٌ قانونيٌّ عراقيٌّ أو التزامٌ دوليٌّ نافذٌ على العراقِ يبررُ الإجراءَ المُتخذَ ضدَّ إيران.
وإنَّ هذا القرارَ هو تعطيلٌ للنهوضِ بالواقعِ الاقتصاديِّ والتنمويِّ؛ لأنه أضرَّ بشكلٍ كبيرٍ ومباشرٍ بمفصلٍ مهمٍّ من مفاصلِ الاقتصادِ الوطنيِّ، وهو السياحةُ الدينيةُ، حيث يُعدُّ الطيرانُ الإيرانيُّ الناقلَ الأساسيَّ لمئاتِ الآلافِ من الزوارِ الإيرانيينَ والعراقيينَ بين البلدينِ، خاصةً عبرَ مطارَي بغدادَ والنجف.
فالحظرُ يؤدي إلى تراجعٍ مباشرٍ في الإيراداتِ السياحيةِ والتجاريةِ، وخسائرِ شركاتِ الطيرانِ ووكالاتِ السفرِ، وتوقفِ شركاتِ السياحةِ، وانخفاضِ إيراداتِ رسومِ العبورِ والأجواءِ التي تستحصلُها السلطاتُ الملاحيةُ العراقيةُ لقاءَ تقديمِ الخدماتِ الأرضيةِ والملاحيةِ.
هنا، وبصفتي البرلمانيةَ، أوجهُ سؤالاً إلى الحكومةِ العراقيةِ:
ما هي خططُكم لتعويضِ الضررِ الحاصلِ نتيجةَ هذا القرارِ لقطاعِ السياحةِ الدينيةِ والعاملينَ فيه، أصحابِ الشركاتِ والفنادقِ وأصحابِ المهنِ الحرةِ، الذين ستتعطلُ أعمالُهم ومصالحُهم؟
وما هي خططُكم إذا اتخذتْ إيرانُ قرارَ التعاملِ بالمثلِ، وتوقفتْ عن تزويدِ العراقِ بالغازِ الطبيعيِّ، وانهارتِ المنظومةُ الكهربائيةُ، حيث سيفقدُ العراقُ ثلثَ إنتاجِ الطاقةِ؛ لأنَّ إيقافَه بالكاملِ يتسببُ بفقدانٍ مباشرٍ لما يقاربُ (30% إلى 40%) من القدرةِ التشغيليةِ للشبكةِ الوطنيةِ، وهذا يعني زيادةَ ساعاتِ انقطاعِ التيارِ الكهربائيِّ في العاصمةِ بغدادَ والمحافظاتِ الوسطى والجنوبيةِ، وشللَ القطاعاتِ الحيويةِ: المستشفياتِ، ومحطاتِ معالجةِ وتصفيةِ وضخِّ المياهِ، والمراكزِ الخدميةِ العامةِ.
وأخيراً،
أؤكدُ أنَّ مجلسَ النوابِ جاهزٌ لعقدِ جلسةٍ استثنائيةٍ في حالِ عدمِ التراجعِ عن هذا القرارِ، ولديه خطواتٌ عمليةٌ سيقومُ بها، وكذلك إجراءاتٌ رقابيةٌ بحقِّ الجهاتِ المخالفةِ للدستورِ.
ونؤكدُ أنَّ قرارَ العراقِ يجبُ أن يكونَ قرارًا وطنيًّا مستقلاً، نابعًا من قيمِه ومبادئِه، ووفقاً لالتزاماتِه الشرعيةِ والأخلاقيةِ والدستوريةِ، ولن نسمحَ، تحتَ أيِّ ظرفٍ، أن يكونَ العراقُ شريكاً في الحصارِ على الجمهوريةِ الإسلاميةِ.
عدنان فيحان الدليمي
النائب الأول لرئيس مجلس النواب
26 - ايلول - 2026</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91644" target="_blank">📅 15:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91643">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
سوف يعتلي صهوة الجياد اليوم ببغداد فارس من بني عامر …</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91643" target="_blank">📅 14:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91642">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09f372b1b.mp4?token=cUUGcaWvhPhIu4JwtegdAOhg0hlRQ5ALRaMPk_gjwlcbg7qn-VQRft3LIVaEkwt4jnxdRkqYqupauaNaATekJlFompuRW7-Cb9NAK7QOnV1Vbv-CnNJPjTB-_-rrPHPG6RHFVZjVXnFmF96Apj1Wsf7PfDdnq34Q1Kq2WkzNqGJ4zSr4ng25vuQ_vHb_CjS_oQ83WBySICcPZzm0RX_bXVBJlB7dCbBUZSRO4icVGZfimt22IbxC4eAdurCOcG5Jf695L0AHVOeLRKjMsklPVgZtQS7PHFfIe8F1-BsiFcAQw0xWmXljywkGvBHuN1w3gheudiOq_O97JzyJOmoShg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09f372b1b.mp4?token=cUUGcaWvhPhIu4JwtegdAOhg0hlRQ5ALRaMPk_gjwlcbg7qn-VQRft3LIVaEkwt4jnxdRkqYqupauaNaATekJlFompuRW7-Cb9NAK7QOnV1Vbv-CnNJPjTB-_-rrPHPG6RHFVZjVXnFmF96Apj1Wsf7PfDdnq34Q1Kq2WkzNqGJ4zSr4ng25vuQ_vHb_CjS_oQ83WBySICcPZzm0RX_bXVBJlB7dCbBUZSRO4icVGZfimt22IbxC4eAdurCOcG5Jf695L0AHVOeLRKjMsklPVgZtQS7PHFfIe8F1-BsiFcAQw0xWmXljywkGvBHuN1w3gheudiOq_O97JzyJOmoShg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
‏مقتل 11 وإصابة 30 آخرين في انفجار بمدينة ديرا إسماعيل خان بشمال غرب باكستان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91642" target="_blank">📅 14:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91641">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">النظام السعودي يستهدف معلم في منطقة قطبين اليمنية مكتوب فيه أسم الرسول محمد (ص) في اعلى المرتفع.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91641" target="_blank">📅 14:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91640">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني:
إغلاق مضيق هرمز أمر طبيعي عندما تقطع الطرق أمام إيران.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91640" target="_blank">📅 13:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91639">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇶
🇮🇷
ائتلاف الاعمار والتنمية:
نحذر من الانعكاسات المحتملة لحظر الطيران الايراني على المصالح الاقتصادية العراقية، ولا سيما القطاعات المرتبطة بالسفر والزيارات الدينية، لما قد تسببه من عرقلة لحركة الزائرين بين العراق وإيران، وزيادة الأعباء على المسافرين.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91639" target="_blank">📅 12:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91638">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
وكالة الأنباء الألمانية:
استمرار البحث عن 18 مهاجرًا عراقيًّا يعتقد أنهم غرقوا قبالة سواحل ليبيا.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91638" target="_blank">📅 12:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91637">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
🇺🇸
الحكومة العراقية:
"قاعدة فكتوريا" خالية الآن من التواجد الأميركي.
‏مباحثات في إسطنبول لإخلاء موقع بعشيقة.
‏إخلاء تركي لقاعدة بعشيقة خلال "60" يوما.‏
3 فصائل سلمت أسلحتها من مسيرات وصواريخ.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91637" target="_blank">📅 12:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91636">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_5qH7L6kXpFgp1ce6oz1vbKvjdfSD09HAyQ0lAtkMwVLVw-V84kx0ZXjagb7gG3SwhmNcYQyllP-O2wZ088vL3kmJpCs5JffBz7OHC-rHKnMePFxM_i1jtyFNXZU0lfYyyaNaM5t9GN4vBky7Bw-FWehMMlXVZ7x7Sz_ePnycgWmd4euvwa02PxB-NrsqacF7ScUs90GKbXcALbQNfGwR-vd_H54-NZ14CcD87YVif9BJn_43zs_0LSzYJEHwgZ1vfJCFIau_9LIcQQE11mmbOqPkz7PHoLyyCUuOHB4xGZzQm0FfEATx6E-TkM-mOt5EWtgEaG5nsTQB8cAqUo-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ قيس الخزعلي حول الحصار الجوي على الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91636" target="_blank">📅 11:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91635">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔻
مؤسسة النفط الليبية:
توقف وحدة في مصفاة الزاوية بسبب إغلاق مسلحين لصمام على خط "الشرارة".</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91635" target="_blank">📅 11:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91634">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91634" target="_blank">📅 11:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91633">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opZIea2U3FsnlyaMdBkrR4Xi6oAAVNO1nzaAZu-kl3OMx5unqzVGnJmv0TVqSRBnG-RTlCaKK2RkW6hQKFLwB6t3Z29uygqMMTbsCMNaLPP4kgk09eJyznU1aOaJXZTdaWG7bdKYZi8hCHkJfz_UBfpVh8_obPCVGw8mi6e7FDW9MMkL3LafuhjfNM7e1Ay_6v3xUWbQcb6kpd7S3tGVFtZwZlFb07jEcajGpSteKZeyso9mlnBQebgdz-kP_MOZR5LY76B2Q6KguroQ4PgIlYNimI-tWa-_0qTBVZMMxUVw-LhnhJR_iLosP55Oo102Rn7vd2_N8Clsms0MHAj7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
حركة بصائر العراقية
على الجميع الوقوف بحزم امام تمادي الإطار التنسيقي بحكومات في الانصياع وراء قرارات امريكا الجائرة تجاه ايران</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91633" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91632">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
اللواء كوثري بشأن الحصار الجوي على إيران:
سنتخذ إجراءات لإفشال هذا الحظر وسنوقع عليهم مصيبة تجعلهم يندمون على الحصار.
الحصار الجوي لا يمكن أن يستمر.
الضغط الناتج عن الحصار الجوي على إيران يقع على عاتق الشعب.
لدينا خبرة في تجاوز العقوبات.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91632" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91631">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
مدير عام مطار الإمام الخميني:
الرحلات الجوية إلى شرق آسيا، بما في ذلك الصين وفيتنام وماليزيا، مستمرة.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91631" target="_blank">📅 11:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91630">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
وزارة البيشمركة في إقليم كردستان العراق:
التحالف الدولي أوقف المساعدات المالية لقواتنا.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91630" target="_blank">📅 11:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91629">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
وزارة الدفاع الإيرانية:
في السنوات الأخيرة، تم نقل جزء من القدرات الاستراتيجية للقوات المسلحة إلى بيئات آمنة وبنية تحتية تحت الأرض.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91629" target="_blank">📅 11:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91628">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
المكتب الاعلامي لرئيس مجلس الوزراء:
الحكومة العراقية تجري حواراً مباشراً مع الجانب الامريكي لاستثناء بعض المطارات العراقية من الإجراءات التي اتخذتها وزارة الخزانة الأمريكية بشأن رحلات شركات الطيران الإيرانية إلى مطارات دول المنطقة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/91628" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91627">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THxOc_Mi5XN3bIcdfxJRDNhlPfvSnkLV6NWXCz7Kay3ZkGhmcGYf3ESSib2Kz11cYMFkcFFAdDRSBi1c6mGO_xJQSSzpi6cMEy54BBJmNrSnnwMVW6NLp34e97NVSZXwbrwHsobxFKR1BoTXqPNFA_dzyjzdYEmEtTcmhQb_7aQWnzq_jydd1usiVQGoK23zuo8d7mfpPfS6GMg5xw6H5ko-h1TobRqrYj8jsOgPXzb89F6m9Pz7YL4KQv27BsktOmQyLWiSeEr9otHwoMs53cTbtTUaGVtLxoiZgezPiBNlSgXpse4_MweinCZqlwlm77wbzK7u32rK0vN6Hy0M9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
غارات للطيران الحربي الصهيوني على بلدة سجد في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91627" target="_blank">📅 09:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91626">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBP1yz3c-GIRrkQVQkzuC1TgfPHdYccR4ZIdKkIaZLhI-zcCX_GZi0LK6huHc-e5oBJmr8r8zYq3rAnEL7IdW2iPfx1sd4zpKNvtMaTtfao-kP5tB9eWZetVHtsqJtuSBj57mGXnw3xsFxDwPIlnkbzQJYNiiDQ8VeEnUSuCiJ6Gu_zUbelV6nv3vbESzm9J7iIbGUE6pzAGR22vJc4mqfRKEPxm80LPYSv02szRPC6wvOxAGH-JmmuriRfs5-jRV0YAi8i2SZpIuae3txQfGFxc_Q_ZP4lE7uyh2-ykfrODFUHDZyoInMBYhwiHDaYX5IAgO66GAn4NNwKjeWpr-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
🇷🇺
إنفجارات عنيفة تهز العاصمة الأوكرانية كييف في هذه الأثناء.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/91626" target="_blank">📅 08:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91625">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا   صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/91625" target="_blank">📅 04:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91624">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">النظام السعودي:الدفاع الجوي اعترض صاروخ باليستي أطلقته قوات الحوثي تجاه خميس مشيط.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/91624" target="_blank">📅 04:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91623">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3PpqI8XmonpjLOU6GX0_pvtC3phMKVpFHGYEUxIxVvotuY2bGvDt24ya7xua7ZSLG48VZznFSCkoSDBLkh4RmscLs9RnUFdi7QM46-UhZUVFNAXmImirozhKE7A8dxTSXAks9weNG3vuV_ABk195clUfc7bob2l46OoTzvzxfCU2lCDG04WAKuDd0hdXxgyJO65cKBiCgj9TMjt3jCMWE7X0UBaiuqc4dYaNWz_OCMbTYgJFYT0NdsI6r9gmMjGEAfTk9fr05hYEGK1cD4ztkNJsEOgw73Kz1jeweeg3iW-V7OEFjRnFcVrsVUo02a7hxCNzirpddqTIT_UC_oxeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو انصار الله حزام الاسد: جار تأديب وتربية عيال ابستين</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/91623" target="_blank">📅 04:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91622">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مجددا خميس مشيط</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/91622" target="_blank">📅 04:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91621">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POZ-253ndDK6KCUdW5BuRLFxnFMLPGlcSIEg9_AUdJ1bpYrunG0PCWzk05qwiW7tCeACMDZOdTXgvm7OAqtFEBrKn5xBMzwHIwvgnu-6yv4-qUtXYPPh1_l_xj7LUTrYNcLBD79qSXWfrWYOXI3Au6fD6iEHuh-9WnTCcOV7mC2AgAoKki3qs_wfXfJ93DaKD5c0jEaLbqnJIoHLN7YcwgRqWmoLJ6rTcB-2yvzEregEX5v4ZpTdLJC0v_94EF07KiT0LMBdrMhl2hpePVQbk8O7iWXeyESSl8NNIIbbMBDBtVJl-5DXc3r_5vsSXQ4jyEtPnzlgpkuVK3Vp42pMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇺🇸
ترامب ينشر مضيق هرمز تحت عنوان "مضيق ترامب" وسط توقعات بالرد من قبل هيبت الحلبوسي</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/91621" target="_blank">📅 04:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91620">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مجددا خميس مشيط</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/91620" target="_blank">📅 04:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91619">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">النظام السعودي: هجوم على الرياض</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/91619" target="_blank">📅 04:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91618">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏النظام السعودي: نرصد ونتابع تهديد صاروخي ومسيرات باتجاه المملكة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/91618" target="_blank">📅 04:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91617">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تفعيل منظومة احذف تكفى في الجنوب السعودي</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/91617" target="_blank">📅 04:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91616">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ابها تحت القصف</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91616" target="_blank">📅 04:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91615">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات تهز خميس مشيط السعودية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91615" target="_blank">📅 04:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91614">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات تهز خميس مشيط السعودية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/91614" target="_blank">📅 04:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91613">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ول ستريت جورنال: ‏ترامب يرفض وقف إطلاق النار مع إيران ؛ ويتوقع تصعيداً في القصف بعد انتخابات التجديد النصفي</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91613" target="_blank">📅 04:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91612">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91612" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/91612" target="_blank">📅 03:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91611">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات تهز الدمام الان</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91611" target="_blank">📅 03:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91610">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا   صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91610" target="_blank">📅 03:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91609">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ljh45Vthbrp6GpLiGHYhKRIFPxsptMrffjdTswfMt8FQZ9qmfuwVnpEkCxCOObgPpBdze4IluT015x5XWssn4yZZdSgf_yyd0fTfOwuETsR5DLOO2j-T7CXUQmnq_BpQrdENu_Ahq8TLQGIsAjDR_PplwIBRzHqy2HljZl3jn8CyA84YdZd5MHznzkkZhuYhKdrpf3AImpeEYKV9ffTEHv7b83BqSl-7FxyTECuZhpavaiKPhsBslYGHKRcUIFVNCb_UTX8f6h861O0YRauqfwVEXlNibD2-NLpd0-HCG_pfCJx_dZMtL-VqSxV7ZGJpLMBVol_yyOMDLlooI9mL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا   صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91609" target="_blank">📅 03:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91608">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇸🇦
🇾🇪
مصدر محلي لنايا
صوتين انفجار سمعا بوضوح في العاصمة السعودية الرياض. الأصوات سمعت قرب حي بنبان قرب مطار الملك خالد الدولي .</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/91608" target="_blank">📅 03:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91607">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">والعتب موصول لسماحة السيد مقتدى الصدر
عرفنا السيد مقتدى الصدر انه مع دعاة استقلال العراق وتأثره وتبنيه بمقولة لا شرقية ولا غربية
فكيف يرضى ان يخضع العراق  للأمريكان ويشارك في حصار على الجمهورية الإسلامية الإيرانية المنصورة بأذن الله
واين تغريداته التي تعلمنا منها عن المشاركة في نصرة المظلوم على الظالم ؟!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/91607" target="_blank">📅 03:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91606">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امر مستغرب جدا
لا موقف """جدي """ عملي معلن من قادة الإطار التنسيقي الشيعي حول ما يجري بمطار النجف ؛ الإطار هو الذي  أتى بالحكومة ؛ و لا نريد تغريدات لكون البيانات لا تغني ولا تسمن
والعتب الأكبر على من نحسن الظن بهم الشيخ همام حمودي ؛ السيد هادي العامري ؛ نوري المالكي ، محسن المندلاوي ، عبد الحسين الموسوي ، عامر الفايز ، الحاج ابو الاء
لديكم برلمان كامل وزارات ماذا تنتظرون  ؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91606" target="_blank">📅 02:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91605">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
السيد صلاح المكصوصي :
لقد تعودنا أن تغلق الحدود وأن ترهن القرارات العراقية بإشارة من سفارة لا تمثل إلا الذلة فإذا كان منع الطيران يقطع رحم المحبة بين شعبين دمهما واحد فاعلموا أنكم لم تمنعوا طائرة بل منعتم الكرامة وأسقطتم ما تبقى من هيبة الدولة
من يظن أن منع الأجواء مسألة ممرات جوية فقط فهو إما جاهل بحياة الناس أو متعمد تغليب مصلحة السيد الأمريكي على مصلحة العراقيين
فبسبب هذا المنع المذل تقطع الزيارات المتبادلة للعتبات المقدسة آلاف الزائرين العراقيين الذين يزورون مشهد وقم وجمكران والعتبات في إيران وآلاف الإيرانيين الذين يقصدون كربلاء والنجف والكاظمية وسامراء اليوم يقفون بين حيرة الطرق البرية وكلفتها وتعبها وتحرم أرواحهم من زيارة أولياء الله
ويربك طلاب الكليات العراقيين والإيرانيين الذين يدرسون في جامعات البلدين طالب في كلية الفقه أو الطب أو الهندسة يمنع من العودة إلى مقعده أو من لقاء أهله لأن قرارا انبطاحيا أغلق عليه السماء
ويحرم مراجعو العلاج من السفر لتلقي العلاج في المستشفيات الإيرانية كما يحرم المرضى الإيرانيون من المجيء للعراق أرواح بشرية تدفع ثمنها لأن حكومة بغداد خافت أن تغضب واشنطن أكثر من خوفها أن تموت امرأة أو طفل على حدود البر
وتشل التجارة مع إيران السوق العراقي الذي يرتبط بالمنافذ والاستيراد والتبادل التجاري مع الجارة إيران يدفع فاتورة الشلل والغلاء وشركات النقل والتجار والأسواق تترك ضحية لابتزاز الدولار والتهديد الأمريكي
هذا هو وجه القرار الحقيقي
ليس أمنا ولا سيادة بل محاربة للزيارة وضرب للطلبة وتعطيل للعلاج وخنق للتجارة من أجل رضا سفارة لا تملك حقا على سماء العراق
الذين يدافعون اليوم عن هذا القرار تحت ذريعة أن الحكومة مجبرة وأن أمريكا ستضربنا وأن الدولار سينقطع هم أنفسهم حفظة مدرسة نخشى أن تصيبنا دائرة ومدرسة بيوتنا عورة لا نستطيع أن نغير
أي سيادة هذه التي تبنى على إذن أمريكي بعبور السماء
وأي حكومة هذه التي لا تعبر عن شجاعة الشعب العراقي حين تقف عاجزة أمام قطع رزق التاجر وعذاب المريض وحرمان الزائر وتشتيت الطالب
إن الحكومة التي اتخذت هذا القرار المذل تضع مصلحة الضغط الأمريكي فوق راحة شعبها وعمق علاقتها بجارتها إيران فقد خرجت من رحمة الموقف الوطني ولم تعد أهلا لأن تمثل من ضحى بدمه لئلا تدخل داعش بغداد
فلا عزاء لمن جعل سماء العراق مفتاحا بيد البيت الأبيض</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91605" target="_blank">📅 02:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91604">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
🔻
إيقاف دخول الوافدين إلى المطار بتوجيه من مدير عام المطارات والملاحة  أفادت معلومات بأن مدير عام المطارات والملاحة، وجّه بإيقاف دخول الوافدين إلى المطار، وذلك بناءً على توجيهات من السفارة الأمريكية   وبحسب المعلومات، جاء القرار على خلفية مخاوف من إقامة…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/91604" target="_blank">📅 02:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91603">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
🔻
إيقاف دخول الوافدين إلى المطار بتوجيه من مدير عام المطارات والملاحة
أفادت معلومات بأن مدير عام المطارات والملاحة، وجّه بإيقاف دخول الوافدين إلى المطار، وذلك بناءً على توجيهات من السفارة الأمريكية
وبحسب المعلومات، جاء القرار على خلفية مخاوف من إقامة اعتصامات داخل المطار، على خلفية الدعوات التي أطلقها الشيخ أكرم الكعبي لتنظيم اعتصامات، فيما أشارت المعلومات إلى أن الإجراء تم من دون علم الوزارة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/91603" target="_blank">📅 02:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91602">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avkVAMNgZCKoJD-bkz_Frc779HRpq5rlLAxadi8Cg_3oB51iMSj3uKcqE1MGv4kdWpyXB3hDFepGRntU8h6Hpz6UrFZYq4E53C-GpVh6cnY_urgaRlVGdPQ8zoZ9DDh2SawdBdT3ThV6tJX-85dzdJYrg0qf93Spscik2P1xykRp98PnlQP7-dtxwWCPcQWCvxaN31bTHcdNPmYsIFLz2-0ZoV-Hj4vPd1-1Uwz9C59n80gA2w6WiA7JqaDKDVVMTXSJK-sgdLKz7WH3O1LlTjjmc9Qq_UXE6yyMvxse2HyZ1a9VRFJGS-eAcKPPHm46vpH37aAi6r8qS2M5LLfmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/aboalaa_alwalae/status/2103610717991563618?s=46</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/91602" target="_blank">📅 01:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91601">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91601" target="_blank">📅 01:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91600">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/91600" target="_blank">📅 01:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91599">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InCwQ270HGNUhQM_Xx1h9AqoaJFsJwAM6MihQo99Twp7LGxv20-B2d2cL6gng-JXE6IvjqxGWU4R9NXpbqhISy8lNbg7LmJAhOc19_dYm4PAHwi9rOX6_7JqQxzzTi3VY5Xm2R6QxFH1wEzDuYBe8Tv_8kJj0Y9KKPCYGzJIeNtnMNhjSAnUnLuBjGqx4Q7bySdTu40NNwCovuBMSegHit3Lpj8SMoCUoti-x4YaIovqu3bMIsUXOIuTpc1JkJtHlpMxN6ORyg0XXc7_xMSWp4GlTkznE7tPMuY0M9hm9GngkTxMGPXVEwCMH4c7KZm1dpl0QhT9F35CEJUearWhUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابو جاسم الذي نحبه : كلا كلا للحصار على الجمهورية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/91599" target="_blank">📅 00:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91598">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇷🇺
الغالبية العظمى من ناقلات النفط التي تعبر مضيق باب المندب حالياً مرتبطة بروسيا.
لا تمر أي ناقلة نفط مرتبطة بإسرائيل أو السعودية من هنا.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/91598" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91597">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
أضاف البنتاغون بهدوء 37 جندياً إلى حصيلته المعلنة من الأفراد المصابين خلال الحرب الإيرانية هذا الأسبوع، ليصل إجمالي عدد أفراد الخدمة الأمريكية المصابين إلى 861.
وتشمل هذه الزيادة 29 بحاراً من البحرية وثمانية من مشاة البحرية، لكن وزارة الدفاع لم توضح متى أو كيف وقعت الإصابات.
أعلنت البحرية أن البحارة عادوا إلى الخدمة بعد إصاباتهم التي لم يتم تحديدها.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91597" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91595">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قبيلة الشغانبة العراقية تعلن تحرير باخرة عراقية تعود لأحد أبناء القبيلة بعد أن استولى عليها قراصنة صوماليون أثناء إبحارها قرب السواحل الصومالية حيث خاض أبناء القبيلة مواجهة مسلحة مع المجموعة التي كانت تسيطر عليها استمرت أكثر من خمس ساعات، وانتهت بمقتل عدد…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/91595" target="_blank">📅 23:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91594">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قبيلة الشغانبة العراقية تعلن تحرير باخرة عراقية تعود لأحد أبناء القبيلة بعد أن استولى عليها قراصنة صوماليون أثناء إبحارها قرب السواحل الصومالية حيث خاض أبناء القبيلة مواجهة مسلحة مع المجموعة التي كانت تسيطر عليها استمرت أكثر من خمس ساعات، وانتهت بمقتل عدد…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/91594" target="_blank">📅 22:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91589">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXePME5tcT39ZXWVUY0eV1oKnOuyA00nQH-Z_L6p1b7RmEajEcFw3obPd0fKKNdswRyt_fzOgKZ0e7OZfkvuKfs0A59ksKLKM2y-HODQu1H275lF3gb5Q0V0flH7aqs2boZeZDbKFK19IMK04M0xFl2o7jzLdjv90ZSXrn5PJcIgfb9C11TYkdA4xpRKUysUKQQ5knnYc-9htgG10TTan0Y4bf-lorVNpw-Bf0XPb34TZxw8uFFlbr45BFrHLo5RM_AoLdPyFqR7dVaix4Vhbp0ArqywkW5ne1VkFo4sh_dzvnaoDkEAoeQfYdprLg0tXH99mFZgrVe3j2ky6Gg32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sH3zJOq0Mo9Rp1X4hibYnHxTpOh3ZOkJcd1XAGX0IcRHm8DwwGJXy0K8Y-6grAMvdFfQVXoA7JPNpUJCAVmZ_hTFMakHNluZFJzUuLia-gB5zaTLs8TTPrnYhMJ90f9NaOIFpigf7I6c0frFYyQZzGWnbGfdSXTbU8XlduK3VLVKDYBy5icGCVhskaEcD1_IIEbZv10FYpmN67eEfd5xHTR9q9p-zG6XY1Tra08lE3FqMBe41bRSNI5HN-DOZRbovMobXhvtGOuh0qlgCfdWoBciXsvhrqHksj_CACYQ5sH2pl_2VyZFO7amwtuRB1oEz8Byv8U9hsKnR2yh8V02QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhg1ft5iCD2UHYRz18itVtiElxR5aHiPKYgjsleWkbAaCFE6DBAYMiFo6xGRjLFFtqG0UYYyl0So_HVEsPNuBYRJ3o2V5E26LozhimYIS6s4DkgixMl2vElwGvBKZ_gYg8y5m8EmjjRmCm2ogtqppUiOq4EOMkxREKJzrIjBe1k1Wk67pqIAp4miB-lLm6V8FST-9MIfypwFHe8ndnZqm6abbMxKobMoVVa34FjpbW4RpH8rMEYMypXW9c4a7GbRO6OTnvXVYTkSPazM2F4dyP1b71xFOVzm0A9F89AFH2JnEvg32G-bKtAWCo0RFJuw4hXzYJxcvRef4GCSYte_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiWTghnpG4_gFVTLU2JlDH03Z5NGpWbnoaBPp3XzPVYwGZonmz_h0NwQp_PGz_B_UWUUD6rQIqzPoG1J09x9p1hkzzaHn2rZ7P1Yc1-kd_JxpOwBL-JZIV3ds07kbA115DGerDRIXhcdY9HqPcPplZklWcfN3XXo7PaApCKD6OnbcN14zTtTRLV0fVRBW58uFRecN7mBrQ2sZCtZupRQ-zmE51-KbFdFme6mqpErPxfCRxo6WwMBpSUD13iEzKJOYEHOs-HOGNrVg4Y8NaEfXvuFIIPnUtd-Jym4uzGiJyzpnYwc2zfLX-inyAJzliYi5jnc6hszXzn5dpnSszwkag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d931c9710.mp4?token=KWp7czMcB9_kqBcnrTwthguteBVbmddR82iXSUi7q-Hxh8nfhvhzkq8MHM36hNMdkwXOyRRSyNA8dCxdfgHT7t8lQUs0lF_wQtFPOYmYSiIPvnEk-i9xGDpwHTg_JrRVKWT_b_XVdP0IM-eXHDuTLskVckObU79jXgrPCznMh8gRy0tv5K6jlSn75PBHQh29dU-lLN4wsyiqcWlRm_EAyBTV8zBgti6_iumwekvmaZyZnGzTBalA66xxIDZeqpcxKPMjFR0bM55iegYO6bRgi7eLLzar28o6bK8mELVt4foeDjGkNhwALNMqjbinhuYeXBX5Rz62rTVb-d-0jhGf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d931c9710.mp4?token=KWp7czMcB9_kqBcnrTwthguteBVbmddR82iXSUi7q-Hxh8nfhvhzkq8MHM36hNMdkwXOyRRSyNA8dCxdfgHT7t8lQUs0lF_wQtFPOYmYSiIPvnEk-i9xGDpwHTg_JrRVKWT_b_XVdP0IM-eXHDuTLskVckObU79jXgrPCznMh8gRy0tv5K6jlSn75PBHQh29dU-lLN4wsyiqcWlRm_EAyBTV8zBgti6_iumwekvmaZyZnGzTBalA66xxIDZeqpcxKPMjFR0bM55iegYO6bRgi7eLLzar28o6bK8mELVt4foeDjGkNhwALNMqjbinhuYeXBX5Rz62rTVb-d-0jhGf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبيلة الشغانبة العراقية تعلن تحرير باخرة عراقية تعود لأحد أبناء القبيلة بعد أن استولى عليها قراصنة صوماليون أثناء إبحارها قرب السواحل الصومالية حيث خاض أبناء القبيلة مواجهة مسلحة مع المجموعة التي كانت تسيطر عليها استمرت أكثر من خمس ساعات، وانتهت بمقتل عدد من المسلحين وأسر آخرين فضلاً عن الاستيلاء على أسلحتهم وتحرير الباخرة</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91589" target="_blank">📅 22:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91588">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_4kOV2kFUxgTtBDOsV5l7G2YLiB02HeZoLIVNn0xQEQGTDnsoCVgciW2KLVhZHiCm13QwofMCpZtM6HM7ZgSowZJPhlx_nzUSgFL6zlSqhMAs5-OBQ02tdkyWEbVVewTPS_YnAfW0CemJFUo57e4LHqGozilo6MwSyl_7rt54MoNxb6wUHZ0mXgJSQXcC9OYMvor9iDg0vy3ylJPnNOsQfLc3OnBtijRBsZ81aOexVEuEnkDlh0hinmEt8fbOTbmPCM33mCq0BMeyVh9P0NMOKBf6xPrXiT2KMken5K7Te6FhvVh-eW0c4_pz-ly9v9XPGzFZiqYU4igz9p0fAHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جماهير البصرة الغيارى تستنكر وترفض
تخبط الإجراءات الحكومية الأخيرة وامتثالها للقرارات بحق الشعب الإيراني الشقيق.
موعدنا معكم
🗓
الزمان: يوم السبت 26/9/2026
⏰
الساعة: الرابعة عصرًا
📍
المكان: كورنيش البصرة
نقطة الانطلاق: من مقابل طوارئ المستشفى التعليمي، تحت الجسر، باتجاه النافورة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91588" target="_blank">📅 22:17 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

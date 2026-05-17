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
<img src="https://cdn4.telesco.pe/file/c-fIwOuAj8X-QBoQKCG1dR0LCPLqSHpvF1rUIR1x5vGa89pknA3QYoTZhajQbEHajkVtS-cNZyAhkSjZ8iaBjPeUtLNxZAEp08-DF_CYuBidvrtZKwKgYW1y_yLmZPK2V7iMruj3fIK9fu3a9PHXjm6bKL9yji7yvn-bh1MprMJslrRwkhUxVqZGyLqe3J8i2qsMvhJvk7VuxGw0XWHQUX93SblUJIXcNH2Cv-qAC3VGxzfnlYNKh-IgN4ViUGuzqdaRKKxE-2NVNS2EGmIw5K2Yp6SYTRqpwbdheUR0slsiCtnz4Gj0wICYpxwwBJt6mnw-pYgjd1rrN4G6EjHWfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 254K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 22:25:48</div>
<hr>

<div class="tg-post" id="msg-75576">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⭐️
مكتبُ سماحة السيد السيستاني (دام ظلّه) في النجف الأشرف: يوم غدٍ الإثنين (18-5-2026) هو الأول من شهر ذي الحجة لعام 1447 للهجرة.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/naya_foriraq/75576" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75575">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 15-05-2026 ناقلة جند تابعة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/naya_foriraq/75575" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75574">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تشير حسابات إماراتية على مواقع التواصل الاجتماعي إلى احتمال اتخاذ الإمارات خطوات نحو الاعتراف الرسمي بصوماليلاند، في خطوةٍ تُعدّ بالغة الأهمية. وتحتفل صوماليلاند غداً بيومها الوطني، وسيقدم أول سفير لها لدى الكيان الصهيوني أوراق اعتماده إلى الرئيس هرتسوغ في القدس المحتلة ؛ وتؤكد مصادر في هرجيسا متانة العلاقات مع الإمارات، إلا أن توقيت هذا الاعتراف يعود إلى أبوظبي.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/naya_foriraq/75574" target="_blank">📅 21:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75573">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a281c93fa5.mp4?token=thFCm4bARhyJsrek1GJj39eU98124w8vkDm-fMU_X69xHCObM177nD4vRhlbnxWOLJOHCHZ7qbv3zhe8__ZfjTb0N68c0WPdTq-N7JuTyNbde9USB7IsEzY96OLGbrTyg0LO9yhyKzVv2j2fVt7lutvIivCW1VfUKSihKEw2bZyog_sy7xYNWFvkxloMlZFl2JziZhQX9AwiER-h1MrWuwisrXXu-eIMZkTDjiCJYbvHUF55HwNpR-OTMUjIihobN-0ks7VJzMC1nlF4JSJXQfGASnoNsmfewW_08vgnOZgToa-Xppq_ExDoVSGH9E6J8hrYWO33zi-0emgktCVyTHLz1ieDvXPATbsckgTWxsa7QLVjlL24xLNrl8J_qjXYbBIZNBscWcEBNjmUTmlxtJK895y8O9c2LRvteMbWRJ3B0i6h_W2IRomWn4ti4n1SK7SnXVqu_b4d0m_1wWaagJl4mErtcSDeDeCUQ1W7-aAlTcPv6E0yB_ysIQp1QItjdh-iUwf0P_bb5aKEyfj-4X8rjDNCcuNFE_1EHkw-ZJeyqmBi4xvlCwx0Jnys_rSoOKiFUl4F6mF8SI0y9jaMOsdMjI3AyR9zQxjMkea9SJfX68BZ5j-aRHzk4PJt6_PI07BbZKq_MDDZekrx4vxhcp_Xbii2vhFT93ZcH8yM16w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a281c93fa5.mp4?token=thFCm4bARhyJsrek1GJj39eU98124w8vkDm-fMU_X69xHCObM177nD4vRhlbnxWOLJOHCHZ7qbv3zhe8__ZfjTb0N68c0WPdTq-N7JuTyNbde9USB7IsEzY96OLGbrTyg0LO9yhyKzVv2j2fVt7lutvIivCW1VfUKSihKEw2bZyog_sy7xYNWFvkxloMlZFl2JziZhQX9AwiER-h1MrWuwisrXXu-eIMZkTDjiCJYbvHUF55HwNpR-OTMUjIihobN-0ks7VJzMC1nlF4JSJXQfGASnoNsmfewW_08vgnOZgToa-Xppq_ExDoVSGH9E6J8hrYWO33zi-0emgktCVyTHLz1ieDvXPATbsckgTWxsa7QLVjlL24xLNrl8J_qjXYbBIZNBscWcEBNjmUTmlxtJK895y8O9c2LRvteMbWRJ3B0i6h_W2IRomWn4ti4n1SK7SnXVqu_b4d0m_1wWaagJl4mErtcSDeDeCUQ1W7-aAlTcPv6E0yB_ysIQp1QItjdh-iUwf0P_bb5aKEyfj-4X8rjDNCcuNFE_1EHkw-ZJeyqmBi4xvlCwx0Jnys_rSoOKiFUl4F6mF8SI0y9jaMOsdMjI3AyR9zQxjMkea9SJfX68BZ5j-aRHzk4PJt6_PI07BbZKq_MDDZekrx4vxhcp_Xbii2vhFT93ZcH8yM16w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماذا حدث في منطقة شنان قرب الاديان لمن هي الـ عجلات العسكرية المدرعة ماذا يفعل الأمريكان بالأحداثية  ‏37R  KV 750018  3478349 ما قصة هبوط هليكوبتر عدد ٦ ونصب خيم أمريكية في صحراء الانبار جنوب ناحية النخيب منطقة شنانه الاحداثيات ‏38R  KV  69654  98230  لماذا…</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/naya_foriraq/75573" target="_blank">📅 21:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75572">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
🏴‍☠️
هيئة البث الإسرائيلية عن مسؤول: الولايات المتحدة وإسرائيل ترفعان حالة التأهب لإمكانية استئناف القتال بإيران.</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/75572" target="_blank">📅 20:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75571">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
‏ترامب: إذا لم ترسل إيران مقترحا جيدا سنضربها كما لم نفعل من قبل.</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/naya_foriraq/75571" target="_blank">📅 20:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75570">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
‏ترامب: على إيران أن تخاف وأن تحذر مني.</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/naya_foriraq/75570" target="_blank">📅 20:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75569">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
‏ترامب: بالنسبة لإيران، الوقت ينفد، وعليهم التحرك بسرعة، وإلا فلن يبقى منهم شيء. الوقت جوهري!</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/75569" target="_blank">📅 20:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75568">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj1aMs7bqvIMbAYGWTkvzvvIfGPWmxqbS9tCzEpp5Nrfz8kAl0mFkMNUwjtxfxQlgOVFJbImVl27YIB9rEge6Rrgwe4tDV72vrKx6UVO77L6IZ6ekVxlOAulb4yVzk4EoEGhT15IcVkrv43eWGHa-3VHQPSvUuvs9plC1rrXoZKcK1hXS5EopQ98ZvIgexPejs9howOSo7G2GqQER1OLLOTyukA6pwHzGk2BOzwyTP1yvwKKyxTXT8DbOAsuh0pjIq7pucr_2uVP8XrW-mnHV-M6qqYk1ear4zLgOyZeVpVMB-W3RTJCQBky08rtHQuyvlYacsGWVQ4ZnhBTpFxn0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
بالنسبة لإيران، الوقت ينفد، وعليهم التحرك بسرعة، وإلا فلن يبقى منهم شيء. الوقت جوهري!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/75568" target="_blank">📅 20:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75567">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭐️
مكتبُ سماحة السيد السيستاني (دام ظلّه) في النجف الأشرف:
يوم غدٍ الإثنين (18-5-2026) هو الأول من شهر ذي الحجة لعام 1447 للهجرة.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/75567" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75566">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭐️
روسيا:
القوات الأوكرانية قصفت ورشة النقل التابعة لمحطة توليد الطاقة النووية في زابوروجي وشنت هجومًا بطائرة مسيرة على محطة "رادوجا".</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75566" target="_blank">📅 19:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75565">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-05-2026 تجمّع لجنود جيش العدو الإسرائيلي في موقع رأس الناقورة العسكري جنوب لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75565" target="_blank">📅 17:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75564">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزارة دفاع دويلة الامارات: تعرضنا لهجمات بـ3 طائرات مسيّرة دخلت من جهة الحدود الغربية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75564" target="_blank">📅 17:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75563">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75563" target="_blank">📅 17:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75562">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75562" target="_blank">📅 17:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75561">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئيس مجلس النواب الأمريكي: عملية الغضب الملحمي انتهت</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75561" target="_blank">📅 16:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75560">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3348e2fc.mp4?token=dqYwBE84xvVaPSof_z34TNBsYVTpnldFvSE2459Lxe6nchhziyUKbAFeTVhtnxwoALSKK549f_2T6WN9QG7Run-pu5_67ped2r2OXOJt9sPkolZk2mECP9DguNMdiHln9x5pSJCUJqFr-ZCiIScN9-WrWa9dHMg3RuiaS73SL-8_inujHS0ohutzwKOTOmvZtrJSoay4Ygnpu1iquuucTIq5drW9_vwh2cbWbTawxA6ttRDH3-GT1JoU6PezoBh1wTl7U7yOku4wW60HhG2SPpD_YJ7Euj-Xt_mar8S25bkSdxeAzrqsjCZj5-nPlD-JoaKxBuI1oVB8r1NQZz0LJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3348e2fc.mp4?token=dqYwBE84xvVaPSof_z34TNBsYVTpnldFvSE2459Lxe6nchhziyUKbAFeTVhtnxwoALSKK549f_2T6WN9QG7Run-pu5_67ped2r2OXOJt9sPkolZk2mECP9DguNMdiHln9x5pSJCUJqFr-ZCiIScN9-WrWa9dHMg3RuiaS73SL-8_inujHS0ohutzwKOTOmvZtrJSoay4Ygnpu1iquuucTIq5drW9_vwh2cbWbTawxA6ttRDH3-GT1JoU6PezoBh1wTl7U7yOku4wW60HhG2SPpD_YJ7Euj-Xt_mar8S25bkSdxeAzrqsjCZj5-nPlD-JoaKxBuI1oVB8r1NQZz0LJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الطيران الصهيوني يرتكب مجزرة في بلدة طيرفلسيه جنوبي لبنان</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75560" target="_blank">📅 16:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75559">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📰
‏
أكسيوس عن مسؤول امريكي:
كوبا بدأت مناقشة خطط لمهاجمة سفن حربية أميركية وقاعدة غوانتانامو وتسعى للحصول على المسيرات والمعدات العسكرية من روسيا وهي تحاول معرفة شكل المواجهة بين قواتنا وإيران</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75559" target="_blank">📅 16:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75558">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الصدر يبارك للزيدي
المكتب الخاص / النجف الأشرف: أجرى سماحة القائد السيد مقتدى الصدر (أعزه الله) اليوم الأحد السابع عشر من شهر آيار ٢٠٢٦ اتصالاً هاتفياً برئيس مجلس الوزراء السيد علي فالح الزيدي وبارك له تشكيل الحكومة وحثه على الحفاظ على سيادة البلد وتحسين الواقع الخدمي بعد أن رأى منه الهمّة والعزم والإصرار لتحسين الواقع العراقي، كما حثه على الوقوف بحزم لمحاربة الفساد، والحفاظ على مقدرات البلد وتأمين العيش الكريم للشعب العراقي كتقديم الخدمات وتلبية احتياجاته وحفظ حقوقه.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75558" target="_blank">📅 14:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75557">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نيويورك تايمز: دور الولايات المتحدة في الأمن العراقي كان جزءاً من حسابات إسرائيل في قرارها بأنها تستطيع العمل سراً بأمان في العراق.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75557" target="_blank">📅 14:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75556">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نيويورك تايمز: تشير المعلومات إلى أن قاعدة واحدة على الأقل من القواعد التي عثر عليها عواد الشمري كانت معروفة لواشنطن وهذا يعني على الأرجح أن حليف بغداد، الولايات المتحدة، كان على علم بأن هناك قواعد اسرائيلية على الاراضي العراقية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75556" target="_blank">📅 14:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75555">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نيويورك تايمز عن الجيش العراقي: في جلسات خاصة اتصل رئيس أركان القوات المسلحة العراقية الفريق أول عبد الأمير يارالله بنظرائه في الجيش الأمريكي وأكدوا أن القوة ليست قوة أمريكية. لذلك فهمنا أنها إسرائيلية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75555" target="_blank">📅 14:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75554">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نيويورك تايمز عن المتحدث باسم قيادة عمليات كربلاء: الشهيد عواد الشمري اتصل بالسلطات المحلية بعد رصد قوات اجنبية وبعد ذلك بوقت قصير، فقدنا الاتصال به. بعد يومين من البحث عنه تم العثور عليه مقتولا.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75554" target="_blank">📅 14:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75553">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏نيويورك تايمز عن مسؤولين عراقيين: في كل من الحرب القصيرة العام الماضي والصراع الحالي، أجبرت واشنطن العراق على إغلاق راداراته لحماية الطائرات الأمريكية، مما جعل بغداد أكثر اعتمادًا على القوات الأمريكية لاكتشاف النشاط العدائي.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75553" target="_blank">📅 14:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75552">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏
نيويورك تايمز عن مسؤولين عراقيين:
في كل من الحرب القصيرة العام الماضي والصراع الحالي، أجبرت واشنطن العراق على إغلاق راداراته لحماية الطائرات الأمريكية، مما جعل بغداد أكثر اعتمادًا على القوات الأمريكية لاكتشاف النشاط العدائي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75552" target="_blank">📅 14:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75551">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 14-05-2026 منظومة اتصالات لاسلكيّة تابعة لجيش العدو الإسرائيلي في موقع بلاط المُستَحدَث مقابل بلدة رامية جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75551" target="_blank">📅 14:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الاعلام الكردي:
الاتحاد الوطني الكردستاني يوجه رسمياً طلب الى حكومة إقليم كردستان لتطبيق نموذج الإدارتين داخل الاقليم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75550" target="_blank">📅 14:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75549" target="_blank">📅 13:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75548">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">استهداف محطة براكة للطاقة النووية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75548" target="_blank">📅 13:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75547">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75547" target="_blank">📅 13:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75546">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75546" target="_blank">📅 13:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75545">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات تهز الامارات</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75545" target="_blank">📅 13:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75544">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال: هبوط اضطراري لمسيرة شمالي الضفة الغربية إثر خلل تقني</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75544" target="_blank">📅 13:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75543">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaP-2vtDWXjKcpCpfL77gOb5uoxljXaYqqe0tN3kNzwdymd_PWxxKfrnVKgxaOKq1LkKHXiY4dm8A4wtEWlQB_Xcisgisgf-6qf37iUTCSyQAyjdNtGXNytZVB6Kl9j0STNCeTnSGpzW45VbsjIGAkMbmCwr5RNvPLTUhlH-WnBBE2ayLJjltztjj1YYx4bk1Ub9VlrZyWBUbBUi-g3wbH2s99ZovMO08i0IQ9yGhgjneQd1357U6eZ4AmWRSbf3YTtXC_U1PfY8TOf2Ua-L_HEj70yFZRLAL12MgVO3dtN3j9wNAPfOaYvcOjmhkY-ZFTEgr8J_6O4R6qds4o9n0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إسماعيل بقائي:
الكذبة الكبرى التالية التي يتم طرحها لتبرير "حرب الاختيار" غير القانونية هي الادعاء بأنهم "يحافظون على السلام والاستقرار في أسواق الطاقة العالمية".
في الواقع، على الرغم من ذلك، كان إثارة الحرب المتهورة للأنظمة الأمريكية والإسرائيلية هي التي حطمت العمليات الدبلوماسية الواعدة، ومن خلال العدوان العسكري غير المبرر ضد إيران، ضخت عمدا انعدام الأمن في طرق الطاقة الحيوية - عندها فقط لاتهام إيران بزعزعة الاستقرار، من أجل وضع قول غوبلز السيئ السمعة موضع التنفيذ: "اتهام الآخرين بما تفعله أنت بنفسك".
هذا هو كتاب قواعد اللعبة المألوف والساخر: صنع الأزمة والحرب، ثم التصعيد أكثر تحت الراية النبيلة المتمثلة في "استعادة الاستقرار" و "الدفاع عن السلام".
إنهم يخلقون خرابا ويطلقون عليه السلام".
﻿</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75543" target="_blank">📅 13:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75542">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
إعلام إيراني‏: 5 شروط رئيسية في رد واشنطن على مقترح الاتفاق:
🔹
عدم دفع أي تعويضات أو أضرار من جانب الولايات المتحدة
🔹
إخراج وتسليم 400 كيلوغرام من اليورانيوم من إيران إلى الولايات المتحدة
🔹
إبقاء مجموعة واحدة فقط من المنشآت النووية الإيرانية قيد التشغيل
🔹
عدم دفع حتى 25% من الأصول الإيرانية المجمدة
🔹
ربط وقف إطلاق النار في جميع المناطق بالمفاوضات
🔹
يؤكد التقرير أنه حتى في حال استجابة إيران لهذه الشروط، فإن خطر العدوان الأمريكي والصهيوني سيظل قائماً.
🔹
يرى الخبراء أن المقترح الأمريكي، بدلاً من حل المشكلة، يسعى إلى تحقيق أهداف عجزت إيران عن تحقيقها خلال الحرب.
🔹
في المقابل، ربطت إيران أي مفاوضات بتحقيق خمسة شروط مسبقة لبناء الثقة، وهي:
🔹
إنهاء الحرب على جميع الجبهات، وخاصة لبنان
🔹
رفع العقوبات المفروضة على إيران
🔹
الإفراج عن الأموال الإيرانية المجمدة
🔹
التعويض عن الأضرار الناجمة عن الحرب
🔹
الاعتراف بسيادة إيران على مضيق هرمز</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75542" target="_blank">📅 12:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75541">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇱🇻
موقع "إل إس إم" عن بيانات من الجيش اللاتفي: طائرة مسيرة مجهولة دخلت أجوا لاتفيا صباح يوم الأحد.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75541" target="_blank">📅 12:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75540">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية تجمّع آليات وجنود جيش العدو الإسرائيلي في جنوب لبنان بالصواريخ والمسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75540" target="_blank">📅 12:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75539">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
المتحدث باسم القوات المسلحة الإيرانية: إذا تكررت الاعتداءات على إيران فإن ممتلكات الجيش الأميركي ستواجه سيناريوهات جديدة هجومية ومباغتة وعاصفة</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75539" target="_blank">📅 12:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75538">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">💡
مصدر خاص لنايا:
انقطاع الكهرباء في معظم مناطق محافظة أربيل شمال العراق دون معرفة الأسباب.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75538" target="_blank">📅 11:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75537">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">#عاجـــــــــــــــل
🔻
اندلاع اشتباكات مسلحة في قرية دوكان بمحافظة السليمانية شمال العراق ؛ مقتل شخصين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75537" target="_blank">📅 11:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75536">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
🇨🇳
تعيين محمد باقر قاليباف الممثل الخاص لإيران لدى الصين.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75536" target="_blank">📅 11:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75535">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112f5e93b7.mp4?token=SAAXVi0YMHDbDI-iW-m7NupLuAl8dOnu5UMi6SQN8S7rY4yzu9oVCKZsjbMcEa0ljxJNxTSkNej8oEOkR9Ay-kkO3itjNeehkYeZsVqQp7WRmNWYDhEeLgmLWSevrGFRXWGDwIaxaU0bWVoyGO7mN6CBbp1mSB58V-Ii4FLZXDWVYfKKC3Bhbd_PlmsJ3K3cL45QskqddzhUpaW-_0fWB_0yiTqwCcsG1eEBttXw8yXmQ9zktVVFRcsnRc_1xX7OzgrUP9rKjl11YG1VxLvfteTidpEn2XrEjsHC4-qzMQwcQeyEL-dI55qGjzIRgmvfGeDc6SrD9lR9Jq6hNM6V0jYBWMkrYdMB3EhsV8kB9CLTKKGqsTQRaHgOLgFpDTEpzoZ9kDOjVd6I2CX87VlPN-qUpAZb5JsxPtlEWW_Nc-TwvQ3raLZzjQt7tf0OKDwi1lmKzNrVipnVBmml8wf93gI4npVPqPh616acwkijf_AtOfBeGqILoCEcv9qPgmVH80Oo8PIubzKi2nNZZEljFjoQq2qymXb9iyTbpK4nnMbhuXWuWTKLs8wM9bYRp2UGTi6e5WjlOht3oaUBiw09YO15KVd1cpdAlIVxsvl7UDpzmyWuXU-8NuBFLvkDBVl5DQSLnyG9ECn6iSHdSl9jqPmjEb61wEkgfjlVTpTZIog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112f5e93b7.mp4?token=SAAXVi0YMHDbDI-iW-m7NupLuAl8dOnu5UMi6SQN8S7rY4yzu9oVCKZsjbMcEa0ljxJNxTSkNej8oEOkR9Ay-kkO3itjNeehkYeZsVqQp7WRmNWYDhEeLgmLWSevrGFRXWGDwIaxaU0bWVoyGO7mN6CBbp1mSB58V-Ii4FLZXDWVYfKKC3Bhbd_PlmsJ3K3cL45QskqddzhUpaW-_0fWB_0yiTqwCcsG1eEBttXw8yXmQ9zktVVFRcsnRc_1xX7OzgrUP9rKjl11YG1VxLvfteTidpEn2XrEjsHC4-qzMQwcQeyEL-dI55qGjzIRgmvfGeDc6SrD9lR9Jq6hNM6V0jYBWMkrYdMB3EhsV8kB9CLTKKGqsTQRaHgOLgFpDTEpzoZ9kDOjVd6I2CX87VlPN-qUpAZb5JsxPtlEWW_Nc-TwvQ3raLZzjQt7tf0OKDwi1lmKzNrVipnVBmml8wf93gI4npVPqPh616acwkijf_AtOfBeGqILoCEcv9qPgmVH80Oo8PIubzKi2nNZZEljFjoQq2qymXb9iyTbpK4nnMbhuXWuWTKLs8wM9bYRp2UGTi6e5WjlOht3oaUBiw09YO15KVd1cpdAlIVxsvl7UDpzmyWuXU-8NuBFLvkDBVl5DQSLnyG9ECn6iSHdSl9jqPmjEb61wEkgfjlVTpTZIog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
توغل إسرائيلي مؤلف من ثلاث دبابات وآلية مزودة برشاش دوشكا في محافظة درعا جنوب سوريا وإطلاق نار على المارة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75535" target="_blank">📅 10:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75534">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq7f_W1NLgWNLaQbm3VezlT8gUK_G5-uI0mp-XnN3Dp9XzMCBaWDdmyzqdQlqtyjPw4TiXeItd5ubhlG9MmWnGzuiPcyvIhLV0y_aX0Flywc8swAXxwP2vWU67HuZPgcB8-hdYVd0jEB84nP9n4PlQOz-yIlCtFkSfnpAcqKwkBhHOiiEQxjlqPG1Gjp-fdxQdzG9Bbuvk3RKCqRq-Bgy-S3KKxiQWmx4HcKyMsyhK9-xT4CeH0ttGtpi3T_LExca1ZdRj3Iakjg325Btcoq0xLqQ1fhAurCReweKihAHzeHjbHCnrZvTQ1VRlIuhYjEngnW3cmAIQOeWdfdMEcfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
⚔️
الشرق الأوسط السعودية عن كتائب حزب الله في العراق
تعمل في بيئة سرية شديدة الصرامة لهذا فإن الغموض وقلة المعلومات تحيطان بمعظم الشخصيات القيادية داخل هذه الجماعة ، بالنظر لامتناعهم عن الظهور العام رغم النفوذ الذي تتمتع به محلياً بوصفها من أكثر الفصائل قرباً وارتباطاً بالحرس الثوري.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75534" target="_blank">📅 10:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75533">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هيئة البث الصهيونية: نشر شبكة حماية جنوب لبنان لتقليص خطر إطلاق المسيرات غير كاف</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75533" target="_blank">📅 09:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75532">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JioAgAAx0S71Vh6gE2VjrgH6vnONH_LA_WuaRLsuMuenm5wxPzEFYtMEXdmN4L_P-yFomQSrHPE0ZiKc3q8nUT3LIULTXIZhbVQDiqYeLuotxWTf2bZ56O3e2oFXrmS2wgVY5uvvECfAuPVxX3cYhHrtts7j0RC1Ukha1dgIzgFUuDMpBIewFNwk61pPY7bG3sF0_c81JPKP8pKLs5S97E4iN2jGZI1g30n3gFdApHNpj546kZj3HJaHJE979BAeERlEnU5Zl43FvE-dHOZWpbISezSVxBjcV-5JAfvcSNCzc5D1SAaawTqZCBIGBaAOl2JJZ2DSIAsV_FD2u-h78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇮🇶
قادمة من تل ابيب
نشاط لطيران وقود أمريكي في اجواء محافظة الأنبار غربي العراق انطلقت من مطار بن غورين باتجاه الأراضي العراقية ؛ تواجد هكذا نوع من الطيران يشير إلى وجود طيران حربي وتجسسي في سماء العراق بحاجة إلى عمليات لوجستية …</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75532" target="_blank">📅 08:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75531">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W68__cUahAMxIo-nrXijIqtroRA0Z1VXwcxH53F5OiKts7ECt4j-9zqPvB0VkUfzORAalECQI9MhOmioPWPC8qworlboNv1UI3EQlEQ-aSh6y64A83lFZDuPWd4jZCWnOnf3TV_laDZzm4lYImC3Vmofwqgu1E6i0wqlfEx4EHNiTU7UHHG-B6lh49R_quaYbLva3m16oD6hpu65SazgeJiyNjLPMud5aDKUO8GKMrpZYrsoFEYK8Sx3n_vCfAPG5Dfc1n2yT-CyeqV_DnR70oAsOs72sgSrvffr-5-yt7okFIwt97Kzc-_1mSDjHhXOq1n41y5NbSiHCfWJhPQzIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اسعار النفط تقفز الى اكثر من 109 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/75531" target="_blank">📅 04:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75530">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوي انفجارات في ريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/75530" target="_blank">📅 00:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75529">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوي انفجارات في ريف العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/75529" target="_blank">📅 00:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75528">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz7kbzw72bIQxsAGwTv9GG2yqgVxi2vsBDhWsagO2bJvEeN6COINA0CZBJigfRt5I7TWqLwkgcf8Z22ip_tE89lUEx_u5OUtm6h1htKc3z9LzTc8N7HLn5fKVsaHskHanhwZ_YVX5AOWqU2B0ooqbfMeGO8ef1ZPjCId7ao3-9vULpFFD99fQMV8fsyM5CiSqeK_qNWq3QbVpYtFhiJw5R0IpVgbMfOjnZIqWA3GmFYvMkC-z6uM3BaJIhSE-9CfYD1i0zFLkGlIyvcvQRMGWim017SNQ3GeVrgvLBv5QrFsFOV41O7zOCp0fNwYj_YsT93GxMm-nz3fO-85Fx8HUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبه لهم يا حسين
ما طحت انت من ميمونك
السلام على سلاح المقاومة العراقية البطلة ..</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/75528" target="_blank">📅 00:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75527">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d1203d03.mp4?token=U-NQWJ2HHtHjjjxpjVDSg3XB0cr-K4thlxYEXJ-QWTFcbw2T8tiI-LG7Cw4I2lIau5PBw85DW29PLZSXuvzZGpxEo5S8M-40uTMfBtUxGHNmWPzEZB48JxGkyuQ6lO7lhoMp9MqioZ4BpqzEBnNm_5uLrkBUuZGoji81rx-xsSiNJN8_Zg5y-4MnVmq26UJxhwNN0jAYtEejXrRNkk85nP-hzaNKvT_sYo3fLevc0wSCl6u4ft84suuUdKbjG2llLNC8O_xgxtUoRwvurIMDbmFNShPBHmBXHbYiBIIE-udNl_14KGPb0B21olQn5X9DqmqhvycjItLR9COgQRaSDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d1203d03.mp4?token=U-NQWJ2HHtHjjjxpjVDSg3XB0cr-K4thlxYEXJ-QWTFcbw2T8tiI-LG7Cw4I2lIau5PBw85DW29PLZSXuvzZGpxEo5S8M-40uTMfBtUxGHNmWPzEZB48JxGkyuQ6lO7lhoMp9MqioZ4BpqzEBnNm_5uLrkBUuZGoji81rx-xsSiNJN8_Zg5y-4MnVmq26UJxhwNN0jAYtEejXrRNkk85nP-hzaNKvT_sYo3fLevc0wSCl6u4ft84suuUdKbjG2llLNC8O_xgxtUoRwvurIMDbmFNShPBHmBXHbYiBIIE-udNl_14KGPb0B21olQn5X9DqmqhvycjItLR9COgQRaSDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: انفجار في مصنع شركة تومر. تقوم الشركة بتطوير وتصنيع محركات الصواريخ الثقيلة والخفيفة، بما في ذلك محركات الدفع لصواريخ آرو 2 وآرو 3، ومحرك صاروخ سيلفر أنكور المستهدف، ومحركات أقمار هورايزون الصناعية، ومحركات صواريخ باراك 8 وباراك إم إكس.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/75527" target="_blank">📅 00:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75526">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: يتم توجيه المراسلين للقول إنه منشأة مدنية - هكذا يحاولون إسكات الجمهور، أمر جنوني.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/75526" target="_blank">📅 00:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">النيران لازالت تسعر في موقع حساس بمدينة بيت شيمش عقب إنفجار ضخم جداً.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/75525" target="_blank">📅 23:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75524">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن استهداف وإحراق دبابة ميركافا تابعة لجيش الإحتلال في بلدة البياضة بجنوب لبنان.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75524" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE4Cjt5oH_ld3b-xTYvVtG3PPAjpqkzqoTLIfStwPveYCXyoKEq6-Xa8V1eKQZpH9r6AkuUhu8sZ6UUMfwM97bgq1r0JqG4BtNzmKkEGjEFAVn89eJvWaFHbV3qxM7crHYpMkdlt_Q5iBKnV-8tKxHfWYOLLm76DmUynMTL1XUws3S-JSnzMCnvbu8Rk1VAwLQf3_i2Mv752SWXvlxVVLiBKXcOKmfG5wGR4AkSS-r9aoMt6gvg6KjaMgx_Zjjl5TjE5UMl1EFIrgcsVi27I27JodWlObGKAd-cUhWZUfe3kdgFcf8ue70TZd8QA-yIYMNMAHDkkwc0tXHh85s1JKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: كان الهدوء الذي يسبق العاصفة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75523" target="_blank">📅 23:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75522">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9722a2e8a3.mp4?token=vSKgXDP8q5ROCI68k7BCiLhKckHznsqLSdI1Q4QEVU_gBxXpL1HGjaopf0EY6mH3PYTxmSbmOxw_AOrK6L1oNwUsv-XuyNqt-BBYGVF1z5DPFGoUBJ9JGifGP3qJyZKvYR3Ew51VIfgk3ZpxJBUnj5L9yh6SUD4mc4MFigU-pHfHAvGDpp2uLdzDppiMJKxpwpTxFN27pXNTUdCYOKTXhqSLwcdZDw8ls8t51FFyZdMXIT0UogUhr6gls63dIGfevXdz3KXdZd6eDQAuJz4sFhmrdr8OG_MKQTXuL5CPZ0w1zUEZfN1H_n63Q8kf1WaOVe9fAiW_QIvgjrBSh_BOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9722a2e8a3.mp4?token=vSKgXDP8q5ROCI68k7BCiLhKckHznsqLSdI1Q4QEVU_gBxXpL1HGjaopf0EY6mH3PYTxmSbmOxw_AOrK6L1oNwUsv-XuyNqt-BBYGVF1z5DPFGoUBJ9JGifGP3qJyZKvYR3Ew51VIfgk3ZpxJBUnj5L9yh6SUD4mc4MFigU-pHfHAvGDpp2uLdzDppiMJKxpwpTxFN27pXNTUdCYOKTXhqSLwcdZDw8ls8t51FFyZdMXIT0UogUhr6gls63dIGfevXdz3KXdZd6eDQAuJz4sFhmrdr8OG_MKQTXuL5CPZ0w1zUEZfN1H_n63Q8kf1WaOVe9fAiW_QIvgjrBSh_BOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إعلام العدو: في حالات الانفجارات المسيطر عليها يتم الإبلاغ للجمهور مسبقًا، وحتى عندما يحدث انفجار مسيطر عليه لا ينتج عنه انفجار بهذا الحجم وفطر واسع - مثير للاهتمام!!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75522" target="_blank">📅 23:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">من الإنفجار الضخم الذي أشعل سماء غرب القدس المحتلة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75521" target="_blank">📅 23:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoaoTCpxqq4l3hBDZqabb_6DvLhbUqdkMyG2_hjNrGvXexuywXDI7dJLIn7eZe6QdZNj-Zh3bas1XXpProw4lmc8kXk7isK00uz9VAa71vaEyn8kXeT7JoguBmShx0R7peJ08uB2WzotH3WRor_jkz-DkoucibGjpkZamFtt13WMfMI7KFT3N4pDzmzNZwsO5LX3lU1DmDMVGGsCWOMi5aoJTDKDaUU3P6eeGDtoQm8lbNqOEl5bO8lhI7_dIbYDkkePsOJZOFPRuTG1Pb96OgSuC4jFs4GHP_ftdkwgtf7DsU1Bh7zV4e2h1TSL-OX6loHpAWG3x0LVT47-0du7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو: الإنفجار قد يكون في منشأة حساسة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75520" target="_blank">📅 23:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">إعلام العدو: الجيش يمنع عجلات الإسعاف إلى الإقتراب من مكان الحادث.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75519" target="_blank">📅 23:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">إعلام العدو: انفجار كبير جدا في مدينة بيت شيمش غربي القدس المحتلة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75518" target="_blank">📅 23:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b382f11f53.mp4?token=L8hLFGQLp79iQTKRGm42tkE0t6byMzLZ4GoiAoF5bGTpoieEP2r3lY020_e6gR6KUrfh8IaYhua-mmUpPEnAOIldXiBDi0On26bZJZRtfrEkCFQloiE9PGn026Tf4aUBodahOjhNXRUs82nxSZhDcQl1FvaOQybv27J6oEnwxbZJOl0doN1OiAlW2OnBTBQ5W1m0FX_HQh789XtQrHHpuVsFIW_ase4vmijXA-JjEO1mjWjNb9_euhl2naKGX998zLR5m5ZRKSri7lbDBbEAlqnODjqEvO8cFZy-qTzeUOvfegHZw5t0S5MbbFD-ffFp3a2UI1QP3x9YLtTIXx5V4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b382f11f53.mp4?token=L8hLFGQLp79iQTKRGm42tkE0t6byMzLZ4GoiAoF5bGTpoieEP2r3lY020_e6gR6KUrfh8IaYhua-mmUpPEnAOIldXiBDi0On26bZJZRtfrEkCFQloiE9PGn026Tf4aUBodahOjhNXRUs82nxSZhDcQl1FvaOQybv27J6oEnwxbZJOl0doN1OiAlW2OnBTBQ5W1m0FX_HQh789XtQrHHpuVsFIW_ase4vmijXA-JjEO1mjWjNb9_euhl2naKGX998zLR5m5ZRKSri7lbDBbEAlqnODjqEvO8cFZy-qTzeUOvfegHZw5t0S5MbbFD-ffFp3a2UI1QP3x9YLtTIXx5V4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إعلام العدو: انفجار كبير في بيت شيمش في القدس المحتلة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75517" target="_blank">📅 23:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189597cd2d.mp4?token=NVRyVmMGkolzCTY-qujy__wimlFpUunYrKMMFPQtKZ5ab5rbeWXLcVcmR2GdyYzLNic-X6COFKmEImEkjZncgnPOQD-jA4Ws-GLKSyxouWFJikXNgYlPxUtVsM9FfJbjKpJIdnxKVE8qYXgo2IFNv0z_clwwoci_k62nz69-z-dyyvZ6nSCM_kS689XlY2BTxV2oOEozoVyxmD-ehRaJkzJssnhHathtGGjlRLuocK82k9tJ2E5QCfamEpyH8cwed1278sBjpTR1MTaaMyFwsdomonZ5PeOnbRdGlEnc5-sOAODIkkMwFbhfsmCct9yQOYm46sbPG2AnE9cuf2Qebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189597cd2d.mp4?token=NVRyVmMGkolzCTY-qujy__wimlFpUunYrKMMFPQtKZ5ab5rbeWXLcVcmR2GdyYzLNic-X6COFKmEImEkjZncgnPOQD-jA4Ws-GLKSyxouWFJikXNgYlPxUtVsM9FfJbjKpJIdnxKVE8qYXgo2IFNv0z_clwwoci_k62nz69-z-dyyvZ6nSCM_kS689XlY2BTxV2oOEozoVyxmD-ehRaJkzJssnhHathtGGjlRLuocK82k9tJ2E5QCfamEpyH8cwed1278sBjpTR1MTaaMyFwsdomonZ5PeOnbRdGlEnc5-sOAODIkkMwFbhfsmCct9yQOYm46sbPG2AnE9cuf2Qebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إعلام العدو: انفجار كبير في بيت شيمش في القدس المحتلة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75516" target="_blank">📅 23:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqND6CJ_TifYpFdLrsU1T6C6jwaucX8c7i-gY9SBTu0jfLSGwsKFUWGDC0bME_JbcVoaidSv8XHnGnDGJZylryBM-NOPy8m9ik3I06XDc34mNuZWMVUDLyLxbyY3bPEQEgn0RxRZMGkfKmI3Yioch8H8huwQBEteM3V_IlNNxzXzZbIxPyCCIpFGCM6R5tChemd9UV3vYJ10Mw1G9crgsRBaZyulZ3cqz7NMdfs8jZr1yT9L9DFWBGVFJd8kw4u75Le4ZOJMm7bqPfFnt__6FUo25gXKgpRm-jP_1ls2lS2gHy8FngYwBuTtL5-R3tJlt7t0gqKtwbclRWEWHdc9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
العالم يقف على عتبة نظام جديد.
كما قال الرئيس شي "التحول غير المرئي في قرن من الزمن يتسارع في جميع أنحاء العالم"، وأشدد على أن مقاومة الأمة الإيرانية لمدة 70 يومًا قد سرعت هذا التحول.
المستقبل ملك للجنوب العالمي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75515" target="_blank">📅 22:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB2YQdxctp1fmVurVdZulYZUkmUHCOl7TGUofJIbBlJBoy_UHf-tFv5GMpNvRbXxy-k0gaF7Bnb3QyXHnGOy4gO1Ic-8dzaj6seEiVuDUC1Oe0Sc8Nc4uIMSFxNnOnNOPvj5KznoPMqDVQJAlS2dJE8Q8jVEiDphuJ06lmvLE2eSObA3mBmMmidTWVSNDi4hZYMXZM6UEbmhRyHAu9CeEg3mmWqSmIMqDSZwmOTDKfjv2wEpiO_NY6OD4KFz6BTsnHyGtaNcdw4G4eQKvwZeKBbECkJ9u2vArJz7x1crn03KKHdWCDQh5t_-NcQ5PSFYj1rw-ZX4pS096Z5w09kHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: مقتل جندي وإصابة آخرين في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75514" target="_blank">📅 21:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322470de2f.mp4?token=oU0CV2gu38toy0HSNhXoU-R3iVWDFYvkqiOAN2slzs65azVYamp5GRkx2xImN6ni0pPQYZyM7i1oyRanDW6D6pcUlBGfCqhXMjmvQ024nUgmoehUU8DcuWa72vlXzO2DnDUUnDu5wwpaXBJSuGCZw6SXtNjABpIEp-HVkv4NBEGiyruLtf7Al5J9G9jIfD-57lMV7MVmcVURAgwROlwJuKYqB3_O7Gu9NtIvniQZJ07a7pXg4xnb4mKDvsJiUdiIOXGof-UBamZeQsL42ODb470DWeUAjW8F6XOtJdLXt8_AtKzTcqmVVRGdt7tpPTc0Z0XDVRYuJjAk9VGF8TRmdLeUcytw3puLVr6u3zS6rq7IFDn6ZrYa26j5wAWIbAevDQ3l4rpC5ZETweDFl16FTojsriDaBkrGiutES6BGYUJyTAC-SOszRjiUap8uk4qCcwApnxWlAJDWKMFUwlPr2extzARXU9Xp6pusQ8LaltnK4oD9kGUb3Wkt2rJOXt6IOsx5Bx4lYQrwd26VScPqn26AgSI6Dt2U0bfAhAi4-sm2KI7HLBpPcSnpyd54jkbHjVJJJBMv63P22BQ0WWYGVKQjx0-IL0HU_3LCNN-AZCk7rHoMAJKug_Ksln5fEZUWsmcyYpg46ZsExMokjzI8bC5fZ2BhZvQwTAtljiIQTC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322470de2f.mp4?token=oU0CV2gu38toy0HSNhXoU-R3iVWDFYvkqiOAN2slzs65azVYamp5GRkx2xImN6ni0pPQYZyM7i1oyRanDW6D6pcUlBGfCqhXMjmvQ024nUgmoehUU8DcuWa72vlXzO2DnDUUnDu5wwpaXBJSuGCZw6SXtNjABpIEp-HVkv4NBEGiyruLtf7Al5J9G9jIfD-57lMV7MVmcVURAgwROlwJuKYqB3_O7Gu9NtIvniQZJ07a7pXg4xnb4mKDvsJiUdiIOXGof-UBamZeQsL42ODb470DWeUAjW8F6XOtJdLXt8_AtKzTcqmVVRGdt7tpPTc0Z0XDVRYuJjAk9VGF8TRmdLeUcytw3puLVr6u3zS6rq7IFDn6ZrYa26j5wAWIbAevDQ3l4rpC5ZETweDFl16FTojsriDaBkrGiutES6BGYUJyTAC-SOszRjiUap8uk4qCcwApnxWlAJDWKMFUwlPr2extzARXU9Xp6pusQ8LaltnK4oD9kGUb3Wkt2rJOXt6IOsx5Bx4lYQrwd26VScPqn26AgSI6Dt2U0bfAhAi4-sm2KI7HLBpPcSnpyd54jkbHjVJJJBMv63P22BQ0WWYGVKQjx0-IL0HU_3LCNN-AZCk7rHoMAJKug_Ksln5fEZUWsmcyYpg46ZsExMokjzI8bC5fZ2BhZvQwTAtljiIQTC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
آلية "هامفي" تابعة لجيش العدو الإسرائيلي على طريق الناقورة - الإسكندرون جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75513" target="_blank">📅 21:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⭐️
هجوم بطائرة مسيرة إنتحارية على مواقع المعارضة الكردية الإيرانية في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75512" target="_blank">📅 21:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
ترامب:
إيران ستمر بوقت عصيب للغاية إذا لم يتم التوصل إلى اتفاق.
لا أعلم ما إذا كان سيتم قريبا التوصل إلى اتفاق ومن الأفضل لإيران أن تبرم اتفاقا.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75511" target="_blank">📅 21:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6xkXIjqXQQ8wtwlKk4ZGTmpgMV9HxjBiuFW2eeN8y4NpC-I4al7DMbd0_M2STfSgwyptZLwk92yzcF7tf3K2GXp_sbB71_n_o-mbHyfqCnQVX85_qJKOM6XBEBCZiZtxxzMKlKUtv4E7K9AxuIwpmuKJqKK6ziX_GaYiRDo_xVLBsJgI8ljLkDUimWEKB4SsAEOJU7GC_twHP9MSbKZIueRk1aiKuX7pRRxNn1cM2fVAD0-b6mT0Kn_bBYLNfm_rcaF8g4W7OS-imfqG8Ro_s47SyL3oUeapZcjeGv2ptd_BR7D4AfrBWUVRO-RcvUkrQQ4F3vDRvb6dq_J8yAUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشاب العراقي المختطف محمد السعدي بعد وصوله إلى امريكا من قبل الـFBI مخاطب والدته عن طريق محاميه الخاص</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75510" target="_blank">📅 21:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be80b3e22.mp4?token=GrN5zQ2csVQ9ac4Ueicj3aqd4_3SUkgL7vVeKKzPt5aYGmkUTXoJ-SWfdiO0TyodXVsVZYPaJgyBSuMT4NRaaN-r04ViVn17Eg-p926C_CaKoclzPdBKWcjENIASRkfdPKKX-bFpRF9GBVBTaitVFtyI50J6srOge5NOhjFDJkQp-HhMqkoinbC0yMPUhWlnnDon8jV70LRSQ_WnmRqrmcWUWZbX4pPsfAzOTuWT5ygWG9W3fePVAuUiWyMr_67PAsOJFVBDZcNBiKUHBaz77kuexj9qR-GHROo0KOdx-HSpX2ECldXiY0VuwfKasD-c7bYL4uKPhc8at5SAZgOM0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be80b3e22.mp4?token=GrN5zQ2csVQ9ac4Ueicj3aqd4_3SUkgL7vVeKKzPt5aYGmkUTXoJ-SWfdiO0TyodXVsVZYPaJgyBSuMT4NRaaN-r04ViVn17Eg-p926C_CaKoclzPdBKWcjENIASRkfdPKKX-bFpRF9GBVBTaitVFtyI50J6srOge5NOhjFDJkQp-HhMqkoinbC0yMPUhWlnnDon8jV70LRSQ_WnmRqrmcWUWZbX4pPsfAzOTuWT5ygWG9W3fePVAuUiWyMr_67PAsOJFVBDZcNBiKUHBaz77kuexj9qR-GHROo0KOdx-HSpX2ECldXiY0VuwfKasD-c7bYL4uKPhc8at5SAZgOM0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
نائب رئيس الجمهورية الإيراني:
لن نسمح بعد الآن بمرور معدات العدو العسكرية عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75509" target="_blank">📅 20:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
مقتل جندي وإصابة آخرين في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75508" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lluj-WeRZCvRb68D4XzAS-w6YPWXa0tu-ClXrNBKY7cCFThEM1p2KtnU-aEWT3S6Tx74Pac2XMBZtn4Fo7FIeDy6ZpzMdKlu7PsiZJIEqKMeOsmWhEtxbTI0m4SFdKxuvv7hM1UrQ1ZpGZ22eQrmVvgpxXY8fGcZSHhNlBN9y4GyP1miLegrFyvW7yArfwy5pqCb5admJQ5_n_xX_HJTZS_PZdr3jBgvqvei-fwusptXZAYRXfxEoTEfMaQDFibjFSLsnIsUKlKK8SdoD2kFdhyoR6DflNH3BaF8oEbwPWsfK0jDQ_D8YHcaoOr9YH65uG63uprRwYbnTvaQNXYc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
"بركة المياه العاكسة بين نصب لنكولن التذكاري ونصب واشنطن التذكاري، التي يبلغ ارتفاعها حوالي 2030 قدمًا، مقارنةً بأطول المباني في الولايات المتحدة الأمريكية، أنفق أوباما وبايدن أكثر من 100 مليون دولار في محاولة لإصلاحها. بلغت التكلفة التقديرية لـ"إصلاحهم" 355 مليون دولار. أنا أعمل الآن في مجال الإنشاءات، وقد قررتُ الانتقال إلى مستوى أعلى بكثير من الإصلاح، باستخدام مواد صناعية فائقة المتانة، مما سيمنحها عمرًا أطول ومظهرًا أفضل! سيكون السعر جزءًا صغيرًا من الأموال التي أنفقوها، دون جدوى، لإصلاحها. في الواقع، لقد زادوا الأمر سوءًا! الهدف هو إنجازها، بهذا المستوى الأعلى، قبل الرابع من يوليو - نحن متقدمون على الجدول الزمني!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/75507" target="_blank">📅 20:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b924f8da87.mp4?token=UEKAQzScTCVgB4KgXClDPc0TZhbx_mnf0dEP-FWkuoYjQADcAgz0ul2Xdop48YsEQF_Ke8cLG-UCxj3YrXnUwFQ-KhBggiBmIulGXLXRpzG2BJy8U3rcsIs-RlhGlit6DfNkhqL8eg55UojqueTnuI-JaSQpdApIMLlrrvvELpjFBxTFs6-ul9NaR4tRQhF6G2fQ95Gjj24zo59GwHujOIIMd3Y_e_ivLr5wFUZRzLZL9QwxZKdODKhC5OHDDeBKtv2gtMs6Ew6utdjnC5jaWB0uS1Q_0X-_naS2w5GuKK58ZQeqipYFWX6tl4rgAUlqyr04LlriO-P29vbccBDQMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b924f8da87.mp4?token=UEKAQzScTCVgB4KgXClDPc0TZhbx_mnf0dEP-FWkuoYjQADcAgz0ul2Xdop48YsEQF_Ke8cLG-UCxj3YrXnUwFQ-KhBggiBmIulGXLXRpzG2BJy8U3rcsIs-RlhGlit6DfNkhqL8eg55UojqueTnuI-JaSQpdApIMLlrrvvELpjFBxTFs6-ul9NaR4tRQhF6G2fQ95Gjj24zo59GwHujOIIMd3Y_e_ivLr5wFUZRzLZL9QwxZKdODKhC5OHDDeBKtv2gtMs6Ew6utdjnC5jaWB0uS1Q_0X-_naS2w5GuKK58ZQeqipYFWX6tl4rgAUlqyr04LlriO-P29vbccBDQMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
هجوم مركب..
إطلاق رشقات صاروخية وطيران مسير من لبنان نحو مستوطنات الشمال الفلسطيني المحتل ودفاعات الكيان الصهيوني تحاول الإعتراض.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75506" target="_blank">📅 20:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef9228732.mp4?token=jjJWAO2ThoaODRnf4hTuJ_LT8PFWKMqeHwtLnXwZ-4z_Gx3W_VipQHiXGmHEAWHCRsDyBQygnlro4rrwOJdlbIKbL4KRc8kKoSnmOU9RvasQzuuVp-c1WleD8zeLXkwxB_64FLMzianHauR-jvmzOtUnsJ1cPki5z2xhOKUWsx49FekkJe1pgS5hHXJhBXsg3Qsm0XKmxKQMPculMXH3lRe1o6bvf7CDsBe24RY_p6l6qBcoCezmxAxL-viC7IBq3WhbKXVQDX8e_w1p_vCfn9_HkAJZ0Yor49lbQ3APs2C9zakiO6xZ-ljpSR7M_Gi68Kn_Xwj41tUhfnxTA2R415DLbf_if3G_FzrkpeY08lju5mWwP6KjeFOr5f1XDW6bdo3pFhq-5SBY35LhEq9D6L9S_VBotd1fnEAmxSDv6aUglaStyADcqOZvzkDGqhe-BPcYlVyeeQvaSrBWfXOhJrQmhCpHQudkahMXNX_H7UZAn6kBk9RQ71OwuA6LImncyyZtjJVvInL8B9pn7-GtRliwKfnTtEtNm7JUk1XVQ5a4_DtV6Go8MiE1AZjxJ7hKIk6U-IlfDsVqrRE5CvNz92QREYlaB64mT0cIdmbEljept_JoCT3Iudub_hzaCF7aQuOr5_ixeh3hLfBxNd3eOVdvDg5guxOYtcHx_azS8ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef9228732.mp4?token=jjJWAO2ThoaODRnf4hTuJ_LT8PFWKMqeHwtLnXwZ-4z_Gx3W_VipQHiXGmHEAWHCRsDyBQygnlro4rrwOJdlbIKbL4KRc8kKoSnmOU9RvasQzuuVp-c1WleD8zeLXkwxB_64FLMzianHauR-jvmzOtUnsJ1cPki5z2xhOKUWsx49FekkJe1pgS5hHXJhBXsg3Qsm0XKmxKQMPculMXH3lRe1o6bvf7CDsBe24RY_p6l6qBcoCezmxAxL-viC7IBq3WhbKXVQDX8e_w1p_vCfn9_HkAJZ0Yor49lbQ3APs2C9zakiO6xZ-ljpSR7M_Gi68Kn_Xwj41tUhfnxTA2R415DLbf_if3G_FzrkpeY08lju5mWwP6KjeFOr5f1XDW6bdo3pFhq-5SBY35LhEq9D6L9S_VBotd1fnEAmxSDv6aUglaStyADcqOZvzkDGqhe-BPcYlVyeeQvaSrBWfXOhJrQmhCpHQudkahMXNX_H7UZAn6kBk9RQ71OwuA6LImncyyZtjJVvInL8B9pn7-GtRliwKfnTtEtNm7JUk1XVQ5a4_DtV6Go8MiE1AZjxJ7hKIk6U-IlfDsVqrRE5CvNz92QREYlaB64mT0cIdmbEljept_JoCT3Iudub_hzaCF7aQuOr5_ixeh3hLfBxNd3eOVdvDg5guxOYtcHx_azS8ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 13-05-2026 ناقلة جند مدرّعة تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75505" target="_blank">📅 20:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترفيهي
⭐️
صنداي تلغراف:
يحث مساعدو ترامب دولة الإمارات العربية المتحدة على تعميق دورها في حرب إيران - بما في ذلك الاستيلاء على جزيرة لافان الإيرانية الاستراتيجية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75504" target="_blank">📅 19:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba6d0a562.mp4?token=U4HwZywMFxYrU-9lC5q11xLMXsy5CHXxkjlO3uVTiuYevLZbxTFwU_oEGNfOLSlLcFWVlvOJkCatq_CY3iqJjpkL2QnHC3z-gbL1UhRLu-gLKhf3i4mYyTaXeNd0zJ8p3i65fz0Op561Hp0R5o9-8vuSXttenwLyjYXwOg9Lkm5ZEiC16uc367c4DGa8BZaj5PKCUUsjxj64fBHWHXpQRk8r554xxUZbbo3K0cINDpFaULbeC1-hN_svMg1qICmDqRh5lNSLT4hFdr5gNqDz4rLJBdfNYYigBtZtWhB9sQPExSUTJ7eS9lQtVjwVHAOZ5Zu7Zi4EEm2WY_oqhKGWVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba6d0a562.mp4?token=U4HwZywMFxYrU-9lC5q11xLMXsy5CHXxkjlO3uVTiuYevLZbxTFwU_oEGNfOLSlLcFWVlvOJkCatq_CY3iqJjpkL2QnHC3z-gbL1UhRLu-gLKhf3i4mYyTaXeNd0zJ8p3i65fz0Op561Hp0R5o9-8vuSXttenwLyjYXwOg9Lkm5ZEiC16uc367c4DGa8BZaj5PKCUUsjxj64fBHWHXpQRk8r554xxUZbbo3K0cINDpFaULbeC1-hN_svMg1qICmDqRh5lNSLT4hFdr5gNqDz4rLJBdfNYYigBtZtWhB9sQPExSUTJ7eS9lQtVjwVHAOZ5Zu7Zi4EEm2WY_oqhKGWVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
توثيق يظهر تساقط الصواريخ التي أطلقها حزب الله على مواقع العدو الصهيوني في بلدة البياضة بجنوب لبنان واعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75503" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌟
🏴‍☠️
إطلاق رشقة صاروخية كبيرة من لبنان نحو مستوطنة راس الناقورة ومحيطها بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75502" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0mA96-Rz-Lu8sTwxjnA_rNIh5DXO3fhnvlNQH0VjSquoIKQRlRgSz4Y8eZpzis2oTp6Il0ZQO62_0LovXc8PEV_zldGwCIojF400mGQfxDF5gNFw_qtAiclVq48LsEGiRXliVthpu_lNE7h6s1Lav7DMoMcPorL0gXzBBJRy8NNJLn1kMLA5HDbuX2hs6unl5btHEOixNMGmCYY8_XKBn9OQwCNJHwpXZ2Fp6pfpAWtk9Wrxtfa133BCv3WeL5tJbKDmBOEB1p4fO3lRJEL-wNFSRZeFfZHtWrMPbeWeiCNQOgXrPCCN3aNMayC4qpkdyEmKgjv8V9s8ucuMI-QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب يعلق على الضربات العسكرية الأمريكية في نيجيريا: "لا مجال للمزاح!!! ترقبوا ما سيحدث لاحقاً بشأن موضوعكم المفضل!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75501" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📰
بلومبرغ:
‏ناقلة نفط من طراز سويزماكس يُعتقد أنها تحمل نفطاً خاماً عراقياً تقترب من الهند بعد أن عبرت على ما يبدو مضيق هرمز في الأيام الأخيرة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75500" target="_blank">📅 18:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75499">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 09-05-2026 جرّافة تابعة لجيش العدو الإسرائيلي عند خلّة الراج في بلدة دير سريان جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75499" target="_blank">📅 18:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs1i7NLxrCEl939b71dFz_lSO8nsna-c7WGsf9Cyv9_HijDWV9AiuWMjymmsSRMco2KRrLYODtoQXYOYqMb2r5ydSe3miDoIMEhT-CiX3Q99LhRXts4iaOWCG9rrrmW3AlSm8Rhg3kaZNV45a4rLsfhzcPOeQjIft6PTchBP1346Z_b04HY113VfCZNFlwl9iHcezq_w5nqZc4P_MquAQLcV25navSItJ2a07bqKHIzRV-IQWXoXixpnHIevAouLY-R4IKSMCru29IB8ZNLCNnYA43OVmw4cnnQukDBnC1At8-vd4S_cT00tEJq8digpqY5wnkH2U712JQAGvuV8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سكرتير القائد العام للقوات المسلحة العراقية الجديد خريج كلية الحرب الأمريكية وكان بدورة واحدة مع السيسي ..</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75498" target="_blank">📅 17:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75497">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
🇨🇳
وزارة التجارة الصينية:
توصل الجانبان الامريكي والصيني إلى ترتيبات ذات صلة بشأن شراء الصين طائرات من الولايات المتحدة، وضمان الولايات المتحدة توريد محركات الطائرات وقطع الغيار إلى الصين.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75497" target="_blank">📅 17:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75495">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY0vx9oGhgzD-tmaTNA7pgwnUHKF8wn4LCfyyAkpeQitf8qGTNt8z3J9-efC4ZdyQbqO7-cp5ejpA5CYG-asrCDS72HWq4DD78EqFeIxAUS_YkY0sdVy--iNnafTii7qjsAuBY805U00Ki98CNNcYm13qnX77n0lwJWlBLzSaYtvB2ado3f3k25-CFdbsHhK72wUfh8gOZYjVdOb6xi_CJppAB3rNlXbCqVdcIapmbd3V8QzwllTtEi_lw8BphTVIkGmKW0HiGEygm7UIVm7AwGjfYdeBpuCfCsgNYL43hi7-7ajevJigHubsiXi3sObq3AcsyjAKItH4aKtp7bDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
دونالد ترامب:
يجب تمرير قانون إنقاذ أمريكا، الآن. استخدموا مشروعي قانوني الإسكان وقانون مراقبة الاستخبارات الأجنبية لإنجاز ذلك! تم الكشف مؤخرًا عن 500,000 بطاقة اقتراع بريدية مزورة في ولاية ماريلاند. لا يمكننا، كدولة، تحمل هذا بعد الآن!!! يجب الموافقة على بطاقات هوية الناخبين وإثبات الجنسية، الآن. يجب إيقاف التصويت البريدي الفاسد!!! ضعوا كل ذلك في مشروعي قانوني الإسكان وقانون مراقبة الاستخبارات الأجنبية. لنجعل أمريكا عظيمة مرة أخرى!!! الرئيس دونالد ج. ترامب</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/75495" target="_blank">📅 17:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🌟
🇷🇺
السفير الروسي في بغداد:
مستعدين للتعاون مع الجهات العراقية المختصة بشأن الموقوفين من حملة الجنسية الروسية في العراق، وفقًا للقوانين العراقية النافذة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75494" target="_blank">📅 16:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qas2K8qNe7SOM_53cgzytq2gSL59fKHNfT3i4TeAk000K6RO60mBMI9vAk4Y8r-jKZmERssgQ7FVyXZaIHyYXaZ7H5FDu2r4wysOBNXWHtXSRIj45c9dGsRgPEWrxZdM90GZatSlcItDItZk4WB8CUHOrewuo0iKr6lkNWHOyHnbkG1ZmI3BiGWfj_TQuMcl823Jzfp9mk8YXnmOU9d97P5EvW0JRSBRdZBXbRf0-I-tiN-RWaxSMxpMTn6nULzCMPyhycPh-MKRL0NEtfVI16YOZry3at4OQ5Nxrbr4Ebbme3hnhuApvrMifxxdYVrrhV6v5U4FVM4BKAodT-ha1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARtpOliWoZYACckdfAQwpl-Xd33uje2uhylgzmIFza3s9zdbS9TQLB25s9J5sCcd9lfwa2mNAREXXa-9VrxzUGjkIZCNWgqW1IxrzeMxYeDfVG5qPYmeDZGhLgSGlP4yPnt22BdGZu7pKoQ_4Fbz5jfhO7CC8RmHLBukGZJQzt2s4jllrJv3MXQVxHMeNFFvMTLLNX2zCxkRXgdBIG5gVM1H-mSoezceRi6IE1Woq5PMmUsCFtuHwMdvMmu59C2Z7HPG-6frh1-xjNhnCv7nEmGjQ3EzLfVpNacCHolF-2Qq7GFWtXmA7E4uDBgeugQP9TMPz3ghX1jasLmgI1lrgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHPa0C2PdDHNzF2zLgE8nPSEHOnAokUPmhtK1Lvh8HuKOd0UmBU5r2BADEBL5IidIKB_LAA3emNgXSBBt5fVNTxuW4w7oNi6CzBUts_uyYaknj22ATYno_e3as36n3Ww5_kJfSPAQ40sX9u8Q0v11ZQX46eaIsDGgF8yzJERCRKjp_T2GCqu7YmKLJeBQ8wvmxdBe-oCL7UPHROMxUAl_lELiDbJ6odGmtd1UjyJpNVcwwMIHWQR5u1vTWJwLnnoglcBHRORMZp3uQEivt268J5KbfMb3cShCVNddK8VI8C-OBar1W077cpXTk_QLbfIt_38nsj9XK-u73YRrDvRVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
🌟
مدينة الكاظمية المقدسة في العاصمة العراقية بغداد تشيع احد شهداء حزب الله بعد ان طلب في وصيته دفنه في العراق.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/75491" target="_blank">📅 16:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75490">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صافرات الانذار تدوي في المطلة بعد تسلل سرب طائرات مسيرة تابع لحزب الله</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75490" target="_blank">📅 16:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75489">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🤺
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ
14-05-2026 تجمّعات لجنود جيش العدو الإسرائيلي في بلدتي العديسة والبيّاضة جنوبيّ لبنان بالصواريخ والمسيّرات الانقضاضيّة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75489" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
🇮🇷
وكالة الأنباء الإيرانية:
زيارة غير معلنة لوزير الداخلية الباكستاني لطهران للقاء المسؤولين الإيرانيين</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/75488" target="_blank">📅 14:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75487" target="_blank">📅 14:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75486" target="_blank">📅 13:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPMdKiIXYyDV80E1AD3U4Q2KpRYTbmB8si8YmkJpTAlsz8LqBYn2iFjT2bCi2QqEwy---_fTiDs7B4JeEQaUAVbD5s1C5zIr3bkbngT2xVSOLdfdKMUP9YmlC-j1EDSnBeVhhzfPq9Swa36EcO500rQBgT-l7rWn4Jwkmu7bbd3gk9vmBQ3DMT2ZLhVn8Vr1PtZs7yJevyVXs9jDtgqnaM_YhEu3xi3fP8HoNMNSMU71cLsngiOwhIi9VEuKfcU4n95eiSJKi6u2uN3VyCEXwURY59C_YLoiA16L6QT0d15OCGopZbX6IqjsJYtDvAtl4iDr-vd00Ggv93vkkp2ZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس لجنة الامن القومي الايرانية:
أعدت إيران ، في إطار سيادتها الوطنية وضمان أمن التجارة الدولية ، آلية مهنية لإدارة حركة المرور في مضيق هرمز على طول طريق محدد ، سيتم الكشف عنه قريبا. في هذه العملية، لن تستفيد منها سوى السفن التجارية والأطراف المتعاونة مع إيران. وسيتم تحصيل الرسوم اللازمة للخدمات المتخصصة المقدمة في إطار هذه الآلية. وسيظل هذا الطريق مغلقا أمام مشغلي ما يسمى "مشروع الحرية".</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75485" target="_blank">📅 13:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulWT960Wz_WQ9sFC6CtymxVWCUKn12MBsiFZsKff36vdwUmwQL7Z5rwAY-JDd8yUNpRFP-NP9E1qMEA63kUGcG_c5fR5jSshrc1Cam86SuTKtMl3IKI3TDo1vWjLa5uoF0c5PvidcitmgG9AatbwGupftwHpHLXz_IDY7H6cNV8csqAVCaeTS0uv29drqs4UoOBuPhvjDe8XGX0MNL5dLhcEF3qSDdd3rTKMXcit_4_j_XMSud8UacNPQZXuPTd1sA5qO9z7i7hgVkx-haTrv-Ly6-u-VUg0QCupftcqmTgYfw22zF0u-YEqZgwzltJGtfGYLlrLGQ564j5C1hOOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهاز ال FBI الأمريكي : ألقت عناصر مكتب التحقيقات الفيدرالي القبض على محمد السعدي، وهو هدف آخر ذو قيمة عالية مسؤول عن الإرهاب العالمي الجماعي، وأعادته إلى البلاد - في أحدث نجاح في العمل التاريخي لإدارة ترامب لتقديم الإرهابيين إلى العدالة. يُزعم أن السعدي وشركائه…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75484" target="_blank">📅 13:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df110dc480.mp4?token=Jbq7sobiDCUkzMlcZV_TEQeCt6bNBTmdKUIfV2PlxN2W0HoDWCvKN_3qwWOzbZSje__oNiR8rWjV2QHkRb6tEnQMK67KTLw8zeZIvG9p9A7NAGzCBOBYSWCFpPTfxXTIpOY7gWFV2ZsazqLKuSCHlrk0MZpILFEUiMPPm7FDWaEbS9oGR_lBpmmSnmUVnEGhNITM1-2ls5TI4Fpg3hBinRttU5sDZ7vZzPBbzvzHUatSG0tmPmkwjPLl7gMWXkBsct5sBcZe9ehyu9eu9Fado1m_zs2gGCLS8OO-qEbNZCohv6pufyTt0XpZ2-AKv31s_bbTtZ6rZDw3VKTkhJaIeStV6bEzj4brig36GAgVWUH4tFIRR9qWZMsuRF-WBdTfNmn7X6cNxAHzPskR8GNLpHNwCI9IaP0QcBF0xTSO6JB7jEEIif3qCCfB-FvnV0bU3TDReVMimYIutzY4FvsE3AsHFU17Hg83M14yRRDh0ti7eElpzukck5RL5k71BHkPN8BrDfwp883_LuM8YPZ7CzNBlc_Ozw4lSY4Bey_Dggo5GmvBgKwy3cZ9zlJRa7C9382beWgal4dqvEHUM7hvOIm_wS-oyJFjYLcnCNlEOjLAeOR2QPWZm7JAFAIba-dNJJ7bpFPwBxisih9fD2xLmMZpgVdKFB4PWcoymgUDt_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df110dc480.mp4?token=Jbq7sobiDCUkzMlcZV_TEQeCt6bNBTmdKUIfV2PlxN2W0HoDWCvKN_3qwWOzbZSje__oNiR8rWjV2QHkRb6tEnQMK67KTLw8zeZIvG9p9A7NAGzCBOBYSWCFpPTfxXTIpOY7gWFV2ZsazqLKuSCHlrk0MZpILFEUiMPPm7FDWaEbS9oGR_lBpmmSnmUVnEGhNITM1-2ls5TI4Fpg3hBinRttU5sDZ7vZzPBbzvzHUatSG0tmPmkwjPLl7gMWXkBsct5sBcZe9ehyu9eu9Fado1m_zs2gGCLS8OO-qEbNZCohv6pufyTt0XpZ2-AKv31s_bbTtZ6rZDw3VKTkhJaIeStV6bEzj4brig36GAgVWUH4tFIRR9qWZMsuRF-WBdTfNmn7X6cNxAHzPskR8GNLpHNwCI9IaP0QcBF0xTSO6JB7jEEIif3qCCfB-FvnV0bU3TDReVMimYIutzY4FvsE3AsHFU17Hg83M14yRRDh0ti7eElpzukck5RL5k71BHkPN8BrDfwp883_LuM8YPZ7CzNBlc_Ozw4lSY4Bey_Dggo5GmvBgKwy3cZ9zlJRa7C9382beWgal4dqvEHUM7hvOIm_wS-oyJFjYLcnCNlEOjLAeOR2QPWZm7JAFAIba-dNJJ7bpFPwBxisih9fD2xLmMZpgVdKFB4PWcoymgUDt_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
06-05-2026
آلية "نميرا" تابعة لجيش العدو الإسرائيلي في مدينة بنت جبيل جنوبي لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75483" target="_blank">📅 13:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkECH72gdkcmY2Z0XnhhcXj8H6Etwo_-TbrBfPT9xAyDbdxTtwWy5k5ujW50QnzsFWCIWMDuSyshX8qDfK6iHlRJEF4ZlCU7RI9mZ-QBD7VD6hj9983xiiGHFNZ30Nv3Vf93NRe-eAjfP-xTFhgNx9mi_3IsNvNH9mBfWhonMaJjmRmA10y5FVUR405WuDWo0DbllSTFkxABUp5iF0YEJ0_efqzJMzWdTKTABiLPSjx5H2jN9b7Pk2T6B3RTlmA8hKawzNvhU_1zodX32AgoFIQmWE5sjdQsYqQoLr4XUryGrd-TjCEsx-jxz6av0j8XbyNOEbhVaXHMPZJ-D_EZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
رئيس الوزراء الروسي ميخائيل ميشوستين يوجه برقية تهنئة إلى الزيدي</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75482" target="_blank">📅 13:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ناقلة غاز مسال قطرية - هي الثالثة خلال الأسابيع الماضية - ترسي في ميناء كراتشي قادمة عبر مضيق هرمز</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/75481" target="_blank">📅 12:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75480">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
تعطيل الدوام الرسمي يوم الأحد لموظفي مجلس محافظة بغداد بذكرى استشهاد الإمام محمد الجواد (عليه السلام)</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/75480" target="_blank">📅 12:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f924a615.mp4?token=IHZJGbdXPna7SiG-tzP2Hc7OvV95Pux8AZVlddLkyrQccRs0y9crwwpoXuw6G3CZBc9gW037mwyUzRjRXyjqKkuDykZzEGF68JR466W5slcV-4NRfgvK7NoJ6Pnigr2iY7Ns1UY0gHR2ztqIpDqldKZ5ZaVG-23-53L_xjv0Xbs6LCgPwKEq1qxsQ8ag2djPEsjW51lEkrxhB21CKmyzK3KSDR89c58iCQVrpguoFdlLYOgF8qF1V-1sB67e-Mi0gXtO_WkvZZqPc5zlxtYVCEJOaIHDKkPUuOrHnp64pg-HCIGg9f200sh7yMIjRWdfKSxaksWcF1bRlzeYx-bT8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f924a615.mp4?token=IHZJGbdXPna7SiG-tzP2Hc7OvV95Pux8AZVlddLkyrQccRs0y9crwwpoXuw6G3CZBc9gW037mwyUzRjRXyjqKkuDykZzEGF68JR466W5slcV-4NRfgvK7NoJ6Pnigr2iY7Ns1UY0gHR2ztqIpDqldKZ5ZaVG-23-53L_xjv0Xbs6LCgPwKEq1qxsQ8ag2djPEsjW51lEkrxhB21CKmyzK3KSDR89c58iCQVrpguoFdlLYOgF8qF1V-1sB67e-Mi0gXtO_WkvZZqPc5zlxtYVCEJOaIHDKkPUuOrHnp64pg-HCIGg9f200sh7yMIjRWdfKSxaksWcF1bRlzeYx-bT8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات الاحتلال الصهيوني تتوغل في محافظة القنيطرة جنوبي سوريا وتنفذ عمليات مداهمة للمنازل في المنطقة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75479" target="_blank">📅 10:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجار يهز المنطقة الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75478" target="_blank">📅 09:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجار يهز المنطقة الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75477" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75476">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تسلل طيران مسير من حزب الله باتجاه شمال الكيان المحتل</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/75476" target="_blank">📅 09:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75475">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">إعلام أمريكي: تمكنا من إحباط مساعي هذا الرجل في زرع الفوضى وتصدير الرعب، ليس إلى الولايات المتحدة وحدها، بل إلى كندا وأوروبا أيضا.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/75475" target="_blank">📅 01:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75474">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📰
وول ستريت جورنال:
لا يزال أكثر من 100 منصب سفير أمريكي شاغراً بعد مرور 18 شهراً على ولاية ترامب الثانية - وهو معدل غير مسبوق يحذر الدبلوماسيون من أنه يضعف النفوذ الأمريكي في الخارج.
تشمل الفجوات الرئيسية المملكة العربية السعودية، والإمارات العربية المتحدة، وقطر، والعراق، والكويت، وأوكرانيا، وروسيا. وفي أفريقيا، تفتقر 37 سفارة من أصل 51 سفارة إلى سفراء.
يمكن للدبلوماسيين المهنيين الذين يعملون كمبعوثين مؤقتين إدارة العمليات اليومية، لكنهم غالباً ما يفتقرون إلى إمكانية الوصول والنفوذ الذي يتمتع به السفراء الذين تم تأكيدهم من قبل مجلس الشيوخ.
وفقاً للجمعية الأمريكية للخدمة الخارجية، هناك حالياً 115 منصباً سفيرياً شاغراً من أصل 195 منصباً - مقارنة بـ 45 شاغراً في نفس الفترة من الولاية الأولى لترامب و 12 شاغراً خلال الولاية الثانية لأوباما.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/75474" target="_blank">📅 01:26 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

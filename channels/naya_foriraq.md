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
<img src="https://cdn4.telesco.pe/file/HLcs_ptFCR9u9XlF9jkPeYB_CkfX3UQrExjZRUVqT-VBL1vAgcKIbWlVLXLA_FT9_2fOVrN7kWat0Y7yirNIQ9t82_FzNEAqUX3mPcMfsTxWiu31pIzIAM5poGm5TG2xcYCsS1pjDr0GaHNiE2sT8qlvccD2TnGyopnKOyDasRI4AgCdr6Mqg6dy3hiZaH5qctAP77tEO9zXaqKZj0IRokXrxMWOwRXp-RHFKJsRuUEY3qCbJweaoDuN1796f8bS9jLk8UHTHuyupy1mTwPv6-iGzanHFdpDtuRZmXzbp5GAWnw3VN-XjbS0x0Zan22m0OO_ToSNt-zq8ubUU8_t7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-93000">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
🇸🇦
البعثة الأمريكية في السعودية تصدر تحذير امني لبعثتها خوفا من الهجمات اليمنية.</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/naya_foriraq/93000" target="_blank">📅 20:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92999">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db71UYgCrQ0BsEyqKN2z3JJ76HkZoYt6DmxT2CUgTjFARv9gIsOVsOaczNHJPHB9MWVHavN293gArf3D7V25-VYEZyjk6g-rLdNKcyDtO5qjLXrWHEf_UvhZ6n1Gg8MZEM9gjKoyUdVEy6VeS2RbsZfz_ulEdqgWH1oYnyYqyLSrCJolbysKdc8Az89tSQ6xjFwR4qhflCIS6k-HbDb1Oi23ZKtabTQrrrrCviJNsZFos9gHpap5EMBgoDcy69A3k9Wa5FfhmGXUFFgahGPYz5v8E6O8JUAgl56uLSME-sd2PoqwKSvcfStExxPahCyPEPGwZ68z0LIZ-zPG5p0w2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
المعاون العسكري لحركة النجباء الحاج عبد القادر الكربلائي:
فيا أنصار الله ورسوله والإسلام، إننا معكم ولن نتخلى عنكم.</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/naya_foriraq/92999" target="_blank">📅 20:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92998">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqvMFLaXrXrIpPCK_NG2VcEasASuzPutGjX0p8HxVMfhMrgNkWIWaBnw59lNLOidAqDg5B3X4c0mzFLmeEogyurkE-H7qzjg-jhQI0TAx61UvvanJquIgv9QvRK_P2HoxsoMEJN5PxvgLT2PHVE2Z7vLZVdEh_9CBxd5VJ2j1HJ7kwud6paqy2Hlouu987wC0S3NhmCTFOfiAVVF7bXnnNUgxawcVT2JFg6sRwf2BQm_a5ITMQ6I-O-HXfQUWMYAVbWfXLvhX-Hy9SPH7EDQmUEhgBQEiEr1K3tt6vMYnO7dnu4sVwaMxlJ69fzldAQrCSalxyX0dKkYY6JT-R_ksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: لن نشن هجومًا على إيران في أي وقت قبل الانتخابات النصفية، نحن نجري محادثات مثمرة مع إيران.</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/naya_foriraq/92998" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92997">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZkc0YYEzN5N7ak400nlzHIkcNlAdSMTq7SZDj9PTpwWEk_cul6EKeCI9kUPlqDQdsfpmIzYmQlVcGSQrD23M-ZZI-xEQG4sjTaLeOaP4xRFDo4G8nzM9JsO5GxYxJDrFegSYfKUse8F693Sfy0kvAwPkEXmnuUTDZkeTBHyAphmhW4RTHnuYe4WSz_PFSH6JCU2lgpgZxCJ6WAjwzVWCDpxIsupXm2jLp9Ffnl0rZ6vqIX7K2I7wMSF7f2xLE5qSADvvtJkH_GGNn1QmMCp_gwK4rsVYD1cQRpZzaOQw8wZ3vFVJmBK7ZSdhotV6_Zj2lZh_q6ZwPh5AC7p-xKNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
: لن نشن هجومًا على إيران في أي وقت قبل الانتخابات النصفية، نحن نجري محادثات مثمرة مع إيران.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/naya_foriraq/92997" target="_blank">📅 19:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92996">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تدمير طائرة في مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/naya_foriraq/92996" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92995">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇶
‏
مستشار الأمن القومي العراقي:
العراق رفض طلبا من سوريا لإعادة آلاف الأشخاص المشتبه في انتمائهم إلى داعش، اجتماع عُقد مؤخرا بين سوريا والعراق وأميركا لبحث مصير سجناء داعش، العراق أعاد إلى سوريا نحو 50 محتجزا سوريا ثبت أنهم ليسوا أعضاء في داعش.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/naya_foriraq/92995" target="_blank">📅 19:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92994">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv7iCY6xEnQJuqRNKDMQJbnKuEE7TQTsYE5kP3IOEeLpCMeunpxEV48a8kBjYXDHJ6S3XCD3cLQGezBynujM6TRkh73I40K0Ikl2xQBZEQlHmNZpJG6tGu5ss_ctTaGUAAkUHOa2OfMk1KuGjXJNy9nX7x2KMQaM7Lf8am3VEg4t8IqxeB9Gf2MbeWWXiNXP2Z3iSkpzr5AvU-_5Oj8jQTmtEy2eT1sMibDzkSGz4_4Ha_6qsD4lDUXPQOA-Rg6_djqjvlu7h6s6yGbaHSxjxtSgr399bg67JHaRSlgoMpxsMd-0LuEVysRJqJm5F0VcphUAkRlBTE8Y8shenN4DyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظة الهجوم اليمني على مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/naya_foriraq/92994" target="_blank">📅 19:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92993">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06b1ab0be6.mp4?token=DrC8uf5SEONthKkQv8w6g-AxkwZuC83z583uCeOvoaKx4WsWDLotvKyrIMTBmKAMvENkMx3U7MpuW7Lr8YxTzjTN9TDxXLbE-5WKSrel0yz24JhSWAUaMz7DHwHmRMvuD7qFxIJbd-X-03rCchVGC0bcGO2cOt3sIm0NfMMRyOBpR_TCNamg-qHg_sUwFdN_vD16IRgikcW4mtaqXV-C-qFPE-h5ytcc3hcyphbQf64XcJYlzuVtnig-6EEUOah3WVcd0I8bulmhxY6zK64tvSQj0Spx00EmTinkPC6ZUKjb2VB0m9lEddOG_1gjBCEcMSWXSOHXM5xim_vyTn8z8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06b1ab0be6.mp4?token=DrC8uf5SEONthKkQv8w6g-AxkwZuC83z583uCeOvoaKx4WsWDLotvKyrIMTBmKAMvENkMx3U7MpuW7Lr8YxTzjTN9TDxXLbE-5WKSrel0yz24JhSWAUaMz7DHwHmRMvuD7qFxIJbd-X-03rCchVGC0bcGO2cOt3sIm0NfMMRyOBpR_TCNamg-qHg_sUwFdN_vD16IRgikcW4mtaqXV-C-qFPE-h5ytcc3hcyphbQf64XcJYlzuVtnig-6EEUOah3WVcd0I8bulmhxY6zK64tvSQj0Spx00EmTinkPC6ZUKjb2VB0m9lEddOG_1gjBCEcMSWXSOHXM5xim_vyTn8z8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اشتباكات مسلحة بين يهود حريديم وقوات الامن اثناء تضاهراتهم في الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/naya_foriraq/92993" target="_blank">📅 19:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92992">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
استهدف قواتنا المسلحة مساء اليوم مطار الملك خالد بالرياض بصاروخين مجنحين، ومطار نجران بصاروخ باليستي، والقاعدة الجوية في خميس مشيط بصاروخ باليستي، وكانت الإصابات دقيقة ومباشرة بفضل الله، وأدت إلى تعطل حركة الملاحة في المطارين وإلحاق أضرار بهما وبالقاعدة الجوية.</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/naya_foriraq/92992" target="_blank">📅 19:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92991">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
🇮🇷
اللواء وحيدي
: نذكر أن استراتيجيتنا في هذا المجال واضحة ومبدئية وغير قابلة للتغيير: أمن الخليج الفارسي ومضيق هرمز هو أمن داخلي وإقليمي، ولا يحق لأي قوة خارجية تهديده أو التواجد بشكل استعماري أو التدخل فيه. مضيق هرمز هو شريان الحياة للطاقة في العالم، والخط الأحمر الاستراتيجي لإيران الإسلامية، والحفاظ عليه هو الحفاظ على المصالح الوطنية وأمن الأمة وكرامة إيران.</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/naya_foriraq/92991" target="_blank">📅 19:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92990">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات تهز مضيق هرمز: ناقلة نفط خام تعرضت للاستهداف بمقذوف أثناء عبورها المضيق.</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/92990" target="_blank">📅 18:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92989">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">😀
الخطوط الجوية الهندية تلغي رحلاتها من وإلى الرياض حتى 10 أكتوبر نظراً لتطورات الوضع في المنطقة.
المطار بالمطار</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/naya_foriraq/92989" target="_blank">📅 18:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92988">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92d6aa9cc.mp4?token=oz35TEKU2x5hA1R2aQKLmkJev5NXgFu8nBnx8_6gGJRp3IFlLRduLymGaPqrNVRu0_0UQ9vtoEcPTkGGyHX9SE0UEm4SkZBoUrutOy4auDdSfEtbD1wYWNzgt359TSjdtQtIiuLwblDW-dZ7YHt_KQYDOJe_tzeBk-6Z1JXL5sbBv3dLDtTjcaWk3XXLia6Sif1vkouMYpHd6IKcratS-IM6-NwE9xdVr617GtI8EHyHpl3BFWp6FGqwWqzJ2sdZW-E-_Pb5VKWJHspbAlGxqnYohvCB_b6-NkeAqp3wG9JCgPc-aVpU3gO0CCtU1An3JaSfsuS0D2zAfZHT7L7ifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92d6aa9cc.mp4?token=oz35TEKU2x5hA1R2aQKLmkJev5NXgFu8nBnx8_6gGJRp3IFlLRduLymGaPqrNVRu0_0UQ9vtoEcPTkGGyHX9SE0UEm4SkZBoUrutOy4auDdSfEtbD1wYWNzgt359TSjdtQtIiuLwblDW-dZ7YHt_KQYDOJe_tzeBk-6Z1JXL5sbBv3dLDtTjcaWk3XXLia6Sif1vkouMYpHd6IKcratS-IM6-NwE9xdVr617GtI8EHyHpl3BFWp6FGqwWqzJ2sdZW-E-_Pb5VKWJHspbAlGxqnYohvCB_b6-NkeAqp3wG9JCgPc-aVpU3gO0CCtU1An3JaSfsuS0D2zAfZHT7L7ifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباكات بين الشرطة الصهيونية ويهود الحريديم في مدينة القدس المحتلة.</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/naya_foriraq/92988" target="_blank">📅 18:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92987">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزارة المواصلات الصهيونية تصدر تعليمات لشركات الطيران الأجنبية تُلزمها بإجراء فحص لأفراد الطاقم والجنسيات التي يحملونها، في كل رحلة إلى "إسرائيل" أو تعبر مجالها الجوي. ودخلت التعليمات حيز التنفيذ بشكل فوري.</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/naya_foriraq/92987" target="_blank">📅 18:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92983">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHxvEz3IDpj652J-ohq1S8opqMAqzBtxccUrygNk34-njIyZ3FATBKNPyIFC_NGqYe1cERJ_c3KXuWtx7ozXDN3_6iZw9vgUNholp0Jl4hfVHsGzoZA89Nx02lbxPk0fELTVmhUMDXaCYggyqDf-_cvtD1pln0-HUwtRHt1vmORIQH70czO8TBZtLLT7Bx0NtQtxypXFoA0-MShkqY_aAWkchQw64CrHrxZ_C7HHDBaXF3FUA9t0rmSh4d1J7KpYfTxtviFuW05OUilyEvTodkSuU3CfgwtwsJjtQZCmFcXOh-u18WZmrYyksnD-P7iZx4CRm1VhiHGFYAOqROtKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZjlk5rDRstKgj3-6vjQIYeYh4enBJjtWQNcaXPn5PR5FsTyVVNpTt9NNNOwafQW30bbV7vo0OslzrhSCoVwTthOlBmUSB8WiIwR1X2_C1t6sXt7vBF2TG4MDL4SNOMSy160nYNFjT0admoD_TgGe55idrIMn_R_pd2G-aOJA7tLht1pT2RdOiXRtAzoyQT5wvP8YQcCpYmoa6xGEdqnAIew5EYWrwxJHZyIV4YsuNXvwjy-nJ_iAt0i8Ckrw5ZM6m9QlWc4Ho3IJkQzTUQHyB-upUlo7yHWWMCuZX4syItirKg2bboUAmOSai_MmbwW6WL-MLclhFOC8evglW3Vig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479a877651.mp4?token=J89fOySF1TA8b-EkniSOaji8GSDmBulh9CpF-vUnbVevR2smzEEDCCosB8SYFUUOJDtc6F1AkHYM4damKrH0kbSYnEqmiXLGC-PWQOLx6LBqwweOj5bqItbrPgARZjtQfARGAIb8gM9vsMXRANDGIo_yU2D7lR9JtF3ZnUHRHl-IjEh2G0nDRQvGXorKcCfbIkNP18rFdN4XUSr9m5EdMybGPeTFy5Y6uYKwLyaex4f20O3l2APwjZZorqXRmm6CLu656lP--d0O_P1vyaegREWC5YgdPPU23TAdadg-LtGvQ3ZgKlKh25lEIk8iiyk_M8z-vYfmGF-Xf_wFWJTmbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479a877651.mp4?token=J89fOySF1TA8b-EkniSOaji8GSDmBulh9CpF-vUnbVevR2smzEEDCCosB8SYFUUOJDtc6F1AkHYM4damKrH0kbSYnEqmiXLGC-PWQOLx6LBqwweOj5bqItbrPgARZjtQfARGAIb8gM9vsMXRANDGIo_yU2D7lR9JtF3ZnUHRHl-IjEh2G0nDRQvGXorKcCfbIkNP18rFdN4XUSr9m5EdMybGPeTFy5Y6uYKwLyaex4f20O3l2APwjZZorqXRmm6CLu656lP--d0O_P1vyaegREWC5YgdPPU23TAdadg-LtGvQ3ZgKlKh25lEIk8iiyk_M8z-vYfmGF-Xf_wFWJTmbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات اليمنية تدك منشأت ارامكو في بقيق</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/naya_foriraq/92983" target="_blank">📅 18:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92982">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUSWUgtyv0II_p7u2vS3LT0jexS8xV9iRnv7bXTkCRdQqtrvPiKjuZGyBrjRhi_HGwA89ShRsGqcGzPBYWn7wrOfwXqNl0mwfX0UBhycPu-48i7Z8UB3-e3GSKwniGufUGGQKwJ8Buy82zBW7y1YJLhxzhdGIQpJjXukHi1_9j-mef1z4GDKvFjWHIOf0C7ucqUYvtYi1V7VJ4DqzO4YI0Jw5M3WxnSf8QBeDKwaPaiMgciLU0KKhShizyVC8ulN2zM_3MXTZXnDikeoIf3LUa-jetEGoKxPj1ijlmTwE9v0CQJxCpJHxv86h4elfxK6Yj304Eu2QThogHCILx8Oxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز مضيق هرمز: ناقلة نفط خام تعرضت للاستهداف بمقذوف أثناء عبورها المضيق.</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/naya_foriraq/92982" target="_blank">📅 18:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92981">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇾🇪
التلفزيون اليمني:
العدو السعودي استهدف بغارتين باص نقل مواطنين ما أسفر عن شهداء وجرحى في طريق شرجب التربة.</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/naya_foriraq/92981" target="_blank">📅 18:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92980">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c545f6ef23.mp4?token=I-eMKoBcWa0ZNA0nvfxDuFnXIdtEsvNBcVyvXnozMI-RrWw1BK4GD7-JAqGhy-gfa0EVKIVNYzWwTyUJa2Yl2AQ1Ytv_830iwlCmGMZ89UahaY6qyPX0ukVc13L2uvEFQGTIC5x9AQv9u5eC9oZpEJRF_7uYmcHhbqeMLWysA1vHqWZuBFPO2zsZN-drkpR1jrXg7bGJJlVizzzk1EyADDWYXJTV0eij3zebpm7DS_8F1O_MzZpuOxknWZxGXSD9vBw6ufJICtfebdNoSGqHiEn4Cy2pPe_0p0Yj_4n-Mk0YzB3SjlIx_alMtxJsE30wxEoNYj2WL_ungdL1QtjpPTeIMR0iyO4e3LSC0lbp039EY13EijIdIdznNQm_-RDWYq_zxxf4IEZDknd8SeLk7216h6_3wd85NrEhl3fN625KJ3C6EifemKWD345t3X12IacgbfBdOjtRPjXcOeir9igjjfFLX8rM3zOJMFsrE4ixGEizcxBXHOf12HcEKzYEbUP78aS386p8edHMc-3jejQ58kmK9cIsMQGPD2nWXYxYYHjkR34baaDfphomYo5xsXTKbDQ-De-CTwHUgq3mUd8Kp6xGJQIUQKFv1lv3GC850d8rUF4aq8POPtnOtX7kP_OCDrVaP8YAf9F_85RZjtLwUSMRZRQDvEhng_EMOeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c545f6ef23.mp4?token=I-eMKoBcWa0ZNA0nvfxDuFnXIdtEsvNBcVyvXnozMI-RrWw1BK4GD7-JAqGhy-gfa0EVKIVNYzWwTyUJa2Yl2AQ1Ytv_830iwlCmGMZ89UahaY6qyPX0ukVc13L2uvEFQGTIC5x9AQv9u5eC9oZpEJRF_7uYmcHhbqeMLWysA1vHqWZuBFPO2zsZN-drkpR1jrXg7bGJJlVizzzk1EyADDWYXJTV0eij3zebpm7DS_8F1O_MzZpuOxknWZxGXSD9vBw6ufJICtfebdNoSGqHiEn4Cy2pPe_0p0Yj_4n-Mk0YzB3SjlIx_alMtxJsE30wxEoNYj2WL_ungdL1QtjpPTeIMR0iyO4e3LSC0lbp039EY13EijIdIdznNQm_-RDWYq_zxxf4IEZDknd8SeLk7216h6_3wd85NrEhl3fN625KJ3C6EifemKWD345t3X12IacgbfBdOjtRPjXcOeir9igjjfFLX8rM3zOJMFsrE4ixGEizcxBXHOf12HcEKzYEbUP78aS386p8edHMc-3jejQ58kmK9cIsMQGPD2nWXYxYYHjkR34baaDfphomYo5xsXTKbDQ-De-CTwHUgq3mUd8Kp6xGJQIUQKFv1lv3GC850d8rUF4aq8POPtnOtX7kP_OCDrVaP8YAf9F_85RZjtLwUSMRZRQDvEhng_EMOeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الغاء عشرات الرحلات الجوية المتجهة إلى مطار الرياض بعد استهدافه من قبل القوات المسلحة اليمنية ولم يتبقَّ سوى عدد قليل من الرحلات.</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/92980" target="_blank">📅 17:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇾🇪
🇾🇪
السيد عبدالملك الحوثي:
-
بالأمس نصحنا القطري الذي بات يتبني العدوان السعودي على بلدنا سياسيا وإعلاميا، وهذا القدر من المشاركة مشاركة في الظلم على شعبنا
-
نحن بالأمس أشرنا إلى القطري بما فعله به السعودي، ونقول: نذكركم بحقائق أنتم عشتموها في واقعكم بعد مشاركتهم في العدوان على بلدنا مطلع العدوان عندما لم يقدّر لكم ذلك وقام بحملة كبيرة عليكم
-
النظام السعودي عمل على عزل قطر بشكل تام والمقاطعة السياسية والاقتصادية والترهيب العسكري وحرّض الآخرين عليه
-
النظام السعودي له أمل في تغيير النظام في قطر كما آل خليفة في البحرين
-
هل كان للنظام السعودي ما يبرر كل هذا ضد قطر، وأنتم تعرفون أن طموحاته تجاهكم سيئة للغاية إذا حظي بإذن أمريكي
-
قطر عملت إبان الأمير حمد على حل النزاعات إلى درجة الغيظ السعودي منها، والعودة الآن للتبعية للسعودي في السياسات الخارجية تراجع كبير جدا
-
ننصح القطري نصحا أخويا بمراجعة حساباته، وشعبنا في موقف مظلومية ويدافع عن حريته</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/92979" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92977">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2y7NTClO6ddarHJED7KkhxuY2ipAeg_EFjLy3u74SCAm84hbx9s7s2MkyrhdCP0xNjQKjYQRRDuBTyImFJd4a-d_XRmZkqmq-s5V14VGmINrWHxngfPusiwbwfdTm8gu3R4VyfkcyRY-OebILOAERzui6RHDR9sZKTgweyykl39Eyr3EjnmoH6h97hsw9uPS_HrJLWDbkseJGGIlTyP7S-ujZc2_6R-Lh_FS5fZVMrNAyfn6kedGItuiNJfx83jn53OroabKaKhLAKDqLO10w9ZkERmAZ7uTfynMBsSUTcxgBKjPKlVs8KhRKm162gMJnYps2NVkficgjsByMbRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibIKt1RERA2ZRKNy2-NMcvvtyqccfVUKGhTtNhg6wV694HhBTyQAJqZFDJ_DInI-foT2_W0icXLpSYM3tnZU3RWYYkNVbsodjwvoZh79e0mFJ6JZVq2GokdBKT8bE4TVR8zrTZ56g6KeO1zMp6bpWOAd2_xA31PdNO6sFlFdbYyCb-qQyn3gmHe0I0eOVW9lxnbrDORGGLU2j17QfxDOtXb2smpV2fMYgYmvuowDioVUEVuK_LKsmYI2Fsn7L53TbR9QrokvukADpMHnlngjmC3azPsMdimlY4CRn4AKhVx8NB5yGOQbdSvD4Qq5dkhGOfNYIkSI29euIS0_rbDlWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇱
قوات الاحتلال الإسرائيلي تسيطر على قرية جبة في وسط منطقة القنيطرة في سوريا بعد تسلل دبابات ومركبات عسكرية.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/92977" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92976">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde9df01ca.mp4?token=IMllopSMuhPicfXyZ876X-X3sRZPu6nRf4ouGk-SDQCxBd8duKd0viv9cV5uyydsDJg7iGT0mNCGMIgt46b2ibQjL4l3I2hXvmuWu9LEhYcUmX_LtVGSgaTLTj4Cq89mcZMHH9wWVFEqewF_WeaMo83rH2981JGUI7pNRlZURTFJc8s9CoAvGqjwdSnBwl7Lh2_U6ldD8VGzyHZa0rFvCxiW2DwPG3bxrVZdJbaA8fEOakR8DexrD24ukeyTLb8oM62vjxAq7Tvn4jem_90NZ6waPHkToOM_RpAVm1FzCwomPgF-T8DBeEP3ceARfK5R74XWINECjaLKbYdfzmh4pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde9df01ca.mp4?token=IMllopSMuhPicfXyZ876X-X3sRZPu6nRf4ouGk-SDQCxBd8duKd0viv9cV5uyydsDJg7iGT0mNCGMIgt46b2ibQjL4l3I2hXvmuWu9LEhYcUmX_LtVGSgaTLTj4Cq89mcZMHH9wWVFEqewF_WeaMo83rH2981JGUI7pNRlZURTFJc8s9CoAvGqjwdSnBwl7Lh2_U6ldD8VGzyHZa0rFvCxiW2DwPG3bxrVZdJbaA8fEOakR8DexrD24ukeyTLb8oM62vjxAq7Tvn4jem_90NZ6waPHkToOM_RpAVm1FzCwomPgF-T8DBeEP3ceARfK5R74XWINECjaLKbYdfzmh4pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقفة احتجاجية في محافظة البصرة رفضاً لرفع سعر صرف الدولار والمطالبة بالتراجع عن القرار</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/92976" target="_blank">📅 17:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92975">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b86a06f11.mp4?token=tvXLGBr_kBfjWRfLlkzK1MXddOhvU2OjOVwPGFp5p7pdfnVMNreVNwNgX2jjrDPXqK2CCgM8VsRIx5VU5rybEWG7CqRUTynjbLDLe6Z2mXwIiAa9wKSPsuNsuwLmH7q0Df0TBz7ARp35MKcLWQ-9NiIgn9Zt0uH57wdJ8hC1KCji7rVDJAg0iWaP6aY8ZPdXrb7KNEgJETvNW4HkZhKGx1FFsEr4tp2glfA8TdOgmHT20vIpVePhrItlG7pwG1DQvTM0WA1SUkg8mHBaJKqHC5tJ7RlZNOOQxGkQYulcHI8mwevbYFERWzxTw4wto1grysiCO1XSzkqbKsP6Qh7qDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b86a06f11.mp4?token=tvXLGBr_kBfjWRfLlkzK1MXddOhvU2OjOVwPGFp5p7pdfnVMNreVNwNgX2jjrDPXqK2CCgM8VsRIx5VU5rybEWG7CqRUTynjbLDLe6Z2mXwIiAa9wKSPsuNsuwLmH7q0Df0TBz7ARp35MKcLWQ-9NiIgn9Zt0uH57wdJ8hC1KCji7rVDJAg0iWaP6aY8ZPdXrb7KNEgJETvNW4HkZhKGx1FFsEr4tp2glfA8TdOgmHT20vIpVePhrItlG7pwG1DQvTM0WA1SUkg8mHBaJKqHC5tJ7RlZNOOQxGkQYulcHI8mwevbYFERWzxTw4wto1grysiCO1XSzkqbKsP6Qh7qDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة الهجوم اليمني على مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/92975" target="_blank">📅 17:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92974">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fc6292df.mp4?token=EVDmozho_UvBAivqW8OTrHdyOWAp_ZKzgtt--llBCXldvMZR6pkj9d7N0ZiqENLtCLXAZ9jFcjY1eUk-J2S1Lx-UOeYGH8947zjlMM4GYRd25KE3kojJeDeKtkB3pMMaoGAUa6YOCldmJFuyPL_lTL7g55NtZSNvEaL0W9WWmmlrCRkNwy5MECF-NlHoo52R6vmYKq4SNewQ3Rs5_EJ1NYoUz6gAEcAGmb12S26b2UCDepvYghXbk38GPzhcW1srPQ16dgfM6Z-jTiflInqAg8HHjzvd0fKTMgWU-F3VjTzenzUIFGA4RV5dgKcJdQaTxpsgjEz13qReF-ABTsn48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fc6292df.mp4?token=EVDmozho_UvBAivqW8OTrHdyOWAp_ZKzgtt--llBCXldvMZR6pkj9d7N0ZiqENLtCLXAZ9jFcjY1eUk-J2S1Lx-UOeYGH8947zjlMM4GYRd25KE3kojJeDeKtkB3pMMaoGAUa6YOCldmJFuyPL_lTL7g55NtZSNvEaL0W9WWmmlrCRkNwy5MECF-NlHoo52R6vmYKq4SNewQ3Rs5_EJ1NYoUz6gAEcAGmb12S26b2UCDepvYghXbk38GPzhcW1srPQ16dgfM6Z-jTiflInqAg8HHjzvd0fKTMgWU-F3VjTzenzUIFGA4RV5dgKcJdQaTxpsgjEz13qReF-ABTsn48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ اليمنية تصول وتجول في سماء السعودية</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/naya_foriraq/92974" target="_blank">📅 17:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92973">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c997f9f6.mp4?token=fIKrGSLQPfMTBv7YkZG0STLIBiKYk-6XRxkGcZNtfzDgAplYHodNrJ_9wobT8D2fv0ycXvdy7_woxHcn7waPP2faP3iDdMGtlU_SenZP77hLpqZnGtX8eagidn1HJQaC_mmVCXvbSPmch3e0yhSjHNH40IlSPg1CnZ6LDtyyxXQ-sCwqDLdSBsRtCE28upy0f8pNH5S7rDSPdqyiB3I3zag06vc_CVoZlosnkY0bfbE-hW6kpwlBUVCfX3a7nNlYlH6Nj1uE-3iixsQULdMP64X_1g-txxEA5VyYRBrjNshm_JO6QCDcLhBj7PVWlraMAjCCBUVgsyX-Z0PtsogCDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c997f9f6.mp4?token=fIKrGSLQPfMTBv7YkZG0STLIBiKYk-6XRxkGcZNtfzDgAplYHodNrJ_9wobT8D2fv0ycXvdy7_woxHcn7waPP2faP3iDdMGtlU_SenZP77hLpqZnGtX8eagidn1HJQaC_mmVCXvbSPmch3e0yhSjHNH40IlSPg1CnZ6LDtyyxXQ-sCwqDLdSBsRtCE28upy0f8pNH5S7rDSPdqyiB3I3zag06vc_CVoZlosnkY0bfbE-hW6kpwlBUVCfX3a7nNlYlH6Nj1uE-3iixsQULdMP64X_1g-txxEA5VyYRBrjNshm_JO6QCDcLhBj7PVWlraMAjCCBUVgsyX-Z0PtsogCDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رصد عشرات الصواريخ اليمنية في سماء السعودية</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/naya_foriraq/92973" target="_blank">📅 17:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92972">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">السعودية تعلن عن اضرار جسيمة في عدد من المنشأت بسبب "سقوط شظايا".</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/naya_foriraq/92972" target="_blank">📅 17:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92971">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇱
اعلام العدو:
اصيب جنديان من الجيش الإسرائيلي إصابة خطيرة في حادث عملياتي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/92971" target="_blank">📅 16:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92970">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مطار الرياض الدولي يشير الى الغاء الرحلات:
ننوه للمسافرين بضرورة التواصل مع الناقلات الجوية، والتحقق من حالة الرحلة قبل التوجه إلى المطار</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/92970" target="_blank">📅 16:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgewXXedLZM_pfjh22uXcN4wwPhT1WA50Us1PJMF4fQ4SpextIVSmen9jYCySvua9rF8xzE0EgoCiCY4vCB_OS9py6h9Uf74tZT_ZbmrbQFkCP2IbIXXZQc4MDQt7qksBKTRDqUMsDzdlMJxsOMJiA7IoMIUvoyuHfb-fVghXmNPf1eQT2y1zxs_j2XwbyuaXZH2wIC0bI_z3-DjIoy7gIxKstgn2aGuYyPeeLug6FKFWMpuS2OgUR1XpIjMuOaeuCxLD7ouluoTcnky1xfpsaT3YxTJ_XWEsmhnOnE0Uio6ZoE146LzMPkuvEs8ybeqJSpHW2sJMKGsK6-_MkeyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعاف جوي يتجه الى الرياض لنقل اصابات وقتلى بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/92969" target="_blank">📅 16:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b004cd58.mp4?token=LYe7b8rRKHHYxqqkq5IjOAfchruYs-n0y3QUANzWgcsnhKbnXews-3OgYcPDaOy3Tc_GOvxrTG2DXttWha7lyOwQgPK8t9aYfUQecSQYgGZq3bgXHn8Put-aZ27vaUPzdrPfWAEYA1F9vhoWQTIcY194P-jRcPdY1QD-7BsJKzqpuHp1lzPNXgJbKUhaL8f1q-fGAZ0_HhBDdHP3ioWIghScy7_U-laCy5jOcVFWPpUaV8MLw0XxiNccHqGL9_xtrgKfWHhZS123A3AC-dTE0gCXZxdi9AJVt-7XKPcv4mxbAZx4PfQtP4VYBj9Cw4jKIILYFgki7ganEiEI8WxMq4DB_qEP_mDD3qBjATHSueeB3LT73BOYwblUB_BLbL_K4CA7LzoqowX404vp6qvk8okdeNK9S0qSO4YXgokPJpMT4OqKM1Cdd7NDH0ObezjIeCBV4GGeghMnJjOXUzrtnn1IQoAlaZ2AVrh-3RYcpTJRxFcz2tEUcZNxigbVqtasVZ0rzbOO5s1wiF0wTwiVrVlD_Q9_7YFXmSkWAT7mnURezOj90j-1h4XO03OUjQVD55rZt8QgmsBVPGLkkhb-j5iTkPYRM8_g0UcnVWGo7xKOwxmSTo4s8BB0mqw62BwK1gMQda46xPOqIDH4wL4oIYYLw1lHbdsDn20MBMfiK4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b004cd58.mp4?token=LYe7b8rRKHHYxqqkq5IjOAfchruYs-n0y3QUANzWgcsnhKbnXews-3OgYcPDaOy3Tc_GOvxrTG2DXttWha7lyOwQgPK8t9aYfUQecSQYgGZq3bgXHn8Put-aZ27vaUPzdrPfWAEYA1F9vhoWQTIcY194P-jRcPdY1QD-7BsJKzqpuHp1lzPNXgJbKUhaL8f1q-fGAZ0_HhBDdHP3ioWIghScy7_U-laCy5jOcVFWPpUaV8MLw0XxiNccHqGL9_xtrgKfWHhZS123A3AC-dTE0gCXZxdi9AJVt-7XKPcv4mxbAZx4PfQtP4VYBj9Cw4jKIILYFgki7ganEiEI8WxMq4DB_qEP_mDD3qBjATHSueeB3LT73BOYwblUB_BLbL_K4CA7LzoqowX404vp6qvk8okdeNK9S0qSO4YXgokPJpMT4OqKM1Cdd7NDH0ObezjIeCBV4GGeghMnJjOXUzrtnn1IQoAlaZ2AVrh-3RYcpTJRxFcz2tEUcZNxigbVqtasVZ0rzbOO5s1wiF0wTwiVrVlD_Q9_7YFXmSkWAT7mnURezOj90j-1h4XO03OUjQVD55rZt8QgmsBVPGLkkhb-j5iTkPYRM8_g0UcnVWGo7xKOwxmSTo4s8BB0mqw62BwK1gMQda46xPOqIDH4wL4oIYYLw1lHbdsDn20MBMfiK4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇺🇸
وزير الخارجية الامريكي ماركو روبيو: لن نخرق أبدًا سيادة أي دولة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/92968" target="_blank">📅 16:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92966">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VcE3MFEab0eRUYMF1Yc_ELuBNUYF_nTrevCMsfAePb149Og05wLO2BwXS7DYjf53TLYdV6FMrvlrFJRGI9YV3wKuvgeZgVRyfQhOmrVer275ulus8DRGZiE-Xlm-m_IzsTiSmjbHYdUkB-nag1RSPGQjHhGSg8Ojvhs0X2l6lOwX6xX4IHwMzwUbfHzXUTt-cuX71gxjQ8dZiMEOO-m6SZvcOU9-sJ2cHL8AZ_DH30_pzZY64exZETN4s0YdGnaO76ybBv9EboKlBli-VF_zxmqXfz3uKTOFf5yA9nWgdaOa2dVEAXjTHBHUO6BzKhJKT5VBSR8MLw5Tpf32MJ3Ybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fn2cxOsM7gLH29p9SV-rBesm0ejrsGm8oe2Leewd4uu3eH9EBU1_9m32wktlfgAzSR43RBvxZZqS2rrRGsyS1jKIlxy98BWuvud5-ucnmEbifHsgI2iGKyRijlIEHIjEq4YkOZWdUmjG-Fcbbd90u82J4D2BhBLNPdIWaqtzZSOh2pk3UII57VUqoaXerqMdIW6eNJjeD3dkZb6-ajSzbkiXTJ5Nbm58aCjT4jUYxkhCX3LnYqiUUYVTUfFWJ9j87P88x1AGV5Lyr6N_vcVMY30cq0PPIYjUZfqFxwFXGAZqe0LJnAwMawrGS8oa7IVFz_enxIA0boeWcqs1RQ0jnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات اليمنية تدك منشأت ارامكو في بقيق</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/92966" target="_blank">📅 16:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92965">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">القوات اليمنية تدك منشأت ارامكو في بقيق</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/92965" target="_blank">📅 16:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92964">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة بفضل الله من استهداف مطار الملك خالد في الرياض بصاروخ باليستي ظهر اليوم وقد أصاب هدفه بنجاح وتسبب في حدوث أضرار وتعطيل الحركة الملاحية في المطار.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/92964" target="_blank">📅 16:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92963">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92963" target="_blank">📅 16:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92962">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/92962" target="_blank">📅 16:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92961">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6u_ntK-aX2D4luTByePDjyCmngiUBbmtndPNiWf-M0wUpJZgD7MH8CgVQIJ9VmAPBWtINScgDQUnKKys28Y0bSyplfmhNCMM_Ywz_-veDHkALpqupl53bAU3CAwC9UR7CjwcJtzuM6JOsnHRbddydR-puIheADNObEKhSHhNQN6eo0TPm3fVt9lKAHobM9gSm4iuBjiFfNRXI7VY7q7j22r9feujWbBm8O_inEEw40RTBfeTQM7Ry_-stLJe1EJDQ0s2VZaXYh_3MtUuXNr4l_y1Ag1AG9t6NzRrk7BSBPYeEq6dryhsXth2M1EcoOKuzKeZSGGOMmh6jX3GIA99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي  السعودية تزعم صد هجوم على الرياض</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/92961" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92960">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">#
ترفيهي
السعودية تزعم صد هجوم على الرياض</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/92960" target="_blank">📅 15:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92959">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9efb2a7c2.mp4?token=eUwJ9hdNIown3wsB4fHCXFEFqR-rI9G5x2J_UnA4WADxvs3lNNu7DT7yoC8tn8AtSdLUh59b1yYACfTjDHAkyUQFW11CCJmsMqPbq7iwYUKgXZaGJe_OC0qdHjtIHODZjcL-cOBM-pPgoPqlCXxiar4v8bn1EOk-gNdY65iqX2yYh_CzL7iVdt6fjELCtT81dj3I7qKuWNh9wB942MG53Gq9D5McngxeCRAUaQqtp3n-JxltVbX_ibXIsixg6WytuqchVGYVsuyDyDmN0r3NERxkJBEAvAxnRdON-1qhTV0aWSHzEZWBZrn7YQsFsEhxZo7dB71B4gnZTCsCAzcTDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9efb2a7c2.mp4?token=eUwJ9hdNIown3wsB4fHCXFEFqR-rI9G5x2J_UnA4WADxvs3lNNu7DT7yoC8tn8AtSdLUh59b1yYACfTjDHAkyUQFW11CCJmsMqPbq7iwYUKgXZaGJe_OC0qdHjtIHODZjcL-cOBM-pPgoPqlCXxiar4v8bn1EOk-gNdY65iqX2yYh_CzL7iVdt6fjELCtT81dj3I7qKuWNh9wB942MG53Gq9D5McngxeCRAUaQqtp3n-JxltVbX_ibXIsixg6WytuqchVGYVsuyDyDmN0r3NERxkJBEAvAxnRdON-1qhTV0aWSHzEZWBZrn7YQsFsEhxZo7dB71B4gnZTCsCAzcTDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تحرر جبل حبشي ومحيطه في تعز بالكامل</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92959" target="_blank">📅 15:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92958">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
🇾🇪
يحيى سريع:
القوات المسلحة اليمنية تحذر جميع الموظفين من الخبراء والمهندسين والعمال في جميع المنشآت النفطية السعودية من التواجد في الأماكن التي تمثل أهدافا لقواتنا حتى لا يعرضوا حياتهم للخطر سواء التي تم استهدافُها من قبل أو غيرها كما تجدد تحذيرها لشركات الملاحة الجوية في المجالات والمطارات والمسافرين والعاملين فيها التي تم الإعلان عنها سابقا.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92958" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92957">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c7b71acb.mp4?token=HlVRHUBFf0pMTcLvevXgJ6oeJTD2x_dYB9STJ8NZGnQWmz7-eSFzYjf5J95V2K1qekbmN6jbYFaF1RuLHa3gohH43YjJoN_JRFh4zq_QTaW4NYQdfJ-ftR4Dws7QJ45OfmqqF0FvJ2st46MWg61uWl440GT5MPCF7sIMbpXZj4MUbTON_WcU6hGEY6ZpLPzbM9WxtnzVoD8dWbLKmLL2MMEW06NZMbkqQ-r9oXUvUAWVvxVB4-cINP4KcSid4-cRuNGpxkZmcieSe6_36QUkNqb73KRQL37RVYVOVksD81-JM4Ze9XBF6D_okBkotqj6fX3vxtW2c9O_8u5l9NWsBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c7b71acb.mp4?token=HlVRHUBFf0pMTcLvevXgJ6oeJTD2x_dYB9STJ8NZGnQWmz7-eSFzYjf5J95V2K1qekbmN6jbYFaF1RuLHa3gohH43YjJoN_JRFh4zq_QTaW4NYQdfJ-ftR4Dws7QJ45OfmqqF0FvJ2st46MWg61uWl440GT5MPCF7sIMbpXZj4MUbTON_WcU6hGEY6ZpLPzbM9WxtnzVoD8dWbLKmLL2MMEW06NZMbkqQ-r9oXUvUAWVvxVB4-cINP4KcSid4-cRuNGpxkZmcieSe6_36QUkNqb73KRQL37RVYVOVksD81-JM4Ze9XBF6D_okBkotqj6fX3vxtW2c9O_8u5l9NWsBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة الهجوم اليمني على الرياض</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92957" target="_blank">📅 15:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92955">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40a3604bca.mp4?token=SLtTAkepSA-3lV9kxdcZaCZ9fcMnDwzxs356HBpThwvhvm1gTp1Nbm2bArob56Pk-HqK3jh7KuoehTbEBq-bQ_hQBOhxSDsECopu4H6M5urT2knR6cXJm6_OpmztWWx7mP76cdeQm1JwGmMTF3C5ZONH7ItLXcHDIy7CRRFTYt_ERO-6LiK6RPU2ZZvtRRwwGE5S9BJeJPDk_KUMARrOhMqQ96jZBqxFo0esT8KDnMeOdCHii39OQRA6xz1grn1ykSlEbR89FpPQKxTysYkJbk1Mtrdihcx9_scfYDwfqIrVcf-V4OsJh3xPU4iTgGm5ZrstxjQLP9lJeVcUdAKLHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40a3604bca.mp4?token=SLtTAkepSA-3lV9kxdcZaCZ9fcMnDwzxs356HBpThwvhvm1gTp1Nbm2bArob56Pk-HqK3jh7KuoehTbEBq-bQ_hQBOhxSDsECopu4H6M5urT2knR6cXJm6_OpmztWWx7mP76cdeQm1JwGmMTF3C5ZONH7ItLXcHDIy7CRRFTYt_ERO-6LiK6RPU2ZZvtRRwwGE5S9BJeJPDk_KUMARrOhMqQ96jZBqxFo0esT8KDnMeOdCHii39OQRA6xz1grn1ykSlEbR89FpPQKxTysYkJbk1Mtrdihcx9_scfYDwfqIrVcf-V4OsJh3xPU4iTgGm5ZrstxjQLP9lJeVcUdAKLHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
لحظة الهجوم اليمني: مقيمين هنود يشاهدون الصاروخ اليمني وهو يتجه لدك مطار ال سعود في الرياض.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/92955" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92954">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">لحظة دك مطار الرياض بصواريخ القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92954" target="_blank">📅 15:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92953">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201a76143b.mp4?token=l_-YnaC-63qmszzfKt_pcwvEJCMgh1R7p4vi36U33WgAeG2jouyv88gopMFgjswOv8bmHrVZlLILVsS-dl2ASdHcyThDFaVxVRINefAjzelUbNmOQXOiCljRD6ND7G0zHc24oW8k0uSUJMS2yI6LBFqZNMjOcCuTQHoGm-Z3IWJO_03Mg2fLe2jSKTPIIYj2BxJr6gOES8wXG59sUua3gGx0xBqQvgE4EgIS080-YYZ008vQKB5GNswYwBv2Ibpl4eGYkh0qg9KxompUUSc6wU-YTGCcqZtsu6ODOO4LvrIkhW1cwLgXEGAtJcXw5vLsPqq7_2u5qMF7Yub8vrNaWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201a76143b.mp4?token=l_-YnaC-63qmszzfKt_pcwvEJCMgh1R7p4vi36U33WgAeG2jouyv88gopMFgjswOv8bmHrVZlLILVsS-dl2ASdHcyThDFaVxVRINefAjzelUbNmOQXOiCljRD6ND7G0zHc24oW8k0uSUJMS2yI6LBFqZNMjOcCuTQHoGm-Z3IWJO_03Mg2fLe2jSKTPIIYj2BxJr6gOES8wXG59sUua3gGx0xBqQvgE4EgIS080-YYZ008vQKB5GNswYwBv2Ibpl4eGYkh0qg9KxompUUSc6wU-YTGCcqZtsu6ODOO4LvrIkhW1cwLgXEGAtJcXw5vLsPqq7_2u5qMF7Yub8vrNaWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطار الرياض يحترق بعد الهجوم اليماني</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/92953" target="_blank">📅 15:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92952">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9230f8f37d.mp4?token=HK3WvP8D_QlToR9MAuyEPBD5J0t6Tgv97QzKLRmeSKdOybar93jiMb2qBGCVAavAFnMsC2pFrRkU4ka1L_DJ432h82MMhry5MsbahJnMqGbGFFpritumCSljc465WbHZeer3ed1u2ZCvXS4udFS-biEsth0W5T1BwjSa5t5G7fY7bt6xkXwFwrgCvv-O52jKKnGCLzWZliujJ_oUOwawlBrqDzF7Jr8tHBjy25PASs9zmQ3HOexpv38diiSldtIMus_rtuu-sSlvKQ3a-LrNZubBrSrFWXADaprfW4aGQdNuXLVZCSYlaR_6Cb-ZgVDxPhKu-ovjFHAmi81Zb5_76Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9230f8f37d.mp4?token=HK3WvP8D_QlToR9MAuyEPBD5J0t6Tgv97QzKLRmeSKdOybar93jiMb2qBGCVAavAFnMsC2pFrRkU4ka1L_DJ432h82MMhry5MsbahJnMqGbGFFpritumCSljc465WbHZeer3ed1u2ZCvXS4udFS-biEsth0W5T1BwjSa5t5G7fY7bt6xkXwFwrgCvv-O52jKKnGCLzWZliujJ_oUOwawlBrqDzF7Jr8tHBjy25PASs9zmQ3HOexpv38diiSldtIMus_rtuu-sSlvKQ3a-LrNZubBrSrFWXADaprfW4aGQdNuXLVZCSYlaR_6Cb-ZgVDxPhKu-ovjFHAmi81Zb5_76Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مطار الرياض الدولي</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/92952" target="_blank">📅 15:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92951">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7009ef3ba7.mp4?token=OTa848wC5wpPpYtxy_r7TnT8xZp4NTnxG1QnikMYcSDMSRJk8kJXRZ0gX1AZjCkvdyp6fIMIyyxi67k74kKTKhV_HZ8pvvnF3UqpkM3qdRcYfKGR3o-ljMOjB3kyhHVJ9mjtVktKHu3yws6TVm2PxTr1cVbL0YHIjKWm6kRIC2e1Yg_Zerztr4SzjeG9b0oSpru3d3pknjfT7D7PNRu-3IGlLE5TR62zFhUKi411_-TCxviUc7Rzu3jThtgfWdgkG_Me9nIA9adQs4TbK-EG6ItluOlgTHA06RC8crPv1jeHd6Pd4kUp7GM7w6zZQLVmjj821uaAQ7XpUkJo4IkKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7009ef3ba7.mp4?token=OTa848wC5wpPpYtxy_r7TnT8xZp4NTnxG1QnikMYcSDMSRJk8kJXRZ0gX1AZjCkvdyp6fIMIyyxi67k74kKTKhV_HZ8pvvnF3UqpkM3qdRcYfKGR3o-ljMOjB3kyhHVJ9mjtVktKHu3yws6TVm2PxTr1cVbL0YHIjKWm6kRIC2e1Yg_Zerztr4SzjeG9b0oSpru3d3pknjfT7D7PNRu-3IGlLE5TR62zFhUKi411_-TCxviUc7Rzu3jThtgfWdgkG_Me9nIA9adQs4TbK-EG6ItluOlgTHA06RC8crPv1jeHd6Pd4kUp7GM7w6zZQLVmjj821uaAQ7XpUkJo4IkKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطار الرياض يحترق</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/92951" target="_blank">📅 15:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92950">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تصاعد اعمدة الدخان من الرياض</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/92950" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92949">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/92949" target="_blank">📅 15:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92948">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4d22faab.mp4?token=eGuWnDBKJ3HIz4dfiRhdBkcHQxrDajFRcPpbS2p6CLFK-JuHzYQimYBUctK-PyGiYZDW_rf7IHrG4kw1qJ8CnQAJ_2BO9T4m_oTNPPyt5gC3Llm68u__cACM80sXJzwxRfpkIoSMZwh43KInEniiCfhFmsTpQItvA432xictILGYmsOSJpIUuavZZOAyvrCVmEcoG6UO26ieAioFh2SgBHCfbcDkWrcRSjMCfzbT2UM_gJeB6w8zGpY8GGTpEbdgsJx6OVRFD_hhLL1aqmRN3q9Xzhvoekzjl_f-4UemLMMaUa9jXvUT01_KAUR3dN5atVaPBuYyrbJihNZgvi8fRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4d22faab.mp4?token=eGuWnDBKJ3HIz4dfiRhdBkcHQxrDajFRcPpbS2p6CLFK-JuHzYQimYBUctK-PyGiYZDW_rf7IHrG4kw1qJ8CnQAJ_2BO9T4m_oTNPPyt5gC3Llm68u__cACM80sXJzwxRfpkIoSMZwh43KInEniiCfhFmsTpQItvA432xictILGYmsOSJpIUuavZZOAyvrCVmEcoG6UO26ieAioFh2SgBHCfbcDkWrcRSjMCfzbT2UM_gJeB6w8zGpY8GGTpEbdgsJx6OVRFD_hhLL1aqmRN3q9Xzhvoekzjl_f-4UemLMMaUa9jXvUT01_KAUR3dN5atVaPBuYyrbJihNZgvi8fRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92948" target="_blank">📅 15:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92947">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/92947" target="_blank">📅 15:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92946">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">محافظ البنك المركزي العراقي:
سعر الصرف الجديد ثابت ولا يمكن تغييره أبداً</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92946" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92945">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله اكبر
انفجارات عنيفة تهز الرياض الان</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/92945" target="_blank">📅 15:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92944">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmTOocpgn039bJwvmkYdgFZSKrs2nj6HoWMVxAsYPdDcZHerPedgWXb-_vh7iz0T2yem9tswmkNvTLQPYDDw_8qUdeha8cDWlYBsMFkxBzte9qOfhazbteFfUoDGz35q-wfOXb5tA4Plu5GkKLH102k0xIkR2I8PsxcyZ9tsbYaGza5jfVH9AGQdo7LpBbvOjJ-fzUtHEjl3XdWcGoI7JLAQnJ8DTKMwsZTN7axf5nlXJr2sDv46tWZmwASh9jPK5UouSw5czIcRqB7ybYhx7SwTGDsGKLH4CjD-FJEiSrFZP8r18Kmluznn-lpRI0KylMk_oIK_esJB9hIRXNIlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدوان سعودي يطال مطار الحديدة اليمني</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92944" target="_blank">📅 14:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92943">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a46942fb8.mp4?token=AR80KJPP6mKza2l_a74xxSvtNEzphaDWATbFa8bL2r-DzrKuCIQcCqL94ZWYN9Jm1rxpQSXiUOL6d4OFHwAnTnjyYcYCQyXT4EyzEQ5uoF-X1_b9PTuloQTyNfGHGz6rNp31m0IQTYxbhjnk8_-P1kjPX3kfsguuzSgyuFxEmSuOpr7J7DT8_aqZq6nDFruNfHI4KcaIFhjUhEMSLmMrOIEeGBdH7iVd17G4leF78KZzEXASHMEXm_NmmexpWpoEgEhx8_U79i59g-Sy3hedb9LsloJSMycejR20ZX1i4xl5eDWUhMaT0FByZ2YoG03a0aaVDiIvOW-GDTrhxc9vKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a46942fb8.mp4?token=AR80KJPP6mKza2l_a74xxSvtNEzphaDWATbFa8bL2r-DzrKuCIQcCqL94ZWYN9Jm1rxpQSXiUOL6d4OFHwAnTnjyYcYCQyXT4EyzEQ5uoF-X1_b9PTuloQTyNfGHGz6rNp31m0IQTYxbhjnk8_-P1kjPX3kfsguuzSgyuFxEmSuOpr7J7DT8_aqZq6nDFruNfHI4KcaIFhjUhEMSLmMrOIEeGBdH7iVd17G4leF78KZzEXASHMEXm_NmmexpWpoEgEhx8_U79i59g-Sy3hedb9LsloJSMycejR20ZX1i4xl5eDWUhMaT0FByZ2YoG03a0aaVDiIvOW-GDTrhxc9vKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران العدو السعودي يستهدف منازل المواطنين في مدينة اليريم اليمنية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92943" target="_blank">📅 14:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92942">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عدوان سعودي يطال مطار الحديدة اليمني</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/92942" target="_blank">📅 14:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92941">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">﴿كَمْ مِنْ فِئَةٍ قَلِيلَةٍ غَلَبَتْ فِئَةً كَثِيرَةً بِإِذْنِ اللَّهِ وَاللَّهُ مَعَ الصَّابِرِينَ﴾
🔻
معكم امريكا وبريطانيا وباكستان و تركيا واليونان وإيطاليا وألمانيا وفرنسا
🇾🇪
ومعنا الله و بندقية ابو الفضل طومر و الشعب اليمني و الأحرار في العالم .</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92941" target="_blank">📅 14:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92940">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/92940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92940" target="_blank">📅 14:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92939">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇸🇦
🔻
مصدر محلي لنايا   اكثر من ١٠ انفجارات تهز العاصمة السعودية الرياض نتيجة هجمات أنصار الله في اليمن ..</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92939" target="_blank">📅 14:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92938">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الله اكبر   انفجارات تهز الرياض مجددا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92938" target="_blank">📅 14:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92937">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الله اكبر
انفجارات تهز الرياض مجددا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92937" target="_blank">📅 14:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92936">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">طيران العدو السعودي يستهدف منازل المواطنين في مدينة اليريم اليمنية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92936" target="_blank">📅 14:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92935">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
مستشار ومساعد قائد الثورة والجمهورية في إيران محمد مخبر: لن يُفتح مضيق هرمز بأي حال من الأحوال حتى تُحل مشكلات البلاد.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92935" target="_blank">📅 13:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92934">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a207cb54.mp4?token=Aa1PYvnaA_cbWW5-UsiEjt1-HQ1o62eLlc2wLagHfrOEFb2TPVXycOfm7VonOF7tQk7QzI1AM_VY1x9LHJorFNauuJTl7Y2eVpvBKmotr1b0DOFTyPV7qr-pzecsfZWyDHk0TuUvzK4q9BQeKUBDShno7i-exMC_96mC4WC2a7ObazJicYJUXDCbyKTOoWidIDuyRURV-pV1VYh0UkOBru-Yw8wIQNnmq0FO47TvKFR1t-Yr2fgVp7vR5anLQBs_aJVQBYdqtpEeITi3KDOTWf3x40IkaD9QgN2vsNt7N1X6ckf7YIOixKF7ep4BVdoEaAspRbDoqWCmYz1dAh3a-Kqz1rYLCrCM1R-fsULG-VRS_s_RwUsOg0xAo16cY5NVHDrA-QGaMA7h9l55_nP30CB1ZkP59qfc_Bhv8T-hkrVROuZ58S0dgjZSCIKn71tyfmOVSZ_hWpufG0Lhej6AOSFicnEXBTwL8Aiz7xSTO_nlT6qiVmbec-oUUncDWqLOOyUfGzQzbIxcfXLlGVFKLxNpIGEUghyBG9ymMrdOOfWK7UvBmYRLUW4LmS8gOvp3o0dJ9hC9Bd4tsP6elB1HnWEDY_5ITotyYP386E8p-7iOUbURhsjWT3eiTPDZTkhOyntPE4Xc46A2nr8Iav1y7LqP72CPdv7Uxoahx6-C_sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a207cb54.mp4?token=Aa1PYvnaA_cbWW5-UsiEjt1-HQ1o62eLlc2wLagHfrOEFb2TPVXycOfm7VonOF7tQk7QzI1AM_VY1x9LHJorFNauuJTl7Y2eVpvBKmotr1b0DOFTyPV7qr-pzecsfZWyDHk0TuUvzK4q9BQeKUBDShno7i-exMC_96mC4WC2a7ObazJicYJUXDCbyKTOoWidIDuyRURV-pV1VYh0UkOBru-Yw8wIQNnmq0FO47TvKFR1t-Yr2fgVp7vR5anLQBs_aJVQBYdqtpEeITi3KDOTWf3x40IkaD9QgN2vsNt7N1X6ckf7YIOixKF7ep4BVdoEaAspRbDoqWCmYz1dAh3a-Kqz1rYLCrCM1R-fsULG-VRS_s_RwUsOg0xAo16cY5NVHDrA-QGaMA7h9l55_nP30CB1ZkP59qfc_Bhv8T-hkrVROuZ58S0dgjZSCIKn71tyfmOVSZ_hWpufG0Lhej6AOSFicnEXBTwL8Aiz7xSTO_nlT6qiVmbec-oUUncDWqLOOyUfGzQzbIxcfXLlGVFKLxNpIGEUghyBG9ymMrdOOfWK7UvBmYRLUW4LmS8gOvp3o0dJ9hC9Bd4tsP6elB1HnWEDY_5ITotyYP386E8p-7iOUbURhsjWT3eiTPDZTkhOyntPE4Xc46A2nr8Iav1y7LqP72CPdv7Uxoahx6-C_sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇷🇺
إنفجارات ضخمة تهز العاصمة الأوكرانية كييف عقب هجوم روسي بالطائرات المسيرة الإنقضاضية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92934" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92933">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔻
‏
مجلة ألمانية:
إيران تضع قواعد عسكرية أميركية في ألمانيا ضمن دائرة الاستهداف.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92933" target="_blank">📅 13:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92932">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f51255457.mp4?token=idmwX3d9nrJk2SDft81en5i_zw_O0O7FZ7hw9TWZgEySco3vswWvrLnA2nDu2QJudSRlk3KXef747ANHxY8szV4bLoEtXl_RAN1z8krg7ZMREAkkjHi4l_isNSWq5oesOWQG3pm_OJ4hsqbXqZ3VUkCKx6mM21Q86BZ70MgQpHR43oAyPB3Iwc2jdwo7sTtUP8s9GguHWN7hRKRT1X8vP5ZLEmht1mfhU_ZjJBz52_-FhabIEi9uSh82-H3DNWMXC8-D6M7HP2WEWOUtgo7zGNwBXfWf4Eq59fFcBGPxnrOPu-2ZpacabOCRbzqpp2YiTOc9p9ywnOZW7BsbNZnrOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f51255457.mp4?token=idmwX3d9nrJk2SDft81en5i_zw_O0O7FZ7hw9TWZgEySco3vswWvrLnA2nDu2QJudSRlk3KXef747ANHxY8szV4bLoEtXl_RAN1z8krg7ZMREAkkjHi4l_isNSWq5oesOWQG3pm_OJ4hsqbXqZ3VUkCKx6mM21Q86BZ70MgQpHR43oAyPB3Iwc2jdwo7sTtUP8s9GguHWN7hRKRT1X8vP5ZLEmht1mfhU_ZjJBz52_-FhabIEi9uSh82-H3DNWMXC8-D6M7HP2WEWOUtgo7zGNwBXfWf4Eq59fFcBGPxnrOPu-2ZpacabOCRbzqpp2YiTOc9p9ywnOZW7BsbNZnrOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇬🇧
خارجية الكيان الصهيوني: القنصل العام البريطاني و20 دبلوماسيا سيغادرون إسرائيل.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92932" target="_blank">📅 13:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92931">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇹🇷
🇸🇦
وزارة الدفاع التركية: تمت مناقشة نشر قوات عسكرية بالسعودية في الاجتماع الأخير الذي انعقد في إطار اتفاقية مكة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92931" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92930">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇸🇦
🔻
🇾🇪
مصدر لنايا: تصاعد أعمدة الدخان في عدة مواقع بالعاصمة السعودية الرياض عقب هجوم صاروخي يمني.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92930" target="_blank">📅 13:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92929">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇹🇷
🇸🇦
وزارة الدفاع التركية:
تمت مناقشة نشر قوات عسكرية بالسعودية في الاجتماع الأخير الذي انعقد في إطار اتفاقية مكة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92929" target="_blank">📅 12:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92928">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
تحديث.. استشهاد أحد عناصر الشرطة الإيرانية نتيجة هجوم إرهابي في مدينة زاهدان.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92928" target="_blank">📅 12:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92927">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sErurScVcFDjpXTNlM9UMtHS1AMch0FrsRmCH0PRCXFYJ7vWai1te2rjWcYOO4fie9PVA0N8GI5IscDaqS9COq2fgpiGp8HxualT4t9DgnRocPCWiWedYzNyCKfcrAxmboIP3J_azgevHYZuelrh1yOLjknJbHwDyx-9MkvijUv2hN7MehTfDNSJ_wOtN5ys16GqCegYNZsydXmJLLIDIbFtr40ytfG-rpIWjr-WO8Y4quFO-ZUmNIxvjd7QVyr3fT7H_4dF-t9km_KqF6cwlLr83nZhGrJ2LdQk_RxiSaQYPhdfB5YTzV4AmsyRf0phRSkj5sNkIkbl4YvPYKNp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عقب هجوم إرهابي على عجلة تابعة للشرطة.. إندلاع إشتباكات بين القوات الامنية الإيرانية وعناصر إرهابية في مدينة زاهدان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92927" target="_blank">📅 11:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92926">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c636dd07.mp4?token=tVSxAUtQ-HK62LcAcCzJO_oFQ8R5bJWsp3aco9Y_4_230bJgeagcOjQV6e_C3BTGIINZD_VeacUo7C9-Y0BnAurxPysJMAfQtZkhxImnRP8epyQL_uVF8S7IdbLjsO2HY0RmKoJreC9dtrnffEBnbgkj_7jd2cTneJNvDDBN7MqbVxiiSW54MFDUr563k8T-S0C1nn1UhN_XZmqioJ45ZLUBI39xi3mkmf-paX_3hpW1F7sOJNoiGOvjkofaeZcXwB2iaPv_R6Lj_JXTtToDLarD514bx67EqiYA-bksJ690Ypu0SCa6V41irsXC0a7dU5QPAYNgGVI_eTJ0mHYK4XDVoaEMMT21OkPodvcONKlnmgcOhoQ6-szbK_eLb1V-9juGEJjx78Hbz-tMwNgNPxw8gEOWxTD-hD4m3WR_FJC42yCDDTzNPSWSPm7IfjeMhAQMBLw4djnfEoEL3OBvz5DppWr_g9-eJLIdjwpl4W8KkgHvSmsTCGjt0E68bc9nzL6iCkj9SsxGqwvyHTwEsFquPYjpLy6GNpLzMzPOehjwxumUC1m3_lXRN9mVUi-NtdfuwtK_RUgbLQA5kLHVHKHyQtM-2yJq6qlByYZGVgT4dhT-n8oEM67NyGNVuFvUk-DTkFamLehITylHMg2EeetkrluyngK4piykqkdHB9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c636dd07.mp4?token=tVSxAUtQ-HK62LcAcCzJO_oFQ8R5bJWsp3aco9Y_4_230bJgeagcOjQV6e_C3BTGIINZD_VeacUo7C9-Y0BnAurxPysJMAfQtZkhxImnRP8epyQL_uVF8S7IdbLjsO2HY0RmKoJreC9dtrnffEBnbgkj_7jd2cTneJNvDDBN7MqbVxiiSW54MFDUr563k8T-S0C1nn1UhN_XZmqioJ45ZLUBI39xi3mkmf-paX_3hpW1F7sOJNoiGOvjkofaeZcXwB2iaPv_R6Lj_JXTtToDLarD514bx67EqiYA-bksJ690Ypu0SCa6V41irsXC0a7dU5QPAYNgGVI_eTJ0mHYK4XDVoaEMMT21OkPodvcONKlnmgcOhoQ6-szbK_eLb1V-9juGEJjx78Hbz-tMwNgNPxw8gEOWxTD-hD4m3WR_FJC42yCDDTzNPSWSPm7IfjeMhAQMBLw4djnfEoEL3OBvz5DppWr_g9-eJLIdjwpl4W8KkgHvSmsTCGjt0E68bc9nzL6iCkj9SsxGqwvyHTwEsFquPYjpLy6GNpLzMzPOehjwxumUC1m3_lXRN9mVUi-NtdfuwtK_RUgbLQA5kLHVHKHyQtM-2yJq6qlByYZGVgT4dhT-n8oEM67NyGNVuFvUk-DTkFamLehITylHMg2EeetkrluyngK4piykqkdHB9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
صاحب محل جملة يروي أثار تغيير سعر الدولار وإرتفاع حاد لأغلب البضائع في الأسواق العراقية!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92926" target="_blank">📅 11:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92925">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇸🇦
إنفجارات تهز العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92925" target="_blank">📅 11:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92924">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
إعلام العدو:
اصابة 6 جنود في حادثة بقادة عسكرية وسط البلاد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92924" target="_blank">📅 11:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92923">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عبر بوت نايا
🔻
إلى وزير التربية العراقي عبد الكريم عبطان..
بعض مشرفي وزارة التربية على مدارس الرصافة الثانية ومهم المدعو (لؤي العبيدي) شخص يتعامل بأسلوب طائفي مع مديري المدارس وبشهادة الشهود من المعلمات.
احنا بزمن غادرنا مسألة الطائفية المقيتة فلا تخلونا نرجع لمربع تافه محد من العراقيين يريده.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92923" target="_blank">📅 10:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92922">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNuPG61lUT6WaawBFzndKfhSOSh9e_363gaHS5IHkVb1yVWRHr08Kl0vQdQqJMq46JtG4roxAkyQxZYrXkm9rIKo7yAYw4nGaqX8t4nB3qlTV2jCcnhWVC1fUz-rXHScIGUDruY8ooEhVGu850q739DE1ObBWKja8PZU0YQiVO1XT4gdWlXApUK-UgdpMHugG1lBltz-ZPr_FMuQqeCEWgwAQNgzrRApfnPFvCzIvtEwkdZx5e9g2qFYImk42D7zAhfP0XiDw_sYEHYmxNS7ct6SKyoNKU4GOZV91gQ6Knqmt4YcPD7-T2QyTuBfT7rFjj8otn3VYTePB2Tc_MV24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد زيادة وتيرة ضرب ناقلات النفط في مضيق هرمز.. أسعار النفط العالمية ترتفع إلى 103 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92922" target="_blank">📅 10:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92921">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
عقب هجوم إرهابي على عجلة تابعة للشرطة..
إندلاع إشتباكات بين القوات الامنية الإيرانية وعناصر إرهابية في مدينة زاهدان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92921" target="_blank">📅 10:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92920">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np5V0LxyczwxNOUy-R7WBPuboCKYBWwqKHLFm3eRxXCPZGyZjZVSVhkcSESa6HpR1_5uHuiPvTfsVtyLhH6bWdnBoGh3gmvgtyOziwS1Hn6uSY57hZ9SGT_rhicmf3YG1dXhKMIF1L5UQxLQTs6UITVtNqnIbBRLcRntDxbtlchHyPjJgUJNT_R-XZtX90P_LhcXL78lmNhIYACSHtZa9IAxPAO0O2TVoo1qOjhmD77bh9ZeYAGvDleNXEem22G4iv_PGRm-zRvcspR_GY-_lOJA-u_2K1hqZPYzTf77pQVe4xTxg0l5DevbIsKvbNj2bhBgnol3SwbLhLjv-XARaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
إنفجارات تهز العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92920" target="_blank">📅 10:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92919">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇸🇦
إنفجارات تهز العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92919" target="_blank">📅 10:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92918">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvJ-FE_b9N3BtNC9bfV7U03ZYRwaJT3f-_EI_YWu57pvf-SVGshPuAfjm94QQF0Fmtc76WfCivaFuLH8te5OKflnRSMnBDkXTlrd82YNJvmhN8LfMXEBY0z4JQdlOQ2SIGQqtlF4nLTTgP8mztVaF4cIQLjxavVZ6WQhwJXouFXE4fzxlLOEMdkVb97oi5C2F7dJwQAFmbdleTNyX7225yp0P4JGn50w6J3pyEPcqfUlK1KRQVYaccU-gMVMVCnv8hfM31LSg7NhjSZxv6QV0RS_JqKEUvgtlnq9BO_R2dU0Et4ajDQ1CDiohITYXECU6_Lk8hSuwGifh65aCbhnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
🇷🇺
إنفجارات ضخمة تهز العاصمة الأوكرانية كييف عقب هجوم روسي بالطائرات المسيرة الإنقضاضية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92918" target="_blank">📅 09:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92917">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BflvCrriKSrkSEBPoV__2n3uFLx_n741kdXye_As6M8zAdglGzR_JF3wmTWZSnaevca5CXfX9gAUMYRnphgMyn6gQQ1yrKGrN86lQd9qzCBLHuzF_NWiS-c55-YMztcdUXncM_WIWmi2_ooXnkuGk-Z3GzkEfWgRIIBxQh_4HohXx__h_fowitf1X45xVrfOedPR-Z02aLyg06a5hPaSlBWtBavLEGraqxXxvufJf98Td5ZtsmT5d_Z-M4uSJ8osM650_SMeKM7cl4rJLN0ubbZ_FzX3zAh7H7OgB9_qzz8OyvBZUuvmWH9BNpqdjMJ3NVqlrVPqZCHk-jmyC7JvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد زيادة وتيرة ضرب ناقلات النفط في مضيق هرمز..
أسعار النفط العالمية ترتفع إلى 103 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92917" target="_blank">📅 09:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92916">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
صاحب محل جملة يروي أثار تغيير سعر الدولار وإرتفاع حاد لأغلب البضائع في الأسواق العراقية!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92916" target="_blank">📅 09:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92915">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇱
🇬🇧
خارجية الكيان الصهيوني:
القنصل العام البريطاني و20 دبلوماسيا سيغادرون إسرائيل.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92915" target="_blank">📅 09:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92914">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇸🇦
🇾🇪
رشقة صاروخية ثقيلة اتجاه السعودية الان من اليمن.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/92914" target="_blank">📅 03:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92913">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70b5a5cadf.mp4?token=qozt1yqE30dUTMP8gGbYG-XhDXiwjKS5DxzV3e2Vh2OfQwTscm6HxeVHq72sq5Sl-dXSzKoy5-BOB6pqQSS83_iXh5u6oRR1ktenmDKfXuwfgzvGOvJzMEo6eXl6kUrysGpcpkFJ289QkYcbcWM1petuC9E13MDaD4wNwo7RLKjFCXw0H--afqqoOi5ZKEplp4VerpImr-OT6jTPe65qOqNXJ4u_0RJ7V_GQrWCBx4lxltxLNPkWq17l4WKPuUlBqMbjaT3oVLOOZ9TkxzFtvt1Vgqs012NgKPy9hEztnOjjk8DmAPVnuN6bcnRasp7TiKxzPojBe60oiajw5kX00w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70b5a5cadf.mp4?token=qozt1yqE30dUTMP8gGbYG-XhDXiwjKS5DxzV3e2Vh2OfQwTscm6HxeVHq72sq5Sl-dXSzKoy5-BOB6pqQSS83_iXh5u6oRR1ktenmDKfXuwfgzvGOvJzMEo6eXl6kUrysGpcpkFJ289QkYcbcWM1petuC9E13MDaD4wNwo7RLKjFCXw0H--afqqoOi5ZKEplp4VerpImr-OT6jTPe65qOqNXJ4u_0RJ7V_GQrWCBx4lxltxLNPkWq17l4WKPuUlBqMbjaT3oVLOOZ9TkxzFtvt1Vgqs012NgKPy9hEztnOjjk8DmAPVnuN6bcnRasp7TiKxzPojBe60oiajw5kX00w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بعد إعتراضه على سياسات ترامب احد المحتجين يتعرض للاعتداء من قبل مؤيدي الرئيس الامريكي خلال كلمته</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/92913" target="_blank">📅 02:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92912">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1712337481.mp4?token=kTH7nJjBqHB7FXFy27K2KB7hsI9Tz2jWlTrp4pcXLSjlQkaPwPbJxNos1mxz6QIReTylNP95ZSJIG8gdDDwDSEXX2HOg4LVPek43MWp9m0-sYYd9xaoVTzgJnPcRRgjU-lSENtqso3je6OqidirVcQssGQ_N6igsrdtKuaf37cI5K2dBriLM2m5yViYViYpbOCzIn5iLL2FpyI07Vp4WfhVLMe9_Ez-o9ezy8sG0VOE6nDH9pVM-kTCMc1zQ1D2mTCxhnm0wjTeCBMhDv7lF0GmHgBRHDAUYE9DYsn0NNLQyUyrzOSqomqRACzXgJfmsZZELI-X8HUsgd_KQ8OtMMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1712337481.mp4?token=kTH7nJjBqHB7FXFy27K2KB7hsI9Tz2jWlTrp4pcXLSjlQkaPwPbJxNos1mxz6QIReTylNP95ZSJIG8gdDDwDSEXX2HOg4LVPek43MWp9m0-sYYd9xaoVTzgJnPcRRgjU-lSENtqso3je6OqidirVcQssGQ_N6igsrdtKuaf37cI5K2dBriLM2m5yViYViYpbOCzIn5iLL2FpyI07Vp4WfhVLMe9_Ez-o9ezy8sG0VOE6nDH9pVM-kTCMc1zQ1D2mTCxhnm0wjTeCBMhDv7lF0GmHgBRHDAUYE9DYsn0NNLQyUyrzOSqomqRACzXgJfmsZZELI-X8HUsgd_KQ8OtMMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بعد إعتراضه على سياسات ترامب احد المحتجين يتعرض للاعتداء من قبل مؤيدي الرئيس الامريكي خلال كلمته</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/92912" target="_blank">📅 02:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92911">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇸
اعلام اجنبي
: البنتاغون أمر القيادة المركزية بالاستعداد لاستئناف الضربات ضد إيران</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92911" target="_blank">📅 02:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92910">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تجمع عظامة العراق يقيم وقفة استنكارية في ساحة التحرير وسط العاصمة العراقية بغداد احتجاجا على رفع سعر صرف الدولار مما ادى الى ارتفاع اسعار اللحوم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/92910" target="_blank">📅 01:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92909">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTLTexDJAuPpx0joYlcz3WpL4gy6aqWrdYxztt7LSpO9O9tWM6ZkBV1101QlDkm8tw-jK2zlNf9lmTjl5NdCbV9udC0PYopv2WdY_gFbbpZAuOcShvtQWlwAtzJEQ_eNnHCla58C9VNn-tv2C-j-7ILvXk71qTfHqLpFFX5GFHD_PtK2vQHS32kkITcuX1aOaPVyhF38d3FHoEh0Wk4-vnFnFM8rCenbnj0hPc4BFaW4_eJJBE0ZGJlAoWf6Avre2SINYuoC7w8lq-bPUBSgzL8TCH_aaRWSiG9je7aEJjSsO6fVNLBOPMihNIwcdGEB1EYWs5XD1710PqzeSbMiow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:لن ننسَ يوم 7 أكتوبر أبدًا. ولن ننسَ الضحايا أبدًا. وسنظل دائمًا في مواجهة قوى الإرهاب والشر.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/92909" target="_blank">📅 00:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92905">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUdabG1pq6fLXLCYCdNJPXeD03p_ckxpuo9E2c11vAcweIyMy07O0YrYbUOZiCLkHThpouaXx9P1uSFWJ_LTASFmaKFW7JJG8rEypA4_Ifx5VLYN96lPhzSp60A9bGHreHsYxj2Jf8kPJ3wMVC2jfmL7YeEw7o3M7A7ntgP6sOkVXs20_ZZMu8uqan4ZON_PbsVQC1B8oU0Z9iZsh8M-WJF6jUvAQYnXZAkymo6C2yOgWf72_-iTw3NVHhgIQOC5Nf3IJzs_jOOY6WDCD3Yc4_B4bFVOXay3GWM1b-jbOfTprjIzJoHpNztUJEyuq2Wv3CpEpbqT2SDI7JR06eVbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpMjrlXPU_YAFGRvYzzWSGyeOfJ4x2hCjkiniaeV238BQtwxgfNMx3DGxNxhf9rHiYRG5ST9k9H4CT18RyCRvEAjI9yELaIwH2CVei3KqxrCs_0P83bO5CT8uAsQ5UgQQIS9maVIZr6igGUDRyyR4tL2glGNuVkfXBjpEZCOrdQL9Jti-hnjHz_sBkus4M5YlxCzpA4aVntQWW_c7X4-y01bj8HJ_-APsNBJs2LUzo_FSQvn-r9q89469pTjwJpFgjb37cxhpYd8-hcI8B0Rbof3S_CKOfeFE9nABeKjx7ZwAroUTUWQSHf8xdMMGTpxi0stdJcFkU7eMBzqKWb2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMxykF5LPnbM-5xhb_lqy_VioT_Y3h-sTs7AndQtYyEypWFPX8hlw95mwfBLb3HPUxj1H6USEEy-N6jMndr5yyLI0UojjYdIisYX7uik_8jd219dVg_le5rT1hpzhG2QVApPTRERzdbB6cm8kwXHzZ6ly66A2vBRNaShvIyT506JMI4X21ufDRVnxJ5YYLbE1MoO4oVAYZPl0LwDyf3TVT5wPR8JNEi3FRA1IRCaOWQpnVhuMIJZxTK9sGq5q3IJVyQnh-2i8SzeIdp50jdkvPpw_b6N84xda_r05MwXGdZzEqU7q7LhYnDL_HiPr3jl8taojkhqoQfh0YjRSmeIXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeffef5d6f.mp4?token=OkAoF_v5r6vVcI8pfst4LlEI0mzE9Qe1vivLF-2Gf3XpNQV42_M6OHe6maOiWqdgTLBS32wAfTne6oV9eXDEV40XoSN-WafL0T2La4Onm48D-ropCmRTEa-t5bDvKZxymRF7K-ILKnpYz6iLvDcKG13GZbJYV6lqoFdPiS8nD0G_DtnVYLB37Ujvhl0CnSgyh40BeUeIncBY5SGY-X1tQmS1TV-uKVbjxvlJyPp23wy_2sxgi5J3KRoO0CFFquYqOmMZbiXISP2eQwBuHY5HiOWr_PgNN90oFQaIeGp3MfEzGQ8tQxZxMxbJqEJlC9qvMDbjDPld5INW5VaWwDAAAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeffef5d6f.mp4?token=OkAoF_v5r6vVcI8pfst4LlEI0mzE9Qe1vivLF-2Gf3XpNQV42_M6OHe6maOiWqdgTLBS32wAfTne6oV9eXDEV40XoSN-WafL0T2La4Onm48D-ropCmRTEa-t5bDvKZxymRF7K-ILKnpYz6iLvDcKG13GZbJYV6lqoFdPiS8nD0G_DtnVYLB37Ujvhl0CnSgyh40BeUeIncBY5SGY-X1tQmS1TV-uKVbjxvlJyPp23wy_2sxgi5J3KRoO0CFFquYqOmMZbiXISP2eQwBuHY5HiOWr_PgNN90oFQaIeGp3MfEzGQ8tQxZxMxbJqEJlC9qvMDbjDPld5INW5VaWwDAAAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🫡
مظاهرات جماهيرية واسعة في محافظة واسط العراقية تستذكر يوم العبور 7 اكتوبر وتقوم بحرق أعلام امريكا والكيان الصهيوني .</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/92905" target="_blank">📅 23:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCjCslxmMhkvouObe6EkBxzbS1a235M7vbyXv1OocVJCivogGLuvc1-Ul8xPaoeKuoNdVJ8yeJUaKsBHtWCjyAC3WIWkIueAFri2PyaQvhY1M43ye_3CuPkJew1UK5JW8uDergs-KI1-9QjD3liIcLFV7BNikaKh_QsyT2AFEpkp_sMO6FC60JS-Jq76elrdxgLt5KzAR3GcQQJK7vpSMOgq2CfDanrMTfDrqY5jY382qLgFobjKWdu86JyhiBpB0T-ww0TixVFwOg9bGGd9OJ_raXbLPL2pbsS77t18FKS4fvgXUXdmloYgQ6vCCszGBlJLxt4_yJ7mCGt5ZkJWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سماع دوي انفجارات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/92903" target="_blank">📅 23:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92901">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IdIdZsO4qwmxsD8aLsWuy4QVmFvpslCHnkcxogo8syBZHL3z8SjM8PAVCrbgUnMHP0WnqoIGc9q-OecmnAn2X7xevPPg2ctW1obKHdCKodIelwj2Bt_Uc_gIlOSNo5NiMlTTxjetkVv6kbFWMUJ9xbuNesCv1LvXJ524RIL73vZRbEc0BoVUH-Itdk0Ry7uYZ5Su-l8GfEYkHbDXgL2IqDMBJeKpYWOAtjZefGunzRiIONeusMXtBTnFRms6HyUDCBvUTBS3oRfhs9ZjO8pifiKKyCGdO79DTHoA7g0PO_Xso1z5KVJI-qa3zMeyiXUUoQ1orBbFHeSGGo5oL4KSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GL2GPLEwPvsi-dPh6LI5tkx2RVneGyyTeKW_t6hfGYOeFUjWDFo-NZhoXRudoV9gFd2Q0ScYAejy1wUfFG8e0daV4sBKoWu2wRp2RrPZX7qdL5XnGqTDWpIHSnEkg4rmnC001fE2wEcMLvxh6SYrZiL_S-ESX2lbewaGxLqfdicFTKc74pQBWBJiBZ5V_7aTep_ZkukmAhelCz9kPuiggxIH0bruTtEAFRvzijKPyp7EnEKunpgsvX76qYzIBZ53liI8zCe8OFGFhV87ODnqyCVRSCKeWlap_E07DR4Vs9EBjTALkqdEZu2fBXoBdVKsLfD2PqZoJEfa-L0wPRspGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
اهالي محافظة النجف ينتفضون ضد قرار سعر الصرف الجديد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/92901" target="_blank">📅 23:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92900">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇸🇦
🇾🇪
تعليق الدراسة في جازان غدًا الخميس خوفا من الهجمات اليمنية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92900" target="_blank">📅 22:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92899">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
خدمة أبحاث الكونغرس:
فقدت أو تضررت 81 طائرة عسكرية أمريكية في عملية "الغضب الملحمي".</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92899" target="_blank">📅 22:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92898">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
سماع دوي انفجارات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92898" target="_blank">📅 22:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92897">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇨🇳
تعرضت سفينة الحاويات الصينية لهجوم بمقذوف حربي في البحر الاحمر.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/92897" target="_blank">📅 22:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92896">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
🇪🇬
القوات الامنية العراقية
تلقي القبض على الاعلامية المصرية (مها سراج) بسبب مخالفتها النشر ومخالفتها الاقامة وتحريضها على الاقتتال الداخلي.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/92896" target="_blank">📅 21:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇾🇪
مشاهد لطرد التحشيدات التابعة للعدو السعودي من مديريتي المعافر والمواسط بمحافظة تعز - 7 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/92895" target="_blank">📅 21:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇸🇦
🇾🇪
الطيران السعودي: وفاة شخصين في مطار أبها وإصابة 28 آخرين جراء القصف اليمني.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92894" target="_blank">📅 21:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92893">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇸🇦
🇾🇪
الطيران السعودي:
وفاة شخصين في مطار أبها وإصابة 28 آخرين جراء القصف اليمني.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92893" target="_blank">📅 21:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92892">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhP5k4rERMiMsv0xtxve2gRk7WH5m-lWMN0klH_9X_p5Hz4RWti7iNVAl4MO5DRKKO-FWCZeDBIsiWoFMmQIC9VexKjR5zmk1rs1aURYUM03f25ZJq3SYfkbfSxUbrsD4mPG5aG4f3EiMJZrZwx8-7UsOAr589n9fVTm-ttJG_JympEw9xpkuKtyKlGYZogap_1tbuE0V4gM1kdJCWrt5vNP_XmQDgOISGDCD0MXp19-ZppiBwx0m27vQi1EcrOYNcM7iP6TOuGLfMmtx_gxp3DDYxNjVVMcS0tAw4GudrG6jopImbCIUAvVs2nXE14D7V-Swq49AnxSr5scVLfXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب حسين مؤنس:
الدولار الذي نحتاجه يجب أن نُنتجه داخل العراق، عبر تطوير القطاع الخاص، ونقل الموظفين تدريجيًا من القطاع الحكومي إلى القطاع الخاص، وزيادة الإنتاج والتصدير، لا أن نعالج عجز الاقتصاد برفع سعر الصرف، بما يؤدي إلى إضعاف الدينار العراقي وتقليص القدرة الشرائية للمواطنين.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92892" target="_blank">📅 21:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hw26Gz8rgNB6lFFij6L78RX4w_m0Qlhzy02wFRdiUreh9_Gthz8iPqHiJP3eU-rB_qglqQFeKWaLKFEaE4xKIotI3QDzEvxFnNA8PjIvAStSBxOfK47KD00a98lSmCGTBrG8mPxlf6UZIdw_X8gBYEordGzD6cJ9c262CVUs6cB7VI8Ab3iFd6ENywQnlPBMzztlIux8qfW8CnznrPSOcdVMQHbLhHkDNEBf50_bTYJhY99muhSLlBC3QrQXgY4ToF12UIcsg1eU-Ie8hGX5Ch8FLmNCIHc0wrirCnJupCA3Vc3QFaUsHs7TF6_ur7DVxS4q18Awcc_qUiYmBoA39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
🇮🇶
اسعار الصرف في بورصة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92891" target="_blank">📅 21:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92890">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d69d0e9c4.mp4?token=hoHRpRjtvUZQxR2qRcasUtgm_0IbgHWR-MuuXlki8Wp7EJmTQlvYgfD6T2rkWD71FHYrmCJdUGW25SEPOrP6T0GD4qYFOFwqlW_U_fMlJ95tMOQPgnX9_DzCAYsPFv9GL2TeUPmqzChVCjugzf6iZzwjepTmYN5WfHU8h4RJsV7tCmOZ_pU74rCnJMmjtLH3a35HxUT1Dqp9fQGbcHUcyTIC1Qd0jSvv9w-47PIQUdyyq4N6WkQwVc4AgcfOpsCOCciCsKPPrZW2-JfRNYGLAznm-EN_1OBJju0IYYtX3-tR3xpqwHU2jB0AVJg2l-2CYcynu8XrliiNpudXB4y0XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d69d0e9c4.mp4?token=hoHRpRjtvUZQxR2qRcasUtgm_0IbgHWR-MuuXlki8Wp7EJmTQlvYgfD6T2rkWD71FHYrmCJdUGW25SEPOrP6T0GD4qYFOFwqlW_U_fMlJ95tMOQPgnX9_DzCAYsPFv9GL2TeUPmqzChVCjugzf6iZzwjepTmYN5WfHU8h4RJsV7tCmOZ_pU74rCnJMmjtLH3a35HxUT1Dqp9fQGbcHUcyTIC1Qd0jSvv9w-47PIQUdyyq4N6WkQwVc4AgcfOpsCOCciCsKPPrZW2-JfRNYGLAznm-EN_1OBJju0IYYtX3-tR3xpqwHU2jB0AVJg2l-2CYcynu8XrliiNpudXB4y0XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب حول الطاعون:
روسيا لا تصدر الكثير من التصريحات.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92890" target="_blank">📅 20:59 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

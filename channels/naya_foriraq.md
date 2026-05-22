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
<img src="https://cdn4.telesco.pe/file/l2AdWnGecRyk1kQEXr3T-IbEAUymEXTHibljilEhrierhCAJUMahXn95ncjAu5ivxH1QkAf4L32MXy7ZwArktcX6cX5z8Ch1GkOw4JwyS10Uq9-MHUZ3dvvKKBMkgZiOGbyrqMbZeB3vK8lckQ-YOQ_kV4TRSKoRuLAjadGYS9jIG5-Hh2dEApaGrC6cQRhoxLt-mRoSGu9JnABwtEFGBWWGXcoPe1bgLEMWG88NAhV0g-p6nCMlf76ZD8i5AVMRVv-xj_5ng6eU5Z1CJbjumdwq41L0Vqx8mTuniR0ublJR_bkYJiO8_2SM-LaevhjogUgI71pUWnGd9xwrHkaLfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 06:04:48</div>
<hr>

<div class="tg-post" id="msg-75855">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بلومبرغ عن شركة رابيدان إينرجي:
استمرار إغلاق هرمز حتى أغسطس يزيد من خطر ركود اقتصادي يقترب من حجم ركود 2008.</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/naya_foriraq/75855" target="_blank">📅 02:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">#عاجـــــــــــــل
⭐️
الشركة العامة لموانئ العراق:
تعلن الشركة العامة لموانئ العراق استنفار جميع كوادرها في قسم السيطرة البحرية ومركز البحث والإنقاذ ضمن حدود المياه الإقليمية العراقية، وذلك عقب ورود معلومات بشأن فقدان سفينتين، مؤكدة أن أقسامها البحرية لم تتلق أي نداء استغاثة من السفينتين (Bridge 1) و(Bridge 2) اللتين ترفعان العلم البوليفي.
وأوضحت الشركة أنها تلقت رسائل إلكترونية من الجهات الامنية في عدد من موانئ حوض الخليج العربي، ومن مالكي السفينتين، تضمنت طلب تزويدها بأية معلومات تتعلق بالسفينتين المذكورتين، وذلك بسبب فقدان الاتصال مع طاقميهما وصعوبة التواصل معهما خلال الفترة الماضية.
وبينت الشركة العامة لموانئ العراق أن السفينتين لم تدخلا المياه العراقية، كما أن الأقسام البحرية المختصة، بما فيها السيطرة البحرية  ومركز البحث والانقاذ ، لم تتلق أي اتصال أو نداء استغاثة من طاقمي السفينتين، ولا تتوفر لديها أية معلومات عن موقعهما الحالي.
وأكدت الشركة العامة لموانئ العراق أن عمليات المتابعة مستمرة عبر أنظمة التتبع الإلكتروني بالأقمار الاصطناعية، وبالتنسيق مع إدارات البحث والإنقاذ في دول المنطقة، وسيتم الإعلان عن أي معلومات أو مستجدات فور ورودها.
https://t.me/nayaforiraq2</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75854" target="_blank">📅 00:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75852">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta_0O8vKANnDGbh46_ta7NI_myAvdCuZzXPsKF4FneL-ceFDiYd7Fvv8Cez9gzwBo4LMjHSjTHtnnoM0WAH5Tt_1_NxefqF1FBu-tNGW2PwNYc9HJmg84SFEAjoF7Oomcrk67BWz0Sn5Pz6XAajjw8AgfXadSQW7d6IUjYPesouYHJ9rUFeMmC2zl1b9H-wMhtSNrvF_VHx_-Wnal9hapWP0-h9Itgf6db7e8Doyry3ptAPyIfAJv8zLK1gbZsGAvlQ47QUbwXWtRtbt90HVFlAwCou9cnY5eYuAGKd2lGYCHhfaTA7wPH3R-TTWz3fENeM_uLgbblRXgkkVZzt_rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b338d82e3.mp4?token=u0aB-7whECePrs3chMwOeEY1U5eKhimVbce48DI_ihr2JVRbAmxGDlbOT1qyUHG2g-Yp2N3wKq_YdOEEhxE4uDkFWekPITnzIfzu4kb4_BA1KsIFOv6IFhRa8FsJEhTUKsML-obknIJXLznMk9UTBTPk-HedUtv_-SO3Png_BiegORyZ5IaN8k6l6Gev3aHwR_Lr4nTAxaTE-1NvBRMSD6rIfYeOKkhnpl8LskprHAfHllVsILhgUr3yje3Wi8SMrczB8RW91zfP2zUChjyjjlYRoAf16ZfPYPxmm7tBfNcx0c4-mQ2SJ1-ls2CqIkFwIFXi5FkYjbDAJ-NOivpqbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b338d82e3.mp4?token=u0aB-7whECePrs3chMwOeEY1U5eKhimVbce48DI_ihr2JVRbAmxGDlbOT1qyUHG2g-Yp2N3wKq_YdOEEhxE4uDkFWekPITnzIfzu4kb4_BA1KsIFOv6IFhRa8FsJEhTUKsML-obknIJXLznMk9UTBTPk-HedUtv_-SO3Png_BiegORyZ5IaN8k6l6Gev3aHwR_Lr4nTAxaTE-1NvBRMSD6rIfYeOKkhnpl8LskprHAfHllVsILhgUr3yje3Wi8SMrczB8RW91zfP2zUChjyjjlYRoAf16ZfPYPxmm7tBfNcx0c4-mQ2SJ1-ls2CqIkFwIFXi5FkYjbDAJ-NOivpqbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مواطنة جرينلاندية تهتف ضد مبعوث ترامب إلى جرينلاند "جيف لاندري" وتدعوه إلى ترك بلدها والعودة إلى منزله.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75852" target="_blank">📅 00:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75851">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn-9i27gekANQJplsjpo5MMKPWM3JpP68Hhm-TlGYBRUWylfeCo53G9ldQIIA-oyWHM9Vyxlg8x6uukjciNcIYpg4D192ni3-3F-vTaA7kQsdPVzvA3tUffnhKTkXGOmi_ds9V5BTsrFtzZHZflfcEcKvvcijnS7MeDX-Rmf1BFQ3-DnJ6FTNdMznghiNWDbFMzVjNN7DqFquofPgbG3OWap7A1qF6GeKMmVCFZ87mD8VAVl2EeJm0GthGn6TpDsj5lYf8yYk6IcPQdw0nFKHQaJ2lp-QBBVHmtuq_BNrV1yG3fw_Wibnli_gBZCozltg9jLOjUbH7h_gv4qK1qGIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
"بناءً على فوز الرئيس الحالي لبولندا، كارول ناووركي، الذي تشرفتُ بتأييده، وعلاقتنا به، يسرني أن أعلن أن الولايات المتحدة سترسل 5000 جندي إضافي إلى بولندا. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/75851" target="_blank">📅 23:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75850">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭐️
حكومة آل خليفة المتصهينة تأمر بحبس أكثر من 40 عالماً ورجل دين شيعي بارز في البحرين لمدة 60 يوماً على ذمة التحقيق، بالتزامن مع تجميد حساباتهم المصرفية، في خطوة تُعد استهدافاً لأسرهم وتصعيداً جديداً في سياسة التضييق والمعاقبة الجماعية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75850" target="_blank">📅 23:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75849">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭐️
دوي إنفجارات في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75849" target="_blank">📅 22:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75848">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
عضو لجنة الأمن القومي في البرلمان الإيراني "إسماعيل كوثري":
إذا استخدمت الإمارات العربية المتحدة المواقع التي وفرتها الولايات المتحدة ضدنا، فسوف نطلق عليها صواريخنا بكل تأكيد.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75848" target="_blank">📅 22:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75847">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
🇺🇸
بيان صادر عن حزب الله ردًا على العقوبات الأميركية:
إنّ ما صدر عن وزارتَي الخارجيّة والخزانة الأميركيتين من عقوبات طالت نوّابًا لبنانيّين منتخبين من الشعب، وضبّاطًا في الجيش والأمن العام، ومسؤولين في حزب الله وحركة أمل، هو محاولة ترهيب أميركيّة للشعب اللبناني الحر من أجل تدعيم العدوان الصهيوني على بلدنا، وإعطائه جرعة سياسيّة وهميّة بعد فشل جرائمه في ثني اللبنانيّين عن ممارسة حقّهم المشروع في المقاومة دفاعًا عن وطنهم.
إنّ التهمة التي ساقتها الإدارة الأميركيّة ضد نوّابنا ومسؤولينا هي رفض نزع سلاح المقاومة والتصدّي لمشاريع الاستسلام التي تحاول الإدارة الأميركيّة جرّ بلدنا إليها لمصلحة الكيان الصهيوني، وهذه التهمة تطال غالبيّة الشعب المتمسّك بالمقاومة والرافض للاستسلام. وهذه العقوبات هي وسام شرف على صدر المشمولين بها، وتأكيد إضافي على صوابيّة خيارنا، وهي في مفاعيلها لا تساوي الحبر الذي كُتبت به، ولن يكون لها أي تأثير عملي على خياراتنا وعلى مواصلة عمل الإخوة والمسؤولين في إطار خدمة شعبهم والدفاع عن مصالحه وسيادته.
أمّا استهداف القرار الضبّاط اللبنانيّين عشيّة اللقاءات في البنتاغون، فهي محاولة مكشوفة لترهيب مؤسساتنا الأمنيّة الرسميّة وإخضاع الدولة لشروط الوصاية الأميركيّة، وهذا القرار برسم من يدّعون صداقتهم للولايات المتحدة التي تسعى لتقويض المؤسّسات الوطنيّة. وعلى السلطة اللبنانية أن تدافع عن مؤسساتها الدستورية والأمنية والعسكرية، حفاظاً على السيادة الوطنية وكرامة لبنان واللبنانيين.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75847" target="_blank">📅 22:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75846">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سوالف الگهوة
مسرور وارين بارزاني وسومو والزيدي في بغداد ..</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75846" target="_blank">📅 22:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75845">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
نحن على استعداد للتضحية بكل ما أوتينا من أجل شرف إيران وعزتها، ولا نخشى الشهادة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75845" target="_blank">📅 22:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75844">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭐️
يديعوت أحرونوت:
🇮🇷
🏴‍☠️
صور الأقمار الاصطناعية تظهر تضرر قاعدة "رمات دافيد" وإصابات محتملة في قاعدة "نيفاتيم" وأخرى تابعة للوحدة 82000 وقواعد إضافية جراء القصف الإيراني.
🌟
🏴‍☠️
تُظهر صور الأقمار الصناعية حريقًا هائلًا نشب في معسكر "شمشون" قرب طبريا بدءًا من 10 مارس/آذار، وهو اليوم الذي أعلن فيه حزب الله عن هجومه على الموقع باستخدام سرب من الطائرات المسيّرة. بحسب تحليل الصور، استمر الحريق لعدة أيام، وامتد على مساحة تقارب 200 متر داخل القاعدة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75844" target="_blank">📅 22:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75843">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkTPr2i4wZybHDTxnG83mV_IJCmF4LgbMih5My9h1e06quSH5VCQqEjDWDXrLq5lXcq3-eOCQNirqNO_pI_33sHOZ5zT1dlEWaN1X6NejOZbvlzHveF85Rwc7TADGZeqd7A3ItqatNfTD7vIeeN83046Q_nchggcQbTt-vTmlBVmPwBl3eTfhIJogrL0PHT2Exsj4Zn4G3jSQ9Y3AbQzFXLpVtaoVqvCvFnE8ovC37IZ_DiOUK-8c1ISChSCJd1RscOkoNain7-evP1Gbi2zazlA0tWtRkU6Cu2UBDbnMlYZY57i5QdHJCz-pHPfBV3emm_7c9WkMItToTD1Sd9oRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
شكرا لتروي نيلز العظيم على القتال من أجل مواطني شرق فلسطين، وسلامة السكك الحديدية، وجدول أعمالي. أدعو الجمهوريين في لجنة النقل إلى دعم تعديل قانون سلامة السكك الحديدية، الذي سيتم التصويت عليه قريبا جدا. لقد أيدت مشروع القانون منذ عام 2023، ونحن بحاجة إلى إنجازه! شكرا لك على اهتمامك بهذه المسألة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75843" target="_blank">📅 22:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75842">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
🌟
بلومبرغ:
‏دمرت إيران أكثر من عشرين طائرة بدون طيار من طراز MQ-9 Reaper التي تشغلها القوات الأمريكية منذ بداية الحرب، وهي خسارة كبيرة بقيمة تقارب مليار دولار تمثل 20% من مخزون البنتاغون قبل الحرب لهذا النظام غير المأهول الذي يصعب استبداله.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75842" target="_blank">📅 22:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75841">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlQZ1Jci2SRFltXD0k4ZmbeGKzrI1KY276c5X30kjMfmvjJiUUzyMGlN1IUb9caQVBJ9w4pVbR2lEueaei-qcIW4GFPebEyodZRb0TdWVQVRtoh8j2mGBmw-myro0sPuYhl2mGt9NsT5unoIPm-bewuRmNCeGj4EslRm3TvAtAqKU8c9GnpXYZCSxaoMB5D7DEZNMuyXTq-97xmwFS_5gEfb5cAickv5TAdr13utgOQdw9swlJ3NDlaVBZfRaQNtxWCPMqe0MQOVU59hhBpTjISkTAW_kj27X0GCWozwyN_mQ1IF_9sMs9ewfK4cRUlQdvMUQForoRlnT25I32l5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
برعاية وزير النقل السيد وهب الحسني..
وزارة النقل توقع إتفاق تعاون ونقل رسمي بين الخطوط الجوية العراقية والإتحاد العراقي لكرة القدم لدعم المنتخبات الوطنية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75841" target="_blank">📅 21:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75840">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⭐️
رئيس المجلس السياسي الأعلى اليمني "مهدي المشاط":
أثبتت أحداث السنوات الماضية والراهنة في غزة واليمن ولبنان والعراق وإيران أن العدو الصهيوني رغم جبروته العسكري ليس بقوة لا تقهر.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/75840" target="_blank">📅 21:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75839">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⭐️
وسائل إعلام كردية:
محاولة إغتيال تطال "خورشيد هركي" في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75839" target="_blank">📅 21:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75838">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
ترامب: لا يمكن لإيران أن تحتفظ بيورانيومها المخصب للغاية. بمجرد أن نحصل عليه، سنقوم على الأرجح بتدميره. نحن لا نريده.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75838" target="_blank">📅 20:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75837">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏴‍☠️
طيران مسير من لبنان يهاجم كريات شمونة ومحيطها وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/75837" target="_blank">📅 20:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75836">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
ترامب: لا يمكن لإيران أن تحتفظ بيورانيومها المخصب للغاية. بمجرد أن نحصل عليه، سنقوم على الأرجح بتدميره. نحن لا نريده.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75836" target="_blank">📅 19:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75835">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc2cb4582.mp4?token=BwZjVSEr5P8UrVuu59g908207zP35ItcKTh1a_BTs_tHlimE2rvAe02xBKrZQYJ7aqix6f71kBAuCrUKiUARfSsiEad0TkfaBSxfCSR5LkNhp-ELJ0p4f9Mx0MuhkUTHLKCoNW8rMM7Y3tKy50TxYckyVU8xaUBIv09gBLSGsTzIMKZZlatrW7DmOOfgEvrQJjCUhi6oYhdo_2bIAiTulcPY9l_2aANDve76pzSydB9O9mTdOfeSjkEFr0op45BphVUEyfy4-tDNZFEEtqjDe2k2SbYd1uU7MOdbs9zPkPWyLC1-ssmKcHnUIMIKFOfqiYxtQvZqilSvOO-Bgq1XuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc2cb4582.mp4?token=BwZjVSEr5P8UrVuu59g908207zP35ItcKTh1a_BTs_tHlimE2rvAe02xBKrZQYJ7aqix6f71kBAuCrUKiUARfSsiEad0TkfaBSxfCSR5LkNhp-ELJ0p4f9Mx0MuhkUTHLKCoNW8rMM7Y3tKy50TxYckyVU8xaUBIv09gBLSGsTzIMKZZlatrW7DmOOfgEvrQJjCUhi6oYhdo_2bIAiTulcPY9l_2aANDve76pzSydB9O9mTdOfeSjkEFr0op45BphVUEyfy4-tDNZFEEtqjDe2k2SbYd1uU7MOdbs9zPkPWyLC1-ssmKcHnUIMIKFOfqiYxtQvZqilSvOO-Bgq1XuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌟
ترامب: نحن نتفاوض بشأن إيران وسنحقق هدفنا مهما كانت الطرق.  نحن ندرس رسوم العبور في هرمز، ولدينا السيطرة التامة على المضيق.  أريد مضيق هرمز مفتوحًا ومجانيًا دون رسوم.  نملك تكنولوجيا طائرات مسيرة متطورة لضرب إيران.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75835" target="_blank">📅 19:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75834">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7053f45077.mp4?token=tpTwx178QLSucFGK_CY-DIO1qJbNmXtxP2TViuGFUBja1iZNJOXQT7AVCwIQvJFKxZ-IcDtZ1Bz6Z8wWYRibKH8VOwkyCnszysrPVSGKC43TM01vuPbRJ36LusDOwLalgZNKiKUSqgtqd3MacwQ_Qb6aWkmzR-0vPqrzN_KyS0JThIbc8Gv6M7G_vVxJSjIGWLaQ9Fl96EuEPYfGtC-jjMFtsjTfssxpt_BXiT4voWsp6dEGTD5JJxS1K200Vg6RADqJs3rhI1xl3d6TsqL46IHdEK_Q8PLkOXnr6f8eTUhZdNNgE2zg8bZiEnRwcp3aB3vtT7ugw2L_Xig0aYPV8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7053f45077.mp4?token=tpTwx178QLSucFGK_CY-DIO1qJbNmXtxP2TViuGFUBja1iZNJOXQT7AVCwIQvJFKxZ-IcDtZ1Bz6Z8wWYRibKH8VOwkyCnszysrPVSGKC43TM01vuPbRJ36LusDOwLalgZNKiKUSqgtqd3MacwQ_Qb6aWkmzR-0vPqrzN_KyS0JThIbc8Gv6M7G_vVxJSjIGWLaQ9Fl96EuEPYfGtC-jjMFtsjTfssxpt_BXiT4voWsp6dEGTD5JJxS1K200Vg6RADqJs3rhI1xl3d6TsqL46IHdEK_Q8PLkOXnr6f8eTUhZdNNgE2zg8bZiEnRwcp3aB3vtT7ugw2L_Xig0aYPV8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌟
ترامب:
نحن نتفاوض بشأن إيران وسنحقق هدفنا مهما كانت الطرق.
نحن ندرس رسوم العبور في هرمز، ولدينا السيطرة التامة على المضيق.
أريد مضيق هرمز مفتوحًا ومجانيًا دون رسوم.
نملك تكنولوجيا طائرات مسيرة متطورة لضرب إيران.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75834" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75833">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرايا اولياء الدم</strong></div>
<div class="tg-text">قصيدة
نحن اولياء الدم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75833" target="_blank">📅 19:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75832">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
وزير الخارجية الأمريكي: نظام الرسوم في مضيق هرمز سيجعل التوصل إلى اتفاق دبلوماسي أمراً غير ممكن.  ‏كان هناك بعض التقدم في المفاوضات مع إيران لكن النظام فيها متصدع.  ‏ترامب يفضل اتفاقا مع إيران لكن الخيار العسكري على الطاولة.  ‏الباكستانيون سيتوجهون إلى إيران…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75832" target="_blank">📅 18:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75831">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
وزير الخارجية الأمريكي: نظام الرسوم في مضيق هرمز سيجعل التوصل إلى اتفاق دبلوماسي أمراً غير ممكن.  ‏كان هناك بعض التقدم في المفاوضات مع إيران لكن النظام فيها متصدع.  ‏ترامب يفضل اتفاقا مع إيران لكن الخيار العسكري على الطاولة.  ‏الباكستانيون سيتوجهون إلى إيران…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75831" target="_blank">📅 18:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75830">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
وزير الخارجية الأمريكي:
نظام الرسوم في مضيق هرمز سيجعل التوصل إلى اتفاق دبلوماسي أمراً غير ممكن.
‏كان هناك بعض التقدم في المفاوضات مع إيران لكن النظام فيها متصدع.
‏ترامب يفضل اتفاقا مع إيران لكن الخيار العسكري على الطاولة.
‏الباكستانيون سيتوجهون إلى إيران اليوم.
دعونا نرى إمكانية التوصل إلى اتفاق مع إيران، حيث توجد بعض المؤشرات الإيجابية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75830" target="_blank">📅 18:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75829">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇷🇺
وكالة
إنترفاكس الروسية:
بوتين عرض على الرئيس الصيني فكرة نقل وتخزين اليورانيوم الإيراني المخصب في روسيا.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75829" target="_blank">📅 18:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75828">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇹🇷
النيابة العامة التركية تنقل عدد من ناشطي الصمود إلى وزارة العدل التركية لأخذ إفاداتهم تمهيدًا لإعداد مذكرات اعتقال بحق مسؤولين إسرائيليين متهمين بالاعتداء على الناشطين.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75828" target="_blank">📅 18:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75827">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
السيد عبدالملك الحوثي:
النفط العراقي تنهبه الشركات الأمريكية وتستفيد منه قبل الشعب العراقي، حتى على مستوى الشركات المنتجة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75827" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75826">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📰
بلومبرغ:
‏تجري إيران مناقشات مع سلطنة عمان حول كيفية إنشاء شكل من أشكال نظام الرسوم الدائمة الذي من شأنه أن يضفي الطابع الرسمي على سيطرتها على حركة الملاحة البحرية عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75826" target="_blank">📅 17:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75825">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🤺
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ
18-05-2026 منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في مستوطنة شوميرا بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75825" target="_blank">📅 17:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75824">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
مدير مركز العمليات المعلوماتية المشتركة العراقية:
رصد أكثر من 3200 صفحة مرتبطة بـ (إسرائيل) ودول مجاورة تعمل على إثارة النعرات الطائفية، حيث وصل المركز إلى مراحل متقدمة في مواجهة هذه الحملات.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75824" target="_blank">📅 17:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75823">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7be1616c.mp4?token=W8i4V29-MCoRg6wpdjG0Zth4CP-Y2WjoPtoeOT0WzePGqkeLMjae8QpkD8U7wp-V_HOVW8V63JsrzJG1lqn5ic7C4TIlGVT2v6-SpFsfdaGuOkWLq7rnKhtQq9Cdc1uHW1sqA3I5Ecob3CNeL1UVGTJQkaQPVSYN-i9fVurp1gQa7vf2nUuspGIcYKlMRg50gK07n_KVSoU1f6ijvoZu1VagHUL3UMpWJwTvPt2iW5JIzcQf8QNtn5LNl6hsw5s1H9PT4EpKJ72cRSidM-vNA91uc_KELnAWTbaCiYM37XrwHYEdz1gU28Ai_t9-lvUzguP2514AhQ-Ga4Ixn-Rumg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7be1616c.mp4?token=W8i4V29-MCoRg6wpdjG0Zth4CP-Y2WjoPtoeOT0WzePGqkeLMjae8QpkD8U7wp-V_HOVW8V63JsrzJG1lqn5ic7C4TIlGVT2v6-SpFsfdaGuOkWLq7rnKhtQq9Cdc1uHW1sqA3I5Ecob3CNeL1UVGTJQkaQPVSYN-i9fVurp1gQa7vf2nUuspGIcYKlMRg50gK07n_KVSoU1f6ijvoZu1VagHUL3UMpWJwTvPt2iW5JIzcQf8QNtn5LNl6hsw5s1H9PT4EpKJ72cRSidM-vNA91uc_KELnAWTbaCiYM37XrwHYEdz1gU28Ai_t9-lvUzguP2514AhQ-Ga4Ixn-Rumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75823" target="_blank">📅 16:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75822">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75822" target="_blank">📅 16:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75821">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🤩
استطلاع رأي لفوكس نيوز:
ارتفاع نسبة المعارضين من الأمريكيين للعمل العسكري ضد ايران إلى 60%</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75821" target="_blank">📅 16:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75820">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📰
‏
مسؤول أميركي لفوكس نيوز:
إيران مصممة على إبقاء اليورانيوم المخصب داخل حدودها.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75820" target="_blank">📅 16:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75815">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ib0jMy9t7wt6lD2k8L3fWoR5oKM4Awx9Wn_wDY719N_pZ7OeEFRAVe8tu2MLs6cHeB293SKuem5req7P_UEgE9klR_pNUZ9xbpiVFhaaLbQWflc_yVnkE1Sj8ZsHJsGulj56KfnW95qttVAvPjIWEG3bMADhhLK0W1mL_aZ3CnJ5no7G8gPGksx9KBAlcMtycqcrI2goTheXq7EWLrTXEh2MVEv_pxIA1oYTX6SmIdBLdnRBJ_hDnCxVJFqGTGrO99paYvD2npAdbtcW0Ju2v7oUXEuatNPoX-7fmRuG6Xm5CCMUxoxRUbYwmW4gV7E8Lhhpx3R_HQdz8_aStYIcBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzyDw7VodRlBjMoOCFWhjUKnaFQ_uiy2ah5TyPb0dJVAPjRs2tWaZiZRV3u_gRVblcv90vgYEK63XWFcLOkAOk6AQYl09HkEUGQrwdq02GBg_8hERc8JjpwTfoXiWjbUIgHAFQtLORNDZSaI4nrAr33hJPagC95J-6j5I9NE6uWSMu18qZt52mHBxPGuDeJQ5WOSj_-Ydsg9ZXuCGoFLghYYVrTpya2Qe5vbAywvWYV6KSoZWijOxcH7FuxyX3l1hsi8TKPxJa6BsFngcitml9vQQk9s9dIPX6iiiP-2eQNhtx9V0YwdwtvifjBWxh4vV1apxbqNx-tbnI4pHE8ZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKjVYk_6GroD1JOBTDrm0wyiRymSOLX-he22OzxrQ6eEsXlq_gTO3mPe8rq31LHrYgyIibMKy6EJk66Cge9XcL33IS3RZsjZk1yYfiAcCpMx75o2EO7viqUCTvkRzZbXEqlnpaWIP05YuQg7y6x0j0uU_pM7JyW6c5SLUNYQPpVim5M5V6EvocaJgbaa3eXde3lwMo4h8T3tYOpBZ6ZHzjaW_TsW_Attqxx7OCXDNWPqNUK1iCd2PFTdnFSVZRAlN58D41geKeXtc_B_ATcy_Mv9BImNWnkCZPaTC-7eXj0CSG4v1jXeW3SStEi3GTweuWvcSGbhBN4OEpAmPkAHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1d5Rc5L7lZd6O6MxUWcBKGLJ7-QdAGH5Yu7NvxRukh2OSQ7tzyW6-6tkc8vZulqQ1On36K2iv0Ytyp2sPQzNL0w20ZyFpyYTbeX7e5BuHLJBybuG44-iAn85F9G99l0BRjHB3iFoxNiTzclxhks3RMcs0LmEwm8pbRiNeesyuH8zktDdeuotTl6wyO-Gtfvavr6T-MARFrE3eKLWW-hw4DAeZJ_pjYkbcHaOzlWDGAWbEFX1L9EiqY3Nd-oRQN8G7szeorHogMtK1GLwxQN03gj2j22oEh4YChfO-KhAfnBXMkP_dl_zOfKoMWQRdU9xZ_3idWxsPtQ80dNZrXn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcU6bQ4Ht_d_Qz2NexL0vTL_eSo-m904V4x4HqvjxUM2SwAwIsv09SUjhoRqLJ9ha-Li22tcoMUOcUg2ol0uEmf6ln65o07pGxc6wDDB89v4Ui2ARzaw4fopQMU23_K52cEMbvef_WRS0S8NUEOjucexTTMRRMX32dsMcm6PI5mp9sBSBD0Cc9xZqLdSUEMBia-7_f2wjDWlCfOfv1rM9AF2lcCtDWapANEzt4PiTV_o7MF0Dd_G_lM8aa2JZmuRsf-He1CkSkwXxd2FU374CEmBf6HCl1l6Uxtq_YIhyxrUn931AbsOeJuBnnEuH8hX1Ym4aZgjCtpFM0OjIA_1wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">يصادف 21 أيار اليوم العالمي للشاي</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75815" target="_blank">📅 15:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75814">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اختطاف زوجة وشقيق (كاروخ سيد رزكار) زعيم الحزب الوطني الكردستاني من حي رابرين في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/75814" target="_blank">📅 15:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75813">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
🏴‍☠️
القناة 13 الإسرائيلية:
نتن ياهو يدفع باتجاه استئناف الهجمات على إيران، بينما طالب ترامب بمنح مزيد من الوقت.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75813" target="_blank">📅 15:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75812">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇳
‏الهند تؤجل قمة مع الاتحاد الأفريقي بسبب تفشي فيروس إيبولا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75812" target="_blank">📅 15:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75811">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">😞
‏الطاقة الدولية: أسواق النفط يمكن أن تصل إلى منطقة الخطر في يوليو وأغسطس، صعوبات ستواجه المزارعين لتزامن الحصاد مع ذروة طلب الوقود.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75811" target="_blank">📅 15:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KswtDicsSD6g1kRFMIqRaQl1bKt5lpIe4TP_zj5XKoaOVdfWj5tulUdpo3va6Yf_zwOamhHVc8lCawYk79j8kPXTVl9FWQAWwohrD6Nh4lhjG-vvnDUMNalTNI6Grbx-qJQDME-K-NMWxnW0EdAnT1yYyAwIn934QovC3u501zw9QR6PdRzxGsJgNhI9g0JAmtOdSjbLEP0GLSxUxWOwXmuIWNdXxwpD_pM6bYIEJpngpBZhE9H7_8ytj1lZtkxdWoM13fdaySSdLtrPT9mNLqsAQKeSBOKbOSP79GWSOZSX16RqyMPHVW2LRrd4adec3-Jcm_HC_UTWBpWKxO7Csg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
إيطاليا تطالب بعقوبات أوروبية على
الوزير الإسرائيلي
بن غفير بسبب المعاملة المسيئة لناشطي أسطول غزة</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75810" target="_blank">📅 15:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75809">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">😞
‏
الطاقة الدولية:
أسواق النفط يمكن أن تصل إلى منطقة الخطر في يوليو وأغسطس، صعوبات ستواجه المزارعين لتزامن الحصاد مع ذروة طلب الوقود.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75809" target="_blank">📅 14:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75808">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hijuERptcGIX9kbFmuSoIiijtOLKnWruQQcyBXxmVJIGSyqRu4Mkvm41bCi0DqyLbxrOmkoKIeLEL7IDH0GnJRN9pZjcM-ZoEtVdLk-VdtNwxnTBkJ-3nFkzCAPC-oAsYY1M9YtZEy1o0w9l2p_EJwMtQrmOaQdhxkvhSXo4CkVr1lRP5NoDJK-3I7TzufGjAaqpOW4PGuEKN9ppeIo_v7c0oVuYPsjZOD-BGVjb9-BqyqYSf5VE2GEalbN5GSxQCjwHmQD0TvNMwdjH838wPlng3YXBNVOb4hrirbwbWytqpOit4RIWIB8I4xRlyC3nuLD3X-wuodQ7BFFk3uikYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الايرانية:
إن صور وزير النظام الإسرائيلي في ميناء أشدود شخصيا وهو يهين النشطاء الإنسانيين المكبلين من أسطول "المساعدة إلى غزة" (كثير منهم مواطنون أوروبيون) صادمة للغاية. إنها تستحضر أحلك أصداء التاريخ - لحظات يرى فيها نظام، محمي منذ فترة طويلة من المساءلة، نفسه استثنائيا ولا يمكن المساس به وفوق القانون.
في ثلاثينيات القرن العشرين، عزت أوروبا نفسها بالوهم بأنها يمكن أن تظل صامتة - ومحصنة - في مواجهة التدهور المنهجي للكرامة الإنسانية والقانون الدولي والمبادئ الأخلاقية الأساسية، دون أن تدفع ثمنا على الإطلاق. لقد قدم التاريخ درسا وحشيا؛ ولا يزال تطبيع الفوضى والفظائع يقتصر أبدا على هدفه الأصلي.
واليوم، يمتد الخطر الحقيقي إلى ما هو أبعد من السلوك المؤكد لمسؤول النظام الإسرائيلي. تكمن القضية الأعمق في الصمت المتواطئ، والقبول السلبي، والتقاعس المؤسسي عن العمل تجاه الاحتلال، والفصل العنصري والإبادة الجماعية التي منحت مثل هذه السياسات والسلوك مظهرا من مظاهر الحياة الطبيعية والاستمرارية والجرأة المتزايدة.
إذا استمر الغرب في توسيع الفجوة بين قيمه الأساسية المعلنة وسلوكه الفعلي، فسيتعين عليه مرة أخرى أن يتعلم درس التاريخ القاسي: الإفلات من العقاب الذي لا نهاية له لا يخفف من الفوضى - فهو يطبع الفظائع ويشجع مرتكبيها.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75808" target="_blank">📅 14:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75807">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f30a6f56ef.mp4?token=niKbMP_o2nC39S_L89zxptzfwRV1oTgmvuPNzAXOHyKF0Drr0o21o9YAZOaZ2ViZbLE7ndPGRuwXw1P36kfNr7GbmruC8Z8CovCO4RNk78pKa_XyRv0p-eScdbieNNbKxHuTXjMICdVcRKVNsAL0NVEM7Q6cgjQstFxzCJ5B4B5CC4NohEjTDNMUZATTGgI6yKO0BhTU1PWNdtO5aJ9OXRXljzfj83_t0N4ibMzD1uyQp0odUJu-AoGBWmdTtZThtq9wZMSokZZBoC88DY9e-KO4H-l7GJgnDIxbWP3rAJqUUMkW74Pty594NoOxNkmXvVdtX2eH-3eBRkQI8gznH6ze5XxtKmhvKRnf3bLtqb7CVLiSzLSkvXy7Ym2r3IOKA91gmrtnnbF718sgZ4aqqtwIiA5kVDUDMnv4PB0BxCRrHEIjPHhVdcbba4OWcmJF3abqMydM0OJiTkcTuxDHMsQWLAj3E9S2UOh_OkNtNYX-W_Lwag6L6SoHwqPWq_DcLIwfoYJLOaOMtL6g6y4s2R9D4cZJ9orzKIi_5NN4a8Jo72R_5BiRLefnKGiT01YlDRdSDWsKe5p5-Z2TxifqGdYjIE5fzfIOoSoc5A_1PMZb0GebPYTPS-2mYSmUw36rga1yCX-VaC6SrEHp7-ZlH2iRmeA1iZU5azUfZbi0Xqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f30a6f56ef.mp4?token=niKbMP_o2nC39S_L89zxptzfwRV1oTgmvuPNzAXOHyKF0Drr0o21o9YAZOaZ2ViZbLE7ndPGRuwXw1P36kfNr7GbmruC8Z8CovCO4RNk78pKa_XyRv0p-eScdbieNNbKxHuTXjMICdVcRKVNsAL0NVEM7Q6cgjQstFxzCJ5B4B5CC4NohEjTDNMUZATTGgI6yKO0BhTU1PWNdtO5aJ9OXRXljzfj83_t0N4ibMzD1uyQp0odUJu-AoGBWmdTtZThtq9wZMSokZZBoC88DY9e-KO4H-l7GJgnDIxbWP3rAJqUUMkW74Pty594NoOxNkmXvVdtX2eH-3eBRkQI8gznH6ze5XxtKmhvKRnf3bLtqb7CVLiSzLSkvXy7Ym2r3IOKA91gmrtnnbF718sgZ4aqqtwIiA5kVDUDMnv4PB0BxCRrHEIjPHhVdcbba4OWcmJF3abqMydM0OJiTkcTuxDHMsQWLAj3E9S2UOh_OkNtNYX-W_Lwag6L6SoHwqPWq_DcLIwfoYJLOaOMtL6g6y4s2R9D4cZJ9orzKIi_5NN4a8Jo72R_5BiRLefnKGiT01YlDRdSDWsKe5p5-Z2TxifqGdYjIE5fzfIOoSoc5A_1PMZb0GebPYTPS-2mYSmUw36rga1yCX-VaC6SrEHp7-ZlH2iRmeA1iZU5azUfZbi0Xqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام العدو:
الإمارات تشتري من إسرائيل مكبرات صوت سيتم شحنها لأبو ظبي لتستخدم في صفارات الإنذار.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75807" target="_blank">📅 14:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل سرب من الطائرات المسيرة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75806" target="_blank">📅 14:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 17-05-2026 آلية عسكرية تابعة لجيش العدو الإسرائيلي في اسكندرونة ببلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75805" target="_blank">📅 14:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📰
وكالة ‏رويترز:
السيد مجتبى الخامنئي يرفض فكرة إخراج اليورانيوم المخصب من البلاد.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75804" target="_blank">📅 14:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75803">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل سرب من الطائرات المسيرة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75803" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75802">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الشرق الأوسط السعودية:
باتريوس كان بمهمة جمع معلومات من القادة السياسين العراقيين عن من يستهدفهم في العراق و كيف يتم تفكيك سلاح الفصائل .</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75802" target="_blank">📅 13:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75801">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: من المتوقع اصدار تعليمات لسكك الحديد والنقل ومحطات الحافلات بالبلاد للاستعداد لحالات الطوارئ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75801" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75800">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">إعلام إيراني: وصول قائد الجيش الباكستاني إلى طهران لتضييق الفجوات</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75800" target="_blank">📅 12:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75799">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
عمليات بغداد: تفجير مسيطر عليه من قبل الجهات الأمنية المختصة لمخلفات حربية  اليوم الخميس الموافق ٢١ ايار ٢٠٢٦ وذلك ضمن مقتربات مطار بغداد الدولي غربي العاصمة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75799" target="_blank">📅 11:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75798">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">إعلام خليجي عن ‏مصدر ديبلوماسي: طهران تدرس النص الأميركي ولم تقدّم ردّها بعد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75798" target="_blank">📅 11:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75797">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوي انفجارات في قضاء سوران بمحافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75797" target="_blank">📅 11:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75796">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb68cec79c.mp4?token=NblFIZbhbv96HMndU3N3_soVWocsX0Inf7ZETzjGuHLuFBXNKORdx9lIlyGQBGJ_uXPHpfdhZxxJ7GV_Xxg389llPitgF8Jq_mCnQnIhgk04ZS2xSqRK4cTq5lr489-BD-vXAQsasEpW12O5ZJ5nTjGEvJq6hul0847SjCjsi42B5A2cEBnD7JeK4mL6LOPQjN0AS8YCN33TJWDgOW3Y-mbBtobiOumNMWiw5-yuVKsFZmDl_dyqi7SwDBMXcKloJ9-Jc1Rud1cs37aO4luy_IYr4QG_K7JdJQGMT_zpjGI-iKJY--ch5n8_Vay0DJhyLp436YlDGfIY5KD5_Tunrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb68cec79c.mp4?token=NblFIZbhbv96HMndU3N3_soVWocsX0Inf7ZETzjGuHLuFBXNKORdx9lIlyGQBGJ_uXPHpfdhZxxJ7GV_Xxg389llPitgF8Jq_mCnQnIhgk04ZS2xSqRK4cTq5lr489-BD-vXAQsasEpW12O5ZJ5nTjGEvJq6hul0847SjCjsi42B5A2cEBnD7JeK4mL6LOPQjN0AS8YCN33TJWDgOW3Y-mbBtobiOumNMWiw5-yuVKsFZmDl_dyqi7SwDBMXcKloJ9-Jc1Rud1cs37aO4luy_IYr4QG_K7JdJQGMT_zpjGI-iKJY--ch5n8_Vay0DJhyLp436YlDGfIY5KD5_Tunrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من لقاء وزير الخارجية الإيراني عراقجي بوزير الداخلية الباكستاني.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75796" target="_blank">📅 10:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75795">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇵🇱
🏴‍☠️
بولندا تستدعي القائم بالأعمال الإسرائيلي بشأن احتجاز نشطاء أسطول الصمود
نطالب إسرائيل بالإفراج الفوري عن مواطنينا ومعاملتهم وفقا للمعايير الدولية
ننصح مواطنينا بعدم السفر إلى إسرائيل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75795" target="_blank">📅 10:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75794">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇪🇸
وزير الخارجية الإسباني: ترحيل 44 من نشطاء أسطول الصمود من إسرائيل إلى إسبانيا عبر تركيا مساء اليوم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75794" target="_blank">📅 10:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75793">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏴‍☠️
إعلام العدو عن ضباط كبار:
لا جدوى من البقاء في لبنان والجيش لا يحقق إنجازات في هذه الحرب بشكلها الحالي
مهمتنا غير مفهومة ولا نعرف إن كان الجيش يريد وقفا لإطلاق النار  في لبنان
لا يوجد وقف إطلاق نار في جنوب لبنان لكن لا يمكننا تفعيل كامل قوتنا
هناك تحديات كثيرة في الجبهة اللبنانية فإما أن تسمح لنا القيادة بالعمل أو ننسحب</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75793" target="_blank">📅 09:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75792">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-vNn50y9E6xbmqU-HBFOmfTTR3VppMgINDNNLRWopFj74gbvRf6twX5oNfgQGzGpz_m6Qkgsb7j5VBGzc5SDEIuJC6wFZUNMkJG0tahvfBP15Q7JELi0ruKVle_6ybnwzTYwmxQJNfj8QbxEi6goPZ7RIIp_Unn6xHTGMYQYvvcqDNd_HhCoHGQheqAqYNnE83pDoOOQVV7KgbKiy-u5lv54kVLAbN2O6C-E3JcnuMbtfpWX6wATjlqTbYdqIn56m_V-CvGqdJqITp0BveAaG2vYE7qviJybirwkNGX5j5xpGxedfB7uhL8B0MGgrOS7tpaZ95Y3aBNpJ11egN_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو
في تلك الأيام، في مثل هذا الوقت: عشية عيد الأسابيع (شفوعوت) عام ١٩٨١، دمر سلاح الجو الإسرائيلي
المفاعل النووي العراقي
. زجّ الهجوم "إسرائيل" في جدل سياسي، إذ كانت آنذاك في خضم حملة انتخابية محمومة للكنيست العاشر. اتهمت المعارضة بيغن بالتضحية بالأمن والمصالح السياسية في سبيل الدعاية الانتخابية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75792" target="_blank">📅 08:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75791">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
مساعد قائد البحرية في الحرس الثوري الإيراني:
أيدينا على الزناد وإذا كان ترامب يظن أنه يستطيع فتح مضيق هرمز بالقوة والسفن، فعليه أن يعلم أن البحرية نفسها التي زعمتم أنها دُمرت ستُغرقكم في قاع البحر.
على أعدائنا أن يعلموا أنهم مخطئون تمامًا إن ظنوا أن هذه الأمة ستتراجع بتدمير بنيتها التحتية، فقد أثبتت هذه الأمة على مدى 47 عامًا أنها قابلة للتدمير لكنها لا تستسلم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75791" target="_blank">📅 23:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75790">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية يطال عجلة تابعة للقوات الأمنية في مدينة سراوان بمحافظة بلوشستان جنوب شرق إيران ؛ إستشهاد أحد أفراد الأمن الإيراني كحصيلة أولية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75790" target="_blank">📅 23:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75789">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKXMcW9k5oMMNIBwVGWMu21vPdPS8rBXVYggJh17nJwxkv3aTvKVqemlemKQMxaOvUx_tNTVF79BLxFI62U5WUczL3N1NkH5BbagrektUCBu39M4iggX5jmeSfomiP1miXZzEg5oddtOlmi6xZ6ZXpsyRjeERO1BCJhIVjSdF9F8G54iSGWyUSWLUuYzgy0Hd-sJ8VK2m-vE6xPtR-gwQg86B3JA8A_tVLbMKLsDWy6S4TOU1e18qbw1qOlbgAOsHnd5V6jDxZ76BMsr2DHReES3CKtZ8i7yMZpgb_k6qEvMKEJy6kp5JX5BKyIHyDQfKU6J6Y_-siqDqXdyPA18kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هيئة إدارة مضيق الخليج الفارسي:
حددت الجمهورية الإسلامية الإيرانية حدود منطقة الإشراف على إدارة مضيق هرمز على النحو التالي: "الخط الذي يربط جبل كوه مبارك في إيران وجنوب الفجيرة في الإمارات العربية المتحدة شرق المضيق بالخط الذي يربط نهاية جزيرة قشم في إيران وأم القيوين في الإمارات العربية المتحدة غرب المضيق.
يتطلب المرور في هذه المنطقة عبر مضيق هرمز التنسيق مع إدارة الممرات المائية في الخليج الفارسي والحصول على إذن من هذه المؤسسة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75789" target="_blank">📅 23:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75788">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ddf11200.mp4?token=AyZ93-OflCdXaPf3rUQ2t6AtoHyNPaPEApHp3Kp2L6S0OOgYVQXE18z9Dr0hX5reXg-RrEM7R2jNhavhyIwAQoPqKoK745vDJUrgM5XaEFfjWLd32vtJzraXuK1kQvUomlurfMV5Lk676SvVixw5g5CKJ8uE_Kl0UyKUJoE4ASXMh_N6jQD2wsnE0jxMr-CL8FuxDTIYwsdqPBVjOHvbDWmU3b9nlR9hADTJNb7WaMwy2YXa2GTw54ZLtAR69uq_5YSGB47xoDrLukhSig8G3nB5qEfnIqBcWN8DMAkc_V3Iki4f9FjERXgRG7hu6Mq-z5M-17BC8ZkWqZ1XytzLMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ddf11200.mp4?token=AyZ93-OflCdXaPf3rUQ2t6AtoHyNPaPEApHp3Kp2L6S0OOgYVQXE18z9Dr0hX5reXg-RrEM7R2jNhavhyIwAQoPqKoK745vDJUrgM5XaEFfjWLd32vtJzraXuK1kQvUomlurfMV5Lk676SvVixw5g5CKJ8uE_Kl0UyKUJoE4ASXMh_N6jQD2wsnE0jxMr-CL8FuxDTIYwsdqPBVjOHvbDWmU3b9nlR9hADTJNb7WaMwy2YXa2GTw54ZLtAR69uq_5YSGB47xoDrLukhSig8G3nB5qEfnIqBcWN8DMAkc_V3Iki4f9FjERXgRG7hu6Mq-z5M-17BC8ZkWqZ1XytzLMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوالف الگهوة   من منزل العامري ، طرح مبادرة اليوم تتضمن صلح وبناء الجدار المتصدع داخل الإطار التنسيقي في العراق..</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75788" target="_blank">📅 23:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75787">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqZzTkiJ_S1t9mR0ZGIqsxdeVahbt-MOml453jOy3VB8301kZKgN4Ku5sqhkYcdAXq-cjwNKm6VeVTdA8VfUQoBz-4iVXAiLyDy2U_TNPwUUCTy3ZJ6q8BgMyFY64pqhnesfQvKOGpQ8Tz9x4kAnB-7TEPolt1TWpje0KlQdGbNuoH-_WcDvtA_-PbgFpIRtWtLc64fBBkmty660MeQjVtwPiYe8hupjJssh5EerIyNVcqoZFOrOS2eBuOXTzcXv8JDrjpm7din3VUsgbsbBmZ0BrN0KVKDGTh5ClwYrOD1-qRgAhNLLGijNv-fNeRv0TPmTFXsXmoa-0B3J79GsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالف الگهوة   من منزل العامري ، طرح مبادرة اليوم تتضمن صلح وبناء الجدار المتصدع داخل الإطار التنسيقي في العراق..</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75787" target="_blank">📅 23:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75786">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⭐️
هجوم صاروخي جديد يدك مقرات المعارضة الكرادية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75786" target="_blank">📅 23:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75785">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭐️
توثيق يظهر تصاعد أعمدة الدخان من مقر تابع لحزب الكوملة الكردي الإرهابي في محافظة السليمانية بعد دكه بمسيرات إنتحارية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75785" target="_blank">📅 23:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75784">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092cf934a6.mp4?token=GL6s9615-wU5-jvqgbXO8ZLxMD1IFVb3qXhI0mJ0b7joR4Sguut2pN9SxBJngpPRBkh5J6SlQ9cLuVtNOZbm8x3GUMsSQOL7dOWlNUQPbU04evCovQ3t5S_obmy2i95uVHFhcJHgxwdWdu9pg7xVE5W1Dhxdf0nJGnu57H--bEhraUXwP7-sQ05BQ-4zzGesRN6oN6YJSBqecTZsJM75829XyyzklgtBNOEnheadTcKaOgPmRl0iEsEE8GN-LqxyRItBzHZxv92z4DTXiJI3gos7jw-AXzBeJdnoHid2oENDPRwtC2_EuwHvSDTKugUcTqIMOy20f8u4L6vAO3NBEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092cf934a6.mp4?token=GL6s9615-wU5-jvqgbXO8ZLxMD1IFVb3qXhI0mJ0b7joR4Sguut2pN9SxBJngpPRBkh5J6SlQ9cLuVtNOZbm8x3GUMsSQOL7dOWlNUQPbU04evCovQ3t5S_obmy2i95uVHFhcJHgxwdWdu9pg7xVE5W1Dhxdf0nJGnu57H--bEhraUXwP7-sQ05BQ-4zzGesRN6oN6YJSBqecTZsJM75829XyyzklgtBNOEnheadTcKaOgPmRl0iEsEE8GN-LqxyRItBzHZxv92z4DTXiJI3gos7jw-AXzBeJdnoHid2oENDPRwtC2_EuwHvSDTKugUcTqIMOy20f8u4L6vAO3NBEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجار جراء هجوم بطائرة مسيرة انتحارية استهدفت مقر تابع للمعارضة الكردية (الكوملة) في محافظة السليمانية ضمن اقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75784" target="_blank">📅 23:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75783">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f0661e65.mp4?token=N7GP29eW1t89StOkz_5Q9r4GkvLZALj4Y2Vq8uzYVXeb5y6RjTlwDnFxTvFX7FiP2TvlpPwe1DzIUFCB_leokQvhCds7vl3H1RFwQGDcxvdZYdFF1FqNvIbz4RKR3UcJi7NTqsvy5goiyCbQovat0HEDz8J9QrIdPs1nn5vf6-YdQNs3HT6zjGGCq-yzR4j7i7sX-s47gyE45XwTA4x2_jJYhlOicEX-7gYdlUT_6olXwk2zl8ccqEclHRnWy7-VW9CETNylIqBeSziBULIPWyH-ZTbdgA2il68tbo5v2Bt2rsfvfvIVDTX1_HiJr694Kb19gj1_hsgwinSOdXrFRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f0661e65.mp4?token=N7GP29eW1t89StOkz_5Q9r4GkvLZALj4Y2Vq8uzYVXeb5y6RjTlwDnFxTvFX7FiP2TvlpPwe1DzIUFCB_leokQvhCds7vl3H1RFwQGDcxvdZYdFF1FqNvIbz4RKR3UcJi7NTqsvy5goiyCbQovat0HEDz8J9QrIdPs1nn5vf6-YdQNs3HT6zjGGCq-yzR4j7i7sX-s47gyE45XwTA4x2_jJYhlOicEX-7gYdlUT_6olXwk2zl8ccqEclHRnWy7-VW9CETNylIqBeSziBULIPWyH-ZTbdgA2il68tbo5v2Bt2rsfvfvIVDTX1_HiJr694Kb19gj1_hsgwinSOdXrFRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مواطنة جرينلاندية تهتف ضد مبعوث ترامب إلى جرينلاند "جيف لاندري" وتدعوه إلى ترك بلدها والعودة إلى منزله.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75783" target="_blank">📅 22:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75782">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الصهيوني:
إصابة 7 من ضباط وجنود الجيش (بعضها حرجة) نتيجة سقوط طائرة بدون طيار مفخخة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75782" target="_blank">📅 22:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75781">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228ceb0fe.mp4?token=Z-9Qr97d3Y-THwFVmZjMxKWmq4WVGuhzS-Vls-evXXuGUy8d0Rl-heDDvcB_T6u9xEStZR_t--Rcip_Y5s5PskqCZ7xyBdheeR0MHjpJkQFYC3UUdLqx_k99goCpAcLPlFfFLfZK2vAsiKCNxEoUNJ3_9tzkvLswersS9jvGTZigkL_Gb-1XJYbLg6bJg0wzcTdKmy7xHlGy_Onb1l5QmtpjuGK93CVEMgqG6SD0Q8WEUGSh7FAhMdlImHxayREbmCk2Qp1I5xuCJlR2DYvoA9huWxWC7kPNg_zOas2kkkHdefXAQ3FWnNctm8ncQI33pJ0nFnSkaJ_Ggu2nHynaSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228ceb0fe.mp4?token=Z-9Qr97d3Y-THwFVmZjMxKWmq4WVGuhzS-Vls-evXXuGUy8d0Rl-heDDvcB_T6u9xEStZR_t--Rcip_Y5s5PskqCZ7xyBdheeR0MHjpJkQFYC3UUdLqx_k99goCpAcLPlFfFLfZK2vAsiKCNxEoUNJ3_9tzkvLswersS9jvGTZigkL_Gb-1XJYbLg6bJg0wzcTdKmy7xHlGy_Onb1l5QmtpjuGK93CVEMgqG6SD0Q8WEUGSh7FAhMdlImHxayREbmCk2Qp1I5xuCJlR2DYvoA9huWxWC7kPNg_zOas2kkkHdefXAQ3FWnNctm8ncQI33pJ0nFnSkaJ_Ggu2nHynaSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران حربي منخفض في أجواء محافظة الموصل شمالي العراق.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75781" target="_blank">📅 22:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75780">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌟
الله أكبر.. استهداف قوة مشاة ودبابتي ميركافا تابعة لجيش الإحتلال الصهيوني في بلدة حداثا من قبل أبناء نصرالله.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75780" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75779">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f088d5ca1a.mp4?token=VEisQM6KO4VSo2B9Ich5fxuHaIRxEHis4oWN5j6zBPDunas9xKhp2HQURS3aK5BGBQ6xgxiYo4HJSSD2aGaqdVsT40mWRbkXD0xzgiz_dKtaC3l3Vh1mPjZ5zOi-u6U8eU3JWPqvWbFFUAeHOAH-FkbCmk6YowlxTwz0YztNBLkGazYM1Wt9Hq4Ui48fT5nwFAcM4GjhSGzNKX4SqwmlycJHug4dikxB4oyA6Z_kC9IC3sn_jCSI5xFgoEv6AdpIvyLjlvtKrHAOtqzgSgowwBucDwHvOtJPa97ekNq7jjB62kopKBwUKwG1bhyedbESo9Sp8josMtuIIWrPntQaHCL_9eUjhTupKE29YcWGQXU091FwpPlo4O-I7XQydx5Aqlsrq89eBInx2iLOnz1zpJALz_yH6NDBB3z8qNeqAg9wtRjCJP6b5yYqgK_eyazeXjm5seWlH0b-efc6TvQtlQKMjVxNyFDXckjGJtJlpL6d9VjCI_4oAPyNKsTMr3XIvJqY7y04KWAYmxBzO_w7_k9JXz_cqrUZdTKErU-1ryA2tVsWOe9veQhAB25taBgGrEkFURZdEWLHUXUw4zeVEUFHuXbcTH3bveBDAIc0p9uFOqqvPmkne9js8xkz3KkkfkHqtdRjve9SDnKRBzTmJfDwyq0aiIAgAt5__tvSEQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f088d5ca1a.mp4?token=VEisQM6KO4VSo2B9Ich5fxuHaIRxEHis4oWN5j6zBPDunas9xKhp2HQURS3aK5BGBQ6xgxiYo4HJSSD2aGaqdVsT40mWRbkXD0xzgiz_dKtaC3l3Vh1mPjZ5zOi-u6U8eU3JWPqvWbFFUAeHOAH-FkbCmk6YowlxTwz0YztNBLkGazYM1Wt9Hq4Ui48fT5nwFAcM4GjhSGzNKX4SqwmlycJHug4dikxB4oyA6Z_kC9IC3sn_jCSI5xFgoEv6AdpIvyLjlvtKrHAOtqzgSgowwBucDwHvOtJPa97ekNq7jjB62kopKBwUKwG1bhyedbESo9Sp8josMtuIIWrPntQaHCL_9eUjhTupKE29YcWGQXU091FwpPlo4O-I7XQydx5Aqlsrq89eBInx2iLOnz1zpJALz_yH6NDBB3z8qNeqAg9wtRjCJP6b5yYqgK_eyazeXjm5seWlH0b-efc6TvQtlQKMjVxNyFDXckjGJtJlpL6d9VjCI_4oAPyNKsTMr3XIvJqY7y04KWAYmxBzO_w7_k9JXz_cqrUZdTKErU-1ryA2tVsWOe9veQhAB25taBgGrEkFURZdEWLHUXUw4zeVEUFHuXbcTH3bveBDAIc0p9uFOqqvPmkne9js8xkz3KkkfkHqtdRjve9SDnKRBzTmJfDwyq0aiIAgAt5__tvSEQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: نقوم بتحرير كوبا وعلينا مساعدة الكوبيين فليس لديهم طعام ولا طاقة لكنهم شعب عظيم.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75779" target="_blank">📅 22:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75778">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامب: نقوم بتحرير كوبا وعلينا مساعدة الكوبيين فليس لديهم طعام ولا طاقة لكنهم شعب عظيم.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75778" target="_blank">📅 22:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75777">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d5c56470.mp4?token=TbDEG2PNi8RJFZZniLgj-FvfvuXnSoMHGyyzbV-PIks6qvVsz9KmV0vbDuajYKW9bZQPqWX0Enf1Ds3VCAQC1pyeFT8fECupkqo3PN91yDjRzkycsPoOHZDwOjI9MHUNiaR3giUGzqeCJCmz27sHF-ibS9WfQtR6a4mNafw6pVpUioqNv2tVgwnP5iRY87WBzkgSsZNANb5euCAvYfxyHOK_Cb08SwC1_R-wDf5cUg5KU8oUid6yHvWiuUpFJ5W9u8w0ZI1Blqd8tCJL9GeYsLnyaQIeb-i2HzCw5U2Kseq0YLlpMDLOtjKAwX1jQ5ymqisNbpaUol6s1JS6GL9IMVedmn-RJdV9JP7J832Y_8Vz9gnUQhtY_kbOY-mSnmuAAv5V-TrO0JzuYPIw_XaB1PIlqkCDVGQfCriRxaxmXLmXyWj9tJYndyJm-ZyCdaBK6fwrlgmO0oUCXzjHgLOOk-5aNfFr3cF69fWiAArLknb_wVdDhsHEedPJAeSQdJxK1HrsnJMtVdXcguQOq1OMt6_IQHJoAvnkC4RnQ8jI2BBH2GnsykX1YegMVPA510ohbQEQS2TGQaDhRIwwxvoZ6cKc1fozWCGBuv5kYXWd-wxMrjmfswiPKny00-NQok1O5eLmowihZ3f8BJY2LxXa2S45lCWOXMDlWDu3SjaEcbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d5c56470.mp4?token=TbDEG2PNi8RJFZZniLgj-FvfvuXnSoMHGyyzbV-PIks6qvVsz9KmV0vbDuajYKW9bZQPqWX0Enf1Ds3VCAQC1pyeFT8fECupkqo3PN91yDjRzkycsPoOHZDwOjI9MHUNiaR3giUGzqeCJCmz27sHF-ibS9WfQtR6a4mNafw6pVpUioqNv2tVgwnP5iRY87WBzkgSsZNANb5euCAvYfxyHOK_Cb08SwC1_R-wDf5cUg5KU8oUid6yHvWiuUpFJ5W9u8w0ZI1Blqd8tCJL9GeYsLnyaQIeb-i2HzCw5U2Kseq0YLlpMDLOtjKAwX1jQ5ymqisNbpaUol6s1JS6GL9IMVedmn-RJdV9JP7J832Y_8Vz9gnUQhtY_kbOY-mSnmuAAv5V-TrO0JzuYPIw_XaB1PIlqkCDVGQfCriRxaxmXLmXyWj9tJYndyJm-ZyCdaBK6fwrlgmO0oUCXzjHgLOOk-5aNfFr3cF69fWiAArLknb_wVdDhsHEedPJAeSQdJxK1HrsnJMtVdXcguQOq1OMt6_IQHJoAvnkC4RnQ8jI2BBH2GnsykX1YegMVPA510ohbQEQS2TGQaDhRIwwxvoZ6cKc1fozWCGBuv5kYXWd-wxMrjmfswiPKny00-NQok1O5eLmowihZ3f8BJY2LxXa2S45lCWOXMDlWDu3SjaEcbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
16-05-2026
آلية هامر تابعة لجيش العدو الإسرائيلي في اسكندرونة ببلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75777" target="_blank">📅 22:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75776">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن إستهداف وإسقاط مسيرة صهيونية من طراز "هرمز 450" بصاروخ أرض جو في القطاع الأوسط اللبناني.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75776" target="_blank">📅 22:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75775">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭐️
إنفجار جراء هجوم بطائرة مسيرة انتحارية استهدفت مقر تابع للمعارضة الكردية (الكوملة) في محافظة السليمانية ضمن اقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75775" target="_blank">📅 21:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75774">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTzYc_V8iapvyEub5sAVlQyLWwiJFtPt7bchiA5lJRPUtc-kqI4c6daECOrhkRcrkqkUgJDhoihePe-ytx6_1K2xQIKL3IYmgCZNzUWiLjqqmO4yBvwkxXEG-_qAH3oC-OOLdxc5w58WD3o2HBWzaIgM_QCKCD5CbU8HB4rXqYTILj9uuG0VlBqM_mJwZ4m8UnsrwRJk8beRsCo9p8R985ExeDnp9x5UWHO43dWd7oJ_AoP8R_Diq-pcVZ1bLkzm03ch5kjFxSRXmBMzKWKEzSZ_DFRETSmKY0sIXnYWmQRtymDwQt50ctZoaHnAsB_8GPNiFG-sU4fRVfZNLvD20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إن الأمريكيين، بعد إرسالهم رسالة إيرانية من 14 بندًا قبل ثلاثة أيام، أرسلوا رسالة أخرى إلى إيران عبر وسيط باكستاني. تدرس إيران الرسالة ولم تردّ عليها بعد. يسعى الوسيط الباكستاني في طهران إلى تقريب وجهات النظر بين الرسالتين. لم يتم التوصل…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75774" target="_blank">📅 21:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75773">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الإسرائيلية: نتنياهو يحاول إقناع ترمب بمنح الضوء الأخضر لاستئناف الحرب على إيران.  ‏نتنياهو لم يكن على توافق مع رأي ترامب بشأن التفاوض مع إيران.   ترامب يميل لدعم توجيه ضربة عسكرية لكنه لا يزال يترك نافذة ضيقة للمفاوضات مع إيران.   إسرائيل تتخذ…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75773" target="_blank">📅 21:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75772">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
🏴‍☠️
محرقة جديدة للميركافا.. حزب الله يعلن عن إستهداف 3 دبابات ميركافا وجرافتين D9 تابعة لجيش الإحتلال الصهيوني في بلدة حداثا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75772" target="_blank">📅 21:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75771">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: استهداف دبابة ميركافا وإعطابها بواسطة صاروخ موجه في جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75771" target="_blank">📅 21:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75770">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8a416d9e.mp4?token=JMGXdWhq09skkqNNMd78eGEq1jAri2P2hyrAlJVt3bbFBUIrbujZumCxlP6TemwTkFmXZklFCzmAaXc_SZZRiPFzb3IioJVcDPMwPAEueWhEoJ6m3dvQTyad5kZhoISolVXQHk1i6hE74ZMEsj24TWTR1StyFM2pCg-kyrLCFC4IwlGYLUAar9idQY_Himb5LINa2A4CDoiEX0QVEW4UXtctkwocQhmAvS9-IDBm3X2-DR5Et0hvMfP9UBnRXM6utVTZ9DDi9bMxsdZg-GYwnkguLsyc3obV9dND7qhBUIhrepEQQh5dNfkPniPTkQq4K2DXn_ruu-QlvHtDbnXJRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8a416d9e.mp4?token=JMGXdWhq09skkqNNMd78eGEq1jAri2P2hyrAlJVt3bbFBUIrbujZumCxlP6TemwTkFmXZklFCzmAaXc_SZZRiPFzb3IioJVcDPMwPAEueWhEoJ6m3dvQTyad5kZhoISolVXQHk1i6hE74ZMEsj24TWTR1StyFM2pCg-kyrLCFC4IwlGYLUAar9idQY_Himb5LINa2A4CDoiEX0QVEW4UXtctkwocQhmAvS9-IDBm3X2-DR5Et0hvMfP9UBnRXM6utVTZ9DDi9bMxsdZg-GYwnkguLsyc3obV9dND7qhBUIhrepEQQh5dNfkPniPTkQq4K2DXn_ruu-QlvHtDbnXJRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
نيابة عن شرفاء العالم..
ناشطة تبصق على جندي إسرائيلي أثناء اختطاف نشطاء "أسطول الصمود" السلميين والتنكيل بهم.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75770" target="_blank">📅 21:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏴‍☠️
‏هيئة البث الإسرائيلية: نتنياهو يحاول إقناع ترمب بمنح الضوء الأخضر لاستئناف الحرب على إيران.  ‏نتنياهو لم يكن على توافق مع رأي ترامب بشأن التفاوض مع إيران.   ترامب يميل لدعم توجيه ضربة عسكرية لكنه لا يزال يترك نافذة ضيقة للمفاوضات مع إيران.   إسرائيل تتخذ…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75769" target="_blank">📅 20:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75768">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏ترامب: رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه  متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75768" target="_blank">📅 20:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff7f595ec.mp4?token=U1SXLv8XPWNjjhM8_U2XPYYc3bRyPAMImVrCapP9eQASSQFaY9Lj9uQeMr6-TDkop1RTz62hloFEwi-J3Ttugh3X617tLAlzaxz8ftdGCswhBKBMR-GT4_c_I8mC0WR3bnRBEfj425j7T-yGB5NMRY6ExvmhmhIozUR6NRLGjUyCG50rhaQYpYHHB0URbOqOCVDn-eObnomwUl_RRCoeSX0e631g4WiwVZLmSeFsvzm9_3etGr-HqUbl1dgh57-3B7F5Hfr_oC3BapcyZc-djM_8Rj5_-oQ-Iv-t5L4HCNHBKe9oslsxhS5R4_By1ULf320gVUk-pIGzn8lzu5W2RmWAKW09sfbBd9RelLB9BVBR0UBfCHT2jNrE9aXwhHNWAFdhmDnlO-7uLkSYJ-Boz18a9PxgASZxX9IsakZ5_c-Zm9C1N6e_cn6inJDMBA8SJwWIlvWbTRPzSwW3oH03mjfqHhr4P6Zh5Cp776T5sSR-cGPFoDhFJvMrfCjkQVWzj9M0h4BGXkExvEDRrqF2j3gpWoaqH7x3vUKoVX72zGFX9sVc4hCFREFIaKQRfSefSPz9vyYwT4SBFV2xCbx3SNCO4fhrWN-flsGJIUE74qPZaV-GRkvOc69Y4Nl8vWFeWEa5EmoW9Tma9mj-HcpQtcLdnVw7kpYBJzPZ2hg33XM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff7f595ec.mp4?token=U1SXLv8XPWNjjhM8_U2XPYYc3bRyPAMImVrCapP9eQASSQFaY9Lj9uQeMr6-TDkop1RTz62hloFEwi-J3Ttugh3X617tLAlzaxz8ftdGCswhBKBMR-GT4_c_I8mC0WR3bnRBEfj425j7T-yGB5NMRY6ExvmhmhIozUR6NRLGjUyCG50rhaQYpYHHB0URbOqOCVDn-eObnomwUl_RRCoeSX0e631g4WiwVZLmSeFsvzm9_3etGr-HqUbl1dgh57-3B7F5Hfr_oC3BapcyZc-djM_8Rj5_-oQ-Iv-t5L4HCNHBKe9oslsxhS5R4_By1ULf320gVUk-pIGzn8lzu5W2RmWAKW09sfbBd9RelLB9BVBR0UBfCHT2jNrE9aXwhHNWAFdhmDnlO-7uLkSYJ-Boz18a9PxgASZxX9IsakZ5_c-Zm9C1N6e_cn6inJDMBA8SJwWIlvWbTRPzSwW3oH03mjfqHhr4P6Zh5Cp776T5sSR-cGPFoDhFJvMrfCjkQVWzj9M0h4BGXkExvEDRrqF2j3gpWoaqH7x3vUKoVX72zGFX9sVc4hCFREFIaKQRfSefSPz9vyYwT4SBFV2xCbx3SNCO4fhrWN-flsGJIUE74qPZaV-GRkvOc69Y4Nl8vWFeWEa5EmoW9Tma9mj-HcpQtcLdnVw7kpYBJzPZ2hg33XM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
17-05-2026
تموضع لوجستي تابع لجيش العدو الإسرائيلي في اسكندرونة ببلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75767" target="_blank">📅 20:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75766">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73f31002da.mp4?token=PtRXBY4BfJAGoM696XEKHz7c0aH_lLhRVEYFDEhezlir1QdCYSiSYENmc3USe1p233hplbku0WyG2J0eB18mCXbJ21GK7fucHiF99WyZu0WABf-Jk50pa1BQe_JIM-j50cM9DQVbRr0GOuVGXVjqrZfRKtFT-PsyNGnXfA2SuSQOTcNDNlbZbi3JkZD5Z_f_NZxQCNoMnZRwiNOMkZKjFqTScS--7Q1agf1cKq8x-yE5f1GISxi2VmF_MpQDEEsQ2SRwfeUSoqI5cfY_IjtOHn38RQjrLmajKtRCAe2WvTy-Cq7Pk0P4ymQUIb2bh0z1KcjAClc60Lq3sE-mQBoLoYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73f31002da.mp4?token=PtRXBY4BfJAGoM696XEKHz7c0aH_lLhRVEYFDEhezlir1QdCYSiSYENmc3USe1p233hplbku0WyG2J0eB18mCXbJ21GK7fucHiF99WyZu0WABf-Jk50pa1BQe_JIM-j50cM9DQVbRr0GOuVGXVjqrZfRKtFT-PsyNGnXfA2SuSQOTcNDNlbZbi3JkZD5Z_f_NZxQCNoMnZRwiNOMkZKjFqTScS--7Q1agf1cKq8x-yE5f1GISxi2VmF_MpQDEEsQ2SRwfeUSoqI5cfY_IjtOHn38RQjrLmajKtRCAe2WvTy-Cq7Pk0P4ymQUIb2bh0z1KcjAClc60Lq3sE-mQBoLoYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية تزعم:
في وقت سابق اليوم في خليج عمان، استولى مشاة البحرية الأمريكية من الوحدة البحرية الاستكشافية الـ 31 على سفينة النفط التجارية M/T Celestial Sea، التي ترفع العلم الإيراني، والتي يشتبه في أنها حاولت انتهاك الحصار الأمريكي من خلال العبور نحو ميناء إيراني.
أطلقت القوات الأمريكية سراح السفينة بعد تفتيشها وإصدار الأوامر لطاقم السفينة بتغيير مسارها.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75766" target="_blank">📅 20:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75765">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
نركز حاليا على إنهاء الحرب في جميع الجبهات لا سيما لبنان.
إذا أصر الطرف المقابل على مطالبه المفرطة فإنه يمكن القول إن الدبلوماسية لم تحقق نتائجها.
الحديث عن الإنذارات والمواعيد النهائية بشأن إيران أمرٌ سخيف.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75765" target="_blank">📅 20:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75764">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭐️
رويترز:
بعض السفن تدفع لإيران ما يزيد عن 150 ألف دولار لضمان مرور مضيق هرمز.
‏رسوم عبور السفن لمضيق هرمز لا تفرض على كافة الدول.
‏الآلية الإيرانية الجديدة في مضيق هرمز تعطي الأفضلية للسفن المرتبطة بروسيا والصين.
‏"وثيقة الانتماء" التي تقدم للسفن مقابل عبور هرمز تؤكد عدم ارتباطها بأميركا أو تل أبيب.
‏الدول التي ترغب في عبور سفنها مضيق هرمز يجب أن تتصل بوزير الخارجية الإيراني.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75764" target="_blank">📅 20:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75763">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⭐️
إستمرار موجة الإنسحابات..
النائب "حسن قاسم الخفاجي" يعلن إنسحابه عن تحالف الإعمار والتنمية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75763" target="_blank">📅 20:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75762">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2e4689c.mp4?token=IST5384xqglQ-HyXntWKu6NulbXxF6pYDMo45u59aeO7r8nQeOmsTTeQOKRqK1L2jbSeRWcnpO3tNsD7Hds9RZ85ls_pS1zUcnobW-UYnIlcbWFGfbJdrwscPaue928vHe7kV1f0r5P3HFFapF_Y8Bt9BBgvOXp_Ld4BZu7-VSVrtk5mhIjd-c-502N5YL29lyad-0URTlSc-mrorLgKcCr-EPRYjc6bhsPkJYN5HIWuhD7h8pPkyR2eN0ZBMDC9lOwQlZ2ktG8t6PcqsMHhhtnprudVOkL_6ZPhwgXYML7YAGDGAb9-2CTAZLKiZ_OOcQazCzWRcgwkRXzmhRX9Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2e4689c.mp4?token=IST5384xqglQ-HyXntWKu6NulbXxF6pYDMo45u59aeO7r8nQeOmsTTeQOKRqK1L2jbSeRWcnpO3tNsD7Hds9RZ85ls_pS1zUcnobW-UYnIlcbWFGfbJdrwscPaue928vHe7kV1f0r5P3HFFapF_Y8Bt9BBgvOXp_Ld4BZu7-VSVrtk5mhIjd-c-502N5YL29lyad-0URTlSc-mrorLgKcCr-EPRYjc6bhsPkJYN5HIWuhD7h8pPkyR2eN0ZBMDC9lOwQlZ2ktG8t6PcqsMHhhtnprudVOkL_6ZPhwgXYML7YAGDGAb9-2CTAZLKiZ_OOcQazCzWRcgwkRXzmhRX9Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب: سنمنح ايران فرصة واحدة، أنا لست في عجلة من أمري.  إما أن نتوصل إلى اتفاق مع إيران أو سنقوم بأمور قاسية ونأمل ألا يحدث ذلك.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75762" target="_blank">📅 19:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75761">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
هجوم مسلح من قبل عناصر إرهابية يطال عجلة تابعة للقوات الأمنية في مدينة سراوان بمحافظة بلوشستان جنوب شرق إيران ؛ إستشهاد أحد أفراد الأمن الإيراني كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75761" target="_blank">📅 19:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75760">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
استهداف دبابة ميركافا وإعطابها بواسطة صاروخ موجه في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/75760" target="_blank">📅 19:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75759">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93dd2e141.mp4?token=q0KgjeqFxC2mAJhnM3FwvYnu7lk-RyYiDMAWRDImbIupLQc_etwqBxNjFHv62gNInHcjOXU787h0ZVuaJTU9KFhavgoWRGcMBYNzvCWipdrkalSo9Pi94jWOa22HQD1yK3S4aWV2rO06kdHqNW-ILQuLUKm0j2jWzlF1Y4qoS6K0B7j6ElsNUMZewrgCKwzZFNxYkbm2BKBrRULlkAoN5xYDYE4PUJyZ5Dhi4ISHO93mpyrKwIJxoNKbx4VCHfrGgwEG7Lldu-BY7UQxt6A3Z6LsL4wyh0t-o3WtTqwHNCEdBk_uCKHjOhXvQO3k4bLyCO3caE4ROH89ndgIL36u1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93dd2e141.mp4?token=q0KgjeqFxC2mAJhnM3FwvYnu7lk-RyYiDMAWRDImbIupLQc_etwqBxNjFHv62gNInHcjOXU787h0ZVuaJTU9KFhavgoWRGcMBYNzvCWipdrkalSo9Pi94jWOa22HQD1yK3S4aWV2rO06kdHqNW-ILQuLUKm0j2jWzlF1Y4qoS6K0B7j6ElsNUMZewrgCKwzZFNxYkbm2BKBrRULlkAoN5xYDYE4PUJyZ5Dhi4ISHO93mpyrKwIJxoNKbx4VCHfrGgwEG7Lldu-BY7UQxt6A3Z6LsL4wyh0t-o3WtTqwHNCEdBk_uCKHjOhXvQO3k4bLyCO3caE4ROH89ndgIL36u1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🏴‍☠️
ضمن الإستعدادات العسكرية للعدو الصهيوأمريكي..
مشاهد تظهر العديد من طائرات التزود بالوقود الأمريكية في مطار بن غوريون الصهيوني.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75759" target="_blank">📅 18:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZW_sJ0QcrP3g8he0_npyWNV6ic2L6yFx_XCuollVltsyKVzMVlOnY9XZQhxd83K2f0BJJB-wOXriUXIgICemZuKKYd4iRv_TwK9BEG-_Qfw9I4AhD8nYWO_IUQV5LTENXZxnxl21jTzraKDkOCxOK9UwdwrabfGMUGG4FxPE6IeaU_r74kcuG1i6qX00QG4f-nCeMXPeHvXutz_eKYKBc0V1VWCimftkZML1Ub4J2lDFY8gKQzLrPS_j9wtiolM7zUwuFuaMhIAcjGZE6R6ncYaimcqH0DtBm4WS53kDY57yzaHOsZNEYsByf7Jkr2Eyw6mF8qqO5M5fveR76sULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
من المثير للصدمة أن الجمهوريين احتفظوا بالموقف المهم جدا "البرلماني" في أيدي امرأة، إليزابيث ماكدونو، التي عينها، منذ فترة طويلة، من قبل باراك حسين أوباما والمجنون الشرير المعروف باسم السيناتور هاري ريد، الذي أدار مجلس الشيوخ للدوموقراطيين ب "قبضة حديدية". على مر السنين، كانت وحشية للجمهوريين، ولكن ليس كذلك بالنسبة للدومقراطيين - فلماذا لم يتم استبدالها؟ هناك العديد من الأشخاص العادلين الذين سيكونون مؤهلين لتلك الوظيفة الحيوية.
يلعب الجمهوريون لعبة ناعمة للغاية مقارنة بالدوموقراطيين. إنه أكبر عيب في السياسة. يغش الدوموقراطيون ويكذبون ويسرقون، خاصة عندما يتعلق الأمر بالأصوات في الانتخابات، ولكنهم يلتزمون ببعضهم البعض، في حين يسمح الجمهوريون لإليزابيث ماكدونوز في العالم بالبقاء في السلطة، ووحشيتنا. نحن بحاجة إلى تمرير قانون إنقاذ أمريكا، والآن - وبالمثل، قتل المماطلة، التي من شأنها أن تعطينا كل شيء! إذا لم نمرر واحدا على الأقل من هذين الحكمين بسرعة، فلن ترى رئيسا جمهوريا آخر مرة أخرى. سينتهي الأمر بالدوموقراطيين بولايتين إضافيتين، العاصمة وبورتوريكو، وكل ما يترتب على ذلك، بما في ذلك
4 أعضاء في مجلس الشيوخ، والعديد من أعضاء الكونغرس، والعديد من الأصوات الانتخابية الإضافية، وسيحصلون أيضا على حلمهم في محكمة عليا للولايات المتحدة معبأة برقمهم المفضل - 21 قاضيا.
سيقضي الدوموقراطيون على المماطلة في اليوم الأول الذي يحصلون فيه على فرصة للقيام بذلك.
الجمهوريون لا يفعلون ذلك لأنهم يقولون إن الدوموقراطيين لن يفعلوا ذلك أبدا، لكن الجمهوريين مخطئون. كن جمهوريين أذكياء وصعبين، وإلا ستبحثون جميعا عن وظيفة في وقت أقرب بكثير مما كنتم تعتقدون أنه ممكن!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75758" target="_blank">📅 18:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d89ae9e5.mp4?token=CdwpqpDDeG6FwEEeTTZwHcPlP2LZ7kWZP53Hc38R6P5KeB-GIc9iMZRYMNH9h5h1lVqXO80OA0iv2L8ZkQPG1ar6h2w1xfnoURURraRgQPFBEC8HYd0p9OaeahYH1f8UNFWhkJzCugYkpOSnSrxw4HBznJaRdxoKKTXrXVD6uHXQ3UNpvabDjgbSdpzbe9-v9-ILywEpacXCSFDAQwVquTym_Ay-jVKr0Kew27duXfRo_STs2TB-dNiOfbJT2TeWpexvsnprmg06giJKM9ICqjidPMTaVO6mRh7LkXTNQS3u1QgS8w2jdxjpmcsIiQwr4oAnktDbx4NE_CZFKgwlU0gbNrxDOZgbhmTj-CxL0IWHVhh-HwaaNlYrbrQI4om2OgFyv_WN9-AlerwlXcBU1su-dEZI502aLOKxQv130rnVJRR2ls0AEs5m3_9HCBOTL1_7eAu-jW1PrmjCSf2tBztEeFhQ4QlPzF0tzQ90uHfgBymm9O-7I2sHtLaphbUchTxYCiEWCPlofJToOd1z-J5nPQ2lrmDE-ZTXS5X6ahpaF44GaHWoFY7D0nskNUesXM2jfN0c-sFzVxRgRj7WOCW3IBqmbTbebcykVl5ncnNcoIe_eObNc54dpvNo2jwk1k63Rnhjmmll0eo4oNhoj_3xnhp7VHX1ZINHfFHME78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d89ae9e5.mp4?token=CdwpqpDDeG6FwEEeTTZwHcPlP2LZ7kWZP53Hc38R6P5KeB-GIc9iMZRYMNH9h5h1lVqXO80OA0iv2L8ZkQPG1ar6h2w1xfnoURURraRgQPFBEC8HYd0p9OaeahYH1f8UNFWhkJzCugYkpOSnSrxw4HBznJaRdxoKKTXrXVD6uHXQ3UNpvabDjgbSdpzbe9-v9-ILywEpacXCSFDAQwVquTym_Ay-jVKr0Kew27duXfRo_STs2TB-dNiOfbJT2TeWpexvsnprmg06giJKM9ICqjidPMTaVO6mRh7LkXTNQS3u1QgS8w2jdxjpmcsIiQwr4oAnktDbx4NE_CZFKgwlU0gbNrxDOZgbhmTj-CxL0IWHVhh-HwaaNlYrbrQI4om2OgFyv_WN9-AlerwlXcBU1su-dEZI502aLOKxQv130rnVJRR2ls0AEs5m3_9HCBOTL1_7eAu-jW1PrmjCSf2tBztEeFhQ4QlPzF0tzQ90uHfgBymm9O-7I2sHtLaphbUchTxYCiEWCPlofJToOd1z-J5nPQ2lrmDE-ZTXS5X6ahpaF44GaHWoFY7D0nskNUesXM2jfN0c-sFzVxRgRj7WOCW3IBqmbTbebcykVl5ncnNcoIe_eObNc54dpvNo2jwk1k63Rnhjmmll0eo4oNhoj_3xnhp7VHX1ZINHfFHME78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اعلام العدو تحت بند سمح بالنشر: اصيب قائد اللواء 401، بجروح خطيرة إثر انفجار طائرة مسيّرة مفخخة اخترقت المنزل الذي كان متواجدًا فيه في جنوب لبنان. كما أُصيب معه أيضًا ضابط برتبة مقدم.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75757" target="_blank">📅 18:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الايرانية:
المفاوضات مستمرة عبر وسطاء باكستانيين. ما نريده في الأساس ليس مطالب، بل حقوقنا. قدمت الولايات المتحدة مطالب عديدة، لكن السؤال هو: لماذا ينبغي لإيران نقل يورانيومها المخصب إلى دولة أخرى؟ لم يكن أحد قلقًا بشأن برنامجنا النووي، والجميع يعلم أن برنامجنا النووي سلمي تمامًا.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75756" target="_blank">📅 18:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
‏
ترامب بشأن كوبا:
لن تتسامح أمريكا مع دولة مارقة تمارس عمليات عسكرية واستخباراتية وإرهابية أجنبية معادية على بعد تسعين ميلاً فقط منا.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75755" target="_blank">📅 18:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75754">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
نت بلوكس:
تُظهر المقاييس انقطاع خدمة الإنترنت في معظم أنحاء ‌العراق باستثناء الشمال لمدة ساعتين تقريبًا هذا الصباح. تُقدَّم هذه السياسة، المطبقة منذ سنوات، كوسيلة لوقف التسريب والغش في الامتحانات المدرسية، لكنها تؤثر بشكل غير متناسب على المستخدمين والشركات.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75754" target="_blank">📅 18:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW6Ce05Gt0mCEVo5i6W-3hsL_iW-M3nz7q7v8X-YRHxuyxAhqz8yyB4TTUKgb--oU7RyeUrgWacQPkbsr7qkX6OP8_wc_Qa9QvxCBpA8oVod2agcH1iLf2yfCOPtmWNRx4bBL-QW6WKeZaRnwexopkCmmSHDqggEpZQxJI1uh5v7MUX622dSr2UpErKqm_wlT78WSfc4SQbHL-QBjQf_tvFECkyrVWEfHsUPeOeyb_Mcv9ykPRPYgmZ1ZmXnZcEI_nrHyR-FqV2CP7p51Jjxessat58_0J6qPfhB2MwUFLcLLeplIUYbY9xJaWuJ99vF7UC-8w3qHeUPDEqFE7dNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسالة من مجاهدي المقاومة الإسلامية إلى سماحة الأمين العام لحزب الله الشيخ نعيم قاسم (حفظه الله):
بسم الله الرحمن الرحيم
سماحة الأمين العام حجة الإسلام والمسلمين المجاهد الشيخ نعيم قاسم حفظكم المولى
السلام عليكم ورحمة الله وبركاته
تلقّينا رسالتكم العزيزة وفيها أثر الوالد على أبنائه والقائد على جنوده والشيخ على مريديه.
نشكر لكم يا شيخنا الحبيب مشاعركم الصادقة ومودتكم الخالصة وعاطفتكم الصافية.
ونرد لكم التحية، بتحيّةٍ ملؤها إيمان وسنامها جهاد ومآلها نصر وشهادة.
كما نتوجّه بإجلالٍ وتعظيمٍ إلى أرواح الشهداء من إخوتنا المجاهدين وأهلنا الأوفياء، الذين أدهشوا العالم بصبرهم وثباتهم وصمودهم، وكانوا وما زالوا الحصن المنيع على الفتن والسند المتين في ذورة المحن، ظهر المقاومة في ميدان الدّفاع عن الوطن ضدّ الاحتلال الصّهيونيّ الغادر والهمجي.
أيها الأمين المفدى، إن أبناءك المجاهدين في المقاومة الإسلامية قد راهنوا على الله تعالى قبل حمل البنادق، وامتثلوا لأمره وتوكّلوا عليه ونزلوا سوح الوغى مسدّدين بالصّبر ومؤيّدين بالمدد من عنده، وهم في كل يوم يسطرون ملاحم التصدي الكربلائي ويلاحقون العدو بكافة أنواع أسلحتهم، يدمّرون دبّاباته ويحرّقون آلياته ويرعبون جنوده ويلقّنون جيشه دروساً ستُحفر في ذاكرته المصطنعة، ويبقون الوطن عصياً على القهر والإحتلال.
يا شيخنا، لقد فتحت قيادتكم الشّجاعة الطّريق أمام سلسلة من العمليات التي جعلت العدوّ منهكاً، يتهيّب الاستقرار فوق التّراب الجنوبيّ، قد أدمن النظر إلى السّماء، مترقّبا صلياتنا ومسيراتنا، واعتاد تنكيس رأسه في الأرض، مذعورًا من عبواتنا وكمائننا. عهدنا ما عهدتم إلينا به: سنبقيه على هذه الحال ولدينا مزيد؛ لن نهدأ ولن نستكين ولن تقر لنا عين حتى يرحل الاحتلال عن أرضنا مهزوماً خائباً، وبيننا وبينه أيامٌ لن يصبر على مدتها وسنصبر، لأننا أهل الأرض، وليالٍ مظلمة في عين المحتل أضأناها بذكر الله، وميدانٌ سيحصد منه أشلاء القتلى والجرحى، بعد أن زرعناه بالبارود والنار.
باسم حبات التّراب، باسم كل شهيد، وكل مجاهد في تشكيلات المقاومة المتأهبة على امتداد جبهة المواجهة، نجدد لكم الولاية والقسم والبيعة، بالاستمرار على هذا النّهج حفاظًا على العزّة والحرية والكرامة والإستقلال؛ فحياة الأوطان لا تُكتسب إلا بالتضحيات الحمراء، وشرف الجنوب يأبى أن يتحرّر إلاّ على أيدي المقاومين، ولن يخيب عليهم رهان إن شاء الله تعالى.
والسّلام عليكم ونصر الله وبركاته
أبناؤك مجاهدو المقاومة الاسلامية
الأربعاء 20-05-2026 م
03 ذو الحجّة 1447 هـ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75753" target="_blank">📅 18:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75752">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الاعلام السعودي يزعم: العمل جار بجدية على وضع اللمسات النهائية على نص اتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75752" target="_blank">📅 17:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75751">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الاعلام السعودي يزعم:
العمل جار بجدية على وضع اللمسات النهائية على نص اتفاق بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75751" target="_blank">📅 17:44 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

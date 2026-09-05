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
<img src="https://cdn4.telesco.pe/file/pN92NQ0T26amhuP1boo27BF9terOd49sZsj359y8-SBbR_RTkx6DMeCssEBkfokW2n9wqpq6zLLbpTCrmDMM8DFE-VPvVppJZ3SxavpIgtlGqkRn1dB3qi6fVlFn0DIWTAkXSflUIZLqFyNfZ6LiND6aMhvwKvvNntUieLnq8NIBNHv9zWO5GJ32I9Ob72VwitZJdiuK6eL6i60INtO44iNqEjWSLzZxzxTkFcz9anIMQOG2DOtb4BW95wv9pIf4hvf7gQDnOSwmlHQREBCl0RVNSv9jfnADtBwb_nf2NnVs9yc3ZMfoxowo4QjQL9oqE9gKQgdAmE0qC5ZuMzFdmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 01:59:55</div>
<hr>

<div class="tg-post" id="msg-89445">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔻
الحرس الثوري:
شنّت القوات الجوية التابعة للحرس الثوري الإسلامي هجومًا بصواريخ باليستية متعددة على حاملة طائرات ومدمرة تابعتين للجيش الأمريكي المعتدي، الذي كان يضايق السفن الإيرانية ويشارك في الحصار البحري.
اضطرت هاتان السفينتان الحربيتان إلى مغادرة منطقة النزاع بعد تعرضهما لأضرار وخشية هجوم جديد.
اضطر العدو المعتدي، الذي دأب على إطلاق ادعاءات كاذبة في مرتفعات الجولان لسنوات، إلى الاعتراف رسميًا اليوم بتعرض سفينتين حربيتين تابعتين للبحرية الأمريكية لهجوم.
إن اعتراف القيادة المركزية الأمريكية (CENTCOM) بهذه العملية دليلٌ قاطع على الهزيمة الاستراتيجية للعدو، وبرهانٌ على القوة الهجومية للحرس الثوري الإسلامي.
يدافع الحرس الثوري الإسلامي، إلى جانب القوات المسلحة الأخرى للجمهورية الإسلامية الإيرانية، بحزمٍ وحزمٍ عن الأمة الإسلامية الإيرانية.
إن الحضور المجيد للأمة الإسلامية على الساحة، والقتال الدؤوب للمقاتلين الإسلاميين الأشداء، يحولان دون تحقيق العدو لأهدافه الشريرة.
إذا استمرت الأعمال العدائية والعدوانية، فعلى النظام الأمريكي أن يتوقع ردودًا قوية من القوات المسلحة للجمهورية الإسلامية الإيرانية. نحن أقوى من أي وقت مضى. النصر حليف الأمة الصامدة للجمهورية الإسلامية الإيرانية، والهزيمة والندم مصيرٌ محتوم للمعتدين.</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/naya_foriraq/89445" target="_blank">📅 01:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89444">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
مصدر أمني لنايا:
دخول رتل عسكري أمريكي إلى بغداد قادماً من محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/naya_foriraq/89444" target="_blank">📅 01:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89443">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
مشاهد مرئية لاستهدافات المباشرة للحرس الثوري للسفن المخالفة في مضيق هرمز.</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/89443" target="_blank">📅 00:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89442">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f593e4ec53.mp4?token=vdgyHUnNiOnFsqyov6NZPLEvbX0ESV60yCPm-7Hq6dSlTCA25z64n4-H82bUwrAwQUT99Rey0Yc65HuKVAOAkh4MN_54ntMWRIXWRJnkPkXi5ZRd4JN1Zp-ckOqR7NhaS0ABP9XgDi3FpT1BSNeOdT-wk5zC6bksJgZSpuRIZfDr-BwTda5r44VX6LT_kdeJKYpASarLyhnc-3wghgTWpJv67FW6FGGMPu3ffOt5wuIR01T4tqHwzo7zrTQ0szJqOKwuPTitZ-aY7yOv_eU8mYlP7hxg0i_jfDNFv9Ei-Dc_aRVWqT3CxwTrWW7Mvdg-UynUFD1FMHImByffxa8S9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f593e4ec53.mp4?token=vdgyHUnNiOnFsqyov6NZPLEvbX0ESV60yCPm-7Hq6dSlTCA25z64n4-H82bUwrAwQUT99Rey0Yc65HuKVAOAkh4MN_54ntMWRIXWRJnkPkXi5ZRd4JN1Zp-ckOqR7NhaS0ABP9XgDi3FpT1BSNeOdT-wk5zC6bksJgZSpuRIZfDr-BwTda5r44VX6LT_kdeJKYpASarLyhnc-3wghgTWpJv67FW6FGGMPu3ffOt5wuIR01T4tqHwzo7zrTQ0szJqOKwuPTitZ-aY7yOv_eU8mYlP7hxg0i_jfDNFv9Ei-Dc_aRVWqT3CxwTrWW7Mvdg-UynUFD1FMHImByffxa8S9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
‏هل حدث شيء ما في محطة رأس لفان للغاز الطبيعي المسال في قطر؟ تُظهر صور الأقمار الصناعية اليوم ظاهرة غير طبيعية لا تبدو كغيوم. رُصدت طاقة حرارية قدرها 80 ميغاواط صباح اليوم على جهاز VIIRS، كما رصد القمر الصناعي Terra طاقة حرارية قدرها 120 ميغاواط قبل أربع ساعات.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/89442" target="_blank">📅 23:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89441">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh8eOcvOnrsozNS9OSctDrA4r9zVc862pj91tEh5UfY594tcDhwxn4WjSUo0ekgk9hCJa6lSkSrKJs3WvgHXHmqNEaMicsK_0UEt8wYGRc8ECUJmQuKnjDYpG_SopBmD-nz3nOysZ8m8GdeTro09NLYP5Qm-DTP-swSfS_aSS9jqM8QsOlW0Rk1w4Dlnc9muDr2GfrK7eFLffF8GNsdUZNqqi9QJfuJDBUSBB85YON8dHP6US9ti945c2uUoeyrTK8bRhHx9LbK2iQr00vn5mdJYuMxubFH68oAW6POe9v4Me3KNfQXuJM3TdoJRxVtD0iY30X2gmE5Rh8u9t6ji4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🔻
انتحار جندي احتياط إسرائيلي يبلغ من العمر 46 عامًا وله أطفال، أنهى حياته نتيجة لصدمة نفسية من الحرب مع حزب الله .</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/89441" target="_blank">📅 23:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89440">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/89440" target="_blank">📅 23:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89439">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ee9026ad.mp4?token=o04xNlSF2uqKDikXjQ7F2Wdi3BTKHxHxBIChfZJn38j1jwhQCQSks_Ny7qrQoQt37kR9EFXMU8sYMK1lAhWWymZ_gr8KwWmRIL6dKEmRrfHE65wHYJ7AxOx9DxDtkaSwlhssIMrfLKLhGy3lc7CT_rEgB941xGKBympaW2eHkl776YUz02yVYpv8Wc9s5i9kcqJeC_4YhARjsufUZxBOhQ2isYRHC861zECy_at-ZYfPsxNEG_5QuONdDthuKCbhtRtrsmb2UYQVIW-taYUJa15lBgcSSIMlDx9xOF-SLtIORlxBSmemQFcjlYdOxNTsJK1CQNbVEo7NubmJzOvPrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ee9026ad.mp4?token=o04xNlSF2uqKDikXjQ7F2Wdi3BTKHxHxBIChfZJn38j1jwhQCQSks_Ny7qrQoQt37kR9EFXMU8sYMK1lAhWWymZ_gr8KwWmRIL6dKEmRrfHE65wHYJ7AxOx9DxDtkaSwlhssIMrfLKLhGy3lc7CT_rEgB941xGKBympaW2eHkl776YUz02yVYpv8Wc9s5i9kcqJeC_4YhARjsufUZxBOhQ2isYRHC861zECy_at-ZYfPsxNEG_5QuONdDthuKCbhtRtrsmb2UYQVIW-taYUJa15lBgcSSIMlDx9xOF-SLtIORlxBSmemQFcjlYdOxNTsJK1CQNbVEo7NubmJzOvPrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔻
القوات البحرية للحرس الثوري الإسلامي:
تحذير شديد اللهجة من قائد القوات البحرية للحرس الثوري الإيراني: لا تنخدعوا بأمريكا؛ أي تحرك مشبوه سيتم استهدافه.
ردًا على عدوان الجيش الأمريكي الإرهابي الذي هاجم ثلاث ناقلات نفط تابعة للجمهورية الإسلامية الإيرانية
القوات البحرية للحرس الثوري الإسلامي:
أيها الشعب الإيراني البطل المستقيم؛
هذا الصباح، قام الجيش الأمريكي الإرهابي العدواني، في عمل وحشي ويائس لإغلاق مضيق هرمز، بمهاجمة ثلاث ناقلات نفط تابعة للجمهورية الإسلامية الإيرانية، مما أدى إلى إلحاق أضرار بها.
استهدفت البحرية التابعة للحرس الثوري الإيراني، بعون الله وتوفيقه، وبدعمكم ومساندة الشعب البواسل، وامتثالاً لآية القرآن الكريم: "وَمَنْ يَعْتَدْكُمْ فَاعْتَبُوهُ بِمَا يَعْتَدْكُمْ"، ثلاث ناقلات نفط في ممر مضيق هرمز غير المصرح به، وثلاث سفن تابعة للولايات المتحدة الأمريكية في مناطق أخرى.
وعقب هذا العمل، تُوجه البحرية التابعة للحرس الثوري الإيراني تحذيراً شديد اللهجة لجميع السفن الموجودة في الخليج العربي وبالقرب من مضيق هرمز: لا تنخدعوا بالجيش الأمريكي الإرهابي، وتجنبوا أي تحركات مشبوهة لعبور الممرات المائية غير المصرح بها، وإلا ستكونون هدفاً.
والنصر من عند الله العلي القدير الحكيم.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/89439" target="_blank">📅 23:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89438">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9d45912a.mp4?token=BEkZR4Og5iCOW3hhfxe3Hwn_iLoFZAOMG6n__vqp7p0JEAF012h81DJzNgrujl29Jow8kpKEQhr8L0RMrKnXKyGFREjyneE5QJi4Ss36ppJoDfUgCs8ltWpFoX83iMD3xMRABQf3XNznmU4J41AJ5sEQO9hRgngp_bX_VMcPljrgUsFxThLzXKx4GDH8VqfUjxF_eddh1TTjK-QFK5ylR1r8vEy62OpRFX9YoQj-Zogs2NkDfnAUp9pj_ajwZsIU2VSsRAEGh6KEWSleQMomyN68aIvQ3_ldERXF9bgcPj6nNb0rR4jdlzpyl_HuPERYZ4-SQUIoy7RxssH3TNL15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9d45912a.mp4?token=BEkZR4Og5iCOW3hhfxe3Hwn_iLoFZAOMG6n__vqp7p0JEAF012h81DJzNgrujl29Jow8kpKEQhr8L0RMrKnXKyGFREjyneE5QJi4Ss36ppJoDfUgCs8ltWpFoX83iMD3xMRABQf3XNznmU4J41AJ5sEQO9hRgngp_bX_VMcPljrgUsFxThLzXKx4GDH8VqfUjxF_eddh1TTjK-QFK5ylR1r8vEy62OpRFX9YoQj-Zogs2NkDfnAUp9pj_ajwZsIU2VSsRAEGh6KEWSleQMomyN68aIvQ3_ldERXF9bgcPj6nNb0rR4jdlzpyl_HuPERYZ4-SQUIoy7RxssH3TNL15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇮🇷
نتنياهو حول إيران:
إذا لم نتخذ إجراءات ضد إيران، لكانت إيران اليوم تمتلك قنابل نووية تهدف إلى تدميرنا.
الآن، سيحاولون مرة أخرى. إنهم يحاولون مرة أخرى، وسيحاولون مرة أخرى إعادة بناء التحالف الذي حطمنا.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/89438" target="_blank">📅 23:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89437">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇱
🇸🇾
جيش العدو الإسرائيلي يطلق قذائف صاروخية باتجاه حدود الجولان المحتل عقب رصد مجموعة من الشبان يُشتبه بمحاولتهم زرع عبوة ناسفة في المنطقة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/89437" target="_blank">📅 22:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89436">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89436" target="_blank">📅 21:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89435">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اصابة عدة سفن مخالفة في مضيق هرمز</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/89435" target="_blank">📅 20:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89434">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
الانفجارات في جزيرة قشم ناتجة عن اطلاقات صاروخية نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89434" target="_blank">📅 20:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89433">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
جيش العدو الإسرائيلي يستعد لتقليص قواته في جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89433" target="_blank">📅 20:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89432">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
دوي انفجار في جزيرة قشم.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89432" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89431">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
دوي انفجار في جزيرة قشم.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89431" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89430">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b07a20cb6.mp4?token=m6qvWkaZh3YSq3Vj6TdX1HFjDz06oEhl1IIefwmCd7eZfefrIvBuz1dlmasIWOBD75nlDg1d9k0P9ra2PrQgXUA5wK9NSs1oOumEl94s8BQF8c7dHs1LEDzBWN_TDx-egWMUnaU0ZJOKBee92OBaoghYf1w3g7bHuMNemz0wpXiIkf_mp3rSfExsbZPE_CdXXSIY7HS5dW5Gl5X-lcO35RjffbYaIMoV34l-m3glrhPqdAb_w4rvm-gzjbPcw4-iQ4Jxcqb29hC_TcXduicUDr8fKdofJAP4HiejS4eW79SIAD2BX2MUrt6VUSxepmKR6fjgwwg3U08PDlLInt0LPVYY5bjdGUKc-paFqSH3VO5PLAbA1yRTU6kZ1Pxjsh0_0HJUywd37rACtPiGjRn9BDOVvfcnyPa3R5RRxol-GzvvYf_KL_sRiyayrRkyn-B_FSwqFrE-r5z8jbyBtTnACNEDwS_FL59oGNaHJYNYH-tEtZ5gnBlcX_KYpE--E81SKpo2oug8v6H1xiWc7nn987Sl_7ypFx2kmlOEdBafZcVtkdkCdkvRoypOhEjdGYGHrXvKCQi0A45uXii3Is9r9-a9PLecBb0s66Ofet3vSLbMSp-9EbVfTuE4H24bQY8c3KSuZhf5yzdZEzB_bDhSinr5rRo2hy7qsVRC4k4UVxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b07a20cb6.mp4?token=m6qvWkaZh3YSq3Vj6TdX1HFjDz06oEhl1IIefwmCd7eZfefrIvBuz1dlmasIWOBD75nlDg1d9k0P9ra2PrQgXUA5wK9NSs1oOumEl94s8BQF8c7dHs1LEDzBWN_TDx-egWMUnaU0ZJOKBee92OBaoghYf1w3g7bHuMNemz0wpXiIkf_mp3rSfExsbZPE_CdXXSIY7HS5dW5Gl5X-lcO35RjffbYaIMoV34l-m3glrhPqdAb_w4rvm-gzjbPcw4-iQ4Jxcqb29hC_TcXduicUDr8fKdofJAP4HiejS4eW79SIAD2BX2MUrt6VUSxepmKR6fjgwwg3U08PDlLInt0LPVYY5bjdGUKc-paFqSH3VO5PLAbA1yRTU6kZ1Pxjsh0_0HJUywd37rACtPiGjRn9BDOVvfcnyPa3R5RRxol-GzvvYf_KL_sRiyayrRkyn-B_FSwqFrE-r5z8jbyBtTnACNEDwS_FL59oGNaHJYNYH-tEtZ5gnBlcX_KYpE--E81SKpo2oug8v6H1xiWc7nn987Sl_7ypFx2kmlOEdBafZcVtkdkCdkvRoypOhEjdGYGHrXvKCQi0A45uXii3Is9r9-a9PLecBb0s66Ofet3vSLbMSp-9EbVfTuE4H24bQY8c3KSuZhf5yzdZEzB_bDhSinr5rRo2hy7qsVRC4k4UVxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇸
الكرملين
: بوتين يبدأ محادثات مع المبعوثين الأمريكيين الخاصين ويتكوف وكوشنر.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/89430" target="_blank">📅 20:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89429">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇶
اغلاق قناة NRT المملوكة لعائلة عبد الواحد المعارضة للبرزاني في محافظة دهوك شمالي العراق من قبل مجاميع مسلحة بسبب نشر تقرير عن الوضع المعاشي السيء في دهوك.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89429" target="_blank">📅 20:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89428">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8076d542b.mp4?token=fyNfVnanjnpmDdh8awFWzZHlidX0QPsJIgyxN2_-a0U4hMikyMqkBQWr2U_O2TTCqndZVRSxOZA_4GDOJGIubo17U0JAia8KguwTjS5JxC-MDbKaIW20bvkxy74C3iapjIN4xkaYwt5bWTn3PKvq_avq6FTmnsW7Vlx3AY7dmPHZL6J1f8Lf4DCP0QHvav0IwbejNhSNnrDWpm87144eD7r3qeE-HBJ6IjApQ7kCzwAVFiyTjAE90vU2jd6Ej47Q0IgwIpMAi0-PdELaI330xggaXavk6D79xDmfjdLjlFTX0tsOMSaXMhDfQEMiuR7ko4ACTG5pgUq43KfqAVXKYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8076d542b.mp4?token=fyNfVnanjnpmDdh8awFWzZHlidX0QPsJIgyxN2_-a0U4hMikyMqkBQWr2U_O2TTCqndZVRSxOZA_4GDOJGIubo17U0JAia8KguwTjS5JxC-MDbKaIW20bvkxy74C3iapjIN4xkaYwt5bWTn3PKvq_avq6FTmnsW7Vlx3AY7dmPHZL6J1f8Lf4DCP0QHvav0IwbejNhSNnrDWpm87144eD7r3qeE-HBJ6IjApQ7kCzwAVFiyTjAE90vU2jd6Ej47Q0IgwIpMAi0-PdELaI330xggaXavk6D79xDmfjdLjlFTX0tsOMSaXMhDfQEMiuR7ko4ACTG5pgUq43KfqAVXKYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد آنية من مضيق هرمز تُظهر تكدّس ناقلات النفط بانتظار أوامر الحرس الثوري للسماح لها بالعبور.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89428" target="_blank">📅 20:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89426">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c1784708.mp4?token=b55OK3Sg6VSQ7WNteuHqf9EuWogEqRCdhv9FKxhe4bHwtrzcykQYwJPgJ-rAsRmNolc_wahKca4G4BuWhYm_kw4RELa2kPIhdxxdNqok75KFwjSqKgt2Bp5huxCeBXSoCZtt3RwWvZxC3B0i1G8O9auj0uQO42uqHp0THYOccQV0iFToDA9TtVdol0seMm4d38OHR6Q8T2LSmm6aQljTpDQBzlYvTtdqRodcJxDfqmjaaRzPDWKLsnjyz-dVR4Ib3iBXTOmofUdwx3kQhf-g-JnIGecmh70r5mJ_S7YC1KA4GEdWor2i1awuDQW6Fh0z5j4Uh_BqS4yh5PvLydqz4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c1784708.mp4?token=b55OK3Sg6VSQ7WNteuHqf9EuWogEqRCdhv9FKxhe4bHwtrzcykQYwJPgJ-rAsRmNolc_wahKca4G4BuWhYm_kw4RELa2kPIhdxxdNqok75KFwjSqKgt2Bp5huxCeBXSoCZtt3RwWvZxC3B0i1G8O9auj0uQO42uqHp0THYOccQV0iFToDA9TtVdol0seMm4d38OHR6Q8T2LSmm6aQljTpDQBzlYvTtdqRodcJxDfqmjaaRzPDWKLsnjyz-dVR4Ib3iBXTOmofUdwx3kQhf-g-JnIGecmh70r5mJ_S7YC1KA4GEdWor2i1awuDQW6Fh0z5j4Uh_BqS4yh5PvLydqz4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
الاعلام العبري: تقارير أولية عن عملية إطلاق نار في مستوطنة نتانيا.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89426" target="_blank">📅 19:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89425">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
تقارير أولية عن عملية إطلاق نار في مستوطنة نتانيا.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89425" target="_blank">📅 19:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89424">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3-Wl7ZPArtAednpyk0kRUSCpdCfw8RP_A4TphzeGfKyiu0YsNXMO1A8I0mRuMToaHW2Yfj3YuBN-aJH7U2ELaINZ2OKT1DyGc2zLWv7Wk66T1ZMrctgN1Epw-ZLIQbG7OTgsg7KDISD1_W0oeVh04X7Cp0iEasxmB86Izc5KhlZLM0lIll5JoZlT7BkngpmD2uW-NTCFILW_5NnMnc4kgXrBeS3gWGX2wkuYZcaS0bVnTx6LIwznlPzXwn16lDGqJtwbQk3LP9HaExY92XxhgTI-0aTVDFyLIak_ESpbhWPSe5vatxDmMpkjyk4a0svrvXn38Td1Q9KtV1jCfPcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات اخرى قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/89424" target="_blank">📅 19:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89423">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انفجارات تستهدف ناقلة شمال الخليج الفارسي قرب السواحل العراقية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89423" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89422">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عدة احداث بحرية في الخليج</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/89422" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89421">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حدث بحري</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/89421" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89420">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حدث بحري</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/89420" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89419">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
السفارة الامريكية في البحرين:
نظرًا للتوترات في الشرق الأوسط، لا تزال البيئة الأمنية معقدة مع احتمال حدوث تصعيد غير متوقع.
تُذكّر السفارة الأمريكية المواطنين الأمريكيين بأن إيران استهدفت سابقًا بنية تحتية مدنية في البحرين، بما في ذلك فنادق في المنامة.
يجب على الأمريكيين الموجودين حاليًا في الشرق الأوسط توخي مزيد من اليقظة والانتباه إلى احتمالية إلغاء الرحلات الجوية وإغلاق المجال الجوي واضطرابات السفر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89419" target="_blank">📅 17:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89418">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية تزعم:
شنت قوات القيادة المركزية الأمريكية (سنتكوم) غارات جوية على ثلاث ناقلات نفط خام إيرانية في الخامس من سبتمبر/أيلول، بعد أن أطلق الحرس الثوري الإيراني صواريخ باليستية باتجاه سفينتين حربيتين تابعتين للبحرية الأمريكية كانتا تقومان بدوريات في المياه الإقليمية.
نجحت حاملة طائرات أمريكية ومدمرة صواريخ موجهة في تفادي عدة هجمات إيرانية غير مبررة. ولم يُصب أي من أفراد القوات الأمريكية بأذى.
وعقب فشل الهجمات الإيرانية، عطلت قيادة سنتركوم بشكل دائم ناقلتي النفط الخام التابعتين للحرس الثوري الإيراني، وهما ناقلة النفط "داوني" قبالة سواحل جزيرة خارك، وناقلة النفط "ستارك 1" بالقرب من جاسك. كما دمرت القوات الأمريكية بالكامل ناقلة النفط الخام الفارغة "كيلو" (المعروفة أيضاً باسم "نوكسن") في خليج عُمان، حيث استهدفت السفينة في عدة مواقع حيوية لإخراجها عن الخدمة بعد أن صدرت الأوامر لطاقمها بإخلاء السفينة</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/89418" target="_blank">📅 17:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89417">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1cI0YFPT3xntZwU6Lhx1nww5VtAyLy_dte7RR_VrP6mV_GmcaObBaXgqlWHhJZMqxwNNWTU6y7aP5tV3OFq6S_3H_DYqXzYi2dOw4deGnh-VCkaKlln9OUzAcechxfr92ktIE_JC2mPcKtCALf9nRpFIO28qRiWsWia9s0cm-CF1JiqLotANZY7k9900EO6XZ8dAbW81cr0u2eVAeo7iDMsz2OWtutfOJvzACw9SMJm3y4Tbre-6bEfML09xS7sG1dJ3GxEkuV7-OtNYmdXXB-zeU-HnEXhgTHvNrezKTnBMjy4OAtDWwIphAyx10hBnWYcR1ZtBPTgnVe1wEI-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
بعد انتهاك السيادة من قبل اغلب دول العالم.. طائرة عسكرية ايطالية تحلق في الاجواء العراقية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/89417" target="_blank">📅 15:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89416">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇷🇺
بوتين يصدر أمرًا بعدم شن هجمات على كييف لمدة ثلاثة أيام وذلك في إطار التحضيرات لاستقبال الوفد الأمريكي.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89416" target="_blank">📅 15:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89415">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESqiFr9GiXT5_dXsrrYec8WothM9MunXgKLf5X-RBQUoqFvHae4Tw2c5sJn9GdRp6WTFZz-NKpv76AyLyRLH_Sg4TGytfhagTQf6fLSs1TIA1mZ2232J7eQzEk6OMw_F3EOZNflWYhWjq1adC0xBVTs1dlMOG6XoDIDvg17RcUx70GohO4lJBuw85o5gZzvxrXO1XEGyXC67KOhEz-l4vCulcjnptl_ydrmeu805ykoFkqokWggLOi3bUFEFakq-N5dOYJFfo7lnaRewGkRQOpon60-vEHbCv7MWJuTVJ2RN6Qw3gnZbvgyhKetCldBe1w49M6PxDQGkYTsoqjuibQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات الامنية العراقية تلقي القبض على غسان الجميلي شقيق عدنان الجميلي المدان بقضايا فساد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/89415" target="_blank">📅 15:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89414">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
🇱🇧
بيان صادر عن حزب الله حول العدوان الإسرائيلي المتمادي على لبنان:
يواصل العدو الإسرائيلي تصعيد عدوانه وإجرامه بحق لبنان، قتلًا وقصفًا وتدميرًا وتفجيرًا ممنهجًا للمنازل والقرى، ومحوًا لمعالمها، ونسفًا لكل مقومات الحياة فيها، دون رادع وبذرائع واهية، وقد أدى عدوانه الإرهابي يوم أمس إلى ارتقاء أربعة شهداء وسقوط عشرات الجرحى، في ظل صمت دولي مطبق وتواطؤ أميركي فاضح، ووسط غياب تام للسلطة اللبنانية عن تحمل مسؤولياتها، وإصرار مخزٍ منها على الاستمرار في خياراتها الخاطئة ونهجها التنازلي والاستسلامي وإطارها الذي يدوسه العدو كل يوم، والذي لم يجلب للبنان سوى العار والخزي، ولم يؤدّ إلا إلى تكريس الاحتلال واستمرار العدو في عدوانه وإجرامه بحق اللبنانيين.
إن هذا العدوان المدان والمستمر بشراكة وغطاء وتخطيط أميركي كامل، لا مبرّر له سوى الضغط على السلطة اللبنانية وابتزازها لدفعها إلى تنفيذ أجندات باتت معروفة الأهداف ولو كان الثمن إغراق لبنان في مستنقع فتنة داخلية. وإن استمرار السلطة في اللهاث خلف هذا المسار العبثي وغير الشرعي وغير الدستوري، يعطي العدو غطاءً لاستمرار عدوانه، ويمنحه مزيدًا من الوقت لتحقيق أهدافه وفرض شروطه وإملاءاته على لبنان.
إن ادعاءات السلطة أن مفاوضاتها المباشرة العقيمة واتفاق الإطار المشؤوم مع العدو يحقق إنجازات، يسقطها ويبددها استمرار الاحتلال والعدوان وسفك دم اللبنانيين والتدمير والتفجير. وإن الإفراج عن بعض الأسرى اللبنانيين، على أهميته، لا يمكن أن يكون غطاءً للتغاضي عن استمرار العدوان والاحتلال والقتل، ولا مبررًا للاستمرار في مسار أثبت فشله وعجزه عن حماية لبنان وشعبه، فيما سبق للسلطة أن أكدت مرارًا من أنها لن تذهب إلى أي مسار تفاوضي قبل وقف العدو لعدوانه.
إن السلطة مدعوة إلى إعادة حساباتها والتوقف عن المكابرة، ووضع العناد والمناكفات جانبًا، لما فيه مصلحة لبنان وشعبه، والعودة إلى الثوابت الوطنية الجامعة التي تحمي سيادة لبنان. وإننا ندعو جميع اللبنانيين إلى الوقوف صفًا واحدًا خلف موقف وطني موحّد يحفظ قوة لبنان ومنعته وسيادته في مواجهة العدوان الإسرائيلي.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89414" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89413">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتن ياهو يزعم احباط عملية لاغتيال نجله</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89413" target="_blank">📅 14:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89412">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتن ياهو: لقد هاجمت قطر - كما قمت بقصفها وهاجمتها خلال الحرب، وهم هاجموني. كل هذه القضية المتعلقة بقطر هي مجرد تلاعب. قطر دولة معادية، ولكن قطر ليست دولة فرضت أي شيء هنا.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89412" target="_blank">📅 14:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89411">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية تتوعد مستخدمي الذكاء الاصطناعي لصنع فيديوات خادشة للحياء أو تحتوي على كلمات وإيحاءات لا تمتَّ بصلة إلى ثقافة وأخلاق المجتمع العراقي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/89411" target="_blank">📅 14:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89410">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نتن ياهو: لقد هاجمت قطر - كما قمت بقصفها وهاجمتها خلال الحرب، وهم هاجموني. كل هذه القضية المتعلقة بقطر هي مجرد تلاعب. قطر دولة معادية، ولكن قطر ليست دولة فرضت أي شيء هنا.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/89410" target="_blank">📅 14:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89409">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتن ياهو يتوسل لانتخابه: من سيُنهي ما يجب أن يُنهى؟ من سيُنهي هذا النظام في إيران؟ من سيُنهي حزب الله؟ من سيُنهي حماس؟ خصومي السياسيون يستسلمون لكل ضغط. أمريكا تقول لهم "لا"، وهم يرتجفون على الفور. هل سيفعلون ذلك؟ لا. لن يفعلوا ذلك. نحن سنفعل ذلك.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89409" target="_blank">📅 14:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89408">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee42d895b.mp4?token=TgHD-MnXdIFoomtQDIi17WY-K-hXYrfHWNkI-s07lm38MPWvYFV13mNGq2rIwbqYCiaJwDN8dmquqhCHZeaTDd3wJmWMv4DTwNc7POaGLuj7s_7GJMR7onpqAf1j8-ZENjmI7g3wwiWNPz2r_Cat4o5L5ajMpXXlOR1HkihHOqhuKtNwsJuMZoXZ52eVfxpacCyjZApFL-lHYp81kzXb9feciMN3xWMqVV7ANiS8zdxs2NaMddiRRirrmkgMmliE2ueKKQyxy0kYRquHiYNa9X-vRIlAOxk9FLf1os40xS_GlSMyV3dw7Nv5FzS0mKob6JT6zyj57a83mSCpBqnzkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee42d895b.mp4?token=TgHD-MnXdIFoomtQDIi17WY-K-hXYrfHWNkI-s07lm38MPWvYFV13mNGq2rIwbqYCiaJwDN8dmquqhCHZeaTDd3wJmWMv4DTwNc7POaGLuj7s_7GJMR7onpqAf1j8-ZENjmI7g3wwiWNPz2r_Cat4o5L5ajMpXXlOR1HkihHOqhuKtNwsJuMZoXZ52eVfxpacCyjZApFL-lHYp81kzXb9feciMN3xWMqVV7ANiS8zdxs2NaMddiRRirrmkgMmliE2ueKKQyxy0kYRquHiYNa9X-vRIlAOxk9FLf1os40xS_GlSMyV3dw7Nv5FzS0mKob6JT6zyj57a83mSCpBqnzkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أزمة البنزين تتوسع في العاصمة العراقية بغداد وطوابير الوقود تمتد إلى مسافات طويلة</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89408" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89407">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
العراق يعلن نجاحه في تفكيك مخيم الهول السوري ويعلن اغلاقه قريبا.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/89407" target="_blank">📅 14:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89406">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fa90f779.mp4?token=HBLH7jF92faQ_ZWht-eorpOTSVWUJY5OVP41hWbcivIOn69toDzqYniJ1ONuhzHgvsRmGHYCVR3MqDiY_xMma3XEywhlD7XTViHNLdZSE9VOSALAgS7Yw0suxUHIHCwGuCGczg3hbjp25SYOGjiB8GwVo9cD6-WRo8UvHwfmhz8McrgSkX8B1qVEtBJ7tBizxwbXYwYqm2U-KsMtLTKEu7k0g9KWF2pMmIykDOfFlrUOWYeZIf97Eo0_V0zBgUGXZmKbsv9-FN26MhtmtTqTXVeh9Aq_8Tm1aT49QJMpAV6K0phz6JuVi0tjLrnHQstUCZeKzqHNTgidUn8igjsInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fa90f779.mp4?token=HBLH7jF92faQ_ZWht-eorpOTSVWUJY5OVP41hWbcivIOn69toDzqYniJ1ONuhzHgvsRmGHYCVR3MqDiY_xMma3XEywhlD7XTViHNLdZSE9VOSALAgS7Yw0suxUHIHCwGuCGczg3hbjp25SYOGjiB8GwVo9cD6-WRo8UvHwfmhz8McrgSkX8B1qVEtBJ7tBizxwbXYwYqm2U-KsMtLTKEu7k0g9KWF2pMmIykDOfFlrUOWYeZIf97Eo0_V0zBgUGXZmKbsv9-FN26MhtmtTqTXVeh9Aq_8Tm1aT49QJMpAV6K0phz6JuVi0tjLrnHQstUCZeKzqHNTgidUn8igjsInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
طائرة عسكرية امريكية تهبط في مطار اربيل الدولي شمالي العراق.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89406" target="_blank">📅 13:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89405">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇵🇰
البرلمان الباكستاني وللمرة الأولى في تاريخ البلاد يمنح قائد الجيش عاصم منير سلطة قيادة رسمية على جميع القوات المسلحة الثلاث: الجيش والبحرية والقوات الجوية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/89405" target="_blank">📅 12:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89404">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9faa2ed76c.mp4?token=NQjlIynnDcqgfUWBp5ofzE5lvJRJ2j_SaJpO5pd1jyEF9blfLUc-loVIScq-ugK1ZW7KQ-p03FQVbHf1g1MgbuVulPdkW9wYJnr9-hjOcX_hJmkLdykvQsTZY314F_ofv1jITpLW5H816rqNEynzvFNapFvzG9hZF3esfebkRK9eEgZSHBwD1mczvo6YDDOLeq6baZljUKGfUM4o1JOsFNiwVTOAHChTizLjcyU2bzSGrUqNBla8PCrBTNX0Oht6B4U5GdfK3Rv9T_qznx0EwNwuinil65xmYA7mV1ohAnBJ76FKunRd6_jV61I_hIxbam2RePbZ2aiTKatf89ZcoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9faa2ed76c.mp4?token=NQjlIynnDcqgfUWBp5ofzE5lvJRJ2j_SaJpO5pd1jyEF9blfLUc-loVIScq-ugK1ZW7KQ-p03FQVbHf1g1MgbuVulPdkW9wYJnr9-hjOcX_hJmkLdykvQsTZY314F_ofv1jITpLW5H816rqNEynzvFNapFvzG9hZF3esfebkRK9eEgZSHBwD1mczvo6YDDOLeq6baZljUKGfUM4o1JOsFNiwVTOAHChTizLjcyU2bzSGrUqNBla8PCrBTNX0Oht6B4U5GdfK3Rv9T_qznx0EwNwuinil65xmYA7mV1ohAnBJ76FKunRd6_jV61I_hIxbam2RePbZ2aiTKatf89ZcoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
زيلينسكي:
روسيا استهدفت مطارين في كييف و بوريسبيل قبيل وصول ويتكوف وكوشنر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/89404" target="_blank">📅 12:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89403">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5042640b.mp4?token=oRoy8gDYS01s1HgQp3ONfNnEOA3xeXo-XtbVg3wMHZDYLnD55Ts8aL94xYDnSndNsIa01qiDKIbrWfOvGMDvZpKF61_lQGrBXXEMAvsUs6QksQyC7IerGdIvCFnuzPNEIXdlPz_Te6afnG-ynXG0oLIfCdjWSj4zAsYSim0ZDPEH6PtljEpWzpp-IbW9M-rBVMRf4rdtwCuHbELxb6-aBSXBatwq7Bfw2-o53WOiiHxw4kl5OjbrCStUVMmeNYKVS4h42TepuyTB3KlLwPFBOsoAk0FkpfHwxfP2gNnS-z5Pa6ToDffevac904P573HcD4Hru-McUIf_lBSaE7-3olU0H2pEbWOXO85f-2t_eO53b5PV-lKjPksqXZsIE-qpMpCV-ICtrXKTHQxDts29unyYP6JW-d2uNnGUx-4XPCjRQTba3k9sAdjcgijDcv-UNOiqMZ-Rpl58fVgcjbFP9uQYuifHc-dzcDXcfkXne2S8ZvK1rsO0SHlZOpoL78nQGWb2oqhC0X1p1gZVMW6MwhU6haE_9gHxm2KQQG1MReZZCN0_ZXhXOAfaweNeYDW5GAgKon3e4PQp_PNBvvytszgLTw-jrZNQ1mI5OMELBfwNALExvfvpasBgl9shWQh7w1h9rRBC8n3JogfSkBUWu_hBDyhWb7gXRYybcTMLhOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5042640b.mp4?token=oRoy8gDYS01s1HgQp3ONfNnEOA3xeXo-XtbVg3wMHZDYLnD55Ts8aL94xYDnSndNsIa01qiDKIbrWfOvGMDvZpKF61_lQGrBXXEMAvsUs6QksQyC7IerGdIvCFnuzPNEIXdlPz_Te6afnG-ynXG0oLIfCdjWSj4zAsYSim0ZDPEH6PtljEpWzpp-IbW9M-rBVMRf4rdtwCuHbELxb6-aBSXBatwq7Bfw2-o53WOiiHxw4kl5OjbrCStUVMmeNYKVS4h42TepuyTB3KlLwPFBOsoAk0FkpfHwxfP2gNnS-z5Pa6ToDffevac904P573HcD4Hru-McUIf_lBSaE7-3olU0H2pEbWOXO85f-2t_eO53b5PV-lKjPksqXZsIE-qpMpCV-ICtrXKTHQxDts29unyYP6JW-d2uNnGUx-4XPCjRQTba3k9sAdjcgijDcv-UNOiqMZ-Rpl58fVgcjbFP9uQYuifHc-dzcDXcfkXne2S8ZvK1rsO0SHlZOpoL78nQGWb2oqhC0X1p1gZVMW6MwhU6haE_9gHxm2KQQG1MReZZCN0_ZXhXOAfaweNeYDW5GAgKon3e4PQp_PNBvvytszgLTw-jrZNQ1mI5OMELBfwNALExvfvpasBgl9shWQh7w1h9rRBC8n3JogfSkBUWu_hBDyhWb7gXRYybcTMLhOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇦
بسبب زيارة كوشنر صهر ترامب لأوكرانيا   ‏تم أمر وحدات من قوات الأوكرانية المدعومة من الناتو بالالتزام بنظام الصمت على الخط الأمامي من الساعة 00:00 يوم 5 سبتمبر إلى الساعة 23:59 يوم 8 سبتمبر ..</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89403" target="_blank">📅 12:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89402">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2665ced0fb.mp4?token=apE6ex1zZnl16EJlv_q8Wf0zehfKtvspjYTRJScbBZeurBdAd65d254oIfXBLMOFmvkHKOsNTRUOTar4Bc170McVWuDZaXLPctBSXXKSUFSlA2kgDSfRrsimngjypz3ucCXGTTwRglaLsEqRLoFOTEdIBWiAyWo-Z4XbXyzemOxCAQ9jAWiTL7Uf08_b67YDW1FXshJLAUqZYtw2DOyXcAQ77AB0SUsXnLt2Tno-B6rIFZoZZ_DroPpcr2SyOE27m6RTEFIAUY_jJKpkb4i4oRhDXsTGo3Kx0e1oev3bIosameiEAjol_ZIt_MKDjFaoNsLVSE18kLC9zI1uRIlOSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2665ced0fb.mp4?token=apE6ex1zZnl16EJlv_q8Wf0zehfKtvspjYTRJScbBZeurBdAd65d254oIfXBLMOFmvkHKOsNTRUOTar4Bc170McVWuDZaXLPctBSXXKSUFSlA2kgDSfRrsimngjypz3ucCXGTTwRglaLsEqRLoFOTEdIBWiAyWo-Z4XbXyzemOxCAQ9jAWiTL7Uf08_b67YDW1FXshJLAUqZYtw2DOyXcAQ77AB0SUsXnLt2Tno-B6rIFZoZZ_DroPpcr2SyOE27m6RTEFIAUY_jJKpkb4i4oRhDXsTGo3Kx0e1oev3bIosameiEAjol_ZIt_MKDjFaoNsLVSE18kLC9zI1uRIlOSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة خارج.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/89402" target="_blank">📅 11:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89401">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇷🇺
🇺🇦
دخول اتفاق وقف إطلاق النار المحلي في منطقة محطة زابوريجيا النوويةحيز التنفيذ.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/89401" target="_blank">📅 11:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89400">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
مصدر امني ايراني...
الانفجارات في محافظتي طهران واصفهان ناتجة عن تفجيرات مسيطر عليها.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/89400" target="_blank">📅 10:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89399">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة خارج.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/89399" target="_blank">📅 10:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89398">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
نيويورك تايمز:
تحقيق مع نحو 50 عضوا في هيئة الأركان المشتركة بشأن تسريب معلومات للصحافة عن حرب إيران.
التحقيق مع العسكريين يتركز على تسريب معلومات عن تراجع مخزون الجيش من الذخائر الحيوية.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/89398" target="_blank">📅 04:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89397">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇦
زيلنسكي يتوسل: أدعو روسيا لوقف هجماتها على أوكرانيا خلال زيارة المبعوثين الأمريكيين ويتكوف وكوشنير إلى كييف الأحد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/naya_foriraq/89397" target="_blank">📅 00:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89396">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇱
🔻
جيش الاحتلال يدعي اعتراض مسيّرة أطلقها حزب الله باتجاههم في جنوب لبنان.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/naya_foriraq/89396" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89395">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اصوات انفجارات في سيريك</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/89395" target="_blank">📅 23:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89394">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اصوات انفجارات في سيريك</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/naya_foriraq/89394" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89393">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8295dd1410.mp4?token=kYHTtLAQFbIatex5fLRHS2crHIQcCmJuWgUAODRoTSmXtrFbFKONtoq8hCwp91ArGzdbQn_VoAU5N3KXLM244X-Wdzh2FMrA8LdQ-YjVgd3W6MIscQp5zXMrRDFx98OlX9C690G6VaustKQ_Wk6HFTO2KAF589AeOwPexGhups76xgyX_tyumRIa7bq_-x1dJiqj_8spZUfvzKN0EbuVUWcTG8rCrXkiJD6iYCgj_Y0NcUkcL0j40NqfI1gVuHHtSt3VSMng3URtlgBuxGxZNzerNewp08V2CnZZIWk9rxIe78BhOftV0qM5unbFDdDZtC6EmWUEsmrlwlYp6QPW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8295dd1410.mp4?token=kYHTtLAQFbIatex5fLRHS2crHIQcCmJuWgUAODRoTSmXtrFbFKONtoq8hCwp91ArGzdbQn_VoAU5N3KXLM244X-Wdzh2FMrA8LdQ-YjVgd3W6MIscQp5zXMrRDFx98OlX9C690G6VaustKQ_Wk6HFTO2KAF589AeOwPexGhups76xgyX_tyumRIa7bq_-x1dJiqj_8spZUfvzKN0EbuVUWcTG8rCrXkiJD6iYCgj_Y0NcUkcL0j40NqfI1gVuHHtSt3VSMng3URtlgBuxGxZNzerNewp08V2CnZZIWk9rxIe78BhOftV0qM5unbFDdDZtC6EmWUEsmrlwlYp6QPW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب: أتحدث إلى بوتين، وهو لا يسعى إلى مهاجمة حلف شمال الأطلسي (الناتو)، ويتكوف وكوشنر سيقدمان مقترحًا لإنهاء الحرب في روسيا.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/naya_foriraq/89393" target="_blank">📅 22:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89392">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94f4f649a5.mp4?token=Dt-u3ob18boO9cMenvdXkWd2z7lQmF-29Go_i55sjXhoi-HWXZgVWChQEF6C893DhC8Hmz3mj2yDxcMgopy6lGVONl1h0TOlYIaud_ubO3UJqa40_9XKyL-JZfw35AT8bdQTim9aTYmWX-sdHd4GV7x3Gr8PP456hMmHxekNT1fbq2cWALobzEcwo-Aqfg8Z3qZ1zn2DDLJqFIyT9A9TnS_k7_jIR4gjVLNIf5dZPevOr_iMej5njxwHmtgD5yxwd29Awx6sK6iyetcZnYXOn30vJhUdDnL4TXjbu4KqdBOJrWs0Ml2rpAthO8yN2EH6XtyvpHlnk4L5f6YTFzQ46Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94f4f649a5.mp4?token=Dt-u3ob18boO9cMenvdXkWd2z7lQmF-29Go_i55sjXhoi-HWXZgVWChQEF6C893DhC8Hmz3mj2yDxcMgopy6lGVONl1h0TOlYIaud_ubO3UJqa40_9XKyL-JZfw35AT8bdQTim9aTYmWX-sdHd4GV7x3Gr8PP456hMmHxekNT1fbq2cWALobzEcwo-Aqfg8Z3qZ1zn2DDLJqFIyT9A9TnS_k7_jIR4gjVLNIf5dZPevOr_iMej5njxwHmtgD5yxwd29Awx6sK6iyetcZnYXOn30vJhUdDnL4TXjbu4KqdBOJrWs0Ml2rpAthO8yN2EH6XtyvpHlnk4L5f6YTFzQ46Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب: قد نضرب "جبل الفأس" قريبًا جدًا.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/89392" target="_blank">📅 22:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89391">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7cc3a576.mp4?token=ll6ZQpEfpGz7GnYoTKOtwG7ILletFZ31OzEuePJFhVDONGB_2_Zz6tktESUykw95ZUoTN_pn6K6CpKn26ueRMfDcYEe-0jxN5Z_Lddz3YyGr7TD3mue2bK3uCpOzkK5mSnOqLe6f2ScKAyYP-ncDDhNoJf1pCIGbtYGJjBw1g8SIkIaVCuHFfwmhgDz0zBwHWLpX1r9pjZuJOfvmrwBynyzF_XmY-DHkphG-Tpyhfc3YDHC6W1BQLgMi5eOol-wD1FHT9YAd75Voj7PLA6W4eO6oiylfQtA-xW4PSgsNQ5GlgYa8VwfzNuYQJvwrkzO3j_D13Uel9lhgCmhOiKqGIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7cc3a576.mp4?token=ll6ZQpEfpGz7GnYoTKOtwG7ILletFZ31OzEuePJFhVDONGB_2_Zz6tktESUykw95ZUoTN_pn6K6CpKn26ueRMfDcYEe-0jxN5Z_Lddz3YyGr7TD3mue2bK3uCpOzkK5mSnOqLe6f2ScKAyYP-ncDDhNoJf1pCIGbtYGJjBw1g8SIkIaVCuHFfwmhgDz0zBwHWLpX1r9pjZuJOfvmrwBynyzF_XmY-DHkphG-Tpyhfc3YDHC6W1BQLgMi5eOol-wD1FHT9YAd75Voj7PLA6W4eO6oiylfQtA-xW4PSgsNQ5GlgYa8VwfzNuYQJvwrkzO3j_D13Uel9lhgCmhOiKqGIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: إذا لم يكن الصراع مع إيران حربًا، فما هو بالضبط؟  ترامب: أصفه بأنه صراع عسكري لأننا نعتبره أمرًا بسيطًا بالنسبة لنا؛ إنه ليس شيئًا كبيرًا،  نقوم بشنّ ضربات متقطعة في إيران. نحن نستهدف كميات كبيرة من النفط، الحرب مع إيران أمر بسيط بالنسبة لأميركا.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/89391" target="_blank">📅 22:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89390">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd38aba6f.mp4?token=PipMGAD914V7X3oeQkqKlD6mS3KipXOchERMBB2FGbLqhKWah-bNy-L-X4dnYCzTz4Y5GrhNZZu54v9XkNPOr4oHAIZ4a-xupHKeqiswNIo4f6zCOXBfkTZS2qjkVuDC9f0kWzqK-8EXXDsnBPKRFV_WpVR5hAfn5aCP-vW5msYtTxkivF8qPcPm-cUv27vUtY1BJfWxGRBchzRYXTL_NiwMThaomGJy3dl0yQiqzLNZgjMDH0i-mhe2Lyp7Fvx-z1FiIP7LdJoWzu0FdkGoUjOfjxq-rjsm03MM_SgIGH4o-lUYoirLIfrPwiOu_rfibj2IawEOhShbNCwjlDGk74i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd38aba6f.mp4?token=PipMGAD914V7X3oeQkqKlD6mS3KipXOchERMBB2FGbLqhKWah-bNy-L-X4dnYCzTz4Y5GrhNZZu54v9XkNPOr4oHAIZ4a-xupHKeqiswNIo4f6zCOXBfkTZS2qjkVuDC9f0kWzqK-8EXXDsnBPKRFV_WpVR5hAfn5aCP-vW5msYtTxkivF8qPcPm-cUv27vUtY1BJfWxGRBchzRYXTL_NiwMThaomGJy3dl0yQiqzLNZgjMDH0i-mhe2Lyp7Fvx-z1FiIP7LdJoWzu0FdkGoUjOfjxq-rjsm03MM_SgIGH4o-lUYoirLIfrPwiOu_rfibj2IawEOhShbNCwjlDGk74i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل
: إذا لم يكن الصراع مع إيران حربًا، فما هو بالضبط؟
ترامب
: أصفه بأنه صراع عسكري لأننا نعتبره أمرًا بسيطًا بالنسبة لنا؛ إنه ليس شيئًا كبيرًا،  نقوم بشنّ ضربات متقطعة في إيران. نحن نستهدف كميات كبيرة من النفط، الحرب مع إيران أمر بسيط بالنسبة لأميركا.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/89390" target="_blank">📅 22:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89389">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihlXusTkUxv0uItBhOiCw0E2HQRnE4U6FAK8d5ZJUoHsNYOyJJ-HixDcY8QB5Q-JOoNlCJTjNDtP7uBT1KykiWVCpgoQu-CmL8QdosqCMHAUTS6rEmbklDECH7C5tWyExX41DtvUYXuIvJqoxjak9Srvg6_gbIWgWhrZPKnSIxW-NMV4gZwY5-WjaRVqlmAI7uC4wqeJLqqKzaYW6zs47zTJ_1TTbSeqNj7MZbRjDmI9AMkVyuh3rGw2wBl8t_97u7v3bS3JjkJ4UvhsjTtVBOvSJni3c-VRc20aBlZajeWDSRMCWaJmayhZG1oBUDQZutji0K4a3CZGIABGeRJuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حشدُ الله.. حُماةُ الأرض، حُماةُ العراق.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/89389" target="_blank">📅 22:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89388">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
🇺🇸
‏
الخارجية الأميركية:
صفقة طائرات هليكوبتر بيل 412 إلى العراق تقدر بـ 150 مليون دولار ‌.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/89388" target="_blank">📅 21:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89387">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127f5c1af7.mp4?token=Z18IhhXDTKKqZb_q92aFORmFHQmNcii1YImj9h1oanaGMaFL-Yw-15w7zDrN5G1pWe3fBSUSVWjQOrl80poVWvqkZQmoSThoTQsw2-lLBKGLEtDTtUxLYQ2PT2-nOdxeXnhAbHYTXPkTAqD1G1mqYSAx_I3cf-tAlK2LdtnCViBJ5iaqASmwNSFXoaD0S_agzTp2kkqfcBMjh6yMB2zLgHUZWH8vPwd2iXKSC05e5As5uapHW2l1M9adtHA05aEqC6YPAV1m0PAYSOszsk8TzRjETN30PD66fuof8AzTPvsblbcIZLi6qxXiOqSMgpzeeTIzSZ2CMR_jBAC2KBW8vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127f5c1af7.mp4?token=Z18IhhXDTKKqZb_q92aFORmFHQmNcii1YImj9h1oanaGMaFL-Yw-15w7zDrN5G1pWe3fBSUSVWjQOrl80poVWvqkZQmoSThoTQsw2-lLBKGLEtDTtUxLYQ2PT2-nOdxeXnhAbHYTXPkTAqD1G1mqYSAx_I3cf-tAlK2LdtnCViBJ5iaqASmwNSFXoaD0S_agzTp2kkqfcBMjh6yMB2zLgHUZWH8vPwd2iXKSC05e5As5uapHW2l1M9adtHA05aEqC6YPAV1m0PAYSOszsk8TzRjETN30PD66fuof8AzTPvsblbcIZLi6qxXiOqSMgpzeeTIzSZ2CMR_jBAC2KBW8vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات قوية تسمع في الاردن</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/89387" target="_blank">📅 20:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89386">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">موجة انفجارات جديدة في سماء قاعدة الأزرق بالأردن</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/89386" target="_blank">📅 20:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89385">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/89385" target="_blank">📅 20:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89384">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7oJ3N8mbiZglohbE9JKosD1YMRdm6JvHRPDCUrUPWKut4BQUqG4mI8yV5aoxqyZI2bhcblJN-wEa3dwMeKQ41qv_vIPzIuWX1O0cmrv2bJPPKHPRu7QVdWrdIczzlh5P6GngAJ251RvZCb8ewiNeAr53s3OXB-XAoKpxApmGM0LZQNiQfeMH7xEaukEbxPkWHTftyvje9-xHBYicPw4shwDn9__53nlHLmwqotvDdGUsskH8UofWXAVxZu5TZlmC1WRDwQUFRFmQ7ljwbuamQKoJdXY6BI99v4qUOUDLoy2DOPDHcOlqabOWFq_M5MKNvaDUnWHEquOoKn4OG-d4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاق صاروخي من ايران</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/89384" target="_blank">📅 20:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89383">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇷🇺
طائرة روسية مسيرة تشن غارات على مقر جهاز الأمن الأوكراني (SBU) في كييف.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89383" target="_blank">📅 20:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89382">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3MyLEcO1tJzGhnIlz4wkWe1s0-cU0cqvlqeeMqb8cwzSjAiEix-LeO31jIxiv6vnObZtC5b_I57sqV7wJ3MqjawhzC9vOViihReENS7CS8Va44Q3Vh7tk0fBCmunCfSs7g_LjjrGdMGdyCeyFkhRUWS3umSuPkxZd5489ZGvrZIDM8K-odAVcm8H5Hk6KKY3fDSJ2aHELpmuPI_WpcCZHBKkzD7vxk6nx08lZwFRAsqlJjtMSs3gjhyM-n36S0bUIHF9bQDx1-JtVStJYhFIEfh4HZSZ_5mU5MMcWg1PYxIxi3CWsYZPXiZNbu6IfFBg50arscp2oLuw7toN8h27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
قاليباف
: ‏إن تركيز الصين على تعزيز الأمن المشترك يعكس مبدأً لطالما دافعت عنه إيران.‏يجب على دول المنطقة أن تتولى زمام مستقبلها بنفسها، ولن يتحقق الاستقرار الحقيقي إلا من خلال بنية أمنية جديدة محلية المنشأ. إيران على أهبة الاستعداد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/89382" target="_blank">📅 20:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89381">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c44ad22364.mp4?token=tYeEsi76kvjJlO9T5XfHlY-ix1V7_qXY_y8DLJKs70gjS1933P1SChfn-fGnAoYTIUEtwCR_IxczBY_mIzHdT-sNmTtLtvQEBcuYq-Lcz06H1sl1LOHqhxlhWZLGgCeJGyQ5FJe-CnbJFEzvDkP5mWgFqTd_ollml0qo3hQuRueMU3tC14VRxGmmSmMAtvU12lrN7EvunigPdxe0RD4Mp60SfyLVFU0HwlPQL-cSKOtuYvwuSX0P-GnyjmmZsjHJW0IX8CmGFGCNa3NENDqPNRsykOberw_pXpbhcmmrspT-lknbGg8tCMueH83jYN1Bi6KdWhMIDRqbMOqd-cgq0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c44ad22364.mp4?token=tYeEsi76kvjJlO9T5XfHlY-ix1V7_qXY_y8DLJKs70gjS1933P1SChfn-fGnAoYTIUEtwCR_IxczBY_mIzHdT-sNmTtLtvQEBcuYq-Lcz06H1sl1LOHqhxlhWZLGgCeJGyQ5FJe-CnbJFEzvDkP5mWgFqTd_ollml0qo3hQuRueMU3tC14VRxGmmSmMAtvU12lrN7EvunigPdxe0RD4Mp60SfyLVFU0HwlPQL-cSKOtuYvwuSX0P-GnyjmmZsjHJW0IX8CmGFGCNa3NENDqPNRsykOberw_pXpbhcmmrspT-lknbGg8tCMueH83jYN1Bi6KdWhMIDRqbMOqd-cgq0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق صاروخي من ايران</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/89381" target="_blank">📅 20:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89380">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/89380" target="_blank">📅 20:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89379">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الصواريخ الايرانية تصل الى الاردن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/89379" target="_blank">📅 20:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89378">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇦
زيلنسكي يتوسل:
أدعو روسيا لوقف هجماتها على أوكرانيا خلال زيارة المبعوثين الأمريكيين ويتكوف وكوشنير إلى كييف الأحد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/89378" target="_blank">📅 19:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89377">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMabcS0FvVamltsrGElwm00Q9fedfcf0rW3glpQtL63aGszGs3GG1hBa2yhEZ-ycBZSTs6Bel8dmrORUluGn1ebDu6QOZYArw75wjs0rtR6ON18ahPDoIDCH7BAbhfPYzCFS_N76WAmJxYVyLRHUfIIMi8ZA2D_miTRWq8lNN1M3KXmYphNlpF7pPH_ErpyaX7GlFY7z4H-ZpZX8n3P-AV4Tjkyn4zWI486jbpL2WR-mB7YXcJlS1aQtBCpY3VXmm9OI0d0hEQ2dJHsnkyxmPX4gUyhjwa_TwKmN_p6CjvKbybzCkV6Kx440Nkdz8bbkepYn_otUPDOLT0dm6xHKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
يفضل المتطرفون اليساريون والديمقراطيون والشيوعيون أن نخسر الحرب في إيران على أن يربح الرئيس دونالد ج. ترامب الحرب من أجل أمريكا. بعبارة أخرى، يفضلون أن نخسر على أن نربح! هؤلاء أشخاص مرضى للغاية يعانون من متلازمة جنون ترامب الخطيرة، والتي يشار إليها أحيانًا باسم متلازمة جنون ترامب.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/89377" target="_blank">📅 19:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89375">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
‏تسعى الولايات المتحدة، في أعقاب الأضرار الجسيمة التي لحقت بطائرات MQ-9 Reaper المسيّرة وتدميرها خلال النزاع مع إيران، إلى إيجاد بديل أقل تكلفة لهذه الطائرات.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/89375" target="_blank">📅 19:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اطلاق صاروخي من ايران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/89374" target="_blank">📅 19:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
دبلوماسي إيراني:
أي استهداف للبنية التحتية الإيرانية من القواعد الأميركية في الدول الإقليمية سيواجه برد من إيران.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/89373" target="_blank">📅 18:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
مجلس نقابة المحامين العراقيين يقرر منع قبول انتماء المقيمين بصورة دائمة في إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/89372" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89370">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d722832d1c.mp4?token=T6ru1qwUT52bI2I0XoCYBkCX22b-MxqhXmuJxLHxEjxBel03lJVBDlX5N4FSHYFMRC6mpgxoZNXBnm0P6m6_2ofl4qT29hF1VhmP6R5RpRzfFTFGNEEtPsjFOZ-mpeOvZc1nYEvTqyjwQH1ti_GcZRwqcd2geiaVxK0jtLZvyMP-_qy5vgoeVL-E2_9kOUVrxa9dloAn48xGuN6w6y1hmW4NjXhjTgtQ7MQQF4zm9pIix7i7DAW1nPgZ2XkT3AnBGJhIh38My3hyAbaQPprHL0AQWhZfAmiCYfBE4n_P3qe6IObReXkIHxL4-EjRotGt0JHk6U-EC3HKKgCSVGoM5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d722832d1c.mp4?token=T6ru1qwUT52bI2I0XoCYBkCX22b-MxqhXmuJxLHxEjxBel03lJVBDlX5N4FSHYFMRC6mpgxoZNXBnm0P6m6_2ofl4qT29hF1VhmP6R5RpRzfFTFGNEEtPsjFOZ-mpeOvZc1nYEvTqyjwQH1ti_GcZRwqcd2geiaVxK0jtLZvyMP-_qy5vgoeVL-E2_9kOUVrxa9dloAn48xGuN6w6y1hmW4NjXhjTgtQ7MQQF4zm9pIix7i7DAW1nPgZ2XkT3AnBGJhIh38My3hyAbaQPprHL0AQWhZfAmiCYfBE4n_P3qe6IObReXkIHxL4-EjRotGt0JHk6U-EC3HKKgCSVGoM5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء عن اطلاق صواريخ باتجاه مضيق هرمز</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/89370" target="_blank">📅 18:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89369">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snGIusx4DXPOHurK28NczsnzNtlbLKOrTID075ghH30v0XMneahZdq3tEjvPUY2ZIOmP07A3tD3d1Ue7lJEi_wl6vuTixJso1bJahsRaqsRZThSQsiKbw_8usPsikvGE567wMceZDmHUT24D6dVbi9zboDJy3aHcsXOHTtilt_tAXccCHoqNOL1TuZuXYQ8RGKNIdm6bMKxcvKX0MKazdyPZKmoJU04HO0V2Raed8kyJuPE7KQJt4ozdQnNCt38An9MBBmQdHu6_DB7z1s-z4O4CU4tiToh8v2xq_4u1pM5N-R820jvtUOf00LlphSCWT5Nh0kH4Blse7H3bHk8LFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
منصات التتبع:
‏لم تُرصد أي سفينة اليوم تعبر مضيق هرمز عبر المسار "الآمن" للولايات المتحدة  ويمكن رؤية ثلاث سفن فقط، سبق أن تعرضت لهجوم إيراني مهجورة وراسية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/89369" target="_blank">📅 17:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89368">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية تعلن تحقيق أعلى معدل صادرات وواردات منذ اندلاع الحرب في آب الماضي حيث وصل التصدير قرابة 70 مليون برميل.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/89368" target="_blank">📅 17:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89367">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الولايات المتحدة تفرض عقوبات جديدة مرتبطة بإيران تستهدف ثلاث جهات</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/89367" target="_blank">📅 17:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89366">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الولايات المتحدة تفرض عقوبات جديدة مرتبطة بإيران تستهدف ثلاث جهات</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/89366" target="_blank">📅 17:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89365">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇱
اعلام العدو:
يعتقد أن إيران وحماس تكثفان جهودهما لمهاجمة صهاينة في الخارج قبل الأعياد اليهودية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/89365" target="_blank">📅 17:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d7c563a.mp4?token=M4yRXe2OPHrXnpMzIEq6l8AilwojjRwrJQyVfZ5P6thrAK5lP_oBHqTawlsQAe6qsO9ab8q7vyKlfinnHU1NSt-2_MDqxCEUjS5jPrsTHP62LvD083z_fEyrqBH70_R28lZcfEU-D1iCyPDUGnAqrVYLGAtr_zyi4ggI9RlOfudL6Lwg12y7YwGDz7e6zB1s_C94KjXDg17RDKLwHoCXMdJ_SeXbBgwxXavdMgyEG1HCuWHK4o6laMdSy8nWbTwjkzf0xwcsMaH0m45TNpls-pjrFRtHdksgnE29CF1Gy3Cc-d5ZArouiWQOhvciKMFVUHFNGdXLbuvF4z-yDdzppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d7c563a.mp4?token=M4yRXe2OPHrXnpMzIEq6l8AilwojjRwrJQyVfZ5P6thrAK5lP_oBHqTawlsQAe6qsO9ab8q7vyKlfinnHU1NSt-2_MDqxCEUjS5jPrsTHP62LvD083z_fEyrqBH70_R28lZcfEU-D1iCyPDUGnAqrVYLGAtr_zyi4ggI9RlOfudL6Lwg12y7YwGDz7e6zB1s_C94KjXDg17RDKLwHoCXMdJ_SeXbBgwxXavdMgyEG1HCuWHK4o6laMdSy8nWbTwjkzf0xwcsMaH0m45TNpls-pjrFRtHdksgnE29CF1Gy3Cc-d5ZArouiWQOhvciKMFVUHFNGdXLbuvF4z-yDdzppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
طائرة روسية مسيرة تشن غارات على مقر جهاز الأمن الأوكراني (SBU) في كييف.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/89364" target="_blank">📅 17:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89363">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
وكالة رويترز:
‏تسعى الولايات المتحدة ودول أوروبا الثلاث إلى التوصل إلى قرار في اجتماع مجلس محافظي الوكالة الدولية للطاقة الذرية الأسبوع المقبل، يقضي بإبلاغ مجلس الأمن التابع للأمم المتحدة عن إيران لخرقها التزاماتها المتعلقة بعدم انتشار الأسلحة النووية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89363" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89362">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انباء عن اطلاق صواريخ باتجاه مضيق هرمز</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89362" target="_blank">📅 17:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇷🇺
طائرة روسية مسيرة تشن غارات على مقر جهاز الأمن الأوكراني (SBU) في كييف.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89361" target="_blank">📅 16:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
سنقوم بعمليات استباقية في أي مكان نشعر فيه بالتهديد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/89360" target="_blank">📅 16:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89359">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
ازمة وقود تضرب العاصمة العراقية بغداد وعدة محافظات اخرى.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/89359" target="_blank">📅 15:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89358">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c841790a8a.mp4?token=aC9sYHpbkhtQ8rkz7lkE4iuY6CEO5bG4v90RQykwsr7LfUtoMxjuH448lHIdYPPUi4Mec0nvbQKOCWnjOLj4mjUzanI57iYNdgGCnBsN6_lWM2SiWuBx9ZF1YjInZYFCpSwwWIspOzLMpb7YiFbK30cw8GIKWUOBnTaOPfkM_Kk_vPPlJpQiTBt7M8mFXaKcphX7nNOx36X47vW-mNBwab77k_khNTn_3f9zaKmgtKz6lnxINUopGYp5HC025jeIoQ_MUiNmCxraNzay0uiBmPM7H3phFiusGEuLxgJBIu8jjkWw8ySqHrzxwuQU1lWw_r4gvXF-epoxGKeIRf9dpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c841790a8a.mp4?token=aC9sYHpbkhtQ8rkz7lkE4iuY6CEO5bG4v90RQykwsr7LfUtoMxjuH448lHIdYPPUi4Mec0nvbQKOCWnjOLj4mjUzanI57iYNdgGCnBsN6_lWM2SiWuBx9ZF1YjInZYFCpSwwWIspOzLMpb7YiFbK30cw8GIKWUOBnTaOPfkM_Kk_vPPlJpQiTBt7M8mFXaKcphX7nNOx36X47vW-mNBwab77k_khNTn_3f9zaKmgtKz6lnxINUopGYp5HC025jeIoQ_MUiNmCxraNzay0uiBmPM7H3phFiusGEuLxgJBIu8jjkWw8ySqHrzxwuQU1lWw_r4gvXF-epoxGKeIRf9dpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرحة كبيرة في صفوف الارهابيين التكفيريين داخل سجن رومية اللبناني بعد إقرار العفو العام داخل مجلس النواب اللبناني</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/89358" target="_blank">📅 15:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89357">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4fe167d53.mp4?token=npI8Nsc0u76P6YDLDO36OmL-hbs5ZP8yY7wLse6L40fL_XNqvcAuoWlWfKEnoXQn0y1MtPUjOvbCpRJpMlmGK6vq2XAX5VbRymEE3JaPgcw9yElAjyJFeNGmhy-2f6m3mi4gBWAOkUeJLl3lYA4B0_z2jzXpLDh-Xs0VGOmMgpP-LgxAQWdNiZ5avMJyn_ExxNcOf-Yi3TAdKrBwliSELAt_jU5bx6RQfic3Er-IOGa6kfZeuMo2nmF_SzBqTkils-n97ooC4aR-Xr9j2cM-a_WgbGeM0-Z79qs5_kQmf4YhLxAIudqfKlYzCRRAIk87Absg18hBDrxC7eh615vgQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4fe167d53.mp4?token=npI8Nsc0u76P6YDLDO36OmL-hbs5ZP8yY7wLse6L40fL_XNqvcAuoWlWfKEnoXQn0y1MtPUjOvbCpRJpMlmGK6vq2XAX5VbRymEE3JaPgcw9yElAjyJFeNGmhy-2f6m3mi4gBWAOkUeJLl3lYA4B0_z2jzXpLDh-Xs0VGOmMgpP-LgxAQWdNiZ5avMJyn_ExxNcOf-Yi3TAdKrBwliSELAt_jU5bx6RQfic3Er-IOGa6kfZeuMo2nmF_SzBqTkils-n97ooC4aR-Xr9j2cM-a_WgbGeM0-Z79qs5_kQmf4YhLxAIudqfKlYzCRRAIk87Absg18hBDrxC7eh615vgQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇮🇶
سرقة صندوق تبرعات احدى جوامع مدينة الموصل شمالي العراق اثناء صلاة الجمعة وامام الجامع يناشد لارجاع الصندوق.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89357" target="_blank">📅 15:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89356">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75c9ac861.mp4?token=OaP4AAGjJbRjKedpqBf-TxGNr5OChiQjDhO9HKqHszRcucAVpxesNpRE7avxr2CyHB9cd0XBxDeR3SFt79QwLeLG7LWDYQ3KgxMWkc32fJq23_VzZN8GNzYYxY0GSJ23DufoeMFbUXaawjn-56_RuF58ZroMHAxGu-N6Pa3zpLcKxm2jtiteZht_nXdf62ODpht-uTKAeDAqZ9VNJbKWxNxZBeR-CW1Af4aRxbVCh6KhAtaikv9BgXrS-i04wSbpvu3XXTHohJfzslqSuiPcYCqEaKRdsp3v9l1kCGy5HV2ontSIiE5AJoVY42GvUYmoC08nEtszTNKZyg7yMGiImQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75c9ac861.mp4?token=OaP4AAGjJbRjKedpqBf-TxGNr5OChiQjDhO9HKqHszRcucAVpxesNpRE7avxr2CyHB9cd0XBxDeR3SFt79QwLeLG7LWDYQ3KgxMWkc32fJq23_VzZN8GNzYYxY0GSJ23DufoeMFbUXaawjn-56_RuF58ZroMHAxGu-N6Pa3zpLcKxm2jtiteZht_nXdf62ODpht-uTKAeDAqZ9VNJbKWxNxZBeR-CW1Af4aRxbVCh6KhAtaikv9BgXrS-i04wSbpvu3XXTHohJfzslqSuiPcYCqEaKRdsp3v9l1kCGy5HV2ontSIiE5AJoVY42GvUYmoC08nEtszTNKZyg7yMGiImQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عودة ازمة شحة الوقود من جديد... ازدحامات خانقة وطوابير طويلة أمام محطات الوقود في عدة محافظات عراقية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89356" target="_blank">📅 14:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
تطورات تسليم حزب العمال الكردستاني لسلاحه ومغادرته الاراضي العراقية:
جهاز الاستخبارات التركي سيتولى الإشراف على تسليم حزب العمال الكردستاني لأسلحته في العراق
المخابرات التركية ستشرف ميدانياً على إخلاء 72 موقعاً ومخبأ تابعاً لحزب العمال الكردستاني
سيتم تحديد 5 نقاط لتسليم السلاح على الحدود بين أربيل والسليمانية
بعد إخلاء المناطق من حزب العمال الكردستاني ستنتشر قوات حرس الحدود العراقية مع البيشمركة</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89355" target="_blank">📅 14:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
اعلام العدو:
أُوقف مواطن إسرائيلي للتحقيق لدى الشاباك والشرطة على خلفية الاشتباه بارتكاب مخالفات أمنية. وتبيّن خلال التحقيق أنه جرى تشغيل المذكور من قبل جهات استخبارات أجنبية، وأنه كان ضالعًا في نشاط تأثير أجنبي. ومع انتهاء التحقيق معه، قُدّمت بحقه لائحة اتهام وطلب لتمديد توقيفه حتى انتهاء الإجراءات القانونية، على خلفية مخالفات أمنية نُسبت إليه بسبب تشغيله من قبل جهات استخبارات أجنبية ضد "إسرائيل".
وبقية تفاصيل القضية ممنوعة حاليًا من النشر.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/89354" target="_blank">📅 12:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
🇺🇸
فايننشال تايمز:
- مسؤولون أميركيون أبلغوا الوسطاء بأن واشنطن تريد فتح مضيق هرمز بالكامل بغض النظر عما تتفق عليه طهران ومسقط
- واشنطن غيرت شروطها بعدما أُبلغت بأن إيران وعُمان تحرزان تقدماً في محادثاتهما بشأن المضيق
- طهران تصر على أنها لن تعيد فتح المضيق إلا بعد رفع الحصار الأميركي وإعادة العمل بإعفاء يسمح لها ببيع النفط والسماح لها بالوصول إلى بعض أصولها المجمدة في الخارج</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/89353" target="_blank">📅 12:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYb1cRytQYdwKY-yNwDp64Nphm5Q1rANe_pHCuec9ePsvFfHjVzJJs362eAwTvl5upmTrR2kdYxASc1MyJsthWi5BCDBTkvK5G7-hQ3MogKTG0eRmZ9KN8zvTbw7oGp4bfD5bJzJi4mmlNH9-LvKHcXk9krF5StYDc_YKfuCSPYDVstwF89FsHX3jJDg-CEUnn77Fqt7t3kLCJcjxV3YKWCW42oVVfNenvFrrC6xDzzXRQvtYWZ5DPNsftnZTJ_ZgCI5eqRldIOwpxH0ZwcOfomhtPn127GI55kiF1xv-4XdJTEGYGrcwIt4P2YBxQ5AeRzpgZnsJs8j-n62-6gyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/89352" target="_blank">📅 12:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89351">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
‏فانس: لا أعتقد أن لدينا أي معلومات بخصوص هجوم الزفاف، الولايات المتحدة لا تستهدف المدنيين أبدًا في القتال، ولن نفعل ذلك أبدًا.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89351" target="_blank">📅 12:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89350">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇷🇺
🇺🇦
بعد تهديد زلينسكي باستهداف الطيران المدني
طيران تنزانيا توقف رحلاتها لموسكو</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/89350" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89349">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC2Iwox8xj4nfBWST1MhaOUahVGE6aEByl3Q2c6nngW-qzRDVpvGXKHSnSGtj220csTsCCUxr6sRs_f0Rma8nIAY1vi5egNNFtluIWE3-aDAgEGDZLu4SMJYPvUy7ldbDf1Rd3nfFZ3QC9Dy9fGOZD05cxvVOf215XtrCY6iljh-RhZGEnmN09-l6ftlLH291j8aWlVuUmFXG07wDR0Ew1tNfwyylsas2NhQNFYAC-hIR6ITL2prRHFtnX8mRFNX0mEfKjXfGjJ21Dm2wxb4Dz-J5gZ_3T04GSVnLzVeaPpkTcxetPwUx7ZbrX7KtGlgcIxYPFWQ6qkT35qvN0DgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
عراقجي
يرد على وزير الخارجية الاردني:
كم من الوقت يرى وزير الخارجية الأردني أنه يتعين على إيران أن تنتظر قبل أن ترد على معتد لا يحترم سيادة العرب
وهل هو حقا غير مدرك أن المجال الجوي والأراضي والمياه العربية استخدمت في الهجمات الأمريكية الأولى التي أسفرت عن مقتل إيرانيين أبرياء ؟</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/89349" target="_blank">📅 11:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89348">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ada3f1a49.mp4?token=VYbZ9KuWMofrj5Ben2O-zyXIK-nmJLyv5kNzVf85Yw7usbpuKEI1nXj8KvQBQCHrZIy6Deif-tWMsSzqa_pklB5RgH0I-zIhn4THOBad6R8i0V-fYleuut-yhewtv77l-demTk0_W5qFiWa3Q13yCcjjq7MeyZ4i2zh7smoJnl7dHUyCi1gPN10IzTLQml8OdkPeEwW87Rrpg0yWpARagKLAKP5ykPZTOxjrFKobaYGWEyBzFz6_I1X_JM5wgGF-deLj-lds14ckbX6agU07kiemBwNfcXCMED7_Aq2w3t4M3kEkEG6tbWCiSJbtAMLAd-MoaPk7EawHzRT2va2dgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ada3f1a49.mp4?token=VYbZ9KuWMofrj5Ben2O-zyXIK-nmJLyv5kNzVf85Yw7usbpuKEI1nXj8KvQBQCHrZIy6Deif-tWMsSzqa_pklB5RgH0I-zIhn4THOBad6R8i0V-fYleuut-yhewtv77l-demTk0_W5qFiWa3Q13yCcjjq7MeyZ4i2zh7smoJnl7dHUyCi1gPN10IzTLQml8OdkPeEwW87Rrpg0yWpARagKLAKP5ykPZTOxjrFKobaYGWEyBzFz6_I1X_JM5wgGF-deLj-lds14ckbX6agU07kiemBwNfcXCMED7_Aq2w3t4M3kEkEG6tbWCiSJbtAMLAd-MoaPk7EawHzRT2va2dgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عودة ازمة شحة الوقود من جديد...
ازدحامات خانقة وطوابير طويلة أمام محطات الوقود في عدة محافظات عراقية.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/89348" target="_blank">📅 10:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89347">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
وزير الخزانة الأمريكي:
الاتحاد الأوروبي انضم رسميا لعملية المنبوذ الاقتصادي ضد إيران ونقدر موقفه القوي والمبكر.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/89347" target="_blank">📅 03:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89346">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1ja4BMc1s6nkr4TcLq7MvupuvyNusaFDz8f5UaUa4W_-PZKosaTXxXuL8stCZ2OXn4VJFcC1FcxpcicGcVyPVYdADGLygEHPyVDbe33Q1C9S7t4jIOsVp1Dg3DtesMKacebUJXOT7wD6-Y0k5PdHfXWN1ghbM86tYt0MMYvzyJ7czuG8QSb-Lb5mPX1YXgtkoVOrMmHgms7erLEeLLL_lpVYshYltkh5N3S0o_IqdXOGH2h8yIc0sTLbadA5t8ctpPo1MdgvvCzbViV2J49SC0D0XupGlhzoUGnSMX01hIbBxrkEbgx9z5F6K01WCe2Ur_doA59PPA59i9mI-FIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
لقد أصدرت المحكمة العليا في ميزوري حكمًا سخيفًا لصالح إعادة الخرائط إلى ما كانت عليه منذ زمن بعيد. هذا ما يُسمى بالتاريخ القديم! المشكلة، بحسب فقهاء القانون، ليست فقط أن الحكم كان فظيعًا وسخيفًا وغير دستوري، بل لن يكون هناك وقت كافٍ لإعادة الخريطة مع اقتراب الانتخابات في فترة وجيزة جدًا. العملية الانتخابية، كالعادة، تتعرض للتشويش في أمريكا! يجب أن تتمكن ميزوري من استخدام الخريطة التي كانت سارية قبل شهرين فقط، في الانتخابات التمهيدية.
‏هذا يوم أسود للعدالة في ميسوري! شكرًا لاهتمامكم بهذه المسألة.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/89346" target="_blank">📅 02:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89345">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
رصد إطلاق نار باتجاه قوات الجيش الإسرائيلي التي تعمل شرق الخط الأصفر في شمال قطاع غزة. مسلحون في غزة يخططون لتنفيذ أعمال معادية ضد قواتنا.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/89345" target="_blank">📅 02:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89344">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
الاطلاقات نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/89344" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89343">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
اصوات طائرات مسيرة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/89343" target="_blank">📅 01:25 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/c6bgWZKLl8jSUnsCo1oVwaH0It2mO_wYOtbpjQBQzZWTcvoZje5QbHoFDobzhJirjwNBITW5vtRkXF2_1ev7cZJ4CnUmx_Drx414jlRSr4tYVfB-3E6KhsrvmF-IFDNvx28wnWMy6XGipsTusLcSqI4aiV-Fqe4M3e6_fVVGDoJWy2dpNOPPNlWY2Jd_QfmlZpSpxVkua2YQj49SK8xHArCm0STzIdbqBc7cjRUBR9RByeh4N5RlMQmpYg3YF8FKCUO4hw6k5HLtGkLO1HWFUJX719xEd9Jxt0ovzlNujDdJroLjlaGUs4ho5XTjPibBEOzZA5qsurlD05_1N-Zr4w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 19:28:13</div>
<hr>

<div class="tg-post" id="msg-79874">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAtsP6ilQZbSDzX6paEWwWh1chu5eqUcR59Fu03vWKX4lZg5yKb8g0UNJyNiN0zkn4lxTCuSYGzZQcC1Mha3vvsj45uMRX85SP6RL8zLfpqO66IZkiRq9EAfpiKv7-ESmW01OGkvZU5vk93u0rkrDlYOKk0cix_r3XwyOhk01Ivvwqn7Z6uWLbX307GIvE-Xuhg5vjAJH1YeF2xEv0tRPg4xFz_9iXtxs32UR3d6qBLB7HncN3JnNoUZ3p_v8y5xsoOeFPdCScEJZNDb7g4wpMJ8AA2k5DL7_GbpyP4yRw4hUXUERjtXbtPP0o3vKnkXDOo9gU1tqS1F7jF-FB2o5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الأمين العام للمقاومة الإسلامية حركة النجباء "الشيخ أكرم الكعبي":
سيف يزيد المعاصر سينكسر أمام القبضات الحسينية، وراية الحق ستبقى ترفرف فوق قمم الانتصار.</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/naya_foriraq/79874" target="_blank">📅 19:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79873">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/naya_foriraq/79873" target="_blank">📅 19:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79872">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭐️
المعارضة الكردية الإيرانية الإرهابية، ماتسمى"وحدات كردستان الشرقية" تزعم تعرض مقراتها بالقرب من الحدود العراقية الإيرانية إلى هجمات بطائرات مسيرة صباح اليوم.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/naya_foriraq/79872" target="_blank">📅 19:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79871">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
‏
نتنياهو:
لن ننسحب من لبنان ‏وأمرنا الجيش بالقيام بكل ما يلزم لحماية سكان الشمال.
نحن في ذروة حرب إقليمية متواصلة لا تقل عن حرب الاستقلال.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/naya_foriraq/79871" target="_blank">📅 18:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79870">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭐️
حادث وقع على بعد 7.5 ميل بحري جنوب شرق داهيت، عمان. أصيبت سفينة شحن على جانبها الأيمن بمقذوف مجهول، مما تسبب في أضرار لجسر القيادة.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/naya_foriraq/79870" target="_blank">📅 18:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79869">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭐️
​
ضغوطات لحركة طالبان ضد أكبر مدرسة دينية شيعية وقناة التمدن الفضائية في العاصمة الأفغانية كابل..
وفقاً للتقارير الواردة من العاصمة الأفغانية، تواجه "حوزة خاتم النبيين (ص) العلمية" و"شبكة التمدن التلفزيونية" ضغوطاً ومساعي من قبل حركة طالبان للسيطرة عليهما أو تعليق أنشطتهما، واللتين تُعدّان من أبرز الميراثين العلمي والثقافي  آية الله الشيخ محمد آصف محسني (رحمه الله).
​نبذة عن المؤسسات المستهدفة
​مدرسة خاتم النبيين (ص) العلمية: يُعرف هذا المركز بأنه أكبر مدرسة للعلوم الدينية الشيعية وأكثرها تجهيزاً في أفغانستان. ولم يقتصر دورها على تعليم طلاب العلوم الدينية فحسب، بل لعبت دوراً محورياً في التقريب بين المذاهب الإسلامية والحفاظ على الانسجام والتماسك الاجتماعي في البلاد.
​شبكة التمدن التلفزيونية: تأسست هذه الوسيلة الإعلامية المرئية بهدف نشر معارف أهل البيت (عليهم السلام)، وترويج الأخلاق الإسلامية، ورفع الوعي الديني والثقافي. وقد نشطت لسنوات طويلة كواحدة من وسائل الإعلام الرصينة والمستقلة في أفغانستان.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/naya_foriraq/79869" target="_blank">📅 18:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79868">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b657424a.mp4?token=rqzd9YWPPEGe98qp9RgOYUgdSOdOxdWmfTNmH9_6AqaUHyXe16z0jZtblNPceXDoVC5tuj5iXe6HtVk0fWlmGFKXkldV87p5lRmAbQ8lU8TK0D9dI5UZfjAUarOqvcLN3UfBxp2v0HV7vg8RL8XCXoXIRbv4U6GabxT8-8M8pvvGCwHMJFRsPCVr19AaNU-jhRNjM8Wl-Rm2eTqYoSxiqqJzAUMKxl5uKilCr9pPOmzyJKW-AFFjz8kUNyNl9li1ZdGnBivX74o-Rlg6K7xl8J6MqFYAFg3xU87md9IcG8bX_gdP1SVH2pt8KbTzYJkHfQoGXAPn_1W1rQTo0CtEMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b657424a.mp4?token=rqzd9YWPPEGe98qp9RgOYUgdSOdOxdWmfTNmH9_6AqaUHyXe16z0jZtblNPceXDoVC5tuj5iXe6HtVk0fWlmGFKXkldV87p5lRmAbQ8lU8TK0D9dI5UZfjAUarOqvcLN3UfBxp2v0HV7vg8RL8XCXoXIRbv4U6GabxT8-8M8pvvGCwHMJFRsPCVr19AaNU-jhRNjM8Wl-Rm2eTqYoSxiqqJzAUMKxl5uKilCr9pPOmzyJKW-AFFjz8kUNyNl9li1ZdGnBivX74o-Rlg6K7xl8J6MqFYAFg3xU87md9IcG8bX_gdP1SVH2pt8KbTzYJkHfQoGXAPn_1W1rQTo0CtEMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مسلحين تابعين لعصابات الجولاني الإرهابية، ترفض عودة الأكراد إلى مدينة رأس العين ضمن محافظة الحسكة السورية وتتوعد من يعود إلى المدينة بالقتل.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/naya_foriraq/79868" target="_blank">📅 18:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79867">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/naya_foriraq/79867" target="_blank">📅 18:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79866">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هجوم على سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/naya_foriraq/79866" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79865">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
تسعى إيران إلى كسب مليارات من الدولارات عن طريق فرض رسوم على السفن لخدمات الأمن والسلامة والبيئة في مضيق هرمز بعد الحرب.
تقول طهران إن الخطة يمكن أن تدر ما يصل إلى 40 مليار دولار أمريكي سنويًا، وتريد من الدول الخليجية المجاورة أن تشارك في الإيرادات.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/naya_foriraq/79865" target="_blank">📅 18:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79863">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQo20yPgUw0NvLg2u6AseV14lHMwcv-HnzOs123KXveFQYPrdX4GZcWZeF2B8xT4E3Za_FB3I4SoKEJ1LqOS7u6jmDgxopENsy0P8Chy2_PMeV9jERl28x3dbIlHM5CrjwAkhmAK7V5i_FUlFsN6fDVqp7SMwyxUvk2bJrdLEEQ_M5i1lGBLxKebw9MQKbn3iccZw8so3rVpaoFR6Cg3dWLtZcJUlL2xfKyhDRRJicx2baQCNRsUUQOuJzXuUNJrC52gS19VOVaeLp8rP5tu7T3_hoHDVUkwHwI_39DI4GRnxcJZfq-YDT5mBVgreRHy6bb91hYz8JQhw-cLezjGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUkkImm8Jkfk375WL7REgRV0pEH9cAfY4d8oxy9vXfnhcPxsQlAFtIHPbdKCo-9i9EyhXZ3w9SlTeXxgXDVfYofGi6TrRhdprDg3uWrvCwoEwMHvIKzwpZCV_-IIRURCj6ewJBMFxmmceOr0CyG0NoRrZYjCpeYqOYPxqwvFAtFjIlN_D7gC5KcvDvLJtENgnxCdqjkIUsgWErAlSW2OpGmoR9iEC8SQ_l5kJHqkfJZH6xMCHTNJxG-YjRkCM3lAycQ4mVthEsNPcQfoZpRzD5gUvkbO7770m6WEYje6s-nAmmXRne4p427SlcVWCmATNH_-t-X_F76Yo-_bREj-1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
المعاون العسكري للمقاومة الإسلامية حركة النجباء "عبدالقادر الكربلائي":
إننا بعون الله لن نحيد عن درب المقاومة، ولن ننساق وراء تخرصات الأعداء وأوهامهم، فسلاحنا سيبقى مرفوعاً بوجههم وراياتنا خفاقة ما دام فينا عرق ينبض وسنبقى مقاومين حسينيين لن نتراجع أو نساوم إن شاء الله.</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/naya_foriraq/79863" target="_blank">📅 18:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/naya_foriraq/79862" target="_blank">📅 17:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79df748d9.mp4?token=oHxX84PhGdPftdrJC2TRc8tEuCYn2JxQgjcL74_4kw6zOiQhp1y9aOTkISoQiMA12lPF1DY3pZ8JH9nA_zGAMTm2XwJtfC8g0f217f6IzTD-B7Wjud-ziJxTheeefTNNUZIXwG5eBwZeJOvW9fiRPLSSrEVjItXahZH0_9gjqr_RCNcg1M2gMelEj05nEGXvuGHlP7k8EudvdjQP8XbiEWOhyjTwxJe--GsESPNP2hsBPeEPnDgBNaV1-HZmrHbJRVvwHq9oOZwJuDyBngTcrvhgj8cyCuxqzqF2O_Zjuh0qrkqKyDlaC9NuwC-Rb32rglphnrkDeeYK1nTC_RABCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79df748d9.mp4?token=oHxX84PhGdPftdrJC2TRc8tEuCYn2JxQgjcL74_4kw6zOiQhp1y9aOTkISoQiMA12lPF1DY3pZ8JH9nA_zGAMTm2XwJtfC8g0f217f6IzTD-B7Wjud-ziJxTheeefTNNUZIXwG5eBwZeJOvW9fiRPLSSrEVjItXahZH0_9gjqr_RCNcg1M2gMelEj05nEGXvuGHlP7k8EudvdjQP8XbiEWOhyjTwxJe--GsESPNP2hsBPeEPnDgBNaV1-HZmrHbJRVvwHq9oOZwJuDyBngTcrvhgj8cyCuxqzqF2O_Zjuh0qrkqKyDlaC9NuwC-Rb32rglphnrkDeeYK1nTC_RABCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/79861" target="_blank">📅 17:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0389a80ba9.mp4?token=Eb6HcxaDrhnIoD-75IauGioWgmi6VYamew07tGjOn4rmjEeSaw6X3ZgMG1NR9Qnda355vvQYqQpltBNbJO-IDuJTt9x-RoKn7hSS6kH1OayP7qBMojGBppB9ksqNYDUcNWR9erc7zvT33KeH_hLk-ZjCnYBZUPrEGDJsim-hCZkKaG3IeyIvH1FcaanOzrnphtIU1i6_h-Juh2Mrk5fbXb_iuUyPlm7lUkk_a6Qc9STRYROd1DJrCh-C_4TYNEW13RzqYTNU48VtPGVnqqnGZHSITZba31Ygin02uoUyNRovGLEClchClYbKA8lA5DrDraLBhZwciQl-D2Z0f5cyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0389a80ba9.mp4?token=Eb6HcxaDrhnIoD-75IauGioWgmi6VYamew07tGjOn4rmjEeSaw6X3ZgMG1NR9Qnda355vvQYqQpltBNbJO-IDuJTt9x-RoKn7hSS6kH1OayP7qBMojGBppB9ksqNYDUcNWR9erc7zvT33KeH_hLk-ZjCnYBZUPrEGDJsim-hCZkKaG3IeyIvH1FcaanOzrnphtIU1i6_h-Juh2Mrk5fbXb_iuUyPlm7lUkk_a6Qc9STRYROd1DJrCh-C_4TYNEW13RzqYTNU48VtPGVnqqnGZHSITZba31Ygin02uoUyNRovGLEClchClYbKA8lA5DrDraLBhZwciQl-D2Z0f5cyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
أعمدة الدخان تتصاعد من قضاء المقدادية في محافظة ديالى شرقي العراق بعد إنفجار مجهول.</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/naya_foriraq/79860" target="_blank">📅 17:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇾🇪
السيد عبدالملك الحوثي:
نرصد بكل اهتمام مجريات الوضع في أرض الصومال وما يقوم به العدو الإسرائيلي بهدف السيطرة على خليج عدن وباب المندب والتحكم في البحر الأحمر، نحث الدول المطلة على البحر الأحمر لموقف مشترك إزاء نشاط العدو الإسرائيلي، ولن نقف مكتوفي الأيدي أمام أي تمركز في الصومال وسنبادر في أي وقت لاستهداف أي نشاط للعدو الإسرائيلي في أرض الصومال.</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/79859" target="_blank">📅 17:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79858">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مقتل ضابط بجهاز المخابرات العراقي برتبة مقدم في العاصمة بغداد بعد اندلاع اشتباكات مسلحة في منطقة المعالف</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/79858" target="_blank">📅 17:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79857">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
✊
العراق يعلن تسجيل تحفظه على بعض فقرات “إعلان باكو” الصادر عن الدورة العشرين لمؤتمر اتحاد مجالس الدول الأعضاء في منظمة التعاون الإسلامي المنعقد في العاصمة الأذربيجانية باكو
العراق يؤكد تمسكه بمواقفه الثابتة والداعمة للقضية الفلسطينية وحقوق الشعب الفلسطيني المشروعة، معرباً عن تحفظه على الإشارة إلى “حل الدولتين” بصيغته الواردة في الإعلان، انسجاماً مع التشريعات والقرارات الصادرة عن مجلس النواب العراقي الداعمة لإقامة الدولة الفلسطينية وعاصمتها القدس الشريف، وضمان حق العودة والتعويض للشعب الفلسطيني.</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/79857" target="_blank">📅 16:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79856">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
السلطة القضائية الايرانية:
أن الادعاء بـ"حظر ترديد الشعارات المناهضة للنظام الأمريكي وحرق علم الحكومة الأمريكية الإرهابية في التجمعات" ادعاءٌ باطلٌ لا أساس له من الصحة.</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/79856" target="_blank">📅 16:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79855">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇷🇺
‏وزارة الخارجية الروسية تستدعي سفير رومانيا وتعلن القنصل العام لرومانيا في سانت بطرسبرغ شخصًا غير مرغوب فيه وتعلن اغلاق المكتب القنصلي الروماني هناك ردًا على إلغاء بوخارست موافقتها على القنصلية العامة الروسية في كونستانتا وإعلان مديرها شخصًا غير مرغوب فيه.</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/79855" target="_blank">📅 16:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79854">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDuIm4lBl14uBYCiM0bg4NtUQRyJsJctjff4qRvhpWJv238_WRv7sEH5hapQPyC91BHhE57gIH5WiosWsfcshjrgFA3s_lF43qJD_mUdh8m9bNLxBjl6QPXhwuqiZuokOBSBWL3cxHmHmUYww6pyfGK8aOeFOK1aIBV6pP-hONQAy0P3SgGX1Jh_v_zmyW9IGer0Udd3LXGzBT2rhY_W-OzmhmbkIL2VdWS4pz-7KPXCwmb9_3gKuhuAoq-c72c3HS3mj9eSgW74uPfkDXn0KmNLkhSDaX6JXW5_UtQywwxDQQAB5sHBGIwZNpwx5Ke-VPqmgT61nlPk2pvOBZw9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
‏
تزعم أمريكا زوراً أن أصولنا المجمدة ستشتري منتجاتها الزراعية. أمرٌ مثيرٌ للاهتمام. المحصول الوحيد الذي نحصده هو ما زرعتموه أنتم: عقودٌ من انعدام الثقة. إنه عضوي، وفير، ومحلي الصنع. لكن يبدو أن الولايات المتحدة لا تصدّر سوى فول الصويا المعدل وراثياً، والوعود الكاذبة، والتصريحات الجوفاء.</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/naya_foriraq/79854" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79852">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCz_ig3AVy9NN48qbV6MnMru7XUWdycU_wrLtaAv2t3bZkhgwlq9LO-N7vbitHa9Tm5EAlWAnLE1Id9vgdNtKKYT_8Rz1fDj5UnArB4Wls_Q27xKFc-WRc2BNUV4sZll8bIs6NEW9UGfSee3sV5P21XmYoWeE-NDw-y2Kj6z9HRDDP-BE7TvfxRWpNsg4pK0ZiGbYOVjsnNPiRjrGr-DuMmBnmk43MaC-_-xxY6Lv2Td_7iuVZPOabTHgflPJ8VA9lL9nfUO7_w7fp49MBlDgvunx5O09-lPqKPTh3mo3DvTBkPBixK-fFzC-P_8GlLn1vRpI8P5wmYjjNdCdxywZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yjloqo8DoydSwP1vEtX8IZELKpp7Ml42VjlIYbfNaZJWNQZgP9l7oHh6Uj7rh6oVBxLznMuU6JkOaYzTO56PJWo45yocw8eVztShmaTq67hugLDv6ICITTDOrSgFTOKNbc4DthxdSgU1z4WzBpkOf1pA2eaAW5QcGYhaUKTdRjARSPXfvgNxYgyJm0hnSBdju4UbgKRoPyu0oFXvONXR_nJ59q8zoBSKA24gpgodA320141KKkPhrpnQNhCtdkxTeBGYA8w_q3uSS_60iKLHxs6nWkK1dl_Bzz0uprYl0MVCDkNjv7pqr0wAQpmlg4r6_oxQ4mAUGgm-ukkl8XsDVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
❤️
القيادات الايرانية تشارك في احياء يوم عاشوراء.</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/79852" target="_blank">📅 15:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79851">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏ زلزال بقوة 5.5 درجة يضرب تشيلي</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/79851" target="_blank">📅 15:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79850">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏روبيو: دول الناتو لم تسمح لنا باستخدام قواعدنا العسكرية رغم أن إيران تشكّل تهديداً أكبر لهم</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/79850" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79849">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">روبيو: إذا استخدمت إيران الأموال لتمويل وكلاء لها، فإن الاتفاق لن ينجح.</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/79849" target="_blank">📅 15:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79848">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">روبيو: نحن قريبون من التوصل إلى اتفاق مبدئي بين إسرائيل ولبنان</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/79848" target="_blank">📅 15:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79847">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏روبيو: سنشارك دول الخليج على خطوات تطبيق مذكرة التفاهم مع إيران  تحديدا فقرة دفع الـ300 مليار دولار
😄</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/79847" target="_blank">📅 15:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79846">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
‏روبيو: لن يكون هناك سلام واستقرار في المنطقة مع وكلاء إيران.</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/naya_foriraq/79846" target="_blank">📅 15:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79845">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">السلطات المصرية تغلق مسجد الامام الحسين (عليه السلام) في القاهرة لمدة 3 ايام بحجة "اجراء صيانة"!</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/79845" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79844">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
‏
بيان صادر عن البحرية التابعة للحرس الثوري الإيراني:
لا يُسمح بالمرور في مضيق هرمز إلا عبر المسارات التي أعلنها مراسل إيران دراغون المتمركز في المياه الشمالية لمضيق هرمز. وقد أعلنت البحرية التابعة للحرس الثوري الإيراني حظر مرور السفن خارج هذه المسارات، واصفةً إياه بالخطير للغاية، وطلبت من جميع السفن الالتزام التام بالمسارات المعلنة. ويُشترط التنسيق مع البحرية التابعة للحرس الثوري الإيراني لعبور مضيق هرمز عبر القناة 16، وسيتم اتخاذ الإجراءات اللازمة بحق المخالفين. والرسالة العامة لهذا البيان هي أن الملاحة في مضيق هرمز لن تكون آمنة إلا في ظل الأوامر الإيرانية</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/naya_foriraq/79844" target="_blank">📅 14:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79843">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو: لا يوجد أي دعم من دول الخليج لفرض رسوم أو ضرائب على مضيق هرمز، دول الخليج أكدت خلال الاجتماع عن مخاوف جدية.</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/79843" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79842">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزير الخارجية الامريكي ‏روبيو:
لا يوجد أي دعم من دول الخليج لفرض رسوم أو ضرائب على مضيق هرمز، دول الخليج أكدت خلال الاجتماع عن مخاوف جدية.</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/naya_foriraq/79842" target="_blank">📅 14:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79841">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
قائد قوة القدس في حرس الثورة الإسلامية اللواء اسماعيل قاأني للصهاينة:
عليكم مغادرة لبنان بأكمله؛ لأن هذه الأرض ساحة مقاومة ونضال، وليست ملعبًا للمحتلين. إن لم تتراجعوا اليوم بإرادتكم الحرة، فستُجبرون غدًا على الفرار مُذلّين مهزومين. لا تنسوا عام 2000 والإرادة التاريخية للشهيد السيد الحسن نصر الله في بنت جبيل؛ ذلك الوعد لا يزال قائمًا، ولا شك أن المشهد نفسه سيتكرر.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79841" target="_blank">📅 14:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79840">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني ‏كاتس: كل دولار يصل إلى إيران قد يجد طريقه إلى حزب الله وحماس والحوثيين.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79840" target="_blank">📅 14:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79839">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الصهيوني ‏كاتس:
كل دولار يصل إلى إيران قد يجد طريقه إلى حزب الله وحماس والحوثيين.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79839" target="_blank">📅 14:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79838">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇶
مقتل ثلاث اشخاص واصابة اخرين كحصيلة اولية في اشتباكات مسلحة بمحافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79838" target="_blank">📅 14:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79837">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
تتويج العراق في لقب بطولة العالم للمواي تاي في ماليزيا بعد فوز اللاعب العراقي مصطفى التكريتي على نظيره الروسي في النهائي.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/79837" target="_blank">📅 13:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79836">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🌟
وزارة النفط العراقية:
إن ما أُثير بشأن تلويح العراق بانهاء عضويته بمنظمة أوبك لا يعكس الموقف الرسمي للحكومة العراقية، إذ لم يطرح رئيس مجلس الوزراء أو الحكومة العراقية مسألة الانسحاب، بل أكد العراق باستمرار أهمية إعادة تقييم السقوف الإنتاجية بما يتوافق مع الطاقات الإنتاجية المستدامة للدول الأعضاء وفقا للاتفاق الذي أقرته كافة الدول المعنية والتفاهمات الخاصة بوضع العراق الأمني والاقتصادي.
وفي هذا السياق، استجابت دول منظمة أوبك والدول المؤتلفة معها لهذا التوجه من خلال إطلاق عملية إعادة تقييم الطاقة الإنتاجية القصوى المستدامة للدول الأعضاء، والتي تُنفَّذ حالياً بالتنسيق مع شركة استشارية دولية مستقلة، وبمشاركة فاعلة من العراق، وفقاً للجدول الزمني المعتمد.
كما باشرت دول منظمة أوبك والدول المؤتلفة معها بالفعل بإعادة الكميات المخفضة تدريجياً، ومن المقرر استكمال عودة جميع التخفيضات الطوعية خلال الأشهر القليلة المقبلة، بما يسهم في تعزيز السقف الإنتاجي للعراق. وعليه، فإن أي مطالب تتعلق بالسقوف الإنتاجية أو مستويات الطاقة الإنتاجية تُعالج من خلال الآليات الفنية والتوافقية المعتمدة ضمن إطار دول منظمة أوبك والدول المؤتلفة معها.
كما نود الإشارة هنا إلى وجود تفهم عالي المستوى من الدول الأعضاء في المنظمة لوضع العراق الخاص وما عانته الصناعة النفطية العراقية خلال اكثر من أربعين عام مضى من الحروب والحصار والتحديات وآخرها ما حصل من تدمير للعديد من جزئيات بنيته التحتية النفطية والساندة من خلال الهجمات الارهابية التخريبية وان هذا سيؤخذ بنظر الاهتمام ليكون الانتاج النفطي العراقي بالمستوى العادل الذي يمكنه من استعادة موقعه كثاني اكبر منتج ضمن دول المنظمة ويحقق النتائج المرجوة من مشاريع التطوير والتأهيل لكافة مفاصل الصناعة النفطية التي تشكل العصب الرئيسي للعائدات المالية العراقية.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79836" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79835">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2psAmnlQB-WQIU39eye1_AvgJU9_MqW_-53Eg0jqK_7VdZ1BoIFyTHnKqApP4FOoy9nVw-ns5tzKMAQP_9J809p0ffHznQWauHBuCRZ9ASaFWXZ9JYdykNSKKShpAg2UnCaZzkmPZDrhmaTkgTkIOZOs4by55kFfxq3J4wWFp6Qn3NKkZM9-5GKTJpCxlmLY8WqWIHmvIbwRIphxazh9oVARxGKDq_E4LaN9piCncWtocMUOv_QiWWLQjDGjckSyJnrJCzTBqpFGbwSUILDNv21m3BjcgEjy2B8t55qt1psRF_KrqaYsjgaTWQc-4wdn_1zVXnm3WdUGoLZ6ml9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
قوات حرس الحدود العراقية تحبط محاولة تهريب 34 كغم من المخدرات بواسطة بالون هوائي على الحدود العراقية الاردنية السورية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79835" target="_blank">📅 13:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79834">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇷🇺
🔵
فرنسا تتدعي انها اعترضت ناقلة نفط خامسة تابعة لأسطول الظل الروسي</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79834" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79832">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">إعلام أمريكي: امريكا توجه الجيش اللبناني بالتوجه فوراً نحو المناطق التي انسحب منها الجيش الإسرائيلي جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79832" target="_blank">📅 12:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79831">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">إعلام أمريكي: امريكا توجه الجيش اللبناني بالتوجه فوراً نحو المناطق التي انسحب منها الجيش الإسرائيلي جنوب لبنان.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79831" target="_blank">📅 12:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79830">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
📰
رويترز عن مسؤول كبير بقطاع النفط: العراق يمر بأزمة مالية حادة ناجمة عن الانخفاض الكبير في صادرات النفط بسبب حرب إيران ويجب النظر في زيادة حصته في أوبك بمنتهى الجدية
🔻
العراق ناقش داخلياً احتمال خروجه من منظمة أوبك، لكنه يعتزم البقاء في المجموعة والضغط من أجل الحصول على حصة إنتاج أكبر.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79830" target="_blank">📅 11:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79829">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2hzAhcmnkCwca0_2YNdboqUnHIz96cYNjScjyIsRlLwIeX9lGiMSnBiNjHCRSyUKLIYBJwG53qqq_t5aJVuPjxLQUlqTxYKmMNJ7Q1lHep0KEYs2k5fVw60tVeqw4cEQnFyzhOT8mVdQrbweGdOQdmUJQqF2IXubHLVmfOnZUXtd9G230gVr5LS-NxfY8bFzSsxZfyETRRlUUlzWaT_MM0CVJcIzkmA5niUa0gYXSqMFEATNTA2pHiSY8hNYAnPlCgq9-rpLOjPWQ1vIPqgesJoDqECIYDp7PxdFCESZc9xtnKkdu_X2L9tf-KNTxlAKM3RLiR2UgbPo31YZYRNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
أفلس العراق رسميا ؟!
مجلس الوزراء العراقي يقرر إيقاف التعاقدات للمشروعات الجديدة الاستثمارية وما يخص العقود السابقة يبلغ الشركات " اصبروا ان الله مع الصابرين " يبدو انها آثار عواقب الحرب بين امريكا وايران على المنطقة ..</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79829" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79828">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0395c35c88.mp4?token=PDcC1CLWyiGCcc6vfyn5WerrDz3RvnumHzn7dyCwEzloizTWI81VRssdUA06SEiFkVJy0pIWQg4sOWd-C4udi2Tk2Vrv0m-7UUNKsw_E6WVyGsHdnR1O9vv3DBvBCAAN2W72zdTxM5hxi0Kisnxf7oLIy6oJsTxsUmIMsxF48dWL4yrmxmAxKmwxKo6FrIg7zgMwmTzpKPlIjtAhx4LBD8T-HffJelzUVxK5YROHgJDI-P4eIcUmR8A6qtGN1knO01C5OC5JcklQW8S7wBGfnmglWopMYdMeF9ZLECXT63GTxp2TvS2J1N7fCv7DtLPP94U7YyMzAqKdxYKFKY_ZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0395c35c88.mp4?token=PDcC1CLWyiGCcc6vfyn5WerrDz3RvnumHzn7dyCwEzloizTWI81VRssdUA06SEiFkVJy0pIWQg4sOWd-C4udi2Tk2Vrv0m-7UUNKsw_E6WVyGsHdnR1O9vv3DBvBCAAN2W72zdTxM5hxi0Kisnxf7oLIy6oJsTxsUmIMsxF48dWL4yrmxmAxKmwxKo6FrIg7zgMwmTzpKPlIjtAhx4LBD8T-HffJelzUVxK5YROHgJDI-P4eIcUmR8A6qtGN1knO01C5OC5JcklQW8S7wBGfnmglWopMYdMeF9ZLECXT63GTxp2TvS2J1N7fCv7DtLPP94U7YyMzAqKdxYKFKY_ZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تاكر كارلسون: كان ترامب مقتنعًا بأن قتل آية الله سيؤدي بطريقة ما إلى انهيار إيران. لكنه وقع في فخ الحرب مع إيران بعد وفاة آية الله علي خامنئي.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79828" target="_blank">📅 09:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79827">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36962cfb3a.mp4?token=vg_v2BeUAX7m-c174U05zLAx9p1nVmKxIAhzv3a5yzLFrKrTg9Gp24AtZOjNXAD59J6VYoywSbzzaRn1ydj6e_g04XV2Uf7mt0njifIg40qC1zUix_cyKNY7Q3qEb0CkUdWVeaWiCfIzT6DOHqULaNJNBCVXbJR1gSvo-uk5Dqm6SZmpPogPfTdXlPIMrRiHGOtI0XlwDKqLFSjtsuuH9mibR0mr5v4nYKX87eAHzHVq4R7F7akNz7jHFkQ8u4KZDWWOpqXn5GvSZ1_WLzw7jxRuvyXQDwFCxJD-hL5mIt6KjSoCxW0C20hulVpP6LCo3Z44hcvsjayQ1n4mxm4gVEop8V8wPYdiNCIv7zC846brv6H0wrDCUAKtAWxpHSYtk8HiexEUiUU6jhm8kHgJwa64k5VhkhbAH74gutbIW0jaP9h-LGnt8VNyXiWOSXp5KYLKjwMh1MG7nu3CY-CLfur_Gc1sPYXPkYMtYEPdNuk88FSC_M8Lvv3u9Hmwt7GhvHL18tgxcnwp_OiNtFQfYV47RT18jVZxcnVfgafOIBV7FbmtshqGZ0EZhJ6WMbX67DwIY42LgqBIUtJ7iig3UidyMhi-zw_1BTqK9DX0lxp9psSz06QwYQOzkiP-XwdPfW8rhNbNgkPAE8bESJm-KVUFFFfQlte6cNdJ4eGGfs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36962cfb3a.mp4?token=vg_v2BeUAX7m-c174U05zLAx9p1nVmKxIAhzv3a5yzLFrKrTg9Gp24AtZOjNXAD59J6VYoywSbzzaRn1ydj6e_g04XV2Uf7mt0njifIg40qC1zUix_cyKNY7Q3qEb0CkUdWVeaWiCfIzT6DOHqULaNJNBCVXbJR1gSvo-uk5Dqm6SZmpPogPfTdXlPIMrRiHGOtI0XlwDKqLFSjtsuuH9mibR0mr5v4nYKX87eAHzHVq4R7F7akNz7jHFkQ8u4KZDWWOpqXn5GvSZ1_WLzw7jxRuvyXQDwFCxJD-hL5mIt6KjSoCxW0C20hulVpP6LCo3Z44hcvsjayQ1n4mxm4gVEop8V8wPYdiNCIv7zC846brv6H0wrDCUAKtAWxpHSYtk8HiexEUiUU6jhm8kHgJwa64k5VhkhbAH74gutbIW0jaP9h-LGnt8VNyXiWOSXp5KYLKjwMh1MG7nu3CY-CLfur_Gc1sPYXPkYMtYEPdNuk88FSC_M8Lvv3u9Hmwt7GhvHL18tgxcnwp_OiNtFQfYV47RT18jVZxcnVfgafOIBV7FbmtshqGZ0EZhJ6WMbX67DwIY42LgqBIUtJ7iig3UidyMhi-zw_1BTqK9DX0lxp9psSz06QwYQOzkiP-XwdPfW8rhNbNgkPAE8bESJm-KVUFFFfQlte6cNdJ4eGGfs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران لا تمتلك منصات إطلاق صواريخ. للمرة الأولى منذ 3000 عام، سنحظى أخيرًا بالسلام في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79827" target="_blank">📅 09:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79826">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039cf77145.mp4?token=Awf3GKX_0nNguFpgWpvTsc_VRPn2K6apwrgEMvgJ79jrgAeLsfzu_CK5GsIjU-UiY3G4fE332G7pkBh-fWH-WElMoX5N4QNLzq3tvLTM2YJNZyqgnz6cWd_dMWxNWO3l9lDwG2vwDa-RizSA5NhwAe0hMMXQJ3-mp-3dXoQ0E2ei3c551WxkvM06193nZWLh2gUDaU8XKv7OX5XODCpiqhZaY_8P8R5exoAcQwtJCT-nmbFLjreQ5CHPFq5FVWVc4gHDCFolJYFZPWHSGCYR-VIgVzud38z9yOCxeSU4fFwJ7WG74bFzcuDQ8jKzO4mBDmlnOtJZcgIxo6iqDDDXgC-UGH7fAIW3p0fX4gt6CaLEXnOTUo3_tHzCJZ1tp_5YpBxpBO-Za0xSndxUWcR4GsXQV3yQJm-WwmfAHX3BkkGPqAllBDaWf_oYiOtCo97sDix8PEN8NHLcOsq6KTN-1z78RRiFFbW6xy_C10G6PkZm4xAYAen7QJFQBlg8-bJtD8Hm0LSg3YlLqZqq5XxIgwdGbtk2_lyiqJASoOu5sy0vm7AdfrAW-SEwLX1JlGdBLcW7WJoWBN6PSzyy1cc8K8pzve7N3RG4Ao-JhfmOggRTRxiRRJkIMhPD41PkbgvY24BhqkKb1kN6f12AXCQaHN_WvAnCsW90HY95iwYJ7vI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039cf77145.mp4?token=Awf3GKX_0nNguFpgWpvTsc_VRPn2K6apwrgEMvgJ79jrgAeLsfzu_CK5GsIjU-UiY3G4fE332G7pkBh-fWH-WElMoX5N4QNLzq3tvLTM2YJNZyqgnz6cWd_dMWxNWO3l9lDwG2vwDa-RizSA5NhwAe0hMMXQJ3-mp-3dXoQ0E2ei3c551WxkvM06193nZWLh2gUDaU8XKv7OX5XODCpiqhZaY_8P8R5exoAcQwtJCT-nmbFLjreQ5CHPFq5FVWVc4gHDCFolJYFZPWHSGCYR-VIgVzud38z9yOCxeSU4fFwJ7WG74bFzcuDQ8jKzO4mBDmlnOtJZcgIxo6iqDDDXgC-UGH7fAIW3p0fX4gt6CaLEXnOTUo3_tHzCJZ1tp_5YpBxpBO-Za0xSndxUWcR4GsXQV3yQJm-WwmfAHX3BkkGPqAllBDaWf_oYiOtCo97sDix8PEN8NHLcOsq6KTN-1z78RRiFFbW6xy_C10G6PkZm4xAYAen7QJFQBlg8-bJtD8Hm0LSg3YlLqZqq5XxIgwdGbtk2_lyiqJASoOu5sy0vm7AdfrAW-SEwLX1JlGdBLcW7WJoWBN6PSzyy1cc8K8pzve7N3RG4Ao-JhfmOggRTRxiRRJkIMhPD41PkbgvY24BhqkKb1kN6f12AXCQaHN_WvAnCsW90HY95iwYJ7vI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران لا تمتلك منصات إطلاق صواريخ. للمرة الأولى منذ 3000 عام، سنحظى أخيرًا بالسلام في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79826" target="_blank">📅 09:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
هزة أرضية بقوة 3.5 تضرب خراسان شمال شرق إيران</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79825" target="_blank">📅 09:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAIsz0m6kZHStgGxxFTsCVpJCJNH7LNMGOrjNl0dzAY3wd2u_KmjDe5GDSfCxXNDL-B5RQJi0tqxY-WwK03t1tk3-ESBvzCR7TWPMzm28IzZfRm1bpVl-ppCmYGrap6u_1qvMu0Jp31tBO7usZgwBihAX_hQyxRCZby26TptMaUzNRPHkpTK1f8ksqyV_v_Ob2IY6-KDmSmNXF6L9XD4xMgO-Rfyv8U6MN1bHG_FCXsy3csxePYnpOivFssyeCcXNS_sU4ukdnzDNCLnWvrl_Z3i8Tv7CWvWRPiW346TNOR5Fk5jhjVcP4x_Ytn6ZBOwtlYyCGJrjSU8cCdomjKokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
الزلزالان الكبيران اللذان ضربا فنزويلا مؤخراً كانا هائلين، وقد خلّفا عدداً هائلاً من الضحايا. الولايات المتحدة الأمريكية على أهبة الاستعداد لتقديم المساعدة!
‏لقد أصدرتُ تعليماتي لجميع أجهزة حكومتنا بالاستعداد للتحرك بسرعة. سنكون حاضرين لدعم أصدقائنا الجدد والرائعين. التقارير الأولية ليست مبشرة!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79824" target="_blank">📅 08:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZglEdR4uUbmizEypG4VWJAZpxzBdY9BPBhtMI9S9bDixAO6WMFdvVwf7-zr2E2oF2pUs4VumNmYL7Z6AWkX__JrFEwamf6weZfTvizqEcqpBKibAFDqxRRlu8EJydx7Y1C8ZHYfrEp6fS5aKAesLJp3y62vEf-zIBlUhZjixhtsndSYts1b8TmJe-PeavdZhvcLcHsbvdv4uXDkLg4HWb6K1gPezqHjO7snt1iajxuAEJBCu2SwdJqdPlF5CmNXG8o2cyqBzYl19_XCJNOOCnZk3MV6qt-x4WLY7KDAEk_fgqdVj9tjokgKZ8RIovkXXMAfC_WtCMMue-gOl6dd1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزيدي للصحافة العالمية :
سيتم تخصيص 500 ألف برميل يومياً من النفط العراقي لتجديد الاحتياطي النفطي الاستراتيجي الأمريكي ؛ سيدرس العراق "تعليق" عضويته في منظمة أوبك إذا مُنع من الإنتاج بما يتناسب مع قدراته
‏سيتم "خنق" الفساد
‏سيتم نزع سلاح الميليشيات بحلول 30 سبتمبر مع مغادرة آخر القوات الأمريكية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/79823" target="_blank">📅 01:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امين عام النيتو في البيت الأبيض يحاول إقناع ترامب بأن الحلفاء الأوروبيين ساعدوا الولايات المتحدة فعليًا خلال حرب إيران. ليرد ترامب خاب أملي من إيطاليا وبريطانيا وألمانيا وفرنسا وإسبانيا وكان من اللطيف أن يعرضوا مساعدتنا في حرب إيران</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79822" target="_blank">📅 00:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f1c85d25.mp4?token=bnhS4XKTJCfRBkXQXrgVFJyRSiUKAlej3Y7HRYIkaBePGYHjU3_eoSQTMFXxIliG7pvqDVdMKGD9D1O_2w2QvecNTn8aKEH-aO56lx8WSMsLFiuP5wVAWIDzuQVwf24fflHmVtlCisD6pd0UTx-YoOUqg2ymg0ngsZcFXx3BJWvUzGZHgokmWyTtBUi5-wuihpsnGkykbuboUwsgH31KeLjo_vpuTG-AE3OnCswfmpqyPOzttC15nI4MjCBf1mQNVueh6ChXroKu62nhJm4eQqiMqujua7V8oRUENzthYRhbGSeJQ94ve_UIxb1mcIiBeblhsxQCQ2yj-3d2_W-O8S57oB1DAd6qmxXJkQ5uyjXZLC_jPZlFn8plNzwai7Juupk4L3LDYSf4pQP6MQZlR4qqFTBE2QyO5cgrSXRGbH6Cy5OHEX4RRaGhfIDKFaZ1G3X8Cn7A2rlWEqdQLvN26kDAj_4kdM1gcEJu-CI-kLLj8w8eKCmq95ovVKDzzXGJI5nmuMMeH9Vrr7Ls_wT8688rsG2NcLT_pFaW5r8TUJAv7HKlIgHm9Yzvv6lSqA_FKuTm5-Ep4ntriUWx-HOtGs7ONFW8TjbcYLRWLpM9Mk7zEPB2L0hM2bdHTYQqJfRcvqitUbUN4QLSBJx4AXv7uRB6_sabyiJmTSw8lY1InWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f1c85d25.mp4?token=bnhS4XKTJCfRBkXQXrgVFJyRSiUKAlej3Y7HRYIkaBePGYHjU3_eoSQTMFXxIliG7pvqDVdMKGD9D1O_2w2QvecNTn8aKEH-aO56lx8WSMsLFiuP5wVAWIDzuQVwf24fflHmVtlCisD6pd0UTx-YoOUqg2ymg0ngsZcFXx3BJWvUzGZHgokmWyTtBUi5-wuihpsnGkykbuboUwsgH31KeLjo_vpuTG-AE3OnCswfmpqyPOzttC15nI4MjCBf1mQNVueh6ChXroKu62nhJm4eQqiMqujua7V8oRUENzthYRhbGSeJQ94ve_UIxb1mcIiBeblhsxQCQ2yj-3d2_W-O8S57oB1DAd6qmxXJkQ5uyjXZLC_jPZlFn8plNzwai7Juupk4L3LDYSf4pQP6MQZlR4qqFTBE2QyO5cgrSXRGbH6Cy5OHEX4RRaGhfIDKFaZ1G3X8Cn7A2rlWEqdQLvN26kDAj_4kdM1gcEJu-CI-kLLj8w8eKCmq95ovVKDzzXGJI5nmuMMeH9Vrr7Ls_wT8688rsG2NcLT_pFaW5r8TUJAv7HKlIgHm9Yzvv6lSqA_FKuTm5-Ep4ntriUWx-HOtGs7ONFW8TjbcYLRWLpM9Mk7zEPB2L0hM2bdHTYQqJfRcvqitUbUN4QLSBJx4AXv7uRB6_sabyiJmTSw8lY1InWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امين عام النيتو في البيت الأبيض يحاول إقناع ترامب بأن الحلفاء الأوروبيين ساعدوا الولايات المتحدة فعليًا خلال حرب إيران.
ليرد ترامب خاب أملي من إيطاليا وبريطانيا وألمانيا وفرنسا وإسبانيا وكان من اللطيف أن يعرضوا مساعدتنا في حرب إيران</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/79821" target="_blank">📅 23:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌟
جيش الاحتلال الصهيوني:
أصيب مقاتل من جيش الإسرائيلي بجروح خطيرة نتيجة انفجار عبوة ناسفة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79820" target="_blank">📅 23:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c6939043.mp4?token=FfZ6SRj0_X5NYIwSTH5J1pNTpszTchFqpQBtcE7xPuCstM6fAIZpPj7qG8ksFjqihyL7IVORiUemmEp5VdH32e5XzyhRT09LyFcpeTZzo7FK-NOVbB0LTBLD4or88VelY9BYkzn8P-xfipm8NGj3e0X5c7YahP31F25Dp3L4XP4Osq4B2JA4d4AY7YDrACMIX9KpysSZMZjV6KAToOOb4A-0Fpw9v3ByYoN5i9jbr3q9XB876v2FijCQvjYanMocXIzKg7ZLSUgugVb7u5OAGiT2X75c2dqbJAuVKaC3VrbGb28mQMYbbW4KDVGhNRNAfVbiXoMKBaofoqzLb6liiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c6939043.mp4?token=FfZ6SRj0_X5NYIwSTH5J1pNTpszTchFqpQBtcE7xPuCstM6fAIZpPj7qG8ksFjqihyL7IVORiUemmEp5VdH32e5XzyhRT09LyFcpeTZzo7FK-NOVbB0LTBLD4or88VelY9BYkzn8P-xfipm8NGj3e0X5c7YahP31F25Dp3L4XP4Osq4B2JA4d4AY7YDrACMIX9KpysSZMZjV6KAToOOb4A-0Fpw9v3ByYoN5i9jbr3q9XB876v2FijCQvjYanMocXIzKg7ZLSUgugVb7u5OAGiT2X75c2dqbJAuVKaC3VrbGb28mQMYbbW4KDVGhNRNAfVbiXoMKBaofoqzLb6liiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
رغم التضييق، يواصل أبناء البحرين إحياء الشعائر الحسينية، مؤكدين تمسكهم بممارسة الحريات الدينية التي تُعد من الحقوق الأساسية للمواطنة في الدولة الحديثة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79819" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79818">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09002baed0.mp4?token=iiOLYsXFxjGG1sRsY6KcEkGmu-OrntMlJ6xR0A1w6t70b1L7g8hcwCg-L5s5Jjb5OxTBJesjKvtiirG6BGrT60y9goAf54ud-octybfe8wnzCMyiga4Pj7kRnJ1KeneKZbNnEkjxlaq2BfKzYwR_-W9uAlqTKL315zc1wVzgSrYcbu2Fp6JbkOj7XkZj2OyD9IUI-c6LbDqyiXHrR1WGKHCOAtYVYGVxGrTts8R1Yv_5vQ3SLmf8NVkHth1rgR88rHS1mVDV_Ngt_j19kdt4vLn1-ImFW5Jm0Z1sVI-cmmGVjwUWqoX_88nRJBwkgbxeY40CxAeB_fHjj_7xU0qyNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09002baed0.mp4?token=iiOLYsXFxjGG1sRsY6KcEkGmu-OrntMlJ6xR0A1w6t70b1L7g8hcwCg-L5s5Jjb5OxTBJesjKvtiirG6BGrT60y9goAf54ud-octybfe8wnzCMyiga4Pj7kRnJ1KeneKZbNnEkjxlaq2BfKzYwR_-W9uAlqTKL315zc1wVzgSrYcbu2Fp6JbkOj7XkZj2OyD9IUI-c6LbDqyiXHrR1WGKHCOAtYVYGVxGrTts8R1Yv_5vQ3SLmf8NVkHth1rgR88rHS1mVDV_Ngt_j19kdt4vLn1-ImFW5Jm0Z1sVI-cmmGVjwUWqoX_88nRJBwkgbxeY40CxAeB_fHjj_7xU0qyNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏ترامب: الحرب تسير على ما يرام. كما تعلمون، نحن نحقق انتصارات كبيرة. إيران تقدم تنازلات كبيرة للغاية. سنرى ما سيحدث ،لكنها كانت قوية للغاية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79818" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌟
🇮🇷
استكمالاً للتنظيم الأمريكي الفاشل في كأس العالم..
أفاد الاتحاد الإيراني لكرة القدم أنه خلال الزيارة الثالثة للمنتخب الوطني إلى الولايات المتحدة، قام مسؤولون أمريكيون بمضايقة سعيد الهاوي ومهدي طارمي، مما أدى إلى تأخير مغادرة الموكب إلى سياتل لخوض المباراة ضد مصر. وينتظر أعضاء المنتخب انضمام اللاعبين إليهم.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79817" target="_blank">📅 20:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d12ba221.mp4?token=Ae9l0t0fcSo5WwGWEpAavNnhYPWN1EzCjcBBlUS6njJ68v7JTVhF-_vZNeWbeq_9UOkSZfCrNey-_wJ5ueox7Nh1UOCK0LxO9pKup-UFybjtZtLZTXXYYxWSRomNuueXx92F9qbeCxK8VXB3J0rNATOcpU70JQ_BU9ygiF06fBfSEUIw6HHqs-RX9sTMzlGQhrCbshGLuSt_JmVRDTwQv6iffI3FKFirI85tEyvb6TfLb9M9sSooyPQl1BSWHhRgb4FQP9lKILRIa1VS8rJ3HoUoB-V-G7nMc3KJ4OboVyMI6TX2l9Isy_yOA596wEZmlpJJMg-UWnjxxL9-67F_ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d12ba221.mp4?token=Ae9l0t0fcSo5WwGWEpAavNnhYPWN1EzCjcBBlUS6njJ68v7JTVhF-_vZNeWbeq_9UOkSZfCrNey-_wJ5ueox7Nh1UOCK0LxO9pKup-UFybjtZtLZTXXYYxWSRomNuueXx92F9qbeCxK8VXB3J0rNATOcpU70JQ_BU9ygiF06fBfSEUIw6HHqs-RX9sTMzlGQhrCbshGLuSt_JmVRDTwQv6iffI3FKFirI85tEyvb6TfLb9M9sSooyPQl1BSWHhRgb4FQP9lKILRIa1VS8rJ3HoUoB-V-G7nMc3KJ4OboVyMI6TX2l9Isy_yOA596wEZmlpJJMg-UWnjxxL9-67F_ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
جيش الإحتلال الإسرائيلي يعلن عن خرقه لوقف إطلاق النار: شنّ الجيش الإسرائيلي هجومًا على شخصين مشتبه بهما عبرا المنطقة الأمنية في جنوب لبنان، وشكّلا تهديدًا لقواتنا.  قبل قليل، تم رصد مركبة تقلّ مشتبهين عبرا المنطقة الأمنية في منطقة مرتفعات علي طاهر، وشكّلا…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/79816" target="_blank">📅 20:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79815">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed3ef8188.mp4?token=LNYmC5kA4PfqHjHuATa5EUYj6wDgW39boOsc86MXYlKy1Ga2CCAxpx_8ToI1pX9DlIjTDcTK8RcW26e8Em9ldwx7oh4-Zx2LR_xg90qsmg-u1_nQjWrc9j7fr_lLDwTZwhhFM7Fmz8S-fZle7OvLCptan3BE6itapOKQC1HJiSvYW6Bai7relHWgF5ox7gsf6bKCXVooptH4lmdH9qk3gUoC5b6qcoUmSHublVM7ok9PoFdDLz_ICBwCwQ_92z10HKA7jSOkH31lyAlLkYCAca2BgX_uD2XJwQktRdBneO3sQR5z_gmOvo5I3yFKdZF5PYvQQm_fr1BrpWhIafjGXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed3ef8188.mp4?token=LNYmC5kA4PfqHjHuATa5EUYj6wDgW39boOsc86MXYlKy1Ga2CCAxpx_8ToI1pX9DlIjTDcTK8RcW26e8Em9ldwx7oh4-Zx2LR_xg90qsmg-u1_nQjWrc9j7fr_lLDwTZwhhFM7Fmz8S-fZle7OvLCptan3BE6itapOKQC1HJiSvYW6Bai7relHWgF5ox7gsf6bKCXVooptH4lmdH9qk3gUoC5b6qcoUmSHublVM7ok9PoFdDLz_ICBwCwQ_92z10HKA7jSOkH31lyAlLkYCAca2BgX_uD2XJwQktRdBneO3sQR5z_gmOvo5I3yFKdZF5PYvQQm_fr1BrpWhIafjGXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
ترامب:
الحرب تسير على ما يرام. كما تعلمون، نحن نحقق انتصارات كبيرة. إيران تقدم تنازلات كبيرة للغاية. سنرى ما سيحدث ،لكنها كانت قوية للغاية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79815" target="_blank">📅 20:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79814">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🌟
🇮🇷
‏
وزير الطاقة الأميركي:
إيران لن تكون قادرة على إغلاق مضيق هرمز بعد الآن.
‏الألغام الإيرانية أخرت عودة تدفقات النفط إلى طبيعتها  في مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79814" target="_blank">📅 20:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79813">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌟
🌟
خروقات مستمرة لوقف إطلاق النار.. غارة معادية على النبطية فوقا وقصف مدفعي صهيوني على بلدة ياطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79813" target="_blank">📅 20:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79812">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhSPSI7-NWLTGKGc2TqJlgQy_YhA8ta_n4dAd2eRvsEnG163EPxmlTGDBlttNZjqv_Q8yDm470a5XQO9G5ymD-4QmH8qZJqMJfvY1_tKOAbFHAfykm3b4SXOIOVxYghwZCieIkQublkpwny8e1QTf5PBQnLb53mp7bkctG2g1vesu8YnbuTYySzqRWzdIyoPJx9Xfn9rFbeG7fwKFZrdFykUWUOK1WzyiGignqnXAGM3r5RDbhTn9sak0HSXS9nufR6ALiiIlwoY974rzLuZqPtMqkSB_d7R0eCA-aikItf27dJ42FK61mnQid0hXDsw_qnDFjOjIP-UdsuGjExXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية:
لن ينخدع أحد؛ لا يمكننا أن ننعم بمنطقة مسالمة طالما استمرت النزعة العسكرية والتدخلية الأمريكية، واستمر وكيل الاحتلال التابع لها، مع الإفلات التام من العقاب، في شن حروب لا نهاية لها في جميع أنحاء المنطقة وارتكاب الإبادة الجماعية والعنف الإرهابي وكل أنواع الفظائع.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79812" target="_blank">📅 19:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79811">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiqhMoTHEO0tGvFUcf091xMs6ow4nDyrGI62aksAeIot73ImO0Wefmns126N9_25Fn0spZ4kuntMLjm8Vy712OqWFMarlWgFXHkwOF_LlRuMa3tclNCTAz9FY6qSanLpSc_je8JpsCJ5aaN2hgf4hikcr2d-4cIKNySPQZA1xhO4QEto_3Ld2P5gUPiK90JrANzSkRH8ypFGjRDCttXiJI1W6ymkudOrUAna3ZZpfhVu-KgmowBOTDrgYkHss5FcP53B7RSd4poknyH1gXaJy8rtWAwxTcsjRpkjbR4rtButFBZXJEpHZQnJdRw3cZxOme_G5eAFa2U5nLygPvaX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
طائرة أمريكية تطلق إنذار الإستغاثة (7700) فوق الأراضي الفلسطينية المحتلة بعد عودتها من أجواء غرب العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79811" target="_blank">📅 19:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79810">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⭐️
علي الزيدي:
العلاقة مع الولايات المتحدة ستتحوّل من عسكرية إلى شراكة اقتصادية.
معظم الفصائل بدأت بالفعل بتسليم سلاحها للدولة.
بعد انسحاب كل القوات الأميركية لن يكون هناك أي مبرر أو حاجة لأي مقاومة في العراق.
نريد من "أوبك" زيادة إنتاجنا النفطي بما يتناسب  وقدرات العراق النفطية وعدد سكانه.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79810" target="_blank">📅 19:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79809">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
روبيو:
الرئيس ترامب يريد أن تلتزم إيران بمذكرة التفاهم وإلا فلديه العديد من الخيارات بينها العودة لفرض عقوبات.
اللجنة الفنية ستعود إلى سويسرا يوم 29 الشهر الجاري لاستئناف المحادثات مع إيران.
المحادثات الفنية مع إيران تتعلق بالملف النووي والعقوبات.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79809" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79807">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HKQ6Jt-w6-CNIILBI3MPAH162HH55ObaTydGikWwfjmIeCnoXhQAuKX7c3UVAKNDkbKSR7wyXZFFsTiiz0f0JFkaKwr1x_huKPhFNlZFJomgHeJBNRYINvFlJvpm1wXyBzoYINXHf-gI2zGCdhLpbrxQcMb4mKieKJKAGx4cFFpTWmvBSMwXFIHYCixdkmFP2LEKARXtU9NoM92slcm9Bb8rJHELPD2FCWQA-KEBpIwR2jUSZ-Hzb0c5FAtmCuuYTi-al8nXoN9H42r29baKEJTSxsIZsdT0uHzBnVv7L3B8hwKpIabH4Nn42DY_L6fFc_pJegpt3vbwKBe-0GA3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flt_uu82CinfcWSy44rVGwN2NBAuPVBZTJ2-MAG18MG8HmONa8T3cVvnrQRn-r1q0b0RjadRsKsxfVddr7nlY7OwYwH8yML6xWEp8B9PGPoRV36YlHOdLQ6W0Pliq9GoRM7WsHbr7pfSeh-_dv_laTxan-GdbOsR5wSGfZT1cFz4u2gVYb3p80J9pM4CjTSzTlojE-KrpTKwcNAZYFFTUkrkTyGb_g7rOaQ1Rm8e9U6IoxuP0AK8Icjkho4fden5ts6EQ4kGe-bBHmKQAfSx-Q8RytPa1xVdVFfqe_cTDykquxoM6My7uBEsFo3MO2l-MUEH86-qNA7FXhHYXitwFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صورة خالدة لإرادة قوية..
طهران، تقاطع ولي العصر؛ رجل مسن منحني الظهر، وعلمٌ ظلّ مرفوعًا.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79807" target="_blank">📅 19:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79806">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
🔳
🌟
سي بي إس نيوز حول هجوم إيراني على قاعدة أمريكية في الكويت:
يشكك عدد من الجنود الأمريكيين الذين أصيبوا في هجوم إيراني بطائرة مسيرة على موقع عسكري أمريكي في ميناء الشعيبة الكويتي في الأول من مارس/آذار، في مزاعم البنتاغون بأن معظم المصابين تعرضوا لإصابات طفيفة وعادوا سريعًا إلى الخدمة. في مارس/آذار، صرّح وزير الحرب بيت هيغسيث بأن "ما يقرب من 90%" من نحو 400 جندي أمريكي أصيبوا خلال الحرب الإيرانية، تعرضوا لإصابات طفيفة وعادوا إلى الخدمة. إلا أن بعض الجرحى وعائلاتهم أبلغوا أن الإصابات كانت أشد بكثير مما تشير إليه التصنيفات العسكرية الرسمية. من بين هؤلاء، رئيس ضباط الصف رودني بيرمان، الذي امتلأ جسده بشظايا عندما أصابت طائرة مسيرة إيرانية موقع عمله في هجوم الأول من مارس/آذار. تُظهر السجلات الطبية أنه عانى من ارتجاج في المخ، وفقدان للسمع والبصر، وتلف في الرئتين، وجروح متعددة بشظايا، ومع ذلك صنّفه الجيش على أنه "غير مصاب بجروح خطيرة". وصفت زوجته، إيمي بيرمان، هذا التصنيف بأنه "غير مقبول"، إذ أُبلغت في البداية بأنه سيعود إلى الخدمة. كما أصيب الرقيب أول كوري هيكس بجروح بالغة جراء الشظايا، وخضع لعدة عمليات جراحية طارئة في مستشفى كويتي، ويتعافى حاليًا من إصابة دماغية رضية. وقال إن عائلته أُبلغت في البداية بأن إصاباته طفيفة. أسفر الهجوم على ميناء الشعيبة الكويتي عن مقتل ستة عسكريين أمريكيين وإصابة أكثر من عشرين آخرين في الموقع العسكري الأمريكي. وأفاد ناجون وأقارب أنهم يعتقدون أن الجيش قلل من شأن خطورة الخسائر، بينما يرفض الجيش هذا الاتهام، مؤكدًا أن تصنيف "مصاب بجروح خطيرة" مخصص للأفراد المعرضين لخطر الموت خلال 72 ساعة، ولا يعكس بالضرورة العواقب الطبية طويلة الأمد.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79806" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79805">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c62883e3.mp4?token=CjpeYP2bWZmNBmD9QCPICqwEAcXRH0DI3f3VH3-eSl3bUzdO7yGuElM48Q_n5QkPjqJ2xdDTJkedg8cY2i1lsVnVPC6SpfO0obn-wKf6BLHffdgYq8XxWt1AKQ9T_n01xCbOIk_hjx655-d95QPz7w7odsgWVvTAwS5sz5mtsqZocm-8-1gpyZ6IqZ38D-NTNEqELJAywhunVxQ3Ml4l9PfjWDS1A0EvRtuV87Un5kRgZlrZ98xjxiqNwQkeVkGnKu04DuaAiRibr7T2IeOJqjw6WDwbO_l-yfyTgrG0pRbWbX8nt60EOW5Wd2ju3GErcNLXFb-TsKkY8eyUxirUUCV_eImF0695ACGOSKYpJZlW9NopcCG5grytanZ9R7VQ0wdC9Q1OLuz0mwuGOCMcwlXpIr5ptzarpfC314RfM155uDgF-uiPSVD2f1X0W3eOXRPfvm89fnQrhNI_UgFneZ2oGINhkg7biGW6aPOKuNoKdRvlcUUF-6xaqazxlknf-hvrygJMncRY9MgSBc4ZGljd6vJUXtyZC2sZoM-PBuW5iG4rInaPdeX7WCAIUzc_YP5S5KGQTKXsNfIsZt36tY3f6jBqZtvLKw_J_udOdba8s2mDUXTyripcqJhJk1ll_yizRrjZIn9LYNtBKkOckt63bPYLSj3mf3Hw_QZLG88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c62883e3.mp4?token=CjpeYP2bWZmNBmD9QCPICqwEAcXRH0DI3f3VH3-eSl3bUzdO7yGuElM48Q_n5QkPjqJ2xdDTJkedg8cY2i1lsVnVPC6SpfO0obn-wKf6BLHffdgYq8XxWt1AKQ9T_n01xCbOIk_hjx655-d95QPz7w7odsgWVvTAwS5sz5mtsqZocm-8-1gpyZ6IqZ38D-NTNEqELJAywhunVxQ3Ml4l9PfjWDS1A0EvRtuV87Un5kRgZlrZ98xjxiqNwQkeVkGnKu04DuaAiRibr7T2IeOJqjw6WDwbO_l-yfyTgrG0pRbWbX8nt60EOW5Wd2ju3GErcNLXFb-TsKkY8eyUxirUUCV_eImF0695ACGOSKYpJZlW9NopcCG5grytanZ9R7VQ0wdC9Q1OLuz0mwuGOCMcwlXpIr5ptzarpfC314RfM155uDgF-uiPSVD2f1X0W3eOXRPfvm89fnQrhNI_UgFneZ2oGINhkg7biGW6aPOKuNoKdRvlcUUF-6xaqazxlknf-hvrygJMncRY9MgSBc4ZGljd6vJUXtyZC2sZoM-PBuW5iG4rInaPdeX7WCAIUzc_YP5S5KGQTKXsNfIsZt36tY3f6jBqZtvLKw_J_udOdba8s2mDUXTyripcqJhJk1ll_yizRrjZIn9LYNtBKkOckt63bPYLSj3mf3Hw_QZLG88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-06-2026
جنود جيش العدو الإسرائيلي في بلدة العديسة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79805" target="_blank">📅 18:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79804">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruxTAX7U7mCB0JmaI1ObXuhDxPAN1RP8QRb-opNug466Q81vGT53FHhkejw34Q4HyZITKY-FCqaePBMA-_PY8AE18a113-uO9z2gZgT1j94RCnoox-egCOHa-ge5UqmAXiJccqiXsfO_QhJOc48UTuv0lwFqqbMdE_WQsnrCcamwF6NZlkADPuget14Q7uty_zugkJvop0YzXZzJUCT_WLHGxK3MBiGw_cdeDpX2GTh9UA_Dxj7PNgp2OkpNnAWi8PKNo3n1XA14O0ICkVNhC9U7S1lX4w2jdYGHYx_gZLN7EAIdJxhcOn2i7OQ2BnazQHcizPrg4CnEdvhNkifVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
خروقات مستمرة لوقف إطلاق النار..
غارة معادية على النبطية فوقا وقصف مدفعي صهيوني على بلدة ياطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79804" target="_blank">📅 18:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79803">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uvy7Nc8velotjr8nrpd_SL870NGLG_tmv857mGtUY6oHMY72kcFMD-wurYCZbsg6FKdk753UDT5HpRWolBCh2WpEwlF_hwIfjIXpI3aOstjTa0C1Y1Yr8jjyL-a5r0RfBFhDEbhu-Eb4QISGeOuX9JRchxCHNzA7VjobeWFSR3J8jc0xefqgkZH7zzgLOxV9dtUDDBULB9PHFQuHH3FogP5xRQt0wkAAGrLyEEqantCsD_tDs03TxTXBQqeFPbWZcYjsNjZUaRu1MUO4bAs-3EDcCCDfyNTNzf2evo25xB9jZ0Q1vtwaaLUD47-8MRhU9Bd4fdNy7etHk7Wki1Y_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شركة نفط البصرة توجه حقل الزبير: لمتطلبات العمل ولأستمرار حالة الظروف القاهرة في المنطقة وعدم توفر ناقلات يرجى تقليص الأنتاج والضخ ليكون الأنتاج بمقدار (300) الف برميل في اليوم اعتباراً من الساعة 12:00 مساءاً ليوم 2026 / 06 /23</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79803" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79801">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8401d06eab.mp4?token=eyHDDDNuavJjAN3rJyrFv-AR7Ka4_Pq1k8rGmhnUJY77Zr0Gi4ldejPwsLzwAa3EDc5KUuh4CBqQRetyPz6CExRiwBFhrvWFsurnAOwRTZ23XUUZjlNVYsgabR19rbFn1x9jmycuifQEvS9JNLsq1YH6K0g3pv2ckpjl4iZcM9U4nNC9mwVLVlB6arZU4D9vJs9K_i-6Wz2DEa2YzifaVwTsCwsj77QvltULwM5lLXKGBwm6KyDVsaZAL0X8y77URCsG7yJTpeokbNeTRbUXJ_anVBCxR0YcjHkcKnZJlCIIoc9qtS4eVP0Qv1xOyOaSmmLyqDsWfpKWItMh3gtxyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8401d06eab.mp4?token=eyHDDDNuavJjAN3rJyrFv-AR7Ka4_Pq1k8rGmhnUJY77Zr0Gi4ldejPwsLzwAa3EDc5KUuh4CBqQRetyPz6CExRiwBFhrvWFsurnAOwRTZ23XUUZjlNVYsgabR19rbFn1x9jmycuifQEvS9JNLsq1YH6K0g3pv2ckpjl4iZcM9U4nNC9mwVLVlB6arZU4D9vJs9K_i-6Wz2DEa2YzifaVwTsCwsj77QvltULwM5lLXKGBwm6KyDVsaZAL0X8y77URCsG7yJTpeokbNeTRbUXJ_anVBCxR0YcjHkcKnZJlCIIoc9qtS4eVP0Qv1xOyOaSmmLyqDsWfpKWItMh3gtxyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مروحي تركي يجوب أجواء مدينة الباب بريف محافظة حلب السورية، وأنباء عن نقل جرحى إلى مشفى المدينة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79801" target="_blank">📅 18:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79800">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d073efb9.mp4?token=oXU9cmdqqR7IDXd3u5ZF7ObhQvUOzQaaONnXmBAcalkXX3jg_10am1FGN2fvr4qxtSMOYSFobJGv11PcAzyS46IHdV1TVtF7ClbjeTCNzGfqWktz-E8lu636BBHNcksOjlE8emQfuScocittwlA4JJhpup6zqhWxJ6y5z9jmjCRseFOzVwwaW9ydQuj_YC6vpYMyEnCL3JaP2Ks_F8gkNNZjuphHCB6jmXpDdIad6I5hq6AGlmBwBZvvpD5lXXI-zflVNqjbBhwZNsiSORqO1gpQaUmhB9O3J5ex35Wr-QEBiaRh5XoWg71qVnnCEQZ9y1gVCfmJde7IEYAhfSVEsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d073efb9.mp4?token=oXU9cmdqqR7IDXd3u5ZF7ObhQvUOzQaaONnXmBAcalkXX3jg_10am1FGN2fvr4qxtSMOYSFobJGv11PcAzyS46IHdV1TVtF7ClbjeTCNzGfqWktz-E8lu636BBHNcksOjlE8emQfuScocittwlA4JJhpup6zqhWxJ6y5z9jmjCRseFOzVwwaW9ydQuj_YC6vpYMyEnCL3JaP2Ks_F8gkNNZjuphHCB6jmXpDdIad6I5hq6AGlmBwBZvvpD5lXXI-zflVNqjbBhwZNsiSORqO1gpQaUmhB9O3J5ex35Wr-QEBiaRh5XoWg71qVnnCEQZ9y1gVCfmJde7IEYAhfSVEsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
الكيان الصهيوني ينهار من الداخل..
استمرار المعارك الداخلية بين الحريديم والمستوطنين في عدة مناطق بفلسطين المحتلة.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79800" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79799">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCPDDxUzCzR8olOmYFJIvpBSCPxxQpl4bgR2AyGlL_kKb2FGA0VPwoEfcTDDP9gVOY0JQnfDpFuFmxqS67GVymTovnGVuLQnufi5At0I6lFogA6_E0E5mTUeTeI3KnZg_3TYyzR6zb3nxBlqXIBjNfXv_bbM7PNkZe6oIW2ot0rZ_IOzk9zXB5ku4fabRpld769vdFeN6-C3Kak_eDMvf5jcKo_kdjIkp1tjQBO0ttKPMlR5qc89XB2q4VnNsp-d_JKS2ZIeB9BM6JuUmRazIJeEm0IGVgRtMwoPbQfOq2gcbyYrtuQD9_XUU6JHYN530sWMGNU0xZP0r_acfFeIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
يُلغى بموجب هذا المؤتمر الصحفي والتوقيع على قانون الإسكان المقرر عقده اليوم إلى حين إقرار قانون إنقاذ أمريكا الذي نحن في أمس الحاجة إليه.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79799" target="_blank">📅 17:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79798">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🌟
نتنياهو:
نقيم حزاما أمنيا عازلا في جنوب لبنان لمنع حزب الله من شن هجمات علينا.
لا يزال هناك ما يجب علينا فعله في لبنان.
سوف نحمي إخواننا الدروز.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79798" target="_blank">📅 17:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79797">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🌟
إعلام العدو:
إصابة جندي إسرائيلي بجروح إثر انفجار وقع ليلاً في لبنان ويجري التحقيق في ظروف الحادث.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/79797" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79796">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBzD8_UeIJp5HeedGelKdS0luDu2qnGS9j69U01INy3JSacuevnhsTz6LYr4cPuYrhS16-qaDtftQ7nfDt_Ak2zBfx35DKHo9gkPrI0wAd3YhnJ1V3jDL2MKA-afNdvvhy0gXc_KxG66gtd0_NqxrEDrIYFPvPst1vnEGUR11jcTDMKR88ub4jmq6F-YnVhRZwUHop2BSfn9dgGtsiVanziEQn-0TnqG6sGjEOth-psPjtW_ZhN5xEi_HPZLcp-ieOQzWYub7L_aN0YXRlfB8YmobFGZKpHUhLTfsFaid4AP6A958f-sdfmHQ0B6aLdDxr_V9UKz2VJK_z_Pmef3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
سحب العمدة مامداني ثلاثة شيوعيين قويين، وتلقى تصفيقًا عاليًا وشاملًا من وسائل الإعلام الإخبارية المزيفة. تهانينا سيد العمدة!
حققت ليلة أمس رقمًا قياسيًا بلا خسائر، حيث ساعدت في انتخاب وطنيين أمريكيين رائعين، ووسائل الإعلام لا تقول كلمة واحدة.
على مدى العامين الماضيين، أدى دعمي إلى فوز 259 انتخابًا تكميليًا، ولم تكن هناك خسائر تقريبًا، مع عدم تلقي أي اهتمام من وسائل الإعلام؛ أخبار مزيفة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79796" target="_blank">📅 17:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79795">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-2SpQekOoVTia-9rDf-bEa2oFacsYjy0ZBcS-8Yy9FrqTOnQrEJjUXurRCEksJ-JtqeCLy9DY7h-C6yUuAU2ztFsgM8RvhNVpKcxCPF7dHceJAfz2sMQNSTKAleNJdmiJ7xIizS3zDhwGR8hrhtpbwhpm0803QioSLNMzYy1HkRpb9Y9_nwQ_Qg773O8KSE-7lxAOg356wxUc3XUAZ3QuuMSoWMMLUEkBE4d9Ht3T7BPXpXWXErS1q5VtIjkghlJZ1dUUML9gN83-1OyqoJFTjMHMWqNRgTJ_tD4FIU26TzeeFf-kr7_u_dtA6iRfyUX7L8WPNs2RI8twuuoh--ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شركة نفط البصرة توجه حقل الزبير:
لمتطلبات العمل ولأستمرار حالة الظروف القاهرة في المنطقة وعدم توفر ناقلات يرجى تقليص الأنتاج والضخ ليكون الأنتاج بمقدار (300) الف برميل في اليوم اعتباراً من الساعة 12:00 مساءاً ليوم 2026 / 06 /23</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79795" target="_blank">📅 16:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79794">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
سلطة الطيران المدني العراقي:
منح ترخيص التشغيل لمطار النجف الأشرف.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79794" target="_blank">📅 16:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79793">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴‍☠️
‏إير فرانس تمدد تعليق الرحلات من
تل أبيب
وإليها حتى 30 يونيو.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79793" target="_blank">📅 16:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79792">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الذهب يسجل خسائر غير مسبوقة منذ نوفمبر 2025 وسعر الأونصة يتراجع إلى أقل من 4000 دولار</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79792" target="_blank">📅 16:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79791">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64062428bd.mp4?token=VAU3kOdL9nzVg1RZr4fUDAATkKD9aplTLw7uH0axqruQ5iFZJKatqPs9fQ1_Sx3GMT29EIkJO-ZqFiwZ8OPgiS20EwvFsNHOwe8T5WqJk9SyHqZyrSBeo3MU6gK2LRBWZ_5fnjdd9vUC7A0E2WRR1Bi6oiYh8sEw9McgXKqhKMv48MKncBsffo34L4rcy9FEyZknm_6Nd06ISclyTo7RZnT8uFQMNSguR4zu8aDY8XVrYTgSwQX3V6Uy8v2Bz9z_RLsPVZGDeudLJMfYbDsroEzWjcephkPywUFzn-gdHsoWp7kvFdLbCiAJUoNtI_Gqg3D7QVAxivIxqM6Kr72Q2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64062428bd.mp4?token=VAU3kOdL9nzVg1RZr4fUDAATkKD9aplTLw7uH0axqruQ5iFZJKatqPs9fQ1_Sx3GMT29EIkJO-ZqFiwZ8OPgiS20EwvFsNHOwe8T5WqJk9SyHqZyrSBeo3MU6gK2LRBWZ_5fnjdd9vUC7A0E2WRR1Bi6oiYh8sEw9McgXKqhKMv48MKncBsffo34L4rcy9FEyZknm_6Nd06ISclyTo7RZnT8uFQMNSguR4zu8aDY8XVrYTgSwQX3V6Uy8v2Bz9z_RLsPVZGDeudLJMfYbDsroEzWjcephkPywUFzn-gdHsoWp7kvFdLbCiAJUoNtI_Gqg3D7QVAxivIxqM6Kr72Q2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
مشاهد من احياء ليالي شهر محرم الحرام وذكرى استشهاد الامام الحسين (عليه السلام) في مدينة ديربينت الروسية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79791" target="_blank">📅 16:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79790">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امريكا تزعم قتل قيادي من داعش في غرب سوريا</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79790" target="_blank">📅 16:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79789">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIyyw8F6XFSWsRwCrEEFQLDq0IwId1NTjofYNwrEqF7kaqpyNNmEKlWm2mqM9xaxlSIFVGgJZMxFSCDLk1HPyhw5m22U3UmcU5Yj_op1A41VmdffX6MTM9yJdlfvOxVnxweIb38jwh13KuHrkwV7WIbr-hirT9Hl9OyA7w9iRHkh6aT8-dXnAzqpx36PYOxnybJuwo04JmpgaTDdWZBWvVyJFeDAssZpJKnofm0UAoYVpgopxWfEfj1A4XYgnhXjc77fiRbdz8kgaFHS2_w4bNEE7wXOV7fYn55jlvzAtb-wYjRNrnBqgD8WUq0F7gbUjVOYs1EnISCxL-pe0zKtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارة الامريكية في بغداد تشارك تصريحات ‏وزير الخارجية الامريكي ماركو روبيو:
"لا يمكن إنهاء الأعمال العدائية والصراعات في المنطقة ما دامت الميليشيات المدعومة من إيران تواصل إطلاق الصواريخ والمسيرات من العراق، وتشارك في الإرهاب كما فعلت حركة حماس وحزب الله".</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79789" target="_blank">📅 15:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79788">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
بعد الرفض الايراني.. ‏ترامب: لا داعي للعجلة في إرسال مفتشين إلى المواقع الإيرانية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79788" target="_blank">📅 15:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79787">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
‏ترامب: سيُسمح للمفتشين بالوصول إلى مواقع اليورانيوم الإيراني.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79787" target="_blank">📅 15:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79786">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
‏
ترامب:
سيُسمح للمفتشين بالوصول إلى مواقع اليورانيوم الإيراني.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79786" target="_blank">📅 15:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79785">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تراجع سعر برميل خام برنت إلى ما دون 75 دولارا لأول مرة منذ 27 فبراير.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79785" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79784">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزير الخزانة الأمريكي: أي أموال يتلقاها الإيرانيون هي للإيرانيين، نسبة كبيرة جداً ستُخصص للأغذية والأدوية الأمريكية تحت إشراف وزارة الخزانة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79784" target="_blank">📅 15:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79783">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El0weRnUbj_2XNB2ldJ4sE1KGmuo_ewe-uFKUQqR1Ax3haEc5KG5wHbzHKA2jP1ve1BFkW3tAXaDwWPNcD2SYp4mQVLfN7kR94JQLCOLf1ujaWPh2MZiphV9VdULYJTem1Av9Hrm-ri1pneFVaomrkJsWoYhkQrLHIm9lsOkydmS-vqI09bew3S103uMFONOtuDGDBspdxk3iAjNBJ4XD-VOQkBpDLXDLkm4KKeZ_6amkl_R5Nz9lzbXEc_Rnsh4A17BYB8tinBH9rxutZOiN4O5P-PqJku12ONUzCafAbmJxfqC8mQXrOyWu_2vbLV9RXVlukjvknjzz4yUfaXW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
أبلغت إيران الولايات المتحدة أنه على الرغم من التقارير الإخبارية الكاذبة المثيرة للمشاكل التي تفيد بخلاف ذلك، "لا توجد رسوم عبور، ولا تكاليف تأمين، ولا أي رسوم أخرى من أي نوع تطلبها أو تتلقاها إيران على السفن التي تسافر عبر مضيق هرمز. إذا كانت هذه معلومات خاطئة، فستنتهي المفاوضات على الفور! بالإضافة إلى ذلك، لم تُقدم الولايات المتحدة أي أموال لإيران، أو تُفرج عن أي أموال منها لصالحها. سنُفرج عن بعض أموالها، التي نتحكم بها بالكامل، لمزارعينا ومربي الماشية لدينا، لشراء الذرة والقمح وفول الصويا والمزيد. هناك حاجة ماسة إلى الغذاء في إيران، وسنشتريه لهم حصريًا من الولايات المتحدة. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79783" target="_blank">📅 15:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79782">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏴‍☠️
‏
وزير ما يسمى بـ"الحكم المحلي" الصهيوني:
قادرون على منع إيران من امتلاك أسلحة نووية ولكن واشنطن لم تسمح.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79782" target="_blank">📅 14:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79781">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
🌟
السلطات الايرانية:
أكثر من 3 ملايين زائر ايراني وصلوا إلى كربلاء المقدسة للمشاركة في مراسم عاشوراء. اليوم عبر 400 ألف زائر إيراني الحدود البرية إلى العراق.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79781" target="_blank">📅 14:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79780">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e10fb40c.mp4?token=do4SyqnvVvlgMK66MirVr7STQa8V8dRV6ubBEUocQUpmD6_xDSaCCOOUmbibzZPA3XJ-BHWz7H4aIdtA1HoXoyuB6zv23GLagi-EFRKqRJofgvS0mKKaBcV6IkizF-5okhEs0Xz1soALetkAVAIPkdeSw2CgkZFaw8PWo88nkC8uSSv-NM_V4PmLgPJbYU10ZpKJ_KOVnzTTX43UGbYEcIvJ-qREDO1PoMcvv_qIh-qmdQBnJUOoy5NuTosu0xkWh75iSVQhNji9vcRTkYadcr79amIx-ncmcRtuvtE3jfNgHxmZM4CnHuUX1bRAbpHagicu5g8Hi2sqW6mMc_absg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e10fb40c.mp4?token=do4SyqnvVvlgMK66MirVr7STQa8V8dRV6ubBEUocQUpmD6_xDSaCCOOUmbibzZPA3XJ-BHWz7H4aIdtA1HoXoyuB6zv23GLagi-EFRKqRJofgvS0mKKaBcV6IkizF-5okhEs0Xz1soALetkAVAIPkdeSw2CgkZFaw8PWo88nkC8uSSv-NM_V4PmLgPJbYU10ZpKJ_KOVnzTTX43UGbYEcIvJ-qREDO1PoMcvv_qIh-qmdQBnJUOoy5NuTosu0xkWh75iSVQhNji9vcRTkYadcr79amIx-ncmcRtuvtE3jfNgHxmZM4CnHuUX1bRAbpHagicu5g8Hi2sqW6mMc_absg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق هائل يلتهم مصنع في قضاء الشيخان التابع اداريا لمحافظة نينوى وتحتله ميليشيات البرزاني وضمته لمحافظة دهوك.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79780" target="_blank">📅 14:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79779">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
‏
نائب وزير الخارجية الإيراني:
لم يُعقد أي اجتماع مع غروسي في سويسرا، رغم طلبه. كما لا يوجد برنامج للوصول إلى المنشآت والمواد النووية التي تعرضت للهجوم. ستُدرس هذه القضايا وتُحل فقط في إطار الاتفاق النهائي ونتيجةً لإجراءات الطرف الآخر العملية برفع جميع العقوبات.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79779" target="_blank">📅 14:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79778">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
وكالة الاستخبارات والتحقيقات الاتحادية العراقية تلقي القبض على(25) شخصاً أجنبياً أثاروا مشاجرة في محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79778" target="_blank">📅 14:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79777">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏴‍☠️
‏
وزير الحرب الصهيوني:
حتى لو كان هناك طلب أمريكي، فلن ننسحب من جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79777" target="_blank">📅 14:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79776">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇶🇦
وكالة ‏رويترز: رئيس وزراء قطر يبحث في مسقط عقد محادثات بين إيران ومجلس التعاون والعراق حول هرمز.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79776" target="_blank">📅 13:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79775">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇶🇦
وكالة ‏رويترز:
رئيس وزراء قطر يبحث في مسقط عقد محادثات بين إيران ومجلس التعاون والعراق حول هرمز.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79775" target="_blank">📅 13:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79774">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇷🇺
‏
الكرملين:
الأسلحة النووية هي الضامن الوحيد لمنع حرب عالمية ثالثة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79774" target="_blank">📅 13:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79773">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
وزير الخارجية الباكستاني:
التفاوض بين واشنطن وطهران يدور حاليا بشأن البرنامج النووي والأرصدة الإيرانية ولبنان ولن تكون هناك رسوم عبور لمضيق هرمز أو أذونات وتصاريح.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79773" target="_blank">📅 13:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79772">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حدث أمني في أنقرة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79772" target="_blank">📅 12:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79771">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حدث أمني في أنقرة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79771" target="_blank">📅 12:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79770">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇫🇷
أ ف ب: رصد إصابة أولى بفيروس إيبولا في فرنسا.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79770" target="_blank">📅 12:35 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

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
<img src="https://cdn4.telesco.pe/file/AncggfiCU95rumxzJa7ML3cTDnN1NjH_nk7JcelTkrhZjO7enmJUsOKAqv_vNfmJtVRP-VzzBYfXKO__qSmzR7Nd02wBlpzM8Wflc95ZDWtdEwQ5ZcPC7gg-uN7MJQQH_q3cLY2c4NWAHgMwTQqWJURgCyGlDrWw4Q-aMAHQdCLNTmyTKPrWg50eEzQMWnN4WI_iVbT_nV3ZxedVv3hHBdf3nBXcn9sFTCtdMAPPikzAp2tenASRdpbhztlL9d3w5Rn5ZrK4KIiorvnv1II4EI0n4Rp4Z3N3CLlcK8iO-IWpBl5Epue2MQ58CebKjzRBlqVT9MvYVEbTMgoV7FoZGg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-86184">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmDU22ybfrUdRJSoEN81-cwDjsq9O2xOGLRQHxVbwDB-cABgHR6tF3icJbwZJEGd-yxhJzISFkg8g3HS11Qz5LC4VeerJ77eDKQKc-aT5zEnwJJD0hGsezObpKGjP73RCuetpg3CgRU15na7MlM3fR4fBPy2r_ExFC8iWV9D_HZGGHOtAOD0pMq1Z1b_wi6ZGPukDndKlrOIF3oeeouJX33NaDBuBvY7z2JIVI1FZvhPOeeHHymlbJKDG0DUQk03HKcEmaw2hPX6znebsQ42mxYjUwn5nbrlQW5sc7_UINSKfsNotLguR_2YvWUar9btVjZ5JGY5ks0MXyka_zhYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZHUPLNEieDH3fYitONzFzwtjJOZKrw-dgZ34y66f8I9wauSzEeOvuWwiFg8_dIjTGHJ4aD6yRgb9MhLGGCev1TE0ilEebsRYshpt1z_NMUBQ3hwKKA08M9aJ6EQCzhVoCjC5z90nN8eK8ZnmV5mvjdKZtaEDMEsPi56LZGsTX9ke0KG2jWR-ce9XaAZCKrkuB-ch_nLr48w5oZA1XegrdQGA29--hXKOy8AUt1Zfi2GBLCCFEXLCmuC4QoCI8euaT-VFUDs8ETbDxHSwhlpiJx_VC7SjXJDSOZgy78Q9Enl-ROBcd5hEC92--FRQMfBEe_2F-fMEkrEbavdWJTARA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استعدادات للتشييع في العاصمة بغداد وغضب يعم المشيعين وسط مطالبات للرد والثأر</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/86184" target="_blank">📅 16:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86182">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSPOro0X-orLcGaFCVyvIf7kwuCqeB4O4HJJy0_ke0OtKWX7jdpEEFeLVsdVZnjL7uiHIUszdK-DuFwsKOOQ0-jA9YPzhMi7QVievpEasGqSg-OifoNa1rdGhlcb7AAZC2tb1B41UWkOoIwULaT_uw4e4G5sfEOsa0bMsLDmd-0y02wNJehb6_y3Va8NsjH8KWXFFiya2vjozSNWzgn-lfluZwMVrUVZnVo_i9QFG6_GkVemhPpjQ8NByZf0y7EmF4v7nuwDQXAQTNCcjKbaIGPYSo1GF4IzDSA2sLJii-bxOESRlkzVvpHPEvNexPWX07_YeC7ZoUcQDlG1LXKeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqoenx3NYWZkX94yobgZS0ftLxxQ5KJjE0EaYNAsdRwCS3ML_81pmd5Yzo9HW6C0M_EMFIn43E4oBGwfrE843BmW6onwyoWLS5lodH_wtrxCE7Gv_d8FhT9cQEo4CDWQvfm2K6L-2bzLRq2hUpJF4aOe7bejpZzPKT3i0X27kEia8Q1TswxyvrnAYgG6KUzT6Qs6E1yMKPYhzlAn6KoL6DbvFMo3A3dLp552_VeagN0nmsd2VfDFfwIBP5Vt1WPi2nX6Jtj_Gywr6A8wHExxL5lftU0CZUYGjn2R4o9LeFH9leYY1PegaG82un4F2KJ3MT6CI6gFiudZ9eo_MSzhuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تحركات امريكية واسعة في الشرق الاوسط ‏استعدادا للهجوم على الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/naya_foriraq/86182" target="_blank">📅 16:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86181">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/86181" target="_blank">📅 16:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86180">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJWCShKardVaTUX2i1RRh5mfB1BfeVWcVhLby4ao_xrvs2C3uxCUOJ9JRMzxwRu-S0zBw5K2EcRkteqhzKPBi_pf5OkD8AbMzJT2R3klI_B2_o2dGHkWJz3cupDRw49oYEZs8sKThs-yDgdhY0HkMgfRYxCmQisekRpACtNt7IcLiFlLHO_fcxu0ZTeCAZuXwgvS3-PxZQxMztSJAeDbgy3NeZthV0RWV7JlO2ZxR3Vl14FtULyQnhxC32Ai-MPDzosQPN6Vf1dHqhaoXfKX7CZ9f7DwTAvh8JxK7rQFQLdc9rU3grRmKSQ2QKA1jPBjwq_rE0h4_q-uKnOQ-9wm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
﴿فَلَا تَهِنُوا وَتَدْعُوا إِلَى السَّلْمِ وَأَنْتُمُ الْأَعْلَوْنَ وَاللَّهُ مَعَكُمْ وَلَنْ يَتِرَكُمْ أَعْمَالَكُمْ﴾
صدق الله العلي العظيم
لا حول ولا قوة إلا بالله العلي العظيم وإنا لله وانا اليه راجعون، الرحمة للشهداء والشفاء العاجل للجرحى، ونؤكد على ما يلي:
1- إن الدولة العراقية لا تُدار بمنطق الصفقات التجارية أو المصالح الاقتصادية عندما يتعلق الأمر بسيادة الوطن وكرامة شعبه؛ فسيادة العراق ودماء أبنائه ليست محل تفاوض أو مساومة، وهي تعلو على جميع الاعتبارات الأخرى.
2- ندعو الحكومة العراقية إلى إعادة النظر في جميع الاتفاقيات والعقود التي أُبرمت مؤخرًا مع الولايات المتحدة الامريكية، وإلغاء الزيارة المقررة الى الحجاز.
3- إننا في المقاومة الاسلامية سرايا اولياء الدم لازلنا ننتظر موقفًا رسميًا من الحكومة العراقية يرتقي إلى حجم الحدث، ويعبّر عن الوفاء لتضحيات الشهداء.
4- يجب طرد السفير السعودي من العراق فورًا، وقطع العلاقات الدبلوماسية والاقتصادية مع السعودية.
5- في حال تقاعست الحكومة عن اداء واجبها فعلى الشعب العراقي الغيور المطالبة بحصر سلاح الحكومة بيد المقاومة.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/naya_foriraq/86180" target="_blank">📅 16:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86179">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs6TlbG3_HStQ3__LcjsD3M7eFcFGXABoeItPsXnmi5RwuMRLnFflWba3Z-CbwcrI_jjM1EDgc5RfLK8_fnd_F1x3qhVX0VxeVlk4feXU-kVHkvDwE9xbsboViskdhcnYBwO_2t_H5fkrJqoN1hGAhYMXml2Wwr30J9xXwCtUpL2xHJ2R5h9iWZI52MtFDw4xtDIXOuO2SXyr24XrfZuybMhnbaBCymw7ebG0lZNGi9WQVe4yMSc7K5H6GMWXkwjzj8juUjRwmB9scwJqAvgKJIlNu6rL6TJ_p_tBpSrazNqPJjEssr32pqSYzqCAtXF6kO8X-TJTTy4XOUsSsCS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
خاص لنايا | مشاهد من الاردن لتصاعد اعمدة الدخان بعد الهجوم الصاروخي والمسير.</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/naya_foriraq/86179" target="_blank">📅 16:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86178">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بيان لرئيس البرلمان العراقي هيبت الحلبوسي يرفض ايضا تحديد هوية العدوان:
ندين بأشد العبارات الاعتداء الذي استهدف مواقع تابعة للقوات الأمنية العراقية، والذي أسفر عن سقوط عدد من الشهداء والجرحى، ونؤكد أن هذا الاعتداء يمثِّل انتهاكاً مرفوضاً لسيادة العراق، ومساساً بأمنه واستقراره، وتجاوزاً على مؤسسات الدولة الأمنية التي تؤدِّي واجباتها في حماية الوطن والدفاع عنه.
ونشدِّد على أن سيادة العراق ووحدة أراضيه تمثِّلان خطاً أحمر لا يجوز المساس به، وأن احترام القانون الدولي وميثاق الأمم المتحدة يقتضي الامتناع عن أي أعمال عسكرية تنتهك سيادة الدول أو تهدِّد أمنها واستقرارها.
وفي الوقت ذاته، ندعو القائد العام للقوات المسلحة إلى إجراء تحقيق شامل وشفَّاف في هذا الاعتداء، واتخاذ جميع الإجراءات الدبلوماسية والقانونية التي تحفظ حقوق العراق وسيادته، بالتوازي مع كشف الجهات المتورطة في أي أعمال عدائية تنطلق من الأراضي العراقية باتجاه دول الجوار، ومحاسبة المسؤولين عنها وفق أحكام القانون، التزاماً بما نصَّ عليه الدستور العراقي من عدم استخدام الأراضي العراقية مقراً أو ممراً لأي اعتداء على أي دولة، وعدم السماح باستخدامها منطلقاً للإضرار بأمن واستقرار الدول المجاورة.
ونجدِّد التأكيد على ضرورة تحييد العراق عن الصراعات الإقليمية والدولية، وعدم جرِّه إلى أتون الحروب، فالمصلحة الوطنية العليا تقتضي أن يبقى العراق ساحةً للاستقرار والحوار والتعاون، لا ميداناً لتصفية الحسابات أو تبادل الرسائل العسكرية.
خالص التعازي والمواساة إلى عوائل الشهداء، ونتمنَّى الشفاء العاجل للجرحى، سائلين المولى عزَّ وجلَّ أن يحفظ العراق وشعبه، وأن يديم عليه نعمة الأمن والاستقرار، ويوفق الجميع إلى ما فيه خير الوطن وسيادته ووحدته.
هيبت الحلبوسي
رئيس مجلس النواب
29 تموز 2026</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/86178" target="_blank">📅 15:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86177">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6c54053f3.mp4?token=nM0A6j9ZJlnFWtOXkRwruAab4UHFI_KqSVHg46PumN1uZYZRuJaGUQd_u-It4ghMVm8L5P2BDkCsiJTbYdvXAAZE8WJIERdqpHySG3OaDPd8ybcjMbBMXJ-RHZ7lJKTKTDk4H9xB2gHNNMbgQ5SPvohx9ipqfslxjgXEijUj-DvusRhTiFPLrYBUQax7PbOUuiIN7KWqjB_WSe1_EDx7wOe46vtrCMV8s0w-Ru2HqR-cCvSvJvYSQQL0QkqCJslH_8QVO93L7WjviEhWsbiDlXjo-OZxVFESC-ibeKBRBOaDoHdYmxX0V90olvJ9S-_sWSypKZUpLvnFA-U6hwmL1HTqjbKvLq65eJgl9O_LKtdqnqxafKz6i_zw8d7VKc3QXvlnElDB_U7UoIhyI-1FFHkNxQKlPALikdMlSfRserJZ1OflnmAwg4FsW5sBgcROh6ynqs_GTCcTY318SwrPQA2qgiLQhX24P99ks3H9xvcK5yw04BwPEHLZsUrliyrPMmpUdrcmI9yllJgPY8YEDSBac38aFOZcdp668pxvd5k29lgQ6iVMHlx8Rs5eBnfhQS_FkdRU_dBrCoEZ7NsPbMrQf-JW35zPiOoWmx2hdkG1zROkNJe6Oec2W5XEmgZBuj8JdMSlsRyQ0dlnvjOEu809sYSqGrYp3fBhKbaCvNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6c54053f3.mp4?token=nM0A6j9ZJlnFWtOXkRwruAab4UHFI_KqSVHg46PumN1uZYZRuJaGUQd_u-It4ghMVm8L5P2BDkCsiJTbYdvXAAZE8WJIERdqpHySG3OaDPd8ybcjMbBMXJ-RHZ7lJKTKTDk4H9xB2gHNNMbgQ5SPvohx9ipqfslxjgXEijUj-DvusRhTiFPLrYBUQax7PbOUuiIN7KWqjB_WSe1_EDx7wOe46vtrCMV8s0w-Ru2HqR-cCvSvJvYSQQL0QkqCJslH_8QVO93L7WjviEhWsbiDlXjo-OZxVFESC-ibeKBRBOaDoHdYmxX0V90olvJ9S-_sWSypKZUpLvnFA-U6hwmL1HTqjbKvLq65eJgl9O_LKtdqnqxafKz6i_zw8d7VKc3QXvlnElDB_U7UoIhyI-1FFHkNxQKlPALikdMlSfRserJZ1OflnmAwg4FsW5sBgcROh6ynqs_GTCcTY318SwrPQA2qgiLQhX24P99ks3H9xvcK5yw04BwPEHLZsUrliyrPMmpUdrcmI9yllJgPY8YEDSBac38aFOZcdp668pxvd5k29lgQ6iVMHlx8Rs5eBnfhQS_FkdRU_dBrCoEZ7NsPbMrQf-JW35zPiOoWmx2hdkG1zROkNJe6Oec2W5XEmgZBuj8JdMSlsRyQ0dlnvjOEu809sYSqGrYp3fBhKbaCvNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: تم تنسيق الضربات الأمريكية والسعودية مع الحكومة العراقية</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/naya_foriraq/86177" target="_blank">📅 15:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86176">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامب يقول ان الهجمات بموافقة الحكومة العراقية</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/86176" target="_blank">📅 15:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86175">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بعد قليل ...
بيان هام للمتحدث العسكري للمقاومة الاسلامية سرايا اولياء الدم
ابو مهدي الجعفري .</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/86175" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86174">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامب: تم تنسيق الضربات الأمريكية والسعودية مع الحكومة العراقية</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/86174" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86173">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامب: ردًا على الهجمات التي استهدفت أهدافًا أمريكية في الأردن، سيتم تنفيذ هجمات على إيران.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/86173" target="_blank">📅 15:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86172">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏ترامب: سنضرب إيران بقوة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/86172" target="_blank">📅 15:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86171">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏ترامب: سنضرب إيران بقوة.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/86171" target="_blank">📅 15:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86169">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdihB0WqOATaYZSghIw7qpWnfyncWLEsovuUX9SBHoiUDldS318lMt4zI0zIVFcUTW7t8CTDNe_QkFjQpW08aXUjILpUH6VATXEmlJkTIgf68NE-pnFikRhmLsfBJkUy2Z1zlfi0cGqY5TD7pbCVtNUMIhSMAYjdPkcRvVk_qQBM1OfIA_H9EltOL7lMqvdGkyaVI-kTkgRc3co8tr_a1BG8CpWXCK1LRBwW0FIRtPZ4_eGohTUQgvlNYXUCBgbo3PvkdQvmxULT--0Y-bH0rE0jwfwS-IKDYw0BZsahTC8fM-99CwufRqifzKySLfhkethV3ftNMjRDh3XIwjMxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tS5wyCf1k-eEPFzdNyBs3urVy00wqAC-ErD0cZXJc8J5lK-Px7qJb61b-NDGBs_hU-VHgihnqkbMbi7_TKmX0Qf3gxipDcluklGbm6lnHLL_53LRASNCZFDzQW9haoinC2h0wi5W_mQ7bIa286hqY18WdfeOjdit2n-qvmtxA3hW9YoIy1Q_hWmtRd3LAKUHXAXUR_pZBFI5aOXhmlni29C1PXjHzn_8KNCc9-qiaHj1nMBc19EB4hZORvS4F24XV_aQvr9sDfx8IQ3c8xChwCLDxEwkaNCR6PZ9ULyYx5ISHtwdW7ZKBWBEB6DDCfEzd4nA5rqVpPew4lESHp3iHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
النائب سعود الساعدي يوجه اسئلة إلى كل من رئيس الوزراء ووزير الخارجية:
ما الإجراءات العسكرية والقانونية والدبلوماسية التي تعتزم الحكومة اتخاذها، بما في ذلك إمكانية إلغاء زيارة رئيس الوزراء إلى السعودية واستدعاء السفير السعودي وتسليمه مذكرة احتجاج واتخاذ إجراءات بحق السفارة السعودية فضلاً عن تقديم شكوى رسمية إلى الأمين العام للأمم المتحدة على خلفية الهجمات.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/86169" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86168">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">كلمة الشيخ حسن الشبكي آمر الفوج الرابع في لواء 30 سهل نينوى الان بعد وصول جتْمامـ...ين السّْهداء الى العاصمة بغداد...</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/86168" target="_blank">📅 15:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86167">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نايا
المجاهدون العراقيون الذين تقدمت بهم السن يظنون أنه إذا فرّوا من المعركة، فإن المعركة أيضاً ستهرب منهم!
كان الخطأ الأكبر في حسابات جبهة المقاومة أننا كنا نظن أن خفض مستوى التوتر سيجعل العدو يتراجع أو يغض الطرف.
لكن العدو يستهدف وجودنا نفسه، ولا يفرّق بالنسبة له بين ….. والكعبي.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86167" target="_blank">📅 15:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86166">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نايا
إنّ التجارة مع الولايات المتحدة، ولقاء السفير الأمريكي، والانحناء أمام ترامب، لن تحمي الإخوة العراقيين من الضربات.
لقد انتهت فكرة الحفاظ على النظام الشيعي في العراق عبر مسك العصا من الوسط بين إيران والولايات المتحدة، صباح يوم استشهاد قاسم سليماني!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/86166" target="_blank">📅 15:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86165">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">المجلس الأعلى الإسلامي العراقي
نستنكر بشدة العدوان الأمريكي- السعودي على العراق، واستهداف قواته الامنية الرسمية في الحشد الشعبي، وما أسفر عنه من سقوط عدد كبير من الشهداء والمصابين، ونستغرب ان يأتي هذا العدوان تزامناً مع تحرك حكومي عراقي جاد لفتح صفحة جديدة من العلاقات مع دول الخليج، بعد ايام من زيارة السيد رئيس الوزراء للولايات المتحدة وإبرام 48 مذكرة تفاهم ضمن توجه لبناء شراكة اقتصادية، والانتقال الى مرحلة جديدة من العلاقات.
إن ما حدث من عدوان قد يندرج ضمن مسعى "صهيوني أمريكي" لمنع دول المنطقة من بناء تفاهمات مشتركة لمستقبلها الامني والاقتصادي بعيداً عن التدخل الاجنبي، فضلاً عن الحيلولة دون استقرار العراق، وبناء اقتصاده، واستعادة دوره كمحور التقاء دول المنطقة، وكوسيط إيجابي لتذويب خلافاتها وبناء تفاهمات دولها.
نؤكد ثقتنا بأن العدوان لن ينال من إرادة قواتنا الامنية، ولا عزيمة شعبنا، ولا مكانة العراق ودوره، وإن كل المؤامرات مصيرها الفشل أمام إرادة شعبنا العظيم.
نسال الله ان يرحم شهدائنا الأبرار من أبناء حشدنا الغيارى، ويمنّ على المصابين بالشفاء العاجل باذنه تعالى.
د. على فاضل الدفاعي
الناطق الرسمي للمجلس الأعلى الإسلامي العراقي
٢٩/٧/٢٠٢٦</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86165" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86164">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مقطع يوثق آثار العدوان الأميركي - السعودي على مقرٍ للحـشد الشعبي في سهل نينوى</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/86164" target="_blank">📅 15:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86163">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الشيخ قيس الخزعلي: إن قيام دول أجنبية، يدعي بعضها أنها حليفة، والأخرى أنها شقيقة، بمهاجمة قواتنا الأمنية وقتل أبنائنا فيها، بدعاوى لم يتم إثبات صدقيتها، ولم يترك المجال للقائد العام للقوات المسلحة لاتخاذ الإجراءات القانونية والأمنية المطلوبة في حال ثبوتها، هو انتهاك، بل استهتار، بالسيادة العراقية والكرامة الوطنية، وهذا أمر لا يقبله أي عراقي شريف.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/86163" target="_blank">📅 15:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86162">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzz2J-YKuLWYllcdKBFBUe4Lf872hEvKpKqpsurP-ZpF9BJMinAHu1Zd-GIvt2qcDZ82q2tJ7-R3cyqSx8ZLt-sHZVSZw7VioBycUWi3mK0M74i4Fr79T1Z4iTcJtO7YCYa4IGVw0LWblXkRWNbLstmGQfc_tDQFfQacb8Q_DzL8R63YypNHXRFixZC7Qrc8LYE85qmNWR0ywuTOSimX_sAo6wu3Nx6mM-_i3ynu_f4tfADXunGkBiKOMwDz1kDpgx0o5LKtaNMX8nwiumE4_ofXnlRIcnJNC3uaoCfA592Ef4F8ajrmKxmwq_aieHwaMRso8w7Ue-VPhb4o5fr2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">A night before the incident</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/86162" target="_blank">📅 15:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86161">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3eFZ86ZRZiA5nRaHcaxaUyBBdM7GG5vW_TrW5uye_IvVdMD3TkP_WPDD1RxGoT93gYZXbLMHqpfC_-PcokFGn_Bq_XpWiV3FXcQjii2h5jlBL_PP6xy5rkF6eP7M8LjZbnFuNy1EPItItizQWceUBONyf1tJfjDVbyGg0PXuzunVRvLu0lq4dXv7xTvuwW-lkxg-ZLmMDWZ5901zG0eEU0pP80J-dr5xk5YXcAXGlEteYnapsCfD6Wryi_JkLv4arGETtKTaoPNNw9Wx_abQ8_uQdaOqdDFBceMBDwAgokl1oLIYnUs6W4LUNv5WEm_IlGlFYnz_HDWRJKx4PLpUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسين مؤنس رئيس حركة حقوق ينشر</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/86161" target="_blank">📅 15:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86160">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ef8Bf69eISsObtMNocwG7LUv1wqu4j-8_hczxDOQpuqSPfyJkdkdp27VIEc8D09vbgKZl4wRx5OhVWzZQFpywkICU34bw_e9DnWnYUSQyFML1Is3-YwRxJJfkHjQtSFvpa2cNmpEpCTaaHMo2xhjipYTU5IFdWzi8a1E0YccOMGTDvdVc0AITQ40nK7PWbmqT17WugQT0Gj8KfzkMJGjZ7RSVG9u30kGIrteXy0nnH8AMe_NrryCO0Ew4Q3UocgYHpkHYx94bsQAEp98oquCHvstzThxQwiDdSrfrT1a_Z6bADnXmBqnNQh5Npb6ItL2Yct4b0QFbtxmIXnOfz5V1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐦
بيان صادر عن حركة النجباء
:
بسم الله الرحمن الرحيم
﴿وَسَيَعْلَمُ الَّذِينَ ظَلَمُوا أَيَّ مُنقَلَبٍ يَنقَلِبُونَ﴾
تطل علينا قوى الاستكبار العالمي والتبعية ممثلة بالاحتلال الأمريكي الغاشم والتحالف السعودي المأجور، لتؤكد مجدداً وجهها القبيح وعقيدتها الدموية القائمة على الغدر متجاوزة كل أعراف السيادة وكرامة الأوطان..
فجر اليوم امتدت أيدي الخيانة والإجرام لتستهدف بطائراتها وصواريخها الحاقدة عمق المدن العراقية الآمنة في عدوان سافر يؤكد بما لا يدع مجالاً للشك أن هذا الحلف المشبوه لا يعترف بسيادة ولا عهود، بل يسعى يائساً لإركاع هذا الشعب الأبي الذي قهر طغاة الأرض..
إن المقاومة الإسلامية حركة النجباء إذ تدين وتستنكر هذا العدوان الأمريكي السعودي الآثم، فإنها تؤكد للجميع أن دماء شهدائنا الأبرار لن تذهب هباء وأن الأقنعة قد سقطت إلى الأبد تحت وطأة الحديد والنار، وأمام هذا المنعطف التاريخي الخطير نطلق مطالباتنا الحاسمة وغير القابلة للمساومة، موجهين رسالتنا المباشرة والحتمية للحكومة العراقية والجهات الرسمية بما يأتي:
أولاً: طرد المحتل وقطع دابر العمالة: إن بقاء القواعد والمقرات التابعة للاحتلال الأمريكي على الأراضي العراقية بات خطراً داهماً يهدد أمن البلاد واستقرارها.
ثانياً: قطع جميع أشكال التعاون مع النظام السعودي المجرم الذي أثبت أنه رأس الأفعى وممول الإرهاب ضد العراق وأهله.
ثالثاً: نطالب الحكومة العراقية بالخروج الفوري عن صمتها وعدم الاكتفاء بيانات الشجب والاستنكار التي تغري المعتدي وتدفعه إلى التمادي.
رابعاً: نطالب بتأمين منظومات دفاع جوي متطورة وحماية سيادة البلاد وأجوائها بشكل فوري وفعال ومحاسبة كل من تسبب في ترك سماء الوطن مستباحة لرغبات القتلة.
خامساً: إننا في حركة النجباء لن نسمح بأن يدنس أرض العراق طغاة واشنطن وأعراب السعودية من دون ثمن باهظ يدفعونه من مصالحهم وأمنهم.
الخلود للشهداء الأبرار.. والشفاء للجرحى..
المقاومة الإسلامية حركة النجباء
14 صفر 1448 هـ
29 تموز 2026 م</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/86160" target="_blank">📅 14:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86159">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رئاسة الجمهورية في العراق:  ندين القصف الذي استهدف مقرات قوات الحشد الشعبي في عدد من المناطق، والذي أسفر عن استشهاد وإصابة عدد من المنتسبين، وتعدّه اعتداءً مرفوضاً وانتهاكاً صارخاً لسيادة العراق واستهدافاً لمؤسساته الأمنية الرسمية بما يتعارض مع قواعد القانون…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/86159" target="_blank">📅 14:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86158">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رئاسة الجمهورية في العراق:
ندين القصف الذي استهدف مقرات قوات الحشد الشعبي في عدد من المناطق، والذي أسفر عن استشهاد وإصابة عدد من المنتسبين، وتعدّه اعتداءً مرفوضاً وانتهاكاً صارخاً لسيادة العراق واستهدافاً لمؤسساته الأمنية الرسمية بما يتعارض مع قواعد القانون الدولي وميثاق الأمم المتحدة.
وفي الوقت الذي نؤكد فيه رفض العراق القاطع الاعتداء على أراضيه، نجدد موقفنا الثابت الرافض لاستخدام الأراضي العراقية منطلقاً أو ساحةً للاعتداء على دول الجوار أو لتصفية الحسابات الإقليمية والدولية، انطلاقاً من الالتزام بمبادئ حسن الجوار واحترام سيادة الدول وعدم التدخل في شؤونها الداخلية.
وتدعو رئاسة الجمهورية جميع الأطراف إلى احترام سيادة العراق والامتناع عن أي أعمال من شأنها زعزعة أمنه واستقراره، وضرورة تغليب لغة الحوار لمعالجة الأزمات بما يحفظ أمن المنطقة ويجنب شعوبها مزيداً من التصعيد والتوتر.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/86158" target="_blank">📅 14:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86157">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
🇮🇷
ايران تدين العدوان على العراق  أدانت وزارة الخارجية بجمهورية إيران الإسلامية، بأشد العبارات، الهجمات العدوانية التي شنتها الولايات المتحدة الأمريكية والمملكة العربية السعودية على بعض المناطق في العراق، بما في ذلك الهجمات على المنشآت والأماكن التابعة للمؤسسات…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/86157" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86156">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7lqGi4id_aC1y45Zg4magML4xNaRdaJQA1k1Y4vjcRR_6OZBgSZBSE_iCYO3sJ-dC6YtmAb3s949Qg1iOoBJFUGsdLElFXWfUfXvKPz5TIw61qNn4ZsTGi4SuHTHzMkbeefJYlqw6T5uWMZ0lBB-UKjowYay-kjQ0VGSFarCrgg5WvnxE8Pc_KoDfi9bB-4oT4NvNc3O_m5RUv3qKjg_8araupKgrXOPJ9KrzlicX1KyaiwhyinV5hUjF2bA2_3led8saOHIx8YhiydZmnctwSJl06TpJeJGGPwGzk8f2l0wzNWMm9f_SjTN_E-CH7UbeM-ftKE2c-YZakwTiBfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ايران تدين العدوان على العراق
أدانت وزارة الخارجية بجمهورية إيران الإسلامية، بأشد العبارات، الهجمات العدوانية التي شنتها الولايات المتحدة الأمريكية والمملكة العربية السعودية على بعض المناطق في العراق، بما في ذلك الهجمات على المنشآت والأماكن التابعة للمؤسسات الرسمية العراقية، وكذلك على مخيمات ومحطات استقبال زوار زيارة الأربعين الحسينية.
تُعد هذه الهجمات انتهاكًا صارخًا للسيادة الوطنية وسلامة الأراضي العراقية، وتُشكل خرقًا جسيمًا للبند الرابع من المادة الثانية من ميثاق الأمم المتحدة وقواعد القانون الدولي الأساسية، وهي جزء من طموحات الولايات المتحدة وإسرائيل لتوسيع نطاق الحرب والصراع في منطقة غرب آسيا.
وعلى الرغم من إعلان وزارة الخارجية عن تعزيتها في استشهاد مجموعة من أبناء الشعب العراقي الشرفاء في سياق هذه الهجمات العدوانية، تؤكد الجمهورية الإسلامية الإيرانية على دعمها وتضامنها الكاملين مع الحكومة والشعب العراقي، وتعتبر النظام الأمريكي المثير للحروب وحلفاءه في المنطقة مسؤولين عن العواقب الخطيرة لهذه الأعمال الإجرامية وغير الإنسانية والتحريضية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/86156" target="_blank">📅 14:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86155">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7Tr0MmzyV5EW0iXgkymypUr_UvuiCFIzjfec7g5gYpAN8yxLqelxXpUbtPEVO7DWPLh6Fhs5ga_eH-3KfTykpuTgQsbTkHXWUwL8k1J0WGuUz_YkqoJqBpoJ_0pKgaGm18U73Axn7BSMGm2dspjHzRJZYfr2ZvnwCN5pJCU1gTh8SLpAqvWHNRwJCmQmrZU5qIsdPejao6f0uU97-VzxtR2Y8W3kJuJEdgz3bxytEnIDlSA0cPO38U8oe7b0OxjuEfqKp71jg13QopsfWQ88QoN8AbbENsHtQ454b6UWzvg2HujAJv9KB8N3unuejjirO-_DyO31XPbn5g3P8x6hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوف تدفعون ثمن استهداف العراق غالياً</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/86155" target="_blank">📅 14:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
وكالة فارس عن مصدر:
مضيق هرمز مغلقًا بالكامل، ولا يحق لأي سفينة عبور
المضيق.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/86154" target="_blank">📅 14:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">طيرهن يا ابو الاء ..
الشعب كله معكم</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/86153" target="_blank">📅 14:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86151">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/86151" target="_blank">📅 14:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86150">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elOQAt0QakbxgOxUaB_GkWZCMcZMiA4jHPbXm13c_kW1rkXSJex3JY39RywpSFOZfyJhLeTYYoPKkgasSkoTn4lX9y9V7eeEjd9_t_bFrfuvj9rdpHGmfKIlkQ-r-IilW7SXJ3yXBETTMOCFrGQ3DVvXdQrgPomvdyTIDwrGyY6t1DTE3Rnq-KYw2z0BRDoAq62OXeD-W6Zhp2QBLHJH_Y4okDNumZLcLF82PSh8r68nWHOQckmsUCwv6kfnjtcpRhQnC2FYpzJKnpraiBue8Yv2EUEIvfJzUHxfZy2UJpWVkwLFYW79JtVNawKTI26mAzGYVIYZi6jHOchWLYIc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إِنَّا مِنَ الْمُجْرِمِينَ مُنتَقِمُونَ
وعدٌ إلهي لا يسقط بالتقادم، ولا تُطفئه الجرائم ولا يغيّبه الزمن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86150" target="_blank">📅 14:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86149">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
🇮🇶
وزارة الخارجية اليمنية: للجمهورية العراقية ومقاومته المجاهدة وشعبه المسلم الحق المشروع في الرد على هذه الجريمة وفق الأعراف والقوانين الدولية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86149" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86148">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
🇮🇶
وزارة الخارجية اليمنية:
للجمهورية العراقية ومقاومته المجاهدة وشعبه المسلم الحق المشروع في الرد على هذه الجريمة وفق الأعراف والقوانين الدولية.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86148" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86147">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A81wf95pBRS2VSSIXWbdlAVbOrK7RAnKSJwSCjp9HWn8CX1VHgcbUHjZgguZDvX4lLadiizIUwRrZnyvB0jNK4Hfug9E8gvS-r0VlhyyvOLIaGpB0wVVs5lYCyivlnWjfvG03wiu2JMVc4ZSytWeYRAuB3Bo7s_IcXJeCqqlNYKEzF76KBQUS8-MvTVDCfHWsVxkpF0lY32C09pU-fM8eRYhrUK1G1c8UHj_ieOYS_pMxTqUpYCyi-O9URRhZfoX_hf1ztFywupaPAlDQ5de4yP5D0kkDxVZ1RVeyw12yv0AMeIv1z26sPA0pVjWy5a2Y5wCzP9gzEzalI8JP07GTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بوت نايا   ...أمانه من احد متابعينكم شنو تريد المقاومه بيتي والله ابيعه الهم وانطي فلوسه ويقصفون ال سعود وأمريكا نفسي ودمي فدوة الهم عائلتي فدوة الهم شنو يريدون مكانات بديوانية وسماوة  حاضره اني واهلي وكل عائلتي فدوة للدماء الطاهره يشهد الله حاضرين حتى…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86147" target="_blank">📅 13:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86146">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
الحشد الشعبي العراقي يدعو جماهيره للمشاركة في التشييع الرسمي للشهداء اليوم من امام مبنى المديرية العامة للإعلام – شارع كريم الندى الساعة الرابعة عصراً.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86146" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86145">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هجوم مسير يستهدف موقع الحزب الديمقراطي الكردستاني الإيراني المعارض شمال شرق محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86145" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86144">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اعلام العدو:
تعرض آلية عسكرية من نوع "D9" تابعة للجيش الإسرائيلي للضرر الليلة نتيجة اصطدام طائرة مسيرة متفجرة تابعة لحزب الله.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86144" target="_blank">📅 13:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86143">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM5wVZ60JCZfM7YX-n8EM_S3v5QycqXpid9lV7Q08JIg6MMrF5NSpldtUHN4rDgw57dRUoReFqaAAxI54Nb73w0Ja6KQ2G9_G2WHH9EyF5VVP3HvFJieKBUAsWHnMqP-eY0CmHqcgLGNSZLrhSyIC71Lt1aGxYlh463yimjgAyJP8EJ5Lqjci1r5JzR53kAFXxssrOQLG20a6Jyx6BVz_tdOEvfVrqER0zt9ffezGC-P_-3hFt3wdbkAm8tEh-ZDXX3rPvTDDvfSz9Y4JP3Arp6T4K8HPf5XViHuz348nY9Inm9KfNY4mHJI0Hs7iAkDkZXHhR_8JKRZIFaUaU1Bxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
خاص لنايا | تصاعد اعمدة الدخان من الاردن</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86143" target="_blank">📅 13:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86142">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7587bf80.mp4?token=IcqS-yifPjno6gn87nSqqN1GiTre3kR4O5DaFiF27BwCztRF47UajGplaPmEOJiCJjEAXnshoyJnqZGigm62jxUus7iHjsC10UOehYKHVQT4QwvHbr55MrfYERM6_2iDLLY2CP4C5yY_2C4D85WULyKY8N7uqVaO9ZcOPPzxKwiSma36s1phbvNVBTqeR4i5p6_5rari_pKItCJ3UZuHa5pT0nhLtQJnKj_8SSI63sjWzWAbFiSjevn6NpJgsUPCV0D9h88Ir8SwF9Yq-UdhW01J4MXumwbUsIp-VFASwjz5ek5RwCptYRCVneC9NQgZxCQypvN2Wp-DazT92vEtKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7587bf80.mp4?token=IcqS-yifPjno6gn87nSqqN1GiTre3kR4O5DaFiF27BwCztRF47UajGplaPmEOJiCJjEAXnshoyJnqZGigm62jxUus7iHjsC10UOehYKHVQT4QwvHbr55MrfYERM6_2iDLLY2CP4C5yY_2C4D85WULyKY8N7uqVaO9ZcOPPzxKwiSma36s1phbvNVBTqeR4i5p6_5rari_pKItCJ3UZuHa5pT0nhLtQJnKj_8SSI63sjWzWAbFiSjevn6NpJgsUPCV0D9h88Ir8SwF9Yq-UdhW01J4MXumwbUsIp-VFASwjz5ek5RwCptYRCVneC9NQgZxCQypvN2Wp-DazT92vEtKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من الاردن ويمكن مشاهدتها من محافظة درعا السورية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86142" target="_blank">📅 13:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86141">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86141" target="_blank">📅 13:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86140">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86140" target="_blank">📅 13:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86139">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزير الاتصالات العراقي مصطفى سند: منطق السياسة وأبجديات بناء الدول، هي ردع المُعتدين بما يتناسب مع الأعتداء، لا يُرد الشر إلا بالشر. رحم الله شهداءنا واللعنة على القَتلة والمُتخاذلين.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86139" target="_blank">📅 13:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86131">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEAEGKuHNoKs-epEeXmOPL9GKznuqGlDzbMAp75AzDDDq_eVG3YR9mtov4DpEX88_080S4f8-OYvfADxLhSssAPBQ-l_uaaUDkXPI452Ls9uclwoRfLiEn3CW8lxP7APKz5Pk1RONtxabICjwfvWdmsRaZuzrL0ziUyf4nKtgSV6phInJM1MyZ9d7DRRz9NjI0-4fGVnOANpxY3BaISVQK5VamuxfIs7lA4n8hVrwrANiGhTuOSzIKBtGBR1Jd96wk-1c29CTQUysqn5zB5qgsnn9qEuC27aUZ7EBlIMFyksrWGyBysrQTVOdLT_ogTrumGnPcXN3EBLn4p27TZkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlY-Y1VNVSjuP9z-RcWKYUWahYUphEaT50GkTSTHjy5qLO7bYG74AFWJgPGOocgN0qFMkMzKNu7TymZfPg4rMzvIPG1XZf1fFnsKRWULLnYUZtOG0bYDczNjrlVCyj8ObssKsYBQjFagYFBHuAcz-TM053ekBzdhBEmFrEriE_u6PglgHowLiyVXs5oabCeEf5V-ICTwmELUOHjw5Hw2UKT7Xfs6U7CJsryjFE0rV9nHX-gF6bzM_fBLeQgvJiy4rvZyAOzXednZhOYDAnn5VTFDCkrrNfUaI6r6leg_ECArqYwHpDg5nlO2Bl4bBgMT371earxtwKRCj5qS4DisyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmQ7K3Qk2Ej5a7zq-Qx3TZl2cdOVS6WE5GmSOIXfDHkGnP99fxS6nXOxKJOmFbFxdsEukXsmwzkwC0-qbJ6uaP5ZAhVudGH1cUzX26X_jOg8vLuA3AqYMVmUnTnhT3pyQxHSgpAJD_3-HPUjBsfrbaWP8f3wPuQSe_EYJw2pys2dUjbEdu4hGY1AGY2p1-sIF8UmLn-Wz-Yo8hlSH62ycoomiaWMoQtXWS2posxLQ5kXm5n-x5DCGV3jwKprd4-Mt_0xhKZQTAZMHnYlNV8QMxns_xHa30n8uNNzqwUmevMYBACxGKtn6DO9X6UeaTwOjZrj_H7oFkr0sfFzy6r2JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2HtY97-_gGlrwI9BmX6ez2uB-v1zDYyux5Kz2p_AI_9gX9tEB93S7YzS64hROuyswQ_uo4wHPDBFKs2NORace0t_mSF5vRKbh1otxoP4v7qZqCcVdp14IgHvmFPwrJRK0QU732NsI6gA9gp-8c_ghvg_gZlKHedgEHzb_KBr4Gi3neCSPSa7th2skmQQiPDxNKU34ufQfW9hS-viF7-OLv9tggmn2tiiGDSxY3q-WGnT_QBx9Av1FucVB4zA44bXiwdCfWTIBrjaL4Lm5Drny_ZIrHwpl2o2Y8hi_hLtZr6UmXsLgm8Z24V9tBTaFVw5zuprtKrbmxhycGTrvSuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TofkL1vg_dFYDN4BDatgAPHISFhwIG6tn8LaFNGN_96orUeFJfMozNU1kY46UhaB6PNZp3n3WFbXgs2sgW-LAeOL8n8MdL80u4PaNHTCs_iV1cGv-H2nqL_Fixp3FI8tnvA_3obavzA0tBmNkMWOKJtscV-dTW8-qb18nxuQWGK_gnKqzGXGnsDZqBQqgyl0RtdmPvH88kQyzkQJPCQtarpCTlfM0CS-wdKPNyyjwJVXBW4slFZho1MTwxM3psKzk72LiRuV8DPWAeBNy9PCPPVC2rSAU941Tfi-8YesDKkWnN0uOcNyiG8SGEnnHcXu5OkKNz649mev2_83G61CNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XY_1NlaIEvi942UwNKor54nmUEsc0M1WXW-K7Jz66I0M4xmXCetN8qWzPQB6dq04DCRJc0BnPAWEvgXR8BITK2VYjAzboWyNLaXzTgz7ThEFL2KFB5Bua_f8YlMkDzmi6qDLTNbzICif5xhlscCIHVrQZX4gIaqBKbMXIcoCDymyGp3c-vycK8YwZLuctdvpR-MSmuft_ntXNC8OnlLC7MkIsGZ2TIs7Euh9HUm-DFNjEYd22dTjWQtoBUyQx7BJ-nxe4MmFuWvTNChOmvf_GPqkGM-P_255QBgpOAtIS27Bfiht_txKKB6CfnMJt-H-WnMo1Ry9bKfEY_LqawQE5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZHTxDl0aH9U7n8v3IpJ4Cd1rgk5_w8K1mcbsUtE2Xr7in-R2uQSxKQdQ4UP4HLAARrSOx0f_lUhPEE1d-p_S9D6LewXhAL9VSaElDvMeqxgFPqyTQhFagJGyIaiLj1PSfyUfe4ekcMsar9JLvItAYMSiRoG77aMaoZp13cIjlCYWq6HeuECQKxuCcbUJGBtppQOlnSZRPPp5YclhB-OQBCA-QaByuvoC2ZslHFw9aT2Hz5fU91fYz4GLQaxmUwV-w4Ogl0DCauQ30lZYLdpAPhOECPoPvrgBBO1yUkB-OY7jNa4jynATzk0Qjp_luhN4pg288fgf_DrmvsLnM8SiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxpD3EbopQ0r7dw3CqLkW8m3QwuJXeWaJIn4gM_vcZHS1gz2ej4b2U_cekAJSa1VSvqQn-ztFss82zRm5_67swhZMT9QU7waAja0KUcLehjL1ktXvlPjFVb1-OsuCVrvRa2aZwk51GrtK0AGM5RHjP8fdzqLsDxpZ5bSlbPfPINWsPyh22Fg_9wUf9uaa5QsupElNsarob727ezSKEIcKP7Tkpjc24nWZ1JWEuPOXBaRRXzSbB60gmCfWK85nXxdFcAw7knSIwmJL6SbxLHbVeIl6oBLNfj4Kwtn-vIe6MeFBl-MxfBsXoAd5yO-75ToWP6Bw_9jDwmy17P5iqI1Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من الدمار الذي حدث جرّاء الهجوم الإرهابي الهمجي الذي شنّته السعودية والولايات المتحدة، واستهدف المقرات الرسمية التابعة لهيئة الحشد الشعبي، في سياق مسلسلٍ متواصل من انتهاك السيادة العراقية.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86131" target="_blank">📅 13:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86130">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajUivZyfR97WsqUAIkM2Aq1bpUwasTBaUSUKzU5g4I9SsUzcH3trMPwx6qnn43ItGKP_ezhV3jfHOENDxI6CNRLwYRkN2EtpkuyZU_7DLEhU1psFz8qKgXpggJu2f_K6Rwg0rIGQUuYQtRkTqZ3tbU0G_VAxS1XJ3SnwZpyEMYh8xVZQay4csCQEnUUZAAfDU4DRCXpuB3s5Jebfd4CIZNsHIviiJroML10y08FtFBLTmQHUgCOQwDfQOjNXs2ZSJDF3NsSt6dVd4ZNvL0faHxgytQmpfEgxrlGHNaxzSOakQHwodICnEyl6pyKmSTanKsZ0SKgKAzURtlYoT874Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇮🇶
الحشد الشعبي العراقي:
امتدّ العدوان الإرهابي ليطال حتى بيوتَ الله، في انتهاكٍ صارخ لكل القيم والمواثيق.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86130" target="_blank">📅 12:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86129">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05368b5b56.mp4?token=WGNRySribZwLliFdxGSLT1uK-8XB_rNRQCk6UcNvwSCkTeG8Cn9iuk85iIeJ01vbmSDVsHsPzMJO1MO9icIfdlLN1X9VdMJqwFGlszixdjOYLpBbgZ5407o0J29i3YmobodzQY4fOb7PbJEKi_FClyiwPVDFaR94nsV8N_QUuN8JLpIWvzsbeJZHEiksKJj2VwqzDrUAsuLVjpyeE5jlmloKeX11RoEP9NgJnwoLhgP0q2gWCfR8EehQwC94zfq2chCkVoDLkEsdImHLTxeHHrPAvddNZy2t-hF4-5jA2jFgo34qoa9Q5czohRWgH3a-BxF2RS5eAnLPcaVQsxam3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05368b5b56.mp4?token=WGNRySribZwLliFdxGSLT1uK-8XB_rNRQCk6UcNvwSCkTeG8Cn9iuk85iIeJ01vbmSDVsHsPzMJO1MO9icIfdlLN1X9VdMJqwFGlszixdjOYLpBbgZ5407o0J29i3YmobodzQY4fOb7PbJEKi_FClyiwPVDFaR94nsV8N_QUuN8JLpIWvzsbeJZHEiksKJj2VwqzDrUAsuLVjpyeE5jlmloKeX11RoEP9NgJnwoLhgP0q2gWCfR8EehQwC94zfq2chCkVoDLkEsdImHLTxeHHrPAvddNZy2t-hF4-5jA2jFgo34qoa9Q5czohRWgH3a-BxF2RS5eAnLPcaVQsxam3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور من لحظة إطلاق الصواريخ الباليستية في عملية "سحر" التي نفذتها اليوم القوات الفضائية التابعة لحرس الثورة، وذلك في إطار عملية "النصر 2" التي تستهدف قاعدة جوية ومركز قيادة مركزي للجيش الأمريكي في الأردن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86129" target="_blank">📅 12:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86128">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇷🇺
🇮🇶
السفارة الروسية في العراق
:
تتقدم سفارة روسيا الاتحادية لدى جمهورية العراق بخالص التعازي وصادق المواساة إلى ابناء الشعب العراقي الصديق وبالأخص إلى هيئة الحشد الشعبي في استشهاد وإصابة الأبناء الأبطال نتيجة الضربات على مقراتها في عدد من المحافظات العراقية العزيزة.
إن حياة كل ابن الشعب العراقي هو كنز ونشارك ألم اسر الشهداء والمصابين وندعو الله سبحانه وتعالى ان يعطي لذويهم وأقربائهم الصبر والسلوان في هذا الفقدان المؤلم والموجع.
الله يرحم شهداء الشعب العراقي الصديق ويغفر لهم ويسكنهم فسيح جناته. ونتمنى الشفاء العاجل لجميع المصابين.
انا لله وانا اليه راجعون</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86128" target="_blank">📅 12:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86127">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8kxpFdPP1D6emJe889RDEVBYFJ7rua_7WQEwdroQHpEf2iXNuXSAmG525NjTI5OCUw2yWJBOiYJ8riSqBaNo_0PIOe_Cbvkmqp549EHUQ0cNavObqGwltHfUkEfpTGU-b4cLlDuw6raGHdVKFwt-Uf5JLZSEYgctPe40siX9voDhRUtM-hDlHJh9-SKmlYJKtFEgBc5IHp17PAVQyUpJi_5RVPJRc9asmgsL2oNVPCtdd6wBmaFCaPFa8r2NtS6yCO3kfaNvAvcWISGO7U8Wz2SFL0tTwRIuDtHwZluDKZL_Svp2Nv0CaSO5lB3NSiU9_8oYxiAPfRDphdEcaJyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحاج العامري ديالى تعرضت للقصف   هل سوف تصمت بدر التي حررت تلك المدينة بدمائها عن عدوان ال سعود ؟!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86127" target="_blank">📅 12:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86126">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeYjnmEqLkn1XdrU_6t-xKZLSl3-7Htk2TWrCWn-X-XL9Mdbfb-NV7aswat0lYu_90T9alxDVbMj2jGM9jtt9vGZL_y0DFtBDbFmJ7HoaQ4cuYBadILE8dUdLmYOuDPFHlqg-PV1OqIFgSlYuudGT4ham3QGwmKmSNcTRJw2Md-A2d3xf9d1el-2y50C8-Ya2vCx19dlJqtBssofUYY_94ZLtMKPVA-66AEdeoTpmzq34xNqCovYdZ-01p-9OCEiXf0Bgai9CZ9hr-Rfv-y-42EKFWLYm48lsbrlAp7Ez0ah9SnYaQ19MEExUXr1HhL0WjoJ2JRR6Z-GwWFVkGRStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد مقتدى الصدر: استنكر استهداف الأراضي العراقية وأدعو الحكومة العراقية لضبط الأمن وفرض السيادة والعمل الجاد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86126" target="_blank">📅 12:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86125">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
خلل تقني يتعرض له تطبيق التليجرام عند أغلب المستخدمين في العراق.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/86125" target="_blank">📅 11:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86124">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b0c5bab1.mp4?token=NQOEOCmVEq3tk6zRRrpQjyJdot5qAseZwbuP-q4NXK6-7FIXE6Y9l40MOxYFCzXoW7f0f17Hn8wyUD_PMJV0O3FyoPwrh3v6DF_2PJSs2PhFr99kv18TOTx7_xQn8Oym08H5yqrDSznR79ggviNR2HyzEqJlLPTK9ZWOHyqHHT2tSIweyhYhSwhcFVYwuWs7Z9YQNFSRxyNH46rGds8prveNqmPOc2_fAjCmvkFIRJxtC_1NYNMaHYP4BdOg8JVz1FwIthrBUuBueCrwej-AgenDlMvMD90mTFkZWQ4sbAauswWxhZ0BewPO6ewGXF2TMkJT8b8T6YJp-SRTuFrfJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b0c5bab1.mp4?token=NQOEOCmVEq3tk6zRRrpQjyJdot5qAseZwbuP-q4NXK6-7FIXE6Y9l40MOxYFCzXoW7f0f17Hn8wyUD_PMJV0O3FyoPwrh3v6DF_2PJSs2PhFr99kv18TOTx7_xQn8Oym08H5yqrDSznR79ggviNR2HyzEqJlLPTK9ZWOHyqHHT2tSIweyhYhSwhcFVYwuWs7Z9YQNFSRxyNH46rGds8prveNqmPOc2_fAjCmvkFIRJxtC_1NYNMaHYP4BdOg8JVz1FwIthrBUuBueCrwej-AgenDlMvMD90mTFkZWQ4sbAauswWxhZ0BewPO6ewGXF2TMkJT8b8T6YJp-SRTuFrfJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد جديدة من العدوان الغاشم على موقع الحشد الشعبي في نينوى</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86124" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86123">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اتش به اختيار   حرية إطلاق النار</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/86123" target="_blank">📅 10:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86122">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087ed24835.mp4?token=qoup7P1TuZ9Ns0_zr0kopQ3pWJWkqkqu5pA6vL79j9Y0XY0ptdaun2X5XwcHSmCqbxT7RibsutTz7_naIdEuzaBosu2bZW3RnFYX5U-Ucztt5AZdzIdTdAZzrnSg1ICynvjW0xZPZZCxX3Yr1qkIH-hXC8nyNZQ5yM977XJDkVeYGiGZb06AVIKFxxtfFH3C581T51qOfz0liymihGn8i2B06PuQ5lHOWWzAgNRFeqJjy8AaVl4FEqLlLFnzAqb3ac-AQ-55z7K3aa65Vf5YDMyPpERfp7QnRJukD4FbLUZq3tQpFWT475Rm0Rhkyhb151oo_Fy-AG4f3XHtZ76ZTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087ed24835.mp4?token=qoup7P1TuZ9Ns0_zr0kopQ3pWJWkqkqu5pA6vL79j9Y0XY0ptdaun2X5XwcHSmCqbxT7RibsutTz7_naIdEuzaBosu2bZW3RnFYX5U-Ucztt5AZdzIdTdAZzrnSg1ICynvjW0xZPZZCxX3Yr1qkIH-hXC8nyNZQ5yM977XJDkVeYGiGZb06AVIKFxxtfFH3C581T51qOfz0liymihGn8i2B06PuQ5lHOWWzAgNRFeqJjy8AaVl4FEqLlLFnzAqb3ac-AQ-55z7K3aa65Vf5YDMyPpERfp7QnRJukD4FbLUZq3tQpFWT475Rm0Rhkyhb151oo_Fy-AG4f3XHtZ76ZTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتنياهو حول المحكمة الجنائية الدولية: المحكمة الجنائية الدولية لا تتهم الإيرانيين. ولا تتهم حزب الله. وزعموا أنهم اتهموا حماس، لكن الشخص المعني كان قد توفي بالفعل.
هذا كله زائف. إنه تزوير كبير.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86122" target="_blank">📅 10:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86121">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اتش به اختيار
حرية إطلاق النار</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86121" target="_blank">📅 10:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86120">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nr6rqcvpNuNsiEykwdXMH3Z10CZOffTUJ7cxPTEb3C9NGNvNzumG71Fqu5s4F6zdjDETa-vKqGc9tKcnyVn2EmnPpee5f7FcJuRNTgFPDnUMqMpHxz9Bu00-EGpLbpljpy1aornxIlWAfgrdzqaqHE2GwA5oLAveZFxv9I3-DBbaJkGKyLBIF91rSWcODtD1-TU2fz3EHud1ZMh98uiFwrsP_3qNEXC2ixNLGdxM0oIOs1Ya3jL6T7zDsmrQBbbJPNrgr7e4WPQ2D6HkZdE1A6bEPlKzbmFvZw30Z1mrjMpJ_wuOVKcjF429RYp88M4WEV-i7QxhdYxSeZdhHVzDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استلم الراتب البارحة
كان يواعد والدته بشراء المخضر والفواكه لان الرواتب تأخرت لم يلحق بمعاملة الشراء ..</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86120" target="_blank">📅 10:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86119">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي: استُشهد ما لا يقل عن (20) مجاهداً، وأُصيب (32) آخرون، في حصيلة غير نهائية للهجمات الإرهابية التي شنّها العدوان الأمريكي–السعودي المشترك، والتي استهدفت عدداً من مقرات هيئة الحشد الشعبي الرسمية في عدد من المحافظات العراقية.
ووفقاً للمعلومات التي جُمعت، فقد طالت الاعتداءات مقرات الهيئة في محافظات بغداد، وواسط، ونينوى، والبصرة، وكركوك، وكربلاء، وديالى، ما أسفر أيضاً عن أضرار مادية متفاوتة لحقت بعدد من المقرات والآليات والمعدات العسكرية.
وتؤكد هيئة الحشد الشعبي أن اللجان المختصة تواصل أعمالها الميدانية لحصر الأضرار وتدقيق المعلومات، وعليه فإن أعداد الشهداء والجرحى المعلنة تُعد حصيلة أولية قابلة للارتفاع أو التحديث مع استمرار عمليات البحث والتدقيق واستكمال التقارير الميدانية</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86119" target="_blank">📅 10:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86118">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">السفارة الأمريكية في بغداد للمرة المليون
تحذر الأمريكان من السفر للعراق</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/86118" target="_blank">📅 10:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86117">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/katSBE0S1zLUxdIPAirtjfPL50aHwh8IiO_dF9HrWXgQB6HipXf0IFrjj1cgBLc79CoTs0FZqRkT-pEuUfIW3b5HJfDhh4zUXS46RGBdOLu1kTIbtOr9Uixim6WEXkRVDAyh5rveg62ZirnjHCwzxEvrjcU-kOv4auPth5QK23lFLWHA2pnmWzkWRVp-LyUIqLhBOKPxydx7YANtDpvCQy0Ncg33zRetT4FEuGHvREDesnzuQk3v7uhCxYQPtnFfr9r2x71DmNOOhovDpaW5ikVEOpah7wyTAILtTW3aJNAUXigi_iB3k025c_C-uENSkGuZTtDe0BkvY-1k2scdvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشعب يخول المقاومة العراقية بالرد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/86117" target="_blank">📅 10:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86116">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نقسم برب العرش خلاق السماء بانعدم الجيش السعودي نعدمه  عيسى الليث…</div>
  <div class="tg-doc-extra">Ahmet Demrak</div>
</div>
<a href="https://t.me/naya_foriraq/86116" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86116" target="_blank">📅 10:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86112">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JW_vcb7ap6IxVvmXqBdpZFPzE52G8QfuMxVXbIBLvefoSDgk_YFYaAU9VwkZJFeGYkY4nXYpT2Wz_ooHoi7VQDq6hboewxbVl-fPFJfitSiptZB4_NPEHnI39EOy2e-YwHOvku81IsBmKVNjCQ324skTY30Q7rU3wsnRWAKI7z9uy75BwQS_E9Why2winK_2D9eieML0t9FVIHF-SjMm0Yww39ZoR7Xo-a9gniZxKN6Kk9nPeHhNPzIixZOm9Su-xVV8iF-7YOvbkgSoagSxCtwBPL2Yl00fiSMuWLvb0gvvvLuwWDDsFD-keblYMfQfqS8OfMxspV__uK4bbVqDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gp1O87cjKg77eydD-j6HXNkqwGHr8L_G5IOBtHnITYJ_waKrDakDnov5uw0E-rQDj6xHtKAJ5YcrG4couWjP3ee2BKP0xx-UoJyK_HFgymb-P1oapSw3dT9ZwRQ1ilYopM439UZeY3QQqClIa7x6PKNVQVrxY9Vrr27BWZ3MxE0ThsApab2dp5Z1Q7dCEfielnHm1nkRn-tkUCsDo1pAu_PexnLp9JHWrVesFtBILjxCXhXri1XIIOTVcJuhjsU7qI4qpVUZMR4viZtSY5iWcf1bsVaMtjrM4efwc2LK8WTuZJ4z2RqBeEajDX1b2elTA8yQrZvGq3gSx4VTvzkT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0iy8n1ELUA5o74hWgSgcwxqMhTd1NKqCMICOYVlXgz_EqsgsXZnzQqYcujV087dZFhf0HgMQy3MzKQwRPYOffe40gt6bKVX1EEw1Wstn7-61C1DrsVAjhy2ZWlspuXgrKvqn1AppHFq2_0PJl9dKhLTraRu94KaM6-7SxT3cCXmLhVtMKan3t7bdDuURLuRw1gBt0HeTZaVxsG2E25q_2K7LBYgBLvEyGeO1ZoP2BPwMpO7ZrmF_R26ZkSYIBEC99eG9XSv9Gm_6Ewb-DZ56UDKYbSBX-SK0msiCrTtmZ2rFeqUiToQR-WdLRfrspKH81UQatkfM_l_5ZqsSfRtpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/raiO4Hu_C8Axw11yRprDUF1x16eQ-dd2gqbXDubHSgshQMmRd3Lu5rrjfFunUadPMVAIQyy2Loq4DMelqzgC7JeWabO9eiyKEcpeG83ItY9ivf2WoFrnNa8iZ1yKjZnCLquasG3orGooaewi9BOE3jyRERnL0PCYiWqdl52HsmGFBc4wicu-V2CtchTUbI7dY0OgU07cD1VYSXnqUscMM6Uq99G6CSlzD8iRa4Vjcyis2PPvSX2cPDrGE8sDVyEPJ02RmzDNkQw76IJ4DxQ1CgBQNZ7Kl8QW59ozM6B6sz3OY6Y0cuCyQ-zOEZHN7V6tItNPyCm6S7eFoeY_EJXIng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من آثار اجرام ال سعود
جرحانا فخرنا وقدوتنا</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86112" target="_blank">📅 10:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86111">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من بوت نايا
السلام عليكم
نحن ابناء الشبك نشعر بمرارة والم بفقدنا لشهدائنا الابرار نتيجة الاعتداء الجبان من قبل آل سعود المجرمين على رجالنا في الحشد الشعبي الابطال
يجب أن يؤخذ الثأر مربع من آل سعود.
"الدم بالدم"</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86111" target="_blank">📅 10:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86110">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/86110" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86110" target="_blank">📅 09:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86109">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">من بوت نايا
...أمانه من احد متابعينكم شنو تريد المقاومه بيتي والله ابيعه الهم وانطي فلوسه ويقصفون ال سعود وأمريكا نفسي ودمي فدوة الهم عائلتي فدوة الهم شنو يريدون مكانات بديوانية وسماوة  حاضره اني واهلي وكل عائلتي فدوة للدماء الطاهره يشهد الله حاضرين حتى للموت وياهم</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86109" target="_blank">📅 09:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86108">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">من موقع العدوان الغاشم على الحشد الشعبي المقاوم الفوج الرابع اللواء 30</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86108" target="_blank">📅 09:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86107">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الحاج العامري ديالى تعرضت للقصف
هل سوف تصمت بدر التي حررت تلك المدينة بدمائها عن عدوان ال سعود ؟!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86107" target="_blank">📅 09:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86106">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سيد طالب الثار الثار لديالى</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86106" target="_blank">📅 09:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86103">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qADxw2Ub_xv7ftp9z3BQTbjbEKCbW3xaMAAT70uP8t-ytQsxc06tnoIF3aP2OX0OIeoGtiArryS6TeEwQUL_v5QxRlYChSPouXcgIV4btz2Sm3TsXyt3GeXhTZmn20XWZDeZBN9Pp4LsYcENf7yM9xhb5yTdsyzSOVQHUcruCvpt5Uamdq2zOMy_lmjtVUzMEJ5P7797YpurXw5O7pG5QCuIC4dKXN31vq_NrOKAM6TR6YX_304RSZKc8SiD_OAIPXTy5sYsWhBPMqYMBoJszoCRuN9uj5cfnWaCdUhPAljtq1juDhhdT5-Bssr_6zo2MUmexnqUO3sbEAcGXLff-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asoSNP9rNXE0Pb30bnirk_s9ktZ1LHNbYnOlb_vc51X9DJgKHgrd5tceonhm7EVqoJ0lwDVWl8Kq138rFYnP4j4aUe-ckMVllg-4aEOYD_HPJtD2-znCoURY8urPrtGvSUo7Vjb5yr8sq3eucT2JcLdMrRiEJt9vrhDzDl2HuehOpzs8M-ej7lpaRiHxZAQLYdLsvQicisfAvNdn-FGXVuukvwxQbqjqZF0XTqKFW1eP195lAYMhbvx9f1DjUE29E9Fn0CQUi_kSYM7jJ3ZNbiSsZsVwOijiF1b2ZuFYBqT0OJwyrcmu0ISCv1Wj65Bas8vwHD7AxOicHXVyxsi9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCnF74iHJ5XFxC6BNFsDaaDWPhaSCobhriYEQTFtp-4vXkhFARF0pg70-xruU6sNsbPgbwgu05gFF3Nep4t5Kp1NvWUGTS97JodhWA4AEOanWArQHrQxyR3TZOpgXidGZLl4-pBLrl-itCBJRrdTzzIumURhmqp2B3VDvXZhfYIL4ovKzxIHnVytNyCw0x_UZj5VSJtEBzP2c1gE-qbXwfBdR1tZ_MsJxNHlBoguCwKnAzyW14emv1kbrBrxWg43UAma142i4_RtPhF9HiuSKWufFCRznOhkDxb-YRL6t0EZUg7U6sAdLp8jjoBY25Z2iesX7OA8bbDbO6C8rbdm3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد أخرى من العدوان الأمريكي السعودي الغاشم الذي استهدف العراق فجر اليوم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86103" target="_blank">📅 09:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86102">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
خلية الإعلام الأمني: وجَّه رئيس مجلس الوزراء بعقد اجتماع طارئ للمجلس الوزاري للأمن الوطني اليوم الأربعاء، بناءً على تطورات الموقف الأمني والقصف الجوي الذي تعرضت له البلاد فجر اليوم.
وسيصدر عقب هذا الاجتماع بيان تفصيلي عن مجريات الأحداث والقرارات المتخذة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86102" target="_blank">📅 09:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86101">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مطاليب شعبية وجماهيرية ليكون تشيع شهداء الحشد الشعبي من مدينة الكاظمية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86101" target="_blank">📅 09:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86100">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جهاز الأمن الروسي FSB : مؤسس "تلغرام" بافل دوروف أدرج على قائمة المطلوبين دوليا</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/86100" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86098">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rT-FsQnptsEbeEe3gR_Fc9ZxIrKGIJr_c3gN9B2lYEPAXBWZVdMC5oXgsRGtwGHzTqnC3xexwWPos9HWuGOSlfInmD4nLVBswArKQdpvQZg0wOYdyYu0PZVBSrVyNp3Larl2Z4kPLl-G38UB5a91z8l1jT6SgmlcUKXKwR6LTfw4kKSuN3elUXRlTgmzQ5bF8a2lmxqkfIaZ1p5FF_XoFcb1BF7HTnXQN2zaCjiS5naKB7ZFFxb_UTQMwIHUWGqE0s4gYwrOMgpLskPhIRXEwQczQUxc5UZkTXEbJQqCTLtOVziYwFQlecNQ9UCR3WuK4xOxqRfiEH_aWatzfOvHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WN2ITTPICAww4ZQ4MIQatOR2vJpDK1xIm_NvjUjAICtldwFPUgGHuiQxgMR3gimrG8XW16YFnGGo5YAuNtziPl33snE2OkYX2RvvtIkAd3XCK80jNuivwOi-MsE3BesHsJn27AHocmuLthPJhRID9MFw9Nu6YjUPTV5AsffQAmb8EQhJzCmtdO0htXk6CBJWW_gboBO9Qw9L5pRe4ixiToO0S67YGQCTbG9aiwsogkz8Mtg1kckHT4jumrvkoN8XN-ufqTx1C5ceLQr0Rw5VZ37rkavayNWOSeZ_JsbxEClmGt5BsZKQbLkgnUPiRTamb-XXG5mhlB2E29Hden9MjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد جديدة من القصف الغاشم الأمريكي السعودي على مقر اللواء24 في قضاء المقدادية بمحافظة ديالى</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86098" target="_blank">📅 09:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86096">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDzLandSzbZ0Guvf055dvYx5NUJE0tH-WPgVSYvEO65V_9OStj0ewTRLGGupZCeMRqy958r1u-ZKylsE_liMc9Y8PXE085gGdwB76duvFtKelwzeY9K41oLIPkLKfMFmTEz7SOoESIQ0CNKwHn-BJ_Y26y_AqiM1Jp6gbBTDA87J_gTyD8iVZoV7wZiaLcLgMo0GCnUpMqTjilc0KcLI3f7mQ8mSR8XJYwW-T042M0EwiYUl8TTviBw21NfA5Fjc1z7xCf7ju6WKtI6-EypwWIXT9LldepZZmu5DRpbf8it4hFssm2pIp0xHWqjlgVP3S18FFkfcykbFD5k4XwgcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استشهاد شهيدين من اللواء 24 في الحشد الشعبي جراء العدوان السعودي الغاشم</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86096" target="_blank">📅 09:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86095">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/604b4c39ba.mp4?token=soLnU1UdUvF2KVR7DuqI7gxM5ahu241ExQf1SCZcjCAVEr2tuM5odn3Wg5h26YE78Fc1CILA16S-B15VrrIyCxgDGocY-ViOJSyvZPVefL2IvotjnxjJ-d9oH-AlqocqzKJ6QdxDo4mx8EGcvPHWpegNDDjS8hOkc581-dh02Rxron31ZP9FTtPKoTbVsmTJdaXVfDzcr7RoSq0ojISXxTqWl8GGkgVzZ3Vw_6Svwr7rkVuy1eH1R14ht78pjLa5-iHM_pImLjaLI1STJeXgxJXIEWqIhhcG4T_oEQs5cgkgiD2nct58ULlamzNhCo9ONIj2f3UPh9GdReX33eCu9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/604b4c39ba.mp4?token=soLnU1UdUvF2KVR7DuqI7gxM5ahu241ExQf1SCZcjCAVEr2tuM5odn3Wg5h26YE78Fc1CILA16S-B15VrrIyCxgDGocY-ViOJSyvZPVefL2IvotjnxjJ-d9oH-AlqocqzKJ6QdxDo4mx8EGcvPHWpegNDDjS8hOkc581-dh02Rxron31ZP9FTtPKoTbVsmTJdaXVfDzcr7RoSq0ojISXxTqWl8GGkgVzZ3Vw_6Svwr7rkVuy1eH1R14ht78pjLa5-iHM_pImLjaLI1STJeXgxJXIEWqIhhcG4T_oEQs5cgkgiD2nct58ULlamzNhCo9ONIj2f3UPh9GdReX33eCu9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أحد شهداء الحشد الشعبي جراء العدوان الذي طال العراق</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86095" target="_blank">📅 09:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86094">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">إلى كل من يستطيع التبرع بالدم، نناشدكم التوجه فورًا إلى مستشفى الزهراء في ديالى
قد تكون دقائق من وقتك سببًا في إنقاذ حياة إنسان… فلا تتردد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86094" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86093">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مصدر لنايا   ارتفاع عدد شهداء الحشد الشعبي في الموصل وديالى إلى ١٢ شهيد .</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86093" target="_blank">📅 08:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86092">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مصدر لنايا
ارتفاع عدد شهداء الحشد الشعبي في الموصل وديالى إلى ١٢ شهيد .</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86092" target="_blank">📅 08:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86091">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2cda5407f.mp4?token=GDoGt2mUq93TNFpOibsSF7YvnDhBagFAdMZSKGIDuh_DQ-bmo8UlJAthP6EJ78YAtxKFfnO52gQSK9bagAYGSzORSnc-gsZ0AQU2xOxg3iFP7ok_W2Z4fXB682IgJbKC_wBzT2zzgzNAPH-qsCmLIUDWvW_vGMx25i8ISJYGKa2_Ir7xaLP5jT6yXlpYU3LNn5e3Gk3i8FieBJYx2U7khjm37Dz59zDQ8dGeBiv4HwS1lOQ01QVE3_Ij2gJiLuEsse3lR1gjDF_p-AM_eZqowKJDFY89YlcltL7hYrYitIUsfEMB8AdDtjxYVp69Fu_lOYobCqv4w4baOGLkUwxthw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2cda5407f.mp4?token=GDoGt2mUq93TNFpOibsSF7YvnDhBagFAdMZSKGIDuh_DQ-bmo8UlJAthP6EJ78YAtxKFfnO52gQSK9bagAYGSzORSnc-gsZ0AQU2xOxg3iFP7ok_W2Z4fXB682IgJbKC_wBzT2zzgzNAPH-qsCmLIUDWvW_vGMx25i8ISJYGKa2_Ir7xaLP5jT6yXlpYU3LNn5e3Gk3i8FieBJYx2U7khjm37Dz59zDQ8dGeBiv4HwS1lOQ01QVE3_Ij2gJiLuEsse3lR1gjDF_p-AM_eZqowKJDFY89YlcltL7hYrYitIUsfEMB8AdDtjxYVp69Fu_lOYobCqv4w4baOGLkUwxthw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نقل جثامين الشهداء من مستشفى الحمدانية إلى الطب العدلي تمهيداً لنقلهم إلى مطار المثنى.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86091" target="_blank">📅 08:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86090">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317976fcdc.mp4?token=DewJDyForTsnEIhj8chhXkdh4Askd-B-bwdlbgX57PD535gA8u_811LoqN4iJMh87hAZvUBdxFWR_xJMi8dZFMJqffo95rRd5V1uas60Brf4YUoiEPpD64WHGLQ0Rgz65CrsIAHrRyBd7Ji7s2ydKCLZ8lcEBiDtBGlWu9hwcl39t3rRkTXnjJ4uzugbTAIROXoxXbNqckoT2qR-DidQ1T4-ZMrFxH-2YFS-kp4d1POKq1PR-pOc-BYOk2-voRycr7BuaH9df_eiTihzYjMs2xNWBbnM1LVeqSdofRCG8gXbE8h0BON3aYJUpUEbu3pR3SDEd2EUm5Wifq-V6DT5zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317976fcdc.mp4?token=DewJDyForTsnEIhj8chhXkdh4Askd-B-bwdlbgX57PD535gA8u_811LoqN4iJMh87hAZvUBdxFWR_xJMi8dZFMJqffo95rRd5V1uas60Brf4YUoiEPpD64WHGLQ0Rgz65CrsIAHrRyBd7Ji7s2ydKCLZ8lcEBiDtBGlWu9hwcl39t3rRkTXnjJ4uzugbTAIROXoxXbNqckoT2qR-DidQ1T4-ZMrFxH-2YFS-kp4d1POKq1PR-pOc-BYOk2-voRycr7BuaH9df_eiTihzYjMs2xNWBbnM1LVeqSdofRCG8gXbE8h0BON3aYJUpUEbu3pR3SDEd2EUm5Wifq-V6DT5zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عدنا الحميداوي ونعم منه
بالستي بأيام الحرب جنه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86090" target="_blank">📅 08:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86089">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مدير الميادين في بغداد يسأل كيف راح يكون رد الحكومة العراقية عسكريا لو دبلوماسيا
استاذ عبدالله بدران الرد ما ترون لا ما تسمعون وسيكون رد على يد ابناء المقاومة وسلاحها الشريف</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86089" target="_blank">📅 08:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86088">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دويلة الكويت تدين اعتداءات العراق على السعودية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/86088" target="_blank">📅 08:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86087">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شهيد من الحشد الشعبي في ديالى نتيجة ضربات محمد بن سلمان على العراق</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86087" target="_blank">📅 08:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86086">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pm1czz_CGvNcnkB45I2LbFyOeDktpII79gy_R7C8X8skWdpZh8JFDxezb4p7betvZEUUVTAR1olwrHrL64vkveR9fpCOWuEW0wFOodWVuj4vb5QVoMvWqMG04hnANIgfj7a1dg5ProKaX1EWhTaIN1Z0Gh1eSGhSbOF8AG4mLls6uX_qOm6ARpDJIYJwZx385-JULxuqqgI3Kc8yzUa6Wqrxp94o79fqduhzsYyMUsxYb7K5O6W6jejUi9rOvod9mbCzDDAZhQTO1BxTHLhjUYPgzRFDpsBSvelrSFjtvu5dcHwWR3_5MfCWg4KUapFlLplAcI4HbndZQYup3FwTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد بن سلمان يثأر لقتلاه السعودين في التنظيمات الارهابية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86086" target="_blank">📅 08:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0kIotBR0Ur_gbDeNDUMegOYlt-GJwVH8DYhTrMhLfLqo5FtKiRR9gVY5Cu7mdGBab1CTQoXg1YorJGrB7WXQ29T-Mlv1pOMlA3SOUm6Qm0YQYdsjVMiVRuCEkw4AQiEklBBjbczCwFpM6sHg_buGzQ8eKrTxp0UZZo7dUhByGLsez4ECK6gBJFVD4IdqON2C3VdnD5xKeSQj78ar9gTDV1SrTbs_xzs-1RohPQdtp4BclyOvtkuTVlug4xIj_pW-V1vANnx19h0-nDiaYRSAX4FdPRswZ1yx0zb_ZgCmFw1l0jt8dsJDdLmGNaudZ4igevoVNn4bAAGZGS_4sQZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fcQy9z6SXZ_jLX53fwo7WurAUk5we4edSDOderYkuYppJ28xhy5PBffiANgxZILaUUfsIA2XzMqO8P2JTIZYG5YIT7ymbwjpUvogGKSd9Me48-5pNFO5Mdu8b3XYN-EhPN6zCw_G21UQjO3ro90pWkLMzeMNuIJE4qfw83jaF6uEqCD2Hw1fYlIhJ6REcgxNDDFuKnQBFUiVQe5hNl97dLID1X_7kSVJIDI80BPWNSySfyDH6pDbfgwj1JuI8FPqCsixrg7ZtDVoR8VpKsEiZKjJkMQ1TUrqud-n_Pql9FPV4KDhX8tE2fXQIiC79ynZ_TpgFENUmPF3-ZLYNtRLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDaR6ep7z4xYa-dqx2yHxoozUoOIgzAmZBwhpfeujGve1Wp0aeUvAzglBk-R_WFlt3j0NfZnobNbXaPN-g9s30zC49LvSbupOo0L-ceJdu1cq8PSmEXRywcwhjlNJGTub0CHIcTgGm82tQgI3M_w2BCrf9nW56QNKMyZwpU8hBn5cegkG6TVDaX06s6k3nW4nCrvL-B0RMdwaQLarYWtb-B9EMlNG8oR1Im1-h4dXNXRK1YNEyk-ufhg7UK59fOAIA2sg6SR0P93Kz_Vb1hp_9yxwopTUFlEO3UxbqwaQaXS3nrF55xumrfa-Ly3lg52Z75nZPAItpfqjZ96h1rZWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قاطعوا المنتجات السعودية
#خلوها_تخيس</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86083" target="_blank">📅 08:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86082">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91420be471.mp4?token=SBzrzD2a8SC8vRK9otJ8XrLxJm4leXgq-HGnKnG5dM5u5_k4BmB750IsetR5ceTPcb0RXyXbj949X1Lzu14ihMQHnMVIRv7NUIQehAZj-k2GghzXzIhsh5VUOUOEmuelMBa4UDTNQcvu3bJ2FSS30p96ECcGibthzdv_6tiFlHgZAkZDGsSo-P0tECn9CEJNykex3eyMwUt8Go5_jq_2M398SsYz2wjqK5bdHpEzS56AR1sillQkKSGcBni3adiSN_24fFJs-NL5Hvubbfwwnv_BwvWjV8KM86BmJw4nvz_32eX73iiC91RP9tt_-d2mA0IivgtTPimc3wso8XYGbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91420be471.mp4?token=SBzrzD2a8SC8vRK9otJ8XrLxJm4leXgq-HGnKnG5dM5u5_k4BmB750IsetR5ceTPcb0RXyXbj949X1Lzu14ihMQHnMVIRv7NUIQehAZj-k2GghzXzIhsh5VUOUOEmuelMBa4UDTNQcvu3bJ2FSS30p96ECcGibthzdv_6tiFlHgZAkZDGsSo-P0tECn9CEJNykex3eyMwUt8Go5_jq_2M398SsYz2wjqK5bdHpEzS56AR1sillQkKSGcBni3adiSN_24fFJs-NL5Hvubbfwwnv_BwvWjV8KM86BmJw4nvz_32eX73iiC91RP9tt_-d2mA0IivgtTPimc3wso8XYGbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شيخ اكرم تمادى الخاين ابن سعود
بويه الحميداوي خله يدخن البارود</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86082" target="_blank">📅 08:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86081">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قاطعوا المنتجات السعودية في العراق</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86081" target="_blank">📅 08:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86080">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05de60a14d.mp4?token=biXf7oGIRUAwVdc7HaUgPIPnZoQ3mF8FIMRj2iLnT19mK82zxvfDDRtgaZD84b8iZFhME6MaZQrRF37RT0F1jB6SOhJBNsRPZHsjGTF11okgtnmie9o_5hEye2ADKjjx8eKkKWVtLKZjIKtLhiiq_sO5f792wHX9gMSaGTy4DiFxhK_wv84EYoeDQYMGeqPHuy7rOxrSidsdIWb1Hnl5wiFPfRdclbEvupHE0DHVMk2lSrbZuycENCkwsSAbbK-kBK7WcPYRUqUwknNC6rfFLFuiC2-_DbqBJtDxgLVNeKl-Q85sVbRfqoVKETnBYr4IbSkSoAoV7Mp0819IW27Jsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05de60a14d.mp4?token=biXf7oGIRUAwVdc7HaUgPIPnZoQ3mF8FIMRj2iLnT19mK82zxvfDDRtgaZD84b8iZFhME6MaZQrRF37RT0F1jB6SOhJBNsRPZHsjGTF11okgtnmie9o_5hEye2ADKjjx8eKkKWVtLKZjIKtLhiiq_sO5f792wHX9gMSaGTy4DiFxhK_wv84EYoeDQYMGeqPHuy7rOxrSidsdIWb1Hnl5wiFPfRdclbEvupHE0DHVMk2lSrbZuycENCkwsSAbbK-kBK7WcPYRUqUwknNC6rfFLFuiC2-_DbqBJtDxgLVNeKl-Q85sVbRfqoVKETnBYr4IbSkSoAoV7Mp0819IW27Jsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العروبة والعروبة وهل التفاهات
اطردوا ال سعود من العراق</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86080" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86079">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMiddle East Observer</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v13RhTaGvick4S43Qg4XLW9EaFRT4dRq1JxdfgKNVF86USrnwdaWroENsC4b2J4UETI5SBDU-zywl89hqGTedgr8N-umqldUDiGWBlzdIGxK_8vSJfX-S-o7vyxC4loWuBtscgMcHmxRVzz7CGVgAodpRKRhyFHeY9IJ83XzgA8r4QdT3ECC5mBOvi_VaRaPUEkuYePlJQauTrnYMxYBkB_TWFbP4yoaLtqHhhIs546aPTHKvuqejpWWPyfurxE5dFQ7tgpWxJmxRy4NxKOUfopaZLiuVvDopUqgmx7oSi0RGInu1dBs7ZH7qnjf53n0CNEZasjDghPlGZ2akodpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Mohammed bin Salman's crime:
A call for Husseini processions to print and distribute pictures on the pilgrims' path</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86079" target="_blank">📅 08:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86078">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/86078" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
عاشت المقاومة العراقية البطلة وسلاحها الموجه نحو الاحتلال</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/86078" target="_blank">📅 08:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86077">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">والله لن نسكت
قاتلنا الأمريكان بايدي فارغة اليوم أيدينا مملؤة
السلام على الأشتر والارقب والأرفد و جمال والفاتح ١١٠ و الشاهد ١٠١ و ذاكر و الحديد ١١٠ و باوه ..  سنقاتل ال سعود</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86077" target="_blank">📅 08:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86076">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887651b463.mp4?token=GOOqMPst_PejBJx3FoVg_jRzUWjgN-CaGmHHVcmVQ0xm6lHZfiWlULvplwMSTPkxL4cVySxXmNvMcGwgeldXprn4ZNxBtcNqHhBXSrHzvLTGEjm5gJZRfmSRu3dcCNBSkxc8YgiSHCaEMovIH384IA2cyD714XS7NMQntd1NGVIi8OYYw9d3CPb-L3AuoEak6KVAlCjTC8oMLalJMdURBEd_61InfDx4iqdB_Fk9o-hFQZYDMzRHv5F9TpIfIn-Be_UcW3TQwtJTugA8aDP0xSmlsOJe3zPRe2q44kiotsd8pxmXjJNPAvtGYMB-xUts404awm4Dww1NOYDtqB5p35zj1xcCDI3e2BV-Tm9WfnpOULjCfXzlHMz_CoO8chGjxiI1XQmAkoxAFPwi4ffDKOT3mBYnayuo36q2F06hCWZV8UrOZRz750oAXFZDCZmgQEBVjxFJgevUvZfO0VvVKSvje37pVIN2T8UuEegkiIMjyFemJAbYDldz4faEa1qGHSmPPm6PyGeXF3HLMN555RIRE-8ygjbvBgFOg681RXubjNo4WAuJaAIzvcsPVaCw1mq9D6viKy-MOuoN6F3CYlvZtbwpV0Q-VqGng3qhwJzuyVgk3yzhTZO7fk_JsG0YoL_RQ8NdxlbozYAckov1FselszbJp9nGgajwRkdWGts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887651b463.mp4?token=GOOqMPst_PejBJx3FoVg_jRzUWjgN-CaGmHHVcmVQ0xm6lHZfiWlULvplwMSTPkxL4cVySxXmNvMcGwgeldXprn4ZNxBtcNqHhBXSrHzvLTGEjm5gJZRfmSRu3dcCNBSkxc8YgiSHCaEMovIH384IA2cyD714XS7NMQntd1NGVIi8OYYw9d3CPb-L3AuoEak6KVAlCjTC8oMLalJMdURBEd_61InfDx4iqdB_Fk9o-hFQZYDMzRHv5F9TpIfIn-Be_UcW3TQwtJTugA8aDP0xSmlsOJe3zPRe2q44kiotsd8pxmXjJNPAvtGYMB-xUts404awm4Dww1NOYDtqB5p35zj1xcCDI3e2BV-Tm9WfnpOULjCfXzlHMz_CoO8chGjxiI1XQmAkoxAFPwi4ffDKOT3mBYnayuo36q2F06hCWZV8UrOZRz750oAXFZDCZmgQEBVjxFJgevUvZfO0VvVKSvje37pVIN2T8UuEegkiIMjyFemJAbYDldz4faEa1qGHSmPPm6PyGeXF3HLMN555RIRE-8ygjbvBgFOg681RXubjNo4WAuJaAIzvcsPVaCw1mq9D6viKy-MOuoN6F3CYlvZtbwpV0Q-VqGng3qhwJzuyVgk3yzhTZO7fk_JsG0YoL_RQ8NdxlbozYAckov1FselszbJp9nGgajwRkdWGts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد فاقد الموسوي: الوهابية يقصفون كربلاء والبصرة  والسياسيين لا يصنعون صاروخ لا يوفرون كهرباء للشعب</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86076" target="_blank">📅 08:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86075">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYN5TjJSISGn1OSIzcWRRXP-RDmNh9FuDLQKbKkkO42m_7pnmeG4-2qI2P5EIA-pGutny-AAO8xa1MRsAkDZ7ry35rXRM1VfA7uW_gqQqAqKuRJbtWw8vd9Fe-rlq8lYyz88wvAgVn9r8_PYudBDF6yeo6OQ-rrMqmp6wIP6GizKHbAVJTtjhG3hScRvGaCyuSjHTVUBbeIfYggOCcFWrCMEszRM73jKvPE2g1IO8Cp9Pxhfj2832WiymBP7u7A4rW_C7cCF_Om2NB0StQqtVtjX-M66YOH723lLGSW3ZdzVfuuc6drwGfCcDtX-7bHBZ6XrFzYw2OLPg-GCgmgtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جريمة محمد بن سلمان
دعوة للمواكب الحسينية بطبع الصور ونشرها على طريق الزوار</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86075" target="_blank">📅 08:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مصادر لنايا
المجلس الجهادي لحركة النجباء يدعو مقاتليه للالتحاق الفوري والعاجل لساحات القتال  ..</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86074" target="_blank">📅 08:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86073">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/86073" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86073" target="_blank">📅 08:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86072">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKCjr1inVgbM6IVzNztlbyH0kE-SrHZNFPrDR3eKMvA41g_w1G6lIDoUME1pHfqgozCABOmDJNS-n2AUWa90oUd3l8BCM3XZ86GUHJiXMmGLRBY0AWa9pk8kzzVF7ADomz86sIY-rNs69DcjKHmRtVPu2Gxo6A5u26ZvjY-fcdXKjkY3CC7Y_zLpELj_xNJ6QQt5Mx51soc1W9ZBciKF3vjcBLcGowqPveSDv4p_QCzVM-KAkZZP5XTYlmCfafB5ba477Ja21f5n2HVh0SbTij8KbgqmbW9xgEt26po4Rmr0fi09hMXZ5rJBZSudeydEvOWJR3xK_mn3WueNNTuzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلم ابو حسين مجانين   اكرم يقاتل بوجها ما لبس يوم القناع   عليهم يا ابو الاء الولائي   الغراوي الكلف   كتيبة كربلاء.   مجاميع السيد الصفوي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86072" target="_blank">📅 08:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86071">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86071" target="_blank">📅 08:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86070">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">زلم ابو حسين مجانين
اكرم يقاتل بوجها ما لبس يوم القناع
عليهم يا ابو الاء الولائي
الغراوي الكلف
كتيبة كربلاء.
مجاميع السيد الصفوي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86070" target="_blank">📅 08:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86069">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86069" target="_blank">📅 08:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86068">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stJO_BIW7FIUxmG3ZoaLFdWwCjJS0uDG2Lq-B_MUaH10y8oKFsrAYgu1zvYJC9wTA2hDhMCrtkYqUjaRi_J2uwgph_j7e2X6MPjP1NQI_HQOot893SZkSWa89ciLMWBhz_ro2dkIC5OqntFbP9KJajpyT9y_ntBae1j4Z6KkbBmvkAiWkpZjW9j8P7dTURiJRN5YbXG2nHVUMCmrmnhDYq5VX1LC2qhsKEeD6MinXdyCaXSQ2mMuTz4BCYt24CkOwo1rvQinPSXYFntfFOaZcbZJvtCoZTUelsjGldurjQ9r9_yIXXoFXmsCzxB41fmhlLpmIY-0s-u07mzV31kJSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا يظن محمد بن سلمان ان الأمر سيكون هينا
قسما بفاطمة وهذا قسما عظيم من اليمامة إلى العلا ستكون هدفنا القادم</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86068" target="_blank">📅 08:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86067">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هل سيذهب رئيس الوزراء العراقي للقاء محمد بن سلمان؟!
ام ان الدماء العراقية أغلى ؟!
الإطار التنسيقي ملزم امام الله وعلى من انتخبه بموقف جاد من علاقة العراق مع ال سعود …</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86067" target="_blank">📅 07:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86066">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f598d6c1.mp4?token=R9CL2Sxoayek4u2y5UC3Muwo-G2GApzZowQd_PLaMnlPSe1RXw7tdvT3mGUWyFeCMs8dYg76_g4RQPf6mFC8j1rzdODQnpgxuN3aGb_IsJwAuGWibffFB6X3xJL-Qw9aesAaeW7dkmYVfrVe_xbONKpsX63zHpwfiuDnWVBUoe_bNh1-o-Dzv83tZ0N1wrne17uFbCLGC9g0eBnkmolZSif5XZHbY2V0z8zjd224gCpWGo4bR_-5VUmfxCWuURiy-YI07i45k-t1SLz80eY3q3fLJAVqkX3okv2cTSj0xydIghOTkP9Lf3L8TAFzRCskWBdO3_jimCJpjsYFtPhEHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f598d6c1.mp4?token=R9CL2Sxoayek4u2y5UC3Muwo-G2GApzZowQd_PLaMnlPSe1RXw7tdvT3mGUWyFeCMs8dYg76_g4RQPf6mFC8j1rzdODQnpgxuN3aGb_IsJwAuGWibffFB6X3xJL-Qw9aesAaeW7dkmYVfrVe_xbONKpsX63zHpwfiuDnWVBUoe_bNh1-o-Dzv83tZ0N1wrne17uFbCLGC9g0eBnkmolZSif5XZHbY2V0z8zjd224gCpWGo4bR_-5VUmfxCWuURiy-YI07i45k-t1SLz80eY3q3fLJAVqkX3okv2cTSj0xydIghOTkP9Lf3L8TAFzRCskWBdO3_jimCJpjsYFtPhEHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق طيران مسير مجهول في سماء الناصرية</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86066" target="_blank">📅 07:56 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

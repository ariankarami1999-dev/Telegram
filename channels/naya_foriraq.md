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
<img src="https://cdn4.telesco.pe/file/tg_mPLQs5jvAKboZj2KAGsX0XKNrXdxJJ5rwtdF765P5ody7Jsk2JQ8sVqs-2Ny531ejAWbc0r3ehez5GZiCKoTeuvmvM2q2MZS8R66NocSWzUZp6KFVKi2z0QvjiVHGlDxSyQimYiXNMuiNWX445gHVHK4GazhVeQzBns8-7oV4a9D1aFXORT4k6TvjzfVIOVBHBlzO_k02R8MKAiamgigxkbSVl00LhR9V3fhQParndoOkk5MHdym4nykL1O_P1u6lpXFxD7TVFg5q-gwDODeWaynXZD1cxpTkHTUrQPGIf54tq-BLD1_f3b-rYw2AgP8AMjNj4Kr0zPotaNUxXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 02:26:41</div>
<hr>

<div class="tg-post" id="msg-86446">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AijjgwAi31NreALvL6gFxRRoGHnDihGB5mvvBZ5BE4M3OoBqhvfcvFVzkimFe1TUL0Lt2KEWQelLyQn8DLQXGTrHvC4g1EqG_yxNwTelqyoiQy70SPJl7872k74y7QUgmRkUeXf1yYlS3gjKl7tWIuvND8r3oqbNCzwn0RX6SXIEJu4j1bTpHzk0NFBJUpLhFwbiiQFST9wdCTyCFF2JB7042v3q8wEWOVLZrwqYXhnO-Fb-Dfp2jfZKaJzXt3Py9rXHwXfvwBHObvSTfd2-BpItZGoaM9aTYysxxUFIH3MTlMKLu9NGbeS0uwBBQJQMjAItA0sNVD89J-ic7NK_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
اليوم، توصل مجلس السلام إلى اتفاق تاريخي لنزع السلاح الكامل لحماس وجميع الجماعات المسلحة الأخرى في غزة. هذه خطوة هائلة نحو السلام والأمن الدائمين.
يعد هذا الاتفاق خطوة حاسمة نحو حكم غزة أخيرا من قبل حكومة فلسطينية جديدة ستعمل عن كثب مع مجلس السلام لمساعدة الشعب الفلسطيني. وفي الوقت نفسه، سيكون لدى إسرائيل الأمن الذي تستحقه، حيث لم تعد غزة تستخدم كقاعدة للهجمات الإرهابية.
هذا معلم رئيسي في تنفيذ خطة ترامب المكونة من 20 نقطة. سيتم تنفيذ الاتفاقية على مراحل منظمة بعناية. مع اكتمال نزع السلاح، ستنسحب القوات الإسرائيلية، وستعمل قوة الاستقرار الدولية مع قوة شرطة فلسطينية جديدة لتحمل المسؤولية عن سلامة غزة لسكانها وجيرانها.
قبل عام واحد كانت هناك حرب عنيفة مستعرة وأزمة إنسانية واحتجز الرهائن في الأسر الوحشي. لقد أحرزنا تقدما تاريخيا ولا يزال هناك الكثير من العمل الذي يتعين القيام به.
أود أن أشكر الوسطاء - مصر وقطر وتركيا - على جهودهم الهامة، وخاصة فريقي المتميز، الذي جعل عمله الدؤوب هذا الاختراق التاريخي ممكنا.
لن يسمح بإعادة بناء التهديد الذي ظهر من غزة في 7 أكتوبر!
بموجب هذا الاتفاق، ستكون غزة أخيرا في أيدي حكومة فلسطينية جديدة تخدم شعبها.
تهانينا للجميع على هذا التطور المذهل، الذي قال الجميع إنه لا يمكن تحقيقه أبدا!</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/86446" target="_blank">📅 01:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86445">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇸🇾
‏الجولاني يستنكر محاولة استهداف ميليشيات تابعة لإيران في العراق للمنشآت البترولية السعودية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/86445" target="_blank">📅 01:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86444">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6571e4ae.mp4?token=bolDGNn9SOu--yaRi-sOeSbNSjuGIGlyyi1z17SJoVsGltRZoeq6gI5K4mLRfYWfCWNWKlgYe42uBuo2MShlB7sYLa1PBAVsM_bxPahCB_UjxBQeGyxR7v2hBudEaEswq6ql74-BrAxXCXUJ-QWkEB6hvygRMN-gY1_Q4FweOuLtK5xnx0fnevhAROJuYAWuFWaisDrRK5sIrp__Q-v9gUOA3bObIBBEvoZdxm4aXhAMLcfJ7TrVh_xuxIjT0pOGtiJCHfPvHVCSbY_x8cq5ghI5aoSn8DXaFbqCKeM9YtEcvcjTaagslp7H0K0KXQyon0Zk8SdgDo4wOnhAQx2FHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6571e4ae.mp4?token=bolDGNn9SOu--yaRi-sOeSbNSjuGIGlyyi1z17SJoVsGltRZoeq6gI5K4mLRfYWfCWNWKlgYe42uBuo2MShlB7sYLa1PBAVsM_bxPahCB_UjxBQeGyxR7v2hBudEaEswq6ql74-BrAxXCXUJ-QWkEB6hvygRMN-gY1_Q4FweOuLtK5xnx0fnevhAROJuYAWuFWaisDrRK5sIrp__Q-v9gUOA3bObIBBEvoZdxm4aXhAMLcfJ7TrVh_xuxIjT0pOGtiJCHfPvHVCSbY_x8cq5ghI5aoSn8DXaFbqCKeM9YtEcvcjTaagslp7H0K0KXQyon0Zk8SdgDo4wOnhAQx2FHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏نتنياهو  وكاتس : تدمير أنفاق قلعة الشقيف جاءت رداً على خرق حزب الله لاتفاق وقف النار.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/86444" target="_blank">📅 01:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86443">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
طيران حربي معادي منخفض في اجواء سهل نينوى بمحافظة نينوى شمالي العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/86443" target="_blank">📅 00:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86442">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65aa1a707f.mp4?token=Kt4sShBJR-2Dx29TzZz_l_SmZmFvWQBTfNJjk_2IsGMx7Geak7s0n5SP-rawVP3ehAAPBKYcqOGjzZJbNsDbACDw1WctyfoR2xB8sxhDYJecZJpp-ja-i37uv_vIuTzuJhcbk_mFGQTzxEPO3AMgKN5kFnpIOEMR_SemxprdUu-l7jCsdaRMMO2QoPz6g_yXVLO8VzYYSXMRdkKUV_zyXdckU7mM0euPyxJkttD8utZX9m-ynR7uS7pmdSnL2Zp1aV4zKnI6FzoVZ65-ypw0NhTiQOPDutrA7URGBYDMu7GFsTs4_AVvzwrM35iyq3kWATgY-FSrQEKCb-S8ot1AmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65aa1a707f.mp4?token=Kt4sShBJR-2Dx29TzZz_l_SmZmFvWQBTfNJjk_2IsGMx7Geak7s0n5SP-rawVP3ehAAPBKYcqOGjzZJbNsDbACDw1WctyfoR2xB8sxhDYJecZJpp-ja-i37uv_vIuTzuJhcbk_mFGQTzxEPO3AMgKN5kFnpIOEMR_SemxprdUu-l7jCsdaRMMO2QoPz6g_yXVLO8VzYYSXMRdkKUV_zyXdckU7mM0euPyxJkttD8utZX9m-ynR7uS7pmdSnL2Zp1aV4zKnI6FzoVZ65-ypw0NhTiQOPDutrA7URGBYDMu7GFsTs4_AVvzwrM35iyq3kWATgY-FSrQEKCb-S8ot1AmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الذكرى السنوية لرحيل المجاهد القائد الكبير ابو حسن المالكي ورفاقه
هذا وين الگال ما عدهم رجال
بالنجف مدفون حماي الحمى</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/86442" target="_blank">📅 00:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86441">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇱
‏
نتنياهو  وكاتس :
تدمير أنفاق قلعة الشقيف جاءت رداً على خرق حزب الله لاتفاق وقف النار.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/86441" target="_blank">📅 00:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86440">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇪🇬
🇮🇱
‏جيش العدو الإسرائيلي ينفي الادعاءات باستهداف ميناء دمياط في مصر.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86440" target="_blank">📅 00:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86439">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الاعلام الاجنبي:
‏أصر الوسيط الباكستاني يوم الخميس على أن المفاوضات بين إيران والولايات المتحدة لا تزال جارية، حتى مع قيام واشنطن بتنفيذ "موجة كبيرة من الضربات" على خصمها رداً على هجمات جديدة استهدفت الأردن.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86439" target="_blank">📅 23:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86438">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-zFVqSvH_Fw4agpLfD98Gk3PvC0BZXVpIehiVX4rBQpKl8PXQR8S7bg1o-1VHUR75Yv98-Uhgj1EGwWhKVgVXSvQQZoS4i5GE21KXpJFMH7e5w745dsoApPMf5Ktj3G8YUEekoCslr2wM4AQNTRk2y_oek6jWCG4LmkfQvX2CcpIHMKBhATUMgtaPp3lPPyWXn8pr3vi3bNGwn-R729JWjPbZ6aOJhPOUsCtMevXCxk_O0ARYPnPks4EgDxhU4WcHRvQldcw-eznJewq4VQ4KE5v8Mn0TVn8YqFTgVZTe083LIE1seP1NygEsXc2BAY0JhQ26W7gUO4Ie62xAgjyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
مصر صديق وشريك مهم في المنطقة، وأمنها ذو أهمية قصوى بالنسبة لنا.
يجب علينا جميعًا توخي الحذر من المؤامرات الإسرائيلية والعمليات المضللة التي تهدف إلى تقويض السلام الإقليمي.
التهديد واضح ومتبادل، ويخشى التضامن الإسلامي.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86438" target="_blank">📅 23:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86437">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية: الحكومة لم تمنح أي موافقة لتنفيذ اعتداءات على مواقع معينة أو جماعات محددة داخل الأراضي العراقية، والحكومة ليس لديها أي علم مسبق بتنفيذ الاعتداءات على الأراضي العراقية،و تعليق زيارة رئيس الوزراء إلى السعودية بعد الاعتداءات الأخيرة…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86437" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86436">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a56c23c8e.mp4?token=D8A7oc_Lgumm5KTzOUuqjFeV_IcU_xra-wmCAZX4WykeBYWFLu5hPqxmY6z3McfVUb9Om7JFyv7js0SlfrSf5eUv3Tb7OkOfZpdIPFOHs6U82R6do7YjZIJZSiGS5KF75foVJo2OlYeJQ5E_8Ly5HMYZBjUXWI7LDjNBRtFeQ2NXelgidYDq7OCeQ087_2vxa7z99ZBZPmCiDjwOoMRH5enD0JEctZV-_wzgmw7Nmn0OQ6A8Q8vcVYDYbgnerf8nYhBiZhNJsEEOMGq65GyEocEyMYc-TZFOXBd5kL99EMhfbr9I74l6kPvaGSitpjFAa3jvYS75b7XnHKviIOix_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a56c23c8e.mp4?token=D8A7oc_Lgumm5KTzOUuqjFeV_IcU_xra-wmCAZX4WykeBYWFLu5hPqxmY6z3McfVUb9Om7JFyv7js0SlfrSf5eUv3Tb7OkOfZpdIPFOHs6U82R6do7YjZIJZSiGS5KF75foVJo2OlYeJQ5E_8Ly5HMYZBjUXWI7LDjNBRtFeQ2NXelgidYDq7OCeQ087_2vxa7z99ZBZPmCiDjwOoMRH5enD0JEctZV-_wzgmw7Nmn0OQ6A8Q8vcVYDYbgnerf8nYhBiZhNJsEEOMGq65GyEocEyMYc-TZFOXBd5kL99EMhfbr9I74l6kPvaGSitpjFAa3jvYS75b7XnHKviIOix_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات هبوط واقلاع من قاعدة موفق السلطي بالاردن منذ عصر اليوم والى الان.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86436" target="_blank">📅 23:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86435">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية:
الحكومة لم تمنح أي موافقة لتنفيذ اعتداءات على مواقع معينة أو جماعات محددة داخل الأراضي العراقية، والحكومة ليس لديها أي علم مسبق بتنفيذ الاعتداءات على الأراضي العراقية،و تعليق زيارة رئيس الوزراء إلى السعودية بعد الاعتداءات الأخيرة والحكومة العراقية خاطبت السعودية لتقديم الأدلة حول ادعاءات الهجمات.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86435" target="_blank">📅 22:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86434">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b961f0162.mp4?token=gKTYYQmtkdkqFGSWMHl79IRIkNG5Ms6wVKhh1kfmDPyhy5-65GcevJMmDAb-YAzAujGFRcj-pBRpExDCWGjxiytacb3tNaO4llRsmjp3_ohkDopwttPppSsmfhH5O3Nr_AZqiTqd3Vvs_CiQND8ibdkR2JDlxragwOrNOyoCo4u9eF1ngqUSfGwpPSlMr7nfbw2j5UsToW7U2Y_nXsyPhe-GA4rKKZOaBAU1so75z6yXgYr0XnuKTrgk4CmD6yyGv4CynnQl7f2Npo8enGaUAcGY9UsgQQFwFX_GpOEHLvNwNOECU8EooiXMyltY1cpTW6Amvy3EuYYfEKqhcYWl4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b961f0162.mp4?token=gKTYYQmtkdkqFGSWMHl79IRIkNG5Ms6wVKhh1kfmDPyhy5-65GcevJMmDAb-YAzAujGFRcj-pBRpExDCWGjxiytacb3tNaO4llRsmjp3_ohkDopwttPppSsmfhH5O3Nr_AZqiTqd3Vvs_CiQND8ibdkR2JDlxragwOrNOyoCo4u9eF1ngqUSfGwpPSlMr7nfbw2j5UsToW7U2Y_nXsyPhe-GA4rKKZOaBAU1so75z6yXgYr0XnuKTrgk4CmD6yyGv4CynnQl7f2Npo8enGaUAcGY9UsgQQFwFX_GpOEHLvNwNOECU8EooiXMyltY1cpTW6Amvy3EuYYfEKqhcYWl4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سماحة الشهيد سيد حسن نصرالله (رضوان الله عليه) قالها سابقا
"كيف يمكن لأناسٍ طبيعيين أن ينظروا بعين الود والمحبة إلى السعوديين"</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/86434" target="_blank">📅 22:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86433">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/86433" target="_blank">📅 22:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86432">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elyF_VeujOFyn7TD_--z8Mwf5O2Txx8012l_YviZoZjelsLPmxxlgOx84kN3hC9cAWfQfVb-BU-0dgDvClKVOZBvoVQC0IrTDZsob-vAdEi8ql8jAFZgwu4ccaEHDRKph8e2KSKbhrf9aXThXg5DsnP6kHq3oAm-J7PUfnhcfDvaoTKGRlbWDNrtHpfYBBPRWwGmSsR35jnc2aGp8etMzn6_4rqrsYY07yZC2tWig6A0pgpa_QOyVIyU3s32hmQS9BbD5JV7zyvOMQACTeNBCtwlSzelh7BAsiAE6G-Oo9PegA3hjKVkqJubCBiApnHMgzrzWzFV_bybjH76D8MWWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86432" target="_blank">📅 22:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86431">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
🇷🇺
الخطوط الجوية العراقية تستأنف رحلاتها إلى موسكو بعد توقف دام 5 شهور.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/86431" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86429">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a90d4340.mp4?token=qVHft9boGr3kbBIeF_JHzCTN95OesIv_zx8QCqCiXpn7ZVjkzZRKF7ZV8K1VlnBGtDOQ52pa4uJYXiytRgr3CKP0zY6b8nNw0P3tvP5hrFrxe4WGEMzhowqRHbbDtHwM6qkWpcm-gYKt3ZhBjnoOBLw9IdXXio8Oe1jbqUN3Ux4p0ehJlbj0WWbFwX9_IqGV3ZxDZhMdtwe6CgMZwg7n4ZS4dKReahWbQOgoNCxNGJaPSsk1yHQ9MRcDnOYJb021_2kDHONt2fg8iQ268tqGyG6kLaxzknm-bFitkSoSjz3P12AcoRy9Jk7ahxSsA-73PfMBIdJIum0l6gGIugVjAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a90d4340.mp4?token=qVHft9boGr3kbBIeF_JHzCTN95OesIv_zx8QCqCiXpn7ZVjkzZRKF7ZV8K1VlnBGtDOQ52pa4uJYXiytRgr3CKP0zY6b8nNw0P3tvP5hrFrxe4WGEMzhowqRHbbDtHwM6qkWpcm-gYKt3ZhBjnoOBLw9IdXXio8Oe1jbqUN3Ux4p0ehJlbj0WWbFwX9_IqGV3ZxDZhMdtwe6CgMZwg7n4ZS4dKReahWbQOgoNCxNGJaPSsk1yHQ9MRcDnOYJb021_2kDHONt2fg8iQ268tqGyG6kLaxzknm-bFitkSoSjz3P12AcoRy9Jk7ahxSsA-73PfMBIdJIum0l6gGIugVjAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات هبوط واقلاع من قاعدة موفق السلطي بالاردن منذ عصر اليوم والى الان.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86429" target="_blank">📅 22:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86428">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
من تشييع جثاميين الطاهرة للشهداء الذين استشهدو في القصف السعودي على الاراضي العراقية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86428" target="_blank">📅 21:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86427">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
‏اعلام السعودي: بعثات غربية في بغداد أعادت تنظيم حركة كوادرها وقلصت التنقلات الخارجية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86427" target="_blank">📅 21:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86426">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
‏الاعلام السعودي: السفارة الأميركية في بغداد تصدر تعليمات تقضي بتقييد حركة موظفيها.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86426" target="_blank">📅 21:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86425">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
‏
الاعلام السعودي:
السفارة الأميركية في بغداد تصدر تعليمات تقضي بتقييد حركة موظفيها.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86425" target="_blank">📅 21:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86424">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=b76p15bM5ak1KoT6PAUdQU8xhQmOqrHLDpJsWwl8a4MAv_WEl-DLGgDjhpTepjSNTgXKLZA1VaTUy92-urS15q4dcvDbQjkPbM21L4lWYpY7m5hVWL2fktOo1_nblkToW7OPUeFAjWdwCmW2fl0TjFaoOUvPYLVOKkEotJyiRYmOq4mYvR5LWw09F0uLHP0JySX2f5Ai_OJJh-pI4KJxu59R9of6htWpmHKt7wy-YHUTyUB2ZAKHHUWH4KwXWvhS1W5EOWJ-Opm2u7TvcGrCkWsl7uDQp5m3zP-U0e-Qo6tDsSNYUXR0hIzjBU6Tqluwj-bnENoR20MrjrtcUB3ZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=b76p15bM5ak1KoT6PAUdQU8xhQmOqrHLDpJsWwl8a4MAv_WEl-DLGgDjhpTepjSNTgXKLZA1VaTUy92-urS15q4dcvDbQjkPbM21L4lWYpY7m5hVWL2fktOo1_nblkToW7OPUeFAjWdwCmW2fl0TjFaoOUvPYLVOKkEotJyiRYmOq4mYvR5LWw09F0uLHP0JySX2f5Ai_OJJh-pI4KJxu59R9of6htWpmHKt7wy-YHUTyUB2ZAKHHUWH4KwXWvhS1W5EOWJ-Opm2u7TvcGrCkWsl7uDQp5m3zP-U0e-Qo6tDsSNYUXR0hIzjBU6Tqluwj-bnENoR20MrjrtcUB3ZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بيان العلاقات العامة للجيش في المرحلة السادسة والعشرين من عملية البرق، وانتقامًا لدماء الشهيد الأمير العميد ماجد كاظمي، الطيار الشجاع لطائرة سوخوي 24
التابعة لسلاح الجو الإيراني استهدفت طائرات إيرانية مسيرة مولدات الكهرباء وأنظمة الملاحة والمباني الإدارية والمساندة التابعة للجيش الأمريكي في قاعدة الشيخ عيسى
أسفرت هجمات الأيام الماضية، وكذلك الليلة، على القواعد الأمريكية في المنطقة، رغم أنظمة الدفاع والمعدات المتطورة فيها، عن أضرار جسيمة في معدات ومراكز انتشار القوات الأمريكية.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86424" target="_blank">📅 21:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86423">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
مجلس الشيوخ الأمريكي
يصوت ضد مشروع قرار لوقف العمليات العسكرية ضد إيران.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86423" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86422">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇪🇬
البحرية البريطانية تؤكد تعرض سفينتين في مصر لاستهداف بواسطة مسيرتين.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86422" target="_blank">📅 20:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86421">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏
الخارجية الفرنسية:
إغلاق مضيق هرمز يؤثر على اقتصاد العالم.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86421" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86420">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80be21696.mp4?token=qFQjCRVJiudBVGfgFeH_LhcwBmbBK-fR5gxBvfRDwtWURsRlGkFKsAf_2tsKPeXEaiNjTuPhl41JmVlaYZnIJ5kEMiTjirY9o-LpreSS-4LE7p2Zpv2KZZ_SJQCLA5SBjELD5fM-dO8i4F4KuXUXFAoZIKs-Yi5O7hbUnMOqRpgT6W-rqx9Zs_MEezjY9_Zy_p1nIafrnggiov1x4fEANddnEnVBpay4aPvKf8Pne1JrW9Cqtz66qwRWbFbdQcx3kDyCkZJbsRoV__RJRVnF7MlPPa5aq2wCNvtZjiuBbtREj0GgUH9KLbG58AjT8G0XrRV5V3WAOxq7m1gni4KZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80be21696.mp4?token=qFQjCRVJiudBVGfgFeH_LhcwBmbBK-fR5gxBvfRDwtWURsRlGkFKsAf_2tsKPeXEaiNjTuPhl41JmVlaYZnIJ5kEMiTjirY9o-LpreSS-4LE7p2Zpv2KZZ_SJQCLA5SBjELD5fM-dO8i4F4KuXUXFAoZIKs-Yi5O7hbUnMOqRpgT6W-rqx9Zs_MEezjY9_Zy_p1nIafrnggiov1x4fEANddnEnVBpay4aPvKf8Pne1JrW9Cqtz66qwRWbFbdQcx3kDyCkZJbsRoV__RJRVnF7MlPPa5aq2wCNvtZjiuBbtREj0GgUH9KLbG58AjT8G0XrRV5V3WAOxq7m1gni4KZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع صوت طيران مسير في قضاء كوية بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86420" target="_blank">📅 20:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86419">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phQQuJctdiG2t3ZUrZME-9EVsJuRNhF9UPeef-J5UwFfWXW2Zd19U2XBJKxsSWSuixNLd-7tK4QYC0DSUUIVSVrXUKhWg4OApgDhxQVM3mt5SXDEtt7LYTj5ndjYobA4D5VE5H-E4n26g1JR4U8ZIieiNdt16mcgrwct2xLSv_WLEe3Ea1lucccNHBwzR0ELtd7brnZyN8vLl68a3HPABt0jBt4U3D0h2R8E-HyVX3s-cON871cyW3o5ASJQSZ96LAUChTtUJf672UO5pIm1tIlEGfFNwWVrwZVQwRaX2bc4jgUBOd2IWY_qAVkcPZLVWuuVKI3TpZHDF5lLuJRUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام الاجنبي‏: السلطات المصرية حملت إيران مسؤولية الهجوم على ميناء دمياط.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86419" target="_blank">📅 19:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86418">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f68ec6f4.mp4?token=Nqo6Ri8L7-LgsFCdPGr22o96gg5iTYWe49shrVXHPY6-C5LIgsVUjXMkTyaXCocgUWQHk3Ij-0yT7HLxn9_7sW0AynRVFFvb5hErFph_ecwG8kj8ZtxTubHihEXipvXADOkTXAmG37Z4kUREwep-qGYeFRDgw32bP89qzzg5JTlrwCccDAGCumk5LFO8jDTrZddLGKo7nslfSrKWRyqwPczFbhxmPuR6Mz36xO3zWKIBWGf0mCFhf6ajUyvMheyd5Z0gcblU3mo4k5zVdxKGVo-DVPeZoPUcbVDd5Sd-FV1B8gJtzdtpetcQ5OPX7QbbEhCKdJ4DLCtWSaEEwY8fiTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f68ec6f4.mp4?token=Nqo6Ri8L7-LgsFCdPGr22o96gg5iTYWe49shrVXHPY6-C5LIgsVUjXMkTyaXCocgUWQHk3Ij-0yT7HLxn9_7sW0AynRVFFvb5hErFph_ecwG8kj8ZtxTubHihEXipvXADOkTXAmG37Z4kUREwep-qGYeFRDgw32bP89qzzg5JTlrwCccDAGCumk5LFO8jDTrZddLGKo7nslfSrKWRyqwPczFbhxmPuR6Mz36xO3zWKIBWGf0mCFhf6ajUyvMheyd5Z0gcblU3mo4k5zVdxKGVo-DVPeZoPUcbVDd5Sd-FV1B8gJtzdtpetcQ5OPX7QbbEhCKdJ4DLCtWSaEEwY8fiTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتنياهو
: عمدة نيويورك زهران مامداني، "يدعم إيران وحماس وحزب الله".</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86418" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86417">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace29ffb85.mp4?token=cnKnpy-1HMksHgusQ9nubbxPOhmGWTTrtFNjJrufMrGnQIgjl49NYOegf3sXq36tShaeTM0SqNwJWwDjD6dsfOPFcuJO4S833ALD5A7t3zoJk_gWBneL_ss_6ZYpOCZCFxEZOAbXi3iY6BPLY979LPUblCEsLXSpctWaPUjbzfTTSGzJNtd3885tBN6EcK35JpSP1dYu9_ZuIV0_1A9zNvoe2DVzoKH8PGCwy-H1SVx9-5S52xZVveNeQjcgNF26RD8cTwr_7mloM_cDnYWCm5rjXSr8kmSjcSJxkVFB7nArPUxYfYSbYtzx-Q7ECdH0mtQFhOkQrtgJIJT_dRxBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace29ffb85.mp4?token=cnKnpy-1HMksHgusQ9nubbxPOhmGWTTrtFNjJrufMrGnQIgjl49NYOegf3sXq36tShaeTM0SqNwJWwDjD6dsfOPFcuJO4S833ALD5A7t3zoJk_gWBneL_ss_6ZYpOCZCFxEZOAbXi3iY6BPLY979LPUblCEsLXSpctWaPUjbzfTTSGzJNtd3885tBN6EcK35JpSP1dYu9_ZuIV0_1A9zNvoe2DVzoKH8PGCwy-H1SVx9-5S52xZVveNeQjcgNF26RD8cTwr_7mloM_cDnYWCm5rjXSr8kmSjcSJxkVFB7nArPUxYfYSbYtzx-Q7ECdH0mtQFhOkQrtgJIJT_dRxBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من تشييع جثاميين الطاهرة للشهداء الذين استشهدو في القصف السعودي على الاراضي العراقية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86417" target="_blank">📅 19:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86416">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/987b1f2bad.mp4?token=UUQrObsTQ-2uffNnIxgcYhnJUDxQQkj2cCPODraKztFmvG-G8EXi7njebKuskEefBJt8fI9_1ZqKgLGyOaDKF_yIHP--Zq_BQa2hFs8stIwjMC_YcomPBRgimTNaQRkA_Xq4qtkVXokUVf8L8tV-pwsIcKXQgrmMvScqeeRHEgWMwKKXLmZhZ4c_iyJ65rY9X3mIEqQU8mZDvSr4OuN2s1UJVCa7KCEuBPLPsASMl8_Py7O2cqe_yWMKg_0UL9HAuk64kwr4obBg3lTfkBBiCqkj9GIL9QxDaYgiEZCwYCJxh5X9mhRTYWlH7KayKzXAF6-TEtKiwerZJLlDpW_w6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/987b1f2bad.mp4?token=UUQrObsTQ-2uffNnIxgcYhnJUDxQQkj2cCPODraKztFmvG-G8EXi7njebKuskEefBJt8fI9_1ZqKgLGyOaDKF_yIHP--Zq_BQa2hFs8stIwjMC_YcomPBRgimTNaQRkA_Xq4qtkVXokUVf8L8tV-pwsIcKXQgrmMvScqeeRHEgWMwKKXLmZhZ4c_iyJ65rY9X3mIEqQU8mZDvSr4OuN2s1UJVCa7KCEuBPLPsASMl8_Py7O2cqe_yWMKg_0UL9HAuk64kwr4obBg3lTfkBBiCqkj9GIL9QxDaYgiEZCwYCJxh5X9mhRTYWlH7KayKzXAF6-TEtKiwerZJLlDpW_w6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مسير معادي في سماء محافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86416" target="_blank">📅 19:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86415">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الاعلام الاجنبي‏:
السلطات المصرية حملت إيران مسؤولية الهجوم على ميناء دمياط.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86415" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86414">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
سماع صوت طيران مسير في قضاء كوية بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86414" target="_blank">📅 19:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86410">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHZ7GUmeLIfAIErkbL_p2A3YS9M8JvOvgj0dhKqSS3Us7eLIsDGLkXgWqeqtD60YRcz_CdD54S_x7Jequ4SU3exQzFl6b5g8vANTmup-sv4VC1IFpE7BLeANzmups5oP-9XOT-4VUaW_Kh2ZGcG3V-PYP6E0Ovq0i5GzorNw10sF--I1mmmpukIF3q77juqkFrvkf8r8SaXtdW22zSNPQGR4BOJJWOzRccLyUrcma0zkORSHKpCaqnjDqmyyXPvhee6ljaixuMPTkps2w29IKybfvawjUOJkEVSVuDWBNqPiLIYgulMn2gFcHcAIl5jDDJSCw7r9TxySkD_QLndUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PE_T4kQjCRYDz5CVrIEk6QN40ACuwLrZuR6o0dI4k-JHzX1oLdHsZ0fiI6YmdRgHAHwltQ2wo1jm9iVY3HwitF_h6tZWZUUod6YfxhKqP1tggmM9xa8BMO2A2y7QAzEJ5vPJgnHynzwJsO4Q-KmGC7zNidAD-5zo0BfgUVMWG4yfDtCCBn0ZXX7ymhj3jT3BTUligIe_rW7bZYomLUzDN3nK3zbZgScOVAZYAV4-ftIffy7GDkDy--yZgmBkHP5-nRr579dMJAQhFheqP7tQWAdCaSryCQOSzJIM_l8KZp2P265CYT3lkRuuDkRR2nhwzLP4DJ8fl1OHUYYFcXDDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVMsSZ-HMfxPRgQUzyO551svjhIFC-82O66_65QhZTV6IFx4OxUi3MuNC7FhpF7bAeDp5ixvdS3AV0gkAX6PksVpbaca__GoQ767BmJRxKDt7Z8iqFB1dAN3Rn9UK5-s-W4JZjNGnNE5xbkcycqRn2Xs28vfp7tLfeOu-SE2YZeetBivKKsERd9KEr7r-1yk5nJX_jX8k9bo4wnKJihs2N_avC_qEaLg-OatmGuVQ68N2GjIfaTYWJs7xTaUv7rczm-IgvadCSN8UvgnIuN3Vhkae_vjCnMMkCiHAnzaAPcrDmdXwRg62M6EE-l8Gv72rfWofeaIZpZ7fD3XdGz1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRDJBTS4QrGPlAa9poS1SJQcp0YaGlCx5AqleY9t9XxqV80WbdK7K3__5DOoeUr2GVZFdd9oIBlllWwiCtRPAaRDwIvDO7BDHNibcPHiazAFpyYeAvekaHfdHYBpWPYS5H2yZFRA6KeLXh-XRdEyGCee2KF_OwcdtdsQ9JGdhm4BeDsPvEEMpf9nhC0QZxYAMnIw0PMCMu6rb6MYHKWn5jlmUlaZUzkk0Or9CsNC6xfGFTT0BCBWajylHe4mnpYLKLrXeY7bLqgPNiLaqVqDyr60ZGmZyJnUvQ5BGVNpns1O6Gq7-PqOpWyLMlRKzOVcvXWhGDaTqQBUHxxyc5TX7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇷
تشييع مهيب لجثامين شهداء الاعتداءات الاميركية السعودية الغادرة في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86410" target="_blank">📅 19:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86409">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏وافقت الاتحادات الوطنية الـ 55 التابعة للاتحاد الأوروبي لكرة القدم بالإجماع على مقاطعة كأس العالم وجميع مسابقات الفيفا إذا مضى جياني إنفانتينو قدماً في خططه لبيع جزء من الفيفا لمستثمرين من القطاع الخاص.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86409" target="_blank">📅 19:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86408">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8dcb22e88.mp4?token=Bq87OipJBEGH6nRnjVlICgxYyCDp916aOlVU8ZVqpSwxQKQ_B8zjMGiMt9FE7j_krK40RuzAHw2qLJ8sFBa0GVt8tLHv_r3LxnbixgblqcbDgCewUso5OoZqCMa31MZ1DUNb6mlVCgya9dMbIvAsJ-4aLsHHqzxKTMq4Ic67DirxSBgONX0qpVQ7IribFqjaG1tGQL5IA8e9YQb-M1yqdrWMbeVEvAEq57i5De59oi8OGJzLjxNdkAq6iDsvzyJ3AJGxTV9lFP5K7XDGJ1GuFCwo550NnUMHsbwvYovA2jyWip6fFsVGzA2kr5O6xAet5fbUNIjlPrtu90yJsuSntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8dcb22e88.mp4?token=Bq87OipJBEGH6nRnjVlICgxYyCDp916aOlVU8ZVqpSwxQKQ_B8zjMGiMt9FE7j_krK40RuzAHw2qLJ8sFBa0GVt8tLHv_r3LxnbixgblqcbDgCewUso5OoZqCMa31MZ1DUNb6mlVCgya9dMbIvAsJ-4aLsHHqzxKTMq4Ic67DirxSBgONX0qpVQ7IribFqjaG1tGQL5IA8e9YQb-M1yqdrWMbeVEvAEq57i5De59oi8OGJzLjxNdkAq6iDsvzyJ3AJGxTV9lFP5K7XDGJ1GuFCwo550NnUMHsbwvYovA2jyWip6fFsVGzA2kr5O6xAet5fbUNIjlPrtu90yJsuSntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
سنتكوم تنشر تسجيلًا صوتيًا تزعم أنه يوثق تهديدًا منسوبًا للحرس الثوري للسفن التي تحاول عبور مضيق هرمز لمخالفتها قوانين وتعليمات العبور.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86408" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86406">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
🇾🇪
🔻
رويترز : قال مسؤولان في المنطقة إن الحوثيين اليمنيين هاجموا السعودية هذا الأسبوع من الأراضي العراقية بالتنسيق مع الجماعات المسلحة العراقية، وفقاً لتقييمات أجرتها السعودية وشركاؤها الإقليميون، مما يعكس تزايد التنسيق بين الميليشيات الموالية لإيران.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86406" target="_blank">📅 18:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86405">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db13ec2079.mp4?token=LG24BfUBPS1HPp5qQ1goIEZW0USkCJ_yxVgSM1JGKjgqoPgUwXe0pEbe3QvTGWCeqoHeeLfQLVeGpSnj_Y3VPEOpsFiAasLweH5pPZ8LHNN5LKAYw4iBbQVTedlZ20bEHGAARLQVgZQhyUduP7x-7QsM3m8b4TS0gmtkt8PdJceOFbG43yXe5Ui98MnwXjYfHMNGQN8Naa2wCeBN0l473_BIdc--3-IBgiZ5fse8eb3UOuEJGabcAAnFb2ZTLrSACTK-BA2TTVyR9AabgYmkr5_yNFhGQ1-C4z3ut_RgamWxEvCdy4WjuN3Os9rXP8yU735iwq-GW3xj0WGw56M9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db13ec2079.mp4?token=LG24BfUBPS1HPp5qQ1goIEZW0USkCJ_yxVgSM1JGKjgqoPgUwXe0pEbe3QvTGWCeqoHeeLfQLVeGpSnj_Y3VPEOpsFiAasLweH5pPZ8LHNN5LKAYw4iBbQVTedlZ20bEHGAARLQVgZQhyUduP7x-7QsM3m8b4TS0gmtkt8PdJceOFbG43yXe5Ui98MnwXjYfHMNGQN8Naa2wCeBN0l473_BIdc--3-IBgiZ5fse8eb3UOuEJGabcAAnFb2ZTLrSACTK-BA2TTVyR9AabgYmkr5_yNFhGQ1-C4z3ut_RgamWxEvCdy4WjuN3Os9rXP8yU735iwq-GW3xj0WGw56M9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان يستهدف العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86405" target="_blank">📅 18:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86404">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هزة أرضية في محافظة كركوك</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86404" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86403">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انباء عن انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86403" target="_blank">📅 18:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86402">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انباء عن انفجارات في صنعاء</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86402" target="_blank">📅 18:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86401">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">السيد عبدالملك الحوثي: ترامب يقول بنفسه عن السعودي بأنه بقرة حلوب يحلبونها حتى يجف ضرعها ثم يذبحونها بعد ذلك</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86401" target="_blank">📅 18:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86400">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436447c59d.mp4?token=rpw-h2GuQsKczWQeZqAlserf8msRBQU3UNSLR_OgrYi3B8X9BeGrUt3hJ3vCFsKGKSUUreTAQaj3J7aUnK4W0QzRvilNQiCn4R5uHKM6KcaHoYv9E8qMPqI9fJB3EDZALy9EjvHfQmNx-zz6K8dWDHcVn9uNKFWUoryXOSTNix3xkaprTCkiGqqe4h_DJEFBV2NnmqeJzl4fdi-_2FkHV6-fvucLnj2HWHMsxANer0STLeDxhf5NNokCTTdwBFQhAy0VSePitnYqQ2GILYmJBj2OsHupkXDbLkDkSEafGJ9G2eAljhM7LGuaignAsgwNhzraeGUa64R-ijObf1bUgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436447c59d.mp4?token=rpw-h2GuQsKczWQeZqAlserf8msRBQU3UNSLR_OgrYi3B8X9BeGrUt3hJ3vCFsKGKSUUreTAQaj3J7aUnK4W0QzRvilNQiCn4R5uHKM6KcaHoYv9E8qMPqI9fJB3EDZALy9EjvHfQmNx-zz6K8dWDHcVn9uNKFWUoryXOSTNix3xkaprTCkiGqqe4h_DJEFBV2NnmqeJzl4fdi-_2FkHV6-fvucLnj2HWHMsxANer0STLeDxhf5NNokCTTdwBFQhAy0VSePitnYqQ2GILYmJBj2OsHupkXDbLkDkSEafGJ9G2eAljhM7LGuaignAsgwNhzraeGUa64R-ijObf1bUgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇰🇼
الاقمار الصناعية تظهر ان إيران تمكنت من استهداف قاعدة علي السالم الجوية الأمريكية في الكويت الليلة الماضية. لم يتضح بعد نوع المنشآت التي كانت موجودة هناك.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86400" target="_blank">📅 17:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86399">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
🤡
Zelenskyy, be careful tonight. Mama Odesa is in danger</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86399" target="_blank">📅 17:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86398">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2dVBuLEhshOPKRuR0_dFFtkNpFHl4nm53mLVIzn1i5Uc_0CLhpVO8-l1jV_h9lCQiGnQ9Po7AAO3-h7wCnp7J1FGXBDYofwPdjqgJOTf3wDY3bv1_7gSaFMt9cEJCn-klTmF0FhFQwi6-iBaA5V13OQ6aZETpHaGqUN86Fwuit7d91hsBpMHGlXASBm9auXs83pDDJUgd4oWmPncrM3pVJ1ECqkF8F4yw6cnYBa29DLEfTyESN5i2K7Vl0b7jJ4h2UEfuoP59dJ97hgAoXXVa3W3Z_rgwI4vfkw5u7Hb2GoO_2JtJPX57LrBwoHgcnvbByD041dZKYKsV-IbELCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام غربي : تعمل السعودية على تشكيل تحالف دولي يهدف إلى حماية طرق الشحن في البحر الأحمر من هجمات الحوثيين، وفقًا لمصادر مطلعة على المناقشات.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86398" target="_blank">📅 17:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86397">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇾🇪
🇮🇶
السيد عبدالملك الحوثي: نتوجه بخالص العزاء والمواساة إلى الشعب العراقي العزيز ومؤسسته الأمنية ومجاهديه الأعزاء وإلى أسر الشهداء في العدوان الأمريكي السعودي الغادر الظالم، نستنكر وندين العدوان الأمريكي السعودي الظالم ونؤكد على تضامننا الكامل مع الشعب العراقي…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86397" target="_blank">📅 16:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86396">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇾🇪
🇮🇶
السيد عبدالملك الحوثي:
نتوجه بخالص العزاء والمواساة إلى الشعب العراقي العزيز ومؤسسته الأمنية ومجاهديه الأعزاء وإلى أسر الشهداء في العدوان الأمريكي السعودي الغادر الظالم، نستنكر وندين العدوان الأمريكي السعودي الظالم ونؤكد على تضامننا الكامل مع الشعب العراقي ومؤسسته الأمنية ومجاهديه الأعزاء بكل مستويات التضامن والموقف.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86396" target="_blank">📅 16:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86395">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhnyQfqLOFtncCGJkZuTsNCxeZogjisixhGWCbHD2YNdShnXllHK4vXJAJwxiX2qKwM2s6Nzs0z6jtSfYoYPIwtk-Exg0osLRbXuYaGxgZajt7z18nufcU8WHpTZKBVH-RkoJc7eoSQVRsLfaFT15wRMwKjaq30j53TV7xX6L1whPXtcPnrUu83XA-kVfjTlkSV1ziLFR1JZu1TWrZCGCWvcK-Mu-rtfmQeT_Ht88No2kWL0be51IZ2NifLrzVplegHMp7e7950_Voj-GvzRfZC2n9gfSJ7ixdSbmSxvAgGt3to6HHGgTkD8et8Lt2MdO7pFcHnvsfIzxnX7VqsdCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:  صباح اليوم، وفي إطار العملية "النصر 2" ومعاقبة الغزاة، تم استهداف قاعدة جوية أمريكية في علي السالم، حيث تم إشعال وتدمير منشأتين للطائرات بدون طيار وخزان وقود للطائرات والمروحيات العسكرية.  يجب أن يعلم المسلمون في الكويت أن معاقبة الغزاة…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86395" target="_blank">📅 16:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86394">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0b5a4b97.mp4?token=qlwVIpkri_aXm89YrkMr338xNV5ZMSLX492EVrTn1xV6dnxr9n4dGUauMrfTeyXKvcAQLA8gz7LxwPiIAzV-fr3-ThoM9qbgCRpRIhnh_0UlvlIAfbMN_Gpd3c_m0fKYxeDZcNYOahM0dIcuTEi9pPl5ASUVOtCNC5eaLxyEeWJvPR5eY2OWxmrLmCf-XADjFYFOqOkMerK-UWh-za8BWekpwQthRrHa8zaIF1djpE0wwhfXeV2wIU-9qdeKUppBBwytBIdYLGzxYc3nmajVlEYGuxGnUJFOter_9inw9Fnh_xDlj6t_9HacmaKSP7fCqpkgQVtsZ26GApgBhiAhYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0b5a4b97.mp4?token=qlwVIpkri_aXm89YrkMr338xNV5ZMSLX492EVrTn1xV6dnxr9n4dGUauMrfTeyXKvcAQLA8gz7LxwPiIAzV-fr3-ThoM9qbgCRpRIhnh_0UlvlIAfbMN_Gpd3c_m0fKYxeDZcNYOahM0dIcuTEi9pPl5ASUVOtCNC5eaLxyEeWJvPR5eY2OWxmrLmCf-XADjFYFOqOkMerK-UWh-za8BWekpwQthRrHa8zaIF1djpE0wwhfXeV2wIU-9qdeKUppBBwytBIdYLGzxYc3nmajVlEYGuxGnUJFOter_9inw9Fnh_xDlj6t_9HacmaKSP7fCqpkgQVtsZ26GApgBhiAhYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:
صباح اليوم، وفي إطار العملية "النصر 2" ومعاقبة الغزاة، تم استهداف قاعدة جوية أمريكية في علي السالم، حيث تم إشعال وتدمير منشأتين للطائرات بدون طيار وخزان وقود للطائرات والمروحيات العسكرية.
يجب أن يعلم المسلمون في الكويت أن معاقبة الغزاة مستمرة حتى يتم إنهاء نهب ثروات وموارد المسلمين الوطنية، وطرد المحتلين واللصوص الأمريكيين من المنطقة.
ولا النصر إلا من عند الله العزيز الحكيم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/86394" target="_blank">📅 16:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86393">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg7Efq5TZd9lHgxBoXmvI59siMyhd01uQLb-EdTvWXbIkOrwobVIieyKcTjw3MSNsQLil5DFwHwPlvMwk4U-kaCv6_4yrmqRh8zDfjYMctDYi28mI_AJx6iN96sijjhbsmZe1xPI56BYCHosBeF2CpYZ2foE1SUitoRRx6Ef8mY_8lk45gyOuJNdFMe1Zpb0CZpHhJ4cQSq5KTLIuUyp2keQcd1GgdHY2nl_MXHwBgtO_8cOXW-Toui2yLltMmpb3YeQ5iW-kYoapjcOmBcEc080yI2jLLo1Wi91xAEYZtDQkeDDWbpUI4fUw2VkNNGbAh9tkZw-xnDaFZF76XGj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇵
🇷🇺
اوكرانيا تزعم:
من المرجح أن روسيا استخدمت ولاول مرة صاروخًا كوريًا شماليًا في هجوم مميت استهدف مبنى بالقرب من مدينة كريفي ريه.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86393" target="_blank">📅 16:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86392">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇪🇬
🇾🇪
مصدر بوزارة الخارجية اليمنية:
لا صحة للشائعات حول استهداف اليمن سفينة في ميناء دمياط بجمهورية مصر العربية، الموقف اليمني واضح ومعلن وصريح ويستهدف النظام السعودي فقط لحصاره الظالم وعدوانه المستمر على الشعب اليمني.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86392" target="_blank">📅 16:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86389">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJeCdcbFDU4BPHV1OOBD8v6gIqmhc2ia8ANS-Gqerhaz_xwpHIEuOpU8hl5X55n8eHyAC196abnVBj86sKZ4F4YOmrP7v0l43IKQuOilkldlxfeNDhBxJPD0RP7_SnzTeSkdOJG_-4kfvpDIey7Be53MAWWYemecuWt1C5BHWDs9RLSRmY60KbwaGNnkgZ6WvVvpyHavYqTZT69f1PzUmFyPCaRiJ2A7hK_wsiG9KdyOVo7lAKqvbGV-XeoRCPJnEoP4wmoQcu3_rEBZpYTWToVYaZN_kgP9Iwi65cKdMl0aNbpW3s8Feh6-6o4fmSxiat4_WR9TJg7KngYEmTRISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5lZg6eJ9cr7ji6qVdC7QdoiJ6GfWHUZfc2x1V_84dpFj0b_STGou_zLUNGwBvVxvAz7rxcSxrykQYJIW_kn64JsYCVrQRhP0T2PN9VBImTGJUk9zepwlAbdpxcwrQDCgPu9cvsibcG0NsxN0lc2i8Y1RMviv5MkoQ61dnhUWWsqTL025bPAIfWLVv7Hd5dEIFpOE0LNCbx3PGGWG24fqOeps26s6Rl4TCG1IRo8bO30qXOgYBYQeugpF2--xvT_1pCTnF8Mhc9b7W4gMIqi2gCtC72N0Zrm7Ryr0E1vkRB_-JlTwBs9JDg5VuHYkDrF3l32vBMJBO5kNgqENK2nkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKH_uKUlIN1Z8QA4i3dPSx3yIqu_M6XyOJEOA_wdrjclqU-NUfxnFjQTg46ctAJyUgbz2tPISaeNePg9oaLdVHM1qKJm4plo1msyvMi8nOrOK6YuuPqC7867vHcBl7o_RBmMZpoy-hvz63WRbBQCN-xH36Kbzd6Iq5p6_8264za84_X0vUqjs17JcEom-yGRWKWkDCsaaGvkEeQukAIr6iCUyXtefKXFUabDhapbDNbVZmM4AhRt0JQmb04JtmBYzGGuFzbGSFnHp1H9e0arHQlmnwzF7_sh3G6bQsFbCJbG7Igs91SWy02uuqEJOxR00IjPOoEZwTGPkGN8AuOj_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
خاص لنايا |
هبوط عدة طائرات امريكية في قاعدة عيسى الجوية بالبحرين.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86389" target="_blank">📅 15:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86388">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية
:
في مؤشر يفضح مستوى التنسيق والتعاون الأمريكي، السعودي، الإسرائيلي، استقبل المجرم ترامب كلاً من المجرم نتنياهو ووزير دفاع النظام السعودي.
أن هذه اللقاءات تأتي في وقت يرتكب فيه كيان العدو الإسرائيلي، أبشع الجرائم بحق الشعب الفلسطيني واستمرار احتلاله للأراضي اللبنانية والسورية والعدوان الأمريكي المستمر على الجمهورية الإسلامية في إيران والجمهورية العراقية وبمشاركة النظام السعودي الذي يواصل حصاره على الجمهورية اليمنية وانتهاك سيادتها واستقلالها.
تلك اللقاءات، تكشف الدور السيء الذي يقوم به النظام السعودي في المنطقة العربية والأمة الإسلامية خدمة للمشروع الصهيوني ضمن مخطط ما يسمى بتغيير الشرق الأوسط.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86388" target="_blank">📅 15:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86387">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">النتن يتعرض لموقف محرج
🇮🇱
السيناتور الأميركي جون فيترمان يستقبل نتن ياهو مرتديًا سروالًا قصيرًا، في مشهد عكس حالة من عدم الاكتراث إذ بدا منشغلًا بهاتفه طوال اللقاء دون أن يُظهر اهتمامًا يُذكر أثناء الاستقبال.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86387" target="_blank">📅 15:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86386">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇱
إنهيار في جيش الإحتلال.. عناصر الجيش الصهيوني يتمردون في قاعدة سديه تيمان بعد خلاف مع قائد الكتيبة ويتركون أسلحتهم ويغادرون القاعدة إلى منازلهم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86386" target="_blank">📅 14:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86385">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله أكبر
إسقاط مسيرة معادية في سماء ميناء الامام الخميني بمحافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86385" target="_blank">📅 14:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86382">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad4e6f260.mp4?token=MzYX7ZXu0D1fZwsnFysjSyxyldAmEk2kWfQM_nCmRqVzIdvej6O4GFQiOmo0-OFSF9LPz44mreWn8dLdpU7xKbCkJ9wCI1FiaBEH21G3UjKJSEmqYpq5Ss32khs5cmCzwuqjgcdOIhKhit9UxseQSHR33snR66APPXI6YgsmNrdeTo3OmBMJ4LgYRknXw4cWEc0ur1aPMWjasCQ77MZs2jtivOASVK_VsW8_NADYo3mdU5GYyNAXbQ1xq7C2-2SV5H4KsTAoTPzOt903v0cz5rbcJECZJS5lPBdRqn-NlWz2YDh4YOdsM3kRi69v06Xk7gMQAqe_IXXAERVaOxCjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad4e6f260.mp4?token=MzYX7ZXu0D1fZwsnFysjSyxyldAmEk2kWfQM_nCmRqVzIdvej6O4GFQiOmo0-OFSF9LPz44mreWn8dLdpU7xKbCkJ9wCI1FiaBEH21G3UjKJSEmqYpq5Ss32khs5cmCzwuqjgcdOIhKhit9UxseQSHR33snR66APPXI6YgsmNrdeTo3OmBMJ4LgYRknXw4cWEc0ur1aPMWjasCQ77MZs2jtivOASVK_VsW8_NADYo3mdU5GYyNAXbQ1xq7C2-2SV5H4KsTAoTPzOt903v0cz5rbcJECZJS5lPBdRqn-NlWz2YDh4YOdsM3kRi69v06Xk7gMQAqe_IXXAERVaOxCjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إنهيار في جيش الإحتلال..
عناصر الجيش الصهيوني يتمردون في قاعدة سديه تيمان بعد خلاف مع قائد الكتيبة ويتركون أسلحتهم ويغادرون القاعدة إلى منازلهم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86382" target="_blank">📅 14:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86381">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:
أُذِنَ لِلَّذِينَ يُقَٰتَلُونَ بِأَنَّهُم ظُلِمُواْۚ وَإِنَّ ٱللَّهَ عَلَىٰ نَصرِهِم لَقَدِيرٌ
أيها الشعب الأردني الكريم والنبيه؛ إن تكاتفكم وتعاونكم الصادق، وخاصة مواقف بعض المثقفين الأردنيين الواضحة، قد ضيق الخناق على العدو وجعله في موقف ضعف.
في فجر اليوم، قام العدو الأمريكي، بدافع العجز عن المواجهة العسكرية الشريفة، وباستخدام القواعد العسكرية المحتلة في بلدكم، بشن هجوم جوي على منزلين سكنيين في جزيرة قشم، مستخدمًا قنابل مدمرة. وقد استهدف هذان المنزلان البسيطان اللذان يقطنهما أهالي محليون، مما أسفر عن إصابة الأب والأم وطفل من عائلة شهيد، بالإضافة إلى إصابة طفلين آخرين.
ردًا على هذه الجريمة، وللمساعدة في تحرير الأراضي الإسلامية في الأردن من عار الاحتلال الأمريكي، قام مقاتلو القوة الجوية التابعة لحرس الثورة الإسلامية، في وقت مبكر من صباح اليوم، بشن هجوم على منصة إطلاق وصيانة طائرات F-35 التابعة للعدو الأمريكي في القاعدة الجوية في الأزرق، مستخدمين عدة صواريخ باليستية. وقد أسفر الهجوم عن تدمير كامل لثلاث طائرات من طراز F-35، وإلحاق أضرار جسيمة بثلاث طائرات أخرى.
كما أسفر الهجوم عن مقتل عدد من الضباط والفنيين والمهندسين المسؤولين عن صيانة الطائرات التابعة للعدو.
منطقتنا ليست مكانًا لجيش يقتل الأطفال، والذي يرتكب هذه الفظائع بوحشية، ويقتل عائلات بريئة في منتصف الليل أثناء نومهم. ستستمر معركتنا ومعركتكم حتى طرد آخر محتل أمريكي من الأراضي الإسلامية.
«إِنْ تَنْصُرُوا اللَّهَ یَنْصُرْکُمْ وَ یُثَبِّتْ أَقْدَامَکُمْ»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/86381" target="_blank">📅 14:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86380">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة أرضية تضرب الحدود العراقية الإيرانية مركزها مدينة حلبجة شمال العراق.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/86380" target="_blank">📅 12:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86379">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
لمعرفة خطة تحويل الطرق والمسارات البديلة لزيارة الأربعينية في العراق التي نشرها الإعلام الأمني انضموا إلى قناتنا الثانية عبر الرابط التالي.
https://t.me/nayaforiraq2</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/86379" target="_blank">📅 12:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86378">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇦
🇷🇺
🇵🇱
تصاعد أعمدة الدخان من حدود أوكرانيا _ بولندا بعد انفجار صاروخ كروز روسي من طراز "Kh-101.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/86378" target="_blank">📅 12:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86377">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇪🇬
انفجار بمحطة الغاز الطبيعي المسال في ميناء دمياط بمصر أثناء تفريغ شحنة</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/86377" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86376">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام العراقي:
القوات الأمنية الرسمية هي المسؤولة حصراً عن الملف الأمني ولن تسمح بوجود أي سلاح خارج إطار الدولة".
القائد العام وجه فوراً بتكريم عوائل الشهداء وتوفير الرعاية الصحية الكاملة للجرحى، بما في ذلك نقلهم خارج العراق إذا اقتضت حالتهم الصحية"، مطالبا "بتقديم الدلائل والبراهين بشأن الادعاءات حول انطلاق اعتداءات من داخل العراق".
"الحكومة لن تسمح بأية تصرفات فردية من الداخل، وفي الوقت ذاته لن تقبل بأي انتهاك يأتي من خارج الحدود".</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/86376" target="_blank">📅 11:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86375">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
زلزال بقوة 3.4 درجة ريختر يضرب محافظة خوزستان الإيرانية</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/86375" target="_blank">📅 10:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86374">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVZLQfJt23K0aphleQLPexM8icqCOToJ08VlEqRhAExFSqjTzUjGqGdoM8fb-8609h32bH2rwQrK7Dn3M5OYETHrkuv7hZigKTPRdVm-0Vpnt430qe35RpQS-jqfqRKSs0Wy4K6orMSAilkcCLrBUETGo1vWhKN9Y3JI3jD3WzV6WGko8pBKKy9BfhXcuXg0WUCZtgBWPJf-AqILW6pvA5LwLLGZPfz3aSnlrL1NPN7DKUgOfZoDPakkopnXDfgJtcmjQsC_7toKisS-MNCPCONC5dVDJFLV6I7A1OqwU2HJv5UngbleLVhNdJWcTyhKQhFDubWlRoGPQSauBHW3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الحرس الثوري الإيراني: بمشيئة الله تعالى، سيتم اليوم معاقبة المعتدين.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/86374" target="_blank">📅 10:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86373">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الكويت: هجوم ايراني استهدف مبنى تابعًا لإحدى الشركات الصينية مما أسفر عن مقتل أحد العاملين، وإلحاق أضرار مادية جسيمة بالمبنى.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86373" target="_blank">📅 10:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86372">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/86372" target="_blank">📅 10:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86371">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrZnsiH9QyRbN0pH6_aIA3pbuS6aXcO0rBlEWzN3ciMk88nKf4IZt5QQGG1vIdISyWkLOaMukZFHDTDTAggODn83Ssu1E554yC8Gtp3tyR6twFDgZrL9oEeCEozOwa_7EGO6hn5loB_gXvutTW-PiQBFYPCbPwHfKh70zpT7LQ0E7DJe_ymXGbhBbpAWEO6A_tEZKaWIphMsFag7tcIFJBlIf6rMspjiBGJe-DNRID_T-7a4FqvAhXSFV0Ouau6wfaiJ-GAiEX5o-Os1lD7fFFMvmrpLUvy_sX61EX2fGc37StTNWb8SUwInOXFjaO7av_2LAbUI6pFoTc1wxNYNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد مقتدى الصدر: عدم حصر السلاح بيد الدولة لا زال يتسبب باستشهاد المجاهدين في الحشد الشعبي والقوات الأمنية بلا وجهة حق.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86371" target="_blank">📅 10:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86370">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqUnD3ZuFUpYZL8gQn6uTSopwv2DkN-XYMkNqNasf6n_3jFVTV759_nR2gVnVNihbBx-zGLH8rpyt6vqiCMnvY1BXycC2SWVZhin2hxpzq8UbBqFFqUZi120YxIkUGoGthX6lZx6piuKJgHgUc0ay-VSu9cL9EBHYFVmSGgpUtHHj1QiNrUUnx1-3r_LOrCnqP-GngGJ3WK-fqG6n-J_aSmSB3NvMug6-JB5PwAIb4hCEB1bmL_LkOC2GewpGHz-UFLRPxWDYfMULE7KJiuQxCVEp36Q0CrcLd2ObbwUlAIwFbqROXCHpmNW6ezwCegjz-TtZkBbRwK9SFhfKhkOyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار النفط بالارتفاع بعد تجدد الصراعات في الشرق الأوسط حيث وصل سعر برميل النفط الواحد إلى ما يقارب 93 دولار.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/86370" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86369">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شركة أنابيب بحر قزوين: تعرض ناقلة نفط لهجوم من طائرة مسيرة أثناء تحميلها النفط في مرساها.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/86369" target="_blank">📅 09:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86367">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شركة أنابيب بحر قزوين: تعرض ناقلة نفط لهجوم من طائرة مسيرة أثناء تحميلها النفط في مرساها.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/86367" target="_blank">📅 09:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86366">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8NpnJGDyu9jVRMtB8w1ZiC5DwGFOqE15XaPaWHox_oXGeT7Ka_rljnpjENsGlCATmlmSql9_q0eqpisqsZW6X00gieel8g_AFYlA-Km-uLEV2_aMVdjURuPJWRbvjYt3boZkeY6jHNNM8I_JYj1vb5FOSk01T4xPqKUgPo90wHc7Ieip62ConJC4CA9LO7bAJc_SX1lXQq8iKXqNI4CHR56feepQHNNCs1GMvtGJkA3h4kVNPb9T7BuGHmycV-kDqNHtrZm6u5z7v7MG6OnqsDRvTP9fLvnokJgx76QwQbV47SWRJ6EETD0Uz-4VFiVZIKTjiZFAt8Tc2y4Pu31zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇯🇴
بعد فشل الدفاعات الأمريكية بالتصدي للصواريخ الإيرانية ؛ تظهر بيانات الملاحة الجوية إلى أن طائرات عسكرية ألمانية وفرنسية توجهت إلى القواعد الأمريكية في الأردن لمساعدة الاحتلال الأمريكي في اعتراض الهجمات الإيرانية.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/86366" target="_blank">📅 09:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86365">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/86365" target="_blank">📅 08:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86364" target="_blank">📅 08:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86363">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني:
الليلة الماضية، حاولت ناقلتا نفط، استفزازًا من طيور أمريكية، مغادرة الممر غير الآمن جنوب مضيق هرمز، ولكن بعد اندلاع حريق هائل في إحداهما، عادت السفينتان أدراجهما على الفور.
مضيق هرمز أرضنا، وبحارة البحرية التابعة للحرس الثوري الإيراني يسيطرون عليه سيطرة تامة، ولن يُسمح لدخيلٍ قادمٍ من آلاف الكيلومترات بالتدخل فيه. وبعون الله تعالى، سيُعاقب المعتدي اليوم.
ستتلقى الدول المتورطة في مساعدة المعتدي ردًا قاسيًا إن لم تُصحح سلوكها.
لن يُفتح مضيق هرمز ما دامت مبالغات وتهديدات المسؤولين الأمريكيين وتدخلهم في الحركة البحرية بالمنطقة مستمرة، ولن تُؤدي التهديدات والتدخلات إلا إلى تفاقم الوضع وتعقيده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86363" target="_blank">📅 08:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86362">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2411719d9.mp4?token=FvZTYyqM8kP6NMl8BE1moCE-jGKurODQA4D8R7tcJIbLn6jlatXNZvWKvEgJZ323z13K-X1DOAk8Yf2AUE7HgEiR-5d7rv9xb81BbUrrQu14tRcx7I_fDLnfLyA6wsb4iwbQNfZjRpUZDqdvceYKMnMCvBAIcXNEKl7h2ELkmYh7J1vDAEk0ORfUku3VDQNW2T2edH8e_FZ2-r8Ai-657QGxoLa6OmhveWR_7IuLV4D9GdRSL1bkBW3HgVtE5Fw7jLXoUXRBp0va_7Vy3Y5mLlKGnYwGq8f0cnms_BBFziDGd0klMfmYuxOQaPmipFFbwggR9QLc1b29wKTLV4ITmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2411719d9.mp4?token=FvZTYyqM8kP6NMl8BE1moCE-jGKurODQA4D8R7tcJIbLn6jlatXNZvWKvEgJZ323z13K-X1DOAk8Yf2AUE7HgEiR-5d7rv9xb81BbUrrQu14tRcx7I_fDLnfLyA6wsb4iwbQNfZjRpUZDqdvceYKMnMCvBAIcXNEKl7h2ELkmYh7J1vDAEk0ORfUku3VDQNW2T2edH8e_FZ2-r8Ai-657QGxoLa6OmhveWR_7IuLV4D9GdRSL1bkBW3HgVtE5Fw7jLXoUXRBp0va_7Vy3Y5mLlKGnYwGq8f0cnms_BBFziDGd0klMfmYuxOQaPmipFFbwggR9QLc1b29wKTLV4ITmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جثمان الشهيد ليث علك أحد شهداء العدوان الأمريكي السعودي على العراق يصل إلى دائرة الطب العدلي في محافظة ميسان لتسليمه لذويه وتشييعه.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/86362" target="_blank">📅 08:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86361">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1726eadc79.mp4?token=Ci4GF4r5ZAw4ZNyR-d20VSkDXOQL51pQiqlwZP-6wWE2LKg0mZRtZgfiuyG4aKIZ0v419wTanypn4tQ4P9sDS4F24w4fUl-epwk_r5YseLLLlk3U7QMAVhku7WEnJ83i03BJfxBUiMs5p79RJ1BvsizTh0caSL6V1je7reZgVoeJOhyKsqYgZLwk_bwci3F_yoRz34EXOnBx3g75CJhaBH0XUkFUKTiIRGUOrn_dNipQTu8R5YWWHUfPxnY1OzENI0tnDgOLJcxFNUxVGM27vrJwUFZ4rGS04d2lr9nQSxWz2r3IX3J-_mMuNL0MCdUsGhfbTtfklch6KNBXrBwvKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1726eadc79.mp4?token=Ci4GF4r5ZAw4ZNyR-d20VSkDXOQL51pQiqlwZP-6wWE2LKg0mZRtZgfiuyG4aKIZ0v419wTanypn4tQ4P9sDS4F24w4fUl-epwk_r5YseLLLlk3U7QMAVhku7WEnJ83i03BJfxBUiMs5p79RJ1BvsizTh0caSL6V1je7reZgVoeJOhyKsqYgZLwk_bwci3F_yoRz34EXOnBx3g75CJhaBH0XUkFUKTiIRGUOrn_dNipQTu8R5YWWHUfPxnY1OzENI0tnDgOLJcxFNUxVGM27vrJwUFZ4rGS04d2lr9nQSxWz2r3IX3J-_mMuNL0MCdUsGhfbTtfklch6KNBXrBwvKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة لانطلاق وفشل الدفاعات الجوية في قاعدة موفق السلطي في الأردن قبل دكها بالصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/86361" target="_blank">📅 08:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86360">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86360" target="_blank">📅 08:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86359">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86359" target="_blank">📅 08:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86358">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
مراسل نايا |
سقوط صاروخين بشكل مباشر داخل قاعدة موفق السلطي وتصاعد أعمدة الدخان بشكل كثيف وسط فشل فادح للدفاعات الجوية الأمريكية واستمرار دوي صافرات الإنذار</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86358" target="_blank">📅 08:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86356">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ct6LJYAidz11kl8HiyfOA-zo1AsLBBrN02SvjHoaDOMoM2zUHajcYbY7KTha7RQNPiPGyq0SAXPrqBHnFWmpgp7S0UcxvUusfX1DRO2GDOZe09XzUXtXXo-bPPXKOCC-JgAdxpUjU3K3BXW8hPX7MjQni38KJQR5sqVjmor3Ex5DYl1x9G2fNNW8x1Mtm6gv7KyULHHDqZKTNhtp7X0AfXsYc-fkNr-gmhLx70di7bIUQ0puPjEBM4g2o6u34Jojmp_OlGBm4we3TCAws1IzVtw0za3TKJlKHZshxk-NS-6AVl2ADNWfxhqki1iEKuAizyJT9fq_mstZk3qyccbDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_WG-IOfme2AfX79voZ048n6I2WXqucv76BaFFIeADZppAHDHBdPrgFkwEJaWB3RuqMYLDXhgpoBl8Vhij2KGzjzPi8V6qP8ehxXqDSOftja47q7Jx5vVisUYJQUp99KdcWBNVWdJPb97PPLcJ3V4Ypf3h3j6eOpNMRNire_i-Cb0nBUm1iiGSpqCHDnlucOo23hQoCztCio388TwxVrH5axb42qkJdhBZwp8weG9KwgtbrhRLkz3IKLoROw5OifjfgB8hQ6p7-UfzsL8LxglzCBGOWB2alTOTm_84zbUITxW0afuT-TUTIl20xfzh3CTbf2Yq3f8GbnAdV2fm3eXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الدخان يتصاعد بكثافة فوق القاعدة رغم المحاولات المكثفة للدفاعات الجوية لاعتراض الصواريخ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86356" target="_blank">📅 08:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86355">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86355" target="_blank">📅 08:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86354">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378eb493eb.mp4?token=PgkFz4LtxAqd5hawsmezsQ2eS0ORVRcVxtoyikPFASRSCZ6BdnL5h-cR8hy5H-NrSuwKoO9fflcU20kCtKkHXtBKr-ugls4i9Wq2teBEL9-Q167Yhbb2nk7NmJPCOJ0bxBuP_XXXHpf-RfMD25axvkoZnaH836QXoy6cYUw_XWTLpiVo0o1HjS-fliFUV_aNTtHcE-mcYCjVX1jkv80lSnDLrVFUIYLRIpcU5mY-CKaRJzcPqo3zZStghWZtYalV0kYIpMuqSAx7PyvoEt_o_jiPDscRHWm4Y7MpKcxa6shZxARxDuC43Mf0KAl1qMZG-pkD5Oe9NJyxT5VVUiX6DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378eb493eb.mp4?token=PgkFz4LtxAqd5hawsmezsQ2eS0ORVRcVxtoyikPFASRSCZ6BdnL5h-cR8hy5H-NrSuwKoO9fflcU20kCtKkHXtBKr-ugls4i9Wq2teBEL9-Q167Yhbb2nk7NmJPCOJ0bxBuP_XXXHpf-RfMD25axvkoZnaH836QXoy6cYUw_XWTLpiVo0o1HjS-fliFUV_aNTtHcE-mcYCjVX1jkv80lSnDLrVFUIYLRIpcU5mY-CKaRJzcPqo3zZStghWZtYalV0kYIpMuqSAx7PyvoEt_o_jiPDscRHWm4Y7MpKcxa6shZxARxDuC43Mf0KAl1qMZG-pkD5Oe9NJyxT5VVUiX6DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد للاطلاق الصاروخي الإيراني المكثف الذي يدك معاقل الاحتلال الأمريكي في الأردن</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86354" target="_blank">📅 07:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86353">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/86353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86353" target="_blank">📅 07:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86352">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8ZwXR5TRxkZkaMjIVz7BwQSQ0PkiEE7pyJGpOzWDJQaZONVsuc4MOpHtE8UucHS9mF7JSJrNxEUIgD5IrN3VzwEDIC-KSdBK9n1x08a89D9cwbP0Rcijj-qc9sY12i_sF08vhIry4fjm2CgboePm2dICd7DpvtNACJXqPvexycKoa7jnxoGHcgbuBDnZG-IhRSwx7yEHjWf19Jb3NHZ8kwi8S2p-SsI7tW6KQhyoXFDtwCdi-0wWlerK5ZlFJWg1iTOaBEf8aPcOHVOnSoittv5qfyUfrHqkto6ktLpvFYv2nMhcdtRUKjoWOhaYaQouIX0oRG1dxtev65tCD8EEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الدخان يتصاعد بكثافة فوق القاعدة رغم المحاولات المكثفة للدفاعات الجوية لاعتراض الصواريخ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86352" target="_blank">📅 07:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86351">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86351" target="_blank">📅 07:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86350">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyLKM9ZxUw-wLflPRm_QDUfKX6lNST2m8Fzm20UKIJOeDfNn7SVGrC9HRHaI1PsxCjIiiwlNJXVXVF6g5gHiGg0WLdnvBBVui5qKXsvu1CL8I8SY52u0ONoWxMUMcpEj5nb8OaT6GVV_trIUg3KTaIPCk0jFwBDHvYcXNoZrhJf7T3HejwB_M-minzlTbLSnXBSB37JF71zeRtW_79VFnkBS6uT5V47XyuG3j8L8_iEwQdtdafbx6X5TsWp2j2fesarh3viRS1uf-P0A8Y6wl_helvl8Zs_TFirXLD_E2jUIItGPFpdl6vJtXMd4Lbn7pIlK3b1Ew7zvZiJPBHLdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86350" target="_blank">📅 07:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86349">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QILDjTfQUmI2tZd8X0v6VdFImr4DV41paWaMrsbimR2Xv-sFlhdslEJl7YPwhl4sYMjSUMJpsJxJLfxY1Y5Z_GQvkC2vMni_erZy416k3uXLngBl54wdqQ8Yrl2NZ8oMKozbiCTF2EAWue5DWDok41Pwai-BmbqBnQJNqBkyHF63MZY9KrKLMv3kZvVcDaEKeBxfvOJRDQRA802pHazYdp1gsSGBFPiC0_6gn8oPeW9JY3TcRes79t6mU5BoSrKIGmpJKbtQW1DHF6VDW3t7YONMYwfQeh4xn4EyaCNTzP3AmMrp-DDPWoh8CLJZHUtxbedE06NRXr1It0_HNC3rzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجات صاروخية مكثفة تنطلق من إيران</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/86349" target="_blank">📅 07:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86348">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfb4b4712.mp4?token=aIAfEiwcvgjsqUTs51PrZVxDd6eVB4SxDrPwc8Uwdss1nTC9KgketLZ1F5ILs3afjf3JPe9frchvGi1ilbcsA-qe39qKqaHI1ch2KUNhPcoCKnGIRJ-JquGKfu09QqOabmI_7n_khZASeCDqVlExx9x-Bbqvd9nKI3iCRuv92jWFahUfCYBHQVmgPrZ7l4rHlEmuTesy30C260jILiJAhi0yknXoOjiNpDVez8Wdj_HJX4bSy2jkBfTqRc4Zz3a2tGf-jxmcgDqjojYoAJp_ljuitmoAmQMBCHzhjUEeTCGsAjOaKxvgdGZHA_wJpizvdlSi1iuhb55Izone7f7AOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfb4b4712.mp4?token=aIAfEiwcvgjsqUTs51PrZVxDd6eVB4SxDrPwc8Uwdss1nTC9KgketLZ1F5ILs3afjf3JPe9frchvGi1ilbcsA-qe39qKqaHI1ch2KUNhPcoCKnGIRJ-JquGKfu09QqOabmI_7n_khZASeCDqVlExx9x-Bbqvd9nKI3iCRuv92jWFahUfCYBHQVmgPrZ7l4rHlEmuTesy30C260jILiJAhi0yknXoOjiNpDVez8Wdj_HJX4bSy2jkBfTqRc4Zz3a2tGf-jxmcgDqjojYoAJp_ljuitmoAmQMBCHzhjUEeTCGsAjOaKxvgdGZHA_wJpizvdlSi1iuhb55Izone7f7AOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الاردن بعد تعرضها لموجة صاروخية كبيرة استهدفت قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86348" target="_blank">📅 07:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86347">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad1427d80.mp4?token=Tsta2mfvWg6wIf_2aop_o1rvpn8ScfIiqK1M-03fgFp8_8xpES7r8lXm4oRpXShO0-v8ajD0ZTfn4zWcQzlmtL7hCiKuw8vyvi62OHeu9XJKC0ke-7CXvNOjMfOdMxN3Nbr_avcagrt6jCGDkugVJmWeh0rjnqmz7oQxT6hSNKdwUavP6Mf54Uq1iq3wulc4t-T8-vX8G8vjcFjvKkJ-QE2rzK4F6C9lSnvCHl_Yo1QlH1uGv4dlOo-oCyFp1_9llg5AD0GSf829komq-K3b29HGdIZcvycrYKpcEAJeKdvfdC-kDSROBgPclb-Zoa6wTDuheiTEofzsI1nMCU3kJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad1427d80.mp4?token=Tsta2mfvWg6wIf_2aop_o1rvpn8ScfIiqK1M-03fgFp8_8xpES7r8lXm4oRpXShO0-v8ajD0ZTfn4zWcQzlmtL7hCiKuw8vyvi62OHeu9XJKC0ke-7CXvNOjMfOdMxN3Nbr_avcagrt6jCGDkugVJmWeh0rjnqmz7oQxT6hSNKdwUavP6Mf54Uq1iq3wulc4t-T8-vX8G8vjcFjvKkJ-QE2rzK4F6C9lSnvCHl_Yo1QlH1uGv4dlOo-oCyFp1_9llg5AD0GSf829komq-K3b29HGdIZcvycrYKpcEAJeKdvfdC-kDSROBgPclb-Zoa6wTDuheiTEofzsI1nMCU3kJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لمرور الصواريخ الإيرانية في سماء المنطقة قبل وصولها إلى شرق الأردن</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86347" target="_blank">📅 07:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86346">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارات تهز قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/86346" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86345">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86345" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86344">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBul0XeKidtJnUXlGbBRlaE0Ho-UxZ6R7arlYL1XGDuIsxAIggWtdguI5Dm3xD1MRLf8q4qUwYI1CwUL3_-8zd2UuEzlmWSUkZmXNjAu42vOu_N-9OzwjQDMF5W7_g4j6B8TOShXlZ73Q7qp9deZko_nHl7B5c0yWsE_JTjv_5ZhDnUW1HCG3KNmGTSKd0wYb25KdEi2LA8STQQqkQwUQBxwqdSNia7ETjDYiPkahBGufADxKhD1pB68cRN79GXA8DCfOFFFa7gxs3C54Jldqoyf0oq1S_KWY-RHOryFWAEcA0GFtObXwAC6WxEMUzcIH1CP3j1S10N36N-8zbQOyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد لمرور الصواريخ الإيرانية في سماء المنطقة قبل وصولها إلى شرق الأردن</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86344" target="_blank">📅 07:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86343">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/86343" target="_blank">📅 07:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86342">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/86342" target="_blank">📅 07:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86341">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-EKwB_RyHxJ5p0WrQ2ACucNKYFZ9AWARvlfhxeZpWhB39R3qH-HDIe0szoRjJjeqCauITtfCSim8CCSOwK5P97IpuRedSZijCSJvUVWX358jXi5L5UNix6wH260eZ9PzWdbNvlc8YdRVnbNHjTTROo5g_d6MpQI36pE2NjtEzTpcPBbliOS_DrjCOwuvRajKyBlMx2kQQNPiqChFWVlWN8kL0wQVozhI-BFze-_zbVP3vkGAzXYEm2ZYqI08eJjxn4PD6OE9bd0VuxZ-s1_D9o_x5CS0Mi3USD85BmQH16km5CfD8Wzut3f6g9z1KBaKtKiOfrMlXSQLcEy9VlcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ في طريقها لدك معاقل الاحتلال</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86341" target="_blank">📅 07:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86340">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MarOp84CxbmI9bygcxlB7UNSG-e159cOXXabRdpVFHxWx-hTR1lvxqN9KSgQVhghRZTTAiL5zMZ4v7YtCyj838ryi1Vn5fNtpLyrw49duvB92o6phjlzAWoZd1Y9-qHYWvzR_ITvWWME-_KdRwccLyDyAn5Euwp9Ql6iebpUUnqQ47VP_L7LzmnWgbY0Q7qEhlRCLa0ak-lHnoUFBqLtUIDDnQUmORFQurKpmik9mhCD9YVK4OS-bf1Z6mC_QnGZ6-5GCj-gupX7WTKNiXE3L1PKOkrVNFww1SIvPuOMQYZkz21-n4HsMU4cLLUEChPpbr39ouolRVoY3GRdt58wog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ في طريقها لدك معاقل الاحتلال</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86340" target="_blank">📅 07:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86339">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86339" target="_blank">📅 07:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86338">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">إطلاق صواريخ من إيران باتجاه معاقل الاحتلال الأمريكي في المنطقة</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/86338" target="_blank">📅 07:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86337">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5367294f98.mp4?token=v2A0RSgG64J6dtMChFG_Ik1NNKz-CKaviKdGJ61iFVbJ8CWXBUQtfY98eVsuKcseGcEaN_07VF2za_zQDSMOQcKAjGx-vUHg1ynNGCHRIlUuKeZuFmkKU6N7dhuXnCVY5D4DHZfb8bz0r6n2Ha0TykO5503NgekRYYwyLmPbiI5erjvuURlNaYnVwG42WOVEyhrxumdoPrY6vkWabcNbHK_ygf8Q9T-DipXXb2ROFlXQ6uVmqQTwE9V_PDlFOkibJuS4gfTssuScjSe9m5X7cu72L3L7TJK-ZNhny1TVyrWTh95zr30j9XMe9ygwg7k2ik3TgYDaCGejeFhDNAAO0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5367294f98.mp4?token=v2A0RSgG64J6dtMChFG_Ik1NNKz-CKaviKdGJ61iFVbJ8CWXBUQtfY98eVsuKcseGcEaN_07VF2za_zQDSMOQcKAjGx-vUHg1ynNGCHRIlUuKeZuFmkKU6N7dhuXnCVY5D4DHZfb8bz0r6n2Ha0TykO5503NgekRYYwyLmPbiI5erjvuURlNaYnVwG42WOVEyhrxumdoPrY6vkWabcNbHK_ygf8Q9T-DipXXb2ROFlXQ6uVmqQTwE9V_PDlFOkibJuS4gfTssuScjSe9m5X7cu72L3L7TJK-ZNhny1TVyrWTh95zr30j9XMe9ygwg7k2ik3TgYDaCGejeFhDNAAO0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طيران حربي مكثف في سماء محافظة ديالى العراقية</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/86337" target="_blank">📅 07:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86336">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bedb34f2c1.mp4?token=NQ3hRmDftBeugvAMCrDDioFCbDb39T4RoO1uwTl7kc5cvlXveb9bYQyITRL-pvj8UU-hXz_ppjDPaHjVyFhjOX4k0ttYwNkiCebtvL_-hQ3F9bVzoYMTmaC3hgSIkiED0xpdCU3pOVNFkr0L5NpnKhTGDvaqvgYtdXXYfKjO7pc_xtDR6T9HkMqEMsloQqqQc9YoHhfoq9eApUJVQ0gQH8MblcMmOPuLFa7XtENKEFnpWd75wVQEWN_QUrLK6c1dAmGOexSfTKeICw_pUQItDw2VEfZNmlPmnN6qrd-ULHLdQ3k7mjyIJGhdxwQxN7msrAx-ZRTCOk0KXYbw_Sim0oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bedb34f2c1.mp4?token=NQ3hRmDftBeugvAMCrDDioFCbDb39T4RoO1uwTl7kc5cvlXveb9bYQyITRL-pvj8UU-hXz_ppjDPaHjVyFhjOX4k0ttYwNkiCebtvL_-hQ3F9bVzoYMTmaC3hgSIkiED0xpdCU3pOVNFkr0L5NpnKhTGDvaqvgYtdXXYfKjO7pc_xtDR6T9HkMqEMsloQqqQc9YoHhfoq9eApUJVQ0gQH8MblcMmOPuLFa7XtENKEFnpWd75wVQEWN_QUrLK6c1dAmGOexSfTKeICw_pUQItDw2VEfZNmlPmnN6qrd-ULHLdQ3k7mjyIJGhdxwQxN7msrAx-ZRTCOk0KXYbw_Sim0oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇱
نتنياهو حول إيران:
لا أعرف ما إذا كانت الدبلوماسية غير واردة، ولكنني متشكك في طريقة عمل إيران.
إنهم يكذبون دائمًا، ويغشون دائمًا، ودائمًا ما يماطلون.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/86336" target="_blank">📅 07:14 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

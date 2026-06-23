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
<img src="https://cdn4.telesco.pe/file/aUlw272PviX1H-pB8w0jFzxeNN3LbgL3FudI0gP3q7H0VvOIv9hVtC0exvEFFHNVP7XcjHal1j2g-Qc7sG3n9gdmpiXuQTvjA8Dy28N0yaEP3CQwgtB4TjcBoyZ9VW3efQRF3NdBbnM08wvfC5dxs82fEF7jlbL5P9nJrONToSydsy0r13Y2_-7Vsn7OHDyWAUaLjJ6foObcHrpXVsuhf6xhq3TK0SpLRqec9jWada4RRsMFyNVJRX1Yf66WRoiY0GumL6n0iGXN677kZsQnitGDz1-amaWhpo2PV7Zzb_i-fYXCUArHDSvsoqpMrNM8DPCYT1Db2MzhGEE5e-rFQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 15:06:33</div>
<hr>

<div class="tg-post" id="msg-79723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDw6MEZMw3tBMwkICziR9AApDi_FyXwWpNEF5HFixo57ZFhuDgeuqOJ0tP5Z9QMlt-HU-dJZX7hQhBu7LfGcXrgj6hY_zK3o_9rGvP1UB1aMwPMDonPu0l16UsSJo8xqOFtdIUYBrT0DK5mkwNdgXs1EMr06yr2jV8F8_LNx4ZOng9fIWgXeeXXWTX0JGhnzAYOWjOilmP50m2Zf-LN4yQ6Ll693IM4aqeiKnU0Qf_VdUAL59zzft_BOKr2luoQGvXSdKynEHI_cC1_Uzas8-wtLOAQcoZ7f3Q5BuNX0uD0K9wICxV3YEj8VUIKgTg4kljU8dgqUgnaY_mLhT6eKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
تدفقت 19 مليون برميل من النفط من مضيق هرمز أمس، وهو رقم قياسي غير مسبوق. أسعار النفط تتراجع، والعالم مكان أكثر أمانًا بكثير!!!</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/naya_foriraq/79723" target="_blank">📅 14:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuZ47fo0jFEZgB2bsNzLT6t9ojJy35OYdbfDrbXxb-Wtpp2iyRRmGDum23Q1k_LEcDKNQkuKFrwcJGgYZMGxXJPPem8xzttMVHr12etQQ0UGZp8wL-qFpo3ga-DQ4Ask4leCwJ6tcYdyGOhgVJnBJciQOQMzIzjjCRCGYji-ok-hvyhNedtnlEejcyNcsGX1mXFJwyLUjgt1_emhy60pMSa4J8U9ItNCoLvXbzj4FwptPnfWmyFYwIOOmDj_MRXohvWp4UUTPCA8gjJDN3VVq3N1O5RChoDxQbxBMv8le3c8CQxW-J2-8TA3J0eZkHTfj7b3J3SXDDJnT1lcLz7WMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
على الرغم من احتجاجاتهم وتصريحاتهم الكاذبة المخالفة، بالإضافة إلى حملة التضليل الإعلامي التي تبذل قصارى جهدها لتهميش انتصار الولايات المتحدة، فقد وافقت إيران بشكل كامل ونهائي على أعلى مستويات التفتيش النووي لفترة طويلة (إلى ما لا نهاية!). هذا سيضمن "الشفافية النووية". لو لم يوافقوا على ذلك، لما كانت هناك مفاوضات أخرى! بناءً على هذا، وعلى تنازلات أخرى كبيرة قدمتها إيران، وافقتُ على إبقاء مضيق هرمز مفتوحًا، دون فرض حصار بحري إضافي. مع ذلك، ستبقى جميع السفن في مواقعها تحسبًا لإعادة فرض الحصار، وهو أمر يبدو مستبعدًا للغاية في هذه المرحلة. الأموال و/أو العقوبات التي تُفرج عنها وزارة الخزانة الأمريكية تُودع في حساب ضمان تحت سيطرة الولايات المتحدة، وستُستخدم لشراء المواد الغذائية والإمدادات الطبية، حصريًا من الولايات المتحدة، بما في ذلك الذرة والقمح وفول الصويا من مزارعينا الأمريكيين العظماء. هذه مواد تحتاجها إيران بشدة." هذه أزمة إنسانية، وأشعر بضرورة تقديم المساعدة الآن، قبل فوات الأوان. المحادثات تسير على ما يرام! شكرًا لاهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/naya_foriraq/79722" target="_blank">📅 14:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79720">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0_dLzNfo9MewEj2XRgLcZUzZgTB8Qyisw2ITvZy0XG9lPvzPQFSG9lndBdLLmG6e_urXoD05d-crWGC--6dxCE_-9atAm4U6rZzavRDVcqdwzLYYJq06rex2A9a8i2QUXlEoYKfoDTXuLexmBKJWlyzmLzqH4q8jONJgIoaLKnH5fppxx1hqMscoAtZamyJNZqW4GCYQfEM5GV5QjE--1Vyq_lw55QtlZ6t2RzfzF1y7FtMLgNZ4sIdPowGUm_F-x2srnFk0B-JxydG6bXVAIQalEeskKDgMA-EDWWLjfGqTFtGXAaIQXyffMyxzLRUlfHZaXdgBxdp-qEYzLvI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtvpyarfGmhQTOoixCKxvVjgxQxt8AwtNXyI1hIwpNO_212pgmvHPYawfc-lMYhPY-nzeu-rrvx-9vr9mp8h3dCj_H7uxvMiGwFAWE-1mgrYA74h_r2hSlOS-IF_nGJYnOkfseVDWoFIFnOeZrNpYJ395L0Mi0cPiHSTkEpU_Ne4S9kVAlBPJ-Wo65M1VeG1VxtS4JGMDtVOPW3VM8rkC5fD3whd-MJLhyQSegRtfHB9jsyZ99L2a2eNF_2pjS0t4e4bsZX5AENyG-a6bF_kjnYwaKNM4lFWPAjNlrACGuHduvNChI7pu0t2ij3qc6o80HmBszVBFnurNR6SCcvJuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفينة تجارية سورية تتعرض لقصف في ميناء أوديسا الأوكراني ما أدى الى مقتل كامل طاقمها</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/naya_foriraq/79720" target="_blank">📅 14:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79719">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
🌟
بيان مشترك ببن الجمهورية الاسلامية الايرانية وسلطنة عمان حول مضيق هرمز:
- أكدت سلطنة عُمان وجمهورية إيران الإسلامية بوصفهما الدولتين الساحليتين المطلتين على مضيق هرمز التزامهما بضمان المرور الآمن عبر المضيق وفقًا لأحكام القانون الدولي ذات الصلة، مع التأكيد على سيادتهما وحقوقهما السيادية على مياههما الإقليمية في مضيق هرمز.
- اتفق الجانبان على مواصلة الحوار حول هذه المسألة من خلال فريق عمل مشترك بين وزارتي خارجية البلدين، بهدف التوصل إلى اتفاق بشأن إدارة الملاحة في مضيق هرمز مستقبلًا، والخدمات المقدمة في هذا الشأن، والتكاليف المرتبطة بها، وفقًا للمعايير الدولية.
- اتفق الجانبان أيضًا على إجراء مباحثات مع الدول الساحلية في المنطقة ومع أي جهات أخرى ذات صلة.
- اكد الجانبان على ضرورة أن تحترم جميع الترتيبات المتعلقة بمضيق هرمز سيادة الدولتين المطلتين على المضيق وحقوقهما السيادية احترامًا كاملًا.
- جددت سلطنة عمان والجمهورية الإسلامية الإيرانية التزامهما بالحفاظ على مضيق هرمز كممر مائي آمن ومفتوح للملاحة الدولية، وأكدتا أهمية استمرار التعاون لتعزيز السلامة البحرية وحرية الملاحة والاستقرار الإقليمي.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/naya_foriraq/79719" target="_blank">📅 14:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79718">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlgPJb-DmeqrvJE0ffAoDzBjBONgkRvU3O7qbv7qXTVox7UGvIMAuGwGOurlVcUVD8Oo0KZlhilSKCmrdLjvZmjhpfvx2kLuTTuG-ebRGtqfiApC4LbOVMUcrfDYl3Vcvvkxa_g6_okrgHdHdVH9LYG4nZnQ0fNlhdux5BwY8Pm_xOVU8TbhmvB42WB78sqk7DLKdSMkeWMF4-1G8vEZt3u_FDy8A0HDuERIDdAIBZ_6qNrvoTw8qi-7N0VJjBeyFqYL1tW6DhopxzUjouNtLsMA4rwx_iX30WPrb-T1hjudKLEXCAzKifj9aU9UGjby2eia4ZJhnhl3lcqDRAyTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مواطنون يناشدون أهل الرحم بضرورة حصر السلاح المنفلت داخل المكاتب الحكومية
نعم نعم للإصلاح</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/naya_foriraq/79718" target="_blank">📅 14:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79717">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">محافظة النجف الأشرف تقرر تعطيل الدوام الرسمي يوم غد الاربعاء باستقناء الدوائر الامنية والخدمية والامتحانات الوزارية للصف السادس العلمي والأدبي والمهني.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/naya_foriraq/79717" target="_blank">📅 14:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79716">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtFG7r6OoWdCWbyQUKBcWW3pgHvO7-BNqBCB6A6h6oLF4uCDTDTpB9lOZsBbJbtAQR1xPV2hYYsxKWYOEyFO7-pu6Ob2Gc7lzqYGtBpzkLLrFE8pmC2n1iA4k34aO-JzTVkjKO4IIQRWORxoRFZS73hGQxsel2b6riHpEszBRczo_hg7WD4S2LoSJx3t7bXK_ReKg-roM7GVPiplpDi4c3lSx_NvmQLyxK2pEdRiI1D6iLdmhmPbkjXLlCpcFFo1hyiWZM1_wIxfyHXPHp2wct-qQm7VrdaLlUv5Qb1zZAitJXJGUQn3_1XrnY-ok7ktiCX375NBd4QRIgcEg9BjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الاتصالات العراقي مصطفى سند يعلن اعادة القضاء العراقي 85 مليار دينار كانت مختلسة الى حساب وزارة الاتصالات.</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/naya_foriraq/79716" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79715">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eh8LRPkvEpmi1mQVh7YK2pILCNmm6T8rNKXNaqXFwwZUlx4jJx1KdYVVVTNeRMHen6Urul5MvtRzZqnsmlQhbLXVkSGguCaJ3qdHfc-ned6MWaVGVlZ8pZP-uf4Rc6b2qN4DYTCjhzJ26SLe6onGpt7l0TtrM_gEmlolqjGBHUT6ql9Ho4DVwQO31ltv9UU0z5MBDiEo_vO7BYzIodtOoOPPmPQ3k-w2-oiwFs1Nb6BfnRUUDsUdVoTj6JdpAeMKNrHg7RbB4LLr2801j1IMmCZa2wnAjtWE2GcDTl4irgcBQ02jIDKJVrGKn0-cMvJGzfJl6GOIwPxaVGmv0wZvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
‏وصول الرئيس الإيراني إلى باكستان</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/naya_foriraq/79715" target="_blank">📅 13:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79714">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
مجلس القضاء الأعلى العراقي:
ما تم نشره في موقع (قناة الدولة الفضائية) التي تزعم رصد مجلس القضاء الأعلى (65 زيارة) للمتهم الموقوف وكيل وزير النفط لشؤون التصفية (عدنان الجميلي) من قبل مسؤولين ووزراء ونواب وقادة فصائل ومديرين عامين ورجال أعمال هي معلومات غير صحيحة لا علاقة للقضاء بها</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/naya_foriraq/79714" target="_blank">📅 13:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79713">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌟
وزارة العدل العراقية:
رد دعوى قضائية بقرار صادر من المحكمة الاتحادية العليا الأمريكية وتجنب العراق دفع 53 مليون دولار ضد شركات أردنية.</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/naya_foriraq/79713" target="_blank">📅 13:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79712">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌟
وزارة التربية العراقية:
اعلان نتائج الثالث المتوسط الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/naya_foriraq/79712" target="_blank">📅 13:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79708">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هيئة النزاهة العراقية: الحبس الشديد خمس سنوات بحق يزن مشعان الجبوري لاقترافه جريمة النصب والاحتيال، المدان أوهم مُشتكياً بقدرته على ترتيب لقاء مع رئيس الوزراء واستولى على (41) مليار دينار</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/naya_foriraq/79708" target="_blank">📅 13:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79707">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
🔻
🇮🇷
مصادر إعلامية:
وزير الخارجية الإيراني عباس عراقجي يزور بغداد يوم الأحد المقبل</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/79707" target="_blank">📅 12:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79706">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
منصة كبلر للملاحة البحرية: 36 سفينة عبرت مضيق هرمز أمس في أعلى معدل حركة يشهدها المضيق منذ أول مارس</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79706" target="_blank">📅 12:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79705">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
الرقابة النووية: العراق مؤهل لإنشاء محطات نووية لإنتاج الطاقة الكهربائية</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/79705" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79704">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc16091f2.mp4?token=im_jTq2FIWLrbXkOGHlw9dIW16N674TPqUO8GcdRBi2zOdH_x1V2HMw75zkhRsJ3a_xuQiDo5zqXh1aa6-rolHL9FnUJB6DDtnt5lbIW1pfRlnQJo4cMrYqRQK3TxGSS8RjloF5Mk4c8KU7cxZcNiiIUisEvq-5-qg6QkeAIqSamNJelFX1Zdmg9msR7QXGMGG1s3b-PRFiKdbAgXQlRiQrTmVhfvgT3JZ0kLc-vYI5mZi_XUcx6IKKVf-1sJJIZ7jKu8laXdrNtdKLItM_7c4lywjK3m6qLQ9z9TuU4tB3rETOvgwY_TLGB4R76_lHHvODHgOtVc-RCkMiLwxYQmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc16091f2.mp4?token=im_jTq2FIWLrbXkOGHlw9dIW16N674TPqUO8GcdRBi2zOdH_x1V2HMw75zkhRsJ3a_xuQiDo5zqXh1aa6-rolHL9FnUJB6DDtnt5lbIW1pfRlnQJo4cMrYqRQK3TxGSS8RjloF5Mk4c8KU7cxZcNiiIUisEvq-5-qg6QkeAIqSamNJelFX1Zdmg9msR7QXGMGG1s3b-PRFiKdbAgXQlRiQrTmVhfvgT3JZ0kLc-vYI5mZi_XUcx6IKKVf-1sJJIZ7jKu8laXdrNtdKLItM_7c4lywjK3m6qLQ9z9TuU4tB3rETOvgwY_TLGB4R76_lHHvODHgOtVc-RCkMiLwxYQmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بن غفير حول قتال سوريا ضد حزب الله: لا سمح الله. هذا شر يحل محل شر آخر ؛ جلب داعـSh بالقرب من حدودنا - وهو داعـSh حقيقي اغتصب الناس وقتلهم وذبحهم - هو تهور تام.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79704" target="_blank">📅 11:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79703">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o46sIrN0FarfRC3lxGF7EzMeF_rzsKLcCX-wGzjSFjM2SZ4bklI4WlhjdxxB_WC8S7zJoFnUecQBA9pXgXNbktctBm_Tf6fX6Yct4m51RnuwoCnJQ3_ZKo07LJsryCsR93nOUhdSEPxoNry8yY9PY3TKLMSZ40dH05BV00MDcMIV04xOAuB8lAUiJC0nGxM3gKXibCuDwbYSimvu6UWBnKHUqvdsIBAZYCu_OFx1kiMfvntnYrhZ7TCsATQb-T-b9iuAjJuqlF2ROtTuVP8EhNPX3Bxij1i-hXCCfG61jxd3qvUCyuNmM7-wAQzrAeuu2RWiHOP6N4wUBBJaCD5yeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الموقع الرسمي لنادي ريال مدريد يثخن ويتشمت بالعراق بعد تسديد مهاجمه ممبابي على العراق وفوز فريقه الفرنسي ليلة البارحة على منتخبنا الوطني …</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79703" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79702">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
لم نجر أي لقاء مع مدير الوكالة الذرية في سويسرا ولا خطط لتفتيش منشآتنا النووية التي قصفت ولا ننوي السماح لمفتشي الوكالة الدولية الذرية بزيارة المواقع النووية
الأموال الإيرانية المحررة نحن من سنتخذ القرار حول صرفها ولا قيود في هذا الإطار
إيران تحاول المضي قدماً لتحقيق أهدافها
الالتزام بوقف الحرب في لبنان جزء من مذكرة التفاهم والولايات المتحدة تعهدت بذلك
سوف يتم التفاهم على مزيد من التفاصيل في الأيام المقبلة</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79702" target="_blank">📅 11:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79701">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏴‍☠️
إذاعة الجيش الإسرائيلي: عدم انسحابنا من لبنان يشمل منطقة الشقيف حتى تفكيك حزب الله بالكامل
يعني عنجد رح تفككوه
😄</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79701" target="_blank">📅 10:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79700">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42f7ae6a5.mp4?token=LbOlVS4yPkV7eGHILizF759Nn9lFLspDX_JzZFpzbHE2mIgQ_kIQYyiNOLj30DZqeaKWUsQ7SRyv7umX_pAKNqHwpdEyYj_pTExgNaJq__wMw3gpjpQY7ehTIyJOPXAMFsiLmKUcJK5OVhgnDZzhntJhMS8AK3dbMvjR3jRE0KoAVEC2IZhWr_sxn9O4WDoa3Xa7bVRQmINZhk9RJYUPVa_YPgitmOAVBjBOPVM5tL-ewSt1kXzLev-ybuGgPHT5-gR3nwXdk_NxR4dnuT5aC3jfiHic9LzvNkjzxijql9fIZUEEr1c1EaF-KHNDc0j2YQX8nV0Cl46vbAibl8qdRRuY_4Z5VbgLdX4HS7WZM03cIsPvphitdPAHAsvHaxYdFsNbQjuxRq24wnUVZnvssPbQpwRPcXKCeOfExBPL3qUr6hKbOgqnNd3cpyoJWTJq6EwXDPdHJlI-S1Zz3WwFgSLomyad0YGsIQWWE7BQlSgVhOynunxUlZdqzIrAx3LiY1mI8tQhvFJuLKLz2jZXsnLVqDLGLAvQBljafKaEeGmT62kel6KtX9AomzXVSPpZ1sJT2-G5ygHea8IGdGHvOc3BUGi_-PivPcFWJR_fUevZNoQFol5cUSITYn82xt3Ov3jciosLpnN2SCR8lgtWh78B5-_YphLyACZAfGryWdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42f7ae6a5.mp4?token=LbOlVS4yPkV7eGHILizF759Nn9lFLspDX_JzZFpzbHE2mIgQ_kIQYyiNOLj30DZqeaKWUsQ7SRyv7umX_pAKNqHwpdEyYj_pTExgNaJq__wMw3gpjpQY7ehTIyJOPXAMFsiLmKUcJK5OVhgnDZzhntJhMS8AK3dbMvjR3jRE0KoAVEC2IZhWr_sxn9O4WDoa3Xa7bVRQmINZhk9RJYUPVa_YPgitmOAVBjBOPVM5tL-ewSt1kXzLev-ybuGgPHT5-gR3nwXdk_NxR4dnuT5aC3jfiHic9LzvNkjzxijql9fIZUEEr1c1EaF-KHNDc0j2YQX8nV0Cl46vbAibl8qdRRuY_4Z5VbgLdX4HS7WZM03cIsPvphitdPAHAsvHaxYdFsNbQjuxRq24wnUVZnvssPbQpwRPcXKCeOfExBPL3qUr6hKbOgqnNd3cpyoJWTJq6EwXDPdHJlI-S1Zz3WwFgSLomyad0YGsIQWWE7BQlSgVhOynunxUlZdqzIrAx3LiY1mI8tQhvFJuLKLz2jZXsnLVqDLGLAvQBljafKaEeGmT62kel6KtX9AomzXVSPpZ1sJT2-G5ygHea8IGdGHvOc3BUGi_-PivPcFWJR_fUevZNoQFol5cUSITYn82xt3Ov3jciosLpnN2SCR8lgtWh78B5-_YphLyACZAfGryWdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇶
محافظة الناصرية تحيي ذكرى استشهاد أبي الفضل العباس عليه السلام.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79700" target="_blank">📅 09:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79697">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هدف ثالث للمنتخب الفرنسي</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79697" target="_blank">📅 04:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79696">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هدف ثاني للمنتخب فرنسي</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/79696" target="_blank">📅 03:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79695">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هدف أول للمنتخب الفرنسي</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/79695" target="_blank">📅 03:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
🇫🇷
المباراة تستأنف الساعة 03:00 فجراً بتوقيت بغداد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79694" target="_blank">📅 03:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79693">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
الشوط الثاني لمباراة منتخبنا الوطني ونظيره الفرنسي سيتم استئنافه عند الساعة 2:50.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/79693" target="_blank">📅 03:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03589363ac.mp4?token=I67sjcFcNAWxbsiSsnIRw3RChcx4Av_YJWBpgkdObd04wDd2ZQGemANkZK8ORBwu11th128dBNxiG9Q-NqHH8olBAu5gljU_-DoI598qsXM2ltueA3ys_-eSfB_gIhwbcb-Wm2_o6tK7I4h2G6aCA8_ZgXezv9aJT4ZvtVE9iosMBntkBYGbcMdyaDtcvoeHRM24eHAKcI1g5ed1YTN6_xqIQB9R5vRPphxHQOyV6rOrusSC9oDQhGmgzQG90o9HDHb6LLnIud-09SgGFDWFvzDSMsgixMrdBPRcQe_hcqBW4n6QR8aXBo1L_qDqn_5PNZZQnzv8a-SFDJL63ut0gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03589363ac.mp4?token=I67sjcFcNAWxbsiSsnIRw3RChcx4Av_YJWBpgkdObd04wDd2ZQGemANkZK8ORBwu11th128dBNxiG9Q-NqHH8olBAu5gljU_-DoI598qsXM2ltueA3ys_-eSfB_gIhwbcb-Wm2_o6tK7I4h2G6aCA8_ZgXezv9aJT4ZvtVE9iosMBntkBYGbcMdyaDtcvoeHRM24eHAKcI1g5ed1YTN6_xqIQB9R5vRPphxHQOyV6rOrusSC9oDQhGmgzQG90o9HDHb6LLnIud-09SgGFDWFvzDSMsgixMrdBPRcQe_hcqBW4n6QR8aXBo1L_qDqn_5PNZZQnzv8a-SFDJL63ut0gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇫🇷
تحضيرات لدخول لاعبي المنتخبين إلى أرضية الملعب من أجل إجراء عمليات الإحماء قبل انطلاق المباراة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/79692" target="_blank">📅 03:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9f786227.mp4?token=ccYohgKdKgwFxfRMsytPESICbzSK7RztYJmUjeq7RTKnB5qAPDD_hdUs6krPrR4XpnFCD_-j7P_NUJjWYPq_ajsvyZ07KCEJqckkK81VItA3G7dnwWhARBtn3ohvHmjj6BY6kvTu5RduEBbThaRhUI4iLZL97ygL2TaNYKlb_GM6Co13dlJyaa2-eXohBHNh_-NFLepeWkC5CTxm6iQ54W0Z_-z7fnMpABnpaJUaSeSu-QJqmWIXh1n2sB_ZSF0WOnpV6KdYy2UDchjUa3TZP8NWCAJEe-dCRjwi3C03VPRWgprf3oDSv3OSVf_ykV-JkojpGleshTrCU5GW1XpktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9f786227.mp4?token=ccYohgKdKgwFxfRMsytPESICbzSK7RztYJmUjeq7RTKnB5qAPDD_hdUs6krPrR4XpnFCD_-j7P_NUJjWYPq_ajsvyZ07KCEJqckkK81VItA3G7dnwWhARBtn3ohvHmjj6BY6kvTu5RduEBbThaRhUI4iLZL97ygL2TaNYKlb_GM6Co13dlJyaa2-eXohBHNh_-NFLepeWkC5CTxm6iQ54W0Z_-z7fnMpABnpaJUaSeSu-QJqmWIXh1n2sB_ZSF0WOnpV6KdYy2UDchjUa3TZP8NWCAJEe-dCRjwi3C03VPRWgprf3oDSv3OSVf_ykV-JkojpGleshTrCU5GW1XpktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الشوط الثاني لمباراة منتخبنا الوطني ونظيره الفرنسي سيتم استئنافه عند الساعة 2:50.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79691" target="_blank">📅 02:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592498269d.mp4?token=HQimOiY5Ul7b6_lHUEDPL93w-SH8da1TIl1sFV6zXnRitcrLxxXqHyaq4MFUf1YN-rVbtJA4XLaBckPdySG21LMLjwoUbhzb__t2ZT0IZ9bMT0H2v6M1p9IeAIk-DgEmJFSp5fP7g0bGh8rKr88Q2XSzbe0ZyiarNA2Uv6qZF6UsOrgsJ6sTJoNGzYjN6tLfLo_-JR302AivsGG6jI2sa0V2gqkdKlySV0CniQUWMV4pyRyXJsJClqrC2BeogsMEtIkVmJAZ-pyO07ZSEhKRrRxp8oN6EPhf4amF5wj9LZS5BCuuqJ03w7qDwsBGA9wQB6sAjukTm5ZHsilifWwq1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592498269d.mp4?token=HQimOiY5Ul7b6_lHUEDPL93w-SH8da1TIl1sFV6zXnRitcrLxxXqHyaq4MFUf1YN-rVbtJA4XLaBckPdySG21LMLjwoUbhzb__t2ZT0IZ9bMT0H2v6M1p9IeAIk-DgEmJFSp5fP7g0bGh8rKr88Q2XSzbe0ZyiarNA2Uv6qZF6UsOrgsJ6sTJoNGzYjN6tLfLo_-JR302AivsGG6jI2sa0V2gqkdKlySV0CniQUWMV4pyRyXJsJClqrC2BeogsMEtIkVmJAZ-pyO07ZSEhKRrRxp8oN6EPhf4amF5wj9LZS5BCuuqJ03w7qDwsBGA9wQB6sAjukTm5ZHsilifWwq1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الشوط الثاني لمباراة منتخبنا الوطني ونظيره الفرنسي سيتم استئنافه عند الساعة 2:50.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79690" target="_blank">📅 02:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79689">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
🇫🇷
تمديد جديد موعد انطلاق الشوط الثاني تأجل إلى 2:20 صباحا بتوقيت بغداد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79689" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJSK5cxR3pZOD2MhQuWaKf5tNhAzSl0lPM9E_leI-a06D-i0eBFusSw9dLjFt0RRdedU9NcCqNGDfo2IC2WC00pEnHz8OjeuPeUnq1Buf90SXYRobgH087r8OxJsmsDYILzrXF6jJT1av9S5_WVJ9HfdFNmboGFpxmMtrg2i4-6CCyVpLlz7Rb0IqnuxCU_lmQLA5kToWDIctda4OxDhNMC3ut-BFwgVdF5Tuj2fgRj60El6LIvohiuKUMfz4yZj0IjUw28pLRJvUkx7pXjzSxGBN8ATPjtdka6l0iHHoo9UZJlBqjPcD5lUupkSJxEIFIMcyr2H5omFTiTr-Gw9jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
🌟
أبد والله لن ننسى حسينا،
راية الإمام الحسين (ع) حاضرة في مباراة منتخبنا الوطني.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79688" target="_blank">📅 02:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ستستأنف مباراة فرنسا والعراق ساعة 2:00</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79687" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79685">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwPJ4r7H_1eK_R9llhPIBt3PLk0Nef8AkeCfr7pliKmsGPlFZssyBPUR0x2eef_dOM3gRV3dY-XbYQ72-wDJwVp813ViSuhAh9LewOKbVD8b-4KQuIgrDS-5iGzvXbjPfVaeojI2CR9cj5PllI0y2p3d-8AIi5dzYGDrJBNExa2ywuK6oMFXjwOvAjMPKm5D6-OzgB1YHzed5T9txlT6rghS7zehdDNxhBUvwE7l948Quq-dgEmdjMc7xeG83vNo0OhuFDknEgoxeFg5Mxk4PHqgWiO3-hKjMWH6YVOLAPPllCDV2oj4NUZ12ZUhBOYcBfi1qth52LyruMT_dmXusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
انطلاق مباراة منتخبنا الوطني أمام نظيره الفرنسي.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79685" target="_blank">📅 02:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79684">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7459db2f.mp4?token=T7aPUbInVPW1gK5JSlHA6JXzMwm2u8IZ_phyrjajButQkueix3UfhPnNd3DPLD6R7qfFn0TdTpeffZcIAHJ2jO4Gh_Z8_vZcLTozEW7vT1td3vu7fz7R3dpkkht4OfQfOEm03MhhJbwvFp67F9K9lPUb1sSzK6JG2v3cx76dR94obg0buO1NJQXbrSZEq2CQkagg__XgXe4kxYNF-qr3Rk_emqIg8l5ltSpVni-bfgHKMofHpRUfkEH6rPsP7n8eNTEpda39yS14ZZ4qzokcaO27h1sRCyICthAtfac4CKU42bAuNcW-KMhjktbnql51Tayd7I93h2pN0M402OKU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7459db2f.mp4?token=T7aPUbInVPW1gK5JSlHA6JXzMwm2u8IZ_phyrjajButQkueix3UfhPnNd3DPLD6R7qfFn0TdTpeffZcIAHJ2jO4Gh_Z8_vZcLTozEW7vT1td3vu7fz7R3dpkkht4OfQfOEm03MhhJbwvFp67F9K9lPUb1sSzK6JG2v3cx76dR94obg0buO1NJQXbrSZEq2CQkagg__XgXe4kxYNF-qr3Rk_emqIg8l5ltSpVni-bfgHKMofHpRUfkEH6rPsP7n8eNTEpda39yS14ZZ4qzokcaO27h1sRCyICthAtfac4CKU42bAuNcW-KMhjktbnql51Tayd7I93h2pN0M402OKU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خروج معظم الجماهير بسبب شدة الامطار</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79684" target="_blank">📅 01:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79683">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2c91accd.mp4?token=NGZbV4ctLonYGCWGC025bXR01KaTJFQJ5uN7nnJkfwXZYfTv_sLKyQLRSWtCnmz9KofYjzSgsVtM85fqA5PdQ-tw_KItShSXgapWkyMtQAjQorsnlYVRW8W9kkYwr1Q09sfopCCS5qIcvDyeac7wgOSeQlb61jtlz8Lanbxhkm9FbHphDOrYMXN3dc8MiwBKjb0HrA1YXj9jU0q7Q063P1KJtMDFxh_7N28nvwzBH2uGlb5Z-VCOQUODWjQqMaEw66o0--8sIchzZCycdnVQZY-IQaUUnsFkl1Z-l_jjftkeu8CpcNvm0u6CkormMK5pELOfnyW9QtxcKX5E-9GuyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2c91accd.mp4?token=NGZbV4ctLonYGCWGC025bXR01KaTJFQJ5uN7nnJkfwXZYfTv_sLKyQLRSWtCnmz9KofYjzSgsVtM85fqA5PdQ-tw_KItShSXgapWkyMtQAjQorsnlYVRW8W9kkYwr1Q09sfopCCS5qIcvDyeac7wgOSeQlb61jtlz8Lanbxhkm9FbHphDOrYMXN3dc8MiwBKjb0HrA1YXj9jU0q7Q063P1KJtMDFxh_7N28nvwzBH2uGlb5Z-VCOQUODWjQqMaEw66o0--8sIchzZCycdnVQZY-IQaUUnsFkl1Z-l_jjftkeu8CpcNvm0u6CkormMK5pELOfnyW9QtxcKX5E-9GuyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترند يشعل الرأي العام العربي، بعد أن زعم ناشط عراقي، بحسب روايته، أنه وضع أنواعاً من السحر أمام موقع دخول المنتخبين العراقي والفرنسي بالولايات المتحدة بهدف التأثير على لاعبي المنتخب الفرنسي.  خوفك لا ينكلب السحر على الساحر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79683" target="_blank">📅 01:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79682">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ستستأنف مباراة فرنسا والعراق ساعة 2:00</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79682" target="_blank">📅 01:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79681">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🌟
🇫🇷
تمديد استراحة بين الشوطين لمباراة منتخبنا الوطني ونظيره الفرنسي 30 دقيقة بسبب سوء الأحوال الجوية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79681" target="_blank">📅 01:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79680">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6JdStlEUdbeZhYPL0YoooQ7NASRRLWJD4DN3vAKE8xJbcNNKDpSZp4NFYeTrwsjSUwqO1cVfhbX74q-OPRK52Emv7mVhPMLSO_rUO1gEw5-EOvUvVTn3kc--g2jqeof5jHekeNycQRIfdlja8rGA4mx3812sOzXea3ile-V_JOyH4Uz7TwovOvxKBiF_2JjTrIomMptdNXpvRA40BYoUFdDyjbD_W_DEs78ows7kHBDBnyVSE4VpfVDZmmYxgmmK4Jf-2pwGWA8ed2Lt0jyhEMF12WCVNs0HJk_sqHsCHT-7gs1jdtZ3PFRoC_NKzvR2fSXv6B_Z674P1B9kEhnzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج معظم الجماهير بسبب شدة الامطار</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/79680" target="_blank">📅 01:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79679">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc252ab75.mp4?token=VnWv0jTTnkdiamW6zN2k7FoWgXrhM5LgzHTERV605Zp8ePoCp-6pM8yHh2sDgfeT9wEqGy5tIb8qH3vxO5Ku7-GFcvWR0eubeUdUEL39awyX5bmGFHJW5jUhKH_NBjrpYMOR2gPVS68xlPgYdbfho4pdBUytk4vUk-hfIRiMyyRZp8bS8qBhozu97HfnaRG7tZOuSvrsEWGRnf41zQfezBB6a-fPEiHSIrTEEnJpHI5frrUnQ77aNcnpL82tpIQkqHeiGNXsKUZx3GFd-b5-ugfI1cOARvJnCG3TyXhV0hOUPBoMVdxPyV_eNUR9KBo6UXcD-LJNJgrGpY8tFCRCEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc252ab75.mp4?token=VnWv0jTTnkdiamW6zN2k7FoWgXrhM5LgzHTERV605Zp8ePoCp-6pM8yHh2sDgfeT9wEqGy5tIb8qH3vxO5Ku7-GFcvWR0eubeUdUEL39awyX5bmGFHJW5jUhKH_NBjrpYMOR2gPVS68xlPgYdbfho4pdBUytk4vUk-hfIRiMyyRZp8bS8qBhozu97HfnaRG7tZOuSvrsEWGRnf41zQfezBB6a-fPEiHSIrTEEnJpHI5frrUnQ77aNcnpL82tpIQkqHeiGNXsKUZx3GFd-b5-ugfI1cOARvJnCG3TyXhV0hOUPBoMVdxPyV_eNUR9KBo6UXcD-LJNJgrGpY8tFCRCEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇫🇷
انتهاء الشوط الأول بتقدم فرنسا على منتخبنا الوطني 1-0.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79679" target="_blank">📅 01:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79678">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هدف أول للمنتخب الفرنسي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79678" target="_blank">📅 01:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79677">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هدف أول للمنتخب الفرنسي</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79677" target="_blank">📅 01:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79676">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مجلس محافظة المثنى يعلن تعطيل الدوام الرسمي في المحافظة اليوم الثلاثاء</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/79676" target="_blank">📅 00:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79675">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
انطلاق مباراة منتخبنا الوطني أمام نظيره الفرنسي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79675" target="_blank">📅 00:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79674">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
انطلاق مباراة منتخبنا الوطني أمام نظيره الفرنسي.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79674" target="_blank">📅 00:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79673">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3459228578.mp4?token=CK08N9GgopuIztG-0rm-O_aGKgUy5knv6-UG6DCYILgOIgRId2ToyKoTLBFkcG-izcAmFflxnBz4d5HELoOh0bG5twSWGEGUgZp2m4vdvUU5U1UZU9qRRUHVODNrCJzCcvNcfraOMPcGNa2w8OJACazslMSGWQoT63N4xhLKmou-TECBP8eIsG4pRj6G0Jfp2iST5IJ9uQgF-wW-tiqywR0pezxWQSc8fWePXRwBXHeLi4xn82iqqoLLWHDlbuwTsJSEe4axHgabMjUmR55ty95ORJxELOhT1eEort-vh5PJLwIKboLWoytlE6SqLNVZXrUZQaxa-ueelvWxGgEXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3459228578.mp4?token=CK08N9GgopuIztG-0rm-O_aGKgUy5knv6-UG6DCYILgOIgRId2ToyKoTLBFkcG-izcAmFflxnBz4d5HELoOh0bG5twSWGEGUgZp2m4vdvUU5U1UZU9qRRUHVODNrCJzCcvNcfraOMPcGNa2w8OJACazslMSGWQoT63N4xhLKmou-TECBP8eIsG4pRj6G0Jfp2iST5IJ9uQgF-wW-tiqywR0pezxWQSc8fWePXRwBXHeLi4xn82iqqoLLWHDlbuwTsJSEe4axHgabMjUmR55ty95ORJxELOhT1eEort-vh5PJLwIKboLWoytlE6SqLNVZXrUZQaxa-ueelvWxGgEXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
مشاهد من مدرجات الملعب الذي يحتضن مواجهة المنتخب العراقي ونظيره الفرنسي، قبل انطلاق المباراة المرتقبة ضمن منافسات كأس العالم 2026.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79673" target="_blank">📅 00:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79672">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏محافظ المركزي الإيراني: طهران "غير ملزمة" بشراء منتجات زراعية أميركية وفقا للاتفاق</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79672" target="_blank">📅 00:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79671">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4670db6896.mp4?token=YynlhL7oMwYiiB6cijEoquoQfa5HPrBbGdWImfaeFXwHlCw5QR4Id1nZ6u0C_BDX545AIr5vBeAQMBFGw_OtFRhbIhSN_J1DpTbhNF_42MfkiN8vYM_nv2gT9gm-ZvY7RCQD1yemVvfA8KDIF5ilKpqgxsFhZnU_Kl690M4inSIVIkUdJCqAthb-tLgGptf2u5sNFgqxstAF2ImPvOsmG3H-MJXRBUxJ_tw_uyGt4vkSIxmjGO5yCmXbDAlOQeVt57-_8Zr3jh311sk7WNd9HpntZvtdV5l4vuniLLR_WazNb8zON6M1AI3RQ6acbRCGDCVKQ7YLwfWhSpP2MWH2cSQyzWTofC6M4GVhqWIGDS6C-7Kec28DXe_cfsPLnwc4ot0tTj8R1acZe3dFXzTUr8qujOpDJ_7TvYJKI1UgLMtZ9k5NmEhSM8WZhR1voUtCYYUbKo_uaWx_BN68NO7RwFKucq-1u4_jxGdSXz64zrdGKWaPK8H6cCW2j7r7ERZGPd_gG-PCs-7QppaRrI6qmUCQ99GIK1Enev6Z0YigB8gu50KoXYc-KNybHxZ0nlLRppXdPmM49eLRLq90-9E5O9Q1uuKuBkS3tlLt6r7c5ZEa9CWggjKCBf0AG03zgAqx8ijFUn-KsLs7UWBgJLK2lpi4ulOJ3mwCpy9Los23P8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4670db6896.mp4?token=YynlhL7oMwYiiB6cijEoquoQfa5HPrBbGdWImfaeFXwHlCw5QR4Id1nZ6u0C_BDX545AIr5vBeAQMBFGw_OtFRhbIhSN_J1DpTbhNF_42MfkiN8vYM_nv2gT9gm-ZvY7RCQD1yemVvfA8KDIF5ilKpqgxsFhZnU_Kl690M4inSIVIkUdJCqAthb-tLgGptf2u5sNFgqxstAF2ImPvOsmG3H-MJXRBUxJ_tw_uyGt4vkSIxmjGO5yCmXbDAlOQeVt57-_8Zr3jh311sk7WNd9HpntZvtdV5l4vuniLLR_WazNb8zON6M1AI3RQ6acbRCGDCVKQ7YLwfWhSpP2MWH2cSQyzWTofC6M4GVhqWIGDS6C-7Kec28DXe_cfsPLnwc4ot0tTj8R1acZe3dFXzTUr8qujOpDJ_7TvYJKI1UgLMtZ9k5NmEhSM8WZhR1voUtCYYUbKo_uaWx_BN68NO7RwFKucq-1u4_jxGdSXz64zrdGKWaPK8H6cCW2j7r7ERZGPd_gG-PCs-7QppaRrI6qmUCQ99GIK1Enev6Z0YigB8gu50KoXYc-KNybHxZ0nlLRppXdPmM49eLRLq90-9E5O9Q1uuKuBkS3tlLt6r7c5ZEa9CWggjKCBf0AG03zgAqx8ijFUn-KsLs7UWBgJLK2lpi4ulOJ3mwCpy9Los23P8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
نزول لاعبي منتخب الوطني الى ارضية الملعب لاجراء الاحماء قبل انطلاق المباراة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79671" target="_blank">📅 23:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79670">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4619fb40.mp4?token=UM3l6vxYa3MVfEWrpYa0HbERhy1xr8r-0Ufx3ztTxOyv2tpxJY71dwC_z1fU2FxfCF9slJfLujLONxYS0SCLectweKuwMP8ZAlU_frl9ztGqxmAuhoTClbkx3xecJbOIUxvhc6KWF2II7IIBLdeEmxB_hEL0cO1uci1I4C0EvE2pjngMKICWqzxV9S1WRCG84aHa5FPI5EoRyP7JrMmod4KAeNBB-TUB_54TazKFMp-yoZ_2jAV3jPuXtKm1QV85swqtXgm1f4HIJgKueqHv1quxtBcS9uAnqsQix3B0LnjKdD3xbwF3LDxB9hFi3saxNl_tru1mosLcNup3PFfGGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4619fb40.mp4?token=UM3l6vxYa3MVfEWrpYa0HbERhy1xr8r-0Ufx3ztTxOyv2tpxJY71dwC_z1fU2FxfCF9slJfLujLONxYS0SCLectweKuwMP8ZAlU_frl9ztGqxmAuhoTClbkx3xecJbOIUxvhc6KWF2II7IIBLdeEmxB_hEL0cO1uci1I4C0EvE2pjngMKICWqzxV9S1WRCG84aHa5FPI5EoRyP7JrMmod4KAeNBB-TUB_54TazKFMp-yoZ_2jAV3jPuXtKm1QV85swqtXgm1f4HIJgKueqHv1quxtBcS9uAnqsQix3B0LnjKdD3xbwF3LDxB9hFi3saxNl_tru1mosLcNup3PFfGGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
ترمب
: مضيق هرمز مفتوح بالكامل،والأموال الإيرانية المجمدة التي سيفرج عنها ستستخدم حصرا لشراء المواد الغذائية من المزارعين الأمريكيين.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79670" target="_blank">📅 23:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79669">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda743fbcd.mp4?token=WBM0Rt3uyoZdtK5rmVAfMvDI7vJkMf4d95992Gr1lxatma2mXvJ4bV79-O0DqZJQ2CbGknC8ehAncw4N2KFd9BCU23fG-vhckj8bwDgC7E2OSfEyF0I3_DEOGhI4nbopuskkKbTmZFeqHi5PAF3SknjLpgWx34Zvw2D6KQFMmZblbPVK6TSRWgcafvBYGDLUp_CEtTQLA9jAf-tymgRzzV4ejfGtyItMsK2Ys19-c9SjH44Jc9moRz7bygmH6UeOA5JuM-v-GJ0Y3Q8lo22_aBI19XJ9nPS6RISUEgF0TSKtGGYPxHlARVsWGxkyYFJlNn91cr8nsvZQEQTCLeEquA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda743fbcd.mp4?token=WBM0Rt3uyoZdtK5rmVAfMvDI7vJkMf4d95992Gr1lxatma2mXvJ4bV79-O0DqZJQ2CbGknC8ehAncw4N2KFd9BCU23fG-vhckj8bwDgC7E2OSfEyF0I3_DEOGhI4nbopuskkKbTmZFeqHi5PAF3SknjLpgWx34Zvw2D6KQFMmZblbPVK6TSRWgcafvBYGDLUp_CEtTQLA9jAf-tymgRzzV4ejfGtyItMsK2Ys19-c9SjH44Jc9moRz7bygmH6UeOA5JuM-v-GJ0Y3Q8lo22_aBI19XJ9nPS6RISUEgF0TSKtGGYPxHlARVsWGxkyYFJlNn91cr8nsvZQEQTCLeEquA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
تشكيلة المنتخب العراقي لمواجهة المنتخب الفرنسي</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79669" target="_blank">📅 23:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79668">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KT6N4QPmZfx4DRWce5N0KOqP7otsyhQEFaCYEQm-g8XsNxBhcoSbHgCNXOa0Hp-0yhg94-boaIVW3h7c2Btvsr2Ft5DNQVyxlcQXKu7v9_eUveXUzCxJr79rQepMtp4rpoCgZDm7ctq2VGDX9plIo3SJZ9Oenn0VVVEBN7lQr2tsO-cYGXT62am8bcpdKCL0V0Hyd9rG5ZBwg8S1ZScANbv_xq1DYoW4elRSjfCMyk0_Ml8Xx7mKmkPhNHuaye2ZeXaCxaUqdQ6ArhqAIYUk9NifN27wvSmoK3TfrbtEkGNMmPUUlQ7IBwzyeJ9Um-YK7FzLaOVbA7EjgcIUOjzeAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
تشكيلة المنتخب العراقي لمواجهة المنتخب الفرنسي</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79668" target="_blank">📅 23:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79667">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
‏خفر السواحل الأمريكي يعلن تحطم مروحية من طراز MH-60 جاي هوك في ألاسكا، وفرق الإنقاذ تستجيب للحادث.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79667" target="_blank">📅 23:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79666">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b5ad36da0.mp4?token=QMoxj3NMinV642Ldg66ks4MkRVRbtJzp97yQMNpi1Gu7aaLsEU1ZFvBaizA6wpj6XZON7PvuoRCr-bTwhIYZHgdPcN4N7kUK8p2whvS-BVIhuIZvblEpU4Il06IDtE98q2_EaMoqaKAYeZp0OGrYKu1XSDhei1uirlANT5em-X_yIdVEZzERQx-W0SvBU7XdUzeqKNoOe1ycwklON5MLkF1t0Xu3dTlSXTCjlP0juKCpX8CnLD_W7KZLhnncYKgUwy_x2VrD8uBRNFxy-bk0NyPBnF__QmgqeIg-evXSyGY-HWeJeDnP6TEyT0616krn5xsYmxlDAwNoMxsMlZ08Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b5ad36da0.mp4?token=QMoxj3NMinV642Ldg66ks4MkRVRbtJzp97yQMNpi1Gu7aaLsEU1ZFvBaizA6wpj6XZON7PvuoRCr-bTwhIYZHgdPcN4N7kUK8p2whvS-BVIhuIZvblEpU4Il06IDtE98q2_EaMoqaKAYeZp0OGrYKu1XSDhei1uirlANT5em-X_yIdVEZzERQx-W0SvBU7XdUzeqKNoOe1ycwklON5MLkF1t0Xu3dTlSXTCjlP0juKCpX8CnLD_W7KZLhnncYKgUwy_x2VrD8uBRNFxy-bk0NyPBnF__QmgqeIg-evXSyGY-HWeJeDnP6TEyT0616krn5xsYmxlDAwNoMxsMlZ08Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
خلال زيارة بافل طالباني لإحدى الكنائس الكلدانية في محافظة السليمانية، وجّه إعلامي تابع للبرزاني سؤالاً له بشأن تشكيل الحكومة أثناء مغادرته، ليردّ عليه بانفعال قائلاً:
"مو وقت هذا الكلام يا حيوان".</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79666" target="_blank">📅 22:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79665">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d275b950.mp4?token=LG600C9zJ_iafYRGAQYVbxg3RvVmbA0is4Aqy5zGGVibeklGJYmM-Jcf9L5Xy_MxQs3FvIumtRK6Rjpzei9a-bclGMkhopBAC-M1Zlc3V4mQCNt9LsihdOiVT7KCC45Y0m5zLO7FbtbBPe9ZwC_gCqYs3JbAnSuSThhLjerC_J0jYs9XSZfc42JIIWGOZCAx4JA2_10Ay0Wp8KPstRCsFSggqssxCxe1GxXk1g9UCNB8cbfCeRBMOXuxptbNlvox9HeqjksDzP_7oP5DKa3tSHnO8qhGe8Cb3P1YF9o05CJUOtVNpt85vcq-HzpYbhabRdu7a12WFzu2S7DhaZjRig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d275b950.mp4?token=LG600C9zJ_iafYRGAQYVbxg3RvVmbA0is4Aqy5zGGVibeklGJYmM-Jcf9L5Xy_MxQs3FvIumtRK6Rjpzei9a-bclGMkhopBAC-M1Zlc3V4mQCNt9LsihdOiVT7KCC45Y0m5zLO7FbtbBPe9ZwC_gCqYs3JbAnSuSThhLjerC_J0jYs9XSZfc42JIIWGOZCAx4JA2_10Ay0Wp8KPstRCsFSggqssxCxe1GxXk1g9UCNB8cbfCeRBMOXuxptbNlvox9HeqjksDzP_7oP5DKa3tSHnO8qhGe8Cb3P1YF9o05CJUOtVNpt85vcq-HzpYbhabRdu7a12WFzu2S7DhaZjRig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سمح لجماهير المنتخبين الفرنسي والعراقي بدخول للملعب بصورة طبيعية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79665" target="_blank">📅 22:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79664">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YatzupQuR2wGsOa4eWeeN-3phnbvlIECoTGWEY3AzEsUZbl6L9FIW4LBYqb-4mQfUDd2wsDTN4ZpO_jQmbVGSKGqsoa8Ad-cUAgB-n4OoY507Nx910kkoJrhZySpuyLBul4NcvMxhoLllqMHtwvUdlXlMgpzuxzHdPVLFR6KsAQyzCDvbhMzdRyAzRITUOYnezz-FxZKwN6TiI196WTYcgc3pR12x7l06sCWlfpuUgO5Xm5xAF-8N9jKYFS15hMXuU2WpSb3BU_QDeynHIodvgtg1-GfUrCgMxaztmoYPJOk0Vz05iebo2loWvnYJkxp3ZBazcuoT-37op8GsdJ04A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد جاسم : المباراة بين العراق وفرنسا قد تتأجل</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79664" target="_blank">📅 22:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79663">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭐️
عاصفة جوية تأخر فتح أبواب ملعب مباراة العراق وفرنسا.  يبدو أن مفعول إبراهيم الخلاني قد جاء بنتيجة
😆</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79663" target="_blank">📅 22:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79662">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbb558716.mp4?token=kMXJ_Iw12ZD2KElnyZavmuK9F0R5o8rLdFnM25tJ0pXJQ9Og6hEjTzlyQWh38KhCqqjyTmYbWguffkpr57di5zDvQ3dkGuV_ideJqu-iYZ360196DNX-gCdZ47yAV78ffnkO_JKyOIFcl_wH90_FA9C5LBfmfsRZ1PKIMLdOhdjLEDGShcw4aLh_Z6rghBLn_Anszdc4poXnuqFtrzuwee7yYhZdg2AD2kAA1IDujHojVfIQhj8DgII29-i-86nRmPmUjH-KYzDuT_qwbqmQVB4c19ZNUSXYy6bYYIe5d8Lniepf-ScXSfgeU4laq8osRA82pvZiXnpcnlV-PR5Uuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbb558716.mp4?token=kMXJ_Iw12ZD2KElnyZavmuK9F0R5o8rLdFnM25tJ0pXJQ9Og6hEjTzlyQWh38KhCqqjyTmYbWguffkpr57di5zDvQ3dkGuV_ideJqu-iYZ360196DNX-gCdZ47yAV78ffnkO_JKyOIFcl_wH90_FA9C5LBfmfsRZ1PKIMLdOhdjLEDGShcw4aLh_Z6rghBLn_Anszdc4poXnuqFtrzuwee7yYhZdg2AD2kAA1IDujHojVfIQhj8DgII29-i-86nRmPmUjH-KYzDuT_qwbqmQVB4c19ZNUSXYy6bYYIe5d8Lniepf-ScXSfgeU4laq8osRA82pvZiXnpcnlV-PR5Uuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
قوات الأمن الكندية تحاول إخلاء محيط المركز اليهودي في مدينة مونتريال الذي تعرض إلى هجوم مسلح وسط إستمرار الحدث الأمني.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79662" target="_blank">📅 22:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79661">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdef836eef.mp4?token=Z4ShmDhd6FLI8_QquvgsikXc1I4KPZikUAK9ZkmtOVu-U4kH846u_zKZp-dYxI0EE4ag2gSKf_2JsEl9i3Vi3g23-iD-T3wifFZFTZK-8s53Zy3AlSYEbtYI43-4jk34hTNEBkklOK3NzSPAh9fKzfQgzX02OBT8jjcYcuBEYBvQdRA9K3bMsjQqfhxHNSSRZiP0JwzhRMk9rhTfqin2UMX0s5MigUwmcg-xWwEV3z9jEuWqWQjJIoDJQvsCxgPnoA409Qug9TCArybvM0STpDICLeNH0Xdpxvs2rX2ZbfNbtKB2gCuBbKIoec1iyWuICfTVxAe14jmX5rNlz7Xdew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdef836eef.mp4?token=Z4ShmDhd6FLI8_QquvgsikXc1I4KPZikUAK9ZkmtOVu-U4kH846u_zKZp-dYxI0EE4ag2gSKf_2JsEl9i3Vi3g23-iD-T3wifFZFTZK-8s53Zy3AlSYEbtYI43-4jk34hTNEBkklOK3NzSPAh9fKzfQgzX02OBT8jjcYcuBEYBvQdRA9K3bMsjQqfhxHNSSRZiP0JwzhRMk9rhTfqin2UMX0s5MigUwmcg-xWwEV3z9jEuWqWQjJIoDJQvsCxgPnoA409Qug9TCArybvM0STpDICLeNH0Xdpxvs2rX2ZbfNbtKB2gCuBbKIoec1iyWuICfTVxAe14jmX5rNlz7Xdew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
عاصفة جوية تأخر فتح أبواب ملعب مباراة العراق وفرنسا.  يبدو أن مفعول إبراهيم الخلاني قد جاء بنتيجة
😆</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79661" target="_blank">📅 22:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/535b8f94e7.mp4?token=miIYHLf_UI-0q1PKfBZkwI80lKQwpar0nh_OB1l8Am1MJazFZcfNhpBTlMUXLCT77V2OFe2ZKNXrqPiAQZG0qLn5-QvuAt2m6hY_XQcx5gzzQhekOhTFlPYtSRWeqvzeogpFWBoqhiXJv4kNZi3yR4fn4ESib5F1qXa6cbMfVmSK1qHsboYs7SYKIyyVUFL7RgbfqzkQeH-3z6q1mGtLgP54ofPvxjIzdGlAu1idBUovg3zzLsAOUBYe6GLCKJiHTtSvfJi4UkbFFiD3B5pc650H1tMI9BoaB3x3CTLOH8yZ6HbL_bLaM4mHzIBOjpqzexGqEqAGfSAw_s3kv71n3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/535b8f94e7.mp4?token=miIYHLf_UI-0q1PKfBZkwI80lKQwpar0nh_OB1l8Am1MJazFZcfNhpBTlMUXLCT77V2OFe2ZKNXrqPiAQZG0qLn5-QvuAt2m6hY_XQcx5gzzQhekOhTFlPYtSRWeqvzeogpFWBoqhiXJv4kNZi3yR4fn4ESib5F1qXa6cbMfVmSK1qHsboYs7SYKIyyVUFL7RgbfqzkQeH-3z6q1mGtLgP54ofPvxjIzdGlAu1idBUovg3zzLsAOUBYe6GLCKJiHTtSvfJi4UkbFFiD3B5pc650H1tMI9BoaB3x3CTLOH8yZ6HbL_bLaM4mHzIBOjpqzexGqEqAGfSAw_s3kv71n3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترند يشعل الرأي العام العربي، بعد أن زعم ناشط عراقي، بحسب روايته، أنه وضع أنواعاً من السحر أمام موقع دخول المنتخبين العراقي والفرنسي بالولايات المتحدة بهدف التأثير على لاعبي المنتخب الفرنسي.  خوفك لا ينكلب السحر على الساحر</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79660" target="_blank">📅 21:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79659">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXLlR4Mh9KUi5oOUTAJBx9o0P8m8GoMju-tw5fqKGpmuhvGrGVlrDEnh2mIIokRlUSaOCmFlGT2arrgYqFN10LE116coBs_5-8ZeY8FEGZ9-gTABy5FhFhhcwb1EXaUrg-S3jrWsQnvGrXrULSXCS-Jd5kNPfSKOf-HMUYRSmtNR7iuigPclKAIL9F75KshkyZADjFScqzWit35IqQMP0G5tfg4l34IgzgdRvTAXSOf-Yu2gfWjaLGEvfFaYATfn9fgQCm6pgmbYongbHgjEtK-qO0SHcl9R4RlcAGSUmBBA71zw1VCfz0YyOYxb3OnnRw_WH-pqS3EY_CpPwI2RLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🙃
🇬🇧
هجمات صاروخية عنيفة تتعرض لها مدينة فورنيج الروسية من قبل أوكرانيا على ما يبدو هجوم بصواريخ شدو البريطانية .</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79659" target="_blank">📅 21:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79658">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8adaf80237.mp4?token=sJ_uNDtq_IgEC6aVd9ML3EEAL4v_fR97lDyIBSDgYuqhgCM-kKjGkzyEyJDDU085YBvP5JrlpfiMDzSpoQxJMHnVdRHeOk5rw72ua-ey8CpQzWHhrN6zwiXwtX8cqJWKa0uNTWTQh5z1DmEa-G6rvytCkBy-EemtvR9BMhjlU6x-Ie2oYFunHgumFoir9dcJvu-f85fh98_kXDGbIUa1iqowCmX1mxZI3ZCK6w7CSI-8woNw_uJpWAHSAjenugYcbFlDNjy31oqPDvMdPKuG5rjF3RWsshC4mcLPXDggHeL1glUUMd8JffbirwsxA6eYz_17prP8dWYosxeBooMCxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8adaf80237.mp4?token=sJ_uNDtq_IgEC6aVd9ML3EEAL4v_fR97lDyIBSDgYuqhgCM-kKjGkzyEyJDDU085YBvP5JrlpfiMDzSpoQxJMHnVdRHeOk5rw72ua-ey8CpQzWHhrN6zwiXwtX8cqJWKa0uNTWTQh5z1DmEa-G6rvytCkBy-EemtvR9BMhjlU6x-Ie2oYFunHgumFoir9dcJvu-f85fh98_kXDGbIUa1iqowCmX1mxZI3ZCK6w7CSI-8woNw_uJpWAHSAjenugYcbFlDNjy31oqPDvMdPKuG5rjF3RWsshC4mcLPXDggHeL1glUUMd8JffbirwsxA6eYz_17prP8dWYosxeBooMCxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تأجيل فتح أبواب ملعب فيلادلفيا قبل مباراة فرنسا والعراق تحسبا لعاصفة.
"
الشعب يطالب تأجل اللعبة أو الغائها
"
😭</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79658" target="_blank">📅 21:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79657">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4yPBNUCJN0pZN870FiZyeSLHoBCsdGoMuzeGpjz-FPqlg74_BDDUiQZH3f9V3Id0c1yTKnudtiG82WFaCRS2hdXN-UgSFfM5jJVNh2NUt36seTkFRVH1BwlQuuBCAUmglCTMFkRMN-O9hIGR38YSKDIldLD9K8fQ0SI-d38n1VXcBBhQz-4ZRT8aWrOjSd8tMbY04OjhpkdfC7St6nz61tHS8fFhDeKDpq6tWTJSpbHnmVoNGBbFPVGywMIcmXHZV2yegsCidCXMoSkZpz29TdgE35wWuXOsUmY_B2C3Xa7vVUYzemexFkCbFjKcNthr_5jQhMRPBngOnYBWQvjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
سوالف الگهوة   تعين گريكور الأرمني سفير العراق بالولايات المتحدة الأميركية ؛ گريكور كان يشغل منصب مستشار السوداني</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79657" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
قوات التعبئة العامة اليمنية:
نعلن جهوزيتنا الكاملة والفورية لترجمة توجيهات السيد القائد يحفظه الله لإسناد ورفد الجيش بالمقاتلين لمواجهة قوى العدوان.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79656" target="_blank">📅 21:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
🇮🇶
السفير الإيراني في العراق محمد كاظم آل صادق:
العلاقة مع العراق تتجاوز أعمار الحكومات
نحترم أي قرار تتخذه الحكومة بشأن حصر السلاح باعتباره شأناً عراقياً
مكافحة الإرهاب وأمن الحدود والتجارة أهم ملفات التعاون مع العراق
المقاومة هي خيار للشعب العراقي
إيران تحترم حق الشعب العراقي في الدفاع عن نفسه
إيران لم تطلب من أي طرف التدخل في حربها مع الولايات المتحدة و(إسرائيل)
مقترح لتفعيل موضوع المناطق الصناعية المشتركة في بعض المحافظات العراقية
العقوبات الأمريكية تسببت بمشاكل للعراق في دفع مستحقات الغاز الإيراني
74 جامعة إيرانية مدرجة ضمن قائمة الجامعات المعترف بها في العراق.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79655" target="_blank">📅 21:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79654">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
الطيران المدني الإيراني:
قيود على حركة الطيران في طهران وقم ومشهد خلال مراسيم جنازة قائد الثورة الإسلامية الشهيد آية الله السيد علي الخامنئي(رضوان الله عليه).</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79654" target="_blank">📅 21:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79653">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a8eda7fc.mp4?token=ZOvBgB3-RJ6qK8t8q7Pv0hmQYdmzDenpthR9Ay62c0oaAIcF_YfqdvQkXgWedAONPGPOPFWlYqPCbtGTazYrclNrVOh8o3Yiu4kQlMRPhGAw783m2hOAFqco2WYqMRKnmRFryHCIUN6H_mrN6tGZJZO7G_VOK40VeAML-aUO27F2pGq7ev9ettzhNArmFCvc7TRJ3pO_mz0ZW_oxwXC8OUUXoquGvq7VdT0jT_8FVAwzwTHFR3H6VH15dLPU99-6Yct1HYdAb7uUYXGqFONikxtu0qXRt1a72uYyCRVhnbdc4ur55MyfG2sBgU927-dG0YTHFHTvJVFemtVobJSLMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a8eda7fc.mp4?token=ZOvBgB3-RJ6qK8t8q7Pv0hmQYdmzDenpthR9Ay62c0oaAIcF_YfqdvQkXgWedAONPGPOPFWlYqPCbtGTazYrclNrVOh8o3Yiu4kQlMRPhGAw783m2hOAFqco2WYqMRKnmRFryHCIUN6H_mrN6tGZJZO7G_VOK40VeAML-aUO27F2pGq7ev9ettzhNArmFCvc7TRJ3pO_mz0ZW_oxwXC8OUUXoquGvq7VdT0jT_8FVAwzwTHFR3H6VH15dLPU99-6Yct1HYdAb7uUYXGqFONikxtu0qXRt1a72uYyCRVhnbdc4ur55MyfG2sBgU927-dG0YTHFHTvJVFemtVobJSLMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
قوات الأمن الكندية تحاول إخلاء محيط المركز اليهودي في مدينة مونتريال الذي تعرض إلى هجوم مسلح وسط إستمرار الحدث الأمني.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79653" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79652">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامب: يدرك الجميع تماماً أن إيران ستوافق على إجراء عمليات تفتيش رئيسية للأسلحة لضمان "النزاهة النووية" على المدى البعيد.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79652" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79651">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/150b134093.mp4?token=dHaNdy4wkJqdzevYO8Sdg8bz1hGU3ztoLMr6kL8WDnFHFgujz-X4KDPj7mGxEJ3GOoLvSu7n8a2Gp5JuNriARadIjYiiC71LvgCHqfflqPQWoQac1KYc0JOowGrcyxQA03OZzVfP8UvcYfxAxioS_VvnW9wVOnrhPLkO_pw1RxDt3Vr6-V81QbxgHO_hyS1k3Nz2gpEhyTVUJ9c4Sg4HzmAhuQmex-C2N9UbTVKohRF7UdfMHY9TYdXGc2aQI6XfqzrjOT1HS99jSfTMmAY7lg_RVYa9phZ6d9yMvlIS8S-IimEDr6opdZx9DgN24HPmxrX3L4K30zWXevImyy6k_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/150b134093.mp4?token=dHaNdy4wkJqdzevYO8Sdg8bz1hGU3ztoLMr6kL8WDnFHFgujz-X4KDPj7mGxEJ3GOoLvSu7n8a2Gp5JuNriARadIjYiiC71LvgCHqfflqPQWoQac1KYc0JOowGrcyxQA03OZzVfP8UvcYfxAxioS_VvnW9wVOnrhPLkO_pw1RxDt3Vr6-V81QbxgHO_hyS1k3Nz2gpEhyTVUJ9c4Sg4HzmAhuQmex-C2N9UbTVKohRF7UdfMHY9TYdXGc2aQI6XfqzrjOT1HS99jSfTMmAY7lg_RVYa9phZ6d9yMvlIS8S-IimEDr6opdZx9DgN24HPmxrX3L4K30zWXevImyy6k_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صورة تظهر قطعة سلاح استخدمها المهاجمين لاستهداف مركز يهودي في مونتريال الكندية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79651" target="_blank">📅 21:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79650">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6435480bd6.mp4?token=aqWQm99PVIz9vLUcLbqMw4adSrVqdM6ulqnnE3gPNUtFlJCuHoafz1RM88Jmhkw5kg7mVs2bu2s76Nob-DolcRhOK66eLHXIMlsayCxNQa3sCQHnEUQIcjXmFOtEv4LiRGI9JUGydiUiC-PGXScM8zC8IH1ZNI1_8v0YqT__VCtJXlY1t-kGL8pPIvhWvPU4c3XEJpg2Q2nuEW5QxbESxbcI2PlddMrMiGVvNFxOZfyoX7r2-u0APXWl_rLav58pDiL_Da4mPfHZN-11E4g0CUFy7SbL9-ZVeriQyr-ZU8moRrdzvwNCuF7hFd5pFMEu0ObyHpOJW1Mo2jfb67w6Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6435480bd6.mp4?token=aqWQm99PVIz9vLUcLbqMw4adSrVqdM6ulqnnE3gPNUtFlJCuHoafz1RM88Jmhkw5kg7mVs2bu2s76Nob-DolcRhOK66eLHXIMlsayCxNQa3sCQHnEUQIcjXmFOtEv4LiRGI9JUGydiUiC-PGXScM8zC8IH1ZNI1_8v0YqT__VCtJXlY1t-kGL8pPIvhWvPU4c3XEJpg2Q2nuEW5QxbESxbcI2PlddMrMiGVvNFxOZfyoX7r2-u0APXWl_rLav58pDiL_Da4mPfHZN-11E4g0CUFy7SbL9-ZVeriQyr-ZU8moRrdzvwNCuF7hFd5pFMEu0ObyHpOJW1Mo2jfb67w6Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
بعد عودتهما من سويسرا.. قاليباف وعراقجي يتوجهان الى سلطنة عُمان للقاء سلطان "هيثم بن طارق"، وبحث سبل تعزيز التعاون الثنائي وتوطيد الترتيبات الإيرانية لإدارة مضيق هرمز.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/79650" target="_blank">📅 20:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79649">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iank73DVMhEKnQDR9wBIlMTtCpWLj-Ti3M1ambTjryEGYG-OfzkWm4NAVgqYyDuoLBLfqyOJEppyPzyGyfKRTq3nml-YzUcYMDTs3UEyidiRHN_ptcs4eOzrWdRYP3fhuXpVGfK_-J5aISShYbl8QNS8-D1xP3a2Bb_-TFWOOq-XfFb3O5PsWFB4LQ-h8k2tdGcxOb1TsJhKm2ITxuRCOtMKdzaToeJRR7-7jNt0fYu-wTL0hYWGAaVpb4c0Xz11H7h8mFQmWu7T8CSLDKtH8DoWECdrqwD7uWzugNODCpSzbr-L1YvArQsq1ebz41hTEPfP9An7YhlJwhspYMgujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو: وجود رهائن داخل الموقع اليهودي المستهدف في مونتريال الكندية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79649" target="_blank">📅 20:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79648">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
الهجوم المسلح استهدف مركز أعمال يهودي في مدينة مونتريال الكندية.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/79648" target="_blank">📅 20:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79647">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⭐️
قتلى وإصابات في حي يهودي بمدينة مونتريال الكندية جراء هجوم مسلح عنيف.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79647" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79646">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11bf06c348.mp4?token=s__x58dNSRwgBC6U0yTtvMcF5ta1pwIzJzHdWk0GwYyBTaR7x98Xx8esBebZAIm1WjMMmPxFP87uk3geC-LqrL7Zb0u-SkO_qqXHB3XseYVQEx__baGbUXZCGOwQTnxVcIwATF2Y91lcQ6QaNsK8l85uyGISLG0AsRDCMOBNbBWCvJijRK2bLpS5leR1B8eVngNJSCbEmf4VortdbDSUpqaVvEDWsChR7Y5C8g5_jZbmvrvJ-6ozJfbs0qck8umUft0qxQZ94WEwgCBXLJcLQEcZrnd4P_7m1sLciaJqnn7s1ti7nyGN1c0Jn7Y4ltRKwbVykRg3O2CoJMHTL83kpmjLPt22DuPeniU_5VCxKDE4qFfyu1SEdXOOgpZs95SxaWgk9_DCRkwplqi711KncSqv_uMxgB66BZYnzEWMlYb0hwYI1Ft98JvnjoEGz1_qBseq8hpkrrd3gvMdI5APxLzGy64GzdcGt8W-O2Qs0wJ1V7wCybWxDoJx35vOU86YN5yKcIF1M_89Ri0tyEN3Ag3-eibBni_1B1V6MmCeJPLaK-ZnT6fQuXnUhuRw4Z01c3u1BCox8kf2wEQjZiG9HuX0XvnKieb4PEi2VQKUHCRSQQoOTYbd6YopLMpj7TkkqtXk2FZ3AKouv4epv5fyZv1nDjlmlDucr-KlOSt_pA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11bf06c348.mp4?token=s__x58dNSRwgBC6U0yTtvMcF5ta1pwIzJzHdWk0GwYyBTaR7x98Xx8esBebZAIm1WjMMmPxFP87uk3geC-LqrL7Zb0u-SkO_qqXHB3XseYVQEx__baGbUXZCGOwQTnxVcIwATF2Y91lcQ6QaNsK8l85uyGISLG0AsRDCMOBNbBWCvJijRK2bLpS5leR1B8eVngNJSCbEmf4VortdbDSUpqaVvEDWsChR7Y5C8g5_jZbmvrvJ-6ozJfbs0qck8umUft0qxQZ94WEwgCBXLJcLQEcZrnd4P_7m1sLciaJqnn7s1ti7nyGN1c0Jn7Y4ltRKwbVykRg3O2CoJMHTL83kpmjLPt22DuPeniU_5VCxKDE4qFfyu1SEdXOOgpZs95SxaWgk9_DCRkwplqi711KncSqv_uMxgB66BZYnzEWMlYb0hwYI1Ft98JvnjoEGz1_qBseq8hpkrrd3gvMdI5APxLzGy64GzdcGt8W-O2Qs0wJ1V7wCybWxDoJx35vOU86YN5yKcIF1M_89Ri0tyEN3Ag3-eibBni_1B1V6MmCeJPLaK-ZnT6fQuXnUhuRw4Z01c3u1BCox8kf2wEQjZiG9HuX0XvnKieb4PEi2VQKUHCRSQQoOTYbd6YopLMpj7TkkqtXk2FZ3AKouv4epv5fyZv1nDjlmlDucr-KlOSt_pA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
13-06-2026
ناقلة جند "نميرا" تابعة لجيش العدو الإسرائيلي في موقع مرتفع الحمامص المُستَحدث مقابل بلدة الخيام جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79646" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79645">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIUVT2JHczXdz_LoeRYj7Ki5L2xJggnh9MAT2NkgL1Fc9GNIA3M-0d8eBgY-QPBPri7Ux-ocZB0hg4FSzeRQetOMxRBwGmVT-VN8ptoQ58qN8VFx2MzhDomoV2vJPCAB7PJ1asdgR8b_A64VjkWCl-TskQTlsMd2x_293SWetTrE1tS6oE9Rp7wXKeaHX4yn08JeaaPFZdqpYtICdiXJ10Pl0U8VkIE490_Ck-A1wUXipRXPvE07Yf1fszMRFSoJ1L3ccl8Ng4JYRy_fwfUL-zActpjGuSzpQS7rqBwapEKTlzplbfHc9bFe6lJnvRHRnSAPawad0X6gcOvks7T66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: "إنّ ادعاء نائب الرئيس الأمريكي بشأن عودة مفتشي الوكالة الدولية للطاقة الذرية إلى البلاد منافٍ للواقع وكاذب. لم يُذكر وجود مفتشين في البلاد خلال المفاوضات السويسرية."</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79645" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79644">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a163827b.mp4?token=orbi5FcABcd_JUCo19VQMU8rnRPAg6LQOanSUarb9KMhhjNW8gvn4dUI97d0G6i9eZUPznAbDuntxoUa45cCAI0qmSZ624YWD7W-Ha6dEFaTNbgw4kC6XkR9Z4D1O4yjZ5co4iuNOXCoiKpHDOi4eHwp3uewixRukv1W-cBWpIJMna9OxVQtCkjSGi5PrwJ42SjEOVpzNh4tao79WZw2Y_dBXDcWqtxpffbsFm3BmtzNrI3irryiiGtnoKoi6mwlfoxm0bIG7YmmF4dNmwiOREZ9EyFM8Z2Ir6x7tpmMhEhaTVcN-AnJHFHDuAcC1WyadFOv9RVOVchSRrdN71MpNUuFCv5iwak1UQeyuEsiIK9cyCMHfoEHx44Cl-G_KdaE7V7kR2-2jHzNOtLU4K0IcQdmQrT_ozYKLrI9lHVD48lp5h9TCHNfixYhae40YlrCJa8-ORi8q3DbYp0pyMbLW6Ff0he6I1tb8mLp-bbdks2ywBf6vfTS-6xn-CigbRaKevDwThxhaa6EgYnqU-yFcbbIasU5NqP4SiUaasw5h_dCMljPKWRt6mx0i_9Z6kXvFsB_sn0xQ8r3Eml-5k_NDWI7ieA0VKzViiV5NiJwJWXf0DXUTJodjqMFWls2KHsOxmWQU5U6qg4dBROfw3UxFNJpmdk4DbrdQgqw_0VHq6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a163827b.mp4?token=orbi5FcABcd_JUCo19VQMU8rnRPAg6LQOanSUarb9KMhhjNW8gvn4dUI97d0G6i9eZUPznAbDuntxoUa45cCAI0qmSZ624YWD7W-Ha6dEFaTNbgw4kC6XkR9Z4D1O4yjZ5co4iuNOXCoiKpHDOi4eHwp3uewixRukv1W-cBWpIJMna9OxVQtCkjSGi5PrwJ42SjEOVpzNh4tao79WZw2Y_dBXDcWqtxpffbsFm3BmtzNrI3irryiiGtnoKoi6mwlfoxm0bIG7YmmF4dNmwiOREZ9EyFM8Z2Ir6x7tpmMhEhaTVcN-AnJHFHDuAcC1WyadFOv9RVOVchSRrdN71MpNUuFCv5iwak1UQeyuEsiIK9cyCMHfoEHx44Cl-G_KdaE7V7kR2-2jHzNOtLU4K0IcQdmQrT_ozYKLrI9lHVD48lp5h9TCHNfixYhae40YlrCJa8-ORi8q3DbYp0pyMbLW6Ff0he6I1tb8mLp-bbdks2ywBf6vfTS-6xn-CigbRaKevDwThxhaa6EgYnqU-yFcbbIasU5NqP4SiUaasw5h_dCMljPKWRt6mx0i_9Z6kXvFsB_sn0xQ8r3Eml-5k_NDWI7ieA0VKzViiV5NiJwJWXf0DXUTJodjqMFWls2KHsOxmWQU5U6qg4dBROfw3UxFNJpmdk4DbrdQgqw_0VHq6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: عملية إطلاق نار في حي يهودي في مونتريال بكندا.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79644" target="_blank">📅 20:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79643">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
عملية إطلاق نار في حي يهودي في مونتريال بكندا.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/79643" target="_blank">📅 20:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79642">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: "إنّ ادعاء نائب الرئيس الأمريكي بشأن عودة مفتشي الوكالة الدولية للطاقة الذرية إلى البلاد منافٍ للواقع وكاذب. لم يُذكر وجود مفتشين في البلاد خلال المفاوضات السويسرية."</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79642" target="_blank">📅 20:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79640">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0500adc4.mp4?token=XKB7ETQD5vu0RDYXFOt4CX8g13gXFzPhhTkcTImPSCHDcgfpw_Df44iVDdTMBGMtgR1ut7fEOJhRRvgP7ddpUaSBy5D9hhmlGjLYfaiL5_8zeey9u3M60EXXsAgTH5FPU8F8qBg5FjLwGJuyWleHOduxE3N0l2Hd3RXD0aoqD5oyZokZyI0jxOCnChd500ABTvJjWDxjTTS-gKsQjYTx0ISDTA5LdcjrXlnaReYH5yDgTz-gTr3g61DpOJO4yuttNd3WZAhb-SaneFX7ihKIuFm7MAhu5uh6F-Wu6Aq4oHEQbkG7em0YAb3bbL-uZ3p5L6-rRJa9vcof9WqMkAb9gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0500adc4.mp4?token=XKB7ETQD5vu0RDYXFOt4CX8g13gXFzPhhTkcTImPSCHDcgfpw_Df44iVDdTMBGMtgR1ut7fEOJhRRvgP7ddpUaSBy5D9hhmlGjLYfaiL5_8zeey9u3M60EXXsAgTH5FPU8F8qBg5FjLwGJuyWleHOduxE3N0l2Hd3RXD0aoqD5oyZokZyI0jxOCnChd500ABTvJjWDxjTTS-gKsQjYTx0ISDTA5LdcjrXlnaReYH5yDgTz-gTr3g61DpOJO4yuttNd3WZAhb-SaneFX7ihKIuFm7MAhu5uh6F-Wu6Aq4oHEQbkG7em0YAb3bbL-uZ3p5L6-rRJa9vcof9WqMkAb9gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
حادثة إطلاق نار في مدينة مونتريال الكندية ؛ مقتل وإصابة عدة أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79640" target="_blank">📅 20:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79639">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4504a0ba.mp4?token=viRbTWU1GdX94xYQmsBUsUH4nwCuuFEIFv76Cm3b4oiFubIj8YayMKA1OnJNZTocgnCPn13O3Gu9SCoeb8vrAolQPaFkwjvkXNM3AzNgmLFr79V-dsGYuySAuhjz6uYaNjYrmZxAAbHnwpSeHKL-WA36PsdoKeKJ-EQKi7vzw1mpS82b-_anA3a9hCespUWYmQechbOQJEnJYu-66dKSYTOgpOp6K1I7_CG4OvUDBqelPW42mwXmeWQhqRiIA3wIXYjNEYhxJFrP_U-1NQ4GiTKI17DSRre-XZRvc5lmfan3Hpcd2xEynTiRlf9g12NyrpnoRlA6IrD04_CAtMZnPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4504a0ba.mp4?token=viRbTWU1GdX94xYQmsBUsUH4nwCuuFEIFv76Cm3b4oiFubIj8YayMKA1OnJNZTocgnCPn13O3Gu9SCoeb8vrAolQPaFkwjvkXNM3AzNgmLFr79V-dsGYuySAuhjz6uYaNjYrmZxAAbHnwpSeHKL-WA36PsdoKeKJ-EQKi7vzw1mpS82b-_anA3a9hCespUWYmQechbOQJEnJYu-66dKSYTOgpOp6K1I7_CG4OvUDBqelPW42mwXmeWQhqRiIA3wIXYjNEYhxJFrP_U-1NQ4GiTKI17DSRre-XZRvc5lmfan3Hpcd2xEynTiRlf9g12NyrpnoRlA6IrD04_CAtMZnPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
حادثة إطلاق نار في مدينة مونتريال الكندية ؛ مقتل وإصابة عدة أشخاص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/79639" target="_blank">📅 20:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79638">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
🇮🇷
رک و صریح..
مجالس عزاداری امام حسین (ع) در نجف اشرف همراه و در کنار جمهوری اسلامی ایران است.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79638" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79637">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭐️
نتائج إغلاق مضيق هرمز من قبل الجمهورية الإسلامية..رويترز:
انخفضت مخزونات النفط الخام في الاحتياطي الاستراتيجي للبترول الأمريكي بنحو 9.1 مليون إلى 331.2 مليون برميل الأسبوع الماضي، وهو أدنى مستوى منذ عام 1983.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79637" target="_blank">📅 19:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79636">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYxL12VYzCA5UHxRW_nkDdTdLyfNCMUsm4V2DWtAfnunb9pJVdeLxKa6v4oodnJvAPUqzRuNS6-9Jss4fbHc1ONCLsJpoGSuZ5pf81l9Nx2gsQ6D1IGQiblqEgORbfGez3iUovN2-6P_cac14YDPSBTzrhFFlamnqLjnfrriKW7bUkkQPWQCc6E-sCOBZrEAhnt4vJ-sU96ifE-fTkQ4Y_pLlkY_OhAE_nyiuV-nlFy9gTsHU6oyRAkTR6BEPdBenMmJDIeuA5erSLyk46x8NqqodEZbLcykQOioHGjNipaobChhsp5lvAtBCRXkCRrGBpk3C_Jjyo5kp6xHbST52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
⚔️
محلل سياسي مقرب من الحلبوسي  يتهم كتائب حزب الله وراء الهجوم على الحلبوسي   والصحفية منى سامي ترد : حزب الله ما يدز مسيرة مجرقعة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79636" target="_blank">📅 19:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79635">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
في ضوء التقرير المتعلق بتحذير رئيس جهاز الأمن العام الإسرائيلي (الشاباك) زيني بأن "اليوم السابع من أكتوبر المقبل سيكون في إيلات"، يُصدر الجيش الإسرائيلي تحديثًا: ستُجرى مناورة عسكرية صباح غدٍ في منطقة خليج إيلات. وكجزء من المناورة، ستشهد المنطقة تحركات مكثفة لقوات الأمن والسفن. لا يوجد ما يدعو للقلق من وقوع أي حادث أمني، وفي حال وقوع أي حادث فعلي، سيتم إبلاغ السكان من قبل قوات الأمن.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/79635" target="_blank">📅 19:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79634">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: "إنّ ادعاء نائب الرئيس الأمريكي بشأن عودة مفتشي الوكالة الدولية للطاقة الذرية إلى البلاد منافٍ للواقع وكاذب. لم يُذكر وجود مفتشين في البلاد خلال المفاوضات السويسرية."</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79634" target="_blank">📅 19:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79633">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الإيرانية: سيستمر تفاعل إيران مع الوكالة الدولية للطاقة الذرية وفقاً للإجراءات الحالية ووفقاً لموافقات مجلس الشورى الإسلامي وقرارات المجلس الأعلى للأمن القومي.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79633" target="_blank">📅 19:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79632">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
متداول: احالة الفريق ماهر والفريق محمد سكر والفريق هادي رزيج والفريق شاكر إلى التقاعد الوجوبي بأمر السيد القائد العام للقوات المسلحة الى جانب:  1- اعفاء اللواء عدنان حسن حمد قائد شرطة بغداد الكرخ من منصبه.  2- أعفاء اللواء شعلان علي صالح قائد شرطة بغداد الرصافة…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79632" target="_blank">📅 19:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79631">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الإيرانية:
سيستمر تفاعل إيران مع الوكالة الدولية للطاقة الذرية وفقاً للإجراءات الحالية ووفقاً لموافقات مجلس الشورى الإسلامي وقرارات المجلس الأعلى للأمن القومي.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79631" target="_blank">📅 18:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79630">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🌟
حزب الله:
من الميدان... ثَابِتون</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79630" target="_blank">📅 18:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79629">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
🇮🇶
سوالف الگهوة
تعين گريكور الأرمني سفير العراق بالولايات المتحدة الأميركية ؛ گريكور كان يشغل منصب مستشار السوداني</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79629" target="_blank">📅 17:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌐
خلل يضرب منصة X تويتر سابقا</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79627" target="_blank">📅 17:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تعطيل الدوام الرسمي في اقليم كردستان يوم الخميس بمناسبة يوم عاشوراء</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79626" target="_blank">📅 17:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nx1Jzp7uB3e7SdawmCK-wNWPWjJngnPZRbl4zCXOIHSeVLr-oH3L2DnGJHGxzOlL5u-gMoVS00pDRy30931Ti0fh6vdmv3gwnl4QipVB21aaAcpgv62lN8VeKEf1JZYqZW2Zd56PKprZXuavd2m2I2LWfi_HJPbMujMIWfLbCBhIUPWusiIFucQafrnPqdhXnsjBR90bhlO67pnOkj3tTNdIs5I9sm_Bga-YHbTDjyQ_buMT08z2FpiXUlF4tR0KKUPd5-CZTVaG6kKNjSnOCKgWIrwocqJ1MXGDHIfYVVMUEo6MDc8015XeVragZzasKatRRt99ZYNMvcX46u224g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انخفاض كبير في اسعار النفط بعد انباء عن نجاح الاجتماع الايراني الامريكي ليصل الى 77 دولار</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79625" target="_blank">📅 17:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌟
متداول:
احالة الفريق ماهر والفريق محمد سكر والفريق هادي رزيج والفريق شاكر إلى التقاعد الوجوبي بأمر السيد القائد العام للقوات المسلحة الى جانب:
1- اعفاء اللواء عدنان حسن حمد قائد شرطة بغداد الكرخ من منصبه.
2- أعفاء اللواء شعلان علي صالح قائد شرطة بغداد الرصافة من منصبه.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79624" target="_blank">📅 17:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
توجيهاتي واضحة ولم تتغير: مقاتلونا في جنوب لبنان يتمتعون بحرية كاملة في التحرك لصدّ أي تهديد مباشر أو محتمل لهم أو لسكان الشمال. لا توجد أي قيود على الجيش الإسرائيلي في هذا الشأن وسنبقى في المنطقة الأمنية في جنوب لبنان ما دام ذلك ضرورياً.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79623" target="_blank">📅 16:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزارة الخزانة الامريكية تصدر ترخيص لايران لبيع النفط الخام والمنتجات البتروكيماوية والمنتجات البترولية حتى 21 أغسطس 2026</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79622" target="_blank">📅 16:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزارة الخزانة الامريكية تصدر ترخيص لايران لبيع النفط الخام والمنتجات البتروكيماوية والمنتجات البترولية حتى 21 أغسطس 2026</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79621" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزارة الطاقة القطرية: إصابة 66 شخصاً</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79620" target="_blank">📅 16:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزارة الطاقة القطرية تعلن وفاة 13 شخصا في حادثة انفجار بمصنع في منطقة رأس لفان</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79619" target="_blank">📅 16:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزير الطاقة القطري: ما حدث في رأس لفان كان حادثاً وليس عدواناً أو تخريباً</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79618" target="_blank">📅 16:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزير الطاقة القطري: ما حدث في رأس لفان كان حادثاً وليس عدواناً أو تخريباً</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79617" target="_blank">📅 16:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">محافظة الديوانية تعلن تعطيل الدوام الرسمي يوم غد الثلاثاء بمناسبة ذكرى استشهاد أبي الفضل العباس (عليه السلام)</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79616" target="_blank">📅 16:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
القضاء العراقي:  ارتفاع حصيلة الأموال المضبوطة بقضية وكيل وزارة النفط لشؤون التصفية عدنان الجميلي والأطراف المتورطة معه لتصل إلى (10) ملايين دولار أمريكي و(31) مليار دينار عراقي. الجهود المستمرة أسفرت يوم أمس الأحد عن ضبط ما يقارب (20) مليار دينار عراقي كانت…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/79615" target="_blank">📅 16:11 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

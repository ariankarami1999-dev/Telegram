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
<img src="https://cdn4.telesco.pe/file/QPkPXIsZ4QVzlvpQO4s65V8EfCzzvPDWO6XRA89EGHII_WT_VwkNNGBTNsgJPE8I4uLRE4a-n2iVS_zUoYXUkd--Zd-qDdVDUp6Sih7CBuMc-AKqOR9v0Rf39PlYC8N3ZYq6dV0aMkYTa7ZIkTWc8IirUB8iRgpmDtCoZUjpNCOPlVJk_d_KKRWjfJE1JvIc0O3V2jDWqLogkYDv-_Jgbqc-nAMoQBL8mNrOwXleNDP-jE1JyXRq77uahguMno8QXX5JEwgyCKjNw9O9UX4tcwk6dO6dXCpz93Z30GojrSf0JU0pAgwpKv5nQcHkzSfl9XmW6Zp4fbxv361U5PLgXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 250K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 23:41:19</div>
<hr>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae667f98ea.mp4?token=kt2oqvZigLrNGX5AjfALHObL80YULkyBswzxJjecXpoJwv3-t_bI0igw6cIGNokJXbAGop1y-iECVCsnUP4MlfgTbvWBZxb0EnVQsu_1IasK1DtTM9qI7X5Nx0WxvP6N26x-fi0_DfGYZDcmobFZiy42oHvqTLuXv3kHP7KKqthU7n6-TU4wTj0RMvW83pDw_emk849ASMiXQzDma1NjH9RKaxDrIW_88gfxrGEn7BaQo4S0SPS_IaigJOBzz-foYv7hD5Jyqqgzg0iH6WFWS-ur5A9BD8wVd2zxu93wjFCn0DOKeXB48SdpoA6Ix3oZjutyGr2goUF9LHFM-U3E_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae667f98ea.mp4?token=kt2oqvZigLrNGX5AjfALHObL80YULkyBswzxJjecXpoJwv3-t_bI0igw6cIGNokJXbAGop1y-iECVCsnUP4MlfgTbvWBZxb0EnVQsu_1IasK1DtTM9qI7X5Nx0WxvP6N26x-fi0_DfGYZDcmobFZiy42oHvqTLuXv3kHP7KKqthU7n6-TU4wTj0RMvW83pDw_emk849ASMiXQzDma1NjH9RKaxDrIW_88gfxrGEn7BaQo4S0SPS_IaigJOBzz-foYv7hD5Jyqqgzg0iH6WFWS-ur5A9BD8wVd2zxu93wjFCn0DOKeXB48SdpoA6Ix3oZjutyGr2goUF9LHFM-U3E_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمليات التجارة البحرية البريطانية: تم إبلاغنا بوقوع اصطدام ثانٍ لسفينة الشحن في ميناء ام قصر العراقي مما أدى إلى اندلاع حريق تم إخماده. لم ترد أنباء عن إصابات بين أفراد الطاقم. يُنصح السفن بالعبور بحذر والإبلاغ عن أي نشاط مشبوه إلى عمليات التجارة البحرية البريطانية.…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/naya_foriraq/76680" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">إعلام العدو الأسئلة:  1. هل ستبقى قوات الجيش الإسرائيلي في مواقعها الحالية؟ 2. هل تستطيع "إسرائيل" مهاجمة أي تهديد ناشئ؟ 3. هل سيلتزم حزب الله بعدم الهجوم حتى لو تجدد إطلاق النار في إيران؟ 4. هل سيستمر تدمير القرى الشيعية في جنوب لبنان؟</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/naya_foriraq/76679" target="_blank">📅 23:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🌟
بنيامين نتنياهو:
تحدثت هذا المساء مع الرئيس ترامب وأخبرته أنه إذا لم يتوقف حزب الله عن مهاجمة مدننا ومواطنينا - ستهاجم إسرائيل أهدافًا إرهابية في بيروت.موقفنا هذا لا يزال ثابتًا.في الوقت نفسه، سيواصل جيش الدفاع الإسرائيلي العمل كما هو مخطط في جنوب لبنان.</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/76678" target="_blank">📅 23:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhojE8MHXFo7X2XW9szWB5z3Z0tx6UgxviZuq6t22CwRI4NOMWsFZB4h4zgDy4on_c02b1-yrYhrnUlauMrekHBN__hLsxOpoqUPsn0RgpIR8d21Yih0CrU9K5flBfHS8YKhe0B4ijdyINn_1xyhp-DyS5BQUZuMPSa2lbmFletSzcGUoBQhKiP2Us3yrnEU-3Ogy1tw69XX6BzQDQqSE2oJqFvijmX2msBQe5SwE-DxHo820x1ds2nLIQyKhlF0Czr1VTvS3tGWY1aSU_bnV_0ko33YROlzs9nnZkv83_L2zNw2Hsp_50Uo_QkOln2jz0aqerJwzY3LAbhQUgBVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصحافة الإيرانية في اول مانشيت لها
لن يكون ذلك أبداً من دون حزب الله» أو «أبداً بلا حزب الله»</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/naya_foriraq/76677" target="_blank">📅 22:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/76676" target="_blank">📅 22:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
🌟
تحديث  أصيب 7 جنود آخرين، من بينهم 4 ضباط، في الحادث. 3 منهم في حالة خطيرة، واحد في حالة متوسطة و3 في حالة طفيفة. من بينهم قائد وحدة شاكيد برتبة مقدم، اثناء معارك مع حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/naya_foriraq/76675" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a07ca0f04.mp4?token=CeD7elCx2C4RbKuvIZqCN8UMgV6W9m3tmBf3BFMynU9MU_A2VybCK8MH23tNX_OjM7o-2Iuu_gXAntkT-zLT6hfxcCmBexVM4g5C7w9hdO8p2BL1fyVFCFdSiMxOrVe2BlHuAD72c7Py8lAI2tGTahYJOxreEmLFFl3D4_Bn7vg14GZX5k7tWkBHWlAjJUkjS6Y7SSBIA3o-Ju-xTJc3sfIA-l9IjnIEbFfUbxlQZxUq_6M8YAKbrobf37Pm-nmaR5_C7vJ8c-jmXFW_onTCAGxaT8NW24fReu6H8xr60KLNLElDy7UKgvDq9iM9xZZkAEFwXaEcRLRK7BjxZ_w24XN6qizTKSpCtP856Wf3DQfAW31W64bdvLQPjDWYD8XmHFZ7OU6C_SgidiEQ26RfGLUl9g30FkOLvPYM8Jk5ie5ZpjcWT6Z7Sa_DBLxcdLQHhed1xSxRySctOOK0oZuJXamkY0m0WVnoynoJTjWfrowxwbHd8YFKDhwiKCYAUhb45B4lVofadhmthdOebiS0ZAH1eMLvQU_vuEuPrj3Ltitu4PWmkMEdTZYC7NjOH_m2b_b83yOxLS2ZUWwecpMOfABai5YEIOhJIGWHhRaUpSIuIJXkYV1eOV1x_s0DYiwCL397SUUCoJTjzYCma8Cg94AnS1PYa3R8x3oJyLKAUYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a07ca0f04.mp4?token=CeD7elCx2C4RbKuvIZqCN8UMgV6W9m3tmBf3BFMynU9MU_A2VybCK8MH23tNX_OjM7o-2Iuu_gXAntkT-zLT6hfxcCmBexVM4g5C7w9hdO8p2BL1fyVFCFdSiMxOrVe2BlHuAD72c7Py8lAI2tGTahYJOxreEmLFFl3D4_Bn7vg14GZX5k7tWkBHWlAjJUkjS6Y7SSBIA3o-Ju-xTJc3sfIA-l9IjnIEbFfUbxlQZxUq_6M8YAKbrobf37Pm-nmaR5_C7vJ8c-jmXFW_onTCAGxaT8NW24fReu6H8xr60KLNLElDy7UKgvDq9iM9xZZkAEFwXaEcRLRK7BjxZ_w24XN6qizTKSpCtP856Wf3DQfAW31W64bdvLQPjDWYD8XmHFZ7OU6C_SgidiEQ26RfGLUl9g30FkOLvPYM8Jk5ie5ZpjcWT6Z7Sa_DBLxcdLQHhed1xSxRySctOOK0oZuJXamkY0m0WVnoynoJTjWfrowxwbHd8YFKDhwiKCYAUhb45B4lVofadhmthdOebiS0ZAH1eMLvQU_vuEuPrj3Ltitu4PWmkMEdTZYC7NjOH_m2b_b83yOxLS2ZUWwecpMOfABai5YEIOhJIGWHhRaUpSIuIJXkYV1eOV1x_s0DYiwCL397SUUCoJTjzYCma8Cg94AnS1PYa3R8x3oJyLKAUYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الاسرائيلي يعلن مقتل الرائد د. أوري يوسف سيلفستر  ، عمره 30 عامًا، من تل أبيب، طبيب كتيبة شكد (424)، لواء جبعاتي بمسيرة من حزب الله.</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/naya_foriraq/76674" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
🌟
أصيب ستة مقاتلين، من بينهم ضابطان ومقاتل في حالة خطيرة، اثناء معارك مع حزب الله جنوب لبنان.</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/76673" target="_blank">📅 22:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الاسرائيلي يعلن مقتل الرائد د. أوري يوسف سيلفستر  ، عمره 30 عامًا، من تل أبيب، طبيب كتيبة شكد (424)، لواء جبعاتي بمسيرة من حزب الله.</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/76672" target="_blank">📅 22:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHh4DFTl2TTKGOSwui3G5HIxJ28dUF9Ubsa8_RsBoBKC_T1snQIarB5oN8J3aqTujIE-MgZTuTYuDQU95Ob6QN5niWJIuOcabq4yHCrXmOif0WXTicC3_FBpt1l8LRExat5PsmOmd3jUR2SetJD9VTpROZ8pDzlxso3W3kdiWPFV4Cu1_sOaudQQd0zon2ARAEztYblKNTKOH-6DF6ejfarfv2opy5VgVFZAlmJOOuAyzS69uJmSCxlOCBmNB3v6nwa7WeBN9zXtjEE1G1hFUCTmoI1oiHvMW4ZMvFO9WpnHAq5tfQJl8zAdxRlIb0xxS11nmCp3QVQdLCV49TKjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المتحدث باسم جيش العدو : مقتل جنديين في جنوب لبنان</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/76671" target="_blank">📅 22:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بن غفير: سيدي رئيس الوزراء، لقد حان الوقت لنقول لصديقنا، الرئيس ترامب: «لا».</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/naya_foriraq/76670" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brop0TfEeN_WnUFfBIPIfTg2Eu8Ef7PQSiqly-_YONksO44D-Tw-fvXL1O5mpECCvxTUjRpncJUkdzp-_1r0mx7jQsb_lw5-iofk-NBYBjxfHmu0IqLl0afbD9fXI-0hj5vichKX9dpWY0Q0rh3-2irhxaPBRk9DqLdjFuwINVwjVsJDXENQBkw-d0X2q4SwfLeHFAQ4NG8VD6pYWz9kQ6iyH2Yf7MDRY4cW8ztLFbdCsPLboyjMu5gZbiY-1XaRWXQlugrpRoIUBlcjeMQuLgGlhFR-C7ruTH2PyEZmMHHaoqVgB3ViG5pIhW2GjpYsCilCM5C34OYs3JMSfMYhIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مؤسسة إدارة الممرات المائية في الخليج الفارسي:
‏منذ أن بدأ الكيان ⁧ العمل في أوائل شهر مايو، أرسلت أكثر من 300 سفينة غير إيرانية معلومات للحصول على إذن بالمرور الآمن عبر ⁧ مضيق هرمز ، ومعظمها كانت ناقلات نفط.</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/76669" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">زعيم المعارضة الإسرائيلية "يائير لابيد": إسرائيل تحت الوصاية الأمريكية الكاملة.</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/76668" target="_blank">📅 21:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عمليات التجارة البحرية البريطانية:
تم إبلاغنا بوقوع اصطدام ثانٍ لسفينة الشحن في ميناء ام قصر العراقي مما أدى إلى اندلاع حريق تم إخماده. لم ترد أنباء عن إصابات بين أفراد الطاقم. يُنصح السفن بالعبور بحذر والإبلاغ عن أي نشاط مشبوه إلى عمليات التجارة البحرية البريطانية. السلطات تُجري تحقيقًا.</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/naya_foriraq/76667" target="_blank">📅 21:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بينيت: لقد فقدت الحكومة السيطرة على السيادة الإسرائيلية.    ليبرمان: هذا ليس رئيس وزراء - إنه دمية.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/76666" target="_blank">📅 21:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">إعلام العدو الأسئلة:  1. هل ستبقى قوات الجيش الإسرائيلي في مواقعها الحالية؟ 2. هل تستطيع "إسرائيل" مهاجمة أي تهديد ناشئ؟ 3. هل سيلتزم حزب الله بعدم الهجوم حتى لو تجدد إطلاق النار في إيران؟ 4. هل سيستمر تدمير القرى الشيعية في جنوب لبنان؟</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76665" target="_blank">📅 21:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 30-05-2026
دبّابة ميركافا جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76664" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صحيفة "معاريف" العبرية:
في الساعات الأخيرة جرت مناقشة في المؤسسة الأمنية الإسرائيلية حول امتلاك حزب الله لمحلقات مفخخة مجهزة بكاميرات رؤية ليلية.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76663" target="_blank">📅 21:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚠️
إلى المستوطنين في شمال فلسطين المحتلة، المنطقة التي تضم: الجليل الأعلى الجليل الأسفل الجولان وحيفا إنذارٌ عاجلٌ سيصدر قريبًا، ترقّبوا. يتبع  ️ ️ אל המתיישבים בצפון פלסטין הכבושה, האזור הכולל: הגליל העליון הגליל התחתון הגולן וחיפה אזהרה דחופה תפורסם בקרוב…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76662" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">إعلام العدو الأسئلة:  1. هل ستبقى قوات الجيش الإسرائيلي في مواقعها الحالية؟ 2. هل تستطيع "إسرائيل" مهاجمة أي تهديد ناشئ؟ 3. هل سيلتزم حزب الله بعدم الهجوم حتى لو تجدد إطلاق النار في إيران؟ 4. هل سيستمر تدمير القرى الشيعية في جنوب لبنان؟</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/76661" target="_blank">📅 21:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">إعلام العدو الأسئلة:  1. هل ستبقى قوات الجيش الإسرائيلي في مواقعها الحالية؟ 2. هل تستطيع "إسرائيل" مهاجمة أي تهديد ناشئ؟ 3. هل سيلتزم حزب الله بعدم الهجوم حتى لو تجدد إطلاق النار في إيران؟ 4. هل سيستمر تدمير القرى الشيعية في جنوب لبنان؟</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/76660" target="_blank">📅 21:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbNQWYc_GAJZeehYjU7aqRvqoStX_l78T5-K0T7kCQRW6zK5mc6H1hTVqXrsGId1wR-2XtzDD55YAXhBkr_ALBUfssajvp4ui6PBQn8Zr-MBcqlXkTsZVppzY9xl2MQi9E7g9amRhyv-erajkw7N85bVteuaL6cQvfCrSAG39Frh9PI7KWyqQH9h0p5JWjbbMKpy8iII5QzCRQJ4FoMJRiLWcBdcqExflGvXs5j-gjcgP4LRCFXFzpOyRmaTuAZzGbtZ4Nj7Rit24-JUqRfuohGu0uV462njHFhWmAostUkezJ9ZEOGx7z_I-darCYdHsnro9PLWcPZxYTM7QtraCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المحور يعيش اقوى حالته منذ قيام الثورة الإسلامية في ايران
لكن البعض ترك الباص ونسى هذا العز ، تهديد خاتم الأنبياء جعل اقوى دولتين تتراجع عن مهاجمة مجموعة شيعية لا حول ولا قوة لها إلا بعزة الله ورسوله .. افيقوا يرحمكم الله</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/76659" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1ElGGrqsDRTRLirihfJzlZG-DN0g0oY6KIicjf2Zn2cTwngCLPEPlCiQ0KJbcA8pGVPaS5zsME_jwExzNydmB-ggrfGQd9_b9P_OLyJmYCmeDIzvoP8BPkuG2Wp_YuGUgAVvvD2zxtYZ-MBZv23sd34gNmBLYsU_4bTwlOoKeEnvKzqVcqOcfgjZC4w-hOD5i-jgUPcGm7gyw2B5_8abyakgvFZ0vMsrs4SQdCD3krxFfQWUPnObKzG5JFvNYKrPC4bzA5ETMbYn--Dm_Q3tfR4qixdFhQW73m7BN_vCVk7Bffi1QG5g488DQ2tnPbYYNVaBHeYXtQzOlmazlEchQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: المحادثات مستمرة، بوتيرة سريعة، مع
جمهورية إيران الإسلامية
. شكرا لك على اهتمامك بهذه المسألة!</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76658" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">إعلام العدو الأسئلة:
1. هل ستبقى قوات الجيش الإسرائيلي في مواقعها الحالية؟
2. هل تستطيع "إسرائيل" مهاجمة أي تهديد ناشئ؟
3. هل سيلتزم حزب الله بعدم الهجوم حتى لو تجدد إطلاق النار في إيران؟
4. هل سيستمر تدمير القرى الشيعية في جنوب لبنان؟</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/76657" target="_blank">📅 21:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">يبدو ان مجموعة في حزب الله تقاتل بنظام الفيلق   أطلقت الان رشقة نحو الجليل</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/76656" target="_blank">📅 21:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامب: لقد أجريت مكالمة مثمرة للغاية مع رئيس الوزراء بيبي نتنياهو، من إسرائيل، ولن تكون هناك قوات تذهب إلى بيروت، وأي قوات في طريقها، قد أعيدت بالفعل. وبالمثل، من خلال ممثلين عاليين، أجريت مكالمة جيدة جدا مع حزب الله، واتفقوا على أن جميع عمليات إطلاق النار…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76655" target="_blank">📅 21:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76654">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/76654" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/76654" target="_blank">📅 21:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kylWdbd2E18OsHzHcJc1K5J-nI4YtBVnSGu6o8Zfzkl0psLoZxoHYqF0top4HPVl9Psv8iz3n_JzhZHj9VIGASAkuqkTvYtN6ncTi4R653AjebJ2pv5OS7TbDp-FOoef90pqfJ9PRd7ZrlLNL1wpFFD7UPPueiI3H9qTsteXxFlNhzrbYWT48Jaq_SPVplxoDJEIsOefotw298LHg5u45RObZVrG3I4rXmArBsP3m2enRvF33AKa_cmTZGfEB2oQs3-pyYZxlEL9C3YUyFrSwdWU88EJOhjleWR6Kq6Tfkgb38V34jeqV-20lHzFnMLsOp9d8b9hvKUQBvUtu6Fxgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا : العراقيون جاهزون لمواجهة العدوان على الضاحية .</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76653" target="_blank">📅 21:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامب: لقد أجريت مكالمة مثمرة للغاية مع رئيس الوزراء بيبي نتنياهو، من إسرائيل، ولن تكون هناك قوات تذهب إلى بيروت، وأي قوات في طريقها، قد أعيدت بالفعل. وبالمثل، من خلال ممثلين عاليين، أجريت مكالمة جيدة جدا مع حزب الله، واتفقوا على أن جميع عمليات إطلاق النار…</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/76652" target="_blank">📅 21:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامب: لقد أجريت مكالمة مثمرة للغاية مع رئيس الوزراء بيبي نتنياهو، من إسرائيل، ولن تكون هناك قوات تذهب إلى بيروت، وأي قوات في طريقها، قد أعيدت بالفعل. وبالمثل، من خلال ممثلين عاليين، أجريت مكالمة جيدة جدا مع حزب الله، واتفقوا على أن جميع عمليات إطلاق النار…</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/naya_foriraq/76651" target="_blank">📅 21:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامب: لقد أجريت مكالمة مثمرة للغاية مع رئيس الوزراء بيبي نتنياهو، من إسرائيل، ولن تكون هناك قوات تذهب إلى بيروت، وأي قوات في طريقها، قد أعيدت بالفعل. وبالمثل، من خلال ممثلين عاليين، أجريت مكالمة جيدة جدا مع حزب الله، واتفقوا على أن جميع عمليات إطلاق النار…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76650" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامب: لقد أجريت مكالمة مثمرة للغاية مع رئيس الوزراء بيبي نتنياهو، من إسرائيل، ولن تكون هناك قوات تذهب إلى بيروت، وأي قوات في طريقها، قد أعيدت بالفعل. وبالمثل، من خلال ممثلين عاليين، أجريت مكالمة جيدة جدا مع حزب الله، واتفقوا على أن جميع عمليات إطلاق النار…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/76649" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامب: لقد أجريت مكالمة مثمرة للغاية مع رئيس الوزراء بيبي نتنياهو، من إسرائيل، ولن تكون هناك قوات تذهب إلى بيروت، وأي قوات في طريقها، قد أعيدت بالفعل. وبالمثل، من خلال ممثلين عاليين، أجريت مكالمة جيدة جدا مع حزب الله، واتفقوا على أن جميع عمليات إطلاق النار…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76648" target="_blank">📅 21:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76647">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR0EZWYNGraYQPw2VmQEiu6tP_uIe2Kj2BTFfeI8ca3tVDpKFSQGU1vtmJIwDBWtHRGvwrHYbYADvNz-qvCm5h688XlPz9gedj63050zofhiNnPW56rRWuGC70FExi3K_s02Ukxfm4PKoN47vOBTxGFVO8AFDTi4uw12BMZS7IFuVysAYXPhgbOOw-QwDJfgupWTRcNCi8u033Y020TkX7a9k11bnEpGsaXXsWzHEVcrtgzhJO99PZJqQtusyrXQYKf8lnZgwNi8uq0nBbfHN85tGXC9hb9K-HKi_elw5pmCeOpm7F41LJg0DaCDD5LzWEs1jxIlJRqRC7qdIMYSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: لقد أجريت مكالمة مثمرة للغاية مع رئيس الوزراء بيبي نتنياهو، من إسرائيل، ولن تكون هناك قوات تذهب إلى بيروت، وأي قوات في طريقها، قد أعيدت بالفعل. وبالمثل، من خلال ممثلين عاليين، أجريت مكالمة جيدة جدا مع حزب الله، واتفقوا على أن جميع عمليات إطلاق النار ستتوقف - وأن إسرائيل لن تهاجمهم، ولن يهاجموا إسرائيل.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76647" target="_blank">📅 21:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76646">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">הוראת פינוי מיידית  לתושבי ההתנחלויות בצפון פלסטין הכבושה נמסר כי האזור המסומן במפה המצורפת, הכולל את הגליל העליון, הגליל התחתון, רמת הגולן וחיפה, מוגדר מרגע זה כאזור צבאי סגור. במקרה שמנהיגיכם הפושעים יתקפו את הדאחייה הדרומית של ביירות או את העיר ביירות,…</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/naya_foriraq/76646" target="_blank">📅 21:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76645">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc8QH5FQ9l1xnZkpM5Uy_zmj05QaLxo_dzeCOqcq6AUCdMcgOPBa-8_NLXHJIe41jXcbU1szMh6JDr87lJllw6Zh-ei1OvBRhqvbX-usQFfnNHRF_cvjiPQyHBsX8wcdgtPrvGXf-jV5WX-sfnsJfptvUkJ1Qwg5K7YcI-oFM6FdXnGj0oAoMMEhCt4GMgUQNu54jClNW4_tUWMgxirePijZzNYDINmGDNmA9DK-n7e0dcUaC2OmG_nMT1N2ucasZm_UpOCOiNoBfPiNUmcsQsxuPszmf3WYD-gcKvLCPtjBCrZ42PFbs4uYPnMxeEmntlQ2aN6uD1NFOYFhGx5rOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/76645" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76644">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">הוראת פינוי מיידית  לתושבי ההתנחלויות בצפון פלסטין הכבושה נמסר כי האזור המסומן במפה המצורפת, הכולל את הגליל העליון, הגליל התחתון, רמת הגולן וחיפה, מוגדר מרגע זה כאזור צבאי סגור. במקרה שמנהיגיכם הפושעים יתקפו את הדאחייה הדרומית של ביירות או את העיר ביירות,…</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/76644" target="_blank">📅 20:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76643">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📰
رويترز:
إسرائيل تنتظر الموافقة النهائية من ترامب على أي عملية في الضاحية الجنوبية لبيروت</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/76643" target="_blank">📅 20:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76642">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0noSfaWoL61FkMiI-MlJLtXNryCOJtM6kYQA7r7vvOJ6tE0jBKt7R4_TGBmHtQUhn1hYhLXO0kvEjGJEvA9IkdUjN63YDguWFrSqvAwkFltjGHG3BEL-zU24jDOmED6FQeQDoEgUBr3PkUQ-3F5xjk1706yLgO8NKhswj3n2Hz90sCxt1RFF7HnMM_CQB27gY2x6f94lYFxQprTsU4_7u0F47E0gVUDcIzFlP1ulABK_vLCEYNXbg4pnxQKHfuLxe4mDYxhAYj_U5rP5Ibaw7EqWvskFMFxQavZQitCShueXum7UL69shRIVx2wi0ZzNuKyYv_4174-PY2LAiQS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
إلى المستوطنين في شمال فلسطين المحتلة، المنطقة التي تضم: الجليل الأعلى الجليل الأسفل الجولان وحيفا إنذارٌ عاجلٌ سيصدر قريبًا، ترقّبوا. يتبع  ️ ️ אל המתיישבים בצפון פלסטין הכבושה, האזור הכולל: הגליל העליון הגליל התחתון הגולן וחיפה אזהרה דחופה תפורסם בקרוב…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/76642" target="_blank">📅 20:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76641">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚠️
إلى المستوطنين في شمال فلسطين المحتلة، المنطقة التي تضم:
الجليل الأعلى
الجليل الأسفل
الجولان
وحيفا
إنذارٌ عاجلٌ سيصدر قريبًا، ترقّبوا.
يتبع
️ ️ אל המתיישבים בצפון פלסטין הכבושה, האזור הכולל:
הגליל העליון
הגליל התחתון
הגולן
וחיפה
אזהרה דחופה תפורסם בקרוב, היו בכוננות.
המשך יבוא</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/76641" target="_blank">📅 20:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76640">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">المتحدث باسم جيش العدو : مقتل جنديين في جنوب لبنان</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/76640" target="_blank">📅 20:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76639">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
ترامب لـ CNBC: لا يهمني أن تنتهي محادثات السلام مع إيران.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/76639" target="_blank">📅 20:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
ترامب لـ CNBC:
لا يهمني أن تنتهي محادثات السلام مع إيران.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/76638" target="_blank">📅 20:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBModyBnDnHqf5TGaNoDN6xeBQT86MbTIn4bL829cR9AxYVoGD6A4w9wKAyGSeDNGhntbaCgkDVTD1lEdjt_qp1PloS8cnkdASrG17MKApjJuQ-3WB0hfQXHKQZ6c9laKGBhZZXobIIQLTru1glTwf4cJFyl9DiH8xrWBQEsHdK3IvnHwUt8hPKNsD5TFfc647s508jwXvZ0-g6YuQEbH1OHE0oVZzJsXQW2Wa2kWGvJ3G3fJdVF15hDhegVuk7H_BJeIz1Ju6vbGKNtwH1-Hfdm3Ya9FzHym8BYj4S6d_DbaGaHdDcEw_dmsBkKGJrxncK3gwfnaIsxe5dYN66OUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية:
تُذكّر وزارة خارجية الجمهورية الإسلامية الإيرانية، في معرض حديثها عن اتفاق وقف إطلاق النار المؤرخ في 8 أبريل/نيسان 2026، والذي أوقف الحرب التي فرضتها الولايات المتحدة والكيان الصهيوني على الجمهورية الإسلامية الإيرانية على جميع الجبهات، بما فيها لبنان، بأن الولايات المتحدة، منذ إعلان وقف إطلاق النار في 8 أبريل/نيسان، ارتكبت انتهاكات صارخة ومتكررة لوقف إطلاق النار، بما في ذلك هجمات متواصلة على السفن التجارية الإيرانية. وفي الوقت نفسه، انتهك الكيان الصهيوني، بانتهاكه الصارخ لوقف إطلاق النار، وحدة أراضي لبنان وسيادته الوطنية، مما تسبب في استشهاد وإصابة آلاف اللبنانيين، وتشريد مليوني شخص، وتدمير البنية التحتية للبلاد ومنازل المواطنين. ويُعدّ انتهاك وقف إطلاق النار على أي من الجبهات انتهاكاً له. إنه موجود على جميع الجبهات.
على الرغم من الجهود المعلنة التي بذلتها الولايات المتحدة في الأيام الأولى التي أعقبت وقف إطلاق النار لإجبار الكيان الصهيوني على وقف عدوانه على لبنان، فإن المسؤولية المباشرة للولايات المتحدة واضحة، سواء في انتهاك وقف إطلاق النار ضد إيران أو في انتهاك الكيان الإسرائيلي لوقف إطلاق النار ضد لبنان، وتقع مسؤولية آثار وتداعيات هذا الوضع على عاتق الولايات المتحدة. وقد حذرت الجمهورية الإسلامية الإيرانية مرارًا وتكرارًا من العواقب الوخيمة لانتهاكات وقف إطلاق النار على السلام والأمن الإقليميين، ودعت إلى وضع حد لهذه العدوان والجرائم. ومن البديهي أن الجمهورية الإسلامية الإيرانية ستدافع عن مصالحها بكل قوتها وباستخدام جميع إمكانياتها، انطلاقًا من حقها الأصيل في الدفاع المشروع، أينما رأت ذلك ضروريًا.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76637" target="_blank">📅 20:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXBkbcwAFwb1jW5tC0K2yvTt4cZaWDrSopvkeJ1redoeJaYNA1UOnD9r95deqBFWB5_P8datdePgfpMIHJEyijLDLStYlD79DxyWn38bzbK3kcvBe-j3vU04X-rv8moet2Pv3TC1DJ1KzoSL2p13WuQLtJD0sxAEA09ksmeCK4jp5mtdHRoxy45BSEu0HjGIAJNUk00p_ZYLj0j1CPbhaiLm3uB8HgqA2KiVsrC0sUUjT4Xh2YIR2ewK4qaGydlKMqQSvZpIvenqfC8KHsScv8VcAqNZvYYuT_UjQJPYmzI4-L4McpfjK0rwGptDgWyE71wqG1NL-PhFQ-1fAZl57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقلا عن وزير الاتصالات العراقي : يعلن إعفاء فرحان الفرطوسي من منصب مدير موانئ العراق</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76636" target="_blank">📅 20:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اعلام العدو: ‏تأجل حفل تعيين رئيس جديد للموساد بسبب مكالمة هاتفية بين  نتن ياهو والرئيس الأمريكي دونالد ترامب.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/76635" target="_blank">📅 20:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نقلا عن وزير الاتصالات العراقي : يعلن إعفاء فرحان الفرطوسي من منصب مدير موانئ العراق</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76634" target="_blank">📅 19:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامب: هذا لا يعني أننا سنبدأ بإلقاء القنابل. سنلتزم الصمت.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76633" target="_blank">📅 19:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامب عن إيران: إذا كنت تريد معرفة الحقيقة، أعتقد أننا نتحدث كثيرًا. أعتقد أن الصمت سيكون أفضل بكثير. لم اتلقى أي أخبار تفيد بتعليق المحادثات مع إيران.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76632" target="_blank">📅 19:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامب عن إيران:
إذا كنت تريد معرفة الحقيقة، أعتقد أننا نتحدث كثيرًا. أعتقد أن الصمت سيكون أفضل بكثير. لم اتلقى أي أخبار تفيد بتعليق المحادثات مع إيران.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76631" target="_blank">📅 19:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزارة الدفاع الكويتية تحذر من اصوات انفجارات كبيرة خلال الساعات المقبلة بسبب بقايا صواريخ إيرانية</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76630" target="_blank">📅 19:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beea9f2f7.mp4?token=Ewwq2yJB52hCwD-Hnib9vk22lFUGwwZsi9XI-Cs7faGwxXImLAJ_f7i2qK8_bZ_zIgkkpMhF9c_A3CmwBVJXrTGat1mkEAue6IEj8dnfsof6Gb7TW88CJdyrIZZrD3vyqJV2CViiRmDw0OXqqV_4N137qer1pRQXuPod-eTObV9y6CKqi10qqG3epIiqEPGJwgZb4Zb9Y8oefsa2pqX5vWYrPZKIetrD-jbETVxMGt1EDByuR69Ao277x6CvmIfTH7bH_bTKLUBGtK0LbX7mr9SHWtC59dMOiStoH7VzHqgJY_XiOotSx0yn_Dm5ZWr3X0KNA8VPXQtQOnKi2U6iqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beea9f2f7.mp4?token=Ewwq2yJB52hCwD-Hnib9vk22lFUGwwZsi9XI-Cs7faGwxXImLAJ_f7i2qK8_bZ_zIgkkpMhF9c_A3CmwBVJXrTGat1mkEAue6IEj8dnfsof6Gb7TW88CJdyrIZZrD3vyqJV2CViiRmDw0OXqqV_4N137qer1pRQXuPod-eTObV9y6CKqi10qqG3epIiqEPGJwgZb4Zb9Y8oefsa2pqX5vWYrPZKIetrD-jbETVxMGt1EDByuR69Ao277x6CvmIfTH7bH_bTKLUBGtK0LbX7mr9SHWtC59dMOiStoH7VzHqgJY_XiOotSx0yn_Dm5ZWr3X0KNA8VPXQtQOnKi2U6iqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تظاهرات واحداث شغب في الكيان بعد اطلاق يهود الحريديم تظاهرات غاضبة اغلقت الطرق والقطارات واشعلت الاطارات في الشوارع احتجاجًا على اعتقال المتخلفين عن الخدمة العسكرية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76629" target="_blank">📅 19:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">الخطوط الجوية العراقية: رحلاتنا إلى بيروت متوقفة حالياً بسبب الظروف الأمنية والأوضاع السائدة في المنطقة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76628" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
🏴‍☠️
القيادة المركزية لمقر خاتم الأنبياء تحذر سكان الأراضي المحتلة:
نتنياهو، الذي يواصل أعماله الشريرة في المنطقة، هدد بقصف الضاحية وبيروت، وأصدر تحذيراً بالإخلاء لسكانها. نظراً لانتهاكات النظام المتكررة لوقف إطلاق النار، فإننا نحذر سكان المناطق الشمالية والمستوطنات العسكرية في الأراضي المحتلة، في حال تنفيذ هذا التهديد، بضرورة مغادرة المنطقة فوراً حفاظاً على سلامتهم.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76627" target="_blank">📅 19:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">المتحدث باسم جيش العدو : مقتل جنديين في جنوب لبنان</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76626" target="_blank">📅 18:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76625">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 31-05-2026
نقطة تموضع جنود وآلية هامفي تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقتي
ابابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76625" target="_blank">📅 18:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76624">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">إذاعة جيش العدو: انفجار محلّقة مفخخة داخل موقع عسكري في رأس الناقورة بالجليل الغربي.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76624" target="_blank">📅 18:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76623">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇬🇧
الجيش البريطاني يعلن عن مقتل أحد أفراده  في شمال العراق خلال حادث تدريبي (حسب وصفهم).</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76623" target="_blank">📅 17:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇬🇧
الجيش البريطاني يعلن عن مقتل أحد أفراده  في شمال العراق خلال حادث تدريبي (حسب وصفهم).</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76622" target="_blank">📅 17:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭐️
إنفجار مجهول في الباخرة الأجنبية العملاقة MSC SARISKY V في خور عبد الله بعد إكمال تفريغ حمولتها في ميناء أم قصر جنوبي العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76621" target="_blank">📅 17:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76620">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxVLOC3DC7-GXKs8HsuPmv6vaAv9c6Q0FT3fvqtTZxkjMupNXQe-_01Wc3YyqkZW7GCnfEwY-RRL6NEwBHQvcl70RJmjNMw5ieEtCeQho8zC4CqYg2oqGktR1NoQ6MnwtlFzzdC53YT6VEGNLUdsMd8PIDTLhvjkDaJkwfyn-8xs6MpKknJwK_Q1ekQqxu6oHd_FfVIx5jaQP6vP5XqeKpIMwBkAcdoP76sA0GsyXrXDUDlc-2xCmx_kGo-Hs-XIVMZ4zcunFjvWePTJnL-i0G9EXys8vY0mRXvRl7hh8sQaKaI22aaptfS8Xca2Uf0wmKxzY2IDqQi-H19q5oosQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط العالمي تبدأ التحليق بعد إعلان إيران وقف المفاوضات والتهديد بإغلاق مضيق هرمز وباب المندب.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76620" target="_blank">📅 17:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🏴‍☠️
إنذار إخلاء من جيش الاحتلال للضاحية الجنوبية ببيروت.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76619" target="_blank">📅 17:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f9941fa3.mp4?token=EP1NHEpdeVnzBjsS62ONX7Z1KC_70odZHNSQpnvpoFZ68nwSjZVcxuFat8p7c0Vulvms7c7MFVk9NlX3lCT5TssNe5CHzfXxr02jWRTa9ZPWFafxqsTiKBdYgLWzUzzxUkUmBuAafi9umAbEx3m3WzVX58Von-6l4S4QiBdRZ6PnD8z1_Q4xC9Ncwnkq-Vb-9Xf_J-rSNkXkMd9dKPjVb_ypPgstYRkuWBBse1oNUNv-7YkjlgjggQqxF68RiMYJXqZURoNxdDk9oyYhL0g8kBXthef_mQczbe9I9eu5tIeP1GwYTVA2bnocJw2VQl_KSa0eEgQu-1WAZKBOcBdImzpSk8OYLbBIXKG9p_rXsm1uwRKYpSj_shiwEZrUVA9fgMvYXmy3zZyuIAW6nsOKKafvZ_qrlSFyqdU6pXRSIE1g6wqJWzdzICQgc7XYhFsr4zG2VPCzitV7fdeWQuo8lgiAK5i9xPUYUXLB7H08Jk5glEIN8m1YWdH1gcDDVKutI1HTkZCgnnHQ7bI81nMWTg9_OMYeJs9ub6MGId0hkm8ynGbZGiekLa3OvSCBKDMP6NGVGIghAQQdbT8N7ZbakvsXWTmFgV-JF1hfH1lk4qHkiAJ4M1cnR2kUsaZ2SGPcX3L-nEnl3FBkq7vtaZq0j3zX3X2ZTs6x5IEMdkSuGf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f9941fa3.mp4?token=EP1NHEpdeVnzBjsS62ONX7Z1KC_70odZHNSQpnvpoFZ68nwSjZVcxuFat8p7c0Vulvms7c7MFVk9NlX3lCT5TssNe5CHzfXxr02jWRTa9ZPWFafxqsTiKBdYgLWzUzzxUkUmBuAafi9umAbEx3m3WzVX58Von-6l4S4QiBdRZ6PnD8z1_Q4xC9Ncwnkq-Vb-9Xf_J-rSNkXkMd9dKPjVb_ypPgstYRkuWBBse1oNUNv-7YkjlgjggQqxF68RiMYJXqZURoNxdDk9oyYhL0g8kBXthef_mQczbe9I9eu5tIeP1GwYTVA2bnocJw2VQl_KSa0eEgQu-1WAZKBOcBdImzpSk8OYLbBIXKG9p_rXsm1uwRKYpSj_shiwEZrUVA9fgMvYXmy3zZyuIAW6nsOKKafvZ_qrlSFyqdU6pXRSIE1g6wqJWzdzICQgc7XYhFsr4zG2VPCzitV7fdeWQuo8lgiAK5i9xPUYUXLB7H08Jk5glEIN8m1YWdH1gcDDVKutI1HTkZCgnnHQ7bI81nMWTg9_OMYeJs9ub6MGId0hkm8ynGbZGiekLa3OvSCBKDMP6NGVGIghAQQdbT8N7ZbakvsXWTmFgV-JF1hfH1lk4qHkiAJ4M1cnR2kUsaZ2SGPcX3L-nEnl3FBkq7vtaZq0j3zX3X2ZTs6x5IEMdkSuGf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
31-05-2026
تجمّع لجنود جيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76618" target="_blank">📅 17:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76617">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17494497c8.mp4?token=OV3dEUytzm4mJ3cw2S9GGh7M6NKu31YYe_3LTHM9tnXFaPoOk0oKZH7m-DQ-Di93Xzp12VJiOyCINwOm2pTmmHujKEthc5J-kIYjTs9jZyiRjtpvfM_IKvjgknZEp0qMAalZR4cMm7EqBhMN1aE_JnFstyBl8aZhPtut7TvBq3fkmI8hM9zu1L1g2KAJFNQ21L1pAk6XRuivOWkGCvH5GyWOXVHBER16-BebOSsM7DVvD4rdMxbdgnmIxzSvrK8yWP9-axKZNMdJTGlcg4v5DDAz31c-wnO87qi3KNw253NqNMLlLuqVZQCflix9m4MzOhKsVvBBi5jt72LrgmX_0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17494497c8.mp4?token=OV3dEUytzm4mJ3cw2S9GGh7M6NKu31YYe_3LTHM9tnXFaPoOk0oKZH7m-DQ-Di93Xzp12VJiOyCINwOm2pTmmHujKEthc5J-kIYjTs9jZyiRjtpvfM_IKvjgknZEp0qMAalZR4cMm7EqBhMN1aE_JnFstyBl8aZhPtut7TvBq3fkmI8hM9zu1L1g2KAJFNQ21L1pAk6XRuivOWkGCvH5GyWOXVHBER16-BebOSsM7DVvD4rdMxbdgnmIxzSvrK8yWP9-axKZNMdJTGlcg4v5DDAz31c-wnO87qi3KNw253NqNMLlLuqVZQCflix9m4MzOhKsVvBBi5jt72LrgmX_0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إيران توقف تبادل الرسائل مع أمريكا احتجاجًا على الجرائم الصهيونية وتهدد بفتح جبهات أخرى وإغلاق مضيق هرمز بالكامل.  نظرًا لاستمرار جرائم الكيان الصهيوني في لبنان، ولأن لبنان كان أحد الشروط المسبقة لوقف إطلاق النار، ولأن هذا الوقف قد انتُهك…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76617" target="_blank">📅 17:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏴‍☠️
إعلام العدو يعلن عن مقتل جندي صهيوني وإصابة أخرين بعد دكهم بطائرة انقضاضية على أيدي أبناء نصرالله بجنوب لبنان.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76616" target="_blank">📅 17:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfebVJ9SbaUmF8U-aJVpJXafsnmrO1mQGJxPoa0LjCsPabB2UsGkwBsJHXVqjTb9pDsOq0jepumwwntlg48WmkJlO_X7xfXnvjOd5qsFqdt6ye-fFe3WJqn6g7trAVhbEvHqXo3wvvrX_LwLf-0M7np0zbYzyzxI1SjSVDtuL1EZ57gW4g_I6ef1N0DRxYJriDKpd9l-rpEMmAs95biU6cXk49_cyzBvy0TaR8d2tzovQpX3YWPmyU1NlroL45gh7CFrkRRkC0He27sdSFWJ-h7dhlTiD6Jb8ORU__rVVQ0vcVhmxPhVvbooYpvgWCpvMQQtdJkZbFJIfyjEYax9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إيران توقف تبادل الرسائل مع أمريكا احتجاجًا على الجرائم الصهيونية وتهدد بفتح جبهات أخرى وإغلاق مضيق هرمز بالكامل.  نظرًا لاستمرار جرائم الكيان الصهيوني في لبنان، ولأن لبنان كان أحد الشروط المسبقة لوقف إطلاق النار، ولأن هذا الوقف قد انتُهك…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76615" target="_blank">📅 17:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76614">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
تم احالة السيد عبد الكريم ابو ايمن الى التقاعد وتكليف السيد يوسف بدلا عنه برئاسة هيئة المستشارين كان يعمل رئيس جامعة الشعب
أيضا تكليف السيد حسنين الشيخ بدلا عن السيد علي شمران بادارة دائرة المراسم
تكليف السيدة ازهار بادارة المكتب الخاص بدلا عن علي الاميري ، السيدة ازهار متقاعدة سابقا كانت وكيل وزارة التخطيط …</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76614" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76613">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إيران توقف تبادل الرسائل مع أمريكا احتجاجًا على الجرائم الصهيونية وتهدد بفتح جبهات أخرى وإغلاق مضيق هرمز بالكامل.  نظرًا لاستمرار جرائم الكيان الصهيوني في لبنان، ولأن لبنان كان أحد الشروط المسبقة لوقف إطلاق النار، ولأن هذا الوقف قد انتُهك…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76613" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76612">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رشقات صاروخية ضخمة تدك مركز الجليل المحتل</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/76612" target="_blank">📅 16:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع:
إيران توقف تبادل الرسائل مع أمريكا احتجاجًا على الجرائم الصهيونية وتهدد بفتح جبهات أخرى وإغلاق مضيق هرمز بالكامل.
نظرًا لاستمرار جرائم الكيان الصهيوني في لبنان، ولأن لبنان كان أحد الشروط المسبقة لوقف إطلاق النار، ولأن هذا الوقف قد انتُهك الآن على جميع الجبهات، بما فيها لبنان، فإن فريق التفاوض الإيراني يوقف "الحوارات وتبادل النصوص عبر وسيط".
أكد المسؤولون والمفاوضون الإيرانيون على ضرورة الوقف الفوري للعمليات العدوانية والوحشية لجيش الكيان الصهيوني في غزة ولبنان، وضرورة انسحاب الكيان الكامل من الأراضي المحتلة في لبنان، ولن تُجرى أي مفاوضات حتى يتم تلبية موقف إيران والمقاومة في هذا الشأن. كما أعربت جبهة المقاومة وإيران عن عزمهما على إغلاق مضيق هرمز بالكامل وتفعيل جبهات أخرى، بما فيها مضيق باب المندب، لمعاقبة الصهاينة وأنصارهم.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76611" target="_blank">📅 16:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76610">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db7ecbe9a.mp4?token=opudIoilYCx_Ce-LcweAonM-cCpPDCgwzq3wu-ebQ4MkDFqVMSI5N3DorzM2Zfoup4BSfjQC-dS3PDJtnVRkAmYPRzoEuuuRsGmHL3SGIiTQE15dgjlc-0bjHtFWGIOP5YMnO6ECXbjuM4LgAw5DXPT-t2tabZq8-rhsYqmwTNvVEig9JNUJ35Gs69oVNuM9OpPA2v_5I2sxtyWMvuLvu20Gp-giPxFYrTrEmL3AIMlxBx3ti9iy4WXLEVG6aI0xIh_Xh1kifsbn2FxWbDxdisBcHv9k-SxlqcJiqXn-68S5wHkM6X_Ed5UC5vs9dfz8oL1hynRPpf282PlNTg2aKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db7ecbe9a.mp4?token=opudIoilYCx_Ce-LcweAonM-cCpPDCgwzq3wu-ebQ4MkDFqVMSI5N3DorzM2Zfoup4BSfjQC-dS3PDJtnVRkAmYPRzoEuuuRsGmHL3SGIiTQE15dgjlc-0bjHtFWGIOP5YMnO6ECXbjuM4LgAw5DXPT-t2tabZq8-rhsYqmwTNvVEig9JNUJ35Gs69oVNuM9OpPA2v_5I2sxtyWMvuLvu20Gp-giPxFYrTrEmL3AIMlxBx3ti9iy4WXLEVG6aI0xIh_Xh1kifsbn2FxWbDxdisBcHv9k-SxlqcJiqXn-68S5wHkM6X_Ed5UC5vs9dfz8oL1hynRPpf282PlNTg2aKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجار مجهول في الباخرة الأجنبية العملاقة MSC SARISKY V في خور عبد الله بعد إكمال تفريغ حمولتها في ميناء أم قصر جنوبي العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76610" target="_blank">📅 16:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76609">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab4e51e32f.mp4?token=V3mUIe7nlfpSr00SJq0OImDBK6LuCkeDbWaHkipciVF_TM8dX-zoT23XJTwPNlu0JB8i668CdvDC3Dgev_zxxJdYdA8NDWwg5njXlgEowvz3L8pewAqiklUZWhNZbxBIBS-AYjMtf7rDrjfuRKP-kMZF2S02-duz24qY9aMamjHxv0mBZ_yL_T8f0MsMtAd4hdyZHHBQdABXgbmyk5CPW3rc7XbvLFhnn6VqDceMDn3q6Lkh8mfLgLVzP05wb1_S4ofKqA6qWpT1VfAVN-hXvbBip2e_PvFzEl3jfPt_ANiSPV2goGoRznA3UnIX_BZ_sdKjujGY5vVNftX27d8_3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab4e51e32f.mp4?token=V3mUIe7nlfpSr00SJq0OImDBK6LuCkeDbWaHkipciVF_TM8dX-zoT23XJTwPNlu0JB8i668CdvDC3Dgev_zxxJdYdA8NDWwg5njXlgEowvz3L8pewAqiklUZWhNZbxBIBS-AYjMtf7rDrjfuRKP-kMZF2S02-duz24qY9aMamjHxv0mBZ_yL_T8f0MsMtAd4hdyZHHBQdABXgbmyk5CPW3rc7XbvLFhnn6VqDceMDn3q6Lkh8mfLgLVzP05wb1_S4ofKqA6qWpT1VfAVN-hXvbBip2e_PvFzEl3jfPt_ANiSPV2goGoRznA3UnIX_BZ_sdKjujGY5vVNftX27d8_3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إصابة مباشرة لصواريخ المقاومة في مستوطنة المطلة بالشمال الفلسطيني المحتل وأعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76609" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76608">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGC_t5OmKPPi7HcW-CBpz4DrrBjWESx92usEfdIC4-5SDVi2EDEq5kKqUEUoejy8RWpdRc0tQeSly2QvDfqJg_-xqx6wz9CtoDoYQ6LUkQd1sb2bz17YshKnTipjVLQsiekUKIEreCm77pNwaZpRerPK0uoVfGnASsdn4-mZJ1qvz_KLfsD0sgynbw7K2j8gD9cnXtR4kOUlsSdVdzGCpoWXLh6zCByq1f0GBIb5TZkBsSO7Y25qFEmN1-l4CIpBhZtBUEQG_rTntCqOC9Wp7EhL3h8ynAEcnDIZARxNsqyAodoPv71ZsD3YT9vuuTde_lbbON__1kLwD2CAd-vJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إندلاع حريق وإرتفاع أعمدة الدخان بالقرب من مطار بن غوريون الإسرائيلي.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76608" target="_blank">📅 16:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76607">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
بيان صادر عن غرفة عمليّات المقاومة الإسلاميّة حول تواجد العدو في قلعة الشّقيف التّاريخيّة:‏
بِسْمِ اللَّـهِ الرحمن الرَّحِيم
‏﴿أُذِنَ لِلَّذِينَ يُقَاتَلُونَ بِأَنَّهُمْ ظُلِمُوا وَإِنَّ اللَّهَ عَلَىٰ نَصْرِهِمْ لَقَدِيرٌ﴾‏
صَدَقَ اللهُ العَلِيّ العَظِيم
مع التّأثير السّلبي الكبير الّذي تسبّبت به المواد المصوّرة التي تبثّها المقاومة الإسلاميّة لعمليّاتها ضدّ قوات جيش العدوّ الإسرائيليّ في وعي المستوطنين داخل كيان الاحتلال، سعى جيش العدوّ جاهدًا للحصول على صورة يروّج لها على أنّها انتصار ساحق، علّه يسكّن من خلالها روع مستوطني الشّمال، فكان الهدف هو قلعة الشّقيف التّاريخية في جنوب لبنان والتي تبعد عن الحدود اللّبنانيّة الفلسطينيّة حوالي 4 كلم فقط.
على مدى أكثر من 5 أيام، شنّ العدوّ الإسرائيليّ سلسلة من الاعتداءات الجويّة العنيفة والقصف المدفعيّ الكثيف على بلدة يحمر الشّقيف والقرى المحيطة بهدف السّيطرة عليها واحتلال قلعة الشّقيف، وما إن تقدّم باتّجاه أطراف البلدة الجنوبية حتّى واجه مقاومة بطوليّة وشرسة ونيران كثيفة من مجاهدي المقاومة الإسلاميّة منعته من تحقيق هدفه، فاكتفى بالّلجوء إلى أطراف البلدة الشرقيّة ذات التّضاريس الوعرة. غروب يوم السّبت 30/05/2026 تسلّلت مجموعة مشاة إسرائيليّة تحت غطاء دخانيّ كثيف من الجهة الشرقيّة لقلعة الشّقيف حيث المسارات غير المرئيّة، ووصلت إلى القلعة والتقطت مجموعة من الصّور الفوتوغرافيّة الّتي سارع العدوّ إلى توزيعها صباح الأحد والتّرويج بأنّه احتلّ القلعة، علمًا أنّ القلعة كانت خالية من أيّ وجود عسكريّ للمقاومة.
يجد العدو منذ فجر أمس وحتى ساعة إصدار هذا البيان صعوبة كبيرة في تثبيت قوّاته في محيط القلعة، حيث تتواجد هذه القوّات قرب منطقة الاستراحة أسفل القلعة. تخوض المقاومة الإسلاميّة معركة استنزاف ضدّ قوّات جيش العدوّ الإسرائيليّ المتواجدة في المنطقة، والمشاهد المصوّرة القادمة ستثبت ذلك.
﴿وَمَا النَّصْرُ إِلاَّ مِنْ عِندِ اللّهِ الْعَزِيزِ الْحَكِيم﴾‏
الإثنين 01-06-2026‏
15 ذو الحجة 1447 هـ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/76607" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76606">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭐️
طيران حربي منخفض في سماء نواحي مدينة آبادان (عبادان) بمحافظة خوزستان الإيرانية بالقرب من الحدود العراقية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76606" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76605">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
القيادة المركزية الامريكية:
في الليلة الماضية في الساعة 11 مساء بالتوقيت الشرقي، اعترضت القوات الأمريكية بنجاح صاروخين باليستيين إيرانيين يستهدفان القوات الأمريكية المتمركزة في الكويت. هزمت هذه الصواريخ على الفور ولم يصب أي من الأفراد الأمريكيين بأذى.
لا تزال القيادة المركزية الأمريكية يقظة وستواصل حماية قواتنا من العدوان الإيراني مع دعم وقف إطلاق النار المستمر.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76605" target="_blank">📅 15:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76604">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daec07043a.mp4?token=BIefHyf-2usSKCRHa4xZFIvylsmsJpCxVjFnTtXSJxaSHI04-zKdQROYmx-Hz847stPU_Optavk7N78YPfzbGOLQz-6z61FiY3C1jKDsrn_gofR3F4GlWZ2I_-NAh3syMCLbpCZ0Id-9dSAPTgw-IWRHXI2CQ5-6XHvTp8cEbhT-4XXZYxk1yW15ooYsdVM03T8SmiRgKq3-VDz7IP1aPeptgKRsyJxcTl44znHWi6lwqj6bsBcFOnHiZsvN640yh2D5wYa0VaNXpowNg9OoxVnA10YBzq3n_OAgDIRbRIYGiKQS3lZCtGCY9CmGZRT-cj1MzCdw03Pp7sSgbgpq0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daec07043a.mp4?token=BIefHyf-2usSKCRHa4xZFIvylsmsJpCxVjFnTtXSJxaSHI04-zKdQROYmx-Hz847stPU_Optavk7N78YPfzbGOLQz-6z61FiY3C1jKDsrn_gofR3F4GlWZ2I_-NAh3syMCLbpCZ0Id-9dSAPTgw-IWRHXI2CQ5-6XHvTp8cEbhT-4XXZYxk1yW15ooYsdVM03T8SmiRgKq3-VDz7IP1aPeptgKRsyJxcTl44znHWi6lwqj6bsBcFOnHiZsvN640yh2D5wYa0VaNXpowNg9OoxVnA10YBzq3n_OAgDIRbRIYGiKQS3lZCtGCY9CmGZRT-cj1MzCdw03Pp7sSgbgpq0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
الإحتلال الصهيوني ينشر ملاجئ جديدة في الشمال الفلسطيني المحتل خشية تصعيد محتمل.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76604" target="_blank">📅 15:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487f60223a.mp4?token=B4qJAFMv0GL8T6KwmKfJOniEsg9VF2p9awxsRMKWvpc-atLlEo86hPAsMZ4pDMOacg9SWwKFRRIz2iM_s4SHYwjXaOmd-mIMszt1AHq4ap8KL_TXsMU6jaQhOXMD2vr42UZEj3QnRqONjenviDKTOQsQ6-u4l03Bi4P9nMHIoUDVhqZzhvIR4mN1F2qDoZ9fuENO41CGDvJw8js3iTzlqL_Bl_PQie8KEs8fc36kEHVk8OoGBURCzOxaPeYGoSQWKQ4rs6te_KHCK2BqcCZduZrHfTIYcYq-XyaJY2RNT_9QABCApzcZyYdU812afUm7cnM-DIlcnLn0kf6Trpn80VS809OTpqCKe4x5WxklXgPfV3e59ou6orcH-qxw2MS7wx3PsQaK_XLdutdhnlAETZ-TJU3E3U9e1N8EYOaiqnBAC000BOSevmToBDcV0jh83PPbqIA7Obg34etckwys83nsErp_Xm3Jn6LdxjETk_TW3J4pJT7dCFd7FlgqYAviemXpBttzX0zufokRC1Zb_IES3TGlwqaR0HJ-QkJ2kpGKwt20_hNrOq_ZB1jI7ADVDBjumHcHk5HnmRVvTWbr9GgiS0pCs-Sh5YfNvo-a7KTQtmiILiGwmfVwoyvbMOVZ0Z_pDJ-U5uasSXtQFL5okfZ1pjQ_kfDO3S0VDfjJUyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487f60223a.mp4?token=B4qJAFMv0GL8T6KwmKfJOniEsg9VF2p9awxsRMKWvpc-atLlEo86hPAsMZ4pDMOacg9SWwKFRRIz2iM_s4SHYwjXaOmd-mIMszt1AHq4ap8KL_TXsMU6jaQhOXMD2vr42UZEj3QnRqONjenviDKTOQsQ6-u4l03Bi4P9nMHIoUDVhqZzhvIR4mN1F2qDoZ9fuENO41CGDvJw8js3iTzlqL_Bl_PQie8KEs8fc36kEHVk8OoGBURCzOxaPeYGoSQWKQ4rs6te_KHCK2BqcCZduZrHfTIYcYq-XyaJY2RNT_9QABCApzcZyYdU812afUm7cnM-DIlcnLn0kf6Trpn80VS809OTpqCKe4x5WxklXgPfV3e59ou6orcH-qxw2MS7wx3PsQaK_XLdutdhnlAETZ-TJU3E3U9e1N8EYOaiqnBAC000BOSevmToBDcV0jh83PPbqIA7Obg34etckwys83nsErp_Xm3Jn6LdxjETk_TW3J4pJT7dCFd7FlgqYAviemXpBttzX0zufokRC1Zb_IES3TGlwqaR0HJ-QkJ2kpGKwt20_hNrOq_ZB1jI7ADVDBjumHcHk5HnmRVvTWbr9GgiS0pCs-Sh5YfNvo-a7KTQtmiILiGwmfVwoyvbMOVZ0Z_pDJ-U5uasSXtQFL5okfZ1pjQ_kfDO3S0VDfjJUyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد لتدمير طائرة MQ1 المسيّرة الأمريكية بواسطة نظام الدفاع الجديد التابع للقوات الجوية للحرس الثوري الإيراني فجر يوم أمس.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76603" target="_blank">📅 15:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
سماع انفجارات في حيفا.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76602" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭐️
إنفجار مجهول في الباخرة الأجنبية العملاقة MSC SARISKY V في خور عبد الله بعد إكمال تفريغ حمولتها في ميناء أم قصر جنوبي العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76601" target="_blank">📅 15:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZwZ5UN8CUNcu6eF7jLa9xQDudC3P0eETXVDG8y2O4qLfJSfelgMxY2O8DAWA5Ln4qMZjD5KdFZ9OdK-1qvqEEjhU48vfCXUValToSKJabRzDUSwgu-oxUgkl6EJhyN5Bn5XkHP56gToL2BQ5NrrK6G7jKTiB1J845zo5-MME3U6ie0rtXOF7zylowmWoPh3BbWCFeCn9VX5128MPW_jaZqLC0ZAHtVQR_uPkIB05W34lNu0p6sfy-PTwYVB3OZhiysjUvCa4fOoIwWNOehnJlfrIEOM_dpkbvOz8cElY8rVg01iEmmNa_v-ERnLQ6HmE1E_MTwMhEtggOrRFBLEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
للعلم الفوري:
وقف إطلاق النار بين إيران والولايات المتحدة هو وقف إطلاق نار لا لبس فيه على جميع الجبهات، بما في ذلك في لبنان.
إن انتهاكه على جبهة واحدة هو انتهاك لوقف إطلاق النار على جميع الجبهات.
الولايات المتحدة وإسرائيل مسؤولتان عن عواقب أي انتهاك</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76600" target="_blank">📅 14:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce25a3cd4e.mp4?token=dKh5TBwlnAhvf7KNaT3JAXic6uNY-c59PJvC09BB2ItqGcYGH0RBLK6QENqoahPf9IcQCaqfK_aHmDO1NQJGsC7FtsQlYefjI3UVj_NWWXUBAwc42YOgLvZX-xv-FvtW89ljpJrlATBCvdmcYr3NXzUY86gXn4aajWWBJhoVOPNnVyZm9sS07wN-V_oD99wTvHmVNtzFi07kXvcONV8dD53QTV2yzcUKgWYzYrdGdDqD7cEfYtXPA5hVYxPz262THe6SkqVZycLXK04wE_Pnrtt_sYAFZKpaMVK-Hk-q9OdHF6pjKUypu3WHPxaxPe5yJNHNOUiByogQ40FV1Qh9nkA7i5X6i1q6eXqG2fJ_uTqxkppj42rEcFytbsQrDrHBAqxb-wOvtaY8-vb-sPlelZuHnmIjTM8fPXfQ7IKnIVloVLhdf2gUFHDdMxDbAzo0__Xnl_AFLS7nKfaOe5EwIVOCK8O2JB3b6j94LXdZPxYTKJwj3ZQucJSPrJ1qFgHS8BWaycABPL-4d_VH7MU0XUrnwv-tqdoq4tKSONT-dQBbt5vpQM0ymuhhNLc3nsvR1tRNDj3dIcyWFAGACrLhOdoQsI8MAdHrEfk2W-WIJTn4z0LEQtX4c3A4D-x65Hl0c_x6RZ9j9RI7iG8IligjaGB77peK-ETVKSJ1R9OhGyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce25a3cd4e.mp4?token=dKh5TBwlnAhvf7KNaT3JAXic6uNY-c59PJvC09BB2ItqGcYGH0RBLK6QENqoahPf9IcQCaqfK_aHmDO1NQJGsC7FtsQlYefjI3UVj_NWWXUBAwc42YOgLvZX-xv-FvtW89ljpJrlATBCvdmcYr3NXzUY86gXn4aajWWBJhoVOPNnVyZm9sS07wN-V_oD99wTvHmVNtzFi07kXvcONV8dD53QTV2yzcUKgWYzYrdGdDqD7cEfYtXPA5hVYxPz262THe6SkqVZycLXK04wE_Pnrtt_sYAFZKpaMVK-Hk-q9OdHF6pjKUypu3WHPxaxPe5yJNHNOUiByogQ40FV1Qh9nkA7i5X6i1q6eXqG2fJ_uTqxkppj42rEcFytbsQrDrHBAqxb-wOvtaY8-vb-sPlelZuHnmIjTM8fPXfQ7IKnIVloVLhdf2gUFHDdMxDbAzo0__Xnl_AFLS7nKfaOe5EwIVOCK8O2JB3b6j94LXdZPxYTKJwj3ZQucJSPrJ1qFgHS8BWaycABPL-4d_VH7MU0XUrnwv-tqdoq4tKSONT-dQBbt5vpQM0ymuhhNLc3nsvR1tRNDj3dIcyWFAGACrLhOdoQsI8MAdHrEfk2W-WIJTn4z0LEQtX4c3A4D-x65Hl0c_x6RZ9j9RI7iG8IligjaGB77peK-ETVKSJ1R9OhGyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
27-05-2026
منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في موقع جل العلام شمال فلسطين المحتلّة بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76599" target="_blank">📅 14:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تعرض طائرة مروحية من نوع Bell إلى هبوط اضطراري داخل القاعدة أثناء تنفيذها طلعة تدريبية مما ادى إلى ارتطام الطائرة بالأرض ما تسبب بأضرار مادية في هيكلها</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76598" target="_blank">📅 14:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
قاليباف:  إن الحصار البحري وتصعيد جرائم الحرب في لبنان من قبل النظام الصهيوني الإبادي دليل واضح على عدم امتثال الولايات المتحدة لوقف إطلاق النار.  لكل خيار ثمن، ويجب دفع الفاتورة. كل شيء سيستقر في مكانه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76597" target="_blank">📅 14:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
مصادر إعلامية تتحدث عن تغيرات   تسمية عبد الزهرة الهنداوي مدير اعلام مكتب رئيس الوزراء بدلا من ربيع نادر .  ‏ تسمية حيدر العبودي، المتحدث الرسمي بأسم الحكومة بدلا من باسم العوادي</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76596" target="_blank">📅 13:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الجمهورية الاسلامية:
"نقل" اليورانيوم و "التخلص منه" ليس في مسودة الاتفاقية الأمريكية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76595" target="_blank">📅 13:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noqh6SO1oixiS-sG3qH63LMRlQL-1rro4AjZUfHulPDyJ64FOlTupoRCzegplmzxEnLfuF3H0tedIXgKMtQAzJOAB6jq_KsmjYLgb9OsqfQhM_XxEVsWzRqXRUDywbIfkL40zmJ_1XkeNbVJov3iKLvsR0poGQt2rzHN72MmqxWJLUpQjYcPzaHOTYz8Trm-9KLsDNDwg7Y0IHFcO_oqxU0rBGHv-UH0JURaB3qZslYmrfczGsODE_2AnpZWK7T4cEieA-qX0Ps-hCqqB7UfqZiX2BubDhaKXFyjRbV1v_h-AOkOjQGEyUdoaekQPe1byDllW-jbmsxMFRalRxMdUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث باسم وزارة الخارجية الايرانية:
أوروبا، التي تغذي الغضب العالمي من كل ادعاء لم يتم التحقق منه حول النساء في إيران وتصف المهاجمين على الشرطة بأنهم "متظاهرون"، انتقدت امرأة حامل بعنف على الأرض وسحبتها من شعرها في هولندا - ولا تزال صامتة إلى حد كبير.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76594" target="_blank">📅 13:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76593">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d9c96244.mp4?token=Oy04EWUWAoISXq4f7ogGrnLuRe6oVTQM4-SG0uHWBWU530XhepXRomfzmsj8c4H2twulaFz14NKb87jC-NN6_pXSqOv75LBFppUbcKpj3qnY_PtRS_x_47sxJPqiQ-O-gMFomugQSNdzBcvX_FnC146mLoDkuTDvzJPHwHGQE2_JuM2cihNZipXtwuu3FCwlCafJWmHnegk6_an5zfBxauSfX3U8HzbsA05tLvdrB2NXI8xtL5fNcYbKoVfxx5fkoWe7K3BJgCGlmqb24LzxQKJwKlvUG-zG6K5lweTR-R5AZrhw5SqJ1X8L9qp8pmy6p3hv1DZDuWvbAJW8xfEEqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d9c96244.mp4?token=Oy04EWUWAoISXq4f7ogGrnLuRe6oVTQM4-SG0uHWBWU530XhepXRomfzmsj8c4H2twulaFz14NKb87jC-NN6_pXSqOv75LBFppUbcKpj3qnY_PtRS_x_47sxJPqiQ-O-gMFomugQSNdzBcvX_FnC146mLoDkuTDvzJPHwHGQE2_JuM2cihNZipXtwuu3FCwlCafJWmHnegk6_an5zfBxauSfX3U8HzbsA05tLvdrB2NXI8xtL5fNcYbKoVfxx5fkoWe7K3BJgCGlmqb24LzxQKJwKlvUG-zG6K5lweTR-R5AZrhw5SqJ1X8L9qp8pmy6p3hv1DZDuWvbAJW8xfEEqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء طبريا بعد هجوم صاروخي من قبل حزب الله</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76593" target="_blank">📅 13:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76592">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: أوامر نتنياهو باستهداف الضاحية الجنوبية تمت بالتنسيق مع أميركا</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/76592" target="_blank">📅 12:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76591">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
مصادر إعلامية تتحدث عن تغيرات
تسمية عبد الزهرة الهنداوي مدير اعلام مكتب رئيس الوزراء بدلا من ربيع نادر .
‏ تسمية حيدر العبودي، المتحدث الرسمي بأسم الحكومة بدلا من باسم العوادي</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76591" target="_blank">📅 12:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76590">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106ccc92d9.mp4?token=jjUy5fc1z18D54-Ik60MloUseGg6gVyxUxmsjrXHMj9i0sfEw5UpZunRUWqJXfZwlXdd-bEPtXrjci3k7F-bEhPZolBDO9QwnfHG5S9nyANzI0uAG9D9ksiriBZ6sX5w92Bv-LDhdOBF0VnXtp35A20vkJA4pbMINTicBsLzB2Xk-ApR6kuVGty77JgMYkzn3WjSGFAamORnQwnxGV7KLjqbFMdopngwt9ov2SumKb0qHBfv6p9bFUO2J4HOxATCAoky4SxopwvogyVOXkh_bd3OSwpU7ljVDUX2TPUpJ719P7_G-Kx64RZabh3QLtBeID2QTLze4iagxTchItHEEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106ccc92d9.mp4?token=jjUy5fc1z18D54-Ik60MloUseGg6gVyxUxmsjrXHMj9i0sfEw5UpZunRUWqJXfZwlXdd-bEPtXrjci3k7F-bEhPZolBDO9QwnfHG5S9nyANzI0uAG9D9ksiriBZ6sX5w92Bv-LDhdOBF0VnXtp35A20vkJA4pbMINTicBsLzB2Xk-ApR6kuVGty77JgMYkzn3WjSGFAamORnQwnxGV7KLjqbFMdopngwt9ov2SumKb0qHBfv6p9bFUO2J4HOxATCAoky4SxopwvogyVOXkh_bd3OSwpU7ljVDUX2TPUpJ719P7_G-Kx64RZabh3QLtBeID2QTLze4iagxTchItHEEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
سلسلة غارات صهيونية تستهدف الحوش في مدينة صور جنوب لبنان</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76590" target="_blank">📅 12:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76589">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjdeZlco5FlZgo1oyDByZfslXJEwUasjmXEl2q0Mc6I7h68esrGkBzWrKt70JlN_JuJ7TTK2AsKf8mdlKtu6g70SGq7P_C_vXj5o5N37UHEecu7rMkgQu18PVMBQ6qGEhXYipNmKzu9FpyjuzBNLVEt2q5mLa_LZ-Zrda5-q_msQWtUMq1NlaStKtiMhIGUNqA7f6EZxKN1VuWPRuWJxmr7ko-0cNwc_hu9eiR2wSoTdKmgWx9RYDNPqLFbP8A9kqIY-XLE_FpwXuGQcnUdHwolupyD8APFZ2r73P5Ff0X5FY7aGUJNBTFmEkPmuHnd9kuvIOBZTSS8Kmq0n56AdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
إن الحصار البحري وتصعيد جرائم الحرب في لبنان من قبل النظام الصهيوني الإبادي دليل واضح على عدم امتثال الولايات المتحدة لوقف إطلاق النار.
لكل خيار ثمن، ويجب دفع الفاتورة. كل شيء سيستقر في مكانه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76589" target="_blank">📅 12:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني في ألون شابوت جنوب غرب مدينة القدس</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76588" target="_blank">📅 12:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ffdbce01.mp4?token=HTxUJ23SMG5kn2eJ1b3yejgJV0cXzTwVVCkPM56CuMnKFOfhjco5jpgJDiw9EcZtS7DV5BOzsMxW-F3i0KBBd1pOJsae5S7c7sA5QhcwDUbc33NCl3hHEZZ0ZXaWv5aEzmeVkTqp4E0NoRumKYQVEBVW3RiQDj_fuvmoYOe3Y25yjou7vjUHDtEUR9PiUjhBC0ileORUghJTbuyFqBlcyDzMIfZMXtucZAGmGQpDxl1vA2-5O3WFrYZ2Ld12dnAanSFM6JAi8L3Hr_TrP4BfETF2pnIV5lvdMeJjY4HmgR20gki0CPO1-3EmJ56MqSIruD_iIBYeJo8QZMJ-UfBivw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ffdbce01.mp4?token=HTxUJ23SMG5kn2eJ1b3yejgJV0cXzTwVVCkPM56CuMnKFOfhjco5jpgJDiw9EcZtS7DV5BOzsMxW-F3i0KBBd1pOJsae5S7c7sA5QhcwDUbc33NCl3hHEZZ0ZXaWv5aEzmeVkTqp4E0NoRumKYQVEBVW3RiQDj_fuvmoYOe3Y25yjou7vjUHDtEUR9PiUjhBC0ileORUghJTbuyFqBlcyDzMIfZMXtucZAGmGQpDxl1vA2-5O3WFrYZ2Ld12dnAanSFM6JAi8L3Hr_TrP4BfETF2pnIV5lvdMeJjY4HmgR20gki0CPO1-3EmJ56MqSIruD_iIBYeJo8QZMJ-UfBivw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صور من إحدى عمليات الدورية والمراقبة التي نفذتها زوارق البحرية التابعة للحرس الثوري الإيراني في مضيق هرمز.
أفادت إدارة العلاقات العامة في البحرية التابعة للحرس الثوري الإيراني بأن هذه العمليات تُنفذ ليلاً ونهاراً وبشكل دوري.
من مهام هذه الزوارق السريعة توجيه السفن في حركة الملاحة، وفي حال مخالفة أي سفينة للتحذيرات أو تجاهلها، سيتم إيقافها.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76587" target="_blank">📅 12:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSZTKxdMUedd_3fDsCtiijg9GI89s5AsgKZyRJRc0u-uJfe6v2_Mo_1jh54ww9RgbYUS5hxenHtFHa5s3r_BltH3z74Yedk0pY3yFS39xg4H_4gM5eibgtagoh8Q7MRkXAwUukPZbkNxcDvkBqwCiB041GesW6gHdWCcC0aHcwwXevS7pPsTe9jIZOLW_C3C-fd68rToFwQb2sI7geeQPYx2kJ_BTVBwBI0y0k4HX0PxIWuZXlRWxBYPcxttP7_PyivN4q79N2wwdlS3O40GpkSPsuYbOuL8cJZBa9pjgKQIWtm_WHQBlMlAUhhl-iFPKeMdw_fm6z4WYUtC2_3qxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر صور الأقمار الاصطناعية في 29 مايو سفينة بطول 252 مترًا مشتعلة عند مدخل مضيق هرمز، مع اقتراب أربعة زوارق سريعة كبيرة مشتبه بها تابعة للحرس الثوري الإيراني من الاتجاه الإيراني، ومغادرة خامسة من الاتجاه الجنوبي الشرقي.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76586" target="_blank">📅 12:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76585">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWTmlnSjrh6z2fVxvqtipZHZd8mQDRyPM7s29BggSdwbLk4ZGJ9EtdGj-_uK1_upzGskHK7A5TEG2fwgak9Cx_GnGhy1f2sNfCvKw5INXozIa2I5T_SUQfxSmBGjuGP5h9OPU3chuQrAHK59GZGr6SbVnLWKdcjnu7YCgVud88UdV-Gf6RpAOh7Y8kBPMuqEAVKXHpiwKUqz2WXdk7yxed-2LxgCXC35ks5lm7dG8PlQnmSM-1xVc-nfJu7u1bana8KOwY9nfW5slKY4AUBWxUaRHGLkSs8jWN1QVmgMA8rfsOE5vjXUbVTycV21dVNPgzV5Adm_4s9t2Guoax2-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رؤية اخرى !</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/76585" target="_blank">📅 11:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🌟
حزب الله: تصدّى مجاهدو المُقاومة الإسلاميّة عند السّاعة 15:30 أمس الأحد 31-05-2026‏ لمسيّرة إسرائيليّة من نوع "هرمز  450 - زيك" في أجواء البقاع بصاروخ أرض جو.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/76584" target="_blank">📅 11:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇰🇼
دويلة الكويت تدين الهجمات الإيرانية على قاعدة علي السالم في أراضيها.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76583" target="_blank">📅 11:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6c91e2a9.mp4?token=AAIUQWMUmVItj27mfBg1QsIAwLV8EkwJexwhVaPGfWdm6h3fDOIzG5FSLWXcUNTf4VZOAtDuWY1Q_V8P7fe8LUDudUo-DXRqsf_oc1DdcPpBsQ0rJtH8rb5R_BiYGEpqxjKCgd-hop57GhH_JkSLMAjocvChy-60We3Kns_EabRN7Ofsos0arvCEsNsVdrss3PrDCvQksNWIUg6zN2s6zWS3opWcwfFRyGUMMh5Y6iIZhVMI_kEjh_Ap7KOZ_G7eQJYj4_FdHCgzBnlYFToVMOyY7kbPAqtQ1ey4GhpkjjzWy_BAX_WE3EOJlUzYlPIXSJktAtvzGRdZ3GwHoMWU5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6c91e2a9.mp4?token=AAIUQWMUmVItj27mfBg1QsIAwLV8EkwJexwhVaPGfWdm6h3fDOIzG5FSLWXcUNTf4VZOAtDuWY1Q_V8P7fe8LUDudUo-DXRqsf_oc1DdcPpBsQ0rJtH8rb5R_BiYGEpqxjKCgd-hop57GhH_JkSLMAjocvChy-60We3Kns_EabRN7Ofsos0arvCEsNsVdrss3PrDCvQksNWIUg6zN2s6zWS3opWcwfFRyGUMMh5Y6iIZhVMI_kEjh_Ap7KOZ_G7eQJYj4_FdHCgzBnlYFToVMOyY7kbPAqtQ1ey4GhpkjjzWy_BAX_WE3EOJlUzYlPIXSJktAtvzGRdZ3GwHoMWU5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
حركة نزوح تشهدها الضاحية الجنوبية بعد توجه نتنياهو وكاتس بقصفها إلى جانب تعطيل جميع المدارس.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76582" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏴‍☠️
حدث أمني جنوب لبنان وإخلاء مروحي ل 4 جنود مصابين.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76581" target="_blank">📅 11:10 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

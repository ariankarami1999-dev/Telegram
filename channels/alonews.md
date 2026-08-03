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
<img src="https://cdn4.telesco.pe/file/ve7ykfdS7NvybeltI7lv4yjtc794Gsr494m_8mcid5ktJrWZWr0aj96C02HVY6Qo62M6hVF-X_6V6Ip9bgsYI-MFdFhm24gdWIBXfW_2Tdemfv8tFJyd_EBmjP2k75rHwuT-ygIh_ohMLUNg48CdmaJW7Qnj6IrJyG5lff_ExUXnBK9pIJDO2dJzNEcyPTxNNEBO11udQ0cZOYw0MytBuFk1gx8cAgDw59U37E4CjtZaSIc4ZqLtkhlrMK1tQqd0_XJRB_qI36yfcuS-7ye3-qX-Hq6robHowKky_uj9h0OBRW0O2R5f-I_uO8o2F4sYlPQkdY3hzR_aM-UWkOvW-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 988K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 22:13:24</div>
<hr>

<div class="tg-post" id="msg-139716">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ:
آنها به پای ما افتادند و گفتند توروخدا حمله نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/alonews/139716" target="_blank">📅 22:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139715">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ: فعلا سر جمهوری اسلامی رو قطع نمیکنم و فرصت میدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/alonews/139715" target="_blank">📅 22:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139714">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edad057e3.mp4?token=PHS43P1CUOLHvH-eX9P8w5EEjUzpHQkvBw7MTrXCjbq-yX6HYDsC-utxHpr_C6rIh_vLAyhffOiVPNZzK9F_LARc96nOAc56Z3XjTcJ7g9Scm3UUeEEdL_1AYQdXLmhazYe0FekddfBhQSU0L7bTZ82JmO75Q_DEMlgtlYR3U913sliF5cIxAFQVEZPA7fULZiWmVZJBUYg9yiN_Nu7-HsnwbtdfIQbJpIubndYBh94Eh8fJk7ERBfynVbPeQSgviKOuHKybUBV4palc_CZfAUd5RIwqXmnCKSYJK4o8GSR1d1L6XbE_wdjBNGGPL36T6w9-22uiDufTSYXvpBJnZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edad057e3.mp4?token=PHS43P1CUOLHvH-eX9P8w5EEjUzpHQkvBw7MTrXCjbq-yX6HYDsC-utxHpr_C6rIh_vLAyhffOiVPNZzK9F_LARc96nOAc56Z3XjTcJ7g9Scm3UUeEEdL_1AYQdXLmhazYe0FekddfBhQSU0L7bTZ82JmO75Q_DEMlgtlYR3U913sliF5cIxAFQVEZPA7fULZiWmVZJBUYg9yiN_Nu7-HsnwbtdfIQbJpIubndYBh94Eh8fJk7ERBfynVbPeQSgviKOuHKybUBV4palc_CZfAUd5RIwqXmnCKSYJK4o8GSR1d1L6XbE_wdjBNGGPL36T6w9-22uiDufTSYXvpBJnZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران تماس می‌گیرد و خواستار توافق می‌شود
🔴
دونالد ترامپ درباره ایران مدعی شد: «آن‌ها با من تماس می‌گیرند و می‌گویند: "لطفاً حمله نکنید، ما توافق خواهیم کرد."»
🔴
ترامپ افزود: «این حقیقت ماجراست و همه آن را می‌دانند.»
🔴
او در پایان گفت: «چه کسی در چنین شرایطی تماس نمی‌گرفت؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/139714" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139713">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ: پیش از اقدام قاطع، آخرین فرصت را به ایران می‌دهم
🔴
دونالد ترامپ درباره ایران گفت: «می‌خواهم پیش از اقدام قاطع، آخرین فرصت را به ایران بدهم.»
🔴
او افزود: «امیدوارم آن‌ها به خودشان بیایند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/139713" target="_blank">📅 22:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139712">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری / یک کشتی باری ترکیه‌ای که به سمت روسیه در حرکت بود، در دریای سیاه مورد حمله یک پهپاد انتحاری قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/139712" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139711">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: من اروپا را بهتر از هر کسی می‌شناسم؛ حتی بهتر از کسانی که آن را اداره می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/139711" target="_blank">📅 21:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139710">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: شرکت‌های نفتی سود بیش از حد به دست می‌آورند؛ باید بخشی از آن را به مردم بازگردانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/139710" target="_blank">📅 21:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139709">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: چمن مثل انسان‌هاست. آن هم زندگی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/139709" target="_blank">📅 21:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139708">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: در موضوع مهاجرت، اروپا با بحرانی جدی روبه‌رو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139708" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139707">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: آنها فردا اعلام خواهند کرد که تنگه هرمز باز است
🔴
ترامپ: تنگه هرمز به طور کامل در دست ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139707" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139706">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: بریتانیا با بهره‌برداری از نفت دریای شمال می‌تواند دوباره ثروتمند شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139706" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139705">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ : من اروپا رو بهتر از هر کسی می‌شناسم؛ حتی بهتر از کسایی که خودشون دارن اداره‌ش می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/139705" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139704">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ درباره عوارض‌ عبوری از تنگه هرمز: نمی‌گذارم ایران عوارض بگیرد. اگر قرار باشد کسی عوارض بگیرد، این ما هستیم که می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139704" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139703">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: ما دیروز میخواستیم بزرگترین عملیات تاریخ پس از جنگ جهانی دوم را آغاز کنیم ولی منصرفمان کردند، ما در حال حاضر، بنا به درخواست ایران، و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، در حال گفتگو هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/139703" target="_blank">📅 21:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139702">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fbe9e8fc4.mp4?token=SiN55L8Cj0EUSYjdrHkoBPmboHjs43sCRTZ8_vytS4AqJS9A0DOfQrEE6BbLTSqFgxOD-jc8XIsplzXPHFPepWLpVOlvJWU7AKM4hbs2pnctEC4nqrynPT-di7afrvRXlEdQAKKPX-2FNLd7TBdX4qzUL0uJh652x2RWRGj8_Vz4U_ZJ8KZOqoFV2qHBmkjl7w7OBIPTWmCrGjDnqh2dB1GhQiNkP1tLPxO1JXjs-by8WiemEfN3Z0wIF9heOGljF0KELbsdyfFS4dI5GTv3nCgWr0gVviIPaEtFKHXjbmsUjToeOfMQHf3RfBJ7Knsi7mn04-S0Z_G-EmP3V1CXoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fbe9e8fc4.mp4?token=SiN55L8Cj0EUSYjdrHkoBPmboHjs43sCRTZ8_vytS4AqJS9A0DOfQrEE6BbLTSqFgxOD-jc8XIsplzXPHFPepWLpVOlvJWU7AKM4hbs2pnctEC4nqrynPT-di7afrvRXlEdQAKKPX-2FNLd7TBdX4qzUL0uJh652x2RWRGj8_Vz4U_ZJ8KZOqoFV2qHBmkjl7w7OBIPTWmCrGjDnqh2dB1GhQiNkP1tLPxO1JXjs-by8WiemEfN3Z0wIF9heOGljF0KELbsdyfFS4dI5GTv3nCgWr0gVviIPaEtFKHXjbmsUjToeOfMQHf3RfBJ7Knsi7mn04-S0Z_G-EmP3V1CXoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمجید ترامپ از هگست
🔴
دونالد ترامپ خطاب به پیت هگست گفت: «کارت را فوق‌العاده انجام می‌دهی.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/139702" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139701">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3282f58089.mp4?token=RaW861BlERsiTnmQqXkxC_jbfqg6sXFVJWVAohjOoZHcU0Btkx72Ts_vCde737CuY1ilg8-FYK098uyi8ejofpXNXDLuayWqzWTCi30aIaj0UGlS1VlazivmIAI7_yVqXzJcBr-NjrjHUjNUi_7RQM6-XovLVmy8uDCghC30Ctiq-3s1zTjQcRuBC0gwV4drsAIL9_SOnVIfxKVUZpe4v8PuZJtsU9tvy65bk6TTaeeLc18Z_qZvCY_xuBfRMwEMmiDrqeP52oNtjItFIGpp_DZC7kxb9IW57ek-KnJQB75inV_bJ0_eRTuQtfKSxxuLLT6pMxkwZEmqyUbR9TRQUwBBUU9jE5aMlBUPv-BLZ05c8cn0T651u-xNwqj80u-Y3OaSXIbD0CZsNGMmpP6TfVQdqnBAH65VweAeB46RrM0T7wb7VhddTcDo2IIyZFGVskRR0-p3ObKThffsmUpnch1K3pGbsj6GIt0AgoRrpAd4RZGufQIQ29vd7upuTatTFl8WMJAmYMzNLFY7vgXuFLKmcB_kki9ew_TvVrSxRs5z_tqXqMyKrqc2cJo39ei17T5htYFdThJzuvXDrnV_NRQgHGo-XSqOcGs-uSLxG_xmFdw513yl7hMkOckOM3rVt5YB9O8XQlnkIIMomqFUOyoM1jHnVlf3ubz_zZtNcGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3282f58089.mp4?token=RaW861BlERsiTnmQqXkxC_jbfqg6sXFVJWVAohjOoZHcU0Btkx72Ts_vCde737CuY1ilg8-FYK098uyi8ejofpXNXDLuayWqzWTCi30aIaj0UGlS1VlazivmIAI7_yVqXzJcBr-NjrjHUjNUi_7RQM6-XovLVmy8uDCghC30Ctiq-3s1zTjQcRuBC0gwV4drsAIL9_SOnVIfxKVUZpe4v8PuZJtsU9tvy65bk6TTaeeLc18Z_qZvCY_xuBfRMwEMmiDrqeP52oNtjItFIGpp_DZC7kxb9IW57ek-KnJQB75inV_bJ0_eRTuQtfKSxxuLLT6pMxkwZEmqyUbR9TRQUwBBUU9jE5aMlBUPv-BLZ05c8cn0T651u-xNwqj80u-Y3OaSXIbD0CZsNGMmpP6TfVQdqnBAH65VweAeB46RrM0T7wb7VhddTcDo2IIyZFGVskRR0-p3ObKThffsmUpnch1K3pGbsj6GIt0AgoRrpAd4RZGufQIQ29vd7upuTatTFl8WMJAmYMzNLFY7vgXuFLKmcB_kki9ew_TvVrSxRs5z_tqXqMyKrqc2cJo39ei17T5htYFdThJzuvXDrnV_NRQgHGo-XSqOcGs-uSLxG_xmFdw513yl7hMkOckOM3rVt5YB9O8XQlnkIIMomqFUOyoM1jHnVlf3ubz_zZtNcGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ایران:
مذاکرات در حال حاضر در جریان است. این یک اتفاق شگفت‌انگیز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/139701" target="_blank">📅 21:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139700">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/ترامپ: امروز یا فردا متوجه خواهید شدند که مذاکرات در چه وضعیتی قرار دارند.
🔴
قرار است فردا تنگه هرمز را به طور کامل باز کنیم.
🔴
سپس درباره ظرفیت هسته‌ای ایران صحبت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/139700" target="_blank">📅 21:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139699">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ برای بار هزارم: ما دیروز قرار بود آن‌ها را به شدت مورد ضرب و شتم قرار بدیم. با قدرت بسیار زیاد. قوی‌تر از هر حمله‌ای از زمان جنگ جهانی دوم، اما به درخواست ایران و ضمانت کشور های عربی این حمله را انجام ندادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/139699" target="_blank">📅 21:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139698">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرنگار: مذاکرات با ایران الان منتفی شده است
🔴
ترامپ: همین الان در جریان است. این موضوع شگفت‌انگیزی است.
🔴
آنها این بار آن را تکذیب نمی‌کنند.
🔴
اما به دلایلی، وقتی در حال مذاکره هستند، دوست ندارند بگویند که در حال مذاکره هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/139698" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139697">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ : با ونزوئلا اختلافاتی داشتیم که به‌خوبی حلش کردیم
🔴
با ایران هم اختلافاتی داریم و روندش به نفع ما پیش میره؛ اوضاع خیلی خوبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/139697" target="_blank">📅 21:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139696">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزارت امور خارجه:
در حال حاضر، هیچ آتش‌بسی بین ایران و ایالات متحده وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/139696" target="_blank">📅 21:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139694">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: نتانیاهو با حضور وزیر جنگ و رئیس ستاد ارتش، یک نشست امنیتی برگزار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139694" target="_blank">📅 21:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139693">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
زلنسکی، سفیر اوکراین در آمریکا را برکنار کرد
🔴
طبق گزارش روزنامه آنلاین کی‌یف ایندیپندنت، این اقدام در بحبوحه تغییرات اساسی در دولت اوکراین انجام شده و انتظار می‌رود چرخش گسترده‌تری برای سفرای اوکراین صورت گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/139693" target="_blank">📅 21:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139692">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر خارجه پاکستان در تماس تلفنی با وزیر خارجه ایران و رایزنی پیرامون آخرین تحولات منطقه‌ای، از سید عباس عراقچی برای سفر به اسلام‌آباد دعوت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/139692" target="_blank">📅 21:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139691">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: ترامپ دوباره در حال تلاش برای یافتن یک راه‌حل دیپلماتیک برای جلوگیری از تشدید تنش نظامی است. اما هیچ مسیر مشخصی، چه از نظر دیپلماتیک و چه از نظر نظامی، برای رساندن ترامپ به جایی که بتواند اعلام پیروزی کند، وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/139691" target="_blank">📅 20:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139690">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رویترز: رهبران ایران معتقدند تهدید های نظامی پرزیدنت ترامپ صرفا برای تقویت جایگاه او در مذاکرات است، نه به قصد گسترش جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/139690" target="_blank">📅 20:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139689">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
فرمانده نیروی زمینی سپاه:  درصورت هرگونه خطای گروهک‌های تروریستی این سرزمین را به گورستان عناصر مزدور بدل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/139689" target="_blank">📅 20:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d504354916.mp4?token=OPO8KTLdyqtShpzQVy8mYRHMsyIvbOGDKbKQvajfjnAb3moVWg17WLvoTm9RlOUQRkEblN3ab-uzhe5Q3ShNoRxdZRdjqHTrtOCJCPSDUYU8FtGq7RaEMYVQS63DcoAm9RMmvRkkCkWgIpI20Y1_hZrrNIyzIome1_4Xj_vtNHhzYbMs0oWfTs7RqLoLFEIz8JNRMsQD0JQLiqR9w-pttGvvo3gHyyyACJ66DLBkNgOvw3CHzdoGgW1mZXCciSPOVEtKpmj50XdLkrfNZn79od6bzMhkwJWMcp-uxt8948BkMFVRzhvqMnL7iUzD2IFy_iyVCh6Mv7QZb51JXNwxtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d504354916.mp4?token=OPO8KTLdyqtShpzQVy8mYRHMsyIvbOGDKbKQvajfjnAb3moVWg17WLvoTm9RlOUQRkEblN3ab-uzhe5Q3ShNoRxdZRdjqHTrtOCJCPSDUYU8FtGq7RaEMYVQS63DcoAm9RMmvRkkCkWgIpI20Y1_hZrrNIyzIome1_4Xj_vtNHhzYbMs0oWfTs7RqLoLFEIz8JNRMsQD0JQLiqR9w-pttGvvo3gHyyyACJ66DLBkNgOvw3CHzdoGgW1mZXCciSPOVEtKpmj50XdLkrfNZn79od6bzMhkwJWMcp-uxt8948BkMFVRzhvqMnL7iUzD2IFy_iyVCh6Mv7QZb51JXNwxtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده F-16I سفا نیروی هوایی اسرائیل در حال رها کردن فلر (شراره منحرف کننده موشک) بر فراز جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139687" target="_blank">📅 20:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJIivVg_C-Jd2XzavI6gQVS81J6o0gbu9Dq0NxjFZT4e3MQZ2XnzAv823RjA7dG39iy04lZW1wXMNWRv4i1XqJW_9CM4cz5pEV7C2YacGB1PabDaLSco1SgI0VvyaoqW0ueO7QzBScpY48XkyD9MRrqwayDnB7v4yuI7wJ_Bbhe3rqVmAaawHVPXWJU1Qb7aXtouRs4UNkIiED1ElClAZAJsf-5gfqtHJzmY_wVg5c6Mo2-qonZpdJcKLHGHs4uRKbn0q7oVWW8J_8GBVTdAYlPjzA88oYB6jjBWexjMN2g_nNggUtN88Jp1I-9iCllrWojDdSY0h_kiEg-b95bYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/139686" target="_blank">📅 20:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شبکه CBS : یک مقام آمریکایی اعلام کرد علی رغم ادعاهای ترامپ هیچگونه برنامه ریزی برای مذاکره با مقامات ایرانی وجود نداره
🔴
تماس ها صرفا از طریق واسطه ها جریان داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/139685" target="_blank">📅 20:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام): به اعمال شدید محاصره دریایی علیه ایران ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139684" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139683">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc718d54a.mp4?token=VKmwM1cgEy9tn8I6LnFq_xz3F8pK6ba4il-X33FeQLorGxKAUdSWhB5hi4QPqwSiWyiUAFEHsI7zg3OQ4xZAPQZMXFCm-acuRIWfvYZWFQSREIX5YI_6EnMZ9woEXqXTSsp2VSwiuj8MBkWnfsrdtuiP2FYenkCuf_Pv-6GaTckDviDAtfTQdp8i9fMxOOb_Q1gbTCs1rgWB1ZrsLHbkj5sAJuEenOj24PwfSIuO4bXMl7Xx1NX82RmRpb6NcRgCotkfCz_pOshhotFYY_zb9-17rbQKNjd66sc1ePqrD9AtKe8ifVnkJfcbPaJ5rFu15dr1LduGW9-eNEBo7FK43Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc718d54a.mp4?token=VKmwM1cgEy9tn8I6LnFq_xz3F8pK6ba4il-X33FeQLorGxKAUdSWhB5hi4QPqwSiWyiUAFEHsI7zg3OQ4xZAPQZMXFCm-acuRIWfvYZWFQSREIX5YI_6EnMZ9woEXqXTSsp2VSwiuj8MBkWnfsrdtuiP2FYenkCuf_Pv-6GaTckDviDAtfTQdp8i9fMxOOb_Q1gbTCs1rgWB1ZrsLHbkj5sAJuEenOj24PwfSIuO4bXMl7Xx1NX82RmRpb6NcRgCotkfCz_pOshhotFYY_zb9-17rbQKNjd66sc1ePqrD9AtKe8ifVnkJfcbPaJ5rFu15dr1LduGW9-eNEBo7FK43Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام : ۴۴ کشتی تجاری رو تغییر مسیر دادیم
🔴
۲ کشتی رو از کار انداختیم
🔴
۲ کشتی رو برای بررسی و اطمینان از رعایت قوانین، سوار شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139683" target="_blank">📅 20:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
فارس: عاقبت مذاکره با آمریکای ترامپ بن‌بست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/139682" target="_blank">📅 20:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139681">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ae581f7d.mp4?token=m9zBWtMKByyoIJJortPmzoTbYce07T9ixbwmVGgQ-jNv86O4ClgKp4AZ3cPJs-lw3LU3zIeOF9l0gIjcMLhgfQjkJxtMNGtVl3CGjZD7yCxzIreZ1VdV8WyCHYBgN3GKAeFL4kh6vv4-f0NNAWEfUKU_iY8BojNtuzXXwE3h_VJp9wsIWfje3TDKpx-eoRvqbdtHUAMn8sACEK_kBWJzg-YvLGhpAE0jytBqgJkWaBBJlqpxh_xfPckGqf7ZOljc49Bn-QIcVvm64ncCTnw-xTZuNKthA-sGBF2_nI6Vp2RTuMiZyImYAVsPS6cTJarmGt54zD_f1K0WHCwocUml0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ae581f7d.mp4?token=m9zBWtMKByyoIJJortPmzoTbYce07T9ixbwmVGgQ-jNv86O4ClgKp4AZ3cPJs-lw3LU3zIeOF9l0gIjcMLhgfQjkJxtMNGtVl3CGjZD7yCxzIreZ1VdV8WyCHYBgN3GKAeFL4kh6vv4-f0NNAWEfUKU_iY8BojNtuzXXwE3h_VJp9wsIWfje3TDKpx-eoRvqbdtHUAMn8sACEK_kBWJzg-YvLGhpAE0jytBqgJkWaBBJlqpxh_xfPckGqf7ZOljc49Bn-QIcVvm64ncCTnw-xTZuNKthA-sGBF2_nI6Vp2RTuMiZyImYAVsPS6cTJarmGt54zD_f1K0WHCwocUml0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ف-۱۶ اوکراین یک پهپاد انتحاری روسی «گران-۲» رو با توپ خودش سرنگون کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139681" target="_blank">📅 20:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
اسرائیل برنامه صلح غزه را رد کرده و همچنان به حملاتش علیه غزه ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/139680" target="_blank">📅 20:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17c460e34.mp4?token=IVqPNUSdAQ8UnPD_Od8OepRq5E0WuT1-puiVh271iNfJIEIN3fq_tdA1yxN8QSFLZj8qG9B2NYli2Kepy-9O4czlQb2pTN94qetifxR8r_XgPAcMeEDV3Ef65Dj_8G29MCtifiea7mI0EF49dH26EYXkqESTuBEIQMVfJTxc8ZtwLdi3fhGfIWDh_C9RpCBVjtBH2RcYcBD6S3SvfkhcJ0-eNxT1os_10MgD8fwdRUUsTBXFe78BLZu4ZuTXg2kMUcbLHUllWcxVTsAW3e6RwRxHxoZtXGjDX4LtVxYLxKK1u7ZOeKoq0bDJFnVC6Uun9H1HKk0nl9Fp_kypSD4Uvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17c460e34.mp4?token=IVqPNUSdAQ8UnPD_Od8OepRq5E0WuT1-puiVh271iNfJIEIN3fq_tdA1yxN8QSFLZj8qG9B2NYli2Kepy-9O4czlQb2pTN94qetifxR8r_XgPAcMeEDV3Ef65Dj_8G29MCtifiea7mI0EF49dH26EYXkqESTuBEIQMVfJTxc8ZtwLdi3fhGfIWDh_C9RpCBVjtBH2RcYcBD6S3SvfkhcJ0-eNxT1os_10MgD8fwdRUUsTBXFe78BLZu4ZuTXg2kMUcbLHUllWcxVTsAW3e6RwRxHxoZtXGjDX4LtVxYLxKK1u7ZOeKoq0bDJFnVC6Uun9H1HKk0nl9Fp_kypSD4Uvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل، بن گویر:
من از وزیر اسموتریچ به خاطر پس گرفتن حمایت خود از طرح ورود شورای صلح به غزه در کابینه تقدیر می‌کنم.
🔴
به نظر من امروز همه درک می‌کنند که نمی‌توان برای انجام کارهایمان به هیچ طرف بین‌المللی تکیه کرد.
🔴
این توافق نباید به عجله تصویب شود. این توافق باید به کنگره ارجاع داده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/139679" target="_blank">📅 19:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: ایران هرگز سلاح هسته‌ای نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/139678" target="_blank">📅 19:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139677">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏
👈
سید محمدباقر خرازی: رهبری گفتند اگر آقای پزشکیان یک بار دیگر استعفا کند، استعفایش را می‌پذیرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/139677" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139676">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رویترز: ذخایر نفت در آمریکا به پایین‌ترین سطح از سال ۱۹۸۳ رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/139676" target="_blank">📅 19:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139675">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: ایران درخواست مذاکره می‌کند و سپس ادعاهای همیشگی خود مبنی بر کنترل اجباری تنگه هرمز را تکرار می‌کند
🔴
ترامپ رئیس‌جمهور آمریکا مدعی شد که رهبران ایران به طرز باورنکردی فریبکار هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/139675" target="_blank">📅 19:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139674">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVy9vqrepPYnREBAn7d4OFmDlasCHPQk6Q2FYjlPwUR2Hv8-pshlHXQAF7XksDwwFklORVxLVIqcdi3DNV68HdWXj1y52Yb9fghf6JfY1W9J8JJf5X1DpZ-DG6twxXkZ6_QlbShnM-wpI932FB0oAyzSfktXaOGqDOlUFD3z6airWZoKv4rv-KOsqR6x6KXdDacFAW_MIWIo_T_jthMZgRgjZkjlIG2jeXIQQqeM5WP2I0EleEOBu2N3RpRvpfG14_tXe0JK8UJZnysiv1DNHqxcyd1tHkALD9wu4fep4KOhQaqXdgIMVx1l4Z7KlSVjRSSV-kGamLIBfc230qD9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: یا مرگ یا سرزمین مادری
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/139674" target="_blank">📅 19:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139673">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: هیچ چیز به ایران نمی‌رسد مگر اینکه یک توافق حاصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139673" target="_blank">📅 19:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139672">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
العربيه: پاکستان به گزارش‌ها میزبان وزیر امور خارجه عباس عراقچی خواهد بود تا در مورد مذاکرات احتمالی با ایالات متحده گفتگو کند، پس از اینکه مقامات پاکستانی اعلام کردند که هنوز هیچ جلسه‌ای برنامه‌ریزی نشده است.
✅
@AloNewa</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/139672" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139671">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
العربيه: پاکستان به گزارش‌ها میزبان وزیر امور خارجه عباس عراقچی خواهد بود تا در مورد مذاکرات احتمالی با ایالات متحده گفتگو کند، پس از اینکه مقامات پاکستانی اعلام کردند که هنوز هیچ جلسه‌ای برنامه‌ریزی نشده است.
✅
@AloNewa</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139671" target="_blank">📅 19:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139670">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqBMffw9NsGN5JtPxXaZxi2YVgZrVXhBghCAgKEbJIkfSNu2OMcxxulrvLrHmnifWEjCO4lIr5PdCIMeMw8R-bFej8sUkx1Hy0M5GM7Bc0n4E_2kbrKOX-5eWqC1QeGgi4iUcIUKZeyD4kjoiL37BYvU4AEuU4iuQD0FzWQB2lf6ezhTT3Wb_n_8-7J8pGuz9bzg0dRMfu3EaSxIh_S6yEZuKmE-taXMfKKNB-grBzdEzV-2srPle7m00AhJVIdpcnHh9LnWLo8txcX_zL1pF6Cm2xhukBlwT1C4rESoBZeWWGqS9rg0ODNaxqceLVfixiATaCEX0Y_AgjGIdLD95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای نظارتی E-3G Sentry متعلق به نیروی هوایی ایالات متحده در حال پرواز در نزدیکی تنگه هرمز بود و احتمالاً علاوه بر ردیابی کشتی‌های تجاری و کشتی‌های متعلق به نیروی دریایی سپاه پاسداران انقلاب اسلامی، به دنبال پرتاب احتمالی موشک‌های کروز ضدکشویی توسط نیروی دریایی سپاه پاسداران بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139670" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139669">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXQtQW9JF55Pq2ZZYzOeTeTIityFN1xDzqkNPaBjuhsmCbEy1sOqp-OEysv6QNo5AUp0A12b-naEcNcLinlnvj7NDEpD-skO7UFiLk9vski6Of7HazPfSckSfR6tHxi3YUNXYji6vRpj2xHKuHZM75I_1F_mohBNk549prpMWSR3xxzAsndX58XmV7W9gLk13x2bADSHx3w5U-tFaallko1EUTjPDt_jxWR_6xfDk7D9ry-z4NWtIg3w-AiEIQCJvb9rDNp3Fecl54R-2FLYoEgMwID9mdS41FHGMUzvjnfGWn8s_0yLKK33Kq2cY4keqKG-hIOsEFEmjXOXs_SU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیدینگ ریپورت : دانشمندا اعلام کردن تنها راه نجات کره زمین اینه که جمعیتش از ۸ میلیارد نفر نصف بشه و به ۴ میلیارد نفر کاهش پیدا کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139669" target="_blank">📅 19:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139668">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8oNMfmWnMPxPvFVAbJQJXsrid-8B-kEgy1GwUqEgzpcxub9KHWkbD5dAuLSoXeEsyKmW182JSMWFA2J6vEnr2g0IguBvun1JP0pDICfRrOSLUJDdK5JnJIIeKLsIciHF8F_-vsEl9cQ5g448e6j0fbhhYjyIHJc4b8TMwKSDVPbPwiq611VDTIyh8zKqxCW59YXmz66Kaj2ZW_ywh3R1fVS4RtsIUA1DshuYTWF4zhS7ytEIlqHi49Zh2665Rpa-XcOTxvDOr79VhDNco2kVi4tMSYGU8Zc8HKUWef0aScKQECunVPGW7elvG1OnkSuGUkUodSDF42o1PfBCdiOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: رهبران ایران به طرز باورنکردنی‌ای دو رو و ریاکارن! از یه طرف درخواست جلسه می‌کنن، بعضیا حتی می‌گن «التماس» می‌کنن، مذاکرات شروع می‌شه و قرارهای بعدی هم برای همین روزهای نزدیک هماهنگ می‌شه؛ اما همزمان جلوی دوربین با افتخار می‌گن اصلاً هیچ مذاکره‌ای در کار نیست، هیچ صحبتی انجام نشده و فقط با «عمان» طرف هستن.
🔴
بعد هم طبق معمول شروع می‌کنن به حرف‌های تکراری و ادعا می‌کنن که تنگه هرمز با قدرت کامل دست خودشونه؛ در حالی که همین الان هم عملاً نیروی دریایی آمریکا کنترل کامل اونجا رو در اختیار داره و چیزی که ما بهش «محاصره» می‌گیم، یا به قول بعضیا «دیوار فولادی آمریکا»، برقرار شده.
🔴
هیچ چیزی بدون اجازه ما به ایران نمی‌رسه، مگر اینکه خودمون بخوایم؛ و از این به بعد هم هیچ چیزی رد نخواهد شد، مگر اینکه یا توافقی حاصل بشه یا ایران کاملاً تسلیم بشه.
🔴
ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم برای حل مشکلی مذاکره می‌کنیم که خودش طی چند دهه به وجود آورده.
🔴
موضوع خیلی ساده‌ست:
ایران هیچ‌وقت به سلاح هسته‌ای دست پیدا نخواهد کرد!
🔴
از توجه شما به این موضوع سپاسگزارم پرزیدنت دونالد جی ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139668" target="_blank">📅 19:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139667">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4xDPIngBm7kEvYhWpXPfSimaWtY22PzdV8MGqEOJpBYqMdtg4B3MtRXfyV1EVFZGqWTQ_1B7qUaAzN3iM1x0o6fJrpKjwHsVmCnslhLEGIFwkvTDjAK6HDPSMcoJ9G34gQVnPCnkpPz_nmNH7y3_4tIRz0ntg71HOBb8mCzWB_cLU5cCnac6NSYZA5TGzwRFGPrb33zVu7MDXwfX2FFDrkfo2QJPByMLyUjm0Oz-SUoTYvQa7qyhEDlYMTgUuxbt1I56KRuHZHFbGJw2Meoz5o6BqKPzykRGl_ICbljQb_P0oh2IDntfhIKst4Uw47KoGj99qkVIf2GR8in1rgj-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام توییتی را منتشر کرد که در آن از اعزام لشگر هوابرد چترباز های آمریکایی به خاورمیانه و تصویری از تمرین این نیرو ها خبر می دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139667" target="_blank">📅 18:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139666">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76554f0287.mp4?token=ULqGzdgc22V2cehI3Wo2L2-hYbtbAMzqGJylG3TMyWZPk51Ydj0-uqi7W3sNNXo6AtguCA5JQJwv3Wx5-oN7TKYiPbXbG4CWLogE4k_6ZpcGMJMwzrKjaEQtNm5eWGvETzSTXrZyatAV1fpa3Nik3zcvAnCEsFWFiUi9xry1hdvdTuHAl3ED7EZ0FRVIzDsYPXucYKex7Rym3ACFH2mP_PjycbXPIRYcBrtVbtOggYlpJpVcJgRON08Ayb8TMhtJA2hyqyfcq8WwZR2zMv-aRH8RfCX3kU6MEFEIDCaqjtwaIQv5TtjIe_f9DZFUg8jAZ09lzai1fw6NdI22oDSMMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76554f0287.mp4?token=ULqGzdgc22V2cehI3Wo2L2-hYbtbAMzqGJylG3TMyWZPk51Ydj0-uqi7W3sNNXo6AtguCA5JQJwv3Wx5-oN7TKYiPbXbG4CWLogE4k_6ZpcGMJMwzrKjaEQtNm5eWGvETzSTXrZyatAV1fpa3Nik3zcvAnCEsFWFiUi9xry1hdvdTuHAl3ED7EZ0FRVIzDsYPXucYKex7Rym3ACFH2mP_PjycbXPIRYcBrtVbtOggYlpJpVcJgRON08Ayb8TMhtJA2hyqyfcq8WwZR2zMv-aRH8RfCX3kU6MEFEIDCaqjtwaIQv5TtjIe_f9DZFUg8jAZ09lzai1fw6NdI22oDSMMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادعای نتانیاهو: اکثریت قاطع مردم ایران شیفتهٔ اسرائیل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/139666" target="_blank">📅 18:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139665">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd46c3368.mp4?token=Rx9CCUkyNs6UpJfC-u8IloZhGWEKfhMJMmzlFEuFBSOdSoP4ynQrLsAEwtDzakRaETgpNiMpz2X5OKx7oKRAHGc626svGwa_5UT6liM_ce5iNx61TP6vHBc3EwRq23yWF4KiEZK5iU4Ptwrobkf4t4Empv6_DPXHU1S40LByVJrTZh_mvTmj7uESMvMkl1FgslCYXTzTPJWgdV4FQAz4KSGnLztIOfNtwtSjdP_jzUD_aP86x-QrAh0jiSxsFLYIp6bICTxCKepaR4kM3nrMwuxnH5O9RZtWHXJ0DYjULfKSmVbgwJtxRXov2VzKFvdzOzvtURjWG0qjJlrc5aVS8Fgr1Lj_RsGkuT-9oDEuVVRuMUw4aZR9mssdhh5h49pDOXrShjc5682mjdj0A8ZKq3U0sjTP4038RIUqzPCKIUL6VjEenzDifETsequUNGq8stWBoAoxCIbXzBi8k87qK_fybTh3pARu2P26frXNjFSyuSRS5pp5qhBdIm9s_9RDNvTfRH_VhqeFl3PUb65DuptHwlTGDXygbjuRMXO_Za3oJhBXkN4w-mNDAf34I-XMULpDDu3dllUCXJnLnKTFVXpDwlZgu4vaIM4X5ZEBEUoqPGnRqcHDV94SnJWjCoUXPDZejUmfHfc8BLHRV_AhoVBQJm5i6n_T0Hj1J_2lpwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd46c3368.mp4?token=Rx9CCUkyNs6UpJfC-u8IloZhGWEKfhMJMmzlFEuFBSOdSoP4ynQrLsAEwtDzakRaETgpNiMpz2X5OKx7oKRAHGc626svGwa_5UT6liM_ce5iNx61TP6vHBc3EwRq23yWF4KiEZK5iU4Ptwrobkf4t4Empv6_DPXHU1S40LByVJrTZh_mvTmj7uESMvMkl1FgslCYXTzTPJWgdV4FQAz4KSGnLztIOfNtwtSjdP_jzUD_aP86x-QrAh0jiSxsFLYIp6bICTxCKepaR4kM3nrMwuxnH5O9RZtWHXJ0DYjULfKSmVbgwJtxRXov2VzKFvdzOzvtURjWG0qjJlrc5aVS8Fgr1Lj_RsGkuT-9oDEuVVRuMUw4aZR9mssdhh5h49pDOXrShjc5682mjdj0A8ZKq3U0sjTP4038RIUqzPCKIUL6VjEenzDifETsequUNGq8stWBoAoxCIbXzBi8k87qK_fybTh3pARu2P26frXNjFSyuSRS5pp5qhBdIm9s_9RDNvTfRH_VhqeFl3PUb65DuptHwlTGDXygbjuRMXO_Za3oJhBXkN4w-mNDAf34I-XMULpDDu3dllUCXJnLnKTFVXpDwlZgu4vaIM4X5ZEBEUoqPGnRqcHDV94SnJWjCoUXPDZejUmfHfc8BLHRV_AhoVBQJm5i6n_T0Hj1J_2lpwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: خاورمیانه دیگر همان خاورمیانه سابق نیست. ایران دیگر همان ایران سابق نیست. آن‌ها بسیار شدیداً تحت ضربت قرار گرفته‌اند.
🔴
آن‌ها هنوز توانایی‌هایی دارند، اما به ماه گذشته نگاه کنید؛ آن‌ها به ما شلیک نکرده‌اند.
🔴
چرا شلیک نکرده‌اند؟ زیرا می‌دانند که ما می‌توانیم آن‌ها را آن‌قدر شدید بزنیم که بازدارنده باشیم. اگر به ما حمله کنند، ضربه‌ای بسیار شدید را تحمل خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139665" target="_blank">📅 18:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139664">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نتانیاهو: ایران به‌شدت آسیب دیده است؛ اگر حمله کند، ضربه‌ای بسیار سنگین دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139664" target="_blank">📅 18:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139663">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نتانیاهو: یک کمپین سازماندهی شده با کمک مالی بزرگ وجود دارد تا اسرائیل را در شبکه های اجتماعی بی اعتبار کند.
ما باید با این کمپین مقابله کنیم و آن را شکست دهیم.
🔴
من فکر می کنم محاسبات ترامپ بر این اساس است که نمی خواهد اقتصاد جهانی فروبپاشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139663" target="_blank">📅 18:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139662">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نتانیاهو: در دو جا نمی توان زندگی کرد: در کره شمالی و در غزه.
🔴
غزه اجازه خروج به شهروندانش را نمی دهد. من همیشه می پرسم چرا مردم غزه حقوق بقیه مردم دنیا را ندارند، حق مهاجرت.
🔴
اسرائیل دومین قدرت سایبری دنیاست.
ما در حال تبدیل شدن به دومین قدرت هوش مصنوعی در دنیا هم هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139662" target="_blank">📅 18:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139661">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نتانیاهو: من قصد دارم شرکای جدیدی داشته باشیم. برای همین هست که من به شدت در هند سرمایه گذاری کرده ام و نارندرا دوست خوب من است و ما در هند بسیار محبوبیت داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139661" target="_blank">📅 18:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139660">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نتانیاهو: من دوست دارم نیروی هوایی خودمان را توسعه بدیم. فولادین ترین نیرو هوایی ممکن برای آینده. چون ما نمی دونیم کمک هایی که دریافت می کنیم قراره تا چقدر ادامه پیدا کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139660" target="_blank">📅 18:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه ایران و عمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139659" target="_blank">📅 18:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139658">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
منابع دیپلماتیک به شبکه الحدث: پاکستان در تدارک ارسال دعوت‌نامه‌های رسمی برای قالیباف و عراقچی به‌منظور بررسی ازسرگیری مذاکرات است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139658" target="_blank">📅 18:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
روزنامه کیهان: اگه به نیروگاه‌های ما حمله کنن، خدمات کاهش پیدا میکنه و کاملا قطع نمیشه ولی ما توی نصف روز کل کشورهای حاشیه خلیج فارس رو با موشکامون وارد وضعیت بحرانی میکنیم و در آخر آمریکا مجبور میشه کاملا از خاورمیانه خارج بشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139657" target="_blank">📅 18:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139656">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ایلان ماسک : تا یک سال دیگر نابینا ها با نورالینک خواهند دید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139656" target="_blank">📅 18:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139655">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: وزیر خارجه این کشور در گفتگو با همسایه‌ (همتای) ایرانی خود، تحولات منطقه‌ای و بین‌المللی را بررسی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139655" target="_blank">📅 18:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139654">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: وزیر امور خارجه از عراقچی دعوت کرد در کوتاه‌ترین زمان ممکن به پاکستان سفر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139654" target="_blank">📅 18:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سوئیس: با ایران و آمریکا در خصوص مذاکرات احتمالی در تماسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139653" target="_blank">📅 18:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139652">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4FoIdCHhEn2E8-lwd6XJUze-xCaH149zD-3IG501AaX9rsqm60CVBf57gNfuZxnstznsXZSYkpmlZvNAZ3CDGpovM6KsJHbFATCuYbUcWKQtaxa6Y4fi1wKTaDrinCN_EB8h3zFjSxJC6KItLHAWset51ovfgnbnSrNl8Yryo9r40heMoHXWS3XXjevKsh3-dRyY3q44luzTItGV3U-plslFkxb4onU1D-cPjV5msrJR4TdKSX_Haxpfkn0dq-yv-BBfHkOa2uivvCJrYW6hJwP5Fs7DfGqnqIZVjT4Dte0CZFhocrZoHNRyb-k51tQr9Fx9HDcyCK9Q94YRauLJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفیر آمریکا در ناتو: در حال حاضر ما دیپلماسی و مذاکره را انتخاب می‌کنیم
🔴
متیو ویتاکر: فکر می‌کنم ایران و آمریکا بیش از هر زمان دیگری به توافق نزدیک شده‌اند. اما در عین حال، ما همچنان در رابطه با ایران از موضع قدرت رفتار می‌کنیم.
🔴
در حال حاضر ما دیپلماسی و مذاکره را انتخاب می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139652" target="_blank">📅 18:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / آناتولی به نقل از منابع دولت پاکستان:دطبق پیشنهاد، تهران تنگه هرمز را باز خواهد کرد و واشنگتن نیز محاصره را لغو خواهد کرد
🔴
وزیر کشور پاکستان، قرار است «طی یک یا دو روز آینده» به تهران سفر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139651" target="_blank">📅 18:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f2b33055.mp4?token=RXAvqyfv1cKqFVH40KzPThEKI7jhepbyHzorm14mZ0o1CI9RYhQYh8r0LfbWzMXYjepp4bxgxwDVYd2UKDerBIxUZk0dDPIXKZnld_W5sOzyu4UDcvFWHao7Z4j2EKus-9AEq6dIjNqABCteJhkFXhgXyQJ6z9SCH2wk-rSU6BGFIy4oqlvjeFOT8Bi5yDlAZQcX4H195iKys9e9hirnxue3v5nAJO5KdrpvYtr0WVt-oQLNP3GSQf7R1jpExv_oMOAx50Pg3b0KZHRZAToP9mkqPysmbxebL0ZwV2Ag5jJ9PDDYGL3FvukJ38msGIWRhZh4tXANl_7T-imtqwCYihIBvSdIKnG8NUhI5W5j1UsBGIdMFj3LjgQXY_Cfi8Q9RfY8RKi1Otoxetj45Uj85pOZ-UsWFrJ-wtnYph8EazrrqYaVoWBv0n2b_IZHBUzr63SxFa5wN5BffaR1333oj_m99DRk_E-17YMb4RMC_6CMbBupD8weGU0V9cnnhz4kIoqlWifrvYPXCqD_9Q4gjQvfxos7EmKLuV6ykOZQALdDdtvRiREYa6Z7it9ku5zetb8FWUlKNZPXJY_beoNR7yYkeNNcV70AKZF_gjNUbjGJYRixnU7bX-HY9s31-pb1KQ_r0_lZqrDDgw2J-afQPYadVoe9oevbhscuv6KYBEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f2b33055.mp4?token=RXAvqyfv1cKqFVH40KzPThEKI7jhepbyHzorm14mZ0o1CI9RYhQYh8r0LfbWzMXYjepp4bxgxwDVYd2UKDerBIxUZk0dDPIXKZnld_W5sOzyu4UDcvFWHao7Z4j2EKus-9AEq6dIjNqABCteJhkFXhgXyQJ6z9SCH2wk-rSU6BGFIy4oqlvjeFOT8Bi5yDlAZQcX4H195iKys9e9hirnxue3v5nAJO5KdrpvYtr0WVt-oQLNP3GSQf7R1jpExv_oMOAx50Pg3b0KZHRZAToP9mkqPysmbxebL0ZwV2Ag5jJ9PDDYGL3FvukJ38msGIWRhZh4tXANl_7T-imtqwCYihIBvSdIKnG8NUhI5W5j1UsBGIdMFj3LjgQXY_Cfi8Q9RfY8RKi1Otoxetj45Uj85pOZ-UsWFrJ-wtnYph8EazrrqYaVoWBv0n2b_IZHBUzr63SxFa5wN5BffaR1333oj_m99DRk_E-17YMb4RMC_6CMbBupD8weGU0V9cnnhz4kIoqlWifrvYPXCqD_9Q4gjQvfxos7EmKLuV6ykOZQALdDdtvRiREYa6Z7it9ku5zetb8FWUlKNZPXJY_beoNR7yYkeNNcV70AKZF_gjNUbjGJYRixnU7bX-HY9s31-pb1KQ_r0_lZqrDDgw2J-afQPYadVoe9oevbhscuv6KYBEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی : ما می‌دونیم پوتین دنبال طولانی کردن جنگه و برای بسیج نیرو و حملات جدید آماده می‌شه
🔴
اهداف واقعی روسیه رو می‌بینیم، متحدانمون رو کنار هم نگه می‌داریم و فشار روی روسیه رو بیشتر می‌کنیم
🔴
ما اهداف واقعی روسیه رو می‌بینیم، متحدانمون رو کنار هم نگه می‌داریم و فشار روی روسیه رو بیشتر می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139650" target="_blank">📅 18:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گزارش ها از شنیده شدن صدای انفجار در دبی امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139649" target="_blank">📅 17:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
گزارش ها از شنیده شدن صدای انفجار در دبی امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/139648" target="_blank">📅 17:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139647">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مطلع: نماینده ارشد شورای صلح و مشاور این شورا امروز با نتانیاهو دیدار کرده و به او ابلاغ کردند که باید حملات به غزه متوقف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139647" target="_blank">📅 17:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
آناتولی: منابع از تصمیم محسن نقوی، وزیر کشور پاکستان، برای سفر به ایران ظرف «یک یا دو روز آینده» خبر داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139646" target="_blank">📅 17:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He5_QH6KwS4iAyXNzz5-_SVoDnn7x0r--6yFfdaTnfn-F92lX8tqwpIN3vIxzsg0ytpePynE7ioxbjVigKyd_JRn1yLONeEzMuZMhGJpayxA_m9kjZVOhEyvnVgrYebEqkZNmXc24RrRHJGJc6ly9OdA-9QGw_naDZV-SomHMcpucHMJKo9CBjQsR1tkeZnlmue1XktxhxIIAxgXX0IvYMbPl7Xk2n_y_PQmXlX_iji3sv6ulI3COXlchwldMg_RXWsn00OQfZJe7C77ddsmaBbmtLPt400y1XYDvo93tOeOH9vWak_Ad_KTnRTZ3V-sxOgHDhejucy2hw-TgwhGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ عکس خودشو کنار جورج واشنگتن و آبراهام لینکلن منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139645" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9F6jQBwjNpMOYeLJQzft1LxmqK4YJllt3LdLWwKj9DIdxw_jVntwy6hw3CN5p7iwfueLlLG_fwp2Epe8DSXoKY_heUrVYtwx9r-vxM1giGERVUk6Jl4u1EVFw_aIBLXDs7sLpVhnuOl9B84c44_ajo_5U2EzpnDbCbG7qa4JWEqzkBwdxlTRNOX63RZI6nXy48nlohZiTYE2Og2jTPuujL0G08QzJ_fBvpx_FABsoTGoC8jl5IcX8CqP1nMQ_8_eC2EHJPw5xylMc3ABjIGpdYubXzHsPKcvRCfe_h80a7UihbnjFyMVxdT0FsBi4bAt_u3yhy2tz0ExpgbjIt4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏ترامپ
:
شرکت‌های نفتی، قیمت نفت رو برای مصرف‌کنند‌ها پایین بیارید، همین حالا!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139644" target="_blank">📅 17:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
فارن پالیسی: حمله زمینی گسترده به ایران بعید است، اما عملیات محدود همچنان روی میز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/139643" target="_blank">📅 17:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
روزنامه نیویورک پست گزارش داد جیانی اینفانتینو، رئیس فیفا، همزمان با افزایش فشارها برای کناره‌گیری، در پی جلب حمایت دولت دونالد ترامپ است.
🔴
بر اساس این گزارش، اینفانتینو دیدارهای خصوصی با مارکو روبیو، وزیر خارجه آمریکا، برگزار کرده و یک منبع مدعی شده است که این گفت‌وگوها «بیشتر درباره حفظ موقعیت شغلی اوست تا دیپلماسی فوتبال»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139642" target="_blank">📅 17:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عارف: برنامه‌ای برای قطع اینترنت در صورت بروز تنش یا جنگ وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139641" target="_blank">📅 17:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139640">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g06FrT95fhlK62FjA16x5D0hzoCQbqoTHxseR3L3QbyaSrBZS9MtSfMzF7w0-4xK6g2ClAhKRgpOX_0muIkr07BfcQX8Xv7P6MU3fE0Ps_v8vcW5pM2MtUChy-FVKcujkbSTJH-4ZgoZMM9-XPBgCDwrg7QHfUiP8Sf69qIGGiNyvib-mzDmHLubN77j11SYgSR9kl6i68XBCW-_uvHd1WRYH93rLvU3NBfqJM8ycuBSbNhCzKl791fGofs-xG34ZBvUy3CqNEUdGfzC3tvmtfhAExMYq2Lmj78ziNJhD8C2PhtZ_TrxO1CYaFdJtQcEZw6NE0Qp-E40Yvs67J07xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارک لوین، تحلیلگر نزدیک به ترامپ در فاکس نیوز:
🔴
از اسرائیل حمایت می‌کنم.
🔴
از اوکراین حمایت می‌کنم.
🔴
از تایوان حمایت می‌کنم.
🔴
از مردم ایران حمایت می‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/139640" target="_blank">📅 17:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139639">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbb6qKOPO5lnurqaYlcnK_vZ_spYc8YNiKvkkBNKi0uY8e671rTxIIUDDtKeCK0rDWS4UTrg0IFslGBvv4BDfVWzOM8z1jmH9k_MOTS8xmjnrvEoSilwcir-21PG5vWpG3tbeWZZSE9-6gcQ9h9EpECHfLyu_gM-74r0VAInvzledvTNNhojSOKKlF7tNIBAlDSg3K_Xnuq_VeNp1GFiIHzCrC2GV3vriKtaebzOKFpLlgWe-ZWSpvvbCU0ZbQA2TVs-6-AslPZbLioZKpKwzZKic3XkSBqYzQ-vPwl0hGdyfNxQOWTHnZQCwfHNLLeMo9htWO9VGOBUkjaF2wQktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در تمام ماه جولای ارتش روسیه تنها ۳۰کیلومتر مربع پیشروی رو به جلو داشته است، در حالی‌که ارتش اوکراین در این ماه توانست ۱۳۸کیلومتر مربع از خاک خود در جبهه لیمان، دنیپروپتروفسک و زاپورژیا آزاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139639" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139638">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsZmU8dbJq1Jugl5JOcDXbBr28cFXIM44YJeuBTimF25kcKARBNS3uBVksL_rhIz3auo0oUPbRmrGJtvqaEJvRLKGwJYoIY1tsMqlG_NmA3Thk24qgNrKia9EiDXek0ZIt9pfdDyyVqlArFsbyexhcLMWXMmX8HJbaENbiZUZ2Pw8tOoa5TsR7UPs7JfFTzliw5fPCaZyE7NZe0avi4zw0FWeS02wp4MWCLJE2hd-kC2JbU3izRpo2SmBMpWUj7KYRu6Gx03Tw4tVi8n_EckkDT_pnba6DKGPIHSzrkGXGDY5pSmBSuJpZQJ51ThGZuPu6bh9u9MN3rfiQV1sllc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: آمار واقعی محبوبیت من، نه نظرسنجی‌های ساختگی رسانه‌های جعلی، بهترین نتایجی را نشان می‌دهد که تاکنون داشته‌ام. چرا هم نباید این‌گونه باشد؟ با بزرگ‌ترین کاهش مالیات و بهترین آمار اشتغال در تاریخ، بزرگ‌ترین سرمایه‌گذاری خارجی در تاریخ آمریکا، مرزهایی کاملاً امن، یک پیروزی بزرگ در ونزوئلا، خلع سلاح هسته‌ای ایران، احترام و موفقیتی بی‌سابقه در سراسر جهان و دستاوردهای بسیار دیگر.
🔴
به نظرسنجی‌های جعلی چپ افراطی باور نکنید. آن‌ها فریبکار و فاسد هستند، درست مانند دموکرات‌های فاسد و متقلبی که کشور را نابود می‌کنند.
🔴
برای عظمت آمریکا به جمهوری‌خواهان رأی دهید! از توجه شما به این موضوع سپاسگزارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/139638" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139637">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
منبع ارشد حماس به الجزیرة: این جنبش با میانجیگران تماس گرفته و خواستار موضع‌گیری صریح در قبال تشدید اخیر تنش‌ها توسط اسرائیل در غزه شده است.
🔴
این جنبش از میانجیگران خواسته است تا مستقیماً مداخله کنند تا اسرائیل را به اجرای آتش‌بس کامل وادار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139637" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139636">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سنتکام: نیروهای ما آماده پشتیبانی از کشتی‌های تجاری هستند که مایل به عبور از تنگه هرمز هستند
🔴
سخنگوی فرماندهی مرکزی ایالات متحده : نیروهای ما هوشیار و آماده انجام هرگونه مأموریتی هستند که به آنها محول می‌شود.
🔴
نیروهای ما آماده پشتیبانی از کشتی‌های تجاری هستند که مایل به عبور از تنگه هرمز هستند.
🔴
از ابتدای ماه مه، ما به بیش از هزار کشتی کمک کرده‌ایم تا از تنگه هرمز عبور کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/139636" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139635">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAZR7RfETr0Q1dDGKw1EQXazi72pwxGMGBvuAgTdXkbbqKe919EOEZSMst2hLcbNmwPm6cO5HAXmYgobrrVyM0TXto3ojEUgIYvayRTTKX0B9NNmyVY3SSS058xYbIJnRkyUxDymgArkW9hIIWcCpfXBTBHhmLxIHLB0fRT6UA_eQqLaHpCUcvaEpB00_6QZD3GcvtLT3UROSE3NkXGv1uXCT63k6AUJHCxnvMuX6Li5WhPlc6bKCe9F344IZY-z4ROl4otDVSddBFkFqYq6zKSXYB0YtAmA-tyryehNWljst7w8jV1VrjGSSmZNKHTM3P8ONON0qaTKD7X2CS1MLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر صمت عازم پاکستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139635" target="_blank">📅 17:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139634">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4NlPtPmMlRiWQi8kYwrx12Vw6YkRXZ23f4-3XWmCidUXHnbQjT0LZwuDi04IpY6ZCnHAohxhojTMfNCaEdhf7tcFFViXSVXjoKTmcRHpEmlwcidOROk9Wkg2iHmCtFvFdtAhieFrGeGzmuHKBH1hJwfLRKg16arE9JtHoX2IxDJFdh70KFWjvKuhnG7SoX9QSzaXMhDM8sL-ic8HbB6rYYitVp5JeAV9rjTQjlMEF5OXE1CGuEY_2wXlZCogGo8AL92fjK_YMMK5FNepMASdSIJoo30_fUFZF0zEnsbjZ77I00O2Son9e9NJqpHZ6YgcIMganQ4uwVv89RXk9maqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای جاسوسی مشترک RC-135W نیروی هوایی ایالات متحده (شماره دم 62-4126) به تازگی از پایگاه نیروی هوایی سلطنتی میلدنهال با شناسه OLIVE26 وارد فرودگاه چانیا در یونان شده است
🔴
این هواپیما از زمان ورود از پایگاه نیروی هوایی آفات در 5 ژوئن در پایگاه نیروی هوایی سلطنتی میلدنهال مستقر بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/139634" target="_blank">📅 17:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مقامات ارشد پاکستانی:
هیچ مذاکراتی میان ایران و آمریکا تعیین نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139633" target="_blank">📅 17:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
اسناد شرکت اسرائیلی «البیت سیستمز» فاش کرد که اسرائیل پهپاد‌های استراتژیک و سیستم‌های نظامی پیشرفته ای به امارات فروخته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/139632" target="_blank">📅 17:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139631">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
داده‌های ردیابی دریایی نشان می‌دهد ۶ نفتکش بزرگ با پرچم عربستان طی روزهای اخیر مسیر خود را در خلیج عدن تغییر داده‌اند.
🔴
این نفتکش‌ها پس از بازگشت از مقصدهای مختلف در آسیا، به‌جای عبور از جنوب دریای سرخ و تنگه باب‌المندب، به سمت جنوب قاره آفریقا حرکت کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139631" target="_blank">📅 16:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رودا: نیروهای آمریکایی، بریتانیایی، فرانسوی و آلمانی طی ۷۲ ساعته، صدها نیرو و سامانه‌های کلیدی پدافند هوایی خود را از فرودگاه اربیل خارج کرده‌اند
🔴
این اقدام، اقلیم کردستان را در برابر حملات [احتمالی] ایران، به شدت آسیب‌پذیر کرده
🔴
در مدت سه روز، آمریکا هشت سامانه موشکی پاتریوت زمین‌ به هوا را به اردن منتقل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/139630" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع ایرانی: ایالات متحده در موضوع مربوط به بسته ماندن مسیر جنوبی در تنگه هرمز، امتیازی به ایران ارائه کرده است
🔴
ایران در پاسخ به آخرین پیشنهاد آمریکا، با رد این پیشنهاد اعلام کرده است که تا پایان کامل جنگ، تنگه هرمز را باز نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139629" target="_blank">📅 16:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139628">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: هیچ برنامه‌ای برای گفت‌وگوی مارکو روبیو با رئیس فیفا وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139628" target="_blank">📅 16:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: هیچ گفت‌وگویی درباره پرونده هسته‌ای در جریان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139627" target="_blank">📅 16:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YugMD_g2lVrsi_-mQdRbetk6yJWwURDqUuSmdeVIgyDWQdsb1iBmbDhFfmrgGI9vBV5yO35liRJUEEplp3pizcrlZADmb1to1vPMbR9nNFc2djpP4f1ithXdR0bJeT1FoRHQ1GGW4DZzKdFKLxA6MeiTfORoOIlik_GEbhDJA9OKzFqnKhKeY9vBaVcN1Qbh9HRrJ5oY_bLrtgjKzqMGj6silENkJ8PsxYK6DBej7MS112SvQIp6O_vkXl6vVxHixICdkonqvcDt7wRS2oaZLslsEPLMmfkG6q3FzNc_qWs3cp-eEx7DivWZd7WrTRGmvDHOeN1CqXbTbyUPdXk5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر 1 گیگ اینترنت که مصرف کنید توسط اپراتور‌ها 2.7 گیگ‌ محاسبه میشه و کسی هم صداش درنمیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139626" target="_blank">📅 16:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بلومبرگ گزارش داد شرکت «نورثروپ گرومن» قراردادهایی به ارزش حداکثر ۳ میلیارد دلار برای تأمین قطعات کلیدی موشک‌های رهگیر ساخت «لاکهید مارتین» امضا کرده است.
🔴
این قراردادها بخشی از برنامه گسترده آمریکا برای افزایش تولید مهمات و موشک‌های رهگیر پس از کاهش ذخایر تسلیحاتی در جریان جنگ ایران عنوان شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139625" target="_blank">📅 16:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWUV-YIJ7x0ny_sq_PC0vJN_RBX39vlN57gjfaZfO7Ub4DhSLIkOj5kmmoW3pamu_-pkFPdp6dkortM7HzUiAABLAkWQi0CY6_jSRjy5EiMHfCZIqN8jzB55YKevIkZpnRxmBp-Mht2fvj4YkgQEjMujV53io9QSkCcUDFQo7Fc7yGHbMLFpEBJKkJVCRe40s-NKs9s0C4-8YU7nVW3Rw10rSd3WhnSzKNE5EN_85n-6JPN5rvQtsv-diZOx1Q0UBHfGaEwLsNu_PrqLIiziqWGmfZ2NPdAjmSp_dbY7_0-m9jPvgH5TQqrsyrUMG1fEnpmMd_hN_FpOc8Z-6i4XJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با وجود اظهارات پرزیدنت ترامپ مبنی بر آغاز مذاکرات امروز، طبق گزارش آنا‌دولو با استناد به منابع دولتی پاکستان، هنوز تاریخ یا مکانی برای از سرگیری مذاکرات مستقیم میان واشنگتن و تهران نهایی نشده است.
🔴
میانجی‌گران پاکستانی و قطری همچنان در تماس با واشنگتن و تهران برای ترتیب دادن یک نشست هستند و اسلام‌آباد و دوحه از میان مکان‌های احتمالی محسوب می‌شوند. با ادامه تبادل پیام‌ها از طریق میانجی‌گران از سوی هر دو طرف، پیشرفت‌های مثبتی در هفته جاری انتظار می‌رود.
🔴
انتظار می‌رود مذاکرات ابتدا به صورت غیرمستقیم آغاز شده و سپس به مذاکرات مستقیم تبدیل شوند. در مرحله اولیه، تمرکز بر تثبیت توقف فعلی درگیری‌ها و بازگشت به وضعیت پیش از ۹ ژوئیه خواهد بود، نه بر برنامه هسته‌ای ایران.
🔴
اجرای آتش‌بس در جنوب لبنان نیز از جمله موارد اصلی در دستور کار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/139624" target="_blank">📅 16:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139620">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVwEt8FM6PHlXx362ACwvmYAjV4Xuay5hZLpjR-qzYueQuiQnPSK4G7nSL2bBmD1GaMviEFXLNC854htQYQlGQYrAvyGPT8DHOlFid6hU42aSgbUKJgkM8C5r9gfCCQF5FRS_gbaDMZhIy2avmfUER5QIyky8s3ZVFyvhOG-H-8OVrZ4b2H9GoxlqrAR5eSH6S6zW4cM19A1BdmwHRUjtkCSCW7HY3DXzeewpZAsJHCkWj2Bs7bgjNe3r-RMc7mMyBKjtCI2lt3MH8dG82kGF_4wKgZPM_RFT6JY9_yg_mz0q-nBI3A7LSr1cZaOwScQnBCvHcJQwedj8r-k5rL2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6g480b1TecH2v9KbA_npK-MODXFzA3CtP_poQ4zlXzbgaalpCDoov9ygpPumn2G59FkhblaDvxFV2sn1_D7R93uMbyXX1NNkgBZENXB8KMdBl9A-sY1xp8wrsVtO7f6mUA6nai0MroRYP4zmGV0CA7wgmJ_W1P1nNWjB99X8DjMISf5dxJH5KE1FKV2awDTCkn5DE8jyg5lQK-fIqZ2r4hIlOS2nMseoOjZFaPAtr2bDyrZNX-4W3VTOZpFF4AkGP_y5zcifFqgEHUHZsHI7oMRxk3KHRjF7exLJkjWaRmgIgty74p533hCahrPtw2Tly8niUJo0mVmAIJ5qeZwSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb22e4cb2c.mp4?token=rk7aFjymvzeWTFPBXpecf3rgogpxgMgxPAWmnWqDH7fAVA-UX500imfcYANabS116-fMP8IGAnPHyqfiIwoA3A3gswUCkE7V49_TFgtTFAkETqLoI6C0C90xG2bk99I75fmPR_zwwxTtjgnvtJJiUg2e047Zz4eDYaqcuKkyGSGY8ho_oZFYakRnp5T0KwKSwrA65majxYd9_ag2fbY155L06PEPZcRaB1QtEmoGLIpa6sV6bW2XhuySZ-ciX3UKmBGvHyhusNdL2-McJaZIpCXvVv5cwHEnnwf39f2SA2XDUnEFyCAjLqc_ow1KmBhzysfUDmgY9pLo6bzBfTDn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb22e4cb2c.mp4?token=rk7aFjymvzeWTFPBXpecf3rgogpxgMgxPAWmnWqDH7fAVA-UX500imfcYANabS116-fMP8IGAnPHyqfiIwoA3A3gswUCkE7V49_TFgtTFAkETqLoI6C0C90xG2bk99I75fmPR_zwwxTtjgnvtJJiUg2e047Zz4eDYaqcuKkyGSGY8ho_oZFYakRnp5T0KwKSwrA65majxYd9_ag2fbY155L06PEPZcRaB1QtEmoGLIpa6sV6bW2XhuySZ-ciX3UKmBGvHyhusNdL2-McJaZIpCXvVv5cwHEnnwf39f2SA2XDUnEFyCAjLqc_ow1KmBhzysfUDmgY9pLo6bzBfTDn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عباس عراقچی در نجف
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139620" target="_blank">📅 16:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139619">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0c519f38.mp4?token=T1RKuqHbeXG9SCLSUhu-49yuQB-XGhRNVYehXxb9ThOt8EbuahN9a905eUMqIGv5smt-KMrhP1Q68O6OXu4l-Uuxg-1NuKwUN76sUoACuKCNQEcOOznG5Y5RtSnPf9OekLngDegQInBvaA_4DneSW8o_cjuOOYJ4T4SWBYnpz8WMJtcxtVqyQtvQRhUCN4abJjG8cwNNK-q1drWTDfAA92ndYL95LK9ojF2Wojg1dFMnr6xwh428rzmxaKAa8b7_a7I7G1uwYAYSG6niT6VN5kbtFDh2ed-2h2_Y8CHR9DwdlqmWK7a0MfZACEIIIBcY_2kgOwj5SF1IIcdaAbZz3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0c519f38.mp4?token=T1RKuqHbeXG9SCLSUhu-49yuQB-XGhRNVYehXxb9ThOt8EbuahN9a905eUMqIGv5smt-KMrhP1Q68O6OXu4l-Uuxg-1NuKwUN76sUoACuKCNQEcOOznG5Y5RtSnPf9OekLngDegQInBvaA_4DneSW8o_cjuOOYJ4T4SWBYnpz8WMJtcxtVqyQtvQRhUCN4abJjG8cwNNK-q1drWTDfAA92ndYL95LK9ojF2Wojg1dFMnr6xwh428rzmxaKAa8b7_a7I7G1uwYAYSG6niT6VN5kbtFDh2ed-2h2_Y8CHR9DwdlqmWK7a0MfZACEIIIBcY_2kgOwj5SF1IIcdaAbZz3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های «وحیده عظیمی فر» وکیل پایه یک دادگستری؛ در مورد حقوق زنان در ازدواج.
مرد فقط با اجازه همسرش میتونه زن دوم؛ سوم و چهارم بگیره.
حق حضانت فرزند تا ۷ سالگی با مادرشه؛ بعدش هرطور که به صلاحش باشه.
حق طلاق با مرده.
جهیزیه مال زنه.
زن با ازدواج مجدد مستمری شوهر فوت شدش قطع نمیشه.
زن خیانت هم بکنه و حتی خیانتش محرز هم بشه بازم مهریشو میتونه بگیره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139619" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139618">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
دیده‌بان حقوق بشر: افغانستان همچنان تنها کشور جهان است که در آن دختران پس از پایان دوره ابتدایی (پس از صنف ششم) از آموزش محروم هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139618" target="_blank">📅 16:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139617">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👸
شهبانو فرح پهلوی 10 سال قبل از فتنه57 تو بهترین محله پاریس برای دانشجوهای بورسیه شاهنشاهی ایران یک خوابگاه مجلل چند طبقه میسازه
🔴
حالا اعتراض دانشجوهای چپول اونموقع چی بوده؟ باورش سخته اما اعتراض داشتن چرا این خوابگاه بلندتر و زیباتر و باشکوه تر از خوابگاههای کشورهای دیگه اس!
🤔
احمق بودن طرفداری های رژیم جای خودش چون ما میگین اونا از احمق بودنشونه که نمیفهمن ولی چپ نفهم که با بورسیه دولتی برای تحصیل رفتن اروپا و آمریکا از حرام زاده بودنشونه که نمیفهمن یعنی درآمدشون از همینه که نفهمن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/139617" target="_blank">📅 16:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139616">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c6686423.mp4?token=HNm4y__Hi0Sf086f2gOdWCenZVCW8J4o6mW9vErSl4xodgQLbgDi7q9vNDq7PGumaMIj98DquGibheJxOecavJAQRHUmH6KbN8z32f5drjS-B9LJS9LzfR4hYDCogCa4lDG3_FYYoCobBi_bgofsb3tp0xLhx8LWg3vs1EoOipua3Sl5-Ab3lwfD_ohHSZeG0xnOPuG8334tCXWI4lNXnj1oU2-0VF4MkjWynEo-m1JbzghPeuzPUoM0Z2rdFscOw2DKX-JTimgMEvsa4KQOC4DlJ4qfV_m50Be83SOVT1W7OLJOzyO8-V1lW48D1Z6tfYGiT8BJo9KGNkigv6o39Kjq2s1isWG_RbkZFgVm_fcCLp3_1fbxpZM75z_S2sA6Df6lW0CjlErZMuo1uoiYZM6TXiPdJ4lE-VLRiTYInmG9ENxuVnVzu3QDDuOHU2azQ7bFwmyDVCXwQeIrHm_dfsFi1v8a6mpzXk2iCwFAUDMZ_eJErz2snfhkpiWVPZMZfJHmPLs1op49z28Trlb4lZWbFIwqSvbW4r9HFqIpE8LKePDOX3zuI2q4gcD_yjM4S5avI5Pf25nOy-HiYNvjyvQqLGuo4q10OvFYDrr-PLGeHhtT_AJ739URFug_8Tyu7wyjU__bpjijcwBVwwceRCulxP2CwNfFz0iitAZgl1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c6686423.mp4?token=HNm4y__Hi0Sf086f2gOdWCenZVCW8J4o6mW9vErSl4xodgQLbgDi7q9vNDq7PGumaMIj98DquGibheJxOecavJAQRHUmH6KbN8z32f5drjS-B9LJS9LzfR4hYDCogCa4lDG3_FYYoCobBi_bgofsb3tp0xLhx8LWg3vs1EoOipua3Sl5-Ab3lwfD_ohHSZeG0xnOPuG8334tCXWI4lNXnj1oU2-0VF4MkjWynEo-m1JbzghPeuzPUoM0Z2rdFscOw2DKX-JTimgMEvsa4KQOC4DlJ4qfV_m50Be83SOVT1W7OLJOzyO8-V1lW48D1Z6tfYGiT8BJo9KGNkigv6o39Kjq2s1isWG_RbkZFgVm_fcCLp3_1fbxpZM75z_S2sA6Df6lW0CjlErZMuo1uoiYZM6TXiPdJ4lE-VLRiTYInmG9ENxuVnVzu3QDDuOHU2azQ7bFwmyDVCXwQeIrHm_dfsFi1v8a6mpzXk2iCwFAUDMZ_eJErz2snfhkpiWVPZMZfJHmPLs1op49z28Trlb4lZWbFIwqSvbW4r9HFqIpE8LKePDOX3zuI2q4gcD_yjM4S5avI5Pf25nOy-HiYNvjyvQqLGuo4q10OvFYDrr-PLGeHhtT_AJ739URFug_8Tyu7wyjU__bpjijcwBVwwceRCulxP2CwNfFz0iitAZgl1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه احمد الشرع: عملیات نظامی تنها یک ابزار است، همه چیز نیست.
🔴
وقتی با واقعیتی مانند آنچه سوریه با آن روبرو بوده سر و کار دارید، نیروی نظامی به تنهایی هرگز کافی نیست.
🔴
شما همچنین به یک استراتژی رسانه‌ای نیاز دارید. به افکار عمومی نیاز دارید. به توانایی اداره امور عمومی نیاز دارید. به ساختن نهادهای نیاز دارید. به یک اقتصاد نیاز دارید. باید به وضعیتی از توسعه دست یابید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/139616" target="_blank">📅 16:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139615">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
مجری صدا و سیما: آقای شهید ما میهن پرست ترین رهبر تمام تاریخ ایران هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/139615" target="_blank">📅 16:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139614">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaYFCvpxy4Uyyf9gkkv6WG0NCoD_SNie4XPBwObyVp00myDtU2g9gAxhoyDVpsadNL4Zw0C9CKbJLo_GV4Fuo3eXhvt7HGaG8VEYSwRAIM2GD9Q27i3U0aY6Qc_02YDu1d2mRxEyCblwvGepQZKiTNZW04BQcgrcdW7BOyVAeKn2DZIKZ52y6a7kGK0XijlOk4tDqYFgQJljEyQ5z9ed74gROn98Sjo0o0McqyYX1QN_Dwam97jVlo7qxNeFe5adYTkv00KPDL2jdF3GYRaQlG-TRgq_ZyfCG7CnAJhRv_NbhFuIcf7zTQHrKWdw-USdYSYdAKIIiwYLPgf8cB3srA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه کاربر خارجی توئیت زده که اگه نقشه ایران رو برعکس کنیم شبیه ترامپ‌ میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139614" target="_blank">📅 16:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139613">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725521aa48.mp4?token=oR7pCIxdOiIh7WnxUJPVvHHnQYr-nCyOqlPj2Jw5BnBH2Ttt5XOR2IgNFcOz7_pzh3sI0zu7xN3PEo9iI2eWNZryAQhYLxwj-MkABOrVCG3sITbsvxjsVLb3v1vwGrv4GyVGIaEBlu9f94S0VefmvvPsEqGx9cLtdBVnmB3TugJ3vN5y--WsqsSaOZw1GGnwWkDbm1ltTEaKlUEZcjedF9BAJJ23RX_K08iJrPpJ7R9zGChSczqhtJl1yUvQXV7gWb_u1mfyXAPEy3sPQNL05Ur3jbBlLaI4pMwHZp7vXLrh7RnnuYi4gcjHwk2-QI3ryd291kmIzqJOkCqw6wMb5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725521aa48.mp4?token=oR7pCIxdOiIh7WnxUJPVvHHnQYr-nCyOqlPj2Jw5BnBH2Ttt5XOR2IgNFcOz7_pzh3sI0zu7xN3PEo9iI2eWNZryAQhYLxwj-MkABOrVCG3sITbsvxjsVLb3v1vwGrv4GyVGIaEBlu9f94S0VefmvvPsEqGx9cLtdBVnmB3TugJ3vN5y--WsqsSaOZw1GGnwWkDbm1ltTEaKlUEZcjedF9BAJJ23RX_K08iJrPpJ7R9zGChSczqhtJl1yUvQXV7gWb_u1mfyXAPEy3sPQNL05Ur3jbBlLaI4pMwHZp7vXLrh7RnnuYi4gcjHwk2-QI3ryd291kmIzqJOkCqw6wMb5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوان ایرانی
💔
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139613" target="_blank">📅 16:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139612">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
هاآرتص: اسناد افشاشده نشان می‌دهد اسرائیل پهپادهای راهبردی و سامانه‌های نظامی بسیار پیشرفته‌ای را به امارات فروخته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139612" target="_blank">📅 15:59 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>

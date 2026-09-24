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
<img src="https://cdn4.telesco.pe/file/Q5yFJA0fRnTH-Y54-P2Dc00ivjnLrv7qktmKOANYfMwVCFpu5VkoiaHO7eDt6BXTWB6xOaFoV4A-veg0J3sU3yP0PlGB4PaKVayawmCxalVPGvNTJisykb6oBrWaag1bvWZHBIJpEPkvmOQH8wf8vqewcowDZIc6VqcgjSwINa_QutZgtTSA3nk4p9G30QY5w4k1O-8FLUpD1IpGFdD4bk77DY8P7q-rpH_xjfVaVLHIfL2YTX2d3bUuSaqPcsfzIbyjAEVZWV5t4Z_NvI7gIPJ9WEmjQ0CA1UKR6vBZXMUQUBAHyqWLNzHO3Nb4eiCVqHXby2P1fPLHTj6B6pGXCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 14:17:46</div>
<hr>

<div class="tg-post" id="msg-149128">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دیمیتری پسکوف، سخنگوی کرملین:
هنوز خیلی زود است که درباره سفر پوتین به گروه ۲۰ و ملاقات او با ترامپ صحبت کنیم.
🔴
ما پاسخ خود را به این دعوتنامه در آینده اعلام خواهیم کرد، اما روسیه به هر حال در فعالیت‌های گروه ۲۰ شرکت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/alonews/149128" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149127">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترکمنستان آسمان خود را به روی هواپیماهای ایرانی بست
🔴
سخنگوی سازمان هواپیمایی کشوری: به دلیل اینکه ترکمنستان مجوز عبور ایرلاین‌های ایرانی را از آسمان خود صادر نکرد، پرواز تهران - دوشنبه نتوانست در مقصد فرود آید و ناچار شد به فرودگاه امام در تهران بازگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/149127" target="_blank">📅 14:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149126">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سرلشکر صفوی: تنگه هرمز هیچ‌گاه به شکل قبل بازنخواهد گشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/149126" target="_blank">📅 14:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149125">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بانک مرکزی: صدور چک‌های رمزدار از سه‌شنبه ۷ مهر ۱۴۰۵ ممنوع و پذیرش این چک‌ها در سامانه چکاوک نیز از اول دی‌ماه متوقف خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/149125" target="_blank">📅 14:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149124">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گزارش اختلال GPS در مناطقی از تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/149124" target="_blank">📅 13:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149121">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFBNsudWwNq4jofOY-APW2Z2xa3OCdxBfHARkOqV-nsAcUB8ZmeyFXPMXo-EUOn5tC36rzoeZSHQGh94VQUHEliqy1_k-LaHm98ZYl6qA5I8l2ZXPnXQhtusAXkWml3OctPZKv3tonmqqo-NhprMFRNsC7D8juILYqbWYI8nbQrLagkaeO_BFEh9fNkiJ8l8BetQR3_HWahVAIMJD9yz5tYA4kAMdsmd-aFe55buRBDGa0QTZJSL_7inzIF7UHr2dNbjDvnjgCN_r0RIqZqWzGMIG5DI5FqZDcUYWiAi3ho8GaDekS911gYq-a2VL9SMTuOHDZW49yGB89gxwSrDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1Hf5ZuF0UsasXGU0NnjeUIUhQXxsQ_xNjLRPryziob43ZspAkwhxte4W6EAXO-F7UO8MhxUPih7vgt53ffxm3ADb5tR1OpsmRFjNEWNA7OxHXguHHPJooK-lVFf7fdZqCqvmOyPU9KNZperY3nQp5wvD-kl11UTmBSth-AVrMokR95-zFo6gKUTbzSsDDIWZ2nbBJ9Huiqn8OILuTS2BIftvHKjROOO-DfxfqS8c5ZUkpQGY6i3XqojZ81TPk0UkJzwNvk8AK7LD3BW4RXMZYBwIXJnMtC0dYmqXeTK0icabu1eydKfd7o-Zjo_TcXsYWvVCsWA_o2q5BrzklDnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhbK3ynexlI-hZgefH-ctsXu5-ub9jvE5QuYHC9e00oeUgm7wUMpyDFMUa4Hg8sULy3Dc-c_FrJQ53VZnLLGnlYBHLKcE0nPo1okQ-FgACqX-0iepWJRctIvPwXbHS8fWNe1WmwfdxZwuDfnlcfl-44L-u7vDmOtqqtS6rg7HyJ9IloRC5Fm17PSdMzYD3OLP8rHO1VmRFv8UNpREnyA0mUZS7ZQ1tlvr8BAQuyUTnrnwrC-_5_79KQh0RPYezPhoglh0i3-fuSSzH3ih0yBo4NpJ89h1qJTmvs7IJHDT8wJa4PYGrfPpWi8Lb6UIb3oRokgWfMAOLHilGdjVIP7Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149121" target="_blank">📅 13:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149120">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP5yknpy3d5HkL1frf31GLdDVH_bfFVdAX4G12R9i291ZgbOJPZPI_CM71bcGh5yiWS_bkDVa8Zg4tYRi4-Z_u5PFXg6nuH82Mn6lVhTwsDqxW1BR9yeZKHR_kZkI3JDqt135uIgx1kTZJTv0kcFGrn0kn7Av3aJywjS2e_AxBykvoAZy_ItsyCogy6w1SYZdZmJS1UkBRQY0oDgWxgwhger5SRQNtb2NI76ao6KPloRdDsonyEb4sxjs0rf486FENteFXXahRzbkQRELeq4hzi3y2idegI-2BhiiWoURlVMaURNr43puBeNHTY4gLJG0xPKbDxuG8GwLMUbNIP0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۱۰۶.۳ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/149120" target="_blank">📅 13:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149119">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO7GeVPzPv1haVe0liiKDMV4rtTbpjF8QPXMuCHkkHD3nsAjQN6BNIZ3p4nFKfeHS9s69LlTNgGuLgcHEkS6_r87zQTRpG1c1ijYV_I6mpEDxTviDl2Jd7zWgIHVed7o7Y3YAdOWQ-jzujmectyPWE6l63SbfTSHO3ThzxMrW5L7PReYo4ItEM-JGLEENyi_apIUwkzikWX77UxQMspyrvgKam5Zlk5Kp3l2NIhsyeW-FcZ8ifK-nnlxm0RVlsLi0wknyYkZMF8W0SVcAf4eyPNXkvlcA7aswWRi5TLZIxMxQehUfegYf-rDg6uuIhXOQStDTYQ91F5VZFeckgAPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر جدید از حادثه امروز در پالایشگاه آبادان
🔴
صدای شنیده شده امروز صبح در برخی مناطق شهری آبادان به دلیل نقص فنی در یکی از واحدهای صنعتی پالایشگاه آبادان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/149119" target="_blank">📅 13:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149118">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
آرامکو: ۳ مسیر برای صادرات نفت داریم/ در حال بررسی ۲ مسیر جدید هستیم
🔴
رئیس شرکت نفت عربستان (آرامکو) گفت ما هم اکنون ۳ مسیر برای صادرات نفت در اختیار داریم و در حال بررسی ایجاد چهارمین و پنجمین مسیر صادراتی هستیم.
🔴
وی افزود، وضع انرژی در جهان بدتر خواهد شد زیرا قطع جریان انرژی، زیاد است نه محدود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/149118" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149117">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
یک منبع اسرائیلی: ایران فعالیت‌های خود در زمینه انتقال و تقویت تاسیسات هسته‌ای خود را در منطقه کوه کلنگ در نزدیکی نطنز، تشدید کرده است
🔴
در صورتی که تهران از خطوط قرمز عبور کند، مجدداً برای حمله به تاسیسات هسته‌ای ایران اقدام خواهیم کرد.
🔴
ما هیچ فرصت واقعی برای دستیابی به توافقی بین ایالات متحده و ایران نمی‌بینیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/149117" target="_blank">📅 13:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149116">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a5b9bfa1.mp4?token=F0dfaYHf_bu2NsTkAyWt8o2npDUYT6j_pTuwGv5s7INB1KJwWfT8WtGFS1hBLI3e1pf8epYPKbPUZnvtaj0a3pmSTYt2G86V_vhj-kowHiXwtvJwgt5I18MPs_tCb7gPFYxq6pM7YM_YEJabHRLoXH8wNPzAn8-lkvusodPxqcimUOQOePYndqdfb-ZCX0DPUIHqEtvK2QLy4b0mCT2clMRm50d3s2RnMX8g7R71xUmBqaXVBRmhLxcDuPeTWftwsQXnCZh5VADqc2dDMM580ZZjOZS5NgOFC2AT_nZDdatBgbjTkbrdN2Jlvq-d_iefjtyDMCbv8It3h7s0gW8FIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a5b9bfa1.mp4?token=F0dfaYHf_bu2NsTkAyWt8o2npDUYT6j_pTuwGv5s7INB1KJwWfT8WtGFS1hBLI3e1pf8epYPKbPUZnvtaj0a3pmSTYt2G86V_vhj-kowHiXwtvJwgt5I18MPs_tCb7gPFYxq6pM7YM_YEJabHRLoXH8wNPzAn8-lkvusodPxqcimUOQOePYndqdfb-ZCX0DPUIHqEtvK2QLy4b0mCT2clMRm50d3s2RnMX8g7R71xUmBqaXVBRmhLxcDuPeTWftwsQXnCZh5VADqc2dDMM580ZZjOZS5NgOFC2AT_nZDdatBgbjTkbrdN2Jlvq-d_iefjtyDMCbv8It3h7s0gW8FIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاکستان رسما به ده نقطه از افغانستان حمله کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/149116" target="_blank">📅 13:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149115">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پرواز ایران‌ایرتور در مسیر تهران–دبی لغو شد
‏
🔴
بر اساس اطلاعات درج‌شده در تابلوی وضعیت پروازهای وب‌سایت فرودگاه امام، پرواز امروز پنجشنبه ۲ مهر ۱۴۰۵، برابر با ۲۴ سپتامبر ۲۰۲۶، هواپیمایی ایران‌ایرتور در مسیر تهران–دبی لغو شده است.
‏
🔴
گفته می‌شود: امارات اجازه ورود این پرواز از ایران را نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/149115" target="_blank">📅 13:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149114">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پیشروی ترکیه در شمال عراق برای تصاحب اردوگاه‌های پ.ک.ک
🔴
منابع رسانه‌ای از حرکت یگان‌هایی از ارتش ترکیه در داخل استان دهوک در شمال عراق به سمت کوه‌های کاره و متین خبر دادند.
🔴
طبق گزارش‌ها، دلیل این تحرک، تحویل مقرها و اردوگاه‌های پ.ک.ک پس از خلع سلاح و عقب‌نشینی نیروهای آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/149114" target="_blank">📅 13:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149113">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ccce0989.mp4?token=AJ7Be4Lhi2uSSgfh5-Slu-76SqnT3ibG_T-KnyY917-ZET19dQY1Eg0550NGsf4RgikB7e3s1rNNzIwaEBVifURpI_d3MkxhNOXEq1Q_W5wyGn1U7cyhM8XpIKp6Ot00ZzPbMpuwZlFF9IeSh2CkShcYVLzzsoCMPTQO1gJ620h_xEyEheinbfuuUPbjYLRBQVm35_5oHdMVnxiNDwWqA1XAUE3yMN82AtNrKjEJyrAc9AfllMutNNf2UHroPtK24W0SA9tjnGEY168HJlKjA18DbqgjrGH4u0TlNtvLsaF_jF1jRH764t8gfJ0uFhafnM1RKqAWyzpBjAx6A9eUBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ccce0989.mp4?token=AJ7Be4Lhi2uSSgfh5-Slu-76SqnT3ibG_T-KnyY917-ZET19dQY1Eg0550NGsf4RgikB7e3s1rNNzIwaEBVifURpI_d3MkxhNOXEq1Q_W5wyGn1U7cyhM8XpIKp6Ot00ZzPbMpuwZlFF9IeSh2CkShcYVLzzsoCMPTQO1gJ620h_xEyEheinbfuuUPbjYLRBQVm35_5oHdMVnxiNDwWqA1XAUE3yMN82AtNrKjEJyrAc9AfllMutNNf2UHroPtK24W0SA9tjnGEY168HJlKjA18DbqgjrGH4u0TlNtvLsaF_jF1jRH764t8gfJ0uFhafnM1RKqAWyzpBjAx6A9eUBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بِسنت درباره ایران: ممکن است تانکرهای نفتی مورد اصابت قرار بگیرند. بسیاری از آنها به مسیر خود ادامه می‌دهند. آنها به مسیر خود ادامه می‌دهند.
🔴
می‌دانید، ممکن است ایرانی‌ها سه، چهار، پنج یا شش پهپاد را به سمت آنها بفرستند. ناوگان قدرتمند ما مانع از این کار می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/149113" target="_blank">📅 12:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149112">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f2a4fb766.mp4?token=TQBszxj0Td8xCLyjeHXCc3baG2HMzX7cFjb55B5tFc0sf25TZf7WjFdfhWRc9k601hWoovfXYbQ5atA_S8FJO_78H30_vmixBgtNW9WqFGIF_7vNROetjEVF9JOroXy9z3e1ss8areItCRVHBMxpxewUkyzdGmCfpNuDhRlrz141aueEdQ-997uo3ZNOm04LqaueblpbQho0uGL3tvvtZe2aS_WVjf_ZITzetY_HuvB5VrTqk2ekGSW4EqP4BGMh0fgr35nkJIlC6z3Cz3c_OCT5jViwgSe9cG0HAZGp3F8DRujza1COT5UiX5ueEL7e3hq4sMMQVdPuTBXQT2N1hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f2a4fb766.mp4?token=TQBszxj0Td8xCLyjeHXCc3baG2HMzX7cFjb55B5tFc0sf25TZf7WjFdfhWRc9k601hWoovfXYbQ5atA_S8FJO_78H30_vmixBgtNW9WqFGIF_7vNROetjEVF9JOroXy9z3e1ss8areItCRVHBMxpxewUkyzdGmCfpNuDhRlrz141aueEdQ-997uo3ZNOm04LqaueblpbQho0uGL3tvvtZe2aS_WVjf_ZITzetY_HuvB5VrTqk2ekGSW4EqP4BGMh0fgr35nkJIlC6z3Cz3c_OCT5jViwgSe9cG0HAZGp3F8DRujza1COT5UiX5ueEL7e3hq4sMMQVdPuTBXQT2N1hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بِسنت: ما از این جنگ در ایران عبور خواهیم کرد. قیمت انرژی کاهش خواهد یافت و قدرت خرید شما دوباره افزایش پیدا خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/149112" target="_blank">📅 12:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149111">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3318463bf.mp4?token=mNpI9hwszxeYuvPi4pYu3aooK3L5TGIt3eIUNHNPgb-wAVzON-42PdKx64FYlyyNVXRGK9ynXwe14Gq0fKcnz75JH9LpuPrph3HXpq0J6lR7Yls1mv5AlHIY-YeqBbliWvv3eILucIB6-_BlpNVwDnziQ5LiiKm0bOC-TKIsKJEBO4z-9asOxs9AvfAWJ6LhwemgR6Rb6-or2efl4Q31xIh66wW2vzM7W5_Ucug8xE5v0x9pU-5DgbmNvBVUq9NottMpHJABKXk3udvTFAMagbq-M9pfdJXIy8GwvRMvXbvMZ2S5PFmHZv55H8kZFYH2axDz_dwkHRTJK-FFgEEraFGr9RAYcxDBT4hNB0OXE5ujXE64JowStak9I6kC7Dl9T49nQ_NS6XCqRQiyGvN2cqN1CGkUfn-cYn50mPq9GGIIH_0TwQ9jfxklf9Bwdp60Tb9Z27ACNBhH0BtzpiWwUPibbaXkUHcb2mGkqKDzCtzwoWKYElBHlAaiSi571NgFHsk_PCFCKzzCQGZdqFR4yOqYWj_fZvvUBJMnU5pSP8xQ9PNqGGN6xRNIgLjrqeGpY-JMqPvAirHJTwTKeeBDhC1Il26iTdYHqpbymjKE-cOIJM9WAfxRAqkKFBq3ck_uIXSfzvU_tKD7zMNqFCzW5lp4tpWEaHt1ypqLz9_ps4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3318463bf.mp4?token=mNpI9hwszxeYuvPi4pYu3aooK3L5TGIt3eIUNHNPgb-wAVzON-42PdKx64FYlyyNVXRGK9ynXwe14Gq0fKcnz75JH9LpuPrph3HXpq0J6lR7Yls1mv5AlHIY-YeqBbliWvv3eILucIB6-_BlpNVwDnziQ5LiiKm0bOC-TKIsKJEBO4z-9asOxs9AvfAWJ6LhwemgR6Rb6-or2efl4Q31xIh66wW2vzM7W5_Ucug8xE5v0x9pU-5DgbmNvBVUq9NottMpHJABKXk3udvTFAMagbq-M9pfdJXIy8GwvRMvXbvMZ2S5PFmHZv55H8kZFYH2axDz_dwkHRTJK-FFgEEraFGr9RAYcxDBT4hNB0OXE5ujXE64JowStak9I6kC7Dl9T49nQ_NS6XCqRQiyGvN2cqN1CGkUfn-cYn50mPq9GGIIH_0TwQ9jfxklf9Bwdp60Tb9Z27ACNBhH0BtzpiWwUPibbaXkUHcb2mGkqKDzCtzwoWKYElBHlAaiSi571NgFHsk_PCFCKzzCQGZdqFR4yOqYWj_fZvvUBJMnU5pSP8xQ9PNqGGN6xRNIgLjrqeGpY-JMqPvAirHJTwTKeeBDhC1Il26iTdYHqpbymjKE-cOIJM9WAfxRAqkKFBq3ck_uIXSfzvU_tKD7zMNqFCzW5lp4tpWEaHt1ypqLz9_ps4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت درباره ایران: نمی‌دانم یک هفته، یک ماه یا دو ماه طول می‌کشد، اما آنها تسلیم خواهند شد (به گریه خواهند افتاد)
🔴
هدف در اینجا می‌تواند یکی از سه حالت جهان باشد: رژیم علیه خودش می‌شود؛ ما نوعی قیام مردمی در ایران می‌بینیم؛ یا کاری می‌کنیم که ایرانی‌ها، اگر بخواهند توافقی انجام دهند، به آن توافق پایبند بمانند.
🔴
این بار، اگر توافقی باشد، به شما تضمین می‌دهم که به آن پایبند خواهند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/149111" target="_blank">📅 12:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149110">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: ما با عمان به یک سازوکار در مورد تردد در تنگه هرمز دست یافته‌ایم، اما واشنگتن مانع آن می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/149110" target="_blank">📅 12:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149109">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سپاه: فردا ۸ صبح تو تهران رژه ۴۰ هزار نفری موتور سواران جانفدا داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/149109" target="_blank">📅 12:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149108">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
مجله «آفریقا ریپورت»: عربستان در اولین واکنش خود به تصمیم واشنگتن مبنی بر عدم صدور ویزا برای رئیس شورای حاکمیتی سودان تهدید به خروج از گروه چهارجانبه کرد.
🔴
گروه چهارجانبه سودان، شامل آمریکا، عربستان، مصر و امارات در تلاش برای ایجاد آتش‌بس بشردوستانه، آتش‌بس و یک روند سیاسی برای پایان دادن به جنگ هستند.
🔴
سازمان ملل متحد از کشور میزبان خواست تا ویزا را مطابق با تعهدات مندرج در توافقنامه مقر سازمان ملل تضمین کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/149108" target="_blank">📅 12:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149107">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9JgsNlqo0-hlnU1jmJdNU0WD9mbAfmLRQyTJZFSelgr_mE91fRmfE1lhbnDZofCIzHQzqjWcJA9UTrxsqNp3qQeJoP7foTh1N7IiFX9TnhfOWV32i9O091BV5YXuaVYU3cD8U50Y98uRim-mvv60kuX__zGqsFobOMhQIbWN97ALZr7BrEc3zeDHOF-YoMdxGpNFt01oCUcHb22EfTTURRVWf3wFZK8Yb4cX0chymu_3Ih9VR4pW3xaYzvz78IKl-ZKiHoqlC9eFWz_1gQMdBi7X2iQSQr9HSg-NWZaRHP2XSperPcIq8zoCaf8iLBL3NJ1hPPd5GBSEgnIA02RCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت ۱۰۶ دلار رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/149107" target="_blank">📅 12:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149106">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
زلزله ۵.۱ ریشتری ترکیه را لرزاند
🔴
مرکز لرزه‌نگاری اروپا و مدیترانه از وقوع زلزله ۵.۱ ریشتری در شرق ترکیه در عمق ۱۰ کیلومتری زمین خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149106" target="_blank">📅 12:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149104">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نان هم بزودی گران خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/149104" target="_blank">📅 12:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149103">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
روسیه: با توجه به تهدیدات آمریکا، بازگشت بازرسان آژانس اتمی به ایران ممکن نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/149103" target="_blank">📅 12:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149102">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4432d3af9.mp4?token=dl16-h5qSbt1Q4kZm3Aay-agRbR2Psav9ZaNfvuPCPFdPYWMQS_ay5ns4H_a8eJxKT8Rqn2DS-Kn7sKAm7FHPrSWOl7QDSifBpgj1heYfudsjwJo1hUWJJmui0K78je96_VSm_L_y8NjQ3qcdVQtR5u5N3Rgef_H___YNSs8mF3nXSvQ8jOroGJnx_XMIzknWnYXGxlfvKQ-F4TFC2St1h1OqGzck9wKu367xmkXyNamupn3y8lHzJyhyeRMBh67fqdk6pXxFybNTzvNT5z-C-d6X4Ic3igCNEQTTAnkV4oiJK5MsDfcPdEej4gTruXn3Wa_9dhWPFCmPDk04irwzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4432d3af9.mp4?token=dl16-h5qSbt1Q4kZm3Aay-agRbR2Psav9ZaNfvuPCPFdPYWMQS_ay5ns4H_a8eJxKT8Rqn2DS-Kn7sKAm7FHPrSWOl7QDSifBpgj1heYfudsjwJo1hUWJJmui0K78je96_VSm_L_y8NjQ3qcdVQtR5u5N3Rgef_H___YNSs8mF3nXSvQ8jOroGJnx_XMIzknWnYXGxlfvKQ-F4TFC2St1h1OqGzck9wKu367xmkXyNamupn3y8lHzJyhyeRMBh67fqdk6pXxFybNTzvNT5z-C-d6X4Ic3igCNEQTTAnkV4oiJK5MsDfcPdEej4gTruXn3Wa_9dhWPFCmPDk04irwzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ دستور داده بود برای اینکه شی جین پینگ، رئیس جمهور چین رو بترسونن، جنگنده‌های B-1 تو ارتفاع کم از بالاسرشون رد بشن.
🔴
اما داستان برعکس شد و خودش سورپرایز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149102" target="_blank">📅 12:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149101">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: بعد از امضای یادداشت تفاهم میان ایران و آمریکا، اتفاقات غیر قابل انتظاری به وقوع پیوست
🔴
اسلام‌آباد ناامید نیست؛ تمام تلاش‌های ما بر روی پیش‌برد میانجی‌گری و توقف جنگ در منطقه متمرکز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149101" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149100">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEaoDbWwS9VXBswTNw-yRoQlv9kMUA23NOJmM-X1wvQAsQWs6qqkb8qc1IfpDzyrZegGn3U_lOS9Td8x3OqVjTgHCU325Rd4BcyVucNyAUzYtONZC9pmui9zzNDblc5yMgtEtdOFBsrF0YOkglJL4qTb7F2KpnxTFlOXuNiCLMy3RL8edHfTykbgSDJPMY_qn15O9Xbo9-iyPWU2QPwCpUT_-zX1ooenkhyYTws_0nwyMjLtVIQx7XV_SRxsrED_lytDEbLr376bcfoyJgP9IAH5bYhauzc45CrDTl_JLEjRaR0w8h9MIIKvN_BJzFagQ27vqkpNMgHucc1dWco-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت همچنان در حال افزایش است و به ۱۰۵ دلار برای هر بشکه رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/149100" target="_blank">📅 11:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149099">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رونمایی از گجت هوش مصنوعی Muse توسط «مارک زاکربرگ» در مراسم کانکت ۲۰۲۶
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/149099" target="_blank">📅 11:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149098">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رسانه‌های اماراتی : در حملات موشکی حوثی‌ها به شهر‌های تعز و صعده، ۹۸ نفر از نیروهای وفادار به عربستان سعودی کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/149098" target="_blank">📅 11:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149097">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diz1O0rGlwYmqISgb87QPeFmVtwnAhtqtgXVY5dBhSTn_83qOwsDKwhsd2-60pHUDFbdTcnaQb32FJ-zQeT0Q7juK-vBgNqVYeDuWVsqcA12ZA7f2UZODjuefDntb4ibRaIIfcH7MTlOaiM8wEtpY9AtzCC2tHEBipI92-1p6rLnPWsEuHsj3D2Jj7k-KfQ7JqvMlslIxPwSHnATAOqG5pFz-aAUHmhR84Zm4QqNM7DKRTb6qW_C_Yp-qxcFlxHffzdtBoKiVULgIaxIzihIlZNtTzK9isGPq5KdKOCfJ4AnPkSwW8q7Gbb7se5EgSu8CDG30pj5gNcmFwct71ZU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرایط امنیتی در نزدیکی محل اقامت نتانیاهو در نیویورک
🔴
پلیس و منابع آمریکا گفتند که یک گروه سه نفره مشکوک در حال خروج از یک چاه فاضلاب، تنها چند قدم دورتر از هتلی که قرار است بنیامین نتانیاهو، نخست وزیر اسرائیل، در آن اقامت داشته باشد، مشاهده شدند.
🔴
مقامات شهر نیویورک اعلام کردند که این سه مرد ناشناس حدود ساعت ۴:۳۵ صبح در حال بالا رفتن از چاه فاضلاب در خیابان پارک، مشاهده شدند.
🔴
پلیس اعلام کرد که آن‌ها با دو وسیله نقلیه فرار کردند.
🔴
پلیس نیویورک در بیانیه‌ای اعلام کرد: «با توجه به مجمع عمومی سازمان ملل و حساسیت محل، به دلیل احتیاط فراوان، پلیس نیویورک در حال انجام بررسی‌های امنیتی بیشتر با شرکای فدرال خود است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/149097" target="_blank">📅 11:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
آکسیوس: ایران از طریق مذاکرات غیرمستقیم پیشنهاد داده است در صورت کاهش فشار نظامی آمریکا و لغو محاصره بنادر ایران، تنگه هرمز را ظرف یک هفته بازگشایی کند.
🔴
با این حال، آمریکا این پیشنهاد را رد کرده و گفته است ایران کنترل تنگه هرمز را در اختیار ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149096" target="_blank">📅 11:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlFgoUEYXVFqv9qNmQSdX0QvZ0t8uUI0BXM-EFCQMBlRw-rkkbaw-3-C8U0qvkjy2LIaQAMHmaTGaiS3f4mdZW4uLWFR7TX4ZASg4v-iZ-Sq6FY2PHDc2TWmAstvvDpvPzElrlBZa_EDPq6JzfHlCjy-KgAowDMi9tAySZOA5vzZT38epfanoSTupj83Up8S7IEjf2MEyODYg69fMYhLF8IHO0D6YfFVNWUFBy19-N2Qa9oqayhtLcT3kuS-BzU3fuSKVjJbP_lBAaOdWVqtD3Vw0Mhx1LN3FLHlSJ1qVyNbAE4DYm-5KlGNkgO-R8HydQNTs14H9WdrxGxnHMpSug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل، منطقه المنصوری در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/149095" target="_blank">📅 11:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کاتز وزیر جنگ اسرائیل خطاب به اردوغان: دست از درگیری با اسرائیل بردار
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/149094" target="_blank">📅 11:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149093">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
انگلیس محدودیت‌های مالی علیه ۵ بانک ایرانی را تشدید کرد
🔴
دولت انگلیس محدودیت‌های مالی علیه پنج بانک ایرانی در این کشور را تشدید کرد.
🔴
این تصمیم بانک سپه، ملی بانک پی‌ال‌سی، بانک صادرات، پرشیا اینترنشنال بانک و بانک تجارت را شامل می‌شود.
🔴
وزارت خزانه‌داری انگلیس اعلام کرد که درخواست‌های این بانک‌ها تنها در موارد الزام قانونی یا شرایط «استثنایی و فوری» بررسی خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/149093" target="_blank">📅 11:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4zlhTAEneTHi-YzI3h_Ld_fjO1eC7ADZ2ziZ68GUAJojM6-jXs_HZqTrxO-82wez-ThaAQc_UV1Y-rqBZ4XmH18JrsPDII1rFZUNv9DoGddvnoNrmqJwtrhp-3OGciSuKxaddkaV2pl7ecuZx3MyXZt-4CIDy9xAHr-Tspk9MqU9ATxhvu8pkCzzUb-WTjAZ7A0vVRC89ZrZFBBCxYlb7_zo8OCBS4tkxMM2kqL05FdNaFQUjXLuiZFDogazh-TuT_s5aD9TRNxpgWFJWnPh6YIbEIbPX0QqcVULUvatm3cAuryWZtnDrOn-1rrr-i3SAb0ypvdxelbzmdWYHwXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب خواهران جانفدارو بردن تو سنگر بهشون آموزش کار با سلاح بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149091" target="_blank">📅 11:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149090">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhOpH8XHFk1nItGoVsWh8SshwZjCJLB04pjlBAa8Le0XJxVrkxXHe1GGDd9PXb_aZ22rTVlJ1zkOqyA0l-DFRA6OZA893tVvaP_xMQb5c7LdZFIgMRhBqA23RLUJnP8XDm9yF5u8pbrdVFTocuo0eHo5mBnA7-a5-O0m3uuLrm30UdjMfo9uWKNRgXoLherFM5PGO-yE3OI0hrirzDIkPzjpawfvKl1TEmRyyQOpUUcS7UhoNanjDcjgPex_vrXO2keo9AuAbjMAJ4pK-gZAwYsC-ARqyJ4f0jq3peY7eNGW9YAW8ldqYJIoLa6F9GMx5afRUD2m7e07KND7tR27zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل: فرمانده حماس که در نگهداری ۷ گروگان اسرائیلی نقش داشت، کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/149090" target="_blank">📅 11:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I-nVUw_NTYH2izcRxO_9TsbrrDij7-ZFxZrZRFDP4ddrC9yU--E5WblDRxTGgKIZU37w4cnvzh6YnuFgjmkT0v_jjiV30Mo6NIi2t5jyJuOdbu7njMaReaRVF3bQjvaFAaEwUGDYHgxKyao2xkqZPzCcMw4jln0-WF42n77RjYN0TF6pZHpg6fvXwBGDhFPcA-6x_QhxcjRHY3EHVpRIL_8wWRwa__k5SEDfDn7a87mMrI_IgXOEL-GoXqyrf-IOixgEl-LLQJYx1oqONQxve8hSyqNxPdTjg1NHHHhpvaimpavPYDyxOuxKQQtaH8qV7UOFsMeVm01XcNz3ROPc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ArvBCEde59xIpE4EAHNax5DR9BkjoMwpDLqluLg7rir1MdAqbhSqAKWa4IFsxUhWTpLnpbTJTsC--DFrl5WSWdIiOasnn5mAOW-TAjjWhBoURwd0xL_O8Vf90_6AVezl-KnjUwUQvZfPLUWuZrQff1uLbtTBdT25V-mFxFLD2Gvl9kFpG8JtHLUbWAmfLI_lWIH4_YlCxfk8mEA_L9cyJ2cfdE_hD8szxZRmmZ3oM3ugcIkgmES9aoX_KzzP0VP-SNnDvJY0rLKL_V5k4QY2WvYTVPovS_QyIXc6Kmq974BMyF3UAynsbMnElfsLTwVi8-oBNvXQW_uEhSgNaf9nwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JVwEE9kRn41bzuPKy162_4BicoFphT_rkpTRj_hdj_yxMB-D7JNT5C2bery7K6OUumuSWZR6dAkg2MVsb9yFvONJcADYza_1JOgMLpMmCcaAzoZGVLB_m9B8wXSdolQ72aA6JfqinhHh8S3HW9oHrYuF75r0ieeqUj7_rffSTOSTUB6bGTMlxGIsas1KnmyA-moYbCjmLEfntHpqfFR8UOj1MfDwsxMB42czr5ZpU6O7Vb_ch0q3MmH2c81SPrZMZ25xR-UqLtOUp_xafib03MD6D_Fua4kpKYV6JU_nXIj2hp4ZsODaSlNZh6_Z8LSou12aBnxsnaT3im_Pye5tLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gc8kfh2JOyHW2GdEYkS5d3kZXsDRn0cs9Pc82A2lGpTD_jiE5ZhuEIi4SK9nm-tlB4-mZ8dDlQGzjKff_y64KyQ530rgieKwJGtsPYSpvTjsPuH41QojqXBAXWEkfso6I-47929eGQxqcfWvbq6GIV7P-iekYKlZagMY5RjuW3Qqr6RNOapmCobKiccWYLT9IG1i0h6Wr40u3bxYsM-fjPcttTOHCxUvSkbopHjrtME2RQ-0k9qop8NKR3m5VTeHf7-K7HypHAh2vnMFoNaooVfq7We3uz0vR4L7_Z0Ej5RMmQfhmJ_DdRwzgX2k9Db7f5Wja8dA1c5ecQWSnxAlaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سی‌ان‌ان : متن کامل نامه کائو، سرپرست وزارت نیروی دریایی آمریکا، را منتشر کرده است
🔴
اشاره به تلاش‌های ناموفق برای خودکشی در صفحه دوم نامه آمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/149086" target="_blank">📅 10:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پزشکیان: در مجمع عمومی سازمان‌ملل از حقانیت ملت ایران دفاع کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/149085" target="_blank">📅 10:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ایران در مذاکرات غیرمستقیم با آمریکا در نیویورک به واشنگتن یک هفته مهلت داد تا با خواسته‌های تهران موافقت کرده و تنگه هرمز را بازگشایی کند.
🔴
با این حال، مذاکره‌کنندگان آمریکایی این درخواست را قاطعانه رد کردند و گفتند ایران کنترل تنگه هرمز را در اختیار ندارد و درباره اهرم فشار و قدرت چانه‌زنی تهران نیز ابراز تردید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149084" target="_blank">📅 10:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToKxlfQJ_JqbCl2yMX6_RsDd9TfVe0NrEkdVn1AQ0a-xvx5zgGpbEkX0vQv_ma2QIpyBfs1DUVYN9bWK4v9NgnIt0cYxIGW2O_YZeIkMqirbxvAqEwi8NiHAxnERs8AbwJ19G0DAM2Q22omKEHEfFesgmI_rwQvlHeGGRND5VfKOqYvyJFppwXmlGwPfyxdGczZtwplkkdWQcHEzUGJx2iqjUGJsi7YcJflY2yNHkxtTDW0o1tfsbmGoSuaErBk2Y4qBh2K6Bei4CPCRDP86J5zm8LD0-fxK83VNxt97CrNJNLZA9iJASXGCbcrZqWWYF7s31beXpBgac1wvYB6OlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ال‌موندو: سیا به چند دولت اروپایی درباره حملات احتمالی پهپادی روسیه علیه کشورهای مدیترانه‌ای از جمله اسپانیا، فرانسه و ایتالیا هشدار داده است.
🔴
بر اساس این گزارش، روسیه ممکن است پهپادهای Gerbera را داخل کانتینرهای کشتی‌های تجاری پنهان کرده و از آب‌های بین‌المللی به سمت اهداف پرتاب کند.
🔴
مقام‌های اروپایی معتقدند هدف احتمالی این حملات، تضعیف حمایت از اوکراین، ایجاد شکاف در ناتو و افزایش نگرانی عمومی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149083" target="_blank">📅 10:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0NjR30mBx3aCTcbouSR5fHljpnpeOlB80JLMoBCV15nX4yUnonhOJMPegPqmZ__GqDaZIBvwfBM_tWpDiP9VK3gYQ3Hk5ORDNmxLaTkok50eU44rVVo2M4aBSfoJx1ZJ5c01xXs5IoCU3aZfSLZFRJygzsbE6pA4OC_rUNflOCgXmYgcMwcqLK_AWmdf-2ELVaTsaL_LCxri-0ZWw3AwXZ1o87wkuAcoTn-4nWntu4g9EMig7L5S0RxEVBEaHzo-Qan31Bnm2cM-NztIbe-3U_fyXH9FZlKY-yl5AXaz_EEMCV-ZFbmFuueIQ19k8wh0yEbXYnvGVWgp8y-5TGNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ در تروث‌سوشال:
«روز بزرگی برای بوئینگ و تولیدات آمریکایی!
🔴
امروز ترکیه و بنگلادش خرید مجموعاً ۱۱۱ فروند هواپیمای بوئینگ را اعلام کردند و گزینه خرید ۵۰ فروند دیگر را نیز در اختیار دارند.
🔴
این قراردادها به معنای ده‌ها میلیارد دلار فروش و افزایش صادرات آمریکا و حمایت از ده‌ها هزار شغل آمریکایی در سراسر کشور است.
🔴
وقتی در آمریکا تولید کنید، از آمریکا صادر کنید و از کارگران آمریکایی حمایت کنید، شرکت خود را قدرتمندتر می‌کنید.
🔴
به بوئینگ و نیروی کار فوق‌العاده آن تبریک می‌گویم!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/149082" target="_blank">📅 10:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پزشکیان: وقتی سخنرانی ترامپ در سازمان ملل را شنیدیم، نگاهمان از متنی که از پیش آماده کرده بودیم تا در مجمع عمومی قرائت کنیم، فراتر رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149081" target="_blank">📅 10:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149080">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/842589bc02.mp4?token=Br-q28gpnYDzKwxQFAwssbY86-xCyAcM32yG-qrp2HOUSFb6Z7IDF8zz7fVFLhDzZ4WnoAnYXPmdX9OCgzBMuQXJ3crJ7SE6PcmLY_FEofCJUbBz-wW2uwEpG9wRldwIavgyj9od2sDRXjS3pXOnn6YAt1HCpW9jiafKYISfUrTvN3DgaSa1TVNyITKP8nrW8iitJULuPDCAGdSTRHS9R80TXHubjVVuYb6b6VgqQ3dPwkjt2KucKYNsK6loxh67CLt66IofnKbal_ZeU20MvkGxjcAn61A8IVaMxKJO12r_gHz7Q2_vcA9Z4FAgE4FF0MLD0hzuvg16cG1TxZwnPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/842589bc02.mp4?token=Br-q28gpnYDzKwxQFAwssbY86-xCyAcM32yG-qrp2HOUSFb6Z7IDF8zz7fVFLhDzZ4WnoAnYXPmdX9OCgzBMuQXJ3crJ7SE6PcmLY_FEofCJUbBz-wW2uwEpG9wRldwIavgyj9od2sDRXjS3pXOnn6YAt1HCpW9jiafKYISfUrTvN3DgaSa1TVNyITKP8nrW8iitJULuPDCAGdSTRHS9R80TXHubjVVuYb6b6VgqQ3dPwkjt2KucKYNsK6loxh67CLt66IofnKbal_ZeU20MvkGxjcAn61A8IVaMxKJO12r_gHz7Q2_vcA9Z4FAgE4FF0MLD0hzuvg16cG1TxZwnPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله پهپاد شاهد-۱۳۶ به سوران در اقلیم کردستان عراق منتشر شده است.
🔴
این حمله در حومه شهر سوران انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149080" target="_blank">📅 10:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149079">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نیروی دریایی آمریکا: ۸ ملوان ناو هواپیمابر «آبراهام لینکلن» در جریان مأموریت طولانی این ناو در جنگ علیه ایران، اقدام به خودکشی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149079" target="_blank">📅 10:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149078">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFmH7vXY_Bm5PjlHQPZ4r11j7fYtiOuqHULkD3uatEPYXfNx8cBQgYiMDS2uJkvr6NEx37XF2N-xP4RtPtop9I48tl8QhxrKOLmaF39Y01Lwvq30LJnq7NHiTWoZ-52Q5Qa9Z9kIFmD9sxTYlmA-uux4KKCE9Ti_ghriyR17kCDyb6Vgv3bFrrbVIa5J-35Pho3pND_UPhXB3EiyA84Xi82OIwEjeZQwMSxgEtMiNpjR5vmANfVy-EDChwuNkqmgEJOrcWAKIKyZeqRlxiAvbqqZ06bKExpR8-PR5VIsDBUKI_rSM_p_sYl5NCTvbJ13HThuzgUXKiJ_ZKpkTCpD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ: «این ادعا که کاخ سفید یا من می‌خواهیم نام من را بر تئاتر فورد در واشنگتن دی‌سی، جایی که آبراهام لینکلن ترور شد، بگذاریم، یک دروغ مضحک است. این خبر جعلی است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149078" target="_blank">📅 09:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149077">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
صدای شنیده شده در آبادان به‌دلیل نقص فنی در پالایشگاه است
‏
🔴
استانداری خوزستان: صدای شنیده‌شده در برخی مناطق شهری آبادان به‌دلیل نقص فنی در یکی از واحدهای صنعتی پالایشگاه است.
‏
🔴
متخصصان درحال برطرف کردن مشکل هستند. هیچ‌گونه خللی در تولید بنزین ایجاد نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149077" target="_blank">📅 09:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149076">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
زلنسکی: طرح آمریکا شامل آتش‌بس درباره تأسیسات انرژی و بازگشایی کریدور غلات است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149076" target="_blank">📅 09:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149075">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8b8f260d.mp4?token=hY-C618ONke2y4bghSouyrObDYLpRt-2q12-9l-_o45BoQWqmjsDK4k-4zQVHCUKb5uqplfyk3Q8dN4pqvlXit5eTrORvDhUkH87WQ1ivgUdVLJuy9tKJidpArHeflRvVyCX0q4gLeEn93Kaat-kt4r8OIDK9W5A6ZQzYVFONe_46yrG8tNWTbiMQs8_RXBOuhr1AYWlHLa2FcKYQMYznbK-q_grWPZcUmcaJtfzgh7Mz1F-PX7dyAXXH18ofrY-rN5aFr52M5yKPV49eywLyDlAAcDE9v8N06fVnW4YC0qNTCB5MXQWxU-WW4drGABB2vH5iLOxyGfkcBCf1nQ7QmSIBHrdSwBJUhlbBJCPywCuWTowYF4ryYIYYub5nMp4GBucYM-mTfKu4TMonUjXttZBMqwwAJfWVhoviBSTGuXFYI8xmbiv2VbbIfct5PYju_6JSQtKJomkFwhf9vnCHjZjZwT5Cy2Mo6-u_w6-qeqepPLf7ORgYx1rumv7eFkrT6_93e58vbRGPskfNmfyY-jxJKBWi_1pTP9qz8Ut1tvi4IJVXqhDjg8sQq1rDdlfTzU7jxZARKyzf9BRYoXeh5e9pR2E_OcViuUNE4Z7u9odMI5FuZ5yfvy_5HkvIdOjGzs4k6jZPC-Ih6TlSCM9Z8Vf4krWlB7MO50SPMNYLfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8b8f260d.mp4?token=hY-C618ONke2y4bghSouyrObDYLpRt-2q12-9l-_o45BoQWqmjsDK4k-4zQVHCUKb5uqplfyk3Q8dN4pqvlXit5eTrORvDhUkH87WQ1ivgUdVLJuy9tKJidpArHeflRvVyCX0q4gLeEn93Kaat-kt4r8OIDK9W5A6ZQzYVFONe_46yrG8tNWTbiMQs8_RXBOuhr1AYWlHLa2FcKYQMYznbK-q_grWPZcUmcaJtfzgh7Mz1F-PX7dyAXXH18ofrY-rN5aFr52M5yKPV49eywLyDlAAcDE9v8N06fVnW4YC0qNTCB5MXQWxU-WW4drGABB2vH5iLOxyGfkcBCf1nQ7QmSIBHrdSwBJUhlbBJCPywCuWTowYF4ryYIYYub5nMp4GBucYM-mTfKu4TMonUjXttZBMqwwAJfWVhoviBSTGuXFYI8xmbiv2VbbIfct5PYju_6JSQtKJomkFwhf9vnCHjZjZwT5Cy2Mo6-u_w6-qeqepPLf7ORgYx1rumv7eFkrT6_93e58vbRGPskfNmfyY-jxJKBWi_1pTP9qz8Ut1tvi4IJVXqhDjg8sQq1rDdlfTzU7jxZARKyzf9BRYoXeh5e9pR2E_OcViuUNE4Z7u9odMI5FuZ5yfvy_5HkvIdOjGzs4k6jZPC-Ih6TlSCM9Z8Vf4krWlB7MO50SPMNYLfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا: «برخی تلاش می‌کنند در امور داخلی ونزوئلا مداخله کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149075" target="_blank">📅 09:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149074">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: احتمالاً بیش از ۸۰ یا ۹۰ درصد پرواز های خارجی ایران لغو شده‌اند
🔴
حتی مطمئن نیستم نمایندگان ایران در سازمان ملل چطور قرار است به کشورشان برگردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149074" target="_blank">📅 09:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149071">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3h2Taz4x2NfvvP8yHAXiP2hFPW9r10-E8-cFT0JSeGf1LkxIMLbeF9D9LC3aEvcmd84OhdMHnVFKh8dVx9vi8f_okcY2Ez_3M0HG02-y_iIUCUXceokz9sRp27acTKFNTfsN-KX-mV1I4ygcOobDA8Hen2IsfMRkNTOkT_nUGhAeRQy2qk_KgFLOOhQNByjZ5u4Q3Sh_sujkuGpwQF-MjiiRs85ARB77R0A-F8NNc497fdXVZZogH_ZWaPHX7RH-zvHQATkEPpKbwVEDbCXTd3TIDEUwzyFq0klZmZ0271jqVJpGXhSHU3xUfVvVwEapuqYdwCmxkQn3k1Csg5nUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpTw73HMAuLlXYDAv6p0eDOtg8mz-omy3N5A-YgXoS9xaQWXzqjCV9nmGRGc8hTioVA7Ag1M028zPxBsEtQeO1o3gX1FoGIiKFF-1DLW6k27waJv5Nb3VyynFJdZC89-iXV_u1DmGwJKn8GkRGbOqT9sd7ZcXbvj72uOdgtQKbujN0WHXs2i8BCaQ6dl5Od-0vXId69OxJ9v6ADXjaBFR696qo_ahrtcgYrXCXlrmiukpz0eGTx1-950EJYMcxKdowtG5iYR7fvwp7qCAh-eCda9uhXxVC8zjCin4hu0D-OhJK0OAAzSDf-T5vPinlAMJuHkB1TxAxVPhL8Bn_jBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXLNI5PsHz5mdqGyUrujnmgXOYxWtABPex2ieCBTRwhwx1tivNubNalZfPNvisAV39SVV-j7qlVTFgnRPTanAVMyCTuZiqDmXewD0dAK_oxYE25Hwtr4ltX4SzO0b_PVbxnZkOo0_ytCIGaw0gAMA45Uh4TagKXiYCfnM0CYnRGQ-SJgX4agnHufuBbXvoWxJzUDXoCwN2OqEkmC6Mszzpkal2LO2abuwYUDnc3iuxFqK6zVN5LNpj15ihoyovg72iSptK8MjyQqE8q18ASSK7h-t2Sg51-AsTxrd9BGGVS2zmSkYULQT-4uVahTAMK7Alhan6vYXiLkay8XGVkHyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگر از حملات هوایی پاکستان علیه استان قندهار در افغانستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149071" target="_blank">📅 09:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149070">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وال استریت ژورنال: چین در طول جنگ علیه ایران، قطعاتی که در ساخت پهپادها و موشک‌های بالستیک مورد استفاده قرار می‌گیرند را برای تهران تأمین کرده
🔴
پکن تنها چند روز پیش از آغاز جنگ، ۳۰۰ تن ترکیبات شیمیایی به ایران ارسال کرده
🔴
در شش ماه نخست سال ۲۰۲۶، حدود ۱۳۰۰ محموله از قطعات دو منظوره از چین به ایران فرستاده شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149070" target="_blank">📅 09:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149069">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
انجمن داروسازان ایران: استامینوفن کدئین کمیاب شده؛این دارو اکنون به‌صورت محدود و سهمیه‌ای در داروخانه‌ها توزیع می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149069" target="_blank">📅 09:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149068">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5877224c5.mp4?token=m3xPvEyu-p6_e49Ha6TeuYjZ3yKhRleiUlQYoLQ37A-dMMulC6S_zuBrtDqgwATc53tj6zzMzVUJTM6K6MuVSDicCUKwCKSQTRCAbJg8bmkIAbcTe4d-i-mgXNRpL9GGUXZnQJ9hIeQLG6q_326FvZc-h4FMas4_aBOKyEKjvrf9LVuaEnr0brvFc5sUEkGMcfFk0C8lcVgGUIhMhi9AU-n2zBztnLxPQmYHB5aD5p-ez-mkak1Lc3HhqvWetTmtym-AyjYqV8rAfvXLb0KV2WuXSfC_2CgLaEmKWzFyfEVILGnGUjFgn1b9dAZtCP1c-8u6HFlRBeNWadnNYrHiWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5877224c5.mp4?token=m3xPvEyu-p6_e49Ha6TeuYjZ3yKhRleiUlQYoLQ37A-dMMulC6S_zuBrtDqgwATc53tj6zzMzVUJTM6K6MuVSDicCUKwCKSQTRCAbJg8bmkIAbcTe4d-i-mgXNRpL9GGUXZnQJ9hIeQLG6q_326FvZc-h4FMas4_aBOKyEKjvrf9LVuaEnr0brvFc5sUEkGMcfFk0C8lcVgGUIhMhi9AU-n2zBztnLxPQmYHB5aD5p-ez-mkak1Lc3HhqvWetTmtym-AyjYqV8rAfvXLb0KV2WuXSfC_2CgLaEmKWzFyfEVILGnGUjFgn1b9dAZtCP1c-8u6HFlRBeNWadnNYrHiWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از هدف قرار گرفتن یک کشتی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149068" target="_blank">📅 08:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149067">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeRnFLyFxBkFowlufSFkhuGDUbKoN4voviNhf1aCUFp-C8wmUnDp5arIHEWtZdztEhsNUAurnDG30oGUlVn92sz-dfd2UCR-1kT2Ukx8sTNWR_JAWXdNqK8FcLQ6F0tWoma0JdtNJpTJden8hIQXmb9wCIJBl6LS1SxuOxZVFMIQpfBLd34HCIXIrgZzfBiuTMgdnfCSRan26WEamz5a4hPRCZ8dbiFKVUjbIJZ__-jgL5oaa271fWHQO7x-wxIBSp7WgfyXQv0OQa3nhPXraoizRN1uZs66rCq9j8sVnZrqiogyM1L-YbtoA7_cTnCTe23iS4dT5MkCfIETeSxEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عراقچی و وزیر خارجه اوکراین در حاشیه مجمع عمومی سازمان ملل
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149067" target="_blank">📅 08:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149066">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dfdf05f7a6.mp4?token=bKBxl44Ol4F8p2w_nMTvGP91O7I5FeI5NbUyCsemqkxgAoKoz-F3REaAhp4jdjvOSAMN0cwgLFBPdBzH-7SyKdltEOffG9eX2M_tHrX2cBeNEc04o3NywT5-hyjscHGatfgRZCti3JSJRVH1eNByR8R68L8aDofxz2S4L06Tvzw2JDzQ4qY0mDhvFWxysA-kh_-6nJMRRKRxgmLlp7wrIxFOoKKUPjMskTGbK36Ph57mleKE9RdPeRGDKpesDQmpf8IoQttIq9RsrCs-sPdMGFWQMtn0PNSaOyz7zr2W9ecup1FZ_l05YJYNKatQQenI2nlg73MhAWqhrMDTcq2Pqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dfdf05f7a6.mp4?token=bKBxl44Ol4F8p2w_nMTvGP91O7I5FeI5NbUyCsemqkxgAoKoz-F3REaAhp4jdjvOSAMN0cwgLFBPdBzH-7SyKdltEOffG9eX2M_tHrX2cBeNEc04o3NywT5-hyjscHGatfgRZCti3JSJRVH1eNByR8R68L8aDofxz2S4L06Tvzw2JDzQ4qY0mDhvFWxysA-kh_-6nJMRRKRxgmLlp7wrIxFOoKKUPjMskTGbK36Ph57mleKE9RdPeRGDKpesDQmpf8IoQttIq9RsrCs-sPdMGFWQMtn0PNSaOyz7zr2W9ecup1FZ_l05YJYNKatQQenI2nlg73MhAWqhrMDTcq2Pqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی پاکستان به افغانستان
‏
🔴
جنگنده‌های پاکستانی در حداقل ۳ نوبت نقاطی در شهر و ولایت قندهار در جنوب افغانستان را بمباران کردند. شهر قندهار محل استقرار هبت‌الله آخوندزاده، رهبر طالبان، به شمار می‌رود.
‏
🔴
گفته می‌شود مجتمع ملا عمر، بنیانگذار طالبان نیز هدف این حملات هوایی قرار گرفته است. به گفته منابع غیررسمی، علاوه بر ولایت قندهار، ولایات پکتیا و خوست نیز بمباران شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149066" target="_blank">📅 08:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149065">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK0d8phGt2yTrQhBW5gRGkWU-831mCAh8m-l7EBNS2ohUrNqzCZAhqH5uAROTyeqqNhtOHksi6_chLQaXGKOHfXrz7Rf0rEVWjoEOdc06wnzAfO9XF0ywEhWv186Q-lzXxXU0xwtOp8xReLpKgB4ASnKEcTtnmiNO5FR0hf9_C3A-Oga5rPH3igCg4W3ezwmzZJa2xSJ5CP3IS2Gc2hAR4cKt55FyhtEBaZ1fPVX8ZMy0ppm_4Zvo3w8DzT-zHb-INFPDOKVImUIsjht-EVzqGkHDiWvJeZ9_7XXReSuUAITlB2UYRnHisUj4XauR89xmME4_cNa6MnvH2Ehly1sYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ اعلام کرد که با شی جین پینگ رئیس جمهور چین درباره ایران و بسیاری از موضوعات دیگر صحبت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/149065" target="_blank">📅 08:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149064">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fdf1eb3d.mp4?token=Lrsl8fr5OrPvFSehVK8ZUG7Cxl3vmEx4AugbW08HjjnW_TPZ2h5RW0HaB6X3fYmyxLV0Yns-BZKHL9QN-Ql32Z4C90BbMLv1KkzFBCnv1pW2BO63QwkDTU1PO9bPMCN8CuhzyIj91kB7bDUWrA8daMCVGvo063mcnBV2JM0Jopi-j78SzLkusOPjEJv0lPBLaAzyF55IOiiTdPDwKAN_99elcXebKcPoFaYFrc4H5nIiKFJ9yJpQexpc_GUU1-Eviu12Z8TMNj00YXdZ2g5-mizdZi1MKfqo6db8_j1NIw8VBay4MLF-3AgKvlgEC0SMGDzHBPiQPnWNMp7wIlvyRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fdf1eb3d.mp4?token=Lrsl8fr5OrPvFSehVK8ZUG7Cxl3vmEx4AugbW08HjjnW_TPZ2h5RW0HaB6X3fYmyxLV0Yns-BZKHL9QN-Ql32Z4C90BbMLv1KkzFBCnv1pW2BO63QwkDTU1PO9bPMCN8CuhzyIj91kB7bDUWrA8daMCVGvo063mcnBV2JM0Jopi-j78SzLkusOPjEJv0lPBLaAzyF55IOiiTdPDwKAN_99elcXebKcPoFaYFrc4H5nIiKFJ9yJpQexpc_GUU1-Eviu12Z8TMNj00YXdZ2g5-mizdZi1MKfqo6db8_j1NIw8VBay4MLF-3AgKvlgEC0SMGDzHBPiQPnWNMp7wIlvyRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی با همتای پاکستانی خود دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/149064" target="_blank">📅 08:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149063">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=Mn7sWAb_KQwNB0aXjucDWAfT4m3FZAenGPxm6wDHRar1SQSZMw3P8l0jx8zRMGEF-T5Chv9lnoikxEGMJyyxYkdpoS9SD0ZfJFd1Q68XcbgQBLWUJ8GSX7Q682XfjWUyJ1qZjLjrGQ9wxsFEJYTYYqO-2A6AkCwqinZ_XGVhdrh01D3o2WMPD8x-wMuOPDjqwHbNWKAL91yTgbnSgkCacQwdjGiimNUwdaEkcE-QB6IzGKKDlRRyBNoVsiDkx5-n35_Rmu3fqvQBV9HYDETh9WVu0Ov7L2dIFxRConq9jjf03p0xqmW5NKTvvGqAL4yuZmAgpi4Y0hyRBlMtGgLZAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=Mn7sWAb_KQwNB0aXjucDWAfT4m3FZAenGPxm6wDHRar1SQSZMw3P8l0jx8zRMGEF-T5Chv9lnoikxEGMJyyxYkdpoS9SD0ZfJFd1Q68XcbgQBLWUJ8GSX7Q682XfjWUyJ1qZjLjrGQ9wxsFEJYTYYqO-2A6AkCwqinZ_XGVhdrh01D3o2WMPD8x-wMuOPDjqwHbNWKAL91yTgbnSgkCacQwdjGiimNUwdaEkcE-QB6IzGKKDlRRyBNoVsiDkx5-n35_Rmu3fqvQBV9HYDETh9WVu0Ov7L2dIFxRConq9jjf03p0xqmW5NKTvvGqAL4yuZmAgpi4Y0hyRBlMtGgLZAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز یه بمب افکن b1 هنگام استقبال از شی
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/149063" target="_blank">📅 01:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149062">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099168c283.mp4?token=myaZAyYdnvnyGEmXgwXClHQn3elh0_iOQyzIPGGQm1gGF4ZH-zPHU5PCalgEVrDQiRYE7Z5EwD2IvC5VvCd0xfDs8_YOH544cHcFToTlC7dMTygAm2eh7LtiMMUtjEhMjDzdoMIaQs25Vwlvpaisrairu7SKnNpY5bNFrmMZ1bVirFFA3-Y_IgMShGmqMlhwRm_leBlVANBsKcSTLi8KxAOsy2is1Y8l9nEFlWiG8DNr8R_1ZiWY9pnRTlZz5eddb-cx5MS63PjWDbnjLBp5lLorpM22kxlqc4NL1GygPm0DxFHL0796IlNBzHNKJW7tDGIhDUaNNk58aB8fJ115Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099168c283.mp4?token=myaZAyYdnvnyGEmXgwXClHQn3elh0_iOQyzIPGGQm1gGF4ZH-zPHU5PCalgEVrDQiRYE7Z5EwD2IvC5VvCd0xfDs8_YOH544cHcFToTlC7dMTygAm2eh7LtiMMUtjEhMjDzdoMIaQs25Vwlvpaisrairu7SKnNpY5bNFrmMZ1bVirFFA3-Y_IgMShGmqMlhwRm_leBlVANBsKcSTLi8KxAOsy2is1Y8l9nEFlWiG8DNr8R_1ZiWY9pnRTlZz5eddb-cx5MS63PjWDbnjLBp5lLorpM22kxlqc4NL1GygPm0DxFHL0796IlNBzHNKJW7tDGIhDUaNNk58aB8fJ115Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال ترامپ از شی
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/149062" target="_blank">📅 01:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149061">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
تانکرترکرز گزارش می‌دهد که نزدیک به ۶ میلیون بشکه نفت خام توقیف‌شده جمهوری اسلامی ایران، به‌صورت مخفیانه در حال انتقال به ایالات متحده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/149061" target="_blank">📅 01:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149059">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijbXyOfNnLx2Iel1BwoT6OuFcES83JOQHZFF_ItYnaFvWTx7oDN9jsx18pcFZVk9Z9RCj1ZwMkV_bpywZFHxpAnDs4z1inh5tcBZASgSpQS3rnbz1l9Hkh-zI3VsZrdtpG-kkGRJyGP7SBvxP88HzDpUjxGtxyQ3bwnZJFIRzr1SYiAHf4N4SO1HRLjQMi91NJdPh3HnjyOUAZFeUg2btgGv2PmoUqQzHpeXOM80BHLJTVtOuLer1s5cPRJXGdzZeRQD-Lt_CuB-PZMOkt6tKNfb1UB8CPOKR5MXdQN0cqPXuj3uTFhuUe7Lp_RffMSwiFRPNqlgH7u0xg-dp7fD0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tz4n6t02c4hdVY2_U3bVSRmvrQsCIZ16EZAoTosfIxsGDMypzx7wwJ3ci4pXGJNe-1v8AZZFWrrad1o0YwyjTMSjuaRZylcHF4X9TmILiVqM-PH6jfegjHgL_Y0JwJT73QzDjnTSjVuiC1XUI4iR_y9wEiapLZ4K6iAFuG0t9VKGLwH-4osCAd5ujure0xbgfk3swatc9j8XwPs3Kx0nlz4SNDp6BnOh1KvWrXUhagpJKDksi6cF4r_2VeBJXdwoTTKDrVYGmm0U4fqY78osNRSh8zmS35cwFKrOQlLdpD0CeWY_dWi1XPbilVAVABRhu_-Sijqck6hkmXsjZ8w0TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فیلد مارشال: زیر دریایی آمریکا رو مهندسی معکوس کردیم و تا ۶۰۰۰متر میتونه زیر آب بره
🔴
پ.ن: میانگین آب اقیانوس‌ها ۳۷۰۰متر هست و تنها گودال ماریانا و جاوه بالای ۶۰۰۰متره که اونم خیلی از ایران دوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/149059" target="_blank">📅 01:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149058">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNxUWpbA2JiU78Z-lEY8d8Ic-Yw2i_UyqKlqCcYbs5YTmNAXJ-DbPH-EcpG54YckCJtRa7JoGFb72zCbYFbVeSh9gz6tLWqkT_XvJozgfmZsGbcComV_ZtqibhefETiz0XK6qFPlONRdOxeIGTUX_wZOWHPoPsJdWw0Re9KIyp-GB5GgKA4B9_xan3oLL-ZN-9mc_MTCH13IKITzgQDPAZFeo7JkxAdYGWDq06ud9PwJ6YHQlfKdsWBgZNiORTSJtLtTk8XqlvWRosdKk4mJF2jh1YkX349k6MIj-sm-GvVQOFC48Lx9m5UnRby0F5lrhfjTYDY92ciuOs7Byuac4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: جنگ‌های آتی ما و آمریکا تو فضا انجام میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/149058" target="_blank">📅 01:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149057">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sKEVHdOssvGXsJeJhWJ63e1DY9OzvMaUVcLMHGTPLoxQFiDEyokc6N47B7cpAvYDsqF7wJEDFC_NHVjio1n8KcthyXIWtMY66i0mNOmuyk1sJmbu8kLAOs8mUc_fdi1YkJmE-s6P5dAezDVJUnLnYAaU0dpYJMRcSXzxS9Bwrhs-mYLAT6nX6kgazJ-PmjaDtBtU7WPnIzVXJeTRxp_HuzSSV4OSs0ldvXAqssPNWjDGvNUAfAGvuY6uqTSC_tqUHWwAToQ2k6l60FwMxrR14UyQKCRmAsDOZS7SUL2pSRM0UtomHFjTDBeR41limKMXUAe0FgiPJpScy3oIaElw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: اگر کشورهای خلیج فارس جلوی پروازهای ایران رو بگیرن، ایران فرودگاه‌هاشون رو با موشک باران تعطیل می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/149057" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149056">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
گزارش‌ها از شلیک موشک کروز به سوی تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/149056" target="_blank">📅 00:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149055">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
صدای انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/149055" target="_blank">📅 00:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149054">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99cb34213.mp4?token=PlOQetzB2cW8QaJYinixIE2bIIsijpdcpDzUirhkQ-3QcLEybqw3RewEzwCVR169X0l704D81EZsnf_FWLQyg-p3TrMpyodq3aOWTeCpjkRjgfEHf7aWqJkpoEOtQrmb69ovnoUHfX_a_Ksd8-t2fwwrxQFg_eEx8BgsJ2jQqpK6c6yFiHJXnwkspVrEBYxMO5foli3ZnK7OQmN7tJYpOZRicJZxrOZptJjoQNuwdr0RGgJTaVsF_oA3xZuWGTyLO1QS5f4pZpcJ0D8Jy-SmP_RiZINmlbxPYYno3kdZkHlWDETKQOPVpRsK-_GdePMppG07cgKnYTY4AA7ftuW56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99cb34213.mp4?token=PlOQetzB2cW8QaJYinixIE2bIIsijpdcpDzUirhkQ-3QcLEybqw3RewEzwCVR169X0l704D81EZsnf_FWLQyg-p3TrMpyodq3aOWTeCpjkRjgfEHf7aWqJkpoEOtQrmb69ovnoUHfX_a_Ksd8-t2fwwrxQFg_eEx8BgsJ2jQqpK6c6yFiHJXnwkspVrEBYxMO5foli3ZnK7OQmN7tJYpOZRicJZxrOZptJjoQNuwdr0RGgJTaVsF_oA3xZuWGTyLO1QS5f4pZpcJ0D8Jy-SmP_RiZINmlbxPYYno3kdZkHlWDETKQOPVpRsK-_GdePMppG07cgKnYTY4AA7ftuW56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله به نسیم شهر تهران در جنگ ۴۰روزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/alonews/149054" target="_blank">📅 00:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149053">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
صدای انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/alonews/149053" target="_blank">📅 00:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149052">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سم آلتمن مدیرعامل شرکت OpenAI در نشست سازمان ملل گفت: هوش مصنوعی می‌تواند تصمیماتی بگیرد که انسان‌ها دیگر قادر به درک یا کنترل آنها نیستند. در این شرایط لازم است که به شدت مراقب باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/149052" target="_blank">📅 00:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149051">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پزشکیان از نیویورک خطاب به مردم: دعا کنید ناامیدتان نکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/alonews/149051" target="_blank">📅 23:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149050">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سی‌ان‌ان: پسر سفیر اسرائیل در ایالات متحده، در جریان حمله در کرانه باختری، به شدت مجروح شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/149050" target="_blank">📅 23:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149049">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a34e6892.mp4?token=YhKL0ecfD-zysr1WXh9hL-G4iaQ488XDcdzX8-1n3Zzdw4HDnUSGviwnVl1ukw7SNu-ZbYEE7TPHhqEON4ZDN90Xg_gg64Yn23s2kjzNjCC0tTfF5qx36eV1gzqSHLTNWQjCdGB-QKowx03JCy82rgXyieXWucxrq8vwF-8JC9FY2DcrwqKTDTqWcGTStd9P90zQNfVUL8EaXpyJOZh_RiZG7imZziD0w0af_-Mzj3eDxbHR82Gy0gZ7OPDMwRdQUaFtk0aRrj0yVwToTLwPC9ngcUtv1eInmC4Er7DQvmv-Dkc8Xqi9krDGKHTN4ZJ3sOhI1fU7IYeJFpt2UVQfqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a34e6892.mp4?token=YhKL0ecfD-zysr1WXh9hL-G4iaQ488XDcdzX8-1n3Zzdw4HDnUSGviwnVl1ukw7SNu-ZbYEE7TPHhqEON4ZDN90Xg_gg64Yn23s2kjzNjCC0tTfF5qx36eV1gzqSHLTNWQjCdGB-QKowx03JCy82rgXyieXWucxrq8vwF-8JC9FY2DcrwqKTDTqWcGTStd9P90zQNfVUL8EaXpyJOZh_RiZG7imZziD0w0af_-Mzj3eDxbHR82Gy0gZ7OPDMwRdQUaFtk0aRrj0yVwToTLwPC9ngcUtv1eInmC4Er7DQvmv-Dkc8Xqi9krDGKHTN4ZJ3sOhI1fU7IYeJFpt2UVQfqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دوسی، خبرنگار فاکس‌نیوز: اولویت اصلی و مطالبه شماره یک رئیس‌جمهور ترامپ این خواهد بود که چینی‌ها ارائه اطلاعات به ایرانی‌ها را متوقف کنند؛ اطلاعاتی که آنها از آن برای هدف قرار دادن منافع آمریکا استفاده می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/149049" target="_blank">📅 23:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149048">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a31482c0f.mp4?token=ZFgp_8jdYau_2vEmT_T14PzAIcGnffarwqeZqGyehclVlUBmuwPDihjDF4AcVDVsfr4xEuFzHyXm6O75qEIJ_2rsET4yVKcvA3EjgB_wf5sarjMFwy2h0HHRN-J8zA0P1FOWY2nGKiz0vQZAXXv942NnIVsNv1FIg8j_XtB58a_4DgvNAIF8FuQ991G9FgQ6-EbOcyCZOSrN9UuuIYij3rclJYsKYmu2i0RoKsJvLFZXzQEQjOxhGZcB15HNX7WNZK5JIDR3sAFftwLw4DEp8Tohct8SoSMWg-vUEcTfVLH-Vuxd-92v1iEXxh_jWDerQccCBN7NMANAvHM_dg8Uqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a31482c0f.mp4?token=ZFgp_8jdYau_2vEmT_T14PzAIcGnffarwqeZqGyehclVlUBmuwPDihjDF4AcVDVsfr4xEuFzHyXm6O75qEIJ_2rsET4yVKcvA3EjgB_wf5sarjMFwy2h0HHRN-J8zA0P1FOWY2nGKiz0vQZAXXv942NnIVsNv1FIg8j_XtB58a_4DgvNAIF8FuQ991G9FgQ6-EbOcyCZOSrN9UuuIYij3rclJYsKYmu2i0RoKsJvLFZXzQEQjOxhGZcB15HNX7WNZK5JIDR3sAFftwLw4DEp8Tohct8SoSMWg-vUEcTfVLH-Vuxd-92v1iEXxh_jWDerQccCBN7NMANAvHM_dg8Uqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید پتراوس، مدیر سابق سازمان سیا:
مقامات غربی تخمین می‌زنند که روسیه در حال حاضر هر ماه ۶۰۰۰ نیروی انسانی بیشتر را از دست می‌دهد تا اینکه نیرو جذب می‌کند، و این موضوع تا حدودی توضیح‌دهنده گزارش‌هایی است که حاکی از آن است که ژنرال‌های روسی خواستار بسیج بیشتر در چند ماه آینده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/149048" target="_blank">📅 23:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149047">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
گزارش ها وقوع چندین انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/149047" target="_blank">📅 23:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149046">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
به گزارش NBC News، مسائل مرتبط با نظام سلامت در آستانه انتخابات میان‌دوره‌ای ۲۰۲۶ به یکی از چالش‌های سیاسی جمهوری‌خواهان تبدیل شده است.
🔴
دموکرات‌ها امیدوارند با تمرکز بر موضوعاتی مانند هزینه‌های درمان و سیاست‌های بهداشتی، در انتخابات پیش‌رو کنترل مجلس نمایندگان و سنا را به دست آورند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/149046" target="_blank">📅 23:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149045">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
کرملین از دعوت آمریکا از ولادیمیر پوتین برای شرکت در نشست گروه ۲۰ استقبال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/149045" target="_blank">📅 23:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149042">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZvjdymDnYqsU1wVTBuZxJ_yRjCyM9B2Zz1UDLDUB3_30X4gyYp7GHDyQEFTNqdP582FznDFwULj9GJ1i9CbM-lOMByuAtoJSqf3RhnXoVnv-_7VC5RFxipYbdHjb-0xSQTJ-UehrO_h1cxYdQn5gsLJFMO2MngZBDEI9upZosqaB2ZR7SDMMfZB-wpVBmzHEpxRsiW6f2TKyDzRMW84kcHGM1Ti0CCPnc5eeKwurrlWOHJr8zZtJ0pEBiN_TeaQugJWfflhBxLx7NPDoZDf-lTiV1YTfjW0hJf0ceRk19ef2qBGKuGI1X1qPideXyk2BIGErQH7zoLWYQAT-WjVAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5UHeTkbGNR6N2SqPQ1GmgRZqjZcAG0jYNZhglpDVIwSOGqhWQ79rxkGKKS2imYsuc2LJruqITapDtVpmNaaax_Fc_yny8Bc1lzaSWGAf6Ktp3XJrLnluh63P3jtd0w5GS-FPISmQje4cTsr_6a9ErLf0hdr2mhptvgvWpCiwsuDZkQpWaYgstXihcgk7CXpJUBo0u05kEcvAPpSvTeTl3RKrQAZ1vGEzxSh6rOcXrVMfmTxK-a6bg74EZq6DFCyrWV5H6Il2fJJMQJL8Nf2j_CnoU3LWXQqRqUwhJYbCQSaayvx_N_c6zh5VNW9XbgeVKlPl7xuXR_h45IywoPlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzSO_dEInLh5jMtsaCBFneBiheToMeJESSjVWe-E9ae9LjAWD44JYnb_rNn_XMjL50l5lMhbsPlGlLZygRcczVEVIV7g4fucvKbW6l1EPo6mM1foSJQa2OeYgPob1zLT2wyPwDtbaPIs9FiN6ej3NHUrcxyIJyyrfYN8GZe5ABkm2SLADgq0qGBQEXovZy6ZC36SYE3mt4xZZSyD_uoAguaUvG6E5sTbnZyLaPdrPDfIqspvlJIikfK4CLyMQfiXuTDsauNTKJSAYW8-pKRdC1865g6hVd-bSVGeaZQsjbm-D7F9jQuwrC7D4Y-iNg7TKC9ts1_kVhUyDGXZs7RbUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای ترابری انگلیسی از نوع C-17 حامل تجهیزات نظامی در پایگاه هوایی طائف فرود آمد
🔴
همزمان، هواپیماهای جاسوسی و سوخت‌رسان انگلیسی در قبرس مستقر شدند و ۳ فروند هواپیمای ترابری کویتی نیز از اسلواکی در پایگاه هوایی خمیس مشیط فرود آمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/149042" target="_blank">📅 23:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149041">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8ba758d8.mp4?token=CEljx5HVaRqWPKP6aX6Xd17cbxYlVIdp1u-suqAVoOMDXr3qS-PAqGhQvyqDBullwh_g_BwqnmmWdtYkFNgDGn2gXb0QxKd5z8e5ZKlpG6U3-tFb67FtWAtgXqJ6M6xa076ZximjrSeNelJuGOsE0P83m2HtIDa8BKL9peg6DeDK5uoJmFBBWoPHWkL7iG6qNCSxDD9k4GjHqzpgPlq8XIpdZ5n7-t5TBiBbZFFVUGulgVCdtCAwGARLKZtzDm0Di8LBQyz1ZYaCoFuFDjmy1UtKLiG4OaQz-QIqzsdgu5F8Gyxj89BsrtTRGHcz8JSi_VEv_QXuGXX_VzFN8RzYqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8ba758d8.mp4?token=CEljx5HVaRqWPKP6aX6Xd17cbxYlVIdp1u-suqAVoOMDXr3qS-PAqGhQvyqDBullwh_g_BwqnmmWdtYkFNgDGn2gXb0QxKd5z8e5ZKlpG6U3-tFb67FtWAtgXqJ6M6xa076ZximjrSeNelJuGOsE0P83m2HtIDa8BKL9peg6DeDK5uoJmFBBWoPHWkL7iG6qNCSxDD9k4GjHqzpgPlq8XIpdZ5n7-t5TBiBbZFFVUGulgVCdtCAwGARLKZtzDm0Di8LBQyz1ZYaCoFuFDjmy1UtKLiG4OaQz-QIqzsdgu5F8Gyxj89BsrtTRGHcz8JSi_VEv_QXuGXX_VzFN8RzYqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خاویر میلی، رئیس‌جمهور آرژانتین:
اگر نتانیاهو نبود، تردید دارم که اسرائیل امروز همچنان وجود می‌داشت، و این یک خطر واقعی نه تنها برای اسرائیل، بلکه برای اروپا و کل غرب خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/149041" target="_blank">📅 23:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149040">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
عمان: خدمه یک کشتی تجاری هدف قرار گرفته را تخلیه کردیم
🔴
یک خدمه جان باخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/149040" target="_blank">📅 23:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149039">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سخنگوی سپاه: پزشکیان امروز پیام قدرت را از قلب نظام سلطه بازتاب داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/149039" target="_blank">📅 23:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149038">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG1R6a2G-Q7qDldNbdw36-w8WrIfsbNPgULB7ej2yl2AdAFuT-SwnGdGEmWlMmngAj0vrKqS7hPYUy2eiaM3FDcjEO_NJv8Jp1Iv_WojrjiLg2s5iUaa08qeyVDAp-3JAp3-anriQvL8o3RyuhHwKokpR820aAjREGMjn3eucMTctjlwwTsjNCnhHtN7w3tVNb3QFRA3Vl1svoFkqgCyruj9_2wzJrtAKN8yDJBXq7RwsTzFnb_NGm9wuN_rE5s_MZl8y7Q8scHC844WczWkl0ReEwQwCUASKVLqwQ9ufOsK7yIdHfd-UcjAXpOgGmj4YDDNPSeYekHg6TKWjsdEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش ۴ درصدی قیمت نفت پس از سخنان محسن رضایی مبنی بر حمله به فرودگاهای منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/149038" target="_blank">📅 22:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149037">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری / شلیک موشک به سوی کشتی‌های متخلف در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/149037" target="_blank">📅 22:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149036">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
زلنسکی در مجمع عمومی سازمان ملل: روسیه با پهپاد های شاهد و تکنولوژی ایرانی نمی‌تواند ما را تسلیم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/149036" target="_blank">📅 22:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149035">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UF2MS99iVjCbXLopkWIF2X-fvPN-kPVGLciUIdScOumcw7sUYig9v8__BDZNJ3oLQG3YUJ4iaZfS1IzArsRvSAPX_wfX5stBbx7ojtO635g_p-n-kX1b78G0SLNMtvg74F5k3BpyAwfh4BZ18UsDsW8H2GsFqhpUz-e___K433MAQy-3csY6xHrXO-rBlHTNkWCMt-Pd9Mb-Le0oVDaC76emO7hy5TTU7oWHYK4k6M8fPpRwh4AhSdWHMPOrWYBqYtmhuouN486XYn1e6mzmODLl_y_wfLCJS4OU9-_3AjcPvE3WN9FGJEeyXBqAev5_NQ1RYpClmraYJs9v3qSGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز:
ایران تهدید به فلج فرودگاه‌های همسایه کرد
🔴
ایران تهدید کرده اگه همسایه‌ها پروازهای ایرانی رو قطع کنن، فرودگاه‌هاشون رو فلج می‌کنه. این تهدید تازه‌ست و می‌تونه تنش‌ها رو تشدید کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/149035" target="_blank">📅 22:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149034">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
دولت ترامپ: فعالیت سه رسانه تهدیدی برای امنیت ملی است
🔴
به گزارش USA Today، وکلای وزارت دادگستری آمریکا در دفاع از ممنوعیت فعالیت CNN، MS NOW و پولیتیکو در کاخ سفید استدلال کرده‌اند که نحوه گزارش‌دهی این سه رسانه می‌تواند تهدیدی برای امنیت ملی ایجاد کند.
🔴
این استدلال در جریان پرونده قضایی مربوط به تصمیم دولت ترامپ برای محدود کردن دسترسی این رسانه‌ها به کاخ سفید مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/149034" target="_blank">📅 22:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149033">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
احتمال صدای انفجار کنترل شده در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/149033" target="_blank">📅 22:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149032">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
تحریم‌های جدید کانادا علیه ایران
🔴
وزیر امور خارجه کانادا: امروز کانادا تحریم‌های بیشتری را تحت مقررات اقدامات ویژه اقتصادی علیه پنج فرد و پنج نهاد ایرانی اعمال می‌کند.
🔴
دلیل  این تحریم‌ها «حقوق بشر و خشونت غیرقانونی» ذکر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/149032" target="_blank">📅 22:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149031">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
هیمتی: در حد توانمون تورم رو کنترل می‌کنیم باقیش رو هم هرچی خدا بخواد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/149031" target="_blank">📅 22:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149030">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
جزئیات مذاکرات ایران و آمریکا در سازمان ملل/ آمریکا رفع محاصره دریایی ایران را نپذیرفت
🔴
مذاکرات ایران و آمریکا در حاشیه مجمع عمومی سازمان ملل با میانجیگری قطر انجام شد. در این رایزنی‌ها، استیو ویتکاف و جرد کوشنر از طرف آمریکا و عباس عراقچی از طرف ایران حضور داشتند.
🔴
اسماعیل بقایی، سخنگوی وزارت امور خارجه، گفت هدف این تعامل، انتقال شروط ایران از جمله پایان جنگ، توقف اقدامات نظامی آمریکا، رفع محاصره دریایی، پایان فشار اقتصادی و آزادسازی دارایی‌های ایران بوده است.
🔴
با این حال، بر اساس گزارش العربیه به نقل از یک منبع آمریکایی حاضر در مذاکرات، واشنگتن درخواست ایران برای لغو محاصره دریایی را نپذیرفته و اختلافات میان دو طرف همچنان پابرجاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/149030" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149029">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">صید یک ماهی عجیب در دریای بالتیک  [@AloTweet]</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/149029" target="_blank">📅 21:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149028">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt_R1-X2pMqKcJUE9RV1fDYQsnc4gF9VK7KBCIx2MIRi5lM_bIZDwPRQmQGdLSVXD741Zpqhan8_nb4lbfgMQJNoS4MHvk5HNzqZ0Xyd92Zm8aDYG7OQlpYrBR0kb96VeBvsJLVMIu1Gv1iBIGY6gXX8ImOM4DvwSIZ3HOCB1gD1-XWPG-7nMh0J7Db2PmhOD79B8KryWaGnow4904X48AnUgSXix-Bxkf3dS9zKhuN-E2FljrVng2Cil7gfnLWgAOjOP8TJx9tzgMpyVbJphqQS2wyo9Q8mVmlwQJuOMR9a1RjncKAAaiiVBDHrdKMadUNzkYNp86Juf83MCa01hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش روبیو به سخنرانی پزشکیان: کسانی که ده‌ها هزار معترض بی گناه را میکشند حق حرف زدن درباره منشور سازمان ملل را ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/149028" target="_blank">📅 21:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149027">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
زلنسکی: امسال به طور میانگین هر ماه ۳۱ هزار تا روس رو توی جنگ کشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/149027" target="_blank">📅 21:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149026">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfa61ab86.mp4?token=ptc1MeyJX4Zb-KzfBJHsAj67AAB8TyqxXWj08Ec66KYb1lw8NcIm3RueS0zYy3RUl4-jwXCYZA_i5BdA_cYIRMOZPbniThu5YMnuQSm5miL676XrJROXwQdaas57oVMAki3TFmv3yUfIXXPolrGegZfVLWxwjnPM6UTrVjq654FyOTf2Rdhlbr87Ej6jbwT9hRAEOFNpIxIJ6axc762qKduR9U1mUIMazSFsM92-Um8St0Ajb2_GTFxQ-0EJBLUGYGIWoPR4IsZHPaIzmc0LDFG2kewLiVRRAyEtLVxWD2YHVllijXIOm70meEX5D0Cq6CRujulqQWrzO0EBk3lDvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfa61ab86.mp4?token=ptc1MeyJX4Zb-KzfBJHsAj67AAB8TyqxXWj08Ec66KYb1lw8NcIm3RueS0zYy3RUl4-jwXCYZA_i5BdA_cYIRMOZPbniThu5YMnuQSm5miL676XrJROXwQdaas57oVMAki3TFmv3yUfIXXPolrGegZfVLWxwjnPM6UTrVjq654FyOTf2Rdhlbr87Ej6jbwT9hRAEOFNpIxIJ6axc762qKduR9U1mUIMazSFsM92-Um8St0Ajb2_GTFxQ-0EJBLUGYGIWoPR4IsZHPaIzmc0LDFG2kewLiVRRAyEtLVxWD2YHVllijXIOm70meEX5D0Cq6CRujulqQWrzO0EBk3lDvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید حدادیان، مداح: مجتبی خامنه‌ای امام ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/149026" target="_blank">📅 21:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149025">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">💢
قیمت دلار و طلا منفجر شد</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/149025" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149024">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
زلنسکی: فقط یک نفر علناً طرفدار ادامه این جنگ است
🔴
من هیچ‌کس را نمی‌شناسم که علناً طرفدار این جنگ باشد، جز یک نفر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/149024" target="_blank">📅 21:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149023">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6137406465.mp4?token=FpMNygRQKAubzlRJtPm3iy_21bPm_kTWL-E8iX-7P81HpFvh5FIF8TW1x3lEvtJQZnGrZHKdnXk-Ab870a7R_rZJKno0Z8Yty2PGbmWXtAm162QSsyP6wJisjCM-dVfrjJBURJ0f65Te1PcX8_WS1VbOMxJx-MV9VZ6FLFI5yvRbgQmKNdHr_lT_HqWPdiZtqnFdQvduKqEa0otAjDdoeMkXg-nMezOoOZoq7oz5_uvYhPg4kk-woCI5LpJ_z4CCmtmdYfeSF8gVr26Jr-3mxp0vt5JJJgXIuaXeZGbHUM7LK0RtaYLm6cq7I98TYgtAxqgHmo7coe9cuN3YM8-cNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6137406465.mp4?token=FpMNygRQKAubzlRJtPm3iy_21bPm_kTWL-E8iX-7P81HpFvh5FIF8TW1x3lEvtJQZnGrZHKdnXk-Ab870a7R_rZJKno0Z8Yty2PGbmWXtAm162QSsyP6wJisjCM-dVfrjJBURJ0f65Te1PcX8_WS1VbOMxJx-MV9VZ6FLFI5yvRbgQmKNdHr_lT_HqWPdiZtqnFdQvduKqEa0otAjDdoeMkXg-nMezOoOZoq7oz5_uvYhPg4kk-woCI5LpJ_z4CCmtmdYfeSF8gVr26Jr-3mxp0vt5JJJgXIuaXeZGbHUM7LK0RtaYLm6cq7I98TYgtAxqgHmo7coe9cuN3YM8-cNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشت پهپاد که امروز توسط طالبان افغانستان به سمت پاکستان پرتاب شده بودند، سرنگون شدند.
🔴
در این حمله از مهمات سرگردان، پهپادهای انتحاری و کوادکوپترها استفاده شده بود، اما هر هشت فروند سرنگون شدند.
🔴
گفته می‌شود تمامی این پهپادها در مناطق کوهستانی خارج از کوهات و در نزدیکی تورخم در ایالت خیبر پختونخوا پاکستان سرنگون شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/149023" target="_blank">📅 21:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149022">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کانال ۱۳ عبری: نتانیاهو امشب اسرائیل را ترک می‌کند و فردا صبح به نیویورک می‌رسد و فردا شب بلافاصله پس از سخنرانی در سازمان ملل به اسرائیل باز خواهد گشت.
🔴
نتانیاهو به دلایل امنیتی ویژه در خاورمیانه، حتی یک شب هم در نیویورک اقامت نخواهد کرد و فوراً به اسرائیل بازمی‌گردد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/149022" target="_blank">📅 21:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149021">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
محسن رضایی: هر کشوری حریم هوایی خودش رو به روی ما ببنده، فرودگاه اون کشور رو نابود می‌کنیم؛ اون‌ها هم دیگه نمی‌تونن پرواز داشته باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/149021" target="_blank">📅 21:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149020">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پزشکیان امروز غیرمستقیم گفت که معترضان دی ماه، مزدور مسلح شده توسط آمریکا و اسرائیل بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/149020" target="_blank">📅 21:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149019">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏
👈
بقایی:
بله دیروز با آمریکا حرف زدیم و براش شرط گذاشتیم جنگو محاصره و فشار اقتصادی رو تمام کنه، پولامونم آزاد کنه، تنگه هرمز هم دست ما باشه و یه دور هم به ما بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/149019" target="_blank">📅 21:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149018">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فارس: پزشکیان در نیویورک در هتل مستقر نشده است
🔴
پزشکیان در سفر به نیویورک به‌جای هتل، در محل اقامت نماینده ایران در سازمان ملل (رزیدانس) مستقر شده است
🔴
این اقدام با هدف کاهش هزینه‌های سفر، برای اولین‌بار توسط یکی از رؤسای‌جمهور ایران انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/149018" target="_blank">📅 21:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149017">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر نفت: پول نفت‌هایی که فروخته‌ایم درحال وصول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/149017" target="_blank">📅 21:07 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
